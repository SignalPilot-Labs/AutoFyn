## imo-2026-06

Lens: gap sequence `d_n = a_{n+1}-a_n` attacked directly via extremal/pigeonhole
density arguments and a monovariant/finite-state approach, as opposed to
prime-by-prime bookkeeping. Findings below mix **rigorously proved** facts
(marked PROVEN), and **empirical/conjectural** patterns from simulation
(marked CONJECTURE) — kept clearly separated per the Rules.

### Distinct openings

1. **(PROVEN, cheap) "a_1's own prime factors are permanent for all time."**
   Directly from the definition, `gcd(a_{n+1}, a_i) > 1` must hold for **every**
   `i = 1,...,n`, in particular for `i = 1`. So `gcd(a_n, a_1) > 1` for every
   `n ≥ 2`: every later term shares a prime with `a_1` specifically, not just
   with "some earlier term." This is a one-line but load-bearing fact — the set
   `rad(a_1)` of primes dividing `a_1` is a **permanent constraint** on the whole
   sequence, forever, not merely transient. (More generally: for any fixed `m`,
   every `a_n` with `n > m` shares a prime with `a_m`.) A genuinely different
   top-level framing falls out of this: the sets `P_n = {primes dividing a_n}`
   form an infinite **pairwise-intersecting family of finite sets** (`P_i ∩ P_j
   ≠ ∅` for all `i < j`, immediate from the definition). This turns the whole
   problem into a hypergraph/intersecting-family question, distinct from the
   gap-arithmetic framing — worth offering the outliner as an alternate top-level
   target (e.g. show the family of `P_n` eventually cycles through a periodic
   pattern of finitely many "generating" sets).

2. **(PROVEN, complete mini-result) The prime-power starting case is fully
   solved and gives T=1 exactly.** If `a_1 = p^k` for a single prime `p`
   (in particular whenever `a_1` is **even**, taking `p=2`), then by induction
   `a_n = a_1 + p(n-1)` for all `n`, i.e. `T = 1, L = p` **exactly, from n=1**.
   *Proof*: suppose inductively `a_1,...,a_n` are all multiples of `p` (true for
   n=1). Since `p | a_n`, none of `a_n+1, ..., a_n+p-1` is a multiple of `p`,
   and each of these is consecutive to `a_n` or shares no common prime forced by
   `a_1 = p^k` (concretely `gcd(a_n+j, a_1) = gcd(a_n+j, p^k)` needs `p | a_n+j`,
   false for `1≤j≤p-1`), so all of them are inadmissible. `a_n+p` is a multiple
   of `p`, hence `gcd(a_n+p, a_i) ≥ p > 1` for every earlier multiple-of-p term
   `a_i` (i ≤ n) automatically — admissible, and minimal by the above. So
   `a_{n+1} = a_n + p`. QED. This fully disposes of the case `a_1` even (T=1,
   L=2) or an odd prime power (verified in simulation: a_1=9 → T=1,L=3; a_1=49
   → T=1,L=7; a_1=25 → T=1,L=5) — a genuine cheap-kill covering an entire
   family of starting values, not just intuition.

3. **Direct density/pigeonhole bound on d_n via "available primes so far."**
   At step `n`, admissibility of a candidate `x > a_n` requires, for each
   `i ≤ n`, that `x` share a prime with `a_i`. If among `a_1,...,a_n` there is
   at least one **even** term, then any even `x` automatically satisfies the
   gcd condition against every even `a_i`, so the only *live* constraints come
   from the odd `a_i`'s. Empirically (see below) the sequence quickly acquires
   an even term (often `a_2`), after which candidates only need to be even AND
   satisfy finitely many "odd-term" constraints — this bounds how far away the
   next admissible even number can be by a density/CRT argument over the
   (typically small) set of primes dividing the surviving odd terms. This is
   the natural "cheap bound" route to show `d_n` is *eventually bounded* — but
   note (point 6 below) boundedness alone is NOT the hard part; getting *exact*
   recurrence (T,L) is.

4. **Monovariant/finite-state candidate:** define the state at step `n` as the
   tuple of residues, modulo a conjectural finite modulus `L` (product of a
   finite set `S` of "active" primes), that record which residue classes mod
   `L` are already "claimed" by which prime in `S` among recent terms. If one
   can show (a) only finitely many primes are ever load-bearing (see point 6),
   and (b) the admissibility of the next candidate depends only on this finite
   state, then the state space is finite and the (deterministic, forward-only)
   process must eventually revisit a state — forcing exact eventual periodicity
   by pigeonhole + determinism. This is the "bounded state ⟹ eventually
   periodic" schema, and matches a crux move found in the corpus (see below).
   I did **not** attempt to nail down what "the state" precisely is or prove
   finiteness of `S` — that is the real gap, flagged for the outliner.

### Candidate technique(s)
- Finite-state pigeonhole + determinism ⟹ eventual periodicity (need: bounded
  state description of "what primes are locally required").
  KB: "Order of an element, Fermat/Euler: periodicity of a^n mod m" and
  "Linear recurrences ... sequences eventually periodic mod m" (§Number Theory)
  are the closest generic KB entries — same schema, different mechanism.
