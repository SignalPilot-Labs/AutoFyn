"""Config package constants — shared across all containers."""

from dataclasses import dataclass

SANDBOX_REPO_DIR: str = "/home/agentuser/repo"

# Subagent registry — the shipped subagents live in config/subagents.json so
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

# Valid subagent `type` values (phase grouping). A subagent entry with any
# other type is rejected at load.
SUBAGENT_TYPES: frozenset[str] = frozenset(SUBAGENT_PHASE_ORDER)

# Valid `model` tier strings for a subagent. A repo-defined agent with any
# other tier is rejected at load (a typo would otherwise silently downgrade
# to sonnet). These are the canonical tier literals — the agent container's
# utils.constants.TIER_OPUS/TIER_SONNET hold the same values, but config is
# the lowest layer and cannot import from autofyn.
ALLOWED_SUBAGENT_MODELS: frozenset[str] = frozenset({"opus", "sonnet"})

# A repo `.autofyn/subagents.json` declares its own tools per entry — that list
# IS the allowlist for that agent (built-ins plus any MCP tool the repo wires in
# via its dashboard mcp_servers config). The only tools a repo agent may NEVER
# request are the session-gate tools: ending a round or the whole session is the
# orchestrator's job alone, so a subagent must not be able to call them.
# `SESSION_GATE_SERVER_NAME` mirrors the sandbox constant of the same name;
# config is the lowest layer and cannot import from sandbox, so it is duplicated
# here. A tool is forbidden if it is the bare server name or any `mcp__<server>__*`
# tool from it.
SESSION_GATE_SERVER_NAME: str = "session_gate"
SESSION_GATE_TOOL_PREFIX: str = f"mcp__{SESSION_GATE_SERVER_NAME}__"

# Upper bound on repo-defined subagents — caps the per-agent prompt-body
# HTTP reads done at bootstrap. Well above any realistic count.
MAX_REPO_SUBAGENTS: int = 32

# `needs_verification` is optional in a subagent entry — when omitted, the
# agent does not get the verification-rules fragment (run tests/typecheck).
# Only agents that inspect runnable code opt in. Repo-defined agents can omit
# it entirely.
DEFAULT_NEEDS_VERIFICATION: bool = False


@dataclass(frozen=True)
class SubagentSpec:
    """One subagent's metadata, from config/subagents.json or a repo overlay.

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
