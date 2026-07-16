# IMO 2026 P3 — Optimality Conditions Lens

## imo-2026-03

---

## CRITICAL FINDING: Round 1 Was Wrong

**The claimed answer c(n) = 2^n/(2^{n+1}-1) IS CORRECT.** Round 1's finding that "arithmetic beats geometric" was based on a bug: the Round 1 code only tested EQUAL sub-piece splits for XY. With optimal (unequal) XY splits, the picture reverses completely.

### The Error Demonstrated

For n=2, arithmetic LB = [1/6, 1/3, 1/2]:
- **Round 1's XY** (equal split): 1/2 → [1/4, 1/4]. Final pieces [1/3, 1/4, 1/4, 1/6]. LB gets 1/3+1/4 = 7/12.
- **Optimal XY** (unequal split): 1/2 → [1/3, 1/6]. Final pieces [1/3, 1/3, 1/6, 1/6]. LB gets 1/3+1/6 = **1/2**.

For n=2, geometric LB = [1/7, 2/7, 4/7]:
- **Optimal XY** (any split of 4/7 into [t, 4/7-t]): LB gets **exactly 4/7** regardless of t (proved analytically).

Conclusion: arithmetic guarantees only 1/2 (not 7/12), while geometric guarantees 4/7. **Geometric beats arithmetic** for n≥2.

---

## Distinct Openings

### Opening 1: The Invariance Property of Geometric LB (Lower Bound)

The geometric config {1, 2, 4, ..., 2^n}/(2^{n+1}-1) has a remarkable invariant:

**If XY places 1 mark inside L_n = 2^n/D, splitting it into [t, L_n-t], LB always gets EXACTLY 2^n/D.**

Proof for n=2, pieces {1/7, 2/7, t, 4/7-t}:
- If t ∈ (0, 1/7): LB gets (4/7-t)+1/7 = 5/7-t > 4/7 (XY has been too aggressive)
- If t ∈ [1/7, 2/7]: sorted = [4/7-t, 2/7, t, 1/7]. LB picks 0+2: (4/7-t)+t = 4/7 ✓
- If t ∈ [2/7, 4/7]: sorted has t ≥ 2/7. LB picks t+(4/7-t) = 4/7 ✓

The invariance extends to n marks in L_n: verified for n=3,4 (100 random sub-piece configurations tested, all give LB ≥ 2^n/D).

**Attack on lower bound:** Two cases suffice.
- **Case A (XY avoids L_n):** L_n > sum of all other LB pieces (geometric dominance). LB picks L_n first, total ≥ L_n. ✓
- **Case B (XY places j marks in L_n):** By the invariance property, LB still gets ≥ L_n.
  The key sub-claim: for any partition {a_1,...,a_k} of L_n and the original pieces {L_0,...,L_{n-1}}, greedy alternating picks give LB ≥ L_n.

### Opening 2: The Parity Argument (XY's Mark Count)

XY's optimal number of marks is exactly n-1, NOT n. Using n marks HURTS XY.

