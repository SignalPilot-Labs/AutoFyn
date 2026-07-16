# Outline Review — imo-2026-03 (Round 5)

Answer c(n)=2^n/(2^{n+1}−1) confirmed. LB complete except LL t≥2 A(Q)>0 (3-round plateau).
UB complete except Regimes B/C. Field: 1 advance (geometric-selfsimilar Regime B), 2 new LL
bypass/frontal slugs (mandated plateau break), 1 revise long-shot (extremal-smoothing quasiconcavity).

I re-verified every load-bearing new claim numerically (fractions, exact) before ranking:
- INC-GAP (S_Q⊆S_R ⇒ A(R)≥A(Q)+1), n=3 valid-cut grid: **15 containment configs, 0 violations.**
- Case-1 disjointness (max(Q)≥2^{n−1}+1 ⇒ A(Q∪R)≥b≥1), n=3: **540 configs, 0 violations, minA=1.**
- Regime B n=2 XY strategy (B1 one-cut / B2 paired-cut): **worst LB share 0.5667 ≤ 4/7=0.5714** over a 30×30 grid — both sub-strategies hold.

---

## geometric-selfsimilar — APPROVE (advance; BUILD)
Technique sound and the round's most concrete deliverable. Regime B mechanism verified: B1 (A_1≥1−c(n))
gives val=1−A_1≤c(n) via the explicit sorted order; B2 (A_1<1−c(n)) uses a paired A_m/2 cut (A-invisible)
plus an ε-cancelling cut of A_1, val=A_1+A_m/2. Both hold numerically at n=2 (worst 0.5667≤4/7).
Not through any recorded dead-end (this is shadow-regime casework, not concentrate-on-A_1, not greedy-XY).
Issues to close while building (do not hand-wave):
- The B2 overlap B=0 claim: prove the ε-cancellation exactly (the outliner's own "watch out" — the two
  small S-intervals of the paired cut touch only [0,ε), and A_2>ε keeps them clear of the upper S-interval).
  My ε=1/1000 probe held, but the builder must show it as an identity, not a numeric coincidence.
- General-n B1 sorted-order casework for m>3 pieces (placing A_1−A_2 relative to A_3,…,A_m).
- General-n B2 recursion + the algebra A_1+A_m/2≤c(n) at general m.
- Regime C (A_1>c(n)) is explicitly NOT this round's target — fine, leave open.

## ll-dyadic-symdiff — APPROVE (new; register; BUILD) — mandated LL bypass
Whole attempt at c(n) importing the certified lemmas; distinctive route = direct bound on
measure(S_Q△S_R), never using the a/b merge decomposition (recorded dead-end) or the peel-one-Q-cut
induction (recorded circular). Three-way split is exhaustive: Case 1 (max(Q)≥2^{n−1}+1, verified above),
Case 2 (odd count, pieces≥1 → certified Lemma P), Case 3 residual. Sub-3a parity move at x=1 is a valid
mechanism, not hand-waving. Sub-3b honestly flagged OPEN with a concrete crux (the Dyadic-interval lemma).
Not a false closure — the outliner correctly records the naive even-count [1,2) test covers only
6348/13041, and correctly warns that ∫(N_Q−N_R)=1 alone does NOT force measure≥1 (the G_{n−1} dyadic
structure must be used explicitly). This is the plateau-break the shared-gap rule requires.
Issue: the whole slug lives or dies on the Dyadic-interval lemma (Sub-3b). Builder must either prove it
via the G_{n−1} alternating structure or produce the weaker summed "mismatch mass ≥1 across levels" bound —
must not assert "integral 1 ⇒ measure 1."

## ll-inclusion-gap — APPROVE (new; register; BUILD) — second viable LL route
Distinct mechanism from ll-dyadic-symdiff (split on containment S_Q⊆S_R, not on max(Q) scale), so the two
are genuine rival whole attempts at the same gap, not one proof cut into pieces — exactly what the
plateau rule sanctions. INC-GAP verified n=3 here (0 violations) and n=3,4 by the frontal explorer; its
mechanism (containment pins Q-parts into dyadic bands, ΣQ=2^n caps A(Q)) is stated with a reason, and the
outliner correctly records that the total-cut constraint t+cuts_R≤n is ESSENTIAL (INC-GAP is FALSE without
it — R={4,2,½,½} counterexample), so the proof must consume the budget. SYM-DIFF verified true, no general
proof — honestly open. Avoids the recorded-circular naive t→t−1 induction by the two-case split.
Issues: (1) general-n lift of INC-GAP integrality argument to arbitrary dyadic depth; (2) SYM-DIFF
alignment-cost ≥1 bound. Both real gaps, both flagged — build as an honest partial.

## extremal-smoothing — CHANGES REQUESTED (revise; NOT in build set this round)
Technique is the only LL-independent upper-bound route and the quasiconcavity idea is legitimately weaker
than the disproven "V globally concave" (R3), so it is not automatically dead. BUT its stated mechanism has
an unjustified leap: "min over XY responses of a piecewise-linear A(final)" is a min of *piecewise*-linear
(not linear) functions, so it is NOT concave in general — the outliner's own "IF the cell structure is
convexity-compatible" is the entire difficulty, and it is UNVERIFIED. The slug's first deliverable is a
numeric super-level-set convexity check for n=2,3 with "no proof path" until it passes. That is a probe,
not a build. With three stronger slugs already covering both the concrete Regime-B gain and the mandated
LL break, spending a build slot on an unverified long-shot whose predecessor was disproven is not
justified this round. Keep it live (registered, ranked lowest); run the bounded convexity probe as a
cheap explorer task before it ever earns a build slot. Do NOT re-table global concavity.

---

## Ranking (updated, whole field, stale flags cleared)
geometric-selfsimilar 1606 > ll-inclusion-gap 1517 ≈ ll-dyadic-symdiff 1515 > alternating-sum-value 1470 > extremal-smoothing 1391

Anchors: geometric-selfsimilar (advanced leader + verified concrete Regime-B deliverable) beats all.
The two new LL slugs (verified small-n mechanisms directly at the crux plateau) beat alternating-sum-value
(its distinctive greedy route is a recorded dead-end; contributes only shared certified lemmas this round)
and extremal-smoothing (unverified quasiconcavity). The two LL slugs drawn against each other (both honest
partials, both with verified n=3/4 mechanisms and explicit open sub-cases). extremal-smoothing lowest
(S1 stuck 3 rounds, predecessor disproven, hinges on an unchecked convexity property).

build set: geometric-selfsimilar, ll-dyadic-symdiff, ll-inclusion-gap
