## imo-2026-03

### Distinct openings
1. **Two-phase minimax reduction.** Prove the claiming phase is *equivalent* to
   both players simply "always take the currently-largest unclaimed piece"
   (a pure greedy rule, no real strategic interaction once the piece multiset
   is fixed). This collapses the whole problem to a **combinatorial
   optimization on multisets**: LB picks a partition of `[0,1]` into
   `≤ n+1` positive lengths (using `≤ n` points), XY refines it into
   `≤ 2n+1` pieces (using `≤ n` more points, each new point splits one
   existing piece), and the payoff is `Σ (odd-ranked pieces, sorted desc)`.
   I verified this greedy-equivalence lemma **computationally** (exact game-tree
   recursion vs. greedy, 200 random multisets up to 6 pieces, always match —
   see below). This lemma is the crux move to state and prove formally
   (exchange-argument / induction on number of pieces) — I did NOT find it
   already in the KB, so it likely needs its own short proof.
2. **XY's response as an "even-out the sizes" attack.** Once pieces are fixed,
   XY's goal is to *maximize the sum of even ranks* (equivalently minimize
   LB's odd-rank sum). Cheap structural fact: with `m` equal pieces and any
   split, XY can force LB down to essentially `⌈m'/2⌉/m'` for the *resulting*
   piece count `m'`; in particular **splitting exactly one piece of an
   all-equal partition in half already forces LB down to exactly 1/2**
   (verified: 3 equal thirds + 1 XY cut ⇒ LB gets exactly 1/2; this is a very
   cheap, strong upper-bound tool for ANY n: if LB ever presents `k` equal
   "big" pieces XY can degrade LB toward 1/2 using few points).
3. **LB's "geometric doubling" construction.** Instead of equal spacing,
   LB should make pieces of *geometrically increasing* size
   `1, 2, 4, …, 2^n` (in units of `1/(2^{n+1}-1)`), i.e. cut points at
   partial sums of `1,2,4,…,2^{n-1}` (n points, n+1 pieces). This is the
   construction that (for n=1,2, see below) provably/numerically achieves
   the true optimum — strictly better than equal spacing or the naive
   "one small + n copies of 2/(2n+1)" idea (see Dead ends).
4. **Self-similar / recursive framing.** The doubling construction suggests
   viewing LB's strategy as: reserve a top piece of size `t`, and recursively
   play the *same game with one fewer point* on the remaining `1−t` of stick
   (scaled). This recursive/self-similarity idea is a good target for an
   induction-based proof of the closed form, and matches the exact recursion
   `S(n) = 2^n + S(n-1)`, `S(n) = 2^{n+1}-1` (total "scale" units), `top(n) =
   2·top(n-1)`.

### Candidate technique(s)
- Exchange argument / greedy-optimality proof for the alternating-pick
  subgame (KB: no direct entry, but this is the same flavor as "Pigeonhole
  / extremal principle" and "Invariants & monovariants" — more precisely
  it's a standard "greedy is optimal in a zero-interaction alternating
  selection game" lemma, provable by induction on the number of pieces
  with a swap argument).
- Induction / recursive construction (KB: **Induction**, **Constructive vs.
  existence** — "find all n" needs matching upper bound + construction).
- Extremal / adversary argument, "smoothing" toward equal pieces (KB:
  **Piecewise-concavity smoothing** entry is for sinusoids, not directly
  applicable, but the general idea — the adversary's optimal response drives
  configurations toward a boundary/canonical shape — is analogous).

### Cheap-kill candidates
- **Parity/size count**: total pieces after both phases is at most `2n+1`
  (odd!), so if BOTH players use all their points and no piece coincidentally
  gets a duplicate, LB (who picks 1st, 3rd, 5th, …) always ends up with
  `≥ ⌈m/2⌉` of the pieces for whatever final piece-count `m` — but `m` itself
  is contested (LB wants odd final `m`, XY wants even `m`) since LB only
  controls making `n+1` pieces and XY controls whether to add an odd or even
  number of splits. This parity tension is a good structural warm-up fact but
  does NOT by itself pin the value (I confirmed XY can still hurt LB a lot
  even keeping `m` odd, by unequal splits, not just by parity).
- **"Equal partition is bad for LB"**: if LB ever makes 2 or more pieces
  equal to each other and "big" (comparable size), XY can pair-split down
  toward exactly 1/2. This immediately kills any construction based on equal
  spacing or on the naive "`(n+1)/(2n+1)`" guess (see Dead ends) — useful as
  a pruning check on any candidate LB construction the outliner proposes.

### Knowledge-base entries to use
- **Induction** and **Constructive vs. existence** (General Proof Methods) —
  for the "find `c(n)`, prove upper bound (XY's response construction) AND
  matching LB strategy" structure required by `compute_and_prove`.
- **Invariants & monovariants** (Combinatorics) — possibly for tracking the
  total/ratio through the recursive doubling structure.
- **Pigeonhole / extremal principle** — general flavor of the size-comparison
  arguments needed to show XY's response is optimal (no config beats the
  claimed bound).
- No entry in `knowledge_base.md` directly addresses "alternating claiming of
  items to maximize own sum" — flag this gap; the greedy-equivalence lemma
  needs to be proved from scratch (exchange argument), it is NOT citable from
  the KB as stated.

