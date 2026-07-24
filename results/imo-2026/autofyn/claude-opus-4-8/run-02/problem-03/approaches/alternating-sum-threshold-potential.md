# Approach: alternating-sum-threshold-potential

## Status
partial

## Approaches tried
- **(round 3) GAP-U CLOSED COMPLETELY.** Replaced the stuck "telescoped multi-peel /
  middle-regime" plan with a cleaner and fully rigorous route. Key discovery: Xiang Yu's
  cut toolkit reduces to two atomic *visible-multiset* operations — **delete** a piece
  (bisect it; the equal halves are invisible) and **subtract** a pair `a_i ≥ a_j` (replace
  `{a_i,a_j}` by `a_i − a_j`; the created `a_j` pairs with the old `a_j`, invisible). With
  exactly `m−1` such operations XY can collapse `m` pieces to a single visible piece, whose
  value is any *reachable* signed subset combination. Proved (Lemma A, strong induction) that
  the **min signed `{−1,0,1}`-combination `φ(P)` is always reachable**, and (Lemma B,
  pigeonhole on the `2^m` subset sums) that `φ(P) ≤ s/(2^m−1)`. Together with the trivial
  "budget `≥ m` ⇒ bisect all ⇒ `f=0`" case, this proves Invariant (I) `g_b(P) ≤ s/D_b` in
  FULL for every `m ≤ b+1` — no middle-regime gap remains. Hence the **upper bound
  `c(n) ≤ 2^n/D_n` is complete and rigorous.** Numerically re-verified end to end (exact
  inductive strategy reaches `≤ φ ≤ theta`, 0 violations / 5000; `V_full = φ` 0 mismatches;
  `φ/theta ≤ 1`, worst 1.0). The whole *problem* is still `partial` only because it imports
  GAP-L (lower bound) from the sibling `self-similar-recursion`, which is not yet certified.
- (round 1) Threshold/parity-potential reformulation. Fully proved: Lemma 0 (endgame =
  odd-rank sum), the payoff identity `LB = (1+M)/2` with `M = measure{t: c(t) odd}`, the
  matching reformulation `M = min-weight perfect matching`, the exact single-cut action on
  the potential, and the **complete solution of the case n=1 (both bounds)**. The two
  general cruxes (LB: dyadic caps XY's damage at `M ≥ 1/D_n`; UB: XY forces `M ≤ 1/D_n`
  for every LB marking) are reduced to clean matching/measure inequalities but remain
  open. Recorded dead end: XY's greedy "duplicate-the-top" recursion does NOT achieve the
  cap (numerically violates it from n=3 on); the true optimal XY response is subtler.
- (round 2) LP/matching-duality one-shot certificate route.
  **GAP-L via a dual price φ: DEAD END (confirmed collapse).** The LP dual of the
  min-weight *perfect* matching (on the line, with edge weight `|u−v|`, phantom `0` if odd
  count) is exactly the "parity-crossing" bound `cost ≥ ∫ 1[c(t) odd] dt = f` — i.e. the
  dual is *tight and tautological*: it re-derives `f`, giving no leverage on
  `f(refinement) ≥ 1`. Worse, any *fixed* per-length price `φ(ℓ)` is forced `≤ 0` (two
  equal pieces `x,x` can be matched at cost `0`, so dual feasibility demands `2φ(x) ≤ 0`,
  and cuts do create equal pieces), so `Σφ ≤ 0 < 1` — a fixed monovariant dual **cannot
  exist**. The reviewer's flagged risk is realized; GAP-L is not accessible from a one-shot
  dual and is left to the exchange-lemma/cascade route (self-similar-recursion), not this
  approach. **GAP-U via an explicit XY strategy: genuine partial progress** — a clean
  budget-recursion invariant `g_b(P) ≤ s/D_b` (numerically verified true and tight, dyadic
  extremal), fully proved except one precisely-delimited "middle regime" sub-case (details
  and gap below).

## Current best
**GAP-U is fully closed: the upper bound `c(n) ≤ 2^n/D_n` is proved end to end** (round 3).
Mechanism: Xiang Yu's cutting reduces to two visible-multiset operations (DELETE = bisect,
SUBTRACT = generalized top-match), collapsing `m` pieces to one visible piece in `m−1` cuts
whose value is the min reachable signed subset combination `φ(P)`; Lemma A proves `φ(P)` is
reachable, Lemma B (subset-sum pigeonhole) proves `φ(P) ≤ s/(2^m−1)`, and the surplus case
`b ≥ m` gives `f = 0`. This yields Invariant (I) `g_b(P) ≤ s/D_b` for all `m ≤ b+1`, hence
`M* ≤ 1/D_n` and `c(n) ≤ 2^n/D_n`. The overall problem remains `partial` only because the
matching **lower bound `c(n) ≥ 2^n/D_n` (GAP-L)** is owned by the sibling approach
`self-similar-recursion` and not yet certified; once GAP-L lands, `c(n) = 2^n/D_n` is complete.

Answer **`c(n) = 2^n/(2^{n+1}-1)`** (write `D_n = 2^{n+1}-1`). Established with full rigor:
the whole game reduces to the scalar quantity `M = measure{t≥0 : #{pieces > t} is odd}`
via `LB total = (1+M)/2`, so `c(n) = (1+M*)/2` with `M* = max_LB min_XY M`, and the claim
is equivalent to `M* = 1/D_n`. Proven completely for **n=1** (`c(1)=2/3`); LB Case 1 (top
uncut) proved for all `n` via `f ≥ 2a₁ − S = 1`.

