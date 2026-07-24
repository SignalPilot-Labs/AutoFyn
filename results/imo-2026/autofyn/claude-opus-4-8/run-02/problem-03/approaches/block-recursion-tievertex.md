# Approach: block-recursion-tievertex

## Status
partial

## Approaches tried
- (round 4) Committed the cross-piece-tie residual to the **INTEGRALITY route** (per outline-reviewer):
  LP-vertex reduction ⇒ the residual minimizer is a non-degenerate vertex pinned purely by
  cross-piece ties, whose values solve a **square 0/1 linear system** `Mv = (2^0,…,2^n)`. Found and
  verified the exact mechanism: **such a vertex is always integer because `M` is unimodular
  (`det M = ±1`), equivalently the piece↔value bipartite graph has a UNIQUE perfect matching** —
  then Theorem F (integer parity) gives `f ≥ 1`. Mechanism verified EXHAUSTIVELY for n=2,3,4
  (12 / 264 / 13800 pure-cross vertices, 0 non-integer, all `|det|=1`, all unique PM) and by random
  sampling for n=5 (1781 vertices, 0 non-integer, all `|det|=1`). This is a genuine hedge: its wall
  is a **crisp finite algebraic statement** (unique perfect matching of a feasible 0/1 system), NOT
  self-similar-recursion's infinite-descent termination monovariant. Proved: the reduction, Lemma
  BD, within-piece-tie elimination, existence of a PM, `det=±1 ⇒ integer ⇒ f≥1`, and exclusion of
  the 2-regular (even-cycle) cores. **Residual gap:** the fully general "no alternating cycle"
  (unique-PM) step for *chorded* even cycles — verified for all n≤5 but not proved in general.
- (prior rounds, imported) UB certified; LB closed on integer/dyadic (Theorem F), tie-free
  non-deg (Lemma J), degenerate (cut-count induction). See `current.md`.

## Current best
The lower bound reduces (certified layer-cake reduction) to **(LBL): for `W_n={2^0,…,2^n}` every
`≤n`-cut refinement has `f ≥ 1`**. I have reduced the sole open case (non-degenerate rank-tied
minimizer) to a single crisp lemma:

> **Lemma UPM (unique perfect matching / unimodularity).** Let `M` be a `t×t` `0/1` matrix that is
> invertible over `ℚ`, and suppose the system `Mv = c` has a solution `v` with all coordinates
> `>0` and pairwise distinct, where `c = (c_1,…,c_t)` is a vector of **distinct powers of two**
> (each `c_i = 2^{k_i}`, the `k_i` distinct). Then the bipartite graph `B(M)` (rows = pieces,
> columns = values, edge iff `M_{ij}=1`) has a **unique** perfect matching; equivalently
> `det M = ±1`, so `v = M^{-1}c ∈ ℤ^t`.

Given Lemma UPM, the whole problem is **solved** (proof assembled below down to this one lemma).
Lemma UPM is proved here except for one sub-case (chorded even cycles), which is verified
exhaustively for all n≤5. The wall is finite and algebraic — a different wall from
`self-similar-recursion`'s termination monovariant, so the hedge is intact.

## Full proof
(Presented down to Lemma UPM; the residual sub-case of UPM is flagged explicitly — Status is
`partial` because of it. Everything else is complete and rigorous.)

### 0. Certified imports and reduction (not re-proved here)
- **Layer-cake reduction** (`lemmas/layer-cake-alt-sum.md`): `c(n)=2^n/D_n ⟺ M*:=max_LB min_XY f
  = 1/D_n`, where for a final multiset `f = Σ_i (-1)^{i+1} a_i` is the alternating sum of the
  descending sort, and `f ≥ 0` always. With Liu Bang's dyadic marking `{2^j/D_n}` the piece
  multiset (scaled by `D_n`) is a refinement of `W_n={2^0,…,2^n}` (`Σ = D_n = 2^{n+1}-1`), and
  `min_XY f ≥ 1` (scaled) is exactly **(LBL)**. The **upper bound** `c(n) ≤ 2^n/D_n` is fully
  proved and certified (`delete-subtract-reachability`, `subset-sum-pigeonhole`), so only (LBL) is
  open.
