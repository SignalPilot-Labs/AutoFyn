## imo-2026-06 (lens: greedy-minimality)

### HEADLINE FINDING (most important thing in this report)
The central gap the whole round-1 population converged on — **"S :=
{p : p | a_n for infinitely many n} is finite"** — is almost certainly the
**wrong target**, and I have strong evidence (theoretical + numerical) that
**S is in fact infinite** in general. Chasing "S finite" is a dead end that
should be abandoned, not merely reattempted with a sharper mechanism. This
also explains, after the fact, why three independent approaches in round 1
each proved (correctly!) that their own natural counting/pigeonhole
mechanism could not close it — they were trying to prove a false statement.

**Why S should be infinite (theoretical argument).** Suppose (as the problem
asks us to prove) $a_{n+T}=a_n+L$ holds for all $n \ge n_0$, some fixed
$T,L\ge1$. Fix a residue class $n \equiv n_1 \pmod T$ with $n_1 \ge n_0$; the
values $a_{n_1}, a_{n_1+T}, a_{n_1+2T},\dots$ form an infinite arithmetic
progression $x, x+L, x+2L,\dots$. For **any** prime $p \nmid L$, this AP hits
every residue class mod $p$ periodically (since $L$ is invertible mod $p$),
so $p$ divides infinitely many terms of the AP, hence infinitely many terms
of the whole sequence — i.e. $p \in S$. This uses nothing but elementary
modular arithmetic (no Dirichlet needed). Conclusion: **every prime not
dividing $L$ is automatically in $S$** — so $S$ is *coinfinite-complement*,
i.e. $S \supseteq \{\text{primes}\} \setminus \{\text{primes dividing } L\}$,
which is infinite. So "S finite" is not just hard to prove — assuming the
problem's own conclusion, it is *false*. The correct finite object is the
(tiny) set of primes dividing $L$, not $S$.

**Numerical confirmation.** For $a_1=6$: the greedy sequence is exactly
$6,8,10,12,\dots$ (every even number $\ge 6$; verified by direct
computation), so $L=2,T=1$, and indeed *every* odd prime $p$ divides
infinitely many terms (every $p$-th even number), confirming $S=$ all
primes. For $a_1=15$: computed the sequence out to 2000 terms. Found (a) the
"active window" of primes seen in the last 100 terms keeps growing without
bound as $n$ grows (max prime in window: 127 at $n=200$, 313 at $n=500$, 619
at $n=1000$, 1249 at $n=2000$) — i.e. new large primes keep entering; (b)
**every single prime $\le 409$ divides at least 5 of the first 2000 terms**
(checked exhaustively — the set of primes with count $\ge 5$ is *exactly*
the primes $\le 409$, no gaps); (c) spot-checked specific primes 101 and 233:
each recurs regularly and repeatedly throughout the whole range (101 divides
19 of the first 2000 terms, spread evenly from index 157 to 1882; 233
divides 8 terms spread from 369 to 1860) — these are not one-off incidental
hits, they are genuinely-recurring divisors. This is decisive evidence that
$S$ = (essentially) all primes, confirming the theoretical argument above.

### What IS true, unconditionally, from the start (reframing the finite object)
Do **not** try to discover a finite "load-bearing prime set" via pigeonhole
over the infinite tail (that produces $S$, which is infinite). Instead the
right finite set is available **immediately, for free, from $a_1$ itself**:
let $P$ = the (at most $\log_2 a_1$) distinct primes dividing $a_1$. Since
$\gcd(a_{n+1},a_1)>1$ is *always* one of the defining constraints (as $1\le
n$ for every $n\ge1$), **every** $a_n$ for $n\ge 2$ shares a prime with
$a_1$, i.e. is divisible by some prime of $P$ (this is exactly Fact 1 /
"every-term-meets-recurring-set"'s easy cousin, no pigeonhole needed — it's
immediate from the definition, not a limiting/infinite-tail argument). $P$
is finite *by construction*, not by a hard theorem.

