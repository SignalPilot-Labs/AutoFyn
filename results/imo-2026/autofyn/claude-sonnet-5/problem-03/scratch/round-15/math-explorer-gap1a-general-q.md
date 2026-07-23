## imo-2026-03 — lens: general-q closure of the Per-Partner Domination Lemma (Gap 1a)

- Distinct openings:
  1. **Naive peel-Res induction on q (the "obvious" extension of the q=3 proof) is NOT a clean
     induction — it reproduces two already-known-hard obstacles.** Peeling the top element `w1` of
     `Res` (size `q-2`) via the certified Extreme-Element/GMB Peeling trichotomy gives three branches:
     DELETE (fine, recurses to a smaller-`q` instance of the *same* lemma, background stays size 2);
     KEEP (via Fact 3 telescoping, reduces to `w1 - MAXOPT({b_0,d_l}, Res\{w1})` — needs a genuinely
     **dual (sigma=-1, MAX) companion statement**, not covered by the min-form IH); MATCH (`w1`
     matched to some `wj∈Res`, background **grows from size 2 to size 3**, `{b_0,d_l,w1-wj}`). I
     verified computationally (see below) that the MATCH branch is **not vacuous** — it strictly beats
     DELETE/KEEP-only selections in a nonzero and *growing* fraction of instances (~1.5% at q=4, ~3.6%
     at q=5, ~5.8% at q=6, random sweep, 4500/10500/18000 checks respectively) — so a proof **cannot**
     dodge background-size-3 recursion via "MATCH never wins." This is exactly the |B|≥2-generalization
     barrier already flagged as fatal for a *different, stronger* claim (round 10's dead Match-Recovery
     Lemma / FSI generalization, and math-explorer.md rule #7's "scalar-to-multi-element-context jump")
     — worth flagging explicitly since Per-Partner Domination's target is weaker (a min-bound with
     slack, not an exact index-recovery claim), so it is *not* automatically doomed the same way, but
     any q≥4 proof attempt WILL have to face genuine background-size-3 recursion, not sidestep it.
  2. **A new, clean, fully general "Background-Release Domination" lemma — found this round, TRUE,
     robustly tested, and a promising building block (not yet a full closure).** For *any* background
     `C` (arbitrary size, not just ≤2), list `W`, and any single element `y∈C` (writing `C'=C\{y}`):
     ```
     OPT_{+1}(C,W) >= min( OPT_{+1}(C', W u {y}),  e(C) )         [and the sigma=-1 MAX-dual with max]
     ```
     i.e. releasing one background element back into the free list, or deleting everything, are both
     valid lower-bound witnesses. Verified **0/6000+0/6000** (sigma=+1 and its MAX-dual separately),
     with `|C|` up to 4, deliberately duplicate/tie-heavy alphabets (the round-13 lesson about stress
     -testing boundary/tie events). This is background-size-generic (unlike anything currently on file)
     and reduces "background grows by one" (the MATCH branch's own effect) to a single clean inequality
     — this is the concrete candidate "genuine inductive structure" the dispatch asked me to look for.
  3. **But the obvious way to CHAIN this into a q-induction closure fails — two tested and refuted
     routes, both worth recording as false starts before a future round re-tries them:**
     - (a) *Full telescoping down to a background-free (`|C|=0`) bound* — chaining Background-Release
       Domination repeatedly until `C` is empty gives `OPT_{+1}(C,W) >= min(e(C), e(C\{y1}), ...,
       OPT_{+1}(∅, W∪C))`. I verified the *chain inequality itself* holds robustly (0/2500, arbitrary
       random release order) — but the resulting background-free term is **too lossy to be useful**:
       testing `OPT_{+1}(∅, Res∪{b_0,d_l}) >= min(A_1,D_l)` directly gives **6918/17956 (~38%)
       violations** (e.g. `z=[6,0,0],b0=3`: `min(A1,Dl)=3` but the background-free bound is `0`) —
       releasing *both* background elements at once lets them cancel/match against each other or
       against `Res`, destroying the very structure the bound needs. **Do not attempt the full release-
       to-background-free reduction — it is a dead end**, even though each individual release step is
       individually valid.
     - (b) *Single release step, comparing directly against `A_1`* — the natural one-step application
       (`C={b_0,d_l}`, release `y=d_l`, giving `OPT_{+1}(C,W) >= min(OPT_{+1}(\{b_0\},Res∪{d_l}), D_l)`)
       tempts one to claim `OPT_{+1}(\{b_0\},Res∪\{d_l\}) >= A_1` (since `A_1=OPT_{+1}(\{b_0\},
       Res∪\{z_l\})` looks like "the same shape, different one element"). **This is FALSE — 1923/12034
       (~16%) violations** (e.g. `z=[6,4,1],b0=7,l=1`: `A_1=3` but `OPT_{+1}(\{b_0\},Res∪\{d_l\})=2`).
       Swapping the list element `z_l` for its derived value `d_l=z_1-z_l` is **not** a monotone
       operation on `OPT_{+1}` — no general domination/magnitude relation between `z_l` and `d_l` makes
       this work (this is the SAME "positional, not magnitude" phenomenon already flagged for the
       half-step lemma in Gap 1c, §21.3, and the No-Gap Lemma in Gap 1a's own base case — a recurring
       pattern across all three gaps). **Do not re-attempt this direct one-step chain as the closing
       argument** — Background-Release Domination is real and useful, but connecting it to `A_1`
       specifically (rather than to some other release-order target) needs a genuinely new idea.
  4. **The q=3 proof's own core technique (Rank-Extraction applied to peel the *derived* value `d_l`
     directly out of a candidate optimal multiset) generalizes to the WRONG DIRECTION of inequality —
     a concrete instance of the "false start recurring" pattern the dispatch asked me to check for.**
     I traced this by hand: let `η` be any selection achieving `A_{3,l}`, `S:={b_0,d_l}∪V(η)`. Applying
     the General Rank-Extraction Identity to peel `d_l` out of `S` (rank `r`) gives an exact relation
     `e(S\{d_l}) = 2e(head) + (-1)^{r-1}d_l - A_{3,l}`, i.e. `A_1 <= e(S\{d_l}) = 2e(head) ± d_l -
     A_{3,l}`, which rearranges to an **upper bound on `A_{3,l}`** (`A_{3,l} <= 2e(head)±d_l - A_1`),
     not the lower bound `A_{3,l} >= min(A_1,D_l)` actually needed. This is exactly the shape of
     round-14's own documented false start (using a too-weak/wrong-direction bound) — a natural-looking
     generalization of the q=3 technique to arbitrary `q` produces the inequality **backwards**, and a
     builder attempting to literally extend the q=3 rank-extraction argument to peel `d_l` out of the
     *whole* optimal multiset (rather than just `{b_0,d_l,w}`) should expect to hit this exact trap.

