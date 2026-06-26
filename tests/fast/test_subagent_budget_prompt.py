"""Tests for the subagent wall-clock budget line.

A subagent is a single tool call from the orchestrator's view, so its
lifetime cap is `tool_call_timeout_sec`. The budget line tells it how long
it has and to save its report before then. The timestamp it cites MUST be
UTC — a local-time label would mislead the subagent about its deadline.
"""

import re

from prompts.loader import render_subagent_budget


class TestRenderSubagentBudget:
    """render_subagent_budget substitutes budget, UTC start, and round."""

    def test_substitutes_all_placeholders(self) -> None:
        out = render_subagent_budget(
            budget_min=60, start_time_utc="2026-06-26 14:30", round_number=3,
        )
        assert "60 min" in out
        assert "2026-06-26 14:30" in out
        assert "round-3" in out
        # No raw placeholders left behind.
        assert "{" not in out and "}" not in out

    def test_labels_the_time_as_utc(self) -> None:
        # The whole point: the cited time must be marked UTC so the subagent
        # doesn't misread it as local time and miscompute its deadline.
        out = render_subagent_budget(
            budget_min=60, start_time_utc="2026-06-26 09:05", round_number=1,
        )
        assert re.search(r"2026-06-26 09:05\s*UTC", out)
