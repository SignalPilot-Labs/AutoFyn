## imo-2026-03 — Lower bound (Liu Bang's guarantee) lens

**Setup recap.** Stick [0,1]. LB marks ≤n points, then XY marks ≤n points (distinct from LB's and each other's). Cut at all marks → pieces. Claim alternately, LB first, each maximizing own total. Find largest c(n) LB can guarantee.

**Key mechanical fact used throughout (should be a named lemma in the outline).** On any fixed multiset of piece lengths, if both players simply always grab the currently-largest unclaimed piece, this is optimal for *both* (standard exchange argument: swapping a smaller current pick for a larger available one can only help, and this is a zero-sum item-partition game with no synergies between pieces). Hence with the final piece multiset sorted descending, LB (mover 1) gets exactly the pieces at odd ranks (1st, 3rd, 5th, …) and XY gets the even ranks. I did **not** find this fact named in `knowledge_base.md` — it should be proven from scratch as the first lemma (an easy exchange/interchange argument), not cited.

## Numerical experiment (this is the core of my lens)

I built a Python model (`scipy.optimize.minimize`, Nelder–Mead, many random restarts, per split-composition) that, given LB's n+1 initial segment lengths, brute-force searches XY's best response over (a) how he distributes his n points among the n+1 segments (all integer compositions of n into n+1 parts) and (b) where exactly he places them within each chosen segment — then reports XY's best-response value (= LB's guaranteed share for that LB configuration). I then searched over LB's segment-length choices (grid search + local perturbation) to find the configuration maximizing this worst case.

**Result, confirmed for n = 1, 2, 3, 4 (all reproduced to 6+ decimal places):**

LB's optimal segments are **geometric with ratio 2**: lengths
`ℓ_i = 2^i / (2^{n+1} − 1)` for `i = 0, 1, …, n` (n+1 segments, marks at the partial sums `(2^{i}-1)/(2^{n+1}-1)`... i.e. cumulative sums of these lengths). This yields the guaranteed value

**c(n) = 2^n / (2^{n+1} − 1)**

Checked numerically:
- n=1: 2/3 = 0.6667 — exact closed-form derivation (see below) matches search exactly.
- n=2: 4/7 = 0.5714286 — matches search to 10 decimal places, confirmed against many perturbations of the (1,2,4)/7 profile (none beat it).
- n=3: 8/15 = 0.5333333 — matches search.
- n=4: 16/31 = 0.5161290 — matches search; several distinct XY compositions ((0,0,0,0,4), (0,0,0,2,2), (0,0,1,1,2), (0,0,0,1,3)) all tie at exactly this value, only (1,1,1,1,0) (splitting each small segment once, leaving the largest alone) is much worse for XY (0.629) — i.e. it is *not* optimal for XY to spread splits across all segments; the largest segment(s) absorb the splitting budget.

As n→∞, c(n) → 1/2 + 1/2^{n+2}·(1+o(1)) — i.e. LB's edge over the fair 1/2 split shrinks geometrically, which is intuitively right: with more marking power for both sides the game becomes more symmetric, but LB's first-mover-in-both-phases advantage never vanishes.

