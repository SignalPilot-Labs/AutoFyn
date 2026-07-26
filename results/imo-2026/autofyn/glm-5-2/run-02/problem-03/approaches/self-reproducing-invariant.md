## Status
partial

## Approaches tried
- `self-reproducing-invariant` (round 6, NEW) — Genuinely-different G2 framing for general n: the pair-pile as a **self-reproducing invariant** on the pair-excess vector (crux `aimo-0262` Cinderella/Stepmother template adapted). The equality locus E_n (dyadic + ridge family R_e, all n >= 2) is where the invariant reproduces exactly (cap = alpha). A 2-strategy family (split-distance 1 or 2 on the active piece) covers the near-dyadic active+below perturbation with cap <= alpha. The far-from-dyadic closure is an OPEN GAP (single-gap-trap risk with two-regime explicitly noted). — Verdict: partial (self-reproduction + E_n + 2-strategy family rigorous; far-from-dyadic and active-grows-from-above gaps open).

## Current best
The pair-pile is formalized as a self-reproducing invariant on the pair-excess vector: pair-pile(n+1) = bisect(M) ++ pair-pile(n) (same integer pieces in D(n+1) units, n >= 2), A = 0 + 1 = alpha(n+1)*D(n+1). The equality locus E_n contains the dyadic (limit) and the ridge family R_e = (2^n,...,4, 2+e, 1-e)/D(n) for all n >= 2, e in (0,1), where A = alpha(n) exactly (pair-pile reproduces, compensating excesses (1-e)+e=1). A 2-strategy family (split at distance 1 or 2 from the left end of the active piece of dyadic size 4) gives cap <= alpha for the near-dyadic active+below perturbation (the piece of size 4 and the piece of size 2): dist-2 split gives A = 1 = alpha always (verified n=3..7, 0 violations), dist-1 split gives A = 1+2a (strict for a < 0, overshoot for a > 0, where a is the active perturbation; verified exact). The structural trichotomy (reproduce on E_n / strict when active shrinks / overshoot when active grows) is precisely characterized. OPEN GAPS: (1) "active grows from above" (perturbation transfers mass from a bisected piece to the active, piece below untouched): both strategies overshoot (A = 1+e > 1, verified n=4..6); (2) far-from-dyadic (balanced, extreme-dominant, moderate-dominant): completely open, the bare pair-pile overshoots (mirror probed dead, A=0.8 on extreme-dominant), and closure requires the S1/S3 sliver strategies which are two-regime's wall (single-gap-trap risk).

## Full proof
(Not yet — Status is `partial`. The self-reproducing invariant is formalized and proved on E_n and the 2-strategy family covers the near-dyadic active+below perturbation, but two gaps remain: "active grows from above" and far-from-dyadic. The approach does not prove c(n) for any n end-to-end; it targets the general-n U(n) upper bound, which is the larger open problem. The c(1)=2/3, c(2)=4/7, and c(3) lower bound stand from prior rounds.)

---

# Self-reproducing invariant — the pair-pile as a recursive invariant on the pair-excess vector

**Target.** Prove the non-strict upper bound `cap(P) := min_{Xiang marks} A(P, x) <= alpha(n) = 1/D(n)` for ALL Liu configs `P` at ALL `n` (= `U(n)`), via a self-reproducing invariant mechanism on the pair-excess vector. This is the **upper-bound half** of `c(n) = f(n) = 2^n/D(n)`; combined with the certified lower bound `L(n)` (cell-complex, open for general n) it would give `c(n) = f(n)`.

