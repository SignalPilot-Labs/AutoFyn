**Status: CERTIFIED** (reviewer, round 2). The three-case rank analysis is
rigorous; Case 2's identity `oddsum({w} ∪ R') = w + oddsum(R') − A_tail` and
the bound `w ≤ evensum(R') + A_tail ≥ s_2 ≥ w` re-derived and verified. Case 3
correctly invokes Lemma `L(n)`. Verified: min gap `0` for `n = 1, 2, 3` (exact
enumeration on the `D(n)` grid, all refinements `R'` by `≤ n` marks, all
integer `w ∈ [0, R_largest]`), equality at the self-similar extremal
(`R'` = pair-pile, `w = R_largest`). Correctly stated as a *corollary* of
`L(n)` at the same level (only Case 3 uses `L(n)`). Importable.

# Lemma L* — single-auxiliary strengthened dual of Lemma L

**Statement.** Let `R` be the level-`n` dyadic config (pieces
`(1, 2, 4, …, 2^n)/D(n)`, `D(n) = 2^{n+1} − 1`, total `1`, largest piece
`R_largest = 2^n/D(n) = f(n)`). Let `R'` be any refinement of `R` obtained by
placing **at most `n`** Xiang marks (so `R'` has at most `2n + 1` pieces, total
`1`). Let `w` be a single auxiliary piece with `0 ≤ w ≤ R_largest`. Then the
merged multiset `{w} ∪ R'` satisfies

> **`evensum({w} ∪ R') ≥ w`**, equivalently **`oddsum({w} ∪ R') ≤ total(R') = 1`**.

**Corollary (the lemma's purpose).** `L*(n)` is the strengthened induction
hypothesis used to close the `k = 1` sub-case of Lemma `L(n+1)` (Liu's lower bound
on the level-`(n+1)` dyadic config): one Xiang mark inside the largest piece
`M = 2^{n+1}/D(n+1)` splits it as `M → (m_1, m_2)`, `m_1 ≥ m_2`; since
`m_1 ≥ M/2 = 2^n/D(n+1) = R_largest` (of the scaled level-`n` rest), `m_1` is the
global rank-`1` piece (Liu's), and `global_oddsum = m_1 + evensum({m_2} ∪ R') ≥
m_1 + m_2 = M = f(n+1)` by `L*(n)` applied to the scaled rest `R` with
auxiliary `w = m_2 ≤ M/2 = R_largest`. (Scaling: rescale `R` to total `1`; the
auxiliary rescales to `w·D(n+1)/D(n) ≤ 2^n/D(n) = R_largest`.) So `L*(n)` is
the engine that makes the `k = 1` sub-case a clean one-step reduction.

**Proof.** Sort `{w} ∪ R'` descending; write the sorted list as
`q_1 ≥ q_2 ≥ … ≥ q_{m+1}` where `m = |R'| ≥ 2` (since `n ≥ 1` implies `R` has
`≥ 2` pieces and refining only adds pieces). Let `r` be the rank at which `w`
sits (ties broken arbitrarily in `w`'s favor; the argument is independent of the
tie-break because we use only inequalities valid for every consistent
placement). Denote `R'`'s own sorted list by `s_1 ≥ s_2 ≥ … ≥ s_m`.

We split on the parity of `r`.

*Case 1: `r` is even.* Then `w` is one of the even-rank pieces of the merged
multiset, so `evensum({w} ∪ R') ≥ w` directly. ✓

*Case 2: `r` is odd, `r ≥ 3`.* Then `w` lies strictly below the top two `R'`
pieces in the merged order, i.e. `s_1 ≥ s_2 ≥ … ≥ s_{r−1} ≥ w ≥ s_r ≥ …`, so in
particular **`w ≤ s_{r−1} ≤ s_2`** (using `r − 1 ≥ 2`). We claim
`oddsum({w} ∪ R') ≤ 1`. Compute: the merged odd-rank pieces consist of `w`
itself, plus the `R'` pieces at merged odd ranks `≠ r`. Merged ranks below `r`
are unchanged by the insertion of `w`, so merged odd ranks `1, 3, …, r − 2`
contribute `s_1, s_3, …, s_{r−2}` (the `R'` odd ranks below `r`). Merged ranks
above `r` are shifted down by one (because `w` occupies rank `r`), flipping their
parity; merged odd ranks `r + 2, r + 4, …` thus correspond to `R'` even ranks
`r + 1, r + 3, …`, contributing `s_{r+1}, s_{r+3}, …`. Therefore

```
oddsum({w} ∪ R') = w + (s_1 + s_3 + … + s_{r−2}) + (s_{r+1} + s_{r+3} + …).
```

Let `A_tail = (s_r − s_{r+1}) + (s_{r+2} − s_{r+3}) + …` be the alternating sum
of `R'`'s tail from rank `r` onward (each bracketed term is `≥ 0` by the sorted
order, so `A_tail ≥ 0`). A short rearrangement gives

```
oddsum({w} ∪ R') = w + oddsum(R') − A_tail.
```

We want `≤ 1 = oddsum(R') + evensum(R')`, i.e. `w − A_tail ≤ evensum(R')`. Now
`evensum(R') = s_2 + s_4 + … ≥ s_2` (all terms non-negative, `s_2` among them),
and `A_tail ≥ 0`, so `evensum(R') + A_tail ≥ s_2 ≥ w`. Hence
`oddsum({w} ∪ R') ≤ 1`, equivalently `evensum({w} ∪ R') ≥ w`. ✓
(No induction hypothesis is used in this case — the bound is purely from sorted
order.)

*Case 3: `r = 1` (`w` is the largest piece of the merged multiset).* Then
`w ≥ s_1 = R'_largest`, and the hypothesis gives `w ≤ R_largest`. The merged
odd-rank pieces are `w` (rank `1`) plus the `R'` pieces at merged odd ranks
`3, 5, 7, …`, which (by the rank-`+1` shift) are the `R'` even ranks
`2, 4, 6, …`. Thus

```
oddsum({w} ∪ R') = w + evensum(R') = w + 1 − oddsum(R').
```

We want `≤ 1`, i.e. `w ≤ oddsum(R')`. By **Lemma `L(n)`** (the level-`n` lower
bound on `R'`: `oddsum(R') ≥ f(n) = 2^n/D(n) = R_largest`), and
`w ≤ R_largest`, we get `w ≤ R_largest ≤ oddsum(R')`. ✓

Combining the three cases, `evensum({w} ∪ R') ≥ w` holds in every position of
`w` in the merged sort. ∎

**Remark (induction structure).** Lemma `L*(n)` is a *corollary of* Lemma `L(n)`
at the same level `n` — only Case 3 (`r = 1`) uses `L(n)`, and only through
`oddsum(R') ≥ R_largest ≥ w`. This gives the clean induction chain
`L(n) ⟹ L*(n) ⟹ L(n+1)[k ≤ 1]`, where the `k = 0` sub-case of `L(n+1)` is
trivial (`M ⊎ R` decomposition) and the `k = 1` sub-case is the one-step
reduction of the corollary above. The `k ≥ 2` sub-case of `L(n+1)` is a
separate, genuinely harder obstruction (multi-aux `L*` is FALSE — see the
explorer's counterexample `W = (1/9, 4/9, 1/9)` over `D = 9`); it is not closed
by this lemma and remains the open gap of the lower-bound route.

**Verification.**

- Exact enumeration (denominator `D(n)`, all refinements `R'` of the level-`n`
  dyadic by `≤ n` Xiang marks, all integer `w` in `[0, R_largest]`):
  `n = 1, 2, 3` — minimum gap `evensum({w} ∪ R') − w` is **`0`** in each case,
  attained at the self-similar extremal `R' = pair-pile of level n`,
  `w = R_largest = 2^n/D(n)`.
- Monte-Carlo (30 000 random `(R', w)` trials) at `n = 4`: minimum gap `0`,
  no negative gap observed.
- Self-similar extremal equality check (`R'` = pair-pile, `w = R_largest`):
  `n = 2, 3, 4, 5` — gap `0` in every case (rational arithmetic).

**Knowledge-base tools.** **Induction** (Pólya "Generalize: a stronger
statement is sometimes easier to prove by induction" — `L*(n)` is the
Xiang-side dual loaded alongside `L(n)`, cf. Lemma G's both-move-orders
pattern); **Invariants & monovariants** (the alternating sum `A` and its
tail-shift `A_tail`); **Casework / exhaustion** (the three position cases for
`w` in the merged sort).

**Where proved.** `approaches/pairing-partner.md`, "Lemma L* — single-auxiliary
strengthened dual" (round 2).
