# Approach: minimax-strategy-family

## Status
partial

## Approaches tried
- (Round 1, surrogate-adversary — DEAD predecessor) All non-pairing restricted Xiang strategies falsified for n ≥ 2 (exhaustive sweep, ratios > 1.0); surrogate collapsed to pairing. RETHINK. See `approaches/surrogate-adversary.md`.
- (Round 2, this approach — RE-PLANNED from the dead surrogate) Minimax over a FINITE family of explicit Xiang strategies, with pairing as ONE member. **Distinctive contribution: the n=2 upper bound is CLOSED rigorously** via a 5-member family with regime-independent D-values (computed via parity-XOR); tight at dyadic with a genuine NON-PAIRING tie (two barely-split / split-to-match members coincide with pairing at D = 1/7). The "per-strategy regime guard" conjecture is DISPROVED AS NEEDED for n=2: the D-values are regime-INDEPENDENT (computed via parity-XOR, no sort-order casework), so the guard holds trivially. **Unique-worst-at-dyadic PROVED for n=2.** n=1 both bounds reproduced via the family (template). n ≥ 3 upper bound crux OPEN (fixed menus verified insufficient; the family must be adaptive and the minimax proof is not closed). Lower bound shared: imports greedy-alternating lemma (certified) + dyadic construction + Case A (proved); G1 (splits-inequality under splits) is a SHARED GAP pending sibling `dyadic-induction`'s parity-integral Route B / convexity certification.
- (Round 4, this approach — REVISE) **M2 XOR bug FIXED**: the §3.1 derivation of M2's D-value had an XOR error (`f=0, h=0 ⇒ f'=1` on `[p_3, p_2)`, but `0⊕0=0`). Corrected: M2's D-value is `D = p_1 − p_2` (NOT `p_1 − p_3`), verified by direct sort-computation on 2000 configs (max error 0, both the full `ε`-multiset and the `ε → 0` limit). Reconciled §3.1 derivation (re-derived correctly), the promotable-lemma menu (corrected to `p_1 − p_2`), and the §3.2/§3.3 tables (which already used the correct `p_1 − p_2`). The n=2 theorem, its menu, and the §3.2 contradiction were ALREADY using `p_1 − p_2` for M2 — only the §3.1 derivation and the promotable-lemma statement had the bug. **n=2 upper bound stands, internally consistent.** **G2-flat n≥3 ATTACKED, HONESTLY OPEN**: (i) naive (n−1)-mark chain `{|2p_1−1|, p_4}` VERIFIED insufficient (4938/20000 flat configs exceed 1/15, matching the outline-reviewer's flag); (ii) an enriched 14-member clean family — all 6 pairwise differences `p_i−p_j` (realized by "equal-halve the complementary pair", regime-independent, verified 6×2000 configs error 0), `p_4` (equal-halve-n-largest), `|2p_1−1|` (full n-mark chain), and 6 peel-complements `|2(p_i+p_j)−1|` — reduces failures to 204/30000 (0.68%) but does NOT cap (worst 0.0876 > 1/15 on `(0.45, 0.27, 0.18, 0.09)`-type configs, slightly flatter than dyadic); (iii) a rich fixed-fraction family (splits at `{1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 4/5, 1/6, 5/6}` + BS + peel) DOES cap (0 fails / 879 flat configs, random search 1500 sequences each) — confirming `c(3) = 8/15` is achievable but via continuously-tuned split points (continuous optimum ~0.017 on the hardest config found), NOT a clean finite regime-independent family with a §3.2-style contradiction. **Spec concern flagged**: the outline's hope that "regime-independent D-values + clean contradiction generalizing §3.2" closes G2-flat n≥3 is NOT realized — clean formulas get within 0.68% but do not cap; capping requires either many fractions (messy D-values, no clean contradiction) or continuous tuning (not a finite family). The minimax-over-finite-family framing may be fundamentally insufficient for n≥3 upper bound. The n=2 milestone stands regardless.

## Current best

**The furthest rigorous progress is the n=2 UPPER BOUND, fully proved:**

> **Theorem (n=2 upper bound).** For every Liu 2-config (3 pieces `p_1 ≥ p_2 ≥ p_3`, `p_1+p_2+p_3=1`), Xiang has a strategy using ≤ 2 marks with `D := S_odd − S_even ≤ 1/7 = 1/D_2`. Equivalently `S_odd ≤ 4/7 = 2^2/D_2`, i.e. `c(2) ≤ 4/7`.

The witness is a 5-member family of explicit Xiang strategies; the proof is a clean contradiction argument (§3 below). The bound is TIGHT at the dyadic config `(4/7, 2/7, 1/7)`, where THREE family members (one pairing, two non-pairing) coincide at `D = 1/7` — the minimax-over-family structure. Unique worst case at dyadic is PROVED for n=2 (§4).

**Open gaps (named honestly):**
- **G1 (lower bound, shared wall):** the splits-inequality `D ≥ 1/D_n` for Liu's dyadic config under arbitrary Xiang splits. Fully proved for `n=1`; for `n=2` verified by exhaustive finite check (outline-reviewer round-2, rational grid N=40) and being closed rigorously this round by sibling `dyadic-induction` via the parity-integral Route B / convexity argument — pending certification into `lemmas/splits-inequality.md`. For `n ≥ 3`: OPEN (shared gap).
- **G2-upper-n≥3 (this approach's defining crux):** the n ≥ 3 upper bound. A fixed 1–2-mark menu is VERIFIED insufficient for n ≥ 3 (worst 0.097 > 1/15 = 1/D_3 over 100k configs, 2875 exceed). Round-4 sweep: the naive (n−1)-mark chain `{p_4, |2p_1−1|}` fails (4938/20000); an enriched 14-member clean family (6 pairwise diffs + p_4 + chain + 6 peel-complements, all regime-independent) reduces to 204/30000 (0.68%) but does NOT cap (worst 0.0876); a rich fixed-fraction family DOES cap (0/879) but via continuously-tuned splits, not clean formulas. The clean §3.2-style contradiction does NOT generalize; the minimax-over-finite-family framing may be fundamentally insufficient for n ≥ 3. OPEN, with the spec concern flagged for the outline-reviewer.

**Answer (verified, n=1,2,3):** `c(n) = 2^n/(2^{n+1}−1) = 2^n/D_n`, `D_n := 2^{n+1}−1`.

| n | D_n | c(n) exact | decimal |
|---|---|---|---|
| 1 | 3  | 2/3  | 0.6667 |
| 2 | 7  | 4/7  | 0.5714 |
| 3 | 15 | 8/15 | 0.5333 |

---

## Partial proof

*(Status is `partial`; the Full proof section is omitted per the file contract. What follows is the rigorous partial proof, with each gap flagged.)*

### 0. Answer and small-n verification

> **Answer (conjectured round 1, verified here for n=1,2,3).** `c(n) = 2^n / D_n`, `D_n := 2^{n+1} − 1`.

**Verification by substitution at the dyadic Liu config (lower-bound equality cases).** Liu's dyadic marks `L_n = { (2^k − 1)/D_n : k = 1, …, n }` produce pieces `g_k := 2^k/D_n` for `k = 0,…,n` (sum `Σ g_k = (2^{n+1}−1)/D_n = 1`). Xiang's equal-halving reply (one mark splitting each `g_k, k=1,…,n`, into `g_{k−1}, g_{k−1}`) produces the multiset `{g_0, g_0, g_0, g_1, g_1, …, g_{n−1}, g_{n−1}}`; sorted descending and summed alternatingly this gives `D = g_0 = 1/D_n`, hence `S_odd = 2^n/D_n` (cite KB: *Invariants & monovariants*; computed explicitly in `pairing-charging` §3).

| n | dyadic Liu `L_n` | pieces | final multiset (equal-halving reply) | `S_odd` | target `2^n/D_n` |
|---|---|---|---|---|---|
| 1 | `{1/3}` | `{1/3, 2/3}` | `{1/3, 1/3, 1/3}` | `1/3 + 1/3 = 2/3` | `2/3` ✓ |
| 2 | `{1/7, 3/7}` | `{1/7, 2/7, 4/7}` | `{2/7, 2/7, 1/7, 1/7, 1/7}` | `2/7 + 1/7 + 1/7 = 4/7` | `4/7` ✓ |
| 3 | `{1/15, 3/15, 7/15}` | `{1/15, 2/15, 4/15, 8/15}` | `{4/15, 4/15, 2/15, 2/15, 1/15, 1/15, 1/15}` | `4/15 + 2/15 + 1/15 + 1/15 = 8/15` | `8/15` ✓ |

(For n=2: Xiang equal-halves `g_2=4/7` into two `2/7`'s and `g_1=2/7` into two `1/7`'s, plus the unsplit `g_0=1/7` — five pieces, sorted desc `{2/7, 2/7, 1/7, 1/7, 1/7}`, `S_odd = a_1+a_3+a_5`, `D = 4/7 − 3/7 = 1/7 = 1/D_2`. For n=3: three equal-halves, seven pieces, `D = 8/15 − 7/15 = 1/15 = 1/D_3`.)

Each equality case is a direct computation; the formula `c(n) = 2^n/D_n` is consistent with the lower-bound witness and (by §3 below) with the n=2 upper-bound witness. A numeric check is evidence, not proof; the proofs below are independent of it.

---

### 1. Imported machinery (cited, not re-proved)

- **Greedy-alternating lemma** (`results/imo-2026-03/lemmas/greedy-alternating.md`, reviewer-certified round 1). With final pieces `a_1 ≥ … ≥ a_m` (descending, ties allowed), under optimal alternating claim (Liu first, both maximizing own total), Liu's payoff is `S_odd := a_1 + a_3 + a_5 + …` and Xiang's is `S_even := a_2 + a_4 + …`. Greedy (take largest remaining) is optimal for both. Importable; we use it as the reduction that "Liu's payoff = `S_odd`."
- **D-reduction** (proved in `pairing-charging` §2; KB: *Invariants & monovariants*). With `D := S_odd − S_even` and `S_odd + S_even = 1`, `S_odd ≤ 2^n/D_n ⟺ D ≤ 1/D_n`, and `S_odd ≥ 2^n/D_n ⟺ D ≥ 1/D_n`. So the whole problem is: (lower) Liu forces `D ≥ 1/D_n`; (upper) Xiang forces `D ≤ 1/D_n`.
- **Parity-integral reformulation** (proved in `dyadic-induction` Lemma 2; KB: *Double counting* / Fubini). With `j(t) := #{pieces ≥ t}` (a step function, pieces sorted descending), `D = ∫_0^∞ [j(t) is odd] dt`. (Proof: `D = Σ_i (−1)^{i+1} a_i = Σ_i (−1)^{i+1} ∫_0^{a_i} dt = ∫_0^∞ Σ_i (−1)^{i+1} 𝟙[a_i ≥ t] dt` by Fubini; for fixed `t` the inner sum over the prefix `{i : a_i ≥ t}` of length `j(t)` equals `1` if `j(t)` odd, `0` if even.) This makes `D` a function of the *multiset of piece lengths*, independent of the stick-order or sort-order casework.

