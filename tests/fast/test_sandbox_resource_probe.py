"""Regression tests for the sandbox resource probe.

The probe must report the box the sandbox actually runs in, not the host
node — the OOM that motivated this feature happened because the agent
sized parallel work off node RAM instead of its 128G cgroup cap. These
pin: kind detection from Slurm/Apptainer env, and the memory-limit read
(real cap vs the "max" sentinel vs an absent cgroup file).
"""

import os
from pathlib import Path

import pytest

from config.constants import SANDBOX_KIND_DOCKER, SANDBOX_KIND_SLURM
from constants import APPTAINER_MARKER_ENV_VAR, SLURM_JOB_ID_ENV_VAR
from shared.resources import _probe_kind, _probe_mem_limit_bytes, probe_resources


class TestSandboxResourceProbe:
    """probe_resources reports the sandbox's own allocation."""

    def teardown_method(self) -> None:
        """Drop any marker env vars a test may have set."""
        os.environ.pop(SLURM_JOB_ID_ENV_VAR, None)
        os.environ.pop(APPTAINER_MARKER_ENV_VAR, None)

    def test_kind_is_docker_without_markers(self) -> None:
        os.environ.pop(SLURM_JOB_ID_ENV_VAR, None)
        os.environ.pop(APPTAINER_MARKER_ENV_VAR, None)
        assert _probe_kind() == SANDBOX_KIND_DOCKER

    def test_kind_is_slurm_with_slurm_job_id(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv(SLURM_JOB_ID_ENV_VAR, "16455047")
        assert _probe_kind() == SANDBOX_KIND_SLURM

    def test_kind_is_slurm_with_apptainer_marker(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv(APPTAINER_MARKER_ENV_VAR, "/some/image.sif")
        assert _probe_kind() == SANDBOX_KIND_SLURM

    def test_mem_limit_reads_real_cap(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        cap = tmp_path / "memory.max"
        cap.write_text("137438953472\n", encoding="utf-8")
        monkeypatch.setattr("shared.resources.CGROUP_MEMORY_MAX_PATH", str(cap))
        assert _probe_mem_limit_bytes() == 137438953472

    def test_mem_limit_is_none_when_uncapped(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        cap = tmp_path / "memory.max"
        cap.write_text("max\n", encoding="utf-8")
        monkeypatch.setattr("shared.resources.CGROUP_MEMORY_MAX_PATH", str(cap))
        assert _probe_mem_limit_bytes() is None

    def test_mem_limit_is_none_when_file_absent(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        missing = tmp_path / "does_not_exist"
        monkeypatch.setattr("shared.resources.CGROUP_MEMORY_MAX_PATH", str(missing))
        assert _probe_mem_limit_bytes() is None

    @pytest.mark.skipif(
        not hasattr(os, "sched_getaffinity"),
        reason="sched_getaffinity is Linux-only; the sandbox always runs on Linux",
    )
    def test_probe_resources_returns_positive_cpu_count(self) -> None:
        res = probe_resources()
        assert res.cpu_count >= 1
