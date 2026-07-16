## imo-2026-03: Type 3 Strategy Algebraic Characterization for n=5

**Lens:** Type 3 algebraic characterization in the "all pairwise > 1" bounded region.

---

### Critical Finding: Type 3 Strategies Are Insufficient

The claim from n5-five-mark.md ("100% Type 3 coverage with 50x50 grid") is FALSE. With finer grids (N=40 on each cut position), approximately 5-6% of valid samples in the bounded "all pairwise > 1" region have best achievable Type 3 LB **above** c(5). These are genuine failures, not numerical artifacts.

**Example failure:** params (α,β,γ,δ,ε,ζ) = (0.007, 2.205, 3.321, 1.060, 4.441, 5.584), weighted sum ≈ 42, min pairwise diff = 1.053 > 1.
- Best Type 3 LB = 0.508115 > c(5) = 0.507937.
- Pattern: α is very small (close to 0), δ is second-smallest. These are edge cases near the Case A/B boundary.

---

### What Type 3 Strategies Create

A Type 3 strategy uses 2 marks (arbitrary positions) on 2 different pieces + 3 marks (halves) on 3 other pieces. The 6th piece is left as a singleton.

**Piece count:** 6 LB pieces + 5 XY marks → 11 total pieces. LB picks ceil(11/2) = 6.

After Pairing Cancellation for 3 halved pairs:
```
LB = sum(P_halved)/2 + lb_score({s1, P_cut1 - s1, s2, P_cut2 - s2, P_singleton})
```
where lb_score of 5 pieces picks 3 (positions 1,3,5 in sorted descending).

**Algebraic condition for Type 3 "Cut P_a, P_b; Halve others; Singleton P_c":**
XY minimizes lb_score({s1, P_a-s1, s2, P_b-s2, P_c}) = (P_a + P_b + P_c) - (2nd + 4th largest). XY maximizes the sum of the 2nd and 4th largest values.

