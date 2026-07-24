## Lemma: Cofinite Sufficiency Lemma (certified)

**Source.** `cofinite-window-capacity-bound`, round 9. Independently re-verified by
the proof-reviewer (round 9).

**Depends on (certified).** `free-facts-gcd.md`, `extended-persistent-type-pigeonhole.md`,
`projection-lemma.md`, `monotonicity-of-resolution.md`, `collateral-safety-theorem.md`,
`extended-earliest-witness-intersection.md` (Lemma G).

**Setup.** Fix stage `k` of the S₀-recruitment process, a currently-rogue disjoint
base-type pair `(A,B)` with `S₀ := S₀^{(k)}`. For any pair of disjoint-base-type
`S₀`-extended-persistent refinements `A', B'` of `A, B` (so `A' ∩ B' = ∅`), with
witnesses `n_A < n_B` and canonical prime `q* := min(F' ∩ F'')` (nonempty by Lemma G),
define the exception sets
`E := {n > n_B : ρ(n) = A', q* ∤ a_n}`, `E_sym := {n > n_A : ρ(n) = B', q* ∤ a_n}`.

**Theorem.** If, for every currently-rogue extended-type pair `(A',B')` refining
every currently-rogue base-type pair `(A,B)` at stage `k`, both `E` and `E_sym` are
finite ("Cofinite FAH"), then batch-recruiting the canonical prime `q*` of every such
pair in one round (`S₁ := S₀ ∪ {q* : (A',B') \text{ rogue at } S₀}`, a finite union
since there are finitely many `Q`-persistent base types hence finitely many
extended-persistent refinement pairs at any fixed `S₀`) makes every base-type pair
that was rogue at stage `k` fully safe at `S₁`: every pair of `S₁`-extended
refinements `A'', B''` of any such `(A,B)` satisfies `A'' ∩ B'' ≠ ∅`.

**Proof.** Fix such `A,B` and `S₁`-extended refinements `A'', B''`. By the certified
Projection Lemma, `A' := A'' ∩ S₀`, `B' := B'' ∩ S₀` are `S₀`-extended-persistent
refinements of `A, B`, and `A'' ⊇ A'`, `B'' ⊇ B'`.

- If `A' ∩ B' ≠ ∅`: then `A'' ∩ B'' ⊇ A' ∩ B' ≠ ∅`. Done.
- If `A' ∩ B' = ∅`: then `(A',B')` is itself a rogue extended pair at `S₀`, with its
  own canonical prime `q*_{A',B'} ∈ S₁` (recruited in the batch step). By hypothesis
  `E_{A',B'}` is finite; let `N₀` be its max element (or `n_B` if empty). Since `A''`
  is `S₁`-extended-persistent it has infinitely many occurrences, so some occurrence
  `n* > N₀` exists. By the Projection Lemma (applied in the direction `A' = A'' ∩ S₀`),
  `ρ_{S₀}(n*) = A'`, so `n* ∉ E_{A',B'}` (as `n* > N₀`), giving `q*_{A',B'} | a_{n*}`.
  Hence `q*_{A',B'} ∈ P(a_{n*}) ∩ S₁ = A''`. By the symmetric argument using `E_sym`
  finite, `q*_{A',B'} ∈ B''` too. So `A'' ∩ B'' ⊇ {q*_{A',B'}} ≠ ∅`. ∎

**Scope.** This licenses replacing the literal-FAH target (`E = E_sym = ∅`) with the
strictly weaker cofinite target (`E, E_sym` finite) inside the certified
CRT/cyclic-pigeonhole finish (`covering-system-construction` Step 8.5), which uses
this Theorem verbatim in place of its own literal-FAH case split. Does not itself
prove Cofinite FAH — purely a reduction, non-circular (assumes nothing about FAH,
only the hypothesis it is conditioned on).

**Status.** Correct, complete, no gaps, unconditional modulo its stated hypothesis
(Cofinite FAH), which remains open. Independently re-derived by the reviewer
(re-checked both branches of the case split and the batch-recruitment finiteness
claim). Certified as a standalone reusable conditional lemma.
