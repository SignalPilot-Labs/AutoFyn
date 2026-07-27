# Proof Review — Round 4 — imo-2026-03

## Verdict: CHANGES REQUESTED (overall); U(2) APPROVE, L(3) CHANGES REQUESTED

## Status decisions

- **Overall problem (general n): partial** — general Case B (GML(n)) and U(n) for n≥3 remain open. No change.
- **n=2 sub-result (c(2)=4/7): SOLVED.** Both L(2) (prior round, verified) and U(2) (§C-2, this round) are rigorous and complete. Independently verified below.
- **n=3 lower bound (c(3)≥8/15, §B-5): PARTIAL.** The result is CORRECT and independently verified by computation (4M random samples, 0 violations, min D=1.0000; 59+13 full-dimensional cells all D≥1), but the k_8=2 sub-case has a WRITEUP GAP: the 59-cell verification table is claimed but not written out. The k_8=3 table (13 cells) IS fully written out and correct. The k_8=1 hand proof is correct. The gap is closeable by tabulating the 59 cells (or providing the verification script).

## Scores

| Proof | Correctness | Completeness/Rigor | Progress | Status |
|-------|-------------|---------------------|----------|--------|
| U(2) (§C-2) | 10/10 | 10/10 | Major (closes U(2)) | solved |
| L(3) (§B-5) | 9/10 | 6/10 | Major (proves c(3)≥8/15 if gap closed) | partial |

---

## 1. U(2) review (§C-2, lines 737–843) — APPROVE

### S1–S4 formula verification

I independently verified all four strategy formulae by direct sorted-order computation against 2×10⁴ random 3-piece partitions (a1≥a2≥a3, sum=1):

- **S1** (halve a3): D = a1−a2. Max discrepancy vs direct: 1.1e-16. ✓
- **S2** (halve a1): D = a2−a3. Max discrepancy: 2.8e-17. ✓ The two a1/2-equal pieces are always adjacent; the remaining two positions always carry opposite signs (positions (1,4), (1,2), or (3,4) — all have + and −). The larger of {a2,a3} lands on +. ✓
- **S3** (match a2): D = |2a1−1|. Max discrepancy: 3.3e-16. ✓ The two a2-equal pieces are adjacent; the remaining {p, a3} on two opposite-sign positions → D = |p−a3| = |a1−a2−a3| = |2a1−1|. The coincident-boundary cases (a2=p, a2=a3, p=a3) are checked in the proof and all yield |2a1−1|. ✓
- **S4** (halve a1 and a2): D = a3. Max discrepancy: 0. ✓ Since a1/2 ≥ a2/2 (a1≥a2), the a1/2-pair sits above the a2/2-pair. The single a3 is at position 1, 3, or 5 (all odd, + sign) depending on whether a3 ≥ a1/2, a2/2 ≤ a3 ≤ a1/2, or a3 ≤ a2/2. ✓

### Key inequality

min(a1−a2, a2−a3, |2a1−1|, a3) ≤ 1/7. Verified:
- 0 violations in 2×10⁴ random samples.
- Grid check (401×401): max of min = 0.14214 < 1/7 = 0.142857.
- The contradiction argument (lines 799–806) is algebraically correct and exhaustive: all four > 1/7 ⟹ a3 > 1/7, a2 > 2/7, a1 > 3/7, and |2a1−1| > 1/7. The branch a1 < 3/7 is ruled out by a1 > 3/7, so a1 > 4/7, giving a2+a3 < 3/7 contradicting a2+a3 > 3/7. ✓

### Equality

At (4/7, 2/7, 1/7): S1=2/7, S2=S3=S4=1/7, min=1/7. ✓ Combined with L(2) (min_XY D(geometric) ≥ 1/7), this gives c(2) = (1+1/7)/2 = 4/7. ✓

### Cut budget

S1–S3 each use 1 cut; S4 uses 2 cuts. All ≤ n=2. ✓

**U(2) is rigorous and complete. APPROVE.**

---

## 2. L(3) review (§B-5, lines 531–690) — CHANGES REQUESTED

### Reductions R1/R2 — correct

- R1 (b7 ≥ 1 ⟹ D ≥ b7 ≥ 1): valid since all drops drop_i = b_i − b_{i+1} ≥ 0. ✓
- R2 (b1 ≥ 5 ⟹ b2 ≤ 4 ⟹ drop_1 ≥ 1): valid; the only piece exceeding 4 is 8 (or a fragment ≥ 5 of 8); other fragments ≤ 3, tail ≤ 4. ✓

### Case A (k8=0) — correct

b1=8, b2≤4, D ≥ 4 ≥ 1. ✓

### k8=1 hand proof (B2a/B2b/B2c) — correct

