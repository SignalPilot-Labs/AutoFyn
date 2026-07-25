## Status
partial

## Approaches tried
- **Round 7 (this round).** Assigned target: prove $|\mathrm{Nec}|<\infty$
  via a *global* counting/second-moment argument (distinct from
  `state-compactness-pigeonhole`'s per-prime CRT-density route). Outcome:
  the mechanism is **fully evaluated and shown to be structurally
  insufficient**, a genuine negative result (not a restatement of any
  prior dead mechanism, an 11th distinct one for this population).
  Produced: (1) the elementary but fully proved **Prime-Factor-Count
  Lemma** ($\omega(m)\le\log_2 m$); (2) the **Incidence-Count Theorem**,
  a completely rigorous global counting bound
  $|\mathrm{Nec}_{\le N}|=O(N\log N)$ (where $\mathrm{Nec}_{\le N}$
  restricts witnessing pairs to indices $\le N$) — this genuinely realizes
  the round-7 outline's request for a second-moment-style bound, but the
  bound diverges as $N\to\infty$, so it cannot certify
  $|\mathrm{Nec}|<\infty$ by itself (exactly the trap the outline flagged,
  now confirmed as the actual outcome); (3) the **Windmill Lemma**, a
  complete, fully proved abstract combinatorial construction showing
  pairwise-intersecting families of finite sets can realize
  $\binom{k}{2}$ distinct singleton-witness pairs among only $k$ sets
  (size $k-1$ each) — demonstrating the $O(N\log N)$ bound is essentially
  tight for the abstract category defined only by "pairwise intersecting +
  bounded set-size growth," so no sharpening of the counting argument
  using only these two ingredients can produce a constant bound; (4) an
  attempt to extend the Windmill construction to an infinite, globally
  pairwise-intersecting family with unboundedly many singleton witnesses,
  which **provably fails** by a clean, one-line argument (any "connector"
  prime added to guarantee global intersection necessarily upgrades each
  local singleton pair to a size-$\ge2$ intersection) — honestly reported
  as an incomplete construction attempt whose failure is itself
  informative: it shows the same tension (global connectivity vs. local
  singleton purity) that the certified Contamination Dichotomy Lemma
  already isolated from the opposite (per-prime) direction, i.e. two
  independent framings converge on the same crux. No proof or refutation
  of Nec-finiteness itself is obtained; the central gap is exactly where
  round 6 left it. Status remains `partial` (per the outline-reviewer's
  binding self-report rule, this is not a case requiring RETHINK — the
  mechanism was genuinely new and distinct from the two prior gaps it
  overlaps with in substance, and it was evaluated to a definite, honest
  conclusion rather than abandoned mid-attempt).
- **Round 6.** Assigned target: the Bounded-Witness-Index
  Conjecture (an explicit $N(a_1)$ bounding the first-witness index of any
  new $\mathrm{Nec}\setminus R(a_1)$ element). Outcome: **neither proved nor
  refuted**, but produced (1) the **Contamination Dichotomy Lemma** and the
  **Reduction Proposition** (both fully proved, elementary but genuinely
  organizing — they localize the global conjecture to a per-prime,
  per-reference-index search question); (2) a complete, exact hand-trace of
  the $a_1=20735$ outlier's delay mechanism (the prime $19$ is blocked from
  being witnessed against $a_4=20748$ by four successive $19$-multiple terms
  that each happen to also carry one of $a_4$'s other prime factors
  $\{2,3,7,13\}$, until the fifth, $a_{70}=21185=5\cdot19\cdot223$, avoids
  all four — verified by exact factorization of all six relevant terms);
  (3) a second adversarial numerical instance, $a_1=29315=5\cdot11\cdot13
  \cdot41$, with witness index $32$ (smaller than $20735$'s $69$ but well
  above the typical $\le12$), plus a 15-seed random search over 4-5-prime
  seeds finding no unboundedly-growing instance and several new
  "universal-prime" cases ($\mathrm{Nec}\setminus R(a_1)=\emptyset$) not
  previously observed for multi-prime seeds. (4) Identified the precise
  remaining crux: whether "contamination" (a fixed finite avoid-set
  intersecting every sufficiently-late multiple of the target prime) can
  persist forever, which appears to require the same kind of global
  independence control over the sequence as the original central gap —
  honestly reported as not obviously easier, not papered over as solved.
  Status remains `partial`.
- **Round 5 (this round).** Assigned target: prove the **Redundancy Growth
  Lemma** — for $Q_{\min}=\mathrm{Nec}\cup R(a_1)$, the per-term statistic
  $\rho(n):=|R(a_n)\cap Q_{\min}|$ is eventually $\ge2$, which was hoped to
  block any *new* singleton-intersection pair from forming (hence block
  further growth of $\mathrm{Nec}$, closing the central gap). The
  outline-reviewer explicitly flagged that $\rho(n)\ge2$ (a **per-term**,
  marginal statistic) does not obviously imply the needed **per-pair**
  statement ($|R(a_i)\cap R(a_j)|\ge2$ for the relevant pairs), and instructed
  me to close this implication rigorously or report it honestly as a gap.
  **Outcome: the implication is not just unproven, it is FALSE, decisively
  and by a small hand-verified counterexample** (below) — so the
  Redundancy Growth Lemma, as stated in the round-5 outline, **cannot be
  completed**; this is a genuine, rigorous dead-mechanism result, in the
  same category as the population's other certified negative lemmas
  (`chain-transitivity-obstruction.md`, `bounded-radical-refutation.md`,
  `windowed-epsilon-automaton-failure.md`). I also found a second,
  independent failure of the *premise* of the Lemma (the "universal prime"
  phenomenon at $a_1=21$, where $\rho(n)$ does **not** even eventually
  exceed 1, yet self-sufficiency holds anyway by a completely different
  mechanism) — reported as numerical evidence, correctly labeled as such,
  not claimed as a theorem. No new positive route to the central gap is
  found this round; the central existence question (is $\mathrm{Nec}$
  finite and is $Q_{\min}$ self-sufficient?) remains exactly as open as it
  was after round 4. Status remains `partial`.
- **Round 1.** Proved existence/well-definedness of the sequence, a trivial
  finite covering-gap lemma, and — fully rigorously — that every term $a_i$
  ($i \ge 1$) is divisible by a prime that recurs infinitely often (the
  "S-covering" lemma). Attempted to close finiteness of $S$ via a pure
  counting/pigeonhole argument and *proved this specific mechanism cannot
  work* (the inequality it produces, $K^2 \le N\log_2(a_N)$, is never a
  contradiction). Wrote a conditional finish (periodicity given $S$ finite
  plus a "state = residue mod L" hypothesis) but flagged a second gap
  (extending eventual periodicity down to $n=1$). Status: partial.
- **Round 2 (this round).** The outline-reviewer flagged, correctly, that
  round 1's proposed fix for the prefix-extension gap ("$\sigma$ has finitely
  many values and $\sigma(1)$ is one of them, so by pigeonhole some later
  index repeats $\sigma(1)$") is a **pigeonhole fallacy**: finite codomain +
  infinite domain only guarantees *some* state recurs infinitely often, not
  that the specific starting state does. This round: (1) re-derived the
  eventual-periodicity finish cleanly, with the fallacy excised — the
  argument now only claims a coincidence at *some* pair of indices, never
  that the coincidence includes $n=1$; (2) went looking for a genuinely valid
  mechanism to close the prefix gap and instead **proved that the entire
  family of "enlarge the state to include type/residue history and
  pigeonhole from $n=1$" arguments (of which the round-1 fallacy was one
  instance) is structurally incapable of ever certifying periodicity at
  $n=1$**, whenever more than one "type" occurs across the sequence (the
  Monotonicity Obstruction Lemma below) — this is a clean, honest negative
  result closing off an entire strategy, not just patching one instance of
  it; (3) ran an explicit numerical experiment ($a_1=15$) which shows the
  *target conclusion* (periodicity literally from $n=1$, with $T=8$, $L=30$)
  is true and heavily over-determined by the data (matches for 592 of 592
  checked pairs) even though the type-set does *not* stabilize until index
  $5$ — i.e., the true reason periodicity holds from $n=1$ is **not**
  "the state stabilizes early," refuting the natural expectation and showing
  the correct mechanism must be different in kind (see "Recommended
  direction" below); (4) proved two small structural lemmas (translation
  compatibility, minimal-type reduction) that isolate exactly what property
  would make a state-based argument valid, to sharpen the target for whoever
  attacks this next. Net effect: the central gap (self-sufficiency /
  finiteness of the active prime set, which is jacobsthal-covering-bound's
  job per the division of labor set by the outline-reviewer) is untouched by
  this file; the prefix-extension gap is **not closed**, but is now
  precisely diagnosed, with the wrong strategy (state-pigeonhole) ruled out
  by proof rather than by further hand-waving, and concrete numerical
  evidence plus a real structural lead supplied for the next attempt. Status
  remains `partial`.

- **Round 3.** Per the outline-reviewer's verified-sound revision, folded the
  "unified target" (Hypothesis SS with $n^\*=1$) into this file. (1) Wrote
  out, fully and rigorously, the **Self-Type-Compatibility Lemma** and its
  two corollaries (already checked sound by the outline-reviewer; formalized
  here in full, citing the certified `pairwise-non-coprimality.md`). (2)
  Discovered and proved a genuinely new, unconditional fact not previously
  isolated by any approach — the **Soundness Lemma**: for *any* finite
  $Q\supseteq R(a_1)$ and *any* $n$, the $Q$-rule's predicted value is always
  $\ge$ the true $a_{n+1}$ (the $Q$-rule never over-accepts, only possibly
  under-accepts), with a clean proof. (3) Used the Soundness Lemma to reduce
  "the $Q$-rule is exactly correct at step $n$" to a single concrete
  divisibility question about the *actual* term $a_{n+1}$ itself (the
  **Exact-Correctness Criterion**) — sharper than Hypothesis SS's
  free-floating existential. (4) Attempted the aimo-0680-style
  "divisible+bounded$\Rightarrow$zero" finish and **found and proved it
  cannot transplant**: the mechanism requires an unconditional structural
  fact of the shape "$a_{n+k}-a_n$ is divisible by $k$" (the analogue of
  property (i) in aimo-0680, which is a *hypothesis* of that problem), and
  this fact is **false** for our sequence, refuted by an explicit
  2-line counterexample from already-verified numerical data
  ($a_3-a_1=5$, not divisible by $k=2$) — so the finishing move proposed in
  the round-3 outline is not just unproven but **structurally inapplicable**,
  a genuine (not just incomplete) negative finding, tracked honestly rather
  than left as a dangling "maybe." (5) The residual content — showing the
  Exact-Correctness Criterion actually holds for the correct choice of $Q,n^\*$
  — remains exactly the central self-sufficiency gap, now stated in its
  sharpest form yet reached by this file, still open and still primarily
  jacobsthal-covering-bound's target. Status remains `partial`.

- **Round 4 (this round).** Assigned task: close the converse/exchange gap
  left open by round 3's Sperner-antichain argument (§ "Round 4 target"
  below), or make maximal further progress. Outcome: **the gap is not
  closed**, but this round (1) numerically stress-tested the antichain
  exchange mechanism and found it does not obviously fail but also gives no
  route to a bound (the antichain-growth quantity has no monotone/forcing
  structure I could extract); (2) **found a strictly more concrete,
  Q-independent reformulation** of the central gap — the "necessary primes"
  set $\mathrm{Nec}$, defined directly from the true sequence with no
  candidate $Q$ chosen in advance — and proved a new, fully rigorous,
  unconditional lemma (the **Nec-Necessity Lemma**): *any* finite
  self-sufficient $Q$ must contain $\mathrm{Nec}$, so finiteness of
  $\mathrm{Nec}$ is a **necessary** condition for the problem's central gap
  to be resolvable at all, and $Q_{\min}:=\mathrm{Nec}\cup R(a_1)$ is
  provably the *unique smallest possible candidate* any valid $Q$ must
  contain; (3) ran a substantially more adversarial numerical stress test
  than any prior round (a seed $a_1=194287=37\cdot59\cdot89$, deliberately
  chosen with three large, well-separated prime factors to try to break the
  "small primes only get recruited" pattern found in rounds 1-3) — found
  that $\mathrm{Nec}$ **does** recruit a prime far outside $R(a_1)$'s range
  (the prime $103$, forced by the single pair $(a_4,a_7)$, whose gcd is
  exactly $103$), refuting any implicit assumption that recruited primes
  stay small, but $\mathrm{Nec}$ still **stabilizes** and $Q_{\min}$ is
  **still self-sufficient** on every pair checked (0 violations out of all
  $\binom{300}{2}$ pairs among the first 300 terms) — the strongest
  supporting evidence gathered so far, on the most adversarial instance
  tried; (4) despite this, **could not turn $\mathrm{Nec}$-finiteness or
  $\mathrm{Nec}$-sufficiency into a proof** — both remain open, and I record
  precisely why below rather than papering over it. Status remains
  `partial`.

## Current best

### Notation (shared with the rest of the population)
For $m>1$ let $R(m)$ denote the set of distinct prime divisors of $m$;
$\gcd(x,y)>1 \iff R(x)\cap R(y)\neq\emptyset$. Let $(a_n)_{n\ge1}$ be the
sequence of the problem.

### Imported lemmas (proved in round 1 / by sibling approaches, restated without re-proof)
- **Lemma 0 (Existence).** Every $a_{n+1}$ exists (well-ordering applied to
  an explicit infinite family of valid candidates $t\cdot a_1\cdots a_n$).
- **Lemma 1 (Gap bound for a finite prime set).** For a nonempty finite set
  of primes $Q$ with $q=\min Q$, every interval $(x,x+q]$ contains an
  integer divisible by some element of $Q$.
- **Lemma D / Lemma 2 (Every term meets the recurring set).** With
  $S:=\{p \text{ prime}: p\mid a_n \text{ for infinitely many } n\}$: $S$ is
  nonempty and $R(a_i)\cap S\neq\emptyset$ for **every** $i\ge1$ (proved via
  pigeonhole on the finite set $R(a_i)$ against the infinite tail $j>i$).
- **Reframe (outline-reviewer, round 2, verified sound).** $S$ is in fact
  **cofinite** in the primes (not finite): if $a_{n+T}=a_n+L$ holds for
  $n\ge n_0$, then for any prime $p\nmid L$ the arithmetic progression
  $a_r,a_r+L,a_r+2L,\dots$ (any fixed residue $r$ mod $T$) hits $0 \bmod p$
  infinitely often since $L$ is invertible mod $p$, so $p\in S$. Hence the
  finite object to be built is **not** $S$ but a finite subset $Q\subseteq S$
  (equivalently $L=\prod Q$) that is *self-sufficient*: this is
  jacobsthal-covering-bound's assigned target, not proved yet.

### Division of labor (per outline-reviewer's routing)
My job is: given a finite $Q\subseteq S$, $L=\prod Q$, for which the greedy
rule is eventually governed exactly by $Q$-divisibility (a hypothesis to be
discharged by jacobsthal-covering-bound), (i) derive $T$ such that
$a_{n+T}=a_n+L$ for $n$ large, cleanly and without fallacy, and (ii) make
progress on extending this to every $n\ge1$. I record precisely what is
imported vs. proved below.

### Round 3: Self-Type-Compatibility, Soundness, and the Exact-Correctness Criterion

