/** Regression tests for the StartRunModal model→provider cascade. */

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

/** The checked provider label in the segmented Provider control, or null. */
function selectedProvider(): string | null {
  const group = screen.queryByRole("radiogroup", { name: "Provider" });
  if (!group) return null;
  return within(group).getByRole("radio", { checked: true }).textContent;
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
    expect(selectedProvider()).toBe("Anthropic");
    // One available provider => the pill is not clickable (read-only clarity).
    const group = screen.getByRole("radiogroup", { name: "Provider" });
    expect(within(group).getByRole("radio")).toBeDisabled();
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
    expect(screen.getByText(/No API keys/i)).toBeInTheDocument();
    expect(screen.queryByRole("radiogroup", { name: "Provider" })).toBeNull();
    expect(startButton()).toBeDisabled();
  });

  it("cascades A(1)->B(0)->C(1) resetting provider, no stale value in onStart", async () => {
    const { props } = renderModal();
    await openModelSection();

    // A: anthropic auto-selected, start enabled.
    expect(selectedProvider()).toBe("Anthropic");
    expect(startButton()).not.toBeDisabled();

    // B: zero providers — provider clears, start disabled, no control.
    await pickModel("No Keys Model");
    expect(screen.queryByRole("radiogroup", { name: "Provider" })).toBeNull();
    expect(startButton()).toBeDisabled();

    // C: openrouter re-selected, not the stale "anthropic" from A.
    await pickModel("GPT-5.6 Sol");
    expect(selectedProvider()).toBe("OpenRouter");
    expect(startButton()).not.toBeDisabled();

    await userEvent.click(startButton());
    expect((props.onStart as ReturnType<typeof vi.fn>).mock.calls[0][6]).toBe("openrouter");
    expect((props.onStart as ReturnType<typeof vi.fn>).mock.calls[0][5]).toBe("openai/gpt-5.6-sol");
  });
});
