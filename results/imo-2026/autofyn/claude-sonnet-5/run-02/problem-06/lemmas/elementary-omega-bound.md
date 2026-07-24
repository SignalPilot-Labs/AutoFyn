## Lemma: Elementary ω(a_n) = O(log n) Bound (CERTIFIED, round 19)

**Source.** `triangle-consistency-pigeonhole`, round 19, §5.1. Independently
re-verified by the round-19 proof-reviewer (trivial, re-derived from
scratch).

**Depends on (certified).** `bounded-gap-lemma.md` (`a_n ≤ n·a_1`).

**Statement.** For every `n ≥ 1`, `ω(a_n) ≤ log_2 a_n` (`ω(m)` = number of
distinct prime factors of `m`); consequently `ω(a_n) ≤ log_2 n + log_2 a_1`.

**Proof.** Write `a_n = p_1^{e_1}···p_k^{e_k}`, `k=ω(a_n)`, each `p_i≥2,
e_i≥1`. Then `a_n ≥ ∏ p_i ≥ 2^k`, so `k ≤ log_2 a_n`. Substitute the certified
Bounded Gap Lemma's `a_n ≤ n·a_1`. ∎

**Status.** Correct, complete, unconditional, purely elementary (no PNT).
Upper bound only — explicitly does NOT give any lower bound on the frequency
of singleton (`ω=1`-outside-core) occurrences; scope limited accordingly.
Reusable whenever a future approach needs a crude a priori cap on the number
of distinct prime factors of a term of this sequence.
