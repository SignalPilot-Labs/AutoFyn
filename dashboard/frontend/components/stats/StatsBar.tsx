"use client";

import { useMemo } from "react";
import { motion } from "framer-motion";
import type { Run, FeedEvent } from "@/lib/types";
import { ModelBadge } from "@/components/ui/ModelBadge";

const EMPTY_EVENTS: FeedEvent[] = [];

function computeLiveStats(events: FeedEvent[]) {
  let toolCount = 0;
  let contextTokens = 0;
  // null until a usage event reports a cost — the agent sends null when no
  // usage has settled, and collapsing that to 0 here would hide it.
  let costUsd: number | null = null;
  let tokens = ZERO_TOKENS;

  for (const e of events) {
    if (e._kind === "tool") {
      toolCount++;
    } else if (e._kind === "usage") {
      contextTokens = e.data.context_tokens;
      costUsd = e.data.total_cost_usd;
      tokens = {
        input: e.data.total_input_tokens,
        output: e.data.total_output_tokens,
        cacheWrite: e.data.cache_creation_input_tokens,
        cacheRead: e.data.cache_read_input_tokens,
      };
    }
  }

  return { toolCount, contextTokens, costUsd, tokens };
}

function formatTokenCount(n: number): string {
  if (n >= 1_000_000) return `${(n / 1_000_000).toFixed(1)}M`;
  if (n >= 1_000) return `${(n / 1_000).toFixed(1)}k`;
  return String(n);
}

export const NO_DATA = "—";

/**
 * Distinct cost states — never collapse them into a single fallback chain.
 *  - settled: DB has a real number → show `$X.XX` (no tilde)
 *  - estimated: only in-flight live cost is available → show `~$X.XX`
 *  - none: no data at all → show `—` so a broken pipeline is visible
 */
export function formatCostStat(
  settled: number | null | undefined,
  liveCost: number | null,
): { value: string; accent: string } {
  if (settled !== null && settled !== undefined) {
    return { value: `$${settled.toFixed(2)}`, accent: "text-[#00ff88]" };
  }
  if (liveCost !== null && liveCost > 0) {
    return { value: `~$${liveCost.toFixed(2)}`, accent: "text-[#00ff88]/70" };
  }
  return { value: NO_DATA, accent: "text-text-dim" };
}

export function formatToolStat(settled: number | null | undefined, liveCount: number): string {
  if (settled !== null && settled !== undefined && settled > 0) return String(settled);
  if (liveCount > 0) return String(liveCount);
  return NO_DATA;
}

export function formatContextStat(liveTokens: number, settledTokens: number | null | undefined): string {
  if (liveTokens > 0) return formatTokenCount(liveTokens);
  if (settledTokens !== null && settledTokens !== undefined && settledTokens > 0) {
    return formatTokenCount(settledTokens);
  }
  return NO_DATA;
}

/**
 * Cumulative token counters for a run. Distinct from `context_tokens`, which is
 * a snapshot of the last message's window and moves both up and down.
 */
export interface TokenTotals {
  input: number;
  output: number;
  cacheWrite: number;
  cacheRead: number;
}

export const ZERO_TOKENS: TokenTotals = { input: 0, output: 0, cacheWrite: 0, cacheRead: 0 };

export function sumTokens(t: TokenTotals): number {
  return t.input + t.output + t.cacheWrite + t.cacheRead;
}

/**
 * Total tokens processed across the run: uncached input + output (thinking
 * included) + cache writes + cache reads. Live totals win while the run
 * streams; the settled DB row takes over once it ends. Zero on both sides
 * means no usage was ever reported, which renders as `—` rather than a
 * misleading `0`.
 */
export function formatTokensStat(live: TokenTotals, settled: TokenTotals): string {
  if (sumTokens(live) > 0) return formatTokenCount(sumTokens(live));
  if (sumTokens(settled) > 0) return formatTokenCount(sumTokens(settled));
  return NO_DATA;
}

/** Hover text spelling out where the total came from. */
export function formatTokensBreakdown(t: TokenTotals): string {
  return [
    `Input ${formatTokenCount(t.input)}`,
    `Output ${formatTokenCount(t.output)}`,
    `Cache write ${formatTokenCount(t.cacheWrite)}`,
    `Cache read ${formatTokenCount(t.cacheRead)}`,
  ].join(" · ");
}

/**
 * Extract the PR number from a GitHub pull request URL.
 * Strips a trailing slash before splitting so URLs like
 * `https://github.com/owner/repo/pull/42/` return `"42"` instead of `""`.
 */
export function extractPrNumber(url: string): string {
  return url.replace(/\/$/, "").split("/").pop() ?? NO_DATA;
}

