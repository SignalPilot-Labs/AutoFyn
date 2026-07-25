## Status
partial

## Approaches tried
- **Round 3 (this build).** Fixed the flaw the outline-reviewer found in the
  round-3 outline's baseline-step definition (§ "Flaw found" in
  `/tmp/round-3/outline-reviewer.md`): the original $b_n:=\min\{d\ge1:
  \gcd(a_n+d,a_1)>1\}$ is **not** a legal candidate against all earlier
  terms, only against $a_1$ — exactly the `covering-membership-not-safety-
  certificate.md` trap. Repaired the definition by taking $b_n$ to be the
  gap to the *next multiple of $R:=\mathrm{rad}(a_1)$*, whose legality
  against **every** earlier term is already established by the certified
  `lemmas/bounded-gap-via-rad-a1.md`. Re-derived the finite-alphabet
  Adjacent-Link Lemma from scratch. Then attempted the outline's central
  target — bounded-order ("windowed automaton") determinacy of the
  exceptional-step indicator $\epsilon_n$ — and **refuted it**, both
  computationally (exact-integer search over several $a_1$, no floating
  point) and then **analytically**, with a complete, self-contained,
  computation-free proof for $a_1=21$: the pair sequence $(d_n,\ell_n)$ is
  literally constant $(3,3)$ for *every* $n\ge1$ (this in fact solves the
  whole problem for $a_1=21$, with $T=1,L=3$), yet $\epsilon_n$ is
  **provably period-7**, so no window of the (constant!) pair sequence, of
  any width, can determine it. Generalized this to a clean unconditional
  structural theorem (Theorem N below) explaining exactly why: $\epsilon_n$
  depends on the *cumulative* residue $a_n\bmod R$, an additive quantity a
  bounded window of relative gaps cannot see, whenever the eventual common
  gap $d^*$ is a proper divisor-compatible value with $R/\gcd(d^*,R)>1$.
  **Outcome:** the approach's central mechanism (Step 4 of the round-3
  outline) is now proved to be false in general, not merely empirically
  unverified. The unconditional finite-alphabet content and the corrected,
  provably-legal baseline survive and are the salvaged content of this
  round; Step 5's fallback ("bounded density of exceptional steps") is also
  checked and found unhelpful (density is *high*, not low, in exactly the
  cases where the mechanism fails). Status: **partial**, honestly
  documenting a real negative result rather than a working automaton.

## Current best

### 0. Setup and notation
Let $(a_n)_{n\ge1}$ be the problem's greedy sequence, $R:=\mathrm{rad}(a_1)$
(product of the distinct primes dividing $a_1$), $d_n:=a_{n+1}-a_n$ the
gap sequence, and $\ell_n:=\gcd(a_n,a_{n+1})$ the link sequence.

### 1. Adjacent-Link Lemma (unconditional, no transient)
**Claim.** For every $n\ge1$: $\ell_n=\gcd(a_n,d_n)\mid d_n$, and $d_n\le R$;
consequently $d_n,\ell_n\in\{1,\dots,R\}$ for every $n\ge1$.

**Proof.** By the elementary identity $\gcd(x,x+d)=\gcd(x,d)$ (since any
common divisor of $x$ and $x+d$ divides their difference $d$, and conversely
any common divisor of $x$ and $d$ divides $x+d$), we get $\gcd(a_n,a_{n+1})
=\gcd(a_n,d_n)$, which divides $d_n$ by definition of gcd. The bound
$d_n\le R$ is exactly the certified `lemmas/bounded-gap-via-rad-a1.md`
(Key Lemma). Combining, $1\le \ell_n\le d_n\le R$ for all $n\ge1$. $\blacksquare$

This gives a **fixed, finite alphabet** $\{1,\dots,R\}^2$ for the pair
$\sigma_n:=(d_n,\ell_n)$, valid for *every* $n\ge1$ — no hypothesis, no
transient, no dependence on any auxiliary set $Q$ of primes. (This lemma is
shared with `jacobsthal-covering-bound.md`, which independently derives the
same statement under the name "Adjacent-Link Lemma"; per the outline's
coordination note, only one copy should be certified into `lemmas/`.)

### 2. Corrected baseline step $b_n$ (repairing the round-3 outline's flaw)

**Definition.** For $n\ge1$ let $M_n$ be the smallest multiple of $R$
exceeding $a_n$, i.e. $M_n=R\cdot(\lfloor a_n/R\rfloor+1)$, and set
$$b_n:=M_n-a_n.$$

