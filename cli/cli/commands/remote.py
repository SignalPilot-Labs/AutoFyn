"""Remote sandbox image update — `autofyn update --remote <docker|slurm>`.

Runs ON the remote machine itself (after installing the CLI there with
`pip install ~/.autofyn/cli`) to pull/refresh only the sandbox image. No
Docker stack, git checkout, or dashboard is involved — just the image pull.

- docker: `docker pull <repo>:<tag>` into the local docker store.
- slurm:  clear apptainer's layer cache (so `--force` can't reuse a stale
  image), then `apptainer pull --force <workdir>/sandbox.sif <repo>:<tag>`.

The work dir (where the SIF lives, next to per-run overlays) is resolved
flag > saved config > default, and saved on first use so it need not be
re-passed.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import typer
from rich.console import Console

from cli.config import load_remote_workdir, save_remote_workdir
from cli.constants import (
    BRANCH_TO_IMAGE_TAG,
    MKSQUASHFS_THREAD_ERROR,
    REMOTE_DEFAULT_IMAGE_TAG,
    REMOTE_DEFAULT_WORKDIR,
    REMOTE_SIF_NAME,
    REMOTE_TYPE_DOCKER,
    REMOTE_TYPES,
    SANDBOX_IMAGE_REPO,
)

console = Console()


def update_remote_sandbox(
    remote_type: str,
    branch: str | None,
    workdir_override: str | None,
) -> None:
    """Pull/refresh the sandbox image on this remote machine."""
    if remote_type not in REMOTE_TYPES:
        console.print(
            f"[red]Invalid --remote value '{remote_type}'. "
            f"Use one of: {', '.join(sorted(REMOTE_TYPES))}[/red]",
        )
        raise typer.Exit(code=1)

    tag = _resolve_tag(branch)
    image_ref = f"docker://{SANDBOX_IMAGE_REPO}:{tag}"

    if remote_type == REMOTE_TYPE_DOCKER:
        _pull_docker(tag)
    else:
        _pull_slurm(image_ref, workdir_override)


def _resolve_tag(branch: str | None) -> str:
    """Map --branch to an image tag, defaulting to stable when unset."""
    if branch is None:
        return REMOTE_DEFAULT_IMAGE_TAG
    return BRANCH_TO_IMAGE_TAG.get(branch, REMOTE_DEFAULT_IMAGE_TAG)


def _resolve_workdir(workdir_override: str | None) -> str:
    """Resolve the SIF work dir: flag > saved config > default.

    The chosen value is persisted so subsequent runs need no flag.
    """
    if workdir_override is not None:
        save_remote_workdir(workdir_override)
        return workdir_override
    saved = load_remote_workdir()
    if saved is not None:
        return saved
    save_remote_workdir(REMOTE_DEFAULT_WORKDIR)
    return REMOTE_DEFAULT_WORKDIR


def _pull_docker(tag: str) -> None:
    """Pull the sandbox image into the local docker store."""
    ref = f"{SANDBOX_IMAGE_REPO}:{tag}"
    console.print(f"[dim]→ docker pull {ref}[/dim]")
    # docker streams its own progress/errors to the terminal — inherit them.
    result = subprocess.run(["docker", "pull", ref])
    if result.returncode != 0:
        console.print("[red]docker pull failed (see output above)[/red]")
        raise typer.Exit(code=result.returncode)
    console.print(f"[green]✓[/green] Sandbox image updated (tag: {tag})")


def _pull_slurm(image_ref: str, workdir_override: str | None) -> None:
    """Clear the apptainer cache, then pull a fresh SIF into the work dir."""
    workdir = _resolve_workdir(workdir_override)
    sif_path = str(Path(workdir).expanduser() / REMOTE_SIF_NAME)

    # Clearing the cache is the whole point — without it `--force` reuses a
    # stale layer and silently pulls an old image. If it fails, stop: a pull
    # now would defeat the command.
    console.print("[dim]→ apptainer cache clean -f[/dim]")
    clean = subprocess.run(["apptainer", "cache", "clean", "-f"])
    if clean.returncode != 0:
        console.print("[red]apptainer cache clean failed — aborting to avoid a stale pull[/red]")
        raise typer.Exit(code=clean.returncode)

    console.print(f"[dim]→ apptainer pull --force {sif_path} {image_ref}[/dim]")
    result = subprocess.run(
        ["apptainer", "pull", "--force", sif_path, image_ref],
        capture_output=True,
        text=True,
    )
    if result.stdout:
        console.print(result.stdout.rstrip())
    if result.returncode != 0:
        _report_slurm_failure(result.stderr)
        raise typer.Exit(code=result.returncode)
    console.print(f"[green]✓[/green] Sandbox SIF updated at {sif_path}")


def _report_slurm_failure(stderr: str) -> None:
    """Print the pull failure, with a hint for the login-node thread limit."""
    console.print(f"[red]apptainer pull failed[/red]\n{stderr.rstrip()}")
    if MKSQUASHFS_THREAD_ERROR in stderr:
        console.print(
            "[yellow]This login node has a low thread limit. Run the pull "
            "on a compute node instead, e.g.:\n"
            "  srun --pty --mem=8G --time=00:30:00 "
            "autofyn update --remote slurm[/yellow]",
        )
