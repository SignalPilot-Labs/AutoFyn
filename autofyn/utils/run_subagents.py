"""Per-run subagent list resolved after the target repo is cloned.

The shipped subagents live in `config/subagents.json` (loaded locally by the
agent). A target repo may carry its own `.autofyn/subagents.json` that
overrides and extends them — merged local-repo-wins-by-name. This module reads
that file from the sandbox over HTTP (the repo lives in the sandbox, not the
agent), validates it fail-fast, merges it with the shipped subagents, and
prefetches each repo agent's prompt body so the per-round prompt builder can
stay synchronous.

The repo file is untrusted (the AI agent can write it), so every entry is
validated at load: known `type`, known `model` tier, whitelisted `tools`, and
a `prompt_file` constrained to within the repo. Any violation fails the run.
"""

import json
from dataclasses import dataclass
from pathlib import PurePosixPath

from config.constants import (
    ALLOWED_SUBAGENT_MODELS,
    ALLOWED_SUBAGENT_TOOLS,
    DEFAULT_NEEDS_VERIFICATION,
    MAX_REPO_SUBAGENTS,
    SUBAGENT_TYPES,
    SubagentSpec,
)
from config.loader import merge_subagents
from sandbox_client.client import SandboxClient
from utils.constants import WORK_DIR

_REPO_SUBAGENTS_PATH = f"{WORK_DIR}/.autofyn/subagents.json"


@dataclass(frozen=True)
class SubagentConfig:
    """The subagents resolved for one run: the merged list and repo bodies.

    `specs` is the shipped subagents merged with the repo overlay (repo wins
    by name). `bodies` holds ONLY the repo agents' prompt bodies, keyed by
    name — the prompt builder uses it to override local markdown for those
    agents; shipped agents are absent and load from disk. Built once at
    bootstrap, read every round (the same lifecycle as RunAgentConfig).
    """

    specs: tuple[SubagentSpec, ...]
    bodies: dict[str, str]


async def load_repo_subagents(sandbox: SandboxClient) -> SubagentConfig:
    """Read, validate, merge, and prefetch the target repo's subagent overlay.

    Returns the shipped subagents with empty bodies when the repo has no
    `.autofyn/subagents.json`. Otherwise merges the repo's entries over the
    shipped subagents and prefetches each repo agent's prompt body. Fails fast
    on malformed JSON, an invalid entry, or a missing body.
    """
    raw = await sandbox.file_system.read(_REPO_SUBAGENTS_PATH)
    if raw is None:
        return SubagentConfig(specs=merge_subagents(None), bodies={})

    repo_specs = _parse_repo_specs(json.loads(raw))
    specs = merge_subagents(repo_specs)
    bodies = await _prefetch_repo_bodies(sandbox, repo_specs)
    return SubagentConfig(specs=specs, bodies=bodies)


def _parse_repo_specs(raw: object) -> tuple[SubagentSpec, ...]:
    """Validate the raw repo JSON into SubagentSpecs, fail-fast per entry."""
    if not isinstance(raw, list):
        raise RuntimeError(".autofyn/subagents.json must be a JSON array")
    if len(raw) > MAX_REPO_SUBAGENTS:
        raise RuntimeError(
            f".autofyn/subagents.json has {len(raw)} agents — "
            f"max is {MAX_REPO_SUBAGENTS}"
        )
    specs: list[SubagentSpec] = []
    seen: set[str] = set()
    for entry in raw:
        spec = _parse_repo_spec(entry)
        if spec.name in seen:
            raise RuntimeError(f"Duplicate repo subagent name: {spec.name}")
        seen.add(spec.name)
        specs.append(spec)
    return tuple(specs)


def _parse_repo_spec(entry: object) -> SubagentSpec:
    """Validate one untrusted repo entry into a SubagentSpec, fail-fast."""
    if not isinstance(entry, dict):
        raise RuntimeError("Each repo subagent entry must be a JSON object")
    name = entry["name"]
    if entry["type"] not in SUBAGENT_TYPES:
        raise RuntimeError(
            f"Repo subagent '{name}' has unknown type '{entry['type']}' — "
            f"must be one of {sorted(SUBAGENT_TYPES)}"
        )
    if entry["model"] not in ALLOWED_SUBAGENT_MODELS:
        raise RuntimeError(
            f"Repo subagent '{name}' has unknown model tier '{entry['model']}' — "
            f"must be one of {sorted(ALLOWED_SUBAGENT_MODELS)}"
        )
    tools = tuple(entry["tools"])
    unknown_tools = set(tools) - ALLOWED_SUBAGENT_TOOLS
    if unknown_tools:
        raise RuntimeError(
            f"Repo subagent '{name}' requests unknown tools: "
            f"{sorted(unknown_tools)} — allowed: {sorted(ALLOWED_SUBAGENT_TOOLS)}"
        )
    _validate_repo_prompt_path(name, entry["prompt_file"])
    return SubagentSpec(
        name=name,
        type=entry["type"],
        description=entry["description"],
        model=entry["model"],
        tools=tools,
        prompt_file=entry["prompt_file"],
        needs_verification=entry.get(
            "needs_verification", DEFAULT_NEEDS_VERIFICATION
        ),
        needs_run_state=entry["needs_run_state"],
    )


def _validate_repo_prompt_path(name: str, prompt_file: str) -> None:
    """Reject a repo prompt_file that escapes the repo (fail-fast)."""
    if not prompt_file:
        raise RuntimeError(f"Repo subagent '{name}' has an empty prompt_file")
    if prompt_file.startswith("/"):
        raise RuntimeError(
            f"Repo subagent '{name}' prompt_file must be repo-relative, "
            f"not absolute: {prompt_file}"
        )
    if ".." in PurePosixPath(prompt_file).parts:
        raise RuntimeError(
            f"Repo subagent '{name}' prompt_file must stay within the repo "
            f"(no '..'): {prompt_file}"
        )


async def _prefetch_repo_bodies(
    sandbox: SandboxClient,
    repo_specs: tuple[SubagentSpec, ...],
) -> dict[str, str]:
    """Fetch each repo agent's prompt body from the sandbox, fail-fast."""
    bodies: dict[str, str] = {}
    for spec in repo_specs:
        body = await sandbox.file_system.read(f"{WORK_DIR}/{spec.prompt_file}")
        if body is None:
            raise RuntimeError(
                f"Repo subagent '{spec.name}' prompt_file not found: "
                f"{spec.prompt_file}"
            )
        bodies[spec.name] = body
    return bodies
