# Signed-Sum Realizability Lemma

**Certified by:** proof-reviewer, round 19 (second pass), from approach
`pigeonhole-subset-sum-upper-bound` (round 19, second build — Case A fix). Independently
re-derived and re-verified by the reviewer, both symbolically (the Case A merge identity
re-derived from scratch with `sympy`, confirmed sign-agnostic with no hidden case split) and
computationally (a fresh, from-scratch harness, `2{,}095+` exact-`Fraction` trials across the
`X=(10,9,9)` witness that broke an earlier draft of the proof, wide random/tie-heavy/zero-heavy/
fractional/all-same-value instances, larger sizes, and an explicit per-step optimality-invariant
check — `0` failures, `0` invariant violations, `0` "stuck" states anywhere).

**Depends on:** `lemmas/dm-operation-reformulation.md` (Lemma D/M — only the definition of the
`M`-operation, `x\ge y\mapsto x-y`, is used; no other property).

## Statement

For every finite multiset `X` of nonnegative reals with `|X|=p\ge1`, define, for a signing
`\varepsilon:X\to\{+1,-1\}`, `V(\varepsilon):=\sum_{x\in X}\varepsilon(x)x` and
`\mathrm{OPT}(X):=\min_\varepsilon|V(\varepsilon)|`. Then there is a sequence of `p-1`
`M`-operations (each combining two currently-active values `x\ge y` into `x-y`; unrestricted
choice of which pair to merge at each step) reducing `X` to a single surviving value equal to
`\mathrm{OPT}(X)` exactly.

## Proof

Strong induction on `p`.

**Base case `p=1`.** `X=\{x_1\}`; the only signings give `\pm x_1`, so `\mathrm{OPT}(X)=x_1`. Zero
operations needed.

**Inductive step, `p\ge2`.** Fix any signing `\varepsilon^*` achieving `M:=\mathrm{OPT}(X)`
(exists — finitely many signings). Replacing `\varepsilon^*` by `-\varepsilon^*` if necessary
(which preserves `|V(\varepsilon^*)|`, a magnitude — a trivial, always-valid fact, independent of
any case split on which elements carry which sign), assume `V(\varepsilon^*)=M\ge0`. Let
`P:=\{i:\varepsilon^*_i=+1\}`, `N:=\{i:\varepsilon^*_i=-1\}`.

**Sub-lemma (same-sign forces a zero).** *If `P=\{1,\dots,p\}` or `N=\{1,\dots,p\}` (`p\ge2`),
then `\min_ix_i=0`.*

*Proof.* WLOG `P`=all (the `N`=all case is identical after negating `\varepsilon^*`, a legitimate
step here because it only uses that negation preserves the *magnitude* `\mathrm{OPT}(X)`, a
sign-independent quantity — not any specific signed value tied to element membership). Then
`M=\sum_ix_i`. Let `q:=\min_ix_i\ge0`; since the `p\ge2` nonnegative values sum to `M`, `q\le M/2`.
If `M=0`: all `x_i\ge0` summing to `0` forces every `x_i=0`, so `q=0`. If `M>0` and (for
contradiction) `q>0`: flipping the sign of the minimal element gives a new signing of value
`M-2q\in[0,M)`, strictly smaller magnitude than `\mathrm{OPT}(X)` — contradiction. Hence `q=0`.
`\blacksquare`

**Case A: `P,N` both nonempty.** Let `x^*=x_{i^*}` be a global maximum of `X` (ties broken
arbitrarily); let `s:=\varepsilon^*_{i^*}\in\{+1,-1\}` be its **actual** current sign under
`\varepsilon^*` — no normalization or case split on whether `i^*\in P` or `i^*\in N`. Since `P,N`
are both nonempty, pick any `y=x_j` with `\varepsilon^*_j=-s`. Since `x^*` is a global maximum,
`x^*\ge y`, so `M(x^*,y)=x^*-y\ge0` is a legal `M`-operation. Let
`X':=(X\setminus\{x^*,y\})\cup\{x^*-y\}` (`|X'|=p-1`), and define `\varepsilon'` on `X'`: equal to
`\varepsilon^*` on `X\setminus\{x^*,y\}`, and `\varepsilon'(x^*-y):=s`.

