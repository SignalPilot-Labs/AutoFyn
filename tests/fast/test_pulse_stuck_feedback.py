"""Tests that PulseWatchdog writes a stuck-recovery feedback file on interrupt.

The feedback file lands in the current round's folder so the next round's
orchestrator can read what was killed and adapt instead of re-dispatching the
same stuck agent.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agent_session.pulse import PulseWatchdog
from utils.constants import ROUND_DIR_PREFIX, STUCK_RECOVERY_REPORT_NAME
from utils.models import StuckSubagent
from utils.run_config import RunAgentConfig

_RUN_CONFIG = RunAgentConfig(
    max_rounds=128,
    tool_call_timeout_sec=3600,
    session_idle_timeout_sec=120,
    subagent_idle_kill_sec=600,
)


class TestPulseStuckFeedback:
    """PulseWatchdog._check_stuck_subagents feedback-file behaviour."""

    def _watchdog(self, round_number: int) -> tuple[PulseWatchdog, MagicMock, MagicMock]:
        sandbox = MagicMock()
        sandbox.file_system.write = AsyncMock()
        sandbox.session.interrupt = AsyncMock()
        inbox = MagicMock()
        watchdog = PulseWatchdog(
            sandbox, "run-1", "run-1"[:8], inbox, _RUN_CONFIG, round_number
        )
        return watchdog, sandbox, inbox

    @pytest.mark.asyncio
    async def test_writes_feedback_file_into_current_round_folder(self) -> None:
        watchdog, sandbox, _ = self._watchdog(round_number=2)
        tracker = MagicMock()
        tracker.stuck_subagents.return_value = [
            StuckSubagent("a8b3254d7b3f23f38", "security-reviewer", 605, 1332),
        ]

        with patch("agent_session.pulse.log_audit", new=AsyncMock()):
            triggered = await watchdog._check_stuck_subagents(tracker, "sess-1")

        assert triggered is True
        sandbox.file_system.write.assert_awaited_once()
        path, content = sandbox.file_system.write.await_args.args[:2]
        assert path == f"{ROUND_DIR_PREFIX}2/{STUCK_RECOVERY_REPORT_NAME}"
        assert "security-reviewer" in content
        assert "605" in content

    @pytest.mark.asyncio
    async def test_no_write_when_nothing_stuck(self) -> None:
        watchdog, sandbox, _ = self._watchdog(round_number=1)
        tracker = MagicMock()
        tracker.stuck_subagents.return_value = []

        triggered = await watchdog._check_stuck_subagents(tracker, "sess-1")

        assert triggered is False
        sandbox.file_system.write.assert_not_awaited()

    def test_feedback_md_lists_every_stuck_agent(self) -> None:
        watchdog, _, _ = self._watchdog(round_number=4)
        md = watchdog._stuck_feedback_md(
            [
                StuckSubagent("aaaaaaaa", "security-reviewer", 605, 1332),
                StuckSubagent("bbbbbbbb", "backend-dev", 300, 900),
            ]
        )
        assert "Round 4" in md
        assert "security-reviewer" in md
        assert "backend-dev" in md
