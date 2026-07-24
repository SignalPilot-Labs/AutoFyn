## imo-2026-06

- Distinct openings (analytic/counting angles NOT yet tried in this workspace):
  1. **AP-identity + divisibility-difference-vanish upgrade** (aimo-0680 Step 2 style). The
     general shape: if a quantity is known to lie on infinitely many "candidate arithmetic
     progressions" (here: infinitely many indices n_j with q*|a_{n_j}, guaranteed by the
     already-certified Generalized Bounded Witness Lemma / infinite pigeonhole), pick two
     far-apart indices y > j in that infinite set so that BOTH of two competing quantities are
     divisible by y-j while their difference is smaller than y-j, forcing the difference to
     vanish exactly (not just "eventually small"). This is a genuinely different mechanism from
     gcd-pigeonhole: it does not try to promote "some prime works" to "one prime always works"
     directly, it instead exploits an exact linear/AP structure to force TWO OCCURRENCES to
     coincide exactly. The catch (see Cheap-kill / gap below): aimo-0680's version needs the
     problem's own strong global identity `n | f^n(m)-m` to make "divisible by y-j" available at
     all; our greedy sequence has no known analog of this identity (only the weaker `a_{n+1} <=
     a_n + a_1`, no index-divisibility structure). This is a real gap, not a technicality — see
     "why it might fail" below.
  2. **Return-time / syndetic-recurrence counting bound.** A genuinely new, currently UNPROVEN
     structural fact worth testing first as a cheap-kill: is there a uniform bound B (depending
     only on S₀, not on the specific extended type) such that consecutive occurrences of any
     fixed extended-persistent type A' have index gap ≤ B? If so, the occurrence-index
     subsequence n_1<n_2<... of A' is syndetic, which is exactly the missing ingredient any
     aimo-0680-style "dense row" argument needs (their Step 2 first manufactures a syndetic/dense
     row via a pigeonhole counting argument over windows before the AP-identity step fires). This
     bound is NOT currently certified anywhere in the lemma stack — Extended Persistent-Type
     Pigeonhole only says *some* persistent type recurs within a bounded window, not that a FIXED
     type A' does. Worth a direct numerical check before any proof attempt (see Cheap-kill below).
  3. **Growth-rate / linear-density counting on the finite divisor alphabet (Confined-GCD
     Lemma).** Confined-GCD already reduces the FAH exception set to `⋃_{d∈D_bad} {n : g_n=d}`,
     a finite union over a FIXED finite alphabet Div(b). A genuinely analytic move not yet tried:
     instead of asking "is one class infinite" (the pigeonhole that already stalls), ask whether
     the classes' NATURAL DENSITIES among A'-type occurrences sum correctly and whether a
     counting/averaging argument (e.g. Cesàro sums of an indicator, or an Abelian/Tauberian-style
     argument) can show all but the q*-class classes have density 0 with SUMMABLE (not just
     density-0) occurrence — i.e. `sum_n [g_n = d, d bad] < infinity` via a comparison/telescoping
     count rather than density. NOTE: round 8's certified rule (math-explorer memory rule #24)
     already flags that bare density-1 is NOT strong enough (density-1 ≠ cofinite), so density
     alone is a dead end; the only way this angle could work is if it can be upgraded to an
     explicit SUMMABLE/telescoping bound (à la aimo-0134's monovariant-drop-to-integer-floor
     trick or aimo-0477's second solution's "nonincreasing p-adic valuation, hence eventually
     constant" argument) rather than a soft asymptotic density statement.
  4. **p-adic valuation monotonicity à la aimo-0477 (2nd solution).** That solution shows
     `v_p(a_n)` is eventually monotone (nonincreasing or nondecreasing depending on a dichotomy)
     using the problem's OWN algebraic identity (`s_{n+1}-s_n` integer forces valuation
     inequalities). The mechanism (monotone bounded integer sequence ⟹ eventually constant) is
     a completely different tool from anything tried in 9 rounds (all 9 dead mechanisms are
     pigeonhole/infinite-existential, none use monotonicity of a valuation or an integer
     potential). It requires finding OUR problem's analog of their sum-integrality identity — not
     found yet; flagged as the key missing ingredient, see Dead ends below.

- Candidate technique(s): (a) aimo-0680-style two-step "dense row via window-counting" +
  "AP-identity divisibility-difference-vanish" upgrade,  (b) a genuinely new **Return-Time
  Boundedness Lemma** (untried, unproven) as a prerequisite for (a), (c) monotone integer
  potential / p-adic valuation descent (aimo-0134, aimo-0477 2nd solution style) IF a suitable
  potential tied to gcd(a_n, a_{n_B}) or v_q*(a_n) can be found that is forced monotone by
  MINIMALITY of the greedy choice rather than by an algebraic sum-identity (since our problem
  has no such identity). This monovariant angle is DIFFERENT from the three size/index
  monovariants already killed (rounds 3, 5) — those measured set-size or witness-index, not a
  p-adic valuation or a gcd value.

- Cheap-kill candidates:
  - **Test Return-Time Boundedness numerically first** (opening #2): for several seeds with a
    genuine |F'|≥2 rogue pair at a correctly-recruited core (a_1=4807, 11305, and any other
    from round 9's sweep), compute the extended-persistent type A' of the rogue pair and measure
    max/mean/variance of consecutive-occurrence index gaps over a long window (N~5000-15000).
    If gaps grow unboundedly (not just large but scaling with n), this whole opening (#1, #2)
    dies immediately as a cheap kill before any proof effort. If gaps stay bounded, it's a
    genuinely promising, previously untested structural fact worth its own lemma attempt.
  - **Check whether Confined-GCD's g_n sequence is itself eventually monotone** (a direct
    numerical test of opening #4's needed ingredient): for the same rogue-pair seeds, track
    g_n = gcd(a_n, a_{n_B}) restricted to A'-type occurrences n_1<n_2<... and check if the
    SEQUENCE g_{n_1}, g_{n_2}, ... is eventually monotone (nondecreasing, divisor-ordered) rather
    than just eventually-constant-at-full-value. If it's NOT monotone (jumps up and down), the
    p-adic/monotonicity angle (opening #4) dies as a cheap kill without needing a full proof
    attempt.
  - Parity/size pigeonhole: none obvious beyond what's already certified (Confined-GCD already
    gives the tightest known finite-alphabet reduction).

- Knowledge-base entries to use: none of `knowledge_base.md`'s generic entries were found to add
  a NEW analytic tool beyond what's already certified in this workspace's lemma stack (Free
  Facts, Bounded/Generalized Bounded Gap Lemmas, Finite Core Theorem, Generalized Bounded
  Witness Lemma, Confined-GCD, Cofinite Sufficiency) — I did not find a Dirichlet-density,
  sieve, or CRT-counting entry in knowledge_base.md that is a closer match than the crux-corpus
  hits below; recommend the outliner treat the crux corpus (not knowledge_base.md) as the
  primary source for this lens.

- Analogous past problems (cruxes):
  1. **aimo-0680** (IMO-SL 2015 N4, "prove f(n)-n eventually periodic," subtopics
     size-bounding-and-descent / divisibility-and-gcd) — closest genuine structural analog for
     the WHOLE FAH crux: its 3-part template (window-counting to find a syndetic "dense row" →
     bounded-integer pigeonhole to extract a fixed AP-step along an infinite subset → an EXACT
     divisibility-difference-vanishing argument to upgrade "holds along an infinite subset" to
     "holds identically") is precisely the missing ingredient per the workspace's own Lemma-I
     diagnosis (existential → universal promotion). Already flagged in round 8 (math-explorer
     memory rule #25) as promising but blocked on the missing global index-divisibility identity
     — my numeric-cheap-kill proposals above (Return-Time Boundedness, g_n monotonicity) are new,
     concrete, NOT yet run, and would settle whether a substitute identity/structure exists
     before investing in a full transplant attempt.
  2. **aimo-0477** (IMO-SL 2018 N4, "sum condition ⟹ eventually constant sequence," subtopics
     p-adic-valuation / divisibility-and-gcd) — its 2nd solution's p-adic valuation monotonicity
     argument (opening #4) is a genuinely different proof SHAPE (monotone-bounded-integer descent
     on v_p, not pigeonhole) from all 9 dead mechanisms; its 1st solution's divisor-chain
     `gcd(a_1,a_n) | gcd(a_1,a_{n+1})` monotonicity is the shape already flagged in round 7/9
     (math-explorer memory rules #23, #31) and already tried once (Step 8.9, dead by tautology).
     The 2nd solution's valuation-monotonicity has NOT been tried yet and is a distinct
     mechanism from the 1st solution's — worth flagging as a fresh sub-variant, not a repeat.
  3. **aimo-0134** (USAMO 2007, "digit-average sequence eventually constant," subtopic
     size-bounding-and-descent) — a clean, simple template for "nonincreasing integer-valued
     average forces eventual constancy, then constancy of the average forces constancy of the
     original sequence via a difference identity." Only loosely analogous (no gcd/prime structure)
     but useful as a template for opening #3's "integer-valued running quantity, monotone, hence
     eventually constant" shape if a suitable running quantity built from g_n's can be found.

- Prior progress: as recorded in `current.md` / round 9 rules — reduction chain (Finite Core
  Theorem → Generalized Bounded Witness Lemma → Cofinite Sufficiency Lemma → Confined-GCD Lemma)
  is fully certified and unconditional; sole open crux is Cofinite FAH (equivalently, the
  Successor Claim per the certified Successor-Transport Reduction Lemma). NINE mechanisms dead,
  all in the gcd-pigeonhole family. No analytic/counting mechanism has been attempted before
  this round per the round-9 Rules explicitly requesting one.

- Dead ends (do not retry): all 9 gcd-pigeonhole mechanisms listed in run_state.md round 9 Rules
  (Recruitment-Budget, Fixed-Witness Divisor-Chain, Two-Witness Intersection Uniqueness,
  scalar-well-ordering-lock-in, seed-coupling-induction, Blocking-Data Bridging, window-capacity
  counting bound as attempted in round 9 [note: this round's opening #2/#3 are NOT a repeat of
  that — round 9's window-capacity bound tried to bound the COUNT of a competing divisor class
  directly and stalled at "some class infinite, not provably only one"; openings #1-#3 here
  target a different object, either return-time boundedness or an exact AP-identity, neither
  tried in round 9]. Also do not re-propose bare density-1 claims (memory rule #24) — any
  analytic argument must produce a summable/telescoping or exact (not asymptotic-density) bound.

- **Cheap-kills actually run this round (new data, not proposals):** simulated the real greedy
  sequence for a_1=4807 to N=8000 terms (`python3 math.gcd` brute force, ~1.7s) and reconstructed
  the round-9 rogue pair at the pre-recruitment core S0={2,3,5,11,19,23} (Q={11,19,23} minus
  {13,17}): A'={3,5,19} (base type {19}), B'={2,11} (base type {11}), witnesses n_A=6, n_B=7,
  q*=17 (=min(F'∩F'')={13,17}∩{17}... matches round 9's exact numbers a_6=4845=3·5·17·19,
  a_7=4862=2·11·13·17).
  - **Opening #4 (raw g_n numeric monotonicity) is FALSE, confirmed by direct data — do not
    pursue as stated.** Tracked g_n := gcd(a_n, a_7) at all 12 A'-type occurrences up to n=7775:
    the sequence of g_n values is `17,17,17,17,221,17,17,17,17,17,17,17` — NOT numerically
    monotone (221=13·17 appears once, mid-sequence, then drops back to 17). So the naive "g_n is
    an eventually-monotone integer sequence" claim (the direct transplant of aimo-0477's 2nd
    solution) is refuted by this single data point; any p-adic/monotone-potential attempt must
    use a genuinely different potential than g_n itself (e.g. only track v_17(a_n), which in this
    data stays constant at 1 in every occurrence — a much weaker, already-known fact, since q*
    divides every occurrence with zero exceptions here).
  - **Opening #2 (Return-Time Boundedness) is SUPPORTED by this data point, not falsified —
    worth a real numerical sweep before building on it.** The 12 occurrence indices are
    561, 1114, 1668, 2223, 3335, 3892, 4445, 5002, 5557, 6667, 7223, 7775 — consecutive gaps are
    553, 554, 555, 1112(=2×556), 557, 553, 557, 555, 1110(=2×555), 556, 552: i.e. the gap is
    essentially CONSTANT at ≈555 (occasionally doubling, i.e. one A'-occurrence is "skipped" by
    the ambient dynamics, but the gap does not grow with n across the tested range n≤7775). This
    is a genuinely new, previously-unrecorded observation in this workspace (no prior round
    measured occurrence-index gaps for a rogue-pair type) and is consistent with — though far
    short of proving — the target Return-Time Boundedness Lemma (opening #2's prerequisite for
    an aimo-0680-style dense-row argument). It is also consistent with (and roughly the same
    order of magnitude as) the seed's own eventual period once found, which is expected since the
    problem's OWN conclusion is exactly this kind of periodicity — so this evidence is suggestive
    but not free of the risk of implicitly assuming what's being proved; flag this caveat to the
    outliner.
  - Also confirmed (0/12 exceptions): FAH itself holds with zero failures for this seed across
    the whole tested range, consistent with round 9's findings — not new evidence but a sanity
    check that the reconstruction is correct before trusting the two findings above.

- Small-case / intuition notes (all conjecture, not proof):
  - Round 9's 550+ seed sweep already gives very strong support for FAH itself; I did not re-run
    a fresh large sweep (would duplicate round 9's work) — instead I designed two NEW, currently
    unrun numerical cheap-kills (Return-Time Boundedness of a fixed extended-persistent type's
    occurrence gaps; monotonicity of the Confined-GCD sequence g_n along A'-type occurrences) that
    directly test the two structural prerequisites openings #1/#2 and #4 would need. Neither has
    been checked by any prior round — they are cheap (reuse existing simulation code, a_1=4807 /
    11305 seeds already have correctly-recruited cores computed) and should be run before
    committing a build slot to either analytic mechanism, since if either prerequisite fails
    numerically, that whole opening should be retired immediately rather than attempted formally.
  - Structural intuition: the greedy sequence's defining rule (smallest legal next integer) is a
    *local, existential* rule with no global algebraic identity (unlike aimo-0680's `n|f^n(m)-m`
    or aimo-0477's integer-sum condition) — this is plausibly WHY 9 pigeonhole mechanisms have
    failed to promote existential-to-universal: the tool that does this promotion in every crux
    hit found (aimo-0680, aimo-0477) is an exact global identity this problem structurally lacks.
    If the two cheap-kills above come back negative (unbounded return times / non-monotone g_n),
    this is fairly strong evidence that NO purely analytic/counting transplant from these cruxes
    will work either, and the crux may need a bespoke argument built from the greedy rule's own
    minimality (not yet mined analytically — e.g. "the greedy minimality forces q* into a_n
    because NOT having q* would make a smaller/legal alternative exist" — a minimality-based
    rather than counting-based mechanism, distinct from both the 9 dead pigeonhole mechanisms AND
    the 3 analytic openings above; flagged here as a possible 4th genuinely-different family for
    the outliner to weigh against, though I did not develop it further per my scouting-only
    mandate).
