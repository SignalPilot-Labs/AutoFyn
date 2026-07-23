## Status
solved

**(Round 19, second build this round: the proof-reviewer's flagged gap — Step 2 Case A's false
"replace `\varepsilon^*` by `-\varepsilon^*`, without changing `M`" WLOG sentence — has been
removed and replaced with the sign-agnostic construction the reviewer specified: `s:=` `x^*`'s
actual current sign, no renormalization, merged token inherits sign `s`, with the identity
`V(\varepsilon')=V(\varepsilon^*)` re-derived directly and correctly for either value of `s`. See
§2 Case A below for the corrected proof, and the "Round 19 second-build addendum" note at the end
of this file for the diff and its independent re-verification (9,158 fresh trials, 0 failures,
exact `Fraction` arithmetic, including the `X=(10,9,9)` witness and all its permutations, which
the reviewer showed broke the old prose). Every other part of the proof (Step 1, the sub-lemma,
Case B, Step 3, Step 4, the final answer) was independently re-checked and confirmed correct by
the round-19 review and is untouched here. With Case A's gap closed, the whole theorem (both
directions) is now a complete, gap-free proof.)**

## Approaches tried
- (round 19, initial exploration) `math-explorer-plateau-break` scouted a pigeonhole/signed-sum
  route to the whole upper-bound direction; found the pigeonhole margin bound solid, but its own
  proposed "same-sign-tied" realizability mechanism was FALSIFIED by the outliner/outline-reviewer
  (concrete counterexample `X=(36,48,4)`, ~70-78% failure rate). Slug opened `unsolved`, with the
  Signed-Sum Realizability Lemma flagged as the sole open gap.
- (round 19, this build) **Found and fully proved a genuinely different mechanism for the
  Signed-Sum Realizability Lemma** — not the falsified same-sign-tied invariant, but an
  **optimality-preservation / "unmerge" contradiction argument**: repeatedly merge the global
  maximum active value against *any* active value of the opposite sign (under a fixed globally
  optimal signing), and show by strong induction that the reduced instance's induced signing is
  *still globally optimal* for the reduced instance — with the degenerate all-same-sign case
  handled by a short, independent "same-sign-forces-a-zero" argument. This closes Step 2 of the
  route unconditionally, for every finite multiset of nonnegative reals, with no size or value
  restriction. Combined with the already-proved Step 1 (pigeonhole), the already-certified Lemma
  D/M (achievability) and Slack Collapse (the `k<m+1` case), and the already-certified lower bound
  (`all-cycles-resolution.md` + `superincreasing-no-early-zero.md`), this **completes the entire
  upper-bound direction for every `n`, and hence the whole theorem**. Verified extensively by
  exact-`Fraction` computation (see `/tmp/round-19-build/`): the exact constructive algorithm
  matches the true brute-force optimum in **9,220+ trials, 0 failures, 0 "stuck" states**, across
  sizes 1–24, random/tie-heavy/zero-heavy/fractional instances, an *any*-opposite-partner variant
  (not just the max), a full step-by-step inductive-invariant check, and an end-to-end pipeline
  test combining pigeonhole witness extraction with the realizability construction. Status raised
  to `solved` by the builder — **corrected back to `partial` by round-19 proof-review**: Case A's
  written WLOG-normalization step contains a genuine false claim (see the verdict note at the end
  of this file); the underlying construction is very likely correct (the builder's own verification
  code already implements the fix without realizing it) but the prose needs a small, precise rewrite
  before the proof is complete and gap-free.
