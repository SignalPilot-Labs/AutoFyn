## imo-2026-03

Terrain shift this round: two explorers independently located a unified framing (matching the
official solution shape) that works with Liu Bang's n+1 ORIGINAL segments — dissolving BOTH
standing walls (UB branch-inequality casework AND the LB (PM)/(CB)/β residual) at once. I open
ONE new unified slug for it, keep the strongest LB-residual advance alive as a fallback, and hold
the two approaches that share the (now possibly superseded) LB wall.

---

segment-subset-pigeonhole: new
Target: the WHOLE problem — c(n) = 2^n/(2^{n+1}−1) with BOTH bounds (XY forces gap G ≤ 1/D_n for
every A; Liu via dyadic A forces G ≥ 1/D_n). D_n := 2^{n+1}−1.
Technique: pigeonhole over the 2^{n+1} subset-sums of Liu's n+1 original segments (UB) + a
spanning-tree/bipartite extraction giving G ≥ Δ(A) = min nonzero |Σ ε_i a_i| (LB). No induction
on n, no branch-inequality casework, no (PM) residual. Full skeleton in
results/imo-2026-03/approaches/segment-subset-pigeonhole.md.
Skeleton:
  1. Reduction G = S(B); Liu-value = (1+G)/2 (import L0, L2); target ⟺ force G vs 1/D_n.
  2. Lemma UB1 (mirrored cut): for disjoint S,T ⊆ segments, XY refines in ≤n cuts to G ≤ |Σ(S)−Σ(T)|
     — merge-align the S-block against the T-block, matched equal sub-pieces cancel (global L4),
     one overhang of length |Σ(S)−Σ(T)| survives.
  3. Lemma UB2 (pigeonhole): 2^{n+1} subset sums in [0,1] vs D_n bins ⟹ distinct S′,T′ within
     1/D_n; prune common elements ⟹ disjoint S,T with |Σ(S)−Σ(T)| ≤ 1/D_n; apply UB1 ⟹ G ≤ 1/D_n
     for every A. (Explains the 2^{n+1}−1 denominator directly — one line.)
  4. Lemma LB1 (tree/bipartite): d_i := x_{2i−1}−x_{2i}, G = Σd_i; multigraph n+2 vertices (segments
     + dummy), n+1 edges ⟹ a tree component ⟹ bipartite S⊔T ⟹ Δ(A) ≤ |Σ(S)−Σ(T)| ≤ G.
  5. Lemma LB2 (dyadic): a_i = 2^{i−1}/D_n ⟹ Δ = 1/D_n (nonzero {−1,0,1}-combo of powers of 2 is a
     nonzero integer; verified numerically n=1..5). ⟹ Liu forces G ≥ 1/D_n. Bounds meet.
Key lemmas (claim + mechanism):
  - UB1 G ≤ |Σ(S)−Σ(T)| — because merge-aligning the two subset-blocks pairs off equal-length
    sub-pieces that cancel in the alternating sum by the adjacent-equal-cancellation of certified
    L4, leaving only the Σ(S)−Σ(T) overhang.
  - UB2 G ≤ 1/D_n — because 2^{n+1} subset sums in [0,1] against D_n = 2^{n+1}−1 sub-intervals
    forces two within 1/D_n (pigeonhole); pruning common elements preserves the difference.
  - LB1 G ≥ Δ(A) — because n+2 vertices with only n+1 edges forces a tree component (cycle-rank),
    whose bipartition realizes some signed segment-sum ±Σd_i ≤ G, and that signed sum is one of the
    values Δ minimizes over.
  - LB2 Δ(dyadic) = 1/D_n — because a nonzero {−1,0,1}-combination of superincreasing powers of 2
    is a nonzero integer (|·| ≥ 1), attained by ε = e_1.
