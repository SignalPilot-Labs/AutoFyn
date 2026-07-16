# Build report — geometric-selfsimilar (Round 7)

Status: **partial** (upper bound reduced further; single residual gap remains open, now with a rigorous
obstruction pinning down why).

## What was proved this round (rigorous, complete)

1. **Case A.A closure — gap case with p₁ > Σ/2.** Subtract-all chain: cut p₁ successively at p₂,…,p_m
   (m−1 ≤ b cuts by the budget invariant |X| ≤ b+1), doubling every non-p₁ piece (parity-invisible),
   leaving the single leftover L_m = 2p₁ − Σ > 0. So A(final) = 2p₁ − Σ. With the exact threshold
   identity 2τ − Σ = Σ/D_b and p₁ < τ, we get A = 2p₁ − Σ < Σ/D_b **strictly**. No induction. Closes the
   gap-case window p₁ ∈ (Σ/2, τ). Verified 0 anomalies / 3000.

2. **SB-obstruction theorem** (rigorous negative result). For a pairing step at piece q,
   Σ'/D_{b−1} ≤ Σ/D_b ⟺ q ≥ τ/2 (exact, one-line from D_b − D_{b−1} = 2^b). Corollary: in a gap case
   every piece q ≤ p₂ < τ/2, so EVERY parity-invisible pairing step strictly breaks the SB invariant.
   This proves the round-6 recorded dead-end rigorously and, crucially, **refutes the gap-step-then-R3
   route as an SB-chaining**: after the gap-step, R3's own bound Σ'/D_{b−1} already exceeds the target
   Σ/D_b. Verified 0 anomalies / 20000.

## What remains open (honest)

- **Residual gap case p₁ ≤ Σ/2** (the bulk). The SB-obstruction shows no SB-monotone reduction reaches
  it; closing it needs a potential that tracks the ACTUAL alternating sum A through the multi-step
  recursion, not the running sum. Numerically (SB) is comfortably true there (n=3 denom-30 residual gap
  cases: actual μ·D_b ≤ 1/2, half the target), but no proof.

## Correction to the outline's proposed mechanism

The outliner/explorer proposed "gap-step then R3" (25/28 numeric support). This round I proved it CANNOT
work as an SB-chaining: the gap-step at any q < τ/2 makes Σ'/D_{b−1} > Σ/D_b, so R3's post-step
guarantee already overshoots the target. The 25/28 numeric success is the ACTUAL optimal strategy
reaching the bound, not the SB bound propagating — so the "then-R3" needs actual-A tracking, which R3
does not provide. This is a genuine sharpening: the gap is not a matter of finding the right adaptive
pairing j, but of finding a stronger potential.

## Proposed lemma files for certification

- `lemmas/gap-caseAA-subtract-chain.md` — Case A.A closure (p₁ > Σ/2 ⇒ μ ≤ 2p₁ − Σ < Σ/D_b).
- `lemmas/sb-obstruction.md` — Σ'/D_{b−1} ≤ Σ/D_b ⟺ q ≥ τ/2; hence gap-case blocks every SB-monotone step.

Both are short, self-contained, fully proved above, and verified numerically (bounded, exact Fractions).

## Spec concerns:
