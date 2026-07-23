# Outline review — imo-2026-03, round 2

## Independent verification of the round-2 mechanism (Lemma P-zero / Case (i) closure)

I re-derived everything by hand with exact `Fraction` arithmetic (scripts run, not trusted
from the outliner's prose) before accepting the outline. Summary of what I checked:

1. **Recursion `e_n = e_{n-1}/(2+e_{n-1})` with `e_n = 1/(2^{n+1}-1)`** — verified exactly
   for n=1..5.
2. **Lemma P-zero (duplicate pair contributes exactly 0 to e=L−X)** — verified on two
   independent concrete multisets (a Case-(i) example and the file's own Case-(ii)
   example): in both cases `e(after XY's move) == e(residual with the duplicate pair
   removed)` exactly, confirmed with exact fractions, not floats.
3. **Case (i) closure (a_1 ≥ 2a_2 ⇒ bisection always creates a top-of-order duplicate pair,
   e(after)=e(residual) exactly, form (B) closes)** — verified on a concrete 4-piece
   example: e(after bisecting a_1)=1/10, e(residual)=1/10, exact match. **This mechanism is
   correct and Case (i) genuinely closes as claimed.**
4. **Case (ii) "naive chain fails" claim** — I independently re-derived *why* it fails,
   via a cleaner route than the outline's worked example: the case-(ii) hypothesis only
   forces `a2/S > 1/(k+1) ≥ 1/(n+2)` (from `a1<2a2` and `a3,…,ak≤a2`), but closing the
   induction via "match a1 to a2, then invoke IH(n−1) on the residual" needs
   `a2/S ≥ 2^{n-1}/(2^{n+1}-1)`. These two bounds coincide at n=1 (both give exactly 1/3)
   but diverge at n=2 (1/4 < 2/7): **the guaranteed lower bound on a2/S is too weak from
   n=2 on.** This confirms the outline's finding independently and pins down exactly where
   the naive chain breaks (a clean one-line reason, useful for the builder to know instead
   of re-deriving the numeric example from scratch).
5. **Random/brute-force stress test at n=2**: brute-forced (fine grid, all 2-cut
   combinatorial patterns, not just "bisect"/"match") XY's true best response over 300
   random 3-piece partitions (152 landed in Case (ii)). **Zero violations of e ≤ e_2=1/7**
   found. This is strong numerical evidence the *theorem* is true at n=2 — the open gap is
   a proof-technique gap, not a wrong conjecture. Good news for confidence in the target.

**New finding to flag to the builder (not previously in the outline):** XY's response
space is *not* fully captured by the outline's two named "elementary moves" (bisect top /
match top-to-second). Brute force found a case ((a1,a2,a3)=(0.5,0.3,0.2), which happens to
satisfy a1=a2+a3) where XY's optimal single cut splits a_1 into two pieces that
simultaneously match a_2 *and* a_3 (creating e=0 immediately, beating both bisect-alone and
match-alone). And in another case ((0.45,0.30,0.25), Case (ii), a1/a2=1.5) bisecting a_1
(even though it lands mid-order, not top-of-order) strictly beats "match a1 to a2" for XY
(e=0.05 vs e=0.10) — confirmed by exact recomputation, not grid noise. Two implications:
  - For the **upper-bound direction** (dyadic-cascade-induction, potential-weighting-
    upper-bound), this is not fatal: the upper bound only needs *some* XY strategy that
    provably achieves e ≤ target for every a in Case (ii) — it does **not** need that
    strategy to be XY's true optimum. "Match a1 to a2" still satisfies the bound in both
    examples I checked (0.10 ≤ 1/7, trivially). The builder should make sure the write-up
    never claims "match is XY's best response" as a load-bearing fact (it's false in
    general) — only "match achieves ≤ target," which is the weaker, sufficient claim.
  - For **elementary-exchange-smoothing**, this matters more: its Step 2/3 explicitly need
    to identify XY's *true* optimal local response pattern (to compute the correct sign of
    the slope of g near a non-dyadic point), not just *a* sufficient one. My finding shows
    the relevant pattern set is richer than the "2 canonical moves" the outline enumerates
    (at least a third family: splitting a_1 to double-match two other pieces
    simultaneously). This makes elementary-exchange-smoothing's gap *harder in kind* than
    dyadic-cascade-induction's, not merely "the same computation reformulated" as the
    outline currently states — flag this to its builder explicitly (see per-approach notes
    below).

