# Chain Lemma (certified)

For any $\theta\in(0,180°)$: if the current triangle has an angle equal to $K\theta$ for
a positive integer $K$, then Mulan can force a win within at most $K-1$ further moves
(with $K=1$ meaning the triangle already has angle $\theta$, i.e. Mulan has already won).

**Proof.** Induction on $K$. Base case $K=1$: immediate. Inductive step $K\ge2$: cut the
$K\theta$-angle vertex (as apex) with cut-parameter $x=\theta$ (valid since
$0<\theta<K\theta$). Using the single-cut formula — apex angle $A$ split at
$x\in(0,A)$ into child$_1=(x,B,180-x-B)$, child$_2=(A-x,C,B+x)$ where $B,C$ are the other
two current angles — taking $A=K\theta$, $x=\theta$ gives
child$_1=(\theta,B,180-\theta-B)$ (already has angle $\theta$: instant win if Shan-Yu
keeps it) and child$_2=((K-1)\theta,C,B+\theta)$ (has angle $(K-1)\theta$, apply the
induction hypothesis). Either choice forces a win within $\le 1+(K-2)=K-1$ moves.
$\blacksquare$

Source: certified from `results/imo-2026-04/approaches/interval-partition-topological.md`
(Lemma S1) and independently reproduced in `resonance-lattice-invariant.md` (Lemma 1);
certified by proof-reviewer round 2 after independent re-derivation. No hypothesis on
$\theta$ beyond $\theta\in(0,180°)$; reusable standalone.
