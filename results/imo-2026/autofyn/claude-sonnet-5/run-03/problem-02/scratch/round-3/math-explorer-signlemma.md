## imo-2026-02 — SYNTHETIC SIGN / BRANCH-SELECTION lens

### Part A: `fixed-point-concyclic`'s (H1)-(H3) vertex-sign gap — CLOSED, full derivation below

The gap flagged by round 2's proof-reviewer (H2/H3's sign at vertices N, M was
only checked "on a representative CCW triangle") is fully closable by a
**one-line cross-product computation per vertex**, all four of which I
verified symbolically (sympy, symbolic `bx,by,cx,cy`, A at origin, b=B, c=C
as vectors). Let `bxc := b×c` (scalar cross product = 2·signed_area(A,B,C);
CCW triangle ⟺ `bxc > 0`). With `M = b/2`, `N = c/2`:

$$\mathrm{cross}(BA,BC) = (A-B)\times(C-B) = -\,bxc$$
$$\mathrm{cross}(CA,CB) = (A-C)\times(B-C) = +\,bxc$$
$$\mathrm{cross}(NB,NC) = (B-N)\times(C-N) = +\tfrac12\,bxc$$
$$\mathrm{cross}(MC,MB) = (C-M)\times(B-M) = -\tfrac12\,bxc \quad\Longleftrightarrow\quad \mathrm{cross}(MB,MC)=+\tfrac12\,bxc$$

