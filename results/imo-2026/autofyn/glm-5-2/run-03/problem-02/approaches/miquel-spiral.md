## Status
unsolved

## Approaches tried
- Round 1 (miquel-spiral): Ran the GAP-2 numeric gate required by the
  outline-reviewer. CONJECTURE S (a spiral/indirect similarity center S₀
  sending (B,K)→(C,L) or (M,K)→(N,L), with S₀ = O or on perp-bis(MN)) is
  **FALSE** on every scalene triangle tested. The Miquel point of the
  complete quadrilateral (AB, AC, BK, CL) is also NOT on perp-bis(MN) and
  NOT equal to O. Outcome: DEAD END as framed. The three sub-routes
  (S-route-1/2/3) all collapse because the load-bearing transformation
  does not exist. The approach must go back to the outliner for a re-plan
  if it is to survive; as currently framed it cannot yield a proof.

## Current best
No correct synthetic progress via this framing. The only verified facts
produced are *negative* (the conjectured transformation does not exist):
- Sanity check (validates the (K,L)-construction): for the 1-parameter
  family of valid (K,L) on 5 triangles (4 scalene + 1 isosceles), OM = ON
  holds to ~1e-9 (circumcenter O of △AKL lies on perp-bis(MN) to ~1e-13).
  This confirms the (K,L)-construction is correct and the theorem is true,
  but it does NOT advance this approach toward a transformation-based proof.
- Negative finding: the spiral-similarity center for (B,K)→(C,L) is at
  distance 0.45–1.0 from O and 0.13–0.99 OFF perp-bis(MN) (scalene1,
  α=15..35°). The spiral-similarity center for (M,K)→(N,L) is at distance
  3.4–6.5 from O and 0.05–4.0 OFF perp-bis(MN). The Miquel point of
  (AB,AC,BK,CL) is at distance 2.2–3.9 from O and 0.03–1.7 OFF perp-bis(MN).
  None of these is O, none lies on perp-bis(MN) (beyond numerical-noise
  coincidence on a few samples).
- The only near-hit — a spiral center for the *reversed* pairing (M→N, L→K)
  occasionally landing close to perp-bis(MN) — is NOT an identity: on the
  "random" triangle A=(0,0),B=(5,0),C=(3,2) it sits 0.09 off the line
  with ratio |SM|/|SN|≈0.83 (not 1), i.e. a generic spiral center whose
  proximity to the line is coincidental, not a rotation.

Open gap (the whole approach): there is no transformation (spiral,
indirect similarity, or Miquel point) of the kind CONJECTURE S requires.
The approach is dead as framed.

## Full proof
Not present — Status is `unsolved`. The numeric gate (GAP-2) failed, so
per the outline-reviewer's instruction no proof prose was built on top of
the unverified conjecture.

## Numeric gate report (GAP-2)

Triangles tested (all with α ∈ {15°,20°,25°,30°,35°}, the full 1-parameter
family of valid (K,L) per triangle; (K,L) built by: K = ray from B at α
from BA, root-finding the master relation ∠ACK = α + ∠BMK; L = ray from C
at α from CA, root-finding ∠LBK = ∠LNC):

  scalene1  A=(0,0) B=(4,0) C=(1,3)
  scalene2  A=(0,0) B=(5,0) C=(2,4)
  right     A=(0,0) B=(6,0) C=(0,4)
  random    A=(0,0) B=(5,0) C=(3,2)
  isosceles A=(0,3) B=(-2,0) C=(2,0)  [degenerate-symmetry control]

Construction validated by OM=ON ≈ 1e-9 on every sample (so the (K,L)
pairs genuinely satisfy the three angle conditions (i)-(iii) and the
inside/∠LBA/∠ACK constraints).

Definitions (all named, see knowledge_base.md "Geometry (synthetic &
analytic)"): spiral similarity = direct similarity of the form
x ↦ S₀ + ρ R_θ (x − S₀); its center S₀ is the point with
|S₀P|/|S₀p| = |S₀Q|/|S₀q| and arg((p−S₀)/(P−S₀)) = arg((q−S₀)/(Q−S₀)).
Perp-bisector of MN = locus {X : |XM|=|XN|} (a line ⟂ MN through its
midpoint); O ∈ perp-bis(MN) ⟺ OM = ON (the target). Miquel point of a
complete quadrilateral = the common point of the four circumcircles of the
four triangles determined by choosing three of the four lines.

