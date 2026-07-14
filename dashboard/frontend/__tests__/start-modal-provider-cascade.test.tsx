/**
 * Regression tests for the StartRunModal provider cascade.
 *
 * The modal does cascading selection: pick a model, then a provider from a
 * dropdown filtered to the providers the user holds keys for. These tests pin
 * the delicate state transitions the cascade effect must get right:
 *   - a model with one available provider auto-selects it (read-only select),
 *   - a model with zero providers shows the "add keys" warning and disables
 *     start (provider === "" gates the button),
 *   - switching model A(1) -> B(0) -> C(1) resets provider each time with no
 *     stale value leaking into onStart,
 *   - on open the modal refetches models so a key added in Settings is picked
 *     up without a page reload.
 */

import { render, screen, fireEvent, within } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, it, expect, vi, beforeEach } from "vitest";
import { StartRunModal } from "@/components/controls/StartRunModal";

// Three models exercising the cascade: opus has one provider (anthropic), the
// GPT model has one provider (openrouter), and the "no-keys" model has none.
const MODELS = [
  { id: "claude-opus-4-8", label: "Claude Opus 4.8", short: "Opus 4.8", description: "a", context: "1M context", tier: "opus" },
  { id: "no-keys-model", label: "No Keys Model", short: "NoKeys", description: "b", context: "1M context", tier: "opus" },
  { id: "openai/gpt-5.6-sol", label: "GPT-5.6 Sol", short: "Sol", description: "c", context: "1M context", tier: "opus" },
];

const PROVIDERS_BY_MODEL: Record<string, string[]> = {
  "claude-opus-4-8": ["anthropic"],
  "no-keys-model": [],
  "openai/gpt-5.6-sol": ["openrouter"],
};

const refetch = vi.fn();

vi.mock("@/lib/models", async (importOriginal) => {
  const actual = await importOriginal<typeof import("@/lib/models")>();
  return {
    ...actual,
    useModels: () => ({
      models: MODELS,
      defaultModel: "claude-opus-4-8",
      providersByModel: PROVIDERS_BY_MODEL,
      loading: false,
      refetch,
    }),
  };
});

function renderModal(overrides = {}) {
  const defaults = {
    open: true,
    onClose: vi.fn(),
    onStart: vi.fn(),
    busy: false,
    branches: ["main"],
    defaultBranch: "main",
    activeRepo: null,
  };
  const props = { ...defaults, ...overrides };
  return { ...render(<StartRunModal {...props} />), props };
}

/** Expand the collapsible Model section so the ModelSelector + Provider select render. */
async function openModelSection(): Promise<void> {
  const modelHeader = Array.from(
    document.querySelectorAll<HTMLButtonElement>("button[aria-expanded]"),
  ).find((b) => b.textContent?.includes("Model"));
  await userEvent.click(modelHeader!);
}

/** Pick a model by label through the real ModelSelector listbox. */
async function pickModel(label: string): Promise<void> {
  // The trigger button and the listbox both carry aria-label="Model"; target
  // the trigger by its haspopup role, then pick the option inside the listbox.
  fireEvent.click(screen.getByRole("button", { name: "Model" }));
  const option = within(screen.getByRole("listbox")).getByText(label);
  fireEvent.click(option);
}

function startButton(): HTMLButtonElement {
  return Array.from(document.querySelectorAll("button")).find(
    (b) => b.textContent?.includes("New Run") && !b.textContent?.includes("Starting"),
  ) as HTMLButtonElement;
}

describe("StartRunModal provider cascade", () => {
  beforeEach(() => {
    localStorage.clear();
    refetch.mockClear();
  });

  it("refetches models when the modal opens (picks up a newly-added key)", () => {
    const { rerender, props } = renderModal({ open: false });
    expect(refetch).not.toHaveBeenCalled();
    rerender(<StartRunModal {...props} open={true} />);
    expect(refetch).toHaveBeenCalledOnce();
  });

  it("auto-selects the sole provider and shows it read-only", async () => {
    renderModal();
    await openModelSection();
    const select = screen.getByLabelText<HTMLSelectElement>("Provider");
    expect(select.value).toBe("anthropic");
    // One available provider => the select is disabled (read-only clarity).
    expect(select).toBeDisabled();
  });

  it("passes the auto-selected provider to onStart at position 6", async () => {
    const { props } = renderModal();
    await userEvent.click(startButton());
    expect(props.onStart).toHaveBeenCalledOnce();
    // onStart(prompt, preset, budget, duration, baseBranch, model, provider, ...)
    expect((props.onStart as ReturnType<typeof vi.fn>).mock.calls[0][6]).toBe("anthropic");
  });

  it("shows the no-keys warning and disables start for a zero-provider model", async () => {
    renderModal();
    await openModelSection();
    await pickModel("No Keys Model");
    expect(screen.getByText(/No API keys for this model/i)).toBeInTheDocument();
    expect(screen.queryByLabelText("Provider")).toBeNull();
    expect(startButton()).toBeDisabled();
  });

  it("cascades A(1)->B(0)->C(1) resetting provider, no stale value in onStart", async () => {
    const { props } = renderModal();
    await openModelSection();

    // A: anthropic auto-selected, start enabled.
    expect(screen.getByLabelText<HTMLSelectElement>("Provider").value).toBe("anthropic");
    expect(startButton()).not.toBeDisabled();

    // B: zero providers — provider clears, start disabled, no select.
    await pickModel("No Keys Model");
    expect(screen.queryByLabelText("Provider")).toBeNull();
    expect(startButton()).toBeDisabled();

    // C: single (openrouter) provider — provider re-selects to the new model's
    // provider, NOT the stale "anthropic" from A.
    await pickModel("GPT-5.6 Sol");
    const select = screen.getByLabelText<HTMLSelectElement>("Provider");
    expect(select.value).toBe("openrouter");
    expect(within(select).queryByText(/anthropic/i)).toBeNull();
    expect(startButton()).not.toBeDisabled();

    await userEvent.click(startButton());
    expect((props.onStart as ReturnType<typeof vi.fn>).mock.calls[0][6]).toBe("openrouter");
    expect((props.onStart as ReturnType<typeof vi.fn>).mock.calls[0][5]).toBe("openai/gpt-5.6-sol");
  });
});
