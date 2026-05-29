/**
 * UserPromptCard regression tests.
 *
 * Guards the copy-prompt feature: each user message renders a "Copy prompt"
 * button that writes the prompt text to the clipboard, so users can re-run the
 * same prompt against a different repo.
 */

import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect, vi, beforeEach } from "vitest";
import { UserPromptCard } from "@/components/feed/MessageCards";

describe("UserPromptCard", () => {
  let writeText: ReturnType<typeof vi.fn>;

  beforeEach(() => {
    writeText = vi.fn().mockResolvedValue(undefined);
    Object.defineProperty(navigator, "clipboard", {
      value: { writeText },
      configurable: true,
    });
  });

  it("renders the prompt text", () => {
    render(<UserPromptCard prompt="audit this repo for vulns" ts="2026-05-29T12:00:00Z" />);
    expect(screen.getByText("audit this repo for vulns")).toBeTruthy();
  });

  it("copies the prompt text via the copy button", () => {
    render(<UserPromptCard prompt="audit this repo for vulns" ts="2026-05-29T12:00:00Z" />);

    fireEvent.click(screen.getByRole("button", { name: "Copy prompt" }));

    expect(writeText).toHaveBeenCalledExactlyOnceWith("audit this repo for vulns");
  });
});