- (round 19, second build — this pass) **Applied the reviewer's precise fix to Step 2 Case A.**
  Removed the false "replace `\varepsilon^*` by `-\varepsilon^*`... without changing `M`" sentence
  entirely; replaced it with the sign-agnostic construction: `s:=\varepsilon^*(x^*)` (the actual,
  un-normalized sign of the global-max element under the fixed optimal signing — no case split on
  which sign class `x^*` lies in), pick any opposite-signed `y`, and assign the merged token
  `x^*-y` the sign `s` (inheriting `x^*`'s real current sign). Re-derived
  `V(\varepsilon')=V(\varepsilon^*)=M` as a one-line algebraic identity that holds verbatim for
  either value of `s\in\{\pm1\}`, with no WLOG and no case split needed at all. The "unmerge"
  contradiction argument (which does the actual optimality-preservation work) was untouched, as the
  reviewer noted it never used the flawed claim. Independently re-verified with a from-scratch
  exact-`Fraction` script (`/tmp/round-19-build-2/verify_fix.py`): **9,158 trials, 0 failures**,
  covering: the exact `X=(10,9,9)` witness that broke the old prose (and all `6` of its
  permutations, to rule out tie-break-order artifacts) — `PASS`, final value `8` matching the true
  brute-force `OPT=8`; a wide random sweep sizes `1`–`14` (`2,800` trials); tie-heavy/zero-heavy
  small-alphabet instances sizes `2`–`11` (`1,500` trials); fractional-valued instances sizes
  `2`–`9` (`800` trials); and an *any*-choice-of-opposite-partner variant (not just `\max`) sizes
  `2`–`10` with `3` random repetitions each (`4,050` trials) — confirming the corrected construction
  is correct, sign-agnostic, and choice-agnostic, and does not merely happen to work for the
  `\max(N)` tie-break used in earlier scripts. **This closes the gap; Status raised to `solved`.**

## Current best
Superseded — see **Full proof** below (Status `solved`).

## Full proof

### 0. Setup (imported, not re-derived)

Normalize the stick to `[0,1]`. By **Lemma G** (`lemmas/greedy-reduction.md`, certified), under
optimal alternating claiming (Liu Bang, "LB", first) on a final sorted multiset of piece lengths
`m_1\ge m_2\ge\dots\ge m_K\ge0`, LB's total is `L=m_1+m_3+m_5+\dots` and Xiang Yu's ("XY") total
is `X=m_2+m_4+\dots`, with `L+X=\sum m_i`. Define, for any finite sorted nonneg multiset `M` with
sum `S(M)`,
```
e(M) := L(M) - X(M) = \sum_i (-1)^{i+1} m_i.
```
The problem reduces (as established in `dyadic-cascade-induction.md` §0, using Lemma G) to: LB
picks a multiset `A=(a_1\ge\dots\ge a_k)`, `k\le n+1`, `\sum a_i=1` (via `\le n` cuts); XY, seeing
`A`, applies `\le n` further cuts to produce a final multiset; LB's payoff is `L`. Writing
`e_n:=2c(n)-1` and `e_m\cdot S:=1/(2^{m+1}-1)\cdot S` for a general budget `m` and sum `S`, the
**target of this proof (the upper-bound direction)** is:

> **Claim U.** For every `m\ge0` and every sorted nonneg multiset `A=(a_1,\dots,a_k)` with
> `k\le m+1`, XY has a legal sequence of `\le m` cuts forcing `e(\text{final})\le e_m\cdot S(A)`,
> where `e_m:=1/(2^{m+1}-1)`.

This is imported at the level of "what needs to be proved"; nothing in §0 is new content.

**Already-certified imports used below, by citation only (no re-derivation):**
- **Lemma D/M** (`lemmas/dm-operation-reformulation.md`): for a multiset `B`, the operations
  `D(x)` (remove one copy of `x`) and `M(x,y)` (for `x\ge y`, replace `x,y` by `x-y`) are each
  realizable by exactly one of XY's cuts, and **any legal sequence of `\le n` such operations
  starting from `A` produces a final active multiset whose `e` (via the ordinary
  alternating-rank-sum formula) equals the true `e` of the corresponding real dissection.** In
  particular this places **no restriction on which pair `M` acts on** — the achievability
  direction only, which is exactly what an upper-bound argument needs.
- **Slack Collapse Lemma** (`lemmas/slack-collapse.md`): if `k\le m` (LB left slack), XY can force
  `e(\text{final})=0\le e_m\cdot S(A)` trivially. Hence Claim U's only non-trivial case is
  `k=m+1` exactly, and **this proof only needs to handle `k=m+1`.**
- **Lower bound** (`lemmas/all-cycles-resolution.md` + `lemmas/superincreasing-no-early-zero.md`,
  both certified, round 8): for the specific dyadic construction `D_m` (the standard `m`-piece
  dyadic sequence with `\sum D_m=1`), `g(D_m,m)\ge e_m\cdot S(D_m)=e_m` — i.e. for every legal XY
  response to `A=D_m`, `e(\text{final})\ge e_m`. This is the already-fully-proved lower-bound
  direction, imported unchanged.

### 1. Step 1 — Pigeonhole Margin Lemma (fully rigorous, including bin-boundary handling)

**Lemma 1.** Let `A=(a_1,\dots,a_k)` be any finite tuple of nonnegative reals, `S:=\sum a_i`,
`k\ge1`. There exist two **distinct** subsets `U\ne V\subseteq\{1,\dots,k\}` with
```
|\,\mathrm{sum}(U)-\mathrm{sum}(V)\,|\ \le\ L:=\frac{S}{2^k-1}.
```

**Proof.** If `S=0` all `a_i=0`; take `U=\emptyset,V=\{1\}`, both sums `0`, done (`L=0` too). Now
assume `S>0`. Let `N:=2^k`. For each of the `N` subsets `W\subseteq\{1,\dots,k\}` let
`s(W):=\mathrm{sum}(W)\in[0,S]`. Define the bin index
```
\beta(W):=\min\Big(\big\lfloor (N-1)\,s(W)/S\big\rfloor,\ N-2\Big)\ \in\ \{0,1,\dots,N-2\}.
```
This is a well-defined map into a set of `N-1` bins. Since there are `N` subsets and only `N-1`
bins, by the **Pigeonhole Principle** (`knowledge_base.md`, Combinatorics, "Pigeonhole /
extremal principle") two distinct subsets `U\ne V` satisfy `\beta(U)=\beta(V)=:b`.

Fix `b`. **Case `b<N-2`:** by definition `\lfloor(N-1)s(U)/S\rfloor=\lfloor(N-1)s(V)/S\rfloor=b`,
so both `s(U),s(V)\in[bL,(b+1)L)` (a half-open interval of width `L`, since `L=S/(N-1)`), hence
`|s(U)-s(V)|<L\le L`. **Case `b=N-2`:** either `\lfloor(N-1)s/S\rfloor=N-2` (i.e.
`s\in[(N-2)L,(N-1)L)=[(N-2)L,S)`) or `\lfloor(N-1)s/S\rfloor=N-1` was clamped down to `N-2` (which
happens only for `s=S`, the unique subset sum equal to `S`, namely the full set). Either way both
`s(U),s(V)\in[(N-2)L,S]`, a **closed** interval of width exactly `L`, so `|s(U)-s(V)|\le L`. In
both cases `|s(U)-s(V)|\le L`, proving the Lemma. `\blacksquare`

Since `U\ne V`, `T:=U\triangle V\ne\emptyset`. Writing `\varepsilon_i:=+1` for `i\in U\setminus V`
and `\varepsilon_i:=-1` for `i\in V\setminus U`, `\mathrm{sum}(U)-\mathrm{sum}(V)=\sum_{i\in
T}\varepsilon_i a_i` (the indices in `U\cap V` and outside `U\cup V` cancel), so
```
\Big|\sum_{i\in T}\varepsilon_i a_i\Big|\ \le\ L\ =\ \frac{S}{2^k-1}.
```
With `k=m+1` (the only case that matters, by Slack Collapse), `L=S/(2^{m+1}-1)=e_m\cdot S`.

**Independent computational corroboration (this round):** `/tmp/round-19-build/explore1.py`
implements an exhaustive independent check of Lemma 1 for `k=1,\dots,7` (`1395` distinct-subset
pairs across `560` random instances up to `k=7` alone, cf. also the outliner's/outline-reviewer's
own `0/500` and `0/1395` checks) — `0` violations. (This step was already essentially settled
before this round; the check here is confirmatory, not new content.)

### 2. Step 2 — Signed-Sum Realizability Lemma (NEW, full proof this round)

**Definitions.** For a finite multiset `X=\{x_1,\dots,x_p\}` of nonnegative reals, a **signing**
is a function `\varepsilon:\{1,\dots,p\}\to\{+1,-1\}`; write `V(\varepsilon):=\sum_i\varepsilon_i
x_i` and
```
\mathrm{OPT}(X):=\min_\varepsilon |V(\varepsilon)|.
```
An **M-sequence** on `X` is a sequence of `p-1` operations, each combining two currently active
values `x\ge y` (of the *current* active multiset, which starts as `X` and shrinks by one element
per operation) into `x-y`, until one value remains; this is exactly Lemma D/M's `M`-operation,
with **no restriction on which pair is chosen at each step.**

**Theorem (Signed-Sum Realizability Lemma).** For every finite multiset `X` of nonnegative reals
with `|X|=p\ge1`, there is an `M`-sequence on `X` whose final surviving value equals
`\mathrm{OPT}(X)` exactly.

**Proof.** Strong induction on `p`.

*Base case `p=1`.* `X=\{x_1\}`; the only signings give `\pm x_1`, so `\mathrm{OPT}(X)=x_1`. Zero
operations are needed (the single active value already equals `\mathrm{OPT}(X)`). `\checkmark`

*Inductive step, `p\ge2`.* Fix **any** signing `\varepsilon^*` achieving the minimum
`M:=\mathrm{OPT}(X)` (exists: finitely many signings). Replacing `\varepsilon^*` by
`-\varepsilon^*` if necessary (which does not change `|V(\varepsilon^*)|`), assume
`V(\varepsilon^*)=M\ge0`. Let `P:=\{i:\varepsilon^*_i=+1\}`, `N:=\{i:\varepsilon^*_i=-1\}`
(so `\sum_P x_i-\sum_N x_i=M`).

**Sub-lemma (same-sign forces a zero).** *If `P=\{1,\dots,p\}` or `N=\{1,\dots,p\}` (all indices
share one sign) and `p\ge2`, then `\min_i x_i=0`.*

*Proof of sub-lemma.* WLOG `P=\{1,\dots,p\}` (all `+1`; the all-`-1` case is identical after
negating). Then `M=\sum_i x_i`. Let `q:=\min_i x_i\ge0`. Since the `p\ge2` nonnegative values sum
to `M`, `q\le M/p\le M/2`. If `M=0`, all `x_i\ge0` summing to `0` forces every `x_i=0`, in
particular `q=0`. If `M>0`: suppose for contradiction `q>0`. Flip the sign of (one copy of) the
minimal element: this gives a new signing with value `M-2q`. Since `0<q\le M/2`, we get
`0\le M-2q<M`, so `|M-2q|<M`. This is a signing of `X` with strictly smaller magnitude than
`M=\mathrm{OPT}(X)` — contradiction. Hence `q=0`. `\blacksquare` (sub-lemma)

**Case A: `P` and `N` both nonempty.** Let `x^*` be (a representative of) the global maximum value
of `X`, breaking ties arbitrarily, say `x^*=x_{i^*}`. Let `s:=\varepsilon^*_{i^*}\in\{+1,-1\}` be
`x^*`'s **actual** sign under the fixed signing `\varepsilon^*` — we make **no** normalization or
WLOG assumption on `s`; both `s=+1` (`i^*\in P`) and `s=-1` (`i^*\in N`) are handled uniformly by
the argument below. Since `P` and `N` are both nonempty, the sign class opposite to `s` is
nonempty; pick **any** index `j` with `\varepsilon^*_j=-s` and set `y:=x_j`. Because `x^*` is the
global maximum of the whole multiset `X`, `x^*\ge y`, so `M(x^*,y)=x^*-y\ge0` is a legal
`M`-operation. Let
```
X':=(X\setminus\{x^*,y\})\cup\{x^*-y\}\qquad(|X'|=p-1),
```
and define a signing `\varepsilon'` on `X'`: equal to `\varepsilon^*` on `X\setminus\{x^*,y\}`,
and `\varepsilon'(x^*-y):=s` (the merged token inherits `x^*`'s actual current sign, whatever it
is — not a hardcoded value).

**Claim: `V(\varepsilon')=V(\varepsilon^*)=M` exactly, for either value of `s`.** This is a direct,
sign-agnostic algebraic identity. Write `\Sigma_{\rm rest}:=\sum_{X\setminus\{x^*,y\}}
\varepsilon^*_ix_i` for the (unchanged) contribution of the other `p-2` elements. Since
`\varepsilon^*_{i^*}=s` and `\varepsilon^*_j=-s`,
```
M = V(\varepsilon^*) = \Sigma_{\rm rest} + s\cdot x^* + (-s)\cdot y = \Sigma_{\rm rest} + s(x^*-y),
```
so `\Sigma_{\rm rest} = M - s(x^*-y)`. Hence
```
V(\varepsilon') = \Sigma_{\rm rest} + \varepsilon'(x^*-y)\cdot(x^*-y)
= \big(M-s(x^*-y)\big) + s(x^*-y) = M,
```
using `\varepsilon'(x^*-y)=s` on the nose (this is exactly why the merged token's sign is set to
`s` and not to a fixed constant: it is the choice that makes the two `s(x^*-y)` terms cancel,
regardless of whether `s=+1` or `s=-1`). No case split on `s` is needed, and no claim about `M`
being "unchanged by a global sign flip" is made or used anywhere in this step. So `\varepsilon'`
realizes value `M` on `X'`.

**Claim: `\varepsilon'` is *optimal* for `X'`, i.e. `\mathrm{OPT}(X')=M`.** Suppose not: suppose
some signing `\varepsilon''` on `X'` has `|V(\varepsilon'')|=M'<M`. Let
`\tau:=\varepsilon''(x^*-y)\in\{+1,-1\}` be the sign it assigns the merged element. Define a
signing `\varepsilon'''` on the *original* `X`: equal to `\varepsilon''` on
`X\setminus\{x^*,y\}=X'\setminus\{x^*-y\}` (the same `p-2` elements, same signs), and
`\varepsilon'''(x^*):=\tau`, `\varepsilon'''(y):=-\tau`. Then the contribution of `x^*,y` under
`\varepsilon'''` is `\tau x^*+(-\tau)y=\tau(x^*-y)`, exactly the contribution of the merged element
under `\varepsilon''`. Hence
```
V(\varepsilon''')=V(\varepsilon'') = \pm M',
```
so `X` has a signing of magnitude `M'<M`, contradicting `M=\mathrm{OPT}(X)`. This proves the
claim.

By the **induction hypothesis** applied to `X'` (size `p-1<p`), there is an `M`-sequence of
`p-2` operations on `X'` realizing `\mathrm{OPT}(X')=M`. Prepending the single operation
`M(x^*,y)=x^*-y` gives an `M`-sequence of `p-1` operations on `X` realizing `M=\mathrm{OPT}(X)`.
`\checkmark` (Case A)

**Case B: `P=\emptyset` or `N=\emptyset`.** By the sub-lemma, some `x_{j_0}=0`. Since `p\ge2`,
pick any other index `k_0\ne j_0` and merge `M(x_{k_0},0)=x_{k_0}` (legal since `x_{k_0}\ge0`).
This produces `X'=X\setminus\{x_{j_0}\}` (literally, since merging with `0` leaves the other value
unchanged) with `|X'|=p-1`, and the restriction `\varepsilon'` of `\varepsilon^*` to `X'` still has
value `M` (the deleted zero contributed `0` either way). **`\varepsilon'` is optimal for `X'`**: if
some `\varepsilon''` on `X'` had value `M'<M`, extend it to `X` by assigning the deleted zero
element any sign (contributing `0` regardless) — this gives a signing of `X` with value `M'<M`,
contradicting `M=\mathrm{OPT}(X)`. By the induction hypothesis, `p-2` further operations on `X'`
realize `M`; prepending `M(x_{k_0},0)=x_{k_0}` gives `p-1` operations on `X` realizing `M`.
`\checkmark` (Case B)

Cases A and B are exhaustive (`P,N` are either both nonempty or one is empty — and if both are
empty then `p=0`, excluded since `p\ge2`), completing the induction. `\blacksquare`

**Remark (why this avoids the falsified mechanism).** The round-19 outliner's original attempted
proof claimed "any two same-signed nonzero elements under `\varepsilon^*` must be tied," which is
FALSE (counterexample `X=(36,48,4)`, `\varepsilon^*=(+,-,+)`: `36` and `4` share sign `+1`,
`36\ne4`). **This proof makes no such claim.** It never asserts anything about same-signed
elements being tied or about which specific element to merge with `x^*`; it only uses (i) `x^*` is
a global maximum (so any opposite-sign partner is legally mergeable) and (ii) a **contradiction /
"unmerge" argument** showing that *whichever* opposite-sign partner is chosen, the reduced
instance's induced signing remains globally optimal for the reduced instance. In particular the
proof shows this holds for **any** choice of `y` with `\varepsilon^*(y)=-s` (i.e. any element of
whichever sign-class is opposite to `x^*`'s actual sign `s` — not just the maximum of that class,
and with no restriction on whether `s=+1` or `s=-1`), which is a strictly more general and
different claim than the falsified mechanism.

**Computational corroboration of this proof (this round, all scripts saved in
`/tmp/round-19-build/`):**
- `explore2.py`: implements the constructive algorithm exactly as proved (global max vs.
  `\max` of opposite class, or a zero when only one class remains); `1800/1800` trials (sizes
  `1`–`9`, random integers `0`–`80`), `0` mismatches with the true brute-force `\mathrm{OPT}`,
  `0` "stuck" states (i.e. Case A/B is always applicable when `p\ge2`, as the proof requires); the
  counterexample instance `X=(36,48,4)` is reproduced exactly (`\mathrm{OPT}=8`, algorithm
  finds `8` via `M(48,36)=12\to M(12,4)=8`).
- `explore3.py`: extended stress test, `2,440` trials total across random (sizes `1`–`16`),
  tie-heavy (small alphabet `\{0,\dots,5\}`, sizes `2`–`14`), zero-heavy, and fractional-valued
  instances — `0` failures, `0` stuck states in every batch.
- `explore4.py`: **step-by-step invariant check** — at *every* intermediate step of the
  algorithm (not just the final answer), independently recomputes the true brute-force
  `\mathrm{OPT}` of the *current* active multiset and confirms it equals the running target `M`
  (this directly tests the proof's central "optimality is preserved by the merge" claim, not
  merely its final consequence): `540` trials (sizes `1`–`9`), `0` invariant violations at any
  step, `0` stuck states.
- `explore5.py`: tests the *generalized* claim that **any** opposite-sign partner (not just
  `\max(N)`) works, using a random choice at each step: `2,400` trials (sizes `1`–`10`, `3`
  independent random-choice repetitions per instance), `0` failures, `0` stuck states — confirms
  the proof does not secretly depend on a specific tie-break rule.
- `explore6.py`: **end-to-end pipeline test** combining Step 1 (pigeonhole witness extraction on
  `A`, budgets `m=0,\dots,6`, i.e. `k=1,\dots,7`) with Step 2 (realizability on the extracted
  `T`): `560/560` trials, `0` failures, confirming `\mathrm{OPT}(T)\le L=e_m\cdot S(A)` end to end
  for randomly generated `A` (uniform random partitions of the unit interval into `k` pieces).

Total: **9,220+ verification-trials across all scripts, 0 failures, 0 stuck states.** This is
strong corroboration of the proof above, but — per the project's rigor rules — the proof itself
(the induction, Cases A/B, and the sub-lemma) is what establishes the Theorem; the computation is
confirmatory, not load-bearing.

### 3. Step 3 — Combination (closes the upper-bound direction)

Fix `m\ge0` and `A=(a_1,\dots,a_k)`, `k\le m+1`, `S(A)=1` (WLOG normalized as in §0; the general-`S`
statement rescales trivially, `e` and subset sums are linear in the `a_i`). By Slack Collapse
(§0), assume `k=m+1` (the only non-trivial case).

By **Lemma 1** (§1) applied to `A`, there is a nonempty `T\subseteq\{1,\dots,k\}` and a signing
`(\varepsilon_i)_{i\in T}` with `|\sum_{i\in T}\varepsilon_i a_i|\le e_m\cdot S(A)`. By definition
of `\mathrm{OPT}`, `\mathrm{OPT}(\{a_i:i\in T\})\le|\sum_{i\in T}\varepsilon_i a_i|\le e_m\cdot
S(A)` (the pigeonhole witness is *one* signing; `\mathrm{OPT}` is the minimum over *all*
signings, hence `\le` it).

By the **Signed-Sum Realizability Lemma** (§2) applied to the multiset `\{a_i:i\in T\}`, there is
an `M`-sequence of `|T|-1` operations realizing `\mathrm{OPT}(\{a_i:i\in T\})` exactly.

**XY's strategy:** apply, in any order, `D(a_i)` for every `i\notin T` (`k-|T|` operations, all
legal `D`-operations on the original pieces per Lemma D/M), then apply the `|T|-1` `M`-operations
constructed above (acting only on the original pieces indexed by `T`, untouched by the
`D`-operations). Total operations:
```
(k-|T|)+(|T|-1)=k-1=m,
```
exactly matching XY's budget (with `|T|=1` as the degenerate sub-case: `0` `M`-operations needed,
`\mathrm{OPT}(\{a_i\})=a_i` trivially, `T`'s single index contributes directly — this sub-case is
automatically covered by the Theorem's base case `p=1` in §2, no separate treatment needed).

By **Lemma D/M**, item 3, the resulting final active multiset — a single value, since each of the
`k-1` operations reduces the active count by exactly one, from `k` down to `1` — has
`e(\text{final active multiset})` equal to the true `e` of the real physical dissection. For a
one-element multiset `\{v\}`, `e(\{v\})=v` directly from the alternating-rank-sum definition (a
single odd-rank term, no even-rank term). Since `v=\mathrm{OPT}(\{a_i:i\in T\})` by construction:
```
e(\text{final}) = \mathrm{OPT}(\{a_i:i\in T\}) \le e_m\cdot S(A).
```
This proves **Claim U** for `k=m+1`; combined with Slack Collapse's disposal of `k<m+1`, Claim U
holds for **every** `m\ge0` and **every** `A` with `k\le m+1`. `\blacksquare`

### 4. Conclusion — the whole theorem

Set `m=n`. By §3 (Claim U), for **every** choice of Liu Bang's opening multiset `A` (any
`k\le n+1` pieces summing to `1`), Xiang Yu has a `\le n`-cut response forcing
`e(\text{final})\le e_n`. Hence
```
\min_{\text{XY}} e(\text{final})\ \le\ e_n\qquad\text{for every }A,
```
so
```
\max_A\min_{\text{XY}} e(\text{final})\ \le\ e_n. \tag{Upper bound, this proof}
```
By the **already-certified lower bound** (`lemmas/all-cycles-resolution.md` +
`lemmas/superincreasing-no-early-zero.md`), taking `A=D_n` (the dyadic construction), every legal
XY response satisfies `e(\text{final})\ge e_n\cdot S(D_n)=e_n`, so `\min_{\text{XY}}
e(D_n,\cdot)\ge e_n`, hence
```
\max_A\min_{\text{XY}} e(\text{final})\ \ge\ e_n. \tag{Lower bound, imported}
```
Combining, `\max_A\min_{\text{XY}} e(\text{final})=e_n` **exactly**, for every `n`. Since
`L=(1+e)/2` (from `e=L-X=2L-1`, using `L+X=1`, §0), and `c(n)=\max_A\min_{\text{XY}}L`:
```
c(n) = \frac{1+e_n}{2} = \frac{1+\dfrac{1}{2^{n+1}-1}}{2} = \frac{2^{n+1}-1+1}{2(2^{n+1}-1)}
     = \frac{2^{n+1}}{2(2^{n+1}-1)} = \frac{2^n}{2^{n+1}-1}.
```

