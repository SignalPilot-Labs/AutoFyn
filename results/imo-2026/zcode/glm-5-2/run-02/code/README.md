# Proof certificates: OM = ON

This folder contains machine-checkable certificates for the theorem:

> Let $ABC$ be a triangle, $M,N$ the midpoints of $AB,AC$. Let $K\in(BMC)$,
> $L\in(BNC)$ with $K$ inside $\angle LBA$, $L$ inside $\angle ACK$, and
> $\angle KBA=\angle ACL$, $\angle LBK=\angle LNC$, $\angle LCK=\angle BMK$.
> If $O$ is the circumcentre of $\triangle AKL$, then $OM=ON$.

## Files

| file | what it does |
|------|--------------|
| `groebner_proof.py` | **Rigorous algebraic proof.** Places the midpoint of $MN$ at the origin with $M=(-1,0)$, $N=(1,0)$, $A=(a,h)$. Parametrises $K,L$ by $\varphi=\angle KBA=\angle ACL$ and $m,n>0$. Shows conditions (ii),(iii) are equivalent (up to nonzero scalar factors) to two quadratic relations $R_n,R_m$, then proves the numerator of the circumcentre's $x$-coordinate lies in the ideal $\langle R_m,R_n,c^2+s^2-1\rangle$ via a **Gröbner-basis reduction whose remainder is exactly 0**. Hence $O_x=0$, i.e. $O$ is on the perpendicular bisector of $MN$. |
| `numerical_check.py` | **Independent numerical check.** Builds 300 random triangles/parameters, solves for $K,L$ satisfying *all* hypotheses, and reports $\max|OM-ON|$. |

## How to run

```bash
python3 groebner_proof.py    # exact symbolic computation -> remainder 0
python3 numerical_check.py   # ~300 configs -> |OM-ON| ~ 1e-13
```

Requires `sympy` (for `groebner_proof.py`) and `numpy`, `scipy` (for `numerical_check.py`).

## Proof sketch (see the writeup for full detail)

1. **Coordinates.** Midpoint of $MN$ at origin, $MN$ on the $x$-axis, $|MN|=2$:
   $M=(-1,0),\;N=(1,0),\;A=(a,h),\;B=(-2-a,-h),\;C=(2-a,-h)$.
   Goal: circumcentre $O$ of $\triangle AKL$ has $O_x=0$.

2. **Parametrise.** With $\varphi=\angle KBA=\angle ACL$ (condition (i)),
   $c=\cos\varphi,s=\sin\varphi$, write
   $K=B+m\,R_{-\varphi}(A-B)$, $L=C+n\,R_{+\varphi}(A-C)$ ($m,n>0$).

3. **Conditions (ii),(iii).** Using oriented-angle tangent identities
   $\frac{[u,v]}{u\cdot v}$, conditions (ii) and (iii) expand (and factor,
   using $c^2+s^2=1$) to:
   $$R_n := U n^2 + V n + (ch-(1+a)s)=0,\qquad R_m := U m^2 + V m + (ch-(1-a)s)=0,$$
   where $U=s(a^2+h^2-1)+2ch$ and $V=-cs(a^2+h^2)-2c^2h+cs-h$. The dropped
   scalar factors $8m\cdot\frac{|AC|^2}{4}$ and $8n\cdot\frac{|AB|^2}{4}$ are
   nonzero, so the equivalences are exact.

4. **Circumcentre.** $O_x = P\,/\,(2[K-A,L-A])$ where $P$ is an explicit polynomial
   and the denominator is nonzero (since $O$ exists).

5. **The identity.** Reducing $P$ modulo $\langle R_m,R_n,c^2+s^2-1\rangle$ by a
   Gröbner basis (lex order $m>n>c>s$) gives **remainder 0**. So $P=0$ whenever
   the hypotheses hold, giving $O_x=0$.

6. **Conclusion.** $O$ lies on the $y$-axis = perpendicular bisector of $MN$,
   hence $OM=ON$. $\blacksquare$