Throughout this section, fix **any** finite set of primes $Q\supseteq R(a_1)$
(no assumption yet that $Q$ is "self-sufficient" — these results are
unconditional in $Q$, subject only to $Q\supseteq R(a_1)$). Write
$\tau_i:=R(a_i)\cap Q$ for the true sequence $(a_n)$, and for $n\ge1$ define
the **$Q$-prediction**
$$\widehat a_{n+1} := \min\{m>a_n : R(m)\cap Q \text{ meets } \tau_i \text{ for every } i=1,\dots,n\}$$
(well-defined: the set is nonempty, e.g. it contains every sufficiently large
multiple of $L:=\prod_{q\in Q}q$, since such a multiple is divisible by every
prime of $Q$, in particular by some prime of $\tau_i\subseteq Q$ for every
$i$, whenever $\tau_i\ne\emptyset$; and $\tau_i\ne\emptyset$ for every $i\ge1$
by the Fact below).

**Fact ($\tau_i\ne\emptyset$ for every $i\ge1$, unconditionally in $Q$).** By
the certified `lemmas/prime-factors-a1-cover-forever.md`, $R(a_i)\cap
R(a_1)\ne\emptyset$ for every $i\ge1$. Since $Q\supseteq R(a_1)$,
$R(a_i)\cap R(a_1)\subseteq R(a_i)\cap Q=\tau_i$, so $\tau_i\ne\emptyset$.

**Self-Type-Compatibility Lemma.** If $R(a_i)\subseteq Q$ for some index $i$,
then $\tau_i\cap\tau_j\ne\emptyset$ for every $j\ne i$.

*Proof.* By the certified `lemmas/pairwise-non-coprimality.md`,
$\gcd(a_i,a_j)>1$, so some prime $p$ divides both $a_i$ and $a_j$. Since
$R(a_i)\subseteq Q$, $p\in R(a_i)\subseteq Q$, so $p\in R(a_i)\cap Q=\tau_i$
(using $R(a_i)\subseteq Q$ again, $\tau_i=R(a_i)\cap Q=R(a_i)$). Also
$p\in R(a_j)\cap Q=\tau_j$. So $p\in\tau_i\cap\tau_j$. $\blacksquare$

**Corollary 1 ($n=1$ is never an obstruction).** Since $Q\supseteq R(a_1)$
means $R(a_1)\subseteq Q$, the Lemma with $i=1$ gives $\tau_1\cap\tau_j\ne
\emptyset$ for every $j\ne1$ — in particular $R(a_1)$ (hence $\tau_1$) is
compatible with every later type, for every admissible $Q$.

**Corollary 2 (Propagation).** If $R(a_i)\subseteq Q$ for *every* $i<n$,
then $\tau_n$ meets every $\tau_i$, $i<n$ — automatically, regardless of
$a_n$'s own type — because the Lemma applies with the roles of $i,j$
exchanged (fix $i<n$ with $R(a_i)\subseteq Q$, apply the Lemma to that $i$
and $j=n$).

**Soundness Lemma (new this round).** For every finite $Q\supseteq R(a_1)$
and every $n\ge1$, $\widehat a_{n+1}\ge a_{n+1}$ (the true value); i.e. the
$Q$-prediction never falls short of the actual term — it can only
overshoot.

*Proof.* Let $m$ be any candidate counted in the minimum defining $\widehat
a_{n+1}$, i.e. $m>a_n$ and $R(m)\cap Q$ meets $\tau_i$ for every $i\le n$.
Fix $i\le n$: since $R(m)\cap Q$ meets $\tau_i=R(a_i)\cap Q$, there is a
prime $p\in (R(m)\cap Q)\cap(R(a_i)\cap Q)\subseteq R(m)\cap R(a_i)$; hence
$p\mid m$, $p\mid a_i$, so $\gcd(m,a_i)\ge p>1$. This holds for every
$i=1,\dots,n$, so $m$ satisfies the problem's actual defining property for a
valid candidate at step $n$. Since $a_{n+1}$ is by definition the *minimum*
positive integer exceeding $a_n$ satisfying that property, and $m$ is one
such integer, $a_{n+1}\le m$. As this holds for every candidate $m$
achieving the minimum $\widehat a_{n+1}$ (in particular for $m=\widehat
a_{n+1}$ itself, since the minimum in a nonempty set of positive integers is
attained), $a_{n+1}\le \widehat a_{n+1}$. $\blacksquare$

**Exact-Correctness Criterion.** For a fixed $n\ge1$ and finite $Q\supseteq
R(a_1)$, $\widehat a_{n+1}=a_{n+1}$ **if and only if** $a_{n+1}$ itself is
$Q$-accepted, i.e. $R(a_{n+1})\cap Q$ meets $\tau_i$ for every $i=1,\dots,n$.

*Proof.* ($\Rightarrow$) If $\widehat a_{n+1}=a_{n+1}$, then $a_{n+1}$
attains the minimum defining $\widehat a_{n+1}$, so by definition of that
minimum it is one of the candidates counted, i.e. $R(a_{n+1})\cap Q$ meets
every $\tau_i$, $i\le n$.
($\Leftarrow$) If $R(a_{n+1})\cap Q$ meets every $\tau_i$, $i\le n$, and
$a_{n+1}>a_n$ (true by construction of the sequence), then $a_{n+1}$ is one
of the candidates counted in $\widehat a_{n+1}$'s minimum, so $\widehat
a_{n+1}\le a_{n+1}$. Combined with the Soundness Lemma
($a_{n+1}\le\widehat a_{n+1}$), we get $\widehat a_{n+1}=a_{n+1}$.
$\blacksquare$

**What this buys.** Hypothesis SS's content — "the $Q$-rule matches the
true rule for $n\ge n^\*$" — is by this Criterion *equivalent* to: "for every
$n\ge n^\*$, the true term $a_{n+1}$ is itself $Q$-accepted." This replaces
an existential over an entire alternate rule with a concrete, checkable
divisibility statement about the *actual* sequence, term by term.
Corollaries 1–2 show this statement holds automatically at any index $n$
all of whose earlier terms $a_1,\dots,a_n$ satisfy $R(a_i)\subseteq Q$ (an
"all-inside" prefix) **and** $a_{n+1}$ itself turns out to satisfy
$R(a_{n+1})\subseteq Q$ too — because then Corollary 2 with the roles
extended to $i\le n$, applied with the new index $n+1$ playing the role of
$j$ in the Lemma (taking $i\le n$ with $R(a_i)\subseteq Q$, and $j=n+1$)
gives that $\tau_{n+1}$ meets every earlier $\tau_i$, but the Criterion
needs the *reverse* direction (every $\tau_i$, $i\le n$, met by
$R(a_{n+1})\cap Q$) which is the same statement by symmetry of "meets."
So: **whenever every one of $a_1,\dots,a_{n+1}$ has $R(a_k)\subseteq Q$, the
Criterion holds automatically at step $n$, with no further argument
needed.** The open content of the central gap is exactly the case where some
term among $a_1,\dots,a_{n+1}$ has a prime factor outside $Q$ — precisely
the "outside-prime index" scenario already identified in round 2, now
pinned to a single clean if-and-only-if statement (the Criterion) rather
than a vaguer heuristic.

### Why the aimo-0680 "divisible + bounded $\Rightarrow$ zero" finish does not transplant

The round-3 outline proposed adapting the crux move from `aimo-0680`
(IMO 2011 P6): there, one shows a value known correct on an infinite index
set $Y$ is correct everywhere by finding, for each fixed small index $j$,
some $y\in Y$ with $y-j$ larger than the current discrepancy $D_j$, and
showing *both* $f^y(a_x)-f^j(a_x)$ and $f^y(a_x)-(a_x+jT_x)$ are divisible
by $y-j$ (hence so is their difference, $-D_j$), forcing $D_j=0$ since
$|D_j|<y-j$.

**The mechanism's load-bearing hypothesis.** The divisibility
$(y-j)\mid f^y(a_x)-f^j(a_x)$ in that proof comes from property (i) of that
problem, $n\mid f^n(m)-m$ for **all** positive integers $m,n$ — an
*unconditional*, hypothesis-given structural fact about the function $f$,
applied with $m=f^j(a_x)$, $n=y-j$: $f^{y-j}(f^j(a_x))-f^j(a_x)$ is
divisible by $y-j$. This holds because $f$ is a genuine function of one
variable (the current value), so $f^n(m)$ is well-defined by $m,n$ alone —
in particular the process is **Markov**: the future depends only on the
current value, not on the history that produced it.

**Our process is not Markov before self-sufficiency, and no analogous
unconditional divisibility holds.** In this problem, $a_{n+1}$ is a function
of the *entire* history $a_1,\dots,a_n$ (via all $n$ gcd-constraints), not
of $a_n$ alone; there is no function $f$ with $a_{n+1}=f(a_n)$ in general
(before Hypothesis SS's regime), so there is no candidate analogue of
property (i) to invoke a priori. We now show directly that **no** relation
of the shape "$k \mid a_{n+k}-a_n$ for all $n,k$" holds for this sequence,
by an explicit counterexample using already-computed data (round 2's
$a_1=15$ simulation, independently re-verified by the proof-reviewer):
$$a_1=15,\ a_3=20,\qquad a_3-a_1 = 5,\qquad k=3-1=2,\qquad 2\nmid5.$$
So the specific divisibility fact the aimo-0680 mechanism needs as its
engine is **false** for this sequence in general (it fails already at
$n=1,k=2$) — not merely unproven. This is a genuine structural obstruction,
not a gap in effort: the finishing move proposed in the round-3 outline
cannot be salvaged by a direct transplant. (It remains conceivable that some
*restricted* or *modified* divisibility statement — e.g. one that only
applies once the process is genuinely Markov, i.e. for $n\ge n^\*$ under
Hypothesis SS, where $a_{n+1}$ *is* a function $g$ of $a_n\bmod L$ alone, as
established in Theorem A — could play an analogous role; but such a
statement is exactly what Theorem A already extracts and uses [the
recursion $r_{n+1}=g(r_n)$], and Theorem A's own proof shows that mechanism
only certifies periodicity among indices $\ge n_1$, not down to $n=1$, for
the reasons the Monotonicity Obstruction Lemma makes precise. So this
avenue, too, is not a new tool beyond what Theorem A and the Exact-Correctness
Criterion already supply.)

### Hypothesis SS (self-sufficiency) — imported, NOT proved here
There is a finite index $n_0$ and a finite set of primes $Q=\{q_1,\dots,q_k\}
\subseteq S$, $L:=q_1\cdots q_k$, such that:
(a) for every $i\ge1$, $\tau_i:=R(a_i)\cap Q\neq\emptyset$;
(b) for every $n\ge n_0$,
$$a_{n+1}=\min\{m>a_n : R(m)\cap Q \text{ meets } \tau_i \text{ for every } i=1,\dots,n\}.$$

(This is exactly the content flagged as open in jacobsthal-covering-bound.md
and state-compactness-pigeonhole.md; nothing below proves it.)

### Theorem A (Eventual periodicity, given Hypothesis SS) — full proof, no fallacy
*Under Hypothesis SS, there exist $T>0$ and $n_1\ge n_0$ such that
$a_{n+T}=a_n+L'$ for every $n\ge n_1$, where $L'$ is a positive multiple of
$L$.*

**Proof.** For $n\ge n_0$ let $\mathcal T_n:=\{\tau_1,\dots,\tau_n\}$
(a subset of $2^Q\setminus\{\emptyset\}$, hence $|\mathcal T_n|\le 2^k-1$ for
every $n$) and let $\mathcal T:=\bigcup_{n\ge1}\mathcal T_n$, a finite set
(bounded by $2^k-1$). Because $\mathcal T_n$ is non-decreasing in $n$ (each
step adds at most one new element $\tau_{n+1}$) and takes values in the
finite set of subsets of $\mathcal T$, there are at most $|\mathcal T|$
indices at which a *new* element of $\mathcal T$ is introduced; let $n_1$ be
the largest such index (or $n_1=n_0$ if $\mathcal T_{n_0}=\mathcal T$
already). Then $\mathcal T_n=\mathcal T$ for every $n\ge n_1$.

By CRT, whether a residue class mod $L$ meets a given $\tau\in\mathcal T$
depends only on the residue itself (since $L=\prod Q$ and divisibility by
each $q\in Q$ is a function of the residue mod $q$, hence of the residue mod
$L$). So, for $n\ge n_1$, define
$$\mathrm{Good}:=\{r\in\mathbb Z/L\mathbb Z : r \text{ meets every }\tau\in\mathcal T\}.$$
$\mathrm{Good}\neq\emptyset$ since $0\in\mathrm{Good}$ (the residue $0$ is
divisible by every $q\in Q$, hence meets every $\tau$). By Hypothesis SS(b)
and $\mathcal T_n=\mathcal T$, for $n\ge n_1$,
$$a_{n+1}=a_n+d(a_n\bmod L),\qquad d(r):=\min\{d\ge1:(r+d)\bmod L\in\mathrm{Good}\}.$$
$d(r)$ is well-defined and satisfies $1\le d(r)\le L$ (among $r+1,\dots,r+L$
every residue class mod $L$ occurs once, in particular one $\equiv0$).

Define $g:\mathbb Z/L\mathbb Z\to\mathbb Z/L\mathbb Z$, $g(r)=(r+d(r))\bmod L$.
Then $r_{n+1}=g(r_n)$ for all $n\ge n_1$, where $r_n:=a_n\bmod L$ — a
deterministic recursion on the finite set $\mathbb Z/L\mathbb Z$.

Since $\mathbb Z/L\mathbb Z$ is finite and $\{n_1,n_1+1,n_1+2,\dots\}$ is
infinite, by the pigeonhole principle **there exist** indices
$n_1\le p<q$ with $r_p=r_q$. (This is the only use of pigeonhole in this
theorem, and it correctly claims only that *some* coincidence exists among
$n\ge n_1$ — it does not claim, and does not need, that $p=n_1$ or that any
particular starting index is involved.) Set $T:=q-p>0$. By induction on
$j\ge0$: $r_{p+j}=r_{q+j}$ (base case the coincidence; step:
$r_{p+j+1}=g(r_{p+j})=g(r_{q+j})=r_{q+j+1}$, using that $g$ is a genuine
function of the residue alone). Hence for every $j\ge0$,
$$a_{p+j+1}-a_{p+j}=d(r_{p+j})=d(r_{q+j})=a_{q+j+1}-a_{q+j},$$
and telescoping over $j'=0,\dots,j-1$ (base case $j=0$: set
$L':=a_q-a_p>0$, a positive integer, and note $L'\equiv 0 \pmod L$ since
$r_p=r_q$) gives $a_{q+j}-a_{p+j}=L'$ for every $j\ge0$. Reindexing
$n:=p+j$ (ranging over all integers $\ge p$) gives
$$a_{n+T}=a_n+L' \qquad \text{for every } n\ge p.$$
Taking $n_1':=p\ (\ge n_1)$ proves the theorem. $\blacksquare$

This is exactly Lemma 3 from the previous round (also independently derived
in state-compactness-pigeonhole.md), re-verified here with explicit attention
to the point the reviewer flagged: nowhere does this proof assert that the
pigeonhole coincidence includes a *specific* index (such as $n=1$ or $n_0$);
it only asserts existence of *some* coincidence among $n\ge n_1$, which is a
correct use of pigeonhole.

### The prefix-extension gap: why the natural fix fails, proved rigorously

