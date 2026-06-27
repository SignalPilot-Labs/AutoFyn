/**
 * Regression tests for WorkTree oversize handling.
 *
 * The diff contract is list+expand: the polled response carries only the
 * file list (no bodies), and a single file's body is fetched on click. So
 * "too large" is now a PER-FILE concern on expand — an oversize body must
 * render a "Diff too large" message instead of a perpetual loading spinner.
 *
 * (The old per-source blob oversize model — repoTooLarge/tmpTooLarge on two
 * giant blobs — no longer exists: bodies are never bulk-fetched.)
 */

import { describe, it, expect } from "vitest";
import * as fs from "fs";
import * as path from "path";

const SRC = fs.readFileSync(
  path.resolve(__dirname, "../components/worktree/WorkTree.tsx"),
  "utf-8",
);

describe("WorkTree: per-file expand oversize handling", () => {
  it("declares expandTooLarge state for the selected file's body", () => {
    expect(SRC).toContain("expandTooLarge");
    expect(SRC).toContain("setExpandTooLarge");
  });

  it("the expand effect flags a body that exceeds DIFF_MAX_BYTES", () => {
    const start = SRC.indexOf("// Fetch the selected file's body");
    expect(start).toBeGreaterThan(-1);
    const body = SRC.slice(start, start + 1400);
    expect(body).toContain("DIFF_MAX_BYTES");
    expect(body).toContain("setExpandTooLarge(true)");
  });

  it("renders the 'too large' message instead of a spinner when oversize", () => {
    // Both the oversize message and the loading spinner must exist, gated on
    // expandTooLarge so an oversize body never shows a perpetual spinner.
    expect(SRC).toContain("expandTooLarge ? (");
    expect(SRC).toContain("Diff too large to display");
    expect(SRC).toContain('aria-label="Diff too large"');
    expect(SRC).toContain('aria-label="Loading diff"');
  });

  it("resets expand state when the selected file clears", () => {
    const start = SRC.indexOf("selectedFile === null");
    expect(start).toBeGreaterThan(-1);
    const block = SRC.slice(start, start + 200);
    expect(block).toContain("setExpandTooLarge(false)");
  });
});
