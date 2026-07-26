# Lemma U(2) — four-strategy upper bound, equality iff dyadic

**Status: CERTIFIED** (reviewer, round 2). Rigorous; four formulas and the
contradiction argument verified by exact rational arithmetic (python) and
re-derived independently. Minor Strategy-A edge case at `c = b` is covered by
the other three strategies (the contradiction argument only imposes MORE
conditions, so a degenerate strategy cannot create a false "all four > 4/7").

**Statement.** For every `n = 2` Liu config — three pieces `(a, b, c)` with
`a ≤ b ≤ c`, `a + b + c = 1` — Xiang with `2` marks has a strategy forcing
`Liu ≤ 4/7 = f(2)`, with **strict** inequality for every non-dyadic config and
equality (cap `= 4/7`) iff `(a, b, c) = (1/7, 2/7, 4/7)` (the order-2 dyadic).

**Strategy family.** Four explicit Xiang strategies; the value quoted for the
sliver strategies is the **infimum** as the sliver `s → 0+` (the actual value
approaches this infimum from above, so for non-dyadic configs where the
infimum is `< 4/7`, Xiang picks `s` small enough to achieve `Liu < 4/7`
strictly). Strategy A is exact for `c > b` (the two sub-pieces `(c−b)/2` are
positive); at the boundary `c = b` it degenerates, but the bound is then
carried by Strategy C (`Liu_C → 1/2 < 4/7`).

- **Strategy A** (match 2nd-largest inside the largest): split `c` into
  `(b, (c−b)/2, (c−b)/2)`. Final multiset `{a, b, b, (c−b)/2, (c−b)/2}`; the
  two equal pairs each contribute `0` to the advantage, leaving `A = a`.
  `Liu_A = (1 + a)/2`.
- **Strategy B** (bisect largest, then a sliver): bisect `c → (c/2, c/2)`, then
  cut a sliver `s → 0+` from one half. Limit multiset `{a, b, c/2, c/2, 0}`;
  the equal pair `c/2, c/2` cancels. `Liu_B (inf) = (1 + b − a)/2`.
- **Strategy C** (split the smallest into halves plus a sliver): split `a` into
  `(s, a/2, a/2 − s)`. Limit multiset `{a/2, a/2, b, c, 0}`; the equal pair
  `a/2, a/2` cancels. `Liu_C (inf) = (1 + c − b)/2`.
- **Strategy E** (match 2nd-largest in largest + sliver from smallest): split
  `c → (b, c − b)`, cut a sliver `s → 0+` from `a`. Limit multiset
  `{b, b, c − b, a, 0}`; the equal pair `b, b` cancels.
  `Liu_E (inf) = (1 + |2c − 1|)/2 = max(c, 1 − c)`.

**Claim.** `min(Liu_A, Liu_B, Liu_C, Liu_E) ≤ 4/7`, equality iff the dyadic.

**Proof (4-way contradiction).** Translate each bound to a condition on
`(a, b, c)` with `a + b + c = 1`, `a ≤ b ≤ c`:
- `Liu_A ≤ 4/7` ⟺ `a ≤ 1/7`.
- `Liu_B ≤ 4/7` ⟺ `b − a ≤ 1/7`.
- `Liu_C ≤ 4/7` ⟺ `c − b ≤ 1/7`.
- `Liu_E ≤ 4/7` ⟺ `3/7 ≤ c ≤ 4/7`.

Suppose all four bounds are `> 4/7`. Then `a > 1/7`, `b − a > 1/7`,
`c − b > 1/7`, and (`c < 3/7` or `c > 4/7`). From the first three:
`c > b + 1/7 > a + 2/7 > 3/7`, so `c > 3/7`, forcing `c > 4/7`. Then
`a + b = 1 − c < 3/7`. But `b > a + 1/7 > 2/7`, so
`a + b > 2a + 1/7 > 3/7` — contradiction. So `min ≤ 4/7`.

Equality analysis: replace `>` with `≥`. From `a ≥ 1/7`, `b − a ≥ 1/7`,
`c − b ≥ 1/7` get `c ≥ 3/7`. If `c ≤ 3/7` then `c = 3/7` and all intermediate
inequalities are equalities: `a = 1/7, b = 2/7, c = 3/7`, but
`a + b + c = 6/7 ≠ 1` — contradiction. So `c ≥ 4/7`, giving
`a + b ≤ 3/7`; combined with `a + b ≥ 2a + 1/7 ≥ 3/7`, equality throughout:
`a = 1/7, b = 2/7, c = 4/7`. ∎

**Verification.** Exact rational arithmetic: (a) all four strategy formulas
reproduce the directly-computed advantage `A` of the constructed final
multiset for several configs; (b) on a grid `N = 84` over all `(a, b, c)` with
`a ≤ b ≤ c`, `a + b + c = 1`, **0 violations** of `min ≤ 4/7`, and the unique
config with `min = 4/7` is exactly `(1/7, 2/7, 4/7)` — the dyadic. The dyadic
is capped exactly by Strategy A (and by the certified pair-pile); every
non-dyadic config has `min < 4/7` strictly.

**Knowledge-base tools.** Casework / exhaustion (the 4-way contradiction);
Invariants & monovariants (the advantage `A` and the equal-pair cancellation);
Constructive / incremental (explicit mark placements).

**Where proved.** `approaches/two-regime-disjunctive.md`, Section 4 (round 2).
Reviewer-certified round 2 (python verification in `/tmp/verify_round2.py`).
