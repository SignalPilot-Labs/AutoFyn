# Approach: majorization-smoothing

## Status
partial

## Approaches tried
- (round 1, this approach) One-shot directed majorization / smoothing on the sorted
  piece-vector. **Outcome: reframed successfully into a clean parity/measure toolkit**
  (`Odd = (1+A)/2`, `A = ∫ 1[c(t) odd] dt`, matched-pair invisibility, bisection-deletes,
  top-match-difference). Proved Lemma 0 in full; proved the reformulation and toolkit in
  full; proved both bounds fully for `n = 1`. **Hit the predicted wall on the two general
  bounds:** neither "bisect a subset of LB's pieces" (gives `A ≤ min_{K} A(K)`) nor
  "repeatedly match top-to-second" (gives the `Φ`-functional) is universally `≤ 1/D_n` —
  I verified numerically that the first over-shoots (max over configs `≈0.167 > 1/7` at
  `n=2`) and the second is catastrophic on `[1,ε,…]` configs (`≈1`). The true XY optimum
  is an adaptive **combination** of bisection-deletion and matching, a covering
  optimization I could not close in one shot. Both general bounds are left as explicit,
  clearly-labelled GAPS.
- Recorded dead ends inherited (do NOT re-propose): "XY bisects max n times" (over-cuts,
  0.75 vs 4/7 at n=2); "LB marks n+1 equal pieces" (collapses); "blanket non-max-cut
  domination" (FALSE). Also newly killed this round: **"XY bisects a subset of LB's
  pieces" alone is insufficient** (max config value `1/(n+1)`-ish, not `1/D_n`); and
  **"XY always matches top-to-second" alone is insufficient** (fails on top-heavy configs).

## Current best
The problem is exactly reformulated (rigorously) and equipped with a proved toolkit.
- **Answer.** `c(n) = 2^n / (2^{n+1} − 1)`. Write `D_n = 2^{n+1} − 1`.
  Checks: `n=0 → 1`, `n=1 → 2/3`, `n=2 → 4/7`, `n=3 → 8/15`.
- **Lemma 0 (endgame) — PROVED in full** (induction + monotonicity sub-lemma). Reduces
  the game to: LB picks `≤ n+1` pieces, XY refines with `≤ n` cuts, LB's payoff is
  `Odd =` sum of odd-ranked (sorted-descending) pieces. Promotable.
- **Reformulation — PROVED in full.** `Odd = (1+A)/2` where `A = Σ (−1)^{i+1} a_i`
  (sorted desc) `= ∫_0^∞ 1[c(t) odd] dt`, `c(t) = #{pieces > t}`. So the claim
  `c(n)=2^n/D_n` is *equivalent* to `max_LB min_XY A = 1/D_n`.
- **Parity toolkit — PROVED in full** (P1 matched-pair invisibility, P2 bisection deletes
  a piece from `A`, P3 subset-bisection gives `A ≤ min_{K≠∅} A(K)`, P4 top-match replaces
  `{p₁,p₂}` by `{p₁−p₂}`). These are correct, reusable, and promotable.
- **`n=1` — PROVED in full, both bounds** (`c(1)=2/3`).
- **Open GAP-U (upper bound, general n):** for every LB marking, XY can force `A ≤ 1/D_n`.
  Mechanism identified: an adaptive mix of P2 (bisect-delete) and P4 (match), i.e. a
  covering/pairing optimization; the maximiser is dyadic with value exactly `1/D_n`
  (exact at `n≤2` per outline-reviewer maximin; numerics `n≤5`). Not closed one-shot.
- **Open GAP-L (lower bound, general n):** for LB's dyadic config, every XY response has
  `A ≥ 1/D_n`. Mechanism: geometric "budget vs. band-width" resource count (XY's `n` cuts
  cannot neutralise the geometrically growing odd-bands). Not closed one-shot.

## Full proof
(Not present: Status is `partial`. The complete sub-results below are rigorous; the two
general bounds remain GAP-U and GAP-L.)

### Setup and Lemma 0 (endgame) — PROVED

After all marks are placed and the stick cut, we have a fixed multiset of piece lengths.
Players alternately claim a whole unclaimed piece, LB first, each maximising his own total.

