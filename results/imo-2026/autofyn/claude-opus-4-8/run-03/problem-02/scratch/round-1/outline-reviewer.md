# Outline review — imo-2026-02 (IMO 2026 P2, geometry), round 1

Opening the initial field: four whole-attempt approaches at OM=ON. I independently
re-verified the shared foundation on a scalene triangle across the β-family
(`/tmp/check.py`): the configuration is real (fsolve residual ≤1e-13), **OM=ON holds
to machine precision** (|OM−ON| ≤ 2e-13), **MX/NY = b/c exactly** (0.94615 = b/c at
β=0.3, 0.45, 0.6), and the phantom approach's proposed crux **OK′≠OL′** (0.6681 vs
0.6769). So the reduction spine common to all four is sound, and the outliner's
warnings on the phantom lemma are accurate.

No approach is circular, none repeats a recorded dead end (empty population), and each
targets the actual claim OM=ON end-to-end (not a sub-lemma). The four framings are
genuinely far apart — metric/avoid-O, coordinate/compute-O, synthetic/auxiliary-point,
phantom-point — so they do not share one wall. Good diversity.

## pow-reduction-trig — APPROVE
Strongest and most self-contained. Steps 1–3 (OM=ON ⟺ pow(M)=pow(N) ⟺ MX/NY=b/c) are
rigorous standard power-of-a-point + the midpoint hypothesis, and I confirmed MX/NY=b/c
holds *exactly*, so the reduction is not a coincidence. Remaining work is real but
bounded:
- GAP-1 (steps 5–6): closed forms for BK, CL then MX, NY via law of sines in the four
  named triangles. Load-bearing. Reminder the mis-assignment trap: ∠LNC, ∠BMK are at
  midpoints N, M, not at B/C.
- GAP-2 (step 7): the identity MX/NY=b/c. The σ-symmetry mechanism (MX=F(β;B,C,b,c),
  NY=F(β;C,B,c,b)) is a valid route, but the builder must actually exhibit that
  structural F — a bare "σ forces it" is not enough; show the two expressions share one
  functional form. One value-check alone does not prove an identity in β.

## coordinate-identity — APPROVE (heavy but tractable, not a hidden wall)
Judged per the dispatch. The reduction OM=ON ⟺ O_x=(M+N)_x/2 (BC on x-axis ⟹ MN
horizontal) is clean and correct. The step-3 system solved uniquely under fsolve, so it
is genuinely solvable per β; the real question is whether the closed form is clean. This
is a legitimate guaranteed-terminating bash: even if step 3 is mildly nonlinear (angles
at M,N involve the unknowns), one picks the admissible root and the final O_x−midpoint
cancellation is an identity a resultant/factor will certify. Two caveats for the builder:
- GAP-2 must be a **written** algebraic identity valid on the whole β-interval, NOT
  "sympy returned 0" — the rigor rules forbid that.
- Confirm step-3 solvability in closed form before committing to the full cancellation;
  if quadratic, state which root is the in-region one.
Ranked below pow-reduction-trig because it is heavier and computes O (which pow avoids),
but it is not a dead end — a solid independent second route.

## synthetic-sigma-spiral — APPROVE (higher variance, distinct framing)
Lemma ρ (B→C, M→N) is correct and easy. Step-2/3 reduction matches the verified
foundation. The crux GAP-1 is genuinely **undetermined**: the explorers refuted every
concyclicity among the 7 given points and refuted ρ(K)=L, so a new auxiliary point must
be constructed (K′=2M−K is the flagged candidate). This is real risk, but the framing is
the most likely to yield a short human-checkable proof if the point is found, and it is
far from the two computational routes. Builder must numerically test candidate
concyclicities before writing any angle chase.

## midpoint-doubling-phantom — APPROVE to keep live, NOT in build set
Lemma D (median-length OM²=(R²+OK′²)/2−|KK′|²/4) is solid. But its headline Lemma B
(OK′=OL′) is **numerically false** (I confirmed 0.6681≠0.6769). The outliner honestly
flagged this and left the true balancing target undetermined — so the crux is not just
hard but currently unspecified. Weakest of the four; kept live for framing diversity but
not worth a builder this round until the balance target is pinned by numerics.

## Field / diversity note
Healthy spread — no shared single gap. All four route through pow(M)=pow(N) but reach
the finish by four distinct mechanisms. The two synthetic routes both hinge on the same
K′=2M−K auxiliary point; if both stall next round, that is the shared wall to watch, and
the orchestrator should push one approach into a genuinely new framing.

## Ranking (Elo after this round)
1. pow-reduction-trig 1546 — reduction fully verified, only a trig identity remains.
2. coordinate-identity 1515 — guaranteed-terminating bash, heavier.
3. synthetic-sigma-spiral 1485 — undetermined crux point, best-case shortest proof.
4. midpoint-doubling-phantom 1454 — crux lemma refuted, target unspecified.

Build the three far-apart, most-likely-to-progress framings (metric, coordinate,
synthetic); hold the phantom slug live.

build set: pow-reduction-trig, coordinate-identity, synthetic-sigma-spiral
