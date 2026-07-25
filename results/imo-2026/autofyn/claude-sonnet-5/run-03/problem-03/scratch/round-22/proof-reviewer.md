# Round 22 proof-reviewer report — imo-2026-03

Independently re-verified (own scripts, exact `Fraction`/`sympy`, not
reusing any builder script) both round-22 approach files. Full detail is
now written into `results/imo-2026-03/current.md`; summary below.

## 1. `self-similar-induction-on-n` (round 22: Track 1 + Track 2)

**Verdict: CHANGES REQUESTED. Status: partial (correctly self-reported,
no overclaim found).**

### Track 1 — Odd-Excess e≥3 Endpoint Closure Theorem

Re-derived the margin identity `margin(a1) = 2^k/6 + 2^m/6 - a1/2 - 1/2`
symbolically from scratch with sympy — matches the file's claim exactly
(`sympy.simplify` gives residual 0). Confirmed it is affine, strictly
decreasing in `a1` (slope -1/2), so on the right-closed domain
`(2^(k-1), 2^k]` the minimum is genuinely attained at `a1 = 2^k` (not an
open supremum — this is exactly the class of boundary bug flagged in
round 17/18, and this round's file explicitly checks it correctly).
Evaluated `margin(2^k) = 2^k(2^e-2)/6 - 1/2` symbolically — matches.
For odd e≥3 this is ≥ 2^k - 1/2 ≥ 3/2 > 0 for every k≥1 (tight at k=1,
e=3). Independently wrote a fresh exact-`Fraction` stress-test script
(547 then 10,000 trials, k=1..6, e∈{3,5,7}, `a1` spanning the whole
interval including the exact endpoint, R of random count up to 15 with
`max(R)≤2^(k-1)` deliberately uncapped in count beyond GT(m)'s own
cardinality cap to confirm cap-freeness): zero violations, minimum
observed margin ≈1.66 (close to the theoretical exact floor 1.5, not
hit exactly by random sampling but consistent). Also hand-checked the
exact worst-configuration instance (k=1,e=3,a1=2,R=14 copies of 1):
OddSum=18>16=2^m, consistent (the Half-Sum-Corollary-derived floor of
3/2 is a valid lower bound on the margin, not necessarily tight for
every R — correctly used as an inequality, not an equality claim).
**Crucially, plugged e=1 into the SAME formula and got margin(2^k)=-1/2
< 0** — exactly reproducing round 17's known e=1 boundary
counterexample, which is strong internal-consistency evidence the
formula and its scope restriction (e≥3 odd, explicitly excluding e=1)
are both correct, not an artificial narrowing. No gap found in Track 1.

### Track 2 — Cap-Free GCH + Case-B(m,k) Sliver Closure

The headline risk here ("the cap is never used" in each of Steps A, B,
C0, C1, C2, plus the underlying Finite Reduction Theorem) was audited by
directly re-reading the cap's role in each cited proof (not just trusting
the file's prose) and then independently stress-testing the FINAL
cap-free theorem end-to-end with deliberately extreme cap-violating
instances (e.g. k=3, R={7,1} with max(R)=7 ≫ old cap 4): 18,000-trial
exact-`Fraction` sweep (k=1..6, S∈[2^k,2^k+1), |R|≤k+1, values genuinely
uncapped) — zero violations, minimum AltSum=1 exactly (tight, as
expected). The k=1 hand-proof (two exhaustive sub-cases on |R|∈{1,2})
was re-checked by hand and matches a 5,000-trial spot check. The new
tie-robust AltSum Peeling identity (no unique-max hypothesis) was
verified elementary and correctly scoped as needed (the certified
Even-target Companion Peeling identity requires a unique max, which
Case-B(m,k)'s b1 is not guaranteed to have).

Independently verified the Case-B(m,k) Sliver Closure Theorem itself
with a fresh script (13,617 trials, m=2..6, b1 random in the sliver,
B' of random structure with no cap enforced, 6,383 infeasible
constructions correctly skipped): zero violations of OddSum(B∪Γ_{m-2})
≤2^m-1. Combined with round 5's Theorem 2 (outside the sliver), this
genuinely closes Case-B(m,k) in full.

**The file's own honest negative finding was independently checked and
confirmed genuine**: it retracts round 17's claim that GT(m)'s
remaining e=0 residual for sub-case (i) is "the same object" as
Case-B(m,k). Re-derived both objects' sum ranges by hand: sub-case (i)'s
own e=0 form needs sum(R)∈(2^(k-1)-1,2^(k-1)) (just BELOW 2^(k-1)), while
Case-B(m,k)'s peel produces sum(B')∈(2^(m-1),2^(m-1)+1) (just ABOVE
2^(m-1)) — genuinely different ranges relative to the same threshold.
This is a real, previously-unflagged correction, not a manufactured
distinction to avoid overclaiming.

**No gap found in either track.** GT(m) as a whole is correctly reported
as still open (sub-case (i)'s e=0 residual untouched) — this is not an
overclaim, it's an honest and precisely-scoped partial result.

**2 new lemma files certified**: `lemmas/odd-excess-e-geq-3-endpoint-closure.md`, `lemmas/cap-free-gch-and-case-b-sliver-closure.md`.

## 2. `global-lp-vertex-sufficiency` (round 22 Section 13)

**Verdict: CHANGES REQUESTED. Status: partial (correctly self-reported,
no overclaim found).**

Independently re-derived all three new closed-form identities (Q, BB,
CB, both CB sub-cases) from scratch in sympy, expressing everything in
`(g1,g2,g3,p4)` via the mass identity `p4=(1-g1-2g2-3g3)/4`:
`sympy.simplify` gives exact residual 0 for all four claimed identities
(`OddSum(Q)-c(3)-(p4-g2-gamma(3))/2`, `OddSum(BB)-c(3)-(g1-p4-gamma(3))/2`,
and both CB-case identities). All match the file digit-for-digit.

Independently re-verified the Duplicate-Pair Contribution Fact (an
even-multiplicity block of size 2j contributes exactly j copies of its
value to OddSum, position-independent) via a 5,000-trial exact-`Fraction`
test comparing OddSum with/without an appended even-multiplicity block —
zero mismatches, confirms the general-purpose elementary fact.

**The claimed exact counterexample to the outline's 6-construction panel
{H,C,Q,R,BB,W} was independently and exactly reproduced.** At
p=(6,4,2,1)/13 (confirmed a valid, strictly interior point of Region II:
all gaps > gamma(3)=1/15, p1<1/2, p4>gamma(3) so outside Region I):
independently computed Construction C's response {g1,p2,p2,p3,p4} and
Construction Q's response {p1/2,p1/2,g2,p3,p3,p4} and Construction BB's
response {g1,p2,p2,p3/2,p3/2,p4}, all giving OddSum=7/13 exactly,
matching the file — excess 7/13-8/15=1/195>0. Independently confirmed H
illegal (x=(p3-g1)/2=0 exactly) and W illegal (p1-p2-p3=0 exactly),
their legality boundaries genuinely coinciding at this point. (Note: I
was not able to locate Construction R's exact definition in this file —
it appears to originate from a round-22 math-explorer report, not
restated in the approach file itself; I did not independently verify R's
claimed value at this point, but the independently-confirmed C/Q/BB
triple tie at exactly 7/13 already fully substantiates the panel-wide
failure on its own.) Also independently confirmed the patch: Construction
CB's response {g1,p2,p2,p3,p4/2,p4/2} gives OddSum=1/2 exactly at this
point (<c(3)=8/15), matching the file's claim and its independently-
computed brute-force LP optimum.

This is genuine, precise, checked progress: a real hole found in a prior
round's own proposed candidate panel, pinned to an exact rational point
(not a numeric near-miss), and patched with a new construction whose
closed form is separately verified. **The file correctly does NOT claim
this closes Region II** — it explicitly flags that (a) Q/BB/CB's
identities are proved only on their own order-condition sub-domains, (b)
no case-complete symbolic argument establishes min{H,C,Q,R,BB,W,CB}≤c(3)
everywhere in Region II, only an 18-restart differential-evolution search
(evidence, not proof), and (c) it remains genuinely possible the enlarged
7-panel has its own undiscovered exact counterexample, exactly as the
6-panel did. No overclaim found.

**1 new lemma file certified**: `lemmas/construction-q-bb-cb-identities.md`.

## Overall problem status: imo-2026-03 remains `partial`, NOT solved.

Neither direction of the Existence Theorem/lower-bound program is
complete for general n:
- **Lower bound (GT(m))**: every excess-carrying sub-case (e≥1, both
  parities) is now closed, and `Case-B(m,k)` is now fully closed — but
  sub-case (i)'s own separate e=0 residual remains open, and this round
  found it is genuinely distinct from Case-B(m,k) (not interchangeable,
  contrary to round 17's characterization).
- **Upper bound (Existence Theorem)**: complete for n=2; n=3's Region I
  is complete; n=3's Region II remains open (narrower and better
  characterized this round, with a real hole found+patched, but not
  closed); n≥4 has not been attempted at all.

`results/imo-2026-03/current.md` has been rewritten with `## Status:
partial`, a detailed `## Current best` summarizing exactly what is
closed vs. open on each side, and the full round-22 `## Approaches
tried` entries (round 21 and earlier history preserved below). No `##
Full proof` section — none is warranted.

Both approaches are recorded via `record_outcome` as `advanced` for
round 22 (real sub-closures / real caught-and-patched gaps, not merely
narrowing).

Files touched:
- `/home/agentuser/repo/results/imo-2026-03/current.md` (rewritten)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/odd-excess-e-geq-3-endpoint-closure.md` (new, certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/cap-free-gch-and-case-b-sliver-closure.md` (new, certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/construction-q-bb-cb-identities.md` (new, certified)
