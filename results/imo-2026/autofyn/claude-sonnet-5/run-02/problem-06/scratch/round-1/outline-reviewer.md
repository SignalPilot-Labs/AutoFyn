# Outline review — imo-2026-06, round 1

## Sanity checks performed (Bash/python3)

1. Simulated the greedy sequence for a_1 = 15, 35, 143, 1001 up to a few thousand
   terms (`/tmp/sim2.py`).
2. Confirmed the shared "free fact" (gcd(a_n,a_1)>1 for n≥2, hence P(a_n)∩Q≠∅ with
   Q=P(a_1) fixed and finite) is a one-line consequence of the hypothesis with i=1 —
   trivially correct, not a real gap for any approach.
3. Directly searched for T, L with `a_{n+T} = a_n + L` **holding from n=1** (not just
   eventually) for all four seeds, up to T≤800: found (T,L) = (8,30) for a_1=15,
   (34,210) for a_1=35, (64,858) for a_1=143, (282,2002) for a_1=1001 — in every
   tested case the periodic identity holds *from n=1*, with L = product of a small
   finite recruited prime set (2002=2·7·11·13 for a_1=1001, matching the outliner's
   {2,7,11,13} claim exactly, T=282 also matches). This is strong evidence (not proof)
   that the shared building block (ii) — CRT+pigeonhole finish given S finite — is
   sound, and that the "n=1 boundary" gap all four approaches flag is real but likely
   not fatal: in every tested instance the period was already exact from n=1, no
   special pre-period patching was needed. Still must be proved in general, not just
   observed; keep it as a required (but probably short) closing step, not a wall.
4. Traced the pattern-class mechanism for a_1=15 by hand from the simulation output:
   terms with Q-pattern {3} only and terms with Q-pattern {5} only are, empirically,
   *always* even (witnessed by the single helper prime 2) throughout 60+ terms, while
   terms with pattern {3,5} (odd multiples of 15) need no helper at all. This gives a
   genuine, checkable mechanism for why finitely many helper primes suffice: a term
   with pattern A must intersect **every** previously-seen term of a disjoint pattern
   B; since the B-pattern terms do not share a uniform "extra" prime among themselves
   beyond a small set, any A-pattern term is forced to share a *fixed* prime (here 2)
   with essentially all of them, or else it would need to be divisible by infinitely
   many distinct primes — impossible for a single fixed integer. This is essentially
   the mechanism amortized-charging-budget is reaching for, and it appears to be a real
   route to the core lemma, not a dead end. Good news for the population: the shared
   crux (finiteness of S) looks true and provable, not a wall that kills all four
   approaches outright.
5. Confirmed the trivial |Q|=1 case (a_1=4): sequence is exactly all even integers > 4,
   T=1, L=2, holds from n=1 — matches all four approaches' claimed base case.

## Per-approach verdicts

### hypergraph-transversal — CHANGES REQUESTED
Technique (minimal-antichain transversal) is legitimate and steps 1–2 (transversal
equivalence, antichain update rule) are genuinely proved, not hand-waved. But the
proposed mechanism for the load-bearing lemma (step 3, finiteness of S) is not really a
mechanism: the "potential Φ_n = Σ 2^{-min(B)}" is defined but never shown bounded, and
the approach *itself* admits the potential-function framing "does NOT yet prove S is
finite a priori" and that an "auxiliary growth/density argument... is unavoidable" —
i.e. it explicitly falls back on density-sieve-contradiction's mechanism to close its
own key step. As written this is the weakest of the four: it names a lemma without a
working mechanism, which CLAUDE.md flags as an unverified hand-off. Fix before next
build: either (a) give a genuine monovariant that provably decreases/bounds without
appeal to an outside density argument, or (b) explicitly merge with a sibling approach
rather than presenting an incomplete potential function as if it were self-sufficient.

### covering-system-construction — CHANGES REQUESTED
Sound, concrete framing: explicit recruitment with a stated (if unproved) quantitative
target — primorial growth vs. a Bertrand's-postulate-style gap bound. This is a real,
checkable inequality, not a hand-wave, and the approach correctly flags it as the one
open piece. Step 6 (n=1 boundary) same caveat as all others, but as discussed above this
looks tractable. Recommend the builder work the |Q|=2 template (a_1=15) fully by hand
first, as the outline itself proposes, to pin down the actual inequality before
generalizing.

