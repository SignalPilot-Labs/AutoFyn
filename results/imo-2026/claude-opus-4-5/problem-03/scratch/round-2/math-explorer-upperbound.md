# Explorer Report: imo-2026-03 — Upper Bound / XY's Strategy Lens

## CRITICAL CORRECTION FROM ROUND 1

**Round 1's conclusion that "arithmetic beats geometric" was WRONG due to a computational error.**

Round 1 said: XY's best response to arithmetic [1/6, 1/3, 1/2] is to split 1/2 equally into [1/4, 1/4], giving LB = 7/12.

**VERIFIED WRONG**: XY can instead split 1/2 **asymmetrically** into [1/3, 1/6]:
- New pieces: [1/6, 1/3, 1/3, 1/6] = sorted [1/3, 1/3, 1/6, 1/6]
- LB picks positions 1, 3: 1/3 + 1/6 = **1/2**, not 7/12.

XY's true optimal with 2 marks against arithmetic is **LB = 1/2** (confirmed numerically, exact). So arithmetic [1:2:3] gives LB only 1/2, WORSE than geometric's 4/7.

**The correct answer is c(n) = 2^n / (2^{n+1} - 1).** Round 1 was right about geometric being optimal; the comparison was wrong.

---

## imo-2026-03

- **Distinct openings:**

  1. **Saddle-point / Nash equilibrium approach**: The game has a minimax saddle point. LB uses the geometric config [1, 2, 4, ..., 2^n]/D (D = 2^{n+1}-1); XY's two critical response strategies give EQUAL value c(n) = 2^n/D at this config. For any other LB config, at least one XY strategy does strictly better. This is the minimax equilibrium characterization.

  2. **XY's two-strategy upper bound (n=2 in detail)**: For pieces [a, b, c] with a ≤ b ≤ c, XY has two key 2-mark strategies:
     - Strategy A: 1 mark on c at midpoint. If c ≥ 2b: LB gets c/2+b. If c < 2b: LB gets c.
     - Strategy B: 1 mark on c at midpoint + 1 mark on b at midpoint. Creates 5 pieces [a, b/2, b/2, c/2, c/2]. LB picks 3: c/2 + b/2 + a = (1+a)/2.
     
     XY picks whichever strategy gives LESS. Setting Strategy A = Strategy B at geometric config:
     - c = 2b: A gives c/2+b = 2b, B gives (1+a)/2. Setting equal: 2b = (1+a)/2 where a=1-3b. Solving: 2b = (1+1-3b)/2 = (2-3b)/2 → 4b = 2-3b → 7b = 2 → b = 2/7. Then c = 4/7, a = 1/7. **Geometric config!**
     
     At b=2/7: min(A,B) = min(4/7, 4/7) = 4/7. For any other config, min(A,B) < 4/7. Numerically confirmed.

  3. **Induction on n via the n=1 base case structure**: For n=1, XY's strategy:
     - If p ≤ 1/3 (LB's smaller piece): split (1-p) equally → LB gets (1+p)/2 ≤ 2/3.
     - If p > 1/3: split (1-p) into [p, 1-2p] → LB gets 1-p < 2/3.
     
     The two strategies cross exactly at p = 1/3 (geometric config for n=1). Same saddle structure.

  4. **Geometric "domination" lower bound**: Against geometric LB, if XY avoids splitting the largest piece, LB gets the whole largest piece 2^n/D > 1/2 first, then more. XY must split the largest piece. With n-1 marks on the largest piece creating n sub-pieces, the optimal split gives exactly c(n).

  5. **Alternating sum bound via sorted pairing**: After XY's n-1 marks on largest piece, the 2n total sorted pieces have a "paired" structure where each LB piece of size 2^k/D is paired with an equal XY sub-piece. LB picks one of each equal pair, getting exactly c(n).

- **Candidate technique(s)**:
  - Minimax game theory / Nash equilibrium saddle point
  - Exchange argument (greedy optimality, already proved)
  - Induction on n with explicit XY strategy
  - Case analysis on ratio c/b (where c is LB's largest piece)

- **Cheap-kill candidates**:
  - **Parity of piece count**: XY prefers to create an EVEN number of pieces (2n). If XY uses n-1 marks (not n), the total is n + (n-1) + 1 = 2n pieces; LB and XY each pick n. Using n marks creates 2n+1 pieces; LB picks n+1. The extra pick favors LB — so XY should use at most n-1 marks. (Exception: when the 2nd mark saves more than the extra pick costs, which also needs case analysis.)
  - **Geometric ratio threshold**: XY's 1-mark response to largest piece c is useful only when c ≥ 2b (ratio ≥ 2). If c < 2b, XY must split c into 3 (use 2 marks) or attack other pieces. This is a clean structural case split.

- **Knowledge-base entries to use**:
  - **Minimax theorem / saddle point**: (not explicitly named in KB but related to the Stackelberg game structure)
  - **Standard inequalities / AM-GM**: bounding the alternating sum
  - **Extremal principle**: the geometric config is extremal — proved by showing any other config has a strictly worse XY response
  - **Induction-and-construction**: the general c(n) proof likely uses induction on n with the XY strategy as explicit construction

- **Analogous past problems (cruxes)**:
  - **aimo-0117** (subtopic: games-and-strategy): assigns values as geometric/dyadic sequence. Crux: "Assign values as two-sided geometric sequence; defer committing the extreme value until opponent moves." Analogous in that the geometric doubling structure is the winning config. The "deferred commitment" mirrors LB's geometric setup which forces XY into an unfavorable response.
  - **aimo-0019** (subtopic: games-and-strategy): dyadic covering game where the correct move involves halving intervals. Crux: "respond to each opponent move by painting the next dyadic interval." Analogous structure — the power-of-2 lengths are central to both problems.
  - **aimo-0369** (subtopic: games-and-strategy): proof that in a 2n-card line-pick game, the first player can guarantee getting either ALL odd-indexed or ALL even-indexed cards. This proves a "choice of parity" lemma that is directly relevant: LB's greedy = picking odd-indexed pieces. The Dutch proof shows the first player controls which parity they get — but here the problem is richer because piece sizes are not fixed.

- **Prior progress**: 
  - Greedy Optimality Lemma: CERTIFIED (LB and XY both play greedy = always pick the largest).
  - Geometric lower bound: c(n) = 2^n/(2^{n+1}-1) is achievable by LB using geometric config. VERIFIED for n=1,2,3,4.
  - Current best approach: geometric-direct (status: partial, correctly sets up the answer but has gaps in both lower bound proof and upper bound proof).

- **Dead ends (do not retry)**:
  - **induction-on-n approach**: RETHINK status. The upper bound argument ("interleaving") was fatally flawed because it assumed XY's only good strategy is equal splitting. NOW we know XY has multiple strategy types and needs case analysis.
  - **arithmetic is optimal for LB**: DISPROVED. Arithmetic [1:2:3:..:(n+1)] gives LB only 1/2 (for n=2), far below 4/7. Round 1's computation used a suboptimal XY response (equal split). Do NOT retry approaches based on arithmetic being LB-optimal.

- **Small-case / intuition notes** (labeled as conjecture/verified):

  For n=2 VERIFIED:
  - Geometric [1/7, 2/7, 4/7]: LB gets exactly 4/7 against XY's optimal 2-mark play.
  - Arithmetic [1/6, 1/3, 1/2]: LB gets only 1/2 against XY's optimal 1-mark play (split 1/2 → [1/3, 1/6]).
  - Equal [1/3, 1/3, 1/3]: LB gets 2/3... wait, XY can split one 1/3 into [1/6, 1/6]: 4 pieces [1/6, 1/6, 1/3, 1/3]. Sorted [1/3, 1/3, 1/6, 1/6]. LB picks 1/3+1/6 = 1/2.
  - The saddle point: geometric is where XY's two main strategies (1-mark on c, 2-mark on c+b) give equal values. LB maximizes over configs; XY minimizes over strategies. Both optimize to 4/7 at geometric.

  For n=3 VERIFIED:
  - Geometric [1,2,4,8]/15: LB gets exactly 8/15 against XY's optimal 3-mark play.
  - XY's optimal: 2 marks on 8/15 splitting into [4/15, 2/15, 2/15]. Creates 6 pieces. LB picks 3.

  CONJECTURE (from pattern):
  - c(n) = 2^n/(2^{n+1}-1) for all n ≥ 1.
  - c(n) → 1/2 as n → ∞.
  - XY's optimal against geometric LB uses exactly n-1 marks (one mark fewer than LB).
  - The "paired configuration" after XY's optimal response: sorted pieces are (2^{n-1}/D, 2^{n-1}/D, 2^{n-2}/D, 2^{n-2}/D, ..., 1/D, 1/D, 1/D) where LB picks one of each pair.

## Key Structural Insight for the Proof

**For the lower bound** (geometric ≥ c(n)): The geometric dominance property: 2^n/D > sum of all smaller pieces. So if XY places all marks OUTSIDE the largest piece 2^n/D, LB gets that piece first (it's the unique largest), getting ≥ 2^n/D = c(n). If XY places j ≥ 1 marks inside 2^n/D, the sub-pieces plus the n-1 other LB pieces must be carefully analyzed via case analysis on j.

**For the upper bound** (any LB ≤ c(n)): XY's strategy depends on the LB config's structure. The key is that XY always has n marks and can use them to reduce LB below c(n) by creating a "balanced" configuration. The proof likely proceeds by induction with an explicit XY strategy:
- If LB's largest piece c ≥ 2*(second-largest): XY uses n-1 marks on c to create paired sub-pieces, reducing LB to c(n).
- If c < 2*(second-largest): XY attacks differently (uses marks on multiple pieces).

The induction should use the n=1 base case (explicit strategy with 2 case branches) and the recursive structure where XY "pretends" the problem has n-1 marks by consuming one piece.
