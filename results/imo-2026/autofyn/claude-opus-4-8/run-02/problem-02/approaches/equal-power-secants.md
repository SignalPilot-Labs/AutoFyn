# Approach: equal-power-secants

## Status
partial

## Approaches tried
- (round 1, new) Power-of-a-point / radical-axis framing. Recast `OM = ON` as
  `pow_M(⊙AKL) = pow_N(⊙AKL)`. **L1 (power reformulation) proved in full and reused
  below.** Attempted the distinctive engine — compute each power along a secant through
  `M`/`N` whose *second* intersection with `⊙AKL` is controlled by the angle
  conditions. **This engine is now refuted as unworkable** (see Current best): the two
  natural realizations both fail.
  - Secant **through A** (line `AB` for `M`, line `AC` for `N`): computable, but it
    collapses *exactly* onto the shared reduction `AO·BC = (AC²−AB²)/4` and uses NONE of
    the three angle hypotheses. So it re-proves the target's *reformulation*, not the
    target; the angle data is still needed to locate `O`, which is precisely the hard
    part. No independent leverage.
  - Secant **through K / L** (line `MK` meeting `⊙AKL` again at `K₂`; line `NL` at `L₂`):
    the outline's crux, GAP-1. Numerically refuted — see below. There is NO clean
    control of `K₂, L₂`.

## Current best

### L1 — Power reformulation (PROVED, rigorous, promotable)
Let `O` be the circumcentre and `R` the circumradius of `⊙AKL`, so `A, K, L` lie on the
circle and `|OA| = R`. For any point `X`, the **power of a point** (knowledge_base.md,
"Synthetic toolkit — power of a point") is `pow_X(⊙AKL) = |OX|² − R²`. Hence
```
pow_M − pow_N = |OM|² − |ON|² .
```
Because `|OM|, |ON| ≥ 0`, we get `OM = ON ⟺ |OM|² = |ON|² ⟺ pow_M = pow_N`. This is an
exact equivalence with no case split; whether `M, N` lie inside or outside the circle
(sign of the power) is absorbed by the `|OX|²−R²` form.

Making it explicit with `A` as origin. Write `\vec{AX}` for position vectors from `A`.
Since `M, N` are midpoints, `\vec{AM} = \tfrac12\vec{AB}`, `\vec{AN} = \tfrac12\vec{AC}`.
Using `|OA| = R`,
```
pow_M = |OM|² − R² = |\vec{AO} − \vec{AM}|² − |\vec{AO}|²
      = −2\,\vec{AO}·\vec{AM} + |\vec{AM}|²
      = −\vec{AO}·\vec{AB} + \tfrac14 AB² ,
```
and symmetrically `pow_N = −\vec{AO}·\vec{AC} + \tfrac14 AC²`. Subtracting,
```
pow_M − pow_N = \vec{AO}·(\vec{AC} − \vec{AB}) + \tfrac14(AB² − AC²)
             = \vec{AO}·\vec{BC} + \tfrac14(AB² − AC²).
```
(Both identities verified symbolically with sympy: `powM`, `powN` match the closed forms
and `pow_M − pow_N ≡ \vec{AO}·\vec{BC} + (AB²−AC²)/4` exactly.) Therefore
```
        OM = ON  ⟺  pow_M = pow_N  ⟺  \vec{AO}·\vec{BC} = \tfrac14(AC² − AB²).            (★)
```
This is precisely the shared, explorer-verified reduction. **(★) is fully established.**

### The distinctive engine (secant through K, L) is REFUTED
Equivalent restatement of `pow_M`: `pow_M = \overline{MK}·\overline{MK₂}` where `K₂` is
the second intersection of line `MK` with `⊙AKL` (`K ∈ ⊙AKL`), likewise
`pow_N = \overline{NL}·\overline{NL₂}`. For this to *advance* the proof, `K₂` (resp.
`L₂`) must be pinned by the angle hypotheses. It cannot be, by direct computation on the
solved 1-parameter family (scalene `A=(1.3,4), B=(0,0), C=(5,0)`, branch satisfying all
containment/angle hypotheses, sampled at `θ = ∠KBA = ∠ACL = 15°,25°,35°`):
- **No spiral similarity carries the second intersection.** The only correspondences the
  hypotheses hand us for free are cond 3 `∠KCL = ∠KMB` and cond 2 `∠LBK = ∠LNC`. Turning
  either into a *genuine* similarity (`△KCL ∼ △KMB`, `△LBK ∼ △LNC`) needs a second angle:
  `∠KLC = ∠KBM (= θ)` and `∠LKB = ∠LCN (= θ)`. Both are **false**: measured
  `∠KLC ≈ 145.7°, 156.1°, 166.8°` (vs `θ`), `∠LKB ≈ 125.1°, 134.7°, 143.9°` (vs `θ`).
- **No invariant concyclicity.** A search over all 4-subsets of `{A,B,C,M,N,K,L}` found
  **no** quadruple concyclic across the family (only the trivial collinear triples
  `A,B,M` and `A,C,N`). In particular `B, C ∉ ⊙AKL` — as already flagged — so the
  outline's step L2 ("`∠LCK` is the inscribed angle at `C`") is invalid, and there is no
  substitute circle putting the reference points on `⊙AKL`.
- **The second intersections are not distinguished points.** Computing `K₂` (2nd meet of
  `MK`) gives `K₂ ≠ A`, `K₂ ∉` line `AC`, and no simple locus; `∠K₂AK` is not `θ`-linked.

**Conclusion.** The power framing yields a correct *reformulation* (★) but no engine
independent of actually locating `O`. Its distinctive move (secant-through-`K/L` control)
has no valid mechanism; the secant-through-`A` move is (★) verbatim. So the remaining work
— proving (★) from the angle hypotheses — is the *same* crux as the metric/trig approach
(pin `AO·BC`). This approach does not, on its own, close the problem.

## Open gaps
- GAP (crux, unresolved): prove `\vec{AO}·\vec{BC} = \tfrac14(AC² − AB²)` from the three
  angle hypotheses. Within this framing there is no power-of-a-point shortcut to it (the
  only computable secant, through `A`, gives exactly this identity and no more). Closing
  it requires locating `O` (equivalently `AK, AL, ∠KAL`) via the angle data — i.e. the
  trig/metric engine. GAP-1 of the original outline (control `K₂, L₂`) is **withdrawn as
  unworkable**, with the numerical evidence above.

## Cases to cover
- Sign of the power (`M, N` inside vs outside `⊙AKL`): handled uniformly by the
  `|OX|²−R²` form in L1 — no case split needed. (Done.)
- Scalene main case / isosceles: (★) is proved for all; the *remaining* identity is open.

## Promotable lemmas
- **L1 (power reformulation).** Statement:
  `OM = ON ⟺ pow_M(⊙AKL) = pow_N(⊙AKL) ⟺ \vec{AO}·\vec{BC} = \tfrac14(AC² − AB²)`,
  where `O` = circumcentre(AKL), `M, N` midpoints of `AB, AC`. Proof: complete above
  (power of a point + vector expansion using `|OA| = R`; sign of power irrelevant;
  identities sympy-checked). Reusable by every approach as the canonical restated target.