**Exact hand derivation for n=1 (fully rigorous, not just numeric).** LB marks one point splitting [0,1] into L ≤ R = 1−L. XY adds one point, splitting either L or R into x, (segment−x). Working out the median of the resulting 3 pieces as a function of x (XY's only freedom) shows: if L ≤ R/2, XY's best response is to bisect R exactly, giving pieces {L, R/2, R/2}; if L > R/2, XY's best is to barely nick R (or L) so the piece of length L survives as the median-defining value, giving LB total 1−L. LB's value is (1+L)/2 for L≤1/3, and 1−L for L≥1/3; maximized at **L = 1/3**, giving c(1) = 2/3, and the resulting configuration is XY-forced into **three equal pieces of 1/3** — LB gets 2 of them. This exact computation matches the numerical search precisely and should be portable to the outline as a fully proven base case / sanity check.

## Distinct openings (rival lower-bound strategies to hand the outliner)

1. **Geometric-segments construction + exact-tie argument (the one the search found).** LB places n marks at cumulative positions of a geometric sequence `2^0, 2^1, …, 2^n` (scaled to sum 1). Conjectured mechanism (needs proof, not yet verified structurally by me): whatever XY does, in the final sorted-descending order the pieces coming from splits of the *largest* original segment(s) interleave exactly at the odd ranks with the smaller untouched original segments at the even ranks, so LB's total telescopes to exactly the sum of the split segment(s) values, i.e. `2^n/(2^{n+1}-1)`, independent of exactly how XY chooses to split (I observed this "value is invariant across many different XY splits" phenomenon directly in the n=2 raw-pieces printout — see below). This invariance is the likely route to a clean induction proof.
   - Direct evidence for the invariance: for n=2, segments (1,2,4)/7, forcing XY to spend both points on the 4/7 segment, ANY split of that segment into 3 sub-pieces (I found the optimizer landing at wildly different splits like {0.396,0.144,0.031} vs others) gives LB exactly 4/7 — because the two untouched segments 1/7, 2/7 always land at ranks 2 and 4, sandwiching the three subpieces at ranks 1,3,5, so LB's total = sum of all 3 subpieces = the whole big segment = 4/7, *regardless of how it's split*, as long as the sort order interleaves that way (each subpiece stays under 2/7 and one stays above 1/7, etc. — the exact interleaving conditions need to be pinned down and shown to be forced).
   - This suggests an **induction on n**: prove that if XY commits his whole budget to the largest segment, the recursive sub-game structure exactly reproduces the (n−1)-point version at 1/2 the scale, giving the recursion `c(n) = ℓ_top + c(n-1)·(rest)` or similar telescoping identity that resolves to `2^n/(2^{n+1}-1)`. Someone should check whether `c(n) = c(n-1)/2 + (something)` reproduces the closed form: `2^n/(2^{n+1}-1)` vs `2^{n-1}/(2^n-1)` — algebraic relation exists and is worth deriving cleanly as the induction step.

2. **Direct "sum of odd ranks" LP/adversary bound (no construction, just an inequality).** Rather than building a specific configuration, treat LB's problem as: choose n+1 nonnegative lengths summing to 1 to maximize `min` over XY's n-point splits of (sum of odd-ranks). This is a minimax that could in principle be attacked directly via a clean combinatorial inequality (e.g., relating LB's odd-rank sum to `L + (rest)/2` type recursive bounds) without needing to guess the geometric profile first — i.e., prove the bound `2^n/(2^{n+1}-1)` is *forced* to be optimal via an adversary argument bounding any LB config from above (this would double as part of the *upper bound / XY's counter-strategy* proof — flag this as an opening that could unify both directions of the proof rather than needing two totally separate arguments).

3. **n=1 base case as a template, generalized combinatorially.** The exact n=1 computation (median-of-3 case analysis) is fully rigorous and short. It strongly suggests the right general technique is: for each of LB's n+1 segments, work out how much "protection" it has against being neutralized by XY's splitting, then optimize segment lengths to equalize marginal protection (a Lagrangian/equalization idea — at the optimum, LB should be indifferent among a few different response strategies for XY, exactly as we saw at n=1's boundary a=1/3 where both regimes tie). This equalization-at-the-margin structure is a good target for the proof-outliner: characterize the optimum by a stationarity/indifference condition rather than guessing the closed form outright.

## Candidate technique(s)
- **Exchange-argument lemma** for "greedy taking is optimal for both players in an alternating item-claim game" (state and prove first; not in KB, must be proved from scratch).
- **Extremal / equalization principle** (KB: "Pigeonhole / extremal principle", "Piecewise-concavity smoothing" for LP-flavored minimax — the median-of-3 computation for n=1 is exactly this kind of piecewise-linear optimization over a breakpoint).
- **Induction / self-similar recursive construction** (KB: "Induction: ordinary, strong, or structural… for all n constructions, build step n from step n−1"), likely the right proof skeleton given the geometric-doubling structure found numerically.
- **Constructive vs. existence** (KB Meta-Strategy): this is a find-the-extremal-value problem — needs BOTH a matching LB strategy (this lens) and an XY strategy forcing the bound tight (the other lens's job).

## Cheap-kill candidates
- None found that immediately resolve the problem, but a useful pruning fact: **XY should never split more than one (or the top few, tied) segments** — the numeric search consistently found that spreading splits across many small segments is strictly worse for XY than concentrating on the largest segment(s) (e.g. n=4: (1,1,1,1,0) gave XY only 0.371 vs 0.484 achievable by concentrating). This "concentrate, don't spread" fact for XY's best response is worth trying to prove directly (an interchange/majorization argument) — it would sharply cut the case analysis needed for both the lower- and upper-bound proofs.
- Symmetry: the problem is scale-invariant/self-similar under "zoom into the largest remaining segment," hinting that a clean recursive relation in n exists.

## Knowledge-base entries to use
- **Pigeonhole / extremal principle** — for characterizing LB's optimal segment lengths as an extremal configuration.
- **Piecewise-concavity smoothing** (Algebra section) — directly analogous machinery to the n=1 median-as-function-of-breakpoint computation; the general n case is likely also piecewise-linear in the split positions with the optimum at a breakpoint (boundary between regimes), same flavor as that KB entry's technique.
- **Induction: ordinary/strong/structural, build step n from n−1** (General Proof Methods) — likely proof skeleton given the geometric/self-similar numeric pattern.
- **Constructive vs. existence — "find all/largest n" needs upper bound AND matching construction** (Meta-Strategy / General Proof Methods) — reminder that this lens (construction) is only half the proof.

## Analogous past problems (cruxes)
I filtered `combinatorics` × `games-and-strategy` (39 cruxes) and cross-checked against `past_problems_database.json` for stick/segment/claim/alternately/length keywords. **None are genuinely analogous.** The closest by surface theme (`aimo-0596`, a card-XOR pairing/parity alternating-take game; `aimo-0854`, an edge-orientation pairing game) both rely on a *pairing/involution/mirroring* strategy for the *second* player to force a draw/loss — structurally different from this problem (continuous lengths, first player advantage, no natural involution since LB moves first in both the marking and the claiming phase). I would not force these as templates. A broader keyword search across the full problems DB for "claim"+"piece/length/stick/segment" turned up only one irrelevant geometry hit. **Verdict: no close crux match; this problem's game-tree/continuous-optimization flavor is not represented in the corpus.**

## Prior progress
None — `results/imo-2026-03/current.md` is empty (Status: unsolved, round 1 start), no approaches exist yet in the ranker.

## Dead ends (do not retry)
- **Equal-spacing construction** (LB marks at k/(n+1), i.e. n+1 equal segments): numerically verified inferior. For n=1 this is a=1/2, giving only c=1/2 (XY neutralizes by an extreme near-degenerate split, `xy_best_response` confirms 0.5000005 vs the optimal 2/3). For n=2, equal thirds (1/3,1/3,1/3) also give only 0.5000. **Root cause:** equal segments let XY create pairs of near-equal pieces that "match" LB's pieces one-for-one in the sort order, erasing LB's first-move edge; LB needs *unequal* (geometric) segments so his edge survives XY's best split.
- **The naive guess c(n) = (n+1)/(2n+1)** (matches n=1's 2/3 by coincidence): numerically refuted at n=2 — the (1,2,2)/5 profile that would realize it only guarantees 0.500, not 0.6, because XY's best response there ((2,0,0): dump both points into the *smallest* segment, splitting it into two pieces of size matching the two large 2/5 segments) neutralizes it completely. Do not pursue this formula.

## Small-case / intuition notes (conjecture, not proof)
- **Conjectured closed form: c(n) = 2^n / (2^{n+1} − 1).** Verified numerically (global search over LB configs + exhaustive-composition search over XY responses, high-precision Nelder-Mead) for n = 1, 2, 3, 4. n=1 additionally verified by exact hand computation.
- Conjectured optimal LB marking: geometric segments of length `2^i/(2^{n+1}-1)`, i=0,…,n (marks at partial sums).
- Conjectured XY best response: concentrate all n points into splitting the largest segment (or split the value ties among the top few segments) — never spread thin across all n+1 segments.
- Conjectured invariance: once XY commits to splitting only the largest segment, LB's total is *invariant* to exactly where within it XY places his n sub-marks (as long as the resulting sub-pieces interleave with the untouched smaller segments in a specific order) — this "splitting doesn't matter once XY is confined to the top segment" phenomenon is the likely crux of a clean inductive proof and is worth the outliner's first attention.
