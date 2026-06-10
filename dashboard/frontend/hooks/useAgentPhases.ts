"use client";

import { useState, useEffect } from "react";
import { fetchRepoSubagents } from "@/lib/settings-api";
import type { SubagentPhase } from "@/lib/phaseColors";

/** Name→phase map for a run's subagents, sourced from the backend.
 *
 * The backend is the source of truth for which phase each subagent belongs
 * to: GET /repos/{repo}/subagents returns the merged list (shipped + the
 * repo's `.autofyn/subagents.json` overlay), each with a `type` (phase). The
 * run feed uses this to color agent cards — including repo-defined agents the
 * frontend can't know about statically.
 *
 * Returns an empty map when there is no repo or the fetch fails; the feed then
 * falls back to the default color, matching the pre-fetch state.
 */
export function useAgentPhases(repo: string | null): Record<string, SubagentPhase> {
  const [phases, setPhases] = useState<Record<string, SubagentPhase>>({});

  useEffect(() => {
    if (!repo) {
      setPhases({});
      return;
    }
    let cancelled = false;
    fetchRepoSubagents(repo)
      .then((res) => {
        if (cancelled) return;
        const map: Record<string, SubagentPhase> = {};
        for (const agent of res.agents) map[agent.name] = agent.type;
        setPhases(map);
      })
      .catch(() => {
        if (!cancelled) setPhases({});
      });
    return () => {
      cancelled = true;
    };
  }, [repo]);

  return phases;
}
