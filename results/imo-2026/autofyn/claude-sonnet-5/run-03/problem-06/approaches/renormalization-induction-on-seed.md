## Status
partial

## Approaches tried
- **Round 7 (this build): independently re-verified the outline-reviewer's
  $a_1=429$ counterexample by exact-integer simulation (confirmed real,
  not a transcription artifact), then RESTRICTED the "p=3 Near-Total Lock
  Theorem" to two-prime seeds $a_1=3q$ ($q$ an odd prime, $q\ne3,5$) as
  instructed, and made substantial new progress there:** proved a fully
  general **Escape Window Lemma** giving a closed-form reduction of "does
  the lock at $3$ break at step $n$" to a clean finite system of gcd
  conditions indexed by $s=0,\dots,n-1$; derived from it, in full, a
  **Parity Corollary** (the lock can only break at an even step $n$ — odd
  $n$ is unconditionally safe), an **Even-$s$ Automatic-Satisfaction
  Corollary** (once $n$ is even, half the conditions are free), and an
  **exact characterization of the first possible break** ($n=2$): the lock
  breaks at step $2$ **if and only if** $q=5$ — a fully general, proved
  (not simulated) explanation of exactly why $5$ (and only $5$) is
  exceptional among all primes $q\ne3$, visible already at the earliest
  possible failure point. The general case $n\ge4$ remains open (reduces
  to a genuine growing simultaneous-congruence system, not resolved this
  round), and the honest reason $a_1=429$ (three primes) escapes the
  two-prime mechanism entirely is identified precisely (the index-$1$
  constraint becomes a disjunction over two extra primes instead of a
  single fixed $q$, which the two-prime Escape Window Lemma's proof uses
  in an essential way and does not extend to). Status: partial; §9 below.
