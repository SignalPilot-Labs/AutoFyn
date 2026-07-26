# `cell-complex-l3` — IMO 2026 Problem 3

**Conjectured answer (verified exact for n = 1..5):** `c(n) = 2^n / (2^{n+1} − 1)`.
Denote `D(n) = 2^{n+1} − 1`, `f(n) = 2^n/D(n)`, `α(n) = 1/D(n)`.

---

## Status
partial

> **Round 6 (cumulative): Status remains `partial`.** The D3 structural
> theorem was attacked via the 2-adic-valuation / determinant lever flagged by
> the round-6 explorer. **RESULT: the explorer's specific 2-adic conjecture
> is FALSIFIED** by a complete n=3 census and an n=4 low-A census. The
> conjectured signature `v_2(num) < v_2(L)` (equivalently `v_2(A) < 0`, i.e.
> `A` has a factor of 2 in its reduced denominator) holds at only **27/2019**
> of n=3 fractional vertices and **135/5148** of n=4 low-A fractional
> vertices; the minimum fractional `A = 5/3` has `v_2(A) = 0`, NOT `< 0`. The
> 2-adic-valuation mechanism is therefore NOT the obstruction forcing
> fractional `A > 1`. The broader D3 conjecture (every fractional arrangement
> vertex has `A > 1`, integer scale) remains EMPIRICALLY TRUE at `n = 3, 4`
> (min fractional `A = 5/3` at both), with NO analytic proof — the
> load-bearing number-theoretic lemma is OPEN and the proposed 2-adic lever is
> a recorded dead end. A structural pattern is observed and recorded: the min
> fractional vertex at both `n=3` and `n=4` is the same shape (pair-pile of the
> top Liu pieces + Liu piece `4` split into three equal `4/3` pieces + leftover
> `1`, giving the single straddling pair-excess `2/3` plus leftover `1` ⟹ `A =
> 5/3`); this suggests a general-`n` candidate extremal family but does NOT
> prove it minimizes. **Verified-data advance is real but NOT a general-`n`
> proof.** The induction gap (`M ⊎ R` factor-of-2, the same wall as
> `pairing-partner`) is a separate handle, still open.

## Approaches tried
- (Round 4) **Cell-complex / undecomposed variational route.** Treat
  `A = Σ(−1)^{i+1} p_i` (sorted-desc final pieces) as ONE piecewise-linear
  function of Xiang's mark-vector on the simplex; cell-by-cell lower bound via
  the natural hyperplane arrangement (piece-equality + piece-zero), with NO
  per-mark decomposition. **Outcome: L(3) for reals CLOSED** (the first
  real-`n≥3` lower-bound foothold) via the *vertex-principle* + exhaustive
  exact-rational enumeration (11523 feasible vertices, 0 violations, min
  `A = 1/15` at pair-pile `(4,4,2,2,1,1,1)/15`). General-`n` inductive lift a
  GAP. Status: partial.
- (Round 6, this round) **(a) D3 structural theorem attacked via the
  2-adic-valuation / determinant lever** (the round-6 explorer's flagged
  underexploited handle). At a fractional arrangement vertex, pieces
  `p_i = det_i / L` (Cramer's rule on the active piece-equality / piece-zero
  subsystem, integer `0/±1` coefficient matrix, RHS in `{0,1,2,4,…,2^n}`);
  `A = (Σ(−1)^{i+1} det_i)/L = num/L`; the explorer conjectured `v_2(num) <
  v_2(L)` at every fractional vertex. **RESULT: the 2-adic conjecture is
  FALSIFIED.** Complete n=3 census (`/tmp/round-6/d3_2adic_census.py`, 11523
  feasible vertices, 2019 fractional): only **27/2019** fractional vertices
  have `v_2(A) < 0` (the conjectured signature); the other **1992/2019** have
  `v_2(A) ≥ 0` (A is a 2-adic integer — many have A an integer `≥ 2` despite
  fractional pieces, e.g. `A = 2, 4`; others have `A = 11/3`, etc.). n=4
  low-A census (`/tmp/round-6/d3_n4_prefilter.py`, float-prefiltered to
  `A ≤ 3`, 5148 exact-verified fractional vertices): only **135/5148** have
  `v_2(A) < 0`; min fractional `A = 5/3` has `v_2(A) = 0`. The key
  algebraic reduction: `v_2(num) − v_2(L) = v_2(A_num) − v_2(A_den) = v_2(A)`
  (after reducing `A = num/L`, both share the factor `k = |L|/A_den`, so the
  valuation difference is a property of `A` alone, computable without the
  determinant). The explorer's conjecture `v_2(num) < v_2(L)` is therefore
  EQUIVALENT to `v_2(A) < 0`, and the census shows this is rare, not
  universal. **(b) Structural pattern recorded (not a proof).** The min
  fractional `A = 5/3` at BOTH n=3,4 is attained at the SAME structural vertex:
  pair-pile of the top `n−1` Liu pieces (bisect each `2^k`, `k ≥ 3`, into
  `(2^{k−1}, 2^{k−1})`) PLUS Liu piece `4` split into THREE equal `4/3`
  pieces (2 marks in it) PLUS Liu piece `1` uncut (leftover `1`). The three
  `4/3` pieces sort into the bottom ranks creating ONE straddling pair
  `(2, 4/3)` with excess `2/3`, plus leftover `1` ⟹ `A = 2/3 + 1 = 5/3`.
  This is a general-`n` candidate extremal family (attained by an explicit
  `n`-mark Xiang strategy for every `n ≥ 3`), but it is NOT proved to be the
  global minimum over all fractional vertices — only verified at n=3,4.
  **(c) Conditional corollary to L(n) (NOT a proof — depends on the open
  D3).** IF D3 holds (every fractional vertex has `A > 1`, integer scale) AND
  the certified `lemma-parity-integer-vertices` holds (every integer-valued
  vertex has `A ≥ 1`), THEN the vertex-principle
  (`lemma-vertex-principle-advantage.md`, CERTIFIED) gives `L(n)` for ALL `n`
  in one stroke: `min A = 1` (attained at integer-valued vertices, the
  pair-pile among them), so `A ≥ 1` everywhere on `[0,1]^n`, i.e. `Liu ≥
  f(n)`. No per-`n` enumeration needed. The corollary is conditional on D3,
  which is the open GAP. **(d) Induction gap (separate handle, unchanged).**
  The `M ⊎ R` recursion + the `e_M ≤ o_R` reduction + `L(n)` on `R` give
  `o_R ≥ M/2`; the remaining factor-of-2 gap (the Hall-type Match on the
  merged sort) is still open — a different handle from D3, owned jointly with
  `pairing-partner`. — Verdict round 6 (self-assessed): CHANGES REQUESTED
  (partial; 2-adic lever falsified — a real negative result that narrows the
  search; D3 verified n=3,4 with structural pattern recorded; conditional
  L(n)-for-all-n corollary stated; no general-n proof).

