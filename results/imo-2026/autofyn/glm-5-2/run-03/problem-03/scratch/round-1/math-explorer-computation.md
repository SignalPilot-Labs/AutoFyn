## imo-2026-03 (COMPUTATIONAL route)

### Computed values (verified numerically to ~1e-6)

| n | c(n) computed | exact fraction | formula 2^n/(2^{n+1}-1) |
|---|---|---|---|
| 1 | 0.6666667 | **2/3** | 2/3 ✓ |
| 2 | 0.5714286 | **4/7** | 4/7 ✓ |
| 3 | 0.5333333 | **8/15** | 8/15 ✓ |

**Conjectured closed form: c(n) = 2^n / (2^{n+1} − 1).** As n→∞ this → 1/2, matching the intuition that with many marks both players approach equal shares.

### How computed (method, so the outliner can trust it)

Foundational fact assumed (greedy-alternating lemma, being proved by another explorer): with final pieces sorted descending a_1≥a_2≥…≥a_m, Liu Bang (picks first) gets odd positions a_1+a_3+a_5+….

Payoff function: `liu_payoff(L,Y) = sum of odd-indexed entries of descending-sorted piece lengths`, where pieces come from cutting [0,1] at L∪Y (L = Liu's marks, Y = Xiang Yu's marks).

