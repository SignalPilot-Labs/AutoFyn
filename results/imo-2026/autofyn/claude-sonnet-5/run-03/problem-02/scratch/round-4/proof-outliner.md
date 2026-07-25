# Proof-outliner report — imo-2026-02, round 4

## Context read
`current.md` (Status `partial`; gap 1 genericity fully closed round 3; sole
remaining gap for the whole problem = branch selection, plus the
round-1-flagged unaddressed isosceles case `AB=AC`), all seven
`approaches/*.md`, all lemma certificates, and this round's three
math-explorer reports (`F2lens`, `acutelens`, `ptolemylens`).

## Field of rival approaches this round

### 1. `coordinate-bash-resultant-boundary` — ADVANCE (build)

Status stays `partial`. This is now the strongest live route to closing
gap 2 (branch selection). Round 4's F2-lens explorer closed exactly the
piece this approach's file (§6, "what remains open," item 1) flagged as
missing: **`F2=0 ⟺ β=∠ACB`**, proved by the identical technique already
certified for `F1=0 ⟺ β=∠ABC` (`lemmas/branch-crossing-locus-equals-angle-B.md`)
— tan-injectivity-on-`(0,π)` plus a direct cross/dot computation
`tan β|_{F2=0} = a·cc/(b²+cc²−ab) = tan(∠ACB)`. The explorer additionally
gave **geometric confirmation** (continuation-based numeric root-tracking,
4 triangles including one with `∠C<∠B` — a case none of round 3's numerics
exercised) that `F2=0` is the mirror boundary of `F1=0`: the point where
`L` (extended along ray `CL`) exits triangle `BNC` through side `BC`,
exactly as `F1=0` is where `K` exits `BMC` through `BC`.

**This round's build target — reduce range-connectedness to one clean
geometric claim and prove it.** The explorer showed numerically (4
triangles, continuation-tracked) that the valid β-range is exactly
`(0, min(∠B,∠C))`, i.e. bounded above by whichever of `F1,F2`'s root is
smaller, and — crucially — that it never terminates earlier via some other,
unidentified boundary (the `BM`/`BN` edges of the containment triangles, or
the two extra "inside-the-angle" hypotheses). Task for the builder:

1. Prove synthetically, via the **monotone ray-sweep argument the explorer
   sketched**: as `β` increases from `0`, ray `BK` (direction
   `(-\cos\beta,\sin\beta)`) sweeps monotonically away from ray `BA`
   towards ray `BC`, staying strictly inside angle `ABC` throughout (so `K`
   can only ever leave triangle `BMC` through edge `BC`, never through edge
   `BM`, since `BM` lies along ray `BA` itself and `K` moves away from that
   ray, not back towards it) — hence `K∈\triangle BMC` for exactly
   `β\in(0,\angle ABC)`, matching `F1=0` at the right endpoint exactly.
   Symmetric argument for `L`/`BNC`/`F2=0=∠ACB`.
2. Conclude range-connectedness: the joint valid range is the intersection
   `(0,\angle B)\cap(0,\angle C)=(0,\min(\angle B,\angle C))`, an interval,
   so it trivially cannot cross either `F1=0` or `F2=0` in its *interior*
   (they are its own endpoints) — closing the "no interior branch-crossing"
   half of the IVT argument for whichever of `F1,F2` is the binding
   constraint. (Still must handle: does an interior crossing of `F3` or of
   `∠LBA`/`∠ACK` sub-conditions occur? If time remains, address `F3`
   (`2a\cos^2\beta=b`, flagged by the acute-lens explorer as unclassified)
   — but this is the IVT mechanism's *third* resultant factor, not F1/F2, so
   treat it as a stretch goal, not required to advance Status this round.)
