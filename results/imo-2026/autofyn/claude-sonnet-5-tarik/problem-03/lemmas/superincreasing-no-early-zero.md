# Superincreasing No-Early-Zero Lemma

**Certified by:** proof-reviewer, round 5, from approach `dyadic-cascade-induction`
(round-5 builder, §5.3 Steps 3.1–3.6). Independently re-derived and re-verified by the
reviewer, both symbolically (re-checking every step of the token-invariant induction from
scratch) and computationally (exact-integer BFS: exhaustive state-space enumeration for
`D_m`, `m=1..5`, and 15 fresh random strictly superincreasing sequences of sizes 3–5,
zero violations in every case — see Verification below).

**Depends on:** the certified `lemmas/dm-operation-reformulation.md` (Lemma D/M, the
`D`/`M` operation definitions) and the elementary fact `e(M)=\sum_i(-1)^{i+1}m_i` for a
sorted descending multiset `M`.

## Statement

Let `a_1>a_2>\dots>a_k>0` be **strictly superincreasing**, i.e. `a_i>a_{i+1}+\dots+a_k`
for every `i<k`. Then for every legal sequence of `t<k` D/M operations starting from
`\{a_1,\dots,a_k\}`, the resulting active multiset `M_t` (which has exactly `k-t\ge1`
elements) satisfies `e(M_t)>0` strictly. In particular, no sequence of fewer than `k`
D/M operations ever reaches an active state with `e=0`.

(By the certified `lemmas/insertion-and-cascade-facts.md`, Fact 5, `e=0` *is* reachable
using exactly `k` operations — so `k` is exactly the threshold, not merely a bound.)

## Proof

**Step 1 (no vanishing signed subset sum).** For strictly superincreasing `a_1>\dots>a_k>0`,
any nonempty `S\subseteq\{1,\dots,k\}`, and any sign function `\varepsilon:S\to\{+1,-1\}`,
`\sum_{i\in S}\varepsilon(i)a_i\ne0`. *Proof:* let `i_0:=\min(S)`. Then
`|\sum_{i\in S\setminus\{i_0\}}\varepsilon(i)a_i|\le\sum_{i\in S\setminus\{i_0\}}a_i\le
\sum_{i=i_0+1}^k a_i<a_{i_0}` (superincreasing hypothesis, strict). Since the term at `i_0`
has absolute value exactly `a_{i_0}`, strictly larger than the rest of the sum's absolute
value, the reverse triangle inequality gives the total sum's absolute value `>0`.

**Step 2 (token invariant, induction on operation count).** Assign to every value `v` that is
ever active during a legal D/M sequence a pair `(S(v),\varepsilon(v))`: originals `a_i` get
`S(a_i)=\{i\}`, `\varepsilon(a_i)(i)=+1`; a value `v=x-y` created by `M(x,y)` gets
`S(v)=S(x)\sqcup S(y)`, `\varepsilon(v)=\varepsilon(x)` on `S(x)` and `-\varepsilon(y)` on
`S(y)`. By induction on the number of operations, **(I1)** the sets `S(v)` of all
simultaneously-active tokens are pairwise disjoint, and **(I2)** every active `v` satisfies
`v=\sum_{i\in S(v)}\varepsilon(v)(i)a_i` exactly. Base case: trivial (distinct singletons).
Inductive step: `D(x)` simply retires a token, preserving both invariants trivially; `M(x,y)`
combines two (by (I1), disjoint) index sets into a disjoint union, and (I2) follows by direct
substitution (`x-y=\sum_{S(x)}\varepsilon(x)a_i-\sum_{S(y)}\varepsilon(y)a_j=\sum_{S(v)}
\varepsilon(v)a_i`); the new set is disjoint from every other active set since each of `S(x)`,
`S(y)` already was.

**Step 3 (active tokens always positive and pairwise distinct).** By Step 2 + Step 1, every
active token `v=\sum_{S(v)}\varepsilon(v)a_i\ne0`; combined with `v\ge0` always (originals
positive, `M`-outputs are `x-y\ge0`), every active token is `>0`. For two distinct
simultaneously-active tokens `u\ne v`: by (I1) `S(u),S(v)` disjoint, so `u-v` is itself a
nonempty signed subset sum over `S(u)\sqcup S(v)`, hence `\ne0` by Step 1 — so `u\ne v` as
real numbers.

**Step 4 (conclusion).** Each D/M operation reduces the active count by exactly 1, so after
`t<k` operations exactly `k-t\ge1` tokens remain; by Step 3 they are pairwise distinct and
strictly positive. Sorting them `x_1>x_2>\dots>x_{k-t}>0` (strict, by distinctness),
`e=x_1-x_2+x_3-\dots` is a sum of at least one strictly positive paired difference (or a
strictly positive trailing singleton), hence `e>0`. `\blacksquare`

## Verification

Independently re-derived by the proof-reviewer step-by-step (Steps 1–4 re-checked from
scratch for logical validity, no gap found: the induction's base case, the `D`-operation case
(token retirement, no new ties possible), and the `M`-operation case (disjoint-union
well-definedness) were each traced explicitly). Independently re-verified computationally:
- Exhaustive exact-integer BFS over the *entire* D/M-reachable state space from `D_m`,
  `m=1,\dots,5` (not merely the minimizing path): the minimum number of operations needed to
  reach any `e=0` state is exactly `m+1=k` in every case, and `\min e` after exactly `m`
  operations is exactly `1` in every case — matching the Lemma's conclusion exactly.
- 15 freshly generated random strictly superincreasing integer sequences (sizes 3–5,
  independently constructed bottom-up so each `a_i` exceeds the sum of all later terms),
  exhaustively BFS-enumerated: minimum ops to `e=0` was exactly `k` (the sequence's own size)
  in every trial, zero violations, zero exceptions.

## Reusable by

Any approach needing a "no early cancellation" obstruction for a subtract-and-remove
operation sequence (D/M-style) on a superincreasing base multiset — directly the mechanism
behind `dyadic-cascade-induction`'s §5.3 unconditional proof that
`h(D_m,m)\ge e_m\cdot S(D_m)` for every `m` (the D/M-restricted lower bound). **Caveat,
carried over honestly:** this lemma is purely about the D/M-operation formalism. Promoting a
conclusion drawn from it to a bound on Xiang Yu's *true* physical strategy space additionally
requires `lemmas/dm-completeness-partial.md`'s conditional `g=h` result (open "all-cycles"
case) — not resolved by this lemma, and not claimed to be.
