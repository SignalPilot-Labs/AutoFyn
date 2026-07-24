## Statement

Let $S$ be a finite multiset of positive reals with a distinguished element
$z\in S$ of maximal value (i.e. $z=\max S$; if the maximum is attained by
several equal elements, fix any one copy as "$z$"). Write $G:=S\setminus\{z\}$
(the remaining elements, as a multiset) and $r:=\mathrm{Total}(G)$. Then
$$A(S) \;=\; z + A(G) - 2\int_0^{\min(z,r)} v(t)\,dt,\qquad
v(t):=\mathbb 1[N_G(t)\text{ is odd}],$$
where $N_G(t):=\#\{g\in G: g>t\}$. Equivalently, since $A(\{z\})=z$ (a
single-element multiset has alternating sum equal to itself):
$$A(S) = A(\{z\})+A(G) - 2\int_0^{\mathrm{Total}(G)}\mathbb1[t<z]\cdot v(t)\,dt.$$

This is nothing more than the certified `cross-term-identity-threshold`
instantiated at $F:=\{z\}$ (a singleton), $G:=S\setminus\{z\}$ — recorded
here as its own named lemma because "peel off the single largest element and
treat everything else as one lump" is a recurring move (used to reduce a
$c_1$-way fragmentation of one piece to a 1-vs-rest split with no case
distinction on where further cuts land), and because the resulting window
$[0,z)$ is **anchored at the origin**, a structurally different shape from
the two-element, midpoint-anchored window used in
`rank-tie-vertex-reduction.md`'s Cross-Term Reduction Theorem — worth
distinguishing by name to avoid conflating the two.

## Proof

Apply `cross-term-identity-threshold` with $F=\{z\}$, $G=S\setminus\{z\}$,
$r=\mathrm{Total}(G)$: $A(F\cup G)=A(F)+A(G)-2\int_0^r u(t)v(t)\,dt$, where
$u(t):=\mathbb1[N_F(t)\text{ odd}]$. Since $F$ has one element,
$N_F(t)=\mathbb1[t<z]\in\{0,1\}$, so $u(t)=\mathbb1[t<z]$ (odd iff $N_F(t)=1$
iff $t<z$), and $A(F)=z$ directly from the definition (a single sorted
element $L_1=z$ gives $A=(-1)^{1+1}z=z$; also recoverable from
`integral-alternating-sum-formula`, $A(\{z\})=\int_0^\infty\mathbb1[t<z]\,dt
=z$). Hence $\int_0^r u v = \int_0^r \mathbb1[t<z]\,v(t)\,dt =
\int_0^{\min(z,r)} v(t)\,dt$ (the integrand is zero for $t\ge z$, and the
outer integration is capped at $r$ regardless), giving the stated identity.
$F\cup G=S$ by construction ($z$ plus everything else). $\blacksquare$

## Certification note (self-check, this round; not yet reviewer-certified)

Direct algebraic corollary of the already-certified
`cross-term-identity-threshold` and `integral-alternating-sum-formula` — no
new machinery, only a specific instantiation, so no independent numeric
check is strictly needed beyond what already certifies those two lemmas.
Cross-checked anyway, incidentally, by the exact-`Fraction` verification
underlying `case-ii-exact-peel-identity.md` (every trial there also
implicitly re-derives this identity as its first step): $5{,}957$ legal
random trials plus $6{,}840$ further trials outside that lemma's ladder-
specific hypothesis, all consistent with this general identity (which holds
unconditionally, independent of any ladder structure).

## Origin

`results/imo-2026-03/approaches/rank-tie-vertex-reduction.md`, round 7
(peel-induction-on-$c_1$ task).

## Certification note (proof-reviewer, round 7)

**CERTIFIED.** Re-derived by hand: a direct, immediate instantiation of the
already-certified `cross-term-identity-threshold` at $F=\{z\}$ — no new
machinery, algebra checked line by line, no gap. Independently re-verified
computationally as part of verifying `case-ii-exact-peel-identity` below
(every trial there re-derives this identity as its first step; 10,138
independent random trials in the dominant-fragment regime, zero
mismatches, run with a freshly-written script, not the builder's).
