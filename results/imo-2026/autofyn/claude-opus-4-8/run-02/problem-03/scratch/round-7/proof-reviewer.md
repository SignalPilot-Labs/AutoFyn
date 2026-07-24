# Proof review — imo-2026-03 (IMO 2026 P3), Round 7

Three slugs built, all self-reported `partial`. I independently re-derived every new claim and verified
numerically (`/tmp/verify7.py`). **No overclaim** — all three are honestly partial. All three
**CHANGES REQUESTED**. Six new lemmas certified; `isolated-cycle-exclusion` superseded.

---

## 1. self-similar-recursion — CHANGES REQUESTED (Status: partial)

**Scores:** Correctness 10/10 (no false step). Completeness 6/10 (two explicit residuals A′, B).
Progress: real — extended cycle exclusion and pinned Gap B's nature.

**Load-bearing new claim re-derived from scratch: Lemma CC+ (degree-2-cycle exclusion).**
The claim rests on the observation that a cycle-piece of degree exactly 2 has its whole budget on its
two cycle components, giving the CLOSED system `u_{i-1}+u_i=2^{a_i}` — independent of any off-cycle
component attachment. I re-derived both branches:
- Even `r`: left null-vector of the cyclic bidiagonal is alternating `(-1)^i`; consistency needs
  `Σ(-1)^i2^{a_i}=0`, impossible for distinct powers (largest unmatched, superincreasing). Verified
  **0 zero-altsum over 1,970,730 even distinct-power arrangements** (r=2,4,6,8).
