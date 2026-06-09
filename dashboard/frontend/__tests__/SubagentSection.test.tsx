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
    { name: "architect", type: "plan", description: "designs work", source: "shipped" },
    { name: "code-reviewer", type: "review", description: "reviews code", source: "shipped" },
    { name: "ui-reviewer", type: "review", description: "reviews UI", source: "shipped" },
    { name: "ml-trainer", type: "build", description: "trains models", source: "repo" },
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

    // Initially "4 of 4 enabled".
    expect(screen.getByText("4 of 4 enabled")).toBeInTheDocument();

    await act(async () => {
      screen.getByLabelText("Disable ui-reviewer").click();
    });

    // After the failed save, the count reverts to 4 of 4 (toggle rolled back)
    // and an error is shown.
    await waitFor(() => expect(screen.getByText("network down")).toBeInTheDocument());
    expect(screen.getByText("4 of 4 enabled")).toBeInTheDocument();
  });

  it("expands and collapses a description via the more/less control", async () => {
    render(<SubagentSection activeRepo="org/repo" />);
    await waitFor(() => expect(screen.getByText("architect")).toBeInTheDocument());

    // Each agent row starts collapsed with a "more" control.
    expect(screen.getAllByText("more").length).toBe(4);

    await act(async () => {
      screen.getAllByText("more")[0].click();
    });

    // The clicked row now reads "less"; the other two still read "more".
    expect(screen.getByText("less")).toBeInTheDocument();
    expect(screen.getAllByText("more").length).toBe(3);
  });

  it("clicking more expands the description without disabling the agent", async () => {
    render(<SubagentSection activeRepo="org/repo" />);
    await waitFor(() => expect(screen.getByText("architect")).toBeInTheDocument());

    await act(async () => {
      screen.getAllByText("more")[0].click();
    });

    // The more/less control must not toggle the agent's enabled state.
    expect(saveRepoSubagents).not.toHaveBeenCalled();
    expect(screen.getByText("4 of 4 enabled")).toBeInTheDocument();
  });

  it("hides the description until expanded, then hides it again on less", async () => {
    render(<SubagentSection activeRepo="org/repo" />);
    await waitFor(() => expect(screen.getByText("architect")).toBeInTheDocument());

    // Collapsed: the description is not rendered at all.
    expect(screen.queryByText("designs work")).not.toBeInTheDocument();

    // "more" → the description appears.
    await act(async () => {
      screen.getAllByText("more")[0].click();
    });
    expect(screen.getByText("designs work")).toBeInTheDocument();

    // "less" → the description is removed again.
    await act(async () => {
      screen.getByText("less").click();
    });
    expect(screen.queryByText("designs work")).not.toBeInTheDocument();
  });

  it("badges a repo-defined agent and shows it alongside shipped ones", async () => {
    render(<SubagentSection activeRepo="org/repo" />);
    await waitFor(() => expect(screen.getByText("ml-trainer")).toBeInTheDocument());

    // The repo-defined agent renders a single "repo" badge; shipped ones don't.
    const badges = screen.getAllByText("repo");
    expect(badges.length).toBe(1);
  });
});