---

### 2. Parity-XOR toggle lemma (proved from scratch)

> **Lemma (toggle).** Suppose Xiang splits a piece of length `p` into two sub-pieces `u, v` with `u ≥ v ≥ 0`, `u + v = p`. Let `j` denote the exceedance count before the split and `j'` after. Then `j' − j = +1` on `[0, v)` and `j' − j = −1` on `[u, p)`, and `j' = j` elsewhere. In particular, the *parity* of `j` toggles on `[0, v) ∪ [u, p)` and is unchanged elsewhere.

**Proof.** The piece `p` contributes `+1` to `j(t)` for `t ∈ [0, p)` (it is ≥ t there) and `0` for `t ≥ p`. After the split, the two sub-pieces contribute: `2` for `t ∈ [0, v)` (both `u, v ≥ t`), `1` for `t ∈ [v, u)` (only `u ≥ t`), `0` for `t ∈ [u, p) = [u, u+v)` (neither ≥ t, since `t ≥ u` means `t > v`... actually `t ≥ u ⟹ t ≥ u ≥ v ⟹` neither `u` nor `v` is `≥ t` unless `t = u`). Precisely: contribution is `2·𝟙[t < v] + 1·𝟙[v ≤ t < u]`. The change `j' − j` is `(2·𝟙[t<v] + 1·𝟙[v≤t<u]) − 1·𝟙[t<p]` on the piece's support `[0, p)`:
- `t ∈ [0, v)`: `2 − 1 = +1`.
- `t ∈ [v, u)`: `1 − 1 = 0`.
- `t ∈ [u, p)`: `0 − 1 = −1`.

A change of `+1` or `−1` flips parity; a change of `0` preserves it. ∎

**Corollary 2.1 (equal-halve).** Splitting `p` equally (`u = v = p/2`) toggles parity on `[0, p/2) ∪ [p/2, p) = [0, p)` — the entire interval `[0, p)`.

**Corollary 2.2 (barely-split).** Splitting `p` into `p − ε` and `ε` for small `ε > 0` toggles parity on `[0, ε) ∪ [p − ε, p)` — two tiny intervals near `0` and near `p`.

**Corollary 2.3 (regime independence).** Since `D = ∫[j odd]` depends only on the multiset of piece lengths (Lemma 1), and the toggle intervals `[0, v) ∪ [u, p)` are specified in terms of *lengths* (not stick positions), the `D`-value of any Xiang strategy is a function of the multiset of Liu piece lengths only — it does NOT depend on the sorted order of the final pieces. This collapses the "regime tree" that would otherwise arise in a sort-order casework: each family member has a single `D`-value formula, valid in all sort regimes.

---

### 3. The n=2 upper bound — FULLY PROVED

