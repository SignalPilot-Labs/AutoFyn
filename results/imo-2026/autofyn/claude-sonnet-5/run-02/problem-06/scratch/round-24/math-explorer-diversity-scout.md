## imo-2026-06 (lens: diversity scout — fresh subfamily + fresh whole-problem framing)

- Distinct openings:
  1. **New 5th-subfamily candidate: `a_1 = 3^a * q` (fixed exponent `a>=1` on
     the SMALL prime 3, `q` a large prime, `q!=3`)** — structurally distinct
     from the currently-stuck `a1-3qk-subfamily-theorem` (`a_1=3*q^m`, which
     exponentiates the LARGE prime and is provably stuck for `m>=2`, see
     Dead ends below). Numerically verified (`q` prime in `[7,300)`, up to 90
     terms, `math.gcd`-based simulator): `a=1` (certified already, 0
     exceptions), `a=2` (`9q`) has exactly **one** exception (`q=11`, breaks
     at `n=5`: actual `a_5=110` vs predicted `120`), `a=3,4,5` (`27q,81q,
     243q`) have **zero** exceptions out of 59 tested primes each. This
     matches memory rule 30's earlier flag (`9q` fails at `q=11`) but adds
     the new, more important finding: **`a=3,4,5` are fully clean**, so the
     single `a=2` exception looks like exactly the same kind of small,
     hand-resolvable residual case that `a1-3q` itself had (2 exceptions,
     `q=7,11`), not a structural obstruction. Algebraic reason this
     generalization is the RIGHT axis (unlike `3q^m`): in the `K_0` bookkeeping
     used by the certified `a1-3q` proof, `K_0 = (a_{n_0}+2)/q`. For
     `a_1=3^a q`, `K_0` scales like the FIXED constant `3^a` (independent of
     `q`) — exactly like the certified `m=1` case's bounded `K_0∈{4,5}` — so
     the same Legendre Sieve Gap Bound / Primorial Floor Bound toolkit that
     closed `a1-3q` should transplant with only a *larger but still-fixed*
     residual table (indexed by `a`, not growing with `q`). This is the
     opposite of `a_1=3q^m`'s failure mode, where `K_0~3q^{m-1}` grows
     *with* `q`, permanently breaking `L/K_0->infinity`. **Recommend
     the outliner open this as a genuinely new build target instead of
     continuing to push `a1-3qk-subfamily-theorem`'s stuck `m>=2` case.**
  2. **General principle surfaced (useful for future subfamily scouting,
     not itself a theorem):** the toolkit's "clean literal T=1,L=c
     periodicity" pattern needs `K_0` (the ratio `(a_1+O(1))/q` near the
     first hard occurrence) to stay BOUNDED as the large prime `q→∞` —
     i.e. it needs `a_1/q` bounded, i.e. `a_1 = c(q)*q` with `c(q)` bounded
     (ideally constant). This is exactly satisfied by `3q`, `5q`, `3^a*q`
     for fixed `a` — and exactly violated by `3q^m` (`m>=2`), where the
     large prime's OWN exponent grows. This gives a crisp criterion for
     future subfamily proposals: **fix the SMALL-prime part's structure
     (any power, any number of small primes with additional casework), but
     always keep the LARGE prime to the first power** — this alone predicts
     which of the many `a_1=c*q` variants are tractable vs FAH-hard.
  3. **Composite small-part with >=2 distinct primes is a trap, not a
     shortcut — checked concretely, saving a future round from trying it.**
     I hypothesized composite `c` (e.g. `c=6,10,12`) might need LESS
     casework (its own small primes eliminate residues for free). Checked
     numerically: **every even `c` tested (`6,9->no,10,12,14`) reduces
     trivially to the ALREADY-CERTIFIED `2|a_1` theorem** (`L=2`, not `L=c`)
     — because `2|a_1` forces the intermediate even offset `a_n+2` to be
     LEGAL (shares factor 2 with every prior even term), not illegal as a
     naive "c's own primes kill residues" argument would assume; I had the
     legality direction backwards on first pass — worth flagging so no one
     repeats this reasoning error. For `c` with TWO distinct ODD primes
     (`c=15,45,33`): numerically MESSY (`c=15,45`: 32/32 primes fail at
     literal `L=3`; `c=33`: 8/31 fail) — consistent with the long-standing
     finding that `|Q|>=3` distinct-prime seeds (like the canonical `a_1=15`
     itself) are genuinely FAH-hard, not a new tractable subfamily. `c=21,27`
     (one odd prime to a power, or `3*7`) tested clean at `N<=150,q<300` but
     this is much weaker evidence than the `3^a*q` family's structural
     argument above and should NOT be assumed tractable without its own
     `K_0`-boundedness check.
  4. **Fresh whole-problem framing / crux-corpus search (task 2), broadened
     beyond number_theory:** searched the full 2434-crux corpus (all 3
     domains) for "greedy" + "eventually periodic"/"ultimately periodic"
     keyword co-occurrence. Found only 3 genuinely on-topic hits:
     `aimo-0514` (reversible-transition-map / bijection-on-finite-state-set
     — already imported round 5, dead, equivalent to gap †), `aimo-0907`
     (orbit-merging additive offset — already imported round 22/23, dead,
     equivalent to the theorem itself), and `aimo-0648` (order-statistic
     invariant confines a recurrence to a bounded interval, forcing eventual
     periodicity via pigeonhole on a finite state space) — this LOOKS fresh
     but on inspection is exactly the already-exhausted "finite bounded state
     space" corridor (cofinite-window-capacity-bound / subword-complexity-
     periodicity / transfer-matrix, all dead per rounds 9,12,17): the
     obstruction is always the same — no a priori bound exists on the state
     needed to determine legality (the "core" is exactly the unbounded
     object FAH must control). **No genuinely new crux-corpus mechanism was
     found this round for H1** — the corpus well for this exact crux appears
     to be as exhausted as the technique-family sweep already found.

