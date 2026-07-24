# Approach: game-value-recursion

Framing (deliberately distinct from the other two live approaches): work in **game
space**. Never integrate the layer-cake parity indicator, and never solve a scalar
minimax over cut-positions. Instead reformulate both bounds as *explicit guarantees in the
alternating-claiming game* and try to prove them turn-by-turn with a **dyadic-domination
invariant** (the `aimo-0117` crux) plus a **budget-non-fungibility** decoupling that turns
the whole game into a recursion `c(n) = φ(c(n-1))` with fixed point `2^n/D_n`.

## Status
partial

## Approaches tried
- (round 2, this approach, NEW) Game-value recursion via claiming-game reformulation +
  dyadic domination. **Outcome: partial.** Fully proved: the reformulation "LB lower bound
  ⇔ LB claims ≥ 2^n on any ≤n-cut refinement of W_n"; the domination invariant; the LOWER
  bound in the **top-uncut** regime (Case A) end to end; base cases n=0, n=1; the fixed-point
  algebra and final-answer verification. The **budget non-fungibility** decoupling (Case B:
  XY cuts the top piece) is reduced to a single precise game-value sub-claim but is NOT
  closed — this is the same combinatorial crux the whole field is stuck on, reached here from
  a different direction. The upper bound is set up as the mirror recursion and left open.

## Current best

The furthest rigorous progress of THIS approach:

1. **Game-value reformulation (proved).** `V_n := max_{LB} min_{XY} f(P) = 1/D_n` is
   equivalent to `c(n) = 2^n/D_n` (certified, `layer-cake-alt-sum.md`). For the LB lower
   bound with LB's dyadic marking, working in **unnormalized** units
   `W_n = {2^0, 2^1, …, 2^n}` (total `D_n = 2^{n+1}-1`), the statement `f(P) ≥ 1/D_n` for
   every XY response becomes, via `Odd(P) = (Σ(P)+f(P))/2` (Lemma 0, certified):

   > **(LB-claim)** On any multiset `Q` obtained from `W_n` by ≤ n cuts, the first mover
   > (Liu Bang) can guarantee total ≥ `2^n` in the alternating-claiming game.

   Indeed `Odd(Q) = (D_n + f(Q))/2 ≥ 2^n ⇔ f(Q) ≥ 2^{n+1} - D_n = 1`. So the LB lower bound is *exactly* the
   pure combinatorial-game guarantee (LB-claim). This is the genuinely different top-level
   target: a claiming-game guarantee, not an integral.

2. **Dyadic domination invariant (proved).** For `W_n`, every piece dominates the sum of all
   strictly smaller original pieces: `2^k > 2^{k-1}+⋯+2^0 = 2^k-1`. In particular the top
   piece `2^n` strictly exceeds the total `2^n-1` of the whole remainder `R := W_{n-1}`.

3. **LOWER BOUND, Case A (top piece uncut) — PROVED.** `f(Q) ≥ 1`, hence LB claims ≥ 2^n.
4. **Base cases n=0, n=1 — PROVED.**
5. **Fixed-point / final answer — VERIFIED.** `c(n) = (1+1/D_n)/2 = 2^n/D_n`, and
   `2·2^n/D_n − 1 = 1/D_n`.

**The open gap (Case B — budget non-fungibility).** When XY spends `j ≥ 1` of its `n` cuts
on the top piece and `n−j` on the remainder, the top no longer dominates and the peel
identity does not directly reduce to the `(n−1)`-game. The precise remaining sub-claim is
stated and partially reduced in the *Full analysis* below; it is the same wall
(`GAP-L`, Case 2) that `self-similar-recursion` and `alternating-sum-threshold-potential`
reach by their routes. Reached here as: *"an adaptive XY that splits its cut budget across
the top region and the remainder cannot beat an XY that spends greedily on the current
largest piece."*

## Full analysis (rigorous where marked PROVED; the gap is delimited explicitly)

Throughout, for a finite multiset `S` of nonnegative reals sorted descending
`a_1 ≥ a_2 ≥ ⋯ ≥ a_m`, put `f(S) = a_1 - a_2 + a_3 - ⋯` (alternating sum) and
`Σ(S) = Σ a_i`. By Lemma 0 (`endgame-greedy.md`, certified) the value of the
alternating-claiming game to the first mover is `Odd(S) = (Σ(S)+f(S))/2`. `D_m = 2^{m+1}-1`.