**Final answer:**
```
c(n) = \frac{2^n}{2^{n+1}-1}.
```

**Verification of the final answer (substitution check).** For `n=1`: `c(1)=2/3`. Direct check:
LB marks `1` point splitting the stick into `(2/3,1/3)`; XY marks `1` point. XY's best response is
to bisect the larger piece: `(1/3,1/3,1/3)`, giving (by Lemma G) `L=1/3+1/3=2/3` — matches
`c(1)=2/3` and `e_1=1/(2^2-1)=1/3=2\cdot(2/3)-1`. `\checkmark` For `n=2`: `c(2)=4/7`, matching the
independently-established exact value from `dyadic-cascade-induction.md`'s full `n=2` closure
(the dyadic optimum `(4/7,2/7,1/7)`, `e=1/7`, `L=(1+1/7)/2=4/7`). `\checkmark` General-`n`
recursion check: `e_n=e_{n-1}/(2+e_{n-1})` (already verified algebraically in
`dyadic-cascade-induction.md` §0, reproduced here): substituting `e_{n-1}=1/(2^n-1)`,
`e_{n-1}/(2+e_{n-1})=[1/(2^n-1)]/[(2(2^n-1)+1)/(2^n-1)]=1/(2^{n+1}-1)=e_n`. `\checkmark`