**Crux adapted.** `aimo-0262` (Cinderella/Stepmother): the defender (Cinderella = Xiang) maintains a **self-reproducing invariant** — a configuration of buckets that re-establishes after every adversary (Stepmother = Liu) move, capping every bucket at 1 < 2 forever. The bound comes from a disjoint-pair averaging argument (`y_0+y_1+y_2+y_3 <= 2` implies `y_0+y_2 <= 1` or `y_1+y_3 <= 1`). **Adaptation (not citation):** the pair-pile IS such a self-reproducing invariant — "after my marks, the pair-excess structure holds: every bisected pair has excess 0, the active pair has excess 1, total `A = alpha(n)`." The ridge finding shows this invariant **reproduces under level-1-exact perturbations** (the pair-pile absorbs deeper-level perturbation, residual excesses `(1-e)+e = 1` sum to `alpha`). The reproduction is **structural** (the invariant at level n+1 contains the invariant at level n as a sub-structure), not **temporal** (our game has one round, not a sequence — the adaptation replaces aimo-0262's temporal re-establishment with a structural recursion). Every step below is proved from scratch.

**Conventions.** All lengths in `1/D(n)` integer units (`D(n) = 2^{n+1} - 1`). The advantage `A = sum of pair-excesses (+ leftover if odd piece count)`. By Lemma G (certified `lemmas/lemma-g-greedy-picking.md`), `Liu = (1 + A/D(n))/2`, so `Liu <= f(n)` iff `A <= 1`. The pair-pile (certified `lemmas/lemma-pair-pile-dyadic-cap.md`) uses `n-1` marks (for `n >= 2`; 1 mark for `n = 1`), giving `2n` pieces (even count), `A = sum_{i=1}^{n} e_i` where `e_i = p_{2i-1} - p_{2i}` (no leftover).

## 1. The invariant: the pair-pile as a self-reproducing invariant on the pair-excess vector

### 1.1. The pair-pile structure (review of the certified construction)

For the level-`n` dyadic config `P_n^* = (2^n, 2^{n-1}, ..., 4, 2, 1)/D(n)` (Liu's `n` marks at cumulative sums of `(1, 2, ..., 2^{n-1})/D(n)`), the pair-pile strategy (certified `lemmas/lemma-pair-pile-dyadic-cap.md`) places `n-1` marks (for `n >= 2`):
- **Bisect** each piece of dyadic size `2^k` for `k = 3, 4, ..., n` (i.e. sizes `8, 16, ..., 2^n`): mark at the piece's midpoint, splitting `2^k -> (2^{k-1}, 2^{k-1})` (an equal pair, excess `0`).
- **Split** the piece of dyadic size `4` (= `2^2`, the piece at 0-based index `n-2`) at distance `1` from its left end: `4 -> (1, 3)`.
- **Leave** the two smallest pieces (dyadic sizes `2` and `1`, 0-based indices `n-1` and `n`) untouched.

The resulting multiset (in `1/D(n)` units) is the **pair-pile**:
```
2^{n-1}, 2^{n-1}, 2^{n-2}, 2^{n-2}, ..., 4, 4, 3, 2, 1, 1   (n >= 3),
```
with `2n` pieces summing to `D(n)`. Consecutive sorted pairs: each `(2^k, 2^k)` has excess `0`; the pair `(3, 2)` has excess `1`; the pair `(1, 1)` has excess `0`. So `A = 0 + ... + 0 + 1 + 0 = 1 = alpha(n) * D(n)`, giving `Liu = f(n)` (by Lemma G). For `n = 2`: pair-pile `(3, 2, 1, 1)`, `A = 1`. For `n = 1`: pair-pile `(1, 1, 1)`, `A = 1` (odd count, leftover `1`).

### 1.2. The pair-excess vector and the invariant

**Definition (pair-excess vector).** Given a sorted-desc partition into `2n` pieces `(p_1, ..., p_{2n})` (the result of Xiang's `n-1` marks on Liu's `n+1` pieces), the **pair-excess vector** is `(e_1, ..., e_n)` where `e_i = p_{2i-1} - p_{2i} >= 0`. The advantage is `A = sum_{i=1}^{n} e_i`. (For `2n+1` pieces, add the leftover `ell = p_{2n+1}`; `A = sum e_i + ell`. The pair-pile always produces `2n` pieces, so we work with the even-count form.)

**Definition (the pair-pile invariant).** The pair-pile invariant on level `n` is the pair-excess vector satisfying:
- Each bisected pair `(2^{k-1}, 2^{k-1})` has excess `e = 0`.
- The active pair `(3, 2)` (from the split of the piece of size `4`) has excess `e = 1`.
- The bottom pair `(1, 1)` has excess `e = 0`.
- **Invariant value:** `A = sum e_i = 1 = alpha(n) * D(n)`.

### 1.3. The self-reproduction rule

**Theorem (self-reproduction, n >= 2).** *The pair-pile on level `n+1` is the disjoint union of the bisected dominant piece `M = 2^{n+1}/D(n+1)` (split into the equal pair `(2^n, 2^n)`, excess `0`) and the pair-pile on the level-`n` sub-config `R = (2^n, 2^{n-1}, ..., 1)/D(n+1)` (the bottom `n` pieces of the level-`(n+1)` dyadic). The integer pieces are identical (the pair-pile(n) multiset appears verbatim in `D(n+1)` units); the advantage satisfies `A_{n+1} = 0 + 1 = 1 = alpha(n+1) * D(n+1)`.*

**Proof.** The level-`(n+1)` dyadic is `P_{n+1}^* = (2^{n+1}, 2^n, ..., 4, 2, 1)/D(n+1)`. The dominant piece is `M = 2^{n+1}/D(n+1)` (piece 1); the remaining `n` pieces form `R = (2^n, 2^{n-1}, ..., 4, 2, 1)/D(n+1)`, which is the level-`n` dyadic scaled by `D(n)/D(n+1)` (since `(2^n, ..., 1)` sums to `D(n)` and `D(n)/D(n+1)` is the scale factor, but the INTEGER pieces in `D(n+1)` units are `(2^n, ..., 1)` — the same integers as the level-`n` dyadic in `D(n)` units).

The pair-pile on level `n+1` applies `n` marks:
- **Mark 1:** bisect piece `M = 2^{n+1}` at its midpoint `-> (2^n, 2^n)` (equal pair, excess `0`).
- **Marks 2 to n:** apply the pair-pile strategy to the sub-config `R`. Since `R`'s pieces (in `D(n+1)` units) are `(2^n, 2^{n-1}, ..., 4, 2, 1)` — the same integers as the level-`n` dyadic in `D(n)` units — the pair-pile marks on `R` produce the pair-pile(n) multiset `(2^{n-1}, 2^{n-1}, ..., 4, 4, 3, 2, 1, 1)` in `D(n+1)` units (the marks are at the same RELATIVE positions within `R`, which spans `[2^{n+1}/D(n+1), 1]`).

The full pair-pile(n+1) multiset is `{2^n, 2^n} union pair-pile(n)` = `(2^n, 2^n, 2^{n-1}, 2^{n-1}, ..., 4, 4, 3, 2, 1, 1)` in `D(n+1)` units. Sum: `2 * 2^n + D(n) = 2^{n+1} + D(n) = D(n+1)`. ✓

The advantage: the `(2^n, 2^n)` pair contributes `0`; the pair-pile(n) structure contributes `1` (the `(3, 2)` pair). So `A_{n+1} = 0 + 1 = 1 = alpha(n+1) * D(n+1)`. ∎

**Operationally, "reproduces" means:** the pair-pile on level `n+1` CONTAINS the pair-pile on level `n` as a sub-structure (the same integer pieces, at the same relative positions, within the `R` sub-config). The dominant piece `M` is bisected into a zero-excess pair, and the pair-pile(n) invariant on `R` is re-established verbatim. The integer advantage stays `1`; the real advantage rescales from `1/D(n) = alpha(n)` to `1/D(n+1) = alpha(n+1)`. (Verified by exact-rational computation for `n = 2, ..., 5`: piece multiset match, `A` match, sum match. File: `/tmp/round-6/self_repro_verify.py`, section 5/13.)

**Remark (the aimo-0262 analogy).** In aimo-0262, Cinderella's invariant re-establishes after every Stepmother move (temporal reproduction). Here, the "adversary move" is Liu's choice of config `P`; the "defender response" is Xiang's pair-pile. The reproduction is **structural**: the pair-pile at level `n+1` is built FROM the pair-pile at level `n` (recursive construction), and — as the ridge (Section 2) shows — the invariant value `A = alpha` is preserved under perturbations of the bottom pieces (the pair-excesses shift but their sum stays `1`). The temporal "re-establish after each move" becomes the structural "re-establish under each perturbation class."

## 2. E_n characterization: the equality locus

### 2.1. The ridge family (all n >= 2)

**Definition (ridge family).** For `n >= 2` and `e in (0, 1)`, the **ridge** is the config
```
R_e^{(n)} = (2^n, 2^{n-1}, ..., 4, 2+e, 1-e) / D(n),
```
i.e. the level-`n` dyadic with the bottom two pieces (sizes `2` and `1`) perturbed by `(+e, -e)` (compensating, sum preserved). Level 1 through level `n-2` are exact (every `p_i = 2 p_{i+1}` for `i = 1, ..., n-2`); levels `n-1` and `n` are broken.

**Theorem (ridge reproduction, all n >= 2).** *For every `n >= 2` and `e in (0, 1)`, the pair-pile strategy on `R_e^{(n)}` gives `A = 1 = alpha(n) * D(n)`. The pair-pile invariant reproduces on the ridge.*

**Proof.** The pair-pile strategy touches pieces of dyadic size `2^k` for `k = 2, ..., n` (0-based indices `0` to `n-2`), i.e. all pieces except the bottom two. On `R_e^{(n)}`, the top `n-1` pieces are unchanged (same as the dyadic), so the pair-pile applies the same marks: bisects pieces of size `2^k` for `k >= 3` into `(2^{k-1}, 2^{k-1})`, and splits the piece of size `4` (at 0-based index `n-2`) into `(1, 3)`. The bottom two pieces `(2+e, 1-e)` are left untouched.

The final multiset (in `1/D(n)` units):
```
{2^{n-1}, 2^{n-1}, 2^{n-2}, 2^{n-2}, ..., 4, 4, 3, 2+e, 1, 1-e}.
```
For `e in (0, 1)`: `3 > 2 + e` (iff `e < 1`, ✓) and `1 > 1 - e` (iff `e > 0`, ✓). So the sorted order is `2^{n-1}, 2^{n-1}, ..., 4, 4, 3, 2+e, 1, 1-e` (the perturbed pieces sit below the split piece `3` and above the split piece `1`).

Pair-excesses:
- Each `(2^{k}, 2^{k})` pair: excess `0`.
- Pair `(3, 2+e)`: excess `3 - (2+e) = 1 - e`.
- Pair `(1, 1-e)`: excess `1 - (1-e) = e`.

Sum: `A = 0 + ... + 0 + (1-e) + e = 1`. So `A = 1/D(n) = alpha(n)`. ∎

**Remark (compensation mechanism).** The perturbation `(+e, -e)` on the bottom two pieces shifts the pair-excesses from `(1, 0)` (dyadic: `(3,2)` and `(1,1)`) to `(1-e, e)` (ridge: `(3, 2+e)` and `(1, 1-e)`). The excesses **compensate**: `(1-e) + e = 1` regardless of `e`. This is the self-reproducing invariant in action — the pair-excess vector changes, but its sum (the invariant value `A = alpha`) is preserved. The pair-pile's level-1-through-(n-2) exactness (all bisected pairs, excess `0`) is the "free" structure that absorbs the perturbation; the active pair `(3, ?)` and the bottom pair `(1, ?)` are the "active" components where the compensation happens.

**Import of the certified ridge-falsification lemma.** The certified `lemmas/lemma-ridge-falsification.md` records that the strict-decrease conjecture `Phi > 0 => cap < alpha(n)` is FALSE — the ridge `R_e^{(3)}` has `Phi = 5e > 0` yet `cap = alpha(3)` (the pair-pile achieves `A = alpha(3)`). We use this NOT as a strict-decrease (dead) but as the **E_n witness**: the ridge is a non-dyadic config where the pair-pile invariant reproduces exactly. The dyadic is NOT an isolated point of `E_n`; `E_n` is positive-dimensional (parametrized by `e`). Theorem 2.1 generalizes the n=3 ridge (certified) to all `n >= 2`.

### 2.2. The equality locus E_n

**Definition (E_n, the equality locus).** `E_n` is the set of configs `P` (sorted-desc, `n+1` pieces summing to `1`) for which the pair-pile strategy gives `A = alpha(n) * D(n) = 1` (integer scale).

**Theorem (E_n contains the dyadic and the ridge).** *`E_n` contains (i) the level-`n` dyadic `P_n^*` (for all `n >= 1`; certified `lemmas/lemma-pair-pile-dyadic-cap.md`); (ii) the ridge family `R_e^{(n)}` for all `n >= 2`, `e in (0, 1)` (Theorem 2.1).*

**Proof.** (i) is the certified pair-pile construction. (ii) is Theorem 2.1. ∎

**Conjecture (general form of E_n, OPEN).** The explorer's round-6 report conjectures that `E_n` is the set of configs where, for some `j`, levels `1, ..., j` are exact and levels `j+1, ..., n` are perturbed with pair-excesses summing to `alpha(n)`. The ridge is the case `j = n-2` (levels `1, ..., n-2` exact, levels `n-1, n` perturbed). Testing deeper perturbations (level `j` broken for `j < n-1`) shows the pair-pile does NOT reproduce on all such configs (e.g. perturbing the piece of size `4` from above causes overshoot — see Section 4). The precise characterization of `E_n` beyond the ridge is an **OPEN GAP**.

## 3. The 2-strategy family: near-dyadic active+below perturbation

### 3.1. The active piece and the two split strategies

The pair-pile has exactly one **active piece**: the piece of dyadic size `4` (0-based index `n-2`), split at distance `1` from its left end into `(1, 3)`. All other touched pieces are bisected into equal pairs (excess `0`). The two bottom pieces (sizes `2` and `1`) are untouched.

**Definition (split-distance strategies).** The **dist-d strategy** (for `d in {1, 2}`) modifies the pair-pile by splitting the active piece at distance `d` from its left end:
- `d = 1` (pair-pile): active piece of size `4 + a` -> `(1, 3 + a)`.
- `d = 2` (modified): active piece of size `4 + a` -> `(2, 2 + a)`.

All other marks are identical (bisect top pieces, leave bottom two untouched). Each uses `n - 1 <= n` marks.

### 3.2. The active+below perturbation and the 2-strategy bound

**Setup.** Consider a perturbation of the dyadic where the active piece (size `4`) and the piece below it (size `2`) are perturbed by `(+a, -a)` (compensating, sum preserved): active piece becomes `4 + a`, piece below becomes `2 - a`. The top `n - 2` pieces and the bottom piece (size `1`) are unchanged (dyadic). Call this the **active+below perturbation** with parameter `a`. Validity: `4 + a > 0` and `2 - a > 0`, so `a in (-4, 2)`; and the sort is preserved when `4 + a >= 2 - a` (i.e. `a >= -1`) and `2 - a >= 1` (i.e. `a <= 1`), so `a in (-1, 1)`.

**Theorem (2-strategy bound for active+below, all n >= 3).** *For the active+below perturbation with `a in (-1, 1)`, Xiang's 2-strategy family (dist-1 or dist-2 split on the active piece) achieves `A <= 1 = alpha(n) * D(n)`. Specifically:*
- *dist-1 (pair-pile): `A = 1 + 2a` (valid for `a in (-1/2, 1)`; strict `< 1` for `a < 0`, overshoot `> 1` for `a > 0`).*
- *dist-2 (modified): `A = 1` for all `a in (-1, 1)`.*
- *So `min(A_{dist1}, A_{dist2}) <= 1` for all `a in (-1/2, 1)`.*

**Proof.** The top `n - 2` pieces are dyadic and bisected into equal pairs (excess `0` each). The bottom piece (size `1`) is untouched. Only the active pair and the bottom pair contribute to `A`.

**dist-1 (pair-pile).** Active piece `4 + a` split at distance `1 -> (1, 3 + a)`. Piece below `2 - a` untouched. Bottom piece `1` untouched. Bottom 4 pieces: `{3 + a, 2 - a, 1, 1}`. For `a in (-1/2, 1)`: `3 + a > 2 - a` (iff `a > -1/2`) and `2 - a > 1` (iff `a < 1`). Sorted: `3 + a, 2 - a, 1, 1`. Pairs: `(3+a, 2-a) -> 1 + 2a`; `(1, 1) -> 0`. `A = 1 + 2a`. (For `a > 0`: `A > 1`, overshoot. For `a < 0`: `A < 1`, strict. For `a = 0`: `A = 1`, ridge.)

**dist-2 (modified).** Active piece `4 + a` split at distance `2 -> (2, 2 + a)`. Piece below `2 - a` untouched. Bottom piece `1` untouched. Bottom 4 pieces: `{2 + a, 2, 2 - a, 1}` (the `2 + a` is the rest of the active piece, `2` is from the split, `2 - a` is the perturbed piece below, `1` is the untouched bottom piece). For `a in (-1, 1)`, all four values are positive. Three sub-cases by the sign of `a`:
- **`a > 0`:** `2 + a > 2 > 2 - a > 1`. Pairs: `(2+a, 2) -> a`; `(2-a, 1) -> 1 - a`. `A = a + (1-a) = 1`.
- **`a < 0`:** `2 - a > 2 > 2 + a > 1`. Pairs: `(2-a, 2) -> -a`; `(2+a, 1) -> 1 + a`. `A = -a + (1+a) = 1`.
- **`a = 0` (ridge):** `{2, 2, 2, 1}`. Sorted: `2, 2, 2, 1`. Pairs: `(2, 2) -> 0`; `(2, 1) -> 1`. `A = 1`.

In all cases, `A_{dist2} = 1`. Combined with `A_{dist1} = 1 + 2a`:
- For `a >= 0`: `A_{dist2} = 1 <= 1`. ✓ (use dist-2)
- For `a < 0`: `A_{dist1} = 1 + 2a < 1`. ✓ (use dist-1)
- For `a = 0` (ridge): `A = 1` (both). ✓

So `min(A_{dist1}, A_{dist2}) <= 1` for all `a in (-1/2, 1)`. ∎

**Verification.** Exact-rational computation (`fractions.Fraction`) for `n = 3, 4, 5, 6, 7`, `a` from `-0.9` to `0.9` in steps of `0.1` (restricting to sort-valid `a`): dist-2 gives `A = 1` (0 violations); dist-1 gives `A = 1 + 2a` (0 mismatches). File: `/tmp/round-6/self_repro_verify.py`, sections 9, 15, 16.

### 3.3. The structural trichotomy

The pair-pile (dist-1) on near-dyadic perturbations of the active+below pair exhibits a clean **trichotomy**:

| Perturbation direction | Active piece | Piece below | `A` (dist-1) | `A` (dist-2) | Status |
|---|---|---|---|---|---|
| `a = 0` (ridge) | `4` | `2` | `1` | `1` | reproduce (= alpha) |
| `a < 0` (active shrinks) | `4 + a < 4` | `2 - a > 2` | `1 + 2a < 1` | `1` | strict (< alpha) |
| `a > 0` (active grows) | `4 + a > 4` | `2 - a < 2` | `1 + 2a > 1` | `1` | dist-1 overshoot, dist-2 reproduce |

The pair-pile reproduces on the ridge (`a = 0`), strict-decreases when the active piece shrinks (`a < 0`), and **overshoots** when the active piece grows (`a > 0`) — but the dist-2 strategy absorbs the growth (reproduce, `A = 1`). The 2-strategy family covers all three cases with `A <= 1`.

This is the near-dyadic mechanism: the invariant `A = 1` is preserved (dist-2 for growth, dist-1 for shrink), and the pair-pile's recursive structure (bisected pairs absorb all perturbations not involving the active piece) confines the "action" to the active pair and the bottom pair.

## 4. Open gaps (honest)

### Gap 1: "Active grows from above" (near-dyadic, OPEN)

Consider a perturbation where mass is transferred FROM a bisected piece (above the active) TO the active piece: the piece of dyadic size `8` (0-based index `n-3`) shrinks by `e`, and the active piece (size `4`, index `n-2`) grows by `e`. The piece below (size `2`, index `n-1`) is **untouched**.

**The pair-pile (dist-1) overshoots:** active piece `4 + e` split at distance `1 -> (1, 3 + e)`. Piece below `2` untouched. Bottom 4 pieces: `{3 + e, 2, 1, 1}`. Pairs: `(3+e, 2) -> 1 + e`; `(1, 1) -> 0`. `A = 1 + e > 1`. **Overshoot.**

**The dist-2 strategy also overshoots:** active piece `4 + e` split at distance `2 -> (2, 2 + e)`. Bottom 4 pieces: `{2 + e, 2, 2, 1}`. Sorted: `2 + e, 2, 2, 1`. Pairs: `(2+e, 2) -> e`; `(2, 1) -> 1`. `A = e + 1 = 1 + e > 1`. **Overshoot** (the two `2`'s — one from the split, one the untouched piece below — tie and pair with each other, leaving `(2+e, 2) -> e` and `(2, 1) -> 1`).

**Both strategies fail** because the piece below is untouched (`= 2`), so the excess `(3+e) - 2 = 1+e` (dist-1) or `e + 1 = 1+e` (dist-2) has no compensating term. In the active+below perturbation (Section 3), the piece below was perturbed (`2 - a`), providing the compensation; here it is not.

**Verification.** Exact-rational for `n = 4, 5, 6`, `e in {1/10, 1/5, 3/10}`: both dist-1 and dist-2 give `A = 1 + e > 1` (0 strategies succeed). File: `/tmp/round-6/self_repro_verify.py`, section 17.

**Status: OPEN.** A third strategy (e.g. bisecting the piece below, or using a local-kink-type mark on the bisected piece above) might close this, but I have not found one. For `n = 3` specifically, the certified `lemmas/lemma-local-kink-level1.md` handles the analogous case (mass-down, piece 1 shrinks) with a dyadic-position mark on piece 1, but this does not generalize to `n >= 4` (where the perturbation involves an interior bisected piece, not the top piece).

### Gap 2: Far-from-dyadic (OPEN, single-gap-trap risk)

For configs far from the dyadic — balanced `(w, ..., w)`, extreme-dominant `(L, t, t, t)`, moderate-dominant — the bare pair-pile **overshoots**. The mirror (a single self-similar strategy, probed this round) overshoots to `A = 0.8` on extreme-dominant `(.9, 1/30, 1/30, 1/30)` and `A = 0.2` on moderate-dominant `(.6, .25, .1, .05)` (24410/30000 random `n = 3` configs violate; file: `/tmp/round-6/math-explorer-new-g2-framing.md`, Opening 5). The pair-pile is tight ONLY on `E_n` (dyadic + ridge + symmetric configs).

**Closure of this gap requires the S1/S3 sliver strategies** (certified `lemmas/lemma-s1-balanced-sliver.md` for balanced, and the two-dyadic / extreme-dominant slivers in `approaches/two-regime-disjunctive.md` for the other classes). These are `two-regime-disjunctive`'s territory.

**Single-gap-trap risk (explicitly noted).** The outline-reviewer's gate warning is correct: if the far-from-dyadic closure of this approach reduces to importing `two-regime`'s S1/S3 slivers as "family members," this approach becomes a near-twin of `two-regime` and dies if `two-regime`'s wall fails. I do NOT paper over this: the far-from-dyadic closure is an **OPEN GAP**, and the approach is scoped to **near-dyadic + E_n only**. The genuinely-different contribution is the self-reproducing invariant mechanism (Sections 1-3) on the near-dyadic regime, NOT the far-from-dyadic closure.

### Gap 3: The aimo-0262 disjoint-pair averaging (does not directly translate)

In `aimo-0262`, the bound comes from a disjoint-pair averaging: `y_0 + y_1 + y_2 + y_3 <= 2` implies `y_0 + y_2 <= 1` OR `y_1 + y_3 <= 1` (pigeonhole on two disjoint pairs). The analogue for our pair-excess vector `A = sum e_i` would require splitting the `n` pair-excesses into two disjoint sub-collections whose sums are individually bounded, forcing one `<= alpha/2`. But `A` is a **sum** (not a max of buckets), and the pair-excesses are already the natural disjoint pairs — there is no further disjoint-pair structure to exploit for an upper bound. The disjoint-pair averaging of `aimo-0262` does NOT directly translate to a universal `cap <= alpha` proof; the self-reproduction mechanism (Sections 1-3) is the genuinely-different contribution, and it covers only the near-dyadic regime.

## 5. Summary of rigorous progress

**Proved (rigorous, all n):**
1. The self-reproduction recursion: pair-pile(n+1) = bisect(M) ++ pair-pile(n), `A = alpha(n+1)` (Theorem 1.3, n >= 2).
2. The ridge family `R_e^{(n)}` (all n >= 2, e in (0,1)): pair-pile reproduces, `A = alpha(n)` (Theorem 2.1).
3. E_n contains the dyadic + the ridge (Theorem 2.2).
4. The 2-strategy bound for active+below perturbation: `A <= alpha(n)` for all `a in (-1/2, 1)` (Theorem 3.2, n >= 3).
5. The structural trichotomy (Section 3.3): reproduce / strict / overshoot, precisely characterized.

**Open gaps (honest):**
1. "Active grows from above" (near-dyadic, both strategies overshoot, n >= 4).
2. Far-from-dyadic (balanced, extreme-dominant, moderate-dominant): OPEN, single-gap-trap risk with two-regime noted.
3. The general form of E_n (beyond the ridge): OPEN.
4. The disjoint-pair averaging of aimo-0262 does NOT directly translate to a universal upper bound.

**What this approach does NOT prove:** `c(n) = f(n)` for any `n` end-to-end. It targets the general-n `U(n)` upper bound and proves a **near-dyadic + E_n sub-case**. The certified results `c(1) = 2/3`, `c(2) = 4/7` (prior rounds), `L(3)` / `L(4)` over reals (cell-complex, prior rounds), and `U(3)` partial (two-regime, round 5) stand independently. This approach's contribution is the **self-reproducing invariant framing** of the near-dyadic upper bound — a genuinely-different G2 mechanism (far from the dead 2-adic strict-decrease and the two-regime 17-family casework) that may, with the far-from-dyadic gap closed by a different mechanism, lift to universal `U(n)`.

## Promotable lemmas

1. **Self-reproduction of the pair-pile (Theorem 1.3).** *For n >= 2, the pair-pile on level n+1 is the disjoint union of the bisected dominant piece (excess 0) and the pair-pile on the level-n sub-config R (same integer pieces in D(n+1) units), giving A_{n+1} = alpha(n+1).* Proved in Section 1.3. Candidate for `lemmas/lemma-pair-pile-self-reproduction.md`. (Structural recursion; does NOT close U(n) but provides the self-reproducing-invariant foundation.)

2. **Ridge reproduction (Theorem 2.1).** *For all n >= 2 and e in (0,1), the pair-pile on R_e^{(n)} = (2^n, ..., 4, 2+e, 1-e)/D(n) gives A = alpha(n), with compensating excesses (1-e) + e = 1.* Proved in Section 2.1. Generalizes the n=3 certified `lemma-ridge-falsification.md` (which records the falsification) to all n, and establishes the POSITIVE result (pair-pile reproduces) rather than just the negative (strict-decrease is false). Candidate for `lemmas/lemma-ridge-reproduction-all-n.md`.

3. **2-strategy bound for active+below perturbation (Theorem 3.2).** *For the near-dyadic active+below perturbation (active piece 4+a, piece below 2-a, a in (-1, 1)), Xiang's 2-strategy family (dist-1 or dist-2 split on the active piece) achieves A <= alpha(n) for all n >= 3.* Proved in Section 3.2. The dist-2 split gives A = 1 always; the dist-1 split gives A = 1+2a (strict for a < 0). Candidate for `lemmas/lemma-2strategy-active-below.md`.

---

**Build summary.** This round built the `self-reproducing-invariant` approach from scratch: formalized the pair-pile as a recursive self-reproducing invariant on the pair-excess vector (Theorem 1.3), proved the ridge family reproduces for all n >= 2 (Theorem 2.1, generalizing the certified n=3 ridge falsification), and proved a 2-strategy family (dist-1/dist-2 split on the active piece) gives cap <= alpha for the near-dyadic active+below perturbation (Theorem 3.2, all n >= 3). The structural trichotomy (reproduce/strict/overshoot) is precisely characterized. Two honest open gaps remain: (1) "active grows from above" (both strategies overshoot, n >= 4), and (2) far-from-dyadic (OPEN, single-gap-trap risk with two-regime explicitly noted — the approach is scoped to near-dyadic + E_n only, not papered over with S1/S3 slivers). The aimo-0262 disjoint-pair averaging does NOT directly translate (our A is a sum, not a max). All computations verified with exact-rational arithmetic (`fractions.Fraction`, file `/tmp/round-6/self_repro_verify.py`, 17 test sections, 0 unexpected violations). Three promotable lemmas proposed. Status: partial.
