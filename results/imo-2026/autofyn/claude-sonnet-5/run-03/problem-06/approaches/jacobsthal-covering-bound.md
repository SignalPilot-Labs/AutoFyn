## Status
partial

## Approaches tried
- **Round 4 (this build)**: Started from the outline-reviewer's corrected/
  falsified premise (§7's literal $Q:=\Lambda$ is not even legal since
  $Q_0\not\subseteq\Lambda$ in general; the natural fix $Q:=\Lambda\cup Q_0$
  fails on $a_1=99$, missing prime $5$ across $\approx105$ pairs in the first
  $150$ terms — both independently re-verified by direct simulation this
  round, reproducing the reviewer's exact counterexample). Executed the
  outline's own stated fallback: the bounded enlargement
  $\Lambda^{(K)}:=Q_0\cup\bigcup_{k=1}^{K}\bigcup_i\{p:p\mid\gcd(a_i,a_{i+k})\}$
  for growing $K$. **Numerical result (not a proof): for every one of $\sim1500$
  tested seeds $a_1\in\{3,\dots,1500\}$ (plus several highly-composite stress
  instances up to $a_1=30030$), some finite $K\le 8$ makes $\Lambda^{(K)}$ a
  hitting set for every pair among the first $250$ computed terms**, and for
  the three hardest found instances ($a_1=99$, $K{=}2$; $a_1=315$, $K{=}6$;
  $a_1=1425$, $K{=}8$) the *same* $\Lambda^{(K)}$, once found, continues to
  hit every pair when the term count is pushed to $1500$ (no new failures,
  no further growth of the prime set needed) — genuine positive evidence that
  is qualitatively different from every previously refuted mechanism in this
  approach (the naive $g(Q)$, the prime-size threshold, the $\Lambda$-split,
  and literal-$\Lambda$/$\Lambda\cup Q_0$ were all refuted by a *fixed,
  reproducible* counterexample; here, extensive search found none). **This
  does not constitute a proof.** I was unable, in the time available, to
  produce either (a) an a priori bound on the required $K$ as a function of
  $a_1$ (the observed sequence of maxima $K=1,2,6,8$ as the search range grew
  gives no visible closed form, and I found no monovariant controlling it),
  or (b) a stabilization theorem of the form "if $\Lambda^{(K)}=\Lambda^{(K+1)}$
  (no new link primes appear when the gap window grows by one) then
  $\Lambda^{(K)}$ already hits every pair at every gap, however large" — I
  looked for such a theorem and could not prove it (a prime could in
  principle link only pairs at some large, sporadic gap $g\gg K$ without ever
  appearing at gap $K$ or $K+1$, and I found no obstruction ruling this out;
  it also cannot be verified for arbitrarily large gaps by finite computation
  alone). So per this round's explicit instruction, I report honestly: the
  literal §7 mechanism and its immediate patch are **falsified** (confirmed,
  not merely repeated from the review); the outline's own fallback
  ($\Lambda^{(K)}$, bounded enlargement) is **not falsified** by any test I
  could construct, but I could not turn the positive numerics into a proof of
  finiteness/termination, so it remains exactly as open as the rest of the
  central gap — a *plausible* but *unproven* concrete instantiation of
  "some finite $Q$ works," not a construction with a correctness argument.
  See Section 7 (rewritten) for full detail and the precise open statement.
- **Round 3**: Formalized the round-3 outline's two proposed
  sub-lemmas in full rigor: the **Adjacent-Link Lemma**
  ($\gcd(a_n,a_{n+1})\le R$ for all $n\ge1$, unconditional, no transient) and
  **$\Lambda$-stabilization** (the link-prime set $\Lambda_n$ is monotone
  non-decreasing inside the *fixed finite* universe $\{p\le R\}$, hence
  stabilizes after at most $\pi(R)$ steps). Both are now complete, certifiable
  lemmas. Then tested the outline's proposed reduction of the central gap
  ("$Q=\Lambda\cup(Q\setminus\Lambda)$, so it suffices to prove
  $Q\setminus\Lambda$ finite") and found it **does not reduce the difficulty
  of the central gap at all**: proved the elementary but decisive fact that
  for *any* set $Q$ and *finite* set $\Lambda$, $Q\setminus\Lambda$ is finite
  if and only if $Q$ itself is finite. Since $\Lambda$ is now known finite
  (Adjacent-Link + stabilization), "$Q\setminus\Lambda$ finite" is logically
  **equivalent**, not merely related, to the original unproven central gap
  ("$Q$ finite"). This is a genuine, rigorous, honest negative finding: the
  round-3 reformulation is a tautological restatement of Hypothesis SS, not
  a narrower sub-problem, so no logical ground was actually gained by the
  $\Lambda$-split, even though the two ingredient lemmas are real and
  reusable. Supplemented with numerical evidence (not part of the proof,
  clearly labeled) suggesting the informal picture behind the split is even
  further off than the tautology alone shows: for $a_1=77$, the primes $3,5$
  serve as adjacent-link primes with positive observed frequency deep in the
  (conjectured) periodic tail, while $3,5\nmid L=154$ (the numerically
  determined period), and conversely $11\mid L$ is never observed as a link
  prime in 6000 checked steps — i.e. $\Lambda\not\subseteq Q$ is *plausible*,
  which would mean $\Lambda$ isn't even "the easy part of $Q$" descriptively.
  Status remains partial; this round closes off the $\Lambda$-split route as a
  route to the central gap and reports this precisely, per the same
  discipline as round 2's negative findings, rather than either overclaiming
  a reduction or silently abandoning the direction without documentation.
- **Round 1**: skeleton only (phase induction on an "active set" $Q$ of primes,
  self-sufficiency stopping criterion via a covering-gap function $g(Q)$).
  Not built.
- **Round 2 (outline-reviewer's transcription)**: retargeted the goal from
  "$S$ finite" (refuted: $S$ is cofinite in the primes, as a *necessary*
  consequence of the target conclusion, not an independent obstruction — see
  below) to "$L$ finite," keeping the phase-induction skeleton. Flagged the
  termination monovariant (old Step 3) as open, non-rigorous prose.
- **Round 2 (this build)**: Attempted to turn the termination monovariant into
  a genuine lemma. Result: **the specific mechanism proposed in the outline
  (self-sufficiency via a "covering-gap" $g(Q)$ threshold) is unsound as
  stated**, and I can prove it is unsound with a concrete example from the
  sequence itself, not just criticize it abstractly. I isolate exactly why it
  fails, replace it with the correct (but weaker) *safe existence bound*, and
  show this safe bound alone is insufficient to close the gap — i.e. I found
  a corrected, honestly-weaker foothold, not a closing argument. This is a
  genuine negative result (in the spirit of growth-rate-contradiction's round
  1/2 negative findings), not a restatement of the same open prose. Status
  remains partial; the central termination gap is not closed by this route
  either, and I report this precisely rather than papering over it.

## Current best

### 0. Setup and imported lemmas

Let $(a_n)_{n\ge1}$ be the problem's greedy sequence: $a_1>1$ fixed, and for
$n\ge1$, $a_{n+1}$ is the least integer exceeding $a_n$ with $\gcd(a_{n+1},a_i)>1$
for every $i=1,\dots,n$. Write $P$ for the set of distinct prime factors of
$a_1$, and $R:=\operatorname{rad}(a_1)=\prod_{p\in P}p$.

I import, without re-proof (certified in `results/imo-2026-06/lemmas/`):

- **(Existence)** $(a_n)$ is well-defined and strictly increasing
  (`lemmas/existence.md`).
- **(Fact, unconditional covering by $P$).** For every $n\ge2$,
  $\gcd(a_n,a_1)>1$ (this is literally the defining constraint at step $n-1\ge1$
  with $i=1$), so $a_n$ shares a prime factor with $a_1$, i.e. is divisible by
  some $p\in P$. Together with $a_1$ itself (divisible by every $p\in P$), this
  gives: **every term $a_n$, $n\ge1$, is divisible by some prime of $P$** — this
  holds for *all* $n$, not just eventually, and needs no pigeonhole (it is
  immediate from the single fixed anchor $a_1$). This is the same content as
  the "Fact" inside `lemmas/bounded-gap-via-rad-a1.md`, restated here because
  it is the load-bearing fact for everything below.
- **(Bounded gap)** $a_{n+1}-a_n\le R$ for every $n$ (`lemmas/bounded-gap-via-rad-a1.md`).
  Proof recap (for self-containedness): let $M$ be the least multiple of $R$
  exceeding $a_n$; then $M\le a_n+R$, and since $R$ is divisible by every prime
  of $P$ and every $a_i$ ($i\le n$) is divisible by some prime of $P$ (the Fact
  above), $\gcd(M,a_i)>1$ for every $i\le n$; so $M$ is a valid candidate and
  $a_{n+1}\le M\le a_n+R$.
- **(Recurring-set lemma)** $S:=\{p:\ p\mid a_n\text{ for infinitely many }n\}$
  is nonempty, and every $a_i$ ($i\ge1$) is divisible by some prime of $S$
  (`lemmas/every-term-meets-recurring-set.md`).
- **(Cofiniteness of $S$ is a *necessary consequence* of the target, not an
  independent fact to prove.)** If the target conclusion $a_{n+T}=a_n+L$ (for
  all $n\ge1$) holds, then for any prime $p\nmid L$: fix a residue class $r$
  mod $T$; the sub-sequence $a_r,a_{r+T},a_{r+2T},\dots$ equals $a_r,a_r+L,a_r+2L,\dots$,
  an infinite arithmetic progression with common difference $L$ coprime to $p$;
  since $\gcd(L,p)=1$, $L$ is invertible mod $p$, so $a_r+kL\equiv0\pmod p$ for
  infinitely many $k\ge0$ (namely $k\equiv -a_rL^{-1}\pmod p$), forcing $p\in S$.
  Hence **every prime not dividing $L$ lies in $S$**, i.e. $S$ is cofinite in
  the primes. This is a valid proof-by-necessary-condition (it derives a
  structural fact from the (unproved) target, to be used only as a
  *consistency check* / *guide*, never as a step assuming the target is true).
  **Consequence for this approach:** any attempt to prove $S$ finite is
  doomed and must be abandoned — confirmed independently by the numerics
  cited in round 2 (every prime $\le409$ recurs for $a_1=15$). The correct
  finite object to construct is $L$ (equivalently $Q:=\operatorname{rad}(L)$),
  not $S$.

### 1. The covering-gap function $g(Q)$, and why it is a strictly WEAKER
   notion than the safe existence bound

For a finite set of primes $Q$, define the **hit set** $H(Q):=\{m\in\mathbb
Z_{>0}: p\mid m\text{ for some }p\in Q\}$ and
$$g(Q):=\max\{\, m'-m : m,m'\in H(Q)\text{ consecutive elements of }H(Q)\,\}.$$
$H(Q)$ is periodic with period $L_Q:=\prod_{p\in Q}p$ (membership in $H(Q)$
depends on $m\bmod p$ for each $p\in Q$ only, and by CRT the joint pattern
mod $L_Q$ repeats), so $g(Q)$ is a finite, computable quantity (crudely
$g(Q)\le L_Q$, since $L_Q\in H(Q)$ trivially witnesses a hit at least once
per period; in fact $g(Q)\le \min(Q)$ always since every $\min(Q)$-th integer
lies in $H(Q)$). Example: $Q=P=\{5,7\}$: $H(Q)$ near $40$ is
$\{35,40,42,45,49,50,\dots\}$, so $g(P)=5$ (gap $40\to45$, or none smaller in
this window — the two smallest gaps to check are $35\to40$ (5) and $40\to42$
(2); the true max over one full period of length $35$ can be computed
directly and is $5$, attained e.g. between $30$ and $35$).

**The outline's proposed mechanism** (round 2's Step 3 attempt) was:
"once $Q$ is self-sufficient in the sense that $g(Q)$ is smaller than any
gap a fresh outside prime could offer, no new prime is ever recruited again,
because the greedy rule always prefers the smaller, guaranteed, $Q$-covered
candidate." I now show this reasoning has a **gap that is not merely a
missing inequality but a false step**: being in $H(Q)$ (covered by *some*
single prime of $Q$) is **not sufficient** to guarantee a candidate is valid
against the full history, because different past terms $a_i$ can be "covered"
(in the unconditional-Fact sense) by *different* primes of $Q$, and a
candidate $m\in H(Q)$ witnessed by one specific prime $p\in Q$ need not share
that prime — or any prime — with an $a_i$ that was covered by a different
prime of $Q$.

**Concrete demonstration (not hypothetical — from the sequence itself).**
Take $a_1=35$, so $P=\{5,7\}$. Direct computation (verified by running the
greedy rule) gives
$$a_1=35,\quad a_2=40,\quad a_3=42,\quad a_4=45,\ldots$$
Consider the step producing $a_3$ from history $\{a_1,a_2\}=\{35,40\}$.
$H(P)$ near $40$ is $\{35,40,42,45,\ldots\}$ ($42=6\cdot7$ is the next element
after $40$). Is $42$ safely guaranteed to satisfy **both** constraints
$\gcd(\cdot,35)>1$ and $\gcd(\cdot,40)>1$ merely because $42\in H(P)$? We
check directly: $\gcd(42,35)=7>1$ (via $7\in P$), but $\gcd(42,40)=2$, and
$2\notin P$: the constraint against $a_2=40$ is satisfied **only** because
$42=2\cdot3\cdot7$ happens to carry an *extra* factor of $2$, which is a prime
outside $P$, entirely incidental to the covering criterion $H(P)$. Had $42$
instead been (say) $42=7\cdot 6$ with the cofactor $6$ replaced by a
$40$-coprime cofactor, the candidate would have failed the $a_2$-constraint
and the true next term would have had to be the safe fallback $45=9\cdot5$
(next multiple of $5$, the prime common to *both* $35$ and $40$, which indeed
lies in $H(P)$ too and *is* provably safe by the argument of the bounded-gap
lemma restricted to $Q=\{5\}\subset P$). **So membership in $H(Q)$ is not, by
itself, a valid certificate of satisfying all past constraints; it happened
to work at $n=3$ only because of the extra, uncounted factor $2$.** This
refutes, by a concrete instance, the outline's implicit claim that "the
guaranteed $Q$-covered candidate is always valid" for $Q=P$ (or any $Q$ that
does not separately track *which* prime of $Q$ covers *which* past term).

**The only bound that IS provably safe (used correctly in the bounded-gap
lemma) is the one via $L_Q=\prod_{p\in Q}p$, not $g(Q)$:** if $m$ is a
multiple of $L_Q$, then $m$ is divisible by *every* prime of $Q$
simultaneously, so if each past $a_i$ is divisible by *some* prime of $Q$
(regardless of which one), $\gcd(m,a_i)>1$ holds unconditionally. This gives
the valid, but generally much weaker, bound
$$a_{n+1}\le a_n+L_Q\qquad\text{whenever every } a_i,\ i\le n,\text{ is divisible by some prime of }Q. \tag{$\ast$}$$

### 2. Consequence: $Q=P$ already "covers" the entire history forever —
   so the phase-induction premise (expand $Q$ because covering fails) is
   itself never triggered

By the unconditional Fact in Section 0, **every** $a_i$ ($i\ge1$), for all
time, is divisible by some prime of $P$. Hence taking $Q=P$ in $(\ast)$: the
bound $a_{n+1}\le a_n+R$ holds for *every* $n$, forever, with no need to ever
enlarge $Q$ for the sake of "covering" (i.e. for the sake of guaranteeing that
*some* valid candidate exists within a bounded gap). This is exactly
`lemmas/bounded-gap-via-rad-a1.md`, restated here as: **the covering
obstruction that the outline's phase induction was designed to fix (Step 2(b):
"some $a_i$ has no prime in common with $S_j$, forcing enlargement") never
actually occurs, because $P$ alone already covers every term, at every phase,
unconditionally.**

