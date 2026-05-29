/**
 * Tests for the model helpers in lib/models.tsx.
 *
 * The model list + metadata now come from /api/models at runtime (single
 * source of truth = db/constants.py). The frontend hardcodes no model list,
 * so these tests cover only the pure helpers: looking a model up by id and
 * resolving the initial selection from a stored choice + backend default.
 *
 * Model ids are exact SDK ids — there is no alias/migration layer.
 */

import { describe, it, expect, beforeEach, afterEach } from "vitest";
import { findModel, resolveInitialModel, saveStoredModel, LOCALSTORAGE_MODEL_KEY } from "@/lib/models";
import type { ModelInfo } from "@/lib/api";

const MODELS: ModelInfo[] = [
  { id: "claude-opus-4-8", label: "Claude Opus 4.8", short: "Opus 4.8", description: "x", context: "1M", tier: "opus" },
  { id: "claude-sonnet-4-6", label: "Claude Sonnet 4.6", short: "Sonnet 4.6", description: "y", context: "1M", tier: "sonnet" },
];

describe("findModel", () => {
  it("returns the matching model by exact id", () => {
    expect(findModel(MODELS, "claude-sonnet-4-6")?.short).toBe("Sonnet 4.6");
  });

  it("returns null for an unknown id (no alias resolution)", () => {
    expect(findModel(MODELS, "opus")).toBeNull();
    expect(findModel(MODELS, "claude-opus-4-6")).toBeNull();
    expect(findModel(MODELS, "gpt-4")).toBeNull();
  });

  it("returns null for null/undefined/empty", () => {
    expect(findModel(MODELS, null)).toBeNull();
    expect(findModel(MODELS, undefined)).toBeNull();
    expect(findModel(MODELS, "")).toBeNull();
  });
});

describe("resolveInitialModel", () => {
  beforeEach(() => {
    localStorage.clear();
  });

  afterEach(() => {
    localStorage.clear();
  });

  it("uses the stored model when it is a known id", () => {
    saveStoredModel("claude-sonnet-4-6");
    expect(resolveInitialModel(MODELS, "claude-opus-4-8")).toBe("claude-sonnet-4-6");
  });

  it("falls back to the backend default when nothing is stored", () => {
    expect(resolveInitialModel(MODELS, "claude-opus-4-8")).toBe("claude-opus-4-8");
  });

  it("falls back to the backend default when the stored id is no longer valid", () => {
    localStorage.setItem(LOCALSTORAGE_MODEL_KEY, "claude-opus-4-5");
    expect(resolveInitialModel(MODELS, "claude-opus-4-8")).toBe("claude-opus-4-8");
  });
});
