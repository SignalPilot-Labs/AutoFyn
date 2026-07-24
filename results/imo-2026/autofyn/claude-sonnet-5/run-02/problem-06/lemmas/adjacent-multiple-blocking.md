## Adjacent Multiple Blocking (Lemma K) — CERTIFIED, round 7

**Source.** `greedy-exchange-cost-potential`, round 7.

**Depends on.** Only the problem's own greedy defining rule (a_n is the smallest
positive integer exceeding a_{n-1} legal against every a_1,...,a_{n-1}); no other
certified lemma.

**Statement.** Let n ≥ 2 and let q be any prime with q ∤ a_n. Let
c := q · ⌊a_n/q⌋ (the largest multiple of q strictly less than a_n; well-defined,
and c < a_n since q ∤ a_n forces a_n mod q ∈ {1,...,q−1}). Then either
(a) c ≤ a_{n-1}, or
(b) there is an index j < n with gcd(c, a_j) = 1 (c is illegal against a_j — a
"skipped candidate" in the greedy sense).

**Proof.** If c ≤ a_{n-1}, (a) holds. Otherwise a_{n-1} < c < a_n, so c is a positive
integer strictly between a_{n-1} and a_n. Since a_n is, by the greedy rule, the
*smallest* positive integer exceeding a_{n-1} with gcd(·, a_i) > 1 for every i < n,
and c is a smaller candidate exceeding a_{n-1}, c cannot itself satisfy this
legality condition for every i < n (else minimality of a_n would force a_n ≤ c <
a_n, a contradiction). So some j < n has gcd(c, a_j) = 1, giving (b). ∎

**Scope.** A fully general, elementary consequence of greedy minimality; unlike the
certified Critical Prime Dichotomy (Lemma H), which strips a prime that DOES divide
the witness (so the resulting c = a_n/q'^e has an exactly controlled factorization
P(c) = P(a_n) \ {q'}), this lemma rounds a_n DOWN to the nearest multiple of a prime
q that does NOT divide a_n, producing a competitor c = a_n − r (1 ≤ r < q) whose
factorization has no established relationship to a_n's own. This is the first tool
in the workspace to use negative/illegality (skipped-candidate) data rather than
positive/existential divisibility facts. Unconditional, no dependence on any open
hypothesis. Does NOT by itself close FAH/Symmetric FAH — see
`greedy-exchange-cost-potential`'s round-7 section for the precisely diagnosed
reason (branch (b)'s blocking prime has no controlled relationship to q, so it
cannot be pinned down).

**Status.** Correct, complete, no gaps, unconditional. Certified by the round-7
proof-reviewer: independently re-derived — a direct, correct minimality argument,
structurally analogous to but genuinely distinct from the certified Critical Prime
Dichotomy.
