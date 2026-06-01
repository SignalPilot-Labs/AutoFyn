/**
 * Tests for copyText — the secure/insecure-origin clipboard helper.
 *
 * Secure context: uses navigator.clipboard.writeText. Insecure context
 * (navigator.clipboard undefined, as on http://<LAN-IP>) or a rejected
 * writeText: falls back to document.execCommand("copy"). Returns whether the
 * copy succeeded.
 */

import { describe, it, expect, vi, afterEach } from "vitest";
import { copyText } from "@/lib/clipboard";

function setClipboard(value: { writeText: ReturnType<typeof vi.fn> } | undefined): void {
  Object.defineProperty(navigator, "clipboard", { value, configurable: true });
}

// jsdom has no execCommand; install a stub we can assert on.
function stubExecCommand(result: boolean): ReturnType<typeof vi.fn> {
  const exec = vi.fn().mockReturnValue(result);
  Object.defineProperty(document, "execCommand", { value: exec, configurable: true });
  return exec;
}

describe("copyText", () => {
  afterEach(() => {
    vi.restoreAllMocks();
    setClipboard(undefined);
  });

  it("uses navigator.clipboard when available", async () => {
    const writeText = vi.fn().mockResolvedValue(undefined);
    setClipboard({ writeText });

    const ok = await copyText("hello");

    expect(ok).toBe(true);
    expect(writeText).toHaveBeenCalledExactlyOnceWith("hello");
  });

  it("falls back to execCommand on an insecure origin (no navigator.clipboard)", async () => {
    setClipboard(undefined);
    const exec = stubExecCommand(true);

    const ok = await copyText("lan copy");

    expect(ok).toBe(true);
    expect(exec).toHaveBeenCalledWith("copy");
  });

  it("falls back to execCommand when navigator.clipboard.writeText rejects", async () => {
    const writeText = vi.fn().mockRejectedValue(new Error("denied"));
    setClipboard({ writeText });
    const exec = stubExecCommand(true);

    const ok = await copyText("denied then fallback");

    expect(writeText).toHaveBeenCalledOnce();
    expect(exec).toHaveBeenCalledWith("copy");
    expect(ok).toBe(true);
  });

  it("returns false when both paths fail", async () => {
    setClipboard(undefined);
    stubExecCommand(false);

    expect(await copyText("nope")).toBe(false);
  });

  it("removes the temporary textarea after copying", async () => {
    setClipboard(undefined);
    stubExecCommand(true);

    await copyText("cleanup");

    expect(document.querySelector("textarea")).toBeNull();
  });
});
