## Lemma: Singleton-Side FAH (certified)

**Source.** `covering-system-construction`, round 8, Step 8.9. Independently
re-verified by the proof-reviewer (round 8).

**Depends on (certified).** `generalized-bounded-witness-lemma.md`,
`extended-earliest-witness-intersection.md` (Lemma G, for producing the rogue-pair
setup this lemma is stated relative to).

**Setup.** Fix a rogue pair of disjoint-base-type extended-persistent types (A', B')
at core S₀, with witnesses n_A, n_B (any valid witnesses — n_A with ρ(n_A) = A', n_B
with ρ(n_B) = B', WLOG n_A < n_B). Let F' := P(a_{n_A}) \ S₀, F'' := P(a_{n_B}) \ S₀.

**Theorem.** If F'' is a singleton, F'' = {q}, then q | a_n for EVERY n > n_B with
ρ(n) = A' — not merely cofinitely many such n, literally all of them, zero
exceptions. Symmetrically, if F' is a singleton, F' = {q'}, then q' | a_n for every
n > n_A with ρ(n) = B'.

**Proof.** By the certified Generalized Bounded Witness Lemma applied with the fixed
witness index m := n_B (ρ(n_B) = B'): for every n > n_B with ρ(n) = A', a_n is
divisible by some prime of the fixed finite set F'_{A',B'} := P(a_{n_B}) \ S₀ = F''.
Since F'' = {q} has exactly one element, that prime must be q itself. So q | a_n for
every such n, with no exceptions (the Generalized Bounded Witness Lemma's conclusion
already holds for ALL n > m of the given type, not merely infinitely many, so no
further pigeonhole step is needed once F'' is a singleton). The symmetric statement
follows by the identical argument with the roles of A', B' (and n_A, n_B) exchanged. ∎

**Scope.** This is a genuine unconditional special case of Joint FAH / Symmetric
FAH: whenever the "far side" witness's outside-core factor set has exactly one
element, full absorption on the corresponding near side is immediate and requires no
new mechanism — it is a direct corollary of an already-certified lemma with no
additional pigeonhole or divisor-chain argument.

**Why this matters for the workspace.** Every rogue-pair example used as
computational support for FAH/Symmetric FAH through round 8 (a_1 = 187, 209) has
F' = F'' = {singleton} on both sides, so this Lemma alone fully explains all of that
positive evidence — none of it engages the genuinely open |F'|, |F''| ≥ 2 regime.
An independent computation on a_1 = 4807 at an un-recruited core (S₀ = Q, before the
Finite Core Theorem's own recruitment), where F' = {17,3,5} and F'' = {17,2,13}
(neither a singleton), found only ~6% (50–74 out of roughly 800–1200 sampled
occurrences, across two independently reproduced runs) of later A'-type terms
divisible by the shared prime 17 — confirming the general (non-singleton) case is
NOT covered by this lemma and remains the genuinely hard, open part of Joint FAH.

**Status.** Correct, complete, no gaps, unconditional (conditional only on the
already-certified Generalized Bounded Witness Lemma and the existence of a rogue
pair with a singleton far-side factor set — not on any open hypothesis).
Independently re-derived by the reviewer; independently re-verified the two
supporting computational examples (a_1=187: F'=F''={7}, 0 exceptions in 46+
occurrences; a_1=4807 non-singleton case: ~74/1200 divisible, confirming the general
case is genuinely different and unresolved). Certified as a standalone reusable
lemma.
