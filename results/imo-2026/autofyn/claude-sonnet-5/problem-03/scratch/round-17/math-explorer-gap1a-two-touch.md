## imo-2026-03 — Gap 1a's Two-Touch Lemma, the 2 open sub-pieces (KEEP branch `b_0<=w_1`; Match-Branch Domination)

### Setup recap (from `approaches/potential-weighting-upper-bound.md` §26.5, verified against the file)
`Two-Touch(C,W) := min( e(C), min_w e(C∪{w}), min_{i<j} e(C∪{|w_i-w_j|}) )`, `C` size `<=1`.
Conjecture `OPT_{+1}(C,W) = Two-Touch(C,W)`. 3/5 structural pieces proved (base case `|W|<=2`,
DELETE branch, KEEP branch's `b_0>w_1` sub-case, all via peeling `w_1=max(W)`). Open:
(d) KEEP branch `b_0<=w_1`: needs an upper bound on `OPT_{-1}({b_0},rest)` (a `sigma=-1`
"mirror Two-Touch", explicitly flagged in the file as **"not yet even formulated"**).
(e) MATCH branch: needs `OPT_{+1}({b_0,d},X) >= Two-Touch({b_0},W)` for `d=|w_1-w_j|`,
`X=W\{w_1,w_j}` — a narrow, SPECIFIC `|C|=2` comparison, NOT the general (confirmed-false)
`|C|=2` Two-Touch closed form.

I verified my brute-force `OPT_sigma`/`e_sorted` harness (`/tmp/round-17/explore/defs.py`)
against all 4 of the file's own worked examples before trusting any new result (all 4
reproduced exactly): `OPT_{+1}([5,8],(10,8,7,2))=0`, `OPT_{-1}(same)=10`,
`OPT_{+1}([1],(10,8,7))=0`, `OPT_{-1}([2,4],(5,3))=4`.

### MAIN NEW FINDING: an explicit closed-form "Three-Touch" candidate for the missing `sigma=-1` mirror (sub-piece (d))

**Conjecture (new, this round):**
```
OPT_{-1}({c},W)  =  max(
  e({c}),                                    # delete all
  max_w e({c,w}),                            # keep exactly one
  max_{i<j} e({c,|w_i-w_j|}),                # match exactly one pair, delete the rest
  max_{i<j} e({c,w_i,w_j}),                  # keep exactly two
  max_{i<j,k distinct} e({c,|w_i-w_j|,w_k})  # match one pair AND keep one other element
)
```
i.e. the `sigma=-1` maximization mirror of Two-Touch needs **touch<=3** (not `touch<=2` like the
`sigma=+1` minimization side) — a genuine, previously-undiscovered structural asymmetry between
the min- and max-directions of this recursion. The extra "touch-3" term (match-one-pair +
keep-one-other) is load-bearing, not redundant: in a 1000-trial sweep it is the strict maximizer
(strictly beats every touch<=2 candidate) in **193/1000 (19.3%)** of instances, so this is not a
disguised touch<=2 fact.

**Mechanism found by hand-inspecting counterexamples to the naive "keep-everything" and
"delete-all-or-keep-one" guesses:** the optimum for maximization can exploit the
already-certified **duplicate-pair cancellation** (Lemma P): match two `W`-elements to
manufacture a value equal to `c`, so background `c` and the manufactured duplicate cancel
in `e_sorted`, leaving only the untouched top elements. E.g. `c=8`, `W=(10,9,5,5,1)`: match
`(9,1)->diff 8`, keep `10`, delete `5,5` gives `{8,8,10}` sorted `->10-8+8=10`, beating every
"simple" (touch<=2) candidate (max there is `8`). This is a concrete instance of the
already-certified duplicate-pair-invariance mechanism being used adversarially by the
*maximizer* rather than the minimizer — worth flagging to the outliner as the intuition behind
why touch<=3 is necessary here specifically (nothing like it obstructs the `sigma=+1` side,
because there duplicate cancellation only ever *helps* the minimizer, never forces it to reach
further).

**Corroboration (bounded exact-`Fraction` computation, all clean, no violations found anywhere):**
- 600 random trials, `|W|<=6`, mixed alphabets: `0/600`.
- `|W|=4..6`, `0/400`; `|W|=7`, `0/300` (pushes one level past what round 16 tested for the
  `sigma=+1` side).
- duplicate/near-duplicate-heavy adversarial family (`W` drawn from a small pool including
  copies of `c` and `c+1/2`): `0/400`.
- **exhaustive** (not sampled) grid `W,c` from `{0,1,2,3}`, `|W|in{3,4}`: `0/1280`.
- Total: **0 violations across ~3480 combined checks** this session.

