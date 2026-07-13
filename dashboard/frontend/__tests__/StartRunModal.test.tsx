/**
 * StartRunModal component tests.
 *
 * Covers: opening/closing, model selector, busy state,
 * collapsed sections, expand behavior, and onStart callback wiring.
 */

import { render } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, it, expect, vi, beforeEach } from "vitest";
import { StartRunModal } from "@/components/controls/StartRunModal";
import { STARTER_PRESETS, STARTER_PRESET_KEYS } from "@/lib/constants";

// The modal reads its model list from useModels() (sourced at runtime from
// /api/models). Provide a fixed list so renders are deterministic without a
// live ModelsProvider fetch; keep the real helpers (findModel, etc.).
vi.mock("@/lib/models", async (importOriginal) => {
  const actual = await importOriginal<typeof import("@/lib/models")>();
  return {
    ...actual,
    useModels: () => ({
      models: [
        { id: "claude-opus-4-8", api_model: "claude-opus-4-8", label: "Claude Opus 4.8", short: "Opus 4.8", description: "Most capable", context: "1M context", tier: "opus", provider: "anthropic" },
        { id: "claude-sonnet-4-6", api_model: "claude-sonnet-4-6", label: "Claude Sonnet 4.6", short: "Sonnet 4.6", description: "Fast", context: "1M context", tier: "sonnet", provider: "anthropic" },
      ],
      defaultModel: "claude-opus-4-8",
      loading: false,
    }),
  };
});

function renderModal(overrides = {}) {
  const defaults = {
    open: true,
    onClose: vi.fn(),
    onStart: vi.fn(),
    busy: false,
    branches: ["main", "staging", "develop"],
    defaultBranch: "main",
    activeRepo: null,
  };
  const props = { ...defaults, ...overrides };
  return { ...render(<StartRunModal {...props} />), props };
}

describe("StartRunModal", () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it("renders modal content when open", () => {
    renderModal();
    expect(document.body.textContent).toContain("New Run");
  });

  it("does not render when closed", () => {
    renderModal({ open: false });
    expect(document.body.textContent).not.toContain("Security hardening");
  });

  it("shows model selector with model options", () => {
    renderModal();
    // "Model" label appears in CollapsibleSection header
    expect(document.body.textContent).toContain("Model");
    // Summary text includes model label when collapsed
    expect(document.body.textContent).toContain("Claude Opus 4.8");
  });

  it("shows branch selector with main", () => {
    renderModal();
    expect(document.body.textContent).toContain("main");
  });

  // Regression: older repos default to "master", not "main". The modal must
  // preselect the repo's actual default branch, never a hardcoded "main".
  it("preselects the repo's default branch when it is not main", () => {
    renderModal({ branches: ["master", "feature"], defaultBranch: "master" });
    const trigger = document.querySelector<HTMLButtonElement>(
      'button[aria-haspopup="listbox"]',
    );
    expect(trigger?.textContent?.trim()).toBe("master");
  });

  it("passes the default branch to onStart when unchanged", async () => {
    const { props } = renderModal({
      branches: ["master", "feature"],
      defaultBranch: "master",
    });
    const startBtn = Array.from(document.querySelectorAll("button")).find(
      (b) => b.textContent?.trim() === "New Run",
    );
    if (startBtn) await userEvent.click(startBtn);
    // baseBranch is the 5th positional arg of onStart.
    expect(props.onStart).toHaveBeenCalledOnce();
    expect((props.onStart as ReturnType<typeof vi.fn>).mock.calls[0][4]).toBe(
      "master",
    );
  });

  it("shows quick start options", () => {
    renderModal();
    expect(document.body.textContent).toContain("Quick Start");
  });

  it("disables when busy", () => {
    renderModal({ busy: true });
    expect(document.body.textContent).toContain("Starting...");
  });

  it("calls onStart when start button clicked", async () => {
    const { props } = renderModal();
    const buttons = document.querySelectorAll("button");
    const startBtn = Array.from(buttons).find(
      (b) => b.textContent?.includes("New Run") && !b.textContent?.includes("Starting")
    );
    if (startBtn) {
      await userEvent.click(startBtn);
      expect(props.onStart).toHaveBeenCalledOnce();
    }
  });

  it("collapsed sections show summaries", () => {
    renderModal();
    // Budget section shows "Unlimited" when collapsed and budget is disabled
    expect(document.body.textContent).toContain("Unlimited");
    // Model section summary includes model name when collapsed
    expect(document.body.textContent).toContain("Claude Opus 4.8");
    // Env section summary shows "No vars" when empty
    expect(document.body.textContent).toContain("No vars");
  });

  it("collapsed sections show host mounts summary", () => {
    renderModal();
    expect(document.body.textContent).toContain("Host Mounts");
    expect(document.body.textContent).toContain("None");
  });

  it("expanding host mounts shows add button", async () => {
    renderModal();
    const collapsibleButtons = Array.from(
      document.querySelectorAll<HTMLButtonElement>("button[aria-expanded]")
    );
    const mountsButton = collapsibleButtons.find((b) =>
      b.textContent?.includes("Host Mounts")
    );
    expect(mountsButton).toBeDefined();
    if (mountsButton) {
      await userEvent.click(mountsButton);
    }
    expect(document.body.textContent).toContain("Add Mount");
  });

  it("expanding a section reveals its content", async () => {
    renderModal();

    // Model section header button — find by aria-expanded=false and containing "Model"
    const collapsibleButtons = Array.from(
      document.querySelectorAll<HTMLButtonElement>("button[aria-expanded]")
    );
    const modelButton = collapsibleButtons.find((b) =>
      b.textContent?.includes("Model")
    );
    expect(modelButton).toBeDefined();

    // Before clicking: the ModelSelector trigger should not be visible
    expect(
      document.body.querySelector('[aria-haspopup="listbox"][aria-label="Model"]')
    ).toBeNull();

    if (modelButton) {
      await userEvent.click(modelButton);
    }

    // After clicking: the ModelSelector trigger should now appear
    expect(
      document.body.querySelector('[aria-haspopup="listbox"][aria-label="Model"]')
    ).not.toBeNull();
  });
});

