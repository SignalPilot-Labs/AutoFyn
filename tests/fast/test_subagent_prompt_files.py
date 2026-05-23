"""Tests that every registered subagent has a loadable markdown prompt file.

Guards against the failure mode of registering a SubagentDef in SUBAGENT_DEFS
without creating the corresponding prompt file — which causes a silent runtime
failure when build_agent_defs() tries to load the prompt.
"""

import pytest

from prompts.loader import load_markdown
from prompts.subagent import SUBAGENT_DEFS
from utils.models import SubagentDef


def _prompt_path(defn: SubagentDef) -> str:
    """Return the loader path for a subagent's markdown prompt."""
    return f"subagents/{defn.phase}/{defn.name}"


class TestSubagentPromptFiles:
    """Every SubagentDef in SUBAGENT_DEFS must have a non-empty prompt file."""

    @pytest.mark.parametrize("defn", SUBAGENT_DEFS, ids=lambda d: f"{d.phase}/{d.name}")
    def test_prompt_file_is_loadable(self, defn: SubagentDef) -> None:
        content = load_markdown(_prompt_path(defn))
        assert len(content) > 0, f"Prompt file for {defn.phase}/{defn.name} is empty"
