## imo-2026-04 — Mulan's triangle game (retrieval route)

### Distinct openings (each a different attack the outliner could build into a rival approach)

1. **Game-tree fixpoint / AND-OR characterization.** Define W = set of triangles from which Mulan can force a win. (A,B,C) ∈ W iff some angle = θ, OR ∃ a cut (vertex V, split α) such that BOTH children ∈ W. Mulan guarantees victory from every start iff W = all triangles. This is the formal workhorse; the BFS below solves it on discrete grids. The outliner can run this game recursion symbolically on the N-torsion cosets.

2. **Mod-θ invariant + supplementary-at-P defense (Shan-Yu side).** The two angles created at the cut point P are supplementary (sum to 180°). If 180 mod θ ≠ 0 (i.e., 180°/θ ∉ ℤ), then for any k, 180° − kθ ≡ 180 mod θ ≠ 0 mod θ, so AT MOST ONE child carries a multiple-of-θ angle at P. This asymmetry is the seed of Shan-Yu's defense. The invariant to maintain is "no angle of T is a multiple of θ" (a stronger condition than "no angle = θ", hence a valid defense). This directly proves the "only if 180°/θ ∈ ℤ" direction.

3. **Torsion / subgroup structure of the circle T = ℝ/180°ℤ.** Angles live in T; A+B+C = 0 in T. The cut keeps the B-side child with angles (α, B, −B−α) in T (where −B−α = A+C−α). The subgroup G = ⟨angles⟩ ⊂ T evolves as G → ⟨α, B⟩ (Mulan chooses α freely). For θ = 180°/N, θ is N-torsion. Forcing "an angle ≡ 0 mod θ" is the natural subgroup target; "angle = θ exactly" is subtler (excludes 2θ, 3θ, …). The torsion lens separates the 180|θN structure cleanly.

4. **Perpendicular / angle-bisector anchor + inductive doubling.** Universal anchor: from ANY triangle Mulan can force 90° in one cut (drop the perpendicular from the vertex opposite the longest side; both children get a 90° angle at the foot — always available since at least one altitude foot lies on its opposite side). Bisecting an angle 2θ (θ<90°) gives θ in both children. This proves θ = 180°/2^k directly. But the full answer needs more (odd N), so this is only one prong of the winning strategy.

5. **Recursive forcing on the doubling chain θ → 2θ → 4θ → … → 90°.** At the WINNING cut, both children must contain θ (Shan-Yu is adversarial). Classifying "both children contain θ" yields exactly two configurations: (a) θ = 90° (perpendicular, any triangle), or (b) current triangle has an angle = 2θ with θ < 90° (bisect it). So a one-step force requires angle 2θ present; recursively, force θ iff the chain θ, 2θ, 4θ, …, 90° closes. This ALONE gives only dyadic θ = 180°/2^k — too sparse — so it is necessary but not sufficient. The genuine answer is richer; the bisector anchor is one piece.

### Candidate technique(s)

- **AND-OR game fixpoint on a torsion-coset discretization** (the workhorse; matches the BFS that produced the conjecture).
- **Subgroup / mod-θ invariant for the lower-bound (defense) direction** — clean and likely complete.
- **Inductive construction on N = 180°/θ** for the upper-bound (Mulan strategy) direction; base N=2 perpendicular; inductive step still needs a real idea for odd N (the BFS shows max depth 2 for θ=60°, so the construction is short, but it is NOT just bisect-2θ).
- **L1-norm monovariant on integer coefficient vectors** (transferred from aimo-0440) — potentially the engine for the odd-N inductive step.

### Cheap-kill candidates

- **The mod-θ supplementary-at-P observation** is a one-line structural kill for the defense direction (θ ≠ 180°/N). Cheap, rigorous, do this first.
- **Perpendicular anchor (θ=90° in one step from any triangle)** is a one-move cheap kill for the base case.
- **"Both children contain θ" classification** (only θ=90° or angle-2θ-present) is a one-move pruning of the final-step configurations; cheap and narrows the recursion.

### Knowledge-base entries to use

- **Invariants & monovariants** (Combinatorics section) — the mod-θ invariant and any monovariant on coefficient vectors.
- **Piecewise-concavity smoothing** — *probably not relevant*; the objective here is discrete/torsion, not a sinusoidal sum. Skip unless an analytic bound on angle triples is needed.
- **Three-gap / Steinhaus theorem** (Number Theory section) — *tangential*; the insertion corollary (largest gap non-increasing under splitting) is spiritually related to "splitting an angle preserves a measure", but the Mulan game lacks the Kronecker-sequence structure. Mention as a loose cousin, not a load-bearing tool.
- **Kronecker / Weyl equidistribution** — relevant only if the answer involved irrational θ; the conjectured answer is purely rational-torsion, so this is likely a red herring. Skip.
- **Sylvester–Gallai** (Combinatorial Geometry) — *not relevant*; no ordinary-line structure.
- **General Proof Methods: invariant/monovariant, induction, casework** — directly applicable.
- **Pólya heuristics: solve a simpler/special case first, work backward** — the N=2,3,4 cases should be worked out explicitly before the general N argument.

