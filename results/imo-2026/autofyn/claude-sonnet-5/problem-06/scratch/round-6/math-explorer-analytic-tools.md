## imo-2026-06

- Distinct openings (this lens = hunt for an analytic-NT/probabilistic closing
  tool for 𝓥_S-finiteness, now that the search space is ≤2^k-2 proper cores):
  1. **Confirmed-absent-tool opening (negative but load-bearing):** neither
     `knowledge_base.md` nor the crux corpus contains any sieve/Mertens/
     Borel–Cantelli/second-moment machinery applicable here — see "Cheap-kill
     candidates" and "Dead ends" below for the concrete reason it doesn't fit
     this problem's structure. Report this explicitly to the outliner so a
     4th round isn't spent re-searching the same terrain.
  2. **"Local Case I" opening (new, promising, non-analytic):** numerically,
     the local channel for a *singleton* proper core `S={p}` (e.g. `a_1=4087`,
     `S={61}`) looks structurally like a scaled-down copy of the
     already-solved Case I (Theorem CI) situation — a "fan" of two-prime
     radicals `{q,p}` for varying extra primes `q`, absorbed all at once when
     a term of radical exactly `{2,p}` (or some other minimal extra-prime
     combo) finally appears. Theorem CI's mechanism (an *exact closed form*
     for `a_n` under Case I, letting you compute exactly when a pure
     `p`-power term appears) is the template; the open question is whether an
     analogous (weaker, not necessarily closed-form) arithmetic argument can
     pin down "some term with radical `⊆{q_0}∪S` for a small explicit `q_0`
     must eventually appear" for a *local* channel even without a global
     closed form. This is a concrete, narrower, non-analytic next target —
     see numeric evidence below. NOTE: I could not find or construct the
     needed bound in this session; flagging it as the most promising *shape*
     of argument, not a working proof.
  3. **Debunked opening (tested and killed this round):** "extra primes
     recruited into a proper core's fan are always `< max(S)`" — plausible
     from the `a_1=4087` example but numerically REFUTED on `a_1=105`,
     `S={5}⊊P_1={3,5,7}`, where extra primes `11,13 > 5` are recruited. Do
     not resurrect this exact bound; any working bound must be more subtle
     than "primes less than the core."

- Candidate technique(s): none found that are genuinely analytic/probabilistic
  and applicable. The one semi-relevant crux template worth naming
  (`aimo-0134`, see below) is a **non-analytic** integer-monovariant +
  difference-identity transfer, already conceptually tried and known
  insufficient here (the (MRS)/𝓥_S cardinality is provably non-monotone,
  round 4's `a_1=4087` 17→3 collapse) — its *transfer-back* trick (recover
  the original object from a stabilized auxiliary average) is the only piece
  not yet explicitly tried, and might be worth 5 minutes of thought next
  round: is there some OTHER auxiliary quantity (not |𝓜_n^S| itself) that
  IS exactly monotone in the local channel, from which 𝓜_n^S's eventual
  constancy could be read off via a difference identity? Untested, not
  claimed to work.

