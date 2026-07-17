# upper-general-cascade (copy-of direct-constructive)

Twin of `direct-constructive`, focusing its new work on the sole remaining upper-bound wall:
the general-n Case-B **hard regime** upper bound via the **pair-creation fragment cascade**
(Lemma H mechanism, fragment cuts allowed). The lower bound and the closed upper-bound slices
are imported from `direct-constructive` / the certified `lemmas/` cache.

## Status
partial

## Approaches tried
- **upper-general-cascade (round 7, this file)** — ADVANCED (B2). (1) **Corrected a real arithmetic
  overclaim**: the double-cancel entry's IH(n−1) threshold is **3·2^{n−2}/D**, NOT 2^{n−1}/D (50%
  too small); moreover the double-cancel move needs the extra domination a_1 − a_2 ≥ a_3, which the
  old entry silently assumed. With the correct threshold the double-cancel residual is genuinely
  **nonempty for n ≥ 3** (empty only for n ≤ 2), so the file's earlier "B2 settled for n ≤ 2 for the
  right reason" was right only vacuously — now stated honestly. (2) **New closed region — the greedy
  full cascade.** Proved (Lemma GreedyCascade) that whenever the top piece a_1 ≥ 1/2, XY with n cuts
  cancels a_2,…,a_{n+1} in matched pairs and leaves the single leftover 2a_1 − 1, so **A = 2a_1 − 1**;
  since B2 has a_1 ≤ c(n) this gives **A ≤ 1/D**. This **closes B2 ∩ {a_1 ≥ 1/2} for ALL n** with an
  explicit closed-form strategy — and it closes *both* of the reviewer/explorer's exact residual
  witnesses (n=3 {47/90,31/135,43/270,4/45} → A = 2/45 < 1/15; n=5 {32/63,…} → A = 1/63 = 1/D exactly,
  the boundary). Verified 0 fails over 1917 random B2 configs with a_1 ∈ [1/2, c(n)], n = 2..7.
  (3) The remaining B2 residual is **a_1 < 1/2** (no dominant piece); it is closable adaptively
  (numeric min-A search: e.g. n=3 (2/5,3/10,1/5,1/10) → A = 0) but has no uniform closed-form
  strategy — it is the same fragment-cascade wall as the IH(q ≥ 5) flat residual. Honestly OPEN.
- **upper-general-cascade (round 6, this file)** — ADVANCED. Consolidated the pair-creation
  cascade upper bound into a clean induction IH(q). Proved the **IH(q)-reducible one-step lemma**
  as a pure conditional (certifiable), and proved **IH(4)-flat** rigorously (the flat-residual leaf
  for q=4). Together these give a COMPLETE proof of **IH(q) for all q ≤ 4**, hence the Case-B
  hard-regime (B1-large) upper bound for all n ≤ 4. Analysed the strengthened dual-bound
  hypothesis IH+(m) proposed by the outliner and found a **structural obstruction** (the flat
  sub-boundary is a fixed point of the halve-max recursion), so IH+(m) does NOT close the general
  flat residual as the outline hoped; recorded this honestly. General IH(q ≥ 5) flat residual and
  sub-case B2 remain OPEN (the genuine open core). Numerically: the min-A cut search finds A ≤ 1/D
  at every hard-regime config tested (n=3 hard config a=(5144,2787,1386,683)/10000 → A=18/625 < 1/15;
  n=4,5 random hard configs 0 failures), but the achieving strategies are highly adaptive with no
  single closed-form rule (verified over q=5 flat configs), which is why a uniform general cascade
  is not yet in hand.
- (inherited from direct-constructive) reduction to the odd-sum marking game (Lemma G1), odd-sum
  rewritings (Lemma R), Lemma H (Case A), Lemma X (XOR evaluator), CaseB-Reductions 1&2, the lower
  bound via the Δ-vertex inequality (★) with the round-6 dyadic Case-1/Case-2 split.

## Current best

**Answer:** c(n) = 2^n / (2^{n+1} − 1). Write D = 2^{n+1} − 1, c(n) = 2^n/D.

