# Approach: safe-set-invariant

## Status
solved

## Approaches tried
- (round 1) Two-sided characterization via a closed "safe set" invariant (impossibility) and a
  both-multiples cut + multiplicity descent (sufficiency). **Worked** — both directions closed in
  full. The hard gap G1 (Phase-1 entry from an arbitrary start) is closed *uniformly* for N ≥ 3 by
  the both-multiples cut on the largest vertex (interval-length argument), and N = 2 by the direct
  supplementary (90,90) cut. G2, G3, G4 closed by explicit positivity/exhaustiveness checks.

## Current best
Complete two-sided proof (see Full proof). Answer: **Mulan forces a win iff θ = 180°/N for an
integer N ≥ 2**, i.e. iff 180/θ ∈ ℤ. No remaining gap.

## Full proof

Throughout, a *triangle* is an ordered/unordered triple of its three angles, each strictly
positive and summing to 180°. Write N-related quantities with the shorthand: when 180/θ is a
positive integer we call it N (so θ = 180°/N). All angles lie in the open interval (0°, 180°).

**Claim (answer).** Mulan can force a win in finitely many steps, regardless of Shan-Yu, **if and
only if** θ = 180°/N for some integer N ≥ 2 — equivalently 180/θ ∈ ℤ.

### 0. Cut mechanics (verified)

Shan-Yu picks the initial triangle; each round, if the current triangle T has an angle exactly θ
Mulan wins, otherwise Mulan chooses a non-vertex point P on the perimeter and a target vertex,
cuts from that vertex to P, and Shan-Yu keeps one of the two resulting triangles.

Let T = (A, B, C). A cut "from vertex A" places P on the side opposite A and splits the angle A
into two positive parts A₁ and A − A₁ with A₁ ∈ (0, A). The two children are

- **Child 1** = (A₁, B, 180° − A₁ − B) = (A₁, B, A + C − A₁),   (inherits B; apex at P equals A+C−A₁)
- **Child 2** = (A − A₁, C, 180° − (A − A₁) − C) = (A − A₁, C, A₁ + B),   (inherits C; apex A₁+B)

Here we used A + B + C = 180°, so 180° − A₁ − B = A + C − A₁ and 180° − (A − A₁) − C = A₁ + B.
The two apex angles are **supplementary**:
(A + C − A₁) + (A₁ + B) = A + B + C = 180°. Because A₁ ∈ (0, A), every listed angle of each child is
strictly positive (A₁ > 0, A − A₁ > 0, B > 0, C > 0, A + C − A₁ = (A − A₁) + C > 0,
A₁ + B > 0), so both children are genuine triangles. Cuts from B or C are the same statement with
the labels of the three angles permuted. (KB: this is just the interior-cevian angle bookkeeping.)

---

### Part A — Impossibility for θ ≠ 180°/N (Shan-Yu survives forever)

Assume 180/θ ∉ ℤ. Define the **safe set**
> S = { triangles (X, Y, Z) : none of X, Y, Z is a positive integer multiple of θ }.

Since every angle is < 180°, only multiples jθ with jθ < 180° can occur; in particular a triangle
in S has no angle equal to θ (= 1·θ), so on such a triangle Mulan has not yet won.

**A.1 — Shan-Yu's starting triangle is safe.** Let T₀ = (θ/2, θ/2, 180° − θ). It is a genuine
triangle: θ/2 > 0, and 180° − θ > 0 because θ < 180°; the sum is θ/2 + θ/2 + 180° − θ = 180°.
It is safe:
- θ/2 = jθ would force j = 1/2, not an integer; so θ/2 is not a multiple of θ.
- 180° − θ = jθ would give 180° = (j + 1)θ, i.e. 180/θ = j + 1 ∈ ℤ — contradicting 180/θ ∉ ℤ. So
  180° − θ is not a multiple of θ.

Hence T₀ ∈ S. Shan-Yu makes T₀ the initial triangle.

