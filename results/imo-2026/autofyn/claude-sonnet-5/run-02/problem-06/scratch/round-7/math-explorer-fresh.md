## imo-2026-06 (fresh-framing lens, deliberately far from recruitment/FAH field)

### Distinct openings

**Opening 1 (the strongest new lead): a *scalar* well-ordering + algebraic
lock-in, à la ISL/IMO 2017-style "gcd/lcm eventual-periodicity" proofs —
genuinely different in kind from the two well-ordering attempts already tried
and killed (round 3's |A'|+|B'| size measure, round 5's witness-index
descent).**

Both prior well-ordering attempts failed for the *same* structural reason: they
minimized a quantity defined over an *ever-refining partition* (extended
types), and refining the partition (S₀ → S₁) can *manufacture new, smaller*
elements out of nowhere — so the "minimal counterexample" is not stable under
the very operation the proof needs to perform. This is flagged in
`current.md` round 5 as "the obstruction is intrinsic to the recruitment
operation, not an artifact of the chosen measure" — but that diagnosis is only
about *set/type-valued* monovariants. A genuinely different kind of
monovariant — a single *integer*, not a set or a partition-indexed quantity —
sidesteps the refinement problem entirely, because `min` of a set of positive
integers exists by pure well-ordering with no partition to refine.

Concrete template, adapted from the crux move in `aimo-0678` (ISL/IMO 2017 N-type
problem, ALSO an "eventually periodic gcd/lcm-driven sequence" claim, ALSO
proved by (a) a non-increasing scalar witness `w_n = min{m ≥ a_n : m ∤ s_n}`
that is shown non-increasing by direct case computation (not pigeonhole), so it
hits its floor `w` at some finite `N` by well-ordering; then (b) a *second*
scalar `g_n = gcd(w, s_n)` is shown, by an exact algebraic identity (not an
existence/pigeonhole argument), to be *constant* for `n ≥ N`; (c) constancy of
both `w` and `g` immediately gives an explicit period `w − g` and step, with the
period *read off directly* from the two frozen scalars — no CRT-on-a-finite-core
step is even needed separately, it falls out of the algebra):

- Define an analogous scalar for THIS problem, e.g. `w_n := min{p prime :
  p does not divide a_i for any i ≤ n}` (the least prime not yet "recruited"
  at all) — trivially non-increasing is false here (it's non-decreasing, primes
  get used up), so the naive transplant needs inversion: try instead
  `w_n := min{q prime : q ∤ a_i for all i ≤ n with a certain type}` or, more
  promisingly, a magnitude-based scalar tied to the SAME object the existing
  work already isolates — e.g. `w_n := min` over currently-open (in the
  Collateral-Safety sense) base-type pairs `(A,B)` of `(the value of the
  earliest still-unresolved witness pair)`. The point is NOT that this exact
  quantity works (untested, likely needs iteration) — it is that the *proof
  technique* should be "exhibit one scalar invariant that is monotone by a
  short *direct case computation on the recurrence itself* (not by
  set-refinement pigeonhole), let well-ordering give a floor, then prove a
  *second, coupled* scalar locks in via an *algebraic identity* (gcd/lcm
  manipulation) rather than another combinatorial pigeonhole." This is
  structurally the missing ingredient current approaches never tried: all six
  rounds' machinery (Lemma G, Critical Prime Dichotomy, FAH, Symmetric FAH) are
  *existential* ("some prime works," "infinitely many terms are divisible")
  — never an *algebraic identity* pinning one specific value exactly, which is
  exactly the gap Lemma I (round 6) diagnoses as missing ("no composition of
  the current tools can promote an existential fact to a uniform identity").
  `aimo-0678`'s Claim 2 is a textbook example of exactly that missing move
  (turning `gcd(a_n,b_n)=gcd(a_n,s_n)` into an exact recursion for `g_{n+1}`
  in terms of `g_n` alone, with no residual existential quantifier).
- Why this might escape the wall: FAH/Symmetric FAH ask "does the SAME prime
  divide EVERY later occurrence of a type" — an infinite conjunction, hard to
  pin from existential lemmas. An algebraic-identity approach instead tries to
  derive the *recurrence for what the next term must be*, in closed form, once
  the process reaches a frozen scalar state — turning "prove universal
  divisibility" into "compute a fixed-point of an explicit recursion," which
  is a different kind of argument entirely (no universal quantifier to
  establish termwise).
- Caveat, honestly stated: no specific scalar has been found or verified to be
  monotone for this problem; this is a *technique* transplant, not a worked
  lemma. The multi-prior-term structure (gcd against ALL i ≤ n, not just the
  immediate predecessor as in `aimo-0678`) makes the direct transplant
  nontrivial — the outliner/builder would need to find the right invariant,
  most plausibly built on top of the *already-certified* extended-type
  machinery (e.g., scalar = the earliest-witness VALUE of the lexicographically
  first currently-open base-type pair under some fixed global ordering of
  pairs, not of extended types) so it inherits Collateral-Safety's monotone
  `open(k) ⊇ open(k+1)` for free while adding a genuinely new algebraic
  finishing move instead of FAH.

**Opening 2 (a correction/redirection, not a full new framework, but changes
what's provable "for free"): the "gap-boundedness" crux in
`density-sieve-contradiction` is ALREADY closed unconditionally and this
approach's own stated crux is therefore moot as scoped.**

`current.md`'s certified item #2/#3 (Bounded Gap Lemma, Generalized Bounded Gap
Lemma) already gives `a_{n+1} ≤ a_n + a_1` unconditionally — this is EXACTLY
`density-sieve-contradiction`'s Step 3/4 target ("gap-boundedness by
contradiction," flagged in that file as "THE GAP"). That file (written round 1,
never rebuilt) does not seem to have been told this is already free; it treats
gap-boundedness as its central unresolved crux and proposes a sieve/Mertens
argument or a "blocking-types capped by |Q|" argument to prove it. Both are
unnecessary — the real content of that approach, if revived, should be
re-aimed *entirely* at its Step 5/6 "confinement of relevant primes to a fixed
finite S" using an ANALYTIC (density/counting) argument instead of the
recruitment-process combinatorics — i.e., try to bound the total number of
distinct primes that can EVER matter to legality (not divide some a_n
incidentally — most large primes dividing a_n are irrelevant "junk" factors,
confirmed numerically below) via a counting argument on how many "independent
blocking reasons" can coexist, using the already-certified Persistent-Type
Pigeonhole (finite 𝒫) as the count, not a fresh sieve. This reduces to the same
crux as the main field (finiteness/absorption), so it is a *redirection*, not
an escape — flagged honestly as such, but worth NOT re-deriving gap-boundedness
from scratch if this approach is revived; it's free.

