# Round 6 proof-reviewer report — imo-2026-06

## Scope
Reviewed all three built slugs (`covering-system-construction`,
`greedy-exchange-cost-potential`, `recruitment-round-charging`), all certified
lemmas depended upon, and this round's explorer/outliner/outline-reviewer reports.
Independently reimplemented the entire pipeline (greedy generation, base/extended
types, persistence detection, canonical witnesses, rogue-pair/FAH/Symmetric-FAH
checks) from scratch in Python (no shared code with any builder) and ran it on 7
seeds (175, 187, 209, 385, 4807, 6851, plus a fresh spot-check).

## Headline verification results

**1. Projection Lemma + Collateral-Safety Theorem (`covering-system-construction`,
Step 8.1–8.2) — VERIFIED CORRECT, certified.** Line-by-line re-derivation confirms:
Projection Lemma is a one-line set identity (ρ(n)=ρ₁(n)∩S₀); Collateral-Safety
correctly composes it with the already-certified Monotonicity of Resolution Lemma.
No gap, no hidden hypothesis. This genuinely and unconditionally closes round 5's
"collateral rogue pairs" gap (the risk that one recruitment round could spawn new
rogue pairs among previously-safe base-type pairs cannot happen). Step 8.3's
reduction of (†) to a monotone sequence open(k) over a fixed finite set of
≤ C(|𝒫|,2) base-type pairs is likewise correct (direct consequence of the
Corollary). Certified: `lemmas/projection-lemma.md`, `lemmas/collateral-safety-
theorem.md`.

**2. Step 8.5's conditional theorem (Symmetric FAH ⟹ termination in one round) —
VERIFIED CORRECT as a conditional implication.** Re-derived Case 1 (Monotonicity)
and Case 2 (Projection + Symmetric FAH placing q_i in both A'' and B'' via
cofinite-tail arguments) independently; no unstated assumption found. The builder's
own honest flag — that the sibling's literal one-sided FAH is NOT enough for Case 2,
and a symmetric (two-sided) strengthening is needed — is correct and well-argued.

**3. Important correction to the builders' own bookkeeping: Symmetric FAH already
has empirical support in the workspace.** `covering-system-construction` states it
has not verified Symmetric FAH computationally. But `greedy-exchange-cost-
potential`'s own Step 0 "B'-side" check (every B'-occurrence after n_B divisible by
q) is, once one notes n_B is B's own minimal witness (so no B'-occurrence exists in
(n_A,n_B), and q|a_{n_B} already holds by Lemma G), EXACTLY an empirical check of
Symmetric FAH — 0 failures across all 7 of that file's seeds. Neither builder
noticed this equivalence; recorded in current.md.

**4. Independent 4th-implementation reconfirmation of FAH, Symmetric FAH, and the
critical |F'|=2 falsification.** Ran a from-scratch script (no shared code) on
a_1=187, 209, 385, 4807:
- a_1=4807: reconfirmed the exact rogue pair (A'={3,5,19} at n=6, B'={2,11} at n=7,
  F'={13,17}, Lemma-G prime q=17, a_6=4845=3·5·17·19, a_7=4862=2·11·13·17) —
  matching the explorer's and outline-reviewer's numbers exactly (now a 4th
  independent confirmation of the Universal Singleton Hypothesis falsification).
  FAH and Symmetric FAH both hold with 0 failures (checked to n=15000; the A'-type
  {3,5,19} recurs periodically — 20 occurrences by n=15000 — confirming it is a
  genuine persistent type, not a fluke).
- a_1=187, 209, 385: FAH and Symmetric FAH both hold with 0 failures on every rogue
  pair found (matches prior rounds' reports).
- Note: my implementation did NOT reproduce a rogue pair for a_1=4807 at the
  "one-round" S₀ used by `recruitment-round-charging`'s own script (that file
  flagged the identical discrepancy itself, attributing it to a tail-window
  persistence-detection heuristic mismatch, not a retraction) — resolved by
  extending N and the persistence-detection window, at which point the pair
  reappears exactly as reported. Not a genuine counterexample; a detection-
  threshold artifact, now explained.

**5. `recruitment-round-charging`'s batch-resolution finding — independently
reconfirmed.** Reran the pipeline on a_1=6851 (Q={13,17,31}): found 10 distinct
rogue extended-type pairs, ALL sharing the same recruited prime 5 — matches the
builder's report of "4 simultaneous rogue pairs, all resolved by prime 5" (I found
more pairs at a larger N, but the "all share one prime" qualitative finding holds).
The builder's **Hub Singleton Batch Lemma** (certified: `lemmas/hub-singleton-
batch-lemma.md`) is a correct, if trivial, corollary of Lemma G. The builder's
honest finding that 16/19 sampled hub instances have |F'_H|=2 with the same element
always picked is correctly diagnosed as reducing to the shared FAH question, not an
independent route.

**6. Lemma I (`greedy-exchange-cost-potential`) — sound as a diagnostic, NOT
certified as a portable lemma.** Independently checked each of the four cited tools'
proofs (Free Facts, Generalized Bounded Witness Lemma, Gap Lemmas, Critical Prime
Dichotomy) and confirmed none contains an identity-forcing step — the exhaustive-
inspection argument is correct. But, matching the round-3 precedent for Lemma F
("minimality bounds magnitude, not type," also not certified), this is a statement
about the CURRENT certified toolkit, not a lemma that remains true independent of
what gets certified later — recorded in current.md as guidance, not certified as a
standalone file.

## Verdicts (independent, per-approach)

- **covering-system-construction: CHANGES REQUESTED (partial).** Substantial
  verified progress (Projection Lemma, Collateral-Safety Theorem both certified);
  gap now pinned exactly to FAH + Symmetric FAH (both open, well-supported).
- **greedy-exchange-cost-potential: CHANGES REQUESTED (partial).** Correctly
  retired Universal Singleton Hypothesis (independently reconfirmed), extended FAH's
  empirical base (independently reconfirmed), three honest failed proof attempts,
  Lemma I recorded as valid guidance (not certified as portable).
- **recruitment-round-charging: RETHINK.** All three charging candidates now
  confirmed to either dead-end or reduce to the shared FAH crux; the charging
  framing itself cannot deliver an independent route as scoped. One small certified
  lemma (Hub Singleton Batch) and a genuinely reconfirmed empirical finding
  (batch resolution) are real contributions, but per CLAUDE.md's RETHINK criterion
  ("the approach can't work as set up"), this approach should not continue as a
  charging variant — if revived, it needs a framing genuinely far from recruitment-
  round charging.

## Lemmas certified this round
- `lemmas/projection-lemma.md`
- `lemmas/collateral-safety-theorem.md`
- `lemmas/hub-singleton-batch-lemma.md`

## current.md
Fully updated: Status line, new ROUND 6 section (Projection Lemma, Collateral-Safety
Theorem, the base-type-pair-level reduction, the FAH/Symmetric-FAH empirical
cross-check finding, Lemma I assessment, recruitment-round-charging assessment),
lemma certification list, per-approach verdicts, and next-round guidance.

## Next-round guidance (headline)
Priority 1 is now sharply focused: prove FAH and/or Symmetric FAH (equivalent in
observed empirical strength — every tested seed satisfies both). Do not re-attempt
the three proof mechanisms Lemma I shows fail (Lemma H branch analysis, inductive
chaining, exchange/minimality built from the current certified toolkit alone); a
genuinely new mechanism converting existential per-occurrence facts into uniform
identity claims is needed. `recruitment-round-charging`, if continued, must pivot to
a framing genuinely different from a charging/potential argument over the
recruitment process.