**A.2 — Closure Lemma.** *If T = (A, B, C) ∈ S and 180/θ ∉ ℤ, then for every cut Mulan can make,
at least one child lies in S.*

*Proof.* By the label symmetry noted in §0 it suffices to treat a cut from vertex A; the cases of B
or C are identical after permuting the names of the three angles, and membership in S is symmetric
in the three angles. The children are
Child 1 = (A₁, B, A + C − A₁) and Child 2 = (A − A₁, C, A₁ + B), with A₁ ∈ (0, A).

Suppose, for contradiction, that **both** children are non-safe. Because T ∈ S, its inherited
angles B and C are not multiples of θ. Therefore:
- Child 1 non-safe forces one of its *non-inherited* angles to be a positive multiple of θ:
  **A₁ = nθ** or **A + C − A₁ = nθ** for some positive integer n.
- Child 2 non-safe forces **A − A₁ = mθ** or **A₁ + B = mθ** for some positive integer m.

This gives exactly four combinations; we derive a contradiction in each.

1. **A₁ = nθ and A − A₁ = mθ.** Adding: A = A₁ + (A − A₁) = (n + m)θ, a positive integer multiple
   of θ. But A is an angle of T ∈ S — contradiction.
2. **A₁ = nθ and A₁ + B = mθ.** Subtracting: B = (m − n)θ. Since B > 0 we need m > n, so m − n is a
   positive integer and B is a positive multiple of θ — contradicting T ∈ S. (If m ≤ n then
   B = (m − n)θ ≤ 0, impossible.)
3. **A + C − A₁ = nθ and A − A₁ = mθ.** Subtracting the second from the first:
   C = (A + C − A₁) − (A − A₁) = (n − m)θ. Since C > 0 we need n > m, so C is a positive multiple of
   θ — contradicting T ∈ S. (If n ≤ m then C ≤ 0, impossible.)
4. **A + C − A₁ = nθ and A₁ + B = mθ.** Adding:
   (A + C − A₁) + (A₁ + B) = A + B + C = 180° = (n + m)θ, hence 180/θ = n + m ∈ ℤ — contradicting the
   hypothesis 180/θ ∉ ℤ.

Every case is contradictory, so both children cannot be non-safe; at least one child is in S. This
covers all four ways (2 choices in each child) that both children could be non-safe, so the case
split is exhaustive; and the same four identities arise verbatim for a cut from B or C by symmetry
(resolving G4). ∎

**A.3 — Conclusion of Part A.** Shan-Yu plays: start at T₀ ∈ S (A.1); after each Mulan cut, keep a
child that lies in S (which exists by the Closure Lemma A.2). By induction on the number of rounds,
the current triangle is always in S, hence never has an angle equal to θ. Therefore Mulan never
wins. This holds for **every** θ with 180/θ ∉ ℤ — rational or irrational, ≤ 90° or > 90°. So for
θ ≠ 180°/N, Shan-Yu survives forever and Mulan cannot force a win. ∎(Part A)

---

### Part B — Sufficiency for θ = 180°/N (Mulan wins in finitely many steps)

Now θ = 180°/N with integer N ≥ 2, so **Nθ = 180°** and the multiples of θ that are valid angles are
exactly θ, 2θ, …, (N−1)θ (each < 180°), with the "complementary" identity jθ + (N−j)θ = 180° for
1 ≤ j ≤ N−1.

Shan-Yu makes some initial triangle T. If T already has an angle equal to θ, Mulan has already won,
so assume T has no angle equal to θ. We give Mulan an explicit strategy that wins in at most N − 1
cuts. Two cases by N.

**B.1 — The case N = 2 (θ = 90°): win in one cut.** Every triangle has at most one non-acute angle
(two angles ≥ 90° would already sum to ≥ 180°), hence at least two acute angles. Choose the vertex
A so that the other two angles B and C are both acute (B, C < 90°): if T has a right or obtuse
angle, let A be that (unique) angle; otherwise all are acute and any choice works. Cut from A with
A₁ = 90° − B. Then A₁ = 90° − B ∈ (0, A): indeed A₁ > 0 since B < 90°, and A₁ < A since
90° − B < A ⟺ A + B > 90° ⟺ C < 90°, which holds as C is acute. The two children are
- Child 2 apex = A₁ + B = 90° = θ,
- Child 1 apex = A + C − A₁ = A + C − 90° + B = 180° − 90° = 90° = θ.

