# Approach: cut-budget-jacobsthal-recursion

## Status
partial

## Approaches tried
- **Round 5 (this slug, NEW): budget induction driven by the certified two-band cut-slide
  derivative, targeting the floor identity `min_{≤k cuts} f(W_n) = f(W_{n−k})` (Jacobsthal
  1,1,3,5,11,21,…).** Cheap-kill vertex/optimization enumeration CONFIRMS the endpoint identity
  exactly for n=3 (5,3,1,1 over k=0..3) and n=4 (11,5,3,1,1 over k=0..4), so the framing is alive.
  Proven rigorously this round: (i) the two-band per-cut identity from certified Lemma L; (ii)
  the tightness/upper direction (top-bisection cascade attains `f(W_{n−k})`); (iii) the "at least
  one original piece is uncut" structural lemma; (iv) the **top-uncut case** `f≥1` in full (clean
  `f(Q)=2^n−f(rest)≥2^{n−1}`); (v) the **all-bisection case** `f≥1`. **Negative finding
  (important):** the specific per-cut *domination / decrement* mechanism the spec proposed —
  "each cut drops `f` by at most the Jacobsthal decrement `f(W_{n−k+1})−f(W_{n−k})`" — is
  **FALSE**, refuted by an explicit reachable config (see §7). A single cut can drop `f` by 12.27
  from a 3-cut config whose decrement budget is 0. So the induction *driver* as specified does not
  close the gap; the genuine residual coincides with the long-standing "top piece is cut" (Case B)
  crux. Outcome: partial — real proven scaffolding + an honest refutation of the proposed
  mechanism, gap reformulated precisely.

## Current best

The whole problem is reduced (via certified machinery) to the lower-bound residual (LBL):

> **(LBL):** every refinement `Q` of `W_n = {2^0, 2^1, …, 2^n}` obtained by at most `n` extra
> cuts satisfies `f(Q) ≥ 1`, where `f` is the alternating sum of the sorted-descending piece
> multiset.

The upper bound `c(n) ≤ 2^n/D_n` (`D_n = 2^{n+1}−1`) is **fully proven and certified** and is
imported. Answer `c(n) = 2^n/(2^{n+1}−1)`, verified below.

This approach establishes a rigorous **budget scaffold** for (LBL): the Jacobsthal floor sequence
`f(W_m) = (2^{m+1}+(−1)^m)/3` (values `1,1,3,5,11,21,…`), the exact **two-band per-cut identity**,
the exact **tightness** of the floor (XY *attains* `f(W_{n−k})` with `k` cuts), and a full proof
of (LBL) in the **top-uncut** case and the **all-bisection** case. The **open gap** is the
top-cut case, equivalently the *per-cut domination floor* (§7); crucially, this round shows the
naive per-cut decrement bound that was meant to drive the induction is **false**, so the gap must
be closed by a global/structural argument, not by a local per-cut accounting.

---

## 1. Setup and imported reductions (all certified)

The game reduces (certified `lemmas/endgame-greedy.md`, `lemmas/layer-cake-alt-sum.md`) as
follows. After all cuts, the final multiset of piece lengths is `P` (total `1`). By
**endgame-greedy**, Liu Bang (moving first) guarantees exactly `Odd(P) = (1+f(P))/2`, where for a
multiset sorted descending `a_1 ≥ a_2 ≥ …`,
```
    f(P) = a_1 − a_2 + a_3 − ⋯ .
```
By **layer-cake-alt-sum**, `f(P) = M(P) := measure{ t ≥ 0 : c_P(t) is odd }`, where
`c_P(t) = #{pieces of P exceeding t}`. Consequently, writing `D_n = 2^{n+1}−1` and using
`2·(2^n/D_n) − 1 = 1/D_n`,
```
    c(n) = (1 + max_{LB} min_{XY} f)/2,   and   c(n) = 2^n/D_n  ⇔  max_{LB} min_{XY} f = 1/D_n .
```

