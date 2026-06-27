import { describe, it, expect } from "vitest";
import {
  norm,
  extractFileChanges,
  buildTreeFromDiff,
} from "@/lib/worktree-utils";

describe("norm", () => {
  it("strips /home/agentuser/repo/ prefix", () => {
    expect(norm("/home/agentuser/repo/src/main.ts")).toBe("src/main.ts");
  });
  it("strips /workspace/ prefix", () => {
    expect(norm("/workspace/foo.py")).toBe("foo.py");
  });
  it("converts /home/agentuser/ to ~/", () => {
    expect(norm("/home/agentuser/.config/file")).toBe("~/.config/file");
  });
  it("returns unchanged if no prefix match", () => {
    expect(norm("relative/path.ts")).toBe("relative/path.ts");
  });
  it("strips /tmp/ prefix to tmp/", () => {
    expect(norm("/tmp/memory/run_state.md")).toBe("tmp/memory/run_state.md");
  });
  it("strips /tmp/round-N prefix to tmp/round-N", () => {
    expect(norm("/tmp/round-1/architect.md")).toBe("tmp/round-1/architect.md");
  });
});

describe("buildTreeFromDiff", () => {
  it("returns empty root for empty input", () => {
    const root = buildTreeFromDiff([]);
    expect(root.children.size).toBe(0);
  });
  it("builds nested tree from file paths", () => {
    const root = buildTreeFromDiff([
      { path: "src/index.ts", added: 10, removed: 2, status: "modified" },
      { path: "src/utils/helper.ts", added: 5, removed: 0, status: "added" },
    ]);
    expect(root.children.has("src")).toBe(true);
    const src = root.children.get("src")!;
    expect(src.isDir).toBe(true);
    expect(src.children.has("index.ts")).toBe(true);
    expect(src.children.get("index.ts")!.added).toBe(10);
    expect(src.children.has("utils")).toBe(true);
  });
  it("marks leaf nodes with status", () => {
    const root = buildTreeFromDiff([
      { path: "deleted.py", added: 0, removed: 50, status: "deleted" },
    ]);
    const leaf = root.children.get("deleted.py")!;
    expect(leaf.status).toBe("deleted");
    expect(leaf.removed).toBe(50);
  });
  it("includes tmp/ paths in the same tree (unified list)", () => {
    // repo and tmp file lists now concat into one buildTreeFromDiff call,
    // so a tmp/round-N path must build the same nested structure.
    const root = buildTreeFromDiff([
      { path: "src/a.ts", added: 1, removed: 0, status: "modified" },
      { path: "tmp/round-1/architect.md", added: 9, removed: 0, status: "added" },
    ]);
    expect(root.children.has("src")).toBe(true);
    const tmp = root.children.get("tmp")!;
    expect(tmp.isDir).toBe(true);
    const leaf = tmp.children.get("round-1")!.children.get("architect.md")!;
    expect(leaf.status).toBe("added");
    expect(leaf.added).toBe(9);
  });
});

describe("extractFileChanges", () => {
  it("returns empty for no events", () => {
    expect(extractFileChanges([])).toEqual([]);
  });
  it("extracts read action from tool event", () => {
    const changes = extractFileChanges([{
      _kind: "tool",
      data: {
        id: 1, tool_name: "Read", ts: "t1",
        input_data: { file_path: "/home/agentuser/repo/src/main.ts" },
        output_data: {},
      },
    } as any]);
    expect(changes).toHaveLength(1);
    expect(changes[0].action).toBe("read");
    expect(changes[0].path).toBe("src/main.ts");
  });
  it("extracts edit with line counts", () => {
    const changes = extractFileChanges([{
      _kind: "tool",
      data: {
        id: 2, tool_name: "Edit", ts: "t2",
        input_data: { file_path: "/workspace/foo.py" },
        output_data: {
          structuredPatch: [{ lines: ["+added", "-removed", " context", "+another"] }],
        },
      },
    } as any]);
    expect(changes).toHaveLength(1);
    expect(changes[0].action).toBe("edit");
    expect(changes[0].linesAdded).toBe(2);
    expect(changes[0].linesRemoved).toBe(1);
  });

  it("write with structuredPatch counts actual + lines", () => {
    const changes = extractFileChanges([{
      _kind: "tool",
      data: {
        id: 3, tool_name: "Write", ts: "t3",
        input_data: { file_path: "/workspace/new-file.ts" },
        output_data: {
          structuredPatch: [{ lines: ["+new", " ctx", "+added", "-old"] }],
        },
      },
    } as any]);
    expect(changes).toHaveLength(1);
    expect(changes[0].action).toBe("write");
    expect(changes[0].linesAdded).toBe(2);
    expect(changes[0].linesRemoved).toBe(1);
  });

  it("write without structuredPatch has undefined line counts", () => {
    const changes = extractFileChanges([{
      _kind: "tool",
      data: {
        id: 4, tool_name: "Write", ts: "t4",
        input_data: { file_path: "/workspace/new-file.ts" },
        output_data: {},
      },
    } as any]);
    expect(changes).toHaveLength(1);
    expect(changes[0].action).toBe("write");
    expect(changes[0].linesAdded).toBeUndefined();
    expect(changes[0].linesRemoved).toBeUndefined();
  });

  it("write with both + and - lines counts both", () => {
    const changes = extractFileChanges([{
      _kind: "tool",
      data: {
        id: 5, tool_name: "Write", ts: "t5",
        input_data: { file_path: "/workspace/rewritten.ts" },
        output_data: {
          structuredPatch: [
            { lines: ["+++ b/rewritten.ts", "+line1", "+line2", "-old1", " ctx"] },
            { lines: ["+line3", "-old2", "-old3"] },
          ],
        },
      },
    } as any]);
    expect(changes).toHaveLength(1);
    expect(changes[0].linesAdded).toBe(3);
    expect(changes[0].linesRemoved).toBe(3);
  });

  it("edit still works after refactor to shared helper", () => {
    const changes = extractFileChanges([{
      _kind: "tool",
      data: {
        id: 6, tool_name: "Edit", ts: "t6",
        input_data: { file_path: "/workspace/existing.ts" },
        output_data: {
          structuredPatch: [
            { lines: ["--- a/existing.ts", "+++ b/existing.ts", "+added1", "-removed1", " unchanged"] },
            { lines: ["+added2", "+added3"] },
          ],
        },
      },
    } as any]);
    expect(changes).toHaveLength(1);
    expect(changes[0].action).toBe("edit");
    expect(changes[0].linesAdded).toBe(3);
    expect(changes[0].linesRemoved).toBe(1);
  });
});
