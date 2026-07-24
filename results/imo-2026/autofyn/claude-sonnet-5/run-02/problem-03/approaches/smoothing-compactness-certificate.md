## Status
partial

## Approaches tried
- (Round 1, first pass) Outline only: static optimization / smoothing-perturbation framing (Steps 1–6), Step 3 (the local-exchange smoothing lemma toward 2:1 ratios) flagged as entirely open with no derived mechanism.
- (Round 1, this pass — feasibility probe requested by the outline-reviewer) Attempted the n=2 local-optimality computation by hand/CAS (`sympy`/`scipy`/exact `Fraction` arithmetic). **Outcome: the literal "continuous local perturbation / directional derivative" smoothing lemma is NOT the right mechanism, but a closely related and fully rigorous mechanism — domination by a small finite family of explicit Xiang Yu "template" strategies, combined with a linear-programming-style contradiction argument over Liu Bang's configuration simplex — DOES work for n=2 and gives a complete, non-numeric proof of the upper bound `c(2) ≤ 4/7`.** This is a genuine, derived mechanism (not numerical evidence used as a proof step); numerics were used only to *discover* which finite strategies to use, and the final argument is checked by hand algebra. Details below. The matching lower bound (ladder guarantees `≥4/7`) is also established for 7 of the 10 relevant Xiang-Yu cut-distribution cases by exact case analysis; the remaining 3 mixed cases are confirmed only by fine numerical search (no exact proof yet) — see Open gap.
- (Round 2 — this pass, dispatched task) **Closed all 3 remaining `n=2` lower-bound compositions `(1,1,0)`, `(1,0,1)`, `(0,1,1)` exactly and symbolically**, by the same "insert the fixed pieces into the sorted order, case-split on the free cut parameter's range, sum the odd ranks" method that closed the other 7/10 cases — no numerics anywhere in the final argument (numerics were used only as an a-priori spot check of the closed forms derived, reported below, matching the derived infima to 4 decimal places). **`c(2) = 4/7` is now a fully rigorous, non-numeric, complete result** (both directions, all 10 lower-bound cut-distribution cases, plus the previously-completed upper bound and degenerate-configuration cases). Also produced the general-`n` template/region sketch requested as a stretch goal (Status remains `partial` for the overall problem since general `n` is not closed, but the round's assigned task — full symbolic closure of `n=2` — is complete).
- (Round 4 — this pass, dispatched task: generalize the template+LP-contradiction mechanism to `n=3`, taking into account the outline-reviewer's correction that the "cascading-halving hits the target at every prefix length `k`" claim is false in general). **Two results, one positive and general, one negative and diagnostic:**
  1. **Positive (new, general-`n`, fully proved — not just numerically checked):** proved in closed form, for *every* `n`, that the two boundary cascading-halving responses (cutting the top `k=n-1` or `k=n` pieces of the ladder, each into two copies of the next rung) give `Φ = a_n = 2^n/(2^{n+1}-1)` **exactly**, via a direct rank-position count (no case-by-case induction or numerics needed) — turning the round-4 explorer's numerically-verified-for-`n≤6` finding (and the outline-reviewer's correction narrowing it to `k∈{n-1,n}`) into an actual theorem for all `n`. See "General-`n` cascade achievability theorem" below; certified as a promotable lemma.
  2. **Negative/diagnostic (honest gap, `n=3` upper-bound generalization attempt):** attempted to extend this approach's own `n=2` mechanism (a small finite family of template strategies + LP-contradiction over Liu Bang's configuration simplex) to `n=3`, using the direct analogs of `n=2`'s six templates (bisect-prefix `T1,T2,T3` generalizing `A,C`; bisect-suffix `D1,D2,D3` generalizing `D,E`). **Found and verified by exact `Fraction` arithmetic (no floating point) a concrete `n=3` configuration where this 6-template family fails**: at `(p,q,r,s)=(3/8,1/4,1/4,1/8)`, all six templates give `Φ=9/16` or `11/16`, both `>` the target `8/15`, which would (falsely) suggest the upper bound fails there. The true minimum at that point is only `1/2 < 8/15` (no actual violation), achieved by a strategy outside the 6-template family — splitting `p` into three parts tied to `s` — but this patch is **not a universal fix**: a broader numerical search (`scipy.optimize`, `differential_evolution`-style multi-start) over compositions that only touch the single largest piece `p` shows the optimal split is **not** a fixed closed-form rule (e.g. "equal thirds") but a genuine per-configuration LP-vertex optimization, tying `p`'s fragments to whichever of `q,r,s` the local geometry demands — i.e. the same "vertex enumeration does not collapse to a short list" obstruction the round-4 superincreasing explorer found on the *lower-bound* side now appears to afflict this approach's *upper-bound* mechanism too, and worse than hoped: even a single-composition sub-family (touch only `p`) needs configuration-dependent case analysis rather than a handful of closed forms. **Status of the upper-bound generalization: genuinely open at `n=3`, more so than the round-3 sketch anticipated.** Full computational trail in `/tmp/round-4/n3_*.py` and `verify_counterexample.py`.

## Current best

**Setup (shared with `greedy-halving-adversary`; imported, not re-derived here).**
By the claiming-subgame reduction lemma (any fixed final multiset of pieces is
claimed greedy-largest-first by both players, since deviating from "take the
current max" is a weakly dominated swap — payoffs are additive over the
remaining multiset with no cross-terms), Liu Bang's guaranteed total for a
fixed final multiset is `Φ(M) = ` sum of the odd-sorted-rank entries of `M`
(1st, 3rd, 5th, … largest). So
`c(n) = max_{L} min_{X refines L} Φ(X)`,
where `L` ranges over Liu Bang's `≤n`-point cuts (`≤(n+1)` pieces) and `X`
ranges over Xiang Yu's `≤n` further cuts.

### n = 2: a complete, rigorous mechanism for the upper bound `c(2) ≤ 4/7`

Write a general Liu Bang 3-piece configuration as `(p,q,r)` with
`p ≥ q ≥ r > 0`, `p+q+r=1` (the case of `<2` Liu Bang points is handled
separately, see below). We exhibit **six explicit, always-or-conditionally
available Xiang Yu strategies**, each using at most 2 cuts, and prove by
direct algebra (not search) that Liu Bang can never force `Φ` above `4/7`
against the best of them.

**The six strategies and their exact values** (each verified by a short,
fully exhaustive case check on how the produced pieces interleave in sorted
order — the check is genuinely case-exhaustive, not "clearly"):

- **A — bisect the largest piece only** (1 cut: split `p` into `p/2,p/2`,
  leave `q,r`). Resulting 4-piece multiset `{p/2,p/2,q,r}`. Exhaustive
  3-case check on where `r` falls relative to `p/2` (`m := p/2`): if `m≥q`
  sorted order is `m,m,q,r`; if `r≤m<q` it is `q,m,m,r`; if `m<r` it is
  `q,r,m,m`. In all three cases the sum of ranks 1 and 3 equals `m+q`.
  **`Φ_A = p/2 + q`, valid for every `p≥q≥r>0`.**

