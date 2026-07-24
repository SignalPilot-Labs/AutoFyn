## Lemma G: Extended Earliest-Witness Intersection (certified)

**Source.** `greedy-exchange-cost-potential`, round 4, "New Lemma G (Extended
Earliest-Witness Intersection)". Independently re-verified by the proof-reviewer
(round 4) — the proof is a direct, one-step application of the certified Free Facts
lemma and does not depend on any specific numerical example (see reviewer note below
on a computational bug affecting this file's *motivating example*, which does not
affect this abstract Lemma's proof).

**Depends on (certified).** `free-facts-gcd.md`.

**Statement.** Let S₀ ⊇ Q be any fixed finite set of primes, ρ(n) := P(a_n) ∩ S₀, and
let A', B' ⊆ S₀ be two S₀-extended-persistent types (each occurring for infinitely
many n) with A' ∩ B' = ∅. Let n_A := min{n : ρ(n) = A'} and n_B := min{n : ρ(n) = B'}
(both exist and are finite). Then there is a prime q ∉ S₀ with q | a_{n_A} and
q | a_{n_B} simultaneously.

**Proof.** Both A', B' are nonempty (Q ⊆ S₀ and Free Facts force P(a_n) ∩ Q ≠ ∅ for
n ≥ 2, and ρ(1) ⊇ Q ≠ ∅), and distinct (A' ∩ B' = ∅ with both nonempty), so
n_A ≠ n_B (ρ(n_A) = A' ≠ B' = ρ(n_B)). By the Free Facts lemma, gcd(a_{n_A}, a_{n_B}) > 1,
so some prime p divides both a_{n_A} and a_{n_B}. If p ∈ S₀, then
p ∈ P(a_{n_A}) ∩ S₀ = ρ(n_A) = A' and p ∈ P(a_{n_B}) ∩ S₀ = ρ(n_B) = B', so
p ∈ A' ∩ B' = ∅, a contradiction. Hence p ∉ S₀; take q := p. ∎

**Scope.** Strictly generalizes the certified F_A ∩ F_B ≠ ∅ lemma
(`canonical-witness-intersection.md`) from base-type canonical witnesses to arbitrary
S₀-extended-persistent types via their own earliest occurrences. Gives a *symmetric*
pair of witness indices (both n_A and n_B carry the shared prime q), unlike the
certified Generalized Bounded Witness Lemma's Corollary, which only certifies
recurrence of a shared prime on one side.

**Status.** Correct, complete, no gaps, unconditional. Certified as a standalone
reusable lemma. **Caution for future use:** any numerical example illustrating this
lemma (or built on top of it) must compute S₀ and the extended-persistent-type set 𝒫'
using the *literal, minimal* canonical-witness convention (earliest occurrence of each
base/extended type, not a witness sampled from deep in a simulation's tail window) —
see the round-4 proof-reviewer's report for a documented instance (a_1 = 175) where a
non-minimal witness choice produced an incorrect S₀ and a spurious "rogue pair" that
does not exist under the correct, minimal S₀.