- Odd `r`: unique solution `u_j=½Σ(-1)^t b_{j+1+t}`; start chosen so `b_M` gets `-1` ⇒ `2u_j<0`.
  Verified **0 all-positive over 246 odd systems** (plus round-6's 197,064 for CC).
CC+ genuinely supersedes CC (needs only piece degrees). Certified as `degree-2-cycle-exclusion.md`;
`isolated-cycle-exclusion.md` marked superseded.

**Gap B pinning verified.** The explicit `W_2` shared-`μ=3` even-leaf `{4/3,4/3,4/3,4/3,1,2/3}`:
I confirmed Σ=7 and **f=1/3<1**, using 3 cuts (>n=2). This correctly proves Gap-B exclusion is
inherently budget/minimality-based (Lemma BD), not local/algebraic. Sound and honest.

**The gap that remains (name it):** §6b Gap A′ — cycles with a cycle-piece of degree ≥3 (chord /
non-uniform mult-≥2 edge / off-cycle-mass) — genuinely open; the circulation minimality direction is a
documented V-kink (verified 200/200), so no descent/flat-Φ-rise lever exists yet. §6′ Gap B — Lemma BD
(degenerate f-flat competitor) unconstructed. The conditional integrality closure §5 is valid GIVEN
A′+B. No circularity, no skipped case within the conditional. Verdict: advance.

## 2. dual-integer-certificate — CHANGES REQUESTED (Status: partial)

**Scores:** Correctness 10/10. Completeness 6/10 (two open: (D′), Budget Lemma). Progress: real —
Positivity collapsed to one clean statement, odd-cancellation branch eliminated.

**Load-bearing new claim re-derived: Lemma POS-CHAR (`f=0 ⟺ all-even`).** I re-proved it: for even T,
`f=Σ(a_{2i-1}-a_{2i})≥0`, equality iff every consecutive pair equal iff every value-block has even
length iff all-even (a block of odd length straddles a pair boundary → strict positivity). For odd T,
`f≥a_T>0`. Verified **0 mismatches over 200,000 random rational multisets**, and `T` odd ⟹ `f>0` with
0 violations. This is the strongest single move this round: it eliminates the feared odd-cancellation
Positivity branch and reduces Positivity to the Budget Lemma. Certified `pos-char.md`.

**Lemma CRAMER** — standard Cramer + integer cofactors, correct; certified `cramer-square-integrality.md`.
Correctly notes (via `gap-d-not-universal`) the divisibility fails off-minimizer, so minimality is
required. **top-piece-cut** re-derived and correct (verified housing argument); certified
`top-piece-cut-alleven.md`, with the companion refutation of "every piece cut" (`{2,2,1,1,½,½}` example).

**The gap that remains (name it):** (D′) `f(P*)∈ℤ` at minimizers (= `det U∣M` square / gcd-1 minors
rect) — load-bearing, open, must use minimality. The Budget Lemma (no all-even in `≤n` cuts) — open;
the J-invariant count gives only `N≥(n+1)/3`, too weak. Both honestly flagged. Verdict: advance.

## 3. concentration-exclusion-rigidity — CHANGES REQUESTED (Status: partial)

**Scores:** Correctness 10/10. Completeness 5/10 (two open gaps, rectangular case not fully carried).
Progress: real for a newcomer — closed the odd/fatal concentration case with its own argument and a
clean negative finding.

The round-6 flaw the outline-reviewer flagged (cross-piece exchange, infeasible in `∏Δ_k`) is FIXED:
step 2 is recast as the certified tie-breaking Move M3 (stays in `G`). I re-derived all three:
- **Lemma 1** (`m·e_k ⇒ m∣det U`): trivial cofactor expansion, correct.
- **Concentration Exclusion Theorem**: M2 ⇒ `m≤3`; M3 kills odd `m=3` (so the fatal
  `{2,4/3,4/3,4/3,1}` dies HERE via M3, not reduced to Gap B — this addresses the reviewer's defect #2);
  hence `m=2`, invisible. Sound (rests on certified M2/M3).
- **Reduction Lemma** (`det U=±2 det U'`, `w_i` unchanged): correct cofactor cancellation of the factor
  2 in numerator and denominator; I checked the `det(U_i)` expansion agrees.
- **Negative finding verified:** the `n=3` minimizer `{3,3,2,2,2,2,1}` has `Uw=b`, `f=1`, and maximal-
  minor **gcd = 2** (I recomputed the four 3×3 minors `{0,-2,-4,0}`, gcd 2). So "benign-U = det/gcd ±1"
  is literally false — an honest, valuable correction. Certified `concentration-exclusion.md`.

**The gap that remains (name it):** Gap 1 — `|det U^★|=1` (square) / coprime maximal minors (rect) on
the concentration-free VISIBLE subsystem (the outline-reviewer's defect #3, the `±1`-pivot, is NOT
re-asserted — honestly left as Gap 1). Gap 2 — Positivity (the visible numerator ≠0). Rectangular
bookkeeping stated, not carried out. Verdict: advance (worth continuing; head-on framing of the shared
wall with a genuinely distinct object).

---

## Certified lemmas (6 new; 1 superseded)
- `degree-2-cycle-exclusion.md` (CC+) — **supersedes** `isolated-cycle-exclusion.md` (marked).
- `pos-char.md` (f=0 ⟺ all-even, unconditional — reusable by all routes).
- `cramer-square-integrality.md` (Lemma CRAMER).
- `concentration-exclusion.md` (Lemma 1 + Concentration Exclusion Theorem + Reduction Lemma).
- `top-piece-cut-alleven.md` (top-piece-cut + not-per-piece refutation).

## Goal Progress (for Eval History)
Still **partial**, one gap from solved, but the residual is the smallest it has ever been and now
attacked by THREE genuinely distinct machineries, all bottoming on the SAME fact — minimality ⇒
benign-U — from different objects. self-similar shrank Gap A′ to cycle-piece-deg≥3 and pinned Gap B as
budget-based; dual collapsed Positivity to one Budget Lemma (odd-cancellation eliminated) and tied the
square target to `det U∣M`; concentration fully characterized/removed the concentration obstruction and
corrected the benign-U statement. No overclaim. Ranking unchanged in order: self-similar 1689 >
dual 1557 > concentration 1498.
