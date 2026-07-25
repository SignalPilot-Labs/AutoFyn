# Explorer report: $n=3$ case-split construction scouting (round 21)

**Lens:** find a genuinely new $n=3$ upper-bound construction — a real
case-split (different fragment-pairings/response-shapes on different
sub-regions of $B(3)$), not another single uniform pairing. Tested by
dense grid/LP-style stress-testing over the *whole* region $B(3)$, not
random sampling alone (per round 20's rule that random sampling misses
thin adversarial regions).

## Setup used (re-derived, matches round 19/20's parametrization)

$g_1=p_1-p_2,\ g_2=p_2-p_3,\ g_3=p_3-p_4$, each $>\gamma_3=1/15$;
$p_4=(1-g_1-2g_2-3g_3)/4$; $B(3)$ additionally requires $p_4>0$
($g_1+2g_2+3g_3<1$) and $p_1<1/2$ (equivalently $3g_1+2g_2+g_3<1$, a
clean identity re-derived directly). Target: $c(3)=8/15$. All scans
below are exact-arithmetic-checked at reported boundary points; the bulk
screening used dense uniform sampling ($2$–$4\times10^5$ region-valid
points per construction) plus targeted sampling of the $p_4\to0$
boundary (the region flagged historically hardest).

## Already-refuted baselines (confirmed, not retried as-is)

- **$p_2,p_3$-tied pairing** ($M=\{p_2,p_2,p_3,p_3,r,p_4\}$,
  $r=p_1-p_2-p_3$): infeasible ($r\le0$) on $\approx80\%$ of $B(3)$ in
  this scan (matches round 20's finding); on the $\approx20\%$ where
  feasible, a **new finding**: it *also* has its own value-violation
  region ($\approx8.7\%$ of its feasible subset, e.g.
  $p\approx(0.441,0.254,0.187,0.118)$, excess $\approx0.025$) — not
  previously reported, since round 20 stopped at the feasibility
  refutation.
- **$p_3,p_4$-tied pairing** ($M'=\{r',p_3,p_3,p_4,p_4,p_2\}$): confirmed
  broadly infeasible-to-succeed, $\approx64\%$ of its (fully feasible)
  domain violates, matching round 20's $\sup=1/9$ finding.

## New constructions tried this round

All use $\le3$ cuts on the four-piece partition $p_1>p_2>p_3>p_4$.

| id | construction | cuts | feasible % | viol % of feasible | worst excess found |
|---|---|---|---|---|---|
| C | $p_1\to\{p_2,g_1\}$, $p_3\to\{p_4,g_3\}$ ("double cascade", $p_2,p_4$ each duplicated) | 2 | 100% | 30% | $\mathbf{1/15}$ (exact, at boundary below) |
| D | $p_2\to\{p_3,p_4,s\}$, $s=p_2-p_3-p_4$, $p_1$ untouched ("shift-down" analogue of the $p_2,p_3$-pairing, one level lower) | 2 | 89.5% | **100%** of feasible | $0.217$ |
| E | $p_1\to\{p_3,r\}$, $p_2,p_3,p_4$ untouched, skip $p_2$ (5 elements, odd) | 1 | 100% | 74.7% | $0.111$ |
| F | $p_1\to\{p_2,p_4,r\}$, skip $p_3$ | 2 | 93.1% | 61.6% | $0.088$ |
| G | $p_1\to\{p_2,g_1\}$, $p_2\to\{p_3,g_2\}$ (cascade top-down) | 2 | 100% | 97.4% | $0.133$ |
| K | full 3-cut cascade: $p_1\to\{p_2,g_1\}$, $p_2\to\{p_3,g_2\}$, $p_3\to\{p_4,g_3\}$ (7 elements, odd) | 3 | 100% | **100%** | $0.133$ |
| trisection | $p_1\to\{p_1/3,p_1/3,p_1/3\}$, untied, $p_2,p_3,p_4$ untouched | 2 | 100% | **100%** | $0.161$ |

**D, K, and trisection are dead on arrival** (fail on essentially the
entire region, not a sub-region — no point case-splitting *to* them).
**E and G are dominated** by C (worse violation rates, no region where
they beat C). **F** is dominated too. None of the seven is close to a
usable single-region patch on its own.

**Best-of-all-seven test** (per point, take the construction with the
smallest OddSum, i.e. simulate an *optimal* case-split among exactly
these seven shapes): worst-case residual excess over $4\times10^5$
region-valid points is $\approx0.0649$ — **still strictly positive**, so
even the best available case-split among all constructions tried this
round (old and new) does **not** close $B(3)$. Construction C
(the double-cascade $p_1\!\to\!\{p_2,g_1\}$, $p_3\!\to\!\{p_4,g_3\}$) is
the argmin at $\approx80\%$ of sampled points and the $p_2,p_3$-pairing
(A) at the other $\approx20\%$ (exactly its feasible sub-region) — the
other five constructions are *never* the best choice anywhere in the
sample.

