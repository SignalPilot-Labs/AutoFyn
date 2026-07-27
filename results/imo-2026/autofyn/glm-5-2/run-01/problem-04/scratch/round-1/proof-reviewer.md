# proof-reviewer — IMO 2026 P4 (`imo-2026-04`), round 1

Problem: characterize `θ ∈ (0°,180°)` for which Mulan guarantees victory in
finitely many steps. Conjectured answer: `θ = 180°/n`, integer `n ≥ 2`.

I read all three built approaches fully and adversarially, re-derived the
load-bearing identities from scratch (symbolic + numeric simulation), and
checked the four-case exhaustiveness, Lemma R's positivity descent, Lemma F's
interval bound, and the `n=2` base against obtuse/acute openings.

## Independent verification performed

- **Four-case telescoping** (sympy): the four linear combinations of `γ` reduce
  to `C, A, B, 180°` exactly. Cases (i)–(iv) are exhaustive (each child's bad
  angle is one of two named new angles) and each yields a genuine contradiction.
- **Sufficiency simulation** (worst-case Shan-Yu keeps the child that delays
  the win): `n=2,3,4,5`, 2000 random triangles each → 0 failures, max moves =
  `n−1` in every case. Confirms Lemma R + Lemma F + `n=2` special move.
- **Necessity simulation** (Shan-Yu: equilateral + keep safe child; Mulan:
  random cuts): 9 non-integer `180/θ` values (`50°,72°,80°,100°,120°,70°,7°,33°,55°`)
  each survive 500 rounds without ever hitting `θ`, and the closure (≥1 safe
  child) is never violated.
- **Chip-transfer dead-end arithmetic**: the `q=(3,2,3)` fixed point actually
  arises from cutting index 0 (cyclic transition `(q_C, q_A−1, q_B+1)`), NOT
  index 2 as the approach writes (cutting index 2 gives `(2,2,4)`). The
  approach has the two indices swapped. The dead-end conclusion (no strict
  monovariant — a greedy fixed point exists) still stands.

## Verdicts

### `direct-four-case-interval`: APPROVE — Status solved

Complete and rigorous, both directions. Every load-bearing claim verified:

- **Four-case closure (necessity)**: cases disjoint and exhaustive; each
  telescoping identity confirmed; the `k_i ≥ 1` positivity (from `0 < γ < C` and
  `B_θ`-membership) is correctly invoked to turn "is an integer multiple of
  `θ`" into "is in `B_θ`". The logical structure (disjunction of four
  conjunctions, each contradicting) is valid even when a child has two bad
  angles.
- **Equilateral safety**: `60° = kθ ⇒ 180/θ = 3k ∈ ℤ`; clean.
- **Lemma R (induction on `m`)**: base `m=1` trivial; step `m≥2` legality
  `θ < mθ`; `T2` validity with the bound `A+θ < 180°−(m−1)θ ≤ 180°−θ < 180°`,
  re-established at every level (the two non-split angles sum to `180°−jθ` at
  level `j`). Airtight for ALL configurations Shan-Yu could force: whichever
  child is kept, either carries `θ` (immediate) or carries `(m−1)θ` at a clean
  vertex angle (iterable). Confirmed by simulation.
- **Lemma F**: `C ≥ 60° ≥ θ` (largest angle, `n≥3`); `C ≠ θ` so `C > θ`,
  `C/θ > 1`; interval-contains-integer; `k ∈ {1,…,n−1}` from
  `k < (A+C)/θ = n − B/θ < n`. Both `p1=(n−k)θ`, `p2=kθ` in `B_θ`. The chosen
  child does carry a strictly-smaller-index multiple of `θ` regardless of
  which triangle Shan-Yu keeps (both children carry one). Confirmed.
- **`n=2` base**: covers right (0 moves), acute, and obtuse openings; the
  `A,B < 90°` claim holds in both acute (all `<90°`) and obtuse (only `C ≥ 90°`)
  cases; `γ = 90°−A ∈ (0,C)` verified for both. Both `P`-angles equal `90°`.
- **Tightness**: attainment (each `n` works) + upper bound (every other `θ`
  fails) both present and constructive. Final answer stated explicitly.

No gaps. The proof is complete and correct. Headline proof.

### `attractor-level-fixpoint`: APPROVE — Status solved

Same engine as `direct-four-case-interval` (one-move transition, four-case
closure §2, Lemma R §3, Lemma F §3, `n=2` base §3, combine). All the
load-bearing steps are present and correct, identical in substance to the
headline proof.