Both children have an angle equal to θ = 90°. Shan-Yu must keep one of them, and it has angle θ, so
Mulan wins in one cut. (This resolves G3.)

**B.2 — The case N ≥ 3 (θ = 180°/N ≤ 60°).** We use two phases.

**Phase 1 (one cut — force a multiple of θ, ≥ 2θ, into the survivor, or win).**
Let A be the **largest** angle of T, with the other two angles B and C. The largest angle of any
triangle is ≥ 60°. Moreover A ≠ θ (T has no angle θ), so:
- if N > 3 then θ < 60° ≤ A, hence A > θ;
- if N = 3 then θ = 60°; A ≥ 60° = θ, and A ≠ θ forces A > 60°. (If A = 60° then, being the
  largest, all three angles equal 60° and each equals θ — but then Mulan already won, excluded.)

So in all cases **A > θ**. Consider the open interval (C, A + C). Dividing by θ, the interval
(C/θ, (A + C)/θ) has length A/θ > 1. An open interval of length greater than 1 contains an integer:
with a = C/θ, the integer n := ⌊C/θ⌋ + 1 satisfies n > a (as ⌊a⌋ > a − 1) and
n = ⌊a⌋ + 1 ≤ a + 1 < a + A/θ (the last inequality is A/θ > 1). Hence

> C < nθ < A + C,  with n := ⌊C/θ⌋ + 1 a positive integer.

Because C > 0 we have n ≥ 1, and nθ < A + C = 180° − B < 180° gives nθ < Nθ, so n ≤ N − 1.
Now cut from vertex A with A₁ = x := A + C − nθ. Then x ∈ (0, A): x > 0 ⟺ nθ < A + C ✓, and
x < A ⟺ C < nθ ✓. The children are

- Child 1 = (x, B, A + C − x) = (A + C − nθ, B, **nθ**),
- Child 2 = (A − x, C, x + B) = (nθ − C, C, A + C − nθ + B) = (nθ − C, C, **180° − nθ**) = (nθ − C, C, **(N − n)θ**).

All angles are positive: A + C − nθ = x > 0, nθ > 0; nθ − C = A − x > 0 (since x < A), and
180° − nθ = (N − n)θ > 0 since n ≤ N − 1. So both children are genuine triangles, and **each carries
a positive integer multiple of θ**: Child 1 has nθ (1 ≤ n ≤ N−1), Child 2 has (N − n)θ
(1 ≤ N − n ≤ N−1).

Whichever child Shan-Yu keeps, it has an angle jθ with 1 ≤ j ≤ N − 1. If j = 1 that angle is θ and
Mulan has already won. Otherwise the survivor has an angle jθ with 2 ≤ j ≤ N − 1. (This closes G1:
the construction is uniform over *every* Shan-Yu start with N ≥ 3, needs only A > θ, and x ∈ (0,A)
is explicit.)

**Phase 2 (multiplicity descent — reduce j by 1 each cut until a forced win).**
*Descent Lemma.* Suppose the current triangle has an angle equal to jθ with 2 ≤ j ≤ N − 1; call that
vertex A = jθ, with neighbours B, C. Cut from A with A₁ = θ. This is legal: A₁ = θ ∈ (0, jθ) since
j ≥ 2 makes jθ > θ > 0. The children are
- Child 1 = (θ, B, A + C − θ) = (θ, B, (j − 1)θ + C),
- Child 2 = (A − θ, C, θ + B) = ((j − 1)θ, C, θ + B).

Positivity: (j−1)θ + C > 0 (j ≥ 2), (j − 1)θ > 0, θ + B > 0 — genuine triangles.

