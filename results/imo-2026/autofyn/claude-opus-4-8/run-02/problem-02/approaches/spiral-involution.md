# Approach: spiral-involution

## Status
partial

## Approaches tried
- (round 1) Synthetic angle-chase exploiting the hidden involution
  `σ : (B↔C, M↔N, K↔L, A↦A)` under which the whole hypothesis system is invariant,
  intending to upgrade conditions 2,3 to genuine spiral similarities `S_K, S_L` and
  push `O` onto perp-bisector(MN). **Outcome: the σ-invariance (L1) and the
  supplementary relation (L2) are PROVED in full and are correct. The spiral-similarity
  engine (L3 / GAP-1) is REFUTED — see below — so the approach as framed cannot reach
  `OM=ON`. RETHINK of the engine required; L1,L2 survive as promotable lemmas.**

## Current best
Three rigorous, self-contained results (proofs below):

1. **Reduction.** `OM = ON ⟺ O ∈ perp-bisector(MN)` (elementary; also the shared field
   fact). Equivalently `pow_M(⊙AKL) = pow_N(⊙AKL)` since `A ∈ ⊙AKL`.
2. **L1 (σ-invariance), PROVED.** The formal involution `σ:(B↔C, M↔N, K↔L, A↦A)` maps the
   entire hypothesis set (three angle conditions + region constraints) to itself:
   condition 1 is σ-fixed, conditions 2 and 3 are swapped, and the conclusion `OM=ON`
   is σ-fixed. This is an organizing symmetry ("prove one side, relabel for the other"),
   NOT an isometry when `AB≠AC`, so by itself it proves nothing — it must be combined
   with a working engine.
3. **L2 (supplementary relation), PROVED.** `∠LBA + ∠NLC = π`, and its σ-image
   `∠KCA + ∠MKB = π`. (Numerically confirmed = 180.0000° across several triangles and θ.)

The open gap is the engine that turns L1+L2 into `pow_M = pow_N`. The engine this
approach was built on (spiral similarities) is refuted.

## Target
The full problem claim: `OM = ON`.

## GAP-1 — RESOLVED AS FALSE (the spiral engine is dead)

The skeleton read condition 3 (`∠LCK=∠BMK`) as the base-angle equality of a spiral
similarity `S_K` centred at `K` with `L↦B, C↦M`; a genuine such similarity is
equivalent to `△KLC ~ △KBM` (vertex order K↔K, L↔B, C↔M). I tested this on the exact
configuration (correct region branch, all three conditions satisfied to `1e-10`,
`OM−ON≈8e-11`):

| quantity (θ=0.3) | value on △KLC | value on △KBM |
|---|---|---|
| angle at K (∠LKC / ∠BKM) | 0.245 | 2.526 |
| angle at L / B (∠KLC / ∠KBM) | 2.581 | 0.300 |
| angle at C / M (∠KCL / ∠KMB) | 0.315 | 0.315 (= condition 3) |
| side ratio KL/KB vs KC/KM | 2.296 | 4.129 |

Only the one *given* angle matches; the other two angles and the side ratio disagree
grossly. The angle **multisets** are `{0.245, 2.581, 0.315}` vs `{2.526, 0.300, 0.315}` —
not equal, so the triangles are not similar under any correspondence, direct or mirror.
The σ-image spiral `S_L` (`△LKB ~ △LCN`) fails identically. Hence L2 does **not** supply
a second independent angle, and none exists: a genuine spiral similarity is impossible.

A decisive independent check: I searched **all** pairs of triangles on the 7 points
`{A,B,C,M,N,K,L}` for a similarity forced across two different θ. The only forced
similar pairs are the trivial midpoint ones (`△ABC ~ △AMN`, `△ABM ~ △ACN`). There is no
hidden similarity for a spiral engine to exploit. **GAP-1 cannot be closed; the
spiral-similarity framing is a genuine dead end (RETHINK).**

## Full proofs of the surviving results

### Reduction `OM=ON ⟺ O ∈ perp-bisector(MN)`
`OM=ON` is by definition `O` equidistant from `M,N`, i.e. `O` on the perpendicular
bisector of segment `MN`. (Trivial; stated for completeness.) Since `A` lies on `⊙AKL`,
for the midpoints `pow_M(⊙AKL)=OM²−R²` and `pow_N(⊙AKL)=ON²−R²`, so `OM=ON ⟺
pow_M(⊙AKL)=pow_N(⊙AKL)`.

### L1 (σ-invariance), full proof
Work with unsigned angles; every betweenness used below is guaranteed by the region
hypotheses. Define the label swap `σ`: `A↦A, B↔C, M↔N, K↔L`. Note `σ` sends the
midpoint `M` of `AB` to the midpoint `N` of `AC` (consistent with `B↔C`), and fixes the
circumcircle `⊙AKL` (it maps `{A,K,L}` to `{A,L,K}`), hence fixes `O`.

- *Condition 1* `∠KBA=∠ACL`. Apply `σ` to each side by relabelling vertices:
  `∠KBA ↦ ∠LCA = ∠ACL` and `∠ACL ↦ ∠ABK = ∠KBA`. So the equation `∠KBA=∠ACL` maps to
  `∠ACL=∠KBA`, the same equation. **σ-fixed.**