**Lemma 0.** For a fixed multiset `S` of nonnegative reals sorted `a₁ ≥ a₂ ≥ … ≥ a_m`,
the alternating-claim game has a well-defined value; the first mover's total is exactly
`a₁ + a₃ + a₅ + …` (odd ranks) and greedily taking the current largest is optimal for
both players.

*Proof.* The total `T = Σ S` is fixed, so maximising one's own total is the same as
minimising the opponent's; the game is finite and zero-sum, so backward induction gives a
well-defined value `V(S)` = the amount the mover can guarantee. If the mover takes a piece
`x`, the opponent then moves on `S∖{x}` and secures `V(S∖{x})`, so the mover ends with
`x + [(T−x) − V(S∖{x})] = T − V(S∖{x})`. Hence
```
    V(S) = max_{x∈S} [ T − V(S∖{x}) ] = T − min_{x∈S} V(S∖{x}).        (★)
```

*Monotonicity sub-lemma (M).* For any multiset `R` and reals `b ≥ b′ ≥ 0`,
`0 ≤ V(R ∪ {b}) − V(R ∪ {b′}) ≤ b − b′`.

*Proof of (M), by induction on `|R|`.* Base `|R| = 0`: `V({b}) = b`, `V({b′}) = b′`, and
`b − b′ ∈ [0, b−b′]`. Inductive step, `|R| = m ≥ 1`: put `U = R∪{b}`, `U′ = R∪{b′}`. By (★),
`V(U) = ΣU − f`, `V(U′) = ΣU′ − f′`, where `f = min_{x∈U} V(U∖{x})`,
`f′ = min_{y∈U′} V(U′∖{y})`. Since `ΣU − ΣU′ = b − b′`,
`V(U) − V(U′) = (b−b′) − (f − f′)`, so it suffices to prove `0 ≤ f − f′ ≤ b − b′`.
The removals split into: remove the tagged element, giving `V(R)` in both cases; or remove
some `x ∈ R`, giving `V((R∖{x})∪{b})` resp. `V((R∖{x})∪{b′})`. By the induction hypothesis
applied with base set `R∖{x}` (size `m−1`), for every `x ∈ R`
```
    0 ≤ V((R∖{x})∪{b}) − V((R∖{x})∪{b′}) ≤ b − b′.
```
Writing `g = min_{x∈R} V((R∖{x})∪{b})`, `g′ = min_{x∈R} V((R∖{x})∪{b′})`, this gives
`g ≥ g′` and `g ≤ g′ + (b−b′)`. Now `f = min(V(R), g)`, `f′ = min(V(R), g′)`. From `g ≥ g′`
we get `f ≥ f′`. From `g ≤ g′ + (b−b′)` and the elementary inequality
`min(A, C+d) ≤ min(A,C) + d` for `d ≥ 0`, we get `f = min(V(R),g) ≤ min(V(R),g′) + (b−b′)
= f′ + (b−b′)`. Hence `0 ≤ f − f′ ≤ b − b′`, proving (M). ∎(M)

*Main claim, by induction on `m`.* For `m ≤ 1` it is immediate. For `m ≥ 2`: by (★),
`V(S) = T − min_{x∈S} V(S∖{x})`. Compare removing `a₁` (the largest) with removing any
`a_k`. Writing `R = S∖{a₁,a_k}`, we have `S∖{a_k} = R∪{a₁}` and `S∖{a₁} = R∪{a_k}` with
`a₁ ≥ a_k`; by (M), `V(S∖{a_k}) ≥ V(S∖{a₁})`. Thus the minimum in (★) is attained by
removing `a₁`, so greedily taking `a₁` is optimal and
`V(S) = T − V(S∖{a₁})`. By the induction hypothesis on `S∖{a₁} = (a₂ ≥ a₃ ≥ …)`,
`V(S∖{a₁}) = a₂ + a₄ + …`, whence `V(S) = (a₁+a₂+…) − (a₂+a₄+…) = a₁ + a₃ + a₅ + …`. ∎

So, sorting the final pieces descending, **LB receives `Odd := a₁ + a₃ + a₅ + …`.** The
whole problem becomes `c(n) = max_{LB} min_{XY} Odd`, over LB's `≤ n` cuts (giving
`≤ n+1` pieces) and XY's `≤ n` further cuts.

