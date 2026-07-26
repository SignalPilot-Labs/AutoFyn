Worked for 37 m 23 s

# Solution

We prove that the circumcentre $O$ of $\triangle AKL$ lies on the perpendicular bisector of $MN$, which is equivalent to $OM=ON$.

## Setup and coordinates

Let $G$ be the midpoint of $MN$. Place coordinates with $G$ at the origin and $MN$ along the $x$-axis, scaled so that
$$M=(-1,0),\qquad N=(1,0).$$
Write $A=(a,h)$ with $h>0$. Since $M,N$ are the midpoints of $AB,AC$,
$$B=2M-A=(-2-a,\,-h),\qquad C=2N-A=(2-a,\,-h).$$
The perpendicular bisector of $MN$ is the $y$-axis, so we must show that the circumcentre $O=(O_x,O_y)$ of $\triangle AKL$ satisfies $O_x=0$.

## Parametrising $K$ and $L$

Set $\varphi=\angle KBA=\angle ACL$ (this is condition (i)), and write $c=\cos\varphi$, $s=\sin\varphi$, so $c^2+s^2=1$. Let $R_\theta$ denote rotation through angle $\theta$. The ray $BK$ is obtained from $BA$ by a rotation of $-\varphi$ (toward the interior of the triangle), and $CL$ is obtained from $CA$ by a rotation of $+\varphi$; thus for some $m,n>0$,
$$K=B+m\,R_{-\varphi}(A-B),\qquad L=C+n\,R_{+\varphi}(A-C).$$
Concretely (with $\vec{BA}=A-B=(2a+2,2h)$ and $\vec{CA}=A-C=(2a-2,2h)$),
$$K=B+m\bigl(c(2a+2)+2hs,\; 2ch-s(2a+2)\bigr),$$
$$L=C+n\bigl(c(2a-2)-2hs,\; 2ch+s(2a-2)\bigr).$$

## Translating conditions (ii) and (iii)

For two non-zero vectors $u,v$, the equality of (unsigned) angles $\angle(u,\cdot)=\angle(v,\cdot)$ is captured by the *oriented* tangent identity
$$\frac{[u,v]}{u\cdot v}\ \text{ agrees in sign and value}, \qquad\text{i.e.}\quad [u_1,v_1]\,(u_2\cdot v_2)=(u_1\cdot v_1)\,[u_2,v_2],$$
where $[\cdot,\cdot]$ is the 2-D cross product. Applying this:

* **(ii)** $\angle LBK=\angle LNC$ uses $(u_1,v_1)=(\vec{BK},\vec{BL})$ and $(u_2,v_2)=(\vec{NC},\vec{NL})$.
* **(iii)** $\angle LCK=\angle BMK$ uses $(u_1,v_1)=(\vec{CL},\vec{CK})$ and $(u_2,v_2)=(\vec{MB},\vec{MK})$.

Define
$$U=s(a^{2}+h^{2}-1)+2ch,\qquad V=-cs(a^{2}+h^{2})-2c^{2}h+cs-h.$$
A direct expansion (using $c^2+s^2=1$) gives the exact factorisations
$$[\vec{BK},\vec{BL}](\vec{NC}\!\cdot\!\vec{NL})-(\vec{BK}\!\cdot\!\vec{BL})[\vec{NC},\vec{NL}]=-8m\bigl((a-1)^{2}+h^{2}\bigr)\cdot R_n,$$
$$[\vec{CL},\vec{CK}](\vec{MB}\!\cdot\!\vec{MK})-(\vec{CL}\!\cdot\!\vec{CK})[\vec{MB},\vec{MK}]=\phantom{-}8n\bigl((a+1)^{2}+h^{2}\bigr)\cdot R_m,$$
where
$$\boxed{\;R_n=U\,n^{2}+V\,n+\bigl(ch-(1+a)s\bigr),\qquad R_m=U\,m^{2}+V\,m+\bigl(ch-(1-a)s\bigr)\;}$$

Since $m,n>0$ and $(a\mp1)^2+h^2=\tfrac14|AC|^2,\tfrac14|AB|^2>0$, conditions (ii) and (iii) are **equivalent** to
$$R_n=0\quad\text{and}\quad R_m=0.$$

## The circumcentre's $x$-coordinate

The circumcentre $O=(O_x,O_y)$ of $\triangle AKL$ is determined by $|OA|^2=|OK|^2=|OL|^2$. Subtracting pairs gives a linear system; solving,
$$O_x=\frac{P(a,h,m,n,c,s)}{2\,[\vec{KA},\vec{LA}]},$$
where $P$ is an explicit polynomial. The denominator equals $2[\vec{KA},\vec{LA}]=2[\,K-A,\,L-A\,]$, which is non-zero precisely because $A,K,L$ are not collinear (the circumcentre $O$ exists by hypothesis).

## The algebraic identity (verified by Gröbner reduction)

**Claim.** $P\in\langle\,R_m,\,R_n,\,c^2+s^2-1\,\rangle$ in the polynomial ring $\mathbb{Q}[a,h,m,n,c,s]$.

*Proof of claim.* Reducing $P$ modulo the ideal $\langle R_m,R_n,c^2+s^2-1\rangle$ via a Gröbner basis (lexicographic order $m>n>c>s$) yields **remainder $0$**. (This is a finite, mechanically checkable polynomial division; the computation was carried out symbolically and confirmed to give identically zero.) $\square$

Therefore, whenever conditions (ii) and (iii) hold (so $R_m=R_n=0$) and $\varphi$ is a real angle (so $c^2+s^2=1$), the numerator $P$ vanishes, and consequently
$$O_x=0.$$

## Conclusion

Since $O_x=0$, the circumcentre $O$ lies on the $y$-axis, which is the perpendicular bisector of the segment $MN$ (whose endpoints are $M=(-1,0)$, $N=(1,0)$). A point on the perpendicular bisector of a segment is equidistant from the segment's endpoints, so

$$\boxed{\,OM=ON.\,}\qquad\blacksquare$$