**Lemma (legality and boundedness of $b_n$).** For every $n\ge1$:
(a) $1\le b_n\le R$; (b) $\gcd(a_n+b_n,a_i)>1$ for **every** $i=1,\dots,n$
(so $a_n+b_n=M_n$ is a legal candidate for $a_{n+1}$ against the *entire*
prefix, not merely against $a_1$); (c) consequently $d_n\le b_n$.

**Proof.** (a) Rounding $a_n$ up to the next multiple of $R$ never
overshoots by more than $R$, and since $a_n$ is a positive integer not
already required to be a multiple of $R$ in general, $1\le b_n\le R$
(if $a_n$ happens to be a multiple of $R$, $b_n=R$; otherwise
$b_n=R-(a_n\bmod R)\in\{1,\dots,R-1\}$).

(b) This is exactly the content already established inside the certified
`lemmas/bounded-gap-via-rad-a1.md`: by its internal "Fact," every $a_i$
($i\ge1$) is divisible by some prime $p\in P:=R(a_1)$; since $R=\prod_{p\in
P}p$ divides $M_n=a_n+b_n$, in particular $p\mid M_n$, so $p\mid\gcd(M_n,
a_i)$, i.e. $\gcd(M_n,a_i)\ge p>1$. This holds for every $i=1,\dots,n$
simultaneously (unlike the flawed round-3 draft's $b_n$, which only used a
*single* prime shared with $a_1$ and gave no information about $a_i$,
$i\ge2$, covered by a possibly different prime of $R(a_1)$ — precisely the
gap the outline-reviewer flagged, citing `covering-membership-not-safety-
certificate.md`). Here, by contrast, divisibility of $M_n$ by *every* prime
of $P$ at once removes that gap entirely: whichever prime of $P$ covers
$a_i$, $M_n$ is divisible by it too.

(c) Since $M_n=a_n+b_n$ is a legal candidate for $a_{n+1}$ (satisfies $m>a_n$
and $\gcd(m,a_i)>1$ for all $i\le n$) and $a_{n+1}$ is by definition the
*smallest* such candidate, $a_{n+1}\le M_n$, i.e. $d_n=a_{n+1}-a_n\le
M_n-a_n=b_n$. $\blacksquare$

### 3. The exceptional-step indicator
Define $\epsilon_n:=\mathbb 1[d_n\ne b_n]\in\{0,1\}$ for $n\ge1$. By part (c)
above, $d_n\le b_n$ always, so $\epsilon_n=0$ exactly when the true greedy
step happens to coincide with the (always-legal, always-bounded) fallback
of jumping to the next multiple of $R$, and $\epsilon_n=1$ exactly when some
strictly smaller candidate exists (using a prime combination not reducible
to "all of $R(a_1)$ at once"). This $\epsilon_n$ is well-defined,
unconditionally, for every $n\ge1$; it is a new, valid statistic, distinct
from (and here correctly built on) the outline's original but flawed
$b_n$.

### 4. The central attempt (Step 4 of the outline) and its refutation

The outline's proposed mechanism was: is $\epsilon_{n+1}$ a function of only
a bounded-width window $(\sigma_{n-w+1},\dots,\sigma_n)$ of the compressed
pair statistic, for some fixed $w$? We show this is **false in general**,
first by exact computation, then by a complete closed-form proof.

**4.1 Computational search (exact integer arithmetic, no floating point).**
For $a_1\in\{15,21,33,35,55,63,65,99,105,231\}$ we generated the greedy
sequence exactly (using Python's arbitrary-precision integers and exact
`gcd`) up to several thousand terms, computed $(d_n,\ell_n,b_n,\epsilon_n)$
by the formulas above, and searched for the smallest window width $w$ at
which no two occurrences of the same length-$w$ window
$(\sigma_{n-w+1},\dots,\sigma_n)$ are followed by different values of
$\epsilon_{n+1}$. For $a_1=65,99$ no conflict was found once $w\ge13$ (but
see 4.3 below for why this is misleading, not a genuine automaton). For
$a_1=21$, **conflicts persisted for every tested window width up to
$w=599$** — i.e. no bounded window, however wide (within the tested range),
determines $\epsilon_{n+1}$.

