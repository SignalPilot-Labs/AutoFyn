# Build report — game-value-recursion (imo-2026-03, round 2)

**Status: partial.** Approach file: `results/imo-2026-03/approaches/game-value-recursion.md`.

## What this approach is
The diversity seed: work in game space, never integrate the layer-cake indicator and never
solve a scalar minimax over cut positions. Reformulate the LB lower bound as a pure
alternating-claiming-game guarantee and attack it with a dyadic-domination invariant
(`aimo-0117` crux) plus a budget-non-fungibility decoupling toward a recursion
`c(n)=φ(c(n-1))` with fixed point `2^n/D_n`.

## Proved in full this round (rigorous)
1. **Reformulation.** LB lower bound `V_n ≥ 1/D_n` with the dyadic marking ⇔ **(LB-claim)**:
   on any ≤n-cut refinement `Q` of `W_n={2^0,…,2^n}`, the first mover claims ≥ `2^n`, i.e.
   `f(Q) ≥ 1`. Via Lemma 0 (`Odd=(Σ+f)/2`, certified) + homogeneity. Genuinely different
   top-level target (a claiming guarantee, not an integral).
2. **Lemma R0** (proposed for certification): `0 ≤ f(S) ≤ Σ(S)`, and `f(S)=a_1−f(S∖{a_1})`
   for `a_1=max`. Full proof (grouping + sorted peel); numerically verified (200000 trials).
3. **Theorem LB-A** (Case A, top piece uncut): any ≤n-cut refinement leaving `2^n` whole has
   `f ≥ 1`. Three-line proof: `2^n>2^n−1=Σ(rest)` dominates ⇒ `f=2^n−f(rest)`,
   `f(rest)≤Σ(rest)=2^n−1`. Game-space form of certified round-1 "Case 1".
4. **Base cases n=0, n=1** end to end (every XY cut placement settled).
5. **Fixed point + final answer**: `c(n)=(1+1/D_n)/2=2^n/(2^{n+1}-1)`; `2c(n)−1=1/D_n`
   verified; base `c(1)=2/3`.

## The gap (honest, delimited)
**Case B — Budget non-fungibility (BNF).** When XY spends `j≥1` cuts on the top piece
(splitting `2^n` into `T`) and `n−j` on the remainder `R'=W_{n-1}`-refinement, prove
`f(T⊔R')≥1`. I reduced (BNF) to a precise game-value statement — "adaptive cross-region cut
allocation cannot beat the greedy bisection cascade" — and established: (i) the claiming
phase carries no residual adaptivity (Lemma 0), (ii) domination persists level-by-level
below the top (recursive hook), (iii) the cascade line is tight (`f=1`, via matched-pair
collapse). What is NOT proved: that every `(j,T,R')` gives `f≥1` (i.e. no allocation beats
the cascade). Explicitly showed why `f ≥ 2max−Σ` cannot help here (goes negative once the
top is fragmented). This is the SAME crux (GAP-L Case 2) the whole field is stuck on,
reached from the budget-allocation side.

**Upper bound**: set up as the mirror recursion, left open (carried this round by the two
revised approaches).

## Value even though partial
- Names the crux precisely as a *game-value* statement the other two framings also
  implicitly need (adaptivity-gains-nothing lemma).
- Confirms (again, from a new direction) that the two regions do NOT decouple for free — the
  shared n-cut budget is the genuine coupling, not a layer-cake artifact.
- Contributes 3 promotable lemmas (Lemma R0, the claiming-game reformulation, Case-A bound).

## Suggested routing
CHANGES REQUESTED (partial, real progress, gap remains). If the two revises stall on their
certificates next round, this framing's (BNF) target is the place to escalate — or seed a
fourth, even-further framing per the outline-reviewer's field note.

## Promotable lemmas (for reviewer certification)
- Lemma R0 (elementary f-bounds + peel identity).
- Reformulation (claiming-game form of LB lower bound).
- Theorem LB-A (Case-A lower bound, top uncut ⇒ f≥1).
