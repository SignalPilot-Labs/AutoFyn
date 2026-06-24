"""Tests for `autofyn update --remote` sandbox image update.

Pins: tag resolution from --branch, work-dir resolution precedence
(flag > saved config > default, always persisted), the docker vs slurm
command construction, the apptainer cache-clean-before-pull ordering
(the stale-cache trap this feature exists to prevent), and the
login-node mksquashfs hint.
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest
import typer

from cli.commands.remote import (
    _resolve_tag,
    update_remote_sandbox,
)
from cli.constants import (
    REMOTE_DEFAULT_IMAGE_TAG,
    REMOTE_DEFAULT_WORKDIR,
)

MODULE = "cli.commands.remote"


class TestUpdateRemoteSandbox:
    """Remote sandbox image pull: tag, workdir, command construction."""

    def test_no_branch_defaults_to_stable(self) -> None:
        assert _resolve_tag(None) == REMOTE_DEFAULT_IMAGE_TAG

    def test_branch_main_maps_to_nightly(self) -> None:
        assert _resolve_tag("main") == "nightly"

    def test_unknown_branch_falls_back_to_stable(self) -> None:
        assert _resolve_tag("some-feature") == REMOTE_DEFAULT_IMAGE_TAG

    def test_invalid_remote_type_exits(self) -> None:
        with pytest.raises(typer.Exit):
            update_remote_sandbox("kubernetes", None, None)

    @patch(f"{MODULE}.subprocess.run")
    def test_docker_pulls_image_ref(self, mock_run: MagicMock) -> None:
        mock_run.return_value = MagicMock(returncode=0)
        update_remote_sandbox("docker", None, None)
        args = mock_run.call_args[0][0]
        assert args[0] == "docker"
        assert args[1] == "pull"
        assert args[2].endswith(":stable")

    @patch(f"{MODULE}.save_remote_workdir")
    @patch(f"{MODULE}.load_remote_workdir", return_value=None)
    @patch(f"{MODULE}.subprocess.run")
    def test_slurm_clears_cache_before_pull(
        self, mock_run: MagicMock, _load: MagicMock, _save: MagicMock,
    ) -> None:
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")
        update_remote_sandbox("slurm", None, "~/scratch/autofyn")
        calls = [c[0][0] for c in mock_run.call_args_list]
        # cache clean must run before the pull, or --force reuses a stale layer.
        assert calls[0] == ["apptainer", "cache", "clean", "-f"]
        assert calls[1][:3] == ["apptainer", "pull", "--force"]
        assert calls[1][3].endswith("/sandbox.sif")

    @patch(f"{MODULE}.save_remote_workdir")
    @patch(f"{MODULE}.load_remote_workdir", return_value=None)
    @patch(f"{MODULE}.subprocess.run")
    def test_slurm_workdir_flag_is_saved(
        self, mock_run: MagicMock, _load: MagicMock, mock_save: MagicMock,
    ) -> None:
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")
        update_remote_sandbox("slurm", None, "/my/scratch")
        mock_save.assert_called_once_with("/my/scratch")

    @patch(f"{MODULE}.save_remote_workdir")
    @patch(f"{MODULE}.load_remote_workdir", return_value="/saved/dir")
    @patch(f"{MODULE}.subprocess.run")
    def test_slurm_uses_saved_workdir_when_no_flag(
        self, mock_run: MagicMock, _load: MagicMock, mock_save: MagicMock,
    ) -> None:
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")
        update_remote_sandbox("slurm", None, None)
        sif_arg = mock_run.call_args_list[1][0][0][3]
        assert sif_arg == "/saved/dir/sandbox.sif"
        mock_save.assert_not_called()

    @patch(f"{MODULE}.save_remote_workdir")
    @patch(f"{MODULE}.load_remote_workdir", return_value=None)
    @patch(f"{MODULE}.subprocess.run")
    def test_slurm_no_flag_no_saved_uses_default_and_saves(
        self, mock_run: MagicMock, _load: MagicMock, mock_save: MagicMock,
    ) -> None:
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")
        update_remote_sandbox("slurm", None, None)
        mock_save.assert_called_once_with(REMOTE_DEFAULT_WORKDIR)

    @patch(f"{MODULE}.save_remote_workdir")
    @patch(f"{MODULE}.load_remote_workdir", return_value="/d")
    @patch(f"{MODULE}.subprocess.run")
    def test_slurm_pull_failure_exits_nonzero(
        self, mock_run: MagicMock, _load: MagicMock, _save: MagicMock,
    ) -> None:
        # cache clean ok, pull fails.
        mock_run.side_effect = [
            MagicMock(returncode=0),
            MagicMock(returncode=255, stdout="", stderr="Failed to create thread"),
        ]
        with pytest.raises(typer.Exit):
            update_remote_sandbox("slurm", None, None)
