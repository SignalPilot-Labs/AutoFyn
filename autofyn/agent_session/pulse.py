"""PulseWatchdog — periodic stuck-subagent and tool-timeout detection.

Runs as a background asyncio task (via `asyncio.create_task`) and is
cancelled externally when the round ends. Each cycle checks for stuck
subagents and timed-out tool calls, interrupting the session and
injecting context so the orchestrator can recover.
"""

import asyncio
import logging

from prompts.loader import render_stuck_recovery, render_tool_timeout
from sandbox_client.client import SandboxClient
from user.inbox import UserInbox
from agent_session.tracker import SubagentTracker
from utils.db_logging import log_audit
from utils.constants import (
    pulse_check_interval_sec,
    ROUND_DIR_PREFIX,
    STUCK_RECOVERY_REPORT_NAME,
)
from utils.run_config import RunAgentConfig
from utils.models import StuckSubagent

log = logging.getLogger("session.pulse")


class PulseWatchdog:
    """Periodic watchdog for stuck subagents and timed-out tool calls.

    Two checks each cycle:
    1. Stuck subagents (idle > subagent_idle_kill_sec) — interrupt + inject recovery.
    2. Timed-out tool calls (running > tool_call_timeout_sec) — interrupt + inject timeout.

    Only one recovery is triggered per cycle to avoid double-interrupting.
    """

    def __init__(
        self,
        sandbox: SandboxClient,
        run_id: str,
        rid: str,
        inbox: UserInbox,
        run_config: RunAgentConfig,
        round_number: int,
    ) -> None:
        self._sandbox = sandbox
        self._run_id = run_id
        self._rid = rid
        self._inbox = inbox
        self._run_config = run_config
        self._round_number = round_number

    async def run(self, tracker: SubagentTracker, session_id: str) -> None:
        """Infinite loop — meant to be wrapped in asyncio.create_task and cancelled externally."""
        while True:
            await asyncio.sleep(pulse_check_interval_sec())
            if await self._check_stuck_subagents(tracker, session_id):
                continue
            await self._check_timed_out_tools(tracker, session_id)

    async def _check_stuck_subagents(
        self,
        tracker: SubagentTracker,
        session_id: str,
    ) -> bool:
        """Interrupt stuck subagents and notify the orchestrator.

        Returns True if any recovery was triggered.
        """
        stuck = tracker.stuck_subagents()
        if not stuck:
            return False
        descriptions = [
            f"{s.agent_type} ({s.agent_id[:8]}, idle {s.idle_seconds}s)"
            for s in stuck
        ]
        log.warning(
            "[%s] Stuck subagent(s) — interrupting: %s",
            self._rid,
            ", ".join(descriptions),
        )
        await log_audit(
            self._run_id,
            "stuck_recovery",
            {
                "stuck": [
                    {
                        "agent_id": s.agent_id,
                        "agent_type": s.agent_type,
                        "idle_seconds": s.idle_seconds,
                        "total_seconds": s.total_seconds,
                    }
                    for s in stuck
                ],
            },
        )
        await self._write_stuck_feedback(stuck)
        for s in stuck:
            tracker.record_stop(s.agent_id)
        await self._sandbox.session.interrupt(session_id)
        agent_names = ", ".join(s.agent_type for s in stuck)
        self._inbox.push(
            "inject",
            render_stuck_recovery(agent_names, self._run_config.subagent_idle_kill_sec // 60),
        )
        return True

    async def _write_stuck_feedback(self, stuck: list[StuckSubagent]) -> None:
        """Write a feedback file into this round's folder for the next round.

        Interrupting the session ends the current round, so the orchestrator
        never reads the injected recovery message. The next round's prompt
        points the orchestrator at this file so it can adapt instead of
        re-dispatching the same agent blind.
        """
        path = f"{ROUND_DIR_PREFIX}{self._round_number}/{STUCK_RECOVERY_REPORT_NAME}"
        await self._sandbox.file_system.write(
            path, self._stuck_feedback_md(stuck), append=False
        )

    def _stuck_feedback_md(self, stuck: list[StuckSubagent]) -> str:
        """Render the facts of a stuck-recovery: what was killed and how long idle."""
        lines = [
            f"# Stuck Recovery — Round {self._round_number}",
            "",
            "The stuck watchdog force-interrupted the following subagent(s) "
            "because they stopped emitting output. This ended the round early. "
            "Adjust your approach for these agent type(s) before re-dispatching "
            "them — split the work smaller, avoid long no-output operations.",
            "",
        ]
        for s in stuck:
            lines.append(
                f"- **{s.agent_type}** (`{s.agent_id[:8]}`) — "
                f"idle {s.idle_seconds}s, running {s.total_seconds}s total"
            )
        return "\n".join(lines) + "\n"

    async def _check_timed_out_tools(
        self,
        tracker: SubagentTracker,
        session_id: str,
    ) -> None:
        """Interrupt tool calls that exceeded tool_call_timeout_sec."""
        timed_out = tracker.timed_out_tools()
        if not timed_out:
            return
        for key, elapsed in timed_out:
            log.warning(
                "[%s] Tool call timed out (%s, %ds) — interrupting",
                self._rid,
                key[:8],
                elapsed,
            )
            await log_audit(
                self._run_id,
                "tool_timeout",
                {"agent_key": key, "elapsed_seconds": elapsed},
            )
        for key, _ in timed_out:
            tracker.clear_tool_state(key)
        max_elapsed = max(e for _, e in timed_out)
        await self._sandbox.session.interrupt(session_id)
        self._inbox.push(
            "inject",
            render_tool_timeout(max_elapsed // 60),
        )
