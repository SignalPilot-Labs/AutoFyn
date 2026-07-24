"""Regression: result model_usage must settle full-round tokens, subagents included.

Token counters accumulated only from orchestrator message_delta stream events;
subagent turns never emit stream events ("subagent partials don't surface"),
so every archived run's totals were an orchestrator-only undercount — in one
IMO 2026 run the subagents made 93% of the tool calls and none of their
generation was counted. The CLI reports full-session usage per model in the
result event's modelUsage (verified empirically: orchestrator transcript +
subagent transcript sums match modelUsage to the token), which the sandbox
already forwards. The dispatcher must settle this round's token totals from
it, mirroring how total_cost_usd settles cost.

Payload shapes below are verbatim from a live `claude -p --output-format json`
run that spawned one Task subagent.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from agent_session.stream import StreamDispatcher
from agent_session.tracker import SubagentTracker
from tests.fast.conftest import _DEFAULT_RUN_CONFIG, _make_dispatcher

ORCHESTRATOR_DELTA = {
    "type": "message_delta",
    "usage": {
        "input_tokens": 28,
        "output_tokens": 811,
        "cache_creation_input_tokens": 29890,
        "cache_read_input_tokens": 56773,
    },
}

# Full-session usage incl. one subagent (out 141, cache_create 14333, in 10)
# on top of the orchestrator delta above.
MODEL_USAGE = {
    "claude-haiku-4-5-20251001": {
        "inputTokens": 38,
        "outputTokens": 952,
        "cacheReadInputTokens": 56773,
        "cacheCreationInputTokens": 44223,
        "webSearchRequests": 0,
        "costUSD": 0.08878855,
        "contextWindow": 200000,
        "maxOutputTokens": 32000,
    },
}

TWO_MODEL_USAGE = {
    "claude-haiku-4-5-20251001": {
        "inputTokens": 38,
        "outputTokens": 952,
        "cacheReadInputTokens": 56773,
        "cacheCreationInputTokens": 44223,
    },
    "claude-sonnet-5": {
        "inputTokens": 4,
        "outputTokens": 48,
        "cacheReadInputTokens": 1000,
        "cacheCreationInputTokens": 2000,
    },
}


def _result_event(model_usage: dict | None, total_cost_usd: float | None) -> dict:
    """Build a result stream event as the sandbox serializer emits it."""
    return {
        "event": "result",
        "data": {
            "session_id": "sess-1",
            "total_cost_usd": total_cost_usd,
            "num_turns": 3,
            "usage": {"input_tokens": 10, "output_tokens": 101},
            "model_usage": model_usage,
        },
    }


async def _dispatch(dispatcher: StreamDispatcher, event: dict) -> None:
    """Dispatch one event with DB and audit I/O mocked out."""
    with patch("agent_session.stream.log_audit", new=AsyncMock()):
        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=AsyncMock()):
                await dispatcher.dispatch(event)


class TestResultSettlesSubagentTokens:
    """The result's model_usage settles round tokens; its absence changes nothing."""

    @pytest.mark.asyncio
    async def test_model_usage_replaces_orchestrator_only_totals(self) -> None:
        """Delta-accumulated (orchestrator-only) totals must be settled upward."""
        dispatcher, _ = _make_dispatcher()

        await _dispatch(
            dispatcher,
            {"event": "stream_event", "data": {"event": ORCHESTRATOR_DELTA}},
        )
        await _dispatch(dispatcher, _result_event(MODEL_USAGE, 0.08878855))

        run = dispatcher._run
        assert run.total_output_tokens == 952
        assert run.cache_creation_input_tokens == 44223
        assert run.cache_read_input_tokens == 56773
        assert run.total_input_tokens == 38
        assert run.total_cost == pytest.approx(0.08878855)

    @pytest.mark.asyncio
    async def test_multiple_models_are_summed(self) -> None:
        """A round spanning models (fallback) must sum all modelUsage entries."""
        dispatcher, _ = _make_dispatcher()

        await _dispatch(dispatcher, _result_event(TWO_MODEL_USAGE, 0.1))

        run = dispatcher._run
        assert run.total_output_tokens == 1000
        assert run.cache_creation_input_tokens == 46223
        assert run.cache_read_input_tokens == 57773
        assert run.total_input_tokens == 42

    @pytest.mark.asyncio
    async def test_missing_model_usage_preserves_delta_totals(self) -> None:
        """Without model_usage the delta-accumulated totals must survive."""
        dispatcher, _ = _make_dispatcher()

        await _dispatch(
            dispatcher,
            {"event": "stream_event", "data": {"event": ORCHESTRATOR_DELTA}},
        )
        await _dispatch(dispatcher, _result_event(None, 0.05))

        run = dispatcher._run
        assert run.total_output_tokens == 811
        assert run.cache_creation_input_tokens == 29890
        assert run.total_cost == pytest.approx(0.05)

    @pytest.mark.asyncio
    async def test_settled_tokens_feed_cost_estimate_when_cost_absent(self) -> None:
        """Subscription auth reports no cost; the estimate must cover subagents."""
        dispatcher, _ = _make_dispatcher()

        await _dispatch(
            dispatcher,
            {"event": "stream_event", "data": {"event": ORCHESTRATOR_DELTA}},
        )
        orchestrator_only_cost = dispatcher._run.total_cost
        await _dispatch(dispatcher, _result_event(MODEL_USAGE, None))

        run = dispatcher._run
        assert run.total_output_tokens == 952
        assert orchestrator_only_cost is not None
        assert run.total_cost is not None
        assert run.total_cost > orchestrator_only_cost

    @pytest.mark.asyncio
    async def test_gateway_cost_survives_token_settle(self) -> None:
        """OpenRouter rounds: tokens settle full, the gateway's cost must win."""
        dispatcher, _ = _make_dispatcher()
        gateway_delta = {
            "type": "message_delta",
            "usage": {
                "input_tokens": 28,
                "output_tokens": 811,
                "cache_creation_input_tokens": 29890,
                "cache_read_input_tokens": 56773,
                "cost": 0.05,
            },
        }

        await _dispatch(
            dispatcher, {"event": "stream_event", "data": {"event": gateway_delta}}
        )
        await _dispatch(dispatcher, _result_event(MODEL_USAGE, 0.0))

        run = dispatcher._run
        assert run.total_output_tokens == 952
        assert run.total_cost == pytest.approx(0.05)

    @pytest.mark.asyncio
    async def test_late_delta_after_estimate_settle_stays_incremental(self) -> None:
        """A delta after an estimate settle must extend totals, not corrupt cost.

        The estimate is linear in tokens, so cost after a late delta must equal
        the estimate over (settled + late) tokens — this is why the estimate
        branch needs no baseline rebase.
        """
        dispatcher, _ = _make_dispatcher()
        late_delta = {
            "type": "message_delta",
            "usage": {
                "input_tokens": 1,
                "output_tokens": 5,
                "cache_creation_input_tokens": 0,
                "cache_read_input_tokens": 0,
            },
        }

        await _dispatch(dispatcher, _result_event(MODEL_USAGE, None))
        settled_cost = dispatcher._run.total_cost
        await _dispatch(
            dispatcher, {"event": "stream_event", "data": {"event": late_delta}}
        )

        run = dispatcher._run
        assert run.total_output_tokens == 952 + 5
        assert settled_cost is not None
        assert run.total_cost is not None
        assert run.total_cost > settled_cost

    @pytest.mark.asyncio
    async def test_result_cost_after_estimate_settle_is_not_double_counted(
        self,
    ) -> None:
        """An authoritative result cost must replace the estimate, not stack on it.

        Guards the deliberate absence of a _cost_baseline rebase in the
        estimate branch: the round's real cost already covers everything the
        estimate covered.
        """
        dispatcher, _ = _make_dispatcher()

        await _dispatch(dispatcher, _result_event(MODEL_USAGE, None))
        await _dispatch(dispatcher, _result_event(MODEL_USAGE, 0.08878855))

        assert dispatcher._run.total_cost == pytest.approx(0.08878855)

    @pytest.mark.asyncio
    async def test_settle_rebases_against_prior_round_baseline(self) -> None:
        """Prior-round totals must be preserved, not overwritten by this round."""
        dispatcher, _ = _make_dispatcher()
        run = dispatcher._run
        run.total_output_tokens = 100
        run.total_input_tokens = 5
        run.cache_creation_input_tokens = 200
        run.cache_read_input_tokens = 300
        round_two = StreamDispatcher(
            run=run,
            round_number=2,
            tracker=SubagentTracker(_DEFAULT_RUN_CONFIG),
        )

        await _dispatch(round_two, _result_event(MODEL_USAGE, 0.08878855))

        assert run.total_output_tokens == 100 + 952
        assert run.total_input_tokens == 5 + 38
        assert run.cache_creation_input_tokens == 200 + 44223
        assert run.cache_read_input_tokens == 300 + 56773
