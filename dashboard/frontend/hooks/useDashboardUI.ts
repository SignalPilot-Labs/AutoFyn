"use client";

import { useState, useCallback } from "react";

/**
 * Ephemeral UI state for the dashboard shell — modals, panels, and layout
 * toggles that have no coupling to server state, the run lifecycle, or the
 * SSE/event machinery. Split out of useDashboard so the parent hook is left
 * with only server-state coordination.
 *
 * sidebarCollapsed and its toggle persist to localStorage; everything else is
 * in-memory session state.
 */

const SIDEBAR_COLLAPSED_KEY = "autofyn_sidebar_collapsed";

export type MobilePanel = "feed" | "runs" | "changes" | "logs";
export type RightPanel = "changes" | "logs";

export interface DashboardUIState {
  startModalOpen: boolean;
  setStartModalOpen: (v: boolean) => void;
  onboardingOpen: boolean;
  setOnboardingOpen: (v: boolean) => void;
  mobilePanel: MobilePanel;
  setMobilePanel: (v: MobilePanel) => void;
  controlsOpen: boolean;
  setControlsOpen: (v: boolean) => void;
  rightPanel: RightPanel;
  setRightPanel: (v: RightPanel) => void;
  sidebarCollapsed: boolean;
  handleToggleSidebar: () => void;
  showShortcuts: boolean;
  setShowShortcuts: (v: boolean) => void;
}

export function useDashboardUI(): DashboardUIState {
  const [startModalOpen, setStartModalOpen] = useState(false);
  const [onboardingOpen, setOnboardingOpen] = useState(false);
  const [mobilePanel, setMobilePanel] = useState<MobilePanel>("feed");
  const [controlsOpen, setControlsOpen] = useState(false);
  const [rightPanel, setRightPanel] = useState<RightPanel>("changes");
  const [sidebarCollapsed, setSidebarCollapsed] = useState<boolean>(() => {
    try { return localStorage.getItem(SIDEBAR_COLLAPSED_KEY) === "true"; } catch { return false; }
  });
  const [showShortcuts, setShowShortcuts] = useState(false);

  const handleToggleSidebar = useCallback(() => {
    setSidebarCollapsed((prev) => {
      const next = !prev;
      try { localStorage.setItem(SIDEBAR_COLLAPSED_KEY, String(next)); } catch {}
      return next;
    });
  }, []);

  return {
    startModalOpen,
    setStartModalOpen,
    onboardingOpen,
    setOnboardingOpen,
    mobilePanel,
    setMobilePanel,
    controlsOpen,
    setControlsOpen,
    rightPanel,
    setRightPanel,
    sidebarCollapsed,
    handleToggleSidebar,
    showShortcuts,
    setShowShortcuts,
  };
}
