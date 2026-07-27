# Round 2 proof-reviewer — IMO 2026 Problem 5

Three approaches reviewed. The central adjudication (master squeeze) is done
first because it determines the fate of all three.

## 1. Master-squeeze adjudication

**Verdict: the master squeeze is TRUE (an equivalence to the original chain,
both directions). master-sos-identity is right; density-contradiction's
rejection is an error.**

### 1a. SOS identities — verified exactly (sympy)

With $f(x)=x+g(x)$, $f(y)=y+g(y)$, and
$U=\frac{x^{2}+f(y)^{2}}2-\bigl(\frac{f(x)+y}2\bigr)^2$,
$L=\bigl(\frac{f(x)+y}2\bigr)^2-xf(y)$, sympy expands:
- $U+L-(x-f(y))^{2}/2 \equiv 0$ — exact.
- $U-L+(g(x)-g(y))(g(x)+g(y)+2x+2y)/2 \equiv 0$ — exact.

Both identities hold as polynomial identities. (Completing the square.)

### 1b. The biconditional Fact

For $a,b\in\mathbb R$: $a,b\ge0 \iff a+b\ge0\ \land\ |a-b|\le a+b$.
- $(\Rightarrow)$ $a,b\ge0\Rightarrow a+b\ge0$ and $-a\le b,-b\le a$.
- $(\Leftarrow)$ $a-b\le a+b\Rightarrow b\ge0$; $b-a\le a+b\Rightarrow a\ge0$.
Verified on $10^5$ random pairs. Apply with $a=U,b=L$: since
$U+L=(x-f(y))^2/2\ge0$ automatically, $U,L\ge0\iff|U-L|\le U+L=(x-f(y))^2/2$,
i.e. $|(g(x)-g(y))(g(x)+g(y)+2x+2y)|\le(x-f(y))^2$ — **both directions**. The
squeeze is EQUIVALENT to the chain: every chain-satisfying $f$ satisfies it,
and conversely.

### 1c. density's "counterexample $a=1,b=3$" — refuted

Reconstructed concretely: density's scenario corresponds to $x=1$, $f(y)=3$
with $g(x)=1,g(y)=0$, i.e. $f(1)=2,f(3)=3$. At $(x,y)=(1,3)$:
- Master squeeze LHS $=|1-0|(1+0+2+6)=9$, RHS $=(1-3)^2=4$. $9\le4$ is FALSE.
- Original chain at $(1,3)$: $\mathrm{QM}=\sqrt5\approx2.236$,
  $\mathrm{AM}=(2+3)/2=2.5$, $\mathrm{GM}=\sqrt3\approx1.732$.
  $\mathrm{QM}\ge\mathrm{AM}$ FAILS ($2.236<2.5$).

So this $f$ does **not** satisfy the original chain, hence is **not** a
counterexample to the lemma (which is the implication chain $\Rightarrow$
squeeze). Because the squeeze is equivalent to the chain, no counterexample
can exist: any $f$ satisfying the chain satisfies the squeeze. density's
rejection of the master squeeze is an error. (Note: density's own proof does
not actually rely on the master squeeze — it uses an independently-derived
weaker squeeze — so this error does not propagate; see Section 3 below.)

## 2. orbit-monotonicity-sandwich — APPROVE, Status solved

Uses the master squeeze (proven in-file in Section 4, self-contained; sympy-
verified above). Reviewed each load-bearing step:

- **Section 4 (master squeeze).** Self-contained: $A=(f(x)+y)^2-4xf(y)\ge0$,
  $B=2(x^2+f(y)^2)-(f(x)+y)^2\ge0$; $A+B=2(x-f(y))^2$,
  $A-B=2(g(x)-g(y))(g(x)+g(y)+2x+2y)$ (matches the certified identity:
  $A=4L,B=4U$). $|A-B|\le A+B$ gives $(\star)$. Valid.
- **Lemma 5 (asymptotic pinning).** Valid. The arithmetic orbit
  $y_n=y_0+n\alpha$ carries $g=\alpha$ and $f(y_n)=y_{n+1}$. The lattice
  $\{y_0+m\alpha\}_{m\ge1}$ covers $[y_0+\alpha/2,\infty)$ within $\alpha/2$;
  nearest-point selection gives $|x-y_{n+1}|\le\alpha/2$; squeeze
  $|g(x)-\alpha|\le(x-y_{n+1})^2/(2(x+y_n))\le\alpha^2/(8(x+y_0))\to0$. Checked
  numerically: bound shrinks to $0$. No hidden attainment assumption — the
  limit is *derived* from the squeeze, not assumed; positive values need not
  form a tail a priori, the limit forces it.
- **Cor 5.1.** Uniqueness of limits: $g(a)=g(b)=\lim g$. Valid.
- **Lemma 6 (tail constant).** Image $\subseteq\{0,\beta\}$ (Cor 5.1 + $g\ge0$);
  $g\to\beta$ forces $g=\beta$ on a tail. Valid.
- **Lemma 7 (zero-set open).** Squeeze at $y=a$ ($g(a)=0$, $f(a)=a$) gives
  $|g(x)|\le(x-a)^2/(2(x+a))\to0$; continuity at $a$; image in $\{0,\beta\}$
  forces $g=0$ near $a$. Valid.