3. Anchor the IVT argument at one endpoint (e.g. `β\to\min(\angle B,\angle
   C)^-$, or a symbolic isosceles/right-triangle special case) to confirm
   which branch (`G2a`/`G3a` vs `G2b`/`G3b`) is correct just inside the
   range — completing gap 6, item 3 from the file's own "what remains
   open" list.

Write up the new `F2=∠ACB` result as a lemma parallel to
`lemmas/branch-crossing-locus-equals-angle-B.md` (e.g.
`lemmas/branch-crossing-locus-equals-angle-C.md`) if the builder confirms
it independently (don't just import the explorer's numbers — the algebraic
identification itself is cheap to re-derive and should be, per the
population's own verification norms).

**Do not** pursue the acute-angle-bound route in this file (it was never
this file's mechanism — no change needed here on that front).

### 2. `coordinate-bash-resultant` — REDIRECT (build, retire one sub-route, absorb the isosceles-lemma task)

The acute-angle-bound sub-route pursued in this file for two rounds is
**REFUTED this round** (acute-lens explorer: explicit non-degenerate
counterexamples, `∠LCK=∠BMK` up to 123.5° with healthy containment
margins, ~9% and ~18% of triangle area — not boundary artifacts). This
sub-route should **not** be pursued further in any form (including the
"same-sign reduction to two clean inequalities" corollary the explorer
derived — it is real and reusable as a lemma but does *not* rescue branch
selection, since the explorer showed both signs genuinely occur). File
should record this as a clean negative result (already precisely diagnosed
by the explorer) and mark this sub-route dormant.

**Redirected task for this round**: write up the free isosceles-case
(`AB=AC`) proof the ptolemy-lens explorer found, as its own certified,
standalone lemma — independent of Ptolemy, Q, or branch selection, and
reusable by every approach in the population (it closes the
round-1-flagged "isosceles edge case unaddressed" gap that
`fixed-point-concyclic`'s Q-based reduction explicitly cannot handle,
since `Q=A` there). Content to formalize (per the explorer's writeup):

- `AB=AC ⟹ ∠B=∠C`, so the two decoupled constraint equations governing
  `ψ` (from `θ,A,C`) and `φ` (from `θ,A,B`) become the *identical* equation
  — needs an explicit existence/uniqueness argument for the root in the
  valid bracket (the explorer flagged this as needed but not yet written
  out by anyone: show the two sides of the governing equation are each
  monotonic on the relevant sub-interval, so the root is unique, hence
  `ψ=φ` exactly, not just "some root equals some root").
- `ψ=φ` and `AB=AC` (`b=c`) force `α=α'` and `AK=AL` (via the closed
  forms `AK=c\sinθ/\sin(θ+α)`, `AL=b\sinθ/\sin(θ+α')` — already
  established machinery, imported from `ptolemy-trig-identity`), i.e. `K,L`
  are reflections of each other across the triangle's axis of symmetry
  (the perpendicular bisector of `BC`, through `A`).
- Hence circle(`A,K,L`) is invariant under this reflection (it swaps
  `K↔L`, fixes `A`), so its center `O` lies on the axis; the same
  reflection swaps `M↔N` (midpoints of `AB,AC`) since it swaps `B↔C`; an
  isometry fixing `O` and swapping `M,N` gives `OM=d(O,M)=d(refl(O),
  refl(M))=d(O,N)=ON` directly.
- State explicitly the one hidden nondegeneracy needed (`A,K,L`
  non-collinear, so circle(AKL) exists) and where it follows from
  (containment of `K,L` in the interiors of `BMC,BNC` respectively, same
  genericity assumption used throughout the population).

This is a **self-contained, Ptolemy-independent, branch-selection-independent**
lemma — certify it as e.g. `lemmas/isosceles-case-symmetry.md` once built,
for reuse by every live approach (all of them currently implicitly assume
`AB≠AC` somewhere, most sharply `fixed-point-concyclic`'s `Q≠A`
requirement and the whole rotation-parametrization/Weierstrass pipeline's
generic-triangle framing).

### 3. `ptolemy-trig-identity` — ADVANCE (build)

