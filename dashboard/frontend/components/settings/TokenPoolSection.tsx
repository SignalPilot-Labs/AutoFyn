/**Settings section for Claude token pool management.*/

"use client";

import { useState } from "react";
import { AnimatePresence } from "framer-motion";
import type { PoolToken } from "@/lib/types";
import { TOKEN_LABEL_MAX_LEN, TOKEN_NAME_PLACEHOLDER, CREDENTIAL_PROVIDERS } from "@/lib/constants";
import { Button } from "@/components/ui/Button";
import { Tag } from "@/components/ui/Tag";
import { ListRow } from "@/components/ui/ListRow";
import { IconLock, IconCheck, IconPlus } from "@/components/ui/icons";
import { ProviderSelector } from "@/components/settings/ProviderSelector";

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
          {tokens.length} key{tokens.length !== 1 ? "s" : ""} · round-robin
        </span>
      </div>

      <div className="space-y-1.5 mb-3">
        <AnimatePresence>
          {tokens.map((t) => (
            <ListRow key={t.index} layoutId={String(t.index)} onDelete={() => onRemoveToken(t.index)} deleteTitle="Remove token">
              <IconLock className="text-text-secondary shrink-0" />
              <Tag className="shrink-0">
                {CREDENTIAL_PROVIDERS.find((p) => p.value === t.provider)?.label ?? t.provider}
              </Tag>
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
                  className="flex-1 min-w-0 bg-black/30 border border-border rounded px-3 py-2 text-content text-accent-hover placeholder:text-text-secondary focus-visible:outline-none focus-visible:border-[#00ff88]/30 focus-visible:ring-1 focus-visible:ring-[#00ff88]/40 transition-all"
                  autoComplete="off"
                  spellCheck={false}
                />
              ) : (
                <button
                  onClick={() => { startEdit(t); }}
                  title="Rename token"
                  className={`text-content shrink-0 truncate text-left hover:text-[#00ff88] transition-colors ${t.label ? "text-accent-hover" : "text-text-dim"}`}
                >
                  {t.label ?? TOKEN_NAME_PLACEHOLDER}
                </button>
              )}
              <span className="text-content font-mono text-text-secondary flex-1 min-w-0 truncate">
                {t.masked}
              </span>
              {t.active && (
                <span className="flex items-center gap-1 text-content text-[#00ff88]/60 shrink-0">
                  <IconCheck />
                  Next
                </span>
              )}
            </ListRow>
          ))}
        </AnimatePresence>

        {tokens.length === 0 && (
          <div className="px-2.5 py-3 text-content text-text-secondary text-center">
            No tokens yet
          </div>
        )}
      </div>

      <div className="flex gap-2">
        <ProviderSelector value={newProvider} onChange={onNewProviderChange} />
        <input
          type="text"
          value={newLabel}
          onChange={(e) => { onNewLabelChange(e.target.value); }}
          onKeyDown={(e) => { if (e.key === "Enter") { e.preventDefault(); onAddToken(); } }}
          placeholder="Name (optional)"
          maxLength={TOKEN_LABEL_MAX_LEN}
          className="w-32 bg-black/30 border border-border rounded px-3 py-2 text-content text-accent-hover placeholder:text-text-secondary focus-visible:outline-none focus-visible:border-[#00ff88]/30 focus-visible:ring-1 focus-visible:ring-[#00ff88]/40 transition-all"
          autoComplete="off"
          spellCheck={false}
        />
        <input
          type="password"
          value={newToken}
          onChange={(e) => { onNewTokenChange(e.target.value); }}
          onKeyDown={(e) => { if (e.key === "Enter") { e.preventDefault(); onAddToken(); } }}
          placeholder="sk-ant-oat01-..."
          className="flex-1 bg-black/30 border border-border rounded px-3 py-2 text-content text-accent-hover font-mono placeholder:text-text-secondary focus-visible:outline-none focus-visible:border-[#00ff88]/30 focus-visible:ring-1 focus-visible:ring-[#00ff88]/40 transition-all"
          autoComplete="off"
          spellCheck={false}
        />
        <Button
          variant="success"
          size="md"
          icon={<IconPlus size={10} />}
          onClick={onAddToken}
          disabled={addingToken || !newToken.trim()}
        >
          {addingToken ? "Adding..." : "Add"}
        </Button>
      </div>

      {tokenError && (
        <p className="mt-1.5 text-content text-[#ff4444]">{tokenError}</p>
      )}

      <p className="mt-2 text-content text-text-dim">
        Run <code className="text-[#88ccff] bg-[#88ccff]/[0.06] px-1 py-0.5 rounded">claude setup-token</code> to generate tokens. Multiple keys rotate on rate limit.
      </p>
    </div>
  );
}
