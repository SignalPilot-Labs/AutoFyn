# Goal

Solve **imo-2026-04** (Mulan's Triangle Game, IMO 2026 P4). Produce a complete, rigorous
prose proof characterizing exactly which θ (0° < θ < 180°) let Mulan guarantee victory in
finitely many steps, no matter how Shan-Yu plays. `task=compute_and_prove`,
`answer_type=characterization` — must state the answer set explicitly AND prove both
directions (Mulan wins for θ in the set; Shan-Yu survives forever otherwise).

- Metric: proof-reviewer verdict on `results/imo-2026-04/current.md`.
- Eval: proof-reviewer APPROVE ⇒ Status `solved`; else `partial`/`unsolved` + ranking.
- Baseline (round 1): unsolved, no approaches, empty population.
- Target: Status `solved`, complete correct characterization with both directions proven.
- Constraint: full rigor per CLAUDE.md rigor rules (no skipped cases, upper bound + construction).

# Goal Updates

- [2026-07-24] User: solve imo-2026-04 (Mulan's Triangle Game). Base goal set above.

# Eval History

- Round 1 baseline: no approaches, Status unsolved.
- Round 1 result: **BREAKTHROUGH — SOLVED.** Status `solved`. Answer: Mulan wins iff θ = 180°/n,
  integer n ≥ 2 (θ divides 180° evenly: 90,60,45,36,30,180/7,...). Two independent proofs both
  APPROVE'd by proof-reviewer (re-derived + numerically confirmed, n=2..12 + adversarial sim):
  - residue-invariant (Elo 1531): necessity via mod-θ 4-coincidence exclusion (Lemma A);
    sufficiency via alignment+peel. Cleanest.
  - geometric-forcing-extremal (Elo 1500): raw-degree; non-obtuse invariant (θ>90) + fixed-sum
    covering Lemma D (θ≤90 non-div); sufficiency Lemma E/F.
  - q-linear-independence (Elo 1469): registered, not built (redundant/highest-risk).
  current.md holds Full proof; lemmas certified into results/imo-2026-04/lemmas/.

# Rules

- ALWAYS run the proof-reviewer as the gate even when builders self-report `solved` (both did
  round 1; reviewer independently confirmed) (because self-assessment is untrusted, round 1).

# State

## Done
- Round 1: setup env; explored (3 routes, converged on θ=180/n); outlined 3 rival approaches;
  reviewer gated/ranked; built 2; proof-reviewer APPROVE'd both → SOLVED.

## Broken
- (none)

## Next
- Goal achieved. If more rounds run: optionally consolidate the two proofs / harden exposition,
  or build q-linear-independence for a third independent confirmation. No new work required.
