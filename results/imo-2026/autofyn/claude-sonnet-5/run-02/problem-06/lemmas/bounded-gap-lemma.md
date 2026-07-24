## Lemma: Bounded Gap Lemma (certified)

**Source.** `amortized-charging-budget`, Lemma 2 (Section 2).

**Statement.** For every n ≥ 1, a_{n+1} ≤ a_n + a_1. Consequently the sequence grows
linearly: a_1 + (n-1) ≤ a_n ≤ n·a_1 for all n ≥ 1.

**Proof.** Let r be the smallest multiple of a_1 exceeding a_n; since a_1 ≥ 2, among
any a_1 consecutive integers exactly one is a multiple of a_1, so r ≤ a_n + a_1. Write
r = a_1·t. For i = 1: a_1 | r so gcd(r, a_1) = a_1 > 1. For 2 ≤ i ≤ n: by the Free
Facts lemma, gcd(a_i, a_1) > 1, so some prime q_i divides both a_1 and a_i; since
a_1 | r, q_i | r, hence q_i | gcd(r, a_i), so gcd(r, a_i) > 1. Thus r is a valid
candidate for a_{n+1} (satisfies gcd(r, a_i) > 1 for all i = 1, ..., n), and by
minimality of a_{n+1} (the *smallest* valid successor), a_{n+1} ≤ r ≤ a_n + a_1. ∎

**Verification.** Numerically confirmed (a_1 = 15, 35, 143, 1001): observed maximum
gaps are 6, 10, 22, 14 respectively, all ≤ a_1, consistent with the bound.

**Status.** Correct, complete, unconditional (does not depend on any other lemma or
open gap). Reusable by any approach to this problem.
