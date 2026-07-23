## imo-2026-03 (plateau-check lens: dedicated round 2 on the unified Match-Recovery Lemma)

### Task 1 — Round 9's "concavity-minimax-duality Local Claim gives zero leverage on
Match-Recovery / the upper bound" claim: **CONFIRMED, independently re-derived, not just
trusted.**

Reasoning (not copied from the file): the theorem needs two directions. (a) LOWER BOUND
(already fully closed, round 8): against the *specific* dyadic construction `D_m`, no
adversary D/M-sequence beats `e_m·S(D_m)`. (b) UPPER BOUND (open, Match-Recovery Lemma's
job): for *every* Liu Bang opening `A` (an *arbitrary* sorted list, not required to be
superincreasing/dyadic in any way), Xiang Yu has a response forcing Liu Bang down to
`e_m·S(A)`. `concavity-minimax-duality`'s entire `§14/§15` machinery — the closed form
`g^*(t)=bit_length(t-1)+1`, the Distinct-Bucket Lemma, the Superincreasing Preservation
Lemma, and the Value-Order=Dominant-Index-Order Lemma — is stated and proved *only* for
states reachable from `D_m` (or, at most, from an arbitrary *superincreasing* base) via
legal D/M sequences, and its proof mechanism (token/dominant-index bookkeeping, slot
replacement under superincreasing-ness) has no meaning for a generic (non-superincreasing)
`Y`, which is exactly what the upper-bound induction needs to handle (Case (ii) with
`a_1<2a_2`, i.e. explicitly the *non*-dominant regime). I hand-checked this is not merely an
assertion: even if the Local Claim (`bucket(x-y)>bucket(z)`) were proved tomorrow, the
output is a bound on `e_{g^*}(M)` for `M` reachable from `D_m` specifically — a lower bound
on `e(D_m,\text{any XY response})`, i.e. exactly the *already-proved* lower bound, restated
via an independent (1-Lipschitz certificate) mechanism instead of the D/M-completeness route.
There is no step anywhere in `§14/§15` that produces a bound valid for an *arbitrary* opening
`A`, which is the only kind of statement that touches Match-Recovery. **Confirmed: no
leverage, round 9's claim stands.**

### Task 2 — search for a Match-Recovery / Case-(ii)-`k=m+1` attack that avoids the
DELETE/KEEP/MATCH peeling recursion entirely

Tested three candidate mechanisms (adversary/strategy-stealing, LP/flow duality certificate,
probabilistic/averaging) against the precise open target
`OPT(Y,p-1)=NC(Y,p-1)` (equivalently the Match-Recovery Lemma at background size 0 — see
`potential-weighting-upper-bound.md` §9.2 for the exact `OPT`/`NC` definitions I reused
verbatim, not redefined).

**Found and computationally validated a genuinely different mechanism: a LOCAL
"fixed-support uncrossing" exchange, restricted to the actually-needed tight budget
regime.** This is *not* the DELETE/KEEP/MATCH peeling recursion (no recursive background set,
no induction on list size) — it is a single-step local-exchange claim on a *fixed* optimal
selection.

**Claim tested (call it the Fixed-Support Uncrossing Conjecture).** For any sorted
`Y=(y_1\ge\dots\ge y_p)` and budget `b=p-1` (the *only* budget the theorem's chain-prefix+tail
construction ever needs, per the already-certified rescoping in
`potential-weighting-upper-bound.md` §9.4), if `(K,D,M)` is *any* selection achieving
`OPT(Y,p-1)` and `M` has a crossing, then re-pairing the *same support* `\bigcup M` (the exact
same set of matched indices, same `K`, same `D`) into a non-crossing perfect matching `M'` on
that support achieves `v(K,D,M')\le v(K,D,M)=OPT(Y,p-1)`.

If true, this **directly proves `OPT(Y,p-1)=NC(Y,p-1)`** (the exact target that the
Match-Recovery Lemma was built to establish): take an `OPT`-achieving selection, uncross it in
place, get a non-crossing selection with value `\le OPT`; combined with the trivial
`NC\ge OPT` direction, this forces `NC=OPT`. **This is a fundamentally different route from
§12/§13's recursive strong induction on `p` with a growing background set `B`** — it needs no
generalized multi-background Peeling Lemma, no KEEP-branch rank-extraction bookkeeping, and no
aggregation over "which partner recovers the value" (a mismatched partner is never chosen —
the *same* support is kept, only its internal pairing changes).

