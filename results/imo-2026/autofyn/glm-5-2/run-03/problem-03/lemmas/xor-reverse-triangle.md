# Lemma: XOR-measure reverse triangle inequality

## Status
PROVED (round 6, by `parity-xor-reachability` §4). Certified by proof-reviewer round 6 as a standalone reusable tool. (Note: the G1 F_2-form induction that USES this tool in `parity-xor-reachability` is NOT certified — it has a fatal toggle-decomposition gap; see the round-6 review.)

## Statement

> For `{0,1}`-valued indicator functions `g, q` on a common measure domain,
> `|g ⊕ q| = |g| + |q| − 2|g ∩ q| ≥ ||g| − |q||,`
> where `|g| = ∫ g` (the measure of `g`'s support), `|g ∩ q| = ∫ g · q` (the overlap measure), and `g ⊕ q` is the pointwise XOR (indicator of the symmetric difference of supports).

Equivalently (set-theoretic form): `|A Δ B| ≥ ||A| − |B||` for measurable sets `A, B`.

## Proof

**XOR-integral identity.** For `a, b ∈ {0,1}`, `a ⊕ b = a + b − 2ab` (pointwise: `0⊕0=0, 0⊕1=1, 1⊕0=1, 1⊕1=0`). Integrating:
> `|g ⊕ q| = ∫ (g + q − 2g·q) = |g| + |q| − 2|g ∩ q|`.

**Reverse triangle inequality.** The overlap `|g ∩ q| ≤ min(|g|, |q|)` (the overlap cannot exceed either side). Substituting:
- If `|g| ≥ |q|`: `|g ⊕ q| = |g| + |q| − 2|g ∩ q| ≥ |g| + |q| − 2|q| = |g| − |q|`.
- If `|g| < |q|`: symmetric, `≥ |q| − |g|`.

So `|g ⊕ q| ≥ ||g| − |q||`. ∎ (KB: *Triangle inequality* — the XOR/`L^1` form for `{0,1}`-indicators.)

Equality holds iff `|g ∩ q| ∈ {0, min(|g|, |q|)}` (full overlap or no overlap of the smaller set within the larger).

## Verification

Algebraic identity (no numerics needed). Independently confirmed by proof-reviewer round 6.

## Import notes

- A universal XOR-measure lower bound — applies to ANY pair of indicator functions, regardless of overlap structure.
- Used (correctly, as a standalone tool) in `parity-xor-reachability` §4. Note: the surrounding G1 induction that invokes this tool has a fatal gap (the toggle decomposition `h = h_{2^n} ⊕ h_rest` is invalid when Xiang re-splits a large fragment of `2^n`); the tool itself is sound.
- Reusable by any approach needing a measure-level lower bound on a symmetric-difference residual.
