## Divisor-Restricted Pigeonhole (Lemma J) — CERTIFIED, round 7

**Source.** `greedy-exchange-cost-potential`, round 7.

**Depends on.** The certified Generalized Bounded Witness Lemma
(`generalized-bounded-witness-lemma.md`) and the infinite pigeonhole principle
(`knowledge_base.md`).

**Statement.** Let (A', B') be a disjoint pair of S₀-extended-persistent types with
witnesses n_A < n_B (WLOG; the mirror case is identical by relabeling). Let
F' := P(a_{n_B}) \ S₀ (finite, nonempty by Lemma G / the Generalized Bounded Witness
Lemma) and, for n > n_B with ρ(n) = A', let D(n) := P(a_n) ∩ F'. Then D(n) ≠ ∅ for
every such n, and there is a fixed nonempty subset D* ⊆ F' with D(n) = D* for
infinitely many such n.

**Proof.** Nonemptiness of D(n) is immediate from the Generalized Bounded Witness
Lemma applied with witness m = n_B: every n > n_B with ρ(n) = A' has a_n divisible by
some prime of F'_{A',B'} = P(a_{n_B}) \ S₀ = F', so that prime lies in P(a_n) ∩ F' =
D(n). Since A' is S₀-extended-persistent, infinitely many n > n_B satisfy ρ(n) = A';
for each, D(n) is a nonempty subset of the fixed finite set F', so D(n) ranges over
the finite set 2^{F'} \ {∅} as n ranges over an infinite index set. By the infinite
pigeonhole principle, some fixed D* ⊆ F' is attained by D(n) for infinitely many n. ∎

**Scope.** Strictly refines the certified Generalized Bounded Witness Lemma's
Corollary (which pigeonholes over a single responsible prime per n) by pigeonholing
over the whole intersection set D(n) at once. Unconditional, no dependence on any
open hypothesis (FAH, Symmetric FAH, Singleton Hypothesis). Does not by itself close
FAH — see `greedy-exchange-cost-potential`'s round-7 section for the documented
stall of the "Blocking-Data Bridging" mechanism that attempted to build on this
lemma.

**Status.** Correct, complete, no gaps, unconditional. Certified by the round-7
proof-reviewer: independently re-derived and checked — a straightforward,
gap-free strengthening of the already-certified pigeonhole mechanism to the full
intersection set.
