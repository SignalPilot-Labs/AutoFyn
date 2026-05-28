"""Round archiver — persists /tmp/round-N between sandbox restarts.

The sandbox keeps writing reports to /tmp/round-N/ and /tmp/memory/rounds.json.
After each round the agent pulls that content into its own persistent
volume at /var/autofyn/rounds/<run_id>/. On a resumed run the agent
pushes it back into the new sandbox's /tmp before the first round
starts, so the orchestrator sees its prior-round files exactly where
it expects.

Isolation: the persistent volume is mounted ONLY on the agent. Sandboxes
cannot see each other's archives — no convention-based scoping to bypass.
"""

import logging
import re
from pathlib import Path

from sandbox_client.client import SandboxClient
from utils.constants import (
    MEMORY_DIR,
    ROUND_ARCHIVE_AGENT_DIR,
    ROUND_DIR_PREFIX,
)

log = logging.getLogger("memory.archiver")

_ROUND_DIR_RE = re.compile(r"^round-(\d+)$")


class RoundArchiver:
    """Bi-directional round archive between sandbox /tmp and agent volume.

    Public API:
        archive_round(n)   -> None     pull /tmp/round-N into the volume
        restore_all()      -> int      push archive back, return last round n
    """

    def __init__(self, sandbox: SandboxClient, run_id: str) -> None:
        self._sandbox = sandbox
        self._host_root = Path(ROUND_ARCHIVE_AGENT_DIR) / run_id
        self._memory_host = self._host_root / "memory"

    async def archive_round(self, round_number: int) -> None:
        """Pull /tmp/round-<n> and /tmp/memory/ into the host volume."""
        sandbox_dir = f"{ROUND_DIR_PREFIX}{round_number}"
        files = await self._sandbox.file_system.read_dir(sandbox_dir)
        if files is None:
            log.warning("archive_round: %s missing in sandbox", sandbox_dir)
            return
        host_dir = self._host_root / f"round-{round_number}"
        host_dir.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            (host_dir / name).write_text(content, encoding="utf-8")
        await self._archive_memory()
        log.info(
            "Archived round %d (%d files) to %s",
            round_number, len(files), host_dir,
        )

    async def restore_all(self) -> int:
        """Push every archived round and memory back into the sandbox.

        Returns the highest round number found (0 if nothing archived).
        """
        if not self._host_root.is_dir():
            return 0
        highest = 0
        for entry in sorted(self._host_root.iterdir()):
            if not entry.is_dir():
                continue
            m = _ROUND_DIR_RE.match(entry.name)
            if not m:
                continue
            n = int(m.group(1))
            files = {
                p.name: p.read_text(encoding="utf-8")
                for p in entry.iterdir()
                if p.is_file()
            }
            await self._sandbox.file_system.write_dir(
                f"{ROUND_DIR_PREFIX}{n}", files,
            )
            highest = max(highest, n)
        await self._restore_memory()
        if highest > 0:
            log.info(
                "Restored %d prior round(s) from %s", highest, self._host_root,
            )
        return highest

    async def _archive_memory(self) -> None:
        """Pull all files from /tmp/memory/ into the host volume."""
        memory_files = await self._sandbox.file_system.read_dir(MEMORY_DIR)
        if not memory_files:
            return
        self._memory_host.mkdir(parents=True, exist_ok=True)
        for name, content in memory_files.items():
            (self._memory_host / name).write_text(content, encoding="utf-8")

    async def _restore_memory(self) -> None:
        """Push archived memory files back into /tmp/memory/."""
        if not self._memory_host.is_dir():
            return
        files = {
            p.name: p.read_text(encoding="utf-8")
            for p in self._memory_host.iterdir()
            if p.is_file()
        }
        if files:
            await self._sandbox.file_system.write_dir(MEMORY_DIR, files)