Real, independent progress this round from the ptolemy-lens explorer: the
exact (sympy-verified) closed-form reduction
$$\cot\alpha=\cot\theta+2\cot\psi,\qquad \cot\alpha'=\cot\theta+2\cot\varphi$$
collapses the file's remaining gap (`\angle BAK<\angle BAL`, i.e.
`\alpha<\alpha'$ or the reverse depending on the `AB` vs `AC` case split
already established) to a pure comparison of `\psi(\theta)` vs
`\varphi(\theta)$ — the two decoupled roots of (III),(IV) — with `\alpha,
\alpha'$ no longer needing separate tracking. The naive shortcut "`\psi<
\varphi$ always" is **numerically refuted** (sign of `\psi-\varphi` flips
between triangles: confirmed true throughout on one triangle, false
throughout on another) — do not re-attempt that shortcut.

**Build task**: use the exact cot-identity to attack the inequality via the
*specific* asymmetric dependence — `\psi$ solves (III) using `(A,C)$ only,
`\varphi$ solves (IV) using `(A,B)$ only, and the case split already
established is governed by `\mathrm{sign}(AB-AC)$ (equivalently
`\mathrm{sign}(c-b)$). Concretely:
1. Write out (III),(IV) explicitly enough to extract how `\psi,\varphi$
   depend on `b,c$ respectively (holding `A,\theta$ fixed) — likely via an
   implicit-function/monotonicity argument in the defining transcendental
   equation (is `\psi$ a monotonic function of `c$, or of `b/c$, for fixed
   `A,\theta$?).
2. Combine with `\cot\alpha=\cot\theta+2\cot\psi$ (a monotonically
   decreasing function of `\psi$ on the relevant range, since `\cot$ is
   decreasing on `(0,\pi)$) to translate a monotonicity-in-`(b,c)$ fact
   about `\psi,\varphi$ directly into the desired inequality between
   `\alpha,\alpha'$, matching the sign of `c-b`.
3. If the full inequality cannot be closed this round, report exactly
   which monotonicity sub-claim resisted proof (as precisely isolated as
   this file already isolates its other gaps) rather than leaving a vague
   "still open."

Do **not** duplicate the isosceles-case writeup here — that task is
assigned to `coordinate-bash-resultant` this round (see above) as a
standalone, Ptolemy-independent lemma, to avoid two files certifying the
same fact redundantly. If this file's own machinery is needed as an input
(the closed forms `AK,AL$ and the projection identity), the redirected
builder should cite/import it, not re-derive it.

### 4–7. `coordinate-bash`, `fixed-point-concyclic`, `power-of-point-secants`, `spiral-similarity-bootstrap` — hold (no build this round)

No new information this round bears on these directly.
`fixed-point-concyclic`'s Q-based route remains blocked on the same
central elimination as before (now understood to be equivalent to the
already-closed gap 1, per round 3), and its `Q=A` degeneracy at `AB=AC`
will be superseded once `coordinate-bash-resultant`'s standalone isosceles
lemma lands (any approach, including this one, can then cite it rather
than solve the degenerate case itself). `coordinate-bash` and
`power-of-point-secants` remain honestly-reported dead-ends/subsumed
routes, unchanged this round. `spiral-similarity-bootstrap` remains an
unbuilt outline; not prioritized this round given two live, independent,
actively-progressing routes to gap 2 already in the build set (IVT
mechanism and the Ptolemy inequality) — CLAUDE.md's shared-gap-plateau
concern is not currently triggered, since these two routes are genuinely
different framings (algebraic resultant/continuity vs. trigonometric
Ptolemy), not variations of one idea.

## Summary of this round's priorities addressed

- Advancing `coordinate-bash-resultant-boundary`'s IVT mechanism using the
  new `F2=∠ACB` identification, targeting range-connectedness via the
  monotone ray-sweep argument. ✓ (slug 1)
- Retiring the refuted acute-angle-bound sub-route in
  `coordinate-bash-resultant`, redirecting its effort. ✓ (slug 2, redirected)
- Advancing `ptolemy-trig-identity` with the new cot-identity reduction, an
  independent alternate route to a full solve. ✓ (slug 3)
- Writing up the isosceles-case free lemma as a certified standalone lemma
  this round, closing the round-1-flagged gap. ✓ (assigned to slug 2)

build set: coordinate-bash-resultant-boundary, coordinate-bash-resultant, ptolemy-trig-identity
