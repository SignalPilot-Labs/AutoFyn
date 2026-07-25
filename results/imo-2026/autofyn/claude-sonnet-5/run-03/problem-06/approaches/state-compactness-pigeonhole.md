## Status
partial

## Approaches tried
- Round 1: built the "state-compactness / direct finite-state pigeonhole"
  approach on the *accepted* sequence directly. Proved from scratch: (i)
  well-definedness of the greedy sequence (Lemma 0, now certified as
  `lemmas/existence.md`); (ii) pairwise non-coprimality $\gcd(a_i,a_j)>1$ for
  *every* $i\ne j$ (Lemma 1, certified as `lemmas/pairwise-non-coprimality.md`);
  (iii) every term meets the recurring-prime set $S$ (Lemma D, certified as
  `lemmas/every-term-meets-recurring-set.md`). Gave a conditional finish
  (Lemma 3) via a deterministic map $g:\mathbb Z/L\mathbb Z\to\mathbb
  Z/L\mathbb Z$ and a pigeonhole coincidence of two orbits, correct but
  resting on two unproved hypotheses (S finite; S-hitting exactly governs
  validity eventually). Flagged, honestly, a second gap: extending the
  eventually-periodic relation down to every $n\ge 1$. Status: partial.
- Round 2 (this round): the outline-reviewer refuted the round-1 target
  "$S$ is finite" outright (see below) and redirected this approach to a
  genuinely different bookkeeping device: periodicity of the **complement
  set** $B=\mathbb Z_{>1}\setminus\{a_n\}$ (the rejected integers), rather
  than of the difference sequence $a_{n+1}-a_n$. This round I built that
  framing out in full. New content, all proved from scratch and independent
  of the round-1 write-up:
  - A strictly simpler, **unconditional** finite covering set $Q_0:=R(a_1)$
    (no pigeonhole needed at all — it is immediate from the $i=1$ clause of
    the definition), replacing the pigeonhole-derived $S$ as the object to
    build the finite "type space" on.
  - A fully rigorous **set-theoretic reformulation of acceptance**
    (Proposition B below): $m$ is accepted iff $m=a_1$ or $m>a_1$ and $m$ is
    coprime to no earlier-accepted term — proved by an honest two-directional
    argument from the greedy minimality, not merely asserted.
  - A clean, **self-contained combinatorial lemma** (Lemma P: "a union of
    finitely many residue classes mod $L$, listed in increasing order, is
    *exactly* $T$-periodic with common increment $L$ from its very first
    element" — no pigeonhole-orbit-coincidence argument needed at all).
  - A **streamlined conditional theorem**: granting the same open hypothesis
    the whole population needs (here named Hypothesis SS, the "self-sufficiency"
    hypothesis), the complement/set-theoretic route reproduces the eventual
    periodicity conclusion by a shorter, more transparent argument than the
    round-1 orbit-pigeonhole device, and moreover shows directly that the
    *set* $A\cap(a_{n^*},\infty)$ is a union of full residue classes mod $L$,
    which is a strictly cleaner structural statement than "eventually the
    increments repeat."
  - This round I also checked, and rejected, a natural attempted fix for
    Gap 2 specific to this framing (comparing the true greedy process to an
    alternate process run with the *final* stabilized type family from the
    start) — documented honestly below as a genuine, checked negative
    finding, not glossed over.
  Outcome: Gap 1 (the self-sufficiency/termination lemma) and Gap 2 (prefix
  extension) both remain open; this round narrows and cleans up the
  conditional machinery but does not close either gap. Status remains
  `partial`, exactly as flagged by the outline-reviewer ("a second,
  independent route to the same open lemma, useful as a cross-check, not an
  independent closure").
- Round 3 (this round): built out the outline-reviewer's certified
  Self-Type-Compatibility Lemma into a full **Reduction Lemma** (new,
  §9.3): Hypothesis SS$(Q,1)$ (the rule holding from the very first term) is
  **exactly equivalent** to the single statement "every accepted term $a_n$
  is itself $Q$-Good" (i.e. $\mathcal T$ is a pairwise-intersecting family
  realized by every actual term, not just $a_1$) — proved as a clean
  if-and-only-if, both directions fully rigorous. Combined this with a
  **transient-free finishing theorem** (§9.4): given this single statement
  for *some* finite $Q\supseteq Q_0$, the full target conclusion
  $a_{n+T}=a_n+L$ for *every* $n\ge1$ (no exceptions, no transient) follows
  directly via Lemma P applied with $c=a_1-1$ (covering the entire sequence
  $A$ at once, not just a tail). This **collapses the previously separately-
  tracked Gap 1 (self-sufficiency) and Gap 2 (prefix extension) into one
  single open statement**, the "Unified Central Claim": does there exist a
  finite set of primes $Q$ such that every two terms $a_i,a_j$ of the
  sequence share a prime factor in $Q$? Ran numerical checks (§9.5) across 15
  values of $a_1$, confirming this claim with $Q=R(L)$ (the eventual
  period's prime support) holds with zero exceptions in every tested
  instance (including an exhaustive pairwise check for $a_1=15$ over the
  first 80 terms) — strong evidence, explicitly flagged as evidence, not
  proof, since it uses the sequence's own empirically-observed period to
  define $Q$, which is circular for an actual proof. The Unified Central
  Claim itself is not proved this round; it is the single remaining gap.
  Status remains `partial`.
- Round 5 (this round): assigned target "redundant-covering density" (does
  hitting-multiplicity $\ge2$, or some density mechanism, block further
  growth of $\mathrm{Nec}$ beyond a finite stage?). Proved, fully and
  unconditionally, a genuinely new structural fact not previously in the
  population — the **Multiple-of-$R$ Realization Lemma**: every multiple of
  $R:=\mathrm{rad}(a_1)$ exceeding $a_1$ is *itself* an accepted term of the
  sequence (not merely a legal candidate, as the older `bounded-gap-via-rad-a1.md`
  showed — the stronger claim that it is *actually accepted*). Built on this
  a **Same-Class-Free Lemma / Class-Partition Reduction**: partitioning
  indices by a deterministic choice of "owning prime" in $P:=R(a_1)$ shows
  every *same-class* pair is automatically $Q_{\min}$-hit for free, and any
  prime witnessing $\mathrm{Nec}$ via a same-class pair must already lie in
  $P$ — so $\mathrm{Nec}\setminus P$ can only ever be witnessed by
  cross-class pairs. Tested computationally whether this shrinks the
  remaining difficulty to a finite residual problem: it does **not** — the
  set of "$P$-problematic" pairs (pairs sharing no prime of $P$ at all) is
  large and growing across the tested range (thousands of instances among
  the first 400 terms, no sign of finiteness), so this reduction, while
  correct and new, does not by itself resolve the central gap. Then directly
  tested the specific redundant-covering-density mechanism proposed in the
  round-5 outline (bounded index-gap for a fixed prime's divisibility index
  set, which would drive a multiplicity-$\ge2$ argument) and **refuted it**
  with a complete, fully hand-verified (every step derived from the raw
  recursive definition, all $8$ terms checked by hand against every earlier
  term) counterexample at $a_1=385=5\cdot7\cdot11$: the prime $5$ divides
  $a_2=390$ and next divides $a_8=420$, an index gap of $6>5=p$. This is a
  genuine, honest negative result on the specific mechanism the outline
  proposed (bounded-by-$p$ index gaps), not a strawman — it is the smallest
  counterexample found by a systematic search, small enough to verify every
  step by hand. The central existence gap remains open; this round's
  contribution is a solid new unconditional structural lemma (promotable)
  plus a real narrowing/refutation of the specific mechanism assigned.
  Status remains `partial`.
- Round 4 (this round): built the **Hitting-Set Lemma** (§10.1, certified
  sound by the round-4 outline-reviewer) into an explicit, concrete,
  $a_1$-only-dependent candidate — the **Bounded-Radical Hitting-Set
  Claim** ($Q=\{p\le\mathrm{rad}(a_1)\}$ always works) — proved it in two
  genuine special cases ($i=1$, via the certified Self-Type-Compatibility
  Corollary; adjacent pairs, via the certified Adjacent-Link Lemma), and
  then **decisively refuted it in general** via a complete, fully
  hand-verified (not merely computer-asserted) counterexample at
  $a_1=375$: the sequence's first seven terms are derived by hand from the
  raw recursive definition, and $a_3=380=2^2\cdot5\cdot19$,
  $a_7=399=3\cdot7\cdot19$ are shown to share *only* the prime $19$, which
  exceeds $R=\mathrm{rad}(375)=15$ — so $R(a_3)\cap R(a_7)\cap[2,R]=
  \emptyset$, refuting the claim outright. Checked (computationally, as a
  sanity check, not a proof step) that the underlying incremental
  recruitment construction of §10.2 is *not* refuted by this example — it
  still terminates on $a_1=375$, producing $Q=\{2,3,5,7,19\}$. Also
  documented two general negative findings preventing future rounds from
  repeating dead-end proof strategies: (a) a "single-small-prime
  replacement" minimality argument cannot work because no single prime
  (unlike the full $Q_0$-baseline) guarantees legality against *every*
  earlier term simultaneously; (b) an "adjacent-chain transitivity"
  induction strategy is impossible *in general*, by a pure set-theoretic
  obstruction (consecutive pairwise intersection of a chain of sets does
  not imply the endpoints intersect — exhibited both abstractly and via
  actual sequence data, e.g. $a_1=15$ has $50$ instances among the first
  $100$ terms where adjacent $Q_0$-types are disjoint). This is a sixth
  ruled-out mechanism for the population's shared central gap (after the
  $g(Q)$ threshold, prime-size threshold, $\Lambda$-split, windowed-
  $\epsilon_n$-automaton, and now the closed-form Bounded-Radical
  candidate). The central gap (does §10.2's recruitment terminate for
  *every* $a_1$?) remains fully open; this round's honest contribution is
  ruling out the most attractive available shortcut and pinning down
  exactly why the two most natural proof strategies for it cannot work,
  rather than a further-unverified positive claim. Status remains
  `partial`.
- Round 6 (this round): hand-traced the assigned outlier instance
  $a_1=20735=5\cdot11\cdot13\cdot29$ (new §13). Computed the exact witness
  pair for its slow $\mathrm{Nec}$-element $19$ ($a_4=20748=2^2\cdot3\cdot7
  \cdot13\cdot19$, $a_{70}=21185=5\cdot19\cdot223$, verified by direct
  factorization) and identified the precise combinatorial cause of the
  delay: five consecutive multiples of $19$ in the sequence
  ($a_{13},a_{27},a_{41},a_{55}$) each "accidentally" also carry one of
  $a_4$'s other four prime factors $\{2,3,7,13\}$ (the *obstruction set*),
  before the sixth multiple ($a_{70}$) finally avoids all four. Cross-
  checked this "obstruction-set size drives witness delay" diagnosis
  against the two previously-fast seeds $a_1=385$ (obstruction set size
  $2$, delay $2$ trials) and $a_1=194287$ (obstruction set size $3$, delay
  $2$ trials): order-of-magnitude consistent with a heuristic independent-
  avoidance probability model in all three cases, but **explicitly not
  turned into a proof or a bound** — the round honestly identifies a
  potential obstruction-set-size feedback loop (the obstruction set's size
  grows as more primes are recruited, which could make future delays grow
  without a priori bound) as the reason no simple closed-form bound is
  found, rather than asserting an unproved one. No new certified lemma
  results (this is diagnostic content, not a proof); the central gap
  remains fully open. Status remains `partial`.
- Round 7 (this round): built out the round-7 outline's "Generalized
  Multiple-of-$r$ Realization Lemma via CRT-positive-density," with the
  outline-reviewer's mandate to actually prove (or honestly fail to prove)
  the density-to-bounded-index **bridging step**, not just restate CRT
  density. Result: the bridging step is **not closed**, but this round
  produces two genuinely new, fully rigorous pieces of content that pin
  down *exactly* why it resists closure, going well beyond "this looks as
  hard as the original gap" (the honest assessment recorded through round
  6). (1) A clean **Impossibility Lemma** (new §14.1): the literal
  mechanism proposed in the outline (forcing the target integer to also be
  a multiple of $\mathrm{rad}(a_1)$, so as to reuse the already-certified
  Multiple-of-$R$ Realization Lemma for acceptance) is **provably vacuous**
  for the intended purpose whenever the reference index $i$ has
  $R(a_1)\subseteq R(a_i)$ — an explicit, infinite, and easily-described
  family of indices (includes $i=1$ always, and every index of the
  Multiple-of-$R$ subsequence) — because forcing $\mathrm{rad}(a_1)\mid x$
  *automatically* reintroduces a shared $R(a_1)$-prime between $a_i$ and
  $x$, so $x$ can never realize a **singleton** intersection $\{r\}$ with
  $a_i$; independently confirmed by a from-scratch hand computation
  ($a_1=35$, $i=1$, $r=3$: every integer up to $390$ that is a multiple of
  $3$ and avoids $R(a_1)=\{5,7\}$ entirely is rejected by the sequence,
  with zero exceptions, exactly as the lemma predicts, since avoiding
  $\{5,7\}$ entirely means failing Lemma $Q_0$ against $a_1$ itself). (2)
  For the genuinely different, non-vacuous version of the mechanism (a
  "clean" multiple of $r$ relative to a reference index $i$ with
  $R(a_1)\not\subseteq R(a_i)$, *not* forced to be a multiple of
  $\mathrm{rad}(a_1)$), I hand-verify a concrete counterexample (new §14.2)
  showing that CRT-cleanliness (avoiding the contaminant set $E_i$) plus
  even *additionally* hitting $R(a_1)$ (needed for Lemma $Q_0$) is still
  **not sufficient** for acceptance: for $a_1=35$, $i=2$ ($a_2=40=2^2\cdot
  5$, so $r=2$, $E_2=\{5\}$), the integer $x=56=2^3\cdot7$ is divisible by
  $r=2$, avoids the sole contaminant $5$, and even hits $R(a_1)=\{5,7\}$
  via $7$ (so it clears *both* filters the outline's mechanism controls) —
  yet $x=56$ is rejected, because $\gcd(56,45)=1$ where $a_4=45=3^2\cdot5$
  is a *different* earlier term the mechanism's finite exclusion set never
  accounted for (verified fully by hand). This shows explicitly, with a
  real hand-checked instance (not just an abstract circularity warning),
  that legality is a conjunction against the *entire, unboundedly growing*
  prefix, while any CRT-density construction can only ever encode finitely
  many of those constraints (the ones from the one chosen reference pair)
  — the fundamental, structural reason the bridging step cannot be closed
  with the tools certified so far. Status remains `partial`; this round's
  honest contribution is a full closure of one specific instantiation of
  the mechanism (§14.1, a genuine kill) plus a sharpened, hand-verified
  diagnosis of exactly where the general version breaks (§14.2), rather
  than an unproved "still open" placeholder.

## Current best

**Pointer (round 7):** the furthest correct progress overall remains §12
(round 5)'s Multiple-of-$R$ Realization Lemma and Class-Partition
Reduction — still the sharpest unconditional structural facts in this
approach. Round 7 (§14, new) does not close the central gap, but pins down
precisely why this round's assigned mechanism (CRT-positive-density
bridging for a recruited prime $r$) cannot be pushed through with the
tools certified so far: §14.1 proves the mechanism is **vacuous** (not
merely unproved) whenever the reference index has $R(a_1)\subseteq
R(a_i)$ (an explicit infinite family, e.g. every index of the Multiple-
of-$R$ subsequence), and §14.2 hand-verifies a concrete instance
($a_1=35$, $x=56$) showing that even outside that vacuous family, passing
every filter the CRT-density mechanism controls (divisibility by $r$,
avoiding the finite contaminant set, hitting $R(a_1)$) is still not
sufficient for acceptance, because legality is a conjunction against the
*entire, unboundedly growing* prefix, of which any single reference pair's
exclusion set only encodes a finite piece. The central existence gap
(does a finite self-sufficient $Q$ exist / is $\mathrm{Nec}$ finite) itself
remains **completely open** after this round.

**Pointer (round 6, superseded above for headline purposes, kept for
context):** the furthest correct progress overall remains §12
(round 5)'s Multiple-of-$R$ Realization Lemma and Class-Partition
Reduction; round 6 (§13) adds a hand-checked diagnostic case study
(the $a_1=20735$ outlier's witness-delay mechanism) that explains, but does
not bound, why the central gap's recruitment process can be slow — see
§13.4 for the precise honest summary of what is and is not established.

**Pointer (round 5):** the furthest correct progress this round is §12
below. It contains a genuinely new, fully proved, unconditional structural
fact (the Multiple-of-$R$ Realization Lemma: every multiple of
$R=\mathrm{rad}(a_1)$ exceeding $a_1$ is an accepted term) and a clean
reduction (Class-Partition Reduction) isolating exactly which pairs of
terms can ever need a primes outside $P=R(a_1)$ to be covered. The central
gap (existence of a finite self-sufficient $Q$) is **still open**: the
"problematic pair" set the reduction leaves behind is shown (computationally)
to be infinite in every tested range, and the specific "bounded index-gap"
density mechanism proposed by the round-5 outline is refuted by a small,
fully hand-verified counterexample ($a_1=385$). See §12.5 for the precise
current state. The sections below (§§0–11) record the population's shared
machinery and rounds 3-4 results, unchanged.

### 0. Imported certified lemmas (not reproved here)
- **Lemma 0 (existence)** — `lemmas/existence.md`: the greedy sequence is
  well-defined and strictly increasing.
- **Lemma 1 (pairwise non-coprimality)** — `lemmas/pairwise-non-coprimality.md`:
  $\gcd(a_i,a_j)>1$ for all $i\ne j$.
- **Bounded-gap lemma** — `lemmas/bounded-gap-via-rad-a1.md`: writing
  $Q_0:=R(a_1)$ (the set of distinct prime factors of $a_1$) and
  $\mathrm{rad}(a_1)=\prod_{p\in Q_0}p$, this lemma's internal *Fact* already
  establishes: **for every $n\ge 1$, $R(a_n)\cap Q_0\ne\emptyset$** (proof:
  $n=1$ is immediate since $Q_0=R(a_1)$; for $n\ge2$, applying the definition
  at step $n-1\ge1$ with constraint index $i=1$ gives $\gcd(a_n,a_1)>1$, so
  $a_n$ shares a prime with $a_1$, i.e. a prime of $Q_0$). We refer to this
  as **Lemma $Q_0$** below; it needs no further proof, only restating for
  emphasis, since it is the load-bearing fact for everything that follows.
- **"Every term meets $S$" lemma** — `lemmas/every-term-meets-recurring-set.md`
  (referenced for context; superseded for our purposes by Lemma $Q_0$ above,
  which is unconditional and requires no pigeonhole, since $Q_0=R(a_1)$ is
  already known and finite the moment $a_1$ is fixed).

Throughout, for $m>1$ write $R(m)$ for the (finite, nonempty) set of prime
divisors of $m$, so $\gcd(x,y)>1 \iff R(x)\cap R(y)\ne\emptyset$.

### 1. Why this round targets $Q_0$, not $S$ (the population-wide reframe)

The round-1 target "$S:=\{p:p\mid a_n\text{ for infinitely many }n\}$ is
finite" is **refuted**, not merely unproved (this was checked and confirmed,
independently, by the outline-reviewer and by other approaches in the
population this round): *if* the desired conclusion $a_{n+T}=a_n+L$ holds for
all $n\ge n_0$, then for any prime $p\nmid L$, $p$ is invertible mod $L$... — more
precisely, fixing a residue class $r$ mod $T$, the sub-progression
$a_r,a_{r+T},a_{r+2T},\dots$ has common difference $L$; since $\gcd(L,p)=1$
for $p\nmid L$, the map $j\mapsto a_r + jL \pmod p$ is a bijection of
$\mathbb Z/p\mathbb Z$ as $j$ ranges over $0,\dots,p-1$ (multiplication by the
unit $L$), so it hits residue $0$ for some $j$, forcing $p\mid a_{r+jT}$.
Hence **every prime not dividing $L$ already lies in $S$**, i.e. $S$ is
cofinite in the primes, purely as a *consequence* of the periodicity we are
trying to prove — it can never be shown finite. This means "$S$ finite" was
the wrong finite object to chase from the start; the correct finite object is
$L$ itself (equivalently its prime support), and it must be produced by a
recruitment/self-sufficiency argument, not an infinite-tail counting
argument on $S$. We therefore replace $S$ throughout by an explicit finite
set $Q\supseteq Q_0$ that is a candidate for $R(L)$, and by Lemma $Q_0$ above
we no longer need any pigeonhole step just to exhibit *some* finite covering
set — $Q_0=R(a_1)$ already works as a starting point, unconditionally.