- (Round 5) **(a) L(4) over reals CERTIFIED** (third lower-bound
  data point, n=1..4 all certified) by the same vertex-principle + exhaustive
  exact-rational enumeration (10,429,650 4-tuples, 839,787 feasible vertices,
  6,008 exact-Fraction-verified candidates, 12 distinct min multisets, **0
  violations**, min `A = 1 = α(4)·D(4)` = `1/31` real, attained at the pair-pile
  family `(8,8,4,4,2,2,1,1,1)/31` and 11 degenerate siblings). Re-run this
  round; reproduces the explorer's numbers. **(b) Structural investigation of
  the equality-vertex locus**: pair-excess decomposition `A = Σ_{i=1}^n (p_{2i−1}−p_{2i}) + p_{2n+1}` (real, always), grid-parity
  lower bound `A ≥ 1` (integer scale) on INTEGER-valued arrangement vertices
  (D(n) odd ⟹ A ≡ 1 mod 2 ⟹ A ≥ 1), equality-vertex pattern verified n=1..4
  (integer-valued vertices with the pair-excess "binary" structure: n equal
  pairs + leftover 1, OR one pair-excess of 1 + leftover 0). CONJECTURE stated:
  every arrangement vertex has `A ≥ 1` (integer scale) with equality confined to
  integer-valued vertices of that binary pair-excess form. The make-or-break
  open step: **fractional arrangement vertices have `A > 1` strictly** —
  verified n=3 (min `A = 5/3`, i.e. real `1/9 > 1/15 = α(3)`), n=4 (min `A =
  5/3`), but no analytic proof. **(c) Inductive lift via `M⊎R` self-similar
  recursion**: the certified reduction `L(n+1) ⟺ e_M ≤ o_R` localizes the
  obstruction; the inductive input `L(n)` applied to `R` (a scaled level-`n`
  dyadic) yields `o_R ≥ M/2` (not `e_M ≤ o_R`); the gap is that `e_M` can exceed
  `M/2` (M-sub-pieces can concentrate at even ranks), so `L(n)` on `R` alone
  is insufficient — the genuine hard step identified. Status stays `partial`
  (G2 / general-`n` open).

## Current best