## The persistent hardest corner (found repeatedly, not a fluke)

Independently of which construction, the worst residual keeps
concentrating at the **same** corner: $g_1,g_2\to\gamma_3^+$ (both
smallest gaps pinned at the minimum) with $p_4\to0^+$. In the exact
limit this is the boundary point
$$p^\dagger=\Bigl(\tfrac25,\ \tfrac13,\ \tfrac4{15},\ 0\Bigr)
=\Bigl(\tfrac6{15},\tfrac5{15},\tfrac4{15},\tfrac0{15}\Bigr),$$
where $g_1=g_2=\gamma_3=1/15$ exactly and $g_3=4/15$. This is a clean,
reproducible, exactly-computable witness of the **best construction
found's residual failure**: at $p^\dagger$, construction C gives
$M=\{p_2,p_2,g_1,p_4,p_4,g_3\}=\{\tfrac13,\tfrac13,\tfrac1{15},0,0,
\tfrac4{15}\}$, sorted $\tfrac13,\tfrac13,\tfrac4{15},\tfrac1{15},0,0$,
so
$$\mathrm{OddSum}(M)=\tfrac13+\tfrac4{15}+0=\tfrac9{15}=\tfrac35,\qquad
\tfrac35-\tfrac8{15}=\tfrac1{15}>0$$
— an **exact** excess of $1/15$, matching the numeric scan
($\approx0.0649$) almost exactly (the tiny gap is because $p^\dagger$ is
an open-region limit, not attained). All seven constructions tested this
round fail at or near this same corner (best-of-seven $\approx0.0649
\approx 1/15$ confirms C is essentially optimal among the tried family
there). This strongly suggests the corner is a **genuine structural
obstruction for this whole family** ("split one or two pieces, tie
fragments to other pieces"), not an artifact of any one pairing choice.

## What this rules out / narrows for next round

1. **No single construction among the eight tried (two from round 20,
   six new) closes $B(3)$**; best achievable via naive case-splitting
   among them still leaves a real gap ($1/15$) at an explicit, exact
   corner point.
2. **The odd-fragment-count parity diagnosis (Section 10.8) is
   reconfirmed but not sufficient**: E (5 elements) and K (7 elements)
   are indeed among the worst performers, but several *even*-count
   constructions (D, G, trisection) are just as bad or worse — evenness
   is necessary-looking but nowhere near sufficient for success.
3. **The obstruction is not primarily "which pieces get tied"** — every
   tie pattern tried (adjacent pairs $p_2,p_3$; $p_3,p_4$; skip-one
   $p_2,p_4$; cascading single-cuts; untied equal split) fails at
   essentially the *same* corner, $p^\dagger=(2/5,1/3,4/15,0)$-ish. A
   construction that wants to beat this corner needs to specifically
   handle the regime "$g_1,g_2$ near the floor $\gamma_3$, $p_4$ near
   $0$" — i.e. a partition that is *effectively 3 pieces* (since $p_4$
   is negligible) but with the two upper gaps pinned at the *legal
   minimum*, so the fragments this family produces ($g_1$ or $g_3$,
   whichever is used) are too small to ever land at an odd rank and pull
   the sum down.
4. **Concrete next-round idea (untested, flagged honestly):** near
   $p^\dagger$, $p_4\approx0$ means Xiang Yu effectively has only 3
   "real" pieces summing to $\approx1$ with the top two gaps at the
   floor — this is structurally close to the (now fully closed) $n=2$
   problem but with $\gamma_3=1/15<\gamma_2=1/7$, i.e. a *more uniform*
   3-piece configuration than $n=2$ ever allows, which is exactly why it
   resists every $n=2$-style single-cut mechanism. A genuinely different
   idea worth LP-testing next: use the **third spare cut** (all
   constructions above except K/trisection leave at least one of $n=3$'s
   3 cuts unused) to split $p_4$ itself (even though tiny) tied to
   $g_1$ or $g_3$, specifically to shift the parity/rank of the smallest
   fragments right at this corner — i.e., a genuine 3-cut, three-piece-
   touched construction different from both the "cascade" (K, refuted)
   and "trisect one piece" (refuted) shapes tried here. Not attempted
   this round; flagged as the most promising concrete next probe, since
   it directly targets the one recurring failure point rather than
   another global variant.

## Files / scripts

Exploratory scripts (not part of the proof, scratch only):
`/tmp/n3_explore.py`, `/tmp/n3_scan.py`, `/tmp/n3_bestof.py`,
`/tmp/n3_trisect.py`, `/tmp/n3_more.py`.