### 2. The complement-set reformulation

Let $A:=\{a_n : n\ge1\}$ (the accepted set) and $B:=\mathbb Z_{>1}\setminus A$
(the rejected set). Since $(a_n)$ is strictly increasing (Lemma 0), for
$m>a_1$ define
$$\mathrm{Good}(m) :\iff \gcd(m,a_i)>1 \text{ for every } i\ge1 \text{ with } a_i<m.$$

**Proposition B (set-theoretic characterization of acceptance).** For every
integer $m>a_1$: $m\in A \iff \mathrm{Good}(m)$.

*Proof.*

($\Rightarrow$) Suppose $m=a_n\in A$ for some $n$; since $m>a_1$ and $(a_n)$
is strictly increasing, $n\ge2$. For any $i\ge1$ with $a_i<m=a_n$, strict
monotonicity of $(a_n)$ forces $i<n$, i.e. $i\le n-1$. By the defining
property of the sequence applied at step $n-1$, $a_n$ satisfies
$\gcd(a_n,a_i)>1$ for every $i=1,\dots,n-1$; in particular for our $i$. Hence
$\mathrm{Good}(m)$ holds.

($\Leftarrow$) Suppose $\mathrm{Good}(m)$ holds for some $m>a_1$. Since
$a_1<m$ and $a_n\to\infty$ (strictly increasing sequence of integers), the
set $\{n\ge1 : a_n<m\}$ is a nonempty finite set of positive integers; let
$n$ be its largest element (so $a_n<m$ and, by maximality of $n$,
$a_{n+1}\ge m$). We show $m=a_{n+1}$, which gives $m\in A$.

Suppose, for contradiction, $m\ne a_{n+1}$; combined with $a_{n+1}\ge m$ this
gives $a_n<m<a_{n+1}$. By definition, $a_{n+1}$ is the *smallest* integer
exceeding $a_n$ with $\gcd(\cdot,a_i)>1$ for every $i=1,\dots,n$. Since $m$ is
a smaller integer than $a_{n+1}$ that also exceeds $a_n$, minimality of
$a_{n+1}$ forces $m$ to **fail** this condition: there exists some
$i_0\in\{1,\dots,n\}$ with $\gcd(m,a_{i_0})=1$. But $a_{i_0}\le a_n<m$ (since
$i_0\le n$ and the sequence is increasing), so $i_0$ is an index with
$a_{i_0}<m$ and $\gcd(m,a_{i_0})=1$ — this directly contradicts
$\mathrm{Good}(m)$. Hence $m=a_{n+1}\in A$. $\blacksquare$

This is new, fully rigorous content: it converts membership in $A$ (a
recursively-defined, order-dependent notion) into a *static* predicate
$\mathrm{Good}(m)$ that can be analyzed set-theoretically, which is exactly
what makes the complement-set framing usable.

### 3. A general combinatorial lemma: exact periodicity of a union of residue classes

**Lemma P.** Let $L\ge1$ be an integer, $\emptyset\ne \mathrm{GoodRes}
\subseteq \mathbb Z/L\mathbb Z$, and $c\ge0$ an integer. Let
$$C:=\{m\in\mathbb Z_{>c} : m \bmod L \in \mathrm{GoodRes}\},$$
listed in increasing order as $c_1<c_2<c_3<\cdots$ (an infinite set, since
each of the $|\mathrm{GoodRes}|\ge1$ residue classes mod $L$ contributes an
infinite arithmetic progression). Let $T:=|\mathrm{GoodRes}|$. Then
$$c_{j+T} = c_j + L \quad\text{for every } j\ge1.$$

*Proof.* Define $\varphi:C\to \mathbb Z$ by $\varphi(x)=x+L$. If $x\in C$
then $x>c$ so $x+L>c$, and $(x+L)\bmod L = x\bmod L\in\mathrm{GoodRes}$, so
$\varphi(x)\in C$; thus $\varphi$ maps $C$ into $C$, and in fact into
$C':=C\cap(c+L,\infty)$ (since $x>c\Rightarrow x+L>c+L$). Moreover $\varphi$
is injective (it's a translation) and strictly increasing.

$\varphi:C\to C'$ is **surjective**: given $y\in C'$, $y>c+L$, so
$y-L>c$; and $(y-L)\bmod L = y\bmod L\in\mathrm{GoodRes}$, so $y-L\in C$, and
$\varphi(y-L)=y$. Hence $\varphi$ is an order-preserving bijection $C\to C'$.

The interval $(c,c+L]$ consists of exactly $L$ consecutive integers, hence
contains exactly one representative of each residue class mod $L$; exactly
$T=|\mathrm{GoodRes}|$ of these representatives lie in $C$. Since every
element of $C$ either lies in $(c,c+L]$ or exceeds $c+L$ (i.e. lies in $C'$),
we conclude $C\setminus C' = C\cap(c,c+L]$ has exactly $T$ elements, i.e.
$C' = \{c_j : j>T\} = \{c_{T+1},c_{T+2},\dots\}$.

Now we show by induction on $j\ge1$ that $\varphi(c_j)=c_{j+T}$.
*Base case* ($j=1$): $c_1=\min C$, so $\varphi(c_1)=\min \varphi(C) = \min C'$
(as $\varphi$ is an order-preserving bijection onto $C'$, it sends the least
element of $C$ to the least element of $C'$) $= c_{T+1}$ (since
$C'=\{c_{T+1},c_{T+2},\dots\}$ listed increasingly).
*Inductive step*: assume $\varphi(c_j)=c_{j+T}$. Since $c_{j+1}$ is, by
definition, the smallest element of $C$ exceeding $c_j$, and $\varphi$ is a
strictly increasing bijection $C\to C'$, $\varphi(c_{j+1})$ is the smallest
element of $C'$ exceeding $\varphi(c_j)=c_{j+T}$. But $C'=\{c_{T+1},c_{T+2},
\dots\}$ listed increasingly, and $c_{j+T}\in C'$ (as $j+T>T$), so the
smallest element of $C'$ exceeding $c_{j+T}$ is precisely the next term in
that listing, $c_{j+T+1}=c_{(j+1)+T}$. Hence
$\varphi(c_{j+1})=c_{(j+1)+T}$, completing the induction.

Thus $c_j + L = \varphi(c_j) = c_{j+T}$ for every $j\ge1$. $\blacksquare$

This is a self-contained, purely combinatorial fact (no dependence on the
sequence $(a_n)$ at all) that will replace the round-1 orbit-pigeonhole
argument (Lemma 3 of the round-1 write-up) once we know $A$'s tail is such a
union of residue classes — it gives **exact** periodicity of the listing
from its very first indexed element, with no separate "two orbits coincide"
step needed.

### 4. The finite type space for a general covering set $Q\supseteq Q_0$

Fix any finite set of primes $Q\supseteq Q_0=R(a_1)$ (candidates: $Q_0$
itself, or an enlargement of it — which enlargement, if any, is required is
exactly Gap 1 below). By Lemma $Q_0$, $R(a_i)\cap Q_0\ne\emptyset$ for every
$i\ge1$, and since $Q_0\subseteq Q$, also $R(a_i)\cap Q\ne\emptyset$ for
every $i\ge1$. Define the **$Q$-type** of index $i$:
$$\tau_i := R(a_i)\cap Q \ \in\ 2^Q\setminus\{\emptyset\},$$
a nonempty subset of $Q$, and let $\mathcal T := \{\tau_i : i\ge1\}$, the
(a priori infinite-indexed, but automatically finite-valued) set of all
types that occur.

**Lemma 2$'$ (type stabilization, unconditional for any fixed finite
$Q\supseteq Q_0$).** $\mathcal T\subseteq 2^Q\setminus\{\emptyset\}$ is
finite ($|\mathcal T|\le 2^{|Q|}-1$), and there is a finite index $n_1(Q)$
such that $\{\tau_i : i\le n_1(Q)\} = \mathcal T$.

*Proof.* $2^Q\setminus\{\emptyset\}$ is finite since $Q$ is finite, and
$\mathcal T$ is a subset of it, hence finite. Since $\mathcal T$ is by
definition the set of *all* values the function $i\mapsto\tau_i$ ever takes,
only finitely many indices $i$ can be "first occurrences" of a value not
already among $\tau_1,\dots,\tau_{i-1}$ — at most $|\mathcal T|$ many, since
each first occurrence uses up one element of the finite set $\mathcal T$
that has not yet been used. Let $n_1(Q)$ be the largest such first-occurrence
index (or $1$ if $\mathcal T=\{\tau_1\}$). By index $n_1(Q)$, every element
of $\mathcal T$ has occurred among $\tau_1,\dots,\tau_{n_1(Q)}$. $\blacksquare$

Define $L:=L(Q):=\prod_{q\in Q}q$ and, for $m\in\mathbb Z_{>1}$,
$$\mathrm{Good}_Q(m) :\iff R(m)\cap Q \text{ meets every } \tau\in\mathcal T.$$
By the Chinese Remainder Theorem, divisibility of $m$ by a fixed prime
$q\in Q$ depends only on $m\bmod q$, so $R(m)\cap Q$ (and hence
$\mathrm{Good}_Q(m)$, since $\mathcal T$ is now fixed once $Q$ is fixed) is
determined entirely by $m \bmod L$; thus $\mathrm{Good}_Q$ defines a fixed
subset $\mathrm{GoodRes}(Q)\subseteq \mathbb Z/L\mathbb Z$.

**Lemma S1 (sufficiency of $Q$-type-hitting — unconditional).** For every
$m>1$: if $\mathrm{Good}_Q(m)$ holds, then $\mathrm{Good}(m)$ holds (in the
sense of §2, i.e. $\gcd(m,a_i)>1$ for *every* $i\ge1$ with $a_i<m$).

*Proof.* Let $i\ge1$ with $a_i<m$. Then $\tau_i\in\mathcal T$ by definition
of $\mathcal T$, so by hypothesis $R(m)\cap Q$ meets $\tau_i = R(a_i)\cap Q$;
pick a common prime $q$ in both. Then $q\mid m$ and $q\mid a_i$, so
$\gcd(m,a_i)\ge q>1$. $\blacksquare$

Note $\mathrm{GoodRes}(Q)\ne\emptyset$: the residue $0$ (any multiple of
$L$) is divisible by every prime of $Q$, so $R(m)\cap Q = Q$ meets every
nonempty subset $\tau\subseteq Q$, in particular every $\tau\in\mathcal T$.

### 5. Hypothesis SS (the single remaining central gap) and the conditional theorem

**Hypothesis SS($Q,n^*$).** There is a finite set of primes $Q\supseteq Q_0$
and an index $n^*\ge n_1(Q)$ such that for every $n\ge n^*$,
$$a_{n+1} = \min\{\, m>a_n : \mathrm{Good}_Q(m) \,\}.$$

(By Lemma S1, the right-hand candidate set is always a *subset* of the true
candidate set $\{m>a_n:\mathrm{Good}(m)\}$ used implicitly by the recursive
definition restricted via Proposition B, so the true $a_{n+1}$ is always
$\le$ the right-hand minimum; Hypothesis SS asserts *equality holds from
$n^*$ on* — i.e. that eventually no candidate using a prime outside $Q$ ever
undercuts the guaranteed $Q$-hitting candidate. This is exactly the
"self-sufficiency" content that `jacobsthal-covering-bound.md` also isolates
as its own central open lemma, approached here from the complement/set
side rather than from a phase-induction/recruitment side. **This hypothesis
is not proved by this approach, nor by any approach in the current
population** — it is recorded honestly as Gap 1.)

**Theorem (conditional periodicity of the tail, via the complement set).**
Assume Hypothesis SS($Q,n^*$) holds, with associated $L=L(Q)$,
$\mathrm{GoodRes}=\mathrm{GoodRes}(Q)$, $T:=|\mathrm{GoodRes}|\ge1$. Then
there is an index $m_0\ge n^*$ such that
$$a_{n+T} = a_n + L \quad\text{for every } n > m_0.$$

*Proof.* **Step 1 (the tail of $A$ is exactly $Q_0$-Good).** We claim
$$A\cap(a_{n^*},\infty) \;=\; \{m>a_{n^*} : \mathrm{Good}_Q(m)\}. \tag{$\ast$}$$

($\subseteq$) If $m=a_{n+1}\in A$ with $m>a_{n^*}$, then, since $(a_n)$ is
increasing and $a_{n^*}<m=a_{n+1}$, we have $n\ge n^*$ (if $n<n^*$ then
$a_{n+1}\le a_{n^*}$, a contradiction — more precisely if $n+1\le n^*$ then
$m=a_{n+1}\le a_{n^*}$; since $m>a_{n^*}$ this forces $n+1>n^*$, i.e.
$n\ge n^*$). By Hypothesis SS, $a_{n+1}=\min\{m'>a_n:\mathrm{Good}_Q(m')\}$,
so in particular $\mathrm{Good}_Q(a_{n+1})=\mathrm{Good}_Q(m)$ holds (the
minimum itself satisfies the defining predicate).

($\supseteq$) Suppose $m>a_{n^*}$ and $\mathrm{Good}_Q(m)$ holds. Since
$a_n\to\infty$, let $n\ge n^*$ be the largest index with $a_n<m$ (exists:
the set of $n$ with $a_n<m$ is nonempty, as $a_{n^*}<m$, and finite; its
largest element is $\ge n^*$ since $a_{n^*}<m$ means $n^*$ itself is among
the candidates, or a larger index is). If $n\ge n^*$ we may apply Hypothesis
SS: $a_{n+1}=\min\{m'>a_n : \mathrm{Good}_Q(m')\}$. Since $m>a_n$ and
$\mathrm{Good}_Q(m)$ holds, $m$ is one of the candidates in this minimum, so
$a_{n+1}\le m$. On the other hand, by maximality of $n$ (largest index with
$a_n<m$), we get $a_{n+1}\ge m$ (if $a_{n+1}<m$ then $n+1$ would also satisfy
$a_{n+1}<m$, contradicting maximality of $n$). Combining, $a_{n+1}=m$, so
$m\in A$. This proves ($\ast$).

**Step 2 (translate to residues).** Since $\mathrm{Good}_Q(m)$ depends only
on $m\bmod L$ (via $\mathrm{GoodRes}$), ($\ast$) reads
$$A\cap(a_{n^*},\infty) = \{m>a_{n^*} : m\bmod L\in \mathrm{GoodRes}\},$$
exactly the set $C$ of Lemma P with $c=a_{n^*}$.

**Step 3 (apply Lemma P).** Let $m_0$ be the number of indices $n$ with
$a_n\le a_{n^*}$ (so $m_0\ge n^*$, and $A\cap(a_{n^*},\infty) =
\{a_{m_0+1},a_{m_0+2},\dots\}$, i.e. $c_j = a_{m_0+j}$ for $j\ge1$ in the
notation of Lemma P). Lemma P gives $c_{j+T}=c_j+L$ for every $j\ge1$, i.e.
$a_{m_0+j+T} = a_{m_0+j}+L$ for every $j\ge1$. Reindexing $n:=m_0+j$ (ranging
over all integers $>m_0$ as $j$ ranges over all positive integers) gives
$$a_{n+T} = a_n + L \quad\text{for every } n>m_0. \qquad\blacksquare$$

This reproves the population's shared conditional conclusion (eventual
periodicity, given a self-sufficiency hypothesis), but via a strictly
shorter route than the round-1 orbit-pigeonhole argument (no need to find a
coincidence of two state-orbits and telescope increments — Lemma P gives
exact periodicity of the *set* $A$'s tail directly, from its very first
listed element beyond $a_{n^*}$). It is genuinely useful as a cross-check
that the two different bookkeeping devices (difference-sequence pigeonhole
in the round-1 write-up, vs. set-listing periodicity here) agree on the
conditional conclusion — but it rests on exactly the same unproved
Hypothesis SS, so **it is not an independent resolution of Gap 1**, as the
outline-reviewer correctly anticipated.

**Note (superseded by §9 below).** Sections 6–7 record the gap structure as
it stood after round 2 (two separately-tracked gaps, transient index $n^*$
possibly $>1$). Round 3 (§9) proves these are the *same* gap once
$n^*=1$ is targeted directly, and gives a single unified open statement.
Sections 6–7 are kept for the historical record and because they still
correctly describe the *general* difficulty (for arbitrary/wrong $Q$); read
them together with §9's reconciliation note before §9.4.

### 6. Gap 1 (open): proving Hypothesis SS for some finite $Q$

This is the shared central difficulty of the whole population (called the
"self-sufficiency lemma" in `jacobsthal-covering-bound.md`, and the
termination of prime-recruitment in `active-set-stabilization.md`). No
approach, including this one, has proved it. What this round's complement
framing adds is a cleaner *statement* of exactly what must be shown: a
finite set of primes $Q\supseteq Q_0$ and an index $n^*$ such that no
candidate $m$ using a prime outside $Q$ to satisfy some historical
constraint is ever, from $n^*$ on, actually smaller than the guaranteed
$Q$-hitting candidate. Equivalently (via Step 1's proof, run in reverse):
$Q$ fails to be self-sufficient at some $n\ge n_1(Q)$ exactly when some
integer $m$ with $a_n<m<\min\{m'>a_n:\mathrm{Good}_Q(m')\}$ satisfies
$\mathrm{Good}(m)$ (i.e. beats every historical constraint) while failing
$\mathrm{Good}_Q(m)$ (i.e. needs a prime outside $Q$ for at least one
historical constraint) — such an $m$, if it is ever accepted, forces
recruitment of a new prime into the active set. No unconditional bound on
how many times, or how far, such recruitment can happen has been found by
any approach in the population.

