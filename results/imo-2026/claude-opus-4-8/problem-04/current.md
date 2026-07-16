## Status
solved

## Approaches tried
- safe-set-invariant — **solved (APPROVE)**. Two-sided characterization: safe-set closure lemma
  (impossibility for θ≠180/N) + both-multiples cut then multiplicity descent (win for θ=180/N).
- force-2theta-bisect — **solved (APPROVE)**. Same answer and same mathematical content, packaged as
  a Cut Lemma + chain-entry cut + descent move + closure lemma. Both independently complete.
- rational-below-90 — superseded: the "rational ≤ 90°" answer is refuted by θ=72° (Shan-Yu survives).

## Current best
Complete, verified two-sided proof. **Answer: Mulan can force a win iff θ = 180°/N for an integer
N ≥ 2, i.e. iff 180/θ ∈ ℤ.** Verified numerically: winning-side full-game simulation for
N = 2..12 always reaches an angle θ against an adversarial Shan-Yu; losing-side simulation for
θ = 72°, 100°, 40° keeps a safe child indefinitely.

## Full proof

Throughout, a *triangle* is a triple of strictly positive angles summing to 180°. When 180/θ is a
positive integer we call it N (θ = 180°/N). All angles lie in (0°, 180°).

**Answer.** Mulan can force a win in finitely many steps, regardless of Shan-Yu, **iff** θ = 180°/N
for some integer N ≥ 2 (equivalently 180/θ ∈ ℤ).

### 0. Cut mechanics

Let T = (A, B, C). A cut "from vertex A" places P on the side opposite A and splits angle A into
positive parts A₁ and A − A₁ with A₁ ∈ (0, A). Let V_A, V_B, V_C carry the angles and P lie on
V_B V_C. The cevian V_A P splits T into V_A V_B P and V_A P V_C:
- V_A V_B P: angle A₁ at V_A, full B at V_B (side V_A V_B uncut), and 180° − A₁ − B = A + C − A₁ at P.
  So **Child 1 = (A₁, B, A + C − A₁)**.
- V_A P V_C: angle A − A₁ at V_A, full C at V_C, and 180° − (A − A₁) − C = A₁ + B at P. So
  **Child 2 = (A − A₁, C, A₁ + B)**.

The two P-angles are **supplementary**: (A + C − A₁) + (A₁ + B) = A + B + C = 180°. For A₁ ∈ (0, A)
every listed entry is strictly positive (A₁ > 0, A − A₁ > 0, B, C > 0, A + C − A₁ = (A − A₁) + C > 0,
A₁ + B > 0), so both children are genuine triangles and P is not a vertex. Cuts from B or C are the
same statement with the three angle-labels permuted.

### Part A — Impossibility for θ ≠ 180°/N (Shan-Yu survives forever)

Assume 180/θ ∉ ℤ. Define the **safe set** S = { triangles no angle of which is a positive integer
multiple of θ }. A safe triangle has no angle equal to θ = 1·θ, so Mulan has not won on it.

**A.1 — Safe start.** T₀ = (θ/2, θ/2, 180° − θ) is a genuine triangle (θ/2 > 0; 180° − θ > 0 as
θ < 180°; sum 180°). It is safe: θ/2 = jθ needs j = 1/2 ∉ ℤ; 180° − θ = jθ needs 180 = (j+1)θ, i.e.
180/θ ∈ ℤ, excluded. So T₀ ∈ S. Shan-Yu opens with T₀.

**A.2 — Closure Lemma.** *If 180/θ ∉ ℤ and T = (A, B, C) ∈ S, then for every cut at least one child is
in S.* By label symmetry treat a cut from A: Child 1 = (A₁, B, A + C − A₁), Child 2 = (A − A₁, C, A₁ + B).
Since B, C are not multiples of θ, the only non-inherited angles are A₁, A − A₁ and the two P-angles.
Suppose both children non-safe. Then Child 1 forces A₁ = nθ or A + C − A₁ = nθ, and Child 2 forces
A − A₁ = mθ or A₁ + B = mθ (n, m positive integers). Four exhaustive cases:
1. A₁ = nθ, A − A₁ = mθ ⟹ A = (n+m)θ — contradicts A ∉ multiples (T ∈ S).
2. A₁ = nθ, A₁ + B = mθ ⟹ B = (m−n)θ, and B > 0 ⟹ m > n ⟹ B a positive multiple — contradicts T ∈ S.
3. A + C − A₁ = nθ, A − A₁ = mθ ⟹ C = (n−m)θ, C > 0 ⟹ n > m ⟹ C a positive multiple — contradicts T ∈ S.
4. A + C − A₁ = nθ, A₁ + B = mθ ⟹ 180° = A + B + C = (n+m)θ ⟹ 180/θ ∈ ℤ — contradicts hypothesis.
All impossible, so some child ∈ S. The same four identities arise for cuts from B or C after
relabeling. ∎

