## imo-2026-03 — L2 Exchange-Step Terrain Report

### 1. Precise restatement of L2

**Setup (§4 units, scaled by D = 2^{n+1}−1).**
LB marks geometric positions: pieces {R_0=1, R_1=2, ..., R_{n-1}=2^{n-1}, R_n=2^n}.
XY makes k ≤ n cuts total.

- *Spare-R_n case*: XY places no cut in R_n → §4.1 gives A ≥ 2^n for every placement, PROVED.
- *R_n-cut case*: XY places k_n ≥ 1 cuts inside R_n. The confined sub-case (all k cuts in R_n, k_stray = 0) is PROVED by DyadicLower-confined.

**What L2 must establish**: for ANY XY strategy that cuts R_n and also places k_stray = s ≥ 1 cuts in some R_j (j < n), the alternating sum A ≥ 1 (equivalently O ≥ 2^n).

**Piece multiset in the stray case** (budget k_n + s ≤ n, s ≥ 1):
- k_n + 1 fragments of R_n, summing to 2^n. (k_n ≤ n − s ≤ n−1.)
- For each j that XY cuts: sub-pieces of R_j summing to 2^j, with each sub-piece < 2^j ≤ 2^{n-1}.
- Uncut intacts {2^k : k ∉ cut-index set, k < n}.
- Total non-R_n pieces: (n − s) uncut intacts + 2s sub-pieces = n + s. (Each stray cut turns 1 intact into 2 sub-pieces, net +1 per stray cut.)
- Sum of non-R_n pieces = 2^n − 1 (unchanged from confined). All non-R_n pieces < 2^{n-1}.

### 2. Numerical sanity checks (conjectured, not proved)

All numerical results are computed in exact or high-precision arithmetic:

| Config | min A over class | A ≥ 1? |
|---|---|---|
| Confined, k_n = n-1 = 2 cuts (n=3) | 1.00 (exact interleaving) | ✓ |
| Stray: k_n=2 cuts, 1 stray in R_2 (n=3) | 1.10 | ✓ |
| Stray: k_n=1 cut, 1 stray in R_2 (n=3) | 1.10 (same!) | ✓ |
| Stray: k_n=2 cuts, 1 stray in R_1 (n=3) | 1.10 | ✓ |
| Stray: k_n=2 cuts, 1 stray in R_0 (n=3) | 1.02 | ✓ |

**Conjecture (numerical)**: min A over stray configs with s ≥ 1 is strictly > 1. The infimum approaches 1 only in the limit where stray cut lengths → 0 (recovering the confined interleaving). The strict minimum is not attained in the stray subspace.

**CONFIRMED**: in all 60,000+ tested stray configs for n=3, A ≥ 1 with no violations. Min observed ≈ 1.02, well above 1.

**Exchange direction fact**: for same TOTAL budget k ≤ n, min_confined A = 1 ≤ min_stray A ≈ 1.10. Adding stray cuts HURTS XY globally. But pointwise: adding a stray cut to FIXED R_n cuts can DECREASE A (716/17980 violations in tests). So the pointwise exchange "stray → confined weakly increases A for same R_n cuts" is FALSE.

### 3. Key structural insight (the count argument)

**Claim**: With k_n + 1 R_n fragments and n + s non-R_n pieces, and k_n ≤ n − s (budget), we have k_n + 1 ≤ n − s + 1 < n + s for ALL s ≥ 1.

**Proof**: n − s + 1 < n + s iff 1 < 2s iff s ≥ 1. ✓

**Consequence** (count of non-R_n pieces at odd ranks): In any sorted order of T = k_n + 1 + n + s total pieces, there are ⌈T/2⌉ odd ranks. For all n + s non-R_n pieces to be at EVEN ranks, we'd need k_n + 1 ≥ n + s R_n fragments at odd ranks plus n + s non-R_n at even ranks, requiring k_n + 1 ≥ n + s. But k_n + 1 < n + s. **Contradiction**. Hence: at least one non-R_n piece is always at an ODD rank.

**Numerical confirmation**: In all tested stray configs, exactly 1–4 non-R_n pieces at odd ranks (never 0). Min A when exactly 1 non-R_n at odd rank: ≈ 1.10 > 1.

### 4. Why the approach file's §4.4 "cannot tie" argument is the right start

