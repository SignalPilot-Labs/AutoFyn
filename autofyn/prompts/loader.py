"""Prompt file loader and shared query renderers.

`load_markdown` reads a markdown file from the prompts directory.
`render_time_status` renders the time-status query with concrete minute
values — used by both the orchestrator prompt builder and the subagent
prompt builder so there is one source of truth for the wording.
"""

from config.constants import SandboxResources
from utils.constants import (
    BYTES_PER_GIB,
    PROMPTS_DIR,
    PROMPTS_FALLBACK_DIR,
    SANDBOX_KIND_DESCRIPTION_FALLBACK,
    SANDBOX_KIND_DESCRIPTIONS,
    SANDBOX_MEM_CAP_WARNING,
    SANDBOX_MEM_UNCAPPED_NOTE,
)


def load_markdown(name: str) -> str:
    """Load a markdown file by name (path relative to prompts/).

    Raises FileNotFoundError if the file does not exist in either
    `PROMPTS_DIR` (the runtime install location) or
    `PROMPTS_FALLBACK_DIR` (the sibling path during local dev).
    """
    for root in (PROMPTS_DIR, PROMPTS_FALLBACK_DIR):
        path = root / f"{name}.md"
        if path.exists():
            return path.read_text(encoding="utf-8").strip()
    raise FileNotFoundError(f"prompt file not found: {name}.md")


def render_tool_timeout(elapsed_minutes: int) -> str:
    """Render `query/tool-timeout.md` with the elapsed duration."""
    template = load_markdown("query/tool-timeout")
    return template.replace("{ELAPSED_MINUTES}", str(elapsed_minutes))


def render_idle_nudge(idle_seconds: int) -> str:
    """Render `query/idle-nudge.md` with the idle duration."""
    template = load_markdown("query/idle-nudge")
    return template.replace("{IDLE_SECONDS}", str(idle_seconds))


def render_stuck_recovery(
    agent_names: str,
    idle_threshold_min: int,
) -> str:
    """Render `query/stuck-recovery.md` with subagent details."""
    template = load_markdown("query/stuck-recovery")
    return (
        template
        .replace("{AGENT_NAMES}", agent_names)
        .replace("{IDLE_THRESHOLD_MIN}", str(idle_threshold_min))
    )


def render_time_status(
    duration_minutes: float,
    time_remaining_minutes: float,
) -> str:
    """Render `query/time-status.md` with concrete minute values."""
    template = load_markdown("query/time-status")
    return (
        template
        .replace("{TIME_REMAINING_MINUTES}", str(max(int(time_remaining_minutes), 0)))
        .replace("{DURATION_MINUTES}", str(int(duration_minutes)))
    )


def render_subagent_budget(
    budget_min: int,
    round_number: int,
) -> str:
    """Render `query/subagent-budget.md` — a subagent is one tool call for the
    orchestrator, so its wall-clock budget is the tool-call timeout.

    No timestamp is baked in: the prompt is built once at round-start, long
    before the subagent spawns, so any absolute time would be stale. Instead
    the subagent stamps its own start with `date -u` (it always has Bash).
    """
    template = load_markdown("query/subagent-budget")
    return (
        template
        .replace("{BUDGET_MIN}", str(budget_min))
        .replace("{ROUND_NUMBER}", str(round_number))
    )


def render_environment(
    round_number: int,
    tool_call_timeout_min: int,
    host_mounts: list[dict[str, str]] | None,
    user_env_keys: list[str],
    base_branch: str,
    sandbox_resources: SandboxResources,
) -> str:
    """Render `query/environment.md` with runtime values and host mounts."""
    template = load_markdown("query/environment")
    return (
        template
        .replace("{SANDBOX_RESOURCES_BLOCK}", _sandbox_resources_block(sandbox_resources))
        .replace("{ROUND_NUMBER}", str(round_number))
        .replace("{TOOL_CALL_TIMEOUT_MIN}", str(tool_call_timeout_min))
        .replace("{HOST_MOUNTS_BLOCK}", _host_mounts_block(host_mounts))
        .replace("{USER_ENV_BLOCK}", _user_env_block(user_env_keys))
        .replace("{BASE_BRANCH}", base_branch)
    )


def _sandbox_resources_block(resources: SandboxResources) -> str:
    """Render the sandbox's kind, CPU count, and memory budget.

    Replaces a hardcoded environment description so the prompt is honest
    for both local Docker and remote Slurm/Apptainer sandboxes, and warns
    the agent off node-level memory tools when a hard cap exists.
    """
    kind = SANDBOX_KIND_DESCRIPTIONS.get(
        resources.kind, SANDBOX_KIND_DESCRIPTION_FALLBACK,
    )
    if resources.mem_limit_bytes is None:
        memory = SANDBOX_MEM_UNCAPPED_NOTE
    else:
        gib = resources.mem_limit_bytes / BYTES_PER_GIB
        memory = f"Memory: {gib:.0f} GB hard cap. {SANDBOX_MEM_CAP_WARNING}"
    return (
        f"You run in {kind}. CPUs: {resources.cpu_count}. {memory}"
    )


def _user_env_block(keys: list[str]) -> str:
    """Render a list of user-provided env var names, or empty string when none."""
    if not keys:
        return ""
    safe = ", ".join(f"`{k}`" for k in keys)
    return f"User-provided environment variables available in this container: {safe}."


def _host_mounts_block(host_mounts: list[dict[str, str]] | None) -> str:
    """Render a 'Host mounts:\\n- ...' block, or empty string when there are none."""
    if not host_mounts:
        return ""
    lines = ["Host mounts:"]
    for m in host_mounts:
        mode = m.get("mode", "ro")
        access = "read-only" if mode == "ro" else "read-write"
        lines.append(f"- `{m['container_path']}` ({access})")
    return "\n".join(lines)
