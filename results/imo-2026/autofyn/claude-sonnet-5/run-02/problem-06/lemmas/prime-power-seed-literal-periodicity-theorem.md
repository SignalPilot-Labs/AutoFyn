## Lemma: Prime-Power Seed Literal Periodicity Theorem (certified)

**Source.** `prime-power-seed-periodicity-theorem`, round 18. Independently
re-verified by the proof-reviewer (round 18).

**Depends on (certified).** Nothing beyond the problem's own definitions
(cites `free-facts-gcd.md`-style reasoning inline, but is otherwise
self-contained; does not use the persistent-type/FAH machinery at all).

**Statement.** Let `a_1, a_2, a_3, ...` be the sequence defined by the
problem (`a_1 > 1`; `a_{n+1}` is the smallest integer `> a_n` with
`gcd(a_{n+1}, a_i) > 1` for every `i = 1, ..., n`). If `a_1 = p^k` for a
prime `p` and integer `k ≥ 1`, then `a_n = a_1 + p(n-1)` for every `n ≥ 1`.
Consequently the problem's conclusion holds with `T = 1`, `L = p`,
literally from `n = 1` (not merely eventually).

**Proof.** Strong induction on `n`. Base case `n=1` trivial. Inductive step:
assuming `a_i = a_1+p(i-1)` for `i ≤ n` (so `p | a_i` for all `i ≤ n`, since
`p | a_1 = p^k` and `p | p(i-1)`), show `a_{n+1} = a_n+p`.
- *Illegality of `a_n+j`, `1 ≤ j ≤ p-1`*: `a_n+j ≡ j ≢ 0 (mod p)`, so
  `p ∤ (a_n+j)`. Since `P(a_1) = {p}` (as `a_1=p^k`), any common divisor of
  `a_n+j` and `a_1` is a power of `p`; since `p ∤ (a_n+j)`, that common
  divisor is `1`. So `gcd(a_n+j, a_1) = 1`, failing the `i=1` legality
  check — illegal, for every `j = 1,...,p-1`.
- *Legality of `a_n+p`*: `p | a_n` and `p | p`, so `p | (a_n+p)`; since
  `p | a_i` for every `i ≤ n`, `p` is a common divisor, so
  `gcd(a_n+p, a_i) ≥ p > 1` for every `i ≤ n`.
- Since every integer strictly between `a_n` and `a_n+p` is ruled illegal
  and `a_n+p` is legal, minimality of `a_{n+1}` forces `a_{n+1} = a_n+p`,
  which equals `a_1+p((n+1)-1)`, closing the induction (and `p | a_{n+1}`
  is preserved for the next step). ∎

**Independent verification (this review).** Re-derived the induction from
scratch (matches above). Independently re-simulated (fresh Python
trial-division greedy generator, no shortcuts) on 43 seeds — the builder's
own 24-seed set plus 19 additional seeds this review chose independently,
including primes NOT in the builder's test set (`p=29,31,37,41`) and larger
exponents (`k` up to `10`, e.g. `a_1=1024=2^10`) — exact match of the closed
form `a_n = a_1+p(n-1)` on the first 15 terms in every case, zero
discrepancies.

**Scope.** Applies exactly to `a_1 = p^k` (`|Q|=1`, `Q` a singleton prime
power). Strictly generalizes the previously-implicit `p=2` special case
(subsumed, for `p=2`, by the strictly broader `even-seed-literal-
periodicity-theorem.md`, which covers all even `a_1`, not just powers of
`2`). Does **not** extend to `|Q| ≥ 2` (the argument depends essentially on
`P(a_1)` being a singleton — a candidate ruled out against index `1` for
lack of any shared prime with `a_1` when `P(a_1)` has one element; with a
second prime factor of `a_1`, a candidate `a_n+j` failing to share `p` may
still share the other prime, so is not automatically ruled out). This is
explicitly confirmed by `n1-periodicity-reconciliation` §6.1's Odd-Prime
Non-Trivialization Proposition (`a_1=15,45`, `|Q|=2`, independently
re-verified — see round 18 proof-reviewer report), which is a genuine
counterexample to any naive extension of this theorem's mechanism to
`|Q| ≥ 2`.

**Status.** Correct, complete, no gaps, fully unconditional. Certified.
The `2 | a_1` subfamily and the `a_1 = p^k` subfamily are now BOTH fully
and unconditionally solved sub-cases of the general problem (overlapping
exactly at `a_1 = 2^k`); the general problem (arbitrary `a_1 > 1`, in
particular any `|Q| ≥ 2` seed not of the form `2·(\text{anything})`) remains
open, conditional on H1/H2 as documented in `current.md`.
