# Lemma CK — cheap-kill: `A ≥ smallest piece` for odd piece-count

**Status: CERTIFIED** (round 3, reviewer). One-line proof; verified on `n = 2, 3` grids (0 violations; tight at minimizers).

**Statement.** Let the final pieces be sorted descending `p_1 ≥ p_2 ≥ … ≥ p_{2m+1}` (odd count `M = 2m+1`). Then the alternating advantage sum
```
A = Σ_{i=1}^{2m+1} (−1)^{i+1} p_i  ≥  p_{2m+1},
```
i.e. `A` is at least the smallest piece.

**Proof.** Group the sum into consecutive sorted pairs plus the last leftover:
```
A = (p_1 − p_2) + (p_3 − p_4) + … + (p_{2m−1} − p_{2m}) + p_{2m+1}.
```
Because the pieces are sorted descending, `p_{2i−1} ≥ p_{2i}` for every `i = 1, …, m`, so each pair-excess `p_{2i−1} − p_{2i} ≥ 0`. The leftover is `p_{2m+1}`, the smallest piece (last index, sorted). Therefore `A ≥ 0 + … + 0 + p_{2m+1} = p_{2m+1}`. ∎

**Scope and limitation (honest).** CK applies ONLY to odd piece-count configs. On the integer grid (pieces positive multiples of `1/D(n)`), the smallest piece `≥ 1/D(n) = α(n)`, so CK closes the odd-count sub-case of Lemma L for grid-aligned marks. It does NOT lift to reals: Xiang can make a sub-`α(n)` smallest piece (the fragment then cancels at an odd rank, so `A ≥ α(n)` survives but CK cannot detect it). The even-count sub-case (e.g. the pair-pile extremal, `2n` pieces) is NOT covered by CK at all. CK is a useful lower-bound tool for odd-count configs but is not a standalone closure of Lemma L.

**Verification.** Checked on all odd-count configs of the `n = 2` fine grid (denominator `7`): 0 violations. At `n = 3`, all 22 odd-count minimizers of the level-3 dyadic satisfy `A = α(3) = 1/15` and `smallest = 1/15`, so `A = smallest` with equality (CK is tight). These are computational checks, not proof steps.

**Knowledge-base tool.** Invariants & monovariants (the alternating advantage sum decomposes into non-negative pair-excesses plus a leftover singleton exactly when the piece-count is odd).

**Where proved.** `approaches/pairing-partner-transfer.md` (round 3, §Lemma CK); also appears in `approaches/pairing-partner.md`.
