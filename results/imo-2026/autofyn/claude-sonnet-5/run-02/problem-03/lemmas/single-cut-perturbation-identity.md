## Statement

Let $S=R\cup\{M\}$ be a finite multiset of positive reals ($R$ arbitrary,
$M>0$ one further element). Split $M$ into two positive fragments
$f_1\ge f_2>0$ with $f_1+f_2=M$ (any split point), and let
$S'=R\cup\{f_1,f_2\}$. Let $u_R(x):=\mathbb1[N_R(x)\text{ odd}]$
($N_R(x):=\#\{s\in R: s>x\}$). Then
$$A(S')-A(S) = 2(I_1+I_2)-2f_2,\qquad
I_1:=\int_0^{f_2}u_R(x)\,dx,\quad I_2:=\int_{f_1}^M u_R(x)\,dx.$$
($I_1,I_2$ are integrals of a $\{0,1\}$-valued function over windows of
length exactly $f_2$ apiece, so $0\le I_1,I_2\le f_2$ and
$-2f_2\le A(S')-A(S)\le2f_2$ — the sign is not determined by mass alone.)

Fully general: no ladder-specific structure assumed.

## Proof

By `cross-term-identity-threshold` (with $F=R$, $G=\{M\}$, threshold $M$):
the odd-parity indicator of $\{M\}$ is $1$ on $[0,M)$, $0$ beyond, so
$A(\{M\})=M$ and
$$A(S)=A(R)+M-2\int_0^M u_R(x)\,dx.$$
By the same identity again (with $G=\{f_1,f_2\}$, threshold $f_1+f_2=M$):
$A(\{f_1,f_2\})=f_1-f_2$ and its odd-parity indicator is
$\mathbb1[f_2\le x<f_1]$, so
$$A(S')=A(R)+(f_1-f_2)-2\int_{f_2}^{f_1}u_R(x)\,dx.$$
Subtracting and using $f_1-f_2-M=-2f_2$ together with
$\int_0^M u_R=\int_0^{f_2}u_R+\int_{f_2}^{f_1}u_R+\int_{f_1}^M u_R$, the
middle term cancels, leaving
$$A(S')-A(S)=-2f_2+2\Big(\int_0^{f_2}u_R+\int_{f_1}^M u_R\Big)=2(I_1+I_2)-2f_2.
\qquad\blacksquare$$

## Numeric verification (proof-reviewer, round 5)

Independently re-derived the algebra above line by line (no gap), and
independently re-ran 3000 random exact-`Fraction` trials ($R$ of random size
1–5 with random rational entries, $M$ random, split point random in
$(0,1)$), comparing the claimed identity's RHS against a direct
sort-and-alternate-sum computation of $A(S')-A(S)$: zero mismatches.

## Origin / usage

Derived in `results/imo-2026-03/approaches/greedy-halving-adversary.md`
(Lemma 14, round 5), used to prove Proposition 15 (the refutation of claim
(B) for arbitrary $F$, see `refutation-of-tail-refinement-monotonicity.md`)
and a strengthening of `symmetric-split-c1-lower-bound` (splitting $p_2$
with $F=\{p_1\}$ leaves $A$ unchanged for *every* split point, not just the
symmetric one).

## Certification note (proof-reviewer, round 5)
**CERTIFIED.** Independently re-derived the proof and independently
re-verified by a 3000-trial exact-`Fraction` script comparing both sides —
zero mismatches. Promoted to `lemmas/`.
