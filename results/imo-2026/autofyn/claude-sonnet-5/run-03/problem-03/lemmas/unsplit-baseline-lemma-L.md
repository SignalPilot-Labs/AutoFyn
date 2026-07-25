# Lemma L (Unsplit-Baseline)

Certified round 9. Proved in `approaches/greedy-reduction-geometric.md`
(round 9, Section 13.1).

**Statement.** Let $m\ge2$, $k\ge2$. Let $B''=\{b_3,\dots,b_k\}$ have the
Dominance-Chain property at level $m-2$ (so $\mathrm{sum}(B'')\le2^{m-2}$),
and let $S''$ be a refinement of $\Gamma_{m-2}$ (levels $0,\dots,m-2$) in
which the top $k-1$ levels ($m-2,\dots,m-k$) are left unsplit. Suppose
$\{b_2\}\cup B''$ has the Dominance-Chain property at level $m-1$ (so
$\mathrm{sum}(\{b_2\}\cup B'')=b_2+\mathrm{sum}(B'')\le2^{m-1}$). Then, if the
value $2^{m-1}$ (level $m-1$) is left **unsplit** and merged in with $S''$
and $B''$,
$$\mathrm{OddSum}\bigl(S''\cup B''\cup\{2^{m-1}\}\bigr)\ \ge\ 2^{m-1}\ \ge\ b_2+\mathrm{sum}(B'').$$

**Proof.** Apply the already-certified **Theorem 7a**
(`approaches/greedy-reduction-geometric.md`, Section 10.1: for $m'\ge1$,
$b_1\ge2^{m'-1}$, and $S$ any refinement of $\Gamma_{m'-1}$,
$\mathrm{OddSum}(\{b_1\}\cup S)\ge b_1$ — proved directly from the
Global-max Peeling Lemma since $b_1=\max(\{b_1\}\cup S)$ and
$\mathrm{EvenSum}\ge0$) with parameter $m':=m-1$ and $b_1:=2^{m-1}$. The
hypothesis $b_1\ge2^{m'-1}=2^{m-2}$ holds ($2^{m-1}>2^{m-2}$), and $S''$ is
by construction a refinement of $\Gamma_{m'-1}=\Gamma_{m-2}$, so
$$\mathrm{OddSum}(\{2^{m-1}\}\cup S'')\ \ge\ 2^{m-1}.$$
Apply the already-certified **Theorem 13** (General Insertion
Monotonicity, `lemmas/insertion-monotonicity-theorems-12-13.md`): for any
finite multisets $N,R$ of positive reals, $\mathrm{OddSum}(N\cup R)\ge
\mathrm{OddSum}(N)$, with $N:=\{2^{m-1}\}\cup S''$, $R:=B''$:
$$\mathrm{OddSum}\bigl(\{2^{m-1}\}\cup S''\cup B''\bigr)\ \ge\
\mathrm{OddSum}(\{2^{m-1}\}\cup S'')\ \ge\ 2^{m-1}.$$
Finally $b_2+\mathrm{sum}(B'')\le2^{m-1}$ is exactly the Dominance-Chain
hypothesis on $\{b_2\}\cup B''$. $\blacksquare$

**Reviewer verification.** Independently traced both certified inputs
(Theorem 7a, Theorem 13) and confirmed the hypotheses of each are met
exactly as invoked (Theorem 7a's refinement requirement on $S''$, Theorem
13's total absence of any hypothesis on $R=B''$). The chain is two
one-line applications with no gap. Verified the elementary algebraic fact
$2^{m-1}>2^{m-2}$ for $m\ge2$ by inspection.

**What this does and does not resolve.** This isolates the entire
remaining difficulty of Open Sub-Problem B (Level-Absorption, the
cut-budget-corrected version, `approaches/greedy-reduction-geometric.md`
Section 11.1) to a single "re-splitting degradation" question: how much
can $\mathrm{OddSum}(M'\cup P)$ fall short of
$\mathrm{OddSum}(M'\cup\{2^{m-1}\})$ when $2^{m-1}$ is actually split into
$P=\{\mu_1\}\cup R_1$ instead of left whole, given the explicit slack
$\Sigma:=2^{m-1}-b_2-\mathrm{sum}(B'')\ge0$ this lemma provides. This
lemma does **not** itself close Level-Absorption (the degradation question
is open); it is a genuinely reusable baseline fact, not a full solution.
