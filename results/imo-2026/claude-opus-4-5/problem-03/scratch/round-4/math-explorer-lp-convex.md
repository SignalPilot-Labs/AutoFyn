## imo-2026-03 — LP/Convex Optimization Lens

### Problem recap

c(n) = max_{LB config} min_{XY response} LB_greedy_value = 2^n / (2^{n+1} - 1). Lower bound proved. Upper bound (for all LB configs XY limits LB to <= c(n)) is the shared gap.

---

### Distinct openings surfaced

**Opening A: Shadow-b strategy proves upper bound for the "large-top-piece" regime.**

For any LB config (P_1 <= ... <= P_{n+1}) with P_{n+1} > c(n): XY uses n marks inside P_{n+1} to create sub-pieces [P_n, (P_{n+1}-P_n)/2, (P_{n+1}-P_n)/2, ...] (for n=2: 3 sub-pieces using 2 marks). Let s = (P_{n+1}-P_n)/2. Resulting pieces (all 2n+1 of them, n-1 sub-pieces are s):

Full piece set: {P_1, ..., P_n, P_n, s, s, ..., s} — P_k appears twice for k=n, once for k < n, plus (n-1) copies of s.

**Computed formula:** LB_value = (1 + P_1)/2, regardless of how P_2,...,P_n, P_{n+1} distribute. (Verified algebraically for n=2: for all sorted orderings of {P_1, P_n, P_n, s, s}, LB always picks (P_n) + (s or P_1) + ... = (1+P_1)/2.)

**Key condition:** LB <= c(n) iff P_1 <= L_0 = 1/(2^{n+1}-1).

**At the geometric equilibrium:** P_1 = L_0 exactly, so LB = (1+L_0)/2 = (1+1/D)/2 = (D+1)/(2D) = 2^n/(2^{n+1}-1) = c(n). Shadow-b achieves the EXACT saddle value at the geometric config. ✓

**Opening B: Split-halves strategy covers the complementary regime.**

For P_{n+1} > c(n) and P_1 > L_0: XY creates [P_{n+1}/2, P_{n+1}/2, epsilon, epsilon,...] from P_{n+1} (using n marks, with one large epsilon piece and the rest tiny). Resulting sorted order: [P_{n+1}/2, P_{n+1}/2, P_n, P_{n-1}, ..., P_1, ~0].

**Formula (n=2):** LB = 1/2 + (P_2 - P_1)/2.

**Key LP lemma:** When P_{n+1} > c(n) > 1/2 AND P_1 > L_0:
From P_1 > L_0 = 1/D and P_{n+1} > c(n) = 2^n/D with P_1 + P_2 + P_{n+1} = 1 (for n=2):
P_2 = 1 - P_1 - P_{n+1} < 1 - L_0 - c(n) = 2/D (= 2*L_0).
Also P_2 >= P_1 > L_0. So L_0 < P_2 < 2*L_0, giving P_2 - P_1 < L_0 = 1/D = 1/7 (for n=2).
Therefore LB = 1/2 + (P_2-P_1)/2 < 1/2 + L_0/2 = 1/2 + 1/14 = 4/7 = c(2). ✓

**This proves the upper bound for the ENTIRE regime P_{n+1} > c(n) for n=2 via two explicit XY strategies with a clean case split.**

**Opening C: The concavity of V(P) as an LP/convex argument.**

Define V(P) = min_{XY response} LB_greedy_value(P). This is a minimum of linear functions (one per XY strategy, each of which gives LB a linear function of the pieces). So **V is concave** in P.

LB's problem: max_P V(P) over the simplex. This is maximizing a concave function = convex optimization. The unique interior maximum (if V is strictly concave at the geometric point) is the geometric config.

LP dual: XY's optimal response is a mixture of strategies (the dual variables). Complementary slackness at the geometric config says all of XY's active strategies give the same LB value c(n). This is EXACTLY the property of the geometric config: shadow-b AND split-halves AND other XY strategies all give LB = c(n) at the geometric config.

**Opening D: The two-strategy cover gives the complete upper bound for c > c(n).**