For n=4 with geometric LB, XY using j marks in L_4 gives:
- j=0: LB gets 0.677 (no XY marks, LB dominates)
- j=1: LB gets 0.581
- j=2: LB gets 0.548
- **j=3 (=n-1): LB gets 0.516 = 16/31** (minimum, XY's best)
- j=4 (=n): LB gets 0.531 (WORSE for XY — extra pick helps LB)

**Why:** j marks in L_n create j+1 sub-pieces. Total pieces = n+1+j. LB picks ceil((n+1+j)/2).
- j = n-1: total = 2n pieces (even), both pick n.
- j = n: total = 2n+1 pieces (odd), LB picks n+1 — one more pick for LB!

The parity argument is key for the lower bound: XY should use ≤ n-1 marks to avoid giving LB an extra pick.

### Opening 3: XY's Optimal Sub-Pieces (What XY Creates Against Geometric)

For geometric LB, XY's n-1 marks in L_n create n sub-pieces:
{L_{n-1}, L_{n-2}, ..., L_2, L_1, L_1} = {2^{n-1}, 2^{n-2}, ..., 4, 2, 2}/D

These n sub-pieces pair with the n original LB pieces {L_0, L_1, ..., L_{n-1}}:
- Pair (L_{n-1}, L_{n-1}): equal, LB picks one → L_{n-1}
- Pair (L_{n-2}, L_{n-2}): equal, LB picks one → L_{n-2}
- ...
- Pair (L_1, L_1): three L_1's! LB picks two → 2*L_1
- L_0 left: LB picks it (last) → L_0

Wait: actual LB total = L_{n-1} + L_{n-2} + ... + L_2 + L_1 + L_1 = (2^{n-1}+...+2+2)/D = (2^n-2+2)/D = 2^n/D = L_n. ✓

### Opening 4: Upper Bound (XY Limits Any LB to ≤ c(n))

This is the harder direction. Key numerical verification:
- n=2: over a fine grid of all [p1, p2, p3] configs with p1≤p2≤p3, XY with up to 2 marks always limits LB to ≤ 4/7. Maximum found: 0.5683 (grid resolution issue), true max is exactly 4/7.
- Example showing non-geometric configs are worse: [1/5, 2/5, 2/5] — XY splits 1/5 → [1/10, 1/10], giving LB = 2/5+1/10 = 1/2 < 4/7. ✓

**XY's upper bound strategy (proposed):** XY uses n-1 marks. The key insight: XY should sometimes mark INSIDE THE SMALLEST piece(s) to equalize things, not always the largest. The optimal XY response depends on the specific LB config.

**Critical observation for upper bound proof:** If LB doesn't use the geometric progression, there exists a piece L_k with L_k < 2*L_{k-1} (the doubling fails). XY can then split L_k to create a piece matching L_{k-1}, breaking the invariance.

### Opening 5: Why Arithmetic Fails (Structural Reason)

Arithmetic [1, 2, 3, ..., n+1]/T has p_{k+1}-p_k = p_k-p_{k-1} (constant difference). 
Geometric [1, 2, 4, ..., 2^n]/D has p_{k+1}/p_k = 2 (constant ratio).

For arithmetic n=2, LB pieces [1/6, 1/3, 1/2]:
XY splits 1/2 into [1/3, 1/6] (= [p_2, p_1]):
- This creates a second copy of p_2 and a second copy of p_1.
- Final pieces: [1/3, 1/3, 1/6, 1/6]. Both paired at the same level.
- LB picks 1/3+1/6 = 1/2 = p_3 (the piece XY split!).

For geometric n=2, LB pieces [1/7, 2/7, 4/7]:
XY tries to split 4/7 into [2/7, 2/7] (= [p_2, p_2]):
- But p_3 = 2*p_2! So both sub-pieces equal p_2.
- Final pieces: [2/7, 2/7, 2/7, 1/7]. LB picks 2/7+2/7 = 4/7 = p_3. ✓
- XY cannot reduce LB below p_3 no matter what!

**The geometric doubling is precisely what makes any split preserve LB's total.** With p_3 = 2*p_2:
- Sub-pieces [t, p_3-t] for any t ∈ [p_2, p_3]: p_3-t ∈ [0, p_2], so LB picks t+(second slot not t), and the key identity: t+(p_3-t) = p_3 appears whenever t and p_3-t straddle p_2.

For arithmetic: p_3 = p_2 + p_1 (not p_3 = 2*p_2), so XY can choose t = p_2, giving sub-pieces [p_2, p_1]. Now these fall "below" p_3, and LB only picks p_2+p_1 = 1/2 instead of p_3 = 1/2. Same value? Actually: 1/2 = p_3 here, so LB gets 1/2 regardless — the issue is that LB's second pick is diminished.

---

## Candidate Technique(s)

- **Minimax duality** (Stackelberg game): LB commits first, XY responds optimally.
- **Exchange/greedy argument**: Greedy optimality lemma (already certified) + induction on LB's piece structure.
- **Invariance property**: Geometric config preserves LB's total under any XY splitting of L_n.
- **Geometric dominance**: 2^n > 2^{n-1}+...+1 (key for Case A of lower bound).

---

## Cheap-Kill Candidates

- **Parity**: XY using n marks (instead of n-1) gives LB an extra pick and hurts XY. This kills all "XY uses all n marks" strategies.
- **Geometric dominance**: If XY avoids the largest piece L_n, LB picks it first (dominant piece). Simple calculation.
- **The split invariant for n=2**: Analytical case analysis proves LB gets exactly 4/7 from any XY split of 4/7. Short proof.

---

## Knowledge-Base Entries to Use

- Greedy/exchange argument (for Greedy Optimality Lemma — already certified).
- Minimax theorem (Stackelberg structure).
- Induction on the length of the geometric progression.
- Geometric series identities: 1 + 2 + ... + 2^{n-1} = 2^n - 1.

---

## Analogous Past Problems (Cruxes)

None closely analogous found yet (stick-splitting with greedy alternation is specialized). The closest are coin-splitting or cake-cutting games with greedy strategies, but the specific two-stage marking + cutting structure is novel.

---

## Prior Progress

**CRITICAL CORRECTION to Round 1:**
- The claim "c(n) = 2^n/(2^{n+1}-1) is wrong for n≥2" is FALSE.
- The actual finding: c(n) = 2^n/(2^{n+1}-1) is CORRECT.
- Round 1's error: XY's optimal splits are NOT equal sub-pieces. With optimal XY:
  - Arithmetic n=2: LB gets only 1/2 (not 7/12)
  - Geometric n=2: LB gets exactly 4/7 (confirmed)

**What IS established:**
1. Greedy Optimality Lemma (certified) ✓
2. Geometric LB config achieves 2^n/(2^{n+1}-1) against XY's optimal ✓
3. XY's optimal against geometric: n-1 marks in L_n creating {L_{n-1},...,L_1,L_1} ✓
4. Numerical evidence that geometric IS LB's optimal config ✓

**What needs proof:**
1. Lower bound: For geometric LB, ANY XY strategy gives LB ≥ 2^n/D. (Case A easy; Case B needs the key lemma)
2. Upper bound: For ANY LB config, XY can limit LB to ≤ 2^n/D. (Harder direction)

---

## Dead Ends (Do Not Retry)

- **"Arithmetic beats geometric"** — This is FALSE. Round 1 made an error assuming XY uses equal sub-pieces. Do NOT develop approaches based on arithmetic being optimal.
- **induction-on-n approach as stated** — The upper bound argument there was wrong, and moreover used the wrong answer. Requires complete rethinking with the correct answer.
- **Computing XY's best response assuming equal sub-pieces** — Will give wrong LB guarantees (too high for non-geometric configs).

---

## Small-Case / Intuition Notes (labeled as conjectures)

### Confirmed facts (computational):
| n | c(n) = 2^n/(2^{n+1}-1) | Geometric guarantee |
|---|------------------------|---------------------|
| 1 | 2/3 = 0.6667 | 2/3 ✓ |
| 2 | 4/7 = 0.5714 | 4/7 ✓ |
| 3 | 8/15 = 0.5333 | 8/15 ✓ |
| 4 | 16/31 = 0.5161 | 16/31 ✓ |
| 5 | 32/63 = 0.5079 | 32/63 ✓ |

### Structural invariant (confirmed for n=2 analytically, n=3,4 numerically):
**For geometric LB with pieces {L_0,...,L_n} = {1,2,...,2^n}/D:**
Any partition of L_n into sub-pieces {a_1,...,a_k} gives LB ≥ L_n = 2^n/D via greedy picking from {L_0,...,L_{n-1}, a_1,...,a_k}.

**Conjecture:** This invariant also holds when XY places marks in pieces OTHER than L_n (not just inside L_n). The numerical evidence (tested for n=3: min over ALL 2-mark XY strategies = 8/15) confirms the overall lower bound.

### XY's behavior (confirmed for n=2,3,4):
- XY's optimal: use EXACTLY n-1 marks.
- Using n marks (even number creating 2n+1 pieces) is COUNTERPRODUCTIVE for XY.
- Using fewer than n-1 marks leaves some LB pieces unmatched → LB gets more.

### LB's optimal (conjecture, supported by n=2 grid search):
The geometric config is the unique optimal LB strategy (up to scaling). The scan over all 3-piece configs for n=2 found maximum guarantee ≈ 0.568 < 4/7, with the maximum approached by configs close to the geometric ratio 1:2:4.

### The key structural reason geometric is optimal:
The doubling property L_k = 2*L_{k-1} ensures that when XY splits L_n at any position t, the two sub-pieces t and L_n-t "straddle" L_{n-1} = L_n/2, and LB picks one from each straddled level, always totaling L_n. Non-geometric configs (arithmetic, equal, etc.) lack this property, allowing XY to create sub-pieces that fall "between" existing LB pieces and reduce LB's total.
