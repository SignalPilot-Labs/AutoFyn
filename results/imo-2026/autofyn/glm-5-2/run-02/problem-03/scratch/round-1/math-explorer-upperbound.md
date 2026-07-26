## imo-2026-03 — Upper-bound / adversarial-Xiang lens

### Headline

**Conjectured answer (very high confidence, numerically exact for n=1..5):**

> c(n) = 2^n / (2^{n+1} − 1).

Values: c(1)=2/3, c(2)=4/7, c(3)=8/15, c(4)=16/31, c(5)=32/63. Limit 1/2 from above. Recursion f(n+1)=2 f(n)/(2 f(n)+1), i.e. **1/f(n+1) = 1 + 1/(2 f(n))**, equivalently on Xiang's share h(n)=1−f(n): **h(n+1) = 1/(3 − 2 h(n))**, h(0)=0. Base f(0)=1 (no marks, Liu takes the whole stick).

This recursion is the load-bearing structure for BOTH halves. The match upper=lower is tight at exactly ONE Liu configuration: the **powers-of-2 partition** (intervals 1,2,4,…,2^n each ÷(2^{n+1}−1)).

### Distinct openings surfaced (each a different attack the outliner could build)

1. **Powers-of-2 lower bound (Liu's strategy).** Liu marks at cumulative sums of (1,2,4,…,2^n)/(2^{n+1}−1). Key property (verified by 200k-sample Monte Carlo for n=1..5): for this partition, Liu's odd-rank sum is **always ≥ the formula regardless of Xiang's response** — the minimum equals the formula and is attained by a *continuum* of Xiang responses, not a unique one. The proof target: show that for this Liu partition, no placement of n Xiang-marks drives the alternating (sorted-desc) odd-rank sum below 2^n/(2^{n+1}−1). The structural reason: the largest interval 2^n/(2^{n+1}−1) *strictly exceeds the sum of all the others* (2^n > 2^n − 1), so after any n cuts the largest interval still dominates and pins a lower bound on the top rank. (See crux aimo-0117 below — same "dyadic-geometric where largest beats sum of rest" move.)
2. **Recursive upper bound via 1/f(n+1)=1+1/(2 f(n))** (Xiang's strategy). The recursion factors as "Xiang spends one mark to reduce to a half-scale (n−1)-game." Candidate inductive invariant: Xiang, with n marks, facing any partition into n+1 intervals, caps Liu at f(n). The inductive step must combine two micro-strategies observed at n=1 — (a) **bisect the largest** interval into equal halves (used when Liu's smaller interval ≤ 1/3), and (b) **make a tiny piece** by placing a mark ε-close to a Liu mark / endpoint (used when the target is ≥ formula) — generalized. **GAP (load-bearing): the exact inductive invariant / one-mark reduction is not yet identified.** Simple universal heuristics all FAIL (see dead ends). The recursion is the guide but the precise "what does Xiang's first mark do" lemma is open for the outliner.
3. **Pairing / mirror upper bound.** Xiang pairs up pieces so each Liu-taken (odd-rank) piece is matched by an ≥-sized Xiang-taken (even-rank) piece, leaving Liu only the "leftover" odd rank. At the tight config the leftover equals 2^n/(2^{n+1}−1). This is the aimo-0461 / aimo-0854 pairing-move flavor. Useful as a *cross-check* on the recursive bound but unlikely to be the whole proof (the cap is < 1/2 + leftover in general; pairing alone usually yields the coarser 1/2).
4. **Surrogate-adversary upper bound** (aimo-0560 crux). Replace Liu's real mark configuration by a *stronger surrogate* whose reply is pointwise ≥ damaging; prove the bound against the surrogate, transfer down. Candidate because the real Liu partition is arbitrary continuous — a surrogate that snaps Liu's marks to the dyadic grid might make the cap provable without casework on positions.

### Candidate technique(s)

- **Induction on n with the halving recursion** 1/f(n+1)=1+1/(2 f(n)). The factor 2 in "2 f(n)" is the tell that each step halves something.
- **Pairing strategy** for the upper bound (partner-cell / mirror).
- **"Largest-exceeds-sum-of-rest" dyadic construction** for the lower bound.
- Monotonicity of the sorted-desc alternating sum under refinement of the partition (the lower bound at powers-of-2 holds for *all* refinements — a monotonicity/robustness lemma).

### Cheap-kill candidates

- **Parity/rank identity:** Liu's take = (1 + Σ(−1)^{i+1} p_i)/2 where p_i are pieces sorted desc. So Xiang minimizes Liu ⟺ Xiang minimizes the alternating sum. Reformulate the upper bound as "Xiang forces the alternating sum ≤ 1/(2^{n+1}−1) · 2 = 2/(2^{n+1}−1)·... " — i.e. Liu−Xiang ≤ 2 f(n)−1 = (2·2^n − (2^{n+1}−1))/(2^{n+1}−1) = 1/(2^{n+1}−1). So the **upper bound is: Xiang forces (Liu's take − Xiang's take) ≤ 1/(2^{n+1}−1).** This is a clean target. (Liu's lower bound at powers-of-2 makes this difference exactly 1/(2^{n+1}−1).)
- **Dyadic bucket / size bound:** the largest interval M ≥ 1/(n+1). Cases M ≥ 2^n/(2^{n+1}−1) vs M ≤ that. In the first case Liu is already "too big" and Xiang attacks M; in the second case the partition is fine and Xiang attacks the smallest. This is the n=1 proof generalized.

