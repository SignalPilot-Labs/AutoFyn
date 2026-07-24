"""Regression: every runner exit path must flow through finalize_round.

A session_error arriving in the gate→result drain window used to surface as
status "session_error", which the round loop retries by decrementing
round_number — replaying a round the orchestrator declared complete.
"""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agent_session.runner import RoundRunner
from tests.fast.conftest import _DEFAULT_RUN_CONFIG, _make_dispatcher, _make_run
from utils.run_config import RunAgentConfig

STREAM_EVENTS = [
    {"event": "end_round", "data": {"round_summary": "done", "session_summary": "s"}},
    {"event": "session_error", "data": {"error": "boom"}},
]

PATIENT_RUN_CONFIG = RunAgentConfig(
    max_rounds=_DEFAULT_RUN_CONFIG.max_rounds,
    tool_call_timeout_sec=_DEFAULT_RUN_CONFIG.tool_call_timeout_sec,
    session_idle_timeout_sec=9999,
    subagent_idle_kill_sec=_DEFAULT_RUN_CONFIG.subagent_idle_kill_sec,
)


async def _stream_events(session_id: str, after_seq: int) -> AsyncIterator[dict]:
    """Fake sandbox SSE stream: gate event, then a drain-window error."""
    for event in STREAM_EVENTS:
        yield event


async def _never() -> dict:
    """Inbox that never produces a user event."""
    await asyncio.sleep(9999)
    return {}


class TestRunnerFinalizesRound:
    """_drive_stream must return the finalized RoundResult."""

    @pytest.mark.asyncio
    async def test_session_error_after_end_round_completes_instead_of_retrying(
        self,
    ) -> None:
        """The gate's declared outcome must survive a drain-window error."""
        sandbox = MagicMock()
        sandbox.session.stream_events = _stream_events
        inbox = MagicMock()
        inbox.next_event = _never
        runner = RoundRunner(
            sandbox=sandbox,
            run=_make_run(),
            inbox=inbox,
            time_lock=MagicMock(),
            run_config=PATIENT_RUN_CONFIG,
        )
        dispatcher, _ = _make_dispatcher()

        with patch("agent_session.stream.log_audit", new=AsyncMock()):
            with patch("agent_session.stream.db.update_run_cost", new=AsyncMock()):
                result = await runner._drive_stream(
                    "sess-1", dispatcher, MagicMock(), 1
                )

        assert result.status == "complete"
        assert result.round_summary == "done"
        assert result.session_summary == "s"