### 7. Gap 2 (open): extending periodicity from $n>m_0$ to every $n\ge1$

The theorem of §5 only gives $a_{n+T}=a_n+L$ for $n$ beyond the transient
cutoff $m_0\ge n^*\ge n_1(Q)$; the problem demands it for *every* $n\ge1$.
This is the same secondary gap flagged (independently) by
`active-set-stabilization.md`; here I record a genuine, checked negative
finding specific to the complement-set framing, so it is not attempted
again fruitlessly by a future round on this approach.

**Attempted fix (checked and rejected): comparing to the "stabilized-rule"
process run from the start.** Given Hypothesis SS with data $(Q,n^*)$,
define an auxiliary sequence $(b_n)$ by $b_1=a_1$ and, for $n\ge1$,
$b_{n+1}=\min\{m>b_n : \mathrm{Good}_Q(m)\}$ (i.e. run the *eventual* rule
from the very first step, instead of only from $n^*$ on). One might hope
$b_n=a_n$ for all $n$, which would immediately extend the periodicity to
every $n\ge1$ (since $(b_n)$, being generated by the single fixed rule
$\mathrm{Good}_Q$ throughout, is periodic in exactly the sense of Lemma P
applied with $c=0$, i.e. $T,L$ work for the *whole* sequence $b_1,b_2,\dots$
starting at $n=1$).

This fix **fails in general**, and the reason is structural, not a
computational accident: for $n<n^*$ (before all types in $\mathcal T$ have
appeared among $\tau_1,\dots,\tau_n$), the *true* candidate set for
$a_{n+1}$ is $\{m>a_n:\mathrm{Good}(m)\}$, which by Proposition B only
requires $\gcd(m,a_i)>1$ for the *finitely many already-realized* indices
$i\le n$ — a **weaker** requirement than $\mathrm{Good}_Q(m)$, which (via
$\mathcal T$, defined using *all* indices $i\ge1$) requires hitting every
type that will *ever* occur, including types realized only by later,
not-yet-existing terms. Consequently the true candidate set for $a_{n+1}$
(before stabilization) is a strict superset of the $Q$-Good candidate set,
so $a_{n+1}\le b_{n+1}$ always, but the true minimum $a_{n+1}$ can be, and
typically is, a smaller integer than $b_{n+1}$ that fails to be
$Q$-type-hitting for a type not yet realized — this is, in fact, exactly
*how* new types get realized in the first place (an early term is accepted
precisely because it only had to clear the constraints realized so far, not
the full eventual family $\mathcal T$). So $(a_n)$ and $(b_n)$ genuinely
diverge for small $n$ in general, and no argument of this shape closes Gap
2. This matches the outline-reviewer's independent warning (given to
`active-set-stabilization.md`) against pigeonhole-fallacy "fixes" for this
same gap: the pre-stabilization dynamics are governed by a different
(weaker, and shrinking-in-effect) rule than the post-stabilization one, and
there is no a priori reason the two coincide, nor that the transient
indices lie on the eventual cycle. I record Gap 2 as open, distinct from Gap
1, and note that **both** gaps must be closed (by whichever approach in the
population ultimately resolves Gap 1) before the problem is fully solved.

### 8. Value of this approach relative to the population

Independent of Gaps 1–2, this round contributes, and certifies as reusable:
(a) the observation that $Q_0=R(a_1)$ is already an unconditional finite
covering set, making the pigeonhole-derived $S$ of round 1 unnecessary as a
starting point; (b) Proposition B, a fully rigorous static (set-theoretic)
reformulation of the recursive acceptance rule; (c) Lemma P, a clean,
general, and reusable combinatorial fact (exact — not merely eventual —
periodicity of a listed union of residue classes) that gives a shorter proof
of the conditional finish than the round-1 orbit-pigeonhole device, usable
by any approach that reaches a hypothesis of the shape "eventually,
$\mathrm{Good}$ is governed by hitting a fixed finite type family mod $L$";
(d) a checked, honestly-recorded negative finding on one natural approach to
Gap 2 (the "run the stabilized rule from the start" idea), saving a future
round from re-attempting it.

### 9. Round 3 build: collapsing Gap 1 and Gap 2 into a single Unified Central Claim

This section is new content built this round on top of the outline-reviewer's
certified **Self-Type-Compatibility Lemma** (restated and re-proved below for
self-containedness) and the machinery of §§2–5 above. The main result of this
round: **Gap 1 (self-sufficiency) and Gap 2 (prefix extension) are not two
separate difficulties — they reduce to one single combinatorial statement**,
proved below to be exactly equivalent to full periodicity from $n=1$. This is
a genuine structural simplification, not a re-derivation of the round-2
conditional finish. Numerical experiments across many values of $a_1$ (§9.5)
support the truth of the resulting single statement, but it is **not proved**
here — it is isolated as the one remaining open gap.

#### 9.1 Fact D: the greedy recursion re-expressed via $\mathrm{Good}$, for every $n\ge1$, with no $n^*$

**Fact D.** For every $n\ge1$, $a_{n+1} = \min\{m > a_n : \mathrm{Good}(m)\}$
(where $\mathrm{Good}$ is defined, as in §2, using *all* earlier accepted
terms — but restricted here to indices realized so far).

*Proof.* By the definition of the sequence, $a_{n+1}$ is the smallest integer
exceeding $a_n$ with $\gcd(\cdot,a_i)>1$ for every $i=1,\dots,n$. For any $m$
with $a_n<m<a_{n+1}$ or $m=a_{n+1}$, the set of indices $i$ with $a_i<m$ is
exactly $\{1,\dots,n\}$: indeed $a_i<m$ for $i\le n$ since $a_i\le a_n<m$
(monotonicity, Lemma 0), and $a_i\ge a_{n+1}\ge m$ for $i\ge n+1$ (with
equality only when $i=n+1,m=a_{n+1}$, which is excluded from "$a_i<m$" since
then $a_i=m\not<m$). Hence, for such $m$, $\mathrm{Good}(m)$ (as defined in
§2: $\gcd(m,a_i)>1$ for every $i$ with $a_i<m$) is *literally* the same
condition as "$\gcd(m,a_i)>1$ for $i=1,\dots,n$", which is exactly the
condition the recursive definition tests. So on the range $(a_n,a_{n+1}]$,
$\mathrm{Good}$ and the recursive acceptance test agree pointwise, and
$a_{n+1}$ is by definition the smallest integer in this range passing the
test, i.e. the smallest integer $>a_n$ with $\mathrm{Good}$ true. $\blacksquare$

(This is a strictly more elementary and more general fact than Proposition B:
it holds for *every* $n\ge1$ unconditionally, with no restriction to
$m>a_1$, and needs only the raw recursive definition, not the two-directional
argument of §2. Proposition B remains useful for describing $\mathrm{Good}$
of an arbitrary $m$ independent of any specific index $n$; Fact D is the
sharper, index-local restatement used below.)

#### 9.2 The Self-Type-Compatibility Lemma (re-derived, shared ingredient)

**Self-Type-Compatibility Lemma.** Fix a finite set of primes $Q\supseteq
Q_0=R(a_1)$. If $R(a_i)\subseteq Q$ for some index $i$, then $\tau_i\cap
\tau_j\ne\emptyset$ for every $j\ne i$ (where $\tau_k:=R(a_k)\cap Q$, as in
§4).

*Proof.* By the certified `lemmas/pairwise-non-coprimality.md`,
$\gcd(a_i,a_j)>1$, so there is a prime $p$ with $p\mid a_i$ and $p\mid a_j$.
Since $p\mid a_i$, $p\in R(a_i)$; since $R(a_i)\subseteq Q$, $p\in Q$, so
$p\in R(a_i)\cap Q=\tau_i$ (using $R(a_i)\subseteq Q$ once more: $\tau_i=
R(a_i)\cap Q=R(a_i)$). Also $p\mid a_j$ and $p\in Q$ give $p\in\tau_j$. Hence
$p\in\tau_i\cap\tau_j$. $\blacksquare$

**Corollary (unconditional).** For *every* finite $Q\supseteq Q_0$,
$\mathrm{Good}_Q(a_1)$ holds.

*Proof.* Apply the lemma with $i=1$: since $R(a_1)=Q_0\subseteq Q$ by
hypothesis on $Q$, we get $\tau_1\cap\tau_j\ne\emptyset$ for every $j\ne1$.
Also $\tau_1\cap\tau_1=\tau_1\ne\emptyset$ (nonempty since $a_1>1$ has a prime
factor, which lies in $R(a_1)=Q_0\subseteq Q$). Hence $\tau_1$ meets $\tau_j$
for *every* $j\ge1$, i.e. $\tau_1=R(a_1)\cap Q$ meets every element of
$\mathcal T=\{\tau_j:j\ge1\}$. This is exactly $\mathrm{Good}_Q(a_1)$ (§4
definition, applied at $m=a_1$: $R(a_1)\cap Q$ meets every $\tau\in\mathcal
T$). $\blacksquare$

This matches the outline-reviewer's cross-cutting verification of this lemma
(sound, no pigeonhole, usable independent of type-stabilization index
$n_1(Q)$).

#### 9.3 The Reduction Lemma: Hypothesis SS$(Q,1)$ $\iff$ every accepted term is $Q$-Good

**Reduction Lemma.** Fix a finite $Q\supseteq Q_0$. The following are
equivalent:

(a) **Hypothesis SS$(Q,1)$**: for every $n\ge1$, $a_{n+1}=\min\{m>a_n:
\mathrm{Good}_Q(m)\}$.

(b) **Unified Central Claim for $Q$**: for every $n\ge1$, $\mathrm{Good}_Q
(a_n)$ holds (equivalently: $\tau_n\cap\tau_j\ne\emptyset$ for *every* pair
$n,j\ge1$, i.e. $\mathcal T$ is a *pairwise intersecting family*, and every
term of the sequence itself realizes this — not merely those with
$R(a_i)\subseteq Q$).

*Proof.*

(a)$\Rightarrow$(b): We use strong induction is not even needed: fix $n\ge1$.
If $n=1$, $\mathrm{Good}_Q(a_1)$ holds by the Corollary of §9.2, unconditionally
(no need to invoke (a)). If $n\ge2$, write $n=k+1$ with $k\ge1$; by (a)
applied at index $k$, $a_{k+1}=\min\{m>a_k:\mathrm{Good}_Q(m)\}$. This set is
nonempty: $\mathrm{GoodRes}(Q)\ne\emptyset$ (§4, the residue $0$ always
qualifies), so it contains arbitrarily large multiples of $L(Q)$, in
particular one exceeding $a_k$. A nonempty set of positive integers has a
minimum, and that minimum trivially satisfies the defining predicate of the
set: so $a_{k+1}=\min\{m>a_k:\mathrm{Good}_Q(m)\}$ itself satisfies
$\mathrm{Good}_Q$, i.e. $\mathrm{Good}_Q(a_{k+1})=\mathrm{Good}_Q(a_n)$ holds.

(b)$\Rightarrow$(a): Fix $n\ge1$; we show $a_{n+1}=\mu$ where
$\mu:=\min\{m>a_n:\mathrm{Good}_Q(m)\}$ (which exists by the same
nonemptiness argument as above). By Lemma S1 (§4, unconditional: $\mathrm{Good}_Q
(m)\Rightarrow\mathrm{Good}(m)$ for every $m$), every candidate for $\mu$ is
also a candidate for $\min\{m>a_n:\mathrm{Good}(m)\}=a_{n+1}$ (Fact D, §9.1);
since $\mu$ ranges over a subset of the candidates of the latter minimum,
$\mu\ge a_{n+1}$. Conversely, by (b), $\mathrm{Good}_Q(a_{n+1})$ holds, and
$a_{n+1}>a_n$, so $a_{n+1}$ is itself a candidate for $\mu$, giving
$\mu\le a_{n+1}$. Hence $\mu=a_{n+1}$, i.e. (a) holds at this $n$. As $n\ge1$
was arbitrary, (a) holds for all $n\ge1$. $\blacksquare$

This is the main structural contribution of this round: it shows the
population's central open difficulty (Hypothesis SS, previously stated with
an unspecified transient index $n^*$) is **exactly equivalent**, once
restricted to $n^*=1$, to the single clean statement (b) — no separate
"prefix extension" argument (Gap 2) is needed at all once (b) is established
for *some* finite $Q\supseteq Q_0$: (a) already asserts the rule holds from
$n=1$, not just eventually.

#### 9.4 From the Unified Central Claim to full periodicity for every $n\ge1$

**Theorem (unconditional given the Unified Central Claim).** Suppose there is
a finite set of primes $Q\supseteq Q_0$ such that $\mathrm{Good}_Q(a_n)$
holds for every $n\ge1$ (i.e. (b) of §9.3 holds for $Q$). Let $L=L(Q)$,
$T=|\mathrm{GoodRes}(Q)|\ge1$. Then
$$a_{n+T}=a_n+L\quad\text{for every }n\ge1$$
— exact periodicity from the very first term, with **no transient**.

*Proof.* By the Reduction Lemma, Hypothesis SS$(Q,1)$ holds.

**Step 1: $A=\{m\ge a_1 : \mathrm{Good}_Q(m)\}$.** ($\subseteq$) If $m=a_n\in
A$, $\mathrm{Good}_Q(a_n)$ holds by hypothesis (b), and $a_n\ge a_1$.
($\supseteq$) Suppose $m\ge a_1$, $\mathrm{Good}_Q(m)$. If $m=a_1$, then
$m\in A$ trivially. If $m>a_1$: since $a_n\to\infty$ (Lemma 0) and $a_1<m$,
the set $\{n\ge1:a_n<m\}$ is a nonempty finite set of positive integers
(nonempty since $n=1$ qualifies); let $n$ be its largest element, so
$a_n<m$ and (by maximality) $a_{n+1}\ge m$. By Hypothesis SS$(Q,1)$ at index
$n$, $a_{n+1}=\min\{m'>a_n:\mathrm{Good}_Q(m')\}$; since $m>a_n$ and
$\mathrm{Good}_Q(m)$ holds, $m$ is a candidate, so $a_{n+1}\le m$. Combined
with $a_{n+1}\ge m$ from maximality, $a_{n+1}=m$, so $m\in A$.

**Step 2: translate to residues.** Since $\mathrm{Good}_Q(m)$ depends only on
$m\bmod L$ (§4, by CRT), Step 1 reads
$$A = \{m > a_1-1 : m\bmod L\in\mathrm{GoodRes}(Q)\},$$
i.e. $A$ (the *entire* accepted set, not just a tail) is exactly the set $C$
of Lemma P with $c:=a_1-1$ (a nonnegative integer since $a_1\ge2$).

**Step 3: apply Lemma P.** Listing $C$ in increasing order gives $c_j=a_j$
for every $j\ge1$ (since $A$ listed increasingly *is* $(a_n)_{n\ge1}$ by
definition). Lemma P (§3, exact — not eventual — periodicity) gives
$c_{j+T}=c_j+L$ for *every* $j\ge1$, i.e.
$$a_{n+T}=a_n+L\quad\text{for every }n\ge1. \qquad\blacksquare$$

This is the complete, transient-free finish: **if** some finite $Q\supseteq
Q_0$ satisfying the Unified Central Claim of §9.3(b) can be exhibited, the
problem's target conclusion (Hypothesis SS with $n^*=1$, full periodicity for
every $n\ge1$) follows immediately and completely by the chain
§9.2 $\to$ §9.3 $\to$ this theorem, with every step above fully rigorous and
none of it resting on an unproved auxiliary hypothesis beyond the Unified
Central Claim itself.

#### 9.5 Status of the Unified Central Claim: strong numerical support, no proof

The Unified Central Claim (§9.3(b), for $Q=R(L)$ where $L$ is the sequence's
own eventual common increment) was checked computationally, independently of
the machinery above, for the following values of $a_1$: $9,15,21,25,33,35,
45,49,55,77,85,91,119,121,169$. In every case, using the sequence's own
observed periodic tail to determine $L$ (hence $Q:=R(L)$) and $\mathcal T$
(the set of $Q$-types occurring among the first several hundred terms), the
check
$$A\cap[a_1, N] \;=\; \{m\in[a_1,N] : \mathrm{Good}_Q(m)\}$$
held with **zero exceptions**, checked exhaustively for every integer $m$ in
range (not just at the $a_n$ themselves), for $N$ up to several hundred and
often the first 100+ terms of the sequence. In particular, for $a_1=15$
($Q=\{2,3,5\}$, $L=30$, $\mathcal T=\{\{2,5\},\{2,3,5\},\{2,3\},\{3,5\}\}$),
every one of the $\binom{40}{2}$ pairs among the first 80 terms was checked
directly and found to share a prime specifically in $Q$ (not merely *some*
common prime, as pairwise non-coprimality already guarantees) — this is a
computational confirmation of the pairwise-intersecting reformulation of
(b), independent of the recursive machinery. This is **strong evidence, not
a proof**: it confirms the Unified Central Claim is very plausibly true (with
$Q$ taken to be exactly the prime support of the eventual period $L$), and
that the reduction of §9.3–9.4 is not vacuous — a genuine finite $Q$ appears
to work in every tested instance, from the very first term, with no
exceptions and no transient. But:

- **The definition of $Q=R(L)$ used in the check is circular for a proof**:
  $L$ is defined via the sequence's own (empirically observed) eventual
  period, which is exactly the object the problem asks us to establish
  exists. An honest proof of the Unified Central Claim needs $Q$ (or at least
  a certificate that *some* finite $Q$ works) constructed or characterized
  *independently* of already knowing the periodic tail.
- **No mechanism in this approach (or, per `current.md`, any approach in the
  population) constructs such a $Q$ or proves its existence.** This remains
  the single open gap of the whole problem, in this approach's cleanest form
  to date: *does there exist a finite set of primes $Q$ such that every two
  terms $a_i,a_j$ of the sequence share a prime factor lying in $Q$?*

This numeric check was run in Python (not included as part of the written
proof, per the rigor rules — it is reported here only as motivating evidence
for the plausibility of the open claim, not as a proof step).

#### 9.5.1 Reconciliation with round 2's "rejected fix" (§7)

The construction $b_1=a_1$, $b_{n+1}=\min\{m>b_n:\mathrm{Good}_Q(m)\}$
examined and rejected in §7 is, by Fact D and the Reduction Lemma, *exactly*
the recursion satisfied by $(a_n)$ itself if and only if the Unified Central
Claim holds for $Q$. So §7's finding — "$(b_n)=(a_n)$ cannot be assumed for
free, because the true early candidate set is generally a *strict superset*
of the $Q$-Good one" — remains entirely correct as a general warning: it
shows why the Unified Central Claim is not automatic or free for an
arbitrary $Q$ (indeed for a "wrong" $Q$, missing a prime the sequence
actually needs early on, $(b_n)$ and $(a_n)$ provably diverge, exactly as
§7 argues). What §9.3–9.4 add is that this is not a *separate* difficulty
requiring its own argument: $(b_n)=(a_n)$ for the *correct* $Q$ is
**precisely equivalent** to the Unified Central Claim, so once that single
claim is established (for the right $Q$) the coincidence $(b_n)=(a_n)$, and
hence the full periodicity conclusion, follow with no further work — there
is no possibility of the Unified Central Claim holding while $(b_n)\ne(a_n)$,
by the Reduction Lemma's own proof. This is consistent with, not
contradictory to, §7: §7 shows the naive assumption is unjustified in
general (true); §9 shows exactly what would justify it (the single Unified
Central Claim) and that nothing more is needed once that claim holds.

