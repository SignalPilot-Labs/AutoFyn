## Lemma (General vertex-sign cross-product identities)

For `A=0` (origin), `B,C ∈ ℝ²` (position vectors), `M=B/2`, `N=C/2` (midpoints
of `AB`, `AC`), and `bxc := B×C` (twice the signed area of triangle `ABC`,
using `u×v := u₁v₂−u₂v₁`), the following hold as **polynomial identities in
the coordinates of `B,C`**, valid for every `B,C ∈ ℝ²` (no case split, no
genericity restriction beyond `B,C≠0` and `B,C` non-collinear with `A`):
$$(A-B)\times(C-B) = -\,bxc,\qquad (A-C)\times(B-C)= +\,bxc,$$
$$(B-N)\times(C-N) = +\tfrac12\,bxc, \qquad (B-M)\times(C-M) = +\tfrac12\,bxc.$$

## Proof
Direct expansion using bilinearity and antisymmetry of `×` (`u×u=0`,
`u×v=−v×u`); e.g. `(A−B)×(C−B) = (−B)×(C−B) = −B×C+B×B = −bxc`, and
symmetrically for the other three. See
`results/imo-2026-02/approaches/fixed-point-concyclic.md` (round 3, Lemma 6)
for the full four-line computation.

## Geometric meaning
For a CCW-oriented triangle `ABC` (`bxc>0`): the sweep ray `BA`→ray `BC`
through the interior of `ABC` (hence of the sub-triangle `BMC`) is
clockwise; the sweep ray `CA`→ray `CB` (hence of `BNC`) is
counterclockwise; the sweep ray `NB`→ray `NC` through the interior of `BNC`
is counterclockwise; the sweep ray `MB`→ray `MC` through the interior of
`BMC` is counterclockwise.

## Independent verification
Independently re-verified by the proof-reviewer (round 3) via direct
`sympy` symbolic expansion in free coordinates `bx,by,cx,cy`: all four
claimed identities reduce to exactly `0` residual. Confirmed general (not
example-only), unlike the round-2 version of this fact for the N/M-vertex
case, which the round-2 reviewer had declined to certify for exactly this
reason.

## Source
`results/imo-2026-02/approaches/fixed-point-concyclic.md` (round 3, Lemma 6,
imported from `math-explorer-signlemma` Part A).

## Status
Certified — general-purpose tool for fixing directed-angle sign conventions
at a vertex or edge-midpoint of a triangle, reusable beyond this problem.