- Cheap-kill candidates / structural reasons analytic tools don't fit:
  - **No randomness to exploit.** The sequence `(a_n)` is fully deterministic
    (no free parameter, no family to average over) — `knowledge_base.md`'s
    only probabilistic-method-adjacent entries (weighted-averaging arguments)
    and the crux corpus's `probabilistic-method` cruxes (checked both
    `combinatorics` and `algebra` domains, 5 total hits, none number-theoretic)
    all require a genuine random/averaging construction over a *family* of
    objects; there is no such family here to average over. This is a
    structural, not just empirical, reason a Borel–Cantelli-style argument
    doesn't transplant.
  - **Wrong direction on Mertens.** `Σ_{p≤x} 1/p ~ log log x` *diverges* — if
    anything this says the "resource" of available primes for the greedy rule
    to recruit into a fan is *not* scarce, i.e. Mertens' theorem is evidence
    *against* an easy sieve-exhaustion argument (which typically wants a
    convergent series, e.g. `Σ1/p²`, to show only finitely many "bad" primes
    ever get used). No natural convergent-series quantity in this problem
    was found to bound total recruitment (checked `|𝓥_S|` vs several
    candidate convergent sums numerically, no clean match — see below).
  - **The dead-`d` gap is structural, not just "not yet found."** Any
    Markov/Chebyshev/Cauchy–Schwarz argument on `Σ_q D_n(q)²`-type quantities
    (round-3-certified Domination Lemma territory) bounds *instantaneous*
    concurrent state (`|𝓜_n^S|` at a fixed `n`), never *cumulative distinct
    arrivals* (`|⋃_n 𝓜_n^S| = |𝓥_S|`) — these are different quantities, and
    the problem's difficulty is entirely in the latter (round 5's own
    `a_1=4087` data already shows `|𝓜_n|` non-monotone with a `17→3`
    collapse, i.e. bounded concurrent size at any one time does NOT bound
    total distinct visitors over all time, since a bounded-size antichain can
    still cycle through unboundedly many never-repeated values in principle —
    only the already-certified No-Resurrection Lemma rules that out, and it's
    a combinatorial not analytic fact).

- Knowledge-base entries to use: none new. Confirmed (re-reading the entire
  `knowledge_base.md` Number Theory section) it contains no Mertens/sieve/
  density entry at all — only Bertrand's postulate and Dirichlet's theorem
  (primes in AP), neither of which bounds a recruitment/accumulation process
  (they *guarantee* primes exist in a range, the opposite of what's needed
  here). No "greedy sequence" or "radical/squarefree kernel" KB entry exists
  either (checked explicitly per dispatch instruction 2) — the closest is the
  generic "Divisor analysis" bullet, already implicitly used by every
  certified lemma in `lemmas/`.