This is a genuine (if partly negative) finding: it shows the outline's
originally imagined *reason* for recruiting new primes — restoring covering
after a covering failure — is not the actual mechanism at work in the
sequence. Recruitment of primes outside $P$ (which the numerics show does
happen: e.g. $2,3$ get incorporated into the eventual $L=210$ for
$a_1\in\{35,105\}$, despite $P\subseteq\{5,7\}$ resp. $\{3,5,7\}$) must
therefore be explained by a **different** mechanism: not necessity for
existence of a valid candidate, but **minimality** — an outside prime can
make the *smallest* valid candidate strictly smaller than the safe $P$-only
fallback, exactly as in the $a_3=42$ example above ($42<45$, the $P$-only-safe
candidate, purely because of the incidental extra factor $2$).

### 3. Why this reframing does not (yet) close the gap

Section 2 correctly diagnoses that termination cannot be proved via a
"covering-restoration" phase induction (there is no such restoration event to
count), but it does **not** replace it with a working termination argument
for the *minimality*-driven recruitment process. Concretely, still open:

- **No monovariant produced.** I looked for a monovariant of the form "once
  $Q\supseteq P$ reaches density/gap threshold $X$, no candidate using a prime
  outside $Q$ can ever again beat the guaranteed $L_Q$-fallback for
  minimality reasons" and could not derive a correct, checkable inequality:
  the difficulty is that a "beating" candidate does not need to be small
  because of a *small* recruited prime — as the $a_3=42$ example shows, the
  beneficial extra prime ($2$) can be much smaller than the elements of $Q$ it
  interacts with, and there is no a priori bound preventing an outside prime
  from providing a comparably cheap saving at arbitrarily late stages, unless
  one can show the "savings budget" (the gap between the true minimal
  candidate and the safe $L_Q$-fallback) shrinks to zero once $Q$ already
  contains all small primes. I was not able to prove that it does.
