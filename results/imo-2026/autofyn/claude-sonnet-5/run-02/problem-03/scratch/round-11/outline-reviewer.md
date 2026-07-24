## imo-2026-03 — Round 11 outline review

### greedy-halving-adversary: unified strong induction for Claim (B), ℓ(F)≤2

**Verdict: CHANGES REQUESTED** (sound strategy, build with the flagged gaps
tracked explicitly, not silently).

Checks performed:

- **Is this really "one whole attempt," not a fragment?** Yes. The outline's
  target `P(n)` is the full restricted-Claim-(B) statement at ℓ(F)≤1 (plus
  the ℓ(F)=2 extension), the same top-level object this approach has owned
  since round 8 — it is a genuine consolidation of three previously-separate
  propositions into one induction, not a slice of someone else's proof. No
  fragmentation concern.

- **Does P(n) really only need P(n-1)/P(n-2), and is the recursion
  non-circular?** I traced the two claimed reductions against the *existing*
  approach file (not just the outline's paraphrase):
  - Step 4/5's rescaling substitution (`Q=τ/r`, `w=w'/r`, `q_2=p_3/r`) is not
    a new claim — it is *already written out* in Proposition 25's own proof
    (`greedy-halving-adversary.md` lines 1465–1520), which explicitly
    identifies the tail `{p_2,...,p_{n+1}}/r` as exactly the `(n-1)`-ladder.
    Reusing it for the two remaining uncovered branches is legitimate reuse
    of a mechanism already proved, not an unverified hand-off.
  - Step 3's `v<s → P(n-2)` reduction is new content this round but its
    mechanism is precisely stated (only the "`v≥s`" step of the existing
    `A(F∪G')=p_2-v+A(R')` algebra needs replacing by the IH applied to `R'`
    directly) — a real mechanism, not a bare label.
  - Base case `n≤4`: confirmed directly against the file (grep hits at
    lines 24, 66, 1519, 1702, 2057, 2232) — Propositions 22/24 are already
    unconditional for `n≤4` because `(⋆_{n-2})` bottoms out at `(⋆_0)` or
    `(⋆_1)` or `(⋆_2)`, all already fully closed. The two-depth recursion
    (P(n) needs P(n-1) *and* P(n-2)) does bottom out cleanly — no skipped or
    doubled level, since the outline's own base case matches exactly what
    the certified propositions already establish unconditionally.
  - The outline itself flags (correctly) that the *exact* bookkeeping of
    which depth is needed where should be nailed down precisely by the
    builder, not just asserted — this is the right level of caution, not an
    admission of a hidden flaw.

- **Does the window-difference decomposition for ℓ(F)=2 silently reintroduce
  the round-10 "illegal merge" failure?** No. The round-10 dead end was a
  literal "merge two residuals into one fragment of size `v_1-v_2`" — an
  operation on the *multiset itself* that is not mass-preserving (not a
  legal move). This round's window-difference idea never merges anything:
  it only splits the *integral* `∫_{v_2}^{v_1} v_{G'}` linearly into
  `∫_0^{v_1} - ∫_0^{v_2}`, both against the *same*, unmodified `G'`. Linearity
  of integration is unconditionally true; I don't need to re-derive it. The
  real open risk — which the outline itself explicitly flags as unverified
  (the mixed-regime case `v_1≥p_2>v_2`, where the two single-threshold pieces
  land in different ladder regimes and so may not literally be the exact
  closed forms Prop 20/24/25 output) — is the correct thing to flag, and is
  not yet checked. This is a real gap the builder must close, not a fatal
  flaw in the mechanism.

- **Small-case sanity.** I independently re-ran a check consistent with
  `/tmp/round-11/probe.py`'s numeric corroboration (20,000-trial exact
  search, `v<s` branch, `n=3..6`, zero violations, shrinking-but-positive
  margin) — consistent with the induction target, not a counterexample.

- **Does it avoid a recorded dead end?** Yes — explicitly avoids the merge
  move; correctly does not resurrect bisection-only/binary-carry/ℓ(S)-
  induction/claiming-order-invariant/iterated-greedy-peel.

**Open items to hold the builder to** (per the outline's own honest gaps
list, which I confirm are real and not yet closed): (1) mixed-regime
sub-case of ℓ(F)=2's window split; (2) exact P(n-1)/P(n-2) bookkeeping,
proved not asserted; (3) ℓ(F)≥3 is explicitly out of scope this round — the
outline is right to flag this rather than silently drop it; a future round
must decide whether the window-decomposition generalizes to k/2 windows or
needs new machinery.

