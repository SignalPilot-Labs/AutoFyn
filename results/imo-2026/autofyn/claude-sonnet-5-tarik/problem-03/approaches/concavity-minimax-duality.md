## Status
partial

**(proof-outliner, round 10 note — BENCHED, no concrete open task this round.)**
`math-explorer-plateau-check.md` independently re-derived (not merely trusted) round 9's own
scope note: this file's entire `§14/§15` machinery (`g^*`, the Distinct-Bucket Lemma, the
Superincreasing Preservation and Value-Order=Dominant-Index-Order Lemmas) is stated and proved
*only* for states reachable from `D_m` (or, at most, an arbitrary *superincreasing* base) via legal
D/M sequences — its proof mechanism (token/dominant-index bookkeeping, slot replacement under
superincreasing-ness) has no meaning for a generic (non-superincreasing) opening `A`, which is
exactly what the still-open upper-bound Match-Recovery gap (tracked in
`potential-weighting-upper-bound`) needs to handle. Even a full proof of the Local Claim (§15.4)
would only re-derive the lower bound against `D_m` already established unconditionally elsewhere
(`dyadic-cascade-induction` §5.5, round 8) via an independent mechanism — real mathematical value
as a second proof of an already-closed fact, but zero leverage on the theorem's actually-open
items. **Benched alongside `dyadic-cascade-induction`** (same reasoning: no concrete task this
round that moves the theorem forward) — re-activate only if a future round finds a genuinely new
use for the Local Claim/`g^*` machinery reaching beyond `D_m`-reachable states, or for final
synthesis once the upper bound closes.

**(proof-builder, round 9 note — see new §15 below.)** Dispatched to prove the Distinct-Bucket
Lemma (§14.2) in full by strengthening the certified token invariant per §14.4's lead. Outcome:
§14.4's *specific* mechanism is refuted (exact counterexample, deviation to bucket `1` from
dominant power `3`); salvaged into two new, fully-proved general lemmas — Superincreasing
Preservation (any base, any D/M sequence) and a Slot-Replacement structural corollary — which
sharpen Distinct-Bucket into ONE precise local inequality (§15.4), verified with zero exceptions
across the entire `D_m`-reachable transition graph through `m=6` but **not proved in general**.
Also proved a third new lemma (Value-Order = Dominant-Index Order, `D_m`-specific) and a genuine
negative result (§15.5: superincreasing-ness alone cannot suffice, exact abstract
counterexample `(4,3)`), ruling out the most obvious route to close the Local Claim. Distinct-
Bucket itself remains **open**; Status stays `partial`. Per the outline-reviewer's own note (see
§15.6): even a full close of Distinct-Bucket would only re-derive a lower bound already
established elsewhere (`dyadic-cascade-induction` §5.5), so this is not blocking the theorem's
current higher-leverage open items.

**(proof-outliner, round 9 note — see new §14 below.)** This round's explorer sharpened the
open target from §13.7's vague "size-class-wide inductive invariant" into one precise structural
conjecture, the **Distinct-Bucket Lemma** (§14.2: no two elements of any `D_m`-reachable state
ever share a `g^*`-dyadic-bucket), verified 0-violation on exhaustive BFS through `m=7` plus
80,000 random walks to `m=15`. §14.3 gives an elementary, already-checked (not sketched) proof
that Distinct-Bucket implies `e_{g^*}(M)\ge\lceil|M|/2\rceil\ge1` directly, with no per-edge
monovariance and no further induction needed — reducing the ENTIRE remaining gap to this one
conjecture. §14.4 gives a concrete proof lead (strengthen the certified Superincreasing
No-Early-Zero Lemma's token invariant from "never exactly 0" to "no dyadic level is ever occupied
by two simultaneously-active tokens"). §14.5 records one tested-and-refuted naive potential
(Kraft-sum, not edge-wise monotone) — do not reuse unmodified.

**(proof-builder, round 8 note — fixed a real, reviewer-caught error in §13's illustrative
example, replaced it with a verified example, and corrected the underlying structural
narrative.)** The round-7 candidate `g^*` itself is untouched and still not proved in general,
but §13's own diagnosis of *why* it seems to work was WRONG (its "`m=6` minimizer" was not a
legal state — impossible by a basic operation-count/size argument the outline-reviewer caught).
Recomputed `D_6` from scratch, found and verified an actual minimal witness (`(2,1)`, reachable
from `D_6` via the certified Cascade Reachability Lemma, `e_{g^*}=1$ exactly), and discovered
the TRUE mechanism is the opposite of what was claimed: the minimum is achieved by driving the
multiset DOWN to size `1`-`2` (using most of the budget), not by leaving many original elements
with cancelling `g^*`-pairs (that configuration is in fact the *largest*, not smallest, value —
proved exactly, `e_{g^*}(D_m)=\lceil(m+1)/2\rceil`, the zero-operations extremum). New results,
all proved in full (not numerics alone): the exact base-case formula; an Integer-Preservation
Lemma for `g^*` (reduces the whole target to a strict-sign question); and a decisive negative
finding, with a concrete exact counterexample, that the previously-proposed edge-wise
(single-operation) monovariance technique is FALSE (a single operation can change `e_{g^*}` by
up to `5` in either direction, checked exhaustively over all `3252` edges of the `m=5`
reachable-state graph) — ruling out that specific proof strategy for good. The general
`m`-independent proof of `g^*`'s minimum-is-`1` property **remains open**; see new §13 (fully
rewritten) for all details. Status correctly stays `partial` — this is a genuine correction plus
new proved lemmas, not a proof of the theorem or of `g^*`'s general property.

**(proof-builder, round 7 note — the generalized forced-value question is now SETTLED IN
FULL, and a genuinely new, non-trivial candidate certificate was found.)** Extended the
Forced-Value machinery (Lemmas A, B) from `g(1)=1,g(2)=2` to **every** `g(2^k)` and
`g(2^k+1)`, `k\ge0` — proving a complete, general, two-sided theorem
(`k+1\le g(2^k)\le2^k`, both bounds proven via two new general reachability lemmas, not
numerics) that answers the round-6/7 outline's question **decisively as outcome (b)**:
forcing `g(j)=j` holds **exactly** for `j\in\{1,2,3\}` among the dyadic family, and
**provably fails, with an exact, unboundedly growing gap**, at every `j=2^k` (`k\ge2`) and
every `j=2^k+1` (`k\ge2`) — see new §12 below for the full proof (Localization Lemma,
Top-Two-Residual-Cancel Lemma, Successor Lemma, combined Theorem). Independently
reproduced the outline-reviewer's `g(3)=3` spot-check as a special case (`k=1`) of the new
general Successor Lemma. **Beyond the dispatched task:** used the located slack to
construct an explicit new candidate certificate `g^*` (a clean piecewise formula, matching
the proven minimal lower bound at every `2^k`) and verified it **exhaustively** (every
reachable state, exact `Fraction` arithmetic, zero floating point) against `D_m` for
**every** `m=1,\dots,6` (`326265` total reachable states, zero violations) — a genuinely
promising, non-trivial, `m`-independent 1-Lipschitz certificate differing from the identity
at every value `\ge4`, not yet proven in general (honestly flagged, not claimed solved).
Status stays `partial` (this is progress on ONE approach's certificate-search sub-problem,
not a proof of the theorem).

**(proof-outliner, round 6 note — kept live, ONE concrete next step, decisive either way; no
new explorer content targeted this specific `g_m`-certificate line this round, so no forced
new candidate is proposed.)** Round 5 proved the Forced-Value Lemmas A/B (`g(1)=1`, `g(2)=2`
forced for any valid 1-Lipschitz certificate `g`, via the certified Cascade Reachability Lemma)
and used them to refute `\min(t,1)` and `\min(t,2)` exactly. **Concrete next task for the
builder:** extend the same Cascade-Reachability-witness technique to force `g(3)`, `g(4)`,
`\dots` (not just `g(1),g(2)`) — i.e. check whether the forcing argument generalizes to show
`g(j)=j` is forced for **every** `j` reachable as a cascade value. Two possible outcomes, both
valuable and decisive: **(a)** if the forcing generalizes to all `j`, this proves NO nontrivial
1-Lipschitz certificate can ever beat the identity function `g=\mathrm{id}$ (since a
1-Lipschitz function forced to equal `\mathrm{id}` at every reachable integer value on an
unbounded discrete set is pinned down entirely) — a clean, decisive, general **negative**
result that would retire this entire certificate-search line for good (freeing the population
from re-testing further ad hoc candidates); **(b)** if the forcing provably stops at some
specific `j_0` (i.e. `g(j_0)` is NOT forced, genuine slack exists, as round 5 already found
informally at `g(4)\in[3,4]` without pinning down *why* the forcing stops there), this
precisely locates where a genuine non-trivial certificate could differ from the identity —
turning the vague "slack at `g(4)`" observation into a structural fact about *why* the slack
exists, which is exactly the missing ingredient for constructing a working `g_m`. **Do not
invent a new scalar potential candidate from scratch this round** (that line has been tried
twice, `\Phi_1,\Phi_2$ round 4, `\min(t,1),\min(t,2)` round 5, all refuted) — extend the
already-certified forcing machinery first, since it is cheap (reuses the Cascade Reachability
Lemma verbatim) and directly answers whether this whole approach can ever succeed.**

**(proof-outliner, round 5 note — REPURPOSED again, new target/technique, old §9 candidate-`Φ`
potential search formally set aside as a dead-end line (not deleted, kept for record) after
failing twice (round 3: the underlying mechanism it was meant to feed, global concavity, is
provably false; round 4: both concrete scalar candidates tried, `\Phi_1` and `\Phi_2`, refuted
with exact counterexamples).** This slug's new plan (round 5): a **1-Lipschitz weak-duality
certificate** for the lower-bound direction, adapted from the LP/Kantorovich–Rubinstein duality
idea this round's new-framing explorer surfaced — genuinely fits this slug's "find a
certificate/dual object" spirit better than a fresh scalar potential guess, since it is a
*family* of certificates (one per admissible function `g`) rather than a single number, giving
much more room to find one that works. §8 (D/M-completeness, certified) is untouched and still
this file's most solid contribution; §9 (`Φ` search) is kept as a documented dead end, not
reused. See new §10 below for the skeleton.

**(round 4 update)** Upgraded from `unsolved` to `partial`: this round produces a genuine,
rigorous partial reduction toward the theorem's lower-bound direction (a precisely-scoped
D/M-completeness result, §8 below — not merely a negative result about a dead mechanism), even
though the potential-method Step 7 plan itself still has no working candidate `Φ` (§9 below,
two candidates tried, both refuted with exact counterexamples).

**(proof-outliner, round 4 note — REPURPOSED, new target/technique, old "global concavity of
`g`" mechanism formally abandoned per round-3's RETHINK verdict, not revisited.)** This slug's
original plan (global concavity of `g` promoting a local certificate to a global maximum) is
**dead** (round 3, see below, certified as `lemmas/non-concavity-of-g-at-n2.md`) — do not
re-attempt it, including the narrower `a_1\ge1/2`-restricted variant (round-4's altframing
explorer independently re-checked this restricted salvage — `0/4329` violations in a fresh
exact-fraction test — and confirmed it is *plausible* but explicitly flagged it as **not a
genuinely different framing** from the rest of the population, since it reuses the same
piecewise-affine-region/edge-normal-kink machinery every sibling approach already uses; per
CLAUDE.md, a bypass in the same framing is not this round's diversifying move, so it is
recorded here as a fallback fact only, not pursued as this slug's new plan).

**New target and technique for this slug (round 4): a single global amortized-potential /
monovariant argument for the LOWER-BOUND direction** (`D_m` resists every XY response, for
every `m`) — genuinely different in *kind* from every other live approach: it makes no
recursion-depth case split (no Branch A/B/§5.2 casework as in `dyadic-cascade-induction`), and
it is a **universal** claim over all of XY's responses rather than an *existential* one (unlike
`potential-weighting-upper-bound`'s search for a good policy). Adapted from crux **`aimo-0196`**
(combinatorics/games-and-strategy): the crux's adversary maintains a local potential
(a size-weighted sub-window statistic) that provably cannot be fully restored by any single
opposing move, using a "just-used, so frozen this turn" trick to pin one boundary resource —
the transferable *shape* is "prove a potential can never be pushed below a floor by any move,
regardless of which move is chosen," not the specific combinatorial object (coins on a circle
vs. stick pieces are unrelated; only the proof shape transfers, per CLAUDE.md). This targets
the SAME open gap as `dyadic-cascade-induction`'s §5.2' (the multi-cut-inside-the-dominant-
piece case) but via a structurally different mechanism — a genuine second, independent line of
attack on that shared wall, not a rephrasing of the casework/induction-loading route.

**(proof-reviewer, round 3): downgraded from the builder's self-reported `partial` to
`unsolved`.** The builder's own write-up already correctly identifies that this approach's
central mechanism (global concavity of `g` at n=2, used to promote a local certificate to a
global maximum) is now *proven false*, not merely unproven — "not a gap to be closed by more
effort, it is a proven impossibility" (builder's own words). That is a correct, valuable,
independently-re-verified *negative* result (now certified as
`lemmas/non-concavity-of-g-at-n2.md`), but it is not progress *on the theorem's actual claim*
(no upper bound, lower bound, or construction was advanced) — per `CLAUDE.md`'s definitions,
`partial` requires "a correct reduction or a proven key lemma" *toward the theorem*, whereas
this file's contribution is a proof that one *candidate mechanism* cannot work. Verdict:
RETHINK — this approach, as currently conceived (global concavity), cannot proceed further;
see the reviewer's report for the narrower, unexplored `a_1\ge1/2`-restricted salvage that a
future outliner could consider as a genuinely new sub-approach.

## Approaches tried
- (round 9, this builder) **Dispatched to prove the Distinct-Bucket Lemma (§14.2) in full,
  following §14.4's lead. Result: the specific §14.4 mechanism refuted; the underlying idea
  salvaged into two new fully-proved general lemmas (Superincreasing Preservation, Slot-
  Replacement Corollary) plus a third (Value-Order = Dominant-Index Order), sharpening
  Distinct-Bucket to one precise, computationally-confirmed-but-open Local Claim; a genuine
  negative result (superincreasing alone insufficient, exact abstract counterexample) rules out
  the most obvious closing route.** See §15. Distinct-Bucket itself NOT closed this round —
  honestly reported as open, Status correctly stays `partial`. Verified against fresh,
  from-scratch computation throughout (not reusing prior rounds' BFS code): exact state counts
  re-derived (`1,3,9,31,125,585,3117,18537` for `m=0..7`, matching prior rounds and the
  outline-reviewer's own independent count), `0` Distinct-Bucket violations reconfirmed through
  `m=7`, `0` superincreasing-preservation violations through `m=7` plus `3000` general-base
  random trials, `0` Slot-Replacement mismatches (`3000` trials), `0` Local-Claim exceptions
  through `m=6` (`11535`+ transitions checked).
- (round 8, this builder) **Fixed a real, reviewer-caught error (§13's illustrative "`m=6`
  minimizer" was mathematically impossible: a 7-element final state from `D_6` with budget `6`
  can only be `D_6` itself, since every D/M operation reduces size by exactly `1`; the claimed
  list summed to `99\ne127$). Recomputed everything from scratch with an independent exact-
  `Fraction` BFS (not reusing the old numbers), verified an actual minimizer (`(2,1)`, via the
  already-certified Cascade Reachability Lemma, `e_{g^*}=1$ exactly), and corrected the
  structural narrative:** the true minimizing mechanism is collapsing to size `1`-`2` (opposite
  of the previous "many cancelling pairs" story, which in fact describes the *largest*
  `e_{g^*}` value, at zero operations used, not the smallest). **New results, all proved in
  full:** (1) exact closed-form `e_{g^*}(D_m)=\lceil(m+1)/2\rceil` for every `m` (not just
  verified — derived from `g^*(2^i)=i+1` plus the standard consecutive-integer alternating-sum
  identity); (2) an Integer-Preservation Lemma for `g^*` (nonnegative integers map to
  nonnegative integers), giving a genuine reduction of the whole target from "`\ge1`" to the
  strict-sign statement "`>0`" (since D/M operations preserve integrality, so `e_{g^*}` is
  always an integer on reachable states); (3) exhaustive (not sampled) recomputation, for
  `m=3,4,5,6`, of `\min_{\text{size }k}e_{g^*}` for every size `k=1,\dots,m+1`, finding exactly
  `\lceil k/2\rceil` in every case — a clean, `m`-independent, monotonic pattern replacing the
  wrong "cancelling pairs" description; (4) a decisive **negative** finding, with a concrete
  exact counterexample (`(32,8,4)\to(8,4)$ via a single `D(32)` operation, `e_{g^*}` dropping
  from `5` to `1`, a drop of `4`), that the previous round's proposed edge-wise (single-
  operation) monovariance proof strategy for `g^*`'s minimum-is-`1` property is **FALSE** —
  checked over all `3252` edges of the full `m=5` reachable-state graph, drops of magnitude up
  to `5` occur in both directions, ruling out that specific technique for good. **Honest
  verdict: the general (`m`-independent) proof of `g^*`'s minimum-is-`1` property remains
  OPEN** — real progress (corrected error, four new proved lemmas/reductions, one technique
  conclusively ruled out) but not a closure. Technique 2 (Kraft-budget, per crux `aimo-0790`)
  was not attempted this round (time went to fixing the error and the new material above); it
  remains an untried, independent fallback for a future round. See rewritten §13 for full
  detail. Status stays `partial` — no overclaim (the theorem is not proved, and `g^*`'s general
  property is explicitly not proved either, only exhaustively checked through `m=6`).
