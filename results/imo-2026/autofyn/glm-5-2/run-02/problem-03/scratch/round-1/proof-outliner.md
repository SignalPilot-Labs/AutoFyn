## imo-2026-03

**Answer (conjecture, exact for n=1..5):** `c(n) = 2^n / (2^{n+1} − 1)`. Let `D(n) = 2^{n+1} − 1` (Mersenne), so `c(n) = 2^n / D(n)`. Limit 1/2 from above. Verified exact by rational arithmetic for n=1..5 by all three explorers.

**The recursion (load-bearing for every upper-bound route).** Let `f(n) = c(n)` = Liu's share, `A(n) = 2 f(n) − 1 = Liu − Xiang` = the alternating sum `p₁ − p₂ + p₃ − …` (Liu's advantage). Then:
- `1/f(n+1) = 1 + 1/(2 f(n))`  ⟺  `f(n+1) = 2 f(n)/(2 f(n)+1)`.
- On the advantage: `1/A(n+1) = 1 + 2/A(n)`  ⟺  `A(n) = 1/D(n)` (base A(0)=1).
- **Möbius linearization:** `u(n) := −1/A(n)` satisfies the **linear** recursion `u(n+1) = 2 u(n) − 1`, `u(0) = −1`, hence `u(n) = −D(n) = −(2^{n+1}−1)`. (Verified n=0..5.)
- The upper bound `Liu ≤ f(n)` is **equivalent** to `A ≤ 1/D(n)` is **equivalent** to `u ≤ −D(n)`.

**Shared structure (every slug includes this whole proof; the lower bound half is the same across slugs, the upper-bound route diverges).** Each slug must contain:

- **Lemma G (greedy-picking reduction, load-bearing).** After all marks are placed, with M ≤ 2n+1 pieces sorted descending p₁ ≥ … ≥ p_M, optimal play by BOTH players in the alternating-pick phase is greedy (always take the largest unclaimed piece); the outcome is Liu = p₁ + p₃ + p₅ + … (odd ranks), Xiang = even ranks. *Mechanism:* exchange / backward-induction — Liu deviating from greedy leaves Xiang able to grab p₁ (the current largest) on his turn; since p₁ ≥ p₂, p₃ ≥ p₄, … the alternating greedy split is the unique subgame-perfect outcome. *Gap:* write the formal exchange argument (the explorers verified 0/2000 minimax mismatches, but that is evidence, not proof).
- **Lemma L (Liu's lower bound — dyadic config).** Liu places his n marks at the cumulative sums of (1, 2, 4, …, 2^{n−1})/D(n), i.e. at positions 1/D, 3/D, 7/D, …, (2^n−1)/D. This partitions [0,1] into pieces of lengths (1, 2, 4, …, 2^n)/D(n). Claim: for EVERY Xiang response (any ≤ n marks), Liu's odd-rank sum ≥ 2^n/D(n). *Mechanism (aimo-0117 crux adapted):* the largest Liu interval 2^n/D strictly exceeds the sum of all the others (2^n > 2^n − 1), so the dominant piece pins the top odd rank; the geometric/rapidly-decreasing structure starves Xiang of a small-enough interval to shred profitably. *Gap:* formal robustness/induction-on-Xiang's-marks argument that the alternating sum stays ≥ 1/D(n) under any refinement (the lower-bound fixed-point of the same recursion A ↦ A/(A+2), but in the direction "Xiang cannot push A below 1/D on the dyadic config").
- **Lemma S (small-n verification).** Exact-rational check n=1..5 (computation done by explorers). State c(1)=2/3, …, c(5)=32/63. This is verification, not proof; include as a check.

---

### `induct-one-mark` : new
**Target:** c(n) = 2^n/(2^{n+1}−1) end-to-end (lower bound + upper bound + small-n).
**Technique:** Strong induction on n (the number of Xiang marks), via a **one-mark reduction lemma** that factors the recursion `1/f(n+1) = 1 + 1/(2 f(n))`. This is the most direct inductive framing.
**Skeleton:**
  1. Lemma G (greedy → odd-rank sum). — by exchange/backward-induction.
  2. Lemma L (Liu dyadic lower bound, shared). — by dyadic dominance + induction on Xiang's marks.
  3. Lemma S (small-n check).
  4. **Inductive hypothesis (upper bound):** For any partition of an interval of total length L into n+1 Liu-intervals, Xiang with n marks can force Liu's odd-rank sum ≤ f(n)·L. (Base n=0: trivial, Liu = L = f(0)L. n=1: hand-prove the two-mode cap, see below.)
  5. **One-mark reduction lemma (THE GAP):** Given any partition of [0,1] into n+2 intervals (Liu has n+1 marks), Xiang has a SINGLE first mark reducing the game to an n-mark instance with the right scaling so that IH + the recursion `f(n+1) = 2 f(n)/(2 f(n)+1)` closes the bound. The recursion factorization reads: the "+1" in `1/f(n+1) = 1 + 1/(2 f(n))` is the unit of advantage Xiang secures with this one mark; the "1/(2 f(n))" is the residual (n)-game on a half-scaled interval. The two micro-modes observed at n=1 generalize:
     - **(i) Bisect-halve mode:** when the largest interval M ≥ f(n+1), Xiang splits M so a controlled half partners the top rank (the "+1" unit).
     - **(ii) Sliver-shred mode:** when all intervals ≤ f(n+1), Xiang places a mark ε-close to a boundary, creating a tiny piece that pins Liu's top odd rank to a fixed large piece minus ε (the n=1 "Liu = 1−a" tactic, generalized by induction on the remaining intervals).
  6. Combine: by IH, after the one reduction mark, Xiang's remaining n marks cap the residual game at f(n) of the residual mass; algebra `f(n+1) = 2 f(n)/(2 f(n)+1)` yields Liu ≤ f(n+1). ∎
**Key lemmas (claim + mechanism):**
  - *One-mark reduction lemma* — because the recursion `1/f(n+1) = 1 + 1/(2 f(n))` decomposes into "one secured even-rank unit" + "a residual (n)-game at half scale", and the n=1 base case exhibits exactly this decomposition in the two regimes (M ≥ 1/3: bisect; M ≤ 1/3: sliver).
  - *n=1 base cap (verified, the model for the reduction):* Liu has 2 intervals (a, 1−a), a ≤ 1/2. If a ≤ 1/3, Xiang bisects the big interval → Liu = (1+a)/2 ≤ 2/3. If a ≥ 1/3, Xiang shaves a sliver ε off the big interval → sorted (1−a−ε, a, ε), Liu = (1−a−ε) + ε = 1−a ≤ 2/3. — because the sliver lands at rank 3 (Liu's) and exactly compensates the ε shaved from rank 1.
**Open gaps:** (1) the formal greedy exchange argument; (2) the lower-bound robustness proof on the dyadic config; (3) **the one-mark reduction lemma** — constructing Xiang's first mark and proving the residual game is an (n)-instance at half scale. This is the load-bearing gap; the bisect/sliver two-mode split must be shown exhaustive and to land exactly on `f(n+1) = 2 f(n)/(2 f(n)+1)`.
**Cases to cover:** the bisect regime (large interval) vs the sliver regime (all intervals small), at each inductive level; the boundary case where M = f(n+1) exactly.
**Watch out for:** explorers flagged that "split-largest-into-equal-halves" and "split-all-equal" and "split-n-largest" all FAIL as universal heuristics — the one-mark reduction is NOT a one-line greedy rule; the right mark depends on the whole partition. Also: splitting the largest piece flips the parity of every subsequent piece (p₂ moves even→odd), inflating Liu — the reduction lemma must account for this parity flip, not ignore it.
**Why this route might succeed:** the recursion is the exact inductive signature, and the n=1 base case gives a clean two-mode template; where it might fail: the one-mark reduction for general n may not close — the "residual (n)-game at half scale" may not be a clean (n)-instance because the parity flip scrambles the structure.

---

### `potential-linearize` : new
**Target:** c(n) = 2^n/(2^{n+1}−1) end-to-end.
**Technique:** **Möbius linearization of the recursion.** Define the potential `u(partition) := −1/A(partition)` where `A = p₁ − p₂ + p₃ − …` is the alternating sum (= Liu's advantage = 2·Liu − 1). The nonlinear recursion `A ↦ A/(A+2)` becomes the **linear** map `u ↦ 2u − 1`. Prove Xiang's per-mark move drives `u` by `u ↦ 2u − 1` (a monovariant in the linearized coordinate), giving `u ≤ −D(n)` after n marks ⟺ Liu ≤ f(n). This is a potential/monovariant framing (aimo-0019 amortized-potential and aimo-0236 "regime-preserved monovariant" style), NOT induction on n.
**Skeleton:**
  1. Lemma G (greedy → odd-rank sum) and the identity `Liu = (1 + A)/2`, `A = Σ (−1)^{i+1} p_i`.
  2. Lemma L (Liu dyadic lower bound, shared).
  3. Lemma S (small-n check).
  4. **Define the potential:** `u(P) := −1/A(P)` for a partition P with A(P) > 0 (Liu-favoring). Note `u < 0`. Target: after n Xiang marks, `u ≤ −D(n)`.
  5. **Per-mark lemma (THE GAP):** For any partition P with `u(P) = U`, Xiang has a mark producing a refined partition P' with `u(P') ≥ 2U − 1` (i.e., u grows in magnitude by the linear rule). Equivalently (inverting), `A(P') ≤ A(P)/(A(P) + 2)`. The mechanism to attempt: when Xiang splits a piece p_k into (x, p_k − x) landing at adjacent ranks (k, k+1), the alternating sum changes by `ΔA = −2·((−1)^{k+1} x + T)` where T = tail alternating sum Σ_{i>k} (−1)^{i+1} p_i (derive this identity). Xiang chooses (k, x) to maximize the drop. Show the optimal drop achieves `A' ≤ A/(A+2)`.
  6. Iterate: `u_0 = −1` (no marks, A=1), after n marks `u_n ≥ T^n(−1) = −(2^{n+1}−1) = −D(n)`. Hence `A ≤ 1/D(n)`, Liu ≤ f(n). ∎
**Key lemmas (claim + mechanism):**
  - *Per-mark linear-advance lemma* — because splitting a piece at adjacent ranks changes A by the closed form `ΔA = −2·((−1)^{k+1} x + T)`, so Xiang controls ΔA via (k, x); optimizing over k and x yields exactly `A' = A/(A+2)` (the fixed-point drop), which is `u' = 2u − 1` in the linearized coordinate.
  - *Linearization identity* — because `u = −1/A` conjugates the Möbius map `A ↦ A/(A+2)` to `u ↦ 2u − 1` (verified n=0..5), turning a nonlinear recursion into a linear monovariant.
**Open gaps:** (1) greedy exchange; (2) lower-bound robustness; (3) **the per-mark linear-advance lemma** — proving the optimized single-split achieves `A' ≤ A/(A+2)` for EVERY partition, not just dyadic ones. The closed form `ΔA = −2·((−1)^{k+1} x + T)` is the starting point; the maximization over (k, x) and the proof that the max equals `A/(A+2)·A`'s reciprocal drop is the hard part.
**Cases to cover:** the rank k of the split piece (odd vs even — sign of (−1)^{k+1} flips the optimal direction of x); whether the two split-halves land at adjacent ranks (must verify the sorting condition `p_{k−1} ≥ p_k − x ≥ x ≥ p_{k+1}`); degenerate M=1 (one piece, n=0 base).
**Watch out for:** splitting a piece into halves that do NOT land at adjacent ranks (the closed form for ΔA then changes — the parity flip hits a different boundary); the potential u is only defined for A > 0, but Xiang might drive A ≤ 0 (Liu ≤ 1/2), which is below the target f(n) > 1/2 anyway — handle as an immediate win.
**Why this route might succeed:** the linearization removes the nonlinear recursion and reduces the upper bound to a clean per-mark potential drop with a closed-form expression for ΔA; where it might fail: the optimization `max_{k,x} ΔA` may not attain `A/(A+2)` exactly for every partition — only for dyadic ones — leaving a gap.

---

### `pairing-partner` : new
**Target:** c(n) = 2^n/(2^{n+1}−1) end-to-end.
**Technique:** **Partner-piece pairing / Hall matching** (aimo-0461 conflict-cycle cap adapted). Use `Liu = (1 + A)/2`; bound the advantage A by pairing each Liu-taken (odd-rank) piece with an ≥-sized Xiang-taken (even-rank) piece, leaving a small "leftover" equal to 1/D(n). Xiang's marks CREATE the partners. This is a matching/structural framing, not induction or potential.
**Skeleton:**
  1. Lemma G + identity `Liu = (1 + A)/2`, `A = Σ (p_{2k−1} − p_{2k})` (sum of pair-excesses).
  2. Lemma L (shared dyadic lower bound).
  3. Lemma S (small-n check).
  4. **Pairing target:** write `A = Σ_{k} (p_{2k−1} − p_{2k})` (pair (p₁,p₂), (p₃,p₄), …). Liu's excess = Σ of per-pair excesses. Goal: Xiang's marks realize a pairing with total excess ≤ 1/D(n).
  5. **Partner construction lemma (THE GAP):** For any Liu config (n+1 intervals), Xiang's n marks partition the stick into ≤ 2n+1 pieces such that the sorted-desc consecutive pairs (p_{2k−1}, p_{2k}) have excess-sum ≤ 1/D(n). Mechanism: Xiang's mark inside Liu's largest interval M creates a "partner" piece for M (a piece ≥ M's partner's excess gets absorbed); recursively, the remaining intervals form an (n−1)-pairing problem. The dyadic config's optimal response realizes exactly the pair-pile `2^n, 2^n, 2^{n−1}, 2^{n−1}, …, 3, 2, 1, 1` (each pair has zero excess except the tail `3,2` and `1,1`-ish, summing to 1/D).
  6. **Hall/matching step:** verify the partner assignment is a valid matching (each Liu piece matched to a distinct Xiang piece ≥-sized) via Hall's condition on the rank-order graph (knowledge_base: Hall's marriage theorem / SDR). The leftover unmatched mass is the 1/D(n) excess.
  7. Conclude A ≤ 1/D(n), Liu ≤ f(n). ∎
**Key lemmas (claim + mechanism):**
  - *Partner-construction lemma* — because the sorted-desc consecutive pairs naturally pair Liu-odd with Xiang-even, and Xiang's marks (placed inside Liu intervals) create partners whose sizes are controlled by the split ratio; the pair-pile `2^k, 2^k` (zero-excess pairs) is the extremal certificate (verified at the dyadic config for n=1..5).
  - *Tail-excess bound* — because the residual unpaired tail in the pair-pile sums to exactly `1/D(n) = 1/(2^{n+1}−1)` (geometric series), matching the target A.
**Open gaps:** (1) greedy exchange; (2) lower-bound robustness; (3) **the partner-construction lemma for ARBITRARY Liu configs** — showing Xiang's marks always induce consecutive pairs with excess-sum ≤ 1/D(n). The dyadic config is the tight case; non-dyadic configs must admit a strictly-better pairing. Hall condition verification is the formal crux.
**Cases to cover:** Liu intervals sorted descending (WLOG); the largest interval (Xiang's primary target); the tail (unpaired leftovers); odd vs even number of final pieces.
**Watch out for:** explorers' dead end "naive equal-pairing gives (n+1)/(2n+1)" — that is the WRONG pairing (equal pairs); the correct pairing is the dyadic-ratio pair-pile, and equal-pairing overestimates c(n). Also: "shred-the-small" (Xiang's mode ii) breaks naive pairings — the partner construction must account for shredding, not just bisecting.
**Why this route might succeed:** the pair-excess decomposition `A = Σ (p_{2k−1} − p_{2k})` is exact and the dyadic certificate is a clean pair-pile; Hall's theorem gives a rigorous matching condition. Where it might fail: for arbitrary Liu configs, Xiang's marks may not realize the pair-pile structure — the pairing may only be achievable on dyadic configs, leaving non-dyadic caps unproven by this method.

---

### `surrogate-snap` : new
**Target:** c(n) = 2^n/(2^{n+1}−1) end-to-end.
**Technique:** **Surrogate-adversary / domination-by-extremal** (aimo-0560 crux adapted: replace the real adversary by a strictly stronger surrogate whose reply is pointwise at least as damaging; a win against the surrogate transfers down). Here the surrogate is a STRONGER LIU CONFIG: snap any Liu mark-config to the dyadic config L* = {(1,2,…,2^n)/D}; show Liu's payoff under L* ≥ Liu's payoff under the real L for the SAME Xiang marks (L* dominates L). Since the dyadic config is the unique minimax saddle (verified tight for n=1..5), `c(L*) = f(n)` (Liu's guarantee on L* = f(n), AND Xiang can cap L* at f(n)), so `c(L) ≤ c(L*) = f(n)`. This is a domination/reduction framing, NOT induction on n.
**Skeleton:**
  1. Lemma G (greedy → odd-rank sum).
  2. Lemma L (Liu dyadic lower bound, shared — this doubles as the "Liu ≥ f(n) on L*" half of the saddle).
  3. **Xiang caps L* at f(n) (the upper bound on the surrogate):** construct an explicit Xiang response on the dyadic config forcing Liu = f(n) (the pair-pile response `2^n, 2^n, 2^{n−1}, 2^{n−1}, …`, verified for n=1..5). *Gap:* prove this response holds for general n (induct on the levels of the dyadic partition).
  4. Lemma S (small-n check).
  5. **Domination lemma (THE GAP):** For any Liu config L, construct a dyadic config L* (same number of marks, pieces in geometric ratio 2) such that for EVERY Xiang mark-set S, `payoff(L*, S) ≥ payoff(L, S)` (Liu does at least as well on L* as on L, under identical Xiang marks). Mechanism: the dyadic config has the largest possible largest-interval (2^n/D > 1/2) and strictly-decreasing rapidly-shrinking smaller intervals, which is the "most spread" config — any refinement hits the dominant top rank hardest on L* and the shrinking tail lightest. (The snap: move Liu's marks to the nearest dyadic-grid position; show each piecewise move is monotone non-decreasing in Liu's payoff.)
  6. Transfer: `min_S payoff(L, S) ≤ min_S payoff(L*, S) = f(n)` (the last `=` by step 3 + Lemma L). Hence c(L) ≤ f(n). ∎
**Key lemmas (claim + mechanism):**
  - *Domination lemma* — because the dyadic config is the extremal "most-spread" config (largest top, geometrically-shrinking tail), and the odd-rank sum is Schur-convex / monotone under majorization toward the dyadic extreme (the largest-interval-exceeds-sum-of-rest property, aimo-0117, makes the top rank dominant and refinement-monotone).
  - *Surrogate cap on L* — because the dyadic config admits the explicit pair-pile Xiang response (verified n=1..5), whose general-n proof is an induction on the dyadic levels (each level splits the largest remaining piece into a zero-excess pair).
**Open gaps:** (1) greedy exchange; (2) lower-bound robustness (Lemma L, shared); (3) **the domination lemma** — proving `payoff(L*, S) ≥ payoff(L, S)` for the SAME S, which requires the odd-rank sum to be monotone under a mark-snap toward the dyadic config. This is the load-bearing gap; majorization/Schur-convexity is the candidate tool but the odd-rank sum is NOT obviously Schur-convex (it is a signed sum, not a symmetric convex function). (4) the general-n Xiang cap on L* (the pair-pile response).
**Cases to cover:** the snap direction (which way to move each Liu mark); configs where L already has a piece > 2^n/D (impossible — 2^n/D > 1/2 is the max possible top piece for n marks, since n+1 pieces must fit); configs with tied piece sizes.
**Watch out for:** the domination must hold for the SAME Xiang mark-set, not just at Xiang's optimum — otherwise `min_S payoff(L*) ≥ min_S payoff(L)` does not follow. Also: the odd-rank sum is a SIGNED alternating sum, which is not a symmetric/convex function of the piece multiset, so standard majorization may not apply directly. The domination lemma is the riskiest gap of all four slugs.
**Why this route might succeed:** it bypasses the per-mark induction entirely — once the dyadic config is shown to be the global maximizer of Liu's guaranteed value (the saddle), the upper bound is just "c(L) ≤ c(L*) = f(n)". Where it might fail: the domination lemma is strong and may be false — the odd-rank sum may not be monotone under the snap, in which case this framing collapses (and a counterexample would be informative for the other slugs).

---

### Summary of proposed slugs

| slug | action | upper-bound route | main gap |
|---|---|---|---|
| `induct-one-mark` | new | strong induction on n via one-mark reduction factoring `1/f(n+1)=1+1/(2f(n))` (bisect/sliver two-mode) | the one-mark reduction lemma (per-n Xiang first mark reduces to (n−1)-game at half scale); parity-flip on tail |
| `potential-linearize` | new | Möbius linearization `u=−1/A` → linear `u↦2u−1` per mark; closed-form ΔA for adjacent-rank split | per-mark linear-advance lemma: optimized single split achieves `A'≤A/(A+2)` for every partition |
| `pairing-partner` | new | consecutive-pair excess `A=Σ(p_{2k−1}−p_{2k})`; Xiang's marks realize dyadic pair-pile; Hall matching | partner-construction lemma for arbitrary Liu configs (not just dyadic); shred-mode handling |
| `surrogate-snap` | new | dominate real Liu by dyadic surrogate L*; transfer `c(L)≤c(L*)=f(n)` (aimo-0560 surrogate) | domination lemma `payoff(L*,S)≥payoff(L,S)` for same S — odd-rank sum may not be Schur-convex |

All four are NEW (round 1, no existing approaches). All four include the shared lower bound (Lemma G + Lemma L + Lemma S) and target the whole claim `c(n) = 2^n/(2^{n+1}−1)` end-to-end. Diversity is in the **upper-bound framing**: inductive reduction vs. linearized monovariant vs. matching/pairing vs. surrogate-domination — four genuinely different routes to the same wall, so if one framing bottoms out the others do not share its gap.