By Lemma G1 (certified) the claiming phase gives Liu Bang exactly the odd-ranked pieces, and the
value of the whole game equals the minimax of the odd-sum O over LB's ≤ n marks and XY's ≤ n marks.
By Lemma R (certified), O = (1 + A)/2 with A = μ{t : N(t) odd} the sorted alternating sum, and by
Lemma X (certified) A = μ(⊕_i [0, ℓ_i]) (symmetric difference of prefix intervals of the final
piece lengths ℓ_i). Thus the XY upper bound "O ≤ c(n)" is equivalent to **A ≤ 1/D**, and the LB
lower bound to A ≥ 1/D on LB's geometric construction. The construction and lower bound are imported
from `direct-constructive` (round-6 dyadic split closes (★) modulo the flat-move termination
detail there). This file owns the **XY upper bound in the Case-B hard regime**.

By Lemma H (Case A) and CaseB-Reductions 1 & 2 (all certified), the Case-B upper bound reduces to the
**hard regime**: p = n+1 pieces a_1 ≥ … ≥ a_{n+1}, all a_i > 1/D, all consecutive gaps a_i−a_{i+1} > 1/D,
Σ a_i = 1 = (2^{n+1}−1)/D. Split on a_1:

- **B1-large (a_1 > c(n)).** XY halves a_1 (one cut; the pair {a_1/2, a_1/2} cancels in the XOR by
  Lemma X). The remaining pieces {a_2,…,a_{n+1}} are q := n pieces of sum S = 1 − a_1 < 1 − c(n)
  = (2^n − 1)/D, all > 1/D. XY has n − 1 = q − 1 cuts left. So B1-large reduces to **IH(q)** below
  with strict sum bound. **This file proves IH(q) completely for q ≤ 4** (⟹ B1-large closed for
  n ≤ 4). IH(q ≥ 5) flat residual is the open core.
- **B2 (a_1 ≤ c(n)).** Halving a_1 does not enter a strict IH instance (sum 1 − a_1 ≥ (2^n − 1)/D).
  Split again on 1/2 (note 1/D < 1/2 < c(n) for all n ≥ 1, so both parts are nonempty):
  - **B2-large (1/2 ≤ a_1 ≤ c(n)).** **CLOSED for all n** by the greedy full cascade (Lemma
    GreedyCascade below): A = 2a_1 − 1 ≤ 2c(n) − 1 = 1/D.
  - **B2-small (a_1 < 1/2).** OPEN (partial analysis below); the same fragment-cascade wall as
    IH(q ≥ 5).

**The furthest rigorous progress owned here:** (i) IH(q) is proved for all q ≤ 4 (Theorem UB below),
via the certifiable **IH-reducible** one-step lemma and the certifiable **IH4-flat** leaf lemma —
closing B1-large for n ≤ 4. (ii) **New (round 7): Lemma GreedyCascade closes B2-large (1/2 ≤ a_1 ≤
c(n)) for ALL n** with the explicit strategy A = 2a_1 − 1 ≤ 1/D. The remaining open core is the single
fragment-cascade wall in two faces: B1-large IH(q ≥ 5) flat residual, and B2-small (a_1 < 1/2).

---

## The induction IH(q) and what is proved

Throughout, D = 2^{n+1} − 1 is fixed by the ambient problem; "cut" means splitting one current
piece into two (so k cuts on a starting multiset of q pieces produce ≤ q + k pieces); by Lemma X
the score of a final multiset {ℓ_i} is A = μ(⊕_i [0, ℓ_i]), and equal lengths cancel in the XOR.
For a multiset sorted b_1 > b_2 > … (distinct) one has A = (b_1 − b_2) + (b_3 − b_4) + … (the
alternating sum), because t ∈ ⊕[0,b_i] iff #{i : b_i > t} is odd, i.e. the ON-set is
(b_2, b_1] ∪ (b_4, b_3] ∪ ….

> **IH(q).** For any multiset of q reals b_1 ≥ b_2 ≥ … ≥ b_q > 0 with sum S < (2^q − 1)/D, XY can,
> using at most q − 1 cuts, reach a final multiset with A ≤ 1/D.

