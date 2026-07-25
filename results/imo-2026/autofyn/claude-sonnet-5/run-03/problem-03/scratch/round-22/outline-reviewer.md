# Outline review — round 22 — imo-2026-03

## self-similar-induction-on-n — revise (two tracks, GT(m) closure)

### Track 1 — Odd-excess e>=3 Endpoint Closure Theorem

**Verdict: APPROVE.**

Independently re-verified the core claim by direct multiset computation
(own exact-`Fraction` script, not the explorer's): for D = {a1} ∪ R,
`max(R) <= 2^{k-1}`, `sum(D) = 2^m`, a1 ranging over the *whole* range
`(2^{k-1}, 2^k]` (not just the window), k = 1..4, e ∈ {3,5,7}, R of random
count up to 8 (deliberately uncapped in count) — 3600 trials, **zero
violations** of `OddSum(D∪Γ_{m-1}) >= 2^m`, matching the claimed margin
formula `2^k(2^e-2)/6 - 1/2` exactly (positive for all k>=1, odd e>=3).
The logic is sound: the margin is affine in a1 (slope -1/2, derived by
direct combination of two already-certified lemmas — Half-Sum Corollary
and the corrected e-fold q=0-chain closed form), so its minimum over the
closed-on-the-right interval is at the right endpoint a1=2^k, evaluated
in closed form. No case-split, no cap needed (Half-Sum Corollary is
cap-free by construction) — this really is a short, mechanical, 3-step
closure, as the round-22 explorer found. The outline correctly
cross-references round 18's exact bug class (evaluating only at the
window sup instead of the true range endpoint) and explicitly instructs
the builder not to repeat it, and correctly scopes e=1 out (stays on the
harder, already-closed-in-round-21 GCH(k) route). No gap in this track.

### Track 2 — Case-B(m,k) sliver via cap-free GCH strengthening

**Verdict: APPROVE, with the outline's own flagged gaps genuinely being
the load-bearing open work (not defects in the outline itself).**

Re-verified the peel-then-invoke-GCH mechanism independently. First
attempt at a numeric check produced spurious violations because my own
script failed to enforce `b1 = max(B)` (a bug in my test, not the
outline's claim) — corrected by requiring all other parts `<= b1`, after
which 2500 trials across m=2..6 gave **zero violations** of the sliver
target `OddSum(B∪Γ_{m-2}) <= 2^m-1`. This is exactly the kind of
self-correction the repo's "ALWAYS" verification rules are meant to
catch, and it confirms the outline's claim is genuinely sound once the
maximality constraint is respected (this is a good, concrete
double-check point to flag to the builder: `b1` must literally be the
max of the whole multiset B, not merely satisfy the sliver's numeric
range — this is used implicitly when invoking Global-max Peeling).
Separately verified the cap-free GCH claim directly (R with `|R| <= k+1`,
`sum(R) ∈ [2^k, 2^k+1)`, max(R) *unconstrained*, k=1..6, 3000 trials):
**zero violations** of `AltSum(R∪Γ_{k-1}) >= 1`, matching the explorer's
claim that Case (C2)'s cap is not load-bearing.

The feasibility arithmetic checks out symbolically: peeling b1 leaves
B' with `sum(B') = 2^m - b1 ∈ (2^{m-1}, 2^{m-1}+1) ⊆ [2^{m-1}, 2^{m-1}+1)`
and `|B'| <= m = (m-1)+1`, exactly matching GCH(m-1)'s hypotheses with
`k := m-1`. The chain of implications from the cap-free GCH conclusion
to the sliver's strict inequality is correct algebra (`AltSum(B∪Γ_{m-2})
= b1 - AltSum(B'∪Γ_{m-2}) <= b1 - 1 < 2^{m-1}-1` since `b1 < 2^{m-1}` in
the sliver).

What remains genuinely open, correctly flagged by the outline itself
(not something I found missing): (1) the line-by-line re-verification
that Steps A/(C0)/(C1) of the certified GCH proof never load-bear on the
value cap — this is a proof-text audit, not a numeric question, and must
actually be done by the builder, not re-asserted from the explorer's
informal read; (2) the k=1/m=2 boundary case, outside GCH's stated
`k>=2` range, needs its own short direct argument. Both are correctly
scoped as the round's real work, not outline defects.

The outline is also honest and correct that closing Case-B(m,k) does
**not** automatically close sub-case (i)'s own e=0 residual (opposite
side of the threshold — `sum(R)` approaches `2^{k-1}` from below there,
not `2^k` from above as GCH needs) — this is exactly right and must stay
flagged, not silently folded into "GT(m) closed."

### Build assignment

