"use client";

import { useModels, findModel } from "@/lib/models";
import { Tag } from "@/components/ui/Tag";

interface ModelBadgeProps {
  /** Raw model_name from the Run (an exact SDK id, e.g. "claude-opus-4-8"). */
  modelName: string | null | undefined;
  /** Show a small model-icon to the left of the label. */
  showIcon?: boolean;
  className?: string;
}

/**
 * Display-only fallback for an unrecognized model_name (e.g. a legacy value
 * from an old run like "claude-opus-4-6" or "opus"). We don't know the exact
 * version, so we show only the family we can read off the string — never a
 * fabricated version and never the default. Returns null if no family is
 * recognizable. This is presentation over historical data, not the selection
 * or validation path, which stay strict on exact ids.
 */
function legacyFamilyLabel(modelName: string): string | null {
  const lower = modelName.toLowerCase();
  if (lower.includes("opus")) return "Opus";
  if (lower.includes("sonnet")) return "Sonnet";
  return null;
}

/**
 * Badge showing a model's short name. Metadata comes from the /api/models
 * source of truth via useModels(). For a known model it shows the short name
 * ("Opus 4.8"); for an unrecognized model_name it falls back to the parsed
 * family ("Opus"/"Sonnet"). Returns null when there is no model_name or no
 * recognizable family.
 */
export function ModelBadge({ modelName, showIcon = false, className }: ModelBadgeProps): React.ReactElement | null {
  const { models } = useModels();
  if (!modelName) return null;
  const model = findModel(models, modelName);
  const label = model ? model.short : legacyFamilyLabel(modelName);
  if (!label) return null;
  return (
    <Tag
      className={className}
      aria-label={`Model: ${label}`}
      icon={showIcon ? (
        <svg width="8" height="8" viewBox="0 0 8 8" fill="none" stroke="currentColor" strokeWidth="1.2" aria-hidden="true">
          <circle cx="4" cy="4" r="3" />
          <path d="M2.5 4h3M4 2.5v3" />
        </svg>
      ) : undefined}
    >
      {label}
    </Tag>
  );
}
