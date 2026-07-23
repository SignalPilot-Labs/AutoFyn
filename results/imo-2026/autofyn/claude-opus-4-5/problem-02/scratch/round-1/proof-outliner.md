## imo-2026-02

power-balance: new
Target: Prove OM = ON where O = circumcenter(AKL), M = midpoint(AB), N = midpoint(AC)
Technique: Power of a point + sine rule. Reformulate as pow(M, omega_AKL) = pow(N, omega_AKL), then express via second-intersection lever identity AB . MP_B = AC . NP_N.
Skeleton:
  1. OM = ON iff pow(M) = pow(N) w.r.t. circumcircle omega_AKL -- by power-of-point iff equidistant
  2. pow(M) = MA . MP_B = (AB/2) . MP_B where P_B = second intersection of AB with omega -- by power formula
  3. pow(N) = NA . NP_N = (AC/2) . NP_N where P_N = second intersection of AC with omega -- by power formula
  4. BK = (AB/2) . sin(gamma)/sin(alpha+gamma) from triangle BMK -- by sine rule in BMK
  5. CL = (AC/2) . sin(beta)/sin(alpha+beta) from triangle CLN -- by sine rule in CLN
  6. Condition (iii) controls P_B position via inscribed angles at M -- by angle chase
  7. Condition (ii) controls P_N position via inscribed angles at N -- by angle chase
  8. AB . MP_B = AC . NP_N -- combine steps 4-7
Key lemmas (claim + one-line mechanism):
  - pow(M) = pow(N) iff OM = ON -- because both lie on the same sphere around O
  - BK = (AB/2) sin(gamma)/sin(alpha+gamma) -- by sine rule with angles alpha at B, gamma at M in triangle BMK
  - The lever identity follows from conditions (ii), (iii) embedding the midpoint structure -- mechanism TBD in builder
Open gaps: Step 8 (the lever identity derivation from angle conditions) is the main gap
Cases to cover: none
Watch out for: signed angles are essential; P_B, P_N are on omega_AKL not other circles

complex-identity: new
Target: Prove OM = ON where O = circumcenter(AKL), M = midpoint(AB), N = midpoint(AC)
Technique: Complex algebra with A=0. Angle conditions become "ratio is real" constraints; derive circumcenter x-coordinate identity.
Skeleton:
  1. Place A=0, B=b, C=c, K=k, L=l (complex). M=b/2, N=c/2 -- coordinate setup
  2. Circumcenter O_0 of {0,k,l} satisfies Re(O_0 conj(k))=|k|^2/2, Re(O_0 conj(l))=|l|^2/2 -- perpendicular bisector
  3. OM = ON iff Re(O_0 (conj(c)-conj(b))) = (|c|^2-|b|^2)/4 -- expand |O-M|=|O-N|
  4. (C1): bc/((k-b)(l-c)) in R encodes angle(KBA)=angle(ACL) -- directed angle to arg ratio
  5. (C2): (k-b)(2l-c)/((l-b)c) in R encodes angle(LBK)=angle(LNC) -- note 2l-c involves N=c/2
  6. (C3): b(k-c)/((l-c)(2k-b)) in R encodes angle(LCK)=angle(BMK) -- note 2k-b involves M=b/2
  7. From (C1)-(C3), derive the identity in step 3 -- algebraic elimination
Key lemmas (claim + one-line mechanism):
  - The "factor of 2" (2l-c, 2k-b) encodes midpoints -- because 2l-c is reflection of C over N=c/2
  - Target: 4(b-c).O_0 = |b|^2-|c|^2 -- because this is the condition for M,N equidistant from O
  - Conditions (C1)-(C3) force this identity on the 1-parameter family of (k,l) -- TBD algebraically
Open gaps: Step 7 (the algebraic elimination) is the main gap; requires CAS or clever manipulation
Cases to cover: none
Watch out for: unsigned angles give wrong system; signed angles essential; 1-param family of solutions

sigma-symmetry: new
Target: Prove OM = ON where O = circumcenter(AKL), M = midpoint(AB), N = midpoint(AC)
Technique: Sigma-symmetry (swap B<->C, K<->L, M<->N) + reduction to isoceles case.
Skeleton:
  1. Define sigma: (A,B,C,K,L,M,N) -> (A,C,B,L,K,N,M). Angle conditions are sigma-self-conjugate -- direct check
  2. Triangle AKL = triangle ALK under sigma, so circumcenter O is fixed -- same triangle
  3. M <-> N under sigma -- midpoint swap
  4. Isoceles case (AB=AC): sigma is reflection over perp bisector of BC, fixes O, swaps M,N => OM=ON -- isometry argument
  5. General case: sigma is NOT a geometric isometry, but configurations are algebraically related
  6. Use identity principle: OM=ON is polynomial identity, holds on isoceles dense locus => holds everywhere -- algebraic geometry
Key lemmas (claim + one-line mechanism):
  - Sigma fixes O -- because triangle AKL is preserved (just relabeled K<->L)
  - Sigma swaps M,N -- because M=(A+B)/2 -> (A+C)/2=N
  - Isoceles => OM=ON by symmetry -- sigma is then a geometric reflection
Open gaps: Step 6 (making the continuity/identity principle rigorous for general case)
Cases to cover: isoceles (trivial), general (needs algebraic argument)
Watch out for: sigma is relabeling not isometry in general; perp bis of MN != perp bis of BC

dot-product-identity: new
Target: Prove OM = ON where O = circumcenter(AKL), M = midpoint(AB), N = midpoint(AC)
Technique: Direct dot-product computation: translate OM=ON to 4(B-C).(O-A) = AB^2 - AC^2, then derive from angle conditions.
Skeleton:
  1. OM = ON iff 4(b-c).O_0 = |b|^2 - |c|^2 where b=B-A, c=C-A, O_0=O-A -- expand |O-M|=|O-N|
  2. Circumcenter O_0 of {0,k,l} given by standard formula involving |k|^2, |l|^2, det(k,l) -- perp bisector intersection
  3. Encode angle conditions as constraints on k,l -- as in complex-identity approach
  4. Substitute and verify 4(b-c).O_0 = |b|^2 - |c|^2 -- algebraic computation
Key lemmas (claim + one-line mechanism):
  - 4(B-C).(O-A) = AB^2 - AC^2 iff OM=ON -- because this is the perp-bisector condition
  - Conditions (C2), (C3) involve 2k-b, 2l-c which are the midpoint reflections -- structural link to M,N
Open gaps: Step 4 (the algebraic verification) is the main gap
Cases to cover: none
Watch out for: determinant in denominator; need det(k,l) != 0 (K,L,A not collinear)
