# Lemma (PROPOSED): D3 — fractional arrangement vertices have A > 1

**Status:** REJECTED for certification (round 6, reviewer) — this is an UNPROVEN
CONJECTURE, not a proved lemma. Retained in `lemmas/` as a tracked OPEN problem.
Verified at n=3,4 (min fractional A=5/3 > 1); the 2-adic-valuation mechanism proposed
by the round-6 explorer is FALSIFIED (valuation-reduction lemma sound; min fractional
A=5/3 has v_2=0, odd denominator 3; only 27/2019 at n=3 have v_2(A)<0). The general-n
proof is OPEN. The conditional L(n)-for-all-n corollary (cell-complex-l3 §D3.3) is sound
IF D3 holds. NOT a certified lemma; a conjecture worth tracking centrally.

## Statement (the open D3 conjecture)

For every `n >= 1`, at every **fractional-valued** arrangement vertex of the
level-`n` dyadic's hyperplane arrangement (i.e. an arrangement vertex at
which at least one of the `2n+1` sub-pieces is a non-integer rational), the
advantage sum `A` (integer scale, `D(n)` times the real advantage) satisfies

```
A > 1,   equivalently   A > alpha(n) * D(n)  (real scale).
```

Combined with the CERTIFIED `lemma-parity-integer-vertices` (every
integer-valued arrangement vertex has `A >= 1`, with equality at the
pair-excess binary form) and the CERTIFIED `lemma-vertex-principle-advantage`
(`min A` over reals = `min A` over arrangement vertices), this would give
`L(n)` for ALL `n` without per-`n` enumeration: `min A = 1`, hence `A >= 1`
everywhere, hence (Lemma G) `Liu >= f(n)`.

## Verified data (n = 3, 4)

- **n = 3** (complete exact-rational census, `/tmp/round-6/d3_2adic_census.py`,
  11523 feasible vertices, 2019 fractional): min fractional `A = 5/3` (real
  `5/45 = 1/9 > 1/15 = alpha(3)`). All 2019 fractional vertices have
  `A >= 5/3 > 1`. The min is attained at the multiset
  `(4, 4, 2, 4/3, 4/3, 4/3, 1)` (sum `15 = D(3)`).
- **n = 4** (low-A exact-rational census, `/tmp/round-6/d3_n4_prefilter.py`,
  float-prefiltered to `A <= 3`, 5148 exact-verified fractional vertices):
  min fractional `A = 5/3` (real `5/93 > 1/31 = alpha(4)`). All verified
  fractional vertices have `A >= 5/3 > 1`. The min is attained at the
  multiset `(8, 8, 4, 4, 2, 4/3, 4/3, 4/3, 1)` (sum `31 = D(4)`).

The two min fractional vertices have the SAME structural shape: pair-pile of
the top `n-1` Liu pieces + Liu piece `4` split into three equal `4/3` pieces
+ Liu piece `1` uncut. This is an explicit general-`n` candidate extremal
family (an `n`-mark Xiang strategy attains it for every `n >= 3`), giving
`A = 5/3` everywhere; verified to be the global min at n=3,4 only.

## Falsification of the 2-adic-valuation mechanism (round 6)

The round-6 explorer conjectured that the obstruction forcing fractional
`A > 1` is 2-adic: at a fractional vertex, `A = num/L` (Cramer), and the
claim was `v_2(num) < v_2(L)`, forcing `A = num/L` to have a factor of `2`
in its reduced denominator. This is FALSIFIED by the census:

- **Valuation-reduction lemma (proved).** `v_2(num) - v_2(L) = v_2(A)` (the
  2-adic valuation of `A`): after reducing `A = num/L = A_num/A_den`, both
  `num, L` share the factor `k = |L|/A_den`, so the valuation difference is a
  property of `A` alone. The explorer's `v_2(num) < v_2(L)` is equivalent to
  `v_2(A) < 0`.
- **n=3 census:** only `27/2019` fractional vertices have `v_2(A) < 0`; the
  other `1992` have `v_2(A) >= 0` (A is a 2-adic integer; many have A an
  integer `>= 2` despite fractional pieces). The min fractional `A = 5/3` has
  `v_2(A) = 0` (odd denominator `3`).
- **n=4 census:** only `135/5148` low-A fractional vertices have
  `v_2(A) < 0`. The min fractional `A = 5/3` again has `v_2(A) = 0`.

So the 2-adic-valuation mechanism is NOT the obstruction. The denominator
at the min fractional vertex is `3` (odd), pointing to a `3`-adic or
structural (not `2`-adic) story — but no such mechanism is established.

## Open gap (honest)

D3 is VERIFIED at `n = 3, 4` and FALSIFIED as a 2-adic phenomenon; the
general-`n` proof is OPEN. The conditional `L(n)`-for-all-`n` corollary
(stated in `approaches/cell-complex-l3.md` S-D3.3) makes D3 the SOLE open
step in the cell-complex route to `L(n)` for all `n`. Tightness (Xiang caps
at `f(n)`) is already CERTIFIED for all `n` by the pair-pile / mirror
(`lemma-pair-pile-dyadic-cap`, `lemma-mirror-dyadic-cap`), independent of
D3.

The induction gap (`M+R` factor-of-2, the `pairing-partner`-shared wall) is
a SEPARATE handle, unchanged by this round.

## Reusability

If a future round proves D3 (by any mechanism — 3-adic, structural,
LP-duality, or otherwise), this file upgrades to CERTIFIED and immediately
yields `L(n)` for all `n` via the conditional theorem in S-D3.3. If D3 is
falsified (a fractional vertex with `A <= 1` is found at some `n`), the
cell-complex route to general-`n` `L(n)` is dead and the induction /
pairing-partner Hall route becomes the sole live handle. Either resolution
is load-bearing, so the conjecture is worth tracking centrally.
