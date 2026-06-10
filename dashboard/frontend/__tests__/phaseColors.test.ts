import { describe, it, expect } from "vitest";
import {
  DEFAULT_PHASE_META,
  PHASE_META,
  hexToRgba,
  resolvePhase,
} from "@/lib/phaseColors";
import type { SubagentPhase } from "@/lib/phaseColors";

// The backend (GET /repos/{repo}/subagents) is the source of truth for
// name→phase. resolvePhase reads only from the map it's handed — no hardcoded
// agent names — so shipped and repo-defined agents resolve identically.
const PHASES: Record<string, SubagentPhase> = {
  "code-explorer": "explore",
  "architect": "plan",
  "backend-dev": "build",
  "code-reviewer": "review",
  // a repo-defined agent the frontend can't know statically
  "proof-builder": "build",
};

describe("resolvePhase", () => {
  it("resolves a name to its phase and color from the supplied map", () => {
    expect(resolvePhase("code-explorer", PHASES).phase).toBe("explore");
    expect(resolvePhase("code-explorer", PHASES).meta).toBe(PHASE_META.explore);
    expect(resolvePhase("architect", PHASES).meta.color).toBe("#cc88ff");
    expect(resolvePhase("code-reviewer", PHASES).phase).toBe("review");
  });

  it("colors a repo-defined agent the same as a shipped one (the bug)", () => {
    // proof-builder is not a shipped name — before the backend became the
    // source of truth it fell back to orange. Now it resolves to build/green.
    const result = resolvePhase("proof-builder", PHASES);
    expect(result.phase).toBe("build");
    expect(result.meta).toBe(PHASE_META.build);
  });

  it("falls back to DEFAULT_PHASE_META for a name not in the map", () => {
    const result = resolvePhase("made-up-agent", PHASES);
    expect(result.phase).toBeNull();
    expect(result.meta).toBe(DEFAULT_PHASE_META);
  });

  it("falls back to the default for an empty map (e.g. before load)", () => {
    const result = resolvePhase("code-explorer", {});
    expect(result.phase).toBeNull();
    expect(result.meta.color).toBe("#ff8844");
  });

  it("returns null phase but orange color for empty string", () => {
    const result = resolvePhase("", PHASES);
    expect(result.phase).toBeNull();
    expect(result.meta.color).toBe("#ff8844");
  });
});

describe("PHASE_META color palette", () => {
  it("assigns a unique color to each phase", () => {
    const colors = Object.values(PHASE_META).map((m) => m.color);
    expect(new Set(colors).size).toBe(colors.length);
  });

  it("keeps Review distinct from the running-state amber (#ffaa00)", () => {
    // Regression guard: previously Review == #ffaa00 which collided with
    // the running-state indicator color, making Review cards fully amber
    // with no phase/state separation. Never let it go back.
    expect(PHASE_META.review.color).not.toBe("#ffaa00");
  });
});

describe("hexToRgba", () => {
  it("converts 6-digit hex to rgba with the given alpha", () => {
    expect(hexToRgba("#44ddff", 0.5)).toBe("rgba(68, 221, 255, 0.5)");
    expect(hexToRgba("#000000", 1)).toBe("rgba(0, 0, 0, 1)");
    expect(hexToRgba("#ffffff", 0)).toBe("rgba(255, 255, 255, 0)");
  });

  it("accepts uppercase hex digits", () => {
    expect(hexToRgba("#FFAA00", 0.3)).toBe("rgba(255, 170, 0, 0.3)");
  });

  it("throws on missing # prefix", () => {
    expect(() => hexToRgba("44ddff", 0.5)).toThrow(/invalid hex color/);
  });

  it("throws on 3-digit shorthand", () => {
    expect(() => hexToRgba("#fff", 0.5)).toThrow(/invalid hex color/);
  });

  it("throws on 8-digit hex with alpha channel", () => {
    expect(() => hexToRgba("#44ddff80", 0.5)).toThrow(/invalid hex color/);
  });

  it("throws on non-hex characters", () => {
    expect(() => hexToRgba("#gghhii", 0.5)).toThrow(/invalid hex color/);
  });

  it("throws on alpha outside [0, 1]", () => {
    expect(() => hexToRgba("#44ddff", 1.5)).toThrow(/out of range/);
    expect(() => hexToRgba("#44ddff", -0.1)).toThrow(/out of range/);
  });

  it("works for every phase color without throwing", () => {
    for (const meta of Object.values(PHASE_META)) {
      expect(() => hexToRgba(meta.color, 0.25)).not.toThrow();
    }
    expect(() => hexToRgba(DEFAULT_PHASE_META.color, 0.25)).not.toThrow();
  });
});
