# Run State — imo-2026-04

## Goal
Produce a complete, rigorous, proof-reviewer-APPROVED proof for problem **imo-2026-04** (Mulan's triangle game).
- Problem type: compute_and_prove, answer_type = characterization.
- Task: Determine (with full proof) exactly which θ ∈ (0°,180°) let Mulan guarantee victory in finitely many steps, no matter how Shan-Yu plays.
- Metric: proof-reviewer verdict on results/imo-2026-04/current.md.
- Eval: dispatch proof-reviewer on the live approach + current.md → Status must be `solved` (APPROVE).
- Baseline (round 1): no approaches exist, Status = unsolved.
- Target: Status = solved, APPROVE, answer stated explicitly and both directions proven (θ works ⇒ Mulan wins; θ fails ⇒ Shan-Yu survives).
- Constraint: prose Markdown proof; every case settled; name theorems; verify the characterization.

NOTE: user explicitly requested imo-2026-04 (difficulty_level=medium), overriding the "hard only" default in CLAUDE.md.

## Goal Updates
- [Round 1] Initial user request: solve imo-2026-04.
- [Round 2] CORRECTED ANSWER. Round-1 conjecture {90°/2^k} and round-2-outline conjecture
  {90°/n} are BOTH WRONG (θ=60° is a rigorous 2-move Mulan win; 90/60∉ℤ). Two independent
  builders (and-or-closure, transcendence) converged on **θ = 180°/m, integer m≥2**
  (equiv: 180/θ ∈ ℤ, θ≤90) with COMPLETE ⊇ constructions + matching exhaustive tests
  (72,80,40,50,70 not winnable). Mechanism: cevian's two P-angles are supplementary (sum
  180°), so 180−θ is a θ-multiple iff 180/θ∈ℤ. Builder B's rival dyadic answer (claims
  72,80 winnable) has an UNPROVEN construction — likely wrong. TARGET is now proving the
  full characterization θ=180°/m. Open crux: ⊆ direction for 0<θ<90, 180/θ∉ℤ (Shan-Yu
  survives, incl. adaptive play). θ>90° impossibility already fully proved.

## Eval History
- Round 3 (BREAKTHROUGH — SOLVED, APPROVE): full cycle (2 explorers -> outliner -> outline-
  reviewer -> 2 builders -> proof-reviewer). The ⊆ survival gap CLOSED. Both explorers +
  outliner + outline-reviewer + reviewer independently converged: the x=c−B "algebraic collapse"
  obstacle was ILLUSORY — the prior rounds carried a strictly stronger invariant (F-free AND
  transcendental); only the extra conjunct dies under collapse. The pure BOOLEAN invariant
  "F-free" (no angle equals any positive integer multiple of θ) is Shan-Yu-maintainable against
  EVERY legal cut via Sub-lemma B's 4-case algebra (no transcendence), then F-free ⟹ ∉ W_k
  (rank induction) ⟹ non-winnable, and an F-free start exists for every θ with 180/θ∉ℤ.
  Reviewer re-derived Sub-lemma B by hand + 201k adversarial exact-arithmetic splits (0 fails,
  incl. collapse & halving cuts). BOTH built slugs APPROVE/solved:
  and-or-closure-rank-induction (fixpoint/AND-OR route) and explicit-ffree-strategy (explicit
  defender route) — two independent architectures. current.md Status=SOLVED with Full proof.
  3 new lemmas certified: sub-lemma-b-ffree-split, ffree-start-exists, ffree-rank-induction.
  FINAL ANSWER: Mulan wins iff θ=180°/m, integer m≥2. GOAL ACHIEVED.
- Round 1 baseline: unsolved, no approaches yet.
- Round 1 (partial, ended early — explorer stuck): 2 explorer reports produced.
  Constructive half essentially proved: Mulan forces θ ∈ {90°/2^k, k≥0}. Conjectured
  answer {90°/2^k} — LATER SHOWN WRONG (round 2).
