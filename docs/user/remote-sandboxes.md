# Remote Sandboxes

By default, AutoFyn runs each sandbox in a local Docker container. Remote sandboxes let you run on HPC clusters, GPU servers, or any machine you can SSH into.

## How it works

1. AutoFyn SSH-tunnels to the remote machine via the **connector** (a local process started automatically by `autofyn start`)
2. Your **start command** runs on the remote — it launches the sandbox container/process
3. The sandbox binds a free port and prints `AF_BOUND port=<port>`
4. Once healthy, it prints `AF_READY host=<compute-node> port=<port>`
5. The connector establishes a reverse tunnel and proxies all traffic

The agent talks to the remote sandbox exactly like a local one — same HTTP API, same security.

## Setup

### 1. Install the sandbox image on the remote

Install the AutoFyn CLI **on the remote machine** and let it pull the sandbox image for you. This is the recommended path — it handles the apptainer cache correctly (see the warning below) so you don't get a silently stale image.

```bash
# On the remote machine — install the CLI (same as the local quick start):
git clone https://github.com/SignalPilot-Labs/AutoFyn.git ~/.autofyn
pip install ~/.autofyn/cli

# HPC (Slurm / Apptainer):
autofyn update --remote slurm --workdir <dir>  # choose where the SIF lives

# Remote Docker host:
autofyn update --remote docker                 # pulls into the local docker store
```

`--remote slurm` writes the SIF to `<workdir>/sandbox.sif` (default `~/scratch/autofyn`, remembered after the first run so you can omit `--workdir` next time). Each run creates a temporary overlay under `<workdir>/autofyn/runs/` and cleans it up when done; leftover `runs/` directories after a hard kill (SIGKILL, node crash) can be safely deleted.

Pick a work dir on fast, high-capacity storage your cluster provides (scratch, local SSD). Avoid home directories — they're usually small, backed up, and may not mount on compute nodes.

By default `--remote` installs the **stable** image. The author/testers can pull the nightly image with `--branch main`:

```bash
autofyn update --remote slurm --branch main    # nightly sandbox image
```

#### Updating the sandbox image

The remote sandbox image does **not** auto-update — it's decoupled from the agent. When you update AutoFyn, re-run the same `autofyn update --remote ...` command so the agent and sandbox stay in sync. A sandbox image older than the agent causes runs to fail at bootstrap.

> **Why use the CLI:** `apptainer pull --force` overwrites the `.sif` file but **rebuilds it from apptainer's local layer cache**, so a manual pull can silently produce a *stale* image even with `--force`. `autofyn update --remote slurm` runs `apptainer cache clean -f` first, every time, so you always get a genuinely fresh image.

If the pull fails on a login node with `mksquashfs: FATAL ERROR: Failed to create thread`, run it inside an interactive job instead — the CLI prints this hint, and see Troubleshooting below.

### 2. Ensure SSH access

You need passwordless SSH to the remote (key-based auth). Test it:

```bash
ssh user@remote-host "echo ok"
```

You can use an SSH config alias (e.g. `Host mycluster` in `~/.ssh/config`).

### 3. Add the sandbox in the dashboard

Go to **Settings → Remote Sandboxes → Add Sandbox**.

For **Slurm** sandboxes, the form provides structured fields (partition, CPUs, memory, GPU, work directory) that auto-generate the start command. You can also edit the command directly for custom flags.

| Field | Description |
|-------|-------------|
| **Name** | Display name (e.g. "GPU Server", "HPC Cluster") |
| **Type** | `Docker` or `Slurm` |
| **SSH Target** | `user@host` or SSH config alias |
| **AutoFyn Work Directory** | The directory from step 1 (e.g. `~/scratch/autofyn`) |
| **Partition** | Slurm partition name (e.g. `gpu`, `normal`) |
| **CPUs** | CPU cores per task |
| **Memory** | Memory per node (e.g. `16G`, `32G`) |
| **GPU** | GPU GRES (e.g. `a100:1`, `h100:2`). Leave empty for no GPU |
| **Start Command** | Auto-generated from fields above, or edit directly |
| **Startup Timeout** | Max seconds to wait for `AF_READY` (default: 1800 for Slurm queues) |
| **Inactivity Timeout** | Sandbox self-terminates after this many seconds idle (default: 1800) |

### 4. Start a run using the remote sandbox

In the **New Run** modal, expand the **Sandbox** section and select your remote sandbox instead of "Docker (local)". AutoFyn remembers your last choice per repo.

