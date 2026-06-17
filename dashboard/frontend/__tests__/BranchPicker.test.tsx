/**
 * BranchPicker component tests.
 *
 * Covers dropdown ordering: the repo's actual default branch sorts first,
 * ahead of the statically pinned branches, so older repos whose default is
 * "master" (not "main") surface it at the top of the list.
 */

import { render } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, it, expect, vi } from "vitest";
import { BranchPicker } from "@/components/controls/BranchPicker";

function renderPicker(overrides: Partial<{
  branches: string[];
  selected: string;
  defaultBranch: string;
  onSelect: (b: string) => void;
}> = {}) {
  const defaults = {
    branches: ["zeta", "main", "master", "alpha"],
    selected: "master",
    defaultBranch: "master",
    onSelect: vi.fn(),
  };
  return render(<BranchPicker {...defaults} {...overrides} />);
}

function openDropdownOrder(): string[] {
  return Array.from(document.querySelectorAll('[role="option"]')).map(
    (el) => el.textContent?.trim() ?? "",
  );
}

describe("BranchPicker: ordering", () => {
  it("lists the repo's default branch first, ahead of statically pinned branches", async () => {
    renderPicker({ defaultBranch: "master" });
    await userEvent.click(
      document.querySelector('button[aria-haspopup="listbox"]')!,
    );
    // "master" is the repo default → first. "main" is statically pinned →
    // next. Remaining branches sort alphabetically.
    expect(openDropdownOrder()).toEqual(["master", "main", "alpha", "zeta"]);
  });

  it("falls back to static pins when the default branch is main", async () => {
    renderPicker({
      branches: ["zeta", "main", "staging", "alpha"],
      selected: "main",
      defaultBranch: "main",
    });
    await userEvent.click(
      document.querySelector('button[aria-haspopup="listbox"]')!,
    );
    expect(openDropdownOrder()).toEqual(["main", "staging", "alpha", "zeta"]);
  });
});
