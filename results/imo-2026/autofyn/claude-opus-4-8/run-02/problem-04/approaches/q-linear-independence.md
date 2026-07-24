# Approach: q-linear-independence (ℚ-vector-space / genericity framing)

## Status
partial

## Answer (conjectured)
Mulan wins **iff θ = 180°/n, n ≥ 2 integer**. This route proves necessity through **linear
algebra over ℚ** (a dimension/independence obstruction) rather than a single modulus — a
genuinely different mechanism, so it does not share the residue route's wall.

## Framing / spine
Shan-Yu picks the initial triangle to be **ℚ-generic relative to θ**. Then every angle ever
produced lies in the affine set θ·ℤ + ℚ-span of the initial data, and an angle can equal θ (a
"clean" value) only if a ℚ-linear relation among the seeds forces it — which happens for *all*
seeds simultaneously only when 180 ∈ θℤ. Spine: **invariant living in a ℚ-vector space**
(KB "Invariants & monovariants"), the invariant being the ℚ-coordinates of each angle.

## Move algebra
Children of a cut: T1={x,β,180−β−x}, T2={α−x,γ,β+x}. Note every child angle is one of:
an untouched seed angle, the free cut value x, or a **ℤ-combination 180−β−x / β+x** — i.e. an
integer-coefficient affine expression in {x, existing angles, 180}.

## Skeleton
1. **Genericity setup (necessity).** Let θ∤180. Shan-Yu chooses initial angles α₀,β₀ (γ₀=
   180−α₀−β₀) so that {1, θ, α₀, β₀} is **linearly independent over ℚ**, with α₀,β₀ chosen
   inside a valid triangle. — possible since ℚ is countable and the constraint region is open.
2. **Coordinate invariant.** Track each angle by its coordinates in the ℚ-vector space
   V = ℚ⟨1, θ, α₀, β₀⟩ / the running span. Claim: to avoid ever creating an angle = θ,
   Shan-Yu keeps a child whose three angles all have **nonzero θ-defect** — the coefficient
   structure that would be needed for an angle to collapse to exactly θ never materialises. The
   free cut value x that Mulan injects can be chosen by her, but Shan-Yu's discard removes the
   dangerous branch. — by Lemma G.
3. **The obstruction is exactly θ|180.** The *only* ℚ-relation available among the seeds that
   Mulan can exploit universally (independent of Shan-Yu's generic α₀,β₀) is 180 = nθ; when
   θ∤180 no such relation exists, so no universal alignment is possible and Shan-Yu survives.
   — by Lemma H.
4. **Sufficiency θ=180/n.** Here 180=nθ *is* a ℚ-relation among the seeds; Mulan uses it as the
   alignment identity (place complementary multiples 180−β−x=kθ and β+x=(n−k)θ into the two
   children) then peels down — same construction as the other approaches, re-derived from the
   relation 180=nθ. — by the alignment+peel construction.

## Key lemmas (claim + mechanism)
- **Lemma G (generic-survival).** From a ℚ-generic triangle, for every Mulan cut, at least one
  child is again ℚ-generic (no angle equals θ, and independence is preserved). *Mechanism:*
  the two children's compound angles 180−β−x and β+x differ from θ by expressions whose ℚ-
  coordinates cannot both vanish; concretely, "both children contain θ" would force two
  independent affine equations in x that are jointly solvable only if 180−2·(untouched) ∈ θℤ,
  impossible under genericity + θ∤180. (This is the ℚ-independence twin of Lemma A / Lemma D.)
- **Lemma H (uniqueness of the exploitable relation).** Among all ways a single cut can be
  designed to threaten *both* children regardless of the (adversarial, generic) seed angles,
  the required identity reduces to 180 ≡ 0 in the θ-coordinate — i.e. θ|180. *Mechanism:*
  seed-independence kills every relation involving α₀ or β₀, leaving only the 1- and θ-
  coordinates, whose balance is exactly 180 = nθ.
- **Alignment + peel (sufficiency).** Same as residue-invariant Lemmas B, C, but justified by
  the honest ℚ-relation 180 = nθ rather than a residue congruence.

## Open gaps (builder fills)
- **G1:** make Lemma G rigorous — define the invariant precisely (which finite-dim ℚ-space; how
  x enlarges it; why one child stays generic) and prove closure under all cuts and Shan-Yu's
  discard. This is the crux and the riskiest gap of this framing.
- **G2:** reconcile with the θ>90 case — genericity handles *all* θ∤180 uniformly, so confirm
  it does not accidentally also "prove" survival for θ=180/n (it must not; Lemma H is the
  firewall).
- **G3:** sufficiency range-existence pigeonhole (shared with other approaches).

## Cases to cover
- Necessity: every cut from a generic triangle (Lemma G) — uniform over θ∤180, no 90° split.
- Sufficiency: the alignment move's two branches + the peel chain.

## Watch out for
- **Highest-risk approach:** the ℚ-invariant (Lemma G) is elegant but easy to hand-wave. The
  reviewer will demand a precise definition of the tracked coordinates and a real closure
  proof, not "genericity is preserved." If G1 cannot be nailed, this route RETHINKs toward the
  cleaner residue framing — but its independent mechanism is worth an attempt for diversity.
- x is a *new* real each move; the ℚ-span can grow. The invariant must be about the θ- and
  1-coordinates staying balanced, not about a fixed finite basis.

## Approaches tried
- (this file) ℚ-linear-independence / genericity route. Distinct necessity mechanism from the
  residue and extremal approaches.

## Current best
Framework set up; sufficiency shares the alignment+peel construction. Necessity reduced to
Lemmas G, H, with G the open crux.