Tests, all carried out with the corrected perp-bisector (normal parallel
to MN, not to its perpendicular):

1. S₁ = spiral center sending (B,K) → (C,L)  [CONJECTURE S, first pairing].
   - scalene1, α=15°: S₁=(0.821,0.944), dist(S₁,O)=0.453, perpbiMN=0.441.
   - scalene1, α=25°: S₁=(1.142,1.420), dist(S₁,O)=0.615, perpbiMN=0.550.
   - scalene1, α=35°: S₁=(1.289,1.966), dist(S₁,O)=1.010, perpbiMN=0.832.
   - |S₁B|≠|S₁C| (e.g. 3.316 vs 2.063), so the ratio is not 1 and S₁ is
     NOT on perp-bis(BC) either. Verdict: NOT O, NOT on perp-bis(MN).

2. S₂ = spiral center sending (M,K) → (N,L)  [CONJECTURE S, second pairing].
   - scalene1, α=15°: S₂=(−2.339,−4.723), dist(S₂,O)=6.48, perpbiMN=−1.33.
   - scalene1, α=25°: S₂=(−1.670,−2.615), dist(S₂,O)=4.58, perpbiMN=−0.31.
   - |S₂M|≠|S₂N| (6.413 vs 6.840), ratio not 1. Verdict: NOT O, NOT on
     perp-bis(MN).

3. Miquel point Mq of the complete quadrilateral (AB, AC, BK, CL).
   - scalene1, α=15°: Mq=(3.443,1.270), dist(Mq,O)=2.31, perpbiMN=−1.18.
   - scalene1, α=25°: Mq=(3.358,1.717), dist(Mq,O)=2.21, perpbiMN=−0.81.
   - scalene1, α=35°: Mq=(3.217,2.290), dist(Mq,O)=2.19, perpbiMN=−0.30.
   - Verdict: NOT O, NOT on perp-bis(MN). S-route-2 is unsupported.

4. O-centered rotation sending K→L (S-route-1 variant): does the rotation
   about O (angle ∠KOL) that sends K→L also send M→N or B→C?
   - scalene1, α=15°: rotation by 114.0° sends M→(1.526,1.718)≠N=(0.5,1.5),
     B→(0.712,3.545)≠C=(1,3). Verdict: NO. O is not a spiral center for any
     of the natural pairings.

5. Isosceles control: by symmetry the spiral center S₁ for (B,K)→(C,L)
   lies on the symmetry axis = perp-bis(MN) (verified), but S₁ ≠ O
   (dist 0.08–0.50 across α). So even in the symmetric case the
   conjecture "spiral center = O" is false; only the weaker "on the axis"
   holds, purely by symmetry, with no scalene generalization.

6. Reversed-pairing probe: spiral center sending (M,L)→(N,K) [L,K swapped]
   lands NEAR perp-bis(MN) on some samples (perpbiMN ≈ 4e-3) but it is a
   generic spiral center with ratio |SM|/|SN| = |SL|/|SK| ≠ 1, not a
   rotation; on the "random" triangle it is 0.09 off the line with ratio
   0.83. So this is coincidental proximity, not an identity, and it does
   not equal O in any sample (dist 0.20–1.10). Not a usable lemma.

CONCLUSION OF GATE: CONJECTURE S is refuted. There is no spiral/indirect
similarity centered at O, nor one centered on perp-bis(MN) for the stated
pairings (B,K)→(C,L) or (M,K)→(N,L), and the Miquel point of (AB,AC,BK,CL)
is neither O nor on perp-bis(MN). The miquel-spiral framing cannot yield
the conclusion from its defining transformation property.

## Recommendation to the outliner (for a possible re-plan)
The transformation angle is not empty in principle — the angle conditions
(i)-(iii) form a chain (α,β,γ) and the midpoint structure is real — but
the SPECIFIC transformations conjectured do not exist. Any revival of a
transformation framing should NOT propose S₀ = O or S₀ ∈ perp-bis(MN) for
the pairings tested. The honest path is to leave this approach unsolved
and let the rival framings (a-star-cyclicity, analytic-resultant) carry
the proof; this approach stays in the population only as a recorded
negative result so the dead-end is not retried.

## Promotable lemmas
None. (No lemma was proved in full this round; the round produced only a
negative gate result.)
