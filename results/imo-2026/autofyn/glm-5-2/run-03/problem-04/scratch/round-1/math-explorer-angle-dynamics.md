## imo-2026-04 (lens: angle-dynamics & invariant analysis)

### Distinct openings (each a different attack the outliner could build into a rival approach)

1. **Acute-strategy upper bound (necessity, θ > 90°).** Prove Mulan loses for θ > 90° by giving Shan-Yu a monovariant strategy: start with an acute triangle, and after every Mulan cut keep the acute (or right) successor. From an all-acute state (a,b,c < 90), cut to vertex a, φ ∈ (0,a): S1 = (φ, b, 180−b−φ), S2 = (a−φ, c, b+φ). S1's third angle > 90 ⇔ φ < 90−b; S2's third angle > 90 ⇔ φ > 90−b. These are *complementary* conditions, so for every φ at most one successor is obtuse (at φ = 90−b both are right). So Shan-Yu can always keep a non-obtuse successor; the state stays in {acute} ∪ {right}; no angle ever exceeds 90°, hence θ > 90° never appears. This is a clean, rigorous necessity direction. (Verified: θ ∈ {91,92,95,100,120,150,179} all lose in both integer- and half-degree solvers — only the base-case states containing θ are winning.)

2. **The 90°-trick (one-step force from any state).** For θ = 90°, Mulan wins in one step from *any* triangle: any triangle has at least two angles < 90° (at most one angle ≥ 90°). Cut to the third vertex (angle a), set φ = 90 − b where b is one of the two < 90° angles. Then S1 = (90−b, b, 90), S2 = (a−90+b, c, 90) — both contain 90°. So θ = 90° is the sharp boundary and is winning. (The trick needs b < 90 and c < 90; both hold for any non-degenerate triangle by pigeonhole on the sum 180°.) This is both the sufficiency base case and the key "residue-breaking" move for general θ.

3. **Transfer move = Euclidean-algorithm / residue-invariant structure (sufficiency machinery).** From state (a,b,c), if a > θ, Mulan cuts to vertex a with φ = a − θ. Then S2 = (θ, c, b+a−θ) contains θ, so Shan-Yu is *forced* to keep S1 = (a−θ, b, c+θ). This is a **deterministic forced transition** (a,b,c) → (a−θ, b, c+θ): Mulan subtracts θ from one angle and adds θ to another. By cyclically choosing the cut vertex she can transfer θ from any angle > θ to any other angle. **Invariant**: each angle's value mod θ is preserved by transfers. So transfers alone reach θ only if some initial angle is ≡ 0 mod θ — which Shan-Yu will avoid. Sufficiency therefore cannot rest on transfers alone; it needs a move that *breaks* the mod-θ residue invariant.

4. **Bisection move (2θ-sink).** From a state containing angle 2θ, cut to that vertex with φ = θ: both successors = (θ, *, *) contain θ → win. So any state with an angle = 2θ is a one-step win. Iterating: states with angle 2^k·θ are k-step wins (need 2^k·θ ≤ 178). But Shan-Yu controls the initial triangle, so this is a *target*, not a strategy — Mulan must *drive* an angle to 2θ.

5. **Combined sufficiency (the real crux for the outliner).** The natural sufficiency recipe: (i) use the 90°-trick to plant a 90° angle (residue 90 mod θ, regardless of initial residues — this is the residue-breaker); (ii) from the right triangle (90, x, 90−x), run transfers (Euclidean algorithm) to reduce the 90° angle modulo θ down to r = (90 mod θ); (iii) when θ | 90 this already lands on θ → win; (iv) for general θ ≤ 90 the residues interact and Mulan must combine bisection / a second 90-trick-flavored move to escape the residue trap. **This residue-escape step is the open crux** — the half-degree solver confirms it always succeeds for θ ≤ 90 (every state, including nasty ones like (2,2,176) for θ = 89, is winning), but the explicit constructive strategy for arbitrary θ < 90 (non-divisor of 90) is what the outliner must design. Candidate sub-lemmas: (a) Mulan can force the *smallest* angle to strictly decrease via transfers until it is < θ, then use bisection on a larger angle to create a fresh 90°-trick target; (b) a potential/monovariant argument showing repeated {90-trick, transfer} drives some angle to exactly θ.

6. **Invariant / monovariant hunt (alternative framing).** Look for a real-valued potential F(a,b,c) that Mulan can force strictly downward (toward a level set containing θ) regardless of Shan-Yu's choice — e.g. min distance from {a,b,c} to θ, or the minimum angle. The transfer move monotonically decreases the chosen angle; the 90-trick resets a residue. A Lyapunov-style proof may close sufficiency without exhibiting the exact strategy.

### Candidate technique(s)
- **Invariants & monovariants** (knowledge_base "Combinatorics / General Proof Methods"): the acute-strategy is a Shan-Yu monovariant ("state stays acute"); the transfer is a Mulan monovariant on the chosen angle.
- **Euclidean algorithm / modular residues**: transfers preserve each angle mod θ — the central obstruction and the reason the 90-trick (which produces residue 90 mod θ fresh) is load-bearing.
- **Game-graph closure / attractor computation**: W = least set with (state contains θ) ∪ (∃ move both successors ∈ W); want W = all states. This is the formal scaffold for a sufficiency induction.

