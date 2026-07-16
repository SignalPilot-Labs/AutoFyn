# Build report — geometric-selfsimilar (imo-2026-03), Round 8

**Status: partial** (real increment; the m≥4 residual gap remains open).

## What I closed this round

**Lemma R4 (gap-case m = 3 closure) — FULLY PROVED.** For a residual gap case with exactly
m = 3 distinct pieces p₁ > p₂ > p₃, p₁ ≤ Σ/2, and p₂, p₃ < τ/2 (τ = Σ·2^b/D_b), XY's single R3 cut of
p₁ at offset p₂ creates the parity-invisible pair {p₂, p₂}, leaving effective pieces {p₁ − p₂, p₃}. Since
p₁ ≤ Σ/2 forces p₃ ≥ p₁ − p₂, the actual alternating sum is A(final) = Σ − 2p₁. The gap gives
p₂ + p₃ < τ ⟹ p₁ > Σ(2^b − 1)/D_b, and the EXACT identity D_b − 2(2^b − 1) = 1 (verified b = 1..8) gives
A(final) = Σ − 2p₁ < Σ/D_b strictly. This is an **actual-A potential**, exactly as the potential explorer
outlined — and it checks out perfectly (0 mismatches / 0 violations, 1351 budget-enforced configs).

**Corollary R4.1.** With Case A.A (certified R7: p₁ > Σ/2, and m = 2 distinct is always p₁ > Σ/2), the
gap case is now CLOSED for **all m ≤ 3**. Consequence: the **entire upper bound is rigorous at n = 2**
via the framework (previously Regime C at n = 2 was only by-numeric). This is the concrete headline win.

## What I could NOT close (and why the outline's m≥4 plan is wrong)

The outline/explorer claimed the potential A(final) ≤ Σ − 2p₁ < Σ/D_b extends to m ≥ 4 via an
R3-cascade. **This is false**, and I refuted it with bounded, budget-enforced exact-Fraction tests:

- The bound A(final) ≤ Σ − 2p₁ is itself useless for m ≥ 4: for near-equal distinct pieces p₁ ≈ Σ/m, so
  Σ − 2p₁ ≈ Σ/2 ≫ Σ/D_b. The potential does not control the target.
- Every simple deterministic strategy the outline proposed VIOLATES μ ≤ Σ/D_b on a majority of gap
  configs: greedy "cut largest at second-largest" cascade **18385/29234** (worst ratio 21); recursive
  "R3 at p₂ then recurse" **1314/2000** (worst 27); recursive partial-shadow **1268/2000** (worst 29).
- The reviewer's "Case B" worry was well-placed, but the failure is broader than Case B: NO myopic
  one-step rule works. The R7 SB-obstruction theorem already showed no sum-monotone reduction reaches the
  residual; my R8 tests extend that to the actual-A side.
- By contrast the **true optimal** μ (full bounded DFS over invisible-pair/halving cuts) satisfies
  μ ≤ Σ/D_b with **0 violations** (worst ratio 0.88, m=4,b=3; μ ∈ {0,1} on integer configs). So (SB) is
  almost certainly true — but the optimal first cut is not determined by any greedy/recursive rule; it
  needs lookahead. There is no simple potential to write down.

Honest conclusion: the m ≥ 4 residual gap (only bites at n ≥ 3) is genuinely open. I did not paper over
it; I documented the refutation with the numbers in the approach file (`# R8` section, Verification log,
Open gaps).

## Files written
- `results/imo-2026-03/approaches/geometric-selfsimilar.md` — added R8 to Approaches tried; new `# R8`
  proof section (Lemma R4 full proof, Corollary R4.1 with the n=2 closure, the m≥4 obstruction table);
  updated Current best, Open gaps, Verification log, Promotable lemmas. Status stays `partial`.

## Promotable lemma (for the reviewer to certify)
- **Gap-case m = 3 closure (Lemma R4).** Statement + full proof in the `# R8` section. Proposed file
  `results/imo-2026-03/lemmas/gap-case-m3-closure.md`. Certifiable independently; it composes with the
  already-certified `gap-caseAA-subtract-chain.md` to give Corollary R4.1 (gap closed for all m ≤ 3;
  n = 2 upper bound rigorous).

## Spec concerns
- The round-8 outline/explorer overstated the m≥4 case: it presented "A(final) ≤ Σ − 2p₁ < Σ/D_b in all
  cases" and the R3-cascade as essentially a proof modulo "Case B sub-casework." My bounded tests show
  the potential and all proposed deterministic strategies are decisively wrong for m ≥ 4 (majority
  violations). Future outlines for this gap should NOT reuse the A = Σ − 2p₁ cascade; the true optimal
  needs lookahead. Recommend: either a non-constructive/extremal argument (the extremal-smoothing S1
  route) or a genuinely new potential. This is now a recorded dead-end in the approach file.
- No issue with the certified lemmas I imported (Lemma R1/M0, gap-caseAA, sb-obstruction) — all used
  exactly as stated.
