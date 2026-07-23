## imo-2026-03 — lens: upper-bound Case (ii) at general m≥3

### The terrain (what's been tried, and exactly why it failed)

Everything upstream of this gap is solid: **Lemma G** (greedy/order-statistic reduction),
**Lemma P** (duplicate-pair invariance of `e=L-X`), and **Lemma D/M**
(`lemmas/dm-operation-reformulation.md`, certified round 3) together reduce the whole
upper-bound direction to: *for every Liu-Bang opening multiset `A=(a_1≥…≥a_k)`, `k≤m+1`,
sum `S`, exhibit a sequence of ≤m "D" (bisect) / "M" (match-two-values) operations on the
active multiset reaching `e_final ≤ e_m·S`.* Case (i) (`a_1≥2a_2`) is fully closed for every
`m` via a clean one-variable calculus argument on `a_1` alone using both IH forms (A)/(B)
on the residual (`dyadic-cascade-induction.md` §2d) — **this part is not in question and
needs no new mechanism.**

Case (ii) (`a_1<2a_2`) is where every attempt has died, and specifically at general `m≥3`
(the `n=1,2` instances are fully closed by exhaustive hand casework that relies on `k≤3`).
Two concrete single-step greedy policies inside the certified D/M framework were tried and
**both conclusively falsified with exact-fraction counterexamples** (`potential-weighting-
upper-bound.md`, round 3, independently re-verified by the reviewer):
- **Rule 1** ("top-two-ratio test", i.e. Case-(i)/(ii)'s own split executed as a literal
  recursive algorithm): fails at `m=3`, exact witness `A=(239/500,112/500,75/500,74/500)`,
  giving `e=37/500=111/1500 > e_3=1/15=100/1500`. Diagnosis: it spends 2 of 3 cuts deleting
  the top two elements outright, leaving no budget to match the near-tied bottom pair
  `(75/500,74/500)` (gap `1/500`) that would have driven `e` to `1/500`.
- **Rule 2** ("match the smallest adjacent gap"): fails at `m=2`, witness
  `A≈(0.5006,0.3331,0.1664)`, value `≈0.1664 > e_2=1/7≈0.1429`; the objectively optimal move
  there is `M` on `(a_1,a_2)` — the *larger* gap (`≈0.1675`, not the smallest `≈0.1667`) —
  because it creates a *new* near-tied pair one level deeper (`≈0.0011` gap) that a smallest-
  gap-first rule never reaches.

Both counterexamples share one structural signature: **the correct move commits budget to a
pair that looks locally suboptimal because its payoff only materializes after a further
operation reshuffles the ranking.** Any policy decided by a function of the *current* top-`O(1)`
ranks/gaps alone is therefore structurally doomed — this is now a proven (not just observed)
fact about the D/M space at `m≥2,3`, confirmed independently by the reviewer with exact
arithmetic, so it should not be re-litigated.

What *is* known to work at every tested point: **exhaustive search over the whole (small,
bounded) D/M sequence space always finds a valid response** — i.e. the operation space itself
is adequate; only a *provable, general-m selection principle* is missing. This reframes the
open problem precisely: not "is there enough freedom" but "how do you prove existence of a
good sequence without naming an explicit greedy rule for it."

### Candidate mechanisms for Case (ii) at general m