- **Lemma 8 (boundary contradiction).** $Z=\{g=0\}$ open, bounded above by
  $X_0$; $q=\sup Z\notin Z$ (else neighborhood in $Z$, contradicting sup),
  so $g(q)=\beta$, $f(q)=q+\beta$. Sequence $x_n\nearrow q$ in $Z$ (exists by
  definition of sup for a set not containing its sup). Apply $(\star)$ with
  $x=x_n,y=q$: $\beta(\beta+2x_n+2q)\le(x_n-q-\beta)^2$; limit gives
  $\beta(\beta+4q)\le\beta^2\Rightarrow q\le0$, contradicting $q\ge x_n>0$.
  Valid. Edge cases: "$g$ has no zeros" is the desired conclusion (no
  contradiction needed); "$g$ has no positive value" is Case 1 ($g\equiv0$);
  "$g>0$ everywhere nonconstant" is ruled out by Cor 5.1. All cases covered.

Exhibit verified (Section 0). COMPLETE and RIGOROUS. Status solved is correct.

## 3. density-contradiction — CHANGES REQUESTED, Status partial

The weaker squeeze density uses, $|g(x)-g(y)|\le(x-f(y))^2/(x+f(y))$, is
correctly and independently derived (rationalize $2U$, difference-of-squares
for $2L$; $|s|\le\max(2U,2L)$). The "denominator $\ge a+b>0$" observation in
the irrational case correctly **defuses the rate concern**: the bound is
$\le\mathrm{num}^2/(a+b)$, and Kronecker density makes $\mathrm{num}\to0$ with
no Diophantine rate needed (the denominator is bounded *below*, so shrinking
numerator drives the fraction to 0). The rational-ratio R1 (same-coset
intersection, Bezout) and R2 (distinct cosets, fixed residue $\rho$, growing
denominator $\to\infty$ with fixed $\rho^2$) arguments are correct.

**Gap A — irrational case, Section 6: target off by $\alpha$.** The
cross-distance is $D=b-a+m\beta-(n+1)\alpha$ (since $f(y)=a+(n+1)\alpha$). To
drive $D\to0$ one needs $m\beta-(n+1)\alpha\to a-b$. Density sets
$c_0:=a+\alpha-b$ and demands $|m\beta-(n+1)\alpha-c_0|<\varepsilon$, which
drives $m\beta-(n+1)\alpha\to a+\alpha-b$, hence
$D\to(b-a)+(a+\alpha-b)=\alpha\ne0$. The bound then tends to
$\alpha^2/(a+b)>0$, which does **not** force $\beta=\alpha$. As written the
irrational case fails. Fix: set $c_0=a-b$ (Kronecker works for any target).
This is a one-token fix but the proof as written is wrong at its load-bearing
step.

**Gap B — Stage B, Section 8: sign error in the $a-b\in\beta\mathbb Z$,
$k\le-1$ sub-case.** Density claims $a=b+(-k)\beta\in B$ (the forward orbit
$\{b+m\beta:m\ge0\}$). But $a-b=k\beta$ with $k\le-1$ gives
$a=b+k\beta=b-(-k)\beta<b$; so $a=b-(-k)\beta$, NOT $b+(-k)\beta$, and $a\notin
B$ (the forward orbit walks upward from $b$). No contradiction from orbit
membership here. The case split sends this sub-case to a broken argument
instead of the (case-independent) propagation argument that follows. Fix:
drop the case split — the propagation (base case: continuity-at-zero +
two-valued image gives a zero interval; extension: $g\le(x-y)^2/(x+y)<\beta$
near the boundary forces more zeros) reaches $g\equiv0$ on $[a,\infty)$
rightward by a fixed step $\sim\sqrt{2u\beta}$, which intersects the unbounded
forward orbit of $b$ (where $g=\beta$), giving the contradiction. The
propagation does not need $a-b\in\beta\mathbb Z$.

**Side error (non-propagating):** density's explicit rejection of the master
squeeze as "false" is wrong (it is a true theorem, equivalent to the chain —
Section 1 above). This does not affect the proof because density uses its own
weaker squeeze, but the rejection should be retracted.

## 4. master-sos-identity — CHANGES REQUESTED, Status partial (verified lemma)

The Master Squeeze Lemma (SOS identity + both-direction equivalence + reduced
form under $g\ge0$ + swapped-min corollary) is proven correctly and rigorously;
sympy confirms both identities to zero residue; the biconditional Fact is
correct. **Certified** into `results/imo-2026-05/lemmas/master-squeeze.md`.

The direct algebraic kill is honestly flagged open: sub-routes (a) no
simultaneous-collapse family without regularity, (b) no IVT without
continuity, (c) the optimization "bound" $\min\le((g(x)+g(y))/2)^2$ retracted
as a non-result. The retraction of (c) is **correct**: for $g(x)=g(y)=1$,
$d=x-y=100$ gives $\min\{9801,9801\}=9801\gg1=((1+1)/2)^2$, refuting the
claimed universal bound. The `partial` status is correctly assigned (lemma
proven, full problem not solved by this approach alone).

## Summary table

| approach | builder status | true status | verdict | gap |
|---|---|---|---|---|
| orbit-monotonicity-sandwich | solved | solved | APPROVE | none |
| density-contradiction | solved | partial | CHANGES REQUESTED | Gap A (irrational target off by $\alpha$), Gap B (Stage B $k\le-1$ sign error) |
| master-sos-identity | partial | partial | CHANGES REQUESTED | direct kill open (honest); lemma certified |