## Per-approach verdicts

### dyadic-cascade-induction — APPROVE (build set)
Technique is right (order-statistic reduction + explicit adversary strategy), Lemma
G/Lemma P are standard and correctly justified, Case (i) of the upper-bound induction is
now genuinely closed (verified independently above) with a clean mechanism, not
hand-waved. Case (ii) is a real, correctly-scoped, bounded remaining gap (not a fake gap —
confirmed by my own re-derivation of why the naive chain fails, and by the fact that the
claim itself survives 152 random stress-test samples with zero violations). The n=2-first,
closed-form/Lagrange (not search) ordering is the right way to avoid repeating round 1's
hang: it is a genuinely finite 2-parameter problem.
Additional fix requested: when writing Case (ii), do NOT claim "match a1 to a2" is XY's
optimal response (it provably is not, in general — see finding above); only claim it
achieves the required bound. Also still open and unaddressed in this round's revision:
Step 3 (lower-bound resistance to ALL of XY's responses, not just the cascade) and the
"fewer than full budget never helps" lemma — these are pre-existing gaps, not new.

### elementary-exchange-smoothing — CHANGES REQUESTED (build set)
Technique (extremal smoothing) is legitimate and the ratio-2 crossover is independently
consistent with n=1/n=2 numerics. However the outline's claim that this approach's Step 3
"is governed by the SAME two-level recursion dyadic-cascade-induction is working out" is an
**overstatement** — my finding above shows XY's relevant response-pattern set near a
generic point is richer than the two canonical moves both files assume, and this
approach's Step 2 needs the *true* locally-optimal pattern (not merely a sufficient
strategy), which dyadic-cascade-induction's upper-bound argument does not need. Change
requested: the builder should first check, by hand on the same bounded n=2 case, whether
the "locally constant active pattern" genericity claim (Step 2) still holds once the
richer move set (including "split to double-match two other pieces") is accounted for,
before assuming it reduces cleanly to dyadic-cascade-induction's residual computation.
This is still a bounded, hand-checkable task (2 free parameters) — not a scope increase
into general n — so it does not reopen the round-1 hang risk, but it is a real added item
the current file text does not mention.

### potential-weighting-upper-bound — CHANGES REQUESTED, NOT in build set this round
Math content: correct and consistent with the other two (same Φ=L−X=e, same Lemma P-zero,
Case (i) closes identically). Two problems, independent of the shared math:
1. **Dangling reference**: the file cites `majorization-smoothing-general-optimum.md`
   twice (Step 4 and "Key lemmas") — this slug does not exist in this round's population
   (`.ranking.json` only has 4 entries: concavity-minimax-duality, dyadic-cascade-
   induction, elementary-exchange-smoothing, potential-weighting-upper-bound). Leftover
   name from an earlier draft — remove/replace before this file is next picked up.
2. **Not a self-contained whole attempt.** Per CLAUDE.md, each slug must target the
   problem's actual claim end to end, not "one slice of a proof split across sibling
   slugs." This file explicitly punts its lower-bound/majorization step to
   dyadic-cascade-induction ("not independently open... reduces to the same bookkeeping")
   and its remaining upper-bound gap is now word-for-word the same Case (ii) computation
   as dyadic-cascade-induction. As written, this is no longer a distinct rival approach —
   it is dyadic-cascade-induction's upper-bound argument repackaged as a potential
   function, with its construction direction outsourced entirely. This is not fatal (the
   packaging genuinely differs and could produce a cleaner final write-up once Case (ii)
   is resolved), but it should not consume a separate builder slot this round while the
   identical underlying computation is already being attacked by dyadic-cascade-induction.
   Recommendation: bench it until Case (ii) closes elsewhere, then have this file restate
   the construction/majorization step in its own words (even if the argument ends up
   identical) so it reads as complete on its own.

