# Round 3 proof-reviewer report — imo-2026-02

## Headline

Gap 1 (genericity of the central identity `O·(C−B)=(|C|²−|B|²)/4`, for
*every* real triangle, on the correctly-selected branch) is now **fully
closed and independently reproduced from scratch by me**, not just
re-typed from the builders' transcripts. I wrote my own `sympy` script
(different variable-extraction logic, an independent `cancel()`-based fully
reduced target `T` in addition to the builders' `together/numer` version)
starting only from the geometric problem statement (the rotation
parametrization `K=B+t1(-cosβ,sinβ)`, `L=C+s2·R(β)(A−C)`, and the four
hypothesis vectors), and reproduced: `eq2` exactly divisible by `t1²`,
`eq3` by `s2²`; the quotients' degree-4-in-`u` factors `G2a,G3a` match both
approach files' displayed polynomials term-for-term; the Gröbner basis of
`⟨G2a,G3a⟩` (18 generators, grevlex) reduces `T` to remainder 0 — for
**both** representations of `T` I tried (the builders' unreduced numerator,
degree 14/8-in-u, *and* a strictly-reduced coprime numerator via
`sympy.cancel`, degree 10/4-in-u) — and `T` is in neither `⟨G2a⟩` nor
`⟨G3a⟩` alone. This is a robust, doubly-independent confirmation; certified
as `lemmas/symbolic-genericity-certificate.md`.

Branch selection (gap 2) — which of `G2a=G3a=0` vs `G2b=G3b=0` the genuine
geometric solution lies on — remains **open**. This is now the population's
sole shared wall for the whole problem (plus the still-unaddressed
isosceles edge case `AB=AC`).

## Per-approach verdicts

### coordinate-bash-resultant — CHANGES REQUESTED (Status: partial, correct as self-reported)
- **Verified correct**: the fully symbolic genericity certificate (see
  above — independently rebuilt end to end, matches exactly). No
  overclaim: file correctly states Status `partial`, correctly separates
  "gap 1 closed" from "gap 2 open."
- **Verified correct**: the crude-containment-bound-insufficiency argument
  (§9 Attempt 1) is a valid, general proof (not conjecture) — I checked the
  logic (ray BM = ray BA since M is the midpoint; the containment bound
  gives only `0<∠LBK<∠ABC`, not `<90°`) and it holds.
- **Spot-checked and confirmed**: the resultant `Res_{s2}(G2a,G2b)` factors
  exactly as `64u²(u²+1)⁴F1·F2·F3` with `F1=2au−2bu+ccu²−cc`,
  `F2=−2abu+accu²−acc+2b²u+2cc²u`, `F3=2au⁴−4au²+2a−bu⁴−2bu²−b` — I
  independently recomputed this resultant from my own `G2a,G2b` and got an
  identical factorization (used to cross-check the sibling file too).
- **Gap 2 (branch selection) is genuinely not closed.** The acute-angle
  claim is honestly labeled a conjecture, backed only by numerics (150
  points, 9 triangles). No overclaim found anywhere in the file.
- No issues with the writeup this round (round 2's cosmetic L-formula
  transcription error is not repeated).

### coordinate-bash-resultant-boundary — CHANGES REQUESTED (Status: partial, correct as self-reported)
- **Verified correct**: independent re-derivation of the same genericity
  certificate (redundant with the sibling, but a valuable cross-check —
  matches on generator count, timing order, and remainder-0 result).
- **Verified correct, independently, the key new algebraic fact**:
  `F1 = (1+u²)[(a−b)sinβ − cc·cosβ]` — I substituted the Weierstrass
  identities and confirmed `sympy.simplify` gives residual 0. The
  cross-product reading (`F1=0 ⟺ direction of ray BK parallel to B−C`) is
  algebraically correct (I verified the cross-product identity by hand).
  The stronger geometric claim "exactly at `β=∠ABC`, not merely at a
  parallel configuration" is plausible (monotonic sweep argument) but I
  did not independently re-verify this specific direction-uniqueness claim
  in full rigor — I certified the algebraic factorization unconditionally
  and flagged this residual uncertainty explicitly in the lemma file
  (`lemmas/branch-crossing-locus-equals-angle-B.md`).
- `F2`'s classification and the connectedness of the valid `β`-range are
  honestly reported as open — no overclaim.
- This is a **genuinely different mechanism** from the sibling's
  acute-angle metric bound (continuity/IVT via shared resultant zero-loci,
  vs. a direct trigonometric inequality) — real framing diversity within
  the branch-selection sub-problem, as the file itself argues and I agree.

### fixed-point-concyclic — CHANGES REQUESTED (Status: partial, correct as self-reported)
- **Verified correct, in full**: Lemma 6 (four vertex-sign cross-product
  identities) — I re-derived all four directly in free symbolic
  coordinates `bx,by,cx,cy` and got exact zero residuals against the
  claimed RHS in every case. This is a genuine, fully general fact (not
  example-only), and correctly closes the round-2-flagged overclaim (the
  N/M-vertex sign facts). Certified as
  `lemmas/vertex-sign-cross-product-identities.md`.
- **Verified correct, in full**: Step 4's negative result. I built `P1,P2,P3`
  and `T` exactly as displayed in the file, computed the Gröbner basis (9
  generators, matching the file's claim), and confirmed the reduction of
  `T` is nonzero, with the exact factor structure
  `−(B·C̄−B̄·C)·S(...)/(B̄C̄)` claimed (matched symbolically, not just in
  functional form). This is a genuinely useful, correctly-diagnosed
  negative result — the file is honest that the "independent-conjugate
  ideal membership" shortcut does not work, and correctly explains why
  (the relaxed variety is strictly larger than the true real-conjugate
  locus). No overclaim.
- Two secondary gaps (collinearity exclusion, isosceles case) are
  correctly flagged as still open.

### ptolemy-trig-identity — CHANGES REQUESTED (Status: partial, correct as self-reported)
- **Spot-checked and confirmed**: Lemma S1 (ray-angle determines cyclic
  order) — the half-angle computation `P−A =
  2sin(φ/2)(−sin(φ/2),cos(φ/2))` is a standard, correct identity, and the
  monotonicity conclusion follows immediately. This is a genuinely new,
  fully general, reusable lemma with no gap. Certified as
  `lemmas/ray-angle-determines-cyclic-order.md`.
- Lemma S2 (projection identity `c=a\cos B+b\cos A`, hence direction angle
  of `C−B` is `π−B`) is a standard textbook fact, correctly applied.
- The Proposition ("Q is angularly extreme, governed by sgn(AB−AC)") is a
  correct, fully synthetic consequence of S1–S3 — no numerics needed, and
  the file is explicit that this alone was previously only numerical and
  is now proved.
- **The one remaining case-split gap** (`∠BAK<∠BAL`) is honestly reported
  as unproved, backed only by ~90 numerically-checked configurations
  across 9 triangle shapes — correctly not claimed as a theorem. Two
  genuine proof attempts (tan-formula comparison, σ-symmetry check) are
  reported as having failed, with correct diagnoses (the tan comparison
  needs case analysis not completed; the σ-symmetry check is self-dual,
  hence uninformative — I checked this self-duality claim by hand and it
  is correct: applying σ to `α<β_L` gives `α'<A−α`, i.e. `α<A−α'=β_L`, the
  same statement).
- **The general Ptolemy equality ⟹ concyclic theorem** (already certified
  round 2) is correctly reused, and the application of `(W,X,Y,Z)` to
  `(A,K,L,Q)` in both the `AB>AC` and `AB<AC` cases is worked out
  correctly (I traced through the index assignment and confirmed the
  diagonal/side products match the two target identities as claimed).
- Symbolic completion of the trig identity is honestly still open (no
  overclaim — labeled numerics-only, per "prove don't conjecture").

## Certified lemmas this round

- `lemmas/symbolic-genericity-certificate.md` (new) — the round's headline
  result, doubly independently reproduced by me from scratch. Supersedes
  `homogeneity-decoupling-rotation-param.md`'s concrete-triangle-only scope
  for the downstream ideal-membership fact.
- `lemmas/vertex-sign-cross-product-identities.md` (new) — Lemma 6 from
  `fixed-point-concyclic`, fully general, independently re-verified.
- `lemmas/branch-crossing-locus-equals-angle-B.md` (new) — the algebraic
  factorization/parallel-vector fact from `coordinate-bash-resultant-boundary`,
  certified with an explicit caveat distinguishing the certified algebraic
  fact from the (plausible but not independently re-verified) stronger
  "exactly β=∠B" geometric reading.
- `lemmas/ray-angle-determines-cyclic-order.md` (new) — Lemma S1 from
  `ptolemy-trig-identity`, fully general, independently re-verified.

No lemma was rejected this round — all four builders' promotable-lemma
proposals that I checked held up under independent re-derivation. (I did
not separately certify every promotable-lemma item listed in each file —
e.g. Lemma S2–S4, the explicit two-ray construction, etc. — for time
reasons; these are standard/derivative facts that I spot-checked but did
not write up as separate certified lemma files. They remain usable within
their own approach files.)

## `current.md`

Updated: `## Status` remains `partial`. Added a Round 3 section to
`## Approaches tried` recording all four verdicts and independent
verifications above. Added a "Round 3 update — gap 1 is now fully closed"
section to `## Current best` summarizing the closed genericity gap and the
precisely-isolated remaining branch-selection gap (with the two
independent partial mechanisms now on the table). `## Full proof` remains
absent (Status is `partial`).

## Verdicts (routing)

- **coordinate-bash-resultant**: CHANGES REQUESTED — real progress (gap 1
  closed), gap 2 (branch selection) remains; re-dispatch to push the
  acute-angle-bound / resultant-factor lead, or pivot to the sibling's IVT
  mechanism.
- **coordinate-bash-resultant-boundary**: CHANGES REQUESTED — real
  progress (gap 1 re-confirmed, new IVT mechanism with one sub-fact
  proved), two precise sub-gaps remain (F2's geometric meaning,
  range-connectedness).
- **fixed-point-concyclic**: CHANGES REQUESTED — real progress (sign gap
  fully closed, new precisely-diagnosed negative result on the complex
  elimination), central elimination itself still open.
- **ptolemy-trig-identity**: CHANGES REQUESTED — real progress (case-split
  narrowed to one inequality, KQ/LQ closed forms proved), that inequality
  and the symbolic trig identity completion remain open.

No RETHINK, no APPROVE this round — all four approaches remain viable and
should stay in the population. Per CLAUDE.md's shared-gap-plateau rule:
the identity itself is no longer the shared wall (proved this round);
branch selection is now the sole shared wall, attacked from genuinely
different angles by the two coordinate-bash-resultant siblings this round
— round 4 should push these two levers further and/or seek a synthetic
resolution of `F2`'s geometric meaning, before concluding a framing pivot
is needed.
