"""Regression tests: a long tool call must not flag its agent stuck on completion.

A subagent that runs a single tool longer than subagent_idle_kill_sec was
being killed the instant the tool returned, because the idle clock
(_last_tool_at) was only refreshed when a tool *started*, never when it
finished. record_tool_done now resets the idle clock so "idle" measures
time since the last tool *finished*, not time since it started.

See run a1caaae9 — quant-reviewer sims running ~600s were stuck-killed on
completion against a 600s subagent_idle_kill_sec.
"""

import time

from agent_session.tracker import ORCHESTRATOR_ID, SubagentTracker
from utils.run_config import RunAgentConfig

_DEFAULT_RUN_CONFIG = RunAgentConfig(
    max_rounds=128,
    tool_call_timeout_sec=3600,
    session_idle_timeout_sec=120,
    subagent_idle_kill_sec=600,
)


class TestStuckLongToolCompletion:
    """A tool that ran longer than subagent_idle_kill_sec then completed."""

    def test_long_tool_completion_does_not_flag_stuck(self) -> None:
        """A single tool that ran > kill threshold is not stuck once it returns."""
        tracker = SubagentTracker(_DEFAULT_RUN_CONFIG)
        agent_id = "long-sim-agent"
        tracker.record_start(agent_id, "quant-reviewer")

        # Start a tool, then backdate its start to simulate a ~601s sim that
        # was in-flight the entire time (shielded from the stuck check).
        tracker.record_tool_use(agent_id)
        tracker._last_tool_at[agent_id] = time.time() - 601
        tracker._tool_started_at[agent_id] = time.time() - 601
        assert tracker.stuck_subagents() == []

        # Tool returns. The idle clock must reset to now, not stay at start.
        tracker.record_tool_done(agent_id)
        assert tracker.stuck_subagents() == []

    def test_idle_clock_resets_on_completion(self) -> None:
        """record_tool_done refreshes _last_tool_at to the completion time."""
        tracker = SubagentTracker(_DEFAULT_RUN_CONFIG)
        agent_id = "agent-1"
        tracker.record_start(agent_id, "quant-reviewer")
        tracker.record_tool_use(agent_id)
        tracker._last_tool_at[agent_id] = time.time() - 601

        before = time.time()
        tracker.record_tool_done(agent_id)
        assert tracker._last_tool_at[agent_id] >= before

    def test_genuine_idle_after_completion_still_flags_stuck(self) -> None:
        """After a tool finishes, real idleness past the threshold still flags."""
        tracker = SubagentTracker(_DEFAULT_RUN_CONFIG)
        agent_id = "agent-2"
        tracker.record_start(agent_id, "quant-reviewer")
        tracker.record_tool_use(agent_id)
        tracker.record_tool_done(agent_id)

        # Now the agent sits idle past the threshold with no tool running.
        tracker._last_tool_at[agent_id] = time.time() - 700
        stuck = tracker.stuck_subagents()
        assert len(stuck) == 1
        assert stuck[0].agent_id == agent_id

    def test_orchestrator_completion_leaves_idle_clock_untouched(self) -> None:
        """record_tool_done for the orchestrator must not touch _last_tool_at."""
        tracker = SubagentTracker(_DEFAULT_RUN_CONFIG)
        tracker.record_tool_use(None)
        tracker.record_tool_done(None)
        assert ORCHESTRATOR_ID not in tracker._last_tool_at
