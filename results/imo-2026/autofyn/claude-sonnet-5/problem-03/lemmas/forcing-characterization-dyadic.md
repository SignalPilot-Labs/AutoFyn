# Localization, Top-Two-Residual-Cancel, and Successor Lemmas; the Combined forced/unforced
Theorem for the 1-Lipschitz certificate method on the dyadic family

**Certified by:** proof-reviewer, round 7, from approach `concavity-minimax-duality` (round-7
builder, §12.1-12.4). Independently re-derived (all four proofs re-checked step-by-step) and
independently re-verified computationally (exact `fractions.Fraction` construction of the exact
operation sequences claimed, `k=2..8` for Top-Two-Residual-Cancel, `j=0..8` for Successor) by
the reviewer.

**Depends on:** the certified `lemmas/dm-operation-reformulation.md` (Lemma D/M) and
`lemmas/lipschitz-certificate-and-forced-values.md` (1-Lipschitz weak duality, Cascade
Reachability, Forced-Value Lemmas A/B, whose hypotheses this file's Combined Theorem reuses
verbatim).

## Statement

**Localization Lemma.** Let `M=A\sqcup B` be a disjoint union of (multi)sets of positive reals.
If a legal sequence of D/M operations, applied to `A` alone, transforms `A` into `A'`, and every
value appearing at any intermediate step of that sequence is distinct from every value in `B`,
then the same sequence of operations applied to `M` transforms it into `A'\sqcup B`, using the
same number of operations, leaving `B` completely untouched throughout.

**Top-Two-Residual-Cancel Lemma.** For every integer `k\ge1` and every `m\ge k`, the state
`(2^k,2^{k-1},\tfrac12,\tfrac12)` is reachable from `D_m` within exactly `m-1` D/M-operations.

**Successor (Consecutive-Pair) Lemma.** For every integer `j\ge0` and every `m\ge j+1`, the
state `(2^j+1,2^j)` is reachable from `D_m` within exactly `m-1` D/M-operations.

**Combined Theorem.** For every `k\ge0`, any 1-Lipschitz certificate `g` (`g(0)=0`, `e_g(M)\ge1`
on every state reachable from `D_m` within `\le m` operations, for every `m`) satisfies
```
k+1 \le g(2^k) \le 2^k,
```
both bounds tight, with equality (hence `g(2^k)` forced to a single value) **iff `k\in\{0,1\}`**
(the gap `2^k-(k+1)` is `\ge1` for `k\ge2` and strictly increasing, `\to\infty`). Moreover, for
every `j\ge0`, `g(2^j+1)=g(2^j)+1` exactly, so `g(2^j+1)` is forced iff `g(2^j)` is — giving
`g(3)=3` forced (`j=1`) but `g(5),g(9),g(17),\dots` (`j\ge2`) provably **not** forced, with the
identical (unboundedly growing) slack as `g(4),g(8),g(16),\dots`.

## Proof

**Localization:** immediate from the definitions of `D(x)`/`M(x,y)`, both of which act only on
the referenced value(s) and leave every other element unchanged; if the referenced value(s) are
always drawn from the (distinct-from-`B`) evolving part `A`, running the sequence on `M`
proceeds identically with `B` along for the ride. Induction on sequence length.

**Top-Two-Residual-Cancel:** for `k=1`, `D_1=(2,1)` reachable in `m-1` ops directly (Cascade
Reachability). For `k\ge2`: reach `D_k` in `m-k` ops (Cascade Reachability); split `D_k` into
`A:=D_{k-2}=\{2^{k-2},\dots,1\}` and `B:=\{2^k,2^{k-1}\}`; every value appearing while cascading
`A` to `\{1\}` (`k-2` ops) is `\le2^{k-2}<2^{k-1}=\min B`, so Localization applies, giving
`\{1\}\sqcup B`; one further `D(1)` (value `1`, distinct from `B`) gives
`(2^k,2^{k-1},\tfrac12,\tfrac12)`. Total: `(m-k)+(k-2)+1=m-1`.

