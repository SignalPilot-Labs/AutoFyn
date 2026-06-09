/**
 * Behavioral tests for SubagentSection — per-repo subagent enable/disable.
 *
 * Covers: subagents render from the API; toggling an enabled agent persists
 * it into the disabled list; a save failure rolls the toggle back; and no
 * active repo shows the hint instead of fetching.
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

const SUBAGENTS = {
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
  fetchRepoSubagents.mockResolvedValue({ ...SUBAGENTS, disabled: [] });
  saveRepoSubagents.mockResolvedValue({ ok: true, disabled_count: 0 });
});

describe("SubagentSection", () => {
  it("renders the subagents grouped by phase once loaded", async () => {
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
      screen.getByLabelText("Disable ui-reviewer").click();
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
      screen.getByLabelText("Disable ui-reviewer").click();
    });

    // After the failed save, the count reverts to 3 of 3 (toggle rolled back)
    // and an error is shown.
    await waitFor(() => expect(screen.getByText("network down")).toBeInTheDocument());
    expect(screen.getByText("3 of 3 enabled")).toBeInTheDocument();
  });

  it("expands and collapses a description via the more/less control", async () => {
    render(<SubagentSection activeRepo="org/repo" />);
    await waitFor(() => expect(screen.getByText("architect")).toBeInTheDocument());

    // Each agent row starts collapsed with a "more" control.
    expect(screen.getAllByText("more").length).toBe(3);

    await act(async () => {
      screen.getAllByText("more")[0].click();
    });

    // The clicked row now reads "less"; the other two still read "more".
    expect(screen.getByText("less")).toBeInTheDocument();
    expect(screen.getAllByText("more").length).toBe(2);
  });

  it("clicking more expands the description without disabling the agent", async () => {
    render(<SubagentSection activeRepo="org/repo" />);
    await waitFor(() => expect(screen.getByText("architect")).toBeInTheDocument());

    await act(async () => {
      screen.getAllByText("more")[0].click();
    });

    // The more/less control must not toggle the agent's enabled state.
    expect(saveRepoSubagents).not.toHaveBeenCalled();
    expect(screen.getByText("3 of 3 enabled")).toBeInTheDocument();
  });

  it("clamps the description until expanded, then shows it in full", async () => {
    render(<SubagentSection activeRepo="org/repo" />);
    await waitFor(() => expect(screen.getByText("architect")).toBeInTheDocument());

    // Collapsed: the description is line-clamped.
    const desc = screen.getByText("designs work");
    expect(desc.className).toContain("line-clamp-2");

    await act(async () => {
      screen.getAllByText("more")[0].click();
    });

    // Expanded: the clamp is removed so the whole description shows.
    expect(screen.getByText("designs work").className).not.toContain("line-clamp-2");
  });
});
