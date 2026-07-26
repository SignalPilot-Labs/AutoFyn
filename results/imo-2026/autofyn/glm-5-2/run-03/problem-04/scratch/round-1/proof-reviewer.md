# Proof review — IMO 2026 P4 (Mulan's triangle game), round 1

Target answer (verified against problem): **Mulan can guarantee victory in finitely
many steps ⟺ θ = 180°/n for some integer n ≥ 2.**

Three independent complete proofs were submitted this round, all claiming
Status: solved. I reviewed each adversarially and independently: I re-derived
the load-bearing claims from scratch, checked the angle-transformation formula,
checked the four-case necessity closure exhaustively, checked the sufficiency
descent (n=2/θ=90 boundary, parity, base case k=1, max-angle/lattice entry,
altitude-foot-on-segment fact), and verified computations numerically with
numpy across n ∈ {3,4,5,6,7,11,60,180,1000} (sufficiency machinery) and
non-winning θ ∈ {40,50,72,80,89,91,100,110,70,33,50.5,17.3,179} (necessity
closure). All checks passed for all three.

## Common load-bearing step verified independently

**Angle-transformation formula.** Triangle △ABC (angles A,B,C at A,B,C), P on
side BC, cut from P to opposite vertex A, α = ∠BAP ∈ (0,A). Re-derived:
- △ABP: angles α (at A), B (at B, since BP ⊂ BC), 180−B−α (at P). ✓
- △ACP: angles A−α (at A), C (at C), 180−(A−α)−C = B+α (at P). ✓
- The two angles at P sum to (180−B−α)+(B+α) = 180, consistent with P∈BC. ✓
- IVT: α continuous and strictly increasing in P from 0 to A, so every α∈(0,A)
  is realized. ✓

All three proofs use this formula in the identical (correct) form
`(α, b, 180−b−α)` and `(a−α, c, b+α)` (with `180−b−α = a+c−α`).

**Four-case necessity closure (all three equivalent).** State (a,b,c) safe
(no angle a positive multiple of θ), 180∉θZ. Cut at A, parameter x:
C1 = (x, b, a+c−x), C2 = (a−x, c, b+x). Since b,c safe, C1 marked ⟺ x or
(a+c−x) marked; C2 marked ⟺ (a−x) or (b+x) marked. "Both marked" expands to
four cases:
- (i) x, a−x ∈ θZ+ → a ∈ θZ+ ✗ (a safe)
- (ii) x, b+x ∈ θZ+ → b = (b+x)−x ∈ θZ+ ✗ (b safe; uses b>0 so b+x>x)
- (iii) a+c−x, a−x ∈ θZ+ → c = (a+c−x)−(a−x) ∈ θZ+ ✗ (c safe; uses c>0)
- (iv) a+c−x, b+x ∈ θZ+ → 180 = (a+c−x)+(b+x) = a+b+c ∈ θZ+ ✗ (180∉θZ+)

Exhaustive (2×2 expansion of two binary disjunctions), each settled. ✓ in all
three proofs. Equilateral opening is safe (60=mθ ⟹ 180=3mθ ⟹ θ=180/(3m),
3m≥3≥2, contradiction). ✓

---

## Approach 1: `lattice-coset-descent` — APPROVE, Status solved

**Structure.** Reduction to angle game + cut-geometry lemma (§1); lattice
L_θ and safe complement (§2); necessity via four-coset intersection Lemma A +
equilateral-defense Corollary (§3); sufficiency via max-angle lattice-point
entry Lemma B + index-k descent Lemma D + Corollaries C, E (§4–5); sharpness
(§6).

**Adversarial re-derivation of the crux (Lemma B).** Relabel A≥B≥C. Need k
with 1≤k≤n−1 and kθ ∈ (C, A+C).
- n≥3: A≥60 (max of three summing to 180). A>θ, else all three <θ (Phase-1,
  non-multiples) ⟹ sum<3θ≤180=sum, contradiction. Interval (C,A+C) length A>θ.
  C not a multiple ⟹ C/θ∉Z. m=⌈C/θ⌉ gives mθ>C (strict, C non-multiple) and
  mθ<C+θ<C+A (θ<A). So mθ∈(C,A+C); mθ<A+C<180=nθ ⟹ m<n ⟹ k=m≤n−1. ✓
  **I reproduced this independently; verified numerically over 20000 random
  Phase-1 triangles per n∈{3,4,5,6,7}: always a valid k.**
- n=2 (θ=90): need 90∈(C,A+C)=90∈(C,180−B), i.e. C<90<B+A=...  C<90 (min,
  ≤1 angle ≥90), and B<90 (else A≥B≥90 ⟹ A+B≥180 ⟹ C≤0). ✓ Verified.

