# Build report — ll-dyadic-symdiff (Round 6)

**Status: partial.** Slug file: `results/imo-2026-03/approaches/ll-dyadic-symdiff.md`.

## What I did (per the outline-reviewer's mandate)

1. **Proved & propose the General reflection identity (Lemma REFL) — the round's rigorous advance.**
   For any multiset `Q` with `μ = max(Q) ≥ 2^{n−1}`, `Q' = Q ∖ {μ}`, and `R` with `max(R) ≤ 2^{n−1}`:
   `A(Q∪R) = μ − A(Q'∪R)`. Full proof in the file: on `[0,μ)`, `N_Q = 1 + N_{Q'}` gives
   `S_Q = [0,μ)∖S_{Q'}`; since `S_R ⊆ [0,μ)`, the set identity `(U∖A)△B = U∖(A△B)` yields
   `S_Q△S_R = [0,μ)∖(S_{Q'}△S_R)`, hence the identity. This **extends** the certified `max(Q)=2^{n−1}`
   identity to the whole range `μ ≥ 2^{n−1}` (so it also covers the band `μ∈(2^{n−1},2^{n−1}+1)`).
   Machine-verified 490/490, 0 mismatches (1/4-grid, joint cut budget enforced). Proposed to
   `lemmas/ll-reflection-identity.md`.

2. **Reduced branches B1 (`2^{n−1}<μ<2^{n−1}+1`) and B2 (`μ=2^{n−1}`) to one upper bound**
   `(RED): A(Q'∪R) ≤ μ − 1`. Non-circular (Q'∪R is not a valid G_{n−1}-refinement; sum ≠ 2^n−1), so it
   is an upper-bound target, never a recursive IH call. Verified 490/490, 0 violations, tight (min slack 0).

3. **DELETED the FALSE Step-2 "A ≥ 2" slack claim** and corrected the record with a *sharper* fact than
   the reviewer had: on the 1/4-grid with the joint budget, the `max(Q) < 2^{n−1}` branch (B3) attains
   `A(Q∪R) = 1` **exactly** — witness `Q={3,3,2}`, `R={2,2,2,1}` (n=3, budget 2+1=3=n). So B3 is *also
   tight*; the `max(Q)` split does NOT confine tight cases to B2, and the A≥2 mechanism is permanently dead.
   (The reviewer's coarse-grid min 3/2 is itself not tight; the true min is 1.)

## What remains open (honestly flagged, not papered over)

Sub-3b now reduces to exactly two inequalities, both the shared INC/GAP crux:
- **GAP-A** (B1,B2 via RED): `A(Q'∪R) ≤ max(Q) − 1`. Upper-bound form; needs the alternating-tail bound
  `(p_2−p_3)+(p_4−p_5)+⋯ ≥ 1` for general n = `ll-inclusion-gap`'s G-INC-1. Not closed.
- **GAP-B** (B3): `A(Q∪R) ≥ 1` for `max(Q) < 2^{n−1}`. Tight, no slack; needs R's dyadic structure. Not closed.

The naive integral bound `∫(N_Q−N_R)=1` is confirmed insufficient for both. I did not manufacture a
proof for either; Sub-3b is not closed.

## Verification (bounded, <20s each, joint budget `#Q-cuts+#R-cuts ≤ n` enforced)
- Lemma REFL: 490 instances, 0 mismatches.
- (RED) `A(Q'∪R) ≤ μ−1`: 490 instances, 0 violations, min slack 0.
- GAP-B (`max(Q)<4`): min `A(Q∪R)=1` (witness above), 0 violations of A≥1 — refutes A≥2 on fine grid.
- Anchor `R=G_2` uncut: min A=1, 0 violations — flagged as a natural next closeable sub-target.

## Assessment for the orchestrator
This slug's independent value is now the **certifiable Lemma REFL** (clean, reusable, collapses B1∪B2 to
GAP-A). Beyond that, the reviewer's read is confirmed: Sub-3b = GAP-A ∪ GAP-B converges on the same
INC/GAP arithmetic crux that `ll-inclusion-gap` owns. The two LL routes now share one residual
(alternating-tail bound / G-INC-1). Recommend: certify Lemma REFL; consider whether to keep two LL slugs
on the identical residual or merge, since neither closes the crux yet. The `R=G_{n−1}` uncut anchor
(clean dyadic S_R) is the most tractable next lower-bound sub-target.

## Promotable lemma
- **Lemma REFL** (general reflection identity), proven in full — proposed to
  `results/imo-2026-03/lemmas/ll-reflection-identity.md`.
