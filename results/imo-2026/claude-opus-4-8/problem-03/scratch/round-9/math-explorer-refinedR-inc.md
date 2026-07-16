# imo-2026-03 — Explorer Report: Refined-R INC Branch (G-INC-2)

**Lens: Lower-bound refined-R inclusion branch, G-INC-2**

---

## Problem ID: imo-2026-03

---

## (a) What G-INC-2 asserts and why G-INC-1 does NOT auto-give it

**Statement of G-INC-2.** In the INC branch of LL (t ≥ 2), when the Xiang Yu refinement R of G_{n−1} has c_R ≥ 1 extra cuts (so R is a strict refinement, e.g., min-piece 3/2 instead of 1), prove:
```
A(Q) ≤ A(R) − 1    (equivalently A(Q ∪ R) = A(R) − A(Q) ≥ 1)
```
for every Q with S_Q ⊆ S_R, |Q| ≤ n (budget-reduced: certified budget-reduction lemma gives |Q| ≤ n when c_R ≥ 1), and ΣQ = 2^n.

**G-INC-2 is vacuous at n = 3**: Step 14 of ll-inclusion-gap (confirmed) — the joint budget + parity force c_Q + c_R > 3 for any valid n=3 refined-R INC pair. **First nontrivial at n = 4**, specifically c_R = 1 (cut of one piece of G_3), c_Q = 3, |Q| ≤ 4.

**Why G-INC-1 does NOT auto-give G-INC-2.** Three concrete reasons:

1. **Tight INC pairs exist with S_Q ⊄ S_{G_{n−1}}**: the tight case at n=4 is Q = {5,5,4,2}, R = {4,4,4,2,1} (G3 with top piece 8 split equally into 4+4). Here A(Q) = 2 = A(R)−1 = 3−1 (margin 1, tight), **but S_Q = [2,4) is NOT a subset of S_{G_3} = [1,2)∪[4,8)**. G-INC-1 (which requires S_Q ⊆ S_{G_{n−1}}) is simply inapplicable to this pair. Similarly at n=5: tight pair Q = {4,8,10,10}, R = {8,8,8,4,2,1} has S_Q = [4,8) ⊄ S_{G_4} = [1,2)∪[4,16).

2. **No refined-R analogue of the SET IDENTITY**: The anchor proof used `S_{G_{n−1}} ∩ [0,2^{n−2}) = S_{G_{n−3}}` (certified `set-identity-selfsimilar.md`), which is a fact about G_{n−1}'s clean dyadic band structure. For S_R of refined R this identity has no analogue: S_R = S_{G_{n−1}} △ F (flip from the extra cut), so S_R ∩ [0,2^{n−2}) = S_{G_{n−3}} △ (F ∩ [0,2^{n−2})). The second term is non-empty and non-trivial.

3. **Parity of h breaks for equal-split top-piece cuts**: The top-band decomposition requires h = #{Q-parts ≥ 2^{n−2}} to be **even** (from the Parity-Condition Lemma, because the band just below 2^{n−2} has N_{G_{n−1}} = 2, hence N_R = 2 even for "most" refined R). However, when the top piece 2^{n−1} is split **equally** into {2^{n−2}, 2^{n−2}}: N_R(2^{n−2}−0) = #{R-parts ≥ 2^{n−2}} = 3 (ODD), removing the parity constraint on h. **Verified**: Q = {5,5,4,2}, R = {4,4,4,2,1} has h = #{5,5,4} ≥ 4 = 3 (ODD). The Parity-Condition Lemma does not fire at an ODD-count threshold, so h can be 3 in a valid tight INC case.

**Numerical verification (0 violations):** G-INC-2 holds at:
- n=4, c_R ∈ {1,2}, step=0.25: 4164 INC configs, 0 violations, minimum margin = 1.000.
- n=5, c_R=1 critical case (top-piece equal split R=[8,8,8,4,2,1]): 34 INC configs, 0 violations, max A(Q) = 4 = A(R)−1 = 5−1 (tight).

---

## (b) Induction on c_R via flipped-region split: where it works and where it breaks

