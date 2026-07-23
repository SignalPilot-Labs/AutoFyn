# Lattice Safety Invariant (certified)

Fix $\theta\in(0,180°)$ with $180°/\theta\notin\mathbb Z$ ("non-resonant"). Call a
triangle $(A,B,C)$ ($A+B+C=180°$) *safe* if none of $A,B,C$ lies in $\theta\mathbb Z$.
Then: for every safe triangle and every legal single-cut move of Mulan (any apex, any
labeling of the two base angles, any interior cut parameter $x$), **at least one of the
two resulting children is again safe.**

**Proof sketch (full proof in `interval-partition-topological.md` Lemma N1).** With apex
$A$ cut at $x\in(0,A)$: child$_1=(x,B,180-x-B)$, child$_2=(A-x,C,B+x)$. child$_1$'s
middle slot $B$ is always safe (given); child$_1$ is unsafe only if $x\in\theta\mathbb Z$
or $180-x-B\in\theta\mathbb Z$. In the first case, $A-x$ and $B+x$ differ from $A,B$ by a
multiple of $\theta$, hence stay off the lattice (since $A,B$ do) — child$_2$ safe. In the
second case ($x=180-B-k\theta$), $A-x=k\theta-C$ (off-lattice since $C$ is) and
$B+x=180-k\theta$, which is on the lattice iff $180\in\theta\mathbb Z$ iff $\theta$ is
resonant — excluded by hypothesis. So child$_2$ safe in both cases. $\blacksquare$

**Corollary (explicit safe start).** The equilateral triangle $(60°,60°,60°)$ is safe for
every non-resonant $\theta$: $60=k\theta \Rightarrow 180/\theta = 3k \in \mathbb Z$,
contradiction.

Source: certified from `results/imo-2026-04/approaches/interval-partition-topological.md`
(Lemmas N1+N2), cross-verified against the equivalent 4-case argument in
`resonance-lattice-invariant.md` (Lemma 2). Certified by proof-reviewer round 2 after
independent algebraic re-derivation and exact-arithmetic computational check (20000
trials, 0 counterexamples). This is the necessity-direction invariant for the Mulan's
Triangle Game characterization ($\theta=180/n$); reusable for any problem requiring an
"avoid all multiples of a fixed angle under iterated angle-splitting" argument.
