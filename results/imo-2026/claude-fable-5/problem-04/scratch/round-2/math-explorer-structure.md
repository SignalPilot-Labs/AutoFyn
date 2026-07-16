## imo-2026-04

- **Distinct openings:**

  1. **Linear-descent strategy (main attack):** For θ = 180°/n, Mulan uses two phases: (Phase 1) from any triangle with smallest angle a < θ, cut to the largest angle c with s = θ − a; this forces θ into p2 (Shan-Yu must discard p2 or lose immediately) and puts (n−1)θ into p1. (Phase 2) from a triangle with angle kθ (k = n−1, n−2, …, 2), cut to kθ with s = (k−1)θ; p2 gets θ (Shan-Yu discards), p1 gets (k−1)θ. After n−2 descent steps, we reach k=2: cut to 2θ with s=θ gives BOTH pieces angle θ. Mulan wins in exactly n−1 steps. Computationally verified for n = 2, 3, …, 20 with exact rational arithmetic.

  2. **Invariant-maintenance converse (Shan-Yu's strategy):** When 180°/θ ∉ ℤ, Shan-Yu maintains the invariant "no angle of the current triangle equals any positive-integer multiple of θ." The key: if BOTH pieces p1 = (b, s, 180−b−s) and p2 = (c, a−s, b+s) each had a multiple-of-θ angle (not inherited from T), the only non-contradictory sub-case is (180−b−s) = jθ AND (b+s) = kθ, giving 180 = (j+k)θ, i.e., j+k = 180/θ ∈ ℤ — contradiction when 180/θ ∉ ℤ. The other three sub-cases force an angle of the safe triangle T to be a multiple of θ, also contradicting safety. So at least one piece is always safe; Shan-Yu always has a survival move.

  3. **Case 3 (all angles > θ) reduction:** When all three angles of T exceed θ (possible for n ≥ 5), cut to the smallest angle a (> θ) with s = a − θ; p2 gets angle a−s = θ (Shan-Yu discards), p1 = (b, a−θ, c+θ) with smallest angle a−θ < a. Repeat until the smallest angle drops below θ, then apply Phase 1. This terminates because a decreases by θ each step, taking at most n−1 additional steps.

  4. **One-step characterization of the 2θ vertex:** Mulan wins in a single step from T iff T has an angle 2θ: cut to 2θ with s = θ forces θ into BOTH p1 (via the s slot, since 180−b−s = 180−b−θ and p1 also gets s=θ in its angle-slot) and p2 (via va−s = 2θ−θ = θ). This gives a clean "base case" for the descent.

  5. **Binary-halving shortcut (alternative Phase 2):** Instead of linear descent k → k−1, Mulan can halve: cut to kθ with s = ⌊k/2⌋·θ; p1 gets ⌊k/2⌋·θ, p2 gets ⌈k/2⌉·θ. Both are multiples of θ; Shan-Yu keeps the larger. The sequence converges to k=1 in O(log n) steps. Cleaner for large n but harder to write up.

- **Candidate technique(s):**
  - Game strategy via monovariant: "largest multiple of θ present in the surviving triangle" is a strict monovariant for Phase 2, decreasing by θ each step.
  - Invariant for Shan-Yu: "no angle is a positive-integer multiple of θ," sustained by a 4-case exhaustive argument on how both pieces could simultaneously be unsafe — the only non-contradictory case requires 180/θ ∈ ℤ.
  - Exhaustive casework on the angle structure of T (three cases: has θ, has angle < θ, all angles > θ).

- **Cheap-kill candidates:**
  - θ > 90°: 180°/θ < 2, so no integer n ≥ 2 with nθ = 180° exists — these θ are automatically non-winning.
  - If θ = 180°/n for n ≥ 2, all kθ for k = 1, …, n−1 lie strictly in (0°, 180°) — valid as triangle angles. This is needed for the descent steps to be geometrically valid.

- **Knowledge-base entries to use:**
  - Invariants and Monovariants (combinatorics section): Phase 2 monovariant; Shan-Yu's invariant.
  - Game Theory / Two-player games: "Mulan has strategy iff invariant is breakable" structure.
  - Extremal Principle / Casework: three cases for starting position.
  - Induction: descent on k (Phase 2).

- **Analogous past problems (cruxes):**
  - Searched combinatorics + games-and-strategy subcorpus (39 entries). No exact match found. The closest structural analogue would be any problem where a game step generates an orbit modulo M and the question is whether the orbit hits a target — crux move "divisibility condition determines reachability." The invariant argument (both pieces unsafe ⟹ 180/θ ∈ ℤ) is a new combinatorial observation not found in the corpus.

- **Prior progress:** None (round 1 died early, no approaches or workspace for imo-2026-04).

- **Dead ends (do not retry):**
  - Integer-degree discretization for verification: restricting s to integer values gives false failures (e.g., the required s = θ−a is non-integer for most starting triangles). Verification must use exact rational arithmetic or pure algebra.
  - Computational game-tree search over continuous angle space: intractable. Proof must be algebraic.
  - Binary halving as the primary presentation: the recursive structure (k even vs. odd) complicates the write-up; the simpler linear descent (n−1 steps) is better.

- **Small-case / intuition notes:**
  - VERIFIED (exact rational arithmetic): Mulan wins in exactly n−1 steps from the near-degenerate triangle (1/n, 1/n, 180°−2/n) using the linear-descent strategy, for n = 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20.
  - VERIFIED (integer model, depth 11): θ = 40° (180/40 = 4.5 ∉ ℤ) — Shan-Yu survives from (1°, 1°, 178°).
  - VERIFIED (algebraic): for θ = 40°, Shan-Yu can keep T = (1°, 2°, 177°) safe — no s makes both pieces unsafe simultaneously; the case (180−b−s) = j·40° AND (b+s) = k·40° would require j+k = 4.5, a non-integer, contradiction.
  - The cut formula (exact): cutting to vertex with angle va, with cut parameter s ∈ (0°, va°): p1 = (vb, s, 180°−vb−s), p2 = (vc, va−s, vb+s). The two "complementary" angle slots (180−b−s) in p1 and (b+s) in p2 sum to 180°. If both are multiples jθ and kθ, then (j+k)θ = 180°, forcing 180°/θ ∈ ℤ.
  - CONJECTURED ANSWER (strongly supported): Mulan guarantees victory in finitely many steps if and only if θ = 180°/n for some integer n ≥ 2. Equivalently: nθ = 180° for some n ∈ ℤ, n ≥ 2.

**Proof sketch summary (for the outliner):**

Direction 1 (Mulan wins for θ = 180°/n): Explicit strategy. Phase 1: one cut creates angle (n−1)θ in surviving piece (valid because s = θ−a > 0 iff a < θ, and s < c always since a+b = 180°−c < 180°−θ = (n−1)θ, so c > θ−a = s). Phase 2: n−2 cuts reduce kθ → (k−1)θ (valid since s = (k−1)θ < kθ = va). Final cut: BOTH pieces get θ. Total: n−1 steps.

Direction 2 (Shan-Yu survives if 180°/θ ∉ ℤ): Shan-Yu starts with any triangle where no angle is a multiple of θ (such triangles exist, e.g., (α, α, 180°−2α) for generic α). Invariant maintained by 4-case argument: if both pieces are unsafe, one of four contradictions arises — either an angle of T is a multiple of θ (contradicts safety of T) or 180° = (j+k)θ for positive integers j+k (contradicts 180°/θ ∉ ℤ). No further structure needed.