- If j = 2: Child 1 = (θ, B, ·) and Child 2 = (θ, C, ·) — **both children have an angle equal to θ.**
  Shan-Yu must keep one; it has θ, so Mulan wins this cut.
- If j ≥ 3: Child 1 has angle θ, so if Shan-Yu keeps it Mulan wins; otherwise Shan-Yu keeps
  Child 2, which has angle (j − 1)θ with 2 ≤ j − 1 ≤ N − 2. The multiple index has strictly
  decreased, from j to j − 1.

Starting from the survivor of Phase 1 (index j₀ with 2 ≤ j₀ ≤ N − 1), Mulan repeatedly applies the
Descent Lemma to the current jθ-vertex. Each cut either ends the game (Shan-Yu keeps a child with θ)
or strictly decreases the index. Since the index is a positive integer bounded below by 2, after at
most j₀ − 2 ≤ N − 3 decreasing cuts the index reaches 2, and the next (terminal) cut produces two
children each containing θ, forcing a win. The index is a strictly decreasing **monovariant** (KB:
monovariant / descent), so the process terminates. (This closes G2: every intermediate triangle was
shown to be genuine and the terminal j = 2 step gives both children θ.)

**B.3 — Step count.** For N ≥ 3: Phase 1 is 1 cut; Phase 2 is at most (N − 3) descending cuts plus
1 terminal cut, so at most N − 1 cuts total. For N = 2: 1 cut. In all cases Mulan wins in finitely
many (≤ N − 1) steps regardless of Shan-Yu's choices. ∎(Part B)

---

### Conclusion

Part A shows Mulan cannot force a win when 180/θ ∉ ℤ (Shan-Yu keeps a safe child forever). Part B
gives Mulan an explicit finite winning strategy whenever θ = 180°/N with integer N ≥ 2. Therefore

> **Mulan can force a win if and only if θ = 180°/N for some integer N ≥ 2, i.e. iff 180/θ ∈ ℤ.**

*Verification of the answer on the discriminating value θ = 72°:* 180/72 = 2.5 ∉ ℤ, so θ = 72° is a
losing value. Indeed T₀ = (36°, 36°, 108°) ∈ S (36 = θ/2 is not a multiple of 72; 108 = 1.5·72 is
not an integer multiple), and by the Closure Lemma Shan-Yu survives forever — matching the claim.
For θ = 90° (N = 2), 60° (N = 3), 45° (N = 4), 36° (N = 5), 30° (N = 6): 180/θ ∈ ℤ, all winning, as
Part B constructs. ∎

## Promotable lemmas

- **Closure Lemma (safe-set invariance).** *Fix θ with 180/θ ∉ ℤ and let
  S = {triangles no angle of which is a positive integer multiple of θ}. If T ∈ S then every cevian
  cut of T (from any vertex to any interior point of the opposite side) has at least one child in S.*
  Proved in full in Part A.2 by the exhaustive four-case supplementary-multiple analysis
  (both children non-safe ⟹ a parent angle is a multiple of θ, or 180° = (n+m)θ ⟹ 180/θ ∈ ℤ —
  both impossible). Reusable by any approach for the impossibility direction. Written to
  `results/imo-2026-04/lemmas/closure-lemma.md`.
- **Both-multiples cut.** *If θ = 180°/N (N ≥ 3) and T has no angle θ, then cutting the largest
  vertex A (which satisfies A > θ) with A₁ = A + C − nθ, where n = ⌊C/θ⌋ + 1, yields two genuine
  children with apex angles nθ and (N − n)θ — both positive integer multiples of θ.* Proved in
  Part B.2, Phase 1.
- **Descent Lemma.** *If T has an angle jθ (2 ≤ j ≤ N − 1, θ = 180°/N), cutting that vertex with
  A₁ = θ gives a child with angle θ (Child 1) and a child with angle (j − 1)θ (Child 2); when j = 2
  both children have angle θ, forcing a win.* Proved in Part B.2, Phase 2.
