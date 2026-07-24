# Outline review — imo-2026-06, round 20

## Process note (important, flag for orchestrator)

The proof-outliner's report (`/tmp/round-20/proof-outliner.md`) described 4
approaches, but only 2 of the corresponding `approaches/*.md` files were
actually touched this round (`triangle-consistency-pigeonhole.md`,
`n1-periodicity-reconciliation.md` — both still show only round-19 builder
content, no round-20 material was written into them). The other two —
`a1-3q-subfamily-theorem` (new) and `triangle-critical-dichotomy-witness`
(copy) — had **no approach file at all**. Per the `register_approach` tool's
own contract ("the outliner seeds the approach's commentary
`results/<id>/approaches/<slug>.md`"), this is the outliner's job. To avoid
losing a round, I wrote seed files for both (transcribing the outliner's
vetted skeleton, with my own numeric corrections folded in — see below) so
the builders have a starting point. **Future outliners: always create/seed
the approach file for a NEW or copy-of slug in the same round it is
proposed, don't leave it to the reviewer.**

## 1. `triangle-consistency-pigeonhole` (revise) — APPROVE

Sound continuation of the strongest live FAH thread. Verified:
- Steps 1-2 correctly cite already-certified lemmas (no reproof needed).
- Step 3 (Constrained Singleton Coherence) mechanism is a straightforward,
  correct consequence of Confined-GCD + the definition of singleton
  occurrence — checked the logic by hand, it holds: if `d*` divides `a_x`
  and `a_x`'s entire outside-core part is the single prime `q_x`, any
  divisor of `a_x` supported outside `S_0` must be `q_x^j`. No gap in this
  step's own reasoning.
- Step 4 (the open gap) is honestly and precisely scoped, correctly kept
  separate from step 4(ii)'s "singleton actually populates the class"
  sub-claim (good — the outline explicitly warns against conflating (i) and
  (ii), a real risk given round-19's near-miss).
- The outline's own "watch out for" (a) correctly pre-empts the class of
  failure ("core-enlargement recruitment" collapsing back to H1/H2) that
  killed several prior mechanisms (rules 15, 26 in memory) — good
  self-screening.

No numeric red flags found in the parts I could spot-check (the mechanism
here is symbolic, not a concrete quantitative claim to falsify).

## 2. `triangle-critical-dichotomy-witness` (copy) — APPROVE, with mandatory equivalence check

The outliner itself flagged this as "possibly redundant" with approach 1.
I scrutinized this directly:
- Approach 1's engine: FIX one early occurrence `m_A` of `A'`; pigeonhole
  `gcd(a_{m_A}, a_x)` over MANY LATER occurrences `x` of `B'` to force a
  constant divisor class, then look for a singleton inside that class.
  Direction: forward, one-fixed-witness-vs-many-later-candidates.
- Approach 2's engine: FIX a later occurrence `n` of `A'`; use the Critical
  Prime Dichotomy Lemma's minimality argument to look BACKWARD for the
  single earlier index `i<n` that `q'` uniquely "rescues" (`P(a_i)∩P(a_n) =
  {q'}`). Direction: backward, one-later-term looking for its one earlier
  rescued index.

These are genuinely different constructions — different certified tool as
the engine (Double-Witness Nested Pigeonhole vs. Critical Prime Dichotomy
branch (b)), different direction of search, different open bridging step.
This is not the same shape as memory rule 6's "duplicate wearing a technique
label" pattern (round 3's minimal-counterexample-vs-forward-induction on the
IDENTICAL gap) — here the intermediate objects produced (a constant divisor
class vs. a specific rescued index) are different enough that it is not
obvious a priori they collapse. This matches exactly the use case
`copy_approach` was built for. APPROVE for build, but the outline's own
mandate — builder's FIRST deliverable must be an explicit equivalence check
against approach 1's step 4 — is correct and must be enforced; if the
builder finds they collapse, RETHINK this slug next round rather than
keeping two names on one fact (single-gap-trap, per CLAUDE.md).

## 3. `a1-3q-subfamily-theorem` (new) — APPROVE with a corrected witness target

**Verified positive:**
- Literal periodicity `a_n = 3q+3(n-1)` from n=1, tested by direct greedy
  simulation (trial-division gcd, not the target formula) for
  `q ∈ {7,11,13,17,19,23,29,31,37,41}`, 40 terms each: EXACT match, zero
  deviation.
- `q=5` exclusion is justified: `a_1=15` genuinely diverges from the
  formula at n=3 (true sequence `15,18,20,24,...` vs claimed
  `15,18,21,24,...`), matching the already-certified Odd-Prime
  Non-Trivialization finding.
- The mod-3 argument for `3∤(a_n+2)` and the `{1,q}`-confinement of common
  factors are correct algebra.

**Falsified (found via direct simulation, blocking this exact proposed
mechanism, per memory rule 5's "test a concrete quantitative lemma before
approving"):**
- The outline's proposed witness "`a_2=3(q+1)` alone always works when
  `q|(a_n+2)`" is FALSE — fails in roughly half the `q`-coincidence cases
  (142/285 at q=7 alone). Root cause: `q` odd ⟹ `q+1` even ⟹ `a_2` even;
  whenever `a_n+2` is also even (n even), `gcd` already picks up factor 2.
  This is a systematic, not edge-case, failure.
- I also tested the natural fallback "fixed pair `{a_2,a_3}`" — ALSO false,
  12 explicit counterexamples across q∈{11,13,19,23,37,43,53,61} where
  neither is coprime to the candidate (e.g. q=13, n=74: gcd with a_2 is 2,
  with a_3 is 5).
- Positive finding to hand the builder: the TRUE minimal witness index
  (found by brute force against the real greedy sequence) stays small in
  every case tested — max index 5 for q≤97, max index 3 for q∈{101,...,809}
  — supporting the outline's own fallback ("bounded search over a few early
  terms") as still viable, just not with the specific candidates named.

This is exactly the situation CLAUDE.md's rigor rules are meant to catch
before a builder wastes a round: the outline's headline claim (a single
named witness) is wrong, but the underlying THEOREM and a corrected,
still-tractable proof strategy survive. I've written the falsification and
the corrected target directly into the seed file
(`a1-3q-subfamily-theorem.md`) so the builder doesn't re-attempt the dead
`a_2`/`{a_2,a_3}` claims. APPROVE for build with this correction; if the
builder cannot find a uniformly bounded witness window for all q, they
should report this honestly as a dead end for this specific technique per
the outline's own instruction, not force an unbounded search.

## 4. `n1-periodicity-reconciliation` (advance) — APPROVE

Low-risk consolidation task, correctly scoped: (1) restrict the round-19
Generalized Class-Blindness Obstruction to the narrower, actually-provable
"ambient/decoupled-from-realized-data" scope the reviewer identified last
round (matches its two certified predecessors' true scope — no overclaim
risk since the outline explicitly instructs stating the narrower coverage),
(2) assemble the floor-deliverable write-up. Neither task opens new attack
surface on H1/H2, both are bookkeeping/audit work building on already-
certified content. No numeric claim to falsify here. APPROVE.

## Diversity check

Approaches 1-2 are two different constructions on the SAME narrowed FAH
existence gap (legitimate per the copy mechanism, but the field still shares
one wall if both fail) — the outliner is correctly treating this as an
intentional parallel-path bet on the strongest live thread, not a
diversity-of-thought violation, since approach 3 (elementary subfamily,
touches neither H1 nor H2) and approach 4 (consolidation) are genuinely
orthogonal. Field composition this round is reasonable: 2 shots at the FAH
crux itself, 1 concrete unconditional floor deliverable, 1 hedge/audit task.
No repeat of a recorded dead end found in any of the 4 (checked against
memory rules and current.md's standing cautions).

## Ranking

Updated via `update_ranking` (13 comparisons), anchoring both newcomers
(`a1-3q-subfamily-theorem` cold-start, `triangle-critical-dichotomy-witness`
copy-inherited) against established approaches including the confirmed
dead-end `core-growth-monotonicity` and the certified-milestone
`prime-power-seed-periodicity-theorem`. Post-update order (best-first):
covering-system-construction (1861) > greedy-exchange-cost-potential (1761)
> n1-periodicity-reconciliation (1673) > prime-power-seed-periodicity-theorem
(1545) > triangle-critical-dichotomy-witness (1530) >
triangle-consistency-pigeonhole (1507) > a1-3q-subfamily-theorem (1497) >
self-absorbing-by-construction (1491) > core-growth-monotonicity (1424).
All `stale` flags cleared.

## Build set

All 4 proposed approaches are sound to build this round, each with the
gap/correction noted above folded into its approach file for the builder to
read first.

build set: triangle-consistency-pigeonhole, triangle-critical-dichotomy-witness, a1-3q-subfamily-theorem, n1-periodicity-reconciliation
