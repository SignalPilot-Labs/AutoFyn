"use client";

/** Model picker: a collapsed trigger that opens a listbox of models from
 * /api/models. Legacy-tier models sort last and render dimmed; models are
 * grouped under a provider header (one provider today, more later). */

import { useRef, useState, useEffect, useMemo } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { clsx } from "clsx";
import { useModels, findModel, saveStoredModel } from "@/lib/models";
import type { ModelInfo } from "@/lib/api";

export interface ModelSelectorProps {
  value: string;
  onChange: (id: string) => void;
}

const LEGACY_TIER = "legacy";

/** Display label for a provider group header, keyed on the model's provider. */
const PROVIDER_LABELS: Record<string, string> = {
  anthropic: "Anthropic",
  openrouter: "OpenRouter",
};

/** Provider group header for a model, from its provider field (not id prefix). */
function providerOf(model: ModelInfo): string {
  return PROVIDER_LABELS[model.provider] ?? model.provider;
}

/** Non-legacy models first (in list order), legacy models last. */
function orderModels(models: ModelInfo[]): ModelInfo[] {
  const primary = models.filter((m) => m.tier !== LEGACY_TIER);
  const legacy = models.filter((m) => m.tier === LEGACY_TIER);
  return [...primary, ...legacy];
}

export function ModelSelector({ value, onChange }: ModelSelectorProps): React.ReactElement {
  const { models } = useModels();
  const [open, setOpen] = useState(false);
  const [focusedIndex, setFocusedIndex] = useState(-1);
  const containerRef = useRef<HTMLDivElement>(null);
  const itemRefs = useRef<Array<HTMLButtonElement | null>>([]);

  const ordered = useMemo(() => orderModels(models), [models]);
  const selected = findModel(models, value);

  const selectById = (id: string): void => {
    onChange(id);
    saveStoredModel(id);
    setOpen(false);
  };

  useEffect(() => {
    if (!open) { setFocusedIndex(-1); return; }
    const idx = ordered.findIndex((m) => m.id === value);
    setFocusedIndex(idx >= 0 ? idx : 0);
  }, [open, ordered, value]);

  useEffect(() => {
    if (open && focusedIndex >= 0) itemRefs.current[focusedIndex]?.focus();
  }, [open, focusedIndex]);

  useEffect(() => {
    if (!open) return;
    const handler = (e: MouseEvent): void => {
      if (containerRef.current && !containerRef.current.contains(e.target as Node)) setOpen(false);
    };
    document.addEventListener("mousedown", handler);
    return () => document.removeEventListener("mousedown", handler);
  }, [open]);

  const handleListKeyDown = (e: React.KeyboardEvent): void => {
    const last = ordered.length - 1;
    if (e.key === "ArrowDown") { e.preventDefault(); setFocusedIndex((p) => (p >= last ? 0 : p + 1)); }
    else if (e.key === "ArrowUp") { e.preventDefault(); setFocusedIndex((p) => (p <= 0 ? last : p - 1)); }
    else if (e.key === "Home") { e.preventDefault(); setFocusedIndex(0); }
    else if (e.key === "End") { e.preventDefault(); setFocusedIndex(last); }
    else if (e.key === "Enter" && focusedIndex >= 0) { e.preventDefault(); selectById(ordered[focusedIndex].id); }
    else if (e.key === "Escape") { e.preventDefault(); setOpen(false); }
  };

  let renderedProvider: string | null = null;

  return (
    <div ref={containerRef} className="relative">
      <button
        type="button"
        onClick={() => setOpen((o) => !o)}
        aria-haspopup="listbox"
        aria-expanded={open}
        aria-label="Model"
        className="w-full flex items-center justify-between gap-2 px-3 py-2 bg-black/30 border border-border rounded text-left hover:border-border-hover transition-colors focus-visible:outline-none focus-visible:border-[#00ff88]/30 focus-visible:ring-1 focus-visible:ring-[#00ff88]/40"
      >
        <span className="min-w-0 flex items-baseline gap-2">
          <span className="text-content font-medium text-text truncate">
            {selected ? selected.label : "Select model"}
          </span>
          {selected && (
            <span className="text-caption font-mono text-text-dim shrink-0">{selected.context}</span>
          )}
        </span>
        <svg
          width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="#999" strokeWidth="1.5"
          strokeLinecap="round" className={clsx("shrink-0 transition-transform", open && "rotate-180")}
        >
          <polyline points="2 4 5 6 8 4" />
        </svg>
      </button>

      <AnimatePresence initial={false}>
        {open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.15 }}
            style={{ overflow: "hidden" }}
            className="mt-1 w-full"
          >
            <div
              role="listbox"
              aria-label="Model"
              onKeyDown={handleListKeyDown}
              className="max-h-[190px] overflow-y-auto py-1 bg-bg-elevated border border-border rounded shadow-xl shadow-black/40"
            >
              {ordered.map((m, idx) => {
                const isSelected = m.id === value;
                const isLegacy = m.tier === LEGACY_TIER;
                const provider = providerOf(m);
                const header = provider !== renderedProvider ? provider : null;
                renderedProvider = provider;
                return (
                  <div key={m.id}>
                    {header && (
                      <div className="px-3 pt-2 pb-1 text-caption uppercase tracking-[0.15em] text-text-muted font-semibold">
                        {header}
                      </div>
                    )}
                    <button
                      ref={(el) => { itemRefs.current[idx] = el; }}
                      type="button"
                      role="option"
                      aria-selected={isSelected}
                      tabIndex={-1}
                      onClick={() => selectById(m.id)}
                      className={clsx(
                        "w-full flex items-start gap-2 px-3 py-2 text-left transition-colors focus-visible:outline-none",
                        isSelected
                          ? "bg-[#00ff88]/[0.06]"
                          : "hover:bg-white/[0.03] focus-visible:bg-white/[0.06]"
                      )}
                    >
                      <span className="shrink-0 pt-0.5">
                        {isSelected ? (
                          <svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="#00ff88" strokeWidth="1.5">
                            <polyline points="2 5 4 7 8 3" />
                          </svg>
                        ) : (
                          <span className="block w-[10px]" />
                        )}
                      </span>
                      <span className="min-w-0 flex-1">
                        <span className="flex items-center gap-1.5">
                          <span
                            className={clsx(
                              "text-content font-medium leading-tight",
                              isSelected ? "text-[#00ff88]" : isLegacy ? "text-text-dim" : "text-text"
                            )}
                          >
                            {m.label}
                          </span>
                          {isLegacy && (
                            <span className="text-caption uppercase tracking-wide text-text-dim border border-border rounded px-1 leading-tight">
                              Legacy
                            </span>
                          )}
                        </span>
                        <span className="block text-body text-text-muted mt-0.5 leading-tight">
                          {m.description}
                        </span>
                      </span>
                      <span
                        className={clsx(
                          "shrink-0 text-caption font-mono pt-0.5",
                          isSelected ? "text-[#00ff88]/70" : "text-text-dim"
                        )}
                      >
                        {m.context}
                      </span>
                    </button>
                  </div>
                );
              })}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

