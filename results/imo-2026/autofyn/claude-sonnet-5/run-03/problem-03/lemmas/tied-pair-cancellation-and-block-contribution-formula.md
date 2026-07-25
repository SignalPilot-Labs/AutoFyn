## Source
`approaches/self-similar-induction-on-n.md`, round 19. Certified by the
round-19 proof-reviewer after independent re-derivation from scratch (own
exact-`Fraction` scripts, not reusing the builder's).

## Lemma TPC (Tied-Pair Cancellation)

Let $M$ be a finite multiset of positive reals and suppose the value $x$
occurs in $M$ with multiplicity *exactly* $2$. Let $M'=M\setminus\{x,x\}$.
Then $\mathrm{AltSum}(M)=\mathrm{AltSum}(M')$, where $\mathrm{AltSum}$
denotes the true alternating sum $m_1-m_2+m_3-\cdots$ of $M$ sorted in
weakly decreasing order.

*Proof.* Sort $M$ in weakly decreasing order. Since no other element of
$M$ equals $x$, the two copies of $x$ occupy two consecutive ranks
$i,i+1$; these ranks have opposite parity, so their combined contribution
to $\mathrm{AltSum}(M)$ is $0$. Deleting these two positions shifts every
rank $r>i+1$ down to $r-2$ (same parity), leaving all other terms' signs
unchanged. Hence $\mathrm{AltSum}(M)=\mathrm{AltSum}(M')$. $\blacksquare$

*Independent verification.* Own exact-`Fraction` script, 30,000 random
trials (base multiset of distinct values plus an exact-multiplicity-2
pair inserted at a fresh value), zero violations.

## Lemma BCF (Block-Contribution Formula)

Let $M$ be a finite multiset of positive reals, partitioned into "levels"
of distinct values $v_1>v_2>\cdots>v_L>0$ with multiplicities
$t_1,\dots,t_L\ge1$. For each $i$ let $C_i:=\sum_{i'<i}t_{i'}$ (the number
of elements of $M$ strictly greater than $v_i$). Then
$$\mathrm{AltSum}(M)=\sum_{i:\,t_i\text{ odd}}(-1)^{C_i}v_i.$$

*Proof.* Induction on $\sum_i t_i$, base case all $t_i=1$ immediate from
the definition; inductive step applies Lemma TPC to reduce some
$t_{i_0}\ge2$ by $2$, which changes no other level's $C_i$ parity.
$\blacksquare$

**Corollary (even blocks are free).** If $t_i$ is even for some level
$i$, that level contributes exactly $0$ to $\mathrm{AltSum}(M)$
regardless of its value $v_i$ or its position among the other levels.

*Independent verification.* Own exact-`Fraction` scripts: 20,000 random
trials of the general formula against direct computation (zero
mismatches); 10,000 random trials of the corollary (forcing a random
level to even multiplicity and comparing $\mathrm{AltSum}$ with/without
that level present), zero mismatches.

## Lemma LNI (Local Non-Improvement)

Suppose $R$ is a feasible configuration for GCH($k$) (finite multiset,
$\max(R)\le\mathrm{cap}=2^{k-1}$, $\mathrm{sum}(R)=S$ fixed) and $R$ has
two coordinates $r_i\ne r_j$ with (a) both strictly between two
consecutive values of $\Gamma_{k-1}\cup\{0,\mathrm{cap}\}$ that bound
them, and (b) opposite rank parity in the sorted order of
$R\cup\Gamma_{k-1}$. Then $R$ does not locally minimize
$\mathrm{AltSum}(R\cup\Gamma_{k-1})$ subject to $\mathrm{sum}(R)=S$: the
mass-preserving perturbation $r_i\mapsto r_i+t,\ r_j\mapsto r_j-t$
changes $\mathrm{AltSum}$ at nonzero rate $c_i-c_j$ (the rank-parity
signs) for small enough $t$ that no rank-crossing occurs.

*Proof.* On the open neighborhood with no rank-crossing,
$\mathrm{AltSum}(R\cup\Gamma_{k-1})$ is affine in $(r_i,r_j)$ with
$r_i+r_j$ fixed, with $t$-derivative $c_i-c_j\ne0$ by hypothesis (b).
$\blacksquare$

**Consequence (Vertex Reduction).** At any true minimizer, every pair of
simultaneously-free coordinates must share the same rank parity.

*Independent verification.* Own exact-`Fraction` worked examples
($k=3$, $\Gamma_2=\{4,2,1\}$): confirmed the rate formula
$\Delta\mathrm{AltSum}=t\cdot(c_i-c_j)$ exactly at a concrete
opposite-parity pair ($r_i=3.5$ at rank 2, $r_j=0.5$ at rank 5,
$c_i-c_j=-2$; perturbations $t=\pm0.1$ matched the predicted linear
change to the digit).

## Scope note (what these lemmas do NOT establish)

These are general-purpose elementary tools about $\mathrm{AltSum}$ of a
finite multiset (Lemma TPC/BCF) and a first-order necessary condition on
minimizers of a fixed constrained optimization (Lemma LNI). They do
**not**, by themselves, establish the GCH($k$) general lower bound
$\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ for every feasible $R$ — that
remains open (see the source file's round-19 section, "the lower-bound
direction: partial progress, honest open gap").