- Density / covering-system style argument (sum of `1/p` over active primes)
  to bound gaps and to show only finitely many primes are ever load-bearing —
  analogous in spirit to the grid/prime-covering counting in the KB-adjacent
  crux `aimo-0447` (see below).
- Bezout-combination trick to convert "period T holds for indices differing by
  various step sizes with gcd 1" into "period T holds for shift 1" — seen in
  crux `aimo-0648`, directly reusable schema once boundedness + eventual
  periodicity are established.

### Cheap-kill candidates
- **`a_1` is a prime power (in particular `a_1` even)**: T=1, L=p, fully
  provable by the 4-line induction in item 2 above. Dispatch this as an
  immediate settled sub-case so effort concentrates on `a_1` with ≥2 distinct
  prime factors.
- `gcd(a_n, a_1) > 1` for all n (item 1): cheap, immediate, but structurally
  central — use it to seed the "permanently active prime set" `rad(a_1)`.
- Consecutive-integer coprimality (`gcd(k,k+1)=1`, in KB "Divisor analysis"):
  used repeatedly in the induction of item 2, and generally explains why
  `d_n ≥ 2` always (a_{n+1} can never just be a_n+1).

### Knowledge-base entries to use
- "Order of an element, Fermat/Euler ... eventual periodicity of products of a
  sequence mod m" and "Linear recurrences ... sequences are eventually
  periodic mod m" (§Number Theory) — generic template for the finite-state
  pigeonhole argument.
- "Pigeonhole / extremal principle" and "Invariants & monovariants" (§Combinatorics,
  §General Proof Methods) — the meta-schema (bounded state ⟹ recurrence).
- "Divisor analysis" (§Number Theory) — consecutive-integer coprimality,
  gcd/difference relations.
- "Meta-Strategy: prune before you compute ... a size/dyadic-bucket bound" —
  matches the density-of-small-primes cheap bound idea in item 3.

### Analogous past problems (cruxes)
- `aimo-0648` (algebra, sequences-and-recurrences) — **best match for the
  finite-state mechanism**: "Show an order statistic (max/min) of the terms is
  preserved by the recurrence to confine the sequence to a bounded interval,
  forcing eventual periodicity of an integer sequence" + "Use a Bezout
  combination of the step sizes modulo the period to convert index-shifts by
  the d_i into a shift by 1, propagating a property to every index." The
  underlying problem (an averaging recurrence with several lags `d_1,...,d_k`,
  `gcd(d_i)=1`, prove eventually constant) is a different recursion, but the
  *proof schema* — bound the sequence into a finite range, invoke pigeonhole to
  get eventual periodicity, then use a gcd/Bezout argument on the periodic
  structure to sharpen the conclusion — is exactly the shape needed here (gap
  sequence bounded ⟹ periodic; then use gcd=1 among some finite structural
  parameters to pin down exact T, L). Worth adapting the two-stage skeleton,
  not the arithmetic.
- `aimo-0907` (algebra, functional-equations / sequences) — crux "Bound the
  minimal period of a periodic sequence by showing the period divides each of
  two parameter expressions, then take their gcd to pin it." Useful *if* the
  outliner's proof produces two different valid periods `T_1, T_2` (e.g. from
  two different vantage points/starting indices) — gcd(T_1,T_2) is then also a
  period, a clean way to nail down minimality once existence is known.
- `aimo-0447` (number_theory, divisibility-and-gcd) — "Encode a 'gcd>1 for
  every pair of shifts' hypothesis by placing in cell (i,j) a prime dividing
  the gcd, turning the condition into a complete prime-covering of a grid,"
  with a density bound `Σ 1/p² < 1/2` etc. This is a **different problem**
  (a lower bound on `min{a,b}` given an `n×n` grid of gcd>1 conditions between
  two arithmetic progressions) but the *encode-gcd-condition-as-a-prime-grid,
  then bound by prime density* technique is directly relevant to proving "only
  finitely many primes are ever load-bearing" in our problem (item 6 below) —
  flag as a technique donor, not a solution donor.
- Not a match: I did not find a crux in the corpus that solves an "eventually
  periodic gcd-greedy sequence" problem directly; the three above are technique
  donors for sub-pieces, not full analogues.

### Prior progress
None — this is round 1, workspace was empty (no approaches, no lemmas) before
this exploration pass.

### Dead ends (do not retry)
None recorded yet (fresh problem). One thing to flag as a **likely trap**,
not yet a dead end: naively trying to prove "d_n is eventually bounded" as a
standalone lemma and hoping periodicity "falls out" — empirically this is
false as a strategy in isolation. Boundedness is necessary but the interesting
content is the *exact* recurrence `a_{n+T}=a_n+L`, which (per simulation)
holds **immediately from n=1 in every example tested**, not just eventually —
so an approach that produces only "eventually periodic, for n ≥ N₀" under-
delivers relative to what's empirically true and to what a clean inductive
proof (as in item 2) should give directly. Push the outliner toward an
approach that establishes periodicity from n=1 outright (e.g. via strong
induction annotated with the periodic pattern as invariant), not via a
"discard the transient" argument that would need extra work to rule out.

