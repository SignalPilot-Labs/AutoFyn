## imo-2026-02

Population is empty (round 1). No `register_approach` tool is exposed to me
(only `sample_approaches`); per the ranker's own docstring, `register_approach`
is the outline-reviewer's gate tool, not the outliner's — I have written all
five approach files to `results/imo-2026-02/approaches/<slug>.md` per the file
contract, but the outline-reviewer must call `register_approach` for each new
slug this round to seed them into `.ranking.json` before `sample_approaches`
will return them.

All three explorers independently and numerically confirmed (to ~1e-14): (a)
the three angle conditions leave a genuine 1-parameter family of valid (K,L)
for fixed ABC, not a unique point; (b) OM=ON holds along the ENTIRE family,
which in coordinates B=(-1,0), C=(1,0), A=(p,q) is exactly the scalar identity
O_x = p/2 (O lies on the fixed line = perpendicular bisector of MN); (c) this
breaks only when a solver returns a wrong-orientation branch violating the
containment hypotheses — so any proof must track orientation, not just solve
the angle equalities as bare equations. Confirmed dead ends (do not retry):
spiral similarity BMK~CNL directly; M,K,N,L concyclic; O being any fixed named
center of ABC (circumcenter/orthocenter/nine-point center) — O genuinely moves
along the family, only its membership on the fixed perpendicular bisector of
MN is invariant.

nine-point-link: new
Target: OM=ON, proved by linking circle(AKL) to the nine-point circle of ABC
(which already passes through M, N, forcing its own center equidistant from
M,N) via a fixed transformation (inversion at A or a two-step spiral
similarity), so O is shown to share the nine-point center's line ℓ =
perp-bisector(MN) without needing O = nine-point center (already refuted).
Technique: classical circle-transformation toolkit (inversion, spiral
similarity, radical axis) — knowledge_base.md "Synthetic toolkit."
Skeleton:
  1. Cite the nine-point circle theorem: M, N, midpoint(BC) concyclic, center
     N₉ trivially equidistant from M, N — via the medial-triangle homothety
     (ratio −1/2 at centroid G) taking circle(ABC) to the nine-point circle.
  2. State the reduced goal precisely: show O and N₉ lie on the same line ℓ
     (not that O=N₉, which is refuted).
  3. Search for a transformation (inversion at A with a matched power, or two
     local spiral similarities) carrying circle(AKL) data to the nine-point
     circle's line ℓ; note a single inversion at A with power AM·AB does NOT
     also fix N via AN·AC unless AB=AC — must find the right auxiliary map or
     abandon inversion for a different mechanism.
  4. Fall back: certify the nine-point-circle-through-M,N fact as a standalone
     lemma for the shared cache even if the transformation link stalls.
Key lemmas: nine-point circle passes through M,N (standard, via medial
triangle homothety) — because the medial triangle MNP ~ ABC (ratio 1/2, same
orientation) has the nine-point circle as its circumcircle.
Open gaps: the core transformation link (steps 3) is completely open and
speculative — no confirmed mechanism yet, this is the highest-risk approach.
Cases to cover: none identified.
Watch out for: do not assume O=N₉ (refuted); do not resurrect the refuted
BMK~CNL similarity or MKNL concyclicity under a different name.

coordinate-trig-bash: new
Target: OM=ON via full coordinate placement B=(-1,0), C=(1,0), A=(p,q),
reducing the target to O_x=p/2, then symbolically deriving this identity from
an explicit trig parametrization of the 1-parameter family (free parameter
t=∠KBA=∠ACL, unknowns r₁,r₂ = distances of K,L along their fixed rays).
Technique: coordinate + trig bash with sympy elimination (resultants) — the
committed "sledgehammer" given the terrain strongly supports a clean algebraic
identity.
Skeleton:
  1. Coordinates + linearize the target: OM²−ON² = 2·O_x·1 + (|M|²−|N|²) since
     N−M=(1,0); show target ⟺ O_x=p/2 exactly.
  2. Parametrize K=B+r₁·û(t), L=C+r₂·v(t) with û,v built by rotating dir(B→A),
     dir(C→A) by angle t toward the interior (bakes in ∠KBA=∠ACL=t
     automatically).
  3. Impose ∠LBK=∠LNC and ∠LCK=∠BMK as two trig equations in (r₁,r₂) for
     fixed t via the tan(angle-between-rays)=cross/dot formula; eliminate
     r₁,r₂ (resultants) or solve r₁(t), r₂(t) explicitly.
  4. Substitute into the circumcenter-of-AKL formula (Cramer's rule on the two
     perpendicular-bisector linear equations) and simplify O_x to p/2 via
     sympy.
  5. Track the orientation/branch explicitly against the containment
     hypotheses (K∈int BMC, L∈int BNC, etc.) — the coordinate explorer found
     wrong branches give OM≠ON, so branch selection is not optional.
