## imo-2026-03

- **Distinct openings surfaced (and why each collapses or not):**
  1. **"Explicit claiming-phase strategy" (checked, PROVABLY NOT a bypass).** By the
     certified `endgame-greedy` lemma, once the final multiset `Q` is fixed (all cuts
     happen *before* claiming begins — Liu Bang marks, Xiang Yu marks, cut, THEN
     alternate), the claiming game has a *unique* deterministic value: greedy is optimal,
     and Liu Bang's guaranteed take is `Odd(Q) = (Σ(Q)+f(Q))/2`. There is **no residual
     strategic freedom** in the claiming phase to exploit — "explicit strategy" there just
     *is* "take the current max," which is already proven optimal. So a claiming-phase
     strategy argument cannot be a genuinely different target from `f(Q) ≥ 1`; it is the
     *same* statement by an already-certified equivalence (`layer-cake-alt-sum.md` +
     `endgame-greedy.md`). This closes off the most literal reading of the assigned lens.
  2. **"Explicit marking strategy for Liu Bang's own n points" (checked — already found,
     dormant, same wall).** `results/imo-2026-03/approaches/game-value-recursion.md`
     already IS this framing: it reformulates the whole LB lower bound as the pure
     combinatorial-game guarantee **(LB-claim)**: *on any ≤n-cut refinement `Q` of
     `W_n={2^0,...,2^n}`, Liu Bang's dyadic marking guarantees he claims ≥ `2^n`*, i.e.
     `f(Q) ≥ 1`. It proves this in full for Case A (top piece left uncut, via the dyadic
     domination chain `2^k > 2^{k-1}+...+2^0`) and reduces the rest to a **budget-non-
     fungibility (BNF)** sub-claim: however Xiang Yu splits its ≤n cuts between the top
     piece (turning `2^n` into `j+1` fragments `T`) and the remainder `R=W_{n-1}`
     (`n-j` cuts, giving `R'`), still `f(T ⊔ R') ≥ 1`. **This is definitionally identical
     to Gap A + Gap B / the "tied non-degenerate vertex" residual** — not a different
     mathematical object, just reached by a different derivation (peel-identity + domination
     instead of Φ-max + graph theory). Confirmed by re-reading the file: it says so
     explicitly ("same crux (GAP-L Case 2) as the other approaches, reached from the
     claiming-game side").
  3. **Genuinely open sub-idea (not yet tried): strategy-stealing / involution pairing
     directly on Xiang Yu's n cuts vs Liu Bang's n marks.** The crux corpus's
     `games-and-strategy` entries (`aimo-0225` strategy-stealing symmetry, `aimo-0596`/
     `aimo-0115`/`aimo-0854` pairing/mirroring with a floating unpaired element) suggest a
     template: pin down the worst Xiang Yu response by an involution argument (reach a
     "canonical" adversary line and argue any deviation could have been "stolen") rather
     than by Φ-maximality. I did **not** find a way to instantiate this for BNF within
     scouting time — the obstruction is that Xiang Yu's cuts on `T` (top fragment) and
     `R'` (remainder) are NOT symmetric to Liu Bang's original dyadic marks (different
     multiplicities, different scales), so there is no obvious involution on the cut set
     to steal against. Flagging as an unexplored idea, not a result.

- **Candidate technique(s):** None beyond what's already certified. The claiming phase is
  fully pinned by `endgame-greedy` (dead end for new technique). The marking-strategy
  framing (`game-value-recursion`) is sound scaffolding (LB-claim reformulation, Lemma R0,
  Theorem LB-A) but its open gap (BNF) IS Gap A/Gap B/Case B restated — not a new target.

- **Cheap-kill candidates:** ran a 200k-trial random-refinement search (Python, exact
  float, `n=2,3,4`) directly on **BNF's own formulation** (random ≤n-cut refinements of
  `W_n`, minimizing `f`). Result: `min f ≈ 1` confirmed for all three `n` (conjecture, not
  proof), consistent with all prior numerics. Notably the argmin found at `n=2` is
  `{2.615,2,1.180,1,0.205}` — a configuration where **both** of Xiang Yu's cuts landed
  inside the top piece `4` (splitting it 3 ways: `2.615+1.180+0.205=4`) while `2` and `1`
  are left whole — i.e. an extremal case with `j=2` (all cuts on top) rather than the pure
  bisection cascade. This is a genuine "Case B, `j=n`" configuration achieving the floor,
  confirming BNF's hardest case is not confined to the bisection-cascade line (matches the
  round-3 "flat region" finding) — no new cheap kill beyond what's already known, but
  useful concrete confirmation the residual is not an isolated boundary case.

