# Empty-Background Lemma, Background-Splitting Lemma, and the Non-Matching-Witness Criterion

**Certified by:** proof-reviewer, round 12, from approach `potential-weighting-upper-bound`
(round-12 builder, §18.2, §18.4). Independently re-derived by the reviewer from scratch (every
proof step re-traced symbolically, no gap found) and re-verified computationally with fresh code,
written directly from the file's own prose definitions (not adapted from the builder's harness) —
zero mismatches across every check below.

**Depends on:** the already-certified **Fact 1 & 2** ("dominant extraction",
`lemmas/dominant-extraction.md`, `e(M)\ge0` and `e(M)\le\max(M)` for nonnegative `M`) and **Fact 3**
(block extraction, `lemmas/insertion-and-cascade-facts.md`) — and, for the Non-Matching-Witness
Criterion, the already-certified Generalized Multi-Background Peeling Lemma trichotomy
(`potential-weighting-upper-bound.md` §13.2).

## Setup / notation

`e(M)` = alternating sum of the sorted-descending multiset `M` (`m_1-m_2+m_3-\dots`). For a
background multiset `B` (external, fixed, never selectable) and sorted list `W=(w_1\ge\dots\ge
w_k)`, `\sigma\in\{+1,-1\}`:
```
OPT_\sigma(B,W)    := \sigma-optimal value of e(B \cup K\text{-values} \cup M\text{-differences})
                       over ALL selections (K,D,M) of W (no crossing restriction).
OPT_KD_\sigma(C,W) := \sigma-optimal value of e(C \cup S) over all S\subseteq W (Keep/Delete only,
                       no matching at all).
```

## Statement 1 — Empty-Background Lemma

For **any** sorted `W` (any size, possibly empty) and `\sigma\in\{+1,-1\}`:
```
OPT_\sigma(\emptyset,W) = OPT_KD_\sigma(\emptyset,W),
```
with the explicit closed values `OPT_{+1}(\emptyset,W)=0` and `OPT_{-1}(\emptyset,W)=\max(W)` (or
`0` if `W=\emptyset`), in both cases achieved with **zero** matched pairs.

**Proof.** `\sigma=+1`: `D=W` gives `e(\emptyset)=0`, so `OPT_{+1}(\emptyset,W)\le0`; by Fact 1,
every selection's value is `\ge0`, so `OPT_{+1}(\emptyset,W)=0` exactly, via the zero-match
selection `D=W`. `\sigma=-1$ (`W\ne\emptyset`): `K=\{w_1\}` gives `e(\{w_1\})=w_1`, so
`OPT_{-1}(\emptyset,W)\ge w_1`; by Fact 2, every selection's resulting multiset has every element
`\le w_1` (kept values are literal elements of `W`; a matched difference `w_i-w_j\le w_i\le w_1`),
so every value is `\le w_1`, giving `OPT_{-1}(\emptyset,W)\le w_1`. Hence `=w_1` exactly, via the
zero-match selection `K=\{w_1\}`. Since both optimal values are achieved with zero matched pairs,
the identical constructions are available to `OPT\_KD` (which only forbids matching, not these
particular selections), and `OPT\_KD\ge OPT` always (smaller search space), giving
`OPT\_KD_\sigma(\emptyset,W)=OPT_\sigma(\emptyset,W)` too. `\blacksquare`

## Statement 2 — Background-Splitting Lemma

For **any** background `C`, sorted `W`, `\sigma\in\{+1,-1\}`: write `w_{\max}:=\max(W)` (or, if
`W=\emptyset`, treat `C_{\mathrm{hi}}:=C`, `C_{\mathrm{lo}}:=\emptyset`), `C_{\mathrm{hi}}:=\{c\in
C: c\ge w_{\max}\}`, `C_{\mathrm{lo}}:=C\setminus C_{\mathrm{hi}}`, `h:=|C_{\mathrm{hi}}|`. Then
```
OPT_\sigma(C,W) = e(C_{\mathrm{hi}}) + (-1)^h \cdot OPT_{\sigma\cdot(-1)^h}(C_{\mathrm{lo}}, W),
```
and **identically** with `OPT` replaced by `OPT\_KD` throughout.

**Proof.** For *any* selection of `W` with resulting "rest" multiset `R` (kept values `\cup`
matched differences), every element of `R` is `\le w_{\max}` (kept values are elements of `W`,
hence `\le w_{\max}`; a matched difference `w_i-w_j\le w_i\le w_{\max}` since `i<j` in sorted order
forces `w_i\ge w_j\ge0`). So `C_{\mathrm{hi}}` dominates `C_{\mathrm{lo}}\cup R` entirely, and Fact
3 gives, **selection-by-selection** (the split point `h=|C_{\mathrm{hi}}|` is fixed, depending only
on `C` and `w_{\max}`, not on the selection):
```
e(C\cup R) = e(C_{\mathrm{hi}}) + (-1)^h e(C_{\mathrm{lo}}\cup R).
```
Taking `\sigma`-opt over all selections of `W` on both sides (the additive/multiplicative constant
`e(C_{\mathrm{hi}})`, `(-1)^h` do not depend on the selection, so they factor out of the
optimization) gives the claimed identity for `OPT`. Restricting the selection range to `K/D`-only
proves the `OPT\_KD` version identically (the pointwise identity above holds for *every*
individual selection, matched or not, so it restricts to any sub-collection of selections).
`\blacksquare`

**Corollary (reduction of a "no-second-trigger"/Claim-A-type inequality across background
splitting).** Since the map `x\mapsto e(C_{\mathrm{hi}})+(-1)^h x` is a fixed
order-preserving-or-reversing affine transform applied *identically* to every candidate value of
`OPT_{\sigma(-1)^h}(C_{\mathrm{lo}},W)` and of `OPT\_KD_{\sigma(-1)^h}(C_{\mathrm{lo}},W)` (by the
selection-by-selection identity above, this transform commutes with restricting to any
branch of a trichotomy on `W`'s own top element, e.g. a DELETE/KEEP/MATCH split): **any inequality
of the shape "the `\sigma`-optimal value of one restricted class of selections of `(C,W)` does not
strictly beat another" holds at `(C,W,\sigma)` if and only if the same inequality (with the same
restricted classes) holds at `(C_{\mathrm{lo}},W,\sigma\cdot(-1)^h)`.** In particular this applies
directly to `potential-weighting-upper-bound.md`'s "Claim A" (MATCH does not strictly beat
`\sigma`-opt(DEL,KEEP) at a node of the scope family `\mathcal F`, §17.2/§17.5): Claim A holds at
`(C,W,\sigma)` iff it holds at `(C_{\mathrm{lo}},W,\sigma\cdot(-1)^h)`. Since `C_{\mathrm{lo}}=
\emptyset` is fully resolved by the Empty-Background Lemma (Statement 1) unconditionally, this
proves Claim A unconditionally at every node where `C` is already "dominated" (`C_{\mathrm{hi}}=C`,
i.e. every element of `C` is `\ge\max(W)`) — the open content of Claim A is confined to nodes where
`C_{\mathrm{lo}}\ne\emptyset`.

## Statement 3 — Non-Matching-Witness Criterion

For any `(C,W,\sigma)` with `W\ne\emptyset`, write `w_1:=\max(W)`, `V:=OPT_\sigma(C,W)`. Then: the
MATCH branch of `(C,W)`'s own DELETE/KEEP/MATCH trichotomy does not strictly beat `\sigma`-opt
(DEL,KEEP) **if and only if** some optimal witness achieving `V` does not match `w_1`.

**Proof.** (`\Leftarrow`) Suppose an optimal witness `\eta` achieves `V` with `w_1\in D(\eta)` (the
`w_1\in K(\eta)` case is symmetric, with KEEP in place of DELETE). Restricting `\eta` to
`W\setminus\{w_1\}` is a valid selection of that smaller list with the same value (`w_1`
contributes nothing to a deletion), so `\mathrm{DEL}\le V` (writing the `\sigma=+1` direction;
`\sigma=-1` is identical with inequalities reversed). Combined with the trivial direction
`\mathrm{DEL}\ge V` (each individual branch of the already-certified Generalized Multi-Background
Peeling Lemma's trichotomy is `\sigma`-at-least-as-extreme as the overall optimum `V`), get
`\mathrm{DEL}=V` exactly. Then `\sigma`-opt(DEL,KEEP) is between `V=\mathrm{DEL}$ and `V$ (at most
as extreme as `\mathrm{DEL}=V`, at least as extreme as `V` since both branches are `\ge V`), so it
equals `V` exactly — i.e. MATCH (itself `\ge V$ by the same trivial bound) cannot strictly beat it.
(`\Rightarrow`) If MATCH never strictly beats `\sigma`-opt(DEL,KEEP), then (combined with the
trivial converse direction) `\sigma`-opt(DEL,KEEP)`=V` exactly. Whichever of DEL, KEEP attains this
has its own optimal witness (existence automatic, finite search space) extending to a full
selection of `W` (deleting, resp. keeping, `w_1`) achieving `V` without matching `w_1`.
`\blacksquare`

