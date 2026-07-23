# Lemmas: Max-Element Triple Identity, and Three-Touch's Base Case (`|W|<=3`)

**Status:** CERTIFIED (round 17, proof-reviewer). Proposed this round (round 17,
`potential-weighting-upper-bound` §28.3), fully proved, elementary, general-purpose. Independently
re-verified by the proof-reviewer with a freshly-written harness (not reusing the builder's code):
Lemma A re-derived by hand in one line; Lemma B's 4-case "keep-all-three" domination argument
re-derived symbolically case-by-case (all algebra checked, boundary consistency confirmed) and
cross-checked against a genuinely exhaustive `c,w1,w2,w3∈{0,…,7}` grid (`4096/4096` matches) plus
`8000` random trials over `|W|∈\{0,1,2,3\}` (`0` mismatches), in addition to reproducing the builder's
own computational corroboration counts (`0/1854`, `0/6000`, `0/956`, `0/3000`, `0/3000`) exactly.

Throughout, `e(S)` denotes the sorted-descending alternating sum of a finite multiset `S` of
nonnegative reals (the standard function from `lemmas/duplicate-pair-invariance.md`).

## Lemma A (Max-Element Triple Identity)

**Statement.** For any nonnegative reals `a,b,c` with `a=\max(a,b,c)`:
```
e(\{a,b,c\}) = a - |b-c|.
```

**Proof.** WLOG `b\ge c` (the statement is symmetric in `b,c`). Since `a\ge b\ge c`, the sorted
descending order is exactly `(a,b,c)`, so `e(\{a,b,c\})=a-b+c`. Also `|b-c|=b-c` (as `b\ge c`), so
`a-|b-c|=a-b+c`, matching `e(\{a,b,c\})` exactly. `\blacksquare`

**Computational corroboration.** `0/1854` violations, exhaustive-style random sweep enforcing
`a\ge b` and `a\ge c` (mixed values `0`–`15`), `/tmp/round-17/verify_builder/verify_keep_identity.py`.

## Lemma B (Three-Touch's Base Case, `|W|<=3`)

Fix `\sigma=-1` (the maximization mirror) and a singleton background `\{c\}`. Define, for a list
`W=(w_1,\dots,w_q)` of nonnegative reals,
```
\mathrm{ThreeTouch}(c,W) := \max\Big(e(\{c\}),\ \max_{w\in W}e(\{c,w\}),\ \max_{i<j}e(\{c,|w_i-w_j|\}),
                                       \max_{i<j}e(\{c,w_i,w_j\}),\ \max_{i<j,\,k\ne i,j}e(\{c,|w_i-w_j|,w_k\})\Big).
```
(This is `potential-weighting-upper-bound.md` §27.2(d)'s candidate closed form for
`\mathrm{OPT}_{-1}(\{c\},W)`, the `\sigma=-1` mirror of the certified-partial Two-Touch Lemma.)

**Statement.** For every `c\ge0` and every `W` with `|W|\le3`:
```
\mathrm{OPT}_{-1}(\{c\},W) = \mathrm{ThreeTouch}(c,W).
```

**Proof.** The inequality `\mathrm{OPT}_{-1}(\{c\},W)\ge\mathrm{ThreeTouch}(c,W)` is free: every term
inside `\mathrm{ThreeTouch}`'s outer `\max` is the value of some genuine selection of `W` (delete-all,
keep-one, match-one-pair-delete-rest, keep-a-pair, match-a-pair-and-keep-a-third), so
`\mathrm{OPT}_{-1}$ (the true maximum over *all* selections) is at least as large as the maximum over
this sub-list of selections.

For the reverse inequality, enumerate all selections of a `\le3`-element index set `\{1,\dots,q\}`
into Kept/Deleted/Matched-pairs (a partition, cost unrestricted since full slack is always available,
`\mathrm{potential-weighting-upper-bound.md}` §13.2):

- `q\le2`: **every** selection of `W` already appears literally as one of `\mathrm{ThreeTouch}`'s own
  candidate terms (delete-all = `e(\{c\})`; keep-one = `e(\{c,w\})`; keep-both = `e(\{c,w_1,w_2\})`
  (a `\max_{i<j}e(\{c,w_i,w_j\})` term); match-the-pair = `e(\{c,|w_1-w_2|\})`). Hence
  `\mathrm{OPT}_{-1}(\{c\},W)=\max$ over exactly this list `=\mathrm{ThreeTouch}(c,W)`.
