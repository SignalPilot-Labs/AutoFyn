## Goal

Metric: proof-reviewer verdict on a complete rigorous prose proof of IMO-2026-02.
Problem (fixed for whole run): imo-2026-02 (IMO 2026 P2, geometry, hard, rating 8).
Statement: Triangle ABC, M and N midpoints of AB and AC. Points K inside triangle BMC,
L inside triangle BNC, with K inside angle LBA, L inside angle ACK, and
  angle KBA = angle ACL, angle LBK = angle LNC, angle LCK = angle BMK.
O = circumcentre of triangle AKL. Prove OM = ON.
Eval: proof-reviewer APPROVE (Status `solved` in results/imo-2026-02/current.md) with all rigor rules met.
Progress signal each round: results/imo-2026-02/approaches/.ranking.json (Elo, live/dead) + current.md ## Status.
Baseline: no approaches, Status unsolved. Target: solved (APPROVE).
Constraints: prose Markdown proof; no Lean; every step justified; name theorems; cite knowledge_base.md.

## Goal Updates

- [Round 1] Initial user message: solve imo-2026-02. Goal set as above.

## Eval History

- [Round 2] BREAKTHROUGH — **SOLVED**. Status partial -> solved. proof-reviewer APPROVE on complex-reality-conditions.
  Ranking (Elo): complex-reality-conditions 1547.7 (verified-milestone) > trig-decoupled-bash 1522.1 (partial) >
  power-of-point-balance 1514.0 (partial) > antipode-perp-bisector 1416.2 (partial).
  - complex-reality-conditions: round-1 gap (§3 geometry->algebra directed-angle translation of reality conds C1,C2,C3)
    CLOSED rigorously — signed-area inequalities + "reality hinge" (both directed angles in (0,pi) => unsigned equality lifts
    to exact directed equality mod 2pi, kills supplementary branch); midpoint factors 2l-c, 2k-b correct. Then the last
    residual (§6 detA=0 genericity) REPLACED by an exact polynomial ideal-membership certificate on the physical (real) slice:
    W*Im(TN) = f1*Im(E1)+f2*Im(E2)+f3*Im(E3) in Q[c1,c2,k1,k2,l1,l2], W a product of geometric non-degeneracies
    (|B-K|^2,|C-L|^2,Im(K̄L),Im(B̄C)) — Gröbner reduction to exact 0 at power W^1, reviewer independently reproduced.
    No detA, no continuity. Covers EVERY admissible config. Full proof in current.md.
  - antipode-perp-bisector: advanced to partial — Steps 1,2,4 rigorous; sharper crux Lemma B/C (angle A*BK=90-C, A*CL=90-B,
    alpha-independent) numerically certified, not yet proven. Independent synthetic route (never uses (**)).
  - trig-decoupled-bash / power-of-point-balance: HELD (shared-gap plateau; (**) needs unpresentable Gröbner certificate).
  - New certified lemmas: reality-hinge-directed-angle.md, physical-slice-imaginary-certificate.md, antipode-perp-bisector-equivalence.md.
- [Round 1] Baseline: workspace empty, Status unsolved, no approaches ranked.
- [Round 1] IMPROVED. Status unsolved -> partial. 4 approaches opened & ranked (Elo):
  trig-decoupled-bash 1529.0 > power-of-point-balance 1514.5 > complex-reality-conditions 1502.4 > antipode-perp-bisector 1454.2 (held).
  Built 3 (trig-decoupled-bash, complex-reality-conditions, power-of-point-balance) -> all CHANGES REQUESTED (partial).
  - complex-reality-conditions: builder claimed SOLVED; reviewer downgraded to partial. Algebraic core RIGOROUS + sympy-certified
    (A=0 in C; reality conds C1,C2,C3; Cramer + consistency G=0 forces OM=ON; exact identities Rnum=(b-k)(c-l)G, num=qN*G). GAP: the
    geometry->algebra derivation of reality conditions C2,C3 (orientation/signs) is only asserted + numerically checked, not proven.
    This is the CLOSEST approach — one translation lemma from complete.
  - trig-decoupled-bash: exact reduction OM=ON <=> scalar identity (**). GAP: derive (**) from decoupled constraints (I),(II).
  - power-of-point-balance: exact reduction OM=ON <=> (**)/(diamond5), same residual crux. Lemma S proven.
  - 2 lemmas certified: lemmas/circumcenter-of-0-k-l.md, lemmas/product-to-sum-S.md.

## Rules

- ALWAYS run explorers in parallel each given a distinct lens (structure / computation / analogy) (CLAUDE.md, round 1).
- ALWAYS dispatch exactly one proof-builder per slug in the build set, in parallel (CLAUDE.md, round 1).
- ALWAYS run the outline-reviewer every round — no fast-path skip (CLAUDE.md, round 1).
- ALWAYS verify a geometry claim numerically (verify_config.py / sympy) before trusting an angle-chase or algebra step (round 1).
- NEVER split one proof across slugs; each slug is a complete rival attempt at OM=ON (CLAUDE.md, round 1).
- NOTE: numerical verification of an IDENTITY does not prove it; `solved` requires rigorous derivation of BOTH the geometry->algebra
  translation AND the final algebraic closure (reviewer, round 1). A builder claiming `solved` on numeric certification alone gets downgraded.
- WATCH: trig-decoupled-bash and power-of-point-balance share the SAME crux identity (**). Confirmed shared-gap plateau round 2 —
  (**) only closes via a non-human-presentable Gröbner certificate. Do NOT advance either without a genuinely new route.
- NOTE (round 2): to close a complex-number-bash genericity gap (detA=0 / dense-set), prefer an EXACT polynomial ideal-membership
  certificate on the physical (real) slice (multiply target by geometric non-degeneracy denominators, Gröbner-reduce to exact 0)
  over a continuity/connectedness argument — it is unconditional and covers every config at once. Reproduce the reduction to verify.
- ALWAYS re-review any builder `solved` claim adversarially and have the reviewer INDEPENDENTLY reproduce any symbolic certificate
  (not trust the builder's script) — round 1 & first round-2 pass both over-claimed solved (reviewer, round 2).

## State

Done:
- Round 1: setup env (numpy/scipy/sympy), created workspace, set goal, ran full flow.
  4 approaches opened, 3 built, all partial. Status: partial. Two lemmas certified.
- Round 2: 2 explorers (translation lens + shared-crux lens) -> outliner -> outline-reviewer -> 2 builders
  (complex-reality-conditions, antipode-perp-bisector) -> reviewer (both CHANGES REQUESTED) -> re-dispatched complex builder
  to close last §6 genericity gap -> re-reviewed -> **APPROVE / solved**. GOAL ACHIEVED. 3 new lemmas certified.

Broken:
- Nothing blocking the goal. (Secondary: antipode-perp-bisector still partial — Lemma B/C unproven; trig/power on plateau.)

Next:
- Goal achieved (imo-2026-02 SOLVED, reviewer APPROVE, Full proof in current.md). Run complete.
- If continuing: optionally harden the accepted proof (fully human-readable §6.2 certificate write-up) or push antipode as a
  second independent solution for cross-validation. Not required for the goal.