**Theorem UB.** IH(q) holds for every q ≤ 4. Consequently the Case-B hard-regime upper bound
(B1-large: a_1 > c(n)) holds for every n ≤ 4.

The proof combines four ingredients, each rigorous below: the base cases IH(1), IH(2); the
imported IH(3); the reducible one-step lemma; and the flat leaf IH4-flat.

### Lemma IH-reducible (pure conditional — certifiable)

> Let q ≥ 2 and b_1 ≥ … ≥ b_q > 1/D with all consecutive gaps > 1/D and S < (2^q − 1)/D. If
> **S − max(b_1, 2b_2) < (2^{q−1} − 1)/D**, then XY can, with one cut, pass to a q−1-piece
> instance that either (i) satisfies the hypotheses of IH(q−1) with strict sum bound, or (ii) has
> some consecutive gap ≤ 1/D and is finished directly by CaseB-Reduction 2 with A ≤ 1/D. In case
> (i), if IH(q−1) holds then XY achieves A ≤ 1/D with ≤ q − 1 cuts total.

*Proof.* Note S − max(b_1, 2b_2) = min(S − b_1, S − 2b_2) (elementary: max(x,y) is the larger, so
S minus it is the smaller of S−x, S−y). Two exhaustive sub-cases.

**(a) S − b_1 < (2^{q−1} − 1)/D.** XY halves b_1 (one cut). The pair {b_1/2, b_1/2} cancels in the
XOR (Lemma X toggle with m = b_1/2 gives [0,b_1], and two copies cancel), so the active multiset is
{b_2, …, b_q}: q − 1 pieces, sum S − b_1 < (2^{q−1} − 1)/D, still all > 1/D with all gaps > 1/D
(a sub-list of the original preserves both). This is a strict IH(q−1) instance; q − 2 cuts remain.

**(b) S − b_1 ≥ (2^{q−1} − 1)/D.** Then the hypothesis forces min(S−b_1, S−2b_2) = S − 2b_2
< (2^{q−1} − 1)/D. XY cuts b_1 at b_2, producing pieces {b_2, b_1 − b_2}; the new length-b_2 fragment
cancels the intact b_2 (Lemma X). The active multiset is M := {b_1 − b_2, b_3, …, b_q}: q − 1 pieces,
sum (b_1 − b_2) + Σ_{i≥3} b_i = S − 2b_2 < (2^{q−1} − 1)/D. Every piece exceeds 1/D: b_1 − b_2 > 1/D
(original gap), b_3, …, b_q > 1/D. If, after sorting M, all consecutive gaps still exceed 1/D, this
is a strict IH(q−1) instance (case (i)). Otherwise some consecutive gap of M is ≤ 1/D; then
CaseB-Reduction 2 (certified) applied to the q − 1 pieces of M pairs the two closest pieces and
halves the other q − 3, achieving A = (that gap) ≤ 1/D with (q − 1) − 1 = q − 2 cuts (case (ii)).
In both sub-cases the residual cut budget (q − 2) suffices. ∎

The condition "S − max(b_1, 2b_2) < (2^{q−1} − 1)/D" carries **no empirical percentage**; it is the
exact boundary between the reducible region and the flat residual.

### Base cases

**IH(1).** One piece b_1 = S < 1/D, zero cuts. It is a lone singleton, A = b_1 < 1/D. ✓

**IH(2).** Two pieces b_1 ≥ b_2 > 0, S < 3/D, one cut. We claim IH(2) is entirely reducible (its
"flat residual" is empty). Indeed the flat residual would require S − max(b_1, 2b_2) ≥ (2^1 − 1)/D
= 1/D, i.e. both b_2 = S − b_1 ≥ 1/D and b_1 − b_2 = S − 2b_2 ≥ 1/D; adding, b_1 ≥ 2/D, while
S < 3/D with b_2 ≥ 1/D gives b_1 = S − b_2 < 2/D — a contradiction. So Lemma IH-reducible applies,
reducing to IH(1) (or finishing by Reduction 2). Hence A ≤ 1/D. ✓

