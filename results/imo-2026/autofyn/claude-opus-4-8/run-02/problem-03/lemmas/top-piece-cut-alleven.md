# Fact: top-piece-cut for all-even refinements — CERTIFIED round 7

Source: `dual-integer-certificate` §4(ii). Reviewer re-derived.

## Statement
In any all-even refinement of `W_n={2^0,…,2^n}` (every distinct sub-piece value has even multiplicity),
the largest sub-piece value satisfies `w_1 ≤ 2^{n-1}`; hence piece `2^n` is cut (has ≥2 sub-pieces).

## Proof
`w_1` has even multiplicity `≥2`, so ≥2 sub-pieces equal `w_1`. A sub-piece of value `w_1` can only lie
in a piece `2^m` with `2^m ≥ w_1`. Suppose `w_1 > 2^{n-1}`. Then every piece `2^m`, `m≤n-1`, has
`2^m ≤ 2^{n-1} < w_1`, so cannot house a copy of `w_1`; only piece `2^n` can. But `2w_1 > 2^n`, so piece
`2^n` houses at most `⌊2^n/w_1⌋=1` copy. Total multiplicity `≤1<2` — contradiction. Hence `w_1≤2^{n-1}`,
and piece `2^n` (all sub-pieces `≤w_1≤2^{n-1}<2^n`) is cut. ∎

## Companion negative fact (also certified)
An all-even refinement need NOT cut every piece: `piece1={1}, piece2={½,½,1}, piece4={2,2}` (multiset
`{2,2,1,1,½,½}`, `N=3=n+1`) is all-even with piece `1` uncut. So the Budget Lemma (no all-even in `≤n`
cuts) is NOT provable by a per-piece cut count; it needs the arithmetic of the powers `2^k`.
