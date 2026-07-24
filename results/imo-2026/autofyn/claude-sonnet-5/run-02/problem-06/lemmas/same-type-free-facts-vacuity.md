## Lemma: Same-Type Free Facts Vacuity Observation (certified)

**Source.** `greedy-exchange-cost-potential`, round 9, Step 3 Route (b).
Independently re-verified by the proof-reviewer (round 9).

**Depends on (certified).** `free-facts-gcd.md`; the definition of extended type
`ρ(n) := P(a_n) ∩ S₀`.

**Statement.** Let `n, n'` be two distinct indices with `ρ(n) = ρ(n') = A'` for the
same `S₀`-extended-persistent type `A'`. Then Free Facts' conclusion
`gcd(a_n, a_{n'}) > 1` is automatically satisfied by the primes of `A'` itself (every
prime of `A'` divides both `a_n` and `a_{n'}` by definition of `ρ(n)=ρ(n')=A'`), and
in particular Free Facts, applied to two SAME-type occurrences, supplies **no
outside-core (`S₀`-complement) information** and no route to forcing any specific
outside-core prime to be shared between `a_n` and `a_{n'}`.

**Proof.** By hypothesis every `p ∈ A'` satisfies `p ∈ P(a_n) ∩ S₀` and
`p ∈ P(a_{n'}) ∩ S₀`, i.e. `p | a_n` and `p | a_{n'}`. Since `A'` is a nonempty
persistent type (nonempty as `ρ(n) ⊇ τ(n) ≠ ∅` for the underlying base type), any
`p ∈ A'` already witnesses `gcd(a_n,a_{n'}) ≥ p > 1` — the Free Facts conclusion is
implied by the type definition alone, with no need to invoke Free Facts as an
independent fact, and the specific shared prime it exhibits (any element of `A'`) is
already in `S₀`, carrying no information about primes outside `S₀`. ∎

**Scope.** Contrasts with Lemma G's use of Free Facts on DISJOINT types (`A' ∩ B' =
∅`), where the forced shared prime must lie outside `S₀` (since no `S₀`-prime can be
shared, as `A' ∩ B' = ∅`) — that is the genuinely informative use. This Lemma records
that the same tool degenerates to a tautology when applied to two occurrences of the
SAME type, explaining why a same-type "successor" or "consecutive occurrence"
argument cannot recover the missing existential-to-universal promotion step by
appealing to Free Facts directly.

**Status.** Correct, complete, no gaps, fully unconditional, elementary. Independently
re-derived by the reviewer. Certified as a standalone reusable negative/diagnostic
building-block fact.
