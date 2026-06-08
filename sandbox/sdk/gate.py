"""SessionGate — MCP tools for round/session lifecycle control.

Provides `end_round` and `end_session` tools that the orchestrator
calls to signal round completion or run termination. `end_session`
is denied while the time lock has more than EARLY_EXIT_THRESHOLD_MIN
remaining, unless the session has been explicitly unlocked.
"""

import logging
import time
from typing import Any, Callable, TypedDict

from claude_agent_sdk import tool, create_sdk_mcp_server

from constants import (
    EARLY_EXIT_THRESHOLD_MIN,
    SECONDS_PER_MINUTE,
    SESSION_GATE_SERVER_NAME,
    GATE_TOOL_END_ROUND,
    GATE_TOOL_END_SESSION,
    GATE_EVENT_END_ROUND,
    GATE_EVENT_END_SESSION,
    GATE_EVENT_AUDIT,
    GATE_EVENT_END_SESSION_DENIED,
    GATE_AUDIT_END_SESSION_DENIED,
    GATE_END_ROUND_DESC,
    GATE_END_SESSION_DESC,
    GATE_ROUND_ENDED_TEXT,
    GATE_SESSION_ENDED_TEXT,
    GATE_SESSION_LOCKED_TEXT,
)

log = logging.getLogger("sandbox.session.gate")


class SessionGateConfig(TypedDict):
    duration_minutes: float
    start_time: float


def _evaluate_unlock(
    duration_min: float,
    elapsed_min: float,
    is_unlocked: Callable[[], bool],
) -> bool:
    """Return True if end_session is permitted.

    Mirrors the exact OR condition:
    duration_min <= 0 or (duration_min - elapsed_min) <= EARLY_EXIT_THRESHOLD_MIN
    or is_unlocked().
    """
    remaining_min = duration_min - elapsed_min
    return (
        duration_min <= 0
        or remaining_min <= EARLY_EXIT_THRESHOLD_MIN
        or is_unlocked()
    )


def _build_end_round_payload(args: dict[str, Any]) -> dict[str, Any]:
    """Build the end_round emit payload: {event, data:{round_summary, session_summary}}."""
    return {
        "event": GATE_EVENT_END_ROUND,
        "data": {
            "round_summary": args["round_summary"],
            "session_summary": args["session_summary"],
        },
    }


def _build_end_session_payload(
    args: dict[str, Any], elapsed_min: float
) -> dict[str, Any]:
    """Build the end_session emit payload including elapsed_minutes=round(elapsed_min,1)."""
    return {
        "event": GATE_EVENT_END_SESSION,
        "data": {
            "round_summary": args["round_summary"],
            "session_summary": args["session_summary"],
            "elapsed_minutes": round(elapsed_min, 1),
        },
    }


def _build_denied_payloads(
    remaining_min: float,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Return (audit_payload, denied_payload) IN THAT ORDER.

    The audit event first, then the end_session_denied event.
    Caller emits them in tuple order to preserve the current
    two-emit ordering.
    """
    audit_payload: dict[str, Any] = {
        "event": GATE_EVENT_AUDIT,
        "data": {
            "event_type": GATE_AUDIT_END_SESSION_DENIED,
            "details": {"remaining_minutes": round(remaining_min, 1)},
        },
    }
    denied_payload: dict[str, Any] = {
        "event": GATE_EVENT_END_SESSION_DENIED,
        "data": {"remaining_minutes": round(remaining_min, 1)},
    }
    return audit_payload, denied_payload


def _denied_text(remaining_min: float) -> str:
    """Return the locked response text with remaining minutes interpolated."""
    return GATE_SESSION_LOCKED_TEXT.format(remaining=round(remaining_min, 1))


def _text_content(text: str) -> dict[str, Any]:
    """Wrap a text string in the MCP content response shape."""
    return {"content": [{"type": "text", "text": text}]}


class SessionGate:
    """MCP server with end_round and end_session tools.

    Public API:
        build_mcp(config) -> MCP server for ClaudeAgentOptions
    """

    def __init__(
        self,
        run_id: str,
        emit: Callable[[dict], None],
        mark_ended: Callable[[], None],
        is_unlocked: Callable[[], bool],
    ) -> None:
        self._run_id = run_id
        self._emit = emit
        self._mark_ended = mark_ended
        self._is_unlocked = is_unlocked

    def build_mcp(self, config: SessionGateConfig) -> Any:
        """Build MCP server with end_round + end_session tools."""
        duration_min = config["duration_minutes"]
        start = config["start_time"]
        emit = self._emit
        mark_ended = self._mark_ended
        is_unlocked = self._is_unlocked

        @tool(GATE_TOOL_END_ROUND, GATE_END_ROUND_DESC,
              {"round_summary": str, "session_summary": str})
        async def end_round_tool(args: dict[str, Any]) -> dict[str, Any]:
            mark_ended()
            emit(_build_end_round_payload(args))
            return _text_content(GATE_ROUND_ENDED_TEXT)

        @tool(GATE_TOOL_END_SESSION, GATE_END_SESSION_DESC,
              {"round_summary": str, "session_summary": str})
        async def end_session_tool(args: dict[str, Any]) -> dict[str, Any]:
            elapsed_min = (time.time() - start) / SECONDS_PER_MINUTE
            if _evaluate_unlock(duration_min, elapsed_min, is_unlocked):
                mark_ended()
                emit(_build_end_session_payload(args, elapsed_min))
                return _text_content(GATE_SESSION_ENDED_TEXT)
            remaining_min = duration_min - elapsed_min
            audit_payload, denied_payload = _build_denied_payloads(remaining_min)
            emit(audit_payload)
            emit(denied_payload)
            return _text_content(_denied_text(remaining_min))

        self._end_round = end_round_tool
        self._end_session = end_session_tool
        return create_sdk_mcp_server(
            name=SESSION_GATE_SERVER_NAME,
            tools=[end_round_tool, end_session_tool],
        )