**1. Strengthen (not localize) the induction hypothesis — "induction loading."**
KB's *General Proof Methods* / Pólya heuristics explicitly flag this move ("a stronger,
cleaner statement is sometimes easier to prove by induction — induction loading"). Rather than
seeking a *policy* (an explicit rule for which operation to apply first), prove existence
directly by strong induction on `m` with a **richer IH** than the current scalar bound
`e≤e_m·S`: e.g. an IH that also controls the value achievable when *any one* prescribed pair
of top elements is pre-committed to a match/bisect, or an IH stated as a bound on a small
*vector* of quantities (e.g. `(e, second-best-achievable-e)` or a bound parametrized by the
gap `a_1-a_2`) rather than a single number. This is exactly the kind of fix that makes
"the right move depends on what happens two levels down" provable without ever writing that
move down explicitly — the induction hypothesis absorbs the lookahead instead of a policy
doing it. This is a **structural suggestion, not a specific IH** — the outliner would need to
find the right invariant to add; the two falsified rules show the naive scalar IH is
information-poor (it can't "see" that a bottom-pair cancellation is coming).

**2. Existence via a minimal-counterexample / exchange argument on the whole final sequence
(no explicit strategy ever named).** Adapted from crux **aimo-0287** (algebra,
`extremal-principle`/`symmetric-functions-and-substitution`, "minimality forbids" pattern):
that problem needed to show a set `X` achieving a certain extremum satisfies strong local
constraints, proved not by constructing `X` but by taking a *hypothetical* minimizer and
showing any local boundary swap cannot improve it, pinning down exactly the constraints needed
to finish. Adapted here: suppose, for contradiction, `A` is a (size-minimal) Case-(ii)
counterexample at level `m` — no ≤m-operation D/M sequence achieves `e≤e_m·S`. Derive
necessary structural conditions on `A` from the fact that *every* individual D/M choice at the
first step fails to reduce to a solved `(m-1)`-instance (this is a universally-quantified,
not existentially-quantified, statement — it does not require naming the *right* first move,
only ruling out that *any* first move works, which is a cleaner logical target). This sidesteps
the "which move is right" question entirely by working with the *negation*. This is a genuinely
different top-level target from the D/M-policy search and is worth a rival approach slot.

**3. Global assignment / matching formulation instead of a sequential process.** Noted already
in round-3 memory rules as "a global potential/weight function or whole-multiset pairing
argument" — the crux corpus does not offer an exact analog, but KB's **Hall's marriage
theorem / SDR** entry (Combinatorics section) is the natural tool if this is cast as: does
there exist a valid *simultaneous* assignment of XY's `m` cut-budget to `m` target
gaps/pairs in the sorted sequence (not chosen one at a time, but posed as a global
feasibility/matching question) such that the resulting cancellation pattern achieves the
bound? The appeal is that Hall-type existence proofs prove a global assignment exists
without ever exhibiting the greedy order to build it — which is structurally exactly the kind
of "non-local effect, but existence provable anyway" result needed here. This is speculative
(no crux found that performs literally this reduction) and would need real work to set up the
bipartite structure correctly; flagging it as a mechanism to *try*, not a ready-made proof.

**4. Split-and-recombine induction (bound each half, don't choose a global rule).** Adapted
loosely from crux **aimo-0298** (combinatorics, `induction-and-construction`): that problem
bounds a potential `w(S)=Σ2^{-r(x)}` not by a greedy per-element argument but by **splitting**
the configuration into two overlapping halves (even/odd-indexed), applying the (smaller) IH
to *each half separately*, and combining via `w(S)≤½(w(S_even)+w(S_odd))`. The Case-(ii)
analogue: split the active multiset `A` into a "top block" and a "bottom block" (e.g. `a_1,a_2`
vs. the rest), apply the IH to each block under some *split* of the `m` cut-budget between
them, and argue existence of a good split (not necessarily the greedy-first one) via an
averaging or extremal choice over the finitely many ways to split the budget. This is
structurally close to what `dyadic-cascade-induction`'s Case (i) already does (peel `a_1`,
recurse on the rest) — the round-3 counterexamples show peeling *only* the top element is not
enough for Case (ii), but peeling a **two-element or variable-size top block**, with the split
point itself chosen by an extremal/exists-argument rather than a rule, might recover enough
freedom to reach the deep cancellation the falsified rules missed.

### Assessment: which looks most promising

**#1 (induction loading / strengthened IH) is the most promising**, because: (a) it directly
targets the diagnosed failure mode (the current scalar IH `e≤e_m·S` literally cannot "know"
that a bottom-pair cancellation is two levels away — a richer IH could carry that information
forward); (b) it stays inside the already-certified, reviewer-verified D/M/Lemma-P machinery,
so no new infrastructure is needed, only a better statement to induct on; (c) it is a standard,
well-attested technique (Pólya/induction-loading, explicitly in the KB) rather than a
speculative reduction, and it fits how Case (i)'s own form-(A)/form-(B) *pair* of IH statements
already had to be combined (`min` of two forms) to close that easier case — Case (ii) plausibly
needs a comparable but richer multi-form IH, not a single new global object.

**#2 (minimal-counterexample/negation argument)** is a close second and is attractive precisely
*because* it never has to name the correct move — it only has to rule out that *every* move
fails, which is the natural way to handle a "the right move is sometimes non-local/surprising"
obstruction. It is more of a genuine reframing (existence via contradiction rather than
construction) and would make a good **second, genuinely different rival approach slot** — not
a variation of #1, since it doesn't touch the IH shape at all, it works by exhaustive
first-move exclusion.

**#3 (Hall/global-matching)** is the most speculative — no crux precedent found that performs
this exact reduction for a bisect/match multiset game — but flagged because it's the only
candidate that structurally matches "prove a good global assignment exists without an
algorithm to find it," which is precisely what's needed; worth a scouting pass, not a
committed rival slot yet.

**#4 (split-and-recombine)** is the closest in spirit to the existing (already-partially-
successful) Case (i) peeling machinery, so it is the cheapest to prototype (reuse most of
`dyadic-cascade-induction`'s scaffolding), but it is also the one most likely to reduce to
"which split point" — i.e. it risks reintroducing a new greedy-choice problem one level up
unless the split point itself is chosen by an existence argument (à la #2) rather than a rule.

### Candidate technique(s)
Induction loading / strengthened multi-form IH (KB General Proof Methods, Pólya "generalize");
minimal-counterexample/exchange argument (crux aimo-0287 pattern); Hall's marriage theorem /
SDR as a global-assignment framing (KB Combinatorics); split-and-recombine two-block induction
(crux aimo-0298 pattern). All operate *within* the certified Lemma D/M reformulation — none
require re-deriving Lemma G/P/D-M.

### Cheap-kill candidates
None obvious for ruling out a whole mechanism cheaply here — but a fast sanity move for
whichever mechanism the outliner picks: before attempting a full general-`m` write-up, re-test
it by hand against the **existing two exact counterexamples already on file**
(`A=(239/500,112/500,75/500,74/500)` at `m=3`, and `A≈(0.5006,0.3331,0.1664)` at `m=2`) — any
proposed mechanism that doesn't visibly handle both (i.e. that would reduce, if made explicit,
to Rule 1 or Rule 2) can be discarded in minutes without new computation.

### Knowledge-base entries to use
- General Proof Methods — "Induction… for 'for all n' constructions, build step n from step
  n−1" + Pólya "Generalize: a stronger, cleaner statement is sometimes easier to prove by
  induction (induction loading / strengthening the hypothesis)" (candidate #1's namesake).
- Combinatorics — "Hall's marriage theorem / SDR" (candidate #3).
- Combinatorics — "Invariants & monovariants" (general framing for #1/#4, generic).
- (Already in use, not new:) Lemma G, Lemma P, Lemma D/M, Facts 1&2 (dominant extraction) —
  all certified in `results/imo-2026-03/lemmas/`, reusable as-is by any of the above.

### Analogous past problems (cruxes)
- **aimo-0287** (algebra, subtopics `extremal-principle`/`symmetric-functions-and-substitution`,
  "minimality forbids" local-exchange pattern) — genuinely analogous in *structure*: it proves
  a global extremal object satisfies certain constraints via boundary-swap contradiction rather
  than by constructing it explicitly, exactly the shape candidate #2 needs. Not analogous in
  subject matter (it's a subset-sum balancing problem), so only the proof *shape* transfers,
  not any formula.
- **aimo-0298** (combinatorics, `double-counting`/`extremal-principle`/`induction-and-
  construction`, weighted-potential `w(S)=Σ2^{-r(x)}≤1` via split-into-two-halves induction) —
  analogous in using a two-block split-and-recombine induction instead of a per-element greedy
  rule to bound a potential; candidate #4's namesake. Subject matter (scale/gap counting in a
  point set) is unrelated but the induction *shape* is directly transferable.
- **aimo-0019** (combinatorics, `games-and-strategy`/`invariants-and-monovariants`, dyadic-
  interval covering game with a "paint the cell beyond the frontier, not the gap at the
  frontier" look-ahead rule plus an *amortized* potential invariant "ink spent on `[0,x_r]`
  is at most `3x_r`") — worth naming as a **cautionary** analog: it does use a one-step
  look-ahead rule (paint the *next* cell, not the current gap) successfully, showing look-ahead
  rules aren't hopeless in general — but its success rests on an amortized *global* invariant
  proved by induction over the whole play, not on the look-ahead rule being locally optimal at
  every step. This reinforces candidate #1: the amortized invariant, not the move rule itself,
  is the load-bearing proof object. Flag as suggestive, not a tight match (different game
  structure — resource-supply covering, not alternating bisection).
- No crux found that performs literally the same "bisect/match a sorted multiset to bound an
  alternating rank-sum" operation — this problem's specific combinatorial object (the D/M
  space) appears to be genuinely novel relative to the corpus; only the proof *techniques*
  above transfer, not a ready-made solution.

### Prior progress
See "The terrain" above for the exact state: Case (i) fully closed for every `m`
(`dyadic-cascade-induction.md` §2d); Case (ii) fully closed only through `m=2`
(hand casework using `k≤3`); Lemma D/M certified and general; two greedy policies inside it
falsified with exact counterexamples (`potential-weighting-upper-bound.md`); bounded exhaustive
search confirms the D/M operation space itself suffices at every point checked so far
(evidence, not proof, that no richer strategy space is needed — only a better existence
argument).

### Dead ends (do not retry)
- Rule 1 ("top-two-ratio test" / literal execution of Case (i)/(ii)'s split as a recursive
  algorithm) — falsified at `m=3`, exact witness above. Do not re-propose in any form that
  reduces to it (e.g. "always resolve ties toward the larger element" dressed up differently).
- Rule 2 ("match the smallest adjacent gap") — falsified at `m=2`, exact-to-3-decimal witness
  above. Do not re-propose any single-step rule whose decision is a function of only the
  current top-`O(1)` ranks or adjacent gaps — both falsifications show this local-only
  information is provably insufficient.
- (From `dyadic-cascade-induction`, round 3, already recorded in run_state.md) a "merging
  never increases `e`" general monotonicity lemma — tested and found FALSE; this is for the
  *lower-bound* multi-cut gap, not directly Case (ii), but the failure mode (a plausible-
  sounding general monotonicity fact turning out false under this problem's specific
  dyadic/near-uniform structure) is a useful cautionary pattern for whatever Case (ii)
  mechanism is tried next — don't assume monotonicity-style "simple facts" without checking.
- Global concavity of the true value function `g` — proven FALSE at `n=2`
  (`lemmas/non-concavity-of-g-at-n2.md`); irrelevant to Case (ii) directly but rules out
  "prove Case (ii) via a concavity/convex-optimization shortcut on `g` itself" as a mechanism.

### Small-case / intuition notes (conjecture, not proof)
- The two falsified rules' failure points both occur exactly where the D/M operation
  sequence has a "budget conflict": committing the last available cut to close the visible
  top gap uses up the resource needed to close a not-yet-visible (post-operation) bottom gap.
  This suggests (conjecture) that the correct general mechanism will involve reasoning about
  *all* of XY's `m` cuts as a joint allocation from the start, not a sequential decision
  process — supporting candidates #1 (richer IH that "pre-commits" enough structure) and #3
  (global assignment) over any sequential greedy refinement.
- Both m=2 and m=3 counterexamples are "near-degenerate" configurations (near-tied bottom
  pairs, or top-two close to the `2:1` Case boundary) — consistent with the general pattern
  seen throughout this problem (extremal configurations cluster at case boundaries / near-tie
  points), reinforcing that any correct mechanism must handle near-ties globally, not just at
  the top of the sorted order.