### density-sieve-contradiction — CHANGES REQUESTED, flag convergence risk
The primary sieve/Mertens route (step 3) is honestly flagged by the outline itself as
circular ("needs an a priori cap on distinct small primes... circles back to core
finiteness") — correct self-diagnosis, this sub-route as stated cannot close without
first assuming what it's proving. The recommended fallback (step 4, "blocking types
capped by |Q|") is structurally the *same* combinatorial-type-bounding idea as
amortized-charging-budget's pattern-pair charging — both bound recruitment/blocking by
a quantity depending only on 2^|Q|. This is a real convergence, not superficial: if the
builder pursues step 4 as instructed, this approach and amortized-charging-budget are
likely to produce near-identical cores. Per CLAUDE.md's single-gap-trap guidance, don't
let both consume a build slot doing the same thing under different names this round —
build the charging version now (it's already built around the finite-type idea from the
start, cleaner), and have density-sieve-contradiction either genuinely diversify (do the
raw sieve/Mertens estimate honestly, own its harder circularity risk, potentially with a
different resolution) or wait a round.

### amortized-charging-budget — CHANGES REQUESTED (strongest of the four, build it)
The charging idea is the best fit for the mechanism confirmed numerically above (forced
sharing of a small fixed prime across opposite pattern classes because an infinite family
can't be individually intersected by any other means). Real gap correctly identified:
"permanence" as stated (once a pattern-pair is reconciled it stays reconciled) is not
obviously true and the outline is right to flag it. Recommend the builder replace the
"permanence" framing with the direct argument sketched above: a term of pattern A must
hit *every* earlier term of a disjoint pattern B; since the B-class has no uniform shared
prime beyond a bounded set (or it does — that bounded set is itself the recruit), a term
with pattern A occurring after B-terms have "used up" their available shared primes is
forced onto one of finitely many surviving witness primes. This reframes "permanence" as
a forced-intersection argument rather than an assumed bookkeeping invariant, which
should be easier to make airtight. Keep the |Q|=1, |Q|=2 (a_1=15), |Q|≥3 (a_1=1001) test
cases as required by the outline.

## Diversity assessment
All four target the full claim end to end (not fragments) — acceptable per CLAUDE.md.
They correctly share only the two routine building blocks; the genuine divergence is on
HOW to bound the load-bearing prime set, which is the one hard step in this problem —
this is not the harmful "one proof split across slugs" pattern. However, two pairs are
closer than they look: density-sieve-contradiction's recommended fallback converges with
amortized-charging-budget (flagged above), and hypergraph-transversal's stated mechanism
explicitly bottoms out in the same territory as density-sieve. Net diversity right now
is closer to "2.5 genuinely distinct mechanisms" than 4. Next round's outliner should
either sharpen density-sieve's raw-sieve route to be a real alternative, or fold it and
revisit hypergraph-transversal's potential function with a concrete, self-contained
definition — otherwise the population will collapse toward 2 real lines.

## Ranking
Elo updated via `update_ranking`: amortized-charging-budget and covering-system-
construction come out on top (draw between them, both beat the other two on having a
concrete, checkable, non-circular-as-stated mechanism); density-sieve-contradiction
above hypergraph-transversal (its own diagnosis of its circularity is more honest and
its fallback sub-route is workable, even if convergent with charging), hypergraph-
transversal lowest (names a lemma with no working mechanism, self-admits it needs an
outside density argument to close).

Final Elo: covering-system-construction ≈1531, amortized-charging-budget ≈1530,
density-sieve-contradiction ≈1486, hypergraph-transversal ≈1453.

## Build set rationale
Building all four this round would spend two builder-rounds re-deriving the same
finite-pattern-type bound (density-sieve's fallback ≈ amortized-charging) and one
builder-round patching a lemma (hypergraph-transversal) that currently has no
self-contained mechanism to patch. Build the two strongest, genuinely distinct,
concrete lines this round; leave density-sieve-contradiction and hypergraph-transversal
for the outliner to sharpen (diversify density-sieve away from the convergent fallback;
give hypergraph-transversal a real potential function) before spending a build slot on
them.

build set: amortized-charging-budget, covering-system-construction
