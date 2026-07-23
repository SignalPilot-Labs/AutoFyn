# Value-Order = Dominant-Index-Order Lemma (D_m-specific)

**Certified by:** proof-reviewer, round 9, from approach `concavity-minimax-duality` (round-9
builder, §15.3). Independently re-derived (the induction re-traced from scratch) and
re-verified computationally with fresh code (an independent token-labeled BFS implementation,
not reusing the builder's harness): `m=1,\dots,5`, token-labeled state counts `4, 15, 62, 289,
1510` — matching the builder's and outline-reviewer's own reported counts exactly — `0` order
violations across all `1, 9, 65, 460, 3358` simultaneously-active token pairs checked
respectively.

**Depends on:** the certified token invariant of `lemmas/superincreasing-no-early-zero.md` (each
active token `v` in a `D_m`-reachable state carries an index set `S(v)\subseteq\{1,\dots,m+1\}`,
pairwise disjoint across simultaneously-active tokens, with `S(w)=S(x)\sqcup S(y)` for an
`M(x,y)`-produced token `w`); the Slot-Replacement Corollary
(`lemmas/superincreasing-preservation-and-slot-replacement.md`), applied to `D_m`
(`a_i=2^{m+1-i}`, a special case of a strictly superincreasing base).

## Statement

For `D_m` specifically (`a_i=2^{m+1-i}`, indices `i=1,\dots,m+1`), consider any `D_m`-reachable
token-labeled state. Let `i_0(v):=\min S(v)` be a token `v`'s **dominant index**. Then for any two
simultaneously-active tokens `u,v`:
```
i_0(u) < i_0(v)  \iff  u > v.
```
Equivalently, sorting the active state by value coincides exactly with sorting by increasing
dominant index.

## Proof

Induction on operation count.

**Base case** (`D_m` itself): `i_0(a_i)=i`, and `a_1>a_2>\dots>a_{m+1}`, so value order and index
order coincide trivially (`i_0` is literally the identity on positions).

**`D`-step:** deleting one token preserves the order-correspondence among the survivors (a subset
of an already order-consistent set retains its pairwise order-correspondence).

**`M`-step:** by IH, `x>y\implies i_0(x)<i_0(y)` (the very correspondence being inducted, applied
to the two operands `x,y`, simultaneously active before the operation). By the token invariant's
disjoint-union rule, `S(w)=S(x)\sqcup S(y)`, so
```
i_0(w) = \min(S(x)\cup S(y)) = \min(i_0(x),i_0(y)) = i_0(x)
```
(using `i_0(x)<i_0(y)` just derived). By the Slot-Replacement Corollary, the new value-sorted list
is the old one with `v_a\,(=x)` replaced in place by `w` and `v_b\,(=y)` deleted — and `w`'s
dominant index equals `x`'s own dominant index, unchanged. Hence the value-order/index-order
correspondence, restricted to survivors, is exactly preserved: the slot that held index `i_0(x)`
still does (now via `w`), the slot that held `i_0(y)` is gone (consistent, since `y` is gone), and
every other slot/index pair is untouched. `\blacksquare`

## Verification

Independently re-verified by the proof-reviewer, round 9, with a from-scratch token-labeled BFS
implementation (distinct from the builder's own code): for `m=1,\dots,5`, generated all
token-labeled `D_m`-reachable states (state counts `4, 15, 62, 289, 1510`, exactly matching the
file's own claim), and checked, for every pair of simultaneously-active tokens in every state,
that `i_0(u)<i_0(v)\iff u>v` — `0` violations (`1, 9, 65, 460, 3358` pairs checked respectively),
and `0` cases of two simultaneously-active tokens sharing a dominant index (consistent with the
disjoint-index-set invariant).

## Reusable by

Any approach needing to translate between the token/index bookkeeping of
`lemmas/superincreasing-no-early-zero.md` and the actual real-value ordering of a
`D_m`-reachable state — flagged in `concavity-minimax-duality` §15.5 as a likely ingredient (via
expressing a token's value in terms of its own dominant index) for a future, more refined attempt
at the still-open Local Claim of the Distinct-Bucket Lemma reduction.
