## imo-2026-06 (lens: global/joint potential over the ENTIRE system of minimal supports)

- Distinct openings (all genuinely "whole-system" rather than single-G/pair):

  1. **Sieve-weight potential Ψ_n = Σ_{G∈𝓐_n} 1/∏G** (or the un-normalized Σ_{G∈𝓐_n} μ-signed
     inclusion-exclusion density of "c misses G"). Idea: track this aggregate quantity across ALL
     currently-known minimal supports simultaneously as n→∞, hoping for a monovariant (monotone
     decrease, or a convergent-series obstruction) that forces |𝓐_∞| finite without ever isolating
     one G. **On inspection this is NOT a new lever**: A^c = ∪_{G∈𝓐_∞} B_G with B_G = {c: gcd(c,∏G)=1},
     density(B_G) = ∏_{p∈G}(1-1/p). For |G|=1 with a single LARGE prime q, density(B_G)=1-1/q ≈ 1
     — i.e. the aggregate sieve bound is dominated by exactly the same obstruction family {p*,q_k}
     that already certifies density(A) can stay at a positive limit with Π infinite
     (`monovariants-and-obstruction.md`). Any Σ1/∏G-type convergence argument collapses onto the
     forbidden density-of-A lever (run_state Rule: "NEVER... Sigma-density-of-A... do not resubmit
     in disguised form"). **Flag: secretly forbidden, do not seed.**

  2. **Aggregate double-count of (support, private-witness) incidences across the WHOLE family**:
     count pairs (G,p) with p∈G ranging over ALL of 𝓐_∞ simultaneously, using E3 to attach to each
     such pair a witness distance |t_G − t_{G_p}| ≥ p, and try to bound the TOTAL incidence count
     (not any single p) via a global resource constraint (e.g. terms up to some N can only support
     O(N) such witness pairs, each large p "consumes" Ω(p) of index-space). On inspection this
     reduces immediately to summing the SAME per-pair spread quantity |t−t'| that R5's
     `realizer-index-joint-double-count` already proved is logically EQUIVALENT to the magnitude
     bound q≤C(a₁) via the JSC identity t−t'=q·(A−B), A≠B (`two-anchor-scaffold.md`). Aggregating
     JSC over many pairs does not add leverage — each individual term in the sum is already known to
     be forced (not bounded) by the same illusory lever. **Flag: secretly forbidden (JSC-equivalent
     in disguise), do not seed as an independent pole.**

  3. **Pure combinatorial (arithmetic-free) route via extremal set theory on the whole family**:
     𝓐_∞ is a pairwise-intersecting family of FINITE sets (certified E2⇒: every G is a ⊆-minimal
     transversal, hence meets every other member — a genuine "intersecting family" in the classical
     sense). This IS a legitimately different global object to interrogate: classical extremal
     results (Deza–Frankl sunflower theorem, Hilton–Milner, "star" structure theorems for
     intersecting families) say an intersecting family of k-sets that is NOT a star (all through one
     common point) has size bounded by a function of k. **But this cannot close the crux alone**:
     it needs |G|≤k as a HYPOTHESIS (that is E4/E5 itself, still open), and even granting bounded
     |G|, an infinite intersecting family CAN be an infinite star (all G containing a common prime
     p*) — which is EXACTLY the certified anchor-partition structure (`anchor-partition.md`,
     Lemma A) already explored and proved to collapse (R4 Collapse theorem) when the closing move is
     "realize a common sub-support." So pure set-theory over the whole family reproduces the anchor
     partition, not a bypass of it — it is the SAME wall restated abstractly. **Flag: rediscovers
     the anchor-partition pole verbatim; do not re-seed as new.**

  4. **A genuinely under-explored joint quantity: total "excess growth" / cumulative gap-deficit
     Φ_N = Σ_{n≤N} (a_{n+1}−a_n − 1) = a_{N+1} − a_1 − N**, i.e. the aggregate slack between the
     actual sequence and the "no-gaps" baseline a_1, a_1+1, a_1+2, .... By L2, each summand is in
     [0, M−1] (M=rad(a_1) fixed, independent of Π!). This is a genuinely GLOBAL, already-bounded-rate
     quantity — but note it is a property of A alone (equivalent to density(A) via Φ_N/N →
     M·(1−density(A))-ish), so any attempt to force Φ_N/N → 0 (⇒ density→1 ⇒ finite Π, heuristically)
     again routes through density(A), which is certified NOT forced to converge to 1 (obstruction
     family gives density→1/p*<1 with Π infinite). **Flag: same density wall, not independent.**

  5. **Only partially explored, and NOT yet proven forbidden: a "total capacity" argument bounding
     the RATE of NEW-ANCHOR creation jointly across ALL fibers of the anchor partition** (Lemma A),
     rather than analyzing one fiber's internal structure. Concretely: P=primes(a₁) is FIXED and
     finite from the start (this is data given at n=1, not something that grows). Lemma A gives a
     map α:𝓐_∞→P. If some fiber α^{-1}(p*) is infinite, R4's Collapse theorem already shows the
     "force a common sub-support" route collapses to E5 — but that theorem only rules out ONE
     specific closing mechanism (dominating sub-support realization) for ONE fiber. It does NOT rule
     out a genuinely joint argument using ALL |P| fibers' large-prime recruitments SIMULTANEOUSLY,
     e.g.: every large prime q recruited into ANY fiber must (by Anchor L1) itself divide some term
     a_i whose OTHER prime factors already lie in P∪(primes recruited so far) — i.e. recruitment is
     a sequential process consuming a shared, GLOBALLY finite "vocabulary growth" resource across all
     fibers at once, not per-fiber. Whether this yields an actual bound is UNCLEAR — I could not find
     a concrete inequality in the time available that isn't itself either (a) a per-G product bound
     (forbidden) or (b) a density statement (forbidden). This is the most promising genuinely
     unexplored corner of the "joint potential" lens, but it is UNPROVEN TO EXIST as a working lever,
     not just unproven as a theorem — recommend the outliner treat this as "worth one more probe" but
     be ready to cut fast if the first concrete inequality attempted is a disguised ∏G/|t−t'| bound.

- Candidate technique(s): sieve/inclusion-exclusion density (opening 1, dead), aggregate
  double-counting of witness pairs (opening 2, dead), extremal set theory / sunflower-vs-star
  dichotomy for intersecting families (opening 3, rediscovers anchor-partition), cumulative
  gap-deficit accounting (opening 4, dead — same as density), joint multi-fiber recruitment-rate
  accounting (opening 5, open but unproven to have any content).

- Cheap-kill candidates: before any builder invests in opening 5, have them write the FIRST concrete
  inequality it would need and check by hand whether that inequality, once stated, reduces to
  "∏G ≤ f(a₁)" or "|t−t'| ≤ f(a₁)" for some single G/pair — if so it is the forbidden lever in
  disguise and should be cut immediately (this single check would have caught openings 1 and 2
  before any real work).

- Knowledge-base entries to use: none of `knowledge_base.md`'s generic entries were found to add new
  leverage beyond what's already certified in this problem's own lemma files (the problem's crux is
  now entirely bespoke arithmetic, not a generic KB technique match) — I did not find a KB entry
  matching "global sieve on an intersecting family of prime-supports."

- Analogous past problems (cruxes): searched the corpus (`double-counting`,
  `invariants-and-monovariants`, `pigeonhole` subtopics in number_theory/combinatorics) for
  "intersecting family," "sieve," "sunflower," "global invariant," "aggregate." Found no genuine
  analog. `aimo-0966` (double-counting, inclusion-exclusion sieve over convex-polygon markers) is
  structurally a sieve but on a completely unrelated finite combinatorial object (convex polygons on
  a point set), not a growth/gcd process — **not analogous, do not transplant**. The previously-flagged
  `aimo-0678` (IMO 2015 SL N4, monovariant/two-stage freeze) and `aimo-0447` (interval-hits-prime
  product bound) remain the closest matches from earlier rounds, but both are already certified
  exhausted (value-stream RETHINK R3; realizer-value-pincer lower jaw only, R4) and are per-support/
  per-pair in nature, not joint/global — they belong to the OTHER (forbidden) lens, not this one.
  **Verdict: no new corpus transplant found for the joint-potential lens.**

- Prior progress: (from `results/imo-2026-06/current.md`) whole theorem certified-reduced to Crux
  (Finite Alphabet) ⟺ E4 (sup|G|<∞) ⟺ E5″ (∏(G∖{p_max})<a₁ for ∏G≥a₁) ⟺ every anchor fiber finite
  (Lemma A). No-transient (a_{n+1}=s(a_n) ∀n≥1) fully proved. E1/E2/E3 fully proved. Realizer pincer
  R1/R2/Prop12.A fully closes the ∏G<a₁ subclass. TAS (two-anchor scaffold) certified.

- Dead ends (do not retry): all confirmed from run_state Rules — M-threshold confinement (a₁=375
  counterexample), A_n-only monovariants (obstruction family), value-stream automaton (proven
  equivalent to crux), sub-support-realization / anchor-fiber peeling (R4 Collapse theorem — proven
  to collapse to E5 even when attempted per-fiber), joint-spread |t−t'| bound (R5 JSC theorem — proven
  equivalent to the magnitude bound). This round's openings 1, 2, 4 are NEW instances of these SAME
  dead ends (density-of-A and JSC-equivalent, respectively) wearing a "global" costume — I recommend
  the outliner NOT seed them, and record this explicitly so future rounds don't rediscover them again.
  Opening 3 (intersecting-family extremal structure) is a new-looking framing that, on inspection,
  is EXACTLY the anchor-partition pole (R4 RETHINK) restated in classical extremal-set-theory
  language — also should not be re-seeded as if new.

