## imo-2026-03 (lens: general upper-bound front / dualize lower-bound vertex machinery)

- Distinct openings:
  1. **Vertex-Minimum Theorem is ALREADY marking-agnostic — no dualization needed, just direct reuse.**
     Re-reading `lemmas/vertex-minimum-theorem.md` carefully: its statement and proof use *no*
     ladder-specific structure at all ("Fix any Liu Bang configuration... no assumption on shape").
     Its own certification note even says explicitly: "applies verbatim to the general upper-bound
     direction with an arbitrary Liu Bang marking." So for an arbitrary marking with `p1<T/2`,
     Xiang Yu's minimization of Phi over *all* his legal responses (any composition, any split) is
     *already proved* to be attained at a rank-tie/degenerate-cut vertex — a finite (if
     uncharacterized) search space, exactly like the lower-bound side. This closes the "does the
     machinery transfer" question outright: **yes**, trivially. The actual open problem was never
     "can we reuse the vertex theorem" — it's "characterize/bound the vertex value for an arbitrary
     (non-ladder) marking," which is a different, harder task than what round 9's outline implied.
  2. **`exchange-smoothing-vertex-maximization` is *also* already fully general (not ladder-specific)
     and is precisely the right tool for the "cut only p1, tail untouched" family in the upper-bound
     direction** — read `lemmas/exchange-smoothing-vertex-maximization.md`: it fixes an *arbitrary*
     reference set tau ("need not be ratio-2, the proof never uses that structure") and a mass `s`
     and part-budget `k`, and proves the maximizer of `E(F∪tau)` (⟺ minimizer of `A`, ⟺ minimizer of
     Phi) over ways to split mass `s` into `k` pieces each ≤ tau_1 is attained at a vertex of the
     restricted form: some fragments pinned to existing reference values `tau_l`, the rest sharing
     one common tied value. This is a *direct, literal, unconditional match* to what Theorems A–E in
     `lp-duality-certificate.md` have been hand-crafting ad hoc (Theorem A = all-pinned-to-tau case,
     Theorem C/C' = bisection = "one shared tied value with k=2, p=0" case, Theorem B/B_k = "one
     pinned fragment" case). **This lemma proves those are the *only* candidate vertex shapes for the
     "cut p1 alone" strategy family, for *any* marking** — turning "invent more ad hoc templates" into
     "search the now-finite, already-characterized vertex family directly." This is the strongest
     concrete opening this lens found: it is a genuine, already-certified, unused tool sitting in the
     lower-bound population that directly targets the exact gap (§5 of `lp-duality-certificate.md`).
  3. **A clean equivalent reformulation of the whole general upper bound via the already-general
     `leftover-formula`+`pair-cancellation-identity`** (both certified with zero ladder-specific
     content): `Phi=(T+v)/2` whenever the final multiset is `v` unpaired plus exact pairs. So
     `c(n)<=a_n` for a given marking is *equivalent* to: **Xiang Yu has a legal response with ≤n
     cuts producing a final multiset of `n` exact-value pairs plus one leftover `v<=T/D_n`
     (`D_n=2^{n+1}-1`)** — i.e. a bounded-leftover *matching/pairing* construction, not an
     inequality-proving induction at all. This reframes the whole upper-bound target as an
     existence/construction claim (find a good matching), which is a genuinely different kind of
     proof obligation than the recursive-bisection-template approach `lp-duality-certificate` has
     been running. See numeric evidence below — both on-file hard witnesses are solved *exactly* by
     matchings of this shape with `v=0` (perfect pairing), using far fewer than the full `n` cuts.
  4. **What the obstruction would look like if pursued.** The lower bound's actual *evaluation* tools
     that made vertex theory bite for the ladder (`half-window-vanishing-lemma`,
     `ratio-2-spacing-lemma`, `last-element-bound`) all crucially use the ladder's specific ratio
     identity `p_1=2p_2` (e.g. Half-Window Vanishing's whole proof is "`p_2` is exactly the midpoint
     of the window because `p_1=2p_2`"). None of these transfer to an arbitrary marking — this is the
     real, confirmed obstruction to a literal "dualize the whole lower-bound proof" plan: the
     *characterization/enumeration* machinery is ladder-specific even though the *reduction*
     machinery (vertex theorems, pair-cancellation, leftover-formula) is not. A future builder must
     supply a *new*, marking-agnostic evaluation argument for the vertex family identified by opening
     2/3, not try to reuse Half-Window Vanishing or Ratio-2 Spacing verbatim.

- Candidate technique(s): reuse `exchange-smoothing-vertex-maximization` (already certified, general)
  to enumerate the finite "pin-to-tail-value or shared-tie" candidate family for Xiang Yu's
  "cut-p1-only" strategy on an arbitrary marking with `p1<T/2`; separately, reframe the *whole*
  upper bound (not just cut-p1-only) as a bounded-leftover pairing/matching existence problem via
  `leftover-formula` + `pair-cancellation-identity` (opening 3), and attempt a direct greedy/
  Steinitz-style matching construction rather than another recursive bisection template.

- Cheap-kill candidates: none found that immediately kill the p1<T/2 regime; the pairing
  reformulation (opening 3) does give a cheap *necessary condition* check — count parity: total
  final fragment count is `m+ (\text{cuts used})`; achieving "n exact pairs + 1 leftover" needs an
  *odd* total fragment count, i.e. cuts used must have the same parity as `m-1=n` mod 2 when
  leftover count is exactly 1, or *even* total (0 leftover) otherwise — a cheap necessary-condition
  filter on which cut-counts can even reach `v=0`, worth checking before searching harder
  compositions, but not by itself a proof technique.

- Knowledge-base entries to use: none of `knowledge_base.md`'s generic entries are new here (per
  round 1's standing finding that this problem has no strong KB match); the relevant tools are all
  problem-specific certified lemmas listed above.

- Analogous past problems (cruxes): did not run a fresh corpus query this round — per the
  established round-1/round-4/round-6 findings (see Rules in `/tmp/memory/run_state.md`), generic
  pigeonhole/subset-sum/matching transplants from the corpus (`aimo-0718`-style) have twice been
  checked and refuted as *literal* transplants for this problem's specific multiset structure. If a
  future round pursues the "matching/pairing" reformulation (opening 3) as its own approach, it
  should query `combinatorics` / `extremal-principle` and `processes-and-algorithms` subtopics
  specifically for "greedy pairing with a bounded leftover" cruxes (not yet done this round — flagged
  as a concrete next step, not claimed as checked).

- Prior progress: (see `results/imo-2026-03/current.md`, `approaches/lp-duality-certificate.md`)
  `p1>=T/2` regime fully closed for `n<=3` via Theorem C′ + telescoping-threshold-identity; `n<=3`
  closed both regimes (imported `n2-upper-bound-lp-argument`). `p1<T/2` regime: Theorems D′/E give
  closed-form ceiling conditions that provably never certify the equal-pieces marking (general proof,
  `dprime-equal-pieces-insufficiency`) and fail both on-file witnesses' ceiling versions; both
  witnesses are resolved only by *exact* (non-ceiling) evaluation using Theorem B_k with a
  non-`k=2` peel target, i.e. ad hoc per-witness matching.

- Dead ends (do not retry): naive digit/carry mechanisms (`integer-lattice-reduction`), 2:1
  bijective pairing (`bijective-mersenne-pairing`), generic pigeonhole/subset-sum transplant of
  `aimo-0718` (refuted twice) — all pre-existing, not rediscovered this round. New this round: no
  new dead end found; opening 4 flags that literal reuse of `half-window-vanishing-lemma` /
  `ratio-2-spacing-lemma` / `last-element-bound` for arbitrary markings will fail immediately (their
  proofs are one line each of "$p_1=2p_2$" — do not attempt to import them verbatim; only the
  *reduction* lemmas (`vertex-minimum-theorem`, `exchange-smoothing-vertex-maximization`,
  `pair-cancellation-identity`, `leftover-formula`, `odd-run-reduction-lemma`) are marking-agnostic
  and safe to reuse.

- Small-case / intuition notes (all **conjecture**, numeric only, exact-`Fraction`/rational-grid
  random search, not proof):
  - At both on-file `n=3` hard witnesses, `(3/8,1/4,1/4,1/8)` and `(2/5,3/10,1/5,1/10)`, the
    numerically-located true optimal Xiang Yu strategy achieves the target *exactly* via a
    **perfect pairing** (`v=0`, `A=0`): `(3/8,1/4,1/4,1/8)` pairs as
    `{p2,p3}={1/4,1/4}` (0 cuts, pre-existing tie) + `{p1/2,p1/2}` (1 cut, self-tie) +
    `{p4/2,p4/2}` (1 cut, self-tie) — exactly matching the file's known Theorem-D′-exact
    resolution, using only **2** of the **3** available cuts.
    `(2/5,3/10,1/5,1/10)` pairs as `{p1-\text{fragment},p2}=\{3/10,3/10\}` (1 cut, pin-to-reference)
    + two copies of `{1/10,1/10}` from bisecting `p3` and matching `p4` (2 cuts) — again a perfect
    pairing, using all 3 cuts but landing exactly on `A=0`, well inside target.
  - A fresh, `n=4` (`m=5`) random marking with `p1<T/2` (`p=[37,22,18,14,9]/100`) was probed by
    random-grid search (rational-grid, 40000 trials): best found `Phi≈0.510` vs target `a_4T≈0.516`,
    using a composition with only **3** of the available **4** cuts (`(1,0,1,1,0)`) — consistent
    with (not proving) the same "near-perfect-pairing, budget-slack" pattern generalizing beyond
    `n=3`. Search was not refined to certify exact `v` value or the precise pairing structure at
    this instance (time-limited); this is weaker evidence than the two `n=3` cases and should be
    re-run with a proper exact-vertex solve (Gaussian elimination over tie-hyperplanes, as round 5
    did for the lower bound) if a future round adopts opening 3.
  - **Conjecture** (not verified beyond these 2–3 points): for every marking with `p1<T/2`, Xiang
    Yu's optimal response is a perfect-or-near-perfect pairing (`v` at or near `0`, well under the
    `T/D_n` budget), achievable with strictly fewer than the full `n`-cut budget — i.e. the
    matching-existence reformulation (opening 3) is not just *sufficient* but appears (numerically)
    to be *slack*, suggesting a construction proof may be easier to find than the tight recursive
    template chase the population has been running.
  - Script used (kept for reference, not committed): `/tmp/round-10/probe_upper.py`,
    `/tmp/round-10/probe_upper2.py`.
