# Shallow all-cycles resolution: Guaranteed-Untouched-Original, Shared-Value Cycle-Breaking,
and Cross-Type Cycle Infeasibility Lemmas

**Certified by:** proof-reviewer, round 7, from approach `dyadic-cascade-induction` (round-7
builder, §5.4 Steps 1-2 and the new Cross-Type Cycle Infeasibility Lemma). Independently
re-derived (the pigeonhole and sum-and-dominance arguments re-checked step-by-step from
scratch) and independently re-verified computationally (exact `sympy`/`Fraction` arithmetic,
bounded instances only) by the reviewer.

**Depends on:** the certified `lemmas/vertex-lemma.md` (single-cut piecewise linearity and its
joint-optimum classification), `lemmas/duplicate-pair-invariance.md` (Lemma P), and the
"superincreasing subset-dominance" fact already used in `lemmas/superincreasing-no-early-zero.md`
(if `i_0` is the smallest original index among a set of chosen terms of a strictly
superincreasing sequence, the term at `i_0` strictly exceeds the sum of all other chosen terms).

## Statement

Fix a strictly superincreasing sequence with `k=m+1` terms (in particular `A=D_m=(2^m,\dots,2,1)`)
and consider any physical Xiang-Yu strategy using `\le m` cuts, at whose global minimizer the
tie-dependency graph (as defined in `lemmas/dm-completeness-partial.md`) is a nonempty union of
directed cycles. Fix one such cycle, of length `L`, on cuts `c_1,\dots,c_L` acting on pieces
`b_1,\dots,b_L`.

1. **Guaranteed-Untouched-Original Lemma.** Any such `\le m`-cut strategy leaves at least one
   original piece of `A` completely untouched (since the cut-forest's roots number at most `m`,
   one per cut, while `A` has `k=m+1>m` original pieces — pigeonhole).

2. **Shared-Value Cycle-Breaking Lemma.** If the cycle is of **uniform shared-value type**
   (every `b_i` is a *distinct original* piece of `A`, each cut once at the identical value `t`,
   `L\ge2`), then — given the untouched original piece guaranteed by (1) — this configuration is
   **never the true joint minimizer** of `e`: viewed as a function of the single free parameter
   `t` (every other piece, including the guaranteed-untouched original, held fixed), the
   resulting value is piecewise-linear (Vertex Lemma), so its minimum over `t` occurs either at a
   breakpoint where some surviving value `b_i-t` (or, for odd `L`, the one surviving leftover
   copy of `t`) crosses the untouched original — converting that cut from a cross-tie into a
   tie-to-an-untouched-original, breaking the cycle — or at a degenerate domain endpoint
   (`t\to0` or `t\to\min_i b_i`), which likewise reduces to a strictly-fewer-genuine-cuts
   configuration. A genuinely inescapable interior shared-value cycle optimum therefore never
   occurs.