**4.2 A complete, closed-form proof for $a_1=21$.**
We prove, by elementary induction with no computer assistance needed beyond
three initial gcd checks, that
$$a_n = 3(n+6)\quad\text{for every } n\ge1,\qquad\text{i.e. } a_{n+1}=a_n+3
\text{ for every } n\ge1.$$
(This is itself a complete solution of the problem for $a_1=21$, with
$T=1,\,L=3$ — a genuine, if narrow, positive by-product.)

*Base cases.* $a_1=21$ (given). Candidates for $a_2$: $22=2\cdot11$ has
$\gcd(22,21)=1$, invalid. $23$ is prime, $\gcd(23,21)=1$, invalid. $24=2^3
\cdot3$ has $\gcd(24,21)=3>1$, valid. So $a_2=24=3(2+6)$. Candidates for
$a_3$: $25=5^2$, $\gcd(25,21)=1$, invalid. $26=2\cdot13$, $\gcd(26,21)=1$,
invalid. $27=3^3$, $\gcd(27,21)=3>1$ and $\gcd(27,24)=3>1$, valid. So
$a_3=27=3(3+6)$.

*Inductive step.* Let $n\ge3$ and suppose $a_i=3(i+6)$ for $i=3,\dots,n$
(together with the fixed values $a_1=21,a_2=24$, both established above).
We show $a_{n+1}=a_n+3=3(n+7)$.

Key fact used repeatedly: $a_3=27=3^3$ has **only** the prime factor $3$.
Hence for any integer $m$ with $3\nmid m$, $\gcd(m,a_3)=\gcd(m,27)=1$, so
$m$ is *never* a legal candidate once $n\ge3$ (it fails the constraint
against $a_3$ alone).

- $a_n+1$: since $a_n=3(n+6)\equiv0\pmod3$, $a_n+1\equiv1\pmod3$, so
  $3\nmid(a_n+1)$; by the key fact, invalid.
- $a_n+2\equiv2\pmod3$, so $3\nmid(a_n+2)$; invalid, same reason.
- $a_n+3=3(n+7)$: divisible by $3$. Every earlier term $a_i$ ($i=1,\dots,n$)
  is divisible by $3$ (directly: $a_1=21=3\cdot7$, $a_2=24=3\cdot8$, and
  $a_i=3(i+6)$ for $3\le i\le n$ by the inductive hypothesis). Hence
  $3\mid\gcd(a_n+3,a_i)$ for every $i\le n$, so $\gcd(a_n+3,a_i)\ge3>1$:
  $a_n+3$ is a legal candidate.

Since $a_n+1$ and $a_n+2$ are excluded and $a_n+3$ is legal, minimality of
the greedy rule gives $a_{n+1}=a_n+3=3(n+7)=3((n+1)+6)$, completing the
induction. $\blacksquare$

**Consequence for $(d_n,\ell_n)$.** From $a_n=3(n+6)$ for all $n\ge1$:
$d_n=3$ for every $n\ge1$, and $\ell_n=\gcd(a_n,a_{n+1})=\gcd(3(n+6),3(n+7))
=3\gcd(n+6,n+7)=3\cdot1=3$ for every $n\ge1$ (consecutive integers are
coprime). So $\sigma_n=(d_n,\ell_n)=(3,3)$ **identically, for every
$n\ge1$** — the compressed pair statistic is not just eventually constant,
it is constant from the very first term. Any window of *any* width $w$,
at *any* position, reads the same key $((3,3),\dots,(3,3))$.

**Consequence for $\epsilon_n$.** Here $R=\mathrm{rad}(21)=21$. By the
formula $a_n=3(n+6)$, $a_n\bmod21 = 3\cdot\big((n+6)\bmod7\big)$ (since
$21=3\cdot7$, and multiplying residues mod $7$ by $3$ gives residues mod
$21$ that are multiples of $3$). By definition, $b_n=21-(a_n\bmod21)$ if
$a_n\bmod21\ne0$, and $b_n=21$ if $a_n\bmod21=0$.
- $a_n\bmod21=0 \iff (n+6)\bmod7=0\iff n\equiv1\pmod7$. In this case
  $b_n=21\ne3=d_n$, so $\epsilon_n=1$.
- $b_n=3 \iff a_n\bmod21=18 \iff (n+6)\bmod7=6\iff n\equiv0\pmod7$. In this
  case $b_n=3=d_n$, so $\epsilon_n=0$.
