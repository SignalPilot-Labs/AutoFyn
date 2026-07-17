## Goal

**Problem:** imo-2026-02 (IMO 2026 P2, geometry, difficulty 8/hard).
Statement: Triangle ABC; M, N midpoints of AB, AC. Points K, L inside triangles BMC, BNC
resp., with K inside angle LBA, L inside angle ACK, and ∠KBA=∠ACL, ∠LBK=∠LNC, ∠LCK=∠BMK.
O = circumcentre of AKL. **Prove OM = ON.**

**Metric:** proof-reviewer verdict on the population in results/imo-2026-02/.
**Eval:** dispatch proof-reviewer on each built approach → solved | partial | unsolved,
plus approach ranking in results/imo-2026-02/approaches/.ranking.json.
**Baseline (round 1 start):** unsolved — no approaches yet, no workspace.
**Target:** a complete rigorous proof (proof-reviewer APPROVE, Status=solved, OM=ON proven,
all cases covered, all theorems named/cited).
**Constraints:** prose Markdown proof; no hand-waving; name every theorem; consult
knowledge_base.md. Geometry not in crux corpus — rely on knowledge_base.md + synthetic/
trig/complex/projective toolkit.

## Goal Updates

- [Round 1] Initial task: solve imo-2026-02, prove OM = ON.

## Eval History

- [Round 1 start] Baseline: unsolved, empty population.
- [Round 1 end] Status=partial. 3 approaches built, all CHANGES REQUESTED (real progress,
  gap remains). Elo: power-of-point-BC 1516.7 (leader), trig-lawofsines 1514.6,
  complex-swap-symmetry 1468.7. IMPROVED (empty→3 live approaches + certified shared
  reduction + 3 cached lemmas). No solve yet.
  Shared certified reduction: OM=ON ⟺ pow(M,⊙AKL)=pow(N,⊙AKL) ⟺ pow(B)−pow(C)=(AB²−AC²)/2.
  Ground truth (numeric): K,L a 1-param family; OM=ON identically; O on perp-bisector MN.
- [Round 2 end] **Status=SOLVED. BREAKTHROUGH — GOAL ACHIEVED.** proof-reviewer APPROVE on
  `trig-lawofsines`: complete rigorous proof of OM=ON. Reviewer independently rebuilt
  P(t),Q(s),TN(t,s) in sympy, reran the pseudo-division (lc(P)·TN=q1·P+R1,
  lc(Q)·R1=q2·Q+R2, both remainders deg 3), and Gröbner-reduced R2 mod the 3 Pythagorean
  relations to EXACTLY 0 → lc(P)·lc(Q)·TN=f·P+g·Q is a genuine polynomial identity; lc's
  nonzero on the physical range; OM²−ON²=(T-diff)/(4D) exact ⇒ (T)⟺OM=ON. No gap, no
  circularity, no missing case. Round-1 "spurious γ↦γ+π branch" DISSOLVED: it was an
  artifact of the doubled-angle (cos2γ,sin2γ) coordinates; single-angle Weierstrass
  t=tan(γ/2) is single-valued ⇒ certificate valid on all branches, no branch-selection
  needed. Two lemmas certified (closing-relations, T-reduction-and-certificate).
  Other approaches (stay live, honest partials, CHANGES REQUESTED): power-of-point-BC
  (E2′,E3′ now certified; gaps G3 scalar id + Lemma O ordering + one G2 betweenness);
  inversion-at-A (new, exact circle→line reformulation proven but shown tautological;
  E2/E3 coupling identity open). Elo: power-of-point-BC 1559.6, trig-lawofsines 1527.5
  (verified-milestone), inversion-at-A 1486.0, complex-swap-symmetry 1427.0.

## Rules

- ALWAYS: for this problem, "verified numerically / to N digits" is NOT a proof — the
  proof-reviewer requires an algebraic/synthetic derivation (round 1).
- NEVER on the trig/complex routes: rely on plain Gröbner ideal-membership to close the
  final identity — the reality/orientation constraints make the variety reducible and
  membership gives a FALSE NEGATIVE (spurious γ↦γ+π branch). Must substitute the physical
  closed-form branch / saturate to the geometric component (because both CAS routes hit
  this exact wall, round 1).
- ALWAYS: the orientation & containment constraints (K inside ∠LBA, L inside ∠ACK) are
  load-bearing — magnitude-only solvers land on spurious branches where OM≠ON (round 1).
- NEVER add a 4th CAS-bash approach next round — trig + complex already share the CAS
  elimination wall; keep the synthetic power-of-point route as the diversity anchor
  (outline-reviewer flag, round 1).
- ALWAYS use single-angle Weierstrass t=tan(x/2) (single-valued) over doubled-angle
  (cos2x,sin2x) coordinates when closing a trig identity by elimination — the doubling is
  a 2-to-1 lossy map that manufactures a spurious x↦x+π branch and a Gröbner false
  negative; single-angle dissolves it and needs no branch-selection (this was THE unlock
  that solved imo-2026-02, round 2).

## State

**Done:**
- Round 1: setup (numpy/scipy/sympy installed), workspace created. 3 far-apart approaches
  built, all partial; shared reduction + 3 lemmas certified.
- Round 2: **SOLVED.** 2 explorers (synthetic-closure, different-framing) → outliner
  advanced 2 + opened inversion-at-A → outline-reviewer ranked & emitted build set
  {power-of-point-BC, trig-lawofsines, inversion-at-A} → 3 builders → reviewer. Winning
  move: single-angle Weierstrass t=tan(γ/2) on the UN-doubled E2′,E3′ gave an exact
  pseudo-division certificate for (T), independently re-verified by the reviewer.
  current.md Status=solved, Full proof written.

**Broken (open gaps — non-blocking; problem is solved via trig-lawofsines):**
- power-of-point-BC: G3 scalar identity, Lemma O ordering, one G2 betweenness step.
- inversion-at-A: E2/E3 coupling scalar identity (reformulation proven but tautological).
- complex-swap-symmetry: dormant (shares CAS wall; subsumed by trig Weierstrass fix).

**Next:** GOAL MET — imo-2026-02 SOLVED (proof-reviewer APPROVE, Status=solved). Do NOT
re-attempt (CLAUDE.md: never re-attempt a solved problem). Remaining rounds optional:
could polish/harden the solved proof or bring power-of-point-BC to a second independent
solve for cross-validation, but the target is already achieved. Prefer end_session once
time-lock permits.
