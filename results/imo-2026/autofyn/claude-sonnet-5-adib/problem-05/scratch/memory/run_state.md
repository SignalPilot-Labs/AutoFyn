## Goal

Problem: imo-2026-05 (algebra, functional inequality, difficulty_rating 8, hard).
Statement: Let R>0 be positive reals. Determine all f: R>0 -> R>0 such that
sqrt((x^2 + f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x f(y))
for every x,y in R>0.
Task type: compute_and_prove (characterization). Must find all f, prove they work, and prove no others work.

Metric: results/imo-2026-05/current.md `## Status` field (unsolved | partial | solved), gated by proof-reviewer APPROVE.
Eval command: read results/imo-2026-05/current.md and results/imo-2026-05/approaches/.ranking.json
Baseline: unsolved (no workspace existed at round 1 start).
Target: solved — complete, rigorous, reviewer-approved proof characterizing all such f (conjecture: f(x)=x is likely the only solution, but must be proven not assumed).
Constraint: follow CLAUDE.md rigor rules (no hand-waving, name all theorems, cite knowledge_base.md, prove both directions of the characterization).

## Goal Updates

## Eval History

Round 1: Status went unsolved -> solved. BREAKTHROUGH (solved in a single round).
- 3 parallel math-explorers (substitution, monotonicity, equality-case lenses) independently converged: true answer is family f(x)=x+c, c>=0 (not just identity); derived f(f(y))=2f(y)-y via x=f(y) substitution; f(y)>=y; injectivity.
- proof-outliner opened 4 approaches (quadratic-difference-chaining, monotonicity-first, cauchy-boundedness, extremal-supinf), self-derived a new (KEY) two-sided quadratic bound on S(x)=f(x)-x.
- outline-reviewer cut cauchy-boundedness and extremal-supinf (technique mismatch / redundant restatement), approved build set: quadratic-difference-chaining, monotonicity-first. Elo 1516 vs 1484.
- Both proof-builders reached complete solved proofs independently (different intermediate paths, same KEY bound and conclusion).
- proof-reviewer adversarially verified all algebra with sympy, found no gaps, APPROVED both. current.md Status: solved, Full proof recorded, 4 lemmas certified under results/imo-2026-05/lemmas/.

## Rules
- ALWAYS have explorers verify explorer/outliner conjectured answers symbolically (e.g. sympy) before trusting a "likely f=identity"-style guess in run_state — the true answer here was a family f(x)=x+c, not the naive single-function guess (round 1).
- ALWAYS check knowledge_base.md + crux corpus per crux_moves_documentation.md before outlining (round 1 worked well following this).

## State
Done:
- Round 1: Solved imo-2026-05. Answer: f(x) = x + c for constants c >= 0. Full rigorous proof in results/imo-2026-05/current.md, cross-verified by two independent approaches and an adversarial reviewer with sympy recomputation of every algebraic identity.
Broken: none.
Next: N/A — problem solved and approved. Per CLAUDE.md "never re-attempt a solved problem," no further work needed this run.
