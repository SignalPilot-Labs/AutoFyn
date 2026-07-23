# Proof-builder report — imo-2026-03, slug direct-constructive, Round 7

**Task:** close L2 (stray XY cuts outside R_n) — the sole remaining lower-bound gap.
**Outcome: PARTIAL.** L2 is NOT fully closed. It is reduced, by a rigorous induction, to a
**single residual: the augmented a = 0 closer**. Status of the approach stays `partial`.

## What I proved (new, rigorous, round 7) — §4.4 of the approach file

1. **Reformulation (†).** With F = R_n-fragments (ΣF = 2^n) and G = non-R_n pieces (ΣG = 2^n − 1),
   total D, A = D − 2E, so **A ≥ 1 ⟺ E ≤ ΣG** (even-rank sum ≤ total non-R_n mass). Unifies confined
   and stray; DyadicLower-confined is the s = 0 case.
2. **Augmented vertex reduction.** A is continuous, piecewise-affine on the product-of-simplices
   P = Δ_F × ∏_j Δ_{G,j}; min at an arrangement vertex; stray min = min over finitely many P.
3. **GDL(n)** unifying statement + **induction on n** skeleton. Closed branches feeding the induction:
   - **a = 1, R_{n−1} uncut:** cascade peel of (f_1, 2^{n−1}) → GDL(n−1). Full.
   - **v_1 = 2^{n−1}, v_2 ≤ 2^{n−2}:** A ≥ v_1 − v_2 ≥ 2^{n−2} ≥ 1. Full.
   - **base s = 0:** import DyadicLower-confined. **base n ≤ 2:** finite check.
4. **Count Lemma.** With s ≥ 1 stray cuts, ≥1 non-R_n piece sits at an ODD rank (else 2s ≤ 1). So the
   exact A = 1 interleaving is unreachable off the confined subspace. **Gives A > 0, NOT A ≥ 1** — I
   did not overclaim from it (the reviewer/outliner explicitly flagged this).

## The single residual (honestly open) — §4.4.4

The **augmented a = 0 closer**: no R_n-fragment > 2^{n−1} (all pieces ≤ 2^{n−1}) and not the clean
"v_1 = 2^{n−1}, v_2 ≤ 2^{n−2}" shape. Two sub-shapes (R2: R_{n−1} uncut, v_2 = w_1 ∈ (2^{n−2},2^{n−1});
R1': R_{n−1} cut, v_1 < 2^{n−1}). Both funnel to the DyadicLower Case-2 no-donor/parity closer
**generalised to** (i) donors restricted to a piece's own fixed-sum cut-group (moves cannot transfer
mass between R_n and an intact — a restriction absent in the confined proof), and (ii) the global-min
piece being a **tiny stray sub-piece** (from cutting R_0 = 1) at the bottom odd rank instead of the
intact 1, which breaks the confined "+1 at the bottom" closer. I could not discharge this in the round.

## Why I did not force a full closure (anti-overclaim)

The confined DyadicLower closer relies on: (a) all movable pieces being R_n-fragments (single group),
and (b) the smallest piece being the intact 1 contributing +1. Both fail structurally in the augmented
space. A cheap monotone stray→confined exchange is REFUTED (716/17980 pointwise violations — round-7
explorer), and a peel of (2^{n−1}, w_1) does not reduce the R_n group (ΣF' = 2^n − w_1 > 2^{n−1}), so
the induction stalls exactly at a = 0 — the same wall as confined a = 0, now with two extra
complications. Writing a fake closer would be worse than the honest reduction.

## Verification done (support only)

- Augmented (stray) **min A ≥ 1, 0 violations**, n = 2,3,4,5, incl. CLUSTERED / tie-laden splits
  (per the standing rule to test at clustered vertices). Infimum = 1, attained only as a stray
  sub-piece → 0 (recovering confined interleaving). So A ≥ 1 is TRUE and TIGHT.
- Relaxed (†) with G arbitrary → min A ≈ 0.08 (n=3): dyadic G load-bearing.
- (†) with F unbounded → max(E − ΣG) ≈ 0.43: budget load-bearing.

## Promotable (proposed to reviewer)

Reformulation (†); augmented vertex reduction; Count Lemma; GDL(n) reduction skeleton (as a REDUCTION
lemma, not a full closure). All in §4.4.

## Spec concerns

None new. The answer c(n) = 2^n/(2^{n+1}−1) is unchanged and consistent. L2 residual and upper-bound
U1 (IH q≥5 + B2) remain the two gaps blocking `solved`.

## For next round (outliner)

The lower-bound field has bottomed out on **a = 0** (confined a = 0 was the round-5/6 wall; augmented
a = 0 is the round-7 wall — same clustering/parity obstruction, now with within-group donor restriction
+ tiny-bottom-piece). Recommend either: (a) a targeted closer for the augmented a = 0 Case-2 that
handles cut R_0 via the budget (a cut on R_0 costs an R_n fragment — quantify the trade-off), or
(b) a genuinely different lower-bound framing for a = 0 that avoids the minimiser/parity dance entirely
(the shared-gap-plateau rule may apply: a = 0 has been the lower wall for 3 rounds).
