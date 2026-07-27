## Goal

Solve IMO 2026 Problem 4 (`imo-2026-04`): characterize the real values of θ (0°<θ<180°)
for which Mulan can guarantee victory in finitely many steps, no matter how Shan-Yu
plays. Problem is `compute_and_prove`, `answer_type: characterization`.

- Metric: proof-reviewer verdict on the candidate proof. Headline signal = a `solved`
  (APPROVE) in `results/imo-2026-04/current.md` `## Status`, plus approach Elo in
  `results/imo-2026-04/approaches/.ranking.json`.
- Eval command: read `results/imo-2026-04/current.md` `## Status` and
  `results/imo-2026-04/approaches/.ranking.json` (top Elo + live count).
- Baseline: no approaches, no proof yet (round 1).
- Target: `solved` — complete rigorous proof naming the exact set of θ, both directions
  ("Mulan wins" for θ in the set, "Shan-Yu escapes" for all other θ), all cases covered.
- Constraint: rigor rules in CLAUDE.md. For a characterization: prove upper bound AND
  construct attaining examples; verify the answer is tight.

## Goal Updates

- [2026-07-23] User explicitly named "IMO Problem 4" (the Shan-Yu/Mulan paper-triangle
  game). This overrides the CLAUDE.md "hard-only" default — `imo-2026-04` is
  `difficulty_level: medium` (rating 7) but is the user's target. Attack it.

## Eval History

- [Round 1] BREAKTHROUGH. `current.md` ## Status = **solved**. Reviewer APPROVE
  on 2 approaches. Answer: Mulan wins ⇔ 180°/θ ∈ ℤ (θ = 180°/n, n≥2 integer:
  {90°,60°,45°,36°,30°,…}). Ranking Elo: direct-four-case-interval 1531
  (verified-milestone, headline), attractor-level-fixpoint 1500 (verified-milestone,
  equivalent engine), chip-transfer-monovariant 1469 (partial — necessity rigorous
  in q-space, sufficiency conceded). Both directions proven: necessity via four-case
  closure of B_θ-free safe set S_θ + equilateral universal witness (60=kθ ⟹
  180/θ=3k∈ℤ contradiction); sufficiency via Lemma R (mθ→(m−1)θ induction, ≤n−1
  moves) + Lemma F (interval of length C/θ>1 contains integer) + n=2 (θ=90°) base
  move γ=90−A. Verified symbolically (sympy: four telescoping identities reduce to
  C,A,B,180°) + simulation (n=2,3,4,5 ×2000 random triangles, worst-case Shan-Yu,
  0 failures; non-integer escape survives 500 rounds ×9 θ values). 5 lemmas
  certified in `lemmas/`.

## Rules

- ALWAYS: for a characterization problem (answer_type: characterization), prove BOTH
  directions and verify tightness — attainment example AND upper bound (because
  round-1 solved required both, CLAUDE.md rigor rules, round 1).
- ALWAYS: when an explorer conjectures an answer set, sanity-test boundary values
  before committing builders (equilateral-safe check `60=kθ ⟹ 180/θ=3k∈ℤ` was the
  hinge that confirmed the necessity witness, round 1).
- NEVER: build near-duplicate approaches sharing one engine — outline-reviewer
  correctly refused `modular-residue-orbit` as a single-gap-trap restatement of the
  four-case closure (CLAUDE.md single-gap trap, round 1).
- ALWAYS: record a verified dead-end with its counterexample — chip-transfer's
  bare `t=1` transfer op cycles at `q=(3,2,3)` (cut index 0), so no strict transfer
  monovariant exists; future rounds must not retry that engine (round 1).

## State

Done (round 1): IMO 2026 P4 SOLVED. Conjecture θ=180°/n (n≥2) confirmed and proven
both directions; 2 APPROVE approaches, headline proof in `current.md`, 5 certified
lemmas. Reviewer cross-checked two independent framings (direct four-case + attractor
fixed-point) — same engine, both APPROVE. chip-transfer partial (necessity only).
Next: if a future round wants deeper rigor, harden chip-transfer's sufficiency via a
non-greedy potential or fold it; otherwise the run is complete.