*Claim: `V(\varepsilon')=V(\varepsilon^*)=M`, for either value of `s`, no case split.* Writing
`\Sigma_{\rm rest}` for the (unchanged) contribution of the other `p-2` elements: since
`\varepsilon^*_{i^*}=s,\varepsilon^*_j=-s`,
```
M = V(\varepsilon^*) = \Sigma_{\rm rest} + s\cdot x^* + (-s)\cdot y = \Sigma_{\rm rest} + s(x^*-y),
```
so `\Sigma_{\rm rest}=M-s(x^*-y)`, hence `V(\varepsilon')=\Sigma_{\rm rest}+s(x^*-y)=M` — this is
pure algebra in the free variable `s\in\{\pm1\}`, holding identically for either value, with no
case split needed at any point.

*Claim: `\mathrm{OPT}(X')=M`.* Suppose some `\varepsilon''` on `X'` has `|V(\varepsilon'')|=M'<M`.
Let `\tau:=\varepsilon''(x^*-y)`. Define `\varepsilon'''` on `X`: equal to `\varepsilon''` on
`X\setminus\{x^*,y\}=X'\setminus\{x^*-y\}`, and `\varepsilon'''(x^*):=\tau,
\varepsilon'''(y):=-\tau`. Then the contribution of `x^*,y` under `\varepsilon'''` is
`\tau x^*+(-\tau)y=\tau(x^*-y)`, exactly the merged element's contribution under `\varepsilon''`,
so `V(\varepsilon''')=V(\varepsilon'')=\pm M'`, giving `X` a signing of magnitude `M'<M
=\mathrm{OPT}(X)` — contradiction.

By the induction hypothesis on `X'` (size `p-1<p`), `p-2` operations realize `\mathrm{OPT}(X')=M`;
prepending `M(x^*,y)` gives `p-1` operations on `X` realizing `M`.

**Case B: `P=\emptyset` or `N=\emptyset`.** By the sub-lemma, some `x_{j_0}=0`. Since `p\ge2`, pick
any `k_0\ne j_0` and merge `M(x_{k_0},0)=x_{k_0}` (legal). This gives
`X'=X\setminus\{x_{j_0}\}` (`|X'|=p-1`); the restriction `\varepsilon'` of `\varepsilon^*` to `X'`
still has value `M` (the deleted zero contributed `0` under either sign). `\varepsilon'` is
optimal for `X'`: if some `\varepsilon''` on `X'` had value `M'<M`, extending it to `X` by
assigning the deleted zero any sign (contributing `0` regardless) gives `X` a signing of value
`M'<M`, contradicting `M=\mathrm{OPT}(X)`. By the induction hypothesis, `p-2` further operations
realize `M`; prepending `M(x_{k_0},0)` gives `p-1` operations on `X` realizing `M`.

Cases A and B are exhaustive (`P,N` are either both nonempty or one is empty; both empty is
impossible for `p\ge2`), completing the induction. `\blacksquare`

## Verification

Independent, from-scratch computational corroboration by the round-19 (second-pass) reviewer,
`/tmp/round-19-review2/fresh_verify2.py` (not reusing any prior builder's or reviewer's script):
- `2{,}095+` fresh exact-`Fraction` trials, `0` failures, `0` per-step optimality-invariant
  violations, `0` "stuck" states, across: the exact witness `X=(10,9,9)` (the specific instance
  where the global max carries sign `s=-1`, the branch a prior draft of the proof mishandled) and
  all `6` of its permutations across `5` random tie-break seeds each; wide random integer sweeps
  (sizes `1`-`13`); tie-heavy small-alphabet instances; zero-heavy instances; fractional-valued
  instances; all-same-value instances (stress-testing the same-sign sub-lemma branch); explicit
  edge cases (`p=1`, all-zero, tied pairs); sizes `14`-`15` beyond the originally tested range; and
  `3` independent random-tie-break repetitions per instance (confirming the theorem's "unrestricted
  choice of which pair to merge" claim, not merely a specific tie-break policy).
- The Case A merge identity `V(\varepsilon')=V(\varepsilon^*)=M` was additionally re-derived
  symbolically from scratch (`sympy`, `s` kept as a free symbol, not substituted), confirming it
  holds identically for both signs with no hidden case split.

## Reusable by

Any approach needing to realize an extremal signed subset sum (`\mathrm{OPT}(X):=\min_\varepsilon
|V(\varepsilon)|`) via a legal difference-only merge sequence (Lemma D/M's `M`-operation). Depends
only on elementary real-number inequalities and the `M`-operation's definition — no dependence on
superincreasing-ness, dyadic structure, or any property of a specific base sequence. Used in
`pigeonhole-subset-sum-upper-bound.md` §3 (combined with the Pigeonhole Margin Lemma) to close the
entire upper-bound direction of `imo-2026-03`.