Round-3 progress (this approach): **GAP-U (upper bound `c(n) ≤ 2^n/D_n`) is now COMPLETE
and rigorous.** Invariant (I) `g_b(P) ≤ s/D_b` (for `≤ b+1` pieces of sum `s`) is proved for
all `b ≥ m−1` via: (a) the trivial case `b ≥ m` (bisect all `m` pieces ⇒ every value has even
multiplicity ⇒ `f = 0`); (b) the tight case `b = m−1` via the **pigeonhole–realizability**
theorem: XY can force the final `f` down to `φ(P) := min_{ε∈{−1,0,1}^m, ε≠0} |Σ ε_i a_i|`
(Lemma A, reachability by delete/subtract), and `φ(P) ≤ s/(2^m−1) = s/D_{m−1}` by pigeonhole
on the `2^m` subset sums (Lemma B). The former "middle regime (M)" is dissolved — no phase/
amortisation argument is needed. Full proof in the GAP-U section below.

Round-2 progress (this approach):
- **GAP-L via one-shot dual price: ruled out** (negative result). The LP dual of min-weight
  perfect matching is the parity-crossing bound, which equals `f` tautologically; and any
  fixed length-only price is forced `≤ 0` by equal-piece feasibility, so `Σφ ≤ 0 < 1`. No
  monovariant dual certificate exists. GAP-L belongs to the exchange-lemma/cascade route.

## Full proof
Not present — Status is `partial`. The rigorous components below constitute the progress;
the two general bounds are explicitly reduced to labelled gaps.

---

### Notation and the reduction to a scalar

Write `D_n = 2^{n+1}-1`. After all cutting, the stick is a multiset of piece-lengths
`P`, summing to `1`. Sort descending `a_1 ≥ a_2 ≥ … ≥ a_m > 0` (set `a_i = 0` for `i>m`).

Define the **layer count** `c(t) = #{ i : a_i > t }` for `t ≥ 0`, a non-increasing step
function with `c(t)=k` exactly on `t ∈ [a_{k+1}, a_k)`. Define the **potential**
```
        M(P) = measure{ t ≥ 0 : c(t) is odd } = ∫_0^∞ 1[c(t) odd] dt.
```

---

### Lemma 0 (Endgame = odd-rank sum). 
*For any finite multiset `P` of nonnegative reals, in the alternating-claim game (players
alternately take any remaining piece, first mover = Liu Bang, each maximizing his own
total; the pool sums to a constant `S`, so the game is zero-sum), the value to the first
mover is `g(P) := a_1 + a_3 + a_5 + …` (sum of odd-ranked pieces in descending order), and
taking a largest remaining piece is an optimal move.*

**Proof.** Induct on `m = |P|`. Base `m=0`: value `0 = g(∅)`.

*Monotonicity of `g`.* First we record: if one element of a multiset is increased by
`δ ≥ 0` (others fixed), then `g` changes by an amount in `[0, δ]`. Move the chosen element
continuously upward by `s ∈ [0,δ]`. Within any range of `s` where the sorted order (the
ranks of all elements) is constant, the chosen element occupies a fixed rank `r`, and
`g(s) = (sum of odd-rank values)` has derivative `1` if `r` is odd and `0` if `r` is even,
so slope `∈ {0,1}`. The only order changes occur when the (rising) chosen element meets the
element immediately above it; at that instant the two values are equal, so `g` is
continuous there, and across it the two elements merely swap ranks `r-1 ↔ r`, with the
same pair of values landing on ranks `{r-1,r}` (one of which is odd) — hence `g` is
unchanged in value at the crossing. Therefore `g` is continuous, piecewise linear in `s`
with slopes in `{0,1}`, giving `0 ≤ g(δ)-g(0) ≤ δ`. ∎(sublemma)

*Main induction.* Suppose the claim holds for all multisets of size `< m`. If the first
mover takes piece `a_k`, the opponent then moves first on `P∖{a_k}` and, by the induction
hypothesis, collects `g(P∖{a_k})` out of the remaining `S - a_k`; so the first mover's
total is
```
   a_k + (S - a_k) - g(P∖{a_k}) = S - g(P∖{a_k}).
```
Thus the first mover maximizes by **minimizing** `g(P∖{a_k})` over `k`, i.e.
`V(P) = S - min_k g(P∖{a_k})`. Now `P∖{a_k}` is obtained from `P∖{a_1}` by raising its
element `a_k` up to `a_1` (legitimate since `a_1 ≥ a_k`, `δ = a_1-a_k ≥ 0`); by the
sublemma `g(P∖{a_k}) ≥ g(P∖{a_1})`. Hence the minimum is at `k=1` and taking a largest
piece is optimal. Finally `S - g(P∖{a_1}) = S - (a_2+a_4+…) = a_1+a_3+… = g(P)`, since the
descending list of `P∖{a_1}` is `a_2,a_3,…` whose odd positions are the original even
positions. This closes the induction. Ties (`a_1=a_k`) give `δ=0`, so removing either
largest is equally optimal. ∎

*(Verified computationally: exhaustive game-tree DP matched `g` on thousands of random
multisets — outline-reviewer, 0 mismatches.)*

---

### Lemma 1 (Payoff identity: `LB total = (1+M)/2`).
*With the pieces summing to `1`, Liu Bang's guaranteed value equals `g(P) = (1 + M(P))/2`.*