## Start command examples

### Docker remote

```bash
source /etc/profile && docker run --rm --network=host -e AF_SANDBOX_PORT=0 ghcr.io/signalpilot-labs/autofyn-sandbox:stable
```

### Slurm / Apptainer

```bash
source /etc/profile && module load apptainer && srun --job-name=autofyn -p my_partition -n 1 --cpus-per-task=4 --mem=16G bash -c 'W=~/scratch/autofyn/runs/$AF_RUN_KEY && mkdir -p $W && apptainer exec --overlay $W --pwd /opt/autofyn -B $HOME $AF_HOST_MOUNTS ~/scratch/autofyn/sandbox.sif python3 -m server; rm -rf $W'
```

With GPU access:

```bash
source /etc/profile && module load apptainer && srun --job-name=autofyn -p gpu -n 1 --cpus-per-task=4 --mem=16G --gres=gpu:1 bash -c 'W=~/scratch/autofyn/runs/$AF_RUN_KEY && mkdir -p $W && apptainer exec --nv --overlay $W --pwd /opt/autofyn -B $HOME $AF_HOST_MOUNTS ~/scratch/autofyn/sandbox.sif python3 -m server; rm -rf $W'
```

> **Note:** The sandbox generates its own authentication secret at startup and transmits it back to the connector over the encrypted SSH stdout pipe. All secrets (tokens, env vars from the New Run modal) are passed securely over the SSH tunnel after startup — they never appear in the start command, SSH command-line arguments, or Slurm job metadata.

Key flags:

- `source /etc/profile` — non-interactive SSH doesn't source profile, so `docker`, `module`, and other commands in `/usr/local/bin` or module paths may not be found. Always include this for both Docker and Slurm commands
- `-n 1` — only one task. `-n > 1` would spawn > 1 processes trying to bind the same port and **fail**.
- `--cpus-per-task=4` — request 4 CPU cores (adjust to your needs)
- `--mem=16G` — memory limit per node
- `--gres=gpu:1` — request 1 GPU (Slurm generic resource)
- `--nv` — Apptainer flag to expose NVIDIA GPUs inside the container
- `--overlay $W` — uses a scratch directory as the writable layer on top of the read-only SIF image. Each run gets its own overlay via `$AF_RUN_KEY` (set automatically by the connector). Cleaned up after the run ends.
- `-B $HOME` — binds your home directory for git config, SSH keys, etc.

## Timeline events

When a remote sandbox starts, you'll see these milestones in the dashboard feed:

1. **Run Starting** — run created
2. **Sandbox Queued** — job submitted (shows Slurm job ID)
3. **Sandbox Allocated** — resources allocated (Slurm only)
4. **Sandbox Started** — sandbox is healthy and ready

Startup log lines (srun output, server boot, etc.) are stored in the audit log but not shown in the feed.

## Troubleshooting

**Sandbox start failed / timeout:**
- Check `autofyn logs` for connector errors
- SSH into the remote and run the start command manually to see output
- For Slurm: check `squeue -u $USER` to see if the job is stuck in queue
- Increase the **Startup Timeout** in sandbox settings (Slurm queues can take minutes)

**"Start command exited without AF_READY":**
- The process exited before printing `AF_READY`. Run the command manually on the remote to see errors
- Common causes: wrong module name, missing SIF file, port already in use

**"No space left on device":**
- The scratch overlay directory ran out of space. Check your scratch quota.
- Do NOT use `--writable-tmpfs` — it gives only 64MB of writable space. Use `--overlay` with a scratch directory instead.

**Docker: permission denied / cannot connect to daemon:**
- Your SSH user must have access to the Docker socket. Either add the user to the `docker` group (`sudo usermod -aG docker $USER`, then re-login) or run with `sudo` in the start command
- Verify with: `ssh user@remote "source /etc/profile && docker info"`
- If the socket exists but isn't writable, check permissions: `ls -la /var/run/docker.sock`

**Connection drops during run:**
- The connector auto-reconnects. If it can't, the run status changes to `connector_lost`
- Check `~/.autofyn/.connector.log` for details

**`mksquashfs: FATAL ERROR: Failed to create thread` during `apptainer pull`:**
- The login node has a low thread/process limit (`ulimit -u`). `mksquashfs` cannot create worker threads even with `MKSQUASHFS_PROCS=1`.
- Run the update inside an interactive job instead: `srun --pty --mem=8G --time=00:30:00 autofyn update --remote slurm`
- Compute nodes have higher thread limits than login nodes