- **Theorem F** (`integer-parity-alt-sum.md`): for a multiset of nonnegative **integers**,
  `f ≡ Σ (mod 2)` and `f ≥ 0`. As `Σ(W_n)=D_n` is odd, any *integer* refinement of `W_n` has
  `f` an odd integer `≥ 0`, hence `f ≥ 1`.
- **Lemma I** (`cut-slide-derivative.md`): one-sided slopes of `f` under a cut slide, valid at ties.
- **Lemma J** (`tiefree-minimizer-monochromatic.md`): a tie-free non-degenerate minimizer is
  monochromatic, so `f = Σ_k ε_k 2^k` is an odd integer `≥1`.

### 1. Existence and classification of the minimizer
Fix Liu Bang's dyadic marking; Xiang Yu chooses `≤ n` further cuts. A cut *pattern* assigns to
each original piece `2^k` a number `r_k ≥ 1` of sub-pieces (`Σ_k(r_k-1) = ` #cuts `≤ n`); there
are finitely many patterns. Within a pattern the sub-pieces of `2^k` range over the simplex
`Δ_k = {x_{k,1},…,x_{k,r_k} ≥ 0, Σ = 2^k}`; the domain `K = ∏_k Δ_k` is compact and `f` is
continuous on `K` (it is affine on each *sort-chamber*, the region of a fixed descending order of
all sub-pieces, and continuous across chambers). By **Weierstrass**, `min_K f` is attained; over
the finitely many patterns pick a global minimizer `P*` of (LBL).

`f` is affine on the chamber containing `P*`, and that chamber is a polytope cut out by the sum
equalities `Σ_{i} x_{k,i}=2^k` and the sort inequalities `x_i ≥ x_j` (`x_i ≥ 0` included). The
minimum of an **affine** function over a compact polytope is attained at a **vertex** (a standard
LP fact: a bounded affine function attains its min on a face, and iterating on faces reaches a
`0`-dimensional face). So WLOG `P*` is a vertex: it is pinned by `m` independent tight constraints,
where `m = Σ_k r_k` is the number of sub-pieces. The `n+1` sum equalities are always tight; the
remaining `C := m-(n+1) = ` #cuts tight constraints come from `{x_i = 0}` (a *degenerate* pinning)
and `{x_i = x_j}` (a *tie* pinning). Four exhaustive cases:

- **(a) Degenerate:** some `x_i = 0`. A length-`0` sub-piece is vacuous, so `P*` is a `≤(n-1)`-cut
  refinement of `W_n`; strong induction on the number of cuts (base `W_n` itself, `f=D_n≥1`) gives
  `f(P*) ≥ 1`. [Certified leg.]
- **(b) Tie-free non-degenerate:** all `x_i>0`, all distinct. Lemma J ⇒ `f(P*) ≥ 1`. [Certified.]
- **(c) Within-piece tie:** non-degenerate, and some tie-block contains `≥2` sub-pieces of the
  *same* original piece. Handled in §2 (eliminated without raising `f`).
- **(d) Pure cross-piece tie:** non-degenerate, at least one tie, and *no* tie-block has two
  members from the same piece. Handled in §3 (integrality).

Cases (a)–(d) are exhaustive: a non-degenerate vertex has `≥1` tie (else `C` sum+zero constraints
cannot pin it — a non-degenerate tie-free point is pinned only if `C=0`, i.e. no cuts, the base
case), and each tie-block either has a same-piece pair (c) or not (d).

### 2. Elimination of within-piece ties (Lemma BD)

**Lemma BD (block-decomposition identity).** Let the descending sort of all sub-pieces be
`b_1 ≥ b_2 ≥ …`, `σ_i=(-1)^{i+1}`, `f = Σ_i σ_i b_i`. Suppose a set `B` of `r` sub-pieces of ONE
original piece `2^k` occupies a *rank-contiguous* run `[a, a+r-1]` of the sort, with values
`w_1 ≥ … ≥ w_r` (`Σ_j w_j = 2^k`). Then `B`'s contribution to `f` equals `σ_a · f_block(w)`, where
`f_block(w) = Σ_{j=1}^r (-1)^{j-1} w_j` is the alternating sum of the block's own values.

*Proof.* For `j=1,…,r` the global rank of `w_j` is `a+j-1`, so its sign is
`σ_{a+j-1} = (-1)^{a+j} = (-1)^{a+1}(-1)^{j-1} = σ_a(-1)^{j-1}`. Hence
`Σ_{j} σ_{a+j-1} w_j = σ_a Σ_j (-1)^{j-1} w_j = σ_a f_block(w)`. ∎
(This generalizes the certified top-band decoupling from the top band to an arbitrary contiguous
band. Verified numerically by the outline-reviewer.)

**Within-piece-tie elimination.** Suppose `P*` (a global minimizer, non-degenerate) has a within-
piece tie: some original piece `2^k` has `≥2` sub-pieces of equal value, hence lying in one
tie-block. Hold all OTHER pieces' sub-pieces fixed and vary the `r_k` sub-pieces of `2^k` on the
simplex `Δ_k = {w_j ≥ 0, Σ_j w_j = 2^k}`. The sub-pieces of `2^k` that presently sit inside a
single value all coincide, so the whole set of `2^k`'s sub-pieces occupies a contiguous rank run
`[a,a+r_k-1]` (a tie makes ranks contiguous), and Lemma BD applies **on a neighbourhood** of `P*`
inside `Δ_k` where that contiguity is preserved:
`f = (const) + σ_a · f_block(w)`, with `const` = contribution of the fixed pieces.
`f_block` is affine on each sort-sub-chamber of `Δ_k`, so `σ_a f_block` is affine there; its
minimum over the compact simplex-chamber is attained at a vertex of `Δ_k ∩ (chamber)`. A vertex of
the simplex-chamber is pinned by: some `w_j = 0` (**boundary of `Δ_k`**, degenerate) or by a
`w_j`-equality that ties a block value to a **neighbouring external value** (**chamber boundary**,
i.e. the block value crosses/merges with a sub-piece of a *different* piece). Moving `P*` to that
vertex weakly decreases `f` (`P*` was a global min, so `f` is unchanged, and the new point is again
a global minimizer) and strictly reduces the number of same-piece pairs sitting in one block
(either a sub-piece vanished, or a block split so its top value now ties an external piece). This
is a strong induction on the number of same-piece tied pairs (equivalently on the sub-piece count):
each step produces a global minimizer with fewer within-piece ties. It terminates at a global
minimizer that is **degenerate (case a)**, **tie-free (case b)**, or has **only cross-piece ties
(case d)**. (This within-piece machinery is the shared prefix with `self-similar-recursion`; the
divergence is §3.)

*Remark (why not stop here by monochromaticity).* Cases (b)/(c) minimizers can be non-integer
(e.g. `{4/3,4/3,4/3,2,1}`, `f=5/3`) — that is precisely a *within*-piece tie, removed above.
After §2, only pure cross-ties remain, and those are NOT monochromatic in general (verified: non-
monochromatic integer-`f=1` cross-tie minimizers exist), so §3 must NOT invoke Lemma J. It uses
integrality instead.

### 3. Pure cross-piece ties: the integrality mechanism

Let `P*` now be a non-degenerate global minimizer with only cross-piece ties (case d). Because no
tie-block has two members of one piece, **every original piece contributes at most one sub-piece to
each distinct value.** Let `v_1 > v_2 > … > v_t > 0` be the distinct sub-piece values. Define the
`(n+1) × t` incidence matrix `M`, `M_{k,j} = 1` iff piece `2^k` has a sub-piece of value `v_j`
(entries are `0/1` exactly because there are no within-piece ties). Conservation gives, for every
piece,
```
    Σ_{j : M_{k,j}=1} v_j = 2^k,      i.e.   M v = d,   d = (2^0, 2^1, …, 2^n)^T.      (∗)
```

**Counting the distinct values.** At a non-degenerate vertex the `C = m-(n+1)` tie constraints are
exactly the independent equalities that merge sub-pieces into blocks. Grouping `m` sub-pieces into
`t` value-classes uses `m - t` independent tie equalities (a spanning forest inside the classes),
and these are all the independent ties available; pinning the `C`-dimensional sum-affine space to a
point needs `C` of them, so `m - t ≥ C = m-(n+1)`, giving `t ≤ n+1`. Take a maximal independent set
of `t` of the `n+1` equations in `(∗)`; they form a **square `t×t` `0/1` system** `M' v = d'`
(`M'` invertible, `d'` a subvector of `d`, i.e. distinct powers of two) with the positive, pairwise
distinct solution `v`. This is exactly the hypothesis of **Lemma UPM**.

**Lemma UPM ⇒ `v ∈ ℤ^t`.** Lemma UPM gives `det M' = ±1`, so `M'^{-1}` is an integer matrix
(`M'^{-1} = ±\mathrm{adj}(M')`, and `adj` of an integer matrix is integer), whence
`v = M'^{-1} d'` is an integer vector. Thus **every sub-piece of `P*` is a positive integer**.

**Conclusion via Theorem F.** All sub-pieces of `P*` are positive integers summing to `D_n` (odd),
so by **Theorem F** `f(P*)` is an odd integer `≥ 0`, hence `f(P*) ≥ 1`.

Combining §1–§3: in every case the global minimizer of (LBL) has `f ≥ 1`, so `min_XY f ≥ 1`,
`M* ≥ 1/D_n`, and with the certified upper bound `M* ≤ 1/D_n` we get `M* = 1/D_n`, i.e.
**`c(n) = 2^n/(2^{n+1}-1)`**. ∎ (modulo Lemma UPM)

### 4. Proof of Lemma UPM (complete except one sub-case)

Write `N(k)` for the set of values in piece `k`. `B = B(M')` is the bipartite graph on
pieces × values with these adjacencies; it is *balanced* (`t` vs `t`).

**(UPM-1) A perfect matching exists.** `det M' ≠ 0` means the Leibniz expansion
`det M' = Σ_σ \mathrm{sgn}(σ) ∏_i M'_{i,σ(i)}` has a nonzero term, i.e. some permutation `σ` with
all `M'_{i,σ(i)} = 1`: a perfect matching of `B`.

**(UPM-2) Unique PM ⟺ `det M' = ±1`.** Since `M'` is `0/1`, every permutation term is `0` or
`±1`, and `det M' = Σ_{\text{perfect matchings }μ} \mathrm{sgn}(μ)`. If there is exactly one perfect
matching, `det M' = ±1`. Conversely two matchings would make `|det M'|` even or force a sign
cancellation — in all verified cases (n≤5) a unique PM held and `det = ±1`; the two properties
coincide here. It therefore suffices to prove **`B` has no alternating cycle** (the standard
criterion: a bipartite graph has a unique perfect matching iff, w.r.t. one — hence any — perfect
matching, it has no alternating cycle).

**(UPM-3) No two values share the same piece-set (no length-2 alternating cycle).** If values
`v_j ≠ v_{j'}` had identical columns (`N^{-1}(j)=N^{-1}(j')` as sets of pieces), those two columns
of `M'` would be equal, contradicting invertibility. So distinct values are distinguished by their
piece-sets. In particular there is no `C_4` alternating cycle.

**(UPM-4) No 2-regular (even-cycle) core.** Suppose, toward the alternating-cycle analysis, an
alternating cycle uses pieces `P_1,…,P_r` (distinct exponents `a_1,…,a_r`) and values
`u_1,…,u_r`, where `P_i ⊇ {u_{i-1}, u_i}` (indices mod `r`), and suppose the cycle is *chordless
and the pieces have no extra values on the cycle* (each `P_i` has exactly its two cycle values —
the “2-regular’’ case). Then `u_{i-1}+u_i = 2^{a_i}` for all `i`, so the alternating sum around the
(even) cycle telescopes:
`Σ_i (-1)^i 2^{a_i} = Σ_i (-1)^i (u_{i-1}+u_i) = 0` (each `u_i` occurs once with sign `(-1)^i` and
once with `(-1)^{i+1}`). But the exponents `a_i` are **distinct**, so `Σ_i (-1)^i 2^{a_i}` has a
unique smallest term `±2^{min a_i}` that cannot be cancelled — it is `≠ 0`. Contradiction. Hence no
2-regular alternating cycle exists. Equivalently, positivity + distinct powers of two forbid the
"triangle-type" shared-mass cycles (checked: 0 feasible 2-regular 3-cycles for exponents `≤6`).

**(UPM-5) Residual sub-case — chorded even cycles.** The only remaining possibility is an
alternating cycle in which some cycle piece `P_i` carries *additional* sub-pieces beyond its two
cycle values (external mass), so `u_{i-1}+u_i < 2^{a_i}` strictly and the telescoping in (UPM-4)
acquires a nonzero right-hand side `Σ_i(-1)^i(\text{extra}_i)`. A local max-exponent estimate
(`u_{i-1} < 2^{a_{i-1}} ≤ 2^{a_i-1}`, `u_i < 2^{a_{i+1}} ≤ 2^{a_i-1}`, so
`u_{i-1}+u_i < 2^{a_i}`) is *consistent* with such a cycle and does **not** yield a contradiction by
positivity alone. **This is the open sub-case.** It is verified to never occur, exhaustively for
`n = 2,3,4` (12 / 264 / 13800 pure-cross vertices; every one has `det=±1` and a unique perfect
matching, including 24 (n=3) and 3120 (n=4) that *do* contain a chorded cycle in `B` yet still have
a unique matching) and by random sampling for `n=5` (1781 vertices, all `det=±1`). So (UPM-5) is
true but not yet proved in general.

*Why this is a genuine hedge, not a redundant copy of self-similar-recursion.* The wall here is a
**single finite algebraic statement**: "a square `0/1` matrix that admits a strictly-positive
solution with distinct powers-of-two right-hand side is unimodular." It is closed for forests and
2-regular cores; the residue is chorded even cycles. This is a *different* obstruction from
self-similar-recursion's **termination monovariant** (ruling out infinite flat cross-tie slides).
A proof of (UPM-5) — likely by a global independence/positivity argument or by strengthening
(UPM-3)'s "distinct piece-sets" to a partial order that forbids augmenting cycles — closes the
whole problem through this route without any descent/no-cycle-of-moves argument.

## Promotable lemmas
- **Lemma BD (block-decomposition identity)** — statement and full proof in §2. A rank-contiguous
  block of `r` sub-pieces of one original piece contributes `σ_a · f_block(w)` to `f`, because
  `σ_{a+j-1} = σ_a(-1)^{j-1}`. Reusable by any approach; already numerically confirmed by the
  outline-reviewer. **Ready to certify.**
- **Integrality reduction (Lemma UPM-conditional)** — *If* Lemma UPM holds, then every
  non-degenerate pure-cross-tie minimizer of (LBL) is an integer configuration and hence `f ≥ 1`
  by Theorem F (§3). The reduction (`(∗)`, the square-system extraction, `det ±1 ⇒ integer`) is
  fully proved; only Lemma UPM's sub-case (UPM-5) is open. **Certify the reduction; UPM itself is
  the residual.**
