# Outline review — imo-2026-02, round 1

All four approaches target the full claim OM = ON end to end (whole attempts, not
fragments), and the field is genuinely spread: a finite trig identity, a synthetic
transformed configuration, a polynomial certificate, and a deformation argument.
The shared step (median formula OM = ON ⟺ OB² − OC² = (c²−b²)/2) is unconditional
elementary vector algebra, verified independently by two explorers — sharing it is
free, not a single-gap trap; the load-bearing gaps beyond it are pairwise different
in kind. No approach rests on a refuted conjecture (the outliner's refutation list
is respected in every file's "Watch out for" section).

## New adversarial evidence produced this review (important — builders read this)

I stress-tested the most dangerous hidden assumption in the leading approach:
that the goal identity of secant-trig-identity Step 6 follows from E1–E6 *alone*,
without branch/interiority side conditions (the analogue of the mirror-component
failure the outliner found for the complex encoding). Probe:
`/tmp/round-1/scratch/reviewer_branch_test.py` (+ `reviewer_branch_test2.py`,
high-precision confirm `reviewer_hp.py`).

Result: on two unrelated scalene triangles (A=55°, b=4.3, c=6.0, φ=18°; and
A=71°, b=7.1, c=3.9, φ=31°), I found all 8 distinct roots of the K-side system
(E1&E5, E3) and all 8 of the L-side system (E2&E6, E4) — including roots far
outside any valid configuration range — and the goal identity
2R(c sin δ − b sin(δ+∠A)) = (c²−b²)/2 held on **all 64 root combinations**, to
1e-48 at 50-digit precision (four apparent float-level violations at a
near-degenerate root vanished under mpmath refinement).

Consequences:
1. The Step-6 identity of secant-trig-identity is (very strongly evidenced to be)
   an **unconditional algebraic identity modulo E1–E6** — the elimination need not
   carry semialgebraic branch conditions. All configuration content lives in
   *deriving* E1–E6 (and the additive splittings ∠ACK = φ+χ, ∠ABL = φ+ψ) from the
   hypotheses, not in the elimination.
2. The mirror-component obstruction that breaks plain ideal membership in
   complex-certificate is an artifact of the weaker Im(·)=0 (mod-π, sign-free)
   encoding. Encoding the hypotheses the trig way — one φ shared at B and C, with
   the additive angle splittings — apparently already cuts the right variety.
   The complex builder should substitute the resolved/trig-equivalent forms
   before hunting a certificate, instead of fighting the branch factors.

## Per-approach verdicts

### secant-trig-identity — APPROVE
Sound skeleton. Steps 1–2 are unconditional (median formula; power of B, C along
secants through A ∈ ω); Steps 3–4 verified to 1e-15 by the outliner and the E3/E4
mechanism (BK two ways with MB = c/2) is correct — the midpoint enters as exactly
the factor 2. The single load-bearing gap (the elimination identity) is now
evidenced to be branch-free (see above), which makes this the most concrete line
in the field. Requirements for the build (not blockers):
- Derive E1–E6 rigorously from the configuration hypotheses. In particular the
  additive decompositions ∠ACK = φ+χ, ∠ABL = φ+ψ come from "L inside ∠ACK" /
  "K inside ∠LBA" — prove them, don't assert; this is where all interiority is
  consumed.
- Step 2 must use directed lengths (pow(B,ω) = c(c − AP) needs AP signed along
  ray AB) and Step 3 a single fixed orientation for δ; pin these once, up front.
- Machine-assisted discovery (sympy groebner/resultants) is fine; the deliverable
  is a human-checkable identity chain.
- Do NOT use △LBK ~ △LNC ratio similarity (refuted) or identify P, Q with named
  points (refuted).

### complex-certificate — CHANGES REQUESTED
The framing is viable and its failure mode is independent of the trig grind's
prose-level risks, but the outline as written walks into a known wall: plain
ideal membership G' ∈ (H₁, H₂) is FALSE (mirror components, outliner-verified).
Required changes:
1. Re-encode conditions 2–3 in branch-pinned form before eliminating — best via
   the trig-resolved substitutions (see evidence item 2 above): parametrize
   K, L by (φ, α_K, χ, α_L, ψ) satisfying the E-system rather than by raw
   Im(·) = 0 equations. My probe indicates the certificate then exists over the
   full algebraic variety, with no semialgebraic multiplier gymnastics.
2. The lemma "A, K, L not collinear" (denominator Im(conj(K)L) ≠ 0) must be
   proved from the sector hypotheses, as the outline itself notes — keep it.
3. Fix the circumcentre formula in Step 3 before building (the outline's own
   "hmm" — derive the w-form pow(P) = |P|² − Re(conj(w)P) once, carefully).
Note the risk: after change 1 this approach and secant-trig-identity become the
same elimination in different coordinates. Acceptable this round as a redundancy
hedge on the field's most likely winner; if both reach the identical Groebner
computation, prune one next round.

### midpoint-reflection-isogonal — CHANGES REQUESTED
The reflection dictionary (Steps 1–3) is exact and elegant — parallelogram facts,
machine-verified — and the boxed identity BK·AP₁ + AK² − CL·AP₂ − AL² = (c²−b²)/2
is a correct reformulation. But the load-bearing Step 5 names no mechanism: the
synthetic auxiliary object is explicitly "not yet identified" and every naive
candidate (four concyclicities, ⊙(AK*L*), AK·CL = AL·BK) is already refuted.
That is an unverified hand-off, and the outline's own fallback collapses into
secant-trig-identity (flagged for pruning by the outliner). Required changes:
- The builder's brief is a bounded hunt: test the two proposed candidates (circle
  through K* tangent to AB at M; circle through L* tangent to AC at N; their
  radical axes with ω) numerically FIRST; if refuted, record and stop — do not
  fall back to the trig grind (that duplicates the sibling).