**Proof.** Let `A = A(P) := Σ_i (-1)^{i+1} a_i = (a_1+a_3+…) - (a_2+a_4+…)` be the
alternating sum of the descending list. Since `a_1+a_2+… = 1`,
```
   g(P) = a_1+a_3+… = ((a_1+a_2+…) + A)/2 = (1 + A)/2.
```
It remains to show `A = M(P)`. By the layer-cake representation `a_i = ∫_0^∞ 1[a_i>t] dt`
and `1[a_i>t] = 1[i ≤ c(t)]` (because the descending list has `a_i>t ⇔ i ≤ c(t)`),
```
   A = Σ_i (-1)^{i+1} ∫_0^∞ 1[i ≤ c(t)] dt
     = ∫_0^∞ ( Σ_{i=1}^{c(t)} (-1)^{i+1} ) dt.
```
The inner partial sum `Σ_{i=1}^{c} (-1)^{i+1}` equals `1` if `c` is odd and `0` if `c` is
even. Hence `A = ∫_0^∞ 1[c(t) odd] dt = M(P)`. Therefore `g(P) = (1+M)/2`. ∎

*(Both `g=(1+A)/2` and `A=M` verified to machine precision on thousands of random
multisets.)*

Consequently, with `M* := max_{LB} min_{XY} M(P)` over Liu Bang's `≤n` marks and Xiang
Yu's `≤n` responses,
```
   c(n) = (1 + M*)/2,   and   c(n) = 2^n/D_n  ⇔  M* = 1/D_n,
```
since `2·(2^n/D_n) - 1 = (2^{n+1}-1-... )/D_n = 1/D_n`. So **the whole problem is: prove
`M* = 1/D_n`.** Liu Bang wants `M` large (much odd-parity threshold measure); Xiang Yu
wants it small.

---

### Lemma 2 (Matching reformulation of the potential).
*`M(P) = A(P)` equals the minimum-weight perfect matching of the pieces (adjoin one
`0`-piece if `m` is odd), with edge weight `|p-q|` between pieces `p,q`.*

**Proof.** For an even number of sorted points on a line, the minimum-weight perfect
matching pairs consecutive points, with cost `Σ_k (a_{2k-1}-a_{2k})`; any matching that
"crosses" or "nests" a pair can be uncrossed without increasing cost by the triangle
inequality on the line, so the adjacent pairing is optimal. That optimal cost is exactly
`A = Σ_k (a_{2k-1}-a_{2k})`. For odd `m`, adjoin a phantom `0`; the adjacent pairing leaves
`a_m` matched to `0` at cost `a_m`, giving `A = (a_1-a_2)+…+a_m`. ∎

*(Verified: `A` equals brute-force min-weight matching on random multisets, 0 mismatches.)*

This gives a clean handle on both bounds: `M ≥ 1/D_n` **iff every** perfect matching costs
`≥ 1/D_n` (equivalently the cheapest does); `M ≤ 1/D_n` iff **some** matching costs
`≤ 1/D_n`.

---

### Lemma 3 (Single-cut action on the potential — the engine).
*Cutting one piece of length `p` into two pieces `x` and `p-x` with `0<x≤p/2` flips the
parity of `c(t)` exactly on `[0,x) ∪ [p-x, p)` (total measure `2x = 2·min(x,p-x)`) and
leaves it unchanged elsewhere. In particular a bisection (`x=p/2`) flips parity on all of
`[0,p)`.*

**Proof.** Before the cut, this piece contributes `+1` to `c(t)` for `t ∈ [0,p)`. After,
piece `x` contributes `+1` on `[0,x)` and piece `p-x` contributes `+1` on `[0,p-x)`. The
net change to `c(t)` is: `+1` on `[0,x)` (`2-1`), `0` on `[x,p-x)` (`1-1`), `-1` on
`[p-x,p)` (`0-1`), and `0` outside `[0,p)`. All other pieces are untouched, so `c(t)`'s
parity flips precisely where the net change is odd, i.e. on `[0,x) ∪ [p-x,p)`. ∎

*(Verified numerically: the flip set is exactly `[0,x)∪[p-x,p)`.)*

---

### Complete solution of the case n = 1  (`c(1) = 2/3`)

Liu Bang marks one point, giving pieces `(1-x, x)` with (WLOG) `x ≤ 1/2`, so `1-x ≥ x`.

**Lower bound (`M* ≥ 1/3`).** Liu Bang marks `x = 1/3`, pieces `{2/3, 1/3}`. Xiang Yu's
`≤1`-cut responses:
- *No cut:* `M = 2/3 - 1/3 = 1/3`.
- *Cut the `1/3`-piece into `y, 1/3-y`:* pieces `{2/3, y, 1/3-y}` with `y+(1/3-y)=1/3 < 2/3`,
  so `2/3` is largest; `M = 2/3 - (larger of the two small) + (smaller) = 2/3 - |2y-1/3|`.
  Since `|2y-1/3| ≤ 1/3`, `M ≥ 1/3`.
- *Cut the `2/3`-piece into `y, 2/3-y` (WLOG `y ≤ 1/3`):* pieces `{2/3-y, 1/3, y}`. Here
  `2/3-y ≥ 1/3 ≥ y`, so sorted `(2/3-y, 1/3, y)` and `M = (2/3-y) - 1/3 + y = 1/3` exactly.

Thus every response yields `M ≥ 1/3`, so `min_XY M = 1/3` for this marking, giving
`M* ≥ 1/3`, i.e. `c(1) ≥ 2/3`.

**Upper bound (`M* ≤ 1/3`).** For an arbitrary marking `(1-x,x)`, `x ≤ 1/2`, Xiang Yu:
- If `x ≤ 1/3` (so `1-x ≥ 2x`): **bisect** the big piece: `{(1-x)/2,(1-x)/2, x}`. Since
  `(1-x)/2 ≥ x`, the two equal top pieces cancel and `M = x ≤ 1/3`.
