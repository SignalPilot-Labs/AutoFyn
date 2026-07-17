## Status
partial

## Approach: induction-recursion

**Framing.** Prove the whole result by induction on n, driven by the exact recursion

  c(n) = 2·c(n−1) / (2·c(n−1) + 1),   c(0) = 1,

equivalently 1/c(n) = 1 + 1/(2·c(n−1)), giving c(n) = 2^n/(2^{n+1}−1). The intended engine
is to decompose the n-mark game at the "big-piece boundary" so one round of marking reduces
the n-problem to a renormalized (n−1)-problem for both players.

**Round-2 verdict on the engine (H2): the clean n→(n−1) game separation FAILS.** The
reviewer required a front-loaded H2 check on n=2 before writing "reduce to (n−1)". I ran that
check (and n=3), and the separation does not hold as a genuine spine — it is a numerical
coincidence, not a decomposition of the game. Details below. What survives is (a) Step 1
(recursion ⇔ closed form, airtight) and (b) a new, correct reformulation of the value as an
alternating-sum minimax (promotable). The load-bearing separation lemma is refuted, so this
route needs re-planning at the mechanism level (RETHINK-level concern), while the two
salvaged lemmas are real progress.

---

## Step 1 — recursion ⇒ closed form (AIRTIGHT)

Set r(n) = 1/c(n). From c(n) = 2c(n−1)/(2c(n−1)+1),

  r(n) = 1/c(n) = (2c(n−1)+1)/(2c(n−1)) = 1 + 1/(2c(n−1)) = 1 + r(n−1)/2.

The recurrence r(n) = 1 + r(n−1)/2 has fixed point r* = 2 (from r* = 1 + r*/2). Writing
u(n) = r(n) − 2 gives u(n) = u(n−1)/2, so u(n) = 2^{−n}·u(0). With c(0)=1, r(0)=1, u(0)=−1:

  u(n) = −2^{−n},  r(n) = 2 − 2^{−n} = (2^{n+1}−1)/2^n,  c(n) = 2^n/(2^{n+1}−1).

Check c(0) = 2^0/(2^1−1) = 1 ✓, c(1) = 2/3, c(2) = 4/7, c(3) = 8/15 — matches the brute-force
minimax values. This step is complete and correct.

---

## Step 1′ — Alternating-sum reformulation (PROVEN; promotable)

Assume the greedy=odd-ranked reduction (shared lemma G1: with both players claiming the
largest available piece — optimal by the standard exchange argument on the zero-sum
difference — Liu Bang receives exactly the pieces of odd rank in the sorted-descending list).

Let the pieces after all marks be sorted descending q_1 ≥ q_2 ≥ … ≥ q_m with Σ q_i = 1.
Write
  OddSum = Σ_{i odd} q_i,  EvenSum = Σ_{i even} q_i,  AltSum := Σ_i (−1)^{i+1} q_i.
Then OddSum + EvenSum = 1 and OddSum − EvenSum = AltSum, so

  **OddSum = (1 + AltSum)/2.**    (verified numerically on random configs; identity is exact)

Because OddSum is a strictly increasing affine function of AltSum, the minimax over the
marking phase is unchanged under the substitution, and

  c(n) = (1 + A*(n))/2,  where A*(n) = max_{LB, ≤n marks} min_{XY, ≤n marks} AltSum.

Since c(n) = 2^n/(2^{n+1}−1) = 2^n/D (D := 2^{n+1}−1), we get the clean equivalent target

  **A*(n) = 2c(n) − 1 = 1/D = 1/(2^{n+1}−1).**

I.e. the whole problem is: *the minimax of the alternating sum of the sorted pieces equals
the size of Liu Bang's smallest geometric piece, 1/(2^{n+1}−1).* Confirmed at the known
optima: n=1 config {1/3,1/3,1/3} → AltSum = 1/3 = 1/D; n=2 config {2/7,2/7,2/7,1/7} →
1/7 = 1/D; n=3 config {4,4,3,2,1,1}/15 → 1/15 = 1/D. This reformulation is rigorous and
does not depend on the (failed) separation; it is a candidate shared lemma.