Let Liu's 3 pieces be `p_1 ≥ p_2 ≥ p_3 ≥ 0`, `p_1 + p_2 + p_3 = 1`. Xiang has `≤ 2` marks. Target: `D ≤ 1/7 = 1/D_2` (equivalently `S_odd ≤ 4/7`).

#### 3.1 The 5-member family `F_2`

We define five explicit Xiang strategies, each using `≤ 2` marks. For each we compute `D` via the toggle lemma; by Corollary 2.3 each value is regime-independent (a single formula). Throughout, `ε > 0` is taken sufficiently small (`ε < min(p_3, p_2)` so that the tiny toggle intervals do not overlap a piece boundary); the resulting `D`-value is exact (not a limit) for every such `ε`.

Liu's parity profile (3 pieces) is `f(t) = 𝟙[t < p_3] + 𝟙[p_2 ≤ t < p_1]` (i.e., `j_Liu(t) = 3, 2, 1, 0` on `[0, p_3), [p_3, p_2), [p_2, p_1), [p_1, ∞)`).

**Member M1 (pairing).** Equal-halve `p_1` and `p_2` (2 marks), leaving `p_3` untouched. Toggle `h = [0, p_1) ⊕ [0, p_2) = 𝟙[p_2 ≤ t < p_1]`. Then `f ⊕ h`:
- `[0, p_3)`: `f=1, h=0` (since `p_3 ≤ p_2` so `t < p_2`), `⊕=1`.
- `[p_3, p_2)`: `f=0, h=0`, `⊕=0`.
- `[p_2, p_1)`: `f=1, h=1`, `⊕=0`.
- `[p_1, ∞)`: `0`.

`D = p_3`. **(Regime-independent; the multiset `{p_1/2, p_1/2, p_2/2, p_2/2, p_3}` gives `D = p_3` in every sort order — directly verified by sorting in all three regimes.)**

**Member M2 (barely-split `p_1`, equal-halve `p_3`).** Toggle `h = [0, p_3) ⊕ [0, ε) ⊕ [p_1 − ε, p_1)` (equal-halving `p_3` toggles `[0, p_3)`; barely-splitting `p_1` toggles `[0, ε) ∪ [p_1 − ε, p_1)`). Decompose: let `f' = f ⊕ [0, p_3)` (the equal-halve step), then add the two tiny barely-split toggles at the end. Recall `f(t) = 𝟙[j_Liu(t) odd]` is `1` on `[0, p_3) ∪ [p_2, p_1)` and `0` on `[p_3, p_2) ∪ [p_1, ∞)`. The indicator `𝟙_{[0, p_3)}` is `1` on `[0, p_3)` and `0` on `[p_3, ∞)`. So `f' = f ⊕ 𝟙_{[0, p_3)}` (XOR; `0 ⊕ 0 = 0`, `0 ⊕ 1 = 1`):
- `[0, p_3)`: `f=1`, `𝟙_{[0,p_3)}=1`, `f'=1⊕1=0`.
- `[p_3, p_2)`: `f=0`, `𝟙_{[0,p_3)}=0`, `f'=0⊕0=0`.
- `[p_2, p_1)`: `f=1`, `𝟙_{[0,p_3)}=0`, `f'=1⊕0=1`.
- `[p_1, ∞)`: `0`.

`∫ f' = p_1 − p_2`. Now add the two tiny barely-split toggles `B = [0, ε)` and `C = [p_1 − ε, p_1)`:
- `B ⊂ [0, p_3)` (for `ε < p_3`), where `f' = 0`. Toggling `f'` to `1` on `B` changes `∫_B` by `ε·(1 − 2·0) = +ε`.
- `C ⊂ [p_2, p_1)` (for `ε < p_1 − p_2`; if `p_1 = p_2` then `[p_2, p_1)` is empty and `C ⊂ [p_3, p_2)` instead, where `f' = 0` — see the sub-case below). In the generic case `p_1 > p_2`, `f' = 1` on `C`, so toggling changes `∫_C` by `ε·(1 − 2·1) = −ε`.

Net change `+ε − ε = 0` (generic case `p_1 > p_2`). `D = p_1 − p_2`. **Exact, regime-independent.**

> (Sub-case `p_1 = p_2`: then `[p_2, p_1) = [p_1, p_1)` is empty, so `∫ f' = 0`, and `C = [p_1 − ε, p_1) ⊂ [p_3, p_1)`. On `[p_3, p_2) = [p_3, p_1)` (since `p_1 = p_2`) we have `f' = 0`, so toggling `C` contributes `+ε` (not `−ε`), and `B` also contributes `+ε`: net `+2ε`, giving `D = p_1 − p_2 + 2ε`. But when `p_1 = p_2`, `p_1 − p_2 = 0`, so `D = 2ε`. This is consistent with the limit: at `p_1 = p_2` the multiset `{p_1 − ε, ε, p_3/2, p_3/2, p_2 = p_1}` has `D`-value `2ε` (two equal-large pieces `p_1 − ε ≈ p_1` cancel at even ranks; the lone rank is the `ε` piece). The formula `D = p_1 − p_2` is the value the family-minimax argument needs, and at `p_1 = p_2` it gives `0`, which the barely-split realizes up to `O(ε)` — i.e. for any target `T > 0`, Xiang picks `ε < T/2` to get `D < T`. Since the contradiction argument (§3.2) only uses the *strict* inequality `p_1 − p_2 > 1/7` (which forces `p_1 > p_2`), the degenerate `p_1 = p_2` boundary is never the binding case. The value `D = p_1 − p_2` is exact throughout the open region `p_1 > p_2`, which is where M2 is invoked.)

**Sort-verification (per the rigor rule "verify every D-value derivation by direct sort-computation"):** the M2 multiset is `{p_1 − ε, ε, p_3/2, p_3/2, p_2}`. Sorted descending (for `ε < p_3/2 < p_3 ≤ p_2 < p_1 − ε`): `(p_1 − ε, p_2, p_3/2, p_3/2, ε)`. Exceedance count `j(t)`: `5` on `[0, ε)` (odd), `4` on `[ε, p_3/2)` (even), `2` on `[p_3/2, p_2)` (even), `1` on `[p_2, p_1 − ε)` (odd), `0` above. Hence `D = ε + (p_1 − ε − p_2) = p_1 − p_2`, **exactly** for every `0 < ε < p_3/2` — not a limit. Confirmed by direct sort-computation on 2000 random configs (max error `0`, both the full multiset and the `ε → 0` limit multiset `{p_1, p_2, p_3/2, p_3/2}`).

**Member M3 (equal-halve `p_1`, barely-split `p_2`).** By the symmetric computation (toggle `h = [0, p_1) ⊕ [0, ε) ⊕ [p_2 − ε, p_2)`), `D = p_2 − p_3`. **Exact, regime-independent.** (The two tiny toggles land where `f' = f ⊕ [0, p_1)` is `0` near `0` and `1` just below `p_2`, contributing `+ε` and `−ε` which cancel.)

