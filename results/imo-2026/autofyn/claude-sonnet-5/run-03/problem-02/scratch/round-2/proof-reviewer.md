# Proof review — round 2, imo-2026-02

Reviewed all four built approaches: `ptolemy-trig-identity`, `fixed-point-concyclic`,
`coordinate-bash`, `coordinate-bash-resultant`. Problem: IMO 2026 P2 (prove OM=ON
for the circumcenter O of AKL). None of the four claims `solved`; all self-report
`partial`. I independently re-derived/re-ran the load-bearing computation of each
(sympy/numpy) rather than trusting the builder's own checks. Verdicts below are all
independent per CLAUDE.md's per-approach routing.

## 1. ptolemy-trig-identity — CHANGES REQUESTED (Status: partial, confirmed accurate)

**Load-bearing claim checked**: the "general Ptolemy equality ⟹ concyclic" theorem
(complex numbers). I independently verified the core identity
$(w-y)(x-z)=(w-x)(y-z)+(x-y)(w-z)$ by symbolic expansion (sympy) — holds exactly.
The triangle-inequality equality-case argument and the resulting real cross-ratio
computation are standard and correctly executed. This theorem is genuinely proved,
gap-free, and general-purpose. **Certified as promotable**
(`lemmas/general-ptolemy-equality-concyclic.md`).

**The corrected-outline claim** (case split on sgn(AB−AC) for which Ptolemy pairing
is correct): this is real, useful negative information, based on numerics on two
independent triangles with residuals differing by orders of magnitude between the
two candidate pairings (not a rounding-level discrepancy) — credible. But the file
itself explicitly and correctly labels this "not yet a synthetic or algebraic
proof," i.e. no overclaiming here; it is presented as a conjecture backed by strong
numerical evidence, exactly per the "prove, don't conjecture" rule.

**What remains open**: the core computation — closed forms for KQ, LQ via Law of
Cosines and the resulting trig identity check eliminating ψ,φ via (III),(IV) — was
not carried out. This is the same central gap the whole population shares, now
posed in a genuinely more explicit/decoupled (angle-variable, half-sized via
σ-symmetry) form. Real progress, gap remains. No overclaiming found; Status
`partial` in the file is accurate.

## 2. fixed-point-concyclic — CHANGES REQUESTED (Status: partial; one overclaim found and corrected)

**Load-bearing claim checked**: the cross-ratio-real ⟺ concyclic-or-collinear
criterion — standard Möbius-map argument, correctly executed. **Certified as
promotable** (`lemmas/cross-ratio-real-concyclic-criterion.md`).

