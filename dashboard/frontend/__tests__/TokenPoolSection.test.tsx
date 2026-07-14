/**
 * Tests for TokenPoolSection's per-provider add-token UX. Selecting a provider
 * must switch the token-input placeholder and the help text to that provider's
 * key format/instructions — the OpenRouter path the credential PR adds. The
 * component is fully controlled, so the provider is driven via the newProvider prop.
 */

import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { TokenPoolSection } from "@/components/settings/TokenPoolSection";

const noop = () => {};

function renderWithProvider(provider: string) {
  return render(
    <TokenPoolSection
      tokens={[]}
      newToken=""
      newLabel=""
      newProvider={provider}
      addingToken={false}
      tokenError={null}
      onNewTokenChange={noop}
      onNewLabelChange={noop}
      onNewProviderChange={noop}
      onAddToken={noop}
      onRemoveToken={noop}
      onRenameToken={noop}
    />,
  );
}

describe("TokenPoolSection add-token UX", () => {
  it("shows the Anthropic placeholder and setup-token help by default", () => {
    renderWithProvider("anthropic");
    expect(screen.getByPlaceholderText("sk-ant-oat01-...")).toBeInTheDocument();
    expect(screen.getByText("claude setup-token")).toBeInTheDocument();
  });

  it("switches to the OpenRouter placeholder and openrouter.ai help", () => {
    renderWithProvider("openrouter");
    expect(screen.getByPlaceholderText("sk-or-v1-...")).toBeInTheDocument();
    expect(screen.getByText("openrouter.ai/keys")).toBeInTheDocument();
    // Anthropic-only instruction must not appear for an OpenRouter selection.
    expect(screen.queryByText("claude setup-token")).not.toBeInTheDocument();
  });
});