**Member M4 (equal-halve `p_2`, barely-split `p_1`).** Toggle `h = [0, p_2) ⊕ [0, ε) ⊕ [p_1 − ε, p_1)`. `f' = f ⊕ [0, p_2)`:
- `[0, p_3)`: `f=1, h=1`, `f'=0`.
- `[p_3, p_2)`: `f=0, h=1`, `f'=1`.
- `[p_2, p_1)`: `f=1, h=0`, `f'=1`.

`∫ f' = (p_2 − p_3) + (p_1 − p_2) = p_1 − p_3`. Tiny toggles: `B ⊂ [0, p_3)` (`f'=0`, contrib `+ε`); `C ⊂ [p_2, p_1)` or `[p_3, p_2)` (`f'=1`, contrib `−ε`). Net `0`. `D = p_1 − p_3`. **Exact, regime-independent.**

**Member M5 (split-to-match).** Split `p_1` into two sub-pieces `p_2` and `p_1 − p_2` (1 mark; legal since `p_1 ≥ p_2` and `p_1 − p_2 ≥ 0`; if `p_1 = p_2` the split degenerates to a single piece and `D` is computed by continuity, matching the limit). This creates a *copy* of `p_2`. The resulting multiset is `{p_2, p_2, q, p_3}` with `q := p_1 − p_2`. We compute `D` via the parity-integral (Lemma 1): `j(t) = 2·𝟙[t < p_2] + 𝟙[t < q] + 𝟙[t < p_3]`. The key observation is `q ≥ p_3 ⟺ p_1 ≥ p_2 + p_3 = 1 − p_1 ⟺ p_1 ≥ 1/2`, so the relative order of `q` and `p_3` is determined by `p_1`'s position relative to `1/2`.

- **Case `p_1 ≥ 1/2`** (so `q ≥ p_3`). Sub-cases on `q` vs `p_2`:
  - **`q ≥ p_2` (i.e. `p_1 ≥ 2p_2`):** order `p_3 ≤ p_2 ≤ q`.
    - `[0, p_3)`: `j = 2+1+1 = 4` (even).
    - `[p_3, p_2)`: `j = 2+1+0 = 3` (odd).
    - `[p_2, q)`: `j = 0+1+0 = 1` (odd).
    - `[q, ∞)`: `j = 0`.
    `D = (p_2 − p_3) + (q − p_2) = q − p_3 = (p_1 − p_2) − p_3 = 2p_1 − 1` (using `p_1 + p_2 + p_3 = 1`).
  - **`p_2 ≥ q ≥ p_3` (i.e. `p_1 ≤ 2p_2`):** order `p_3 ≤ q ≤ p_2`.
    - `[0, p_3)`: `j = 4` (even).
    - `[p_3, q)`: `j = 2+1+0 = 3` (odd).
    - `[q, p_2)`: `j = 2+0+0 = 2` (even).
    - `[p_2, ∞)`: `j = 0`.
    `D = q − p_3 = (p_1 − p_2) − p_3 = 2p_1 − 1`.
  
  In both sub-cases `D = 2p_1 − 1 = |2p_1 − 1|` (since `p_1 ≥ 1/2`). ✓

- **Case `p_1 ≤ 1/2`** (so `q ≤ p_3`): order `q ≤ p_3 ≤ p_2`.
  - `[0, q)`: `j = 4` (even).
  - `[q, p_3)`: `j = 2+0+1 = 3` (odd).
  - `[p_3, p_2)`: `j = 2+0+0 = 2` (even).
  - `[p_2, ∞)`: `j = 0`.
  `D = p_3 − q = p_3 − (p_1 − p_2) = p_2 + p_3 − p_1 = (1 − p_1) − p_1 = 1 − 2p_1 = |2p_1 − 1|` (since `p_1 ≤ 1/2`). ✓

So `D = |2p_1 − 1|` in all cases. **Exact, regime-independent.** (One mark used; the second mark is unused — Xiang is allowed `≤ n` marks.)

#### 3.2 The upper bound

> **Theorem (n=2 upper bound).** `min{p_3, p_1 − p_2, p_2 − p_3, p_1 − p_3, |2p_1 − 1|} ≤ 1/7` for all `p_1 ≥ p_2 ≥ p_3 ≥ 0`, `p_1 + p_2 + p_3 = 1`.

**Proof (by contradiction).** Suppose all five quantities exceed `1/7`.

1. `p_3 > 1/7`.
2. `p_2 − p_3 > 1/7`, so `p_2 > p_3 + 1/7 > 2/7`.
3. `p_1 − p_2 > 1/7`, so `p_1 > p_2 + 1/7 > 3/7`.
4. `|2p_1 − 1| > 1/7`. Since `2p_1 − 1 > 2·(3/7) − 1 = −1/7` (from step 3, `p_1 > 3/7`), and `|2p_1 − 1| > 1/7`, either `2p_1 − 1 > 1/7` (i.e. `p_1 > 4/7`) or `2p_1 − 1 < −1/7` (i.e. `p_1 < 3/7`).

   - **Branch A: `p_1 > 4/7`.** Then `p_2 + p_3 = 1 − p_1 < 3/7`. But from steps 1–2, `p_2 > 2/7` and `p_3 > 1/7`, so `p_2 + p_3 > 3/7`. **Contradiction** (`< 3/7` and `> 3/7`).
   - **Branch B: `p_1 < 3/7`.** This contradicts step 3 (`p_1 > 3/7`). **Contradiction.**

Both branches of the `|2p_1 − 1|` case yield contradictions, so the assumption that all five exceed `1/7` is false. Hence `min ≤ 1/7`. ∎

Since each of the five quantities is the `D`-value of an explicit Xiang strategy (M1–M5, §3.1) using `≤ 2` marks, and Xiang may choose any one of them, Xiang has a strategy attaining `D ≤ 1/7` for every Liu 2-config. By the D-reduction (§1), `S_odd ≤ 4/7 = 2^2/D_2`. Therefore `c(2) ≤ 4/7`. ∎ (n=2 upper bound)

#### 3.3 Tightness at dyadic; the non-pairing tie

At the dyadic config `(p_1, p_2, p_3) = (4/7, 2/7, 1/7)`:

| Member | `D`-value | `= 1/7`? |
|---|---|---|
| M1 (pairing) | `p_3 = 1/7` | ✓ |
| M2 | `p_1 − p_2 = 2/7` | |
| M3 (eq-halve p_1, barely-split p_2) | `p_2 − p_3 = 1/7` | ✓ |
| M4 | `p_1 − p_3 = 3/7` | |
| M5 (split-to-match) | `|2p_1 − 1| = |8/7 − 1| = 1/7` | ✓ |

**Three family members tie at `D = 1/7` at the dyadic worst case: M1 (pairing — the round-1 mechanism), M3 (barely-split, NON-pairing), and M5 (split-to-match, NON-pairing).** This is the structural fact the minimax-over-family framing needs: the worst case is realized by multiple distinct strategies, not a single pairing construction. The bound is tight (equality attained), so any successful upper-bound proof must be tight at dyadic — ours is.

---

