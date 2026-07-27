Solution

  Answer. Mulan can guarantee victory if and only if
  $$\theta = \frac{180^\circ}{n}\quad\text{for some positive integer } n.$$

  I verified this extensively via computation (exact fixed-point/game-tree analysis on rational grids at multiple resolutions,
  confirming the exact threshold for dozens of values including non-integer angles like $180/7$) before finding the proof below. Here is
  the complete argument.

  Setup
  
  If $P$ lies on side $BC$ of triangle $ABC$ and we set $x=\angle BAP\in(0,\angle A)$, elementary angle-chasing in triangles $ABP,ACP$
  gives:
  $$T_1=\triangle ABP:\ {B,\ x,\ 180-B-x},\qquad T_2=\triangle ACP:\ {C,\ A-x,\ B+x}.$$
  (Here $A,B,C$ denote both vertices and their angle measures, $A+B+C=180$.) These two formulas are all we ever use.

  ---
  Part 1: If $\theta=180^\circ/n$, Mulan wins in at most $n-1$ moves
  
  Lemma A. If the current triangle has an angle equal to $m\theta$ for an integer $1\le m\le n-1$, Mulan forces a win within $m-1$ 
  further moves, no matter what the other two angles are.

  Proof (strong induction on $m$). If $m=1$ the angle already equals $\theta$: done. If $m\ge 2$, let the apex be $A=m\theta$ (so
  $A>\theta$) with base angles $B,C>0$. Cut with $x=\theta$ (valid since $0<\theta<A$). Then
  $$T_1={B,\theta,180-B-\theta}\ \text{(contains }\theta\text{ — immediate win)},\qquad T_2={C,\ (m-1)\theta,\ B+\theta}.$$
  If Shan‑Yu keeps $T_2$, it contains the angle $(m-1)\theta$, and $1\le m-1<m$, so by induction Mulan wins within $(m-1)-1=m-2$ further
  moves. Either way she wins within $m-1$ moves total. $\blacksquare$

  Lemma B. From any triangle with no angle equal to $\theta$, Mulan can force, in one move regardless of Shan-Yu's choice, that the 
  resulting triangle has an angle equal to an exact integer multiple $j\theta$ ($1\le j\le n-1$).

  First, a triangle with no angle $=\theta$ always satisfies (I) some angle exceeds $\theta$, or (II) at least two angles are less than
  $\theta$ — otherwise all angles are $\le\theta$ while at least two are $\ge \theta$, forcing those to equal $\theta$ exactly, a
  contradiction.

  Case I: some angle $A>\theta$. Let $B,C$ be the other two. The interval $\left(\frac{C}{\theta},, n-\frac{B}{\theta}\right)$ has
  length $\frac{A}{\theta}>1$ (since $A+B+C=180=n\theta$), so it contains an integer $k$ (with automatically $1\le k\le n-1$). Take
  $x=180-B-k\theta\in(0,A)$ (this is exactly the condition $k$ satisfies). Then
  $$T_1={B,\ x,\ k\theta},\qquad T_2={C,\ A-x,\ (n-k)\theta}\quad(\text{using } B+x=180-k\theta=(n-k)\theta).$$
  Both contain an exact multiple of $\theta$.

  Case II: two angles $B,C<\theta$, third $A=180-B-C$. Since $\theta\le 90^\circ$ (as $n\ge2$), $B<\theta\le 180-\theta$, so
  $x:=180-B-\theta\in(0,A)$ is valid (using $C<\theta$ for the upper bound). Then
  $$T_1={B,x,\theta}\ (\text{immediate win if kept}),\qquad T_2={C,\ \theta-C,\ (n-1)\theta}.$$
  Again both branches contain a multiple of $\theta$ ($\theta$ itself, or $(n-1)\theta$). $\blacksquare$

  Conclusion. Apply Lemma B once (1 move), then Lemma A (at most $n-2$ more moves). Total: at most $n-1$ moves, for any starting
  triangle. So Mulan wins whenever $\theta=180^\circ/n$.

  ---
  Part 2: If $\theta \neq 180^\circ/n$ for every integer $n$, Shan-Yu wins forever
  
  For a real $y>0$, write ${y}\theta = y-\theta\lfloor y/\theta\rfloor\in[0,\theta)$ for its residue mod $\theta$; note ${y}\theta=0$
  iff $y$ is an integer multiple of $\theta$. Since $\theta \nmid 180$, $\delta:={180}_\theta\in(0,\theta)$ is nonzero.

  Shan-Yu's invariant (*): no angle of the current triangle is an integer multiple of $\theta$.

  Base case. Start with the equilateral triangle $(60^\circ,60^\circ,60^\circ)$. If $60=k\theta$ for an integer $k$, then $180=3\cdot
  60=3k\theta$, contradicting $\theta\nmid 180$. So $60$ is not a multiple of $\theta$, and (*) holds initially.

  Maintenance. Suppose (*) holds for the current triangle $A,B,C$, with residues $a={A}\theta,,b={B}\theta,,c={C}\theta$, all nonzero, 
  and $a+b+c\equiv\delta \pmod\theta$ (since $A+B+C=180$). Suppose Mulan cuts from apex $A$ with parameter $x$; let $\xi={x}\theta$.
  Using the formulas above:

  - $T_1={B,x,180-B-x}$ fails (*) iff $\xi\equiv 0$ or $\xi\equiv \delta-b \pmod\theta$ (since $b\ne0$ already).
  - $T_2={C,A-x,B+x}$ fails (*) iff $\xi\equiv a$ or $\xi\equiv -b \pmod\theta$ (since $c\ne0$ already).

  Both branches fail only if one of these coincidences holds:
  $$0\equiv a,\qquad 0\equiv -b,\qquad \delta-b\equiv a,\qquad \delta-b\equiv -b \pmod\theta.$$
  - $0\equiv a$ and $0\equiv -b$ are impossible since $a,b\ne 0$.
  - $\delta - b\equiv a$ means $a+b\equiv\delta$, i.e. (since $a+b+c\equiv\delta$) $c\equiv0$ — impossible.
  - $\delta-b\equiv -b$ means $\delta\equiv 0$ — impossible since $\theta\nmid180$.

  So no value of $x$ can defeat both branches simultaneously — Shan-Yu always has a safe choice. (By symmetry of $a,b,c$, the same holds
  for any choice of apex/labeling Mulan makes.) Thus (*) is maintained forever by induction.

  Since (*) in particular forbids any angle from ever equaling $\theta=1\cdot\theta$, Mulan never wins, so Shan-Yu survives
  indefinitely. $\blacksquare$

  ---
  Conclusion
  
  Combining both parts:
  $$\boxed{\text{Mulan can force a win if and only if } \theta = \dfrac{180^\circ}{n} \text{ for some positive integer } n.}$$

  (For such $\theta$ she wins in at most $n-1$ moves from any starting triangle; for all other $\theta$, Shan-Yu starting from the
  equilateral triangle survives forever.)

✻ Churned for 33m 12s