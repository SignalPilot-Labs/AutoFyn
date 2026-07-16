# Lemma: Reality hinge for an unsigned-angle equality (directed angles)

**Setup (complex plane).** For distinct `P,U,V ∈ ℂ` define the directed angle from ray `PU`
to ray `PV` as `∠(PU→PV) := arg((V−P)/(U−P)) ∈ (−π,π]` (principal value), and the signed area
`[P,U,V] := ½ Im( conj(U−P)·(V−P) )`. Then:

- **(SGN)** `∠(PU→PV) ∈ (0,π) ⟺ [P,U,V] > 0`.
  (Proof: `arg w ∈ (0,π) ⟺ Im w > 0`; apply with `w=(V−P)/(U−P)`, whose imaginary part has the
  sign of `Im(conj(U−P)(V−P)) = 2[P,U,V]`.)

**Lemma 2 (reality hinge).** Let `θ₁ = arg z₁`, `θ₂ = arg z₂` (principal args, `z₁,z₂ ∈ ℂ^×`)
be two directed angles, both in `(0,π)`, whose corresponding **unsigned** angles are equal.
Then `θ₁ = θ₂` (as real numbers), `arg(z₁/z₂) = θ₁ − θ₂ = 0`, and hence `z₁/z₂ > 0`;
in particular `z₁/z₂ ∈ ℝ`.

**Proof.** Since `θ₁,θ₂ ∈ (0,π)`, each equals its own unsigned value `|θ_i|`; the hypothesis
"unsigned angles equal" therefore gives `θ₁ = θ₂` as real numbers (not merely mod π). Next,
`arg(z₁/z₂) ≡ θ₁ − θ₂ (mod 2π)`. Because `θ₁,θ₂ ∈ (0,π)`, the difference `θ₁ − θ₂ ∈ (−π,π)`,
and the principal value `arg(z₁/z₂) ∈ (−π,π]`; two numbers of `(−π,π]` congruent mod 2π are
equal, so `arg(z₁/z₂) = θ₁ − θ₂ = 0`, i.e. `z₁/z₂ ∈ ℝ_{>0}`. ∎

**Why it matters.** An unsigned Olympiad angle equality only gives `θ₁ ≡ ±θ₂ (mod π)`; the
supplementary/opposite branch is killed exactly by pinning **both** directed angles into `(0,π)`
(so their difference lies in `(−π,π)` and must be 0, not π). The interior/orientation hypotheses
of a configuration supply the two `(0,π)` facts via (SGN). This converts an unsigned angle
equality into an *exact* reality condition `z₁/z₂ ∈ ℝ` on a cross-ratio-type expression.

**Certification (proof-reviewer, round 2).** Every step re-derived independently and checked:
(SGN) sign identity, the `mod 2π ⇒ equal` collapse on `(−π,π]`, and the `z₁/z₂>0` conclusion are
correct. The lemma is stated no stronger than proved. Verified numerically as a sanity check in
`check_s3.py` (all six directed angles land in `(0,π)`, `arg C_i = θ₁−θ₂ = 0`). Certified for
reuse. Certified from approach `complex-reality-conditions` §3.1.