Key lemmas: OM=ON⟺O_x=p/2 (perp-bisector-of-MN is x=p/2, linear condition);
circumcenter of AKL is a rational function of A,K,L via two linear
perpendicular-bisector equations; r₁(t),r₂(t) are algebraic (resultant-
eliminable) since the angle equations are polynomial after clearing tan
denominators.
Open gaps: closed-form (or resultant-based) elimination of r₁,r₂; the final
symbolic simplification to p/2; rigorous branch tracking.
Cases to cover: none (single continuous family) but must cover the whole
non-degenerate (p,q) space, not just tested numeric samples.
Watch out for: rotation-direction sign errors for K vs L; extraneous
resultant roots; computational intractability (fallback: isosceles AB=AC
special case for partial credit).

labeling-duality: new
Target: OM=ON proved synthetically via the σ: B↔C, K↔L, M↔N relabeling
symmetry of the hypothesis system (∠KBA=∠ACL rewritten as ∠KBM=∠LCN is
self-dual; ∠LBK=∠LNC and ∠LCK=∠BMK swap under σ), without full coordinates —
genuinely distinct framing from coordinate-trig-bash (no explicit
parametrization of the family at all).
Technique: symmetric-function/duality argument + the linear
perpendicular-bisector expansion of O(A,K,L).
Skeleton:
  1. Verify the σ-invariance of the rewritten hypothesis system explicitly,
     and check the containment hypotheses are σ-compatible too (not assumed).
  2. Solve the 2×2 linear system 2O·(K−A)=|K|²−|A|², 2O·(L−A)=|L|²−|A|² for
     O(A,K,L) via Cramer's rule; substitute into OM²−ON²=2·O·(N−M)+|M|²−|N|².
  3. Split the resulting scalar Φ(A,B,C,K,L) into a "near-B" part and its
     σ-dual "near-C" part using law-of-sines expressions for BK, CL, etc. in
     terms of the shared parameter t and ABC's own angles β,γ; look for
     forced cancellation.
  4. Identify how conditions 2 and 3 (which cross the midpoints, and are
     exactly the σ-swap pair) supply the linear relations that cancel the
     antisymmetric residual — this is the central, currently-unproven
     mechanism.
Key lemmas: hypothesis system is σ-invariant (mechanical rewrite check); O is
an explicit Cramer's-rule function of A,K,L (linear algebra fact).
Open gaps: the identification of the σ-dual cancelling quantity (step 3-4) is
wide open — the crux gap.
Cases to cover: none identified; if the duality mechanism does not close,
falls back to the σ-invariance observation as standalone partial credit.
Watch out for: BMK and CNL are NOT similar/congruent (refuted numerically) —
σ is a symmetry of the equations only, never assume it forces a metric
equality of lengths directly.

two-step-spiral-chain: new
Target: OM=ON via two LOCAL spiral similarities/Miquel-type concyclicities
(motivated by conditions 2,3 which "cross" the midpoints: ∠LBK=∠LNC pairs B
with N, ∠LCK=∠BMK pairs C with M) — distinct mechanism from the already-
refuted single global spiral similarity BMK~CNL.
Technique: spiral similarity + Miquel-point/concyclicity converse
(knowledge_base.md "Synthetic toolkit").
Skeleton:
  1. FIRST numerically test (not yet done by any explorer) whether triangle
     BKL and triangle NLC are spiral-similar (equal angle at B/N from
     ∠LBK=∠LNC PLUS matching side ratio BK/BL=NL/NC) — this specific pairing
     is untested; must be checked before any synthetic write-up.
  2. Symmetrically test whether C,M,K and a to-be-identified 4th point (L, B,
     or an intersection point) are concyclic, as suggested by ∠LCK=∠BMK.
  3. If either holds, use the resulting fixed similarity/circle to explain why
     K,L's locus keeps O on the fixed line ℓ regardless of the free
     parameter t.
  4. Assemble both local structures, tied together by the shared parameter t.