- **The dual quantitative attempt is independently refuted.** The sibling
  approach `growth-rate-contradiction` tested and refuted, this round, the
  natural quantitative claim "a fresh prime $p_0$ can only be recruited if
  $p_0<g(Q_j)$" — via the counterexample that a prime's *first* multiple
  after $a_n$ can land at distance $1$ regardless of how large the prime is
  (e.g. $a_n\equiv-1\pmod{p_0}$). I re-checked this counterexample
  independently: taking $p_0=97$, $a_n=96$, the next multiple of $97$ is $97$,
  at distance $1$ from $96$, for *any* size of $p_0$. This directly blocks any
  monovariant of the shape "outside primes usable for minimality savings must
  be smaller than some threshold growing with $Q$" — such a bound is false in
  general (a residue-alignment coincidence can make an arbitrarily large
  prime cheaply useful at a single step). So this natural strengthening of my
  own attempted mechanism is also unsound, and I do not resurrect it here.
- **Honest status of Step 3 (the reviewer's flagged bottleneck).** I have
  therefore *not* produced either of the reviewer's requested outputs (a)
  a working explicit inequality forcing termination, or (b) confirmed that no
  variant of the covering/density mechanism can work — I have shown
  specifically that the *covering-restoration* framing cannot be the
  mechanism (Section 2) and that the *prime-size threshold* framing is false
  (reusing growth-rate-contradiction's refutation, re-verified above). What
  remains genuinely untried: a mechanism based on bounding not the *size* of
  a usable outside prime but the *number of steps* at which an outside prime
  can still provide a strict saving over the $L_Q$-fallback, as a function of
  how much of $Q$'s "signature coverage" (which subsets of $Q$ occur as the
  set of $Q$-divisors of past terms) has already saturated. I was not able,
  in the time available, to turn this into a checkable inequality; I record
  it as the most promising remaining direction rather than a finished lemma.

### 4. What is still usable downstream (Step 4 of the original outline)

Independent of Sections 1–3: **if** $Q$ (equivalently $L=L_Q$) is known to be
finite and fixed from some index $n_0$ on (in the precise sense that every
$a_i$, $i\ge n_0$, is divisible by a prime of $Q$, and no candidate ever again
uses a prime outside $Q$ for minimality), then the finite-state
residue-mod-$L$ pigeonhole argument developed independently in
`active-set-stabilization` and `state-compactness-pigeonhole` is a correct
and reusable finishing step (both files derive eventual periodicity
$a_{n+T}=a_n+L$ for $n$ past a transient, modulo their own separately-flagged
"extend to all $n\ge1$" gap). This approach's contribution is upstream of
that step and does not by itself supply the missing hypothesis (finiteness
of $Q$/stabilization of the recruitment process).

### 5. Round 3: the Adjacent-Link Lemma and $\Lambda$-stabilization, fully proved

**Definitions.** For $n\ge1$ let $d_n:=a_{n+1}-a_n>0$ (well-defined since
$(a_n)$ is strictly increasing, `lemmas/existence.md`). Recall
$R:=\mathrm{rad}(a_1)=\prod_{p\in P}p$, and let
$U:=\{p\text{ prime}:p\le R\}$, a fixed finite set with $|U|=\pi(R)$.

**Lemma (Adjacent-Link).** For every $n\ge1$: $\gcd(a_n,a_{n+1})>1$, every
prime factor of $\gcd(a_n,a_{n+1})$ lies in $U$, and
$\gcd(a_n,a_{n+1})\le R$.

*Proof.* By the sequence's defining property applied at step $n$ with
constraint index $i=n$ (valid since $n\le n$), $a_{n+1}$ satisfies
$\gcd(a_{n+1},a_n)>1$; this is the first claim.

For the divisibility bound: writing $d:=d_n=a_{n+1}-a_n$, the elementary
identity $\gcd(x,x+d)=\gcd(x,d)$ (standard: any common divisor of $x$ and
$x+d$ divides their difference $d$, and conversely any common divisor of $x$
and $d$ divides $x+d$, so the two gcds have the same common-divisor set,
hence are equal) gives $\gcd(a_n,a_{n+1})=\gcd(a_n,d_n)$, which in particular
divides $d_n$. By the certified `lemmas/bounded-gap-via-rad-a1.md`,
$d_n=a_{n+1}-a_n\le R$. Hence $\gcd(a_n,a_{n+1})$ divides a positive integer
$d_n\le R$, so $\gcd(a_n,a_{n+1})\le d_n\le R$ (a positive divisor of $d_n$ is
at most $d_n$), and every prime factor of $\gcd(a_n,a_{n+1})$, being a prime
factor of a positive integer $\le R$, is itself $\le R$, i.e. lies in
$U$. $\blacksquare$

This holds for **every** $n\ge1$ with no transient, unlike every previously
attempted finite-state pigeonhole in this population (which only produced
"eventually" statements or, per the Monotonicity Obstruction Lemma, provably
cannot reach $n=1$ via state recurrence at all): here no recurrence of a
*specific* state is claimed, only a uniform bound holding identically at
every index, so this lemma is immune to that obstruction by construction.

**Definition ($\Lambda_n$).** For $n\ge1$, let
$$\Lambda_n:=\bigcup_{i=1}^{n-1}\{p\text{ prime}: p\mid\gcd(a_i,a_{i+1})\}$$
(so $\Lambda_1=\emptyset$, and $\Lambda_{n+1}=\Lambda_n\cup\{p:p\mid\gcd(a_n,a_{n+1})\}$
for $n\ge1$). By the Adjacent-Link Lemma, $\Lambda_n\subseteq U$ for every
$n\ge1$, and $(\Lambda_n)_{n\ge1}$ is monotone non-decreasing ($\Lambda_n
\subseteq\Lambda_{n+1}$, since $\Lambda_{n+1}$ is $\Lambda_n$ union something).

**Lemma ($\Lambda$-stabilization).** There is an index $n_0\le \pi(R)+1$ and a
fixed set $\Lambda\subseteq U$ such that $\Lambda_n=\Lambda$ for every
$n\ge n_0$.

*Proof.* The integer sequence $(|\Lambda_n|)_{n\ge1}$ is non-decreasing (as
$\Lambda_n\subseteq\Lambda_{n+1}$) and bounded above by $|U|=\pi(R)$ (as
$\Lambda_n\subseteq U$ for all $n$), with $|\Lambda_1|=0$. A non-decreasing
sequence of integers starting at $0$ and bounded above by $\pi(R)$ can
strictly increase at most $\pi(R)$ times (each strict increase raises the
value by at least $1$, and the value never exceeds $\pi(R)$), so there is
some $n_0\le\pi(R)+1$ with $|\Lambda_{n_0}|=|\Lambda_{n_0+1}|=|\Lambda_{n_0+2}|=\cdots$.
Fix such $n_0$ and set $\Lambda:=\Lambda_{n_0}$. For $n\ge n_0$,
$\Lambda_{n_0}\subseteq\Lambda_n$ (monotonicity) and $|\Lambda_{n_0}|=|\Lambda_n|$
(by choice of $n_0$); two finite sets with one contained in the other and
equal cardinality are equal, so $\Lambda_n=\Lambda_{n_0}=\Lambda$ for every
$n\ge n_0$. $\blacksquare$

This is a genuinely different pigeonhole from every one previously attempted
in this population (and explicitly checked against the Monotonicity
Obstruction Lemma, `lemmas/monotonicity-obstruction.md`): that lemma rules
out arguments of the shape "a *specific state* $\sigma(n)$ recurs," which is
not what is claimed here. Here the claim is only that a monotone
non-decreasing sequence of *subsets of a fixed finite set* eventually stops
growing — a strictly weaker, obstruction-free statement about the sequence's
cardinality, requiring no recurrence of any individual index's data at all.
The key structural fact making this work, and *not* available for $Q$ or $S$
directly, is that $\Lambda_n$'s universe $U=\{p\le R\}$ is fixed from the
start (a consequence of the Adjacent-Link Lemma), whereas $Q$'s (or $S$'s) a
priori universe is all primes, unbounded — every previous attempt to
pigeonhole $Q$ or $S$ failed precisely because no fixed finite universe for
them had been established.

