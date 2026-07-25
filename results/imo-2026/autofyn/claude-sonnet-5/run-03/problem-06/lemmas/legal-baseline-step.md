## Legal-baseline-step Lemma

**Statement.** Let $R:=\mathrm{rad}(a_1)$. For $n\ge1$ let $M_n$ be the
smallest multiple of $R$ exceeding $a_n$, and $b_n:=M_n-a_n$. Then for
every $n\ge1$: (a) $1\le b_n\le R$; (b) $\gcd(a_n+b_n,a_i)>1$ for
**every** $i=1,\dots,n$ (so $M_n=a_n+b_n$ is a legal candidate for
$a_{n+1}$ against the entire prefix, not merely against $a_1$); (c)
consequently $d_n:=a_{n+1}-a_n\le b_n$.

**Proof.** (a) Rounding up to the next multiple of $R$ overshoots by at
most $R$ and at least $1$. (b) By the certified `prime-factors-a1-cover-forever.md`
(equivalently the internal Fact of `bounded-gap-via-rad-a1.md`), every
$a_i$ ($i\ge1$) is divisible by some prime $p\in R(a_1)$. Since
$R=\prod_{p\in R(a_1)}p$ divides $M_n$, in particular $p\mid M_n$, so
$p\mid\gcd(M_n,a_i)$, i.e. $\gcd(M_n,a_i)\ge p>1$. This holds for every
$i=1,\dots,n$ simultaneously (using, for each $i$, whichever prime of
$R(a_1)$ divides that particular $a_i$ — a genuine improvement over
naively using only the single prime shared with $a_1$, which does **not**
certify validity against $a_i$, $i\ge2$: see the certified
`covering-membership-not-safety-certificate.md`). (c) $M_n$ is a legal
candidate exceeding $a_n$, and $a_{n+1}$ is the least such candidate, so
$a_{n+1}\le M_n$, i.e. $d_n\le b_n$. $\blacksquare$

### Provenance
`approaches/bounded-link-invariant.md`, round 3, §2 (repairing a flaw the
outline-reviewer found in an earlier draft baseline that used only a
single shared prime with $a_1$). Verified by the proof-reviewer round 3:
correct, and a genuine corollary of the already-certified
`bounded-gap-via-rad-a1.md` / `prime-factors-a1-cover-forever.md`.

### Status
Unconditional, holds for every $n\ge1$, no transient. Gives a pointwise
(not just aggregate) legal-and-bounded fallback candidate at every step.