- *Condition 2* `∠LBK=∠LNC`. Relabel: `∠LBK ↦ ∠KCL = ∠LCK` and `∠LNC ↦ ∠KMB = ∠BMK`.
  So condition 2 maps to `∠LCK=∠BMK`, which is **condition 3**.
- *Condition 3* `∠LCK=∠BMK` maps, by the same relabelling (`σ` is an involution), to
  `∠KBL=∠LNC`, i.e. condition 2.
- *Region constraints.* "`K` inside `∠LBA`" ↦ "`L` inside `∠KCA`" = "`L` inside `∠ACK`"
  (a hypothesis); "`K∈△BMC`" ↦ "`L∈△CNB`" = "`L∈△BNC`" (a hypothesis). Symmetrically the
  images of `L`'s constraints are `K`'s constraints.
- *Conclusion.* `OM=ON ↦ ON=OM`, and `O` is σ-fixed, so the conclusion is σ-fixed.

Thus `σ` is a symmetry of the labelled hypothesis-and-conclusion system. It licenses
proving a B-side statement and obtaining its C-side counterpart by relabelling. Because
`σ` is only a relabelling (not an isometry when `AB≠AC`), it does **not** on its own
force `O` onto any line; it is an organizing device only. ∎ (L1)

### L2 (supplementary relation), full proof
Because `K` lies inside `∠LBA`, ray `BK` is between rays `BA` and `BL`, so
`∠LBA = ∠KBA + ∠LBK`. By condition 2, `∠LBK = ∠LNC`; by condition 1, `∠KBA = ∠ACL`.
Hence
`∠LBA = ∠ACL + ∠LNC`.  (∗)
Now `N` is the midpoint of `AC`, so `N` lies on segment `AC` and ray `CN` = ray `CA`;
therefore `∠LCN = ∠LCA = ∠ACL`. In triangle `LNC` the angle sum gives
`∠LNC + ∠LCN + ∠NLC = π`, i.e. `∠LNC + ∠ACL = π − ∠NLC`. Substituting into (∗),
`∠LBA = π − ∠NLC`, that is `∠LBA + ∠NLC = π`.
Applying `σ` (L1) to this proved statement (`B↔C, M↔N, K↔L`) yields the σ-image
`∠KCA + ∠MKB = π`. ∎ (L2)

(Numerical confirmation: `∠LBA+∠NLC = 180.0000°` and `∠KCA+∠MKB = 180.0000°` for
`A∈{(1.3,4),(2,5),(−1,3)}`, `B=(0,0)`, `C∈{(5,0),(7,0),(4,0)}`, `θ∈{0.25,0.3,0.4}`.)

## Open gaps
- **GAP-1 (crux): CLOSED AS FALSE.** No genuine spiral similarity `S_K`/`S_L` exists
  (`△KLC ≁ △KBM`; no forced similarity among the 7 configuration points). The engine of
  this approach is refuted → **RETHINK**. L2 does not, and cannot, supply the missing
  second angle.
- **GAP-2 (was: powers from spirals): moot**, since the spirals do not exist. The target
  `pow_M=pow_N` is real (verified `= −1.7312…` from both secants `AB` and `AC`) but this
  approach provides no synthetic mechanism to reach it.

## What a re-plan should keep vs discard
- **Keep:** L1 (σ-invariance) and L2 (`∠LBA+∠NLC=π`, `∠KCA+∠MKB=π`) — both fully proved,
  both promotable, both likely useful to any correct route.
- **Discard:** the claim that conditions 2,3 are base-angles of spiral similarities at
  `K,L`. No similarity is forced; the one-angle-per-condition data cannot be upgraded.
- **Suggested new engine (for the outliner, NOT proved here):** L2 says
  `∠LBA + ∠NLC = π`. This is a *supplementary* (cyclic-type) relation, not a similarity;
  the correct synthetic engine is more plausibly a directed-angle concyclicity or an
  isogonal/trig-Ceva argument feeding the reduction `pow_M=pow_N`, combined with L1 to
  halve the work — a genuinely different framing from "spiral at K,L."

## Cases to cover
- Scalene main case (all numerics above are scalene). Isosceles `AB=AC` is the
  degenerate σ-becomes-reflection consistency check (not needed once a general engine
  exists).

## Watch out for
- `σ` is a FORMAL relabelling symmetry, NOT an isometry when `AB≠AC`; it does not fix a
  point set setwise as an isometry and cannot by itself place `O` on a line.
- Spiral-similarity-at-A, `AK=AL`, `∠BAK=∠CAL`, `{A,K,L,B,C}` concyclic, `BK` tangent,
  and now ALSO **`△KLC~△KBM` / `△LKB~△LCN`** are all FALSE — do not reintroduce them.

## Promotable lemmas
- **L1 (σ-invariance of the hypotheses).** The relabelling `σ:(A↦A, B↔C, M↔N, K↔L)`
  fixes condition 1 and the region hypotheses, swaps conditions 2 and 3, and fixes the
  conclusion `OM=ON`. Proof above (relabelled angle chase). Use: prove any B-side fact,
  get the C-side by σ.
- **L2 (supplementary relation).** Under the problem hypotheses, `∠LBA + ∠NLC = π` and
  `∠KCA + ∠MKB = π`. Proof above (region betweenness + conditions 1,2 + angle sum in
  `△LNC`, then σ). This is a clean cyclic-type relation any approach can use.