- **Knowledge-base entries to use:** none new beyond what's cited (`endgame-greedy`,
  `layer-cake-alt-sum` already certified and used by this framing). `knowledge_base.md`'s
  "Invariants & monovariants" and general game-theory sections were checked; nothing
  specific to alternating-claim/dyadic-domination games beyond what's already applied
  (`aimo-0117`'s dyadic-domination crux, already imported round 2).

- **Analogous past problems (cruxes):** searched `games-and-strategy` (40 entries,
  combinatorics + number_theory). Best candidates for the unexplored strategy-stealing
  idea (not yet shown to apply, offered as a lead only):
  - `aimo-0225` — "strategy-stealing symmetry: reach a symmetric position, argue any
    winning reply from it could have been played directly from the original" — the
    template for idea 3 above, but no symmetric position is evident in BNF's `T ⊔ R'`
    split (different scales, no obvious involution).
  - `aimo-0596` — "partner-mirroring with a single unpaired 'floating' card, hand it off
    when the opponent takes the floater" — structurally close to Liu Bang's odd-mover
    edge (`Odd(Q)` has one more element than `Even(Q)` when `|Q|` is odd) but the
    corpus problem's mechanics (misère card game) are too different to transfer directly;
    flagged as "resembles in spirit, not analogous in structure."
  - `aimo-0117` (already imported, round 2) — dyadic domination assignment — this is the
    ONE genuinely analogous crux and it is already fully absorbed into the certified
    domination invariant used by both Case A here and the round-1 Case 1.
  No other entry in the 40 `games-and-strategy` cruxes structurally resembles the
  alternating-claim-on-a-stick game closely enough to transfer a new move.

- **Prior progress:** `game-value-recursion` (dormant, Elo ~1472 as of round 3, not
  revisited since) already contains: (1) the LB-claim reformulation (proved, certifiable),
  (2) Lemma R0 elementary `f`-bounds (proved, certifiable, reusable — `0≤f≤Σ`,
  `f(S)=a_1−f(S∖{a_1})`), (3) Theorem LB-A / Case A in full (proved, re-derivation of
  round-1 Case 1), (4) base cases n=0,1 (proved), (5) fixed-point algebra (verified).
  None of this is new versus the certified lemmas already in `lemmas/`, but Lemma R0 and
  the LB-claim reformulation are clean, general, and NOT yet certified — worth certifying
  as shared infrastructure even without closing the gap (cheap Elo-neutral win for whoever
  builds this slug).

- **Dead ends (do not retry):** (a) treating "explicit game strategy" as a way to avoid
  proving `f(Q) ≥ 1` — impossible, `endgame-greedy` makes the claiming phase fully
  deterministic, so this is provably the same statement, not a bypass (this round). (b)
  Do not re-attempt BNF via the "single-cut monovariant" driver — already refuted in round
  5 (cut-budget-jacobsthal). (c) Do not expect the BNF/Gap-A/B minimizer to be confined to
  the pure bisection cascade — this round's numerics reconfirm a `j=n` (all-cuts-on-top)
  extremal example at the same floor value `1`.

- **Small-case / intuition notes (all conjecture/numerics, not proof):** `min f = 1`
  reconfirmed for `n=2,3,4` via a fresh independent 200k-trial random search (not reusing
  prior code), for BOTH the "any ≤n-cut refinement of `W_n`" formulation (BNF/LB-claim)
  and consistent with the previously-reported minimizer structure (flats at value 1,
  multiple non-cascade extremal configurations). This is strong convergent evidence the
  answer and both bounds are correct; it gives no new route to a proof.

**Bottom line for the outliner:** the assigned lens — an explicit Liu-Bang strategy that
bypasses potential-minimization — does not exist as a *different mathematical target*: the
certified `endgame-greedy` lemma forces any claiming-phase "strategy" argument to reduce
exactly to `f(Q) ≥ 1`, and the one existing "marking-strategy" framing
(`game-value-recursion`) already reaches the identical Gap A/B/Case-B wall via a different
derivation. This is a *fourth* independent route hitting the same wall (after self-similar
Φ-max/forest, block-recursion UPM-5, cut-budget count-function), strengthening the
plateau-rule signal that **the wall itself, not the framing, is the obstruction** — i.e. the
statement "`f(Q) ≥ 1` for every ≤n-cut refinement of `W_n`" is genuinely hard regardless of
which proof genre attacks it, and diversity of *framing* has now been reasonably exhausted
without diversity of *result*. If pursued further, the one under-explored idea is the
strategy-stealing/involution angle (item 3 above), but no instantiation was found this
round. Recommend NOT spending a full build slot re-deriving game-value-recursion's already-
proven content (Case A, LB-claim, Lemma R0) — instead, if reviving it, task the builder
specifically with the strategy-stealing angle on BNF, or fold its certifiable lemmas
(R0, LB-claim reformulation) into the lead route's toolkit and spend the diversity slot
elsewhere (SOS/quadratic dual on `f`, not yet tried, per round 5's own suggestion list).
