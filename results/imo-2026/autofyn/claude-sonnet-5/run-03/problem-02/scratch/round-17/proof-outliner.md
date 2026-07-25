## imo-2026-02

coordinate-bash-resultant-boundary-pointwise-tangent: advance
Target: the whole problem's claim (OM=ON, via the reduction chain: vector
reduction -> rotation parametrization -> Case (b) isolation -> the
Reduction Lemma (round 13, New result 1) -> Tgt(A,B)>0 throughout D
(CLOSED, round 16, lemma `tgt-strictly-positive-throughout-D-full.md`) AND
D_1(A)>=0 on the boundary curve C = C_lo (the sole remaining hypothesis).
Technique: this file's existing machinery — Theorem A's exact closed-form
parametrization of C_lo, plus the file's own two already-certified
techniques (Theorem-B/C-style interval-arithmetic branch-covering away
from equality points; the round-16 Taylor + certified Lagrange-remainder
near-corner derivative-sign argument) — reapplied one level down to a
strictly simpler 1-variable target. No new machinery.
Skeleton:
  1. Re-derive D_1 as an explicit function of B alone on C: substitute
     Theorem A's A = Aof(B) := arctan(-sinB*cos(2B)/(2cos^3B)) into
     D_1(A,B) (already an exact identity on C per round 12's certified
     `lemmas/star-factorization-on-boundary-curve.md`, D_1 := (f-g)|_C)
     — by direct substitution + sympy residual check against the file's
     existing D_1(A,B) formula restricted to X_0=cos^2B.
  2. Correct the domain: the true range of C ∩ D is B ∈ [B*, pi/3]
     (equivalently A ∈ [A*, pi/3]), NOT the `-twopoint` sibling's
     A_max ≈ 1.0484 (a numeric continuation artifact past the point
     A=B=pi/3, where C=pi/3 too, i.e. the curve leaves the valid triangle
     domain B<=C beyond that point) — by the domain check angle-sum
     argument (C = pi - A - B, requiring B <= C) confirmed by the
     gap6-lens explorer.
  3. Confirm D_1(B*) = 0 exactly (already certified, corner value) and
     D_1(pi/3) = 0.3976864042779174... > 0 (Theorem-A closed form,
     direct evaluation) — by the file's existing high-precision mpmath
     machinery.
  4. Split the interval at a fixed small delta (e.g. delta = 0.02):
     (a) AWAY-FROM-CORNER: certified interval-arithmetic (mpmath.iv)
     branch-covering sweep of D_1(B) > 0 on the compact sub-interval
     [B*+delta, pi/3] — structurally identical to the already-certified
     Theorem B/C sweeps in this same file, reused verbatim as a method;
     comfortable numeric margin (min ≈ 0.097) makes this the easy part.
     (b) NEAR-CORNER: certified derivative-sign sweep of D_1'(B) >= c > 0
     (e.g. c=1) on [B*, B*+delta], via the round-16 Taylor +
     Lagrange-remainder technique (D_1(B*)=0, so by MVT/FTC
     D_1(B) = integral_{B*}^{B} D_1'(s) ds >= c(B-B*) > 0 for B in
     (B*, B*+delta]) — reusing the exact certified-remainder-bound
     machinery already proved to work for Tgt in round 16.
  5. Conclude D_1(B) >= 0 on all of [B*, pi/3] with equality only at B*,
     closing gap 6 exactly, hence (via the round-13 Reduction Lemma)
     closing the whole approach's outstanding obligations and completing
     the proof of OM=ON.
Key lemmas (claim + mechanism):
  - D_1 as an explicit 1-variable function of B via Theorem A's exact
    closed-form substitution — because C = C_lo is already parametrized
    in closed form (round 12), so composing with the already-certified
    D_1(A,B)|_C identity eliminates A entirely.
  - D_1'(B*) ≈ 4.626 > 0, a clean non-degenerate one-sided derivative —
    because the corner is a simple (order-1) zero, not a higher-order
    tangency, so a first-order Taylor/MVT bound suffices (no concavity
    needed), sidestepping the previously-planned but harder
    concavity/unimodality route.
  - D_1 has no other zero on [B*,pi/3]: single interior max ≈0.4054 near
    B≈1.030, then a monotone decrease to D_1(pi/3)≈0.3977>0 — because the
    away-from-corner interval sweep (step 4a) directly certifies
    positivity throughout, without needing to characterize the interior
    max's exact location.
