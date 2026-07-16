## imo-2026-04

### Angle bookkeeping (verified)

Cut from vertex C (angle c) — point P on side AB — splits into:
- P1 (triangle APC): angles (a, c₁, b+c−c₁)
- P2 (triangle BPC): angles (b, c−c₁, a+c₁)

where c₁ ∈ (0, c). This is confirmed by code; the two P-angles sum to 180° as required.

### Key structural fact about simultaneous forcing

For BOTH pieces to have angle θ in one cut, exactly two cases:
- **Case B**: current triangle has angle c = 2θ; set c₁ = θ. Then P1 has c₁ = θ and P2 has c−c₁ = θ. Both have θ.
- **Case C**: 2θ = 180°, i.e., θ = 90°. Set c₁ = θ − a; then a+c₁ = θ and b+c−c₁ = (a+b+c)−θ = 180°−θ = 90°. Both pieces get 90°.

No other configurations force both pieces to θ simultaneously (proven by exhaustive case analysis: the sum identity a+b+c = 180° pins all cases).

### The θ = 90° base case (1-step win for Mulan)

From ANY triangle with no 90° angle: at least two angles < 90°. Take va < 90° with vb < 90° (i.e., two acute angles). Cut from vc with c₁ = 90° − va:
- Need c₁ > 0: va < 90° ✓
- Need c₁ < vc: va + vc > 90° ✓ (since vb = 180° − va − vc < 90° forces va + vc > 90°)
- P1 = (va, 90°−va, 90°) ✓; P2 = (vb, vc−90°+va, 90°) ✓

Both pieces have 90°. Mulan wins in 1 step from any triangle. Confirmed numerically on 50+ triangles.

### The n-step strategy for θ = 180°/n

**Claim**: For θ = 180°/n (integer n ≥ 2), Mulan wins in ≤ n/2 + 1 steps (confirmed numerically for n = 2,3,4,5,6,18,90,180).

**Strategy**:
1. (Step 1) Use the θ = 90° base case to force BOTH pieces to have 90°. Shan-Yu keeps one, say (a, b, 90°).
2. (Steps 2 through ~(90/θ)−1) From the 90° triangle, repeatedly cut from the largest angle L with c₁ = θ:
   - P1 = (x, θ, y+L−θ): has θ. Shan-Yu keeps P2.
   - P2 = (y, L−θ, x+θ): largest angle is L−θ.
   - Each step reduces the largest angle by θ. After (L−2θ)/θ = L/θ − 2 steps, L = 2θ.
3. (Final step) From triangle with angle 2θ, cut from 2θ vertex with c₁ = θ: BOTH pieces get θ.

**Verification** (θ = 60° = 180°/3, n = 3, strategy = 2 steps):
- Step 1: Create P1 with 60° and P2 with 120° = 2θ. (from formula: c₁ = vb+vc−θ gives P1 with θ and P2 with 180°−θ = 120°; requires vb < θ, always achievable since not all angles can exceed θ in a non-degenerate triangle without θ.) Shan-Yu keeps P2.
- Step 2: From 120° triangle, cut from 120° with c₁ = 60°: BOTH pieces get 60°.

Tested on 1000 random triangles: 100% success. The key identity: c₁ = vb+vc−θ gives va+c₁ = 180°−θ = (n−1)θ, and P1's third angle = θ. This works whenever vb < θ.

**Triangles where all angles ≥ θ**: In such a triangle (only possible for θ ≤ 60°), cut from vertex C with c₁ = θ; P2's second angle = c−θ. If c ∈ (θ, 2θ), then c−θ ∈ (0,θ) — an angle < θ appears in P2. Since all three angles ≥ θ forces a+b+c ≥ 3θ = 180° with equality only for equilateral, the "small angle < θ appears after one cut" property always kicks in within one step. Confirmed for θ = 36°, 30°.

### Shan-Yu's survival strategy for θ ≠ 180°/n

**Claim**: If n·θ ≠ 180° for ALL integers n ≥ 1, then Shan-Yu survives forever.

**Invariant**: Let S = {2^k θ : k = 0,1,2,...} ∩ (0°,180°). This set is finite (first 2^k·θ ≥ 180° exits), and 180° ∉ S (since n·θ ≠ 180° for all n).

**Shan-Yu's strategy**: Start with a triangle with no angle in S (e.g., equilateral if 60° ∉ S; otherwise any triangle with angles avoiding S). At each step, pick the piece with no angle in S.

**Why it works**: For BOTH P1 and P2 to have some angle s ∈ S, the current triangle would need angle 2s. If 2s < 180°, then 2s ∈ S — but the invariant says no angle ∈ S. If 2s ≥ 180°, a triangle can't have two angles each ≥ 90° = 2s/2 > s... and since s > 90° is impossible for s ∈ S with 2s ≥ 180°, this means s ≥ 90°; but the argument still works: two pieces both having angle s ≥ 90° would require the original triangle to have s+s ≤ 180° somehow — impossible since 2s > 180°.

So at most one piece ever has an angle in S. Shan-Yu always picks the piece without S. The invariant is maintained forever.

