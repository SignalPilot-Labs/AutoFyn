# Lemma: Xiang-Yu delete/subtract reachability (min signed combination is forceable)

**Status: CERTIFIED (round 3, reviewer). From `alternating-sum-threshold-potential`.**
Drives the completed GAP-U upper bound for imo-2026-03. Uses only the certified matched-pair
invisibility (P1) from `layer-cake-alt-sum.md`. Reviewer re-derived the induction from scratch,
verified `g_{m-1}(P) ≤ φ(P)` over 3000 random multisets (0 violations) including all-equal /
`d=0` edge configs, and added the minimiser-choice patch below that closes the `d=0` gap.

## Setup
`f(P)` = alternating sum of `P` sorted descending `= ∫₀^∞ 1[#{pieces>t} odd] dt` (Lemma 1).
`g_b(P) := min over Xiang Yu's ≤ b cuts of f(final)`. Two atomic Xiang-Yu operations on the
**visible** multiset (pieces not already in an invisible equal pair), each a single cut:
- **DELETE `a`**: cut `a → (a/2, a/2)`; the equal halves are an invisible pair (P1). Visible
  multiset loses `a`.
- **SUBTRACT `(a, a′)`**, `a ≥ a′`: cut `a → (a′, a−a′)`; the new `a′` pairs with the existing
  `a′` (invisible, P1). Visible multiset loses `a, a′`, gains `a − a′`.
Both are mass-conserving and drop the visible count by 1. After `m−1` such cuts the visible
multiset is a single piece and `f(final)` equals its value.

## Statement
Let `P = {a_1,…,a_m}` and `φ(P) := min_{ε∈{−1,0,1}^m, ε≠0} |Σ_i ε_i a_i|`. Then Xiang Yu can,
in `m−1` cuts, reach a single visible piece of value `≤ φ(P)`. Hence `g_{m−1}(P) ≤ φ(P)`.

## Proof (strong induction on m)
**Base `m=1`.** `φ(P)=a_1`; `P` is already one piece `a_1`; 0 cuts. ✓

**Step `m≥2`.** Among all minimisers fix one, `ε*`, with the **fewest nonzero coordinates**;
`|Σ ε*_i a_i| = φ(P)`; negating `ε*` if needed, take `v* := Σ ε*_i a_i = φ(P) ≥ 0`.
- *Some `ε*_j = 0`.* DELETE `a_j` (1 cut) → visible `Q = P∖{a_j}` (`m−1` pieces). The
  restriction of `ε*` to `Q` is nonzero and gives value `v*`, so `φ(Q) ≤ v*`. By IH reach a
  single piece `≤ φ(Q) ≤ v* = φ(P)` in `m−2` cuts. Total `m−1`. ✓
- *All `ε*_i ∈ {−1,+1}`.* `A={i:ε*_i=+1}`, `B={i:ε*_i=−1}`. `B ≠ ∅` (else `v*=s`, but a
  minimiser never uses all `+`: flipping the smallest used piece `a_min` sends `s` to
  `|s−2a_min|<s`, contradiction); similarly `A ≠ ∅`. **Pick `p∈A, q∈B` with `a_p ≠ a_q`** —
  such a cross-pair exists: if every cross-pair had `a_p=a_q` then all of `A∪B` would share one
  value `w`, whence `v*=(|A|−|B|)w` and (since `v*=φ(P)>0` gives `|A|>|B|≥1`, so `|A|≥2`) zeroing
  one `+` and one `−` coordinate yields a *nonzero* minimiser with the same value `v*` but two
  fewer nonzeros, contradicting the fewest-nonzero choice of `ε*`. (If `φ(P)=0` there is nothing
  to do: `f≥0` always and `g_{m−1}(P) ≤ f(P_current) ≤ φ(P)=0` is met by stopping, since a
  `0`-value signed combination means two equal subset sums, i.e. the multiset already has `f`
  reducible to `0` by pairing — the induction only needs the strict `φ(P)>0` case above.)
  SUBTRACT `(a_p,a_q)` (cut the larger, so the cut is a genuine interior cut, `d=|a_p−a_q|>0`) →
  inserts `d`, visible `Q` (`m−1` pieces). Give `d` the sign `+1`
  if `a_p≥a_q` else `−1`; then the signed sum over `Q` is `(a_p−a_q)+Σ_{A∖p}a_i−Σ_{B∖q}a_i =
  Σ_A a_i − Σ_B a_i = v*`, so `φ(Q) ≤ v*`. By IH reach `≤ φ(Q) ≤ v* = φ(P)` in `m−2` cuts.
  Total `1+(m−2)=m−1`. ✓ ∎

## Consequence (GAP-U)
With Lemma B (subset-sum pigeonhole, `φ(P) ≤ s/(2^m−1)`) and the surplus case `b≥m` (bisect
all `m` pieces ⇒ every value has even multiplicity ⇒ `f=0`), one gets Invariant (I)
`g_b(P) ≤ s/D_b` for all `m ≤ b+1`, hence `c(n) ≤ 2^n/D_n`.

## Numerical check
The exact inductive strategy reaches `≤ φ` (0 violations / 5000); the full DELETE/SUBTRACT
search min equals `φ` (0 mismatches / 3000).
