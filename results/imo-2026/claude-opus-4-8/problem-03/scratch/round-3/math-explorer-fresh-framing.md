## imo-2026-03

### Problem recap
Liu Bang (LB) marks ≤ n points, Xiang Yu (XY) then marks ≤ n more (distinct, sequential), stick is cut, alternating greedy claiming (LB first). Find c(n) = guaranteed share for LB.
Answer: c(n) = 2^n/(2^{n+1}−1). Write D = 2^{n+1}−1.

### Current field (collapsed)
All three live approaches reduce via Lemma G1 to the odd-sum marking game and use the integral rewriting O = (1+μ{N odd})/2. Open gaps field-wide: L1 (confined Fragments Lemma), L2 (confinement exchange), U1 (upper bound budget accounting). Everyone hits the same three walls.

---

## Candidate Framings — Evaluated Honestly

### Framing (a): Self-reproducing potential Φ certifying both bounds simultaneously

**The proposal**: Define Φ(pieces, r_LB, r_XY) equalling the game value; show Φ is a super/sub-invariant.

**Reality check**: The potential-duality.md approach is registered but unbuilt. A game-value potential exists by backward induction (finite perfect-information game), but its CLOSED FORM is the hard part. Two specific candidate Φ's tested:

- Φ = alternating sum A of the current sorted list. This works at terminal positions (A = 2O−1 and A ≥ 1/D iff O ≥ c(n)), but A is NOT a monovariant under moves: a single XY cut can INCREASE or DECREASE A depending on where it lands. (Tested for n=3: splitting near-minimum fragments gives ΔA = 0, +1/5, +11/10 — always ≥ 0 in the confined case, but this is just L1 restated.)

