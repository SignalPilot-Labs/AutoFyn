## Status
partial (new, round 3 — skeleton)

## Approach: extremal-config

**Framing (genuinely different from direct-constructive).** Do NOT exhibit an explicit XY
strategy per LB configuration. Instead treat the value as a *saddle point of one function
over the space of LB configurations* and pin both bounds by an EXTREMAL / CONCAVITY
argument. The object of study is the map

    g(a) = min over XY's ≤ n cuts of O(a, XY),

a function of the LB piece-vector a = (a_1 ≥ … ≥ a_{n+1}), a_i ≥ 0, Σ a_i = 1 (≤ n+1
pieces). By Lemma G1, c(n) = max_a g(a). The whole problem becomes: **find max_a g(a) and
show it equals c(n) = 2^n/D, attained at the geometric config a* = (2^n,…,2,1)/D.** This
route resolves the upper-bound wall (including direct-constructive's Case B, all pieces >
1/D) uniformly, without any per-config strategy bookkeeping.

Answer (same): c(n) = 2^n/(2^{n+1}−1), D = 2^{n+1}−1.

## Shared imports (certified / reusable)
- **Lemma G1** (greedy = odd-ranked) — certified. Reduces to c(n) = max_a g(a).
- **Lemma R1/R2** (odd-sum rewritings, O = (1+μ{N odd})/2) — certified.
- **Dominance identity** P_j − Σ_{i<j} P_i = 1/D for the geometric config — from
  direct-constructive §3.
- **Lemma I** (interleaving) — from direct-constructive §5. Gives g(a*) = c(n) exactly.

## Skeleton

1. **Reduce to a config-space optimisation.** By G1, c(n) = max_a g(a). [import]

2. **Value at the geometric config: g(a*) = c(n).**
   - Upper: XY puts all n cuts in the top piece P_n = 2^n/D (Lemma I applies since P_n >
     Σ_{i<n} P_i by the dominance identity, and the residual fits), forcing O = P_n = c(n).
   - Lower: any XY response to a* leaves O ≥ c(n) — this is exactly the confined Fragments
     Lemma L1 + confinement L2 of direct-constructive (import once proved), OR is re-proved
     here as "a* is a critical point of g with g(a*) = c(n)" (see step 4).
   So g(a*) = c(n). [depends on L1/L2 or step 4]

3. **Concavity of g on the simplex (the distinct spine).**
   Claim: g is a **concave** function of a on the simplex.
   Mechanism: for each FIXED XY cut-pattern (cut positions expressed as fractions of the
   pieces they lie in, plus the assignment of ranks), O(a, XY) is a LINEAR function of the
   piece-vector a on each region where the induced sorted order is fixed; hence for a fixed
   combinatorial cut-pattern O is piecewise-linear and continuous, and the pointwise
   minimum g = min_XY O is a minimum of (piecewise-linear, hence concave-on-each-cell)
   functions. Establish concavity globally by showing the min is taken over a family closed
   under the ordering swaps so that g is concave (min of concave = concave when the cells
   align). **CHEAP FALSIFICATION FIRST:** numerically test concavity of g on random
   segments in the simplex for n=2,3,4 (sample midpoint vs endpoints: g(½a+½b) ≥
   ½g(a)+½g(b)?). If it fails, this framing is dead — abandon before investing.

4. **Extremal conclusion.** A concave g on the simplex attains its max at a point where the
   (super)gradient vanishes / KKT holds. Show the unique interior stationary point is the
   geometric config a* (the only config for which XY is *indifferent* among its optimal
   cuts — the "threshold indifference" / complementary-slackness condition: at a*, cutting
   the top piece and interleaving both give O = c(n)). The dominance identity
   P_j − Σ_{i<j}P_i = 1/D is exactly the stationarity condition (equal marginal 1/D at
   every rung of the dyadic ladder). Hence max_a g(a) = g(a*) = c(n). [depends on step 3]

5. **Assemble.** c(n) = max_a g(a) = c(n): the lower bound (LB plays a*, guarantees g(a*) =
   c(n)) and the upper bound (no LB config beats g(a*)) both follow from ONE extremal
   analysis. Verify on n=1,2,3.

## Key lemmas (claim + mechanism)

- **Lemma E1 (concavity of g).** g(a) = min_XY O(a,XY) is concave on the simplex, because O
  is piecewise-linear in a for each fixed cut-pattern and the value is a min over
  cut-patterns. — the load-bearing new claim; test numerically before proving.
- **Lemma E2 (stationarity ⟺ dominance identity).** The interior KKT/stationary point of
  the concave g is the geometric config, because the marginal gain of moving length between
  ladder rungs is equalised exactly when P_j − Σ_{i<j}P_i = 1/D for all j (the dominance
  identity). This is the dual certificate.
- **Lemma E3 (value at a*).** g(a*) = c(n): Lemma I gives the upper side (XY forces O =
  P_n = c(n)); L1/L2 (or the concavity+stationarity of step 4) gives the lower side.

## Open gaps
- **E1 (concavity of g)** — HIGH RISK, load-bearing. Run the numerical falsification test
  first. If g is only concave *cellwise* but not globally, replace by a smoothing/exchange
  argument: moving length from a smaller to a larger ladder rung (toward a*) weakly
  increases g until a* is reached.
- **E2 (stationary point = geometric)** — depends on E1; needs the KKT computation.
- **E3 lower side** — imports L1/L2 from direct-constructive, or is subsumed by E1+E2.

## Cases to cover
- Verify g concave numerically for n=2,3,4 BEFORE any proof (kill-switch).
- The boundary of the simplex (some a_i = 0, i.e. fewer than n+1 pieces) — g there equals
  the same problem with fewer marks; check the max is interior, not on the boundary.
- Verify max_a g(a) = c(n) numerically at n=1,2,3 (already known g(a*) = c(n)).

## Watch out for
- **Vacuity / circularity risk:** if concavity cannot be established independently, the
  claim "max is at a*" reduces to the per-config upper bound U1 by another name — the same
  wall. The whole worth of this approach is Lemma E1 being a genuine, independently proved
  structural fact. Run the n=2,3,4 concavity check as the very first step; do not invest if
  it fails.
- g is a min of finitely many linear pieces only after fixing the discrete cut-pattern and
  rank-order — count these carefully; the number of patterns is finite but the ε→0 (open
  cut positions) supremum must be handled (g is a min, attained or approached).
- Do not conflate "concave" with "Schur-concave": g is NOT monotone in inequality of a (the
  vertex config {1,0,…} gives g = 1/2 < c(n)), so the max is a genuine interior saddle, not
  the most-spread config.

## Current best
Framing and the saddle-point identification (a* via the dominance identity as the
stationarity condition) are in hand; g(a*) = c(n) via Lemma I is established. The distinct
content — global concavity of g (Lemma E1) — is conjectural and must pass the numerical
concavity check before investment. If E1 holds, both bounds fall out of one extremal
argument, bypassing the per-config Case-B wall entirely.