**Entry cut (Corollary C).** x = A+C−kθ; 0<x<A from C<kθ<A+C. C1=(x,B,kθ)
(third = A+C−x = kθ, marked), C2=(A−x,C,(n−k)θ) (third = B+x = 180−kθ =
(n−k)θ, marked since k≤n−1). Positivity: x>0, A−x=kθ−C>0, both marked angles
positive. ✓

**Descent (Lemma D).** State has jθ (j∈{2,…,n−1}); cut at that vertex with
x=θ (legal: 0<θ<jθ). C1=(θ,b,(j−1)θ+c) contains θ (immediate win if kept);
C2=((j−1)θ,c,b+θ) contains (j−1)θ. Index drops j→j−1; base j=1 = θ present
(0 moves). ≤n−1 total. ✓

**n=2/θ=90 boundary, equilateral gap.** Explicitly handled (§4, case n=2):
equilateral (60,60,60) Phase-1 for n=2; 60<90<120. The proof correctly notes
the bound "A≥90" is not needed here and uses the direct C<90<A+C argument.
✓ No skipped case.

**Move bound.** Phase-1 entry (1) + descent (≤n−2) = ≤n−1. Sharpness for
n=2 verified. ✓

**Verdict.** Complete, rigorous, every case settled, both directions proved.
Status: **solved**. APPROVE.

---

## Approach 2: `altitude-halving` — APPROVE, Status solved

**Structure.** Cut-geometry Lemma 1 (§1); halving lemma by strong induction
(§2); sufficiency via altitude-to-right-triangle (§3a) + round-up cut (§3c),
with n=2 boundary (§3b); necessity via safe/unsafe dichotomy + external-angle
closure Lemma 4 (§4); equilateral-defense (§4d).

**Adversarial re-derivation of the crux (k-existence, §3c).** Seek integer k
with 45 < kθ ≤ 90, equivalently k ∈ (L,2L], L=45/θ. Cases:
- L<1 (45<θ≤60, n∈{3,4}): 2L∈[1,2); 1∈(L,2L] since L<1≤2L (L≥0.75). k=1.
- L=1 (θ=45, n=4): (1,2] contains 2. k=2.
- L>1 (θ<45, n≥5): interval length L>1 contains an integer (⌈L⌉ if L∉Z with
  ⌈L⌉<L+1≤2L; L+1 if L∈Z with L<L+1<2L since L>1). ✓
**Numerically verified for n∈{3,4,5,6,7,8,11,60,180,1000}: always a valid k.**

**Altitude step (§3a).** Acute: foot of altitude from any vertex lies interior
(acute ⟹ all angles <90 ⟹ foot on segment for every side). Obtuse at V:
altitude from V to opposite side has foot interior (the two other angles are
<90, the standard foot-on-segment criterion). Both children right-angled at
the foot. The foot is interior ⟹ P≠vertices, legal cut. ✓ **The
altitude-foot-on-segment fact is correctly invoked and correctly applied.**

**Round-up cut (§3c).** Right triangle ∠A=90, B≤C, B≤45. α=kθ−B. Legal:
α>0 (kθ>45≥B), α<90 (kθ≤90, B>0). Children △ABP=(kθ−B,B,(n−k)θ) and
△ACP=(90−kθ+B,C,kθ). Both contain a positive multiple of θ (kθ and
(n−k)θ; n−k≥n/2≥3/2>1 so n−k≥1, in fact ≥2). ✓ Positivity verified
(90−kθ+B≥B>0 since kθ≤90).

**Halving lemma (Lemma 2).** Strong induction; cut α=θ at the kθ-vertex;
child C1 contains θ (immediate win if kept), child C2 contains (k−1)θ;
induction gives ≤k−2 more; total ≤k−1. ✓ Identical to approach 1's Lemma D.

**n=2 boundary (§3b).** Right triangle already contains 90=θ; 0 further
moves; total ≤1=n−1. ✓

**Necessity (§4).** Same four-case external-angle closure (Lemma 4), with the
external-angle identities ∠ADC=B+α, ∠ADB=(A−α)+C correctly derived from the
exterior-angle theorem. Four cases (i)–(iv) match approach 1's exactly.
Equilateral safe. ✓

**Move bound.** ≤1 (altitude, if needed) + ≤1 (round-up, if n≥3) + ≤n−2
(descent) ≤ n. (Looser than approach 1's n−1 but still finite; the bound
claim is ≤n, correctly stated.) ✓

**Verdict.** Complete, rigorous, both directions, all cases settled.
Status: **solved**. APPROVE.

---

## Approach 3: `safe-unsafe-pairing` — APPROVE, Status solved

**Structure.** Cut-geometry (§0); necessity via four-coset closure (§I.1,
algebraic + external-angle geometric restatement) + equilateral defense
(§I.2); sufficiency via halving descent (§II.1), n=2 direct 90-trick (§II.2),
deficit function (§II.3), deficit-sum lemma (§II.4), refined pairing lemma
(§II.5), pairing cut (§II.6), conclusion (§II.7).