### Lemma R0 (elementary bounds on f). For every finite multiset `S`,
`0 ≤ f(S) ≤ Σ(S)`, and if `a_1` is a maximum element then `f(S) = a_1 - f(S∖{a_1})`.

*Proof.* Sorted descending, group `f(S) = (a_1-a_2)+(a_3-a_4)+⋯`; each grouped term is
`≥ 0` and the final unpaired term (if `m` odd) is `a_m ≥ 0`, so `f(S) ≥ 0`. Also
`Σ(S) - f(S) = 2(a_2 + a_4 + ⋯) ≥ 0`, so `f(S) ≤ Σ(S)`. Finally, removing a maximum `a_1`
leaves `a_2 ≥ a_3 ≥ ⋯` sorted descending, whose alternating sum is `a_2 - a_3 + ⋯`, and
`a_1 - (a_2 - a_3 + ⋯) = a_1 - a_2 + a_3 - ⋯ = f(S)`. ∎ (Numerically verified: 200000
random multisets, 0 violations of `0 ≤ f ≤ Σ`.)

### Reformulation (PROVED). LB's lower bound `V_n ≥ 1/D_n` with the dyadic marking is
equivalent to statement **(LB-claim)** above.

*Proof.* Normalize away: the dyadic marking scales `W_n` by `1/D_n`, and `f` is homogeneous
of degree 1, so `min_{XY} f ≥ 1/D_n` (normalized) ⇔ `min_{XY} f(Q) ≥ 1` for `Q` an ≤n-cut
refinement of the unnormalized `W_n`. By Lemma 0, LB's claimed total on `Q` is
`Odd(Q) = (Σ(Q)+f(Q))/2 = (D_n + f(Q))/2` (cuts preserve the total `Σ = D_n`), and
`(D_n+f(Q))/2 ≥ 2^n ⇔ f(Q) ≥ 2^{n+1} - D_n = 2^{n+1} - (2^{n+1}-1) = 1`. ∎

So the entire lower bound is the game guarantee (LB-claim). We prove it in the top-uncut
regime and reduce the rest to the budget-non-fungibility sub-claim.

### Theorem LB-A (Case A: XY leaves the top piece whole) — PROVED.
Let `Q` be obtained from `W_n` by ≤ n cuts, none in the interior of the top piece `2^n`.
Then `f(Q) ≥ 1`, so (LB-claim) holds: LB claims ≥ 2^n.

*Proof.* The top piece `2^n` is uncut, so it is one of the pieces of `Q`. Every other piece
of `Q` arises by cutting the remainder `R = {2^0,…,2^{n-1}}` (total `Σ(R)=2^n-1`); cutting
never increases a piece's length, and any piece of a cut-up `R` has length `≤ Σ(R)=2^n-1`.
By the domination invariant `2^n > 2^n-1`, so `2^n` is the strict maximum of `Q`. By Lemma
R0, `f(Q) = 2^n - f(Q∖{2^n})`, and `Q∖{2^n}` is `R` after ≤ n cuts, so by Lemma R0
`0 ≤ f(Q∖{2^n}) ≤ Σ(R) = 2^n - 1`. Hence `f(Q) = 2^n - f(Q∖{2^n}) ≥ 2^n - (2^n-1) = 1`. ∎

This is the game-space rendering of the certified "Case 1": LB simply grabs the dominating
top piece and the domination margin `2^n-(2^n-1)=1` is exactly the answer's numerator.

