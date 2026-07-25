## Lemma: Schur-monotonicity criterion for linear order-statistic functionals, and its consequence that OddSum is not majorization-monotone

**Proposition (Hardy–Littlewood–Pólya-style Schur-monotonicity criterion).**
Fix $N\ge2$ and weights $c_1,\dots,c_N\in\mathbb R$. Write
$L_c(x):=\sum_i c_i x_{[i]}$ for the descending order statistics
$x_{[1]}\ge\cdots\ge x_{[N]}$ of a vector $x$. Then
$$M'\succ M\ \implies\ L_c(M')\ge L_c(M)\quad\text{(for every majorization pair $M'\succ M$ of length $N$)}$$
holds **if and only if** $c_1\ge c_2\ge\cdots\ge c_N$.

**Proof.** ($\Leftarrow$) With $d_j:=\sum_{i\le j}(m_i'-m_i)$ (so $d_0=d_N=0$,
$d_j\ge0$ for $1\le j\le N-1$ by majorization), Abel summation gives
$L_c(M')-L_c(M)=\sum_{i=1}^{N-1}(c_i-c_{i+1})d_i$, a sum of products of
nonnegative terms when $c$ is non-increasing, hence $\ge0$.
($\Rightarrow$) If $c_{i_0}<c_{i_0+1}$ for some $i_0$, take $M$ uniform
($1/N$ each) and $M'$ obtained by moving mass $\varepsilon\in(0,1/N)$ from
rank $i_0+1$ to rank $i_0$ (a valid majorization pair, $d_j=0$ for $j\ne
i_0$, $d_{i_0}=\varepsilon$); then $L_c(M')-L_c(M)=(c_{i_0}-c_{i_0+1})\varepsilon<0$.
$\blacksquare$

**Corollary (OddSum is not Schur-monotone for $N\ge3$).** Applying the
Proposition to $c=(1,0,1,0,\dots)$ (the OddSum weight pattern): $c_1-c_2=1>0$
but $c_2-c_3=-1<0$ for $N\ge3$, so neither $M'\succ M\implies\mathrm{OddSum}(M')\ge\mathrm{OddSum}(M)$
nor the reverse holds in general. (For $N=2$, $c=(1,0)$ is non-increasing,
so OddSum restricted to size-2 multisets IS Schur-monotone — a genuine but
uninteresting-for-this-problem exception.)

**Consequence.** The "majorization/suffix-domination monotonicity"
mechanism (the natural transplant of the crux corpus's suffix-domination
partial order, from `aimo-0287`, to a single sorted real vector) carries
**no** information about OddSum's value, in either direction, for any
instance of interest ($N\ge3$). This is a genuine dead end for this
specific mechanism, not merely a failed numeric search.

**Independent verification (proof-reviewer, round 6).** Re-derived the
Proposition from scratch (standard HLP-style argument, correctly applied).
Independently re-verified the concrete counterexample with exact
`Fraction` arithmetic: $M=(0.34,0.33,0.32,0.01)$, $M'=(0.36,0.34,0.29,0.01)$,
both summing to $1$; prefix sums of $M'$ are $(9/25,7/10,99/100,1)$ and of
$M$ are $(17/50,67/100,99/100,1)$, so $M'\succ M$ holds exactly (every
prefix of $M'$ is $\ge$ the corresponding prefix of $M$); but
$\mathrm{OddSum}(M)=33/50$ while $\mathrm{OddSum}(M')=13/20<33/50$ — an
exact, confirmed violation.

**Source.** Proved in `approaches/dyadic-potential-invariant.md` (round 6,
Section 7).

**Reuse.** Rules out majorization-based monotonicity arguments for OddSum
in any future round of this problem or any problem reducing to a similar
alternating-rank-sum functional; the general Proposition itself (not
specific to OddSum) is reusable whenever a future approach needs to check
whether *any* linear order-statistic functional is majorization-monotone.
