# Lemma: Shrink-List Monotonicity

**Status:** CERTIFIED (round 14, proposed by `potential-weighting-upper-bound`, independently
re-verified from scratch by the round-14 proof-reviewer — own fresh `Fraction`-exact harness,
`800/800` trials both signs, plus an independent reproduction of the file's own worked example
`C=\{5,8\},W=(10,8,7,2)`: `OPT_{+1}=0`, matching exactly). Fully proved, no `\mathcal
F`-provenance restriction needed.

## Statement

Let `OPT_\sigma(C,W)` denote (per `potential-weighting-upper-bound.md` §13.2, the Generalized
Multi-Background Peeling Lemma's own setup) the `\sigma`-optimal (minimum if `\sigma=+1`, maximum if
`\sigma=-1`) value of `e(C\cup K\text{-values}\cup M\text{-differences})` over **all** selections
`(K,D,M)` of a list `W` (Keep/Delete/Match, no crossing restriction), for a fixed external background
multiset `C`. (Deleted elements of `W` contribute nothing to the multiset fed to `e`; this is the
standing convention used throughout the `\mathrm{OPT}_\sigma` recursion, e.g. already relied on by the
certified Extreme-Element Peeling Lemma and the Generalized Multi-Background Peeling Lemma.)

For **any** background `C`, **any** list `W`, and **any** `x\in W`:
```
OPT_{+1}(C,W) \le OPT_{+1}(C, W\setminus\{x\})          (and, mirrored, OPT_{-1}(C,W) \ge OPT_{-1}(C,W\setminus\{x\}))
```

No hypothesis on `C`, `W`, or `x` is needed — this holds for an arbitrary background multiset and an
arbitrary list, not only for instances arising from the problem's own recursive family
`\mathcal F`.

## Proof

Fix `C`, `W`, `x\in W`, and let `\eta` be any selection `(K,D,M)` of `W\setminus\{x\}` achieving the
value `OPT_{+1}(C,W\setminus\{x\})` (such a selection exists since `W\setminus\{x\}` is finite, so
the minimum over its finitely many selections is attained).

Extend `\eta` to a selection `\eta'` of the bigger list `W` by additionally placing `x` into the
Delete set (i.e. `\eta'=(K,D\cup\{x\},M)`, the same Keep set and the same set of matched pairs as
`\eta`, with `x` newly deleted). Since a deleted element contributes nothing to the multiset fed to
`e` (the standing convention stated above), the multiset produced by `\eta'` is *identical* to the
multiset produced by `\eta`: both equal `C\cup K\text{-values}\cup M\text{-differences}`, with `x`
appearing in neither. Hence
```
e(\text{multiset of }\eta') = e(\text{multiset of }\eta) = OPT_{+1}(C,W\setminus\{x\}).
```
`\eta'` is one particular selection of `W` (not necessarily an optimal one) — it lies in the search
space that `OPT_{+1}(C,W)` minimizes over. Since `OPT_{+1}(C,W)` is the *minimum* over that whole
search space, and `\eta'` is one member of it with value `OPT_{+1}(C,W\setminus\{x\})`,
```
OPT_{+1}(C,W) \le e(\text{multiset of }\eta') = OPT_{+1}(C,W\setminus\{x\}).
```
This proves the `\sigma=+1` case.

For `\sigma=-1`, the identical construction applies verbatim (extend a `\sigma=-1`-optimal selection
`\eta$ of `W\setminus\{x\}` by additionally deleting `x`, giving an element of `W`'s search space with
the same value), but now `OPT_{-1}(C,W)` is a **maximum** over its search space, so this particular
member gives a **lower** bound instead: `OPT_{-1}(C,W) \ge OPT_{-1}(C,W\setminus\{x\})`. `\blacksquare`

## Remarks

- The proof is a one-line bijection/embedding argument: it only uses (a) the "delete contributes 0"
  convention, and (b) that a `\sigma`-optimum over a superset of a search space is at least as good
  (for the appropriate direction) as the value achieved on any particular subset-derived candidate.
  No structural property of `C`, `W`, or `x` is used anywhere.
- **Corollary (repeated application).** For any background `C` and any finite list `W`, iterating the
  lemma once per element of `W` (removing one element at a time, in any order, down to the empty
  list) gives
  ```
  OPT_{+1}(C,W) \le OPT_{+1}(C,\emptyset) = e(C)          (mirror: OPT_{-1}(C,W)\ge e(C)).
  ```
  This is the "free" (`\le D` for `\sigma=+1`) direction used throughout the population's work on
  Gap 1a (`potential-weighting-upper-bound.md` §21.1, the Deletion-Suffices-for-`k^*` sub-lemma):
  applying it with `C=\{b_0,d_{k^*}\}`, `W=Z_1$ immediately gives `M=A_{3,k^*}=OPT_{+1}(\{b_0,d_{k^*}\},
  Z_1)\le e(\{b_0,d_{k^*}\})=|b_0-d_{k^*}|=D`, i.e. `M\le D` unconditionally, with no trigger or
  argmin hypothesis needed — isolating the *entire* remaining content of Deletion-Suffices to the
  reverse inequality `M\ge D`.

## Verification

Independently stress-tested by two different agents (round-14 `math-explorer`, round-14
`outline-reviewer`) via fresh, independently-written exact-`Fraction` code on fully arbitrary
`(C,W,x)` triples (no `\mathcal F`-restriction): `0` violations across `14{,}160+` (explorer) and
`3{,}000` (outline-reviewer, fresh independent harness) trials, both signs `\sigma=\pm1`. The
numerical checks corroborate but are not needed to trust the proof, which is a direct, fully general
argument with no case analysis.

## Used by

- `potential-weighting-upper-bound.md` §21.1/§21.3/§22 (the "free" direction of Deletion-Suffices,
  and as the certified half of the retargeted "half-step" decomposition for Gap 1c — only the
  companion background-growing direction, `OPT_{+1}(C\cup\{d\},X)\ge OPT_{+1}(C,X)`, remains open
  there, and is a logically *different*, `\mathcal F`-specific claim, NOT an instance of this lemma).
