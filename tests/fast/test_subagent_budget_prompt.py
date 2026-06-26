"""Tests for the subagent wall-clock budget line.

A subagent is a single tool call from the orchestrator's view, so its
lifetime cap is `tool_call_timeout_sec`. The prompt is built once at
round-start, long before the subagent spawns, so it bakes in NO absolute
timestamp (which would be stale). Instead it tells the subagent to stamp
its own start with `date -u` and save its report before the budget runs out.
"""

from prompts.loader import render_subagent_budget


class TestRenderSubagentBudget:
    """render_subagent_budget substitutes the budget and round, no stale time."""

    def test_substitutes_placeholders(self) -> None:
        out = render_subagent_budget(budget_min=60, round_number=3)
        assert "60 min" in out
        assert "round-3" in out
        # No raw placeholders left behind.
        assert "{" not in out and "}" not in out

    def test_tells_subagent_to_self_stamp_its_start(self) -> None:
        # The fix for stale timestamps: the subagent reads its own clock
        # rather than trusting a build-time value baked into the prompt.
        out = render_subagent_budget(budget_min=60, round_number=1)
        assert "date -u" in out

    def test_bakes_no_absolute_timestamp(self) -> None:
        # A digit-bearing date/time would mean a stale build-time value crept
        # back in. The only number should be the budget itself.
        out = render_subagent_budget(budget_min=45, round_number=2)
        assert "45 min" in out
        # No "HH:MM" or "YYYY-MM-DD" pattern.
        assert ":" not in out
