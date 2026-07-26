# Lemma: U(3) — 5-cap dominant-regime contradiction (d ≥ 1/2, equality iff dyadic)

**Status:** CERTIFIED (round 5, proof-reviewer). Proved in `approaches/two-regime-disjunctive.md` §5d.2. Reviewer re-derived the five cap formulas and the 2-case contradiction with exact-rational python (grids `N = 60, 90, 120, 150` + 50k random reals over `d ≥ 1/2`, 0 violations, unique equality at the dyadic).

## Statement

For every `n = 3` Liu config `(a, b, c, d)`, `a ≤ b ≤ c ≤ d`, `a + b + c + d = 1`, `d ≥ 1/2` (the dominant regime), Xiang with `3` marks forces

```
min(a, b − a, c − b, 2d − 1, |a + b − c|) ≤ α(3) = 1/15,
```

hence `Liu ≤ 8/15 = f(3)` (via `Liu = (1 + A)/2`), with **equality** (the min `= 1/15`) **iff** `(a, b, c, d) = (1, 2, 4, 8)/15` (the order-3 dyadic).

## The five cap strategies (each ≤ 3 marks)

Let `A = p_1 − p_2 + p_3 − … + p_7` (7 final pieces, sorted desc). Each strategy creates cancelling equal-pairs plus a singleton whose value is the named cap:

- `S_a` (bisect `b, c, d`; 3 marks): pairs `(b/2,b/2),(c/2,c/2),(d/2,d/2)`; singleton `a`. `A = a`.
- `S_{b−a}` (match `a` in `b` + bisect `c, d`; 3 marks): pairs `(a,a),(c/2,c/2),(d/2,d/2)`; singleton `b − a`. `A = b − a`.
- `S_{c−b}` (match `b` in `c` + bisect `a, d`; 3 marks): pairs `(b,b),(a/2,a/2),(d/2,d/2)`; singleton `c − b`. `A = c − b`.
- `S_{2d−1}` (match `a, b, c` in `d`; 3 marks, **admissible iff `d ≥ a + b + c ⟺ d ≥ 1/2`**): pairs `(a,a),(b,b),(c,c)`; singleton `d − a − b − c = 2d − 1 ≥ 0`. `A = 2d − 1`.
- `S_{|a+b−c|}` (bisect `d` + match `a` in `c`; 2 marks): pairs `(d/2,d/2),(a,a)`; two singletons `b, c − a`. By the equal-pair cancellation lemma, `A = |b − (c − a)| = |a + b − c|`.

Each formula is verified by direct multiset alt-sum (exact rational). The equal-pair cancellation lemma: in a sorted-desc multiset, a block of even multiplicity at a single value contributes `0`; for `2m+1` pieces with `m` equal-pairs + 1 singleton the singleton is at the leftover odd rank; for `2m` pieces with `m−1` pairs + 2 singletons the larger singleton sits at the odd rank, giving `A = (larger) − (smaller) = |difference|`.

## Proof of the contradiction

Assume for contradiction all five caps `> 1/15`. Then:
1. `a > 1/15`,
2. `b − a > 1/15` ⟹ `b > a + 1/15`,
3. `c − b > 1/15` ⟹ `c > b + 1/15`,
4. `2d − 1 > 1/15` ⟹ `d > 8/15` (and `2d − 1 ≥ 0` by `d ≥ 1/2`),
5. `|a + b − c| > 1/15` ⟹ **Case i** `c < a + b − 1/15` OR **Case ii** `c > a + b + 1/15`.

From (1)–(3): `a > 1/15`, `b > 2/15`, `c > 3/15`, so `a + b + c > 6/15`, hence `d = 1 − (a + b + c) < 9/15`. Combined with (4): `8/15 < d < 9/15`.

**Case i:** `c < a + b − 1/15` with (3) `c > b + 1/15` ⟹ `a > 2/15`. Then `b > 3/15`, `c > 4/15`, `a + b + c > 9/15`, so `d < 6/15`, contradicting `d > 8/15`. ✓ contradiction.

**Case ii:** `c > a + b + 1/15` with (1),(2) `a + b > 3/15` ⟹ `a + b + c > 2(a + b) + 1/15 > 7/15`, so `d < 8/15`, contradicting `d > 8/15`. ✓ contradiction.

Both cases contradict, so at least one cap `≤ 1/15`.

**Equality analysis** (replace `>` with `≥`): Case i impossible under `≥` (forces `d ≤ 6/15` contradicting `d ≥ 8/15`). Case ii gives `a + b + c ≥ 7/15` ⟹ `d ≤ 8/15`; combined with `d ≥ 8/15` forces `d = 8/15` and all intermediate inequalities to equality: `a = 1/15`, `b = 2/15`, `c = 4/15`. Hence `(a, b, c, d) = (1, 2, 4, 8)/15`. ∎

## Verification

Exact rational arithmetic on grids `N = 60, 90, 120, 150` over `a ≤ b ≤ c ≤ d`, `d ≥ 1/2`: 0 violations; unique equality config exactly `(1/15, 2/15, 4/15, 8/15)`. At the dyadic, four of the five caps tie at `1/15` (`a, b − a, 2d − 1, |a + b − c|`); `c − b = 2/15` is loose.

## Reusability

The direct `n = 3` generalization of the certified `U(2)` four-strategy lemma. Closes the dominant regime of `U(3)` rigorously. Combined with `L(3)` (CERTIFIED, cell-complex) and the `d < 1/2` sliver (`lemma-u3-sliver-gap.md`) + 17-family, contributes to the `c(3) = 8/15` upper-bound half. The moderate-dominant class `L = d ∈ [8/15, 4/5]` (where cap-`a` alone fails) is covered by this 5-cap multi-way argument, NOT by the single `a`-cap.

## Scope

- **`n = 3` only**, and **the `d ≥ 1/2` (dominant) regime only** (the `S_{2d−1}` cap is invalid for `d < 1/2`).
- Does NOT close `U(3)` for the `d < 1/2` regime (handled by the sliver + 17-family; the `d < 1/2` extreme sub-cases `w < −2α` or `z < −2α` are an OPEN GAP — see `approaches/two-regime-disjunctive.md` §5d.4).
- Does NOT generalize to `n ≥ 4` (the cap family grows combinatorially; no inductive lift known).