- If `1/3 < x ≤ 1/2`: cut the big piece `1-x` into `x` and `1-2x` (valid: `1-2x ≥ 0`,
  `x ≤ 1-x`). Pieces `{x, x, 1-2x}` with `1-2x ≤ x`, so the two `x`'s are on top and cancel:
  `M = 1-2x ≤ 1/3` (as `x ≥ 1/3`).

Either way `min_XY M ≤ 1/3` for every marking, so `M* ≤ 1/3`, i.e. `c(1) ≤ 2/3`.

**Conclusion:** `M* = 1/3` and `c(1) = (1+1/3)/2 = 2/3`. ✓ (Matches `2^1/D_1 = 2/3`.)

---

### General lower bound — Liu Bang's dyadic construction (GAP-L)

**Construction.** Liu Bang places his `n` marks so the `n+1` pieces are the **dyadic**
lengths `W_n = { 2^j/D_n : j = 0,1,…,n }` (sum `= (2^{n+1}-1)/D_n = 1`). Largest piece
`2^n/D_n`, each piece double the next. Scaling by `D_n`, the target `M(final) ≥ 1/D_n`
becomes `f(final) ≥ 1` for every `≤ n`-cut refinement of the integer set `{1,2,…,2^n}`.

**Round-2 finding (negative): the one-shot dual certificate collapses.** The route assigned
to this approach was to exhibit a dyadic-level dual price `φ` that is (i) feasible
(`φ(u)+φ(v) ≤ |u−v|`), (ii) monovariant-up under cuts, (iii) `Σφ(W_n) = 1`, giving
`cost ≥ Σφ ≥ 1` by weak LP-duality. This route **provably fails**, for two independent
reasons, both now verified:

1. *The dual is tautological.* The LP dual of the min-weight **perfect** matching (nodes =
   pieces, plus a phantom `0` if the count is odd; edge weight `|u−v|`) is exactly the
   *parity-crossing lower bound*: for any level `t`, the number of matched edges straddling
   `t` is `≥ c_P(t) mod 2`, and integrating gives `cost ≥ ∫₀^∞ 1[c_P(t) odd] dt = f(P)` —
   which is an **equality** (Lemma 2). So the strongest dual merely reproduces `f`; it gives
   no handle on the inequality `f(refinement) ≥ 1` beyond "compute `f`."
2. *No fixed monovariant `φ` can exist.* A cut may create two equal pieces `x,x`, and any
   perfect matching may pair them at cost `0`, so dual feasibility forces `2φ(x) ≤ 0`, i.e.
   `φ ≤ 0` at every value that can be duplicated. Then `Σφ ≤ 0 < 1`, so a length-only price
   with `Σφ ≥ 1` uniform over refinements is impossible. A refinement-*dependent* `φ` is just
   re-solving the matching, i.e. re-deriving `f` (see 1).

**Conclusion for GAP-L in this approach.** The matching-duality mechanism does not close
GAP-L; the honest content of GAP-L is the combinatorial inequality `f(≤n-cut refinement of
W_n) ≥ 1`, which is exactly the **exchange-lemma / bisection-cascade** target of the
`self-similar-recursion` approach (`min_{≤k cuts} f(W_m) = f(W_{m-k})`, numerically exact
`n ≤ 4`). GAP-L is therefore left to that route; this approach contributes the *negative*
result that a one-shot dual price cannot supply the certificate — pruning the field's
search. (Case 1, top piece uncut, remains proved here via `f ≥ 2a₁ − S = 1`; see below.)

*Case 1 (top uncut), self-contained proof.* For any sorted multiset with max `a₁` and total
`S`, `f = a₁ − a₂ + a₃ − ⋯`. Grouping `a₂+a₃+⋯ = S−a₁` and using
`a₂+a₃+a₄+⋯ ≥ a₂−a₃+a₄−⋯ = a₁−f` (the dropped terms `2a₃+2a₅+⋯ ≥ 0`), we get
`S − a₁ ≥ a₁ − f`, i.e. **`f ≥ 2a₁ − S`**. If XY never cuts the top piece of `W_n` then
`a₁ = 2^n/D_n` and `S = 1`, so `M = f ≥ 2·2^n/D_n − 1 = 1/D_n`. ∎(Case 1)

---

### General upper bound — Xiang Yu's cap (GAP-U): COMPLETE PROOF (round 3)

We prove Invariant (I) in full, hence `c(n) ≤ 2^n/D_n`. The round-2 "budget-recursion /
middle-regime" analysis (kept below for the record) is superseded by a cleaner route: reduce
Xiang Yu's play to a two-operation *visible-multiset* game, and close it with a
reachability lemma plus a subset-sum pigeonhole. No middle-regime / amortisation argument is
needed; the former gap (M) is dissolved.

Throughout we use the **matched-pair invisibility** primitive **(P1)** (certified,
`lemmas/layer-cake-alt-sum.md`): *removing two equal-valued pieces from a multiset does not
change `f`.* Proof of (P1), for completeness: two equal pieces of value `v` each add `+1` to
the layer count `c(t)` on `[0,v)`, a total of `+2`, so the parity of `c(t)` is unchanged at
every `t`; since `f = ∫₀^∞ 1[c(t) odd] dt` (Lemma 1), `f` is unchanged. ∎

#### The two atomic Xiang-Yu operations (each is ONE cut)

