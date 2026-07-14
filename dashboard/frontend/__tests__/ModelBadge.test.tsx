/**
 * Tests for ModelBadge label resolution.
 *
 * A known model_name (exact SDK id, present in /api/models) shows the full
 * label ("Claude Opus 4.8", "GPT-5.6 Sol") — families are mixed, so the short
 * name is ambiguous. An unrecognized legacy model_name falls back to the parsed
 * family ("Claude Opus"/"Claude Sonnet") — never a fabricated version, never the
 * default. No model_name or no recognizable family renders nothing.
 */

import { render } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import { ModelBadge } from "@/components/ui/ModelBadge";

vi.mock("@/lib/models", async (importOriginal) => {
  const actual = await importOriginal<typeof import("@/lib/models")>();
  return {
    ...actual,
    useModels: () => ({
      models: [
        { id: "claude-opus-4-8", label: "Claude Opus 4.8", short: "Opus 4.8", description: "x", context: "1M", tier: "opus" },
        { id: "claude-sonnet-4-6", label: "Claude Sonnet 4.6", short: "Sonnet 4.6", description: "y", context: "1M", tier: "sonnet" },
        { id: "openai/gpt-5.6-sol", label: "GPT-5.6 Sol", short: "Sol", description: "z", context: "1M", tier: "opus" },
      ],
      defaultModel: "claude-opus-4-8",
      providersByModel: {},
      loading: false,
      refetch: () => {},
    }),
  };
});

describe("ModelBadge", () => {
  it("shows the full label for a known Claude model", () => {
    const { container } = render(<ModelBadge modelName="claude-opus-4-8" />);
    expect(container.textContent).toBe("Claude Opus 4.8");
  });

  it("shows the full label for a known GPT model", () => {
    const { container } = render(<ModelBadge modelName="openai/gpt-5.6-sol" />);
    expect(container.textContent).toBe("GPT-5.6 Sol");
  });

  it("falls back to the parsed family for a legacy opus model_name", () => {
    expect(render(<ModelBadge modelName="claude-opus-4-6" />).container.textContent).toBe("Claude Opus");
    expect(render(<ModelBadge modelName="opus" />).container.textContent).toBe("Claude Opus");
    expect(render(<ModelBadge modelName="opus-4-5" />).container.textContent).toBe("Claude Opus");
  });

  it("falls back to Claude Sonnet for a legacy sonnet model_name", () => {
    expect(render(<ModelBadge modelName="sonnet" />).container.textContent).toBe("Claude Sonnet");
  });

  it("renders nothing for an unrecognizable model_name", () => {
    expect(render(<ModelBadge modelName="gpt-4" />).container.textContent).toBe("");
  });

  it("renders nothing when model_name is null or empty", () => {
    expect(render(<ModelBadge modelName={null} />).container.textContent).toBe("");
    expect(render(<ModelBadge modelName="" />).container.textContent).toBe("");
  });
});
