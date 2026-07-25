## imo-2026-06

- Distinct openings (all genuinely different from the order-theoretic antichain/⊆-minimal-support
  framing that both live approaches share and both bottom out on):

  **(A) Monovariant / extremal-invariant framing (most promising — recommend this one).**
  Instead of proving Π finite as a *set-of-primes* statement, mimic IMO 2015 SL N4 (crux corpus
  `aimo-0678`, essentially the same problem *shape*: a greedy/recursive integer sequence, prove
  eventual periodicity). Its solution does NOT touch prime-supports at all; it constructs an
  auxiliary integer quantity `w_n = min{m ≥ a_n : m ∤ s_n}` (an extremal "first failure" witness)
  built from a secondary invariant `s_n` that freezes during one type of step, shows `w_n` is
  **non-increasing**, hence — bounded below by 1 — eventually **constant** `= w`, and that
  constancy is exactly what pins down a finite modulus and forces the cyclic repeat. The
  transplantable move is: *find some integer-valued statistic of the state that (i) is
  non-increasing along the recursion, (ii) is bounded below, hence stabilizes by well-ordering,
  and (iii) its stabilized value directly yields the finite structure needed* (there, the
  eventual period; here, plausibly a bound on which primes can still enter a new ⊆-minimal
  support). Concretely for our problem: consider, for each `n`, the quantity
  `m(a_n) := least multiple of M exceeding a_n` (already used in Lemma 2) and the "savings"
  `d_n := m(a_n) − a_{n+1} ≥ 0`. Candidate monovariant to search for: something like
  `w_n := min{ q prime : q ∉ (primes used as sole witnesses among a_1,…,a_n) and q could still
  be forced by a future minimal support}` — i.e. try to build an explicit extremal quantity
  whose stabilization directly caps the primes that can ever appear in a *new* ⊆-minimal support
  after some point. **This is not yet constructed** — it is the concrete first step to attempt,
  not a finished lemma. Honest failure mode: `aimo-0678`'s invariant `s_n = a_n+b_n` has an exact
  algebraic reason to freeze (gcd+lcm identity); our problem has no visible two-coordinate
  algebraic partner to play `b_n`'s role, so the analogous freezing identity must be hunted for
  (candidate: pair `a_n` with `M`, or with the "running admissible-set trace" `a_n mod (current
  known primes)`) — this hunt is real work, not guaranteed to succeed.

  **(B) Self-referential bootstrapping via Distance–prime + growth rate (partially explored,
  worth pushing further).** Lemma 3 (Distance–prime, certified) says a shared prime `q | a_i,a_j`
  forces `q ≤ |a_i − a_j|`, and Lemma 2 gives `a_n = Θ(n)` (`a_1+(n−1) ≤ a_n ≤ a_1+(n−1)M`). So if
  a prime `q` is to recur as a witness across many terms (needed for it to anchor a *persistent*
  ⊆-minimal support), its recurrences among the `a_n` are spaced at least `~q/M` indices apart
  (from Lemma 3 read the other way: two terms both divisible by `q` are `≥ q` apart in value,
  hence `≥ q/M` apart in index by the growth bound). This gives a density bound: `q` can divide at
  most `O(N/q)` of the first `N` terms, i.e. large primes are asymptotically rare *among all
  terms*. The gap in turning this into finiteness of `𝓐_∞` (flagged already in
  `redundant-constraint-antichain` §7c) is that "rare" is not "eventually absent" — a prime with
  density `1/q → 0` can still recur infinitely often and be load-bearing (exactly what happens
  with `q=19` in the `a_1=375` example, refuting any naive "rare ⇒ finite" jump). The genuinely
  new angle to try under this lens: instead of counting *occurrences* of a single prime, count
  **how many distinct large primes can be simultaneously "active" as sole witnesses in a single
  window of length `M`** (only `O(1)` slots per window since a term has boundedly many prime
  factors — bounded by `log_2(a_n)` — but that bound grows with `n`, so this alone does not close
  the gap either; flag as a genuine dead end unless a sharper per-window count is found).

  **(C) CRT / covering-system obstruction — checked and it does NOT work as an obstruction to
  infinite Π (report so the outliner does not waste a round on it).** The natural idea is: "if
  infinitely many primes were structurally required, use CRT to build an arbitrarily long stretch
  of integers avoiding all currently-known constraints, contradicting the bounded-gap property of
  `A`." This fails for a clean reason found by working it out: **`A` (the admissible set) already
  contains every multiple of `M = rad(a_1)` regardless of whether Π is finite or infinite** — this
  is exactly the content of Lemma 2's proof (Anchor + `p|M` gives any multiple of `M` meets every
  `F_i`). So `A` has density `≥ 1/M` and bounded gaps `≤ M` *unconditionally*, whether or not `Π`
  is finite. There is no bounded-gaps-vs-infinite-Π contradiction to exploit — the "trivial"
  multiples-of-`M` witnesses already explain the bounded gap, so this route is a dead end as a
  *direct* contradiction mechanism. (It could conceivably still be useful as a sub-tool for
  framing (A)'s search, but not as a standalone crux-closer.)

  **(D) "Eventually periodic with linear shift" crux-corpus match.** Searched
  `sequences-and-recurrences`, `divisibility-and-gcd`, `processes-and-algorithms` (NT and combo)
  for "greedy + gcd + eventually periodic." The single close structural match is `aimo-0678`
  (folded into (A) above). `aimo-0503` (`gcd(a_i,a_{i+1}) > a_{i-1} ⟹ a_n ≥ 2^n`) and `aimo-0577`
  (a-ary greedy sequence, answer via residue-class argument) are same-flavor greedy/gcd sequences
  but their mechanisms (strict growth induction; residue-class counting with a coprime `d`) don't
  transplant directly — noted for completeness, not recommended as primary routes.

- Candidate technique(s): **extremal/monovariant argument (transplanted from aimo-0678)** is the
  standout far-framing candidate; secondarily, a sharper density/counting argument on
  simultaneously-active large-prime witnesses per window (framing B), if a per-window bound
  independent of `n` can be found.

- Cheap-kill candidates: none found that dispatch the Crux in one move. The CRT/covering-system
  idea (C) *looked* like a one-line kill and was checked numerically/structurally — it is refuted
  as a direct approach (see (C) above); record this so it is not retried.

- Knowledge-base entries to use: none of `knowledge_base.md`'s named NT entries (Zsigmondy, LTE,
  Dirichlet, Bertrand, CRT/Hensel) directly apply — this problem's crux is closer to a
  monovariant/extremal-principle argument, which the KB's "General Proof Methods" and
  "Pigeonhole / extremal principle" entries name only generically. The KB has no entry specific
  enough to cite for the actual missing step; the outliner should treat the transplanted
  `aimo-0678` monovariant idea as the operative "technique," not a KB citation.

