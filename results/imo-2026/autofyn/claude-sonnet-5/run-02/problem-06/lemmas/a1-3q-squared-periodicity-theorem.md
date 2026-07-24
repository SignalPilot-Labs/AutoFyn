## Lemma/Theorem: `a_1 = 3q^2` Literal Periodicity Theorem (CERTIFIED, round 24)

**Source.** `a1-3qk-subfamily-theorem`, round 24, Part IV (closing Case (b),
`n` even, for `m=2`), building on the certified `m`-generic Parts I-III
(`lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md`). Independently
re-verified in full by the round-24 proof-reviewer.

**Depends on (certified).** `lemmas/legendre-sieve-gap-bound.md`,
`lemmas/primorial-floor-bound.md`, `lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md`.

**Statement.** For every prime `q ≥ 7, q ≠ 5`, the sequence with `a_1 = 3q^2`
satisfies, literally from `n=1`: `a_n = 3(q^2+n-1) = 3q^2+3(n-1)` for every
`n ≥ 1`. I.e. `T=1, L=3` from the very first term.

**Proof.** By strong induction on `n`, using: (i) the `m`-generic base case,
`a_n+1` illegality, Case (a) `q∤(a_n+2)` illegality, and odd-`n` Parity
Witness illegality, all transplanted verbatim from the certified
`m`-generic lemmas; (ii) `a_n+3` legality via the shared factor 3; (iii) Case
(b) (`n` even, `q|(a_n+2)`), split into `k=0` and `k≥1` sub-cases, each
closed via a two-branch sieve argument: large `ω(K)` (or `ω(qK)`) handled
unconditionally in `q` via a sharpened Primorial-Floor-Bound inequality
(`(r+1)! ≥ 9·2^r(r+1)+8` for `r≥6`, proved by induction), small `ω`
handled via the generic bound `2^r(r+1)≤192` giving an explicit finite
`q`-threshold, leaving a finite residual list of `(q,k)` pairs resolved by
direct witness search. Full derivation (Claims 1–2, parts (A), (B0), (B1),
(B2)) given in `approaches/a1-3qk-subfamily-theorem.md` (round 24 version).

**Independent verification (this review, fresh scripts).** (1) Reproduced,
via an independent `sympy` sieve-bound scan, the exact claimed residual
list: 4 failures at `k=0` (`q∈{11,17,23,29}`), and 4 further failures at
`k∈{1,...,7}` beyond the separately-handled `q=7` case
(`(q,k)∈{(13,1),(17,1),(19,1),(11,2)}`), plus the `q=7,k=1` failure — 9 total
exceptions, matching the builder's table exactly, digit for digit. (2)
Independently verified all 9 explicit witnesses (`i=3` in every case) by
direct `gcd` computation. (3) Spot-checked `k∈{8,...,39}` for `q<500` (no
further failures, consistent with the claimed unconditional `k≥8` closure).
(4) Independently re-simulated the full theorem (own fresh greedy
generator) for `q∈{7,11,13,17,19,23,29,31,37,41,43,53,59,61,71,73,79,83,89,
97,101,103}` out to 40–60 terms each: **zero mismatches** in every case,
including exact agreement at every one of the 9 hand-resolved exceptional
indices.

**Status.** Correct, complete, unconditional, no gaps found. `m=3` and
general `m≥3` remain open (not addressed by this lemma, which is scoped
strictly to `m=2`); see `approaches/a1-3qk-subfamily-theorem.md` for the
honestly-reported open gap on that front. Reusable as a standalone,
self-contained addition to the population of certified `a_1`-subfamily
periodicity theorems (joining `2|a_1`, `a_1=p^k`, `a_1=3q`).