- For the remaining five residues $n\bmod7\in\{2,3,4,5,6\}$: $a_n\bmod21=
  3\big((n+6)\bmod7\big)\notin\{0,18\}$ (since $(n+6)\bmod7\notin\{0,6\}$),
  so $b_n=21-3\big((n+6)\bmod7\big)\in\{3,6,9,12,15\}\setminus\{3\}
  =\{6,9,12,15\}\ne3=d_n$: $\epsilon_n=1$.

So $\epsilon_n=0$ exactly when $7\mid n$, and $\epsilon_n=1$ otherwise — a
genuinely **period-7** function of $n$, verified directly and exactly
against the computed values ($n=21$: $7\mid21$, $\epsilon_{21}=0$ ✓;
$n=22$: $7\nmid22$, $\epsilon_{22}=1$ ✓, matching §4.1's search output).

**Theorem (refutation of Step 4, general form).** *If, for some $n_0$, the
pair sequence $(d_n,\ell_n)$ is constant $=(d^*,\ell^*)$ for all $n\ge n_0$
with $1\le d^*<R$, then, writing $g:=\gcd(d^*,R)$, the sequence $a_n\bmod R$
for $n\ge n_0$ runs exactly once around a coset of the subgroup $g\mathbb
Z/R\mathbb Z\le\mathbb Z/R\mathbb Z$ of size $R/g$ (since $a_{n+1}\equiv
a_n+d^*\pmod R$, i.e. $a_n\bmod R$ advances by the fixed step $d^*$ each
time, an orbit of exact period $R/g$ under addition of $d^*$ in $\mathbb
Z/R\mathbb Z$). If $R/g>1$ — equivalently $d^*\ne R$ (since $d^*\le R$
already) — then $b_n=R-(a_n\bmod R)$ (with the convention $0\mapsto R$)
takes $R/g\ge2$ distinct values as $n$ ranges over one period, so
$\epsilon_n=\mathbb1[d^*\ne b_n]$ is **not constant** on that period: it is
eventually periodic with exact period $R/g>1$ in $n$. Since a window
$(\sigma_{n-w+1},\dots,\sigma_n)$ reads the identical key $((d^*,\ell^*),
\dots,(d^*,\ell^*))$ at every position $n\ge n_0+w-1$ regardless of which
point of the period $n$ is at, **no function of any fixed-width window can
recover $\epsilon_{n+1}$** — the window carries zero information about the
absolute residue $a_n\bmod R$, which is exactly what $\epsilon_{n+1}$
depends on. $\blacksquare$*

The $a_1=21$ computation above is a fully verified, non-vacuous instance of
this theorem's hypothesis ($d^*=3<R=21$, $g=\gcd(3,21)=3$, period
$R/g=7>1$), so the refutation is not merely conditional — it is realized.
Since $a_1\in\{33,55,63,231\}$ were also observed (round 2,
`math-explorer-alt-framing.md`) to eventually lock to a constant gap
$d^*<R$, the same obstruction is expected to recur there (not re-derived
symbolically here for lack of remaining time, but consistent with §4.1's
computational search, which likewise found conflicts persisting to large
window widths for the non-locking $a_1=21,65,99$ tested).

**4.3 Why the "no conflict at $w=13$" findings for $a_1=65,99$ are not
evidence of a genuine automaton.** For those values, the search in §4.1
found only $\approx80$–$100$ *distinct* window keys among nearly $6000$
sampled windows (i.e. the raw sequence $(d_n,\ell_n)$ itself is already
repeating with a short period within the tested range — which is
unsurprising, since eventual periodicity of $(a_n)$, hence of $(d_n,
\ell_n)$, is exactly the theorem being sought). Testing "no conflict in a
window of width $w$" over a sample where the underlying sequence has
already entered its short eventual period is circular: it is really just
re-observing that the pair sequence is periodic there, not exhibiting an
independent local rule that could be used to *derive* periodicity. Hence
even the "successful" cases give **no actual evidence** that a bounded-order
automaton mechanism, as a proof technique, works — they are an artifact of
already being in the periodic regime.

