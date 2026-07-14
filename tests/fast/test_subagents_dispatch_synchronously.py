"""Regression test: subagents must be pinned to synchronous dispatch.

The CLI's Agent tool defaults `run_in_background` to true: the orchestrator
dispatches, gets control back before the subagent has run, and ends its turn
saying it will report the result "as soon as it completes". Nothing collects
it, the round ends, and the backgrounded subagent is killed mid-flight.

Observed as runs with N subagent_start events and zero subagent_complete,
rounds ending in ~30s with no report files written. Reproduced directly
against the CLI: with background unset the dispatching turn ended before the
subagent's Bash ever ran; with background=False the result came back inline.

Nothing in AutoFyn changed to cause this — the default arrived through the
unpinned CLI, which is why runs on untouched branches broke too.
"""

from __future__ import annotations

from constants import SUBAGENT_RUNS_IN_BACKGROUND
from sdk.utils import parse_agents

_RAW_AGENTS = {
    "math-explorer": {
        "description": "explores the problem",
        "prompt": "You are an explorer.",
        "model": "claude-fable-5",
        "tools": ["Bash", "Read"],
    },
    "code-reviewer": {
        "description": "reviews the diff",
        "prompt": "You are a reviewer.",
        "model": "claude-fable-5",
        "tools": ["Read"],
    },
}


class TestSubagentsDispatchSynchronously:
    """Every agent definition must block the orchestrator until it finishes."""

    def test_the_constant_pins_foreground_dispatch(self) -> None:
        """Backgrounding is the bug; the constant must never be flipped to True."""
        assert SUBAGENT_RUNS_IN_BACKGROUND is False

    def test_parsed_agents_are_not_backgrounded(self) -> None:
        """background must reach AgentDefinition, not be left None (the CLI default)."""
        agents = parse_agents(_RAW_AGENTS)

        assert agents
        for name, defn in agents.items():
            assert defn.background is False, f"{name} would dispatch in the background"

    def test_every_agent_is_pinned_not_just_the_first(self) -> None:
        """A per-agent field set in a loop must cover all of them."""
        agents = parse_agents(_RAW_AGENTS)

        assert len(agents) == len(_RAW_AGENTS)
        assert {d.background for d in agents.values()} == {False}

    def test_parsing_preserves_the_rest_of_the_definition(self) -> None:
        """Pinning dispatch must not disturb prompt, model, or tools."""
        agents = parse_agents(_RAW_AGENTS)

        explorer = agents["math-explorer"]
        assert explorer.prompt == "You are an explorer."
        assert explorer.model == "claude-fable-5"
        assert explorer.tools == ["Bash", "Read"]