### lp-duality-certificate: pin-set fix + structural redirection to marking-agnostic vertex-minimum-theorem

**Verdict: CHANGES REQUESTED** (both sub-tasks are sound; the second is
correctly scoped as opening a hard new front, not closing it).

Checks performed:

- **Pin-set fix — is "adding 0 is safe" actually true?** Verified two ways:
  (a) the existing proof of Lemma A.1/A.2 already uses the reference set
  `{0,τ_1,...,τ_r}` internally (per round 10's finding, re-confirmed by the
  explorer's citation of specific line numbers in the approach file) — so
  this is a restatement to match an already-correct proof, not new
  mathematics; (b) I independently verified the "0-pinned coordinate is
  inert to Φ" claim with my own fresh script (2000 random-multiset trials,
  exact `Fraction`, appending a literal 0 element and recomputing the
  odd-rank sum) — zero mismatches. The mechanism (a zero element is always
  last in sorted order, so it can never sit "above" — i.e. at a smaller
  rank than — any positive element, hence cannot change any positive
  element's rank parity) is correct and general, not merely spot-checked.
  This sub-task is low-risk as claimed.

- **"Cut-p1-only is provably too narrow" — checked against the cited
  witnesses.** Confirmed directly: Theorem D′'s resolution of
  `(3/8,1/4,1/4,1/8)` bisects `p_1` **and** `p_m` simultaneously; Theorem
  B_4's resolution of `(2/5,3/10,1/5,1/10)` peels `p_1` against `p_4` and
  then bisects `p_3` — neither strategy is expressible as "cut `p_1` only."
  This is a fact already on file (not a fresh conjecture), so citing it as
  proof (not conjecture) that the narrow family is insufficient is correct
  usage per the file contract's "prove, don't conjecture" rule — the
  outline is careful to phrase this as "the narrow family cannot in general
  close `p_1<T/2`," not "Route A is worthless" (its pin-set fix is still
  useful for a possible sufficient sub-condition).

- **Structural redirection to the general vertex-minimum-theorem — is this
  the right technique, and is it honestly scoped?** `vertex-minimum-theorem`
  is already certified and marking-agnostic (confirmed against the lemma
  file and prior rounds' usage), so applying it to arbitrary compositions
  requires no new proof for that step — legitimate reuse. The outline
  correctly identifies that *this is the original min-form* of the theorem
  (Xiang Yu is minimizing Φ here), so no dualization/MAX-reuse caveat
  applies — unlike the lower-bound side's reuse, which the outline
  explicitly and correctly distinguishes (good adherence to memory rule 6).
  The outline is honest that step 6 (evaluating the resulting vertex family
  for an *arbitrary*, non-ladder tail) is genuinely open — Ratio-2 Spacing
  and Last-Element Bound are confirmed (per round 10/memory rule 9) not to
  transfer, and no replacement evaluation lemma exists yet. This is
  correctly flagged as "genuinely open, not unattempted busywork," which
  matches the actual state of the project — no overclaim.

**Open items to hold the builder to**: step 6 (arbitrary-tail evaluation) is
the crux and is unproved — the builder should not present partial numeric
corroboration as closure; step 2's "downstream unaffected" claim should be
checked against A.2/A.3's literal statements throughout, not spot-checked
once (per memory rule 3's caution about resubmitted-approach claims).

### Diversity check

The two approaches remain on genuinely different halves of the theorem
(Claim B / lower bound vs. the general upper bound) via different
techniques (induction consolidation vs. LP-vertex redirection) — no
same-wall plateau this round. No new slug was opened, and none was needed:
neither front shows a 3+-round same-framing stall: greedy-halving-adversary
is closing new sub-branches each round (25 → 24 → this round's
consolidation), and lp-duality-certificate is pivoting away from a
confirmed-insufficient narrow family toward a structurally new redirection,
not repeating Route B's dead mechanism.

### Ranking

Registered: no new slugs (both slugs already in the population from prior
rounds; no branching requested this round). Ranking updated via
`update_ranking` with comparisons anchored to last-recorded outcomes:
`rank-pigeonhole-budget` (verified-milestone, full closure of Claim A) beats
`greedy-halving-adversary` (still partial); `greedy-halving-adversary` and
`lp-duality-certificate` drawn (both "advanced" last round with comparably
solid, well-scoped continuing plans this round); both beat their
dead-end/long-stalled neighbors (`claiming-order-invariant`,
`integer-lattice-reduction`, `bijective-mersenne-pairing`,
`self-similar-bracketing`) which clears the stale flags on the two build
candidates.

build set: greedy-halving-adversary, lp-duality-certificate
