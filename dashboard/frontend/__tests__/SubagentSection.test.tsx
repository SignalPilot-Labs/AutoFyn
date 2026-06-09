/**
 * Behavioral tests for SubagentSection — per-repo subagent enable/disable.
 *
 * Covers: roster renders from the API; toggling an enabled agent persists it
 * into the disabled list; a save failure rolls the toggle back; and no active
 * repo shows the hint instead of fetching.
 */

import { render, screen, waitFor, act } from "@testing-library/react";
import { describe, it, expect, vi, beforeEach } from "vitest";

const fetchRepoSubagents = vi.fn();
const saveRepoSubagents = vi.fn();

vi.mock("@/lib/settings-api", () => ({
  fetchRepoSubagents: (...args: unknown[]) => fetchRepoSubagents(...args),
  saveRepoSubagents: (...args: unknown[]) => saveRepoSubagents(...args),
}));

import { SubagentSection } from "@/components/settings/SubagentSection";

const ROSTER = {
  repo: "org/repo",
  agents: [
    { name: "architect", type: "plan", description: "designs work" },
    { name: "code-reviewer", type: "review", description: "reviews code" },
    { name: "ui-reviewer", type: "review", description: "reviews UI" },
  ],
  disabled: [] as string[],
};

beforeEach(() => {
  fetchRepoSubagents.mockReset();
  saveRepoSubagents.mockReset();
  fetchRepoSubagents.mockResolvedValue({ ...ROSTER, disabled: [] });
  saveRepoSubagents.mockResolvedValue({ ok: true, disabled_count: 0 });
});

describe("SubagentSection", () => {
  it("renders the roster grouped by phase once loaded", async () => {
    render(<SubagentSection activeRepo="org/repo" />);
    await waitFor(() => expect(screen.getByText("architect")).toBeInTheDocument());
    expect(screen.getByText("code-reviewer")).toBeInTheDocument();
    expect(screen.getByText("ui-reviewer")).toBeInTheDocument();
    // Phase headings present.
    expect(screen.getByText("Plan")).toBeInTheDocument();
    expect(screen.getByText("Review")).toBeInTheDocument();
  });

  it("does not fetch and shows a hint when no repo is active", () => {
    render(<SubagentSection activeRepo="" />);
    expect(fetchRepoSubagents).not.toHaveBeenCalled();
    expect(
      screen.getByText(/Set an active repository to configure/i),
    ).toBeInTheDocument();
  });

  it("toggling an enabled agent persists it into the disabled list", async () => {
    render(<SubagentSection activeRepo="org/repo" />);
    await waitFor(() => expect(screen.getByText("ui-reviewer")).toBeInTheDocument());

    await act(async () => {
      screen.getByText("ui-reviewer").click();
    });

    expect(saveRepoSubagents).toHaveBeenCalledWith("org/repo", ["ui-reviewer"]);
  });

  it("rolls back the toggle when the save fails", async () => {
    saveRepoSubagents.mockRejectedValueOnce(new Error("network down"));
    render(<SubagentSection activeRepo="org/repo" />);
    await waitFor(() => expect(screen.getByText("ui-reviewer")).toBeInTheDocument());

    // Initially "3 of 3 enabled".
    expect(screen.getByText("3 of 3 enabled")).toBeInTheDocument();

    await act(async () => {
      screen.getByText("ui-reviewer").click();
    });

    // After the failed save, the count reverts to 3 of 3 (toggle rolled back)
    // and an error is shown.
    await waitFor(() => expect(screen.getByText("network down")).toBeInTheDocument());
    expect(screen.getByText("3 of 3 enabled")).toBeInTheDocument();
  });
});
