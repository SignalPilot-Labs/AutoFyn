"""Probe the sandbox's own compute allocation.

The sandbox reports `{kind, cpu_count, mem_limit_bytes}` on /health so the
agent can size parallel work against the box it actually runs in. This
matters most on HPC: a Slurm cgroup caps memory below the node's free RAM,
and `free`/`/proc/meminfo` there report the whole node, not the allocation
— reading them led an agent to launch parallel memory-heavy work and get
OOM-killed at the cgroup ceiling.

All values come from runtime sources, never config:
- kind: presence of Slurm/Apptainer env vars
- cpu_count: os.sched_getaffinity (the cores the process may actually use,
  respecting cgroup/Slurm pinning — unlike os.cpu_count which is host-wide)
- mem_limit_bytes: cgroup v2 memory.max ("max" → no hard cap → None)
"""

import logging
import os
from pathlib import Path

from config.constants import (
    SANDBOX_KIND_DOCKER,
    SANDBOX_KIND_SLURM,
    SandboxResources,
)
from constants import (
    APPTAINER_MARKER_ENV_VAR,
    CGROUP_MEMORY_MAX_PATH,
    CGROUP_UNLIMITED_SENTINEL,
    SLURM_JOB_ID_ENV_VAR,
)

log = logging.getLogger("sandbox.resources")


def probe_resources() -> SandboxResources:
    """Read the sandbox's kind, CPU count, and memory ceiling."""
    return SandboxResources(
        kind=_probe_kind(),
        # sched_getaffinity is Linux-only (the sandbox always runs on
        # Linux); it counts the cores the process may actually use,
        # respecting cgroup/Slurm pinning, unlike os.cpu_count.
        cpu_count=len(os.sched_getaffinity(0)),  # pyright: ignore[reportAttributeAccessIssue]
        mem_limit_bytes=_probe_mem_limit_bytes(),
    )


def _probe_kind() -> str:
    """Slurm/Apptainer if either marker env var is set, else gVisor Docker."""
    in_slurm = (
        SLURM_JOB_ID_ENV_VAR in os.environ
        or APPTAINER_MARKER_ENV_VAR in os.environ
    )
    return SANDBOX_KIND_SLURM if in_slurm else SANDBOX_KIND_DOCKER


def _probe_mem_limit_bytes() -> int | None:
    """cgroup v2 memory.max, or None when uncapped or unreadable.

    Returns None (treated as "no hard cap") when the file is absent (e.g.
    cgroup v1 hosts) so an unreadable limit never masquerades as a real
    ceiling the agent would trust.
    """
    path = Path(CGROUP_MEMORY_MAX_PATH)
    if not path.exists():
        log.warning("cgroup memory.max not found at %s — reporting uncapped", path)
        return None
    raw = path.read_text(encoding="utf-8").strip()
    if raw == CGROUP_UNLIMITED_SENTINEL:
        return None
    return int(raw)