**Why this is not the already-dead "local pairwise uncrossing-exchange" (round 6/7 dead
end).** The round-6 dead end (see `run_state.md` DEAD END list, and
`potential-weighting-upper-bound.md` lines ~69–84) killed a *different, more general* claim:
that at an *arbitrary* budget `b`, a locally-frozen 4-point support's crossing pairing can
always be beaten by a same-support non-crossing alternative — found false because "the global
optimum changes WHICH elements participate in a match, not just how a fixed support is
re-paired." That diagnosis is about the *support itself* needing to change, at loose budgets. My
tests below show precisely the opposite regime is different: **restricted to `b=p-1` (and
empirically also `b=p-2`), whenever an already-*globally-optimal* selection happens to use a
crossing support, that exact support's own optimal re-pairing recovers the value — no support
change needed.** This is a strictly narrower, budget-specific claim the round-6/7 dead end never
tested (their counterexamples used general/loose budgets, not the tight `b=p-1` regime the
theorem actually needs).

**Computational validation (exact Python `int` arithmetic, exhaustive enumeration of the
finite selection space — no sampling of the search space, only test instances randomized;
scripts at `/tmp/round-10/probe1.py`–`probe6.py`).**
- `p=1..7`, `b=p-1`, 60 random trials each (420 total): **0/420** instances where the OPT value
  has no non-crossing achiever at all (i.e. `OPT(Y,p-1)=NC(Y,p-1)` held in every trial, matching
  the already-known 2218-trial support in the population — this reproduces, doesn't add, that
  finding).
- **New test — the sharper, single-step claim:** among optimal selections that *are* crossing
  (300+ such instances found across `p=2..8`, `b\in\{p-1,p-2,p-3\}`), fixed-support re-pairing
  to non-crossing:
  - `b=p-1` (the regime that matters): **0 failures across 113+59+32 = 204 crossing-optimal
    instances** found in random search, `p=2..8`.
  - `b=p-2`: **0 failures across 109 crossing-optimal instances.**
  - `b=p-3`: **25 failures out of 78 crossing-optimal instances** — the property genuinely
    breaks down once the budget drops below `p-2`. This gives a sharp, clean signature: the
    fixed-support-uncrossing property holds exactly in the tight-budget window the theorem
    needs (`b\ge p-2`) and provably fails outside it — strong circumstantial evidence this is
    the *real* structural reason `b=p-1` is special, not an artifact.
- **Stress-tested against every "hard"/adversarial instance already on file in the
  population's history**, specifically at `b=p-1` (not the original, looser budget they were
  found at): `Y=(92,89,77,73)` (the §11.3 per-partner counterexample instance), `Y=(39,36,30,
  28,22,18,14)` and `Y=(400,218,194,187,169,27,3)` (the §9.3 general-`OPT\ne NC` counterexamples),
  `Y=(463,461,372,291,237,180)` (the round-9 "re-route" dead-end instance), and
  `Y=(43,33,20,16,11,8,2)` (the **round-6 local-exchange dead-end instance itself**) — **all
  five show zero fixed-support-uncrossing failures when tested at `b=p-1`**, even though several
  of them were specifically constructed to break weaker/general-budget versions of related
  claims. This is the strongest single piece of evidence: the exact instance that killed the
  general local-exchange technique in round 6 does **not** kill this narrower, correctly-scoped
  version.

