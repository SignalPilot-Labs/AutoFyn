start: 03:23pm end: 4:11pm

## Answer

**Mulan can force a win if and only if $\theta$ divides $180^\circ$** — that is, if and only if $\dfrac{180^\circ}{\theta}$ is an integer, equivalently $\theta = \dfrac{180^\circ}{n}$ for some integer $n \ge 2$. So Mulan wins exactly for $\theta \in \{90^\circ, 60^\circ, 45^\circ, 36^\circ, 30^\circ, \dots\}$, and Shan‑Yu survives for every other $\theta$.

Throughout, all angles are measured in degrees and $\theta$ is fixed.

## Setup: the two pieces of a cut

Let a triangle have vertices with angles $X, Y, Z$ (so $X+Y+Z = 180$). A cut goes from a chosen vertex $X$ to a point $P$ on the opposite side $YZ$. Writing $\alpha = \angle YXP \in (0,X)$ (so $\angle ZXP = X-\alpha$), the two pieces are:

$$P_1 = \{\,Y,\ \alpha,\ 180-Y-\alpha\,\}, \qquad P_2 = \{\,Z,\ X-\alpha,\ Y+\alpha\,\},$$

since the apex angle at $P$ in $P_2$ is $180-Z-(X-\alpha) = Y+\alpha$. Mulan chooses the vertex $X$ and $\alpha\in(0,X)$; Shan‑Yu keeps one piece.

**Definitions.** Call an angle $\varphi$ a *multiple of $\theta$* if $\varphi = k\theta$ with $k$ a positive integer. Call a triangle **safe** if none of its three angles is a multiple of $\theta$. For a real $\varphi$ write $r(\varphi) = \varphi \bmod \theta \in [0,\theta)$; then $\varphi$ is a multiple of $\theta$ iff $r(\varphi)=0$, and a triangle is safe iff $r$ of each of its three angles is nonzero. Let

$$\rho := r(180) = 180 - \left\lfloor \tfrac{180}{\theta}\right\rfloor\theta \in [0,\theta), \qquad\text{so } \theta \mid 180 \iff \rho = 0 .$$

Since Mulan wins exactly when an angle equals $\theta$ (a multiple of $\theta$), **Mulan wins only if a multiple of $\theta$ ever appears as an angle.**

## Part 1: If $\theta \nmid 180$, Shan‑Yu survives forever

Shan‑Yu's strategy: start with a safe triangle and always keep a safe piece.

**A safe starting triangle exists:** choose any three positive angles summing to $180$, none a multiple of $\theta$ (e.g. perturb an equilateral triangle).

**Key invariant.** For any triangle in play, $r(X)+r(Y)+r(Z) \equiv X+Y+Z \equiv 180 \equiv \rho \pmod\theta$.

**Lemma (a safe piece always exists).** *If the current triangle is safe and $\rho \ne 0$, then for every legal cut at least one of $P_1,P_2$ is safe.*

*Proof.* Cut from $X$ (neighbors $Y,Z$) with $s := r(\alpha)$. Using $r(180)=\rho$, the residues of the pieces are
$$P_1:\ \{\,r(Y),\ s,\ \rho - r(Y) - s\,\}, \qquad P_2:\ \{\,r(Z),\ r(X)-s,\ r(Y)+s\,\}\pmod\theta.$$
Since the triangle is safe, $r(Y),r(Z)\ne 0$. Thus:
- $P_1$ has a zero residue $\iff s\equiv 0$ or $s\equiv \rho - r(Y)$;
- $P_2$ has a zero residue $\iff s\equiv r(X)$ or $s\equiv -r(Y)$.

If **both** pieces had a zero residue, one of four cases would hold:
1. $s\equiv 0 \equiv r(X)$ $\Rightarrow r(X)=0$, impossible;
2. $s\equiv 0\equiv -r(Y)$ $\Rightarrow r(Y)=0$, impossible;
3. $\rho - r(Y)\equiv r(X) \Rightarrow \rho \equiv r(X)+r(Y) \Rightarrow r(Z)\equiv 0$ (by the invariant), impossible;
4. $\rho - r(Y)\equiv -r(Y) \Rightarrow \rho\equiv 0$, excluded since $\rho\ne 0$.

