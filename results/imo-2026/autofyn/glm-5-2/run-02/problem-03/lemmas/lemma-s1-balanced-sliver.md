# Lemma S1: Balanced-config sliver forcing (all n ≥ 1, reals)

**Status:** CERTIFIED (round 4, proof-reviewer). Proved in `approaches/two-regime-disjunctive.md` §5c.3. Reviewer re-derived the sign-sum `A = 2s` for `n = 1..7` with exact-rational python (matches `2s` to equality in every case, `A < α(n)` verified).

## Statement

Let Liu play the **balanced config** of `n + 1` equal pieces `(w, w, …, w)`, `w = 1/(n+1)`. Then Xiang with at most `n` marks has an explicit strategy forcing

`A(final) ≤ 2s`   for every `s ∈ (0, w/2)`,

hence `inf_Xiang A = 0 < α(n) = 1/D(n)`. The balanced config is therefore regime-`N` (strict `A < α(n)`) for every `n ≥ 1`.

## Strategy (explicit, real-valued)

Two cases by the parity of `n`:

- **`n` odd.** Xiang uses all `n` marks, each cutting a sliver of size `s` from a distinct one of `n` "non-leftover" pieces (one piece left untouched). Each cut piece `w` becomes `(w − s, s)`. Final multiset: `1` piece `w`, `n` pieces `w − s`, `n` pieces `s` (total `2n + 1` pieces). For `s < w/2`: `w > w − s > s`, sorted desc: `w`, then `n` copies of `w − s` (ranks `2, …, n+1`), then `n` copies of `s` (ranks `n+2, …, 2n+1`).

- **`n` even.** Xiang uses `1` mark to bisect one piece `w → (w/2, w/2)`, and `n − 1` marks each cutting a sliver `s` from a distinct one of the remaining `n − 1` non-bisected non-leftover pieces (one piece left untouched). Final multiset: `1` piece `w`, `n − 1` pieces `w − s`, `2` pieces `w/2`, `n − 1` pieces `s` (total `2n + 1` pieces). For `s < w/2`: `w > w − s > w/2 > s`, sorted desc: `w`, then `n − 1` copies of `w − s` (ranks `2, …, n`), then `2` copies of `w/2` (ranks `n+1, n+2` — consecutive, cancelling), then `n − 1` copies of `s` (ranks `n+3, …, 2n+1`).

## Computation of `A`

Let `T_1` = sign-sum over the `w − s` block, `T_2` = sign-sum over the `s` block. (The `w/2` block in the `n`-even case contributes `0` — its two equal members sit at consecutive ranks of opposite sign.)

- *`n` odd:* the `w − s` block has `n` (odd) members starting at sign `−` (rank `2`); `T_1 = −1`. The `s` block has `n` (odd) members, first at rank `n + 2` with sign `(−1)^{n+3} = +1` (since `n` odd ⟹ `n+3` even); `T_2 = +1`. Hence `A = w·(+1) + (w−s)·(−1) + s·(+1) = w − (w−s) + s = 2s`.
- *`n` even:* the `w − s` block has `n − 1` (odd) members starting at sign `−`; `T_1 = −1`. The `s` block has `n − 1` (odd) members, first at rank `n + 3` with sign `(−1)^{n+4} = +1` (since `n` even ⟹ `n+4` even); `T_2 = +1`. Hence `A = w·(+1) + (w−s)·(−1) + 0 + s·(+1) = 2s`.

In both cases `A = 2s`. Choosing `s < α(n)/2` gives `A < α(n)` strictly; `s → 0^+` gives `inf A = 0`. Since `A ≥ 0` always (sorted-desc alt-sum = non-negative pair-excesses + non-negative leftover), `Φ(balanced) = 0` exactly (attained in the limit). ∎

## Verification (reviewer, exact rational)

`A = 2s` confirmed for `n = 1, 2, 3, 4, 5, 6, 7` with `w = 1/(n+1)`, `s = 1/1000`; each matches `2s` to exact rational equality, and `2s < α(n)` in every case.

## Reusability

A clean, real-valued (not grid-only) regime-`N` result for a structural class (balanced configs). Admissible as one case of a disjunctive regime-`N` cover. The sliver-cut + bisect-one trick (for `n` even) is a reusable technique for forcing `A → 0` on symmetric configs.

## Scope

- Balanced configs only (`(w, w, …, w)`); NOT a universal regime-`N` proof.
- The config is non-dyadic for `n ≥ 2` (for `n = 1` the balanced `(1/2, 1/2)` is covered by `U(1)` Mode `S`).
- Two further structural classes (two-dyadic `n = 3` `(1/2, 1/4, 1/8, 1/8)` → `A = 0` with 2 marks; extreme-dominant `n = 3` `(L, t, t, t)` `L > 4/5` → `A = (1−L)/3 < α(3)`) are proved in the approach file but are too `n = 3`-specific for the shared cache (recorded in `approaches/two-regime-disjunctive.md` §5c.4).
- The universal regime-`N` cover for `n ≥ 3` (arbitrary non-dyadic configs) remains OPEN.