### 5. Step 5 fallback (density of exceptional steps) — checked, unhelpful
The outline's fallback target was: if full bounded-order determinacy fails,
show at least that $(\epsilon_n)$ has bounded density (few exceptional
steps). §4.2's exact computation for $a_1=21$ shows the opposite: in the
regime where the refutation applies, $\epsilon_n=1$ for $6$ of every $7$
values of $n$ — density $6/7$, i.e. *high*, not low. The numerical data in
§4.1 for the other tested $a_1$ (fraction of $\epsilon_n=1$ ranging from
$\approx75\%$ to $\approx99\%$) is consistent with this: exceptional steps
are the overwhelming majority, not a sparse correction. So the fallback
target as stated does not hold in a useful direction, and this approach
does not currently produce any structural fact usable by the rest of the
population (e.g. `jacobsthal-covering-bound`'s $Q\setminus\Lambda$
finiteness target) beyond what is already certified.

### Summary of what is (and is not) established
- **Established, unconditional, for all $n\ge1$:** the Adjacent-Link Lemma
  (finite alphabet for $(d_n,\ell_n)$); the corrected, provably-legal
  baseline $b_n$ (gap to next multiple of $R$) with $d_n\le b_n\le R$; the
  well-definedness of $\epsilon_n$.
- **Established, unconditional, general negative theorem:** if $(d_n,
  \ell_n)$ is eventually constant at a value $d^*<R$, then $\epsilon_n$ is
  provably *not* a function of any bounded window of $(d_n,\ell_n)$ — it
  has genuine period $R/\gcd(d^*,R)>1$, invisible to any window of the
  (locally constant) pair sequence.
- **Established, unconditional, complete: solves the whole problem for
  $a_1=21$** ($T=1$, $L=3$), as a by-product of proving the hypothesis of
  the negative theorem is realized.
- **Refuted:** the outline's Step 4 target (bounded-order determinacy of
  $\epsilon_n$ from the compressed pair statistic) is false in general, not
  merely unverified — this specific mechanism does not extend to a proof of
  the problem's eventual periodicity.
- **Not established:** any positive path from the (correctly diversified,
  $Q$-free) finite-alphabet framing to the problem's conclusion. The
  approach currently has no mechanism left on the table beyond the refuted
  one; a genuinely different use of the finite alphabet $(d_n,\ell_n)$
  (not "windowed automaton on the compressed statistic") would be needed
  for this framing to make further progress.

## Full proof
(not present — Status is `partial`; the central mechanism of this approach
is refuted, and no replacement mechanism has been found this round. Full
solution obtained only for the single instance $a_1=21$, not for general
$a_1$.)

## Promotable lemmas

- **Adjacent-Link Lemma** — $\gcd(a_n,a_{n+1})=\gcd(a_n,d_n)\mid d_n\le R$
  for all $n\ge1$, giving a fixed finite alphabet for $(d_n,\ell_n)$.
  Proved in full in §1 above. (Coordinate with `jacobsthal-covering-bound`,
  which independently derives the identical statement — certify only one
  copy.)
- **Legal-baseline-step lemma** — $b_n:=$ gap to next multiple of
  $R=\mathrm{rad}(a_1)$ satisfies $1\le b_n\le R$ and is a legal candidate
  against *every* earlier term (not just $a_1$), hence $d_n\le b_n$ for all
  $n\ge1$. Proved in §2; this is a direct corollary of the already-certified
  `lemmas/bounded-gap-via-rad-a1.md`, stated here as a standalone,
  reusable fact (useful anywhere a *pointwise*, per-$n$ legal-and-bounded
  candidate is needed, as opposed to just the aggregate growth bound).
- **Windowed-$\epsilon$-automaton failure theorem** — if $(d_n,\ell_n)$ is
  eventually constant at $d^*<R$, then the exceptional-step indicator
  $\epsilon_n$ (relative to the legal-baseline-step lemma above) is
  eventually periodic with exact period $R/\gcd(d^*,R)>1$ and is **not** a
  function of any fixed-width window of $(d_n,\ell_n)$. Proved in full,
  unconditionally, in §4.2 (general statement) with a complete
  computation-free realized instance ($a_1=21$). Reusable as a standing
  warning against any future "compressed local automaton" mechanism
  proposed for this problem: any successful finite-state argument must
  track an *additive/cumulative* invariant (such as $a_n\bmod R$), not a
  purely relative sliding window of gaps.
- **Full solution for $a_1=21$** — $a_n=3(n+6)$ for all $n\ge1$ (so $T=1$,
  $L=3$ solve the problem for this specific instance). Proved in full in
  §4.2. Not directly reusable for the general problem, but usable as a
  concrete sanity-check instance for any future general mechanism (any
  correct general proof must reduce to this on substitution $a_1=21$).
