# Proof Builder Report: imo-2026-03, Round 4

## Approach: induction-on-n

### Summary

Completed Case B (sandwich case, k* = m+1) of the upper bound proof. The proof is now complete.

### Work Done

**Case B: Sandwich Case ($k^* = m+1$)**

The sandwich case occurs when $p_{m+1} \leq 2^m \cdot S \cdot t_m$ but all smaller pieces exceed their thresholds: $p_k > 2^{k-1} \cdot S \cdot t_m$ for $k = 1, \ldots, m$.

**XY's Create-Duplicate Strategy:**

1. **Ratio bound:** From the sandwich conditions, $p_m > 2^{m-1} \cdot S \cdot t_m$ and $p_{m+1} \leq 2^m \cdot S \cdot t_m = 2 \cdot (2^{m-1} \cdot S \cdot t_m) < 2 p_m$. Hence $p_{m+1} < 2 p_m$.

2. **Cut p_{m+1} at position p_m:** Creates pieces $(p_m, p_{m+1} - p_m)$ where $p_{m+1} - p_m < p_m$.

3. **Pair at positions 1-2:** The two copies of $p_m$ are the largest pieces (all others are $< p_m$). They occupy positions 1-2 and cancel: contribution 0 to alternating sum $A$.

4. **Apply P(m-1) to sub-problem:** Pieces $\{p_1, \ldots, p_{m-1}, p_{m+1} - p_m\}$ sum to $S - 2p_m$. By IH, $A_{\text{sub}} \leq (S - 2p_m) \cdot t_{m-1}$.

5. **Algebraic bound:** Verified that $(S - 2p_m) \cdot t_{m-1} \leq S \cdot t_m$ iff $p_m \geq 2^{m-1} \cdot S \cdot t_m$, which is exactly the sandwich condition.

6. **Conclusion:** $A_{\text{total}} = 0 + A_{\text{sub}} \leq S \cdot t_m$. P(m) holds in Case B.

### Reviewer Feedback Addressed

1. **Changed strict to non-strict bounds:** The outline had $(S - 2p_m) \cdot t_{m-1} < S \cdot t_m$ (strict). Fixed to $\leq$ since equality holds at the geometric boundary configuration.

2. **Handled boundary case:** Noted that at exact geometric configuration where $p_k = 2^{k-1} \cdot S \cdot t_m$, we get $p_{m+1} = 2p_m$ exactly (three copies of $p_m$), and the bound becomes equality. This is correct since P(m) requires $A \leq S \cdot t_m$, not strict.

### Status

**solved** - The proof is complete:
- Base case P(1): Verified by exhaustive casework
- Inductive step Case A (k* < m+1): Halve+recurse strategy with ratio > 2
- Inductive step Case B (k* = m+1): Create-duplicate strategy with pair cancellation
- Both lower and upper bounds established
- Final answer: $c(n) = \frac{2^n}{2^{n+1} - 1}$

### Output File

`results/imo-2026-03/approaches/induction-on-n.md`
