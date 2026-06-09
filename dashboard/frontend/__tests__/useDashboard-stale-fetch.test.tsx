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

beforeEach(() => {
  localStorage.clear();
  resetDashboardMocks();
});

afterEach(() => {
  localStorage.clear();
  vi.restoreAllMocks();
});

describe("useDashboard init fetch: stale-result guard via initGenRef", () => {
  it("does not apply state (or warn) when unmounted before init fetches resolve", async () => {
    // Capture the resolvers so the init fetches stay pending across unmount.
    let resolveSettings!: (v: unknown) => void;
    let resolveRepos!: (v: unknown) => void;
    apiMocks.fetchSettingsStatus.mockImplementationOnce(
      () => new Promise((res) => { resolveSettings = res; }),
    );
    apiMocks.fetchRepos.mockImplementationOnce(
      () => new Promise((res) => { resolveRepos = res; }),
    );

    // Any console.error during the act() below (React's "state update on an
    // unmounted component" warning surfaces here) fails the test.
    const errorSpy = vi.spyOn(console, "error").mockImplementation(() => undefined);

    const { unmount } = renderHook(() => useDashboard());

    // Unmount before the init fetches resolve — the cleanup bumps initGenRef.
    unmount();

    // Now the stale fetches resolve. The guard must discard them: no setState,
    // no throw, no warning.
    await act(async () => {
      resolveSettings({ configured: true });
      resolveRepos([]);
      await Promise.resolve();
    });

    expect(errorSpy).not.toHaveBeenCalled();
    errorSpy.mockRestore();
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
