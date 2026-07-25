# Lemma: lattice-covering (mod-θ covering)

Status: CERTIFIED by proof-reviewer (round 2). Statement correct, proof sorry-free, the four-case mod-θ exhaustion is complete (verified independently, incl. 20k-case brute check across θ∈{40,50,70,25,80,100,180/7,140,17,23.3}). No stronger than proved.

## Statement
Let $0<\theta<180$ with $180/\theta \notin \mathbb{Z}$ (i.e. $\theta\nmid 180$). Suppose a
triangle has angles $\alpha,\beta,\gamma$ (summing to $180$), none of which is an integer
multiple of $\theta$. Then for **every** choice of cut vertex (with angle $\alpha$ and neighbours
$\beta,\gamma$) and **every** cut parameter $x\in(0,\alpha)$, at least one of the two children
$$\text{child}_1=\{x,\ \beta,\ 180-x-\beta\},\qquad \text{child}_2=\{\alpha-x,\ \gamma,\ x+\beta\}$$
has all three of its angles off the lattice $\theta\mathbb{Z}=\{k\theta:k\in\mathbb{Z}_{\ge1}\}$.

## Proof
Call an angle $\varphi$ *on-lattice* if $\varphi\equiv 0\pmod\theta$ (equivalently $\varphi/\theta
\in\mathbb{Z}$; for $\varphi\in(0,180)$ this means $\varphi$ is a positive multiple of $\theta$).
By hypothesis $\alpha,\beta,\gamma$ are all off-lattice.

Suppose for contradiction that **both** children contain an on-lattice angle.

In $\text{child}_1$, $\beta$ is off-lattice, so the on-lattice angle is $x$ or $180-x-\beta$;
hence $x\equiv0$ or $x\equiv180-\beta\pmod\theta$.

In $\text{child}_2$, $\gamma$ is off-lattice, so the on-lattice angle is $\alpha-x$ or $x+\beta$;
hence $x\equiv\alpha$ or $x\equiv-\beta\pmod\theta$.

So $(x\equiv0\ \lor\ x\equiv180-\beta)\wedge(x\equiv\alpha\ \lor\ x\equiv-\beta)\pmod\theta$,
which is exactly four cases (mod $\theta$ throughout):

1. $x\equiv0,\ x\equiv\alpha\Rightarrow \alpha\equiv0$: $\alpha$ on-lattice — contradiction.
2. $x\equiv0,\ x\equiv-\beta\Rightarrow \beta\equiv0$: $\beta$ on-lattice — contradiction.
3. $x\equiv180-\beta,\ x\equiv\alpha\Rightarrow \alpha+\beta\equiv180$. Since $\alpha+\beta=180-\gamma$,
   $180-\gamma\equiv180$, so $\gamma\equiv0$: $\gamma$ on-lattice — contradiction.
4. $x\equiv180-\beta,\ x\equiv-\beta\Rightarrow 180\equiv0$: $\theta\mid180$ — contradiction.

All four cases contradict the hypotheses, so both-children-on-lattice is impossible. Hence at
least one child is entirely off-lattice. The four cases exhaust all $x\in(0,\alpha)$, so the
conclusion holds for every $x$ and every cut-vertex choice. $\qquad\blacksquare$

## Consequence
Under the invariant "no angle on-lattice," Shan-Yu can always keep an off-lattice child (which
is nondegenerate: all six child angles lie strictly in $(0,180)$ for $x\in(0,\alpha)$), so the
invariant is preserved forever and no angle ever equals $\theta$. This is the necessity half of
"Mulan wins $\iff\theta\mid180$."
