## Lemma: Primorial Floor Bound (CERTIFIED, round 22)

**Source.** `a1-3q-subfamily-theorem`, round 22, closing Case (b) `n` even
`k≥1`. Self-contained. Independently re-verified in full by the round-22
proof-reviewer (the `M≥(r+1)!` bound and the corollary's induction, including
the base case and the `(s+2)^2≥2(s+3)` inequality, re-derived from scratch)
— promoted from certified-candidate to **certified**.

**Statement.** If a positive integer `M` has `r := ω(M)` distinct prime
factors, then `M ≥ (r+1)!`.

**Proof.** Let `p_1<p_2<⋯<p_r` be `M`'s distinct prime factors. As in the
Legendre Sieve Gap Bound's Step 1, a strictly increasing sequence of integers
starting at `p_1 ≥ 2` has `p_i ≥ i+1` for every `i=1,…,r`. Hence
`M ≥ p_1 p_2 ⋯ p_r ≥ ∏_{i=1}^r (i+1) = (r+1)!`. ∎

**Corollary (used downstream).** For integers `s ≥ 4`,
`(s+1)! ≥ (3/7)·2^{s+1}·(s+2) + 5`. *Proof:* base case `s=4`:
`5! = 120 ≥ (3/7)(32)(6)+5 = 576/7+5 ≈ 87.3`. Inductive step `s → s+1`
(`s≥4`): `(s+2)! = (s+2)(s+1)! ≥ (s+2)[(3/7)2^{s+1}(s+2)+5]` (by the
inductive hypothesis) `= (3/7)2^{s+1}(s+2)^2 + 5(s+2)`. Since
`(s+2)^2 ≥ 2(s+3)` for all `s ≥ 1` (`s^2+2s-2≥0` at `s=1` already, and
increasing thereafter), `(3/7)2^{s+1}(s+2)^2 ≥ (3/7)2^{s+2}(s+3)`; combined
with `5(s+2) ≥ 5`, this gives `(s+2)! ≥ (3/7)2^{s+2}(s+3)+5`, closing the
induction. ∎ Consequently, whenever `ω(M)=s≥4`, `M ≥ (s+1)! ≥
(3/7)2^{s+1}(s+2)+5`, i.e. `M-5 ≥ (3/7)2^{s+1}(s+2)`.

**Status.** Correct, complete, unconditional, purely elementary (uses only
that primes in increasing order grow at least linearly with their index — no
Chebyshev/PNT/binomial-coefficient machinery, unlike the heavier route
originally sketched in round 21's outline). Reusable whenever a future
approach needs an explicit (not merely asymptotic) lower bound on the size
of an integer in terms of its number of distinct prime factors, or the
paired corollary comparing `2^{ω}·poly(ω)`-type growth against factorial
growth.
