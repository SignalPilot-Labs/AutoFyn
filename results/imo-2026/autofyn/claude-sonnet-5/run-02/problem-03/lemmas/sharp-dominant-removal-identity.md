## Statement (PROPOSED — awaiting proof-reviewer certification)

Let $T$ be a finite multiset of positive reals with $m:=\max(T)$, and let
$f_1>m$. Then
$$A(\{f_1\}\cup T) = f_1 - A(T),$$
where $A(\cdot)$ is the alternating-sum-of-sorted-descending-order
functional of the certified `integral-alternating-sum-formula` lemma.

This **strictly generalizes** the certified `dominant-element-removal-identity`
lemma, whose hypothesis is the stronger $f_1>\mathrm{Total}(T)$ (dominance
over the *sum* of the rest). Here only $f_1>\max(T)$ is required — the
identity holds even when $f_1<\mathrm{Total}(T)$, i.e. even when $f_1$ is
"locally" but not "globally" dominant.

## Proof

By `integral-alternating-sum-formula`,
$A(S)=\int_0^\infty\mathbb1[N_S(x)\text{ odd}]\,dx$, $N_S(x):=\#\{s\in S:
s>x\}$. Write $N(x):=N_{\{f_1\}\cup T}(x)=\mathbb1[f_1>x]+N_T(x)$.

*Range $x\ge m$:* $N_T(x)=0$ (every element of $T$ is $\le m\le x$), so
$N(x)=\mathbb1[f_1>x]$, contributing
$\int_m^\infty\mathbb1[f_1>x]\,dx=\int_m^{f_1}1\,dx=f_1-m$.

*Range $x<m$:* $f_1>m>x$, so $\mathbb1[f_1>x]=1$ identically and
$N(x)=1+N_T(x)$; parity of $N(x)$ is the negation of $N_T(x)$'s parity, so
$\mathbb1[N(x)\text{ odd}]=1-\mathbb1[N_T(x)\text{ odd}]$ on $[0,m)$, giving
$$\int_0^m\mathbb1[N(x)\text{ odd}]\,dx = m-\int_0^m\mathbb1[N_T(x)\text{
odd}]\,dx = m-A(T)$$
(using $N_T(x)=0$ for $x\ge m$, so $A(T)=\int_0^m\mathbb1[N_T\text{ odd}]$).

Summing: $A(\{f_1\}\cup T)=(f_1-m)+(m-A(T))=f_1-A(T)$. $\blacksquare$

## Numeric verification (this build, round 4)

20000 random exact-`Fraction` trials, deliberately constructed so that
$f_1>\max(T)$ while $f_1<\mathrm{Total}(T)$ in many cases (i.e. genuinely
outside the old lemma's hypothesis): zero mismatches between
$A(\{f_1\}\cup T)$ (direct sort-and-alternate-sum) and $f_1-A(T)$.

**Explicit witness that the weaker hypothesis is actually exercised:**
$T=\{\underbrace{1,\dots,1}_{11}\}$, $f_1=10$. Here $\max(T)=1<10=f_1$
(new hypothesis holds), but $\mathrm{Total}(T)=11>10=f_1$ (old lemma's
hypothesis $f_1>\mathrm{Total}(T)$ *fails*). Direct computation:
$A(T)=1-1+1-\dots+1=1$ (eleven terms), $A(\{10\}\cup T)$: sorted
$\{10,1,\dots,1\}$ (12 elements), $A=10-1+1-1+\dots+1=9$, matching
$f_1-A(T)=10-1=9$.

## Origin / usage

Derived in `results/imo-2026-03/approaches/rank-pigeonhole-budget.md`, §1
(round 4), to collapse Proposition 10's Case-A cross-term analysis
(`greedy-halving-adversary.md`) into a single-line identity: applied with
$T=F'\cup G'$ (Xiang Yu's small fragments of $p_1$ plus his tail
refinement), where the ladder's Key Lemma ("at most one fragment of $p_1$
exceeds $r$") guarantees $\max(T)\le r<f_1$, this gives
$A(F\cup G')=f_1-A(F'\cup G')$ directly, replacing a two-step chained
application of `cross-term-identity-threshold`.

## Certification note (proof-reviewer, round 4)
**CERTIFIED.** Independently re-derived the integral-splitting proof line by
line (no gap) and independently re-verified by an exact-`Fraction` script
(20000 random trials, $f_1>\max(T)$ with $f_1<\mathrm{Total}(T)$ deliberately
included) — zero mismatches. Re-checked the explicit witness
$T=\{1^{11}\}$, $f_1=10$: $A(T)=1$, $A(\{10\}\cup T)=9=10-1$, exact match.
Promoted to `lemmas/`.