### Knowledge-base entries to use

- **Hall's marriage theorem / SDR** (combinatorics) — for a pairing-style upper bound, pairing odd-rank pieces to even-rank pieces via a matching condition.
- **Pigeonhole / extremal principle** + **Invariants & monovariants** — the recursion 1/f(n+1)=1+1/(2 f(n)) is a monovariant-style reduction.
- **Constructive / incremental** (combinatorics) — the powers-of-2 Liu construction.
- **General: Induction, Contradiction, Pigeonhole/extremal** (general proof methods).
- **Pólya heuristics:** "specialize to small n" (we did n=1,2,3) and "find analogous problem."

### Analogous past problems (cruxes)

1. **aimo-0117 (Dutch TST 2021)** — crux: "Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others." *Genuinely analogous:* Liu's extremal partition is dyadic with largest interval 2^n/(2^{n+1}−1) > (sum of the rest) = (2^n−1)/(2^{n+1}−1). Same crux move (geometric/dyadic construction where the top element dominates). Adapt, do not cite — the surrounding game is different.
2. **aimo-0560 (IMO-SL 2022, lumberjack/gardener)** — crux: "Replace the adversary with a strictly stronger surrogate whose reply is pointwise at least as damaging, so a win against the surrogate transfers down." *Candidate technique* for the upper bound (arbitrary Liu partition → snap to dyadic-grid surrogate). Hint only.
3. **aimo-0461** — crux: "Cap each disjoint conflict-cycle at one placement by having the responder immediately occupy the mover's cyclic-opposite vertex" + "partition conflict graph into small components each holding one." *Pairing-flavor* upper bound analogy for matching Liu's odd-rank pieces to Xiang's even-rank pieces. Weaker analogy.

No crux in the corpus is a direct match (no cake/stick + alternate-picking problem in the 2026-disjoint set).

### Prior progress

None (round 1, no approaches, no lemmas, status `unsolved`).

### Dead ends (do not retry)

- **"Split each Liu interval into equal halves" (all n marks, one per interval or bisection) does NOT cap.** For n=2, Liu=(1/5,2/5,2/5): equal-splitting gives 5 equal pieces → Liu = 3/5 = 0.6 > 4/7. So the naive "(n+1)/(2n+1) equal-pieces" conjecture is FALSE; it overestimates c(n). Do not pursue c(n)=(n+1)/(2n+1).
- **"Recursively halve the largest interval"** (greedy split-largest-into-equal-halves) does NOT cap for n≥2. On random partitions it leaves Liu as high as 0.736 (n=2), far above 4/7. At the powers-of-2 partition for n=3 it gives 9/15=0.6 > 8/15. Rejected as the upper-bound strategy. (It does coincidentally hit 4/7 at n=2 powers-of-2, but not generally.)
- **"Put all n marks into the largest interval, split into n+1 equal sub-pieces"** fails (n=2 random worst 0.711 > 4/7).
- **"Split the n largest intervals in half"** fails (n=2 worst 0.744).
- **Equal Liu partition (1/(n+1),…)** is a BAD Liu strategy: Xiang caps Liu at ~1/2 (verified n=2,3). Liu must use the dyadic partition, not the equal one.

