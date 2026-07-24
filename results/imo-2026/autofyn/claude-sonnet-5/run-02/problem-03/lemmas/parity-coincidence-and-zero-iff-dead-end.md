# Parity Coincidence Lemma, Zero-Iff Lemma, and the peel-by-$\ell$ dead end

**Certified:** round 8, from `rank-tie-vertex-reduction.md` §7.1–7.2.
Reviewer independently confirmed both proofs are correct elementary facts
(three-line double-counting argument; standard telescoping-positivity
argument for the alternating sum of a strictly decreasing positive
sequence).

**Parity Coincidence Lemma.** For every finite multiset $S$,
$\ell(S)\equiv|S|\pmod2$, where $\ell(S):=|S'|$ is the size of the
odd-run-reduced multiset (`odd-run-reduction-lemma`). Proof: reducing
$|S|=\sum_v\mu(v)$ mod $2$ term-by-term gives $\sum_v(\mu(v)\bmod2)$, which
counts exactly the values of odd multiplicity, i.e. $\ell(S)$.

**Zero-Iff Lemma.** For every finite multiset $S$ of positive reals,
$\ell(S)=0\iff A(S)=0$. Proof: ($\Rightarrow$) trivial. ($\Leftarrow$) if
$\ell(S)\ge1$, group $A(S')$'s alternating sum into consecutive pairs
(each strictly positive since $S'$ is strictly decreasing) plus possibly one
strictly positive leftover term; the total is a sum of finitely many
strictly positive terms, hence $>0$.

**Consequence (dead end, recorded).** These two facts jointly prove that
induction on $\ell(S)$ (in place of $N=|S|$) for the general $c_1\ge2$
lower-bound gap **cannot escape the parity obstruction** that has
independently stalled peel-the-min (`rank-pigeonhole-budget`) and
peel-the-max (`rank-tie-vertex-reduction`'s own round-7 attempt): the
even/odd case split is provably the *same bit* whichever variable indexes
the induction, and the naive "free" base case $\ell=0$ is not actually
free — ruling it out is equivalent to proving $A(S)\ne0$ for every legal
response, itself unestablished. Any future round should not re-attempt a
peel-by-$\ell$ (single-element, paired-element, or reduced-multiset)
mechanism for this gap.

**Scope.** The two lemmas themselves are fully general (no dependence on
the ladder); the dead-end diagnosis is specific to this project's $c_1\ge2$
gap.