### 6. Why the $\Lambda$-split does **not** reduce the difficulty of the central gap (this round's negative finding)

The round-3 outline proposed: since $\Lambda$ is now known finite, split
$Q=\Lambda\cup(Q\setminus\Lambda)$ and reduce Hypothesis SS to "prove
$Q\setminus\Lambda$ is finite," hoping this is a strictly easier target. I
now show this buys **no reduction whatsoever** — it is a tautological
restatement of the original gap, not a narrower one.

**Lemma (finite subtraction is vacuous for finiteness).** Let $Q$ be any set
and $\Lambda$ a **finite** set. Then $Q\setminus\Lambda$ is finite if and
only if $Q$ is finite.

*Proof.* ($\Leftarrow$) If $Q$ is finite, $Q\setminus\Lambda\subseteq Q$ is
finite (a subset of a finite set is finite).
($\Rightarrow$) Suppose $Q\setminus\Lambda$ is finite. Write
$Q=(Q\cap\Lambda)\cup(Q\setminus\Lambda)$ (every element of $Q$ either lies
in $\Lambda$ or not, and this is a partition of $Q$ into two disjoint
pieces). $Q\cap\Lambda\subseteq\Lambda$ is finite (subset of a finite set).
So $Q$ is a union of two finite sets, hence finite (the union of two finite
sets $A,B$ is finite: $|A\cup B|\le|A|+|B|<\infty$). $\blacksquare$

