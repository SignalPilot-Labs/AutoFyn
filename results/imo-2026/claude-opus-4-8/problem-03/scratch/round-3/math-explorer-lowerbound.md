## imo-2026-03 — Lower-Bound Case 2 Gap (Lemma LL / GAP AL)

**Lens:** sharper tools for the Q–R interaction in the A(Q)>0 sub-case.

---

### Problem recap for this gap

Induction on n. LB plays G_n = {2^0, 2^1, ..., 2^n} (geometric config). XY cuts the largest piece 2^n into parts forming multiset Q (t+1 ≥ 2 parts, so t ≥ 1 cuts) and refines the remainder G_{n-1} into R with val(R) ≥ 2^{n-1} by IH (n-t cuts left for R). Must show val(Q ∪ R) ≥ 2^n, equivalently A(Q∪R) ≥ 1 (since T(Q∪R) = 2^n + T(R) = 2^{n+1}-1 in the D=2^{n+1}-1 normalization and val = (T+A)/2, so val ≥ 2^n iff A ≥ 1).

Merge formula: A(Q∪R) = A(Q) + A(R) - 2B where B = measure{x : N_Q(x) odd AND N_R(x) odd}.

Sub-case A(Q)=0 is CLOSED (merge lemma gives A(Q∪R) ≥ A(R) - A(Q) = A(R) ≥ 1).

Sub-case A(Q)>0 is OPEN — merge lemma alone gives A(Q∪R) ≥ |A(Q)-A(R)| which can be < 1.

---

### Case B (t=1): CLEAN PROOF FOUND

When XY uses exactly 1 cut on 2^n, producing Q = {q, 2^n - q} with q ≤ 2^{n-1}:
- The Q-odd region is the single interval (q, 2^n - q), so A(Q) = 2^n - 2q.
- Key formula: A(Q∪R) = A(Q) + A(R) - 2B = (2^n - 2q) + A(R) - 2 · measure{x ∈ (q, 2^n-q) : N_R(x) odd}.
- Since measure{x ∈ (q, max(R)] : N_R(x) odd} ≤ max(R) - q (trivial: the R-odd region inside [q, max(R)] has measure at most the interval length), and N_R(x)=0 for x > max(R) (so R-odd region above max(R) is empty):
  - B ≤ max(R) - q.
  - Since max(R) ≤ 2^{n-1} (R is a refinement of G_{n-1}, so all R-pieces ≤ 2^{n-1}):
  - A(Q∪R) ≥ (2^n - 2q) + A(R) - 2(max(R) - q) = 2^n - 2·max(R) + A(R).
  - Since max(R) ≤ 2^{n-1} and A(R) ≥ 2·max(R) - 2^{n-1} + 1... wait, simpler:
  
  Actually split into two sub-cases:
  - If max(R) ≤ q: B = 0 (no R-odd region above q), so A(Q∪R) ≥ A(Q) + A(R) - 0 = (2^n - 2q) + A(R) ≥ 0 + A(R) ≥ 1. ✓
  - If max(R) > q: B ≤ max(R) - q, so A(Q∪R) ≥ (2^n - 2q) + A(R) - 2(max(R) - q) = 2^n - 2·max(R) + A(R). Since max(R) ≤ 2^{n-1}: A(Q∪R) ≥ 2^n - 2^n + A(R) = A(R) ≥ 1. ✓

This is a **complete rigorous proof for Case B** (t=1, all Q-pieces ≤ 2^{n-1} is not even needed — Q = {q, 2^n-q} with q ≤ 2^{n-1} automatically satisfies max(Q) = 2^n - q ≥ 2^{n-1}).

The key insight: the Q-odd region has a simple interval form when t=1, and the only dangerous overlap with R-odd region is bounded by max(R) ≤ 2^{n-1}.

---

### Case A (t≥2): OPEN — analysis of the difficulty