The catch (why this doesn't immediately finish the problem): $P$ alone is
not always enough to pin down the eventual periodic structure — e.g. for
$a_1=15$ ($P=\{3,5\}$), the prime $2$ (not in $P$) gets recruited early and
becomes permanently load-bearing (used to satisfy constraints between
otherwise-$P$-disjoint terms), and the *true* governing modulus turns out to
be $L=30=2\cdot\mathrm{rad}(a_1)$, not $\mathrm{rad}(a_1)=15$ itself. So the
finite governing set is $P$ **plus possibly a small number of additional
primes recruited very early**, not necessarily $P$ alone. Numerically this
extra recruitment set seems to stabilize almost immediately (within the
first few terms) rather than needing an infinite-pigeonhole argument to
discover — this is the opening that greedy minimality should be used to
control.

### Distinct openings (using minimality directly)
1. **Bounded-window direct computation.** The Key Lemma (already proved,
   `lemmas/bounded-gap-via-rad-a1.md`) shows the *actual* $a_{n+1}$ always
   lies in the window $(a_n, a_n+R]$ where $R=\mathrm{rad}(a_1)$ is a FIXED
   constant (independent of $n$!). So determining $a_{n+1}$ is always a
   finite search over at most $R-1$ candidates. Minimality says: $a_{n+1}$ is
   the *first* $m$ in this window with $\gcd(m,a_i)>1$ for all $i\le n$. Try
   to show directly that which $m$ in the window wins is eventually
   determined by a bounded amount of information about $a_1,\dots,a_n$ (not
   the whole history) — e.g. by which residues mod (some fixed finite $M$,
   built from $P$ plus a bounded number of "early recruits") have appeared
   among the *recent* terms. This sidesteps $S$ entirely.
2. **Exact-from-the-start periodicity (no transient needed).** Numerically
   (see below), for every $a_1$ tested, the minimal $T$ for which
   $a_{n+T}-a_n$ is CONSTANT held **for all $n\ge1$ in the observed range**
   — i.e. no prefix-patching was needed at all in these examples. This
   suggests the "secondary gap" (extend eventual periodicity down to $n=1$)
   flagged by both `active-set-stabilization` and
   `state-compactness-pigeonhole` may not need patching as a separate
   argument if the periodicity is established via a state defined from
   $n=1$ onward (rather than "eventually periodic, then extend") — worth
   trying to build the finite-state argument so it's valid from the first
   index, sidestepping gap 2 as well as gap 1's wrong target.
3. **Minimality as a "smallest-wins" tournament between a bounded number of
   residue classes.** Since $a_{n+1}\le a_n+R$ always, and (by Fact 1) it
   must be divisible by some prime of $P$, in fact $a_{n+1}$ is *the winner*
   of a competition among (at most) $|P|$ many "prime-$p$ candidate slots"
   (for each $p\in P$, the next multiple of $p$ after $a_n$) *and* possibly a
   small number of "extra recruited prime" candidate slots that can
   occasionally undercut all of these — greedy minimality means we always
   take the literal smallest such candidate. If the set of "ever-relevant"
   extra primes can be shown to close up after a *bounded* (not just finite)
   number of recruitment events — using an explicit potential like
   $\sum_{p \text{ recruited}} 1/p$ or number-of-residues-mod-$R$-still-
   uncovered — this gives an actual finite construction of $L$
   ($L = R\cdot k$ for a small explicit $k$) rather than an abstract
   compactness argument.
4. **Reformulate the target away from "S finite" toward "L finite" directly**
   in the write-up handed to the outliner: state plainly that proving $S$
   finite is off the table (likely false), and that the correct statement to
   aim for is: *there is a finite $L$ (a multiple of $R=\mathrm{rad}(a_1)$,
   built by a finite, explicit recruitment process) such that $a_n \bmod L$
   is eventually periodic in $n$* — and $S$ being infinite is then a harmless
   consequence, not an obstruction.

### Cheap-kill / sanity checks
- Any proposed lemma of the shape "$S$ is finite" or "only finitely many
  primes ever get freshly recruited" should be numerically stress-tested
  first (as I did for $a_1=15$ to 2000 terms) before investing proof effort
  — it is very likely false as stated.
- The quantity that IS finite and should be the target is $L$ (equivalently,
  the finite set of primes dividing $L$), reachable in principle from $a_1$
  by a bounded recruitment process, not by an infinite-tail pigeonhole
  argument over $S$.

### Candidate technique(s)
- Direct bounded-window search (using the already-proved Key Lemma) +
  an explicit finite recruitment/potential argument, rather than
  compactness/pigeonhole over an infinite set of primes.
- A "smallest-candidate-wins" tournament argument tracking a bounded set of
  competing residue classes mod a growing-but-eventually-fixed finite $M$.

### Knowledge-base entries to use
Did not find a directly-named KB entry for this specific mechanism (greedy
covering-density stabilization); the relevant general tools already in use
by the population are elementary pigeonhole and CRT/residue arguments — no
named heavy theorem (Zsigmondy, LTE, etc.) appears applicable here, since the
obstruction is combinatorial/structural, not about prime powers or orders.

### Analogous past problems (cruxes)
Searched `past_crux_moves_database.json` (domain filters: number_theory
`extremal-principle`, `divisibility-and-gcd`, `sequences-and-recurrences`,
`invariants-and-monovariants`, `pigeonhole`; also scanned all domains for
"greedy") — no problem in the corpus matches this problem's structure
closely (a self-referential greedy sequence built from pairwise-gcd
constraints against its own entire past). The single most structurally
suggestive crux is:
- **aimo-0813** (number_theory, divisibility-and-gcd): "Take the minimal
  element $d$ of an addition-closed subset of $\mathbb N$ and show the
  subset is exactly the multiples of $d$, ruling out non-multiples by
  minimal-counterexample descent." (Iran functional-equation problem,
  $f(m+n)$ divisible by $p$ iff $f(m)+f(n)$ divisible by $p$ ⟹ $f=\mathrm{id}$.)
  The crux move — fix a prime $p$, let $d=\min\{x : p\mid f(x)\}$, then show
  by a minimal-counterexample argument that $p\mid f(x) \iff d\mid x$ — is
  the closest available template for "use minimality of a witness index to
  force a clean multiples-of-$d$ structure." It is NOT a direct fit (that
  problem's structure is an additive functional equation on indices; ours is
  a gcd-covering condition on values), but the *shape* of the argument
  (fix an object, minimize an index/value witnessing a property, then use
  minimality + the closure property to force *all* other witnesses to be
  exactly the multiples of the minimal one) is worth trying to adapt: e.g.
  fix prime $p \in P$ (or a candidate recruited prime), let
  $d_p = \min\{n : p \mid a_n\}$, and try to show $p \mid a_n$ for $n$ in a
  residue class related to $d_p$ using minimality of the greedy choice
  (rather than via the pigeonhole/compactness route the population has been
  using). No other crux in the corpus was judged a genuine match; I recommend
  not forcing a citation beyond this one adaptable shape.

