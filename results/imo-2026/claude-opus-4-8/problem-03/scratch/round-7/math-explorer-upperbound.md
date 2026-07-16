## imo-2026-03 (upper-bound residual gap case)

**Lens**: geometric-selfsimilar route — the gap case (distinct X, p1 < τ, p2 < τ/2)

---

### Distinct openings

**Opening 1 — The "gap + R3" two-level induction (most promising)**

Computational finding: for EVERY gap-case config tested (222 cases, denom 60, n=3), the "best-pairing" strategy (try all possible j: cut p1 at p_j, creating pair {p_j, p_j} invisible) achieves mu <= Sigma/D_b (0 failures). This is a DIFFERENT strategy from partial-shadow; it pairs p1 with one of its SMALLER siblings, not with a greedy prefix.

Key observation from tracing the n=3 tight example X=(7/15, 7/30, 1/6, 2/15): the optimal XY strategy is a 3-step R3 chain — cut 7/15 at 7/30, leaving leftover 7/30; now Sigma'=8/15, and p3=1/6 satisfies new R3 condition (1/6 >= new tau'/2 = 22/105); then cut 7/30 at 1/6 leaving 1/10; then R3 again with leftover 1/15. Final A = 1/15 = target (tight at boundary).

The algebraic mechanism: pairing p1 at p2 (even though p2 < tau/2, so this is NOT a valid R3 move) reduces Sigma to Sigma' = Sigma - 2*p2. Because Sigma decreases, the new threshold tau' = Sigma' * 2^{b-1}/D_{b-1} decreases, and the UNCHANGED piece p3 may now satisfy new tau'/2 — enabling a VALID R3 at the next step. Verified: in 25 out of 28 denom-30 gap cases, after pairing at p2, the next step has R3 or R1 applicable. The remaining 3 cases require two gap steps before R3 fires.