**End-to-end check that this closed form actually closes sub-piece (d)'s target inequality
(not just internally self-consistent):** using the Three-Touch closed form for
`OPT_{-1}({b_0},rest)` directly (not the brute-force `OPT`), verified
`w_1 - ThreeTouch(b_0,rest) >= TwoTouch({b_0},W)` for all `b_0<=w_1`: **`0/1239`** violations
(`|W|in{2..6}`). This is the actual KEEP-branch-`b_0<=w_1` target, confirmed at the level of
the proposed closed form, not just numerically via brute-force `OPT` (which the file's builder
already separately confirmed `0/2182`).

**Recommended proof route for the outliner:** Three-Touch itself looks provable by the exact
same "induction on `|W|`, peel `w_1:=max(W)` via the certified peeling trichotomy" strategy that
already closed 3/5 of the `sigma=+1` Two-Touch pieces:
- DELETE branch: trivial by the same subset-of-candidates argument (Three-Touch's candidate
  list for `W\{w_1}` is literally a subset of Three-Touch's list for `W` — this argument is
  sign-independent and carries over verbatim).
- Base case `|W|<=3`: should reduce to a "Four-Bound"-ish elementary lemma analogous to the
  already-certified Three-Bound Domination Lemma (a case-split-on-rank finite proof) — not
  attempted this round (scouting only), but the shape is the same family of technique, and
  `|W|<=3` is small enough that a similar finite case analysis (now on 4 or 5 candidates instead
  of 3) is very plausible to close directly.
- KEEP/MATCH branches of Three-Touch's own recursive proof will need their own case analysis
  (this is genuinely new work, not free — Three-Touch has 5 candidate shapes vs Two-Touch's 3,
  so expect more sub-cases, but the technique family transfers).
- Then, once Three-Touch is proved, sub-piece (d) itself becomes a second, separate finite
  algebra task (bounding `w_1 - ThreeTouch(b_0,rest)` against `TwoTouch(b_0,W)` term-by-term,
  matching each of ThreeTouch's 5 candidate shapes against an appropriate TwoTouch candidate that
  additionally uses `w_1`) — I confirmed this target holds (`0/1239`) but did not attempt the
  term-matching proof itself (out of scope for scouting).

**This is a genuinely new, concrete, well-corroborated lead the file does not currently have**
(the file explicitly says the `sigma=-1` mirror is "not yet even formulated" — this round
formulates and heavily stress-tests a specific candidate).

### MATCH-BRANCH DOMINATION (sub-piece (e)) — narrowed further, no closing mechanism found, one dead end reconfirmed and sharpened

**New observation: the base case (`gamma=empty`, i.e. delete all of `X`) is IMMEDIATE, not
open.** `e({b_0,d}) = e({b_0,|w_1-w_j|})` is *literally* one of `TwoTouch({b_0},W)`'s own
candidate terms (the pair `(w_1,w_j)` is one of the `i<j` pairs ranging over all of `W`), so
`e({b_0,d}) >= TwoTouch({b_0},W)` trivially by definition of the min. **The entire open content
of Match-Branch Domination is therefore about whether FURTHER touching `X` (beyond leaving it
fully deleted) can ever push the value below `TwoTouch({b_0},W)`** — confirmed this is a real,
nontrivial phenomenon: in a 300-trial sweep, matching/keeping within `X` reduces the value below
the base `e({b_0,d})` in **148/300 (49%)** of instances, yet (per the builder's and my own
checks) never below `TwoTouch({b_0},W)` itself.

**Cheap-kill / dead-end recheck performed as instructed:** tested whether the already-known-false
general `|C|=2` "touch<=2" Two-Touch family could serve merely as a **one-directional lower
bound** on `OPT_{+1}(C,X)` (i.e. not needing the false equality, just `OPT_{+1}(C,X) >=
touch<=2-family(C,X)`) — **also FALSE**, and more sharply so than previously documented: at
`|C|=2` specifically, `1075/3000 (35.8%)` of instances have `OPT_{+1}(C,X) <` the naive
touch<=2-family value (true optimum can go *below* the naive family's prediction, not just
disagree with it) — confirms this is a genuine structural wall, not a near-miss, and rules out
even the weaker "use it as a sufficient lower bound, don't need exact equality" idea that a
builder might otherwise try as a shortcut. (At general `|C|` this failure is even worse,
`405/3000` when `|C|` ranges `0..3` mixed in — but the `|C|=2`-isolated figure above is the
relevant one.) This does NOT touch the flagged dead end (Two-Touch fails at `|C|=2` as an exact
formula) — it is a strictly additional, sharper negative result about the same wall, confirming
(not contradicting) the existing DEAD END entry; the file's own diagnosis that the general
`|C|=2` route must be avoided here is correct and this finding reinforces it further.

