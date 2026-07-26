## imo-2026-03 (IMO 2026 P3, Chu-Han war stick game)

**The answer (conjectured, strongly supported):** `c(n) = 2^n / (2^{n+1} − 1)`. Verified exactly for n=1 (2/3), n=2 (4/7), n=3 (8/15) by numerical minimax; the geometric strategy below hits the value to 1e-7 in every case, and the upper bound (Xiang holding Liu ≤ value) holds for all random Liu strategies tested. Satisfies the clean recursion `1/c(n) = 1/c(n−1) + 1/2^n`, `c(0)=1`, i.e. `1/c(n) = Σ_{k=0}^{n} 1/2^k = 2 − 1/2^n`. This recursion is the strongest hint that an inductive/telescoping proof exists.

### Distinct openings (each a different attack the outliner could build)

1. **Lower bound via the geometric-ratio-2 (dyadic) Liu strategy.** Liu pre-marks n points splitting the stick into pieces of sizes `1, 2, 4, …, 2^n` (each divided by `S = 2^{n+1}−1`), i.e. marks at cumulative sums `1/S, 3/S, 7/S, …, (2^n−1)/S`. The key property: the largest piece `2^n/S` strictly exceeds the sum of all the others `(2^n−1)/S`. Numerically, no matter how Xiang places n marks, Liu's odd-position sum is `≥ 2^n/S`, with equality when Xiang splits each piece `2^k` (k≥1) into two equal halves `2^{k−1}, 2^{k−1}` (yielding the multiset `1,1,1,2,2,4,4,…,2^{n−1},2^{n−1}` whose odd-position sum is exactly `2^n/S`). The crux is proving the inequality for ARBITRARY (non-equal) Xiang splits — the equal-halving Xiang response is the minimizer.

2. **Lower bound via the alternating-sum D reformulation.** Liu's share = `(1+D)/2` where `D = q_1 − q_2 + q_3 − …` is the alternating sum of the final pieces sorted descending. So the lower bound `Liu ≥ 2^n/S` is equivalent to `D ≥ 1/S` (the smallest geometric piece). This reframes the lower bound as: *after any n splits of the dyadic multiset `{1,2,…,2^n}/S`, the alternating-sum D stays ≥ the smallest piece.* This is a cleaner invariant to prove — likely by induction on splits, showing each split either preserves D or increases it, with the equal-halving split being the unique D-preserving move.

3. **Upper bound via a recursive/telescoping Xiang strategy (the recursion route).** The recursion `1/c(n) = 1/c(n−1) + 1/2^n` suggests an inductive upper bound: given Liu's n+1 pieces, Xiang uses ONE mark to "peel off" a piece of size ≈ 1/2^n worth of D, then the remaining game reduces to the (n−1)-game. For n=1 the Xiang strategy is explicit and instructive: if the larger piece A ≥ 2/3, split it equally (→ Liu = 1 − A/2 ≤ 2/3); if A < 2/3, split the larger piece barely (→ Liu = A < 2/3). Generalizing this "split-the-largest, either equally or barely, then recurse" is the natural inductive upper-bound engine.

4. **Upper bound via a stronger-surrogate adversary.** Replace Xiang with a more powerful surrogate (e.g. one allowed to choose the final sorted-order sign pattern freely, not just by alternating greedy). If even the surrogate cannot push Liu below 2^n/S, the real Xiang cannot either. Reduces to a linear-programming / sign-assignment extremal problem — heavier, but a clean fallback if the inductive upper bound stalls.

5. **Direct minimax / LP characterization.** For fixed n the game is a finite-dimensional continuous minimax; the value is a rational (2^n/S). One could in principle derive it by LP duality on the "Liu picks piece sizes, Xiang picks splits" formulation — but this is a verification engine, not a proof, and only useful to confirm small n.

### Candidate technique(s)
- **Greedy-alternating lemma** (free-choice pick-1 game, both maximize own total): first player's optimal value = sum of pieces at ODD positions when sorted descending. Proven airtight by induction (see below). This is the load-bearing reduction from the claiming phase to "odd-position sum."
- **Induction on n** with the recursion `1/c(n) = 1/c(n−1) + 1/2^n` as the engine.
- **Dyadic / powers-of-two construction** for Liu's lower bound; the property "largest piece > sum of all others" is the structural reason the construction works.
- **Alternating-sum invariant** `D ≥ smallest piece` for the lower-bound inequality-under-splits lemma.

### Cheap-kill candidates
- The greedy-alternating lemma is the cheap reduction: it collapses the whole claiming phase to "sort descending, sum odd positions." Provable in ~10 lines (done below). Don't re-derive it per-approach.
- The n=1 case is fully solvable by hand (c(1)=2/3, Liu marks at 1/3) — use as the induction base and as a sanity check.

### Knowledge-base entries to use
- `Pólya heuristics`: solve simpler/special case first (n=1 → 2/3 spots the pattern); find related/analogous problem.
- `Induction` (General Proof Methods): the recursion `1/c(n)=1/c(n−1)+1/2^n` is a textbook induction-loading target.
- `Invariants & monovariants` (Combinatorics): the alternating-sum D as an invariant-ish quantity under splits.
- `Constructive vs. existence`: "find largest c" needs matching lower bound (Liu strategy) AND upper bound (Xiang strategy) — both required for `solved`.
- `Pigeonhole / extremal`: possibly for the upper bound (extremal Liu configuration).