- Any tangent–chord reading at M/N must check the arc side (the file's own
  warning).
Kept live as the genuinely different (synthetic) framing — the field's hedge if
the algebra proves intractably heavy.

### family-invariance-boundary — CHANGES REQUESTED (do not build this round)
The skeleton is logically sound (Step 3's affine-in-circle-coordinates
reformulation is correct: F' = −2⟨O', B−C⟩, matching the observed "O slides along
the perpendicular bisector of MN"). But it carries TWO load-bearing gaps (the
differential identity AND the anchor limit) plus a branch/connectivity obligation
and IFT hypotheses — the highest rigor burden in the field. Moreover my
branch-test evidence weakens its raison d'être: the finite identity appears to
hold unconditionally on the whole algebraic variety, so the deformation detour
buys no branch-avoidance and adds analytic cost. Issues to fix before it is ever
built: (i) Jacobian nonvanishing for Step 2 must be an actual proof obligation
with a stated route; (ii) the anchor must be named concretely (which endpoint,
what closed form) — currently a bare label; (iii) connectivity of the valid set
per Step 5. Kept in the population as the constant-of-motion holding; rank last.

## Diversity assessment
The field does not share a load-bearing gap: trig elimination / polynomial
certificate / missing synthetic object / differential identity + anchor. The one
proximity risk is secant-trig-identity vs complex-certificate after the
recommended re-encoding (change 1) — both may reduce to the same elimination.
Watch next round: if they converge, replace one with a genuinely new framing
(e.g. an inversion at A, or the explorer's involution-swapping-B↔C idea, which no
current slug pursues).

## Ranking (applied via update_ranking)
1. secant-trig-identity (1546) — fully verified reduction chain + branch-free
   identity evidence; single concrete gap.
2. complex-certificate (1515) — viable with the mandated re-encoding; independent
   machinery.
3. midpoint-reflection-isogonal (1485) — exact dictionary but mechanism-less gap.
4. family-invariance-boundary (1454) — sound framing, heaviest rigor burden, now
   partially dominated by the branch-free identity finding.

build set: secant-trig-identity, complex-certificate, midpoint-reflection-isogonal
