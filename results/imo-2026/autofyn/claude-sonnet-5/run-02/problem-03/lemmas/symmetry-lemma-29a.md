## Lemma 29a (Symmetry Lemma)

**Statement.** Let $F_2$ be any finite multiset of nonnegative reals with
$\mathrm{Total}(F_2)=M>0$, and let $u_{F_2}(x):=\mathbb1[N_{F_2}(x)\text{
odd}]$ be its odd-parity indicator (as in the certified
`integral-alternating-sum-formula`). Then
$$\int_0^{M/2} u_{F_2}(x)\,dx \ \ge\ \int_{M/2}^{\infty} u_{F_2}(x)\,dx,$$
equivalently $A(F_2)\le 2\int_0^{M/2}u_{F_2}(x)\,dx$.

## Proof

Let $a:=\int_0^{M/2}u_{F_2}$, $b:=\int_{M/2}^\infty u_{F_2}$ (so $a+b=A(F_2)$).
Let $g_1:=\max(F_2)$ (one copy) and $\mathrm{Rest}:=F_2\setminus\{g_1\}$.

**Case (i): $g_1<M/2$.** Every element of $F_2$ is $<M/2$, so $N_{F_2}(x)=0$
(even) for all $x\ge M/2$, giving $b=0\le a$.

**Case (ii): $g_1\ge M/2$.** Then $\mathrm{Total}(\mathrm{Rest})=M-g_1\le M/2
\le g_1$. For $x<g_1$: $N_{F_2}(x)=1+N_{\mathrm{Rest}}(x)$, so
$u_{F_2}(x)=1-u_{\mathrm{Rest}}(x)$. For $x\ge g_1$: every element of
$\mathrm{Rest}$ is $\le\mathrm{Total}(\mathrm{Rest})\le g_1\le x$, so
$N_{\mathrm{Rest}}(x)=0=N_{F_2}(x)$, giving $u_{F_2}(x)=u_{\mathrm{Rest}}(x)=0$.

Since $M/2\le g_1$, on $[0,M/2)$: $a=\int_0^{M/2}(1-u_{\mathrm{Rest}})
=M/2-\int_0^{M/2}u_{\mathrm{Rest}}$. Since
$u_{\mathrm{Rest}}(x)=0$ for $x\ge\mathrm{Total}(\mathrm{Rest})$ and
$\mathrm{Total}(\mathrm{Rest})\le M/2$, $\int_0^{M/2}u_{\mathrm{Rest}}
=A(\mathrm{Rest})$, so $a=M/2-A(\mathrm{Rest})$.

On $[M/2,g_1)$: $u_{F_2}(x)=1-u_{\mathrm{Rest}}(x)=1-0=1$; and $u_{F_2}\equiv0$
on $[g_1,\infty)$. Hence $b=g_1-M/2$.

Combining: $a-b=(M/2-A(\mathrm{Rest}))-(g_1-M/2)=\mathrm{Total}(\mathrm{Rest})
-A(\mathrm{Rest})\ge0$, using $A(S)\le\mathrm{Total}(S)$ for any multiset $S$
(the elementary bound from the integral characterization of $A$).

Both cases exhaust all possibilities for $F_2$ (either $g_1<M/2$ or
$g_1\ge M/2$), disjointly. $\blacksquare$

## Certification note (proof-reviewer, round 14)

Independently re-derived the two-case telescoping argument and re-verified
with a fresh, independently-written 20,000-trial exact-`Fraction` script
(random multisets of size 1-6, random rational total $M$), zero violations
of $a\ge b$. The proof only uses the elementary $A(S)\le\mathrm{Total}(S)$
fact and case analysis on the location of the max element relative to $M/2$
— no gap, no hidden case, fully general (no ladder structure anywhere).
Certified correct as written.

**Origin:** `results/imo-2026-03/approaches/greedy-halving-adversary.md`,
round 14, Lemma 29a.
