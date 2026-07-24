# Safe-Window Lemma

**Certified:** round 8, from `greedy-halving-adversary.md` Lemma 17.
Reviewer confirmed the induction is a straightforward, correct fact.

**Statement.** For the $n$-ladder ($n\ge2$), let $\tau=\{p_2,\dots,p_{n+1}\}$
and $G'$ any legal refinement of $\tau$ (any finite sequence of cuts, any
order, any pattern). Then every element of $G'$ satisfies $g\le p_2$.

**Proof.** Induction on the number of cuts. Base case: $G'=\tau$, max
element $p_2$. Step: splitting a current piece $s\le p_2$ into positive
fragments $f_1,f_2$ with $f_1+f_2=s$ gives $f_1,f_2\le s\le p_2$.

**Scope.** General (any number/pattern of cuts on the tail); this is the
mechanism silently inside the already-certified
`half-window-vanishing-lemma`, restated standalone.
