"""Regression: the sandbox must forward the ResultMessage after the gate fires.

The old SDK loop broke on `_ended` immediately. The gate tools fire mid-turn,
so the loop always exited before the CLI's ResultMessage — the only carrier
of full-session token usage (subagent turns included) — leaving every round's
totals orchestrator-only. The loop now keeps reading until the ResultMessage,
bounded by RESULT_DRAIN_TIMEOUT_SEC.
"""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator
from unittest.mock import MagicMock

import pytest

from claude_agent_sdk import ResultMessage

import sdk.session as session_module
from sdk.session import Session


def _make_session(events: list[dict]) -> Session:
    """Build a Session whose emitted events are captured into `events`."""
    session = Session("sess-1", {"run_id": "run-1"})
    session._emit = events.append  # type: ignore[method-assign]
    return session


def _make_client(messages: AsyncIterator[object]) -> MagicMock:
    """Fake ClaudeSDKClient exposing only receive_messages()."""
    client = MagicMock()
    client.receive_messages.return_value = messages
    return client


def _result_message() -> ResultMessage:
    """A minimal ResultMessage as the SDK emits at turn completion."""
    return ResultMessage(
        subtype="success",
        duration_ms=1000,
        duration_api_ms=900,
        is_error=False,
        num_turns=3,
        session_id="cli-sess-1",
        total_cost_usd=2.5,
        usage={"input_tokens": 10, "output_tokens": 101},
        model_usage={"claude-opus-4-8": {"outputTokens": 952}},
    )


class TestSessionForwardsResultAfterGate:
    """After `_ended`, the loop reads until the ResultMessage, bounded."""

    @pytest.mark.asyncio
    async def test_result_message_is_forwarded_after_gate_ends_round(self) -> None:
        """The gate firing mid-turn must not cut off the ResultMessage."""
        events: list[dict] = []
        session = _make_session(events)
        consumed_past_result: list[bool] = []

        async def _messages() -> AsyncIterator[object]:
            yield object()  # tool traffic before the gate call
            session._ended = True  # gate tool fires mid-turn
            yield object()  # remainder of the turn
            yield _result_message()  # turn completes
            consumed_past_result.append(True)
            yield object()

        await session._forward_messages(_make_client(_messages()))

        assert [e["event"] for e in events] == ["result"]
        assert events[0]["data"]["model_usage"] == {
            "claude-opus-4-8": {"outputTokens": 952}
        }
        assert not consumed_past_result

    @pytest.mark.asyncio
    async def test_drain_times_out_when_no_result_arrives(self) -> None:
        """A turn that never completes must not hold the session open."""
        events: list[dict] = []
        session = _make_session(events)
        session._ended = True

        async def _messages() -> AsyncIterator[object]:
            await asyncio.sleep(9999)
            yield object()

        original = session_module.RESULT_DRAIN_TIMEOUT_SEC
        session_module.RESULT_DRAIN_TIMEOUT_SEC = 0.01
        try:
            await session._forward_messages(_make_client(_messages()))
        finally:
            session_module.RESULT_DRAIN_TIMEOUT_SEC = original

        assert events == []

    @pytest.mark.asyncio
    async def test_exhausted_stream_returns_without_result(self) -> None:
        """A naturally closed stream must end the loop cleanly."""
        events: list[dict] = []
        session = _make_session(events)

        async def _messages() -> AsyncIterator[object]:
            yield object()

        await session._forward_messages(_make_client(_messages()))

        assert events == []
