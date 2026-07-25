## imo-2026-06

### Distinct openings (genuinely different top-level framings, far from the Q/Good_Q machinery)

**E. Induction-on-seed / renormalization framing (most promising of these, still speculative).**
Instead of fixing $a_1$ and trying to construct $Q$ or $L$ forward along the
one sequence, do **strong induction on a well-founded measure of the seed**
itself — e.g. on $\omega(a_1):=$ number of distinct prime factors of $a_1$,
or on $R=\mathrm{rad}(a_1)$, or on $a_1$ directly. The reduction step would
be: show that once some prime $p\in R(a_1)$ becomes "permanently locked"
(i.e. $p$ divides *every* sufficiently large accepted term — this is a
provable-looking claim, see below), the tail of the sequence restricted to
"new" primes recruited after the lock behaves like an instance of the *same
kind* of greedy process but with a strictly smaller effective seed (fewer
free primes / smaller radical), so the inductive hypothesis applies to the
tail and periodicity propagates back. This entirely sidesteps proving
existence of a single self-sufficient $Q$ in one shot — periodicity would
instead be *inherited* from a smaller instance via a renormalization step,
which is a different proof shape than any of the 4 dead mechanisms (all of
which tried to directly bound or construct $Q$ for the *whole* sequence at
once). Risk: the "permanent lock" claim itself may be exactly as hard as
the central gap (rounds 1–3's memory rule 9/10 show $Q$/$L$ do *not* have a
simple closed form in terms of $a_1$, e.g. $a_1=33$ vs $a_1=99$ have
identical radicals but wildly different $(T,L)$ — so any renormalization
step must be careful not to assume a false uniform "smallest prime always
locks first" rule). Not yet attempted by any approach in the population —
genuinely new proof architecture, not a rephrasing of Q-existence.

**F. Subword-complexity / Morse–Hedlund framing (explicitly the "gaps as a
formal language" angle requested).**
The certified `bounded-gap-via-rad-a1.md` gives an unconditional fact:
$d_n=a_{n+1}-a_n\in\{1,\dots,R\}$ for every $n\ge1$ — i.e. $(d_n)$ is an
infinite word over a **fixed finite alphabet**, known from round 1 (no
transient). The classical **Morse–Hedlund theorem** (a one-sided infinite
word over a finite alphabet is eventually periodic iff its subword
complexity function $p(k)$ (number of distinct length-$k$ factors) satisfies
$p(k)\le k$ for some $k$, equivalently $p(k)$ does not grow linearly) gives
a *different sufficient condition* to target: instead of constructing $Q$,
try to prove $(d_n)$ has bounded subword complexity. This is a genuinely
different top-level target (a combinatorics-on-words statement, not a
number-theoretic covering statement) and is **not in `knowledge_base.md`**
(only order/periodicity-mod-$m$ entries exist there — cite Morse–Hedlund as
an external classical fact, not a KB entry, if used). **Major risk,
already partially foreshadowed by a dead mechanism**: the certified
`windowed-epsilon-automaton-failure.md` proves that a *bounded window* of
the pair $(d_n,\gcd(a_n,a_{n+1}))$ cannot determine the next symbol in
general (period-7 exceptional-step pattern invisible to any fixed window
for $a_1=21$) — this is closely related to (but not identical to) subword
complexity of $(d_n)$ itself: a period-7 hidden pattern in $\epsilon_n$ is
compatible with $(d_n)$ having LOW complexity (e.g. $d_n\equiv3$ constant
for $a_1=21$, complexity $p(k)=1$ for all $k$ — already eventually periodic
trivially there). The real question is whether $(d_n)$'s complexity stays
bounded for the *hard* instances (e.g. $a_1=99,385$) — this is unverified
and could independently need exactly the same unbounded-memory obstruction
that already killed the windowed automaton. Treat as high-risk; worth a
cheap numeric subword-complexity check before committing an approach to
it (see Cheap-kill candidates below).

**G. Complement / exclusion-witness framing (dual to Q, but tracks
rejections instead of coverage).**
Rather than building a finite set $Q$ of primes that *includes* every term
into a common family, directly study $B:=\{m>a_1: m\notin\{a_n\}\}$ (the
rejected integers, characterized exactly by the certified
`set-theoretic-acceptance-characterization.md`: $m$ is rejected iff some
earlier accepted $a_i<m$ has $\gcd(a_i,m)=1$). Try to show the "reason for
rejection" — formalized as, say, the *set of earlier accepted terms that
are coprime to $m$* — stabilizes to a pattern with finite information
content, without ever naming a finite covering set $Q$ explicitly. This is
conceptually the same target reformulated as an "exclusion" statement
rather than an "inclusion" one; I ran a quick exploratory computation (see
Small-case notes) and it did **not** show any obviously bounded/finite
exclusion-witness structure in a naive framing (the set of prime factors of
*rejected* candidates grows unboundedly, as expected, so a naive dual
framing is not obviously easier) — flagging this as a weaker/likely-dead
opening unless refined (e.g. track only the *minimal* rejecting index $i$,
not all prime factors of the candidate, which was not what I tested).

**H. Explicit density / sieve computation of $L$ via Legendre–Jacobsthal
inclusion–exclusion (targets $L$'s value directly, algebraically).**
Attempt to *compute* a specific candidate $L$ from $a_1$ via a sieve
identity (density of integers $\equiv$-covered by the primes of $R(a_1)$
within one period, à la Legendre's formula / Jacobsthal's function $g(R)$),
then verify periodicity for that specific $L$ directly by finite
computation/induction rather than proving abstract existence. This is
close in spirit to the already-dead "$g(Q)$ threshold" and "prime-size
threshold" mechanisms (jacobsthal-covering-bound, rounds 1–2) and to the
tautological $\Lambda$-split (round 3) — **flagging explicitly that this
opening is very likely to re-derive one of the four dead mechanisms** unless
it uses a genuinely different sieve identity (e.g. an *exact* rather than
asymptotic count via CRT on the *specific*, already-certified
`periodicity-of-residue-class-union.md` structure). Lower priority; include
only if the outliner wants a fourth rival and is confident it differs
structurally from the dead ones.

### Candidate technique(s)
- Strong induction / well-founded descent on a measure of the seed $a_1$
  (opening E) — not currently in `knowledge_base.md`; this is a proof
  *architecture* (induction on a parameter of the problem instance), listed
  under "General Proof Methods" broadly (induction/minimal counterexample)
  but no specific KB entry for "renormalize a greedy sequence by removing a
  locked prime."
- Morse–Hedlund subword-complexity criterion for eventual periodicity of
  infinite words (opening F) — classical combinatorics-on-words result, not
  present in `knowledge_base.md`; would need to be stated and used from
  scratch if invoked (cite as an external classical fact, prove or cite the
  standard proof, do not just assert it).
- Sieve/inclusion–exclusion (Legendre/Jacobsthal-type) exact density
  computation (opening H) — closely related to
  `knowledge_base.md`'s Number Theory section entries on periodicity mod
  $m$; high overlap risk with dead mechanisms, see above.

### Cheap-kill candidates
- **For opening F (subword complexity)**: before committing, compute $p(k)$
  (number of distinct length-$k$ factors of $(d_n)$) numerically for a hard
  instance like $a_1=99$ or $a_1=385$ out to a few thousand terms, for
  $k=1,\dots,20$; if $p(k)$ grows roughly linearly (no compression), this
  framing is dead immediately and should not be built. This is a
  <5-minute check any builder should run first.
- **For opening E**: check numerically whether, once a prime $p\in R(a_1)$
  first divides two consecutive terms in a row, it divides *every*
  subsequent term (the literal "permanent lock" claim) for several hard
  instances (35, 99, 385) — if false even once, the naive renormalization
  step needs real work, not just bookkeeping.
- **For opening G**: as tested below, a naive "prime factors of rejected
  candidates" statistic is unbounded — not itself a kill of the framing,
  but a kill of the *naive* version; a refined version tracking only
  minimal witnessing indices was not tested (out of scope this round).

### Knowledge-base entries to use
- No direct KB entry names the Morse–Hedlund theorem, sieve/Jacobsthal
  density, or renormalization induction — all three openings above would
  need external/from-scratch justification, not a KB citation. Existing KB
  entries already in use by the live population (order/periodicity mod $m$,
  general induction/minimal-counterexample, pigeonhole) remain the closest
  matches; see `knowledge_base.md` Number Theory + General Proof Methods
  sections.

### Analogous past problems (cruxes)
- `aimo-0680` (IMO-SL 2015 N4, already known/used by this population): closest
  overall analog — same conclusion shape (eventually periodic shift), but its
  finishing technique ("divisible by all $n$ $\Rightarrow$ equal") was
  already tried and shown **not** to transplant (active-set-stabilization,
  round 3: the needed unconditional fact $k\mid a_{n+k}-a_n$ is false here).
  Do not re-attempt that specific finishing move; the rest of its solution
  structure (injectivity + AP-per-orbit visualization) may still be worth a
  fresh look for opening E's renormalization idea, since aimo-0680's Step 2
  ("every orbit $n,f(n),f^2(n),\dots$ is an arithmetic progression") is
  structurally close to what a renormalized sub-sequence would need to be.
- `aimo-0341` (IMO-SL covering-system problem, `divisibility-and-gcd`/
  covering subtopic): genuinely relevant crux move for **opening E** —
  its descent technique is "peel one prime out of a composite covering
  system's period, splitting the covering into two sub-coverings of
  strictly smaller period, then recombine the two separately-proved
  bounds." This is exactly the *shape* of a renormalization-by-locked-prime
  argument (reduce to a strictly smaller instance by removing one prime's
  worth of structure), even though the underlying problem (a static
  covering system of $\mathbb Z$ by fixed APs) is different from our
  recursively-generated greedy sequence. Worth reading in full if the
  outliner opens approach E.
- `aimo-0224` (Peru, IMO-SL, `induction-and-construction`): constructs a
  sequence with a prescribed pairwise-coprimality pattern by tagging each
  term with a *set of primes* $I_n$ and arranging $I_m\cap I_n\ne\emptyset$
  iff a combinatorial condition on $m,n$ — i.e. it is the **construction**
  dual of our problem's covering condition. Not directly analogous (our
  problem is extraction/greedy, not free construction) but confirms that
  "encode pairwise intersection via a prime-tagging scheme" is a load-bearing
  crux move elsewhere; already effectively what the Q-machinery does, so
  this does not open a new avenue, just corroborates the framing already in
  use.
- `aimo-0447` (grid prime-covering counting bound): same
  "gcd$>1$ for every pair $\Rightarrow$ place a witnessing prime in a grid
  cell" encoding as our $Q$/$\mathrm{Good}_Q$ machinery, but its finishing
  move is a **counting/density bound** on how many cells one prime can
  occupy (via $\sum 1/p^2$, $\sum 1/p$ estimates) to get a *quantitative
  lower bound* on $\min(a,b)$ — not an eventual-periodicity conclusion.
  Not directly transplantable, but its "at least half the grid's primes
  are large, hence a whole row is forced to use very few large primes"
  argument is a  precedent for a *density*-based approach in the same
  qualitative style as opening H; flagging only as weak inspiration, not a
  strong crux match.

No corpus problem found matches this problem's exact combination of
(recursively-defined greedy sequence) + (eventual periodic-shift
conclusion) other than `aimo-0680`, already fully mined by the population.

### Prior progress
Per `current.md`/`reduction-lemma-ss1-vs-unified-claim.md`: the entire
remaining proof is proven (Reduction Lemma, round 3, independently
verified) to reduce to one unified statement — does a finite $Q\supseteq
R(a_1)$ exist with $\mathrm{Good}_Q(a_n)$ true for every $n\ge1$? If so,
`transient-free-finishing-theorem.md` finishes immediately, with no
transient. All openings E–H above are attempts to reach the *conclusion*
$a_{n+T}=a_n+L$ by a route that does not pass through proving this specific
existence statement about $Q$ — none of them currently has a complete
argument; each is an unexplored direction, not a partial result.

### Dead ends (do not retry)
Per `run_state.md` Rules (already binding on this problem, reproduced for
convenience — do not re-propose any of these four):
1. $g(Q)$ covering-gap threshold mechanism (jacobsthal-covering-bound,
   rounds 1–2) — concrete counterexample $a_1=35$.
2. Prime-size threshold strengthening of (1) — also refuted.
3. $\Lambda$-split reduction $Q=\Lambda\cup(Q\setminus\Lambda)$
   (jacobsthal-covering-bound, round 3) — proven tautological
   (`finite-subtraction-vacuous.md`).
4. Windowed $\epsilon_n$ automaton on bounded relative-gap history
   (bounded-link-invariant, round 3) — proven impossible in general
   (`windowed-epsilon-automaton-failure.md`, period-7 hidden pattern
   invisible to any fixed window, even in the fully solved $a_1=21$
   instance).
Also: the aimo-0680 "$k\mid a_{n+k}-a_n$" finishing move — refuted directly
(active-set-stabilization, round 3, $a_1=15$ counterexample $a_3-a_1=5$ not
divisible by $2$).
Also (this round, opening G's naive form): "prime factors of rejected
candidates form a bounded set" — refuted by direct computation below (grows
past 2000 distinct primes within 4000 terms for $a_1=99$); only the naive
version is dead, a refined witness-index version is untested.

### Small-case / intuition notes (conjectural / exploratory only)
- Recomputed (fresh, this round) that for $a_1=385=5\cdot7\cdot11$
  ($R=385$), prime factors as large as $3719$ still appear as divisors of
  *terms* within the first 6000 accepted values — but per the population's
  existing memory rule ("large prime factor of a large composite term is
  not necessarily a Q-member"), this is expected noise, not evidence that
  $Q$ itself is unbounded; it only confirms that testing "$R(a_n)\subseteq
  \{p\le R\}$" is not a viable route to bounding $Q$ (already implicitly
  known from `lambda-stabilization.md`'s scope, which only bounds
  *adjacent-link* primes, not all of $R(a_n)$).
- Ran a naive complement/exclusion-witness check (opening G) on $a_1=99$:
  the set of prime factors appearing among *rejected* candidates in the
  first ~4000 terms already exceeds 2000 distinct primes — no naive
  boundedness in this raw form. This is expected (any large prime can
  cause a coprimality mismatch once) and does not by itself kill a refined
  witness-index version of the framing, but rules out the crudest form.
- No new numeric evidence was gathered this round on Morse–Hedlund subword
  complexity (opening F) or on the "permanent lock" claim (opening E) — both
  are flagged above as cheap (<5 min) checks the next round should run
  before investing outline/build effort in either.