#### 9.6 Net effect of this round on the gap structure

Before this round, the approach carried two open gaps (Gap 1:
self-sufficiency for *some* $n^*$; Gap 2: extending periodicity from $n^*$
down to $n=1$). This round proves (§9.3, Reduction Lemma) that **these are
not independent**: proving Hypothesis SS with $n^*=1$ directly is *exactly
equivalent* to the single clean statement that every accepted term is itself
$Q$-Good, and (§9.4) that this single statement, for any finite $Q\supseteq
Q_0$, already implies the *full, transient-free* conclusion the problem asks
for. So Gap 1 and Gap 2, as previously tracked separately in `current.md`,
are now **provably the same gap** (for this approach's route): the Unified
Central Claim of §9.3(b). This is real progress — a strict simplification of
what remains to be shown — but the Unified Central Claim itself is not
proved this round, so the approach remains Status `partial`.

## Round 3 outline (proof-outliner — advance with a new mechanism, unified target)

**New target (adopt the round-3 unification).** Instead of proving
Hypothesis SS($Q,n^*$) for some $n^*\ge n_1(Q)$ and separately extending to
$n^*=1$ (Gap 1 then Gap 2), attack **Hypothesis SS($Q,1$) directly** —
i.e. show $(\ast)$ from §5 (the tail-equals-$Q$-Good-set identity) holds
with $a_{n^*}$ replaced by $a_1$ itself, or find precisely where it breaks.

**New tool (round-3 explorer finding, distinct from active-set-stabilization's
mechanism — use here in the complement-set/Proposition-B framework):**

**Self-Type-Compatibility Lemma.** Fix finite $Q\supseteq Q_0=R(a_1)$. If
$R(a_i)\subseteq Q$, then $\tau_i\cap\tau_j\ne\emptyset$ for every $j\ne i$.
*Proof:* `lemmas/pairwise-non-coprimality.md` gives a common prime $p\mid
a_i,a_j$; $R(a_i)\subseteq Q\Rightarrow p\in Q$, so $p\in\tau_i\cap\tau_j$.
Taking $i=1$ (so $R(a_1)=Q_0\subseteq Q$ automatically):
**$\mathrm{Good}_Q(a_1)$ holds for every valid $Q$, unconditionally** — no
appeal to $n_1(Q)$ or type-stabilization needed at all.

**Skeleton for this round's build (distinct route from
active-set-stabilization's aimo-0680-style discrepancy argument):**
1. Certify the Self-Type-Compatibility Lemma (short, shared ingredient —
   coordinate with active-set-stabilization so it is only certified once).
2. Revisit Step 1 of §5's Theorem ($(\ast)$: $A\cap(a_{n^*},\infty)=
   \{m>a_{n^*}:\mathrm{Good}_Q(m)\}$) and attempt to push $n^*$ down to $1$
   directly using Proposition B (already certified: $m\in A\iff$
   $\gcd(m,a_i)>1$ for every *earlier accepted* $a_i<m$) **combined with**
   the propagation form of the new lemma: if $R(a_i)\subseteq Q$ for every
   $i<n$, $\mathrm{Good}(a_n)$ and $\mathrm{Good}_Q(a_n)$ coincide on the
   *realized* constraints (both only need $\tau_n$ to meet each earlier
   $\tau_i$, and propagation supplies that meeting via $Q$ regardless of
   $\tau_n$'s content) — the gap is exactly the finitely-occurring indices
   with $R(a_i)\not\subseteq Q$ ("outside-prime" indices), which must be
   checked one at a time or bounded in number.
3. Attempt: use the already-certified **Lemma P** (exact periodicity of a
   residue-class-union listing, no transient) as the finishing step *if*
   step 2 succeeds in establishing $(\ast)$ with $n^*=1$ replaced by $a_1$
   directly — this would give periodicity for **all** $n\ge1$ in one shot
   via Lemma P applied with $c=a_1$ (rather than $c=a_{n^*}$), collapsing
   both Gap 1 and Gap 2 into the single remaining central question of which
   $Q$ works and why outside-prime indices never break $(\ast)$.
4. If the outside-prime indices cannot be shown harmless in general, report
   honestly which specific configurations (from the numerical examples,
   e.g. $a_1=35$'s indices $14,17,22,\dots$) do or do not break $(\ast)$,
   sharpening the diagnosis rather than asserting an unproved fix.

**Open gaps:** (a) which finite $Q$ makes Hypothesis SS true at all (shared
central gap, deferred to `jacobsthal-covering-bound`'s revision); (b)
whether outside-prime indices are always harmless for $(\ast)$ with
$n^*=1$ — genuinely open, not yet attempted by any approach in this precise
form.

**Cases to cover:** none beyond existing.

**Watch out for:** this is a *different* mechanism from
active-set-stabilization's round-3 revision (which uses Lemma M +
aimo-0680's divisible-and-bounded finishing move on a discrepancy sequence
$e_n$) — both use the Self-Type-Compatibility Lemma as a shared ingredient
but diverge in how they try to close the remaining gap; keep them
independent so both routes get a fair try.

### 10. Round 4 target: the Hitting-Set Reformulation and the incremental-recruitment construction

This section attacks the Unified Central Claim (§9.3(b)) directly, via a new
equivalent reformulation and a concrete (partially unresolved) construction
of a candidate $Q$. No previously-dead mechanism (g(Q) threshold, prime-size
threshold, $\Lambda$-split, windowed $\epsilon_n$ automaton) is reused.

#### 10.1 The Hitting-Set Lemma (new, fully proved)

For $i,j\ge1$ define $W(i,j):=R(a_i)\cap R(a_j)$, a **nonempty** finite set
of primes (nonempty by the certified `pairwise-non-coprimality.md`, applied
whenever $i\ne j$; for $i=j$, $W(i,i)=R(a_i)\ne\emptyset$ trivially since
$a_i>1$).

**Hitting-Set Lemma.** For a finite $Q\supseteq Q_0$: the Unified Central
Claim (§9.3(b): $\mathrm{Good}_Q(a_n)$ for every $n\ge1$) holds **iff** $Q$
is a *hitting set* for the family $\{W(i,j):i,j\ge1\}$, i.e. $Q\cap
W(i,j)\ne\emptyset$ for every $i,j\ge1$.

*Proof.* By definition (§4), $\mathrm{Good}_Q(a_n)$ holds for every $n$ iff
$\tau_n\cap\tau_j\ne\emptyset$ for every $n,j\ge1$ (where $\tau_k=R(a_k)\cap
Q$), iff $(R(a_n)\cap Q)\cap(R(a_j)\cap Q)\ne\emptyset$ for every $n,j$, iff
$Q\cap R(a_n)\cap R(a_j)\ne\emptyset$, i.e. $Q\cap W(n,j)\ne\emptyset$, for
every $n,j\ge1$. This is exactly the hitting-set condition. $\blacksquare$

This converts the number-theoretic Unified Central Claim into a pure
**set-hitting problem** for the (infinite) family $\{W(i,j)\}$ of finite
nonempty prime sets — a genuinely different vocabulary from anything the
population has used, though logically equivalent to what was already
implicit. Two consequences, both new and useful:

- **Free partial coverage.** $W(1,j)=R(a_1)\cap R(a_j)\subseteq R(a_1)=Q_0$
  for every $j$, and $W(1,j)\ne\emptyset$ (pairwise-non-coprimality with
  $i=1$). So $Q_0$ *already* hits every $W(1,j)$, $j\ge1$, with **no
  enlargement needed** — this recovers Lemma $Q_0$ (§0) as a special case,
  but now visibly as "the pairs involving index 1 are free." **The entire
  remaining difficulty is confined to pairs $W(i,j)$ with $i,j\ge2$** (or
  more precisely, pairs not already hit by $Q_0$).
- **A finite witness suffices at each pair, not a whole set.** Since each
  $W(i,j)$ is nonempty, *some* single prime always exists to hit it; the
  difficulty is choosing finitely many primes that simultaneously hit all
  (infinitely many) pairs.

#### 10.2 The incremental recruitment construction

Define an increasing chain of finite prime sets $Q^{(0)}\subseteq
Q^{(1)}\subseteq\cdots$ by: $Q^{(0)}:=Q_0=R(a_1)$; given $Q^{(k)}$, if it
already hits every $W(i,j)$ we stop (Unified Central Claim holds for
$Q:=Q^{(k)}$, done). Otherwise let $(i_k,j_k)$ be the pair with smallest
$\max(i_k,j_k)$ (breaking ties by smallest $\min(i_k,j_k)$) among all pairs
not yet hit by $Q^{(k)}$, pick any prime $p_k\in W(i_k,j_k)\setminus
Q^{(k)}$ (exists since $W(i_k,j_k)\ne\emptyset$ and is not hit), and set
$Q^{(k+1)}:=Q^{(k)}\cup\{p_k\}$.

**Open target (this round's central gap, restated concretely): does this
process terminate after finitely many steps $K$?** If so, $Q:=Q^{(K)}$ is a
finite set satisfying the Unified Central Claim, and the whole problem is
solved by §9.4. This is **not proved** here. What is new and checkable:

- The recruiting pairs $(i_k,j_k)$ are, by construction, *not yet hit* by
  $Q^{(k)}\supseteq Q_0$; by the "free partial coverage" fact above, neither
  $i_k$ nor $j_k$ can equal $1$, so recruitment is driven entirely by pairs
  among indices $\ge2$.
- **A genuine (partial) monotonicity fact**: once $p_k$ is recruited, it
  permanently hits $W(i_k,j_k)$ (adding primes to $Q^{(k)}$ never removes
  coverage), so the *set of unhit pairs* is monotone non-increasing under
  this construction — this rules out oscillation, but by itself gives no
  bound on $K$ since the family of unhit pairs is a priori infinite at every
  finite stage.
- **The genuinely open piece**: is there a bound, in terms of $|Q^{(k)}|$
  alone (not in terms of which specific pair triggered recruitment), on how
  many *new* primes can ever be forced in? A natural but **unverified**
  conjecture to test first (cheap, computational): for the numerically
  solved instances (e.g. $a_1=35$, needing exactly $\{2,3\}$ beyond
  $Q_0=\{5,7\}$; $a_1=15$, needing exactly $\{2\}$ beyond $\{3,5\}$), does
  every recruiting pair $(i_k,j_k)$ in this construction have BOTH indices
  bounded by an explicit function of $|Q^{(k)}|$ alone (e.g.
  $\max(i_k,j_k)\le n_1(Q^{(k)})$, the type-stabilization index of Lemma
  2$'$ for the *current* $Q^{(k)}$, applied retroactively)? If this
  "recruitment always happens early, relative to the current $Q$"
  property can be verified and then proved in general, it would give a
  genuine termination argument (each recruitment step is confined to a
  provably finite search window, and the window's growth would need to be
  shown not to outpace itself — the precise self-referential bound flagged
  as Opening 3 in this round's explorer report, not yet resolved).

**This is honestly an open construction, not a completed proof.** The value
added this round is (a) the Hitting-Set Lemma (§10.1, fully proved, reusable
by any approach), which reframes the whole remaining gap as a set-hitting
question, and (b) a precise, checkable termination criterion for the
recruitment process (§10.2) that the next round's builder should test
computationally before attempting a general proof, exactly as flagged.

### 11. Round 4 build: testing, and refuting, the natural closed-form
candidate; confirming §10.2 empirically; pinning down the exact obstruction

This section is new content built this round directly on top of §10 (the
Hitting-Set Lemma and the incremental-recruitment construction, both
verified sound by the round-4 outline-reviewer). The goal was to prove
termination of §10.2's recruitment process. **This is not achieved.** What
is achieved: a natural, very promising closed-form strengthening is
proposed, proved in two nontrivial special cases, and then **decisively
refuted** by an explicit, fully hand-verified counterexample — a genuine
new negative result, not merely "unproved," which prevents any future
round from investing further effort in this specific simplification. The
underlying recruitment construction of §10.2 itself is *not* refuted (it
still terminates on the refuting example, checked directly); only the
specific idea "the finite $Q$ can be taken to be $a_1$-only-dependent, of
the simple form $\{p\le R\}$" is killed.

#### 11.1 The Bounded-Radical Hitting-Set Claim (proposed)

Write $R:=\mathrm{rad}(a_1)$ as before, and let $[2,R]$ denote the set of
primes $\le R$ (a finite set determined by $a_1$ alone, with
$Q_0\subseteq[2,R]$, since every prime of $Q_0$ divides $R=\prod_{p\in
Q_0}p$ and hence is $\le R$). Consider the candidate $Q^\star:=\{p\text{
prime}: p\le R\}$ — a completely explicit finite set, computable from
$a_1$ alone with **no reference to the sequence's own eventual behavior**
(unlike the round-3 numerics, which used $Q=R(L)$ for the *empirically
observed* period $L$ — exactly the circularity flagged in §9.5). By the
Hitting-Set Lemma (§10.1), $Q^\star$ satisfies the Unified Central Claim
iff:

**Bounded-Radical Hitting-Set Claim (proposed).** For every $i,j\ge1$,
$R(a_i)\cap R(a_j)\cap[2,R]\ne\emptyset$.

If true for every $a_1$, this closes the whole problem (via §9.3–9.4). We
first prove it in two special cases unconditionally, then refute it in
general.

**Case $i=1$ (any $j$): proved.** By the Self-Type-Compatibility Corollary
(§9.2, certified), $\mathrm{Good}_Q(a_1)$ holds for *every* finite
$Q\supseteq Q_0$, in particular $Q=Q^\star$; unwinding the definition
(§4), this says $R(a_1)\cap Q^\star$ meets every $\tau_j\in\mathcal
T=\{R(a_k)\cap Q^\star:k\ge1\}$, i.e. $R(a_1)\cap Q^\star\cap R(a_j)\ne
\emptyset$ for every $j$. Since $R(a_1)=Q_0\subseteq Q^\star$ trivially,
$R(a_1)\cap Q^\star=Q_0$, so this reads $Q_0\cap R(a_j)\ne\emptyset$ —
exactly Lemma $Q_0$, already certified, giving the claim for $i=1$ with
room to spare (the witness prime is even in $Q_0$, not just $[2,R]$).

**Case $|i-j|=1$ (adjacent, any position): proved.** By the certified
`lemmas/adjacent-link-lemma.md`, $\gcd(a_n,a_{n+1})\mid d_n\le R$ for every
$n\ge1$ (where $d_n=a_{n+1}-a_n$), so $\gcd(a_n,a_{n+1})$ is a positive
integer $\le R$; every prime factor of a positive integer $\le R$ is
itself $\le R$ (a prime factor of $x$ is $\le x$), and $\gcd(a_n,a_{n+1})
>1$ (pairwise non-coprimality), so it has at least one prime factor, which
lies in $R(a_n)\cap R(a_{n+1})\cap[2,R]$. This proves the claim for every
adjacent pair, unconditionally, with no further argument needed.

So the *only* open sub-case, going in, was pairs $(i,j)$ with $2\le i$ and
$j\ge i+2$ (non-adjacent, neither index equal to $1$).

#### 11.2 Extensive numerical support (before the refutation was found)

The claim was checked computationally (python3, exact integer arithmetic
via `sympy`, direct greedy simulation, trial-checking every prime $\le R$
by division, not by any circular use of the sequence's eventual period)
across a wide range: all $a_1\in\{15,21,35,65,77,99,33,45,105,143,1155,
1001,385,221,91,119,187,209,247,253,289,\dots\}$ with $N$ up to $500$
terms per instance, and separately $a_1=2\cdot3\cdot5\cdot7\cdot11\cdot13
\cdot17=510510$ ($R=510510$, $N=300$) — **zero exceptions found** in all
of these (many thousands of pairs checked per instance, exhaustively, not
sampled). This is reported honestly as strong *evidence*, not proof, per
the rigor rules — and indeed, per §11.3 below, it was misleading: the
claim is false, just not for any $a_1$ in this particular list.

#### 11.3 Refutation: an explicit, fully hand-verified counterexample at $a_1=375$

A systematic sweep over $a_1=4,\dots,399$ (each checked over the first
$120$ terms) was run to stress-test the claim before committing to it as a
target; this sweep found exactly two violating pairs, both for
$a_1=375$. We verify the relevant instance completely by hand below (not
merely reporting a computer's output as a proof step, per the rigor
rules).

**Setup.** $a_1=375=3\cdot5^3$, so $Q_0=\{3,5\}$ and $R=\mathrm{rad}(375)
=3\cdot5=15$. The primes $\le R=15$ are $\{2,3,5,7,11,13\}$.

**Hand-computation of $a_1,\dots,a_7$.** At each step we must find the
smallest integer exceeding the current last term that has $\gcd>1$ with
*every* earlier term.

- $a_1=375=3\cdot5^3$.
- $a_2$: test $376=2^3\cdot47$ ($\gcd(376,375)=1$, reject); $377=13\cdot
  29$ ($\gcd=1$, reject); $378=2\cdot3^3\cdot7$ ($\gcd(378,375)=3>1$,
  accept). So $a_2=378$.
- $a_3$: test $379$ (prime, $\gcd(379,375)=1$, reject); $380=2^2\cdot5
  \cdot19$: $\gcd(380,375)=5>1$; $\gcd(380,378)=\gcd(2^2{\cdot}5{\cdot}19,\,
  2{\cdot}3^3{\cdot}7)=2>1$. Both pass, accept. So $a_3=380$.
- $a_4$: test $381=3\cdot127$: $\gcd(381,375)=3$ ok; $\gcd(381,378)=3$ ok;
  $\gcd(381,380)=\gcd(3{\cdot}127,\,2^2{\cdot}5{\cdot}19)=1$, **fails**
  (reject). $382=2\cdot191$: $\gcd(382,375)=1$, reject. $383$ prime:
  $\gcd(383,375)=1$, reject. $384=2^7\cdot3$: $\gcd(384,375)=3$ ok;
  $\gcd(384,378)=2\cdot3=6$ ok; $\gcd(384,380)=2^2=4$ ok. All pass,
  accept. So $a_4=384$.
- $a_5$: test $385=5\cdot7\cdot11$: $\gcd(385,375)=5$ ok; $\gcd(385,378)=7$
  ok; $\gcd(385,380)=5$ ok; $\gcd(385,384)=1$, **fails** (reject).
  $386=2\cdot193$: $\gcd(386,375)=1$, reject. $387=3^2\cdot43$:
  $\gcd(387,375)=3$ ok; $\gcd(387,378)=3^2=9$ ok; $\gcd(387,380)=1$,
  **fails** (reject). $388=2^2\cdot97$: $\gcd(388,375)=1$, reject. $389$
  prime: $\gcd(389,375)=1$, reject. $390=2\cdot3\cdot5\cdot13$:
  $\gcd(390,375)=15$ ok; $\gcd(390,378)=6$ ok; $\gcd(390,380)=10$ ok;
  $\gcd(390,384)=6$ ok. All pass, accept. So $a_5=390$.
- $a_6$: test $391=17\cdot23$: $\gcd(391,375)=1$, reject. $392=2^3\cdot7^2$:
  $\gcd(392,375)=1$, reject. $393=3\cdot131$: $\gcd(393,375)=3$ ok;
  $\gcd(393,378)=3$ ok; $\gcd(393,380)=1$, **fails**. $394=2\cdot197$:
  $\gcd(394,375)=1$, reject. $395=5\cdot79$: $\gcd(395,375)=5$ ok;
  $\gcd(395,378)=1$, **fails**. $396=2^2\cdot3^2\cdot11$:
  $\gcd(396,375)=3$ ok; $\gcd(396,378)=2\cdot3^2=18$ ok;
  $\gcd(396,380)=2^2=4$ ok; $\gcd(396,384)=2^2\cdot3=12$ ok;
  $\gcd(396,390)=2\cdot3=6$ ok. All pass, accept. So $a_6=396$.
- $a_7$: test $397$ prime: $\gcd(397,375)=1$, reject. $398=2\cdot199$:
  $\gcd(398,375)=1$, reject. $399=3\cdot7\cdot19$: $\gcd(399,375)=3$ ok;
  $\gcd(399,378)=3\cdot7=21$ ok; $\gcd(399,380)=19$ ok (see below);
  $\gcd(399,384)=3$ ok; $\gcd(399,390)=3$ ok; $\gcd(399,396)=3$ ok. All
  six constraints pass, accept. So $a_7=399$.

**The counterexample.** $a_3=380=2^2\cdot5\cdot19$ and $a_7=399=3\cdot7
\cdot19$. Their only common prime factor is $19$ (the prime sets
$\{2,5,19\}$ and $\{3,7,19\}$ intersect in exactly $\{19\}$), so
$$\gcd(a_3,a_7)=19.$$
Since $19>15=R$, and the primes $\le R=15$ dividing $a_3$ are $\{2,5\}$
while those dividing $a_7$ are $\{3,7\}$ — **disjoint** — we get
$$R(a_3)\cap R(a_7)\cap[2,R] = \{2,5\}\cap\{3,7\} = \emptyset.$$

**This is a complete, rigorous, hand-verified refutation** of the Bounded-
Radical Hitting-Set Claim: it is **false** for $a_1=375$, with the
explicit witnessing pair $(i,j)=(3,7)$. (The full derivation above uses
only the raw recursive definition of the sequence at each of the 6 steps;
every gcd claimed is computed directly from the prime factorizations
shown, no computer-only step is used as a proof step, consistent with the
rigor rules.)

**Theorem (Bounded-Radical Hitting-Set Claim is false in general).** There
exists $a_1$ (namely $a_1=375$) and indices $i,j$ (namely $i=3,j=7$) such
that $R(a_i)\cap R(a_j)\cap[2,\mathrm{rad}(a_1)]=\emptyset$. $\blacksquare$

#### 11.4 What this refutation does, and does not, close

- It **rules out** $Q^\star=\{p\le R\}$ as a universal, $a_1$-only-derived
  candidate for the Unified Central Claim's witness set $Q$ — a genuinely
  new, checked, decisive negative result (a fifth failed mechanism for the
  population's shared central gap, after the $g(Q)$ threshold, prime-size
  threshold, $\Lambda$-split, and windowed-$\epsilon_n$-automaton
  failures of rounds 2–3).
- It does **not** refute the incremental-recruitment construction of
  §10.2 itself, nor the existence of *some* finite $Q$ for $a_1=375$: run
  directly (computationally, as a sanity check, not as a proof step) on
  this same instance, the recruitment process of §10.2 still terminates,
  producing $Q=\{2,3,5,7,19\}$ after recruiting $\{2,19,7\}$ beyond
  $Q_0=\{3,5\}$, at triggering pairs $(2,3)$ [prime $2$], $(3,7)$ [prime
  $19$ — exactly the pair exhibited above], $(7,26)$ [prime $7$]. So the
  central open question (does §10.2's recruitment always terminate?) is
  **untouched** by this refutation; only one natural *shortcut* for
  answering it (a closed-form, sequence-independent bound on the
  recruited primes) is now known to be unavailable in general. In
  particular, the recruited prime $19$ in this instance is **not** a
  function of $a_1=375$ alone via any simple bound like $\mathrm{rad}(a_1)$
  or small multiples of it — it arises because $a_3=380=19\cdot20$ and
  $a_7=399=19\cdot21$ happen to be consecutive multiples of $19$
  (Note: $\gcd(19{\cdot}20,19{\cdot}21)=19\cdot\gcd(20,21)=19\cdot1=19$),
  a coincidence of the specific integers involved, not a structural
  feature derivable from $a_1$'s factorization in isolation.

#### 11.5 Why the natural induction strategies fail: two documented negative findings

Two proof strategies for the Bounded-Radical Claim (before its refutation
made this moot for that specific claim, but the obstructions identified
are general and apply to *any* future attempt to prove a closed-form,
$a_1$-only-dependent hitting set) were attempted and are recorded here so
they are not repeated:

**(a) Single-small-prime replacement fails.** Given a bad candidate pair
$(i,j)$ with $\gcd(a_i,a_j)$ having no prime factor $\le R$, one might try
to build a smaller legal candidate than $a_j$ using a single small prime
$q$ known to divide $a_i$ (e.g. a Lemma-$Q_0$ witness). This fails because
a *single* prime $q$ only guarantees legality against those earlier terms
$a_k$ that happen to *also* be divisible by $q$ — unlike the full baseline
$M$ (the next multiple of $R=\prod Q_0$), which is guaranteed legal
against *every* earlier term simultaneously (via Lemma $Q_0$, every $a_k$
has *some* $Q_0$-prime factor, and $M$ is divisible by *all* of $Q_0$
at once). A candidate built from one prime $q\notin Q_0$ (or even $q\in
Q_0$ alone, without the rest of $Q_0$) has no such universal-coverage
guarantee, so no smaller-candidate contradiction can be derived this way
in general.

**(b) Adjacent-chain transitivity fails, by a general set-theoretic
obstruction (not specific to this sequence).** One might hope to induct on
the index gap $d=j-i$, chaining the Adjacent-Link Lemma's pairwise
intersections $\sigma_k\cap\sigma_{k+1}\ne\emptyset$ (where $\sigma_n:=
R(a_n)\cap[2,R]$) along the path $i,i+1,\dots,j$ to conclude $\sigma_i\cap
\sigma_j\ne\emptyset$. This is **impossible in general**, independent of
any property of the sequence $(a_n)$: pairwise-consecutive intersection of
a chain of sets does **not** imply the endpoints intersect. Concrete
witnessing counterexample (pure set theory, no number theory needed):
$\sigma_1=\{1,2\}$, $\sigma_2=\{2,3\}$, $\sigma_3=\{3,4\}$ satisfies
$\sigma_1\cap\sigma_2=\{2\}\ne\emptyset$ and $\sigma_2\cap\sigma_3=\{3\}
\ne\emptyset$, yet $\sigma_1\cap\sigma_3=\emptyset$. This was checked
directly against the actual sequence data too: for $a_1=15$, adjacent
$Q_0$-types are disjoint $50$ times among the first $100$ terms (e.g.
$\tau_2=\{3\}$, $\tau_3=\{5\}$ — disjoint, even though $\sigma_2\cap
\sigma_3\ne\emptyset$ via an outside connecting prime), confirming this is
not a vacuous concern but an actively-occurring pattern in the real
sequences. **Any future attempt at an inductive proof of a hitting-set
claim via chaining consecutive intersections must supply additional
information beyond "consecutive pairs intersect" — plain transitivity of
nonempty intersection does not hold**, and this obstruction should be
regarded as a standing warning, not re-derived from scratch.

#### 11.6 Net status after this round

The central gap (does the incremental-recruitment construction of §10.2
terminate — equivalently, does *some* finite $Q\supseteq Q_0$ satisfy the
Unified Central Claim?) **remains completely open**. This round's
concrete contribution is: (i) two special cases of the natural closed-form
candidate proved outright ($i=1$; adjacent pairs) — reusable facts, not
depending on the (now-refuted) general claim; (ii) a decisive,
hand-verified refutation of the general closed-form candidate $Q=\{p\le
\mathrm{rad}(a_1)\}$, closing off a promising-looking shortcut that could
otherwise have consumed a future round; (iii) a general (sequence-
independent) set-theoretic obstruction to the most natural induction
strategy (chaining), documented so it is not retried; (iv) continued
(now more extensive, and honestly including the found counterexample
rather than suppressing it) empirical support that the *unconstrained*
existential claim — some finite $Q$ exists, not necessarily of the simple
form $\{p\le R\}$ — still holds in every tested instance, including the
refuting one. No approach in the population (including this one) has yet
produced a mechanism that provably bounds the number of recruitment steps
in general. This is honest, checked negative progress plus two small
positive facts, not a resolution.

## Round 6 revision (proof-outliner): hand-trace the slow-stabilization outlier as a concrete lever

This approach continues to own the Unified Central Claim / $Q$-existence
framing, but this round's assigned mechanism is deliberately different from
`active-set-stabilization`'s round-6 abstract Bounded-Witness-Index
Conjecture (same gap, different mechanism, per CLAUDE.md's guidance that
diversity can live in the mechanism attacking a shared hard lemma).

**Target this round.** Hand-analyze the concrete outlier
$a_1=20735=5\cdot11\cdot13\cdot29$ (round-6 nec-finiteness explorer,
witness index $69$ for one of its $\mathrm{Nec}\setminus R(a_1)$ elements,
versus index $\le9$ for every other tested multi-prime seed) to extract the
*combinatorial reason* for the slow stabilization, then test whether that
reason generalizes into an explicit bound. Use the already-certified
**Multiple-of-$R$ Realization Lemma** (`multiple-of-r-realization.md`: every
multiple of $R=\mathrm{rad}(a_1)$ beyond $a_1$ is itself an accepted term)
and the **Same-Class-Free / Class-Partition Reduction**
(`same-class-free-class-partition-reduction.md`: only cross-class pairs can
witness new $\mathrm{Nec}$ elements) as the starting structural facts — both
directly constrain which of the first $69$ terms of the $20735$ sequence
*must* appear (as multiples of $5\cdot11\cdot13\cdot29$'s sub-radicals) and
in which class-partition cell they land, which is exactly the raw material
needed to explain a slow cross-class witness.

**Skeleton for this round's build.**
1. Enumerate $a_1,\dots,a_{70}$ for $a_1=20735$ explicitly (small
   computation), tag each term by its class (smallest $R(a_1)$-prime
   factor, per the Class-Partition Reduction).
2. Identify exactly which cross-class pair $(i,j)$, $j\approx69$, is the
   first to witness a new $\mathrm{Nec}$ element, and what arithmetic
   coincidence makes it happen so late (e.g.: does the delay come from the
   four primes $5,11,13,29$ having a large pairwise LCM structure that
   pushes the first "coincidental" shared extra factor far out? Check
   residues of small primes $2,3,7,\dots$ modulo $5,11,13,29$ for an
   unusually late alignment.)
3. State the extracted mechanism as a candidate general lemma (e.g. "the
   witness index for a cross-class pair is governed by [specific
   arithmetic quantity], which can be bounded by [explicit function of
   $a_1$]") — even a *conjectural*, numerically-tested form is valuable
   progress if honestly labeled as such.
4. Cross-check the candidate mechanism against 2-3 of the already-fast
   seeds (e.g. $a_1=385$, idx 6; $a_1=194287$, idx 9) to make sure it does
   not merely fit the one outlier.

**Why this is not the dead "closed-form $Q$" mechanism.** This is not
proposing a universal formula for $Q$ itself (already refuted,
`bounded-radical-refutation.md`) — it targets the *index* at which
$\mathrm{Nec}$-witnessing saturates, a different object entirely, in the
same spirit as `active-set-stabilization`'s round-6 target but via
hand-tracing a specific hard instance rather than an abstract induction.

**Open gaps:** the general bound $N(a_1)$ (if it exists) is not yet even
conjectured in closed form; this round's deliverable is the diagnosis of
*one* hard instance, which the outline-reviewer should treat as a
stepping-stone, not a finished lemma.

**Watch out for:** don't let this round's hand-trace collapse into
re-deriving the already-refuted "each cross-class pair contributes $O(1)$"
claim (see `active-set-stabilization.md`'s round-6 section) — the $20735$
data point is specifically evidence *against* any simple per-pair-count
bound; the lever here is the *index*, not a count.

### 13. Round 6 build: hand-tracing the $a_1=20735$ slow-stabilization outlier

This section attacks the round-6 outline's assigned target: diagnose the
combinatorial reason $a_1=20735=5\cdot11\cdot13\cdot29$ needs a much later
witness index (in $\mathrm{Nec}$-terms) than every other tested multi-prime
seed, and test whether the diagnosis generalizes into an explicit bound. As
flagged honestly up front: **this does not close the central gap**, and does
not produce a new certified lemma; it produces a precise, checked diagnosis
and an explicitly labeled, unproved quantitative conjecture, which is the
deliverable the round-6 outline asked for.

#### 13.1 Setup and method

Throughout, $P:=R(a_1)=\{5,11,13,29\}$ for $a_1=20735$, and $R(m)$ denotes
the (finite) set of distinct prime factors of $m$, as elsewhere in this
file. I generate the sequence mechanically from the raw recursive
definition (for each $n$, $a_{n+1}$ is the least integer exceeding $a_n$
with $\gcd(\cdot,a_i)>1$ for every $i=1,\dots,n$) — this is a
fully deterministic computation with no randomness or heuristic step in
*generating* the sequence; I report it as **computational, not
step-by-step hand-verified**, matching this file's own established honesty
convention for ranges beyond about ten terms (e.g. §12.3's $400$-term
counts): every individual factorization and gcd claimed below is directly
checkable by trial division, and the generation rule itself is unambiguous
and mechanically re-derivable by anyone, but I do not reproduce all $70$
greedy steps by hand here (that hand-verification, while possible in
principle exactly as done for the $7$- and $8$-step examples in §§11.3 and
12.4, would be impractically long and is not the deliverable of this
round). All numerical claims below were checked by direct computation
(`sympy` trial-factorization, exact integer arithmetic) and cross-checked
by an independent from-scratch re-simulation.

**Definition recap** (`lemmas/nec-necessity.md`): a prime $p$ is
*necessary* ($p\in\mathrm{Nec}$) if there exist indices $i<j$ with
$R(a_i)\cap R(a_j)=\{p\}$ exactly. For each such $p$, define its
**witness pair** as the lexicographically-first pair $(i,j)$ (smallest $j$,
then smallest $i$) realizing this.

#### 13.2 The computed data

Generating the first $100$ terms of the $a_1=20735$ sequence and computing
every pairwise intersection $R(a_i)\cap R(a_j)$ for $1\le i<j\le 100$ gives
the following witness pairs for $\mathrm{Nec}$ (only the first occurrence
of each necessary prime is shown; no further necessary prime appears with
witness index $j\le100$ beyond these):

$$
\begin{array}{c|c|c}
p & \text{witness }(i,j) & \text{status}\\\hline
5 & (1,2) & \in P\\
13 & (1,4) & \in P\\
2 & (2,4) & \text{new}\\
3 & (3,4) & \text{new}\\
7 & (4,6) & \text{new}\\
19 & (4,70) & \text{new (the outlier)}
\end{array}
$$

So $\mathrm{Nec}\setminus P \supseteq \{2,3,7,19\}$ on this range (with
$11,29\in P$ not yet used as unique-witness primes within the first $100$
terms, which is consistent with them simply not having been needed yet —
this says nothing about whether they, or further new primes, appear later;
the point of this section is the *shape* of the delay for $19$, not a claim
that $\mathrm{Nec}$ has stabilized).

**The outlier pair, in detail.** $a_4=20748$ and $a_{70}=21185$. By direct
trial factorization,
$$a_4 = 20748 = 2^2\cdot3\cdot7\cdot13\cdot19,\qquad a_{70}=21185=5\cdot19\cdot223,$$
(check: $4\cdot3\cdot7\cdot13\cdot19 = 12\cdot7\cdot13\cdot19=84\cdot13\cdot
19=1092\cdot19=20748$; and $5\cdot19\cdot223=95\cdot223=21185$). Hence
$$R(a_4)=\{2,3,7,13,19\},\qquad R(a_{70})=\{5,19,223\},\qquad
R(a_4)\cap R(a_{70})=\{19\}.$$
This confirms $19$ is necessary, witnessed by the pair $(4,70)$.

**Why the delay: every earlier multiple of $19$ in the sequence
"accidentally" shares a second prime with $a_4$.** The complete list of
indices $n\le97$ with $19\mid a_n$, computed directly, is
$$I_{19}\cap[1,97] = \{4,\,13,\,27,\,41,\,55,\,70,\,84,\,97\},$$
and their factorizations are:
$$
\begin{aligned}
a_4&=2^2\cdot3\cdot7\cdot13\cdot19, & a_{13}&=3\cdot5\cdot19\cdot73, &
a_{27}&=2^2\cdot5^2\cdot11\cdot19,\\
a_{41}&=5\cdot13\cdot17\cdot19, & a_{55}&=2\cdot3\cdot5\cdot19\cdot37, &
a_{70}&=5\cdot19\cdot223,\\
a_{84}&=2^5\cdot5\cdot7\cdot19, & a_{97}&=3^2\cdot5^3\cdot19. &&
\end{aligned}
$$
Write $O:=R(a_4)\setminus\{19\}=\{2,3,7,13\}$, the **obstruction set** for
$19$ relative to the fixing index $4$: a later multiple of $19$, say $a_n$
($n\in I_{19}$, $n>4$), witnesses $19$ together with $a_4$ (as a
*singleton*-intersection pair) exactly when $R(a_n)\cap O=\emptyset$, i.e.
$a_n$ is divisible by none of $2,3,7,13$. Checking each element of
$I_{19}\cap(4,70)$ against $O$:
$$
\begin{aligned}
R(a_{13})\cap O &= \{3\}\ (13\text{ fails, shares }3),\\
R(a_{27})\cap O &= \{2\}\ (27\text{ fails, shares }2),\\
R(a_{41})\cap O &= \{13\}\ (41\text{ fails, shares }13),\\
R(a_{55})\cap O &= \{2,3\}\ (55\text{ fails, shares }2\text{ and }3),\\
R(a_{70})\cap O &= \emptyset\ (70\text{ succeeds}).
\end{aligned}
$$
So the delay from index $4$ to index $70$ is caused by five consecutive
"near misses": five multiples of $19$ in a row each happen to also carry
one of the four small primes $2,3,7,13$, before the sixth (at $n=70$)
finally avoids all four simultaneously. This is the precise combinatorial
mechanism behind the outlier: **it is not that $19$ takes long to enter the
sequence at all** ($19\mid a_4$ already, at the very same early index that
also witnesses $\mathrm{Nec}$-primes $2,3,7$) — **it is that the specific
fixing index $4$ has an unusually large obstruction set** ($|O|=4$,
compared to $|O|=1$ for the fast primes $2,3,7$ found at indices $4,4,6$
respectively via *different*, smaller-obstruction-set witnessing pairs),
so a witnessing partner for $19$ specifically via $a_4$ needs to dodge four
independent divisibility conditions at once, not just one or two.

#### 13.3 A cross-check: does obstruction-set size correlate with witness-index delay on other seeds?

To test whether "witness delay grows with obstruction-set size" is a
real, reusable pattern (not an artifact of this one instance), I repeated
the same analysis on two previously-tested fast seeds.

**$a_1=385=5\cdot7\cdot11$ ($P=\{5,7,11\}$).** The new prime $19$ is
witnessed at pair $(5,7)$: $a_5=399=3\cdot7\cdot19$,
$a_7=418=2\cdot11\cdot19$ (both already recorded in §12.4's hand-derivation
of this sequence's first $8$ terms). Here the fixing index is $5$
(smaller index of the pair) with obstruction set $O=R(a_5)\setminus\{19\}=
\{3,7\}$, of size $2$; the very next multiple of $19$ after $a_5$ in the
sequence is $a_7$ itself (index gap $2$), which already succeeds (it
avoids $3$ and $7$). Small obstruction set ($|O|=2$), small delay (next
candidate already succeeds).

**$a_1=194287=37\cdot59\cdot89$ ($P=\{37,59,89\}$).** The new prime $17$ is
witnessed at pair $(4,10)$: $a_4=194361=3\cdot17\cdot37\cdot103$,
$a_{10}=194582=2\cdot17\cdot59\cdot97$. Fixing index $4$, obstruction set
$O=R(a_4)\setminus\{17\}=\{3,37,103\}$, size $3$. The full list of indices
with $17\mid a_n$ up to $49$ is $\{4,10,18,41,47,49\}$; the very next one
after $4$ (namely $10$) already succeeds — only **one** near-miss-free
trial needed here (i.e. the *second* element of $I_{17}$ already works),
despite $|O|=3$ being larger than the $385$ case's $|O|=2$.

So across the three instances:
$$
\begin{array}{c|c|c}
a_1 & |O| \text{ (obstruction set size)} & \text{trials needed (position in }I_p\text{)}\\\hline
385 & 2 & 2\\
194287 & 3 & 2\\
20735 & 4 & 6
\end{array}
$$
The pattern "larger $|O|$ needs more trials" is **weakly consistent but not
monotone or quantitatively predictive** from just these three data points
($|O|=3$ needed as few trials as $|O|=2$; only $|O|=4$ shows a real jump).
This is exactly what a probabilistic heuristic would predict only in
*expectation*, not case-by-case: if one heuristically treats divisibility
of the $k$-th element of $I_p$ (a multiple of $p$) by each obstruction
prime $q\in O$ as an independent event of probability $1/q$ (density of
multiples of $q$), the chance a given trial avoids **all** of $O$
simultaneously is heuristically
$$\prod_{q\in O}\Bigl(1-\frac1q\Bigr),$$
and the expected number of trials to first success is the reciprocal of
this. For $O=\{3,7\}$: $(2/3)(6/7)=4/7\approx0.571$, expected trials
$\approx1.75$ (observed: $2$, i.e. success on the very first subsequent
trial — consistent). For $O=\{3,37,103\}$: $(2/3)(36/37)(102/103)\approx
0.6455$, expected $\approx1.55$ (observed: $2$ — succeeds on the very first
subsequent trial, i.e. the second element of $I_{17}$, again consistent).
For $O=\{2,3,7,13\}$: $(1/2)(2/3)(6/7)(12/13)\approx0.2637$, expected
$\approx3.79$ (observed: $6$ trials, i.e. the sixth element of $I_{19}$ —
of the right *order of magnitude*, a single-digit count, but roughly
$1.6\times$ the naive expectation, not an exact match).

**Honest conclusion of this cross-check.** The heuristic explains the
*qualitative* phenomenon (delay is governed by the size, and the specific
primes, of the obstruction set at the fixing index — smaller primes like
$2$ and $3$ in the obstruction set inflate the expected wait, since they
have the highest "hit rate" per trial) and gives the right order of
magnitude in all three tested cases, but it is **only a heuristic**: the
sequence $(a_n)$ is fully deterministic, not a sequence of independent
random trials, so there is no proof that this expectation-style bound
holds in general, nor any proof of a deterministic worst-case bound on the
number of trials as a function of $|O|$ (or of the specific primes in
$O$). In particular this analysis gives **no evidence either way** on
whether the witness-index delay can be made *unboundedly* large by
choosing $a_1$ with more, or smaller, obstruction primes at the fixing
index of some necessary prime — that remains a fully open question, and
answering it (in either direction) would bear directly on whether
$\mathrm{Nec}$ can be shown finite in general.

#### 13.4 What this round does and does not establish

- **Established (computational diagnosis, not a new certified lemma):** the
  exact combinatorial reason the $a_1=20735$ instance needed witness index
  $70$ rather than a single-digit index is a run of five "near-miss"
  multiples of $19$ that each happen to also carry one of $a_4$'s other
  four prime factors $\{2,3,7,13\}$, before the sixth multiple of $19$
  finally avoids all four. This is a completely mechanical, checkable fact
  about this specific instance (§13.2).
- **Tested, not established:** whether "witness delay is governed
  (heuristically, via a joint-avoidance waiting-time argument) by the size
  and identity of the obstruction set at the fixing index" is a general
  phenomenon. The heuristic is qualitatively and order-of-magnitude
  consistent across three instances (§13.3) but is explicitly **not a
  proof of any bound**, and the round found **no way to turn it into a
  bound**: a genuine bound would need to control, for *every* pair of
  indices that could ever serve as a fixing index for *some* future
  necessary prime, the size of that pair's obstruction set as a function
  of $a_1$ alone — and no such control is established or even conjectured
  in closed form here. This matches the round-6 outline's own warning not
  to re-derive the already-refuted "each cross-class pair contributes
  $O(1)$" claim: this section's finding is explicitly the opposite of a
  bound — it is a description of *why* a bound, if one exists, cannot be a
  simple constant, since the relevant obstruction-set size itself is not
  bounded a priori (it is $|R(a_i)|-1$ for whichever index $i$ ends up
  being the eventual fixing index, and $|R(a_i)|$ grows as more primes are
  recruited into the active set over time — a potential feedback loop
  between recruitment and future delay that this round's diagnosis
  surfaces but does not resolve).
- **The central gap (does $\mathrm{Nec}$ stabilize / is there a finite
  self-sufficient $Q$?) remains completely open.** This round adds a
  concrete, hand-checked case study illuminating *why* naive per-instance
  bounds keep failing (the obstruction-set-size feedback loop above), but
  produces no new inequality, lemma, or termination criterion strong
  enough to promote. No prior mechanism in the population's history is
  contradicted or reproven here; this is purely new diagnostic content.

## Round 7 revision (proof-outliner): Generalized Multiple-of-$r$ Realization
Lemma via CRT-positive-density — see the outline text reproduced/summarized
above the "Approaches tried" entry for this round. The outline-reviewer's
verdict was APPROVE (build), with the explicit condition that the write-up
must supply real content for the bridging step (§step 3 of the outline),
not merely restate CRT density as if it were a finish.

### 14. Round 7 build: closing off the literal mechanism, and pinpointing
exactly why the general bridging step remains open

Throughout this section, fix $a_1$, write $P:=R(a_1)$, $R:=\mathrm{rad}
(a_1)=\prod_{p\in P}p$, and recall (§0 above, "Lemma $Q_0$") that **every**
accepted term $a_n$ ($n\ge1$) satisfies $R(a_n)\cap P\ne\emptyset$ — this
single unconditional fact is the load-bearing ingredient for everything
below. Also recall the certified **Multiple-of-$R$ Realization Lemma**
(§12.1): every integer $x>a_1$ with $R\mid x$ is an accepted term.

Fix a prime $r\in\mathrm{Nec}\setminus P$ (a genuinely recruited prime,
`nec-necessity.md`) and a reference index $i\ge1$ with $r\mid a_i$. Write
$E_i:=R(a_i)\setminus\{r\}$, the **contaminant set** for $(r,i)$
(`contamination-dichotomy-and-reduction.md`). Call an integer $x$
**$(r,i)$-clean** if $r\mid x$ and $R(x)\cap E_i=\emptyset$; by the
Contamination Dichotomy Lemma, $x$ is $(r,i)$-clean and $r\mid x$
if and only if, whenever additionally $x>a_i$ is an accepted term with
$x=a_j$ for some $j$, the pair $(i,j)$ **witnesses** $r$ (singleton
intersection $R(a_i)\cap R(a_j)=\{r\}$).

#### 14.1 Impossibility Lemma: the "force $\mathrm{rad}(a_1)\mid x$" instantiation is vacuous whenever $P\subseteq R(a_i)$

The most natural way to try to reuse already-certified machinery for the
outline's step 1–3 is to look at $x:=$ a multiple of $L':=R\cdot r$ (as the
outline's skeleton literally proposes), since the Multiple-of-$R$
Realization Lemma (applied with $R\mid L'\mid x$) then gives, **for free,
with no density or CRT argument at all**, that every such $x>a_1$ is an
accepted term. We show this specific instantiation, however tempting,
**can never produce an $(r,i)$-clean witness** whenever the reference index
$i$ satisfies $P\subseteq R(a_i)$ — a condition satisfied by infinitely
many indices, not a corner case.

**Impossibility Lemma.** Let $r\notin P$ and let $i\ge1$ be an index with
$P\subseteq R(a_i)$ (equivalently, $R\mid a_i$). Then **no** integer $x$
with $r\mid x$ and $R\mid x$ is $(r,i)$-clean. In particular, no multiple
of $L'=R\cdot r$ can ever be used, via reference index $i$, to witness $r$
for the pair $(i,\cdot)$.

*Proof.* Since $r\notin P$, we have $P\subseteq R(a_i)\setminus\{r\}=E_i$
(removing $r$ from $R(a_i)$ does not remove any element of $P$, as
$r\notin P$). Now suppose $x$ satisfies $r\mid x$ and $R\mid x$. Since
$P\ne\emptyset$ (as $a_1>1$), pick any prime $q\in P$; then $q\mid R\mid x$,
so $q\in R(x)$, and $q\in P\subseteq E_i$, so $q\in R(x)\cap E_i$. Hence
$R(x)\cap E_i\ne\emptyset$, i.e. $x$ is **not** $(r,i)$-clean. $\blacksquare$

**Remark (this is not a corner case).** The hypothesis "$P\subseteq
R(a_i)$" holds for $i=1$ automatically (as $R(a_1)=P$), and — by the
certified Multiple-of-$R$ Realization Lemma itself — for **every** index
$i$ such that $a_i$ is one of the infinitely many accepted multiples of
$R$ beyond $a_1$. So the specific instantiation "force $x$ to be a
multiple of $\mathrm{rad}(a_1)\cdot r$" is provably useless as a witnessing
tool for *any* reference index drawn from this large, explicit,
infinite family — it can only ever confirm that $x$ is accepted (already
known, and for a reason that has nothing to do with $r$), never that $x$
witnesses $r$ against such an $i$.

**Hand-verification (independent of the general proof, per the rigor
rules).** Take $a_1=35=5\cdot7$ ($P=\{5,7\}$, $R=35$), $r=3\notin P$
(a prime known to be recruited: $\mathrm{Nec}\supseteq\{2,3,5,7\}$ for
$a_1=35$, per the round-7 outline's own cited numerics), and reference
index $i=1$ (which trivially satisfies $P\subseteq R(a_1)=P$). The lemma
predicts that no multiple of $3$ avoiding $E_1=R(a_1)\setminus\{3\}=
\{5,7\}$ can ever be $(3,1)$-clean — in fact more strongly, by the proof,
no such integer can even satisfy Lemma $Q_0$ against $a_1$, so it can
**never be accepted at all**, regardless of $r=3$. Direct enumeration of
every integer $x\in(35,390]$ with $3\mid x$, $5\nmid x$, $7\nmid x$ (i.e.
every candidate the mechanism would propose) shows **all of them fail to
divide any prime of $\{5,7\}$ by construction**, so each one fails the very
first constraint of the recursive definition (against $a_1=35$ itself) and
is rejected outright — e.g. $x=36=2^2\cdot3^2$: $\gcd(36,35)=1$ since $35=
5\cdot7$ shares no prime factor with $36=2^2\cdot3^2$; likewise $x=39=
3\cdot13$: $\gcd(39,35)=1$; $x=48=2^4\cdot3$: $\gcd(48,35)=1$. Every one of
these fails at the $i=1$ check alone, before any other index is even
considered — exactly as the lemma proves in general, and confirmed by
generating the actual sequence out to $390$ (its $10$th term is $84$, far
past this range) and checking that none of these candidates appear among
the accepted terms.

#### 14.2 The general ("not forced through $\mathrm{rad}(a_1)$") version: hand-verified evidence that it is genuinely insufficient, not merely unproved

Section 14.1 rules out only the specific "force $R\mid x$" instantiation.
The outline's actual intended mechanism is more general: take $x$ merely
$(r,i)$-clean (i.e. $r\mid x$, $R(x)\cap E_i=\emptyset$), for a reference
index $i$ with $P\not\subseteq R(a_i)$ (so 14.1 does not apply), and ask
whether the positive CRT density of such $x$, combined with the sequence's
bounded step size (`bounded-gap-via-rad-a1.md`: $a_{n+1}-a_n\le R$ for
every $n$), forces the greedy process to realize one of them as an actual
term at a bounded index.

We do **not** prove this in general — it remains open, exactly as the
outline warned. What this round adds, beyond restating that it is open, is
a **concrete, fully hand-verified demonstration of exactly why** a natural
strengthening of $(r,i)$-cleanliness (namely: $(r,i)$-clean **and**
additionally satisfying Lemma $Q_0$ against $a_1$, i.e. clearing every
filter that the CRT-density construction can express in closed form) is
still not sufficient for acceptance.

**Setup.** $a_1=35=5\cdot7$, $P=\{5,7\}$. Direct generation from the raw
recursive definition gives (each step verified by hand, checking every
candidate against every earlier term in turn):
$$a_1=35=5\cdot7,\quad a_2=40=2^3\cdot5,\quad a_3=42=2\cdot3\cdot7,\quad
a_4=45=3^2\cdot5,\quad a_5=50=2\cdot5^2,\ \dots$$
(Verification of $a_2$: $36,\dots,39$ each fail $\gcd(\cdot,35)=1$ — $36=
2^2\cdot3^2$, $37$ prime, $38=2\cdot19$, $39=3\cdot13$, none share $5$ or
$7$ with $35$; $40=2^3\cdot5$ shares $5$, accepted. Verification of $a_3$:
$41$ prime fails vs. $35$; $42=2\cdot3\cdot7$ shares $7$ with $35$ and
shares $2$ with $40$, both pass, accepted. Verification of $a_4$: $43$
prime fails vs. $35$; $44=2^2\cdot11$ fails vs. $35$ (no $5$ or $7$
factor); $45=3^2\cdot5$ shares $5$ with $35$, shares nothing even-valued
with $40$ but shares $5$ (indeed $\gcd(45,40)=5$), shares $3$ with $42$
(indeed $\gcd(45,42)=3$) — all constraints pass, accepted.)

Take reference index $i=2$ ($a_2=40=2^3\cdot5$), so $R(a_2)=\{2,5\}$; take
$r=2\in R(a_2)$, giving $E_2=R(a_2)\setminus\{2\}=\{5\}$. Note
$P=\{5,7\}\not\subseteq R(a_2)=\{2,5\}$ (since $7\notin R(a_2)$), so this
reference index falls **outside** the vacuous family ruled out by §14.1 —
this is exactly the "genuinely different, non-vacuous" case the outline's
mechanism is meant to address.

**Candidate.** $x=56=2^3\cdot7$. Check every filter the CRT-density
mechanism controls: (i) $r=2\mid56$ — yes. (ii) $R(56)\cap E_2 =
\{2,7\}\cap\{5\}=\emptyset$ — yes, $(2,2)$-clean. (iii) (the additional,
Lemma-$Q_0$-motivated filter) $R(56)\cap P = \{2,7\}\cap\{5,7\}=\{7\}\ne
\emptyset$ — yes, $x=56$ also hits $R(a_1)$, so it clears the one further
constraint that any CRT-density construction can express in closed form
(a fixed modulus condition guaranteeing legality against $a_1$).

**Yet $x=56$ is not accepted.** Compute $\gcd(56,a_4)=\gcd(56,45)=
\gcd(2^3\cdot7,\,3^2\cdot5)$. The prime factorizations $\{2,7\}$ and
$\{3,5\}$ are disjoint, so $\gcd(56,45)=1$. Hence $56$ **fails** the
recursive definition's constraint against the earlier term $a_4=45$,
and is rejected — regardless of the fact that it cleanly passes every
filter relative to $r=2$, $E_2=\{5\}$, and $P$.

(To confirm $56$ is genuinely excluded from the sequence, not merely
"would fail a hypothetical test": since $56>a_4=45$ and $\gcd(56,45)=1$,
the raw recursive definition — which requires $\gcd(a_{n+1},a_i)>1$ for
*every* $i\le n$, and in particular for $i=4$ once $n\ge4$ — directly
excludes $56$ from being any $a_{n+1}$ with $n\ge4$; and $56>a_3=42$ so it
cannot be $a_3$ either; so $56\notin A$ under the actual definition, not
merely under some derived heuristic.)

**What this shows.** The reference index $i=2$ and prime $r=2$ genuinely
do have a witnessing pair for $\mathrm{Nec}$ (indeed $r=2$ is witnessed by
$(2,3)$: $R(a_2)\cap R(a_3)=\{2,5\}\cap\{2,3,7\}=\{2\}$, confirmed
directly above) — so the *existence* of a clean witness is not in
question here (it already happened, at the very next step $j=3$). What
$x=56$ demonstrates is that **cleanliness relative to one fixed reference
pair's exclusion set, even combined with hitting $R(a_1)$, does not imply
legality against the rest of the (unboundedly growing) prefix** — $56$
fails specifically against $a_4=45$, an index that plays no role at all in
the definition of $E_2$ or $P$. Any attempt to generalize the outline's
mechanism into a genuine bound (e.g. "the *next* $(r,i)$-clean-and-$P$-
hitting integer after $a_i$ is always accepted, or is accepted within a
bounded number of further trials") would have to additionally control
legality against *every* other earlier term — precisely the obstruction
`contamination-dichotomy-and-reduction.md` already flags as
"not obviously easier than the original central existence gap," now
demonstrated concretely rather than asserted abstractly.

#### 14.3 Why the $R(a_1)$-covering trick does not have a single-prime analog

Sections 14.1–14.2 together isolate the precise structural reason the
Multiple-of-$R$ Realization Lemma's proof technique cannot be adapted to a
single recruited prime $r$: that proof works because $R=\mathrm{rad}(a_1)$
is divisible by **every prime that Lemma $Q_0$ guarantees is shared between
$x$ and *any* earlier term** — i.e. a single fixed modulus condition
($R\mid x$) simultaneously guarantees legality against *all* (not just
some fixed finite list of) earlier indices at once, because Lemma $Q_0$
itself is a statement about *every* index $n\ge1$ uniformly. There is no
known analogous fact for a recruited prime $r$: knowing $r\mid a_i$ for one
specific $i$ says nothing about which prime (if any) is shared between $x$
and a *different* earlier term $a_k$ ($k\ne i$) — as $x=56$ above
demonstrates concretely, $a_4=45$'s relevant shared prime with a would-be
accepted term is $3$ or $5$, neither of which is $r=2$ nor a member of
$E_2=\{5\}$'s complement-based construction (indeed $5\in E_2$, so any
$(2,2)$-clean candidate is barred from sharing $5$ with $a_4$, yet $a_4$'s
*other* prime factor $3$ is simply invisible to the construction, which
only tracks $r=2$ and $E_2$). This is the exact sense in which "one
recruited prime's local exclusion data" is structurally weaker than "the
full, fixed, finite set $P=R(a_1)$" — and why no CRT/density argument
built from a single reference pair's data alone can be expected to close
the bridging step without new, additional structure (e.g. simultaneously
tracking exclusion data for *every* earlier index, which reintroduces
the same unbounded/growing-prefix difficulty the whole population has
been stuck on since round 4).

#### 14.4 Net effect of this round

- **Closed (genuine kill):** the literal "force $x$ to be a multiple of
  $\mathrm{rad}(a_1)\cdot r$" instantiation of the outline's mechanism is
  vacuous for the intended witnessing purpose whenever the reference index
  satisfies $P\subseteq R(a_i)$ — an explicit infinite family, not a
  hypothetical corner case (§14.1, Impossibility Lemma, proved in full,
  confirmed by hand for $a_1=35$).
- **Sharpened diagnosis (not a proof, but concrete, not abstract):** for
  reference indices outside that family, even the strongest natural
  strengthening of the mechanism's filters (clean relative to $E_i$ *and*
  hitting $R(a_1)$) is demonstrably insufficient for acceptance, via a
  fully hand-verified counterexample ($a_1=35$, $x=56$, failing against
  $a_4=45$, a term untouched by either filter) — §14.2.
- **Structural explanation (§14.3):** the fundamental reason is that the
  Multiple-of-$R$ Realization Lemma's technique relies on a single fixed
  modulus condition that is guaranteed (via Lemma $Q_0$) to cover *every*
  earlier index uniformly; no analogous uniform guarantee is known, or
  likely to exist without new ideas, for the local exclusion data of a
  single recruited prime.
- **What remains open, honestly:** whether *some* other, genuinely
  different construction (not of the "single reference pair's CRT
  exclusion set" shape) could still bound the witness index or establish
  self-sufficiency of $Q_{\min}$. This round does not attempt such a
  construction; it closes off the specific mechanism assigned by the
  round-7 outline and documents, with hand-verified evidence, exactly
  where and why it fails, so a future round does not have to re-derive
  this diagnosis from scratch. The central existence gap (Nec-finiteness /
  self-sufficiency of $Q_{\min}$) remains **completely open**.

## Promotable lemmas
- **Lemma $Q_0$ (unconditional finite covering set).** For every $n\ge1$,
  $R(a_n)\cap R(a_1)\ne\emptyset$. (Already contained inside the certified
  `lemmas/bounded-gap-via-rad-a1.md` as its internal "Fact"; recommend the
  reviewer additionally certify it as its own standalone lemma file, since
  it is used here independently of the bounded-gap conclusion, purely as a
  covering-set fact with no pigeonhole needed — a genuine simplification
  over the round-1 "every term meets $S$" lemma, which required a pigeonhole
  argument to produce a finite covering set at all.)
- **Proposition B (set-theoretic reformulation of acceptance).** For
  $m>a_1$: $m$ is a term of the sequence iff $\gcd(m,a_i)>1$ for every
  earlier accepted term $a_i<m$. Proved in full above (§2), self-contained,
  depends only on Lemma 0 (well-definedness/monotonicity). Reusable by any
  approach that wants to reason about the accepted or rejected set
  set-theoretically rather than recursively.
- **Lemma P (exact periodicity of a listed union of residue classes).** If
  $C=\{m>c : m\bmod L\in \mathrm{GoodRes}\}$ for a nonempty
  $\mathrm{GoodRes}\subseteq\mathbb Z/L\mathbb Z$, listed increasingly as
  $c_1<c_2<\cdots$, and $T:=|\mathrm{GoodRes}|$, then $c_{j+T}=c_j+L$ for
  *every* $j\ge1$ (not just eventually). Proved in full above (§3),
  self-contained, pure combinatorics, no dependence on the sequence $(a_n)$
  at all. Reusable by any approach (in particular
  `active-set-stabilization.md` and `jacobsthal-covering-bound.md`) once
  they establish that the eventual accepted set is a union of residue
  classes mod some $L$ — it replaces any orbit-pigeonhole telescoping
  argument with a shorter direct proof, and in particular removes any
  temptation to use the (already-flagged, fallacious) "pigeonhole forces
  $\sigma(1)$ to recur" argument for the *set*-periodicity statement (Lemma
  P proves exact periodicity of the listing directly, with no recurrence of
  a specific starting state required).
- **Fact D (recursive step $=$ static $\mathrm{Good}$-minimum, every $n\ge1$,
  no restriction).** For every $n\ge1$, $a_{n+1}=\min\{m>a_n:\mathrm{Good}(m)\}$.
  Proved in full above (§9.1), elementary (a direct unpacking of the
  recursive definition on the interval $(a_n,a_{n+1}]$, where the set of
  indices $i$ with $a_i<m$ is shown to be exactly $\{1,\dots,n\}$), needs
  only Lemma 0. Slightly more elementary and more generally applicable than
  Proposition B (no restriction to $m>a_1$; purely index-local). Useful
  anywhere Proposition B is used to justify a single greedy step.
- **Self-Type-Compatibility Corollary ($\mathrm{Good}_Q(a_1)$ unconditional).**
  For every finite $Q\supseteq R(a_1)$, $\mathrm{Good}_Q(a_1)$ holds — proved
  in full above (§9.2) from the (separately certifiable) Self-Type-
  Compatibility Lemma plus `lemmas/pairwise-non-coprimality.md`. Reusable as
  a base case for any inductive argument attempting to show every accepted
  term is $Q$-Good.
- **Reduction Lemma (Hypothesis SS$(Q,1)$ $\iff$ every term is $Q$-Good).**
  For fixed finite $Q\supseteq R(a_1)$: "$a_{n+1}=\min\{m>a_n:
  \mathrm{Good}_Q(m)\}$ for every $n\ge1$" holds **iff** "$\mathrm{Good}_Q
  (a_n)$ holds for every $n\ge1$." Proved in full above (§9.3), both
  directions, using only Fact D, Lemma S1 (already certified via
  `lemmas/...`/§4 of this file), and the Self-Type-Compatibility Corollary
  for the base case. Reusable by any approach still tracking Gap 1
  (self-sufficiency) and Gap 2 (prefix extension) as separate: this lemma
  shows they are the same gap once stated with $n^*=1$, for any candidate
  $Q$, not specific to the complement-set framing.
- **Transient-free finishing theorem.** If some finite $Q\supseteq R(a_1)$
  satisfies "$\mathrm{Good}_Q(a_n)$ for every $n\ge1$" (the Unified Central
  Claim), then $a_{n+T}=a_n+L$ for *every* $n\ge1$ with $L=L(Q)$,
  $T=|\mathrm{GoodRes}(Q)|$ — no transient index at all. Proved in full above
  (§9.4) by applying Lemma P with $c=a_1-1$ to show $A$ itself (the whole
  accepted set, not merely a tail) equals $\{m\ge a_1:\mathrm{Good}_Q(m)\}$.
  This is the key point that collapses the population's "Gap 2" entirely:
  once the Unified Central Claim is available for some $Q$, no separate
  prefix-extension argument is needed by any approach using this route.
- **Hitting-Set Lemma (new, round 4).** For finite $Q\supseteq R(a_1)$, the
  Unified Central Claim for $Q$ is exactly equivalent to $Q$ being a hitting
  set for the family $\{W(i,j):=R(a_i)\cap R(a_j) : i,j\ge1\}$ of nonempty
  finite prime sets. Proved in full above (§10.1), a one-line unwinding of
  the definitions. Includes the free corollary that $Q_0=R(a_1)$ already
  hits every $W(1,j)$, so the remaining difficulty is confined to pairs not
  involving index $1$. Reusable by any approach wanting to reason about the
  central gap as a set-hitting problem rather than a sequence-acceptance
  problem (in particular useful to `jacobsthal-covering-bound.md`'s
  $\Lambda$-based candidate-$Q$ attempts).
- **Bounded-Radical special cases (new, round 4).** With $R:=\mathrm{rad}
  (a_1)$: (i) $R(a_1)\cap R(a_j)\cap[2,R]\ne\emptyset$ for every $j\ge1$
  (immediate from Lemma $Q_0$, since $R(a_1)=Q_0\subseteq[2,R]$); (ii)
  $R(a_n)\cap R(a_{n+1})\cap[2,R]\ne\emptyset$ for every $n\ge1$ (immediate
  from `lemmas/adjacent-link-lemma.md`, since $\gcd(a_n,a_{n+1})\le R$
  means every one of its prime factors is $\le R$). Proved in full above
  (§11.1). Small, genuinely useful facts: they show any future candidate
  hitting set $Q$ need not separately worry about pairs involving index $1$
  or adjacent pairs — both are free once $Q\supseteq[2,R]\supseteq Q_0$.
- **Bounded-Radical Refutation (new, round 4, negative but reusable).**
  The candidate $Q=\{p\text{ prime}:p\le\mathrm{rad}(a_1)\}$ does **not**
  always satisfy the Unified Central Claim: for $a_1=375$, the terms
  $a_3=380=2^2\cdot5\cdot19$ and $a_7=399=3\cdot7\cdot19$ satisfy
  $R(a_3)\cap R(a_7)=\{19\}$ with $19>\mathrm{rad}(375)=15$. Proved in full
  above (§11.3) by a complete hand-derivation of $a_1,\dots,a_7$ from the
  raw recursive definition (no computer-only step used as a proof step).
  Reusable as a standing counterexample: any future approach proposing a
  closed-form, $a_1$-only-dependent finite hitting set of the form
  $\{p\le f(a_1)\}$ for some simple function $f$ related to $\mathrm{rad}
  (a_1)$ should check it against $a_1=375$ before investing further effort.
- **Chain-Transitivity Obstruction (new, round 4, negative, purely
  set-theoretic, reusable).** Pairwise-consecutive nonempty intersection of
  a chain of sets $\sigma_1,\dots,\sigma_m$ (i.e. $\sigma_k\cap\sigma_{k+1}
  \ne\emptyset$ for every $k$) does **not** imply $\sigma_1\cap\sigma_m\ne
  \emptyset$; witnessed by $\sigma_1=\{1,2\},\sigma_2=\{2,3\},\sigma_3=
  \{3,4\}$. Proved in full above (§11.5(b)), and confirmed to be an
  actively-occurring (not merely hypothetical) pattern in the actual
  sequences (e.g. $50$ disjoint-adjacent-$Q_0$-type instances for $a_1=15$
  among the first $100$ terms). Reusable as a standing warning against any
  future "induct on index gap via chaining" strategy for the central gap,
  for any approach in the population.
- **Multiple-of-$R$ Realization Lemma (new, round 5, unconditional).** Every
  integer $x>a_1$ with $\mathrm{rad}(a_1)\mid x$ is itself an accepted term
  of the sequence. Proved in full below (§12.1), a short direct argument
  from Lemma $Q_0$ and the greedy minimality (no pigeonhole, no auxiliary
  hypothesis). Strictly stronger than the previously-certified
  `bounded-gap-via-rad-a1.md` (which only shows the next multiple of $R$ is
  a *legal candidate*, not that it is *accepted*). Reusable by any approach:
  it pins down an explicit infinite sub-progression of $A$ completely and
  unconditionally, for every $a_1$, with zero exceptions confirmed on all
  tested instances.
- **Same-Class-Free Lemma / Class-Partition Reduction (new, round 5,
  unconditional).** Partitioning indices by $\pi(n):=\min(R(a_n)\cap
  R(a_1))$, any two indices in the same class automatically share a prime
  of $R(a_1)\subseteq Q_{\min}$ (so their pair is free for any valid $Q$),
  and any prime witnessing $\mathrm{Nec}$ via a same-class pair must
  already lie in $R(a_1)$. Proved in full below (§12.2). Reusable by any
  approach working with $\mathrm{Nec}/Q_{\min}$: it confines all remaining
  difficulty (both self-sufficiency and further growth of $\mathrm{Nec}$)
  to cross-class pairs, though (§12.3, reported honestly) this alone does
  not reduce the problem to a finite residual case.
- **Impossibility Lemma for the rad-$(a_1)$-forced single-prime realization
  mechanism (new, round 7, negative but reusable).** For $r\notin
  R(a_1)=:P$ and any reference index $i$ with $P\subseteq R(a_i)$
  (equivalently $\mathrm{rad}(a_1)\mid a_i$ — a condition satisfied by
  $i=1$ always, and by every index of the Multiple-of-$R$ subsequence): no
  integer $x$ with $r\mid x$ and $\mathrm{rad}(a_1)\mid x$ can ever be
  $(r,i)$-clean (i.e. can ever realize a singleton intersection $\{r\}$
  with $a_i$). Proved in full above (§14.1), a short direct argument from
  Lemma $Q_0$; independently confirmed by hand for $a_1=35$, $i=1$, $r=3$
  (every multiple of $3$ avoiding $\{5,7\}$ up to $390$ fails Lemma $Q_0$
  against $a_1$ itself and is rejected). Reusable as a standing warning:
  any future approach proposing to realize a recruited prime $r$ by
  forcing the candidate to also be a multiple of $\mathrm{rad}(a_1)$
  (to piggy-back on the already-certified Multiple-of-$R$ Realization
  Lemma for acceptance) should check this obstruction first — it rules out
  that specific construction for an explicit infinite family of reference
  indices, not just a hypothetical corner case.
- **Insufficiency-of-local-cleanliness counterexample (new, round 7,
  negative but reusable).** For $a_1=35$, reference index $i=2$
  ($a_2=40=2^3\cdot5$), $r=2$, $E_2=\{5\}$: the integer $x=56=2^3\cdot7$
  is $(2,2)$-clean and additionally hits $R(a_1)=\{5,7\}$ (via $7$), yet
  is not accepted, because $\gcd(56,45)=1$ where $a_4=45=3^2\cdot5$ is an
  earlier term untouched by either filter. Proved in full above (§14.2),
  fully hand-verified from the raw recursive definition (all of
  $a_1,\dots,a_5$ derived and checked by hand). Reusable as a standing,
  concrete (not merely abstract) demonstration that CRT-cleanliness
  relative to one fixed reference pair, even combined with hitting
  $R(a_1)$, is not sufficient for legality against the rest of the
  (unboundedly growing) prefix — any future single-reference-pair
  CRT/density construction for bounding a witness index should be checked
  against this instance before being trusted.

### 12. Round 5 build: the Multiple-of-$R$ Realization Lemma, a Class-Partition
Reduction, and refutation of the bounded-index-gap density mechanism

This section attacks the round-5 outline's assigned target for this approach
("redundant-covering density": show that once a prime's divisibility index
set is dense enough, every later pair sharing that prime automatically also
shares a second $Q_{\min}$-prime, blocking further growth of $\mathrm{Nec}$).
Throughout, $P:=R(a_1)=Q_0$ (finite, nonempty, by definition of $a_1>1$), and
we use the already-certified Fact (`lemmas/bounded-gap-via-rad-a1.md`,
internal Fact; restated as "Lemma $Q_0$" in §0 above): **for every $n\ge1$,
$R(a_n)\cap P\ne\emptyset$.**

#### 12.1 The Multiple-of-$R$ Realization Lemma (new, fully proved, unconditional)

**Lemma (Multiple-of-$R$ Realization).** Let $R:=\mathrm{rad}(a_1)=\prod_{p\in
P}p$. For every integer $x$ with $x>a_1$ and $R\mid x$, $x$ is an accepted
term of the sequence, i.e. $x\in A=\{a_n:n\ge1\}$.

*Proof.* Since $x>a_1$ and $(a_n)_{n\ge1}$ is strictly increasing with
$a_n\to\infty$ (Lemma 0, `lemmas/existence.md`), the set $\{n\ge1:a_n<x\}$ is
nonempty (it contains $n=1$, as $a_1<x$) and finite; let $k$ be its largest
element, so
$$a_k<x\quad\text{and}\quad a_{k+1}\ge x \tag{12.1}$$
(the second inequality holds because if $a_{k+1}<x$ then $k+1$ would also
belong to $\{n:a_n<x\}$, contradicting maximality of $k$).

We claim $x$ is a legal candidate for the greedy step at $k$, i.e. $x>a_k$
(already shown in (12.1)) and $\gcd(x,a_i)>1$ for every $i=1,\dots,k$. Fix
$i\in\{1,\dots,k\}$. By Lemma $Q_0$, $R(a_i)\cap P\ne\emptyset$; let
$p\in R(a_i)\cap P$, so $p\mid a_i$. Since $p\in P$ and $R=\prod_{q\in P}q$,
we have $p\mid R$, and since $R\mid x$ (hypothesis), $p\mid x$. Hence $p$ is
a common prime factor of $x$ and $a_i$, so $\gcd(x,a_i)\ge p>1$. As $i$ was
arbitrary in $\{1,\dots,k\}$, $x$ satisfies every constraint of the greedy
step at $k$.

By the defining property of the sequence, $a_{k+1}$ is the *smallest*
integer exceeding $a_k$ satisfying $\gcd(\cdot,a_i)>1$ for $i=1,\dots,k$;
since $x$ is one such integer (just shown), minimality gives $a_{k+1}\le x$.
Combined with $a_{k+1}\ge x$ from (12.1), we conclude $a_{k+1}=x$, so
$x\in A$. $\blacksquare$

**Remark.** This is strictly stronger than the previously-certified
`bounded-gap-via-rad-a1.md`, which only shows the least multiple of $R$
exceeding $a_n$ is a *legal candidate* (hence $a_{n+1}-a_n\le R$) — it does
not claim that multiple is itself *accepted*. The lemma above shows every
single multiple of $R$ beyond $a_1$, with no exception, is realized as an
actual term of the sequence. In particular $A$ contains the full arithmetic
progression $\{a_1+R,a_1+2R,\dots\}$ rounded up to multiples of $R$ — more
precisely, $A\supseteq\{kR:k\ge1,\ kR>a_1\}$.

**Numerical confirmation (evidence only, not a proof step).** Checked for
$a_1\in\{15,21,35,45,63,105,165,210,315,375,429,1425,2310\}$, testing every
multiple of $R=\mathrm{rad}(a_1)$ up to the last generated term (several
thousand terms per instance): zero exceptions in every case. E.g. for
$a_1=15$ ($R=15$), the generated sequence begins
$15,18,20,24,30,36,40,42,45,48,50,54,60,\dots$ and indeed $30=a_5$,
$45=a_9$, $60=a_{13}$ are all multiples of $15$ appearing exactly as
predicted, with no multiple of $15$ beyond $a_1$ ever skipped.

#### 12.2 The Same-Class-Free Lemma and the Class-Partition Reduction

**Definition (owning prime).** By Lemma $Q_0$, $R(a_n)\cap P\ne\emptyset$
for every $n\ge1$. Define $\pi(n):=\min(R(a_n)\cap P)$ (smallest prime of
$P$ dividing $a_n$, using the usual ordering of primes) — a well-defined
function $\pi:\mathbb Z_{\ge1}\to P$. Let $C_p:=\pi^{-1}(p)$ for $p\in P$;
these sets partition $\mathbb Z_{\ge1}$ into $|P|$ (possibly empty, though
$C_{\pi(1)}\ni1$ so at least one is nonempty) classes.

**Same-Class-Free Lemma.** For any finite $Q\supseteq P$ (in particular for
$Q=Q_{\min}=\mathrm{Nec}\cup R(a_1)$, since $R(a_1)=P\subseteq Q_{\min}$),
and any $i\ne j$ with $\pi(i)=\pi(j)$ ($i,j$ in the same class), the pair
$(i,j)$ is automatically hit: $W(i,j)\cap Q\ne\emptyset$.

*Proof.* Let $p:=\pi(i)=\pi(j)\in P$. By definition of $\pi$, $p\mid a_i$
and $p\mid a_j$, so $p\in R(a_i)\cap R(a_j)=W(i,j)$. Since $p\in P\subseteq
Q$, $p\in W(i,j)\cap Q$. $\blacksquare$

**Corollary (Nec is witnessed outside $P$ only by cross-class pairs).** If
$p\in\mathrm{Nec}\setminus P$ (i.e. $p$ is the unique common prime factor of
some pair $a_i,a_j$, and $p\notin P$), then $\pi(i)\ne\pi(j)$.

*Proof.* Suppose for contradiction $\pi(i)=\pi(j)=:q$. By the Same-Class-Free
Lemma's proof (with $Q=P$, which trivially contains itself), $q\in
R(a_i)\cap R(a_j)$. Since $p\in\mathrm{Nec}$ is witnessed by this same pair,
$R(a_i)\cap R(a_j)=\{p\}$ (singleton, by the definition of $\mathrm{Nec}$),
so $q=p$. But $q=\pi(i)\in P$ by construction, contradicting $p\notin P$.
$\blacksquare$

**Consequence (a genuine, but not yet sufficient, reduction of the central
gap).** Combined with the certified `hitting-set-lemma.md`, this shows: the
*only* pairs $(i,j)$ that can (a) fail to be $Q_{\min}$-hit, or (b) force a
new element into $\mathrm{Nec}\setminus P$, are **cross-class pairs**
($\pi(i)\ne\pi(j)$). Same-class pairs (within a single fixed $C_p$, $p\in
P$) are unconditionally safe, for *any* finite $Q\supseteq P$, regardless of
how large or numerous they are — no density or recurrence argument is
needed for them at all, only membership in $P$.

#### 12.3 Testing whether this reduction alone finishes the gap: it does not

Define the **$P$-problematic pairs**
$$\mathcal P:=\{(i,j):i\ne j,\ R(a_i)\cap R(a_j)\cap P=\emptyset\}$$
(a subset of the cross-class pairs, by the contrapositive of the Same-Class-
Free Lemma's proof — indeed if $R(a_i)\cap R(a_j)\cap P=\emptyset$ then in
particular $\pi(i)\ne\pi(j)$, since otherwise $\pi(i)=\pi(j)$ would put a
common element of $P$ in the intersection). Every pair *not* in $\mathcal P$
shares a prime of $P\subseteq Q_{\min}$, hence is automatically
$Q_{\min}$-hit; so the entire remaining difficulty of the central gap is
confined to $\mathcal P$.

If $\mathcal P$ were finite, this reduction alone would show $\mathrm{Nec}$
is finite (only finitely many pairs remain to check, each contributing at
most one prime to $\mathrm{Nec}$) and $Q_{\min}$ could be tested for
self-sufficiency by a finite check. **This is not the case.** Computational
check (evidence only, not a proof step): for $a_1\in\{15,35,375\}$, counting
pairs among the first $400$ generated terms with $R(a_i)\cap R(a_j)\cap
P=\emptyset$ gives $20000$, $13488$, and $6024$ such pairs respectively out
of $\binom{400}{2}=79800$ total pairs — a large and, on the ranges tested,
non-shrinking fraction, giving no indication that $\mathcal P$ is finite.
So while the Class-Partition Reduction is a genuine, rigorous narrowing (it
rules out same-class pairs entirely, for free, for any $a_1$), it does
**not** by itself reduce the central gap to a finite residual problem —
$\mathcal P$ itself is (numerically) an infinite family requiring further
structure to control, exactly the same order of difficulty as the original
unrestricted central gap. This is reported honestly as a genuine but
insufficient reduction, not a closing argument.

#### 12.4 Refutation of the specific "bounded index-gap" density mechanism

The round-5 outline's concrete proposed mechanism for redundant-covering
density is: for each prime $p\in Q_{\min}$, the divisibility index set
$I_p:=\{n:p\mid a_n\}$ has *bounded index gaps* — specifically, motivated by
small examples, that consecutive elements of $I_p$ differ by at most $p$
itself, which (if true) would drive a multiplicity-$\ge2$ argument
sufficient to block further growth of $\mathrm{Nec}$. We test and refute
this precise form.

**Refutation (fully hand-verified counterexample).** Take $a_1=385=
5\cdot7\cdot11$, so $P=\{5,7,11\}$, $R=\mathrm{rad}(385)=385$. We compute
$a_1,\dots,a_8$ by hand, directly from the recursive definition, checking
every candidate against every earlier term.

- $a_1=385=5\cdot7\cdot11$.
- $a_2$: smallest $m>385$ with $\gcd(m,385)>1$, i.e. $m$ divisible by $5$,
  $7$, or $11$. Checking $386=2\cdot193$, $387=3^2\cdot43$, $388=2^2\cdot97$,
  $389$ (prime): none divisible by $5,7,11$. $390=2\cdot3\cdot5\cdot13$ is
  divisible by $5$. So $a_2=390$.
- $a_3$: smallest $m>390$ with $\gcd(m,385)>1$ and $\gcd(m,390)>1$.
  $391=17\cdot23$: not divisible by $5,7,11$, fails the first condition.
  $392=2^3\cdot7^2$: divisible by $7$ (first condition OK, shares $7$ with
  $385$); shares $2$ with $390=2\cdot3\cdot5\cdot13$ (second condition OK).
  So $a_3=392$.
- $a_4$: smallest $m>392$ passing vs. $385,390,392$. $393=3\cdot131$: not
  divisible by $5,7,11$ (fails vs. $385$). $394=2\cdot197$: same failure.
  $395=5\cdot79$: divisible by $5$ (OK vs. $385$, and shares $5$ with
  $390$), but $\gcd(395,392)=\gcd(5\cdot79,2^3\cdot7^2)=1$ (fails vs.
  $392$). $396=2^2\cdot3^2\cdot11$: divisible by $11$ (OK vs. $385$); shares
  $2,3$ with $390$ (OK); shares $2$ with $392$ (OK). So $a_4=396$.
- $a_5$: smallest $m>396$ vs. $385,390,392,396$. $397$ (prime): fails vs.
  $385$. $398=2\cdot199$: fails vs. $385$. $399=3\cdot7\cdot19$: divisible
  by $7$ (OK vs. $385$); shares $3$ with $390$; shares $7$ with $392$;
  shares $3$ with $396$. All pass. So $a_5=399$.
- $a_6$: smallest $m>399$ vs. $385,390,392,396,399$. $400=2^4\cdot5^2$:
  divisible by $5$ (OK vs. $385,390,392$-via-$2$,$396$-via-$2$), but
  $\gcd(400,399)=\gcd(2^4\cdot5^2,3\cdot7\cdot19)=1$ (fails vs. $399$).
  $401$ (prime): fails vs. $385$. $402=2\cdot3\cdot67$: fails vs. $385$
  (not divisible by $5,7,11$). $403=13\cdot31$: fails vs. $385$.
  $404=2^2\cdot101$: fails vs. $385$. $405=3^4\cdot5$: divisible by $5$
  (OK vs. $385,390$), shares $3$ with $396$, but $\gcd(405,392)=
  \gcd(3^4\cdot5,2^3\cdot7^2)=1$ (fails vs. $392$). $406=2\cdot7\cdot29$:
  divisible by $7$ (OK vs. $385$); shares $2$ with $390$; shares $2,7$
  with $392$; shares $2$ with $396$; shares $7$ with $399$. All pass. So
  $a_6=406$.
- $a_7$: smallest $m>406$ vs. $385,390,392,396,399,406$. $407=11\cdot37$:
  divisible by $11$ (OK vs. $385$), but $\gcd(407,390)=1$ (fails vs.
  $390$). $408=2^3\cdot3\cdot17$: fails vs. $385$. $409$ (prime): fails vs.
  $385$. $410=2\cdot5\cdot41$: divisible by $5$ (OK vs. $385,390,392$-via-
  $2,396$-via-$2$), but $\gcd(410,399)=\gcd(2\cdot5\cdot41,3\cdot7\cdot19)
  =1$ (fails vs. $399$). $411=3\cdot137$: fails vs. $385$. $412=2^2\cdot
  103$: fails vs. $385$. $413=7\cdot59$: divisible by $7$ (OK vs. $385$),
  but $\gcd(413,390)=1$ (fails vs. $390$). $414=2\cdot3^2\cdot23$: fails
  vs. $385$. $415=5\cdot83$: divisible by $5$ (OK vs. $385,390$), but
  $\gcd(415,392)=1$ (fails vs. $392$). $416=2^5\cdot13$: fails vs. $385$.
  $417=3\cdot139$: fails vs. $385$. $418=2\cdot11\cdot19$: divisible by
  $11$ (OK vs. $385$); shares $2$ with $390,392,396,406$; shares $19$ with
  $399$. All pass. So $a_7=418$.
- $a_8$: smallest $m>418$ vs. $385,390,392,396,399,406,418$. $419$
  (prime): fails vs. $385$. $420=2^2\cdot3\cdot5\cdot7$: divisible by $5,7$
  (OK vs. $385$); shares $2,3,5$ with $390$; shares $2,7$ with $392$;
  shares $2,3$ with $396$; shares $3,7$ with $399$; shares $2,7$ with
  $406$; shares $2$ with $418$. All pass. So $a_8=420$.

This gives $a_1,\dots,a_8 = 385,390,392,396,399,406,418,420$, matching an
independent exact-integer simulation exactly (used only as a sanity check,
not as part of this written proof).

Now examine $I_5=\{n:5\mid a_n\}$ restricted to this range: $5\mid a_1=385$,
$5\mid a_2=390$, and (checking each of $a_3,\dots,a_7$ above) $5\nmid
392,396,399,406,418$, while $5\mid a_8=420$. So the two consecutive elements
of $I_5$ nearest here are index $2$ and index $8$, an **index gap of
$8-2=6$**, strictly greater than $p=5$. This directly refutes, by a fully
hand-verified example, the claim "consecutive elements of $I_p$ (for
$p\in P$) differ in index by at most $p$" — the specific mechanism proposed
for redundant-covering density.

This is not merely a boundary artifact of a hand-picked example: a
systematic (computational, evidence-only) sweep over $a_1=3,\dots,1999$
with $|R(a_1)|\ge2$, checking every prime $p\in R(a_1)$'s index-gap over the
first $400$ terms of each sequence, found violations for several further
values (e.g. $a_1=315,p=7$: index gap $11>7$; $a_1=429,p=11$: index gap
$14>11$; $a_1=1425,p=19$: index gap $25>19$), confirming $a_1=385$ is not an
isolated pathology. **No bound of this simple closed form (index gap $\le
p$) holds in general**, and the present round found no alternative bound
(e.g. index gap $\le\mathrm{rad}(a_1)$, or a value-gap bound) that is both
supported by all tested data *and* has a rigorous proof — the value-gap
variant (consecutive $I_p$-elements' actual integer *values*, not indices,
differing by at most $R=\mathrm{rad}(a_1)$) was numerically consistent with
every test performed this round, but no proof of it was found or attempted
to completion within this round's time budget, so it is recorded here only
as an **open, untested-by-proof observation** for a future round, explicitly
not claimed.

#### 12.5 Net effect of this round

This round's assigned target (redundant-covering density) is **not
established** — the specific mechanism proposed (bounded index-gap $\le p$)
is refuted by a complete hand-verified counterexample, and the natural
structural reduction that was found instead (Class-Partition Reduction,
§12.2) is proved correct but shown (computationally) insufficient by itself
to finish the central gap (§12.3): the residual "$P$-problematic pair" set
$\mathcal P$ is not finite on any tested range. The round's positive,
fully-proved, unconditional contribution is the Multiple-of-$R$ Realization
Lemma (§12.1) — a genuinely new structural fact (every multiple of
$\mathrm{rad}(a_1)$ beyond $a_1$ is an accepted term, not merely a legal
candidate) not previously established anywhere in the population — and the
Same-Class-Free Lemma / Class-Partition Reduction (§12.2), which cleanly
isolates the central gap's remaining difficulty to cross-class pairs. Both
are proposed below for promotion. The central existence gap itself (does a
finite self-sufficient $Q$ exist? equivalently, is $\mathrm{Nec}$ finite and
$Q_{\min}$ self-sufficient?) remains **fully open** after this round.

## Round 7 revision — Generalized Multiple-of-$r$ Realization Lemma via CRT-positive-density

The round-7 Nec-finiteness explorer's opening (1) is a genuinely new,
concrete lever, directly building on this approach's own certified
`multiple-of-r-realization.md` (which only covers $r\mid\mathrm{rad}(a_1)$).
The explorer correctly flags the naive version as circular/insufficient by
itself (positive CRT density among *integers* says nothing about which
integers the greedy rule actually *selects*, and at what index) — this
revision is designed specifically to avoid that trap by tying the density
statement to the already-certified bounded-gap machinery, not treating
density alone as a finish.

**New Target for this approach (does not replace the central existence
question, sharpens the specific mechanism used to attack it):** for a
prime $r\in\mathrm{Nec}\setminus R(a_1)$ (a genuinely recruited prime),
prove a **Generalized Realization Lemma**: every sufficiently large
multiple of $L':=\mathrm{rad}(a_1)\cdot r$ (beyond some explicit bound
depending only on $a_1$ and $r$) is itself an accepted term of the
sequence — strictly generalizing `multiple-of-r-realization.md`'s $r=1$
case (i.e. plain multiples of $\mathrm{rad}(a_1)$) to include one
recruited prime $r$ as well.

**Skeleton:**
1. Fix $r\in\mathrm{Nec}\setminus R(a_1)$ witnessing a pair $(a_i,a_j)$,
   $i<j$, with $R(a_i)\cap R(a_j)=\{r\}$ (definition of $\mathrm{Nec}$,
   cite `nec-necessity.md`). Let $E$ be the (finite, by
   `contamination-dichotomy-and-reduction.md`'s Contamination Dichotomy)
   set of primes that "contaminate" candidate multiples of $r$ near index
   $j$ — i.e. the primes that can cause a multiple of $r$ to be rejected
   for reasons unrelated to $r$ itself.
2. **CRT-density step (elementary, should be free):** among multiples of
   $r$, those additionally avoiding every prime in $E$ have density
   $\prod_{s\in E}(1-1/s)>0$ (standard CRT/inclusion-exclusion — cite
   `knowledge_base.md`'s CRT entry). Call these the *clean* multiples of
   $r$.
3. **Bridging step (the actual open gap, NOT free — this is where the
   explorer's caution applies):** show that the greedy sequence, once it
   is forced to advance through an interval of length $\le\mathrm{rad}(a_1)$
   at every step (cite `bounded-gap-via-rad-a1.md` /
   `sharpened-bounded-gap-lemma.md`), **must eventually land on a clean
   multiple of $r$ at a bounded index** — NOT merely that clean multiples
   exist with positive density among all integers. Candidate mechanism:
   combine the Sharpened Bounded-Gap Lemma (gap $\le R-r_n$ from the
   current residue) with the CRT density bound via a quantitative
   "positive density in every sufficiently long interval $\Rightarrow$ hit
   within a bounded number of steps of size $\le R$" argument (this is the
   step that must NOT be skipped — it is exactly the missing bridge the
   Contamination Dichotomy Lemma already flagged as unresolved).
4. If step 3 succeeds, combine with the Class-Partition Reduction (§12.2,
   already certified) to argue that repeating this one-prime-at-a-time
   realization argument for every element of $\mathrm{Nec}\setminus R(a_1)$
   in turn (in the order they are first recruited) shows $Q_{\min}$ is
   self-sufficient, closing the central gap. This final assembly step is
   itself new and unproved — flag it as a separate sub-gap, since applying
   the one-prime realization argument $|\mathrm{Nec}\setminus R(a_1)|$
   times requires the exclusion sets $E$ for later primes to stay
   compatible with (not undo) the realization already achieved for earlier
   primes.

**Key lemmas (claim + mechanism):**
- CRT-density-of-clean-multiples (step 2) — because a finite union of
  residue-class exclusions removes exactly a $\prod(1-1/s)$ fraction, by
  inclusion-exclusion over independent (coprime) moduli.
- Generalized Realization Lemma (steps 1-3, OPEN, the hard part) — because
  (conjectured) a set of positive density in $\mathbb Z$ that recurs in
  every window of length $O(\mathrm{rad}(a_1))$ must be hit by a sequence
  that is forced to advance by at most $\mathrm{rad}(a_1)$ at each step —
  this implication needs an explicit quantitative argument (e.g. via the
  pigeonhole/interval-covering technique already used for
  `multiple-of-r-realization.md`'s own proof, adapted to a density-$<1$
  target set rather than the density-$1$ set of all multiples of
  $\mathrm{rad}(a_1)$), not yet supplied.

**Open gaps:** step 3 (the density-to-realization bridge — explicitly the
gap the explorer warns is the crux of the whole reduction) and step 4
(assembling one-prime realization into full self-sufficiency of $Q_{\min}$)
are both unproved.

**Cases to cover:** none beyond the general prime $r$ (the argument is
meant to be uniform in $r$); however the builder must check the
$a_1=35409$ outlier (witness index $95$ for prime $23$, per the
Nec-finiteness explorer) against whatever explicit bound step 3 produces,
as a live sanity check — if the bound produced is smaller than $95$ for
that instance, the argument is wrong, not just incomplete.

**Watch out for:** do NOT present the CRT-density fact (step 2) alone as
if it closes anything — the explorer explicitly flags this as the
circularity trap already warned against in
`contamination-dichotomy-and-reduction.md`; a valid write-up must include
an explicit quantitative bridge (step 3) tying density to a bounded-index
hitting guarantee for THIS specific bounded-gap-constrained sequence, not
a general density-of-integers statement.