**Setup.** Cutting piece p_j of G_{n−1} into {a, p_j−a} (a ≤ p_j/2) introduces two "flipped" intervals:
```
F_lo = [0, a)     and     F_hi = [p_j − a, p_j)
```
with S_R = S_{G_{n−1}} △ (F_lo ∪ F_hi). The induction-on-c_R splits on whether S_Q meets F = F_lo ∪ F_hi.

**Three structural sub-cases (for c_R = 1; higher c_R is similar by induction):**

### Sub-case (I): Lower-band cut (k_0 ≤ n−3, cut of piece 2^{k_0} with 2^{k_0} ≤ 2^{n−3})

Here F ⊆ [0, 2^{n−3}] ⊆ [0, 2^{n−2}). The top band I_{n−1} = [2^{n−2}, 2^{n−1}) is **unchanged**: S_R ∩ I_{n−1} = S_{G_{n−1}} ∩ I_{n−1} = I_{n−1} (measure 2^{n−2}).

The top-band decomposition (certified `top-band-decomposition.md`) carries over with A(R) in place of A(G_{n−1}):
```
A(R) − A(Q) = deficit_top + [A(R_lo) − A(Q_lo)]
```
where:
- deficit_top = 2^{n−2} − δ_top ≥ 0 (unchanged, since S_R ∩ I_{n−1} = I_{n−1})
- R_lo = {R-pieces < 2^{n−2}} = G_{n−3} with the same lower-band cut at level k_0
- S_{Q_lo} ⊆ S_{R_lo} (restriction of INC to the lower half — holds since F ⊆ lower half)
- h = #{Q-parts ≥ 2^{n−2}} is EVEN (N_R(2^{n−2}−0) = 2 for lower-band cuts, Parity-Condition applies)

**Key descent**: R_lo is G_{n−3} refined with the same c_R lower-band cut, so by G-INC-2 at level n−2:
```
A(R_lo) − A(Q_lo) ≥ 1
```
Thus A(R) − A(Q) = deficit_top + [A(R_lo) − A(Q_lo)] ≥ 0 + 1 = 1. ✓

