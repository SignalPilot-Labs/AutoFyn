"""Regression: the round must end at the result event, not the gate event.

The gate's end_round/end_session tools fire mid-turn, before the SDK's
ResultMessage — the only carrier of subagent token usage. Gate handlers now
stash the terminal signal and finalize_round reconciles every exit path with
it: summaries filled, status upgraded, unsettled rounds audited + persisted.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from agent_session.stream import StreamDispatcher
from tests.fast.conftest import _make_dispatcher
from utils.models import RoundResult

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

RESULT_EVENT_NO_USAGE = {
    "event": "result",
    "data": {
        "session_id": "sess-1",
        "total_cost_usd": 2.5,
        "num_turns": 3,
        "usage": {"input_tokens": 10, "output_tokens": 101},
        "model_usage": None,
    },
}

COMPLETE = RoundResult(status="complete", session_id="sess-1")
SESSION_ERROR = RoundResult(status="session_error", session_id="sess-1", error="boom")
STOPPED = RoundResult(status="stopped", session_id="sess-1")


async def _dispatch(
    dispatcher: StreamDispatcher, event: dict, audit: AsyncMock, persist: AsyncMock
):
    """Dispatch one event with DB and audit I/O mocked out."""
    with patch("agent_session.stream.log_audit", new=audit):
        with patch("agent_session.stream.db.save_session_id", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=persist):
                return await dispatcher.dispatch(event)


async def _finalize(
    dispatcher: StreamDispatcher,
    result: RoundResult,
    audit: AsyncMock,
    persist: AsyncMock,
) -> RoundResult:
    """Run finalize_round with audit and DB I/O mocked out."""
    with patch("agent_session.stream.log_audit", new=audit):
        with patch("agent_session.stream.db.update_run_cost", new=persist):
            return await dispatcher.finalize_round(result)


class TestRoundEndWaitsForResult:
    """Gate events defer; finalize_round reconciles every terminal path."""

    @pytest.mark.asyncio
    async def test_end_round_returns_continue(self) -> None:
        """end_round must NOT terminate the round — the result event does."""
        dispatcher, _ = _make_dispatcher()

        signal = await _dispatch(dispatcher, END_ROUND_EVENT, AsyncMock(), AsyncMock())

        assert signal.kind == "continue"

    @pytest.mark.asyncio
    async def test_result_terminates_round_with_settled_tokens(self) -> None:
        """The result event must end the round and settle subagent tokens."""
        dispatcher, _ = _make_dispatcher()

        await _dispatch(dispatcher, END_ROUND_EVENT, AsyncMock(), AsyncMock())
        signal = await _dispatch(dispatcher, RESULT_EVENT, AsyncMock(), AsyncMock())

        assert signal.kind == "round_complete"
        assert dispatcher._run.total_output_tokens == 952
        assert dispatcher._run.cache_read_input_tokens == 56773

    @pytest.mark.asyncio
    async def test_finalize_fills_summaries_after_settled_round(self) -> None:
        """A settled round gains the gate's summaries; no settle-miss audit."""
        dispatcher, _ = _make_dispatcher()
        audit = AsyncMock()

        await _dispatch(dispatcher, END_ROUND_EVENT, audit, AsyncMock())
        await _dispatch(dispatcher, RESULT_EVENT, audit, AsyncMock())
        result = await _finalize(dispatcher, COMPLETE, audit, AsyncMock())

        assert result.status == "complete"
        assert result.round_summary == "proved lemma"
        assert result.session_summary == "p6 run"
        audit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_finalize_upgrades_complete_to_ended_after_end_session(self) -> None:
        """An accepted end_session must end the run, not just the round."""
        dispatcher, _ = _make_dispatcher()

        await _dispatch(dispatcher, END_SESSION_EVENT, AsyncMock(), AsyncMock())
        await _dispatch(dispatcher, RESULT_EVENT, AsyncMock(), AsyncMock())
        result = await _finalize(dispatcher, COMPLETE, AsyncMock(), AsyncMock())

        assert result.status == "ended"
        assert result.session_summary == "solved p6"

    @pytest.mark.asyncio
    async def test_finalize_without_result_audits_and_persists(self) -> None:
        """No result event: terminate via the gate's intent, audited + persisted."""
        dispatcher, _ = _make_dispatcher()
        audit = AsyncMock()
        persist = AsyncMock()

        await _dispatch(dispatcher, END_ROUND_EVENT, audit, persist)
        result = await _finalize(dispatcher, COMPLETE, audit, persist)

        assert result.status == "complete"
        assert result.round_summary == "proved lemma"
        audit.assert_awaited_once()
        assert audit.await_args is not None
        assert audit.await_args.args[1] == "usage_settle_missed"
        persist.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_finalize_converts_session_error_after_gate_to_complete(self) -> None:
        """A drain-window session_error must not replay a finished round."""
        dispatcher, _ = _make_dispatcher()

        await _dispatch(dispatcher, END_ROUND_EVENT, AsyncMock(), AsyncMock())
        result = await _finalize(dispatcher, SESSION_ERROR, AsyncMock(), AsyncMock())

        assert result.status == "complete"
        assert result.round_summary == "proved lemma"

    @pytest.mark.asyncio
    async def test_finalize_keeps_stopped_status_but_fills_summaries(self) -> None:
        """User stop during the drain keeps its status; summaries survive."""
        dispatcher, _ = _make_dispatcher()

        await _dispatch(dispatcher, END_ROUND_EVENT, AsyncMock(), AsyncMock())
        result = await _finalize(dispatcher, STOPPED, AsyncMock(), AsyncMock())

        assert result.status == "stopped"
        assert result.round_summary == "proved lemma"

    @pytest.mark.asyncio
    async def test_finalize_without_gate_event_is_passthrough(self) -> None:
        """No gate event: the terminal result is returned untouched, unaudited."""
        dispatcher, _ = _make_dispatcher()
        audit = AsyncMock()

        result = await _finalize(dispatcher, SESSION_ERROR, audit, AsyncMock())

        assert result is SESSION_ERROR
        audit.assert_not_awaited()

    @pytest.mark.asyncio
    async def test_end_round_cannot_downgrade_accepted_end_session(self) -> None:
        """A stray end_round after end_session must not keep the run alive."""
        dispatcher, _ = _make_dispatcher()

        await _dispatch(dispatcher, END_SESSION_EVENT, AsyncMock(), AsyncMock())
        await _dispatch(dispatcher, END_ROUND_EVENT, AsyncMock(), AsyncMock())
        result = await _finalize(dispatcher, COMPLETE, AsyncMock(), AsyncMock())

        assert result.status == "ended"

    @pytest.mark.asyncio
    async def test_result_without_model_usage_counts_as_unsettled(self) -> None:
        """A result lacking model_usage must still trigger the settle-miss audit."""
        dispatcher, _ = _make_dispatcher()
        audit = AsyncMock()

        await _dispatch(dispatcher, END_ROUND_EVENT, audit, AsyncMock())
        await _dispatch(dispatcher, RESULT_EVENT_NO_USAGE, audit, AsyncMock())
        result = await _finalize(dispatcher, COMPLETE, audit, AsyncMock())

        assert result.status == "complete"
        settle_miss = [
            c for c in audit.await_args_list if c.args[1] == "usage_settle_missed"
        ]
        assert len(settle_miss) == 1
