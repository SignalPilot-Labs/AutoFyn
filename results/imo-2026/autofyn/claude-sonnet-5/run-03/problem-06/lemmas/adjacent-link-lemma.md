## Adjacent-Link Lemma

**Statement.** Let $R:=\mathrm{rad}(a_1)$ (product of the distinct primes
dividing $a_1$), and for $n\ge1$ let $d_n:=a_{n+1}-a_n$. Then for every
$n\ge1$:
$$\gcd(a_n,a_{n+1}) = \gcd(a_n,d_n) \mid d_n \le R,$$
so $\gcd(a_n,a_{n+1})\le R$ and every prime factor of $\gcd(a_n,a_{n+1})$
is $\le R$. In particular $(d_n,\gcd(a_n,a_{n+1}))$ takes values in the
fixed finite alphabet $\{1,\dots,R\}^2$ for every $n\ge1$, unconditionally
(no transient).

**Proof.** By the sequence's defining property applied at step $n$ with
constraint index $i=n$, $\gcd(a_{n+1},a_n)>1$. The elementary identity
$\gcd(x,x+d)=\gcd(x,d)$ (any common divisor of $x,x+d$ divides their
difference $d$; any common divisor of $x,d$ divides $x+d$; hence the two
gcds have identical common-divisor sets, so are equal) gives
$\gcd(a_n,a_{n+1})=\gcd(a_n,d_n)$, which divides $d_n$. By the certified
`bounded-gap-via-rad-a1.md`, $d_n\le R$. Hence $\gcd(a_n,a_{n+1})$ divides
a positive integer $\le R$, so is itself $\le R$, and all its prime
factors are $\le R$. $\blacksquare$

**Verified numerically** (round 3, proof-reviewer): direct simulation for
$a_1\in\{15,21,35,77\}$ confirms $d_n\le R$ and the gcd identity at every
checked step.

### Provenance
Independently derived, identically, in
`approaches/jacobsthal-covering-bound.md` (round 3, "Adjacent-Link
Lemma") and `approaches/bounded-link-invariant.md` (round 3, §1). Both
proofs verified correct by the proof-reviewer round 3; certified once
here per the population's own coordination note.

### Status
Unconditional, holds for every $n\ge1$. Gives a fixed finite alphabet for
the pair $(d_n,\gcd(a_n,a_{n+1}))$, usable as raw material for future
finite-state arguments — but see `windowed-epsilon-automaton-failure.md`
for a proof that a *bounded window* of this alphabet alone cannot recover
the residue-dependent quantities needed to finish the problem.