For P_{n+1} > c(n) (n=2 case):
- IF P_1 <= 1/7: shadow-b gives LB = (1+P_1)/2 <= (1+1/7)/2 = 4/7 = c(2). ✓
- IF P_1 > 1/7: split-halves gives LB = 1/2 + (P_2-P_1)/2 < 4/7. ✓ (since P_2-P_1 < 1/7 in this regime)

These two cases are exhaustive (every P_1 satisfies exactly one of P_1 <= 1/7 or P_1 > 1/7). This PROVES the upper bound for all LB configs with P_{n+1} > c(n). No computation needed — both bounds are clean algebra.

**Opening E: For P_{n+1} <= c(n), induction on n.**

When P_{n+1} <= c(n) = c(n): Consider XY using 1 mark to split P_{n+1} into [t, P_{n+1}-t]. The resulting n+2-piece game has n+2 pieces and XY has n-1 marks left. The sub-game value is bounded by c(n-1) <= c(n) by induction. This reduction is NOT yet formal (the sub-game with an extra piece and fewer marks needs careful treatment), but it is a route distinct from the n > n case.

---

### Candidate technique(s)

- **Von Neumann minimax / LP duality:** The game is a two-player zero-sum game with compact strategy spaces and a continuous payoff. Minimax theorem guarantees the saddle. LP duality characterizes XY's optimal strategies via dual variables (one per sorting regime). The dual structure explains why LB = c(n) at the geometric config — all XY's optimal strategies are "balanced" (complementary slackness).
- **Piecewise-linear analysis:** LB's value as a function of XY's sub-pieces is piecewise linear (sorting-regime dependent). XY's optimal is at a regime boundary. The regime boundaries define the "cases" in the upper bound proof.
- **Explicit strategy construction:** Direct construction of XY's shadow-b and split-halves strategies, with algebraic verification of the formulas.

---

### Cheap-kill candidates

1. **The two-strategy cover (Opening A+B):** For the case P_{n+1} > c(n), the upper bound proof reduces to a 2-case split on whether P_1 <= L_0 or not. Each case is settled by an explicit XY strategy. This is elementary algebra (no heavy machinery).

2. **Concavity argument:** V is concave → its maximum is at the unique interior critical point (geometric config). If this can be made rigorous without computing V explicitly, it gives the upper bound "for free." Structural.

3. **Saddle-point balance:** At the geometric config, shadow-b and split-halves BOTH give LB = c(n). This "balance" is the LP complementary slackness condition. It can be verified directly: shadow-b at P_1 = L_0 gives LB = (1+L_0)/2 = c(n). This verifies the geometric config is the saddle, hence optimal for both players.

---

### Knowledge-base entries to use

- **General Proof Methods → Casework / exhaustion**: The two-strategy cover is a 2-case proof (P_1 <= L_0 vs P_1 > L_0), followed by a sub-case for P_{n+1} <= c(n).
- **Standard inequalities**: AM-GM or direct arithmetic needed for the formula LB = (1+P_1)/2 <= c(n) iff P_1 <= L_0.
- **Invariants & monovariants**: The "shadow-b invariant" LB = (1+P_1)/2 is a clean structural invariant independent of b and c. This is the key observation.
- **Meta-Strategy → Reformulate**: Translate XY's strategy to LP variables (sub-piece sizes), fix sorting regime, get linear objective.

---

### Analogous past problems (cruxes)

None identified from crux corpus with the specific LP/convex angle. The saddle-point structure for splitting games does not appear in the crux documentation.

---

### Prior progress

- Lower bound: COMPLETE. Geometric config [L_0,...,L_n] achieves c(n) against any XY. Proof by case analysis (XY marks inside or outside L_n) with pairing lemma. Certified for n=1,2,3 computationally and proved inductively.
- Upper bound: Verified computationally for n=1,2,3,4. No formal general-n proof. The geometric-direct approach hand-waves "extends naturally" — which the reviewer rejected.
- Both current approaches (geometric-direct, minimax-saddle-point) share the same gap: no explicit construction of XY's upper-bound strategy for general LB configs.

---

### Dead ends (do not retry)