- **C — bisect the two largest pieces** (2 cuts: split `p→p/2,p/2` and
  `q→q/2,q/2`, leave `r`). Resulting 5-piece multiset
  `{p/2,p/2,q/2,q/2,r}`. Since `p/2≥q/2` always, only `r`'s position varies;
  a 3-case check (`r≥p/2`; `q/2≤r<p/2`; `r<q/2`) gives, in every case,
  ranks 1,3,5 summing to `p/2+q/2+r`. **`Φ_C = 1/2 + r/2`
  (using `p+q=1-r`), valid for every `p≥q≥r>0`.**

- **D — bisect the smallest piece only** (1 cut: split `r→r/2,r/2`, leave
  `p,q`). Since `r/2 ≤ r ≤ q ≤ p` always, the sorted order is forced —
  `p,q,r/2,r/2` — with no case split needed. **`Φ_D = p + r/2`, valid for
  every `p≥q≥r>0`.**

- **E — bisect the two smallest pieces** (2 cuts: split `q→q/2,q/2` and
  `r→r/2,r/2`, leave `p`). Order is forced: `p,q/2,q/2,r/2,r/2` (since
  `p` is largest and `q/2≥r/2`). **`Φ_E = 1/2 + p/2`, valid for every
  `p≥q≥r>0`.**

- **B — "capture q and r"** (2 cuts, both inside `p`: split `p` into three
  parts `x>q>y>r>z≥0`). When feasible, all three of `x,y,z` land on the odd
  ranks (`q,r` land on the even ranks 2,4), so **`Φ_B = p`.** Feasibility:
  need `y∈[r,q], z∈[0,r], x=p-y-z≥q`; taking the extremal choice
  `y=r,z=0` shows the binding requirement is `p-r ≥ q`, i.e.
  **`p ≥ q+r = 1-p`, i.e. `p ≥ 1/2`.**

- **G — "capture p entirely"** (2 cuts, one inside `p` one inside `r`:
  split `p→p_1,p_2` and `r→r_1,r_2`, leave `q`, arranged
  `q ≥ p_1 ≥ r_1 ≥ p_2 ≥ r_2`). When feasible, `p_1,p_2` land on the even
  ranks (2,4) and `q,r_1,r_2` on the odd ranks, so **`Φ_G = q+r = 1-p`.**
  Setting `r_2=0` (extremal), feasibility reduces to
  `max(r,\,p-r) ≤ q`, which resolves to **feasible whenever `p≤1/2`, or
  whenever `p<2r`** (a short two-case check: if `p≥2r` the condition is
  `p-r≤q ⟺ p≤q+r=1-p ⟺ p≤1/2`; if `p<2r` the condition `r≤q` holds
  automatically).

**The LP-style contradiction argument.** Split the simplex
`{p≥q≥r>0,\ p+q+r=1}` into two regions.

*Region 1: `p ≥ 1/2`* (so `B` is available). Suppose, for contradiction,
that `Φ_A>4/7`, `Φ_B>4/7`, and `Φ_C>4/7` simultaneously. Then:
`Φ_B>4/7 ⟹ p>4/7`; `Φ_A>4/7 ⟹ q>4/7-p/2`; `Φ_C>4/7 ⟹ r>1/7`. Summing,
`1 = p+q+r > p+(4/7-p/2)+1/7 = p/2+5/7`, so `p<2(1-5/7)=4/7` — contradicting
`p>4/7`. Hence `min(Φ_A,Φ_B,Φ_C) ≤ 4/7` throughout Region 1, so
`min_X Φ(p,q,r) ≤ 4/7` there. (Equality is attained only where all three are
simultaneously `=4/7`: solving `p/2+q=p=1/2+r/2=4/7` with `p+q+r=1` gives
exactly `(p,q,r)=(4/7,2/7,1/7)`, the ladder.)

*Region 2: `p ≤ 1/2`* (so `G` is available, since `p≤1/2` is one of `G`'s
two sufficient conditions). Suppose `Φ_A>4/7`, `Φ_D>4/7`, and `Φ_G>4/7`
simultaneously. Then: `Φ_G>4/7 ⟹ p<3/7`; `Φ_A>4/7 ⟹ q>4/7-p/2`;
`Φ_D>4/7 ⟹ r>8/7-2p`. Summing `q+r` bounds:
`1-p = q+r > (4/7-p/2)+(8/7-2p) = 12/7-5p/2`, so `p > 10/21`. But
`10/21 > 3/7` (since `10/21=0.476>0.4286=3/7`), contradicting `p<3/7`.
Hence `min(Φ_A,Φ_D,Φ_G) ≤ 4/7` throughout Region 2 (in fact a finer LP
computation shows the true regional maximum is `5/9 ≈0.556<4/7`, so this
region is not even close to binding).

**Degenerate configurations (Liu Bang uses `<2` points).**
- *1 point (2 pieces `a,1-a`, `a≥1/2`)*: Xiang Yu bisects **both** pieces
  (his full 2-cut budget): result `{a/2,a/2,(1-a)/2,(1-a)/2}`. Since
  `a≥1-a`, sorted order is forced (`a/2,a/2,(1-a)/2,(1-a)/2`), giving
  `Φ = a/2+(1-a)/2 = 1/2` **exactly, for every `a`.** Since `1/2<4/7`, using
  only 1 point is strictly dominated.
- *0 points (1 piece, the whole stick)*: Xiang Yu splits it into 3 parts
  `x≥y≥z>0` (his full budget); Liu's value is `x+z=1-y`. For any `ε>0`,
  taking `x=1/2,\ y=1/2-ε,\ z=ε` (valid for `ε≤1/4`) gives
  `Φ=1/2+ε`, so `Φ` can be pushed arbitrarily close to `1/2` from above;
  in particular `Φ<4/7` is achievable (e.g. `ε<1/14`). So 0 points is also
  strictly dominated.

**Conclusion of the upper bound.** Combining Region 1, Region 2, and the two
degenerate cases: for every legal Liu Bang configuration (0, 1, or 2 marked
points), Xiang Yu has an explicit response with `Φ ≤ 4/7`. Hence
**`c(2) ≤ 4/7`, proved with no numerics in the final argument** (numerics
were used only to discover the six strategies and the region split).

### n = 2: the matching lower bound `c(2) ≥ 4/7`

The ladder `(p,q,r)=(4/7,2/7,1/7)` (equivalently marked points at
`4/7` and `6/7` of the stick) needs: **every** Xiang Yu response (≤2 further
cuts) gives `Φ ≥ 4/7`. Working in units of `1/7` (so `P=4,Q=2,R=1`, target
`Φ≥4`), Xiang Yu's move is classified by which of `P,Q,R` receive his ≤2
cuts — 10 compositions `(k_P,k_Q,k_R)` with `k_P+k_Q+k_R≤2`. Exact proof for
7 of the 10:

