**Status: CERTIFIED** (reviewer, round 2). The collision, symmetry, central-
piece, and excess arguments are rigorous. Verified by exact rational arithmetic
for `n = 1..5`: the merged multiset matches the pair-pile, `A = 1/D(n)`,
`Liu = f(n)` in every case. Uses `n` marks (vs the pair-pile's `n − 1`), both
within budget. Importable as a symmetry-based alternative to the pair-pile.

# Mirror certificate — Xiang caps the dyadic config at f(n) by point-reflection

**Statement.** Against Liu's level-`n` dyadic config — Liu's `n` marks at
`l_j = (2^j − 1)/D(n)`, `j = 1,…,n`, where `D(n) = 2^{n+1} − 1` (giving pieces
`(1, 2, 4, …, 2^n)/D(n)`) — Xiang's **mirror strategy** places his `n` marks at
`1 − l_j` for `j = 1,…,n`. The resulting merged partition is the symmetric
multiset

```
1, 2, 4, …, 2^{n−1},   1,   2^{n−1}, …, 4, 2, 1     (all over D(n)),
```

i.e. **two copies of `2^k/D(n)` for each `k = 0, …, n−1` plus one extra `1/D(n)`
(three copies of `1/D(n)` in total). Sorted descending this is the pair-pile

```
2^{n−1}, 2^{n−1}, 2^{n−2}, 2^{n−2}, …, 4, 4, 2, 2, 1, 1, 1   (over D(n)),
```

whose alternating advantage sum is `A = 1/D(n)`, hence (by Lemma G's parity
identity `Liu = (1 + A)/2`) Liu's payoff is exactly

```
Liu = (1 + 1/D(n))/2 = (D(n)+1)/(2 D(n)) = 2^{n+1}/(2 D(n)) = 2^n/D(n) = f(n).
```

This certifies that the dyadic config's value is **at most** `f(n)` for every
`n ≥ 1`, using `n ≤ n` marks. (The certified pair-pile construction achieves the
same cap with `n − 1 ≤ n` marks; the mirror is an equivalent, symmetry-based
certificate.)

**Proof.**

*Mark placement and distinctness.* Liu's `n` marks are
`l_j = (2^j − 1)/D(n)` for `j = 1,…,n`; they are strictly increasing in `(0,1)`.
Xiang's mirror marks are `1 − l_j`, also strictly increasing. A collision
`l_i = 1 − l_j` would require `l_i + l_j = 1`, i.e.
`(2^i − 1 + 2^j − 1)/D(n) = 1`, i.e. `2^i + 2^j = D(n) + 1 = 2^{n+1}`. A sum of
two powers of two equals a power of two only when the two powers are equal, so
`i = j` and `2·2^i = 2^{n+1}`, i.e. `i = n`; but then `2 l_n = 2(2^n − 1)/D(n) =
(2^{n+1} − 2)/D(n) ≠ 1 = D(n)/D(n)`. Hence no collision; all `2n` marks are
distinct. None equals `0` or `1` (since `l_j ∈ (0,1)`), and none equals `1/2`
(`l_j = 1/2` would force `2(2^j − 1) = 2^{n+1} − 1`, i.e. `2^{j+1} = 2^{n+1} + 1`,
impossible as the RHS is odd and `> 1`).

*Symmetry.* The map `x ↔ 1 − x` sends each Liu mark to a Xiang mark and vice
versa, so the merged mark set is invariant under point-reflection about `1/2`.
The partition it induces is therefore symmetric: each piece `[u, v]` is paired
with the piece `[1 − v, 1 − u]` of equal length, except possibly a piece fixed by
the symmetry (centered at `1/2`, with endpoints `u` and `1 − u` both marks).

*The central piece.* A piece fixed by the symmetry has endpoints `u` and
`1 − u`, both marks, with no mark strictly between them. The pair `(l_n, 1 − l_n)`
satisfies this: `l_n = (2^n − 1)/D(n)`, `1 − l_n = 2^n/D(n)`, and these are
adjacent in the merged sort. To see adjacency, observe that any mark strictly
between `l_n` and `1 − l_n` is either some `l_j` with `l_n < l_j < 1 − l_n`
(impossible since `j > n` would be needed for `l_j > l_n`, but there are only `n`
Liu marks) or some `1 − l_j` with `l_n < 1 − l_j < 1 − l_n`, i.e.
`l_n < l_j < 1 − l_n`; the left inequality `l_n < 1 − l_j` is `l_j < 1 − l_n =
2^n/D(n)`, i.e. `2^j − 1 < 2^n`, i.e. `j ≤ n`, while the right inequality
`1 − l_j < 1 − l_n` is `l_j > l_n`, i.e. `j > n` — a contradiction. So no mark lies
strictly between `l_n` and `1 − l_n`; the central piece is `[l_n, 1 − l_n]` of
length `(1 − l_n) − l_n = 1/D(n)`.

*The symmetric pairs.* Sorting the marks gives
`0 < l_1 < l_2 < … < l_n < 1 − l_n < 1 − l_{n−1} < … < 1 − l_1 < 1` (using
`l_n < 1/2 < 1 − l_n`, which holds as `2(2^n − 1) < 2^{n+1} − 1`). Reading off
the pieces left to right:

```
[l_0, l_1] = 1/D,      [l_1, l_2] = 2/D,   …,  [l_{n−1}, l_n] = 2^{n−1}/D,
[l_n, 1−l_n] = 1/D     (central),
[1−l_n, 1−l_{n−1}] = 2^{n−1}/D,   …,   [1−l_2, 1−l_1] = 2/D,   [1−l_1, 1] = 1/D.
```

The multiset is: two copies of `2^k/D(n)` for each `k = 0, 1, …, n − 1`
(the left-and-right symmetric pairs) plus one extra copy of `1/D(n)` (the
central piece). Total count: `2n + 1` pieces ✓; total length: `2·Σ_{k=0}^{n−1}
2^k/D + 1/D = 2(2^n − 1)/D + 1/D = (2^{n+1} − 2 + 1)/D = (2^{n+1} − 1)/D = 1` ✓.

*Excess/advantage.* Sorted descending, the multiset is the pair-pile
`2^{n−1}, 2^{n−1}, 2^{n−2}, 2^{n−2}, …, 4, 4, 2, 2, 1, 1, 1` (over `D(n)`).
Consecutive sorted pairs: each `(2^k, 2^k)` has excess `0`; the `(1, 1)` pair has
excess `0`; the unpaired final `1` (at the last odd rank) contributes `+1`. Hence
`A = 1` over `D(n)`, i.e. `A = 1/D(n)`. By Lemma G's parity identity,
`Liu = (1 + 1/D(n))/2 = 2^n/D(n) = f(n)`. ∎

**Verification.** Exact rational arithmetic for `n = 1, 2, 3, 4, 5`: the merged
multiset matches the pair-pile above, `A = 1/D(n)`, and `oddsum = 2^n/D(n) = f(n)`
in every case. (n=1: pieces `(1,1,1)/3`, `A = 1/3`, `Liu = 2/3`. n=2: pieces
`(2,2,1,1,1)/7`, `A = 1/7`, `Liu = 4/7`. n=3: `(4,4,2,2,1,1,1)/15`, `A = 1/15`,
`Liu = 8/15`. n=4: `(8,8,4,4,2,2,1,1,1)/31`, `A = 1/31`, `Liu = 16/31`. n=5:
`(16,16,8,8,4,4,2,2,1,1,1)/63`, `A = 1/63`, `Liu = 32/63`.)

**Knowledge-base tools.** **Constructive / incremental** (explicit symmetric
mark placement); **Invariants & monovariants** (the point-reflection symmetry
forces the pair structure); **Exploit symmetry / WLOG** (the `x ↔ 1 − x`
involution).

**Where proved.** `approaches/pairing-partner.md`, "Mirror certificate" (round 2).