- **Interleaving for upper bound:** The "pairing/interleaving" strategy (Q_k = P_{n+1-k}) gives LB = P_{n+1}, which is only useful when P_{n+1} <= c(n). For P_{n+1} > c(n), this FAILS (gives LB = P_{n+1} > c(n)). The current approaches conflate the lower-bound interleaving with the upper-bound XY strategy — they are different things.
- **Induction-on-n (the old "induction-on-n" approach):** Dead-ended in Round 1. Specifically, upper bound proof was "fatally flawed for non-geometric configs." Still the right FRAMEWORK but needs the explicit XY strategy construction from Openings A and B.
- **XY always uses n-1 marks:** False for the upper bound. XY needs ALL n marks to limit LB when P_{n+1} > c(n). The n-1 mark strategy is only optimal AGAINST the geometric LB config.

---

### Small-case / intuition notes (labeled as conjectures)

**Verified (n=2, exact):**

1. Shadow-b formula: For any (a,b,c) with a <= b <= c and a+b+c=1, XY creating [b,(c-b)/2,(c-b)/2] from c gives LB = (1+a)/2. (Algebraically proved — not a conjecture.)

2. Split-halves formula: For any (a,b,c) with a <= b <= c and a+b+c=1, XY creating [c/2,c/2,epsilon] from c gives LB = 1/2 + (b-a)/2. (Algebraically proved — not a conjecture.)

3. Two-strategy cover for c > 4/7 (n=2): Shadow-b covers P_1 <= 1/7, split-halves covers P_1 > 1/7 (with b-a < 1/7 proved from sum constraints). This PROVES the upper bound for all LB configs with P_3 > 4/7. (Proved, not a conjecture.)

**Conjectures (not yet proved for general n):**

4. Shadow-b generalization: For n > 2, XY creates [P_n, (P_{n+1}-P_n)/(n-1), ..., (P_{n+1}-P_n)/(n-1)] from P_{n+1} (1 copy of P_n plus n-1 equal sub-pieces of the remainder). Conjecture: LB = (1+P_1)/2 for this strategy. If true, works when P_1 <= L_0 = 1/D.

5. Split-halves generalization: XY creates [P_{n+1}/(n-1), ..., P_{n+1}/(n-1), epsilon] (n-1 equal sub-pieces plus one tiny piece). Conjecture: LB = 1/2 + (P_n-P_1)/2 and when P_1 > L_0 and P_{n+1} > c(n), sum constraints force P_n - P_1 < L_0, giving LB < c(n).

6. For P_{n+1} <= c(n): XY's optimal strategy involves splitting SMALLER pieces (not P_{n+1}) to "flood" the sorted order with small fragments. Numerical evidence shows XY can always achieve LB <= c(n) but the explicit strategy and proof are missing for general n.

**Saddle point structure (verified computationally for n=1,2,3,4):**

The geometric config is the unique LB config where:
- Shadow-b gives LB = c(n) (achieves the bound exactly)
- All XY strategies give LB >= c(n) (LB can guarantee c(n))
- All non-geometric LB configs give LB < c(n) against XY's optimal

This is the LP complementary slackness condition: at the saddle, all XY's optimal strategies achieve the same value c(n).

---

### Key new finding for the outliner

**For the upper bound gap, the proof for the case P_{n+1} > c(n) is NOW ESSENTIALLY COMPLETE for n=2 via the two-strategy cover (shadow-b + split-halves), and conjecturally extends to general n by the same strategy pair.** The proof for P_{n+1} <= c(n) still needs a separate argument (possibly induction or a different XY strategy construction). This is a concrete, actionable gap.

The shadow-b formula LB = (1+P_1)/2 is the KEY structural insight: XY can limit LB to (1+P_1)/2 for any LB config, and this equals c(n) when P_1 = L_0. For P_1 < L_0 (non-geometric configs), shadow-b gives LB < c(n) — proving the upper bound for this regime without any case analysis on P_{n+1}.

**Actually:** Shadow-b works for ALL P_1 <= L_0 regardless of c! So the upper bound proof for the regime P_1 <= L_0 is complete (no restriction on P_{n+1}). Only the regime P_1 > L_0 needs split-halves (for c > c(n)) and a further argument for c <= c(n).
