## imo-2026-03 — LENS: lower-bound Case 2 (Liu Bang dyadic guarantee, XY cuts the top piece)

- **Distinct openings** (ways to close Sub-claim A2 / G1, ranked by how much new leverage they add beyond what's already written in the two live approach files):

  1. **Unify with the min-pairing identity L4 instead of the layer-cake identity L3.**
     Both live approaches use L3 (parity/layer-cake) for the lower bound and only
     alternating-sum-potential's §5 uses L4 (min-pairing/β) for the upper bound. But my
     numerics below show the exact extremal configuration for Case 2 is the *same* MATCH
     cascade that alternating-sum-potential already uses as the optimal XY witness for the
     upper bound at A = G_n. This is a strong hint that Sub-claim A2 and Sub-claim B/G2
     are two faces of one combinatorial fact about L4: "with ≤n cuts on the superincreasing
     set {1,2,...,2^n}, the maximum achievable matched-smaller-mass β is exactly 2^n − 1
     (units, i.e. (2^n−1)/D_n after scaling), attained uniquely (up to the continuum of
     near-ties found numerically) by the cascade/MATCH construction." Proving *that* single
     β-extremal-value claim as an upper bound on β for ALL cut sequences would simultaneously
     (a) give Sub-claim A2 (S = 1 − 2β ≥ 1 − 2(2^n−1)/D_n... — needs the exact translation,
     but structurally it is the same quantity) and (b) already-known achievability gives the
     matching upper-bound construction. This is the most promising single opening: **recast
     both remaining gaps as one extremal combinatorial claim about β under a cut budget**,
     rather than pursuing Case 2 and Lemma B/D as separate proofs.

  2. **Direct induction on Case 2 using the "+1 reserve" exactly where it is numerically spent.**
     My computation (see below) shows that at the extremal cascade, S(Q) and S(C) differ by
     *exactly* 1 for every n (not that either is near 0), and the overlap W equals
     min(S(Q),S(C)) exactly (full overlap — the bound S(whole) ≥ |S(Q)−S(C)| is *tight*, not
     just an inequality). This says Sub-claim A2 does NOT need a subtler bound than
     |S(Q)−S(C)|; it needs the sharper fact **|S(Q) − S(C)| ≥ 1 whenever the overlap W is
     close to its max min(S(Q),S(C))**, and more slack when W is smaller. Concretely: the
     open task reduces to proving, for Q a refinement of a single mass 2^n into c+1 parts
     (c ≤ n arbitrary) and C a ≤(n−c)-cut dyadic refinement of {2^0,...,2^{n−1}} with
     S(C) ≥ 1 (IH), that S(Q)+S(C)-2W ≥ 1 where W is controlled using that **every part of C
     is ≤ 2^{n−1}** (so W only accumulates mass at heights t ≤ 2^{n-1}, capping how much of
     S(Q)'s mass above that height can be cancelled) — this is the same idea already flagged
     in both approach files but my numerics show WHERE to spend the "+1": it is spent exactly
     once, at the very bottom of the cascade (the extra unmatched "1"), never distributed.
     This suggests inducting on **c** (cuts spent on top) rather than on n: peeling one cut off
     the top at a time and asking what changes.

  3. **Re-peel by GLOBAL current-max instead of by "the original top piece."**
     Case 1's clean proof (already complete) works by removing the piece that is currently
     largest, which happens to equal the *original* top piece 2^n exactly because it survives
     uncut. In Case 2 the global max of B need not be an original piece — it could be a
     sub-piece of Q (if XY leaves a big shard) or an original piece of R. A genuinely
     different induction: induct on total remaining pieces (not on n), always peeling
     whichever single piece is currently the strict max of the WHOLE current multiset B
     (wherever it came from), and track how the "superincreasing margin" transfers. This
     sidesteps the artificial Q/C split entirely and might make Case 1 and Case 2 into one
     uniform argument, at the cost of needing a more general (weaker-hypothesis) inductive
     statement about arbitrary refinements of superincreasing sets, not just P_n itself. Not
     attempted in either live file; worth a dedicated try since it removes the asymmetric
     bookkeeping that both Q/C-split routes are stuck on.

- **Candidate technique(s):** L3 layer-cake decomposition (already in use, insufficient alone);
  L4 min-pairing/β witness (recommended as the *unifying* tool, opening 1 above); strong
  induction on cut-budget c rather than on n (opening 2); re-peeling by global max instead of
  fixed "original piece" (opening 3, a genuinely different induction variable).

- **Cheap-kill candidates:** None that dispatch the whole gap cheaply. One useful structural
  fact for free: **the overlap W is always confined to heights t ≤ 2^{n−1}** (since every part
  of C is ≤ 2^{n−1}, so N_C(t) = 0 — hence not odd — for t > 2^{n−1}); this immediately gives
  S(whole) = S(Q)⁠|_{t>2^{n-1}} + [S(Q)+S(C)-2W]|_{t≤2^{n-1}}, i.e. **the part of S(Q)'s mass
  living strictly above 2^{n−1} is untouchable by the overlap and survives into S(whole)
  unconditionally.** This is a genuine (verified, not just conjectured) structural fact worth
  handing to the outliner/builder — it already isolates exactly which part of Q can be
  "cancelled" by C and which cannot.

- **Knowledge-base entries to use:** check `knowledge_base.md` for entries on alternating-sum
  potentials / minimax games with superincreasing structure — the certified project lemmas
  L0–L4 already cover the reduction machinery; the outliner should look for any KB entry on
  "extremal principle" or "invariants/monovariants" for game potentials to support opening 3.

- **Analogous past problems (cruxes):** `aimo-0117` (combinatorics, games-and-strategy) is a
  strong structural analog: Jesse plays a strictly superincreasing (two-sided geometric,
  powers of 2) sequence of values into two boxes so that the single largest value played
  always exceeds the sum of all previously-played values, and maintains the invariant "the
  current largest power of 2 sits in the target box" by induction, which is exactly the
  mechanism behind Case 1 here (largest-piece-survives ⇒ automatically dominant, same
  superincreasing "+1" idea: 2^j > sum of all smaller played values). It is NOT directly
  analogous to the still-open Case 2 (that problem's invariant never needs to handle "the
  largest value gets split into pieces mid-game" — Jesse always adds a *fresh* value, he
  never subdivides an existing one), so it validates the superincreasing-invariant style of
  argument used in Case 1 but does not supply a ready-made technique for Case 2's splitting
  interaction. Other games-and-strategy cruxes surveyed (aimo-0596 pairing/involution
  strategy, aimo-0663 component-counting pigeonhole, aimo-0225 strategy-stealing) are about
  discrete combinatorial games with a fixed finite state space, not a continuous-split
  alternating-claim game, and do not transfer usefully here — no forced match beyond
  aimo-0117's superincreasing-invariant flavor.

- **Prior progress:** as recorded in `current.md` / the two live approach files: L0–L4 fully
  certified; Case 1 of the lower bound (top piece uncut) fully proven with no gap; base case
  n=1 solved both directions; the exact XOR/layer-cake decomposition
  S(whole) = S(Q) + S(C) − 2W is proven exactly (not just an inequality) in both files. What
  remains unproven in both is exactly Sub-claim A2 / G1 (bound W tightly enough) — this
  report's numeric work sharpens what "tightly enough" means (see below) but does not close it.

- **Dead ends (do not retry):** the abstract bound S(whole) ≥ |S(Q) − S(C)| alone (both files
  already flag this as too weak — confirmed here: at the extremal cascade it is *exactly*
  tight, so the bound itself is not the problem, but S(C) alone (just the IH ≥ 1) is not a
  strong enough input — you need the *specific* value of S(C) relative to S(Q), not merely
  S(C) ≥ 1; a proof that only invokes "S(C) ≥ 1 by IH" and stops there cannot work, since IH
  alone is compatible with S(C) being far from 1 (I confirmed S(uncut R) grows like a
  Jacobsthal sequence 1,1,3,5,11,21,... not staying at 1) while the true worst case keeps
  S(whole)=1 regardless. smoothing-extremal's Lemma G (RETHINK) is unrelated to this gap and
  stays dead per round 2's finding.

- **Small-case / intuition notes (numeric, CONJECTURE only, not proof):**
  - Random search (case2.py, 50k trials, n=1,2,3) over Case 2 (≥1 cut forced on top piece,
    arbitrary cuts on rest) finds min S = 1.000 exactly in every case, matching the target —
    strong evidence the answer/bound is correct and Case 2 is genuinely binding (equality, not
    slack).
  - The **explicit cascade** (split top 2^n via repeated halving into
    {2^{n-1}, 2^{n-2}, …, 2^1, 1, 1}, using exactly n cuts, leaving R = {2^0,...,2^{n-1}}
    fully **uncut**) gives S(whole) = 1 EXACTLY for every n = 1..6 (exact rational
    verification, not just numeric search) — this is the concrete extremal certificate the
    outliner/builder should use as the target configuration to reason about.
  - At this cascade: S(Q) and S(C=uncut R) individually are NOT both small; e.g. n=5 gives
    S(Q)=10, S(C)=11 (|diff|=1 exactly); n=6 gives S(Q)=22, S(C)=21. In every tested n,
    |S(Q) − S(C)| = 1 exactly, and the overlap W = min(S(Q), S(C)) exactly (i.e. the smaller
    of the two potentials is *entirely* absorbed into the overlap) — so S(whole) =
    S(Q)+S(C)-2W = |S(Q)-S(C)| = 1 is achieved with FULL overlap, not partial. This says the
    remaining proof obligation is precisely: **W cannot exceed min(S(Q),S(C)) by "less than
    it should" in the other direction** — i.e. one still needs an upper bound W ≤
    (S(Q)+S(C)-1)/2 in general (equivalently a *lower* bound on |S(Q)-S(C)|, or an *upper*
    bound on W beyond the trivial W ≤ min(S(Q),S(C))), which is exactly Sub-claim A2 as
    stated in induction-peel.md, now with a concrete numeric certificate of tightness.
  - A wider random search additionally splitting the "rest" simultaneously with the top
    (case2d.py, 300k trials, n=3,4,5) still finds min ≈ 1.000 and returns near-cascade
    configurations (each level's cut nearly matches the sibling uncut piece one level down) —
    i.e. there is a whole *continuum* of near-ties around the exact cascade, not an isolated
    point, suggesting the correct proof technique should be robust to small perturbations of
    the match, not a rigid case-by-case check of one exact configuration.
