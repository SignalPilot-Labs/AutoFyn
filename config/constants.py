"""Config package constants — shared across all containers."""

from dataclasses import dataclass

SANDBOX_REPO_DIR: str = "/home/agentuser/repo"

# Subagent registry — the shipped roster lives in config/subagents.json so
# both the agent (which builds the SDK agent defs) and the dashboard (which
# renders the toggle UI) read one source of truth.
SUBAGENTS_FILE: str = "subagents.json"

# Subagent phase ordering + display labels. The order drives both the
# orchestrator's grouped subagent list and the dashboard's phase grouping;
# SUBAGENT_TYPES is the validation set derived from these keys.
SUBAGENT_PHASE_ORDER: tuple[str, ...] = ("explore", "plan", "build", "review")
SUBAGENT_PHASE_LABELS: dict[str, str] = {
    "explore": "Explore",
    "plan": "Plan",
    "build": "Build",
    "review": "Review",
}

# Valid subagent `type` values (phase grouping). A roster entry with any
# other type is rejected at load.
SUBAGENT_TYPES: frozenset[str] = frozenset(SUBAGENT_PHASE_ORDER)


@dataclass(frozen=True)
class SubagentSpec:
    """One shipped subagent's metadata, loaded from config/subagents.json.

    `name`/`type`/`description` are UI-facing (rendered in the settings
    toggle). `model`/`tools`/`prompt_file` are runtime-only (consumed when
    building the SDK agent defs). `needs_verification`/`needs_run_state`
    control which prompt fragments get appended for this agent.
    """

    name: str
    type: str
    description: str
    model: str
    tools: tuple[str, ...]
    prompt_file: str
    needs_verification: bool
    needs_run_state: bool

# Stdout markers emitted by sandbox/connector during startup.
# AF_BOUND: sandbox emits when it binds to a port ({"port": N})
# AF_READY: connector emits after tunnel setup ({"host": str, "port": N})
# AF_QUEUED: emitted when a job is queued ({"backend_id": str})
AF_BOUND_MARKER: str = "AF_BOUND"
AF_READY_MARKER: str = "AF_READY"
AF_QUEUED_MARKER: str = "AF_QUEUED"