I verified with 10⁶ random k8=1 configurations: 0 violations, min D = 1.00004. All configs fall into B2a/B2b/B2c (no "other"). The hand bounds are all valid:
- B2a: alt_+(refine{1,2}) ≤ Σ = 3 ⟹ D ≥ (f1−4)+(r−3) = 1. ✓
- B2b: D(T) ≥ 1 by L(2) (tail is ≤2-cut refinement of G_2); f1−r ≥ 0 ⟹ D ≥ 1. ✓ L(2) applies legitimately: k8=1 means 1 cut on 8, ≤2 on tail, total ≤ 3. ✓
- B2c: alt_+(mid) ≤ Σ(mid) = 7−p ⟹ D ≥ (f1−p+r)−(7−p) = 1. ✓

The sub-case partition (b2 ∈ {4, r, p}) is exhaustive: piece 4 intact → b2=4; piece 4 cut, p≤r → b2=r; piece 4 cut, p>r → b2=p. ✓

### k8=3 (13-cell table) — correct, verified

I independently enumerated all full-dimensional sort-order cells for k8=3 (3 cuts on 8, tail {4,2,1} intact, f1≥f2≥f3≥f4≥0, Σf=8). Found **exactly 13 full-dimensional cells** — matching the proof's claim. All 13 match the proof's table. All 13 have D ≥ 1 (minimum D = 1.0, 0 violations).

The 166 additional boundary cells (where some f-values coincide) are covered by the closures of the 13 full-dimensional cells. All 179 feasible cells have D ≥ 1. ✓

I verified each row's D linear form against an independent computation — all match. The "why ≥ 1" column uses valid cell-constraint bounds. ✓

### k8=2 (59 cells) — CORRECT RESULT, but WRITEUP GAP

I independently enumerated all full-dimensional cells for k8=2:
- V=4: 32 full-dim cells ✓
- V=2: 14 full-dim cells ✓
- V=1: 13 full-dim cells ✓
- **Total: 59** — matching the proof's claim.
- All 59 cells have D ≥ 1. Minima are in {1, 5/3, 2, 3, 5} — matching the proof's claim.
- All 563 feasible cells (including boundaries) have D ≥ 1, 0 violations.

**THE GAP:** The proof describes the 59-cell verification ("the LP ... is solved exactly at a vertex") but does NOT write out the per-cell linear forms and bounds. Unlike k8=3 (which has a complete 13-row table), k8=2 has only a description and one example. The proof says "the cell count (72) is too large to hand-write legibly" — but (a) the actual count is 59, not 72 (minor error), and (b) 59 cells is tabulable (my verification lists them all).

Under the rigor rules ("No hand-waving. If a step is non-trivial, justify it"), a computation described but not shown is a gap. The result is TRUE (independently verified), but the writeup doesn't allow a reader to verify it from the text alone.

**Closeable by:** writing out the 59-cell table (like the k8=3 table) or appending the verification script.

### Degenerate-boundary coverage — correct

D is continuous in the piece sizes (sorting is continuous, and at ties the alternating sum is the same regardless of tie-breaking). Closed cells (fragments ≥ 0) include degenerate boundaries. Fewer-cut configs (with 0-fragments) are boundary points of exactly-3-cut cells, covered by the closed-cell analysis. ✓

### Cut-budget accounting — correct

The case split correctly enforces ≤3 cuts total: k8 + k_tail ≤ 3 for each case. k8 ∈ {0,1,2,3} exhausts all distributions. ✓

### Random sample — 0 violations

4×10⁶ random ≤3-cut refinements of G_3: min D = 1.0000, 0 violations. ✓

### Minor issues

1. **"72" should be "59"** (line 688): the remark says "the cell count (72) is too large" but the actual count (verified independently) is 59.
2. **Overclaim in summary** (line 861): "attained uniquely by LB = geometric and XY = full halving" — this is in the "confirmed (not proved)" section, but it's contradicted by the L(3) proof itself, which shows D=1 is attained on a whole region (the layered-straddle family), not uniquely at full halving. This doesn't affect the rigorous proofs but is an inaccuracy in the summary.

### Equality claims

The proof correctly states "attained throughout the layered-straddle family" and "in particular at full halving" — not "iff full halving" (which was the round-3 overclaim). ✓

---

## 3. Overall assessment

The two new proofs represent substantial progress:
- **U(2) is fully solved** — c(2) = 4/7 is now rigorously proved in both directions (L(2) + U(2)). This is the first complete n-case beyond n=1.
- **L(3) is correct but has a closeable writeup gap** — the result c(3) ≥ 8/15 is verified by independent computation (cell enumeration + 4M random samples), but the k8=2 sub-case needs its 59-cell table written out to meet the "no hand-waving" standard.
- **The overall problem remains partial** — general Case B (GML(n)) and U(n) for n≥3 are open.

The file's current Status (partial) is CORRECT and should remain so.

## Specific gaps to close (for the builder)

1. **Write out the 59-cell table for k8=2** (V=4: 32 cells, V=2: 14 cells, V=1: 13 cells) — each row should have the sort order, the D linear form, and the "why ≥ 1" bound, exactly like the k8=3 table. Alternatively, append the verification script as an executable artifact.
2. **Fix "72" → "59"** on line 688.
3. **Soften "attained uniquely by ... XY = full halving"** on line 861 to "attained at LB=geometric" (the L(3) proof itself shows multiple XY strategies achieve D=1 on geometric).