Open gaps: GAP1 UB1 mirrored-cut bookkeeping (≤n-cut budget, global-sort adjacency of matched
pairs, overhang handling) — the load-bearing step; GAP2 UB2 pigeonhole edge/degenerate cases;
GAP3 LB1 well-defined edge assignment (self-loops = 0 contribution), tree-component existence,
sign bookkeeping; GAP4 reconcile G with S(B) and confirm UB1's input-piece pairing agrees with
L4's output-multiset pairing (do NOT conflate — round-4/5 warning).
Cases to cover: UB — none by shape of A (uniform pigeonhole) + n=1 base + zero-length-segment
degeneracy; LB — dyadic construction only, plus multigraph self-loop/dummy-edge cases.
Watch out for: the UB1 cut-budget/piece bookkeeping (GAP1a) is where the round-2 MATCH move and
the whole refuted match/bisect-on-top-two family died — run the exact-Fraction cheap-kill (n≤4,
verify achieved G ≤ |Σ(S)−Σ(T)| AND cut count ≤ n) BEFORE the full proof; input-vs-output pairing
conflation (GAP4); multigraph self-loop breaking the nonempty-bipartition step (GAP3a).

---

induction-peel: advance
Target: the WHOLE problem (leader, Elo 1693); serves as the LB fallback if segment-subset-
pigeonhole's LB1 tree argument resists rigorous reconstruction.
Technique: strong induction peeling the top dyadic scale (unchanged spine). New push this round:
close the LB residual (CB) [k_C=0 shard inequality] via the **shard-count induction** lead the
lbclosure explorer surfaced — a genuinely new reduction axis, orthogonal to the existing induction
on n.
Skeleton (delta from current file):
  1. Import certified L0–L14; residual is (CB) Σ A_{2m} ≤ Σ B_{2m−1} for k_C=0, c_n≥2, e<1.
  2. NEW: exploit the s_1 = H boundary invariance (slack of Q_low is CONSTANT under any further
     split of the remaining mass H) — verified exact n=3,4.
  3. Peel the boundary H-shard against C's own top value H (L9-style self-pairing, zero net
     displacement), reducing (CB) to the same inequality one level down (n → n−1) on
     "rest of Q_low (sum H) vs rest of C (= P_{n−2} dyadic)".
  4. Induct on the shard count c_shards (base c_shards=1 = Case 1, already closed by L7/L8).
  5. Then the k_C≥1 aggregate cross-scale two-source charging (harder, only aggregate survives per
     the round-5 pointwise refutation).
Key lemmas: s_1=H invariance — because the H-shard's boundary crosses C exactly at C's own H-value
crossing, so the two H-events form a matched pair (L9) leaving a level-(n−1) copy of the problem.
Open gaps: (a) FALSIFY-first the s_1=H invariance at larger n and >2 rest-shards (30s Fraction
check) before investing; (b) the peel-and-recurse reduction made rigorous; (c) the k_C≥1 aggregate
charging (still the hardest residual). UB branch inequalities (gap 2): DEPRIORITIZE / retire — the
official-shape counterexample (n=5, all 32 top-two-greedy branches fail) plus the new pigeonhole
route make it the wrong top-level UB structure.
Cases to cover: k_C=0 (via shard induction) then k_C≥1 (aggregate); base c_shards=1.
Watch out for: pure majorization/Robin-Hood smoothing on the shard vector is REFUTED (non-monotone,
this round) — the induction must condition on which C-band each shard boundary lands in, not just
shard values; do not re-attempt a smoothing proof.

---

alternating-sum-potential: hold
Rationale: shares the exact LB wall (coupled (Wβ), = L12 = (CB)) with induction-peel and interlacing
— all three die together on it. With induction-peel carrying the LB-fallback via the new shard-count
axis and segment-subset-pigeonhole offering a clean independent LB (tree/Δ), a third builder on the
same wall in the SAME framing adds no diversity this round. Keep live; revive only if the shard-count
axis stalls and its distinct dependency (must consume lower-block surplus S(R)−1) offers new leverage.

---

interlacing-bijection: hold
Rationale: its entire net-new content is the reframing + IB-1 (= certified L12); the excess→deficit
injection Φ is unbuilt (heights ≥3, budget-totality) and sits on the same shared LB wall. The new
segment-subset LB1 is a strictly cleaner combinatorial LB (one tree extraction vs an open injection).
Hold; do not build this round.

---

Recommended build set: **segment-subset-pigeonhole** (new, the priority — attacks both walls with a
genuinely different framing, runs the Fraction cheap-kills on GAP1/GAP3 first) and **induction-peel**
(advance — the LB fallback via the new shard-count induction). Hold alternating-sum-potential and
interlacing-bijection to avoid three builders on one shared wall in one framing.