- `(0,0,0)`: `Φ=4+1=5≥4`. ✓
- `(1,0,0)` (`P→p_1≥p_2`, `p_1+p_2=4`, so `p_1≥2`): a 2-case check on
  `p_2 ≥1` vs `p_2<1` gives `Φ=p_1+p_2=4` in the first case and `Φ=p_1+1>4`
  in the second (using `p_1>3` there). **`Φ≥4` always, equality possible.**
- `(0,1,0)` (`Q→q_1,q_2`): `P=4` is always rank 1 (all other 4 values
  `<4`); `Φ=4+`(median of `{q_1,q_2,1}`) `>4`. ✓
- `(0,0,1)` (`R→r_1,r_2`): `P,Q` are ranks 1,2; `Φ=4+2+\max(r_1,r_2)... `
  more precisely `Φ=4+\max(r_1,r_2)≥4+1/2>4`. ✓
- `(2,0,0)` (`P→x≥y≥z`, `x+y+z=4`, `Q=2,R=1` fixed): full case-exhaustive
  analysis on how many of `x,y,z` exceed `2`, lie in `(1,2]`, or are `≤1`
  (the only arithmetically feasible interleaving patterns, given
  `x+y+z=4`, are `(A,B,C)∈\{(1,1,1),(1,0,2),(0,3,0),(0,2,1)\}` where
  `A,B,C` count elements in each range — all other combinations are ruled
  out by direct sum bounds, e.g. `(3,0,0)` would force sum `>6`): computing
  `Φ` in each of the 4 cases gives `Φ=4` (case `(1,1,1)`, exactly),
  `Φ=5-\max(y,z)≥4` (case `(1,0,2)`), `Φ=3+y>4` (case `(0,3,0)`, using
  `y>1`), and `Φ=6-x≥4` (case `(0,2,1)`, using `x≤2`). **`Φ≥4` in every
  case, with equality exactly in case `(1,1,1)`.**
- `(0,2,0)` (`Q→q_1,q_2,q_3`): `P=4` is rank 1 (all `q_i<2<4`); the
  remaining 4 values `{q_1,q_2,q_3,1}` occupy ranks 2–5, contributing
  `\Phi = 4 + (\text{their local rank }2) + (\text{local rank }4) > 4`
  trivially since both added terms are positive. ✓
- `(0,0,2)` (`R→r_1,r_2,r_3`): similarly `P=4,Q=2` are ranks 1,2, and
  `Φ=4+2+(\text{local rank }1)+(\text{local rank }3)>4+2=6>4`. Wait — this
  is `Φ=` sum of ranks 1,3,5 `=4+u_1+u_3` where `u_1≥u_2≥u_3` are the
  sorted `r_i`; since `u_1,u_3>0`, `Φ>4`. ✓

### The 3 remaining mixed compositions, closed exactly this round

The 3 mixed compositions `(1,1,0)`, `(1,0,1)`, `(0,1,1)` (Xiang Yu splits
two *different* original pieces, one cut each) are now closed **exactly, by
the same case-exhaustive "insert fixed pieces into the sorted order" method**
used for `(2,0,0)` and `(1,0,0)` — no numerics anywhere in the arguments
below (a numeric grid search was run only as an *a-priori sanity check*
before writing the exact proofs; it found minima `4.0000075`, `4.000005`,
`4.500628` respectively, matching the exact infima `4`, `4`, `4.5` derived
below to within grid resolution — reported for cross-checking, not used as a
proof step).

Throughout, working in units of `1/7`: `P=4`, `Q=2`, `R=1`.

---

**Case `(1,1,0)`: `P→p₁≥p₂>0` (`p₁+p₂=4`), `Q→q₁≥q₂>0` (`q₁+q₂=2`), `R=1`
untouched.**

Since `p₁≥p₂` and `p₁+p₂=4`, we have `p₁≥2`. Since `q₁≥q₂` and `q₁+q₂=2`,
we have `q₁≥1≥q₂`. Compare `p₁` to the other three values `q₁,q₂,1`: all
three are `≤2≤p₁`, so **`p₁` is always rank 1** (weakly; ties possible only
if `p₁=2`, in which case the sum below is unaffected by which of two equal
elements is called "rank 1"). It remains to determine, among the 4 leftover
values `{p₂,q₁,q₂,1}`, which occupy local ranks 2 and 4 (global ranks 3
and 5), as a function of where `p₂` falls relative to the fixed chain
`q₁≥1≥q₂`. This gives a 4-way exhaustive case split on `p₂`'s position:

- **(i) `p₂≥q₁`** (so `p₂≥q₁≥1≥q₂`): sorted order `p₂,q₁,1,q₂`. Ranks
  2,4 `= q₁,q₂`, summing to `q₁+q₂=2` (fixed, independent of the split).
  `Φ = p₁+2`. Since `p₁≥2`, **`Φ≥4`, equality iff `p₁=2`** (hence
  `p₁=p₂=2`, exact bisection of `P`; note `p₂=2>q₁` always holds then
  since `q₁<2` strictly, `q₂>0` being required for a genuine cut — so this
  case is non-vacuous and equality is *attained*, not just approached).
- **(ii) `1≤p₂<q₁`**: sorted order `q₁,p₂,1,q₂`. Ranks 2,4 `=p₂,q₂`.
  `Φ = p₁+p₂+q₂ = 4+q₂` (using `p₁+p₂=4`). Since `q₂>0`, **`Φ>4`.**
- **(iii) `q₂≤p₂<1`**: sorted order `q₁,1,p₂,q₂`. Ranks 2,4 `=1,q₂`.
  `Φ = p₁+1+q₂`. Since `p₂<1` forces `p₁=4-p₂>3`, and `q₂>0`,
  `Φ>3+1+0=4`. **`Φ>4`.**
- **(iv) `p₂<q₂`**: sorted order `q₁,1,q₂,p₂`. Ranks 2,4 `=1,p₂`.
  `Φ=p₁+1+p₂ = (p₁+p₂)+1 = 4+1=5`. **`Φ=5≥4`.**

These four cases are exhaustive (they partition all `p₂∈(0,2]` given the
fixed chain `q₁≥1≥q₂`) and pairwise-consistent at the shared boundaries: at
`p₂=q₁`, (i) gives `Φ=p₁+2=(4-p₂)+2=6-p₂` and (ii) gives `Φ=4+q₂=4+(2-q₁)
=6-q₁=6-p₂` (using `p₂=q₁`) — match. At `p₂=1`, (ii) gives `Φ=4+q₂` and
(iii) gives `Φ=p₁+1+q₂=(4-1)+1+q₂=4+q₂` — match. At `p₂=q₂`, (iii) gives
`Φ=p₁+1+q₂` and (iv) gives `Φ=p₁+1+p₂=p₁+1+q₂` (using `p₂=q₂`) — match.
(This continuity cross-check is not itself part of the proof — each case
already individually establishes `Φ≥4` — but it confirms no arithmetic slip
at the case boundaries.)

