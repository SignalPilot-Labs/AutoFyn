"use client";

/**
 * Model source of truth for the dashboard.
 *
 * The backend `/api/models` endpoint (db/constants.py SUPPORTED_MODELS) is the
 * single source of truth for the available models and their metadata. The
 * frontend fetches it once at startup via ModelsProvider and exposes it through
 * useModels(). No model list, labels, or badges are hardcoded here — only the
 * localStorage key and the helpers that read/write the user's chosen id.
 *
 * Model ids are exact SDK ids (e.g. "claude-opus-4-8"). No aliases, no
 * migration layer: a stored value is valid only if it appears in the fetched
 * model list.
 */

import { createContext, useContext, useEffect, useState } from "react";
import type { ReactNode } from "react";
import { fetchModels } from "@/lib/api";
import type { ModelInfo } from "@/lib/api";

export const LOCALSTORAGE_MODEL_KEY = "autofyn_model";

interface ModelsContextValue {
  models: ModelInfo[];
  /** Default model id from the backend, or "" until loaded. */
  defaultModel: string;
  loading: boolean;
}

const ModelsContext = createContext<ModelsContextValue>({
  models: [],
  defaultModel: "",
  loading: true,
});

export function ModelsProvider({ children }: { children: ReactNode }): React.ReactElement {
  const [models, setModels] = useState<ModelInfo[]>([]);
  const [defaultModel, setDefaultModel] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    let cancelled = false;
    fetchModels()
      .then((res) => {
        if (cancelled) return;
        setModels(res.models);
        setDefaultModel(res.default);
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, []);

  return (
    <ModelsContext.Provider value={{ models, defaultModel, loading }}>
      {children}
    </ModelsContext.Provider>
  );
}

export function useModels(): ModelsContextValue {
  return useContext(ModelsContext);
}

/** Look up a model's metadata by exact id, or null if not in the list. */
export function findModel(models: ModelInfo[], id: string | null | undefined): ModelInfo | null {
  if (!id) return null;
  return models.find((m) => m.id === id) ?? null;
}

/**
 * Resolve the model to select initially: the user's stored choice if it is a
 * known model, otherwise the backend default. Returns "" until the list loads.
 */
export function resolveInitialModel(models: ModelInfo[], defaultModel: string): string {
  if (typeof window !== "undefined") {
    const stored = localStorage.getItem(LOCALSTORAGE_MODEL_KEY);
    if (stored && models.some((m) => m.id === stored)) return stored;
  }
  return defaultModel;
}

/** Persist the user's chosen model id to localStorage. */
export function saveStoredModel(id: string): void {
  if (typeof window === "undefined") return;
  localStorage.setItem(LOCALSTORAGE_MODEL_KEY, id);
}