**Adversarial re-derivation of the crux (pairing lemma, §II.5).** Under
n≥3, θ≤60; "top" angle = m=n, i.e. x∈(180−θ,180); top ⟹ x>120, two top
would sum >240>180, so ≤1 top. Seek distinct u,v with d(u)<v AND m_u≤n−1.
Negation: for every non-top u and every v≠u, d(u)≥v.
- Case |T|=0 (all non-top): cyclic d(a)≥b, d(b)≥c, d(c)≥a ⟹ d-sum ≥ a+b+c =
  180 = nθ; but deficit-sum ≤2θ ⟹ n≤2, contradicting n≥3. ✓
- Case |T|=1 (c top): a+b=180−c<θ ⟹ a,b∈(0,θ), m_a=m_b=1, d(a)=θ−a,
  d(b)=θ−b. Negation vs v=c: d(a)≥c ⟺ θ−a≥c ⟺ b≥180−θ; d(b)≥c ⟺ a≥180−θ.
  So a,b≥180−θ ⟹ a+b≥2(180−θ)≥240 (θ≤60); but a+b<180<240. ✓
**I reproduced this independently; verified numerically over 20000 random
Phase-1 triangles per n∈{3,4,5,6,7,11,60,180}: pairing always exists, and the
resulting pairing cut always produces two marked children with all angles
positive.**

**Deficit-sum (§II.4).** a=m_aθ−d(a) etc.; summing, d-sum =
(m_a+m_b+m_c−n)θ ∈ (0,3θ) (each d∈(0,θ) since all safe). Multiple of θ, >0
(else d's zero, impossible), <3θ ⟹ ∈{θ,2θ}. ✓ Verified.

**Pairing cut (§II.6).** Cut at vertex with angle v, α=d(u). Legal:
d(u)>0 (u safe), d(u)<v (pairing). Children C1=(d(u),u,(n−m_u)θ) (third =
180−u−d(u) = nθ−m_uθ), C2=(v−d(u),w,m_uθ). Both marked; (n−m_u)θ positive
because m_u≤n−1 (the refinement's exact purpose — without it the top case
m_u=n would give 0, a degenerate angle). ✓ Positivity verified.

**n=2 direct trick (§II.2).** From a triangle with no 90° angle, at least two
angles B,C<90°; A=180−B−C≠90°. Cut at A, α=90−B (legal: α>0 since B<90,
α<A since C<90). Children (90−B,B,90) and (A−90+B,C,90); both contain 90=θ.
✓ Verified numerically.

**Halving descent (§II.1).** Same as approaches 1/2: cut α=θ at kθ-vertex;
C1 contains θ, C2 contains (k−1)θ; induction. ✓

**Move bound.** ≤1 (pairing/90-trick) + ≤n−2 (descent) = ≤n−1. ✓

**Verdict.** Complete, rigorous, genuinely different entry mechanism
(deficit-pairing vs altitude vs max-angle lattice), both directions, all
cases settled. Status: **solved**. APPROVE.

---

## Promotable lemmas — certification

Each builder flagged promotable lemmas. I admit those that meet the full bar
(sorry-free, statement correct and no stronger than proved):

- **cut-geometry-lemma** (all three): correct, proved from scratch, no
  overclaim. ADMIT.
- **four-coset-closure-lemma** (all three, equivalent statements): correct,
  exhaustive four-case proof, no overclaim. ADMIT.
- **halving-k-descent-lemma** (all three): correct, strong induction, no
  overclaim. ADMIT.
- **lattice-point-entry-cut** (approach 1, Lemmas B+C): correct, n=2 handled.
  ADMIT.
- **altitude-right-triangle-entry** (approach 2, §3a+3c): correct, foot-on-
  segment fact correctly invoked. ADMIT.
- **deficit-sum-lemma** (approach 3, §II.4): correct. ADMIT.
- **pairing-lemma-refined** (approach 3, §II.5): correct, the m_u≤n−1
  refinement is exactly what makes the pairing cut nondegenerate. ADMIT.

---

## Summary

All three proofs are complete, rigorous, and correct. The three sufficiency
routes are genuinely different (max-angle lattice-point entry / altitude +
round-up / deficit-pairing) yet all establish the same characterization; the
necessity routes are all the same canonical four-coset closure (correctly
proved in each). No gaps, no skipped cases, no hand-waving, no circularity,
both directions proved in each. Target answer confirmed: θ = 180°/n, n≥2.

Verdict per slug:
- `lattice-coset-descent`: APPROVE, Status solved
- `altitude-halving`: APPROVE, Status solved
- `safe-unsafe-pairing`: APPROVE, Status solved
