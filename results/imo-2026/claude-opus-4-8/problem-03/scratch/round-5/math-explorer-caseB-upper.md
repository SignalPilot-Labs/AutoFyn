## imo-2026-03 — Case-B Upper Bound: Hard-Regime Terrain

### Context

The upper-bound wall (GAP U1) is now confined to: **p = n+1 pieces, all a_i > 1/D, all consecutive gaps > 1/D** (the "hard regime"). The certified reductions (Lemma H = Case A; Reduction 1 = p <= n; Reduction 2 = min gap <= 1/D) close everything else. The open sub-cases are:

- **B1-large**: a_1 > c(n) = 2^n/D. XY halves a_1 (1 cut), reducing to **IH(q)**: q = p-1 pieces b_1 >= ... >= b_q, all > 1/D, S = sum(b_i) < (2^q - 1)/D, q-1 cuts, target A <= 1/D. Proved for q = 1, 2, 3; **open for q >= 4**.
- **B2**: a_1 <= 1/2. No dominant piece. XY has n cuts for n+1 pieces all > 1/D. **Open for all n >= 2**.

---

### Distinct openings

**Opening 1: Dyadic-tier halving induction for IH(q)**

The correct inductive structure for IH(q) is NOT "always pair-create at adjacent piece values" (that fails: after cutting b_1 at b_2, the residual sum S - 2*b_2 can exceed (2^(q-1)-1)/D). Instead, use a **dyadic-tier split**:

- **CASE A (b_1 > 2^(q-2)/D)**: Halve b_1 (1 cut). The pair {b_1/2, b_1/2} cancels in XOR. The remaining q-1 pieces {b_2,...,b_q} have sum S - b_1 < (2^q-1)/D - 2^(q-2)/D = (2^(q-1) - 1)/D, so they satisfy IH(q-1) with q-2 cuts. This is a clean induction (verified for q=4 with b_1 = 7.7/D, halving gives IH(3) on {3.3,2.2,1.1}/D, sum 6.6/D < 7/D ✓).
- **CASE B (b_1 <= 2^(q-2)/D)**: ALL q pieces are <= 2^(q-2)/D. Sum S < 2^(q-2)/D * q ... but also S < (2^q-1)/D. In this case the pieces are "small" relative to the dyadic scale. Need a different move — see Opening 2.

The Case A argument is CLEAN and gives a VALID inductive step for all q: **prove IH(q) in Case A by halving b_1, applying IH(q-1) to the rest**. The gap is Case B.

**Opening 2: Multiple halvings and XOR collapse in Case B of IH(q)**

When all q pieces satisfy b_i <= 2^(q-2)/D (Case B above), the pieces are ALL in the "lower half" of the dyadic range. This means the largest piece b_1 is not dominant enough to halve-and-reduce. The correct strategy appears to involve halving 2 or more pieces simultaneously.

Computational probing (q=4, triple-hard with uniform gaps g = 1.1/D): the OPTIMAL strategy achieves A = 0 in just 2 cuts: (i) halve b_1, (ii) cut b_2 at b_4. After these 2 cuts, the 6 resulting pieces form 3 equal pairs {b_1/2, b_1/2}, {b_4, b_4}, {b_2-b_4, b_3}, all canceling (for uniform gaps: b_2-b_4 = g_2+g_3 = 2g = b_3 when g2=g3). For non-uniform gaps, A = |b_2-b_4-b_3| = |g_2 - b_4|, which can exceed 1/D.

**The right strategy in Case B is adaptive**: XY halves b_1 (reducing to IH(q-1) on {b_2,...,b_q}) if that sum is < (2^(q-1)-1)/D; else XY must make TWO pair-creating cuts that together leave a residual < 1/D. The sum bound S < (2^q-1)/D provides the slack but it is TIGHT (equality at the dyadic config {2^0,...,2^{q-1}}/D).