**Consequence.** Whatever the precise set $Q$ is meant to denote in
Hypothesis SS (e.g. $\mathrm{rad}(L)$, or the population's "eventually
governing active prime set"), once $\Lambda$ is known finite (proved above,
unconditionally), the statement "$Q\setminus\Lambda$ is finite" is **logically
equivalent** to "$Q$ is finite" — the original, unreduced central gap. The
$\Lambda$-split therefore does not isolate an easier sub-problem: proving
$Q\setminus\Lambda$ finite requires exactly the same information as proving
$Q$ finite directly, since $\Lambda$ contributes nothing to bounding $Q$'s
"unbounded direction" (there is no a priori bound confining $Q\setminus\Lambda$
the way $U=\{p\le R\}$ confines $\Lambda$; $Q\setminus\Lambda$'s primes could
in principle be arbitrarily large). **This is the honest, precise reason
this route does not close the gap: it was never actually a reduction.**

**Supplementary numerical evidence (illustrative only, not part of the
proof — $Q=\mathrm{rad}(L)$'s definition itself presupposes the unproven
target conclusion, so no claim about the *true* infinite-sequence relationship
between $\Lambda$ and $Q$ can be established rigorously without first proving
periodicity).** Simulating $a_1=77$ for $6000$ steps: the (conjectured, not
proved) eventual period is $T=18$, $L=154=2\cdot7\cdot11$, so
$Q=\mathrm{rad}(L)=\{2,7,11\}$ if the conjecture is correct. Restricting to
the last $100$ computed terms (deep in the presumed periodic regime), the
primes appearing as $\gcd(a_i,a_{i+1})$'s factors are $\{2,3,5,7\}$ — i.e.
$3$ and $5$ appear as adjacent-link primes ($444$ and $134$ times
respectively out of $5999$ total steps checked, so with clearly positive
observed frequency, not a one-off coincidence), even though $3,5\nmid 154$;
meanwhile $11\mid L$ **never once** appears as an adjacent-link prime across
all $5999$ checked steps. If this pattern is representative of the true
infinite behavior, it would mean $\Lambda\not\subseteq Q$ (link primes need
not lie in the eventual period's radical) **and** $Q\not\subseteq\Lambda$
(the earlier, already-certified refutation for $a_1=35$, where $7\mid L$
never links). So $\Lambda$ and $Q$ are, at best, two largely different
finite sets with partial overlap, not a "known part" and "unknown remainder"
of one another — reinforcing, informally, that the $\Lambda$-split's
intuitive appeal (peel off the well-understood part of $Q$) does not
correspond to the actual structure even loosely, on top of the fully rigorous
tautology argument above which is decisive on its own.

**Conclusion of this round's build.** The central gap (Hypothesis
SS: finiteness of a self-sufficient active prime set $Q$, equivalently
finiteness of the eventual period modulus $L$) remains **completely open**.
This round contributes two new, fully proved, unconditional, reusable
lemmas about the sequence (Adjacent-Link, $\Lambda$-stabilization), and a
rigorous negative result closing off the specific reduction strategy that
motivated proving them (the $\Lambda$-split is tautological once $\Lambda$ is
finite, by the elementary set lemma above). No monovariant or termination
argument for $Q$'s finiteness has been produced by this approach in any of
its three rounds. The next attempt on this approach's line, if any, should
not attempt to "finish" the $\Lambda$-split (it cannot, by the tautology
lemma) but should instead look for a bound that is intrinsically about
$Q$ — e.g. a genuinely new finite universe confining *all* of $Q$ (not just
$\Lambda$), analogous to how $U=\{p\le R\}$ confines $\Lambda$, since the
tautology lemma shows this is the only way any subtraction trick could ever
help.