### Candidate technique(s)
- Opening 1: scalar monovariant (well-ordering on a single integer, not a
  set/partition) + algebraic lock-in of a second coupled scalar via an exact
  gcd/lcm-style identity — modeled on `aimo-0678`'s two-claim structure.
- Opening 2: redirect `density-sieve-contradiction` (drop its now-redundant
  gap-boundedness crux; it's a free corollary of the certified Bounded Gap
  Lemma) toward a density/counting argument for prime-support finiteness,
  built ON TOP of the certified Persistent-Type Pigeonhole rather than a raw
  sieve.

### Cheap-kill candidates
- None obvious for Opening 1 as a "quick kill" — it's a search for the right
  invariant, not a size/parity/injection check.
- For Opening 2: none beyond what's already established (Bounded Gap Lemma
  already subsumes the naive "just bound gaps" target — this itself functions
  as a cheap kill on any future re-derivation of gap-boundedness by sieve,
  which should be skipped as wasted effort).

### Knowledge-base entries to use
- `knowledge_base.md` "Linear recurrences: sequences are eventually periodic
  mod m" and "Order of an element, Fermat/Euler: periodicity of aⁿ mod m" —
  cited already by the population for the CRT+cyclic-pigeonhole finish; Opening
  1 would use these differently (as the shape of the *target* conclusion, not
  the mechanism to reach it).
- No `knowledge_base.md` entry names "covering systems" or "monovariant +
  algebraic lock-in" explicitly; this is a technique import from the crux
  corpus, not the KB.

### Analogous past problems (cruxes)
- **`aimo-0678`** (ISL/IMO-2017-flavor: `a_{n+1}=gcd(a_n,b_n)+1,
  b_{n+1}=lcm(a_n,b_n)-1`, prove `(a_n)` eventually periodic) — genuinely the
  closest structural analog in the whole corpus: same *shape* of conclusion
  (eventual periodicity of an integer sequence built from a gcd-flavored local
  rule), proved via exactly the "scalar well-ordering, then algebraic lock-in
  of a second scalar" mechanism described in Opening 1. Crux move:
  `sequences-and-recurrences` (number_theory), "non-increasing witness
  `w_n=min{m≥a_n : m∤s_n}` hits a floor by well-ordering, then `g_n=gcd(w,s_n)`
  is shown constant by an exact algebraic identity, giving the period
  directly." Disanalogy to flag honestly: `aimo-0678`'s rule only looks at the
  *immediately preceding* pair `(a_n,b_n)`, a one-step Markov recursion; our
  problem's legality condition depends on gcd against *every* prior term
  simultaneously, so the direct transplant of `w_n`/`g_n` does not obviously
  exist — the analogy is at the level of *proof technique*, not a literal
  formula reuse.
