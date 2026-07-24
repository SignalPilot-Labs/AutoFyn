# Lemma: Proposition 39 — Mass-Conservation Obstruction

**Source:** `approaches/greedy-halving-adversary.md`, round 25.

**Statement.** Fix $m\ge1$ and let $S$ range over legal $(\le m-1)$-cut
refinements of the unit $m$-ladder $q=(q_1,\dots,q_{m+1})$
($\mathrm{Total}(S)=1$ identically). Let $c$ range over $(0,q_1]$. There
is no fixed $k\ge0$ and fixed ladder instance $L_k$ of mass $\mu$ such
that $\{c\}\cup S$ is a legal Xiang-Yu response to $L_k$ for every $c$ in
an open subinterval of $(0,q_1]$ — i.e. the "literal substitution" route
($h(m)$ as a disguised instance of the standing general lower bound
$(\star_k)$) is false, for a structural (mass-conservation/injectivity)
reason that persists at every scale $k$.

**Proof.** Mass conservation: every legal response to $L_k$ has total mass
exactly $\mu$ (fixed). $\mathrm{Total}(\{c\}\cup S)=c+1$ is strictly
increasing (hence injective) in $c$, so at most one $c$ can satisfy
$c+1=\mu$ — contradicting "for every $c$ in an open interval." $\blacksquare$

Also identifies the *unique* exception ($c^\ast=q_1$, Claim (II)'s vertex),
where $\{q_1,q_1\}\cup S$ literal-cancels via the odd-run-reduction
identity before any $(\star_k)$-type substitution is needed — explaining
precisely why that one vertex (and no other) admits the shortcut.

**Independent verification.** The mass-conservation/injectivity argument
is elementary and was re-derived by hand by this reviewer; no computation
needed. Correct.

**Status.** Proved in full, general $m$, no gaps. A genuine negative
result (not a repeated assertion) — closes off the "$h(m)$ as $L(m)$
corollary" idea permanently; future rounds should not re-attempt it.

**Certified by:** proof-reviewer, round 25.