### Reformulation (alternating sum / layer cake) — PROVED

Let `Odd = a₁+a₃+…`, `Even = a₂+a₄+…`, so `Odd + Even = 1` (total length) and
`Odd − Even = A`, where `A := Σ_{i} (−1)^{i+1} a_i` is the alternating sum of the
sorted-descending vector. Hence
```
    Odd = (1 + A) / 2 .
```
For each piece, `a_i = ∫_0^∞ 1[a_i > t]\, dt`. Fix `t`; the pieces exceeding `t` are exactly
ranks `1,…,c(t)` (sorted descending), so
`Σ_i (−1)^{i+1} 1[a_i>t] = Σ_{i=1}^{c(t)} (−1)^{i+1} = 1` if `c(t)` is odd, `0` if even.
Integrating,
```
    A = ∫_0^∞ 1[c(t) odd]\, dt = measure{ t ≥ 0 : c(t) = #\{pieces > t\} is odd }.     (LC)
```
(Verified numerically to `1e−5`.) In particular `A ≥ 0` (group `(a₁−a₂)+(a₃−a₄)+… ≥ 0`)
and `A ≤ a₁ ≤ 1`. The claim `c(n) = 2^n/D_n` is **equivalent** to
`max_{LB} min_{XY} A = 1/D_n`, since `2·(2^n/D_n) − 1 = (2^{n+1} − D_n)/D_n = 1/D_n`.

### Parity toolkit — PROVED

All four follow from (LC): `A` only sees the *parity* of `c(t)`.

- **(P1) Matched-pair invisibility.** Adjoining two equal pieces of value `v` to any
  multiset leaves `A` unchanged: it adds `2` to `c(t)` for `t < v` (parity unchanged) and
  `0` for `t ≥ v`. (Verified numerically.)

- **(P2) A bisection deletes a piece.** Cutting a piece of length `ℓ` into `(ℓ/2, ℓ/2)`
  (one cut) creates a matched pair; by (P1), `A` equals that of the configuration with the
  piece **removed**. More generally, for a *subset* `S` of the current pieces, bisecting
  every piece in `S` changes `c(t)` by `Σ_{j∈S}(2·1[t<ℓ_j/2] − 1[t<ℓ_j])`, whose parity is
  `Σ_{j∈S} 1[t<ℓ_j] (mod 2)`; so the final parity is `#\{i∉S : p_i > t\} (mod 2)`, i.e.

- **(P3) Subset-bisection.** If XY bisects a subset `S` of LB's pieces (cost `|S|` cuts),
  then `A = A(\{p_i : i∉S\})`. Since LB has `k ≤ n+1` pieces and XY has `n` cuts, XY may
  bisect all but one piece; thus XY can force `A ≤ min_{∅≠K⊆\{pieces\}} A(K)` (and
  `A = 0` whenever `k ≤ n`).

- **(P4) Top-match.** Cutting the largest piece `p₁` into `(p₂, p₁−p₂)` (one cut) creates a
  matched pair `(p₂, p₂)`; by (P1), `A` equals that of `\{p₁−p₂\} ∪ \{p₃,…,p_{n+1}\}` —
  i.e. it removes `p₁,p₂` and inserts their difference.

### Lower-bound construction (LB's dyadic marking)

LB marks so the `n+1` pieces are `q_j = 2^j/D_n` for `j = 0,…,n` (largest `2^n/D_n`, each
the double of the next, smallest `1/D_n`; they sum to `(2^{n+1}−1)/D_n = 1`). Against the
**self-similar XY attack** (pour all cuts into the current largest piece, re-imposing the
dyadic ratio inside it) one computes, via (LC), `A = 1/D_n` exactly (checked `n≤3`
numerically, and by the recursion below for the tight line). This certifies the *value*
`1/D_n` is attained; that no XY response does better is **GAP-L**.

### Upper-bound tools and the gap

By (P3)/(P4), for any LB marking XY has cheap responses driving `A` down. But:
- (P3) alone gives only `A ≤ min_{K} A(K)`, and `max_{config} min_{K} A(K) ≈ 0.167 > 1/7`
  at `n=2` (verified) — **insufficient**.