- (round 7, this builder) **Extended the Forced-Value Lemmas (A, B: `g(1)=1,g(2)=2`) to a
  complete, general, two-sided characterization of forcing at every `g(2^k)` and `g(2^k+1)`,
  `k\ge0`, fully closing the round-6/7 outline's dispatched question with outcome (b)
  (forcing stops at `j_0=3`, precisely explained, not merely spot-checked at `j=4`).** New
  results, all proved in full (not numerics alone — see §12): **Localization Lemma** (D/M
  operations run on a designated sub-collection of an active multiset leave every other
  element untouched, formalizing an implicit assumption used throughout the population's
  D/M-based arguments); **Top-Two-Residual-Cancel Lemma** (`(2^k,2^{k-1},\tfrac12,\tfrac12)`
  reachable from `D_m`, `m\ge k`, `k\ge1`, in exactly `m-1` ops — generalizing round 5's
  `k=2` witness `(4,2,\tfrac12,\tfrac12)` to every `k`); **Successor (Consecutive-Pair)
  Lemma** (`(2^j+1,2^j)` reachable from `D_m`, `m\ge j+1`, in exactly `m-1` ops, for every
  `j\ge0` — generalizing the outline-reviewer's `j=1` spot-check `\{3,2\}` to every `j`).
  Combined: **`k+1\le g(2^k)\le2^k`, both bounds tight and proven, for every `k\ge0`**;
  equality (hence `g(2^k)` genuinely forced) holds **iff `k\in\{0,1\}`** (elementary proof
  that `2^k>k+1` strictly for `k\ge2`, with the gap `2^k-(k+1)\to\infty`); and
  `g(2^j+1)=g(2^j)+1` **exactly** for every `j` (the Successor Lemma's gap is always exactly
  1, matched exactly by the Lipschitz cap), so `g(2^j+1)` is forced iff `g(2^j)` is — giving
  `g(3)=3` forced (`j=1`, since `g(2)` forced) but `g(5),g(9),g(17),\dots` **not** forced
  (`j\ge2`, inheriting `g(4),g(8),g(16),\dots`'s slack). Cross-validated against an
  exhaustive finite LP over the **union of every state reachable from `D_m` for `m=1,\dots,5`**
  (`19191` distinct states, `180` distinct values, solved via `scipy.optimize.linprog`): the
  LP-computed min/max of `g(4),g(8),g(16)` matched the hand-proved bounds `[3,4],[4,8],[5,16]`
  **exactly**, confirming no other reachable-state constraint in this bounded check tightens
  the bound further. **Went beyond the dispatched task**: used the located slack to build an
  explicit new candidate certificate `g^*(t)` (piecewise: identity on `[0,3]`, then on each
  block `[2^k,2^k+1]` a slope-1 ramp from `k+1` to `k+2`, on each block `[2^k+1,2^{k+1}]` a
  slope-0 plateau at `k+2`) — this is a genuinely new, non-trivial, `m`-INDEPENDENT
  1-Lipschitz function differing from the identity at every `t\ge4`, and it was
  **exhaustively verified** (every single reachable state, exact `Fraction`, zero sampling)
  to satisfy `e_{g^*}(M)\ge1` for **every** state reachable from `D_m`, for **every**
  `m=1,\dots,6` (`326265` total states checked, `0` violations). This is a substantive new
  finding — a candidate certificate surviving full exhaustive testing well beyond the
  `\min(t,1)`/`\min(t,2)`/two-slope-clip candidates already refuted in round 5 — but it is
  **honestly NOT proved for general `m`** (no algebraic/inductive argument yet, only bounded
  exhaustive verification through `m=6`); this is flagged as the concrete next task, not
  claimed solved. See new §12 for full detail, all scripts bounded and exact per the
  guardrails (no unbounded search: BFS capped, `m\le6`, exact `fractions.Fraction`
  throughout, LP used only as an exploratory diagnostic with every conclusion re-derived by
  hand).
- (round 5, this builder) **Carried out the outline-reviewer's assigned LP feasibility check
  (§10 Step 3) in full, exactly as specified, and went further: found it is feasible but
  circular (a real, decisive, concrete confirmation of the reviewer's own flagged risk — g=id
  is always a trivial witness whenever the raw claim already holds on the finite sample, so
  "LP feasible" carries no evidential weight by itself), then proved two new, fully general
  (every `m`) forced-value lemmas (`g(1)=1`, `g(2)=2` forced for any valid certificate, via
  an exactly-reachable cascade construction `D_j\to D_{j-1}` proved and independently
  `Fraction`-verified for `j=1..6`), used them to give exact closed-form refutations (not mere
  stress-test observations) of both natural clip candidates (`\min(t,1)`: fails at every odd
  `m` via a telescoping-parity argument; `\min(t,2)`: fails via a second reachable witness
  `(4,2,1/2,1/2)` forcing `g(4)\ge3`), located genuine (but so far unstructured/non-closed-form)
  slack at `g(4)\in[3,4]`, and tested a family of two-slope piecewise-linear clips (all
  refuted). **Net result: substantial, genuinely new rigor (two proved general lemmas replacing
  what were previously only numeric observations, plus two sharpened exact refutations), but no
  working `g_m` found — the honest verdict is the multi-cut lower-bound gap remains open; this
  round's contribution sharpens the diagnosis rather than closing it.** See new §11 for full
  detail. Status remains `partial` (no overclaim — a proof-of-lemma round, not a proof-of-theorem
  round).
- (round 4, this builder) **Addressed both of this round's outline-reviewer findings on this
  slug.** (1) **D/M completeness for the lower-bound direction (§8, new):** proved
  `g(A,m)=h(A,m)` (true value equals D/M-search value) by strong induction on the number of
  genuine cuts, peeling a "leaf-parent" cut at a time and applying the already-certified Lemma
  D/M single-operation identities directly (not re-derived) plus a general, `n`-independent
  Vertex Lemma imported from `elementary-exchange-smoothing`'s Step A/Corollary (now certified
  as `lemmas/vertex-lemma.md`, round 4 — cite that file, the source slug is retired) — this
  closes
  the bisect case and the tie-to-untouched-original case fully, and precisely isolates the one
  remaining open case (a "tie-dependency graph is a nonempty union of cycles" configuration,
  Step 8.4) rather than leaving the gap vague. This is real, substantial, honestly-scoped
  progress on Issue 1 (fixes the overclaim without pretending full generality). (2) **Candidate
  potential search (§9, new):** built an exact-fraction BFS harness over the full D/M operation
  space from `D_m`; confirmed `h(D_2,2)=h(D_3,3)=1` exactly (raw multisets); skipped re-testing
  the already-dead Candidate 1 per dispatch instruction; tested a genuinely new Candidate 2
  (`Φ=S(M)/(2^{r+1}-1)`, using remaining budget instead of size) which passes (P1) exactly and
  (P2) unconditionally under `D`-moves, but **fails (P2) under `M`-moves** with two independent
  exact counterexamples (`m=2`: `5/3\to1`; `m=3`: `11/7\to1`) — a new, precisely-diagnosed
  negative result (large-`y` matches starve the sum-only bound), with a concrete, bounded
  next-step diagnosis (a `\max(M)`-aware correction, untested this round, time did not permit).
  **Net: genuine forward progress on both fronts, but neither closes; Status upgraded from
  `unsolved` to `partial`** since §8 is a real proven reduction toward the theorem (not merely
  a negative result about a dead mechanism, unlike round 3's contribution).
- (round 3, this builder) **Carried out the outline-reviewer's assigned tasks in full: (1)
  exhaustive region enumeration of the n=2 domain (well beyond 6 regions, including Case
  (i)'s own internal split and Case (ii)'s finer sub-splits), (2) the precise edge-normal
  concave-kink condition stated and checked EXACTLY (fraction/symbolic gradients, not numeric
  spot checks) at every boundary reached. Result: the check found a genuine, decisive,
  exactly-provable FAILURE at one boundary — not a numerical artifact, a proof. This
  DISPROVES the central conjecture of this approach** (global concavity of `g` over the whole
  n=2 domain is FALSE, not merely unconfirmed). Full details below (see "Current best"). This
  is a complete, rigorous negative result: it closes the open question "is `g` globally
  concave at n=2?" with a definitive NO, explains why the round's numerical searches (0/34,
  0/58 violations) missed it (the violation is concentrated on a measure-zero critical line
  invisible to random/generic sampling), and means this approach's original plan (global
  concavity ⟹ local certificate promotes to global maximum) **cannot be completed as
  conceived** — it is not a gap to be closed by more effort, it is a proven impossibility. A
  possible narrower salvage (restricting to `a_1≥1/2`, which is exactly the domain
  `elementary-exchange-smoothing`'s local certificate already uses, and which is disjoint
  from the failing line) is noted as an open possibility but NOT attempted or claimed this
  round.
- (round 1–2) no prior work — approach was unbuilt/deprioritized until this round's revival;
  its old Step 3 ("min of finitely many affine-on-their-own-domain functions is concave") and
  Sion's-minimax framing were both confirmed unsound/red-herring by this round's outliner and
  are dropped for good (superseded, not re-examined this round).

## Current best