**IH(3).** Imported from `direct-constructive` §6.2 (reviewer-verified, round 4): for three pieces
b_1 ≥ b_2 ≥ b_3 > 1/D, S < 7/D, 2 cuts, an exhaustive case split on the two consecutive gaps
achieves A ≤ 1/D. (Its reducible part is Lemma IH-reducible → IH(2); its flat residual is the
"doubly-hard leaf" settled there. Machine-verified, 0 fails.) ✓

### Lemma IH4-flat (the q = 4 flat leaf — proved here, certifiable)

> Let b_1 ≥ b_2 ≥ b_3 ≥ b_4 > 1/D with all consecutive gaps > 1/D, S = Σ b_i < 15/D, and
> **S − max(b_1, 2b_2) ≥ 7/D** (the flat residual). Then XY, with 3 cuts, achieves A < 1/D.

*Proof.* **Step 1 (small b_2).** Since max(b_1, 2b_2) ≥ 2b_2, we have S − 2b_2 ≥ S − max(b_1,2b_2)
≥ 7/D, so 2b_2 ≤ S − 7/D < 15/D − 7/D = 8/D, i.e. **b_2 < 4/D.**

**Step 2 (gap bounds).** From the gaps: b_3 < b_2 − 1/D < 3/D; b_4 < b_3 − 1/D < 2/D; and
b_3 > b_4 + 1/D > 2/D, so b_3 + b_4 > 3/D.

**Step 3 (strategy, 3 cuts).**
1. Halve b_1 → pair {b_1/2, b_1/2}, which cancels in the XOR (Lemma X).
2. Cut b_2 at b_2 − b_3 (equivalently, split b_2 into the two parts b_3 and b_2 − b_3). The new
   length-b_3 fragment cancels the intact b_3 (Lemma X). Residual singleton b_2 − b_3 remains
   (> 1/D by the gap).
3. Cut b_4 into {δ, b_4 − δ} for a small δ ∈ (0, b_4/2) chosen below.

After all cancellations the active multiset is the three singletons S₃ = {b_2 − b_3, b_4 − δ, δ},
and by Lemma X, A = μ(⊕ over S₃) = alternating sum of S₃ sorted descending. Cut count: 1 (halve b_1)
+ 1 (cut b_2) + 1 (cut b_4) = 3 = q − 1. b_3 is left intact.

**Step 4 (bound on A), two exhaustive cases on the sign of b_3 + b_4 − b_2.**

*Case (i): b_2 < b_3 + b_4.* Then b_2 − b_3 < b_4. Choose δ ∈ (0, min(b_4/2, b_3 + b_4 − b_2)); then
b_4 − δ > b_2 − b_3 and b_2 − b_3 > 1/D > δ, so the descending order is b_4 − δ > b_2 − b_3 > δ, and
A = (b_4 − δ) − (b_2 − b_3) + δ = b_3 + b_4 − b_2 (δ cancels; the bound is δ-independent). Now
b_2 > b_3 + 1/D gives b_3 + b_4 − b_2 < b_4 − 1/D, and b_4 < 2/D gives b_4 − 1/D < 1/D. Also
b_3 + b_4 − b_2 > 0 (case hypothesis). Hence **0 < A < 1/D.** ✓

*Case (ii): b_2 ≥ b_3 + b_4.* Then b_2 − b_3 ≥ b_4 > b_4 − δ. From Step 2, b_3 + b_4 > 3/D, and from
Step 1, b_2 < 4/D, so 0 ≤ b_2 − b_3 − b_4 < 4/D − 3/D = 1/D. Choose δ ∈ (0, min(b_4/2,
(1/D − (b_2 − b_3 − b_4))/2)); this interval is nonempty since b_2 − b_3 − b_4 < 1/D. Then the
descending order is b_2 − b_3 ≥ b_4 − δ > δ, and A = (b_2 − b_3) − (b_4 − δ) + δ =
(b_2 − b_3 − b_4) + 2δ < (b_2 − b_3 − b_4) + (1/D − (b_2 − b_3 − b_4)) = 1/D. Hence **A < 1/D.** ✓

