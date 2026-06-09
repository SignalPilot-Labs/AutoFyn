"""Tests for _render_subagent_list — the dynamic '# Subagents' block.

The orchestrator's system prompt must list only the enabled agents, grouped
by phase. A disabled agent's name must never appear, so the orchestrator
cannot try to dispatch an agent that was filtered out of options.agents.

The list passed in is the merged (shipped + repo) one; here we use the
shipped-only list (`merge_subagents(None)`).
"""

from config.loader import merge_subagents
from prompts.orchestrator import _render_subagent_list


class TestRenderSubagentList:
    """_render_subagent_list reflects the enabled subagents, grouped by phase."""

    def test_lists_all_when_none_disabled(self) -> None:
        rendered = _render_subagent_list(merge_subagents(None), [])
        assert "`architect`" in rendered
        assert "`code-reviewer`" in rendered
        # Phase headings are present.
        assert "**Plan**" in rendered
        assert "**Review**" in rendered

    def test_disabled_agent_omitted(self) -> None:
        rendered = _render_subagent_list(merge_subagents(None), ["ui-reviewer"])
        assert "`ui-reviewer`" not in rendered
        # A sibling reviewer remains listed.
        assert "`code-reviewer`" in rendered

    def test_phase_heading_dropped_when_phase_empty(self) -> None:
        # Disabling every explore agent removes the Explore heading entirely.
        rendered = _render_subagent_list(
            merge_subagents(None), ["code-explorer", "security-explorer"]
        )
        assert "**Explore**" not in rendered
        assert "`code-explorer`" not in rendered