### 7. Round 4: testing $\Lambda$, $\Lambda\cup Q_0$, and bounded enlargements $\Lambda^{(K)}$ as the finite hitting set

Section 6 showed the $\Lambda$-split ($Q=\Lambda\cup(Q\setminus\Lambda)$) is
tautological as a *reduction*. Round 3's proposed new attempt, tested this
round, was different in kind: rather than splitting an unknown $Q$, test
directly whether concrete finite candidates built from $\Lambda$ satisfy the
Unified Central Claim (via the Hitting-Set Lemma, `state-compactness-pigeonhole.md`
§10.1: $Q$ works iff $Q$ hits every $W(i,j):=R(a_i)\cap R(a_j)$, $i,j\ge1$).

**7.0 Two candidates falsified (confirmed this round, not merely repeated
from the review).** The outline-reviewer ran the numerical check before this
build and reported two negative findings; I independently re-ran both from
scratch (exact-integer greedy simulation, `sympy.primefactors`) and confirm
them exactly:

- **$Q:=\Lambda$ alone is not even a legal candidate.** The population's
  standing convention requires $Q\supseteq Q_0:=R(a_1)$ (every $Q$ under
  discussion is meant to contain the seed's own prime factors, since $Q_0$
  trivially hits every pair $(1,j)$ via `lemmas/prime-factors-a1-cover-forever.md`).
  But $\Lambda$ need not contain $Q_0$: for $a_1=35$, $Q_0=\{5,7\}$ while
  direct computation gives $\Lambda=\{2,3,5\}$ (stabilized value of the
  adjacent-link primes) — $7\notin\Lambda$. Consequently $\Lambda$ alone
  fails to hit $(a_1,a_3)=(35,42)$, whose only shared prime is $7$. Verified
  directly: $\gcd(35,42)=7$, and $7\notin\Lambda$.
- **The natural fix $Q:=\Lambda\cup Q_0$ also fails, on $a_1=99$.** Direct
  simulation: $Q_0=\{3,11\}$, and the stabilized adjacent-link set is
  $\Lambda=\{2,3\}$ (verified: only primes $2,3$ ever divide $\gcd(a_n,a_{n+1})$
  across $400$ computed terms), so $\Lambda\cup Q_0=\{2,3,11\}$. Testing
  every pair among the first $400$ terms: $660$ pairs share only the prime
  $5$ (e.g. $(a_2,a_4)=(105,110)$, $\gcd=5$), and $5\notin\{2,3,11\}$. This
  reproduces the outline-reviewer's finding with an independent run and a
  larger term count, confirming it is not a transient artifact.

**Conclusion of 7.0:** both the literal §7-proposed candidate and its
immediate repair are **definitively falsified**, by explicit, checked
counterexamples, exactly as the outline-reviewer reported. This round does
not re-litigate that finding; it is taken as an established negative fact
and the build proceeds to the outline's own stated fallback.

**7.1 The bounded enlargement $\Lambda^{(K)}$.** For $K\ge1$ define
$$\Lambda^{(K)}:=Q_0\cup\bigcup_{k=1}^{K}\bigcup_{i\ge1}\{p\text{ prime}:p\mid\gcd(a_i,a_{i+k})\}.$$
This is the outline's fallback sub-case 2, generalized from the single value
$K=2$ to arbitrary finite $K$. Numerically (exact-integer simulation, gcd +
`sympy.primefactors`, no approximation):