### concavity-minimax-duality — APPROVE (kept in population, deprioritized, not in build set)
No change in verdict from round 1: sound in principle (Sion's theorem + concave-infimum-
of-affines is standard), but Step 3's "finitely many patterns" and Step 4's stationarity
algebra are both still completely uncarried-out, and my finding above (XY's response
patterns are richer than 2 canonical moves) makes this approach's core finiteness claim
need *more* enumeration work than the outline currently assumes, not less. Correctly kept
lowest priority; not a dead end, just least mature. Not selected for building this round.

## Diversity assessment
Three of four approaches (dyadic-cascade-induction, elementary-exchange-smoothing,
potential-weighting-upper-bound) now share the exact same load-bearing identity (Lemma
P-zero) and the exact same open gap (Case ii). Per CLAUDE.md's shared-gap-trap warning,
this is worth flagging plainly: **if both build-set approaches stall on Case (ii) for
another 1–2 rounds, the fix is not a third repackaging of the same mechanism — it is a
genuinely different framing** (e.g., actually carrying out concavity-minimax-duality's
stationarity algebra with the corrected, richer move-enumeration, or a fresh math-explorer
angle not built on Lemma P-zero at all). This round is not yet at that trigger point since
Case (i) just closed and Case (ii) has a concrete, verified-non-trivial, bounded next step
— but the orchestrator should watch for this next round.

## Registration / ranking
All four approaches were already registered in `.ranking.json` from round 1 (no new slugs
this round — the outliner revised existing files in place, did not open new ones). Ranked
head-to-head this round based on the *revised* outline quality (no build outcomes exist
yet, since round 1's builder hung with no output):
`dyadic-cascade-induction > elementary-exchange-smoothing > potential-weighting-upper-bound
> concavity-minimax-duality` (dyadic wins on: Case (i) now independently verified closed
with the cleanest path to a full write-up; elementary-exchange-smoothing wins over
potential-weighting-upper-bound on: it is a genuinely distinct technique with its own,
harder open question, not a fragment/repackaging of a sibling; potential-weighting-upper-
bound still beats concavity-minimax-duality on: its core mechanism is resolved and
verified, vs. concavity's stationarity algebra being entirely uncarried-out).
`update_ranking` called with all 6 pairwise comparisons across the full field.

## Instruction to this round's builders (both approaches in the build set)

Attack the shared Case (ii) gap (a_1 < 2·a_2) via the ORDERED bounded steps already in the
files — **do not** attempt general-n symbolic algebra or an unbounded/fine-grid numeric
search; that is the confirmed cause of round 1's 909+s hang.

1. First, fully close **n=2 by hand**: 3 pieces (a_1≥a_2≥a_3, sum=1, 2 free parameters
   after normalizing), restricted to the Case (ii) region a_1<2a_2. Use closed-form
   calculus (Lagrange multipliers / boundary analysis over this bounded triangular region),
   not search. Confirm the true max of e (after XY's *best* response, which per my finding
   above may include XY's richer move set — e.g. splitting a_1 to match two other pieces at
   once — not just "bisect" or "match a_1 to a_2") equals exactly e_2=1/7, attained only at
   the dyadic point.
2. Only after n=2 is fully closed by hand, attempt n=3 (4 pieces, 3 free parameters) the
   same way, before generalizing to all n.
3. When writing the upper-bound argument, remember you only need to exhibit **one**
   sufficient XY strategy achieving e ≤ target for every a in Case (ii) — you do **not**
   need to prove that strategy is XY's true optimum (it likely is not, in general; see the
   verification notes above). Do not assert "match a1 to a2 is XY's best response" as a
   lemma.
4. If a builder's bounded n=2 hand computation does not close within reasonable effort,
   stop and report back with the specific obstruction rather than escalating to a bigger
   symbolic or search-based computation.

build set: dyadic-cascade-induction, elementary-exchange-smoothing
