## Theorem 36b + Corollary 36c: whole-$R'$ lower bound and Case (b)'s smallest-$v$ sub-range

**Source:** `approaches/greedy-halving-adversary.md`, round 22.
**Status:** CERTIFIED as conditional (proof-reviewer, round 22) — same
conditional status as the standing strong induction hypothesis
$(\star_{n-2})$ (unconditional whenever $n\le4$, since then $n-2\le2$ and
$(\star_1),(\star_2)$ are both unconditionally true).

### Statement (Theorem 36b)

Fix $n\ge3$. Let $R'$ be **any** legal refinement of
$\{p_3,\dots,p_{n+1}\}$ using at most $n-3$ cuts (Theorem 35/36's own
object; no restriction on whether $p_3$ itself is touched, so this covers
both Case (a) and Case (b) uniformly). Assume the standing hypothesis
$(\star_{n-2})$: every legal Xiang-Yu response ($\le n-2$ cuts) to the
$(n-2)$-ladder has $A\ge f(n-2)$. Then $A(R')\ge f(n)$.

### Proof

By the certified `general-cross-level-rescaling-lemma` with $k=2$ (so
$m=n-2$, $\lambda_2=f(n)/f(n-2)$), $\{p_3,\dots,p_{n+1}\}=\lambda_2\cdot
\{$unit $(n-2)$-ladder$\}$ exactly. Since $R'$ uses at most $n-3<n-2$
cuts, $R'/\lambda_2$ is a legal response (using at most $n-3\le n-2$ cuts
— fewer than the full budget is always legal) to the unit $(n-2)$-ladder.
By $(\star_{n-2})$, $A(R'/\lambda_2)\ge f(n-2)$. By the homogeneity of $A$
under uniform positive rescaling (certified Lemma 9: $A(\lambda S)=
\lambda A(S)$), $A(R')=\lambda_2\cdot A(R'/\lambda_2)\ge\lambda_2 f(n-2)=
f(n)$ (using the Rescaling Lemma's "in particular" clause). $\blacksquare$

This is genuinely new content, not a restatement of Theorem 35b: Theorem
35b bounds $A(T')$ (the tail *after* peeling $p_3$ off), applicable only
inside Case (a); Theorem 36b bounds $A(R')$ **as a whole**, uniformly
across Cases (a) and (b), which is what first makes any general-$n$
Case (b) progress possible. It is also not the two-variable circularity
round 20 already ruled out (which needed the *full* level-$(n-2)$
$\Delta$-theorem): Theorem 36b only invokes the one-variable hypothesis
$(\star_{n-2})$ applied to the whole $R'$, sidestepping that circularity.

### Statement (Corollary 36c)

For every legal Case-(b) response $R'=\{a,b\}\cup T'$ (with the notation
of `greedy-halving-adversary.md`, $\Delta(n,v):=A(R')-2A(R'_{>v})$) and
every $v\in(0,\min(R'))$: $\Delta(n,v)\le v-f(n)$, conditional on
$(\star_{n-2})$ (unconditional for $n\le4$). New coverage for $n\ge5$ only
(subsumed by Theorem 36's own exact unconditional closure at $n=3,4$).

### Proof

For $v<\min(R')$, every element of $R'$ exceeds $v$, so $R'_{>v}=R'$ and
$A(R'_{>v})=A(R')$, giving $\Delta(n,v)=A(R')-2A(R')=-A(R')$. By Theorem
36b, $A(R')\ge f(n)$, so $\Delta(n,v)=-A(R')\le-f(n)<v-f(n)$ (strict,
since $v>0$). $\blacksquare$

### Verification

Proof-reviewer independently re-derived the algebra of both statements
(matching the builder's proofs exactly) and independently re-verified
Theorem 36b's conclusion numerically with a fresh, independently-written
random-legal-refinement generator (`/tmp/round-22/verify_gha.py`,
`test_theorem36b`, distinct from the builder's own script): for
$n=4,\dots,8$, minimum sampled $A(R')-f(n)$ was $\ge0$ in every trial
(observed minima $0,0,\approx0.0001,\approx0.0003,\approx0.0045$),
consistent with (though not a substitute for) the conditional proof above,
and matching the builder's own reported margins to the same order of
magnitude.

### What is NOT closed

Case (b)'s remaining sub-range $v\in[\min(R'),a)$ — in particular the
"$v\ge a$" endpoint needing $A(B)\ge f(n)$ for $B=\{b\}\cup T'$ — is
**not** closed by Theorem 36b/Corollary 36c; see `insert-element-identity`
for the reviewer-confirmed diagnosis of why this remaining sub-range
resists the file's current one-sided-lower-bound machinery.
