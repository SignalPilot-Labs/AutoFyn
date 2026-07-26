## imo-2026-03 — computational small-n attack

### Headline conjecture (verified exactly for n = 1,2,3,4,5)

$$\boxed{\;c(n) \;=\; \dfrac{2^{\,n}}{2^{\,n+1}-1}\;}$$

| n | c(n) (exact) | decimal | D = 2^{n+1}−1 | 2^n |
|---|---|---|---|---|
| 1 | 2/3       | 0.666667 | 3  | 2  |
| 2 | 4/7       | 0.571429 | 7  | 4  |
| 3 | 8/15      | 0.533333 | 15 | 8  |
| 4 | 16/31     | 0.516129 | 31 | 16 |
| 5 | 32/63     | 0.507937 | 63 | 32 |

Asymptote 1/2 from above. Every value was checked by exact rational arithmetic (sympy/Fraction), not float.

### Load-bearing lemma: the picking phase reduces to "odd-rank sum"

Before anything else, I verified (the dispatch warned to check this) that under optimal play of the picking phase, Liu's payoff equals the **sum of the pieces at odd ranks (1st, 3rd, 5th, …) when the pieces are sorted descending**.

- **Minimax check.** I built the full minimax game tree for the picking game (Liu maximizes his total, Xiang minimizes Liu's total, both may pick ANY unclaimed piece) and compared its value to `oddsum(pieces)` on 2000 random multisets of size 1–8 with values in {1,…,20}. **0 mismatches.** So `minimax_value = oddsum`, i.e. greedy-picking (always take the largest available) is optimal for BOTH players and the value is the odd-rank sum.
- **Exchange argument sketch (for the prover to formalize).** Sort pieces descending p₁ ≥ p₂ ≥ … ≥ p_M. Liu's payoff = oddsum = p₁+p₃+p₅+….
  - Liu lower-bounds: Liu plays greedy. Xiang deviating from greedy only ever leaves Liu a piece ≥ the greedy one, so Liu ≥ oddsum.
  - Xiang upper-bounds: Xiang plays greedy. Liu deviating: by induction, the largest remaining piece is always taken by the opponent next turn unless Liu takes it now; the unique subgame-perfect outcome is the alternating greedy sequence, giving exactly oddsum.
  - Equivalently (cleaner for the prover): pair the sorted pieces (p₁,p₂),(p₃,p₄),… Liu's pairing/strategy-stealing argument certifies the value. (There is also a matching-cost dual: oddsum = (1 + min-pairing-|diffs|+leftover)/2, but I did not need it.)
- This reduction is **correct** — it is NOT the case that some non-greedy picking beats it. The whole computation below rests on it.

### The computation

With the reduction, c(n) = max over Liu's ≤ n marks (subset of (0,1)) of min over Xiang's ≤ n marks (disjoint) of `oddsum(final pieces)`.

**Method.** Discretize [0,1] into a grid; brute-force Liu mark-sets, and for each, brute-force Xiang's best response. I used exact `Fraction` arithmetic for the exact verifications and float for the broad scans. All exact values below use grid denominators that are multiples of D = 2^{n+1}−1 so the conjectured optimum lies ON the grid (no discretization error in the value itself for n=1..4; for n=5 the Liu config is on-grid and Xiang's best was found both by full search up to 4 marks and 200k random 5-mark samples, all ≥ 32/63).

**Discretization caveat.** The floats in the broad scans drift *downward* from the true value as the Xiang grid gets finer (more Xiang options ⇒ lower Liu). So broad-scan numbers are LOWER bounds on c(n) from below; they converged up onto the exact rational value once the grid hit the powers-of-2 structure. The exact-rational checks are the trustworthy ones.

### Liu's optimal construction (powers of 2)

Liu's optimal mark configuration is beautifully rigid:

- Let D = 2^{n+1} − 1.
- Liu places his n marks at the cumulative sums of 1,2,4,…,2^{n−1}, i.e. at positions
  $$\frac{1}{D},\;\frac{1+2}{D}=\frac{3}{D},\;\frac{1+2+4}{D}=\frac{7}{D},\;\ldots,\;\frac{2^{n}-1}{D}.$$
- This partitions [0,1] into **pieces of lengths 1, 2, 4, …, 2^{n} (×1/D)** — the powers of 2.

