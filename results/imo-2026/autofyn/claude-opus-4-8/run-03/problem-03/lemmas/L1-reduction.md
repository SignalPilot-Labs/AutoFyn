# Lemma L1 — Order irrelevance / reduction to the multiset-refinement game

**Status:** CERTIFIED (proof-reviewer, round 2).

**Statement.** The stick game is equivalent to: LB picks a multiset A of ≤ n+1 positive reals
summing to 1 (his ≤ n cut points partition [0,1] into ≤ n+1 intervals); XY performs ≤ n split
operations, each replacing a current part x by two positive parts summing to x (his ≤ n
interior marks); producing final multiset B. LB's guaranteed value equals the odd-rank sum
Σ_odd(B). Hence c(n) = max_A min_B Σ_odd(B).

**Proof.** LB's ≤ n distinct interior marks cut [0,1] into k ≤ n+1 intervals with length
multiset A, Σ A = 1. Each of XY's ≤ n marks is distinct from all others; a mark interior to a
current interval splits it into two positive parts, and a mark at an existing division point
does nothing (never optimal, and allowing it does not enlarge the achievable multisets). So the
reachable final length-multisets B are exactly the ≤ n-split refinements of A. After all cuts,
the claiming phase runs on the multiset B; by L0 its value to LB is Σ_odd(B), depending only on
B (not positions). Total length is 1, so XY maximizing his own total ⟺ minimizing Σ_odd(B).
LB moves first (chooses A) to maximize; hence c(n) = max_A min_B Σ_odd(B). ∎

Depends on: L0.
