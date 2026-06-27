import type { FeedEvent, FileChange } from "@/lib/types";
import type { DiffFile } from "@/lib/api";
import { getToolCategory } from "@/lib/types";

/* ── Patch types ── */
interface PatchHunk {
  lines?: string[];
}

/* ── Shared patch line counter ── */
function _countPatchLines(hunks: PatchHunk[]): { added: number; removed: number } {
  let added = 0;
  let removed = 0;
  for (const hunk of hunks) {
    if (hunk.lines === undefined) continue;
    for (const line of hunk.lines) {
      if (line.startsWith("+") && !line.startsWith("+++")) added++;
      if (line.startsWith("-") && !line.startsWith("---")) removed++;
    }
  }
  return { added, removed };
}

/* ── Tree Node ── */
export interface TreeNode {
  name: string;
  fullPath: string;
  isDir: boolean;
  children: Map<string, TreeNode>;
  added: number;
  removed: number;
  status?: string;
}

/* ── Path normalisation ── */
export function norm(p: string): string {
  return p
    .replace(/^\/tmp\//, "tmp/")
    .replace(/^\/home\/agentuser\/repo\//, "")
    .replace(/^\/workspace\//, "")
    .replace(/^\/home\/agentuser\//, "~/");
}

/* ── Extract file changes from tool call events (live feed) ── */
export function extractFileChanges(events: FeedEvent[]): FileChange[] {
  const changes: FileChange[] = [];
  for (const ev of events) {
    if (ev._kind !== "tool") continue;
    const tc = ev.data;
    const cat = getToolCategory(tc.tool_name);
    const input = tc.input_data || {};
    const output = tc.output_data || {};

    switch (cat) {
      case "read": {
        const fileObj = (output as Record<string, unknown>)?.file as Record<string, unknown> | undefined;
        const fp = (input.file_path as string) || (fileObj?.filePath as string) || "";
        if (fp) {
          changes.push({
            path: norm(fp),
            action: "read",
            timestamp: tc.ts,
            toolCallId: tc.id,
            toolName: tc.tool_name,
          });
        }
        break;
      }
      case "write": {
        const fp = (input.file_path as string) || (output.filePath as string) || "";
        if (fp) {
          const patch = output.structuredPatch as PatchHunk[] | undefined;
          const counts = patch ? _countPatchLines(patch) : undefined;
          changes.push({
            path: norm(fp),
            action: "write",
            linesAdded: counts ? counts.added || undefined : undefined,
            linesRemoved: counts ? counts.removed || undefined : undefined,
            timestamp: tc.ts,
            toolCallId: tc.id,
            toolName: tc.tool_name,
          });
        }
        break;
      }
      case "edit": {
        const fp = (input.file_path as string) || (output.filePath as string) || "";
        if (fp) {
          const patch = output.structuredPatch as PatchHunk[] | undefined;
          const counts = patch ? _countPatchLines(patch) : undefined;
          changes.push({
            path: norm(fp),
            action: "edit",
            linesAdded: counts ? counts.added || undefined : undefined,
            linesRemoved: counts ? counts.removed || undefined : undefined,
            timestamp: tc.ts,
            toolCallId: tc.id,
            toolName: tc.tool_name,
          });
        }
        break;
      }
    }
  }
  return changes;
}

/* ── Build tree from git diff files ── */
export function buildTreeFromDiff(files: DiffFile[]): TreeNode {
  const root: TreeNode = {
    name: "",
    fullPath: "",
    isDir: true,
    children: new Map(),
    added: 0,
    removed: 0,
  };
  for (const f of files) {
    const parts = f.path.split("/").filter(Boolean);
    let cur = root;
    for (let i = 0; i < parts.length; i++) {
      const part = parts[i];
      const isLast = i === parts.length - 1;
      if (!cur.children.has(part)) {
        cur.children.set(part, {
          name: part,
          fullPath: parts.slice(0, i + 1).join("/"),
          isDir: !isLast,
          children: new Map(),
          added: 0,
          removed: 0,
        });
      }
      cur = cur.children.get(part)!;
      if (isLast) {
        cur.added = f.added;
        cur.removed = f.removed;
        cur.status = f.status;
      }
    }
  }
  return root;
}