3. **Cross-Type Cycle Infeasibility Lemma.** If the cycle is of **uniform cross-type** (every
   `b_i` a distinct original piece, `L\ge3`, with dependency `u_i+u_{i+1}=b_{i+1}` for
   `i=1,\dots,L`, indices mod `L`, where `u_i\in(0,b_i)` is cut `i`'s tying output), then **no
   solution exists**: summing all `L` equations gives `\sum u_i=S/2` where `S=\sum b_i`;
   relabelling so `b_1=\max_i b_i=:M`, the equation `u_L+u_1=M` combined with the sum gives
   `u_2+\dots+u_{L-1}=S/2-M`. By the superincreasing subset-dominance fact, `M>S-M`, i.e.
   `S/2-M<0`; but the left side is a sum of `L-2\ge1$ strictly positive terms, a contradiction.
   Hence no cross-type `L`-cycle (`L\ge3`) built from distinct originals of a strictly
   superincreasing sequence is ever physically realizable.

## Combined scope, honestly bounded

Together, (2) and (3) resolve every **uniform** all-cycles configuration whose participants are
all distinct, once-cut, **original** pieces of a strictly superincreasing base sequence (`L=2`
or uniform shared-value any `L`: dominated, never the true minimizer; uniform cross-type
`L\ge3`: infeasible). This is genuinely new content, not previously certified.

**Explicitly NOT resolved by this lemma (open, for a future round):**
- A cycle containing at least one **derived** (non-original, i.e. produced as a signed subset
  sum by an earlier resolved tie elsewhere in the strategy) participant. The natural extension
  of (3)'s dominance argument to such a participant was checked and shown to **fail** for `D_m`
  specifically (the needed inequality `a_{i^*}>2\sum_{l>i^*}a_l` reduces to `a_{i^*}<2`, false
  except at the smallest piece) — this is a genuine, demonstrated obstruction, not merely an
  untried case.
- A cycle that **mixes** shared-value-type and cross-type edges within itself (i.e. is not
  uniformly one type), even when every participant is an original piece. This case is
  **not proved either way** by (2) or (3) as stated: (2)'s breakpoint argument assumes a single
  free parameter `t` shared by every edge of the cycle, and (3)'s sum argument assumes every
  edge is of the `u_i+u_{i+1}=b_{i+1}` shape; a cycle mixing both edge shapes satisfies neither
  hypothesis as given. The reviewer independently ran an exhaustive (not sampled) search over
  every subset/ordering/edge-type-pattern with at least 2 of each edge type, for `D_4` (`L=4,5`,
  `720`+`2400` full enumerations) and `D_5` (`L=4,5,6`, `2160`+`14400`+`36000` full
  enumerations): **zero feasible mixed-type cycles found** — suggestive that mixed cycles are
  also infeasible, but **this is not proved** and is not claimed as proved by either the builder
  or this certification. Flag this precisely as the next concrete target.

## Proof detail

Full derivation in `dyadic-cascade-induction.md` §5.4 (Steps 1-2, and the boxed Cross-Type
Cycle Infeasibility Lemma with its proof). The pigeonhole argument (1), the piecewise-linear
breakpoint argument (2) via the certified Vertex Lemma, and the sum-and-dominance argument (3)
were each independently re-derived from scratch by the reviewer with no gap found.

## Verification

- (1): elementary, re-derived directly, no computation needed.
- (2): spot-checked on a concrete instance (`D_2=(4,2,1)`, tying pieces `4` and `2` at shared
  value `t\in(0,2)`, piece `1` untouched): `e(t)` is exactly `3` (constant) for `t\in[0,1]`, then
  strictly decreasing on `(1,2)` towards `1` as `t\to2^-` (a degenerate boundary) — confirming
  the claimed piecewise-linear shape, with the true minimum approached only at the degenerate
  boundary, never at an interior point, and the `t=1` breakpoint (tying the untouched piece `1`)
  is not itself the global min but is where the configuration ceases to be a genuine 2-cycle.
- (3): independently reproduced by exact `sympy` linear-system solving for `L=3,4,5` on
  `D_2,D_3,D_4` (100 total random subset/ordering trials): odd `L` always gives a unique
  solution violating `u_i\in(0,b_i)` for some `i`; even `L` is always inconsistent — matching
  the proof's predicted failure mode exactly, zero exceptions.
- Mixed-edge-type mini-search (reviewer's own addition, not in the original submission):
  exhaustive over all subsets/orderings/patterns for `D_4` (`L=4,5`) and `D_5` (`L=4,5,6`) with
  at least 2 edges of each type — zero feasible configurations found (corroborates, does not
  prove, that this residual case may also resolve the same way).

## Reusable by

Any approach reasoning about the all-cycles obstruction in `lemmas/dm-completeness-partial.md`
for a strictly superincreasing base sequence. **Scope note, load-bearing:** this lemma narrows
(does not close) the "all-cycles" caveat — the residual open target for promoting
`lemmas/superincreasing-no-early-zero.md`'s D/M-sequence lower bound to the true physical lower
bound is now precisely: (a) any cycle with a derived participant, or (b) any cycle mixing
shared-value and cross-type edges among original participants. Do not cite this lemma as
closing the all-cycles case in full — only the uniform-type, all-original sub-case is closed.