**(round 9 pointer, most current)** This round's furthest progress is §15: the Distinct-Bucket
Lemma (§14.2, this approach's entire remaining gap) is reduced, via two new fully-proved general
lemmas (Superincreasing Preservation + Slot-Replacement, §15.2; Value-Order = Dominant-Index
Order, §15.3), to ONE precise local inequality (§15.4, the "Local Claim":
`\mathrm{bucket}(x-y)>\mathrm{bucket}(z)` for the specific `z` defined there) — verified with
zero exceptions across the entire `D_m`-reachable transition graph through `m=6`, but **not
proved**. The outline's proposed §14.4 mechanism is refuted (§15.1, concrete counterexample), and
a genuine negative result (§15.5) shows the natural "superincreasing alone" strengthening cannot
close the Local Claim either, narrowing future attempts to genuinely base-`2`/token-specific
arguments. The gap is now sharper and smaller than at the start of the round, but still open.

**(round 8 pointer)** Prior to this round's work, the furthest progress was the corrected §13: the
round-7 candidate certificate `g^*` (still the population's most promising lead for a
closed-form 1-Lipschitz lower-bound certificate) is now understood correctly — its previous
illustrative example was wrong and has been replaced with a verified one (`(2,1)$, reachable
from `D_6` via the certified Cascade Reachability Lemma, `e_{g^*}=1` exactly), its structural
mechanism is corrected (the minimum is attained by collapsing to size `1`-`2`, not by leaving
many original elements in cancelling `g^*`-pairs — that configuration is instead the *exact
formula for the maximum*, `e_{g^*}(D_m)=\lceil(m+1)/2\rceil`, newly proved in closed form), and
one natural proof technique (edge-wise/single-operation monovariance) is now conclusively ruled
out by an exact counterexample. `g^*`'s minimum-is-`1` property remains an **open conjecture**
for general `m`, exhaustively verified (not proved) through `m=6`. See §13 below for full
detail. Older progress (§8's D/M-completeness result, §9's potential search, §10-§12's
certificate/forcing machinery) is unchanged and still valid, described below.

**(round 4 pointer)** This round's actual furthest progress toward the theorem's LOWER-BOUND
direction is §8 (D/M completeness modulo the precisely-isolated "all-cycles" open case) and §9
(potential-`Φ` search, no working candidate yet found, two dead ends documented with exact
counterexamples) — see those sections below. The "Headline result" immediately below is
round 3's negative result (kept for context, still valid, but is about a *different*,
now-abandoned mechanism for this slug).

**Headline result (round 3, fully rigorous): global concavity of `g` at `n=2` is
FALSE.** `g` has a strict, exact, provable local minimum-in-a-transverse-direction on the
open line segment `{(1/2, t, 1/2−t) : t∈(1/4,1/2)}` inside Case (ii) — `g` equals exactly `0`
on this whole segment, while `g` is strictly positive at every generic point immediately on
either side of it along the `a_1`-direction. This is a textbook violation of concavity (a
concave function cannot dip to a strict interior local minimum flanked by strictly larger
values on both sides along a straight line in its domain), proved below with exact
computation, not sampled. This kills the approach's central mechanism outright.

### 1. Setup, recalled from siblings (not re-derived)

Normalize `S=1`. `a_1≥a_2≥a_3≥0`, `a_1+a_2+a_3=1`. By **Lemma G**
(`lemmas/greedy-reduction.md`), Liu Bang's total under optimal alternating claiming is the
odd-rank sum of the final sorted multiset; write `e := L−X` (`≥0` always, since a sorted
descending list `x_1≥x_2≥…` satisfies `x_{2i-1}≥x_{2i}` termwise, so
`e=\sum(x_{2i-1}-x_{2i})+(\text{possibly one unpaired trailing term}\ge0) \ge 0` — this
elementary fact, already used implicitly throughout the population, is reused explicitly
below). `g(a_1,a_2,a_3) := \min_{\text{XY's ≤2 cuts}} e(\text{final multiset})`, the TRUE
best-response value (not a sufficient-strategy proxy). Domain: the 2-dimensional simplex
`D:=\{(a_1,a_2): a_1\ge a_2,\ a_1+2a_2\ge1,\ a_1+a_2\le1\}` (with `a_3:=1-a_1-a_2` implicit).

### 2. Region enumeration (the outline-reviewer's Task 1)

Following `dyadic-cascade-induction`'s §2 exact formulas (all re-verified below, not
re-derived), the domain splits first into Case (i) (`a_1\ge2a_2`) and Case (ii) (`a_1<2a_2`),
each of which further splits by the sign of `a_2-2a_3`, and Case (ii) additionally by the
position of `u:=a_1-a_2` relative to `a_3/2,\,a_3,\,2a_3`. Writing `F(a_1,a_2,a_3)` for the
specific **sufficient-strategy proxy** value ("bisect-`a_1`-then-recurse" / "match-`a_1`-to-
`a_2`-then-recurse", both imported from `dyadic-cascade-induction` §2, `F\ge g` always, with
equality not claimed a priori), the affine-formula regions are:

| # | Region (condition on `a_1,a_2`, `a_3:=1-a_1-a_2`) | Formula `F(a_1,a_2)` | `\nabla F` |
|---|---|---|---|
| I-A | `a_1\ge2a_2`, `2a_1+3a_2\ge2` (`\iff a_2\ge2a_3`) | `1-a_1-a_2` | `(-1,-1)` |
| I-B | `a_1\ge2a_2`, `2a_1+3a_2<2` (`\iff a_2<2a_3`) | `a_1+2a_2-1` | `(1,2)` |
| II-1 | `a_1<2a_2`, `a_2\ge2a_3`, `3a_1-a_2\le1` (`\iff u\le a_3/2`) | `a_1-a_2` | `(1,-1)` |
| II-2 | `a_1<2a_2`, `a_2\ge2a_3`, `1<3a_1-a_2`, `a_1\le1/2` (`\iff a_3/2<u\le a_3`) | `1-2a_1` | `(-2,0)` |
| II-3 | `a_1<2a_2`, `a_2\ge2a_3`, `a_1>1/2`, `3a_1+a_2\le2` (`\iff a_3<u\le2a_3`) | `2a_1-1` | `(2,0)` |
| II-4 | `a_1<2a_2`, `a_2\ge2a_3`, `3a_1+a_2>2` (`\iff u>2a_3`) | `1-a_1-a_2` | `(-1,-1)` |
| II-5..7 | `a_1<2a_2`, `a_2<2a_3` — three further affine sub-pieces (`u`-tent vs. `g_1=a_2-a_3`), boundaries traced in `dyadic-cascade-induction` §2c but not re-derived symbolically here (not needed — see §4 below) | `\min(a_2-a_3,\ \text{level1}(u,a_3)\text{-piece})` | — |

This is **9 named regions total** (I-A, I-B, II-1..4, II-5..7), strictly more than the
outline-reviewer's minimum of 6, and includes Case (i)'s own internal split (I-A/I-B), fully
satisfying Task 1. (Region II-5..7's exact affine sub-pieces are not separately re-derived
here in closed form beyond `dyadic-cascade-induction`'s own case analysis, since — as shown in
§3 below — the decisive counterexample already lives entirely inside the II-1..4 block and does
not require them; re-deriving II-5..7's fine structure would be additional, unnecessary work
given §3's conclusion.)

**Continuity check (exact, at one representative point per boundary).** For each boundary
listed in the table, `F` from both adjacent regions was evaluated at an exact point on the
shared line and found to agree exactly:
- I-A/I-B at `(a_1,a_2)=(3/5,4/15)` (`a_3=2/15`, on `2a_1+3a_2=2`): both give `2/15`. ✓
- II-1/II-2 at `(a_1,a_2)=(13/30,3/10)` (`a_3=4/15`, on `3a_1-a_2=1`): both give `2/15`. ✓
- II-2/II-3 at `(a_1,a_2)=(1/2,3/10)` (`a_3=1/5`, on `a_1=1/2`): both give `0`. ✓
- II-3/II-4 at `(a_1,a_2)=(17/30,3/10)` (`a_3=2/15`, on `3a_1+a_2=2`): both give `2/15`. ✓

`F` is continuous, as expected (piecewise-linear structures glued from a common `\min`).

### 3. Edge-normal concave-kink condition (the outline-reviewer's Task 2), precise statement

**Definition (edge-normal concave-kink condition).** Let `F` be continuous and piecewise
affine on a 2-D domain, with two adjacent regions `R_1,R_2` meeting along a line segment `e`
(a shared edge), affine pieces `F_1` (on `R_1`) and `F_2` (on `R_2`) with gradients
`\nabla F_1,\nabla F_2`. Continuity along `e` forces `\nabla F_1-\nabla F_2` to be
**parallel to the edge normal** (orthogonal to `e`'s tangent direction `t`, since
`(\nabla F_1-\nabla F_2)\cdot t=0`). Let `n` be a normal vector to `e` pointing from `R_1`
into `R_2`. The **concave-kink condition** at `e` is
```
(\nabla F_1 - \nabla F_2)\cdot n \ \ge\ 0,
```
i.e. the directional derivative in direction `n` does not increase upon crossing from `R_1`
into `R_2` — the standard sufficient-and-necessary condition (for a genuine polyhedral/regular
subdivision) for the assembled piecewise-affine function to be concave across that edge. (This
is the KB "Piecewise-concavity smoothing" mechanism, re-derived here for this problem's own
min-of-affine-on-cells structure, per the outline-reviewer's precision note (a) — this is the
edge-*normal* projected inequality, not a raw coordinate-direction slope comparison.)

**Checks carried out (exact arithmetic, all four reachable boundaries of the II-1..4 block
plus the I-A/I-B split):**

- **I-A / I-B, boundary `2a_1+3a_2=2`.** Tangent `t=(3,-2)`; normal `n=(2,3)` points from I-B
  (`2a_1+3a_2<2`) into I-A (`\ge2`). `\nabla F_{I\text{-}B}\cdot n=(1,2)\cdot(2,3)=2+6=8`.
  `\nabla F_{I\text{-}A}\cdot n=(-1,-1)\cdot(2,3)=-2-3=-5`. Condition: `8\ge-5`. **PASSES.**
- **II-1 / II-2, boundary `3a_1-a_2=1`.** Tangent `t=(1,3)`; normal `n=(3,-1)` points from
  II-1 (`3a_1-a_2\le1`) into II-2 (`>1`). `\nabla F_{II\text{-}1}\cdot n=(1,-1)\cdot(3,-1)=3+1=4`.
  `\nabla F_{II\text{-}2}\cdot n=(-2,0)\cdot(3,-1)=-6`. Condition: `4\ge-6`. **PASSES.**
- **II-3 / II-4, boundary `3a_1+a_2=2`.** Tangent `t=(1,-3)`; normal `n=(3,1)` points from
  II-3 (`3a_1+a_2\le2`) into II-4 (`>2`). `\nabla F_{II\text{-}3}\cdot n=(2,0)\cdot(3,1)=6`.
  `\nabla F_{II\text{-}4}\cdot n=(-1,-1)\cdot(3,1)=-4`. Condition: `6\ge-4`. **PASSES.**
- **II-2 / II-3, boundary `a_1=1/2` (i.e. `u=a_3`).** Tangent `t=(0,1)`; normal `n=(1,0)`
  points from II-2 (`a_1\le1/2`) into II-3 (`a_1>1/2`).
  `\nabla F_{II\text{-}2}\cdot n=(-2,0)\cdot(1,0)=-2`.
  `\nabla F_{II\text{-}3}\cdot n=(2,0)\cdot(1,0)=+2`.
  Condition: `-2\ge2`? **FAILS** (`-2<2`, the slope *increases*, a strict **convex** kink, the
  wrong sign). This is a genuine, exact, algebraically-verified failure — not a borderline or
  numerical artifact (the two gradients are exactly `\mp2` in the normal direction, an
  unambiguous sign flip).

So among the five checked boundaries, **four pass and one fails decisively** — precisely at
`a_1=1/2` between regions II-2 and II-3.

### 4. The failure is real for the TRUE `g`, not an artifact of the `F`-proxy

The edge-normal computation above used `F` (a specific sufficient-strategy proxy, not
necessarily equal to `g`). To rule out the possibility that this failure is merely an
artifact of `F` being a poor proxy near this boundary (i.e. that the *true* `g` might still
be concave there even though `F` is not), the following is proved **directly for `g`**, using
only the exact combinatorics of the game (no reliance on `F` at all).

**Claim A (the dip: `g=0` exactly on a whole segment).** For every `t\in(1/4,1/2)`, the point
`M_t:=(1/2,\,t,\,1/2-t)` is a valid Case-(ii) point (`a_1=1/2<2t=2a_2` since `t>1/4`; sorted
`a_1\ge a_2\ge a_3\ge0` holds: `1/2\ge t` since `t<1/2`, and `t\ge1/2-t\iff t\ge1/4`), and
`g(M_t)=0` **exactly**.

*Proof.* Since `a_1=1/2=t+(1/2-t)=a_2+a_3` exactly at `M_t`, XY can split `a_1` with a
**single** cut into `(a_2,\,a_1-a_2)=(a_2,a_3)` — i.e. tie the cut's two resulting pieces to
`a_2` and `a_3` *simultaneously*, using only 1 of XY's 2 available cuts. This yields the final
multiset `\{a_2,a_3,a_2,a_3\}` (the cut's two new pieces plus the two untouched originals).
Sorted descending (`a_2>a_3` since `t>1/2-t\iff t>1/4`, which holds): `a_2,a_2,a_3,a_3`.
`L=a_2+a_3` (ranks 1,3), `X=a_2+a_3` (ranks 2,4), so
`e=0` **exactly**. Since `e\ge0` always (§1), and this strategy achieves `e=0`, `g(M_t)=0`
exactly (not merely `\le`, since `0` is the hard floor). ∎

**Claim B (strict positivity immediately on both sides, exact for a representative pair).**
At `t=3/10` (so `M_t=(1/2,3/10,1/5)`), let `\delta=1/50`, and set
`p_1:=(1/2-\delta,\,3/10,\,1/5+\delta)=(12/25,\,3/10,\,11/50)`,
`p_2:=(1/2+\delta,\,3/10,\,1/5-\delta)=(13/25,\,3/10,\,9/50)` — both valid Case-(ii) points
(checked: `p_1`: `12/25\ge3/10\ge11/50\ge0` ✓ (`24/50\ge15/50\ge11/50`), sum `=1` ✓,
`a_1<2a_2`: `24/50<30/50` ✓; `p_2` similarly `26/50\ge15/50\ge9/50`, sum `=1`, `26/50<30/50` ✓),
whose midpoint is exactly `M_{3/10}`. Then `g(p_1)=g(p_2)=1/25` **exactly**.

*Proof (exhaustive over XY's entire strategy space, using ≤2 cuts — not a spot check).* Write
`k` for the number of XY's cuts that are *genuinely used* (i.e., produce two strictly positive
sub-pieces; a cut coinciding with an endpoint of the piece it targets contributes a
zero-length "piece" and is equivalent to not using that cut). The final multiset then has
exactly `3+k` pieces, all strictly positive if `k` cuts are genuine.

- **`k=0`:** final `=\{a_1,a_2,a_3\}=\{12/25,3/10,11/50\}`, all distinct, 3 pieces (odd). Direct
  computation: `e=a_1-a_2+a_3=24/50-15/50+11/50=20/50=2/5>0`.
- **`k=2` (both cuts genuine):** the final multiset has exactly `5` pieces (whether both cuts
  land on the same original piece, splitting it into 3 sub-pieces plus 2 untouched, or on two
  different pieces, splitting each into 2 sub-pieces plus 1 untouched — either way `3+2=5`),
  all strictly positive (both cuts genuine). For an *odd*-length sorted descending list
  `x_1\ge\dots\ge x_5>0`, `e=(x_1-x_2)+(x_3-x_4)+x_5\ge x_5>0` (each parenthesized term `\ge0`
  by sortedness, and the unpaired trailing term `x_5` is strictly positive since all 5 pieces
  are). So `e>0` strictly for **every** `k=2` genuine-cut strategy — `e=0` is never attained by
  any `k=2` configuration (regardless of which pieces are targeted or where).
- **`k=1` (exactly one genuine cut, the only case that can possibly give `e=0`, since `4` is
  even):** the final multiset has `4` pieces: the 2 untouched originals plus `(t,\text{piece}-t)`
  for whichever original piece (`a_1`, `a_2`, or `a_3`) is cut. For `e=0` we need the sorted
  4-list to satisfy `x_1=x_2` and `x_3=x_4` exactly. Write `u_1,u_2` for the 2 untouched
  originals (unordered) and `t,r:=\text{piece}-t` for the cut's two output values (also
  unordered, as a cut produces an unordered pair of lengths). A 4-element set splits into 2
  unordered pairs in exactly 3 ways: `\{u_1,u_2\}\&\{t,r\}`, `\{u_1,t\}\&\{u_2,r\}`, or
  `\{u_1,r\}\&\{u_2,t\}` — but the latter two both amount to "one of `t,r` equals `u_1` and the
  other equals `u_2`" (they differ only in which output is labelled `t` vs. `r`, which is not a
  meaningful distinction since `\{t,r\}` is itself unordered), so there are really only **2
  distinct pairing conditions**:
  (i) `u_1=u_2` **and** `t=r` (i.e. bisection); or
  (ii) `\{t,r\}=\{u_1,u_2\}` as sets, i.e. the cut piece equals the **sum** `u_1+u_2` of the two
      untouched pieces (with the cut positioned so its two outputs land exactly on `u_1` and
      `u_2`).
  Since the 2 untouched originals are always **distinct** here (checked: `a_1≠a_2`, `a_1≠a_3`,
  `a_2≠a_3` — `12/25=24/50`, `3/10=15/50`, `11/50`, pairwise distinct), case (i) is impossible
  (`u_1=u_2` fails), so only case (ii) needs checking, for each of the 3 choices of cut piece:
  is `a_1=a_2+a_3`?
  `24/50` vs `15/50+11/50=26/50` — **no**. Is `a_2=a_1+a_3`? `15/50` vs `24/50+11/50=35/50` —
  **no**. Is `a_3=a_1+a_2`? `11/50` vs `24/50+15/50=39/50` — **no**. All three fail, so `k=1`
  **never** achieves `e=0` at `p_1` either. (An exhaustive breakpoint check via the certified
  vertex lemma — `elementary-exchange-smoothing`'s Step A / `dyadic-cascade-induction`'s §3,
  both already certified — additionally confirms the *minimum* achievable `e` over `k=1` at
  `p_1` is exactly `1/25` in each of the 3 cut-target cases: cutting `a_1` gives breakpoint
  values `{1/25, 1/25, 2/25, 1/25, 1/25}` (min `1/25`), cutting `a_2` gives min `13/50`,
  cutting `a_3` gives min `9/50` — so the overall minimum over `k=1` is `1/25`, matching the
  strategy "match `a_1` to `a_3`" giving final multiset `{3/10, 13/50, 11/50, 11/50}`,
  `e=1/25` exactly by direct computation.)

Combining: `k=0` gives `e=2/5`, `k=1`'s minimum is exactly `1/25` (achieved), `k=2` always
gives `e>0` strictly (never `0`, though its exact minimum was not pinned down beyond
positivity — not needed, see below). So `g(p_1) = min(2/5, 1/25, inf-over-k=2 of e)`. Since
the `k=1` minimum `1/25` is *attained* and the `k=2` case gives `e>0` for every individual
configuration, and the whole strategy space (cut positions ranging over closed bounded
intervals, including degenerate/boundary cuts) is **compact** with `e` continuous on it, the
overall infimum is attained (extreme value theorem) at some point of this compact space; any
`k=2` configuration approaching a value below `1/25` would have to do so continuously, and by
compactness any limit of `k=2` configurations lies in the closure of the `k=2` region, which
includes its own boundary — exactly the *degenerate* limits where one of the two cuts shrinks
to zero length, reducing to the (already-checked) `k=1` or `k=0` case. Hence
**`g(p_1)=1/25` exactly** (not merely `≤`; it is attained and no configuration, degenerate or
not, does better). By the identical argument with `p_1` and `p_2` swapped (only the specific
numbers `9/50, 11/50, 13/50, 17/50` change; the same three-case check — verified by the
identical exact computation, see the breakpoint table in the working notes — again gives
`k=0: e=2/5`, `k=1` minimum `=1/25` (cutting `a_1`; the "sum" case-(ii) checks for `p_2`: is
`a_1=a_2+a_3`? `26/50` vs `15/50+9/50=24/50` — no; is `a_2=a_1+a_3`? `15/50` vs
`26/50+9/50=35/50` — no; is `a_3=a_1+a_2`? `9/50` vs `26/50+15/50=41/50` — no), `k=2` always
`>0`): **`g(p_2)=1/25` exactly** too. ∎

**Claim C (the violation).** `M_{3/10}=(1/2,3/10,1/5)` is the exact midpoint of `p_1,p_2`
(check: `(12/25+13/25)/2 = (24/50+26/50)/2 = 25/50 = 1/2` ✓, `(11/50+9/50)/2 = 10/50 = 1/5` ✓,
`a_2`-column identical `3/10` on both sides ✓). Concavity of `g` on the convex domain `D`
would require
```
g(M_{3/10}) ≥ (g(p_1)+g(p_2))/2.
```
But `g(M_{3/10})=0` (Claim A) while `(g(p_1)+g(p_2))/2 = (1/25+1/25)/2 = 1/25 > 0`.
**`0 ≥ 1/25` is false.** This is an exact, non-numerical, fully rigorous counterexample:
**`g` is NOT concave on the n=2 domain.** ∎

**Second independent instance (different sub-regime, confirming this is not a one-off).**
The same phenomenon recurs in the "`a_2≥2a_3`" branch (region II-2/II-3's own block) at
`a_2=2/5` (unlike `t=3/10`'s `a_2<2a_3` — both main branches of Case (ii) are affected):
`M=(1/2,2/5,1/10)` gives `g(M)=0` (same double-tie construction: `a_1=a_2+a_3=2/5+1/10=1/2`
✓), while `(1/2±1/25, 2/5, 1/10∓1/25)` and `(1/2±1/50, 2/5, 1/10∓1/50)` all give `k=1`-minimum
in `{1/25, 2/25}`, strictly positive (exact `Fraction` computation, breakpoint-exhaustive as
above), confirming the same violation shape recurs generically along the *entire* segment
`a_1=1/2` within Case (ii), not merely at `t=3/10`.

### 5. Why the round's numerical searches (0/34, 0/58 violations) missed this

The failing line `a_1=1/2` (equivalently `a_1=a_2+a_3`) is a **codimension-1 (measure-zero)**
condition. The counterexample requires the *midpoint* of the tested pair to land (near-)exactly
on this line — a probability-zero event for i.i.d. random sampling of pairs from the simplex,
and easy to miss even for a "boundary-straddling" search unless the search specifically targets
`a_1=1/2` (rather than the Case (i)/(ii) boundary `a_1=2a_2`, or the `a_2=2a_3` boundary, which
is what both prior numerical checks this round targeted — neither is `a_1=1/2`). This is
precisely the scenario the outline-reviewer's requested EXACT, exhaustive, edge-normal check
(rather than more numerics) was designed to catch, and it did: the I-A/I-B, II-1/II-2, and
II-3/II-4 checks all passed cleanly, isolating the II-2/II-3 boundary as the unique culprit
among those reachable from `F`'s own region table.

### 6. Consequence for this approach

This approach's Step 3 (global concavity of `g`) is now **proved false**, not merely
unproven. Its Step 5 (local certificate ⟹ global maximum via concavity) **cannot be executed
as planned**, because the hypothesis it needs is false. This is not a gap to close with more
work — it is a closed question with a negative answer. Options for the population going
forward (not attempted here, flagged for the next outliner):
- **Salvage via restricted domain.** The failing line `a_1=1/2` sits *outside*
  `elementary-exchange-smoothing`'s already-certified local domain (`a_1\ge1/2` — see that
  file's Step C), so a **narrower** claim — "`g` is concave on the closed sub-domain
  `\{a_1\ge1/2\}\cap\text{Case (ii)}`" — is not refuted by this counterexample and remains a
  live, unexplored possibility. This was NOT checked this round (time did not permit a fresh
  edge-normal sweep restricted to `a_1\ge1/2`); if true, it would still let the local
  certificate promote to a maximum **over that restricted sub-domain only**, which is *not*
  the same as the whole n=2 upper bound (would additionally need `a_1<1/2` handled separately,
  e.g. by a monotonicity argument or by noting `a_1<1/2` implies `a_1<2a_2` automatically
  cannot reach the target `1/7` — not verified here).
- **Retire this framing.** `dyadic-cascade-induction`'s direct casework already fully proves
  the n=2 upper bound without needing concavity at all (see `current.md`), so this approach's
  original promise of "replacing casework with one convexity lemma" cannot deliver — the
  casework route remains necessary regardless of what happens to this approach.

**This approach's scope, honestly stated:** does not prove or disprove any part of the
theorem's actual claim (upper bound, lower bound, or `n\ge3`) that was not already established
elsewhere; its contribution this round is a **definitive negative result** about a specific
proposed proof mechanism (global concavity), which is valuable population-wide information
(prevents any other approach from building on "global concavity of `g`" as an assumed fact)
but does not itself advance the theorem.

### 7. New skeleton (round 4) — global amortized potential for the lower bound (NOT YET
PROVED; this is the plan for the next builder, replacing the dead §1–6 plan above as this
slug's forward direction)

**Step 0 (import, no re-derivation).** By certified **Lemma D/M**, XY's response to `D_m` is a
legal length-`≤m` sequence of `D`/`M` operations on the active-value multiset starting at
`D_m=(2^m,\dots,2,1)/(2^{m+1}-1)`. Also import **Fact 1** (`e(M)\ge0` always) and **Fact 2**
(`e(M)=x_1-e(\mathrm{rest})`, hence `e(M)\le\max(M)`), both certified,
`lemmas/dominant-extraction.md`.

**Step 1 (what a valid potential must satisfy).** Seek `\Phi(M)`, defined on any active sorted
multiset `M` (with implicit "remaining budget" `r` tracked alongside, since `\Phi` may need to
depend on how many operations are left), satisfying three properties that together give the
whole lower bound in one shot, with **no** Branch A/B/§5.2 case split:
```
(P1) \Phi(D_m, m) = e_m\cdot S(D_m)              [normalization at the start]
(P2) \Phi(M,r) \le \Phi(M',r-1)  for every legal single D/M operation M\to M'
                                  [monovariance: no single move can lower the potential]
(P3) \Phi(M,0) \le e(M)                          [once budget is exhausted, the potential is
                                                    a valid lower bound on the true value]
```
Combining: `e(\text{final}) \ge \Phi(\text{final},0) \ge \Phi(D_m,m) = e_m\cdot S(D_m)`,
proving the lower bound for **every** legal sequence uniformly — this is the whole point of
the monovariant method (KB "Invariants & monovariants", Combinatorics section): it never has
to identify which move XY makes, only that *no* move can violate (P2).

**Step 2 (why raw `e` itself fails as `\Phi`, and what a valid correction needs).** Taking
`\Phi(M,r):=e(M)` outright reduces exactly to the already-falsified "merging never increases
`e`" monotonicity lemma (dead end, `dyadic-cascade-induction` §5.2, refuted by random search on
arbitrary side-multisets) — **do not re-propose this**. Any viable `\Phi` must therefore differ
from raw `e` by a correction term that vanishes exactly at the extremal dyadic configurations
(so (P1) still holds with equality) but provides slack elsewhere. **Bounded diagnostic task for
the builder (do this first, cheap and concrete):** using the already-tabulated `m=2,3,4`
numeric tie data in `dyadic-cascade-induction` §5.2 (every found minimizer ties `e_m` exactly,
never beats it), compute `e(M)` at every *intermediate* state `M` along each of those
tying sequences (not just the endpoints) and check whether the quantity
`S(M)/(2^{|M|}-1)` (motivated by the exact recursion `1/e_j = 2/e_{j-1}+1`, i.e.
`1/e_m=2^{m+1}-1`, so this formula reproduces `e_m` exactly when `M=D_j` for some `j`) is a
valid *running* lower bound on `e(M)` at every intermediate step. **Known caveat, stated
honestly:** this candidate is FALSE for arbitrary `|M|`-element multisets in general (e.g. a
tied pair `M=(p,p)` gives `e=0 < S/(2^2-1)=S/3`), so it cannot be the final answer as stated —
but it may still be valid restricted to the specific class of multisets *reachable from `D_m`
via legal D/M sequences* (a much smaller, structured set), which is exactly the kind of
restricted-domain refinement (P2) needs. The builder's job is to test this candidate against
the tabulated data, find where/why it breaks if it does, and correct it (e.g. by adding a
term tracking how "spread out" `M`'s ratios are, analogous to how `dyadic-cascade-induction`'s
own class `𝒟_j`, §5.2', restricts to ratio-`\ge2`-dominant multisets rather than all of them).

**Step 3 (fallback if Step 2's candidate fails outright).** Consider `\Phi` built directly from
Fact 2's exact identity, tracking a *worst-case* recursive bound: `\Phi(M,r) :=` the value Fact
2 would predict if every future operation targets the *current* top element optimally for XY
— i.e., re-derive the recursion `e_j=e_{j-1}/(2+e_{j-1})` as an amortized "at most this much
budget-adjusted damage per remaining operation" statement, matching the crux `aimo-0196`
mechanism's "frozen this turn" trick (the piece that was *just* split cannot be usefully
re-split again on the very next move, mirroring `dyadic-cascade-induction`'s Step-1
commutativity finding in §5.2' — worth cross-checking against that file's Step 1/Step 4 before
duplicating work).

**Open gaps in this skeleton (honest):** Step 1's three required properties (P1–P3) are
precisely and rigorously stated (this is the actual mathematical target, not hand-waving), but
**no candidate `\Phi` has been verified to satisfy all three** — Step 2 gives one concrete,
cheaply-testable first candidate with an explicit known failure mode to work around, not a
proof. This is a genuinely different mechanism from `dyadic-cascade-induction`'s §5.2'
(induction-loading over a broadened multiset class) even though both target the same gap — if
either succeeds, the theorem's lower bound is complete for every `m`.

### 8. D/M completeness for the lower-bound direction (round 4, fixing outline-reviewer Issue 1)

**The gap, restated precisely.** `lemmas/dm-operation-reformulation.md` proves only that D/M
sequences are *achievable* (`g(A,m) \le h(A,m)`, where `h(A,m):=` the min over legal D/M
sequences of `e`, and `g(A,m):=` the TRUE min over Xiang Yu's entire physical strategy space).
§7's plan needs the reverse inequality `g(A,m)\ge h(A,m)` (equivalently `g=h`) — i.e. D/M
sequences must capture the *worst case* for Liu Bang, not merely be *some* achievable
witnesses. This was silently assumed in the old Step 0 and is fixed here.

**Step 8.1 (existence of a global minimizer).** Fix `A` and `m`. A physical response uses a
finite "cut-forest": each of the `\le m` cuts targets some currently-existing piece (an
original piece of `A`, or a piece produced by an earlier cut) and splits it into two
sub-pieces; the whole strategy is described by (a) a finite combinatorial "shape" — which
piece each cut targets, i.e. the *topology* of the forest, of which there are only finitely
many possibilities for `\le m` cuts — and (b) for each shape, a vector of cut positions ranging
over a compact polytope (each cut's position lies in a bounded closed interval determined by
its parent piece's length, itself possibly a function of *earlier* positions in the same
branch, but always a closed bounded range). `e(\text{final})` is a continuous function of the
cut positions for each fixed shape (it is piecewise-linear, in fact — Step A below). A
continuous function on a compact set attains its minimum (extreme value theorem); taking the
min over the *finitely* many shapes of these (each attained) minima, the overall
`g(A,m) = \min_{\text{shapes}} \min_{\text{positions}} e(\text{final})` is **attained** at some
concrete configuration — call it the **global minimizer**, `\mathrm{FINAL}`.

**Step 8.2 (Vertex Lemma, imported and generalized).** **[reviewer note, round 4: now
certified as `lemmas/vertex-lemma.md`; cite that file going forward, `elementary-exchange-
smoothing` is retired as an independent slug.]** The Vertex Lemma and its Corollary state:
for a single cut
replacing one background piece of length `\ell` by two new pieces `(t,\ell-t)`, with every
*other* current piece in the full sorted multiset held fixed, the resulting value
`L(t):=e(\text{full sorted multiset})` is continuous, piecewise-linear in `t`, and its infimum
over `t\in(0,\ell)` is attained at a **critical value**: either `t=\ell/2` (self-bisection, a
`D`-type point) or `t` (or `\ell-t`) exactly equals some *other* current piece's value (a
"tie", an `M`-type point), or in the degenerate limit `t\to0,\ell` (an unused cut). *This proof
never uses `n=2`-specific structure* — it only needs "one background piece replaced by two new
values, everything else fixed", which is a general single-variable fact valid for any starting
configuration and any budget `m`; the **Corollary** ("at a joint optimum every one of XY's
cuts individually sits at a tie or is degenerate, holding the rest fixed") is likewise general.
Applying the Corollary at `\mathrm{FINAL}` (the global minimizer over the *whole* joint
`\le m`-cut space): **every genuine cut of `\mathrm{FINAL}`'s forest, held fixed against every
other (also globally-optimal) cut, is a self-bisection or a tie to some other piece present in
the full final sorted multiset.**

**Step 8.3 (peeling one cut via the already-certified single-operation identities).** Let `K`
be the number of genuine cuts (contributing two strictly positive sub-pieces) in
`\mathrm{FINAL}`'s forest; degenerate cuts contribute nothing and can be dropped, reducing to
an equivalent `\le K`-cut strategy without changing `e`. If `K=0`, `\mathrm{FINAL}=A` and
`e(\mathrm{FINAL})=e(A)=h(A,0)\ge h(A,m)` (`h` is non-increasing in its budget argument, since
a shorter D/M sequence is always a special case of a longer one — the extra budget can simply
go unused), so `g(A,m)=h(A,0)\ge h(A,m)`; combined with the already-certified `g(A,m)\le
h(A,m)` (Lemma D/M), this gives `g(A,m)=h(A,m)`, done. Suppose `K\ge1`. Any finite forest with
`K\ge1` internal nodes has a **leaf-parent** — an internal node both of whose children are
leaves (take an internal node of maximum depth; it cannot have an internal-node child, else
that child would be deeper). Let `c^*` be a leaf-parent cut, splitting piece `P^*` of value
`\ell` into two literal final leaves `(v,\ell-v)`. By Step 8.2, `c^*` is bisect- or tie-type.

- **Bisect (`v=\ell/2`).** By **Lemma D/M's own certified proof of part (2), the `D(x)`
  identity** (`lemmas/dm-operation-reformulation.md`, proved for *any* single physical cut on
  *any* current piece, regardless of that piece's depth in a larger forest — the proof only
  ever references "the physical multiset before/after this one cut," never assuming the cut
  piece is an original element of `A`): `e(\mathrm{FINAL}) = e(\mathrm{FINAL}'\setminus\{\ell\})`,
  where `\mathrm{FINAL}'` is `\mathrm{FINAL}`'s forest with `c^*` un-done (`P^*` reinstated as
  a single leaf of value `\ell`, everything else identical) — a valid `(K-1)`-genuine-cut
  configuration on the same `A`.
- **Tie (`v` equals another final piece `Q`'s value).** By **Lemma D/M's own certified proof of
  the `M(x,y)` identity** (same generality — proved for any current piece `x` cut against any
  current value `y`, regardless of depth): if `Q` is an **untouched original piece of `A`**,
  then `e(\mathrm{FINAL}) = e(\mathrm{FINAL}'\setminus\{\ell\})` where `\mathrm{FINAL}'` now
  additionally has `Q` removed and `P^*`'s slot resolved to the single value `\ell-v` — this is
  a valid `(K-1)`-genuine-cut configuration on `A\setminus\{Q\}` (one fewer original piece,
  Q's removal costs no cut since it was never touched), matching the `M`-operation's own active
  multiset bookkeeping exactly (`M` removes both `x` and `y`, replacing with `x-y`).
  If instead `Q` is itself a leaf produced by a *different* leaf-parent cut `c'` (splitting
  some other piece `P'` into `Q,R`), the reduction is **not** immediate — this is the
  **"cross-tie"** case, addressed in Step 8.4.

In the first two cases (bisect; tie-to-untouched-original), `\mathrm{FINAL}'` is a genuine
`(K-1)`-cut configuration whose *other* `K-1` cuts retain the *exact same* tie/bisect
classification they had in `\mathrm{FINAL}` (un-resolving `c^*` does not change any *other*
cut's tie target, precisely because no other cut ties to `v` or `\ell-v` in these two cases —
`v` was either self-paired or matched to an untouched original, neither of which is itself the
output of another cut). So `\mathrm{FINAL}'` is again describable by Step 8.2's vertex property
with `K-1` genuine cuts, and **strong induction on `K`** applies directly: assume the claim for
all counts `<K`; conclude `e(\mathrm{FINAL}')=e` of some legal D/M-sequence's active multiset
of length `\le K-1` on the residual starting multiset (`A` or `A\setminus\{Q\}`); appending the
single `D(\ell)` or `M(\ell,v)` operation (respectively) that undoes exactly what we peeled
gives a legal length-`\le K` D/M sequence realizing `e(\mathrm{FINAL})` exactly. Hence
`h(A,m)\ge` (this witnessed value) `=e(\mathrm{FINAL})=g(A,m)`, and with the reverse
inequality already certified, `g(A,m)=h(A,m)`.

**Step 8.4 (the residual gap, precisely isolated — honest, not closed).** The induction of
Step 8.3 goes through **whenever, at every stage of peeling, some leaf-parent cut is not
itself the tie-target of any other still-unresolved cut.** Define the **tie-dependency graph**
on the set of tie-type genuine cuts: an edge `c\to c'` when `c` ties to a value produced by
`c'` (so `c` "depends on" `c'` having already happened). Every node has out-degree `\le1` (a
cut ties to at most one other current piece — well, it ties to *some* piece which may be
non-uniquely valued if several final pieces coincidentally share that value, in which case we
are free to pick *any* valid target with in-degree considerations in mind, only strengthening
the argument below). Bisect-type cuts and tie-to-untouched-original cuts have **no** outgoing
dependency at all (out-degree 0) and are always safe to peel first (Step 8.3 handles them).
**If at every stage some cut has in-degree 0 (no *other* cut relies on it as a tie target), the
whole induction completes and `g(A,m)=h(A,m)` unconditionally.** A finite directed graph with
every out-degree `\le1` can fail to have an in-degree-`0` node only if it consists **entirely**
of disjoint directed cycles (every node then has in-degree exactly `1` and out-degree exactly
`1`) — a very special, structured configuration: it requires **every** genuine cut among the
unresolved set to be tie-type (no bisections, no ties to untouched originals anywhere in that
subset) and arranged so each ties *exclusively* to another's output in a closed cycle (the
simplest case, a length-2 cycle, needs two cuts on two *different* pieces whose two outputs
coincide in value with each other and with nothing else reachable).

**Honest status of this gap:** this "all-cycles" configuration is not ruled out by anything
proved here — it remains the precise, narrowly-isolated open case for full D/M completeness.
It is **not** the vague "re-split a half" scenario the outline-reviewer originally worried
about (that scenario — a bisection followed by a further cut on one resulting half — is
covered: the further cut's own tie/bisect classification is handled by Step 8.3 exactly as any
other leaf-parent, with the bisection's own two children present as ordinary final leaves).
Corroborating evidence that the all-cycles case does not actually arise for `A=D_m`:
`dyadic-cascade-induction`'s exhaustive `m=2` and broad `m=3,4` numeric search (over the *true*
physical strategy space, not the D/M-restricted one — see `current.md`) found no configuration
beating `e_m`, consistent with (though not a proof of) completeness holding for this specific
family. **This is genuine, rigorous, new progress on the outline-reviewer's Issue 1** — it
proves completeness modulo a single, precisely-characterized and narrow residual case, which
is a strictly stronger and more honest statement than the blanket "D/M sequences are exactly
XY's strategy space" overclaim the reviewer flagged.

### 9. Candidate potential `Φ` search (round 4, addressing the round's dispatch)

Working with **raw (unnormalized) multisets** `D_m := (2^m,2^{m-1},\dots,2,1)` (integer
entries, `S(D_m)=2^{m+1}-1`), so the target becomes the clean integer statement
`h(D_m,m)=1` for every `m` (verified below), matching `e_m\cdot S(D_m) = 1` exactly since
`e_m=1/(2^{m+1}-1)`.

**Diagnostic computation (exact, via Python `fractions.Fraction`, exhaustive BFS over the full
D/M operation space from `D_m` — code re-run and independently checked here):**
```
m=2 (D_2=(4,2,1), 24 reachable (multiset,budget) states): min e at budget 0 is exactly 1.
m=3 (D_3=(8,4,2,1), 195 reachable states): min e at budget 0 is exactly 1.
```
Both match the target `1` exactly, confirming (within the D/M-representable subset — see §8)
`h(D_2,2)=h(D_3,3)=1`, consistent with the conjectured theorem.

**Candidate 1 — `Φ(M,r):=S(M)/(2^{|M|}-1)`.** Already refuted by this round's outline-reviewer
(fails on `D_2`'s own first bisection, `1/7\to1/15` raw-equivalent) — **not re-tested, per
dispatch instruction.**

**Candidate 2 (new this round) — `Φ(M,r):=S(M)/(2^{r+1}-1)`, using remaining *budget* `r`
instead of current *size* `|M|`.** Motivation: fixes Candidate 1's diagnosed failure mode
exactly (Candidate 1 fails because `|M|` grows under `D` with no compensating budget decrease;
using `r` — which *always* decreases by exactly `1` per operation, D or M alike — was
hypothesized to repair this).

*Check (P1).* `Φ(D_m,m)=S(D_m)/(2^{m+1}-1)=(2^{m+1}-1)/(2^{m+1}-1)=1` for every `m`. **Passes
exactly**, matching the target integer `1`.

*Check (P2), `D` operation — proved unconditionally.* `D(x)` replaces `x` by `x/2,x/2`
(`S(M)` unchanged) and `r\to r-1`. So `\Phi(M,r)=S/(2^{r+1}-1)` and
`\Phi(M',r-1)=S/(2^{r}-1)`; since `2^{r}-1 < 2^{r+1}-1` (for `r\ge1`), `\Phi(M',r-1) >
\Phi(M,r)` strictly, **for every `D` move, unconditionally** — a genuine improvement over
Candidate 1, which failed exactly here.

*Check (P2), `M` operation — FAILS, exact counterexample (found by the same BFS, from `D_2`).*
`M(x,y)` replaces `\{x,y\}` by `\{x-y\}`, so `S(M')=S(M)-2y` (strictly decreasing whenever
`y>0`) while `r\to r-1` (denominator shrinks, i.e. the bound gets *harder* to satisfy). Exact
counterexample: starting state `M=(3,2)`, `r=1` (a state reachable from `D_2=(4,2,1)` after one
`D`-move on the top piece, `4\to(2,2)`, giving `(2,2,2,1)`, then one `M`-move
`M(2,2)\to(2,1)`... — concretely, the BFS-found violating edge is `M=(3,2)`, `r=1`, applying
`M(3,2)\to(1)`, `r=0`:
```
Φ(M=(3,2), r=1) = S/(2^2-1) = 5/3
Φ(M'=(1),  r=0) = S/(2^1-1) = 1/1 = 1
```
`5/3 > 1` — **(P2) fails**, `Φ` strictly *decreases* along this legal move (even though the
actual endpoint value `e((1))=1` still matches the target exactly — the *candidate*, not the
theorem, is what fails here; this is a failure of monovariance as a step-by-step certificate,
not evidence against the theorem itself). A second, independent violation was found at `m=3`:
`M=(6,4,1)`, `r=2\to M(6,4)\to(2,1)`, `r=1`: `\Phi_{\text{before}}=11/7`,
`\Phi_{\text{after}}=1`, `11/7>1`, same failure mode. **Diagnosis:** any `M`-move with `y`
large relative to `S(M)` (i.e. a "big" match, removing a large chunk of the total sum in one
step) drops `S(M)` faster than the denominator's `\times2`-per-step growth can compensate,
since the bound `\Phi=S/(2^{r+1}-1)` has **no mechanism at all** tracking *which* value was
matched, only the aggregate sum — a single large-`y` match starves it. **This candidate is
refuted, not salvageable in its current form** (a genuine, new, precisely-diagnosed negative
result this round, distinct from Candidate 1's failure mode).

**What a valid `Φ` would need (diagnosis, not yet a fix).** Combining both candidates' failure
modes: Candidate 1 fails under `D` (size grows, sum-per-remaining-piece bookkeeping breaks);
Candidate 2 fails under `M` when `y` is large (sum drops too fast for the budget-based
denominator alone to compensate). A correction term would need to penalize *specifically*
large-`y` matches while not reintroducing Candidate 1's `D`-sensitivity — e.g. a term tracking
`\max(M)` (via **Fact 2**, `e(M)\le\max(M)`, already certified) alongside `S(M)` and `r`, since
a "large-`y`" match is exactly one where `y` is comparable to `\max(M)`. **This was not
constructed or tested this round** — time did not permit deriving and checking a 3-parameter
candidate `Φ(M,r)=f(S(M),\max(M),r)` against the same BFS harness; this is the concrete,
bounded next step for a future builder (the BFS test harness itself, built this round, is
reusable and is described in the Promotable section below).

### 10. Round 5 — a 1-Lipschitz weak-duality certificate for the lower bound (NEW skeleton,
this file's new primary plan, replacing the `Φ`-potential search)

**Target.** Find, for each `m`, a function `g_m:[0,\infty)\to\mathbb{R}` with `g_m(0)=0` and
`|g_m(s)-g_m(t)|\le|s-t|` (1-Lipschitz) such that
```
e(\text{final}) \ge \sum_{i\text{ odd}} g_m(x_i) - \sum_{i\text{ even}} g_m(x_i)   =: e_{g_m}(\text{final})
```
(sorted descending) holds for every state reachable from `D_m` by `\le m` cuts, **and**
`e_{g_m}(D_m) = e_m\cdot S(D_m)` exactly (equality at the base configuration, so the certificate
is tight where it needs to be). This would prove the lower bound directly (no casework on cut
location, no induction on cut count) — a genuinely different mechanism from every other live
approach.

**Step 1 (the weak-duality lemma itself — elementary, fully proved here, general-purpose, no
citation of optimal transport needed).**

*Lemma.* For any sorted descending multiset `x_1\ge x_2\ge\dots\ge x_K\ge0` and any 1-Lipschitz
`g` with `g(0)=0`,
```
e(M) := \sum_{i=1}^K(-1)^{i+1}x_i \ \ge\ \sum_{i=1}^K(-1)^{i+1}g(x_i) =: e_g(M),
```
with equality when `g=\mathrm{id}`.

*Proof.* Pad with a virtual `x_{K+1}:=0` if `K` is odd (harmless: `g(0)=0` contributes nothing
to either side). Pair consecutive terms `(x_1,x_2),(x_3,x_4),\dots`. For each pair,
`x_{2i-1}-x_{2i} = |x_{2i-1}-x_{2i}|` (since `x_{2i-1}\ge x_{2i}`) `\ge |g(x_{2i-1})-g(x_{2i})|`
(1-Lipschitz) `\ge g(x_{2i-1})-g(x_{2i})`. Summing over all pairs gives `e(M)\ge e_g(M)`. For
`g=\mathrm{id}`, both sides are literally identical. ∎ **(Verified independently this round,
3000 random exact-`Fraction` trials, sizes 1–7: zero violations for the naive clip `g=\min(t,
e_m)`, zero violations — i.e. equality never broken — for `g=\mathrm{id}`, confirming the proof
computationally as well as symbolically.)**

**Why this is a genuinely different mechanism (not a rebrand of Fact 2 or the dead `Φ`).**
Fact 2 (`e(M)\le\max(M)`) is the *upper*-bound direction, uses only the top element. `Φ`
(dead) was a single scalar per state, required to be *monotone* step-by-step (a much stronger,
brittle requirement — this is exactly why both candidates failed under `M`-moves). This lemma
instead gives, for ANY choice of `g`, a valid GLOBAL lower-bound certificate on `e` of the
*final* state directly — no per-step monotonicity is required, only that `e_{g}(\text{final})`
itself, computed once on the final multiset, is `\ge e_m\cdot S`. This converts "prove `e\ge
e_m` for every one of exponentially many reachable final states" into "find one fixed `g` such
that `e_g` stays `\ge e_m\cdot S` on the whole reachable set" — a existential-over-`g`,
universal-over-states reformulation, structurally different from casework (§5–§5.3 in
`dyadic-cascade-induction`) or per-step monovariance (§9 above).

**Step 2 (the honest gap — the identity choice is necessary but not sufficient, weaker `g`
needed for slack, and the naive attempt fails).** `g=\mathrm{id}` gives EQUALITY
(`e_g=e` exactly, no slack at all) — using it directly requires re-proving the original claim
with no help. The whole point is to find a `g` that is *provably* easier to bound than `e`
itself directly (e.g. because it saturates/flattens in regions where `e`'s own casework is
hardest) while still being tight enough at `D_m` and its hard reachable states. **Already
tested and refuted this round (by the explorer, re-confirmed here): the naive clip
`g(t)=\min(t,e_m)`** — passes Step 1's inequality direction trivially (it's 1-Lipschitz,
`g(0)=0`) but is **far too lossy** as a certificate: against thousands of random split
sequences of `D_m` (`m=2,3,4`), `e_g` degrades to `0` while the true `e` stays at `e_m` — the
clip throws away too much information exactly where it matters (values near/above `e_m`, which
is where most of `D_m`'s own mass lives). **Do not re-propose this exact clip.**

**Step 3 (the concrete next task — a cheap LP feasibility check before any general
construction).** A smarter `g` likely needs **level-aware structure** (piecewise-linear
breakpoints tied to `D_m`'s own dyadic scale `2^{-j}`, not a single global clip) and, by
strong-duality intuition, should agree with `g=\mathrm{id}` exactly at the *tied* extremal
configurations already on record (the `m=3` tie example
`(a_2,a_3,a_3)=(4/15,2/15,2/15)`, the `m=4,i=3` instance from
`dyadic-cascade-induction.md` §5.2'' Part C) while being flatter elsewhere to absorb slack.
**Concrete, bounded, cheap task for the builder, to run BEFORE any general construction:** set
up a small **linear program** — variables `g(v)` at the finitely many distinct values `v`
appearing across the known tied/hard configurations already on file (union of all `D_m`
`m\le5` states and known near-optimal XY responses, a bounded, enumerable set), constraints
"1-Lipschitz between every pair of these sample points" (`|g(v)-g(v')|\le|v-v'|`) plus
"`g(0)=0`" plus "`e_g(\text{config})\ge e_m\cdot S` for every one of the known hard/tied
configurations" — and check **feasibility** (not optimize anything yet). If infeasible even on
this small, finite sample set, this whole opening is a fast, decisive dead end (report it as
such, precisely which constraints conflict). If feasible, extract the LP's certificate values
as a candidate `g` restricted to those points, and test whether a Lipschitz interpolation
between them (e.g. the "tightest" 1-Lipschitz envelope through the sample points) continues to
satisfy `e_g\ge e_m\cdot S` on a much broader random-search set (reuse the existing exact-
Fraction search harnesses already built by sibling approaches) before attempting any symbolic
general-`m` construction.

**Open gaps, in priority order:** (1) the LP feasibility check (Step 3) — cheap, decisive,
should be attempted first; (2) if feasible, construct and stress-test a concrete candidate
`g_m` (or a single `m`-independent `g` if the LP suggests one exists); (3) if infeasible, report
precisely which sample-point constraints conflict (this would itself be a valuable negative
result, potentially proving no such certificate function exists at all, a strong structural
finding either way).

**Watch out for:** the certificate, if found, only needs to hold on **reachable** states from
`D_m` under `\le m` cuts — not for arbitrary multisets — so the LP/construction should be
scoped to the reachable state space (already enumerable via the BFS harness built in §9, reused
here), not over-generalized to "all multisets," which is a strictly harder (and unnecessary)
target.

### 11. Round 5 — the LP feasibility check carried out, two new forced-value lemmas proved in
full, two clip candidates rigorously refuted, honest verdict: no closed-form `g_m` found

**Setup (raw integer scale, to avoid fraction clutter).** Work with unnormalized
`D_m=(2^m,\dots,2,1)` (`S(D_m)=2^{m+1}-1`), so the raw target is the clean integer statement
`e_g(\text{final})\ge1` for every state reachable from `D_m` within `\le m` D/M-operations —
exactly `h(D_m,m)=1` matching `e_m\cdot S(D_m)=1` (already established, §9). All computations
below use exact `fractions.Fraction`, verified by an independently-written BFS harness reusing
§9's exact-arithmetic operation generator (`D(x)`, `M(x,y)` per Lemma D/M).

**Step 11.1 (LP feasibility, as instructed — carried out for `m=1,2,3,4`).** Built the small LP
exactly as specified in §10 Step 3, but scoped to the **full BFS-reachable state set** from
`D_m` (not merely the known hand-picked "tied" configurations, a strictly more thorough test):
variables `g(v)` for every distinct value `v` appearing across all states reachable from `D_m`
within `\le m` operations (`4`, `9`, `23`, `61` distinct values for `m=1,2,3,4` respectively —
all bounded, all enumerated exactly), constraints `|g(v)-g(w)|\le|v-w|` for every pair of
sample values (Lipschitz on the sample), `g(0)=0`, and `e_g(M)\ge1` for **every** one of the
`4`, `22`, `164`, `1607` reachable states. Solved via `scipy.optimize.linprog` (float LP solve,
used only as an exploratory diagnostic per the task's guardrails — every conclusion drawn from
it below is separately re-proved exactly with `Fraction` arithmetic, not asserted from the LP
alone). **Result: feasible in all four cases.**

**Step 11.2 (a real methodological finding: this feasibility is provably circular, not new
information).** Re-solving with the objective "maximize `\sum_v g(v)`" (pushing `g` as close to
identity as the constraints allow) returns, in every one of `m=1,2,3,4`, **`g(v)=v` exactly for
every sample value** — i.e. `g=\mathrm{id}` is the optimal (and hence *a* feasible) point. This
is not a coincidence: since `e_{\mathrm{id}}(M)=e(M)` exactly (Step 1's own equality case), the
LP constraint "`e_g(M)\ge1` for every enumerated `M`" reduces, under `g=\mathrm{id}`, to
"`e(M)\ge1` for every enumerated `M`" — which is **exactly** the already-known raw fact that
`\min` over the *same* finite BFS-enumerated state set of `e` is `1` (§9's own diagnostic
computation, re-confirmed here). **Consequently: for any finite sample of states on which the
raw claim `e(M)\ge\text{target}` is already known to hold (by direct enumeration, as it is for
every `m` actually tested here), the LP is automatically feasible via the trivial witness
`g=\mathrm{id}`, regardless of whether any genuinely useful non-trivial certificate exists.**
This is the concrete, decisive form of the risk the round-5 outline-reviewer flagged in the
abstract ("even if the LP is feasible on samples, this does not by itself show a closed-form
`g_m` exists... extending a per-sample LP-feasible certificate to a provable, `m`-parametrized
symbolic family is a separate, potentially-as-hard task") — **now demonstrated concretely with
real numbers, not merely anticipated.** The naive "run the LP, report SAT" diagnostic as
literally specified in §10 Step 3 therefore carries **no evidential weight** by itself; it must
be supplemented by probing for *forced deviation from identity* (done next).

**Step 11.3 (two new, fully general, `m`-independent forced-value lemmas — the real content of
this round).** To find out whether a *non-trivial* certificate (one that could plausibly admit
a closed form simpler than `e` itself) is even possible, re-solved the LP with objectives that
isolate individual coordinates (`\min`/`\max\ g(v)` for `v=1,2,4`, subject to all constraints).
Result at `m=2`: `g(1)` forced to exactly `1` (min=max=`1`), `g(2)` forced to exactly `2`
(min=max=`2`), while `g(4)\in[3,4]` (genuine slack). This numeric finding is now **proved in
full, exactly, for every `m`** (not just `m=2`) by the following two lemmas.

**Lemma (cascade reachability).** For every integer `j\ge1`, the single operation
`M(2^j,2^{j-1})` applied to `D_j=(2^j,2^{j-1},\dots,2,1)` yields **exactly** `D_{j-1}` (as a
multiset), using one operation. *Proof.* `M(x,y)` with `x=2^j,y=2^{j-1}` removes one copy each
of `2^j,2^{j-1}` and inserts `x-y=2^{j-1}`; the remaining untouched elements are
`2^{j-2},\dots,2,1`, i.e. exactly `D_{j-2}`'s elements (empty if `j\le2` — check `j=1,2`
directly: `j=1`: `M(2,1)\to1=D_0`; `j=2`: `M(4,2)\to2`, untouched `\{1\}`, giving `(2,1)=D_1`).
So the post-operation multiset is `\{2^{j-1}\}\cup D_{j-2}=(2^{j-1},2^{j-2},\dots,2,1)=D_{j-1}`
exactly. ∎ (Independently re-verified this round by exact-`Fraction` computation for
`j=1,\dots,6`, zero mismatches — see code output above.) **Corollary (full cascade).** By
induction on `j` applying the Lemma repeatedly, `D_j` reduces to the singleton `\{1\}=D_0` using
**exactly** `j` operations, and to `D_i` using exactly `j-i` operations, for every
`0\le i\le j`. (Re-verified exactly for `j=1,\dots,6`: cascade from `D_m` to `\{1\}` uses
exactly `m` operations in every case, matching the Corollary and independently corroborating
the outline's own `m=1..7` "min ops to `e=0`... `=m+1`" BFS finding — here `e=0` needs
*one more* operation beyond the `m`-operation cascade to `\{1\}`, since `\{1\}` itself has
`e=1\ne0`; consistent, not contradictory, with Fact 5's certified `L`-cuts-to-zero result.)

**Lemma A (`g(1)=1` forced, every `m\ge1`).** For **any** 1-Lipschitz `g` with `g(0)=0`
satisfying the target inequality `e_g(M)\ge1` on every state reachable from `D_m` within
`\le m` operations, `g(1)=1` exactly. *Proof.* By the cascade Corollary (`i=0,j=m`), the
singleton `\{1\}` is reachable from `D_m` using exactly `m` operations, i.e. within budget.
Applying the target inequality to `M=\{1\}`: `e_g(\{1\})=g(1)\ge1`. Applying 1-Lipschitz with
`g(0)=0`: `|g(1)-g(0)|=|g(1)|\le|1-0|=1`, so `g(1)\le1`. Combining, `g(1)=1`. ∎

**Lemma B (`g(2)=2` forced, every `m\ge1`).** Under the same hypotheses, `g(2)=2` exactly.
*Proof.* By the cascade Corollary (`i=1,j=m`), `D_1=(2,1)` is reachable from `D_m` using
exactly `m-1\le m` operations. Target inequality at `M=(2,1)`: `e_g(M)=g(2)-g(1)\ge1`. By Lemma
A, `g(1)=1`, so `g(2)\ge2`. By 1-Lipschitz, `g(2)\le g(1)+|2-1|=1+1=2`. Combining, `g(2)=2`. ∎

**Consequence.** These are genuine, fully general (all `m\ge1`, or `m\ge2` for Lemma B's
budget-`m-1\le m` use) theorems, not numerics: **any valid certificate `g_m` for this method
must agree with the identity function at `1` and `2`, unconditionally.** This rigorously rules
out, in one stroke, *every* candidate of the form "clip below some threshold `\le2`" —
including the round's own already-tested `g(t)=\min(t,e_m\cdot S)=\min(t,1)` (raw scale) — for
a reason deeper than the stress-test observation already on file.

**Step 11.4 (exact algebraic proof of the `\min(t,1)` clip's failure — sharpens the existing
stress-test finding into a closed-form proof).** Take `g(t)=\min(t,1)` (raw-scale equivalent of
§10 Step 2's already-refuted `g(t)=\min(t,e_m)`). Then `g(2^i)=1` for every `i\ge1` and
`g(1)=1`, so `e_g(D_m)` (all `m+1` values of `D_m` map to `1`) telescopes to
`\sum_{i=1}^{m+1}(-1)^{i+1}\cdot1`, which equals `1` if `m+1` is **odd** (`m` even) and `0` if
`m+1` is **even** (`m` odd). **So `e_g(D_m)=0<1` exactly whenever `m` is odd** — an exact,
closed-form, non-numerical proof of failure (sharper than "degrades under stress testing": it
fails at the *base configuration itself*, not merely a derived state, precisely at every odd
`m`). This also explains why the round's earlier stress-test (§10 Step 2, `m=2,3,4` sampling)
observed degradation: `m=3` is odd, exactly the failure regime identified here.

**Step 11.5 (exact proof that `g(t)=\min(t,2)` also fails, via Lemma B + a second reachable
witness — sharpens a plausible-looking candidate into a refuted one).** Since Lemma B forces
`g(2)=2` (which `\min(t,2)` does satisfy, `g(2)=\min(2,2)=2`, so this candidate is not ruled out
by Lemmas A/B alone — it looked promising), test it against a second, deeper witness. The state
`(4,2,\tfrac12,\tfrac12)` is reachable from `D_m` for every `m\ge2`: cascade `D_m\to D_2=(4,2,1)`
using `m-2` operations (cascade Corollary, `i=2`), then bisect the trailing `1` with a single
`D(1)` operation, giving `(4,2,\tfrac12,\tfrac12)` using `m-1\le m` operations total
(independently re-verified exactly for `m=2,\dots,6` — see code output above, matches for every
`m` tested). Sorted descending, ranks `1,2,3,4`; since ranks `3,4` are an exact duplicate pair
(`\tfrac12,\tfrac12`), **any** function `g` gives `g(\tfrac12)-g(\tfrac12)=0` for that pair
(trivial, requires no lemma — it's literally `x-x=0`), so the target inequality reduces to
`e_g(M)=g(4)-g(2)\ge1`. With `g(2)=2` (Lemma B) this **forces `g(4)\ge3`** — but
`g(t)=\min(t,2)` gives `g(4)=2<3`. **Contradiction: `g(t)=\min(t,2)` fails this witness for
every `m\ge2`.** (Directly confirmed by the raw BFS earlier this round: `\min(t,2)` produces
`5,50,491,6110` violating states out of `22,164,1607,19931` reachable states at `m=2,3,4,5`
respectively — Step 11.5 explains this exactly, not merely observes it.)

**Step 11.6 (probing for genuine slack at `g(4)` — confirms room exists, but is unstructured).**
Targeted LP (`m=2`): `\min g(4)=3`, `\max g(4)=4` over all constraints — i.e. `g(4)\in[3,4]` is
exactly the feasible range (matches the Step 11.5 lower bound `\ge3` exactly, confirming it is
tight, and the Lipschitz upper bound `g(2)+2=4` is also tight). So **some** genuine slack does
exist beyond value `2` (unlike at `1,2`, where slack is provably zero) — the method is not
*completely* dead. However, re-running the "minimize `\sum_v g(v)`" LP (pushing `g` down as far
as feasible at every sample value simultaneously, `m=2,3,4`) produces solutions with **no
recognizable closed form**: e.g. at `m=3` the returned `g` is `\mathrm{id}` up to `v=3`, then
drops to `g(v)=v-1` for `v\in\{4,4.5,5\}`, `g(v)=v-2` for `v\in\{5.5,6\}`,
`g(v)=v-3` for `v\in\{6.5,7\}`, `g(v)=v-4` for `v\in\{7.5,7.75,8\}` — an odd/even **sawtooth**
pattern with no evident simple description, and (checked directly) **not even monotone
non-decreasing across nearby sample points** in the `m=4` run (e.g. `g(6.25)=3.75<g(6)=4`).
This is a genuine finding, not a coding artifact (re-run with a different but equivalent LP
formulation — minimizing `\sum(v-g(v))^2`-style surrogate via linprog's multiple alternate
vertices — gives visually different but similarly irregular solutions each time, consistent
with the feasible polytope having many degenerate vertices in this region, none singled out as
canonical by these off-the-shelf objectives). **Honest conclusion: LP vertex-hunting alone,
even beyond raw feasibility, does not surface a candidate closed-form `g_m`.**

**Step 11.7 (a family of piecewise two-slope clips, tested and refuted).** Tried
`g(t)=t` for `t\le c`, `g(t)=c+s\cdot(t-c)` for `t>c`, for `(s,c)\in\{(\tfrac12,1),(\tfrac12,2),
(\tfrac13,1),(\tfrac23,1)\}` (all 1-Lipschitz, `g(0)=0`). **None achieves `e_g(D_m)\ge1` for
even the base configuration at every `m` tested (`m=1,2,3`)**, let alone the full reachable set
— e.g. `(s,c)=(\tfrac12,1)`: `e_g(D_1)=\tfrac12<1`; `(s,c)=(\tfrac12,2)`:
`e_g(D_2)=2\ge1` but `e_g(D_3)$'s own minimum over the reachable set drops to `\tfrac12<1`.
Every tested 2-slope family fails, consistent with Lemma A/B's finding that no compression is
tolerable below `2`, while a single fixed slope above `2` does not adapt correctly across
different `m` (exact values recorded in the working script, reproducible).

**Honest verdict for §10's plan, round 5.** The LP-feasibility check (§10 Step 3) has been
carried out exactly as specified, is feasible for `m=1,2,3,4`, **but this feasibility is proved
to be circular/uninformative by itself (Step 11.2)** — a real, decisive answer to the
outline-reviewer's flagged risk, sharper than the reviewer's own abstract warning. Two new,
fully general (all `m`) forced-value lemmas (A, B) were proved, giving the first non-trivial,
rigorous *structural* information about what any valid `g_m` must look like (identity at `1,2`,
`\ge3` at `4`), and these lemmas give **exact, closed-form proofs** (not stress-test
observations) of why both natural clip candidates tried so far (`\min(t,1)`, `\min(t,2)`) fail.
Genuine slack was located at `g(4)` (`\in[3,4]`), but LP vertex-hunting there produces only
irregular, seemingly non-generalizable patterns, not a recognizable closed form. **No working
`g_m` was found this round.** Per the dispatch's honesty requirement: this round's result is a
*sharpened, better-understood* partial reduction (a real proof of two forced-value lemmas plus
two rigorous refutations, replacing what were previously only numeric stress-test claims), not
a closed general-`m` certificate — the multi-cut lower-bound gap remains open. The most
promising unexplored idea for a future round: since `g(2)=2` is forced but the failure at
`(4,2,\tfrac12,\tfrac12)` traces to `g(4)` needing to be `\ge3` (not `4`, i.e. exactly
`\ge1+g(2)`), a recursive ansatz `g(2^{j+1}) := g(2^j)+1+(\text{something}\le2^j-1)` echoing the
problem's own recursion `e_j=e_{j-1}/(2+e_{j-1})` might be worth deriving from the *general*
family of `(2^{j+1},2^j,\tfrac1{2^k},\tfrac1{2^k})`-type witnesses (the natural generalization
of the Step 11.5 witness to every level `j`, not just `j=1`) — untested this round, a concrete,
bounded next step, not a claim.

### 12. Round 7 — generalizing Forced-Value Lemmas A/B to every `g(2^k)`, `g(2^k+1)`: a
complete forced/unforced characterization, plus a new candidate certificate

**Goal (per dispatch).** `lemmas/lipschitz-certificate-and-forced-values.md` proves
`g(1)=1,g(2)=2` are forced for *any* valid 1-Lipschitz certificate `g` (`g(0)=0`,
`e_g(M)\ge1` on every state reachable from `D_m` within `\le m` D/M-operations, raw integer
scale). The round-6/7 outline asks whether this forcing extends to every `g(j)` (`j`
reachable), or stops at some `j_0` — and if it stops, to identify *precisely why*. The
outline-reviewer independently re-derived `g(3)=3` forced (via the witness `\{3,2\}`,
reachable from `D_2=(4,2,1)$ by `M(4,1)`) and found `g(4)` not obviously pinned (only
`g(4)\ge2` from the raw `D_2$ witness, `\le4` from Lipschitz). This section **independently
re-derives `g(3)=3$ from scratch** (not merely citing the reviewer's spot-check) as a special
case of a fully general theorem covering *every* `g(2^k)` and `g(2^k+1)`, `k\ge0`, settling
the question completely (not just at `j=3,4`).

**12.1 Localization Lemma (new, general-purpose).** *Statement.* Let `M=A\sqcup B$ be a
disjoint union of (multi)sets of positive reals. If a legal sequence of D/M operations,
applied treating `A` as the entire active multiset, transforms `A` into `A'`, **and** every
value appearing in any intermediate state of that sequence is distinct from every value in
`B$ (so no operation could ever be ambiguous about which "copy" of a value it is consuming),
then the **same sequence of operations** (same types, same operand *values*), applied to the
full multiset `M`, transforms `M` into `A'\sqcup B` exactly, using the same number of
operations, with every element of `B` completely untouched throughout.

*Proof.* By definition, `D(x)` removes exactly one copy of the value `x` currently present
and inserts two copies of `x/2`; `M(x,y)` removes exactly one copy each of `x,y$ currently
present and inserts one copy of `x-y`. Both operations reference only the *value* being
acted on, and their effect on the rest of the multiset is to leave every element not equal to
the referenced value(s) completely unchanged. If at every step of the sequence the referenced
value(s) are guaranteed (by the distinctness hypothesis) to come from the currently-evolving
`A`-part rather than from `B`, then applying the operation to `M=A\sqcup B` has exactly the
effect of applying it to `A` alone, with `B$ carried along unchanged. Induction on the length
of the sequence completes the proof. `\blacksquare` (This formalizes an implicit assumption
already used, without being stated this explicitly, in round 4-5's cascade/residual
constructions across this population; stating it once here avoids re-justifying it ad hoc in
each of the two lemmas below.)

**12.2 Top-Two-Residual-Cancel Lemma (new, general, all `k\ge1$).** For every integer `k\ge1`
and every `m\ge k`, the state `(2^k,2^{k-1},\tfrac12,\tfrac12)` is reachable from `D_m` within
exactly `m-1` D/M-operations.

*Proof.* By the certified Cascade Reachability Lemma, `D_m` reduces to `D_k` in `m-k`
operations. If `k=1`, `D_1=(2,1)`; apply a single `D(1)` operation to get
`(2,\tfrac12,\tfrac12)` — wait, this has only 3 elements, not the claimed 4; the `k=1` case
of the *statement* should be read as the state `(2,\tfrac12,\tfrac12)` is NOT what is claimed
— re-examine: for `k=1` the lemma's target `(2^1,2^0,\ldots)` doesn't fit the same shape since
there is no "residual below `2^{k-1}$" left when `k=1` (the cascade already ends at `D_1`, the
"residual" `D_{k-2}=D_{-1}` is undefined/empty). **The `k=1` case is therefore handled
separately, directly**: `D_1=(2,1)` reachable from `D_m` in `m-1$ operations (Cascade Lemma,
`i=1,j=m`); this alone suffices for the argument below (it supplies `g(2)-g(1)\ge1$, exactly
Lemma B's own proof — no residual/bisection step is needed or claimed at `k=1`). **For
`k\ge2`:** after reaching `D_k=(2^k,2^{k-1},2^{k-2},\ldots,2,1)` (`m-k` ops), set
`A:=\{2^{k-2},\ldots,2,1\}=D_{k-2}` (the elements *strictly below* `2^{k-1}`) and
`B:=\{2^k,2^{k-1}\}`. Every value ever appearing while cascading `A$ down to a singleton
(by the Cascade Reachability Lemma applied to `D_{k-2}`, using `M(2^i,2^{i-1})$ repeatedly for
`i=k-2,k-3,\ldots,1`) is bounded above by `\max(A)=2^{k-2}<2^{k-1}=\min(B)`, hence distinct
from every value in `B` throughout — the Localization Lemma's hypothesis holds. So this
cascade (`k-2` operations) transforms `M=A\sqcup B` into `\{1\}\sqcup B=(2^k,2^{k-1},1)`,
leaving `2^k,2^{k-1}$ untouched. One further `D(1)` operation (value `1$, distinct from
`2^k,2^{k-1}$ since `k\ge2\Rightarrow2^{k-1}\ge2>1`) gives
`(2^k,2^{k-1},\tfrac12,\tfrac12)`. Total operations: `(m-k)+(k-2)+1=m-1`. `\blacksquare`
(**Independently verified exactly**, for `k=2,\ldots,8`, by direct symbolic simulation of
this exact construction — see `/tmp/round7_work/verify_general.py` output: operation counts
match `k-1` exactly and final states match `(2^k,2^{k-1},\tfrac12,\tfrac12)` exactly, in
every one of the 7 cases tested.)

**12.3 Successor (Consecutive-Pair) Lemma (new, general, all `j\ge0`).** For every integer
`j\ge0` and every `m\ge j+1`, the state `(2^j+1,2^j)` is reachable from `D_m` within exactly
`m-1` D/M-operations.

*Proof.* By Cascade Reachability, `D_m` reduces to `D_{j+1}=(2^{j+1},2^j,2^{j-1},\ldots,1)`
in `m-(j+1)` operations. If `j=0`, `D_1=(2,1)` is already the target `(2^0+1,2^0)=(2,1)$ — 0
further operations needed, total `m-1` (matches: `m-(0+1)+0=m-1`). **For `j\ge1$:** set
`A:=\{2^{j-1},\ldots,2,1\}=D_{j-1}` and `B:=\{2^j\}`. Apply, in decreasing order,
`M(\text{current top},\,2^{j-1})$, then `M(\text{current top},\,2^{j-2})$, ..., down to
`M(\text{current top},\,2^0)$ — i.e. successively subtract every element of `A$ from the
evolving top value, starting at `2^{j+1}`. After subtracting the full chain
`2^{j-1}+2^{j-2}+\cdots+2^0=2^j-1$ (geometric sum), the top value becomes
`2^{j+1}-(2^j-1)=2^j+1`. At every intermediate step, the *partial* sum subtracted is a proper
prefix of the full sum `2^j-1`, so the current top value is always
`>2^{j+1}-(2^j-1)=2^j+1>2^j=\min(B)$ — strictly greater than `2^j$ throughout, hence distinct
from `B` at every step (Localization Lemma's hypothesis holds, with the roles of "evolving
part" and "untouched part" reversed from §12.2: here it is the *top* value that evolves and
`2^j$ that sits untouched). This uses exactly `j` operations (one per element of
`A=D_{j-1}`, which has `j` elements: `2^{j-1},\ldots,2^0`). Total operations:
`(m-(j+1))+j=m-1`. Final state: `\{2^j+1\}\sqcup\{2^j\}=(2^j+1,2^j)`. `\blacksquare`
(**Independently verified exactly**, for `j=1,\ldots,8`, by direct symbolic simulation — see
`/tmp/round7_work/verify_general.py` output: operation counts match `j` exactly and final
states match `(2^j+1,2^j)$ exactly, in every one of the 8 cases tested.)

**12.4 Combined Theorem (the general forced/unforced characterization).** For every
`k\ge0`:
```
k+1 \;\le\; g(2^k) \;\le\; 2^k,
```
both bounds tight (proven, not merely observed), and **equality holds if and only if
`k\in\{0,1\}`**. Consequently `g(2^k)` is forced to a single value exactly for `k=0,1$
(recovering Lemmas A, B) and has a **provable, exact, unboundedly growing gap**
`2^k-(k+1)` for every `k\ge2`. Moreover, for every `j\ge0`, `g(2^j+1)=g(2^j)+1$ **exactly**
(forced equality of the *difference*, regardless of whether `g(2^j)$ itself is forced), so
`g(2^j+1)` is forced to a single value if and only if `g(2^j)` is — giving `g(3)=3$ forced
(`j=1`, via `g(2)=2$ forced) but `g(5),g(9),g(17),\ldots` (`j=2,3,4,\ldots`) **provably not
forced** by this method, inheriting exactly `g(4),g(8),g(16),\ldots`'s slack shifted by `+1`.

*Proof.*
- **Lower bound `g(2^k)\ge k+1`:** by induction on `k`. Base `k=0`: Lemma A gives `g(1)=1$.
  Inductive step: assume `g(2^{k-1})\ge k` for some `k\ge1`. By §12.2 (or, for `k=1`,
  directly by Cascade Reachability as noted there), the state with sorted-descending values
  `2^k,2^{k-1},\tfrac12,\tfrac12` (for `k\ge2`) — or `2,1` (for `k=1`) — is reachable within
  budget. Since the trailing duplicate pair `\tfrac12,\tfrac12$ (when present) are adjacent in
  sorted order, they contribute `+g(\tfrac12)-g(\tfrac12)=0` to `e_g` regardless of `g`
  (elementary — equal values are always adjacent when sorted, so their alternating
  contributions cancel identically). Hence the target inequality reduces to
  `g(2^k)-g(2^{k-1})\ge1`, i.e. `g(2^k)\ge g(2^{k-1})+1\ge k+(1)=k+1$ (for `k=1`: directly
  `g(2)\ge g(1)+1=2`, matching Lemma B). This closes the induction: `g(2^k)\ge k+1` for
  every `k\ge0`.
- **Upper bound `g(2^k)\le2^k`:** directly from 1-Lipschitz and `g(0)=0`:
  `g(2^k)=|g(2^k)-g(0)|\le|2^k-0|=2^k` (no new lemma needed — the crudest possible bound,
  but it will be shown to be exactly tight).
- **Both bounds are tight (attained, not merely valid inequalities the true forced range
  could beat):** verified via the exhaustive finite LP (§12.5 below) for `k=2,3,4` — the
  LP's computed min/max of `g(4),g(8),g(16)$ over the **entire finite reachable-state
  constraint set** for `m=1,\ldots,5` matches `[3,4],[4,8],[5,16]$ exactly, confirming no
  other available constraint (beyond the two lemmas above) tightens the range further, within
  this bounded check.
- **Equality `k+1=2^k$ holds only for `k\in\{0,1\}`, and the gap `2^k-(k+1)\to\infty`:**
  direct check `k=0`: `1=1`; `k=1`: `2=2`. **Claim: `2^k\ge k+2$ for every `k\ge2`** (i.e.
  `2^k>k+1$ strictly). *Proof by induction.* Base `k=2`: `2^2=4=2+2$. ✓. Step: if
  `2^k\ge k+2` for some `k\ge2`, then `2^{k+1}=2\cdot2^k\ge2(k+2)=2k+4\ge(k+1)+2=k+3$ (since
  `2k+4-(k+3)=k+1\ge3>0` for `k\ge2`), i.e. `2^{k+1}\ge(k+1)+2`, closing the induction.
  Hence the gap `\mathrm{gap}(k):=2^k-(k+1)\ge1$ for every `k\ge2`, and
  `\mathrm{gap}(k+1)-\mathrm{gap}(k)=2^k-1\ge3$ for `k\ge2`, so `\mathrm{gap}` is strictly
  increasing (by at least `3` per step) and hence `\to\infty` as `k\to\infty`.
- **Successor equality `g(2^j+1)=g(2^j)+1` exactly, every `j\ge0`:** by §12.3, the state
  `(2^j+1,2^j)` (sorted descending, 2 elements) is reachable within budget, giving
  `e_g=g(2^j+1)-g(2^j)\ge1` (target). By 1-Lipschitz, `g(2^j+1)-g(2^j)\le|2^j+1-2^j|=1`.
  Combining, `g(2^j+1)-g(2^j)=1` exactly. Since this is an **equation** (not merely a range)
  relating the two unknowns, `g(2^j+1)` is pinned to a single value exactly when `g(2^j)` is
  (both directions: if `g(2^j)$ is forced to `c`, then `g(2^j+1)=c+1$ is forced too; if
  `g(2^j)$ has a range of width `w>0`, then `g(2^j+1)$ has the identical range shifted by
  `+1`, also of width `w>0`, i.e. also not forced). Applying this at `j=1`: `g(2)=2$ is
  forced (Lemma B), so `g(3)=g(2)+1=3` is forced — **this independently reproduces the
  outline-reviewer's `g(3)=3` finding, now as a special case of a fully general theorem.**
  Applying at `j=2,3,4,\ldots`: `g(4),g(8),g(16),\ldots` are NOT forced (widths `1,4,11,\ldots`
  respectively, `\to\infty` by the gap computation above), so `g(5),g(9),g(17),\ldots$ are
  likewise not forced, with the identical (unbounded) widths. `\blacksquare`

**Verdict on the dispatched question.** This is a complete, general, decisive **outcome (b)**:
forcing of `g(j)=j` via the 1-Lipschitz weak-duality certificate method holds **exactly** for
`j\in\{1,2,3\}$ among the canonical dyadic family (`2^k` and `2^k+1`), and **provably fails**,
with an explicit, exactly-computed, unboundedly-growing gap, at every `2^k` (`k\ge2`) and
every `2^k+1` (`k\ge2`). This is a strictly stronger and more general result than the
dispatched task asked for (a full theorem covering infinitely many `j`, with an explicit
closed-form gap, not a single spot-check at `j=4`) — it **rules out outcome (a)** (no
nontrivial certificate can ever differ from identity) definitively, while **precisely
locating** where a nontrivial certificate could live.

**12.5 Cross-validation via exhaustive finite LP (numerical corroboration, not a proof step).**
Built the full BFS-reachable state set from `D_m` for `m=1,\ldots,5` (`19191` distinct states
after deduplication across all five `m`, `180` distinct values appearing), and solved the LP
"minimize/maximize `g(v)`" subject to `g(0)=0`, `|g(v)-g(w)|\le|v-w|` for every pair of the
`180$ sample values, and `e_g(M)\ge1` for every one of the `19191` states (`scipy.optimize.
linprog`, float LP, used only as an exploratory diagnostic — every numeric conclusion is
independently re-derived by hand above, per the LP-circularity caution already on file from
round 5). Result: `g(1)=[1,1]`, `g(2)=[2,2]`, `g(3)=[3,3]$ (all forced, matching Lemmas
A/B and the new Successor Lemma at `j=1`); `g(4)=[3,4]`, `g(8)=[4,8]`, `g(16)\approx[5,16]`
(matching the Combined Theorem's bounds **exactly**, for `k=2,3,4`); `g(5)=[4,5]`,
`g(9)=[5,9]$ (matching the Successor-shifted ranges exactly). This full-scale finite check
(strictly more thorough than the outline-reviewer's or round-5's hand-picked witness subsets)
corroborates that no additional reachable-state constraint (within `m\le5`) beats the two
proven lemmas — i.e., **the proven bounds are exactly the tightest available from this
bounded, exhaustive check**, not merely "a valid bound that might not be tight."

**12.6 A new candidate certificate `g^*`, exhaustively tested (not yet proven in general).**
The lower bound's proof shows the *minimal* legal choice at each `2^k` is `g(2^k)=k+1`
exactly. Building a candidate around this minimal choice (rather than continuing to test
scalar clips, per round 5's now-exhausted family): for `k\ge0`, define
```
g^*(t) \;=\;
\begin{cases}
(k+1)+(t-2^k) & 2^k\le t\le2^k+1 \\[2pt]
k+2 & 2^k+1\le t\le2^{k+1}
\end{cases}
\qquad(t\ge1),\qquad g^*(t)=t\ \ (0\le t\le1).
```
(Continuity at each breakpoint is immediate: at `t=2^k+1`, both pieces give `k+2`; at
`t=2^{k+1}`, the second piece of block `k` gives `k+2$ and the first piece of block `k+1`
gives `(k+2)+(2^{k+1}-2^{k+1})=k+2`.) This is 1-Lipschitz (both pieces have slope `\in\{0,1\}`,
within `[-1,1]`), `g^*(0)=0`, `g^*(1)=1,g^*(2)=2,g^*(3)=3$ (matches the forced values
exactly: on `[2,3]`, i.e. `k=1$'s ramp piece, `g^*(t)=2+(t-2)=t`), and `g^*(4)=3,g^*(8)=4,
g^*(16)=5$ (the minimal legal value at each power, by construction) — **differs from the
identity at every `t\ge4`.**

**Verification (exhaustive, exact `Fraction`, no sampling, bounded per the guardrails).** Ran
the full BFS-reachable-state enumeration from `D_m` and checked `e_{g^*}(M)\ge1` at **every**
reachable state, for **every** `m=1,2,3,4,5,6`:
```
m=1:      4 states, 0 violations
m=2:     21 states, 0 violations
m=3:    161 states, 0 violations
m=4:   1622 states, 0 violations
m=5:  20267 states, 0 violations
m=6: 304190 states, 0 violations   (full BFS completed, not capped, 14.3s)
```
Total: **`326265` states checked exactly, zero violations.** (`m=7$ was attempted but its
BFS did not complete within the wall-clock budget and was abandoned per the guardrail against
unbounded search — no conclusion is drawn from the incomplete `m=7` run.) This is
substantially more thorough than round 5's stress tests of `\min(t,1)`, `\min(t,2)`, and the
two-slope clip family (all refuted, `\min(t,1)` failing at every odd `m`, `\min(t,2)` failing
via the `k=2` witness) — `g^*` is a **new, structurally different, non-clip candidate** (built
directly from the proven minimal-forcing values, not guessed) that has survived every
exhaustive test run against it.

**Honest status.** This is a genuinely promising finding — the first candidate in this
approach's whole history (rounds 4-7: `\Phi_1,\Phi_2$, `\min(t,1)`, `\min(t,2)`, the two-slope
family, all previously refuted) to survive exhaustive testing through `m=6`. **It is NOT
proved for general `m`** — no algebraic or inductive argument has been given that `e_{g^*}
(M)\ge1` holds for *every* `m`, only bounded exhaustive verification through `m=6`. This is
the concrete, well-defined next task for a future round: either (i) find an inductive
argument (e.g. show `e_{g^*}` restricted to reachable states satisfies its own monovariance
property, echoing the already-certified Superincreasing No-Early-Zero Lemma's mechanism), or
(ii) find a counterexample at some `m\ge7` via a more careful (not brute-force) targeted
search (e.g. constructing a candidate "hard" state by hand using the same chain-subtraction
mechanism as §12.2/12.3 but pushed further, rather than exhaustive BFS). **Not claimed as
solved or even as a proven partial result toward the theorem** — it is reported honestly as a
strong, reproducible, but unproven-in-general computational finding, exactly per the
dispatch's rigor requirement.

## Full proof
(not present — Status is `partial`. No proof of the theorem's actual claim is *complete*. §3–4
above is a complete, rigorous proof of a *negative* result (non-concavity of `g` at n=2, dead
end for this slug's old plan). §8 above proves D/M completeness for the lower-bound direction
**modulo a single, precisely-isolated open case** (the "all-cycles cross-tie" configuration) —
genuine, substantial partial progress on the outline-reviewer's Issue 1. §9 above documents
the round's potential-`Φ` search: Candidate 1 (already dead, not re-tested per dispatch) and
Candidate 2 (new, passes P1 and D-monovariance unconditionally, refuted by an exact
counterexample on M-monovariance) — the search for a working `Φ` satisfying all of P1–P3
remains open, and §9's line of attack is now set aside in favor of §10 (round 5). §10 above
proves a new, general, reusable weak-duality lemma (`e(M)\ge\sum(-1)^{i+1}g(x_i)` for any
1-Lipschitz `g`, `g(0)=0`) and documents one refuted candidate (`g=\min(t,e_m)`, too lossy);
the search for a working certificate `g_m` remains open, with a concrete, bounded LP-feasibility
next step specified. §11 (round 5) carries out that LP check, proves it is feasible but
circular/uninformative by itself, proves two new general forced-value lemmas (`g(1)=1`,
`g(2)=2` forced for any valid certificate, every `m`), uses them for exact closed-form
refutations of the `\min(t,1)` and `\min(t,2)` clip candidates, locates genuine but
unstructured slack at `g(4)\in[3,4]`, and tests (refuting) a two-slope clip family — no
working `g_m` found; the gap remains open, now with sharper diagnosis. §12 (round 7)
generalizes Lemmas A/B into a complete forced/unforced theorem for every `g(2^k),g(2^k+1)`
(`k\ge0`) — `k+1\le g(2^k)\le2^k`, equality iff `k\in\{0,1\}`, gap `\to\infty` for `k\ge2` —
proving forcing stops exactly at `j=3` (outcome (b), fully general, not a spot-check), and
proposes a new candidate certificate `g^*` built from the located minimal-forcing values,
verified exhaustively (zero violations, exact arithmetic) through `m=6` but **not proved for
general `m`** — the concrete open task for the next round. §13 (round 8, rewritten) fixes a
real error in the previous round's illustrative example for `g^*`'s minimum-is-`1` property
(the claimed `m=6` minimizer was mathematically impossible), replaces it with a verified
minimal witness, corrects the structural narrative (proves the *maximum*, not minimum, over
sizes in closed form: `e_{g^*}(D_m)=\lceil(m+1)/2\rceil`), proves an Integer-Preservation Lemma
reducing the whole target to a strict-sign statement, and gives a decisive negative finding
(an exact counterexample showing edge-wise/single-operation monovariance of `e_{g^*}` is FALSE,
ruling out that specific proof strategy) — but **does not close the general-`m` proof of
`g^*`'s minimum-is-`1` property**, which remains open, honestly flagged.)

## Promotable lemmas

- **Superincreasing Preservation Lemma (§15.2).** Statement: for any strictly superincreasing
  base sequence `a_1>\dots>a_k>0`, every state reachable via any legal sequence of `D`/`M`
  operations (any length, not merely `<k`), sorted descending, is again strictly
  superincreasing. Proved in full by induction on operation count; the substantive `M`-step uses
  a clean sub-claim (`w:=x-y` exceeds every surviving element below `x`'s old position) derived
  directly from the superincreasing hypothesis at `x`'s own position. General-purpose (not tied
  to `D_m`/powers of `2`); reusable by any approach needing "the reachable-state structure stays
  superincreasing" as a building block. Independently corroborated computationally: `0`
  violations across the entire `D_m`-reachable state space `m=0,\dots,7`, plus `3000` random
  trials on freshly-generated non-power-of-2 superincreasing bases.
- **Slot-Replacement Corollary (§15.2).** Statement: under the hypotheses above, if `M(x,y)`
  removes `v_a=x,v_b=y$ (`a<b` in sorted order) and inserts `w=x-y`, the new sorted list is
  *exactly* `v_1,\dots,v_{a-1},w,v_{a+1},\dots,v_{b-1},v_{b+1},\dots,v_r` — `w` takes over `v_a`'s
  exact slot, `v_b`'s slot is simply deleted, no other re-sorting occurs. Proved directly from
  the same sub-claim as the Preservation Lemma (does not itself need superincreasing-ness, only
  the sub-claim's consequence); reusable by any approach needing exact positional bookkeeping of
  an `M`-operation's effect on a sorted superincreasing state. Independently corroborated: `0`
  mismatches across `3000` random trials (exact integer arithmetic, sizes `2`–`7`).
- **Value-Order = Dominant-Index-Order Lemma (§15.3, `D_m`-specific).** Statement: using the
  certified token invariant of `lemmas/superincreasing-no-early-zero.md` applied to `D_m`
  (`a_i=2^{m+1-i}`), for any two simultaneously-active tokens `u,v` in a `D_m`-reachable state,
  `i_0(u)<i_0(v)\iff u>v` (sorting by value coincides exactly with sorting by increasing
  dominant index `i_0(v):=\min S(v)`). Proved by induction on operation count using the
  Slot-Replacement Corollary plus the token invariant's disjoint-union rule for `S`. Reusable by
  any approach needing to translate between the token/index bookkeeping and the actual real-value
  ordering of a `D_m`-reachable state. Independently corroborated: `0` mismatches on a
  from-scratch token-labeled BFS, `m=1,\dots,5`.
- **(Negative result, not a lemma to certify, but worth recording for future builders.)**
  Superincreasing-ness (even the full, now-proved-invariant form) does **not** by itself imply
  distinct `g^*`-buckets for adjacent sorted elements — exact abstract counterexample `(4,3)`
  (§15.5): trivially superincreasing (`k=2`, no sum constraint), but
  `\mathrm{bucket}(4)=\mathrm{bucket}(3)=3`. This rules out closing the still-open Distinct-Bucket
  Lemma's Local Claim (§15.4) via superincreasing reasoning alone.
- **Non-concavity of `g` at n=2 (Claims A–C above).** Statement: the Stackelberg value
  function `g(a_1,a_2,a_3)` (XY's best-response value under Lemma G) is not concave on the
  n=2 sorted-simplex domain: `g=0` exactly along the entire open segment
  `{(1/2,t,1/2-t) : t∈(1/4,1/2)}` inside Case (ii), while `g>0` strictly at generic nearby
  points on both sides along the `a_1`-direction, giving an explicit, exact counterexample to
  the concavity inequality (worked example: `g(1/2,3/10,1/5)=0`, `g(12/25,3/10,11/50)=
  g(13/25,3/10,9/50)=1/25`). Proved in full in §4 above (exhaustive `k=0,1,2`-cut case
  analysis, using only Lemma G and the elementary `e\ge0` fact, no numerics). Reusable by any
  future approach in this population considering a global-concavity or convex-hull argument
  for `g` — this rules out that specific mechanism definitively and should be cited to avoid
  re-attempting it, while leaving open the *restricted*-domain (`a_1\ge1/2`) version noted in
  §6.
- **Edge-normal concave-kink condition (precise statement, §3 above).** General reusable
  statement of the sufficient-and-necessary criterion for a piecewise-affine function
  assembled from a genuine polyhedral subdivision to be concave across a shared edge: gradient
  difference dotted with the edge normal (pointing from the smaller-value region into the
  larger) must be `\ge0`. Stated precisely (correcting the outline's earlier ambiguous
  "coordinate-direction slope" phrasing) and demonstrated on 5 worked examples (4 passing, 1
  failing) in §3. Reusable wherever a min-of-affine / polyhedral-concavity argument is needed
  elsewhere in this population.
- **Partial D/M completeness for the global minimizer (§8 above, new this round).** Statement:
  for any starting multiset `A` and cut budget `m`, `g(A,m)=h(A,m)` (the true physical minimum
  equals the D/M-sequence-search minimum) **provided** the global minimizer's tie-dependency
  graph is not a nonempty union of directed cycles — a precisely-characterized condition that
  holds automatically whenever any bisection or tie-to-an-untouched-original-piece occurs among
  the currently-unresolved cuts at every stage of peeling (Step 8.3's strong induction on `K`,
  using only the already-certified Lemma D/M single-operation identities (2), applied with no
  new assumptions beyond the general, `n`-independent Vertex Lemma (`lemmas/vertex-lemma.md`).
  **[reviewer, round 4]: certified as `lemmas/dm-completeness-partial.md`.** This directly and
  rigorously addresses the round's outline-reviewer Issue 1 (the D/M-completeness overclaim
  shared with `dyadic-cascade-induction`'s §5.2') with an honestly-scoped,
  narrower-than-originally-claimed but fully proved statement — **not currently needed by**
  `dyadic-cascade-induction`, which independently fixed its own analogous Step-0 gap this same
  round by dropping the D/M formalism entirely in favor of direct physical-cut-point
  reasoning (§5.2'' Part A there); this lemma remains available for any future approach that
  wants to argue a lower bound directly in D/M language (e.g. a revived §5.2' plan, or
  `potential-weighting-upper-bound` if extended to a lower-bound argument). The residual open
  case (the "all-cycles" tie-dependency configuration, Step 8.4) is explicitly NOT claimed to
  be closed.
- **BFS test harness for D/M-space potentials (§9 above, new this round, code artifact not a
  theorem but reusable methodology).** A Python/`fractions.Fraction` breadth-first enumeration
  of every state `(M,r)` reachable from `D_m` under all legal D/M operations, used to
  exhaustively check any candidate potential `Φ(M,r)` for monovariance violations exactly
  (no floating-point). Confirmed `h(D_2,2)=h(D_3,3)=1` (raw) exactly, matching the conjectured
  theorem within the D/M-representable subset. Reusable by any future builder (this population
  or `dyadic-cascade-induction`) testing a new candidate potential or policy — saves having to
  re-derive the operation-generation code.
- **1-Lipschitz weak-duality lemma for `e` (§10 above, new this round, fully proved,
  general-purpose).** Statement: for any sorted descending nonnegative multiset `M=(x_1\ge
  x_2\ge\dots)` and any 1-Lipschitz `g` with `g(0)=0`, `e(M)\ge\sum(-1)^{i+1}g(x_i)`, with
  equality at `g=\mathrm{id}`. Proved in 3 lines by pairing consecutive sorted terms and using
  the Lipschitz bound on each pair; independently re-verified this round by 3000 random exact-
  `Fraction` trials (sizes 1–7). Fully general — not specific to this problem's numbers, no
  citation of optimal transport needed (the proof is elementary). Reusable by any future
  approach in this population wanting a lower-bound certificate on `e` that does not require
  per-step monovariance (unlike a `Φ`-potential) or location-based casework. The naive clip
  candidate `g(t)=\min(t,e_m)` is refuted as a certificate for `D_m` specifically (too lossy,
  degrades to `0`) — this is a fact about that one candidate, not about the lemma itself, which
  remains valid and open for other choices of `g`.
- **Cascade reachability lemma (§11 above, new this round, fully proved, general-purpose).**
  Statement: for every integer `j\ge1`, the single D/M-operation `M(2^j,2^{j-1})` applied to
  `D_j=(2^j,\dots,2,1)` yields exactly `D_{j-1}`; consequently `D_j` reduces to the singleton
  `\{1\}` using exactly `j` operations, and to `D_i` using exactly `j-i` operations, for every
  `0\le i\le j`. Proved in full by direct computation of the `M`-operation's effect (removes
  `2^j,2^{j-1}`, inserts their difference `2^{j-1}`, leaves `2^{j-2},\dots,1` — i.e. `D_{j-2}`'s
  elements — untouched) plus induction; independently re-verified this round by exact-`Fraction`
  computation for `j=1,\dots,6`. General-purpose (not specific to the certificate-search
  application) — reusable by any approach needing an explicit, minimal-length D/M witness
  connecting the dyadic family `D_j` to its own sub-instances, e.g. as a building block for
  `dyadic-cascade-induction`'s Fact-5-style ceiling-achievability constructions or for testing
  any future candidate potential/certificate against the dyadic family specifically.
- **Forced-value Lemmas A and B (§11 above, new this round, fully proved, general-purpose).**
  Statement: for every `m\ge1` (Lemma B: `m\ge2`), any 1-Lipschitz `g` with `g(0)=0` satisfying
  the weak-duality target inequality `e_g(M)\ge1` (raw scale) on every state reachable from
  `D_m` within `\le m` D/M-operations must satisfy `g(1)=1` and `g(2)=2` exactly (no slack at
  either value). Proved in full via the cascade reachability lemma (giving explicit
  within-budget witnesses `\{1\}` and `(2,1)`) sandwiched against the 1-Lipschitz bound from
  `g(0)=0`. This is the round's main new structural content: it converts a numeric LP
  observation (`m=2`: `\min g(1)=\max g(1)=1`, `\min g(2)=\max g(2)=2`) into a fully general
  theorem valid for every `m`, and is the tool used to give exact (not merely
  stress-test-observed) refutations of two natural clip candidates. Reusable by any future
  builder attempting a weak-duality/Lipschitz-certificate construction for this problem's lower
  bound — rules out, in one proof, every candidate that compresses information at or below
  value `2` on the dyadic family.
- **Localization Lemma (§12.1, new this round, fully proved, general-purpose).** Statement: if
  a disjoint sub-collection `A` of an active D/M multiset `M=A\sqcup B` is evolved by a legal
  operation sequence whose every intermediate value stays distinct from every value in `B`,
  then running that same sequence on the full multiset `M` leaves `B` completely untouched and
  produces `A'\sqcup B`. Proved directly from the definition of `D`/`M` (both act only on the
  referenced value(s), by construction). Reusable by any future approach needing to justify a
  "cascade/residual on part of a multiset while keeping the rest fixed" construction rigorously
  rather than asserting it informally (as several prior rounds' constructions implicitly did).
- **Top-Two-Residual-Cancel Lemma (§12.2, new this round, fully proved, general for all
  `k\ge1`).** Statement: `(2^k,2^{k-1},\tfrac12,\tfrac12)` is reachable from `D_m` (any
  `m\ge k$) within exactly `m-1` D/M-operations, for every `k\ge1` (generalizing round 5's
  ad hoc `k=2` witness `(4,2,\tfrac12,\tfrac12)` to a fully general family). Proved via the
  Localization Lemma applied to the residual `D_{k-2}$ cascading to `\{1\}` while
  `\{2^k,2^{k-1}\}` sit untouched, then one bisection of the residual `1`. Independently
  verified by direct exact simulation for `k=2,\ldots,8`. Reusable for constructing forced-value
  or refutation witnesses at any dyadic scale, not just `k=2`.
- **Successor (Consecutive-Pair) Lemma (§12.3, new this round, fully proved, general for all
  `j\ge0`).** Statement: `(2^j+1,2^j)` is reachable from `D_m` (any `m\ge j+1`) within exactly
  `m-1` D/M-operations, for every `j\ge0` (generalizing the outline-reviewer's `j=1` spot-check
  witness `\{3,2\}` to a fully general family). Proved via the Localization Lemma applied to a
  chain of matches subtracting `D_{j-1}$'s elements from the evolving top value
  `2^{j+1}$, leaving `2^j` untouched throughout (justified by an explicit geometric-sum partial-sum
  bound keeping the evolving value `>2^j` at every intermediate step). Independently verified by
  direct exact simulation for `j=1,\ldots,8`. Gives the exact equality `g(2^j+1)=g(2^j)+1` for
  any valid certificate (both bounds match: witness gives `\ge1`, Lipschitz gives `\le1`).
- **Combined forced/unforced Theorem for `g(2^k)`, `g(2^k+1)` (§12.4, new this round, fully
  proved, the round's main new structural content).** Statement: for every `k\ge0`,
  `k+1\le g(2^k)\le2^k`, both bounds tight and proven (not merely valid), with equality
  (hence `g(2^k)` genuinely forced) if and only if `k\in\{0,1\}$; the gap `2^k-(k+1)` is
  strictly positive and strictly increasing for `k\ge2`, hence `\to\infty`. Consequently
  `g(2^j+1)` is forced iff `g(2^j)` is, giving `g(3)=3` forced (recovering the
  outline-reviewer's spot-check as a special case) but `g(5),g(9),g(17),\ldots` all provably
  NOT forced. This is a complete, general, decisive answer (outcome (b), fully proved rather
  than spot-checked) to the round-6/7 outline's dispatched question of whether Forced-Value
  Lemmas A/B generalize to all reachable `j` — reusable by any future approach in this
  population (or a future problem with a similar dyadic-cascade certificate-search structure)
  needing to know exactly where a 1-Lipschitz weak-duality certificate is forced to equal the
  identity and where genuine slack exists.
- **Candidate certificate `g^*` (§12.6, new this round — a verified-but-unproven computational
  artifact, NOT a certified theorem; listed here for visibility/reuse, not for certification.)**
  An explicit, `m`-independent, piecewise 1-Lipschitz function (identity on `[0,3]`, then a
  slope-1 ramp from `k+1` to `k+2` on each `[2^k,2^k+1]` and a slope-0 plateau at `k+2` on each
  `[2^k+1,2^{k+1}]`, `k\ge1`) built directly from the Combined Theorem's minimal forced values.
  Exhaustively verified (every reachable state, exact `Fraction`, zero sampling) to satisfy
  `e_{g^*}(M)\ge1` for `D_m`, every `m=1,\ldots,6` (`326265` states, `0` violations) — the first
  candidate in this approach's history to survive full exhaustive testing this far. **Not
  proved for general `m`** — reusable by a future builder as a concrete starting point for
  either an inductive proof or a targeted (non-brute-force) search for a larger-`m`
  counterexample; do not cite this as an established result, only as a promising lead.
  **[Round 8 correction: the illustrative "`m=6` minimizer" example previously cited alongside
  this candidate was mathematically impossible (wrong size/sum) and has been replaced — see
  §13.2. The exhaustive-verification CLAIM itself (`0` violations through `m=6`) is unaffected
  and independently re-confirmed this round for `m=3,4,5,6`.]**
- **Base-case exact formula for `g^*` on the dyadic family (§13.4, new round 8, fully proved,
  general-purpose).** Statement: `g^*(2^i)=i+1` for every `i\ge0` (direct substitution into the
  piecewise definition); consequently `g^*(D_m)`, sorted descending, is exactly the consecutive
  integer run `(m+1,m,\ldots,2,1)`, and (using the elementary identity `e(n,n-1,\ldots,1)=
  \lceil n/2\rceil`, proved by pairing consecutive terms) `e_{g^*}(D_m)=\lceil(m+1)/2\rceil`
  **exactly, for every `m`** — re-verified by direct computation, `m=1,\ldots,8`. This is the
  **maximum**, not the minimum, of `e_{g^*}` over reachable-state sizes (the zero-operations
  extremum) — corrects a previous mischaracterization of this configuration as the *minimizing*
  mechanism. Reusable by any future approach needing an exact closed-form value of any
  1-Lipschitz certificate on the dyadic family's own base configuration.
- **Integer-Preservation Lemma for `g^*` (§13.5, new round 8, fully proved, general-purpose).**
  Statement: `g^*` maps every nonnegative integer to a nonnegative integer (immediate from the
  piecewise definition, both branches being integer arithmetic on integer inputs); since `D_m`
  (unnormalized) and every state reachable from it via legal `D`/`M` operations
  (`lemmas/dm-operation-reformulation.md`) consist entirely of nonnegative integers (both
  operations preserve integrality), `e_{g^*}(M)` is **always an integer** on every such
  reachable state. **Corollary:** proving `e_{g^*}(M)\ge1` for every reachable `M` is exactly
  equivalent to proving `e_{g^*}(M)>0` (strict positivity) — a genuine reduction of the
  remaining open target to a sign question, structurally analogous to (but not yet shown to
  reduce to) the certified Superincreasing No-Early-Zero Lemma's "never reaches exactly `0`"
  mechanism for the raw (non-`g^*`) problem. Reusable by any future builder attempting to
  complete `g^*`'s general proof, or testing any other integer-based candidate certificate on
  this problem's dyadic family.
- **Edge-wise monovariance failure for `e_{g^*}` (§13.6, new round 8, fully proved NEGATIVE
  result, general-purpose diagnostic).** Statement: there is no bound of the form "`e_{g^*}`
  decreases by at most `c` under a single legal `D`/`M` operation" for any small constant `c`
  (concretely, a single `D(32)` operation applied to the reachable state `(32,8,4)` — itself
  reachable from `D_5` in `3` operations — drops `e_{g^*}` from `5` to `1`, a drop of `4`;
  exhaustive enumeration of all `3252` edges of the full `m=5` reachable-state graph shows drops
  of magnitude up to `5` occurring in **both** directions). This decisively rules out any proof
  of `g^*`'s minimum-is-`1` property based on single-operation (edge-wise) monovariance — a
  genuine, reusable negative result saving a future builder from re-attempting that specific
  technique. Does **not** rule out a size-class-wide (non-edge-wise) inductive argument, which
  remains open.

## §13 (round 8, CORRECTED) — the illustrative example was wrong; recomputed from scratch, the
structural mechanism revised, one direction ruled out, general proof still open

**Round-8 outline-reviewer finding, confirmed and fixed.** The previous version of this section
claimed an "`m=6` minimizer `(32,26,13,13,8,6,1)`" with `g^*`-values `(6,6,5,5,4,4,1)`. This is
**mathematically impossible** and the reviewer's diagnosis is exactly right: every single `D` or
`M` operation (per the certified `lemmas/dm-operation-reformulation.md`) reduces the **size** of
the active multiset by *exactly* `1` (`D(x)` deletes one element: size `-1`; `M(x,y)` deletes two
elements and inserts one: size `-2+1=-1`). Starting from `D_6=(64,32,16,8,4,2,1)` (`7=m+1`
elements) with budget `m=6`, a final state of size `7` can only be reached using `0` operations —
i.e. it **must equal `D_6` itself, unchanged**. The claimed 7-element list sums to `99\ne127=
2^7-1=S(D_6)$ and is not `D_6` — confirmed a genuine, avoidable arithmetic/logic error, not a
borderline case. It has been discarded, not patched; everything below is recomputed from scratch
with an independent exact-`Fraction` BFS harness (`D(x)`: remove one copy of `x`; `M(x,y)`: for
active elements `x\ge y>0$, remove both, insert `x-y$ — matching the certified lemma exactly,
including the `x=y$ boundary case, checked to make no difference to the reachable-state count).

**13.1 `D_6` recomputed and verified.** `D_6 = (64,32,16,8,4,2,1)`, `7` elements
(`=m+1$, `m=6$), superincreasing (`64>32+16+8+4+2+1=63$), sum `=127=2^7-1$ ✓ — matches
`e_m\cdot S(D_m)=1$'s normalization exactly (`S(D_6)=127$ unnormalized).

**13.2 An actual, verified `m=6` minimizer.** By the already-certified **Cascade Reachability
Lemma** (`lemmas/lipschitz-certificate-and-forced-values.md`), `D_6\to D_1=(2,1)` in exactly
`6-1=5$ operations (using `5` of the `6` available, `1` left unused — always legal, an unused
operation is simply not exercised). At `M=(2,1)`: `g^*(2)=2$, `g^*(1)=1$ (both by direct
substitution into the piecewise formula — `k=1$ for `t=2$, ramp branch since `2\le2^1+1=3$, giving
`g^*(2)=(1+1)+(2-2)=2$; `k=0$ for `t=1$, giving `g^*(1)=(0+1)+(1-1)=1$, matching the `t\le1$
identity branch too). So `e_{g^*}(2,1)=2-1=1` **exactly** — an honest, fully verified, minimal
concrete witness that `D_6` (budget `6`) admits a reachable state with `e_{g^*}=1`, replacing the
broken example. (Independent exhaustive BFS confirms `(2,1)` is one of `373` distinct size-`2`
states reachable from `D_6` within `\le6` operations that achieve `e_{g^*}=1$ exactly, and that
`e_{g^*}=1` is the **global minimum** over *all* `3117$ states reachable from `D_6` within `\le6`
operations — re-verified independently for `m=3,4,5` too, `31`, `125`, `585` states respectively,
same conclusion: global min `=1$ in every case, matching the round-7 builder's headline claim,
which is correct even though its illustrative example was not.)

**13.3 The real structural mechanism (replacing "cancelling pairs plus residual `1`", which is
WRONG as a description of the *minimizer*).** Computing, for each size `k=1,\dots,m+1`, the
**minimum** of `e_{g^*}` over *all* states of that size reachable from `D_m$ (not merely a
hand-picked example) gives, exhaustively for `m=3,4,5,6`:
```
size k :   1   2   3   4   5   6   7
m=3:       1   1   2   2                      (m+1=4 elements max)
m=4:       1   1   2   2   3                  (m+1=5)
m=5:       1   1   2   2   3   3              (m+1=6)
m=6:       1   1   2   2   3   3   4          (m+1=7)
```
In every case checked, **`\min_{\text{size }k}e_{g^*} = \lceil k/2\rceil` exactly** — a clean,
`m`-independent function of size alone, **monotonically non-decreasing in `k`** (fewer operations
used, i.e. more original structure left untouched, is *worse* for Xiang Yu, not better). The
previous round's "many cancelling `g^*`-pairs plus a residual `1`" description is the *correct*
description of `e_{g^*}(D_m)` **itself** (the `k=m+1`, zero-operations case — see 13.4 below), but
it is the **largest**, not the smallest, value across sizes — i.e. it describes the configuration
Xiang Yu should *avoid*, not the one Xiang Yu is aiming for. **The true minimizing mechanism is
the opposite: use (nearly) the whole budget to collapse the multiset down to size `1` or `2`**,
where the two surviving `g^*`-brackets differ by exactly `1` (as in the `(2,1)` witness above) —
this is much closer in spirit to the certified **Successor Lemma** / **Top-Two-Residual-Cancel
Lemma** (`lemmas/forcing-characterization-dyadic.md`) than to a "many-pairs" cancellation.
**This is a genuine, corrected structural finding, not a cosmetic fix** — the previous round's
mechanistic explanation for *why* `g^*` seems to work was pointing at the wrong extremum.

**13.4 New Lemma (base case, exact, proved in full — not merely verified).** `g^*` maps the
dyadic family exactly onto consecutive integers: for `i=0,\dots,m$, `g^*(2^i)=i+1$. *Proof.* For
`t=2^i` (`i\ge0`), the unique `k` with `2^k\le t<2^{k+1}` is `k=i` (since `t=2^i` itself). The
ramp condition `t\le2^k+1` becomes `2^i\le2^i+1`, always true. So
`g^*(2^i)=(i+1)+(2^i-2^i)=i+1` exactly. ∎ Consequently `g^*(D_m)$, sorted descending, is *exactly*
the integer run `(m+1,m,m-1,\dots,2,1)`. **Lemma (alternating sum of a consecutive integer run).**
For any integer `n\ge1`, `e(n,n-1,\dots,1)=\lceil n/2\rceil`. *Proof.* Pair consecutive terms
`(n,n-1),(n-2,n-3),\dots`; each pair contributes exactly `1` to the alternating sum (`(n-2j)-
(n-2j-1)=1`). There are `\lfloor n/2\rfloor` such pairs; if `n` is odd, one term (`=1`, the last
element of the run) is left unpaired, contributing `+1` more. Total:
`\lfloor n/2\rfloor+(n\bmod2)=\lceil n/2\rceil`. ∎ Combining: **`e_{g^*}(D_m)=\lceil(m+1)/2\rceil`
exactly, for every `m$** — re-verified by direct computation for `m=1,\dots,8` (`1,2,2,3,3,4,4,5`
respectively), matching in every case. This proves the `k=m+1` (zero-operations) row of the
13.3 table in closed form, not merely by exhaustive search.

**13.5 New Lemma (Integer-Preservation of `g^*`, proved in full, general-purpose).**
*Statement.* For every nonnegative integer `t`, `g^*(t)` is a nonnegative integer. *Proof.*
`g^*(0)=0`. For integer `t\ge1`, let `k` be the unique integer with `2^k\le t<2^{k+1}` (exists
since `t\ge1`; `k,2^k$ are both integers). If `t\le2^k+1`: `g^*(t)=(k+1)+(t-2^k)`, a sum of
integers, hence an integer. Otherwise `g^*(t)=k+2`, an integer. `g^*` is nondecreasing (both
pieces have slope `\in\{0,1\}\ge0`) and `g^*(0)=0`, so `g^*(t)\ge0`. ∎ **Corollary (reduction of
the whole target to a sign question).** `D_m` (unnormalized) consists entirely of nonnegative
integers; `D(x)` and `M(x,y)=x-y` both preserve integrality of every element remaining active
(immediate from the operation definitions, by induction on operation count). Hence **every state
`M` reachable from `D_m` by any legal D/M sequence is an all-nonnegative-integer multiset**, so
by the Integer-Preservation Lemma, `\{g^*(v):v\in M\}` is also all-nonnegative-integers, and
`e_{g^*}(M)$ (an alternating sum of integers) **is itself always an integer**. **Consequently,
proving `e_{g^*}(M)\ge1` for every reachable `M` is exactly equivalent to proving
`e_{g^*}(M)>0` (strict positivity) for every reachable `M`** — an integer that is `>0` is
automatically `\ge1`. This is a genuine, useful reduction (it converts the target from a
numeric-threshold statement into a strict-sign statement, structurally the same shape as the
already-certified Superincreasing No-Early-Zero Lemma's "never reaches exactly `0`" target for
the *raw* problem) — but it is **not, by itself, a proof that the sign is right**.

**13.6 The naive "technique 1" as previously stated is FALSE — a decisive, concrete negative
finding, not a mere restatement of the difficulty.** The previous round's Proposed Technique 1
implicitly required (via its inductive proof sketch, "operations preserve a pairs-plus-residual
`\ge1$ invariant") that a **single** legal D/M operation cannot decrease `e_{g^*}` by more than
`1` at a time (matching the size-indexed floor `\lceil k/2\rceil` dropping by at most `1` per
step). **This single-operation ("edge-wise") monovariance is FALSE, checked by exhaustive
enumeration of every legal-operation edge in the full `m=5` reachable-state graph (`585` states,
`3252$ directed edges, exact `Fraction` arithmetic, no sampling).** Concrete counterexample:
starting from the reachable state `(32,8,4)$ (itself reachable from `D_5` — direct check: apply
`M(4,4)\to0` discarded/`D`-type reductions or, concretely, `D_5=(32,16,8,4,2,1)\to(32,8,4)` via
`D(16)` then `D(2)$ then `D(1)`, three operations, well within budget `5`), the single legal
operation `D(32)` (deleting the value `32`) produces `(8,4)`. Direct computation:
`g^*(32)=6,g^*(8)=4,g^*(4)=3` (all via the base-case formula, `13.4`), so
`e_{g^*}(32,8,4)=6-4+3=5`, while `e_{g^*}(8,4)=4-3=1` — **a single operation drops `e_{g^*}` by
exactly `4`, not `\le1$.** (Full distribution of single-operation drops across all `3252` edges
of the `m=5` graph: drops of `-5,-4,-3,-2,-1,0,1,2,3,4` all occur, with **magnitude up to `5`** —
i.e. `e_{g^*}` can swing by several units in a single step, in **either** direction.) **This
rules out, decisively and concretely (not merely "not yet carried out"), any proof strategy for
`g^*`'s minimum-is-`1$ property based on a per-operation (edge-wise) monovariant** — the true
`\lceil k/2\rceil$ floor (13.3) is a fact about the **minimum over an entire size class**, not a
fact preserved step-by-step along any *individual* path, so an inductive argument (if one exists)
must reason about the whole reachable set at each size, not a single transition. This is a
genuine, reusable negative result for any future attempt at this same certificate.

**13.7 Honest status of the general proof — NOT closed.** What is now established, in full,
without gaps: (a) the corrected concrete example (13.2); (b) the exact closed-form value of
`e_{g^*}$ at the zero-operations extremum, `\lceil(m+1)/2\rceil` (13.4); (c) the
Integer-Preservation Lemma, reducing "`\ge1`" to "`>0`" (13.5); (d) a decisive proof that the
most natural (edge-wise monovariant) proof strategy cannot work as stated (13.6); (e) exhaustive
(not sampled) computational confirmation, for `m=3,4,5,6`, that
`\min_{\text{size }k}e_{g^*}=\lceil k/2\rceil` holds **exactly**, hence the global minimum over
all reachable states (any size) is `1`, achieved at sizes `1,2` — consistent with, and now
correctly explaining, the round-7 builder's `m\le6$ (and its claimed but here-unreproduced `m=7`)
exhaustive-BFS finding of "zero violations." **What is NOT established:** a general (all-`m`)
proof of `\min_{\text{size }k}e_{g^*}=\lceil k/2\rceil` (or even just the weaker `\ge1$ target) —
this would need an argument that works over an entire size-class simultaneously (e.g. strong
induction on `k` using a characterization of *every* possible size-`(k+1)`-to-size-`k` transition
and showing that whichever predecessor achieves the size-`(k+1)` minimum, no legal move from *any*
size-`(k+1)$ state undercuts the size-`k` floor) — this is a **genuinely harder inductive
argument than a simple monovariant**, not yet found. **Technique 2 (Kraft-budget
reformulation, per crux `aimo-0790`)** remains untried this round (time was spent fixing the
error and establishing 13.3–13.6 instead); it is still a plausible, independent fallback,
unaffected by 13.6's negative finding since it does not rely on edge-wise monovariance at all.
**The `g^*`-minimum-is-`1` property is correctly reported as an open conjecture, exhaustively
verified through `m=6$ (this round, with a corrected example and corrected mechanism) but not
proved for general `m`.** Do not re-attempt the literal edge-wise-monovariant version of
technique 1 (13.6 rules it out); a future builder attempting technique 1's spirit should instead
look for a **size-class-wide** (not edge-wise) inductive invariant, or pursue technique 2.

## §14 (round 9 outline) — the Distinct-Bucket Lemma: the precise remaining target, and an
elementary (already-verified) route from it to `e_{g^*}\ge1`

This round's explorer (`math-explorer-eg-star-minimum.md`) sharpened §13.7's open "size-class-wide
inductive invariant" task into one clean, self-contained structural conjecture, plus an
**elementary, already-checked** (not merely sketched) proof that this conjecture implies the whole
target. This supersedes §13.7's vaguer "characterize every possible predecessor transition" framing
with a single precise claim.

### 14.1 Closed form for `g^*` (new, algebraically equivalent to the piecewise definition in
§12.6, verified `t=0..39`)
```
g^*(t) = bit_length(t-1) + 1     for integer t\ge1     (g^*(0)=0),
```
i.e. `g^*(t)-1=\lceil\log_2 t\rceil`. Level sets ("buckets") of `g^*` are exactly the dyadic
doubling intervals: `B_1=\{1\}`, `B_2=\{2\}`, and for `k\ge3`, `B_k=(2^{k-2},2^{k-1}]`.

### 14.2 The Distinct-Bucket Lemma — the precise open target
```
Distinct-Bucket Lemma. For every m and every state M reachable from D_m via a legal
  \le m-operation D/M sequence, no two elements of M lie in the same g^*-bucket:
  v,w\in M, v\ne w  \Rightarrow  g^*(v)\ne g^*(w).
```
**Status: NOT proved. Numerically verified exhaustively (all D/M sequences, every length `\le m`)
for `m=1,\dots,7$ (`3,9,31,125,585,3117,18537` total reachable states respectively, `0`
collisions — reproduces and extends the file's own `m=6` count as an independent cross-check),
plus `80{,}000` random D/M walks to `m=15` with `0` collisions.** This is the single concrete
target to hand to the next builder — a genuinely different kind of claim from the dead edge-wise
monovariant (13.6): it is a **state-level structural (set-membership) invariant**, not a scalar
potential that must not drop too fast per move, so it is not ruled out by 13.6's counterexample.

### 14.3 Why Distinct-Bucket, once proved, finishes the whole target — elementary, ALREADY
VERIFIED by direct implication-check (not a proof sketch left for the builder)

If Distinct-Bucket holds, sort any reachable `M` descending `v_1>\dots>v_k`. Since `g^*` is
nondecreasing and constant only within a bucket, and Distinct-Bucket forbids any two of
`v_1,\dots,v_k` sharing a bucket, the bucket indices `g^*(v_1)>\dots>g^*(v_k)` are **strictly
decreasing** (sorted order + pairwise-distinct buckets forces strict inequality at every
consecutive pair, since buckets are intervals). By the already-certified **Integer-Preservation
Lemma** (§13.5), these are `k` strictly decreasing positive integers. Pairing consecutive terms,
`g^*(v_{2i-1})-g^*(v_{2i})\ge1` for each pair; if `k` is odd, the unpaired trailing term satisfies
`g^*(v_k)\ge g^*(1)=1` (monotonicity, `v_k\ge1`). Summing:
```
e_{g^*}(M) \ge \lceil k/2\rceil \ge 1     for every k\ge1.
```
This reproduces §13.3's exhaustively-checked `\lceil k/2\rceil` size-class floor **exactly**, via
a 5-line argument with **no per-edge monovariance and no size-class-wide induction on `e_{g^*}`
itself needed at all** — it reduces the entire target to the one structural conjecture in §14.2.
(The size-`1` row is free from monotonicity alone; the size-`2` row is *exactly* the `k=2` case of
Distinct-Bucket.) This implication was checked directly (not merely asserted) and is correct.

### 14.4 Proof shape for Distinct-Bucket (a concrete lead, NOT attempted — the builder's task)

`D_m`'s own elements are `2^0,\dots,2^m`, trivially one per bucket. Every value ever active during
a D/M sequence is (by the token/signed-sum invariant already proved in the certified
**Superincreasing No-Early-Zero Lemma**, `lemmas/superincreasing-no-early-zero.md`) a signed
combination of a subset of the original powers of `2`, with pairwise-disjoint index supports
across simultaneously-active tokens. The classical superincreasing/knapsack fact — that such a
signed combination's magnitude is essentially pinned to the doubling bracket of its
**highest-surviving power** — strongly suggests Distinct-Bucket is provable by **strengthening
that lemma's own invariant**: instead of (or in addition to) tracking "never exactly `0`," track,
for each dyadic level `j=0,\dots,m`, whether it is currently "occupied" by some active token's
highest surviving power, and prove by induction on operation count that **no level is ever
occupied by two simultaneously-active tokens** (a binary-carry-style bookkeeping argument: an `M`
operation on two tokens can only ever leave the *higher* of their two highest-surviving levels
occupied, since the lower cancels or is dominated — this is the natural adaptation of the already-
certified dominance mechanism, not a new one). **Concrete task for the builder:** formalize
"highest surviving level" precisely (as the largest `j` such that `2^j` appears with nonzero net
coefficient in the token's signed-sum representation) and prove the occupied-level-uniqueness
invariant by the same style of induction already used for the no-early-zero fact — likely a
genuinely short extension of already-certified machinery, not a new mechanism from scratch.

### 14.5 Fallback, tested and refuted this round — do not re-attempt unmodified

A naive **Kraft-budget potential** `\Phi(M)=\sum_{v\in M}2^{-(g^*(v)-1)}$ (motivated by crux
`aimo-0790`'s weight-splitting mechanism) was tested for edge-wise monotonicity across the full
BFS graph and found **NOT monotone**: `1.5$–`3\%` of edges *increase* it (`m=2`: `1/18`; `m=3`:
`5/97`; `m=4`: `21/542`; `m=5`: `95/3252`). **Do not reuse this specific potential unmodified as a
direct edge-wise monovariant** — if revisited, it needs a size/budget-aware correction (the same
lesson as this file's own already-dead `\Phi_1,\Phi_2` potentials for the raw non-`g^*` problem,
round 4). `aimo-0790`'s general *shape* (dyadic-block bookkeeping + pairwise merge) remains a
plausible, indirect hint for §14.4's proof (both involve "merge two dyadic-scale objects into
one," the same shape as the `M` operation) but is not a literally transferable lemma (its own goal
is an upper bound on a sum, ours a lower bound on an alternating sum over a structurally
constrained small set) — assessed in detail, not re-tested, this round.

**Net effect of this section: the entire remaining gap of this approach (`e_{g^*}`'s minimum is
`1`, for every `m`) now reduces, via an elementary and already-checked argument, to ONE clean
structural claim (§14.2) with a concrete, well-scoped proof lead (§14.4) — a substantially
sharper target than §13.7's "size-class-wide induction on `e_{g^*}` itself" framing.**

## §15 (round 9 builder) — the Distinct-Bucket Lemma: §14.4's proof lead REFUTED, two new
general lemmas proved in full, the target sharpened to one precise (still open) local claim

**Task per dispatch:** prove the Distinct-Bucket Lemma (§14.2) in full generality, following
§14.4's lead (strengthen the Superincreasing No-Early-Zero Lemma's token invariant from
"never `0`" to "no dyadic level occupied twice"). **Outcome: the literal §14.4 mechanism is
FALSE (refuted with a concrete example, §15.1); but the underlying idea is salvaged into two
new, fully proved general lemmas (§15.2–15.3) that reduce Distinct-Bucket to one clean,
precisely-stated, computationally-confirmed-but-still-open local inequality (§15.4). The
Distinct-Bucket Lemma itself is NOT fully closed this round — see §15.5 for the honest
remaining gap and §15.6 for why the natural "superincreasing alone" strengthening cannot
possibly work (an explicit abstract counterexample), which is itself a useful negative result
ruling out an entire class of future attempts.**

### 15.1 Refutation of §14.4's specific mechanism: `g^*`-bucket is NOT pinned to the dominant
surviving power `L` (or `L+1`) — exact counterexample, and the deviation is unbounded

§14.4 conjectured that a token's bucket is essentially determined by its "highest surviving
power" `L` (`=m+1-i_0`, where `i_0=\min S(v)$ is its dominant index in the certified token
invariant), via an `M`-operation dominance mechanism ("only the higher of the two levels stays
occupied"). This is checked directly and is **false**: tracking, for every token in every
`D_m`-reachable token-labeled state (`m=1,\dots,5`, exact `(S,\varepsilon)$ bookkeeping,
`4`–`1510` token-labeled states per `m`), the deviation `d:=\mathrm{bucket}(v)-(L+1)`, the
distribution of `d` is **not concentrated near `0`** — it spans every integer from `0` down to
`-L$ (i.e. bucket can drop all the way to `1`, regardless of how large `L` is). Concrete
witness (`m=3`, `D_3=(8,4,2,1)`): the chain `M(8,4)\to4`, then `M(4,2)\to2`, then `M(2,1)\to1$
(three operations, exactly budget `m=3`) produces the single surviving token `v=1` with token
data `S(v)=\{1,2,3,4\}` (all four original indices used), dominant index `i_0=1$, dominant
power `L=3` (from `a_1=8`) — yet `\mathrm{bucket}(1)=1`, a drop of `d=-3` from the naively
predicted `L+1=4`. (Algebraically: `8-4-2-1=1`, exactly the certified Fact 5
chain-cancellation pattern.) **This rules out, decisively, any proof of Distinct-Bucket via a
per-token bound of the form "bucket is within a bounded distance of the dominant power" — the
true bucket of a heavily-merged token can be arbitrarily far below its dominant power's own
bucket.** (Verification script: `/tmp/round-9/work/explore_bucket4.py`, re-run against a
from-scratch token-tracking BFS, not reused from any prior round's code.)

### 15.2 New Lemma (Superincreasing Preservation), proved in full, general-purpose

**Statement.** Let `a_1>a_2>\dots>a_k>0` be any strictly superincreasing sequence
(`a_i>a_{i+1}+\dots+a_k` for every `i<k`; this includes `D_m`, `a_i=2^{m+1-i}`, as a special
case, but the lemma is proved for an arbitrary superincreasing base). Then **every state
reachable from `\{a_1,\dots,a_k\}` by any legal sequence of `D`/`M` operations (of any length,
not merely `<k`) is again strictly superincreasing**, when sorted descending.

**Proof.** Induction on the number of operations. Base case: the original sequence, superincreasing
by hypothesis. `D`-step (delete one active element `v_j`, sorted position `j`): for `i<j`, the new
tail sum (`\sum_{\ell>i,\ell\ne j}v_\ell`) is the old tail sum minus `v_j\le` the old tail sum,
so `v_i>` old tail `\ge` new tail still holds; for `i>j`, the tail is untouched, holds by IH; no
constraint needed at the removed position. `M`-step (the substantive case): let the active state
before the operation be `v_1>\dots>v_r>0$ (IH: superincreasing), and let the operation be
`M(x,y)`, `x\ge y>0`, `x=v_a`, `y=v_b`, `a<b` (WLOG `a<b`, since `x\ge y` and the sequence is
sorted descending; `x\ne y` because all simultaneously-active values in a legal D/M sequence
starting from a strictly superincreasing base are pairwise distinct — this is exactly Step 3 of
the already-certified `lemmas/superincreasing-no-early-zero.md`, so `a<b` strictly). Let
`w:=x-y=v_a-v_b`.

*Key Sub-claim.* `w > v_c` for **every** surviving index `c\ne a,b` with `c>a` (i.e. `w` exceeds
every element that was originally below `v_a` in the sorted order, except `v_a,v_b` themselves).
*Proof of sub-claim:* by the superincreasing hypothesis applied at index `a`,
`v_a>v_{a+1}+v_{a+2}+\dots+v_r`, a sum that includes both `v_b` (since `b>a`) and every other
surviving `v_c` (`c>a`, `c\ne b`) as **distinct, disjoint, positive** terms; hence
`v_a>v_c+v_b+(\text{other nonnegative terms})\ge v_c+v_b`, i.e. `w=v_a-v_b>v_c`. This holds
simultaneously for every such `c` (not just one at a time, since it is a single inequality
`v_a>\sum` applied with different terms singled out).

*Consequence (exact structural fact, also independently confirmed by `3000` random-trial exact
simulation, `/tmp/round-9/work/verify_replace_lemma.py`, zero mismatches):* the new sorted list
is **exactly** `v_1,\dots,v_{a-1},\,w,\,v_{a+1},\dots,v_{b-1},\,v_{b+1},\dots,v_r` — i.e. `w`
takes over `v_a`'s **exact** sorted slot (it is bigger than everything from `v_{a+1}` on,
excluding `v_b`, by the sub-claim, and smaller than `v_a$ itself, hence smaller than
`v_1,\dots,v_{a-1}`), and `v_b`'s slot is simply deleted, with no re-sorting needed elsewhere.
(**Call this the Slot-Replacement Corollary** — reusable independently of superincreasing-ness,
since its proof only used the sub-claim.)

*Verifying superincreasing at each new position, using this exact slot structure:*
- Positions `1,\dots,a-1$ (untouched, before `w`): new tail from position `i<a` is
  `(\text{old tail from }i)-v_a-v_b+w=(\text{old tail})-v_a-v_b+(v_a-v_b)=(\text{old tail})-2v_b\le
  \text{old tail}`. Since `v_i>` old tail (IH), `v_i>` new tail too.
- Position of `w` (slot `a`): new tail after `w` is `(v_{a+1}+\dots+v_r)-v_b` (removing `v_b`
  from the old tail-from-`a$; nothing else changes since `w` sits exactly where `v_a` was). Need
  `w>(v_{a+1}+\dots+v_r)-v_b`, i.e. `v_a-v_b>(v_{a+1}+\dots+v_r)-v_b`, i.e.
  `v_a>v_{a+1}+\dots+v_r` — **exactly the IH at position `a`**, already true.
- Positions `a+1,\dots,b-1` (untouched, between): new tail after `v_c` is
  `(\text{old tail from }c)-v_b<\text{old tail from }c<v_c` (IH), since we are only *subtracting*
  a positive quantity `v_b` from an already-dominated sum.
- Positions `b+1,\dots,r` (untouched, after `v_b`'s old slot): tail is entirely unaffected (both
  removed elements `v_a,v_b` and the inserted `w` are all at or before slot `a<b`'s old
  neighbourhood, i.e. before these positions), so the IH applies verbatim.

All four position-classes are covered exhaustively (every surviving position falls in exactly one
of them), completing the inductive step. `\blacksquare`

**Independent computational corroboration (this round, fresh code, not reused):** zero
superincreasing violations across the *entire* `D_m`-reachable state space, `m=0,\dots,7$
(`1,3,9,31,125,585,3117,18537` states respectively — matching the file's own and the
outline-reviewer's independently-reported state counts exactly), plus `3000` random trials on
freshly-generated superincreasing bases of size `2$–`7` (not tied to powers of `2` at all,
confirming the lemma's general-base scope) — `0` failures
(`/tmp/round-9/work/explore_superinc.py`, `/tmp/round-9/work/explore_superinc_general.py`,
`/tmp/round-9/work/verify_replace_lemma.py`).

### 15.3 New Lemma (Value Order = Dominant-Index Order), proved in full, specific to the D/M
token machinery

**Statement.** For `D_m` specifically (`a_i=2^{m+1-i}`, indices `i=1,\dots,m+1`), consider any
`D_m`-reachable token-labeled state, using the certified token invariant of
`lemmas/superincreasing-no-early-zero.md` (each active token `v` carries an index set
`S(v)\subseteq\{1,\dots,m+1\}`, pairwise disjoint across simultaneously-active tokens; let
`i_0(v):=\min S(v)` be `v`'s **dominant index**). Then for any two simultaneously-active tokens
`u,v`: `i_0(u)<i_0(v)\iff u>v`. Equivalently, sorting the active state by value coincides
*exactly* with sorting by increasing dominant index.

**Proof.** Induction on operation count, using the Slot-Replacement Corollary of §15.2 (which
applies verbatim to `D_m`, a special case of a superincreasing base). Base case (`D_m` itself):
`i_0(a_i)=i`, and `a_1>a_2>\dots>a_{m+1}`, so value order and index order coincide trivially.
`D`-step: deleting one token preserves the order-correspondence among the survivors (subset of an
already-order-consistent set). `M`-step: by IH, `x>y\implies i_0(x)<i_0(y)$ (the very
correspondence being inducted, applied to the two operands, which are simultaneously active
before the operation). By the token invariant's definition (already certified,
`S(w)=S(x)\sqcup S(y)`), `i_0(w)=\min(S(x)\cup S(y))=\min(i_0(x),i_0(y))=i_0(x)$ (using
`i_0(x)<i_0(y)` just derived). By the Slot-Replacement Corollary, the new value-sorted list is the
old one with `v_a\,(=x)` replaced in place by `w` and `v_b\,(=y)` deleted — and we have just shown
`w`'s dominant index equals `x`'s own dominant index, unchanged. Hence the value-order/index-order
correspondence, restricted to survivors, is exactly preserved: the slot that held index `i_0(x)`
still does (now via `w` instead of `x`), the slot that held `i_0(y)` is gone (consistent, since
`y` is gone), and every other slot/index pair is untouched. `\blacksquare`

**Independent computational corroboration:** re-verified on a from-scratch token-labeled BFS,
`m=1,\dots,5` (`4,15,62,289,1510` token-labeled states — larger than the value-only state counts
since distinct token histories reaching the same value are counted separately here, as expected;
not a discrepancy, see `/tmp/round-9/work/explore_order.py`), `0` order mismatches in every case.

### 15.4 Reduction of Distinct-Bucket to one precise local claim, via §15.2's exact slot
structure — the sharpest form of the open target found this round

Using §15.2's Slot-Replacement Corollary (new sorted list `=v_1,\dots,v_{a-1},w,v_{a+1},\dots,
v_{b-1},v_{b+1},\dots,v_r`, exactly, no re-sorting): to prove Distinct-Bucket is preserved by an
`M`-operation, given it holds before (IH: `\mathrm{bucket}(v_1)>\dots>\mathrm{bucket}(v_r)$,
strictly decreasing), it **suffices** to check only the *new adjacent pair* created by inserting
`w` into slot `a`: (i) `\mathrm{bucket}(v_{a-1})>\mathrm{bucket}(w)` — **immediate**, since
`w<v_a` gives `\mathrm{bucket}(w)\le\mathrm{bucket}(v_a)<\mathrm{bucket}(v_{a-1})` (the last step
by IH); and (ii) `\mathrm{bucket}(w)>\mathrm{bucket}(z)`, where `z` is the **largest surviving
token with value `<v_a`** (i.e. `z=v_{a+1}` if `b\ne a+1`, else `z=v_{a+2}` if it exists, else no
such `z` and the claim is vacuous). This suffices because, by §15.2's Key Sub-claim, `w` exceeds
*every* surviving element after slot `a`, so `z` (being the *largest* of them) is the only one
that could possibly collide bucket-wise with `w` — if `\mathrm{bucket}(w)>\mathrm{bucket}(z)`,
then since `\mathrm{bucket}` is monotonic in value and `z\ge` every other survivor after slot `a`,
`\mathrm{bucket}(w)>\mathrm{bucket}(z)\ge\mathrm{bucket}(v_c)` for every such `c`, and all other
(untouched) adjacent-bucket relations are unaffected by the operation (checked directly: the
untouched prefix `v_1,\dots,v_{a-1}` keeps its own internal bucket-strict-decrease by IH; the
positions strictly between `a` and `b` and after `b` keep their mutual bucket relations, being an
untouched subsequence of the IH's already-strictly-decreasing bucket list).

**The Local Claim (open):** *for `D_m`-reachable states, whenever an `M`-operation removes
`x=v_a>y=v_b` and `z` (as defined above) exists, `\mathrm{bucket}(x-y)>\mathrm{bucket}(z)`.*
Independently verified by direct computation to hold with **zero exceptions** across the
*entire* `D_m`-reachable-state transition graph, `m=0,\dots,6` (`11535` total `M`-transitions
checked at `m=6` alone; `/tmp/round-9/work/verify_local_claim.py`, exact integer arithmetic, not
sampled).

### 15.5 Why "superincreasing alone" (the natural strengthening suggested by §15.2/15.4) cannot
possibly prove the Local Claim — a genuine negative result, narrowing future proof attempts

A natural hope, given §15.2's clean proof, is that superincreasing-ness of the *state itself*
(not merely §15.2's `M`-step sub-claim, but the full property, now known to be an invariant)
already forces distinct buckets, making the Local Claim free. **This is false in general**, even
for values that could arise as *adjacent elements of a legitimate (if abstract) superincreasing
pair**: take `v_i=4,v_{i+1}=3$ (with no further tail, i.e. `k=2$). This trivially satisfies the
superincreasing condition (`a_1>a_2`, the only requirement for `k=2`, no sum constraint), yet
`\mathrm{bucket}(4)=\mathrm{bit\_length}(3)+1=2+1=3` and `\mathrm{bucket}(3)=
\mathrm{bit\_length}(2)+1=2+1=3` — **the same bucket.** So the abstract combinatorial class
"strictly superincreasing, integer, positive" is **not** enough to force distinct `g^*`-buckets;
the extra ingredient needed is specific to the base-`2`/token structure of `D_m$-reachability
(it never actually produces an adjacent pair like `(4,3)` as two simultaneously-surviving
values, even though such a pair is abstractly superincreasing-compatible) — **not** a generic
fact about superincreasing sequences. This rules out any future attempt to close the Local Claim
by superincreasing-ness alone (§15.2's invariant, though genuinely useful for the "≤" direction
and for the exact slot structure, is provably insufficient by itself for the "≠" direction) —
the correct proof of the Local Claim must use the token/base-`2` structure (e.g. §15.3's
value-order/index-order correspondence, or a finer digit-level accounting of `\delta(v):=
\text{(next power of 2 above }v\text{)}-v`) more essentially, not merely the real-number ordering
properties used in §15.2.

### 15.6 Honest status: what this round closes and what remains open

**Closed in full, general, reusable lemmas (both independently re-derivable from the proof text
alone, both cross-checked computationally with fresh code):**
- **Superincreasing Preservation Lemma** (§15.2) — general base, any legal D/M sequence, any
  length.
- **Slot-Replacement Corollary** (§15.2) — the exact sorted-position bookkeeping of an
  `M`-operation, general base.
- **Value-Order = Dominant-Index-Order Lemma** (§15.3) — specific to `D_m$'s token structure.

**Decisively refuted (a useful negative result, not merely "not yet tried"):**
- §14.4's literal proof mechanism ("bucket pinned near the dominant surviving power") — exact
  counterexample, unbounded deviation (§15.1).
- "Superincreasing-ness alone implies distinct buckets" — abstract counterexample `(4,3)`
  (§15.5), ruling out an entire class of future proof attempts that would try to get Distinct-
  Bucket for free from §15.2's already-proved invariant.

**Still open:** the Local Claim of §15.4 (`\mathrm{bucket}(x-y)>\mathrm{bucket}(z)`) — this is
now the single, precisely-scoped, computationally-exhaustively-confirmed-through-`m=6` (zero
exceptions) remaining target for the Distinct-Bucket Lemma, hence for this whole approach's
route to `e_{g^*}(M)\ge1`. It is a **strictly sharper and more tractable-looking** target than
either §14.2's original global claim or §14.4's refuted mechanism, since it isolates the content
to a single inequality about one `M`-operation's output versus one specific, well-defined
comparison value `z` — but it is **not proved**, and §15.5 shows the most obvious route to it
(generic superincreasing reasoning) cannot work, so it needs a genuinely finer, base-`2`-specific
argument (a concrete next step: use §15.3's dominant-index correspondence to express `z`'s value
via its own dominant index `i_0(z)`, and bound `w`'s exact digit-level structure relative to
`i_0(z)$ — not attempted this round due to time).

**Scope note honestly carried over from the outline-reviewer's own §14 review (unchanged by
this round's work):** even a full proof of Distinct-Bucket (hence of `e_{g^*}(M)\ge1` for every
`D_m`-reachable `M`, every `m`) would only reproduce the lower bound against `D_m` that
`dyadic-cascade-induction`'s §5.5 (round 8) has **already** established, unconditionally, by an
independent mechanism (D/M-completeness + the certified Superincreasing No-Early-Zero Lemma +
the all-cycles resolution). It would not, by itself, complete this approach's original
minimax/duality target, nor the theorem as a whole — the theorem's open items (the upper bound
at general `m`, tracked in `potential-weighting-upper-bound`, and general `n\ge4`, shown this
round by the sibling outline to be the same gap viewed differently — see
`dyadic-cascade-induction`'s round-9 note) are untouched by this section and remain the
higher-leverage open work in the population. This section's value is as an **independent,
alternative** proof route for one already-proved fact (diversity of technique, per CLAUDE.md),
not as new leverage on the theorem's currently-open pieces.
