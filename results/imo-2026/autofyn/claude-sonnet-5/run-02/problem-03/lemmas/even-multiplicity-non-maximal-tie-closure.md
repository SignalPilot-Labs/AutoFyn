## Statement (CERTIFIED, round 27)

Let $T''$ be a legal $\le(n-4)$-cut refinement of the ladder tail
$\{p_5,\dots,p_{n+1}\}$ (so $p_4>\max(T'')$ and $\mathrm{Total}(T'')=
p_4-f(n)$ — pure ladder algebra, no legality beyond "refinement" needed),
and let $t^\ast\in T''$ be a value occurring with **even** multiplicity
$\mu\ge2$ in $T''$. Let $B:=\{t^\ast\}\cup\{p_4\}\cup T''$. Then
$$A(B)\ \ge\ f(n)+t^\ast\ >\ f(n),$$
unconditionally, for every $n\ge5$ and every such legal $T''$ — no
induction hypothesis $(\star_{n-4})$ or any other standing hypothesis is
used.

This is the exact complement of the certified `anchored-single-tie-
deletion-bound` (which covers the same setup when $t^\ast$'s multiplicity
in $T''$ is **odd**): together the two lemmas cover every possible
multiplicity of a non-maximal tied breakpoint.

## Proof

Write $H:=T''_{>t^\ast}$ (size $k$), $L:=T''_{<t^\ast}$, so $T''$ sorted
descending is $H,\{t^\ast\}^\mu,L$.

