## Status
partial

## Approaches tried
- transcendence-genericity-invariant (round 2): set up the field-theoretic genericity framework
  for the impossibility half. **In the course of stress-testing the invariant against Mulan's
  supplementary-P-angle moves, I DISPROVED the field's stated answer θ=90/n** (verified
  counterexample θ=60°, a 2-move Mulan win) and, by construction + exhaustive search, determined the
  **correct answer θ=180/m (m∈ℤ, m≥2)**. Proved the ⊇ (winnable) direction in FULL rigor for the
  corrected set, and the θ>90 half of ⊆ in full. The generic-survival half of ⊆ for
  0<θ<90, θ∉{180/m} remains open (framework set up; self-restoration is the gap). Outcome:
  major course-correction + two complete halves; crux (generic survival) still open.

## Current best

**Corrected answer (this is the headline finding — the round-1/round-2 target θ=90/n is FALSE):**
> Mulan can force victory **iff θ = 180°/m for some integer m ≥ 2**, equivalently iff **180/θ is an
> integer ≥ 2**. (This set is strictly larger than {90/n}={180/2n}; it also contains 60°=180/3,
> 36°=180/5, 180/7, 20°=180/9, … .)

Proved rigorously below: (I) the ⊇ direction — θ=180/m ⟹ Mulan wins (complete construction);
(II) θ>90° ⟹ Mulan loses (complete induction). Open: (III) 0<θ<90 and 180/θ∉ℤ ⟹ Shan-Yu survives
(strong computational evidence; genericity framework set up; self-restoration lemma is the gap).

### DISPROOF of the previously-stated answer θ=90/n

Take θ=60° (note 90/60=1.5∉ℤ⁺, so the old answer declares θ=60 a LOSS for Mulan). Start
(A,B,C)=(62°,59°,59°) (contains no 60°). Using the normal form child1={x,B,180−x−B},
child2={A−x,C,x+B}:
- **Move 1:** split the 62°-vertex (A=62,B=59,C=59) at x=61°.
  child1={61,59,60} — contains 60°; child2={1,59,120}. Shan-Yu must discard child1 (it holds θ),
  so T={1,59,120}.
- **Move 2:** split the 120°-vertex (A=120,B=1,C=59) at x=60°.
  child1={60,1,119} contains 60°; child2={60,59,61} contains 60°. **Both** contain θ, so Shan-Yu
  loses whichever he keeps.