## Verification

All independently re-derived symbolically from the prose above (not copied from the builder's
proof) and re-verified computationally with fresh code
(`/tmp/round-12/proof-reviewer-work/mydefs.py` + drivers), brute force over the full finite
selection space, `int` arithmetic:
- Empty-Background Lemma: `2000/2000` random trials (`q=0,\dots,6`, both signs), `0` mismatches;
  exact closed values confirmed.
- Background-Splitting Lemma, both `OPT` and `OPT\_KD` versions: `3000/3000` each, `0` mismatches;
  the underlying **pointwise, selection-by-selection** identity independently checked over the
  *entire* selection space of every one of the 3000 trials (not just the aggregated optimum), `0`
  mismatches; the **Corollary** (Claim-A equivalence across the split) independently re-verified
  directly, `1200/1200`, `0` mismatches.
- Non-Matching-Witness Criterion: `3000/3000` random trials, `0` mismatches.
- Sanity check: the underlying Generalized Multi-Background Peeling Lemma trichotomy itself
  (`OPT_\sigma(C,W)=\sigma`-opt(DEL,KEEP,MATCH)), `2000/2000`, `0` mismatches; harness additionally
  validated bit-for-bit against two of the file's own worked examples before being trusted
  (round-9's `B=\{2,4\},Z=(6,3,2,1)`: `OPT_{+1}=0`; round-12's `C=\{5,8\},W=(10,8,7,2)`:
  `OPT_{+1}=0,OPT\_KD_{+1}=2`; `c=1,W=(10,8,7)`: `OPT_{+1}=0,OPT\_KD_{+1}=1`).

## Reusable by

Any approach reasoning about `OPT_\sigma`/`OPT\_KD_\sigma` on a background+list pair: the
Empty-Background Lemma gives an unconditional base case whenever the background vanishes; the
Background-Splitting Lemma (and its Corollary) lets any inequality comparing restricted classes of
selections be reduced, for free, to the sub-instance with only the "non-dominating" part of the
background, whenever the background contains any element(s) at or above the list's current
maximum; the Non-Matching-Witness Criterion turns any such inequality (in particular
`potential-weighting-upper-bound.md`'s still-open Claim A / Gap 1) into a pure existence question
about optimal witnesses, decoupled from any explicit DELETE/KEEP/MATCH value bookkeeping.
