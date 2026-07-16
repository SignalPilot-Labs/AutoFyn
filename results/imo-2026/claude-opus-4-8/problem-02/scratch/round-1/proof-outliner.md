## imo-2026-02

Round 1 — empty population. Four rival complete attempts at OM = ON, spanning genuinely different overall routes (synthetic power, complex-algebra, coordinate-trig, synthetic-antipode). All four share only the numerically confirmed reformulations; none is a piece of another. Note: I did not register (that is the outline-reviewer's gate); slugs + files are ready for ranking.

Verified reformulations (numerics, machine precision) common to the field:
- OM = ON ⟺ pow(M,⊙AKL) = pow(N,⊙AKL) ⟺ pow(B)−pow(C) = (AB²−AC²)/2 ⟺ O_x = (M_x+N_x)/2 (BC on x-axis) ⟺ A*B = A*C where A* = 2O−A. I re-verified the antipode form myself: dot(B−C, A*−A) = (AB²−AC²)/2 to 1e-13.

---

power-of-point-balance: new
Target: OM = ON (whole claim).
Technique: Power of a point + trig cevians. Turn OM=ON into equal power of M,N, then into a length ratio MA′/NA″ = b/c forced by the angle conditions.
Skeleton:
  1. OM=ON ⟺ pow(M,⊙AKL)=pow(N,⊙AKL) — power = |XO|²−R².
  2. pow(M)=MA·MA′ (MA=c/2), pow(N)=NA·NA″ (NA=b/2), A′,A″ = 2nd intersections of AB,AC with ⊙AKL — power on a secant.
  3. Reduce to MA′/NA″ = b/c — algebra.
  4. Locate A′,A″ via inscribed-angle theorem in ⊙AKL — ∠(A′K,A′A)=∠(LK,LA).
  5. Trig-cevian data: cot∠KAB = cot α+2cot γ, BK=(c/2)sin γ/sin(α+γ), etc. — law of sines in BMK,CNL,ABK,ACL.
  6. Show c·MA′ = b·NA″ using decoupled constraints (I),(II) — trig identity.
Key lemmas:
  - pow(M)=MA·MA′, MA=c/2 — M on secant AB cutting circle at A,A′.
  - CRUX: MA′/NA″ = b/c — A′ fixed by chord AK + inscribed angle; substitute trig-cevian lengths and constraints (I) sin C·sin γ·sin(A+2α+γ)=2 sin A·sin(C−α−γ)·sin(α+γ), (II) analog with (B,β); α-terms cancel, residual ratio = AC/AB.
Open gaps: Step 6 (closed-form MA′,NA″ and the identity c·MA′=b·NA″); Step 4 sign/position of A′,A″.
Cases to cover: sign of the signed power (A′∈(M,B), A″∈(N,C)); α→0 limit sanity.
Watch out for: directed angles mod 180°; A is on the circle (don't double-count); must use all three conditions (fails for arbitrary α,β,γ).

complex-reality-conditions: new
Target: OM = ON (whole claim).
Technique: Complex numbers, A=0. Three angle conditions become reality (∈ℝ) conditions; goal is one Im identity that follows algebraically. Mechanical-but-complete.
Skeleton:
  1. A=0; b,c,k,l for B,C,K,L; M=b/2,N=c/2.
  2. O=(k|l|²−l|k|²)/(−2i·Im[k l̄]) — circumcenter of 0,k,l.
  3. OM=ON ⟺ Re[O(c̄−b̄)]=(|c|²−|b|²)/4 ⟹ target T: Im[(k|l|²−l|k|²)(c̄−b̄)] = Im[k l̄]·(|c|²−|b|²)/2.
  4. (C1) bc/((k−b)(l−c))∈ℝ; (C2) (k−b)(2l−c)/(c(l−b))∈ℝ; (C3) b(k−c)/((l−c)(2k−b))∈ℝ.
  5. Solve (C2)=conj, (C3)=conj for k̄,l̄ — linear algebra over ℂ.
  6. Substitute into T; (C1) forces T=0 — polynomial algebra (sympy to discover, transcribe by hand).
Key lemmas:
  - reality ⟺ equal directed angle (arg of a ratio).
  - CRUX (conjugate-solving): from (C2),(C3) solve k̄,l̄ as rational functions of k,l,b,c,b̄,c̄ — because (C2) carries M-data (2l−c,l−b) and (C3) carries N-data (2k−b,k−c) linearly; substituting into T reduces via (C1) to 0=0.
Open gaps: Step 5 closed forms + nondegeneracy; Step 6 final identity.
Cases to cover: none (identity on the whole variety); confirm denominators (k−b,l−c,2k−b,2l−c,Im[k l̄]) nonzero.
Watch out for: orientation when translating ∠→arg (pin with verify values C1≈26.07,C2≈0.218,C3≈12.02, all real); don't submit CAS output as the proof — named-step derivation required.

trig-decoupled-bash: new
Target: OM = ON (whole claim).
Technique: Coordinates + law of sines. BC on x-axis; compute O_x closed-form; show O_x=(M_x+N_x)/2 as a trig identity (⟺ OM=ON since MN∥BC).
Skeleton:
  1. OM=ON ⟺ O_x=(M_x+N_x)/2 — midsegment MN∥BC ⟹ perp-bisector vertical.
  2. Parametrize K,L by α on rays from B,C.
  3. Solve t_K,t_L via decoupled (I) [α,γ only] and (II) [α,β only] — law of sines + conditions 2,3.
  4. O_x = rational-trig function of (α,β,γ,triangle) — circumcenter formula.
  5. O_x−(M_x+N_x)/2 = 0 under (I),(II) — trig identity.
Key lemmas:
  - Decoupling: (I) is (α,γ), (II) is (α,β) — condition 3 links K↔M via △BMK alone, condition 2 links L↔N via △CNL alone.
  - CRUX (balance): MA′/NA″ = b/c — MA′=f(α,γ,c), NA″=f(α,β,b) with the SAME f by B↔C,M↔N,K↔L symmetry; (I),(II) are the same equation swapped; only b/c scaling survives.
Open gaps: Step 5 closed-form O_x and its vanishing; deriving f and proving both sides share it.
Cases to cover: admissible root selection for γ,β (interior); α→0 sanity (O→circumcenter AMN).
Watch out for: (I),(II) multiple roots — pick interior one; keep B↔C symmetry explicit for "same f"; check every law-of-sines step vs verify_config.py.

antipode-perp-bisector: new
Target: OM = ON (whole claim).
Technique: Synthetic via antipode A*=2O−A of A on ⊙AKL; prove A*B=A*C by angle-chase. Elegant, riskiest.
Skeleton:
  1. OM=ON ⟺ (B−C)·A* = (AB²−AC²)/2 ⟺ A*B=A*C — vector identity (self-verified 1e-13).
  2. A*=(⊥ to AK at K)∩(⊥ to AL at L) — AA* diameter ⟹ ∠AKA*=∠ALA*=90° (angle in semicircle).
  3. A*B=A*C ⟺ A*B²−A*C²=0 — Pythagoras/projection onto BC.
  4. Angle-chase C1,C2,C3 + right angles at K,L ⟹ A*B²−A*C²=0 — directed angles.
Key lemmas:
  - Antipode lemma: OM=ON ⟺ A*B=A*C — 2O=A+A*, difference of squared distances collapses to perp-bisector-of-BC condition on A*.
  - A* location: A*K⊥AK, A*L⊥AL (angle in semicircle).
  - CRUX (balance): A*B²−A*C²=0 — expand A*B²=A*K²+K-contribution via ∠A*KA=90° and ∠KBA=α; terms reorganize into c·(left)−b·(right), vanishing by C2/C3 symmetry.
Open gaps: Step 4 (the synthetic core) — may need a trig-length crutch (borrow cevian formulas from the other approaches) as fallback; making Step 3's projection identity precise.
Cases to cover: A* inside/outside triangle (Step 1 identity is position-free); A≠A*.
Watch out for: highest risk of not closing synthetically — flag early; directed angles; perpendicular foot on either side of BC.

---

Recommended build set (breadth, with a computational safety net):
- complex-reality-conditions and trig-decoupled-bash are the two "will close if ground out" routes (mechanical, complete-in-principle) — prioritize both.
- power-of-point-balance is the cleanest human-readable route if the ratio lemma closes.
- antipode-perp-bisector is the elegant long shot; keep live but lower priority.
Suggested: build set = complex-reality-conditions, trig-decoupled-bash, power-of-point-balance (three parallel), holding antipode-perp-bisector for next round.
