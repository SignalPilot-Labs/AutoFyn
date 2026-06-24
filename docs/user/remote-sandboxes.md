# Remote Sandboxes

Run sandboxes on HPC clusters, GPU servers, or any SSH-reachable machine instead of local Docker. The agent talks to them over the same HTTP API via the **connector** (a local process `autofyn start` launches).

## Setup

### 1. Install the sandbox image on the remote

```bash
git clone https://github.com/SignalPilot-Labs/AutoFyn.git ~/.autofyn
pip install ~/.autofyn/cli
autofyn update --remote slurm    # HPC; SIF → ~/scratch/autofyn/sandbox.sif
autofyn update --remote docker   # remote Docker host
```

Re-run to update. `--workdir <dir>` sets the SIF location (remembered); use scratch/SSD, not home. `--branch main` pulls nightly.

### 2. SSH access

Passwordless key-based SSH. Test: `ssh user@host "echo ok"`. An SSH config alias works.

### 3. Add the sandbox in the dashboard

**Settings → Remote Sandboxes → Add Sandbox.** Slurm sandboxes get structured fields (partition, CPUs, memory, GPU, work dir) that auto-generate the start command; you can also edit it directly. Set **Type**, **SSH Target**, **Work Directory** (from step 1), and timeouts (default 1800s).

### 4. Start a run

In the **New Run** modal → **Sandbox** section, pick your remote sandbox. Remembered per repo.

## Troubleshooting

- **Start failed / no `AF_READY`:** run the start command manually on the remote; check `autofyn logs`, `squeue -u $USER`, module name, SIF path, port. Bump **Startup Timeout** for slow queues.
- **No space left:** scratch overlay full — check quota. Don't use `--writable-tmpfs` (64MB only).
- **Docker permission denied:** SSH user needs Docker socket access (`usermod -aG docker $USER` or `sudo`).
- **Connection drops:** connector auto-reconnects; else status → `connector_lost`, see `~/.autofyn/.connector.log`.
- **`mksquashfs: Failed to create thread`:** login-node thread limit — run on a compute node: `srun --pty --mem=8G --time=00:30:00 autofyn update --remote slurm`.
