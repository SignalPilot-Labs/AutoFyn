/**Small inline label chip — the single source of truth for pill/tag styling.

Use this for any short categorical label rendered inline in a row (provider,
model, kind). Do NOT hand-write badge classes (bg-white/[0.04], px-1.5, …) in
components; render a <Tag> so every chip in the app stays identical.*/

"use client";

import { clsx } from "clsx";

interface TagProps {
  children: React.ReactNode;
  /** Optional leading icon (already sized by the caller). */
  icon?: React.ReactNode;
  className?: string;
  "aria-label"?: string;
}

export function Tag({ children, icon, className, ...rest }: TagProps): React.ReactElement {
  return (
    <span
      className={clsx(
        "inline-flex items-center rounded text-caption font-medium leading-tight text-accent-hover bg-white/[0.04]",
        icon ? "gap-1 px-1.5 py-0" : "px-1.5 py-0",
        className,
      )}
      {...rest}
    >
      {icon}
      {children}
    </span>
  );
}