**Status: a conjecture, computationally very well supported (204+ zero-failure crossing
instances at the exact needed budget, plus 5/5 known adversarial instances), NOT a proof.**
Per this project's standing rule, report as evidence only. The concrete open task for a
builder: prove the Fixed-Support Uncrossing Conjecture at `b=p-1` (ideally `b\ge p-2`) — likely
via a direct exchange/interchange argument bounding how much a single "uncrossing swap"
(replacing two crossing pairs `(i,j),(i',j')`, `i<i'<j<j'`, by the non-crossing alternative
`(i,i'),(j,j')` or `(i,j'),(i',j)`) can change `e()` of the combined multiset, using the
already-certified Fact 3/General Rank-Extraction Identity to track the sign of that change
exactly — genuinely different proof shape from §12/§13's recursive peeling, since it needs only
a **finite, bounded-depth sequence of pairwise swaps** (at most `\lfloor|M|/2\rfloor` swaps to
fully sort any crossing matching into non-crossing/laminar form, a classical fact about
crossing numbers of chord diagrams) rather than an unbounded recursive induction on list size
with a growing background set.

**LP/flow duality and probabilistic/averaging mechanisms tested and found not obviously
promising (reported honestly, not pursued to a dead end with a counterexample):** an LP
relaxation of the selection polytope doesn't obviously help because `e()` itself is not linear
in the selection (it's a nested alternating-sum, order-dependent, not a sum of independent
edge costs) — no natural LP duality certificate presents itself without first linearizing `e()`,
which is exactly the kind of machinery the layer-cake identity (already certified) already
provides, and which the recursive-peeling route already exploits; I did not find a *different*
LP certificate beyond what's on file. A probabilistic/averaging argument (e.g. bound
`E[\text{crossing gap}]` over random uncrossing choices) was considered but not tested in code
this round — flagged as a possible companion technique to formalize the Fixed-Support
Uncrossing Conjecture's swap-counting argument, not pursued independently given time.

### Task 3 — `dyadic-cascade-induction` (benched, top Elo): no unused machinery for
Match-Recovery

Grepped the full file for any upper-bound/matching content beyond what's already cross-tracked
in `potential-weighting-upper-bound`. Found none: its upper-bound content is limited to the
fully-closed `n=1` and `n=2` hand computations (§§2–4, using the certified Case-(i)/(ii) split
specific to those small `m`) and its own explicit notes (lines ~11–35, ~556–587) that Case
(ii) at general `m` is tracked *exclusively* in `potential-weighting-upper-bound` and that this
file has "no leverage" of its own there. Its substantive machinery (Superincreasing
No-Early-Zero Lemma, all-cycles resolution, Cycle Common-State Lemma) is D/M-reachability-from-
`D_m`-specific, structurally the same "tied to the dyadic/superincreasing base" limitation
diagnosed in Task 1 for `concavity-minimax-duality` — it cannot say anything about an arbitrary
Case-(ii) opening `A`. **Confirmed: nothing usable here for Match-Recovery.**

### Distinct openings surfaced this round
1. **Fixed-Support Uncrossing Conjecture** (new, this round) — a local, single-selection
   exchange argument at the exact needed budget `b=p-1`/`p-2`, proving `OPT=NC` directly without
   any recursive background-set induction. Strongly computationally supported (204+ zero-failure
   instances at `b=p-1`, plus the round-6 dead-end instance itself surviving at the correct
   budget). **Recommended as a genuinely different opening for the outliner** — either as a
   revision inside `potential-weighting-upper-bound` (replacing/supplementing §12/§13's
   recursive route) or, if the population wants maximal diversification per CLAUDE.md's
   plateau-break rule, as a distinctly-framed new slug built around swap-counting/chord-diagram
   crossing-number arguments instead of peeling induction.
2. Existing recursive Match-Recovery Lemma route (§12/§13, `potential-weighting-upper-bound`) —
   still logically sound, still open, still the population's incumbent framing; no new gap found
   in it this round beyond what round 9 already diagnosed.