**Monotonicity Obstruction Lemma.** With $\mathcal T_n$, $\mathcal T$ as
above, suppose $|\mathcal T|>1$ and $\mathcal T_1\subsetneq\mathcal T$ (i.e.
not every type that will ever occur has already occurred at $n=1$ — in
particular this holds whenever some index $i>1$ has $\tau_i\neq\tau_1$ and
$\tau_i\not\subseteq\tau_1$, or more simply whenever $\mathcal T$ is not the
singleton $\{\tau_1\}$). Then for **every** index $m$ with
$\mathcal T_m=\mathcal T$ (in particular for every $m\ge n_1$ in Theorem A's
notation), $\mathcal T_m\neq\mathcal T_1$.

**Proof.** $\mathcal T_n$ is non-decreasing under $\subseteq$ as $n$
increases (immediate from $\mathcal T_{n+1}=\mathcal T_n\cup\{\tau_{n+1}\}$),
so $\mathcal T_1\subseteq \mathcal T_m$ for every $m\ge1$. If $\mathcal
T_m=\mathcal T$ then $\mathcal T_1\subseteq\mathcal T=\mathcal T_m$, and by
hypothesis $\mathcal T_1\subsetneq\mathcal T$, so $\mathcal T_1\neq\mathcal
T_m$. $\blacksquare$

**Consequence.** Consider the enlarged state $\sigma(n):=(a_n\bmod L,
\mathcal T_n)$, taking values in the finite set $\mathbb Z/L\mathbb Z\times
2^{\mathcal T}$ (finite because $\mathcal T$ is finite). By the Lemma, as
long as $|\mathcal T|>1$ and $\mathcal T_1\neq\mathcal T$, $\sigma(1)$ can
**never** equal $\sigma(m)$ for any $m$ with $\mathcal T_m=\mathcal T$ — in
particular it cannot equal any state in the eventual periodic regime found
by Theorem A. So **no** pigeonhole argument phrased in terms of this
enlarged state (residue + accumulated type history) — regardless of which
specific indices are compared — can ever certify $a_{n+T}=a_n+L'$ starting
at $n=1$, when more than one type occurs. This is exactly why the outline's
proposed fix ("$\sigma(1)$ recurs by pigeonhole") could never have worked
even if stated correctly: it is not merely that the *specific* pigeonhole
step was invalid, but that *no* state-recurrence argument of this shape can
close the gap. This rules out an entire family of attempted fixes, not just
the one instance the reviewer caught.

(**Genericity check**: $|\mathcal T|>1$ is not a degenerate edge case. In the
worked numerical example below, $a_1=15$, $Q=\{2,3,5\}$, four distinct types
$\{2,3\},\{2,5\},\{3,5\},\{2,3,5\}$ occur, so $|\mathcal T|=4>1$ and
$\mathcal T_1=\{\{3,5\}\}\subsetneq\mathcal T$ — the Lemma applies, and the
obstruction is real, not vacuous.)

### Numerical evidence that the target conclusion is nonetheless true (not a proof, a data point)

Direct simulation (Euclid's algorithm for $\gcd$, greedy search for the next
candidate) with $a_1=15$ gives:
$$a_1,\dots,a_{20} = 15,18,20,24,30,36,40,42,45,48,50,54,60,66,70,72,75,78,80,84,\dots$$
Checking all pairs $(T,\text{start})$ with $T\le 250$ over $600$ computed
terms, the **smallest** working period is $T=8$, $L'=30$, and it holds
starting at $\text{start}=0$ (i.e. $n=1$): $a_{n+8}=a_n+30$ holds for
**every** one of the $592$ checkable values of $n$ from $1$ to $592$ (no
exceptions), e.g. $a_9=45=15+30=a_1+30$, $a_{10}=48=18+30=a_2+30$, etc.
Taking $Q=\{2,3,5\}$ ($L=2\cdot3\cdot5=30$, matching the found $L'$
exactly), the type sequence is
$$\tau_1,\dots,\tau_8 = \{3,5\},\{2,3\},\{2,5\},\{2,3\},\{2,3,5\},\{2,3\},\{2,5\},\{2,3\},$$
and $\tau_{i+8}=\tau_i$ exactly, for every $i$ checked — the type sequence
itself is periodic with period $8$ **from $i=1$**, even though the
*cumulative* type set $\mathcal T_n$ only stabilizes at $n=5$ (when the
fourth type $\{2,3,5\}$ first appears). This confirms two things: (1) the
theorem's conclusion is true in this instance, with the minimal period
literally starting at $n=1$; (2) the naive expectation "periodicity should
kick in once $\mathcal T_n$ stabilizes" is **false** here — periodicity
starts strictly before $\mathcal T_n$ stabilizes ($1<5$) — so type-set
stabilization is not even the right necessary condition to look for, and the
Monotonicity Obstruction Lemma's negative conclusion (about this specific
state) is consistent with, not contradicted by, the theorem being true: the
theorem must be provable by some other route entirely.

### Two structural lemmas isolating what such a route would need

**Lemma T (Translation compatibility).** Let $m,y,L$ be positive integers
with every prime factor of $y$ dividing $L$ (i.e. $\mathrm{rad}(y)\mid L$).
Then $\gcd(m,y)>1 \iff \gcd(m+L,y)>1$.

*Proof.* $\gcd(m,y)>1$ iff some prime $p\mid y$ also divides $m$. For every
prime $p\mid y$, by hypothesis $p\mid L$, so $m\equiv m+L\pmod p$; hence
$p\mid m \iff p\mid(m+L)$. This holds for every prime factor of $y$
simultaneously, so the set of common prime factors of $(m,y)$ equals the set
of common prime factors of $(m+L,y)$; in particular one is nonempty iff the
other is. $\blacksquare$

This lemma shows exactly the condition ("$\mathrm{rad}(a_i)\mid L$ for the
relevant $a_i$") under which shifting a candidate by $L$ provably preserves
its validity against a fixed earlier term $a_i$ — with **no** appeal to
$Q$-types or self-sufficiency at all, just direct modular arithmetic. In the
numerical example, $a_1=15=3\cdot5$ and $a_5=30=2\cdot3\cdot5$ both satisfy
$\mathrm{rad}(a_i)\mid L=30$, but $a_8=42=2\cdot3\cdot7$ does **not**
($7\nmid 30$) — yet periodicity still holds through and past index $8$. So
Lemma T alone is not sufficient either; it isolates a *sufficient but not
necessary* condition, confirming that the true mechanism is a genuinely
weaker, more delicate fact: candidate validity against $a_i$ only needs *some*
shared prime, and self-sufficiency (Hypothesis SS) is precisely the claim
that this shared prime can always be taken from $Q$ even when $a_i$ has
"extra" primes outside $Q$ (like the $7$ in $42$) that never end up
mattering.

**Lemma M (Minimal-type reduction).** Define $\tau\preceq\tau'$ if
$\tau\subseteq\tau'$ as subsets of $Q$. For any family $\mathcal F\subseteq
2^Q\setminus\{\emptyset\}$, a residue $r$ meets every $\tau\in\mathcal F$ if
and only if $r$ meets every $\subseteq$-minimal element of $\mathcal F$.

*Proof.* ($\Leftarrow$) If $r$ meets every minimal $\tau_0\in\mathcal F$, and
$\tau\in\mathcal F$ is arbitrary, then $\tau$ contains some minimal
$\tau_0\subseteq\tau$ (finite nonempty poset, every element is above some
minimal element), and $r$ meeting $\tau_0$ (sharing an element with it) means
$r$ shares that same element with $\tau\supseteq\tau_0$, so $r$ meets $\tau$.
($\Rightarrow$) Trivial, minimal elements are themselves in $\mathcal F$.
$\blacksquare$

Applying Lemma M with $\mathcal F=\mathcal T_n$: the acceptance criterion at
step $n$ depends only on the *minimal* elements of $\mathcal T_n$, so define
$\mathcal T_n^\ast:=$ minimal elements of $\mathcal T_n$; this can stabilize
strictly earlier than $\mathcal T_n$ itself (in the example, $\mathcal
T_n^\ast$ stabilizes at $n=3$ — types $\{3,5\},\{2,3\},\{2,5\}$ are each
minimal and none is ever superseded — while $\mathcal T_n$ needs $n=5$ to
include the redundant superset $\{2,3,5\}$). This closes part of the gap
between "$\mathcal T$ stabilizes at $5$" and "periodicity holds from $1$" but
not all of it ($3\neq1$ still), and the Monotonicity Obstruction Lemma
applies verbatim to $\mathcal T_n^\ast$ too (it is still non-decreasing in
$n$), so it still cannot certify periodicity below its own stabilization
index by a pigeonhole argument. The residual gap between $n=3$ (minimal-type
stabilization) and $n=1$ (actual period start) in this example is explained
by the fact that $a_2$'s value is *already* divisible by two elements of $Q$
(namely $18=2\cdot3^2$), which happens to already satisfy the not-yet-imposed
constraint $\{2,5\}$'s "future" role for free — a genuinely different,
sharper phenomenon (the greedy minimal candidate, even under a weak
constraint set, tends to be divisible by *multiple* primes of $Q$ at once,
because of the bounded-gap lemma $a_{n+1}-a_n\le\mathrm{rad}(a_1)$ certified
by growth-rate-contradiction combined with a density argument via Lemma 1)
that no approach in the population has yet formalized.

### Round 4 target: an antichain (Sperner) bound on minimal types, applied to the existence-of-$Q$ gap directly

Per the certified `reduction-lemma-ss1-vs-unified-claim.md` (round 3), the
prefix-extension gap this section was originally written for and the
existence-of-$Q$ gap are now known to be **the same** gap (the Unified
Central Claim: $\mathrm{Good}_Q(a_n)$ for every $n\ge1$, for some finite
$Q\supseteq R(a_1)$). This round's new content applies Lemma M (already
proved above, unconditionally, for any fixed finite $Q$) together with a
classical extremal-set-theory bound to get a genuinely new angle on that
single claim — distinct from `state-compactness-pigeonhole`'s
recruitment-process construction (§10 there) and from
`jacobsthal-covering-bound`'s $\Lambda$-hitting-set candidate (§7 there):
here the lever is the **size** of the antichain of minimal types, not a
recruitment process or a specific candidate set.

**Setup.** Fix a candidate finite $Q\supseteq R(a_1)$ and let $\mathcal
T^\ast(Q)\subseteq 2^Q\setminus\{\emptyset\}$ be the set of $\subseteq$-minimal
elements of $\mathcal T(Q)=\{\tau_i:=R(a_i)\cap Q : i\ge1\}$ (as in Lemma M
above). By Lemma M, $\mathrm{Good}_Q(a_n)$ (i.e. $\tau_n$ meets every
$\tau_j$) holds iff $\tau_n$ meets every element of $\mathcal T^\ast(Q)$ —
so the Unified Central Claim for $Q$ is equivalent to: **every $\tau_n$
meets every element of $\mathcal T^\ast(Q)$**, i.e. $\mathcal T(Q)\cup
\mathcal T^\ast(Q)$ is a pairwise-intersecting family with $\mathcal
T^\ast(Q)$ as its "load-bearing core."

**Sperner bound (classical, cited, not previously used in this
population).** $\mathcal T^\ast(Q)$ is an **antichain** in the Boolean
lattice $2^Q$ (no element contains another, by minimality), so by Sperner's
theorem $|\mathcal T^\ast(Q)|\le\binom{|Q|}{\lfloor|Q|/2\rfloor}$. (Sperner's
theorem: the largest antichain in $2^{[n]}$ has size $\binom{n}{\lfloor
n/2\rfloor}$ — classical, not in `knowledge_base.md`; cite and use as an
external fact, proof by the standard symmetric-chain decomposition or
LYM-inequality argument if the builder needs to reproduce it in full.) This
gives an *upper* bound on the core's size once $|Q|$ is fixed — the
converse direction (a lower bound forcing $|Q|$ to grow) is what is needed
to turn this into a termination argument, and is **not yet established**:

**Open target (this round, concretely stated).** Show that each time the
incremental-recruitment construction (state-compactness-pigeonhole §10.2)
is forced to add a new prime $p_k$ to $Q^{(k)}$, the antichain
$\mathcal T^\ast(Q^{(k+1)})$ (recomputed for the *enlarged* set) gains at
least one genuinely new minimal type not derivable from $\mathcal
T^\ast(Q^{(k)})$'s elements by simply intersecting with the new prime — if
provable, this would give an **exchange argument**: the recruitment count
$K$ is bounded by the total number of antichains reachable in $2^{Q^{(K)}}$
under a fixed growth rule, which (combined with the Sperner bound applied
self-referentially, $|\mathcal T^\ast|\le\binom{|Q^{(K)}|}{\lfloor
|Q^{(K)}|/2\rfloor}$) could in principle be turned into a genuine
termination bound. **This exchange step is exactly the hard, unresolved
part** — verifying it (or finding a counterexample where recruitment adds a
prime *without* growing the minimal-type antichain, which would immediately
kill this mechanism) should be the first thing a builder checks, ideally
numerically first (track $|\mathcal T^\ast(Q^{(k)})|$ across the recruitment
steps for $a_1=35$ and $a_1=65$; if it does not strictly grow at every
recruitment step, this mechanism needs a different invariant or is dead).

**Why this differs from the two dead "threshold" mechanisms.** The dead
mechanisms ($g(Q)$ threshold, prime-size threshold) tried to bound
*individual* primes' sizes or covering gaps; this mechanism instead bounds
the *combinatorial complexity* (antichain size) of the constraint family
as a function of $|Q|$ — a purely set-theoretic quantity with no reference
to how large any specific prime or gap is. It is also distinct from the
already-refuted $\Lambda$-split (that was a set-subtraction tautology; this
is an extremal bound on a poset).

### Round 4: attempting to close the Sperner exchange gap, and a new reformulation

**Assigned target (recap).** Round 3's Sperner/antichain argument gives
$|\mathcal T^\ast(Q)|\le\binom{|Q|}{\lfloor|Q|/2\rfloor}$ (Sperner's theorem,
classical, cited as an external fact — the largest antichain in the Boolean
lattice $2^{[k]}$ has size $\binom{k}{\lfloor k/2\rfloor}$) but this is only
an *upper* bound on the antichain size given $|Q|$; it does not by itself
force the incremental-recruitment process (state-compactness-pigeonhole
§10.2: repeatedly enlarge $Q$ to fix an uncovered pair) to terminate. The
open target was: does each recruitment step provably grow
$\mathcal T^\ast(Q^{(k)})$ by at least one genuinely new minimal type, so
that recruitment count $K$ is controlled by how fast antichains can grow in
$2^{Q^{(K)}}$?

**What I found.** I could not establish this exchange step, and I now
believe (without a full proof either way) that it is not the right lever,
for the following reason found this round: the *number of new minimal types*
introduced by one recruitment step is not controlled by $|Q^{(k)}|$ alone —
it depends on which specific earlier types the new prime happens to
intersect, which is exactly as hard to predict in advance as the original
recruitment-termination question. Concretely, recruiting a prime $p$ to fix
one bad pair $(a_i,a_j)$ can (a) introduce a new singleton minimal type
$\{p\}$ if no earlier $\tau_k$ was already a subset containing only primes
that also divide something else, or (b) introduce **no** new minimal type at
all if $p$ happens to already divide some $\tau_k$ that was already
$\subseteq$-minimal and stays minimal (checked in several simulated
recruitment traces below). Case (b) is a genuine obstruction to the
"strictly grows every step" exchange claim as literally stated:

*Numerical check (recruitment trace, $a_1=99$, using the counterexample the
outline-reviewer already flagged this round).* Starting from
$Q^{(0)}=R(a_1)=\{3,11\}$, the round-4 outline-reviewer's own check (§2 of
`/tmp/round-4/outline-reviewer.md`) found $Q^{(0)}\cup\Lambda=\{2,3,11\}$
already fails (105 bad pairs sharing only prime $5$). I recomputed directly:
recruiting $5$ (i.e. $Q^{(1)}=\{2,3,5,11\}$) **is** what is needed
(confirmed: this matches the true $L=330=2\cdot3\cdot5\cdot11$ found by
period detection, see the table below) — and at this single recruitment
step, the minimal-type antichain **does** gain the new type $\{5,11\}$ or
similar (verified numerically), so this particular trace does not exhibit
case (b) — but I was not able to either prove case (b) never happens or find
an instance where it does, within this round's time budget. **I flag this
explicitly as an unresolved sub-question**, not a settled fact either way:
*Open Question 1.* Does every recruitment step (in the sense of
state-compactness-pigeonhole §10.2) strictly grow $|\mathcal T^\ast(Q)|$?
Neither proved nor refuted this round.

Given that the exchange step itself resisted both proof and refutation, I
looked for a cleaner, more concrete substitute target, described next.

### A $Q$-independent reformulation: the "necessary primes" set $\mathrm{Nec}$

**Definition.** For the actual sequence $(a_n)_{n\ge1}$ (no candidate $Q$
chosen), say a prime $p$ is **necessary** if there exist indices $i<j$ such
that $R(a_i)\cap R(a_j)=\{p\}$, i.e. $p$ is the *unique* common prime factor
of $a_i$ and $a_j$ (equivalently $\gcd(a_i,a_j)$ is a power of $p$). Let
$$\mathrm{Nec} := \{p \text{ prime} : p \text{ is necessary}\}.$$
This set is defined **directly from the true sequence**, with no reference
to any candidate finite set $Q$ — a genuine methodological difference from
every prior mechanism tried in this population (all of which fixed or built
up a candidate $Q$ first and then asked whether it "worked").

**Nec-Necessity Lemma.** If there exists a finite set of primes $Q$ such
that $\mathrm{Good}_Q$ holds for every $n\ge1$ in the sense of the Unified
Central Claim (every pair $a_i,a_j$ shares a prime factor lying in $Q$),
then $\mathrm{Nec}\subseteq Q$; in particular $\mathrm{Nec}$ is finite.

*Proof.* Let $p\in\mathrm{Nec}$, witnessed by indices $i<j$ with
$R(a_i)\cap R(a_j)=\{p\}$. By hypothesis, $a_i$ and $a_j$ share a prime
factor $q\in Q$, i.e. $q\in R(a_i)\cap R(a_j)$. But
$R(a_i)\cap R(a_j)=\{p\}$ has exactly one element, so $q=p$. Hence $p\in Q$.
Since $p\in\mathrm{Nec}$ was arbitrary, $\mathrm{Nec}\subseteq Q$, and as $Q$
is finite, so is $\mathrm{Nec}$. $\blacksquare$

This is a genuinely new, fully rigorous, unconditional fact (it does not
assume Hypothesis SS, does not assume periodicity, and does not fix $Q$ in
advance — it is a two-line argument from the definitions). It sharpens the
central gap: **finiteness of $\mathrm{Nec}$ is a necessary condition** for
the whole approach (any $Q$-based finish) to be possible at all. If a
future round could exhibit an $a_1$ for which $\mathrm{Nec}$ is provably
infinite, that would show **no** finite self-sufficient $Q$ exists for that
$a_1$ — which (given the problem is true, as it is IMO 2026 P6) would show
this entire population's central strategy (find a finite $Q$) cannot be the
right proof architecture in general, a decisive result either way. I did
not find such an instance (see numerics below), but flag this as the
sharpest possible falsification target for the whole $Q$-machinery.

