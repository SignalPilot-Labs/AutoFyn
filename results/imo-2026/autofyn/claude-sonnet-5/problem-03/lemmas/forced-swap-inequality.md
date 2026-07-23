# Forced Swap Inequality

**Certified by:** proof-reviewer, round 11, from approach `potential-weighting-upper-bound`
(round-11 builder, §16.2). Independently re-derived by the reviewer from scratch (the four-point
non-crossing-repair argument re-traced symbolically, matching exactly) and re-verified
computationally with an independently-written harness (not the builder's `verify_fsi_lemma2.py`):
`1289/1289` fresh crossing-pair checks (`q=3,\dots,7`, background size `0`–`4`, random exact
integers), zero violations — on top of the builder's own `3336/3336` (after the builder's own
self-caught, honestly-documented test-harness bug, fixed before certification was requested).

**Depends on:** only the raw definitions of `e(\cdot)` (alternating sum of a sorted-descending
multiset) and `\mathrm{OPT}_\sigma(B,Z)` (§13.2 of `potential-weighting-upper-bound.md`); does not
depend on the General Rank-Extraction Identity or any conjectural material, and needs **no
restriction on background size** `|B|`.

## Statement

Fix a background multiset `B` (any size) and a sorted list `Z=(z_1\ge z_2\ge\dots\ge z_q)`. For
`2\le l\le q` write `d_l:=z_1-z_l\ge0` and `A_{3,l}:=\mathrm{OPT}_{+1}\big(B\cup\{d_l\},\,
Z\setminus\{z_1,z_l\}\big)`. Let `k^*` achieve `M:=\min_l A_{3,l}` (a **global** argmin over every
`l`). Let `\eta^*` be **any** `(K,D,M)`-selection of `Z\setminus\{z_1,z_{k^*}\}` achieving
`A_{3,k^*}=M`. Suppose `\eta^*` contains a matched pair `(i,j)` with `2\le i<k^*<j\le q` (original
positions in `Z`, so this pair "crosses" the pair `(1,k^*)` since `1<i<k^*<j`). Let
`R:=\big(B\cup\mathrm{vals}(\eta^*)\big)\setminus\{d_{k^*},\,z_i-z_j\}` (well-defined as a
multiset removal, since `\mathrm{vals}(\eta^*)` contains `z_i-z_j` and `B\cup\{d_{k^*}\}` contains
`d_{k^*}`).

```
Forced Swap Inequality.
e(R \cup \{z_1-z_i,\ z_{k^*}-z_j\}) \ge M,      and symmetrically
e(R \cup \{z_1-z_j,\ z_i-z_{k^*}\}) \ge M.
```

(Both differences on the left of each pair are of correctly-ordered, nonnegative quantities,
forced by the position ordering `1<i<k^*<j` and `Z` sorted descending: `z_1\ge z_i` and
`z_{k^*}\ge z_j` for the first inequality; `z_1\ge z_j` and `z_i\ge z_{k^*}` for the second.)

Informally: **any single local re-pairing that reassigns `z_1`'s match partner to "fix" a crossing
with the global argmin's own optimal witness is provably no better than the value the global
argmin already achieves.**

## Proof

A crossing pair of arcs on 4 labeled points in fixed position order `1<i<k^*<j` has exactly two
non-crossing alternative pairings: the **disjoint** pairing `(1,i)\ \&\ (k^*,j)`, and the
**nested** pairing `(1,j)\ \&\ (i,k^*)`.

Take the disjoint alternative. Define a selection `\eta''` of `Z\setminus\{z_1,z_i\}` by copying
`\eta^*`'s own `(K,D,M)` structure verbatim on the common index set
`Z\setminus\{z_1,z_{k^*},z_i,z_j\}` (well-defined: `\eta^*` is a selection of
`Z\setminus\{z_1,z_{k^*}\}`, and removing its own matched pair `(i,j)` leaves exactly this set),
and additionally placing `(k^*,j)` as a matched pair. The domain of `\eta''` is
`\big(Z\setminus\{z_1,z_{k^*},z_i,z_j\}\big)\cup\{k^*,j\} = Z\setminus\{z_1,z_i\}`, so `\eta''` is
a **valid** (not necessarily optimal) selection of `Z\setminus\{z_1,z_i\}`, giving
```
A_{3,i} \le e\big(B\cup\{z_1-z_i\}\cup\mathrm{vals}(\eta'')\big) = e\big(R\cup\{z_1-z_i,\,z_{k^*}-z_j\}\big).
```
Since `k^*` is a **global** argmin over *all* `l` (not a locally-chosen one), `M=A_{3,k^*}\le
A_{3,i}`. Chaining, `M\le A_{3,i}\le e(R\cup\{z_1-z_i,z_{k^*}-z_j\})`, proving the first
inequality. The second is identical, using the nested re-pairing `(1,j)\ \&\ (i,k^*)` and
`A_{3,j}` in place of `A_{3,i}`. `\blacksquare`

## Verification

Independently re-verified by the reviewer with a **fresh, independently-written** exact-integer
harness (`mydefs.py` + `verify_fsi_fresh.py`, written from the prose statement only, not by
reading the builder's code): for every optimal witness of every argmin branch found in `4000`
random trials (`q=3,\dots,7`, background size `0`–`4`, integer entries `0,\dots,10`), every
crossing pair `(i,j)` inside it was extracted and both swap alternatives computed directly —
`1289` crossing-pair instances checked, `0` violations of either inequality, and the "sanity"
identity `e(R\cup\{d_{k^*},z_i-z_j\})=M` (confirming `R` was constructed correctly) held in every
case. This matches, via an independent implementation, the builder's own `3336/3336`
(`verify_fsi_lemma2.py`, arbitrary background size `0`–`4`, `q=3,\dots,7`).

**One documentation note, not a soundness issue:** while re-deriving the file's own illustrative
averaging example (§16.3.1: `B=[1],Z=(9,8,8,8,5,3,0)`, claimed "`M=0`, both alternatives `=1`"),
the reviewer's independent recomputation of the specific crossing pairs available at that
instance's argmin branches (`k^*\in\{2,3\}`, both value `8`) instead gives alternative values
`\{0,2\}` (never `\{1,1\}`) — the Forced Swap Inequality itself (`\ge M=0`) still holds in every
one of these cases (`0\ge0` and `2\ge0`), and the broader negative claim of §16.3.1 (averaging the
two alternatives does not reliably recover `M`) was independently re-confirmed by the reviewer via
a properly-rescoped fresh test (restricted to the actual SAR argmin branch and `|B|\le1`,
matching the conjecture's own scope): `0` non-trivial successes (i.e. average `\le M` with not
both alternatives already equal to `M`) out of `5776` argmin-branch crossing instances. Only the
one specific illustrative numeric example in the current file text appears to be a mislabeled
transcription, not a defect in the (independently reproduced) lemma or the (independently
reproduced) negative result it illustrates. Recommended fix for a future round: replace or correct
that one worked example in §16.3.1.

## Reusable by

Any approach that considers repairing a crossing pair in an optimal witness by a **single local
re-pairing** of the four endpoints involved: this lemma shows both non-crossing local repairs are
individually no better than the global optimum already established at the argmin — ruling out an
entire class of "local swap/repair" proof techniques for recovery-type claims (already used this
round, §16.3.1, to rule out *averaging* the two repairs as a recovery mechanism). Needs no
restriction on background size, so it is available at every recursion depth of the
`potential-weighting-upper-bound` approach's own background-carrying family, not just at
`|B|\le1`.