- Analogous past problems (cruxes):
  - `aimo-0477` (number_theory, `divisibility-and-gcd`/`p-adic-valuation`,
    Mongolia sequence problem: eventually-constant `a_n` from an integrality
    condition on a cyclic sum) — crux move "track `d_n=gcd(a_1,a_n)`, show
    it's a divisor of `a_1` hence bounded, and *nondecreasing*, so it
    stabilizes automatically (finite ascending chain in the finite poset of
    divisors of `a_1`), then transfer via `a_1=d·α`, `a_n=d·β_n` to get
    `β_{n+1}|β_n` eventually constant." **Genuinely close in flavor** (a
    gcd-chain sequence proven eventually periodic/constant) but the key
    mechanism — boundedness by a FIXED finite object (`a_1`'s divisor
    lattice) — does not transfer: our proper-core fans are not bounded by
    any a priori fixed finite set (new primes `q` of unbounded size keep
    entering), so there is no finite ambient lattice to sit inside. Worth
    citing as the closest corpus analogue, but confirmed NOT directly
    adaptable.
  - `aimo-0134` (number_theory, `size-bounding-and-descent`/
    `sequences-and-recurrences`, "sequence eventually constant" via
    partial-sum-average monovariant) — crux move: define an auxiliary
    quantity (`b_k`, the integer running average) that is PROVABLY
    nonincreasing and bounded below, hence eventually constant by
    well-ordering, then recover the original sequence's eventual constancy
    via an exact difference identity `a_k=(k+1)b_{k+1}-k b_k`. Structurally
    the cleanest "monovariant + transfer" template in the corpus, but (as
    above) our natural candidate monovariant `|𝓜_n^S|` is provably
    non-monotone (round 4), so the direct transplant fails; flagging the
    *transfer-back-via-difference-identity* idea as untested in a different
    coordinate, not as a working plan.
  - `aimo-0503` (number_theory, `size-bounding-and-descent`/
    `divisibility-and-gcd`, `gcd(a_i,a_{i+1})>a_{i-1}` forces `a_n≥2^n`) —
    same general "gcd bounds the gap" family as this problem's already-
    certified Domination Lemma; no new content beyond what's already
    certified in `lemmas/`.
  - Not analogous / do not pursue further: `aimo-0628` (M=P prime-recruitment
    problem) superficially resembles "prime recruitment" but its mechanism
    (residue-class sparseness + Fermat's little theorem forcing a specific
    prime's appearance) needs a multiplicative structure (`p_1⋯p_k+1`) with
    no counterpart in the gcd-chain recursion here.

- Prior progress: unchanged from round 5's headline — problem reduces to
  finiteness of `𝓥_S` for each proper nonempty core `S⊊P_1`
  (`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`), equivalently
  (MRS_S) per `lemmas/channel-splitting-lemma.md`, equivalently `𝓥` finite
  per `lemmas/theorem-V-veto-finite-iff-MRS.md`. Case I and the top core
  `S=P_1` are closed unconditionally (`lemmas/theorem-CI-case-I-explicit-
  stabilization.md`, Lemma TC). This exploration found **no new tool that
  closes any piece of this gap** — see Dead ends.

- Dead ends (do not retry):
  - Density/Borel-Cantelli/second-moment argument on `Σ 1/p` or `Σ D_n(q)²`
    type quantities *as a route to bounding `|𝓥_S|`* — structurally mismatched
    (see Cheap-kill candidates above): bounds concurrent state, not cumulative
    arrivals; and there is no genuine randomness to exploit (this session's
    finding, extends round 3's already-recorded finding (d) with the
    structural "why," not just the numeric "insufficient").
  - "extra primes recruited into a proper core's fan are bounded by `max(S)`"
    — refuted this session, `a_1=105`, `S={5}` recruits `11,13`.
  - Direct transplant of `aimo-0477`'s "bounded ascending divisor chain"
    mechanism — fails because our fans are not bounded by any fixed finite
    ambient set (checked this session; the mechanism needs a fixed reference
    integer like `a_1`, which our proper-core fans do not have).
  - Zsigmondy/primitive-divisor corpus entries (`aimo-0157`, `aimo-0611`) —
    checked, both go the *wrong direction* (guaranteeing NEW primes appear),
    which is the opposite of what a finiteness proof needs.

- Small-case / intuition notes (all labeled conjecture/empirical, not proof):
  - For `a_1=4087` (`P_1={61,67}`), the local channel for singleton core
    `S={61}` (2062 of the first 4000 indices) recruits extra primes
    `{2,3,5,7,11,13,17,19,23,29,37,41,43,47,53,59}` (16 of them — every prime
    `<61` except `31`, interestingly) one at a time, each forming a transient
    fan member `{2 or that prime, 61}` or similar, before collapsing at
    exactly `n=54` to the single stable value `{2,61}` — reproduces round 4's
    documented `17→3` collapse for the GLOBAL antichain exactly, and shows
    the local-`S={61}` piece is essentially the entire story of that
    collapse. This *looks* like a scaled analogue of Case I's exact
    mechanism (recruiting "candidate extras" until a specific arithmetic
    target — here apparently `2·61=122`-type coincidence — gets hit), but I
    did not find why `31` alone is skipped or derive a general bound; flagged
    as raw data for round 7's outliner, not a proof sketch.
  - For `a_1=105` (`P_1={3,5,7}`), ALL 6 proper cores stabilize almost
    immediately (`|𝓥_S|∈{1,3}`), and the one core with `|𝓥_S|=3` (`S={5}`)
    recruits primes `2,11,13` — i.e., a small "easy" case gives no signal
    about the general mechanism; only genuinely hard `a_1` (large, few
    prime factors, per round 3-5's stress-test methodology) exercise the
    real difficulty. Consistent with, not new beyond, prior rounds' findings.
  - Net numeric conclusion of this session: **no counterexample to (MRS_S)
    was found** (consistent with all prior rounds — every tested proper core
    across every tested `a_1` eventually stabilizes), but **no bound
    mechanism (analytic or otherwise) was found either**. This is negative
    information of the same character as rounds 3-5's findings: the
    conjecture keeps surviving numerically, but the *proof* keeps eluding
    every tool tried so far, analytic tools now included.