**Upper bound (imported, certified).** By **delete-subtract-reachability** (Lemma A) and
**subset-sum-pigeonhole** (Lemma B), against *any* Liu Bang marking XY forces `f ≤ 1/D_n`, hence
`min_{XY} f ≤ 1/D_n` for every LB choice, giving `max_{LB} min_{XY} f ≤ 1/D_n` and
`c(n) ≤ 2^n/D_n`. This is fully proven and is not re-derived here.

**Lower bound = (LBL).** Liu Bang plays the dyadic marking that cuts `[0,1]` into pieces of
scaled lengths `2^i/D_n` (`i = 0,…,n`); in integer units this is `W_n = {2^0,…,2^n}`, sum `D_n`.
XY then adds at most `n` marks, i.e. at most `n` cuts, producing a refinement `Q` of `W_n`. To
prove `min_{XY} f = 1/D_n` it suffices (scaling by `D_n`) to prove **(LBL)**: `f(Q) ≥ 1` for
every ≤`n`-cut refinement `Q` of `W_n`. (Tightness `min = 1` is §4.) Throughout we work in
integer units on `W_n`.

Two facts used repeatedly, both immediate from `f = M`:
- **(F1)** `0 ≤ f(Q) ≤ max(Q)`: since `{t : c_Q(t) odd} ⊆ {t : c_Q(t) ≥ 1} = [0, max(Q))`.
- **(F2) Peel:** if `Q` has a *unique* strict maximum `a_1`, then `f(Q) = a_1 − f(Q∖{a_1})`
  (the max sits at rank 1, all other ranks shift up by one, flipping their signs).

---

## 2. The Jacobsthal floor sequence

**Definition.** `W_m = {2^0, 2^1, …, 2^m}`.

**Lemma 2.1 (Jacobsthal values).** `f(W_m) = (2^{m+1} + (−1)^m)/3`, and `f(W_m) = 2^m − f(W_{m−1})`
with `f(W_0) = 1`. The values for `m = 0,1,2,3,4,5,6` are `1, 1, 3, 5, 11, 21, 43`.

*Proof.* `W_m` sorted descending is `2^m, 2^{m−1}, …, 2^0`, all distinct, so `2^m` is the unique
max and (F2) gives `f(W_m) = 2^m − f(W_{m−1})`, with base `f(W_0) = f({1}) = 1`. Solving the
recurrence `x_m = 2^m − x_{m−1}`, `x_0 = 1`: the particular solution `2^{m+1}/3` plus homogeneous
`(−1)^m·C`; matching `x_0=1` gives `C = 1/3`, so `x_m = (2^{m+1}+(−1)^m)/3`. Substituting
`m=0,…,6` yields `1,1,3,5,11,21,43`. ∎

Note `f(W_m)` is strictly decreasing for `m = n, n−1, …, 1` and `f(W_1) = f(W_0) = 1`, so the
smallest floor value is `f(W_0) = 1`; (LBL) is exactly `f(Q) ≥ f(W_0) = 1` under `n` cuts.

---

## 3. The two-band per-cut identity (proven)

**Lemma 3.1 (single-cut band identity).** Let `Q` be any multiset and let `Q'` be obtained by
replacing one piece of value `V` by two pieces `V_1 ≤ V_2` with `V_1 + V_2 = V`. Put
`m := V_1 = min(V_1,V_2) ≤ V/2`. Relative to the count function of the *other* pieces, cutting
flips the parity of `c(t)` exactly on the two disjoint bands
```
    B_low = [0, m)      and      B_high = [V − m, V),
```
each of length `m`, and does not change `c(t)` elsewhere. Consequently
```
    f(Q') − f(Q) = Δ_low + Δ_high,
    Δ_low  = μ{t∈B_low  : c_Q(t) even} − μ{t∈B_low  : c_Q(t) odd},
    Δ_high = μ{t∈B_high : c_Q(t) even} − μ{t∈B_high : c_Q(t) odd},
```
where `μ` is Lebesgue measure and `c_Q` is the count function *before* the cut. In particular
`|f(Q') − f(Q)| ≤ 2m ≤ V`.