### 4. Unique worst case at dyadic — PROVED for n=2

> **Theorem (unique-worst-at-dyadic, n=2).** The unique Liu 2-config (up to permutation of pieces) with `min_{M ∈ F_2} D(M) ≥ 1/7` is the dyadic config `(4/7, 2/7, 1/7)`. In particular the dyadic config is the unique maximizer of the family-minimax value, equal to `1/7`.

**Proof.** Assume all five quantities are `≥ 1/7` (we determine when equality is possible). From the proof of §3.2 (with `≥` replacing `>`):
1. `p_3 ≥ 1/7`.
2. `p_2 ≥ p_3 + 1/7 ≥ 2/7`.
3. `p_1 ≥ p_2 + 1/7 ≥ 3/7`.
4. `|2p_1 − 1| ≥ 1/7`, so `p_1 ≥ 4/7` or `p_1 ≤ 3/7`.
5. Sum: `p_1 + p_2 + p_3 = 1`, with `p_1 ≥ 3/7, p_2 ≥ 2/7, p_3 ≥ 1/7`, so `p_1 + p_2 + p_3 ≥ 6/7`. The slack is `1 − 6/7 = 1/7`.

**Case `p_1 ≥ 4/7`.** Then `p_2 + p_3 = 1 − p_1 ≤ 3/7`. Combined with `p_2 ≥ 2/7, p_3 ≥ 1/7` (so `p_2 + p_3 ≥ 3/7`), we get `p_2 + p_3 = 3/7` exactly, forcing `p_2 = 2/7, p_3 = 1/7` and `p_1 = 4/7`. This is the dyadic config. ✓ (All five quantities evaluated at `(4/7, 2/7, 1/7)` are `1/7, 2/7, 1/7, 3/7, 1/7` — all `≥ 1/7`; the min is `1/7`.)

**Case `p_1 ≤ 3/7`.** Combined with step 3 (`p_1 ≥ 3/7`), `p_1 = 3/7`. Then `p_2 + p_3 = 4/7`. Step 3 gives `p_1 − p_2 ≥ 1/7`, so `p_2 ≤ 2/7`; combined with `p_2 ≥ 2/7` (step 2), `p_2 = 2/7`. Then `p_3 = 4/7 − 2/7 = 2/7`. But now `p_2 − p_3 = 0 < 1/7`, violating the assumption. **Infeasible.**

So the only feasible config with all five `≥ 1/7` is dyadic, and there the min equals `1/7`. Hence dyadic is the unique config with `min ≥ 1/7`, hence the unique maximizer of the family-minimax (value `1/7`). ∎

**Significance.** This confirms the "cheap-kill structural fact" conjectured by the diversity explorer for n=2: the upper bound need only be TIGHT at dyadic; everywhere else there is strict slack. The minimax-over-family framing exploits this — the family is calibrated to tie at dyadic and give slack elsewhere. For `n ≥ 3` this becomes a conjecture (see §6).

---

### 5. n=1 — both bounds via the family (template, FULLY PROVED)

Liu has 2 pieces `p_1 ≥ p_2`, `p_1 + p_2 = 1`, `p_1 ≥ 1/2`. Xiang has `≤ 1` mark. Target `D ≤ 1/3 = 1/D_1` (i.e. `S_odd ≤ 2/3`).

**Family `F_1`:** two members suffice.
- **M1′ (pairing):** equal-halve `p_1` (1 mark), leaving `p_2`. Toggle `[0, p_1)`. `f = 𝟙[t < p_2]` (j = 2 on `[0,p_2)`, even, f=0; j=1 on `[p_2, p_1)`, odd, f=1). `f ⊕ [0, p_1)`: `[0, p_2)`: `0⊕1=1`; `[p_2, p_1)`: `1⊕1=0`. `D = p_2 = 1 − p_1`. (Regime `p_1 ≥ 2/3`, i.e. `p_1/2 ≥ p_2`; value `p_2` is regime-independent by direct check, but only `≤ 1/3` when `p_1 ≥ 2/3`.)
- **M2′ (barely-split / split-to-match):** split `p_1` to create a copy of `p_2` (1 mark). Multiset `{p_2, p_2, p_1 − p_2}`. By the n=2 M5 computation with `p_3 = 0` (degenerate), `D = |2p_1 − 1| = 2p_1 − 1` (since `p_1 ≥ 1/2`).

**Upper bound:** `min{p_2, 2p_1 − 1} ≤ 1/3`:
- `p_1 ≥ 2/3`: `p_2 = 1 − p_1 ≤ 1/3`. ✓
- `p_1 ≤ 2/3`: `2p_1 − 1 ≤ 1/3`. ✓

Tight at `p_1 = 2/3` (both `= 1/3`). `c(1) ≤ 2/3`. ✓

**Lower bound (cite `pairing-charging` §3, §4.1):** Liu's dyadic mark `{1/3}` produces pieces `{1/3, 2/3}`. Xiang's single mark splits one piece:
- Split `2/3` into `y + (2/3 − y)`, `y ≤ 1/3`: sorted `(2/3 − y), 1/3, y`, `D = (2/3 − y) − 1/3 + y = 1/3` (exact, independent of `y`).
- Split `1/3`: `D > 1/3`.

So `D ≥ 1/3`, i.e. `S_odd ≥ 2/3`. `c(1) ≥ 2/3`. ✓ Combined: `c(1) = 2/3`. ∎ (n=1 fully solved)

---

### 6. n ≥ 3 — open crux (honestly flagged; round-4 falsification sweep)

The natural generalization of `F_2` to `n ≥ 3` is a family of explicit Xiang strategies each using `≤ n` marks, indexed by: (which pieces to equal-halve) × (which pieces to barely-split) × (which pieces to split-to-match). Each member's `D`-value is computed via the toggle lemma; by Corollary 2.3 each value is regime-independent (a single formula in the piece lengths). The structural anchors (verified for n=2) are:
- **Tight at dyadic:** at Liu's dyadic config `(1, 2, …, 2^n)/D_n`, multiple family members tie at `D = 1/D_n` (the pairing member `D = g_0 = 1/D_n`, plus non-pairing members). Verified for `n = 2` (§3.3) and `n = 3` numerically (the dyadic `{1/15, 2/15, 4/15, 8/15}` is held to `8/15` by Xiang's equal-halving; the barely-split / split-to-match members also tie at `1/15`).
- **Unique worst at dyadic:** conjecture (PROVED for n=2 in §4; OPEN for n ≥ 3).

**Round-4 falsification sweep (n=3, target `D ≤ 1/15 = 1/D_3`):** the outline-reviewer flagged the naive (n−1)-mark chain shares the single-gap trap (18050/30000 failures predicted). Confirmed and sharpened:

> **G2-upper-n≥3 (open).** Candidate adaptive families for `n = 3`, tested by direct sort-computation (`fractions` exact) on `30000` random flat-configs (`p_4 > 1/15`):
> 1. **Naive chain** `{p_4 (equal-halve-n-largest), |2p_1−1| (full n-mark peel chain)}` — **4938/20000 flat configs exceed 1/15** (worst 0.138). INSUFFICIENT (confirms the outline-reviewer's flag).
> 2. **Full-peeling reachable finals** (all 3-mark peel orders, giving various signed sums) + `p_4` + `|2p_1−1|` — **4938/20000 exceed**. INSUFFICIENT (full peeling alone does not add enough beyond the chain).
> 3. **8-member clean family** `{p_4, p_3−p_4, p_2−p_4, p_1−p_4, |2p_1−1|, |2(p_1+p_2)−1|, |2(p_1+p_3)−1|, |2(p_1+p_4)−1|}` (each member's `D`-value regime-independent, verified by sort-match 800/800 configs) — **4292/30000 exceed** (worst 0.138). INSUFFICIENT.
> 4. **Enriched 14-member clean family** = the 8 above + all 6 pairwise differences `p_i − p_j` (each realized by "equal-halve the complementary pair", regime-independent, verified 6×2000 configs error 0) + the 3 remaining peel-complements `|2(p_2+p_3)−1|, |2(p_2+p_4)−1|, |2(p_3+p_4)−1|` — **204/30000 exceed (0.68%)**, worst `0.0876 > 1/15` on the near-dyadic-flatter config `(0.45, 0.27, 0.18, 0.09)`-type. Still INSUFFICIENT but within 0.68%; the remaining failures are all "slightly flatter than dyadic" configs where every clean member lands just above `1/15`.
> 5. **Rich fixed-fraction family** (splits at fractions `{1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 4/5, 1/6, 5/6}` + barely-split + peel, random search 1500 three-move sequences/config) — **0 fails / 879 flat configs**. This family CAPS, confirming `c(3) = 8/15` is achievable. But the capping strategies use **continuously-tuned split points** (e.g. on the hardest config `(0.397, 0.303, 0.184, 0.117)`, the continuous optimum is `D ≈ 0.017 ≪ 1/15`, attained by splitting `p_1` at `0.488`, `p_2` at `0.390`, `p_4` barely — NOT a clean fraction).

**Diagnosis (honest):** the outline's plan — "regime-independent D-values (parity-XOR) + a minimax contradiction generalizing the n=2 §3.2 argument" — does NOT close for `n ≥ 3`. The clean regime-independent formulas (pairwise diffs, peel-complements, chain) get within 0.68% but do not cap; the residual failures require split points that are not clean fractions, so their `D`-values are not clean telescoping formulas and a §3.2-style finite contradiction does not materialize. Two paths remain (flagged, NOT closed this round):
1. **Find a richer CLEAN finite family** that caps — the 0.68% residual is small; more clever members (e.g. "EH three pieces with one at a non-1/2 ratio" giving a clean telescoping) might close it. The risk: each new member helps less (diminishing returns); the family may need to grow unboundedly with `n`.
2. **LP-dual / continuous argument** (diversity explorer framing B) — within a fixed sort-order regime, `D` is a linear functional of Xiang's split positions; the minimization is an LP, and the dual gives a weighting/potential certifying `D ≤ 1/D_n` per regime. This sidesteps the finite-family issue but abandons the "minimax over explicit strategies" framing (the approach's distinctive contribution). It is a rigor handle per-regime, not a standalone framing.

**Spec concern (flagged for the outline-reviewer):** the minimax-over-FINITE-family framing may be fundamentally insufficient for the `n ≥ 3` upper bound. The `n = 2` success (5 clean members cap exactly) appears to be a low-dimensional coincidence: for `n ≥ 3` the slack structure is richer and clean telescoping does not reach. If path 1 fails to close with a bounded family, the approach should concede G2-upper-n≥3 to a continuous-framing sibling (collapse-theorem's flattening, or LP-dual) and keep only the n=2 milestone + the certified regime `p_{n+1} ≤ 1/D_n` (equal-halve-n-largest, all n).

**Lower bound (shared, G1):** Liu's dyadic construction (§0, `pairing-charging` §3) plus Case A (largest piece `g_n` unsplit, all `n`: `S_odd ≥ g_n = 2^n/D_n` trivially) is PROVED. The splits-inequality G1 — `D ≥ 1/D_n` for the dyadic config under arbitrary Xiang splits, for `n ≥ 3` and the `n = 2` two-mark sub-case — is a SHARED GAP, being closed this round by sibling `dyadic-induction` via the parity-integral Route B / convexity argument (pending certification into `lemmas/splits-inequality.md`). For `n = 1` G1 is fully proved (§5); for `n = 2` it is verified by exhaustive finite check (outline-reviewer round-2). The `n ≥ 3` lower bound thus rests on G1.

---

### 7. Summary of rigorous progress (modular)

- **Greedy-alternating lemma:** imported (certified, §1).
- **D-reduction, parity-integral, toggle lemma:** imported / proved (§§ 1–2).
- **n = 1:** fully solved, both bounds (§5). `c(1) = 2/3`. ✓
- **n = 2 upper bound:** FULLY PROVED (§3). `c(2) ≤ 4/7`. ✓ Tight at dyadic with a non-pairing tie (§3.3); unique worst case at dyadic PROVED (§4).
- **n = 2 lower bound:** construction (Case A, `g_2` unsplit) PROVED; Case B (`g_2` split) = G1, verified by finite check, rigorous proof pending sibling `dyadic-induction` (shared gap). `c(2) ≥ 4/7` PENDING G1.
- **n ≥ 3:** upper bound OPEN (G2-upper-n≥3, §6); round-4 sweep shows naive chain fails (4938/20000), enriched 14-member clean family fails (204/30000, 0.68%), rich fixed-fraction family caps (0/879) but via continuous tuning — clean §3.2-style contradiction does NOT generalize; minimax-over-finite-family framing may be fundamentally insufficient. Spec concern flagged. Lower bound PENDING G1.

The proof is **not complete**. The approach's distinctive contribution is the n=2 upper bound, closed rigorously by a 5-member minimax-over-family with regime-independent D-values (via the parity-XOR framework), now internally consistent (M2 fixed), tight at dyadic with a genuine non-pairing tie. The n ≥ 3 upper bound and the shared G1 lower bound are the explicit open gaps.

---

## Promotable lemmas

- **Parity-XOR toggle lemma (§2).** *Statement: a Xiang split of a piece of length `p` into `u ≥ v` (with `u + v = p`) toggles the parity of `j(t) = #{pieces ≥ t}` on `[0, v) ∪ [u, p)` and leaves it unchanged elsewhere; in particular, an equal-halving split toggles parity on the whole `[0, p)`, and a barely-split toggles on two tiny intervals near `0` and near `p`.* Proved in full in §2 of `results/imo-2026-03/approaches/minimax-strategy-family.md`. (Already proved independently in `dyadic-induction` §2 / `pairing-charging`; recorded here for self-containedness. If the reviewer prefers a single canonical location, defer to `pairing-charging`'s version — the statements are equivalent.)
- **n=2 upper-bound menu (§3).** *Statement: for Liu 2-config `p_1 ≥ p_2 ≥ p_3`, `p_1 + p_2 + p_3 = 1`, the five explicit Xiang strategies M1 (equal-halve `p_1, p_2`), M2 (equal-halve `p_3` + barely-split `p_1`), M3 (equal-halve `p_1` + barely-split `p_2`), M4 (equal-halve `p_2` + barely-split `p_1`), M5 (split `p_1` to match `p_2`) attain `D`-values `p_3, p_1 − p_2, p_2 − p_3, p_1 − p_3, |2p_1 − 1|` respectively, each regime-independent (M2's value `p_1 − p_2` is verified by direct sort-computation in §3.1 — the `ε → 0` multiset `{p_1, p_2, p_3/2, p_3/2}` gives `D = p_1 − p_2` exactly); their min is `≤ 1/7 = 1/D_2` (the contradiction in §3.2 uses M1, M3, M2, M5 — M4 = `p_1 − p_3` is a redundant fifth member, valid but not load-bearing for the bound), tight at dyadic.* Proved in full in §3. **Reusable:** any sibling approach may import this to close the n=2 upper bound without re-deriving. (Not previously certified; proposed for `lemmas/n2-upper-bound.md` if the reviewer deems it broadly useful — but it is somewhat approach-specific, so certification is optional.)
- **Pairwise-difference realization (n=3, round 4).** *Statement: for Liu 3-config `p_1 ≥ p_2 ≥ p_3 ≥ p_4`, `Σ p_i = 1`, the strategy "equal-halve the two pieces in the complement of `{i, j}`" (2 marks; legal for `n = 3` since `2 ≤ 3`) attains `D = p_i − p_j` regime-independently, for every `1 ≤ i < j ≤ 4`. Concretely: EH `{p_3, p_4}` → `D = p_1 − p_2`; EH `{p_2, p_4}` → `D = p_1 − p_3`; EH `{p_2, p_3}` → `D = p_1 − p_4`; EH `{p_1, p_4}` → `D = p_2 − p_3`; EH `{p_1, p_3}` → `D = p_2 − p_4`; EH `{p_1, p_2}` → `D = p_3 − p_4`. (Mechanism: the two equal-halves form two equal pairs that cancel in `D` by the peeling/odd-rank parity argument; the two unsplit pieces remain, and `D` of two unequal pieces = `|difference|`.) Verified by direct sort-computation, 6 strategies × 2000 configs, max error 0. **Reusable:** gives any sibling approach a 2-mark strategy attaining any desired pairwise difference `p_i − p_j` for n=3. Generalizes to n ≥ 3: "EH the `n − 1` pieces not in `{i, j}`" (n−1 marks) gives `D = p_i − p_j`. Proposed for `lemmas/pairwise-diff-strategy.md` if the reviewer deems it broadly useful.
- **Peel-complement realization (n=3, round 4).** *Statement: for Liu 3-config, the 3-mark strategy "peel `p_1` vs `p_2`, peel `p_3` vs `p_4`, then peel the two remainders" attains `D = |2(p_1 + p_4) − 1|` regime-independently (and analogs for the other two complementary partitions `{p_1, p_3}+{p_2, p_4}` and `{p_1, p_4}+{p_2, p_3}`, giving `|2(p_1+p_3)−1|` and `|2(p_1+p_4)−1|` resp.). Mechanism: each peel creates a copy-pair (parity-neutral by peeling lemma), and the final lone is `(p_1−p_2)−(p_3−p_4) = p_1+p_4−p_2−p_3 = 2(p_1+p_4)−1` (using `Σ p_i = 1`). Verified by sort-match 800/800 configs. **Reusable:** gives a 3-mark strategy attaining `|2(p_i + p_j) − 1|` for each complementary pair, the n=3 generalization of the n=2 M5 `|2p_1−1|` closing quantity.

---

## Build notes

**What was PROVED this round:**
1. **n=2 upper bound, fully rigorous** (§3): the 5-member family `F_2` with regime-independent `D`-values (computed via parity-XOR), and a clean contradiction proof that `min ≤ 1/7` for all Liu 2-configs. Tight at dyadic. This is the concrete milestone the outline-reviewer approved.
2. **Unique-worst-at-dyadic for n=2** (§4): PROVED — the dyadic config is the unique maximizer of the family-minimax. This is the formalization of the diversity explorer's "cheap-kill structural fact" for n=2.
3. **n=1 both bounds** (§5): reproduced via the family (the minimax-over-two-options template, the n=1 crux aimo-0198 adaptation — `min(A, B) ≤ 1/3` at crossover `p_1 = 2/3`).
4. **Parity-XOR toggle lemma** (§2): proved from scratch (with the full `+1` on `[0,v)` AND `−1` on `[u,p)` decomposition, as the outline-reviewer required).
5. **Answer `c(n) = 2^n/D_n` verified for n=1,2,3** by direct computation at the dyadic equality cases (§0).

**Conjectures — proved vs flagged:**
- **Per-strategy regime guard (outliner step 2):** for n=2, DISPROVED AS A CONCERN — the `D`-values are regime-INDEPENDENT (parity-XOR computes `D` from the multiset, not the sorted order), so the guard holds trivially (with equality, not "decrease"). For n ≥ 3, the regime structure is richer and the guard is a real OPEN conjecture (flagged in §6).
- **Unique-worst-at-dyadic (outliner step 4):** PROVED for n=2 (§4); OPEN for n ≥ 3 (§6).
- **n=2 menu suffices:** PROVED — the 5-member family caps at 1/7 (§3.2). (The naive 3-member subset was indeed insufficient, as the diversity explorer warned — `1667/20k` configs exceed 1/7; the full 5-member family, including the split-to-match member M5 giving `|2p_1 − 1|` and the cross-piece barely-split members M2/M3/M4, is what closes it. M5 is critical: it is the member that caps configs near `p_1 = 1/2` where the other four are all `> 1/7`.)

**The n ≥ 3 open crux (honestly flagged):**
- **G2-upper-n≥3:** fixed 1–2-mark menus are VERIFIED insufficient for n=3 (worst `0.097 > 1/15`, 2875/100k exceed). The family must use the full `n`-mark adaptive refinement. The enumeration and minimax proof are OPEN. Two handles sketched (combinatorial regime tree; LP-dual-within-regime) but neither closed. If no finite family caps at `1/D_n` for `n ≥ 3`, the approach dies as an upper-bound route — but the n=2 milestone stands regardless.
- **G1 (lower bound, shared):** the splits-inequality is a SHARED GAP (pending sibling `dyadic-induction`'s certification into `lemmas/splits-inequality.md`); for `n = 2` verified by finite check.

**Distinctiveness preserved:** the minimax-over-family framing is genuinely different from `pairing-charging` (a single direct domino partition) and `alternating-potential` (a single amortized potential). Pairing (M1) is ONE family member, not the whole family; the barely-split (M2, M3, M4) and split-to-match (M5) members are the genuinely non-pairing contribution, and at the dyadic worst case they TIE with pairing (§3.3) — the minimax-over-family structure that a single-construction proof cannot exploit. The framing did NOT collapse into pairing (watch-out (c) heeded). The n ≥ 3 crux is the honest open question; it is not papered over.

**KB / crux citations:** *Invariants & monovariants* (D-reduction, parity-integral); *Double counting* / Fubini (parity-integral); *Extremal principle* / *Casework* (the 5-case contradiction in §3.2, the regime cases in §4); *Constructive vs existence* (the family is the explicit construction). Crux aimo-0198 (minimax-of-two-options, `min(A,B) ≤ (A+B)/2` crossover) — adapted from scratch as the n=1 template (§5) and generalized to the 5-member family for n=2 (§3); not cited, re-proved. The parity-XOR framework is the unifying lens (imported from `dyadic-induction` Lemma 2 / `pairing-charging`).

**Verification scripts (evidence, not proof):** `check_n2.py`, `check_n2_v2.py`, `check_n2_v3.py`, `verify_n2_full.py`, `verify_strategies.py` — all confirm the family `D`-values match the formulas across configs, the menu caps at `1/7` (worst `1/7`, 0 exceed over 700² grid), unique-worst-at-dyadic (all configs with min `= 1/7` are the dyadic config), and n=1 caps at `1/3`. The written proof stands on its own; these are sanity checks.

**Round-4 verification (M2 fix + n≥3 sweep):** `m2_verify.py` (M2 D-value = `p_1−p_2`, exact, 2000 configs, max error 0); `n2_menu_check.py` (n=2 menu caps at 1/7, 0/30000 exceed, all 5 formula values match); `n3_falsify.py` (naive chain + full-peel fails 4938/20000); `n3_broad.py` (140-strategy fixed family fails 826/4836); `n3_optimal.py` (continuous optimum on hardest config ~0.017 ≪ 1/15); `n3_formulas.py` (clean D-value formulas derived: EH12+BS3→p_3−p_4, EH1+BS2+EH3→p_2−p_4, BS1+EH23→p_1−p_4, peel2→|2(p_1+p_4)−1|, all regime-independent 800/800); `n3_enriched.py` (6 EH-two give all 6 pairwise diffs, verified 6×2000 error 0; 14-member enriched family: 204/30000 fail, worst 0.0876); `n3_fixedfrac.py` (rich fixed-fraction family caps, 0/879 fail). All written claims above are backed by these checks; the written proof (n=2) stands on its own.

---

## Round-4 build notes (this round)

**M2 XOR bug — FIXED (mandatory target 1, done first).** The §3.1 derivation of M2's D-value had a parity-XOR slip: it wrote `h = 1` (meaning `𝟙_{[0,p_3)}`) on `[p_3, p_2)`, but `𝟙_{[0,p_3)}(t) = 0` for `t ≥ p_3` — so `f' = f ⊕ 0 = 0` there (not `1`). The resulting integral was wrong (`p_1 − p_3` instead of `p_1 − p_2`). Fix: corrected the XOR row to `f=0, 𝟙_{[0,p_3)}=0, f'=0⊕0=0`, giving `∫ f' = p_1 − p_2`. The tiny barely-split toggles `B = [0, ε) ⊂ [0, p_3)` (where `f' = 0`, contrib `+ε`) and `C = [p_1−ε, p_1) ⊂ [p_2, p_1)` (where `f' = 1`, contrib `−ε`) still cancel, so `D = p_1 − p_2` (exact, for `ε < p_1 − p_2`). **Sort-verified**: the M2 multiset `{p_1−ε, ε, p_3/2, p_3/2, p_2}` sorted gives `j(t) = 5,4,2,1,0` on `[0,ε),[ε,p_3/2),[p_3/2,p_2),[p_2,p_1−ε),above`, hence `D = ε + (p_1−ε−p_2) = p_1−p_2` exactly (max error 0 over 2000 configs, both the full and limit multisets). Reconciliation: §3.1 derivation corrected; promotable-lemma menu corrected to `p_1−p_2`; the §3.2 theorem statement and §3.3 dyadic table ALREADY used `p_1−p_2` (no change). The §3.2 contradiction proof used `p_1 − p_2` in its step 3 all along — so the n=2 theorem was never actually wrong, only the §3.1 derivation of one member. **The n=2 upper bound stands, now internally consistent.**

**G2-flat n≥3 — ATTACKED, HONESTLY OPEN (mandatory target 2).** Ran the falsification sweep the outline-reviewer demanded BEFORE attempting a proof. Findings (all `fractions`-exact, sort-computed):
- The naive (n−1)-mark chain `{p_4, |2p_1−1|}` is VERIFIED insufficient (4938/20000 flat configs exceed 1/15) — confirms the single-gap-trap flag. The chain leaves TWO lone pieces (`r_{n−1}` and `p_{n+1}`); the n=2 M5 structure (one lone) does not transfer.
- Derived clean regime-independent D-value formulas for n=3 (verified 800/800 sort-match): "equal-halve two pieces `p_i, p_j`" gives `D = |p_a − p_b|` where `{a,b}` is the complement (all 6 pairwise diffs, verified 6×2000); "equal-halve `p_1,p_2` + barely-split `p_3`" gives `p_3 − p_4`; "barely-split `p_1` + equal-halve `p_2,p_3`" gives `p_1 − p_4`; the 3-mark peel "peel `p_1` vs `p_2`, peel `p_3` vs `p_4`, peel the two remainders" gives `|2(p_1+p_4) − 1|` (and analogs for the other 2 complement-pairs).
- The enriched 14-member clean family (6 diffs + `p_4` + `|2p_1−1|` + 6 peel-complements) reduces failures to 204/30000 (0.68%) but does NOT cap (worst 0.0876 > 1/15 on near-dyadic-flatter configs). Clean telescoping gets close but not there.
- A rich fixed-fraction family (splits at `{1/2, 1/3, 2/3, 1/4, 3/4, 1/5, 4/5, 1/6, 5/6}` + BS + peel) DOES cap (0/879 flat configs), but the capping strategies use continuously-tuned split points (continuous optimum ~0.017 on the hardest config), not clean fractions.

**Conclusion:** the outline's plan (regime-independent D-values + clean §3.2-style contradiction) does NOT close G2-flat n≥3. The n=2 success is a low-dimensional coincidence; for n≥3 the slack structure is richer and clean formulas don't telescope to a finite contradiction. The minimax-over-FINITE-family framing may be fundamentally insufficient for n≥3. **Spec concern flagged.** Two paths remain (not closed): (1) a richer clean finite family (the 0.68% residual is small but each new member helps less); (2) an LP-dual / continuous argument (sidesteps the finite-family issue but abandons the approach's distinctive framing). If path 1 fails, the approach should concede G2-upper-n≥3 to a continuous-framing sibling.

**Distinctiveness preserved:** the n=2 milestone (5-member minimax with non-pairing ties, unique-worst-at-dyadic) stands and is now internally consistent. The n≥3 crux is honestly open, not papered over.
