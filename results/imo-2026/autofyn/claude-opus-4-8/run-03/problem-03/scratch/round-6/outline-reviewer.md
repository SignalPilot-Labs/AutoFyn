# Outline review — imo-2026-03, round 6

Start 01:35 UTC. I ran the cheap-kill numerics the outliner requested on the new framing's
load-bearing steps (UB cut budget + bound, LB Δ and G≥Δ). Results below drive the verdicts.

## segment-subset-pigeonhole (NEW, unified both-bounds) — APPROVE

This is the official-solution structure (surfaced by both fresh + ubframing explorers from Evan
Chen's IMO-2026 notes). It is a genuinely different framing — works on Liu's n+1 ORIGINAL segments
and their subset sums, never touching the layer-cake S(B)/(PM)/β machinery all four prior slugs
share. It is a whole-problem attempt (both bounds in one file). It must be reproven from scratch —
NOT cited. Every load-bearing step numerically confirmed:

- **UB (mirrored-cut UB1 + pigeonhole UB2):** n=1..5, 300 random A each — the explicit construction
  achieved G ≤ |Σ(S)−Σ(T)| ≤ 1/D_n AND cut count ≤ n in ALL 1500 cases, 0 failures. The cut budget
  (the round-2 MATCH bookkeeping trap, GAP1a) holds.
- **LB (tree extraction LB1 + dyadic LB2):** Δ(dyadic) = 1/D_n exactly, n=1..6. G ≥ Δ(A) for random
  A + random XY plays: 0 violations / ~1600. Dyadic A forces G ≥ 1/D_n: 0 violations / 8000 plays.

The four gaps are genuinely attackable (not hidden leaps). Specific guidance for the builder so it
does not re-fall into the round-4/5 bookkeeping traps:

- **GAP1 (UB1), resolved cleanly — do NOT insist the overhang be a single piece.** The correct,
  trap-free argument: bisect every segment ∉ S∪T (equal halves) and merge-align S vs T so the
  overlap [0,Σ(T)] splits into matched EQUAL S/T sub-piece pairs. Then compute S on the FINAL output
  multiset via L4's *general* min-pairing form: pair every equal pair together (cost 0), and pair the
  leftover overhang pieces P_1..P_r (summing to Σ(S)−Σ(T)) among themselves. Their contribution is
  ≤ their alternating sum ≤ ΣP_i = Σ(S)−Σ(T). Hence G = S(output) ≤ min-pairing ≤ |Σ(S)−Σ(T)|. The
  overhang need NOT be one physical piece — this dissolves GAP1c and the "input-vs-output pairing"
  conflation warning (GAP4): S is computed on the output multiset directly, so there is no
  input/output mismatch to reconcile. Still write the cut-budget count explicitly (the numerics
  confirm ≤ n, including n+1−|S| cuts in the T=∅ case since |S|≥1).

- **GAP2 (pigeonhole):** 2^{n+1} sums vs D_n = 2^{n+1}−1 bins ⟹ two distinct subsets share a bin.
  Handle the T=∅ case (one of the pigeonhole pair may be the empty set): then S is nonempty (distinct),
  diff = Σ(S) ≤ 1/D_n, UB1 with T=∅ uses n+1−|S| ≤ n cuts — verified in the sim. No complementary-pair
  problem: pigeonhole selects a CLOSE pair, so Σ(S)−Σ(T) ≤ 1/D_n by construction.

- **GAP3 (LB1 tree), sound with the edge cases nailed:** V=n+2, E=n+1 ⟹ Σ_components (v_c−e_c) = 1,
  each connected component has v_c−e_c ≤ 1 (=1 iff tree), so ≥1 tree component exists (cycle-rank,
  rigorous). Two edge cases the builder must state: (a) **no isolated-vertex tree** — every segment
  yields ≥1 piece and every piece is an endpoint of exactly one gap-edge, so every vertex has degree
  ≥1; hence the tree component has ≥1 edge ⟹ both bipartition sides nonempty ⟹ ε≠0. (b) **self-loops**
  (both pieces of a gap-pair share a parent) create a cycle, so they never lie in the tree component;
  in the tree component every segment's pieces pair ACROSS to other segments, so Σ(S)−Σ(T) = Σ over
  component edges of ±d_i (each tree edge crosses the bipartition), giving |Σ(S)−Σ(T)| ≤ Σd_i = G.
  The dummy vertex (length 0) is handled the same way; if the tree is {dummy, w} then a_w = d_{n+1} ≤ G.

- **GAP4 (reconciliation):** with the GAP1 fix above this is a non-issue — S is defined and computed
  on the output multiset throughout, and G=S(B), 2c(n)−1=1/D_n are L0/L2 (certified).

The builder should still run the exact-Fraction cheap-kill FIRST (I already did; it passes) and then
write the prose proof. This approach supersedes — does not patch — the (PM)/(CB)/β LB wall and the
refuted UB branch-inequality line.

## induction-peel (advance, LB fallback) — CHANGES REQUESTED (build)

Leader with the most certified progress (L0–L14). Keep it live as the LB fallback in case LB1's tree
reconstruction hits an unforeseen rigor snag. Two required course-corrections:
- **RETIRE the UB branch-inequality line (its Open gap 2).** The official source's explicit n=5
  all-32-branches counterexample (independently confirms the field's F1) shows top-two-greedy
  MATCH/BISECT is the wrong UB structure — it is not salvageable as scoped. Do not spend builder
  effort there; the UB now belongs to segment-subset-pigeonhole.
- **FALSIFY-FIRST the s_1=H boundary-invariance** (30s exact-Fraction check at larger n and >2
  rest-shards) BEFORE investing in the shard-count induction. The peel-and-recurse and k_C≥1 aggregate
  charging stay as gaps. Do NOT re-attempt majorization/Robin-Hood smoothing (refuted).

## alternating-sum-potential — HOLD (not built)
Shares the exact LB wall (coupled (Wβ) = L12 = (CB)) with induction-peel and interlacing in the same
framing. With induction-peel carrying the LB fallback and segment-subset-pigeonhole offering an
independent clean LB, a third builder on the same wall adds no diversity this round. Correct to hold.

## interlacing-bijection — HOLD (not built)
Net-new content is only the reframing + IB-1 (= certified L12); the excess→deficit injection Φ is
unbuilt and sits on the same shared wall. The segment-subset LB1 is strictly cleaner. Correct to hold.

## Field diversity note
The prior 4-slug field had collapsed onto ONE LB wall + ONE refuted UB structure (same layer-cake
framing). segment-subset-pigeonhole breaks that: it attacks BOTH bounds from a genuinely far framing
(subset sums of the original segments, pigeonhole + spanning-tree), with both bounds numerically
verified end-to-end. This is the diversity injection the orchestrator called for. Building it plus the
established leader (as fallback) is the right split; no branch/copy requested or warranted.

## Ranking (folded)
Registered segment-subset-pigeonhole (1500 cold-start), then ranked head-to-head across the whole
field. New approach wins vs induction-peel / alternating-sum / interlacing (verified route to BOTH
bounds vs 5-round-stalled walls + refuted UB), lands at Elo 1557 (2nd), anchored above the mid-field.
induction-peel 1688 (leader), alternating-sum 1576, segment-subset-pigeonhole 1557,
interlacing 1499, global-max-peel 1485, then the dead/dormant tail. All stale flags cleared.

build set: segment-subset-pigeonhole, induction-peel