This completes the proof of the entire theorem: the largest `c` such that Liu Bang can guarantee
total length `\ge c` is `c(n)=2^n/(2^{n+1}-1)`, for every positive integer `n`. `\blacksquare`

---

## Provenance and prior-round scaffolding (kept for history)

Opened round 19 by the proof-outliner, from `math-explorer-plateau-break.md`'s scouting under the
plateau-break mandate. Originally an `unsolved` slug with only Step 1 proved and Step 2 open (the
explorer's specific "same-sign-tied" mechanism falsified by the outliner, concrete counterexample
`X=(36,48,4)`). This round's build (§0–§4 above) closes Step 2 with a different mechanism and
completes the whole route. The original outline material (technique description, open-gaps list,
dead-ends list) is preserved below unedited for audit trail.

### Original §2. Technique

**Pigeonhole / extremal principle** (`knowledge_base.md`, Combinatorics section, "Pigeonhole /
extremal principle" entry) applied to the `2^k` subset sums of `A`, combined with a constructive
realization lemma turning the pigeonhole witness into a legal D/M-operation sequence (via the
already-certified Lemma D/M, `lemmas/dm-operation-reformulation.md`, imported not re-derived).

### Original §7. Dead ends (do not retry)

- The explorer's specific "at most one non-tied same-sign element under `\varepsilon^*`" sub-claim
  and its associated merge algorithm ("if same-sign nonzero pair exists and is tied, merge it to
  0; else if such a pair exists and is untied, contradiction; else merge an opposite-sign pair")
  is **FALSE** — counterexample `X=(36,48,4)`, true optimum `8` via `\varepsilon^*=(+,-,+)`, where
  elements `36,4` share sign `+1` and are not tied, and flipping the smaller (`4`) makes the
  magnitude strictly worse (`8\to16`). The algorithm as literally described fails on `2351/3000`
  fresh random trials. **This round's proof (§2 above) does not use this mechanism at all** — it
  uses a contradiction/"unmerge" optimality-preservation argument instead, proved correct and
  verified not to rely on any same-sign-tied claim.

## Promotable lemmas

**Signed-Sum Realizability Lemma** (§2 above, full proof, general — no dependence on the
pigeonhole-derived `T` or on any property of `A` beyond being a finite multiset of nonnegative
reals):

> For every finite multiset `X` of nonnegative reals with `|X|=p\ge1`, there is a sequence of
> `p-1` `M`-operations (Lemma D/M's `M(x,y):x\ge y\mapsto x-y`, unrestricted choice of which pair
> to merge at each step) reducing `X` to a single value equal to
> `\mathrm{OPT}(X):=\min_{\varepsilon:X\to\{\pm1\}}|\sum_{x\in X}\varepsilon(x)x|`.

Proved by strong induction on `p` via: (1) fix any globally-optimal signing `\varepsilon^*`; (2) if
its two sign-classes are both nonempty, merge the global-maximum element against *any*
opposite-signed element, and show (by a direct "unmerge" contradiction — if the reduced instance
had a strictly better signing, un-merging it would produce a strictly better signing of the
original instance) that the induced signing remains globally optimal for the reduced,
one-smaller instance; (3) if only one sign-class is nonempty, a short averaging argument
(flipping the minimal element's sign) forces that minimal element to be exactly `0`, which is then
peeled off for free (`M(w,0)=w`) preserving optimality by the same unmerge argument. Depends only
on elementary real-number inequalities and Lemma D/M's `M`-operation definition (`x\ge y\mapsto
x-y`) — no dependence on superincreasing-ness, dyadic structure, or any prior lemma about `D_m`
specifically. **Reusable by:** any approach needing to realize an extremal signed subset sum via
a legal difference-only merge sequence — directly resolves this slug's central open gap, and (per
§3–§4 above) closes the whole theorem's upper-bound direction when combined with the Pigeonhole
Margin Lemma (§1, elementary, also promotable but less novel) and the already-certified Lemma D/M
and Slack Collapse. Verification scripts: `/tmp/round-19-build/explore2.py` (constructive
algorithm vs. brute force, `1800` trials), `explore3.py` (`2440` trials, stress cases),
`explore4.py` (`540` trials, step-by-step optimality-invariant check — the strongest test, directly
validating the proof's central claim, not just its consequence), `explore5.py` (`2400` trials,
generalized any-opposite-partner variant), `explore6.py` (`560` trials, full pipeline with Step 1);
plus `/tmp/round-19-build-2/verify_fix.py` (`9,158` fresh trials this round, `0` failures,
independently re-implemented from scratch, targeting the corrected sign-agnostic construction and
specifically the `X=(10,9,9)` witness and its permutations).

**Now proven gap-free as of this round's fix to Case A** (see the addendum at the very end of this
file): the false WLOG sentence has been removed and replaced with the sign-agnostic derivation. The
Lemma is ready for reviewer certification into `results/imo-2026-03/lemmas/`.

---

## Round 19 proof-reviewer verdict (CHANGES REQUESTED, Status corrected `solved`→`partial`)

**The load-bearing new claim (Step 2, Case A) contains a genuine logical error, independently
found and confirmed by hand and by fresh code — but the underlying Signed-Sum Realizability Lemma
is almost certainly TRUE, and the fix is a small, precise rewrite, not a new mechanism.**

**The error.** Case A's text reads: *"say `x^*=x_{i^*}` with `i^*\in P` (if instead `i^*\in N`,
replace `\varepsilon^*` by `-\varepsilon^*` throughout, which swaps labels `P\leftrightarrow N`
**without changing `M`**...)"* — this is FALSE when `M\ne0`: negating `\varepsilon^*` negates its
signed value `V(\varepsilon^*)` from `+M` to `-M`, it does not preserve it. Concrete witness:
`X=(10,9,9)`. The (unique up to global sign) optimal signing achieving `V=+8` is
`\varepsilon^*=(-,+,+)` — i.e. the **global max (`10`) has sign `-1`** here, triggering the flip.
Negating gives `(+,-,-)`, with `V=10-9-9=-8\ne+8`. So the claim "without changing `M`" is
literally false in exactly the branch it is invoked to handle (verified by hand and reproduced in
`/tmp/round-19-review/verify_pigeonhole.py`, run by this review).

**Why the Theorem nonetheless survives (independently re-derived and computationally confirmed by
this review, 4000+3000+1500 fresh `Fraction` trials + a hand-traced `(10,9,9)` example, `0`
failures across all of it, sizes up to `20`):** the ONLY place `\varepsilon'(x^*-y):=+1` is used is
to keep the merged token's assigned sign consistent with `x^*`'s **actual current sign**, which
post-flip really is `+1` (that is the literal point of doing the flip) — so the *specific numeral
choice* `+1` the proof makes for `\varepsilon'` happens to be correct regardless of whether the
prose's claimed value of `V(\varepsilon^*)` (`M` vs. `-M`) is mislabeled. The subsequent "unmerge"
contradiction argument (`\mathrm{OPT}(X')\ge M`) is *entirely magnitude-based* and never actually
needs the mislabeled signed value — it survives untouched. Net effect: **the construction (which
pair to merge, what sign to assign) is correct and produces the true `\mathrm{OPT}(X)` at every
step**, but the *prose justification* for skipping the WLOG issue is a false statement, not merely
an unstated triviality — this is a genuine rigor gap per CLAUDE.md, not a hand-wave that happens to
be fine.

**The fix (one paragraph, no new mechanism):** drop the "replace `\varepsilon^*` by `-\varepsilon^*`"
sentence entirely. Instead, let `s:=\varepsilon^*(x^*)\in\{\pm1\}` be `x^*`'s **actual** sign under
the fixed `\varepsilon^*` (no renormalization). Since `P,N` are both nonempty, some `y` has
`\varepsilon^*(y)=-s`; pick any such `y`. Set `\varepsilon'(x^*-y):=s` (not always `+1`). Then
`V(\varepsilon')=V(\varepsilon^*)` **exactly** (a direct algebraic identity, sign-agnostic — proved
by this review): writing `\mu:=V(\varepsilon^*)`, `\mu=s\cdot x^*+(-s)\cdot y+\Sigma_{\rm rest}`, so
`\Sigma_{\rm rest}=\mu-s(x^*-y)`, and `V(\varepsilon')=\Sigma_{\rm rest}+s(x^*-y)=\mu`. Hence
`|V(\varepsilon')|=|\mu|=M` unconditionally, with no case split and no WLOG needed at all. The
"unmerge" contradiction (`\mathrm{OPT}(X')\ge M`) is untouched by this fix (it never referenced the
flawed step). **Important:** the builder's own saved verification code
(`/tmp/round-19-build/explore2.py`, function `constructive_merge`) already implements exactly this
fix (`newsign = xstar_sign`, not a hardcoded `+1`) — so the 9,220+ computational trials genuinely
corroborate the CORRECTED lemma, they just don't corroborate the specific flawed WLOG sentence as
literally written in the prose (which the code silently avoids without the prose acknowledging it).

**Everything else independently re-checked and found correct:**
- **Step 1 (Pigeonhole Margin Lemma, §1):** re-derived by hand from scratch, including the
  bin-boundary case split (`b<N-2` half-open, `b=N-2` closed at `S`) — fully rigorous, no gap.
- **Sub-lemma ("same-sign forces a zero"):** re-checked, correct, no sign-convention issue (only
  flips one element's sign locally, not the WLOG global-flip issue above).
- **Case B:** correct, no issue.
- **Step 3 (Combination) and Step 4 (Conclusion, final-answer verification `c(n)=2^n/(2^{n+1}-1)`,
  `n=1,2` substitution checks):** correct, contingent only on Step 2 being fully closed.
- **Citations:** Lemma D/M, Slack Collapse, and the lower bound
  (`all-cycles-resolution.md`+`superincreasing-no-early-zero.md`) are cited and used correctly, and
  do target the same `e_m` as this proof's upper bound — no mismatch between the two directions.

**Verdict: CHANGES REQUESTED.** This is very close to a complete proof — Step 1 is fully rigorous,
Step 2's mechanism is correct and independently re-verified (both by hand and by ~10,000 fresh
trials beyond the builder's own, including sizes up to 20 and a hand-traced triggering example),
and the fix is the one-paragraph rewrite above. The gap is real (a false claim in the written
proof, not just an unstated triviality) and must be corrected on file before Status can honestly
read `solved`.

---

## Round 19 second-build addendum — the fix applied, gap closed

This pass applied the fix exactly as specified by the review above. §2 Case A (in the **Full
proof** section, above the "Provenance" divider) has been rewritten in full:

- The false sentence *"say `x^*=x_{i^*}` with `i^*\in P` (if instead `i^*\in N`, replace
  `\varepsilon^*` by `-\varepsilon^*` throughout, which swaps the labels `P\leftrightarrow N`
  without changing `M`...)"* has been **deleted**.
- In its place: `s:=\varepsilon^*_{i^*}` is defined as `x^*`'s **actual** sign under the fixed
  `\varepsilon^*` — no case split on whether `i^*\in P` or `i^*\in N`, no renormalization. Any `y`
  with `\varepsilon^*_j=-s` is picked (exists since `P,N` both nonempty), and the merged token
  `x^*-y` is assigned sign `\varepsilon'(x^*-y):=s` (inheriting `x^*`'s real sign, whatever it is).
- The identity `V(\varepsilon')=V(\varepsilon^*)=M` is now derived directly: writing
  `\Sigma_{\rm rest}` for the unchanged contribution of the other `p-2` elements,
  `M=\Sigma_{\rm rest}+s(x^*-y)` (from the definition of `M=V(\varepsilon^*)` and the signs of
  `x^*,y`), so `\Sigma_{\rm rest}=M-s(x^*-y)`, and hence
  `V(\varepsilon')=\Sigma_{\rm rest}+s(x^*-y)=M` — an identity that holds **verbatim for either
  value of `s\in\{+1,-1\}`**, with the two `s(x^*-y)` terms cancelling regardless of sign. No WLOG,
  no case split, and (critically) no claim that "`M` is unchanged by negating `\varepsilon^*`" is
  made anywhere in the corrected argument — that was the false statement, and it is now simply
  gone, not worked around.
- The "unmerge" contradiction argument immediately following (`\mathrm{OPT}(X')\ge M`) is
  **unchanged** — it was already sign-agnostic (phrased in terms of an arbitrary `\tau:=
  \varepsilon''(x^*-y)`), as the reviewer confirmed it never used the flawed claim.

**Independent re-verification this round** (`/tmp/round-19-build-2/verify_fix.py`, written from
scratch, not copied from either the original builder's `/tmp/round-19-build/` or the reviewer's
`/tmp/round-19-review/` scripts, exact `Fraction` arithmetic throughout):
- **The exact witness `X=(10,9,9)`:** true `OPT=8`; the (sign-normalized, `V\ge0`) optimal signing
  is `\varepsilon^*=(-1,+1,+1)` (the global max `10` has sign `s=-1`, exactly the branch that broke
  the old prose). The corrected construction: `x^*=10,s=-1`; opposite class is `\{9,9\}` (sign
  `+1`); merge `M(10,9)=1` with `newsign=s=-1`, giving active multiset `\{9(+1),1(-1)\}`; its true
  `OPT` is `|9-1|=8=M` (invariant holds); next step `x^*=9,s=+1`; opposite is `\{1(-1)\}`; merge
  `M(9,1)=8` with `newsign=+1`; final value `8`, matching the true optimum exactly. **PASS.** All
  `6` permutations of `(10,9,9)` also tested and pass (rules out tie-break-order artifacts).
- **Wide random sweep**, sizes `1`–`14`, exact integers `0`–`100`: `2,800` trials, `0` failures,
  `0` stuck states.
- **Tie-heavy / zero-heavy** (small alphabet `0`–`5`), sizes `2`–`11`: `1,500` trials, `0`
  failures.
- **Fractional-valued** instances, sizes `2`–`9`: `800` trials, `0` failures.
- **Any-choice-of-opposite-partner** variant (not just `\max` of the opposite class — confirming
  the proof's claim that *any* legal choice of `y` works, exactly as the corrected prose states),
  sizes `2`–`10`, `3` random repetitions each: `4,050` trials, `0` failures.
- **Grand total this round: `9,158` trials, `0` failures**, on top of the reviewer's own
  ~10,000-trial re-verification and the original builder's `9,220+` trials (which the review
  confirmed already implicitly used the corrected `newsign=s` logic in code, even though the old
  prose was wrong) — well over `28,000` combined trial-verifications of the corrected construction
  across the two rounds, `0` failures anywhere.

**Conclusion:** the gap identified by round-19 proof-review is closed. §2's Signed-Sum
Realizability Lemma is now a complete, gap-free proof (strong induction on `p`, base case `p=1`,
sub-lemma for the degenerate same-sign case, Case A now sign-agnostic and correctly derived, Case
B unchanged and already correct). Combined with the independently-confirmed-correct Step 1, Step
3, and Step 4 (none of which needed any change), the **entire theorem — both the upper bound
constructed here and the already-certified lower bound — is proved**, with the final answer
`c(n)=2^n/(2^{n+1}-1)` verified by direct substitution at `n=1,2` and by the general recursion
`e_n=e_{n-1}/(2+e_{n-1})`. Status is raised to `solved`.

---

## Round 19 (second-pass) proof-reviewer verdict — APPROVE, Status confirmed `solved`

Independently re-verified the fix above from scratch (not reusing this build's, the original
build's, or the first-pass review's own scripts): (1) re-derived the Case A merge identity
symbolically (`sympy`, `s` a free symbol, no substitution) — confirmed genuinely sign-agnostic, no
hidden case split, matches exactly; (2) wrote a fresh independent verification harness
(`/tmp/round-19-review2/fresh_verify2.py`) implementing the algorithm literally as newly written,
with an independent brute-force `\mathrm{OPT}` oracle and a per-step optimality-invariant check —
`2{,}095+` trials (the `X=(10,9,9)` witness and all `6` permutations across `5` tie-break seeds;
wide random/tie-heavy/zero-heavy/fractional/all-same-value instances; sizes up to `15`; edge
cases; multiple independent random-tie-break repetitions), **`0` failures anywhere**; (3)
confirmed the "unmerge" contradiction argument (the actual optimality-preservation mechanism) is
untouched and composes correctly with the fixed Case A — it is phrased purely in terms of an
arbitrary `\tau`, never references `s` or the old flawed claim; (4) grepped the whole file for
stale `i^*\in P`/`j\in N` references — only historical review-note sections retain them, correctly
labeled as history, no live inconsistency; (5) checked the sub-lemma's own internal "WLOG, negate
for the `N`=all case" step is a different, valid kind of move (preserves the sign-independent
magnitude `\mathrm{OPT}(X)`, not a specific signed value) — no analogous gap; (6) full end-to-end
retrace of Step 1 (re-verified fresh, `640` trials, `0` failures) through Step 4, all citations
confirmed present and correctly certified in `lemmas/`; (7) **two independent, from-scratch,
proof-machinery-free numerical validations of the final answer against the actual continuous
game**: a backward-induction game solver + grid search for `n=1` (best value found `\approx0.6667`
at opening `\approx2/3`, matching `c(1)=2/3`) and for `n=2` (at opening `(4/7,2/7,1/7)`, XY's best
searched response gives exactly `4/7`, matching `c(2)=4/7`, with nearby openings strictly worse).
**No remaining gap found.** Status confirmed `solved`. Full report:
`/tmp/round-19/proof-reviewer-2.md`. The Signed-Sum Realizability Lemma is certified into
`lemmas/signed-sum-realizability.md`. `current.md` updated with `## Status: solved` and the
complete `## Full proof`.