### Analogous past problems (cruxes)
- **aimo-0117** (best match): crux = "Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others. Jesse writes only powers of two." This is the SAME structural idea as Liu's 1:2:4:…:2^n pieces, where `2^n > 2^n−1 = sum of the rest`. The "largest exceeds sum of all others" property is precisely what makes the dyadic construction a forcing strategy. Strong analogue.
- **aimo-0262** (secondary): crux = "self-reproducing invariant family of configurations; each legal move can restore it, so the bound holds forever by induction." Maps to the alternating-sum invariant `D ≥ 1/S` being preserved/restored under Xiang's splits.
- **aimo-0560** (secondary): crux = "Replace the adversary with a strictly stronger surrogate whose reply is pointwise at least as damaging, so a win against the surrogate transfers down." Maps to opening #4 (surrogate upper bound).

### Prior progress
- None (round 1, workspace empty).

### Dead ends (do not retry)
- **Equal-pre-marking is WRONG.** Marking n equally-spaced points (n+1 equal pieces of 1/(n+1)) does NOT achieve the value: for n=1 it gives Liu only 1/2 < 2/3 (Xiang splits one half barely). The optimal Liu strategy is the ASYMMETRIC dyadic 1:2:4:…:2^n, not equal pieces. Do not pursue equal-piece strategies.
- The conjectured `(n+1)/(2n+1)` (equal-final-pieces value) is WRONG: it gives 3/5=0.6 for n=2, but the true c(2)=4/7≈0.571. Equal final pieces are not attainable by Liu against optimal Xiang.

### Small-case / intuition notes (all CONJECTURE unless flagged proven)

**PROVEN — greedy-alternating lemma (airtight):** For a multiset of m pieces, free-choice alternating claim, both maximizing own total, first player's optimal value = sum of odd-position pieces (sorted descending). Proof by strong induction on m: first player takes piece a_i; rest is played with opponent first, so by induction opponent gets odd-position sum of the (m−1)-piece remainder `O_rest`; first player gets `T − O_rest` where T=total. Minimizing `O_rest` over the choice of which a_i to remove: removing the largest a_1 gives `O_rest = a_2 + a_4 + a_6 + …` (even positions). Removing any other a_i gives `O_rest = (a_1−a_2) + (a_3−a_4) + … ≥ 0` MORE than the a_1 removal (pairwise, since a_{2j−1} ≥ a_{2j}). Hence removing a_1 (greedy) is optimal, value = sum of odd positions. (Verified: 20000 random trials, no counterexample.) — This lemma is rigorous; the outliner can use it as a certified fact.

**PROVEN — n=1 (c(1)=2/3):** Liu marks at 1/3 (pieces 1/3, 2/3). Xiang's best: split the 2/3 piece into a+b=2/3. Result 3 pieces, Liu = largest + smallest. If Xiang splits equally (1/3,1/3): pieces 1/3,1/3,1/3, Liu=2/3. If Xiang splits barely (ε, 2/3−ε): Liu = (2/3−ε) + ε → 2/3 (pieces sorted 2/3−ε, 1/3, ε). For ANY split, Liu ≥ 2/3. If Liu marks elsewhere: x<1/3 → Xiang equal-splits the 1−x piece → Liu=(1+x)/2 < 2/3; x>1/3 → Xiang barely splits → Liu=1−x < 2/3. So c(1)=2/3 exactly. ✓

**CONJECTURED (numerical, n=2,3):**
- c(2) = 4/7 ≈ 0.5714286. Liu marks at 1/7, 3/7 (pieces 1/7, 2/7, 4/7). Xiang's equal-halving response (split 4/7→2/7+2/7, and split a 2/7 barely or split 2/7→1/7+1/7) holds Liu to exactly 4/7.
- c(3) = 8/15 ≈ 0.5333333. Liu marks at 1/15, 3/15, 7/15 (pieces 1/15, 2/15, 4/15, 8/15).
- General: Liu marks at `(2^k − 1)/S` for k=1..n, S=2^{n+1}−1; c(n)=2^n/S.

**CONJECTURED — the lower-bound inequality lemma (the crux to prove):** For the dyadic multiset `{1, 2, 4, …, 2^n}/S`, after any n splits by Xiang, the alternating sum `D = q_1 − q_2 + q_3 − …` of the resulting sorted-desc pieces satisfies `D ≥ 1/S`. Equivalently Liu's odd-position sum ≥ 2^n/S. Equality is achieved by Xiang's equal-halving strategy (split each 2^k, k=1..n, into 2^{k−1}+2^{k−1}). The proof is the main technical difficulty; the outliner should build an induction on splits showing each split's contribution to D is minimized at the equal split and bounded below by 1/S.

**CONJECTURED — the upper bound structure:** For ANY Liu marking (n+1 pieces summing to 1), Xiang has an n-mark response holding Liu to ≤ 2^n/S. The natural strategy is recursive: locate the largest Liu piece; if it is "too large" (≥ some threshold), split it equally; else split it barely; then recurse on the remaining game with n−1 marks. The threshold and the invariant should fall out of the recursion `1/c(n) = 1/c(n−1) + 1/2^n`. Numerically confirmed (worst random Liu held below target for n=1,2,3) but NOT yet proven.

### Hard part summary
Both bounds are nontrivial, but the **lower-bound inequality-under-splits lemma** (opening #2, the D ≥ 1/S claim) is the deepest technical crux: it must show that among all ways Xiang can split the dyadic pieces, the minimum of the odd-position sum is exactly 2^n/S, attained at equal halving. The **upper bound** (opening #3) is the second crux: an inductive Xiang strategy matching the recursion. The greedy-alternating lemma and the n=1 base are solid foundations.