- Round 2 (BREAKTHROUGH, partial): full cycle ran (survival explorer -> outliner -> 3-way
  outline-reviewer -> 3 builders -> proof-reviewer). CORRECTED ANSWER, reviewer-adjudicated:
  **Mulan wins iff θ = 180°/m, integer m≥2** (180/θ∈ℤ, θ≤90°). PROVEN RIGOROUSLY this round:
  (1) ⊇ construction for all 180/m (universal 90°-fork + peel/supplement chain); (2) θ>90°
  impossibility (device classification Lemma D + W_k induction) — complete, no gap.
  3 lemmas certified: cevian-split-normal-form, construction-180-over-m,
  device-classification-theta-gt-90. Ranking: and-or-closure 1531 (advanced, CHANGES REQ),
  transcendence 1469 (advanced, CHANGES REQ), explicit-potential 1500 (DEAD-END/RETHINK —
  its dyadic answer claiming 72°,80° winnable is FALSE). current.md Status=partial.
  OPEN CRUX (single remaining gap): ⊆ survival for 0<θ<90, 180/θ∉ℤ — Shan-Yu survives vs
  all adaptive play; blocker in both live approaches is the x=c−B "algebraic collapse" state.

## Rules
- ALWAYS give math-explorers a tight, directed scope and forbid deep/open-ended
  brute-force minimax search (timebox any computation to seconds); a round-1 explorer
  idled 905s on depth-2+ search and was force-killed (round 1).
- NEVER let a builder present the pure "always bait exactly θ" strategy as a win: the
  mod-θ invariant makes it insufficient (Shan-Yu picks generic start) (round 1).
- ALWAYS treat the answer as θ=180°/m (m≥2 integer); the cevian's two P-angles are
  supplementary (sum 180°), so the modulus is 180° not 90°. NEVER revert to {90°/2^k} or
  {90°/n} or any dyadic set — all reviewer-refuted (θ=60°,36° win but ∉90/n; 72°,80° lose)
  (round 2).
- ALWAYS have builders re-derive/verify the ⊆ (impossibility) direction independently, not
  just the ⊇ construction: three rounds' answers were wrong because ⊆ ("nothing else wins")
  was never checked until builders ran exhaustive searches (round 2).

## Rules (carried)
- ALWAYS treat the answer as θ=180°/m (m≥2 integer); modulus is 180° (supplementary P-angles),
  NEVER {90°/2^k}/{90°/n}/dyadic — all refuted (round 2).
- SOLVED (round 3): the ⊆ survival direction is closed by the BOOLEAN "F-free" invariant + Sub-
  lemma B 4-case split (no transcendence). If ever reopened, do NOT reintroduce a transcendence-
  degree conjunct — that is exactly the strictly-stronger invariant that the x=c−B collapse kills;
  F-freeness alone survives every legal cut (round 3).

## State
### Done
- Round 3: SOLVED. Closed ⊆ survival gap via F-free boolean invariant. Both slugs APPROVE.
  3 lemmas certified. current.md Status=solved, Full proof written. Answer θ=180°/m.
- Round 1: setup (pip numpy/scipy/sympy), created results/imo-2026-04/ workspace.
  2 explorer lenses (forcing, adversary) reported; no outliner/approaches yet.
- Round 2: full cycle. Corrected answer to θ=180°/m. Proved ⊇ construction + θ>90°
  impossibility rigorously. 3 approaches registered; 2 live (and-or-closure, transcendence),
  1 dead-ended (explicit-potential/dyadic). 3 lemmas certified. current.md Status=partial.
### Broken
- (none)
### Next
- GOAL ACHIEVED — problem SOLVED (both directions + θ>90 all proven/certified, APPROVE).
  No further math work required. Remaining rounds (if any): optionally clean up the two dead/
  lower-ranked approaches' bookkeeping, or verify the assembled Full proof reads end-to-end.
  Do NOT re-open the solved characterization.
