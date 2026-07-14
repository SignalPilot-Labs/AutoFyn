/**Settings section for Claude token pool management.*/

"use client";

import { useState } from "react";
import { AnimatePresence } from "framer-motion";
import type { PoolToken } from "@/lib/types";
import { TOKEN_LABEL_MAX_LEN, TOKEN_NAME_PLACEHOLDER, TOKEN_PLACEHOLDERS, CREDENTIAL_PROVIDERS } from "@/lib/constants";
import { ListRow } from "@/components/ui/ListRow";
import { IconLock, IconCheck, IconPlus } from "@/components/ui/icons";
import { ProviderSelector } from "@/components/settings/ProviderSelector";

// Shared box styling so the read-only display fields and the editable inputs
// are pixel-identical — the display row mirrors the add-token row.
const FIELD_BOX =
  "bg-black/30 border border-border rounded px-3 py-2 text-content";
const FIELD_FOCUS =
  "placeholder:text-text-secondary focus-visible:outline-none focus-visible:border-[#00ff88]/30 focus-visible:ring-1 focus-visible:ring-[#00ff88]/40 transition-all";
// Inline command/URL chip in the help text — uses the `info` design token
// (globals.css --color-info), shared by both provider branches.
const CODE_CHIP = "text-info bg-info/[0.06] px-1 py-0.5 rounded";

interface TokenPoolSectionProps {
  tokens: PoolToken[];
  newToken: string;
  newLabel: string;
  newProvider: string;
  addingToken: boolean;
  tokenError: string | null;
  onNewTokenChange: (value: string) => void;
  onNewLabelChange: (value: string) => void;
  onNewProviderChange: (value: string) => void;
  onAddToken: () => void;
  onRemoveToken: (index: number) => void;
  onRenameToken: (index: number, label: string | null) => void;
}

export function TokenPoolSection({
  tokens,
  newToken,
  newLabel,
  newProvider,
  addingToken,
  tokenError,
  onNewTokenChange,
  onNewLabelChange,
  onNewProviderChange,
  onAddToken,
  onRemoveToken,
  onRenameToken,
}: TokenPoolSectionProps) {
  const [editingIndex, setEditingIndex] = useState<number | null>(null);
  const [draftLabel, setDraftLabel] = useState("");

  const startEdit = (t: PoolToken) => {
    setEditingIndex(t.index);
    setDraftLabel(t.label ?? "");
  };

  const commitEdit = (index: number) => {
    onRenameToken(index, draftLabel.trim() || null);
    setEditingIndex(null);
  };

  return (
    <div className="p-4 bg-white/[0.01] border border-border rounded-lg">
      <div className="flex items-center justify-between mb-3">
        <label className="text-content font-semibold text-accent-hover">
          Claude Tokens
        </label>
        <span className="text-content text-text-secondary">
          {tokens.length} key{tokens.length !== 1 ? "s" : ""}
        </span>
      </div>

      <div className="space-y-1.5 mb-3">
        <AnimatePresence>
          {tokens.map((t) => (
            <ListRow key={t.index} layoutId={String(t.index)} onDelete={() => onRemoveToken(t.index)} deleteTitle="Remove token">
              <div className={`${FIELD_BOX} w-32 flex items-center gap-1.5 text-text-secondary`}>
                <IconLock className="shrink-0" />
                <span className="truncate">
                  {CREDENTIAL_PROVIDERS.find((p) => p.value === t.provider)?.label ?? t.provider}
                </span>
              </div>
              {editingIndex === t.index ? (
                <input
                  type="text"
                  value={draftLabel}
                  onChange={(e) => { setDraftLabel(e.target.value); }}
                  onBlur={() => { commitEdit(t.index); }}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") { e.preventDefault(); commitEdit(t.index); }
                    if (e.key === "Escape") { e.preventDefault(); setEditingIndex(null); }
                  }}
                  placeholder="Name"
                  maxLength={TOKEN_LABEL_MAX_LEN}
                  autoFocus
                  className={`${FIELD_BOX} ${FIELD_FOCUS} w-32 text-accent-hover`}
                  autoComplete="off"
                  spellCheck={false}
                />
              ) : (
                <button
                  onClick={() => { startEdit(t); }}
                  title="Rename token"
                  className={`${FIELD_BOX} w-32 text-left truncate hover:border-border-hover transition-colors ${t.label ? "text-accent-hover" : "text-text-dim"}`}
                >
                  {t.label ?? TOKEN_NAME_PLACEHOLDER}
                </button>
              )}
              <div className={`${FIELD_BOX} flex-1 min-w-0 flex items-center gap-2 font-mono text-text-secondary`}>
                <span className="flex-1 min-w-0 truncate">{t.masked}</span>
                {t.active && (
                  <span className="flex items-center gap-1 text-[#00ff88]/60 shrink-0">
                    <IconCheck />
                    Next
                  </span>
                )}
              </div>
            </ListRow>
          ))}
        </AnimatePresence>

        {tokens.length === 0 && (
          <div className="px-2.5 py-3 text-content text-text-secondary text-center">
            No tokens yet
          </div>
        )}
      </div>

      <div className="flex items-center gap-2 px-2.5 border border-transparent">
        <ProviderSelector value={newProvider} onChange={onNewProviderChange} />
        <input
          type="text"
          value={newLabel}
          onChange={(e) => { onNewLabelChange(e.target.value); }}
          onKeyDown={(e) => { if (e.key === "Enter") { e.preventDefault(); onAddToken(); } }}
          placeholder="Name (optional)"
          maxLength={TOKEN_LABEL_MAX_LEN}
          className={`${FIELD_BOX} ${FIELD_FOCUS} w-32 text-accent-hover`}
          autoComplete="off"
          spellCheck={false}
        />
        <input
          type="password"
          value={newToken}
          onChange={(e) => { onNewTokenChange(e.target.value); }}
          onKeyDown={(e) => { if (e.key === "Enter") { e.preventDefault(); onAddToken(); } }}
          placeholder={TOKEN_PLACEHOLDERS[newProvider] ?? "Token"}
          className={`${FIELD_BOX} ${FIELD_FOCUS} flex-1 text-accent-hover font-mono`}
          autoComplete="off"
          spellCheck={false}
        />
        <button
          onClick={onAddToken}
          disabled={addingToken || !newToken.trim()}
          title="Add token"
          className="text-text-secondary hover:text-[#00ff88] disabled:opacity-30 disabled:pointer-events-none transition-colors shrink-0"
        >
          <IconPlus size={11} />
        </button>
      </div>

      {tokenError && (
        <p className="mt-1.5 text-content text-[#ff4444]">{tokenError}</p>
      )}

      <p className="mt-2 text-content text-text-dim">
        {newProvider === "openrouter" ? (
          <>
            Generate keys at <code className={CODE_CHIP}>openrouter.ai/keys</code> and link it.
          </>
        ) : (
          <>
            Run <code className={CODE_CHIP}>claude setup-token</code> to generate tokens. Multiple keys rotate on rate limit.
          </>
        )}
      </p>
    </div>
  );
}