Key lemmas: (both provisional, pending numeric check) BKL~NLC via spiral
similarity at some center; C,M,K,X concyclic for some X — mechanism is the
standard spiral-similarity/inscribed-angle converse, but the SPECIFIC
instances here are unverified.
Open gaps: everything is gated on the step-1/2 numeric checks, which no
explorer has run; if both fail, mark dead-end quickly.
Cases to cover: none yet.
Watch out for: don't confuse with the already-refuted BMK~CNL or MKNL-
concyclic hypotheses — these are different (untested) pairings; verify
ray/vertex labeling of each angle exactly against the statement.

complex-circle-power: new
Target: OM=ON via placing O at the origin in ℂ (A,K,L on |z|=R) and using
power-of-a-point/secant relations through B and C, rather than explicitly
parametrizing the 1-parameter family (distinct computational strategy from
coordinate-trig-bash, which fixes B,C symmetric about the origin instead).
Technique: complex-number + power-of-a-point method.
Skeleton:
  1. Place O at 0, A,K,L on |z|=R with arguments α,κ,λ unknown.
  2. Translate the three angle hypotheses into arg-of-quotient equations
     relating B,C to A,K,L.
  3. Compute target |M|²−|N|² purely in terms of A,B,C (M=(A+B)/2 etc.);
     show it reduces to 2Re(A(B̄−C̄))=|C|²−|B|² in this frame; reconcile
     explicitly against coordinate-trig-bash's O_x=p/2 condition (different
     coordinate frames — this reconciliation is a mandatory first sanity
     check, flagged as a real risk of frame confusion).
  4. Use power of B, C w.r.t. circle(AKL) via secants (e.g. line BA extended,
     since ∠KBA is a given angle) to derive the needed relation, matching
     B-side and C-side computations via the given angle equalities.
Key lemmas: target reduces to 2Re(A(B̄−C̄))=|C|²−|B|² (direct algebra, linear
in O expansion); power-of-a-point via secant-length products (standard
theorem).
Open gaps: frame-reconciliation sanity check (step 3) must be done first; the
actual secant/power computation (step 4) is undeveloped.
Cases to cover: none yet.
Watch out for: if this converges to literally the same computation as
coordinate-trig-bash, downgrade priority in favor of the more concrete
sympy-checkable approach rather than duplicating effort.

Recommended build set (round 1): coordinate-trig-bash, labeling-duality,
two-step-spiral-chain. Rationale: coordinate-trig-bash is the highest-
confidence route given the terrain (all three explorers converged on the
O_x=p/2 identity numerically) and should be built first/hardest since it is
the most likely to actually close. labeling-duality and two-step-spiral-chain
are genuinely different synthetic framings (far from the coordinate bash and
from each other — one is an algebraic-symmetry argument, the other a rigid-
map/concyclicity search) that diversify the field per the "far apart in
framing" mandate; both have cheap, well-defined first actions (steps 1 and
1-2 respectively) that will quickly reveal whether they're viable or should be
marked dead-end next round. nine-point-link and complex-circle-power are
registered as live population members for breadth but are lower priority for
round-1 builder time (nine-point-link is speculative with no confirmed
mechanism; complex-circle-power risks converging to the same computation as
coordinate-trig-bash) — recommend the outline-reviewer register all five now
but include at most 3-4 in this round's actual build set, prioritizing as
above.

Outline-reviewer action needed: register all five new slugs (coordinate-trig-
bash, labeling-duality, nine-point-link, two-step-spiral-chain,
complex-circle-power) via `register_approach` before `sample_approaches` will
surface them next round.