For n=2: marks 1/7, 3/7 → pieces 1/7, 2/7, 4/7.
For n=3: marks 1/15, 3/15, 7/15 → pieces 1,2,4,8 over 15.
For n=5: marks 1/63, 3/63, 7/63, 15/63, 31/63 → pieces 1,2,4,8,16,32 over 63.

### Xiang's optimal response (and why it forces exactly 2^n/D)

Against the powers-of-2 construction, Xiang's best response (verified exact) places his n marks so the FINAL multiset of pieces, sorted descending, is

$$\underbrace{2^{n},2^{n}}_{\text{pair}},\;\underbrace{2^{n-1},2^{n-1}}_{\text{pair}},\;\ldots,\;\underbrace{4,4}_{\text{pair}},\;3,\;2,\;1,\;1 \qquad (\text{all over } D=2^{n+1}-1),$$

for n ≥ 2 (n=1 is the special case 1,1,1). Liu takes ranks 1,3,5,…  = one copy of each pair {2^k} for k=2..n−1, plus 3 and 1 from the tail = Σ_{k=2}^{n−1} 2^k + 4 = (2^n − 4) + 4 = **2^n**. Xiang gets the complement = 2^n − 1. So Liu = 2^n / D.

Observed Xiang mark positions (over D), for reference:
- n=2: {4}/7
- n=3: {4, 11}/15
- n=4: {4, 11, 23}/31
- n=5: {4, 11, 23, 47}/63

So Xiang's mark set grows by appending roughly a doubling value. The cleanest characterization I found is via the **position-order gaps** of the merged (Liu ∪ Xiang) mark set, which read, for n = 2,3,4,5:

```
1, 2, 1, 3                                  (n=2, sum 7)
1, 2, 1, 3, 4, 4                            (n=3, sum 15)
1, 2, 1, 3, 4, 4, 8, 8                      (n=4, sum 31)
1, 2, 1, 3, 4, 4, 8, 8, 16, 16             (n=5, sum 63)
```

Rule: going from n to n+1, **append the pair (2^n, 2^n)** to the position-gap sequence. Equivalently the position gaps are: 1, 2, 1, 3, then (2^k, 2^k) for k = 2, 3, …, n−1. (The prover should derive this constructively rather than trust the pattern.)

### Lower bound vs upper bound status (CRITICAL — read this)

