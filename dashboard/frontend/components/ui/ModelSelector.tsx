"use client";

import { useRef } from "react";
import { clsx } from "clsx";
import { useModels, saveStoredModel } from "@/lib/models";

export interface ModelSelectorProps {
  value: string;
  onChange: (id: string) => void;
}

export function ModelSelector({ value, onChange }: ModelSelectorProps): React.ReactElement {
  const { models } = useModels();
  const buttonsRef = useRef<Array<HTMLButtonElement | null>>([]);

  const selectById = (id: string): void => {
    onChange(id);
    saveStoredModel(id);
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLButtonElement>, idx: number): void => {
    if (e.key !== "ArrowRight" && e.key !== "ArrowLeft" && e.key !== "Home" && e.key !== "End") return;
    e.preventDefault();
    const last = models.length - 1;
    let next = idx;
    if (e.key === "ArrowRight") next = idx === last ? 0 : idx + 1;
    else if (e.key === "ArrowLeft") next = idx === 0 ? last : idx - 1;
    else if (e.key === "Home") next = 0;
    else if (e.key === "End") next = last;
    selectById(models[next].id);
    buttonsRef.current[next]?.focus();
  };

  return (
    <div role="radiogroup" aria-label="Model" className="grid grid-cols-3 gap-2">
      {models.map((m, idx) => {
        const selected = value === m.id;
        return (
          <button
            key={m.id}
            ref={(el) => { buttonsRef.current[idx] = el; }}
            type="button"
            role="radio"
            aria-checked={selected}
            tabIndex={selected ? 0 : -1}
            onClick={() => selectById(m.id)}
            onKeyDown={(e) => handleKeyDown(e, idx)}
            className={clsx(
              "text-left p-3 rounded border transition-all focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-[#00ff88]/60",
              selected
                ? "border-[#00ff88]/30 bg-[#00ff88]/[0.04]"
                : "border-border bg-white/[0.01] hover:bg-white/[0.03]"
            )}
          >
            <div
              className={clsx(
                "text-content font-medium leading-tight",
                selected ? "text-text" : "text-accent-hover"
              )}
            >
              {m.label}
            </div>
            <div className="text-body text-text-muted mt-0.5 leading-tight">
              {m.description}
            </div>
            <div
              className={clsx(
                "text-caption mt-1.5 font-mono",
                selected ? "text-[#00ff88]/70" : "text-text-dim"
              )}
            >
              {m.context}
            </div>
          </button>
        );
      })}
    </div>
  );
}
