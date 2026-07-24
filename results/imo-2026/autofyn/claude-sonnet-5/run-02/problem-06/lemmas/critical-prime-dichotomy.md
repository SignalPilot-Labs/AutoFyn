## Lemma H: Critical Prime Dichotomy (certified, with a corrected statement)

**Source.** `greedy-exchange-cost-potential`, round 5. Independently re-verified by the
proof-reviewer (round 5), with one wording correction (see "Reviewer correction" below)
— the mathematical content and proof are otherwise exactly as submitted.

**Depends on (certified).** `free-facts-gcd.md` (Free Facts) and the problem's own
greedy defining rule (a_n is the smallest integer exceeding a_{n-1} with gcd(a_n,a_i)>1
for all i < n).

**Statement (reviewer-corrected: "at least one," not "exactly one").** Let n ≥ 2 be
any index, S₀ ⊇ Q any fixed finite set of primes, and q′ any prime with q′ | a_n and
q′ ∉ S₀. Let e := v_{q'}(a_n) ≥ 1 and c := a_n / q'^e. Then **at least one** of the
following holds:
(a) c ≤ a_{n−1}, or
(b) there is an index i ∈ {1,...,n−1} with P(a_i) ∩ P(a_n) = {q′} exactly.

**Reviewer correction.** The source file's statement says "exactly one of the
following holds," i.e. claims (a) and (b) are mutually exclusive. The proof given only
establishes the (inclusive) disjunction "(a) or (b)" — it shows ¬(a) ⟹ (b), which gives
"(a) ∨ (b)," not exclusivity. Nothing in the proof (or elsewhere in the certified stack)
rules out (a) and (b) holding simultaneously (e.g. c could simultaneously be ≤ a_{n-1}
and some earlier a_i could still share exactly {q'} with a_n by coincidence). This does
not affect any downstream use in the source file — every application only invokes "(a)
or (b)" — so the substance is unaffected; only the stated exclusivity is corrected here.

**Proof (as submitted, verified correct for the corrected statement).** Write
a_n = q'^e · c with gcd(c,q') = 1; P(c) = P(a_n) \ {q'}, and c < a_n. Suppose (a) fails,
i.e. c > a_{n-1}. Then a_{n-1} < c < a_n, so by minimality of a_n (the greedy rule), c
must be illegal: some i ∈ {1,...,n-1} has gcd(c,a_i) = 1, i.e. P(c) ∩ P(a_i) = ∅. By
Free Facts, gcd(a_n,a_i) > 1; fix p ∈ P(a_n) ∩ P(a_i). Since P(a_n) = P(c) ∪ {q'}
(disjoint union), if p ≠ q' then p ∈ P(c) ∩ P(a_i) = ∅, contradiction; so p = q' is the
only possibility, giving P(a_n) ∩ P(a_i) = {q'} exactly — (b) holds. ∎

**Scope.** A genuine necessary condition on any outside-core prime q' dividing a
witness a_n: either stripping it drops the value below the previous term, or it is the
*sole* rescuer of some specific earlier term's legality. Proved (in
`greedy-exchange-cost-potential`, round 5) to be insufficient by itself to force the
Singleton Hypothesis (|F'| = 1): nothing prevents two distinct primes q', q'' ∈ F' from
each independently satisfying branch (b) via different earlier witnessing indices, and
nothing in the certified stack connects those witnessing indices to force a
contradiction. This remains the sharpest fully general handle on a witness's
outside-core factorization currently in the workspace, but does not close (†).

**Status.** Correct (with the exclusivity wording fixed to "at least one"), complete,
no gaps, unconditional. Certified as a standalone reusable lemma.
