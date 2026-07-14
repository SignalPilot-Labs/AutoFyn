"""Tests for build_agent_defs honouring the disabled-subagents list.

A disabled agent must not appear in the SDK `options.agents` dict, so the
orchestrator has no way to dispatch it. Enabled agents are unaffected.
"""

from config.constants import SANDBOX_KIND_DOCKER, SandboxResources
from config.loader import merge_subagents
from common.constants import PROVIDER_ANTHROPIC, SUPPORTED_OPUS
from prompts.subagent import build_agent_defs

_TEST_RESOURCES = SandboxResources(
    kind=SANDBOX_KIND_DOCKER, cpu_count=8, mem_limit_bytes=None,
)


def _defs(disabled: list[str] | None) -> dict[str, dict]:
    return build_agent_defs(
        round_number=1,
        host_mounts=None,
        user_env_keys=[],
        user_model=SUPPORTED_OPUS,
        provider=PROVIDER_ANTHROPIC,
        tool_call_timeout_sec=600,
        base_branch="main",
        disabled_subagents=disabled,
        subagent_specs=merge_subagents(None),
        repo_prompt_bodies={},
        sandbox_resources=_TEST_RESOURCES,
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
