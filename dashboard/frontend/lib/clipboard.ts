/**
 * Clipboard helper that works on both secure and insecure origins.
 *
 * navigator.clipboard is only defined in a secure context (HTTPS or
 * localhost). The dashboard is routinely accessed over http://<HOST_IP>:3400
 * for LAN/mobile use (see MobileAccessPopover), where it is undefined — so a
 * bare navigator.clipboard.writeText throws. Fall back to the legacy
 * execCommand("copy") path there. Returns whether the copy succeeded.
 */
export async function copyText(text: string): Promise<boolean> {
  if (navigator.clipboard) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch {
      // Fall through to the execCommand path (e.g. permissions denied).
    }
  }
  return legacyCopy(text);
}

function legacyCopy(text: string): boolean {
  if (typeof document === "undefined") return false;
  const textarea = document.createElement("textarea");
  textarea.value = text;
  // Keep it out of view and unfocusable to the user.
  textarea.setAttribute("readonly", "");
  textarea.style.position = "fixed";
  textarea.style.opacity = "0";
  textarea.style.pointerEvents = "none";
  document.body.appendChild(textarea);
  textarea.select();
  let ok = false;
  try {
    ok = document.execCommand("copy");
  } catch {
    ok = false;
  }
  document.body.removeChild(textarea);
  return ok;
}