So both pieces cannot simultaneously carry a zero residue; at least one piece is safe. $\qquad\blacksquare$

Shan‑Yu keeps that safe piece. By induction every triangle stays safe, so **no angle is ever a multiple of $\theta$**; in particular no angle ever equals $\theta$. Mulan never wins.

## Part 2: If $\theta \mid 180$, Mulan wins from every starting triangle

Here $\rho = 0$, i.e. $180\equiv 0\pmod\theta$. Note the largest divisor of $180$ that is $<180$ is $90$, so $\theta \le 90$.

**Lemma A (forcing a multiple of $\theta$ down to $\theta$).** *If some angle equals $m\theta$ with $m\ge 1$, Mulan wins in finitely many steps.*

*Proof.* If $m=1$ the triangle already has angle $\theta$ and Mulan has won. If $m\ge 2$, cut from the vertex of angle $m\theta$ with $\alpha=\theta$ (legal as $\theta< m\theta$). Then $P_1=\{Y,\theta,\dots\}$ contains $\theta$, and $P_2=\{Z,(m-1)\theta,\ Y+\theta\}$. If Shan‑Yu keeps $P_1$, Mulan wins; otherwise the special angle drops to $(m-1)\theta$. Repeating, $m$ strictly decreases, so after finitely many steps either Shan‑Yu hands over an angle $\theta$, or we reach $m=2$, where both pieces contain $\theta$ and Mulan wins. $\qquad\blacksquare$

**Lemma B (double‑zero move).** *If a triangle is safe, Mulan has a cut making **both** pieces contain a multiple of $\theta$.*

*Proof.* Let $X\ge 60$ be the largest angle, with other angles $Y,Z$; put $r_Y = r(Y)\in(0,\theta)$ (nonzero by safety). Set $\alpha_0 = \theta - r_Y \in (0,\theta)$; we check $\alpha_0 < X$:

- If $X \ge \theta$: then $\alpha_0 < \theta \le X$. ✓
- If $X < \theta$: all angles are $<\theta\le 90$, so their sum $180 < 3\theta$, forcing $\theta > 60$; with $\theta\mid 180,\ \theta\le 90$ this gives $\theta = 90$. Then $r_Y = Y$, and since $Z<90$, $X+Y = 180 - Z > 90$, so $X > 90 - Y = \alpha_0$. ✓

Now cut from $X$ with $\alpha = \alpha_0$. Using $180\equiv 0\pmod\theta$:
$$P_1:\ 180 - Y - \alpha_0 \equiv -r_Y - (-r_Y) = 0, \qquad P_2:\ Y + \alpha_0 \equiv r_Y + (-r_Y) = 0 \pmod\theta.$$
Each of these is a genuine positive angle, hence a positive multiple of $\theta$. So both pieces contain a multiple of $\theta$. $\qquad\blacksquare$

**Conclusion for Part 2.** Given any starting triangle: if it already contains a multiple of $\theta$, apply Lemma A. Otherwise it is safe; apply Lemma B, after which *whichever* piece Shan‑Yu keeps contains a multiple of $\theta$, and Lemma A finishes. Every stage terminates in finitely many steps (the multiple $m\theta<180$ bounds the number of shifts), so Mulan wins.

## Verification of consistency

- $\theta = 90^\circ$ ($n=2$): Lemma B is exactly the altitude from the largest vertex, splitting the triangle into two right triangles — an immediate win. ✓
- $\theta = 60^\circ$, triangle $(100,50,30)$: cut from $100$ with $\alpha = 60 - r(50) = 10$; pieces $\{50,10,120\}$ and $\{30,90,60\}$ both contain a multiple of $60$ ($120$ and $60$). ✓
- $\theta = 50^\circ$ ($\rho = 30 \ne 0$): from $(60,60,60)$, residues $(10,10,10)$ sum to $\rho$; any cut leaves a safe piece — Shan‑Yu survives. ✓

## Final answer

$$\boxed{\ \text{Mulan can guarantee victory} \iff \theta \text{ divides } 180^\circ,\ \text{i.e. } \theta = \frac{180^\circ}{n}\ \text{for some integer } n \ge 2.\ }$$

For all other $\theta$ (equivalently, whenever $180^\circ/\theta \notin \mathbb{Z}$), Shan‑Yu can play forever and Mulan cannot win.