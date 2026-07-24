# Build report — cut-budget-jacobsthal-recursion (imo-2026-03), round 5

**Status: partial.** File: `results/imo-2026-03/approaches/cut-budget-jacobsthal-recursion.md`.

## Cheap-kill: PASSED (framing alive)
Ran the mandated vertex/optimization enumeration. The floor identity
`min_{≤k cuts} f(W_n) = f(W_{n−k})` holds EXACTLY:
- n=3: `5,3,1,1` for k=0..3 (= f(W_3),f(W_2),f(W_1),f(W_0)).
- n=4: `11,5,3,1,1` for k=0..4.
Jacobsthal values `f(W_m)=(2^{m+1}+(−1)^m)/3 = 1,1,3,5,11,21,43` confirmed. So the scaffold is real.

## Proven rigorously this round
1. **Reduction** imported from certified `endgame-greedy` + `layer-cake-alt-sum`; upper bound
   imported (certified). Answer `c(n)=2^n/(2^{n+1}−1)` pinned contingent on (LBL).
2. **Lemma 3.1 — two-band per-cut identity** (from certified layer-cake): a single cut of `V` into
   `V_1≤V_2` flips `c(t)` parity exactly on `[0,m)∪[V−m,V)`, `m=min`; `|Δf|≤2m≤V`. Full proof.
   (Discrete companion to certified Lemma I.)
3. **Lemma 4.1 — tightness**: top-bisection cascade attains `f(W_{n−k})` in k cuts (upper direction
   of the identity). Full proof.
4. **Lemma 5.1 — uncut survivor**: any ≤n-cut refinement of W_n leaves ≥1 original piece uncut.
5. **Lemma 6.1 — top-uncut case of (LBL)**: `2^n` uncut ⇒ `f(Q)≥2^{n−1}≥1`. Full proof.
6. **Lemma 6.2 — all-bisection case**: `f(Q)≥1`. Full proof.

## Negative finding (IMPORTANT — the spec's driver is refuted)
The proposed induction driver — "each cut drops f by at most the Jacobsthal decrement
`D_i=f(W_{n−i+1})−f(W_{n−i})`" — is **FALSE**. Explicit refuting instance, reachable from `W_4`
with 3 cuts:
```
Q' = {16, 4, 3.567, 2.115, 2, 1.885, 1, 0.433},  f(Q')≈14.134,
```
one further cut → `f≈1.866` (drop ≈12.27), while `D_4 = f(W_1)−f(W_0) = 0`. Reason: cuts can
RAISE f (new top odd-bands), then a single later cut collapses many bands at once, so the
single-cut drop is unbounded by the remaining Jacobsthal budget. Max observed single-cut drops
(n=4) vs decrements: i=2: 10 vs 2; i=3: 14 vs 2; i=4: 14 vs 0.

The floor is nonetheless respected (0 violations): the correct per-cut statement is the global
**domination floor (D)** `min over single cuts f(Q) ≥ f(W_{n−i})`, which is NOT local — it needs
the full odd-band profile of `Q'`, so it is as hard as (LBL) itself.

## Gap reduction achieved
Via Lemma 6.1, (LBL) reduces to **(LBL-B)**: refinements in which the top piece `2^n` IS cut have
`f≥1`. This is exactly the classical round-1 Case B / round-2 "budget non-fungibility" crux. The
cut-budget framing does not dissolve it; the refutation explains why a per-cut monovariant on `f`
cannot.

## Spec concerns (for the outliner/orchestrator)
- The spec's step-3 "per-cut floor domination = top-bisection dominates any single cut" is stated as
  if the decrement is bounded; the decrement bound is FALSE. The approach can only survive if the
  induction hypothesis is strengthened to carry the whole COUNT-FUNCTION PROFILE of `Q_i` (a
  monovariant on `c(t)`), not just the scalar `f`. Recommend next round either (a) reformulate the
  IH as a profile-domination / majorization on `c(t)`, or (b) drop the budget induction and attack
  (LBL-B) structurally (which of the ≤n−1 non-top cuts must land inside the `2^n` block).
- This slug is genuinely diverse (non-integrality) and the endpoint identity is real, so it is worth
  keeping live, but its headline mechanism needed correction — recorded honestly, no overclaim.

## Promotable lemmas proposed
- Lemma 3.1 (two-band single-cut identity), Lemma 5.1 (uncut survivor), Lemma 6.1 (top-uncut floor).
  All proved in full; see approach file §3, §5, §6.