**A.3.** Shan-Yu opens at T₀ ∈ S and after each cut keeps a safe child (exists by A.2). By induction
the triangle is always safe, hence never has angle θ. This holds for every θ with 180/θ ∉ ℤ —
rational or irrational, ≤ 90° or > 90°. So Mulan cannot force a win. ∎

### Part B — Sufficiency for θ = 180°/N (Mulan wins in ≤ N − 1 steps)

Now θ = 180°/N, N ≥ 2, so Nθ = 180° and the valid multiple-angles are θ, 2θ, …, (N−1)θ, with
jθ + (N−j)θ = 180°. Shan-Yu makes T; if T has angle θ Mulan has won, so assume not.

**B.1 — N = 2 (θ = 90°): one cut.** Let A be the largest angle, B, C the others. Then C < 90°
(if C ≥ 90° then A ≥ C ≥ 90° gives A + C ≥ 180°, impossible) and B < 90° likewise, so A + C = 180° − B
> 90°. Cut from A with A₁ = A + C − 90° ∈ (0, A) (A₁ > 0 ⟺ A + C > 90° ✓; A₁ < A ⟺ C < 90° ✓). Then
Child 1 = (A₁, B, 90°) and Child 2 = (A − A₁, C, 90°). Both have angle 90° = θ, so Mulan wins in one cut.

**B.2 — N ≥ 3.** *Phase 1 (one cut).* Let A be the largest angle. Any triangle's largest angle is
≥ 60°; since θ = 180/N ≤ 60°, A ≥ θ. If A = θ then A = 60°, N = 3, and A being largest and 60° forces
all angles 60° = θ (excluded). So **A > θ**. The open interval (C, A + C) has length A > θ; with
n := ⌊C/θ⌋ + 1 we get nθ > C and nθ ≤ C + θ < C + A, so **C < nθ < A + C**. Cut from A with
A₁ = A + C − nθ ∈ (0, A) (A₁ > 0 ⟺ nθ < A + C ✓; A₁ < A ⟺ nθ > C ✓). Then
Child 1 = (A + C − nθ, B, **nθ**) and Child 2 = (nθ − C, C, 180° − nθ) = (nθ − C, C, **(N − n)θ**). All
entries positive; nθ > C > 0 gives n ≥ 1 and nθ < A + C < 180° = Nθ gives n ≤ N − 1, so both nθ and
(N − n)θ are multiples jθ with 1 ≤ j ≤ N − 1. Whichever child Shan-Yu keeps carries such a jθ; if
j = 1 Mulan has won, else 2 ≤ j ≤ N − 1.

*Phase 2 (descent).* Suppose the current triangle has an angle jθ, 2 ≤ j ≤ N − 1, at vertex A with
neighbours B, C. Cut from A with A₁ = θ ∈ (0, jθ) (legal as j ≥ 2). Then Child 1 = (θ, B, (j−1)θ + C)
and Child 2 = ((j−1)θ, C, θ + B), both genuine. Child 1 has angle θ; if j = 2 then Child 2 = (θ, C, ·)
also has θ, so both children carry θ and Mulan wins. If j ≥ 3 and Shan-Yu avoids Child 1, the survivor
Child 2 carries (j−1)θ with 2 ≤ j−1 ≤ N−2. The marked multiplicity is a strictly decreasing
monovariant (knowledge_base.md, Invariant/monovariant) bounded below by 2, so after ≤ j−2 descent
cuts it reaches 2 and the next cut wins.

**B.3 — Step count.** N = 2: 1 cut. N ≥ 3: 1 (Phase 1) + ≤ N−3 (descent) + 1 (terminal) = ≤ N−1 cuts.
Finite, against every Shan-Yu response. ∎

### Conclusion

Part A: Mulan cannot force a win when 180/θ ∉ ℤ. Part B: Mulan has an explicit ≤ (N−1)-move winning
strategy from every start when θ = 180°/N. Therefore

> **Mulan can force a win iff θ = 180°/N for some integer N ≥ 2 (iff 180/θ ∈ ℤ).**

*Verification.* θ = 72°: 180/72 = 2.5 ∉ ℤ, losing; T₀ = (36°, 36°, 108°) ∈ S. θ = 90°, 60°, 45°, 36°,
30° (N = 2, 3, 4, 5, 6): winning, as Part B constructs. Full-game simulations confirm both directions.
