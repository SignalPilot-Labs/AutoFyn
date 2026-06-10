/**Settings section for enabling/disabling shipped subagents per repo.

Lists the subagents grouped by phase with a checkbox per agent. Checked =
enabled. Toggling saves the disabled list for the active repo. The agent
keeps all subagents when nothing is configured, so an empty disabled list
means "all enabled". At least one agent must stay enabled — the backend
rejects disabling every agent.*/

"use client";

import { useState, useEffect, useCallback } from "react";
import type { SubagentInfo } from "@/lib/types";
import { fetchRepoSubagents, saveRepoSubagents } from "@/lib/settings-api";
import { PHASE_META, SUBAGENT_PHASE_ORDER, hexToRgba } from "@/lib/phaseColors";

interface SubagentSectionProps {
  activeRepo: string;
}

export function SubagentSection({ activeRepo }: SubagentSectionProps) {
  const [agents, setAgents] = useState<SubagentInfo[]>([]);
  const [disabled, setDisabled] = useState<Set<string>>(new Set());
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [saving, setSaving] = useState(false);
  const [expanded, setExpanded] = useState<Set<string>>(new Set());

  useEffect(() => {
    setExpanded(new Set());
    if (!activeRepo) {
      setAgents([]);
      setDisabled(new Set());
      return;
    }
    let cancelled = false;
    setLoading(true);
    setError(null);
    fetchRepoSubagents(activeRepo)
      .then((res) => {
        if (cancelled) return;
        setAgents(res.agents);
        setDisabled(new Set(res.disabled));
        setLoading(false);
      })
      .catch((e) => {
        if (cancelled) return;
        setError(e instanceof Error ? e.message : "Failed to load subagents");
        setLoading(false);
      });
    return () => { cancelled = true; };
  }, [activeRepo]);

  const persist = useCallback(
    async (next: Set<string>) => {
      const previous = disabled;
      setDisabled(next);
      setSaving(true);
      setError(null);
      try {
        await saveRepoSubagents(activeRepo, [...next]);
      } catch (e) {
        setDisabled(previous);
        setError(e instanceof Error ? e.message : "Failed to save");
      } finally {
        setSaving(false);
      }
    },
    [activeRepo, disabled],
  );

  const toggle = (name: string) => {
    const next = new Set(disabled);
    if (next.has(name)) next.delete(name);
    else next.add(name);
    void persist(next);
  };

  const toggleExpand = (name: string) => {
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(name)) next.delete(name);
      else next.add(name);
      return next;
    });
  };

  const enabledCount = agents.length - disabled.size;

  return (
    <div className="p-4 bg-white/[0.01] border border-border rounded-lg">
      <div className="flex items-center justify-between mb-3">
        <label className="text-content font-semibold text-accent-hover">
          Subagents
        </label>
        {activeRepo && agents.length > 0 && (
          <span className="text-content text-text-secondary">
            {enabledCount} of {agents.length} enabled
          </span>
        )}
      </div>

      {!activeRepo && (
        <p className="text-content text-text-secondary">
          Set an active repository to configure its subagents.
        </p>
      )}

      {activeRepo && loading && (
        <p className="text-content text-text-secondary">Loading subagents…</p>
      )}

      {activeRepo && !loading && (
        <div className="space-y-4">
          {SUBAGENT_PHASE_ORDER.map((phase) => {
            const inPhase = agents.filter((a) => a.type === phase);
            if (inPhase.length === 0) return null;
            const meta = PHASE_META[phase];
            return (
              <div key={phase}>
                <div className="flex items-center gap-2 mb-1.5">
                  <span
                    className="w-1.5 h-1.5 rounded-full"
                    style={{ backgroundColor: meta.color }}
                  />
                  <span
                    className="text-content font-medium uppercase tracking-wide"
                    style={{ color: meta.color }}
                  >
                    {meta.label}
                  </span>
                </div>
                <div className="space-y-1">
                  {inPhase.map((agent) => {
                    const isEnabled = !disabled.has(agent.name);
                    const isExpanded = expanded.has(agent.name);
                    return (
                      <div
                        key={agent.name}
                        className="flex items-start gap-2.5 px-2.5 py-2 rounded border border-transparent hover:border-border hover:bg-white/[0.02] transition-colors"
                      >
                        <button
                          type="button"
                          onClick={() => toggle(agent.name)}
                          disabled={saving}
                          aria-label={`${isEnabled ? "Disable" : "Enable"} ${agent.name}`}
                          className="mt-0.5 shrink-0 flex items-center justify-center w-3.5 h-3.5 rounded-sm border transition-colors disabled:opacity-60"
                          style={{
                            borderColor: isEnabled ? meta.color : "var(--border)",
                            backgroundColor: isEnabled ? hexToRgba(meta.color, 0.18) : "transparent",
                          }}
                        >
                          {isEnabled && (
                            <svg width="9" height="9" viewBox="0 0 12 12" fill="none" stroke={meta.color} strokeWidth="2">
                              <polyline points="2 6 5 9 10 3" />
                            </svg>
                          )}
                        </button>
                        <div className="min-w-0 flex-1 text-left">
                          <span className="text-content font-mono text-accent-hover">
                            {agent.name}
                          </span>
                          <span
                            className="ml-1.5 align-middle text-content uppercase tracking-wide px-1 py-0.5 rounded"
                            style={{ color: meta.color, backgroundColor: hexToRgba(meta.color, 0.12) }}
                          >
                            {agent.source === "user" ? "user" : "core"}
                          </span>
                          {isExpanded && (
                            <span className="block text-content text-text-secondary">
                              {agent.description}
                            </span>
                          )}
                          <button
                            type="button"
                            onClick={() => toggleExpand(agent.name)}
                            className="ml-1.5 mt-0.5 text-content text-accent-hover hover:underline cursor-pointer"
                          >
                            {isExpanded ? "less" : "more"}
                          </button>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            );
          })}
        </div>
      )}

      {error && <p className="mt-2 text-content text-[#ff4444]">{error}</p>}
    </div>
  );
}