§4.4 (rigorous half, proved in approach file): "if k_n ≤ n − 1, then R_n contributes at most n pieces; at least one intact 2^m has no R_n-fragment straddling it, forcing 2^m at an odd rank and A > 1."

**CAVEAT**: This argument as stated applies to the confined case (intact intacts, no stray sub-pieces). In the augmented case, a stray sub-piece could potentially "straddle" the intact 2^m (substitute for a missing R_n fragment), keeping 2^m at even rank. So §4.4 as written does NOT directly close L2.

**Extension needed**: Show that stray sub-pieces (which are sub-pieces of R_j < 2^j ≤ 2^{n-1}) cannot effectively substitute for missing R_n fragments in the straddling structure. The KEY ASYMMETRY: R_n fragments can be anywhere in (0, 2^n) (the full range), while stray sub-pieces are bounded by 2^j ≤ 2^{n-1}. In the a=0 region (all fragments ≤ 2^{n-1}), both R_n fragments and stray sub-pieces are in (0, 2^{n-1}], but their TOTALS differ: sum(R_n frags) = 2^n >> sum(sub-pieces of R_j) = 2^j ≤ 2^{n-1}.

### 5. Distinct openings (the terrain)

**Opening A — Count + Dyadic Structure Bound** (most concrete, potentially most direct):

Step 1: By the count argument, at least one non-R_n piece lies at an odd rank.
Step 2: The specific DYADIC STRUCTURE of the intacts and sub-pieces constrains which non-R_n piece is at odd rank. Show the contribution of that piece to O, combined with the R_n fragments at odd ranks, forces O ≥ 2^n.

The key sub-claim: "if exactly one non-R_n piece p is at odd rank, and p is a piece of value ≥ 1 (the minimum piece), then O ≥ p + (R_n frags at odd ranks) ≥ 1 + (R_n at odd) ≥ 2^n."

TRAP: "R_n at odd" could be less than 2^n − 1 (if some R_n frags are at even ranks). Need: 1 + (R_n at odd) ≥ 2^n, i.e., R_n at odd ≥ 2^n − 1 = sum of all non-R_n. This fails when many R_n frags are at even ranks.

The correct version: use the specific DYADIC constraint that the smallest non-R_n piece at odd rank is at LEAST the smallest non-R_n piece overall. With LB's geometric construction, the smallest intact is 1 and stray sub-pieces are ≥ ε (arbitrary). So this approach needs more care; it works best when the smallest non-R_n piece at odd rank is the SMALLEST INTACT.

**Opening B — Augmented DyadicLower (adapt Case 1/Case 2)** (structurally cleanest):

Run the same compact minimization on the AUGMENTED SPACE (stray + confined). The minimum of A over the augmented space is also attained at a vertex of the cell complex. At any vertex:

- **Case a=1** (some R_n fragment > 2^{n-1}): top-fragment cascade (§4.2.4, PROVED). A ≥ 1. ✓
- **Boundary w_1 = 2^{n-1}**: a=1 closure by continuity. ✓  
- **Case 2 (w_1 = max R_n frag ∈ (2^{n-2}, 2^{n-1}))**: 
  - In confined: only 2^{n-1} above w_1 → G(w_1) = 1 (named receiver, no-donor → A ≥ 1). PROVED.
  - In augmented: if R_{n-1} is cut into {a, 2^{n-1}−a}, the sub-piece 2^{n-1}−a could be above w_1. Need to show w_1 is STILL a receiver (G(w_1) odd).
  - KEY: pieces above w_1 are: R_n fragments above w_1 (none, since w_1 is max R_n frag) + non-R_n pieces above w_1. Non-R_n pieces above w_1 in (w_1, 2^{n-1}]: these are either the intact 2^{n-1} (if R_{n-1} is not cut) or sub-pieces of R_{n-1} in (w_1, 2^{n-1}). G(w_1) = count of pieces strictly above w_1.
  - G(w_1) = count of non-R_n pieces in (w_1, 2^{n-1}]. This can be ANY non-negative integer, not necessarily 1.
  - CHALLENGE: G(w_1) might be even → w_1 is NOT a receiver → the confined Case 2 argument fails.
  - Potential fix: show that at a minimizer with G(w_1) even, we can still derive A ≥ 1 via a different argument. Or show G(w_1) is forced to be odd by minimality.