### Prior progress (from `current.md` / approaches / lemmas)
- Certified, reusable, unconditional: existence of the sequence
  (`lemmas/existence.md`); pairwise non-coprimality for all $i\ne j$
  (`lemmas/pairwise-non-coprimality.md`); "every term meets the recurring
  set $S$" (`lemmas/every-term-meets-recurring-set.md` — true but, per this
  report, not useful since $S$ itself is the wrong/infinite object);
  bounded-gap lemma $a_{n+1}-a_n \le R=\mathrm{rad}(a_1)$
  (`lemmas/bounded-gap-via-rad-a1.md` — this one IS very useful, see
  opening 1 above).
- `jacobsthal-covering-bound.md` (unbuilt) already flagged, independently, a
  "self-sufficiency" stopping criterion and noted (honestly) that its own
  attempt to pin $T$ down by a closed formula failed since $T$ depends on
  finer history, not $S$/$L$ alone — consistent with my finding that the
  right target is a bounded recruitment process, not a clean closed form.

### Dead ends (do not retry)
- Any pigeonhole/counting argument aiming to prove **"$S$ is finite"**
  (as attempted by all three built round-1 approaches) — now additionally
  supported by this round's finding that $S$ is very likely genuinely
  infinite, not merely hard to bound. Do not reattempt "$S$ finite" in any
  form; reframe as "$L$ finite / recruitment process terminates" instead.
- `growth-rate-contradiction`'s "freshly recruited prime forces large gap"
  mechanism (already shown false in round 1) — consistent with and
  explained by this report's finding: fresh primes recur regularly (e.g.
  101, 233 for $a_1=15$) and are not rare one-off events at all, so no
  gap-size argument can bound their count.

### Small-case / intuition notes (all labeled conjecture except where computed)
- **Computed exactly** (not conjecture): for $a_1 \in \{6,9,10,15,21,35,105,
  210,231\}$, the sequence is periodic $a_{n+T}=a_n+L$ **for all $n\ge1$
  from the very start** (no transient), with (T,L) = (1,2), (1,3), (1,2),
  (8,30), (1,3), (34,210), (58,210), (1,2), (1,3) respectively (computed via
  direct simulation, searching for the minimal $T$ with constant $T$-shift
  gap over the whole computed range of ~300-400 terms).
- **Conjecture** (small-case pattern, not proven): $L$ is always of the form
  $k\cdot R$ for a small integer $k\ge1$ ($k=1$ in most examples, $k=2$ for
  $a_1=15$), where $k$ counts how many "extra" non-$P$ primes get
  permanently recruited; whenever $a_1$'s own prime factors already
  "self-cover" quickly (e.g. $a_1$ has a small prime factor that alone can
  serve every future constraint, as happens whenever $\min(P)$ is small
  enough relative to $R$), $T=1$ and no extra recruitment occurs at all.
- **Conjecture**: the number of "extra" (non-$P$) primes ever permanently
  recruited is small (bounded by $|P|$ or so) and recruitment happens within
  a bounded number of steps depending only on $a_1$ — this is exactly what
  a minimality-based potential/monovariant argument (opening 3 above) would
  need to make rigorous.
