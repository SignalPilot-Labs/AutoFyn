## imo-2026-02

Opening the initial field (round 1, empty population). All four attack the whole claim OM=ON; kept far apart in framing so they don't share one wall. Shared terrain (numerically confirmed by all three explorers, 1e-14): the hypotheses leave a 1-parameter family in β=∠KBA=∠ACL; OM=ON holds across it; O slides along the fixed perp-bisector of MN; σ:(B↔C,M↔N,K↔L) fixing A,O maps the hypothesis set to itself; ρ (spiral sim at A) sends B→C,M→N but NOT K→L. Cheap kills ruled out: no concyclicity among {A,B,C,M,N,K,L}, no ΔBKM~ΔCLN, no SAS ΔOMK≅ΔONL, OB≠OC. No geometry cruxes in the corpus.

I independently re-verified the core reduction MX/NY = b/c (=0.99121) exactly at β=20°,30°,40° on a scalene triangle, and confirmed AXKL cyclic (∠KXA+∠KLA=180°) and BA·BX=pow(B). ρ(X)≈Y but NOT exactly (off at 2nd decimal) — so no single spiral sim finishes it.

---

pow-reduction-trig: new
Target: OM=ON for every admissible configuration.
Technique: Power of a point + law of sines in the sub-triangles named by the hypotheses (avoids computing O).
Skeleton:
  1. OM=ON ⟺ pow(M,⊙AKL)=pow(N,⊙AKL) — power of a point (OP²−R²).
  2. X,Y = 2nd meets of AB,AC with ⊙AKL; pow(M)=MA·MX, pow(N)=NA·NY — secant/chord through A∈circle.
  3. MA=MB=c/2, NA=NC=b/2 ⟹ target ⟺ MX/NY=b/c — midpoint hypothesis.
  4. Inscribed angles in ⊙AKL pin X,Y (∠KXA=∠KLA etc.) — inscribed angle thm.
  5. Solve hypotheses (3),(4) for cevian lengths BK,CL via law of sines in LBK,LNC,LCK,BMK.
  6. Express MX,NY as closed trig forms in β,B,C,b,c.
  7. Show MX/NY=b/c identically in β.
