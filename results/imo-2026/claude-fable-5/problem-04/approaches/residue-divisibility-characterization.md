# Approach: residue-divisibility-characterization

## Status
solved

## Approaches tried
- Mod-θ residue invariant extended from forced moves to ALL moves (round 1, outline) — worked as a skeleton; necessity (θℤ-avoidance invariant) and sufficiency (fork-to-multiples + downward induction on kθ) laid out with gaps A/B/C.
- Round 1 build: closed GAP A (Lemma 2 induction written in full), GAP B (per outline-reviewer's advice, the fork is claimed only for n ≥ 3, where t₀ < θ ≤ 60 ≤ R is strict; n = 2 is routed entirely through the one-move win Lemma 3), and GAP C (four-case invariant written once with the relabeling symmetry made explicit; "≡ mod θ" defined as difference ∈ θℤ ⊂ ℝ, so irrational θ needs no separate treatment). Cut model derived from the problem statement, including the achievability (IVT) direction. Full proof below — **worked**.
- (Field history, for the record) "Mulan wins iff θ ≤ 90°" — dead end, refuted by the mod-θ residue invariant: e.g. θ = 80° is a Shan-Yu win (verified analytically and by exact-fraction search in the round-1 outline review).

## Current best
Complete proof (below) of: **Mulan can guarantee victory in finitely many steps iff θ = 180°/n for some integer n ≥ 2**, with the explicit bound that for θ = 180°/n Mulan wins after at most n − 1 cuts. No open gaps.

## Spec concerns
None. (Two conventions are fixed explicitly in the proof and flagged here for the reviewer: (i) the stop-check occurs at the start of every round, including round 0 on Shan-Yu's initial triangle — this is the literal reading of the statement's loop; (ii) "≡ (mod θ)" means the difference lies in θℤ = {mθ : m ∈ ℤ} ⊂ ℝ, which requires no rationality of θ.)

## Full proof

**Answer.** Mulan can guarantee victory in finitely many steps **exactly for θ = 180°/n, n an integer, n ≥ 2** — equivalently, exactly when 180/θ is an integer. (Since 0° < θ < 180°, we have 180/θ > 1, so "180/θ ∈ ℤ" and "θ = 180°/n for an integer n ≥ 2" are the same condition; the values are θ = 90°, 60°, 45°, 36°, 30°, … Moreover, when θ = 180°/n, Mulan wins after at most n − 1 cuts.)

All angles are measured in degrees. Throughout, θℤ := {mθ : m ∈ ℤ} ⊂ ℝ, and for real x, y we write x ≡ y (mod θ) to mean x − y ∈ θℤ. This is an equivalence relation on ℝ compatible with addition; nothing in the proof requires θ to be rational. Note that θℤ ∩ (0, 180) is finite: it consists of the kθ with integer 1 ≤ k < 180/θ, and each positive element of θℤ equals kθ for a *unique* positive integer k (since θ > 0). We will use the standard **Intermediate Value Theorem** (IVT) once, and the strategy paradigm is the **invariant method** (knowledge_base.md, "Invariants & monovariants").

### 0. The cut model

**Timing convention.** By the statement, each round begins with the check "does 𝒯 have an angle equal to θ?"; if yes the game stops and Mulan wins, and this check also applies to Shan-Yu's initial triangle. Consequently: *if after a cut the kept triangle has an angle equal to θ, Mulan wins at the start of the next round.* We count Mulan's progress in **cuts**; "Mulan wins after at most m cuts" means the stop condition triggers after at most m cutting rounds, whatever Shan-Yu does.

**Lemma 1 (cut model).** Let 𝒯 be a triangle with angles P, Q, R at vertices V_P, V_Q, V_R (so P, Q, R > 0 and P + Q + R = 180). Then:

(a) *(Form of every legal move.)* Every legal move of Mulan is described by a choice of one vertex — label its angle R — and a real parameter t ∈ (0, R), and it splits 𝒯 into two triangles whose angle triples are
  C₁ = (P, t, Q + R − t)  and  C₂ = (Q, R − t, P + t),
each a valid triangle triple (three positive entries summing to 180).

(b) *(Achievability.)* Conversely, for every choice of vertex (angle R) and every t ∈ (0, R) there is a legal move realizing exactly these two children.

*Proof.* (a) Mulan chooses a point X on the perimeter, different from the three vertices; hence X lies in the relative interior of exactly one side. Label the triangle's vertices so that this side is V_P V_Q; its opposite vertex — the unique vertex not on that side — is V_R, and by the statement the cut is the segment X V_R, splitting 𝒯 into the two triangles V_P X V_R and X V_Q V_R (nondegenerate: X is not on line V_P V_R, because that line meets side V_P V_Q only in V_P, and X is interior to the side; symmetrically for the other child).

Set t := ∠V_P V_R X, the angle of child V_P X V_R at V_R. Since X lies strictly between V_P and V_Q, the ray V_R X lies strictly inside the angle ∠V_P V_R V_Q, so 0 < t and ∠X V_R V_Q = R − t > 0; thus t ∈ (0, R).

Angles of child V_P X V_R: at V_P, the ray V_P X equals the ray V_P V_Q (X is on segment V_P V_Q), so the angle is ∠V_R V_P V_Q = P; at V_R it is t; at X it is 180 − P − t = Q + R − t (using P + Q + R = 180). So its triple is C₁ = (P, t, Q + R − t). Symmetrically, child X V_Q V_R has angle Q at V_Q, angle R − t at V_R, and 180 − Q − (R − t) = P + t at X: triple C₂ = (Q, R − t, P + t). All six entries are positive: P, Q > 0; t > 0; R − t > 0; Q + R − t > Q > 0 and P + t > P > 0 (indeed t < R ≤ R + Q). Each triple sums to 180.

(b) Fix the vertex V_R (angle R, opposite side V_P V_Q) and t ∈ (0, R). Parametrize X(s) = (1 − s)V_P + sV_Q for s ∈ [0, 1] and let f(s) := ∠V_P V_R X(s), the angle at V_R between rays V_R V_P and V_R X(s). Since X(s) ≠ V_R for all s ∈ [0, 1] (V_R is not on line V_P V_Q), f(s) = arccos( ⟨V_P − V_R, X(s) − V_R⟩ / (|V_P − V_R|·|X(s) − V_R|) ) is a continuous function of s on [0, 1], with f(0) = 0 and f(1) = R. By the IVT there is s* ∈ [0, 1] with f(s*) = t; since t ≠ 0 and t ≠ R, s* ∈ (0, 1), i.e. X(s*) is interior to side V_P V_Q, a legal choice of cut point. By the computation in (a) this cut produces exactly the children C₁, C₂. ∎

**Reduction to angle triples.** By Lemma 1, both the stop condition ("some angle equals θ") and the full set of options of both players (Mulan: a vertex and t ∈ (0, R); Shan-Yu: keep C₁ or C₂) depend only on the current (unordered) angle triple — never on side lengths. We therefore identify the game state with its angle triple {P, Q, R} (positive reals summing to 180) from now on; every strategy phrased in terms of triples is realizable on the paper triangle, and vice versa.

### 1. Two winning lemmas for Mulan

**Lemma 2 (multiples of θ are winning).** Suppose the current triangle has an angle x ∈ θℤ. Write x = kθ with k the unique positive integer such that kθ = x (possible since 0 < x and θ > 0; automatically kθ = x < 180). Then Mulan wins after at most k − 1 further cuts, whatever Shan-Yu does.

*Proof.* Induction on k.

*Base k = 1:* the triangle has an angle equal to θ, so the game stops at the current round's check and Mulan wins after 0 further cuts.

*Step k ≥ 2:* Label the angles (P, Q, R) with R = kθ. Mulan attacks the vertex with angle R using t = θ; this is legal by Lemma 1(b) since 0 < θ < kθ = R (as k ≥ 2). The children are
- C₁ = (P, θ, Q + (k−1)θ), which contains the angle θ;
- C₂ = (Q, (k−1)θ, P + θ), which contains the angle (k−1)θ, and (k−1)θ ∈ θℤ with 1 ≤ k − 1 and (k−1)θ < kθ < 180.

If Shan-Yu keeps C₁, the game stops at the next check: Mulan has won after 1 ≤ k − 1 further cuts. If Shan-Yu keeps C₂, the inductive hypothesis applied to the angle (k−1)θ gives a Mulan win after at most k − 2 additional cuts, i.e. at most 1 + (k − 2) = k − 1 further cuts in total. Both of Shan-Yu's options lose, so the position is a Mulan win within k − 1 cuts. ∎

**Lemma 3 (θ = 90°: a universal one-cut win).** Let θ = 90°. From any triangle, Mulan wins after at most 1 cut.

*Proof.* Let the current triangle be (P, Q, R) with R a largest angle. If some angle equals 90, the game stops immediately (0 cuts). Otherwise, no angle equals 90; we claim P, Q < 90. Indeed at most one angle of a triangle is ≥ 90 (two such would sum to ≥ 180, forcing the third ≤ 0). If R < 90 then P, Q ≤ R < 90. If R > 90 then P, Q < 90 since neither can be the second angle ≥ 90. (R = 90 is excluded.) 

Mulan attacks the vertex with angle R using t = 90 − P. Legality (Lemma 1(b)): t > 0 since P < 90, and t < R ⟺ 90 − P < R ⟺ 90 < P + R = 180 − Q ⟺ Q < 90 ✓. The children are
- C₁ = (P, 90 − P, Q + R − 90 + P) = (P, 90 − P, 90) (using P + Q + R = 180),
- C₂ = (Q, R − 90 + P, P + 90 − P)... computed from Lemma 1(a): C₂ = (Q, R − t, P + t) = (Q, R + P − 90, 90).

Both children contain the angle 90 = θ, so whichever Shan-Yu keeps, the game stops at the next check: Mulan wins after 1 cut. (Both children are valid triples by Lemma 1(a); e.g. R + P − 90 = 90 − Q > 0.) ∎

### 2. Sufficiency: θ = 180°/n (n ≥ 2 an integer) ⟹ Mulan wins after at most n − 1 cuts

Let θ = 180/n with integer n ≥ 2, and let (P, Q, R) be Shan-Yu's arbitrary initial triangle.

**Case n = 2 (θ = 90°).** Lemma 3: Mulan wins after at most 1 = n − 1 cut.

**Case n ≥ 3 (so θ = 180/n ≤ 60).**

*Subcase (i): some angle lies in θℤ.* That angle is kθ for a unique integer k ≥ 1, and kθ < 180 = nθ forces k ≤ n − 1. By Lemma 2, Mulan wins after at most k − 1 ≤ n − 2 cuts.

*Subcase (ii): no angle lies in θℤ.* Relabel so that R is a largest angle; then R ≥ 60, since R ≥ (P + Q + R)/3 = 60. Let t₀ be the unique representative of the class of −P modulo θ in the interval [0, θ), i.e. t₀ ∈ [0, θ) and t₀ ≡ −P (mod θ). Since P ∉ θℤ, also −P ∉ θℤ, so t₀ ≠ 0; hence
  0 < t₀ < θ ≤ 60 ≤ R,
and in particular t₀ < R **strictly** (the first inequality t₀ < θ is strict even if θ = 60 = R). So attacking the vertex with angle R using t = t₀ is legal (Lemma 1(b)). The children are:

- C₂ = (Q, R − t₀, P + t₀). Here P + t₀ ≡ P + (−P) = 0 (mod θ), and 0 < P + t₀ < 180 (positive as a child's angle by Lemma 1(a); below 180 since it is an angle of a triangle). So P + t₀ ∈ θℤ ∩ (0, 180), i.e. P + t₀ = kθ for a unique integer 1 ≤ k ≤ n − 1.
- C₁ = (P, t₀, Q + R − t₀). Here Q + R − t₀ ≡ Q + R + P = 180 = nθ ≡ 0 (mod θ), and 0 < Q + R − t₀ < 180 as before. So Q + R − t₀ = k′θ for a unique integer 1 ≤ k′ ≤ n − 1.

Whichever child Shan-Yu keeps, it contains an angle in θℤ ∩ (0, 180), so Lemma 2 finishes in at most (n − 1) − 1 = n − 2 further cuts. Total: at most 1 + (n − 2) = n − 1 cuts.

In all cases Mulan wins after at most n − 1 cuts — in particular, in finitely many steps, no matter how Shan-Yu plays. ∎ (Sufficiency)

### 3. Necessity: 180/θ ∉ ℤ ⟹ Shan-Yu survives forever

Assume 180/θ is not an integer, i.e. **180 ∉ θℤ**. Call a triple (P, Q, R) *clean* if none of P, Q, R lies in θℤ. We show Shan-Yu can start clean and stay clean forever; since θ = 1·θ ∈ θℤ, a clean triangle never has an angle equal to θ, so the stop condition never triggers.

**Step 3a (a clean start exists).** Consider isoceles triples (x, x, 180 − 2x) for x ∈ (0, 90); each is a valid triangle triple. Such a triple fails to be clean only if x ∈ θℤ or 180 − 2x ∈ θℤ, i.e. only if x ∈ (θℤ ∩ (0, 90)) or x ∈ { (180 − m)/2 : m ∈ θℤ ∩ (0, 180) }. Both excluded sets are finite (θℤ ∩ (0, 180) is finite because θ > 0), while (0, 90) is infinite. Shan-Yu picks any non-excluded x and starts with the triangle with angles (x, x, 180 − 2x) — clean.

**Step 3b (cleanness survives every cut).** Let the current triple be clean, and consider any move of Mulan. By Lemma 1(a), the move is: choose one of the three vertices and some t in (0, that vertex's angle). Relabeling the triple so that the attacked angle is called R and the other two are called P and Q is merely a renaming (the move's effect is symmetric in the two non-attacked angles, and the hypothesis "clean" is symmetric in all three), so without loss of generality the children are
  C₁ = (P, t, Q + R − t),  C₂ = (Q, R − t, P + t),  t ∈ (0, R),
with P, Q, R ∉ θℤ. We claim **at least one child is clean**. Suppose not: each child has an angle in θℤ.

- In C₁: P ∉ θℤ by hypothesis, so t ∈ θℤ or Q + R − t ∈ θℤ; that is, t ≡ 0 or t ≡ Q + R (mod θ).
- In C₂: Q ∉ θℤ by hypothesis, so R − t ∈ θℤ or P + t ∈ θℤ; that is, t ≡ R or t ≡ −P (mod θ).

One condition from each list must hold; the four combinations each yield a contradiction:

1. t ≡ 0 and t ≡ R ⟹ R ≡ 0 (mod θ), i.e. R ∈ θℤ — contradicts cleanness.
2. t ≡ 0 and t ≡ −P ⟹ P ≡ 0 (mod θ) — contradicts cleanness.
3. t ≡ Q + R and t ≡ R ⟹ Q ≡ 0 (mod θ) — contradicts cleanness.
4. t ≡ Q + R and t ≡ −P ⟹ P + Q + R ≡ 0 (mod θ), i.e. 180 ∈ θℤ — contradicts 180/θ ∉ ℤ.

(All manipulations are subtractions of congruences, valid since θℤ is a subgroup of (ℝ, +); no rationality of θ is used.) Hence some child is clean, and Shan-Yu keeps it.

**Step 3c (conclusion).** By induction on the number of completed rounds: the triple at the start of round 0 is clean (Step 3a), and if the triple at the start of a round is clean then the stop-check fails (θ ∈ θℤ but no angle is in θℤ), Mulan must cut, and Shan-Yu can keep a clean child (Step 3b), so the triple at the start of the next round is clean. Therefore the game never stops: under this Shan-Yu strategy, no finite number of steps ends with a Mulan win. So Mulan cannot guarantee victory in finitely many steps. ∎ (Necessity)

### 4. Conclusion and verification of the answer

Every θ ∈ (0°, 180°) satisfies exactly one of: 180/θ ∈ ℤ or 180/θ ∉ ℤ.

- If 180/θ ∈ ℤ, then since 180/θ > 1 we have θ = 180/n for an integer n ≥ 2, and Section 2 shows Mulan guarantees a win after at most n − 1 cuts.
- If 180/θ ∉ ℤ (this includes every θ > 90°, every irrational θ, and rational values like 80° or 55°), Section 3 gives Shan-Yu a strategy under which the game never terminates.

**Answer: Mulan can guarantee victory in finitely many steps if and only if θ = 180°/n for some integer n ≥ 2** (equivalently, iff 180/θ ∈ ℤ). Verification of the answer on its smallest instances: θ = 90° (n = 2) is a Mulan win by Lemma 3 (one cut); θ = 60° (n = 3) is a Mulan win within 2 cuts by Section 2; θ = 80° is a Shan-Yu survival by Section 3 (180/80 = 2.25 ∉ ℤ). ∎

## Promotable lemmas
- **L2 (kθ is winning).** Statement: If the current triangle has an angle equal to kθ (k ≥ 1 integer), Mulan wins after at most k − 1 further cuts, for any θ ∈ (0, 180). Proved in full as **Lemma 2** above (with the cut model Lemma 1 it depends on).
- **L1 (θ = 90° one-cut win).** Statement: For θ = 90°, Mulan wins after at most 1 cut from any triangle. Proved in full as **Lemma 3** above.
- **L0 (cut model).** Statement: the legal moves on a triangle with angle triple (P, Q, R) are exactly {attack a vertex R, pick t ∈ (0, R)} producing children (P, t, Q+R−t) and (Q, R−t, P+t); both directions (form + achievability). Proved in full as **Lemma 1** above.
- **L3 (cleanness invariant).** Statement: if 180 ∉ θℤ and no angle of the current triple lies in θℤ, then for every legal Mulan move at least one child has no angle in θℤ. Proved in full as **Step 3b** above.