*Proof.* Let `c(t)` be the count of all pieces of `Q` exceeding `t`, and `c'(t)` the same for
`Q'`. The only difference is the one piece: in `Q` it contributes `1[V > t]`; in `Q'` the two
pieces contribute `1[V_1 > t] + 1[V_2 > t]`. Hence
```
    c'(t) − c(t) = 1[V_1 > t] + 1[V_2 > t] − 1[V > t].
```
For `t ∈ [0, V_1)` this is `1+1−1 = +1`; for `t ∈ [V_1, V_2)` it is `0+1−1 = 0`; for
`t ∈ [V_2, V)` it is `0+0−1 = −1`; for `t ≥ V` it is `0`. Thus `c'(t)` differs from `c(t)` by an
odd number precisely on `[0, V_1) ∪ [V_2, V)`; since `V_1 = m` and `V − V_2 = V − (V−m) = m`,
these are `B_low = [0,m)` and `B_high = [V−m, V)`, each of length `m`, and there the parity of the
count flips; elsewhere the parity is unchanged. By `f = M = ∫ 1[c(t) odd] dt` (layer-cake), the
change in `f` is `∫ (1[c' odd] − 1[c odd])`. Off the two bands the integrand is `0`. On a band
where parity flips, `1[c' odd] − 1[c odd] = +1` where `c` was even and `−1` where `c` was odd,
giving the stated `Δ_low, Δ_high`. Since each band has length `m`, each of `Δ_low, Δ_high` lies in
`[−m, m]`, so `|f(Q')−f(Q)| ≤ 2m ≤ V`. ∎

This is the exact discrete analogue of certified **Lemma I** (`cut-slide-derivative`): sliding one
cut is the derivative form; making a fresh cut is the integrated two-band form above. Both are
consequences of the same layer-cake parity accounting.

---

## 4. Tightness: the floor identity's upper direction (proven)

**Lemma 4.1 (top-bisection cascade attains `f(W_{n−k})`).** For every `0 ≤ k ≤ n` there is a
`k`-cut refinement `Q_k` of `W_n` with `f(Q_k) = f(W_{n−k})`. Hence
`min_{≤k cuts} f(W_n) ≤ f(W_{n−k})`, and at `k=n`, XY can force `f = f(W_0) = 1` (so the LB floor
`1` is tight: `min_{XY} f = 1/D_n` once (LBL) is proven).

*Proof.* Induction on `k`. `Q_0 = W_n`. Given `Q_{k}` with visible multiset `W_{n−k}` (in the
sense that after removing P1-invisible matched pairs the alternating sum equals `f(W_{n−k})`),
bisect one physical copy of the current top value `2^{n−k}` into `{2^{n−k−1}, 2^{n−k−1}}`. By
Lemma 3.1 with `V = 2^{n−k}`, `V_1 = V_2 = 2^{n−k−1}`, `m = 2^{n−k−1}`, the two bands
`B_low = [0, 2^{n−k−1})` and `B_high = [2^{n−k−1}, 2^{n−k})` together cover all of `[0, 2^{n−k})`:
bisection flips the count parity on the entire support of that piece, i.e. it *removes* the piece
`2^{n−k}` from the visible multiset and inserts a matched pair `{2^{n−k−1}, 2^{n−k−1}}`, which is
P1-invisible (`layer-cake` consequence: matched pairs leave `M` unchanged). Concretely, starting
from `W_{n−k} = {2^{n−k}, 2^{n−k−1}, …, 2^0}`, bisecting `2^{n−k}` yields the physical multiset
`{2^{n−k−1}, 2^{n−k−1}, 2^{n−k−1}, 2^{n−k−2}, …, 2^0}`; two of the three copies of `2^{n−k−1}` form
an invisible matched pair, leaving visible multiset `{2^{n−k−1}, 2^{n−k−2}, …, 2^0} = W_{n−k−1}`.
Thus `f(Q_{k+1}) = f(W_{n−k−1})`. This uses one cut, so `Q_k` uses `k` cuts. At `k=n`,
`f(Q_n) = f(W_0) = 1`. ∎