### Base cases — PROVED.
- **n = 0:** `W_0 = {1}`, 0 cuts, `Q = {1}`, `f = 1 ≥ 1`. LB claims `1 = 2^0`. ✓
- **n = 1:** `W_1 = {1,2}`, ≤ 1 cut. If XY makes no cut, `f({1,2}) = 2-1 = 1`. If XY cuts the
  top `2` at offset `x∈(0,2)` into `{x, 2-x}` (so `Q = {1,x,2-x}`): the three values sum to
  `3`; by Lemma R0 the largest is `≥ 3/3 = 1`, and writing `Q=\{u≥v≥w\}` we get
  `f = u - v + w = (u+w) - v = (3 - v) - v ... ` — directly: with `x ≤ 1 ≤ 2-x` the order is
  `2-x ≥ 1 ≥ x`, `f = (2-x) - 1 + x = 1`; with `x ≥ 1` symmetric, `f = 1`; if `x=1`,
  `Q=\{1,1,1\}`, `f = 1-1+1 = 1`. If XY cuts the piece `1` into `{y,1-y}` (so `Q=\{2,y,1-y\}`,
  top `2` still dominates `y+(1-y)=1`): by Lemma R0 `f = 2 - f(\{y,1-y\}) = 2 - |2y-1| ≥ 1`
  (since `|2y-1| ≤ 1`). In every case `f(Q) ≥ 1`. ✓ (Numerically: `min f` over ≤1 cut = 1.)

### Fixed point and final answer — VERIFIED.
Granting the lower bound `f ≥ 1` (normalized `≥ 1/D_n`) and the matching upper bound, the
game value is `V_n = 1/D_n`, so by the certified reduction
`c(n) = (1 + V_n)/2 = (1 + 1/D_n)/2 = (D_n + 1)/(2 D_n)`. Now `D_n + 1 = 2^{n+1}`, so
`c(n) = 2^{n+1}/(2 D_n) = 2^n/D_n = 2^n/(2^{n+1}-1)`. Consistency of the fixed point:
`2·c(n) - 1 = 2·2^n/D_n - 1 = (2^{n+1} - D_n)/D_n = 1/D_n = V_n`, matching
`c(n) = (1+V_n)/2`. Base check `c(1) = 2/3` (certified). ∎ (final answer)

### The recursion and the open gap (Case B: XY cuts the top piece).

Write `Q` as a ≤n-cut refinement of `W_n` in which the top piece `2^n` receives `j ≥ 1`
cuts (splitting it into a multiset `T`, `Σ(T)=2^n`, `|T|=j+1`) and the remainder
`R = W_{n-1}` receives the other `n-j` cuts (giving `R'`, `Σ(R')=2^n-1`), so `Q = T ⊔ R'`.

**The intended recursion (game value).** The self-similar structure is: `R = W_{n-1}` is,
up to the global scale, an instance of the `(n-1)`-level problem. If XY's `n-j` cuts on `R`
could be analyzed *independently* of its `j` cuts on the top, one would get a clean
recursion `min_XY f(Q) = (top contribution) + (scaled (n-1)-game value)` and, by induction,
`f(Q) ≥ 1`. The obstruction, isolated by the new-framing explorer, is exactly that **XY's
budget is one pool of `n` cuts, allocated adaptively across the two regions** — so the
`R`-subgame is played with a variable budget `n-j` chosen by XY after weighing the top.

**Budget-non-fungibility sub-claim (the crux; OPEN).**

> **(BNF)** For every `j` with `1 ≤ j ≤ n`, every split of `2^n` into `j+1` positive pieces
> `T`, and every ≤`(n-j)`-cut refinement `R'` of `R = W_{n-1}`, one has `f(T ⊔ R') ≥ 1`.

Equivalently (claiming form): however XY fragments the top into `j+1` pieces and spends its
remaining `n-j` cuts on the remainder, LB still claims ≥ `2^n` from `Q = T ⊔ R'`.

**Partial reduction of (BNF) (rigorous as far as it goes).**

*(i) The greedy-target principle.* By Lemma 0, in the claiming game "take a current largest
piece" is optimal for the mover. So LB's guaranteed total on `Q` is `Odd(Q)`, and (BNF) is
purely about the sorted multiset `Q = T ⊔ R'`. This removes all adaptivity *in the claiming
phase*; the only adaptivity left is XY's cut allocation, which is the content of (BNF).

*(ii) Domination is retained level-by-level below the top.* Even after the top is
fragmented, the remainder still satisfies the dyadic chain: within `R' = ` refinement of
`{2^0,…,2^{n-1}}`, the original piece `2^{n-1}` (if uncut) dominates `2^{n-1}-1 = Σ` of the
smaller originals, etc. So the *sub*-problem on `R'` is itself a Case-A/Case-B instance one
level down. This is the recursive hook: if the top fragment `T` behaved like a single
"effective top" dominating `R'`, Case A one level down would finish. It does **not** in
general, because `max(T)` can be as small as `2^n/(j+1)`, which for `j ≥ 1` may be `≤`
`max(R') ≤ 2^{n-1}` (they tie at `j=1`, bisection). This tie/inversion at the top is the
precise place the clean recursion breaks.