Given a current multiset, call its pieces the **visible** pieces (those not already members
of an equal pair created earlier — an equal pair contributes `0` to `f` by (P1) and is never
touched again). From the visible multiset Xiang Yu can perform, with a single cut:

- **DELETE `a`** (bisect): cut a visible piece `a` into `(a/2, a/2)`. The two halves form an
  equal pair, invisible by (P1). Net effect on the visible multiset: **remove `a`**.
- **SUBTRACT `(a, a′)`** with `a ≥ a′` (any two visible pieces): cut `a` into `(a′, a−a′)`.
  The new `a′` and the existing `a′` form an equal pair, invisible by (P1). Net effect on
  the visible multiset: **remove `a` and `a′`, insert `a − a′`**.

Both are legal single cuts and are **mass-conserving** (the invisible equal pair carries the
removed mass; DELETE hides `a` as `(a/2,a/2)`, SUBTRACT hides `2a′` as `(a′,a′)` and keeps
`a−a′` visible). Each reduces the visible-piece count by exactly `1`. Starting from `m`
visible pieces, after exactly `m−1` such cuts the visible multiset is a **single piece**, and
`f(final) =` that piece's value (all else is invisible pairs, contributing `0`).

#### Reachable single values

Define, for a multiset `P = {a_1,…,a_m}`,
```
        φ(P) := min over ε ∈ {−1,0,+1}^m, ε ≠ 0  of  |Σ_i ε_i a_i|.
```

**Lemma A (reachability).** *Using `m−1` cuts (DELETE / SUBTRACT), Xiang Yu can drive `P` to
a single visible piece of value `≤ φ(P)`. Consequently `g_{m−1}(P) ≤ φ(P)`.*

*Proof.* Strong induction on `m = |P|`.

*Base `m = 1`.* `φ(P) = a_1` (the only nonzero `ε` is `±1`), and `P` is already a single
piece `a_1 ≤ φ(P)`; `0` cuts. ✓

*Step `m ≥ 2`.* Fix a minimiser `ε*` with `|Σ ε*_i a_i| = φ(P)`; replacing `ε*` by `−ε*` if
necessary, assume `v* := Σ_i ε*_i a_i ≥ 0`, so `v* = φ(P)`. Two cases.

- **Some `ε*_j = 0`.** Perform DELETE `a_j` (1 cut), reaching the visible multiset
  `Q = P ∖ {a_j}` (`m−1` pieces). Restricting `ε*` to the coordinates of `Q` gives a nonzero
  sign vector (it is `ε*` with one zero coordinate dropped, and `ε* ≠ 0`) that realizes the
  value `v*` on `Q`; hence `φ(Q) ≤ v*`. By the induction hypothesis Xiang Yu drives `Q` to a
  single piece `≤ φ(Q) ≤ v* = φ(P)` in `m−2` cuts. Total `m−1` cuts. ✓

- **All `ε*_i ∈ {−1,+1}`.** Let `A = {i : ε*_i = +1}`, `B = {i : ε*_i = −1}`. If `B = ∅`
  then `v* = Σ_i a_i = s > s/(2^m−1) ≥ φ(P)` (using Lemma B below, `φ(P) ≤ s/(2^m−1)`), a
  contradiction; so `B ≠ ∅`, and likewise `A ≠ ∅` (else `v* = −s < 0`). Pick any `p ∈ A`,
  `q ∈ B`. Perform SUBTRACT on the pair `(a_p, a_q)` — cutting the larger of the two — which
  removes `a_p, a_q` and inserts `d := |a_p − a_q|`, reaching a visible multiset `Q` with
  `m−1` pieces. Assign the new piece `d` the sign `η := +1` if `a_p ≥ a_q`, else `η := −1`,
  and keep `ε*` on the other coordinates. Then the signed sum over `Q` is
  ```
     η·d + Σ_{i∈A∖p} a_i − Σ_{i∈B∖q} a_i = (a_p − a_q) + Σ_{A∖p} a_i − Σ_{B∖q} a_i
                                          = Σ_{A} a_i − Σ_{B} a_i = v*,
  ```
  because `η·d = η·|a_p − a_q| = a_p − a_q` in both sub-cases. This sign vector on `Q` is
  nonzero (it has `≥ 1` entry, and `A∖p ∪ B∖q ∪ {d}` is nonempty as `m−1 ≥ 1`), so
  `φ(Q) ≤ |v*| = v*`. By the induction hypothesis Xiang Yu drives `Q` to a single piece
  `≤ φ(Q) ≤ v* = φ(P)` in `m−2` cuts. Total `1 + (m−2) = m−1` cuts. ✓

(The appeal to Lemma B inside the `B=∅` sub-case is not circular: Lemma B is proved below
independently of Lemma A. Alternatively, `B=∅` can be excluded directly — a minimiser never
uses all `+1` signs, since flipping the sign of the *smallest* used piece `a_min` changes
`v* = s` to `|s − 2a_min| < s`, strictly smaller, contradicting minimality.) ∎

**Lemma B (subset-sum pigeonhole).** *For any `P = {a_1,…,a_m}` with sum `s`,
`φ(P) ≤ s/(2^m − 1)`.*

*Proof.* Consider the `2^m` subset sums `σ(T) = Σ_{i∈T} a_i`, one for each `T ⊆ {1,…,m}`,
all lying in the interval `[0, s]`. Partition `[0, s]` into `2^m − 1` half-open subintervals
of equal length `s/(2^m − 1)`. By the pigeonhole principle two distinct subsets `T ≠ T′` have
`σ(T), σ(T′)` in the same subinterval, so `|σ(T) − σ(T′)| ≤ s/(2^m − 1)`. Set
`ε_i = 1[i∈T] − 1[i∈T′] ∈ {−1,0,+1}`; then `ε ≠ 0` (as `T ≠ T′`) and
`|Σ_i ε_i a_i| = |σ(T) − σ(T′)| ≤ s/(2^m − 1)`. Hence `φ(P) ≤ s/(2^m − 1)`. ∎

