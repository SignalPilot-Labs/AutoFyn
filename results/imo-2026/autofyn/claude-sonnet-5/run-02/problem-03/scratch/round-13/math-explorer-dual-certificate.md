## imo-2026-03

- **Distinct openings surfaced (dual-certificate lens):**
  1. **Per-cell LP duality is already fully extracted — no new content there.**
     For a *fixed* rank/order pattern (a fixed cell of the hyperplane
     arrangement that determines which fragment sits at which sorted
     position), the problem "maximize/minimize a linear functional of the
     fragment coordinates subject to `sum_j f_{i,j}=p_i, f_{i,j}>=0`" is a
     genuine LP whose dual is a single scalar per block: `y_i >= c_j` for
     every coordinate `j` in block `i`, with complementary slackness forcing
     every `j` with `f_{i,j}>0` to sit at `c_j=y_i` (the max), and every
     `f_{i,j}=0` at `c_j<y_i`. But this is *exactly* what the already-certified
     `simplex-exchange-smoothing-vertex-maximization` /
     `per-piece-vertex-decomposition-theorem` prove directly (pinned-to-0 or
     tied-to-a-reference-value vertex structure) via an exchange/contradiction
     argument. I confirmed by hand that writing out the LP dual for a toy
     2-fragment block reproduces literally the same pin/tie conditions the
     exchange argument already derives — so a literal LP-dual write-up in
     this framing is a *relabeling*, not new leverage. This matches the
     approach file's own round-11/12 finding that the "finite vertex family"
     question is closed; only its *evaluation* is open.
  2. **The real obstruction is that the objective's own linear functional `c`
     (the +1/-1 sign pattern of "odd rank" vs "even rank") is not fixed in
     advance — it is a function of the point's own sorted order.** So the
     true optimization is a union of exponentially-many (in `n`) LP cells,
     not one LP. A genuine Positivstellensatz/dual certificate would need
     a *single* low-degree nonnegative combination of the constraints
     (`f_{i,j}>=0`, `sum f_{i,j}=p_i`, and the *order* inequalities
     `f_{i,j} <= or >= (\text{some reference value})` that define each cell)
     that is valid *simultaneously across all cells* — i.e. a certificate
     whose degree/complexity does not grow with the number of cells. This
     is the concrete "what would it look like" answer: not a single dual
     vector but a *finite template family* (in the spirit of the file's own
     Theorems A–D, `iterated-greedy-peel-identity`, etc.) each with its own
     small dual certificate, plus a proof the family's *pointwise minimum*
     dominates every cell — which is precisely restating the file's already
     -identified Open Gap 1 ("prove `min(Phi_A,...,Phi_D) <= a_n T` for
     every marking") in dual language, not a new route around it.
  3. **A genuinely different angle worth flagging (not yet tried under this
     name): a "potential function" / amortized certificate**, i.e. instead
     of certifying each vertex directly, find a scalar potential `Psi(marking)`
     such that (a) `Psi` is provably `>= a_n T` (or `<= a_n T`, matching
     whichever direction) at the *specific* recursive reductions Theorems
     C′/B_k/D′ produce, and (b) `Psi` telescopes exactly the way the
     Telescoping Threshold identity (`a_{n-1} = a_n/(2(1-a_n))`, already
     certified) does. This is essentially asking for the *exact* (not
     ceiling) recursive value in closed form — which the file's Open Gap 5/6
     already identify as circular past `n<=2`. I do not see a way past this
     circularity that isn't already on record.

- **Candidate technique(s):** none beyond what's already deployed. Classical
  LP duality (Farkas/complementary slackness) is provably equivalent in
  power, on this problem, to the already-certified exchange-smoothing vertex
  argument — it does not add expressiveness because the "constraint matrix"
  is self-referential (order-dependent). A genuine Positivstellensatz-style
  certificate is conceivable in principle but its complexity would need to
  be uniform in `n`, and no such uniform low-degree family was found or
  suggested by the corpus.

- **Cheap-kill candidates:** none new found. (One negative structural
  observation, not a kill of the whole approach: per-cell LP duality
  trivially reproduces the pin/tie vertex structure — confirmed by direct
  hand derivation on a 2-coordinate block — so any future round should NOT
  spend time "re-deriving the vertex theorem via LP duality," since it is
  provably the same content in different notation. This should save a round
  of wasted effort.)

- **Knowledge-base entries to use:** `knowledge_base.md` has no LP-duality /
  Positivstellensatz / dual-certificate entry (grepped for
  duality/dual/positivstellensatz/farkas/LP — only unrelated hits, e.g. an
  induction-duality remark and an LDS/LIS duality remark, neither applicable).
  The relevant *problem-specific* certified lemmas already in
  `results/imo-2026-03/lemmas/` remain the right toolkit:
  `per-piece-vertex-decomposition-theorem`, `simplex-exchange-smoothing-
  vertex-maximization` (corrected pin set `{0,tau_1,...,tau_r}`),
  `zero-pin-harmlessness-lemma`, `iterated-greedy-peel-identity`,
  `equal-pieces-closure`, `spare-cut-bisection-corollary`, and the exact
  identities `bisect-top-identity` / `bisect-top-recursive-identity` /
  `generalized-peel-identity` / `bisect-top-bottom-recursive-identity` /
  `telescoping-threshold-identity` (the last is the one piece of genuine
  algebraic "certificate" structure on file: it is the exact zero-slack
  threshold match that would need to be reproduced, exactly, at every
  vertex/cell for a real certificate to close the gap).

- **Analogous past problems (cruxes):** I filtered `games-and-strategy`,
  `extremal-principle`, `linear-algebra-method`, `inequalities-SOS-and-
  convexity` for anything mentioning duality/vertex/certificate/weight, and
  separately scanned `games-and-strategy` entries whose problem text
  involves cutting/splitting/pieces. **Nothing genuinely new was found:**
  - `aimo-0117` ("assign played values as a two-sided geometric/dyadic
    sequence so the largest strictly exceeds the sum of the rest") is the
    *same* crux this project already tried and rigorously ruled out as
    inapplicable in round 4 (`claiming-order-invariant`, RETHINK verdict:
    no multi-round structure for a defer-commitment invariant to exploit).
    Do not re-attempt.
  - `aimo-0560` ("replace the adversary with a strictly stronger surrogate
    whose reply is pointwise at least as damaging") is conceptually the
    *same move* as this file's own Theorems A–D (explicit legal strategies
    whose value is computed exactly and shown `<=` some bound) — not a new
    mechanism, just the same "surrogate strategy" idea already deployed four
    times over on file.
  - `aimo-0146` ("maximize a fixed weighted sum of a sorted nonnegative
    sequence by exchange-smoothing weight toward the higher-coefficient
    slot") is the generic exchange-smoothing template already imported and
    corrected as `simplex-exchange-smoothing-vertex-maximization`/
    `exchange-smoothing-vertex-maximization`. No further content to extract.
  - No crux in the corpus uses a genuine LP-dual/Positivstellensatz
    certificate for a combinatorial-game value bound of this "min over one
    player's continuum response, arbitrary opponent configuration" shape;
    the corpus's closest matches (`aimo-0403`'s "intersect reachable-region
    constraints from independent relabelings") are geometric/collision
    arguments, not applicable here. **Verdict: no genuinely analogous crux
    for the dual-certificate mechanism specifically.**

- **Prior progress:** (see `results/imo-2026-03/current.md`,
  `approaches/lp-duality-certificate.md`) — Claim (A) (equal-cuts-on-`p_1`,
  full budget) is fully closed for all `n`. The lower bound (Claim B) is
  closed for `l(F)<=2` under specific sub-cases. The upper bound is closed
  for `p_1>=T/2` at `n<=3`, plus four exact identities (Theorems A–D) valid
  for every `n`/marking, plus round 12's `equal-pieces-closure` and
  `spare-cut-bisection-corollary` closing the "has spare cut budget" and
  "exactly-equal marking" cases unconditionally. The open residual —
  confirmed generic (round 12, ~100% of markings with incommensurate
  denominators) — is exactly the full-budget, zero-mid-process-tie case,
  where I confirmed (small experiment below) that even the *restricted*
  "cut `p_1` only" vertex family (Theorems A/B/C alone) is insufficient at
  generic markings, matching the file's own findings.

- **Dead ends (do not retry):** naive greedy-peel-ties (`iterated-greedy-
  peel-identity` with "always match top two", refuted: ~48–100% failure
  rate depending on sampling, exact `n=4` equal-pieces witness `3/5 >
  16/31`); bisect-largest-cascade (round 12, refuted by exact witness,
  `n=2`, `(177, 6/5, 62/123)`: overshoots target by `~31`); literal LP-dual
  re-derivation of the vertex theorem (my own check this round — not a
  file entry, but should be recorded: it reproduces existing content, adds
  nothing); `aimo-0117`-style defer-commitment invariant (round 4 RETHINK,
  confirmed still correctly dead this round — no multi-round structure
  exists in the one-shot marking stage for it to act on).

- **Small-case / intuition notes (conjecture, not proof):** I ran a fresh
  2000-trial exact-`Fraction` check (`/tmp/dual_cert_explore.py`) at `n=2`
  restricting to the "cut `p_1` only" pinned/tied vertex family (Theorems
  A/B/C's finite vertex set): it is **not** sufficient in general — e.g. at
  `(p1,p2,p3)=(43,43,22)`, the best value in that restricted family is
  `64.5`, while the true target `4/7*T = 432/7 ≈ 61.7`, a real shortfall of
  `~2.8`. This is *consistent with* (not new beyond) the file's own
  round-8/9 finding that "cut `p_1` only" is insufficient in general and
  that tail-touching strategies (Theorem D, bisect-top-and-bottom, or a
  fully joint per-piece vertex) are required — it independently confirms
  that direction is real and not an artifact of one script. It also
  reinforces the report's main conclusion: a per-cell dual certificate on
  the *restricted* family cannot succeed (since the family itself is
  provably insufficient), so any certificate attempt must operate on the
  *full* joint per-piece vertex family (`per-piece-vertex-decomposition-
  theorem`), which is exactly where the self-referential-ordering
  obstruction above bites hardest (many more cells, since every piece can
  independently cross every reference value).

**Bottom line for the outliner:** the "construct an explicit dual
certificate" framing, taken literally (classical LP duality per fixed
order-cell), is not a new attack — it is provably equivalent in content to
the already-certified vertex/exchange machinery on file, and the crux
corpus offers no genuinely different certificate mechanism for this shape
of problem. If this front is to make progress, the productive target is
NOT "write down multipliers" but "prove a single template-strategy family's
pointwise minimum dominates `a_n T` across all cells" — i.e. Open Gap 1 in
`lp-duality-certificate.md`, already correctly identified as the hard
residual — or find a genuinely different (non-LP, e.g. potential/
amortized or probabilistic) argument that sidesteps the cell-explosion
issue entirely, since no evidence was found this round that a bounded-
degree, cell-count-independent certificate exists.
