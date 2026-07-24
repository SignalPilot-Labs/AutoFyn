# Proof review — IMO 2026 P3 (imo-2026-03), round 1

**Problem:** determine `c(n)` = the length Liu Bang can guarantee. **Confirmed answer:**
`c(n) = 2^n/(2^{n+1}-1)`.

## Independent verification of the shared machinery

I re-derived the load-bearing steps from scratch and checked computationally:

- **Lemma 0 (endgame greedy = odd-rank sum).** Re-derived the recursion
  `V(S) = T - min_x V(S\{x})` and the monotonicity argument. Checked the claimed value
  `Odd(S)` against an exhaustive game-tree DP on 3000 random multisets — **0 mismatches**.
  All three write-ups (continuous-move / min-inequality / sign-computation) are valid
  proofs. **CORRECT.**
- **Layer-cake identity `f(P) = M(P) = measure{t: c(t) odd}`.** Re-derived; checked
  alternating sum vs. numerically integrated odd-parity measure on 300 random multisets —
  **0 mismatches**. **CORRECT.**
- **Reduction `c(n)=2^n/D_n ⇔ M*=1/D_n`.** Algebra `2·2^n/D_n - 1 = 1/D_n` verified.
  **CORRECT.**
- **Parity toolkit / single-cut action / matching form.** Matched-pair invisibility,
  bisection-deletes, top-match `{p1,p2}→{p1-p2}`, and the min-weight-matching form of `M`
  are all correct consequences of the layer-cake identity. **CORRECT.**
- **n=1 (both bounds, `c(1)=2/3`).** All three enumerate XY's responses to the `{2/3,1/3}`
  marking (LB) and give an explicit capping cut for every marking (UB). Cases complete and
  disjoint. **CORRECT.**
- **Answer for n=2.** Dyadic `{4/7,2/7,1/7}` gives `min_XY M = 1/7` exactly (numeric);
  maximin numerics consistent with `4/7`. **Supports the answer.**

## Confirmed remaining gaps (genuinely open, same two for all three)

- **GAP-L (general lower bound):** for LB's dyadic marking, every XY response has
  `M >= 1/D_n`. Case 1 (top piece uncut) is genuinely proved; **Case 2** (XY cuts the top)
  is open: prove `(s_1 - 2^{n-1})^+ + f(Q) >= 1`.
- **GAP-U (general upper bound):** for every LB marking, XY caps `M <= 1/D_n`. Open.

These are the true cruxes. Nothing false is claimed as proved in any of the three files.

---

## Per-slug verdicts

### self-similar-recursion — CHANGES REQUESTED (Status: partial)
Correctness 10/10, rigor/completeness 8/10 (honest gaps), progress: highest.
Beyond the shared machinery it **additionally proves LB Case 1** (`f(P)=2^n-f(R') >=
2^n-(2^n-1)=1`, using the unique top piece and `f(Q)<=Σ(Q)` — I re-derived both, correct)
and the **exact Case-2 decoupling** `f(P)=(s_1-2^{n-1})^+ + f(Q)` (re-derived: at most one
top sub-piece exceeds `2^{n-1}`, and capping preserves `c(t)` below `2^{n-1}` — correct).
Self-reported Status `partial` is accurate. Gap to close: **GAP-LB Case 2** and **GAP-UB**.

### alternating-sum-threshold-potential — CHANGES REQUESTED (Status: partial)
Correctness 10/10, rigor 8/10, progress: solid foundation.
Cleanest statement of the reduction and the matching reformulation (Lemma 2); single-cut
Lemma 3 correct. No extra general-n milestone beyond the shared core (its LB/UB are both
left as G2/G3). Self-reported Status `partial` accurate. Gaps: **G2 (LB)** and **G3 (UB)**.

### majorization-smoothing — CHANGES REQUESTED (Status: partial)
Correctness 10/10, rigor 8/10, progress: solid foundation.
Cleanest write-up of Lemma 0's monotonicity sub-lemma (M) via `min(A,C+d)<=min(A,C)+d`;
parity toolkit P1–P4 correct. Honestly records that `Odd` is non-monotone under
majorization, so the one-shot certificate cannot work — a correct negative result, not a
false claim. Self-reported Status `partial` accurate. Gaps: **GAP-U** and **GAP-L**.

---

## Overall problem status: PARTIAL

Answer `c(n)=2^n/(2^{n+1}-1)` confirmed; shared lemmas certified to `lemmas/`
(`endgame-greedy.md`, `layer-cake-alt-sum.md`); n=1 and LB Case 1 proved. Two extremal
bounds (GAP-L Case 2, GAP-U) remain for every approach.

**Orchestration flag:** all three approaches share the identical reduction and hit the same
two walls — the field has collapsed to one framing (single-gap trap). Next round should
seed ≥1 approach from a genuinely different framing (e.g. an explicit LP-duality / potential
certificate on the piece-measure, or a direct adversary strategy), not another variation on
the alternating-sum reduction. Recorded in `current.md`.