Open gaps: steps 1 (explicit substitution + residual check), 4a (interval
sweep implementation), 4b (derivative-sign Lagrange-remainder bound) are
all unproved/uncertified as of this round — this is the round's build
target. Step 2 (domain correction) is a numeric finding to be formalized
as an exact argument (angle-sum identity), not yet written as a lemma.
Cases to cover: none (single continuous target on a compact interval,
split only for proof-technique convenience, not casework).
Watch out for: (a) do NOT attempt a literal closed-form/Weierstrass/
polynomial-SOS reduction of D_1(B) directly — confirmed dead end this
round (trisection/casus-irreducibilis obstruction, sin(arctan(t)/3) not
radical in t); stay in the transcendental/interval-arithmetic regime.
(b) the delta=0.02 split point is provisional — the builder should verify
the derivative stays >= the chosen c throughout [B*,B*+delta] with an
actual certified interval bound, not just the reported point samples
(≈5.02, 4.46, 1.29 at B*+0.02,0.05,0.1) — those are floats, not a
certificate. (c) do not confuse this gap's B-domain [B*,pi/3] with the
stale A_max≈1.0484 claim in the `-twopoint` file; correct that file's
numeric-scan description as a side note but it is not load-bearing for
any certified content.

coordinate-bash-resultant-boundary-pointwise-sos: advance
Target: the whole problem's claim, via Num(u,cosB,sinB) >= 0 on Case (b)'s
domain (equivalently (star)), sought as an explicit Positivstellensatz/SOS
certificate: Num - t = sigma_0 + lambda_1*n_1 + lambda_2*n_2 + lambda_3*n_4sq,
sigma_0, lambda_i SOS.
Technique: exact algebraic root-isolation targeting the newly-diagnosed
complementary-slackness structure — build sigma_0 to explicitly contain
the (s-s*)^2 vanishing factor at the exact algebraic root s* of the
domain-boundary generator n_1(s)=0 (a genuine root of a known degree-10
polynomial over Q(sqrt3)), rather than generic numeric eigen-truncation
of a near-singular Gram matrix (already shown, round 16, to fail
decisively at lambda* ≈ -0.51 for a rank-13 attempt using the wrong
directions).
Skeleton:
  1. Isolate s* exactly via sympy.RootOf / exact real-root isolation of
     the known exact degree-10 polynomial n_1(s) (already computed,
     Q(sqrt3) coefficients) — confirm s* ≈ 0.87467526959909686949... is
     the unique real root in the relevant domain window (0, 2-sqrt3),
     and that it is exactly the lower endpoint of the true u-domain
     (n_1 >= 0) at the fixed witness B — by sign-change bracketing plus
     the already-independently-confirmed numeric match to sigma_0's
     near-double root (5-6 sig figs).
  2. Work in the number field K = Q(sqrt3)(s*) (or its minimal
     polynomial's splitting field) — construct an explicit degree-34
     SOS decomposition ansatz for sigma_0 that is REQUIRED to vanish to
     order exactly 2 at s=s*, i.e. write sigma_0 = (s-s*)^2 * q(s)^2 +
     [remaining SOS terms accounting for the other 3 (of 5) near-null
     directions, currently unexplained] — by explicit polynomial
     division / Gram-matrix null-space-constrained SDP (constrain
     M_0 * z(s*) = 0 as a linear equality on the Gram matrix, not
     merely hope numeric optimization finds it).
  3. Re-run the constrained SDP (z(s*) in the null space of M_0 enforced
     as an explicit linear constraint, not discovered post hoc) and
     check feasibility with a genuine (not near-singular) interior
     point — by cvxpy/CLARABEL with the added equality constraint.
  4. IF step 3 succeeds: extract an exact rational (or exact-algebraic)
     certificate via rational rounding + exact residual verification
     (sympy), the standard round-and-project technique already used
     elsewhere in this population, adapted to the exactly-known s*.
     IF step 3 fails (still infeasible or still near-singular after
     removing the s* direction): this is new information — the 3 other
     unexplained near-null directions are NOT resolved by the
     complementary-slackness mechanism alone, and the ansatz (3
     generators n_1,n_2,n_4sq only) itself may be insufficient; report
     honestly and consider a 4th generator.
Key lemmas (claim + mechanism):
  - s* is an exact root of the known degree-10 polynomial n_1(s), lying
    at the boundary of the true u-domain — because n_1 >= 0 IS the true
    domain constraint at fixed B, so its zero set is exactly the domain
    boundary, and SOS certificates are known (complementary slackness /
    KKT) to be forced to vanish where the active constraint is tight.
  - If sigma_0(s*) = 0 and M_0 is PSD, then M_0 * z(s*) = 0 — because
    z(s*)^T M_0 z(s*) = 0 with M_0 PSD forces z(s*) in the null space of
    M_0 (a PSD quadratic form vanishing at a point vanishes its gradient
    there too, i.e. the point is a null vector), the standard SOS/SDP
    complementary-slackness fact, independently confirmed numerically
    this round (99.99999999996% norm capture).
Open gaps: this is exploratory/diagnostic work, not yet a certificate.
Steps 1-2 (exact root isolation, explicit vanishing-order-2 ansatz
construction) are the near-term deliverable; step 3-4 (constrained SDP
re-run, exact extraction) depend on 1-2 succeeding. The 3 remaining
(of 5) near-null eigenspace directions are explicitly UNEXPLAINED and
must not be silently dropped — flag honestly if step 3 does not resolve
them. Whether this "sigma_0 forced to vanish at n_1=0" pattern recurs at
OTHER witness (cosB,sinB) points (needed for a genuine multivariate, not
merely pointwise, certificate) is untested and is a cheap next check
before committing further effort.
Cases to cover: none yet (single witness-point diagnostic; multivariate
generalization is future work, not this round's deliverable).
Watch out for: do not overclaim — this round's finding is a REFRAMING of
round 16's obstruction (explains the dominant real near-double root),
not a resolution; a full 3-of-5 near-null-dimension explanation and
cross-witness-point recurrence remain open. Do not claim feasibility or
a certificate exists until an actual constrained SDP run with exact
residual verification is performed.

coordinate-bash-resultant-boundary: advance
Target: the whole problem's claim, via a Positivstellensatz certificate
for -q_1 < 0 and -r_0 < 0 (the residual T >= 0 target on the E<0 sub-case,
equivalently the whole Case (b) via the file's own reduction chain).
Technique: this round pivots away from the now-fully-exhausted generator
family {1,sigma,tau,1-sigma,1-tau,B_1,-B_2,B_4,B_6,B_{G_0E},B_{G_0N},B_{EN}}
(margin/robustness-reformulated SDP now shows 8/8 infeasible,
degree-independent at maxdeg=10 vs 12, per this round's clarabel-lens
explorer) toward the case-split fallback identified as higher-priority
by the explorer: an explicit domain-aware case-split of q_1 using the
active region conditions G_0>0, E_num<0, Bc>=0, Num<0, rather than a
single global sign-definite combination.
Skeleton:
  1. Formalize the case-split target: partition the residual sub-domain
     (G_0>0 ∧ E_num<0 ∧ Bc>=0 ∧ Num<0) into sub-regions on which q_1 (or
     a piece of it) admits a DIFFERENT sign-definite combination of
     generators per sub-region — by identifying, via a fresh LP/sign
     scan restricted to each candidate sub-region (e.g. split on the
     sign of a natural pivot quantity such as G_0N or Bc-related
     threshold), whether a per-region linear ansatz becomes feasible
     where the global one is not.
  2. In parallel (per explorer's non-dismissal of option (i)): probe for
     a genuinely NEW base generator beyond {G_0, E_num, Num, Bc}, guided
     by the round-13 parity-obstruction theorem's precise necessary
     condition (a multiplier must carry an explicit bare odd power of c
     or d) — construct 1-2 candidate odd-c/odd-d generators (e.g. c*Num,
     d*G_0, or similar (1,0)/(0,1)-graded products) and re-run the LP
     feasibility check with them added to the basis, using the reusable
     harness at `/tmp/round-17/sdp_work/sdp_run.py`.
  3. If either 1 or 2 yields a feasible LP/SDP: extract an exact
     rational certificate (round-and-project + exact sympy residual
     check against -q_1 or -r_0), the standard technique already used
     elsewhere in this population.
  4. If both fail: report honestly, and note this as further evidence
     the whole {G_0,E_num,Num,Bc}-generated Positivstellensatz approach
     (in its "nice" (0,0)-graded product form) is structurally
     insufficient — motivating a genuinely different reduction of Case
     (b) altogether in a future round if this persists.
Key lemmas (claim + mechanism):
  - The margin/robustness SDP reformulation (maximize t s.t. target - t
    in the cone, instead of a pure feasibility SDP) resolves the
    previously-inconclusive CLARABEL NumericalError instances decisively
    — because a pure feasibility SDP is degenerate exactly at a true
    infeasibility boundary (no Slater point), while the margin
    reformulation has an interior-point-friendly optimal value strictly
    away from 0, giving clean, cross-solver-validated (CLARABEL vs SCS),
    eigenvalue-verified negative margins (≈-0.13 to -0.16).
  - Degree-independence of the margin (maxdeg=10 vs 12 identical to 9-10
     digits) — because the extra multiplier freedom at higher degree is
     provably unused by the optimizer, a strong (though not itself a
     proof) signature that the obstruction is structural to the
     generator family, not a truncation artifact.
Open gaps: the case-split (step 1) and new-generator probe (step 2) are
both untried this round — this is the round's build target. Neither is
guaranteed to succeed; the parity-obstruction theorem only names a
NECESSARY property of a working multiplier, not a sufficient
construction.
Cases to cover: the case-split itself (step 1) is casework by
construction — every sub-region carved out of the residual domain must
be covered by SOME sign-definite combination, with no region left
unaddressed; enumerate the regions explicitly once a natural pivot
quantity is chosen, do not leave any region implicit.
Watch out for: (a) do not re-attempt rescaling-alone as a conditioning
fix — confirmed this round not to resolve CLARABEL NumericalError by
itself (only the margin/robustness reformulation works). (b) do not
re-attempt bare 3-generator or minimal 2-generator ansätze at higher
degree in the SAME generator family — round 14 and this round's
degree-escalation check both show this is fruitless. (c) always verify
returned Gram matrices' minimum eigenvalue directly (not trust solver
status alone) — round 16 caught a spurious SCS artifact this way; this
round's clean eigenvalues (≈-1e-8 to -1e-9) show the standard for a
genuine result.