The **distinctive §5 "determinacy / no-draw dichotomy"** is correct but
redundant: it observes that the partition `180/θ ∈ ℤ` vs `∉ ℤ` is exhaustive
and mutually exclusive, and in each case one player has an explicit strategy
(proven in §3 and §4). The "no draw" is therefore an automatic consequence of
the two proven implications + the law of excluded middle — it is not a new
theorem and invokes no transfinite determinacy result (correctly, since none
is needed: the question is only whether *Mulan* guarantees victory, witnessed
by a single Shan-Yu strategy in the `∉ ℤ` case). The extra fixed-point
language (`W = X \ S_θ` when `∉ ℤ`, via "Lemma R uses only `mθ < 180`") is
also correct — Lemma R's positivity bound `A+θ < 180°−(m−1)θ` genuinely does
not require `n` to exist. No gap introduced.

Equivalent in substance to the headline; I keep `direct-four-case-interval`
as the headline only because it is cleaner (no redundant framing).

### `chip-transfer-monovariant`: CHANGES REQUESTED — Status partial

Honest self-assessment (Status `partial`); the builder's recorded status is
accurate.

**Correct proven content:**
- **Theorem N (necessity in `q`-space)**: this IS the four-case closure,
  correctly re-derived in residue language. Rigorous. (Same algebra as the
  direct approach — the builder is upfront that it is not a rival engine.)
- **Lemma FRAC** (fractional-part 3-cycle of the forced `t=1` transfer): a
  genuine, correctly-proven invariant of the forced-dynamics sub-game, with
  an honest caveat that it does not by itself prove the escape (Mulan may play
  `t ≠ 1`). Correct.

**Gaps / issues:**
1. **Sufficiency conceded** (the headline gap): no transfer-specific
   monovariant exists. The bare greedy `t=1` transfer is a verified dead-end;
   smart `t=1` play's descent *is* Lemma R, not a new potential. The approach
   points the reader at `direct-four-case-interval` for sufficiency. So the
   approach does not independently solve the whole problem — one direction is
   borrowed.
2. **Minor labeling error in the dead-end illustration**: the approach writes
   that cutting index 2 of `q=(3,2,3)` gives the fixed point `(3,2,3)` and
   cutting index 0 gives `(2,2,4)`. The reverse is true: the transition
   `(q_B, q_C−1, q_A+1)` (cutting index 2) gives `(2,2,4)`, while the cyclic
   analogue cutting index 0 gives `(3,2,3)`. The dead-end *conclusion* (a
   greedy fixed point exists, so no strict non-negative-integer monovariant)
   is still valid, but the illustrative arithmetic is muddled and should be
   corrected.

Since the distinctive technique (transfer monovariant) is a verified dead-end
and the necessity is a restatement of the shared four-case engine, the
approach cannot independently reach `solved`. It is a genuine `q`-space
cross-check with one real micro-invariant (Lemma FRAC). The gap to close for
promotion would be an independent sufficiency engine, which the builder has
already shown is not forthcoming via the transfer route — so re-dispatching
the builder to "close more" is unlikely to help; the route is effectively a
dead-end as a *standalone* proof, though its certified lemmas (Theorem N,
Lemma FRAC) remain useful to the population.

## Lemmas certified into `results/imo-2026-04/lemmas/`

- `four-case-closure.md` — admitted (proved, statement correct, not
  over-strong). From attractor §2 / chip-transfer Theorem N / direct §I.1.
- `lemma-R-multiple-descent.md` — admitted. Positivity bound airtight;
  statement correctly notes it needs only `mθ < 180°` (not `n`).
- `lemma-F-reach-multiple.md` — admitted. Interval bound and `k`-range correct.
- `interval-contains-integer.md` — admitted (standard, correctly proved).
- `lemma-FRAC.md` — admitted. Genuine invariant; correctly caveated as not a
  standalone escape.

Rejected: the attractor's "constructive no-draw dichotomy" is not certified
as a separate lemma — it is a restatement of the main theorem (problem-specific,
not a reusable general tool), not a new lemma.

## Summary

- `direct-four-case-interval`: **APPROVE** — Status solved.
- `attractor-level-fixpoint`: **APPROVE** — Status solved.
- `chip-transfer-monovariant`: **CHANGES REQUESTED** — Status partial
  (necessity rigorous but shared; sufficiency conceded as dead-end; minor
  dead-end labeling error to fix).

The problem is **solved**. Headline proof = `direct-four-case-interval`,
written into `current.md` under `## Full proof`.
