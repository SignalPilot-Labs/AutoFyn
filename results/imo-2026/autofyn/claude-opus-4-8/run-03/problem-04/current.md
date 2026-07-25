## Status
solved

## Approaches tried
- lattice-invariant-180 — **solved** (APPROVE). Mod-θ lattice invariant. Necessity: Shan-Yu keeps an off-lattice child via a 4-case mod-θ covering argument; sufficiency: double θ-plant (both children carry a multiple of θ, using 180≡0) then forced descent kθ→(k−1)θ down to θ. Both directions rigorous.
- angle-sum-anchor — **solved** (APPROVE). Independent presentation of the same characterization via the supplementary-angle (180) anchor: Covering Lemma + Double-plant Lemma. Owns the explicit answer tabulation and refutation of both wrong conjectures.
- reduce-to-2theta — not built this round.

## Current best
Full characterization proved both directions. See Full proof.

## Full proof

### 0. Answer

Mulan can guarantee victory in finitely many steps **if and only if θ divides 180°**, i.e. iff
$180/\theta$ is a positive integer. The winning set is $\{\theta=180^\circ/n : n\in\mathbb{Z},\ n\ge 2\}=\{90,60,45,36,30,180/7,22.5,20,18,\dots\}$. Every winning θ is ≤ 90°; but ≤ 90° is not sufficient (e.g. θ=40,50,70,25 are ≤90 yet ∤180, so losses), and the criterion is divisibility of 180, not 90 (e.g. θ=60 ∤ 90 but 60|180, a win). All angles in degrees; a triangle is nondegenerate (three angles strictly in (0,180) summing to 180).

### 1. One-cut algebra

Triangle $A,B,C$ with angles $\alpha,\beta,\gamma$. Mulan picks a point $P$ (not a vertex) on a side, say $BC$, and cuts to the opposite vertex $A$; this splits $\alpha$ into $x=\angle BAP\in(0,\alpha)$ and $\alpha-x$. By angle-sum the two children are
$$\text{child}_1=\{x,\ \beta,\ 180-x-\beta\},\qquad \text{child}_2=\{\alpha-x,\ \gamma,\ x+\beta\},$$
where $\angle APB=180-x-\beta$ and $\angle APC=180-\gamma-(\alpha-x)=x+\beta$ (using $\alpha+\gamma=180-\beta$). The two cut-point angles are **supplementary**: $(180-x-\beta)+(x+\beta)=180$. Mulan freely chooses which vertex to split (labels permute) and $x\in(0,\alpha)$; Shan-Yu discards one child.

**Non-degeneracy.** For any $x\in(0,\alpha)$ all six angles lie strictly in $(0,180)$: $x,\beta,\alpha-x,\gamma>0$; $180-x-\beta>180-\alpha-\beta=\gamma>0$ and $<180$; $0<\beta<x+\beta<\alpha+\beta=180-\gamma<180$. Every cut with $x\in(0,\alpha)$ is legal.

Call $\varphi$ **on-lattice** if $\varphi\in\theta\mathbb{Z}=\{k\theta:k\in\mathbb{Z}_{\ge1}\}$, i.e. $\varphi\equiv 0\pmod\theta$. Mulan wins exactly when an angle equals $\theta$; on-lattice is a superset of that.

### 2. Necessity: θ ∤ 180 ⟹ Shan-Yu wins

Shan-Yu maintains **Invariant $I$: no angle is on-lattice** (so in particular no angle equals θ; the game never stops).

**Base.** Start $\mathcal{T}_0=(\theta/2,\theta/2,180-\theta)$: valid ($\theta<180$), and $I$ holds — $\theta/2=k\theta$ needs $k=1/2\notin\mathbb{Z}$; $180-\theta=k\theta$ needs $180=(k+1)\theta$, i.e. $\theta\mid180$, excluded.