- Candidate technique(s): For opening 1 — the SAME certified toolkit
  (Legendre Sieve Gap Bound `lemmas/legendre-sieve-gap-bound.md`, Primorial
  Floor Bound `lemmas/primorial-floor-bound.md`, Parity Witness identity
  `gcd(N,a_n)=gcd(N,N-a_n)`) used to close `a1-3q`. For opening 4 — none new;
  do not re-dispatch a generic H1 fresh-framing sweep.

- Cheap-kill candidates: `K_0`-boundedness-as-`q→∞` is now a cheap, purely
  algebraic pre-screen any future subfamily proposal `a_1=f(q)` should pass
  BEFORE committing a build slot: compute `K_0 = (a_1 + O(1))/q` symbolically
  and check whether it grows with `q` (kill, like `3q^m` `m>=2`) or is fixed
  (proceed, like `3^a q`, `3q`, `5q`). This would have flagged `3q^m`'s `m>=2`
  failure in round 23 before a build slot was spent on it.

- Knowledge-base entries to use: none beyond what's already certified in
  `lemmas/` for the subfamily route (Legendre Sieve Gap Bound, Primorial
  Floor Bound, parity/gcd-difference identity `gcd(x,y)=gcd(x,x-y)`).
  `knowledge_base.md`'s generic sieve/pigeonhole entries (already cited by
  prior rounds) remain the relevant ones; no new KB entry identified this
  round.

- Analogous past problems (cruxes): `aimo-0514` and `aimo-0907` remain the
  closest whole-corpus analogs for H1 but both are confirmed already-dead
  imports (do not re-propose). `aimo-0648`'s order-statistic-confinement
  mechanism is worth naming explicitly as a THIRD confirmed-equivalent
  instance of the "bounded finite state space" corridor (already dead via
  cofinite-window-capacity-bound / subword-complexity-periodicity), so a
  future explorer doesn't waste a round re-finding it as if new. No genuinely
  fresh analog found in this pass across all 3 domains.

- Prior progress: 3 certified subfamily theorems (`2|a_1`; `a_1=p^k`;
  `a_1=3q`, q prime>=7,!=5) plus gap-free Master Conditional Theorem reducing
  the general case to H1(FAH)+H2. `a1-3qk-subfamily-theorem` (`a_1=3q^m`) is
  `partial`, stuck for `m>=2` on a genuine, well-diagnosed growth-rate
  mismatch (not a routine finishing touch — see Dead ends). `a1-5q-subfamily-
  theorem` is outline-only, not yet built, deprioritized by round 23's own
  outliner in favor of the (now-stuck) `3qk` target.

- Dead ends (do not retry):
  - `a1-3qk-subfamily-theorem`'s `m>=2` case: PROVABLY insufficient via the
    certified Legendre/Primorial toolkit as-is (`K_0(q,m)~3q^{m-1}` grows
    with `q`, `L/K_0` capped below 1, crude bound fails at essentially every
    tested prime for `m=2,3`, not a finite residual table). Needs either a
    genuinely stronger Chebyshev/Jacobsthal-strength `omega`-bound (confirmed
    absent from KB/crux corpus, round 21/22/23) or a different algebraic
    mechanism — do not re-attempt with the same sieve tools; this round's
    finding (opening 1) explains WHY (wrong axis: exponentiating the large
    prime, not the small one) and gives a concrete escape (exponentiate the
    small prime instead).
  - Composite even `c` in an `a_1=c*q` family: NOT a genuine new subfamily —
    collapses trivially to the already-certified `2|a_1` theorem (`L=2`, not
    `L=c`) since the shared even factor makes the small intermediate offset
    LEGAL, not illegal. Don't propose "composite c needs less casework" —
    checked and refuted this round.
  - `a_1=c*q` with `c` having >=2 distinct ODD prime factors (e.g. `15q,
    45q, 33q`): messy/mostly-failing numerically, consistent with the
    long-standing `|Q|>=3` FAH-hard regime (like `a_1=15` itself) — not a
    tractable subfamily via this toolkit, don't propose without new
    machinery.
  - General H1/FAH fresh-framing sweep: per round-23 finding and this
    round's crux-corpus re-check, the well is exhausted (30+ mechanisms
    dead, plus this round's 3 corpus hits all confirmed already-dead or
    equivalent-to-dead corridors). Do not dispatch another generic sweep;
    channel explorer effort into subfamily scouting (task 1's terrain) or a
    bespoke narrow-case attack instead.

- Small-case / intuition notes (all CONJECTURE from numerics, not proofs):
  - `a_1=3^a*q` (fixed `a>=1`, prime `q`, `q!=3`) conjectured to have literal
    `T=1,L=3^a` periodicity for all `q` outside a small, `a`-dependent
    (not `q`-magnitude-dependent) finite exceptional set — verified `a=1`
    (0 exceptions, already certified), `a=2` (1 exception, `q=11`), `a=3,4,5`
    (0 exceptions each) on primes up to 300.
  - `K_0`-boundedness is conjectured (not proved) to be the exact dividing
    line between "same-toolkit-tractable" and "FAH-hard" for `a_1=f(q)`
    single-large-prime families; only checked on the handful of `c` values
    above, not derived as a general theorem.