The KB does NOT have an explicit "Euclidean algorithm on angles" or "Stern-Brocot on angle triples" entry, nor a "combinatorial game theory / partisan game" entry. The closest engine is the **invariant/monovariant** entry plus the **general induction/descent** meta-strategy. The aimo-0440 crux (below) supplies the missing "integer-coefficient L1 monovariant" technique by transfer.

### Analogous past problems (cruxes)

**BEST FIT — `aimo-0440`** (number_theory, subtopics: divisibility-and-gcd / size-bounding-and-descent). Three nonnegative reals r₁,r₂,r₃ with a nontrivial integer relation a₁r₁+a₂r₂+a₃r₃=0 sit on a blackboard. Operation: replace y by y−x for x≤y. Prove a zero is reachable in finitely many steps. **Crux move**: track the auxiliary integer relation alongside the visible state; the subtraction r_i ← r_i − r_j rewrites the coefficient vector, and choosing the pair so that |a_i+a_j| < |a_j| makes the L1 norm |a₁|+|a₂|+|a₃| strictly decrease; integrality forces bottoming at a zero coordinate, reducing to two numbers where the Euclidean algorithm finishes. **Why it transfers**: imo-2026-04 is ALSO a subtractive/Euclidean-flavored operation on a triple carrying an integer relation (A+B+C = 180°, i.e., coefficients (1,1,1) with relation-value 180°); the "track an integer coefficient vector, descend on L1 norm" engine is the leading candidate for the odd-N inductive step where the bisector anchor alone is insufficient. **Fit honesty**: the operations differ (aimo-0440 is deterministic subtractive; imo-2026-04 has Mulan-chooses-α + Shan-Yu-discards, an adversarial game), and aimo-0440 has a single pre-existing integer relation whereas imo-2026-04 manufactures the torsion condition 180° = Nθ. Transfer the *monovariant-on-coefficients* idea, not the proof verbatim.

**SECOND FIT — `aimo-0225`** (combinatorics, games-and-strategy / bijections-and-encoding). Game on a regular n-gon: three counters, slide one without jumping, area must strictly increase; classify n for first-player win. **Crux move**: encode position by the multiset of three arc-lengths {a,b,c} (a+b+c=n); translate "area increases" into "replace two arcs by same-sum numbers strictly increasing the min of the pair"; recurse on v₂ of the halved difference, P/N flips each halving, start (1,1,n−2) is a Win iff v₂(n−3) is odd. **Why it transfers**: it is a triangle-game with an adversarial winning condition, encoded as arithmetic on a triple of arc-lengths summing to a constant — the same shape as imo-2026-04's angle triple (A,B,C) with A+B+C=180°. The "encode geometric move as multiset operation on a summing-to-constant triple, then 2-adic descent" pattern is directly portable. **Fit honesty**: aimo-0225 is turn-based symmetric (both players slide), imo-2026-04 is asymmetric (Mulan cuts, Shan-Yu discards); and aimo-0225's v₂ answer is specific to its area-increase predicate. The 2-adic flavor matches the dyadic anchor of imo-2026-04, but the FULL answer (all N≥2, not just powers of 2) shows the analogy is partial.

**No other crux in the corpus is genuinely close.** I searched combinatorics subtopics {games-and-strategy, invariants-and-monovariants, processes-and-algorithms, extremal-principle, pigeonhole} for keywords {triangle, angle, polygon, cut, split, perimeter, vertex, paper, fold}, and number-theory / algebra for {euclid, stern, continued fraction, modular group, folding}. The other geometry-game cruxes (aimo-0050 hidden-config, aimo-0060 spiral-similarity, aimo-0160 rotations, aimo-0542 line-flips) do not share the "triple-with-relation under subtractive/splitting operation" structure. No crux in the corpus addresses "angle Euclidean algorithm" or "reachable angles under adversarial pruning" directly — this is genuinely a gap the outliner must fill.

### Prior progress

Round 1 — no approaches registered yet (Elo pool empty, Status `unsolved`). This report is the first scouting pass. No prior claims to verify.

### Dead ends (do not retry)