**Covering Lemma (certified, `lemmas/lattice-covering.md`).** If $\theta\nmid180$ and $\alpha,\beta,\gamma$ are all off-lattice, then for every cut vertex and every $x\in(0,\alpha)$ at least one child is entirely off-lattice. *Proof.* Suppose both children contain an on-lattice angle. As $\beta$ is off-lattice, child$_1$ forces $x\equiv0$ or $x\equiv180-\beta$; as $\gamma$ is off-lattice, child$_2$ forces $x\equiv\alpha$ or $x\equiv-\beta$ (mod θ). The four combinations give: (i) $\alpha\equiv0$; (ii) $\beta\equiv0$; (iii) $\alpha+\beta\equiv180\Rightarrow\gamma\equiv0$; (iv) $180\equiv0\Rightarrow\theta\mid180$. Each contradicts a hypothesis. So some child is off-lattice. ∎ (Symmetric under relabeling the apex, so it holds for all three cut-vertex choices.)

Shan-Yu keeps the off-lattice child (nondegenerate by §1). By induction $I$ holds forever, so Mulan never gets an angle θ. This covers all $\theta>90$ (then $180/\theta<2$, integer only if $=1$, i.e. $\theta=180$, excluded) and all $\theta\le90$ with $\theta\nmid180$.

### 3. Sufficiency: θ | 180 ⟹ Mulan wins

Let $n=180/\theta\ge2$, so $\theta\le90$. Assume the current triangle has no angle $=\theta$ (else already won).

**3a. θ=90 (n=2).** At most one angle is $\ge90$, so at least two are acute. Pick apex $A$ with both neighbours $\beta,\gamma$ acute (the obtuse vertex if obtuse, any if acute). Cut $x=90-\beta$: $x>0$ ($\beta<90$); $x<\alpha$ since $\alpha+\beta=180-\gamma>90$ ($\gamma<90$). Children $\{90-\beta,\beta,90\}$ and $\{90-\gamma,\gamma,90\}$ both have a $90°$ angle. Mulan wins in one move (the altitude from $A$).

**3b. θ≤60 (n≥3).** Let $\alpha$ be the largest angle. Then $\alpha>\theta$: if $\theta<60$, $\alpha\ge60>\theta$; if $\theta=60$, $\alpha\ge60$ and $\alpha=60$ forces equilateral (angle $60=\theta$, game already stopped), so $\alpha>60$.

*Double plant.* Cut the largest vertex (neighbour $\beta$) at $x=m\theta-\beta$, $m=\lfloor\beta/\theta\rfloor+1$. Then $x>0$ ($m\theta>\beta$) and $x\le\theta<\alpha$, so $x\in(0,\alpha)$. Child$_2$ angle $x+\beta=m\theta$; child$_1$ angle $180-x-\beta=(n-m)\theta$ (uses $180=n\theta$). Both children carry a multiple of θ with multiplier in $[1,n-1]$ (since $m\theta=x+\beta<\alpha+\beta<180$). Whichever Shan-Yu keeps has an angle $k\theta$, $1\le k\le n-1$.

*Forced descent.* If $k=1$ Mulan has won. If $k\ge2$, cut the $k\theta$-vertex (neighbours $\beta',\gamma'$) at $x=\theta$ (legal, $0<\theta<k\theta$): child$_1=\{\theta,\beta',180-\theta-\beta'\}$ contains θ; child$_2=\{(k-1)\theta,\gamma',\theta+\beta'\}$. If Shan-Yu keeps child$_1$ Mulan wins; else the survivor has angle $(k-1)\theta$ (nondegenerate: $(k-1)\theta>0$, $\theta+\beta'=180-(k-1)\theta-\gamma'\in(0,180)$). The multiplier strictly decreases by 1 each move, so within $\le k-1$ moves it reaches θ. Total $\le 1+(n-2)=n-1$ moves.

### 4. Verification

Both directions proven, so **Mulan wins ⟺ θ | 180**, winning set $\{180/n:n\ge2\}$. Checks: θ=90 (one-move altitude), θ=60 on $(100,30,50)$ — plant $x=30$ gives $\{30,30,120\},\{70,50,60\}$ both on-lattice, then bisect $120$ to reach $60=\theta$. Losses θ=40,50,70,25 (≤90, ∤180) by §2 from $(\theta/2,\theta/2,180-\theta)$. Refutes "θ≤90 suffices" (θ=40 loses) and "θ|90" (θ=60|180 but ∤90 wins). Both load-bearing computations independently brute-verified over ~20k–30k random cases per θ with zero failures. $\qquad\blacksquare$
