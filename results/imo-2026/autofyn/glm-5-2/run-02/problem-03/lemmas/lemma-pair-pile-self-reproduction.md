# Lemma: Self-reproduction of the pair-pile (recursive invariant, all n ≥ 2)

**Status:** CERTIFIED (round 6, reviewer APPROVE). Proved in `approaches/self-reproducing-invariant.md` §1.3. Reviewer (round 6) confirmed the recursion matches the certified pair-pile construction.

## Statement

For every `n ≥ 2`, the pair-pile on level `n+1` is the disjoint union of (i) the bisected dominant piece `M = 2^{n+1}/D(n+1)` → equal pair `(2^n, 2^n)` (excess `0`), and (ii) the pair-pile on the level-`n` sub-config `R = (2^n, 2^{n−1}, …, 1)/D(n+1)` (the bottom `n` pieces of the level-`(n+1)` dyadic). The integer pieces of the pair-pile(n) appear **verbatim** in `D(n+1)` units, and the advantage satisfies

```
A_{n+1} = 0 + 1 = 1 = α(n+1)·D(n+1).
```

So the pair-pile is a **self-reproducing invariant** on the pair-excess vector: the invariant at level `n+1` contains the invariant at level `n` as a sub-structure; the dominant piece is absorbed into a zero-excess pair, and the level-`n` invariant re-establishes verbatim on `R`.

## Proof

The level-`(n+1)` dyadic is `P_{n+1}^* = (2^{n+1}, 2^n, …, 1)/D(n+1)`. The dominant piece `M = 2^{n+1}` is bisected (pair-pile mark 1) into `(2^n, 2^n)` (excess `0`). The remaining `n` pieces `R = (2^n, …, 1)` (in `D(n+1)` units) are the same integers as the level-`n` dyadic in `D(n)` units; the pair-pile marks on `R` (marks 2..n) produce the pair-pile(n) multiset `(2^{n−1}, 2^{n−1}, …, 4, 4, 3, 2, 1, 1)` in `D(n+1)` units. Full multiset `{2^n, 2^n} ∪ pair-pile(n)`, sum `2·2^n + D(n) = 2^{n+1} + (2^{n+1}−1) = D(n+1)`. ✓ Advantage: the `(2^n, 2^n)` pair contributes `0`; pair-pile(n) contributes `1` (the `(3, 2)` excess). So `A = 1`. ∎

(Verified exact-rational for n=2..5: piece multiset match, A match, sum match — `self-reproducing-invariant` §1.3, `/tmp/round-6/self_repro_verify.py`.)

## Reusability

The recursive/structural framing of the certified pair-pile (`lemma-pair-pile-dyadic-cap.md`). Establishes the self-reproducing-invariant foundation for any upper-bound approach using the pair-excess vector; pairs with `lemma-ridge-reproduction-all-n.md` (the invariant reproduces under the ridge perturbation) to delimit the equality locus `E_n`.

## Scope

- All `n ≥ 2` (the recursion base n=1 is the trivial pair-pile `(1,1,1)`, `A=1`).
- Establishes the equality `A = α(n+1)` at the dyadic ONLY; does NOT prove `cap ≤ α` for non-dyadic configs. The non-strict upper bound `U(n)` is OPEN for general n (see `two-regime-disjunctive` for n=3, `self-reproducing-invariant` for near-dyadic + E_n).