**The claimed improvement over round 1** ("sign/orientation... rigorously
justified... not read off one numerical sample") — I scrutinized this hardest, per
dispatch instructions, and found it is **only partially true**:

- The vertex-B/C sign argument (for hypothesis 1) IS a genuine general fact. I
  independently re-derived it symbolically: for any CCW triangle A,B,C,
  signed_area(B,C,A) = signed_area(A,B,C) (cyclic invariance) and
  signed_area(B,C,A) = -½·(A−B)×(C−B), giving (A−B)×(C−B) < 0 whenever
  signed_area(A,B,C) > 0 — this holds for every CCW triangle, not just the
  file's numeric example. Good.
- The vertex-N/M sign argument (used for H2, H3) is, by the file's own words,
  justified only by "a direct computation, e.g. on a representative CCW triangle" —
  i.e. it IS checked on a single example, directly contradicting the file's earlier
  claim that the whole sign derivation avoids numerical sampling. This is a real,
  if narrow, overclaim: the round's headline improvement ("no unverified numerical
  sign guess remains") does not fully hold for H2/H3's sign.
- I checked the underlying claim is nonetheless TRUE in general (not just on the
  file's example): via sympy, signed_area(N,B,C) = signed_area(A,B,C)/2 for
  N = midpoint(AC), for symbolic A,B,C — i.e. triangle N,B,C always has the same
  orientation as A,B,C, giving cross(NB,NC) > 0 in general whenever ABC is CCW,
  matching the file's claimed sign. So the CONCLUSION used downstream is correct;
  the gap is that the file's own proof of it is not general as written (a
  rigor-rule violation per CLAUDE.md — "no hand-waving... if a step is non-trivial,
  justify it" — this step is exactly that kind of gap).

I have recorded this precisely in current.md and flagged it as something the next
round should close (writing out the short general signed-area argument I found is
a low-cost, high-value fix). It does NOT change the file's honest bottom line — the
central elimination (H1)∧(H2)∧(H3) ⟹ χ∈ℝ was not attempted to completion this
round, so the crux gap is unaffected. Because the crux gap remains open and the
Status is correctly `partial` (not overclaimed as solved), I did **not** certify
(H1)-(H3) as a standalone promotable lemma this round — their derivation as written
has the gap above; certifying them verbatim would propagate an unjustified-in-full
sign claim into the shared lemma cache.

## 3. coordinate-bash — CHANGES REQUESTED (Status: partial, confirmed honest)

This is a self-reported negative-results round and I checked it is not
under-selling or over-selling. Two claims scrutinized:

- **"σ-symmetry doesn't work as hoped."** The argument (the rotation frame
  A=0,B=(1,0),C=(a,c) distinguishes B from C, so σ doesn't literally act on this
  coordinate system) is correct and precisely stated; the "correct fix" (re-derive
  in the σ-conjugate frame) is honestly flagged as extra, unattempted work, not
  claimed to be free. No overclaiming.
- **"Resultants didn't terminate/weren't conclusive."** The report of 3 failed
  elimination attempts (2min-killed Gröbner, 10min-killed direct resultant, two
  106s/310s resultants that DID terminate but were too large — 5564/7941
  monomials — to be useful) is plausible and specific enough (timings, monomial
  counts) to be credible; the methodological diagnosis of why the "reduce modulo
  one constraint, treat the other variable as free" shortcut is invalid
  (k[t1] over k=ℚ(t2,...) being a PID with generic gcd=1) is a genuinely correct
  and useful piece of computer-algebra reasoning, not padding.

No error found in the vector reduction or the σ-symmetry lemma (both re-verified
in round 1 and unchanged here). Real progress (smaller, fully explicit degree-
bounded target polynomials in §5), central elimination still open. Status
`partial` accurate.

## 4. coordinate-bash-resultant — CHANGES REQUESTED (Status: partial; strongest
result of the round, independently reproduced and confirmed — one writeup error
found, does not affect the substance)

This is the highest-stakes claim of the round ("complete ideal-membership
certificate... remainder 0"), so I rebuilt the entire pipeline from scratch
independently (sympy/numpy), not trusting the builder's transcript:

- **Found an error while checking**: the displayed closed form for L in §2
  (`L = ((3+t2(3u²+8u-3))/(5(1+u²)), (4+t2(4u²-6u-4))/(5(1+u²)))`) is algebraically
  wrong — I recomputed L directly from the stated definition
  `L = C + t2·R(β)(A−C)/|AC|` both symbolically (Weierstrass substitution) and
  numerically (direct rotation matrix at β=20°, t2=0.7), and both independently
  give `L_x = (3+3u²+t2(3u²+8u-3))/(5(1+u²))`, `L_y = (4+4u²+t2(4u²-6u-4))/(5(1+u²))`
  — the displayed formula is missing the "+3u²"/"+4u²" terms (confirmed by two
  independent methods, and the numeric mismatch is macroscopic: 0.379 vs the
  correct 0.397 at the tested point, not a rounding error).
- **However**, when I independently derived eq2, eq3 from the *correct* L formula,
  divided by t1²/t2² (the claimed homogeneity), and factored the quotients with
  sympy, the resulting G2a, G2b, G3a, G3b polynomials matched the file's stated
  polynomials **exactly, term for term** — strong evidence the file's actual
  computation used the correct L (matching mine) and only the *displayed*
  intermediate formula in the writeup has a transcription bug. This is a real
  writeup defect that should be fixed (it would mislead anyone trying to verify
  by hand from the displayed formula alone), but it does not undermine the
  substantive result.
- **Independently reproduced the core certificate.** Computing T (target numerator)
  from scratch via the Cramer's-rule circumcenter formula and running
  `sympy.groebner([G2a,G3a], t1,t2,u, order='grevlex').reduce(T)` gives remainder
  **0**, confirming T ∈ ⟨G2a,G3a⟩ exactly as claimed. This is a genuine, checkable
  proof of the target identity on this triangle, restricted to the correct branch.
- **Independently spot-checked the branch selection.** Solved the true (unsquared,
  arccos-based) hypothesis system via `fsolve` at β ∈ {10°,15°,20°,25°}, confirmed
  containment (same-sign area test) and the target identity (OM−ON ≈ 1e-12 to
  1e-15), and confirmed G2a, G3a ≈ 0 while G2b, G3b are macroscopically nonzero
  (0.29–0.78) at every sampled point — matches the file's claim exactly.
- **The two residual gaps are correctly and honestly isolated**: genericity across
  all triangles (a,c symbolic — not attempted; the file correctly identifies this
  as the more significant gap) and a synthetic (not numeric/resultant) proof of
  branch selection valid for every triangle. The file's framing "just needs
  genericity, not a full re-derivation" is honest, not optimistic overreach — it
  explicitly lists what would be required (either a symbolic (a,c) rerun or a
  Schwartz–Zippel sampling argument) without asserting either is trivial or
  already done.

**Certified as promotable**: `lemmas/homogeneity-decoupling-rotation-param.md` (the
t1²/t2² factorization fact — reusable, coordinate-free geometric content, and I
independently reproduced it). Not certified as a lemma (correctly, it is a
computational milestone specific to one triangle, not a general reusable
statement): the concrete Gröbner certificate itself — this belongs in current.md
as a progress marker, not the lemma cache.

## Overall

No approach reaches `solved`; all four verdicts are **CHANGES REQUESTED**. This
round's most consequential development is `coordinate-bash-resultant`'s complete,
independently-reproduced concrete-triangle certificate — the first time any
approach in the population has produced a fully checkable proof of the shared
central identity anywhere in the configuration space (previously only numerics or
non-terminating symbolic attempts). Per CLAUDE.md's shared-gap-plateau rule: the
population has now bottomed out on the *same* identity (A,K,L,Q concyclic /
O·(C−B)=(|C|²−|B|²)/4) for three straight rounds (round 1: 3/3 approaches; round 2:
4/4 approaches), even though round 2's progress came from pushing the same
coordinate framing harder rather than a new one. `spiral-similarity-bootstrap`
remains unbuilt after two rounds and is the field's only genuinely different
framing on record — I recommend the outliner prioritize building it out next round
alongside pushing `coordinate-bash-resultant`'s genericity extension.

`results/imo-2026-02/current.md` has been rewritten (Status remains `partial`,
Approaches tried appended with round 2 entries, Current best rewritten to reflect
the concrete-triangle certificate as the headline development and the precise two
remaining gaps).

Lemmas certified this round (all independently re-verified, no gap found):
- `results/imo-2026-02/lemmas/general-ptolemy-equality-concyclic.md`
- `results/imo-2026-02/lemmas/cross-ratio-real-concyclic-criterion.md`
- `results/imo-2026-02/lemmas/homogeneity-decoupling-rotation-param.md`

Lemma explicitly NOT certified this round: `fixed-point-concyclic`'s (H1)-(H3)
complex sign conditions — the underlying facts are true (I proved the general
case for the N/M-vertex sign myself) but the approach file's own derivation for
H2/H3 relies on a single-triangle check, not a general proof, so certifying the
statement verbatim as promotable "reusable, rigorously derived" content would be
inaccurate; flagged in current.md for the next round to close properly.

Outcomes recorded via `record_outcome`: ptolemy-trig-identity → advanced;
fixed-point-concyclic → partial; coordinate-bash → partial;
coordinate-bash-resultant → advanced.

## Per-approach verdict summary
- **ptolemy-trig-identity**: CHANGES REQUESTED (Status: partial)
- **fixed-point-concyclic**: CHANGES REQUESTED (Status: partial)
- **coordinate-bash**: CHANGES REQUESTED (Status: partial)
- **coordinate-bash-resultant**: CHANGES REQUESTED (Status: partial)
