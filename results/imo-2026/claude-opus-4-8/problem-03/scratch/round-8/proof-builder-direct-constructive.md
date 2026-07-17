# Proof-builder report — round 8 — direct-constructive (L2 augmented a=0 closer)

**Status: partial.** The augmented a=0 closer — the sole remaining lower-bound gap — is NOT fully
closed. But I produced new, rigorous, reusable reductions and, crucially, a decisive refutation that
sharpens the residual and kills two tempting bypasses.

## What I proved rigorously this round (§4.4.5 of the approach file)

1. **Sharper reformulation (‡): A ≥ 1 ⟺ E_F ≤ O_G.** From O = O_F+O_G, E = E_F+E_G, ΣG = O_G+E_G, one
   gets E − ΣG = E_F − O_G (tie-break independent), so A = D − 2E ⟹ A ≥ 1 ⟺ (even-rank fragment mass)
   ≤ (odd-rank G mass). This is (†) re-expressed as the exact quantity the interleaving trades.
   Promotable.

2. **All-F-odd sufficiency (B):** E_F = 0 ⟹ A ≥ 1 (= 1 + 2O_G, recovering the explorer identity).
   Immediate from (‡).

3. **Injection / majorisation lemma (C):** if N_F(x) ≤ N_G(x)+1 for all x, then A ≥ 1. Proof: E =
   ∫⌊N/2⌋ ≤ ∫N_G = ΣG (Lemma R), since ⌊(N_F+N_G)/2⌋ ≤ N_G under the hypothesis. Clean layer-cake bound;
   genuinely different from receiver/donor. Promotable. Covers the non-clustered regime.

4. **Minimiser receiver-move (D):** using the tie-valid derivative from DyadicLower-confined, if the
   smallest fragment b_0 has Geq odd (⟺ T − β odd, β = #G-pieces below b_0) then all fragments sit at
   odd ranks ⟹ A ≥ 1. Closes the pure T-odd, no-G-below anchor (the explorer's certified n=3 case).

## The decisive finding (why it is still open — honest)

Exact numerical search (n=3,4,5) shows the **true minimiser has E_F > 0** (a fragment at an *even*
rank — ranks {2,3,5} for n=3,s=1) with **E_F ≈ O_G** (‡ nearly tight). Therefore:
- (B) all-F-odd is FALSE at the minimiser;
- (C) N_F ≤ N_G+1 FAILS at the minimiser (F is clustered);
- in (D) the minimiser lies in the complementary parity T − β even, where the receiver move is
  **tie-blocked** (the increasable fragment is tied to the G-piece directly above it — a vertex of the
  arrangement).

So the minimum lives exactly on the tight clustered face **E_F = O_G**, which is precisely the confined
(2b)/(2c) within-group flat-move obstruction — now with donors restricted to a fixed-sum group and a
possibly-tiny bottom stray sub-piece. **That within-group flat-move termination is not discharged.**

## Spec concerns / guidance for next round

- The outline's suggested routes — T-parity identity A = 1 + 2Σ(G at odd), and the pair-contribution
  comparison A_stray = A_confined + 2t — DO close the anchor cases but do **not** reach the true
  minimiser, which sits at E_F > 0. The reviewer's flag (identity needs all-F-odd, false in general) is
  exactly right and is the wall.
- The residual is genuinely the SAME difficulty as the certified confined Case-2 flat move, ported to
  within-group donors. The correct next step is a **within-group flat-move monovariant on the tight face
  E_F = O_G**, NOT a majorisation bypass (both bypasses provably fail at the minimiser). Recommend the
  outliner frame next round around the tight-face flat move directly, importing the certified confined
  (2c) termination weight and adapting the bottom-piece handling.
- The upper-bound gap (U1) is untouched by this slug (sibling upper-vertex-reduction owns it).

## Lower-bound completeness statement (honest)

The lower bound A ≥ 1 is **NOT yet fully closed**. Confined (s=0) is certified (DyadicLower-confined);
the stray regime's every branch is closed EXCEPT the augmented a=0 tight-face within-group flat move,
which remains open. So L2 (hence the full lower bound) is still partial.

## Promotable lemmas
- Reformulation (‡): A ≥ 1 ⟺ E_F ≤ O_G (tie-robust). Proved §4.4.5(A).
- Injection/majorisation lemma: N_F ≤ N_G+1 ⟹ A ≥ 1. Proved §4.4.5(C).

Numerics: no violations of A ≥ 1 over thousands of stray a=0 configs each for n=3,4,5, all s;
min A → 1 as stray sub-piece → 0 (tight), consistent with the certified infimum.

Proof written to results/imo-2026-03/approaches/direct-constructive.md (Status: partial).
