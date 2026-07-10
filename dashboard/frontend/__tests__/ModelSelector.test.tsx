/**
 * Tests for ModelSelector: the trigger shows the selected model, opening
 * reveals the listbox, legacy-tier models render dimmed and last, and
 * selecting an option calls onChange with the exact id.
 */

import { render, screen, fireEvent, within } from "@testing-library/react";
import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { ModelSelector } from "@/components/ui/ModelSelector";

vi.mock("@/lib/models", async (importOriginal) => {
  const actual = await importOriginal<typeof import("@/lib/models")>();
  return {
    ...actual,
    useModels: () => ({
      models: [
        { id: "claude-fable-5", label: "Claude Fable 5", short: "Fable 5", description: "a", context: "1M context", tier: "opus" },
        { id: "claude-opus-4-8", label: "Claude Opus 4.8", short: "Opus 4.8", description: "b", context: "1M context", tier: "opus" },
        { id: "claude-sonnet-4-6", label: "Claude Sonnet 4.6", short: "Sonnet 4.6", description: "c", context: "1M context", tier: "sonnet" },
        { id: "claude-opus-4-5", label: "Claude Opus 4.5", short: "Opus 4.5", description: "d", context: "200K context", tier: "legacy" },
      ],
      defaultModel: "claude-fable-5",
      loading: false,
    }),
  };
});

describe("ModelSelector", () => {
  beforeEach(() => localStorage.clear());
  afterEach(() => localStorage.clear());

  it("shows the selected model's label on the trigger", () => {
    render(<ModelSelector value="claude-fable-5" onChange={() => {}} />);
    expect(screen.getByLabelText("Model")).toHaveTextContent("Claude Fable 5");
  });

  it("opens the listbox and lists all models", () => {
    render(<ModelSelector value="claude-fable-5" onChange={() => {}} />);
    fireEvent.click(screen.getByLabelText("Model"));
    const listbox = screen.getByRole("listbox");
    expect(within(listbox).getAllByRole("option")).toHaveLength(4);
  });

  it("orders legacy models last", () => {
    render(<ModelSelector value="claude-fable-5" onChange={() => {}} />);
    fireEvent.click(screen.getByLabelText("Model"));
    const options = within(screen.getByRole("listbox")).getAllByRole("option");
    expect(options[options.length - 1]).toHaveTextContent("Claude Opus 4.5");
    expect(options[options.length - 1]).toHaveTextContent("Legacy");
  });

  it("calls onChange with the exact id and persists it when an option is picked", () => {
    const onChange = vi.fn();
    render(<ModelSelector value="claude-fable-5" onChange={onChange} />);
    fireEvent.click(screen.getByLabelText("Model"));
    fireEvent.click(screen.getByText("Claude Sonnet 4.6"));
    expect(onChange).toHaveBeenCalledWith("claude-sonnet-4-6");
    expect(localStorage.getItem("autofyn_model")).toBe("claude-sonnet-4-6");
  });

  it("marks the current value as the selected option", () => {
    render(<ModelSelector value="claude-opus-4-8" onChange={() => {}} />);
    fireEvent.click(screen.getByLabelText("Model"));
    const selectedOption = within(screen.getByRole("listbox"))
      .getAllByRole("option")
      .find((o) => o.getAttribute("aria-selected") === "true");
    expect(selectedOption).toHaveTextContent("Claude Opus 4.8");
  });

  it("does not render provider headers for a single provider", () => {
    render(<ModelSelector value="claude-fable-5" onChange={() => {}} />);
    fireEvent.click(screen.getByLabelText("Model"));
    expect(screen.queryByText("Anthropic")).toBeNull();
  });
});