### Analogous past problems (cruxes)
I read `crux_moves_documentation.md` and would filter `combinatorics` by
subtopic `games-and-strategy` and `extremal-principle` / `processes-and-algorithms`
for genuine analogues (two-phase alternating claiming / cutting games). I did
not have time this round to run the actual corpus queries (JSON files) given
the depth of the numeric exploration below — **flag for next round /
another explorer**: query `past_crux_moves_database.json` with
`domain=combinatorics`, `subtopic=games-and-strategy`, look for stick/interval/
segment-claiming or "alternately pick largest" problems, and cross-reference
`past_problems_database.json` for the statement to judge genuine analogy
before trusting any match.

### Prior progress
None (results/imo-2026-03/current.md was empty; this is round 1).

### Dead ends (do not retry)
- **Naive conjecture `c(n) = (n+1)/(2n+1)`**, from the tempting idea "LB
  makes `n+1` pieces, one of size `1/(2n+1)` and `n` copies of size
  `2/(2n+1)`, XY splits every big one in half giving `2n+1` equal pieces."
  **Refuted numerically**: for `n=2` this LB partition `(1/5,2/5,2/5)` only
  guarantees `≈0.50`, NOT `3/5=0.6` — XY's actual best response is to split
  the *small* piece in half (not the big ones), producing two matched pairs
  `{0.4,0.4}` and `{0.1,0.1}` and pushing LB down to exactly `1/2`. This
  construction and its refutation should not be re-tried as-is; the correct
  LB construction is the geometric-doubling one below.
- **Equal-spacing for LB** (`n+1` equal pieces): XY always beats this down to
  exactly `1/2` with a single well-chosen split (verified for `m=3` and
  `m=5` equal pieces). Any approach proposing equal spacing as LB's strategy
  is a dead end.

### Small-case / intuition notes (numeric, labeled as conjecture except n=1)
- **Greedy-equivalence lemma**: verified computationally exact (not just
  conjectured) on 200 random trials, multisets of size ≤6: the alternating
  "each player maximizes own total" game always has the same first-mover
  total as pure greedy (take-largest-remaining each turn). High confidence
  this is a true, provable lemma (standard exchange-argument territory).
- **n=1 (exact, verified analytically + confirmed by fine grid search)**:
  `c(1) = 2/3`, achieved by LB placing its single point at `1/3` (pieces
  `1/3, 2/3`). Tent-function analysis: LB's guaranteed value as a function of
  its point `p∈[0,1/2]` is `(1+p)/2` for `p≤1/3` and `1-p` for `p≥1/3`,
  maximized at `p=1/3` giving `2/3`. XY's optimal reply at the optimum is to
  cut the big piece exactly in half (giving 3 equal pieces of `1/3`) — but
  note that away from `p=1/3` XY's optimal reply is NOT always "split in
  half"; sometimes it's "match the small piece" (duplicate `L`), i.e. the
  optimal XY response is genuinely case-dependent, not a single uniform rule.
- **n=2 (strong numeric evidence, not yet proved)**: extensive search
  (grid + local continuous optimization of XY's split ratios, restarted from
  many LB partitions) consistently finds the LB-optimal partition to be
  `(1/7, 2/7, 4/7)` (i.e. **geometric doubling** `1,2,4` scaled by `1/7`),
  giving value **`c(2) = 4/7 ≈ 0.5714`**. This beats every other partition
  tried (equal thirds → 1/2; the naive `(1/5,2/5,2/5)` → ~1/2; other nearby
  ratios all score below `4/7` in a fine 1D scan varying the ratio `b/a`
  around 2 and a 2D scan around `(1/7,2/7)` — the scan is symmetric and
  peaks sharply at exactly `a=1/7,b=2/7`).
- **Conjectured closed form** (extrapolating the doubling pattern,
  matches n=1 exactly and n=2 numerically to high precision):
  **`c(n) = 2^n / (2^{n+1} - 1)`**, achieved by LB placing points so the
  `n+1` pieces have lengths proportional to `1, 2, 4, …, 2^n` (partial sums
  `2^{k}-1` scaled by `1/(2^{n+1}-1)`, `k=0,…,n`), i.e. cut points at
  `(2^k - 1)/(2^{n+1}-1)` for `k=1,…,n`. As `n→∞`, `c(n) → 1/2` from above,
  consistent with the "equal pieces get driven to exactly 1/2 by XY" finding.
  **This is the strongest candidate answer to hand to the outliner** — it is
  unverified for `n≥3` (not enough time this round) and is NOT yet proved
  even for n=2 (only numerically optimized over a 2-parameter family via
  local/grid search, not a certificate) — needs (a) an XY-response
  construction proving `c(n) ≤ 2^n/(2^{n+1}-1)` for LB's doubling
  partition specifically (showing XY cannot beat it) and, separately, (b) a
  proof that NO other LB partition does better (the harder direction), most
  plausibly via the recursive/self-similar framing in opening 4.
- All numeric work is in `/tmp/game_check.py`, `/tmp/n1_check.py`,
  `/tmp/n2_check.py`, `/tmp/n2_clean.py`, `/tmp/n2_fine.py` (this container;
  not committed) if reproduction is needed.
