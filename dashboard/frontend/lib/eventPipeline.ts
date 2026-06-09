/**
 * Canonical event-pipeline primitives shared by the live SSE path
 * (eventMerge), the history-load path (loadRunHistory), and the cross-stream
 * dedup (useEventState).
 *
 * Three things were independently reimplemented across those files and are
 * unified here so the pairing rule and the sort order have one definition:
 *
 *  - applyPostToPre: how a post tool row is folded onto its pre.
 *  - getEventTs / getEventPriority / getEventId: the sort key components.
 *  - compareEvents: the canonical (ts, priority, id) ordering.
 *
 * The three higher-level mergers (live append, history batch, cross-stream
 * dedup) stay distinct — they operate on different inputs and lifecycles —
 * but all route their actual pre→post fold through applyPostToPre.
 */

import type { FeedEvent, ToolCall } from "@/lib/types";

/**
 * Fold a post tool row onto its matched pre, immutably.
 *
 * Returns a new ToolCall carrying the pre's identity (id, tool_use_id, input)
 * with the post's output_data, duration_ms, and phase. Never mutates either
 * argument. This is the single definition of "a tool call completed".
 */
export function applyPostToPre(pre: ToolCall, post: ToolCall): ToolCall {
  return {
    ...pre,
    output_data: post.output_data,
    duration_ms: post.duration_ms,
    phase: "post",
  };
}

/** Sort timestamp for any feed event (all variants carry a `ts`). */
export function getEventTs(e: FeedEvent): string {
  if (e._kind === "tool") return e.data.ts;
  if (e._kind === "audit") return e.data.ts;
  if (e._kind === "usage") return e.data.ts;
  return e.ts;
}

/**
 * Type priority for equal-timestamp ordering: audit/llm events (0) sort
 * before tool events (1). Mirrors the backend's TYPE_PRIORITY.
 */
export function getEventPriority(e: FeedEvent): number {
  return e._kind === "tool" ? 1 : 0;
}

/** Stable secondary key: the row id for tool/audit events, 0 otherwise. */
export function getEventId(e: FeedEvent): number {
  if (e._kind === "tool") return e.data.id;
  if (e._kind === "audit") return e.data.id;
  return 0;
}

/**
 * Canonical feed-event ordering: by timestamp, then audit-before-tool,
 * then by id. Used wherever a merged history+live stream is sorted.
 */
export function compareEvents(a: FeedEvent, b: FeedEvent): number {
  const tsA = new Date(getEventTs(a)).getTime();
  const tsB = new Date(getEventTs(b)).getTime();
  if (tsA !== tsB) return tsA - tsB;
  const prio = getEventPriority(a) - getEventPriority(b);
  if (prio !== 0) return prio;
  return getEventId(a) - getEventId(b);
}