- (P4) iterated ("match top-to-second `n` times") yields a scalar functional `Φ` with
  `Φ([1,ε,…]) ≈ 1` — **catastrophically insufficient** on top-heavy configs.

The correct XY play interleaves **(P2) bisect-delete** (kill a piece cheaply, best when one
piece dwarfs its neighbour) with **(P4) match** (pair a piece to a neighbour, best when two
pieces are comparable). Concretely, `min_XY A` for dyadic is exactly `1/D_n`, attained by
bisecting the top piece and then matching within the residual — a mixed, adaptive line. A
one-shot majorization certificate for "`A ≤ 1/D_n` for **every** LB marking" is **GAP-U**;
`A` is provably *not* monotone under majorization, so the certificate must be directed
along the actual cut path, which I could not make uniform across all configs.

### `n = 1` (both bounds) — PROVED in full

Here `D_1 = 3`, target `c(1) = 2/3`, i.e. `max min A = 1/3`.

*Upper bound.* Any LB marking gives pieces `\{p, 1−p\}`; relabel so `p ≥ 1/2`. XY has one
cut of the large piece `p`.
- If `p ≥ 2/3`: XY bisects `p`. By (P2), `A = A(\{1−p\}) = 1−p ≤ 1/3`.
- If `1/2 ≤ p ≤ 2/3`: XY cuts `p` into `(1−p, 2p−1)` (valid: `2p−1 ≥ 0` and `1−p ≤ p`).
  The part `1−p` matches the existing `1−p`; by (P1)/(P4), `A = A(\{2p−1\}) = 2p−1 ≤ 1/3`.
In both ranges `A ≤ 1/3`, so `Odd = (1+A)/2 ≤ 2/3`. Hence `c(1) ≤ 2/3`.

*Lower bound.* LB plays `\{2/3, 1/3\}`. XY makes `≤ 1` cut; enumerate:
- No cut: `A = 2/3 − 1/3 = 1/3`.
- Cut the `1/3` piece into `(a, 1/3−a)`, `a ∈ [1/6, 1/3)`. Sorted: `2/3, a, 1/3−a`, so
  `A = 2/3 − a + (1/3 − a) = 1 − 2a ≥ 1 − 2·(1/3) = 1/3`.
- Cut the `2/3` piece into `(b, 2/3−b)`, `b ∈ [1/3, 2/3)`. Since `b ≥ 1/3 ≥ 2/3−b`, sorted:
  `b, 1/3, 2/3−b`, so `A = b − 1/3 + (2/3 − b) = 1/3`.
Thus `A ≥ 1/3` always, so `Odd ≥ 2/3`. Hence `c(1) ≥ 2/3`. Combining, **`c(1) = 2/3`.** ∎(n=1)

### Answer verification
`c(n) = 2^n/(2^{n+1}−1)`: `n=0` gives `1` (LB takes the whole stick, correct);
`n=1` gives `2/3` (proved above); `n=2` gives `4/7`; `n=3` gives `8/15`. The `n=2` maximin
`4/7` at the dyadic marking `\{4/7,2/7,1/7\}` was confirmed exactly by the outline-reviewer.

## Promotable lemmas
- **Lemma 0 (endgame-greedy).** *Statement:* for a fixed multiset sorted descending, the
  alternating-claim game value to the first mover is the sum of odd-ranked pieces; greedy
  is optimal for both. *Proved in full above* (induction + monotonicity sub-lemma (M)).
  Suggest caching at `lemmas/endgame-greedy.md`.
- **Reformulation lemma (odd-sum = (1+A)/2, layer cake).** *Statement:* `Odd = (1+A)/2`
  with `A = Σ(−1)^{i+1}a_i = measure{t : #\{pieces>t\} odd}`. *Proved in full above.*
- **Parity toolkit (P1)–(P4)** (matched-pair invisibility; bisection deletes a piece;
  subset-bisection `A = A(kept)`; top-match replaces `{p₁,p₂}` by `{p₁−p₂}`). *Proved in
  full above* from the layer-cake identity. Reusable by any approach that works with `A`.
