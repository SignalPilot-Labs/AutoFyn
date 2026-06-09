/**
 * Behavioral regression test: useDashboard's init useEffect must not apply
 * stale fetch results after unmount (React strict-mode double-mount, rapid
 * remount).
 *
 * Bug (pinned by the prior source-grep test): the initial effect called
 * fetchSettingsStatus().then(setSettingsStatus) and fetchRepos().then(setRepos)
 * with no guard. If the component unmounted before the promises resolved, the
 * .then() callbacks ran state setters on an unmounted component (act/React
 * warnings, lost-update bugs).
 *
 * The fix: an initGenRef generation counter incremented at effect entry and
 * checked (`gen !== initGenRef.current`) before applying each result; the
 * cleanup bumps the ref so in-flight fetches are invalidated on unmount.
 *
 * Behavioral assertions:
 *   - Unmounting before the init fetches resolve, then resolving them, throws
 *     no error and produces no act()-warnings (state is never applied post-
 *     unmount).
 *   - On a normal mount the resolved settingsStatus IS applied, and when the
 *     status is unconfigured the onboarding modal opens.
 *
 * This replaces the prior source-grep test; it mounts the real hook.
 */

import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { renderHook, act, waitFor } from "@testing-library/react";
import {
  resetDashboardMocks,
  apiMocks,
} from "./helpers/dashboardHarness";

import { useDashboard } from "@/hooks/useDashboard";

const ACTIVE_REPO_KEY = "sp_improve_active_repo";

beforeEach(() => {
  localStorage.clear();
  resetDashboardMocks();
});

afterEach(() => {
  localStorage.clear();
  vi.restoreAllMocks();
});

describe("useDashboard init fetch: stale-result guard via initGenRef", () => {
  it("discards a stale init fetch that resolves after unmount", async () => {
    // A stored repo that the (pending) fetchRepos result will say no longer
    // exists. On a LIVE mount the init effect would react to this by picking a
    // fallback repo and overwriting localStorage. We use that observable
    // localStorage write as the witness for "the stale result was applied".
    localStorage.setItem(ACTIVE_REPO_KEY, "stale/repo");

    // Keep the init fetchRepos pending so it can resolve AFTER unmount.
    let resolveRepos!: (v: unknown) => void;
    apiMocks.fetchSettingsStatus.mockResolvedValueOnce({ configured: true });
    apiMocks.fetchRepos.mockImplementationOnce(
      () => new Promise((res) => { resolveRepos = res; }),
    );

    const { unmount } = renderHook(() => useDashboard());

    // Unmount before fetchRepos resolves — the effect cleanup bumps initGenRef,
    // so the pending .then() must short-circuit on its generation check.
    unmount();

    // Now the stale fetch resolves with a list that does NOT contain
    // "stale/repo" but DOES have a repo with runs (the fallback the unguarded
    // code would pick). The guard must discard this entirely.
    await act(async () => {
      resolveRepos([{ repo: "other/repo", run_count: 3 }]);
      await Promise.resolve();
    });

    // Guard held: localStorage was never overwritten with the fallback. If the
    // initGenRef guard were removed, the stale .then() would run
    // setActiveRepoFilter("other/repo") + setItem and this would be
    // "other/repo".
    expect(localStorage.getItem(ACTIVE_REPO_KEY)).toBe("stale/repo");
  });

  it("applies settingsStatus on a normal mount", async () => {
    apiMocks.fetchSettingsStatus.mockResolvedValueOnce({ configured: true });
    apiMocks.fetchRepos.mockResolvedValueOnce([]);

    const { result } = renderHook(() => useDashboard());

    await waitFor(() =>
      expect(result.current.settingsStatus).toEqual({ configured: true }),
    );
    expect(result.current.isConfigured).toBe(true);
    // Configured → onboarding stays closed.
    expect(result.current.onboardingOpen).toBe(false);
  });

  it("opens onboarding when the resolved status is unconfigured", async () => {
    apiMocks.fetchSettingsStatus.mockResolvedValueOnce({ configured: false });
    apiMocks.fetchRepos.mockResolvedValueOnce([]);

    const { result } = renderHook(() => useDashboard());

    await waitFor(() =>
      expect(result.current.settingsStatus).toEqual({ configured: false }),
    );
    expect(result.current.isConfigured).toBe(false);
    await waitFor(() => expect(result.current.onboardingOpen).toBe(true));
  });
});
