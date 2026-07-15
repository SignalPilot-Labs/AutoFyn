## Build result

- Slug: `omega-lexicographic-euclid`
- Status: solved
- Artifact: `/home/agentuser/repo/results/imo-2026-01/approaches/omega-lexicographic-euclid.md`

## Work completed

Expanded the approved outline into a complete end-to-end proof. The proof:

1. Defines the lexicographic monovariant \((S,r)\), with \(S=\sum_i\Omega(b_i)\) and \(r\) the number of nonunits.
2. Derives the exact identity showing that a move loses \(\Omega(\gcd(m,n))\) from \(S\).
3. Handles separately \(d>1\) and \(d=1\), and explicitly proves well-foundedness of the resulting descent.
4. Proves the primewise valuation update and checks all four required cases: both valuations zero, exactly one zero, unequal positives, and equal positives.
5. Proves prime-support persistence, excludes an all-ones terminal board, and identifies the sole terminal nonunit by unique factorization as
   \[
   M=\prod_{p\in P}p^{\gcd\{v_p(a_i):v_p(a_i)>0\}}.
   \]
6. Concludes that the terminal value is independent of all choices.

## Promotable lemmas

- Positive-valuation Euclidean invariant.
- Lexicographic multiplicity descent.

## Spec concerns

None.
