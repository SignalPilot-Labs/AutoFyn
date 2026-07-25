# Run State — imo-2026-02

## Goal
Produce a complete, rigorous prose proof of IMO 2026 Problem 2 (geometry).
Statement: Let ABC be a triangle, M, N midpoints of AB, AC. Points K inside triangle BMC and L inside triangle BNC chosen so that K lies inside angle LBA, L inside angle ACK, and ∠KBA=∠ACL, ∠LBK=∠LNC, ∠LCK=∠BMK. O = circumcentre of AKL. Prove OM = ON.
Metric: proof-reviewer verdict on results/imo-2026-02/current.md.
Eval: proof-reviewer adversarial check. Baseline: no workspace, Status=unsolved. Target: Status=solved (APPROVE).
Constraint: full rigor per CLAUDE.md rigor rules; prose Markdown, no Lean.

## Goal Updates

## Eval History
- Round 0 (baseline): no workspace. Status=unsolved. No approaches.
- Round 1: Status=partial (BREAKTHROUGH). 4 approaches registered, 3 built, all CHANGES REQUESTED. Elo: pow-reduction-trig 1546 > coordinate-identity 1515 > synthetic-sigma-spiral 1485 > midpoint-doubling-phantom 1454 (unbuilt). Certified lemmas: reduction-OMeqON (OM=ON ⟺ pow(M,⊙AKL)=pow(N,⊙AKL) ⟺ T=0), spiral-similarity-rho. **coordinate-identity is ONE bounded step from solved**: exact ideal identity a_K·a_L·T=a_L·QK·FK+QL·FL verified (pseudo-div remainder 0, reviewer reran /tmp/clean.py); only gap = prove orientation ε=+1 (unsigned angle hyps ⟹ directed FK=FL=0) from the interiority/betweenness hypotheses. Reviewer showed gap is genuinely load-bearing (θ=0.8 counterexample where unsigned holds but OM≠ON).
- Round 2: **Status=solved (BREAKTHROUGH — GOAL ACHIEVED).** coordinate-identity APPROVE — the round-1 orientation gap CLOSED rigorously. Orientation Lemma proved from interiority alone (Lemma I interior⟹positive barycentric; Lemma B betweenness sign; Fact 0 midpoint-halving; 4 target signs (−,−,+,+); Condition-B pair derived directly at C,M, NOT via sign-reversing σ; unsigned→directed upgrade via same-sign+equal-magnitude-in-(0,π)) — NO numerics, NO continuity. Reviewer re-derived every step by hand + independent sympy ideal-identity check + 11,739 admissible configs (OM=ON to 1.9e-14; a_K·a_L=0 set empty, min|W|=0.25). New certified lemma orientation-sign.md (coordinate-free, importable). pow-reduction-trig CHANGES REQUESTED (Lemmas 4-5 now exact/symbolic; GAP-2′ explicit cofactors f,g still open — honest partial insurance). Elo: coordinate-identity 1558 > pow-reduction-trig 1553 > synthetic-sigma-spiral 1472 > midpoint-doubling-phantom 1416.

## Rules
- ALWAYS run every round: math-explorer×(1-3) → proof-outliner → outline-reviewer → proof-builder×N → proof-reviewer (round 1, CLAUDE.md).
- ALWAYS keep rival approaches far apart in framing (synthetic / trig / complex-coord / projective), not one idea many ways (round 1, CLAUDE.md single-gap trap).
- ALWAYS convert unsigned angle-equality hypotheses to DIRECTED equalities via the interiority/betweenness constraints, and PROVE the orientation sign — never assert it or justify by numerics (round 1: this exact overclaim made coordinate-identity's "solved" invalid; shared wall for 2 of 3 approaches).
- NEVER mark Status=solved on a numeric-only verification of a load-bearing step; an exact symbolic certificate for the algebra does NOT cover the geometric orientation step (round 1).
- ALWAYS upgrade an unsigned angle equality to a directed one via: same-sign cross products (from interior⟹positive-barycentric + betweenness-sign lemmas) + equal unsigned magnitude in (0,π) ⟹ literal directed equality; derive each vertex's sign directly, NEVER transport through a reflection like σ that flips orientation (this closed the imo-2026-02 orientation gap, round 2).

## State
### Done
- Round 1: setup; explored 3 routes; opened 4-approach field; built + reviewed 3. Established 1-param family (free β), OM=ON holds throughout. Reduction certified. coordinate-identity algebraic engine fully verified.
- Round 2: **SOLVED.** Explored orientation gap (2 routes, both converged on interiority ⟹ directed signs). Outliner revised coordinate-identity with explicit Orientation Lemma; reviewer verified route is not numerics-in-disguise. Builder proved it from interiority alone; proof-reviewer APPROVE with independent hand re-derivation. current.md Status=solved, Full proof recorded. orientation-sign.md certified.
### Broken
- pow-reduction-trig (partial, insurance — NOT needed for goal): GAP-2′ explicit bilinear-form cofactors f,g open; Lemmas 4-5 now exact/symbolic.
- synthetic-sigma-spiral (partial): crux c·MX=b·NY open; concyclicities could now import orientation-sign.md to kill numeric sign bullets (untouched round 2).
### Next
- GOAL ACHIEVED (imo-2026-02 solved, APPROVE). If run continues: could harden by a second independent full solve — finish pow-reduction-trig GAP-2′ (extract cofactors f,g symbolically) OR complete synthetic-sigma-spiral importing certified orientation-sign.md. Neither required; primary objective met.
