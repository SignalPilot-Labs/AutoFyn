# Run State — imo-2026-05

## Goal
**Problem:** imo-2026-05 (IMO 2026 P5, algebra, difficulty 8, hard).
Determine all functions f: R>0 → R>0 such that
  sqrt((x^2 + f(y)^2)/2) >= (f(x) + y)/2 >= sqrt(x·f(y))   for all x,y ∈ R>0.

**Metric:** approach-ranking progress + reviewer Status (unsolved → partial → solved).
**Eval:** proof-reviewer verdict on built approaches; read results/imo-2026-05/current.md `## Status`
  and results/imo-2026-05/approaches/.ranking.json each round.
**Baseline (round 1):** Status = unsolved; no approaches yet; ranking empty.
**Target:** Status = solved — a complete rigorous proof characterizing all f.
  CORRECTED ANSWER (round-1 exploration, symbolic+numeric verified): the solution set is the family
  **f(x) = x + c for every constant c ≥ 0** (NOT just f(x)=x). Proof must show BOTH that every f(x)=x+c, c≥0
  satisfies the two inequalities AND that no other function does.
**Constraints:** prose Markdown proof; every step justified; name theorems w/ knowledge_base.md;
  verify the answer by substitution; commit only results/imo-2026-05/.

## Goal Updates
- [Round 1] Initial task: solve imo-2026-05 (IMO 2026 P5 functional inequality).

## Eval History
- [Round 1] Baseline: Status=unsolved, no approaches, ranking empty.
- [Round 1] Explorers (×3) converged: answer is f(x)=x+c for c≥0 (symbolic SOS + 500k-sample numeric, zero violations).
  Load-bearing move: x=f(y) collapses sandwich to equality -> f(f(y))=2f(y)-y exactly; gives injectivity, f(y)>=y,
  defect d(y)=f(y)-y>=0 orbit-invariant. OPEN GAP: prove d is a GLOBAL constant (across orbits) via cross substitution.
- [Round 1] BREAKTHROUGH — SOLVED. 3 approaches built (orbit-interleaving, convex-duality, monotone-continuity), all
  proof-reviewer APPROVE / Status=solved, independently verified (sympy identities -> 0; numeric checks). Answer
  f(x)=x+c, c>=0 proven both directions. Elo: orbit-interleaving 1546 (leader) > mixed 1515 > monotone 1471 > convex 1467.
  current.md holds full proof (orbit-interleaving). Gap closed via off-diagonal lever (∗) + interleaving at ∞ +
  openness/connectedness of (0,∞). 3 lemmas certified. Goal ACHIEVED.

## Rules
- ALWAYS read results/imo-2026-05/current.md + live approach files + knowledge_base.md before attempting (build on prior progress, round 1).
- ALWAYS keep rival approaches far apart in framing/route, not just technique (same-technique approaches share one wall, round 1).
- NEVER split one proof across slugs — each slug is a complete attempt at the whole claim (single-gap trap, round 1).
- ALWAYS target answer f(x)=x+c, c≥0 (the FULL family), not just f(x)=x — a proof concluding f=id is WRONG/incomplete (round 1, verified).
- NEVER stay within a single f-orbit for the uniqueness step — orbit-internal substitutions can't fix the global defect constant; use cross/general substitution (round 1).

## State
### Done
- Round 1: set up env (numpy/scipy/sympy installed), created results/imo-2026-05/ workspace.
- Round 1: full pipeline (3 explorers → outliner → outline-reviewer → 3 builders → proof-reviewer).
  SOLVED — all 3 built approaches APPROVE. current.md = solved with full proof. Answer f(x)=x+c, c>=0.
  4 approaches registered (orbit-interleaving leader). 3 lemmas certified.
### Broken
- (none)
### Next
- GOAL ACHIEVED. If run continues: optionally harden/cross-check the proof, or polish exposition. No further math needed.