The PROOF STRATEGY: Show that for any gap case (X, b), there exists a pairing j such that the reduced instance (X', b-1) is handled by R1/R2/R3 or by a gap instance with b-1. Since b decreases strictly and the final value is bounded by the analysis below, this terminates correctly. The SB invariant CANNOT be maintained step-by-step (see dead-end below); the proof must use a two-level structure.

**Opening 2 — Direct algebraic bound using the "subtract all" chain (Case A.A closure)**

For the specific subcase where p1 - p2 > p3 AND p1-p2-p3 > p4 ("Case A.A"): XY pairs p1 with p2 (step 1), leftover p1-p2 with p3 (step 2), leftover p1-p2-p3 with p4 (step 3). Final A = (p1-p2-p3)-p4 = p1-(p2+p3+p4) = p1-(1-p1) = 2p1-1. For p1 < tau = Sigma*2^b/D_b: 2p1-1 < 2*tau-1. At n=3: 2*(8/15)-1 = 1/15 = target. More generally: 2*tau-1 = 2*Sigma*2^b/D_b - 1. For Sigma=1: 2*2^b/D_b - 1 = (2^{b+1}-D_b)/D_b = (2^{b+1}-(2^{b+1}-1))/D_b = 1/D_b = target. So in Case A.A: A = 2p1-1 < 2*tau-1 = 1/D_b = target (STRICT since p1 < tau strictly). PROVED for Case A.A, no induction needed.

This handles the "dominant LB piece" part of the gap case where p1 > p2+p3. The gap case condition ensures p1 < tau, yielding the strict bound.

**Opening 3 — Generalizing the n=2 B2 explicit strategy**

The n=2 B2 proof uses a SPECIFIC two-cut move (cut p1 at epsilon=(p1-p2)/2, cut p3 in half) giving val = p1 + p3/2 <= (3p1+1)/4 <= c(2). This works because the explicit cuts create pairs {epsilon, epsilon} and {p3/2, p3/2} which are parity-invisible, and val reduces exactly.

For general n in the gap case (which corresponds to B2 for top-level configs), the outliner should attempt to GENERALIZE this move: find a combination of (k-1) cuts creating parity-invisible pairs from non-top pieces, plus (b-k+1) cuts to handle the residual. The gap condition p2 < tau/2 provides extra "room" not present in B1 — the second piece is SMALL enough that many different cut combinations can reduce A.

The key n=2 formula val = p1 + p3/2 generalizes: for m=4 pieces with 3 cuts, investigate val = p1 + p3/2 + p4/2 or p1 + (p3+p4)/2 depending on the pairing pattern. The B2 condition p1 < 1-c(n) = tau - tau/(tau+1) approximately gives val < c(n) when the right pairs are made.

**Opening 4 — Gap case is STRICTLY bounded (not tight inside)**

CRITICAL FINDING: The tight bound mu = Sigma/D_b in the gap case is only attained at the BOUNDARY (p1 = tau, handled by R2; or p2 = tau/2, handled by R3), NOT strictly inside the gap. In the strict interior of the gap case (p1 < tau strictly AND p2 < tau/2 strictly), mu < Sigma/D_b (STRICT). Verified over all 222 denom-60 gap cases: the max mu achieves 1/15 only when p1=8/15=tau (boundary case excluded from strict gap).

Implication: the outliner could try a COMPACTNESS/CONTINUITY ARGUMENT. V is continuous (certified), the strict gap case is an open set, and its closure intersects only with R2/R3 territory. However, this alone does not give a constructive proof.

---

### Candidate technique(s)

- **Double gap-step + R3 induction**: two-level induction where one "non-R3" pairing step reduces the problem to one where R3 or R1 applies. The reduction is in b (not Sigma/D_b).
- **Case A.A direct closure**: algebraic identity A = 2p1-1 < 1/D_b for the subcase p1 > p2+p3. No induction needed.
- **Generalization of the n=2 B2 strategy**: explicit multi-piece cut construction, extending the ε-cancellation identity val = p1 + p3/2 to higher n.
- **Extremal-smoothing S1 (LL-independent)**: G_n is the unique maximizer of V on Delta. STUCK 4+ rounds, no algebraic mechanism found. Not recommended as primary.

---

### Cheap-kill candidates

- **Case A.A (p1 > p2+p3)**: 3-step "subtract all" chain gives A = 2p1-1 < 1/D_b directly. No induction. PROVE THIS FIRST.
- **Equal-piece detection**: if p1-p_j = p_k for some j,k, then after pairing p1 at p_j, R1 fires immediately (two equal pieces). Many gap cases hit this.
- **Small m (m=2)**: halve p1, done. m=3: the n=2 B2a/b analysis applies directly. These are trivial subcases.

---

### Knowledge-base entries to use

- **Alternating sum / measure form** (certified: alt-sum-integral.md, greedy-odd-index.md): A(X) = measure{N odd}, core of all upper-bound computations.
- **Parity-invisible pairs** (certified: sum-bound-reductions.md): equal pairs contribute 0 to A; the core mechanism of all pairing strategies.
- **Berge/Weierstrass for V** (certified: extremal-framework.md): continuity of V on compact Delta; useful for compactness arguments.
- **knowledge_base.md "piecewise-concavity smoothing"**: cell-linearity of the payoff (proved in extremal-smoothing Prop 5) — not directly applicable but the cell-linear structure explains why local induction attempts fail.

---

### Analogous past problems (cruxes)

- **aimo-0196 (combinatorics, invariants-and-monovariants)**: "size-weighted sub-interval as potential; adversary strictly lowers it after any response." The crux is a strict-monovariant descent combined with a designated forced move. Analogous to the gap-case situation where no single step-local invariant works, but a GLOBAL pairing potential can be tracked. Not a direct match (the problem is about coins, not alternating sums), but the "arc potential that strictly decreases under forced moves" is structurally similar to what the gap-case proof needs.
- No other strong crux matches found. The stick-cutting + alternating-sum structure of this problem is not common in the pre-2026 corpus.

---

### Prior progress

- **Regimes A, B1**: CLOSED (shadow + partial-shadow, certified). Regimes A and B1 are NOT gap cases for the SB framework when p2 >= tau/2 (handled by R3). When p2 < tau/2, they overlap with the gap case but were previously closed by a DIFFERENT strategy (not SB induction). The gap case is the residual where NEITHER the shadow/partial-shadow NOR the R1/R2/R3 induction closes directly.
- **Regime B at n=2**: FULLY CLOSED (B1 + B2a + B2b, all rigorous). The B2 closure gives the prototype: val = p1 + p3/2 <= (3p1+1)/4 <= c(2) for the B2a subcase.
- **R1/R2/R3 reductions**: CERTIFIED (sum-bound-reductions.md). The gap case is exactly what remains after all three.
- **Extremal framework**: V continuous, max attained, V(G_n) = c(n). CERTIFIED.

---

### Dead ends (do not retry)

- **Partial-shadow preserves SB invariant**: PROVED FALSE. Sigma'/D_{b-j} <= Sigma/D_b fails 18/123/315/678 instances at n=3/4/5/6. Confirmed again this round: 19/19 tested gap cases have SB broken after optimal pairing. This is the fundamental obstacle.
- **Fixed "always-pair-at-p2" strategy**: 44/222 failures. Does not universally work.
- **Fixed "always-pair-at-smallest" strategy**: 95/222 failures. Worse than pair-at-p2.
- **Halving p1 b times (all cuts on p1)**: Leaves A = A({p2,...}) <= p2 < tau/2. But tau/2 > 1/D_b (since 2^{b-1} > 1), so this is too weak.
- **Halving top k pieces**: Requires sum(p1+...+pk) >= tau*(1-1/2^k). Verified to fail for B2 configs where all pieces are tiny.
- **S1 (G_n unique maximizer via smoothing)**: Stuck 4+ rounds, no mechanism. Explicitly recorded as dead-end in extremal-smoothing.md.
- **Monotone XY induction "more cuts help LB"**: FALSE (reviewer counterexample round 2). Do not use.

---

### Small-case / intuition notes (all conjectural, not proved)

**Gap-case structure at n=3 (4 pieces)**: The gap case has p1 < 8/15, p2 < 4/15, all distinct, sum=1. This forces p1+p2+p3 = 1-p4 > 1-p3 > 1-4/15 = 11/15 and p4 < p3 < 4/15. The three smallest pieces can be arbitrarily small but sum to at least (1-p1)/3 approx.

**Case A.A closure (proved)**: When p1 > p2+p3 (equivalently p1-p2 > p3), the 3-step "subtract all other pieces from p1" chain gives A = 2p1-1 < 1/15. This STRICTLY holds for p1 < 8/15. Covers the regime where p1 is "moderately large" in the gap case (p1 between 1/3 and 8/15 roughly, when 2-piece and 3-piece structure cooperate).

**After one gap-step, R3 often fires** (conjecture with 25/28 support): In most gap cases, after pairing p1 at p2 (one non-R3 step), the reduced instance satisfies R3 for the new tau'. The condition is p3 >= (Sigma-2*p2)*2^{b-2}/D_{b-1} — provable when p2 is close to tau/2 (reduces Sigma enough) or p3 is large.

**The tight gap cases are near G_n** (observation): The maximum mu in the strict gap case approaches 1/D only as p1 -> tau and p2 -> tau/2 simultaneously (i.e., approaching the R2/R3 boundary). In the interior: mu is strictly smaller. The "worst" strict-interior gap case at denom=60 achieves mu = 1/20 (at X=(8/15, 4/15, 3/20, 1/20)) — the boundary again! Strict interior cases (e.g. X=(1/2, 1/5, 1/6, 2/15)) achieve mu = 0.

**The correct proof of the gap case is NOT via a uniform single strategy** but via casework:
- Case A.A (p1 > p2+p3): proved by "subtract all" chain, A = 2p1-1 < 1/D_b.  
- Case B and A.B (p1 <= p2+p3): optimal strategy is adaptive (depends on which p_j brings the reduced instance into R1/R2/R3 territory). The algebraic condition for the "gap + R3" two-level argument to close needs to be formalized.

**Best guess for the proof path**: Close Case A.A directly (2p1-1 formula). For the remaining cases where p1 <= p2+p3 (i.e., p1 < tau AND the leftover p1-p2 < p3): show that either R1 fires (if p1-p2 = p3 for some pairing) OR R3 fires after one gap step (algebraic condition on p3 vs new tau'/2). The condition p1 <= p2+p3 in the gap case with p2 < tau/2 means p1 < tau/2 + p3, which with p3 < p2 < tau/2 gives p1 < tau = 2*(tau/2). This is a MUCH WEAKER condition and the inequality p3 >= new_tau'/2 needs to be proved directly.