Key: for the IH(q) DYADIC CONFIG {b_k = 2^{q-k}/D}, the standard cascade (b_1 at b_2, residual at b_3, ...) achieves A = 1/D exactly in q-1 steps. This saturates the bound, confirming the approach is tight.

**Opening 3: B2 via the "excess-1/D" reduction**

B2 has p=n+1 pieces, S=1=(D)/D (the TIGHT bound, not <). This is why B2 can't reduce to IH(n+1) (which needs S < (D-1)/D). 

ONE PROMISING MOVE: XY makes ONE precision cut first, cutting some piece a_k at a_k - (a_k - c(n)) to create a singleton of size c(n) = 2^n/D. After this 1 cut, the remaining n pieces have sum = 1 - c(n) = (D-2^n)/D = (2^n-1)/D = (2^n-1)/D. **This is exactly the IH(n) bound!** Provided all n remaining pieces are > 1/D and their sum < (2^n-1)/D, IH(n) applies with n-1 cuts. Together: 1 + (n-1) = n cuts total. Final A = c(n) from the precision singleton.

Wait — but c(n) = 2^n/D > 1/D, so A = c(n) is TOO LARGE. The target is A <= 1/D. This doesn't give A <= 1/D.

**CORRECTED**: The precision cut should produce a singleton of 1/D (not c(n)). Cut a_k at a_k - 1/D, creating singleton 1/D. Remaining: n pieces with sum 1 - 1/D - a_{n+1} (if the cut is on piece a_k ≠ a_{n+1}). For IH(n) to apply: sum_remaining < (2^n-1)/D. This requires a_{n+1} > 1 - 1/D - (2^n-1)/D = (D-1-(2^n-1))/D = (D-2^n)/D = (2^n-1)/D. Again a_{n+1} > (2^n-1)/D = c(n)... impossible for small pieces.

**CONCLUSION**: The 1/D-singleton precision cut does NOT give a clean reduction for B2. B2 requires a more global strategy.

**Opening 4: B2 via halving the n largest and the cascade below**

In B2: p=n+1 pieces in (1/D, 1/2]. XY halves the TOP n-1 pieces (n-1 halvings), canceling n-1 pairs. Remaining pieces: {a_n, a_{n+1}} with 1 cut left. One cut (pair-creation): cut a_n at a_{n+1}, leaving A = a_n - a_{n+1} = the n-th consecutive gap. In the hard regime, this gap > 1/D. FAILS.

**Alternate**: Halve the top n-2 pieces (n-2 halvings), leaving {a_{n-1}, a_n, a_{n+1}} with 2 cuts. IH(3) on these 3 pieces: need sum < 7/D. Sum = a_{n-1}+a_n+a_{n+1} = 1 - (a_1+...+a_{n-2}) = 1 - (something close to (n-2)/2). For large n: this is large. FAILS in general.

**THE RIGHT FRAME FOR B2**: The machine confirms A=0 is achievable with 3 cuts for n=3 B2 hard regime (example: a={7/19.3, 5.5/19.3, 4/19.3, 2.8/19.3}). But the strategy requires cutting at COMPUTED values (not piece values). The correct structure may be a **linear programming argument**: with n cuts and n+1 pieces all > 1/D summing to 1, the set of achievable XOR measures is an interval [0, max_A]. Prove the lower endpoint is 0 (or <= 1/D) by a combinatorial/affine argument.

**Opening 5: A unified IH(q) argument via the XOR CHAIN / Euclidean cascade**

The cascade (cut b_1 at b_2, residual r_1 at b_3, etc.) gives final A = || ... |b_1-b_2| - b_3| ... - b_q|. This is the "Euclidean algorithm XOR chain". For the DYADIC config it gives A = 1/D exactly (machine verified: 8-4=4, 4-2=2, 2-1=1 in /D units). 

