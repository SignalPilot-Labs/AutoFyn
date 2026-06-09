/**
 * Unit tests for the shared event-pipeline primitives.
 *
 * These were previously reimplemented (and only indirectly tested) across
 * eventMerge, loadRunHistory, and useEventState. Now that they are the single
 * source of truth for pre→post folding and event ordering, they are tested
 * directly here.
 */

import { describe, it, expect } from "vitest";
import type { FeedEvent, ToolCall } from "@/lib/types";
import {
  applyPostToPre,
  getEventTs,
  getEventPriority,
  getEventId,
  compareEvents,
} from "@/lib/eventPipeline";

function toolCall(over: Partial<ToolCall>): ToolCall {
  return {
    id: 1,
    run_id: "r",
    ts: "2026-01-01T00:00:00.000Z",
    phase: "pre",
    tool_name: "Write",
    input_data: { file_path: "a.ts" },
    output_data: null,
    duration_ms: null,
    permitted: true,
    deny_reason: null,
    agent_role: "worker",
    tool_use_id: "tu-1",
    session_id: null,
    agent_id: null,
    ...over,
  };
}

describe("applyPostToPre", () => {
  it("folds post output/duration/phase onto the pre's identity", () => {
    const pre = toolCall({ id: 10, phase: "pre", tool_use_id: "tu-x", output_data: null });
    const post = toolCall({
      id: 11,
      phase: "post",
      tool_use_id: "tu-x",
      output_data: { result: "ok" },
      duration_ms: 42,
    });

    const merged = applyPostToPre(pre, post);

    // Pre's identity (id, tool_use_id, input) is preserved.
    expect(merged.id).toBe(10);
    expect(merged.tool_use_id).toBe("tu-x");
    expect(merged.input_data).toEqual({ file_path: "a.ts" });
    // Post's completion fields are applied.
    expect(merged.output_data).toEqual({ result: "ok" });
    expect(merged.duration_ms).toBe(42);
    expect(merged.phase).toBe("post");
  });

  it("is immutable — neither argument is mutated", () => {
    const pre = toolCall({ id: 1, phase: "pre", output_data: null, duration_ms: null });
    const post = toolCall({ id: 2, phase: "post", output_data: { x: 1 }, duration_ms: 5 });

    applyPostToPre(pre, post);

    // pre keeps its original (pre) state.
    expect(pre.phase).toBe("pre");
    expect(pre.output_data).toBeNull();
    expect(pre.duration_ms).toBeNull();
    // post is read-only input — also untouched.
    expect(post.id).toBe(2);
    expect(post.phase).toBe("post");
    expect(post.output_data).toEqual({ x: 1 });
    expect(post.duration_ms).toBe(5);
  });
});

describe("getEventTs / getEventPriority / getEventId", () => {
  const toolEv: FeedEvent = { _kind: "tool", data: toolCall({ id: 7, ts: "2026-01-01T00:00:01.000Z" }) };
  const auditEv: FeedEvent = {
    _kind: "audit",
    data: { id: 3, run_id: "r", ts: "2026-01-01T00:00:02.000Z", event_type: "round_started", details: {} },
  };
  const llmEv: FeedEvent = { _kind: "llm_text", text: "hi", ts: "2026-01-01T00:00:03.000Z", agent_role: "worker" };

  it("reads the ts off every event variant", () => {
    expect(getEventTs(toolEv)).toBe("2026-01-01T00:00:01.000Z");
    expect(getEventTs(auditEv)).toBe("2026-01-01T00:00:02.000Z");
    expect(getEventTs(llmEv)).toBe("2026-01-01T00:00:03.000Z");
  });

  it("ranks non-tool events before tool events", () => {
    expect(getEventPriority(toolEv)).toBe(1);
    expect(getEventPriority(auditEv)).toBe(0);
    expect(getEventPriority(llmEv)).toBe(0);
  });

  it("returns row id for tool/audit, 0 for llm", () => {
    expect(getEventId(toolEv)).toBe(7);
    expect(getEventId(auditEv)).toBe(3);
    expect(getEventId(llmEv)).toBe(0);
  });
});

describe("compareEvents", () => {
  it("orders by timestamp ascending", () => {
    const early: FeedEvent = { _kind: "tool", data: toolCall({ id: 1, ts: "2026-01-01T00:00:00.000Z" }) };
    const late: FeedEvent = { _kind: "tool", data: toolCall({ id: 2, ts: "2026-01-01T00:00:05.000Z" }) };
    expect(compareEvents(early, late)).toBeLessThan(0);
    expect(compareEvents(late, early)).toBeGreaterThan(0);
  });

  it("at equal ts, audit sorts before tool", () => {
    const ts = "2026-01-01T00:00:00.000Z";
    const tool: FeedEvent = { _kind: "tool", data: toolCall({ id: 9, ts }) };
    const audit: FeedEvent = { _kind: "audit", data: { id: 9, run_id: "r", ts, event_type: "round_started", details: {} } };
    expect(compareEvents(audit, tool)).toBeLessThan(0);
  });

  it("at equal ts and priority, orders by id", () => {
    const ts = "2026-01-01T00:00:00.000Z";
    const a: FeedEvent = { _kind: "tool", data: toolCall({ id: 1, ts }) };
    const b: FeedEvent = { _kind: "tool", data: toolCall({ id: 2, ts }) };
    expect(compareEvents(a, b)).toBeLessThan(0);
    expect(compareEvents(b, a)).toBeGreaterThan(0);
  });
});
