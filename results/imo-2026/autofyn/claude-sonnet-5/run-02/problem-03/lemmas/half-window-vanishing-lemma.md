## Statement

Fix $n\ge2$, the $n$-ladder $p_i=2^{n+1-i}/D$ ($D=2^{n+1}-1$, $i=1,\dots,n+1$),
and suppose Xiang Yu spends exactly one cut on $p_1$, splitting it into
fragments $x\ge p_1-x>0$ ($x\in[p_1/2,p_1)$), and spends his remaining
$\le n-1$ cuts on the tail $T=\{p_2,\dots,p_{n+1}\}$ in an arbitrary legal
way, producing a refinement $G'$ with $\mathrm{Total}(G')=r=1-p_1$. Write
$\Delta:=2x-p_1\ge0$, $W:=[p_1-x,x)$ (length $\Delta$),
$v(t):=\mathbb1[N_{G'}(t)\text{ odd}]$. Then, unconditionally, for every
$n\ge2$, every such $x$, and every legal $G'$:
$$(\star\star):\qquad \int_{W\cap[0,r)} v(t)\,dt\ \le\ \frac\Delta2.$$

Combined with the certified `cross-term-reduction-theorem`, this **fully
closes the entire "single cut on $p_1$, arbitrary legal tail refinement"
case** of the general lower-bound domination goal, for every $n\ge2$: i.e.
$A(\{x,p_1-x\}\cup G')\ge f(n):=1/D$ for every legal $G'$.

## Key sub-lemma (Half-Window Vanishing)

Every element of a legal refinement $G'$ of $T$ is $\le p_2$ (a legal
fragment of $p_i$, $i\ge2$, is $\le p_i\le p_2$ since the ladder is
decreasing and a positive sum of $\ge1$ terms has each term $\le$ the
total). Hence $N_{G'}(t)=0$ for every $t\ge p_2$, so $v\equiv0$ on
$[p_2,\infty)$.

## Proof of $(\star\star)$

By the ladder identity $p_1=2p_2$, $p_2$ is the exact midpoint of $W$:
writing $W_L:=[p_1-x,p_2)$, $W_R:=[p_2,x)$, both have length $\Delta/2$ and
$W=W_L\sqcup W_R$ (trivial when $\Delta=0$, both empty). Since $r\ge p_2$
(a sum of $n\ge1$ positive terms including $p_2$) and $p_1-x\ge0$,
$W_L\subseteq[0,r)$.

- *Right half:* $W_R\subseteq[p_2,\infty)$, so $v\equiv0$ there (key
  sub-lemma), giving $\int_{W_R\cap[0,r)}v=0$.
- *Left half:* $v\le1$ pointwise, so $\int_{W_L}v\le|W_L|=\Delta/2$.

Summing: $\int_{W\cap[0,r)}v\le\Delta/2+0=\Delta/2$. $\blacksquare$

## Verification

- **Round 6 (proof-reviewer):** independently re-derived the proof line by
  line and re-verified by a fresh 2000-trial exact-`Fraction` simulation
  (built independently of the approach's own script) across
  $n=2,\dots,6$: zero violations.
- **Round 7 (proof-reviewer, this certification):** independently
  re-verified again with a fresh, independently-written 5000-trial
  exact-`Fraction` script (random $n=2,\dots,6$, random asymmetric $x$,
  random tail refinements of varying cut counts): zero violations. Also
  used (and cross-checked) as the load-bearing fact underlying this round's
  `case-ii-exact-peel-identity` (10,138 independent trials, zero
  mismatches) and `rank-pigeonhole-budget`'s Case-II/Case-I machinery,
  which both reuse the identical "no tail/foreign element exceeds $p_2$"
  fact.

## Origin

`results/imo-2026-03/approaches/rank-tie-vertex-reduction.md`, §5.2
(round 6). This file was recommended for certification/promotion at that
time but the standalone lemma file was not created until round 7's review;
backfilled here since round-7 work (`case-ii-exact-peel-identity`) directly
cites it as "the certified Half-Window Vanishing Lemma."

## Certification note (proof-reviewer, round 7)

**CERTIFIED.** Fully proved, general $n\ge2$, no gap; independently
re-derived and re-verified numerically as described above.
