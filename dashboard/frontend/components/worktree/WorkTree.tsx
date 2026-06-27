"use client";

import { useState, useMemo, useEffect, useCallback, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { clsx } from "clsx";
import type { FeedEvent, RunStatus } from "@/lib/types";
import type { DiffStats, DiffFile } from "@/lib/api";
import { fetchRunDiff, fetchDiffRepo, fetchDiffTmp } from "@/lib/api";
import {
  extractFileChanges,
  buildTreeFromDiff,
} from "@/lib/worktree-utils";
import type { TreeNode } from "@/lib/worktree-utils";
import {
  DIFF_MAX_BYTES,
  DIFF_POLL_INTERVAL_MS,
  DIFF_REFETCH_DEBOUNCE_MS,
  TERMINAL_STATUSES,
} from "@/lib/constants";
import { FileDiffViewer } from "./FileDiffViewer";

/* ── Icons ── */
function FileIcon({ name, status }: { name: string; status?: string }) {
  const ext = name.split(".").pop()?.toLowerCase() || "";
  let color = "#555";
  if (status === "added") color = "#00ff88";
  else if (status === "deleted") color = "#ff4444";
  else if (status === "modified") color = "#ffcc44";
  else if (ext === "tsx" || ext === "ts") color = "#3178c6";
  else if (ext === "css") color = "#264de4";
  else if (ext === "py") color = "#3776ab";
  else if (ext === "sql") color = "#e38c00";

  return (
    <svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke={color} strokeWidth="1" strokeLinecap="round">
      <path d="M3 1.5h4.5l2.5 2.5v6.5a1 1 0 01-1 1H3a1 1 0 01-1-1v-8a1 1 0 011-1z" />
      <polyline points="7.5 1.5 7.5 4 10 4" />
    </svg>
  );
}

function DirIcon({ open }: { open: boolean }) {
  return (
    <svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="#555" strokeWidth="1" strokeLinecap="round">
      {open
        ? <><path d="M1 3.5h3l1-1h4.5a1 1 0 011 1V4H2.5L1 9V3.5z" /><path d="M2.5 4L1 9h8.5l1.5-5H2.5z" /></>
        : <path d="M1 3h3l1 1h5a1 1 0 011 1v5a1 1 0 01-1 1H2a1 1 0 01-1-1V3z" />}
    </svg>
  );
}

/* ── Tree Node Component ── */
function NodeItem({
  node,
  depth,
  onFileClick,
  clickablePaths,
}: {
  node: TreeNode;
  depth: number;
  onFileClick: ((path: string, status: string) => void) | null;
  clickablePaths: ReadonlySet<string> | null;
}) {
  const [open, setOpen] = useState(depth < 2);
  const isDir = node.isDir && node.children.size > 0;

  const sorted = useMemo(() => {
    const arr = Array.from(node.children.values());
    return arr.sort((a, b) => {
      if (a.isDir && !b.isDir) return -1;
      if (!a.isDir && b.isDir) return 1;
      return a.name.localeCompare(b.name);
    });
  }, [node.children]);

  const totalAdded = useMemo(() => {
    if (!node.isDir) return node.added;
    let sum = node.added;
    const walk = (n: TreeNode) => { sum += n.added; n.children.forEach(walk); };
    node.children.forEach(walk);
    return sum;
  }, [node]);

  const totalRemoved = useMemo(() => {
    if (!node.isDir) return node.removed;
    let sum = node.removed;
    const walk = (n: TreeNode) => { sum += n.removed; n.children.forEach(walk); };
    node.children.forEach(walk);
    return sum;
  }, [node]);

  const isClickable = !isDir && onFileClick !== null && (clickablePaths === null || clickablePaths.has(node.fullPath));

  const handleClick = () => {
    if (isDir) { setOpen(!open); return; }
    if (isClickable) onFileClick!(node.fullPath, node.status ?? "modified");
  };

  return (
    <div>
      <div
        className={clsx(
          "flex items-center gap-1.5 py-[3px] px-1 rounded transition-colors text-content",
          isDir ? "cursor-pointer" : isClickable ? "cursor-pointer" : "cursor-default",
          isClickable ? "hover:bg-white/[0.06]" : "hover:bg-white/[0.03]",
        )}
        style={{ paddingLeft: depth * 14 + 4 }}
        onClick={handleClick}
      >
        {isDir ? (
          <svg width="8" height="8" viewBox="0 0 8 8" fill="none" stroke="#888" strokeWidth="1.5" strokeLinecap="round"
            className={clsx("shrink-0 transition-transform duration-150", open && "rotate-90")}>
            <polyline points="2 1 6 4 2 7" />
          </svg>
        ) : <span className="w-2 shrink-0" />}

        {isDir ? <DirIcon open={open} /> : <FileIcon name={node.name} status={node.status} />}

        <span className={clsx("flex-1 truncate", node.status === "deleted" ? "text-accent-hover line-through" : "text-accent-hover")}>
          {node.name}
        </span>

        {(totalAdded > 0 || totalRemoved > 0) && (
          <span className="flex items-center gap-1 shrink-0">
            {totalAdded > 0 && <span className="text-caption text-[#00ff88]/70 tabular-nums">+{totalAdded}</span>}
            {totalRemoved > 0 && <span className="text-caption text-[#ff4444]/70 tabular-nums">-{totalRemoved}</span>}
          </span>
        )}

        {node.status && !node.isDir && (
          <span className={clsx(
            "text-caption font-bold uppercase tracking-wider rounded px-1 py-0.5 shrink-0",
            node.status === "added" && "text-[#00ff88]/80 bg-[#00ff88]/10",
            node.status === "modified" && "text-[#ffcc44]/80 bg-[#ffcc44]/10",
            node.status === "deleted" && "text-[#ff4444]/80 bg-[#ff4444]/10",
            node.status === "renamed" && "text-[#88ccff]/80 bg-[#88ccff]/10",
          )}>
            {node.status === "added" ? "A" : node.status === "modified" ? "M" : node.status === "deleted" ? "D" : "R"}
          </span>
        )}
      </div>

      <AnimatePresence>
        {open && isDir && (
          <motion.div initial={{ height: 0, opacity: 0 }} animate={{ height: "auto", opacity: 1 }} exit={{ height: 0, opacity: 0 }} transition={{ duration: 0.15 }} className="overflow-hidden">
            {sorted.map(child => (
              <NodeItem key={child.fullPath} node={child} depth={depth + 1} onFileClick={onFileClick} clickablePaths={clickablePaths} />
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

/* ── Source Badge ── */
// Two states: "live" for content from an active sandbox session (the working
// -tree diff blob, which includes uncommitted edits immediately), and "git"
// for the diff persisted in the DB at teardown. The file list is parsed from
// the same blob the viewer reads, so there's no separate "session" fallback
// state — the tree and the bodies are one source.
type DisplaySource = "diff-live" | "diff-stored" | null;

function SourceBadge({ source }: { source: DisplaySource }) {
  if (!source) return null;

  const config: Record<NonNullable<DisplaySource>, { label: string; className: string }> = {
    "diff-live": {
      label: "live",
      className: "text-[#00ff88]/70 bg-[#00ff88]/10",
    },
    "diff-stored": {
      label: "git",
      className: "text-[#88ccff]/70 bg-[#88ccff]/10",
    },
  };

  const { label, className } = config[source];
  return (
    <span className={clsx("text-caption font-bold rounded px-1 py-0.5 uppercase tracking-wider leading-tight", className)}>
      {label}
    </span>
  );
}

/* ── Empty State ── */
type EmptyReason = "no-run" | "loading" | "unavailable" | "too-large" | "active-no-changes" | "completed-no-changes";

function EmptyState({ reason }: { reason: EmptyReason }) {
  const messages: Record<EmptyReason, string> = {
    "no-run": "Select a run to see file changes",
    loading: "Loading changes\u2026",
    unavailable: "Diff unavailable",
    "too-large": "Diff too large to display — open the PR on GitHub instead",
    "active-no-changes": "No file changes yet",
    "completed-no-changes": "No file changes in this run",
  };

  return (
    <div className="text-meta text-text-dim px-3 py-6 text-center">
      {messages[reason]}
    </div>
  );
}

/* ── Main WorkTree Panel ── */
export interface WorkTreeProps {
  events: FeedEvent[];
  runId: string | null;
  runStatus: RunStatus | null;
}

export function WorkTree({ events, runId, runStatus }: WorkTreeProps) {
  const [diffData, setDiffData] = useState<DiffStats | null>(null);
  const [diffLoading, setDiffLoading] = useState(false);
  // Generation counter: incremented on each new runId mount so stale async
  // fetches from a prior run are discarded when they resolve.
  const diffGenRef = useRef(0);
  // The file LIST (no bodies). repo = git working-tree (tracked+untracked
  // via the sandbox temp-index diff), tmp = /tmp/round-* report files. Both
  // arrive in the SAME {path,status,added,removed,body:null} shape, so they
  // concat into one tree and route through one viewer — no second format.
  const [repoFiles, setRepoFiles] = useState<DiffFile[]>([]);
  const [tmpFiles, setTmpFiles] = useState<DiffFile[]>([]);
  const [selectedFile, setSelectedFile] = useState<{ path: string; status: string } | null>(null);
  // The expanded file's body, fetched on click. {path, body} where body is
  // null for a binary file (server returned no text). Kept separate from the
  // list so a poll refreshing the list never clobbers an open file's body.
  const [expanded, setExpanded] = useState<{ path: string; body: string | null } | null>(null);
  const [expandLoading, setExpandLoading] = useState(false);
  const [expandTooLarge, setExpandTooLarge] = useState(false);
  // True when the expand FETCH failed (network/server error) — distinct from
  // a successful fetch returning a null body, which means the file is binary.
  const [expandError, setExpandError] = useState(false);

  // Refetch the file LISTS (repo + tmp) for the current generation. Bodies
  // are NOT fetched here — only on expand. The `gen` guard discards stale
  // results from a prior run. The source marker drives badge + refresh
  // gating; on failure it falls back to "live" so an early-run 409 keeps the
  // run refreshable instead of stalling.
  const refetchDiff = useCallback((id: string, gen: number): Promise<void> => {
    const lists = Promise.all([
      fetchDiffRepo(id, null).then(d => d.files).catch(() => [] as DiffFile[]),
      fetchDiffTmp(id, null).then(d => d.files).catch(() => [] as DiffFile[]),
    ]).then(([repo, tmp]) => {
      if (gen !== diffGenRef.current) return;
      setRepoFiles(repo);
      setTmpFiles(tmp);
    });
    const marker = fetchRunDiff(id)
      .then(d => { if (gen === diffGenRef.current) setDiffData(d); })
      .catch(err => {
        if (gen !== diffGenRef.current) return;
        console.warn("WorkTree: diff stats fetch failed, enabling refetch retry:", err);
        setDiffData({ source: "live", files: [], total_files: 0, total_added: 0, total_removed: 0 });
      });
    return Promise.all([lists, marker]).then(() => undefined);
  }, []);

  // Initial fetch when the run changes. Resets per-run state, bumps the
  // generation so stale in-flight fetches from the prior run are discarded,
  // then delegates the actual fetch to refetchDiff.
  useEffect(() => {
    if (!runId) {
      setDiffData(null);
      setRepoFiles([]);
      setTmpFiles([]);
      return;
    }
    const gen = ++diffGenRef.current;
    setSelectedFile(null);
    setExpanded(null);
    setDiffLoading(true);
    refetchDiff(runId, gen).finally(() => {
      if (gen === diffGenRef.current) setDiffLoading(false);
    });
    return () => { diffGenRef.current++; };
  }, [runId, refetchDiff]);

  // Fetch the selected file's body (expand). Routes to repo vs tmp by the
  // tmp/ prefix — same endpoint family the list came from, so the path is
  // guaranteed present (the server 404s otherwise, surfaced as an error).
  useEffect(() => {
    if (!runId || selectedFile === null) {
      setExpanded(null);
      setExpandLoading(false);
      setExpandTooLarge(false);
      setExpandError(false);
      return;
    }
    const path = selectedFile.path;
    const gen = diffGenRef.current;
    let cancelled = false;
    setExpanded(null);
    setExpandTooLarge(false);
    setExpandError(false);
    setExpandLoading(true);
    const fetcher = path.startsWith("tmp/") ? fetchDiffTmp : fetchDiffRepo;
    fetcher(runId, path)
      .then(d => {
        if (cancelled || gen !== diffGenRef.current) return;
        const file = d.files.find(f => f.path === path);
        const body = file?.body ?? null;
        if (body !== null && body.length > DIFF_MAX_BYTES) {
          setExpandTooLarge(true);
          setExpanded({ path, body: null });
        } else {
          // A null body here is a genuine binary file (server classified it).
          setExpanded({ path, body });
        }
      })
      .catch(err => {
        if (cancelled || gen !== diffGenRef.current) return;
        // Fetch/server error — NOT a binary file. Flag it distinctly so the
        // viewer shows an error, not a misleading "binary file" message.
        console.warn("WorkTree: expand fetch failed:", err);
        setExpandError(true);
      })
      .finally(() => {
        if (!cancelled && gen === diffGenRef.current) setExpandLoading(false);
      });
    return () => { cancelled = true; };
  }, [runId, selectedFile]);

  // Live changes from event stream. Split tmp/round-N writes off from the
  // rest: those are always new files (correctly 'added'), while other
  // writes are mid-run edits in the working tree (correctly 'modified').
  // This lets the status badges be right during the race window where
  // /diff/tmp hasn't returned yet but the Write event is already in feed.
  const liveChanges = useMemo(() => extractFileChanges(events), [events]);
  const writeChanges = useMemo(() => liveChanges.filter(c => c.action !== "read"), [liveChanges]);

  // Whether the run's diff should keep refreshing. True while the sandbox is
  // live ("live"/"agent"), AND while the run is active but its diff source is
  // not yet ready ("unavailable" from an early-run 409) — otherwise a run
  // selected at startup would never start polling and the diff would stay
  // empty until a page reload. A "stored" (terminal, persisted) diff is final
  // and needs no refresh.
  const runIsActive = runStatus !== null && !TERMINAL_STATUSES.has(runStatus);
  const isRefreshSource =
    diffData?.source === "live" ||
    diffData?.source === "agent" ||
    (runIsActive && diffData?.source === "unavailable");

  // Poll all diff sources so the tree, badge, and click-to-open all stay
  // fresh mid-round as a fallback when no events are arriving.
  useEffect(() => {
    if (!runId || !isRefreshSource) return;
    const id = setInterval(() => {
      refetchDiff(runId, diffGenRef.current);
    }, DIFF_POLL_INTERVAL_MS);
    return () => clearInterval(id);
  }, [runId, isRefreshSource, refetchDiff]);

  // Event-driven refetch: the authoritative git diff is otherwise only
  // refreshed by the 15s poll, so a Write/Edit appears in the file tree
  // (built from SSE events) up to a full poll cycle before its diff body and
  // line counts catch up. Debounce a refetch off the live write count so a
  // burst of edits triggers one refetch shortly after they land, not one per
  // event. This is the fix for "diff doesn't update until reload / round end".
  const liveWriteCount = writeChanges.length;
  useEffect(() => {
    if (!runId || !isRefreshSource || liveWriteCount === 0) return;
    const t = setTimeout(() => {
      refetchDiff(runId, diffGenRef.current);
    }, DIFF_REFETCH_DEBOUNCE_MS);
    return () => clearTimeout(t);
  }, [runId, isRefreshSource, liveWriteCount, refetchDiff]);

  // One unified file list: repo (git working tree) + tmp (round files),
  // both already in the same DiffFile shape from the server. Concatenated
  // into a single tree — no blob parsing, no per-source tree merge. Every
  // node names a path the server's list returned, so a click always
  // resolves (the server 404s on an unknown expand path).
  const allFiles = useMemo(() => [...repoFiles, ...tmpFiles], [repoFiles, tmpFiles]);

  const mergedTree = useMemo(
    () => (allFiles.length > 0 ? buildTreeFromDiff(allFiles) : null),
    [allFiles],
  );

  const hasGitDiff = repoFiles.length > 0;
  // writeChanges (SSE events) still gate the empty-state and refresh, but
  // they no longer feed the clickable tree — a file becomes clickable only
  // once it is in a list the server returned.
  const hasLiveChanges = writeChanges.length > 0;
  const hasTmpFiles = tmpFiles.length > 0;
  const hasContent = hasGitDiff || hasTmpFiles;

  const mergedRoots = useMemo(() => {
    if (!mergedTree) return [];
    return Array.from(mergedTree.children.values())
      .sort((a, b) => a.isDir === b.isDir ? a.name.localeCompare(b.name) : a.isDir ? -1 : 1);
  }, [mergedTree]);

  // Badge: derive directly from diffData.source. "live" and "agent"
  // both mean an active sandbox → green "live"; "stored" → blue "git".
  // No more "session" fallback — worktree diff eliminated the window
  // where we had event-stream content but no git stats.
  const displaySource: DisplaySource = (() => {
    if (!hasContent) return null;
    if (!diffData) return null;
    if (diffData.source === "stored") return "diff-stored";
    return "diff-live";
  })();

  // File count from merged tree
  const headerFileCount = useMemo(() => {
    if (!mergedTree) return 0;
    let count = 0;
    const walk = (n: TreeNode) => { if (!n.isDir) count++; n.children.forEach(walk); };
    mergedTree.children.forEach(walk);
    return count;
  }, [mergedTree]);

  // Stats bar totals, summed from the repo file list so the numbers match
  // the tree exactly (same source). Tmp files are "new file" additions with
  // no removals; they're counted in headerFileCount, not the +/- bar.
  const diffTotals = useMemo(() => ({
    added: repoFiles.reduce((n, f) => n + f.added, 0),
    removed: repoFiles.reduce((n, f) => n + f.removed, 0),
  }), [repoFiles]);
  const showDiffStats = hasGitDiff && (diffTotals.added > 0 || diffTotals.removed > 0);

  // Empty state reason
  const emptyReason: EmptyReason = (() => {
    if (!runId) return "no-run";
    if (diffLoading && !diffData) return "loading";
    if (diffData?.source === "unavailable" && !hasLiveChanges && !hasTmpFiles) return "unavailable";
    const isTerminal = runStatus !== null && TERMINAL_STATUSES.has(runStatus);
    return isTerminal ? "completed-no-changes" : "active-no-changes";
  })();

  // Every tree node was parsed from the blob `diffForPath` returns, so a
  // click is guaranteed to resolve to a patch — there is no separate file
  // list that can name a path the blob lacks. Clickable whenever the tree
  // has content.
  const onFileClick = hasContent
    ? (path: string, status: string) => setSelectedFile({ path, status })
    : null;

  return (
    <div className="flex flex-col bg-sidebar h-full w-full">
      {/* Header */}
      <div className="flex items-center gap-2 px-3 py-2.5 border-b border-border">
        <svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="#888" strokeWidth="1.5" strokeLinecap="round" aria-hidden="true">
          <path d="M6 1v10M6 1L3 4M6 1l3 3" />
          <circle cx="6" cy="11" r="0" /><circle cx="3" cy="6" r="1" /><circle cx="9" cy="8" r="1" />
          <line x1="3" y1="6" x2="6" y2="6" /><line x1="9" y1="8" x2="6" y2="8" />
        </svg>
        <span className="text-body font-bold uppercase tracking-[0.15em] text-text-muted">Changes</span>
        <SourceBadge source={displaySource} />
        {hasContent && (
          <span className="text-meta text-text-dim tabular-nums ml-auto">{headerFileCount} files</span>
        )}
      </div>

      {/* Diff stats bar */}
      {showDiffStats && (
        <div className="flex items-center gap-3 px-3 py-1.5 border-b border-border/60 text-meta text-text-secondary">
          <span>{headerFileCount} files changed</span>
          {diffTotals.added > 0 && <span className="text-[#00ff88]/70">+{diffTotals.added}</span>}
          {diffTotals.removed > 0 && <span className="text-[#ff4444]/70">-{diffTotals.removed}</span>}
        </div>
      )}

      {/* Content */}
      <div className={clsx("flex-1 overflow-y-auto", selectedFile === null && "py-1")}>
        {selectedFile !== null && expanded?.path === selectedFile.path && !expandLoading && !expandTooLarge ? (
          <FileDiffViewer
            body={expanded.body}
            filePath={selectedFile.path}
            fileStatus={selectedFile.status}
            onBack={() => setSelectedFile(null)}
          />
        ) : selectedFile !== null ? (
          /* File selected but its body is still loading — or it is oversize */
          <div>
            <div className="flex items-center gap-2 px-2 py-2 border-b border-border shrink-0">
              <button
                onClick={() => setSelectedFile(null)}
                className="p-2 rounded hover:bg-white/[0.06] transition-colors text-text-dim hover:text-text cursor-pointer min-w-[44px] min-h-[44px] flex items-center justify-center"
                aria-label="Back to file tree"
              >
                <svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round">
                  <polyline points="7 2 3 6 7 10" />
                </svg>
              </button>
              <span className="flex-1 text-content text-accent-hover font-mono truncate" title={selectedFile.path}>
                {selectedFile.path}
              </span>
            </div>
            {expandTooLarge ? (
              <div className="text-meta text-text-dim px-3 py-6 text-center" role="status" aria-label="Diff too large">
                Diff too large to display — open the PR on GitHub instead
              </div>
            ) : expandError ? (
              <div className="text-meta text-[#ff4444]/80 px-3 py-6 text-center" role="status" aria-label="Diff load failed">
                Failed to load this file&apos;s diff — try again
              </div>
            ) : (
              <div className="flex items-center justify-center py-8" role="status" aria-label="Loading diff">
                <div className="h-4 w-4 rounded-full border-2 border-border-subtle border-t-[#00ff88]" style={{ animation: "spin 1s linear infinite" }} />
              </div>
            )}
          </div>
        ) : (
          <>
            {!hasContent && (
              diffLoading && !diffData ? (
                <div className="flex items-center justify-center py-8" role="status" aria-label="Loading changes">
                  <div className="h-4 w-4 rounded-full border-2 border-border-subtle border-t-[#00ff88]" style={{ animation: "spin 1s linear infinite" }} />
                </div>
              ) : (
                <EmptyState reason={emptyReason} />
              )
            )}

            {hasContent && mergedRoots.map(child => (
              <NodeItem key={child.fullPath} node={child} depth={0} onFileClick={onFileClick} clickablePaths={null} />
            ))}
          </>
        )}
      </div>
    </div>
  );
}
