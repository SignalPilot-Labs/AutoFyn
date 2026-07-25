# Build report — segment-subset-pigeonhole (round 6)

**Status: SOLVED.** Complete rigorous proof of imo-2026-03, both bounds, final answer
c(n) = 2^n/(2^{n+1}−1) stated and verified (n=1 ⟹ 2/3; tightness at dyadic checked).

## What was closed (all four outline gaps)

- **GAP1 (UB1 merge-alignment).** Fully rigorous. Followed the reviewer's fix: compute S on the
  OUTPUT multiset via L4's general min-pairing form (equal matched pairs cost 0; overhang pieces
  paired among themselves cost ≤ their mass = Σ(S)−Σ(T)). No single-piece-overhang assumption.
  Cut budget proven ≤ m−1 EXACTLY by a clean three-group count: |L| leftover bisections +
  ≤|T| cuts on S-parts + ≤|S|−1 cuts on T-parts = m−1. For m=n+1 that is exactly n.

- **GAP2 (UB2 pigeonhole).** Resolved, plus a case the outline/skeleton had NOT explicitly
  handled: **m ≤ n parts**. Pigeonhole with D_n bins only guarantees a collision when 2^m > D_n,
  i.e. m = n+1. For m ≤ n I added a separate clean argument: XY bisects ALL m parts (m ≤ n
  splits) ⟹ B is m equal pairs ⟹ S(B)=0 ≤ 1/D_n. This is the one substantive gap the skeleton
  had glossed (it implicitly assumed m=n+1). Now airtight. T=∅ / distinct-subset pruning handled.

- **GAP3 (LB1 tree extraction).** Fully rigorous. V=n+2, E=⌈N/2⌉≤n+1 with N≤2n+1. Tree-component
  existence via cycle-rank (#trees ≥ V−E ≥ 1). All edge cases nailed: no isolated part-vertex
  (every part has ≥1 piece = ≥1 incidence); isolated dummy excluded by a parity split (N odd ⟹
  dummy has degree 1; N even ⟹ E≤n ⟹ ≥2 tree components so one has a real part); self-loops are
  1-cycles hence never in a tree component. Edge-length identity Σσ(v)a_v = Σ±d_e proven from the
  incidence bookkeeping; |Σσa| ≤ Σ_{comp} d_e ≤ S(B) = Σ_all d_e.

- **GAP4 (reconciliation).** Non-issue as the reviewer predicted: S is defined and computed on the
  output multiset B throughout (§0, L2, L4, §1–4 all the same functional), so no input/output
  pairing mismatch.

## Cheap-kills run first (exact Fraction, <30s each, all passed)
- UB merge-align: n=1..4, 200 random A each — S(B) ≤ |Σ(S)−Σ(T)| ≤ 1/D_n AND cuts ≤ n: 0 failures.
- Δ(dyadic)·D_n = 1 for n=1..6: exact.
- LB1 S(B) ≥ Δ on random ≤n-split refinements of dyadic A, n=1..4, 400 each: 0 violations.

## Spec concerns
None. The one thing worth flagging to the reviewer: the m ≤ n case of the UB was implicit in the
outline (it assumed n+1 parts); I closed it with the bisect-all argument. This is a genuine
addition, not in the skeleton verbatim, but elementary and verified. The dyadic LB needs m = n+1
(it is), so LB1 is only invoked at m = n+1 where V=n+2 > E holds.

Proof written to results/imo-2026-03/approaches/segment-subset-pigeonhole.md (Status: solved).