**A structural diagnostic, not a proof lead:** the already-certified **Shrink-List Monotonicity
Lemma** (`lemmas/shrink-list-monotonicity.md`, `OPT_{+1}(C,W) <= OPT_{+1}(C,W\{x})` for any `x`)
explains *why* the match branch's value is so often below the base `e({b_0,d})` — it says
`OPT_{+1}({b_0,d},X)` is monotonically non-increasing as `X` grows from `empty` up to its full
size, which is the WRONG direction to get a lower bound from (it only re-derives "the value can
only decrease or stay flat as you add more touchable elements", consistent with, but not
sufficient to prove, Match-Branch Domination). Flagging this so no one re-tries "just cite
Shrink-List Monotonicity" as a shortcut here — it is necessary background intuition, not a
closing mechanism.

**No viable closing mechanism found for Match-Branch Domination this round.** The narrower
target (specific `d=|w_1-w_j|` with `w_1=max(W)`, specific comparison target
`TwoTouch({b_0},W)`, not a general `|C|=2` formula) remains, as the file already says, the
correct scope — I could not find an induction-on-`|X|` skeleton that avoids the "comparison
target doesn't shrink with `X`" mismatch that made the naive approach awkward (unlike Two-Touch's
own induction, where both sides shrink together). A **strengthened per-partner or "which
`w_j`"-indexed hypothesis** (mirroring how the population's Per-Partner Domination Lemma
sharpened a similarly-stuck aggregated claim in round 14) is the most promising unexplored
structural idea, but I did not find or test a concrete candidate statement for it this round —
flagging as the recommended next angle for a future round/builder, not a scouted result.

### Dead-end double-check (per dispatch instructions)
Re-confirmed the run-state's DEAD END (`Two-Touch fails at |C|=2`, `~24%` failure as an exact
formula) is real and unrelated to either open sub-piece's true content: (d)'s Three-Touch
candidate is strictly `|C|=1` (never grows to size 2 — the recursive call keeps the SAME
singleton `{b_0}`, per the file's own §26.5(d) derivation, confirmed by my own brute-force
reproduction of the KEEP-branch formula, `0/244` fresh checks); (e)'s open content is provably
NOT reducible to the general `|C|=2` formula (confirmed above, both as an equality — already
known — and, newly, as a one-directional lower bound — sharper). Neither proposed strategy
secretly leans on the dead |C|=2 characterization.

### Crux corpus check
Per dispatch, read `crux_moves_documentation.md` (exact field names: `technique`, `how_used`,
`domain`, `subtopic` in `past_crux_moves_database.json`; `problem`, `solutions` in
`past_problems_database.json`). Filtered `combinatorics` x `{games-and-strategy,
extremal-principle}` (205 cruxes) and searched `how_used`/`technique` for
`alternating sum|domination|case split|touch|matched pair|pairwise difference`. Found nothing
subject-matter analogous to a "bounded-touch domination via induction-on-list-size" proof shape
beyond what prior rounds already identified and are already using (the "extremal witness +
secondary tie-break + local rewrite" shape from `aimo-0960`/`aimo-0438`/`aimo-0666`, already
folded into Gap 1c's construction since round 13/16). One tangential hit, `aimo-0594`
(domination-monotone/transitive-order pivot-finding via a staircase family), was read in full —
NOT analogous (it is about locating which single coordinate a comparison rule reads via a
sandwich/transitivity argument on a totally different combinatorial object, no alternating-sum
or matching structure); do not pursue. Consistent with round 10/11/13's prior findings that no
further genuinely-analogous crux exists for this specific recursion — I recommend NOT spending
more builder time on fresh crux search for these two sub-pieces; the promising route is the
Three-Touch construction found above, which is homegrown, not crux-derived.

### Summary for the outliner
- **Sub-piece (d) (KEEP branch `b_0<=w_1`):** a concrete, heavily-corroborated candidate closed
  form ("Three-Touch") for the missing `sigma=-1` mirror is now on the table, verified to close
  the actual target inequality end-to-end (`0/1239`). Recommend this as the priority build target
  — proof route: induction on `|W|` via the certified peeling trichotomy, same technique family
  as the already-proved `sigma=+1` pieces, base case `|W|<=3` via a new finite case-split lemma
  (analogous to Three-Bound Domination but with more cases).
- **Sub-piece (e) (Match-Branch Domination):** narrowed further (base case trivial, open content
  isolated to "does touching `X` ever help drop below `TwoTouch`"), one candidate shortcut
  (naive `|C|=2` touch-family as a mere lower bound) ruled out with a sharper negative result
  than previously on file. No proof mechanism found. Recommend a per-`w_j`-indexed strengthened
  hypothesis as the next angle to try, not yet formulated as a concrete conjecture.
- Neither finding depends on or resurrects the `|C|=2` dead end.
- Even if both sub-pieces close, remember the file's own standing caveat: Two-Touch alone does
  not close Gap 1a's general-`q` Per-Partner Domination induction — a separate per-`q` case
  analysis on `A_{3,l}`'s own recursion remains needed on top (§25.2, unchanged, re-confirmed
  still true).

### Files
- Harness: `/tmp/round-17/explore/defs.py` (validated against all 4 of the approach file's own
  worked `OPT_sigma` examples before any new claim was tested).