**Conclusion: `Φ≥4` in every sub-case, with equality attained exactly when
`p₁=p₂=2`, for any valid split of `Q`.** ✓

---

**Case `(1,0,1)`: `P→p₁≥p₂>0` (`p₁+p₂=4`), `Q=2` untouched, `R→r₁≥r₂>0`
(`r₁+r₂=1`).**

Again `p₁≥2` (as above), and `q=2` and all of `p₂(≤2), r₁,r₂(<1)` are
`≤2≤p₁`, so **`p₁` is rank 1**. Among the remaining `{p₂, 2, r₁, r₂}`:
since `r₁,r₂<1<2` and `p₂≤2`, the value `2` is always `≥` all three others,
so **`2` is local rank 1** (global rank 2), forced with no case split
(ties only possible if `p₂=2`, harmless as above). The remaining three
values `{p₂,r₁,r₂}` fill global ranks 3,4,5, contributing global ranks 3
and 5 `=` **max and min of `{p₂,r₁,r₂}`**. For any three numbers,
`max+min = (\text{sum}) - \text{median}`, so with
`p₂+r₁+r₂ = (4-p₁)+1 = 5-p₁`:
$$\Phi = p_1 + \big[(5-p_1) - \mathrm{median}(p_2,r_1,r_2)\big] = 5 - \mathrm{median}(p_2,r_1,r_2).$$

It remains to bound `median(p₂,r₁,r₂)`. Since `r₁+r₂=1` with `r₁≥r₂>0`, we
have `r₁≥1/2` and (because `r₂>0`) **`r₁<1` strictly**. There are two
exhaustive cases for which of the three values is the median:

- If `p₂` is the median (i.e. `p₂` lies weakly between `r₂` and `r₁`),
  then `p₂≤r₁<1`, so `median = p₂ < 1`.
- If `p₂` is not the median, the median is `max(r₁,r₂)=r₁<1` (a value that
  is `<1` strictly, as shown above).

In both cases **`median(p₂,r₁,r₂) < 1` strictly.** Hence
$$\Phi = 5-\mathrm{median}(p_2,r_1,r_2) > 5-1 = 4.$$

**Conclusion: `Φ>4` strictly for every valid split, with infimum exactly
`4`** (approached, not attained, as `r₂→0`, `r₁→1`, and `p₂` chosen equal
to the median so `p₂→1`⁻ — never actually reaching `4` since `r₂>0` is
required for a genuine cut). ✓

---

**Case `(0,1,1)`: `P=4` untouched, `Q→q₁≥q₂>0` (`q₁+q₂=2`),
`R→r₁≥r₂>0` (`r₁+r₂=1`).**

`q₁≥1≥q₂` and `0<r₂≤1/2≤r₁<1` as established above. Comparing `q₁` to the
other three: `q₁≥1>r₁` (since `r₁<1` strictly) and `q₁≥1≥q₂` (with equality
possible only when `q₁=q₂=1`, harmless as above), so **`q₁` is always rank
1** among `{q₁,q₂,r₁,r₂}` — hence global rank 1 overall (P=4 is even
larger, so `4` is global rank 1 and `q₁` is global rank 2). The remaining
three values `{q₂,r₁,r₂}` fill global ranks 3,4,5, so as in the previous
case,
$$\Phi = 4 + \big[(q_2+r_1+r_2)-\mathrm{median}(q_2,r_1,r_2)\big] = 4+(q_2+1)-\mathrm{median}(q_2,r_1,r_2) = 5+q_2-\mathrm{median}(q_2,r_1,r_2),$$
using `r₁+r₂=1`. Now case-split on the median of `{q₂,r₁,r₂}` (exhaustive,
3 cases by which element is largest/smallest among `q₂,r₁,r₂`, recalling
`r₁≥r₂`):

- **`q₂≥r₁` (so `q₂` is the max of the three):** median `=r₁`.
  `Φ=5+q₂-r₁`. Since `q₂≥r₁` is exactly the case hypothesis, `q₂-r₁≥0`, so
  `Φ≥5`.
- **`r₂≤q₂<r₁` (`q₂` is the median):** median `=q₂`. `Φ=5+q₂-q₂=5`
  exactly.
- **`q₂<r₂` (`q₂` is the min of the three):** median `=r₂` (since
  `q₂<r₂≤r₁`). `Φ=5+q₂-r₂`. Here we must bound `q₂-r₂` from below: `q₂>0`
  and `r₂≤1/2`, so `q₂-r₂ > 0-1/2 = -1/2`, giving **`Φ>5-1/2=4.5`.**

All three cases give `Φ≥4.5` (the first two give `Φ≥5`, the third gives
`Φ>4.5` strictly), and the third case's bound `4.5` is approached but not
attained (as `q₂→0⁺` and `r₂→1/2⁻`, i.e. `r₁=r₂=1/2` exactly — a legal
cut — combined with `q₂` shrinking to `0`).

**Conclusion: `Φ>4.5>4` for every valid split of this composition.** ✓
(This is comfortably above the target `4`, matching that the numeric
pre-check found this composition's minimum, `≈4.5006`, well clear of the
other two, which sit right at the boundary `4`.)

---

**Conclusion for n=2 (all 10 compositions closed, gap resolved):** every
one of the 10 Xiang-Yu cut-distribution compositions against the ladder
`(P,Q,R)=(4,2,1)` (units of `1/7`) satisfies `Φ≥4`, hence `Φ≥4/7` in the
original units, proved by exact closed-form case analysis with **zero
numerics in the final argument** for all 10 cases. Combined with the
already-complete upper bound `c(2)≤4/7` (Region 1 / Region 2 LP-contradiction
above) and the two degenerate-configuration checks (`<2` Liu Bang points are
strictly dominated), **`c(2) = 4/7` is now a fully rigorous, complete,
non-numeric result — the `n=2` base case is fully closed by this approach.**

### General-n cascade achievability theorem (round 4, new, fully proved for every n)

**Setup.** Fix `n≥1` and the ladder `p_i = 2^{n+1-i}/(2^{n+1}-1)` for
`i=1,…,n+1` (so `p_1>p_2>⋯>p_{n+1}>0`, `∑p_i=1`, and `p_i=2p_{i+1}` exactly
for every `i≤n`). For `0≤k≤n` define the **prefix cascading-halving
response**: Xiang Yu cuts each of `p_1,…,p_k` exactly once, splitting
`p_i→(p_{i+1},p_{i+1})` (using the exact identity `p_i=2p_{i+1}`), and
leaves `p_{k+1},…,p_{n+1}` untouched. (This uses `k≤n` cuts, within
budget.) The round-4 explorer verified by exact `Fraction` arithmetic, for
`n≤6`, that this response gives `Φ=a_n:=2^n/(2^{n+1}-1)` exactly when
`k∈{n-1,n}` and strictly more than `a_n` for every `k≤n-2` (the
outline-reviewer's correction to the explorer's over-generalized original
claim). **This section proves the `k∈{n-1,n}` half rigorously for every
`n`** (not merely checked computationally up to `n=6`), by direct
rank-position counting — no induction, no case-by-case argument, no
numerics.

