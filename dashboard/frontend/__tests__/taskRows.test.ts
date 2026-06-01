/**
 * Unit tests for taskRows — normalization of the SDK's relational task tools
 * (TaskCreate/TaskUpdate/TaskGet/TaskList) into TodoDisplay-style status rows.
 *
 * Covers each tool's branch plus the cross-cutting rules: "deleted" tasks are
 * dropped, statusChange renders a "from → to" suffix, and taskId/subject fall
 * back across the merged pre/post payloads.
 */

import { describe, it, expect } from "vitest";
import { taskRows } from "@/components/feed/ToolDisplayCards";

describe("taskRows", () => {
  it("TaskCreate: pending row from input subject", () => {
    const rows = taskRows("TaskCreate", { subject: "Live-verify Finding A" }, null);
    expect(rows).toEqual([{ status: "pending", content: "Live-verify Finding A" }]);
  });

  it("TaskCreate: subject falls back to output.task when input is empty (post-only)", () => {
    const rows = taskRows("TaskCreate", {}, { task: { id: "2", subject: "From output" } });
    expect(rows).toEqual([{ status: "pending", content: "From output" }]);
  });

  it("TaskUpdate: renders status and from → to suffix", () => {
    const rows = taskRows(
      "TaskUpdate",
      { subject: "Build PoC" },
      { statusChange: { from: "pending", to: "in_progress" } }
    );
    expect(rows).toEqual([
      { status: "in_progress", content: "Build PoC (pending → in_progress)" },
    ]);
  });

  it("TaskUpdate: taskId from output when input is empty (post-only)", () => {
    const rows = taskRows(
      "TaskUpdate",
      {},
      { taskId: "7", statusChange: { from: "pending", to: "completed" } }
    );
    expect(rows).toEqual([
      { status: "completed", content: "Task 7 (pending → completed)" },
    ]);
  });

  it("TaskUpdate: unknown status (no statusChange, no input.status) falls back to pending", () => {
    const rows = taskRows("TaskUpdate", { subject: "Edit subject", taskId: "1" }, { taskId: "1" });
    expect(rows).toEqual([{ status: "pending", content: "Edit subject" }]);
  });

  it("TaskUpdate: deleted status drops the row", () => {
    const rows = taskRows(
      "TaskUpdate",
      { taskId: "3" },
      { statusChange: { from: "pending", to: "deleted" } }
    );
    expect(rows).toEqual([]);
  });

  it("TaskList: one row per task, deleted tasks dropped", () => {
    const rows = taskRows("TaskList", {}, {
      tasks: [
        { id: "1", subject: "A", status: "completed" },
        { id: "2", subject: "B", status: "deleted" },
        { id: "3", subject: "C", status: "pending" },
      ],
    });
    expect(rows).toEqual([
      { status: "completed", content: "A" },
      { status: "pending", content: "C" },
    ]);
  });

  it("TaskGet: single row from output.task", () => {
    const rows = taskRows("TaskGet", {}, {
      task: { id: "1", subject: "Get me", status: "in_progress" },
    });
    expect(rows).toEqual([{ status: "in_progress", content: "Get me" }]);
  });

  it("TaskGet: null task returns no rows", () => {
    const rows = taskRows("TaskGet", {}, { task: null });
    expect(rows).toEqual([]);
  });
});
