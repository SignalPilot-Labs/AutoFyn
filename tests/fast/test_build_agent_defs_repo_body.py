"""Test: build_agent_defs uses the prefetched body for a repo agent.

A repo-defined agent's prompt body comes from the prefetched bodies dict, not
from local markdown; a shipped agent still loads its markdown from disk. This
pins the one branch in _resolve_body.
"""

from config.constants import SANDBOX_KIND_DOCKER, SandboxResources, SubagentSpec
from config.loader import merge_subagents
from common.constants import SUPPORTED_OPUS
from prompts.subagent import build_agent_defs

_TEST_RESOURCES = SandboxResources(
    kind=SANDBOX_KIND_DOCKER, cpu_count=8, mem_limit_bytes=None,
)

_REPO_SPEC = SubagentSpec(
    name="ml-trainer",
    type="build",
    description="trains models",
    model="sonnet",
    tools=("Read", "Bash"),
    prompt_file=".autofyn/subagents/ml-trainer.md",
    needs_verification=False,
    needs_run_state=True,
)


class TestBuildAgentDefsRepoBody:
    """build_agent_defs routes prompt bodies by presence in repo_prompt_bodies."""

    def _defs(self) -> dict[str, dict]:
        merged = merge_subagents((_REPO_SPEC,))
        return build_agent_defs(
            round_number=1,
            host_mounts=None,
            user_env_keys=[],
            user_model=SUPPORTED_OPUS,
            tool_call_timeout_sec=600,
            base_branch="main",
            disabled_subagents=None,
            subagent_specs=merged,
            repo_prompt_bodies={"ml-trainer": "ML TRAINER PROMPT BODY"},
            sandbox_resources=_TEST_RESOURCES,
        )

    def test_repo_agent_uses_prefetched_body(self) -> None:
        defs = self._defs()
        assert "ML TRAINER PROMPT BODY" in defs["ml-trainer"]["prompt"]

    def test_shipped_agent_still_present_and_well_formed(self) -> None:
        defs = self._defs()
        # A shipped agent (body loaded from local markdown) is unaffected.
        assert defs["architect"]["prompt"]
        assert defs["architect"]["description"]