Combined with the certified upper bound `min_{XY} f ≤ 1/D_n` (which already implies
`min_{≤n cuts} f(W_n) ≤ 1`), the ANSWER is pinned:
```
    c(n) = 2^n/(2^{n+1} − 1),
```
**contingent on (LBL)** for the matching lower bound. Verification of the answer: for `n=1`,
`c = 2/3`; the certified upper bound gives `≤ 2/3`, and the LB dyadic marking `{1/3, 2/3}` forces
`f ≥ 1/3` after XY's single cut (checked directly: any cut of `{1,2}` in integer units keeps
`f ≥ 1` — e.g. bisecting `2` gives `{1,1,1}`, `f=1`; cutting `2→(a,2−a)` gives sorted
`{2−a or a…}` with `f≥1`), so `c(1) = 2/3` exactly. Endpoint checks `n=2: 4/7`, `n=3: 8/15`,
`n=4: 16/31` all match the numerically confirmed minima.

---

## 5. Structural lemma: an uncut piece always survives (proven)

**Lemma 5.1 (uncut survivor).** Every ≤`n`-cut refinement `Q` of `W_n` leaves at least one of the
`n+1` original pieces `2^0, …, 2^n` uncut (i.e. present intact in `Q`).

*Proof.* Suppose piece `2^i` is cut into `r_i ≥ 1` sub-pieces; the number of cuts is
`Σ_{i=0}^n (r_i − 1) ≤ n`, so `Σ_{i=0}^n r_i ≤ 2n+1`. There are `n+1` summands, each `≥ 1`. If
every `r_i ≥ 2`, then `Σ r_i ≥ 2(n+1) = 2n+2 > 2n+1`, a contradiction. Hence some `r_i = 1`. ∎

---

## 6. Two proven cases of (LBL)

**Lemma 6.1 (top-uncut case).** If the top piece `2^n` is uncut in `Q`, then `f(Q) ≥ 2^{n−1} ≥ 1`.

*Proof.* Every other piece of `Q` is a sub-piece of some `2^i` with `i ≤ n−1`, hence has length
`≤ 2^{n−1} < 2^n`. So `2^n` is the *unique* strict maximum of `Q`. By (F2),
`f(Q) = 2^n − f(Q ∖ {2^n})`. The multiset `R := Q ∖ {2^n}` is a refinement of
`{2^0, …, 2^{n−1}}`, whose pieces are all `≤ 2^{n−1}`, so `max(R) ≤ 2^{n−1}`; by (F1),
`f(R) ≤ max(R) ≤ 2^{n−1}`. Therefore `f(Q) ≥ 2^n − 2^{n−1} = 2^{n−1} ≥ 1` (as `n ≥ 1`). ∎

**Lemma 6.2 (all-bisection case).** If every cut XY makes is a bisection of a distinct original
piece (each `2^i` either uncut or split once into two equal halves), then `f(Q) ≥ 1`.

*Proof.* Let `S ⊆ {0,…,n}` be the set of bisected pieces (`|S| ≤ n`). Bisecting `2^i` replaces it
by the matched pair `{2^{i−1}, 2^{i−1}}`, which is P1-invisible (Lemma 3.1 with `V_1=V_2`: the two
bands cover `[0,2^i)`, removing `2^i` from the visible multiset and adding an invisible pair).
Hence the visible multiset of `Q` is `{2^i : i ∉ S}`, a set of *distinct* powers of two, say
`2^{a_1} > 2^{a_2} > ⋯ > 2^{a_r}` (`r = n+1−|S| ≥ 1`). Then
`f = 2^{a_1} − 2^{a_2} + ⋯ ± 2^{a_r}`. Since `2^{a_1} > 2^{a_1} − 1 = Σ_{j < a_1} 2^j ≥
2^{a_2} + 2^{a_3} + ⋯ + 2^{a_r} ≥ |−2^{a_2} + 2^{a_3} − ⋯|`, we get
`f = 2^{a_1} + (−2^{a_2}+⋯) > 2^{a_1} − (2^{a_2}+⋯) ≥ 2^{a_1} − (2^{a_1}−1) = 1 − (\text{slack}) `;
more carefully, `f > 0` and `f ∈ ℤ`, so `f ≥ 1`. (Integer positivity: `f` is an integer alternating
sum of distinct powers of two, and the displayed inequality gives `f > 0`.) ∎

