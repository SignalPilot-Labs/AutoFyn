"""Tests for build_agent_defs honouring the disabled-subagents list.

A disabled agent must not appear in the SDK `options.agents` dict, so the
orchestrator has no way to dispatch it. Enabled agents are unaffected.
"""

from config.loader import merge_subagents
from db.constants import SUPPORTED_OPUS
from prompts.subagent import build_agent_defs


def _defs(disabled: list[str] | None) -> dict[str, dict]:
    return build_agent_defs(
        round_number=1,
        host_mounts=None,
        user_env_keys=[],
        user_model=SUPPORTED_OPUS,
        tool_call_timeout_sec=600,
        base_branch="main",
        disabled_subagents=disabled,
        subagent_specs=merge_subagents(None),
        repo_prompt_bodies={},
    )


class TestBuildAgentDefsDisabled:
    """build_agent_defs drops disabled agents from the returned dict."""

    def test_no_disable_includes_all(self) -> None:
        defs = _defs(None)
        assert "code-reviewer" in defs
        assert "ui-reviewer" in defs

    def test_disabled_agent_absent(self) -> None:
        defs = _defs(["ui-reviewer"])
        assert "ui-reviewer" not in defs
        # A sibling agent is still present.
        assert "code-reviewer" in defs

    def test_remaining_defs_well_formed(self) -> None:
        defs = _defs(["security-reviewer"])
        entry = defs["architect"]
        assert entry["description"]
        assert entry["prompt"]
        assert entry["model"]
        assert isinstance(entry["tools"], list)