*(All three facts checked to machine precision: the min reachable value equals `φ` over the
full DELETE/SUBTRACT search (0 mismatches / 3000); the exact inductive strategy of Lemma A
reaches `≤ φ` (0 violations / 5000); and `φ·(2^m−1)/s ≤ 1` with equality only on dyadic
inputs (0 violations / 50000).)*

#### Proof of Invariant (I): `g_b(P) ≤ s/D_b` for all `m ≤ b+1`

Recall `D_b = 2^{b+1} − 1`, and `g_b(P) = min over Xiang Yu's ≤ b cuts of f(final)`. Let `P`
have `m` pieces and sum `s`, with `m ≤ b+1`, i.e. `b ≥ m−1`. Two cases.

- **`b ≥ m` (surplus budget).** Xiang Yu DELETEs (bisects) every one of the `m` pieces, using
  `m ≤ b` cuts. In the final multiset each original piece `a_i` contributes two copies of
  `a_i/2`, so every value present has **even multiplicity**; hence `c(t) = #{pieces > t}` is
  even for every `t`, `1[c(t) odd] ≡ 0`, and `f = ∫₀^∞ 1[c(t) odd] dt = 0`. Therefore
  `g_b(P) ≤ 0 = f`, and `0 ≤ s/D_b`. ✓

- **`b = m−1` (tight budget).** By Lemma A, Xiang Yu forces `f(final) ≤ φ(P)` using exactly
  `m−1 = b` cuts, so `g_b(P) ≤ φ(P)`. By Lemma B, `φ(P) ≤ s/(2^m − 1) = s/D_{m−1} = s/D_b`.
  Hence `g_b(P) ≤ s/D_b`. ✓

In both cases `g_b(P) ≤ s/D_b`, proving **Invariant (I)** for every `m ≤ b+1`. ∎

#### GAP-U closed

Take `b = n`, `s = 1`, and any Liu Bang marking `P_0` (`m ≤ n+1 = b+1` pieces of total `1`).
Invariant (I) gives `g_n(P_0) ≤ 1/D_n`, i.e. Xiang Yu forces the potential `M = f ≤ 1/D_n`
against **every** Liu Bang marking. Since `M* = max_{LB} min_{XY} M`, this yields
`M* ≤ 1/D_n`, i.e. `c(n) = (1 + M*)/2 ≤ (1 + 1/D_n)/2 = 2^n/D_n`. **The upper bound
`c(n) ≤ 2^n/D_n` is proved in full.** ∎(GAP-U)

*Note on the extremiser.* Both bounds in Lemma A/B are tight exactly on the dyadic marking
`W_n = {2^j/D_n}`: there `φ(W_n) = 2^0/D_n = 1/D_n` (the pigeonhole subintervals are hit
exactly once each, the closest pair of subset sums differing by the smallest piece `1/D_n`),
matching `s/D_n = 1/D_n`. This is the same configuration that GAP-L shows is extremal for the
lower bound, confirming `c(n) = 2^n/D_n`.

---

### (Superseded, retained for record) Round-2 budget-recursion analysis

Work in the **matching form** (Lemma 2): `f(P)` = min-weight perfect matching cost. For a
multiset `P` (sum `s`) and a cut budget `b`, let
```
      g_b(P)  :=  min over XY's ≤ b cuts of  f(final multiset)
```
be the smallest `f` Xiang Yu can force. GAP-U is exactly: for every Liu Bang marking `P_0`
(`≤ n+1` pieces, sum `1`), `g_n(P_0) ≤ 1/D_n`. We prove this is implied by:

**Invariant (I).** *For every finite multiset `P` with at most `b+1` pieces and sum `s`,*
```
                          g_b(P)  ≤  s / D_b ,        D_b = 2^{b+1} − 1.
```
Taking `b = n`, `s = 1`, `|P_0| ≤ n+1 = b+1` gives GAP-U. Invariant (I) is verified
numerically (heuristic minimiser over bisect/top-match/match-to-any-piece cuts): over
`3·10^5` random `(b ≤ 5, m ≤ b+1)` configurations the ratio `g_b(P)·D_b/s` never exceeded
`1`, approaching `1` on dyadic-shaped inputs — so (I) is **true and tight**, dyadic
`W_b` being the extremiser (`g_b(W_b·λ) = λ = s/D_b` exactly).

**Two atomic XY moves (each: one cut + pair off two equal pieces).** From sorted
`a₁ ≥ a₂ ≥ ⋯ ≥ a_m`:
- **Bisect-top:** cut `a₁ → (a₁/2, a₁/2)`. The two halves are equal; matching them at cost
  `0` and optimally matching the rest gives (Lemma 2, upper bound only)
  `f ≤ f(R)`, where `R = {a₂,…,a_m}`, `sum(R) = s − a₁`, `|R| = m−1`.
- **Top-match:** cut `a₁ → (a₂, a₁−a₂)` (valid since `a₁ ≥ a₂`). Now two pieces equal `a₂`
  (the new one and the original `a₂`); pairing them at cost `0`,
  `f ≤ f(R)`, where `R = {a₁−a₂, a₃,…,a_m}`, `sum(R) = s − 2a₂`, `|R| = m−1`.

