"use client";

import { useState, useCallback, useEffect, useRef } from "react";
import { clsx } from "clsx";
import { COPY_FEEDBACK_MS } from "@/lib/constants";
import { copyText } from "@/lib/clipboard";

interface CopyButtonProps {
  /** Text written to the clipboard on click. */
  value: string;
  /** Tooltip + accessible label (e.g. "Copy prompt"). */
  label: string;
  className?: string;
}

/**
 * Icon button that copies `value` to the clipboard and shows a checkmark for
 * COPY_FEEDBACK_MS before reverting to the copy icon. One place for the copy
 * pattern so cards don't re-implement the state/handler/icon-swap each time.
 * Uses copyText so it works on insecure LAN origins too.
 */
export function CopyButton({ value, label, className }: CopyButtonProps): React.ReactElement {
  const [copied, setCopied] = useState(false);
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  // Feed cards unmount as the list scrolls — clear any pending revert timer.
  useEffect(() => () => {
    if (timerRef.current) clearTimeout(timerRef.current);
  }, []);

  const handleCopy = useCallback(() => {
    void copyText(value).then((ok) => {
      if (!ok) return;
      setCopied(true);
      if (timerRef.current) clearTimeout(timerRef.current);
      timerRef.current = setTimeout(() => setCopied(false), COPY_FEEDBACK_MS);
    });
  }, [value]);

  return (
    <button
      type="button"
      onClick={handleCopy}
      title={label}
      aria-label={label}
      className={clsx(
        "p-1 rounded hover:bg-white/[0.04] text-text-secondary hover:text-accent-hover transition-colors",
        className,
      )}
    >
      {copied ? (
        <svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
          <polyline points="2 6 5 9 10 3" />
        </svg>
      ) : (
        <svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
          <rect x="4" y="4" width="7" height="7" rx="1" />
          <path d="M2 8H1.5A1.5 1.5 0 0 1 0 6.5V1.5A1.5 1.5 0 0 1 1.5 0H6.5A1.5 1.5 0 0 1 8 1.5V2" />
        </svg>
      )}
    </button>
  );
}