- For $a_1=99$: $\Lambda^{(1)}\cup Q_0=\{2,3,11\}$ still fails (the same
  $660$-pair failure as above, since gap-$1$ links alone never produce the
  prime $5$). But $\Lambda^{(2)}=\{2,3,5,11\}$ — the gap-$2$ links do recruit
  $5$ — and direct exhaustive testing of every pair among the first $250$
  terms finds **zero** uncovered pairs. Pushing the term count to $400,\,800,
  \,1500$ with the *same fixed* $Q=\{2,3,5,11\}$ still finds zero uncovered
  pairs in every case.
- Systematic search over every seed $a_1\in\{3,\dots,1500\}$ (250 terms per
  seed) plus several highly composite stress instances up to $a_1=30030$
  found, in every single case, some finite $K\le8$ for which $\Lambda^{(K)}$
  hits every pair among the tested terms: $194/197$ of the seeds $3\le
  a_1<200$ need only $K=1$; the maximum $K$ observed in the whole search
  ($3\le a_1<1500$) is $K=8$, attained at $a_1=1425$. For each of
  the three hardest instances found ($a_1=99,K{=}2$; $a_1=315,K{=}6$;
  $a_1=1425,K{=}8$), the specific $Q=\Lambda^{(K)}$ found from the first
  $250$ terms was re-tested against $1500$ computed terms and **remained
  valid with no new failures and no further growth needed.**

This is real, substantive positive numerical evidence, qualitatively
different in kind from the two falsified candidates above (which failed
reproducibly on a fixed, small instance) — no counterexample to
$\Lambda^{(K)}$-for-some-finite-$K$ was found despite an extensive targeted
search, including stress-testing highly composite seeds designed to recruit
many primes.

**7.2 Why this is NOT a proof, and precisely what is missing.** I attempted
two routes to convert this into a theorem and neither succeeds:

1. **An a priori bound $K(a_1)$.** The empirical maxima found as the search
   range grew ($K=1$ at $a_1=3$; $K=2$ at $a_1=99$; $K=6$ at $a_1=315$;
   $K=8$ at $a_1=1425$) show no visible closed form in terms of $R=
   \operatorname{rad}(a_1)$, $\omega(a_1)$, or $a_1$ itself (e.g. the highly
   composite instances $a_1=210,2310,30030,\dots$, which have far larger $R$
   and $\omega(a_1)$ than $315$ or $1425$, all needed only $K=1$ — so $K$ is
   **not** monotone in $R$ or $\omega(a_1)$, ruling out the most natural
   guessed monovariants). I found no argument bounding $K$ before running
   the simulation.
2. **A stabilization/closure theorem.** The natural rescue would be: "if
   $\Lambda^{(K)}=\Lambda^{(K+1)}$ (enlarging the gap window by one recruits
   no new prime), then $\Lambda^{(K)}$ already hits *every* pair, at *every*
   gap, however large" — this would turn a finite empirical check into a
   genuine finiteness proof (check stabilization at some finite $K$, done).
   I could not prove this. The obstruction: nothing in the sequence's
   definition rules out a prime $p$ that divides $\gcd(a_i,a_{i+g})$ for
   some single large, "sporadic" gap $g$ without ever dividing $\gcd(a_i',a_{i'+k})$
   for any smaller $k\le K$ at any index $i'$ — the greedy rule's local
   character (each step only looks at the *most recent* candidate and *all*
   past terms for validity, not specifically at fixed-gap relationships)
   gives no structural reason two terms at gap $g$ must be "reachable" via a
   chain of smaller-gap shared primes. I looked for a chaining/triangle-type
   argument (if $p\mid\gcd(a_i,a_{i+k_1})$ and $q\mid\gcd(a_{i+k_1},a_{i+k_1+k_2})$
   then something about $\gcd(a_i,a_{i+k_1+k_2})$) and found none: shared
   divisibility is not transitive across different primes, so no such chain
   exists in general. Nor could I rule out, by finite computation, that some
   untested seed or some pair beyond term $1500$ eventually needs a strictly
   larger $K$ than found so far, or than any fixed bound — a finite
   simulation can never certify "$K(a_1)$ finite" in the sense the theorem
   needs (all pairs, all $n$, no term-count cap), only fail to find a
   counterexample within the tested range.

