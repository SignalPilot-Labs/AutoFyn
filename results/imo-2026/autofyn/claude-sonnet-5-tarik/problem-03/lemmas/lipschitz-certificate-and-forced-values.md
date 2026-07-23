# 1-Lipschitz weak-duality lemma, Cascade Reachability, and Forced-Value Lemmas A/B

**Certified by:** proof-reviewer, round 5, from approach `concavity-minimax-duality`
(round-5 builder, §10 Step 1 and §11). Independently re-verified by the reviewer, both
symbolically (re-derivation of each proof) and computationally (exact `Fraction`
recomputation of the cascade identity for `j=1..6`, the odd/even telescoping failure of
`g=min(t,1)` for `m=1..6`, and the reachability of the `(4,2,1/2,1/2)` witness for `m=2..6`
— see Verification below).

**Depends on:** the certified `lemmas/dm-operation-reformulation.md` (Lemma D/M) and the
elementary alternating-sum definition of `e`.

## Statement

**Lemma (1-Lipschitz weak duality).** For any sorted descending multiset
`x_1\ge x_2\ge\dots\ge x_K\ge0` and any 1-Lipschitz `g:[0,\infty)\to\mathbb R` with `g(0)=0`,
```
e(M):=\sum_{i=1}^K(-1)^{i+1}x_i \;\ge\; \sum_{i=1}^K(-1)^{i+1}g(x_i)=:e_g(M),
```
with equality when `g=\mathrm{id}`.

**Lemma (cascade reachability).** For every integer `j\ge1`, the single D/M operation
`M(2^j,2^{j-1})` applied to `D_j=(2^j,2^{j-1},\dots,2,1)` yields exactly `D_{j-1}` (as a
multiset). Consequently `D_j` reduces to the singleton `\{1\}=D_0` using exactly `j`
operations, and to `D_i` using exactly `j-i` operations, for every `0\le i\le j`.

**Lemma A (`g(1)=1` forced).** For every `m\ge1` and any 1-Lipschitz `g` with `g(0)=0`
satisfying `e_g(M)\ge1` on every D/M-reachable state `M` from `D_m` within `\le m`
operations, `g(1)=1` exactly.

**Lemma B (`g(2)=2` forced).** Under the same hypotheses, for every `m\ge2`, `g(2)=2` exactly.

## Proof

**Weak duality.** Pad with `x_{K+1}:=0` if `K` odd (`g(0)=0` contributes nothing to either
side). Pair consecutive terms: `x_{2i-1}-x_{2i}=|x_{2i-1}-x_{2i}|\ge|g(x_{2i-1})-g(x_{2i})|`
(1-Lipschitz) `\ge g(x_{2i-1})-g(x_{2i})`. Summing over all pairs gives `e(M)\ge e_g(M)`. For
`g=\mathrm{id}` both sides are identical termwise.

**Cascade reachability.** `M(2^j,2^{j-1})` removes one copy each of `2^j,2^{j-1}` and inserts
`2^j-2^{j-1}=2^{j-1}`; the untouched elements are `2^{j-2},\dots,2,1` (empty if `j\le2`, check
directly: `j=1`: `M(2,1)\to1=D_0`; `j=2`: `M(4,2)\to2`, untouched `\{1\}`, giving `D_1`). So
the result is `\{2^{j-1}\}\cup\{2^{j-2},\dots,1\}=D_{j-1}` exactly. The Corollary follows by
induction on `j`, applying the single-step identity repeatedly.

**Lemma A.** By cascade reachability (`i=0,j=m`), `\{1\}` is reachable from `D_m` within `m`
operations. Applying the hypothesis at `M=\{1\}`: `g(1)\ge1`. By 1-Lipschitz + `g(0)=0`:
`|g(1)|\le1`, so `g(1)\le1`. Hence `g(1)=1`.

**Lemma B.** By cascade reachability (`i=1,j=m`), `D_1=(2,1)` is reachable from `D_m` within
`m-1\le m` operations. Applying the hypothesis: `g(2)-g(1)\ge1`; by Lemma A, `g(1)=1`, so
`g(2)\ge2`. By 1-Lipschitz: `g(2)\le g(1)+|2-1|=2`. Hence `g(2)=2`. `\blacksquare`

## Verification

Independently re-derived step-by-step (all four proofs re-checked for logical validity, no
gap found). Independently re-verified computationally:
- Cascade identity `M(2^j,2^{j-1})` on `D_j\to D_{j-1}`: confirmed exactly for `j=1,\dots,6`
  (integer arithmetic, exact match every time).
- Full cascade `D_j\to\{1\}` in exactly `j` operations: confirmed for `j=1,\dots,6`.
- The clip `g(t)=\min(t,1)` gives `e_g(D_m)=0` exactly whenever `m` is odd (and `1` when `m`
  is even): confirmed exactly for `m=1,\dots,6` via direct computation, matching the
  consequence drawn from Lemmas A/B's forced values.
- The witness state `(4,2,\tfrac12,\tfrac12)` is reachable from `D_m` within `m-1\le m`
  operations for every `m=2,\dots,6` (cascade to `D_2=(4,2,1)` then bisect the trailing `1`):
  confirmed exactly by direct construction for each `m` tested.

## Reusable by

Any approach searching for a 1-Lipschitz "certificate function" `g` giving a lower bound on
`e` without per-step monovariance or location-based casework. The Forced-Value Lemmas A/B
rule out, in one proof, every candidate `g` that compresses information at or below `2`
(e.g. `\min(t,1)`, `\min(t,2)`, both refuted using these lemmas in `concavity-minimax-duality`
§11.4–11.5) — reusable as a fast screening test for any future candidate `g_m` proposed for
this or a similar weak-duality certificate search. **Scope note:** no working general-`m`
certificate `g_m` has been found; these lemmas are necessary-condition/screening tools, not a
constructive existence result.