**CONJECTURE** (not proved): For ANY q pieces with sum S < (2^q-1)/D and all b_i > 0, the Euclidean cascade gives final residual A <= 1/D. This would prove IH(q) for all q. The obstacle: the Euclidean cascade gives A = | ||b_1-b_2|-b_3|...-b_q|, which depends on the SPECIFIC VALUES and doesn't obviously satisfy A <= 1/D just from the sum bound.

**What makes it work for q=1,2,3**: The key is that the sum bound S < (2^q-1)/D is TIGHT at the dyadic config, and the dyadic cascade achieves A = 1/D exactly. For any OTHER config (with the same sum constraint), the cascade gives A < 1/D (machine-verified for n <= 4 at 10^6 configs). A PROOF that the dyadic config MAXIMIZES the cascade residual A (over the IH(q) feasible region) would close IH(q) for all q.

---

### Candidate technique(s)

1. **Dyadic induction on the tier of b_1** (Opening 1): When b_1 > 2^(q-2)/D, halve it and apply IH(q-1). When b_1 <= 2^(q-2)/D, all pieces are in the "small" regime — need Opening 2.
2. **Euclidean-chain maximization** (Opening 5): Prove the cascade residual is maximized at the dyadic config (b_k = 2^{q-k}/D), where it equals 1/D. An extremal/convexity argument might work.
3. **Fragment-count induction** (Opening 2): Use N_q(2^j/D) <= 2^(q-j)-1 (same as the lower-bound dyadic count) to structure a piece-cancellation induction within each tier.

---

### Cheap-kill candidates

- **IH(q) CASE A is PROVED** (b_1 > 2^(q-2)/D): halve b_1, reduce to IH(q-1). This closes roughly HALF of all hard-regime IH(q) instances. If the outliner proves IH(q) just for Case A and separately handles Case B of IH(q), the induction may close entirely.
- **Gap-closing pigeonhole for B2**: In B2 hard regime (all gaps > 1/D), with n+1 pieces summing to 1: sum of n consecutive gaps = a_1 - a_{n+1}. Total "gap budget" = sum of ALL n consecutive gaps = a_1 - a_{n+1} <= 1/2 (since a_1 <= 1/2). Average gap <= 1/(2n). For large n, MOST gaps are < 1/D... but not all.

---

### Knowledge-base entries to use

- **Casework / exhaustion**: Split IH(q) into Case A (b_1 > 2^(q-2)/D) and Case B (b_1 <= 2^(q-2)/D). Case A closes by induction. Case B needs separate analysis.
- **Induction** (standard and strong): IH(q) -> IH(q-1) via Case A halving is a clean strong induction step. The base cases IH(1,2,3) are proved.
- **Invariants & monovariants**: The XOR chain / Euclidean cascade is a monovariant (residual decreases). Formalizing the decrease is the open step.
- **Pigeonhole**: Fragment-count bound N_q(2^j/D) <= 2^(q-j)-1 is the load-bearing combinatorial bound.

---

### Analogous past problems (cruxes)

- **aimo-0262 (Cinderella/Stepmother capacity game)**: Crux = "hand the defender a self-reproducing invariant family; after each adversary move, restore it." Analogous to IH(q): XY maintains an invariant (XOR measure bounded) through each cut. The Cinderella invariant is a SPECIFIC configuration condition that re-establishes itself. For IH(q), the analog is: after XY's cut, the remaining pieces satisfy IH(q-1). Cinderella uses ADJACENT bucket structure; IH(q) uses DYADIC TIER structure. The self-reproducing invariant is the key.
- **aimo-0012 (bin-packing, 2n-1 groups)**: Crux = "find a mergeable pair by pigeonhole on consecutive pair-sums, fuse it, induct on reduced count." Direct structural analog: for IH(q), find a "mergeable pair" (b_i, b_j) with b_i - b_j < 1/D (Reduction 2) or a "dominant piece" b_1 > 2^(q-2)/D (Case A). When NEITHER holds... the aimo-0012 proof breaks similarly. The resolution in aimo-0012 uses AVERAGING on pair-sums; for IH(q), the analog is the sum bound S < (2^q-1)/D.
- **aimo-0117 (dyadic assignment game)**: Crux = "assign played values as a geometric (dyadic) sequence so the largest strictly exceeds the sum of all others." This is EXACTLY the structure of IH(q): the dyadic config b_k = 2^{q-k}/D has each piece exceeding the sum of all smaller pieces by 1/D (the dominance identity). The aimo-0117 strategy is "play next unused power of two"; for IH(q), the natural analog is "halve the top piece at each step."