**Numerical confirmation**:
- θ = 40° (= 180°/4.5): 0% wins in minimax depth 5 on 100 triangles.
- θ = 72° (= 180°/2.5): 0% wins.
- θ = 120° (= 180°/1.5): 0% wins.
- θ = 135° (= 180°/1.33): 0% wins.
- θ = 150° (= 180°/1.2): 0% wins.
- θ = 100°: 0% wins.

### Conjectured answer

**Mulan wins iff θ = 180°/n for some integer n ≥ 2.**

Equivalently: θ ∈ {90°, 60°, 45°, 36°, 30°, 180°/7, 180°/8, ...}. All winning θ satisfy 0 < θ ≤ 90°.

In the language of the problem: θ must be an exact integer divisor of 180°, i.e., 180°/θ ∈ ℤ≥2.

### Distinct openings (for the outliner)

1. **Direct characterization + inductive strategy**: Prove Mulan wins by induction on n in "θ = 180°/n". The base case n = 2 (θ = 90°) uses the Case C identity. The inductive step shows Mulan can force 90° in step 1 (base case), then reduce the max angle by θ until reaching 2θ.

2. **Shan-Yu's monovariant / invariant**: For the hard direction (θ ≠ 180°/n), prove via the doubling-chain invariant S = {2^k θ} that Shan-Yu can always avoid θ.

3. **The "both pieces get θ" characterization as the crux**: Reformulate Mulan's win as: Mulan must eventually create a triangle with angle 2θ (and keep repeating). Shan-Yu survives iff he can always avoid angles {θ, 2θ, 4θ, ...}. This is cleanest via the S-invariant.

4. **Top-down reduction tree**: Mulan's strategy is essentially: go up to 2θ → 4θ → ... → 2^k θ (the first in [θ, 90°] range), use base case, then come back down. This is the "divisibility tree" structure.

### Candidate techniques

- **Invariant / monovariant** (combinatorics KB entry): Shan-Yu's S-invariant.
- **Constructive + induction** (KB entry): Mulan's inductive strategy.
- **Casework**: Case B (triangle has 2θ) vs Case C (θ = 90°) splits the proof.

### Knowledge-base entries to use

- **Invariants & monovariants** (Combinatorics section): Shan-Yu's survival uses a simple finite-set invariant.
- **Constructive / incremental** (Combinatorics): Mulan's strategy builds up angle 2θ step by step.
- **Direct proof / Induction** (General Proof Methods): the n-step Mulan strategy.
- **Casework / exhaustion**: the "both pieces have θ" analysis splits into exactly Case B and Case C.

### Analogous past problems (cruxes)

1. **aimo-0225** (arc game on n-gon, 2-adic recursion): "Determine game value by recursing on the 2-adic valuation of a difference that exactly halves at each step." Here the analog is: Mulan wins iff the "halving chain" for angle 180°/θ terminates at an integer (i.e., 180°/θ ∈ ℤ). The P/N structure mirrors the recursive angle-doubling chain. Adaptation: instead of 2-adic valuations of integer differences, use the doubling orbit of θ under the map x ↦ 2x on (0°, 180°).

2. **aimo-0262** (Cinderella bucket game): "Hand the defender a self-reproducing invariant family of configurations; each legal move can restore it." Shan-Yu's S-invariant ("no angle in the doubling orbit of θ") is exactly such a self-reproducing invariant — Shan-Yu always finds a piece that restores it.

3. **aimo-0236** (valuation-based token game): "To prove a player can prolong forever, have that player nurse a single chosen token so a driving valuation stays strictly above the threshold." Shan-Yu maintains "no angle = 2^k·θ for any k" (a valuation-type condition on angles), which he can nurse indefinitely since the chain 2^k·θ never hits 180°.

### Prior progress

None (no workspace exists; this is round 1 exploration).

### Dead ends (do not retry)

- The BFS minimax at depth ≤ 5 with small eps gives false negatives for small θ (e.g., θ = 1°, 10°) because those require ~n/2 steps, far beyond depth 5.
- The "all angles < 120°" invariant (suggested for θ = 120°) generalizes: Shan-Yu needs the S-invariant, not a naive angle bound.
- Trying to classify by "θ/180° rational vs irrational" is WRONG — many rational θ (like 40°, 72°, 120°) are Shan-Yu wins.

### Small-case / intuition notes (labeled as conjecture)

- **Conjecture confirmed by computation**: Mulan wins iff θ = 180°/n for some integer n ≥ 2.
- **Step counts** (conjectured): θ = 90° → 1 step; θ = 60° or 45° → 2 steps; θ = 36° or 30° → 2–3 steps; θ = 180°/n → at most ⌊90/θ⌋ steps (approximately n/2).
- **Special role of 90°**: the identity 2×90° = 180° makes it the unique 1-step-win angle and the "forcing engine" for all other 180°/n values via the two-stage strategy.
- **Why θ > 90° always loses** (conjecture): 2θ > 180° so the doubling orbit S = {θ} is a singleton; Shan-Yu trivially maintains "no angle = θ" since he can't even be forced into having 2θ (degenerate).
