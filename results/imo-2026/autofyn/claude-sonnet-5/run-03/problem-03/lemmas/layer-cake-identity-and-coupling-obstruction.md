# Certified (round 4): Layer-cake identity, per-piece additivity, and the Coupling Obstruction

Certified from `approaches/layer-cake-parity-reframing.md` (round 4, new
approach this round). Proof-reviewer independently re-verified the Coupling
Obstruction's exact worked example by rational arithmetic
(`bisect p2 alone`: `AltSum` goes `1/3 -> 7/15`, i.e. `+2/15`;
`bisect p2 after bisecting p1`: `AltSum` goes `1/5 -> 1/15`, i.e. `-2/15`
— exact match to the source file).

**Lemma 1 (Layer-cake identity).** For any finite multiset $X$ of positive
reals and $N_X(t):=\#\{x\in X:x\ge t\}$: $\mathrm{AltSum}(X)=\int_0^\infty
\mathbf1[N_X(t)\text{ odd}]\,dt$. Elementary swap-sum-and-integral +
telescoping argument.

**Lemma 2 (Per-piece additivity).** For a refinement $M=F_1\cup\cdots\cup
F_k$ of a partition $p_1,\dots,p_k$: $N_M(t)=\sum_i n_i(t)$, and
$n_i(t)=0$ for $t>p_i$. Elementary (multiset union is disjoint
concatenation).

**Corollary (exact reduction).** $T(n)$ is exactly equivalent (identity
chain, no relaxation) to a threshold-parity-measure statement
$\mathrm{T}'(n)$: $\int_0^\infty\mathbf1[\sum_i n_i(t)\text{ odd}]\,dt\ge
1/(2^{n+1}-1)$ for every admissible refinement.

**Lemma 3 (Single-cut marginal effect).** Bisecting a whole piece $p$ into
$a\ge b$ ($a+b=p$) changes its own threshold-count contribution by exactly
$+1$ on $(0,b]$ and $-1$ on $(a,p]$ (equal-length intervals).

**Proposition (Coupling Obstruction).** There is an exact ($n=3$, $D=15$)
worked example where the same cut (bisect $p_2$) has marginal
$\Delta\mathrm{AltSum}=+2/15$ applied alone, but $-2/15$ applied after a
different cut (bisect $p_1$) has already been made. This rigorously rules
out any proof mechanism for this framing's remaining gap that assigns cuts
independent, piece-local bounds (a genuine negative result, not merely an
unproved gap) — the correct bound must be a joint function of the whole cut
configuration.

**Status.** This is a genuinely new, independent framing (does not peel a
maximum element, unlike the other three lower-bound approaches) with a
fully proved exact reduction and a fully proved obstruction to its most
natural closing mechanism. $T(n)$ for $n\ge3$ remains open under this
framing.

**Reusable by:** any approach wanting an alternative (non-peel-based) exact
reformulation of the lower-bound target, or wanting a documented dead end
for "independent per-cut budget" proof strategies.
