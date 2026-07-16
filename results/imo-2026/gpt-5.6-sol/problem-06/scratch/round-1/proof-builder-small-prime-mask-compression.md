## Status
solved

## Approach built
`small-prime-mask-compression`

## Result
A complete end-to-end proof was written to `results/imo-2026-06/approaches/small-prime-mask-compression.md`.

The proof explicitly closes every load-bearing point from the outline review:

1. It defines good and bad integers recursively, proves both directions of the recursion, and uses strong induction to identify the greedy sequence with the increasing enumeration of all good integers.
2. It proves the compression lemma with all three required branches: no large prime, a large prime with threshold exponent zero, and a large prime with positive threshold exponent. In the last branch it displays the full chain $x<pk\le Ak<Aq\le b$ and justifies every inequality.
3. It labels the opposite-color pair by color rather than numerical order and proves the replacement pair has strictly smaller maximum; it then transfers the common small prime through both similarities to contradict coprimality.
4. It proves the final shift by the order-preserving bijection $G\to G\cap[k+L,\infty)$ and counts exactly the $T$ initial good elements, removing endpoint ambiguity.
5. It names strong induction, the minimal-counterexample/extremal principle, divisor analysis, and modular arithmetic/periodic residue masks as used knowledge-base tools.

## Promotable lemmas proposed
- Small-prime compression lemma.
- Small-prime-mask invariance for the recursive coprimality kernel.
- Periodic-set enumeration lemma.
