## imo-2026-03

**Lens**: upper-bound residual — Regime B2 (general n) and Regime C.

---

### Distinct openings

**Opening 1 — Multilevel partial shadow (recursion on residual, B2 general n)**

The partial-shadow-B1 lemma (CERTIFIED) gives A(F) = A(R'), val ≤ 1−A_1 via k−1 cuts. For B1 (A_1 ≥ 1−c(n)) this closes. For B2 (A_1 < 1−c(n)), the residual R' may itself be B2 with the remaining n'=n−(k−1) cuts. The correct structure is a **recursion on (n, m)**:

- Level-1 PS (k_1−1 cuts): effective R'_1 has A_1'=A_{k_1+1} as largest piece, Σ(R'_1) = 1−2(A_2+…+A_{k_1}).
- If B1(R'_1) := A_{k_1+1}/Σ(R'_1) ≥ 1−c(n'): apply B1-strategy on R'_1 (1 more cut). DONE.
- Else (still B2): apply PS again on R'_1 with n' cuts, recurse.

The recursion terminates because: m decreases by ≥1 per level, n decreases by ≥1 per level. Terminal case: m'=1 or n'=1, both trivially closed (halve the last piece or do nothing).

**Algebraic identity after r levels each with k_i=2**: effective residual = {d_1, d_2, …, d_r, A_{2r+1}, …} where d_i = A_{2i−1}−A_{2i} are adjacent differences of the original pieces (signed differences of consecutive pairs). Each d_i ≤ A_{2i−1}. The final halve (1 cut) leaves A(final) = smallest remaining piece.

**Numerics for n=3, 4-piece B2**: systematic scan over denom=15 confirmed ALL B2 configs achieve minimax val ≤ c(3)=8/15, with 10 configs exactly attaining 8/15. The hardest cases: {6/15, 6/15, 2/15, 1/15}, {6/15, 5/15, 3/15, 1/15}, {6/15, 4/15, 4/15, 1/15}. (Conjecture, not proof.)

**Key test configs for B2 at n=3**:
- easy-k3 (k=3): (0.45, 0.25, 0.20, 0.10). 2 PS cuts → R'={0.10}. 1 halve → A=0. val=1/2. ✓
- hard-k2-high-A2 (k=2): (0.40, 0.32, 0.16, 0.12). 1 PS + 1 B1 → A(full)=0.04 ≤ 1/15. ✓
- hard-k2-tied (k=2): (0.40, 0.21, 0.20, 0.19). d12=0.19=A4. 2 PS levels + 1 halve → A=0.01. ✓ Grid: val=1/2 achievable (cut A1 at A4, halve A3).
- medium-equal (k=2): (0.35, 0.25, 0.20, 0.20). A3=A4. 2 PS levels + 1 halve → A=0. val=1/2. ✓

**Opening 2 — Pairing strategy (non-PS route, works for both B2 and C)**

The grid search reveals that optimal XY cuts always create PAIRS (p_i=p_j). The strategy: identify a set of n cuts that partition the n+1 LB pieces into pairs (possibly after cuts within pieces). If such a pairing exists using ≤ n cuts, val = 1/2 ≤ c(n).

For 4-piece LB {A_1,A_2,A_3,A_4}:
- Cut A_1 at A_4 → {A_4, A_1−A_4}. If A_1−A_4=A_2: pair {A_2, A_2}. Pair {A_4, A_4}. Remaining: {A_3}. Cut A_3 at A_3/2 → pair. val=1/2. Uses 2 cuts.
- More generally: look for a subset of cuts inside A_1 that decomposes A_1 as a sum of other pieces.

The B2 condition A_1 < 1−c(n) = (2^n−1)/D means A_1 has "room" to be decomposed as a sum of smaller pieces within n cuts.

**Opening 3 — Regime C via dominant-piece decomposition**

Regime C: A_1 > c(n). The key: A_1 is LARGE, so XY can spend all n cuts inside A_1 to create many small paired pieces. Specifically:
- Cut A_1 into {A_2, A_3, …, A_m, remainder} using m−1 cuts (each cut matches an existing piece). Pairs {A_i, A_i} for i=2,…,m all cancel. Remaining: {remainder} where remainder = A_1−(A_2+…+A_m) = 2A_1−1. val = (1+(2A_1−1))/2 = A_1.
- val = A_1 ≤ c(n) iff A_1 ≤ c(n). But C is A_1 > c(n)! So this SHADOW strategy gives val=A_1 > c(n). FAILS for C directly.

Wait: C has A_1 > c(n) ≥ 1/2 (since c(n) > 1/2 for n ≥ 2? No: c(n) = 2^n/(2^{n+1}−1) < 1/2). Actually c(n) < 1/2 for all n. So A_1 > c(n) does NOT imply A_1 ≥ 1/2.

Regime C subdivision: A_1 > c(n). Combined with A_1 might be ≥ or < 1/2.
- C ∩ (A_1 ≥ 1/2) = A_1 ≥ 1/2. This IS Regime A from the original classification (Regime A: 1/2 ≤ A_1 ≤ c(n)... wait, but c(n) < 1/2, so A_1 ≥ 1/2 > c(n) means it's C and A is above 1/2).

WAIT. Re-read: Regime A is 1/2 ≤ A_1 ≤ c(n). But c(n) < 1/2! So Regime A CANNOT EXIST? There must be a normalization issue.

Rechecking from certified lemmas: "shadow-regime-A.md" says 1/2 ≤ A_1 ≤ c(n) with c(n) = 2^n/(2^{n+1}−1). For n=1: c(1)=2/3 > 1/2. For n=2: c(2)=4/7 ≈ 0.571 > 1/2. For n=3: c(3)=8/15 ≈ 0.533 > 1/2. So c(n) > 1/2 for ALL n. ✓ The regime A condition 1/2 ≤ A_1 ≤ c(n) is well-defined and non-empty.

So: Regime A (1/2 ≤ A_1 ≤ c(n)) is CLOSED by shadow strategy. Regime C is A_1 > c(n) ≥ 1/2. This means A_1 ≥ 1/2 (since c(n) > 1/2... wait c(n) > 1/2 means A_1 > c(n) > 1/2). Ah yes: c(n) = 2^n/D > 1/2 iff 2^{n+1} > D = 2^{n+1}−1. TRUE. So c(n) > 1/2 and C has A_1 > c(n) > 1/2.

So Regime C pieces: A_1 > c(n) > 1/2. The shadow strategy gives val = A_1 but A_1 > c(n). So shadow alone fails.

XY needs to further reduce: after shadow (k cuts to pair A_2,…,A_k with copies from A_1 cut), val = A_1 > c(n). But with remaining n−k cuts, XY can further reduce from A_1. NOT the shadow direction.

**C strategy from numerics**: For (4/5, 1/15, 1/15, 1/15) (hardest C config found), optimal XY cuts are [1/15, 2/15, 7/15] (approximately). These correspond to: cut A_1 at 1/15, creating {1/15, 14/15−…}. Pair {A_2=1/15, new 1/15}. Continue.

Pattern for C: XY uses n cuts inside A_1 to CHOP it into n+1 pieces matching/pairing with A_2,…,A_{m}. After pairing, the residual from A_1 has size A_1−Σ(A_2+…+A_m) + (pair adjustments). For A_1 > c(n): 

Σ(A_2+…+A_m) = 1−A_1 < 1−c(n). Shadow approach: cut A_1 into {A_2, A_3, …, A_m, r} where r=A_1−(1−A_1)=2A_1−1. All A_i pair. Remaining: {r=2A_1−1}. A=2A_1−1. val=(1+(2A_1−1))/2=A_1. Still A_1 > c(n).

**So the shadow strategy does NOT solve Regime C**. Regime C requires a genuinely different approach from the certified shadow-regime-A.md strategy (which applies only when A_1 ≤ c(n)).

Wait: shadow-regime-A.md says A is 1/2 ≤ A_1 ≤ c(n). So Regime A ≠ Regime C. C is A_1 > c(n).

The CORRECT STATUS: Regime C is entirely open. It includes the configurations where A_1 > c(n) (e.g., A_1 = 9/15 for n=3). The n=2 case of C was closed separately (reviewer-checked). General n C is OPEN.

**Opening for C**: For C (A_1 > c(n)), XY has a 2-stage strategy:
- Stage 1: use ~m−1 cuts to match A_2,…,A_m from inside A_1 (creating pairs). After this, A_1 becomes r = A_1−(A_2+…+A_m) = 2A_1−1. Uses m−1 cuts. Residual: {r} alone.
- Stage 2: with n−(m−1) leftover cuts, halve r, halve again, etc. Each halve halves A: r → r/2 → r/4 → … After n−m+1 halvings: A = r/2^{n−m+1}.
- Need A ≤ 1/D: r/2^{n−m+1} ≤ 1/D. Since r=2A_1−1 and A_1 ≤ 1: r ≤ 1. Need 1/2^{n−m+1} ≤ 1/D=1/(2^{n+1}−1). Since D<2^{n+1}, this holds when n−m+1 ≥ n+1 i.e. m ≤ 0. IMPOSSIBLE.

So stage-2 halvings don't give 1/D bound directly. Different analysis needed.

The correct C approach (from grid search analysis): cuts inside A_1 create pieces that pair with EACH OTHER (not just with A_2,…,A_m). After binary halving of A_1 using n cuts: A_1 → 2^n equal pieces of A_1/2^n each, all pairing. Then A = A_1 from the now-isolated {A_2,…,A_m} multiset. Need A({A_2,…,A_m}) ≤ 1/D. Since Σ(A_2+…)=1−A_1 < 1−c(n): A({A_2+…}) ≤ 1−A_1 < 1−c(n). Need 1−c(n) ≤ 1/D. Is 1−c(n) ≤ 1/D? 1−c(n) = (D−2^n)/D = (2^n−1)/D = c(n)/2^n × (2^n−1)... 1−c(n)=(2^n−1)/D >> 1/D for large n. NO.

So binary halving of A_1 also fails. The C problem is GENUINELY HARD.

**Opening 4 — Bypass B2 and C via S1 (extremal smoothing)**

The extremal-smoothing approach reduces the entire upper bound to S1: "G_n is the unique maximizer of V on Δ." If S1 holds, then for any non-geometric A ∈ Δ, V(A) < c(n), and the upper bound follows. This bypasses both B2 and C entirely. However, S1 has been stuck for 3+ rounds with no mechanism. NOT RECOMMENDED as primary route.

---

### Candidate technique(s)

- **Multilevel partial shadow** (recursion on n and m): apply the PS lemma iteratively to the residual. Terminates because (n, m) decreases at each level. The algebraic chain: A(final) = f(differences of adjacent original pieces), bounded via B2 condition.
- **Pairing strategy**: find n cuts that create n pairs from the n+1 LB pieces (after cuts). Works via existence argument: the B2 condition guarantees A_1 can be decomposed within n cuts to pair with A_2,…
- **Binary splitting / geometric halving inside A_1** for Regime C: cut A_1 into 2^n equal pieces using n cuts. But as shown above, this doesn't directly close C; needs supplementary analysis.
- **Induction on m+n**: joint induction where each level reduces m or n by at least 1.

---

### Cheap-kill candidates

- **B2 sub-case k≥3 (A_2+A_3 ≤ A_1)**: single PS level (2 cuts) + 1 halve → A(full) = A_3−A_4 ≤ A_3 ≤ A_2 ≤ A_1 ≤ 1−c(n) < 1/2. But need A_3−A_4 ≤ 1/D; not obvious. However, for k≥3: Σ(R')=1−2A_1+2s with s=A_1−(A_2+A_3) ≥ 0. A(R') ≤ 1−2A_1. Halving R' once: A ≤ (1−2A_1)/2 = 1/2−A_1. Need 1/2−A_1 ≤ 1/D: A_1 ≥ 1/2−1/D = (D−2)/(2D). For n≥2: (D−2)/(2D) = (2^{n+1}−3)/(2(2^{n+1}−1)) ≈ 1/2. Actually 1/2−1/D = (D−2)/(2D). For n=3: (15−2)/30 = 13/30 ≈ 0.433. And B2 requires A_1 < 7/15 ≈ 0.467. So for A_1 ∈ [13/30, 7/15], k≥3 sub-case closes with 3 cuts. For A_1 < 13/30: need more halvings or different strategy. **Partial cheap kill**: k≥3 with A_1 large enough in B2.
- **A_2 = A_3 (tied second pieces)**: {A_2,A_3} pair automatically. Reduces to m−2 effective pieces with n cuts. Immediate reduction.
- **m ≤ 2 (degenerate)**: 1 cut makes both pieces equal → A=0. val=1/2 ≤ c(n). Trivial.

---

### Knowledge-base entries to use

- **Extreme value theorem** (already used in extremal-framework.md)
- **Pairing/cancellation** (parity-invisible pairs, LB Lemma M0 integral form) — core of all strategies
- **Divide-and-conquer / recursion** (induction on n with explicit recursive structure)
- **Greedy algorithm** (PS level selection: always pair the largest piece with the next available match)

---

### Analogous past problems (cruxes)

None identified via crux corpus that directly map to a multilevel pairing strategy for a minimax game. The closest analogues are stick-cutting / alternating-sum decomposition problems, but none found in prior rounds.

---

### Prior progress

- Regime A (1/2 ≤ A_1 ≤ c(n)): CLOSED, shadow strategy, certified.
- Regime B1 (1−c(n) ≤ A_1 < 1/2): CLOSED all n, partial-shadow, certified.
- Regime B fully closed at n=2 (B1+B2a+B2b, reviewer-checked).
- Extremal framework: V continuous, max attained, replica bound V(G_n)=c(n). Certified.

---

### Dead ends (do not retry)

- **S1 (G_n unique maximizer)**: 3+ rounds stuck, no algebraic mechanism. Skip.
- **Greedy potential-decrease XY**: confirmed dead-end (stalls A≈0.287 vs target 0.143).
- **Sub-induction via c(n−1)**: c(n−1)=(2^{n−1})/(2^n−1) > c(n); the bound from one fewer cut is too weak.
- **Shadow strategy for Regime C**: gives val=A_1 > c(n). Strictly fails.
- **Single-level PS+B1 for k=2**: A_full=2A_1+2A_4−1, can exceed 1/D (fails ~22% of B2 configs for n=3).
- **Binary-halving A_1 for C**: A_full = A({A_2,…,A_m}) ≥ 1−A_1−... not bounded by 1/D.

---

### Small-case / intuition notes (all conjectural, not proved)

**B2 recursion terminates (conjecture)**: multilevel PS terminates in ≤ n cuts for any B2 config with n pieces. Evidence: all denom=15 B2 4-piece configs at n=3 satisfy val ≤ c(3), verified by grid search. The hardest configs achieve val = c(3) exactly at the tight configs.

**Tight B2 configs (conjecture)**: the configs achieving val=c(3) at n=3 include {6/15,6/15,2/15,1/15}, {6/15,5/15,3/15,1/15}, {6/15,4/15,4/15,1/15}. These have A_1+A_4 ≈ 7/15 or specific arithmetic relationships.

**Regime C is harder than B2 (observation)**: C configs can achieve val=c(n) (tight), e.g., {4/5,1/15,1/15,1/15} (val=8/15 at n=3). The strategy involves cutting inside A_1 to create pairs with the many small pieces. The pieces in C tend to be very unequal (one large, rest tiny), so XY cuts A_1 progressively to match each small piece.

**C strategy candidate (conjecture)**: for A_1 > c(n) with (n+1) pieces: XY uses the following n cuts inside A_1 to create pairs: cut A_1 at A_2, then at A_2+A_3, …, then at A_2+…+A_m. This is the SHADOW strategy of the shadow-regime-A.md extended to m cuts. After m−1 cuts: {A_2,…,A_m,r} from A_1. A=r=2A_1−1. With remaining n−m+1 halvings: A ≤ (2A_1−1)/2^{n−m+1}. For the tight case {9/15, 3/15, 2/15, 1/15}: 2A_1−1=3/15, n−m+1=0 halvings. A=3/15 > 1/15. FAILS. So more halvings needed for C with many small pieces.

**Alternative C strategy (from grid search)**: XY cuts INSIDE A_1 at {A_4, A_4+A_3, A_4+A_3+A_2}={1/15, 3/15, 6/15} for {9/15,3/15,2/15,1/15}. Creates pieces {1/15, 2/15, 3/15, 3/15} from A_1 plus {3/15,2/15,1/15} from others. {3/15,3/15} pair, {2/15,2/15} pair, {1/15,1/15} pair. Remaining: {3/15 from A_1's largest piece}... wait, need to recount. (This case is C-tight with val=8/15=c(3) from above, achieved by some strategy.)

**B2 ALGEBRAIC CORE (conjecture)**: For B2 with 4 pieces at n=3, the multilevel PS strategy yields A(final) = min(A_1−A_2, A_3−A_4) when A_4 ≥ A_1−A_2, or A(final) = |A_2+A_3−A_1−A_4| otherwise. These are ≤ 1/D in the B2 regime by the combinatorial structure of the pieces. Verified numerically for all denom=15 cases.

**Key identity for 2-level PS + final halve** (proved for specific cases, conjectured general):
A(final) ≤ |A_1−A_2−A_3+A_4| for 4-piece B2 configs.
And |A_1−A_2−A_3+A_4| ≤ 1/D iff A_2+A_3−A_1−A_4 ≤ 1/D, i.e., the "inner alternating sum" is small. This is NOT always true (the bound needs a more careful PS-level analysis).

**BOTTOM LINE**: The correct proof for B2 general n is a recursion on m and n. Each PS level uses 1 cut and reduces m by 1 while maintaining the B2/B1 condition on the residual. After at most m−1 levels (using m−1 cuts ≤ n cuts since m ≤ n+1), the residual is a single piece. The final halve uses 1 cut. The algebraic claim: the single residual piece has size ≤ 1/D (provable from the original B2 condition A_1 < (2^n−1)/D). This is the KEY FORMULA the outliner needs to establish.