- **Case 1 (w_1 ≤ 2^{n-2})**: 
  - In confined: A ≥ v_1 − v_2 = 2^{n-1} − 2^{n-2} = 2^{n-2} ≥ 1. Uses: v_1 = 2^{n-1}.
  - In augmented: if R_{n-1} is cut, v_1 might be 2^{n-1}−a ∈ [2^{n-2}, 2^{n-1}). And v_2 ≤ max(w_1, a, 2^{n-2}) ≤ 2^{n-2} (since w_1 ≤ 2^{n-2} and a ≤ 2^{n-2}). So A ≥ v_1 − v_2 ≥ (2^{n-1}−a) − 2^{n-2} = 2^{n-2} − a ≥ 0. **NOT ≥ 1 if a close to 2^{n-2}.**
  - CHALLENGE: Case 1 needs a DIFFERENT ARGUMENT when R_{n-1} is cut.
  - Potential fix: if R_{n-1} is cut with a ≈ 2^{n-2}, the two sub-pieces are both ≈ 2^{n-2}. The pair {a, 2^{n-1}−a} contributes 0 to A by Lemma H's pair-cancellation logic (they're adjacent in sorted order). Combined with the remaining piece structure, A ≥ 1 can be recovered.

**Opening C — Global minimizer ∈ confined subspace**:

Argue that any global minimizer M_min of A over all XY strategies must be in the CONFINED subspace (no stray cuts). This gives: min A (over all stray) = min A (over confined) = 1, hence all stray A ≥ 1.

Proof of "M_min must be confined": At any stray config M, the directional derivative of A with respect to "moving the stray cut position in R_j → toward R_n" is ≤ 0 (A can be decreased by this move). Hence M cannot be a global minimizer. So the global minimum is not achieved in the stray subspace.

**CRITICAL sub-claim**: At ANY stray config with a stray cut in R_j, there EXISTS a direction "adjust stray cut → R_n cut" that DECREASES A.

From the cut-effect formula: the exchange direction ΔA = −(stray cut effect) + (R_n cut effect). We need ΔA ≤ 0 for some R_n cut choice. This is a QUANTITATIVE claim that may be hard to prove in full generality.

**Opening D — Batch argument**: 

View each "batch" of stray sub-pieces of R_j as replacing the intact R_j = 2^j. Show that REPLACING R_j with any two sub-pieces {a, 2^j−a} CANNOT decrease A below its confined value (for the same R_n cut configuration).

From the cut-effect formula (cutting R_j at position a):
ΔA = [μ{t ∈ (0, a): N even} − μ{t ∈ (0, a): N odd}] + [μ{t ∈ (2^j−a, 2^j): N odd} − μ{t ∈ (2^j−a, 2^j): N even}]