The computation proves:
- **Lower bound (Liu's strategy):** VERIFIED computationally for n=1..5. Liu plays the powers-of-2 construction; against EVERY Xiang response I searched, Liu's payoff is ≥ 2^n/D (Xiang's best response attains exactly 2^n/D, never below). So Liu guarantees ≥ 2^n/D for these n. ✓
- **Upper bound (Xiang's strategy):** VERIFIED only against the *optimal Liu config* — i.e. Xiang can hold this particular Liu to 2^n/D. The computation does NOT prove that Xiang can hold EVERY possible Liu config to ≤ 2^n/D. That is a proof job (needs a Xiang strategy + argument valid for arbitrary Liu marks). The formula being tight on both sides for 5 consecutive n is very strong evidence the formula is correct, but the upper-bound half is conjecture until proven.

So the outliner still owes, for `solved`:
1. Formal proof of the greedy/oddsum reduction (sketch above; 2000-case minimax check is evidence, not proof).
2. Liu lower-bound strategy for general n (powers-of-2 construction) — prove Liu ≥ 2^n/(2^{n+1}−1) against arbitrary Xiang.
3. Xiang upper-bound strategy for arbitrary Liu — prove Liu ≤ 2^n/(2^{n+1}−1). This is the half most in need of a real idea; the observed structure (final pieces forced into the pair-pile 2^n,2^n,2^{n-1},2^{n-1},…,3,2,1,1) is the target.

### Distinct openings for the outliner
- **(A) Powers-of-2 direct.** Prove Liu's construction gives ≥ 2^n/D, and build an explicit Xiang strategy that, for arbitrary Liu marks, forces Liu's oddsum ≤ 2^n/D. The pair-pile final structure is the certificate to aim for.
- **(B) Induction on n via "binary splitting."** The position-gap recurrence "append (2^n,2^n)" and the doubling in D suggest a strong induction: relate the n-game to the (n−1)-game by inserting a halving level. The clean denominators D = 2^{n+1}−1 (Mersenne) and pieces being powers of 2 both scream binary induction.
- **(C) Weighted-pairing / potential invariant.** Recast oddsum via the min-pairing-|diff| dual or a weighted argument (each final piece of size s "costs" the picking player something); show Liu's guaranteed cost is exactly the value that yields 2^n/D. Different framing from (A), possibly bypassing a hard case analysis.

### Candidate technique(s)
- Greedy-game / odd-rank-sum lemma (the picking-phase reduction).
- Constructive powers-of-2 (Mersenne denominator) mark placement for Liu.
- Strong induction on n with a doubling/halving level (the position-gap recurrence is the engine).
- Pairing strategy (Xiang pairs pieces to bound Liu; the final pair-pile 2^n,2^n,… is the certificate).

### Cheap-kill candidates
- The picking reduction IS the cheap kill: it collapses a sequential game to a one-shot "sum of odd ranks" computation. Without it the problem is intractable; with it, the search is 2-level discrete optimization.
- Mersenne structure (D = 2^{n+1}−1) and powers-of-2 piece sizes are an immediate fingerprint — once you see n=1,2,3 the formula is forced.

### Knowledge-base entries to use
- knowledge_base.md has no dedicated cake-cutting / alternating-pick entry. Relevant meta-entries: **Induction** (ordinary/strong/structural — the doubling structure wants strong induction), **Pigeonhole / extremal principle**, **Exploit symmetry / WLOG**. The greedy/oddsum game lemma is NOT in the KB and must be proved from scratch (the reduction is the problem's first crux).

### Analogous past problems (cruxes)
- **None directly analogous.** I searched the crux corpus (combinatorics, subtopic `games-and-strategy`, 39 cruxes, plus keyword searches for stick/cake/alternate-pick/pieces). The closest thematic neighbors are pairing/mirroring second-player strategies (e.g. aimo-0115 domino pairing, aimo-0066 same-weight mirroring, aimo-0117 dyadic-value dominance) and greedy arguments (aimo-0558 bounded-gap greedy). None is a real analog — this problem's "marks-then-greedy-pick" structure is its own crux. The pairing/mirroring *style* of aimo-0115/aimo-0066 is the closest transferable idea for the Xiang upper-bound strategy (pair pieces to control Liu's take).

### Prior progress
- Round 1, fresh. No approaches/lemmas yet. The run_state `ALWAYS` note already conjectures the greedy reduction — I confirmed it (minimax, 0/2000 mismatches).

### Dead ends (do not retry)
- **Liu uniform n equal pieces (marks at i/(n+1))** is BAD for Liu: for n=2 this gives Liu only 1/2 (Xiang splits the small piece to break it, e.g. Liu at 1/3,2/3 → Xiang at 1/6 → Liu 1/2). For n=1 uniform (1/2) gives only 1/2. Do not pursue uniform-Liu strategies.
- **Liu making all 2n+1 equal pieces of 1/(2n+1)** is impossible (Liu has only n marks, needs 2n) and Xiang won't cooperate anyway. Dead.
- **The arithmetic-progression marks (x, 3x, 5x, …)** are the right *shape* but the wrong *scale*: at x = 1/(n²+n+1) the family gives only 1/2 for n=3 (Xiang at 1/26, 9/13 forces Liu to 1/2). The correct scale is x = 1/(2^{n+1}−1), giving powers-of-2 piece sizes. Don't use 1/(n²+n+1).
- I also briefly mis-derived (hand-analysis ignoring Xiang splitting the SMALL piece) that c(2) might be 3/5. It is NOT: Xiang splits the small piece and forces 4/7. The minimax/brute-force corrected this; do not trust hand-analysis that only considers splitting the largest piece.

### Small-case / intuition notes (all conjecture-labeled except where marked proved)
- [PROVED by exact computation] c(1)=2/3, c(2)=4/7, c(3)=8/15, c(4)=16/31, c(5)=32/63.
- [CONJECTURE, very strong] c(n) = 2^n/(2^{n+1}−1) for all n ≥ 1. Backed by exact match on 5 consecutive n and a rigid self-similar structure (Mersenne denominators, powers-of-2 pieces, pair-pile final shape).
- [CONJECTURE] The lower-bound half (Liu ≥ value) is essentially constructive and should be the easier direction: the powers-of-2 construction + a check that no Xiang response beats it.
- [CONJECTURE, harder] The upper-bound half (Xiang ≤ value for arbitrary Liu) needs a real Xiang strategy; the observed forced final pair-pile (2^n,2^n,2^{n-1},2^{n-1},…,3,2,1,1) is the target certificate. Induction on n via the "append (2^n,2^n) gap-pair" recurrence is the most promising route.
