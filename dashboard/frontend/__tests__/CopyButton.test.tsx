/**
 * CopyButton component tests.
 *
 * Covers: writes the given value to the clipboard on click, swaps to a
 * checkmark for COPY_FEEDBACK_MS then reverts, and exposes the label as
 * title + aria-label.
 */

import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { CopyButton } from "@/components/ui/CopyButton";
import { COPY_FEEDBACK_MS } from "@/lib/constants";

function mockClipboard(): ReturnType<typeof vi.fn> {
  const writeText = vi.fn().mockResolvedValue(undefined);
  Object.defineProperty(navigator, "clipboard", {
    value: { writeText },
    configurable: true,
  });
  return writeText;
}

describe("CopyButton", () => {
  let writeText: ReturnType<typeof vi.fn>;

  beforeEach(() => {
    writeText = mockClipboard();
  });

  afterEach(() => {
    vi.restoreAllMocks();
    vi.useRealTimers();
  });

  it("uses the label for title and aria-label", () => {
    render(<CopyButton value="hello" label="Copy prompt" />);
    const btn = screen.getByRole("button", { name: "Copy prompt" });
    expect(btn.getAttribute("title")).toBe("Copy prompt");
  });

  it("writes the value to the clipboard on click", () => {
    render(<CopyButton value="reuse this prompt" label="Copy prompt" />);

    fireEvent.click(screen.getByRole("button", { name: "Copy prompt" }));

    expect(writeText).toHaveBeenCalledExactlyOnceWith("reuse this prompt");
  });

  it("shows a checkmark after copy then reverts after COPY_FEEDBACK_MS", async () => {
    const { container } = render(<CopyButton value="x" label="Copy prompt" />);

    // Copy icon (rect) is shown before clicking.
    expect(container.querySelector("rect")).toBeTruthy();
    expect(container.querySelector("polyline")).toBeNull();

    fireEvent.click(screen.getByRole("button", { name: "Copy prompt" }));

    // Checkmark (polyline) replaces the copy icon once writeText resolves.
    await waitFor(() => expect(container.querySelector("polyline")).toBeTruthy());
    expect(container.querySelector("rect")).toBeNull();

    // After the feedback window it reverts to the copy icon.
    await waitFor(() => expect(container.querySelector("rect")).toBeTruthy(), {
      timeout: COPY_FEEDBACK_MS + 500,
    });
    expect(container.querySelector("polyline")).toBeNull();
  });
});
