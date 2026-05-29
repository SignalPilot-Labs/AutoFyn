"use client";

import { clsx } from "clsx";
import { useModels, findModel } from "@/lib/models";

interface ModelBadgeProps {
  /** Raw model_name from the Run (an exact SDK id, e.g. "claude-opus-4-8"). */
  modelName: string | null | undefined;
  /** Show a small model-icon to the left of the label. */
  showIcon?: boolean;
  className?: string;
}

/**
 * Badge showing a model's short name. Metadata comes from the /api/models
 * source of truth via useModels(). Returns null if the model is unknown (or
 * not loaded yet) so callers don't need to null-check twice.
 */
export function ModelBadge({ modelName, showIcon = false, className }: ModelBadgeProps): React.ReactElement | null {
  const { models } = useModels();
  const model = findModel(models, modelName);
  if (!model) return null;
  return (
    <span
      className={clsx(
        "inline-flex items-center rounded text-caption font-medium leading-tight text-accent-hover bg-white/[0.04]",
        showIcon ? "gap-1 px-1.5 py-0" : "px-1 py-0",
        className,
      )}
      aria-label={`Model: ${model.short}`}
    >
      {showIcon && (
        <svg width="8" height="8" viewBox="0 0 8 8" fill="none" stroke="currentColor" strokeWidth="1.2" aria-hidden="true">
          <circle cx="4" cy="4" r="3" />
          <path d="M2.5 4h3M4 2.5v3" />
        </svg>
      )}
      {model.short}
    </span>
  );
}
