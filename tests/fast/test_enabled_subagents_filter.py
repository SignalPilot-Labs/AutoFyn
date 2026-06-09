"""Tests for enabled_subagents — the user-disable filter over the subagents.

Pins the contract:
- No disable list → full list.
- Disabling some agents removes exactly those (by name).
- Unknown names in the disable list are ignored (not matched).
- The all-disabled case is a no-op fail-safe: a run needs ≥1 subagent, so a
  disable list covering everything returns the full list unchanged.

The list passed in is the merged (shipped + repo) one; here we use the
shipped-only list (`merge_subagents(None)`).
"""

from config.loader import merge_subagents
from prompts.subagent import enabled_subagents


class TestEnabledSubagents:
    """enabled_subagents applies the disable filter with a never-empty guard."""

    def test_none_returns_full_list(self) -> None:
        subagents = merge_subagents(None)
        assert enabled_subagents(subagents, None) == subagents

    def test_empty_list_returns_full_list(self) -> None:
        subagents = merge_subagents(None)
        assert enabled_subagents(subagents, []) == subagents

    def test_disabling_removes_named_agents(self) -> None:
        subagents = merge_subagents(None)
        kept = enabled_subagents(subagents, ["ui-reviewer", "security-reviewer"])
        names = {s.name for s in kept}
        assert "ui-reviewer" not in names
        assert "security-reviewer" not in names
        assert "architect" in names

    def test_unknown_names_ignored(self) -> None:
        subagents = merge_subagents(None)
        kept = enabled_subagents(subagents, ["not-a-real-agent"])
        assert kept == subagents

    def test_disabling_all_falls_back_to_full_list(self) -> None:
        subagents = merge_subagents(None)
        all_names = [s.name for s in subagents]
        # Disabling every agent would leave a dead run — guard returns full list.
        assert enabled_subagents(subagents, all_names) == subagents