/* ── Starter preset regression tests ── */

describe("StartRunModal starter presets", () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it("renders all preset labels from STARTER_PRESETS", () => {
    renderModal();
    for (const key of STARTER_PRESET_KEYS) {
      expect(document.body.textContent).toContain(STARTER_PRESETS[key].label);
    }
  });

  it("clicking a preset then starting sends preset key, not prompt", async () => {
    const { props } = renderModal();
    // Click the first preset (security_hardening)
    const presetBtn = Array.from(document.querySelectorAll("button")).find(
      (b) => b.textContent?.includes(STARTER_PRESETS.security_hardening.label),
    );
    expect(presetBtn).toBeDefined();
    await userEvent.click(presetBtn!);

    const startBtn = Array.from(document.querySelectorAll("button")).find(
      (b) => b.textContent?.includes("New Run") && !b.textContent?.includes("Starting"),
    );
    await userEvent.click(startBtn!);

    expect(props.onStart).toHaveBeenCalledOnce();
    const [prompt, preset] = props.onStart.mock.calls[0];
    expect(prompt).toBeUndefined();
    expect(preset).toBe("security_hardening");
  });

  it("typing custom prompt then starting sends prompt, not preset", async () => {
    const { props } = renderModal();
    const textarea = document.querySelector("textarea")!;
    await userEvent.type(textarea, "optimize latency");

    const startBtn = Array.from(document.querySelectorAll("button")).find(
      (b) => b.textContent?.includes("New Run") && !b.textContent?.includes("Starting"),
    );
    await userEvent.click(startBtn!);

    expect(props.onStart).toHaveBeenCalledOnce();
    const [prompt, preset] = props.onStart.mock.calls[0];
    expect(prompt).toBe("optimize latency");
    expect(preset).toBeUndefined();
  });

  it("selecting a preset then typing custom text deselects the preset", async () => {
    const { props } = renderModal();
    // Click a preset
    const presetBtn = Array.from(document.querySelectorAll("button")).find(
      (b) => b.textContent?.includes(STARTER_PRESETS.bug_bash.label),
    );
    await userEvent.click(presetBtn!);

    // Type in custom prompt — should deselect preset
    const textarea = document.querySelector("textarea")!;
    await userEvent.type(textarea, "custom task");

    const startBtn = Array.from(document.querySelectorAll("button")).find(
      (b) => b.textContent?.includes("New Run") && !b.textContent?.includes("Starting"),
    );
    await userEvent.click(startBtn!);

    const [prompt, preset] = props.onStart.mock.calls[0];
    expect(prompt).toBe("custom task");
    expect(preset).toBeUndefined();
  });

  it("every preset key in STARTER_PRESET_KEYS is a non-empty string", () => {
    for (const key of STARTER_PRESET_KEYS) {
      expect(typeof key).toBe("string");
      expect(key.length).toBeGreaterThan(0);
    }
  });
});
