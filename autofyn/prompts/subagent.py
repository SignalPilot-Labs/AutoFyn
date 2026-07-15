"""Subagent registry consumer — builds SDK agent defs from the merged list.

The subagent list is the shipped `config/subagents.json` merged with the
target repo's `.autofyn/subagents.json` overlay (built at bootstrap by
`utils.run_subagents`). `build_agent_defs()` loads each agent's system
prompt — locally for shipped agents, from the prefetched repo bodies for
repo agents — drops any the user disabled, and returns the plain dict the
sandbox session endpoint expects under `options.agents`.

The orchestrator calls these subagents by name via the SDK's Agent tool.
"""

from config.constants import SandboxResources, SubagentSpec
from prompts.loader import load_markdown, render_environment, render_subagent_budget
from common.constants import (
    TIER_OPUS,
    TIER_SONNET,
    api_model_for,
    tier_for_model,
    workhorse_for_model,
)


def _resolve_subagent_model(tier: str, user_model: str, provider: str) -> str:
    """Resolve a subagent tier to the provider's API slug for its model.

    Tiers are roles: opus = flagship, sonnet = workhorse. The run's provider is
    user-picked. An opus-class run gives opus-tier subagents the user's model and
    sonnet-tier subagents the workhorse; a sonnet-class run gives every tier the
    user's model (cost-conscious). The result is the provider's API slug, since
    the subagent ``model`` field feeds the SDK directly.
    """
    if tier_for_model(user_model) == TIER_SONNET or tier == TIER_OPUS:
        return api_model_for(user_model, provider)
    return api_model_for(workhorse_for_model(user_model), provider)


def enabled_subagents(
    subagent_specs: tuple[SubagentSpec, ...],
    disabled_subagents: list[str] | None,
) -> tuple[SubagentSpec, ...]:
    """Return the merged subagent specs minus the user-disabled agents.

    The specs are already merged (shipped + repo overlay) upstream, so the
    disable filter applies to both shipped and repo agents. Fail-safe: if the
    disable list would empty the specs, it is ignored and the full set is
    returned — a run with zero subagents is a dead run. Unknown names in the
    disable list are simply not matched.
    """
    if not disabled_subagents:
        return subagent_specs
    disabled = set(disabled_subagents)
    kept = tuple(spec for spec in subagent_specs if spec.name not in disabled)
    return kept if kept else subagent_specs


def build_agent_defs(
    round_number: int,
    host_mounts: list[dict[str, str]] | None,
    user_env_keys: list[str],
    user_model: str,
    provider: str,
    tool_call_timeout_sec: int,
    base_branch: str,
    disabled_subagents: list[str] | None,
    subagent_specs: tuple[SubagentSpec, ...],
    repo_prompt_bodies: dict[str, str],
    sandbox_resources: SandboxResources,
) -> dict[str, dict]:
    """Build subagent definitions for a single round.

    Takes the merged subagent list (shipped + repo overlay), drops any agent
    the user disabled, then for each remaining agent resolves its prompt body —
    locally for shipped agents, from `repo_prompt_bodies` for repo agents — and
    appends the shared fragments. Placeholders (`{ROUND_NUMBER}`,
    `{PRIOR_ROUND_NUMBER}`) are substituted with live values. Verification and
    run-state fragments are appended per the agent's `needs_*` flags. Every
    subagent gets a budget line (it is one orchestrator tool call, so its
    wall-clock cap is `tool_call_timeout_sec`); they never receive the
    orchestrator's `query/time-status` run-duration query.
    """
    prior_round_number = max(round_number - 1, 0)
    env_block = render_environment(
        round_number=round_number,
        tool_call_timeout_min=tool_call_timeout_sec // 60,
        host_mounts=host_mounts,
        user_env_keys=user_env_keys,
        base_branch=base_branch,
        sandbox_resources=sandbox_resources,
    )
    budget_block = render_subagent_budget(
        budget_min=tool_call_timeout_sec // 60,
        round_number=round_number,
    )
    git_rules = load_markdown("query/git-rules")
    dispatch_rules = load_markdown("query/dispatch-rules")
    verification_rules = load_markdown("query/verification-rules")
    per_role_rules = load_markdown("query/subagent-rules")
    run_state_context = (
        load_markdown("query/prior-round-context") if round_number > 1 else None
    )
    result: dict[str, dict] = {}
    for spec in enabled_subagents(subagent_specs, disabled_subagents):
        agent_body = _substitute(
            _resolve_body(spec, repo_prompt_bodies),
            round_number,
            prior_round_number,
            base_branch,
        )
        prompt_parts = [agent_body, env_block, budget_block, git_rules, dispatch_rules]
        if spec.needs_verification:
            prompt_parts.append(verification_rules)
        if run_state_context and spec.needs_run_state:
            prompt_parts.append(run_state_context)
        if spec.needs_run_state:
            prompt_parts.append(
                per_role_rules
                .replace("{AGENT_NAME}", spec.name)
                .replace("{ROUND_NUMBER}", str(round_number))
            )
        result[spec.name] = {
            "description": spec.description,
            "prompt": "\n\n".join(prompt_parts),
            "model": _resolve_subagent_model(spec.model, user_model, provider),
            "tools": list(spec.tools),
        }
    return result


def _resolve_body(spec: SubagentSpec, repo_prompt_bodies: dict[str, str]) -> str:
    """Return the raw prompt body for an agent.

    A repo agent's body was prefetched from the repo at bootstrap and lives in
    `repo_prompt_bodies`; a shipped agent loads its markdown from the local
    install dir.
    """
    repo_body = repo_prompt_bodies.get(spec.name)
    if repo_body is not None:
        return repo_body
    return load_markdown(spec.prompt_file.removesuffix(".md"))


def _substitute(text: str, round_number: int, prior_round_number: int, base_branch: str) -> str:
    """Replace placeholders in a subagent prompt."""
    return (
        text
        .replace("{ROUND_NUMBER}", str(round_number))
        .replace("{PRIOR_ROUND_NUMBER}", str(prior_round_number))
        .replace("{BASE_BRANCH}", base_branch)
    )
