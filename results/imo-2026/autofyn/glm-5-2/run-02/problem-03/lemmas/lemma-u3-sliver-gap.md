# Lemma: U(3) — 3-mark sliver strategy (gap G closure, d < 1/2)

**Status:** CERTIFIED (round 5, proof-reviewer). Proved in `approaches/two-regime-disjunctive.md` §5d.3. Reviewer re-derived the chain-excess identity `7u + 4v + 2w + z = α` and the sliver cap `A = u − z = 1 − 2d` with exact-rational python (gap configs, 4 values of `ε` per config; `A == 1 − 2d` exactly, `A < α(3)` in the gap).

## Statement

For an `n = 3` Liu config `(a, b, c, d)`, `a ≤ b ≤ c ≤ d`, `a + b + c + d = 1`, in the **gap region**

```
G := {a > α,  b − a > α,  c − a − b > α,  d − b − c > α,  d < 1/2}
```

(where `α = α(3) = 1/15`), Xiang's 3-mark strategy — split `d → (b, c, e_3)` where `e_3 := d − b − c > 0` [2 marks, creating pairs `(b, b)` and `(c, c)`], plus shave `a → (ε, a − ε)` for any `0 < ε < min(u − z, e_3, a)` [1 mark] — forces

```
A = a − e_3 = 1 − 2d = u − z < α(3) = 1/15  strictly,
```

**independent of `ε`** (robust). Hence `U(3)` holds strictly in `G`.

## Notation (chain excesses)

Define `u := a − α`, `v := (b − a) − α`, `w := (c − a − b) − α`, `z := (d − b − c) − α`. Then
`a = α + u`, `b = 2α + u + v`, `c = 4α + 2u + v + w`, `d = 7α + 3u + 2v + w + z`. The sum constraint `a + b + c + d = 1 = 15α` gives the identity

```
7u + 4v + 2w + z = α.
```

In the gap `G`: `u, v, w, z > 0` and `d < 1/2 ⟺ u > z` (since `1 − 2d = u − z`).

## Proof

The final multiset is `{b, b, c, c, a − ε, e_3, ε}` (7 pieces). The equal pairs `(b, b)`, `(c, c)` each cancel. The three singletons `ε, a − ε, e_3` sort (in `G`) as `a − ε > e_3 > ε`: `a − ε > e_3 ⟺ ε < a − e_3 = u − z > 0` (gap); `e_3 > ε ⟺ ε < e_3 = α + z > 0` (gap). Also `e_3 = α + z ≤ α < 2α + u + v = b ≤ c`, so the full sort is `c, c, b, b, a − ε, e_3, ε`. Hence

```
A = c − c + b − b + (a − ε) − e_3 + ε = a − e_3 = (α + u) − (α + z) = u − z.
```

The `ε`-terms cancel, so the cap is independent of `ε`. Finally, `u − z < α ⟺ α − (u − z) = 6u + 4v + 2w + 2z > 0` (using `7u + 4v + 2w + z = α`), which holds strictly since `u, v, w, z > 0` in `G`. ∎

## Verification

Exact rational arithmetic on 22 gap configs + the constructed example `(a, b, c, d) = (α + 1/200, 2α + 1/200 + 3/1000, …)` reproduces `A = 1 − 2d = u − z` exactly (4 values of `ε` per config). At the boundary `d = 1/2` (config `(1, 2, 4, 7)/14`), `A = 0`. At the dyadic `(1, 2, 4, 8)/15` (which lies in `d ≥ 1/2`), the sliver gives `A = |2d − 1| = 1/15 = α` (equality — consistent, the dyadic is handled by the 5-cap, not the sliver).

## Reusability

Closes the **gap region `G`** of `U(3)` (the unique sub-region of `d < 1/2` where all four chain-excess caps `α + u, α + v, α + w, α + z` exceed `α`, defeating the 17-family exact-pair caps). The strategy generalizes the `S_{2d−1}` cap (gives `|2d − 1|` universally; realizable iff `d ≥ b + c` for `d < 1/2`, always for `d ≥ 1/2`). Combined with `lemma-u3-5cap-dominant.md` (the `d ≥ 1/2` regime) and `L(3)` (CERTIFIED, cell-complex), contributes to the `c(3) = 8/15` upper bound on the gap + dominant regimes.

## Scope

- **`n = 3` only**, and **the gap region `G` only** (the sub-region of `d < 1/2` where ALL four chain-excess caps exceed `α`).
- Does NOT cover the `d < 1/2` non-gap sub-cases where some chain excess is `≤ 0` (those are handled by the 17-family exact-pair caps; the extreme sub-cases `w < −2α` or `z < −2α` are an OPEN GAP — see `approaches/two-regime-disjunctive.md` §5d.4).
- Does NOT generalize to `n ≥ 4`.
