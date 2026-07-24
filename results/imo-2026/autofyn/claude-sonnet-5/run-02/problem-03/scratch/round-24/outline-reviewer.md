## imo-2026-03 — round 24 outline review

### 1. greedy-halving-adversary (advance) — APPROVE

Target: same open front as round 23 — Case (b)'s "v>=a" branch, sub-case
where T' cuts p4 (round 23's own diagnostic finding: reduces, after
odd-run pair-cancellation, to a residual object {c2}∪T''' — an arbitrary
non-ladder-native value c2 merged with a smaller legal ladder response,
"the same problematic shape one level down" — not a clean smaller
self-similar instance).

**Checked: is this secretly the dead Cross-Level Rescaling route in
disguise?** No. The outline is explicit and correct that Cross-Level
Rescaling cannot apply here (its hypothesis needs the *whole* tail being
refined to already be a rescaled ladder; c is an arbitrary fragment of p4,
not a ladder value) — step 3/"Watch out for" explicitly forbids
re-attempting it and cites the exact reason (Experiment 1 from this
round's explorer: bisecting p4 into two copies of p5 just reproduces
Theorem 37's own vertex via a longer path). Instead the outline proposes
treating h(m) := inf over (c, legal refinement S of an m-ladder-scale tail)
of A({c}∪S) as its own standalone induction target, attacked by direct
application of the certified Vertex-Minimum Theorem + Odd-Run Reduction
Lemma to the *whole joint object* {c}∪S — this is the generic
compact-polytope/vertex-tie machinery, not the ladder-specific rescaling
lemma, so it is a genuinely different (and not previously exhausted)
tool for this exact shape. This is the same recipe that closed Claim A's
Case I (exchange-smoothing-vertex-maximization on a "free coordinate +
fixed reference set" shape), reused legitimately by analogy, not by
citation-only hand-off.

**Soundness of the mechanism.** Vertex-Minimum Theorem's hypotheses
(fixed composition, affine functional over a compact polytope) are met by
{c}∪S: c ranges over (0,q1], S ranges over its own legal-cut polytope,
jointly compact, A is affine-in-fragment-lengths for a fixed sorted-rank
pattern. No re-derivation is claimed needed for the vertex theorem itself
— correct, it's a direct instantiation. The vertex-family enumeration in
step 4 (c tied to an S-element / c pinned at 0 / c pinned at q1/2 / c ties
across levels after S is refined) looks like a reasonable candidate
list by analogy with the single-insert-point vertex family already
established elsewhere, but is explicitly flagged as unproved-exhaustive
by the outline itself ("enumerate all before claiming exhaustiveness") —
correctly scoped as the round's actual open gap, not asserted as done.

**Watch-out flag is itself correct and useful**: the outline warns against
assuming h(m) is isomorphic to the original problem L(m) — true, c has no
p_i=2p_{i+1}-type relation pinning it, so h(m) is a strictly less
structured object; L(m)'s specific closed-form machinery (Ratio-2 Spacing
Lemma, etc.) cannot be assumed to transfer without re-derivation. Good
guardrail for the builder.

No fatal flaw found. Minor note to relay to the builder: step 4(b)'s
proposed dual (min-direction) use of exchange-smoothing-vertex-maximization
needs the SAME explicit from-scratch re-derivation flagged for the sibling
below — don't assume it's free just because 4(a) (direct vertex
enumeration) is the preferred route; if 4(a) stalls and the builder falls
back to 4(b), the direction issue below applies equally here.

### 2. rank-pigeonhole-budget (advance) — CHANGES REQUESTED

Target: same object via the independently-derived Single-Insert-Point
Vertex Lemma, this round trying to close the residual by an UPPER bound on
a {c2}∪T'''-type quantity (open gap: characterizing exchange-smoothing-
vertex-maximization's polytope one level down).

**Direction check (the dispatch's explicit concern) — a real, unresolved
issue, not just a wording nit.** Re-derived from the project's own
definitions: A(S) = Total(S) − 2E(S) where E is the even-sorted-rank sum.
`exchange-smoothing-vertex-maximization` (certified round 8) computes
**max_F E(F∪τ)** over a fixed reference τ — this is exactly what Case I
Closure used, because Case I needed a LOWER bound on A (Claim A: A≥a_n),
which requires an UPPER bound on E, i.e. the max-E direction — consistent
with the certified statement.

This round's step 3 needs the opposite: an UPPER bound on A({c2}∪T''') (or
the complementary A(T')-type quantity feeding the Insert-Element
Identity's slope formula, per the outline's own step-3 parenthetical: "a
one-sided LOWER bound on A(T')-type quantities is structurally
insufficient, so this step must supply an upper bound instead"). An upper
bound on A ⟺ Total − 2E ≤ K ⟺ E ≥ (Total−K)/2 — a **LOWER bound on E**,
the dual/minimization direction, NOT what `exchange-smoothing-vertex-
maximization` proves. The outline's Key-Lemmas paragraph says this "must
be EXPLICITLY re-verified for the maximization direction here... not
assumed free from the min-direction usage in Case I" — this has the
polarity backwards: Case I's own usage *was* the max-E direction (matching
the certified statement exactly); what this round's step 3 actually needs
is the *min*-E direction, which is NOT yet proved for this shape at all
(only asserted "polarity-agnostic by a standard compact-polytope
argument," which is plausible but genuinely unproved — the same caveat the
sibling's outline states explicitly and correctly for its own step 4(b),
but this outline states confusingly and, on its face, incorrectly for
which direction is "the same as Case I").

This is a build-blocking ambiguity: if the builder takes the outline's
literal instruction ("apply exchange-smoothing-vertex-maximization... the
same shape as Case I's maximization") at face value, it will try to reuse
the *certified* max-E lemma directly, which proves the wrong-signed bound
for what the proof chain needs, and the builder will either produce an
unusable result or waste the round rediscovering the mismatch. Numeric
sanity: a lower bound on E (to get an upper bound on A) is a fundamentally
different extremal computation than an upper bound on E — pinning
coordinates to 0/τ minimizes vs. maximizes E in general, so a fresh
exchange argument (not just "re-verification") is what's actually required
here, exactly the sibling's honest framing of its own analogous step.

**Verdict and required fix.** Not fatal — the underlying target (upper-
bound the complementary quantity feeding the Insert-Element chain) is a
legitimate thing to attempt, and the polytope-structure gap (T''' is not
literally a fixed reference set — it has its own nested cut budget, an
honestly-flagged open item already) is correctly scoped as unresolved.
But before build, the instruction must be corrected: (1) have the builder
first pin down, by direct symbolic derivation of the Insert-Element
Identity's slope formula at this depth, exactly which quantity (A(T'''),
A(T'''_{>c2}), or something else) needs which-signed bound; (2) do NOT
instruct "reuse exchange-smoothing-vertex-maximization, re-verify the
maximization direction" — instead instruct: attempt to prove the DUAL
(min-E) statement for this "free coordinate + fixed(ish) reference"
shape from scratch (same exchange-perturbation technique, opposite
optimization direction), explicitly flagging it as new content, not a
citation. If the builder cannot close this cleanly this round, an honest
"this needs a new min-direction lemma, not yet proved" report is an
acceptable (CHANGES REQUESTED) outcome — just not a mistaken direct reuse
of the max-E lemma presented as sufficient.

### 3. lp-duality-certificate (advance) — APPROVE (with the outline's own
caveats kept intact)

Target: extend the covering-chamber family to close case (b2) at n=3 by
constructing the p1,p2-cross-tie chamber for the residual (1,1,0,0),
(1,1,0,1), (2,0,0,0) compositions near p1→T/2.

**Mechanism check.** Double-Sandwich-Below/Above's claimed closed forms
(Φ = (T+p2+p3−p1)/2, Φ = (T+p1−p2−p3)/2) and complementary feasibility
(p1<p2+p3 vs p1>p2+p3) are a plausible, cheap instantiation of the
already-certified Cross-Piece Sign-Assignment Identity (a straddle over
two untouched tail elements instead of one is the identity's normal use
case, not new machinery) — the outline correctly demotes this to "derive
rigorously, don't just recover numerically," which is the right level of
rigor to demand.

**Residual plausibility check (independently verified).** Ran a fresh
brute-force/randomized search (`/tmp/check_lpdual.py`, exact `Fraction`
arithmetic, 5 random points with p1∈(0.43,0.50)T, n=3) confirming
min_Φ(legal Xiang-Yu response) ≤ a_3·T = 8/15·T at every sampled point in
the flagged residual zone (values found ≈0.51–0.53 < 0.5333) — consistent
with (not a substitute for) the outline's claim that some strategy in this
zone beats the target, supporting that a covering chamber plausibly
exists there. This is exactly the kind of small-case sanity check the
outline should be judged against, and it passes.

**Feasibility-suffices-for-upper-bound** is correctly cited as already
certified (round 23) — the outline's step 4/5 plan (LP/vertex-check the
new chamber's feasibility region is polyhedral, check finitely many
vertices) is the right, already-validated methodology, not new machinery
each time.

**Watch-out section is appropriately cautious**: correctly flags that the
Double-Sandwich chambers' own feasibility intervals degrade to nothing
exactly at the case-(a)/(b2) boundary (p1→T/2), so the new chamber's
feasibility must be explicitly checked in the limit, not just at interior
points — and correctly reminds the builder that the explorer's "reduces
essentially to p1<p2+p3" finding was numeric recovery only, needing exact
algebraic re-derivation before being relied on. No overclaim in the
outline; step 7 explicitly requires an honest non-closure report if step 5
fails.

No fatal flaw found. One thing to relay to the builder: the outline's own
step 6 ("close the ENTIRE general upper bound at n=3") should be read
literally as scoped — n=3 only, no implicit n≥4 claim — which the outline
already states explicitly, good practice to keep.

### Diversity note

All three approaches attack the *same* precisely-localized open item
(Case (b)'s "v≥a" T'-cuts-p4 residual for the lower bound; case (b2)'s
n=3 residual for the upper bound) via genuinely different mechanisms
(whole-object Vertex-Minimum application, independent Single-Insert-Point
slope argument, LP-chamber covering-family construction) — this matches
the project's established acceptable-diversity pattern (memory rule #3):
different techniques converging on adjacent narrow gaps is legitimate,
not a plateau signal, since the population is not collapsing to one
framing (lower-bound front vs. upper-bound front remain two distinct
targets). No new framing is required this round.

### Ranking

Registered: no new slugs this round (all three are advance-in-place,
already registered). Ranked via `update_ranking` — greedy-halving-adversary
and lp-duality-certificate both beat rank-pigeonhole-budget (whose outline
carries the unresolved direction flaw above, needing a fix before its
claimed mechanism can be trusted), and greedy-halving-adversary drew with
lp-duality-certificate (both outlines are clean and well-scoped, on
different fronts). This clears the `stale` flag set by round 23's outcome
recording.

build set: greedy-halving-adversary, lp-duality-certificate, rank-pigeonhole-budget
