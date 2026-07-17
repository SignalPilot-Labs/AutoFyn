# proof-builder — direct-constructive (imo-2026-03), round 2

## Status: partial

## Closed (fully rigorous)
- **G1 (greedy = odd-ranked)** — complete. Alternating-sum recursion V(q)=max_j[q_j−V(q∖q_j)]
  with the telescoping identity f(j)−f(j+1)=(q_j−q_{j+1})(1+(−1)^{j+1})≥0 proving greedy
  optimal and V=A(q). LB's take = Σ odd-ranked pieces. Promotable.
- **R1/R2 odd-sum rewritings** — complete. O=∫⌈N(t)/2⌉dt and O=1/2+½·μ{N(t) odd}. Turns
  both bounds into measure statements: O≥c(n) ⟺ μ{N odd}≥1/D. Numerically verified. Promotable.
- **Construction + dominance identity** — complete. LB marks (2^k−1)/D → pieces 2^j/D;
  P_j−Σ_{i<j}P_i=1/D.
- **Lower bound easy case** — complete. XY spares R_n ⇒ r_1=2^n/D ⇒ O≥2^n/D.
- **Interleaving Lemma I** — complete (in its regime b>Σrest and residual s_p≤a_p): owner
  of b forces odd-claimer to get exactly b.
- **Base cases** — n=1 both bounds fully (XY rule: halve largest if >2/3 else pass);
  n=2 lower confined + construction.

## Open gaps (block `solved`)
- **L1** (the load-bearing lower-bound gap): confined-case "Fragments Lemma" E≤2^n−1 for
  general n. Reduced to the exact identity (‡) E−ΣI=∫⌊(N_F−N_I)/2⌋dt and need this ≤0.
  Numerics: equality at interleaving optimum for all n≤5. NOTE a per-rank bound r_{2j}≤2^{n−j}
  is FALSE (n=3 counterexample {3,2.5,2.5}), so (†) must be a sum inequality.
  KEY NUMERIC FACT I established: with UNLIMITED fragments the bound FAILS (n=2 drops to 3.53);
  it holds only because ≤ n cuts ⇒ ≤ n+1 fragments. So the cut-budget is essential and any
  proof of L1 must use fragment-count ≤ n+1, not just ΣF=2^n.
- **L2**: reduction "XY's optimum confines all cuts to R_n" (exchange argument). Numerics
  strongly support (n=2 minimiser puts both cuts in R_n).
- **U1** (was G3, reviewer's flagged load-bearing gap): general interleave+halve mark-budget
  accounting giving O≤2^n/D for all LB markings/all n. Both mechanisms proved (Lemma I;
  midpoint halving); missing is the budget bookkeeping + the a_1≤1/2 regime.

## Recommendation for next round
- L1 is the cleanest remaining target: it is now a purely 1-D integral inequality
  ∫⌊(N_F−N_I)/2⌋dt≤0 with N_I an explicit power-of-2 staircase and ≤n+1 fragments summing to
  2^n. Attack it via the parity/measure form or a Hall-type transversal on even ranks.
- U1 remains the field-wide wall the outline-reviewer flagged. Worth an explorer on a
  genuinely different framing of the XY upper bound (adaptive adversary / potential on XY's
  spare marks), per the diversity note.
