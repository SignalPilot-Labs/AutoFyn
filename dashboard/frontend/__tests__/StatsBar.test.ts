/**
 * StatsBar fail-fast formatter tests.
 *
 * Guards the distinction between "settled", "estimated", and "no data".
 * The previous bug was a `||` chain that masked $0.00 with stale live cost.
 */

import { describe, it, expect } from "vitest";
import {
  NO_DATA,
  ZERO_TOKENS,
  formatCostStat,
  formatToolStat,
  formatContextStat,
  formatTokensStat,
  formatTokensBreakdown,
  sumTokens,
  extractPrNumber,
  type TokenTotals,
} from "@/components/stats/StatsBar";

describe("formatCostStat", () => {
  it("uses settled value when present (no tilde)", () => {
    expect(formatCostStat(2.5, 0)).toEqual({
      value: "$2.50",
      accent: "text-[#00ff88]",
    });
  });

  it("renders settled $0.00 instead of falling through to live cost", () => {
    // Regression: || would mask $0 with live, ?? was a half-fix.
    expect(formatCostStat(0, 1.23)).toEqual({
      value: "$0.00",
      accent: "text-[#00ff88]",
    });
  });

  it("falls back to live estimate with tilde when settled is null", () => {
    expect(formatCostStat(null, 1.23)).toEqual({
      value: "~$1.23",
      accent: "text-[#00ff88]/70",
    });
  });

  it("renders no-data when both are missing", () => {
    expect(formatCostStat(null, 0)).toEqual({
      value: NO_DATA,
      accent: "text-text-dim",
    });
  });

  it("treats undefined like null", () => {
    expect(formatCostStat(undefined, 0.5).value).toBe("~$0.50");
  });
});

describe("formatToolStat", () => {
  it("uses live count when settled is zero (active run)", () => {
    expect(formatToolStat(0, 5)).toBe("5");
  });

  it("uses live count when settled is null", () => {
    expect(formatToolStat(null, 5)).toBe("5");
  });

  it("renders no-data when both are missing", () => {
    expect(formatToolStat(null, 0)).toBe(NO_DATA);
  });
});

describe("formatContextStat", () => {
  it("formats live tokens with k suffix", () => {
    expect(formatContextStat(2500, null)).toBe("2.5k");
  });

  it("falls back to settled tokens when live is zero", () => {
    expect(formatContextStat(0, 1500)).toBe("1.5k");
  });

  it("renders no-data when both are zero", () => {
    expect(formatContextStat(0, 0)).toBe(NO_DATA);
  });
});

describe("formatTokensStat", () => {
  const live: TokenTotals = { input: 1000, output: 2000, cacheWrite: 500, cacheRead: 6500 };
  const settled: TokenTotals = { input: 10, output: 20, cacheWrite: 5, cacheRead: 65 };

  it("sums all four counters, not just input+output", () => {
    // Regression: cache tokens dominate agentic runs; omitting them
    // under-reports the total by an order of magnitude.
    expect(formatTokensStat(live, ZERO_TOKENS)).toBe("10.0k");
  });

  it("prefers live totals over settled while a run streams", () => {
    expect(formatTokensStat(live, settled)).toBe("10.0k");
  });

  it("falls back to settled totals once live is empty", () => {
    expect(formatTokensStat(ZERO_TOKENS, settled)).toBe("100");
  });

  it("renders no-data rather than 0 when nothing was ever reported", () => {
    // A pipeline that never emitted usage must not look like a free run.
    expect(formatTokensStat(ZERO_TOKENS, ZERO_TOKENS)).toBe(NO_DATA);
  });

  it("does not confuse a context snapshot with a cumulative total", () => {
    // context_tokens goes up and down; these counters only accumulate.
    expect(sumTokens(live)).toBe(10000);
  });
});

describe("formatTokensBreakdown", () => {
  it("spells out every component of the total", () => {
    expect(formatTokensBreakdown({ input: 1500, output: 2_000_000, cacheWrite: 0, cacheRead: 300 })).toBe(
      "Input 1.5k · Output 2.0M · Cache write 0 · Cache read 300",
    );
  });
});

describe("extractPrNumber", () => {
  it("extracts PR number from a normal URL", () => {
    // Regression: .pop() on split of a clean URL must return the number string.
    expect(extractPrNumber("https://github.com/owner/repo/pull/42")).toBe("42");
  });

  it("extracts PR number from a trailing-slash URL", () => {
    // Regression: .pop() previously returned "" because split produced ["...", "42", ""].
    expect(extractPrNumber("https://github.com/owner/repo/pull/42/")).toBe("42");
  });
});
