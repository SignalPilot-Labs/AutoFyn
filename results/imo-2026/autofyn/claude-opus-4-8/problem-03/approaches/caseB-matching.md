## Status
partial

## Approach: caseB-matching

**Framing (as dispatched).** Reframe the Case-B upper bound as a FINITE combinatorial
optimization over the *matching menu*: XY either pairs two LB pieces (cut the larger at the
smaller, creating an exact cancelling copy plus a residual gap), halves a piece (two equal
copies), or keeps a piece intact; budget = #(pairs) + #(halves) ≤ n. The proposed **Lemma M**
claimed the best menu strategy already forces A := μ{N odd} ≤ 1/D.

**MAIN RESULT OF THIS ROUND (round 4): Lemma M is FALSE.** The matching menu is *insufficient*
for the hard regime. I found and machine-verified (exact rational arithmetic) an explicit
Case-B configuration for n = 3 on which **every** menu strategy gives A > 1/D, yet XY *can*
reach A ≤ 1/D with fragment (cascade) cuts. So this approach, as framed, cannot close Case B;
the correct route requires fragment cuts (the interleaving/cascade mechanism of
direct-constructive's Lemma I). Details and the full refutation are under "Spec concerns".

What I did salvage rigorously (all general-n, all correct): the **XOR/parity evaluator** with an
exact toggle-set formula for a cut; the **halve-all reduction** collapsing Case B to exactly
p = n+1 pieces; and the **close-pair reduction** disposing of every Case-B config with a small
pairwise gap. These pin the open core down to a single sharp sub-case (the "hard regime"), which
is the same wall direct-constructive faces.

---

## Approaches tried
- **direct-constructive** — LIVE (imported infrastructure only: G1, R, H, lower bound). Not
  re-attacked here.
- **induction-recursion** — DEAD-END (prior rounds).
- **caseB-matching (finite matching menu, Lemma M)** — **REFUTED this round (round 4).** The
  restriction to the matching menu (each original LB piece cut at most once, "cut larger at
  smaller" + halve) is provably too weak. Exact counterexample (n = 3):
  a = (5144, 2787, 1386, 683)/10000, sum 1, all pieces > 1/15, all consecutive gaps > 1/15
  (a hard-regime Case-B config). Exhaustive search over the entire menu (all matchings of the 4
  pieces × all halve/keep choices, budget ≤ 3) gives **best menu A = 683/10000 = 0.0683 >
  1/15 ≈ 0.0667** (best menu strategy: keep a₄, halve a₁, a₂, a₃). But the fragment **cascade**
  "cut a₁ at a₂, then cut its residual at a₃" (2 cuts inside a₁) yields the pieces
  {a₁−a₂−a₃, a₄} = {0.0971, 0.0683} with A = 0.0288 ≤ 1/15. So the *theorem* (Case-B upper
  bound with general cuts) holds, but **the menu framing does not reach it** — Lemma M is false.
  Verified with `fractions.Fraction` (no floating error). The distinctive mechanism of this
  approach therefore does not work; the approach is a dead-end **as framed**.

## Current best
The furthest rigorous progress of this approach (all general-n, all correct). These reduce the
Case-B upper bound to one sharp sub-case. Throughout, LB's final pieces are a₁ ≥ … ≥ a_p
(p ≤ n+1, Σ = 1), c(n) = 2ⁿ/D with D = 2^{n+1}−1, and (Lemma R, imported) the XY-goal
O ≤ c(n) is equivalent to **A := μ{t : N(t) odd} ≤ 1/D**, where N(t) = #{pieces of length > t}.

### Lemma X (XOR / parity evaluator) — PROVED
For a finite multiset of positive lengths {ℓ₁,…,ℓ_m}, place each as an interval [0, ℓ_i] on the
t-axis. Then
   **A = μ( [0,ℓ₁] ⊕ [0,ℓ₂] ⊕ … ⊕ [0,ℓ_m] )**,   ⊕ = symmetric difference.
*Proof.* By Lemma R (imported, certified), A = μ{t : N(t) odd}, and N(t) = #{i : ℓ_i > t}. A
point t lies in the symmetric difference ⊕_i [0,ℓ_i] iff it lies in an odd number of the
intervals [0, ℓ_i], i.e. iff #{i : ℓ_i ≥ t} is odd; this differs from #{i : ℓ_i > t} only on the
finite (measure-zero) set of the ℓ_i's. Hence μ(⊕_i [0,ℓ_i]) = μ{t : N(t) odd} = A. ∎

**Toggle-set formula for a cut.** Cutting a piece of length ℓ into two pieces (m, ℓ−m) with
0 < m ≤ ℓ/2 replaces the single interval [0,ℓ] by the two intervals [0,m], [0,ℓ−m]. In the XOR
this multiplies the running set by the toggle set
   T = [0,ℓ] ⊕ [0,m] ⊕ [0,ℓ−m] = **[0,m] ∪ (ℓ−m, ℓ]**   (Lebesgue measure 2m).
*Proof.* [0,ℓ] ⊕ [0,m] = (m, ℓ] since [0,m] ⊂ [0,ℓ]. Then, using m ≤ ℓ−m,
(m,ℓ] ⊕ [0,ℓ−m] has union [0,ℓ] and intersection (m,ℓ]∩[0,ℓ−m] = (m, ℓ−m], so the symmetric
difference is [0,ℓ] ∖ (m, ℓ−m] = [0,m] ∪ (ℓ−m, ℓ]. ∎

**Menu-value formula (correct, but the menu is insufficient — see Spec concerns).** For a
matching-menu strategy (pairs P, halves Z, kept K): a pair {i,j} (a_i ≥ a_j, cut a_i at a_j)
produces a copy a_j that cancels the intact a_j in the XOR, leaving the residual gap
[0, a_i−a_j]; a halve produces two equal copies that cancel (∅); a kept piece contributes
[0, a_k]. Hence by Lemma X
   A = μ( ⊕_{{i,j}∈P} [0, a_i − a_j]  ⊕  ⊕_{k∈K} [0, a_k] )
     = alternating sum of the multiset { a_i − a_j : {i,j}∈P } ∪ { a_k : k∈K }.
This formula is exact; the problem is that its minimum over the (finite) menu can exceed 1/D.

### Reduction 1 (halve-all): Case B ⟹ p = n+1 — PROVED
If a Case-B config has p ≤ n pieces, XY halves all p of them (p ≤ n cuts). Each halved piece
gives two equal copies [0, a_i/2] ⊕ [0, a_i/2] = ∅, so the total XOR is empty and, by Lemma X,
**A = 0 ≤ 1/D**, i.e. O = 1/2 ≤ c(n). Therefore the Case-B upper bound is nontrivial only when
LB uses all n marks, producing exactly **p = n+1 pieces**. (When p = n+1 the budget n = p−1
forbids halving all p at once — exactly one piece must survive an operation, which is the source
of the difficulty.) ∎

### Reduction 2 (close-pair): dispose of every config with a small gap — PROVED
Suppose p = n+1 and some two pieces satisfy a_i − a_j ≤ 1/D (with a_i ≥ a_j). Since the pieces
are sorted, the smallest pairwise difference is a *consecutive* gap, so this is equivalent to
d* := min_{1≤k≤p−1} (a_k − a_{k+1}) ≤ 1/D. XY pairs the consecutive pieces attaining d* (cut the
larger at the smaller, 1 cut) and halves the other p−2 pieces (p−2 cuts): total (p−2)+1 = p−1 =
n cuts. By the menu-value formula the surviving XOR is [0, d*] (all halves cancel, the one pair
leaves gap d*), so **A = d* ≤ 1/D**, i.e. O ≤ c(n). ∎

### Residual open core — the "hard regime"
After Reductions 1–2 (and Case A = Lemma H, a_p ≤ 1/D, imported), the Case-B upper bound is
open **only** in the hard regime:
   **p = n+1, all pieces a_i > 1/D, AND all consecutive gaps a_k − a_{k+1} > 1/D.**
This regime is nonempty for every n ≥ 2 (verified: e.g. the exact n = 3 counterexample above).
In it, the matching menu provably fails (Spec concerns), and the correct strategy uses fragment
cascade cuts — precisely direct-constructive's interleaving Lemma I mechanism. Numerically, with
general cuts XY drives A all the way to ≈ 0 on hard-regime configs (n = 3, 60 configs: worst
achievable A = 0.0000, full slack), so the *theorem* is safe; only this approach's menu framing
is not. This is the SAME wall as direct-constructive's U1, reached from the other side.

## Spec concerns
**The core mechanism of this approach (finite matching menu, "Lemma M") is refuted.** The outline
and both kill-switches asserted that the finite matching menu attains A ≤ 1/D over all Case-B
configs with 0 failures. That is *false*: those searches sampled mostly non-hard-regime configs
(smallest piece or some gap ≤ 1/D), where the menu trivially wins via Reduction 2. Restricted to
the **hard regime** (all gaps > 1/D), the menu fails on a positive-measure set of configs:

- Exact witness (n = 3): a = (5144, 2787, 1386, 683)/10000. Exhaustive menu search (rational
  arithmetic) → best A = 683/10000 > 1/15; fragment cascade → A = 288/10000 < 1/15.
- Hard-regime sampling of the exhaustive menu: n = 3 gives ~7/3000 failures, n = 4 gives
  ~3/3000, worst excess +0.003 — small but nonzero, so not a numerical artifact.
- The "kill-switch PASSED with full slack, worst excess −1/D" reported by the outliner and
  independently by the reviewer measures the **general-cut** (fragment-allowed) optimum, NOT the
  menu optimum; the two were conflated. The general-cut optimum indeed has full slack (A → 0),
  which is why the underlying theorem and the answer c(n) = 2ⁿ/D are correct.

**Consequence for the field.** The distinctive selling point of caseB-matching — an
induction-free FINITE matching-exchange — does not exist: the finite menu is the wrong strategy
class. The genuinely-required strategy is fragment cascade cutting, which is direct-constructive's
route. So this approach does not, in fact, diversify the field away from the shared Case-B wall;
it collapses onto it. Recommend the outliner either (a) re-plan a genuinely fragment-based finite
optimization (cascade menu, still finite but strictly larger than the matching menu), or (b)
retire caseB-matching and concentrate on direct-constructive's Lemma I / IH(n) for the hard
regime. The salvaged Reductions 1–2 and Lemma X are worth promoting regardless — they cut the
Case-B upper bound down to the single hard-regime sub-case for all n.

## Promotable lemmas
- **Lemma X (XOR/parity evaluator)** — For pieces of lengths {ℓ_i}, A = μ(⊕_i [0,ℓ_i]); and a
  cut of ℓ into (m, ℓ−m), m ≤ ℓ/2, toggles the A-set by [0,m] ∪ (ℓ−m, ℓ]. Proved above from
  Lemma R (certified). Reusable exact scoring tool for any cutting strategy.
- **Reduction 1 (halve-all)** — Any Case-B config with p ≤ n pieces has A = 0 achievable, so the
  Case-B upper bound reduces to exactly p = n+1 pieces. Proved above. General n.
- **Reduction 2 (close-pair)** — If p = n+1 and the minimum consecutive gap d* ≤ 1/D, then XY
  achieves A = d* ≤ 1/D (pair the closest two, halve the rest). Proved above. General n. Together
  with Case A (Lemma H), this leaves the Case-B upper bound open only in the hard regime
  (p = n+1, all pieces AND all consecutive gaps > 1/D).