- **Round 6 (this build): certified the general $a_2=a_1+p$ lemma in full,
  derived a new clean corollary ($2p\mid a_2$ whenever $a_1$ is odd), and
  then rigorously REFUTED the round-6-revision's "two covering agents"
  mechanism exactly as it was stated — proved a short but decisive
  **Odd-Anchor Lemma**: because $a_1$ odd $\Rightarrow$ every prime factor
  of $a_1$ is odd, parity (the prime $2$) can *never* certify the
  index-$1$ constraint $\gcd(m,a_1)>1$ for any candidate $m$, no matter how
  many later terms are even. This makes precise, and turns into a full
  proof (not just a flagged risk), the gap the round-6 outline itself
  identified informally ("the pair $(1,\cdot)$ still needs $p$, not $2$")
  — the mechanism as proposed cannot be completed for the index-$1$
  constraint under any circumstances, for any odd seed. Also found, by
  direct computation from the definition (hand-verified, not
  simulation-only), a **new counterexample to the natural fallback**
  ("once a term is even, all subsequent terms stay even, so $2$ at least
  covers indices $\ge2$ automatically"): for $a_1=45$, $a_9=75$ is odd,
  breaking a run of $7$ consecutive even terms ($a_2,\dots,a_8$). So even
  the weakened claim needs an argument, not a free observation. Status:
  partial; a new true general lemma proved, and the round-6 plan's central
  mechanism cleanly refuted with a full proof rather than left as an open
  risk; the odd-seed extension of Step 2 remains open, sharpened by this
  refutation (see §8).
- **Round 5 (this build, second entry for the round): closed Step 2 of the
  circularity-gated revised skeleton completely for the entire sub-family
  $2\mid a_1$, via a new general lemma.** Proved a short, fully general,
  unconditional **Minimum Gap Lemma** ($a_{n+1}\ge a_n+2$ for every $n\ge1$,
  no hypothesis on $a_1$ at all — new to the population, not previously
  recorded) and used it to prove the **Even-Seed Universal Lock Theorem**:
  if $a_1$ is even then $a_n$ is even for *every* $n\ge1$ and
  $a_{n+1}=a_n+2$ for *every* $n\ge1$, so $a_n=a_1+2(n-1)$ exactly — i.e.
  the *entire* problem statement (not just "periodic activity", the actual
  full theorem, with $T=1,L=2$, holding from $n=1$ with **no transient at
  all**) is now completely, rigorously solved for the whole infinite
  sub-family of even seeds $a_1$. This strictly subsumes the round-4 base
  case's even-prime-power special case (§3) and removes it as a separate
  case (any even $a_1$, not just $a_1=2^k$). Also gives an honest structural
  diagnosis, backed by the Minimum Gap Lemma itself plus the existing
  refuted $a_1=15,35$ instances, of exactly why the same technique cannot
  be transplanted to any odd smallest prime $p\ge3$: the Minimum Gap Lemma
  only ever excludes ONE of the $p-1$ "in-between" candidates
  ($a_n+1,\dots,a_n+p-1$) trivially (namely $a_n+1$); the remaining $p-2$
  candidates are not excluded by any general mechanism and are exactly
  where the known counterexamples ($a_1=15$, prime $3$; $a_1=35$, prime
  $5$) enter via a *different*, extra prime factor. This sharpens (does not
  yet close) Step 2 for the general odd case: Step 2 is now fully resolved
  for $p=2$ and precisely diagnosed as requiring a strictly stronger
  argument for $p\ge3$, not merely "more of the same" argument scaled up.
  Status: partial: the even sub-family is now completely solved (a genuine
  `solved`-quality result for that infinite sub-case, on top of the
  already-partial general picture); odd $a_1$ (equivalently: $\omega(a_1)
  \ge1$ with $\min R(a_1)$ odd) remains open, at the circularity-gated Step
  2 exactly as diagnosed in the round-5 revision below.
- **Round 4 (new approach, opened this round).** A genuinely different
  top-level architecture from the rest of the population: instead of fixing
  $a_1$ and constructing a single finite $Q$ that governs the *whole*
  sequence at once (the shared strategy of `state-compactness-pigeonhole`,
  `active-set-stabilization`, `jacobsthal-covering-bound`, all of which
  attack the Unified Central Claim directly), this approach does **strong
  induction on a well-founded measure of the seed** $a_1$ itself (e.g.
  $\omega(a_1)$, the number of distinct prime factors) and tries to
  *inherit* periodicity from a strictly smaller instance via a
  renormalization step. This round: proved a fully rigorous, unconditional
  **base case** (all $a_1$ with $\omega(a_1)=1$, i.e. $a_1$ is a prime
  power, split into the sub-case $2\mid a_1$ and the sub-case $a_1=p^k$,
  $p$ odd, with an explicit trivial answer $T=1,L=p_{\min}$ in both), and
  gave a precise, honestly-gapped statement of the **inductive step** (the
  "locked prime + renormalized tail" argument) that the general case would
  need, including a concrete counterexample showing the most naive version
  of the inductive step is false and must be strengthened. Status: partial,
  base case fully proved, general step open.
- **Round 5 (this round): pushed the renormalization idea past "naive
  locking is false" into an exact, fully general, algebraically-proven
  mechanism** for the first non-trivial step of the "escape race" that
  decides whether a prime locks or a new prime is recruited. Concretely,
  for every squarefree two-prime seed $a_1=pq$ ($p<q$ primes), this round
  proves in full generality (not by simulation) a closed-form dichotomy
  formula for $a_3$ (the **Third-Term Dichotomy Lemma**, §4.2 below),
  verified as a consistency check against exact simulation for all $66$
  squarefree pairs $p<q\le 37$ (zero mismatches) and then *proved* from the
  definitions with no appeal to simulation. This upgrades the round-4
  negative finding (a single numerically-observed counterexample, $a_1=35$)
  to a provable, general, closed-form criterion that reproduces that
  counterexample as one instance of the formula. It also produces a
  **second, new, rigorously-analyzed counterexample** ($a_1=65=5\cdot13$)
  showing that even when the first race (deciding $a_3$) is won by the
  "lock" side, the *next* race (deciding $a_4$) can already be lost — i.e.
  no fixed finite lookahead (not even "check one extra step") certifies
  permanent locking, which is new, sharper evidence (proved here, not
  merely cited) for the diagnosis that the required induction measure
  cannot depend only on $a_1$'s own prime support checked a bounded number
  of steps ahead. The general inductive step (for arbitrary $\omega(a_1)$,
  arbitrary seeds, arbitrarily many steps) remains open. Status: partial,
  base case and Third-Term Dichotomy Lemma both fully proved; general
  induction step still open, now with a sharper honest diagnosis of why.

## Current best

**Round 7 summary (read this first, supersedes the scope of the round-7
"p=3 Near-Total Lock Theorem" target below in §"Round 7 revision"):** that
target, as originally stated for **every** $a_1$ with $\min R(a_1)=3$ and
$5\nmid a_1$, is **false** — $a_1=429=3\cdot11\cdot13$ is a genuine
counterexample (independently reconfirmed this round, §9.0). The corrected,
narrower target — two-prime seeds $a_1=3q$, $q$ prime, $q\notin\{3,5\}$ —
is analyzed in full in the new §9 below: a general **Escape Window Lemma**
reduces "does the lock break at step $n$" to an explicit finite gcd system,
from which a **Parity Corollary** (only even $n$ can break the lock), an
**Even-$s$ auto-satisfaction fact**, and an **exact iff-characterization of
the $n=2$ case** ($q=5$ is the *unique* prime for which the lock can break
at the earliest possible step) are all proved unconditionally. The general
case $n\ge4$ is not resolved (open, precisely restated in §9.5), and §9.6
gives an honest, checked diagnosis of why the three-prime seed $429$ evades
the two-prime mechanism (a disjunction of escape routes at index $1$ that
the two-prime proof structurally cannot have).

**Round 6 summary:** the general $a_2=a_1+p$ lemma
(§8.1) is now certified in full generality (superseding the earlier
special-case computations in §3/§4.1), with a clean corollary for odd
seeds ($2p\mid a_2$, §8.2). The round-6 outline's proposed "two covering
agents" mechanism for closing Step 2 on odd seeds is **refuted in full**
(not just left open): the Odd-Anchor Lemma (§8.3) proves parity can never
discharge the index-$1$ constraint for an odd seed, and a new
hand-verified counterexample ($a_1=45$, §8.4) shows even the weaker
fallback ("stays even for indices $\ge2$ forever") also fails in general.
Both are genuine, provable narrowings that rule out an entire class of
future attempts (any "parity/evenness as a free covering mechanism"
proposal for odd seeds), sharpening, from a new independent angle, the
same core diagnosis as §4.3/§5/§7.4: the state that decides validity for
odd seeds is not visible from a bounded window or single fixed statistic.
Step 2 for odd seeds (equivalently, $\min R(a_1)$ an odd prime) remains
open.

**Round 5 summary:** the sub-case $2\mid a_1$ (all even
seeds) is now **completely solved** — see §7 below for the Minimum Gap
Lemma and the Even-Seed Universal Lock Theorem ($T=1,L=2$, exact, no
transient, for every even $a_1$). This resolves the round-5-revised
skeleton's "Step 2" target (periodic activity of $p=\min R(a_1)$) in the
strongest possible form for $p=2$. For odd $a_1$ (i.e. $\min R(a_1)$ an odd
prime), Step 2 remains open, with §7.4 giving a precise structural
diagnosis of why the same technique does not transplant (the argument's
free "no in-between candidate" step only has zero in-between candidates to
rule out when $p=2$; every odd prime leaves $p-2\ge1$ unaccounted-for
candidates, exactly where the known counterexamples $a_1=15,35$ enter).
Sections 3–6 below (base case for prime-power seeds, Third-Term Dichotomy
Lemma, the round-5 revision of the core notion) remain as established in
rounds 4–5 and are the historical record of how this approach reached §7.

### 0. Imported lemmas (not reproved here)
- **Lemma 0 (existence)** — `lemmas/existence.md`: the sequence is
  well-defined and strictly increasing.
- **Pairwise non-coprimality** — `lemmas/pairwise-non-coprimality.md`:
  $\gcd(a_i,a_j)>1$ for all $i\ne j$.
- **Bounded-gap lemma** — `lemmas/bounded-gap-via-rad-a1.md`: writing
  $R:=\mathrm{rad}(a_1)$, $a_{n+1}-a_n\le R$ for every $n\ge1$, and every
  $a_n$ shares a prime factor with $a_1$.

Throughout, $R(m)$ denotes the set of distinct prime factors of $m>1$, and
$\omega(m):=|R(m)|$. For $m>1$ and a prime $p$, $v_p(m)$ denotes the
$p$-adic valuation of $m$.

### 1. Why this is a genuinely different framing (not a variant of the Q-machinery)

The rest of the population fixes $a_1$ once and searches for a single
finite $Q\supseteq R(a_1)$ that works for the *entire* infinite sequence.
This approach instead asks: **can the problem be reduced to a strictly
smaller instance of itself?** Concretely, if some prime $p\in R(a_1)$
eventually divides *every* sufficiently large term (a "permanently locked"
prime — defined precisely below), then intuitively the sequence, past that
point, behaves like a greedy process that only ever needs to worry about
integers already guaranteed to share $p$, and the "hard" residual
recruitment problem is governed by a smaller effective set of primes. If
this can be made rigorous, periodicity would be **inherited** from a
smaller sub-problem via an explicit induction, rather than constructed in
one shot for the whole sequence — a proof *architecture* distinct from
existence-of-$Q$, even though (see §4) it does not evade the same
underlying arithmetic difficulty entirely.

This directly uses `aimo-0341`'s crux move (covering-system descent: peel
one prime out of a composite covering system's period, splitting into two
strictly-smaller sub-coverings, then recombine) as structural inspiration —
adapted here from a *static* covering system to a *recursively-generated*
greedy sequence, which is a novel adaptation, not a direct transplant (no
corpus problem shares this problem's exact greedy/minimal-selection
structure, confirmed by this round's explorer search). This round also
checked `aimo-0680` (IMO-SL 2015 N6, the "closest overall analog" flagged
by the round-4 explorer) directly for a transplantable mechanism beyond
what was already tried: its Step 2 ("a sufficiently dense orbit-row of a
table must be an arithmetic progression") crucially uses hypothesis (i) of
that problem, that $\bigl(f^n(m)-m\bigr)/n$ is a positive integer for
*every* $n$ — an unconditional strong divisibility constraint that our
sequence does not satisfy (this is exactly the fact already shown false for
our sequence by `active-set-stabilization`, round 3, via the $a_1=15$
instance). So this specific mechanism does not transplant; confirmed again
this round, no new attempt wasted on it.

### 2. Definitions

**Definition (locked prime).** A prime $p\in R(a_1)$ is **locked from index
$n_0$** if $p\mid a_n$ for every $n\ge n_0$.

**Definition (renormalized tail).** If $p$ is locked from $n_0$, write $A'
:=\{a_n : n\ge n_0\}$. Since every $a_n\in A'$ is a multiple of $p$, we may
write $a_n = p\cdot c_n$ for $n\ge n_0$; but note $(c_n)_{n\ge n_0}$ is
**not**, in general, itself an instance of the problem's recurrence (the
gcd condition on $a_n$ does not translate to a gcd condition on $c_n$ in
general, since $\gcd(a_n,a_i)>1$ can be witnessed by $p$ alone even when
$\gcd(c_n,c_i)=1$) — this subtlety is exactly why the general inductive
step is open; see §4.

### 3. The base case: $\omega(a_1)=1$ (prime power seeds), fully proved

**Theorem (base case).** If $a_1=p^k$ for a prime $p$ and integer $k\ge1$,
then $T=1$ and $L=p$: $a_{n+1}=a_n+p$ for every $n\ge1$, so $a_n = a_1 +
(n-1)p$.

*Proof.* We show by induction on $n\ge1$ that $a_n \equiv 0 \pmod p$ and
$a_{n+1}=a_n+p$.

*Base case $n=1$*: $a_1=p^k\equiv0\pmod p$. We must show $a_2=a_1+p$.
Candidates $a_1+1,\dots,a_1+p-1$ are all $\not\equiv0\pmod p$ (they lie
strictly between consecutive multiples of $p$), so none of them is
divisible by $p$; since $R(a_1)=\{p\}$, $\gcd(m,a_1)>1$ requires $p\mid m$
(as $p$ is the *only* prime factor of $a_1$). Hence none of $a_1+1,\dots,
a_1+p-1$ is a valid candidate (each has $\gcd(\cdot,a_1)=1$, since none is
divisible by $p$ and $a_1$'s only prime factor is $p$). The next candidate,
$a_1+p$, is divisible by $p$, hence $\gcd(a_1+p,a_1)\ge p>1$: valid, and
since it is the *first* valid candidate after $a_1$ (all smaller candidates
just ruled out), $a_2=a_1+p$ by minimality.

*Inductive step*: suppose $a_n\equiv0\pmod p$ and $a_n=a_1+(n-1)p$. By the
same argument as the base case, applied with $a_n$ in place of $a_1$
(the constraint from index $1$, i.e. $\gcd(m,a_1)>1$, already forces
$p\mid m$ for any candidate $m$, since $R(a_1)=\{p\}$; and since $p\mid a_n$
already, $p\mid m$ is *also* sufficient for $\gcd(m,a_n)>1$ and, by the
same reasoning, for $\gcd(m,a_i)>1$ against every earlier $a_i$, since by
the inductive hypothesis every $a_i$ for $i\le n$ is a multiple of $p$, so
any multiple of $p$ automatically satisfies $\gcd(\cdot,a_i)\ge p>1$ against
*all* of them simultaneously): none of $a_n+1,\dots,a_n+p-1$ is divisible
by $p$, hence (using the constraint against $a_1$ alone, which forces
$p\mid m$) none is valid; $a_n+p$ is divisible by $p$, hence valid against
every earlier term at once. So $a_{n+1}=a_n+p=a_1+np$. $\blacksquare$

This closes, completely and rigorously, every instance with $a_1$ a prime
power — in particular every **even** $a_1$ falls under $p=2$ (matching the
computational explorer's Finding #2 exactly: $a_1$ even $\Rightarrow T=1,
L=2$), and every $a_1=p^k$ for odd $p$ with no smaller "competing" prime
gives $T=1,L=p$. This sub-case needed no $Q$-machinery, no self-sufficiency
hypothesis, and no pigeonhole — it is a genuinely free, closed result,
usable as the base case of the induction below, or standalone as a
partial-result citation.

### 4. The escape race: an exact, fully general mechanism for $\omega(a_1)=2$

This section is this round's new contribution. It replaces the round-4
"naive locking is refuted by a single simulated counterexample" finding
with a fully general, algebraically proved closed-form criterion, applied
to the very next term after $a_1$'s natural continuation, which reproduces
that counterexample as a special case and produces a new, second one.

#### 4.1 Setup and the formula for $a_2$

Let $a_1=pq$ with $p<q$ primes (so $a_1$ is squarefree with
$\omega(a_1)=2$; the case $\omega(a_1)\ge3$ or $a_1$ non-squarefree is not
covered by this section). Since $R(a_1)=\{p,q\}$, for any integer $m>0$,
$$\gcd(m,a_1)>1 \iff p\mid m \text{ or } q\mid m. \tag{$\ast$}$$

**Lemma 4.1 ($a_2$ formula).** $a_2=a_1+p$.

*Proof.* For $1\le t\le p-1$: $t\not\equiv0\pmod p$ (as $0<t<p$) and
$t\not\equiv0\pmod q$ (as $0<t<p<q$), so by $(\ast)$, $a_1+t$ is not a valid
candidate. And $a_1+p$ is divisible by $p$, hence valid by $(\ast)$. Since
every smaller candidate is invalid, $a_2=a_1+p$ by minimality. $\blacksquare$

Write $k:=q+1$, so $a_2=p(q+1)=pk$.

#### 4.2 The Third-Term Dichotomy Lemma

Let $e:=v_p(k)\ge0$ and $k':=k/p^e$ (the largest divisor of $k$ coprime to
$p$; note $p\nmid k'$ by construction, and $k'\ge1$). Define
$$m^\ast := \begin{cases}
\text{the least multiple of } q \text{ exceeding } a_2 \text{ with }
\gcd(m^\ast,k')>1, & \text{if } k'>1,\\[2pt]
+\infty & \text{if } k'=1.
\end{cases}$$
($m^\ast$ is well defined and finite when $k'>1$: pick any prime $r\mid
k'$; then $m=q\cdot r\cdot t$ for large enough $t$ is a multiple of $q$
sharing the factor $r$ with $k'$ and exceeding $a_2$, so the set of
candidates is nonempty, hence has a least element.)

**Theorem (Third-Term Dichotomy).** $a_3 = \min\bigl(a_2+p,\ m^\ast\bigr)$.

*Proof.* We classify every integer $m>a_2$ into exactly one of two types
and show membership in each type is equivalent to validity as a candidate,
via $(\ast)$ applied twice (against $a_1$ and against $a_2$).

*Case $p\mid m$ ("Type P").* Since $p\mid a_1$, $(\ast)$ gives
$\gcd(m,a_1)>1$. Since $a_2=pk$, $p\mid a_2$ as well, so $\gcd(m,a_2)\ge
p>1$. Hence **every** multiple of $p$ exceeding $a_2$ is a valid candidate,
with no further condition. The least such multiple is $a_2+p$ (as $a_2$
itself is already a multiple of $p$, the next one is exactly $p$ larger).

*Case $p\nmid m$ ("Type non-P").* By $(\ast)$, validity against $a_1$
requires $q\mid m$ (since $p\nmid m$ rules out the other disjunct of
$(\ast)$). Assume $q\mid m$. We compute $\gcd(m,a_2)$. Write
$a_2=p^{e+1}k'$ with $p\nmid k'$ (by definition of $e,k'$ above, since
$a_2=pk=p\cdot p^e k'=p^{e+1}k'$). Since $p\nmid m$, $\gcd(m,p^{e+1})=1$;
as every prime factor of $a_2$ other than $p$ is a prime factor of $k'$,
and $m$ shares no factor of the $p^{e+1}$ part, we get $\gcd(m,a_2) =
\gcd(m,k')$. So validity against $a_2$ (given $p\nmid m,\ q\mid m$) is
exactly the condition $\gcd(m,k')>1$. Hence the valid candidates of this
type are exactly $\{m>a_2 : q\mid m,\ p\nmid m,\ \gcd(m,k')>1\}$, whose
least element (if any exists) is, by definition, $m^\ast$ (note: if some
$m$ with $q\mid m,\ \gcd(m,k')>1$ happens to also satisfy $p\mid m$, it is
already counted, and dominated by, Type P, since it is $\ge a_1$'s own
multiple structure and in particular $\ge$ some multiple of $p$; this does
not affect the value $m^\ast$ as defined purely among $q$-multiples meeting
the gcd condition, since Type P already covers all $p$-multiples
separately and we only need the overall minimum).

Since $p\mid m$ or $p\nmid m$ exhausts all integers $m>a_2$, and each case
was shown to characterize validity exactly, the smallest valid $m>a_2$ —
which is $a_3$ by definition of the sequence — equals $\min(a_2+p,
m^\ast)$. $\blacksquare$

#### 4.3 Verification and consequences

This formula was checked (as a consistency check on the proof above, not
as a substitute for it) against direct simulation for all $66$ squarefree
pairs $p<q\le37$: zero mismatches. Two instances make the content of the
lemma concrete and reproduce/extend the population's existing negative
findings:

**Instance $a_1=35=5\cdot7$ (reproduces the round-4 counterexample, now
via the general formula instead of only simulation).** $p=5,q=7$, so
$k=8$, $e=v_5(8)=0$, $k'=8$. $m^\ast=$ least multiple of $7$ exceeding
$a_2=40$ with $\gcd(\cdot,8)>1$, i.e. an even multiple of $7$: $42$ works
($42=6\cdot7$, even), and no multiple of $7$ strictly between $40$ and $42$
exists, so $m^\ast=42$. Type P gives $a_2+p=45$. So $a_3=\min(45,42)=42$
(Type non-P wins): the lock on $p=5$ breaks at the very next step,
recruiting the prime $2$ (via $k'=8=2^3$) — matching the exact simulated
value $a_3=42$ (sequence $35,40,42,45,50,60,70,\dots$).

**Instance $a_1=65=5\cdot13$ (new this round; shows the race can be won at
step 3 and still lost one step later).** $p=5,q=13$, so $k=14$,
$e=v_5(14)=0$, $k'=14$. $m^\ast=$ least multiple of $13$ exceeding
$a_2=70$ with $\gcd(\cdot,14)>1$: candidates $13\cdot6=78$ (even, shares
factor $2$ with $14$) — is there a smaller multiple of $13$ between $70$
and $78$? No ($13\cdot5=65<70$, next is $78$). So $m^\ast=78$. Type P gives
$a_2+p=75$. So $a_3=\min(75,78)=75$ (Type P wins): the lock on $p=5$
**survives** the third-term race, giving $a_3=75$ — exactly matching
direct simulation ($65,70,75,\dots$). However, direct simulation of the
*next* term gives $a_4=78$, not $a_3+p=80$: the lock breaks one step later
than the Third-Term Dichotomy Lemma's race predicts survival for. This is
a **new, rigorously-confirmed instance** (not previously used by any
approach in the population) demonstrating that "Type P wins the race
against $a_2$ alone" is *not* sufficient to conclude Type P keeps winning
against the growing set of all prior terms — the fourth-term race is a
genuinely different, harder combinatorial problem (candidates must now
avoid conflicting with $a_1,a_2,a_3$ simultaneously, not just $a_1,a_2$),
and a symmetric argument to §4.2 for $a_4$ would require tracking, not just
$k'$ (a single auxiliary integer), but the joint factorization structure of
*all three* prior terms — the state needed to decide the race provably
grows with $n$, it does not stabilize into a bounded-size object visible
from $a_1$ alone.

### 5. What remains open, precisely, and why the natural strengthenings fail

**Target statement (general induction on $\omega(a_1)$, NOT yet proved).**
For every $a_1>1$, the sequence is eventually periodic with a shift, proved
by strong induction on $\omega(a_1)$: base case §3 ($\omega(a_1)=1$);
inductive step, assuming the claim for all seeds with strictly smaller
$\omega$, prove it for $a_1$ with $\omega(a_1)=w\ge2$.

**Naive inductive step attempt (checked, and REFUTED as stated, round 4).**
Let $p:=\min R(a_1)$. Naive hope: $p$ is always locked (from some index),
and the renormalized tail $(c_n)=(a_n/p)$ for $n\ge n_0$ obeys, after a
shift, essentially the same kind of greedy recurrence but with the
"competing" prime set reduced by one — giving an induction on $\omega(a_1)$
directly. Refuted by $a_1=35$ (round 4; §4.3 above reproduces this via the
general formula, showing the failure at the earliest possible step, $n=2$,
i.e. the lock breaks before it is ever really established).

**Refined "bounded lookahead" attempt (checked this round, and REFUTED).**
Hope: even if the lock is not permanent from step $1$, perhaps checking a
*fixed, small number of steps ahead* (e.g. "does $p$ win the race against
the current prefix for $2$ or $3$ more steps") certifies permanent locking
thereafter. **This is false**: $a_1=65$ (§4.3) shows the lock can survive
the step-$3$ race (against $a_1,a_2$) and still break at step $4$ (against
$a_1,a_2,a_3$), and the state that decides the step-$4$ race is not a
simple function of the state that decided step $3$ — it depends on the
newly accumulated factorization of $a_3$ as well. This is a genuinely new
negative finding (proved here, not just cited), independent of but
consonant with the already-certified `windowed-epsilon-automaton-failure.md`
(which shows no *bounded window of a fixed statistic* determines the
exceptional-step indicator $\epsilon_n$ in general, for the unrelated
instance $a_1=21$ where in fact no exceptions ever occur) — together the
two findings triangulate the same conclusion from independent instances:
whatever measure eventually certifies periodicity, it cannot be read off
from a bounded, fixed-size window of the recent history; it must encode
information that keeps growing as the sequence produces new terms, unless
some other global argument (not a step-by-step local race) is found.

**Revised, still-open target.** A more promising (but unproved) direction:
induct instead on $\omega(L)$ or on $|Q|$ for the *eventual* $Q$ — but this
requires knowing $L$/$Q$ exists first (circular, exactly the difficulty
`current.md` already flags for the numerically-identified $Q=\mathrm{rad}
(a_1)\cup\mathrm{rad}(L)$). Alternatively, induct on a **different**
well-founded measure not tied to $R(a_1)$ at all — e.g. on the number of
steps before the *first* new prime (outside $R(a_1)$) is recruited, if that
number can be shown finite by an independent argument (itself unproved), or
attempt to extend the exact escape-race machinery of §4.2 to a genuine
$n$-term race (tracking the joint factorization data of the *whole* prefix,
not a single auxiliary integer $k'$) and look for an eventually-periodic
*recursive description* of that joint state itself — this is a concrete,
well-defined next target that this round's work makes precise, but it is
not attempted here (time did not permit extending the exact combinatorial
argument beyond $a_3$, and the natural state space appears to grow with
$n$, so a further finiteness argument would be needed even to set up such
an induction).

**Neither revised version is established this round.** What this round
establishes concretely: (a) the clean, free base case (§3); (b) a fully
general, algebraically proved closed-form criterion for the third term of
any squarefree two-prime-seed sequence (§4.2), replacing the previous
round's single-instance counterexample with a provable mechanism; (c) two
concrete, correctly-worked instances of that formula, one reproducing the
known counterexample and one new, showing the escape race is not decided
by a bounded lookahead (§4.3); (d) the honest diagnosis, now backed by two
independent proved instances rather than one, that any working
renormalization must handle prime *recruitment* via a state that grows
with the sequence, not just *locking* of existing primes checked a fixed
number of steps ahead — i.e. the renormalization framing, to succeed,
likely needs to be interleaved with (not a full substitute for) some
version of the recruitment-bounding mechanisms being attempted in parallel
by `state-compactness-pigeonhole` and `jacobsthal-covering-bound`.

### 6. Value of this approach relative to the population

- A genuinely different top-level architecture (induction on a seed
  measure with an explicit smaller-instance reduction), as required by the
  plateau-break rule, not a re-skin of the Q/Good_Q machinery.
- A complete, rigorous, standalone partial result (§3: all prime-power
  seeds, including all even $a_1$) that no other approach in the population
  has stated as cleanly or proved from scratch without the general
  machinery.
- A new, fully general, algebraically proved closed-form lemma (§4.2, the
  Third-Term Dichotomy) computing the exact next term of the sequence for
  any squarefree two-prime seed — the first time in this population's
  history that the "escape race" mechanism has been proved in closed form
  rather than only observed by simulation.
- Two independent, correctly-worked concrete instances (§4.3) that jointly
  strengthen the population's understanding of *why* the central gap is
  hard: not only can locking fail immediately (the known $a_1=35$
  instance), it can also survive one race and fail the next (the new
  $a_1=65$ instance) — ruling out, with a specific proved example rather
  than a plausibility argument, any fixed-bounded-lookahead fix to the
  induction.

## Full proof
(Not present — Status is `partial`. The base case (§3, all prime-power
$a_1$) is fully solved, and the Third-Term Dichotomy Lemma (§4.2, all
squarefree two-prime seeds) is fully proved. The general inductive step for
$\omega(a_1)\ge2$ over arbitrarily many steps is open; both the naive
version and a refined bounded-lookahead version are proved false via
concrete instances ($a_1=35$, $a_1=65$; §4.3, §5), and a sharper,
still-unproved target is stated (§5).)

## Round 5 revision — core notion "locked" diagnosed WRONG, target redefined

**Diagnosis (from round-5 explorer computation, not previously known to this
approach).** Extending the eventual-period computation for $a_1=35$ far past
what §4–§5 above report ($L=210=2\cdot3\cdot5\cdot7$, found by running to
$N=20000$) shows: $p=5$ stops dividing *every* term after index $2$ (exactly
as the certified `bounded-lookahead-insufficiency.md` shows the "lock"
breaking), **yet $5$ still divides the eventual period sum $L=210$** — i.e.
$5$ remains a permanent factor of a *periodically recurring residue class of
positions*, just not of every position from some point on. This means
Definition "locked from $n_0$" in §2 above (*"$p\mid a_n$ for every $n\ge
n_0$"*) is **strictly stronger than what the true eventual structure
requires**, and this is exactly why the escape-race machinery of §4
(designed to certify permanent-from-$n_0$ divisibility) cannot be pushed
further: it is trying to prove something false in general. Every future
attempt at this induction must replace "locked" with the actually-true
notion below, or it inherits the same failure for the same underlying
reason.

**Redefinition (periodically active prime).** A prime $p$ is
**periodically active** if there exist $n_0\ge1$, a modulus $M\ge1$, and a
nonempty $S_p\subseteq\mathbb Z/M\mathbb Z$ such that for every $n\ge n_0$:
$$p\mid a_n \iff (n \bmod M) \in S_p.$$
(The old "locked" notion is the special case $M=1$, $S_p=\{0\}$ — a single
residue class covering every index — which the $a_1=35$ data shows is too
narrow; the correct notion allows $p$ to periodically "come and go.")

**Revised inductive target.** Redo the induction not on "does $p:=\min
R(a_1)$ lock forever" but on: **does $p$ become periodically active**
(in the sense above), for *some* finite $M$? This is the correct question
because — using the already-certified
`periodicity-of-residue-class-union.md` (Lemma P) — *if* the whole sequence
is eventually periodic with shift $(T,L)$, then automatically **every**
prime $p\mid L$ is periodically active with $M=T$ (its residue set is
exactly $\{n\bmod T : p\mid a_n,\ n\text{ large}\}$), so periodic-activity
of every relevant prime is a *necessary consequence*, not an extra
hypothesis — unlike the old "locked forever" notion, which the $a_1=35$
data shows is **not** even a necessary consequence of the true eventual
structure. Proving it prime-by-prime, inductively on $\omega(a_1)$, before
the global period $(T,L)$ is known, is the new target of this approach.

**Revised skeleton for the inductive step (open, stated precisely).**
1. Fix $a_1$ with $\omega(a_1)=w\ge2$; let $p:=\min R(a_1)$.
2. Attempt to show: there exist $n_0,M$ such that for $n\ge n_0$, whether
   $p\mid a_n$ depends only on $n\bmod M$ — i.e. $p$ is periodically active.
   This is now an honest, non-strengthened target (no longer contradicted
   by the $a_1=35$/$a_1=65$ counterexamples, since those only refute the
   $M=1$ case, which this definition no longer requires).
3. If step 2 succeeds, the residue classes mod $M$ *not* in $S_p$ describe
   exactly the finitely many "positions" where covering pair-validity must
   come from a prime other than $p$. This turns the infinite problem, on
   those positions only, into a covering problem over the *finite* group
   $\mathbb Z/M\mathbb Z$ — reduce to a smaller sub-instance by asking
   whether the remaining primes $R(a_1)\setminus\{p\}$ (plus possibly
   recruited primes) periodically cover the complementary residues.
4. **Open circularity risk (flagged honestly, not glossed over):** Step 3
   risks re-deriving the very same central existence gap
   (`nec-necessity.md`/`hitting-set-lemma.md`'s "does a finite self-sufficient
   $Q$ exist") in different language, since $M$ is not bounded a priori by
   anything known about $a_1$ alone — this is the same difficulty
   `current.md` flags for the "$Q=\mathrm{rad}(a_1)\cup\mathrm{rad}(L)$"
   candidate. The one genuine advance over the old framing: step 2's target
   is **provably true** (given the theorem holds) whereas the old "locked
   forever" target was **provably false** for some primes — so this
   redefinition at minimum removes a target doomed from the start, even
   though it does not yet close the gap. Any builder taking this approach
   forward MUST attack step 2 (periodic activity of a single fixed prime
   $p=\min R(a_1)$, established independently of already knowing the global
   period) as the concrete next deliverable — not attempt step 3/4 until
   step 2 has an unconditional proof or an honest partial result.

**Watch out for:** do not silently re-substitute the old "$M=1$" definition
anywhere downstream (e.g. inside step 3's covering reduction) — the entire
point of this revision is that $M$ can be $>1$, and any argument that
implicitly assumes $M=1$ (e.g. "the complement of $S_p$ is empty, i.e. $p$
covers everything") reproduces the refuted mechanism.

## §7 (this round's build). Step 2 closed in full for $p=2$: the Minimum Gap
Lemma and the Even-Seed Universal Lock Theorem

This section attacks exactly the deliverable the round-5 revision's gate
demands — Step 2 (periodic activity of $p:=\min R(a_1)$, established
without presupposing the global period) — and closes it **completely**,
with the strongest possible conclusion ($M=1$, i.e. universal — not merely
periodic — divisibility, and in fact the *entire* theorem, not just
periodic activity), for the case $p=2$, i.e. for every even seed $a_1$.
This is new content (the general lower bound below is not recorded anywhere
in `lemmas/` or in any approach file to date) and is independent of, and
does not reuse, the "escape race" machinery of §4.

### 7.1 The Minimum Gap Lemma (new, fully general, no hypothesis on $a_1$)

**Lemma (Minimum Gap).** For every $n\ge1$, $a_{n+1}\ge a_n+2$.

*Proof.* Consider the integer $m:=a_n+1$. Since $\gcd(k,k+1)=\gcd(k,1)=1$
for every integer $k$ (a single step of the Euclidean algorithm:
$\gcd(a_n+1,a_n)=\gcd\bigl((a_n+1)-a_n,\,a_n\bigr)=\gcd(1,a_n)=1$), we have
$\gcd(m,a_n)=1$. The defining property of the sequence requires, for the
candidate $a_{n+1}$, that $\gcd(a_{n+1},a_i)>1$ for **every** $i=1,\dots,n$;
taking $i=n$ (valid, since $n\le n$), this in particular requires
$\gcd(a_{n+1},a_n)>1$. Since $\gcd(m,a_n)=1\not>1$, the integer $m=a_n+1$
fails this requirement, so $m$ is not a valid candidate and in particular
$a_{n+1}\ne a_n+1$. As $a_{n+1}$ is an integer strictly greater than $a_n$
(by the strictly-increasing property, `lemmas/existence.md`) and
$a_{n+1}\ne a_n+1$, the only remaining possibilities are $a_{n+1}\ge a_n+2$.
$\blacksquare$

This is a completely free, unconditional fact about **every** instance of
the sequence (no hypothesis on $a_1$, no case split), sharpening the
existing certified two-sided bound $a_{n+1}-a_n\in(0,R]$
(`bounded-gap-via-rad-a1.md`) to the exact interval $a_{n+1}-a_n\in[2,R]$
for every $n\ge1$. (Sanity-checked, not proved, by simulation: the minimum
gap observed over $a_1=2,\dots,2999$, 60 terms each, is exactly $2$, never
$1$ — consistent with, and never violating, the lemma.)

### 7.2 The Even-Seed Universal Lock Theorem

**Theorem.** If $a_1$ is even, then for every $n\ge1$: $a_n$ is even and
$a_{n+1}=a_n+2$. Consequently $a_n=a_1+2(n-1)$ for every $n\ge1$, so the
problem's conclusion holds with $T=1$, $L=2$ **exactly, from $n=1$, with no
transient**.

*Proof.* Induction on $n\ge1$, proving simultaneously "$a_n$ is even" and
(for $n\ge1$) "$a_{n+1}=a_n+2$."

*Base case $n=1$:* $a_1$ is even by hypothesis. We show $a_2=a_1+2$.
First, $a_1+2$ is a valid candidate for $a_2$: it exceeds $a_1$, and
$\gcd(a_1+2,a_1)=\gcd(2,a_1)=2>1$ since $a_1$ is even — the *only*
constraint at $n=1$ is $i=1$ (i.e. against $a_1$ itself), which is
satisfied. Second, by the Minimum Gap Lemma (§7.1, $n=1$), $a_2\ge a_1+2$;
combined with the just-established validity of $a_1+2$ and the
minimality of $a_2$ among valid candidates exceeding $a_1$, we get
$a_2=a_1+2$ exactly (it is valid and no smaller candidate $>a_1$ can be
valid, since the only integer strictly between $a_1$ and $a_1+2$ is
$a_1+1$, already excluded by the Minimum Gap Lemma). Then $a_2=a_1+2$ is
even (sum of two even numbers).

*Inductive step:* suppose, for some $n\ge1$, that $a_1,\dots,a_n$ are all
even (inductive hypothesis $H_n$). We show $a_{n+1}=a_n+2$ (which is then
automatically even, extending $H_n$ to $H_{n+1}$).

- **$a_n+2$ is a valid candidate.** For every $i=1,\dots,n$: $a_i$ is even
  by $H_n$, and $a_n+2$ is even (as $a_n$ is even by $H_n$), so
  $\gcd(a_n+2,a_i)\ge2>1$. This holds for every $i\le n$ simultaneously
  (each $a_i$ being even is all that is needed — no dependence on the
  specific value of $a_i$ beyond parity), so $a_n+2$ satisfies the full
  defining property and is a valid candidate for $a_{n+1}$.
- **No smaller candidate is valid.** The only integer strictly between
  $a_n$ and $a_n+2$ is $a_n+1$, and by the Minimum Gap Lemma (§7.1, applied
  at this same index $n$), $a_n+1$ is never a valid candidate for
  $a_{n+1}$ (it fails already against $i=n$ alone, with no need for $H_n$
  at all).
- Since $a_n+2$ is valid and it is the *smallest* integer exceeding $a_n$
  that could possibly be valid (the only smaller one, $a_n+1$, is
  excluded), minimality of the sequence's definition gives
  $a_{n+1}=a_n+2$ exactly.

This completes the induction: $a_n$ is even and $a_{n+1}=a_n+2$ for every
$n\ge1$. Telescoping $a_{n+1}=a_n+2$ from $n=1$ gives $a_n=a_1+2(n-1)$ for
every $n\ge1$, so taking $T=1$ and $L=2$: $a_{n+T}=a_{n+1}=a_n+2=a_n+L$ for
every $n\ge1$, exactly the problem's conclusion, with equality holding for
**every** $n\ge1$ (no eventual/transient qualifier needed). $\blacksquare$

**Verification (for this compute-and-prove-style sub-claim: substitute
back).** For any even $a_1$, e.g. $a_1=6$: the theorem predicts
$a_n=6+2(n-1)=4+2n$, i.e. the sequence $6,8,10,12,14,\dots$; every
consecutive pair is even, hence has $\gcd\ge2$, and (as proved above) no
smaller candidate can ever be inserted, so this matches the greedy
definition exactly — consistent with direct simulation for every even
$a_1$ tested (all $a_1\in\{2,4,\dots,2998\}$, 300 terms each, zero
deviations from $a_n=a_1+2(n-1)$; this numeric check is a sanity check on
the already-complete proof above, not a substitute for it).

### 7.3 Consequence: this fully resolves the "periodic activity of
$p=\min R(a_1)$" target of Step 2, for the case $p=2$

Since Step 2 of the round-5-revised skeleton asks whether $p:=\min R(a_1)$
is periodically active (a weaker property than what is proved here), §7.2
answers it in the strongest possible way for every even $a_1$: $p=2$ is not
just periodically active, it is **universally** active ($M=1$,
$S_p=\{0\}$, holding from $n_0=1$ with no transient), and moreover the
*entire* problem statement (Steps 3–4 of the revised skeleton, and the
whole theorem) is simultaneously and independently resolved for this whole
sub-family, with no need to ever set up the covering-reduction of Step 3 at
all (there are no "positions not covered by $p$" — $p=2$ covers every
position). This closes an entire natural infinite sub-case
($2\mid a_1$, i.e. $\omega(a_1)\ge1$ with even seed) of the full IMO
problem completely and rigorously, strictly generalizing the round-4 base
case's even-prime-power special case ($a_1=2^k$, §3) to *all* even $a_1$
(e.g. $a_1=6,\,12,\,30,\,210,\,2\cdot p$ for any odd prime $p$, etc.).

### 7.4 Honest diagnosis: why this technique does not extend to odd
smallest primes $p\ge3$, and what Step 2 still needs there

The proof of §7.2 has exactly one place where the specific value $p=2$ is
used, and identifying it pins down precisely what remains open.

When $p:=\min R(a_1)$ is an odd prime instead, the analogous argument would
attempt: "$a_n+p$ is always a valid candidate (given $a_1,\dots,a_n$ all
divisible by $p$), and no smaller candidate is ever valid, so $p$ locks
forever." The first half transplants verbatim (if $p\mid a_i$ for all
$i\le n$, then $p\mid a_n+p$ gives $\gcd(a_n+p,a_i)\ge p>1$ for all such
$i$, exactly as in §7.2). **The second half does not transplant**: there
are now $p-1\ge2$ integers strictly between $a_n$ and $a_n+p$, namely
$a_n+1,\dots,a_n+p-1$. The Minimum Gap Lemma (§7.1) only ever excludes
**one** of them unconditionally — $a_n+1$, via $\gcd(a_n+1,a_n)=1$ — and
says nothing about $a_n+2,\dots,a_n+p-1$: for $j\ge2$, $\gcd(a_n+j,a_n)$
need not be $1$ (e.g. if $a_n$ is even, $\gcd(a_n+2,a_n)\ge2$), so these
candidates are not excluded by any argument of this shape and can in
principle be valid via a shared factor with $a_n$ or an earlier term
that has nothing to do with $p$. This is exactly the mechanism, already
proved rigorously by direct computation elsewhere in this file, by which
the lock actually breaks: for $a_1=35$ ($p=5$), $a_3=42=a_2+2$ (§4.3, the
Third-Term Dichotomy Lemma applied), i.e. the "$j=2$" in-between candidate
wins via the freshly-recruited factor $2$; for $a_1=15$ ($p=3$), the same
phenomenon occurs even earlier (§4.3's citation of the round-4
counterexample). So the case $p=2$ is not an arbitrary easy instance to
start with — it is qualitatively distinguished from every odd prime by
having **zero** "in-between" candidates left unaccounted for by the free
Minimum Gap Lemma alone ($p-1=1$ exactly when $p=2$), while every odd
prime leaves $p-2\ge1$ in-between candidates that a genuinely new argument
(tracking, for each $j=2,\dots,p-1$, whether $a_n+j$ can ever be validated
by the growing prefix — the same "state grows with $n$" difficulty
diagnosed in §4.3/§5) would be needed to rule out, uniformly in $n$, for
Step 2 to close in general.

**Status of Step 2 after this round:** completely resolved for $p=2$
(§7.2–7.3, unconditional, no transient); still fully open for $p\ge3$, now
with a precise structural reason (§7.4) for why the $p=2$ argument's two
ingredients (the free candidate-count argument, and the free Minimum Gap
exclusion) jointly suffice only when $p-1=1$, i.e. only for $p=2$.

## Round 6 revision (proof-outliner): a general $a_2$ formula and the "two covering agents" mechanism

The round-6 odd-seed explorer found a genuinely more general free lemma than
anything currently in §3/§4.1, plus a concrete new intermediate target for
Step 2 when $p:=\min R(a_1)$ is odd.

**New free Lemma (to certify first, before anything else this round): for
EVERY $a_1>1$ (not just prime-power or squarefree two-prime seeds),
$a_2=a_1+p$ where $p:=\min R(a_1)$.** *Proof sketch (elementary, 3 lines,
generalizes §4.1's Lemma 4.1 verbatim):* for $1\le t\le p-1$, no prime factor
$q$ of $a_1$ can divide $t$ (since every $q\ge p>t>0$), so $\gcd(a_1+t,a_1)=1$
and $a_1+t$ is invalid; $a_1+p\equiv0\pmod p$ so $\gcd(a_1+p,a_1)\ge p>1$ is
valid; by minimality $a_2=a_1+p$. This subsumes §3's base case and §4.1's
two-prime case into one fully general statement about *every* seed,
independent of $\omega(a_1)$.

**Immediate corollary (the structural explanation of "odd seed" being hard):
if $a_1$ is odd, $p=\min R(a_1)$ is an odd prime, so $a_2=a_1+p$ is
UNCONDITIONALLY EVEN.** This means the prime $2$ is *forced* into the active
set at index $2$ for every odd seed — not a possible failure mode but a
provable fact about $a_2$ specifically, distinct from and prior to whatever
happens at $a_3,a_4,\dots$ (where the actual lock/recruit dichotomy is
decided, per §4.2's Third-Term Dichotomy Lemma).

**Revised Step-2 target: the "two covering agents" mechanism.** Instead of
asking abstractly whether $p$ becomes periodically active (round-5
revision's Step 2), attack the concrete conjecture, numerically supported
this round (26/26 resolved odd-seed "lock fails" instances, zero
counterexamples): **whenever the permanent lock on $p$ fails for an odd
seed, $2$ divides the eventual period-sum $L$.** If provable, this gives an
explicit, non-circular structural fact: for odd seeds, $L\in\{p\}\cup
\{2m : m>1\}$ — narrowing the possible period structure without first
knowing $Q$ or $L$ exists. Candidate mechanism: track the two covering
agents $\{p,2\}$ jointly — $p$ covers all multiples of $p$ (free, from the
base recurrence), $2$ covers all even integers *from the index where $2$ is
confirmed periodically active* (not yet established for all $n$, only from
$n=2$ against $a_1,a_2$ — extending "$2$ is safe" to hold against the WHOLE
growing prefix, not just $a_1,a_2$, is the open technical step, flagged
honestly by the explorer as not free). This halves the "unaccounted"
$p-2$ in-between candidates (§7.4's diagnosis) to just the *odd*
non-multiples-of-$p$ ones — a genuine narrowing of the open case count, not
a full solve.

**Skeleton for this round's build.**
1. Certify the general $a_2=a_1+p$ lemma (free, no gaps).
2. Prove or refute: "$2$ remains a valid covering agent for every EVEN
   candidate $a_n+j$ ($j$ even, $2\le j\le p-1$) against the *entire*
   prefix $a_1,\dots,a_n$" — i.e., once $a_2$ is even, is $\gcd(a_n+j,a_i)>1$
   automatic for every $i\le n$ whenever $a_n+j$ is even and $a_i$ is even?
   (This needs: are all of $a_2,\dots,a_n$ eventually even, or only some? If
   $a_1$ is odd, $a_1$ itself is odd, so this can only ever cover
   $i\ge2$ — the pair $(1,\cdot)$ still needs $p$, not $2$. State this
   precisely; it is exactly where the "safe against the whole prefix, not
   just $a_1,a_2$" subtlety the explorer flagged lives.)
3. If step 2 succeeds for all EVEN in-between candidates, the only
   remaining unaccounted candidates are the $\lceil(p-2)/2\rceil$ ODD,
   non-multiple-of-$p$ integers strictly between consecutive multiples of
   $p$ — restate the open gap precisely in terms of these only.
4. Attempt the "$2\mid L$ whenever lock fails" conjecture as a standalone
   deliverable even if step 2/3 stall — it is a strictly smaller, checkable
   target than the full Step 2 closure.

**Cases to cover (revisited, see §8 below):** odd seeds split further by $p=\min R(a_1)$; the "lock
succeeds forever" sub-case (majority, ~75% numerically) still needs its own
argument (why does $2\cdot\lceil\rceil$ never get recruited for these?) —
do not assume the covering-agent mechanism only needs to explain the
"failure" cases; a complete Step-2 closure needs both branches.

**Dead ends confirmed again, do not retry:** naive permanent locking
(refuted, $a_1=35$), bounded-lookahead certification (refuted, $a_1=65$), and
any single-congruence classifier for lock success/failure based on $q\bmod
p$, $q\bmod6$, or $q$'s size alone (explorer checked directly this round,
$p=5$: fails at $q=7,13,19$, succeeds at $q=11,17,23,\dots$, no visible
split).

## §8 (this round's build). The general $a_2=a_1+p$ lemma, certified; and the
"two covering agents" mechanism refuted in full

This section carries out exactly the round-6-revision's skeleton step 1
(certify the general $a_2$ lemma) and then attacks step 2 — with the
result that step 2, **as stated**, is impossible, and a corrected
diagnosis is given of what remains for any future attempt.

### 8.1 The general $a_2$ Lemma (certifying the round-6 sketch in full)

**Lemma ($a_2$ formula, fully general).** For every $a_1>1$, writing
$p:=\min R(a_1)$, we have $a_2=a_1+p$.

*Proof.* By definition $a_2$ is the least integer exceeding $a_1$ with
$\gcd(a_2,a_1)>1$ (the defining property at $n=1$ has the single
constraint index $i=1$). Let $1\le t\le p-1$. Suppose toward a
contradiction some prime $q$ divides both $t$ and $a_1$; then $q\in
R(a_1)$, so $q\ge p$ (as $p=\min R(a_1)$) by definition of the minimum,
yet $q\mid t$ with $0<t\le p-1<p\le q$ forces $q\le t<p\le q$, a
contradiction. Hence no prime factor of $a_1$ divides $t$, i.e.
$\gcd(t,a_1)=1$. Since $\gcd(a_1+t,a_1)=\gcd(t,a_1)$ (subtracting the
multiple $a_1$ of itself, a single Euclidean step), $\gcd(a_1+t,a_1)=1$:
$a_1+t$ is not a valid candidate for $a_2$, for every $t=1,\dots,p-1$.

Now consider $t=p$: since $p\in R(a_1)$, $p\mid a_1$, and trivially
$p\mid p$, so $p\mid(a_1+p)$; also $p\mid a_1$, so $p\mid\gcd(a_1+p,a_1)$,
giving $\gcd(a_1+p,a_1)\ge p>1$. So $a_1+p$ **is** a valid candidate.
Since every integer strictly between $a_1$ and $a_1+p$ (namely
$a_1+1,\dots,a_1+p-1$) has just been shown invalid, and $a_1+p$ is valid,
minimality of the sequence's definition gives $a_2=a_1+p$ exactly.
$\blacksquare$

This is fully general — no hypothesis on $\omega(a_1)$ — and strictly
subsumes both §3's base-case computation of $a_2$ (there, $R(a_1)=\{p\}$)
and §4.1's Lemma 4.1 (there, $R(a_1)=\{p,q\}$) as special cases of one
proof.

### 8.2 Corollary: for odd $a_1$, $a_2$ is divisible by $2p$

**Corollary.** If $a_1$ is odd, then $p:=\min R(a_1)$ is odd, and
$a_2=a_1+p$ is divisible by $2p$ (i.e. both $2\mid a_2$ and $p\mid a_2$,
hence $2p\mid a_2$ since $\gcd(2,p)=1$).

*Proof.* $a_1$ odd $\Rightarrow$ every prime factor of $a_1$ is odd (an
even prime factor would force $2\mid a_1$) $\Rightarrow$ $p$, being one of
these prime factors, is odd. By §8.1, $a_2=a_1+p$; since $a_1$ and $p$ are
both odd, their sum is even, so $2\mid a_2$. Also, as shown in the proof
of §8.1, $p\mid a_1$ (by definition $p\in R(a_1)$) and $p\mid p$, so
$p\mid(a_1+p)=a_2$. Since $2$ and $p$ are distinct primes ($p$ odd),
$\gcd(2,p)=1$, so $2\mid a_2$ and $p\mid a_2$ together give $2p\mid a_2$.
$\blacksquare$

This is a genuinely new, fully general fact about *every* odd seed (not
restricted to prime-power or two-prime seeds): the second term of the
sequence is always simultaneously a multiple of the original smallest
prime $p$ *and* of $2$, whenever the seed is odd. It matches, and
explains from first principles, the computational observation recorded in
§7.4/§4.3 that $2$ enters the picture almost immediately for odd seeds
(e.g. $a_1=35\Rightarrow a_2=40=2^3\cdot5$; $a_1=65\Rightarrow
a_2=70=2\cdot5\cdot7$; both divisible by $2p$: $2\cdot5=10\mid40$ and
$10\mid70$, consistent).

### 8.3 The Odd-Anchor Lemma: why "$2$ as a free covering agent" cannot
work against index $1$, for any odd seed — a full refutation of the
round-6 "two covering agents" mechanism as literally stated

The round-6 revision's Step 2 asked, concretely: is $\gcd(a_n+j,a_i)>1$
"automatic" for every $i=1,\dots,n$ whenever $a_n+j$ is even and (for
$i\ge2$) $a_i$ is even, for $j$ even, $2\le j\le p-1$? This section shows
the answer is **no, and can never be yes**, for the single index $i=1$,
whenever $a_1$ is odd — not merely "not yet established," but
impossible, because parity carries no information about divisibility by
an odd number.

**Lemma (Odd-Anchor).** Suppose $a_1$ is odd. Then for every integer
$m>0$, the value of $m\bmod 2$ is logically independent of whether
$\gcd(m,a_1)>1$: knowing $m$ is even never implies $\gcd(m,a_1)>1$, and
knowing $m$ is odd never implies $\gcd(m,a_1)=1$. Equivalently: $2\notin
R(a_1)$, so evenness of a candidate is irrelevant, by itself, to
satisfying the constraint against index $1$.

*Proof.* $a_1$ odd means $2\nmid a_1$, i.e. $2\notin R(a_1)$. By
definition, $\gcd(m,a_1)>1$ holds if and only if $m$ and $a_1$ share some
common prime factor, i.e. some prime of $R(a_1)$ divides $m$. Since every
prime of $R(a_1)$ is odd (as $2\notin R(a_1)$), whether $2\mid m$ has no
bearing on whether some *odd* prime of $R(a_1)$ divides $m$: there exist
even $m$ with $\gcd(m,a_1)=1$ (e.g. $m=2$, since $a_1$ odd and $a_1>1$
means $\gcd(2,a_1)=1$) and even $m$ with $\gcd(m,a_1)>1$ (e.g. $m=2p$,
which is divisible by $p\in R(a_1)$) — so evenness alone determines
neither outcome; the actual value of $\gcd(m,a_1)$ depends entirely on
whether $m$ shares one of $a_1$'s (odd) prime factors, a condition
orthogonal to parity. $\blacksquare$

**Consequence for the round-6 mechanism.** For any candidate $m=a_n+j$
under consideration in the "two covering agents" plan, validity requires
$\gcd(m,a_1)>1$ **in particular** (taking $i=1$ in the defining property,
which — by the certified `pairwise-non-coprimality.md` — is *always* one
of the $n$ simultaneous constraints, for every $n\ge1$). By the Odd-Anchor
Lemma, this constraint can be satisfied **only** by $m$ sharing an actual
odd prime factor with $a_1$ (necessarily a prime of $R(a_1)$, by the
already-certified `prime-factors-a1-cover-forever.md`, which shows every
term of the sequence — not just candidates being tested, but every actual
$a_n$ — shares a prime of $R(a_1)$ with $a_1$). No amount of information
about $m$'s parity, or about the parity of $a_2,\dots,a_n$, contributes
anything toward this. Hence:

**The "two covering agents" mechanism, exactly as proposed in the round-6
revision, cannot ever discharge the index-$1$ constraint via the prime
$2$, for any odd seed $a_1$, at any step $n$, for any candidate.** This
upgrades the round-6 revision's own honest flag ("the pair $(1,\cdot)$
still needs $p$, not $2$ — state this precisely") from a flagged risk
into a fully proved impossibility. The mechanism can, at best, ever hope
to discharge the constraints against indices $i\ge2$ automatically (via
evenness of $a_i$, $i\ge2$, if those terms are in fact all even) — the
index-$1$ constraint must, in every single case, be separately certified
by an actual shared *odd* prime factor of $a_1$, which is precisely the
"escape race" difficulty already identified and left open in §4–§5 and
§7.4. So the "halving" claimed informally in the round-6 sketch ("halves
the unaccounted $p-2$ in-between candidates to just the odd ones") is not
available: **every** in-between candidate $a_n+j$ ($1\le j\le p-1$,
$j\ne$ the one excluded by the Minimum Gap Lemma when $j=1$), even
"nice" even ones, still needs the same real work — an actual shared odd
prime with $a_1$ — to be ruled in or out; parity contributes nothing
toward the index-$1$ half of the problem.

### 8.4 A further honest negative finding: even the weaker fallback
("once even, stays even for $n\ge2$") is also false in general

One might hope to salvage a weaker version of the mechanism: even if $2$
cannot help with index $1$, perhaps for indices $i\ge2$ it is at least
true that, once $a_2$ is even (§8.2), *every* subsequent term $a_n$
($n\ge2$) stays even, so that the constraints against indices $2,\dots,
n-1$ (though never against index $1$) really are free from some point on.
This round checked this directly and it is **false in general**.

**Counterexample.** For $a_1=45=3^2\cdot5$ ($p=3$): direct computation
from the definition gives
$$a_1,\dots,a_9 = 45,\,48,\,50,\,54,\,60,\,66,\,70,\,72,\,75,$$
so $a_2,\dots,a_8$ are all even (seven consecutive even terms), but
$a_9=75$ is **odd**, breaking the run.

*Verification (computed directly from the definitions, exact integer
arithmetic, not floating simulation).* We verify $a_9=75$ by checking
every candidate in $\{73,74,75\}$ against the already-established prefix
$a_1,\dots,a_8=45,48,50,54,60,66,70,72$ (this prefix itself follows by the
same direct gcd-checking at each of the 7 preceding steps; it is not
re-derived here since it is a routine — if lengthy — repetition of the
same check, and matches the value independently produced by the greedy
definition):
- $73$: prime, and $73\nmid45$, so $\gcd(73,45)=1$: invalid already
  against index $1$.
- $74=2\cdot37$: $\gcd(74,45)=1$ since $45=3^2\cdot5$ shares neither $2$
  nor $37$: invalid against index $1$.
- $75=3\cdot5^2$: $\gcd(75,45)=15>1$; $\gcd(75,48)=3>1$ ($48=2^4\cdot3$);
  $\gcd(75,50)=25>1$; $\gcd(75,54)=3>1$ ($54=2\cdot3^3$); $\gcd(75,60)=15
  >1$; $\gcd(75,66)=3>1$ ($66=2\cdot3\cdot11$); $\gcd(75,70)=5>1$
  ($70=2\cdot5\cdot7$); $\gcd(75,72)=3>1$ ($72=2^3\cdot3^2$). All eight
  constraints hold, so $75$ is valid, and since $73,74$ were just shown
  invalid, $a_9=75$ by minimality.

Since $75$ is odd, this refutes "even from index $2$ on, forever" as a
general fact — it can hold for a long finite run (here $7$ terms) and
then fail, exactly the same qualitative phenomenon (a state that *looks*
locked for a while and then isn't) already established for the "$p$ locks
forever" hope in §4.3's Bounded-Lookahead-Insufficiency finding. So this
round's attempted fallback fails for essentially the same underlying
reason as the previously-refuted fallbacks: no bounded amount of
verified recent history (here, "the last $7$ terms were even") certifies
a global pattern ("even forever from here").

### 8.5 Where this leaves the odd-seed extension

Combining §8.1–§8.4: the general $a_2=a_1+p$ lemma and its corollary
$2p\mid a_2$ are new, true, and fully proved facts about every odd seed,
usable as a clean starting fact for any future attempt. But the concrete
mechanism proposed to exploit them this round (the "two covering agents"
plan) is now **provably** incapable of closing Step 2, for two
independent reasons proved in full above: (a) parity structurally cannot
help with the index-$1$ constraint at all (§8.3, an unconditional
impossibility, not merely an unproved step), and (b) even restricted to
indices $\ge2$, "even" is not a permanent property of the tail in general
(§8.4, a concrete refutation). Both of these are genuine, provable
narrowings of the search space for future rounds: any working argument
must (i) handle the index-$1$ constraint via an actual shared odd prime
of $R(a_1)$ (not parity) at every step, and (ii) not assume evenness of
$a_i$, $i\ge2$, persists without a separate proof, since it can and does
lapse. The core difficulty diagnosed in §4.3/§5/§7.4 — that the state
governing validity grows with $n$ and is not visible from a bounded
window or a fixed statistic (parity included) — is thus reconfirmed, this
time from an entirely different, independently-checked angle (the
specific "$p$ and $2$ as two covering agents" idea proposed this round),
rather than merely re-asserted. The general inductive step for odd seeds
remains open.

## Promotable lemmas
- **Escape Window Lemma (new this round, §9.1).** For $a_1=3q$ ($q$ prime,
  $q\ne2,3$) with the sequence locked at $3$ through index $n$ (i.e.
  $a_i=3(q+i-1)$ for $i=1,\dots,n$), the candidate $m=a_n+2$ satisfies
  $\gcd(m,a_i)=\gcd(3(n-i)+2,\,q+i-1)$ for every $i=1,\dots,n$, so the lock
  breaks at step $n$ iff $\gcd(3s+2,q+n-1-s)>1$ for every $s=0,\dots,n-1$.
  Proved directly from the definitions (§9.1); cross-checked against exact
  simulation with zero mismatches. Reusable as the exact closed-form tool
  for analyzing the $p=3$ two-prime-seed lock at any step $n$, replacing
  case-by-case computation.
- **Parity Corollary (new this round, §9.2).** For $a_1=3q$ as above, the
  lock at $3$ can only break at an even step $n$; every odd $n$ is
  unconditionally safe. Proved in three lines from the Escape Window
  Lemma's $s=0$ case. Reusable as a free 50%-reduction of the cases any
  future attempt on this seed family needs to check.
- **$n=2$ Exact Characterization (new this round, §9.4).** For $a_1=3q$
  ($q$ prime, $q\ne2,3$), the lock breaks at step $2$ if and only if
  $q=5$. Fully proved (not simulated) from the Escape Window Lemma.
  Reusable as the precise structural reason $q=5$ (equivalently $a_1=15$)
  is the unique exception to $p=3$-locking among two-prime seeds, and as a
  worked base case for any future induction attempting to close the
  general $q\ge7$ case.
- **General $a_2$ Lemma (new this round, §8.1).** For every $a_1>1$,
  writing $p:=\min R(a_1)$, $a_2=a_1+p$. Fully general (no hypothesis on
  $\omega(a_1)$), proved directly from the definitions in a few lines,
  subsuming §3's and §4.1's special cases. Reusable as the natural
  starting fact for computing/bounding the second term of *any* instance
  of the sequence.
- **Odd-seed $2p\mid a_2$ Corollary (new this round, §8.2).** If $a_1$ is
  odd, then $2p\mid a_2$ where $p:=\min R(a_1)$. Proved in three lines
  from the General $a_2$ Lemma plus parity. Reusable as a clean,
  general starting fact about every odd-seed instance.
- **Odd-Anchor Lemma (new this round, §8.3).** If $a_1$ is odd, then for
  every integer $m$, $2\notin R(a_1)$, so the parity of $m$ is logically
  irrelevant to whether $\gcd(m,a_1)>1$ (both outcomes occur for both
  parities). Consequence: no argument based on parity/evenness can ever
  discharge the "index-$1$" constraint $\gcd(a_n+j,a_1)>1$ for an odd
  seed; only an actual shared odd prime factor of $a_1$ can. Proved in
  full from the definitions. Reusable as a standing, general impossibility
  result against any future "parity as a free covering agent" proposal for
  odd seeds, and as a precise explanation of why the even-seed technique
  (§7, `even-seed-universal-lock-theorem.md`) cannot transplant to odd
  seeds even partially via parity alone.
- **Prime-power base case theorem.** If $a_1=p^k$ (in particular if $a_1$
  is even, taking $p=2$), then $T=1$, $L=p=\min R(a_1)$, and $a_n=a_1+
  (n-1)p$ for every $n\ge1$. Proved in full above (§3), fully elementary,
  self-contained (uses only that $a_1$'s prime support is a singleton).
  Reusable as a free, closed sub-case disposing of all prime-power seeds at
  once, and as a base case for any future inductive framing of the general
  problem.
- **Third-Term Dichotomy Lemma (new this round).** For $a_1=pq$ with $p<q$
  primes: $a_2=a_1+p$, and writing $k=q+1=p^e k'$ ($p\nmid k'$), $a_3 =
  \min(a_2+p,\ m^\ast)$ where $m^\ast$ is the least multiple of $q$
  exceeding $a_2$ with $\gcd(m^\ast,k')>1$ (or $+\infty$ if $k'=1$). Proved
  in full above (§4.2) directly from the definition of the sequence, with
  no simulation dependency; cross-checked against exact simulation on $66$
  squarefree pairs $p<q\le37$ with zero mismatches. Reusable as: (a) a
  clean worked closed-form example of the "escape race" mechanism for any
  future approach that wants to formalize it further; (b) a concrete
  starting point for extending to a general $a_n$ recursion (open, see
  §5); (c) the exact source of both the $a_1=35$ and $a_1=65$ negative
  instances, so future rounds can re-derive further instances on demand
  instead of re-simulating from scratch.
- **Bounded-lookahead insufficiency (negative, new this round).** For
  $a_1=65=5\cdot13$: the Third-Term Dichotomy Lemma correctly predicts $p=5$
  wins the race at step $3$ ($a_3=75$), yet direct computation shows the
  lock already breaks at step $4$ ($a_4=78\ne a_3+5=80$). Hence no
  induction scheme that certifies "$p$ locked forever" via a *fixed,
  bounded* number of look-ahead race comparisons (checking only $a_1,\dots,
  a_j$ for $j$ bounded independent of how far the sequence has run) can be
  correct in general. Proved by direct computation from the sequence's own
  definition (not simulation-only: the $a_3$ value is independently
  confirmed by the Third-Term Dichotomy Lemma, and $a_4$ is computed
  directly by checking the finitely many candidates $76,77,78$ against
  $\gcd(\cdot,65)>1,\gcd(\cdot,70)>1,\gcd(\cdot,75)>1$: $76=4\cdot19$,
  $\gcd(76,65)=1$, invalid; $77=7\cdot11$, $\gcd(77,65)=1$, invalid;
  $78=2\cdot3\cdot13$, $\gcd(78,65)=13>1$, $\gcd(78,70)=2>1$,
  $\gcd(78,75)=3>1$: valid, so $a_4=78$ exactly). Reusable as a standing
  counterexample against any future "check $k$ steps ahead" proposal for
  this problem, for any fixed $k\ge1$ at least up to $k=2$ (an explicit,
  hand-verifiable instance).
- **Minimum Gap Lemma (new this round, §7.1).** For every $n\ge1$,
  $a_{n+1}\ge a_n+2$ — i.e. the greedy sequence never has a gap of exactly
  $1$. Proved unconditionally for every $a_1$ in three lines, from
  $\gcd(a_n+1,a_n)=1$ (consecutive integers) and the defining property
  applied with $i=n$. Sharpens the certified `bounded-gap-via-rad-a1.md`
  bound to the exact interval $a_{n+1}-a_n\in[2,R]$ ($R=\mathrm{rad}(a_1)$)
  for every $n\ge1$. Reusable by any approach in the population as a free
  strengthening of the existing gap bound, with no hypothesis needed.
- **Even-Seed Universal Lock Theorem (new this round, §7.2–7.3).** If
  $a_1$ is even, then $a_n=a_1+2(n-1)$ for every $n\ge1$: the *entire*
  problem statement holds with $T=1,L=2$, exactly, from $n=1$, no
  transient. Proved in full above by induction, using only the Minimum
  Gap Lemma and the fact that any two even numbers have $\gcd\ge2$.
  Completely and rigorously resolves the full IMO claim for the entire
  infinite sub-family of even seeds $a_1$ (strictly generalizing the
  $a_1=2^k$ special case of the prime-power base case theorem to *all*
  even $a_1$). Reusable as: (a) a free, complete disposal of every even-seed
  instance for any future approach to the general problem; (b) a base case
  / anchor instance for any future induction-on-$\omega(a_1)$ or
  induction-on-$\min R(a_1)$ argument, since it settles $p=2$ completely
  and unconditionally; (c) the source of a precise diagnosis (§7.4) of
  exactly which structural feature of $p=2$ ($p-1=1$ "in-between"
  candidate, vs. $p-2\ge1$ unaccounted-for candidates for every odd prime
  $p$) makes it uniquely tractable by this technique among all primes.

## §9 (this round's build). The $p=3$ Near-Total Lock Theorem, corrected in
scope to two-prime seeds, with a new closed-form mechanism

The "Round 7 revision" section immediately below this one (from the
outliner) proposed a target for **every** $a_1$ with $\min R(a_1)=3$ and
$5\nmid a_1$. The outline-reviewer found, and this round independently
re-confirms (§9.0), that this general target is **false**: it must be
restricted to two-prime seeds. This section carries out that correction
and proves everything that can be proved this round about the corrected,
narrower target.

### 9.0 Independent re-verification of the $a_1=429$ counterexample

Using exact Python integer arithmetic (`math.gcd`, no floating point),
computing the sequence directly from the greedy definition (at each step,
scan candidates $a_n+1,a_n+2,\dots$ and accept the first one with
$\gcd(\cdot,a_i)>1$ for every earlier index $i$):
$$a_1,\dots,a_{20}\ (a_1=429=3\cdot11\cdot13):\quad
429,\,432,\,435,\,438,\,440,\,444,\,450,\,456,\,462,\,465,\dots$$
with successive gaps $3,3,3,2,4,6,6,6,3,3,\dots$. So the sequence is
locked at $3$ (gap $3$) through $a_4=438$, but $a_5=440\ne a_4+3=441$: the
lock breaks at $n=4$. Here $5\nmid429$ ($429=3\cdot11\cdot13$), so this is
exactly the outline-reviewer's counterexample to the general (three-prime)
version of the theorem, independently reconfirmed by direct computation
here rather than taken on faith. A hand-check of the mechanism: $440=
2^3\cdot5\cdot11$, and $\gcd(440,429)=11>1$ — so the index-$1$ constraint
is discharged via the prime $11$ (a prime of $R(a_1)$ *other than* $3$),
not via $3$ itself and not via any parity argument. This is the seed of
the diagnosis in §9.6 below.

**Consequence.** The "New Target" as stated in the "Round 7 revision"
section below (for *every* $a_1$ with $\min R(a_1)=3$, $5\nmid a_1$) is
false. From here on, this section restricts attention to the two-prime
case only:

**Corrected setting for the rest of §9.** $a_1=3q$ where $q$ is a prime,
$q\notin\{2,3,5\}$ (excluding $q=2$ since $a_1=3\cdot2=6$ would be even,
already fully resolved by the Even-Seed Universal Lock Theorem, §7.2, and
would in any case have $\min R(a_1)=2\ne3$; excluding $q=3$ as it collapses
to the prime-power base case §3; excluding $q=5$, treated separately in
§9.4 below).

### 9.1 The Escape Window Lemma

Throughout this subsection, fix $a_1=3q$ ($q$ an odd prime, $q\ne3,5$),
and suppose (inductive hypothesis, to be discharged by strong induction on
$n$ exactly as in the even-seed theorem's proof shape) that the sequence
is **locked at $3$ through index $n$**: $a_i=3(q+i-1)$ for every
$i=1,\dots,n$. (This holds vacuously/trivially for $n=1$: $a_1=3(q+1-1)=
3q$.)

By the certified General $a_2$ Lemma (§8.1) with $p=3=\min R(a_1)$ (since
$q>3$), $a_2=a_1+3$, consistent with $i=2$ of the formula; and by the
Minimum Gap Lemma (§7.1), $a_n+1$ is never a valid candidate for
$a_{n+1}$. Since $3\mid a_n$ (by the locked hypothesis), $a_n+2\equiv2
\pmod3$, so $3\nmid(a_n+2)$; and $a_n+3=3(q+n)$ is always valid against
every $a_i$ ($i\le n$), since $3\mid a_i$ and $3\mid(a_n+3)$ give
$\gcd(a_n+3,a_i)\ge3>1$ simultaneously for all $i\le n$. Hence:
$$a_{n+1}=a_n+3 \quad\Longleftrightarrow\quad a_n+2 \text{ is \emph{not}
a valid candidate for } a_{n+1}.$$
So the lock survives step $n$ if and only if $m:=a_n+2$ fails at least
one of the $n$ simultaneous constraints $\gcd(m,a_i)>1$, $i=1,\dots,n$.

**Lemma (Escape Window).** With $a_1,\dots,a_n$ as above and
$m=a_n+2=3(q+n-1)+2$, for every $i=1,\dots,n$:
$$\gcd(m,a_i) = \gcd\bigl(3(n-i)+2,\ q+i-1\bigr).$$
Consequently, $m$ is a valid candidate for $a_{n+1}$ (i.e. the lock breaks
at step $n$) if and only if, writing $s:=n-i$ so that $s$ ranges over
$0,1,\dots,n-1$ as $i$ ranges over $n,n-1,\dots,1$:
$$\gcd(3s+2,\ q+n-1-s) > 1 \quad\text{for every } s=0,1,\dots,n-1. \tag{$\dagger$}$$

*Proof.* Fix $i\in\{1,\dots,n\}$. Since $a_i=3(q+i-1)$, and
$m=3(q+n-1)+2\equiv2\pmod3$ (as just shown), $\gcd(m,3)=1$, so $\gcd(m,a_i)
=\gcd(m,3(q+i-1))=\gcd(m,q+i-1)$ (a common factor of $m$ and $3(q+i-1)$
cannot involve the factor $3$, since $3\nmid m$, so it is exactly a common
factor of $m$ and the cofactor $q+i-1$). Next,
$$m - 3(q+i-1) = \bigl[3(q+n-1)+2\bigr] - 3(q+i-1) = 3(n-i)+2,$$
so $m\equiv 3(n-i)+2 \pmod{(q+i-1)}$, giving $\gcd(m,q+i-1)=\gcd\bigl(3(n-i)+2,
\,q+i-1\bigr)$ (subtracting an exact multiple of the modulus $q+i-1$ from
$m$ does not change the gcd with $q+i-1$ — a single Euclidean-algorithm
step). This proves the displayed identity. Substituting $s=n-i$ turns
"$i$ ranges over $1,\dots,n$" into "$s$ ranges over $0,\dots,n-1$" and
$q+i-1=q+(n-s)-1=q+n-1-s$, giving exactly $(\dagger)$; validity of $m$
means all $n$ constraints hold simultaneously, i.e. $\gcd(3s+2,q+n-1-s)>1$
for every $s=0,\dots,n-1$. $\blacksquare$

*(Numerical cross-check, not a substitute for the proof above: computed
both sides of the identity and both formulations of $(\dagger)$ directly
from the sequence's own definition for $q\in\{5,7,11,13,17,19,23\}$ and
$n=2,\dots,29$ — and, for $q$ prime up to $97$ via `sympy.primerange`,
$n$ up to $3000$ — with the "does $m$ satisfy $(\dagger)$" indicator
matching direct computation of whether $a_n+2$ is actually accepted by the
greedy rule in every tested instance, zero mismatches.)*

### 9.2 Parity Corollary: the lock can only break at an even step

**Corollary.** If the lock at $3$ breaks at step $n$ (i.e. $(\dagger)$
holds for that $n$), then $n$ is even.

*Proof.* Take $s=0$ in $(\dagger)$: $\gcd(2,q+n-1)>1$, i.e. $q+n-1$ is
even. Since $q$ is odd (by hypothesis, $q\ne2$), $q+n-1$ has the same
parity as $n$ (as $q-1$ is even, $q+n-1=(q-1)+n$). So $q+n-1$ even $\iff$
$n$ even. $\blacksquare$

Hence **every odd $n$ is unconditionally safe**: for odd $n$, $a_{n+1}=
a_n+3$ automatically (no further check needed), regardless of $q$.

### 9.3 Even-$s$ Automatic-Satisfaction Corollary

**Corollary.** Suppose $n$ is even (the only case that can matter, by
§9.2). Then for every even $s\in\{0,2,4,\dots\}$ with $0\le s\le n-1$, the
condition $\gcd(3s+2,q+n-1-s)>1$ of $(\dagger)$ holds automatically
(independent of the specific value of $q$).

*Proof.* If $s$ is even, $3s+2$ is even. Also, $q+n-1-s$: $q$ is odd, $n$
is even, $s$ is even, so $q+n-1-s \equiv 1+0-1-0 \equiv 0 \pmod 2$ (using
$q\equiv1,n\equiv0,s\equiv0\pmod2$, and the constant $-1$), i.e.
$q+n-1-s$ is even. Two even numbers have $\gcd\ge2>1$. $\blacksquare$

So, once $n$ is even, $(\dagger)$ reduces to only the **odd**-indexed
conditions $s=1,3,5,\dots$ (up to $n-1$, which is odd since $n$ is even):
$$\gcd(3s+2,\ q+n-1-s)>1 \quad\text{for every odd } s=1,3,\dots,n-1.$$
Writing $s=2r+1$ ($r=0,1,\dots,(n-2)/2$), $3s+2=6r+5$, so these are
divisibility conditions by the numbers $5,11,17,23,\dots$ (the arithmetic
progression $6r+5$), matching exactly the "extra" primes seen entering
in the $a_1=35$ and $a_1=65$ instances elsewhere in this file (§4.3):
$5$ is precisely the $r=0$ case.

### 9.4 Exact characterization at the first possible break, $n=2$: $q=5$ is the unique exception

**Theorem.** For $a_1=3q$ ($q$ prime, $q\ne2,3$), the $3$-lock breaks at
step $n=2$ (i.e. $a_3\ne a_2+3$) if and only if $q=5$.

*Proof.* By §9.2, $n=2$ is even, so it is not excluded by parity. By
$(\dagger)$ with $n=2$, $s$ ranges over $\{0,1\}$:
- $s=0$: $\gcd(2,q+1)>1$. Since $q$ is odd, $q+1$ is even, so this holds
  for every odd prime $q$ — automatically true (consistent with §9.3, as
  $s=0$ is even).
- $s=1$: $\gcd(5,\,q+2-1-1)=\gcd(5,q)>1$. Since $q$ is prime, this holds
  iff $q=5$ (the only way a prime $q$ shares a factor with $5$ is $q=5$
  itself).

Both conditions must hold for the lock to break at $n=2$; $s=0$ always
holds, so the lock breaks at $n=2$ if and only if $s=1$'s condition holds,
i.e. iff $q=5$. $\blacksquare$

This is a full, unconditional proof (not a numerical observation) that $5$
is the *unique* prime among all $q\ne2,3$ for which the two-prime lock can
possibly fail at the earliest opportunity — and it reproduces, from first
principles, the known instance $a_1=15$ ($15,18,20,\dots$: lock breaks
exactly at $n=2$, since $a_2=18$, $a_2+2=20$ is accepted, matching
$q=5\Rightarrow$ break at $n=2$ predicted above).

*(Sanity check against direct computation, not a substitute for the proof:
checked $q\in\{5,7,11,13,17,19,23,29\}$ directly against $(\dagger)$ at
$n=2$ — true only for $q=5$, matching the theorem exactly.)*

**Corollary.** For every prime $q\ne2,3,5$: the lock survives step $2$
($a_3=a_2+3$ is forced).

### 9.5 What remains open: $n\ge4$

For $q\ne2,3,5$, the lock survives $n=2$ (§9.4) and every odd $n$ is
automatically safe (§9.2), so the next possible failure is $n=4$. At
$n=4$, $(\dagger)$'s odd-$s$ conditions are $s=1$ ($\gcd(5,q+2)>1$, i.e.
$5\mid(q+2)$) and $s=3$ ($\gcd(11,q)>1$, i.e. $q=11$, since $11$ is
prime). **Both must hold simultaneously.** If $q=11$: $q+2=13$, and
$5\nmid13$. So the $s=1$ condition fails when $q=11$ — hence **the lock
cannot break at $n=4$ for any prime $q$** (the only candidate consistent
with $s=3$, namely $q=11$, is excluded by $s=1$). This is a second fully
proved instance (beyond $n=2$), extending §9.4's method one step further
and fully general in $q$.

Beyond $n=4$, the pattern does **not** collapse to a single forced value
of $q$ in general: the $s=n-1$ (topmost) condition is $\gcd(3n-1,q)>1$,
which (as $q$ is prime) means $q\mid(3n-1)$ — a condition satisfied by a
full residue class of $n$ modulo $q$ (infinitely many $n$), not a single
$n$, once $3n-1$ is allowed to be a composite multiple of $q$ rather than
forced to equal $q$ exactly (this refines an earlier mis-step in this
approach's own working notes, corrected here: $\gcd(3n-1,q)>1$ with $q$
prime means $q\mid(3n-1)$, not $3n-1=q$; the two coincide only when
$3n-1$ happens itself to be prime, which is what made $n=4$ ($3n-1=11$,
prime) and, by coincidence, $n=2$ ($3\cdot2-1=5$, also prime) special
cases where the topmost condition alone pins down a *unique* $q$). For
general even $n$, the full system $(\dagger)$'s odd-$s$ conditions
$\gcd(6r+5,\,q+n-2-2r)>1$ for $r=0,\dots,(n-2)/2$ form a genuine
simultaneous-congruence system relating $n$ and $q$, whose solvability (or
lack thereof) for a *fixed* $q\ge7$ prime, as $n$ ranges over all even
integers $\ge6$, is **not resolved by this round's work** — this is
exactly the same qualitative difficulty already diagnosed in §4.3/§5/§7.4
(the state governing validity grows with $n$, and here it is now stated in
the sharpest form yet reached by this approach: an explicit, finite,
purely arithmetic system $(\dagger)$, rather than an abstract "escape
race"). Numerically (Python, exact integer arithmetic, `sympy.primerange`
for primes), no break was found for any prime $q\in\{7,11,\dots,97\}$
checking all even $n$ up to $3000$ — strong evidence for, but not a proof
of, "the two-prime lock at $3$ never breaks for $q\ge7$."

**Open gap, precisely restated:** prove or refute, for every prime $q\ge7$:
there is no even $n\ge6$ for which $\gcd(6r+5,q+n-2-2r)>1$ holds
simultaneously for every $r=0,\dots,(n-2)/2$. This is now a fully explicit
number-theoretic statement (not merely "the state grows with $n$"), a
concrete target for a future round.

### 9.6 The exceptional family $5\mid a_1$: what is known, and what is not

For $q=5$ (so $a_1=15$), the lock breaks already at $n=2$ (§9.4), and
direct computation gives $a_1,\dots=15,18,20,24,30,36,40,42,45,48,50,54,
60,66,70,\dots$ — this instance was already independently verified exact
by the round-3 proof-reviewer (cited in the "Round 7 revision" section
below) and is reconfirmed here by the same Python exact-integer
computation used throughout this section. This round additionally
computed $a_1=45=3^2\cdot5$ and $a_1=75=3\cdot5^2$ directly:
$$45,48,50,54,60,66,70,72,75,78,80,84,90,96,100,\dots\qquad
75,78,80,84,90,96,100,102,105,108,110,114,120,126,130,\dots$$
Both again fail to lock at $L=3$ and exhibit the same qualitative
non-trivial recruitment pattern (primes $2$ and eventually others enter)
as $a_1=15$. **This round does not go beyond confirming these three
instances**: no general characterization of the $5\mid a_1$ family's
eventual period is established here (this matches the honest gap already
flagged by the outline for step 4, and this round's additional data point
$a_1=75$ is new but does not by itself supply the missing general
argument). This sub-family remains open for a future round.

### 9.7 Honest diagnosis: why the two-prime mechanism does not extend to $\ge3$-prime seeds (the $a_1=429$ case)

The proof of the Escape Window Lemma (§9.1) uses, at the single step
"$\gcd(m,a_i)=\gcd(m,3(q+i-1))=\gcd(m,q+i-1)$", the fact that $R(a_1)=
\{3,q\}$ has **exactly one** prime besides $3$ — this is what lets the
index-$i$ constraint collapse to a single divisibility test against the
single cofactor $q+i-1$. For a three-prime seed $a_1=3q_1q_2$ (e.g.
$429=3\cdot11\cdot13$), the analogous index-$1$ constraint is
$$\gcd(m,a_1)>1 \iff 3\mid m \text{ or } q_1\mid m \text{ or } q_2\mid m,$$
a **disjunction over two extra primes** instead of a single fixed $q$.
Concretely, for $429$: at $n=4$ (locked prefix $429,432,435,438$), the
candidate $m=a_4+2=440$ fails $3\mid m$ (as required for it to be a
genuine "escape" candidate, exactly as in the two-prime analysis) but
satisfies the index-$1$ constraint via $q_1=11$ ($11\mid440$) — an escape
route with **no two-prime analogue**, since a two-prime seed only ever has
the single fixed prime $q$ available to satisfy that constraint once
$3\nmid m$. This does not, by itself, complete a proof that $\ge3$-prime
seeds behave differently in general — it identifies precisely *which*
step of the two-prime argument (the single-cofactor collapse) fails to
generalize, and exhibits the exact instance where the extra freedom (a
disjunction instead of a single congruence class) is used. A general
theory for $\ge3$-prime seeds with $3\in R(a_1)$, $5\notin R(a_1)$ is not
attempted here (open, flagged for a future round, per the outline
reviewer's requirement to treat this as an explicit new open sub-case
rather than a silent extension).

### 9.8 Summary of §9's status

- **Proved in full, this round:** the Escape Window Lemma (§9.1); the
  Parity Corollary (§9.2); the Even-$s$ auto-satisfaction fact (§9.3); the
  exact $n=2$ characterization "$q=5$ is the unique exception" (§9.4); the
  $n=4$ non-breaking fact for every prime $q$ (§9.5); the identification of
  exactly which step of the argument fails for $\ge3$-prime seeds, with
  $a_1=429$ as a fully worked witness (§9.7).
- **Open, honestly unresolved:** whether the lock at $3$ ever breaks for
  some even $n\ge6$ when $q\ge7$ is prime (§9.5, precisely restated as an
  explicit simultaneous-congruence system); the general structure of the
  $5\mid a_1$ exceptional family beyond three hand-verified instances
  ($a_1=15,45,75$, §9.6); any general theory for $\ge3$-prime seeds with
  $\min R(a_1)=3$, $5\notin R(a_1)$ (§9.7, only the $a_1=429$ failure
  instance is understood, not a general criterion).
- **Corrected scope, as mandated by the outline review:** the theorem
  target of this approach is now stated and partially proved *only* for
  two-prime seeds $a_1=3q$ (with the $q=5$ sub-case handled separately,
  §9.6), not for all $a_1$ with $\min R(a_1)=3,\ 5\nmid a_1$ — that
  broader statement is false, witnessed by $a_1=429$ (§9.0).

## Round 7 outline's original target (superseded by §9's scope correction) — new non-parity target: the $p=3$ Near-Total Lock Theorem

**Note: the general statement below (for every $a_1$ with $\min R(a_1)=3$,
$5\nmid a_1$) is FALSE, refuted by $a_1=429=3\cdot11\cdot13$ — see §9.0
above for the independently-reconfirmed counterexample and §9 generally
for the corrected, two-prime-only scope this round actually worked on.
Retained below verbatim as the historical record of the outline this round
started from.**

All parity-based mechanisms for odd seeds are exhausted (Odd-Anchor Lemma +
the $a_1=45$ weak-fallback counterexample, both certified). Round 7's
odd-seed-recruitment explorer found a sharp, non-parity empirical fact:
for $p:=\min R(a_1)=3$, the sequence locks forever at $p=3$ ($T=1,L=3$,
$a_n=a_1+3(n-1)$ for $n\ge2$) in **106 of 107** tested seeds with
$5\le q<600$ prime and $R(a_1)=\{3,q\}$ (or more generally $5\nmid a_1$);
the **sole** exception found is $a_1=15$ ($q=5$). This is a genuinely new,
non-parity, structurally different target from the fully-exhausted
parity route — it attacks the *next* smallest prime directly, mirroring
the even-seed proof shape ($p=2$: only $p-1=1$ in-between candidate,
always excluded free) but for $p=3$ (only $p-2=1$ non-trivial in-between
candidate, $a_n+2$, since $a_n+1$ is free by the Minimum Gap Lemma).

**New Target (replaces "general odd extension" as the concrete near-term
goal for this approach):** For every $a_1$ with $\min R(a_1)=3$ and
$5\nmid a_1$: $a_n = a_1+3(n-1)$ for all $n\ge2$ (i.e. permanent lock at
$L=3,T=1$ from the second term on, with the only possible transient being
the single step $a_1\to a_2=a_1+3$, already given by the certified
General-$a_2$-Formula). Seeds with $5\mid a_1$ (starting with $a_1=15$)
are treated as a separate, explicitly flagged exceptional sub-family.

**Skeleton:**
1. $a_2 = a_1+3$ — by the certified `general-a2-formula.md` ($p=3$).
2. **Key Necessity Lemma (new, to prove):** Suppose $3\mid a_i$ for every
   $i=1,\dots,n$ (i.e. the sequence has locked at $3$ through index $n$).
   Then $a_{n+1}\ne a_n+3$ (the lock *breaks* at step $n$) only if
   $\gcd(a_n+2,\,a_1)>1$. *Mechanism:* $a_n+2\equiv 2\pmod 3$ (since
   $3\mid a_n$), so $3\nmid(a_n+2)$; by the Minimum Gap Lemma, $a_n+1$ is
   never legal; so the only candidate strictly between $a_n+1$ and $a_n+3$
   is $a_n+2$, and for it to be accepted it must satisfy
   $\gcd(a_n+2,a_i)>1$ for **every** $i=1,\dots,n$ simultaneously,
   including $i=1$ in particular. Since $3\nmid(a_n+2)$, the shared factor
   with $a_1$ (if any) must come from a *different* prime of $R(a_1)$ —
   i.e. $R(a_1)$ must have a prime beyond $3$ for the lock ever to be at
   risk. This immediately reproves the prime-power case $a_1=3^k$ as a
   trivial corollary (no other prime exists in $R(a_1)$, so the lock never
   breaks) — subsumes that special case cleanly.
3. **Key Sufficiency-side gap (open, the hard step):** for $a_1=3q$ (or
   more generally $R(a_1)=\{3\}\cup S$ with $5\notin S$), show the
   necessary condition of step 2 is never actually realized at any index
   $n$ — i.e., there is no $n$ for which $a_n+2$ is simultaneously
   divisible by some $q\in S$ **and** legal against every intermediate
   term $a_2,\dots,a_{n-1}$ (not just $a_1$). Candidate mechanism (adapt
   the certified `third-term-dichotomy-lemma.md`'s escape-race
   machinery, generalized past $n=3$ to all $n$): the locked terms
   $a_2,\dots,a_n$ form the fixed arithmetic-style residue sequence
   $a_1+3,a_1+6,\dots$ (mod any fixed $q\ge7$); since $\gcd(3,q)=1$, the
   residues of $a_n+2 \pmod q$ cycle through all residue classes with
   period $q$, so a "$q\mid a_n+2$" event occurs roughly every $q$ steps —
   but each such event must *additionally* survive gcd-checks against all
   $n-1$ prior *locked* terms, and the claim to prove is that this
   compound survival probability/structure is impossible for every prime
   $q\ge7$ but *is* achievable for $q=5$ specifically. This is exactly
   the open gap; a full proof needs either (a) an explicit residue-class
   argument showing $q\ge7$ candidates always collide with some
   intermediate locked term (the natural conjecture, matching the
   numerics), or (b) a genuinely finer invariant distinguishing $5$ from
   all $q\ge7$ (candidate: $5$ is the unique prime with $5<3\cdot2=6$,
   i.e. the unique prime $q$ with $q<2p$ for $p=3$ other than $p$ itself —
   worth testing as the precise dividing line, since it would explain why
   this mechanism does NOT recur for larger $p$ in the same simple form,
   consistent with the plateau-break explorer's $p=11$ finding that no
   simple proximity threshold survives at $p=11$ — that data point is
   about a *different* prime $p$ and does not directly refute a
   $p=3$-specific $q<2p$ threshold, but the builder must explicitly check
   it against the $p=3$ dataset, not assume it transfers).
4. **Exceptional family ($5\mid a_1$):** at minimum, fully hand-verify and
   characterize $a_1=15$ itself (already known: $a_1,\dots$ eventually
   locks at $L=3$ after recruiting $5$ — cf. round-3's `active-set-
   stabilization` note that $a_1=15$'s sequence is $15,18,20,24,\dots$,
   independently confirmed exact by the round-3 proof-reviewer). State
   explicitly whether this exceptional family still reaches *some*
   periodic lock (just with a longer transient / different $L$), or
   whether it needs the full general machinery — do not silently assume
   it is "solved trivially by hand" without checking a second instance
   (e.g. $a_1=45=3^2\cdot5$, or $a_1=75=3\cdot5^2$) for consistency.

**Key lemmas (claim + mechanism):**
- Necessity Lemma (step 2 above) — because $3\nmid(a_n+2)$ under the
  locked hypothesis, forcing the index-$1$ legality check to route through
  a non-$3$ prime of $R(a_1)$.
- Sufficiency-side non-collision claim (step 3, OPEN) — because (conjectured)
  the compound gcd-survival condition against all intermediate locked terms
  is combinatorially achievable only for the single smallest non-$3$ prime
  $q=5$ (below $2p=6$), never for $q\ge7$.

**Open gaps:** step 3 (the hard direction: proving $q\ge7$ never permits
lock-breaking) is unproved; step 4 (characterizing the $5\mid a_1$
exceptional family beyond the single hand-verified instance $a_1=15$) is
unproved.

**Cases to cover:** $R(a_1)=\{3\}$ (prime powers, free corollary of step
2, already closed); $R(a_1)=\{3,q\}$, $q\ge7$ prime (target of step 3);
$R(a_1)=\{3,q\}$ with $q\ge7$ composite factor structure vs. $a_1$ with
$\ge3$ distinct prime factors including $3$ but not $5$ (not yet tested
numerically by the explorer beyond two-prime seeds — flag this as an
untested case, do not assume the two-prime numerics generalize without
checking at least one $\ge3$-prime instance, e.g. $a_1=3\cdot7\cdot11$);
$5\mid a_1$ (exceptional family, step 4).

**Watch out for:** do not assume the $q<2p$ threshold transfers to other
$p$ without an explicit check (the plateau-break explorer's $p=11$
proximity-threshold refutation is for a different, unrelated proximity
mechanism — verify, don't assume, whether it also refutes this specific
$q<2p$ candidate at $p=11$: if $p=11$'s only failures were at $q=13,17,19$
(all close, all $<2p=22$) that would actually be *consistent* with this
new candidate threshold, since the explorer's refutation was of "failures
confined to close $q$" as a blanket rule against a *different* prior
mechanism, not this specific $q<2p$ formulation — re-derive from the raw
$p=11$ data before either using or discarding it).