**Rank-Split Formula (elementary sub-lemma).** If $S$ is sorted descending
and split at position $k$ into the top-$k$ block $P$ and the remainder
$Q$, then $A(S)=A(P)+(-1)^kA(Q)$. *Proof:* an element of $Q$ at local rank
$i$ sits at global rank $k+i$, contributing sign $(-1)^{k+i-1}=(-1)^k
(-1)^{i-1}$, exactly $(-1)^k$ times its local-rank sign; summing over $Q$
gives $(-1)^kA(Q)$, and $P$'s contributions are unchanged, giving $A(P)$.
(This is the identical computation used, at a different split point,
inside `insert-element-identity`'s own certified proof.)

**Step 1.** Applying the certified `odd-run-reduction-lemma` to
$T''_{\le t^\ast}:=\{t^\ast\}^\mu\cup L$: since $\mu$ is even, $t^\ast$
reduces to $0$ copies, and $T''_{\le t^\ast}$ reduces to the same
fully-reduced multiset as $L$ alone. Hence $A(T''_{\le t^\ast})=A(L)$.

**Step 2.** Rank-Split Formula on $T''$ at $k=|H|$, using Step 1:
$$A(T'')=A(H)+(-1)^kA(T''_{\le t^\ast})=A(H)+(-1)^kA(L).\qquad(\text{Fact I})$$

**Step 3.** Apply the certified `insert-element-identity` to $T'=
\{p_4\}\cup T''$, $b=t^\ast$. Since $p_4>\max(T'')\ge t^\ast$, $j:=
|T'_{>t^\ast}|=1+k$. The identity gives
$$A(B)=2A(T'_{>t^\ast})-A(T')+(-1)^{k+1}t^\ast.$$
$T'_{>t^\ast}=\{p_4\}\cup H$ and $p_4>\max(H)$, so the certified
`sharp-dominant-removal-identity` gives $A(T'_{>t^\ast})=p_4-A(H)$;
likewise $A(T')=A(\{p_4\}\cup T'')=p_4-A(T'')$ (same identity, $p_4>
\max(T'')$). Substituting and using $(-1)^{k+1}=-(-1)^k$:
$$A(B)=2(p_4-A(H))-(p_4-A(T''))-(-1)^kt^\ast=p_4-2A(H)+A(T'')-(-1)^kt^\ast.$$
Substituting Fact I:
$$A(B)=p_4-A(H)+(-1)^k\big(A(L)-t^\ast\big).\qquad(\text{Exact Identity})$$

**Step 4.** $\mathrm{Total}(T'')=p_4-f(n)$ and $\mathrm{Total}(T'')=
\mathrm{Total}(H)+\mu t^\ast+\mathrm{Total}(L)$, so $p_4=f(n)+
\mathrm{Total}(H)+\mu t^\ast+\mathrm{Total}(L)$. Substituting into the
Exact Identity:
$$A(B)=f(n)+\big[\mathrm{Total}(H)-A(H)\big]+\mathrm{Total}(L)+(-1)^kA(L)
+\mu t^\ast-(-1)^kt^\ast.$$
If $k$ even: $A(B)=f(n)+[\mathrm{Total}(H)-A(H)]+[\mathrm{Total}(L)+A(L)]
+(\mu-1)t^\ast$.
If $k$ odd: $A(B)=f(n)+[\mathrm{Total}(H)-A(H)]+[\mathrm{Total}(L)-A(L)]
+(\mu+1)t^\ast$.

**Step 5.** By the trivial bound $A(S)\le\mathrm{Total}(S)$ (certified,
`integral-alternating-sum-formula`), $\mathrm{Total}(H)-A(H)\ge0$ and
$\mathrm{Total}(L)-A(L)\ge0$. By the certified `alternating-sum-
nonnegativity`, $A(L)\ge0$, so $\mathrm{Total}(L)+A(L)\ge0$ too.
Substituting: in either parity of $k$,
$$A(B)\ \ge\ f(n)+(\mu-1)t^\ast\ \ge\ f(n)+t^\ast\ >\ f(n)$$
since $\mu\ge2$. $\blacksquare$

## Why this succeeds where a naive attempt fails

Bounding $A(T''\cup\{t^\ast\})$ via the triangle inequality
($\le A(T'')+t^\ast$, `triangle-bound-for-a`) and then bounding $A(T'')$
as a single block by the trivial bound $A(T'')\le\mathrm{Total}(T'')$
gives only $A(B)\ge f(n)-t^\ast$ (insufficient — can be negative-margin).
This proof instead computes $A(B)$ **exactly** as a function of $A(H)$ and
$A(L)$ separately (Step 3, an equality), and applies the trivial bound to
$H$ and $L$ **individually only after** that exact reduction. This
recovers strictly more slack in general (the two routes coincide only
when $H$ or $L$ is empty), which is exactly what closes the gap.

## Numeric verification (this build, round 27)

1. Exact symbolic algebra (`sympy`), two concrete small instantiations
   covering both parities of $k$: the Exact Identity of Step 3 checked
   exactly, symbolic difference identically $0$.
2. Abstract random exact-`Fraction` trials: $\sim$7,761 trials of the
   Exact Identity (zero mismatches) and $\sim$10,729 trials of the final
   bound with $p_4$ explicitly dominant (zero violations, minimum observed
   slack exactly $0$, matching the proof's own tightness analysis).
3. Actual ladder-structure trials: $6{,}438$ exact-`Fraction` trials,
   $n=5,\dots,11$, engineered even-multiplicity ties via equal-$k$-split
   ($k\in\{2,4\}$) of a random tail piece — zero violations of $A(B)\ge
   f(n)+t^\ast$.

## Origin / usage

Derived in `results/imo-2026-03/approaches/greedy-halving-adversary.md`,
round 27, closing the residual left open by round 26's `anchored-single-
tie-deletion-bound` (Theorem 40). Combined with Theorem 37 (the symmetric
vertex $b=p_4$) and Theorem 40, fully closes Theorem 37's own
"$T'$-untouched" branch of Case (b)'s "$v\ge a$" target, for every
$n\ge5$. Does **not** close Case (b)'s "$v\ge a$" branch as a whole (the
separate "$T'$-cuts-$p_4$" branch, $h(m)$ for $m\ge3$, remains open).

## Certification note

CERTIFIED round 27. Proof-reviewer independently re-derived the entire
chain (Rank-Split Formula, Steps 1-5) by hand and cross-checked every
substitution; independently re-verified the final bound with a fresh
exact-`Fraction` script (`/tmp/round-27/verify_thm41.py`, 20,000 trials
constructing genuine ladder tails with engineered even-multiplicity ties,
zero violations of $A(B)\ge f(n)+t^\ast$). No gap found; certified as
stated, unconditional for every $n\ge5$.
