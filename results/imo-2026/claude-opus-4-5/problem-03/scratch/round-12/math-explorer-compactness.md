## imo-2026-03

**Lens: Compactness/existence argument for n=5 "all pairwise > 1" region**

---

### Distinct openings

1. **Berge continuity + finite certificate.** f(config) = min_T min_{a,b} LB(T,a,b,config) is CONTINUOUS by Berge's Maximum Theorem (LB is continuous in all arguments; the feasible set for cut positions varies Lipschitz-continuously with config). Since K is bounded and f is continuous, f achieves its sup on K. Computation shows sup f < c(5) on K; a rigorous proof would need interval arithmetic to certify a gap δ > 0.

2. **LP structure of optimal cuts.** For a fixed strategy type T and fixed ordering of the 11 result-pieces, LB is a LINEAR function of cut positions (a,b) and config. Optimal (a*,b*) lies at a breakpoint where piece ordering changes. This means: for each of finitely many "orderings," LB ≤ c(5) is a LINEAR inequality in (config, a, b). Enumerate orderings; union covers K. This is a finite algebraic certificate — no interval arithmetic needed.

3. **Boundary limit argument.** On ∂K (some param → 0 or some pairwise diff → 1), V_j or pairwise strategies give LB → c(5) from below. So f → c(5) on ∂K. By the maximum principle for continuous functions on a compact domain, if f ≤ c(5) on ∂K and f is subharmonic (which it isn't in general), then f ≤ c(5) inside too. This is NOT rigorous but motivates the claim.

4. **The "equal-position cut" strategy.** XY cuts two different pieces P_i and P_j at the SAME position t (creating pair {t, t}). The optimal t equates a function of the remaining pieces. For many configs in K, this strategy gives LB ≈ P1 + P5 + (P2+P6)/2 or similar explicit formula. This formula ≤ c(5) iff a linear inequality holds — algebraically verifiable. Candidate: cut P3 and P5 both at t*, halve P2 and P6, cut P1 at tiny. Result: LB ≈ P1 + P5 + (P2+P6)/2.

5. **63-permutation partition.** The "all pairwise > 1" region K with wsum=42 is partitioned into 63 cells by the valid permutations (g_coeffs 35..41). Each cell has a specific relationship between {α,β,γ,δ,ε,ζ} and the sorted order. For each cell, there is (computationally) a SINGLE explicit strategy type (leave_idx, cut_i, cut_j, halve_indices) that works. Find these 63 strategies algebraically — this is a finite but complete proof.

---

### Candidate technique(s)

- **Compactness + Berge continuity** (structural framework, not a proof by itself).
- **LP duality at breakpoints** (translates cut-position optimization to a finite case analysis).
- **Equal-position double-cut** (new strategy: cut two pieces at t — creates pair {t,t} — more powerful than cut-at-existing-piece).

---

### Cheap-kill candidates

- **The "all pairwise > 1" region is NOT empty for n=5 B_small** (confirmed: configs exist with g ∈ (1, 1.2), wsum=42, P6 < c(5)). No pigeonhole eliminating it.
- **Boundary triviality**: Configs near ∂K (any param < ε or any pairwise diff < 1+ε) are handled by V_j or pairwise strategies with LB < c(5). Only the deep interior matters.
- **The region is bounded**: sum of params = S ≤ 6v0 + 15g ≤ 12 + 5g < 18 (since g < 1.2). So S < 18, meaning P6 < (18+6)/63 < 1/2 < c(5). The B_small constraint is automatic — no need to handle B_large separately.

---

### Knowledge-base entries to use

None identified as directly applicable (no "interval arithmetic" or "compactness for game proofs" entries in KB from prior rounds).

---

### Analogous past problems (cruxes)

None found with sufficient analogy to the equal-position cut or the 63-permutation partition structure.

---

### Prior progress

- V_j strategies PROVED (handles any d_j ≤ L0).
- Pairwise strategies PROVED (handles any |x_i - x_j| ≤ 1 in shifted params).
- The "all pairwise > 1" region: bounded (g < 1.2), non-empty, computationally covered at 100% by Type 3 strategies. Algebraic proof OPEN.
- All "failures" in computation were from INVALID configs (wsum ≠ 42 means pieces don't sum to 1). When the constraint wsum=42 holds exactly, every tested config passes (margin ≥ 0.008 away from c(5)).

---

### Dead ends (do not retry)

- **Pigeonhole for n=5**: min weighted sum = 21v0 + 35g > 35 but constraint = 42 > 35, so "all pairwise > 1" region EXISTS — pigeonhole does not eliminate it (unlike n=4 where min > 20 > 16).
- **Single algebraic cut formula**: No single formula for (a*, b*) as functions of config seems to cover all of K. Different permutations need different strategies.
- **Standard pairwise strategies (individual shifted params)**: All fail in "all pairwise > 1" region by definition (all pairwise diffs > 1 in shifted-param space).

---

### Small-case / intuition notes

**Conjecture (not proved):** f(config) = min_{T,a,b} LB(T,a,b,config) is strictly less than c(5) on the interior of K, with f → c(5) only as config → ∂K. Evidence: every VALID config (wsum=42 exactly) tested has f ≤ c(5) - 0.007 (strong interior margin). The apparent failures in prior rounds were computation artifacts from invalid configs.

**Key algebraic finding for the outliner:** The "equal-position double-cut" strategy (cut P_j and P_k both at the same value t) creates a new pair {t, t} beyond what single cuts can achieve. For configs where (6α + 5β + 4γ + 3δ + 2ε + ζ = 42 and all pairwise > 1 and α is small), the strategy:
- Cut P3 at t, cut P5 at t (creating pair {t, t})
- Halve P2, halve P6
- Tiny cut on P1

gives LB ≈ P1 + P5 + (P2+P6)/2. This is ≤ c(5) iff (after substituting):
3α + 2β + (3γ + 3δ + 3ε + ζ)/2 ≤ 22,
which holds when ε ≤ β + γ + 2 (a linear condition in shifted params).

For the complementary case (ε > β + γ + 2), a different strategy is needed — the 63-permutation partition determines which.

**Compactness argument verdict:** The continuity of f and the compactness of K are STRUCTURAL FACTS that confirm the problem is solvable in principle without needing an analytic formula. But the compactness argument alone does not constitute a proof. The real work is either (a) interval arithmetic over K, or (b) the 63-case algebraic argument. Path (b) is more olympiad-appropriate but requires significant casework.
