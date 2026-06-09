"""Subagent registry consumer — loads the roster and builds SDK agent defs.

The shipped roster lives in `config/subagents.json` (one source of truth,
read by both the agent and the dashboard). `build_agent_defs()` loads each
agent's markdown system prompt, drops any disabled by the user, and returns
the plain dict the sandbox session endpoint expects under `options.agents`.

The orchestrator calls these subagents by name via the SDK's Agent tool.
"""

from config.constants import SubagentSpec
from config.loader import load_subagents
from prompts.loader import load_markdown, render_environment
from db.constants import SUPPORTED_SONNET
from utils.constants import TIER_OPUS


def _resolve_subagent_model(tier: str, user_model: str) -> str:
    """Resolve a subagent tier to a concrete model ID based on user selection.

    - User picks an opus model → opus-tier subagents get that model,
      sonnet-tier subagents get SUPPORTED_SONNET.
    - User picks a sonnet model → ALL subagents (including opus-tier) get
      that sonnet model. Sonnet runs are cost-conscious — no opus anywhere.
    """
    is_sonnet_run = "sonnet" in user_model
    if is_sonnet_run:
        return user_model
    if tier == TIER_OPUS:
        return user_model
    return SUPPORTED_SONNET


def enabled_subagents(disabled_subagents: list[str] | None) -> tuple[SubagentSpec, ...]:
    """Return the roster minus the user-disabled agents.

    Fail-safe: if the disable list would empty the roster, it is ignored and
    the full roster is returned — a run with zero subagents is a dead run.
    Unknown names in the disable list are simply not matched.
    """
    roster = load_subagents()
    if not disabled_subagents:
        return roster
    disabled = set(disabled_subagents)
    kept = tuple(spec for spec in roster if spec.name not in disabled)
    return kept if kept else roster


def build_agent_defs(
    round_number: int,
    host_mounts: list[dict[str, str]] | None,
    user_env_keys: list[str],
    user_model: str,
    tool_call_timeout_sec: int,
    base_branch: str,
    disabled_subagents: list[str] | None,
) -> dict[str, dict]:
    """Build subagent definitions for a single round.

    Loads the roster from `config/subagents.json`, drops any agent the user
    disabled, then for each remaining agent loads its markdown prompt and
    appends the shared fragments. Placeholders (`{ROUND_NUMBER}`,
    `{PRIOR_ROUND_NUMBER}`) are substituted with live values. Verification
    and run-state fragments are appended per the agent's `needs_*` flags.
    Subagents never receive `query/time-status` — only the orchestrator acts
    on time.
    """
    prior_round_number = max(round_number - 1, 0)
    env_block = render_environment(
        round_number=round_number,
        tool_call_timeout_min=tool_call_timeout_sec // 60,
        host_mounts=host_mounts,
        user_env_keys=user_env_keys,
        base_branch=base_branch,
    )
    git_rules = load_markdown("query/git-rules")
    dispatch_rules = load_markdown("query/dispatch-rules")
    verification_rules = load_markdown("query/verification-rules")
    per_role_rules = load_markdown("query/subagent-rules")
    run_state_context = (
        load_markdown("query/prior-round-context")
        if round_number > 1
        else None
    )
    result: dict[str, dict] = {}
    for spec in enabled_subagents(disabled_subagents):
        markdown_key = spec.prompt_file.removesuffix(".md")
        agent_body = _substitute(
            load_markdown(markdown_key),
            round_number,
            prior_round_number,
            base_branch,
        )
        prompt_parts = [agent_body, env_block, git_rules, dispatch_rules]
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
            "model": _resolve_subagent_model(spec.model, user_model),
            "tools": list(spec.tools),
        }
    return result


def _substitute(text: str, round_number: int, prior_round_number: int, base_branch: str) -> str:
    """Replace placeholders in a subagent prompt."""
    return (
        text
        .replace("{ROUND_NUMBER}", str(round_number))
        .replace("{PRIOR_ROUND_NUMBER}", str(prior_round_number))
        .replace("{BASE_BRANCH}", base_branch)
    )
