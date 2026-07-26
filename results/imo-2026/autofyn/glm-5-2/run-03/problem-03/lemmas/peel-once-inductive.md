# Lemma: peel-once + (n−1)-bound (inductive upper-bound handle)

## Status
PROVED (conditional on the (n−1)-mark upper bound; inductive, base n=2 certified). Certified round 4 by proof-reviewer (verified arithmetic for n=2..7, exact at threshold).

## Statement

> **Lemma 5 (peel-once + (n−1)-bound).** For `n ≥ 2`, let Liu Bang's pieces be `p_1 ≥ p_2 ≥ … ≥ p_{n+1}` summing to 1. If for some `j ∈ {2, …, n+1}` we have
> `p_j ≥ g_{n−1} := 2^{n−1}/D_n`,  where `D_n := 2^{n+1} − 1`,
> then Xiang Yu peels `p_1 → p_j + (p_1 − p_j)` (1 mark; the peeling lemma `lemmas/peeling.md` makes the pair `(p_j, p_j)` parity-neutral, so `D_final = D_rest` exactly on the n-piece rest) and applies the (n−1)-mark upper bound to the n-piece rest (total `T = 1 − 2 p_j`), achieving
> `D ≤ T / D_{n−1} = (1 − 2 p_j)/D_{n−1} ≤ 1/D_n`.
>
> Equivalently: the regime "some `p_j ≥ g_{n−1}`" is closed at every `n` (conditional on the (n−1)-mark upper bound being established for all n-piece configs).

## Proof

**Peeling step.** By the peeling lemma (`lemmas/peeling.md`, CERTIFIED), splitting `p_1` into `p_j + (p_1 − p_j)` where `p_j` is an existing piece creates two copies of `p_j` that contribute `+2 · 1_{[0, p_j)}` to `j(t)` — even, hence parity-neutral. Removing the pair leaves `D_final = D_rest` exactly, where `rest = {p_1 − p_j} ∪ {p_k : k ≠ 1, j}` is an n-piece multiset with total `T = 1 − 2 p_j`.

**(n−1)-bound application.** The rest is an arbitrary n-piece config (derived, but the (n−1)-mark upper bound — once established for ALL n-piece configs — applies config-independently). Rescaling the (n−1) bound `D ≤ 1/D_{n−1}` (for total 1) to total `T` gives `D_rest ≤ T/D_{n−1}` (the alternating sum `D` scales linearly with the total mass).

**Arithmetic.** `T/D_{n−1} = (1 − 2 p_j)/D_{n−1} ≤ 1/D_n ⟺ D_n (1 − 2 p_j) ≤ D_{n−1} ⟺ (2 D_{n−1} + 1)(1 − 2 p_j) ≤ D_{n−1} ⟺ D_{n−1} + 1 ≤ 2 p_j D_n ⟺ p_j ≥ (D_{n−1} + 1)/(2 D_n) = 2^n/(2 D_n) = 2^{n−1}/D_n = g_{n−1}`.

The hypothesis `p_j ≥ g_{n−1}` is exactly this threshold. So `D ≤ 1/D_n`. ∎

**Verification.** Arithmetic identity `(1 − 2 g_{n−1})/D_{n−1} = 1/D_n` verified for n = 2..7 by exact rational computation (Python `fractions`): at `p_j = g_{n−1}` both sides equal `1/D_n`; for `p_j = g_{n−1} + 1/1000` the LHS is strictly below `1/D_n`; for `p_j = g_{n−1} − 1/1000` strictly above. The peel-then-menu construction on n=3 flat configs (40k+ random, `p_4 > 1/15`) gives 0 failures with `best D ≤ 1/15` throughout (tight at dyadic `(8/15, 4/15, 2/15, 1/15)`, where peeling `p_1 → p_2` gives rest `(4/15, 2/15, 1/15)` and the n=2 menu min `= 1/15`).

## Scope and limitations

- **Closes** the regime "some `p_j ≥ g_{n−1}`" for every `n ≥ 2` (conditional on the (n−1)-mark upper bound, inductive; base n=2 certified via `pairing-charging` §6.3 / `minimax-strategy-family` §3).
- For n=3 this gives the threshold `g_2 = 4/15`: the two sub-cases `p_2 ≥ 4/15` (peel `p_1 → p_2`) and `p_3 ≥ 4/15` (peel `p_1 → p_3`) are PROVED, reducing `D ≤ (1 − 8/15)/7 = 1/15`.
- **Does NOT close** the "very-flat" residual: all `p_j < g_{n−1}` (every piece below the threshold). For n=3 this is Case C (`p_2, p_3 < 4/15`); the construction (peel + full n=2 menu) is verified (0 failures / 30k) but its 12-expression sort-regime casework is an open gap.
- For n ≥ 4 the very-flat residual is open and unverified.

## Import notes

- Importable by any approach needing the upper bound in the "spiky-ish" regime (`p_j ≥ g_{n−1}`) at general n. Combined with `lemmas/equal-halve-n-largest.md` (closes `p_{n+1} ≤ 1/D_n`), this covers the non-flat half of the upper bound.
- The very-flat residual (all `p_j < g_{n−1}`) is the generalized crux of G2-flat; it requires the actual menu values of the (n−1)-bound, not the loose `T/D_{n−1}` bound.