### Small-case / intuition notes (CONJECTURE, numerically verified not proved)

- **n=1: c(1)=2/3 (exact, hand-proved).** Liu marks at 1/3 (intervals 1/3, 2/3). Xiang's best: split the 2/3 → 1/3+1/3, all three pieces 1/3, Liu takes ranks 1,3 = 2/3. For any other Liu split a, Xiang forces ≤ 2/3 (case a≤1/3: bisect larger, Liu=(1+a)/2≤2/3; case a≥1/3: make-tiny, Liu=1−a≤2/3).
- **n=2: c(2)=4/7 (DE-verified to 1e-6, both bounds).** Liu marks at 1/7, 3/7 (intervals 1/7, 2/7, 4/7). Liu's odd-rank sum ≥ 4/7 for ALL Xiang responses (200k sample min = 4/7). Xiang's optimal uses both marks INSIDE the largest interval (4/7), splitting it into three pieces (a continuum of optimal splits, e.g. 0.294, 0.245, 0.032); the two smaller Liu intervals are left untouched. Xiang caps every tested random partition at ≤ 4/7 (DE).
- **n=3: c(3)=8/15 (verified).** Liu=(1/15,2/15,4/15,8/15); same robustness. Xiang's optimal again puts all 3 marks inside the largest interval (8/15).
- **n=4: c(4)=16/31; n=5: c(5)=32/63** — lower-bound robustness verified by sampling; DE Xiang-best hits the formula exactly at powers-of-2.
- **Tight case is unique:** among many tested partitions (equal, one-tiny, one-huge, powers-of-2), ONLY the powers-of-2 partition makes Xiang's cap equal the formula; every other partition lets Xiang force strictly less (often exactly 1/2). This uniqueness is itself a strong hint that the extremal structure is dyadic.
- Intuition: Liu's largest interval 2^n/(2^{n+1}−1) is just over 1/2 and *exceeds the sum of all other intervals*. Xiang cannot "dilute" it below the formula because even devoting all n marks to split it, the dominant piece keeps the odd-rank top, and the smaller (untouched) intervals conspire to keep the lower odd ranks small for Liu. The 1/2 floor is Xiang's easy win on any non-dyadic partition; the dyadic partition is the unique configuration where Liu holds Xiang exactly at the formula.

### Match upper vs lower (the whole ballgame)

- **Lower bound (Liu):** dyadic partition → Liu ≥ 2^n/(2^{n+1}−1) for all Xiang. Robust/monotonicity lemma. Numerically airtight for n≤5; proof target = show the alternating sum stays ≥ 1/(2^{n+1}−1).
- **Upper bound (Xiang):** for ANY Liu partition, Xiang caps Liu ≤ 2^n/(2^{n+1}−1). The cap is achieved by an inductive strategy guided by 1/f(n+1)=1+1/(2 f(n)). Numerically airtight (DE) for n≤3 on many edge-case partitions, tight ONLY at the dyadic partition. **The explicit inductive one-mark reduction is the open gap** — the outliner must construct it. Simple heuristics (split-largest-halves, split-all-equal, split-n-largest) all fail, so the proof is genuinely the recursion argument, not a one-line greedy.

### Flags

- **Greedy-picking reduction (load-bearing lemma):** I trusted the run_state rule (both pick greedily, Liu gets odd ranks). Sanity-checked on small examples (0.5/0.3/0.2, 0.4/0.35/0.25, 0.4/0.4/0.2) — greedy is optimal for Liu in all. NOT rigorously re-proved here; the outliner should prove the exchange argument (deviating lets Xiang grab p1, and p1+p3+… ≥ p2+p4+… since p1≥p2, p3≥p4,…).
- The cap at non-dyadic partitions often lands *exactly* at 1/2 (equal partition → 1/2; one-tiny → 1/2; one-huge → 1/2). Suggests a two-regime proof: dyadic-tight regime (cap = formula) and "everything else" regime (cap ≤ 1/2 < formula).
- Marks "at most n": using FEWER marks is sometimes optimal for Xiang (e.g. n=1, a≥1/3, make-tiny uses 1 mark but the tiny piece needs a mark — actually all strategies use exactly n marks here; but the "≤ n" freedom should be handled in the proof).
