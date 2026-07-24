## Goal

Solve IMO-2026-02 (geometry, difficulty 8, hard), a triangle/circumcenter proof problem.

Statement: Let ABC be a triangle, M and N midpoints of AB and AC. Points K, L inside triangles BMC, BNC resp., such that K lies inside angle LBA, L lies inside angle ACK, and ∠KBA = ∠ACL, ∠LBK = ∠LNC, ∠LCK = ∠BMK. Let O be the circumcentre of triangle AKL. Prove that OM = ON.

Metric: `results/imo-2026-02/current.md` `## Status` field, gated by proof-reviewer APPROVE verdict (solved | partial | unsolved).
Eval: read `results/imo-2026-02/current.md` Status + `results/imo-2026-02/approaches/.ranking.json` each round.
Baseline (round 1, pre-work): unsolved, no approaches yet.
Target: solved — complete rigorous proof with no gaps, verified by proof-reviewer APPROVE.
Constraint: prose Markdown proof (no Lean), must satisfy all Rigor rules in CLAUDE.md (no hand-waving, name every theorem, no skipped cases).

**STATUS: GOAL ACHIEVED — round 2. `results/imo-2026-02/current.md` Status = solved, APPROVE verdict from proof-reviewer (final adversarial pass, round 2). No further work needed unless a future round's re-check finds a flaw.**

## Goal Updates

(none — no user messages changed scope)

## Eval History

- Round 1: Status unsolved -> partial. Shared Lemma 0 established and certified: OM=ON ⟺ (O−N9)·(C−B)=0, via nine-point center N9. Field of 5 approaches opened; build set of 3 built and reviewed:
  - complex-number-argument-bash: CHANGES REQUESTED (partial). Leading approach — Dictionary Lemma, L-elimination, cubic locus X for K established and independently verified. Open gaps: final polynomial identity closure + orientation/sign-matching check.
  - nine-point-locus-two-position: RETHINK -> dead-end. "O affine under reparametrization" mechanism numerically refuted. Byproduct: certified o-free-circumcenter-reformulation lemma.
  - spiral-similarity-radical-axis: RETHINK -> dead-end. No concyclic 4-point subset of {A,B,C,M,N,K,L,O} found (70 subsets scanned, 3 triangles).
- Round 2: Status partial -> **solved** (APPROVE). 2 explorers (algebraic-closure lens, fresh-framing lens) -> outliner revised 2 approaches -> outline-reviewer (build set: complex-number-argument-bash, symmetric-vector-decomposition-sigma) -> 2 parallel builders -> reviewer (CHANGES REQUESTED / RETHINK) -> one more targeted builder pass closed the last gap in the leader -> final adversarial proof-reviewer pass -> **APPROVE**.
  - complex-number-argument-bash: closed the final polynomial-identity gap (exact sympy-verified identity `Fn_num_raw·D2 − (k2−q)·eq2_num = D·X·(E1·l1+E0)`, independently reproduced twice — once by outline-reviewer with a different exact formula than the round-2 explorer's non-reproducing claim, once by the final proof-reviewer from scratch). Then closed the orientation/sign-matching gap via a new "Master Fact" cone-sign toolkit translating the 4 containment hypotheses (K∈△BMC, L∈△BNC, K∈∠LBA, L∈∠ACK) into definite-sign cross-product facts, proved non-circular and load-bearing. Also gave a fully elementary D≠0/D2≠0 genericity argument (replacing an earlier Bezout/continuity approach). Final proof-reviewer independently re-derived EVERY step from raw hypotheses (not builder's formulas) and found zero gaps. Status: solved.
  - symmetric-vector-decomposition-sigma: RETHINK -> dead-end (confirmed, not just claimed). The naive σ-antisymmetry mechanism (B↔C,K↔L,M↔N swap negates target) is a content-free tautology true for ALL points regardless of hypotheses — proven by both builder and reviewer independently in sympy with free coordinates. Certified as a reusable negative-result lemma (`sigma-invariance-and-vacuity.md`) so no future approach retries this exact mechanism.

## Rules

- ALWAYS reuse certified shared lemmas in `results/imo-2026-02/lemmas/` instead of re-deriving: nine-point-center-reduction, dictionary-lemma-equal-signed-angle, o-free-circumcenter-reformulation, cubic-locus-for-K, closing-polynomial-identity-step4, sigma-invariance-and-vacuity.
- NEVER retry spiral similarity centered at A for K,L (ABK~ACL) or for condition (i) specifically — numerically refuted twice independently, round 1 and round 2.
- NEVER retry the "O(θ) affine under reparametrization / two-special-positions" architecture (analogy to aimo-1007/SL2023G5) — numerically refuted across ~15 parametrizations, round 1.
- NEVER look for a concyclic quadruple among {A,B,C,M,N,K,L,O} as a proof route — exhaustively scanned (70 subsets, 3 triangles), all non-concyclic, round 1.
- NEVER retry the naive σ-antisymmetry mechanism (swap B↔C,K↔L,M↔N, claim target negates hence vanishes) — proven to be a content-free tautology true for all points, independent of hypotheses, round 2. A valid σ-based proof (if one exists) needs a genuinely second, non-tautological relation, not mere relabeling.
- ALWAYS independently re-derive claimed polynomial-identity closures from scratch with sympy before trusting them — round 2 saw a claimed "cofactor identity" from an explorer that did NOT reproduce under the outline-reviewer's independent check (though the underlying mathematical claim was true, the specific formula was wrong); use exact `sympy.expand(LHS-RHS)==0`, not just high-precision numerics, and don't chain off an unverified predecessor's formula.
- ALWAYS check for circularity in orientation/sign arguments derived from containment hypotheses that involve the solution points themselves (K, L) — verify sign facts derive purely from the geometric hypotheses on a fixed valid (K,L), never from the very equations (eq1=eq2=eq3=0) being justified.
- Crux corpus has zero geometry-domain entries — for geometry problems, search `past_problems_database.json` directly by keyword instead of filtering by domain=geometry (round 1 finding).

## State

### Done
- Round 1: setup, 3 explorers, outliner (5 approaches), outline-reviewer (build set 3), 3 builders, reviewer. Status -> partial. Leader identified with 2 open gaps.
- Round 2: 2 explorers (closed/de-risked both open gaps numerically) -> outliner (revised 2 approaches with new findings) -> outline-reviewer (build set: complex-number-argument-bash, symmetric-vector-decomposition-sigma; independently caught a wrong "cofactor identity" claim) -> 2 parallel builders (leader made real progress but claimed formula also didn't independently reproduce cleanly; sigma approach found genuine dead end) -> reviewer (CHANGES REQUESTED on leader, RETHINK on sigma) -> targeted second builder pass on leader closed the orientation gap -> final adversarial proof-reviewer pass -> **APPROVE, Status: solved**.

### Broken
(none)

### Next
- Goal achieved. If a future round is dispatched on this run, the correct action is: re-verify `results/imo-2026-02/current.md` is still Status solved and matches the approach file; if a user message reopens the problem or points out a flaw, dispatch a fresh proof-reviewer to re-adjudicate before any rebuild. Otherwise no further routine work is needed — consider ending the session on the next opportunity (`end_session`) once the harness allows it (time-locked).