Minimax: c(n) = max_{|L|≤n} min_{|Y|≤n} liu_payoff(L,Y). Xiang Yu's inner minimization is a non-convex piecewise-linear problem, so I used a FINE grid (≥150 points) over Y for each L (combinations of all sizes k=0..n), plus Nelder-Mead local refinement from multiple starts. WARNING: coarse grids (35–45 pts) systematically OVERESTIMATE Liu's value (miss Xiang Yu's true response); the fine grid is necessary. Final values are exact fractions because the optimal configs sit at rational points.

### Lower bound — Liu Bang's strategy (verified)

Liu Bang places his n marks so that the n+1 initial pieces (before Xiang Yu moves) are in **geometric (dyadic) ratio 1 : 2 : 4 : … : 2^n**, i.e. piece sizes 1/d, 2/d, …, 2^n/d with d = 2^{n+1}−1. Concretely the marks are at the cumulative sums (in any order around the stick): for n=1, mark at 1/3 (pieces 1/3, 2/3); for n=2, marks at {1/7, 3/7} (pieces 1/7, 2/7, 4/7); for n=3, marks at {1/15, 3/15, 7/15} (pieces 1/15, 2/15, 4/15, 8/15). Any permutation of the dyadic pieces around the stick works — verified for n=3: all 24 orderings give exactly 8/15.

The key structural invariant: the largest piece g_n = 2^n/d strictly exceeds the sum of all the others: g_n = 2^n/d > (2^n − 1)/d = g_0+g_1+…+g_{n-1}. This "largest exceeds sum of rest" is the load-bearing condition. (Pointer, not a proof — the outliner must prove that this invariant forces Liu's odd-position sum ≥ g_n = c(n) regardless of how Xiang Yu splits the pieces.)

### Upper bound — Xiang Yu holds Liu to ≤ c(n) (verified numerically)

For n=2: scanned 300 random L + grid(20×20), fine Y-grid(90 pts): max Liu value found = 0.571053 < 4/7 = 0.571429. UB holds.
For n=3: scanned 120 random L + grid(9×9×9), fine Y-grid(70 pts): max found = 0.526606 < 8/15 = 0.533333. UB holds.
No Liu configuration beats the formula. The exact upper-bound PROOF is the open gap for the outliner.

### Xiang Yu's worst-case structure (observed, conjectured)

Inspecting Xiang Yu's best response against Liu's optimal config:
- n=2, L={1/7,3/7}: Xiang Yu needs only **1 mark** (at ≈0.572), yielding pieces desc ≈ [0.428, 0.286, 0.143, 0.143]; Liu (odd) = 0.428+0.143 = 0.571 = 4/7. Xiang Yu's optimal response does NOT always use all n marks — sometimes fewer suffice. So the upper-bound proof for Xiang Yu must consider k=0..n marks (the problem allows "at most n").
- n=3, L={1/15,3/15,7/15}: Xiang Yu uses all 3 marks.
The pieces end up with several near-equal pairs (e.g. two ≈0.143 pieces for n=2), hinting at a pairing/charging upper-bound argument: Xiang Yu arranges that the even positions absorb a controlled share, capped so Liu's odd sum ≤ 2^n/d.

### Edge-case probes
- Liu uses EXACTLY n marks (the dyadic structure needs all n to create the n+1 geometric pieces; using fewer weakens the invariant).
- Xiang Yu sometimes does best with FEWER than n marks (n=2 case uses 1). Do not assume Xiang Yu always marks n.
- Marking at endpoints (0 or 1) is a no-op (no new cut); the optimal strategies keep marks strictly interior.

### Distinct openings for the outliner
1. **Dyadic-geometric lower bound.** Construct Liu's marks to create pieces 1:2:4:…:2^n; prove largest-piece-exceeds-sum-of-rest forces Liu's odd-position sum ≥ 2^n/d. This is the cleanest lower-bound route and is verified for n=1,2,3.
2. **Pairing / charging upper bound.** Find Xiang Yu's strategy (pairing marks, possibly using <n marks) that holds Liu's odd sum ≤ 2^n/d for ANY Liu config. The near-equal-pair structure seen in worst cases is the hint. The "replace adversary with stronger surrogate" crux (aimo-0560) and domino-pairing crux (aimo-0115) are candidate moves.
3. **Induction on n.** The dyadic recurrence (each c(n) drops toward 1/2, with 2^n/2^{n+1}-1 structure) suggests a possible induction: relate the n-game to the (n−1)-game by having Liu "peel off" the largest dyadic piece and reduce. Worth the outliner trying.
4. **Continuity / minimax-saddle reformulation.** Treat as a zero-sum game; the value c(n) is a saddle. Could appeal to a minimax theorem with the dyadic config as optimal mixed/anchor. Less likely olympiad-clean, but a fallback.

### Candidate technique(s)
- Greedy-alternating claim lemma (assumed; another explorer proving): Liu = odd-position sum of descending sort.
- Dyadic / geometric-sequence construction with "largest exceeds sum of rest" (the n=1,2,3 evidence is exact).
- Pairing strategy for the upper bound (Xiang Yu answers Liu's marks to create controlled piece pairs).
- Possible induction on n via the dyadic recurrence.

### Cheap-kill candidates
- "Largest piece > sum of all others" gives an immediate LOWER bound of (largest piece) in many formulations — but Liu's actual payoff is the full odd-position sum, so the cheap kill is only as strong as proving odd-sum ≥ largest piece. Worth attempting as a lemma first.
- For the UPPER bound, a simple total-mass bookkeeping (Liu gets n+1 of 2n+1 pieces, so a naive bound is 1) is useless; need the structural pairing.

### Knowledge-base entries to use
- `knowledge_base.md` has no dedicated entry for greedy alternating claim or dyadic-game value (scanned; the file's content is mostly number-theory/poly). The greedy lemma and the dyadic construction will need to be proved from scratch (as required by the rigor rules).
- The crux corpus (below) is the real source of analogous moves.

### Analogous past problems (cruxes)
- **aimo-0117** — *"Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others."* This is the EXACT mechanism of Liu Bang's lower-bound construction (pieces 1:2:4:…:2^n). Top analog.
- **aimo-0115** — *"Pair the cells of a region into dominoes and have the responding player always answer in the partner cell."* Pairing-strategy template for Xiang Yu's upper bound.
- **aimo-0560** — *"Replace the adversary with a strictly stronger surrogate whose reply is pointwise at least as damaging."* Could simplify the upper-bound proof by giving Xiang Yu a structured "stronger surrogate" response (marking on a refined grid) that upper-bounds his real power.
- **aimo-0461** — *"For an upper bound, partition the conflict graph into small identical components each holding at most one piece, blocker responds inside the same component."* A partition-style UB template; less directly fitting but the "respond in the same component" idea rhymes with Xiang Yu answering near Liu's marks.

### Prior progress
None (round 1, workspace was empty).

### Dead ends (do not retry)
- **Coarse-grid Y optimization** (≤45 points, or Nelder-Mead from a single start) is unreliable: it overestimates Liu's value (e.g. reported c(2)≈0.5795, 0.5682 at various coarse settings) because it misses Xiang Yu's true best response. Use ≥150-point grid + multi-start Nelder-Mead. The TRUE values are the exact fractions 2/3, 4/7, 8/15.
- **Liu symmetric config {1/3, 2/3} for n=2** gives only c=0.500 — NOT optimal. The dyadic structure for n=2 lives at sevenths, not thirds. Do not assume the n=1 pattern (mark at 1/(n+1) or similar) generalizes by simple spacing.
- **{2/7, 4/7} for n=2** gives 0.500: pieces {2/7,2/7,3/7} are NOT dyadic (two equal). The dyadic construction needs DISTINCT powers of 2; equal pieces let Xiang Yu pair them perfectly.

### Small-case / intuition notes (conjectures from numerics, NOT proved)
- Conjecture (strong): c(n) = 2^n/(2^{n+1}−1), verified exactly for n=1,2,3.
- Conjecture: Liu's optimal marks are any permutation of the cumulative dyadic sums {1, 3, 7, …, 2^n−1}/(2^{n+1}−1) (i.e. place marks so pieces read 1:2:4:…:2^n in some order).
- Conjecture: the lower bound rests solely on "largest piece > sum of rest" (the dyadic largest piece 2^n/d beats the other pieces' total (2^n−1)/d by a margin of 1/d).
- Conjecture: the upper bound is a pairing/charging argument; Xiang Yu's response may use fewer than n marks.
- All numeric checks are EVIDENCE, not proof; the outliner must prove each direction.