- Analogous past problems (cruxes):
  - **`aimo-0678` (IMO 2015 SL N4)** — closest analog by far: prove `(a_n)` (from a
    `gcd`/`lcm` two-sequence recursion) is eventually periodic. Crux move: construct
    `w_n = min{m ≥ a_n : m ∤ s_n}` (`s_n` a secondary invariant that freezes on one step-type),
    prove `(w_n)` non-increasing hence eventually constant, and read off the finite cycle from
    the stabilized value. **Directly transplantable in spirit** (same top-level claim shape,
    "greedy/recursive integer process ⇒ eventually periodic," proved by extremal/monovariant
    rather than order theory) though no ready-made `s_n` analog currently exists for our problem
    — this is the honest gap in adapting it.
  - `aimo-0503`, `aimo-0577` — same subject area (greedy gcd-driven integer sequences) but their
    specific mechanisms don't transplant; listed for completeness, not recommended.
  - Nothing in the corpus addresses "families of finite prime-sets, prove finitely many
    ⊆-minimal elements" directly — that exact combinatorial shape (an infinite intersecting
    family of finite sets, all meeting a fixed finite anchor set, prove finitely many
    ⊆-minimal members) does not appear to have a crux match; the closest set-family cruxes
    (`aimo-0224`: constructing an infinite family of finite prime-sets with prescribed
    disjointness pattern) go the *opposite* direction (existence of an infinite antichain-like
    family), which is a useful **cautionary** analog: it confirms that "intersecting + anchored"
    families of finite prime-sets *can* be built with infinitely many ⊆-incomparable members in
    general (matching the antichain approach's own §7(b) counterexample) — so the Crux really
    does need the specific *greedy dynamics* of this sequence, not just its set-theoretic shape.

- Prior progress: as recorded in `current.md` / `redundant-constraint-antichain.md` — the entire
  theorem is reduced (rigorously, for all `n ≥ 1`, no transient) to the single Crux: `𝓐_∞`
  (⊆-minimal prime-supports) is finite. Nothing here advances that reduction further; this report
  only scouts alternative attack routes on the Crux itself.

- Dead ends (do not retry):
  - M-threshold confinement `p|L ⇒ p ≤ M` — refuted (`a_1=375` gives `19|L=3990`, `M=15`).
  - "Bounded gaps of `A` ⇒ Π finite" via CRT/covering-system — checked this round and refuted:
    `A` has density `≥ 1/M` and bounded gaps `≤ M` **unconditionally** (via multiples of `M`),
    independent of whether Π is finite or infinite, so there is no contradiction to extract this
    way. Do not resubmit this as a standalone crux-closing route.
  - "Intersecting + anchored (Lemma 1/4) ⇒ finite antichain" — already refuted in
    `redundant-constraint-antichain` §7(b) with the `{p*}∪{q}` counterexample family; confirmed
    again this round via the `aimo-0224`-style construction showing such families *can* be
    infinite in general. The Crux needs the sequence's actual greedy dynamics.

- Small-case / intuition notes: simulation (`a_1 ∈ {105, 375, 385, 1155, 35, 15}`) confirms Π is
  finite in every case, consistent with the theorem (**conjecture**, not proof, from finitely many
  small cases). For `a_1=375`: `Π={2,3,5,7,19}`, `(T,L)=(852,3990)`, matching
  `redundant-constraint-antichain`'s framework once granted. No case examined shows an unbounded
  or growing alphabet; the empirical picture is fully consistent with the Crux but gives no proof
  mechanism — the large prime `19` enters via a genuinely dynamical (not size-threshold) reason
  that the monovariant framing (A) is the best-positioned candidate to eventually capture, since it
  worked for the structurally closest known problem (`aimo-0678`).