- `q=3`: every selection **except** "keep all three" (`e(\{c,w_1,w_2,w_3\})`) already appears
  literally among `\mathrm{ThreeTouch}$'s candidates (delete-all, keep-one (`\times3`), keep-a-pair
  (`\times3`), match-a-pair-delete-third (`\times3`), match-a-pair-keep-third (`\times3`) — this
  exhausts every partition of a 3-element index set into Kept/Deleted/one-Matched-pair, since a
  3-element set admits at most one matched pair). It remains to show the one exceptional selection,
  "keep all three," never exceeds `\mathrm{ThreeTouch}(c,W)`:

  > **Claim.** For `w_1\ge w_2\ge w_3\ge0$ (WLOG sorted) and `c\ge0`:
  > `e(\{c,w_1,w_2,w_3\}) \le \mathrm{ThreeTouch}(c,\{w_1,w_2,w_3\})`, by exhibiting an explicit
  > dominating candidate in each of 4 exhaustive, mutually exclusive cases on the rank of `c` among
  > `\{w_1,w_2,w_3\}`:
  >
  > 1. **`c\ge w_1`.** Then `c` is the max of `\{c,w_1,w_2,w_3\}`, sorted order `(c,w_1,w_2,w_3)`, so
  >    `e=c-w_1+w_2-w_3`. Let `d:=w_1-w_2\ge0`; since `c\ge w_1\ge d\ge0` and `c\ge w_1\ge w_3`, `c` is
  >    the max of `\{c,d,w_3\}`, so by **Lemma A**, `e(\{c,d,w_3\})=c-|d-w_3|`. If `d\ge w_3`:
  >    `c-|d-w_3|=c-d+w_3=c-w_1+w_2+w_3\ge c-w_1+w_2-w_3$ (since `w_3\ge0`, in fact `2w_3\ge0`). If
  >    `d<w_3`: `c-|d-w_3|=c-w_3+d=c-w_1+w_2+(w_3-2w_3)`... directly: `c-w_3+d=c-w_3+w_1-w_2`, compare
  >    to target `c-w_1+w_2-w_3`: difference `=(c-w_3+w_1-w_2)-(c-w_1+w_2-w_3)=2(w_1-w_2)=2d\ge0`. Either
  >    way `e(\{c,d,w_3\})\ge` target. Since `\{c,d,w_3\}=\{c,|w_1-w_2|,w_3\}` is literally the
  >    touch-3 candidate `e(\{c,|w_i-w_j|,w_k\})` with `(i,j,k)=(1,2,3)`, this dominates.
  > 2. **`w_1\ge c\ge w_2`.** Sorted order `(w_1,c,w_2,w_3)`, `e=w_1-c+w_2-w_3`. Let `d':=w_2-w_3\ge0`;
  >    since `c\ge w_2\ge d'\ge0` and `w_1\ge c$, `w_1$ is the max of `\{w_1,c,d'\}`, so by **Lemma A**,
  >    `e(\{w_1,c,d'\})=w_1-|c-d'|`. Since `c\ge w_2\ge d'$, `|c-d'|=c-d'`, giving
  >    `w_1-c+d'=w_1-c+w_2-w_3`, **exactly equal** to the target. This is the touch-3 candidate
  >    `e(\{c,w_1,|w_2-w_3|\})` (`(i,j,k)=(2,3,1)`), so it dominates (with equality).
  > 3. **`w_2\ge c\ge w_3`.** Sorted order `(w_1,w_2,c,w_3)`, `e=w_1-w_2+c-w_3\le w_1-w_2+c$ (since
  >    `w_3\ge0`) `=e(\{c,w_1,w_2\})$ (sorted `w_1\ge w_2\ge c$ here, so `e(\{c,w_1,w_2\})=w_1-w_2+c`).
  >    This is the touch-2 "keep-pair" candidate `e(\{c,w_1,w_2\})`, so it dominates.
  > 4. **`c\le w_3`.** Sorted order `(w_1,w_2,w_3,c)`, `e=w_1-w_2+w_3-c\le w_1-c$ (since
  >    `w_2\ge w_3\ge0\Rightarrow w_3-w_2\le0`) `=e(\{c,w_1\})$ (sorted `w_1\ge c` here). This is the
  >    touch-1 candidate `e(\{c,w_1\})`, so it dominates.
  >
  > These four cases (`c\ge w_1$; `w_1\ge c\ge w_2$; `w_2\ge c\ge w_3$; `c\le w_3`) are exhaustive
  > (cover every possible rank of `c`) and their boundaries overlap consistently (each inequality
  > above is non-strict, so equal-boundary values are covered validly by either adjoining case,
  > verified to agree there). `\blacksquare`

  Combining: every selection of a `\le3`-element `W` is either literally a `\mathrm{ThreeTouch}`
  candidate, or (the "keep all three" case) is dominated by one, so
  `\mathrm{OPT}_{-1}(\{c\},W)=\max$ over all selections `\le\mathrm{ThreeTouch}(c,W)`. Combined with
  the free reverse inequality above, equality holds. `\blacksquare`

**Computational corroboration.** Case-split candidate-dominates-target check:
`0/6000` violations (`/tmp/round-17/verify_builder/verify_basecase_proof.py`); Case-2 exact-equality
check: `0/956`; direct end-to-end `\mathrm{OPT}_{-1}(\{c\},W)=\mathrm{ThreeTouch}(c,W)` for `|W|\le2`:
`0/3000` (all three, same file).

## Scope note (do not overclaim)

Lemma B closes **only** the base case `|W|\le3` of the induction proving
`\mathrm{OPT}_{-1}(\{c\},W)=\mathrm{ThreeTouch}(c,W)` for every `W` (Three-Touch, the `\sigma=-1`
mirror needed for Gap 1a's Two-Touch KEEP-branch `b_0\le w_1` sub-case). The general inductive step
(peeling `\max(W)` for `|W|\ge4`) is a separate task, **partially** advanced this round (DELETE branch
and both KEEP-branch parity sub-cases fully proved; MATCH branch open) — see
`potential-weighting-upper-bound.md` §28.3. Lemma A is fully general and unconditionally reusable
(no scope restriction).