---

### Prior progress

- IH(1), IH(2), IH(3): proved rigorously (from §6.2 of direct-constructive).
- IH(q) CASE A (b_1 > 2^(q-2)/D): a CLEAN proof exists (halve b_1, S-b_1 < (2^(q-1)-1)/D, apply IH(q-1)). **This was NOT written before; it closes one half of the induction step.**
- B2: machine-verified A <= 1/D for n <= 5, but no explicit strategy.

---

### Dead ends (do not retry)

- **Standard pair-creation cascade alone** (cut b_1 at b_2, residual at b_3, etc.): FAILS as an inductive argument because after cutting b_1 at b_2, the residual sum S - 2*b_2 exceeds (2^(q-1)-1)/D (since b_2 can be as small as 3/D which is < 2^(q-2)/D for q >= 4).
- **Menu/one-cut-per-piece strategy (Lemma M)**: REFUTED by the reviewer (n=3 counterexample in lemmas/CaseB-reductions.md). Do not revisit.
- **n -> (n-1) game-separation induction**: refuted Round 2 (XY budget doesn't decrement; odd-sum is a global functional).
- **Halving all n pieces in B2** (leaving the smallest piece as the singleton): the singleton has size a_{n+1} > 1/D in the hard regime. FAILS.
- **1/D-singleton precision cut for B2**: creates a 1/D piece but the IH(n) sum bound on the remaining pieces requires a_{n+1} > c(n), which fails for small a_{n+1}.

---

### Small-case / intuition notes

- **IH(4) dyadic cascade**: b = {8,4,2,1}/D gives final A = 1/D after 3 cuts (8->4, 4->2, 2->1). This is the TIGHT CASE (equality in IH(q) bound S = 15/D and A = 1/D). All other configs with S < 15/D appear to give A <= 1/D (machine: 0 failures over 10^6 configs, per the current approach file).
- **IH(4) Case A proof** (CONJECTURE, not yet written up): When b_1 > 8/D, halving b_1 leaves S' = S - b_1 < 15/D - 8/D = 7/D with q-1=3 pieces, satisfying IH(3). This is a clean argument. The case b_1 <= 8/D requires a different move.
- **B2 hard regime**: Machine confirms A=0 achievable with 3 cuts for n=3 (uniform-gap example, sum=1). The strategy involves cuts at non-piece-value positions (e.g., cut at 2*b_j for some j). The structure: piece b_k is cut at a COMPUTED value so the residual exactly cancels with another piece under the XOR. No unified explicit strategy found yet.
- **CRITICAL STRUCTURAL OBSERVATION**: IH(q) for q pieces with S < (2^q-1)/D is SELF-SIMILAR to the original problem (n+1 pieces, S=1=(D)/D). The IH(q) sum bound (2^q-1)/D is the geometric sequence sum, exactly as in the LB geometric construction. This self-similarity suggests the right induction tracks the BINARY WEIGHT of the largest piece — the same dyadic structure as the lower-bound's interleaving analysis. (Labeled as conjecture / structural insight.)
- **Minimum of cascade residual**: Numerical evidence (n=2..5, random sampling) confirms min_Δ A = 1/D in the IH(q) hard regime — achieved at the DYADIC CONFIG. This makes the Euclidean cascade tight but doesn't give a proof.
