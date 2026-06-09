/**
 * Shared test harness for behaviorally mounting useDashboard.
 *
 * useDashboard wires together useRuns, useSSE, useEventState, loadRunHistory,
 * and several API calls. To test its behavior (rather than grep its source) we
 * mock the leaf dependencies and expose handles to drive them:
 *
 *  - sseControl: spies for connect/disconnect/clearEvents + fire the
 *    onRunEnded / onSessionResumed callbacks useDashboard passes to useSSE.
 *  - runsControl: set the runs list (runsControl.current.runs) and capture
 *    refresh() calls.
 *  - apiMocks: the mocked fetch* functions, so a test can stub responses,
 *    make loadRunHistory hang/reject, etc.
 *
 * Importing this module registers the vi.mock factories (hoisted to module
 * top); tests then drive the exported control objects.
 */

import { vi } from "vitest";
import type { FeedEvent } from "@/lib/types";

export interface SseControl {
  connect: ReturnType<typeof vi.fn>;
  disconnect: ReturnType<typeof vi.fn>;
  clearEvents: ReturnType<typeof vi.fn>;
  /** Invoke the onRunEnded callback useDashboard handed to useSSE. */
  fireRunEnded: () => void;
  /** Invoke the onSessionResumed callback useDashboard handed to useSSE. */
  fireSessionResumed: () => void;
}

export interface RunsControl {
  refresh: ReturnType<typeof vi.fn>;
  current: { runs: unknown[]; loading: boolean };
}

// Captured callbacks/state live in module scope so the vi.mock factories
// (hoisted) and the tests share them.
const sseCallbacks: { onRunEnded?: () => void; onSessionResumed?: () => void } = {};
export const sseControl: SseControl = {
  connect: vi.fn(),
  disconnect: vi.fn(),
  clearEvents: vi.fn(),
  fireRunEnded: () => sseCallbacks.onRunEnded?.(),
  fireSessionResumed: () => sseCallbacks.onSessionResumed?.(),
};

export const runsControl: RunsControl = {
  refresh: vi.fn(),
  current: { runs: [], loading: false },
};

export const apiMocks = {
  fetchAgentHealth: vi.fn(),
  fetchRepos: vi.fn(),
  setActiveRepo: vi.fn(),
  fetchSettingsStatus: vi.fn(),
  loadRunHistory: vi.fn(),
};

// vi.mock calls are hoisted; they must live at the top level of a module that
// is imported before the hook under test. Importing this harness registers
// them. The factories reference the module-scope control objects above (only
// referenced lazily at call time, so the TDZ-on-hoist rule is satisfied).
vi.mock("@/hooks/useSSE", () => ({
  useSSE: (onRunEnded?: () => void, onSessionResumed?: () => void) => {
    sseCallbacks.onRunEnded = onRunEnded;
    sseCallbacks.onSessionResumed = onSessionResumed;
    return {
      events: [] as FeedEvent[],
      connected: true,
      connectionState: "connected" as const,
      clearEvents: sseControl.clearEvents,
      connect: sseControl.connect,
      disconnect: sseControl.disconnect,
    };
  },
}));

vi.mock("@/hooks/useRuns", () => ({
  useRuns: () => ({
    runs: runsControl.current.runs,
    loading: runsControl.current.loading,
    refresh: runsControl.refresh,
  }),
}));

vi.mock("@/hooks/useMobile", () => ({ useMobile: () => false }));

vi.mock("@/lib/loadRunHistory", () => ({
  loadRunHistory: apiMocks.loadRunHistory,
}));

vi.mock("@/lib/api", () => ({
  fetchAgentHealth: apiMocks.fetchAgentHealth,
  fetchRepos: apiMocks.fetchRepos,
  setActiveRepo: apiMocks.setActiveRepo,
}));

vi.mock("@/lib/settings-api", () => ({
  fetchSettingsStatus: apiMocks.fetchSettingsStatus,
}));

/** Reset all spies + default responses. Call in beforeEach. */
export function resetDashboardMocks(): void {
  sseControl.connect.mockReset();
  sseControl.disconnect.mockReset();
  sseControl.clearEvents.mockReset();
  runsControl.refresh.mockReset();
  runsControl.current = { runs: [], loading: false };
  apiMocks.fetchAgentHealth.mockReset().mockResolvedValue({ runs: [] });
  apiMocks.fetchRepos.mockReset().mockResolvedValue([]);
  apiMocks.setActiveRepo.mockReset().mockResolvedValue(undefined);
  apiMocks.fetchSettingsStatus.mockReset().mockResolvedValue({ configured: true });
  apiMocks.loadRunHistory
    .mockReset()
    .mockResolvedValue({ events: [], lastToolId: 0, lastAuditId: 0, truncated: false });
}

export function makeRun(over: Record<string, unknown>): Record<string, unknown> {
  return {
    id: "run-1",
    run_id: "run-1",
    status: "running",
    github_repo: "owner/repo",
    ...over,
  };
}