---

## H2 test on n=2 and n=3 — the separation FAILS (the load-bearing finding)

**What was tested.** The intended reduction (skeleton Steps 2–3): Liu Bang isolates the
smallest geometric piece P_0 = 1/D with one mark, plays the scaled (n−1)-geometric marking
on the remainder R = [1/D, 1], and invokes the induction hypothesis "LB guarantees
c(n−1)·|R| on R against XY's ≤(n−1) marks." The tempting numeric fact (which I verified) is

  c(n−1)·|R| = c(n−1)·(1 − 1/D) = [2^{n−1}/(2^n−1)]·[(2^{n+1}−2)/D]
             = [2^{n−1}·2·(2^n−1)]/[(2^n−1)·D] = 2^n/D = c(n),

so LB's share of the remainder alone already equals the full target. This is exactly the
coincidence that makes the reduction look plausible. It is not enough. There are two
independent, fatal defects.

**Defect F1 — the mark budget does not decrement.** Xiang Yu holds n marks throughout;
nothing forces XY to "spend a mark on P_0." XY may place ALL n marks inside R. Then R
carries an (n−1)-mark LB structure attacked by n XY marks — strictly outside the scope of the
(n−1) induction hypothesis, which only covers ≤ n−1 XY marks on R. The IH therefore cannot be
invoked, and the reduction is unsound. (This is precisely the "single-gap trap" the outliner
flagged: the induction never legitimately steps from n to n−1 because the opponent's resource
budget is not reduced.)

**Defect F2 — the claiming phase re-ranks globally; no boundary is rank-invariant.** Even
ignoring F1, OddSum/AltSum is a global functional of the merged sorted list, not
"an isolated P_0 term + an independent R-subgame term." I searched XY's best response to the
LB-geometric marking:

- **n=2** (LB marks 1/7, 3/7; pieces 1/7, 2/7, 4/7): XY's optimal response needs only ONE
  mark. E.g. cut the largest 4/7 → (3/7, 1/7) giving sorted {3,2,1,1}/7 (OddSum = 4/7), or
  equivalently HALVE 4/7 → (2/7, 2/7) giving sorted {2,2,2,1}/7 (OddSum = 4/7). Both are
  optimal; no 2-mark response beats 4/7.
- **n=3** (LB marks 1/15, 3/15, 7/15; pieces 1/15, 2/15, 4/15, 8/15): XY's optimal response
  uses TWO marks — bisect the largest 8/15 → (4/15, 4/15) AND cut the second piece
  4/15 → (3/15, 1/15). Result sorted {4,4,3,2,1,1}/15, OddSum = 8/15 = c(3).

In the n=3 optimum the sub-pieces originating on the two sides of ANY fixed boundary
interleave in the sorted order (the three 4/15's, the 3/15 wedged between them, etc.), and the
parity (odd/even rank) of the smallest piece P_0 = 1/15 depends on how many pieces XY
manufactures above it. There is no boundary across which ranks fail to cross, so there is no
independent renormalized (n−1)-subgame. The value is genuinely globally coupled.

**Consequence.** Skeleton Steps 2, 3, 4 (the reduction move, the LB induction, the XY
induction) all rest on H2, which is false. They cannot be written as stated. The recursion is
the correct numeric spine but is NOT realized by a clean separation on n.

---

## Salvageable direction (for the outliner to re-plan — not yet a proof)

The computations DO show a consistent structural fact worth recording: **halving the largest
piece is an optimal Xiang Yu first move** (n=1: 2/3→1/3,1/3; n=2: 4/7→2/7,2/7; n=3:
8/15→4/15,4/15 as the first of two moves). This matches the halving reading of the recursion
1/c(n) = 1 + 1/(2c(n−1)). However, after halving LB's geometric a_1 = 2^n/D into two
2^{n−1}/D's, the residual has THREE equal top pieces 2^{n−1}/D (two halves + the original
P_{n−1}) followed by 2^{n−2}/D,…,1/D — this is NOT a scaled (n−1)-geometric instance, so the
"halve ⇒ (n−1)-game" recursion faces the same global-re-ranking obstacle (F2). Recasting the
recursion as a halving-based UPPER-bound argument is plausible but still requires proving the
residual value is governed by c(n−1), which I could not close and which is exactly where the
separation obstacle reappears. Recommendation: treat the n→(n−1) separation mechanism as
RETHINK; if the recursion is kept, it must be justified by a monovariant on the merged sorted
list (via the AltSum reformulation), not by isolating a sub-stick.

