## Lemma: Bounded Witness Lemma (certified)

**Source.** `covering-system-construction`, Step 2. This is the strongest form of the
"linking prime" idea produced so far — strictly stronger than and supersedes the
`amortized-charging-budget` "Forced-Linking-Prime Lemma" (see
`forced-linking-prime.md`): it needs only ONE arbitrary witness index (not an
infinite-pigeonhole extraction over infinitely many candidates), and it concludes
divisibility for ALL later same-type terms, not merely infinitely many. Recommended as
the default tool for any future approach attacking this problem's core-prime-pool
question.

**Statement.** Let Q = P(a_1), and for n ≥ 1 let τ(n) = P(a_n) ∩ Q. Let A, B ⊆ Q be
two persistent types (in the sense of `persistent-type-pigeonhole.md`) with A ∩ B = ∅.
Fix ANY single index m with τ(m) = B, and let F_{A,B} := P(a_m) \ Q (a fixed, finite
set of primes not in Q, depending only on m). Then for every n > m with τ(n) = A, a_n
is divisible by some prime of F_{A,B}.

**Proof.** Fix n > m with τ(n) = A. By the Free Facts lemma, gcd(a_n, a_m) > 1, so
there is a prime p dividing both a_n and a_m. Suppose p ∈ Q. Then p ∈ P(a_n) ∩ Q =
τ(n) = A and p ∈ P(a_m) ∩ Q = τ(m) = B, so p ∈ A ∩ B = ∅, contradiction. Hence p ∉ Q,
so p ∈ P(a_m) \ Q = F_{A,B}, and p | a_n. ∎

**Status.** Correct, complete, no gaps. Self-contained (uses only the Free Facts
lemma); does not depend on any open gap.
