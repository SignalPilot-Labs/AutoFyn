/**
 * Direct tests for mergeToolPhases — the history-batch pre/post pairing.
 *
 * This is the function whose pairing condition changed when the event-pipeline
 * was unified (immutable fold via applyPostToPre + the `!pre.output_data`
 * guard). Its control flow (one backward loop over a batch) differs from the
 * live incremental merge, so the eventMerge tests do not transfer — it needs
 * its own coverage.
 */

import { describe, it, expect } from "vitest";
import type { ToolCall } from "@/lib/types";
import { mergeToolPhases } from "@/lib/loadRunHistory";

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

describe("mergeToolPhases", () => {
  it("folds a post onto its matching pre by tool_use_id", () => {
    const pre = toolCall({ id: 1, phase: "pre", tool_use_id: "tu-a", output_data: null });
    const post = toolCall({
      id: 2,
      phase: "post",
      tool_use_id: "tu-a",
      output_data: { result: "ok" },
      duration_ms: 30,
    });

    const merged = mergeToolPhases([pre, post]);

    expect(merged).toHaveLength(1);
    expect(merged[0].id).toBe(1); // pre's identity
    expect(merged[0].input_data).toEqual({ file_path: "a.ts" });
    expect(merged[0].phase).toBe("post");
    expect(merged[0].output_data).toEqual({ result: "ok" });
    expect(merged[0].duration_ms).toBe(30);
  });

  it("keeps an orphan post (no matching pre) as a standalone entry", () => {
    const orphan = toolCall({
      id: 5,
      phase: "post",
      tool_use_id: "tu-orphan",
      output_data: { error: "boom" },
    });

    const merged = mergeToolPhases([orphan]);

    // The post must survive so error outputs stay visible.
    expect(merged).toHaveLength(1);
    expect(merged[0].id).toBe(5);
    expect(merged[0].phase).toBe("post");
    expect(merged[0].output_data).toEqual({ error: "boom" });
  });

  it("does not mutate the input rows (immutable fold)", () => {
    const pre = toolCall({ id: 1, phase: "pre", tool_use_id: "tu-a", output_data: null });
    const post = toolCall({ id: 2, phase: "post", tool_use_id: "tu-a", output_data: { result: "ok" } });

    mergeToolPhases([pre, post]);

    // The original pre row is untouched — the fold produced a new object.
    expect(pre.phase).toBe("pre");
    expect(pre.output_data).toBeNull();
  });

  it("pairs concurrent distinct tool_use_ids without cross-pairing", () => {
    // Two tools in flight at once: preA, preB, then postB, postA.
    const preA = toolCall({ id: 1, phase: "pre", tool_use_id: "tu-a", input_data: { file_path: "a.ts" } });
    const preB = toolCall({ id: 2, phase: "pre", tool_use_id: "tu-b", input_data: { file_path: "b.ts" } });
    const postB = toolCall({ id: 3, phase: "post", tool_use_id: "tu-b", output_data: { which: "B" } });
    const postA = toolCall({ id: 4, phase: "post", tool_use_id: "tu-a", output_data: { which: "A" } });

    const merged = mergeToolPhases([preA, preB, postB, postA]);

    expect(merged).toHaveLength(2);
    const byPath = Object.fromEntries(merged.map((t) => [t.input_data?.file_path, t]));
    expect(byPath["a.ts"].output_data).toEqual({ which: "A" });
    expect(byPath["b.ts"].output_data).toEqual({ which: "B" });
  });

  it("does not fold a post onto a pre that already carries output_data", () => {
    // Backend invariant: a 'pre' row never has output_data. This guards the
    // pairing against an already-completed pre — the post stays standalone.
    const completedPre = toolCall({
      id: 1,
      phase: "pre",
      tool_use_id: "tu-a",
      output_data: { result: "already-done" },
    });
    const post = toolCall({ id: 2, phase: "post", tool_use_id: "tu-a", output_data: { result: "new" } });

    const merged = mergeToolPhases([completedPre, post]);

    // Guard skips the completed pre; the post is kept separate rather than
    // overwriting it.
    expect(merged).toHaveLength(2);
    expect(merged[0].output_data).toEqual({ result: "already-done" });
    expect(merged[1].output_data).toEqual({ result: "new" });
  });
});