### Cheap-kill candidates
- **The 90°-trick itself is a one-move structural kill** for θ = 90° and for any state with two angles < 90° (always true) — proves the boundary case instantly.
- **Parity/residue pigeonhole on the sum**: a+b+c = 180 and each move preserves the sum; combined with "at most one angle ≥ 90°" this gives the acute-strategy upper bound in three lines. Try this before any heavy construction.
- **Transfer-forcing injection**: φ = a−θ is the single φ value that makes the move deterministic; identifying it prunes the continuous move-space to a discrete Euclidean-algorithm skeleton.

### Knowledge-base entries to use
- "Invariants & monovariants" (Combinatorics) — for the acute strategy and the transfer residue invariant.
- "Invariant / monovariant" (General Proof Methods) — same.
- "Pigeonhole / extremal" — "at least two angles < 90°" is a pigeonhole on the 180° sum.
- "Contradiction / construct examples" (General Proof Methods) — necessity needs Shan-Yu construction (acute triangle); sufficiency needs Mulan construction.
- "Find a related/analogous problem" / "Reformulate" (Pólya) — reformulate the move as an operation on the angle *multiset* (transfer θ between entries), turning a geometry game into a combinatorial number game.

### Analogous past problems (cruxes)
- **aimo-0236** (token game; crux: "two-phase invariant, first-mover carries a valuation witness one step ahead" + "to prove termination, find a regime where one move fixes valuations while the other's forced move strictly decreases a potential"). Analogous because the transfer move is a forced (Shan-Yu has no choice) potential-decrease, and the residue invariant is a two-phase quantity Mulan nurses while Shan-Yu degrades a different one. The acute-strategy is the dual "Shan-Yu nurses acuteness."
- **aimo-0225** (regular n-gon game; crux: "determine game value by recursing on the 2-adic valuation of a difference that exactly halves at each step, so P/N flips with each halving"). Analogous to the bisection move (φ = a/2) and the 2θ → θ halving sink; the Euclidean-algorithm structure of transfers is a generalized (non-dyadic) halving.
- **aimo-0262** (Cinderella/Stepmother buckets; crux: "self-reproducing invariant family of configurations, each legal move can restore it"). Analogous to Shan-Yu's acute-strategy: the family "acute triangles" is self-reproducing under Shan-Yu's reply (every Mulan cut leaves an acute successor he can keep).
- No exact geometric-triangle-game crux exists in the corpus (geometry cruxes not extracted); the closest analogies are these invariant/valuation games. Do not force a geometric match.

### Prior progress
None in the workspace (round 1; `current.md` Status unsolved, no approaches, no lemmas).

### Dead ends (do not retry)
- **Integer-degree discretization of the game grid.** A first scan (integer angles, n_phi = 120–500) showed a spurious pattern where odd θ ∈ {47,49,53,57,61,63,…,89} appeared to LOSE while even θ ≤ 90 won. This is a **discretization artifact**, not a real loss: integer-degree snapping makes odd-θ targets systematically unreachable by the rational φ-grid. Half-degree resolution (which makes 2θ even-count for integer θ) flips ALL of 45,47,49,51,53,55,57,59,61,63,75,85,89 to WIN. Do not trust any parity-flavored "θ must be even" conjecture — it is false. The true boundary is θ = 90°.
- **Hand-analyzing single states as losing** (e.g. I traced (2,2,176) for θ = 89 and thought it sat in a closed losing cycle {(2,2,176),(2,87,91),(2,2,91)}). The half-degree solver refutes this: (2,2,176) for θ = 89 is in fact WINNING via forcing moves my hand-analysis missed (the continuous φ-space has productive values outside the obvious φ ∈ {a−θ, θ, a/2}). Do not conclude a state is losing from inspecting only φ = a−θ, θ, a/2.

### Small-case / intuition notes (all CONJECTURES unless labeled proved)
- **PROVED**: θ > 90° losing (acute strategy, opening 1). θ = 90° winning (90-trick, opening 2).
- **CONJECTURE (strong numerical support)**: 0° < θ ≤ 90° winning for Mulan. Verified by half-degree attractor computation: every tested θ ∈ {45,47,49,51,53,55,57,59,61,63,75,85,89,90} has W = all 10800 states; θ > 90 has W = base-case-only.
- **CONJECTURE**: the sufficiency goes via the 90-trick (plant residue 90 mod θ) followed by an angle-Euclidean-algorithm using transfers, with a residue-escape sub-step (bisection on a 2θ-reachable angle, or a second 90-trick-equivalent) to handle non-divisors of 90. The explicit construction for general θ < 90 is the open task.
- Numerical witness: even nasty initial states win — (1,1,178) for θ ∈ {30,50,60,89}; (2,2,176) for θ = 89. So Shan-Yu has no losing-for-Mulan starting triangle when θ ≤ 90.
- Boundary sharpness: θ = 90 wins (proved); θ = 91 loses (proved via acute strategy). The set of winning θ is exactly the half-open interval (0°, 90°] — the outliner's job is the sufficiency proof for θ < 90°.
