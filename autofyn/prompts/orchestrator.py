"""Orchestrator prompt builder — per-round system prompt assembly.

Each round gets a fresh Claude SDK session. `build_round_system_prompt`
loads the static `system.md` template, substitutes `{ROUND_NUMBER}`, and
appends dynamic context blocks (time status when time-locked, prior
rounds summary, prior-round file index, user messages).
"""

from claude_agent_sdk.types import SystemPromptPreset

from config.constants import SUBAGENT_PHASE_LABELS, SUBAGENT_PHASE_ORDER, SubagentSpec
from prompts.loader import load_markdown, render_environment, render_time_status
from prompts.subagent import enabled_subagents
from utils.constants import ROUND_DIR_PREFIX, STUCK_RECOVERY_REPORT_NAME
from utils.models import RoundContext, UserAction


def build_round_system_prompt(
    context: RoundContext,
    tool_call_timeout_sec: int,
) -> SystemPromptPreset:
    """Build the system prompt for a single round's orchestrator session."""
    template = load_markdown("system")
    body = _apply_placeholders(template, context)

    env_block = render_environment(
        round_number=context.round_number,
        tool_call_timeout_min=tool_call_timeout_sec // 60,
        host_mounts=context.host_mounts,
        user_env_keys=context.user_env_keys,
        base_branch=context.base_branch,
        sandbox_resources=context.sandbox_resources,
    )
    sections: list[str] = [body, env_block, load_markdown("query/git-rules")]

    if context.duration_minutes > 0:
        sections.append(
            render_time_status(
                context.duration_minutes,
                context.time_remaining_minutes,
            )
        )

    if context.user_activity:
        sections.append(_user_activity_block(context.user_activity))

    return SystemPromptPreset(
        type="preset",
        preset="claude_code",
        append="\n\n".join(sections),
    )


# ── Placeholder substitution ─────────────────────────────────────────


def _apply_placeholders(template: str, context: RoundContext) -> str:
    """Replace `{ROUND_NUMBER}` and `{AVAILABLE_SUBAGENTS}` in the template."""
    return (
        template
        .replace("{ROUND_NUMBER}", str(context.round_number))
        .replace(
            "{AVAILABLE_SUBAGENTS}",
            _render_subagent_list(context.subagent_specs, context.disabled_subagents),
        )
    )


def _render_subagent_list(
    subagent_specs: tuple[SubagentSpec, ...],
    disabled_subagents: list[str],
) -> str:
    """Render the enabled subagents grouped by phase, as markdown bullets.

    Works over the merged subagent specs (shipped + repo overlay). Disabled
    agents are omitted entirely so the orchestrator never sees a name it cannot
    dispatch. Phases with no enabled agent are skipped.
    """
    specs = enabled_subagents(subagent_specs, disabled_subagents)
    lines: list[str] = []
    for phase in SUBAGENT_PHASE_ORDER:
        in_phase = [s for s in specs if s.type == phase]
        if not in_phase:
            continue
        lines.append(f"**{SUBAGENT_PHASE_LABELS[phase]}**")
        for spec in in_phase:
            lines.append(f"- `{spec.name}` — {spec.description}")
        lines.append("")
    return "\n".join(lines).strip()


# ── Dynamic context blocks ───────────────────────────────────────────


def _user_activity_block(activity: list[UserAction]) -> str:
    """Chronological timeline of user actions across the entire run."""
    lines = ["## User activity (chronological)"]
    for action in activity:
        timestamp = action.timestamp[:19].replace("T", " ")
        if action.kind == "task":
            lines.append(f'- [{timestamp}] Task started: "{action.text}"')
        elif action.kind == "message":
            lines.append(f'- [{timestamp}] User message: "{action.text}"')
        else:
            lines.append(f"- [{timestamp}] {action.text}")
    lines.append(
        "Priority: The user's latest message takes highest priority.",
    )
    return "\n".join(lines)


def build_initial_prompt(
    round_number: int,
    task: str,
    is_grace_round: bool,
    prior_round_had_stuck_recovery: bool,
) -> str:
    """Short per-round kickoff message paired with the round system prompt."""
    prompt = f"Round {round_number} is starting.\n\nTask:\n{task.strip()}"
    if prior_round_had_stuck_recovery:
        prior = round_number - 1
        prompt += (
            f"\n\nNote: last round a subagent was force-interrupted for being stuck, "
            f"which ended the round early. Read `{ROUND_DIR_PREFIX}{prior}/"
            f"{STUCK_RECOVERY_REPORT_NAME}` and adapt your approach before re-dispatching "
            f"that agent type."
        )
    if is_grace_round:
        prompt += "\n\nTime lock has expired. This is your final round. Wrap up, ship it, call end_session."
    return prompt