For ΔA ≥ 0 (cutting R_j doesn't decrease A), need: the "even" intervals dominate in both terms.

In the specific LB geometric construction:
- N_I(t) = n − k for t ∈ [2^{k-1}, 2^k) has SPECIFIC PARITY.
- For t ∈ (0, a) with a ≤ 2^{j-1}: N_I(t) = n − j + 1 (parity depends on n − j + 1).
- For t ∈ (2^j−a, 2^j): N_I(t) = n − j (parity depends on n − j).

The sign of ΔA depends on BOTH n − j (parity) AND the current N_F(t) distribution. This is NOT uniformly positive → the batch argument fails in general. (Numerically confirmed: adding a stray cut can decrease A for fixed R_n cuts.)

**DEAD-END DIRECTION** (confirmed by numerics): The simple monotone claim "cutting R_j ≥ 0 for fixed R_n cuts" is FALSE. There are stray configs with A BELOW the confined A for the same k_n R_n cuts. (716/17980 violations in n=3 tests.) **Do not retry this direction.**

### 6. Most promising route for the builder

**RECOMMENDED ROUTE**: Combine Opening A and Opening B, targeting Case-by-Case in the augmented DyadicLower:

1. **Case a=1**: top-fragment cascade (CERTIFIED, no new work).
2. **Case 1 (w_1 ≤ 2^{n-2}) with R_{n-1} intact**: A ≥ 2^{n-2} ≥ 1 exactly as in confined. ✓
3. **Case 1 with R_{n-1} cut at position a**: The pair {a, 2^{n-1}−a} both have value ≤ 2^{n-2} (wait: 2^{n-1}−a > 2^{n-2} when a < 2^{n-2}). NEED: A ≥ 1 when R_{n-1} is cut and w_1 ≤ 2^{n-2}.
   - Sub-case: if the pair {a, 2^{n-1}−a} has 2^{n-1}−a > 2^{n-2}, then Case 1 reduces to: max non-R_n piece is 2^{n-1}−a > 2^{n-2} > w_1. Apply INDUCTION on n: the pair {a, 2^{n-1}−a} + R_n fragments + other intacts can be analyzed as a SMALLER instance.
   - If a = 2^{n-2} (midpoint cut): {2^{n-2}, 2^{n-2}} are a pair; by Lemma H pair-cancellation, they contribute 0 to A. The remaining pieces are {1,...,2^{n-2}} (uncut intacts) + R_n fragments. By DyadicLower-confined applied to (n-1) intacts + R_n fragments (with fewer "effective" intacts), A ≥ 1. [**This is a valid inductive application!**]
4. **Case 2 (w_1 ∈ (2^{n-2}, 2^{n-1}))**:
   - Count pieces above w_1: these are ONLY non-R_n pieces (in the a=0 part). Let G = number of non-R_n pieces in (w_1, 2^{n-1}].
   - If G is ODD: w_1 is a receiver → no-donor argument → A ≥ 1 (same as confined Case 2, just with more non-R_n pieces above w_1).
   - If G is EVEN: w_1 is NOT a receiver. NEED new argument.
   - Key observation: if G is even and w_1 is not a receiver, then by minimality... (no-donor forces G(w_1) = 0 or even). Need to show this forces A ≥ 1 via a different sub-case.

**CHEAP-KILL CANDIDATES**:
- Parity of G(w_1): For G even, the no-donor argument doesn't directly apply. Check whether G being even creates a different structural contradiction that still gives A ≥ 1.
- **SPECIFIC TO L2**: For s = 1 stray cut in R_j, check whether G(w_1) can actually be even at a minimizer. If G is always odd at the minimizer (by a separate counting argument), Case 2 closes cleanly.
- For s = 1 stray in R_{n-1} specifically: the pair {a, 2^{n-1}−a} replaces 2^{n-1}. Pieces above w_1 in the augmented case: these are 2^{n-1}−a (if > w_1) and possible other sub-pieces. With only ONE stray cut in R_{n-1}, G(w_1) ∈ {1, 2} depending on whether a or 2^{n-1}−a is above w_1. If a < w_1 ≤ 2^{n-1}−a: G includes 2^{n-1}−a only → G = 1 (odd) → receiver! ✓. If both > w_1 (a > w_1): G = 2 (even). But a ≤ 2^{n-2} < 2^{n-2} < w_1 (since w_1 > 2^{n-2})... wait: w_1 > 2^{n-2} and a ≤ 2^{n-2} (since the smaller sub-piece ≤ half of R_{n-1} = 2^{n-2}). So a ≤ 2^{n-2} < w_1 → a is NOT above w_1. Hence G counts only 2^{n-1}−a (if > w_1). And 2^{n-1}−a ≥ 2^{n-2} with equality only if a = 2^{n-2}. Since w_1 > 2^{n-2}: if a < 2^{n-2} then 2^{n-1}−a > 2^{n-2} but might still be ≤ w_1 or > w_1.
  - If 2^{n-1}−a > w_1: G = 1 (odd) → receiver. ✓
  - If 2^{n-1}−a ≤ w_1: G = 0 (even). But then 2^{n-1}−a ≤ w_1 < 2^{n-1} and a = 2^{n-1}−(2^{n-1}−a) ≥ 2^{n-1}−w_1 > 0. The pair {a, 2^{n-1}−a} is now BELOW w_1. Combined with all other non-R_n pieces being intacts {1,2,...,2^{n-2}} (assuming R_{n-1} is the only stray cut), G(w_1) = 0 (even). This is the hard sub-case.
  
  **For this hard sub-case**: G(w_1)=0, so minimality says: no direction e_{w_1}−e_b has A'₊ ≤ 0 for any b. But A'₊(e_{w_1}−e_b) = (−1)^{G(w_1)} + (−1)^{Geq(b)} = 1 + (−1)^{Geq(b)}. For A'₊ = 0: Geq(b) odd. So there EXIST donors in this case → A'₊ = 0 (flat moves exist). Following flat moves takes us to a boundary or lower-m configuration. The DyadicLower-confined argument's sub-case (2c) / flat-move termination should still apply here by the same well-foundedness argument.

**VERDICT**: Opening B (augmented DyadicLower) is the most tractable. Case 1 closes by induction/pair-cancellation; Case 2 needs careful handling of G(w_1) parity in the augmented setting, but the flat-move argument (from DyadicLower-confined sub-case 2c) appears to close all branches.

### 7. Knowledge-base entries to use

- **Invariants & monovariants** (KB): the DyadicLower-confined proof's well-foundedness argument (flat-move weight m = #{positive fragments}) applies equally to the augmented case.
- **Piecewise-concavity smoothing** (KB): A is piecewise-affine on the augmented compact space; min attained at a vertex.
- **Casework / exhaustion** (KB): the Case 1/2/boundary split with the additional G-parity sub-cases.
- **Invariants & monovariants** (KB): for "flat-move termination" — the weight m = #{positive non-R_n pieces at odd rank} is a strictly-decreasing monovariant.

### 8. Analogous past problems (cruxes)

Searched combinatorics corpus under `games-and-strategy`, `extremal-principle`, `invariants-and-monovariants`. No strongly analogous problem found — most game cruxes involve board games or token games, not continuous interval-splitting with alternating rank sums. The closest analog is **aimo-0146** (exchange smoothing: "bound a weighted sum by repeatedly moving unit from over-index to under-index"), but the specific structure here (piecewise-affine A on a simplex, dyadic intacts) does not match. **Verdict: none (no strongly analogous crux)**.

### 9. Prior progress & dead ends

**CERTIFIED**: DyadicLower-confined (A ≥ 1 when all XY cuts in R_n). This closes 100% of the CONFINED case. L2 is the ONLY remaining lower-bound gap.

**DEAD ENDS (do not retry)**:
- "Adding a stray cut always increases A for fixed R_n cuts" — FALSE (716/17980 violations). Do not retry.
- Integral identity ‡ — CIRCULAR (identical to A ≥ 1), dropped rounds 3+.
- "Receiver always exists" for a=0 clustered configs — REFUTED round 5.
- Exchange argument direction: "stray → confined config with same k_n gives lower A" — pointwise FALSE (stray can help XY vs same-k_n confined). Do not retry in this form.

**WHAT IS OPEN**: Whether the count argument (k_n+1 < n+s → ≥1 non-R_n at odd rank) can be tightened to give A ≥ 1 (not just A > 0) — this requires using the specific dyadic structure of the non-R_n pieces.

### 10. Small-case / intuition notes (conjectures)

- Min A over stray configs (n=3): ≈ 1.10 for k_n=1 or 2, ≈ 1.02 for k_n=2 and stray in R_0. CONJECTURE: min_stray A > 1 for all n ≥ 2.
- When exactly 1 non-R_n piece lands at odd rank: min A ≈ 1.10 (not 1). The odd-ranked non-R_n piece contributes positive surplus BEYOND 2^n → A > 1.
- For the augmented Case 2 with G(w_1)=0 (no non-R_n piece above w_1): the sub-case G=0 means w_1 is the TOP PIECE of the sorted list among ALL pieces of value ≤ 2^{n-1}. This is a very specific structural configuration; the DyadicLower-confined flat-move argument should close it.
- The PAIR CANCELLATION of stray sub-pieces ({a, 2^j−a} can contribute 0 to A if adjacent in rank) is actually GOOD for the proof: it means the stray cut's net effect on A is at most +2a (the smaller sub-piece moves to odd rank and contributes +a; net with pair = +a ≥ 0). This forces A to be AT LEAST the confined-value-minus-a, which with the dyadic structure is ≥ 1 when a is small. But for a close to 2^{j-1} (near-midpoint stray cut), the cancellation is near-exact and A drops toward the confined value for fewer R_n cuts — but still ≥ 1.