When XY uses t ≥ 2 cuts on 2^n, all Q-pieces are ≤ 2^{n-1} (since 2^n split into ≥3 parts each ≤ 2^{n-1}, assuming XY doesn't make pieces larger than half, which follows from A(Q)>0 requires at least one Q-piece > 2^{n-1}/... wait, actually pieces can be anything).

For Case A where A(Q) > 0 and t ≥ 2:
- The merge lemma gives A(Q∪R) ≥ A(R) - A(Q) which is < 1 when A(Q) ≥ A(R).
- Tight example (n=3, D=15): Q={3,3,2}, A(Q)=2, R={2,2,2,1} (refinement of G_2={1,2,4}→refine 4 into {2,2}), A(R)=1, val(Q∪R)=8 exactly (tight). Here A(Q)-A(R)=1, so merge lemma gives A(Q∪R) ≥ |1-2| = 1. The merge lemma IS sufficient at this tight config.
- Near-tight counterexample to |A(Q)-A(R)| ≥ 1: Q={199/100, 201/100}, R= some refinement with A(R)=3/2, gives |A(Q)-A(R)| = 1/2 < 1. But val is still ≥ 2^n because B is small (the Q-odd and R-odd regions don't overlap much).

So the gap: for Case A configs where |A(Q)-A(R)| < 1, we need to show B is small enough. The challenge is: B = measure{Q-odd AND R-odd}, and when A(Q) is large (Q-odd region wide), and A(R) is also large (R-odd region wide), the overlap B could in principle be large too.

---

### Distinct openings for Case A

**Opening 1: Induction on t (undo one cut).**
If XY uses t ≥ 2 cuts, pick one Q-cut that "closed" the most dangerous interval; removing it reduces to t-1 cuts on Q' (a coarser partition) and n-t+1 cuts on R. The key: removing a cut from Q either (a) merges two Q-pieces, changing A(Q) by at most 2·min(merged pieces), or (b) doesn't change A much. Specifically: merging two adjacent Q-pieces q_i, q_{i+1} into q_i+q_{i+1} changes A(Q) by -(q_i - q_{i+1}) if i is odd (decreases) or +(q_i - q_{i+1}) if i is even. The removed cut frees up one XY cut for R, so R can be refined further. This is a "trading cuts" argument: giving XY fewer cuts on Q and more on R can only help XY (let them refine R better) — so if we prove val ≥ 2^n for t-1 cuts on Q (by induction on t), and adding one more cut to Q can't reduce val below 2^n... but that direction is backwards (we need to show the t-cut case implies the (t-1)-cut case by merging a Q-cut).

Actually the right direction: "merging one Q-cut only decreases A(Q)" (if the merged pair was contributing positively to A). This means A(Q') ≤ A(Q) + something. Unclear if this helps directly.

**Opening 2: Direct formula for A(Q∪R) using the interval structure of Q-odd region.**
When all Q-pieces ≤ 2^{n-1}, the Q-odd region {x : N_Q(x) odd} is a union of intervals entirely below 2^{n-1} (since all Q-pieces ≤ 2^{n-1}). The R-odd region is also below max(R) ≤ 2^{n-1}. Both Q-odd and R-odd regions live in [0, 2^{n-1}].

Now A(Q∪R) = A(Q) + A(R) - 2B where B ≤ min(A(Q), A(R)).

The key bound needed: B ≤ (A(Q) + A(R) - 1)/2, i.e., A(Q) + A(R) - 2B ≥ 1.

Can we show the Q-odd and R-odd regions can't BOTH be large on the same set? If Q-odd region is large (A(Q) large), that means many Q-pieces are in alternating positions, suggesting the Q-odd region covers a substantial portion of [0, 2^{n-1}]. But the R-odd region is controlled by the IH structure of G_{n-1}.

**Opening 3: Exploit the G_{n-1} structure of R.**
R is a refinement of G_{n-1} = {2^{n-1}, 2^{n-2}, ..., 2, 1} (or rather a multiset with the same total 2^{n-1}-1 that arises from refining G_{n-1} pieces). The crucial property: G_{n-1} has the "domination" structure where 2^k > sum of all smaller, giving A(G_{n-1}) = 1 exactly. Any refinement keeps T(R) = 2^{n-1}-1 (unnormalized) but can have val(R) ≥ 2^{n-1} by IH.

Key structural fact: the R-odd region lives in [0, 2^{n-1}). The maximum R-odd measure is A(R) ≤ max(R) ≤ 2^{n-1}.

The R-odd region has a very special structure coming from the geometric config: G_{n-1} has R-odd region = {x : floor(log_2(x)) even} roughly — actually G_{n-1} = {2^{n-1}, 2^{n-2},...,1} which has N_{G_{n-1}}(x) = n+1-k for x ∈ [2^{k-1}, 2^k), and odd counts correspond to specific dyadic intervals. This dyadic interval structure may constrain B.

**Opening 4: Monotonicity / continuity of val(Q∪R) as Q is varied.**
For fixed R, as Q is varied continuously (keeping T(Q)=2^n and t cuts), val(Q∪R) is a piecewise-linear function of the cut positions. Its minimum occurs at a vertex (all Q-pieces equal or some equal to 0). Can we show that val is minimized when A(Q)=0?

Computationally for n=3, the minimum of val(Q∪R) over all valid (Q,R) pairs is exactly 8=2^3, and this minimum is achieved in Case A at Q={3,3,2}, R={2,2,2,1} where A(Q)=2>0. So the minimum is NOT at A(Q)=0 for Case A (which would be Q equal pieces). This means we can't reduce Case A to A(Q)=0 via a monotonicity argument.

However: the joint minimum over ALL cases (including Case B) occurs with A(Q)>0, and the minimum value IS exactly 2^n. So the bound is tight — any proof must be tight.

**Opening 5: Compare Q∪R to a "reference" multiset with known value ≥ 2^n.**
The Lemma G (greedy = odd-index) applies to any multiset. For Q∪R, we need val ≥ 2^n. 

Observation: val(Q∪R) = (T(Q∪R) + A(Q∪R))/2. T(Q∪R) = 2^n + T(R) = 2^n + (2^{n-1}-1) = 3·2^{n-1}-1. So val ≥ 2^n iff A(Q∪R) ≥ 2^n - (3·2^{n-1}-1) - wait, let me recompute: val = (T+A)/2 ≥ 2^n iff T+A ≥ 2^{n+1}, iff A ≥ 2^{n+1} - T = 2^{n+1} - (2^n + 2^{n-1}-1) = 2^{n-1}+1. 

Hmm, that doesn't match. Let me recheck: in the NORMALIZED problem, T=1 and val ≥ c(n) = 2^n/(2^{n+1}-1). In the unnormalized version D=2^{n+1}-1, T(Q∪R) = 2^n + (2^{n-1}-1) = 3·2^{n-1}-1. And val ≥ 2^n means A ≥ 2·2^n - T = 2^{n+1} - (3·2^{n-1}-1) = 2^{n+1} - 3·2^{n-1} + 1 = 4·2^{n-1} - 3·2^{n-1} + 1 = 2^{n-1}+1. That doesn't seem like an integer for all n. 

Wait — I think the unnormalized setup is: D=2^{n+1}-1 is the denominator (LCM of all G_n fractions), and the pieces are integers. So T(G_n) = 2^0+2^1+...+2^n = 2^{n+1}-1 = D. val(G_n) = 2^n (the largest piece), so c(n) = 2^n/D. In Lemma LL, Q partitions 2^n and R refines G_{n-1} with val(R) ≥ 2^{n-1} (by IH in the same unnormalized scale). So T(Q) = 2^n, T(R) = T(G_{n-1}) = 2^n-1. T(Q∪R) = 2^n + (2^n-1) = 2^{n+1}-1 = D. And val(Q∪R) ≥ 2^n means val ≥ D · c(n) = 2^n. ✓ Consistent. And val = (T+A)/2 ≥ 2^n iff A ≥ 2·2^n - D = 2^{n+1} - (2^{n+1}-1) = 1. ✓ So we need A(Q∪R) ≥ 1. Confirmed.

**Opening 6: Potential / exchange argument — flip one cut from Q to R.**
Suppose A(Q∪R) < 1. We derive a contradiction by "exchanging" one XY cut from Q (refining 2^n) to R (refining G_{n-1}), reducing to the case with t-1 cuts on 2^n (= Case B or fewer cuts). This only works if adding a cut to Q from R always decreases val(Q∪R) — but adding a cut to Q (making it finer) can increase or decrease A(Q).

**Opening 7: The tight case analysis.**
At the tight case Q={3,3,2}, R={2,2,2,1} (n=3): A(Q) = 3-3+2 = 2, A(R) = 2-2+2-1 = 1, B = ? Q-odd region is {x: N_Q(x) odd}. Sorted Q = {3,3,2}: N_Q(x) = 3 for x∈[0,2), = 2 for x∈[2,3), = 0 for x≥3. So Q-odd region = [0,2) (measure 2 = A(Q)). R = {2,2,2,1}: N_R(x) = 4 for x∈[0,1), = 3 for x∈[1,2), = 0 for x≥2. R-odd region = [1,2) (measure 1 = A(R)). B = measure([0,2) ∩ [1,2)) = 1. A(Q∪R) = 2 + 1 - 2·1 = 1. ✓ Exactly tight.

This reveals: at the tight case, the Q-odd region COMPLETELY CONTAINS the R-odd region. The overlap B = A(R) = 1. And A(Q∪R) = A(Q) + A(R) - 2A(R) = A(Q) - A(R) = 1. For this to equal 1, we need A(Q) - A(R) = 1, which holds here.

So the tight case is: Q-odd region contains R-odd region, and A(Q) = A(R) + 1. This is the "hardest case" for the merge lemma, and it gives exactly A(Q∪R) = 1.

**Opening 8: Monotonicity in t — adding more cuts to Q can only help.**
Conjecture: For fixed R, val(Q∪R) is non-decreasing in t (number of Q-cuts). Base t=0: Q = {2^n}, A(Q) = 2^n, val(Q∪R) = (2^n + 2^n - 1 + 2^n)/2 - B... wait this is getting complicated.

Actually for t=0 (XY doesn't cut 2^n at all), we're in Case 1 (covered, val ≥ 2^n). For t≥1, val(Q∪R) could be smaller. The minimum occurs at some t. Evidence from n=3: the minimum val=8 occurs at t=2 (Case A). For t=1 (Case B), the minimum approaches 8 only in the limit q→4 (Q→{4,4} is a degenerate cut). So the minimum occurs in the interior of t≥2.

This means: we CANNOT argue "adding more cuts to Q only helps" — the minimum is at t=2, not t=1.

---

### What's actually blocking Case A

The core difficulty: for t≥2, the Q-odd region is a union of potentially many intervals spread across [0, 2^{n-1}]. The R-odd region (from G_{n-1} refinement) is also a union of intervals in [0, 2^{n-1}]. We need their combined measure structure to ensure A(Q) + A(R) - 2B ≥ 1.

The only identity/inequality that works at the tight case Q={3,3,2}, R={2,2,2,1}:
- A(Q) - A(R) = 1 (merge lemma lower bound = 1, tight)
- B = A(R) (Q-odd contains R-odd)

So the argument must show: whenever B is large (close to A(R)), A(Q) must be correspondingly large too (A(Q) ≥ 2B - A(R) + 1 = 2A(R) - A(R) + 1 = A(R) + 1 if B = A(R)).

More generally: B ≤ A(R) always (since B ≤ A(R) by definition), and when B is close to A(R), the Q-odd region must nearly contain the R-odd region, which forces A(Q) ≥ A(R) + 1. Is this provable?

No — A(Q) ≥ A(R) + 1 is NOT always true. Counterexample: Q={5,3} (A(Q)=2), R={1,1,1} (A(R)=1+1=... wait A({1,1,1})=1-1+1=1), then B=1 if Q-odd=[0,3) and R-odd=[0,1): B=1=A(R), A(Q)=2=A(R)+1. ✓ for this case.

But we could have Q={5,1,2} → sorted {5,2,1}, A(Q)=5-2+1=4, R={2,1} A(R)=1, and... this is getting complicated.

**The RIGHT approach for Case A (candidate argument):**

Use the REMOVAL identity: A(S) = p_1 - A(S \ {p_1}) applied to S = Q∪R.

Sort Q∪R. The largest piece is max(Q∪R). Since all R-pieces ≤ 2^{n-1} and all Q-pieces ≤ 2^{n-1} (for Case A, t≥2, all Q-pieces ≤ 2^{n-1} because... actually not necessarily: if t≥2, XY could make one piece of size 2^n - ε and many tiny pieces, giving a Q-piece larger than 2^{n-1}). 

Actually wait: in Case A (t≥2), the Q-pieces could have max(Q) > 2^{n-1}. The Case A/B split isn't by t but by whether the largest Q-piece exceeds 2^{n-1}. In Case B (used in the proof above), the largest Q-piece is 2^n - q < 2^n, but it could still be > 2^{n-1} (e.g., q < 2^{n-1}).

Hmm, actually Case B was t=1 (1 cut on 2^n, so 2 pieces, but one can be > 2^{n-1}). Case A (t≥2) could also have a piece > 2^{n-1}. 

The key question is: what is max(Q)?

If max(Q) ≤ max(R) ≤ 2^{n-1}: then A(Q∪R) ≥ A(R) - A(Q) with the Q-odd region entirely ≤ max(Q) ≤ max(R). The proof would use the same argument as Case B.

If max(Q) > max(R): say max(Q) = m. Then A(Q∪R) ≥ m - A(Q∪R\{m}) = m - (remaining pieces). This is the removal identity and could be tracked recursively.

---

### Candidate approach: Induction on the number of pieces |Q|

**Base |Q|=2 (t=1):** Case B proof above. ✓

**Step |Q|=k+1 (t=k):** Given Q = {q_1,...,q_{k+1}} (t=k cuts), we want to show val(Q∪R) ≥ 2^n. Consider merging the two smallest Q-pieces q_k and q_{k+1} (the two smallest). This gives Q' with |Q'|=k (one fewer piece, t-1 cuts), and frees one XY cut to refine R into R' with val(R') ≥ 2^{n-1}. By induction, val(Q'∪R') ≥ 2^n. We then need: val(Q∪R) ≥ val(Q'∪R'). Is splitting a piece always weakly better for LB? NOT necessarily (splitting Q' into q_k, q_{k+1} can decrease A(Q) and help LB if they were in odd position, or hurt if in even position). So this direction is unclear.

---

### Analogous past problems from crux corpus

From prior round: `aimo-0117` (dyadic geometric sequence game) and `aimo-0019` (amortized potential with dyadic intervals). Neither has a direct match for the Q-odd/R-odd overlap control.

The most analogous structure: problems where A(X∪Y) ≥ threshold is needed using X, Y living in nested dyadic intervals. The crux for such problems is typically an "interval nesting" argument that controls the overlap.

---

### Distinct openings summary

1. **Case B (t=1) — CLEAN PROOF EXISTS**: A(Q∪R) ≥ A(R) - 2·max(0, max(R)-q) ≥ A(R) ≥ 1. Uses: B ≤ max(R)-q, max(R) ≤ 2^{n-1}.

2. **Case A via t-induction (undo one cut)**: Merge two Q-pieces → Q', freeing one cut for R. Track how A(Q∪R) changes. Most promising sub-case: merge the two smallest Q-pieces.

3. **Case A via the tight-case structure**: At the minimum, Q-odd region contains R-odd region (B=A(R)) and A(Q)=A(R)+1. Prove: whenever Q-odd ⊇ R-odd (B close to A(R)), A(Q) ≥ A(R)+1. This is a set-inclusion constraint on the parity regions.

4. **Case A via max(Q) analysis**: Split into max(Q) > 2^{n-1} (like Case B) and max(Q) ≤ 2^{n-1} (all pieces small, A(Q) small because A(Q) ≤ max(Q) ≤ 2^{n-1} ≤ A(R)+... unclear). If max(Q) ≤ 2^{n-1} and A(Q) ≤ max(Q) ≤ 2^{n-1}, then A(Q) ≤ 2^{n-1} and A(R) ≥ 1, merge gives A(Q∪R) ≥ A(R)-A(Q) ≥ 1-2^{n-1} which is useless. But if A(Q) ≤ 1, merge gives A(Q∪R) ≥ A(R)-1 ≥ 0 (useless).

5. **Bypass Case 2 entirely**: Try a different inductive structure that doesn't split into Case 1 / Case 2. For example, induct on the total number of cuts XY makes on ALL pieces (not just 2^n), showing val ≥ 2^n always increases under refinement... but XY is adversarial.

6. **Case A via A(Q) ≤ T(Q)/k bound**: If Q has k+1 pieces each ≤ 2^{n-1}, then A(Q) ≤ 2^{n-1} (A≤p_1≤2^{n-1}). Combined with A(R) ≥ 1 (IH), merge gives A(Q∪R) ≥ A(R)-A(Q) ≥ 1-2^{n-1} — useless. But if A(Q) ≤ 1 (small alternating sum for Q), then A(Q∪R) ≥ A(R) - 1 ≥ 0, still useless. 

   Better: A(Q) = A({q_1,...,q_{k+1}}) ≤ q_1 = max(Q). If max(Q) is close to 2^{n-1}, we're almost back to Case B. If max(Q) << 2^{n-1}, then A(Q) is small AND all Q-pieces are small. In that case the Q-odd region has small measure, and the Q∪R structure is dominated by R — but then val(Q∪R) ≥ val(R) ≥ 2^{n-1} which is less than 2^n. So this direction only gives val ≥ 2^{n-1}, not val ≥ 2^n.

---

### Dead ends (do not retry)

- **Merge lemma alone** (A(Q∪R) ≥ |A(Q)-A(R)|): provably insufficient for Case A with A(Q)>A(R). Checked computationally: 13819 near-tight configs have |A(Q)-A(R)| < 1.
- **Top/bottom decomposition** A = A_top + A_bot - 2B (split at 2^{n-1}): A_top ≥ 2B is false (reviewer confirmed, round 2).
- **Conjecture |A(Q)-A(R)| ≥ 1 for all valid Case A configs**: FALSE. Counterexample: A(Q)=1, A(R)=3/2, |diff|=1/2 (but val still ≥ 2^n because B is small).
- **Monotonicity of val in t (adding more cuts to Q only helps LB)**: FALSE. Minimum val is at t=2, not t=1.
- **All Q-pieces ≤ 2^{n-1} in Case A**: Not always true! XY using t≥2 cuts can still leave one piece > 2^{n-1}.

---

### Knowledge-base entries to use

- **Invariants & monovariants** (for a potential that tracks A(Q∪R) through cut operations).
- **Zero-sum games / backward induction** (for verifying the IH structure is correct).
- **Pigeonhole / extremal** (for the tight-case analysis, showing minimum at specific Q, R).
- **Induction** (the t-induction / removal identity approach).

---

### Prior progress

- Case B (t=1) proof: COMPLETE (found this round).
- Case A (t≥2): OPEN. Tight case identified: Q={3,3,2}, R={2,2,2,1} for n=3 (val=8 exactly, A(Q∪R)=1 exactly from merge with B=A(R)=1, A(Q)=2, A(Q∪R)=2+1-2=1). The tight structure is Q-odd ⊇ R-odd with A(Q)=A(R)+1.

---

### Small-case / intuition notes (labeled CONJECTURE)

- CONJECTURE: The minimum of val(Q∪R) in Case A (t≥2) is always achieved when Q has all equal pieces (the "balanced" split of 2^n). NOT TRUE computationally: tight case Q={3,3,2} is not balanced.
- CONJECTURE: The tight case always has B=A(R) (Q-odd ⊇ R-odd). Supported by n=3 computation: Q={3,3,2}, R={2,2,2,1}, Q-odd=[0,2), R-odd=[1,2), B=1=A(R). Possible inductive structure.
- CONJECTURE: For Case A with all Q-pieces ≤ 2^{n-1}, the minimum of A(Q∪R) is achieved when Q has exactly t=2 cuts (3 pieces), not more. Supported by n=3 computation (no 4-piece Q gives smaller val). Not verified for n≥4.
- OBSERVATION (NOT CONJECTURE): The Case B proof exactly uses max(R) ≤ 2^{n-1}. For Case A, the same geometric bound max(R) ≤ 2^{n-1} holds, but the Q-odd region is not a simple interval — it's a union of intervals — making the bound B ≤ max(R) - q inapplicable.
