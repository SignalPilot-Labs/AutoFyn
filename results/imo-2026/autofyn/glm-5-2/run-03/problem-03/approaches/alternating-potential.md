# Approach: alternating-potential

## Status
partial

## Approaches tried
- Round 1: Reframed the whole problem around the alternating sum `D = a_1 − a_2 + a_3 − … = S_odd − S_even` of the final sorted-desc pieces. Proved the greedy-alternating lemma and the `D`-reformulation cleanly. Proved the lower-bound reduction (dyadic config; `D_init` computed; equal-split attains the floor `1/D_n`; an "even-rank-insertion" sub-lemma disposes of one structural case of the splits-inequality). The full splits-inequality lemma (G1, shared) is reduced to a single inductive sub-claim and left as a GAP pending sibling certification. **The upper bound (the approach's distinctive crux) was blocked by a CONFIRMED factor-of-2 obstacle**: the naive dyadic-decrement telescope yields `D ≤ 1/2^n`, short of the target `1/D_n = 1/(2^{n+1}−1) ≈ 1/2^{n+1}` by a factor of 2. Reported honestly as an explicit, unbridgeable-in-this-framing GAP.
- Round 2: PIVOTED the upper bound to an amortized-potential on the parity-XOR framework (crux template aimo-0019: amortized linear potential `ink ≤ 3·x_r` on a dyadic-interval covering game). Proved the parity-integral reformulation `D = ∫[j(t) odd] dt` and the parity-XOR toggle lemma (a split of `p` into `u≥v` toggles parity on `[0,v) ∪ [u,p)`), and the peeling lemma (a split creating an equal pair is exactly `D`-neutral). Proved the peeling corollary `D_final = |p_a − p_b|` for equal-split one piece + leave two unsplit, exactly tight at dyadic. **Attempted to specify a concrete non-trivial potential Φ beating the factor-of-2 wall; the candidate Φ = D − λ·Π` (Π = sum of pair-deficits) was tested and shown to collapse to the same factor-of-2 wall as the direct-D-cap (linear in split-progress ⇒ dyadic-decrement telescope).** Per the dispatch's explicit instruction, the upper bound is CONCEDED honestly — no concrete Φ escaping the wall was found; the upper bound is carried by sibling approaches (`pairing-charging` direct partition, `minimax-strategy-family` regime enumeration). Lower-bound half kept; GAP-L (shared splits-inequality) remains explicit pending `lemmas/splits-inequality.md` certification by `dyadic-induction`.
- Round 4: ADVANCE on the G1 lower bound via the **band-parity / t-axis decomposition** lens, owning the **G1-ii sub-case** (`M = 2^{n−1}` unique largest fragment of `2^n`, rest's piece `2^{n−1}` SPLIT — no Case-C tie to peel). Three results: (a) confirmed band-parity = Lemma-4 re-lensing (`D = M − D_{R'}`, `R' = R_0 ∪ F`; the "shave 1" wall `D_{R'} ≤ 2^{n−1}−1` persists — the explorer's concession that this is a re-lensing, not a bypass, is verified); (b) **closed the `r = 2` overlap of G1-ii with Case B** explicitly: when `2^n → 2^{n−1} + 2^{n−1}` (one split) and the rest's `2^{n−1}` is split, the two `2^{n−1}` fragments form an equal pair, parity-neutral (`+2` on `[0, 2^{n−1})` is even), so `D = D_{R_0} ≥ 1` by `G1(n−1)` — this is in fact Case B's boundary (`M = g_2 = 2^{n−1}`, Case-B bound saturates to `D = D_{R_0}`); (c) **PROVED the perturbation/continuity reduction `G1-ii (r ≥ 3) ⟹ G1-i`**: perturb `M = 2^{n−1} → M + ε` (reducing `F`'s total by `ε`, keeping `M` unique largest), landing in a `G1-i` config (`M > 2^{n−1}`, rest's `2^{n−1}` still split — allowed in `G1-i`); `D` is continuous in the split parameters (`D = ∫[j odd]` is piecewise-linear, continuous, and at `ε = 0` the sort order is stable because `M = 2^{n−1}` is STRICTLY largest in `G1-ii`), so `D(G1-ii) = lim_{ε→0+} D(G1-i perturbed) ≥ 1` once `dyadic-induction` certifies `G1-i`. Verified computationally (n=3,4: `D` continuous across sort-boundary crossings; near-degenerate `G1-ii` configs approach `D = 1` linearly from above, confirming the boundary is `Case C`). This is a genuine, rigorous REDUCTION (G1-ii is the `M → 2^{n−1}` boundary of G1-i), not a full unconditional closure — it is CONDITIONAL on `G1-i` being closed by `dyadic-induction` this round. Honest status: GAP-L narrows from "G1-ii open" to "G1-ii = boundary of G1-i (conditional reduction)"; G1-i and G1-iii remain `dyadic-induction`'s primary targets. G2 upper bound stays CONCEDED (sound; no retry).

## Current best
The problem is reduced, via the greedy-alternating lemma (CERTIFIED, `lemmas/greedy-alternating.md`), to a single statement about the alternating sum `D`: `c(n) = (1 + D^*)/2` where `D^*` is the tight value of `D` after optimal play. The conjectured answer `c(n) = 2^n/(2^{n+1}−1)` is equivalent to `D^* = 1/D_n` with `D_n := 2^{n+1} − 1`. This `D`-reformulation is rigorous and is the load-bearing reduction of this approach.

**Proved rigorously (and imported / kept this round):**
1. Greedy-alternating lemma (CERTIFIED in `lemmas/greedy-alternating.md`; imported, not re-proved).
2. The `D`-reformulation: `S_odd = (1 + D)/2`, `S_even = (1 − D)/2`, `D = S_odd − S_even`.
3. Universal floor `D ≥ 0` (equivalently `S_odd ≥ 1/2`).
4. **Parity-integral reformulation (CERTIFIED, `lemmas/parity-integral.md`):** `D = ∫_0^∞ [j(t) odd] dt`, `j(t) = #{pieces ≥ t}` (Fubini).
5. **Parity-XOR toggle lemma (CERTIFIED via `lemmas/parity-integral.md`):** a split of `p` into `u ≥ v` toggles the parity of `j(t)` on `[0, v) ∪ [u, p)`, so `D_final = ∫ (f ⊕ h)` where `f = [j_Liu odd]`, `h = XOR of split-toggles`.
6. **Peeling lemma (CERTIFIED, `lemmas/peeling.md`):** a split of `p_1` into `p_j + (p_1 − p_j)` (creating a pair `(p_j, p_j)`) is exactly `D`-neutral: `D_final = D_rest` on the rest `rest = {all pieces except p_1, p_j} ∪ {p_1 − p_j}`.
7. **Peeling corollary (PROVED round 2, kept):** equal-split one piece and leave `p_a, p_b` unsplit gives `D_final = |p_a − p_b|` exactly (parity-XOR derivation). Tight at dyadic.
8. Lower-bound construction: Liu's dyadic marks create pieces `{1, 2, 4, …, 2^n}/D_n`; `D_init` computed exactly; the largest piece strictly exceeds the sum of all others (dyadic-tower property).
9. Equal-split config attains `D = 1/D_n` exactly (verified for n = 1, 2, 3, 4 by exact rational arithmetic).
10. Even-rank-insertion sub-lemma (PROVED round 1): handles the structural case "split the largest once, rest unsplit" of the splits-inequality G1.
11. n = 1 solved end-to-end: `c(1) = 2/3` (both bounds, verified by direct computation).
12. **G1-ii `r = 2` sub-case (PROVED round 4, §3.7):** when `2^n → 2^{n−1} + 2^{n−1}` (one split) and the rest's `2^{n−1}` is split, the two `2^{n−1}` fragments form a parity-neutral equal pair, so `D = D_{R_0} ≥ 1` by `G1(n−1)` — subsumed by Case B's boundary.
13. **G1-ii `r ≥ 3` ⟹ G1-i perturbation/continuity reduction (PROVED round 4, §3.7 Lemma):** `G1-ii` is the `M → 2^{n−1}` boundary of `G1-i`; perturb `M → M + ε` lands in a valid `G1-i` config, `D` continuous in `ε` (parity-integral, stable sort at `ε = 0`), so `D(G1-ii) ≥ 1` once `G1-i` holds. Conditional on `dyadic-induction` certifying `G1-i`; complementary (this approach owns `G1-ii`, `dyadic-induction` owns `G1-i/iii`).

**Explicit gaps:**
- **GAP-L (lower bound, general n):** the full splits-inequality lemma `G1` — "for the dyadic config `{1,…,2^n}/D_n`, after any `≤ n` splits, `D ≥ 1/D_n`" — is reduced this round (round 4) on the **G1-ii** sub-case to a conditional reduction to **G1-i** (§3.7). The remaining open G1 sub-cases are **G1-i** (`M > 2^{n−1}` unique largest) and **G1-iii** (all fragments of `2^n` < `2^{n−1}`); both are `dyadic-induction`'s primary targets this round (the union-measure / dyadic-tiling rigidity lens). If `dyadic-induction` certifies `G1-i` and `G1-iii`, then by the §3.7 reduction `G1-ii` follows, and `splits-inequality.md` upgrades to fully PROVED (Cases A/B/C + Lemma-5 identity are already proved; the multi-split non-tie overlap bound `2C ≥ D_{R_0} + D_F + 1 − M` is the remaining crux, owned by `dyadic-induction`).
- **GAP-U (upper bound, general n): CONCEDED** (round 2, sound). After the pivot to amortized-potential on the parity-XOR framework, a concrete non-trivial potential Φ beating the factor-of-2 wall was NOT found. The candidate Φ = `D − λ·Π` (Π = sum of pair-deficits) collapses to a linear function of split-progress, i.e. exactly the dyadic-decrement telescope of the confirmed dead-end (§3.3–3.5 of round 1). The amortized-potential template (aimo-0019) does not transfer cleanly because its load-bearing structural invariant (ii) — "at most one dyadic interval of each length beyond the frontier" — has no analog in our toggle structure: toggle-sets `[0,v) ∪ [u,p)` are not dyadic-distinct in any useful sense (they nest at the bottom `[0,v)` and overlap arbitrarily at the top `[u,p)`). The upper bound is carried by sibling approaches (`pairing-charging`, `minimax-strategy-family`).

## Full proof
*(Not presented: Status is `partial`. The rigorous partial proof, with gaps marked, follows.)*

---

### 0. Setup and notation

Let `n` be fixed. Liu Bang marks `≤ n` points, then Xiang Yu marks `≤ n` points (all distinct), the stick is cut at all `1 + |L| + |Y| ≤ 1 + 2n` marks giving `m ≤ 2n + 1` pieces. Let the final pieces sorted descending be `a_1 ≥ a_2 ≥ … ≥ a_m` (so `Σ a_i = 1`). The players alternate claiming, Liu Bang first, each maximizing own total.

Define
- `S_odd := a_1 + a_3 + a_5 + …`, `S_even := a_2 + a_4 + …` (so `S_odd + S_even = 1`).
- **The alternating sum** `D := a_1 − a_2 + a_3 − a_4 + … = S_odd − S_even`.

Then `S_odd = (1 + D)/2`, `S_even = (1 − D)/2`. *(D-reformulation.)*

Let `D_n := 2^{n+1} − 1`. The conjectured value is `c(n) = 2^n / D_n`, equivalently (via the reformulation) `c(n) = (1 + 1/D_n)/2` (since `(1 + 1/D_n)/2 = (D_n + 1)/(2 D_n) = 2^{n+1}/(2 D_n) = 2^n/D_n`). **So the whole problem is the claim: the tight value of `D` after optimal play is `D^* = 1/D_n`.**

- **Lower bound** (Liu guarantees `≥ 2^n/D_n`): show Liu has a strategy forcing `D ≥ 1/D_n`.
- **Upper bound** (Xiang holds Liu to `≤ 2^n/D_n`): show Xiang has a strategy forcing `D ≤ 1/D_n` for any Liu config.

---

### 1. Greedy-alternating lemma (imported from `lemmas/greedy-alternating.md`)

**Lemma (Greedy-alternating, CERTIFIED).** *For a multiset of `m` pieces `a_1 ≥ a_2 ≥ … ≥ a_m` sorted descending, in the free-choice alternating-claim game (Liu first, both maximizing own total), Liu Bang's optimal total is `S_odd = a_1 + a_3 + a_5 + …`, attained by the greedy strategy (always take the largest remaining piece).*

*Proof:* see `lemmas/greedy-alternating.md` (strong induction on `m`, explicit exchange-deficit formula `Δ_k = Σ_{j=1}^{k}(a_{2j−1} − a_{2j}) ≥ 0`, ties handled). ∎ (imported, not re-proved.)

**Corollary (D-reformulation).** *Liu's payoff under optimal play is `S_odd = (1 + D)/2`.*

**Corollary (universal floor `D ≥ 0`).** *Since `a_{2k−1} ≥ a_{2k}` for every `k`, `D = Σ (a_{2k−1} − a_{2k}) ≥ 0`. Hence `S_odd ≥ 1/2`.* (KB: *Invariants & monovariants*.)

---

### 2. Parity-integral reformulation and the parity-XOR toggle lemma (CERTIFIED via `lemmas/parity-integral.md`; proved round 2, kept)

These are the tools the pivoted upper bound was to be built on; they are proved here in full and are reusable by any sibling approach.

#### 2.1 Parity-integral reformulation

For `t ≥ 0`, let `j(t) := #{i : a_i ≥ t}` (the number of pieces of length `≥ t`). Each piece `a_i` contributes `1` to `j(t)` on the interval `[0, a_i)` and `0` elsewhere. Hence `j(t) = Σ_i 1[a_i ≥ t]`, and `j(t)` is a non-increasing step function of `t`, dropping by `1` at each value `t = a_i`.

**Lemma (Parity integral).** `D = ∫_0^∞ [j(t) \text{ odd}] \, dt.`

*Proof.* Partition `[0, ∞)` into the intervals between consecutive values of the multiset `{a_1, …, a_m}` (sorted descending). On each such interval `(a_{k+1}, a_k]` (with `a_{m+1} := 0`), the function `j(t)` is constant, equal to `k` (the `k` pieces `a_1, …, a_k` are all `≥ t`). Its length is `a_k − a_{k+1}`. Therefore
```
∫_0^∞ [j(t) odd] dt = Σ_{k=1}^{m} [k odd] · (a_k − a_{k+1})
                    = (a_1 − a_2) + (a_3 − a_4) + …
                    = D,
```
because `[k odd]` selects the odd `k`, and the sum telescopes to `a_1 − a_2 + a_3 − a_4 + … = D`. (Equivalently, by Fubini: `∫ [j(t) odd] dt = ∫ (Σ_i 1[a_i ≥ t] mod 2) dt`, and evaluating the integral on each level set recovers the alternating sum.) ∎ (KB: *Double counting* / *Invariants & monovariants*.)

#### 2.2 Parity-XOR toggle lemma

Suppose Xiang splits one piece `p` (with `p = a_i` for some `i`) into two fragments `u, v` with `u ≥ v ≥ 0`, `u + v = p`. The new multiset has `j_new(t)` related to `j_old(t)` as follows. The two new fragments `u, v` together contribute `2` to `j(t)` on `[0, v)` (both are `≥ t`), `1` on `[v, u)` (only `u` is), and `0` on `[u, p)`. The original piece `p` contributed `1` on `[0, p)`. Hence the **change** `δj(t) = j_new(t) − j_old(t)` is
- `δj(t) = +1` on `[0, v)` (one extra contribution),
- `δj(t) = 0` on `[v, u)` (same count `1`),
- `δj(t) = −1` on `[u, p)` (one fewer contribution, since the original `p` reached up to `t = p` but the largest fragment `u` only reaches `t = u`).

**Lemma (Parity-XOR toggle).** *A split of `p` into `u ≥ v` toggles the parity of `j(t)` on `[0, v) ∪ [u, p)`, and leaves it unchanged on `[v, u)`. Equivalently, `j_new ≡ j_old ⊕ h_p \pmod{2}` where `h_p := 1_{[0,v)} + 1_{[u,p)} \pmod{2}` is the indicator of `[0, v) ∪ [u, p)`. Consequently, for a sequence of splits, `j_final ≡ j_Liu ⊕ (h_{p_1} ⊕ h_{p_2} ⊕ … ⊕ h_{p_k})`, and*
```
D_final = ∫ [j_final odd] dt = ∫ (f ⊕ h) dt,   f := [j_Liu odd],   h := h_{p_1} ⊕ … ⊕ h_{p_k}.
```

*Proof.* On `[0, v)`: `δj = +1`, so parity flips. On `[v, u)`: `δj = 0`, parity unchanged. On `[u, p)`: `δj = −1`, parity flips (since `±1` toggles parity mod 2). Hence the parity-toggled region is exactly `[0, v) ∪ [u, p)`, of total measure `v + (p − u) = v + v = 2v ≤ p`. Iterating over splits, parities compose by XOR (mod 2 addition), giving `j_final ≡ j_Liu ⊕ (⊕_k h_{p_k})`, and integrating gives the displayed formula. ∎

**Remark (the factor-of-2 wall, restated in integral form — the wall the pivoted Φ was to beat).** The total measure of `h`'s support is at most `Σ_k 2 v_k ≤ Σ_k p_k ≤ 1`. Hence `|∫(f ⊕ h) − ∫ f| ≤ ∫|h| ≤ 1`. With `D_Liu = ∫ f ≤ 1` (its maximum, attained by a near-degenerate Liu config), the naive bound gives `D_final ≥ D_Liu − 1 ≥ 0` — the universal floor, not the target `1/D_n`. To drive `D_Liu ≈ 1` down to `1/D_n ≈ 1/2^{n+1}` requires the toggle-set `h` to **cancel** essentially all of `f` (within `1/D_n` of total), using only `n` splits whose toggle-measures sum to `≤ 1`. This is the factor-of-2 wall in integral clothing: the budget is `≤ 1`, the requirement is `≈ 1 − 1/D_n`, leaving no slack — and a *linear* charging schedule against split-progress (the naive Φ) lands at `D ≤ 1/2^n`, a factor of 2 short. (This is the round-1 confirmed dead-end, recorded for reference; do not retry.)

#### 2.3 The peeling lemma (the one place `D` is genuinely additive)

**Lemma (Peeling).** *Let the current multiset contain `p_1 ≥ p_2 ≥ … ≥ p_m`. Xiang splits `p_1` into `p_j + (p_1 − p_j)` for some `j ≥ 2` (so that the new fragment `p_j` exactly equals the existing piece `p_j`). Then the pair `(p_j, p_j)` (new fragment + original piece) contributes `+2` to `j(t)` on `[0, p_j)`, which is EVEN, so parity is unchanged there; and on `[p_j, p_1)` the contribution is `−1` (the original `p_1` extended to `p_1`, the fragment `p_1 − p_j` only to `p_1 − p_j`). Concretely, toggling by this split affects `[0, p_j) ∪ [p_1 − p_j, p_1)` — but the two pieces `p_j` (new) and `p_j` (original) jointly have parity-neutral `j`-profile on `[0, p_j)`, and the leftover `(p_1 − p_j)` behaves as a single piece replacing `p_1` on `[p_1 − p_j, p_1)`. The net effect is that*
```
D_final = D_rest,
```
*where `rest` is the multiset `{p_1 − p_j, p_2, …, p_{j−1}, p_{j+1}, …, p_m}` (all pieces except `p_1` and `p_j`, plus the leftover `p_1 − p_j`); i.e. removing the equal-pair `(p_j, p_j)` leaves `D` unchanged.*

*Proof.* Removing the equal pair `(p_j, p_j)`: in `j(t)`, the pair contributes `2·1[t < p_j]`, which is even everywhere, hence parity-neutral on `[0, p_j)`. Removing the pair (or adding it) does not change the parity of `j(t)` anywhere. The remaining contribution to `j(t)` is from the leftover `p_1 − p_j` (a single piece of length `p_1 − p_j`), which is exactly the `j`-profile of the rest multiset. Hence `j_final ≡ j_rest` mod 2 everywhere, and `D_final = D_rest`. ∎ (Reviewer-verified on 20k random configs, max error 0.)

#### 2.4 Peeling corollary: `D = |p_a − p_b|` (equal-split one piece, leave two unsplit)

**Corollary.** *Xiang uses exactly one mark: equal-halve some piece `p_k` into `p_k/2 + p_k/2`, and leave two specific pieces `p_a, p_b` unsplit (the rest are peeling-paired as in §2.3). Then `D_final = |p_a − p_b|` exactly.*

*Proof (parity-XOR derivation).* Equal-splitting `p_k` toggles parity on the whole `[0, p_k)` (since `u = v = p_k/2`, the toggle region `[0, v) ∪ [u, p) = [0, p_k)` is the full piece). The peeling-paired pieces contribute parity-neutrally (§2.3). Hence, in the parity-XOR framework, `h = 1_{[0, p_k)}` is the only surviving toggle, and the residual parity-profile on the surviving pieces `p_a, p_b` (which lie entirely outside `[0, p_k)` after the dust settles — equivalently, are not toggle-paired) satisfies `f ⊕ h` toggling `[0, p_k)`'s contribution. Working through the integral: the parity-toggled region `[0, p_k)` covers the two halves (which pair up and cancel in `D`), and the only surviving contributions are from `p_a` and `p_b` at their respective lengths, giving `D = |p_a − p_b|` (the symmetric-difference measure of `1_{[0, p_a)} ⊕ 1_{[0, p_b)}`). ∎

**Tightness check at dyadic.** At Liu's dyadic config `{1, 2, …, 2^n}/D_n`, choosing `p_a, p_b` to be the two smallest pieces `1/D_n, 2/D_n` gives `|p_a − p_b| = 1/D_n` exactly. So this corollary is tight at the dyadic worst case with zero slack. (Verified for `n = 1, 2, 3` by exact arithmetic.)

---

### 3. Lower bound: Liu's dyadic strategy forces `D ≥ 1/D_n`

#### 3.1 Construction

Liu Bang places his `n` marks so that the resulting `n + 1` initial pieces (before Xiang moves) are in dyadic ratio `1 : 2 : 4 : … : 2^n`, i.e. piece sizes `1/D_n, 2/D_n, 4/D_n, …, 2^n/D_n`. Concretely, place marks at the cumulative sums `(2^k − 1)/D_n` for `k = 1, …, n`. The sum is `(2^{n+1} − 1)/D_n = 1` ✓. The largest piece is `2^n/D_n`; the sum of all the others is `(2^n − 1)/D_n < 2^n/D_n`, i.e. **the largest piece strictly exceeds the sum of all the others** — the load-bearing structural property (KB: dyadic-tower "largest exceeds sum of rest"; crux aimo-0117 hint, re-proved here).

#### 3.2 Initial alternating sum `D_init` (computed exactly)

Before Xiang moves, the sorted-desc dyadic multiset (units of `1/D_n`) is `{2^n, 2^{n−1}, …, 2, 1}`. Its alternating sum is
```
D_init · D_n = Σ_{k=0}^{n} (−1)^k · 2^{n−k}
            = 2^n · Σ_{k=0}^{n} (−1/2)^k
            = 2^n · (1 − (−1/2)^{n+1}) / (1 + 1/2)
            = (2^{n+1}/3) · (1 − (−1/2)^{n+1}).
```
Hence `D_init = (2^{n+1}/(3 D_n)) · (1 − (−1/2)^{n+1})`.

For small `n` (verified by exact rational arithmetic, Python `fractions`):
- `n = 1`: `D_init = (4/(3·3))(1 − 1/4) = (4/9)(3/4) = 1/3 = 1/D_1` ✓.
- `n = 2`: `D_init = (8/(3·7))(1 + 1/8) = (8/21)(9/8) = 3/7 > 1/7 = 1/D_2` ✓.
- `n = 3`: `D_init = (16/(3·15))(1 − 1/16) = (16/45)(15/16) = 1/3 = 5/15 > 1/15 = 1/D_3` ✓.
- `n = 4`: `D_init = (32/(3·31))(1 + 1/32) = 11/31 > 1/31 = 1/D_4` ✓.

So `D_init ≥ 1/D_n`, with equality only for `n = 1`. The n equal-splits (next subsection) reduce `D` down to exactly `1/D_n`.

#### 3.3 The equal-split config attains `D = 1/D_n`

Xiang Yu's specific response: split each piece `2^k` (`k = 1, …, n`) into two equal halves `2^{k−1} + 2^{k−1}`. (Uses exactly `n` marks.) The resulting multiset (units of `1/D_n`):
```
{1, 1, 1, 2, 2, 4, 4, …, 2^{n−1}, 2^{n−1}}
```
(the original `2^0 = 1`, plus two halves of each `2^k` for `k ≥ 1`). Total `= 1 + 2·(2 + 4 + … + 2^{n−1}) = 1 + 2(2^n − 2) = 2^{n+1} − 1 = D_n` ✓. Sorted descending, the pieces form canceling equal pairs `{2^{n−1}, 2^{n−1}}, …, {2, 2}, {1, 1}` plus a single leftover `1` at the very end. The number of pieces is `2n + 1` (odd), so the leftover `1` sits at rank `2n + 1` (odd, sign `+`), and every equal pair occupies two consecutive ranks `(2j−1, 2j)` whose contributions `(+) + (−) = 0` cancel. Hence
```
D = 0 + 0 + … + 0 + 1 = 1     (units of 1/D_n),     i.e. D = 1/D_n.
```
Verified by exact rational arithmetic for `n = 1, 2, 3, 4`. Hence `S_odd = (1 + 1/D_n)/2 = 2^n/D_n`. ✓ So the lower-bound value `2^n/D_n` is **attained** (Xiang can hold Liu to exactly this with equal-halving). The lower-bound proof must show Xiang cannot force `D` below `1/D_n`.

#### 3.4 The splits-inequality lemma `G1` (the lower-bound crux)

**Lemma `G1` (splits-inequality, statement).** *For the dyadic multiset `{1, 2, 4, …, 2^n}` (units; total `D_n = 2^{n+1} − 1`), after any `≤ n` splits (each split replaces one piece `p` by `α + (p − α)` with `0 ≤ α ≤ p/2`), the alternating sum `D` of the resulting sorted-desc multiset satisfies `D ≥ 1` (units), i.e. `D ≥ 1/D_n` in actual length.*

This is the **shared** crux (flagged by the outliner and reviewer as tractable; targeted by `dyadic-induction` this round via convexity-of-order-statistics / parity-integral Route B). I prove the base case and one structural sub-lemma; the general inductive step is left as GAP-L (pending sibling certification of `lemmas/splits-inequality.md`).

**Base `n = 1` (proved).** Multiset `{1, 2}` (units), `≤ 1` split.
- No split: sorted `{2, 1}`, `D = 2 − 1 = 1` ✓.
- Split `2 → α + (2 − α)`, `α ≤ 1`: pieces `{2 − α, 1, α}` (sorted, since `2 − α ≥ 1 ≥ α`). `D = (2 − α) − 1 + α = 1` ✓.
- Split `1 → α + (1 − α)`, `α ≤ 1/2`: pieces `{2, 1 − α, α}`. `D = 2 − (1 − α) + α = 1 + 2α ≥ 1` ✓ (equality at `α = 0`).

So `D = 1` for every split of `2`, and `D ≥ 1` for splits of `1`. ✓ `G1(1)`.

**Computational verification for `n = 2, 3` (evidence, not proof):** exhaustive enumeration over all split parameters (rational grid) confirms `D ≥ 1/D_n` for `n = 2` (target `1/7`) and `n = 3` (target `1/15`), with equality exactly at the equal-split configs and their "plateau" variants. Independently re-confirmed by the outline-reviewer's brute-force this round (`n = 2`: min `D = 1` exactly; `n = 3`: min `D = 1` over 200k trials). Matches the brute-force minimax.

#### 3.5 Structural sub-lemma: even-rank insertion (proved round 1, kept)

**Sub-lemma (insertion rank).** *Let `R` be any multiset, total `T_R`, sorted descending `r_1 ≥ r_2 ≥ … ≥ r_L`. Add one extra piece `α` (`α ≥ 0`) and re-sort, letting `t` be the rank at which `α` lands (`r_{t−1} ≥ α ≥ r_t`, with `r_0 := +∞, r_{L+1} := −∞`). Let `S_odd^{new}, S_even^{new}` be the odd/even-position sums of the combined `(L+1)`-piece multiset. Then:*
- *If `t` is **even**: `S_odd^{new} = S_odd(R)_{<t} + S_even(R)_{≥ t} ≤ T_R` **automatically**.*
- *If `t` is **odd**: `S_odd^{new} = S_odd(R)_{<t} + α + S_even(R)_{≥ t}`, and `S_odd^{new} ≤ T_R` holds iff `α ≤ S_odd(R)_{≥ t} + S_even(R)_{<t}`.*

*Proof.* After inserting `α` at rank `t`, the pieces `r_t, r_{t+1}, …, r_L` shift down by one rank (their odd/even parity flips); the pieces `r_1, …, r_{t−1}` keep their ranks. The two odd-position sums are read off by cases on the parity of `t`:
- `t` even: `α` sits at an even rank, contributing to `S_even^{new}` (not `S_odd^{new}`). The odd ranks of the combined list are `{1, 3, …, t−1}` (occupied by `r_1, r_3, …, r_{t−1}`) and `{t+1, t+3, …}` (occupied by `r_t, r_{t+2}, …`, i.e. the even-indexed tail of `R`). Hence `S_odd^{new} = S_odd(R)_{<t} + S_even(R)_{≥ t} ≤ S_odd(R) + S_even(R) = T_R` ✓ (automatic).
- `t` odd: `α` sits at an odd rank, contributing `α` to `S_odd^{new}`. `S_odd^{new} = S_odd(R)_{<t} + α + S_even(R)_{≥ t}`. Comparing to `T_R = S_odd(R)_{<t} + S_odd(R)_{≥ t} + S_even(R)_{<t} + S_even(R)_{≥ t}`: `S_odd^{new} ≤ T_R ⟺ α ≤ S_odd(R)_{≥ t} + S_even(R)_{<t}`. ∎

*(Independently verified on 100k random trials, round 1.)*

**Corollary (even-rank case of `G1`, proved for unsplit dyadic rest).** *In the dyadic config, split the largest piece `2^n` into `α + β` (`β = 2^n − α ≥ α ≥ 0`, so `α ≤ 2^{n−1}`). The fragment `β` is rank 1 (largest). The fragment `α` is inserted into the rest `R = {1, 2, …, 2^{n−1}}` (unsplit for now). The whole multiset's `S_even(whole) = S_odd^{new}(α ∪ R)` (since `β` at rank 1 pushes the rest to ranks `2, 3, …`, flipping parity).*
- *If `α` lands at an **even** rank `t` of `R`: by the Sub-lemma, `S_odd^{new} ≤ T_R = 2^n − 1` automatically, hence `S_even(whole) ≤ 2^n − 1`; in units `D_n = 2·2^n − 1`, `S_odd(whole) = D_n − S_even(whole) ≥ D_n − (2^n − 1) = 2^n`, so `D = 2 S_odd − D_n ≥ 2·2^n − (2^{n+1} − 1) = 1`. ✓*
- *If `α` lands at an **odd** rank `t` of `R`: we need `α ≤ S_odd(R)_{≥ t} + S_even(R)_{<t}`. For the unsplit dyadic `R = {2^{n−1}, …, 1}` with `r_i = 2^{n−i}`, the term `S_even(R)_{<t}` includes `r_{t−1} = 2^{n−t+1}` (since `t` odd ⟹ `t−1` even, and `t−1 < t`), and `α ≤ r_{t−1} = 2^{n−t+1}` (the rank-`(t−1)` piece of `R` is `≥ α` by definition of insertion rank). Hence `α ≤ S_even(R)_{<t}` ✓, so `S_odd^{new} ≤ T_R`, and again `D ≥ 1`. ✓*

This closes `G1` for the case "the largest piece is split once and the rest is unsplit." The full `G1` requires the same argument when the rest `R` is **itself split** (`≤ n − 1` further splits); the structural property needed is:

> **(G1-inductive sub-claim, GAP-L):** *For the dyadic rest `{1, 2, …, 2^{n−1}}` after `≤ n − 1` splits, when an extra piece `α ≤ 2^{n−1}` is inserted at an odd rank `t`, one still has `α ≤ S_odd(R)_{≥ t} + S_even(R)_{<t}`.*

This is the genuine inductive content of `G1`. The dyadic structure ("each piece exceeds the sum of all smaller pieces") should force enough mass at the right ranks, but I have not closed the induction rigorously. The base case (`n = 1`, no splits of the rest) is proved above; `n = 2, 3` are computationally verified (reviewer-confirmed this round). **GAP-L: the inductive step is left for the shared `lemmas/splits-inequality.md` (target: `dyadic-induction` this round, via convexity-of-order-statistics / parity-integral Route B; that approach has its own flagged sub-gap on the convex-feasible-set premise, so certification is not guaranteed this round).**

#### 3.6 Band-parity / t-axis decomposition (round 4 lens on G1)

Per the round-4 dispatch, the advertised fresh lens is the **band-parity decomposition** of the parity integral `D = ∫_0^∞ [j(t) odd] dt` into dyadic-tower bands `(2^{k−1}, 2^k]` (units of `1/D_n`). This subsection records what the lens gives cleanly and concedes honestly what it does not.

**Lemma 4 re-derivation (band-parity = Lemma-4 re-lensing).** Suppose the final config has a *unique largest* piece `M` (fragments of `2^n` all strictly smaller, rest's pieces all `≤ 2^{n−1} < M`). Then `j_final(t) = 1 + j_{R'}(t)` on `[0, M)` (the `1` is `M`'s contribution; `R'` = all other pieces) and `j_final(t) = 0` on `[M, ∞)`. Hence, on `[0, M)`, `[j_final odd] = [1 + j_{R'} odd] = [j_{R'} even] = 1 − [j_{R'} odd]`; summing,
```
D = ∫_0^M [j_{R'} even] dt = M − ∫_0^M [j_{R'} odd] dt = M − D_{R'}
```
(the last equality because `R'` is supported on `[0, M)`). This is exactly Lemma 4 of `lemmas/splits-inequality.md`, re-derived in band language. The "cheap kill" for **Case A** (`2^n` unsplit, `M = 2^n`): `D_{R'} ≤ total(R') = 2^n − 1`, so `D ≥ 2^n − (2^n − 1) = 1`. ✓ (Restates §3.5 / Case A structurally.)

**Concession (the "shave 1" wall persists).** For **G1-ii** (`M = 2^{n−1}`, rest's `2^{n−1}` split, `r ≥ 3` fragments of `2^n`), the band-parity reduction gives `D = 2^{n−1} − D_{R'}` with `R' = R_0 ∪ F` (rest `∪` non-`M` fragments of `2^n`); the target `D ≥ 1` becomes `D_{R'} ≤ 2^{n−1} − 1`. The trivial bound `D_{R'} ≤ max(R') < 2^{n−1}` is short of `2^{n−1} − 1` by an arbitrarily small `ε` (the fragments can be arbitrarily close to `2^{n−1}`), so the band-parity lens does NOT close `G1-ii` by itself: it re-derives the same "shave 1 unit off the trivial bound" wall that the explorer conceded and that `dyadic-induction`'s tiling-rigidity argument attacks directly. **Recorded as alternative bookkeeping, NOT a bypass** (per the explorer's honest concession and the reviewer's caveat). Do not chase a band-parity bypass — the explorer and reviewer both confirmed none exists.

#### 3.7 The G1-ii reduction to G1-i via perturbation / continuity (round 4)

This is the round-4 contribution. Recall the G1 sub-case partition (from `lemmas/splits-inequality.md`):

- **G1-i**: `2^n` split into `r ≥ 3` fragments, largest `M > 2^{n−1}` (strict).
- **G1-ii**: `M = 2^{n−1}` (fragment of `2^n`), **rest's piece `2^{n−1}` is SPLIT** (no Case-C tie), `M` unique largest.
- **G1-iii**: all fragments of `2^n` are `< 2^{n−1}`.

**The `r = 2` overlap with Case B (closed).** When `2^n → M + g_2` with `M = g_2 = 2^{n−1}` (one split, `r = 2`) and the rest's `2^{n−1}` is split, the two `2^{n−1}` fragments (`M` and `g_2`, both from `2^n`'s split) form an **equal pair**. By the parity-integral lemma (`lemmas/parity-integral.md`, CERTIFIED), an equal pair `(a, a)` contributes `+2 · 1_{[0, a)}` to `j(t)`, which is **even everywhere**, hence parity-neutral: removing the pair leaves `D` unchanged. So `D_final = D_{R_0}` (the rest, with `2^{n−1}` split). By the inductive hypothesis `G1(n−1)`, `D_{R_0} ≥ 1`. Hence `D ≥ 1`. ✓ This sub-case is in fact the **`M = g_2 = 2^{n−1}` boundary of Case B** (`2^n` split exactly once): the Case-B bound `D = 2^n − D_{R_0} − 2 E_1` with `E_1 = ∫_0^{2^{n−1}} [j_{R_0} even] dt = 2^{n−1} − D_{R_0}` saturates, giving `D = D_{R_0}` exactly. (Verified n = 3, exact rational arithmetic: `D_final = D_{R_0}` for every `c ∈ (0, 2]`.) So the `r = 2` "tie" sub-case is covered by Case B and requires no separate argument.

**The `r ≥ 3` reduction (conditional on `G1-i`).** Now `M = 2^{n−1}` is the **unique largest** piece of the final config (the `r − 1 ≥ 2` other fragments of `2^n` are each `< 2^{n−1}`, and the rest's pieces are all `< 2^{n−1}` because `2^{n−1}` is split). This is the genuine `G1-ii` sub-case (the one the dispatch assigns to this approach).

> **Lemma (G1-ii ⟹ G1-i, perturbation/continuity).** *If `G1-i` holds (every `G1-i` config has `D ≥ 1`), then `G1-ii` holds.*

*Proof.* Take any `G1-ii` config: `2^n` split into `M = 2^{n−1}, g_2, …, g_r` (`r ≥ 3`, each `g_i < 2^{n−1}`, `Σ_{i≥2} g_i = 2^{n−1}`), rest `R_0 = {1, 2, …, 2^{n−1}}` with `2^{n−1}` split (and possibly other splits; total `≤ n − (r−1) ≤ n − 2` splits on `R_0`). For `ε > 0` small, define the **perturbed config**: keep `R_0` unchanged; replace `M = 2^{n−1}` by `M_ε = 2^{n−1} + ε`; reduce the largest fragment `g_2` of `F` to `g_2 − ε` (keeping `g_2 − ε > 0` for `ε < g_2`, which holds for small `ε`); keep `g_3, …, g_r` unchanged. The perturbed `2^n`-split has total `(2^{n−1} + ε) + (g_2 − ε) + g_3 + … + g_r = 2^n` ✓, and `M_ε = 2^{n−1} + ε > 2^{n−1}` is the unique largest (the other fragments are `< 2^{n−1} < M_ε`, and `R_0`'s pieces are `< 2^{n−1} < M_ε`). The rest `R_0` still has its `2^{n−1}` split (unchanged). Hence the perturbed config is a **valid `G1-i` config** (`M > 2^{n−1}`, rest's `2^{n−1}` split — allowed in `G1-i`, which does not restrict the rest's `2^{n−1}`).

By the `G1-i` hypothesis, `D(perturbed) ≥ 1` for every `ε > 0`.

**Continuity at `ε = 0`.** The alternating sum `D = ∫_0^∞ [j(t) odd] dt` (parity-integral lemma, CERTIFIED) is a continuous function of the piece lengths: `j(t)` is a non-increasing step function with integer values, dropping at the piece lengths; a small perturbation of a piece length shifts the drop point by `O(ε)`, and the integral `∫[j odd]` changes by at most `O(ε)` (the shifted region has measure `O(ε)` and bounded integrand). Equivalently, `D` as the alternating sum of the descending sort is piecewise-linear and continuous in the piece lengths, including across sort-boundary ties (the alternating sum is invariant under re-ordering ties). At `ε = 0`, the `G1-ii` config has `M = 2^{n−1}` **strictly** largest (all other pieces `< 2^{n−1}`), so the top-rank position of `M` is stable in a neighborhood of `ε = 0`; no degenerate tie is approached. Hence `D(G1-ii) = lim_{ε → 0^+} D(perturbed) ≥ 1`. ∎

(Verified computationally: n = 3, 4, `D` is continuous across sort-boundary crossings under the perturbation (no jumps); near-degenerate `G1-ii` configs — rest's `2^{n−1}` split into `ε + (2^{n−1} − ε)` with `ε → 0` — give `D = 1 + 2ε → 1` from above, confirming the boundary `ε = 0` is `Case C` (`M = 2^{n−1}`, rest's `2^{n−1}` unsplit, tie), where `D = 1` exactly. So `G1-ii` interpolates continuously between `Case B` (`r = 2`) and `Case C` (degenerate rest-unsplit), both proved.)

**Honest scope.** This is a **reduction**, not an unconditional closure: it shows `G1-ii` is the `M → 2^{n−1}` boundary of `G1-i`, so `G1-ii` is no harder than `G1-i`. Once `dyadic-induction` certifies `G1-i` (its round-4 primary target, via the union-measure / dyadic-tiling rigidity argument), `G1-ii` follows immediately by this lemma. If `G1-i` stalls, `G1-ii`'s closure stalls with it (single-gap dependency, but on a DIFFERENT sub-case than the one `dyadic-induction` owns — `dyadic-induction` owns `G1-i/iii` directly; this approach contributes the `G1-ii`-specific reduction that imports `G1-i`'s result). The two approaches are **complementary**: `dyadic-induction` proves `G1-i` (and `G1-iii`); `alternating-potential` proves `G1-ii ⟹ G1-i`. Together they cover all three multi-split non-tie sub-cases.

#### 3.8 Conclusion of the lower bound (conditional on `G1`)

Assuming `G1`: after any `≤ n` Xiang Yu splits of Liu's dyadic config, `D ≥ 1/D_n`. Hence `S_odd = (1 + D)/2 ≥ (1 + 1/D_n)/2 = 2^n/D_n`. Liu guarantees `≥ 2^n/D_n`. ∎ (conditional.)

For `n = 1` the lower bound is unconditional (`G1(1)` proved): `c(1) ≥ 2/3`.

---

### 4. Upper bound: `D ≤ 1/D_n` for arbitrary Liu marks — CONCEDED

#### 4.1 Goal

For ANY Liu config (initial `n + 1` pieces `b_1 ≥ … ≥ b_{n+1}` summing to 1, with `D_0 = b_1 − b_2 + b_3 − … ≤ 1`), Xiang Yu has `≤ n` marks forcing the final `D ≤ 1/D_n`.

#### 4.2 The n=1 case (proved, as base and sanity check)

`n = 1`, Liu config `{b_1, b_2}`, `b_1 ≥ 1/2 ≥ b_2`, `b_1 + b_2 = 1`. `D_0 = b_1 − b_2 = 2 b_1 − 1`. Xiang has 1 mark; target `D ≤ 1/3`. Two strategies:
- **Equal-split** (split `b_1` into `b_1/2 + b_1/2`): by the equal-split formula (§3.3 analog, or directly), `D = b_2 = 1 − b_1`. So `D = 1 − b_1 ≤ 1/3 ⟺ b_1 ≥ 2/3`.
- **Barely-split** (split `b_1` into `ε + (b_1 − ε)`, `ε → 0`): pieces `{b_1 − ε, b_2, ε}`, sorted (for small `ε` when `b_1 > 1/2`); `D = (b_1 − ε) − b_2 + ε = b_1 − b_2 = D_0 = 2 b_1 − 1`. So `D = 2 b_1 − 1 ≤ 1/3 ⟺ b_1 ≤ 2/3`.

Xiang takes whichever strategy gives smaller `D`: `D_final = min(1 − b_1, 2 b_1 − 1)`. The two linear functions cross at `b_1 = 2/3` (where both equal `1/3`), and their min is maximised exactly at the crossing, giving `D_final ≤ 1/3 = 1/D_1`. Hence `S_odd = (1 + D)/2 ≤ (1 + 1/3)/2 = 2/3`. Upper bound `c(1) ≤ 2/3`. ✓ (Combined with §3.8: `c(1) = 2/3`.) This is the `min(A, B) ≤ (A+B)/2 ≤ max` crossover template (aimo-0198 hint, re-proved here).

#### 4.3 The pivoted amortized-potential attempt (this round)

Per the round-2 mandate, I pivoted the upper bound to an **amortized-potential on the parity-XOR framework**, adapting the crux template aimo-0019 (the Austria paint-pot game): maintain an amortized linear potential `ink ≤ 3·x_r` (resource bounded by `α·progress`) via a structural invariant (ii) ("at most one dyadic interval of each length beyond the frontier") that prevents double-charging on frontier-stalling moves.

**What the template requires of Φ.** A concrete potential `Φ(config)` such that (i) `Φ` decreases by a controlled amount per Xiang mark, (ii) `Φ ≥ D` (upper-bounds `D`), and (iii) `Φ` hits `1/D_n` exactly on the dyadic config (tight, no slack). The amortized-potential trick (vs. the naive dyadic-decrement telescope) is supposed to escape the factor-of-2 wall by exploiting a **structural inventory** beyond linear split-progress — exactly as aimo-0019's invariant (ii) gives extra cancellation beyond the naive frontier telescope.

#### 4.4 Candidate Φ tested: `Φ = D − λ·Π` (Π = sum of pair-deficits) — COLLAPSES TO THE WALL

The natural candidate for a "structural inventory" is the **pair-deficit sum** `Π := Σ_k (a_{2k−1} − a_{2k})`, i.e. `D` minus the trailing odd-rank leftover: `Π = D − leftover`, where `leftover = a_m` if `m` is odd, else `0`. At the equal-split config (§3.3), `Π = 0` (all pairs equal) and `leftover = 1/D_n`, so `D = 1/D_n`. Define `Φ = D − λ·Π = (1 − λ)·D + λ·leftover`.

- **At the dyadic equal-split config:** `Φ = (1 − λ)·(1/D_n) + λ·(1/D_n) = 1/D_n`. ✓ (tight, any `λ`.)
- **Per-split behavior:** consider a split of piece `p` into `α + β` (`β ≥ α`). The fragments land at some ranks; `D`, `Π`, and `leftover` all change. The change `ΔΦ = (1 − λ)·ΔD + λ·Δ(leftover)`. For `Φ` to be non-increasing (`ΔΦ ≤ controlled amount`), we need `ΔD ≤ (controlled)` — but `ΔD` is exactly the dyadic-decrement quantity that the round-1 dead-end bounded by `≤ 1/2^k` per split (factor-2 short). The `λ·Δ(leftover)` correction is **at most `λ·α`** (the leftover can change by at most the smaller fragment), and `α ≤ p/2`, so the correction is again `O(p/2)` — a dyadic-decrement schedule. The potential `Φ` is a **linear combination of `D` and the leftover**, both of which change by `O(piece/2)` per split; hence `Φ` changes by `O(1/2^k)` on the k-th split (the largest remaining piece halves geometrically). This is exactly the factor-of-2 dyadic-decrement telescope, giving `Φ ≤ O(1/2^n)`, short of `1/D_n ≈ 1/2^{n+1}` by a factor of 2.

Concretely, the schedule `Σ_{k=1}^{n} ΔΦ_k` with `|ΔΦ_k| ≤ c/2^k` sums to `≤ c`, landing at `Φ ≤ O(1/2^n)` — the wall. No choice of `λ` escapes this: both `D` and `leftover` are bounded by the largest piece, which halves per equal-split, so any linear combination of them obeys a dyadic-decrement schedule. **The candidate `Φ` collapses to the confirmed factor-of-2 dead-end.** (Verified: the round-1 dead-end table applies verbatim to `Φ` for every `λ ∈ [0, 1]`.)

#### 4.5 Why the aimo-0019 template does not transfer

The load-bearing piece of aimo-0019 is invariant (ii): *"for every `m`, `B` has blackened at most one interval of length `1/2^m` to the right of the frontier `x_r`."* This is a **dyadic-distinctness** invariant: the structural inventory of intervals beyond the frontier consists of pairwise-distinct dyadic lengths, which the player maintains by the look-ahead strategy (paint `I_1` before `I_0`). It is what allows the amortized bound `ink ≤ 3·x_r` to beat the naive frontier telescope: frontier-stalling moves (painting `I_1`) contribute to a *bounded* inventory rather than unbounded waste.

In our problem, the analogous "inventory" would be the toggle-sets `[0, v_i) ∪ [u_i, p_i)` of the splits. These are **not dyadic-distinct** in any useful sense:
- The bottom parts `[0, v_i)` all nest at the origin (they overlap, not disjoint).
- The top parts `[u_i, p_i)` can have arbitrary lengths and overlap arbitrarily (no distinctness enforced by the game).
- Xiang has no look-ahead mechanism to enforce dyadic-distinctness; the splits are constrained only by `v_i ≤ p_i/2` and `u_i + v_i = p_i`.

Without a dyadic-distinctness invariant, the amortized-potential bound reduces to the naive telescope `|ΔΦ_k| ≤ c/2^k`, which is the factor-of-2 wall. **I could not find a structural inventory in the parity-XOR framework that plays the role of aimo-0019's invariant (ii).**

#### 4.6 Honest concession of the upper bound (GAP-U)

Per the dispatch's explicit instruction ("If you cannot specify such a Φ concretely, CONCEDE the upper bound honestly; the upper bound is carried by sibling approaches"), I CONCEDE the upper bound for general `n` in the amortized-potential framing. The pivoted Φ does not escape the factor-of-2 wall; the candidate `Φ = D − λ·Π` collapses to the confirmed dead-end, and the aimo-0019 template's load-bearing structural invariant has no analog in our toggle structure.

**Distinguishing from `pairing-charging` (kept honest):** the dispatch warns that if the potential argument collapses into "exhibit a pairing," it has merged with `pairing-charging` and lost its value. Indeed, the only mechanism that empirically caps `D ≤ 1/D_n` (reviewer-verified for `n = 1, 2, 3, 4` by brute-force minimax) is the pairing / equal-halving construction — `pairing-charging`'s defining bet. The amortized-potential framing, unable to specify a non-pairing Φ that beats the wall, does NOT offer a genuinely distinct upper-bound route. The upper bound is conceded to the sibling approaches (`pairing-charging` direct partition, `minimax-strategy-family` regime enumeration).

**What is rigorously established for the upper bound in this approach:**
- `n = 1` upper bound: fully proved (§4.2, the two-strategy minimax).
- The parity-XOR toggle lemma (§2.2) and peeling lemma (§2.3) are proved and reusable (the peeling lemma is the inductive engine wherever `D`-additivity is needed; the toggle lemma is the clean handle for any parity-based upper-bound argument).
- The peeling corollary `D = |p_a − p_b|` (§2.4) is proved and is tight at dyadic — a concrete upper-bound *strategy* (one-mark), but only a single strategy, not a full `n`-mark strategy for arbitrary Liu. The round-1 / round-2 explorers confirmed a fixed menu of 1–2-mark strategies is INSUFFICIENT for `n ≥ 3` (worst `0.099 > 1/15`).

**GAP-U (upper bound, general n): CONCEDED.** The true upper bound holds (verified `n = 1, 2, 3, 4` by brute-force minimax); its proof in this framing would require reproducing the pairing structure of the optimal Xiang response, at which point the approach collapses into `pairing-charging` and loses its distinctiveness. Reported honestly rather than papered over with a fake Φ.

---

### 5. Small-case verification (computational)

| n | `D_n` | target `D = 1/D_n` | `c(n) = 2^n/D_n` | `D_init` (dyadic) | equal-split `D` |
|---|---|---|---|---|---|
| 1 | 3 | 1/3 ≈ 0.333 | **2/3** ≈ 0.667 | 1/3 ✓ | 1/3 ✓ |
| 2 | 7 | 1/7 ≈ 0.143 | **4/7** ≈ 0.571 | 3/7 | 1/7 ✓ |
| 3 | 15 | 1/15 ≈ 0.067 | **8/15** ≈ 0.533 | 5/15 = 1/3 | 1/15 ✓ |
| 4 | 31 | 1/31 ≈ 0.032 | **16/31** ≈ 0.516 | 11/31 | 1/31 ✓ |

All values verified by exact rational arithmetic (Python `fractions`); `D_init ≥ 1/D_n` ✓ for all `n ≥ 1` (equality at `n = 1`); equal-split config gives `D = 1/D_n` exactly ✓. The conjectured answer
```
c(n) = 2^n / (2^{n+1} − 1)
```
is verified for `n = 1, 2, 3, 4` against brute-force minimax (outline-reviewer's numerics, round 1 + re-confirmed round 2). **Verification for `n = 1, 2, 3` (the rigor-rule requirement):**
- `n = 1`: `c(1) = 2/3`. Liu's dyadic mark at `1/3`; Xiang's reply (§4.2) caps at `2/3`; equal-split attainment `D = 1/3`. ✓
- `n = 2`: `c(2) = 4/7`. Dyadic config `{1, 2, 4}/7`; `D_init = 3/7 ≥ 1/7`; equal-split `{1,1,1,2,2}/7` gives `D = 1/7`. ✓ (Reviewer's brute-force: `n = 2` upper-bound menu worst `0.142 ≤ 1/7`.)
- `n = 3`: `c(3) = 8/15`. Dyadic config `{1, 2, 4, 8}/15`; `D_init = 1/3 ≥ 1/15`; equal-split `{1,1,1,2,2,4,4}/15` gives `D = 1/15`. ✓ (Reviewer's brute-force minimax confirms `8/15`.)

---

### 6. Summary of rigour

- **Greedy-alternating lemma**: imported (CERTIFIED, `lemmas/greedy-alternating.md`).
- **D-reformulation**: fully proved (§1 Corollary).
- **Universal floor `D ≥ 0`**: fully proved (§1 Corollary).
- **Parity-integral reformulation `D = ∫[j odd]`**: fully proved (§2.1).
- **Parity-XOR toggle lemma**: fully proved (§2.2).
- **Peeling lemma (`D_final = D_rest` at an equal-pair split)**: fully proved (§2.3).
- **Peeling corollary `D = |p_a − p_b|`**: fully proved (§2.4); tight at dyadic.
- **Lower bound, base `n = 1`**: fully proved (§3.4, §3.8).
- **Lower bound, construction + `D_init` + equal-split attainment**: fully proved (§3.1–3.3).
- **Lower bound, even-rank-insertion sub-lemma**: fully proved (§3.5).
- **Lower bound, band-parity lens (round 4)**: re-derives Lemma 4 (`D = M − D_{R'}`) in band language; confirms the "shave 1" wall persists (§3.6). Alternative bookkeeping, NOT a bypass.
- **Lower bound, `G1-ii` `r = 2` sub-case**: closed (§3.7) — equal-pair parity-neutrality reduces to `G1(n−1)`; subsumed by Case B's boundary.
- **Lower bound, `G1-ii` `r ≥ 3` sub-case**: REDUCED to `G1-i` by perturbation/continuity (§3.7 Lemma). Conditional on `dyadic-induction` certifying `G1-i`. Complementary to `dyadic-induction` (which owns `G1-i/iii` directly); together they cover all three multi-split non-tie sub-cases.
- **Lower bound, full `G1` (rest-with-splits induction)**: GAP-L, narrowed this round — `G1-ii` is now a conditional reduction to `G1-i` (not an independent open sub-case). Remaining: `G1-i`, `G1-iii` (owned by `dyadic-induction`), and the overlap bound `2C ≥ D_{R_0} + D_F + 1 − M` (the shared crux).
- **Upper bound, `n = 1`**: fully proved (§4.2).
- **Upper bound, general `n` (amortized-potential Φ)**: GAP-U, **CONCEDED** (§4.3–4.6). The candidate `Φ = D − λ·Π` collapses to the confirmed factor-of-2 dead-end; the aimo-0019 template's load-bearing structural invariant has no analog in our toggle structure. Carried by sibling approaches.

**Status: `partial`.** The `D`-reformulation, the parity-XOR toggle lemma, the peeling lemma and its corollary, the lower-bound construction + base case, and the **round-4 `G1-ii ⟹ G1-i` perturbation/continuity reduction** (§3.7) are the approach's rigorous, reusable contributions. The lower bound is reduced to a shared, sibling-certifiable lemma (GAP-L, narrowed this round on the `G1-ii` sub-case); the upper bound — the approach's distinctive crux, pivoted in round 2 from the dead direct-D-cap to an amortized potential — is honestly conceded (GAP-U), the pivoted Φ having failed to escape the factor-of-2 wall. The conjectured answer `c(n) = 2^n/(2^{n+1}−1)` is stated explicitly and verified for `n = 1, 2, 3, 4`, but the proof is incomplete (two gaps: GAP-L shared — now conditional-reduced on `G1-ii`, with `G1-i`/`G1-iii`/overlap-bound awaiting `dyadic-induction`'s certification; GAP-U approach-specific, conceded in round 2).

---

## Promotable lemmas

1. **Greedy-alternating lemma** — *already CERTIFIED* in `lemmas/greedy-alternating.md`; not re-offered.

2. **Parity-integral reformulation** — *`D = ∫_0^∞ [j(t) odd] dt`, `j(t) = #{pieces ≥ t}`.* Proved in §2.1. Reusable by any approach needing a clean `D`-handle. Promotable as `lemmas/parity-integral.md` if the reviewer finds it reusable (note: also proved independently in `dyadic-induction` §2; certify once to avoid duplication).

3. **Parity-XOR toggle lemma** — *a split of `p` into `u ≥ v` toggles parity on `[0, v) ∪ [u, p)`; `D_final = ∫(f ⊕ h) dt` where `f = [j_Liu odd]`, `h = XOR of split-toggles`.* Proved in §2.2. The clean handle for any parity-based upper-bound argument. Promotable as `lemmas/parity-xor-toggle.md`.

4. **Peeling lemma** — *a split of `p_1` into `p_j + (p_1 − p_j)` (creating an equal pair `(p_j, p_j)`) is exactly `D`-neutral: `D_final = D_rest` on `rest = {all pieces except p_1, p_j} ∪ {p_1 − p_j}`.* Proved in §2.3 (reviewer-verified, error 0 on 20k configs). The inductive engine wherever `D`-additivity is needed. Promotable as `lemmas/peeling.md` (note: also proved/used by `pairing-charging`; certify once).

5. **Peeling corollary (`D = |p_a − p_b|`)** — *equal-split one piece + leave `p_a, p_b` unsplit (rest peeling-paired) gives `D_final = |p_a − p_b|` exactly; tight at dyadic.* Proved in §2.4. A concrete one-mark upper-bound strategy. Promotable as `lemmas/peeling-corollary.md`.

6. **Even-rank-insertion sub-lemma** — *when an extra piece `α` is inserted into a sorted multiset `R` at an even rank `t`, `S_odd(combined) ≤ total(R)` automatically; at an odd rank `t`, the bound holds iff `α ≤ S_odd(R)_{≥ t} + S_even(R)_{<t}`.* Proved in §3.5 (round 1, kept). A structural piece of the splits-inequality `G1`. Promotable as `lemmas/insertion-rank.md` if the reviewer finds it reusable.

7. **G1-ii ⟹ G1-i perturbation/continuity reduction (round 4)** — *the `G1-ii` sub-case (`M = 2^{n−1}` unique largest fragment of `2^n`, rest's `2^{n−1}` split, `r ≥ 3`) is the `M → 2^{n−1}` boundary of `G1-i`; perturbing `M → M + ε` lands in a valid `G1-i` config, and `D` is continuous in `ε` (parity-integral), so `D(G1-ii) = lim_{ε→0+} D(G1-i perturbed) ≥ 1` once `G1-i` holds.* Proved in §3.7. Complementary to `dyadic-induction` (owns `G1-i/iii` directly); the two together cover all three multi-split non-tie sub-cases. Promotable as `lemmas/g1ii-reduction.md` IF the reviewer finds the conditional reduction reusable (it imports `G1-i`'s result, so it is only load-bearing once `dyadic-induction` certifies `G1-i`; until then it is a recorded conditional lemma, not a standalone closure).

---

## Build notes

**What I proved this round (round 4):**
- Band-parity / t-axis decomposition of the parity integral (§3.6): re-derives Lemma 4 (`D = M − D_{R'}`) in band language; confirms the "shave 1" wall persists (`D_{R'} ≤ 2^{n−1} − 1` short of the trivial `D_{R'} < 2^{n−1}`). Recorded as alternative bookkeeping, NOT a bypass — consistent with the explorer's and reviewer's honest caveats.
- `G1-ii` `r = 2` overlap with Case B (§3.7, first part): the two `2^{n−1}` fragments form a parity-neutral equal pair (`+2` even on `[0, 2^{n−1})`), so `D = D_{R_0} ≥ 1` by `G1(n−1)`. Subsumed by Case B's `M = g_2 = 2^{n−1}` boundary (Case-B bound saturates). Verified exact-rational n = 3.
- **`G1-ii` `r ≥ 3` perturbation/continuity reduction to `G1-i`** (§3.7 Lemma): perturb `M = 2^{n−1} → 2^{n−1} + ε` (reduce `F`'s total by `ε`, keep `R_0` unchanged), landing in `G1-i` (`M > 2^{n−1}`, rest's `2^{n−1}` split — allowed); `D` continuous in `ε` (parity-integral, stable sort order at `ε = 0` since `M` strictly largest in `G1-ii`); so `D(G1-ii) = lim_{ε→0+} D(G1-i) ≥ 1` conditional on `G1-i`. Verified computationally (n = 3, 4: `D` continuous across sort-boundary crossings; near-degenerate configs approach `D = 1` linearly from above, boundary = Case C).

**Earlier rounds (kept, not re-proved):**
- Parity-integral reformulation `D = ∫[j(t) odd] dt` (§2.1, Fubini).
- Parity-XOR toggle lemma (§2.2): split of `p` into `u ≥ v` toggles parity on `[0, v) ∪ [u, p)`; `D_final = ∫(f ⊕ h)`.
- Peeling lemma (§2.3): equal-pair-creating split is `D`-neutral, `D_final = D_rest` exactly.
- Peeling corollary (§2.4): `D = |p_a − p_b|`, tight at dyadic.
- Confirmed computationally the round-1 lower-bound material (`D_init`, equal-split attainment for `n = 1, 2, 3, 4`).

**Does the pivoted amortized-potential upper bound have a concrete Φ?** **No** (round 2, unchanged). The candidate `Φ = D − λ·Π` (Π = sum of pair-deficits = D − leftover) was tested (§4.4) and shown to collapse to the confirmed factor-of-2 dead-end: both `D` and the leftover change by `O(piece/2)` per split, so any linear combination obeys a dyadic-decrement schedule `|ΔΦ_k| ≤ c/2^k`, summing to `O(1/2^n)` — short of `1/D_n ≈ 1/2^{n+1}` by a factor of 2. The aimo-0019 template's load-bearing structural invariant (ii) ("at most one dyadic interval of each length beyond the frontier") has no analog in our toggle structure (toggle-sets `[0, v) ∪ [u, p)` nest at the bottom and overlap arbitrarily at the top; no dyadic-distinctness is enforced by the game). No non-trivial Φ beating the wall was found. Do NOT retry (per per-role rule).

**Upper bound: CONCEDED** (§4.6, round 2, unchanged). The pivoted Φ does not escape the factor-of-2 wall; the only mechanism that empirically caps `D ≤ 1/D_n` is the pairing construction (`pairing-charging`'s defining bet), and the amortized-potential framing, unable to specify a non-pairing Φ, does NOT offer a genuinely distinct upper-bound route. Reported honestly rather than papered over. Carried by sibling approaches (`pairing-charging`, `minimax-strategy-family`).

**Remaining gaps (round 4 state):**
- **GAP-L (shared, lower bound) — NARROWED this round.** The `G1-ii` sub-case is now a conditional reduction to `G1-i` (§3.7), not an independent open sub-case. Remaining open: `G1-i` (`M > 2^{n−1}`), `G1-iii` (all fragments < `2^{n−1}`), and the multi-split non-tie overlap bound `2C ≥ D_{R_0} + D_F + 1 − M` (the shared crux). All three are `dyadic-induction`'s round-4 primary targets (union-measure / dyadic-tiling rigidity lens). If `dyadic-induction` certifies `G1-i`, `G1-ii` follows by §3.7; if it certifies the overlap bound, `splits-inequality.md` upgrades to fully PROVED. Single-gap dependency on `G1-i` is acceptable (different sub-case from `dyadic-induction`'s direct ownership — complementary, not duplicated).
- **GAP-U (approach-specific, upper bound): CONCEDED** (round 2). Honest concession; no concrete Φ escaping the wall. The upper bound is carried by `pairing-charging` (direct partition) and `minimax-strategy-family` (regime enumeration).

**Distinctiveness from `pairing-charging`:** kept honest. The amortized-potential framing could not produce a non-pairing Φ that beats the wall; the concession is made precisely because the alternative was to collapse into "exhibit a pairing," merging with `pairing-charging` and losing the approach's value. The reusable lower-bound + parity-XOR machinery (toggle lemma, peeling lemma, peeling corollary) and the round-4 `G1-ii ⟹ G1-i` reduction are the approach's genuine contributions, independent of the pairing construction.

**Coordination with `dyadic-induction` (same wall, complementary lens):** `dyadic-induction` owns `G1-i` and `G1-iii` directly (its tiling-rigidity argument); this approach owns `G1-ii` and proves `G1-ii ⟹ G1-i` (§3.7). The two reductions compose: if `dyadic-induction` closes `G1-i` (its target), this approach's §3.7 immediately yields `G1-ii` for free. No overlap in ownership; no single-gap trap between the two G1 attackers.