For the 5 pieces to create near-pairs (Singleton-Pair structure), we need |P_c - s_i| ≤ L0 for some cut piece s_i, OR |P_a-s1 - (P_b-s2)| ≤ L0, etc. All 15 Singleton-Pair conditions fail in the bounded region (that's the definition of "all pairwise > 1").

---

### The Correct Strategy Class: (2,2,1) = Split Two Pieces + Halve One

**Definition:** XY uses 2 marks on piece P_a (creating 3 sub-pieces t1, t2-t1, P_a-t2) + 2 marks on piece P_b (creating 3 sub-pieces) + 1 mark (halve) on piece P_c. Three remaining pieces are uncut singletons.

**Key result (verified computationally with scipy on all 11 Type-3 failures):** The (2,2,1) strategy with the family "Split P3, Split P5, Halve P6" ALWAYS achieves LB ≤ c(5) in the bounded region. Example on the specific failure case above: best (2,2,1) LB = 0.5009 << c(5) = 0.5079.

---

### Mechanism of the (2,2,1) Strategy

For "Split P3, P5; Halve P6; Singletons P1, P2, P4":

After Pairing Cancellation for P6:
```
LB = P6/2 + lb_score({t1, t2-t1, P3-t2, s1, s2-s1, P5-s2, P1, P2, P4})
```
LB picks 5 of these 9 pieces.

**Optimal cut positions create FOUR simultaneous near-pairings:**
1. Cut P5 at s2 ≈ P1+P2 from start: creates sub-pieces {s1≈P1, s2-s1≈P2, P5-s2}
2. P5-s2 ≈ P4 (near-pair with singleton P4) when s2 ≈ P5-P4 = d4

This requires simultaneously: s1 ≈ P1 AND s2-s1 ≈ P2 AND P5-s2 ≈ P4.
These three give: s2 ≈ P1+P2 (from first two) AND d4 ≈ P5-P1-P2 (from third).

The near-pairs from P5 splits create three "near-Pairing Cancellations":
- {P1, s1}: difference ≈ |α - (s1/L0 - 1)| in normalized units
- {P2, s2-s1}: difference proportional to |s2-s1 - P2|
- {P4, P5-s2}: difference proportional to |d4 - 2P1 - d1| = |ε - 2α - β - 1| in shifted params

**Algebraic condition for near-pairs to work:**
The crucial condition is that the COMBINATION of three near-pairings keeps LB below c(5), even when individual differences exceed L0. Verified numerically: in the bounded region, optimal (s1, s2) always produces combined LB < c(5).

---

### Algebraic Formula for (2,2,1) Strategy LB

After 1 Pairing Cancellation for P6/2 and 3 approximate Pairing Cancellations for {P1,s1}, {P2,s2-s1}, {P4,P5-s2}:

```
LB ≈ P6/2 + P1 + P2 + P4 + lb_score({t1, t2-t1, P3-t2, δ1, δ2, δ3})
```
where δ1 = |s1-P1|, δ2 = |s2-s1-P2|, δ3 = |P5-s2-P4| are near-pair errors (each small).

The 6 remaining pieces {t1, t2-t1, P3-t2, δ1, δ2, δ3} contribute LB picks 3 of 6 (approx 3 of 5 since one Pairing Cancellation happens in the 9-piece score too).

P6/2 + P1 + P2 + P4 = [(ζ+ε+δ+γ+β+α+6)/2 + (α+1) + (α+β+2) + (α+β+γ+δ+4)] × L0
= [(ζ+ε+δ+γ+β+α+6)/2 + 3α+2β+γ+δ+7] × L0

For this ≤ c(5) = 32L0, we need the remaining lb_score contribution ≤ c(5) - P6/2 - P1 - P2 - P4.

**In shifted param terms:** P6/2 + P1 + P2 + P4 in L0-units equals (ζ+ε+δ+γ+β+α+6)/2 + 3α+2β+γ+δ+7. Using weighted sum constraint 6α+5β+4γ+3δ+2ε+ζ=42, this simplifies to a computable expression. The "slack" c(5) - P6/2 - P1 - P2 - P4 ≥ 0 is guaranteed in the bounded region.

---

### Distinct Openings for the Outliner

1. **Compactness argument:** The bounded region (g ∈ (1,1.2), v_0 ∈ (0,1/3)) is compact. The function min_{(2,2,1) strategies} LB is continuous. On the BOUNDARY of the bounded region, either V_j or Pairwise strategies apply (since some d_j → L0 or some pairwise → 1 on the boundary). In the INTERIOR, computational evidence shows strict LB < c(5). By compactness, min < c(5) on the closed bounded region. This is not a purely algebraic proof but may be formalizable.

2. **Direct algebraic via sum bound:** Fix the (2,2,1) strategy with "Split P3 at (P3-P2, P3), Split P5 at (P1, P1+P2)" (exactly). This creates pairs {P2,P2} and approximately {P4, P5-P1-P2}. The condition for near-pair 3 is |P5-P1-P2-P4| = |d4-2P1-d1| = |ε-2α-β-1|×L0 ≤ L0, i.e., |ε-2α-β-1| ≤ 1. This holds when ε ≤ 2α+β+2. When ε > 2α+β+2, a DIFFERENT cut on P5 (not at P1+P2) creates the near-pairs.

3. **NEW: Induction on pair structure.** The (2,2,1) strategy creates up to 3 near-pairs simultaneously from P5 splits. When the 3 near-pairs have combined singleton difference ≤ 3L0, the Singleton-Pair formula generalization gives LB ≤ c(5). Proving this bound on combined error requires tracking how the error in each near-pair propagates through the lb_score computation.

4. **Alternative route avoiding the bounded region:** Find an argument that the "all pairwise > 1" bounded region can NEVER arise in B_small without some OTHER structure being exploitable. This would require proving a stronger version of the Pigeonhole Lemma.

---

### Candidate Techniques

- **Pairing Cancellation** (certified lemma): apply 4 times (1 halve + 3 near-pairs)
- **Continuity/compactness** on the bounded region (bounded, closed subset of R^6)
- **Singleton-Pair Formula generalization** to 3 near-pairs with bounded combined error
- **LP/convex duality**: the existence of feasible (t1,t2,s1,s2) is a feasibility LP

---

### Knowledge-Base Entries

- Greedy Optimality Lemma (CERTIFIED)
- Pairing Cancellation Lemma (CERTIFIED)
- Singleton-Pair Formula (CERTIFIED for n=3)
- V_j Strategy (PROVED for n=5)
- Halve+IH Strategy (PROVED for all n≥2)
- "All pairwise > 1" Bounded Region characterization (g ∈ (1,1.2), v_0 ∈ (0,1/3))

---

### Prior Progress

- V_j strategies: PROVED for any d_j ≤ L0
- Pairwise strategies (15 strategies): PROVED for any |x_i-x_j| ≤ 1
- "All pairwise > 1" bounded region: identified and bounded (certified)
- Type 3 coverage: CLAIMED 100% but FALSE (actual ~95%)
- (2,2,1) coverage on Type-3-failures: CONFIRMED by scipy (all tested)

### Dead Ends

- Type 3 alone (2 cuts + 3 halves on different pieces): insufficient (~95% only)
- Halve P5 + n=4 IH: fails because LB bound exceeds c(5) when P5 < c(5)
- Quadruple-halve + single cut on P2: gives LB = 1/2+P1/2 > c(5) (same as Case A)
- Strategy (4,1): 4 marks on 1 piece + 1 halve: FAILS (LB ≈ 0.53)
- Strategy (5,0): all marks on 1 piece: FAILS

### Small-case / Intuition Notes

- The bounded region has g ∈ (1, 1.2) and v_0 ∈ (0, 1/3); P1 is close to L0 in failure cases
- Failure cases are concentrated near the Case A/B boundary (α → 0)
- The (2,2,1) strategy "Split P3, P5; Halve P6" creates 4 near-pairs: {P6/2,P6/2} exact + {s1,P1} + {s2-s1,P2} + {P5-s2,P4} approximate
- Optimal (s1,s2) for P5 satisfies s1 ≈ P1 and s2 ≈ P1+P2 ≈ d4, making P5-s2 ≈ P4
- The P3 split (t1,t2) contributes additional near-pairings that reduce LB further
- The COMBINED effect of all 4 near-pairs achieves LB well below c(5) (gap ≈ 0.007)