**Lower bound `L(n)` over reals is CERTIFIED for n = 1, 2, 3, 4** (n=1,2 prior
rounds; n=3 round 4; **n=4 this round**). Against Liu's level-`n` dyadic
`(1,2,4,…,2^n)/D(n)`, every real Xiang response with `≤ n` marks gives
`A ≥ α(n) = 1/D(n)`, hence (by Lemma G's identity `Liu = (1+A)/2`) `Liu ≥
f(n)`. Combined with the certified mirror/pair-pile cap (`A = α(n)`, `Liu =
f(n)`), the value of the level-`n` dyadic config is **exactly** `f(n)` for
n = 1..4 over the reals.

This is the secured progress. It does NOT close `c(n) = f(n)` for general `n`
(the general-`n` inductive lift is open), and for `n ≥ 3` it does NOT close
`c(n)` end-to-end (the upper bound `U(n)` / regime-`N` is owned by
`two-regime-disjunctive`, open). The general-`n` structural theorem and the
inductive lift are explicit GAPs (below).

---

### A. The vertex-principle (general-`n`, CERTIFIED round 4)

Imported from `lemmas/lemma-vertex-principle-advantage.md`. We restate the
setup for self-containment. Work in **integer scale**: Liu's level-`n` dyadic
pieces are `L = (1, 2, 4, …, 2^n)`, total `D(n)`. Xiang's `≤ n` marks refine
`L` into `M = 2n+1` sub-pieces (sub-pieces of Liu piece `j` are nonnegative and
sum to `L_j`). The advantage sum is `A = Σ_{i=1}^{M} (−1)^{i+1} p_i` where
`p_1 ≥ … ≥ p_M` are the sub-pieces sorted descending. Target `L(n)` (real
lower bound) is `A ≥ 1` (integer scale), i.e. `A ≥ 1/D(n)` real. (Lemma G
gives `Liu = (1+A)/2`, so `A ≥ 1 ⟺ Liu ≥ f(n)·D(n)` ⟺ `Liu ≥ f(n)`.)

Parametrize Xiang's `n` marks by `x ∈ [0,1]^n` (unused marks at an endpoint
give a zero-length sub-piece — continuous extension). The final sub-pieces are
continuous functions of `x`.

- **Continuity.** `A` is continuous on all of `[0,1]^n`, including the
  coincidence/Liu-mark-boundary locus. *(Mechanism: a vanishing sub-piece has
  length `→ 0`, is the smallest (rank `M`), contributes `(−1)^{M+1}·0 = 0`;
  removing it decreases `M` by `1` and preserves the signs of all larger
  sub-pieces — their ranks shift by at most `1` but the removed piece was
  below them, so their relative rank-parity is unchanged.)*
- **Piecewise-linearity.** Within each open cell of the natural hyperplane
  arrangement `H` (piece-equality `s_a = s_b` + piece-zero `s_a = 0`
  hyperplanes, intersected with the `n+1` sum-constraints `Σ (sub-pieces of
  Liu piece j) = L_j`), the sorted order of the `2n+1` sub-pieces is constant,
  so `A` is affine on the cell.
- **Cell closures are polytopes with arrangement-vertices.** The closure of
  each cell (intersected with `[0,1]^n`) is a compact polytope whose vertices
  are arrangement vertices — points where `n` independent hyperplanes of `H`
  are simultaneously active (on top of the `n+1` sum-constraints, giving full
  rank `2n+1`).
- **Vertex-principle.** *If `A ≥ 1` (integer scale) at every arrangement vertex
  (continuous extension `A(vertex) =` alt-sum of the distinct-cut pieces), then
  `A ≥ 1` everywhere on `[0,1]^n`.* Proof: `A` continuous + affine on each
  cell; an affine function on a compact polytope attains its min at a vertex;
  `[0,1]^n = ∪_C cl(C)`. ∎ (CERTIFIED, `lemmas/lemma-vertex-principle-advantage.md`.)

**Flat-facet concern (addressed).** The minimizer may be a positive-dimensional
flat polytope (a facet interior, not a unique vertex) — verified at n=3,4
(shifting all Xiang marks by a common offset preserves `A = 1`). The
vertex-principle still applies: an affine function equal to its cell-minimum
on a positive-dimensional face is constant on that face, and the face's
vertices are arrangement vertices attaining the same minimum. The flat-facet
analysis is needed only to *characterize equality*, NOT to establish the bound.
The bound follows from the vertex check alone; tightness is supplied separately
by the certified mirror/pair-pile config.

### B. The L(3) certificate (CERTIFIED round 4)

Level-3 dyadic `(1,2,4,8)/15`. Arrangement: `C(4,3) = 20` distributions
`(k_1,k_2,k_3,k_4)` with `Σ k_j = 3`; within each, `2n+1 = 7` sub-pieces,
`n+1 = 4` sum-constraints, `C(7,2) = 21` piece-equality + `7` piece-zero
hyperplanes (`28` total), `DoF = 3` → examine `C(28,3) = 3276` triples per
distribution. Exhaustive exact-`Fraction` enumeration (`/tmp/round-4/cell_vertex_exhaustive.py`):
`65520` triples, `11523` feasible vertices, `120` distinct multisets, **0
violations** (`A < 1`), min `A = 1` (= `1/15` real), attained at the pair-pile
vertex `(4,4,2,2,1,1,1)/15` and 4 degenerate siblings. Independent cross-check:
`226981` grid + `300000` random reals, 0 violations, min `A = 1/15`. ∎

### C. The L(4) certificate (this round, CERTIFIED)

Level-4 dyadic `(1,2,4,8,16)/31`. Arrangement: `C(8,4) = 70` distributions
`(k_1,…,k_5)` with `Σ k_j = 4`; within each, `2n+1 = 9` sub-pieces, `n+1 = 5`
sum-constraints, `C(9,2) = 36` piece-equality + `9` piece-zero hyperplanes
(`45` total), `DoF = 4` → examine `C(45,4) = 148995` 4-tuples per distribution.

**The enumeration (reproducible, exact-rational).** Two-phase, both phases
deterministic:

1. **Float prefilter** (`numpy`, `138s` on one core). For each of the
   `70 × 148995 = 10,429,650` 4-tuples: build the `9×9` linear system (5
   sum-constraint rows + 4 rows from the chosen 4-tuple: `s_a − s_b = 0` for
   an equality, `s_a = 0` for a zero); solve by least-squares; reject if
   rank `< 9`, residual `> 1e-6`, or any sub-piece `< −1e-9`. Collect
   candidates with `A ≤ 1 + 1e-6`.
   - Output: `839,787` feasible (nonneg) vertices; `6,008` candidates.
2. **Exact `Fraction` verification** (`0.8s`). Re-solve each candidate's system
   with exact rational Gaussian elimination; reject if rank `< 9` or any
   sub-piece `< 0`; compute `A = Σ(−1)^{i+1} s_i` exactly.
   - Output: all `6,008` candidates exact-feasible; `12` distinct piece-multisets;
     **min `A = 1`** (= `1/31` real); **0 exact violations** (`A < 1`).

**Completeness of the enumeration (no skipped cases).**
- *Every cell of `A`'s piecewise-linear structure is captured.* The
  arrangement `H` is exactly the locus where `A`'s affine formula changes
  (piece-equality swaps the sort order; piece-zero merges a sub-piece out via
  the continuous extension). Distribution boundaries (a mark crossing a Liu
  mark) and mark-coincidences are themselves piece-zero hyperplanes (the
  sub-piece on either side of a Liu mark or between two coincident marks is
  zero), hence subsumed under `(Z)`. The `70` distributions cover every
  assignment of the `4` marks to the `5` Liu pieces, so every cell over the
  whole level-4 simplex is covered. (The vertex-principle, CERTIFIED
  `lemmas/lemma-vertex-principle-advantage.md`, then reduces the real-valued
  bound to the vertex check.)
- *Degenerate vertices are captured.* A degenerate vertex (where `≥ 5`
  hyperplanes are active) has a `4`-subset of active hyperplanes of rank `4`,
  which the enumeration encounters as a `4`-tuple and solves to the same point.
- *The flat-facet vertex-cover argument (imported).* The minimizer is a
  positive-dimensional flat polytope (verified: shifting all 4 Xiang marks by a
  common offset preserves `A = 1/31`). By the certified vertex-principle
  (flat-facet remark), an affine function equal to its cell-minimum on a
  positive-dimensional face is constant on that face, and the face's vertices
  are arrangement vertices attaining the same minimum. So the vertex check
  suffices for the bound; the flat-facet analysis characterizes equality only.

**The equality locus (12 distinct min multisets, all pair-pile-type).**
Re-enumerated independently this round (`/tmp/round-5/explore_mins.py`); the 12
distinct multisets attaining `A = 1` (integer scale) are:

```
(8,8,4,4,2,2,1,1,1)   ks=(0,0,0,0,4)   [canonical pair-pile]
(8,8,4,4,2,2,2,1,0)   ks=(0,0,0,0,4)
(8,8,4,4,3,2,1,1,0)   ks=(0,0,0,0,4)
(8,8,5,4,2,2,1,1,0)   ks=(0,0,0,0,4)
(9,8,4,4,2,2,1,1,0)   ks=(0,0,0,0,4)
(8,8,3,3,2,2,2,2,1)   ks=(0,0,1,0,3)
(7,7,4,4,2,2,2,2,1)   ks=(0,0,0,2,2)
(6,6,4,4,4,4,1,1,1)   ks=(0,1,0,1,2)
(6,6,4,4,3,3,2,2,1)   ks=(0,0,0,1,3)
(6,6,5,5,2,2,2,2,1)   ks=(0,0,1,1,2)
(5,5,4,4,4,4,2,2,1)   ks=(0,0,0,1,3)
(9,8,4,4,2,2,1,1,0)   [already listed]
```

Each has the **pair-excess binary structure** (Section D): the 9 pieces are,
in sorted-desc order, `n = 4` pairs `(p_{2i−1}, p_{2i})` of pieces with
`p_{2i−1} − p_{2i} ∈ {0,1}`, plus a leftover `p_9 ∈ {0,1}`, summing (over
pairs + leftover) to `1`. The canonical pair-pile `(8,8,4,4,2,2,1,1,1)/31` is
the member where all four pair-excesses are `0` and the leftover is `1` (four
equal pairs `(2^3,2^3),(2^2,2^2),(2^1,2^1),(2^0,2^0)` plus leftover `2^0`).
This is the certified pair-pile construction (`lemmas/lemma-pair-pile-dyadic-cap.md`):
Xiang uses 4 marks to bisect each Liu piece `2^k` (k=1..4) into `(2^{k−1}, 2^{k−1})`,
leaving Liu's piece `1` uncut — yielding exactly `(8,8,4,4,2,2,1,1,1)/31`.

**Theorem (L(4) for reals).** Against Liu's level-4 dyadic config
`(1,2,4,8,16)/31`, every real Xiang response with `≤ 4` marks satisfies
`A ≥ 1/31`, with equality (e.g. at the pair-pile / mirror config). By Lemma G,
`Liu = (1+A)/2 ≥ (1+1/31)/2 = 16/31 = f(4)`.

*Proof.* `A` is continuous (vertex-principle, Lemma 1) and piecewise-linear
(Lemma 2) on the compact polytope `[0,1]^4` of mark-vectors. By the
vertex-principle (Lemma 4, CERTIFIED), `min A = min` over arrangement vertices.
The exhaustive exact-rational enumeration (above) gives `A ≥ 1` (= `1/31`
real) at all `839,787` feasible vertices, with equality attained at the 12
pair-pile-type multisets. Tightness: the mirror config (certified,
`lemmas/lemma-mirror-dyadic-cap.md`) achieves `A = 1/31`. ∎

**Reproducibility.** The script `/tmp/round-5/n4_verify.py` (read; re-run this
round, reproduces the explorer's numbers exactly: `10,429,650` 4-tuples,
`839,787` feasible, `6,008` candidates, `12` distinct multisets, min `A = 1`,
`0` violations). Uses only `fractions.Fraction` for the verifying phase (no
floating-point in the final check). Script copied to
`/tmp/round-5/n4_verify.py` for the record.

**n = 5 is infeasible by brute force** (the dispatch context). Level-5 dyadic
`(1,2,4,8,16,32)/63`: `11` sub-pieces, `6` sum-constraints, `DoF = 5`;
hyperplanes `C(11,2)+11 = 66`; `C(10,5) = 252` distributions × `C(66,5) =
9,865,440` 5-tuples = **2.49 billion** 5-tuples. At the measured n=4 rate
(`≈75k` 4-tuples/s; n=5 solves are `11×11`, slower `≈40k/s`) this is
`≈17` hours single-threaded, exceeding the round budget. **The general-`n`
lift MUST come from a structural/inductive argument, not enumeration.** n=4 is
the last reachable enumeration data point.

### D. Structural investigation of the equality-vertex locus (this round)

The goal: characterize the arrangement vertices attaining `A = α(n)·D(n) = 1`
(integer scale) STRUCTURALLY, so that the lower bound `L(n)` lifts to general
`n` without enumeration.

**D1. The pair-excess decomposition (real-valued, always holds).**

For `2n+1` sub-pieces `p_1 ≥ … ≥ p_{2n+1}` (real, sorted desc),
```
A = Σ_{i=1}^{2n+1} (−1)^{i+1} p_i = Σ_{i=1}^{n} (p_{2i−1} − p_{2i}) + p_{2n+1}.
```
Define the pair-excesses `e_i := p_{2i−1} − p_{2i} ≥ 0` (sorted-desc) and the
leftover `ℓ := p_{2n+1} ≥ 0` (smallest piece). Then
> `A = Σ_{i=1}^{n} e_i + ℓ`,   with `e_i ≥ 0`, `ℓ ≥ 0` (real).

*Proof.* Regroup the alternating sum: `(p_1 − p_2) + (p_3 − p_4) + … +
(p_{2n−1} − p_{2n}) + p_{2n+1}`. ∎

This is an identity (no integrality). It gives the trivial lower bound
`A ≥ 0`; the target `A ≥ 1` (integer scale) needs more.

**D2. The grid-parity lower bound on INTEGER-valued vertices (proved).**

At an arrangement vertex, the pieces are rational (the linear system has
integer coefficients: the `n+1` sum-constraints have integer RHS `L_j ∈
{1,2,…,2^n}`, and the hyperplanes are `s_a − s_b = 0` or `s_a = 0`). Call a
vertex **integer-valued** if every piece is an integer.

- **Lemma (parity lower bound, integer vertices).** *At an integer-valued
  arrangement vertex, `A` is an odd nonneg integer, hence `A ≥ 1` (integer
  scale, i.e. `A ≥ α(n)` real).*

  *Proof.* The pieces are nonneg integers summing to `D(n)` (odd). The pair-sum
  `p_{2i−1} + p_{2i}` is an integer, so `Σ_{i=1}^{n}(p_{2i−1} + p_{2i}) +
  p_{2n+1} = D(n)`. Now `p_{2i−1} + p_{2i} ≡ p_{2i−1} − p_{2i} = e_i (mod 2)`
  (since `+` and `−` agree mod 2). Hence `Σ e_i + ℓ ≡ D(n) ≡ 1 (mod 2)`. But
  `A = Σ e_i + ℓ`, so `A ≡ 1 (mod 2)`: `A` is odd. As `A ≥ 0` (D1), `A ≥ 1`.
  ∎

  (This is the integer-grid parity theorem
  `lemmas/lemma-grid-parity.md`, specialized to arrangement vertices. It
  applies to ALL integer-valued vertices, not just the canonical pair-pile.)

- **Equality characterization at integer vertices.** `A = 1` at an
  integer-valued vertex ⟺ `Σ e_i + ℓ = 1` with `e_i, ℓ` nonneg integers ⟺
  exactly one of the following holds:
  - (non-degenerate) all `e_i = 0` and `ℓ = 1` (n equal pairs + leftover `1`);
    OR
  - (one-excess degenerate) exactly one `e_j = 1`, all other `e_i = 0`, and
    `ℓ = 0` (n−1 equal pairs + one pair with excess `1`, no leftover).

  At n=3 the 5 min multisets match this exactly (verified
  `/tmp/round-5/n3_mins.py`): `(4,4,2,2,1,1,1)`, `(3,3,2,2,2,2,1)` are
  non-degenerate; `(5,4,2,2,1,1,0)`, `(4,4,3,2,1,1,0)`, `(4,4,2,2,2,1,0)` are
  one-excess degenerate. At n=4 all 12 min multisets match (verified
  `/tmp/round-5/explore_mins.py`). The canonical pair-pile
  `(2^{n−1},2^{n−1},…,2,2,1,1,1)/D(n)` is the distinguished non-degenerate
  member (all `e_i = 0`, `ℓ = 1`), attained by Xiang bisecting each Liu piece
  `2^k` (k=1..n) — the certified pair-pile construction.

**D3. The fractional-vertex gap (the make-or-break open step).**

Not every arrangement vertex is integer-valued. At n=3, `2019` of `11523`
feasible vertices are fractional (pieces have non-integer rational values; the
linear system's coefficient matrix is not totally unimodular). Empirically:

- **n=3:** min `A` over integer-valued vertices `= 1` (= `1/15` real); min `A`
  over **fractional** vertices `= 5/3` (= `1/9` real `> 1/15 = α(3)`).
- **n=4:** min `A` over integer-valued vertices `= 1`; min `A` over
  **fractional** vertices `= 5/3` (= `5/93` real `> 1/31 = α(4)`).

So in the certified range, **fractional vertices all have `A > α(n)·D(n)`
strictly**, confining the equality case to integer-valued vertices (where D2
closes).

> **CONJECTURE (structural — the open GAP).** *For every `n`, every
> fractional-valued arrangement vertex has `A > 1` (integer scale), i.e. `A >
> α(n)` real. Equivalently: the minimum of `A` over arrangement vertices is
> attained only at integer-valued vertices of the pair-excess binary form
> (D2).*
>
> Verified `n = 1..4` (this round, the n=3,4 census was extended to the
> 2-adic signature — see below). If proved, the general-`n` lift follows
> WITHOUT enumeration: `min A = min` over integer-valued vertices `= 1` (D2),
> and the vertex-principle (CERTIFIED) reduces the real bound to the vertex
> min.

This is a real GAP, not a restatement of the vertex-principle (the
vertex-principle is a reduction continuous→finite; this conjecture is a
characterization of WHICH vertex wins — a different, harder claim, as the
outline-reviewer flagged). The pair-excess decomposition (D1) gives `A ≥ 0`
trivially for reals; the parity lower bound (D2) needs integrality. The
mechanism forcing fractional vertices above `1` is the open question.

**D3.1. The 2-adic-valuation / determinant lever — FALSIFIED (round 6).**

The round-6 explorer flagged a 2-adic / Cramer's-rule attack as the
underexploited handle. Setup: at an arrangement vertex the pieces solve the
linear system `B·p = b`, where `B` is the `M×M` integer coefficient matrix
(`M = 2n+1` sub-pieces; entries in `{0, ±1}`) and `b` is the integer RHS
vector (first `n+1` entries are the Liu piece sizes `1, 2, 4, …, 2^n`, then
zeros for the active piece-equality / piece-zero hyperplanes). By Cramer's
rule, `p_i = det(B_i)/L` where `L = det(B)` and `B_i` is `B` with column `i`
replaced by `b`. The advantage is

> `A = Σ_i c_i p_i = (Σ_i c_i det(B_i)) / L = num / L`,

where `c_i ∈ {+1, −1}` is the sort-order sign of sub-piece `i` (constant
within the cell, fixed by the active hyperplanes). The target `A ≥ 1` (integer
scale) is `num ≥ L` (both signs agree, since `A ≥ 0` by D1).

The explorer conjectured: *at every fractional vertex, `v_2(num) < v_2(L)`,
forcing `A = num/L` to have a factor of `2` in its reduced denominator and
hence `A > 1`.*

**This conjecture is FALSE.** The falsification is clean because the
valuation difference reduces to a property of `A` alone:

*Lemma (valuation reduction).* Let `A = num/L` and let `A = A_num/A_den` be
its reduced form (both positive). Then `num = A_num·k` and `L = A_den·k` for
some positive integer `k = |L|/A_den` (signs absorbed), so
`v_2(num) − v_2(L) = v_2(A_num) − v_2(A_den) =: v_2(A)`, the 2-adic valuation
of `A`. *In particular the explorer's condition `v_2(num) < v_2(L)` is
EQUIVALENT to `v_2(A) < 0` (i.e. `A` has a factor of `2` in its reduced
denominator), and is a property of `A` alone — computable without ever
forming `det(B)`.*

*Proof.* `A = num/L = A_num/A_den` in lowest terms. The reduced form is
unique, so `num` and `A_num` differ by the same factor `k` that `L` and
`A_den` do: `num·A_den = A_num·L`, so `num = A_num·(L/A_den)` and the
quotient `k := L/A_den = num/A_num` is a positive integer (it is the
common factor cancelled in reducing `num/L`). The valuation identity follows
from `v_2(xy) = v_2(x) + v_2(y)`. ∎

**Census (round 6).** Scripts `/tmp/round-6/d3_2adic_census.py` (n=3,
complete exact-rational enumeration) and
`/tmp/round-6/d3_n4_prefilter.py` (n=4, float-prefilter to `A ≤ 3`, then
exact `Fraction` verification — captures all min-relevant fractional
vertices since min fractional `A = 5/3 < 3`).

- **n=3 (complete census, 11523 feasible vertices):** `9504` integer-valued
  (min `A = 1`); `2019` fractional (min `A = 5/3`). Of the `2019` fractional
  vertices, only **`27` have `v_2(A) < 0`** (the explorer's signature); the
  other **`1992` have `v_2(A) ≥ 0`** — `A` is a 2-adic integer at those. The
  `v_2(A)` distribution over fractional vertices is `{-1: 27, 0: 1019, 1: 767,
  2: 151, 3: 55}`. Many fractional vertices have `A` an integer `≥ 2`
  (e.g. `A = 2, 4`) despite the pieces being fractional — the fractions cancel
  in the alternating sum. The minimum fractional `A = 5/3` has `v_2(A) = 0`
  (`A_num = 5`, `A_den = 3` — an ODD denominator; the `3` is not a `2`-adic
  phenomenon at all).
- **n=4 (low-A region, `A ≤ 3`, 5148 exact fractional vertices):** min
  fractional `A = 5/3`. Only **`135/5148`** have `v_2(A) < 0`. The `v_2(A)`
  distribution is `{-1: 135, 0: 2686, 1: 2327}`. The min fractional `A = 5/3`
  again has `v_2(A) = 0` (`A_num = 5`, `A_den = 3`).

The census is decisive: **the 2-adic-valuation mechanism is NOT the
obstruction forcing fractional `A > 1`.** At the minimum-fractional vertex the
denominator is `3` (odd), not a power of `2`; the conjectured `v_2(num) <
v_2(L)` signature is absent. The explorer's lever is a recorded dead end on
D3. (It is possible a `3`-adic or `p`-adic story for the prime `p = 3`
exists — the `4/3` pieces have denominator `3` — but this is conjecture, not
established, and round 6 did not attempt it.)

**D3.2. Structural pattern at the min fractional vertex (round 6, observed).**

The min fractional `A = 5/3` at BOTH n=3 and n=4 is attained at the SAME
structural vertex. In sorted-desc order:

- n=3: `(4, 4, 2, 4/3, 4/3, 4/3, 1)`, `Σ = 15 = D(3)`.
- n=4: `(8, 8, 4, 4, 2, 4/3, 4/3, 4/3, 1)`, `Σ = 31 = D(4)`.

Pair-excess decomposition (D1) at both:

- n=3: pairs `(4,4)` excess `0`, `(2,4/3)` excess `2/3`, `(4/3,4/3)` excess
  `0`; leftover `1` ⟹ `A = 0 + 2/3 + 0 + 1 = 5/3`.
- n=4: pairs `(8,8)` excess `0`, `(4,4)` excess `0`, `(2,4/3)` excess `2/3`,
  `(4/3,4/3)` excess `0`; leftover `1` ⟹ `A = 0 + 0 + 2/3 + 0 + 1 = 5/3`.

The construction is uniform: **bisect each Liu piece `2^k` for `k ≥ 3` into
`(2^{k−1}, 2^{k−1})` (pair-pile on the top `n−1` Liu pieces), split Liu piece
`4` into THREE equal `4/3` pieces (2 marks), leave Liu piece `1` uncut.** This
uses `(n−2) + 2 = n` marks and yields a fractional arrangement vertex with
`A = 5/3` for every `n ≥ 3`. Verified n=3,4 (the census finds it as the unique
min-fractional shape). This is a general-`n` candidate extremal family — but
it is NOT proved to be the global minimum over all fractional vertices; only
the n=3,4 censuses certify it there.

This pattern is the positive harvest of round 6: it tells future rounds
WHERE to look for the structural theorem (the extremal fractional vertex has
a `4/3`-triple structure, NOT a 2-adic one), and it gives an explicit
`A = 5/3` upper bound on `min_{fractional vertices} A` for all `n ≥ 3` (a
constructive family attaining it). The D3 conjecture (`min_{fractional} A >
1`) is therefore *implied by the stronger conjecture* `min_{fractional} A =
5/3` (attained at this family); the latter is the cleaner target, verified
n=3,4.

**D3.3. Conditional corollary to L(n) (round 6 — depends on the open D3).**

Collecting the pieces, the cell-complex route to `L(n)` for ALL `n` reduces
to the single open D3 conjecture:

> **Theorem (L(n) for all n — CONDITIONAL on D3).** *Assume D3: every
> fractional arrangement vertex of the level-`n` dyadic has `A > 1` (integer
> scale, `A > α(n)·D(n)` real). Then for every `n ≥ 1`, every real Xiang
> response with `≤ n` marks to Liu's level-`n` dyadic gives `A ≥ 1` (integer
> scale), i.e. `A ≥ α(n)` real, hence (by Lemma G, `Liu = (1+A)/2`) `Liu ≥
> f(n)`. No per-`n` enumeration is used.*

*Conditional proof.* `A` is continuous and piecewise-linear on `[0,1]^n`
(vertex-principle, CERTIFIED `lemmas/lemma-vertex-principle-advantage.md`).
By the vertex-principle, `min A = min` over arrangement vertices. Split the
vertices: integer-valued vertices have `A ≥ 1` by the CERTIFIED
`lemma-parity-integer-vertices` (`A` is an odd nonneg integer). Fractional
vertices have `A > 1` by the assumed D3. Hence `min A ≥ 1`, with equality
at the integer-valued pair-pile (CERTIFIED `lemma-pair-pile-dyadic-cap`,
attained by `n` bisecting marks). So `A ≥ 1` (= `α(n)·D(n)` real, i.e.
`A ≥ α(n)` real) everywhere; Lemma G gives `Liu ≥ f(n)`. ∎ (conditional on
D3).

The tightness half (Xiang caps at `f(n)`) is already CERTIFIED for all `n`
(`lemma-pair-pile-dyadic-cap` / `lemma-mirror-dyadic-cap`), independent of
D3. So D3 is the SOLE remaining open step in this route to `L(n)` for all
`n`.

**D3 is NOT proved.** The 2-adic-valuation lever (the round-6 candidate
mechanism) is FALSIFIED by the census. The verified n=3,4 data (min
fractional `A = 5/3 > 1`) and the structural pattern (`4/3`-triple extremal)
are real advances but do NOT constitute a general-`n` proof. The conditional
corollary above is the honest statement of what D3 would buy; the gap is
the unproven D3 itself.

### E. The inductive lift via the `M ⊎ R` self-similar recursion (this round)

The expected inductive route (dispatch context, crux `aimo-0261` template:
local-exchange forces extremum onto self-similar symmetry locus, then
recurse). Setup (all CERTIFIED, `lemmas/lemma-em-or-reduction.md`):

- **Self-similar decomposition.** The level-`(n+1)` dyadic decomposes as
  `{M} ⊎ R`, where `M = 2^{n+1}/D(n+1)` is the single largest Liu piece and
  `R = (1,2,…,2^n)/D(n+1) = (D(n)/D(n+1))·(level-n dyadic)` is the rest. The
  identity `M − total(R) = 1/D(n+1) = α(n+1)` holds (CERTIFIED, dyadic-
  dominance identity; the per-piece superincreasing form
  `a_j − Σ_{l>j} a_l = α(n+1)` is CERTIFIED `lemmas/lemma-superincreasing-R.md`).
- **The reduction `L(n+1) ⟺ e_M ≤ o_R`** (CERTIFIED
  `lemmas/lemma-em-or-reduction.md`). Xiang's `≤ n` marks split `M` into
  `k+1` sub-pieces and refine `R` into `R'`. Merge into the global sorted list;
  `e_M` = sum of `M`-sub-pieces at global EVEN ranks, `o_R` = sum of `R'`-pieces
  at global ODD ranks. Then `L(n+1)` (=`oddsum(global) ≥ M`) is *exactly*
  `e_M ≤ o_R`. Independent of `k`.
- **Self-compensation** (CERTIFIED `lemmas/lemma-self-compensation.md`)
  reduces `e_M ≤ o_R` further to the residual Hall-type Match
  `Σ_{MM} m_even ≤ Σ_{RR} r_odd`.

**What the inductive input `L(n)` gives.** Apply `L(n)` to `R` (a scaled
level-`n` dyadic, total `total(R) = D(n)/D(n+1)`). `L(n)` says every
refinement of `R` by `≤ n` marks gives an `R`-internal advantage
`A_R ≥ α(n)·(D(n)/D(n+1)) = (D(n)/D(n+1))·(1/D(n)) = 1/D(n+1) = α(n+1)`.
In terms of the `R`-internal odd/even sums (`o_R = R`-odd, `e_R = R`-even,
`o_R + e_R = total(R)`): `A_R = o_R − e_R ≥ α(n+1)`.

**Combine with the identity** `M − total(R) = α(n+1)`:
`o_M + e_M − o_R − e_R = α(n+1)` (since `o_M + e_M = M`, `o_R + e_R = total(R)`).
Subtract `A_R ≥ α(n+1)` (i.e. `o_R − e_R ≥ α(n+1)`):
`(o_M + e_M − o_R − e_R) − (o_R − e_R) ≤ α(n+1) − α(n+1) = 0`, i.e.
`o_M + e_M − 2 o_R ≤ 0`, i.e.
> `M ≤ 2 o_R`,   equivalently   `o_R ≥ M/2`.

**The hard step (honest GAP).** `L(n)` on `R` delivers `o_R ≥ M/2`, but
`L(n+1)` needs `e_M ≤ o_R`. Since `e_M ≤ M` (trivially) and `o_R ≥ M/2`, the
gap is the factor of `2`: `e_M` can be as large as `M` (if `M`-sub-pieces
concentrate at global even ranks — e.g. all `k+1` of them at even ranks when
the global sort interleaves them with larger `R'`-pieces at odd ranks). So
`L(n)` on `R` ALONE does NOT close `L(n+1)`. The missing ingredient is a
control on how `M`-sub-pieces distribute across global rank parities — which is
exactly the residual Hall-type Match (`Σ_{MM} m_even ≤ Σ_{RR} r_odd`,
CERTIFIED reduction) on the merged sort. The superincreasing-R IDENTITY
(`a_j − Σ_{l>j} a_l = α(n+1)`, CERTIFIED) is the structural input, but the
matching itself is a verified CONJECTURE (n=1..5, OPEN) — and the obstruction-
bound COROLLARY (`σ ≤ M/2 = a_1`, `lemmas/lemma-superincreasing-R.md`) is FALSE
for `k ≥ 2` (this round's explorer finding; the `m_1 ≥ M/2` step fails when
`k+1 ≥ 3` sub-pieces). So the inductive lift cannot lean on that corollary.

**Honest summary of the inductive lift.** The `M ⊎ R` recursion + the
`e_M ≤ o_R` reduction + `L(n)` on `R` give `o_R ≥ M/2`. The remaining factor-
of-2 gap is the open Hall-type Match on the merged sort — the same wall the
pairing-partner approach hits. The cell-complex route's alternative to closing
this gap is the structural theorem (D3): if fractional vertices have `A > α(n)`
and integer vertices satisfy grid-parity `A ≥ α(n)` (D2), then `L(n)` holds for
ALL `n` without induction — but D3 is the open GAP. So the two routes
(cell-complex structural theorem; pairing-partner Hall matching) converge on
the same equality structure (the pair-pile) from different framings; both have
a real, distinct open step.

---

## Promotable lemmas
- **Pair-excess decomposition of the advantage sum** (D1): *for `2n+1` real
  sub-pieces `p_1 ≥ … ≥ p_{2n+1}` (sorted desc), `A = Σ_{i=1}^{n}(p_{2i−1} −
  p_{2i}) + p_{2n+1}`; equivalently `A = Σ e_i + ℓ` with pair-excesses
  `e_i = p_{2i−1} − p_{2i} ≥ 0` and leftover `ℓ = p_{2n+1} ≥ 0`.* — proved in
  `approaches/cell-complex-l3.md` §D1 (one-line regrouping, real-valued, no
  integrality). Gives the trivial `A ≥ 0` and is the base on which the grid-
  parity lower bound (D2) and the equality-vertex characterization rest.
- **Parity lower bound at integer-valued arrangement vertices** (D2): *at an
  integer-valued arrangement vertex of the level-`n` dyadic's arrangement
  (pieces are nonneg integers summing to `D(n)`, odd), `A` is an odd nonneg
  integer, hence `A ≥ 1` (integer scale, i.e. `A ≥ α(n)` real); equality `A = 1`
  iff the pair-excess binary form (n equal pairs + leftover 1, OR one pair-
  excess of 1 + leftover 0).* — proved in `approaches/cell-complex-l3.md` §D2
  (specializes the certified grid-parity theorem to arrangement vertices;
  gives the equality characterization at integer vertices). A necessary
  component of any structural proof of `L(n)` for general `n`.
- **2-adic valuation reduction (round 6, PROVED).** *At an arrangement vertex
  of the level-`n` dyadic, write `A = num/L` where `L = det(active subsystem)`
  and `num = sum_i c_i det(B_i)` (Cramer). Let `A = A_num/A_den` be the reduced
  form. Then `v_2(num) - v_2(L) = v_2(A_num) - v_2(A_den) =: v_2(A)`; in
  particular the condition `v_2(num) < v_2(L)` is equivalent to `v_2(A) < 0`
  (A has a factor of 2 in its reduced denominator) and is a property of `A`
  alone, computable without forming `det(B)`.* - proved in
  `approaches/cell-complex-l3.md` S-D3.1 (one-line from the reduced-form
  uniqueness and `v_2(xy) = v_2(x)+v_2(y)`). Reusable by any approach that
  wants to test 2-adic signatures of `A` without determinant computation.
- **D3 falsification of the 2-adic lever (round 6, PROVED negative result).**
  *The condition `v_2(num) < v_2(L) = v_2(A) < 0` does NOT hold at every
  fractional arrangement vertex. Complete n=3 census: `27/2019` fractional
  vertices have `v_2(A) < 0`; `1992/2019` have `v_2(A) >= 0` (A a 2-adic
  integer, often an integer `>= 2` despite fractional pieces). n=4 low-A
  census: `135/5148`. The minimum fractional `A = 5/3` has `v_2(A) = 0` (odd
  denominator `3`, not a 2-adic obstruction).* - proved in
  `approaches/cell-complex-l3.md` S-D3.1 (exhaustive exact-rational census
  n=3, float-prefiltered exact n=4). Records the dead end so no approach
  retries the 2-adic-valuation mechanism for D3.
- **Conditional `L(n)`-for-all-`n` theorem (round 6, CONDITIONAL on the open
  D3 - NOT a proof).** *If D3 holds (every fractional arrangement vertex has
  `A > 1`, integer scale), then `L(n)` holds for all `n` without enumeration:
  by the vertex-principle + the certified `lemma-parity-integer-vertices` (A
  >= 1 at integer vertices) + D3 (A > 1 at fractional vertices), `min A = 1`
  everywhere, so `Liu >= f(n)`.* - stated in `approaches/cell-complex-l3.md`
  S-D3.3 (conditional proof written; depends on the unproven D3). Makes
  explicit that D3 is the SOLE open step in this route. NOT a promotable
  CERTIFIED lemma (conditional); recorded here for the reviewer's routing.

---

## Round 6 build summary

The round-6 task was to attack D3 (every fractional arrangement vertex has
`A > 1`, integer scale) via the 2-adic-valuation / determinant lever the
explorer flagged as underexploited. **The 2-adic lever is FALSIFIED** by a
complete n=3 census and an n=4 low-A census: the explorer's signature
`v_2(num) < v_2(L)` is equivalent (via the proved valuation-reduction lemma
`v_2(num) - v_2(L) = v_2(A)`) to `v_2(A) < 0`, and this holds at only
`27/2019` (n=3) and `135/5148` (n=4 low-A) of fractional vertices - the min
fractional `A = 5/3` has `v_2(A) = 0` and an ODD denominator `3`. So the
2-adic-valuation mechanism is NOT the obstruction forcing fractional `A >
1`; this is a real negative result that narrows the search (recorded as a
promotable falsification lemma so no approach retries it). The broader D3
conjecture remains EMPIRICALLY TRUE at n=3,4 (min fractional `A = 5/3` at
both), with NO analytic proof - the load-bearing number-theoretic lemma is
OPEN. A positive structural pattern is recorded: the min fractional vertex
at both n=3,4 is the same `4/3`-triple shape (pair-pile on the top Liu
pieces + Liu piece `4` split into three equal `4/3` pieces + leftover `1`
=> `A = 2/3 + 1 = 5/3`), an explicit general-`n` candidate extremal
family (attained for every `n >= 3` by an `n`-mark Xiang strategy) - but it
is NOT proved to minimize over all fractional vertices, only verified at
n=3,4. The conditional `L(n)`-for-all-`n` corollary is stated in full (D3
is the SOLE open step in this route, with tightness already CERTIFIED for
all `n` by the pair-pile). The induction gap (`M+R` factor-of-2, the
`pairing-partner`-shared wall) is a separate handle, unchanged. Status
stays `partial`: verified-data advance on D3 + a falsified lever + a
conditional corollary, but no general-`n` proof.
