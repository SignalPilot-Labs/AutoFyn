"""StreamDispatcher — route sandbox SSE events to handlers.

Pure logic: consumes one event, mutates the RunContext, returns a
StreamSignal telling the session runner what action to take. No
asyncio.wait, no inbox, no sandbox interaction — those belong to the
runner. The StreamSignal dataclass lives in utils.models.

After SSE consolidation, the dispatcher also writes tool call and
audit event records to the DB (previously done by sandbox POSTs).
"""

import logging
from collections.abc import Awaitable, Callable

from agent_session.tracker import SubagentTracker
from utils import db
from utils.db_logging import log_audit, log_audit_idempotent, log_tool_call_idempotent
from utils.constants import (
    LOG_PREVIEW_LIMIT,
    STREAM_EVENT_MESSAGE_DELTA,
    USAGE_COST_KEY,
    USAGE_EMIT_INTERVAL,
    cost_per_cache_read,
    cost_per_cache_write,
    cost_per_input,
    cost_per_output,
)
from utils.models import RunContext, StreamSignal

log = logging.getLogger("session.stream")

EventHandler = Callable[[dict], Awaitable[StreamSignal]]


class StreamDispatcher:
    """Dispatches sandbox SSE events. One instance per round.

    Public API:
        dispatch(event) -> StreamSignal
    """

    def __init__(
        self,
        run: RunContext,
        round_number: int,
        tracker: SubagentTracker,
    ) -> None:
        self._run = run
        self._round_number = round_number
        self._tracker = tracker
        self._rid = run.run_id[:8]
        # Snapshot everything at round start so running cost estimates
        # during this round only measure THIS round's delta — prior
        # rounds' cost and tokens are already accounted for in run.*.
        # None when no prior round reported usage, which is distinct from a
        # prior round that cost exactly 0.0.
        self._cost_baseline: float | None = run.total_cost
        self._input_baseline: int = run.total_input_tokens
        self._output_baseline: int = run.total_output_tokens
        self._cache_create_baseline: int = run.cache_creation_input_tokens
        self._cache_read_baseline: int = run.cache_read_input_tokens
        # Gateway-reported cost accrued this round. None until the gateway
        # reports at all: a gateway that bills 0.0 is telling us the round was
        # free, which is not the same as a gateway that never reported.
        self._round_gateway_cost: float | None = None
        self._message_count: int = 0
        self._latest_context_tokens: int = 0
        self._tools_in_flight: int = 0
        self._sandbox_session_id: str | None = None
        self._dispatch_table: dict[str, EventHandler] = {
            "assistant_message": self._on_assistant_message,
            "stream_event": self._on_stream_event,
            "tool_use": self._on_tool_use,
            "tool_done": self._on_tool_done,
            "subagent_start": self._on_subagent_start,
            "subagent_stop": self._on_subagent_stop,
            "audit": self._on_audit,
            "rate_limit": self._on_rate_limit,
            "result": self._on_result,
            "end_round": self._on_end_round,
            "end_session": self._on_end_session,
            "end_session_denied": self._on_end_session_denied,
            "session_end": self._on_session_end,
            "session_event_log_overflow": self._on_session_event_log_overflow,
            "session_error": self._on_session_error,
            "mcp_warning": self._on_mcp_warning,
        }

    def set_sandbox_session_id(self, session_id: str) -> None:
        """Set the sandbox session ID for idempotency key construction."""
        self._sandbox_session_id = session_id

    def has_tools_in_flight(self) -> bool:
        """True if any tool call is currently executing."""
        return self._tools_in_flight > 0 or self._tracker.has_tools_in_flight()

    def has_active_subagents(self) -> bool:
        """True if any subagents are currently tracked as active."""
        return self._tracker.active_count() > 0

    async def dispatch(self, event: dict) -> StreamSignal:
        """Handle one SSE event. Mutates RoundState, returns a signal."""
        kind = event.get("event", "")
        data = event.get("data", {})
        handler = self._dispatch_table.get(kind)
        if handler is None:
            return StreamSignal(kind="continue")
        return await handler(data)

    # ── Dispatch wrappers (simple handlers: call _handle_*, return fixed signal) ──

    async def _on_assistant_message(self, data: dict) -> StreamSignal:
        await self._handle_assistant_message(data)
        return StreamSignal(kind="continue")

    async def _on_stream_event(self, data: dict) -> StreamSignal:
        await self._handle_stream_event(data)
        return StreamSignal(kind="continue")

    async def _on_tool_use(self, data: dict) -> StreamSignal:
        await self._handle_tool_use(data)
        return StreamSignal(kind="continue")

    async def _on_tool_done(self, data: dict) -> StreamSignal:
        await self._handle_tool_done(data)
        return StreamSignal(kind="continue")

    async def _on_subagent_start(self, data: dict) -> StreamSignal:
        self._handle_subagent_start(data)
        return StreamSignal(kind="continue")

    async def _on_subagent_stop(self, data: dict) -> StreamSignal:
        self._handle_subagent_stop(data)
        return StreamSignal(kind="subagent_boundary")

    async def _on_audit(self, data: dict) -> StreamSignal:
        await self._handle_audit(data)
        return StreamSignal(kind="continue")

    async def _on_result(self, data: dict) -> StreamSignal:
        await self._handle_result(data)
        return StreamSignal(kind="round_complete")

    # ── Dispatch handlers (complex: build signal from data) ──

    async def _on_rate_limit(self, data: dict) -> StreamSignal:
        """The SDK emits `rate_limit` events for THREE statuses."""
        status = data.get("status")
        if status == "rejected":
            log.warning(
                "[%s] rate limit rejected — SDK will retry (resets_at=%s, utilization=%s)",
                self._rid,
                data.get("resets_at"),
                data.get("utilization"),
            )
            return StreamSignal(kind="rate_limit_info", rate_limit_data=data)
        if status == "allowed_warning":
            log.info(
                "[%s] rate limit warning (resets_at=%s, utilization=%s)",
                self._rid,
                data.get("resets_at"),
                data.get("utilization"),
            )
        return StreamSignal(kind="continue")

    async def _on_end_round(self, data: dict) -> StreamSignal:
        round_summary = data.get("round_summary") or ""
        session_summary = data.get("session_summary") or ""
        log.info("[%s] end_round: %s", self._rid, round_summary[:80])
        return StreamSignal(
            kind="round_complete",
            round_summary=round_summary,
            session_summary=session_summary,
        )

    async def _on_end_session(self, data: dict) -> StreamSignal:
        log.info("[%s] end_session received", self._rid)
        return StreamSignal(
            kind="run_ended",
            round_summary=data.get("round_summary"),
            session_summary=data.get("session_summary"),
        )

    async def _on_end_session_denied(self, data: dict) -> StreamSignal:
        log.info(
            "[%s] end_session denied: %sm remaining",
            self._rid,
            data.get("remaining_minutes", "?"),
        )
        return StreamSignal(kind="continue")

    async def _on_session_end(self, data: dict) -> StreamSignal:
        return StreamSignal(kind="round_complete")

    async def _on_session_event_log_overflow(self, data: dict) -> StreamSignal:
        total = data.get("total_bytes", 0)
        limit = data.get("max_bytes", 0)
        error_msg = f"Sandbox event log overflow: {total}/{limit} bytes"
        log.error("[%s] %s", self._rid, error_msg)
        return StreamSignal(kind="session_error", error=error_msg)

    async def _on_session_error(self, data: dict) -> StreamSignal:
        error_msg = data.get("error", "unknown")
        log.error("[%s] session error: %s", self._rid, error_msg)
        return StreamSignal(kind="session_error", error=error_msg)

    async def _on_mcp_warning(self, data: dict) -> StreamSignal:
        msg = data.get("message", "")
        log.warning("[%s] MCP warning: %s", self._rid, msg)
        await log_audit(self._run.run_id, "mcp_warning", {"message": msg})
        return StreamSignal(kind="continue")

    # ── Core handlers (called by _on_* dispatch wrappers above) ────────

    async def _handle_assistant_message(self, data: dict) -> None:
        """Log text/thinking blocks and accumulate token usage.

        Assistant messages from a subagent carry a non-null
        parent_tool_use_id (the parent Agent/SendMessage tool call they run
        inside). Their prose is intermediate narration that never belongs in
        the main feed — the subagent's result is captured separately by the
        SubagentStop hook (subagent_complete.final_text) and rendered as the
        Agent Summary. So we suppress llm_text/llm_thinking for subagent
        messages and only accumulate their token usage; orchestrator messages
        (parent_tool_use_id is None) are logged as before.
        """
        run_id = self._run.run_id
        # serialize_message always sets this key; subscript (not .get) so a
        # serializer regression that drops it fails loud rather than silently
        # mislabeling subagent text as orchestrator text and re-leaking it.
        is_subagent = data["parent_tool_use_id"] is not None
        for block in data.get("content", []):
            block_type = block.get("type", "")
            if block_type == "text":
                text = block.get("text", "")
                log.info(
                    "[%s] %s", self._rid, text[:LOG_PREVIEW_LIMIT].replace("\n", " ")
                )
                if text.strip() and not is_subagent:
                    await log_audit(
                        run_id,
                        "llm_text",
                        {
                            "text": text,
                            "agent_role": self._run.agent_role,
                        },
                    )
            elif block_type == "thinking":
                thinking = block.get("thinking", "")
                log.info("[%s] [thinking] %s...", self._rid, thinking[:100])
                if thinking.strip() and not is_subagent:
                    await log_audit(
                        run_id,
                        "llm_thinking",
                        {
                            "text": thinking,
                            "agent_role": self._run.agent_role,
                        },
                    )
            elif block_type == "tool_use":
                log.info("[%s] Tool: %s", self._rid, block.get("name", ""))

    async def _handle_stream_event(self, data: dict) -> None:
        """Accumulate settled usage from a message_delta stream event.

        message_delta is the only event both providers populate: Anthropic
        fills message_start too, but OpenRouter zeroes it and settles usage
        only at the delta, which also carries the gateway's real cost.
        """
        event = data.get("event") or {}
        if event.get("type") != STREAM_EVENT_MESSAGE_DELTA:
            return
        await self._accumulate_usage(event)

    def _handle_subagent_start(self, data: dict) -> None:
        """Record a subagent starting in the tracker."""
        agent_id = data.get("agent_id", "")
        agent_type = data.get("agent_type", "")
        if agent_id:
            self._tracker.record_start(agent_id, agent_type)

    def _handle_subagent_stop(self, data: dict) -> None:
        """Record a subagent stopping in the tracker."""
        agent_id = data.get("agent_id", "")
        if agent_id:
            self._tracker.record_stop(agent_id)

    def _make_idempotency_key(self, seq: int | None) -> str | None:
        """Build a run-unique idempotency key from sandbox session ID + event seq.

        Returns None only if seq is missing (non-enriched events like
        assistant_message don't need idempotency). If sandbox_session_id
        is not set, that's a bug — fail fast.
        """
        if seq is None:
            return None
        if self._sandbox_session_id is None:
            raise RuntimeError(
                "sandbox_session_id not set — set_sandbox_session_id() must be "
                "called before dispatching events"
            )
        return f"{self._sandbox_session_id}:{seq}"

    async def _handle_tool_use(self, data: dict) -> None:
        """Track tool start and write pre-phase record to DB."""
        self._tools_in_flight += 1
        agent_id: str | None = data.get("agent_id")
        self._tracker.record_tool_use(agent_id)

        await log_tool_call_idempotent(
            run_id=self._run.run_id,
            phase="pre",
            tool_name=data.get("tool_name", ""),
            input_data=data.get("input_data"),
            output_data=None,
            duration_ms=None,
            permitted=True,
            deny_reason=None,
            agent_role=data.get("agent_role", ""),
            tool_use_id=data.get("tool_use_id"),
            session_id=data.get("session_id"),
            agent_id=agent_id,
            idempotency_key=self._make_idempotency_key(data.get("seq")),
        )

    async def _handle_tool_done(self, data: dict) -> None:
        """Track tool completion and write post-phase record to DB."""
        self._tools_in_flight = max(0, self._tools_in_flight - 1)
        agent_id: str | None = data.get("agent_id")
        self._tracker.record_tool_done(agent_id)

        await log_tool_call_idempotent(
            run_id=self._run.run_id,
            phase="post",
            tool_name=data.get("tool_name", ""),
            input_data=data.get("input_data"),
            output_data=data.get("output_data"),
            duration_ms=data.get("duration_ms"),
            permitted=data.get("permitted", True),
            deny_reason=data.get("deny_reason"),
            agent_role=data.get("agent_role", ""),
            tool_use_id=data.get("tool_use_id"),
            session_id=data.get("session_id"),
            agent_id=agent_id,
            idempotency_key=self._make_idempotency_key(data.get("seq")),
        )

    async def _handle_audit(self, data: dict) -> None:
        """Write a sandbox-originated audit event to DB with idempotency key."""
        await log_audit_idempotent(
            self._run.run_id,
            data.get("event_type", ""),
            data.get("details"),
            self._make_idempotency_key(data.get("seq")),
        )

    async def _handle_result(self, data: dict) -> None:
        """Persist the SDK session id and settle this round's tokens and cost.

        model_usage is the round's full-session usage, subagent turns included
        (message_delta never carries those), so it settles the token totals;
        result cost settles cost and rebases so a late delta can't double-count.
        A gateway's per-delta cost beats the SDK's 0.0 for gateway rounds, and
        the estimate branch must not rebase _cost_baseline — a later
        authoritative result cost settles against the true baseline.
        """
        run_id = self._run.run_id
        session_id = data.get("session_id")
        if session_id:
            await db.save_session_id(run_id, session_id)
        model_usage = data.get("model_usage")
        if model_usage:
            self._settle_round_tokens(model_usage)
        else:
            log.warning(
                "[%s] result carried no model_usage; round tokens stay "
                "orchestrator-only (subagent usage uncounted)",
                self._rid,
            )
        round_cost = data.get("total_cost_usd")
        if round_cost is not None and self._round_gateway_cost is None:
            settled = (self._cost_baseline or 0.0) + round_cost
            self._run.total_cost = settled
            self._cost_baseline = settled
            self._input_baseline = self._run.total_input_tokens
            self._output_baseline = self._run.total_output_tokens
            self._cache_create_baseline = self._run.cache_creation_input_tokens
            self._cache_read_baseline = self._run.cache_read_input_tokens
        elif model_usage and self._round_gateway_cost is None:
            self._run.total_cost = (
                self._cost_baseline or 0.0
            ) + self._estimated_round_cost()
        await self._persist_cost()

    def _settle_round_tokens(self, model_usage: dict) -> None:
        """Rebase this round's token totals to the result's full-session usage.

        Sums the per-model modelUsage entries (camelCase keys, per the CLI)
        onto the round-start baselines, replacing the orchestrator-only
        delta accumulation for this round.
        """
        per_model = list(model_usage.values())
        self._run.total_input_tokens = self._input_baseline + sum(
            m.get("inputTokens") or 0 for m in per_model
        )
        self._run.total_output_tokens = self._output_baseline + sum(
            m.get("outputTokens") or 0 for m in per_model
        )
        self._run.cache_creation_input_tokens = self._cache_create_baseline + sum(
            m.get("cacheCreationInputTokens") or 0 for m in per_model
        )
        self._run.cache_read_input_tokens = self._cache_read_baseline + sum(
            m.get("cacheReadInputTokens") or 0 for m in per_model
        )

    def _estimated_round_cost(self) -> float:
        """Cost of this round's tokens at the configured (Opus upper-bound) rates."""
        return (
            (self._run.total_input_tokens - self._input_baseline) * cost_per_input()
            + (self._run.total_output_tokens - self._output_baseline) * cost_per_output()
            + (self._run.cache_creation_input_tokens - self._cache_create_baseline)
            * cost_per_cache_write()
            + (self._run.cache_read_input_tokens - self._cache_read_baseline)
            * cost_per_cache_read()
        )

    async def _accumulate_usage(self, data: dict) -> None:
        """Accumulate token usage and emit a throttled usage audit event.

        Running cost uses ONLY this round's delta (current totals minus
        baselines captured at round start) added to the prior-rounds baseline.
        A gateway that bills us directly reports what it actually charged, which
        is preferred over the rate estimate; Anthropic omits it and settles at
        ResultMessage instead.
        """
        usage = data.get("usage")
        if usage:
            # OpenRouter (GPT-5.6) sends these keys with null for token kinds it
            # lacks (no prompt caching), so `or 0` covers both absent and null;
            # Anthropic always sends real ints. The totals are non-nullable ints.
            inp = usage.get("input_tokens") or 0
            out = usage.get("output_tokens") or 0
            cache_create = usage.get("cache_creation_input_tokens") or 0
            cache_read = usage.get("cache_read_input_tokens") or 0
            self._latest_context_tokens = inp + cache_create + cache_read
            self._run.total_input_tokens += inp
            self._run.total_output_tokens += out
            self._run.cache_creation_input_tokens += cache_create
            self._run.cache_read_input_tokens += cache_read
            gateway_cost = usage.get(USAGE_COST_KEY)
            if gateway_cost is not None:
                self._round_gateway_cost = (self._round_gateway_cost or 0.0) + gateway_cost
            round_cost = (
                self._estimated_round_cost()
                if self._round_gateway_cost is None
                else self._round_gateway_cost
            )
            self._run.total_cost = (self._cost_baseline or 0.0) + round_cost
        self._message_count += 1
        if self._message_count % USAGE_EMIT_INTERVAL == 0:
            await log_audit(
                self._run.run_id,
                "usage",
                {
                    "context_tokens": self._latest_context_tokens,
                    "total_input_tokens": self._run.total_input_tokens,
                    "total_output_tokens": self._run.total_output_tokens,
                    "cache_creation_input_tokens": self._run.cache_creation_input_tokens,
                    "cache_read_input_tokens": self._run.cache_read_input_tokens,
                    "total_cost_usd": self._run.total_cost,
                },
            )
            await self._persist_cost()

    async def _persist_cost(self) -> None:
        """Write current totals to the runs table."""
        r = self._run
        await db.update_run_cost(
            r.run_id,
            r.total_cost,
            r.total_input_tokens,
            r.total_output_tokens,
            r.cache_creation_input_tokens,
            r.cache_read_input_tokens,
            self._latest_context_tokens,
        )