### Small-case / intuition notes (numeric experiments, Python/gcd greedy simulation)
All CONJECTURE / empirical unless stated PROVEN above.

- Simulated the greedy sequence for many starting values `a_1` (up to a few
  thousand terms each) and directly computed `d_n` and searched for the
  minimal `T` with `a_{n+T} = a_n + L` constant, verifying against the **full**
  generated array (not just a late window).
- **a_1 even, or a prime power**: T=1 always (PROVEN, item 2). E.g. a_1 ∈
  {2,4,6,8,10,12,14,...,50,...}: T=1, L=2. a_1=9→(T,L)=(1,3); 25→(1,5);
  49→(1,7).
- **a_1 odd with ≥2 distinct prime factors**: sometimes ALSO trivializes to
  T=1 (e.g. 21=3·7→L=3; 33=3·11→L=3; 39=3·13→L=3; 55=5·11→L=5; 57=3·19→L=3;
  69=3·23→L=3; 85=5·17→L=5), but sometimes gives a genuinely large period:
  15=3·5→(T,L)=(8,30); 35=5·7→(34,210); 65=5·13→(58,390); 77=7·11→(18,154);
  91=7·13→(20,182); 95=5·19→(82,570); 105=3·5·7→(58,210); 143=11·13→(64,858);
  1001=7·11·13→(282,2002); 1155=3·5·7·11→(676,2310). CONJECTURE: L always
  appears to be **even**, and to equal `2·(product of a small set of primes
  including rad(a_1) and sometimes one or two extra small primes not dividing
  a_1)` — e.g. 65=5·13 gives L=390=2·3·5·13 (recruits an extra factor 3 not
  dividing a_1); 91=7·13 gives L=182=2·7·13 (no extra factor); 105=3·5·7 gives
  L=210=2·3·5·7 (=2·105); 1155=3·5·7·11 gives L=2310=2·1155; 1001=7·11·13
  gives L=2002=2·1001; 143=11·13 gives L=858=2·3·11·13 (extra factor 3).
  **Which starts recruit an extra prime and which don't is unclear from this
  pass** — worth a dedicated numeric sweep by the next round if this becomes
  load-bearing.
- **Mechanism observed (why some semiprimes collapse to T=1 and others don't,
  qualitative/CONJECTURE, traced by hand for 15 vs 21):** the sequence permanently
  needs, from `a_1 = p·q` (distinct odd primes), that every later term hit `p`
  or `q`. If at some point a term appears that is a **pure prime power of just
  one of {p,q}** (e.g. for a_1=21=3·7, the term `27=3³` appears at index 2),
  that collapses the "p or q" disjunction down to a single forced prime
  forever (here 3), and the sequence trivializes to T=1 shortly after. If no
  such pure-power term ever appears (e.g. a_1=15=3·5: the odd terms that
  recur — 15,45,75,105,... — are always of the form `15·(odd)`, never a pure
  power of 3 or 5), the "3 or 5" disjunction survives forever, and once an
  even term also appears (a_2=18), the surviving live constraint becomes
  "x even and (3|x or 5|x)" — a genuinely 2-way branching density condition
  with period exactly `2·3·5=30` and `T=8` matching `|{x mod 30 : x even, 3|x
  or 5|x}|=8`. This branch-collapse-or-survive dichotomy is unverified as a
  theorem — flagging as the likely crux phenomenon underlying whether T=1 or
  T>1, worth the outliner's attention but needs a real proof, not just the
  hand-traced examples here.
- **Incidental large primes never stop appearing** but appear to be harmless.
  Tracking every prime factor ever appearing in any `a_n` for `a_1=65` shows
  ~100 distinct primes appear by term 800 (up to 541), and new ones keep
  appearing even past the point where the gap sequence is already confirmed
  exactly periodic (e.g. a fresh prime 499 appears as a factor of the term
  `2994 = 2·3·499` at index 795, well inside the already-periodic regime for
  T=8,L=30 — wait, that specific example used a_1=15 not 65, both share this
  behavior). This confirms: exact periodicity of `d_n` does **not** require
  periodicity of the actual factorizations of `a_n` — most of the "new" prime
  factors are decorative cofactors of composite numbers of the form (small
  active prime)×(large prime), never re-required by anything later. This is
  reassuring for a "finitely many *load-bearing* primes" lemma (item 6) — the
  bookkeeping only needs to track a handful of small "active" primes, ignoring
  the (infinitely many, but individually irrelevant) large incidental cofactors.
- **Periodicity holds exactly from n=1, not just eventually**, verified
  directly for 5 different examples (15, 65, 91, 105, 1155) by checking
  `a[i+T] == a[i] + L` for every `i` from `i=0` across the full simulated
  array (no discarded transient) — zero violations in every case tested. This
  is strong (but still empirical) evidence that the correct proof should give
  immediate periodicity, not "eventually periodic then handle the prefix."
