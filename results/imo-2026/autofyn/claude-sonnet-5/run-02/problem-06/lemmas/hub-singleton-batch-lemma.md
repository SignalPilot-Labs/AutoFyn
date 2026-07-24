## Lemma: Hub Singleton Batch Lemma (certified)

**Source.** `recruitment-round-charging`, round 6 (new approach). Independently
spot-checked by the proof-reviewer (round 6) on a fresh seed (a_1 = 6851), which
reproduced the qualitative pattern (multiple simultaneous rogue pairs at a hub type,
all resolved by the same prime).

**Depends on (certified).** `extended-earliest-witness-intersection.md` (Lemma G).

**Statement.** Let H be an S₀-extended-persistent type that is simultaneously rogue
against several distinct partners X₁, ..., X_r (disjoint base types, pairwise
non-intersecting at the S₀ level), with H's own earliest occurrence n_H fixed across
all these pairings (n_H depends only on H, not on the partner). For each i, let q_i be
a Lemma-G prime for the pair (H, X_i) (dividing both a_{n_H} and a_{n_{X_i}}, outside
S₀). If |F'_H| = 1, where F'_H := P(a_{n_H}) \ S₀, then q_i equals the unique element
of F'_H for every i — a single recruited prime resolves all of H's simultaneous rogue
relationships at once.

**Proof.** By Lemma G applied to (H, X_i), q_i ∈ P(a_{n_H}) \ S₀ = F'_H for every i
(q_i divides a_{n_H} and q_i ∉ S₀ by Lemma G's own construction). If |F'_H| = 1, F'_H
has only one element, so q_i must equal it, for every i. ∎

**Scope.** A trivial but genuine corollary of Lemma G: it upgrades "some Lemma-G prime
resolves each pair separately" to "the same prime resolves all pairs at once,"
conditional only on the hub's own witness having a singleton outside-core factor set
(a strictly weaker, local condition than the retired Universal Singleton Hypothesis,
which required this for every rogue-pair witness, not just hub witnesses with |F'_H|=1).
Does **not** hold in general when |F'_H| ≥ 2: `recruitment-round-charging`'s round-6
scan found 16/19 sampled hub instances have |F'_H| = 2, and in every one, empirically,
the SAME one of the two candidate primes is picked by every partner — but this
stronger fact is not derivable from Lemma G alone and reduces to the same open
Full-Absorption Hypothesis question (see `current.md`), not something this Lemma
establishes.

**Status.** Correct, complete, no gaps, unconditional (for the |F'_H| = 1 case as
stated). Certified as a standalone reusable lemma, though narrow in scope — it does
not, by itself, resolve the general batch-resolution question.
