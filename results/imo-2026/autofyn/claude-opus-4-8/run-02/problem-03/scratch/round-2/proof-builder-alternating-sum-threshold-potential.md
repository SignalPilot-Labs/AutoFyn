# Proof-builder report — alternating-sum-threshold-potential (round 2)

**Status: partial** (was partial). Real progress on GAP-U; negative result on the assigned
GAP-L dual route.

## GAP-L via one-shot dual price φ — RULED OUT (as the reviewer flagged)
The LP/matching-duality route for the lower bound provably cannot supply a certificate:
1. The dual of min-weight *perfect* matching (phantom 0 if odd) is the parity-crossing
   bound `cost ≥ ∫ 1[c_P(t) odd] = f` — an **equality** (Lemma 2). The strongest dual just
   re-derives `f`; no leverage on `f(refinement) ≥ 1`.
2. Any *fixed* length-only price is forced `φ ≤ 0` (two equal pieces `x,x` match at cost 0
   ⇒ `2φ(x) ≤ 0`, and cuts create equal pieces), so `Σφ ≤ 0 < 1`. A monovariant dual with
   `Σφ ≥ 1` cannot exist.
This confirms the outline-reviewer's "φ collapses to re-deriving f" risk. **Pruning value:**
the field should stop looking for a one-shot dual for GAP-L; GAP-L is the exchange-lemma /
bisection-cascade target owned by `self-similar-recursion`. (GAP-L Case 1, top uncut, is
proved here in one line via the new Lemma 5: `f ≥ 2a₁ − S = 1`.)

## GAP-U via explicit XY strategy — genuine partial (the productive half)
Reduced GAP-U to a single clean invariant and proved most of it:
- **Invariant (I):** `g_b(P) ≤ s/D_b` for any multiset with `≤ b+1` pieces, sum `s`
  (`g_b` = min `f` Xiang Yu forces with `≤ b` cuts). At `b=n, s=1` this **is** GAP-U.
  Verified numerically TRUE and TIGHT (dyadic extremal; 3·10^5 samples, ratio ≤ 1).
- **Proved rigorously:** the cut-and-pair reduction `g_b(P) ≤ g_{b-1}(R)` (Lemma 4); base
  `b=0`; the adaptive **STOP** rule (`f(P) ≤ s/D_b` ⇒ done; in particular `a₁ ≤ s/D_b`) —
  this is the correct "adaptive stop keyed to the target" the dispatch asked for, and it
  explains why fixed bisect-n / iterated-top-match overshoot (they cut past the stop line);
  and the **geometric step** under (H) `max(a₁,2a₂) ≥ (2^b/D_b)s`, using `1−D_{b-1}/D_b =
  2^b/D_b` so one cut drops mass to `≤ (D_{b-1}/D_b)s` and the IH closes it.
- **Open sub-case (M) — the single remaining gap:** `f(P) > s/D_b` AND
  `max(a₁,2a₂) < (2^b/D_b)s` (near-balanced, surplus budget). (I) still holds numerically
  here, but the lock-step "one cut ⇒ budget−1 ⇒ mass×r_b" accounting is too coarse; needs an
  amortised multi-cut phase bound (or an IH strengthened to track piece count `m`).

## Newly proved reusable lemmas (propose for certification)
- **Lemma 4 (cut-and-pair reduction):** `g_b(P) ≤ g_{b-1}(R)`, R from bisect-top
  (`sum s−a₁`) or top-match (`sum s−2a₂`), `|R|=m−1`. Fully proved (exhibit the matching;
  Lemma 2 upper-bound only). → `lemmas/cut-and-pair-reduction.md`
- **Lemma 5 (`f ≥ 2a₁ − S`):** for any multiset, alternating sum `≥ 2·max − total`. Fully
  proved; gives GAP-L Case 1 instantly. → `lemmas/alt-sum-two-max-minus-total.md`

## Net for the field
- GAP-L one-shot dual: dead (documented) → route GAP-L through the exchange lemma.
- GAP-U: downgraded from "open crux" to "prove one amortisation lemma for regime (M)"; the
  invariant `g_b(P) ≤ s/D_b`, its reduction, and two of three regimes are done.

Verdict expected: CHANGES REQUESTED (partial, real progress; one delimited gap remains).
File: results/imo-2026-03/approaches/alternating-sum-threshold-potential.md
