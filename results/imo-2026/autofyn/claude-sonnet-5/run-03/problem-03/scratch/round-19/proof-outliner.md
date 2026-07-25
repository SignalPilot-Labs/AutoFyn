## imo-2026-03

self-similar-induction-on-n: revise
Target: The full statement c(n) = 2^n/(2^{n+1}-1), specifically closing
General Theorem GT(m) (the peeling/self-similar induction machinery) for
all m, which requires the general-k Cardinality-Constrained Half-Sum
Lemma GCH(k).
Technique: Self-similar induction on n via GT(m)'s peeling recursion,
now closing the residual sub-lemma GCH(k) via an **extremal-principle /
LP-vertex argument** instead of a circular induction-on-k.
Skeleton:
  1. Restate GCH(k) precisely (already done, certified k=2 case): for R
     finite multiset, max(R)<=2^{k-1}=:cap, |R|<=k+1, sum(R)=S in
     [2^k,2^k+1), then AltSum(R∪Γ_{k-1}) >= 1 — by the certified
     `sharper-odd-residual-and-k2-cardinality-half-sum.md` (k=2 instance)
     and Lemma AS (OddSum-AltSum identity).
  2. **Mandatory cheap-kill first** (per Rule in memory, and explicitly
     flagged by this round's plateau-check explorer): before writing any
     proof, verify computationally that the minimizer of
     AltSum(R∪Γ_{k-1}) subject to sum(R)=S, 0<r_i<=cap is always
     "vertex-shaped" in the LP sense (all but at most one coordinate of
     R pinned at 0 or cap) for k=2..8, several S — use
     `scipy.optimize.linprog` per-interleaving (exact combinatorial LP,
     NOT SLSQP — this round's gtm-general-k explorer found SLSQP gets
     stuck in bad local optima on this piecewise-linear objective, a
     methodological fix that must propagate). If any minimizer is not
     vertex-shaped, the mechanism below is dead cheaply.
  3. **Extremal-principle argument (the new target)**: for fixed
     (k,S,n=|R|), let R* be a minimizer of AltSum(R∪Γ_{k-1}). Show any
     legal two-element mass transfer within R that preserves sum(R)=S
     is non-improving — i.e. either it is blocked (moves a coordinate
     past 0 or cap) or it creates/breaks a tie with a Γ_{k-1}-value, and
     in every case AltSum cannot decrease. This is a smoothing argument
     transplanted from crux `aimo-0119` (extremal-configuration +
     single-item-transfer non-improvement), adapted to this problem's
     actual mechanism: fix a sorted interleaving pattern of R against
     Γ_{k-1}'s fixed dyadic values; AltSum is affine in the r_i on that
     cell (coefficient ±1 by rank parity — this is exactly the Flat/Kink
     Parity Lemma's mechanism, certified in the sibling
     `global-lp-vertex-sufficiency` approach, being reused as a proof
     technique here, NOT cited as a black box — re-derive it for this
     polytope from scratch); an affine functional on a box-simplex
     polytope attains its extrema at vertices (cite the general LP fact
     from knowledge_base.md — check for a named "affine extremization on
     polytope" entry and cite it explicitly).
  4. Enumerate the polytope's vertex shapes for fixed k, n: show they are
     exactly (i) the "chain + tied pair" family R*={2^{k-1},...,4}∪{r,r}
     (k-2 chain elements, |R*|=k, per this round's exact LP finding) for
     k>=3, and the k=2 degenerate case R*={2,r,r} (already certified);
     (ii) any other vertex shape (e.g. using the full |R|=k+1 budget, or
     a different chain truncation) is dominated by (i) — prove this by
     direct comparison of AltSum values across the finite vertex list per
     fixed n, not by assuming it.
  5. Compute AltSum(R*∪Γ_{k-1}) exactly for family (i) via the
     telescoping identity 2^{k-1}+2^{k-2}+...+4 = 2^k-4, confirm it
     equals exactly 1 at S=2^k (tight) and is monotone increasing in S,
     matching the target bound (S+2^k)/2 for OddSum i.e. AltSum>=1.
  6. Conclude GCH(k) for all k, hence GT(m) sub-case (i) e=1 fully closed
     for all m, hence (combined with round 17's even-excess closure) GT(m)
     sub-case (i) fully closed for all excess e>=0.
Key lemmas (claim + mechanism):
  - GCH(k) general form — because the minimizer of a linear functional
    (AltSum, on a fixed interleaving cell) over a box-simplex polytope
    sits at a vertex, and the finite vertex list for this specific
    polytope collapses to one dominant "chain + tied pair" family,
    verified exactly via LP for k=2..5 this round (not approximate
    SLSQP evidence).
  - "WLOG |R|<=k" reduction (secondary, optional) — because the LP
    evidence shows the true minimizer never needs the full cardinality
    budget k+1; if provable cleanly it decouples the count bound from k,
    removing the circularity diagnosed in round 18, but this is NOT
    required if step 3-4 above go through directly on the fixed-n
    vertex enumeration.
Open gaps: the extremal-principle/smoothing argument (step 3) itself is
  not yet proved — only strong LP-exact numeric evidence exists (k=2..5,
  full equality along the whole range, a much stronger evidentiary bar
  than round 18's SLSQP check, but still not a proof). The vertex
  enumeration step (4) — that no other vertex shape beats the chain
  family — needs an actual finite-case argument, not just observation.
Cases to cover: k=2 (already fully proved, base case); k>=3 general
  chain family; the boundary S=2^k (tight equality, must be handled
  exactly, not just as a limit).
Watch out for: (a) do NOT re-attempt the plain induction-on-k peel — it
  is a confirmed dead end (round 18/this round, the residual keeps
  cap=2^{k-1} fixed, a smaller instance of the same excess-1 phenomenon,
  not genuinely smaller); (b) do NOT trust SLSQP/gradient-restart
  numerics on this objective going forward — use exact per-interleaving
  LP only (this round's finding, a real methodological correction); (c)
  the vertex/vertex-enumeration argument is being built FROM SCRATCH on
  R's own box-simplex polytope, not imported wholesale from
  global-lp-vertex-sufficiency's certified lemma (per standing Rule 20:
  never cite a sibling's cell-wise-affine-vertex mechanism directly on a
  different polytope — re-derive it here).

global-lp-vertex-sufficiency: revise
Target: The Existence Theorem — V(p) <= c(n) for every p in the balanced
region — for n=2 in full rigor, then scope exactly what n=3 needs.
Technique: Direct closed-form witness construction (elementary algebra
on one explicit legal response), not LP-vertex enumeration/Σ-shape
classification — this round's explorer found the n=2 case has a much
cheaper direct proof than the heavy machinery this approach has been
building since round 8.
Skeleton:
  1. Re-derive and rigorously write up, in full: from p1+p2+p3=1 and the
     region's defining gap inequalities d1:=p1-p2>γ(2)=1/7,
     d2:=p2-p3>γ(2), derive the closed form p1=(1+2d1+d2)/3, hence
     p1 > 10/21 strictly for every point of the balanced region — a
     one-line algebraic consequence, verify it symbolically (not just
     the 1284-sample numeric check the explorer ran).
  2. Exhibit the witness: split p1 into (p2, p1-p2) [1 cut, legal since
     n=2], leave p2, p3 untouched. Multiset M={p2,p2,p3,p1-p2}. Verify
     all four entries strictly positive.
  3. Prove the rank-order claim rigorously: p3-(p1-p2) = 1-2p1, so
     p3 > p1-p2 is exactly equivalent to p1 < 1/2 (the region's own
     defining inequality, already part of the region's hypotheses) —
     this is NOT a separate case to verify by sampling, it is a direct
     algebraic equivalence; write the full chain of inequalities
     (p2 > p3 from d2>0; p3 > p1-p2 from p1<1/2) establishing the
     descending order p2,p2,p3,p1-p2 unconditionally within the region.
  4. Compute OddSum(M) = p2+p3 = 1-p1 (odd ranks 1,3) from the order in
     step 3, combine with step 1's p1>10/21 to get
     OddSum(M) < 1-10/21 = 11/21 < 12/21 = c(2) = 4/7, strictly, for
     every point of the region — hence V(p) <= OddSum(M) < c(2). This
     closes the n=2 Existence Theorem completely (upper bound direction;
     the lower bound / achievability of c(n) as LB's guaranteed value is
     already handled elsewhere in the overall proof structure via the
     geometric-partition witness, cite that certified result to close
     the loop for n=2 fully).
  5. Scope n=3 honestly: report (per this round's explorer) that the
     direct 1-cut lift (split only p1 into (p2,p1-p2), leave p2,p3,p4
     untouched) FAILS broadly (71/94 sampled violations, unstable rank
     order of the leftover fragment relative to the tail). State
     precisely why the n=2 algebraic coincidence (p3>p1-p2 iff p1<1/2)
     does not have an evident 1-piece-split analogue at n=3, and set the
     next concrete probe: try splitting p1 into 3 fragments (using 2 of
     the 3 cuts) with fragments tied to p2 and p3 respectively, checking
     whether this restores a forced (non-casework) rank order the way
     the n=2 witness had — this is untested, flag it as the immediate
     next step, do not claim it works.
Key lemmas (claim + mechanism):
  - p1 > 10/21 throughout the balanced region at n=2 — because
    p1=(1+2d1+d2)/3 and d1,d2>1/7 strictly force 2d1+d2>3/7.
  - OddSum of the (1,0,0)-branch witness equals 1-p1 exactly — because
    the region's own p1<1/2 hypothesis forces the descending rank order
    p2,p2,p3,(p1-p2) definitionally, not via casework.
Open gaps: n=3 (and general n) Existence Theorem remains fully open;
  the n=2 proof itself, while algebraically verified by the explorer,
  needs the builder to write it as a complete rigorous proof (symbolic
  re-derivation of step 1's identity, not just numeric confirmation) and
  cite/confirm the lower-bound half (LB's guaranteed value = c(2)) is
  already established elsewhere so Status can honestly move for n=2
  specifically, while the overall approach (general n) stays partial.
Cases to cover: none for n=2 (the whole point is casework-free); n=3
  needs a genuine case split on where the leftover fragment(s) rank
  among the tail pieces (not yet enumerated).
Watch out for: do not confuse this narrow closed-form win with a general
  n result — explicitly scope the write-up to n=2 only, and do not
  overclaim progress on Σ-shape classification for general n (that
  remains the long-standing open item for n>=3). Do not reuse the
  (1,0,1)-branch (round 18, certified always > c(2) in the region) as a
  witness anywhere.

lp-duality-split-polytope: advance (light/dormant, no forced new content)
Target: Same overall claim (upper bound V(p)<=c(n)), via the Perfect-Tie-
Family / Mass-Constraint machinery at the region vertex e_0.
Technique: unchanged — Integer-AltSum / Even-Multiplicity / Generalized
Mass-Constraint machinery at e_0.
Skeleton: no new proof content dispatched this round (per plateau-check
  explorer's confirmation: no revival lead found, the certified Mass-
  Constraint Theorem is proved to structurally cap at s~N/2, cannot reach
  the conjectured s>=n-1 necessity by any refinement, and the two crux
  double-counting mechanisms checked in round 18 both fail to transplant
  for identifiable structural reasons). Recommend the builder either (a)
  stand by with no independent build this round (as in round 13), or (b)
  if time permits, a light optional cross-check: does the exact LP
  extremal witness family found this round for GCH(k) (chain
  {2^{k-1},...,4}∪{r,r}) resemble e_0's own certified Twin-Anchor/
  Perfect-Tie construction in any exploitable way? This is speculative
  and NOT required — report honestly if no leverage is found, exactly as
  in round 16's light cross-check.
Key lemmas: none new required.
Open gaps: s>=n-1 necessity conjecture remains open; no mechanism found
  this round or last to close it.
Cases to cover: none.
Watch out for: do not re-attempt mass-counting refinements (proved
  capped at s~N/2); do not re-try aimo-0091/aimo-0178 transplants
  (checked and refuted with reasons in round 18).

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency, lp-duality-split-polytope