**One builder, one slug, sequential.** Both tracks live inside the same
approach's proof of the same overall theorem GT(m) — this is not the
CLAUDE.md "split one proof across slugs" trap (that describes splitting
a *single* gap across rival slugs so they'd die together; here the two
tracks are two structurally distinct sub-cases of one case-split, and
having two builders write to the same approach file in parallel would
just collide). Dispatch a single proof-builder for
`self-similar-induction-on-n`, instructed to do Track 1 first (short,
near-mechanical — a safe, fast certified win) then spend the remainder
of the round on Track 2's harder line-by-line audit and the k=1 boundary
case. If Track 2 isn't fully closed this round, that's a normal
CHANGES REQUESTED outcome, not a failure — Track 1 alone would still be
real, certifiable progress (closing sub-case (i) entirely for e>=1).

---

## global-lp-vertex-sufficiency — revise (n=3 Existence Theorem, Region II)

**Verdict: APPROVE.**

The outline is well-scoped: Region I is closed; the round's job is to
split Region II (still open) into IIa/IIb and close each with a
different construction (Q/R for IIa, BB [+W as fallback] for IIb).

Checked the partition claim algebraically: Region II is defined (by the
existing, certified Region I closure) as the complement `{p4>γ(3)} ∪
{g3+p4<=3g1}`. Setting `IIa := Region II ∩ {p4>γ(3)}` and `IIb :=
Region II ∩ {p4<=γ(3)}`, `IIa ∪ IIb = Region II` is **automatic** by
basic set algebra (any set intersected with a proposition and its
negation partitions trivially) — this isn't a real risk, it's a tautology
given the definitions as stated, so the builder should not over-invest
time re-deriving it; the actual content-bearing step is confirming that
`IIb`, expressed via `{p4<=γ(3)}`, does reduce to exactly `{p4<=γ(3),
g3+p4<=3g1}` (the "other half" of Region II's original union
definition) — a one-line check, correctly flagged as "do first."

The two proposed constructions (Q/R: bisect p1, tie a p2-fragment to
p3/p4; BB: bisect p1 like Construction H's split but also bisect p3) are
genuinely new splitting patterns, not tie-parameter tweaks of the
already-refuted 8-mechanism panel — this matches CLAUDE.md's demand for
route diversity within a single approach's case coverage, not
resubmitting a dead mechanism. Q's legality is essentially free
(`p2 > g2 > p3 > 0` always holds in B(3)); this is correctly flagged as
a one-line check, not a real risk. BB's near-exact numeric tightness
(within 5e-10 of c(3) at the found worst point) is honest, correctly
labeled evidence of a genuine algebraic equality boundary to be derived,
not assumed as already proved — the outline does not overclaim this as
closed.

Open gaps are correctly and specifically named: all of Q/R/BB/W's
closed-form identities are currently spot-checked numerically only, not
derived in exact algebra (unlike Construction H); BB's order condition
`g1 >= p3/2` is checked at only two points, not proved throughout IIb.
These are exactly the right things to flag as this round's real work —
the outline explicitly warns the builder not to shortcut them (citing
the standard set by Construction H's own order-condition proofs), which
is the correct level of rigor demand.

No fatal flaw found. No skipped case: Region I ∪ IIa ∪ IIb is claimed
(and will be, once verified) to cover B(3) exactly; W is correctly
scoped as an optional secondary witness only if BB alone doesn't cover
IIb, not a silently-assumed additional case.

---

## Diversity / plateau check

The two live approaches attack genuinely different halves of the
problem (GT(m)'s lower-bound recursion vs. the Existence Theorem's
upper-bound construction) via structurally unrelated techniques
(peeling/cardinality combinatorics vs. LP-vertex/order-condition
substitution) — this is not a single-framing plateau. Both made
independently-certified progress last round (round 21) and continue to
close well-scoped, distinct sub-gaps this round. No shared-gap collapse
to flag this round.

## Ranking

Updated via `update_ranking` (draw between the two live leaders,
reflecting comparable, genuine round-21 progress on separate halves of
the problem; both beat the currently dormant/dead-end siblings
`lp-duality-split-polytope`, `reciprocal-potential-induction-on-n`,
`discharging-neighbor-transfer`). No new slugs to register this round
(both `self-similar-induction-on-n` and `global-lp-vertex-sufficiency`
are already registered); no `copy_approach` — the two GT(m) tracks stay
inside one slug (see build assignment above), not forked.

Resulting Elo (top of field): `self-similar-induction-on-n` 1628.4,
`global-lp-vertex-sufficiency` 1623.2, `lp-duality-split-polytope`
1507.6, `reciprocal-potential-induction-on-n` 1440.0,
`discharging-neighbor-transfer` 1420.5.

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency
