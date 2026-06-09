/**
 * Tests for useDashboardUI — the ephemeral UI-state hook split out of
 * useDashboard. Most of its state is trivial useState; the only logic worth
 * pinning is sidebarCollapsed (localStorage-backed) and the toggle.
 */

import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { renderHook, act } from "@testing-library/react";
import { useDashboardUI } from "@/hooks/useDashboardUI";

const KEY = "autofyn_sidebar_collapsed";

beforeEach(() => {
  localStorage.clear();
});

afterEach(() => {
  localStorage.clear();
  vi.restoreAllMocks();
});

describe("useDashboardUI", () => {
  it("defaults to sane initial UI state", () => {
    const { result } = renderHook(() => useDashboardUI());
    expect(result.current.startModalOpen).toBe(false);
    expect(result.current.onboardingOpen).toBe(false);
    expect(result.current.mobilePanel).toBe("feed");
    expect(result.current.controlsOpen).toBe(false);
    expect(result.current.rightPanel).toBe("changes");
    expect(result.current.showShortcuts).toBe(false);
    expect(result.current.sidebarCollapsed).toBe(false);
  });

  it("reads sidebarCollapsed from localStorage on mount", () => {
    localStorage.setItem(KEY, "true");
    const { result } = renderHook(() => useDashboardUI());
    expect(result.current.sidebarCollapsed).toBe(true);
  });

  it("toggles sidebarCollapsed and persists the new value", () => {
    const { result } = renderHook(() => useDashboardUI());
    expect(result.current.sidebarCollapsed).toBe(false);

    act(() => { result.current.handleToggleSidebar(); });
    expect(result.current.sidebarCollapsed).toBe(true);
    expect(localStorage.getItem(KEY)).toBe("true");

    act(() => { result.current.handleToggleSidebar(); });
    expect(result.current.sidebarCollapsed).toBe(false);
    expect(localStorage.getItem(KEY)).toBe("false");
  });

  it("does not throw if localStorage is unavailable", () => {
    vi.spyOn(Storage.prototype, "setItem").mockImplementation(() => {
      throw new Error("quota");
    });
    const { result } = renderHook(() => useDashboardUI());
    expect(() => act(() => { result.current.handleToggleSidebar(); })).not.toThrow();
    // State still flips in-memory even when persistence fails.
    expect(result.current.sidebarCollapsed).toBe(true);
  });
});