**Successor:** for `j=0`, `D_1=(2,1)` is already the target, in `m-1` ops. For `j\ge1`: reach
`D_{j+1}` in `m-(j+1)` ops; set `A:=D_{j-1}=\{2^{j-1},\dots,1\}`, `B:=\{2^j\}`; successively
subtract each element of `A` (largest first) from the evolving top value starting at `2^{j+1}`;
the running top stays `>2^j+1>2^j=\min B$ throughout (partial sums of `A`'s geometric total
`2^j-1` are all proper prefixes), so Localization applies; after all `j` subtractions the top is
`2^{j+1}-(2^j-1)=2^j+1`. Total: `(m-(j+1))+j=m-1`. Final state `(2^j+1,2^j)`.

**Combined Theorem, lower bound:** induction on `k`. Base `k=0`: Lemma A (`g(1)=1`). Step: given
`g(2^{k-1})\ge k`, the Top-Two-Residual-Cancel witness (within budget, since it uses `\le m`
ops) forces `e_g\ge1` on `(2^k,2^{k-1},\tfrac12,\tfrac12)`; the trailing equal pair contributes
`0` to `e_g` regardless of `g` (adjacent equal values cancel in any alternating sum), reducing to
`g(2^k)-g(2^{k-1})\ge1`, hence `g(2^k)\ge k+1`.
**Upper bound:** `g(2^k)=|g(2^k)-g(0)|\le2^k` directly from 1-Lipschitz, `g(0)=0`.
**Equality iff `k\in\{0,1\}`:** direct check at `k=0,1`; for `k\ge2`, `2^k\ge k+2` by induction
(base `k=2`: `4=2+2`; step: `2^{k+1}=2\cdot2^k\ge2(k+2)\ge(k+1)+2` since `k\ge2`), so the gap is
`\ge1` and strictly increasing (`\text{gap}(k+1)-\text{gap}(k)=2^k-1\ge3` for `k\ge2`).
**Successor equality:** the Successor witness forces `g(2^j+1)-g(2^j)\ge1`; 1-Lipschitz gives
`\le1`; hence `=1` exactly, an equation propagating forced/unforced status identically between
`g(2^j)` and `g(2^j+1)`.

## Verification

- Top-Two-Residual-Cancel: independently reconstructed the exact operation sequence (cascade to
  `D_k`, then cascade `D_{k-2}` to `\{1\}`, then bisect) in exact `Fraction` arithmetic for
  `k=2,\dots,8` (`m=k` in each case) — operation count `m-1` and final state
  `(2^k,2^{k-1},\tfrac12,\tfrac12)` matched exactly in all 7 cases.
- Successor: independently reconstructed (cascade to `D_{j+1}`, then successive subtraction) for
  `j=0,\dots,8` (`m=j+1`) — operation count `m-1` and final state `(2^j+1,2^j)` matched exactly
  in all 9 cases.
- Combined Theorem's arithmetic (induction bases/steps, gap monotonicity) re-derived directly,
  no gap found.
- Cross-validated (not independently re-run at full scale by the reviewer, given time budget,
  but spot-checked for `m\le4`, zero violations of the g* candidate discussed below) against the
  builder's own exhaustive finite LP over all states reachable from `D_m`, `m=1,\dots,5`
  (`19191` states): LP-computed ranges for `g(4),g(8),g(16)` match `[3,4],[4,8],[5,16]` exactly.

## Reusable by

Any approach pursuing a 1-Lipschitz certificate for the lower-bound direction. **Scope note:**
this theorem shows the *forcing* technique (pin `g` to a unique value via local reachability
witnesses plus the Lipschitz bound) is exhausted beyond `j=3` among the dyadic powers/successors
— it does **not** show no valid nontrivial certificate exists; it precisely locates where slack
remains, which the same round's candidate `g^*` (piecewise, matching the minimal forced value at
each `2^k`) is built to exploit. `g^*` has survived exhaustive (not sampled) testing through
`m=6` (`326265` states, zero violations) but is **explicitly not proved** for general `m` — do
not cite it as established.