**Theorem.** For every `n≥1`, both the `k=n` and the `k=n-1` cascading
responses give `Φ=a_n` exactly.

**Proof.**

*Case `k=n`* (cut every piece except the last, `p_1,…,p_n`, each into two
copies of the next rung). The resulting multiset is
$$\{\,p_2,p_2,\ p_3,p_3,\ \ldots,\ p_n,p_n,\ p_{n+1},p_{n+1},p_{n+1}\,\}$$
— each of `p_2,…,p_n` appears with multiplicity exactly 2 (as the two
fragments produced by cutting the previous piece; note `p_2,…,p_{n-1}`
are themselves *also* cut, since `k=n` cuts everything through `p_n`, so
they never survive as standalone pieces, only as the fragment-product of
cutting `p_1,…,p_{n-1}`), and `p_{n+1}` appears with multiplicity 3 (two
fragments from cutting `p_n`, plus its own untouched copy). Total piece
count: `2(n-1)+3=2n+1`, matching `(n+1)` original pieces `+n` cuts.

Sorted descending, `p_i` (for `2≤i≤n`) occupies the two consecutive ranks
`2(i-2)+1` and `2(i-2)+2` — one odd, one even — so contributes `p_i`
**exactly once** to `Φ` (the odd-rank sum), for each `i=2,…,n`. The value
`p_{n+1}` occupies the three consecutive ranks `2n-1,2n,2n+1`, of which two
(`2n-1` and `2n+1`) are odd, so it contributes `2p_{n+1}` to `Φ`. Hence
$$\Phi = (p_2+p_3+\cdots+p_n) + 2p_{n+1}.$$
Since `p_2+\cdots+p_n = \big(\sum_{i=1}^{n+1}p_i\big) - p_1-p_{n+1} =
1-p_1-p_{n+1}`,
$$\Phi = 1-p_1-p_{n+1}+2p_{n+1} = 1-p_1+p_{n+1}.$$
Substituting `p_1=2^n/(2^{n+1}-1)`, `p_{n+1}=1/(2^{n+1}-1)`:
$$\Phi = \frac{(2^{n+1}-1)-2^n+1}{2^{n+1}-1} = \frac{2^{n+1}-2^n}{2^{n+1}-1}
= \frac{2^n}{2^{n+1}-1} = a_n.$$

*Case `k=n-1`* (cut `p_1,…,p_{n-1}`, leave `p_n,p_{n+1}` untouched). The
resulting multiset is
$$\{\,p_2,p_2,\ldots,p_{n-1},p_{n-1},\ p_n,p_n,p_n,\ p_{n+1}\,\},$$
each of `p_2,…,p_{n-1}` with multiplicity 2 (fragment-products, as above),
`p_n` with multiplicity 3 (two fragments from cutting `p_{n-1}`, plus its
own untouched copy), and `p_{n+1}` with multiplicity 1 (untouched, and
nothing cuts down to it since only `p_1,…,p_{n-1}` are cut, producing
values `p_2,…,p_n` only). Total count `2(n-2)+3+1=2n`, matching `(n+1)+
(n-1)` cuts.

Sorted descending: `p_i` (`2≤i≤n-1`) occupies two consecutive ranks (one
odd, one even), contributing `p_i` once each — sum `p_2+\cdots+p_{n-1}`.
`p_n` occupies three consecutive ranks `2n-3,2n-2,2n-1`, two of which
(`2n-3,2n-1`) are odd, contributing `2p_n`. `p_{n+1}` occupies the single
remaining rank `2n`, which is **even**, contributing `0`. Hence
$$\Phi = (p_2+\cdots+p_{n-1}) + 2p_n + 0 = \big(1-p_1-p_n-p_{n+1}\big)+2p_n
= 1-p_1+p_n-p_{n+1}.$$
Substituting `p_1=2^n/(2^{n+1}-1)`, `p_n=2/(2^{n+1}-1)`,
`p_{n+1}=1/(2^{n+1}-1)`:
$$\Phi = \frac{(2^{n+1}-1)-2^n+2-1}{2^{n+1}-1} = \frac{2^{n+1}-2^n}{2^{n+1}-1}
= \frac{2^n}{2^{n+1}-1}=a_n,$$
the same value as the `k=n` case. $\blacksquare$

(Edge cases `n=1`: `k=n=1` gives multiset `\{p_2,p_2,p_2\}`
(three copies, `p_1` fully cut, `p_2` untouched contributes 1 + 2
fragments), `Φ=2p_2=p_1`(using `p_1=2p_2,p_1+p_2=1⟹p_2=1/3,p_1=2/3`, and
indeed `Φ=2/3=a_1`); `k=n-1=0` means "cut nothing", `Φ=p_1=2/3=a_1`
trivially — both formulas above specialize correctly to these boundary
instances, as verified by direct computation.)

**Independent computational cross-check.** Re-verified by exact `Fraction`
script (`/tmp/round-4/verify_cascade.py`) for every `n=1,\ldots,8` and both
`k=n-1,n`: all 16 cases match `a_n` exactly (zero discrepancy, exact
rational equality, not a floating-point approximation) — confirming the
closed-form proof above rather than merely restating the round-4
explorer's numerics.