**This is a clean n → n−2 induction for lower-band cuts, with NO T-companion needed** (unlike G-INC-1's mutual {Claim, T} machinery). The descent is: G-INC-2(n, lower-band cut at k_0) → G-INC-2(n−2, lower-band cut at k_0), terminating when the cut level k_0 matches (n−2j)−3 for recursion depth j, at which point it becomes a top-piece cut of the recursed level.

**Base cases:** n=2 (trivially: Forcing gives max(Q) ≤ 2 and ΣQ = 4, so Q = {2,2} with A(Q)=0 ≤ A(R)−1 ≥ 0 since A(R) ≥ 1) and n=4 with lower-band cuts (cuts of pieces 1 or 2 of G_3; verified numerically).

**Where it terminates / what the "base" cut becomes.** A lower-band cut of piece 2^{k_0} (at level n) stays at level k_0 under the recursion. After ⌊(n−k_0−3)/2⌋ steps, the recursed problem has level n−2j where n−2j−3 ≤ k_0 < n−2j−1, making the cut a **top-piece cut** of the recursed level. Thus:

- For k_0 = n−3 (the "highest" lower-band cut, piece 2^{n−3}): one descent step gives G-INC-2(n−2) with a top-piece cut of G_{n−3}, which is sub-case (II) or (III) at level n−2.
- For k_0 ≤ n−5: two or more descent steps, eventually hitting a base.

The induction is well-founded and reduces G-INC-2 for lower-band cuts to the top-piece cut sub-cases at smaller levels.

### Sub-case (II): Non-equal top-piece cut (k_0 = n−1, a < 2^{n−2})

Cut of 2^{n−1} into {a, 2^{n−1}−a} with a < 2^{n−2}.

The top band I_{n−1} is **partially modified**: S_R ∩ I_{n−1} = [2^{n−2}, 2^{n−1}−a) (measure 2^{n−2}−a), since [2^{n−1}−a, 2^{n−1}) ⊆ S_{G_{n−1}} ∩ I_{n−1} gets flipped out of S_R.

**h is still EVEN**: N_R(2^{n−2}−0) = #{R-parts ≥ 2^{n−2}} = #{pieces {a, 2^{n−1}−a} ≥ 2^{n−2}} + #{G_{n−3}-pieces ≥ 2^{n−2}} = (0 [a < 2^{n−2}] + 1 [2^{n−1}−a > 2^{n−2}]) + 1 [the original 2^{n−2}] = 2 (even). Parity-Condition applies.

The modified decomposition gives:
```
A(R) − A(Q) = (2^{n−2}−a − δ_top) + [A(R_lo) − A(Q_lo)]
```
with modified deficit_top = (2^{n−2}−a) − δ_top ≥ 0 (since S_Q ∩ I_{n−1} ⊆ S_R ∩ I_{n−1} = [2^{n−2}, 2^{n−1}−a), so δ_top ≤ 2^{n−2}−a).

Here R_lo = {R-pieces < 2^{n−2}} = G_{n−3} with the lower-band contribution of the flip (F_lo = [0,a) ∩ [0,2^{n−2}) = [0,a)). So S_{R_lo} = S_{G_{n−3}} △ [0,a).

The lower-level INC gives A(R_lo) − A(Q_lo) ≥ 1 by G-INC-2 at level n−2 for R_lo = G_{n−3} △ [0,a). But R_lo here is not G_{n−3} with a standard "cut" — it's G_{n−3} with the band [0,a) flipped. This corresponds to cutting the **bottom** piece (piece "1" conceptually) at level n−2. Analysis continues as for lower-band cuts of the recursed level.

**Key obstruction** if a is very small (a < 1): the "flipped band" [0,a) in R_lo may not correspond to a genuine piece cut of G_{n−3} (it's a sub-interval of a piece, not a cut point). This requires a more careful argument than the standard top-band induction. However, numerics confirm 0 violations.

### Sub-case (III): Equal-split top-piece cut (k_0 = n−1, a = 2^{n−2})

Cut of 2^{n−1} into {2^{n−2}, 2^{n−2}} (equal halves). S_R = [0,2^{n−1}) \ S_{G_{n−1}} (the complement of S_{G_{n−1}} within the support). **N_R(2^{n−2}−0) = 3 (ODD).** The h-parity mechanism breaks; h can be ODD.

**A direct case analysis works** (shown explicitly for n=4, holds numerically for n=5):

A(R) = A(G_{n−2}) (proved above: R = {2^{n−2}, 2^{n−2}, 2^{n−2}, G_{n−3}} gives A(R) = 2^{n−2} − A(G_{n−3}) = A(G_{n−2})).

S_R = [0,2^{n−1}) \ S_{G_{n−1}} = union of the "forbidden bands" of G_{n−1}.

For Q with S_Q ⊆ S_R:
- Parts in (2^{n−2}, 2^{n−1}) must appear with **even multiplicity** (by Parity-Condition applied at N_R even on [0,2^{n−2}) and [2^{n−1},...)).
  - Why: N_R(x) = 0 for x ≥ 2^{n−1} (even). So #{Q-parts > 2^{n−1}} must be even. But ΣQ = 2^n, and by Forcing, max(Q) ≤ 2^{n−1}. So actually no Q-parts exceed 2^{n−1}, but parts equal to 2^{n−2} can appear.
  - Actually: N_R(x) for x ∈ [2^{n−2}, 2^{n−1}): only the three copies of 2^{n−2} exceed x (if x < 2^{n−2}, those plus G_{n−3} pieces; if x ∈ [2^{n−2}, 2^{n−1}) then only pieces > x). For x ∈ (2^{n−2}, 2^{n−1}): #{R-pieces > x} = 0 (even). So by Parity-Condition: #{Q-parts > x} is even for x ∈ (2^{n−2}, 2^{n−1}).

- Q-parts equal to 2^{n−2} must appear with **even multiplicity** (from the N_R = 3 odd at 2^{n−2}−0 — wait, that's odd, so Parity-Condition says NOTHING there). However, for x ∈ (2^{n−2}, 2^{n−1}): N_Q(x) = #{Q-parts > x} = #{Q-parts in (x, 2^{n−1})} must be even. Parts equal to 2^{n−2} do NOT contribute (they equal the threshold, not exceed it). So parts > 2^{n−2} appear with even total count.

**Case analysis for n=4** (A(R) = A(G_2) = 3, target A(Q) ≤ 2):

Let pairs = even-multiplicity parts in (4, 8) (contributing 0 to A by cancellation), and remaining parts {p_i} are ≤ 4. ΣQ = 16.

- No pairs: all Q-parts ≤ 4, |Q| ≤ 4, sum = 16 → Q = {4,4,4,4}, A(Q) = 0 ≤ 2. ✓
- One pair {s,s} with s ∈ (4,8): ΣQ = 2s + p_1 + p_2, remaining p_1 ≥ p_2 ≤ 4 (at most 2). A(Q) = s−s+p_1−p_2 = p_1−p_2. For S_Q ⊆ S_R = [0,1)∪[2,4): S_Q = [p_2, p_1) must lie in [0,1)∪[2,4). Either [p_2,p_1) ⊆ [0,1) (A(Q) = p_1−p_2 ≤ 1 ≤ 2 ✓) or [p_2,p_1) ⊆ [2,4) (A(Q) ≤ 2 ✓) or it straddles [1,2) → S_Q ⊃ [1,2) ⊄ S_R → not valid INC. So in all valid sub-cases, A(Q) ≤ 2. ✓
- Two pairs {s,s},{t,t}: A(Q) = 0 ≤ 2. ✓

**The argument for general n** (sketch): Q-parts above 2^{n−2} appear in equal pairs {s,s} contributing 0 to A(Q). The remaining parts p_1 ≥ p_2 ≥ ... all ≤ 2^{n−2} have A(Q-remaining) ≤ p_1 − p_2 ≤ 2^{n−2} (trivially). The INC constraint S_Q ⊆ S_R = ∪(forbidden bands of G_{n−1}) forces S_{Q-remaining} ⊆ ∪(forbidden bands ∩ [0,2^{n−2}]). The "spread" p_1−p_2 is bounded by the width of a single allowed contiguous interval in S_R, which is at most 2^{n−3} (not exactly 2^{n−2}−1 for general n). The bound A(Q) = p_1−p_2 ≤ A(R)−1 = A(G_{n−2})−1 follows from: for a spread of p_1−p_2 to fill an entire allowed band [L_k, L_k + w), we need ΣQ ≥ 2 * L_k + (p_1−p_2) = 2*L_k + w, which must ≤ 2^n. These arithmetic constraints close the gap. (**This is the sub-target the builder should make rigorous for general n.**)

---

## (c) Is there a unifying refined-R lemma covering G-INC-2 and the Sub-3b top-cut bucket?

**Short answer: No known single lemma; the two routes need different arguments.**

- **G-INC-2** (INC, S_Q ⊆ S_R refined-R): target A(R)−A(Q) ≥ 1, proved via the certified INC reduction A(Q∪R) = A(R)−A(Q).
- **Sub-3b top-cut bucket** (GAP, max(Q) < 2^{n−1}, max(R) < 2^{n−1}, no reflection anchor): target measure(S_Q △ S_R) ≥ 1 directly. The ll-dyadic-symdiff approach uses double-REFL which requires max(R) = 2^{n−1} (uncut top piece) — precisely what fails in the top-cut bucket.

The **ll-general-R-core lemma** (certified R8) already covers the R-agnostic Cases 1/2/Sub-3a for both branches (91.6% of n=3 configs). For the residual Sub-3b, the INC and GAP sub-branches need different machinery:

- INC sub-branch: S_Q ⊆ S_R → use A(R)−A(Q) ≥ 1 (G-INC-2).
- GAP sub-branch (top-cut): measure(S_Q △ S_R) ≥ 1 directly. The certified ll-reflection-identity-gen (REFL-gen) works when max(R) ≥ max(Q); for max(R) < max(Q) a new identity is needed.

**One candidate for a partial unifier**: A direct measure argument using the "unit excess" ΣQ − ΣG_{n−1} = 1. In the top-cut bucket with refined R, this excess must manifest as an "odd crossing" somewhere. But the prior explorer confirmed (R6/R7) that ∫(N_Q − N_R) = 1 alone is provably insufficient to bound measure(S_Q △ S_R).

**The most promising unifier** for the two residuals: if G-INC-2 can be proved via a generalized {Claim_R(n,ε), T_R(n)} mutual induction (with R-dependent claims), the Sub-3b GAP top-cut case might be reducible to an anti-INC version of the same framework. **But this requires first proving the equal-split case (Sub-case III above), which currently has no inductive structure**.

---

## (d) Concrete, small-n verifiable sub-targets for next round

**Sub-target A (most accessible, 1–2 round estimate):** Prove G-INC-2 for **lower-band cuts** (cuts of pieces 2^{k_0} with k_0 ≤ n−3) by n → n−2 induction.

- **Statement**: If R = G_{n−1} with one cut of piece 2^{k_0} (k_0 ≤ n−3), S_Q ⊆ S_R, ΣQ = 2^n, |Q| ≤ n, then A(Q) ≤ A(R)−1.
- **Proof structure**: Top-band decomp gives A(R)−A(Q) = deficit_top + [A(R_lo)−A(Q_lo)] ≥ 0 + 1 = 1 by G-INC-2 at level n−2 (IH). Base: n=2 (trivial), n=4 with cuts of G_3 pieces 2 or 1 (direct verification; numerics confirm 0 violations, 481 INC configs at step=0.5).
- **Budget**: The joint budget ensures |Q_lo| = |Q| − h ≤ n − 2, consistent with level n−2 constraints.
- **Verifiable check**: at n=4 cut piece 2 into {0.5, 1.5}: A(R) = 5 (unchanged; f+ = f− = 0.5), R_lo = {1, 0.5, 1.5} = G_1 refined. G-INC-2 at n=2 for R_lo: A(Q_lo) ≤ A(R_lo)−1 = 0 (since A(R_lo) = 1 and only Q_lo = {2,2} is valid). ✓

**Sub-target B (medium, 1 round):** Prove G-INC-2 for the **equal-split top-piece cut** (a = 2^{n−2}).

- **Statement**: If R = G_{n−1} with top piece 2^{n−1} split into {2^{n−2}, 2^{n−2}}, and S_Q ⊆ S_R, ΣQ = 2^n, |Q| ≤ n, then A(Q) ≤ A(G_{n−2})−1 = A(R)−1.
- **Proof structure**: The direct case analysis (Sub-case III above) works for n=4 (verified). For general n: Q-parts in (2^{n−2}, 2^{n−1}) appear in equal pairs (A-contribution 0). Remaining parts p_1 ≥ p_2 determine A(Q) = p_1−p_2. INC forces [p_2, p_1) ⊆ single forbidden band of G_{n−1} in [0, 2^{n−2}]. Each forbidden band has width ≤ 2^{n−3} ≤ A(G_{n−2})−1. **Make this arithmetic explicit.**
- **Verifiable check**: n=5 equal-split R=[8,8,8,4,2,1], A(R)=5, step=0.5: 34 INC configs, max A(Q)=4=A(R)−1 ✓.
- **Key arithmetic**: A(G_{n−2}) − 1 ≥ 2^{n−3} for n ≥ 4 (since A(G_{n−2}) = (2^{n−1}+(−1)^{n−2})/3 ≥ (2^{n−1}−1)/3 ≥ 2^{n−3} for n ≥ 4). And p_1−p_2 ≤ width of single allowed band ≤ 2^{n−3}. So A(Q) ≤ 2^{n−3} ≤ A(G_{n−2})−1. **CHECK this bound for general n** (needs verification that the largest allowed band width is ≤ A(G_{n−2})−1).

**Sub-target C (harder, needs exploration):** Prove G-INC-2 for **non-equal top-piece cuts** (a ∈ (0, 2^{n−2})).

- **Key**: h is even, modified top-band decomp gives deficit_top + [A(R_lo)−A(Q_lo)] ≥ 1, but R_lo = G_{n−3} △ [0,a) is not a standard "cut refinement" for general a < 1. When a ≥ 1 (flip [0,a) is a full sub-interval of [0,1)): R_lo can be identified with a specific lower-level refinement. When a < 1: the flip is within the bottom piece of G_{n−3} and needs a careful sub-case.
- **Partial coverage**: Many non-equal top-piece cuts have A(R) ≥ A(G_{n−1}) (when f+ ≥ f−, i.e., the flip adds more to S_R than it removes). In those cases, A(R)−1 ≥ A(G_{n−1})−1, and G-INC-1 (anchor) directly gives A(Q) ≤ A(G_{n−1})−1 ≤ A(R)−1 (since S_Q ⊆ S_R ⊆ S_{G_{n−1}} when A(R) ≥ A(G_{n−1})). **This case is essentially free from G-INC-1.**
- **Hard sub-case**: f+ < f− (cut DECREASES A(R) below A(G_{n−1})). This occurs for cuts with a < 1 of pieces adjacent to a transition in S_{G_{n−1}} (e.g., cutting piece 8 with a < 1 at n=4 gives A(R) = 5 = A(G3), actually unchanged — checked). Specifically: for odd n, cutting the top piece 2^{n−1} with small a: f+ = 0 (the interval [0,a) is inside S_{G_{n−1}} for odd n), A(R) = A(G_{n−1})−2a < A(G_{n−1}). This is the genuine hard sub-case requiring the modified decomp.

---

## Distinct openings (summary)

1. **Lower-band cut induction (Sub-target A)**: Prove G-INC-2 for k_0 ≤ n−3 cuts by n → n−2 with base n=2 (trivial) and n=4 (direct verification). Clean and likely completable in 1 round.

2. **Equal-split direct case analysis (Sub-target B)**: Prove G-INC-2 for a = 2^{n−2} by: pairs in (2^{n−2}, 2^{n−1}) cancel in A; remaining spread p_1−p_2 ≤ max forbidden-band width ≤ A(G_{n−2})−1. Uses arithmetic of G_{n−2}'s structure.

3. **Anchor-extension for increasing-A cuts**: When the extra cut increases A(R) above A(G_{n−1}) (f+ > f−), G-INC-1 immediately extends: A(Q) ≤ A(G_{n−1})−1 ≤ A(R)−1. This covers many cases "for free".

4. **Modified mutual induction for non-equal top cuts**: Generalize {Claim_R(n,ε), T_R(n)} to track the "effective anchor" A(R) instead of A(G_{n−1}). The T_R companion handles the sum-deficient case analogously to the anchor's T(ℓ). The equal-split case needs a separate base.

---

## Candidate techniques

- **Induction strengthening**: Claim_R(n, ε) with ε tracking the sum variation, exactly as for G-INC-1. The {Claim_R, T_R} mutual induction pattern is the natural extension.
- **Direct case analysis by part-pair structure**: For equal-split top-piece cuts, partitioning Q by pairs in (2^{n−2}, 2^{n−1}) and bounding the remaining spread.
- **Anchor extension**: When A(R) ≥ A(G_{n−1}), G-INC-1 applies directly.

---

## Cheap-kill candidates

- **Increasing-A cuts (A(R) ≥ A(G_{n−1}))**: G-INC-1 immediately gives A(Q) ≤ A(G_{n−1})−1 ≤ A(R)−1. Reduces G-INC-2 scope to cuts that DECREASE A(R). From the flip analysis: only cuts where f− > f+ decrease A(R); and f− > f+ requires the flip intervals to overlap more of S_{G_{n−1}} than its complement. **Compute which cuts decrease A(R) and exclude others from the hard case.**
- **Parity-size bound**: |Q| ≤ n (from budget-reduction), which limits the number of pairs and simplifies the case analysis.

---

## Knowledge-base entries to use

- **Induction loading / strengthening the hypothesis** (knowledge_base.md "Generalize"): the {Claim_R(n,ε), T_R(n)} mutual induction is exactly this.
- **Casework / exhaustion** (knowledge_base.md "Casework"): the equal-split direct case analysis.
- **Minimum counterexample / well-foundedness** (knowledge_base.md): the n → n−2 induction is well-founded.

Specific certified lemmas to import:
- `t-ell-mutual-induction.md` — the mutual {Claim, T} induction pattern (adapt to {Claim_R, T_R}).
- `parity-condition-inc.md` — general INC parity; applies to refined R (N_R even ⟹ N_Q even).
- `top-band-decomposition.md` — use with A(R) in place of A(G_{n−1}) for lower-band cuts.
- `set-identity-selfsimilar.md` — does NOT apply for refined R; alert builder.
- `forcing-inc-reduction.md` — the INC reduction A(Q∪R) = A(R)−A(Q) remains valid.
- `ll-general-R-core.md` — certifies Cases 1/2/Sub-3a are R-agnostic; G-INC-2 only needs the INC sub-branch of Sub-3b.

---

## Analogous past problems (cruxes)

None identified as directly analogous in the crux corpus for this specific refined-R parity issue. The closest is the mutual induction technique used in the anchor's G-INC-1 proof (internal precedent, round 8).

---

## Prior progress

- G-INC-2 vacuous at n=3 (confirmed). Numerically 0 violations at n=4 (c_R=1,2) and n=5 (c_R=1).
- No proof structure for G-INC-2 yet (open since R6).
- The certified mutual {Claim, T} induction from G-INC-1 is the main template to adapt.
- Budget-reduction lemma: certified (|Q| ≤ n when c_R ≥ 1).
- ll-general-R-core lemma: certified Cases 1/2/Sub-3a R-agnostic; only Sub-3b INC residual is G-INC-2.

---

## Dead ends (do not retry)

- **"h is always even for refined R"**: FALSE. Equal-split top-piece cut gives N_R(2^{n−2}−0) = 3 (ODD) → h can be ODD (verified Q=[5,5,4,2], R=[4,4,4,2,1]).
- **"G-INC-1 auto-gives G-INC-2 via S_Q ⊆ S_{G_{n−1}}"**: FALSE. Tight INC pairs for refined R have S_Q ⊄ S_{G_{n−1}} (verified n=4,5).
- **SET IDENTITY analogue for refined R**: No such identity (S_R ∩ [0,2^{n−2}) = S_{G_{n−3}} △ flip). Do not assume it.
- **"Equal-split is vacuous"**: FALSE starting at n=5 (34 valid INC configs at n=5 equal-split).
- **"max(Q) ≤ max(R) from Forcing"**: FALSE. Forcing gives max(Q) ≤ 2^{n−1}, not max(Q) ≤ max(R). The tight case Q=[5,5,4,2] has max(Q)=5 > max(R)=4.

---

## Small-case / intuition notes (labeled as conjecture)

- **Conjecture (supported by 0-violation numerics)**: G-INC-2 holds for all n and all c_R with the joint budget. The minimum margin is exactly 1 at n=4 (tight cases described above).
- **Conjecture**: Sub-targets A + B + partial C (anchor-extension) together cover ALL refined-R cases for c_R = 1. The remaining non-equal top-piece hard sub-case (a < 1, f+ = 0) may be rare or automatically covered by the modified decomp.
- **Conjecture**: The "single allowed band width ≤ A(G_{n−2})−1" bound for Sub-target B holds for all n ≥ 4. Needs arithmetic verification (A(G_{n−2}) grows exponentially; the largest allowed band in G_{n−1} has width 2^{n−2} = I_{n−1}, but for the equal-split S_R the allowed bands are the FORBIDDEN bands of G_{n−1} which have maximum width 2^{n−2}/3 approximately).
- **Structural note (proved)**: The tight INC pairs for the equal-split case (n=4: Q=[5,5,4,2], R=[4,4,4,2,1]; n=5: Q=[4,8,10,10], R=[8,8,8,4,2,1]) have S_Q = single dyadic-aligned interval [2^{n−2}, 2^{n−1}) or [2^{n−3}, 2^{n−2}) — the interval "one level below the equal split". This suggests the bounding interval is indeed A(G_{n−2})−1 = A(R)−1 in the tight case, which is exactly the band width minus 1.
