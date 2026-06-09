"""Tests for merge_subagents — shipped + repo overlay, local-wins.

The merge underpins the repo `.autofyn/subagents.json` feature: a repo spec
with a shipped name replaces it wholesale; a new name is appended; shipped
order is preserved. With no overlay the shipped list is returned unchanged.
"""

from config.constants import SubagentSpec
from config.loader import load_subagents, merge_subagents


def _spec(name: str, type_: str) -> SubagentSpec:
    return SubagentSpec(
        name=name,
        type=type_,
        description=f"{name} desc",
        model="sonnet",
        tools=("Read",),
        prompt_file=f".autofyn/subagents/{name}.md",
        needs_verification=False,
        needs_run_state=True,
    )


class TestMergeSubagents:
    """merge_subagents applies the repo overlay local-wins-by-name."""

    def test_none_returns_shipped(self) -> None:
        assert merge_subagents(None) == load_subagents()

    def test_empty_returns_shipped(self) -> None:
        assert merge_subagents(()) == load_subagents()

    def test_new_name_is_appended(self) -> None:
        shipped = load_subagents()
        merged = merge_subagents((_spec("ml-trainer", "build"),))
        assert len(merged) == len(shipped) + 1
        assert merged[-1].name == "ml-trainer"
        # Shipped agents are unchanged and keep their order.
        assert merged[: len(shipped)] == shipped

    def test_same_name_replaces_shipped_entry(self) -> None:
        shipped = load_subagents()
        override = _spec("code-reviewer", "review")
        merged = merge_subagents((override,))
        # Count is unchanged — replacement, not addition.
        assert len(merged) == len(shipped)
        by_name = {s.name: s for s in merged}
        assert by_name["code-reviewer"] is override
        assert by_name["code-reviewer"].description == "code-reviewer desc"
