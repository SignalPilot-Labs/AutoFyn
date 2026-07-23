## Lemma: Apollonius / median-length identity, and reduction of OM=ON to a power-of-a-point identity

**Source approach:** labeling-duality (round 1). Certified by proof-reviewer, round 1.

### Lemma A (Apollonius median-length identity)

For any point `O` and any segment `XY` with midpoint `Z`,
$$OZ^2 = \frac{OX^2+OY^2}{2} - \frac{XY^2}{4}.$$

*Proof.* Place vectors with origin at `O`; write `x = X-O`, `y = Y-O`,
`z = Z-O = (x+y)/2`. By the parallelogram law `|x+y|^2+|x-y|^2 = 2|x|^2+2|y|^2`:
$$2\,OZ^2 + \tfrac12 XY^2 = 2\left|\tfrac{x+y}2\right|^2+\tfrac12|x-y|^2
=\tfrac12|x+y|^2+\tfrac12|x-y|^2 = |x|^2+|y|^2 = OX^2+OY^2.$$
Rearranging gives the claim. ∎ (Verified independently, both symbolically and
numerically to machine precision on random test points, by the proof-reviewer.)

This is a fully general fact about any point O and midpoint Z of any segment
XY — independent of the rest of imo-2026-02, reusable in any geometry problem
involving midpoints and distances to an arbitrary point.

### Reduction lemma (specific to imo-2026-02, but proof is self-contained)

Let `ABC` be a triangle, `M` the midpoint of `AB`, `N` the midpoint of `AC`,
and `O` the circumcenter of a triangle `AKL` (so `OA=OK=OL=:R`). Let `Γ` be
the circumcircle of `AKL` (center `O`, radius `R`), so for any point `X`,
`pow_Γ(X) := OX^2 - R^2`. Then
$$OM = ON \iff \mathrm{pow}_\Gamma(B) - \mathrm{pow}_\Gamma(C) = \frac{AB^2 - AC^2}{2}. \tag{TI}$$

*Proof.* Apply Lemma A twice:
$$OM^2 = \frac{OA^2+OB^2}{2}-\frac{AB^2}{4}, \qquad ON^2 = \frac{OA^2+OC^2}{2}-\frac{AC^2}{4}.$$
Subtracting: `OM^2 - ON^2 = (OB^2-OC^2)/2 + (AC^2-AB^2)/4`. This holds for
ANY point O (not yet using O = circumcenter of AKL). Hence
`OM=ON \iff OM^2=ON^2 \iff OB^2-OC^2 = (AB^2-AC^2)/2`. Now use `OA=R`:
`OB^2-OC^2 = (OB^2-OA^2)-(OC^2-OA^2) = pow_Γ(B) - pow_Γ(C)`, giving (TI). ∎

This converts the entire problem "prove OM=ON" into the strictly sharper,
single scalar target (TI). **(TI) itself is NOT proved** — deriving it from
the three angle hypotheses of imo-2026-02 remains the open gap for the whole
problem; this lemma only establishes the equivalence.

### Verification
- Symbolic derivation re-checked from scratch by the proof-reviewer (round 1):
  confirmed both Lemma A and the OM=ON ⟺ (TI) equivalence via independent
  vector algebra.
- Numerically confirmed: for an arbitrary circumcenter O of an arbitrary
  (non-hypothesis-satisfying) triangle A,K,L, (TI) and OM=ON are seen to
  fail together (both sides mismatch, consistent with the iff, not just
  consistent when both happen to hold) — see reviewer's `verify2.py` check.

### Reuse
Any future approach to imo-2026-02 (coordinate, synthetic, complex-number)
should target (TI) directly instead of OM=ON — it is a strictly simpler,
single scalar target equivalent to the original claim.
