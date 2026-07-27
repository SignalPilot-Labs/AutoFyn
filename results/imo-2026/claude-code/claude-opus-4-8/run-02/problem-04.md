Setting up the framework

  I'll track only the angles of $\mathcal T$. Label the three angles $(p,q,r)$ with $p+q+r=180^\circ$.

  The cut, in terms of angles. A cut goes from a vertex (the apex, angle $r$) to a point $P$ on the opposite side, splitting the apex
  angle as $r = x+y$ with $x,y>0$. The two pieces are

  $$C_1=(p,;x,;180-p-x),\qquad C_2=(q,;y,;180-q-y),\quad x+y=r .$$

  So Mulan picks which angle is the apex and the split $x$; Shan‑Yu keeps $C_1$ or $C_2$. Note the two "new" angles satisfy
  $(180-p-x)+(180-q-y)=180$.

  Claim. Mulan can force a win iff $\theta=\dfrac{180^\circ}{n}$ for some integer $n\ge 2$ — equivalently, iff $180^\circ/\theta$ is an 
  integer.

  Throughout, write $\bar a = a \bmod \theta$, and note $p+q+r=180$, so $\bar p+\bar q+\bar r\equiv \overline{180}=:\delta \pmod\theta$.

  ---
  If $\theta \nmid 180^\circ$ (so $\delta\neq 0$): Shan‑Yu survives forever

  Shan‑Yu keeps the invariant: no angle is a positive multiple of $\theta$ (i.e. every $\bar a\neq 0$). Initially he picks a triangle
  avoiding the finitely many multiples of $\theta$ (e.g. a small perturbation of equilateral).

  Suppose the current angles satisfy $\bar p,\bar q,\bar r\neq 0$, and Mulan cuts apex $r$ with split $x$. Then:

  - $C_1$ contains a multiple of $\theta$ $\iff \bar x\in{0,\ \delta-\bar p}$  (from $\bar x\equiv0$ or $\overline{180-p-x}\equiv 0$);
  - $C_2$ contains a multiple of $\theta$ $\iff \bar x\in{\bar r,\ -\bar p}$  (using $\bar q+\bar r\equiv\delta-\bar p$).

  For Mulan to trap Shan‑Yu she needs ${0,\delta-\bar p}\cap{\bar r,-\bar p}\neq\varnothing$. Checking all four cases:
  $$0=\bar r,\quad 0=-\bar p,\quad \delta-\bar p=\bar r\ (\Leftrightarrow \bar q=0),\quad \delta-\bar p=-\bar p\ (\Leftrightarrow
  \delta=0),$$
  each forces some $\bar a=0$ or $\delta=0$ — all excluded. Hence the two sets are disjoint, so for every apex choice and every $x$, at
  least one child has all residues nonzero. Shan‑Yu keeps that child, preserving the invariant.

  (Real‑geometry constraints only restrict Mulan, so this survival argument is unaffected.) Since no angle is ever a multiple of
  $\theta$, no angle ever equals $\theta$: Mulan never wins. $\blacksquare$

  ---
  If $\theta=180^\circ/n$ (so $\delta=0$): Mulan wins
  
  Step 2 — any angle equal to $k\theta$ is winning. Induct on $k$ ($1\le k\le n-1$).
  - $k=1$: an angle equals $\theta$, the game stops with Mulan's win.
  - $k\ge2$: make $k\theta$ the apex and split it as $\theta+(k-1)\theta$. Then $C_1$ has an angle $\theta$ (immediate win) and $C_2$
  has an angle $(k-1)\theta$ (winning by induction). Both children are winning, so the triangle is. $\square$

  Step 1 — from any triangle, one cut makes both children "good" (have an angle that is a positive multiple of $\theta$).

  Case $n=2$ ($\theta=90^\circ$). Cut the altitude from the largest‑angle vertex. Its neighbors are acute, so the foot is interior, and
  both children are right triangles — each has a $90^\circ=\theta$ angle. Mulan wins in one move.

  Case $n\ge3$ ($\theta\le 60^\circ$). If some angle is already a multiple of $\theta$, use Step 2. Otherwise take the apex to be the
  largest angle $L\ge 60^\circ$; since no angle is a multiple of $\theta$ we get $L>\theta$. Choose
  $$x=\big((-p)\bmod\theta\big)\in(0,\theta)\subseteq(0,L).$$
  Because $\delta\equiv0$:
  $$\overline{180-p-x}\equiv -\bar p-\bar x\equiv 0,\qquad \overline{180-q-(r-x)}=\overline{p+x}\equiv 0 .$$
  So both children have a third angle that is a positive multiple of $\theta$ (hence in ${\theta,\dots,(n-1)\theta}$) — both are good,
  hence winning by Step 2.

  In every case, from any starting triangle Mulan forces a winning position, so she wins in finitely many steps regardless of Shan‑Yu's
  initial triangle and choices. $\blacksquare$

  ---
  Conclusion
  
  $$\boxed{;\text{Mulan can guarantee victory }\iff\ \theta=\dfrac{180^\circ}{n}\ \text{for some integer } n\ge 2;}$$

  i.e. exactly when $\theta$ divides $180^\circ$: $\theta\in{90^\circ,60^\circ,45^\circ,36^\circ,30^\circ,\dots}$. For all other
  $\theta$ (including every $\theta>90^\circ$, since no such angle divides $180^\circ$), Shan‑Yu can avoid $\theta$ forever.

  Verification checks: $\theta=90^\circ$ (altitude, 1 move) ✓; $\theta=60^\circ$ e.g. $(50,70,60)$ splits to children containing
  $120^\circ$ and $60^\circ$, and any $120^\circ$ splits into $60^\circ+60^\circ$ ✓; $\theta=120^\circ$ and $\theta=50^\circ$ — the two
  "danger sets" for $x$ are disjoint, so Shan‑Yu always has a safe child ✓.

✻ Worked for 13m 53s