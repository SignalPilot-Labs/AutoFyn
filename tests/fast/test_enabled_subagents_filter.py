"""Tests for enabled_subagents — the user-disable filter over the roster.

Pins the contract:
- No disable list → full roster.
- Disabling some agents removes exactly those (by name).
- Unknown names in the disable list are ignored (not matched).
- The all-disabled case is a no-op fail-safe: a run needs ≥1 subagent, so a
  disable list covering the whole roster returns the full roster unchanged.
"""

from config.loader import load_subagents
from prompts.subagent import enabled_subagents


class TestEnabledSubagents:
    """enabled_subagents applies the disable filter with a never-empty guard."""

    def test_none_returns_full_roster(self) -> None:
        roster = load_subagents()
        assert enabled_subagents(None) == roster

    def test_empty_list_returns_full_roster(self) -> None:
        roster = load_subagents()
        assert enabled_subagents([]) == roster

    def test_disabling_removes_named_agents(self) -> None:
        kept = enabled_subagents(["ui-reviewer", "security-reviewer"])
        names = {s.name for s in kept}
        assert "ui-reviewer" not in names
        assert "security-reviewer" not in names
        assert "architect" in names

    def test_unknown_names_ignored(self) -> None:
        roster = load_subagents()
        kept = enabled_subagents(["not-a-real-agent"])
        assert kept == roster

    def test_disabling_all_falls_back_to_full_roster(self) -> None:
        roster = load_subagents()
        all_names = [s.name for s in roster]
        # Disabling every agent would leave a dead run — guard returns full roster.
        assert enabled_subagents(all_names) == roster
