# Lemma: Delete-Suffices Insertion Domination

**Status:** CERTIFIED (round 16, discovered and proved by this round's `potential-weighting-upper-
bound` builder while investigating Gap 1c's `\xi^*=\emptyset` boundary case, per the outline-
reviewer's round-16 flag). Fully general, no `\mathcal F`-provenance needed, elementary (two-line
proof, no case work).

## Statement

Let `C` be any finite multiset of nonnegative reals and `W` any finite list of nonnegative reals.
Suppose "delete everything" achieves the `\sigma=+1` optimum, i.e.
```
OPT_{+1}(C,W) = e(C).
```
Then for **any** two elements `w_a,w_b\in W` (with repetition/index-distinctness, i.e. any valid
matched pair), writing `d:=|w_a-w_b|`,
```
e(C) <= e(C u {d}).
```

## Proof

The selection of `W` that matches `w_a` with `w_b` (contributing the single value `d=|w_a-w_b|` to
the multiset fed to `e`) and deletes every other element of `W` is one particular, valid member of
`OPT_{+1}(C,W)`'s search space (the "delete contributes `0`, match contributes the pairwise
difference" convention, standing throughout `potential-weighting-upper-bound.md` §13.2). Its value is
`e(C\cup\{d\})`. Since `OPT_{+1}(C,W)` is, by definition, the **minimum** over the *entire* search
space, and this particular selection is one member of it,
```
OPT_{+1}(C,W) <= e(C u {d}).
```
Substituting the hypothesis `OPT_{+1}(C,W)=e(C)`,
```
e(C) <= e(C u {d}).      \blacksquare
```

## Remarks

- This is a genuinely free, one-line consequence of the definition of `OPT_{+1}$ as a minimum — no
  structural property of `C` or `W` is used beyond the hypothesis "deletion suffices" itself. It says:
  once you know deleting everything is already optimal for `(C,W)`, inserting *any* pairwise
  difference drawn from `W` into `C` can only make `e` go up (or stay the same), never down.
- **Application.** In `potential-weighting-upper-bound.md`'s scope family `\mathcal F`, at a genuine
  base-generator instance with `C=B_1:=\{b_0,d_{k^*}\}`, `W=\mathrm{Res}`, the quantity `M:=
  OPT_{+1}(B_1,\mathrm{Res})$ is exactly the object the still-open **Deletion-Suffices-for-`k^*`**
  sub-lemma (§21.1 Step 2, proved for `q\le3` by the round-14 builder, open for `q\ge4`) conjectures
  equals `e(B_1)=D_{k^*}`. **If** Deletion-Suffices-for-`k^*` holds at a given node, this Lemma
  immediately gives, for `d:=u_1-u_j` (`u_1:=\max(\mathrm{Res})`, any partner `u_j`, exactly the
  quantity used by Gap 1c's half-step lemma), `e(B_1)\le e(B_1\cup\{d\})` — **which is precisely the
  missing ingredient needed to close Gap 1c's half-step lemma in the `\xi^*=\emptyset` boundary case**
  (see `potential-weighting-upper-bound.md` §27 for the full derivation). This is a genuine, previously
  unnoticed **link between Gap 1a's Step 2 and Gap 1c's `\xi^*=\emptyset` sub-case** — proving
  Deletion-Suffices-for-`k^*` at general `q` would, as an immediate free corollary via this Lemma,
  also retire the `\xi^*=\emptyset` boundary snag in Gap 1c, with zero extra work.
- The Lemma's hypothesis ("deletion suffices") is genuinely necessary, not vacuous or automatic: an
  unconditional version (dropping the hypothesis, requiring `e(C)\le e(C\cup\{d\})` for arbitrary `C`
  and any `d=|w_a-w_b|$, `w_a,w_b\in W`) is **false** in general (`11{,}376/50{,}000` random
  counterexamples found, see Verification below) — so the deletion-suffices hypothesis is doing real
  work, not window-dressing.

## Verification

Independently checked by this round's builder with fresh code
(`/tmp/round-16/verify_builder/delete_suffices_corollary.py`): fully general (no `\mathcal
F`-provenance), random `(C,W)` with `|C|\in\{0,\dots,3\}`, `|W|\in\{2,\dots,5\}`, mixed-denominator
rationals — `4{,}000` raw trials, `1{,}615` genuine "deletion-suffices" nodes found (`OPT_{+1}(C,W)=
e(C)`), **`0`** violations of the conclusion across all pairs `(w_a,w_b)$ tested within each such
node. Negative control confirming the hypothesis is load-bearing: dropping it (arbitrary `C`, `d`
formed from two independent random values, no minimality constraint) gives `11{,}376/50{,}000`
(`\approx23\%`) failures.

## Used by

- `potential-weighting-upper-bound.md` §27 (Gap 1c's half-step lemma, the `\xi^*=\emptyset` boundary
  sub-case, conditional on Gap 1a's Step 2 / Deletion-Suffices-for-`k^*`).