The two cases are exhaustive and disjoint, so in the flat residual XY achieves A < 1/D with 3 cuts. ∎

*(Exact machine check: over all sampled q=4 hard-regime flat-residual configs the strategy gives
A ≤ 1/D, worst A·D ≈ 0.94, 0 failures, in exact rational arithmetic.)*

### Proof of Theorem UB

IH(1) and IH(2) hold (base cases). For q = 3: if the config is reducible, Lemma IH-reducible → IH(2)
gives A ≤ 1/D; otherwise it is flat and IH(3)'s imported flat-leaf case-split gives A ≤ 1/D; either
way IH(3) holds. For q = 4: if reducible, Lemma IH-reducible → IH(3) (just proved) gives A ≤ 1/D;
otherwise flat, and Lemma IH4-flat gives A < 1/D; hence IH(4) holds. Every hard-regime B1-large
configuration for n ≤ 4 reduces (after XY halves a_1) to a q = n ≤ 4-piece instance with strict sum
bound S = 1 − a_1 < (2^n − 1)/D, i.e. to IH(q) with q ≤ 4, which is now proved. Hence B1-large is
closed for all n ≤ 4. ∎

---

## The general obstruction (IH(q ≥ 5) flat residual) — honest gap

The outline proposed a strengthened dual-bound induction **IH+(m)** carrying both a sum bound and a
max bound (max < 2^{m−1}/D). We record precisely why this does **not** close the general flat
residual, so the next round does not repeat the attempt in this form.

**Fixed-point obstruction.** Consider IH(q) with a flat-residual config, S < (2^q − 1)/D and
S − max(b_1, 2b_2) ≥ (2^{q−1} − 1)/D. After ANY single pair-cancel move (halve b_1, or cut b_1 at b_2)
the active (q−1)-piece multiset has sum S − max(b_1, 2b_2) ≥ (2^{q−1} − 1)/D — i.e. it is **at or
above the IH(q−1) sum boundary**, never strictly inside the IH(q−1) range. (This is the very
definition of "flat residual": both S − b_1 and S − 2b_2 are ≥ the sub-boundary.) So one
pair-cancel cannot descend into a strict IH(q−1) instance. Moreover the geometric config
b_k = 2^{q−k}/D (sum exactly the boundary) maps under "halve b_1" to the geometric config with q−1
pieces (again exactly at the boundary): the boundary flat config is a **fixed point** of the
halve-max recursion, and there A = 1/D exactly. Carrying the extra max bound b_2 < 2^{q−2}/D does
not repair this: after halving b_1 the new sum is S − b_1 ≥ (2^{q−1} − 1)/D, so the sub-instance is
not in IH+(q−1)'s (strict-sum) range either — the max bound shrinks one resource but the sum bound
does not shrink at all. Hence **IH+(m) with the halve-max descent stalls at every flat level ≥ 5**,
exactly as IH+ with the single sum bound does. The dual bound is not the missing ingredient.

For q = 4 the flat residual is nonetheless closable, because IH4-flat does **not** recurse: it
collapses the four pieces to **three explicit singletons** {b_2 − b_3, b_4 − δ, δ} and bounds their
alternating sum directly using b_2 < 4/D. For q = 5 the analogous collapse leaves a residual of size
~b_3 with only the weak bound b_2 < 8/D, which is too large (b_2 − b_3 can exceed 4/D), and no fixed
4-cut cross-pair works (verified: cross-pair A = |(b_2−b_3) − (b_4−b_5)| fails on ~50% of q=5 flat
configs). The min-A cut search does find A ≤ 1/D at every q = 5 hard config, but the achieving
strategies are **highly adaptive** (different pairings per config — verified across many q=5 flat
configs), so there is no single closed-form cascade to prove. **This is the genuine open core.**

What is needed (for a future round): either (a) a global optimisation / compactness argument showing
the geometric config maximises min-A (the min-A search shows geometric is the worst case A = 1/D and
all others are strictly below, so a "geometric is extremal" theorem would finish — but the relevant
functional has interior valleys, per the r3 graveyard, so naive concavity fails), or (b) a
multi-level collapse that, at each flat level, records a *bounded number* of controlled singletons
and proves their total alternating contribution stays < 1/D. Neither is in hand.