---

## Approaches tried
- (round 2) induction-recursion: front-loaded the H2 game-separation check demanded by the
  outline-reviewer. Step 1 (recursion ⇒ closed form) proven airtight; derived and proved the
  AltSum reformulation (c(n) = (1+A*)/2, target A* = 1/D). H2 check on n=2 and n=3 by
  best-response search: the "isolate P_0, recurse on R" separation FAILS for two independent
  reasons — (F1) XY's mark budget never decrements from n to n−1, so the (n−1) IH is
  inapplicable; (F2) the claiming phase re-ranks all pieces globally with cross-boundary
  interleaving, so no independent (n−1)-subgame exists. The clean n→(n−1) separation is a
  numerical coincidence (c(n−1)·|R| = c(n)), not a decomposition. Core mechanism refuted;
  lower/upper bounds NOT established via this route. Salvaged: Step 1 + AltSum reformulation +
  the empirical fact that halving the largest piece is an optimal XY move.

## Current best
Two rigorous, reusable results, plus a clear refutation of the approach's engine:
1. **Recursion ⇔ closed form:** c(n) = 2c(n−1)/(2c(n−1)+1), c(0)=1 ⟹ c(n) = 2^n/(2^{n+1}−1).
   Fully proven (Step 1).
2. **Alternating-sum reformulation:** with greedy claiming, OddSum = (1 + AltSum)/2, so
   c(n) = (1 + A*(n))/2 and the target is equivalent to A*(n) = 1/(2^{n+1}−1). Fully proven
   (Step 1′), independent of any separation.
3. **Refutation of H2:** the intended n→(n−1) game separation does not hold (defects F1, F2,
   documented on n=2/n=3). This is the load-bearing gap; it is not closable by patching, it
   requires a different mechanism (monovariant on the merged list, or an entirely different
   framing for the upper bound).

Open: both the lower bound (LB geometric guarantees AltSum ≥ 1/D against any XY cuts) and the
upper bound (XY holds AltSum ≤ 1/D against any LB marking) remain unproved within this route.
The upper bound is the field-wide hard core (per the outline-reviewer's Diversity note).

## Promotable lemmas
- **Alternating-sum reformulation (proved, Step 1′).** Under greedy=odd-ranked claiming (G1),
  for sorted-descending pieces q_1 ≥ … ≥ q_m summing to 1, Liu Bang's take equals
  OddSum = (1 + AltSum)/2 where AltSum = Σ_i (−1)^{i+1} q_i. Hence the game value satisfies
  c(n) = (1 + A*(n))/2 with A*(n) = max_LB min_XY AltSum, and the claim c(n) = 2^n/(2^{n+1}−1)
  is equivalent to A*(n) = 1/(2^{n+1}−1). Reusable by all three approaches (it simplifies the
  target functional). Proof is the exact identity OddSum + EvenSum = 1, OddSum − EvenSum =
  AltSum.
- **Recursion ⇔ closed form (proved, Step 1).** c(n) = 2c(n−1)/(2c(n−1)+1), c(0)=1 has closed
  form c(n) = 2^n/(2^{n+1}−1) (via r(n)=1/c(n)=2−2^{−n}). Reusable for the final-answer
  verification in any approach.