function Stat({
  icon,
  label,
  value,
  accent,
  title,
}: {
  icon: React.ReactNode;
  label: string;
  value: string;
  accent?: string;
  title?: string;
}) {
  return (
    <div className="flex items-center gap-1.5 min-w-0 shrink-0" title={title}>
      <span className="text-text-dim">{icon}</span>
      <span className="text-caption text-text-dim">{label}</span>
      <span className={`text-content font-semibold tabular-nums truncate ${accent ?? "text-text"}`}>
        {value}
      </span>
    </div>
  );
}

export interface StatsRowProps {
  run: Run | null;
  connected: boolean;
  events?: FeedEvent[];
}

export function StatsRow({
  run,
  connected,
  events = EMPTY_EVENTS,
}: StatsRowProps) {
  const live = useMemo(() => computeLiveStats(events), [events]);
  const cost = formatCostStat(run?.total_cost_usd, live.costUsd);
  const toolValue = run ? formatToolStat(run.total_tool_calls, live.toolCount) : NO_DATA;
  const contextValue = run ? formatContextStat(live.contextTokens, run.context_tokens) : NO_DATA;
  // The DB columns are non-null with a 0 default; the optional/nullable types
  // are defensive, so coerce to 0 and let a 0 total render as no-data.
  const settledTokens: TokenTotals = useMemo(
    () => ({
      input: run?.total_input_tokens ?? 0,
      output: run?.total_output_tokens ?? 0,
      cacheWrite: run?.cache_creation_input_tokens ?? 0,
      cacheRead: run?.cache_read_input_tokens ?? 0,
    }),
    [run],
  );
  const tokensValue = run ? formatTokensStat(live.tokens, settledTokens) : NO_DATA;
  const tokensTitle = sumTokens(live.tokens) > 0 ? live.tokens : settledTokens;

  if (!run) {
    return (
      <div className="h-7 flex items-center px-1">
        <span className="text-caption text-text-dim">No run selected</span>
      </div>
    );
  }

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="min-h-[28px] flex items-center gap-3 sm:gap-5 px-1 overflow-hidden"
    >
      <div className="flex items-center gap-1.5">
        <span
          className={`h-1.5 w-1.5 rounded-full ${
            connected ? "bg-[#00ff88]" : "bg-bg-indicator"
          }`}
          style={connected ? { boxShadow: "0 0 4px rgba(0, 255, 136, 0.4)" } : undefined}
        />
        <span className="text-caption text-text-secondary">
          {connected ? "Live" : "Disconnected"}
        </span>
      </div>
      <Stat
        icon={
          <svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M6.5 1L9 3.5 3.5 9H1V6.5L6.5 1z" />
          </svg>
        }
        label="Tools"
        value={toolValue}
      />
      <Stat
        icon={
          <svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" strokeWidth="1.5">
            <circle cx="5" cy="5" r="4" />
            <path d="M3.5 5h3M5 3.5v3" />
          </svg>
        }
        label="Cost"
        value={cost.value}
        accent={cost.accent}
      />
      <Stat
        icon={
          <svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M1 3h8M1 5h8M1 7h5" />
          </svg>
        }
        label="Tokens"
        value={tokensValue}
        title={formatTokensBreakdown(tokensTitle)}
      />
      <Stat
        icon={
          <svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" strokeWidth="1.5">
            <rect x="1" y="1" width="8" height="8" rx="1" />
            <path d="M1 1v8" />
          </svg>
        }
        label="Context"
        value={contextValue}
        accent="text-[#88ccff]"
      />
      <ModelBadge modelName={run.model_name} showIcon />
      {run.pr_url && (
        <a
          href={run.pr_url}
          target="_blank"
          rel="noopener noreferrer"
          className="flex items-center gap-1 text-caption text-[#88ccff] hover:text-[#aaddff] transition-colors"
        >
          <svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" strokeWidth="1.5">
            <circle cx="3" cy="3" r="1.5" />
            <circle cx="7" cy="3" r="1.5" />
            <circle cx="3" cy="7" r="1.5" />
            <line x1="3" y1="4.5" x2="3" y2="5.5" />
            <path d="M7 4.5c0 1.5-1.5 2-4 3" />
          </svg>
          PR #{extractPrNumber(run.pr_url)}
        </a>
      )}
    </motion.div>
  );
}

export function StatsBar({
  run,
  connected,
  events = EMPTY_EVENTS,
}: StatsRowProps) {
  return (
    <div className="min-h-[36px] sm:h-8 flex items-center px-3 sm:px-4 border-t border-border bg-bg">
      <StatsRow run={run} connected={connected} events={events} />
    </div>
  );
}
