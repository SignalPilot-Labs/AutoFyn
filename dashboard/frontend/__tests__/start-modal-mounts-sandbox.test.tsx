/**
 * Regression tests for StartRunModal mounts loaded for wrong sandbox (BUG 4).
 *
 * Root cause: the general data-loading effect called loadMountsForSandbox with
 * a selectedSandboxId left over from the previous render, then never re-fired
 * when the restoration effect set the saved sandbox — so the modal showed one
 * sandbox's mounts while another was selected.
 *
 * Mounts come from two APIs: fetchRepoMounts (local Docker) and
 * fetchRemoteMounts (a remote sandbox). Which one runs on open, with which
 * sandbox id, is the whole bug — so these assert on those calls rather than on
 * the source text of the effects that make them.
 */

import { render, waitFor } from "@testing-library/react";
import { describe, it, expect, vi, beforeEach } from "vitest";
import { StartRunModal } from "@/components/controls/StartRunModal";
import type { StartRunModalProps } from "@/components/controls/StartRunModal";
import * as api from "@/lib/api";

const REPO = "owner/repo";
const SANDBOX_ID = "sandbox-abc";
const LOCAL_MOUNT: api.HostMount[] = [
  { host_path: "/local", container_path: "/local", mode: "rw" },
];
const REMOTE_MOUNT: api.HostMount[] = [
  { host_path: "/remote", container_path: "/remote", mode: "rw" },
];
const REMOTE_SANDBOX: api.RemoteSandboxConfig = {
  id: SANDBOX_ID,
  name: "hpc",
  ssh_target: "user@host",
  type: "docker",
  default_start_cmd: "start-remote",
  queue_timeout: 60,
  heartbeat_timeout: 60,
  work_dir: "/work",
};

vi.mock("@/lib/models", async (importOriginal) => {
  const actual = await importOriginal<typeof import("@/lib/models")>();
  return {
    ...actual,
    useModels: () => ({
      models: [
        { id: "claude-opus-4-8", label: "Claude Opus 4.8", short: "Opus 4.8", description: "Most capable", context: "1M context", tier: "opus" },
      ],
      defaultModel: "claude-opus-4-8",
      defaultEffort: "medium",
      providersByModel: { "claude-opus-4-8": ["anthropic"] },
      loading: false,
      refetch: () => {},
    }),
  };
});

vi.mock("@/lib/api", async (importOriginal) => {
  const actual = await importOriginal<typeof import("@/lib/api")>();
  return {
    ...actual,
    fetchRepoEnv: vi.fn(async () => ({})),
    fetchRepoMcpServers: vi.fn(async () => ({})),
    fetchRepoMounts: vi.fn(async () => LOCAL_MOUNT),
    fetchRemoteMounts: vi.fn(async () => REMOTE_MOUNT),
    fetchRemoteSandboxes: vi.fn(async () => []),
  };
});

/** Open the modal the way a user does: render closed, then flip open.
 *
 * The reset-on-open effect keys on a false -> true transition, so mounting
 * straight to open={true} never runs it and no mounts load.
 */
function openModal(overrides: Partial<StartRunModalProps> = {}): void {
  const props: Omit<StartRunModalProps, "open"> = {
    onClose: vi.fn(),
    onStart: vi.fn(),
    busy: false,
    branches: ["main"],
    defaultBranch: "main",
    activeRepo: REPO,
    ...overrides,
  };
  const { rerender } = render(<StartRunModal open={false} {...props} />);
  rerender(<StartRunModal open={true} {...props} />);
}

describe("StartRunModal: mounts loaded for correct sandbox on open (BUG 4)", () => {
  beforeEach(() => {
    localStorage.clear();
    // clearAllMocks wipes implementations, so re-arm them after it, not before.
    vi.clearAllMocks();
    vi.mocked(api.fetchRepoEnv).mockResolvedValue({});
    vi.mocked(api.fetchRepoMcpServers).mockResolvedValue({});
    vi.mocked(api.fetchRepoMounts).mockResolvedValue(LOCAL_MOUNT);
    vi.mocked(api.fetchRemoteMounts).mockResolvedValue(REMOTE_MOUNT);
    vi.mocked(api.fetchRemoteSandboxes).mockResolvedValue([]);
  });

  it("loads local mounts on open when no sandbox is saved", async () => {
    openModal();

    await waitFor(() => expect(api.fetchRepoMounts).toHaveBeenCalledWith(REPO));
    expect(api.fetchRemoteMounts).not.toHaveBeenCalled();
  });

  it("does not load mounts when there is no active repo", async () => {
    openModal({ activeRepo: null });

    await waitFor(() => expect(api.fetchRemoteSandboxes).toHaveBeenCalled());
    expect(api.fetchRepoMounts).not.toHaveBeenCalled();
    expect(api.fetchRemoteMounts).not.toHaveBeenCalled();
  });

  it("loads mounts for the restored sandbox, not the local default", async () => {
    localStorage.setItem(`autofyn_last_sandbox:${REPO}`, SANDBOX_ID);
    vi.mocked(api.fetchRemoteSandboxes).mockResolvedValue([REMOTE_SANDBOX]);

    openModal();

    // The restoration effect must fetch the saved sandbox's mounts. Before the
    // fix it kept the local mounts, so the id argument is the regression.
    await waitFor(() =>
      expect(api.fetchRemoteMounts).toHaveBeenCalledWith(REPO, SANDBOX_ID),
    );
  });

  it("ignores a saved sandbox that no longer exists", async () => {
    localStorage.setItem(`autofyn_last_sandbox:${REPO}`, "deleted-sandbox");
    vi.mocked(api.fetchRemoteSandboxes).mockResolvedValue([REMOTE_SANDBOX]);

    openModal();

    // The restoration effect only runs once remoteSandboxes has loaded, so
    // wait on the cleanup itself rather than on the local-mount fetch.
    await waitFor(() =>
      expect(localStorage.getItem(`autofyn_last_sandbox:${REPO}`)).toBeNull(),
    );
    expect(api.fetchRemoteMounts).not.toHaveBeenCalled();
  });

  it("does not load mounts while the modal is closed", async () => {
    render(
      <StartRunModal
        open={false}
        onClose={vi.fn()}
        onStart={vi.fn()}
        busy={false}
        branches={["main"]}
        defaultBranch="main"
        activeRepo={REPO}
      />,
    );

    await waitFor(() => expect(api.fetchRepoMounts).not.toHaveBeenCalled());
    expect(api.fetchRemoteMounts).not.toHaveBeenCalled();
  });
});