- **`aimo-0514`** (3-regular planar graph turning-walk, prove periodicity via
  reversibility ⟹ union of cycles) — already explored in this workspace under
  `reversible-transition-map` and shown (round 5, certified negative result)
  to be logically EQUIVALENT to gap (†) at any fixed core level, not a bypass.
  Do not re-propose this framing; it is a documented dead end for the *primary*
  gap, though the same file's untouched secondary finding (early terms need
  not lie on the eventual cycle) remains a legitimate target for the
  "periodicity from n=1" secondary gap only.
- **`aimo-1025`** (Mathbook friendship-closure problem, "run a canonical greedy
  version of the process until stuck, then induct over a merge sequence") —
  a looser analogy (greedy-process-canonicalization flavor matches the
  problem's greedy-smallest-successor rule), but its actual crux move
  (bounding an INITIAL edge count via a merge-sequence lower bound) doesn't
  transplant cleanly to an eventual-periodicity claim; flagged as a weak
  analogy, not a strong lead — mentioned only because it's the closest
  "canonicalize the greedy run" match in `processes-and-algorithms`.

### Prior progress
See `current.md` for the full, extensively-developed state (6 rounds). In
brief, unconditionally proved: Free Facts, Bounded/Generalized Bounded Gap
Lemma, Persistent-Type Pigeonhole, Bounded/Generalized Bounded Witness Lemma,
Finite Core Theorem, Extended Persistent-Type Pigeonhole, Canonical-Refinement
Lemma, F_A∩F_B≠∅, Projection Lemma, Collateral-Safety Theorem. These reduce
gap (†) exactly to: does one round of prime-recruitment achieve "Symmetric Full
Absorption" (a specific prime divides literally EVERY later occurrence of a
type, not just infinitely many) for every currently-open base-type pair — open,
well-supported empirically (0 counterexamples across ~10 seeds, 4 independent
implementations), not proved.

### Dead ends (do not retry)
- `hypergraph-transversal` (round 1): re-read in full this round. Its Step 3
  ("Key Lemma: finiteness of the eventual prime support S") is, on inspection,
  literally the same open question as gap (†)/FAH dressed in antichain
  language — its own file admits the "density argument... is unavoidable here;
  flag as the true crux" and never resolves it. Confirms the orchestrator's
  round-1 assessment; not a fresh escape, just a relabeling of the same wall.
  Its Step 6 (periodicity from n=1) restates the population's known secondary
  gap.
- `density-sieve-contradiction` (round 1): its stated primary crux
  (gap-boundedness) is now a FREE corollary of the certified Bounded Gap
  Lemma (see Opening 2) — do not re-derive it via sieve/Mertens. If revived,
  must be re-aimed at prime-support finiteness directly, where it reduces to
  the same wall as the rest of the field (not an escape).
- `reversible-transition-map`'s primary framing (round 5, RETHINK'd, confirmed
  above): equivalent to (†) at any fixed core, not a bypass.
- Round-3/5 well-ordering descents (|A'|+|B'| size measure; witness-index
  descent): both die to "partition refinement manufactures new smaller
  elements" — Opening 1 is explicitly designed to avoid this failure mode by
  using a scalar (not partition-indexed) invariant; still unverified.

### Small-case / intuition notes (labeled conjecture / numerical evidence only)
- Numerically confirmed (python, `gcd`-based greedy simulation, seeds
  a_1 ∈ {15,35,175,187,209,385}, first 400 terms): the TOTAL number of distinct
  primes dividing *any* term a_1..a_N grows without bound (roughly matching the
  count of primes up to a_N) — e.g. a_1=187 has 62 distinct primes among its
  first 400 terms. This confirms (conjecturally, but strongly) that the
  relevant finite core S is a small, special subset of "legality-relevant"
  primes, NOT "all primes that ever divide some term" — most large prime
  factors of individual terms are numerically incidental "junk," irrelevant to
  the coprimality condition. This is consistent with, and does not contradict,
  the existing Finite Core Theorem framing; it is offered as explicit
  confirmation for whichever approach (Opening 1 or a revived Opening 2) needs
  to argue "most prime factors don't matter, only a bounded legality-relevant
  subset does."
- No new falsifying seed was found for FAH/Symmetric FAH in the limited time
  available (not a focus of this lens); this report defers to the main field's
  extensive empirical support (0 counterexamples, 4 independent
  implementations, per `current.md` round 6).
