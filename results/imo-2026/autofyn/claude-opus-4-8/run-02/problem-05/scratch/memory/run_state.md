# Run State — imo-2026-05

## Goal
**Problem:** IMO 2026 P5 (`imo-2026-05`), algebra, hard (difficulty 8).
Determine all functions f: R_>0 -> R_>0 such that
  sqrt((x^2 + f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x*f(y))   for all x,y > 0.

**Metric:** proof-reviewer verdict + approach ranking (Elo, live vs dead-ended, gaps closing).
**Eval:** proof-reviewer judges each built approach; read results/imo-2026-05/approaches/.ranking.json and results/imo-2026-05/current.md ## Status.
**Baseline (round 1 start):** no approaches, Status = unsolved.
**Target:** Status = solved — a complete, rigorous prose proof characterizing ALL such f (both the derivation of the answer AND verification the claimed family exactly satisfies the constraints), reviewer APPROVE.
**Constraint:** full rigor per CLAUDE.md rigor rules; must state answer explicitly and verify by substitution.

## Goal Updates
- [2026-07-24] Initial task: solve imo-2026-05.

## Eval History
- Round 1 (start): baseline — Status unsolved, 0 approaches.
- Round 1 (end): BREAKTHROUGH — Status = SOLVED. proof-reviewer APPROVE on `orbit-distance` (independently sympy-verified every load-bearing step). Answer: f(x) = x + c for c >= 0. Ranking: orbit-distance (solved, top) > bound-pinch (partial, elo 1500) > monotone-gap (1469, unbuilt). 3 lemmas certified (fe-collapse, ap-orbit, master-reformulation). bound-pinch remains partial (constancy crux reduces to same bounded-distance comparison).

## Rules
- ALWAYS: this is a "find all functions" problem — a solved proof needs BOTH the characterization argument AND verification the claimed family satisfies the constraints (round 1).

## State
### Done
- Round 1: setup + workspace + sci packages. 3 explorers (substitution/squeeze/bounding) converged: answer is FAMILY f(x)=x+c, c>=0 (NOT just f=x); key sub x=f(y) forces FE f(f(y))=2f(y)-y. Outliner opened 3 far-apart approaches; outline-reviewer built {orbit-distance, bound-pinch}. **orbit-distance SOLVED & APPROVED** — global-constant gap closed via bounded-distance two-orbit comparison (residual 4x_k(alpha-beta)+(alpha-d_k)^2 forces alpha=beta). current.md = solved with full proof. GOAL ACHIEVED.

### Broken
- (none)

### Next
- Goal achieved. If run continues: could harden/simplify orbit-distance write-up, or complete bound-pinch as a second independent full proof (its constancy crux still open). No blocking work.