*Remark.* Lemma 6.2 is subsumed by the certified integer-parity result (`integer-parity-alt-sum`):
an all-bisection `Q` has all-integer pieces and `Σ = D_n` odd, so `f ≡ Σ ≡ 1 (mod 2)` and `f ≥ 0`,
whence `f ≥ 1`. It is recorded here only to fix the base structure of the intended budget induction.

---

## 7. The intended budget induction and the OPEN GAP (honest)

**Intended induction.** Order XY's cuts as a chain `W_n = Q_0 → Q_1 → ⋯ → Q_k` (`k ≤ n`), each an
application of Lemma 3.1. The plan was to prove, by induction on `i`, that
```
    (★)   f(Q_i) ≥ f(W_{n−i}) ,
```
so that at `i = k ≤ n`, `f(Q_k) ≥ f(W_{n−k}) ≥ f(W_0) = 1`. The base `i=0` is `f(W_n) ≥ f(W_n)`.
The step needs a **per-cut lemma**: from `f(Q_{i−1}) ≥ f(W_{n−i+1})` and the reachability of
`Q_{i−1}` with `i−1` cuts, conclude `f(Q_i) ≥ f(W_{n−i})`.

**The proposed driver is FALSE (refuted).** The spec proposed to prove the step by bounding the
single-cut *decrease*: "`f(Q_{i−1}) − f(Q_i) ≤ f(W_{n−i+1}) − f(W_{n−i})` (the Jacobsthal
decrement `D_i`)". This is **false**. Numerically (n=4), the maximum single-cut drop from a config
reachable with `i−1` cuts is far above `D_i`:

| `i` | `D_i = f(W_{n−i+1})−f(W_{n−i})` | observed max single-cut drop |
|-----|-------------------------------|------------------------------|
| 1   | 6                             | 6                            |
| 2   | 2                             | 10                           |
| 3   | 2                             | 14                           |
| 4   | 0                             | 14                           |

Explicit refuting instance (reachable from `W_4` with 3 cuts):
```
    Q' = { 16, 4, 3.567, 2.115, 2, 1.885, 1, 0.433 },   f(Q') ≈ 14.134,
```
and a *single* further cut yields `f ≈ 1.866` — a drop of `≈ 12.27`, whereas the Jacobsthal
decrement available at `i=4` is `D_4 = f(W_1) − f(W_0) = 0`. So no local per-cut decrement bound of
the proposed form can hold, and the induction cannot be driven by tracking `f` alone. (The
reachability constraint on `Q'` did not prevent `f(Q')` from rising to `14.13 > f(W_4)=11`: cuts
can *raise* `f` by creating new top odd-bands, then a later cut collapses many bands at once.)

**What is actually true (verified, but global).** For every config `Q'` reachable from `W_n` with
`i−1` cuts, the best single further cut still respects the floor:
```
    (D)   min over single cuts (Q' → Q) of f(Q) ≥ f(W_{n−i})     (0 violations, n=4, all i).
```
Statement (D) — the *per-cut domination floor* — is the correct per-cut form of `(★)` and is the
sole remaining gap. But (D) is **not local**: as the refutation shows, `(D)` cannot follow from the
value `f(Q')` plus a decrement bound; it needs the global odd-band structure of `Q'`. Proving (D)
is therefore essentially as hard as proving (LBL) directly, and — via the top-piece dichotomy below
— it coincides with the field's long-standing crux, not a genuinely new sub-problem.