In both cases `|R| = m − 1 ≤ b`, and XY has `b−1` cuts left for `R`, so
```
        g_b(P) ≤ g_{b-1}(R)          (★)   [cut once, pair the equal pair, recurse on R].
```
*(Rigor of (★): XY spends `1` cut now to create `x,x`, then plays its remaining `≤ b−1`
cuts entirely inside `R`; in the final matching it pairs `x`–`x` (cost `0`) and matches
`R_final` optimally. Hence final `f ≤ f(R_final)`, and minimising over XY's play on `R`
gives `f ≤ g_{b-1}(R)`. Lemma 2 is used only as an upper bound (exhibit one matching), so
no equality is needed.)*

**Proof of (I) — the parts that close.**

*Base `b = 0`.* Then `|P| ≤ 1`. A single piece of length `s` matches the phantom `0` at cost
`s`; the empty multiset has `f = 0`. Either way `g_0(P) = f(P) ≤ s = s/D_0`. ✓ (equality at
one piece — consistent with dyadic tightness).

*The STOP rule (balanced, already-small case).* Xiang Yu may always decline to cut, giving
`g_b(P) ≤ f(P)`. Hence **if `f(P) ≤ s/D_b`, Invariant (I) holds at `P` with `0` cuts.** In
particular, since `f(P) ≤ a₁` (the alternating sum telescopes to `≤ a₁`), whenever the top
piece satisfies `a₁ ≤ s/D_b` we are done immediately. This is the correct "adaptive STOP":
XY compares the current `f(P)` (which it can compute) against the target `s/D_b` and halts
the moment it is under — never over-cutting. (This is why the fixed "bisect `n` times" and
"iterated top-match" strategies overshoot: they cut past the stopping line.)

*The geometric step (dominant / heavy-top case).* Suppose `f(P) > s/D_b` (so we cannot stop)
and, additionally,
```
                 max(a₁, 2a₂)  ≥  (2^b / D_b) · s .                 (H)
```
Recall `1 − D_{b-1}/D_b = 2^b/D_b`. Pick the move whose removed mass is `≥ (2^b/D_b)s`:
bisect-top removes `a₁`, top-match removes `2a₂`, so (H) guarantees one of them works, and
the resulting `R` has `sum(R) = s − (removed) ≤ s − (2^b/D_b)s = (D_{b-1}/D_b)·s`. By (★)
and the induction hypothesis of (I) at budget `b−1` (legitimate: `|R| = m−1 ≤ b = (b−1)+1`),
```
   g_b(P) ≤ g_{b-1}(R) ≤ sum(R)/D_{b-1} ≤ (D_{b-1}/D_b · s)/D_{b-1} = s/D_b .   ✓
```
So (I) holds at `(P,b)` whenever the STOP rule fires **or** (H) holds.

**The remaining gap (GAP-U-mid): the "middle regime."** The only configurations not yet
covered are those with
```
        f(P) > s/D_b     AND     max(a₁, 2a₂) < (2^b/D_b)·s ,        (M)
```
i.e. the potential `f` is still above target, yet no single equal-pair cut removes the full
geometric fraction `2^b/D_b ≈ 1/2` of the mass in one step. Numerics (`2·10^5` samples)
confirm such configs exist for `b ≥ 3` (e.g. `b=3, m=4`, pieces `≈[0.455,0.217,0.180,0.149]`,
`f≈0.269 > 1/15`, `a₁≈0.455 < 8/15·s`); they are typically *near-balanced* (many comparable
pieces), and there Invariant (I) *still holds* (verified: `g_3 ≈ 0.06 ≤ 1/15·… `, the true
minimiser uses several gentler cuts). What is missing is a proof that in regime (M) XY can
reach `≤ s/D_b` — the obstruction is that the lock-step "one cut ⇒ budget `−1` ⇒ mass `×r_b`"
accounting is *too coarse*: XY has surplus budget (`b ≥ m−1` with room to spare when
`m < b+1`) and must spend a **multi-cut phase** that reduces the mass by the needed factor
while only later cashing in the budget. Making that amortised phase-accounting rigorous
(equivalently: strengthening the IH to track the piece count `m` and a gentler per-cut rate)
is the single open sub-case of GAP-U. **This is the honest remaining gap for this approach.**

*Why this is real progress over round 1.* Round 1 had only "an adaptive rule is needed, not
found." We now have: (a) the exact invariant `g_b(P) ≤ s/D_b` (proved equivalent to GAP-U,
verified tight); (b) a fully rigorous reduction (★) and two complete regimes (STOP and the
geometric step (H)); (c) the gap pinned to the *single* precise sub-case (M) with a
diagnosed cause (coarse lock-step accounting vs. surplus budget). GAP-U is reduced from an
open crux to one delimited amortisation lemma.

*Recorded dead ends (do not retry).* "Iterated top-match / duplicate-the-top" and "bisect the
max `n` times" both overshoot (they violate the STOP line); pure "peel the top `n` times"
also overshoots on near-balanced configs (e.g. `n=3`, `[0.385,0.233,0.230,0.153]` → `f≈0.153
≫ 1/15`) — these are precisely the regime-(M) inputs the naive strategies mishandle.

---

### Answer and verification