- **"θ = 180°/2^k only" (dyadic-only conjecture)** — FALSIFIED by numerical BFS. θ = 60°, 30°, 36°, 20°, 18°, 15°, 10°, 9°, … (all non-dyadic) are also universal wins. Do not restrict to powers of 2.
- **"θ is any rational multiple of 180°" (dense rational conjecture)** — FALSIFIED. θ = 2·180°/5 = 72°, 2·180°/7 ≈ 51.4°, 2·180°/9 = 40°, 3·180°/7 ≈ 77.1°, 2·180°/11, 2·180°/13 all LOSE on every grid tested. Only unit fractions p/q with p=1 win.
- **"Symmetric in θ ↔ 180°−θ"** — FALSE. θ=60° wins, θ=120° loses; θ=45° wins, θ=135° loses; θ=30° wins, θ=150° loses. Only θ=90° is self-dual. The game is NOT symmetric under θ ↦ 180°−θ.
- **Treating this as a pure geometry problem** — the synthetic-geometry toolkit (power of a point, radical axes, Ptolemy, Miquel, etc.) does not engage; this is a combinatorial-game / number-theory problem dressed in triangle language. Do not pursue synthetic-geometry approaches.

### Small-case / intuition notes (CONJECTURE, labeled as such)

**Leading conjecture (strongly supported, NOT proven):**
> Mulan guarantees victory in finitely many steps **iff θ = 180°/N for some integer N ≥ 2**.
> Equivalently, 180°/θ is an integer ≥ 2; equivalently, θ ∈ {90°, 60°, 45°, 36°, 30°, 180°/7, 22.5°, 20°, 18°, …} (unit fractions of 180°).

**Numeric evidence (computational, conjecture-grade — NOT a proof):**

- **Full integer-degree scan (θ=1..179):** universal-win set = {1,2,3,4,5,6,9,10,12,15,18,20,30,36,45,60,90} = {180/d : d | 180} (exactly the divisors of 180). No other integer θ wins.
- **Extended to non-integer θ = 180°/N for N=2..30** (multiple grid scalings K=1,3,5, units = 180°/(N·K)): EVERY N is a universal win, including N=7,8,11,13,14,16,17,19,20,21,24,30 (non-divisors of 180). Confirms the answer is "all N≥2", not "divisors of 180".
- **Converse check:** θ = p·180°/N for p≥2 (with p/N not reducing to 1/M) LOSES on every grid tested: 2/5, 3/5, 2/7, 3/7, 2/9, 3/11, 2/11, 2/13, 3/13, 2/3 (=120°), 3/4 (=135°), 2/5 (=72°), 2/9 (=40°). The fractions that reduce to 1/M (e.g., 2/8 = 1/4 → 45°, 3/9 = 1/3 → 60°) win, as expected.
- **Winning depth is small:** for θ=60° (N=3), the maximum number of cuts Mulan needs from any integer-grid triangle is **2**. For θ=90° (N=2) it is **1**. So the strategy is short, not a long descent.

**Theorem the proof would rest on (conjectural assembly):**
- **Defense (only-if direction):** the mod-θ invariant. If 180°/θ ∉ ℤ, write 180° = qθ + r, 0 < r < θ. Shan-Yu maintains "no angle of T is a multiple of θ". The supplementary-angle-at-P fact (the two new angles at the cut point sum to 180° = qθ+r, so at most one is a multiple of θ) plus a check at the cutting vertex V gives Shan-Yu a discarding strategy. This is the load-bearing idea; the outliner must verify the vertex-V case rigorously (it is where the invariant is most fragile).
- **Winning (if direction, θ = 180°/N):** perpendicular anchor for N=2; for general N the technique is NOT just bisector-doubling (which only covers powers of 2). The actual engine for odd N is the open question for the outliner. The most promising transferable tool is the **L1-norm monovariant on integer coefficient vectors** from `aimo-0440`: track an integer linear relation among the angles modulo 180°/N, descend on |a₁|+|a₂|+|a₃|, force a coordinate to zero (i.e., an angle ≡ 0 mod 180°/N), then refine "≡ 0 mod θ" down to "= θ exactly". The BFS shows this descent terminates in ≤2 steps for N=3, so the construction is short.

**Angle-group structure note (for the outliner):** the operation on the angle triple is — in the circle group T = ℝ/180°ℤ — `(A, B, C) → (α, B, −B−α)` (B-side kept) or `(A−α, C, B+α)` (C-side kept), where α is Mulan's free choice. The subgroup generated by the kept triple is `⟨α, B⟩` (B-side) or `⟨A−α, C⟩` (C-side). Mulan can place any element she wants into the new subgroup, but the actual *angles* of the kept triangle are constrained by Shan-Yu's choice. The corpus has NO entry on "which targets are reachable under adversarial pruning of a subtractive/splitting operation on a torsion group" — the outliner builds this from scratch, leaning on the mod-θ supplementary-at-P fact (defense) and the aimo-0440 monovariant (offense).
