## Goal

Solve IMO 2026 P5 (imo-2026-05), a hard algebra functional-inequality problem.
- Metric: proof-reviewer verdict on the population of approaches in results/imo-2026-05/.
- Eval: read results/imo-2026-05/current.md `## Status` + approaches/.ranking.json each round.
- Baseline (round 1): no approaches, Status unsolved, empty population.
- Target: Status `solved` — a complete rigorous proof that characterizes ALL f: R>0→R>0 with
  sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x*f(y)) for all x,y>0.
- Constraints (rigor rules from CLAUDE.md): prove both directions — the characterization holds
  (all listed f satisfy it) AND is exhaustive (no others). State answer explicitly and verify.

Problem statement:
Let R_{>0} be positive reals. Determine all f: R_{>0}->R_{>0} such that
sqrt((x^2 + f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x f(y)) for every x,y in R_{>0}.
(Likely answer: f(x)=x, to be proven.)

## Goal Updates

## Eval History
- Round 1 baseline: empty population, Status unsolved.
- Round 1 explore: 3 explorers CONVERGE. Candidate answer CORRECTED from f(x)=x to the
  FAMILY f(x)=x+c for every constant c>=0 (both inequalities reduce to SOS identity
  ((x-y)-c)^2>=0; verified algebraically + numerically). Established (rigorously per explorers):
  identity f(f(y))=2f(y)-y (from x=f(y) forcing both bounds tight), injectivity, and f(y)>=y.
  OPEN GAP = exhaustiveness: show d(y)=f(y)-y is a single GLOBAL constant. Same-orbit subs
  are vacuous; the constraint lives in cross-orbit subs into the LEFT (QM) inequality.
  Crux analogs: aimo-0008, aimo-0710 (telescoping-orbit-gap template).

## Rules
- ALWAYS verify the candidate answer's easy direction as an SOS identity before assuming it (round 1: caught that the answer is the FAMILY f(x)=x+c, c>=0, not just f(x)=x — both defects = ((x-y)-c)^2).
- ALWAYS route the residual {0,b} exhaustiveness sub-case through openness of the fixed-point set F and shift-set G plus connectedness of (0,inf) (round 1: this closed all three endgames).

## State
### Done
- Round 1: SOLVED. imo-2026-05 fully characterized: f(x)=x+c for every constant c>=0, nothing else.
  Three independent complete proofs, all APPROVE by proof-reviewer:
  * orbit-crossing (elo 1546, strongest): cross-orbit marching kills two positive d-values; F-openness+boundary limit closes {0,b}.
  * shift-family-sos (elo 1502): quadratic-form failure-band squeeze forces F,G both open.
  * monotonicity-orbits (elo 1499): level-set order rigidity; |p-q|>=b separation forces F,G open.
  Shared core: identity f(f(y))=2f(y)-y (x=f(y) makes both bounds tight), injectivity, f(y)>=y, orbit-AP.
  current.md Status=solved with consolidated Full proof; 4 lemmas certified into lemmas/.
### Broken
- (none)
### Next
- Goal achieved. Optional future rounds: consolidate/harden the single canonical proof, or stress-test the
  {0,b} endgame topology once more. No open gaps remain.
### Eval note
- Round 1 = BREAKTHROUGH: empty population -> solved in one round, three independent verified proofs.
