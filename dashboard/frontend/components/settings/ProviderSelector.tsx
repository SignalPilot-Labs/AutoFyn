/**Compact provider dropdown for the credential add-token form.

Matches the RepoSelector design language (button → animated listbox, active dot,
checkmark). Sized to sit inline with the Name and token inputs.*/

"use client";

import { useState, useRef, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { CREDENTIAL_PROVIDERS } from "@/lib/constants";

interface ProviderSelectorProps {
  value: string;
  onChange: (provider: string) => void;
}

export function ProviderSelector({ value, onChange }: ProviderSelectorProps) {
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  // Close on outside click or ESC — only listen when open
  useEffect(() => {
    if (!open) return;
    const handleClick = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
    };
    const handleKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") setOpen(false);
    };
    document.addEventListener("mousedown", handleClick);
    document.addEventListener("keydown", handleKey);
    return () => {
      document.removeEventListener("mousedown", handleClick);
      document.removeEventListener("keydown", handleKey);
    };
  }, [open]);

  const active = CREDENTIAL_PROVIDERS.find((p) => p.value === value);

  return (
    <div ref={ref} className="relative shrink-0">
      <button
        type="button"
        onClick={() => { setOpen(!open); }}
        aria-haspopup="listbox"
        aria-expanded={open}
        className="flex items-center gap-1.5 w-32 h-full bg-black/30 border border-border rounded px-3 py-2 text-content text-accent-hover hover:bg-white/[0.04] focus-visible:outline-none focus-visible:border-[#00ff88]/30 focus-visible:ring-1 focus-visible:ring-[#00ff88]/40 transition-all"
      >
        <span className="flex-1 min-w-0 truncate text-left">
          {active ? active.label : value}
        </span>
        <svg
          width="8" height="8" viewBox="0 0 8 8" fill="none"
          stroke="currentColor" strokeWidth="1.5"
          className={`text-text-secondary transition-transform ${open ? "rotate-180" : ""}`}
        >
          <polyline points="2 3 4 5 6 3" />
        </svg>
      </button>

      <AnimatePresence>
        {open && (
          <motion.div
            role="listbox"
            initial={{ opacity: 0, y: -4 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -4 }}
            transition={{ duration: 0.15 }}
            className="absolute top-full left-0 mt-1 z-50 w-40 bg-bg-card border border-border rounded-lg shadow-xl shadow-black/50 overflow-hidden"
          >
            {CREDENTIAL_PROVIDERS.map((p) => (
              <button
                key={p.value}
                type="button"
                role="option"
                aria-selected={p.value === value}
                onClick={() => { onChange(p.value); setOpen(false); }}
                className={`w-full flex items-center gap-2 px-3 py-2 text-left hover:bg-white/[0.04] transition-colors ${
                  p.value === value ? "bg-white/[0.02]" : ""
                }`}
              >
                <div
                  className={`w-1.5 h-1.5 rounded-full shrink-0 ${
                    p.value === value ? "bg-[#00ff88]" : "bg-transparent"
                  }`}
                />
                <span className="flex-1 min-w-0 truncate text-content text-accent-hover">
                  {p.label}
                </span>
                {p.value === value && (
                  <svg
                    width="10" height="10" viewBox="0 0 10 10"
                    fill="none" stroke="#00ff88" strokeWidth="1.5"
                  >
                    <polyline points="2 5 4 7 8 3" />
                  </svg>
                )}
              </button>
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
