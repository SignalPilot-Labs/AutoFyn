"""Regression: the round must end at the result event, not the gate event.

The session gate's end_round/end_session tools fire mid-turn, before the
SDK's ResultMessage — the only carrier of subagent token usage. Ending the
round at the gate event dropped that message: every round's tokens stayed
orchestrator-only and sdk_session_id was never saved. The gate handlers now
stash the terminal signal, the result event returns it after settling
tokens, and session_end is the audited fallback when no result arrives.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from agent_session.stream import StreamDispatcher
from tests.fast.conftest import _make_dispatcher

MODEL_USAGE = {
    "claude-opus-4-8": {
        "inputTokens": 38,
        "outputTokens": 952,
        "cacheReadInputTokens": 56773,
        "cacheCreationInputTokens": 44223,
    },
}

END_ROUND_EVENT = {
    "event": "end_round",
    "data": {"round_summary": "proved lemma", "session_summary": "p6 run"},
}

END_SESSION_EVENT = {
    "event": "end_session",
    "data": {"round_summary": "final round", "session_summary": "solved p6"},
}

RESULT_EVENT = {
    "event": "result",
    "data": {
        "session_id": "sess-1",
        "total_cost_usd": 2.5,
        "num_turns": 3,
        "usage": {"input_tokens": 10, "output_tokens": 101},
        "model_usage": MODEL_USAGE,
    },
}

SESSION_END_EVENT = {"event": "session_end", "data": {}}


async def _dispatch(dispatcher: StreamDispatcher, event: dict, audit: AsyncMock):
    """Dispatch one event with DB and audit I/O mocked out."""
    with patch("agent_session.stream.log_audit", new=audit):
        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=AsyncMock()):
                return await dispatcher.dispatch(event)


class TestRoundEndWaitsForResult:
    """Gate events defer; the result event terminates with settled tokens."""

    @pytest.mark.asyncio
    async def test_end_round_returns_continue(self) -> None:
        """end_round must NOT terminate the round — the result event does."""
        dispatcher, _ = _make_dispatcher()

        signal = await _dispatch(dispatcher, END_ROUND_EVENT, AsyncMock())

        assert signal.kind == "continue"

    @pytest.mark.asyncio
    async def test_result_after_end_round_terminates_with_settled_tokens(self) -> None:
        """The result event must end the round, carry summaries, settle tokens."""
        dispatcher, _ = _make_dispatcher()

        await _dispatch(dispatcher, END_ROUND_EVENT, AsyncMock())
        signal = await _dispatch(dispatcher, RESULT_EVENT, AsyncMock())

        assert signal.kind == "round_complete"
        assert signal.round_summary == "proved lemma"
        assert signal.session_summary == "p6 run"
        assert dispatcher._run.total_output_tokens == 952
        assert dispatcher._run.cache_read_input_tokens == 56773

    @pytest.mark.asyncio
    async def test_result_after_end_session_terminates_run(self) -> None:
        """After end_session, the result event must end the whole run."""
        dispatcher, _ = _make_dispatcher()

        await _dispatch(dispatcher, END_SESSION_EVENT, AsyncMock())
        signal = await _dispatch(dispatcher, RESULT_EVENT, AsyncMock())

        assert signal.kind == "run_ended"
        assert signal.round_summary == "final round"
        assert signal.session_summary == "solved p6"
        assert dispatcher._run.total_output_tokens == 952

    @pytest.mark.asyncio
    async def test_session_end_fallback_carries_pending_end_and_audits(self) -> None:
        """No result before session_end: terminate via pending end, audit it."""
        dispatcher, _ = _make_dispatcher()
        audit = AsyncMock()

        await _dispatch(dispatcher, END_ROUND_EVENT, audit)
        signal = await _dispatch(dispatcher, SESSION_END_EVENT, audit)

        assert signal.kind == "round_complete"
        assert signal.round_summary == "proved lemma"
        audit.assert_awaited_once()
        assert audit.await_args is not None
        assert audit.await_args.args[1] == "usage_settle_missed"

    @pytest.mark.asyncio
    async def test_result_without_gate_event_stays_round_complete(self) -> None:
        """A result with no prior gate event terminates the round as before."""
        dispatcher, _ = _make_dispatcher()

        signal = await _dispatch(dispatcher, RESULT_EVENT, AsyncMock())

        assert signal.kind == "round_complete"

    @pytest.mark.asyncio
    async def test_session_end_without_gate_event_does_not_audit(self) -> None:
        """A plain session_end (no pending end) must not log a settle miss."""
        dispatcher, _ = _make_dispatcher()
        audit = AsyncMock()

        signal = await _dispatch(dispatcher, SESSION_END_EVENT, audit)

        assert signal.kind == "round_complete"
        audit.assert_not_awaited()