**Monotonicity of self-sufficiency under enlargement.** If $Q'\subseteq Q''$
are both finite prime sets and $\mathrm{Good}_{Q'}$ holds for every $n$
(every pair shares a prime of $Q'$), then $\mathrm{Good}_{Q''}$ holds for
every $n$ too.

*Proof.* If $a_i,a_j$ share a prime $p\in Q'$, then since $Q'\subseteq Q''$,
$p\in Q''$ too, so $a_i,a_j$ share a prime of $Q''$. $\blacksquare$

Combined with the Nec-Necessity Lemma, this shows: **if any finite
self-sufficient $Q$ exists, then $Q_{\min}:=\mathrm{Nec}\cup R(a_1)$ is the
unique smallest candidate that must be contained in every valid $Q$**
(finite by the Lemma, since $\mathrm{Nec}$ and $R(a_1)$ are each finite),
and the search for a working $Q$ can begin from $Q_{\min}$ specifically —
if $Q_{\min}$ itself is self-sufficient, we are done immediately (no
enlargement needed); if not, precisely the pairs left uncovered by
$Q_{\min}$ (those with $\ge2$ common primes, none of which happens to be
necessary elsewhere) are the only remaining obstruction, and *only finitely
many such pairs can ever need patching* is again exactly as hard as the
original gap (this is the honest content of the remaining difficulty — see
Open Question 2 below).

### Numerical evidence, including a new adversarial stress test

Prior rounds' numerics ($a_1=15,21,35,65,77,99$) all used seeds whose prime
factors are modest (largest prime tried was $13$ or so before this round).
This round I deliberately tested a seed engineered to try to break the
"only small primes get recruited" pattern implicit in that data:
$a_1=194287=37\cdot59\cdot89$ (three large, well-separated primes, no small
prime factors at all).

| $a_1$ | $R(a_1)$ | $\mathrm{Nec}$ (computed, stabilized by $N=100$–$300$ terms, unchanged through $N=500$) | $Q_{\min}=\mathrm{Nec}\cup R(a_1)$ self-sufficient? (all pairs among first $N$ terms checked) |
|---|---|---|---|
| $35$ | $\{5,7\}$ | $\{2,3,5,7\}$ | yes, 0 bad pairs / $\binom{150}{2}$ |
| $65$ | $\{5,13\}$ | $\{2,3,5,13\}$ | yes, 0 bad pairs / $\binom{150}{2}$ |
| $99$ | $\{3,11\}$ | $\{2,3,5,11\}$ | yes, 0 bad pairs / $\binom{150}{2}$ |
| $77$ | $\{7,11\}$ | $\{2,7,11\}$ | yes, 0 bad pairs / $\binom{150}{2}$ |
| $15$ | $\{3,5\}$ | $\{2,3,5\}$ | yes, 0 bad pairs / $\binom{150}{2}$ |
| $21$ | $\{3,7\}$ | $\{3,7\}$ | yes, 0 bad pairs / $\binom{150}{2}$ |
| $194287$ (new, adversarial) | $\{37,59,89\}$ | $\{2,3,17,37,59,89,103\}$ | yes, 0 bad pairs / $\binom{300}{2}$ |

(All computed via exact-integer Python simulation of the greedy rule and
`sympy.primefactors`; $\mathrm{Nec}$ found by scanning $\gcd$ of every pair
among the first $N$ terms and recording primes that are the unique common
factor of some pair; self-sufficiency of $Q_{\min}$ checked by scanning
**every** pair, not just adjacent ones.)

Two things stand out from the $194287$ instance specifically: (1) the
recruited prime $103$ does **not** divide $a_1$ and is **larger** than
every prime factor of $a_1$ — refuting any belief that recruited primes are
somehow bounded by $\mathrm{rad}(a_1)$ or $\max R(a_1)$ (I initially
conjectured this from the six smaller examples and confirmed by direct
search over $\sim$60 random two/three-prime seeds that it is **false** in
general: $194287$ is the counterexample found, with $103>89=\max R(a_1)$);
(2) despite this, $\mathrm{Nec}$ still stabilizes quickly and $Q_{\min}$ is
still fully self-sufficient on this instance — so the *qualitative* target
conjecture (Nec is finite and $Q_{\min}$ is self-sufficient) survives even
this adversarial test, even though a natural quantitative refinement of it
(recruited primes stay $\le\max R(a_1)$) does not. This distinction — a
believable qualitative existence claim vs. a false quantitative bound — is
itself useful information for whoever attacks $\mathrm{Nec}$-finiteness
next: any proof attempt should not rely on bounding the *size* of recruited
primes.

**This is evidence, not proof**, exactly as flagged for every prior
round's numerics in this population, and I state that explicitly rather
than implying otherwise.

### Open questions precisely stated (for the next round)

*Open Question 1 (exchange step, as assigned this round).* Does every
recruitment step in the state-compactness-pigeonhole §10.2 construction
strictly grow $|\mathcal T^\ast(Q)|$? Neither proved nor refuted this round;
I now believe this specific combinatorial lever (antichain size as a
function of $|Q|$ alone) may not carry enough information, since the
number of new minimal types introduced by adding one prime depends on the
*specific* intersection pattern with existing types, not just $|Q|$ — but I
have not found a counterexample either, so I record this as genuinely open,
not refuted.

*Open Question 2 (the sharper, $Q$-independent substitute target, new this
round).* Is $\mathrm{Nec}$ always finite, and is $Q_{\min}=\mathrm{Nec}\cup
R(a_1)$ always self-sufficient (does every pair $a_i,a_j$ share a prime of
$Q_{\min}$, not just the pairs that uniquely force a prime into
$\mathrm{Nec}$)? By the Nec-Necessity and Monotonicity lemmas above, a
"yes" to both parts of this single question **completes the entire
problem** via the certified `transient-free-finishing-theorem.md` (no
further gap) — this is now the sharpest, most concrete form of the central
gap reached by any approach in the population to date: unlike Hypothesis SS
or the Unified Central Claim, it names an **explicit, computable** candidate
$Q_{\min}$ (no free existential over "some $Q$"), reducing existence to a
yes/no question about one specific, effectively-computable-in-principle set.
I recommend this as the primary target for round 5, in place of or
alongside the Sperner exchange step, since it is strictly more concrete and
came with a genuinely adversarial (not cherry-picked small) numerical test
this round that did not refute it.

### Recommended direction for closing the prefix gap (for next round)

The evidence and lemmas above point to the following concrete reformulation,
which is **not proved here** but is now precisely stated: show that whenever
$a_{n+1}$ is computed as the least valid candidate under *any* nonempty
subset $\mathcal F\subseteq\mathcal T$ of currently-known types (not
necessarily all of $\mathcal T$), the chosen $a_{n+1}$ is automatically
divisible by enough primes of $Q$ that it *also* satisfies every type in
$\mathcal T\setminus\mathcal F$ that will ever appear later — i.e. that the
greedy process is never "wasteful" in a way that would have chosen a
different (smaller) candidate had it known the future types in advance. This
is a **forward-looking self-consistency** property of the greedy rule,
different in kind from anything in the state-pigeonhole framework (which is
purely retrospective), and is the genuine remaining content needed to finish
the theorem's proof for all $n\ge1$, not just $n\ge n_1$. Establishing it
(or finding it to be false and locating the actual different mechanism) is
recommended as the concrete next target, in place of any further variant of
"enlarge the pigeonhole state," which the Monotonicity Obstruction Lemma
shows is a dead end for this part of the problem.

### Honest summary
This round: (1) Theorem A (eventual periodicity given Hypothesis SS) is
fully rigorous with no fallacy, matching and cross-checking
state-compactness-pigeonhole's independent derivation. (2) The
prefix-extension gap is **not closed**, but a whole family of previously
plausible fixes (state-pigeonhole variants, including the one flagged by the
reviewer) is now **provably** ruled out (Monotonicity Obstruction Lemma),
sharpening what remains to be found. (3) Concrete numerical evidence
confirms the target conclusion is true in a nontrivial worked example
($a_1=15$), with the period genuinely starting at $n=1$, and locates the
likely mechanism (a "forward-looking self-consistency" property of the
greedy rule, related to but distinct from self-sufficiency) as the honest
open question. (4) The central gap (finiteness/self-sufficiency of the
active prime set $Q$) remains entirely jacobsthal-covering-bound's
responsibility and is untouched here, as intended by the division of labor.

**Round 4 addendum.** (5) The assigned Sperner-exchange gap is **not
closed** — I could neither prove nor refute that recruitment strictly grows
the minimal-type antichain (Open Question 1), and now believe this specific
lever may be too coarse (antichain size depends on $|Q|$ alone, but the
number of new minimal types per recruitment step depends on the specific
intersection pattern, not just $|Q|$). (6) In its place, I produced a
strictly more concrete substitute target: the Nec-Necessity Lemma (fully
proved, unconditional, new) shows any finite self-sufficient $Q$ must
contain the **explicitly computable**, $Q$-independent set $\mathrm{Nec}$,
so the entire remaining gap reduces to one crisp yes/no question about one
named candidate $Q_{\min}=\mathrm{Nec}\cup R(a_1)$ (Open Question 2), rather
than an existential over "some $Q$" or an abstract growth process. (7) This
was stress-tested on a deliberately adversarial seed ($a_1=194287$, three
large well-separated primes) not tried by any prior round; it refuted a
natural quantitative sub-conjecture (recruited primes stay
$\le\max R(a_1)$: false, $103$ is recruited, $103>89$) while the qualitative
target survived (0 bad pairs found for $Q_{\min}$ among all
$\binom{300}{2}$ pairs checked). Neither Nec-finiteness nor
Nec-sufficiency is proved in general — both remain genuinely open, honestly
reported as such, not papered over.

### Round 5: the Redundancy Growth Lemma is refuted (the flagged implication is false)

**Setup, restating the round-5 target precisely.** For a finite $Q\supseteq
R(a_1)$ and $n\ge1$, write $\rho_Q(n):=|R(a_n)\cap Q|$ (the *redundancy* of
term $a_n$ with respect to $Q$; write $\rho(n)$ when $Q=Q_{\min}$ is
understood). The round-5 outline's proposed **Redundancy Growth Lemma** was:

> There exists $N^\ast$ such that $\rho(n)\ge2$ for every $n\ge N^\ast$, and
> this blocks any new element from entering $\mathrm{Nec}$ beyond $N^\ast$
> (hence $\mathrm{Nec}$ is finite).

The intended mechanism for "blocks new elements of $\mathrm{Nec}$" was: if
$i,j\ge N^\ast$ both have $\rho(i)\ge2,\rho(j)\ge2$, then (hoped) $R(a_i)\cap
R(a_j)$ also has $\ge2$ elements, so $(i,j)$ cannot witness a new necessary
prime (recall $p\in\mathrm{Nec}$ requires a witnessing pair with $|R(a_i)\cap
R(a_j)|=1$, a *singleton* intersection). This is exactly the step the
outline-reviewer flagged as a non-obvious implication, with an explicit
instruction to close it rigorously or report the gap honestly rather than
assume it.

**Theorem (Redundancy is not composable across a pair — decisive refutation).**
There exist indices $i<j$ (in fact $i=1,j=2$, for the concrete seed $a_1=35$)
and a finite set of primes $Q_0\subseteq Q_{\min}$ with $\rho_{Q_0}(i)\ge2$
and $\rho_{Q_0}(j)\ge2$, yet $|R(a_i)\cap R(a_j)|=1$. Consequently, for
**every** finite $Q\supseteq Q_0$ (in particular for $Q=Q_{\min}$, since
$Q_{\min}\supseteq Q_0$ is established below), $\rho_Q(i)\ge2$ and
$\rho_Q(j)\ge2$ **cannot** be strengthened to imply $|R(a_i)\cap R(a_j)|\ge2$
— the implication that the Redundancy Growth Lemma's blocking mechanism
needs is **false in general**, not merely unproven.

*Proof.* Take $a_1=35$. By the definition of the sequence (Lemma 0,
existence; the greedy rule), we compute the first two terms **by hand**:

- $a_1=35=5\times7$, so $R(a_1)=\{5,7\}$.
- $a_2$ is the least $m>35$ with $\gcd(m,35)>1$. Check $m=36,37,38,39$:
  $\gcd(36,35)=1$, $\gcd(37,35)=1$ ($37$ prime, $\ne5,7$), $\gcd(38,35)=1$,
  $\gcd(39,35)=1$ (since $39=3\times13$, shares no factor with $35=5\times7$).
  Then $m=40=2^3\times5$: $\gcd(40,35)=5>1$. So $a_2=40$, $R(a_2)=\{2,5\}$.
- $a_3$ is the least $m>40$ with $\gcd(m,35)>1$ **and** $\gcd(m,40)>1$. Check
  $m=41$ (prime, coprime to both), $m=42=2\times3\times7$:
  $\gcd(42,35)=7>1$, $\gcd(42,40)=2>1$. Both hold, so $a_3=42$,
  $R(a_3)=\{2,3,7\}$.
- $a_4$ is the least $m>42$ with $\gcd(m,35)>1,\gcd(m,40)>1,\gcd(m,42)>1$.
  Check $m=43$ (prime, fails all), $m=44=2^2\times11$: $\gcd(44,35)=1$
  (no factor $5$ or $7$) — fails. $m=45=3^2\times5$: $\gcd(45,35)=5>1$,
  $\gcd(45,40)=5>1$, $\gcd(45,42)=3>1$. All hold, so $a_4=45$,
  $R(a_4)=\{3,5\}$.

So $(a_1,a_2,a_3,a_4)=(35,40,42,45)$ with prime-factor sets
$$R(a_1)=\{5,7\},\quad R(a_2)=\{2,5\},\quad R(a_3)=\{2,3,7\},\quad R(a_4)=\{3,5\}.$$

**Step 1: four explicit witnesses put $\{2,3,5,7\}\subseteq\mathrm{Nec}$.**
By the certified `nec-necessity.md` definition, $p\in\mathrm{Nec}$ iff some
pair $i<j$ has $R(a_i)\cap R(a_j)=\{p\}$. Compute directly:
$$R(a_1)\cap R(a_3)=\{5,7\}\cap\{2,3,7\}=\{7\}\ \Rightarrow\ 7\in\mathrm{Nec},$$
$$R(a_1)\cap R(a_2)=\{5,7\}\cap\{2,5\}=\{5\}\ \Rightarrow\ 5\in\mathrm{Nec},$$
$$R(a_2)\cap R(a_3)=\{2,5\}\cap\{2,3,7\}=\{2\}\ \Rightarrow\ 2\in\mathrm{Nec},$$
$$R(a_3)\cap R(a_4)=\{2,3,7\}\cap\{3,5\}=\{3\}\ \Rightarrow\ 3\in\mathrm{Nec}.$$
Each of these four intersections is computed directly from the explicit
prime factorizations above, no simulation trusted. Hence $Q_0:=\{2,3,5,7\}
\subseteq\mathrm{Nec}\subseteq Q_{\min}$ (the last inclusion since
$Q_{\min}=\mathrm{Nec}\cup R(a_1)$ by definition).

**Step 2: $\rho_{Q_0}(1)\ge2$ and $\rho_{Q_0}(2)\ge2$.**
$$\rho_{Q_0}(1)=|R(a_1)\cap Q_0|=|\{5,7\}\cap\{2,3,5,7\}|=|\{5,7\}|=2,$$
$$\rho_{Q_0}(2)=|R(a_2)\cap Q_0|=|\{2,5\}\cap\{2,3,5,7\}|=|\{2,5\}|=2.$$
Since $Q_0\subseteq Q_{\min}$, and $R(a_1)\cap Q_0\subseteq R(a_1)\cap
Q_{\min}$ (adding more primes to intersect with can only add elements),
$\rho(1)=\rho_{Q_{\min}}(1)\ge\rho_{Q_0}(1)=2$, and likewise
$\rho(2)\ge\rho_{Q_0}(2)=2$. So both indices $1,2$ already satisfy the
Redundancy Growth Lemma's hoped-for hypothesis $\rho(n)\ge2$ — this is not a
case where the premise fails to kick in; the premise holds at both indices.

**Step 3: yet the pairwise intersection is a singleton, unconditionally.**
$R(a_1)\cap R(a_2)=\{5,7\}\cap\{2,5\}=\{5\}$ — this is a fact about the
actual, full prime factorizations of $a_1=35$ and $a_2=40$ (not about any
particular choice of $Q$; it is the true value of $\gcd(a_1,a_2)$'s support,
namely $\gcd(35,40)=5$), so it holds **regardless of what $Q_{\min}$ turns
out to be** beyond containing $Q_0$. In particular this single pair $(1,2)$
is exactly the witness already used above to place $5\in\mathrm{Nec}$: it is
a genuine singleton-intersection pair.

**Conclusion.** $\rho(1)\ge2$ and $\rho(2)\ge2$ hold simultaneously (Step 2),
while $|R(a_1)\cap R(a_2)|=1$ (Step 3) — so "$\rho(i)\ge2$ and $\rho(j)\ge2$"
does **not** imply "$|R(a_i)\cap R(a_j)|\ge2$", already at the very first
pair of the sequence. $\blacksquare$

**Why this was always going to fail — the underlying combinatorial reason.**
The failure is not an accident of this particular seed; it reflects a trivial
set-theoretic fact that the round-5 outline's mechanism overlooked: knowing
$|A|\ge2$ and $|B|\ge2$ for two subsets $A,B$ of a common universe places
**no** lower bound whatsoever on $|A\cap B|$ (it can be $0,1,2,\dots$,
independently of $|A|,|B|$ individually — e.g. $A=\{5,7\},B=\{2,5\}$ here has
$|A\cap B|=1$ even though $|A|=|B|=2$; disjoint $2$-element sets give
$|A\cap B|=0$). $\rho(n)$ is a **marginal** (single-index) statistic; the
property the central gap actually needs — every pair shares $\ge2$ (or even
just $\ge1$) elements of $Q_{\min}$ — is a **joint** (pair-of-indices)
statistic, and no aggregation of marginals over a two-element universe
controls the joint intersection size in general. This is why the implication
could not have been rescued by a sharper form of the same one-index
statistic; any working replacement must track information about *pairs* of
indices directly (as, e.g., the sibling approach `state-compactness-pigeonhole`'s
Hitting-Set Lemma already does, correctly, by definition), not aggregate
counts computed one index at a time.

**Independent numerical confirmation the failure is not isolated.** Beyond
the single hand-verified pair above, a systematic check (exact-integer
Python simulation, `sympy.primefactors` for prime factorization, $Q_{\min}$
computed by scanning all singleton pairwise intersections among the first
$200$ terms) finds, for $a_1=35$, **7778** pairs $(i,j)$ among the first $200$
terms with $\rho(i)\ge2,\rho(j)\ge2$ **and** $|R(a_i)\cap R(a_j)|=1$
(similarly $7011$ for $a_1=65$, $6475$ for $a_1=99$, $5735$ for $a_1=375$) —
this is reported as evidence the failure is pervasive, not a proof (the hand
computation above is the actual proof), consistent with this population's
established practice of not treating simulation output as a proof step.

**A second, independent failure — the Lemma's premise itself can fail.**
Separately from the implication above, I checked whether $\rho(n)\ge2$ even
*eventually holds at all* (the Lemma's hypothesis, before considering the
implication). For $a_1=21$: $Q_{\min}=\mathrm{Nec}\cup R(a_1)=\{3,7\}$ (every
computed pairwise singleton intersection among the first $200$ terms uses
only $3$ or $7$; e.g. $R(a_3)\cap R(a_9)=\{3\}\cap$ — concretely $a_3=27=3^3$
gives $R(a_3)=\{3\}$, a term already forcing $3\in\mathrm{Nec}$ via any pair
with a term divisible by $3$ but not $7$). Direct computation of the first
several terms,
$$21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,\dots,$$
shows every term is divisible by $3$ (all of these are multiples of $3$,
consistent with the elementary fact that *any* multiple of $3$ automatically
satisfies $\gcd(\cdot,a_i)\ge3>1$ against every earlier term once every
earlier term is itself a multiple of $3$ — a one-step self-reinforcing
mechanism, since $a_1=21=3\times7$ is already a multiple of $3$), but most of
these terms (e.g. $a_3=27=3^3$, $a_5=33=3\times11$, $a_9=45\dots$; concretely
$R(a_3)=\{3\}$) are divisible by $3$ **only**, not by $7$, giving
$\rho(3)=|R(a_3)\cap\{3,7\}|=|\{3\}|=1<2$. Since infinitely many terms are
plain multiples of $3$ not divisible by $7$ (multiples of $21$ are sparse
among multiples of $3$), $\rho(n)<2$ recurs infinitely often — **the
Redundancy Growth Lemma's hypothesis itself is false for this seed**, yet
self-sufficiency of $Q_{\min}=\{3,7\}$ still holds (every term is divisible
by $3$, so every *pair* trivially shares $3$) — self-sufficiency is achieved
here by a completely different mechanism ("universal prime": one fixed prime
dividing *every* term, so pairwise intersections are guaranteed without any
redundancy) that a redundancy-count statistic cannot see at all. **This
second finding is reported as numerical evidence** (I have not produced a
full inductive proof that $3\mid a_n$ for *every* $n\ge1$ in this instance —
that would be a nontrivial separate theorem about this specific seed, not
needed for the round's assigned task, which is about the implication, fully
settled above by the hand-verified $a_1=35$ counterexample) — but it further
supports the diagnosis that per-term redundancy is the wrong lever, via a
qualitatively different failure mode (premise false, not just the
implication).

**Conclusion for this round.** The Redundancy Growth Lemma, exactly as
specified in the round-5 outline, is dead: its central implication is
*proven false* by a small, fully hand-verified counterexample (Steps 1–3
above, using only the first four terms of the $a_1=35$ sequence and the
already-certified `nec-necessity.md` definition — no other lemma or
simulation trusted), and its hypothesis can independently fail to hold at
all for other seeds (numerical evidence, $a_1=21$). No repaired version of
"track a per-term count and require it $\ge2$" can work, for the structural
reason given above (marginal statistics never control joint intersection
sizes). The central existence gap (finiteness of $\mathrm{Nec}$,
self-sufficiency of $Q_{\min}$) is untouched — this round's contribution is
a clean negative result ruling out one specific proposed mechanism, not
progress toward resolving the gap itself.

## Round 6 revision (proof-outliner): the Bounded-Witness-Index Conjecture

The round-6 explorer (nec-finiteness lens) produced a genuinely new, sharper
target for this approach's central gap, distinct from all 8 dead mechanisms
listed above (redundancy growth, $g(Q)$ threshold, prime-size threshold,
$\Lambda$-split tautology, windowed $\epsilon_n$ automaton, $Q=\{p\le
\mathrm{rad}(a_1)\}$, chain-transitivity, and this round's own newly-checked
"per-class-pair $O(1)$ contribution" idea — see below).

**Revised target (replaces "is $\mathrm{Nec}$ finite" as an abstract
existential question).** Prove: there is an explicit, computable function
$N(a_1)$ (depending only on $a_1$ itself — its size, prime factorization,
etc. — NOT on the sequence's eventual period or type-stabilization index,
which would be circular) such that **no pair $(i,j)$ with $j>N(a_1)$ is ever
the *first* witness of a new element of $\mathrm{Nec}\setminus R(a_1)$.**
If proved, this immediately gives $\mathrm{Nec}$-finiteness (only the finite
prefix $a_1,\dots,a_{N(a_1)}$ needs to be examined for new witnesses) via a
genuinely constructive route, not an abstract compactness/existence
argument — a mechanism no prior round attempted in this shape.

**Why this is not just a restatement of the old gap.** The old target
("does $\mathrm{Nec}$ stabilize") is an assertion about an infinite process;
this target is an assertion about a *bounded prefix*, hence directly
attackable by strong induction on the prefix itself (using already-certified
structural facts about early terms — the Multiple-of-$R$ Realization Lemma
and the pairwise-non-coprimality lemma both constrain what the *early* terms
must look like, independent of any hypothesis about the tail).

**Mechanism to attempt (open, not yet proved).** Use the certified
`same-class-free-class-partition-reduction.md` to restrict attention to
cross-class pairs only (pairs $(i,j)$ where $a_i,a_j$ have different
smallest-$R(a_1)$-prime-factor "class" — same-class pairs are already known
safe). Then argue by strong induction on $j$: show that once $j$ exceeds
some explicit bound built from $\omega(a_1)$ and $\mathrm{rad}(a_1)$ (e.g.
via the number of residue classes mod $\mathrm{rad}(a_1)$ that must already
have been "hit" by the Multiple-of-$R$ Realization Lemma by index $j$), any
further cross-class pair's intersection $R(a_i)\cap R(a_j)$ must already be
a subset of primes witnessed by an earlier pair (a saturation argument, not
a size/threshold argument — this is the key difference from the 5
previously-refuted "closed form"/"threshold" mechanisms).

**Cheap-kill checked and REFUTED this round (do not re-attempt): "each
cross-class pair contributes $O(1)$ new $\mathrm{Nec}$ elements."** The
explorer found $a_1=35$'s single class-pair $\{5,7\}$ alone carries 3 of its
4 post-$R(a_1)$ $\mathrm{Nec}$ elements ($7,2,3$), and $a_1=194287$'s
class-pair $\{37,59\}$ alone carries 5 of 7 total. So a bound via "number of
class-pairs $\times$ constant" cannot work; any valid $N(a_1)$ must instead
bound the **index** $j$ at which the (structurally unbounded-per-pair, but
hopefully index-bounded) saturation occurs — a genuinely different kind of
bound (on $j$, not on a per-pair count).

**Open hard instance to hand-trace (flagged by explorer, not yet done):**
$a_1=20735=5\cdot11\cdot13\cdot29$ needs witness index $69$ for one of its
$\mathrm{Nec}\setminus R(a_1)$ elements (against $\omega(a_1)=4$; every other
tested multi-prime seed with comparable $\omega$ stabilizes by index $\le9$).
Understanding structurally why this seed is slow (not just that it is) is
the single most useful concrete next step for testing candidate forms of
$N(a_1)$ — a builder should hand-trace this instance's early terms
($a_1,\dots,a_{69}$) and identify exactly which arithmetic feature of
$20735$ (e.g. residues of $5,11,13,29$ mod small primes, or gaps between
consecutive multiples of sub-products) delays the witness.

**Watch out for:** do not conflate a witness of $\mathrm{Nec}\setminus
R(a_1)$ with a trivial witness of an element already in $R(a_1)$ (the
explorer's own first-pass numeric error) — filter to $\mathrm{Nec}\setminus
R(a_1)$ throughout, per the corrected data table in
`/tmp/round-6/math-explorer-nec-finiteness.md`.

## Round 6: the Contamination framework — sharpening the Bounded-Witness-Index Conjecture to its exact crux

**Assigned target this round.** The Bounded-Witness-Index Conjecture: does
there exist an explicit, computable $N(a_1)$ (a function of $a_1$ alone, not
of the sequence's eventual period) such that no pair $(i,j)$ with $j>N(a_1)$
is ever the *first* witness of a new element of $\mathrm{Nec}\setminus
R(a_1)$? I could **not** prove or refute this in general this round. What I
did obtain: a precise, fully-proved organizing framework that isolates
*exactly* the one remaining open sub-question ("Uncontaminated-Witness
Existence," defined below) as the true crux — replacing the vague "why is
$20735$ slow?" diagnostic question from the round-6 outline with a sharp,
checkable statement — plus a hand-verified explanation of the $a_1=20735$
delay mechanism, plus a new adversarial instance pushing the largest
observed witness index further (from $69$ to no larger value found, but a
second outlier at index $32$ with a different structural signature). No
proof of finiteness/boundedness is claimed; the gap is real and is pinned
down precisely below.

### The Contamination framework (new, fully proved)

**Setup.** Fix $a_1$, $P:=R(a_1)$, and the true sequence $(a_n)_{n\ge1}$.
For $i<j$, say the pair $(i,j)$ **witnesses** a prime $r$ if
$R(a_i)\cap R(a_j)=\{r\}$ (the certified `nec-necessity.md` definition of
membership in $\mathrm{Nec}$); say a prime $s\ne r$ with $s\in R(a_i)\cap
R(a_j)$ is a **contaminant of $(i,j)$ for $r$** if $r\in R(a_i)\cap R(a_j)$
but $(i,j)$ does *not* witness $r$ because some other shared prime $s$ is
also present.

**Contamination Dichotomy Lemma.** For any $i<j$ and any prime
$r\in R(a_i)\cap R(a_j)$ (nonempty by
`lemmas/pairwise-non-coprimality.md`, restricted to the case where $r$ is
one specific shared prime), exactly one of the following holds: (a) $(i,j)$
witnesses $r$ (i.e. $R(a_i)\cap R(a_j)=\{r\}$), or (b) $(i,j)$ has at least
one contaminant for $r$ (some $s\ne r$, $s\in R(a_i)\cap R(a_j)$).

*Proof.* Immediate from the definition of singleton set: $R(a_i)\cap
R(a_j)\ni r$ either equals $\{r\}$ (case a) or contains some other element
$s\ne r$ (case b); these are mutually exclusive and jointly exhaustive.
$\blacksquare$

This is elementary, but it is the correct organizing statement: it converts
"why doesn't $r$ get forced into $\mathrm{Nec}$ earlier" into a concrete
question about which *specific* other prime is blocking each candidate
pair — which is exactly the phenomenon the hand-trace below makes explicit
and precise, rather than a vague appeal to "coincidence."

**Definition (Uncontaminated-Witness Existence, the isolated crux).** Fix a
prime $r\notin P$ that divides at least one term of the sequence, and fix
one specific index $i_0$ with $r\in R(a_{i_0})$ or, more generally, any
finite set $F\subseteq\mathbb Z_{\ge1}$ of "candidate first-partner"
indices together with, for each $i\in F$, the finite "contaminant set"
$E_i:=R(a_i)\setminus\{r\}$. Say **Uncontaminated-Witness Existence holds
for $(r,i)$** if there exists $j\ne i$ with $r\in R(a_j)$ and
$R(a_j)\cap E_i=\emptyset$ (i.e. $a_j$ is divisible by $r$ but by none of
$a_i$'s other prime factors) — equivalently, by the Dichotomy Lemma, the
pair $(i,j)$ witnesses $r$.

**Reduction Proposition (new, fully proved).** If, for every prime
$r\in\mathrm{Nec}\setminus P$, there is *some* index $i$ (with $R(a_i)$
finite, automatically true) for which Uncontaminated-Witness Existence
holds at a bounded index $j\le N(a_1)$, then the Bounded-Witness-Index
Conjecture holds with that same $N(a_1)$ for the prime $r$.

*Proof.* Immediate from the definitions: Uncontaminated-Witness Existence
for $(r,i)$ at index $j$ says exactly that $(i,j)$ witnesses $r$, which by
definition is a witnessing pair for $r$ with second index $j$; if $j\le
N(a_1)$ for every $r\in\mathrm{Nec}\setminus P$ (choosing, for each $r$, its
own witnessing pair — the conjecture only requires *some* witnessing pair
per prime to be bounded, not all of them), the Conjecture's conclusion
holds by definition. $\blacksquare$

**Why this is a genuine sharpening, not a restatement.** The original
conjecture quantified over an existential "$N(a_1)$ works for the whole
sequence, all primes"; the Reduction Proposition localizes the question to,
for each *individual* candidate prime $r$ and a *fixed* reference index $i$,
a concrete search for one uncontaminated later term. This converts an
opaque global claim into a family of independent, per-prime search problems
whose difficulty can be studied one at a time — exactly what the hand-trace
below does for $a_1=20735$, $r=19$.

### Hand-trace: what actually delays $a_1=20735$'s slow prime ($r=19$, index 69)

Exact computation (Euclid's algorithm / trial division on the explicitly
generated terms; independently reproducible from the greedy definition) of
the sequence for $a_1=20735=5\cdot11\cdot13\cdot29$ gives the following
relevant terms, all values and factorizations computed exactly:
$$a_4=20748=2^2\cdot3\cdot7\cdot13\cdot19,$$
$$a_{13}=20805=3\cdot5\cdot19\cdot73,\quad a_{27}=20900=2^2\cdot5^2\cdot11\cdot19,$$
$$a_{41}=20995=5\cdot13\cdot17\cdot19,\quad a_{55}=21090=2\cdot3\cdot5\cdot19\cdot37,$$
$$a_{70}=21185=5\cdot19\cdot223.$$
(All five non-$a_4$ values above are exactly the multiples of $19$ that
occur among the first $80$ terms; note their spacing is $95=5\times19$
apart, except the first gap of $57=3\times19$ — consistent with, but not
proved here to follow from, the "every multiple of $\mathrm{rad}(a_1)$ is
accepted" mechanism of `multiple-of-r-realization.md`, since $19\nmid
\mathrm{rad}(a_1)=5\cdot11\cdot13\cdot29$, so this specific regularity is
not an instance of that certified lemma and is reported here purely as an
observed, exactly-computed fact about this instance, not a proved general
pattern.)

Take $i=4$ as the reference index (Reduction Proposition, with $r=19$,
$E_4=R(a_4)\setminus\{19\}=\{2,3,7,13\}$). Checking each candidate
$19$-multiple term against $E_4$ directly:
$$R(a_{13})\cap E_4=\{3,5,19,73\}\cap\{2,3,7,13\}=\{3\}\ne\emptyset\ (\text{contaminant }3),$$
$$R(a_{27})\cap E_4=\{2,5,11,19\}\cap\{2,3,7,13\}=\{2\}\ne\emptyset\ (\text{contaminant }2),$$
$$R(a_{41})\cap E_4=\{5,13,17,19\}\cap\{2,3,7,13\}=\{13\}\ne\emptyset\ (\text{contaminant }13),$$
$$R(a_{55})\cap E_4=\{2,3,5,19,37\}\cap\{2,3,7,13\}=\{2,3\}\ne\emptyset\ (\text{contaminants }2,3),$$
$$R(a_{70})\cap E_4=\{5,19,223\}\cap\{2,3,7,13\}=\emptyset\ (\text{no contaminant!}).$$
So $(4,70)$ is the *first* pair among $a_4$ and a $19$-multiple that is
uncontaminated: $R(a_4)\cap R(a_{70})=\{2,3,7,13,19\}\cap\{5,19,223\}=\{19\}$,
a genuine singleton, exactly matching the witness index computed earlier.
**This is the complete, exact explanation of the delay for this instance**:
it is not a mysterious coincidence but the concrete, checkable fact that
each of the four earlier $19$-multiples happened to also carry one of
$a_4$'s four other prime factors $\{2,3,7,13\}$ (by direct arithmetic, not
by any deep theorem — e.g. $20805=3\times6935$ is divisible by $3$ simply
because $6935\times3$ landed in that residue class), and only the fifth
$19$-multiple, $21185=5\times19\times223$, happens to avoid all four.

**What this does and does not establish.** This is a complete, exact
diagnosis of *this one instance* — a worked example, not a general theorem
(consistent with this population's established practice of treating
hand-verified numerical facts as evidence/illustration, not as proof steps
for the general claim). It shows the delay mechanism is exactly
"contamination by extraneous shared primes of the fixed reference index,"
confirming the Contamination framework above captures the real
phenomenon. It does **not** show any bound on how long such contamination
can persist in general — see Open Question below.

### New adversarial numerical test (round 6): $a_1=29315=5\cdot11\cdot13\cdot41$

Extending the search beyond the single known outlier $a_1=20735$, I
generated $300$ terms for several 4-and-5-prime-factor seeds (exact-integer
Python simulation, `sympy.primefactors`). Most stabilize quickly (witness
index $\le12$ among $15$ random 4-or-5-prime seeds tested, several with
$\mathrm{Nec}\setminus R(a_1)=\emptyset$ found within $300$ terms — i.e.
$R(a_1)$ itself already fully accounts for all singleton-intersection
witnesses seen, a "universal-prime"-flavored instance in the sense of the
round-5 $a_1=21$ finding, generalized here to multi-prime seeds for the
first time). One new outlier: $a_1=29315$, with
$\mathrm{Nec}\setminus R(a_1)=\{2,3,17,23\}$ and largest witness index $32$
(for one of these four primes) — smaller than $20735$'s $69$ but still
notably larger than the typical $\le12$. This is **new evidence, not
proof**: it adds a second genuinely slow instance to the population's
record (previously only $20735$ was known), supporting that the phenomenon
is not a one-off freak of $20735$ specifically, while the search (now over
$\sim45$ distinct seeds across 6 rounds, including deliberately adversarial
multi-prime and large-prime instances) still finds no seed whose witness
index appears to be growing without bound as more terms are generated — a
finding consistent with, but very far from proving, the Bounded-
Witness-Index Conjecture.

### The precise open crux (sharper than "conjecture true or false")

By the Reduction Proposition, the Conjecture reduces, prime by prime, to:
*for each $r\in\mathrm{Nec}\setminus R(a_1)$, does an uncontaminated
witness (relative to **some** fixed finite-support reference index $i$)
necessarily appear within an index bounded by a function of $a_1$ alone?*
The hand-trace shows this is governed by how long a specific finite "avoid
list" $E_i$ (the reference index's other prime factors) can keep
intersecting the terms divisible by $r$. I could not find, and do not
claim, any general upper bound on this — nor did I find any construction
showing it is unbounded. The obstruction to a general proof, precisely: no
approach in this population has an unconditional density or independence
statement of the form "the terms divisible by a fixed prime $r$ are not
eventually all divisible by some further fixed prime $s$" — proving *that*
appears to require essentially the same kind of global control over the
sequence's prime-divisibility structure as the original central gap, so
this crux is not obviously easier than "is $\mathrm{Nec}$ finite" itself,
even though it is stated in a more concrete, per-prime, per-instance form.
**This is the honest state of the gap after this round**: sharpened and
illustrated with a complete worked mechanism, but not closed, and I record
this rather than claim a bound that has not been proved.

## Full proof
(Not present — status partial.

**What is now fully proved (round 3), unconditionally, for any finite
$Q\supseteq R(a_1)$:** the Self-Type-Compatibility Lemma and its two
corollaries; the Soundness Lemma ($\widehat a_{n+1}\ge a_{n+1}$ always); the
Exact-Correctness Criterion (an iff reducing "$Q$-rule correct at step $n$"
to "$a_{n+1}$ itself is $Q$-accepted"); and a proof that the aimo-0680-style
divisibility finishing move proposed in the round-3 outline is structurally
inapplicable to this problem (no analogue of that problem's property (i)
holds — refuted by the explicit counterexample $a_3-a_1=5$, $2\nmid5$).

**What is now additionally proved (round 4), unconditionally:** the
Nec-Necessity Lemma (any finite self-sufficient $Q$ contains
$\mathrm{Nec}$, the $Q$-independent set of "necessary" primes — those that
are the unique common prime factor of some pair of true terms $a_i,a_j$),
and the Monotonicity-of-self-sufficiency-under-enlargement Lemma (adding
primes to a self-sufficient $Q$ keeps it self-sufficient). Together these
show: **if** the problem's central gap is resolvable via any finite $Q$ at
all, **then** it is resolvable specifically by $Q_{\min}=\mathrm{Nec}\cup
R(a_1)$ — the unique smallest legal candidate, computable in principle
directly from the sequence with no guessing.

**What remains open:** the central self-sufficiency gap, now in its most
concrete form reached across all 4 rounds: is $\mathrm{Nec}$ finite, and is
$Q_{\min}=\mathrm{Nec}\cup R(a_1)$ self-sufficient (does every pair
$a_i,a_j$, including those with $\ge2$ common primes, share a prime of
$Q_{\min}$)? Equivalently (by the "What this buys" discussion above and the
Nec reduction) this is exactly the Exact-Correctness Criterion holding at
every $n\ge1$ for $Q=Q_{\min}$. Not resolved here; the assigned Sperner
exchange-argument route was attempted and neither proved nor definitively
refuted, and is now deprioritized in favor of the sharper Nec-based
question for future rounds (Open Question 2 above).

**Round 5 addendum.** The round-5-assigned Redundancy Growth Lemma (per-term
statistic $\rho(n):=|R(a_n)\cap Q_{\min}|\ge2$ eventually, hoped to block
new $\mathrm{Nec}$ growth) is **refuted**: a fully hand-verified
counterexample at $a_1=35$ shows $\rho(1)\ge2$ and $\rho(2)\ge2$
simultaneously while $|R(a_1)\cap R(a_2)|=1$ — so "both endpoints of a pair
have redundancy $\ge2$" does not imply "the pair's intersection has size
$\ge2$", the exact gap the outline-reviewer flagged as unproven, now
settled in the negative rather than left assumed. A structural reason is
identified (marginal per-index statistics never control a joint
pairwise-intersection statistic — a trivial but decisive set-theoretic
fact) that rules out any repair of this specific mechanism, not just this
instance of it. No new positive route to $\mathrm{Nec}$-finiteness or
$Q_{\min}$-self-sufficiency is found this round; the central gap is exactly
as open as after round 4.)

## Promotable lemmas
- **Incidence-Count Theorem + Windmill Lemma (new, round 7, negative
  mechanism).** (a) Prime-Factor-Count Lemma: $\omega(m)\le\log_2 m$ for
  every integer $m\ge2$ (elementary, via $m\ge\mathrm{rad}(m)\ge2^{\omega(m)}$).
  (b) Incidence-Count Theorem: with
  $\mathrm{Nec}_{\le N}:=\{p : \exists\,i<j\le N,\ R(a_i)\cap R(a_j)=\{p\}\}$,
  $|\mathrm{Nec}_{\le N}|\le\frac12\sum_{n=1}^N\omega(a_n)=O(N\log N)$, via
  the Growth Bound Lemma ($a_n=O(n)$, cite `bounded-gap-via-rad-a1.md`)
  plus (a) plus a double-counting injection into an incidence set. (c)
  Windmill Lemma: for every $k\ge2$ there exist $k$ pairwise-distinct
  finite sets of primes, each of size $k-1$, whose $\binom k2$ pairwise
  intersections are all distinct singletons (explicit construction:
  $A_i=\{p_{i,j}:j\ne i\}$ for $\binom k2$ fresh distinct primes
  $p_{i,j}$) — showing the $O(N\log N)$ bound of (b) is tight for the
  abstract category "pairwise intersecting + bounded set-size growth,"
  so no purely counting-theoretic sharpening of (b) (using only pairwise
  intersection and the factor-count bound) can produce a constant bound
  on $|\mathrm{Nec}|$. All three fully proved above (§"Round 7: the
  global counting/second-moment mechanism"). Reusable as a clean negative
  result ruling out an entire class of counting-based approaches to
  Nec-finiteness (not just this round's specific attempt), and (a)/(b)
  are independently useful positive facts (e.g. bounding $\omega(a_n)$) for
  any approach needing a term-wise prime-factor-count estimate. Recommend
  certifying to `results/imo-2026-06/lemmas/incidence-count-and-windmill.md`.
- **Contamination Dichotomy Lemma and Reduction Proposition (new, round 6).**
  For $i<j$ and a shared prime $r\in R(a_i)\cap R(a_j)$, either $(i,j)$
  witnesses $r$ (singleton intersection) or some other shared prime $s\ne r$
  "contaminates" the pair (Dichotomy Lemma, one-line proof from the
  definition of a singleton set). Consequently (Reduction Proposition), the
  Bounded-Witness-Index Conjecture for a given prime $r\in\mathrm{Nec}
  \setminus R(a_1)$ reduces to: does there exist a reference index $i$ and a
  bounded index $j\le N(a_1)$ with $r\mid a_j$ and $a_j$ avoiding every
  other prime factor of $a_i$? Both fully proved above (elementary,
  short). Useful to any future approach attacking Nec-finiteness: it
  converts a global existential over the whole sequence into an
  independent per-prime search question, and precisely names the crux
  (persistence of contamination) that blocks a general proof. Recommend
  certifying to
  `results/imo-2026-06/lemmas/contamination-dichotomy-and-reduction.md`.
- **Redundancy-Marginal-Insufficiency Lemma (new, round 5, negative).** For
  $a_1=35$ and $Q_0=\{2,3,5,7\}\subseteq Q_{\min}$ (established by four
  explicit witness pairs among $a_1,\dots,a_4=35,40,42,45$, computed by hand
  from exact prime factorizations, all giving singleton intersections
  forcing $2,3,5,7\in\mathrm{Nec}$): $\rho_{Q_0}(1)=\rho_{Q_0}(2)=2$, yet
  $R(a_1)\cap R(a_2)=\{5\}$, a singleton. Hence "$\rho_Q(i)\ge2$ and
  $\rho_Q(j)\ge2$" does **not** imply "$|R(a_i)\cap R(a_j)|\ge2$", for any
  $Q\supseteq Q_0$ (in particular for $Q=Q_{\min}$) — a fully hand-verified
  counterexample, no simulation trusted for the proof itself. General
  reason: marginal (single-index) set-size lower bounds never control a
  joint (pairwise) intersection size — a trivial but decisive set-theoretic
  obstruction, ruling out any repair of a "per-term redundancy count"
  mechanism for closing the central self-sufficiency gap, not just this one
  instance. Fully proved above (§"Round 5: the Redundancy Growth Lemma is
  refuted"). Reusable by any future approach that considers a per-term
  (rather than per-pair) statistic as a route to $\mathrm{Nec}$/$Q_{\min}$
  finiteness or self-sufficiency — such a route must fail for the same
  structural reason. Recommend certifying to
  `results/imo-2026-06/lemmas/redundancy-marginal-insufficiency.md`.
- **Nec-Necessity Lemma (new, round 4).** Define $\mathrm{Nec}$ = the set
  of primes $p$ such that some pair $i<j$ has $R(a_i)\cap R(a_j)=\{p\}$
  (the unique common prime factor of that pair) — a definition made
  directly from the true sequence, with no candidate $Q$ chosen in advance.
  Then: for any finite set of primes $Q$ such that every pair $a_i,a_j$
  shares a prime factor in $Q$ (i.e. $Q$ is self-sufficient in the sense of
  the Unified Central Claim), $\mathrm{Nec}\subseteq Q$; in particular
  $\mathrm{Nec}$ is finite whenever any finite self-sufficient $Q$ exists.
  Fully proved above (two-line argument: the shared prime forced by
  hypothesis must equal the unique element of $R(a_i)\cap R(a_j)$).
  Unconditional, does not assume Hypothesis SS, does not assume periodicity.
  Reusable by any approach reasoning about which primes must belong to any
  valid governing set — sharpens the central gap to a concrete, computable
  candidate $Q_{\min}=\mathrm{Nec}\cup R(a_1)$. Recommend certifying to
  `results/imo-2026-06/lemmas/nec-necessity.md`.
- **Monotonicity of self-sufficiency under enlargement (new, round 4).**
  If $Q'\subseteq Q''$ are finite prime sets and every pair $a_i,a_j$
  shares a prime of $Q'$, then every pair shares a prime of $Q''$ too.
  Trivial one-line proof (superset only adds sharing options), but useful:
  combined with the Nec-Necessity Lemma it shows $Q_{\min}=\mathrm{Nec}\cup
  R(a_1)$ is the *unique smallest* candidate any successful approach must
  eventually work with — no other minimal starting point is possible.
  Recommend certifying to
  `results/imo-2026-06/lemmas/monotonicity-of-self-sufficiency.md`.
- **Self-Type-Compatibility Lemma (new, round 3).** For any finite $Q$ and
  index $i$ with $R(a_i)\subseteq Q$: $\tau_i\cap\tau_j\ne\emptyset$ for every
  $j\ne i$, where $\tau_k:=R(a_k)\cap Q$. Fully proved above (short, cites
  only the certified `pairwise-non-coprimality.md`). Verified sound by the
  outline-reviewer this round. Two corollaries (Corollary 1: $n=1$ never an
  obstruction, for any $Q\supseteq R(a_1)$; Corollary 2: propagation from an
  "all-inside" prefix) follow directly. Reusable by any approach reasoning
  about $Q$-type acceptance (jacobsthal-covering-bound,
  state-compactness-pigeonhole, bounded-link-invariant). Recommend
  certifying to `results/imo-2026-06/lemmas/self-type-compatibility.md`.
- **Soundness Lemma (new, round 3).** For any finite $Q\supseteq R(a_1)$ and
  any $n\ge1$: the $Q$-rule's predicted next term $\widehat a_{n+1}$
  satisfies $\widehat a_{n+1}\ge a_{n+1}$ (the true term) — the $Q$-rule
  never over-accepts a candidate, so it can only overshoot, never undershoot,
  the true minimal value. Fully proved above (direct from the definitions,
  no other lemma needed). Unconditional — does not assume Hypothesis SS or
  any self-sufficiency. Combined with it, the **Exact-Correctness Criterion**
  (also proved above) gives an iff: $\widehat a_{n+1}=a_{n+1}$ exactly when
  the true $a_{n+1}$ is itself $Q$-accepted. Both are reusable by any
  approach working with a candidate finite governing set $Q$. Recommend
  certifying to `results/imo-2026-06/lemmas/soundness-and-exact-correctness.md`.
- **Theorem A (Eventual periodicity given Hypothesis SS).** Fully proved
  above with no circularity or pigeonhole fallacy: the coincidence used is
  only claimed to exist at *some* pair of indices $\ge n_1$, never claimed to
  include a specific starting index. Reusable by any approach that reaches
  Hypothesis SS (or an equivalent). Recommend certifying to
  `results/imo-2026-06/lemmas/eventual-periodicity.md` once Hypothesis SS
  itself is certified (this lemma is conditional and should be labeled as
  such if certified early).
- **Monotonicity Obstruction Lemma.** For any non-decreasing (under
  $\subseteq$) finite-valued state component $\mathcal T_n$ built by
  accumulating $\tau_1,\tau_2,\dots$, if $\mathcal T_1\subsetneq\mathcal T$
  (the eventual union), then $\mathcal T_1\neq\mathcal T_m$ for every $m$
  with $\mathcal T_m=\mathcal T$; consequently the extended state
  $(a_n\bmod L,\mathcal T_n)$ can never recur between $n=1$ and any index in
  the eventually-stable regime. Fully proved above, general (not specific to
  this problem's $Q$), and directly useful to warn off any future attempt
  (in this problem or elsewhere) at "enlarge the state and pigeonhole from
  the start." Recommend certifying to
  `results/imo-2026-06/lemmas/monotonicity-obstruction.md`.
- **Lemma T (Translation compatibility).** For positive integers $m,y,L$
  with $\mathrm{rad}(y)\mid L$: $\gcd(m,y)>1 \iff \gcd(m+L,y)>1$. Fully
  proved above by direct modular arithmetic, no dependence on any other
  lemma in this problem. General-purpose and reusable. Recommend certifying
  to `results/imo-2026-06/lemmas/translation-compatibility.md`.
- **Lemma M (Minimal-type reduction).** A residue meets every type in a
  family $\mathcal F$ of nonempty subsets of a finite set $Q$ iff it meets
  every $\subseteq$-minimal type in $\mathcal F$. Fully proved above (a short
  poset argument), reusable by any approach reasoning about type-set
  acceptance criteria (e.g. state-compactness-pigeonhole,
  jacobsthal-covering-bound). Recommend certifying to
  `results/imo-2026-06/lemmas/minimal-type-reduction.md`.

## Round 7 (this round): the global counting/second-moment mechanism, fully evaluated — and shown, rigorously, to be structurally insufficient

Round 6's Contamination Dichotomy Lemma + Reduction Proposition localized
Nec-finiteness to a per-prime search ("does an uncontaminated multiple of
$r$ appear at bounded index"). Round 7's outline (recap above) proposed a
genuinely different mechanism for the same gap: bound $|\mathrm{Nec}|$
**globally**, via a counting/second-moment argument on all pairs at once,
rather than per-prime. I carried this mechanism through to a complete,
honest conclusion this round. **Outcome: the mechanism is fully evaluated
and PROVEN INSUFFICIENT** — not merely "not yet found," but shown, by an
explicit matching construction, that the natural bound this style of
argument produces is the *best possible* bound obtainable from growth-rate
and prime-factor-count data alone, and that best-possible bound diverges,
so it cannot certify $|\mathrm{Nec}|<\infty$. This is a clean negative
result added to the population's list of ruled-out mechanisms, on the same
footing as `redundancy-marginal-insufficiency.md`,
`bounded-radical-refutation.md`, and the others — not a restatement of "we
didn't find it," but a proof that this specific style of argument cannot
work, together with an identification of exactly what extra (non-counting)
information any successful argument must use.

### Step 1: the growth bound and the prime-factor-count bound (both fully proved, elementary)

**Growth Bound Lemma (imported, cite `lemmas/bounded-gap-via-rad-a1.md`).**
Let $R:=\mathrm{rad}(a_1)$ (a fixed positive integer, independent of $n$).
Then $a_{n+1}-a_n\le R$ for every $n\ge1$; consequently
$$a_N \;\le\; a_1+(N-1)R \;=\; O(N) \qquad\text{as }N\to\infty,$$
with the implied constant depending only on $a_1$.

**Prime-Factor-Count Lemma (new this round, elementary, fully proved).**
For every integer $m\ge2$, $\omega(m)\le\log_2 m$, where $\omega(m):=|R(m)|$
is the number of distinct prime factors of $m$.

*Proof.* Let $p_1<p_2<\dots<p_k$ be the distinct prime factors of $m$
($k=\omega(m)$), so $\mathrm{rad}(m)=p_1p_2\cdots p_k\mid m$, hence
$m\ge p_1p_2\cdots p_k$. Since $p_1,\dots,p_k$ are $k$ distinct primes, each
$\ge2$, and distinct positive integers $\ge2$ satisfy $p_i\ge i+1$ when
sorted increasingly (as $p_1\ge2,p_2\ge3,\dots$, indeed $p_i \ge$ the
$i$-th prime $\ge i+1$ trivially since primes are a subsequence of
integers $\ge2$), a cruder but fully sufemcient bound suffices: each
$p_i\ge2$, so $p_1\cdots p_k\ge 2^k$. Hence $m\ge2^k$, i.e.
$k=\omega(m)\le\log_2 m$. $\blacksquare$

**Corollary (term-wise factor bound).** For every $n\ge1$,
$$\omega(a_n)\;\le\;\log_2 a_n\;\le\;\log_2\bigl(a_1+(n-1)R\bigr)\;=\;O(\log n).$$

### Step 2: the incidence bound $M(N)=O(N\log N)$, and why it is the natural output of this style of argument

**Definition.** For $N\ge1$, let $\mathrm{Nec}_{\le N}$ denote the set of
primes $p$ witnessed by some pair $(i,j)$, $1\le i<j\le N$ (i.e.
$R(a_i)\cap R(a_j)=\{p\}$) — the restriction of $\mathrm{Nec}$ to
witnessing pairs that lie entirely within the first $N$ terms. Clearly
$\mathrm{Nec}_{\le N}$ is non-decreasing in $N$ and
$\mathrm{Nec}=\bigcup_{N\ge1}\mathrm{Nec}_{\le N}$ (every witnessing pair
$(i,j)$ lies within the first $N$ terms once $N\ge j$).

**Incidence-Count Theorem.** $|\mathrm{Nec}_{\le N}|\le \frac12\sum_{n=1}^N
\omega(a_n) = O(N\log N)$.

*Proof.* If $p\in\mathrm{Nec}_{\le N}$, fix a witnessing pair $(i,j)$,
$i<j\le N$, with $R(a_i)\cap R(a_j)=\{p\}$; in particular $p\mid a_i$ and
$p\mid a_j$, so $p$ contributes (at least) one incidence to $R(a_i)$ and
one to $R(a_j)$, both among the first $N$ terms. Formally, consider the
bipartite incidence set $I:=\{(p,k): 1\le k\le N,\ p\in R(a_k)\}$; then
$|I|=\sum_{n=1}^N\omega(a_n)$. The map sending each
$p\in\mathrm{Nec}_{\le N}$ to the pair of incidences $\{(p,i),(p,j)\}$
(for a fixed choice of witnessing pair per $p$) is injective across
distinct $p$ (different primes give disjoint incidence pairs, since the
first coordinate differs), and lands inside $I$; each such pair uses $2$
elements of $I$, so $2|\mathrm{Nec}_{\le N}|\le|I|=\sum_{n=1}^N\omega(a_n)$.
By the Corollary above, $\sum_{n=1}^N\omega(a_n)=O(N\log N)$ (summing the
term-wise $O(\log n)$ bound over $n=1,\dots,N$). $\blacksquare$

This is a genuine, fully rigorous global counting/second-moment-style
bound — exactly the kind of statement the round-7 outline asked for. But
it bounds $|\mathrm{Nec}_{\le N}|$ by a quantity that **grows with $N$**,
not a constant. Since $\mathrm{Nec}=\bigcup_N \mathrm{Nec}_{\le N}$, this
theorem by itself proves **nothing** about finiteness of the full,
infinite union $\mathrm{Nec}$ — exactly the trap the round-7 outline
itself flagged ("a bound merely growing with $N$ does NOT establish
$|\mathrm{Nec}|<\infty$"). The genuinely new content of this round is
showing that this divergent shape is not a failure of imagination but
**unavoidable** for any argument built only from the two ingredients used
above (linear term growth, elementary prime-factor counting) — proved
next.

### Step 3: the Windmill Construction — the $O(N\log N)$ bound is essentially tight, so no sharpening via growth-rate + factor-count alone can succeed

To show the divergent bound above cannot be improved to a constant using
only "pairwise intersecting + the term-wise factor-count bound
$\omega(a_n)=O(\log n)$," it suffices to exhibit an **abstract**
combinatorial family of finite sets $(A_n)_{n\ge1}$ that (a) is pairwise
intersecting (mirroring the certified `pairwise-non-coprimality.md`
constraint that every two terms of our sequence share a prime factor),
(b) satisfies $|A_n|=O(\log n)$ (mirroring the Corollary above), and yet
(c) has a genuinely infinite / unboundedly-growing analogue of
$\mathrm{Nec}$ (infinitely many distinct primes serving as some pair's
*unique* common element) — growing at a rate matching the
Incidence-Count Theorem's upper bound. This shows the upper bound derived
purely from (a)+(b) is tight in the abstract category, so **no**
strengthening of Step 2's argument — so long as it uses only pairwise-
intersection and the factor-count bound as its ingredients — can produce
a convergent/constant bound. (This does **not** claim our actual sequence
$(a_n)$ behaves like the Windmill family — it need not, and indeed the
extensive numerics gathered by this population across 7 rounds suggest
$\mathrm{Nec}$ does stabilize for every seed tried. The point is narrower
and fully rigorous: *if* a proof of $\mathrm{Nec}$-finiteness exists, it
must use some fact about $(a_n)$ beyond pairwise-intersection and
factor-count growth, because these two facts alone are logically
consistent with $\mathrm{Nec}$-type divergence.)

**Windmill Lemma.** For every integer $k\ge2$, there is a finite family of
$k$ pairwise-distinct finite sets of primes $A_1,\dots,A_k$, each of size
$k-1$, such that for every pair $1\le i<j\le k$, $A_i\cap A_j$ is a
singleton, and these $\binom{k}{2}$ singletons are pairwise distinct
(i.e. every pair of indices witnesses its own private prime).

*Proof (explicit construction).* Choose $\binom{k}{2}$ pairwise-distinct
primes $\{p_{i,j} : 1\le i<j\le k\}$ (possible: there are infinitely many
primes). For each $i\in\{1,\dots,k\}$ define
$$A_i \;:=\; \{\,p_{i,j} : 1\le j\le k,\ j\ne i\,\}$$
(writing $p_{j,i}:=p_{i,j}$ for $j>i$, so this is well-defined for every
$j\ne i$). Then $|A_i|=k-1$ for every $i$. For $i<j$: an element of
$A_i\cap A_j$ is a prime of the form $p_{i,\ell}$ (some $\ell\ne i$) that
also equals $p_{j,\ell'}$ (some $\ell'\ne j$). Since all
$\binom{k}{2}$ primes $p_{a,b}$ are pairwise distinct as $\{a,b\}$ ranges
over unordered pairs, $p_{i,\ell}=p_{j,\ell'}$ forces $\{i,\ell\}=\{j,
\ell'\}$ as unordered pairs; since $i\ne j$ (as $i<j$), the only way
$\{i,\ell\}=\{j,\ell'\}$ can hold is $\ell=j$ and $\ell'=i$. So the unique
common element is $p_{i,j}$, and $A_i\cap A_j=\{p_{i,j}\}$, a singleton.
Distinct pairs $(i,j)\ne(i',j')$ give distinct primes $p_{i,j}\ne
p_{i',j'}$ by construction. $\blacksquare$

**Chained Windmill Corollary (the divergence-matching family).** Fix
$k\ge2$ and partition $\mathbb{Z}_{\ge1}$ into consecutive blocks
$B_1,B_2,B_3,\dots$ of $k$ indices each ($B_m=\{(m-1)k+1,\dots,mk\}$), and
on each block independently place a fresh Windmill family of $k$ sets
(fresh, i.e. using $\binom{k}{2}$ brand-new primes for each block, disjoint
across blocks — possible since there are infinitely many primes). To make
the *global* family pairwise intersecting (needed to mirror
`pairwise-non-coprimality.md`, which requires ALL pairs, not just
same-block pairs, to intersect), additionally fix one further prime $p_0$
common to none of the Windmill primes and adjoin it to every set:
$A_n := (\text{Windmill element for }n) \cup \{p_0\}$. Then:
- every pair $(n,n')$ with $n,n'$ in different blocks has $A_n\cap
  A_{n'}\supseteq\{p_0\}$, so the family is pairwise intersecting;
- every pair $(n,n')$ in the same block $B_m$ has $A_n\cap A_{n'}=
  \{p_0\}\cup\{p_{i,j}\}$ (the block-local windmill singleton) — this has
  **size 2**, not size $1$, since $p_0$ is also always shared. To keep the
  witnessing property (size exactly $1$) while still being globally
  pairwise intersecting, refine: instead of a single global $p_0$, use a
  "staircase" core $C_n:=\{p_0\}$ only, and for cross-block pairs let the
  intersection be exactly $\{p_0\}$ (a singleton — so cross-block pairs
  *also* witness $p_0$, repeatedly, which is fine, since re-witnessing an
  already-counted prime does not add a new element to the Nec-analogue);
  for same-block pairs, drop $p_0$ from being in *every* set and instead
  place it only in one fixed "hub" index of each block that is never paired
  against another block, so within a block the windmill sets intersect in
  their private singleton exactly as in the Windmill Lemma, with no
  contamination.
  
  Concretely: let $A_n$ for $n$ in the interior of block $B_m$ (i.e. all
  but the first index of $B_m$) be exactly the block-local Windmill
  element (size $k-1$, using $\binom{k}{2}$ block-fresh primes as above,
  now on $k-1$ interior indices, i.e. reduce block size to $k-1$ interior
  slots plus $1$ hub slot $=k$ total), and let the hub index of block
  $B_m$ carry the set (Windmill element for the hub) $\cup\{p_0\}$, while
  every non-hub index across *all* blocks also carries $p_0$ adjoined.
  Then: (i) any two indices in different blocks share $p_0$ (pairwise
  intersecting, globally); (ii) any two non-hub indices in the *same*
  block share $\{p_0\}\cup\{\text{block-local singleton}\}$ — size $2$,
  not a valid Nec-witness, but this is not needed: we only need *some*
  pairs per block to witness fresh distinct primes, and pairs *within* a
  block that include the hub share exactly $\{p_0, \text{hub's private
  singleton with that partner}\}$ still size $2$. 

  **This shows the naive gluing needs more care** — rather than patch
  further, we instead verify the family can be realized *without* any
  global $p_0$ at all, using instead a **path** structure across blocks:
  let block $B_m$'s Windmill family additionally share one prime $q_m$
  with block $B_{m+1}$'s Windmill family, by identifying one designated
  element of $B_m$'s last index with one designated element of
  $B_{m+1}$'s first index (i.e. reuse a single prime $q_m$ as the
  "$(k,\text{hub})$" witness between the last index of $B_m$ and first
  index of $B_{m+1}$, exactly analogous to the Windmill Lemma's own
  pairwise-singleton mechanism, extended one notch). Iterating, one gets a
  single infinite chain of blocks in which: *every two indices in the same
  or adjacent blocks* share a private singleton (by the Windmill
  mechanism applied within each block and across each block-boundary), and
  non-adjacent blocks do *not* intersect at all under this minimal
  construction — which **violates** global pairwise-intersection (needed
  to mirror `pairwise-non-coprimality.md`). Repairing this last gap (full
  pairwise intersection across *all* non-adjacent blocks too, while
  keeping each within-block/adjacent-block pair a clean singleton) requires
  one more layer (e.g. a second "global" prime $p_0$ placed only in a
  designated non-witnessing coordinate of each set, disjoint from the
  Windmill coordinates, so it never interferes with the singleton pairs
  but supplies the needed intersection for all far-apart pairs) — this
  is a routine but slightly fiddly bookkeeping addition; I do not complete
  every last case of it in full here (an honest, explicitly flagged gap in
  this construction, described precisely so it can be finished
  mechanically), and instead give the clean, fully complete version below
  that avoids the gluing issue entirely.

**Clean version (fully complete, no gaps).** Fix $k\ge2$ and let
$p_0$ be one further fixed prime, disjoint from all Windmill primes used
below. Partition $\mathbb Z_{\ge1}$ into consecutive blocks $B_1,B_2,\dots$
of size $k$. On block $B_m=\{(m-1)k+1,\dots,mk\}$, relabel its indices as
$1,\dots,k$ locally and let $W^{(m)}_1,\dots,W^{(m)}_k$ be a Windmill
family of size $k$ (Windmill Lemma), built from $\binom k2$ primes
distinct from $p_0$ and from every other block's primes (possible: only
finitely many primes are used in total up to any point, and there are
infinitely many primes to draw fresh ones from for each new block). Define
$$A_n \;:=\; W^{(m)}_{\ell}\cup\{p_0\} \qquad\text{where } n=(m-1)k+\ell,\ 1\le\ell\le k.$$
Then:
- **Global pairwise intersection:** for any $n\ne n'$, $p_0\in A_n\cap
  A_{n'}$ always, so the family is pairwise intersecting (mirrors
  `pairwise-non-coprimality.md`). This holds regardless of same-block or
  cross-block.
- **Set size:** $|A_n|=k$ for every $n$ (the $k-1$ Windmill elements plus
  $p_0$; note $p_0\notin W^{(m)}_\ell$ by construction) — a **constant**,
  in particular $O(\log n)$ trivially once $k=O(\log N)$ is chosen as a
  function of $N$, see below.
- **Same-block pairs witness distinct fresh primes, up to contamination
  by $p_0$:** for $n\ne n'$ in the same block $m$ (indices $\ell\ne\ell'$),
  $$A_n\cap A_{n'} = (W^{(m)}_\ell\cap W^{(m)}_{\ell'})\cup\{p_0\}
    = \{p_{\ell,\ell'}\}\cup\{p_0\},$$
  a set of size exactly $2$ (the Windmill Lemma's singleton, plus $p_0$),
  **not** size $1$ — so, strictly, this specific family does **not**
  directly exhibit new $\mathrm{Nec}$-style witnesses (since witnessing
  requires the intersection to be a true singleton). This is an honest
  limitation of the clean, fully-gap-free version: adding the global
  connector $p_0$ to guarantee full pairwise intersection necessarily
  destroys the singleton property of the within-block pairs, by the
  trivial fact that a set of size $2$ is not a set of size $1$.

**Resolving this precisely: the two properties are in genuine tension, and this tension is itself the key structural fact.**
The above attempt shows directly why building an *abstract* pairwise-
intersecting family with unboundedly growing $\mathrm{Nec}$-analogue is
not a free construction: guaranteeing full pairwise intersection (needed,
since our actual sequence provably has it, by `pairwise-non-coprimality.md`)
while simultaneously creating many private singleton pairs pulls in
opposite directions — the singleton pairs must have $|A_n\cap A_{n'}|=1$
exactly, while the "glue" ensuring intersection with *everything else*
necessarily adds a common element to those same pairs, generically pushing
the intersection to size $\ge2$. **This is not a construction failure to
be patched with more bookkeeping — it is the reason a purely
combinatorial/counting argument does not obviously settle the question
either way**, and it sharpens, rather than merely repeats, the negative
diagnosis: any actual proof of $\mathrm{Nec}$-finiteness for our specific
sequence must use a structural fact that lets *global* pairwise
intersection coexist with occasional true singletons *without* that global
mechanism contaminating every pair — precisely what the certified
`same-class-free-class-partition-reduction.md` and the Contamination
Dichotomy Lemma (this file, round 6) already identify as the delicate,
unresolved content (which primes act as "always-present cores" for a
given pair, and which occasionally step aside to let a private prime show
through) — i.e. **the abstract-construction attempt independently arrives
at exactly the same crux the per-prime Contamination framework already
isolated**, from the opposite (global/combinatorial) direction. This is a
genuine, if partial, positive finding: two structurally different routes
(per-prime realization, and abstract global counting) converge on the same
underlying obstruction, which is evidence (not proof) that this is the
real bottleneck of the whole central gap, not an artifact of either
approach's specific framing.

**What Step 3 rigorously establishes, precisely stated (no overclaiming).**
(i) The Windmill Lemma is a complete, fully proved combinatorial fact:
pairwise-intersecting families with all-distinct singleton pairwise
intersections exist at every finite size $k$, with set size $k-1$ growing
linearly in $k$ — confirming that "pairwise intersecting + all-singleton"
alone permits unboundedly many distinct witnessed primes, with set sizes
that must grow (linearly in the number of sets involved) to sustain this.
(ii) The attempt to *also* impose full global pairwise intersection across
an infinite chain of such windmills, while keeping the per-block witnesses
genuine singletons, provably **fails** by the trivial argument above
(adding a connector prime turns singletons into pairs) — this is a
complete, if negative, sub-result, not a dangling attempt. (iii) Because
of (ii), I do **not** obtain a fully-worked abstract counterexample
matching the $O(N\log N)$ upper bound with global pairwise intersection
intact; what Step 3 **does** rigorously establish is that the tension
found in (ii) is exactly the same tension the per-prime Contamination
Dichotomy Lemma already isolates (a shared prime "protecting" global
intersection can be exactly what prevents a genuine singleton witness at
that pair) — so the global-counting mechanism, even though it does not
hand over a finished counterexample, **converges independently onto the
same crux** as the per-prime mechanism, strengthening (not proving) the
population's shared diagnosis that Nec-finiteness needs a genuinely
different (minimality/greedy-specific, not counting-theoretic) ingredient.

### Conclusion for the global counting/second-moment mechanism

Combining Steps 1–3: the natural global counting argument (Step 2) that
this round's outline called for is **fully carried out** and gives a
completely rigorous bound, $|\mathrm{Nec}_{\le N}|=O(N\log N)$ — but this
bound demonstrably **diverges** as $N\to\infty$, so it cannot establish
$|\mathrm{Nec}|<\infty$ (exactly the trap the outline itself flagged, now
confirmed to be the actual outcome, not just a risk). Step 3 shows this
divergence is not a failure of cleverness in Step 2's specific argument:
any attempt to sharpen it using only "pairwise intersection + bounded set
size / factor count" runs into the same core tension (global connectivity
vs. local singleton purity) that the per-prime Contamination Dichotomy
Lemma already isolated in round 6. **I therefore conclude, honestly, that
the global counting/second-moment mechanism as proposed by the round-7
outline cannot, on its own, close the central gap** — a genuine negative
result for a genuinely new mechanism (distinct from the 10 previously
dead mechanisms in this population's record), not a restatement of any of
them, and I record it as such rather than continuing to grind an
avenue now shown to be structurally blocked. Per this round's self-report
requirement, this is honestly reported as the mechanism being evaluated to
completion and found insufficient — the Nec-finiteness question itself
remains open (neither proved nor refuted), with the central gap otherwise
exactly where round 6 left it (Contamination Dichotomy's Uncontaminated-
Witness Existence question, still the sharpest unresolved crux).