**Reduction of the gap to the classical Case B.** By Lemma 6.1, if the top piece `2^n` is uncut in
`Q`, then `f(Q) ≥ 1`. So (LBL) reduces to:
```
    (LBL-B):  every ≤n-cut refinement Q of W_n in which the top piece 2^n IS cut has f(Q) ≥ 1.
```
This is exactly round-1's Case B / round-2's "budget non-fungibility" wall: once `2^n` is split,
`max(Q) ≤ 2^{n−1}` and the (F2) peel no longer dominates, and the `≥1` cuts spent on the top are
entangled with the `≤ n−1` cuts elsewhere. The cut-budget framing does not dissolve this coupling;
the refutation of the decrement mechanism shows precisely why a per-cut monovariant on `f` cannot.

**Precise open statement (the gap this approach leaves).**
> Prove **(D)**: for every config `Q'` reachable from `W_n` by `i−1` cuts (`1 ≤ i ≤ n`), every
> single additional cut `Q' → Q` satisfies `f(Q) ≥ f(W_{n−i})`. Equivalently prove **(LBL-B)**.
> A proof must use the global odd-band profile of the reachable config, since (§7) the local
> per-cut decrement is unbounded by the remaining Jacobsthal budget.

**Consequence for the field (record).** The cut-budget framing is *alive* at the endpoint (the
identity `min_{≤k cuts} f(W_n) = f(W_{n−k})` is confirmed exactly for `n=3,4`) but its proposed
*induction driver* is refuted. Future work on this slug should either (a) strengthen the IH `(★)`
to carry the full odd-band profile of `Q_i` (not just `f`), i.e. a monovariant on the count
function rather than its integral; or (b) accept that the gap is the classical Case B and attack it
by a structural argument on `2^n`'s sub-pieces (which of the `≤ n−1` remaining cuts must land in
the top block). This is genuinely different information from the two integrality routes and should
be kept in the population as the non-integrality framing, with the mechanism corrected.

---

## Full proof
Not present — Status is `partial`. Proven this round: the reduction (imported), the Jacobsthal
scaffold (Lemma 2.1), the two-band per-cut identity (Lemma 3.1), tightness of the floor
(Lemma 4.1, pinning the answer contingent on (LBL)), the uncut-survivor lemma (5.1), and (LBL) in
the top-uncut case (6.1) and all-bisection case (6.2). Open gap: (D) / (LBL-B) — the top-cut case,
which this round shows cannot be closed by the naive per-cut decrement (explicit refutation §7).

## Promotable lemmas

- **Two-band single-cut identity (Lemma 3.1).** *For any multiset `Q`, replacing a piece `V` by
  `V_1 ≤ V_2` (`V_1+V_2=V`, `m=V_1`) flips the parity of `c_Q(t)` exactly on `[0,m) ∪ [V−m, V)`,
  each of length `m`, so `f(Q')−f(Q) = Δ_low+Δ_high` with each band term in `[−m,m]`; hence
  `|f(Q')−f(Q)| ≤ 2m ≤ V`.* Proved in full in §3 from certified `layer-cake-alt-sum`. Reusable
  discrete companion to certified Lemma I.
- **Uncut survivor (Lemma 5.1).** *Every ≤n-cut refinement of `W_n` (n+1 pieces) leaves at least
  one original piece uncut.* Proved in §5 (pigeonhole on `Σ r_i ≤ 2n+1`).
- **Top-uncut floor (Lemma 6.1).** *If `2^n` is uncut in a refinement `Q` of `W_n`, then
  `f(Q) ≥ 2^{n−1} ≥ 1`.* Proved in §6 via (F2) peel and `f(R) ≤ max(R)`. (Matches certified
  round-1 Case A; re-proved cleanly here.)