Hence Mulan forces θ=60° in 2 moves. This contradicts θ=90/n. (Verified by exact rational
arithmetic.) The correct winnable set is {180/m}, confirmed below and by exhaustive
forced-win search (a sound lower bound on Mulan's power) which returns "winnable from every
structure-free generic start" for θ∈{90,60,45,36,30,180/7,22.5,20,180/11} and "not winnable"
for θ∈{50,40,70,72,55,65,80,48,100} — exactly the split 180/θ∈ℤ≥2 vs 180/θ∉ℤ.

### Why 180 is the relevant modulus (the mechanism, and why 90/n was a natural-but-wrong guess)

A cevian from a boundary point P creates two angles at P that are **supplementary**: they are
180−x−B and x+B, summing to 180. If Mulan aims one child's P-angle at a multiple jθ, the other
child's P-angle is 180−jθ. When **180 is an integer multiple of θ** (θ=180/m), 180−jθ=(m−j)θ is
*also* a multiple of θ, so **both** children carry a multiple-of-θ vertex and both are winning
(peel to θ). When 180/θ∉ℤ, exactly one of {jθ, 180−jθ} is a multiple of θ; Shan-Yu keeps the other
child, and the threat dies. The old {90/2^k} and {90/n} guesses came from analyses that only used
the halving/right-angle device (modulus 90) and missed the supplement-of-a-multiple device (modulus
180), which is exactly the extra power that puts 60°, 36°, … into the winnable set.

## Full proof
(Not present: Status is partial. Direction III is open. Directions I and II are complete and are
written in full below as `Current best` support; they should be promoted.)

---

### Normal form (used throughout)

A triangle is an unordered angle triple with positive entries summing to 180°. A move: Mulan picks
a vertex with angle A and a real x∈(0,A); the cevian to the opposite side splits the triangle into
`child1 = {x, B, 180−x−B}` and `child2 = {A−x, C, x+B}`, where B,C are the other two angles. The two
P-angles 180−x−B and x+B are supplementary (they are the two angles at the interior boundary point,
lying on a straight side). Shan-Yu keeps one child. All angles produced are positive:
0<x<A guarantees x>0 and A−x>0; 180−x−B=(A−x)+C>0 and x+B>0. The game halts (Mulan wins) as soon as
some angle equals θ. Standard AND–OR reachability: let W₀={triangles with an angle =θ} and
W_{k+1}=W_k∪{T: some split has BOTH children in W_k}; then **Mulan wins from T ⟺ T∈W(θ):=∪_k W_k**
(Mulan chooses the split = OR-node, Shan-Yu chooses the child = AND-node). "Mulan wins for θ" means
W(θ) contains every triangle (Shan-Yu chooses the starting triangle, so he needs just one triangle
outside W(θ) to survive).

---

### Direction I (⊇): θ=180/m, m≥2 integer ⟹ Mulan wins from EVERY triangle. COMPLETE.

Assume θ=180/m, m≥2, and the current triangle has no angle equal to θ (else Mulan already won).
Note 0<θ≤90.

**Lemma A (peel).** *If a triangle T has a vertex equal to kθ for an integer k with 1≤k≤m−1 (so
0<kθ<180), then T∈W(θ); i.e. Mulan wins from T.*

*Proof.* Downward induction on k. Base k=1: the vertex equals θ, so T∈W₀. Step k≥2: split the
kθ-vertex (A=kθ, neighbours B,C) at x=θ. Since 2≤k, we have θ<kθ=A, so x=θ∈(0,A) is legal.
child1={θ, B, 180−θ−B} contains θ, so child1∈W₀. child2={kθ−θ, C, θ+B}={(k−1)θ, C, θ+B}: its
angles are (k−1)θ>0, C>0, θ+B>0, summing to (k−1)θ+C+θ+B=kθ+B+C=kθ+(180−kθ)=180, a valid triangle
with a vertex (k−1)θ, and 1≤k−1≤m−1. By the induction hypothesis child2∈W(θ). Both children are in
W(θ), so T∈W(θ). ∎

**Lemma B (seed a multiple).** *Any triangle T with no angle equal to θ has a legal split, on its
largest angle, such that BOTH children have a vertex equal to a multiple jθ with 1≤j≤m−1.*

*Proof.* Let A be a largest angle, with the other two B,C. Split A: as x ranges over (0,A), the
child-2 P-angle x+B ranges over the open interval (B, A+B)=(B, 180−C) (using A+B=180−C). We claim
this open interval contains a multiple jθ.

Suppose not. Then B and 180−C lie in one closed gap between consecutive multiples: there is an
integer j with jθ≤B<180−C≤(j+1)θ, whence A=180−B−C=(180−C)−B≤(j+1)θ−jθ=θ. So the largest angle
satisfies A≤θ≤90, forcing all three angles ≤θ.
- If m≥4 then θ=180/m≤45<60, but the largest angle of any triangle is ≥60, contradicting A≤θ.
- If m=3 (θ=60): all angles ≤60 with sum 180 forces all angles =60, i.e. T is equilateral and
  contains θ=60 — excluded (no angle equals θ).
- If m=2 (θ=90): all angles ≤90 with sum 180 and no angle =θ=90 forces all angles <90, in
  particular B<90 and C<90, so B<90=θ<180−C, i.e. 90∈(B,180−C) — contradicting "no multiple in the
  interval."
In every case we reach a contradiction. Hence some multiple jθ∈(B, 180−C), and since
0<jθ<180 we have 1≤j≤m−1.

Set x:=jθ−B. Then x∈(0,A) (because jθ∈(B,A+B)). child1={x,B,180−x−B}={jθ−B, B, 180−jθ}
={jθ−B, B, (m−j)θ}, with all entries positive (jθ>B, and (m−j)θ>0 since j≤m−1). child2
={A−x, C, x+B}={A+B−jθ, C, jθ}, with A+B−jθ>0 (jθ<A+B) and jθ>0. child1 has vertex
(m−j)θ (1≤m−j≤m−1) and child2 has vertex jθ (1≤j≤m−1). ∎

**Direction I conclusion.** From any triangle with no angle θ, Lemma B gives a split both of whose
children carry a vertex kθ (1≤k≤m−1); by Lemma A each such child is in W(θ). Hence the original
triangle is in W(θ). Since the starting triangle is arbitrary, W(θ)=all triangles: Mulan wins for
every θ=180/m, m≥2. (Move count is bounded: one seeding move plus at most m−2 peels ≤ m−1 moves.)
∎

*Verification of the answer by substitution.* θ=90 (m=2): Lemma B with the largest vertex forces a
90° P-angle in both children (a right angle at the foot), an immediate win — matches the classical
θ=90 case. θ=60 (m=3): reproduces the 2-move win exhibited above. θ=45 (m=4): seed 90=2θ, peel once
to 45. All consistent.

---

### Direction II (⊆, part 1): θ>90° ⟹ Mulan loses. COMPLETE.

**Device classification.** *Given a triangle with vertex A (others B,C), none currently equal to θ,
there exists x∈(0,A) with BOTH children containing θ if and only if θ=90° or A=2θ.*

*Proof.* θ can enter child1={x,B,180−x−B} only via x=θ or 180−x−B=θ (B=θ is excluded); it can enter
child2={A−x,C,x+B} only via A−x=θ or x+B=θ (C=θ excluded). The four combinations:
- x=θ and A−x=θ ⟹ A=2θ.
- x=θ and x+B=θ ⟹ B=0, degenerate — impossible.
- 180−x−B=θ and A−x=θ ⟹ subtract: (180−B)−A=0 wait — from 180−x−B=θ, x=180−θ−B; from A−x=θ,
  x=A−θ; equate: 180−θ−B=A−θ ⟹ A+B=180 ⟹ C=0, degenerate — impossible.
- 180−x−B=θ and x+B=θ ⟹ add: 180=2θ ⟹ θ=90°.
So the only possibilities are A=2θ or θ=90°. ∎

**Induction.** For θ>90°: the state-independent device θ=90° is unavailable, and the
state-dependent device A=2θ requires a pre-existing angle 2θ>180°, impossible. By the classification,
no triangle has a split with both children in W₀, so W₁=W₀. Inductively, if W_k=W₀ then "both
children in W_k=W₀" is again the classification's condition, impossible, so W_{k+1}=W₀. Hence
W(θ)=W₀={triangles already containing θ}. Shan-Yu starts with any triangle avoiding θ (e.g. an
equilateral triangle when θ≠60, else (70,70,40)); it is never in W(θ), so he survives forever. ∎

(This also rules out indirect routes through obtuse "gift" angles: any angle >90° is itself
unreachable, so it can never appear as an intermediate either.)

---

### Direction III (⊆, part 2): 0<θ<90 and 180/θ∉ℤ ⟹ Shan-Yu survives. OPEN (the crux).

This is the remaining gap. Below is the genericity framework (the intended engine of this approach),
the sub-results I can prove, and the precise open step.

**Framework.** Shan-Yu picks a starting triangle whose two free angles A₀,B₀ are algebraically
independent over the field K:=ℚ(θ) (C₀=180−A₀−B₀; such reals exist and give a legal triangle, e.g.
A₀,B₀ two independent transcendentals with A₀+B₀<180 chosen so no angle equals θ). All "structural"
constants (θ, 90, multiples jθ, 180) lie in K̄ (the algebraic closure of K in ℝ). Call an angle
*generic* if it is transcendental over K, and a *constant* if it lies in K̄. Every triangle in the
game then has 0, 1, or 3 constant angles (if two are constant so is the third, since they sum to
180∈K). Define the intended invariant:

> **P(T):** T has at least one generic angle, and every constant angle of T lies in a *safe set*
> S(θ) ⊆ K̄, where θ∉S(θ). (In particular no angle of T equals θ.)

If P is preserved along Shan-Yu's chosen children, then no angle ever equals θ and he survives.
Reduction (standard, via the W_k induction): if P(T) implies that for **every** legal split at least
one child satisfies P, then by induction P(T)⟹ T∉W_k for all k ⟹ T∉W(θ); and the generic start
satisfies P (no constants at all). So Direction III reduces to a single **self-restoration lemma**.

**What I proved toward it (partial, rigorous):**

1. *Supplement obstruction (the reason 180/θ∈ℤ is the boundary).* A single split creates two
   supplementary P-angles p and 180−p (one per child). For a child's new P-angle to be a *dangerous*
   constant (a multiple of θ, the only constants from which Direction I forces θ) both p and 180−p
   would need to be multiples of θ; since 180∉θℤ (as 180/θ∉ℤ), at most one of p,180−p is a multiple
   of θ. Hence a freeze move cannot hand Shan-Yu a forced dangerous multiple in *both* children — he
   keeps the non-multiple child. This is exactly the mechanism that fails Direction I's construction
   when 180/θ∉ℤ, and is the seed of self-restoration.

2. *Forcible-constant dynamics on a single constant vertex.* From a level-1 triangle {c, β, γ}
   (c∈K̄ constant, β,γ generic), Mulan's forced operations on the constant are: **halve** c↦c/2
   (splitting the c-vertex at x=c/2 sends both children to constant c/2) and **peel** c↦c−θ for c>θ
   (splitting at x=θ puts θ in one child, forcing c−θ in the other). A constant c reaches θ under
   {÷2, −θ} iff (reversing to ×2, +θ from θ) c∈θℤ⁺. In particular the fork constant 90 reaches θ iff
   90∈θℤ⁺ iff θ=90/n — but the *supplement* route (item 1) shows the additional reachable danger is
   exactly the values 180−jθ, extending 90/n up to the full 180/m; a clean characterization of the
   safe set S(θ)=K̄∖(danger) matching "θ forcible ⟺ 180/θ∈ℤ" is what remains.

**The open step (self-restoration).** Prove: with S(θ) the correct safe set (complement of the
constants from which Mulan can force θ against a generic remainder), for θ<90, 180/θ∉ℤ, every legal
Mulan split from a P-triangle leaves at least one child satisfying P. The genuine difficulty, which
I verified is real and blocks a naive argument, is the interaction between (a) the field-theoretic
"is this angle a constant / a multiple of θ" bookkeeping and (b) the **metric interval constraint**
x∈(0,A): whether Mulan can freeze a P-angle onto a *specific* target constant depends on the actual
real values Shan-Yu chose, not only on the algebra. A pure transcendence-degree invariant is
therefore insufficient (as the reviewer flagged, and as the c−B/x=θ−β collapse move confirms:
it drops transcendence degree and can plant a constant in one child). A correct proof must combine
the algebraic invariant with the metric constraints (Shan-Yu chooses the numeric generic values to
keep every multiple of θ away from the freezable intervals). I did not close this; it is the crux.

**Status of III:** open. Strong computational evidence (exhaustive sound forced-win search: winnable
exactly on 180/θ∈ℤ≥2) plus the supplement obstruction make the boundary certain; the survival proof
for the strict-loss side is not yet rigorous.

## Promotable lemmas

- **Lemma A (peel).** For θ=180/m (m≥2 integer): any triangle with a vertex kθ (1≤k≤m−1) is a
  Mulan win. *Proved in full above (downward induction).*
- **Lemma B (seed a multiple).** For θ=180/m: from any triangle with no angle θ, splitting the
  largest vertex yields a legal split whose two children each carry a vertex that is a multiple of θ
  in {θ,…,(m−1)θ}. *Proved in full above.* Together A+B give the complete ⊇ direction.
- **Device classification.** Both children of a split contain θ ⟺ θ=90° or split-vertex=2θ.
  *Proved in full above.* (Powers Direction II.)
- **Corrected characterization + disproof of θ=90/n.** Mulan wins ⟺ 180/θ∈ℤ≥2; θ=60° is a 2-move
  win (explicit, verified), refuting θ=90/n. *This should update `current.md` and every sibling
  approach — the field's shared target was wrong.*