**`c(n) = 2^n/(2^{n+1}-1)`.** Verified: `n=1 → 2/3` (fully proved, both bounds above);
`n=2 → 4/7` and `n=3 → 8/15` (exact maximin / fine grid search, dyadic construction tight,
per the outline-reviewer and explorer reports). The reduction `c(n) = (1+M*)/2 ⇔
M* = 1/D_n`, Lemmas 0–5, the `n=1` case, and GAP-L Case 1 (`f ≥ 2a₁−S`) are established
with full rigor. **Round 3: GAP-U is fully proved** — Invariant (I) `g_b(P) ≤ s/D_b` holds
for all `m ≤ b+1` (Lemma A reachability + Lemma B pigeonhole + the `b≥m` bisect-all case),
giving `M* ≤ 1/D_n` and the upper bound `c(n) ≤ 2^n/D_n`. Substitution check of the answer:
`2·(2^n/D_n) − 1 = (2^{n+1} − D_n)/D_n = (2^{n+1} − (2^{n+1}−1))/D_n = 1/D_n = M*`, consistent
with `c(n) = (1+M*)/2`. The only remaining component of the full problem is GAP-L (lower
bound), owned by `self-similar-recursion`.

## Promotable lemmas
- **Lemma 0 (Endgame greedy).** In the alternating-claim game on a fixed multiset (first
  mover = Liu Bang), the first mover's value is the sum of odd-ranked pieces (descending),
  and taking a largest piece is optimal. Proved in full above (induction + `g`-monotonicity
  sublemma). Suggested cache: `lemmas/endgame-greedy.md`.
- **Lemma 1 (Payoff identity).** With pieces summing to `1`, Liu Bang's value is
  `(1+M)/2`, where `M = measure{t : #{pieces>t} odd}` (`= A`, the alternating sum). Proved
  in full (layer-cake). 
- **Lemma 2 (Matching form).** `M(P)` equals the minimum-weight perfect matching of the
  pieces (adjoin a `0` if odd count), edge weight `|p-q|`. Proved in full.
- **Lemma 3 (Single-cut action).** Cutting a length-`p` piece at offset `x ≤ p/2` flips the
  parity of `c(t)` exactly on `[0,x)∪[p-x,p)`; a bisection flips it on `[0,p)`. Proved in
  full.
- **Lemma 4 (Cut-and-pair reduction — NEW, round 2, fully proved).** Let `P` have sum `s`
  and max `a₁`, `2nd` `a₂`. Xiang Yu can, with one cut, reach a state where the min-weight
  matching cost obeys `f ≤ f(R)` for `R = {a₂,…,a_m}` (bisect-top, `sum(R)=s−a₁`) or
  `R = {a₁−a₂,a₃,…,a_m}` (top-match, `sum(R)=s−2a₂`); in either case `|R| = m−1`. Hence
  `g_b(P) ≤ g_{b-1}(R)` where `g_b` is the min forced `f` under `≤ b` cuts. Proof: exhibit
  the matching pairing the two created equal pieces at cost `0` and matching `R` optimally
  (Lemma 2, upper-bound direction). Suggested cache: `lemmas/cut-and-pair-reduction.md`.
  Reusable by any approach needing an XY upper-bound recursion.
- **Lemma 5 (`f ≥ 2a₁ − S`, all multisets — round 2, fully proved).** For any finite
  multiset with max `a₁` and total `S`, the alternating sum satisfies `f ≥ 2a₁ − S` (proof:
  `S−a₁ = a₂+a₃+⋯ ≥ a₂−a₃+a₄−⋯ = a₁−f`). Gives GAP-L Case 1 (`a₁=2^n/D_n`, `S=1` ⇒
  `f ≥ 1/D_n`) in one line. Suggested cache: `lemmas/alt-sum-two-max-minus-total.md`.
- **Lemma A (XY delete/subtract reachability — NEW, round 3, fully proved).** From `m`
  pieces, Xiang Yu can, in `m−1` single cuts, reach a single visible piece of value
  `≤ φ(P) := min_{ε∈{−1,0,1}^m∖0} |Σ ε_i a_i|`, where each cut is DELETE `a` (bisect, halves
  invisible) or SUBTRACT `(a,a′)` with `a≥a′` (cut `a` into `(a′,a−a′)`, pair the `a′`s
  invisible; visible loses `a,a′`, gains `a−a′`). Proof: strong induction, deleting a zero
  coordinate or subtracting an `A`-piece against a `B`-piece of the minimiser `ε*`. Uses only
  (P1) matched-pair invisibility. Hence `g_{m−1}(P) ≤ φ(P)`. Suggested cache:
  `lemmas/delete-subtract-reachability.md`. Reusable for any XY / second-player min-alternating
  -sum upper bound.
- **Lemma B (subset-sum pigeonhole floor — NEW, round 3, fully proved).** For any multiset of
  `m` reals with sum `s`, `φ(P) := min_{ε∈{−1,0,1}^m∖0}|Σ ε_i a_i| ≤ s/(2^m−1)`. Proof:
  `2^m` subset sums in `[0,s]`, pigeonhole into `2^m−1` equal subintervals, symmetric
  difference of two collided subsets gives the `{−1,0,1}` witness. Suggested cache:
  `lemmas/subset-sum-pigeonhole.md`.
- **Invariant (I) (GAP-U, NOW FULLY PROVED — round 3).** For every multiset `P` with `m ≤ b+1`
  pieces and sum `s`, `g_b(P) ≤ s/D_b` (`D_b = 2^{b+1}−1`). Proof: `b ≥ m` ⇒ bisect all ⇒
  even multiplicities ⇒ `f=0`; `b = m−1` ⇒ Lemma A + Lemma B give `g_{m−1}(P) ≤ φ(P) ≤
  s/(2^m−1) = s/D_{m−1}`. At `b=n, s=1` this is the whole upper bound `c(n) ≤ 2^n/D_n`.
