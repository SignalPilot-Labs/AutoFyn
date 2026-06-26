"use client";

import { useState, useMemo, useEffect, useCallback, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { clsx } from "clsx";
import type { FeedEvent, RunStatus } from "@/lib/types";
import type { DiffStats } from "@/lib/api";
import { fetchRunDiff, fetchDiffRepo, fetchDiffTmp } from "@/lib/api";
import {
  extractFileChanges,
  buildTreeFromDiff,
  buildTreeFromChanges,
  mergeTrees,
  parseTmpDiffStats,
  parseRepoDiffStats,
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
  // Repo and tmp diffs are separate sources — one is git working-branch-vs-base,
  // the other is sandbox filesystem reads of `/tmp/round-*`. Keeping them as
  // distinct state avoids a combined blob that's awkward to size-cap, parse,
  // and route file-click lookups through.
  const [repoDiff, setRepoDiff] = useState<string | null>(null);
  const [tmpDiff, setTmpDiff] = useState<string | null>(null);
  const [diffTooLarge, setDiffTooLarge] = useState(false);
  const [repoTooLarge, setRepoTooLarge] = useState(false);
  const [tmpTooLarge, setTmpTooLarge] = useState(false);
  const [selectedFile, setSelectedFile] = useState<{ path: string; status: string } | null>(null);

  // Fetch diff bodies (repo + tmp). Called only via refetchDiff so every
  // refresh path fetches stats and bodies together. The `gen` parameter
  // guards against stale results from a prior run overwriting current state.
  const fetchDiffBodies = useCallback((id: string, gen: number): Promise<void> => {
    return Promise.all([
      fetchDiffRepo(id).then(d => d.diff).catch(() => ""),
      fetchDiffTmp(id).then(d => d.diff).catch(() => ""),
    ]).then(([repo, tmp]) => {
      if (gen !== diffGenRef.current) return;
      const repoOversize = repo.length > DIFF_MAX_BYTES;
      const tmpOversize = tmp.length > DIFF_MAX_BYTES;
      const repoSafe = repoOversize ? null : (repo || null);
      const tmpSafe = tmpOversize ? null : (tmp || null);
      setRepoDiff(repoSafe);
      setTmpDiff(tmpSafe);
      setRepoTooLarge(repoOversize);
      setTmpTooLarge(tmpOversize);
      // diffTooLarge: true when at least one source is oversize (for empty-state warning)
      setDiffTooLarge(repoOversize || tmpOversize);
    });
  }, []);

  // Refetch stats + bodies for the current generation. The single fetch path
  // shared by the mount effect, the interval poll, and the event-driven
  // refetch, so all three behave identically. Returns the stats promise so
  // callers can chain loading state. The stats `.catch` sets a "live" sentinel
  // so an early-run failure (sandbox/branch not ready -> 409) keeps the run
  // refreshable instead of stalling on an unavailable source.
  const refetchDiff = useCallback((id: string, gen: number): Promise<void> => {
    // The tree renders from the diff bodies (single source), so the loading
    // gate must await BOTH the source marker and the bodies — otherwise the
    // marker (a fast DB read) resolves first and clears the spinner while the
    // body blob (slow, e.g. GitHub for stored runs) is still in flight,
    // flashing an empty state before the tree appears.
    const bodies = fetchDiffBodies(id, gen);
    const marker = fetchRunDiff(id)
      .then(d => { if (gen === diffGenRef.current) setDiffData(d); })
      .catch(err => {
        if (gen !== diffGenRef.current) return;
        console.warn("WorkTree: diff stats fetch failed, enabling refetch retry:", err);
        setDiffData({ source: "live", files: [], total_files: 0, total_added: 0, total_removed: 0 });
      });
    return Promise.all([bodies, marker]).then(() => undefined);
  }, [fetchDiffBodies]);

  // Initial fetch when the run changes. Resets per-run state, bumps the
  // generation so stale in-flight fetches from the prior run are discarded,
  // then delegates the actual fetch to refetchDiff.
  useEffect(() => {
    if (!runId) {
      setDiffData(null);
      setRepoDiff(null);
      setTmpDiff(null);
      setDiffTooLarge(false);
      setRepoTooLarge(false);
      setTmpTooLarge(false);
      return;
    }
    const gen = ++diffGenRef.current;
    setSelectedFile(null);
    setDiffTooLarge(false);
    setRepoTooLarge(false);
    setTmpTooLarge(false);
    setDiffLoading(true);
    refetchDiff(runId, gen).finally(() => {
      if (gen === diffGenRef.current) setDiffLoading(false);
    });
    return () => { diffGenRef.current++; };
  }, [runId, refetchDiff]);

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

  // Repo diff stats — parsed from the SAME blob the file viewer searches.
  // For stored (terminal) runs the blob comes from GitHub and diffData
  // carries the authoritative DB stats; for live runs the blob is the git
  // working-tree diff and is the single source of truth. Either way, every
  // path here is guaranteed to resolve in `repoDiff` when clicked.
  const repoStats = useMemo(
    () => (repoDiff ? parseRepoDiffStats(repoDiff) : []),
    [repoDiff],
  );

  // Git diff tree, built from the parsed blob stats. Replaces the old
  // separate-endpoint tree so list and body can never drift.
  const diffTree = useMemo(
    () => (repoStats.length > 0 ? buildTreeFromDiff(repoStats) : null),
    [repoStats],
  );

  // Tmp tree: parsed from the dedicated /diff/tmp source — the same blob
  // routed to the file viewer for tmp/ paths, so it too cannot drift.
  const tmpTree = useMemo(() => {
    if (!tmpDiff) return null;
    const tmpChanges = parseTmpDiffStats(tmpDiff);
    if (tmpChanges.length === 0) return null;
    return buildTreeFromChanges(
      tmpChanges.map(c => ({
        path: c.path, action: "edit" as const,
        linesAdded: c.linesAdded, linesRemoved: 0,
        timestamp: "", toolCallId: 0, toolName: "Archive",
      })),
      "added",
    );
  }, [tmpDiff]);

  const hasGitDiff = diffTree !== null;
  // writeChanges (SSE events) still gate the empty-state and refresh, but
  // they no longer feed the clickable tree — a file becomes clickable only
  // once its patch is in a blob we hold.
  const hasLiveChanges = writeChanges.length > 0;
  const hasTmpFiles = tmpTree !== null;
  const hasContent = hasGitDiff || hasTmpFiles;

  // Merged tree: repo diff ⊕ tmp diff. Both sides are derived from the diff
  // blobs the file viewer reads, so every node resolves to a patch. Event-
  // derived files are intentionally excluded — they have no patch body yet.
  const mergedTree = useMemo(() => {
    if (!diffTree && !tmpTree) return null;
    if (!diffTree) return tmpTree;
    if (!tmpTree) return diffTree;
    return mergeTrees(diffTree, tmpTree);
  }, [diffTree, tmpTree]);

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

  // Stats bar totals, summed from the parsed repo blob so the numbers match
  // the tree exactly (same source). Tmp files are "new file" additions with
  // no removals; they're counted in headerFileCount, not the +/- bar.
  const diffTotals = useMemo(() => ({
    added: repoStats.reduce((n, f) => n + f.added, 0),
    removed: repoStats.reduce((n, f) => n + f.removed, 0),
  }), [repoStats]);
  const showDiffStats = hasGitDiff && (diffTotals.added > 0 || diffTotals.removed > 0);

  // Empty state reason
  const emptyReason: EmptyReason = (() => {
    if (!runId) return "no-run";
    if (diffLoading && !diffData) return "loading";
    if (diffTooLarge && !hasLiveChanges && !hasTmpFiles) return "too-large";
    if (diffData?.source === "unavailable" && !hasLiveChanges && !hasTmpFiles) return "unavailable";
    const isTerminal = runStatus !== null && TERMINAL_STATUSES.has(runStatus);
    return isTerminal ? "completed-no-changes" : "active-no-changes";
  })();

  // Each clicked path is backed by one of two diff sources: tmp/round-N
  // files come from the tmp diff, everything else from the repo diff.
  // Pick the right source here so FileDiffViewer is simple.
  const diffForPath = (path: string): string | null =>
    path.startsWith("tmp/") ? tmpDiff : repoDiff;

  // Returns true when the diff source for this path was truncated because
  // it exceeded DIFF_MAX_BYTES — callers should show a "too large" message
  // instead of a loading spinner (the diff will never arrive).
  const isFileSourceTooLarge = (path: string): boolean =>
    path.startsWith("tmp/") ? tmpTooLarge : repoTooLarge;

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
        {selectedFile !== null && diffForPath(selectedFile.path) !== null ? (
          <FileDiffViewer
            fullDiff={diffForPath(selectedFile.path)!}
            filePath={selectedFile.path}
            fileStatus={selectedFile.status}
            onBack={() => setSelectedFile(null)}
          />
        ) : selectedFile !== null ? (
          /* File selected but diff body still loading — or source is oversize */
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
            {isFileSourceTooLarge(selectedFile.path) ? (
              <div className="text-meta text-text-dim px-3 py-6 text-center" role="status" aria-label="Diff too large">
                Diff too large to display — open the PR on GitHub instead
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