- Small-case / intuition notes (conjectural, not proven): the certified obstruction family {p*,q_k}
  (an infinite intersecting family that is a "star" through p*, with each q_k appearing in exactly
  one G_k besides p*) is the ONLY known example structure that keeps every global A_n-statistic
  (density, gap, sieve weight) from detecting infiniteness. This strongly suggests (conjecture) that
  ANY successful global/joint potential must be sensitive to something the star family lacks —
  candidates: (a) REALIZABILITY of the q_k's own witness supports as actual greedy-selected VALUES
  (not just abstract sets) — i.e. the argument must use E1 "every element of A is eventually a term"
  together with growth (L2, a_n=Θ(n)) in a way that forces a genuine ARITHMETIC collision the star
  family's abstract construction doesn't have to honor; or (b) the fact that in the star family
  q_k→∞ strictly, so if the argument can show the RATE at which q_k must grow (via arithmetic
  necessity, not just set structure) is too slow to keep up with term-index growth, that's a route —
  but this is again a per-element (q_k) growth-rate bound, i.e. it risks re-deriving the forbidden
  q≤a₁/formation-window lever unless phrased as a genuinely aggregate rate. I could not find a
  concrete aggregate rate inequality in the time budget; flagging as the single open thread worth one
  more careful pass, with the explicit warning above (cheap-kill check) attached.