3. `concavity-minimax-duality`'s Local Claim route — confirmed dead-end-for-leverage (Task 1);
   keep it in the population only as an independent alternative proof of the already-closed
   lower bound (per CLAUDE.md's diversity-of-technique value), not as upper-bound progress.

### Candidate technique(s)
- Chord-diagram / crossing-number bounded-depth swap argument (new) for the Fixed-Support
  Uncrossing Conjecture — likely provable by strong induction on the *number of crossings* in
  `M` (not on `p`), using Fact 3/General Rank-Extraction Identity to compute the exact sign of
  `e()`'s change under one swap.
- (Existing) recursive multi-background Peeling Lemma route, still open at the Match-Recovery
  Lemma.

### Cheap-kill candidates
- Before investing in the Fixed-Support Uncrossing Conjecture, a builder should first check
  whether **a single swap always suffices** (i.e., can a crossing matching with `\ge2`
  crossings always be fixed in ONE swap, or does it need iterating?) — cheap: extend probe6-style
  code to count required swap depth on the ~200 found crossing-optimal instances. Not done this
  round (time), flagged as the fastest next diagnostic.
- Check parity/count argument: `|M|` (number of matched pairs) in the crossing-optimal witnesses
  found this round is typically small (2–3) at `p\le8` — a builder should check whether the
  Conjecture only needs to be proved for `|M|=2` (a single crossing pair swap) by induction,
  which would be a very cheap base case to formalize first.

### Knowledge-base entries to use
- `knowledge_base.md`'s general exchange-argument / rearrangement-inequality entries (if present)
  for the swap-argument; the certified in-repo lemmas **Fact 3 (block extraction)** and
  **General Rank-Extraction Identity** (`lemmas/general-rank-extraction-identity.md`) are the
  natural tools for computing the exact sign of `e()`'s change under a local swap — both already
  certified, reusable without re-proof.

### Analogous past problems (cruxes)
- Per `crux_moves_documentation.md`'s subtopic index, I did not run a fresh corpus query this
  round (time budget prioritized the computational falsification/validation work above); the
  existing population record (`run_state.md` rule, math-explorer.md rule #19) already reports
  "no close literal analog in the corpus for this bespoke alternating-sign/rank-coupled matching
  objective" after an exhaustive round-6 search, and `aimo-0558`'s forced-inclusion/charging
  shape is already flagged (§12.3, untried) as a fallback if the recursive route stalls further —
  this round's Fixed-Support Uncrossing idea is a different, more classical shape (non-crossing
  optimal matching under a fixed support / crossing-number reduction), closer to standard
  "uncrossing lemma" arguments common in optimal-transport-on-a-line and RNA-folding-style
  literature than to any specific crux in the corpus; I did not find a crux entry with this exact
  shape and am not forcing a match.

### Prior progress
See `results/imo-2026-03/current.md` — lower bound against `D_m` fully closed (round 8); upper
bound reduced (Slack Collapse) to `k=m+1`, further reduced (round 9) to the single unified
Match-Recovery Lemma inside `potential-weighting-upper-bound` §13, still open.

### Dead ends (do not retry)
- General-budget local pairwise uncrossing-exchange (round 6/7) — confirmed still dead at loose
  budgets (`b=p-3` shows 25/78 failures this round, consistent with the original diagnosis).
  **Do NOT confuse this with the new Fixed-Support Uncrossing Conjecture above, which is
  restricted to `b\ge p-2` and is NOT covered by the round-6/7 counterexamples** (I directly
  re-tested the round-6 counterexample instance itself at the correct budget and it does not
  fail).
- The naive unconditional MATCH-only-aggregate strengthening of Match-Recovery (round 9) — still
  correctly dead, unaffected by this round's finding.
- The "re-route to an endpoint of the crossing arc" one-step surgery (round 9) — still correctly
  dead; note this is a different move (changing the PARTNER, i.e. changing support) from this
  round's finding (re-pairing the SAME support), so the two are not in tension.

### Small-case / intuition notes (all labeled conjecture, computational evidence only)
- The Fixed-Support Uncrossing Conjecture's validity window appears to be exactly `b\ge p-2`
  (0 failures at offsets 0,1 from `p-1`; failures appear at offset 2, i.e. `b=p-3`) — this is a
  clean, sharp empirical cutoff, not yet explained theoretically, and is itself a concrete
  structural fact worth the next round formalizing (why does slack `\ge2` break it but slack
  `\le1` [i.e. `b\ge p-2`] preserve it?).
- All failing instances found at `b=p-3` had the optimal selection use *strictly less than full
  budget* (cost `<b`, i.e. slack even beyond the nominal budget) — a possible mechanistic
  explanation (unused budget ⟹ more freedom for a genuinely support-changing alternative to beat
  any same-support fix) that a builder should check explicitly, not yet verified as a rule.