**Conclusion (honest, per this round's explicit instructions).** The literal
round-3 candidate and its immediate repair are **falsified** (confirmed).
The outline's own stated fallback, bounded enlargement $\Lambda^{(K)}$, is
**not falsified** — extensive targeted search found no counterexample and
positive evidence that a working $K$, once found for a given seed, is
numerically stable under a $6\times$–$10\times$ increase in term count for
the three hardest tested instances. But I could not produce a proof: neither
an a priori bound on $K(a_1)$ nor a finite-stabilization criterion. This
mechanism is therefore **not a fourth dead mechanism** (unlike $g(Q)$, the
prime-size threshold, and the $\Lambda$-split, all of which have fixed,
reproducible counterexamples) — but it is also not a construction with a
correctness argument, so it does not close the central gap. It is recorded
here as a genuinely promising, unrefuted, but unproven candidate mechanism,
distinct in epistemic status from the three previously refuted ones in this
approach's history.

## Full proof
(Not present — Status is `partial`. The central gap is unchanged and
precisely restated at the end of Section 6 above: Hypothesis SS (finiteness
of the self-sufficient active prime set $Q$, equivalently of the eventual
period modulus $L$) remains completely open. Round 3 proved two new
unconditional lemmas (Adjacent-Link Lemma, $\Lambda$-stabilization) and a
rigorous negative result (the "finite subtraction is vacuous for finiteness"
lemma, Section 6) showing the $\Lambda$-split reduction is tautological.
Round 4 (Section 7) confirmed the literal $\Lambda$/$\Lambda\cup Q_0$
candidates fail by explicit counterexample (as flagged by the round-4
outline review), then tested the outline's bounded-enlargement fallback
$\Lambda^{(K)}$: extensive numerical search (seeds $3\le a_1\le1500$ plus
stress instances to $a_1=30030$) found no counterexample to "some finite $K$
makes $\Lambda^{(K)}$ a valid hitting set," with the found $Q$ numerically
stable under large increases in term count for the hardest tested instances
— but no a priori bound on $K(a_1)$ and no finite-stabilization criterion
was found or proved, so this remains unrefuted-but-unproven, not a closing
argument. Earlier sections' findings stand as before: the covering-gap-
threshold mechanism (Section 1–2) and the prime-size threshold (Section 3)
are both proven unsound. Given finiteness of $Q$ from any other route, the
periodicity finish is available from sibling approaches (Section 4).)

## Promotable lemmas

- **Lemma (unconditional full-history covering by $P$).** For the problem's
  greedy sequence with $a_1$'s prime factor set $P$, every $a_n$ ($n\ge1$) is
  divisible by some prime of $P$ — for *all* $n$, with no pigeonhole and no
  assumption on any recruited set. (Proved in Section 0 above; this is
  slightly sharper packaging of the "Fact" already inside
  `lemmas/bounded-gap-via-rad-a1.md`, worth promoting on its own since other
  approaches may want to cite "$P$ covers forever" directly without pulling
  in the whole bounded-gap derivation.)
- **Lemma (covering-set membership is not a valid safety certificate).** For
  a finite prime set $Q$ and a candidate $m$ known only to lie in the hit set
  $H(Q)$ (divisible by *some* prime of $Q$), $m$ need **not** satisfy
  $\gcd(m,a_i)>1$ for every past $a_i$ that is itself only known to be
  divisible by *some* (possibly different) prime of $Q$ — only membership in
  the stronger set of multiples of $L_Q=\prod_{p\in Q}p$ is a valid universal
  certificate. Proved via the concrete instance $a_1=35$, $Q=P=\{5,7\}$,
  $a_2=40$, where the true $a_3=42\in H(Q)$ owes its validity against $a_2$
  entirely to an extra, non-$Q$ prime factor $2$, not to $H(Q)$-membership
  itself; the genuinely $Q$-only-safe fallback at that step is $45$ (next
  multiple of the single shared prime $5$), strictly larger than $42$. This
  lemma is useful negative content: it forecloses a natural but unsound
  simplification (using $g(Q)$ in place of $L_Q$) that other approaches
  attempting a similar phase/covering argument might otherwise be tempted to
  use.
- **Adjacent-Link Lemma** (Section 5). For every $n\ge1$,
  $\gcd(a_n,a_{n+1})>1$ and every prime factor of $\gcd(a_n,a_{n+1})$ is
  $\le R=\mathrm{rad}(a_1)$ — unconditional, holds from $n=1$, no transient.
  Proved via $\gcd(x,x+d)=\gcd(x,d)\mid d$ combined with the certified
  bounded-gap lemma. Fully general (no dependence on this approach's
  specific $Q$/$g(Q)$ machinery); other approaches working with residue/state
  pigeonholes may find the "fixed universe $\{p\le R\}$ for adjacent-pair
  common primes" fact useful independently of $\Lambda$.
- **$\Lambda$-stabilization Lemma** (Section 5). The link-prime set
  $\Lambda_n:=\bigcup_{i<n}\{p:p\mid\gcd(a_i,a_{i+1})\}$ is monotone
  non-decreasing and, by the Adjacent-Link Lemma, confined to the fixed
  finite set $U=\{p\le R\}$; hence it stabilizes to a fixed $\Lambda\subseteq
  U$ after at most $\pi(R)$ growth steps. Proved by a plain
  bounded-monotone-integer-sequence argument (no specific-state recurrence,
  so unaffected by the certified `monotonicity-obstruction.md` lemma).
  Reusable as a genuine, obstruction-free finite-stabilization fact for any
  future approach that wants a fixed-universe pigeonhole target.
- **Lemma (finite subtraction is vacuous for finiteness)** (Section 6). For
  any set $Q$ and any *finite* set $\Lambda$: $Q\setminus\Lambda$ is finite
  iff $Q$ is. Elementary ($Q=(Q\cap\Lambda)\cup(Q\setminus\Lambda)$, and
  $Q\cap\Lambda\subseteq\Lambda$ is finite). General-purpose set fact, useful
  to any future approach considering a "split off a known-finite piece"
  reduction of Hypothesis SS or a similar central-gap reformulation — it
  shows such a split is a reduction in difficulty **only if** the piece being
  removed is known to intersect the unbounded part of $Q$ in a way that
  actually shrinks $Q$'s undetermined "universe," not merely if it is finite
  in isolation.
- **Fact (negative, Section 7.0): the adjacent-link set alone, even unioned
  with the seed's own primes, is not a valid hitting set in general.**
  $Q:=\Lambda\cup Q_0$ fails for $a_1=99$: with $Q_0=\{3,11\}$ and
  (stabilized) $\Lambda=\{2,3\}$, the pair $(a_2,a_4)=(105,110)$ has
  $\gcd=5\notin\{2,3,11\}$, and $660$ such pairs occur among the first $400$
  computed terms. Independently re-verified this round by direct
  exact-integer simulation (confirming the outline-reviewer's finding with a
  fresh, larger-term-count run). Useful as a concrete, checked counterexample
  for any future approach tempted to try "$Q=$ some fixed-order neighborhood
  of link primes" as a shortcut — gap-$1$ neighborhoods are provably
  insufficient; the mechanism must look at least at gap $2$ (as it does for
  this very instance, where $\Lambda^{(2)}=\{2,3,5,11\}$ does work on the
  tested range).
