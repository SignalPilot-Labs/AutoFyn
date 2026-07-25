# Build report — induction-peel, round 6 (imo-2026-03)

**Status: partial** (unchanged answer c(n) = 2^n/(2^{n+1}−1)). This round was gate-scoped to two
tasks: retire a refuted line, and falsify-first a proposed new axis. Both executed; no new gap
closed (the falsify-first correctly killed the proposed route).

## 1. UB branch-inequality line — RETIRED / DEAD
Per gate directive, recorded Open gap 2 (top-two-greedy MATCH/BISECT branch inequalities) as dead:
the official IMO-2026 source's explicit n = 5 all-32-branches counterexample confirms F1 — this is
the wrong UB structure and is not salvageable as scoped. UB now belongs to
segment-subset-pigeonhole. The recursion (R), part-count fix, base case, and exact MATCH/BISECT
S-effect formulas remain rigorous/reusable; only the branch inequalities are dead.

## 2. Shard-count induction axis (s_1 = H invariance) — FALSIFIED (falsify-first)
Ran exact-`Fraction` checks, n ≤ 6, budget-respecting (≤ n+1 Q-shards), < 30 s.

- **Invariance claim FALSE.** Slack S(B_low) − (1−e) at s_1 = H is NOT constant: n=3 range [0,2],
  n=4 [0,4], n=5 [0,10], n=6 [0,20]; non-constant even at fixed rest-shard-count. Witness (n=3):
  rest = {3.9, 0.1} gives slack 9/5, vs rest = {2,2} gives 0. The explorer's "constant" reading
  came from three hand-picked r=2 examples.
- **Rigorous diagnosis of why the recurse fails.** The matched-pair cancellation IS real: at
  s_1 = H the Q-shard H and C's top 2^{n-1} = H cancel at adjacent ranks (L4), so
  S(B_low) = S(Q_low' ⊔ P_{n-2}). But (a) this fires only on the measure-zero boundary s_1 = H —
  for the generic interior s_1 < H the two tops (H from C, s_1 from Q) do not cancel; and (b) the
  residual is a valid level-(n−1) copy only when every residual shard ≤ H' = 2^{n-2}; a shard in
  (H', H] exceeds the smaller cap and yields e' = (shard − H')^+ that varies with the split —
  which IS the non-constant slack. The invariance fails for exactly the reason the recursion fails.
- **Verdict:** dead end for (CB). No new (CB) violation found (min slack = 0 throughout — the LB
  claim stays safe, only this route is refuted). Recorded in approach Section 3.5.

## 3. State of the LB wall
Gaps 1'' (Case-B (CB) from Σ s_k ≤ 2^n) and 1''' (k_C ≥ 1 aggregate two-source charging) stand
unchanged. All prior LB machinery (R3, R4, Case-B closed forms, (PM) reduction, L9, R2) intact.

## Spec concerns for the planner
- The layer-cake framing's routes to (CB) are now heavily exhausted: pointwise per-level (round 5),
  majorization/Robin-Hood (round 2 + lbclosure), and now the shard-count/boundary-invariance axis
  (round 6) are all refuted. induction-peel/alternating-sum/interlacing share ONE wall; a fourth
  layer-cake route is unlikely to add value.
- Prioritize segment-subset-pigeonhole (independent tree-extraction LB1 + pigeonhole UB) as the
  live LB and UB route. induction-peel remains the certified-lemma anchor (L0–L14) and LB fallback,
  but its own residual is now walled on all layer-cake-framing sub-routes tried to date.

## Promotable lemmas
None new this round (the tested lead was falsified). Prior promotables (A0, A1, L9, R1–R4, Case-B
closed forms) unchanged.