Key lemmas: reduction OM=ON⟺MX/NY=b/c (pow factors on chords AX,AY, midpoints collapse it); MX a sine-rule expression via the inscribed angle at X; the identity MX/NY=b/c forced by σ-symmetry (MX=F(β;B,C,b,c), NY=F(β;C,B,c,b)) + one value check.
Open gaps: GAP-1 closed forms for BK,CL then MX,NY (the load-bearing computation; ∠LNC,∠BMK are angles at midpoints N,M); GAP-2 the identity MX/NY=b/c (use σ, don't brute-force).
Cases to cover: single trig identity ⟹ all β (analytic on connected interval); directed-length sign of pow (M,N interior — settled).
Watch out for: never compute O/R; ∠LNC,∠BMK live at midpoints not B/C; σ swaps (3)↔(4), use it to halve GAP-1.

synthetic-sigma-spiral: new
Target: OM=ON, via the stronger "O ∈ perp-bisector(MN)".
Technique: directed-angle chase + spiral similarity ρ + σ symmetry, targeting a concyclicity that forces O onto perp-bisector(MN).
Skeleton:
  1. Prove ρ (center A, angle A, ratio AC/AB) sends B→C, M→N — midpoints give exact ratio.
  2. OM=ON ⟺ O∈perp-bisector(MN) ⟺ MA·MX=NA·NY (X,Y as above), synthetically.
  3. Reduce to MB·MX=NC·NY via midpoints.
  4. CRUX: construct an auxiliary point (2nd-int X, ρ(K), or reflection K′=2M−K) creating a concyclicity NOT present among the 7 given points; prove ∠(KX,KA)=∠(LY,LA) from (2),(3),(4).
  5. σ transports the B-side identity to the C-side ⟹ done.
Key lemmas: ρ:B→C,M→N (matched ratio/rotation); crux concyclicity appears only after ONE constructed point (raw config has none — the angle conditions (3),(4) ARE inscribed-angle equalities awaiting a point); σ transport.
Open gaps: GAP-1 (crux) identify the auxiliary point + prove the directed-angle equality — undetermined, test candidate concyclicities numerically first; GAP-2 write Lemma ρ.
Cases to cover: use directed angles mod 180° so betweenness needs no split.
Watch out for: ρ(K)≠L (refuted); NO concyclicity among the 7 points (all refuted) — MUST construct a new point; no ΔBKM~ΔCLN; K′=2M−K (parallelogram BK′AK) is the strongest auxiliary-point candidate.

coordinate-identity: new
Target: OM=ON via the single scalar identity O_x(β) ≡ (M_x+N_x)/2.
Technique: analytic/complex bash on the whole β-family; BC on x-axis ⟹ MN horizontal ⟹ OM=ON ⟺ O_x=const.
Skeleton:
  1. B=(−p,0),C=(q,0),A=(a_x,a_y); M,N at height a_y/2, MN horizontal.
  2. K=B+t_K û_K(β), L=C+t_L û_L(β) from hypothesis (2).
  3. Impose (3),(4) ⟹ solve 2×2 system for t_K(β),t_L(β) closed form.
  4. O_x by circumcenter determinant formula.
  5. Simplify O_x−(M_x+N_x)/2 ≡ 0 as identity in β (sympy to find factorization, then written proof).
Key lemmas: closed form t_K,t_L (system linear in tangents after clearing midpoint angles); identity O_x≡midpoint (β cancels; σ-oddness under p↔q,a_x↦−a_x forces the symmetric part to vanish).
Open gaps: GAP-1 closed form t_K(β),t_L(β) — WATCH the angles ∠LNC,∠BMK depend on the unknowns, system may be mildly nonlinear; GAP-2 the symbolic cancellation (must be a written identity, not "sympy=0", valid for the whole interval).
Cases to cover: one analytic identity ⟹ all β; exclude degenerate collinear A,K,L.
Watch out for: genuinely distinct from pow-reduction-trig (this computes O, that avoids it); the step-3 nonlinearity trap; sympy may not auto-simplify — factor/resultant + human transcription.

midpoint-doubling-phantom: new
Target: OM=ON for every admissible configuration.
Technique: reflect K over M, L over N (phantom points K′=2M−K, L′=2N−L) to eliminate the midpoint-angle conditions, then median-length + σ balancing.
Skeleton:
  1. K′=2M−K, L′=2N−L ⟹ BK′AK, CL′AL parallelograms (AK′=BK∥BK, AL′=CL∥CL).
  2. Rewrite ∠BMK,∠LNC (hyps (3),(4)) as vertex-A angle statements via the reflection.
  3. Median law: OM²=(OK²+OK′²)/2−|KK′|²/4 with OK=R (M midpoint of KK′); same for N.
  4. Reduce OM=ON to a balance between K′,L′ and the circle.
  5. Prove the balance via rewritten conditions + σ (K′↔L′).
Key lemmas: parallelogram AK′=BK (central symmetry at M); median-distance OM²=(R²+OK′²)/2−|KK′|²/4; balance (OK′-side vs OL′-side) forced by σ.
Open gaps: GAP-1 translate the midpoint angles to vertex A (directed angles, numeric check); GAP-2 (crux) prove the balance — TEST OK′=?OL′ numerically FIRST; derive the precise target from the median law before proving (OM=ON does NOT reduce to OK′=OL′ alone).
Cases to cover: reflection orientation (state directed conventions).
Watch out for: distinct framing (phantom points are primary objects); NO termwise congruence ΔOMK≅ΔONL (KM≠LN, ∠KOM≠∠LON refuted) — the balance is a summed/median identity; verify Lemma B numerically before building.

---
Field summary: pow-reduction-trig (metric, avoid O) and coordinate-identity (compute O) are the two most self-contained routes; synthetic-sigma-spiral and midpoint-doubling-phantom are the higher-variance synthetic bets whose crux is "construct the right auxiliary point." All four share the confirmed reduction pow(M)=pow(N) but reach it by four different mechanisms, so they do NOT share one wall. Recommend building pow-reduction-trig and coordinate-identity first (most likely to close), keeping the two synthetic slugs live for diversity.