- Φ = some dyadic weighting. Without an explicit closed form, this is vacuous (the outliner's warning in potential-duality.md is valid).

**Verdict**: This framing is NOT genuinely different. The explicit Φ claim reduces to proving L1 (lower bound) or U1 (upper bound) by another name. Any monovariant that implies O ≥ c(n) is logically equivalent to L1+L2. **Collapses to the same wall.**

---

### Framing (b): Induction on k (cuts inside R_n) for L1 — GENUINELY DIFFERENT

**The proposal**: Prove the Fragments Lemma L1 by induction on k = number of XY cuts inside R_n (k ≤ n), without using the integral ∫⌊(N_F−N_I)/2⌋dt.

**The argument**: Define the induction on k:

**Base k=0**: R_n is intact. O ≥ r_1 = 2^n/D (already proved in direct-constructive §4.1). ✓

**Inductive step**: Assume for any k-fragment decomposition of R_n summing to 2^n with n intact pieces {1,...,2^{n−1}} (D-units), we have O ≥ 2^n. Now XY makes one MORE cut, splitting fragment f into (f', f'') with f' ≥ f'' > 0. Claim: O_new ≥ 2^n.

**Case analysis on f's rank in the current sorted list** (confirmed numerically for n=1,2,3,4 with random search; min O stays ≥ 2^n at each step):

- **If f is at even rank r**: the split replaces f with {f', f''}, both ≤ f. Since f at even rank doesn't contribute to O, and at least one of {f', f''} takes an odd rank (the list grows by 1 element), O weakly increases.

- **If f is at odd rank r, adjacent intact piece I_b at rank r+1**: the split creates:
  - **Sub-case f' > I_b, f'' > I_b**: new sorted order has f' at rank r (odd), I_b at rank r+1 (even), f'' at rank r+2 (odd), I_c at rank r+3 (even). Change: ΔO = (f' + f'') − f = 0. But wait: the piece that was at rank r+2 (odd) in the old list is now pushed to rank r+3 (even). ΔO = f' + f'' − f − (r+2 old contribution). This needs careful accounting.
  
  **The cleanest sub-case**: f is the SMALLEST odd-ranked piece (rank r = m = 2k+1, last odd rank). Splitting f into (f', f''):
    - If f' > I_0 = 1 ≥ f'': list is [..., f', I_0, f'']. Odd ranks include f' and f''. O = O_old − f + f' + f'' = O_old. No change.
    - If I_0 ≥ f' ≥ f'': list is [..., I_0, f', f'']. I_0 moves to odd rank. ΔO = I_0 − f + f'' = I_0 − f'. Since f' ≤ I_0, ΔO ≥ 0. ✓
  
  In both sub-cases ΔO ≥ 0 when we split the last odd-ranked fragment.

**Numerical verification** (n=3, near-minimum config {4.1, 2.1, 1.8} intact {1,2,4}):
- Split f[2]=1.8 at 1.1: O stays 8.0 (ΔO = 0)
- Split f[2]=1.8 at 1.0: O stays 8.0 (ΔO = 0)  
- Split f[2]=1.8 at 0.9: O = 8.1 (ΔO > 0)
- Split f[1]=2.1 at 1.5: O = 8.2 (ΔO > 0)
- Split f[0]=4.1 at 2.1: O = 9.1 (ΔO > 0)

**Critical constraint**: With k ≤ n cuts we have ≤ n+1 fragments. The induction uses k ≤ n ONLY to ensure there's always at least one intact piece at an ODD rank below the smallest fragment (so the "push-up" mechanism works). With k = n+1 (one too many cuts): confirmed counterexample n=3, k=4 (5 frags = {4,2,1,1/2,1/2} summing to 8): O = 15/2 < 8. The constraint k ≤ n is essential AND used in the induction (the last odd rank has an intact piece available as a "buffer").

**Why this is GENUINELY DIFFERENT from the current approach**: 
- Does not use N(t), layer-cake formula, μ{N odd}, or any integral
- Operates on the sorted list directly
- The crux move is "splitting a fragment at odd rank is monotone in O"
- This is a structural/combinatorial argument, not a measure-theoretic one

**The remaining gap**: The general case where f is NOT the smallest odd-ranked piece — when splitting f at odd rank r moves BOTH f' and f'' to BELOW intact pieces that were at even ranks r+1 and r+3. This case needs careful analysis. The key geometric fact: the intact pieces are powers of 2 at fixed positions, so "gaps" between them are large (2^j to 2^{j+1} is a doubling), limiting how many fragments can cluster in one dyadic interval.

---

### Framing (c): Exchange argument for L2 — DIFFERENT APPROACH (not yet formally attempted)

**The proposal**: Prove L2 (XY's optimum confines all cuts to R_n) via an exchange argument: moving any XY cut from P_j (j < n) to R_n leaves O unchanged or decreases it (better for XY).

**Numerical evidence** (n=3):
- Option B (all 3 cuts in P_3): min O = 8.0
- Option A (1 cut in P_2, 2 cuts in P_3): min O ≈ 8.01 > 8
- Option C (2 cuts in P_2, 1 cut in P_3): min O = 8.0

So cuts in P_2 are WEAKLY WORSE for XY (achieve the same or worse min O than confining to P_3). The exchange is TIGHT: displacing a cut from P_2 to P_3 doesn't help XY but doesn't hurt either in the limiting case.

**Mechanism for the exchange**: When XY has a cut in P_j (j < n), it creates fragments ≤ P_{j-1} = P_j/2 (the halves of P_j are at most P_{j-1} in D-units). These small fragments:
- End up at LOW ranks in the sorted list (below P_{j+1}, P_{j+2}, ..., P_{n-1})
- Displace intact pieces from even to odd ranks (HELPING LB, not XY)
- Waste a cut that could have been used in R_n to suppress the large piece

Formal exchange: take the cut from P_j and move it into R_n. The large fragments in R_n (if any) now get more subdivision, pushing large pieces from odd to even ranks (helping XY). The small fragments from P_j are replaced by P_j (intact), which helps XY's suppression of O.

**This is a GENUINELY DIFFERENT approach to L2** (the current approach leaves L2 as an unproved assertion based on numerics). It's a direct combinatorial exchange, not requiring the integral formula.

---

### Framing (d): Casting as a known combinatorial game — NOT PROMISING

**Evaluated**: The odd-sum minimax game is a Stackelberg game (LB commits all marks first, XY responds with full information). This is NOT a standard combinatorial game (Nim, Sprague-Grundy, etc.) because:
1. It's not a sequential-move game (both players commit simultaneously to all their marks in one go, not turn-by-turn)
2. The payoff is a real-valued function (O), not a win/lose outcome
3. No standard solved form was found in the crux corpus matching this structure

**Corpus search**: 39 games-and-strategy cruxes in combinatorics. Closest: aimo-0117 (dyadic sequence game where "largest strictly exceeds sum of rest" = exactly LB's dominance identity P_n > ΣP_j), but aimo-0117 is a sequential move game, not Stackelberg. **Verdict: No useful reduction.**

---

### Framing (e): Strategy stealing / pairing — WEAK

c(n) > 1/2 for all n (since 2^n/(2^{n+1}−1) > 1/2 iff 2^{n+1} > 2^{n+1}−1, true). So LB guarantees > 1/2 by strategy stealing (pass on marking, take the larger half in claiming). But the sharp bound is 2^n/D ≈ 1/2 + 1/(2D), which strategy stealing cannot achieve. **Verdict: gives only weak lower bound, not sharp.**

---

## Distinct Openings Surfaced

1. **Induction-on-k for L1** (the cleanest new route): Base k=0 done. Inductive step: prove splitting any fragment at odd rank r cannot drop O below 2^n. Key case: smallest odd-ranked fragment f_{k+1}. When split into (f', f''): either {f', f''} both above I_0 (O unchanged by exact arithmetic), or I_0 "absorbs" the split and contributes to odd ranks (ΔO = I_0 − f' ≥ 0). The hard case is splitting a MIDDLE odd-ranked fragment where two intact pieces straddle the split — this requires tracking which intact piece "absorbs" each half.

2. **Exchange argument for L2** (new): Show for each j < n, any XY cut in P_j achieves worse (larger) min O than the corresponding cut moved to R_n. The mechanism: cuts in small pieces displace intact pieces from even to odd ranks, benefiting LB; cuts in R_n create large fragments that suppress LB's odd-ranked pieces.

3. **U1 via explicit budget accounting for XY's strategy**: XY's strategy is: if a_1 > 2^n/D, halve it (spending 1 mark). Each halving either (i) reduces the maximum below 2^n/D (success in ≤ n steps since the initial max is ≤ 1 = D/D and 1/2^k ≤ 2^n/D for k ≥ n−... wait need n halvings max) or (ii) creates pieces that allow interleaving. Direct bookkeeping: LB has p ≤ n+1 pieces, XY has n marks. The Möbius map c(n) = 2c(n-1)/(2c(n-1)+1) directly gives the mark budget: XY's k-th halving reduces the value from c(n) to c(n-k), so n halvings suffice to reach c(0) = 1. This bookkeeping for U1 should be cleaner than the current "halve-then-interleave combined accounting" gap.

---

## Candidate Technique(s)

- **L1**: Sorted-list monotonicity / induction on cut count (primary new angle). The crux: "splitting a fragment at odd rank is O-monotone" = the combinatorial core.
- **L2**: Exchange argument / "displacement" (moving cuts from small pieces to R_n is weakly better for XY).
- **U1**: Möbius-iteration budget tracking (each halving step maps c(n) → c(n-1), n steps exhaust the budget).

## Cheap-kill candidates

- For L2: The exchange is TIGHT (min O same for cuts in P_j vs R_n in the limiting case). So L2 might actually follow from L1 by a 1-line dominance: cutting P_j (j < n) with s cuts and R_n with n−s cuts gives a configuration that is (as a multiset of pieces) DOMINATED by confining all n cuts to R_n. This needs a dominance ordering argument.

- For L1: The sub-case where all fragments are > 2^{n-2} (so N_F > 0 in the upper half of the range) has N_F ≤ 3 at most (since 4·2^{n-2} = 2^n = ΣF), giving ⌊(N_F−N_I)/2⌋ ≤ 1 where N_I ≤ 1. The integral over this range is bounded above by 2^{n-2} (the length of the range times 1). The integral over the lower range must be ≤ −2^{n-2} to compensate. This gives a two-range split argument.

## Knowledge-base entries to use

- **Invariants & monovariants** (Combinatorics section): The induction-on-k argument needs a monotone quantity (O is weakly increasing under each split when k ≤ n). This is an invariant approach.
- **Double counting**: The exact identity (‡) E − ΣI = ∫⌊(N_F−N_I)/2⌋dt is a double-counting identity connecting piece sizes to the layer-cake.
- **Pigeonhole**: N_F − N_I ≤ 1 at t=0 (since k+1 ≤ n+1 and N_I(0) = n) is a pigeonhole bound.
- **Constructive/incremental** (Combinatorics): The induction-on-k framing adds cuts one at a time and proves the property is maintained.

## Analogous past problems (cruxes)

**Best analogy**: aimo-0117 ("Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others"). Crux: LB's construction P_n > ΣP_j is EXACTLY this property (dominance identity). How adapted: aimo-0117 uses dyadic dominance to ensure the player holding the largest power "outweighs" the rest; here LB's P_n = 2^n/D outweighs all other LB pieces together. The "defer committing the extreme value" strategy in aimo-0117 (wait until opponent frees the target cell) is analogous to LB's strategy in §4.1 (if XY doesn't cut R_n, the 2^n/D piece wins immediately).

**Second analogy**: aimo-0262 (Cinderella game; "hand the defender a self-reproducing invariant family"). Crux move: maintain an invariant that two complementary pairs sum to ≤ threshold, so you can always choose which pair to empty. Analogous to XY's interleaving strategy: maintain that the sorted list alternates fragment-intact-fragment-intact, so XY's next cut preserves the interleaving structure. The "split the total into two sub-collections and act on the smaller one" mechanism is analogous to XY's "halve then interleave" strategy.

**Third (weak) analogy**: aimo-0225 ("prove N-positions by strategy-stealing symmetry: reach symmetric position, argue winning reply could have been played directly"). The strategy-stealing flavor is present in the easy lower bound §4.1 (if XY doesn't cut R_n, LB wins trivially).

## Prior progress

**Current best (reviewer-certified)**: G1 (greedy = odd-ranked), R1/R2 (odd-sum rewritings), LB geometric construction + dominance identity, easy LB case (XY spares R_n), Interleaving Lemma I, base cases n=1 and n=2, exact identity (‡) E−ΣI = ∫⌊(N_F−N_I)/2⌋dt. Answer c(n) = 2^n/(2^{n+1}−1) confirmed numerically for n ≤ 5. Status: partial, three gaps open.

## Dead ends (do not retry)

- **induction-recursion slug (n→n−1 game separation)**: DEAD. XY's mark budget doesn't decrement (n marks total, not n−1 in the sub-game), and the odd-sum is a global functional of the merged list with cross-boundary interleaving. Do NOT attempt to separate the game at any mark/piece boundary.
- **Per-rank bound r_{2j} ≤ 2^{n−j}**: FALSE. Counterexample n=3, fragments {3, 2.5, 2.5} gives r_4 = 2.5 > 2. Any approach proving L1 term-by-term fails.
- **Unlimited-fragment version of L1**: FALSE. Counterexample n=3, k=4 (5 fragments = {4,2,1,0.5,0.5}): O = 7.5 < 8. Confirms k ≤ n is essential.
- **Strategy stealing for sharp bound**: Only gives LB ≥ 1/2, not the sharp c(n) > 1/2. Cannot sharpen via symmetry.

## Small-case / intuition notes

**Conjecture** (not proved): The Fragments Lemma L1 minimum O = 2^n is achieved EXACTLY when the k+1 fragments form a "perfect interleaving" with the top k intact pieces (each fragment slots just above an intact piece). This conjecture is consistent with all numerical evidence (n ≤ 5, 20000 random trials per case).

**Conjecture**: The induction-on-k step ΔO ≥ 0 holds for ALL splits of ANY fragment (not just the smallest), as long as the intact pieces are {1, 2, ..., 2^{n-1}} and k ≤ n. Numerically confirmed for n=3 (all k=0..3, multiple splits).

**Key structural observation**: At t=0 (below all pieces), N_F − N_I = (k+1) − n ≤ 1. This "starts non-positive" is the reason k ≤ n is the right threshold. With k = n+1, N_F − N_I = 2 at t=0, so ⌊(N_F−N_I)/2⌋ = 1 immediately (contributes a positive integral from t=0 to t=smallest piece), breaking the lemma. The constraint k ≤ n is precisely what forces the integral to start at floor-value 0.

**L2 numerical evidence**: Moving a XY cut from P_j (j < n) to R_n achieves min O ≤ (min O with cut in P_j). The exchange is tight (can achieve the same min O) but never strictly better to cut outside R_n. Suggests L2 follows from a weak dominance argument, not just exchange.