**What this proves and what it does not.** This is a complete,
general-`n`, non-numeric proof that **some** Xiang Yu response against the
ladder achieves `Φ=a_n` exactly — i.e. it proves `\min_X \Phi(\text{ladder})
\le a_n` for every `n` (the "achievability"/tightness half of pinning down
`c(n)` at the ladder). It does **not** prove the harder, still-open
converse `\min_X\Phi(\text{ladder})\ge a_n` for general `n≥3` (that every
Xiang Yu response, not just these two, gives `Φ\ge a_n`) — that is exactly
the general lower-bound gap the sibling approaches
(`greedy-halving-adversary`, `rank-tie-vertex-reduction`,
`exchange-argument-extremal-response`) are still working on. Nor does it
touch the general upper bound over *all* Liu Bang configurations (this
approach's own specialty; see the negative finding immediately below).

### n=3 upper-bound generalization attempt: a concrete new obstruction (round 4, honest negative result)

This round's assigned task was to extend the `n=2` template-family +
LP-contradiction mechanism (the six strategies `A,B,C,D,E,G` above) to
`n=3` — i.e. to prove the **hard direction**, `c(3)\le 8/15` for *every*
Liu Bang 4-piece configuration `(p,q,r,s)`, `p\ge q\ge r\ge s>0`,
`p+q+r+s=1` (not just at the ladder). This is a genuinely different, harder
task than the achievability theorem above (which only concerns the single
point `L=`ladder`).

**Direct analogs of the `n=2` templates.** Generalizing `A` (bisect
largest) and `C` (bisect two largest) to prefix-cascades, and `D`
(bisect smallest) and `E` (bisect two smallest) to suffix-cascades:
- `T1`: bisect `p` only → `{p/2,p/2,q,r,s}`.
- `T2`: bisect `p,q` → `{p/2,p/2,q/2,q/2,r,s}`.
- `T3`: bisect `p,q,r` → `{p/2,p/2,q/2,q/2,r/2,r/2,s}`.
- `D1`: bisect `s` only → `{p,q,r,s/2,s/2}`.
- `D2`: bisect `r,s` → `{p,q,r/2,r/2,s/2,s/2}`.
- `D3`: bisect `q,r,s` → `{p,q/2,q/2,r/2,r/2,s/2,s/2}`.

**Counterexample (exact, `Fraction`-verified, not numerical evidence):** at
`(p,q,r,s)=(3/8,1/4,1/4,1/8)` (a legal configuration, `p\ge q\ge r\ge s>0`,
sum `1`):
$$\Phi_{T1}=\Phi_{T2}=\Phi_{T3}=\Phi_{D2}=9/16,\qquad
\Phi_{D1}=\Phi_{D3}=11/16,$$
computed by direct sort-and-alternate-sum on each explicit multiset (e.g.
`T1`: sorted `\{1/4,1/4,3/16,3/16,1/8\}`, odd ranks `1/4,3/16,1/8`,
sum `4/16+3/16+2/16=9/16`). All six exceed the target `8/15
\approx0.5333` (since `9/16=0.5625>8/15` and `11/16>8/15`). **If these six
templates were the whole story, this would (falsely) refute the
upper bound at this point** — but they are not the whole story: a seventh,
ad hoc strategy (split `p` into **three equal parts** `p/3=3/8\div3=1/8`,
which happens to exactly equal `s` at this particular point, giving
multiset `\{1/4,1/4,1/8,1/8,1/8,1/8\}`, odd ranks (of 6 elements)
`1/4,1/8,1/8`, `\Phi=1/2`) achieves `\Phi=1/2<8/15`, so there is in fact no
violation at this point — the true `\min_X\Phi` there is at most `1/2`,
comfortably below the target. Full computation:
`/tmp/round-4/verify_counterexample.py`.

**Why "trisect `p` equally" is not a general fix.** A systematic numerical
search (`scipy.optimize`, multi-start Nelder–Mead over the free split
ratios, `/tmp/round-4/n3_investigate2.py`) of the single-composition family
"split `p` into `k` parts, leave `q,r,s` untouched" (`k=2,3,4`) shows the
**optimal** split is generally *not* the equal split, and is not a fixed
closed-form rule either — the optimal fragment values tie to `q`, `r`, or
`s` in configuration-dependent ways (e.g. at
`(p,q,r,s)=(0.8442,0.073,0.0693,0.0135)`, the optimal 4-way split of `p`
is approximately `(0.4154,0.4154,0.0135,0.0135)` — two large near-halves
plus two slivers tied exactly to `s` — while at other points a different
tie pattern is optimal). This matches the round-4 superincreasing
explorer's Finding 1 (vertex enumeration does not collapse to a short
list) — except that finding concerned the *lower*-bound vertex
enumeration against the fixed ladder, whereas this is the same phenomenon
appearing on the *upper*-bound side, for an *arbitrary* Liu Bang
configuration, restricted even to the simplest possible sub-family
("touch only the single largest piece"). In other words: **even the
easiest slice of the `n=3` upper-bound problem does not admit a small
closed-form template family the way `n=2`'s did** — the `n=2` templates
`A,B,C,D,E,G` each had a clean, configuration-independent closed form
precisely because `n=2` has few enough pieces (`\le3` before cuts) that
the "extremal tie" is always at one of two fixed neighbors; at `n=3` (`4`
pieces) the extremal tie can jump between `q`, `r`, or `s` depending on
`(p,q,r,s)`, defeating a single formula.

**Honest verdict.** The `n=2`-style "small finite template family + region
LP-contradiction" upper-bound mechanism does **not** straightforwardly
generalize to `n=3`: the concrete counterexample above shows the direct
6-template analog is insufficient, and the follow-up investigation shows
the obstruction is not a fixable oversight (e.g. "add one more strategy")
but a structural one — template values become genuinely
configuration-dependent (vertex-style) even for the simplest
single-piece-split sub-family. This is new, concrete evidence — not
previously established by this approach or (as far as this round's reading
of the other approach files shows) by any sibling approach — that the
upper-bound direction for general `n` faces essentially the same
"vertex enumeration doesn't collapse" difficulty that the lower-bound
direction has been stuck on since round 3, rather than being an easier,
separate problem. **This does not refute the conjecture** (no actual
violation of `c(3)\le8/15` was found — quite the opposite, the true
minimum at the tested point is comfortably below target); it refutes only
the specific *proof mechanism* this approach was asked to try, at `n=3`.
A viable next step (not attempted this round, flagged for whoever picks
this up) is to characterize the finite set of "tie targets" for the
single-piece-split sub-family in closed form as a function of
`(p,q,r,s)`'s *ordering relative to fractions of* `p` (e.g. is the
optimal tie always to whichever of `q,r,s` is closest to `p/2`, `p/3`,
etc.?) — this was not derived and is left open.

### Toward general n: what the mechanism is, and what is NOT yet done

The n=2 computation shows the *actual* working mechanism is **not** a
continuous local-perturbation/directional-derivative smoothing argument (the
naive Step 3 as originally outlined) — rather, it is: **enumerate a small,
explicit, finite family of "template" adversary strategies (bisect subsets
of the current pieces, or use a multi-cut "capture" move that pushes several
small pieces entirely onto the opponent's ranks), derive each one's exact
value as a closed-form linear function of the configuration, and then run a
direct linear-arithmetic contradiction argument (equivalently: solve a small
LP) showing that at every configuration, the best of these strategies
already beats the target value, with equality forced only at the ladder.**
This is a genuine, different-in-character mechanism from both (a) the
originally-envisioned continuous smoothing lemma, and (b) it is also not
identical to the sibling `greedy-halving-adversary` approach's single global
"bisect current max, n times" strategy, though **strategy A above (bisect
the largest piece once) is literally the first step of that strategy** —
so the two approaches are related but not the same: this approach uses
several *different* template strategies (A, B, C, D, E, G) chosen
per-region, rather than one fixed strategy applied uniformly, and pins the
bound via a static LP-style contradiction rather than an inductive
potential-function argument over the number of remaining moves.

**What would be needed to extend to general n (NOT completed this round):**
1. A general definition of the finite strategy family for `n+1` pieces
   (`p_1≥\dots≥p_{n+1}`), presumably indexed by which *prefix* of the
   sorted pieces gets bisected together (generalizing A/C/E: "bisect the
   top `k` pieces simultaneously") plus "capture" moves generalizing B/G
   that use multiple cuts inside one piece to fully absorb several smaller
   pieces onto the opponent's ranks.
2. Closed-form values for each such strategy (generalizing the `p/2+q`,
   `1/2+r/2`, `p`, `1-p` formulas found here) — plausible by the same
   "insert fixed points into a sorted list, exhaust interleaving patterns"
   method, but the number of cases needed grows with `n` (the `(2,0,0)`
   case for `n=2` already needed 4 sub-cases from a naive 27 combinatorial
   possibilities cut down by sum-feasibility; for general `n` this
   case-count growth needs to be controlled, e.g. by finding a slicker
   inductive/telescoping proof of the closed forms rather than raw case
   enumeration). **Round-4 update: this plausibility guess was tested at
   `n=3` and found to fail** — even the simplest single-piece-split
   sub-family ("touch only `p`") does not have a fixed closed form; see
   the new "n=3 upper-bound generalization attempt" section above for the
   concrete counterexample and the diagnosis of *why* (configuration-
   dependent tie targets, not a case-count problem alone).
3. An `(n+1)`-region (or otherwise structured) partition of the Liu Bang
   simplex, and a contradiction/LP argument on each region — the two-region
   split used for `n=2` (`p≥1/2` vs `p≤1/2`) generalizes plausibly to
   comparing the top piece against various partial sums of the rest, but
   this was not derived for general `n`.
4. The number of relevant Xiang Yu cut-distribution compositions for the
   *lower bound* half (matching ladder) grows combinatorially in `n`
   (partitions of `n` cuts among `n+1` pieces); the case-exhaustion method
   used here for `n=2` does not obviously scale without a cleaner inductive
   argument — this is exactly the kind of "superincreasing sequence
   dominates its refinements" lemma that the sibling `greedy-halving-adversary`
   approach already argues in general (accepted as sound reasoning by the
   round-1 outline review), so the lower-bound half for general `n` should
   most efficiently be **imported from that approach once certified**,
   rather than re-derived by case exhaustion here.

**A sharpened observation from fully closing n=2 (new this round, still a
sketch, not a proof):** every one of the 10 lower-bound compositions reduced
to the same underlying fact: whichever pieces end up *untouched* by Xiang
Yu's cuts act as **fixed pivots** that pin down large contiguous blocks of
the sorted order (e.g. in `(1,1,0)`, `R=1` never moves and always separates
`{q₁,·}` from `{·,q₂}`; in `(1,0,1)`/`(0,1,1)`, the untouched `Q=2`/`P=4`
piece is always the extreme rank, reducing the rest to a **3-element
max+min-vs-median identity** `max+min = total - median`). This suggests the
general-`n` mechanism is not merely "enumerate `k` sub-cases per
composition" but rather: **for a Xiang-Yu response that leaves `j` of the
`n+1` ladder pieces untouched, those `j` pieces partition the sorted order
into `≤j+1` fixed "slots," and `Φ` decomposes as a sum, over slots, of
(sum of the split pieces landing in that slot) `−` (a correction term that
is itself an odd/even-rank statistic of the pieces within that slot)** —
generalizing the `n=2` identities `Φ=5-\mathrm{median}(\cdot)` and
`Φ=p₁+2` found above. Formalizing this "slot decomposition" precisely
(what exactly plays the role of "median" for a block of `>3` elements, and
proving the per-slot correction term is always `≤` the slot's contribution
in the ladder) is the concrete next step for a general-`n` proof via this
approach, but it was **not carried out this round** — it is a sharper,
more specific research direction than the round-1 sketch below, not yet a
proof, and is flagged honestly as such.

**Honest verdict on the feasibility probe (the round's actual task):** the
smoothing/exchange *idea* survives the n=2 probe and produces a genuinely
new, rigorous, fully hand-checkable mechanism for the upper bound — this is
real, non-numerical progress, not just consistent numerics. But it does
**not** generalize to arbitrary n by the mechanism originally envisioned
(continuous local perturbation); it generalizes, if at all, via the
finite-template-strategy + LP-contradiction method sketched above, whose
general-n construction is open and looks like a comparable amount of new
work to what has already been done for n=2 (times a factor that likely
grows with n). Given the sibling approach's lower-bound argument
(superincreasing domination) already covers the general-n lower bound with
a mechanism the reviewer accepted as sound, and given this approach's own
upper-bound mechanism overlaps substantially with that approach's Step 3/4
territory (they share strategy "bisect the max"), the marginal value of
fully generalizing this approach beyond n=2 (rather than importing the
lower bound and cross-checking the upper bound against
`greedy-halving-adversary`'s potential-function argument) should be weighed
by the next round's outline-reviewer.

## Full proof
(absent for the overall problem — Status is `partial`: the problem's actual
claim is `c(n)=2^n/(2^{n+1}-1)` for **every** `n`, and general `n` remains
open. However, the `n=2` special case is now **fully and rigorously
resolved** — both directions, zero numerics — by this approach; see
"Current best" above for the complete `n=2` argument (upper bound: Region
1/Region 2 LP-contradiction; lower bound: all 10 Xiang-Yu cut-distribution
compositions closed exactly). That sub-result is promotable as a certified
lemma/base case — see below — but does not by itself constitute a solved
Status for this approach's overall target. **Round 4 adds a genuinely
general-`n` result** (the cascade achievability theorem: `\min_X\Phi
(\text{ladder})\le a_n` for every `n`, via the two boundary cascade
responses, proved in closed form for all `n`, not just checked
numerically) — this is real general-`n` progress, but it is the easy
("some response attains the target") half, not the hard
("every response is at least the target", or "every Liu Bang
configuration admits a response at most the target") half that would be
needed to close the theorem; both hard halves remain open at `n=3` and
beyond, and this round's attempt to close the upper-bound half at `n=3`
specifically found a new, concrete obstruction rather than a proof — see
the "n=3 upper-bound generalization attempt" section above.)

## Promotable lemmas

- **Bisect-largest identity**: for any `p≥q≥r>0`, bisecting `p` alone gives
  `Φ = p/2+q` (proved by exhaustive 3-case check on the position of `p/2`
  relative to `q,r`). Proved in full above ("Strategy A").
- **Bisect-two-largest identity**: for any `p≥q≥r>0`, bisecting both `p`
  and `q` gives `Φ = 1/2+r/2` (exhaustive 3-case check). Proved above
  ("Strategy C").
- **Bisect-smallest / bisect-two-smallest identities**: `Φ=p+r/2` and
  `Φ=1/2+p/2` respectively, each provable with NO case split since the
  sorted order is forced by `p≥q≥r`. Proved above ("Strategy D", "Strategy
  E").
- **Capture-corner-piece feasibility lemmas** (Strategies B, G): exact
  closed forms `Φ=p` (feasible iff `p≥1/2`) and `Φ=q+r=1-p` (feasible iff
  `p≤1/2` or `p<2r`), with feasibility derived from an explicit extremal
  choice of the free cut parameters. Proved above.
- **Two-piece / one-point domination**: any Liu Bang configuration using
  `<2` marked points yields `min_X Φ ≤ 1/2` (attained exactly for 1 point
  via "bisect both pieces"; approached but not attained, arbitrarily
  closely from above, for 0 points) — hence is strictly dominated by using
  the full `n=2` points whenever `4/7>1/2`. Proved above.
- **`n=2` upper-bound LP contradiction**: `c(2)≤4/7`, via the two-region
  argument above (Region 1: `min(Φ_A,Φ_B,Φ_C)≤4/7` when `p≥1/2`; Region 2:
  `min(Φ_A,Φ_D,Φ_G)≤4/7` when `p≤1/2`). This is a complete, reusable,
  self-contained proof of the hardest direction for the `n=2` base case and
  could be cited/imported by any approach needing a fully rigorous (not
  numerically-assisted) verification of `c(2)=4/7`, e.g. as a base case for
  an eventual induction, or as a cross-check for
  `greedy-halving-adversary`'s general-`n` potential-function argument once
  that is completed (the two should agree at `n=2`, and do).

- **The 3 remaining `n=2` lower-bound compositions, closed exactly** (new
  this round): for the ladder `(P,Q,R)=(4,2,1)` (units of `1/7`):
  - `(1,1,0)` (`P` and `Q` each split once, `R` untouched): `Φ≥4` always,
    via a 4-case split on where `p₂` (the smaller `P`-fragment) falls
    relative to the fixed chain `q₁≥1≥q₂`; equality holds exactly when
    `P` is bisected into two equal halves (`p₁=p₂=2`), for *any* split of
    `Q`. Proved in full above.
  - `(1,0,1)` (`P` and `R` each split once, `Q` untouched): the identity
    `Φ = 5-\mathrm{median}(p_2,r_1,r_2)`, combined with `\mathrm{median}<1`
    strictly (since `r₁<1` always, `r₂>0` forced), gives `Φ>4` strictly,
    infimum `4` (approached, not attained). Proved in full above.
  - `(0,1,1)` (`Q` and `R` each split once, `P` untouched): the identity
    `Φ = 5+q_2-\mathrm{median}(q_2,r_1,r_2)`, with a 3-case split on which
    of `q₂,r₁,r₂` is the median, gives `Φ>4.5` strictly in every case,
    infimum `4.5` (well clear of the target `4`). Proved in full above.
  Together with the previously-closed 7/10 cases, this makes the `n=2`
  lower bound `c(2)≥4/7` fully symbolic, matching the already-complete
  upper bound. This whole `n=2` (both directions, zero numerics) result is
  the single most valuable promotable item this round — a certified,
  reusable base case for any induction on `n` (e.g. by
  `greedy-halving-adversary`), and a cross-check for that approach's
  general-`n` argument once complete.

- **General-`n` cascade achievability theorem** (new this round): for
  every `n\ge1`, the two boundary prefix-cascading-halving responses
  (`k=n-1` and `k=n`, cutting the top `k` ladder pieces each into two
  copies of the next rung) both give `\Phi=a_n=2^n/(2^{n+1}-1)` exactly,
  proved by direct rank-position counting (closed form, no induction or
  numerics needed), cross-checked exactly for `n=1,\ldots,8`. Proved above
  in full ("General-`n` cascade achievability theorem"); proposed for
  promotion as `lemmas/general-n-cascade-achievability.md`. This upgrades
  the round-4 explorer's `n\le6` numerical finding (as narrowed by the
  outline-reviewer's correction) into an actual theorem for all `n`, and
  is directly reusable by any approach needing "some Xiang-Yu response
  against the ladder attains the target exactly" as a building block
  (e.g. the tightness half of the still-open general lower bound).

None of these are yet reviewer-certified; flagging for the outline-reviewer
to consider promoting the identities and the fully-closed `n=2` result
(both directions), plus the new general-`n` cascade achievability theorem,
into `lemmas/` as checked base cases, independent of whichever approach
ultimately closes the general-n proof.

## Round 4 update (this pass)

**Status unchanged: `partial`.** Summary of this round's two results (see
detail above): (1) a new, fully general, non-numeric proof that the two
boundary cascading-halving responses give `\Phi=a_n` exactly for *every*
`n` — genuine general-`n` content, proposed as a new certified lemma
(`lemmas/general-n-cascade-achievability.md`); (2) an honest negative
result at `n=3`: the direct 6-template analog of this approach's own
certified `n=2` upper-bound mechanism fails at a concrete, exactly
verified configuration, and the underlying reason (configuration-dependent
tie targets even for the simplest single-piece-split sub-family) suggests
the upper-bound direction shares the same "vertex enumeration doesn't
collapse" difficulty already identified on the lower-bound side by the
round-4 superincreasing explorer and the sibling vertex-based approaches.
**This approach's own upper-bound specialty is now understood to be at
least as hard at `n\ge3` as the lower-bound direction sibling approaches
have been stuck on since round 3** — not an easier, parallel track, as
previously hoped. No overclaiming: the conjecture itself was not
threatened by the counterexample (the true minimum there is well below
target), only the specific small-template proof technique.

## Outline update (round 3, proof-outliner)

No revision to the certified `n=2` result (it stands, fully closed, both
directions). Worth recording a cross-approach convergence found by the
round-3 rank-tracking explorer (`/tmp/round-3/math-explorer-rank-tracking.md`):
this file's own "slot decomposition" sketch (above, "A sharpened
observation from fully closing n=2") — untouched pieces act as fixed pivots
partitioning the sorted order into slots, with a per-slot median-like
correction — is **the same underlying idea**, arrived at independently, as
the new sibling approach `rank-tie-vertex-reduction`'s "piecewise-linear
vertex minimum" mechanism (both say: the extremal configuration is pinned by
exact equalities/pivots, not by a generic mass bound). This convergence
(two independent routes landing on "reduce to a finite exact-matching/pivot
combinatorics problem") is itself evidence this is the real content of the
general-$n$ gap. Recommend: if a future round wants to push this approach's
own general-$n$ generalization further, coordinate with
`rank-tie-vertex-reduction`'s builder rather than re-deriving the slot
decomposition independently — they are very likely the same finite
enumeration problem viewed from two directions, and merging effort avoids
duplicated work. No change made to this file's proved content.
