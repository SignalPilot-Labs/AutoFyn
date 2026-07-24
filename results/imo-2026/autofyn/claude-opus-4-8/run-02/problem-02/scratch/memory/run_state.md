# Run State — imo-2026-02

## Goal
Produce a complete, rigorous prose proof of IMO 2026 Problem 2 (id `imo-2026-02`).

Statement: Let ABC be a triangle; M, N midpoints of AB, AC. Points K, L chosen inside triangles BMC and BNC such that K lies inside angle LBA, L lies inside angle ACK, and ∠KBA = ∠ACL, ∠LBK = ∠LNC, ∠LCK = ∠BMK. Let O be the circumcentre of triangle AKL. Prove that OM = ON.

Domain: geometry. Task: proof_only. answer_type: none.

Metric: proof-reviewer verdict on best approach in results/imo-2026-02/.
Eval: proof-reviewer reads results/imo-2026-02/approaches/<slug>.md + current.md → solved/partial/unsolved.
Baseline (round 1 start): no approaches, Status=unsolved.
Target: Status=solved (proof-reviewer APPROVE), complete & rigorous.
Constraint: no hand-waving, every case settled, all tools named per rigor rules in CLAUDE.md.

## Goal Updates
- [2026-07-24] Initial task: solve imo-2026-02 (fixed problem for whole run).

## Eval History
- Round 1 start: unsolved, empty approach population.
- Round 1 end: SOLVED (BREAKTHROUGH). proof-reviewer APPROVE on `trig-metric-identity`. current.md Status=solved with full proof.
  - Ranking: trig-metric-identity = leader (solved, verified-milestone recorded). equal-power-secants & spiral-involution = partial/RETHINK (distinctive engines refuted, but reusable lemmas certified).
  - Winning route: metric/coordinate. OM=ON ⇔ O_x=(2p+a)/4; family by s=tan(θ/2); conditions 2,3 decouple into E2=t_K·H(t_L), E3=t_L·G(t_K); target poly T ∈ ideal⟨G,H⟩ via EXACT symbolic cofactor identity f·T=Q_G·G+Q_H·H (sympy exact zero, verify.py); positivity f=(1+s²)·AB·AC·sin(∠A+θ)>0 from θ=∠KBA<∠ABC (K∈△BMC) & ∠A+∠ABC<π closes G=H=0⟹T=0.
  - Certified lemmas: goal-reduction, branch-orientation, sigma-and-supplementary, leading-content-positive.

## Rules
- ALWAYS attack the whole claim (OM=ON) end to end per slug; never split one proof across slugs (round 1, CLAUDE.md single-gap trap).
- ALWAYS keep rival approaches far apart in framing/route, not just technique (round 1, CLAUDE.md).
- NEVER build on numerically-FALSE facts for this problem: AK=AL, spiral similarity centered at A, five-point concyclicity {A,K,L,B,C}, tangency BK⊥circle(AKL) — all refuted round 1.
- ALWAYS certify sympy proofs only as EXACT symbolic zeros (simplify/expand→0), never numeric sweeps; and check cofactor/ideal-membership arguments for 0·∞ denominator holes (because that was the last gap in the winning proof, round 1).

## State
### Done
- Round 1: env setup (numpy/scipy/sympy), created results/imo-2026-02/ workspace.
- Round 1: 3 explorers → outliner (3 rival slugs) → outline-reviewer (all built) → 3 builders → reviewer. SOLVED via trig-metric-identity (APPROVE). current.md Status=solved with full self-contained proof; 4 lemmas certified; verify.py exact-zero verification saved.
### Broken
- (none) — equal-power-secants & spiral-involution distinctive engines refuted, but that's expected exploratory loss; their L1/L2 lemmas are certified and reusable.
### Next
- GOAL ACHIEVED. If run continues: optionally seek a second independent (synthetic) proof for robustness, or polish/verify the winning proof's prose exposition. Otherwise nothing required — problem solved.