(All four verified by direct symbolic expansion — each reduces to `bxc` or
`bxc/2` exactly, no residual terms, no case split, valid for **every**
triangle A,B,C with A,B,C in general position, not just "a representative
one." Derivation: e.g. `cross(NB,NC) = (b-c/2)×(c-c/2) = (b-c/2)×(c/2) =
(1/2)[b×c - (c/2)×c] = (1/2)b×c` since `c×c=0`; the M-vertex fact is
identical with `b,c` swapped and a sign flip since `M=b/2` plays the role
`N=c/2` did but the swap `B↔C` in the formula for `cross` is antisymmetric.)

**Consequence for the approach file.** Given `bxc>0` (CCW):
- `cross(BA,BC)<0`: the sweep ray-BA→ray-BC through the interior of triangle
  ABC at vertex B is **clockwise** — exactly the fact the file uses to fix
  the sign of hypothesis 1's `κ = arg((K-B)/(A-B))`.
- `cross(CA,CB)>0`: the mirror sweep at C is **counterclockwise** — fixes
  `λ`'s sign, matching the file.
- `cross(NB,NC)>0`: the sweep ray-NB→ray-NC through the interior of triangle
  BNC at vertex N is **counterclockwise** — this is *exactly* the fact
  needed for (H2)'s sign (`arg((C-N)/(L-N)) = +ψ`), and it is now proved for
  every CCW triangle, not read off one example.
- `cross(MB,MC)>0`, i.e. sweep ray-MB→ray-MC at vertex M (through the
  interior of triangle BMC's companion, the σ-image) is counterclockwise —
  the analogous fact for (H3), consistent with (and now proving, rather than
  merely cross-checking via σ-symmetry) the file's independent direct
  derivation at C,M.

This is a complete, general, four-line replacement for the file's "direct
computation... on a representative CCW triangle" sentence — it should be
substituted in verbatim; it fully removes the overclaim the round-2 reviewer
flagged, closing that specific gap. (Note: this reproduces, with a full
derivation shown, exactly the fact the round-2 reviewer stated it had
verified independently — that verification is confirmed correct here.)

**This does NOT close the file's actual remaining gap** — the elimination
`(H1)∧(H2)∧(H3) ⟹ χ∈ℝ` is untouched by this; only the *sign conventions* of
(H1)-(H3) (needed to state them correctly) are now fully general. Do not
conflate "sign gap closed" with "central identity proved."

### Part B: `coordinate-bash-resultant`'s branch selection — genuinely different question, but a strong new synthetic lead found

**Key distinction (important, not obvious a priori):** the fixed-point-
concyclic sign gap (Part A) is about the SIGN OF A CROSS PRODUCT (which
determines *rotation direction* / which of two angle-sweep orientations is
correct — i.e. distinguishing `+θ` from `-θ`). The coordinate-bash-resultant
branch-selection gap is a DIFFERENT kind of sign question: hypothesis 2/3 are
stated as equality of *unsigned* angles via `cos`, and the polynomial system
is obtained by squaring `(V1·V2)|V3||V4| = (V3·V4)|V1||V2|` to clear square
roots. Since `|Vi|>0` always, the squaring is ambiguous exactly between
`sign(V1·V2) = sign(V3·V4)` (branch a) vs `sign(V1·V2) = -sign(V3·V4)`
(branch b) — i.e. it hinges on the SIGN OF A DOT PRODUCT (whether the named
angle is acute or obtuse), not a cross product. **The signed-area/cross-
product technique of Part A does not directly resolve this** — it is a
genuinely different algebraic fact and needs its own argument. This is worth
flagging explicitly to the outliner so no one tries to paper over the
distinction.

**New numeric finding (strong, multi-triangle, not yet proven).** I solved
the true (unsquared, arccos-based) hypothesis system via `fsolve`, filtered
by both containment conditions, across **9 distinct triangles** spanning a
wide range of shapes — acute, obtuse at A, obtuse at B, "thin" scalene, and
one near-right triangle — and **20-30 β-values each** (≈150 genuine solution
points total). At *every single* genuine solution point, on *every*
triangle tested:
$$BL\cdot BK > 0,\quad NL\cdot NC>0,\quad CK\cdot CL>0,\quad MB\cdot MK>0,$$
i.e. **all four hypothesis angles ∠LBK, ∠LNC, ∠LCK, ∠BMK are acute** — and
not just barely: the observed maximum value across all 150+ points was
**≈49.4°** (on a deliberately thin/near-degenerate triangle), i.e. there is a
real numerical margin below 90°, not a marginal coincidence. (On the most
"generic" acute/obtuse-mix triangles the angles stayed under ~15°.)

**Why this matters.** If "all four hypothesis angles are always acute" can
be proved synthetically (in general, for every valid triangle and every
valid β in the family), it *immediately* resolves coordinate-bash-
resultant's branch-selection gap without any resultant/Gröbner computation:
the correct branch is simply "both dot products positive," i.e. the `+`
sign in the squaring, which picks out `G2a`/`G3a` over `G2b`/`G3b` by
construction (these polynomials were defined by `sympy`'s factorization of
`(\dagger)` and their vanishing loci correspond to the two sign choices —
this correspondence itself should be double-checked in the write-up, but is
very likely just "does V1·V2 have the same sign as V3·V4," which the acute-
angle fact settles as "yes, always +"). This reframes gap (2) from "prove a
resultant-based non-crossing fact on every triangle" to the cleaner target
"prove ∠LBK, ∠LNC, ∠LCK, ∠BMK are always acute" — a genuinely different,
likely more tractable, and more synthetic-flavored target.

**I did not find a proof of the acute-angle fact.** Candidate levers for
next round to try (not attempted to completion here, flagged as leads only):
- `K` lies inside triangle `BMC` and inside angle `LBA`; since `M` is the
  midpoint of `AB`, `BM = AB/2` is comparatively short, which may force `BK`
  to be short too (`K` interior to a triangle with one very close vertex `B`
  and near side `BM`), and short "reach" from `B` combined with `L` on the
  far side (inside triangle `BNC`, away from `B`) is plausible cause for
  `∠LBK` to stay acute — but this is an intuition, not an argument; a
  rigorous version would need an actual length/position bound.
- Alternatively, try to directly bound `∠LBK` using the two containment
  hypotheses ("K inside angle LBA", "L inside angle ACK") which already
  constrain the relative angular position of K, L, A, B, C at each vertex —
  might combine to a clean upper bound via triangle-angle-sum arguments.
- A cheaper interim step (if a full synthetic acute-angle proof doesn't
  materialize quickly): the observed 150-point margin (max 49.4° vs the 90°
  threshold) is itself decent Schwartz–Zippel-style evidence that could be
  strengthened to near-certainty with a proof that the acute-angle property
  is *stable under the connectedness argument already in the file* (the
  valid parameter range for each triangle is connected, angle is continuous,
  so acute-ness can only fail via passing through exactly 90° — check the
  boundary/degenerate limits of the family, e.g. β→0 or the containment-
  breaking boundary, for whether the angle can approach 90°; a boundary
  analysis might be more tractable than a full mid-range proof).

### Cheap-kill / sanity notes
- The four cross-product sign facts (Part A) are now fully rigorous, closed,
  reusable one-liners — recommend they be inserted verbatim into
  `fixed-point-concyclic.md`'s Step 3 to remove the flagged overclaim.
- Part B's acute-angle conjecture is NOT proven — do not let a builder state
  it as settled. It is strong (9 triangles, ~150 points, real margin) but
  remains a conjecture per CLAUDE.md's "prove, don't conjecture" rule.
- Both parts are consistent with (do not contradict) the branch identified
  numerically by `coordinate-bash-resultant` on its one triangle — this is a
  positive cross-check, not new information (same conclusion, independent
  method).

## Knowledge-base entries used
- Standard signed-area / cross-product orientation facts (elementary vector
  algebra — not a named KB entry, but the technique the round-2 reviewer
  used and I have now written out in full, general form).
- `lemmas/cross-ratio-real-concyclic-criterion.md` (context only, not
  extended here).
- `lemmas/homogeneity-decoupling-rotation-param.md` (context for Part B's
  setup, not modified).

## Analogous past problems (cruxes)
Not queried this round — this lens is a narrow algebraic sub-question
(sign/branch selection within an already-identified reduction), not a fresh
top-level framing of the whole problem, so a crux-corpus search for "IMO
geometry problems with fixed point / circumcenter" would not be targeted
enough to be useful here; the prior rounds' math-explorer reports already
recorded that the crux corpus currently has no geometry-domain entries at
all (see `/tmp/memory/run_state.md` Rules). Skipped per the "don't force a
match" guidance.

## Prior progress
See `results/imo-2026-02/current.md` — Status `partial`. This report only
addresses the two specific sign sub-gaps described above; the central
identity (A,K,L,Q concyclic / O·(C−B)=(|C|²−|B|²)/4) remains the open crux,
untouched by this lens.

## Dead ends (do not retry)
- Do not try to derive Part B's branch selection from the SAME cross-product
  technique as Part A — verified above that they are different sign
  questions (cross-product/rotation-direction vs dot-product/acute-obtuse);
  conflating them would be a wasted round.

## Small-case / intuition notes (conjecture, labeled)
- **Conjecture (strong numeric support, 9 triangles × ~150 total genuine
  solution points, not proven):** at every valid configuration point,
  ∠LBK, ∠LNC, ∠LCK, ∠BMK are all acute (observed max ≈49.4°, well under
  90°). If provable, this cleanly resolves coordinate-bash-resultant's
  branch-selection gap in general.
- **Proven (not conjecture):** the four vertex-sign facts of Part A hold
  for every triangle — verified by exact symbolic (not numeric) computation.
