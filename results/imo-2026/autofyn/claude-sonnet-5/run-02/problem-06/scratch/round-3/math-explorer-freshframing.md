## imo-2026-06

- Distinct openings (genuinely orthogonal to the "core prime set / recruitment / CRT"
  language shared by all 5 current approaches):

  1. **A priori numeric bound on load-bearing primes (bound-the-witness-size, not
     bound-the-round-count).** Instead of proving the *recruitment process* (an
     iterative, open-ended set-growth procedure) halts, look for a single **explicit
     numeric bound** B = B(a_1) such that every prime that is ever load-bearing (i.e.
     needed infinitely often to reconcile two disjoint persistent types) is ≤ B. If
     such a bound exists, "finiteness of the core" is immediate for the trivial reason
     that there are only finitely many primes below any fixed B — no monovariant, no
     induction on rounds needed at all. This reframes gap (†) from "does this process
     terminate" to "how large can a load-bearing prime be," a *sizing* question rather
     than a *termination* question. **Caveat found while probing (see below): this is
     NOT free** — the natural witness index m in the Bounded Witness Lemma can be
     arbitrarily deep in the sequence, so a_m (and hence its prime factors) is not
     a priori bounded by a_1 alone; the existing Generalized Bounded Gap Lemma
     (a_{n+1} ≤ a_n + a_1, and the ≤ a_n + a_1·p variant) bounds *gaps*, not the *size
     of prime factors* of a legal candidate. So this framing needs a genuinely new
     ingredient — e.g. a bound on how deep the FIRST witness for a given type-pair can
     occur (index m ≤ some explicit function of |Q| alone, not of n) — to make the
     numeric bound work. Flag as promising but unproven; the outliner should treat
     "bound the witness DEPTH" as the actual sub-target, not "bound the prime size"
     directly (size follows from depth via the Bounded Gap Lemma once depth is capped).

  2. **Decreasing-monovariant / well-ordering framing borrowed from the crux corpus
     (aimo-0678, IMO-style gcd/lcm recursion problem, "eventually periodic" via a
     *non-increasing* potential w_n).** That problem's crux move: define
     w_n = min{m ≥ a_n : m does not divide s_n} (s_n = a_n+b_n), show w_n is
     non-increasing, hence eventually constant by well-ordering on ℕ, and finish from
     there. This is structurally the OPPOSITE shape from our stuck "recruitment
     process" (which is a *growing* set S₀ we're trying to show stops growing) — a
     genuinely different proof shape is to find a quantity that *decreases* with each
     "new prime needed" event and is bounded below, so termination is automatic by
     well-ordering rather than needing an a priori cap. **Important**: current.md
     records that three monovariants were already tried and failed this round
     (persistent-extended-type count, "reconciled pairs stay reconciled", per-term
     prime-factor growth rate) — do NOT resubmit those verbatim. The fresh angle here
     is to mine the *aimo-0678 style* — where the decreasing quantity is defined
     directly on the SEQUENCE VALUES (min unreached integer relative to a running sum),
     not on the recruitment SET — i.e., look for a potential defined via a_n and its
     gaps/witnesses directly (e.g. something like "the smallest candidate window length
     still open" or "distance from a_n to the next integer that is legal using only Q"),
     rather than via prime-set cardinality. This is speculative — no working potential
     was found in the time available — but it is a different search space from the
     three already-ruled-out candidates.

  3. **Positive-density / Mertens-type argument, revived and sharpened, targeting a
     narrower claim than density-sieve-contradiction's stalled step 3.** The stale
     `density-sieve-contradiction` approach tried to prove gap-boundedness by sieve —
     but gap-boundedness is ALREADY unconditionally proved (Bounded Gap Lemma,
     certified, `lemmas/bounded-gap-lemma.md`), so that approach's actual target was
     already moot before it started; its real remaining content (step 4, "each
     recruited prime pays for itself" — bounding blocking types by |Q|) was never
     completed and is worth re-examining, but it is not really independent of the
     "types" language despite billing itself as density/analytic. A genuinely fresh
     analytic angle not yet tried: use that a_n has POSITIVE upper density (from the
     unconditional gap bound a_{n+1} ≤ a_n + a_1, density ≥ 1/a_1) together with
     Mertens' theorem (∑_{p≤x} 1/p ~ ln ln x) to argue that if infinitely many DISTINCT
     primes were each individually necessary (persistently load-bearing) for legality,
     the cumulative "probability" that a random integer in a window of length a_1 is
     blocked by at least one of them would eventually exceed 1 (density → 0), forcing
     the window to sometimes contain NO legal candidate — contradicting that a legal
     a_{n+1} always exists (the process never gets stuck, an unconditional fact of the
     problem's hypothesis). This has the right shape for a genuine contradiction proof
     but the effective bound (how many distinct primes' "blocking probabilities" can be
     packed into a window of FIXED length a_1 before some window becomes fully blocked)
     needs to be made rigorous, and interacts with the fact that don't-need-ALL-primes
     -to-block-everything (types already often overlap by design of the greedy
     process). Rate this as plausible-but-hard, genuinely different in flavor
     (analytic/counting, not structural/set-theoretic) from all 5 current approaches.

  4. **Consecutive-gcd sequence d_n := gcd(a_n, a_{n+1}) as an independent object
     (dispatch idea 3).** Probed this directly: d_n is itself a positive integer > 1,
     but numerically (a_1=15, 35, 1001 checked) it shows no obviously simpler
     structure than the full sequence — it inherits all the same case-dependence on
     "which types intersect." This does not look like a shortcut; recommend NOT
     pursuing as a primary route (assessed and set aside, not a dead end proven false,
     just no traction found in the time available).

- Candidate technique(s): (1) an explicit-bound / witness-depth argument (extension of
  the already-proved Bounded Witness Lemma / Finite Core Theorem, replacing
  "termination of an open-ended process" with "boundedness of a witness index");
  (2) a well-ordering/monovariant argument in the *aimo-0678* style, built on a
  potential defined on sequence VALUES rather than on the recruitment SET; (3) a
  Mertens/density counting argument using the ALREADY-PROVED positive density
  (Bounded Gap Lemma) against an ALREADY-PROVED fact that the process never gets stuck
  (existence of a_{n+1} is given by problem hypothesis) to bound the number of
  distinct persistently-load-bearing primes directly, without any recruitment
  iteration language.

- Cheap-kill candidates: none obvious this round — did not find a one-line parity /
  pigeonhole kill of gap (†) itself; the existing certified lemmas (Free Facts,
  Bounded Gap Lemma, Persistent-Type Pigeonhole, Finite Core Theorem) already extract
  the cheap structural facts. One genuinely cheap observation worth flagging: the
  Persistent-Type Pigeonhole bound |𝒫| ≤ 2^{|Q|} - 1 is FIXED FROM THE START (depends
  only on Q = P(a_1), not on any recruited set) — so the number of *disjoint base-type
  pairs* needing reconciliation is itself already finite and fixed at round 0, before
  any recruitment. The open question is only whether reconciling them (finding glue
  primes) can be done with a UNIFORMLY bounded amount of "extra" structure — not
  whether there are finitely many pairs to reconcile (that part is already free).

- Knowledge-base entries to use: "Modular arithmetic, CRT" (`knowledge_base.md` line
  ~59, for the eventual finish once a finite core is secured); "Pigeonhole / extremal
  principle" and "Invariants & monovariants" (lines ~108–117) — generic entries, no KB
  entry specific to density/sieve or well-ordering termination arguments exists in
  this KB, so any of openings 2–3 above would be argued from first principles (Mertens'
  theorem, well-ordering on ℕ), not cited KB entries.

- Analogous past problems (cruxes):
  - **aimo-0678** (`past_crux_moves_database.json` / `past_problems_database.json`) —
    genuinely the closest analog found: "Prove (a_n) is eventually periodic" for a
    gcd/lcm-defined recursive sequence. Crux move: define w_n = min{m ≥ a_n : m does
    not divide s_n = a_n+b_n}; prove w_n non-increasing (Claim 1, casework on whether
    a_n | b_n); conclude it stabilizes; finish via gcd(w, s_n) analysis. Genuinely
    analogous in TARGET (eventual periodicity of an integer sequence defined by a
    greedy/deterministic divisibility rule) and in PROOF SHAPE (a decreasing potential
    forced to stabilize by well-ordering, THEN a second argument closes the case) —
    but NOT analogous in mechanism: their recursion only depends on the single
    previous state (a_n, b_n), a genuine 2-coordinate Markov map, so finiteness of the
    reachable state space is comparatively easy once boundedness is shown. Our
    problem's legality condition depends on ALL prior terms simultaneously, which is
    exactly the extra difficulty the "type"/"core" machinery exists to compress into a
    finite summary — so this crux's finish does not transfer directly, but its overall
    "find a non-increasing potential, invoke well-ordering, THEN argue" shape is worth
    the outliner considering as opening 2 above.
  - **aimo-0648** (bounded partial-average sequence, eventually constant) — the
    "sequence stays in a bounded interval ⇒ finite state space ⇒ pigeonhole ⇒ eventually
    periodic, then use the periodic MAXIMUM's forced-propagation to show it's actually
    eventually CONSTANT" shape. Less directly analogous (their sequence itself is
    bounded; ours is unbounded, only the GAPS are bounded) but useful as a template
    for the "given boundedness, extract periodicity via pigeonhole on a max/extremal
    state" step — which is essentially what the existing approaches already do at
    their CRT finish (Step 5 in `covering-system-construction`). Not a new opening,
    confirms the existing finish step is the standard move.
  - **aimo-1025** (Mathbook friendship / clique-completion process) — a "run a
    canonical greedy version of the closure operation until stuck, argue anything
    reachable at all must have this canonical run terminate at the full object" crux.
    Structurally similar in FLAVOR to our "recruitment process" (an operation that
    keeps enlarging a structure until no more moves apply) but their termination is
    for a *different reason* (monotone clique-cover size bounded by the fixed vertex
    count n = 2022, a hard finite ambient set from the start) — we lack an analogous
    a priori finite ambient set for the primes (that's exactly gap (†)). Judged NOT
    genuinely analogous enough to import a technique from, beyond confirming that
    "canonical greedy run, argue reachability forces termination at the same place" is
    a known crux shape worth keeping in mind if a natural finite ambient prime-bound
    can be found (ties back to opening 1).
  - Searched the corpus (`processes-and-algorithms`, `invariants-and-monovariants`,
    `sequences-and-recurrences`, `pigeonhole` subtopics in number_theory and
    combinatorics) for "greedy deterministic eventually periodic," "minimal legal
    candidate," "recruitment," "core set" — no other problem closely matches the
    specific "smallest-integer-satisfying-all-past-gcd-constraints" mechanism; this
    appears to be a genuinely novel construction among the corpus's 2434 cruxes (no
    problem_id found reusing this exact greedy-legality-vs-all-history rule).

- Prior progress: see `results/imo-2026-06/current.md` — 10 certified unconditional
  lemmas (Free Facts, Bounded Gap Lemma + generalization, Persistent-Type Pigeonhole,
  Bounded Witness Lemma + generalization + single-witness refinement, Finite Core
  Theorem, Extended Persistent-Type Pigeonhole, |Q|=1 fully solved). Gap (†) — halting
  of the S₀-recruitment process — remains the single open crux across all 5
  approaches, reformulated but not resolved for 2 rounds running (rounds 1–2).

- Dead ends (do not retry, verified from current.md + independent check this round):
  - "Universal glue prime" (single smallest prime outside Q reconciles everything in a
    sparse-Q regime) — refuted by explicit a_1=35 counterexample (T=34, L=210, needs
    TWO extra primes {2,3}); re-verified independently by this round's reviewer via
    direct simulation (confirmed here too, section "Small-case notes" below).
  - "cost(n) ≤ 1 in sparse-Q regime" — refuted, same counterexample data (cost(153)=2
    with an irrelevant "junk" prime 13).
  - Three monovariants on the recruitment-process ROUND COUNT (persistent-extended-
    type count non-monotone in useful direction; "reconciled pairs stay reconciled"
    unproved per-round; per-term prime-factor growth rate doesn't control distinct
    recurring primes) — do not resubmit verbatim; opening 2 above suggests searching
    for a monovariant on SEQUENCE VALUES instead of on the recruitment SET, which is a
    different search space, not yet tried.
  - `hypergraph-transversal`'s "Key Lemma" (finiteness of eventual prime support via a
    Φ_n = Σ 2^{-min(B)} potential) — self-flagged in-file as incomplete/circular
    (assumes what it needs to prove); re-read this round and confirms it is indeed the
    same crux dressed in antichain language, not a new route. Its "hand-off to a
    sieve/counting estimate" pointer is essentially opening 3 above, reframed.
  - `density-sieve-contradiction`'s Step 3 (raw sieve to prove gap-boundedness) is
    MOOT — gap-boundedness is already unconditionally proved (Bounded Gap Lemma); this
    approach's premise (that boundedness itself was the hard part) is stale. Its Step
    4 sub-route ("blocking types capped by |Q|") was never completed; worth revisiting
    only as a possible ingredient of opening 3, not as a standalone route.

- Small-case / intuition notes (all CONJECTURE / numerically observed, not proved):
  - Simulated a_1 ∈ {15, 21, 35, 105, 1001} out to 60 terms. In every case the prime 2
    (and usually 3) gets recruited into the factorization of terms within the first
    2–5 steps — recruited primes appear to skew SMALL early, consistent with the
    greedy rule preferring small legal candidates. This is weak evidence FOR opening 1
    (a numeric bound on load-bearing primes) if one can show the recruitment always
    happens "early" (bounded witness depth) rather than possibly being deferred
    arbitrarily far into the sequence — but the a_1=35 counterexample data (persistent
    type {5} recurring with odd terms hundreds of times deep, per current.md) shows
    that *reconciliation* can be deferred very deep even when the relevant primes
    {2,3} were both already present from early on — so "prime size is small" does NOT
    immediately imply "witness depth is small." This tension (small primes vs. deep
    witness indices) is the crux narrowed to its sharpest form; the outliner should
    treat "bound the witness INDEX m, not the prime p" as the real open sub-target if
    pursuing opening 1.
  - For a_1=1001, incidental large primes (47, 73, 37, 79, 43, 41...) appear ONCE each
    in the first 20 terms and do not recur in that window — consistent with the
    "junk prime" phenomenon already documented (cost(153)=2 with irrelevant 13 for
    a_1=35): most prime factors of any given term are irrelevant noise, only a small
    persistent subset matters. No new structural insight beyond what's already
    documented, but confirms the phenomenon generalizes past the a_1=35 example.
