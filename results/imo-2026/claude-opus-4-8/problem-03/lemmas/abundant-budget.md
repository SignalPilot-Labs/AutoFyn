# Lemma AB (abundant budget): μ(X,b)=0 when b ≥ |X|

**Status:** CERTIFIED (proof-reviewer, round 9). Proposed by `geometric-selfsimilar`. Reviewer
re-derived the constructive strategy from scratch and confirmed the cut-count invariant and A=0 outcome
(0 failures / 5000 random rational multisets via the "pair-two, halve-last" instance).

## Statement
For every finite multiset `X` of positive lengths and every integer budget `b ≥ |X|`, `μ(X,b) = 0`,
where `μ(X,b) = min` over placements of `≤ b` interior cut points of `A(result)` and
`A(P) = measure{x ≥ 0 : N_P(x) odd}` (depends only on the multiset of part lengths).

## Proof
Let `k = |X|`. Xiang Yu runs the **pairing reduction**. While `≥ 2` pieces remain, take two pieces
`a ≥ b'`:
- if `a = b'` they already form an equal pair — delete both, **no cut** (parity-invisible: adding/removing
  `{w,w}` changes `N` by an even amount everywhere, so `A` is unchanged);
- if `a > b'`, cut `a` at interior offset `b'` (legal, `0 < b' < a`) into `(b', a−b')`; the fresh `b'`
  with the existing `b'` is an invisible pair, leaving the new piece `a−b' > 0`. **One cut**, count down 1.

Each step strictly lowers the piece count, so after `≤ k−1` cuts `≤ 1` piece remains. If `0` pieces
remain, `N ≡ 0` and `A = 0`. If a single piece `{w}` remains, `≤ k−1 ≤ b−1` cuts were used, so `≥ 1` cut
remains: cut `w` at its midpoint into `(w/2, w/2)` — an invisible pair — giving `A = 0`. In all cases the
number of cuts is `≤ k ≤ b`, all cut points are strictly interior to distinct current pieces (distinct
stick positions, disjoint from LB's boundary marks), so the placement is legal and `A = 0`. Since
`A ≥ 0` always, `μ(X,b) = 0`. ∎

## Scope / corollary
Under the sum-bound budget invariant `|X| ≤ b+1`, the residual `m ≥ 4` gap case is nontrivial ONLY at the
**tight budget `b = m−1`** (all `b ≥ m` give `μ = 0 ≤ Σ/D_b`). This is a genuine narrowing of the R8
frontier. The tight case `b = m−1` reduces to a finite merge-family inequality (T), which is
**verified (0/9646 exact m=4 gap configs) but NOT analytically proven** — the open residual of the upper
bound. Do not cite (T) as established.
