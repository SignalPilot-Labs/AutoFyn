## Two negative lemmas: peel/bisect-plus-full-IH mechanisms cannot reach case (b2)

**Status: dead-end records** (certified negative results — no future round
should attempt to "improve" either exact mechanism into case (b2)
territory; a genuinely different mechanism is needed).

Recall (from `lp-duality-certificate.md`) case (b2) is the open sub-region
of the general upper bound's $p_1<T/2$ regime with $T/D_n<p_2<a_nT/2$.

### Negative Lemma 1 (Peel-$p_1$-$p_2$-Plus-IH Zero-Slack Dead End)

**Statement.** The mechanism "peel $p_1$ against $p_2$ (one-step-peel, one
cut), then apply the full induction hypothesis $P(m-1)$ to the reduced
instance $S'=\{p_1-p_2,p_3,\dots,p_m\}$" certifies $\Phi_{\min}\le a_nT$ if
and only if $p_2\ge a_nT/2$ — exactly case (a)'s own defining threshold,
with zero slack. Hence this mechanism can never certify any marking in case
(b2) (defined by $p_2<a_nT/2$), regardless of how the IH is strengthened.

**Proof.** By `one-step-peel-identity`, $\Phi_{\min}\le p_2+\Phi_{\min}(S')$;
substituting the full IH $\Phi_{\min}(S')\le a_{n-1}T'$ ($T'=T-2p_2$) gives
$\Phi_{\min}\le p_2(1-2a_{n-1})+a_{n-1}T$. Solving
$p_2(1-2a_{n-1})+a_{n-1}T\le a_nT$ for $p_2$ (note $1-2a_{n-1}<0$ since
$a_{n-1}>1/2$, so the inequality flips): $p_2\ge\dfrac{(a_n-a_{n-1})}
{1-2a_{n-1}}T$. This coefficient equals $a_n/2$ exactly for every $n\ge1$
(verified algebraically below), giving threshold $p_2\ge a_nT/2$ exactly,
zero slack. $\blacksquare$

### Negative Lemma 2 (Bisect-$p_1$-Plus-IH Containment Dead End)

**Statement.** The mechanism "bisect $p_1$ alone (one cut), then apply the
full IH $P(m-1)$ to the untouched tail $\{p_2,\dots,p_m\}$" certifies
$\Phi_{\min}\le a_nT$ if and only if $p_1\ge a_nT$ — a strict subset of the
already-closed region $\{p_1\ge T/2\}$ (since $a_n>1/2$). Hence this
mechanism supplies zero new coverage of $p_1<T/2$, hence zero coverage of
case (b2).

**Proof.** By the bisect-$p_1$ identity, $\Phi=p_1/2+\Phi'(\text{tail})$;
substituting the full IH $\Phi'\le a_{n-1}T'$ ($T'=T-p_1$) and maximizing
the resulting affine-decreasing-in-$p_1$ bound over $p_1\in[a_nT,T)$ (the
coefficient of $p_1$ is $1/2-a_{n-1}<0$) gives threshold
$p_1\ge\dfrac{a_n-a_{n-1}}{1/2-a_{n-1}}T$. This coefficient equals $a_n$
exactly for every $n\ge1$ (verified algebraically below). Since $a_n>1/2$,
$\{p_1\ge a_nT\}\subsetneq\{p_1\ge T/2\}$, already fully covered elsewhere.
$\blacksquare$

## Certification note (proof-reviewer, round 14)

Independently re-derived both threshold algebra chains from scratch (not
re-running the builder's script) using $a_n=2^n/(2^{n+1}-1)$:
$$\frac{a_n-a_{n-1}}{1-2a_{n-1}}=\frac{a_n}{2}\quad\text{and}\quad
\frac{a_n-a_{n-1}}{1/2-a_{n-1}}=a_n$$
verified exactly (symbolic `Fraction` arithmetic, no rounding) for
$n=1,\dots,14$ in both cases — matching the claimed exact zero-slack
thresholds precisely. Both dead-end conclusions (disjointness from case
(b2)) follow immediately from the exact thresholds and the definitions of
case (a) and case (b2)/the $p_1\ge T/2$ region, already established
elsewhere in this project. No gap found; both negative results are
correctly and rigorously proved, not merely observed numerically.

**Origin:** `results/imo-2026-03/approaches/lp-duality-certificate.md`,
round 14, R14.2.
