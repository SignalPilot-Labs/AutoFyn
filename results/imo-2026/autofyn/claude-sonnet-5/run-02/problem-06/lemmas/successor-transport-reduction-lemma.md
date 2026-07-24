## Lemma: Successor-Transport Reduction Lemma (certified)

**Source.** `greedy-exchange-cost-potential`, round 9. Independently re-verified by
the proof-reviewer (round 9).

**Depends on (certified).** `generalized-bounded-witness-lemma.md`,
`extended-earliest-witness-intersection.md` (Lemma G).

**Setup.** Let `(A',B')` be a rogue pair (disjoint `S₀`-extended-persistent types)
with earliest witnesses `n_A, n_B` (Lemma G) and `q* ∈ F' ∩ F''` any fixed prime of
the certified-nonempty intersection. Let `n_1 < n_2 < ...` enumerate all indices
`n > max(n_A,n_B)` with `ρ(n) = A'` (infinite, since `A'` is extended-persistent).

**Lemma.** Suppose:
(i) `q* | a_{n_{j_0}}` for at least one `j_0` (guaranteed unconditionally: the
Generalized Bounded Witness Lemma's Corollary gives, via infinite pigeonhole,
infinitely many such `j_0`); and
(ii) [**the Successor Claim**, an open hypothesis, NOT proved by this lemma] there
is `J` such that for all `j ≥ J`, `q*|a_{n_j} ⟹ q*|a_{n_{j+1}}`.
Then `q* | a_{n_j}` for all sufficiently large `j` — i.e. Cofinite FAH holds for this
pair and this `q*`.

**Proof.** By (i), `D := {j : q*|a_{n_j}}` is nonempty (in fact infinite, though only
nonemptiness is used). Since `D` is infinite and `J` is a fixed finite threshold,
some `j_0 ∈ D` has `j_0 ≥ J`. By (ii), applied repeatedly (ordinary induction on
`k ≥ 0`): `q*|a_{n_{j_0}} ⟹ q*|a_{n_{j_0+1}} ⟹ ... ⟹ q*|a_{n_{j_0+k}}` for every
`k ≥ 0`. Hence `q*|a_{n_j}` for every `j ≥ j_0`, i.e. all but finitely many `j`. ∎

**Scope.** Converts a bare "eventual one-step successor implication" claim (the
Successor Claim, still open) directly into the Cofinite FAH target, which the
certified Cofinite Sufficiency Lemma (`cofinite-sufficiency-lemma.md`) already
proves sufficient for the whole proof's finish. Purely a reduction: assumes nothing
about FAH itself, only converts hypothesis (ii) (if ever proved) into the conclusion.
Does not prove the Successor Claim — `greedy-exchange-cost-potential` Step 3 (round
9) shows both available routes to it (Critical Prime Dichotomy on the failing
occurrence; Free Facts on the two consecutive same-type occurrences) currently stall.

**Status.** Correct, complete, no gaps, unconditional modulo the stated hypothesis
(ii) (Successor Claim), which remains open and unproved. Independently re-derived by
the reviewer (elementary induction, verified step by step). Certified as a
standalone reusable conditional lemma.