- Candidate technique(s): a **joint/mutual strong induction on `q` (or on `|C|+|Res|`) proving BOTH
  the sigma=+1 Per-Partner Domination form and its sigma=-1 (MAX) dual simultaneously**, using the new
  Background-Release Domination Lemma (opening 2) as the mechanism for the MATCH branch's background
  growth — NOT a flat case-bash extension of the q=3 proof, and NOT a naive single-step chain to `A_1`
  (opening 3, both refuted). The concrete missing piece is a genuinely new argument connecting
  `OPT_{+1}(\{b_0\}, Res∪\{d_l\})`-type "released" quantities back to `A_1` (which uses `z_l`, not
  `d_l`) — likely positional (parity/rank of `d_l` vs. `z_l`'s original rank), analogous to the
  No-Gap Lemma / Coincidence Identity machinery already used for Gap 1a's base case and Gap 1c's
  half-step lemma (§21.3's own "suspected untested link" between the two gaps looks even more
  plausible after this round's finding — both need exactly this same positional fact).

- Cheap-kill candidates: before committing a full builder round to the joint-induction route, (i)
  test the MAX-dual analog of the trigger-chain end-to-end on `q=4,5` exhaustively (I only spot-tested
  it structurally, not wired into a full KEEP-branch closure); (ii) test whether Background-Release
  Domination, applied with the *specific* choice `y=w1` (a `Res`-derived MATCH value) rather than `y=
  d_l`, gives a cleaner connection for the MATCH branch specifically (untested this round — I only
  tried releasing `d_l`/`b_0`, not a MATCH-branch-generated background element); (iii) check whether
  restricting to genuine `F`-provenance (rather than the fully general claim currently being tested)
  makes the `A_1` vs. `OPT_{+1}(\{b_0\},Res∪\{d_l\})` swap-inequality (opening 3b) true — it might be
  that only the fully-general (non-`F`) version fails, and provenance restores it, which would be a
  much cheaper win than re-deriving the general case (I tested only the fully general form; this is
  worth a fast provenance-restricted rerun before assuming the swap-inequality route is dead in `F`
  too).

- Knowledge-base entries to use: none of `knowledge_base.md`'s generic entries were newly implicated
  this round beyond what's already cited in the approach file (Rank-Extraction/Fact 3 family, the
  DELETE/KEEP/MATCH trichotomy). The relevant *problem-specific* certified lemmas are `lemmas/general-
  rank-extraction-identity.md`, `lemmas/shrink-list-monotonicity.md`, and the (uncertified but heavily
  corroborated) Extreme-Element/Generalized Multi-Background Peeling Lemma trichotomy in §11.2/§13.2
  of the approach file — all already in use; no new KB entry surfaced.

- Analogous past problems (cruxes): none newly consulted this round (my lens was a direct algebraic/
  computational probe of the existing gap, not a fresh corpus search) — round 13's prior finding
  stands: the closest transferable *shape* is "extremal witness + secondary tie-break + local
  rewrite" (aimo-0960/aimo-0438/aimo-0666), not a literal subject-matter match. Nothing in this
  round's probing suggests a different crux is more apt.

- Prior progress: Per-Partner Domination Lemma (`A_{3,l} >= min(A_1,D_l)`, no trigger, no argmin
  needed) proved in full for `q<=3` (§22.2 of `potential-weighting-upper-bound.md`), certified
  `lemmas/shrink-list-monotonicity.md` gives the free half `A_{3,l}<=D_l` unconditionally for all `q`.
  `q>=4` open, corroborated 0 violations across 34,000+ combined checks (round 14) — I independently
  reconfirmed 0/4000+4000 at q=4,5 in a fresh half-integer exhaustive-style sweep this round, and
  additionally found it survives 0/6000+ under deliberate tie/duplicate stress (new this round).

- Dead ends (do not retry): (1) full telescoping of Background-Release Domination down to a
  background-free (`|C|=0`) bound — 38% violation rate, too lossy, confirmed this round; (2) the
  single-step chain comparing `OPT_{+1}(\{b_0\},Res∪\{d_l\})` directly against `A_1` — 16% violation
  rate, confirmed this round, `z_l` vs `d_l` swap is not monotone; (3) generalizing the q=3 proof's
  Rank-Extraction peel-`d_l`-out-of-the-whole-optimal-multiset technique to arbitrary `q` — produces
  an inequality in the wrong direction (upper, not lower, bound on `A_{3,l}`), confirmed by hand
  derivation this round; do not resurrect any of these three as the primary mechanism without a new
  idea that specifically avoids the failure mode identified (all three failures trace to the same
  root cause: naively substituting/releasing a *derived* value like `d_l` in place of, or alongside,
  the *original* list element `z_l` breaks whatever monotonicity the argument needs — any fix must be
  positional, not magnitude-based, consistent with the established pattern across all three gaps).

- Small-case / intuition notes (all labeled conjecture/corroboration, not proof): (a) the MATCH branch
  of `A_{3,l}`'s own optimal selection is genuinely activated (not vacuous) starting at q=4, and its
  activation rate grows with q (~1.5% at q=4 to ~5.8% at q=6 in my random sweep) — so any correct
  general-q proof must handle real background-size-3+ recursion, it cannot argue MATCH away; (b) the
  new Background-Release Domination Lemma (both sigma=+1 and its MAX dual) held with zero violations
  across 15,000+ combined checks including deliberately duplicate/tie-heavy instances, strongly
  suggesting it is a true, general, and reusable structural fact independent of this specific gap —
  worth certifying as a standalone lemma even before Gap 1a itself closes, since it is unconditional
  and may be useful elsewhere (e.g. as a cleaner replacement mechanism for parts of the already-
  abandoned |B|>=2 Match-Recovery generalization, though I did not test that connection this round);
  (c) the Per-Partner Domination Lemma itself continues to show zero counterexamples at q up to 6
  under both random and tie-stressed sweeps — nothing in this round's probing weakens confidence that
  the conjecture itself is true, only that the *proof mechanism* needs a genuinely new positional
  ingredient beyond a flat case-bash or the two chaining attempts ruled out above.