*(iii) The extremal line.* The minimum `f = 1` is attained by the **bisection cascade**:
`2^n → (2^{n-1},2^{n-1})` collapses (matched-pair invisibility, `layer-cake-alt-sum.md`,
`P1`) `{2^{n-1},2^{n-1}} ⊔ W_{n-1}` to a `W_{n-1}`-shaped multiset (three `2^{n-1}`'s, two
cancel), then recurse. This shows (BNF) is **tight** and that the worst XY allocation is
`j` distributed so as to bisect down the staircase. What remains unproved is that **no other
allocation of the `n` cuts across the two regions drives `f` below 1** — i.e. that the
adaptive cross-region choice of `j` and of where the `n-j` remainder cuts land can never
beat the cascade. Numerically (brute single/double-cut search, and the reviewer's
independent grid search for `n≤4`) the floor is exactly `1` and is achieved on the cascade
line; but a from-scratch proof that every `(j, T, R')` gives `f(T⊔R') ≥ 1` is not in hand.

**Why the bare inequality `f ≥ 2·max − Σ` does NOT close (BNF).** For the whole `Q`,
`2·max(Q) − Σ(Q) = 2·max(Q) − D_n`, and once the top is fragmented `max(Q) ≤ 2^{n-1} < 2^n`,
so `2·max(Q) − D_n < 0`, giving no information. The invariant must be tracked **recursively
per dyadic level** (the domination margin `1` re-appears at each level of the staircase),
not applied once globally — exactly as warned in the outline. This is why (BNF), not a
one-line domination bound, is the true content.

**Status of (BNF): OPEN.** This is the honest remaining gap of this approach. It is the
same crux (`GAP-L` Case 2) as the other approaches, reached from the claiming-game /
budget-allocation side. Its value as a diversity seed: it names the target precisely as a
*game-value* statement — "adaptive cross-region cut allocation cannot beat the greedy
bisection cascade" — which the other framings also implicitly need.

### Upper bound (mirror recursion) — OPEN (not attempted rigorously this round).
The upper bound `V_n ≤ 1/D_n` becomes: on ANY LB marking (≤ n+1 pieces, total 1), XY has a
≤n-cut response with `f ≤ 1/D_n`, i.e. XY holds LB to ≤ `2^n/D_n`. In the recursion framing
this is the dual guarantee "XY forces the game value down to the fixed point at every
scale." It is left open here; the two revised approaches (`self-similar-recursion`'s regime
split and `alternating-sum-threshold-potential`'s explicit slot-matching) carry the UB this
round. This approach's contribution is the LB reformulation and Case A; a full solve needs
(BNF) and the UB recursion.

## Promotable lemmas

- **Lemma R0 (elementary f-bounds).** For every finite multiset `S`: `0 ≤ f(S) ≤ Σ(S)`, and
  `f(S) = a_1 − f(S∖{a_1})` when `a_1 = max S`. Proved in full above (grouping + peel
  identity); numerically verified (200000 trials, 0 violations). Reusable by all approaches
  as the "f ≤ Σ" and "peel-the-max" primitives. *Candidate for certification.*
- **Reformulation (claiming-game form of the LB lower bound).** `V_n ≥ 1/D_n` (dyadic
  marking) ⇔ on every ≤n-cut refinement `Q` of `W_n = {2^0,…,2^n}`, the first mover claims
  ≥ `2^n` (equivalently `f(Q) ≥ 1`). Proved above from Lemma 0 + homogeneity. Useful as the
  common target statement for GAP-L across framings. *Candidate for certification.*
- **Case-A lower bound (Theorem LB-A).** Any ≤n-cut refinement of `W_n` that leaves the top
  piece `2^n` whole has `f ≥ 1`. Proved in full above (domination + peel + `f ≤ Σ`). This is
  the game-space form of the certified round-1 "Case 1"; offered as an independent
  re-derivation. *Candidate for certification.*