## Sub-case B2 (a_1 ≤ c(n))

B2: p = n+1 pieces a_1 ≥ … ≥ a_{n+1}, all > 1/D, all gaps > 1/D, Σ = 1 = (2^{n+1} − 1)/D, with
a_1 ≤ c(n) = 2^n/D (no piece as large as c(n)+; note c(n) > 1/2 for all n since 2^{n+1} > D, and
1/D < 1/2 since D > 2, so 1/D < 1/2 < c(n)). Halving a_1 does not enter a strict IH instance (sum
1 − a_1 ≥ 1 − c(n) = (2^n − 1)/D sits at/above the IH(n) boundary — the same fixed-point obstruction
as the flat residual). We split B2 at a_1 = 1/2.

### Lemma GreedyCascade (closes B2-large, a_1 ≥ 1/2, for all n — proved here, certifiable)

> **Statement.** Let b_1 ≥ b_2 ≥ … ≥ b_p > 0 with Σ_{i} b_i = 1 and **b_1 ≥ 1/2**. Then XY, using
> exactly p − 1 cuts, reaches a final multiset whose XOR-measure (Lemma X) is **A = 2b_1 − 1**.
> Consequently, if in addition b_1 ≤ c(n) = 2^n/D then A ≤ 1/D. (Applied with p = n + 1, the p − 1 = n
> cuts are within XY's budget.)

*Proof.* Define leftovers by r_1 := b_1 and, for j = 1, …, p − 1, XY performs the cut:

  **cut the current leftover r_j at length b_{j+1}** — i.e. split the length-r_j piece into a piece
  of length b_{j+1} and a piece of length r_{j+1} := r_j − b_{j+1}.

This cut is *legal* (a length-b_{j+1} sub-piece fits inside a length-r_j piece) precisely when
r_j ≥ b_{j+1}, which we now verify for every j. By the recursion r_{j+1} = r_j − b_{j+1} and r_1 = b_1,

  r_j = b_1 − (b_2 + b_3 + … + b_j)  (empty sum for j = 1),

so the legality condition r_j ≥ b_{j+1} is equivalent to **b_1 ≥ b_2 + b_3 + … + b_{j+1}**. The
right-hand side is largest at j = p − 1, where it equals b_2 + … + b_p = 1 − b_1. Since b_1 ≥ 1/2,
we have 1 − b_1 ≤ 1/2 ≤ b_1, hence b_1 ≥ b_2 + … + b_p ≥ b_2 + … + b_{j+1} for **every** j ≤ p − 1.
Thus every cut is legal and every leftover satisfies r_{j+1} = r_j − b_{j+1} ≥ 0 (indeed
r_j ≥ b_{j+1} > 0 for j ≤ p − 1).

Track the multiset of lengths. Start {b_1, …, b_p}. Cut 1 replaces b_1 (= r_1) by {b_2, r_2}, giving
{b_2, b_2, r_2, b_3, …, b_p} — two copies of b_2. Cut 2 replaces r_2 by {b_3, r_3}, giving two copies
of b_3; and so on. Inductively, after cut j the length b_{i} (for 2 ≤ i ≤ j + 1) is present in
exactly two copies (one original intact piece, one created fragment) and the remaining originals
b_{j+2}, …, b_p and the leftover r_{j+1} are single. After the final cut p − 1 the multiset is

  {b_2, b_2, b_3, b_3, …, b_p, b_p, r_p},  where  r_p = b_1 − (b_2 + … + b_p) = b_1 − (1 − b_1) = 2b_1 − 1.

By Lemma X (certified), A = μ(⊕_i [0, ℓ_i]) over final lengths ℓ_i. Each value b_i (i ≥ 2) occurs an
**even** number of times (exactly twice), so [0, b_i] ⊕ [0, b_i] = ∅ contributes nothing; only the
single leftover r_p survives. Hence **A = μ([0, r_p]) = r_p = 2b_1 − 1** ≥ 0. (This is exact and holds
even if some b_i coincide, since we literally created a matching second copy of each cancelled length.)
Finally, if b_1 ≤ c(n) then A = 2b_1 − 1 ≤ 2·(2^n/D) − 1 = 2^{n+1}/D − (2^{n+1} − 1)/D = 1/D. ∎

**Application to B2-large.** For any B2 config with 1/2 ≤ a_1 ≤ c(n) (arbitrary n, gap conditions not
even needed), GreedyCascade with p = n + 1 gives A = 2a_1 − 1 ≤ 1/D using n cuts. At the boundary
a_1 = c(n) it gives A = 1/D exactly — matching the tightness of the answer. **B2-large is closed for
all n.** (Numeric confirmation: 0 failures over 1917 exact random B2 configs with a_1 ∈ [1/2, c(n)],
n = 2..7; both reviewer/explorer residual witnesses close — n=3 {47/90,31/135,43/270,4/45}: cascade
r_2 = 79/270, r_3 = 36/270, r_4 = 12/270, so A = 2/45 < 1/15; n=5 {32/63,2/15,73/630,31/315,17/210,4/63}
at a_1 = c(5): A = 1/63 = 1/D.)

### Sub-case B2-small (a_1 < 1/2) — honest gap, with a corrected partial entry

Here no piece dominates the rest (a_1 < 1 − a_1), so GreedyCascade's domination fails at the last
step and the single-leftover cascade no longer collapses to 2a_1 − 1.

**Corrected double-cancel entry (arithmetic fix).** Cutting a_1 at a_2 (cancel a_2) and then cutting
the residual a_1 − a_2 at a_3 (**requires a_1 − a_2 ≥ a_3**; cancel a_3) removes mass 2a_2 + 2a_3,
leaving n − 1 active pieces {a_1 − a_2 − a_3, a_4, …, a_{n+1}} of active sum 1 − 2(a_2 + a_3), with
2 cuts spent and n − 2 remaining. This is a **strict IH(n−1)** instance iff

  1 − 2(a_2 + a_3) < (2^{n−1} − 1)/D
  ⟺ a_2 + a_3 > (1 − (2^{n−1} − 1)/D)/2 = (D − 2^{n−1} + 1)/(2D) = (2^{n+1} − 2^{n−1})/(2D)
  = 3·2^{n−1}/(2D) = **3·2^{n−2}/D.**

**Arithmetic correction (this round).** The previous version of this file stated the threshold as
2^{n−1}/D; that is **wrong by exactly a factor 3/2** (50% too small). The correct threshold is
**3·2^{n−2}/D**. The geometric config a_k = 2^{n+1−k}/D sits *exactly* on it: a_2 + a_3 = 2^{n−1}/D +
2^{n−2}/D = 3·2^{n−2}/D, and there the post-double-cancel active sum is exactly 1 − 2·(3·2^{n−2}/D) =
(2^{n−1} − 1)/D, the IH(n−1) *boundary* (non-strict) — so the geometric config is the marginal case,
as it must be for tightness. Because the true threshold is larger than previously claimed, the true
double-cancel residual **a_2 + a_3 ≤ 3·2^{n−2}/D is nonempty for every n ≥ 3** (LP: min a_2 + a_3 over
the B2 hard regime is 17/45 < 2/5 at n=3, 11/45 < 8/21 at n=5), and is empty only for n ≤ 2. The old
claim "B2 settled for n ≤ 2 for the right reason" was therefore **right only vacuously** — corrected.

Even where a_2 + a_3 > 3·2^{n−2}/D, the double-cancel additionally needs a_1 − a_2 ≥ a_3 to place the
second cut; and IH(n−1) is proved only for n − 1 ≤ 4 (Theorem UB). So this entry closes only the
B2-small sub-region {a_1 − a_2 ≥ a_3, a_2 + a_3 > 3·2^{n−2}/D}, and only for n ≤ 5. The complementary
residual — near-equal small pieces with a_2 + a_3 ≤ 3·2^{n−2}/D, or a_1 − a_2 < a_3, or n ≥ 6 —
stays **open**.

**Status of B2-small.** The min-A cut search confirms A ≤ 1/D is *achievable* for every B2-small
config tested (e.g. n=3 (2/5, 3/10, 1/5, 1/10): cut a_1 → (1/10, 3/10), cut a_3 → (1/10, 1/10) gives
final lengths {3/10, 3/10, 1/10, 1/10, 1/10, 1/10}, all in even multiplicity, A = 0), consistent with
the established answer c(n). But the achieving strategies are **adaptive** (config-dependent pairings,
genuine fragment cuts, no single closed-form rule) — exactly the fragment-cascade wall shared with the
IH(q ≥ 5) flat residual. No uniform strategy is in hand; **B2-small is honestly open.**

## What is closed vs open (summary)

- **Closed (proved here, certifiable):**
  - Lemma IH-reducible (pure conditional); Lemma IH4-flat; hence Theorem UB — IH(q) for all q ≤ 4,
    i.e. the **Case-B B1-large upper bound for all n ≤ 4**.
  - **Lemma GreedyCascade (new, round 7):** the **Case-B B2-large upper bound (1/2 ≤ a_1 ≤ c(n)) for
    ALL n** — explicit n-cut strategy giving A = 2a_1 − 1 ≤ 1/D. This is uniform in n (no q-induction),
    and it closes both prior residual witnesses.
  - With the imported Case A (Lemma H), Reductions 1–2, and the corrected double-cancel entry, the
    **whole Case-B upper bound is now closed except: (U1) IH(q ≥ 5) flat residual in B1-large (a_1 >
    c(n), n ≥ 5), and (U2) B2-small (a_1 < 1/2) beyond the double-cancel sub-region.**
- **Open (honest gap):** (U1) IH(q ≥ 5) flat residual and (U2) B2-small (a_1 < 1/2) for general n —
  the two faces of the same fragment-cascade wall (adaptive, no closed form). The dual-bound IH+(m)
  does **not** close it (fixed-point obstruction proved above); a global-extremal or bounded
  multi-level-collapse argument is required. (Note U2 and the previously-flagged B2 "near-equal
  small pieces" are the same region, now reduced to the single clean condition a_1 < 1/2.)

## Full proof
Not present — Status is partial. The upper bound in Case B is complete for {n ≤ 4} ∪ {a_1 ≥ 1/2, all
n}; the B1-large IH(q ≥ 5) flat residual and the B2-small (a_1 < 1/2) residual remain open, as does
the imported lower-bound flat-move termination detail.

## Promotable lemmas

- **Lemma GreedyCascade** (statement and proof above, round 7). For sorted positive lengths b_1 ≥ …
  ≥ b_p summing to 1 with b_1 ≥ 1/2, XY with p − 1 cuts leaves final XOR-measure A = 2b_1 − 1; hence
  1/2 ≤ b_1 ≤ c(n) ⟹ A ≤ 1/D. Pure conditional, no empirical content. Derived from certified Lemma X.
  Closes **B2-large for all n** and both prior residual witnesses. **Recommend certification.**
- **Lemma IH-reducible** (statement and proof above). Pure conditional, no empirical content:
  for q pieces > 1/D with gaps > 1/D and S < (2^q − 1)/D, if S − max(b_1, 2b_2) < (2^{q−1} − 1)/D
  then one cut reduces to a strict IH(q−1) instance or finishes via CaseB-Reduction 2. Derived from
  certified Lemmas X and CaseB-Reductions. (Already certified in `lemmas/IH-reducible.md`.)
- **Lemma IH4-flat** (statement and proof above). For q = 4 in the flat residual (S < 15/D,
  S − max(b_1, 2b_2) ≥ 7/D), the 3-cut strategy {halve b_1; cut b_2 at b_3; cut b_4 at δ} gives
  A < 1/D. Derived from certified Lemmas X and H (pair-cancellation). (Already certified in
  `lemmas/IH4-flat.md`.) Together with IH-reducible, IH(1), IH(2), imported IH(3), this proves
  **IH(q) for all q ≤ 4** (Theorem UB).
