# Proof-builder report — upper-general-cascade (round 6)

**Slug:** upper-general-cascade (copy-of direct-constructive). **Problem:** imo-2026-03.
**Status: partial.** File: `results/imo-2026-03/approaches/upper-general-cascade.md`.

## What I closed (rigorous, certifiable)

1. **Lemma IH-reducible (pure conditional).** For q pieces b_1≥…≥b_q > 1/D, gaps > 1/D, S < (2^q−1)/D:
   if S − max(b_1,2b_2) < (2^{q−1}−1)/D, one cut (halve b_1, or cut b_1 at b_2) drops to a strict
   IH(q−1) instance, or finishes via CaseB-Reduction 2. Uses the identity S − max(b_1,2b_2) =
   min(S−b_1, S−2b_2). No empirical percentage in the statement (fixes the round-5 rejection reason).
   I also handled the subtle gap-preservation point the round-5 draft glossed: after "cut b_1 at b_2"
   the residual b_1−b_2 may violate a gap > 1/D — but then CaseB-Reduction 2 finishes directly. This
   makes the reducible step fully rigorous.

2. **Lemma IH4-flat (proved + exact machine check).** q=4 flat residual (S<15/D, S−max(b_1,2b_2)≥7/D):
   the 3-cut strategy {halve b_1; cut b_2 at b_3; cut b_4 at δ} leaves the 3 singletons
   {b_2−b_3, b_4−δ, δ} with A < 1/D. Derived b_2 < 4/D from the flat condition, then two exhaustive
   cases on sign(b_3+b_4−b_2). Verified exactly on all sampled q=4 flat configs (worst A·D ≈ 0.94,
   0 fails).

3. **Theorem UB.** IH(1), IH(2) [flat residual proven EMPTY], imported IH(3), + IH-reducible +
   IH4-flat ⟹ **IH(q) for all q ≤ 4**, closing the Case-B B1-large upper bound for all n ≤ 4.

## Honest gaps (the genuine open core — NOT closed)

- **IH(q≥5) flat residual (n≥5 B1-large).** I DISPROVED the outline's hope that the strengthened
  dual-bound IH+(m) closes it. **Fixed-point obstruction:** in a flat residual, any single
  pair-cancel move leaves active sum = S − max(b_1,2b_2) ≥ (2^{q−1}−1)/D, i.e. AT OR ABOVE the
  IH(q−1) boundary — never strictly inside. The geometric config is a fixed point of the halve-max
  recursion (maps q-geometric → (q−1)-geometric, A=1/D throughout). The extra max bound
  b_2 < 2^{q−2}/D shrinks one resource but the sum bound does not shrink at all, so IH+(m) stalls at
  every flat level ≥ 5, exactly like the sum-only IH. So IH+(m) is NOT the fix. IH4-flat works only
  because it does not recurse — it collapses to 3 explicit singletons; the q=5 analogue leaves a
  residual ~b_3 too large (b_2<8/D too weak) and no fixed 4-cut works (~50% fail). Min-A cut search
  finds A ≤ 1/D at every hard config (n=3 hard → 18/625 < 1/15; n=4,5 random 0 fails) but the
  strategies are highly adaptive with no closed form — hence no uniform cascade to prove.

- **B2 (a_1 ≤ c(n)).** Sum sits exactly on IH(n+1) boundary. Double-cancel entry (cut a_1 at a_2,
  then residual at a_3) enters strict IH(n−1) iff a_2+a_3 > 2^{n−1}/D; the near-equal-small-pieces
  sub-region stays open. General proof not in hand.

## Assessment for the orchestrator

This is the genuine open core of an IMO P3 upper bound; I did NOT fully close it and did not
overclaim (round-5 lesson). Concrete advances this round: IH4-flat proved (extends the reducible
region into a complete IH(4)); the reducible lemma tightened to a certifiable pure conditional with
the gap-preservation hole plugged; and — importantly — a rigorous **refutation of the IH+(m) route**
the outline proposed (fixed-point obstruction), so next round should NOT re-attempt dual-bound
descent. The two lemmas (IH-reducible, IH4-flat) are recommended for certification.

**Diversity flag (echoing outline-reviewer):** upper-general-cascade and direct-constructive now
share the same pair-creation move-set on the same wall; the IH+(m) differentiator is refuted. If
IH(q≥5) has not moved by round 8, a genuinely different upper-bound framing (different move-set or
target, outside the whole graveyard) is needed — likely a global-extremal / compactness argument
proving the geometric config maximises min-A (naive concavity fails per the r3 graveyard, so it must
handle interior valleys), OR a bounded multi-level-collapse generalising IH4-flat's 3-singleton
trick.

Proof written to results/imo-2026-03/approaches/upper-general-cascade.md (Status: partial)
