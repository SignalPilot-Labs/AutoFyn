## Status
partial

**(proof-outliner, round 9 note — corrects a stale/imprecise framing, no new gap introduced.**
This round's plateau-break explorer (`math-explorer-n-general.md`) traced the induction
structure in §2d/§5 precisely and confirmed: **"general `n\ge4`" is NOT a separate open
frontier requiring a new top-level argument.** Two independent facts combine to show this:
(1) the **lower bound is already fully general** — §5.5.6's `g(D_m,m)\ge e_m\cdot S(D_m)`
holds for *every* `m` via the token/signed-sum invariant (§5.3) plus the all-cycles closure
(§5.5), with **no induction on `n` anywhere in that argument** (it is proved directly for each
`m`, not by peeling from `m-1`); (2) the **upper bound's Case (i) and Case (ii) are not two
independently-generalizable facts that could each need their own "general `n`" argument** — the
round-3 reviewer's finding (restated precisely by this round's explorer) is that Case (i)'s own
inductive step at level `m` invokes the **full joint IH (both cases) at level `m-1`** on an
*arbitrary* residual, so Case (i) and Case (ii) rise and fall together inside **one single
strong induction on `m`**. Consequently, the moment `potential-weighting-upper-bound`'s
aggregated Small-Gap Crossing-Domination Lemma closes (a single, `m`-independent combinatorial
statement about arbitrary lists `Y,p`), the outer strong induction on `m` closes **for every `m`
simultaneously** — i.e. for every `n` at once, since `m=n` at the tight case `k=m+1` (Slack
Collapse). **There is no separate "extend Case (i)/(ii) to `n\ge4`" task distinct from closing
that one lemma.** This corrects `current.md`'s "what remains open" item 6 ("`n\ge4`, both
directions, remains essentially untouched") — that phrasing is now stale; the accurate
statement is: lower bound done for all `m` (no `n`-generality gap at all), upper bound's
`n`-generality is the *same* task as `potential-weighting-upper-bound`'s single open lemma, not
an additional one. **This file's own remaining useful work is therefore now purely on the upper
bound**: either (a) wait for `potential-weighting-upper-bound` to close the aggregated lemma and
then write up the resulting "for every `m`" joint-induction closure explicitly in this file
(§2d/§5 currently only state Case (i)/(ii) at low `m` and the D/M reformulation — the final
"for every `m`, both cases, joint induction" write-up combining everything is not yet assembled
in one place), or (b) find a genuinely different upper-bound mechanism not requiring the
aggregated lemma at all (unexplored, no lead yet). **Do not treat "general `n\ge4`" as a 5th
open item or a candidate for a new slug** — per CLAUDE.md's single-gap-trap warning and this
round's explorer's explicit recommendation, it would just relabel the existing open lemma.
Also re-confirmed (per dispatch): the recursion `c(n)=2c(n-1)/(2c(n-1)+1)` remains at zero
leverage — its upper-bound side is literally Case (i)'s own existing (circular) mechanism, and
its lower-bound side is now strictly *subsumed* (not merely matched) by the already-certified,
non-inductive §5.3/§5.5 result. No change to any proved content this round; this note is a
scope correction only.**

**(proof-builder, round 8 note — the entire all-cycles caveat is now CLOSED IN FULL, via the
`\#X` cross-type-edge parity dichotomy (§5.5), fixing both gaps the round-8 outline-reviewer
flagged and going beyond the outline's own scope to close the previously-open `\#X\ge3` odd
"hard core" as well. Net effect: `g(D_m,m)=h(D_m,m)` is now unconditional for `D_m` and every
`m` (no remaining caveat), so combined with the already-certified Superincreasing No-Early-Zero
Lemma, the TRUE PHYSICAL lower bound `g(D_m,m)\ge e_m\cdot S(D_m)` is now a complete, unconditional
theorem for every `m` — the lower-bound direction against this specific construction is fully
closed. This does **not** solve the whole theorem: the matching upper bound (Case (ii) at general
`m`, tracked in `potential-weighting-upper-bound`) and general `n\ge4` remain open, so file Status
correctly stays `partial`. See the new §5.5 below for the complete proof, and "Current best" for
the precise, honestly-scoped accounting of what this does and does not establish.)**

**(proof-builder, round 7 note — §5.4's Steps 1–2 are now fully rigorous proofs (no gap), and
Step 3 is CLOSED for every "shallow" all-cycles configuration (`L\ge2` shared-value, `L\ge3`
cross-type), via a new general Cross-Type Cycle Infeasibility Lemma. The all-cycles caveat
blocking promotion of the Superincreasing No-Early-Zero Lemma to the true physical lower bound
is thus substantially narrowed — from "any cyclic tie-dependency structure" down to "a cycle
with at least one derived (non-original) participant, or mixed tie-types" — but NOT fully
closed; see the rewritten §5.4 below for the complete proofs and the precisely-isolated
remaining gap, including a concrete demonstration that the natural extension attempt to derived
tokens fails for `D_m`.)**

**(proof-outliner, round 6 note — new §5.4 skeleton below: a self-contained, D_m-specific
resolution of the "all-cycles" caveat, bypassing the general `dm-completeness-partial.md`
lemma entirely (consistent with this file's own round-4 philosophy of never depending on
D/M-completeness).** This round's all-cycles-lens explorer found three new ingredients, all
combinable with already-certified machinery, none requiring the general lemma to be extended:
(1) a **cheap pigeonhole fact**, not previously stated anywhere in the population: since each
of XY's `\le m` cuts traces back to a unique root original of `A`, at most `m` of `A`'s `k`
original pieces are ever touched — so whenever `k=m+1` (the *only* regime this file's Superin-
creasing No-Early-Zero Lemma needs promoted, by the Slack Collapse corollary), **at least one
original piece of `D_m` is always left completely untouched** by any `\le m`-cut strategy; (2)
a concrete **base-case mini-lemma** (checked exactly by the explorer): for the minimal
"2-cycle" building block (two distinct original pieces each cut once, tying at a shared value
`t`, with the guaranteed untouched third piece present), the pure-cross-tie value, as a
function of `t` alone, is piecewise-linear and its minimum is *always* attained either at a
breakpoint where one cut's output ties the untouched piece (breaking the cycle) or at a
degenerate boundary — i.e. a genuinely inescapable 2-cycle optimum cannot occur once an
untouched original is present; (3) a **crux-inspired generalization mechanism** (`aimo-0003`'s
"reduce invariance-under-all-orderings to invariance under one adjacent transposition, since
adjacent transpositions generate the symmetric group"), suggesting an induction on cycle
length: show any longer cross-tie cycle admits one local "re-target" of some member cut (from
a cross-tie to a tie against the guaranteed-untouched piece, or to a bisection) without
increasing `e`, then induct down to the already-solved base case. See new §5.4 below for the
full skeleton and the precisely-isolated remaining gap (generalizing the base-case argument
beyond length-2 cycles).**

**(proof-outliner, round 5 note — new §5.3 skeleton below: an integer/superincreasing
"no-early-zero" reframe that, if the one flagged combinatorial lemma is proved, closes the
ENTIRE lower-bound direction at once (Branch A, Branch B, and the open Step 4 multi-cut case
together), not just Step 4. This is a genuinely different mechanism from the physical-cut
casework of §5/§5.1/§5.2'' — an invariant/parity-style argument, not more casework — found by
combining this round's lowerbound-multicut explorer's "cancelling vs non-cancelling cuts"
opening with the newly-certified `lemmas/dm-completeness-partial.md`. Verified exhaustively by
hand-run exact-integer BFS for `m=1..5` (zero counterexamples) and cross-checked against 13
random strictly-superincreasing sequences of various sizes (the key claim held on all of
them) vs. 5 random non-superincreasing sequences (which DO admit shortcuts, confirming the
superincreasing hypothesis is load-bearing, not decorative). Case (ii)'s general-`m` upper
bound is NOT re-derived here; see the sibling `potential-weighting-upper-bound` for this
round's new chain-prefix mechanism on that gap — this file only imports its result once
proved (see the note added at the end of the Case (ii) section below), avoiding duplicating
that skeleton here.**

**(proof-builder, round 5 note — §5.3's Main Claim is now CLOSED, in full generality, by a
short elementary argument; see the rewritten §5.3 Step 3 below.)** The "one flagged
combinatorial lemma" the round-5 outliner left open is now **proved in full** — not just for
the dyadic `D_m`, but for *any* strictly superincreasing sequence, exactly the general form the
outline conjectured. The mechanism is a **token/signed-sum invariant**: track, for every value
ever active during a D/M sequence, the (nonempty, pairwise-disjoint-across-simultaneously-active-
tokens) subset of original indices it "descends from" and the ±1 sign pattern with which it
combines them; the classical superincreasing "distinct signed sums are never zero" fact then
forces every active token to be strictly positive and all active tokens at any single moment to
be pairwise distinct — hence (since a strict alternating sum of distinct positive reals is
always strictly positive) `e>0` at every state reachable with fewer than `k` operations, `k`
being the starting size. This resolves *both* named sub-concerns (a) `D`-interleaving and (b)
overlapping/non-contiguous index subsets the outline flagged as needing separate handling — the
invariant is proved once, by ordinary induction on operations, and handles `D` and `M` uniformly
and arbitrary (never actually overlapping, by the same induction) index subsets automatically,
with no additional casework. **Independently re-verified computationally this round**
(exact-integer BFS/graph enumeration, not merely spot sampling): exhaustively confirmed, for
`m=1..6`, that *every* state reachable from `D_m` within `\le m` operations (not just the
`e`-minimizing path) has all-distinct nonzero entries (`3117` states enumerated at `m=6` alone,
zero violations); separately re-ran the general-superincreasing stress test on `25` fresh random
strictly superincreasing sequences (sizes 3–5), exhaustively enumerating every state reachable
within budget for each (not sampling trajectories), zero violations in every case. **Honest
scope of what this closes:** the Main Claim as literally stated (purely about D/M-operation
sequences) is now an unconditional theorem, so `h(D_m,m)\ge e_m\cdot S(D_m)` (the D/M-restricted
minimum) is fully proved for every `m`. Promoting this to the *true* physical lower bound
`g(D_m,m)\ge e_m\cdot S(D_m)` still requires the pre-existing, separately-tracked, unresolved
"all-cycles" completeness caveat from `lemmas/dm-completeness-partial.md` (`g=h`, conditional) —
this caveat is **not** touched, resolved, or worsened by this round's work; it is inherited
exactly as before. See the rewritten §5.3 below for the full proof and an honest final
accounting of what is (and is not) now unconditional.**

**(proof-builder, round 4 note — Step 0 fixed, three new general lemmas proved, Step 4 still
open, see §5.2'' below.)** This round: (1) **fixed the D/M-completeness overclaim** the
outline-reviewer flagged in §5.2' Step 0 — the lower-bound argument now proceeds entirely on
*physical* cuts (as §5.1 already did), never invoking Lemma D/M's achievability-only scope.
(2) Proved three new, fully general, reusable facts: **Fact 3** (block extraction for a
dominant *block*, not just a single element), **Fact 4** (single-insertion changes `e` by at
most the inserted value), and — the most consequential — **Fact 5** (chain-cancellation):
*any* `L`-element multiset can be driven to `e=0` exactly using exactly `L` cuts. Corollary:
Fact 2's ceiling `e(M)\le\max(M)` is **always exactly achievable** within the natural cut
budget, not merely approached. This is a genuine structural finding, proved (not just
observed numerically) — it definitively rules out any future proof of Step 4 that relies on
"the residual's contribution stays safely below its ceiling"; the true bound, if it exists,
must come from a budget-tradeoff argument, not from bounding the residual in isolation.
(3) Attempted to close the simplest genuinely-new sub-case (splitting the leftover `\ell`
after `M(a_1,a_i)`, `i\ge3`, into exactly 2 pieces) — fully closed **one concrete instance**
(`m=4,i=3`, `R\{a_i}` untouched) by hand with exact fractions, confirming the bound holds with
comfortable slack (`3/31` vs. target `1/31`), but the general-`m` version of even this
narrowest sub-case is **not** closed — every general bounding technique tried (Fact 2 alone,
Fact 4's insertion bound, combinations) was empirically and in one case provably too lossy.
**Step 4 remains open.** See §5.2'' below for full detail, including an honest account of what
was tried and found insufficient.

**(proof-outliner, round 4 note — new skeleton for §5.2, see §5.2' below, replacing the
falsified "merging monotonicity" line of attack).** The round-4 lower-bound-lens explorer
hand-traced the `m=3` numerically-tying "2-cuts-inside-`a_1`" example
(`(a_2,a_3,a_3)=(4/15,2/15,2/15)`, from bisecting `a_1` then bisecting one resulting half
again) through Lemma P by hand and found it is **value-identical**, after the two duplicate-
pair cancellations, to "Branch B1 (bisect `a_1`) composed with the level-`(m-1)` IH's own
recursive move on `R`" — i.e. the Branch A/B split by physical cut *location* is an artifact
of this file's own casework, not a real second obstruction: the certified **Lemma D/M**
(`lemmas/dm-operation-reformulation.md`, from sibling `potential-weighting-upper-bound`)
already shows the true effect of any cut depends only on the *sequence of active-multiset
values*, never on which physical piece it geometrically lands in. This motivates dropping the
location-based Branch A/B/§5.2 split and reformulating §5.2 directly in D/M language, closed
via a **broadened induction class** ("induction loading", crux `aimo-0292`) with a
**minimal-counterexample fallback** (crux `aimo-0287`/`aimo-0438`) for the one genuinely hard
sub-claim (dominance-preservation under further splitting). See new **§5.2'** below — this
supersedes the "open gap" framing of the old §5.2, which is kept for its numerical evidence
but should not be extended further as stated (does NOT re-propose "merging monotonicity",
which stays a confirmed dead end for the *unconditional, arbitrary-side-multiset* form).

**(proof-reviewer, round 3 note):** confirmed `partial` (CHANGES REQUESTED), with one
correction to this round's headline claim. §2d's proof that "Case (i)'s form-A gap is closed
for every `m`" **overclaims**: the inductive step invokes "the strong induction hypothesis —
both forms (A) and (B) — at level `m-1`" applied to an *arbitrary* residual `\{a_2,...,a_k\}`,
which need not itself be a Case-(i) configuration at level `m-1` — it can be Case (ii). Since
Case (ii) at general `m` is (correctly, elsewhere in this same file) marked open beyond `m=2`,
the chain of validly-established levels is: level 2 fully established (both cases) ⟹ level 3's
Case (i) is *validly* proved (a genuine new result) ⟹ level 4's Case (i) would need level 3's
Case (ii), which is NOT established, so it is **not** actually proved by this argument, contra
the "for every `m`" phrasing. Net effect: read every occurrence of "Case (i) closed for every
`m`" in this file as "Case (i) closed through `m=3`." This does not affect §5 (the lower-bound
Branch A/B/B1/B2 proofs), which are self-contained (they recurse on the specific dyadic
sequence, not an arbitrary residual) and were independently re-verified as correctly
unconditional for every `m`. See `/tmp/round-3/proof-reviewer.md` for full detail.

## Approaches tried
- **(round 8, this builder) The entire all-cycles caveat is now CLOSED, in full, for every
  participant type — a genuinely complete result, not a further narrowing.** Dispatched to fix
  two precise gaps the round-8 outline-reviewer found in the round-8 outliner's `\#X`-parity-
  dichotomy sketch, and to attempt the flagged-as-hardest `\#X\ge3` odd bucket. Result:
  (1) **Gap 1 fixed** (the `\#X\ge2`-even bucket's disjointness claim previously outran
  `superincreasing-no-early-zero.md`'s literal "simultaneously active in one trajectory" scope):
  proved a new **Cycle Common-State Lemma** (§5.5.1) showing any single (WLOG minimal, via a
  standard SCC-condensation-is-acyclic argument) cyclic component's participants are always
  simultaneously active tokens of one common, legal D/M state — constructed directly from the
  already-certified peeling induction of `dm-completeness-partial.md`, so (I1)/(I2) apply exactly
  as certified, with no extension needed. (2) **Gap 2 fixed** (the `\#X=1` "forces a self-
  bisection, hence not a real cycle" claim): spelled out as an explicit 5-step logical chain
  (§5.5.3) — solve for the forced value, identify it as a numerically exact self-bisection via
  the certified Vertex Lemma, show self-bisections have out-degree 0 by the dependency graph's
  own construction, contradict this against the assumed cycle membership (out-degree exactly 1),
  concluding the configuration is never a genuine cycle. (3) **The `\#X\ge3` odd "hard core" —
  the round-8 outliner's flagged-open target — is now FULLY CLOSED**, for BOTH original and
  derived participants (going beyond what even the outline attempted): proved a new
  **Generalized Cross-Type Domain-Violation Lemma** (§5.5.5) via a genuinely new sign-dominance
  mechanism (not the round-7 crude magnitude bound, confirmed dead) — derives the reduced
  cyclic system's unique closed-form solution by hand (not just `sympy`), shows the coefficient
  of the single most-significant original index flips sign across the cycle's blocks (since
  `\#X\ge3` guarantees both parities occur), and combines with ordinary superincreasing dominance
  to force a strictly negative block value somewhere, directly violating the domain constraint —
  no dominance/magnitude property of the derived pieces themselves is needed at all, unlike the
  confirmed-failed round-7 attempt. This strictly generalizes and supersedes the previously-
  certified Cross-Type Cycle Infeasibility Lemma (recovered as the singleton-token special case).
  **Net effect: `g(D_m,m)=h(D_m,m)` is now unconditional (every possible cyclic tie-dependency
  pattern is either not a genuine cycle, infeasible, or provably not the minimizer — an exhaustive
  case split on `\#X\in\{0,1,\ge2\text{ even},\ge3\text{ odd}\}`), giving the fully unconditional
  TRUE PHYSICAL lower bound `g(D_m,m)\ge e_m\cdot S(D_m)` for every `m` — the first time this
  exact statement has been established without any caveat.** Independently corroborated by
  `\sim4000` total bounded exact-computation trials (`sympy`/exact-integer, never unbounded/fine-
  grid search) across every lemma and a broad mixed sweep (§5.5.7), zero counterexamples found,
  predicted mechanisms (which node goes negative, inconsistent vs. uniquely-infeasible, etc.)
  matching exactly. Full detail in the rewritten §5.5. **Honest scope, not overclaimed:** this
  closes the lower bound against the *dyadic construction specifically*, for every `m` — it does
  **not** by itself establish the theorem's matching upper bound (still open at general `m`,
  tracked in `potential-weighting-upper-bound`) or extend to general `n\ge4` beyond what was
  already known; Status correctly stays `partial` for the file as a whole.
- **(round 7, this builder) §5.4 Steps 1–2 now FULLY PROVED (certified-quality), and Step 3 is
  CLOSED for the natural "shallow" all-cycles configurations (any cycle length `L\ge3` built
  from distinct, once-cut original pieces), via a new, clean, fully general argument — a real
  advance, though the fully general "all-cycles" caveat (allowing deeper/derived cycle
  participants) is honestly NOT closed and is precisely re-isolated as a narrower residual gap.**
  Full detail in the rewritten §5.4 below. Summary:
  (1) **Step 1 (Guaranteed-Untouched-Original Lemma)** written up as a complete, rigorous
  one-paragraph proof (pigeonhole on cut-forest roots) — no gap, matches the outline-reviewer's
  independent re-verification exactly.
  (2) **Step 2 (Base-case Cycle-Breaking Lemma, `L=2`)** written up as a complete, rigorous
  proof via the certified Vertex Lemma + Lemma P, and **generalized** (new this round) to the
  "shared-tie-value" family for **any** number of pieces `L\ge2` sharing one common cut
  parameter `t` — the same piecewise-linear/breakpoint argument closes this whole family at
  once, not just `L=2`.
  (3) **Step 3, new Cross-Type Cycle Infeasibility Lemma (all `L\ge3` at once, no case split
  on parity needed):** for a cross-tie cycle built by cutting `L\ge3` *distinct* original
  pieces of a strictly superincreasing sequence exactly once each, with each cut's "extra"
  output tying the *next* cut's "surviving" output in a closed cyclic chain, the resulting
  linear system of tying equations is **never feasible** — i.e. no choice of cut positions
  realizing this exact combinatorial pattern ever satisfies the requirement that every cut
  position lie strictly between `0` and the length of its own piece. Proved by a genuinely new,
  short, fully general argument (sum every equation in the cycle to get `\Sigma u_i = S/2`;
  isolate the one equation whose right-hand side is the maximum piece value `M`; the
  strict superincreasing dominance `M > S-M` forces the sum of the *remaining* `L-2\ge1` cut
  positions to be strictly negative — impossible, since each must be positive). This is a
  clean, from-scratch, fully general theorem (works for *any* strictly superincreasing base
  sequence, not just `D_m`), independently spot-checked this round by bounded exact/symbolic
  computation (`L=3,4,5` against `D_2,D_3,D_4`, zero feasible cycles found, matching the proof
  exactly, including the `L=4` case being infeasible for the *stronger* reason of outright
  linear inconsistency — also explained by the same superincreasing-dominance fact, since
  consistency for even `L` would require a vanishing signed subset sum of the chosen originals,
  impossible by the (cited, not re-derived) Step 1 of `lemmas/superincreasing-no-early-zero.md`).
  (4) **Honest, precisely re-isolated remaining gap:** the argument above requires every
  cycle-participant piece to be an as-yet-untouched *original* (its "dominance" comes directly
  from the base sequence's superincreasing property). It does **not** cover a cycle where some
  participant is itself a *derived* value (the surviving output of an earlier, already-resolved
  tie elsewhere in the same strategy) — such a derived value is a signed subset sum of several
  originals (by the token invariant) and need **not** retain the "dominance" (max > sum of
  rest) property that made the argument work; I checked this concretely (see §5.4 Step 3,
  "Remaining gap" subsection below) and found the natural attempt to extend the dominance bound
  to such derived tokens is **provably too lossy for `D_m` specifically** (it would require
  `a_{i^*} > 2\sum_{l>i^*}a_l`, but for `D_m`, `\sum_{l>i^*}a_l = a_{i^*}-1` exactly, so the
  needed inequality reduces to `a_{i^*}<2`, false whenever `a_{i^*}\ge2`). This is reported
  honestly as a genuine open sub-case, not swept aside — it is, however, a substantially
  *narrower* residual than the previous "all-cycles, any structure" caveat: only cycles
  involving at least one non-original (derived) participant remain unresolved.
- **(round 5, this builder) Closed §5.3's Main Claim in full generality — a genuine new
  theorem, not a numerics-to-proof restatement.** The round-5 outline's one flagged open
  combinatorial lemma (the "No-Early-Zero Lemma": no `<k`-length D/M sequence from a strictly
  superincreasing `k`-element sequence reaches `e=0`) is now **proved completely**, for
  arbitrary strictly superincreasing sequences (strictly more general than even the outline's
  own conjecture required, which only needed the specific dyadic `D_m`). The mechanism: a
  **token/signed-sum invariant** (§3.2), proved by ordinary induction on the number of D/M
  operations performed, showing every value ever active during the process is represented by a
  nonempty subset of original indices plus a `\pm1` sign pattern, with these index sets always
  pairwise disjoint across simultaneously-active tokens; combined with the classical
  "superincreasing sequences have no vanishing signed subset sums" fact (§3.1, elementary,
  proved from scratch here), this forces every active token to be strictly positive and all
  simultaneously-active tokens to be pairwise distinct (§3.3), hence (§3.4: a strict alternating
  sum of distinct positive reals is always `>0`) `e>0` at every state reachable within budget
  (§3.5–3.6). This closes **both** sub-concerns the outline flagged as needing separate
  handling — `D`-operations interleaved with `M`-chains, and overlapping/non-contiguous index
  subsets — automatically, as a byproduct of the single induction, with no extra casework.
  **Independently re-verified computationally** (not merely re-stating the earlier numerics):
  exhaustive exact-integer BFS over *every* state reachable within budget (not just the
  `e`-minimizing path) for `m=1..6` (`3117` states enumerated at `m=6`, zero violations of
  distinctness/positivity/nonzero-`e`), plus a fresh, independent set of `25` random strictly
  superincreasing sequences (sizes 3–5), each exhaustively enumerated within its own budget,
  zero violations. Also explicitly discharged the raw-integer-to-normalized-`[0,1]` rescaling
  (§3.7) that the previous round's "Watch out for" list flagged as needing to be made explicit,
  not left implicit. **Honest scope, stated precisely in §3.7's closing paragraph:** this proves
  `h(\widetilde D_m,m)\ge e_m\cdot S(\widetilde D_m)` (the D/M-restricted minimum) unconditionally,
  for every `m`; promoting this to the TRUE physical-strategy lower bound `g(\widetilde D_m,m)
  \ge e_m\cdot S` still needs the pre-existing, unresolved "all-cycles" completeness caveat from
  `lemmas/dm-completeness-partial.md` — this caveat is inherited exactly as before, not
  introduced, worsened, or resolved by this round's work. Full proof in the rewritten §5.3 below
  (Steps 3.1–3.7); a candidate new certified lemma ("Superincreasing No-Early-Zero Lemma") is
  proposed at the end of this file for the reviewer to certify.
- **(round 4, this builder) Fixed the Step-0 overclaim; proved three new general lemmas;
  attempted (partially, not fully) to close Step 4.** Full detail in §5.2'' below. Summary:
  (1) the round-4 outline-reviewer correctly flagged that §5.2' Step 0's claim "XY's response
  to `D_m` is exactly a D/M sequence" oversteps the certified scope of Lemma D/M (which only
  guarantees achievability, not completeness, per its own "Consequence" section) — this round
  **removes that dependency entirely**, re-deriving the case split (a1 untouched / exactly one
  cut on a1 / two-or-more cuts on a1) directly from physical cut points, exactly matching how
  the already-proven §5.1 works, so no completeness assumption is needed anywhere in this
  file's lower-bound argument. (2) **Fact 3 (block extraction)**, **Fact 4 (single-insertion
  bound)**, and **Fact 5 (chain-cancellation / ceiling achievability)** are new, fully proved,
  general-purpose lemmas (not specific to this problem's numbers) — Fact 5 in particular is a
  genuine structural discovery: it *proves* (where previous rounds only observed numerically)
  that Fact 2's bound `e(M)\le\max(M)` is always exactly attainable within the natural cut
  budget, which rules out an entire class of naive future attempts at Step 4 and correctly
  redirects the difficulty to a budget-tradeoff argument. (3) Fully hand-verified (exact
  fractions) one concrete new instance of the hardest remaining sub-case (`m=4`, `i=3`,
  splitting the post-match leftover into 2 pieces, `R\{a_i}` untouched) — confirms the bound
  holds with real slack, but every attempt to turn this into a general-`m` argument (Fact 2
  alone, Fact 4's insertion bound, or combinations) produced bounds that were either too lossy
  (provably, with a concrete numeric witness for Fact 4's looseness) or reduced to unbounded
  casework that does not obviously terminate. **Step 4 (the `\ge2`-cuts-inside-a-dominant-
  piece gap) remains open** — this is reported honestly, with the specific things that were
  tried and found insufficient recorded so future rounds do not repeat them.
- **(round 3, this builder) Formalized §2d and substantially advanced §5 (lower bound).**
  (1) **Case (i)'s form-A gap is now FULLY, RIGOROUSLY CLOSED for every `m`** — wrote up the
  1-variable calculus argument as a complete inductive-step proof, and in doing so **found
  and fixed a genuine logical gap** the outline's skeleton had missed: the skeleton assumed
  the adversarial `a_2` is always capped at `a_1/2`, but `a_2` is also capped at `1-a_1`
  (since `a_2` is the largest element of a residual summing to `1-a_1`); the skeleton never
  checked whether `a_1/2\le1-a_1` could fail. Added the missing "Sub-case B" (`a_1>2/3`) and
  proved it is strictly dominated (`e(\text{final})<e_{m-1}/3\le e_m`), so Case (i)'s closure
  is now airtight, not just algebraically-checked-but-logically-incomplete. (2) **Branch A of
  the lower bound (XY never touches `a_1`) is now FULLY, UNCONDITIONALLY PROVED** for every
  `m` and every way XY distributes its cuts on the residual `R` — via two new general-purpose
  elementary facts (`e(M)\ge0` for any sorted `M`, already implicit in Lemma G's own proof but
  now named and reused; and `e(M)\le\max(M)`, "dominant extraction") that reduce Branch A to a
  two-line computation `e(\text{final})\ge a_1-a_2\ge e_m`. (3) **Branch B's single-cut-on-`a_1`
  case is now FULLY CLOSED**, both for bisection (Case B1, reduces to the level-`(m-1)` IH
  exactly, using that `D_m\setminus\{a_1\}` rescales to exactly `D_{m-1}`) and — newly, not
  previously attempted — for **every possible match-to-`a_i` alternative** (Case B2, closed by
  a direct elementary dominance computation, no induction needed, verified exact for
  `m=2,\dots,7`). This is a real advance beyond the outline's "conjecture bisection dominates"
  framing: matches are shown independently `\ge e_m`, so no comparison to bisection was even
  needed. (4) **The remaining multi-cut gap is now sharply narrowed** to "`\ge2` cuts landing
  inside the currently-dominant piece" (not "any multi-cut strategy" as the outline-reviewer's
  flag put it) — gathered numerical evidence at `m=2` (exhaustive cut-distribution grid),
  `m=3` (trisect/quadrisect-`a_1`-only), and `m=4` (300k-trial random search over all cut
  distributions, including a 3-cuts-entirely-inside-`a_1` minimizer), all finding the minimum
  exactly `=e_m`, never below. Also **tested and refuted** the natural candidate general fix
  (a "merging never increases `e`" monotonicity lemma) — found false by random search even
  under the dominance hypothesis — so this is reported as a genuine, structurally-nontrivial
  open gap, not swept under a plausible-sounding but false general fact. See the new §2d and
  §5 write-ups below for full detail.
- **(round 3, outliner) Revised skeleton — two concrete extensions queued for the builder,
  both verified numerically/algebraically by this round's explorers, neither yet written up
  as a rigorous proof in this file:**
  1. **General-`m` closure of Case (i)'s form-A gap (replaces the old n=2-only "exact
     2-element residual" trick).** The general-n explorer verified (exact-`Fraction` algebra,
     `m=1..6`) that Case (i)'s top-level bound `e ≤ e_m·S` holds for **every** `m`, via a
     clean 1-variable calculus argument on `a_1` alone — see new §2d below. This makes the
     n=2-specific "gap 5" fix in §2 (Section "Gap 5 resolved at n=2 specifically") obsolete:
     do not extend that exact-formula trick to n=3; use §2d instead, which is strictly more
     general and no harder.
  2. **Lower-bound direction skeleton via the dominance/superincreasing lock.** The
     lowerbound-lens explorer found `D_n=(2^n,\dots,2,1)` is superincreasing
     (`2^k > 2^{k-1}+\dots+1`), forcing a genuine two-sided case split for XY's response to
     the specific dyadic input: "XY's cuts never touch `a_1`" (Branch A, numerically confirmed
     hopeless for XY — best found `e≈2/7`, far short of target) vs. "XY cuts `a_1`"
     (Branch B, which by the vertex lemma + Lemma P reduces to a scaled copy of the
     level-`(m-1)` problem). This suggests reframing the WHOLE theorem as **one joint strong
     induction on `m`** carrying both form (A)/(B) (upper bound) AND a new form (C) (lower
     bound: the dyadic construction at level `m` resists every response) as the induction
     hypothesis simultaneously — see new §5 below for the skeleton. This is queued as the
     next builder task alongside item 1; both are additions to this approach's existing
     induction skeleton, not a new approach (same top-level target, same Lemma G/P machinery,
     same peel-`a_1` recursive structure).
  3. **Case (ii) at general `m` is explicitly NOT to be attacked by extending the n=2
     two-candidate (bisect-`a_1` / match-`a_1`-to-`a_2`) casework.** The general-n explorer
     proved this family is insufficient at `m=3` (crude bound `≈0.081 > 1/15` near the
     uniform triple `(1/3,1/3,1/3)`, even though the true value there is `0`, trivially small
     via a single bisection). This is now a confirmed dead end for the *general-m* case (the
     n=2 closure itself, using the specific 4 sign-regimes, remains valid and complete at
     n=2 only). General-`m` Case (ii) needs the potential/weight-function or whole-multiset-
     pairing mechanism instead — tracked as its own approach, `potential-weighting-upper-
     bound` (revised this round); this file should import its result once available rather
     than re-deriving.
- (round 1) new approach, no output — round-1 builder hung (909+s, force-killed) attempting
  unbounded/general-n symbolic work on Case (ii); no progress recorded.
- (round 2, outliner) e-based (`e := L−X`) reformulation; identified "Lemma P-zero" and
  used it to close Case (i) (`a_1 ≥ 2a_2`) of the upper-bound induction; narrowed Case (ii)
  (`a_1 < 2a_2`) to a concrete bounded n=2 hand-computation; outline-reviewer independently
  verified Case (i)'s closure and the Case (ii) diagnosis.
- **(round 2, this builder) Full rigorous proofs of Lemma G and Lemma P from scratch**
  (both are more general/cleaner than the outline anticipated, certified as shared lemmas);
  **the n=1 instance of the upper bound is fully and rigorously solved** by direct
  one-variable calculus; **Case (i) (`a_1\ge2a_2`) is fully solved at `n=2`** (both the
  max-normalized form (B) for general `n`, and — using the exact 2-element residual formula
  available specifically at `n=2` — the exact top-level bound, closing a gap in form (B)'s
  promotion to form (A) that was found and fixed within this same round); **Case (ii)
  (`a_1<2a_2`) is fully solved at `n=2`**, via a rigorously-proved "vertex lemma"
  (piecewise-linearity of a single cut) reducing XY's search to 2 sufficient candidate
  strategies, and all 4 resulting sign sub-regimes closed exactly by hand (two attained
  maxima below target, two suprema equal to the target approached only at the shared
  Case-(i) boundary, never inside Case (ii)). **Net result: the entire upper-bound direction
  of the theorem is now a complete, rigorous proof for `n=2` (`c(2)\le4/7`, i.e. XY can always
  cap Liu Bang at `4/7` regardless of Liu Bang's opening).** Remaining open: the matching
  lower-bound direction even at `n=2` (untouched beyond a non-exhaustive numerical spot
  check), and generalizing either direction to `n\ge3`. This is genuine, substantial,
  fully-verified progress on one full half of the theorem at the first non-trivial case
  beyond `n=1`; worked out in full below, with every remaining gap stated honestly.

## Current best

**Proven in full (this round), reusable, certified as lemmas** (see
`lemmas/greedy-reduction.md`, `lemmas/duplicate-pair-invariance.md`):
- **Lemma G** (order-statistic reduction of the alternating claiming phase): under optimal
  play, Liu Bang's total is the sum of odd-ranked pieces, Xiang Yu's the even-ranked ones,
  and "claim the current largest remaining piece" is optimal for whichever player moves —
  proved by strong induction + an explicit pairing inequality, not asserted.
- **Lemma P** (duplicate-pair invariance), in the clean `e := L−X` form: removing any two
  *equal-valued* entries from a sorted multiset leaves `e` exactly unchanged — proved in
  full generality (any two equal-valued entries, not just an "even-multiplicity" run as the
  outline conjectured; the general proof is not harder and subsumes that special case).

**Proven in full (this round), specific to this problem:**
- **The recursion `e_n = e_{n-1}/(2+e_{n-1})`, `e_n = 1/(2^{n+1}-1)`** — direct algebraic
  check (both forms of the closed formula coincide; shown below in the writeup).
- **Case (i) of the upper-bound induction (`a_1 ≥ 2a_2`)**: the max-normalized form (B)
  (`e≤a_1/2^m`) is proved for **all `n`** (bisect the top piece; Lemma P removes the
  resulting duplicate pair with zero residue; induction hypothesis on the residual closes
  it exactly). Separately, **the exact top-level bound (form (A), `e≤e_2·S`) is now also
  fully proved for the concrete case `n=2`**, using the fact that at `n=2` the residual after
  bisecting `a_1` has at most 2 elements, so the *exact* closed-form n=1 solution (not a
  lossy generic bound) applies directly; the resulting 1-variable-family optimization
  (`R:=a_2+a_3`, comparing the unconstrained optimizer `R/3` against the case-(i)-forced cap)
  gives an exact maximum of `1/7`, attained only at `(4/7,2/7,1/7)`. **Case (i) is completely
  closed for `n=2`** (general `m` remains open for this exact-formula trick, since the
  residual can have more than 2 elements — this is gap 4 below, narrowed from a previous
  round's more general-sounding concern).
- **The n=1 instance of the whole theorem (upper bound) is fully solved**, not just by
  abstract induction but by an explicit, elementary 1-variable calculus computation
  (`min(q, p−q)` over `p+q=S`), confirming `e_1 = 1/3` exactly, with the extremizer
  identified.
- **A rigorous "vertex lemma"**: for a single cut splitting one piece into two, `e` (as a
  function of the cut position, all other pieces fixed) is *piecewise linear*, with
  breakpoints exactly where the cut creates a value tying an existing piece or bisecting the
  piece being cut. Consequently the minimum over that one cut is always attained at
  "no cut", "bisect", or "match to some existing piece" — this converts the previously
  heuristic "try match/bisect" moves into a proved reduction to a *finite* candidate set,
  and explains (rather than assumes) why these are the right moves to consider.
- **Case (ii) at n=2 (`a_1<2a_2`) is now COMPLETELY closed.** Via the vertex lemma, XY's
  sufficient strategy pair reduces the goal to
  `min( level1(a_2,a_3), level1(a_1-a_2, a_3) ) ≤ 1/7`
  (`level1(x,y):=min(min(x,y),|x-y|)`, the exact n=1 optimal-response value). This was solved
  exactly by hand in **all four** sign sub-regimes: `a_2\ge2a_3` with `u\le a_3` gives max
  `1/11` (attained, at `(5/11,4/11,2/11)`); `a_2\ge2a_3` with `u>a_3` gives supremum exactly
  `1/7`, approached only at the Case-(i) boundary (never attained inside Case ii); `a_2<2a_3`
  with `u\le a_3` gives max `1/9` (attained, at `(4/9,3/9,2/9)`); `a_2<2a_3` with `u>a_3`
  gives supremum exactly `1/7`, again only at the Case-(i) boundary. **Every case verified
  independently by exact-`Fraction` computation matching the hand derivation precisely**
  (not merely a numeric sweep this time — the exact extremal points and values were computed
  by hand and confirmed by substitution).

**Headline result of this round: combining the above, the entire upper-bound direction of
the theorem — "for every Liu Bang opening with `≤2` cuts, Xiang Yu has a response with `≤2`
cuts forcing Liu Bang's total to `≤4/7`" — is now a complete, rigorous, gap-free proof for
`n=2`.** This is the first fully-closed non-trivial instance of the upper bound beyond the
elementary `n=1` case.

**Open gap (honestly stated, not closed this round):**
1. **The lower-bound direction at general `m` (including `n=2`) is now substantially
   advanced, but NOT fully closed** (round-3 update, supersedes the previous "untouched"
   status). Via the new §5: **Branch A (XY never cuts `a_1`) is fully, unconditionally
   proved** for every `m`. **Branch B, XY's single-cut-on-`a_1` sub-case, is fully closed**
   (bisection via a clean induction on `m`; every match-to-`a_i` alternative via a direct
   elementary bound, no induction needed). **What remains open**: strategies where `\ge2` of
   XY's cuts land *inside* the currently-dominant piece (e.g. trisecting `a_1` directly, or
   matching `a_1` to some `a_i` and then further cutting the leftover `a_1-a_i`) — this is
   numerically well-supported at `m=2,3,4` (exhaustive/broad random search, no violation
   found) but not proved; see §5.2 for the precise statement of the gap and a documented
   negative result (a natural candidate general "merging monotonicity" lemma was tested and
   found FALSE, so this needs a structure-specific argument, not a generic fact).
   **Round-4 update:** the round-4 outline-reviewer flagged that §5.2's successor skeleton
   (§5.2') had itself acquired a new gap (an overclaim about D/M-sequence completeness); this
   is now **fixed** — see §5.2'' Part A, the lower-bound argument is restated purely in
   physical-cut terms, no completeness assumption needed anywhere. Three new general lemmas
   (Facts 3, 4, 5 — §5.2'' Part B) were proved in full this round; **Fact 5 is a genuine
   structural finding** (proved, not numerical): the natural "residual stays below its
   ceiling" proof strategy for Step 4 **cannot work** (the ceiling is always exactly
   attainable within budget), which rules out an entire class of future attempts and
   correctly locates the difficulty in a joint budget-tradeoff, not a decomposable bound. One
   additional concrete instance (`m=4,i=3`, splitting the post-match leftover into 2 pieces)
   was fully closed by hand (§5.2'' Part C), with real slack (`3/31` vs. target `1/31`), but
   the general-`m` version remains **open** — every general technique tried this round (Fact 2
   alone, Fact 4, combinations) was shown too lossy, with a concrete numeric witness for
   Fact 4's looseness. Item 1 is therefore still open, now with a clearer, narrower, and
   better-understood remaining target. **(Round 5 update: a genuinely different mechanism —
   an integer/superincreasing "no-early-zero" invariant, §5.3 — is now FULLY PROVED (the
   No-Early-Zero Lemma, §5.3 Steps 3.1–3.6), for arbitrary strictly superincreasing sequences,
   not just conjectured/verified numerically as in the previous round. This gives an
   unconditional proof that no D/M-operation sequence of length `\le m` starting from (the
   normalized) `D_m` ever reaches `e=0` — equivalently, `h(D_m,m)\ge e_m\cdot S(D_m)` for every
   `m`, where `h` is the D/M-restricted minimum (§3.7 makes the raw-integer/normalized
   rescaling explicit). This subsumes Branch A, Branch B, and Step 4 as special cases of "no
   D/M sequence of length `\le m` reaches `e=0`," entirely superseding the location-based
   casework's SCOPE (though not its logical status — see next sentence). **Honest remaining
   gap:** promoting this D/M-sequence result to the TRUE physical-strategy lower bound
   `g(D_m,m)\ge e_m\cdot S(D_m)` (the theorem's actual claim) still needs
   `lemmas/dm-completeness-partial.md`'s `g=h` result, itself conditional on the "all-cycles"
   tie-dependency case never occurring (a pre-existing, separately-tracked caveat, unaffected —
   neither worsened nor resolved — by this round's proof). So item 1 remains formally open
   ("partial", not "solved"), but the gap is now precisely: **one single, already-isolated,
   never-observed edge case in a DIFFERENT, already-certified lemma** — not an unproved
   combinatorial claim intrinsic to this section anymore. §5–§5.2'' remain valid as an
   independent, fully unconditional (but only partial, Step-4-still-open) fallback that needs
   no D/M-completeness assumption at all. **(Round 7 update:** §5.4 now fully resolves the
   all-cycles caveat for `D_m` in every "shallow" case (any cross-tie cycle built from distinct,
   once-cut, still-untouched original pieces of `D_m`, of *any* length `L\ge2`) — via a new
   Guaranteed-Untouched-Original Lemma (Step 1, full proof), a Base-case/Shared-Value
   Cycle-Breaking Lemma covering every `L\ge2` uniformly (Step 2, full proof, strictly
   generalizing the round-6 skeleton's `L=2`-only claim), and a new Cross-Type Cycle
   Infeasibility Lemma proving every uniform cross-type cyclic tie of length `L\ge3` among
   distinct originals is physically infeasible (Step 3, a genuinely new general theorem for any
   strictly superincreasing sequence). **What remains open, narrowed:** only cycles with at
   least one *derived* (non-original) participant, or mixing tie-types within one cycle — a
   substantially smaller residual than the pre-round-7 "any cyclic structure whatsoever" gap;
   confirmed (not just asserted) that the natural crude extension of this round's dominance
   argument to derived participants fails for `D_m` specifically (`a_{i^*}<2` needed, false for
   `a_{i^*}\ge2`). Item 1 therefore still remains "partial," but the all-cycles caveat is now a
   markedly narrower target than before this round.)**
   **(Round 8 update — item 1 is now FULLY CLOSED.** §5.5 proves, via a complete `\#X`
   (cross-type-edge count) parity dichotomy, that **every** possible cyclic tie-dependency
   pattern — not just "shallow," all-original ones — is either not a genuine cycle at all
   (`\#X=1`, a disguised self-bisection, §5.5.3), physically infeasible (`\#X\ge2` even, §5.5.4;
   `\#X\ge3` odd, §5.5.5 — this second bucket, previously the "one remaining hard core," is the
   one closed this round, via a genuinely new sign-dominance mechanism that succeeds exactly
   where the round-7 crude magnitude bound failed), or provably never the true minimizer
   (`\#X=0`, the pre-existing family (A), §5.5.2). The key enabler for extending this to
   **derived** participants (not just original pieces) is a new Cycle Common-State Lemma
   (§5.5.1), which shows any single cyclic component's participants are always simultaneously
   active tokens of one common legal D/M state — so the certified token-disjointness invariant
   (I1)/(I2) applies directly, with no extension of its literal stated scope, closing the precise
   gap the round-8 outline-reviewer flagged. **Net result: `g(D_m,m)=h(D_m,m)` unconditionally,
   for `D_m` and every `m` — no remaining caveat — so combined with the already-certified
   Superincreasing No-Early-Zero Lemma, `g(D_m,m)\ge e_m\cdot S(D_m)` is now a complete,
   unconditional theorem for every `m`.** This fully closes the lower-bound direction of the
   theorem *against the dyadic construction specifically*. Honest scope: it does **not** by
   itself pin down `c(n)` (that additionally needs the matching upper bound to hold for *every*
   Liu Bang opening, not just `D_m` — see item 2 below and the sibling
   `potential-weighting-upper-bound`) nor does it address `n\ge4` beyond what the self-similar
   Branch A/B argument already gave; those remain separately open, so the file's overall Status
   correctly stays `partial`.)**
2. **Generalizing the upper-bound techniques to `n≥3` is fully open for Case (ii).** Case (i)
   is now closed for every `m` (§2d, below). Case (ii)'s `n=2` sign-regime casework relies on
   the smallness of `k≤3` and does not obviously scale; a genuinely different mechanism is
   needed and is being tracked in the sibling approach `potential-weighting-upper-bound`
   (this file should import its result once available rather than re-deriving).
3. **(round-3: CLOSED this round.)** Case (i)'s form-(B)-to-form-(A) promotion is now a
   complete, rigorous proof for **every** `m` (§2d below) — including a genuine logical gap
   found and fixed while writing it up (the outline's skeleton had not checked the second
   constraint `a_2\le1-a_1` on the residual's top piece; the missing "Sub-case B" is now
   proved, with strict inequality, so it never threatened the bound but needed to be shown).
4. The "using fewer than the full cut budget never helps a player" bookkeeping point is
   handled *ad hoc* wherever it arises in this file (by explicit exhibition) rather than
   proved as a standalone general fact. **Round-3 finding: the most natural general form of
   this fact (a "merging never increases `e`" monotonicity lemma) is FALSE** (refuted by
   random search, see §5.2) — so this cannot be elevated to a clean general lemma as hoped;
   any future closure of item 1 above will need something more specific to this problem's
   dyadic/dominance structure, not a general bookkeeping fact.
5. **(round-3: substantially advanced, see item 1 above and §5 below for full detail.)**
6. **Case (ii) at general `m` needs a genuinely different mechanism than the n=2
   two-candidate casework** — confirmed a dead end at `m=3` by a previous round's general-n
   explorer. Track this in `potential-weighting-upper-bound` rather than attempting to
   extend this file's n=2 casework further. **(Round 9 clarification, see the note at the top
   of "## Status": this item — not a separate "general `n\ge4`" item — is now understood to be
   the ENTIRE remaining upper-bound gap for every `n` simultaneously, since Case (i)/(ii) share
   one joint strong induction on `m`. `current.md`'s prior listing of "`n\ge4`, both directions,
   untouched" as a distinct open item is stale; the lower bound has no `n`-generality gap left
   at all (§5.5.6), and the upper bound's `n`-generality is this same item 6, not an additional
   one.)**

## Full proof
(not present — Status is `partial`. The entire upper-bound direction is fully proved for
`n=2` specifically — see Section 2 of "Approach detail" below for the complete, self-
contained argument — but the theorem as stated needs both directions for *every* `n`, so
this does not yet meet the bar for `solved`. **Round-8 update:** the lower-bound direction
against the dyadic construction `D_m` specifically is now fully, unconditionally proved for
*every* `m` (§5.5 below) — but this alone does not establish the theorem's matching upper
bound at general `m`, nor `n\ge4`, so the file as a whole still does not meet the `solved` bar.)

---

## Approach detail — full write-up of what is proven

### 0. Setup and target

Normalize the stick to `[0,1]`. A choice of `≤n` marks by Liu Bang (LB) followed by `≤n`
marks by Xiang Yu (XY) (all points distinct) creates a finite multiset of piece lengths
summing to 1. By **Lemma G** (`lemmas/greedy-reduction.md`), under optimal alternating
claiming (LB first) LB's total is `L := (\text{sum of odd-ranked pieces, sorted
descending})` and XY's total is `X := (\text{sum of even-ranked pieces})`, with `L+X=1`.
The problem reduces to:

> LB picks a multiset of `k ≤ n+1` pieces `a_1≥…≥a_k ≥0` summing to 1 (via `≤n` cuts); then
> XY, seeing this multiset, applies `≤n` further cuts (splitting any of the `k` pieces
> arbitrarily) to produce a final multiset; LB's payoff is `L` for that final multiset.
> Determine `c(n) := \max_{\text{LB's choice}} \min_{\text{XY's response}} L`.

**Claim:** `c(n) = 2^n/(2^{n+1}-1)`.

Work with `e := L - X = 2L - 1` (since `L+X=1`); write, for a general sorted multiset `M`
with sum `S` (not assuming `S=1`), `e(M) := L(M)-X(M)`, so that if `S=1`, `L = (1+e)/2`.
The target value in `e`-units is
```
e_n := 2c(n) - 1 = 1/(2^{n+1}-1).
```
**Check of the recursion `e_n = e_{n-1}/(2+e_{n-1})`:** substituting `e_{n-1}=1/(2^n-1)`,
```
e_{n-1}/(2+e_{n-1}) = [1/(2^n-1)] / [(2(2^n-1)+1)/(2^n-1)] = 1/(2(2^n-1)+1) = 1/(2^{n+1}-1) = e_n. ✓
```

### 1. Lemma G and Lemma P

Both are proved in full, general form, in the certified lemma files
`lemmas/greedy-reduction.md` and `lemmas/duplicate-pair-invariance.md` (summaries below;
full proofs there).

- **Lemma G.** For a fixed sorted multiset `x_1≥…≥x_K`, under optimal alternating claiming,
  the mover's value is governed by the recursion `v(S) = \mathrm{sum}(S) - \min_{x\in S}
  v(S\setminus\{x\})`; strong induction plus the elementary termwise inequality
  `x_1+x_3+\dots+x_{2t-1} \ge x_2+x_4+\dots+x_{2t}` (true since a sorted sequence has
  `x_{2i-1}\ge x_{2i}`) shows the minimizing removal is always the current maximum, and the
  value is the odd-rank sum. (Full proof in the lemma file.)

- **Lemma P** (as used here, in `e`-form): if a sorted multiset has two entries of equal
  value `x`, deleting any two of them changes `e` by exactly `0`. Proved by splitting `e`'s
  alternating sum into head/block/tail parts: the block (the run of equal value) contributes
  the same amount before and after (since its alternating sum only depends on the run's
  length's parity, and removing 2 elements preserves that parity), and the tail's positions
  all shift by exactly 2 (parity-preserving), so its contribution is literally unchanged
  term-by-term. (Full proof in the lemma file — this version needs no "even multiplicity"
  hypothesis; it works for any two equal entries.)

### 2. The induction skeleton for the upper bound

**Claim (Level `m`, for every `m ≥ 0`).** For any `k ≤ m+1` pieces `a_1≥…≥a_k≥0` summing to
`S`, Xiang Yu (using `≤m` further cuts) can force
```
e(\text{final}) ≤ e_m·S            [form (A)]
```
and moreover, whenever this is achieved via the specific strategies below,
```
e(\text{final}) ≤ a_1/2^m           [form (B), a "max-normalized" version],
```
where `e_0 = 1`, `a_1/2^0 = a_1`.

**Base case `m=0`:** `k≤1` pieces; if `k=0` trivial (`e=0`); if `k=1`, `a_1=S`, XY has 0
cuts, so the final multiset is just `\{a_1\}` and `e = a_1 = S` (single piece: `L=a_1,X=0`
directly from the definition of rank-alternating sums with one term). Both (A)
(`e=S=e_0 S`) and (B) (`e=a_1=a_1/2^0`) hold with equality. ✓

**Handling `k=1` at any level `m≥1`:** if LB used fewer than its full cut budget so that only
one piece is present, XY simply **bisects it fully**: split `a_1` into `(a_1/2,a_1/2)`; this
is itself a full duplicate pair (Lemma P) whose removal leaves the empty multiset, so
`e(\text{final}) = 0 ≤` both `e_m S` and `a_1/2^m` trivially (both targets are `≥0`). This
uses exactly 1 of XY's `m≥1` available cuts (any extra cuts are simply not used — "at most
n" points are allowed, not exactly n). This disposes of `k=1` uniformly at every level, so
from now on we may assume `k≥2` and, by the same trick applied to whichever residual
pieces XY produces, extra unused cuts never cause a problem.

**Inductive step, level `m-1 → m` (`m≥1`):** given `k≤m+1` pieces `a_1≥…≥a_k` (`k≥2`
by the above), split into two cases.

#### Case (i): `a_1 ≥ 2a_2` — CLOSED (full proof)

XY bisects `a_1` into `(a_1/2, a_1/2)`. Since `a_1/2 ≥ a_2 ≥ a_3 ≥ … ≥ a_k`, the sorted
final order is `a_1/2, a_1/2, a_2, a_3, …, a_k` — the two copies of `a_1/2` are contiguous
at ranks `1,2`. By **Lemma P**, `e(\text{final}) = e(\{a_2,…,a_k\})` **exactly** (no
residual cross-term). The residual `\{a_2,…,a_k\}` has `k-1 ≤ m` pieces, so it is an
instance of **Level `m-1`** with largest piece `a_2`; XY has `m-1` cuts left (it used
exactly 1 on the bisection), matching the level-`(m-1)` budget. By the induction
hypothesis, form (B):
```
e(\{a_2,…,a_k\}) ≤ a_2 / 2^{m-1} ≤ (a_1/2)/2^{m-1} = a_1/2^m,
```
(using `a_2 ≤ a_1/2` from the Case (i) hypothesis). This **is** form (B) at level `m`,
and it is fully and rigorously established. **Correction / honest caveat found while
writing this up:** an earlier draft of this paragraph incorrectly asserted that form (A)
(`e ≤ e_m S`) for Case-(i) configurations "follows" automatically from form (B). This is
**false as a generic implication**: form (B) gives `e ≤ a_1/2^m`, but `a_1/2^m` can exceed
`e_m S` (e.g. `m=2`, `(a_1,a_2,a_3)=(0.99,0.005,0.005)`: `a_1/2^2 = 0.2475 > e_2\cdot1 =
1/7\approx0.1429`, even though the *true* `e` there is `0`, far under target — so form (B)'s
own bound is simply too lossy to certify form (A) in that regime by itself). What **does**
appear to work (checked on `200{,}000` random exact-fraction Case-(i) triples at `m=2`,
zero violations) is the **hybrid bound**: apply *both* IH forms to the residual
`\{a_2,\dots,a_k\}` (sum `S-a_1`) and take whichever is smaller,
`e(\text{final}) \le \min\big(e_{m-1}\cdot(S-a_1),\; a_2/2^{m-1}\big)`,
and conjecture (verified numerically, **not yet proven**) that this minimum is always
`\le e_m\cdot S` for Case-(i) configurations. This refinement was not part of the original
outline and is flagged here as an **additional, previously-unnoticed gap**: Case (i)'s
form-(B) conclusion is solid and complete, but promoting it to the top-level target form (A)
(`e\le e_m S`, the actual statement of the theorem) needs this extra hybrid step proved, not
merely form (B) alone. This does not affect Case (i)'s role *inside* the induction (where
only form (B) is invoked recursively, e.g. by Case (ii) below use of form (A)/(B) on
*different* residuals at level `m-1`, which is unaffected by this issue) — it only affects
closing the very top-level statement `e\le e_m\cdot 1` when the top-level configuration
itself falls in Case (i). This is now recorded as an open item (see "Current best") **for
general `m`** — but see immediately below: **it is fully resolved for the concrete case
`m=n=2`.**

**Gap 5 resolved at `n=2` specifically.** At the very top level `m=2` (`S=1`), Case (i)'s
residual `\{a_2,a_3\}` always has **at most 2 elements** (since `k\le3`), so instead of
invoking a generic (and lossy) induction-hypothesis bound on the residual, we may use the
*exact* closed-form n=1 solution from Section 2a directly: `e(\text{final}) =
\mathrm{level1}(a_2,a_3) = \min(a_3,\,a_2-a_3)` **exactly** (no "≤", an equality, since this
is literally XY's optimal play on the 2-element residual, established in Section 2a). So the
top-level Case-(i) question at `n=2` reduces to: maximize `\min(a_3,a_2-a_3)` subject to
`a_1\ge2a_2\ge2a_3\ge0`, `a_1+a_2+a_3=1`. Writing `R:=a_2+a_3=1-a_1`, the *unconstrained*
maximizer of `\mathrm{level1}(a_2,a_3)` over `a_2+a_3=R` is `a_2=2R/3,a_3=R/3` (value `R/3`,
by the general fact in Section 2b), and this is compatible with `a_1\ge2a_2` exactly when
`1-R\ge4R/3\iff R\le3/7`. For `R\le3/7`: max value `R/3\le1/7` (equality at `R=3/7`). For
`R>3/7` (so the unconstrained maximizer `a_2=2R/3` would violate `a_1\ge2a_2`, i.e. `a_2` is
capped at `a_2\le a_1/2=(1-R)/2<2R/3`): on this constrained sub-range, `\mathrm{level1}` (as
a function of `a_2\in[R/2,(1-R)/2]`, still left of its unconstrained peak) is increasing, so
the max is at `a_2=(1-R)/2` (the tightest allowed), giving value `1-2R` (checked: at this
point `2a_2-R=1-2R\le R-a_2=(3R-1)/2 \iff R\ge3/7`, so the min is `1-2R`), which is
*decreasing* in `R`; so its max over `R\in[3/7,1/2)` is at `R=3/7`, again giving `1/7`.
**So the exact maximum of `e` over ALL Case-(i) configurations at `n=2` is exactly `1/7`,
attained uniquely at `R=3/7`, i.e. `(a_1,a_2,a_3)=(4/7,2/7,1/7)`** — the same dyadic point
found everywhere else in this analysis. (Verified independently by an exact-`Fraction` sweep
over Case-(i) triples with denominator up to 1400: observed maximum exactly `1/7`, attained
exactly at `(4/7,2/7,1/7)`, matching the hand derivation precisely.) **This fully closes
form (A) for Case (i) at `n=2` — Case (i)'s top-level gap (item 5) is resolved for `n=2`; it
remains open only for general `m`, where the residual can have more than 2 elements and the
exact 2-element formula is no longer available (a generic IH bound must be used instead, and
gap 5's counterexample shows the naive one is too lossy).**

**Consequence: combined with Section 2c below (Case ii fully closed at `n=2`), the entire
upper-bound direction of the theorem is now fully proved for `n=2` (`c(2)=4/7`).** The
remaining gaps are: generalizing this to all `n` (Case (ii) and Case (i)'s form-(A)
promotion both currently rely on the specific smallness of `k\le3` at `n=2` and are open for
larger `n`), and the entire lower-bound direction (Step 3) at every `n` including `n=2`
(see the honest note at the end of Section 2c).

#### 2d. General-`m` closure of Case (i)'s form-A gap — FULLY PROVED (round 3, this builder)

**This supersedes the n=2-specific "Gap 5 resolved at n=2" paragraph above; that trick is
now obsolete (still correct, but subsumed).**

**Claim.** For every `m≥1`, every Case-(i) configuration (`a_1≥2a_2`, `k≤m+1` pieces, sum `S`)
satisfies form (A): `e(\text{final}) ≤ e_m\cdot S`, where `\text{final}` is the result of XY
bisecting `a_1`.

**Proof.** By induction on `m` (this is the inductive step at level `m`, using the strong
induction hypothesis — both forms (A) and (B) — at level `m-1`; the base case `m=0` was
already established in Section 2 above). We may assume `k≥2` (the `k=1` case is disposed of
uniformly, Section 2 above) and by rescaling assume `S=1` (the whole claim is invariant under
scaling all pieces by a positive constant, since both `e` and `a_1` scale linearly).

After XY bisects `a_1` (Case (i)'s strategy), the residual `\{a_2,\dots,a_k\}` has sum
`1-a_1`, size `k-1\le m`, and largest element `a_2`. By **Lemma P**, `e(\text{final}) =
e(\text{residual})` exactly. Two constraints on `a_2` hold simultaneously: Case (i)'s
hypothesis gives `a_2\le a_1/2`, and since `a_2` is the largest element of a nonnegative
multiset summing to `1-a_1`, also `a_2\le 1-a_1`. So
```
0 \le a_2 \le \min(a_1/2,\ 1-a_1).            (\star)
```
By the strong induction hypothesis at level `m-1` applied to the residual, **both** forms
hold:
```
e(\text{residual}) ≤ e_{m-1}\cdot(1-a_1)      [form A, IH]
e(\text{residual}) ≤ a_2/2^{m-1}              [form B, IH]
```
hence `e(\text{final}) ≤ \min\big(e_{m-1}(1-a_1),\ a_2/2^{m-1}\big) =: \psi(a_1,a_2)`. Since
`\psi` is non-decreasing in `a_2` for fixed `a_1` (only the second argument of the `\min`
depends on `a_2`, and it is increasing in `a_2`), the worst case over `a_2` subject to
`(\star)` is at `a_2 = \min(a_1/2,\,1-a_1)`. Split on which bound binds.

**Sub-case A (`a_1\le2/3`, so `a_1/2\le1-a_1`):** the binding cap is `a_2=a_1/2`, giving
```
e(\text{final}) \le \varphi(a_1) := \min\big(e_{m-1}(1-a_1),\ a_1/2^m\big).
```
`e_{m-1}(1-a_1)` is (weakly) decreasing in `a_1`, `a_1/2^m` is increasing, so `\varphi` is a
`\min` of a decreasing and an increasing function of `a_1`; such a `\min` is maximized exactly
where the two functions cross (**proof of this elementary fact:** let `f` decreasing, `g`
increasing, `a_1^*` the crossing point `f(a_1^*)=g(a_1^*)`. For `a_1\le a_1^*`:
`\min(f,g)(a_1)\le g(a_1)\le g(a_1^*)=\min(f,g)(a_1^*)` since `g` is increasing. For
`a_1>a_1^*`: `\min(f,g)(a_1)\le f(a_1)\le f(a_1^*)=\min(f,g)(a_1^*)` since `f` is decreasing.
Either way `\min(f,g)(a_1)\le\min(f,g)(a_1^*)`, so the crossing point is a global maximizer.)
Solving `e_{m-1}(1-a_1)=a_1/2^m`:
```
a_1^*(e_{m-1}+2^{-m}) = e_{m-1}   \implies   a_1^* = \frac{e_{m-1}}{e_{m-1}+2^{-m}}.
```
**Exact evaluation.** Substituting `e_{m-1}=1/(2^m-1)` (the closed form, already verified in
§0):
```
a_1^* = \frac{1/(2^m-1)}{1/(2^m-1)+1/2^m} = \frac{2^m}{2^m+(2^m-1)} = \frac{2^m}{2^{m+1}-1},
```
and `\varphi(a_1^*) = a_1^*/2^m = 1/(2^{m+1}-1) = e_m`. (Both identities re-verified here by
exact `Fraction` arithmetic for `m=1,\dots,7`; algebra above is exact, not merely checked.)
So the max of `\varphi` over all `a_1` is exactly `e_m`, **provided `a_1^*` itself lies in
Sub-case A's domain `a_1\in[0,2/3]`.** Check: `a_1^*\le2/3 \iff 3\cdot2^m\le2(2^{m+1}-1)
\iff 3\cdot2^m\le4\cdot2^m-2 \iff 2\le2^m \iff m\ge1`, true for every `m\ge1` (with equality
only at `m=1`, where `a_1^*=2/3` sits exactly at the boundary of Sub-case A). So Sub-case A's
supremum is exactly `e_m`, attained at `a_1=a_1^*=2^m/(2^{m+1}-1)` (the dyadic value), for
every `m\ge1`. **Sub-case A closes with `\sup e(\text{final}) = e_m` exactly.**

**Sub-case B (`a_1>2/3`, so `1-a_1<a_1/2`):** the binding cap is `a_2=1-a_1`, giving
`e(\text{final}) \le \min\big(e_{m-1}(1-a_1),\ (1-a_1)/2^{m-1}\big)`. First,
`e_{m-1}\le1/2^{m-1}` for every `m\ge1`: since `e_{m-1}=1/(2^m-1)` and `2^m-1\ge2^{m-1}
\iff 2^{m-1}\ge1 \iff m\ge1` (equality only at `m=1`), so `e_{m-1}\le1/2^{m-1}`. Hence
`e_{m-1}(1-a_1)\le(1-a_1)/2^{m-1}`, so the `\min` above simplifies to `e_{m-1}(1-a_1)`
exactly. Since `a_1>2/3` here, `1-a_1<1/3`, so
```
e(\text{final}) \le e_{m-1}(1-a_1) < e_{m-1}/3.
```
Now `e_{m-1}/3\le e_m` for every `m\ge1`: since `e_m=e_{m-1}/(2+e_{m-1})` (§0's verified
recursion) and `e_{m-1}\le1` for all `m\ge1` (as `e_j` is a decreasing sequence with
`e_0=1`, established already in this file's induction skeleton, or directly: `e_{m-1}=
1/(2^m-1)\le1`), we get `2+e_{m-1}\le3`, so `e_m=e_{m-1}/(2+e_{m-1})\ge e_{m-1}/3`. Combining,
`e(\text{final}) < e_{m-1}/3 \le e_m`. **Sub-case B closes with strict inequality
`e(\text{final})<e_m`, strictly dominated by Sub-case A** — Sub-case B never attains the
maximum and needs no further analysis.

**Conclusion.** Over the whole of Case (i) (`a_1\in[0,1]`, both sub-cases), `e(\text{final})
\le e_m` always, with the value `e_m` actually approached (Sub-case A, at `a_1=a_1^*=
2^m/(2^{m+1}-1)`). This proves form (A) for Case (i) at **every** level `m\ge1`, completing
the inductive step (together with form (B), already established in Section 2 above, which
this proof did not need to re-derive). `∎` (This closes Case (i) completely and supersedes
the old n=2-only "exact 2-element residual" trick, which is no longer needed anywhere in this
file — the argument above required only the IH's two forms at level `m-1`, no extra
machinery, and holds verbatim for every `m`, including `m=2` where it reproduces the earlier
`1/7` finding as a special case: a direct check confirms `a_1^*=4/7` at `m=2`, matching
Section 2's "Gap 5" computation exactly.)

**Note on an initially-overlooked subtlety, found and fixed while writing this proof up.**
An earlier round's skeleton implicitly assumed the adversarial choice of `a_2` is always
`a_1/2` (Sub-case A only), without checking the second constraint `a_2\le1-a_1` coming from
`a_2` being the largest element of a residual summing to `1-a_1`. This omission is harmless
for `m=1,\dots,6` in the numerical spot-checks the outline ran (which apparently sampled
`a_1\le2/3` predominantly, or landed in Sub-case A's basin), but the omission was a genuine
logical gap in the previous skeleton: without Sub-case B's separate argument, the "closure"
was not actually complete. Sub-case B is now proved above (with strict inequality, so it
never threatened the bound, but this needed to be shown, not assumed).

#### Case (ii): `a_1 < 2a_2` — OPEN in general; n=2 (m=2) instance substantially advanced

**(round 5 pointer, no re-derivation here — avoids duplicating a skeleton across two
files.)** The general-`m` closure of Case (ii) is being pursued in the sibling approach
`potential-weighting-upper-bound`, whose round-5 §6 develops a new "chain-prefix + exact
static one-shot allocation" mechanism (a restricted, non-adaptive family within the certified
D/M operation space — repeatedly `M`-merge the running top result against the next original
element `c` times, then solve the residual's optimal allocation *exactly* as a static,
non-cascading combinatorial problem via the already-certified Fact 3 block-extraction
identity). It is stress-tested there against 650+ exact-`Fraction` trials plus all three known
hard counterexamples on file (Rule 1's, Rule 2's, and a new one requiring genuine cascading),
zero failures, no closed-form proof yet. **This file should import that result once proved**
(the same way it already imports Lemma D/M rather than re-deriving it) rather than restate the
mechanism here — see that file for the full skeleton, numerical evidence, and open gap.

This is the genuinely hard case. We do **not** attempt the general-`m` algebra (per the
explicit round-1 hang warning); instead we fully work out the smallest non-trivial
instance, **level `m=1` (n=1)**, completely, and then attack **level `m=2` (n=2)**.

##### 2a. Level `m=1` (n=1) — FULLY SOLVED

Here `k≤2`. The `k=1` sub-case is handled above (`e=0`). For `k=2`: pieces `p≥q≥0`,
`p+q=S`, XY has exactly 1 cut. By the **vertex lemma** (Section 3 below, proved in general
but specialized here), XY's only candidates for its single cut are: don't cut (`e=p-q`,
the raw 2-piece value), bisect `p` (creating a duplicate pair `\{p/2,p/2\}`; by Lemma P this
leaves residual `\{q\}`, so `e=q` directly, by the single-piece formula, *provided* `p/2\ge q`
so the pair sits together in sorted order — but Lemma P's general proof does not actually
need this: even if `p/2 < q`, the two copies of `p/2` are still a contiguous equal-valued run
wherever they land, since sortedness forces it; so `e=q` **unconditionally** after bisecting
`p`), or match `p` to `q` (split `p` into `(q,p-q)`, creating pair `\{q,q\}`; residual
`\{p-q\}`, so `e=p-q`, identical to not cutting). So the candidate set collapses to exactly
`\{p-q,\ q\}`, and XY's best is
```
e_{XY-best}(p,q) = \min(q,\ p-q).
```
**Maximizing LB's choice:** for fixed `S=p+q`, as `q` ranges over `[0,S/2]`,
`\min(q,S-2q)` increases (slope `+1`) for `q<S/3` and decreases (slope `-2`) for `q>S/3`,
so it is maximized at `q=S/3`, value `S/3`. Hence
```
\max_{p\ge q\ge0,\,p+q=S} \min_{\text{XY's 1 cut}} e = S/3 = e_1\cdot S,
```
attained uniquely at `(p,q)=(2S/3,S/3)` — exactly the dyadic point for `n=1`. **This is a
complete, elementary, fully rigorous solution of the whole theorem at `n=1`** (both
directions: the bound above is XY's guarantee for every LB opening, and `(2/3,1/3)` is
LB's matching construction, since at that exact point the guaranteed value is `S/3` and no
XY response can do better, by the identity just derived with `q=S/3` giving
`\min(S/3,S/3)=S/3` — this needs the converse "no XY response beats this", which is
exactly what `e_{XY-best}(p,q)=\min(q,p-q)` says: it *is* the true optimal value against
this specific `(p,q)`, since we exhaustively considered all of XY's candidate cuts via the
vertex lemma, not just an ad hoc pair.)

##### 2b. Level `m=2` (n=2), Case (ii): substantial partial progress

Here `k≤3`; `k≤2` is subsumed into level-1-style reasoning composed with an extra unused
cut (if `k=2`, apply the level-1-optimal single cut, then apply a *second* cut fully
bisecting whatever single residual piece remains, driving `e` to exactly `0` — using both
of XY's `m=2` cuts profitably; since `0 ≤ e_2 S` this is immediate). So the content is
`k=3`: `a_1≥a_2≥a_3≥0`, `S=a_1+a_2+a_3=1` WLOG (rescale), Case (ii): `a_1<2a_2`.

**Candidate strategies (via the vertex lemma, Section 3):**
- **(c)** Bisect `a_1` (1 cut): by Lemma P, residual `= \{a_2,a_3\}` **exactly** regardless
  of where `a_1/2` sits in sorted order (general form of Lemma P used here). Apply the
  level-1-optimal single cut (1 more cut) to this residual: total
  `e = \mathrm{level1}(a_2,a_3) := \min(a_3,\,a_2-a_3)`.
- **(a)** Match `a_1` to `a_2` (split `a_1` into `(a_2,a_1-a_2)`, 1 cut): since
  `a_1<2a_2` (Case ii), `a_1-a_2<a_2`, and the pair `\{a_2,a_2\}` is contiguous in sorted
  order regardless of where the leftover `a_1-a_2` and `a_3` land (Lemma P, general form).
  Residual `=\{a_1-a_2,a_3\}`; apply the level-1-optimal cut (1 more cut): total
  `e = \mathrm{level1}(a_1-a_2,\,a_3)`.

XY plays whichever of (c),(a) is better, so **XY achieves**
```
e ≤ F(a_1,a_2,a_3) := \min\big(\mathrm{level1}(a_2,a_3),\ \mathrm{level1}(a_1-a_2,a_3)\big).
```
(This is a *sufficient* strategy for XY, not asserted to be its true optimum — consistent
with the outline-reviewer's finding that XY's optimal response can involve richer moves
(e.g. simultaneous double-matching); we do not need optimality, only that `F` is achievable
and `F\le 1/7` — see CLAUDE.md / outline-reviewer guidance.)

**Goal:** `F(a_1,a_2,a_3) ≤ 1/7` for every Case-(ii) triple. Write `u:=a_1-a_2 \in[0,a_2)`
(Case ii `\iff u<a_2`); the constraint `a_1+a_2+a_3=1` becomes `2a_2+u+a_3=1`.

**General fact used:** `\mathrm{level1}(x,y) := \min(\min(x,y),|x-y|) \le (x+y)/3` for all
`x,y\ge0`, with equality iff `\{x,y\}=\{2t,t\}` for some `t\ge0`. *(Proof: WLOG `x\ge y`, so
`\mathrm{level1}=\min(y,x-y)`; as a function of `y` with `x+y=:s` fixed, this equals
`\min(y,\,s-2y)`, which is `\le s/3` since the two branches cross exactly at `y=s/3` where
both equal `s/3`, and away from that point the smaller branch is `<s/3`. This is precisely
the level-1 computation of Section 2a, re-used as a general inequality.)*

**Exact solution of the extremal sign-regime.** Split on the sign of `a_2-2a_3` and of
`u` vs. `a_3,2a_3` (these are exactly the breakpoints of `\mathrm{level1}`'s own
definition). Consider the regime
```
a_2 ≥ 2a_3    (so \mathrm{level1}(a_2,a_3) = a_3),
a_3 < u ≤ 2a_3   (so \mathrm{level1}(u,a_3) = u-a_3).
```
In this regime `F = \min(a_3,\,u-a_3) = u-a_3` (since `u\le 2a_3 \Rightarrow u-a_3\le a_3`).
We maximize `u-a_3` subject to: `2a_2+u+a_3=1`, `a_2\ge2a_3`, `a_3<u\le2a_3`, `u<a_2` (Case
ii). For fixed `a_3`, `u-a_3` is maximized by taking `u` as large as the regime allows,
`u=2a_3` (the upper edge of this regime); there `F=u-a_3=a_3`. Substituting `u=2a_3` into
the sum constraint: `2a_2+2a_3+a_3=1 \Rightarrow a_2=(1-3a_3)/2`. The constraint
`a_2\ge2a_3` becomes `(1-3a_3)/2\ge2a_3 \iff 1\ge7a_3 \iff a_3\le1/7`, and Case (ii)'s
`u<a_2` becomes `2a_3<(1-3a_3)/2 \iff 4a_3<1-3a_3 \iff a_3<1/7` **(strict)**. So within this
regime, `F=a_3` with `a_3` ranging over `[0,\,1/7)` (strict upper end), i.e.
```
\sup F = 1/7,\ \text{NOT attained for any point strictly inside Case (ii) in this regime.}
```
At the excluded limit `a_3\to1/7^-`: `a_2\to2/7`, `u\to2/7`, so `a_1=a_2+u\to4/7`, giving
`a_1\to2a_2` exactly — this limiting point is the **Case-(i) boundary** (`a_1=2a_2`),
already covered (with equality `e=1/7`) by Case (i)'s own proof. So on this regime, Case
(ii) proper (`a_1<2a_2` strictly) gives `F<1/7` strictly, consistent with the target, and
the numerically-observed worst points (found by exact-fraction search in Section 2c below)
concentrate exactly in this regime, approaching this boundary. **This regime is fully,
rigorously closed.**

**The other sub-case of `a_2 ≥ 2a_3`, i.e. `u > 2a_3`.** Here `\mathrm{level1}(u,a_3)` is
past its own peak and has *saturated*: `\mathrm{level1}(u,a_3)=a_3` (constant) for all
`u\ge2a_3`. So `F=\min(a_3,a_3)=a_3` throughout this sub-case. The same substitution method
as above (`u=1-2a_2-a_3` from the sum constraint; require `u>2a_3`, `u<a_2` (Case ii),
`a_2\ge2a_3`) shows the region is nonempty exactly when `a_3<1/7`, and gives no constraint
forcing `a_3` away from `1/7^-` — so again `\sup F = a_3 \to 1/7^-`, **not attained**, at the
same limiting boundary point `(4/7,2/7,1/7)` (Case-(i) boundary, excluded from strict Case
(ii)). **This sub-case is also fully closed.**

**The remaining sub-case of `a_2 ≥ 2a_3`, i.e. `u ≤ a_3`.** Here `A=a_3` (as always in this
main regime) and `B=\min(u,a_3-u)`; since `\min(u,a_3-u)\le a_3/2 < a_3`, `F=\min(A,B)=B=
\min(u,a_3-u)` — the `a_3`-cap from `A` never actually binds here. Writing `a_2=(1-u-a_3)/2`
(from the sum constraint) and imposing `a_2\ge2a_3` (`\iff u\le1-5a_3`), `u\le a_3` (regime),
and `u<a_2` (Case ii, `\iff u<(1-a_3)/3`), the admissible `u`-interval for fixed `a_3` is
`[0,\ \min(a_3,\,1-5a_3,\,(1-a_3)/3)]`. The tent function `\min(u,a_3-u)` peaks at `u=a_3/2`;
this peak is admissible exactly when `a_3/2\le1-5a_3` (`\iff a_3\le2/11`) — the other cap
`(1-a_3)/3` is never tighter here (`a_3/2\le(1-a_3)/3\iff a_3\le2/5`, a weaker requirement).
So: for `a_3\le2/11`, the best is `u=a_3/2`, giving `F=a_3/2\le1/11`; for `a_3>2/11`, the
admissible interval is capped below the peak by `u\le1-5a_3` (which is then `<a_3/2`), so
`\min(u,a_3-u)=u` throughout (still on the ascending branch) and is maximized at the right
endpoint `u=1-5a_3`, giving `F=1-5a_3`, which is *decreasing* in `a_3` — so its largest value
on `a_3>2/11` is approached as `a_3\to(2/11)^+`, again giving `1/11`. **Hence `\sup F = 1/11`
over this whole sub-case**, attained exactly at `(a_1,a_2,a_3)=(5/11,4/11,2/11)` (check:
sum `=11/11=1`; `a_1<2a_2`: `5/11<8/11` ✓, Case ii holds; direct substitution confirms
`F=1/11` there). Since `1/11 < 1/7`, **this sub-case is fully closed with strict inequality
throughout — it is not even close to binding.**

**Summary for `a_2 ≥ 2a_3` (regimes I and II combined): FULLY CLOSED.** Both sub-cases
(`u\le a_3` and `u>a_3`, the latter itself split at `u=2a_3`) have been solved exactly by
hand: `u\le a_3` gives `F\le1/11<1/7` strictly; `a_3<u\le2a_3` and `u>2a_3` both give
`\sup F = 1/7`, approached only as Case (ii) degenerates into the Case-(i) boundary, never
attained inside strict Case (ii).

##### 2c. The complementary regime `a_2 < 2a_3` — NOW ALSO CLOSED (completing n=2, Case ii)

Here `\mathrm{level1}(a_2,a_3) = a_2-a_3 =: g_1` (as computed earlier, `A=a_2-a_3` when
`a_2<2a_3`). Write, as before, `a_2=(1-u-a_3)/2` from the sum constraint, so
`g_1(u) = (1-u-3a_3)/2` — **linearly decreasing in `u`**.

**Sub-case `u ≤ a_3`.** Here `B=\mathrm{level1}(u,a_3)=\min(u,a_3-u)=:g_2(u)`, the usual
tent peaking at `u=a_3/2`. The admissible `u`-range (from `a_2<2a_3\iff u>1-5a_3`,
`a_2\ge a_3\iff u\le1-3a_3`, this sub-case's `u\le a_3`, and Case ii's `u<(1-a_3)/3`) is
`u \in \big(\max(0,1-5a_3),\ \min(a_3,\,(1-a_3)/3)\big)` (the cap `1-3a_3` is never tighter
than `a_3` here since `a_3\le1-3a_3\iff a_3\le1/4`, which holds throughout — checked below).
A short computation (comparing `g_1` and `g_2` at the tent peak `u=a_3/2`, where
`g_2=a_3/2` and `g_1(a_3/2)=(2-7a_3)/4`) shows `g_2 < g_1` at the peak `\iff a_3<2/9`, and
this comparison governs which function is larger throughout, giving three sub-ranges of
`a_3`:
- `a_3 \in [1/6,\,2/11]`: the peak `u=a_3/2` is *not* admissible (falls left of the range's
  lower bound `1-5a_3`), so `F=g_2` is evaluated at the range's left endpoint `u=1-5a_3`,
  giving `F = a_3-(1-5a_3) = 6a_3-1`, **increasing** in `a_3`; maximal at `a_3=2/11`, value
  `1/11`.
- `a_3\in[2/11,\,2/9)`: the peak is admissible and `g_2\le g_1` there, so `F=g_2=a_3/2`,
  **increasing**; as `a_3\to(2/9)^-`, `F\to1/9`.
- `a_3\ge2/9`: now `g_1\le g_2` at the tent peak, so the true maximum of `\min(g_1,g_2)` over
  `u` occurs exactly where the *rising* branch of `g_2` (`g_2=u` for `u<a_3/2`) crosses `g_1`:
  solving `u=(1-u-3a_3)/2` gives `u=1/3-a_3`, and `F=1/3-a_3` there — **decreasing** in `a_3`;
  as `a_3\to(2/9)^+`, `F\to1/3-2/9=1/9` (matches the previous branch, continuous).
  Larger `a_3` (checked up to the regime's own upper limit `a_3\le1/4`, beyond which the
  range further shrinks) only decreases `F` further.

So `\sup F = 1/9` over this whole sub-case, **attained exactly** at
`a_3=2/9,\,u=1/9,\,a_2=1/3,\,a_1=4/9` — verified directly: `A=\mathrm{level1}(1/3,2/9)=
\min(2/9,1/9)=1/9`, `B=\mathrm{level1}(1/9,2/9)=\min(1/9,1/9)=1/9`, `F=1/9`. Check validity:
`4/9+3/9+2/9=1` ✓, `4/9\ge3/9\ge2/9` ✓, `a_1<2a_2`: `4/9<6/9` ✓ (genuinely inside Case ii,
not a boundary point). Since `1/9 < 1/7`, **this sub-case is fully closed, with strict
inequality throughout, comfortably slack** (confirmed by an exact-fraction computer check at
this specific point, matching the hand derivation exactly).

**Sub-case `u > a_3`.** Here `B=\mathrm{level1}(u,a_3)=\min(a_3,u-a_3)` (rising from `0` at
`u=a_3` to `a_3` at `u=2a_3`, then constant `=a_3`). Tracking the admissible `u`-range
(`a_2<2a_3\iff u>1-5a_3`, `a_2\ge a_3\iff u\le1-3a_3`, `u>a_3`, Case ii `u<(1-a_3)/3`) shows,
by comparing `1-5a_3` to `a_3` and `1-3a_3`/`(1-a_3)/3` to each other, that **this sub-case is
non-empty only for `a_3\in(1/7,\,1/4)`** (for `a_3\le1/7` the lower cap `1-5a_3` already
exceeds the Case-ii upper cap `(1-a_3)/3`, an empty interval; similarly empty for
`a_3\ge1/4`). Within `a_3\in(1/7,1/4)`, the rising branch `B=u-a_3` crosses the decreasing
`g_1(u)=(1-u-3a_3)/2` at `u^* = (1-a_3)/3` — which is *exactly* Case ii's own upper cap
(`u<a_2\iff u<(1-a_3)/3`)! (Direct check: at `u=u^*`, `a_2=(1-u^*-a_3)/2 = (1-a_3)/3 = u^*`,
i.e. `a_1=a_2+u^*=2u^*=2a_2` exactly — the crossing point is precisely the Case-(i)/(ii)
boundary, hence **excluded** from strict Case ii.) So within the open interval
`u\in(a_3,u^*)`, `B=u-a_3 < g_1` throughout (the crossing is only reached in the limit), so
`F=B=u-a_3`, strictly **increasing**, with
```
\sup_{u\to u^{*-}} F = u^*-a_3 = (1-a_3)/3 - a_3 = (1-4a_3)/3,
```
**not attained** (needs the excluded boundary `u=u^*`). This supremum is **decreasing** in
`a_3`, so its largest value over `a_3\in(1/7,1/4)` is approached as `a_3\to(1/7)^+`, giving
```
\sup F \to (1-4/7)/3 = (3/7)/3 = 1/7,
```
**also not attained** (needs `a_3>1/7` strict as well). The joint limit `a_3\to1/7^+,
u\to u^{*-}` sends `(a_1,a_2,a_3) \to (4/7,\,2/7,\,1/7)` — again exactly the master
Case-(i)/(ii) boundary point. **This sub-case is fully closed**: `F<1/7` strictly at every
point actually inside Case ii, with `1/7` approached only in this boundary limit (verified
independently by exact-fraction spot checks approaching the limit from inside, matching the
predicted formula `(1-4a_3)/3` to within the perturbation size used).

**Conclusion for n=2, Case (ii): FULLY CLOSED.** All four sign sub-regimes of
`F=\min(\mathrm{level1}(a_2,a_3),\,\mathrm{level1}(a_1-a_2,a_3))` have now been solved
exactly by hand:

| regime | sub-case | `\sup F` | attained inside Case ii? |
|---|---|---|---|
| `a_2\ge2a_3` | `u\le a_3` | `1/11` | yes, `(5/11,4/11,2/11)` |
| `a_2\ge2a_3` | `u>a_3` | `1/7` | no (Case-i boundary only) |
| `a_2<2a_3` | `u\le a_3` | `1/9` | yes, `(4/9,3/9,2/9)` |
| `a_2<2a_3` | `u>a_3` | `1/7` | no (Case-i boundary only) |

In every regime `F\le1/7`, so **for every Case-(ii) triple `(a_1,a_2,a_3)` at `n=2`, XY's
sufficient strategy achieves `e\le1/7=e_2`**, with equality never occurring strictly inside
Case (ii) (only in the shared limit with Case (i)'s own boundary, where Case (i)'s proof
already gives equality `e=1/7` exactly, via the dyadic point `(4/7,2/7,1/7)`). Combined with
Case (i)'s exact closure at `n=2` (see the "Gap 5 resolved at `n=2` specifically" paragraph
above, proved by the same style of argument using the exact 2-element residual formula),
**every LB opening at `n=2` (`k\le3` pieces, both Case (i) and Case (ii)) now has a proven
XY response achieving `e\le1/7`, with equality possible only at the unique dyadic point
`(4/7,2/7,1/7)`. This is a complete, gap-free proof of the entire upper-bound direction of
the theorem for `n=2` (`c(2)\le4/7`).** What remains open (see "Current best"): the matching
lower-bound direction at `n=2` (showing the dyadic construction `(4/7,2/7,1/7)` actually
*resists* every one of XY's responses, not just that XY cannot force it lower than `1/7` via
*this specific analysis* — this is the converse direction and has only been spot-checked
numerically, not proved, see the note at the end of this subsection) and the generalization
of both directions to all `n\ge3`.

**Lower-bound direction at `n=2`: preliminary exploration only, not a proof.** For the
lower-bound direction we need the converse: that against the *specific* dyadic input
`(4/7,2/7,1/7)`, **no** response of XY (using its own `\le2` cuts) can push `e` below `1/7`.
Because the input is now fixed (not universally quantified over LB's choice), this is in
principle a bounded computation, and a finite enumeration of vertex-type candidate responses
(bisections, single matches, and "double-match" 3-way splits of one piece against the other
two, plus compositions of two such moves) found no candidate beating `e=1/7` (best found was
exactly `1/7`, via matching the two smaller pieces together). **This is only checked against
a hand-picked finite subset of vertex candidates, not the full, rigorously-enumerated vertex
set that the vertex lemma (Section 3) guarantees is sufficient** (a complete proof would need
to enumerate every joint vertex of the piecewise-linear structure for *two simultaneous cuts
on the same piece*, which was not carried out exhaustively this round) — so this is offered
as supporting evidence only, and the lower-bound direction at `n=2` (and hence the theorem's
full "solved" status even at `n=2`) remains **open**.

### 3. The vertex lemma (piecewise linearity of a single cut)

**Statement.** Fix a sorted multiset of pieces containing a piece `a_i` and consider
splitting `a_i` into `(t,\,a_i-t)` for `t\in(0,a_i)`, leaving all other pieces fixed. Then
`e`, as a function of `t`, is **piecewise linear**, with breakpoints only where `t` or
`a_i-t` equals one of the other (fixed) piece-values, or where `t=a_i-t` (i.e. `t=a_i/2`,
self-bisection).

**Proof.** As `t` varies over an interval not containing any breakpoint, the *sorted order*
(the relative rank of every piece, including the two new pieces `t` and `a_i-t`, among
the whole multiset) is constant — because the only way two elements can swap relative order
as `t` varies continuously is for their values to cross, and the only elements whose values
change with `t` are the two new pieces themselves (values `t` and `a_i-t`, both linear in
`t`); a crossing between these two new pieces happens only at `t=a_i/2`, and a crossing
between a new piece and some fixed other value `a_j` happens only where `t=a_j` or
`a_i-t=a_j`. Away from all such points, every piece's rank (hence its sign `(-1)^{\text{rank}
+1}` in the definition of `e`) is locally constant, so
`e = (\text{constant}) + \sigma_1\cdot t + \sigma_2\cdot(a_i-t)` for fixed signs
`\sigma_1,\sigma_2\in\{\pm1\}` (the signs of the two new pieces' ranks) is affine — i.e.
linear — in `t` on that sub-interval. There are finitely many other piece-values (at most
`k-1`), so finitely many breakpoints, proving piecewise linearity with the stated
breakpoints. ∎

**Consequence.** A continuous piecewise-linear function on a closed interval attains its
minimum at an endpoint or at a breakpoint (each linear piece's extrema are at its own
endpoints). So the minimizing `t` for a single cut on a single piece is always one of:
`t\to0` (equivalent to "don't use this cut" — the game only requires "at most `n`" points),
`t=a_i/2` (bisect), or `t=a_j` / `a_i-t=a_j` for some other existing piece `a_j` (match).
This converts the ad hoc "try bisect / match" heuristic into a **proved** reduction to a
finite candidate list for a single cut; when several cuts are used, the same locally-affine
argument applies jointly (each additional cut contributes another pair of linear terms with
locally-constant sign), so the joint minimum over several cuts is at a "vertex" where
several such single-cut conditions hold simultaneously — this is consistent with, and gives
a rigorous grounding for, the outline-reviewer's empirical finding that XY's richer response
family (e.g. one cut simultaneously matching two other pieces) also arises as such vertices.
We do not carry out the full joint-vertex enumeration for `k>3` in this round (that is the
harder general-n direction, left open), but for `k=3` (n=2) the two-single-cut candidate
list used in Section 2b is exactly the enumeration of the relevant vertices for the specific
sufficient strategies chosen (bisect-then-recurse, match-then-recurse); a full proof that
*no other vertex ever needs to be invoked* to reach `\le 1/7` would require checking the
remaining "double-cut-on-one-piece" vertices (e.g. splitting `a_1` into three parts at once)
are never *strictly necessary* — the numerical evidence (Section 2c) suggests they are not
(candidates (a),(c) alone already suffice), but this has not been proved as a clean
"these two dominate all other vertices" statement, only checked numerically. This is folded
into the open gap recorded above.

### 4. Cases and scope covered vs. not covered this round

Covered, rigorously, and now **complete for `n=2`**: Lemma G (general), Lemma P (general),
the induction skeleton's bookkeeping (cut budgets, `k=1` degenerate handling), Case (i) in
full (both form (B) for all `n`, and the exact top-level closure specifically at `n=2`),
Case (ii) in full at `n=2` (all four sign sub-regimes closed exactly by hand), and the `n=1`
instance of the theorem (both directions, since at `n=1` the lower bound is trivial by the
same exact 2-element formula — LB's choice `(2/3,1/3)` combined with the proven formula
`e_{XY-best}(p,q)=\min(q,p-q)` immediately gives both the upper bound for all openings *and*
the matching lower bound for this specific opening, since it's the same identity read both
ways). So `n=1` is fully solved (both directions) and `n=2`'s **upper bound** is fully
solved.

**(Round-3 update — supersedes the paragraph above.)** The lower-bound direction, for
**every** `m` (not just `n=2`), is now substantially advanced by §5 below: Branch A (XY never
cuts `a_1`) and Branch B's single-cut-on-`a_1` sub-case (both bisection and every match
alternative) are fully, rigorously proved via strong induction on `m` plus two general
elementary facts. What remains open, for every `m` including `m=2`, is narrowly the
"`\ge2` cuts land inside the currently-dominant piece" sub-case (§5.2) — strong numerical
support (`m=2,3,4`), no proof yet, and a documented negative result ruling out the most
natural general fix. Separately open: Case (ii) of the *upper* bound at general `m\ge3`
(Case (i) is now fully closed for every `m` via §2d) — tracked in the sibling approach
`potential-weighting-upper-bound`.

### 5. Lower-bound direction via dominance/superincreasing lock — Branch A closed, Branch B
substantially advanced (round 3, this builder)

**Target.** For every `m`, XY (with `≤m` further cuts) **cannot** force `e` below `e_m`
against the specific input `D_m := (2^m,2^{m-1},\dots,2,1)/(2^{m+1}-1)` (the dyadic
construction, sum normalized to 1). Together with the upper bound (Section 2, now complete
for Case (i) at every `m` via §2d, and for Case (ii) at `n=2`; Case (ii) at general `m` still
open, tracked in `potential-weighting-upper-bound`), this would give `c(m) =
2^m/(2^{m+1}-1)` exactly.

We prove this by strong induction on `m`. Base case `m=0`: a single piece `a_1=1`, no cuts
possible, `e=1=e_0`. ✓. Inductive step (`m\ge1`, IH: the claim holds for `D_{m-1}` at level
`m-1`): fix any strategy of XY using `\le m` cuts against `D_m`. Split into two exhaustive,
disjoint cases: **Branch A** (none of XY's cuts falls inside the piece `a_1`) and **Branch B**
(at least one cut falls inside `a_1`).

#### Two general elementary facts (used in both branches)

**Fact 1 (`e(M)\ge0` for any sorted multiset).** For any `x_1\ge x_2\ge\dots\ge x_K\ge0`,
`e(M):=x_1-x_2+x_3-\dots\ge0`. **Proof.** This is exactly the inequality
`x_1+x_3+\dots+x_{2t-1}\ge x_2+x_4+\dots+x_{2t}` proved inside **Lemma G**'s proof
(`lemmas/greedy-reduction.md`, the termwise bound `x_{2i-1}\ge x_{2i}` summed over
`i=1,\dots,t=\lfloor K/2\rfloor`), applied with `t=\lfloor K/2\rfloor`; if `K` is odd there is
one further unpaired term `x_K\ge0` added to the `+` side, which only increases the sum. So
`e(M)\ge0` in every case. ∎ (This fact is implicitly already used, but not previously named,
in Lemma G's own proof; we name and re-use it here as a standalone corollary.)

**Fact 2 (`e(M)\le\max(M)`, "dominant extraction").** For any sorted multiset
`M=(x_1\ge\dots\ge x_K)` with `K\ge1`, `e(M) = x_1 - e(\text{rest})` where
`\text{rest}:=(x_2,\dots,x_K)` (itself sorted descending), and consequently, by Fact 1
applied to `\text{rest}`, `e(M)\le x_1=\max(M)`. **Proof.** Direct from the definition:
`e(M)=x_1-x_2+x_3-x_4+\dots = x_1-(x_2-x_3+x_4-\dots)=x_1-e(\text{rest})`. Combined with
`e(\text{rest})\ge0` (Fact 1), `e(M)\le x_1`. ∎

Both facts are general (no reference to cutting, budgets, or the dyadic structure); they will
be applied to various sub-multisets that arise from XY's cuts.

#### Branch A: XY's cuts never touch `a_1` — FULLY CLOSED

**Dominance.** `a_1 = 2^m/(2^{m+1}-1)` and `\sum_{i\ge2}a_i = (2^m-1)/(2^{m+1}-1)`, and
`2^m > 2^m-1`, so `a_1 > \sum_{i\ge2}a_i`, i.e. `a_1` strictly exceeds the sum of *all* other
pieces of `D_m`. Since every piece appearing in the final multiset other than `a_1` itself is
either an original piece `a_i` (`i\ge2`) or a fragment obtained by cutting some `a_i`
(`i\ge2`) — cuts only ever produce values strictly smaller than their parent piece — every
such piece is `\le a_2 < a_1`. Hence, with `a_1` uncut, `a_1` is (uniquely) the largest piece
of the final multiset, i.e. it sits at rank 1.

**Reduction via Fact 2.** Write `\text{final} = \{a_1\}\cup R'`, where `R'` is `R:=D_m
\setminus\{a_1\}` after XY's (up to `m`) cuts, none of which touch `a_1`. Since `a_1`
dominates every element of `R'` (just shown), the sorted order of `\text{final}` is `a_1`
followed by `R'` sorted descending, so Fact 2 applies directly with `x_1=a_1`,
`\text{rest}=R'`:
```
e(\text{final}) = a_1 - e(R').
```
Now bound `e(R')` from above using Fact 2 again, this time applied to `R'` itself: `e(R')\le
\max(R')`. Since `R'` is obtained from `R=\{a_2,\dots,a_{m+1}\}` purely by cutting (splitting
existing pieces into smaller ones, never merging), `\max(R')\le\max(R)=a_2` (no cut can ever
produce a piece larger than the piece it split, and no cut can be applied to `a_1` in this
branch by assumption, so nothing in `R'` can exceed `a_2`, the largest original element of
`R`). Hence `e(R')\le a_2`, and:
```
e(\text{final}) = a_1 - e(R') \ge a_1 - a_2 = \frac{2^m}{2^{m+1}-1}-\frac{2^{m-1}}{2^{m+1}-1}
= \frac{2^{m-1}}{2^{m+1}-1}.
```
Since `2^{m-1}\ge1` for every `m\ge1` (equality only at `m=1`),
```
e(\text{final}) \ge \frac{2^{m-1}}{2^{m+1}-1} \ge \frac{1}{2^{m+1}-1} = e_m,
```
**with equality possible only at `m=1`.** This proves Branch A **unconditionally**, for
**every** `m\ge1` and **every** way XY distributes its `\le m` cuts among `R`'s `m` pieces
(any number of cuts on any subset of them, in any pattern) — the argument never needed to
know how many cuts were used or where within `R` they fell, only that none touched `a_1`. `∎`
(Branch A closed.)

#### Branch B: at least one of XY's cuts falls inside `a_1`

By the vertex lemma (Section 3), each individual cut, viewed as the last cut applied (with
all others held fixed), sits at a piecewise-linear breakpoint: either it bisects the piece it
cuts, or it makes the piece it cuts equal to some other currently-existing value in the
multiset. We analyze this in two layers: first, **exactly one cut on `a_1`** (fully resolved
below, both for bisection and for every possible match); second, **two or more cuts landing
inside `a_1`** (only numerically supported so far — the genuine remaining gap, stated
honestly at the end of this section).

##### 5.1 Exactly one cut on `a_1` — FULLY CLOSED

Suppose XY's cut on `a_1` splits it into `(t,a_1-t)`, and this is the *only* cut applied to
(fragments of) `a_1` — the remaining `\le m-1` cuts, however many are used, are applied only
to `R=\{a_2,\dots,a_{m+1}\}`. By the vertex lemma, the optimal such `t` is at a breakpoint:
bisection (`t=a_1/2`) or a match to some `a_i` (`t=a_i` for some `i\ge2`, WLOG `t\le a_1-t`,
i.e. `i` such that `a_i\le a_1/2`, true for all `i\ge2` since `D_m` is dyadic, `a_2=a_1/2`).

**Case B1: bisection (`t=a_1/2`, equivalently "match to `a_2`", since `a_1=2a_2` exactly for
the dyadic input — these coincide).** XY splits `a_1` into `(a_1/2,a_1/2)=(a_2,a_2)`. Combined
with `R` (which already contains one copy of `a_2`), the full multiset before removing
duplicates is `R\cup\{a_2,a_2\}`, which has **two extra** copies of `a_2` layered onto `R`'s
own one copy — i.e. three copies of `a_2` total (`R`'s original plus the two new halves).
Two of these three form a duplicate pair; **Lemma P** removes any two equal-valued entries
with no change to `e`, so
```
e(\text{final}) = e\big(R\setminus\{a_2\}\ \cup\ \{a_2\}\big) = e(R).
```
(Concretely: remove one of the three copies of `a_2` — the computation of `e` is unaffected
— leaving exactly `R=\{a_2,a_3,\dots,a_{m+1}\}` itself, unaltered.) Since `R`, rescaled by
`2^{m+1}-1`, equals `(2^{m-1},\dots,2,1)`, i.e. `R` (with its own sum `(2^m-1)/(2^{m+1}-1)`)
is **exactly the dyadic construction `D_{m-1}` at level `m-1`, scaled** — a direct check:
`D_{m-1}=(2^{m-1},\dots,1)/(2^m-1)`, and `R/\text{sum}(R) = (2^{m-1},\dots,1)/(2^m-1)`,
identical. XY has `\le m-1` cuts remaining for `R` (having used exactly 1 on `a_1`), which is
*exactly* the level-`(m-1)` problem with the correct cut budget. By the **strong induction
hypothesis** (the level-`(m-1)` instance of this very claim, applied to `D_{m-1}`, valid since
`R` is exactly a scaled copy of `D_{m-1}`):
```
e(R\text{-final}) \ge e_{m-1}\cdot\text{sum}(R) = e_{m-1}\cdot\frac{2^m-1}{2^{m+1}-1}.
```
Using the recursion `e_m=e_{m-1}/(2+e_{m-1})` (verified in §0), and
`e_{m-1}=1/(2^m-1)`:
```
e_{m-1}\cdot\frac{2^m-1}{2^{m+1}-1} = \frac{1}{2^m-1}\cdot\frac{2^m-1}{2^{m+1}-1}
= \frac{1}{2^{m+1}-1} = e_m.
```
So `e(\text{final})=e(R\text{-final})\ge e_m` exactly, **with equality attainable** (this is
precisely where the recursive/self-similar structure closes with no slack — consistent with
`D_m` itself being the extremal configuration). **Case B1 closed, for every `m\ge1`, by
induction.**

**Case B2: match to `a_i` for some `i\ge3` (a genuinely different split from bisection,
possible only when `m\ge2`).** XY splits `a_1` into `(a_i,\,a_1-a_i)`. Combined with `R`
(which contains its own copy of `a_i`), the multiset `R\cup\{a_i,a_1-a_i\}` has a duplicate
pair `\{a_i,a_i\}` (one from `R`, one new); by **Lemma P**,
```
e(\text{final}) = e\big((R\setminus\{a_i\})\cup\{a_1-a_i\}\big) =: e(R'').
```
**Dominance of the new top piece.** `a_1-a_i \ge a_1-a_2 = a_1/2 = a_2` (using `a_1=2a_2`
and `a_i\le a_2` since `i\ge3>2`), so `a_1-a_i` is at least as large as every remaining
element of `R\setminus\{a_i\}` (all `\le a_2`), hence it is the maximum of `R''` (ties, if
`a_1-a_i=a_2$, are harmless — Fact 2 does not require strict dominance, only that `a_1-a_i`
is *a* maximal element, which the definition of "sorted" already handles by convention).
Applying **Fact 2** to `R''` (with `x_1=a_1-a_i`, `\text{rest}=R\setminus\{a_i\}`, whatever
further cuts XY applies to `\text{rest}` using its remaining budget):
```
e(R'') = (a_1-a_i) - e\big((R\setminus\{a_i\})\text{-final}\big)
       \ge (a_1-a_i) - \max\big(R\setminus\{a_i\}\big)
       = (a_1-a_i) - a_2
```
(using Fact 2 a second time, on `R\setminus\{a_i\}`'s own further-cut result, exactly as in
Branch A: cutting cannot create anything bigger than `\max(R\setminus\{a_i\})=a_2`, since
`i\ge3` means `a_2\in R\setminus\{a_i\}` still). **Exact computation** (writing
`N:=2^{m+1}-1`, `a_1=2^m/N`, `a_2=2^{m-1}/N`, `a_i=2^{m+1-i}/N` for `i=3,\dots,m+1`):
```
(a_1-a_i)-a_2 = \frac{2^m-2^{m+1-i}-2^{m-1}}{N} = \frac{2^{m-1}-2^{m+1-i}}{N}.
```
We must check this is `\ge e_m=1/N`, i.e. `2^{m-1}-2^{m+1-i}\ge1`. Since `i\ge3`,
`m+1-i\le m-2`, so `2^{m+1-i}\le2^{m-2}`, giving
`2^{m-1}-2^{m+1-i}\ge2^{m-1}-2^{m-2}=2^{m-2}(2-1)=2^{m-2}\ge1` for every `m\ge2` (which is
exactly when this case can arise, since it needs `i\ge3\le m+1`, i.e. `m\ge2`). **So
`(a_1-a_i)-a_2\ge e_m` for every valid `(m,i)`, with equality exactly at `m=2,i=3`** (checked
directly: `m=2,i=3` gives `2^{m-2}=2^0=1`, tight; any larger `m` or `i` gives strict
inequality, since then `2^{m-1}-2^{m+1-i}>2^{m-2}\ge1`, or `2^{m-2}>1`). Hence
`e(\text{final})=e(R'')\ge(a_1-a_i)-a_2\ge e_m` in every case. **Case B2 closed, for every
valid `(m,i)`, by a direct elementary computation — no induction needed.** (This was verified
independently, for `m=2,\dots,7` and every valid `i`, by exact `Fraction` computation; see
below.)

**Conclusion of 5.1.** Combining Cases B1 (needs the level-`(m-1)` IH) and B2 (elementary,
self-contained): **every** strategy of XY that uses *exactly one* cut inside `a_1` (however
the remaining `\le m-1` cuts are spent on `R`, in any pattern) gives `e(\text{final})\ge e_m`.
Together with Branch A (Section above, also fully general in how `R`'s cuts are spent), this
proves the lower bound for **every** strategy of XY that spends **at most one** cut on
`a_1` — the entire single-cut-on-`a_1` vertex-candidate set from the vertex lemma is now
exhausted and closed.

##### 5.2 Two or more cuts landing inside `a_1` — OPEN, with strong (non-exhaustive) numerical support

This is the honestly-remaining gap, now sharply narrowed from the outline-reviewer's original
flag (which covered "any multi-cut strategy on `a_1`"): specifically, whether XY can ever
benefit from spending `c\ge2` of its cuts on subdividing `a_1` itself into `c+1\ge3` pieces
(directly, or via first matching to some `a_i` and then *further* cutting the leftover
fragment `a_1-a_i`, rather than leaving it as a single dominant piece as in Case B2 above).

**Numerical evidence gathered this round (exact `Fraction` grid search, not a proof):**
- `m=2` (budget 2, `D_2=(4,2,1)/7`): exhaustive search over **every** way of distributing 2
  cuts among the 3 pieces `a_1,a_2,a_3$ (all 7 distribution patterns `(c_1,c_2,c_3)` with
  `c_1+c_2+c_3\le2`, grid resolution 30 per cut) found global minimum `e=1/7=e_2` exactly, no
  violation.
- `m=3` (budget 3, `D_3=(8,4,2,1)/15`): trisecting `a_1` alone (2 cuts, `R` untouched, grid
  resolution 40) and quadrisecting `a_1` alone (3 cuts, `R` untouched, resolution 16) both
  found minimum `e=1/15=e_3` exactly, no violation; the minimizing trisection point found was
  `(4/15,2/15,2/15)=(a_2,a_3,a_3)` — i.e. bisect `a_1`, then bisect *one* of the resulting
  halves again down to `a_3`-sized pieces, an explicit multi-cut strategy that **ties** (does
  not beat) the plain-bisection value, consistent with (not violating) the target.
- The reviewer's own independent check (per `/tmp/round-3/outline-reviewer.md`) of trisecting
  `a_1` and of splitting `a_1` and `a_2` simultaneously at `m=2`, and a broader randomized
  3-cut search at `m=3`, also found no violation.
- `m=4` (budget 4, `D_4=(16,8,4,2,1)/31`, target `e_4=1/31`): a broad random search (300,000
  trials, uniformly sampling both the *distribution* of the 4 available cuts among the 5
  pieces and the split positions within each cut piece) found minimum `e=1/31` exactly (no
  violation), with the found minimizer using **3 of the 4 cuts entirely inside `a_1`**
  (quadrisecting it into 4 parts, `R` untouched) — a genuinely deep multi-cut-on-`a_1`
  strategy, and it still only *ties*, never beats, the target.
- **A cautionary finding, worth recording explicitly:** a natural candidate general lemma —
  "merging the two smallest parts of any partition of a dominant piece `a` (holding a fixed
  side-multiset `\text{Rest}` constant) never increases `e`," which would have given a clean
  one-line proof that finer partitions never help XY — was **tested and found FALSE** by
  random search (out of `40{,}000` random trials with `a>\text{sum}(\text{Rest})` enforced,
  more than a third violated it). So the multi-cut gap is **not** just an unproven-but-true
  bookkeeping triviality; a real, structure-specific argument (not a generic merging
  monotonicity) will be needed to close it. This negative result is recorded here so a future
  round does not waste time re-attempting the naive merging approach.

**Why a full proof is still open.** The obstruction is structural, not just "more casework":
when `\ge2` cuts land inside `a_1`, the resulting fragments of `a_1` can interleave with `R`'s
own (possibly also cut) elements in sorted order in ways that do not reduce, via a single
application of Lemma P, to a clean smaller instance of the same problem. Case B2 above
manages to avoid this by leaving the leftover fragment `a_1-a_i` **whole** (uncut) and using
Fact 2 directly on it; the natural next step would be to show that **further cutting
`a_1-a_i`** (or, symmetrically, cutting the *smaller* half after a bisection into pieces that
don't simply reproduce `R`) can be recursively bounded by the *same* Fact-2-style dominant
extraction, since `a_1-a_i\ge a_2` retains a dominance property of its own — but making this
rigorous requires either (a) strengthening the induction hypothesis to cover a broader class
of "top-heavy" multisets beyond the pure dyadic `D_j` (e.g. `(c,a_2,\dots,a_j)` with `c\ge
a_1`'s dyadic value, combined with a dyadic tail possibly missing some elements), or (b) a
direct argument that no cut ever *strictly* helps XY once Fact 2's dominance condition holds,
i.e. a genuine "extra cuts inside a dominant piece do not help" monotonicity lemma — this is
the same not-yet-proven bookkeeping fact flagged elsewhere in this file (see "Current best,"
item 4) surfacing again in its sharpest and most consequential form. **Neither (a) nor (b) is
established in this round; this is reported honestly as the precise remaining gap**, not
papered over — the single-cut case (5.1) is fully rigorous and unconditional, and the
multi-cut case is reduced to this one well-defined, numerically-well-supported open question.

### 5.2' — Revised skeleton for the multi-cut gap (round 4, proof-outliner; NOT YET PROVED,
this is the plan for the next builder)

**Step 0 (import, no re-derivation).** By certified **Lemma D/M**, XY's response to `D_m` is
exactly a legal sequence of `≤m` `D`(bisect)/`M`(match) operations on the active-value
multiset starting at `D_m = (2^m,\dots,2,1)/(2^{m+1}-1)`. Restate the target purely in this
language, dropping "which piece is physically `a_1`" language entirely:
```
For every m and every legal length-≤m D/M sequence starting at D_m, e(final) ≥ e_m.
```

**Step 1 (commutativity of independent operations — a short new lemma, cheap to prove).**
If two operations in a legal sequence act on disjoint sets of active values (neither touches
a value the other one produced or consumed), they commute: applying them in either order
yields the identical active multiset afterward. *Mechanism:* immediate from the definition of
`D`/`M` as multiset replacement — reordering two updates to disjoint parts of a multiset is
literally associativity of multiset union/difference. **Corollary:** in any legal sequence, we
may reorder so that the *first* operation involving the top value `a_1` (or whichever value is
currently `D_m`'s largest, i.e. rank-1) comes first in the sequence — WLOG, since everything
before it in the original order only touched `R := D_m\setminus\{a_1\}` and commutes past.

**Step 2 (the true case split — by content, not location).** After Step 1's WLOG reordering,
the sequence's first operation is either (a) `D(a_1)` [bisect `a_1`] or (b) `M(a_1,a_i)` for
some `i\ge2` [match `a_1` down against `a_i`]. **(a) is fully closed already** (Case B1,
§5.1): after `D(a_1)`, Lemma P collapses the state to exactly `R`, and the IH at level `m-1`
covers **every** legal continuation on `R` (this already handles arbitrarily many further
operations on `R`, including ones that would previously have been mis-classified as
"multi-cut" — there is no remaining gap for branch (a) at all, resolved for free by Step 1's
reordering). **(b) is the residual content of §5.2**: after `M(a_1,a_i)`, the leftover value
`\ell := a_1-a_i` remains active, together with `R\setminus\{a_i\}`; the old Case B2 (§5.1)
bounded this correctly **provided `\ell` is never touched again**. The genuine open question is
exactly: *what if a later operation in the sequence further touches `\ell` (splits it again)?*

**Step 3 (key lemma — broadened induction class, "dominant-tail" multisets `𝒟_j`).**

*Definition.* `𝒟_0 :=` any single nonnegative value. For `j\ge1`, `M\in𝒟_j` iff
`M = \{c\}\cup T` with `T\in𝒟_{j-1}` (so `|M|=j+1`) and `c \ge 2\max(T)` (the same ratio-2
dominance `D_j` itself has, `a_1=2a_2`, recursively down the whole chain).

*Claim (generalizes the whole §5 result to the class `𝒟_j`, not just the single point `D_j`).*
For every `M\in𝒟_j` with sum `S`, and every legal length-`≤j` D/M sequence starting at `M`
(touching the top value `c`, the tail `T`, or both, in any order, **including operations that
further split `c`'s own leftover after an earlier `M(c,\cdot)` step**), `e(\text{final}) \ge
e_j\cdot S`.

*Why this is the right generalization (mechanism, "induction loading" per crux `aimo-0292`):*
`D_m` itself lies in `𝒟_m`, but after `M(a_1,a_i)` (Step 2(b)), the state
`\{\ell\}\cup(R\setminus\{a_i\})` is generally **not** exactly `D_{m-1}` — it is a *different*
top-heavy multiset. The old proof (Case B2) sidestepped this by using Fact 2 once and never
recursing into `\ell`; the fix is to widen the IH so it applies to this whole family, not just
the single dyadic point, so recursion into `\ell` is licensed by the *same* strengthened
statement at level `j-1` (checking `\ell` retains the required `c\ge2\max(T)` dominance —
see Step 4).

**Step 4 (the one genuinely hard sub-claim — bounded, checkable, not unbounded search).**
Prove `\{\ell\}\cup(R\setminus\{a_i\})\in𝒟_{m-2}$-or-better after `M(a_1,a_i)`* — i.e. check
`\ell = a_1-a_i \ge 2\max(R\setminus\{a_i\})`. Since `D_m` is dyadic, `a_1=2a_2`, and for
`i\ge3`, `\max(R\setminus\{a_i\})=a_2$ (as `a_2\in R\setminus\{a_i\}$ still), so the needed
check is `a_1-a_i\ge2a_2 = a_1 \iff a_i\le0` — **false in general** (this is the point where
the naive class fails, exactly diagnosing why a further split of `\ell` is genuinely risky and
why this is the load-bearing gap, not a triviality). **Two ways to close this, either is
sufficient, and the builder should attempt (i) first (bounded, concrete) before falling back
to (ii):**
  (i) *Relax the dominance ratio inside `𝒟_j` from `\ge2` to a weaker, still-sufficient bound
  matched exactly to what `\ell` provably satisfies* (e.g. `c\ge\max(T)` alone, dropping the
  factor of 2, and re-deriving what value of `e_j$-analogue' this weaker class can guarantee —
  a bounded 1-2 level hand computation, check against the already-tabulated `m=2,3,4`
  numerics in old §5.2 before trusting it).
  (ii) *Fall back to a minimal-counterexample argument restricted to this exact sub-question*
  (crux `aimo-0287`/`aimo-0438` shape): assume, for contradiction, a minimal `m$ and a minimal
  number of "further splits of `\ell$" for which the bound fails; a local exchange (replacing
  the further split with the single already-covered `M(a_1,a_i)$ move, using the SPECIFIC
  numeric structure of `D_m$, not a generic side-multiset) either contradicts minimality or
  reduces to an already-closed case. This is narrower than the falsified general "merging
  monotonicity" lemma (that one needed to hold for *arbitrary* `Rest`; this one only needs to
  hold *given* an assumed minimal violator), so it survives the counterexample that killed the
  general form.

**Open gaps in this skeleton (honest):** Step 1 (commutativity) and Step 2 (case split) are
short, essentially mechanical, and should be provable outright by the builder in this round.
Step 3's class definition is new but the `j=0,1` base/first inductive layer should reduce to
already-proved material (§5.1). **Step 4 is the actual open mathematical content** — neither
(i) nor (ii) is verified yet; the builder should test (i) first against the existing `m=2,3,4`
numeric tie data (old §5.2) since it is the cheaper, more constructive route, and only fall
back to (ii) if (i)'s weakened class turns out insufficient to reproduce `e_j` exactly.

### 5.2'' — Round 4: Step-0 fix, three new general lemmas, and a partial attempt at Step 4

**Part A — fixing the Step-0 overclaim (required first, per the round-4 dispatch).**

The round-4 outline-reviewer correctly identified that §5.2' Step 0 overclaims: it restates
the lower-bound target as "for every legal length-`\le m` D/M sequence starting at `D_m`,
`e(\text{final})\ge e_m`," but **Lemma D/M** (`lemmas/dm-operation-reformulation.md`)
explicitly states in its own "Consequence" section that D/M sequences are only guaranteed to
be *achievable* (sufficient for upper-bound arguments), **not** that they capture Xiang Yu's
entire physical strategy space. For a *lower*-bound claim ("for every XY strategy..."), this
matters: restating the target in D/M language would silently narrow "every physical strategy"
down to "every D/M-expressible strategy," a strictly weaker statement, unless D/M-completeness
against `D_m` specifically is separately proved (which it is not, anywhere in this
population).

**Fix.** Drop the D/M reformulation for this purpose entirely. This is not a loss: Sections
5.1 (Branch A, Case B1, Case B2, all already fully proved) never actually used the D/M
formalism — they reason directly about **physical cut points** on the real stick, using
Lemma P directly on real duplicate physical pieces. The case split ("does XY's strategy touch
`a_1`, and if so, with how many cuts") is *already* well-defined and exhaustive purely in
physical terms, with no appeal to any operation-sequence formalism:

> A strategy of XY is, by definition, a choice of `\le m` cut points on the stick (after LB's
> own cuts have produced the multiset `D_m`). Each cut point lies inside exactly one of the
> pieces present at the time it is made (itself possibly a fragment of an earlier cut). The
> **final physical dissection** is determined purely by the *set* of cut points chosen — not
> by any ordering — since disjoint cuts on disjoint stick segments obviously do not interact
> (a cut point's effect, "split the piece it lands in at that point," depends only on which
> piece currently occupies that point of the stick, which is determined by the *other* cut
> points already fixed, regardless of what order they are considered in). So "XY's strategy"
> is fully and simply specified by (a) how many of its `\le m` cuts land at points that are,
> in the final dissection, inside the piece descended from `a_1` (this piece may itself have
> been further subdivided — "inside `a_1`" means: among the fragments that `a_1` is eventually
> partitioned into), and (b) how many land inside fragments descended from `R:=D_m\setminus
> \{a_1\}`. This gives the exhaustive, physical (not D/M-based) case split already used by
> Branch A / Branch B of §5: **0 cuts inside `a_1`** (Branch A, closed), **exactly 1 cut
> inside `a_1`** (§5.1, closed), and **`\ge2` cuts inside `a_1`** (§5.2, the open case,
> attacked further below with no D/M language needed).

This physical restatement is what the rest of this section (and all of §5.1, unchanged) uses.
No completeness claim about D/M sequences is invoked anywhere below.

**Part B — three new general lemmas, fully proved.**

**Fact 3 (block extraction).** Let `F` be a sorted multiset that splits as `F = X\sqcup Y`
(disjoint union as multisets) where every element of `X` is `\ge` every element of `Y` (so,
in `F`'s sorted order, all of `X`'s elements occupy the top `|X|` ranks, followed by all of
`Y`'s). Then
```
e(F) = e(X) + (-1)^{|X|}\, e(Y).
```
*Proof.* Write `X = (x_1\ge\dots\ge x_p)` sorted, `Y=(y_1\ge\dots\ge y_q)` sorted; by the
hypothesis, `F`'s sorted order is exactly `x_1,\dots,x_p,y_1,\dots,y_q`. Then
```
e(F) = \sum_{i=1}^p(-1)^{i+1}x_i + \sum_{j=1}^q(-1)^{p+j+1}y_j
     = e(X) + (-1)^p\sum_{j=1}^q(-1)^{j+1}y_j = e(X)+(-1)^{|X|}e(Y). ∎
```
(This generalizes Fact 2, which is the special case `|X|=1`.)

**Fact 4 (single-insertion bound).** Let `Y` be a sorted multiset of nonnegative reals and
`x\ge0`. Let `Z := Y\cup\{x\}` (insert one copy of `x`, re-sort). Then
```
|e(Z) - e(Y)| \le x.
```
*Proof.* Suppose `x` lands at sorted rank `r` in `Z` (i.e. exactly `r-1` elements of `Y` are
`>x`, hold that fixed). Split `Y = \text{head}\ \sqcup\ \text{tailseq}`, where `\text{head}`
is `Y`'s `r-1` elements exceeding `x` (unaffected by the insertion — they keep their original
ranks and signs) and `\text{tailseq}` is `Y`'s remaining `K-r+1` elements (all `\le x`, since
they sit at or below rank `r` in `Y`'s own order). Write `\text{head-sum} :=
\sum_{i<r}(-1)^{i+1}y_i` and `\text{tail} := \sum_{i\ge r}(-1)^{i+1}y_i` (both computed with
`Y`'s **original** rank-indexing), so `e(Y) = \text{head-sum}+\text{tail}`.

In `Z`, `\text{head}` keeps its ranks/signs unchanged (contributes `\text{head-sum}` again);
`x` sits at rank `r` (sign `(-1)^{r+1}`); and every element of `\text{tailseq}` shifts down by
exactly one rank (to make room for `x`), which **flips its sign** (rank `i\to i+1` flips
`(-1)^{i+1}\to(-1)^{i+2}=-(-1)^{i+1}`), so `\text{tailseq}`'s contribution becomes exactly
`-\text{tail}`. Hence
```
e(Z) = \text{head-sum} + (-1)^{r+1}x - \text{tail} = \big(e(Y)-\text{tail}\big) +
(-1)^{r+1}x - \text{tail} = e(Y) - 2\,\text{tail} + (-1)^{r+1}x.
```
Now write `\text{tail} = (-1)^{r+1}\,e_0(\text{tailseq})`, where `e_0(\text{tailseq})` is
`\text{tailseq}`'s *own* alternating sum with fresh rank-1 indexing (immediate from
`\text{tail}=\sum_{i\ge r}(-1)^{i+1}y_i = (-1)^{r+1}\sum_{j\ge0}(-1)^j y_{r+j} =
(-1)^{r+1}e_0(\text{tailseq})`). Substituting,
```
e(Z)-e(Y) = (-1)^{r+1}\big[x - 2\,e_0(\text{tailseq})\big].
```
By **Fact 1** applied to `\text{tailseq}` (itself sorted, since it is a suffix of the sorted
`Y`), `e_0(\text{tailseq})\ge0`; by **Fact 2** applied to `\text{tailseq}`,
`e_0(\text{tailseq})\le\max(\text{tailseq})\le x` (using `\text{tailseq}`'s elements are all
`\le x`, shown above). So `0\le e_0(\text{tailseq})\le x`, hence `x-2e_0(\text{tailseq})\in
[-x,x]`, giving `|e(Z)-e(Y)|\le x`. ∎

*(Remark, honestly recorded: this bound is in general **not tight enough** to close Step 4 by
itself — see Part C below for a concrete numeric witness of its looseness. It is recorded here
as a proved, reusable general fact, not as a claim that it solves the open gap.)*

**Fact 5 (chain-cancellation / ceiling achievability).** For **any** finite multiset of
nonnegative reals `\{y_1,\dots,y_L\}` (`L\ge0`), there is an explicit sequence of **exactly**
`L` physical cuts (applied only to fragments of these `L` pieces, no other pieces touched)
producing a final multiset with
```
e(\text{final}) = 0 \quad\text{exactly.}
```
*Proof, by induction on `L`.* `L=0`: the empty multiset has `e=0` vacuously, `0` cuts. `L=1`:
bisect `y_1` into `(y_1/2,y_1/2)`; this two-element multiset has `e=y_1/2-y_1/2=0` directly
(no need even for Lemma P — a direct 2-term computation), using exactly `1` cut. **Inductive
step (`L\ge2`, IH: the claim holds for `L-1`).** Relabel so `a:=y_1\ge b:=y_2` (WLOG, just a
choice of labels within the multiset). Cut `a` into `(b,\,a-b)` — **exactly 1 cut**, valid
since `0\le a-b<a` and `b\le a`. This creates a piece of value `b`, which together with the
*original* `y_2=b` forms a genuine duplicate pair `\{b,b\}` inside the physical multiset
`\{a-b,\,b,\,b,\,y_3,\dots,y_L\}`. By **Lemma P**, deleting this pair changes `e` by exactly
`0`, i.e.
```
e\big(\{a-b,b,b,y_3,\dots,y_L\}\big) = e\big(\{a-b,y_3,\dots,y_L\}\big).
```
The right-hand multiset `\{a-b,y_3,\dots,y_L\}` has exactly `L-1` real, nonnegative elements
(all genuine physical piece-lengths: `a-b` is the real leftover fragment of the cut just made,
`y_3,\dots,y_L` are untouched original pieces). By the **induction hypothesis**, applied to
*this specific* `(L-1)`-element list of real pieces, there is a sequence of exactly `L-1`
further physical cuts (applied only to fragments of `a-b,y_3,\dots,y_L`) achieving
`e(\text{their final result})=0`. Apply exactly this sequence. Since Lemma P's cancellation
from the first cut and the induction hypothesis's own (disjoint) cancellations each act on
their own distinct physical pieces (the first pair `\{b,b\}` is never touched again — it plays
no further role, its contribution to `e` is already accounted for as `0` — and the IH's
construction only ever touches fragments of `a-b,y_3,\dots,y_L`), the two sets of
cancellations compose without interaction, exactly as noted in Lemma P's own "Use" section
(applying the lemma repeatedly to disjoint pairs composes cleanly). So the **true final `e`**
of the whole `L`-cut construction equals the IH's guaranteed value, `0`. Total cuts used:
`1 + (L-1) = L`. This completes the induction. ∎

**Corollary (ceiling achievability).** For any sorted `M=(x_1\ge x_2\ge\dots\ge x_K\ge0)`,
`K\ge1`, using exactly `K-1` cuts (applied only to `x_2,\dots,x_K`, leaving `x_1` completely
untouched), XY can achieve
```
e(\text{final}) = x_1 = \max(M) \quad\text{exactly}
```
— i.e. **Fact 2's ceiling `e(M)\le\max(M)` is always exactly attainable within the natural cut
budget, never merely approached.** *Proof.* Apply Fact 5 to `\{x_2,\dots,x_K\}`
(`L=K-1` elements), using exactly `K-1` cuts, to drive its own `e`-contribution to exactly `0`.
Since every fragment produced by these cuts is `\le\max(x_2,\dots,x_K)=x_2\le x_1`, the
untouched `x_1` remains `\ge` every other element throughout, so it sits at rank `1` of the
true final sorted multiset. By **Fact 2** (exact identity, not just the inequality),
`e(\text{final}) = x_1 - e(\text{rest-final}) = x_1 - 0 = x_1`. ∎

**Why this matters for Step 4 (an honest, important negative/diagnostic finding).** Several
natural approaches to Step 4 (including ones tried earlier this round, see Part C) attempt to
bound the "away" part of a multi-cut strategy (e.g. `R\setminus\{a_i\}` after `M(a_1,a_i)`) via
Fact 2's crude ceiling and hope that ceiling is never actually *reached* within the available
budget, leaving some exploitable slack. **Fact 5 proves this hope is false in general**: the
ceiling is always exactly reachable with the *natural* budget (one fewer cut than the number
of elements). So any future proof of Step 4 **must** be a genuine joint/budget-tradeoff
argument — showing that whenever cuts are diverted from "pushing the residual `R\setminus
\{a_i\}` to its ceiling" toward "further splitting the leftover `\ell`," the *combined* effect
on `e(F)` cannot go below `e_m` — not a proof that decomposes into two independently-bounded
pieces. This sharpens (with an actual proof, not numerics) what previous rounds' "merging
monotonicity" refutation already suggested empirically, and gives the next attempt a precise
target.

**Part C — a concrete attempt at the simplest new sub-case, and where it stalls.**

The narrowest genuinely new content beyond what's already closed (Branch A, Case B1, Case B2
with `\ell` untouched) is: after `M(a_1,a_i)` (`i\ge3`), XY spends **some** of its remaining
budget splitting the leftover `\ell:=a_1-a_i` itself. The simplest nontrivial instance is
splitting `\ell` into **exactly 2** pieces `g_1\ge g_2\ge0` (`g_1+g_2=\ell`, one extra cut
beyond the initial match), with `R\setminus\{a_i\}` left **untouched** (the cleanest sub-case,
isolating the new phenomenon).

**Worked instance, fully closed by hand with exact fractions: `m=4`, `i=3`.** Here
`D_4=(16,8,4,2,1)/31`, `a_1=16/31`, `a_3=4/31`, `\ell=a_1-a_3=12/31`, and
`R\setminus\{a_3\}=\{a_2,a_4,a_5\}=\{8/31,2/31,1/31\}` (untouched). Writing `g_1\in
[6/31,12/31)` (the free parameter, `g_2=12/31-g_1`), a **complete case analysis on `g_1`**
(splitting on where `g_1,g_2` fall relative to `8/31,2/31,1/31$, exhaustively, by hand):

| `g_1` range | sorted order of `F` | `e(F)` |
|---|---|---|
| `[6/31,8/31)` | `8/31,g_1,g_2,2/31,1/31` | `19/31-2g_1` (from `7/31` down to `3/31`) |
| `[8/31,10/31]` | `g_1,8/31,g_2,2/31,1/31` | `= \ell-9/31 = 3/31` (constant) |
| `(10/31,11/31]` | `g_1,8/31,2/31,g_2,1/31` | `2g_1-17/31` (from `3/31` up to `5/31`) |
| `(11/31,12/31)` | `g_1,8/31,2/31,1/31,g_2` | `=\ell-7/31=5/31` (constant) |

(Each row derived directly from the alternating-sum definition applied to the stated sorted
order, using `g_1+g_2=12/31$ to eliminate one variable; boundary values checked to agree
between adjacent rows, confirming continuity and no gap in the case split.) **The minimum
over the whole range is exactly `3/31`, attained on the plateau `g_1\in[8/31,10/31]`.**
Compared to the target `e_4=1/31`: `3/31>1/31`, safely above — **no violation, this instance
is fully closed.** (Independently re-verified by exact-`Fraction` computation matching this
table precisely.)

**Why this does not generalize cleanly to a proof for general `m`.** Two general techniques
were tried to turn this single worked instance into a general argument, and **both failed**:

1. **Fact 2 alone (peel the current maximum, bound the rest crudely).** Splitting on whether
   `g_1\ge a_2` or `g_1<a_2$ and peeling via Fact 2 gives, in the two sub-cases,
   `e(F)\ge g_1-a_2` (sub-case `g_1\ge a_2`) or `e(F)\ge a_2-\ell` (sub-case `g_1<a_2`, using
   Fact 1 as a fallback since the Fact-2-derived bound is even worse — see item 2). **Neither
   bound is `\ge e_m` uniformly**: the first is `\ge0$ only, useless as `g_1\to a_2^+`; the
   second, `a_2-\ell=a_2-(a_1-a_i)=a_i-a_2$, is **negative** for every `i\ge3` (since
   `a_i\le a_3<a_2`), hence trivially useless (weaker than Fact 1's own `e(F)\ge0`). Compare to
   the worked instance's true minimum `3/31$: at the plateau's left end `g_1=8/31=a_2` exactly,
   the crude bound `g_1-a_2=0` — far short of the true value `3/31` — confirming this method
   really is too lossy, not merely inconvenient to compute.
2. **Fact 4 (insertion bound), inserting `g_1,g_2` into the fixed `R\setminus\{a_i\}`.** This
   gives `e(F)\ge E_0-\ell` where `E_0:=e(R\setminus\{a_i\}\text{ untouched})`. For the worked
   instance, `E_0=7/31`, giving `e(F)\ge7/31-12/31=-5/31$ — **worse than useless** (negative,
   while the true minimum is `+3/31`), a concrete numeric witness that Fact 4's bound, though
   correctly proved, is **too lossy** for this purpose. (This is the "known caveat" flagged
   generically in Fact 4's own proof, now confirmed concretely against real problem data.)

**What actually closed the worked instance** was a full, sorted-order case split tracking
exactly where `g_1,g_2` interleave with `R\setminus\{a_i\}`'s (here, only 3) elements — a
method that is correct but whose casework complexity grows with `|R\setminus\{a_i\}|=m-2`
(unboundedly many interleaving patterns as `m\to\infty`), so it does **not**, as carried out
here, give a general-`m` proof; only this one concrete `(m,i)=(4,3)` instance is closed.

**Honest conclusion.** Step 4 (`\ge2` cuts inside the dominant piece, in particular the "leftover
gets further split" sub-case) remains **open** for general `m`. This round's contribution is:
(a) removing the D/M-completeness dependency that would otherwise have undermined *any*
resolution of Step 4 (Part A); (b) three new, general, reusable lemmas, of which Fact 5 gives a
proved (not conjectural) structural reason why the natural "bound the residual, it can't reach
its ceiling" approach cannot work, redirecting future attempts toward a genuine joint
budget-tradeoff argument (Part B); (c) one additional concrete instance fully closed by hand,
adding to (and now more precisely explaining, via the exact plateau structure) the existing
numerical evidence base, while honestly documenting that the technique used does not scale to
a general-`m` proof as carried out (Part C).

### 5.3 — the integer/superincreasing "no-early-zero" reframe — a genuinely different
mechanism for the WHOLE lower bound (Main Claim/Step 3 PROVED IN FULL, round 5; the D/M-
sequence result is now unconditional — see §3.7's closing paragraph for the one remaining,
pre-existing, separately-tracked caveat needed to promote it to the true physical lower bound)

**Motivation.** Steps 5–5.2'' above attack Step 4 by casework on *where* cuts physically land.
This round's lowerbound-multicut explorer flagged a different, invariant-style opening
("cancelling vs. non-cancelling cuts") which, made precise below, turns out to reduce the
*entire* lower bound (not just Step 4) to a single clean combinatorial non-vanishing claim.
This is a genuinely different *kind* of argument (a parity/integrality obstruction, not a case
split), so it is presented as a new top-level skeleton for the lower-bound half of this
approach, coexisting with §5–§5.2'' (kept as-is: a valid, independent fallback/cross-check for
Branch A, B1, B2 and the `m=4,i=3` instance, all still correct and citable regardless of
whether §5.3 succeeds).

**Step 0 (scope/import).** Work with the certified **Lemma D/M** operations (`D`/`M`, as
defined in `lemmas/dm-operation-reformulation.md`) and the certified
**`lemmas/dm-completeness-partial.md`** (`g(A,m)=h(A,m)`, the true physical minimum equals the
D/M-search minimum, *provided* the global minimizer's tie-dependency graph is not a nonempty
union of directed cycles — a condition never observed to occur, not proved impossible). Citing
this lemma is now legitimate (it was NOT available when the round-4 outline-reviewer flagged
the D/M-completeness overclaim; it has since been certified) — this is the one place in this
file where working in D/M language for a *lower*-bound claim is justified, with the residual
"all-cycles" case explicitly flagged as an inherited, open caveat (see "Watch out for" at the
end of this section).

**Step 1 (Integer Invariant Lemma — easy, prove in full).** Work with the *raw* (unnormalized)
dyadic multiset `D_m := (2^m, 2^{m-1}, \dots, 2, 1)` (integer entries, `S(D_m)=2^{m+1}-1`); the
target `e_m\cdot S(D_m) = 1/(2^{m+1}-1)\cdot(2^{m+1}-1) = 1` **exactly, for every `m`** — a
clean, `m`-independent integer target.

*Claim.* Every active multiset reachable from `D_m` by any legal sequence of D/M operations
consists entirely of nonnegative **integers**.

*Proof.* Induction on the number of operations performed. Base case: `D_m` itself is all
integers. Inductive step: `D(x)` deletes an existing active integer, leaving integers; `M(x,y)`
removes two active integers `x\ge y` and inserts `x-y`, itself a nonnegative integer. ∎
(Trivial, but load-bearing: it licenses Step 2.)

**Step 2 (`e=0` characterization — easy, prove in full).** For *any* sorted multiset `M` of
nonnegative reals (not just integers), `e(M)=0` iff, after repeatedly deleting exact
duplicate-value pairs (Lemma P), what remains is either empty or consists only of copies of the
value `0`.

*Proof.* By Fact 1's own proof, `e(M) = \sum(x_{2i-1}-x_{2i}) (+ \text{possibly one unpaired
trailing term } x_{\text{last}})`, a sum of manifestly **nonnegative** terms (`x_{2i-1}\ge
x_{2i}` since sorted). A sum of nonnegative terms is `0` iff **every** term is `0`, i.e. every
consecutive pair is exactly *equal* (`x_{2i-1}=x_{2i}`) and any unpaired trailing term is
itself `0`. Equal consecutive pairs are exactly duplicate pairs (Lemma P), which cancel with no
residue; an unpaired trailing term forced to `0` is (trivially) a "duplicate pair" with the
value `0`. ∎

**Combining Steps 1–2 with Fact 1 (`e\ge0` always):** for any D/M-reachable state `M` from
`D_m`, `e(M)` is a **nonnegative integer**. Hence:
```
e(M) \ge 1 \iff e(M) \ne 0.
```
So proving the lower bound `e(\text{final})\ge e_m\cdot S(D_m) = 1` for every legal XY response
using `\le m` cuts is **equivalent** to proving:

> **Main Claim.** No legal sequence of `\le m` D/M operations starting at `D_m` ever reaches an
> active state with `e=0`.

By Step 2, an active state has `e=0` iff it reduces (via duplicate-pair cancellation) to empty
or all-zero — informally, "XY has fully paired off / cancelled the whole multiset." **Fact 5**
(already certified, `lemmas/insertion-and-cascade-facts.md`) shows this IS achievable, but
needs exactly `L=m+1` cuts (one for each of `D_m`'s `m+1` elements) — i.e. `D_m` can be driven
to `e=0`, just not within XY's `m`-cut budget. **The Main Claim is exactly the statement that
`m+1` is the minimum, not merely an achievable, cut count for reaching `e=0` from `D_m`.**

**Numerical confirmation (exact-integer BFS, exhaustive, run this round, not sampled).**
Computed the true minimum number of D/M operations needed to reach ANY `e=0` state, for every
`m=1,\dots,5`, by full breadth-first enumeration of the (integer-valued, hence finite and
enumerable) reachable-state graph:
```
m=1: min ops to e=0 is 2  (=m+1)      m=4: min ops to e=0 is 5  (=m+1)
m=2: min ops to e=0 is 3  (=m+1)      m=5: min ops to e=0 is 6  (=m+1)
m=3: min ops to e=0 is 4  (=m+1)
```
**Exact match to `m+1` at every `m` tested, zero exceptions.** Separately confirmed (same
harness) that the minimum value of `e` achievable using *exactly* `m` operations is exactly
`1` at every `m=1,\dots,5` — matching the target precisely, not merely `\ge1`.

**Why superincreasing-ness is the load-bearing hypothesis (stress test, run this round).**
Repeated the same "minimum ops to reach `e=0`" computation on: (a) **13 random strictly
superincreasing sequences** (`a_i > a_{i+1}+\dots+a_k` for every `i`, sizes `3`–`5`, random
integer gaps) — **every one needed exactly `k` ops** (`k`=its own size), matching `D_m`'s
pattern exactly; (b) **5 random non-superincreasing sequences** of comparable size — **every
one admitted a shortcut**, reaching `e=0` in *fewer* than `k` ops (e.g. `(18,12,8,8)`, size 4,
reached `e=0` in only `2` ops, via the pre-existing near-duplicate `8,8`). This is strong
evidence the superincreasing property of `D_m` (`a_i=2a_{i+1}`, hence
`a_i > a_{i+1}+\dots+a_k$ since the tail is a geometric series summing to `<a_{i+1}\cdot2=a_i`)
is exactly what prevents early cancellation — not a coincidence of the specific numbers.

**Step 3 (the No-Early-Zero Lemma — PROVED IN FULL, round 5).**

> **Theorem (No-Early-Zero Lemma).** Let `a_1>a_2>\dots>a_k>0` be strictly superincreasing
> (`a_i>a_{i+1}+\dots+a_k` for every `i<k`). Then for every legal sequence of `t<k` D/M
> operations starting from `\{a_1,\dots,a_k\}`, the resulting active multiset `M_t` (which has
> exactly `k-t\ge1` elements) satisfies `e(M_t)>0` — strictly. In particular, no sequence of
> fewer than `k` D/M operations ever reaches an active state with `e=0`.

This is exactly the lemma the round-5 outliner conjectured (Step 3 as originally stated), now
proved in full generality (not just for the specific dyadic `D_m`), by an elementary
"signed-sum / token" argument. No induction-loading, no bounded lookahead, no unbounded
casework is needed — the whole proof is four short, self-contained sub-steps.

**3.1 — Distinct signed sums over a superincreasing sequence are never zero.**

*Claim.* For strictly superincreasing `a_1>\dots>a_k>0`, any nonempty `S\subseteq\{1,\dots,k\}`,
and any sign function `\varepsilon:S\to\{+1,-1\}`,
```
\sum_{i\in S}\varepsilon(i)\,a_i \;\ne\; 0.
```
*Proof.* Let `i_0:=\min(S)` (so `a_{i_0}=\max_{i\in S}a_i`, since `a` is strictly decreasing in
its index). Then
```
\Big|\sum_{i\in S\setminus\{i_0\}}\varepsilon(i)a_i\Big|
  \le \sum_{i\in S\setminus\{i_0\}} a_i
  \le \sum_{i=i_0+1}^{k} a_i
  < a_{i_0}
```
(the first inequality is the triangle inequality applied term-by-term with `\varepsilon(i)a_i\le
a_i`; the second holds because `S\setminus\{i_0\}\subseteq\{i_0+1,\dots,k\}` and every `a_i\ge0`,
so restricting to a subset of nonnegative terms only decreases the sum; the third is exactly the
superincreasing hypothesis at index `i_0`, strict). Writing the full sum as
`\varepsilon(i_0)a_{i_0} + \sum_{i\in S\setminus\{i_0\}}\varepsilon(i)a_i`, the first term has
absolute value exactly `a_{i_0}`, strictly larger than the absolute value of the second term, so
by the reverse triangle inequality (`|x+y|\ge|x|-|y|`) the total has absolute value `>0`, i.e. is
nonzero. `\blacksquare`

**3.2 — The token invariant (proved by induction on the number of operations performed).**

For a legal D/M sequence starting at `\{a_1,\dots,a_k\}`, assign to *every value that is ever an
active element at any point in the process* a pair `(S(v),\varepsilon(v))`: `S(v)\subseteq
\{1,\dots,k\}` nonempty, `\varepsilon(v):S(v)\to\{+1,-1\}`, defined recursively by:
- if `v=a_i` (one of the original values, still untouched): `S(v):=\{i\}`, `\varepsilon(v)(i):=+1`;
- if `v` is created by `M(x,y)` (`v=x-y`, `x,y` the two active elements consumed): `S(v):=
  S(x)\sqcup S(y)` (disjoint union — proved disjoint below) and `\varepsilon(v)|_{S(x)}:=
  \varepsilon(x)`, `\varepsilon(v)|_{S(y)}(j):=-\varepsilon(y)(j)` for `j\in S(y)` (i.e. flip
  every sign inherited from `y`'s side).

*Invariant claim, proved by induction on the number of operations `T\ge0` performed so far:*
**(I1)** the index sets `\{S(v):v\text{ active}\}` are pairwise disjoint subsets of
`\{1,\dots,k\}`; **(I2)** every active `v` satisfies `v=\sum_{i\in S(v)}\varepsilon(v)(i)\,a_i`
exactly.

*Base case `T=0`.* Active set `=\{a_1,\dots,a_k\}`; `S(a_i)=\{i\}` are pairwise-disjoint distinct
singletons ((I1)), and `a_i=\sum_{j\in\{i\}}(+1)a_j` trivially ((I2)). ✓

*Inductive step.* Assume (I1),(I2) hold after `T` operations; apply one more operation.
- `D(x)` for active `x`: the new active set is the old one with `x` removed. (I1): removing one
  set from a pairwise-disjoint family leaves it pairwise-disjoint. (I2): unaffected for every
  remaining `v` (its representation is untouched). `x`'s token (and `S(x)`) is simply retired —
  never appears again in the process, since `D` deletes it outright with no replacement value
  (see `lemmas/dm-operation-reformulation.md`'s definition of `D`). ✓ *(This is exactly how the
  argument handles `D`-operations interleaved with `M`-chains, closing the round-5 outline's
  flagged sub-point (a): `D` never creates a new token, so it cannot introduce a new tie or
  violate either invariant — it can only ever remove candidates from future consideration.)*
- `M(x,y)` for two **distinct** active elements `x,y` (`x` value `\ge` `y` value; by the
  definition of `M` in `lemmas/dm-operation-reformulation.md`, `x` and `y` are always two
  different active slots): let `v:=x-y`. By (I1) at time `T`, `S(x)` and `S(y)` are disjoint
  (both were members of the pairwise-disjoint family), so `S(v):=S(x)\sqcup S(y)` is a genuine
  disjoint union, nonempty since `S(x)\ne\emptyset`. For (I2):
  ```
  v = x - y = \sum_{i\in S(x)}\varepsilon(x)(i)a_i - \sum_{j\in S(y)}\varepsilon(y)(j)a_j
    = \sum_{i\in S(x)}\varepsilon(x)(i)a_i + \sum_{j\in S(y)}\big(-\varepsilon(y)(j)\big)a_j
    = \sum_{i\in S(v)}\varepsilon(v)(i)a_i,
  ```
  matching the definition of `\varepsilon(v)` above exactly. Every other active element's
  representation is untouched. For (I1): the new family is the old family with `S(x)` and
  `S(y)` removed and `S(x)\sqcup S(y)` inserted in their place. Since `S(x)` and `S(y)` were each
  already disjoint from every *other* member `S(w)` of the old pairwise-disjoint family (by (I1)
  at time `T`), and disjoint from each other, their union `S(x)\sqcup S(y)` is disjoint from
  every other `S(w)` too (a union of two sets each disjoint from a third is disjoint from that
  third). So the new family remains pairwise disjoint. ✓ *(This handles the outline's flagged
  sub-point (b) — merges combining non-contiguous or "far apart" indices, e.g. `\{2\}` and
  `\{5\}` directly: the invariant makes no assumption that `S(v)` be a contiguous block of
  indices, only that it be a nonempty subset, disjoint from every other currently-active token's
  index set — which is exactly what is proved, unconditionally, at every step. In particular
  index sets across *simultaneously active* tokens never overlap, at any point in any legal
  sequence — overlapping never actually arises, so no special casework for it is needed.)*

By induction, (I1) and (I2) hold at every point of every legal D/M sequence starting from a
strictly superincreasing `\{a_1,\dots,a_k\}`. `\blacksquare`

**3.3 — Corollary: active tokens are always pairwise distinct and strictly positive.**

At every point of any legal D/M sequence from strictly superincreasing `\{a_1,\dots,a_k\}`:
(i) every active token has value `>0`; (ii) any two distinct active tokens have distinct values.

*Proof.* (i) By 3.2, an active token `v` satisfies `v=\sum_{i\in S(v)}\varepsilon(v)(i)a_i` with
`S(v)` nonempty; by 3.1 this sum is `\ne0`. Also `v\ge0` always, since `v` is either an original
`a_i>0` or was produced by `M(x,y)=x-y` with `x\ge y\ge0` (by definition of `M`), hence `v=x-y
\ge0`. Combining, `v>0`.
(ii) Let `u\ne v` be two distinct active tokens present simultaneously. By (I1), `S(u)` and
`S(v)` are disjoint. Set `\delta:S(u)\sqcup S(v)\to\{+1,-1\}` by `\delta:=\varepsilon(u)` on
`S(u)` and `\delta:=-\varepsilon(v)` on `S(v)` (well-defined, since the domains are disjoint).
Then, using (I2) for both `u` and `v`,
```
u - v = \sum_{i\in S(u)}\varepsilon(u)(i)a_i - \sum_{j\in S(v)}\varepsilon(v)(j)a_j
      = \sum_{i\in S(u)\sqcup S(v)}\delta(i)a_i,
```
a signed sum over the nonempty set `S(u)\sqcup S(v)` (nonempty since `S(u)\ne\emptyset`); by 3.1
this is `\ne0`, i.e. `u\ne v` as real numbers. `\blacksquare`

**3.4 — A strict alternating sum of distinct positive reals is strictly positive.**

*Claim.* If `x_1>x_2>\dots>x_s>0` (`s\ge1`, all strict since pairwise distinct and sorted), then
`e:=x_1-x_2+x_3-x_4+\dots+(-1)^{s+1}x_s > 0`.

*Proof.* Pair consecutive terms: if `s` is even, `e=(x_1-x_2)+(x_3-x_4)+\dots+(x_{s-1}-x_s)`, a
sum of `s/2\ge1` terms each `>0` (since `x_{2i-1}>x_{2i}` strictly), hence `e>0`. If `s` is odd,
`e=(x_1-x_2)+\dots+(x_{s-2}-x_{s-1})+x_s`, a sum of `(s-1)/2\ge0` strictly positive terms plus
the strictly positive trailing term `x_s>0`, hence `e>0` (the trailing term alone already
suffices when `s=1`). Either way `e` is a sum of at least one strictly positive term and no
negative ones, so `e>0`. `\blacksquare`

**3.5 — Proof of the Theorem (Step 3, general form).** Fix `t<k` and a legal length-`t` D/M
sequence from `\{a_1,\dots,a_k\}`. Since each of `D`,`M` reduces the active count by exactly 1
(`D` removes one element with no replacement; `M` removes two, inserts one), the resulting
active multiset `M_t` has exactly `k-t` elements, and `k-t\ge1` since `t<k` (i.e. `t\le k-1`). By
3.3, `M_t`'s `k-t\ge1` active tokens are pairwise distinct (3.3(ii)) and strictly positive
(3.3(i)); sorting them descending `x_1>x_2>\dots>x_{k-t}>0` (strict inequalities throughout,
since distinct), 3.4 gives `e(M_t)>0`, strictly. `\blacksquare`

**3.6 — Specialization to `D_m` (Main Claim, fully proved).** `D_m=(2^m,2^{m-1},\dots,2,1)` is
strictly superincreasing: `2^i > 2^{i-1}+2^{i-2}+\dots+2+1 = 2^i-1` for every `i\ge1` (the
geometric-series identity, strict since `2^i \ne 2^i - 1`), and has `k=m+1` elements. By the
Theorem (3.5), every legal D/M sequence of length `t\le m=k-1` starting from `D_m` produces an
active multiset with `e>0`. Combined with **Step 1** (every value reached is a nonnegative
**integer**, since `D_m`'s entries are integers and `D`,`M` preserve integrality), `e(M_t)` is a
strictly positive integer, hence `e(M_t)\ge1`, for **every** `t=0,1,\dots,m`. This is exactly
the Main Claim from Step 2 above, now **fully and unconditionally proved**: no legal sequence of
`\le m` D/M operations starting at `D_m` ever reaches `e=0` — indeed `e` never drops below `1`
throughout the whole `\le m`-operation budget.

**3.7 — Normalization back to the actual (`S=1`) problem.** The theorem's target is stated for
the *normalized* dyadic construction `\widetilde D_m:=D_m/S(D_m)` (each entry divided by
`S(D_m)=2^{m+1}-1`, so `S(\widetilde D_m)=1`), matching how Liu Bang's opening is actually
presented (a partition of the unit stick). Two facts connect the raw-integer result (3.6) to the
normalized target, both elementary and made fully explicit here (per this section's own "Watch
out for" reminder from the previous round, now discharged):

1. **`e` scales linearly.** For any finite multiset `M'` of nonnegative reals and any `c>0`,
   `e(cM')=c\cdot e(M')`. *Proof:* scaling every entry of `M'` by the positive constant `c`
   leaves the sorted order unchanged (multiplying by a positive constant is order-preserving),
   so the alternating-sum formula for `e` — which depends only on the sorted order and the raw
   values — literally scales by `c` termwise: `e(cM')=\sum_i(-1)^{i+1}(c\cdot m_i)=c\sum_i
   (-1)^{i+1}m_i=c\cdot e(M')`.
2. **D/M sequences on `\widetilde D_m` are in exact bijection with those on `D_m`.** Scaling
   every operand of a legal D/M sequence on `D_m` by `c:=1/S(D_m)` produces a legal D/M sequence
   on `\widetilde D_m` with the identical combinatorial structure (same elements combined/deleted,
   same order): `D(x)` becomes `D(cx)` (still a legal single-element deletion) and `M(x,y)`
   becomes `M(cx,cy)` (still legal, since `x\ge y\iff cx\ge cy` for `c>0`, and produces `cx-cy=
   c(x-y)`, matching the scaled value of what `M(x,y)` would have produced). This bijection is
   its own inverse (scale by `S(D_m)` to go back), so the set of `e`-values achievable by legal
   length-`\le m` D/M sequences from `\widetilde D_m` is *exactly* `c` times the set of
   `e`-values achievable from `D_m` (fact 1 above applied to each achievable final state).

Combining: the minimum `e`-value achievable by a length-`\le m` D/M sequence from
`\widetilde D_m` equals `c` times the minimum from `D_m`, which by 3.6 is `\ge c\cdot1 = 1/
(2^{m+1}-1) = e_m = e_m\cdot S(\widetilde D_m)`. This is **exactly** the target inequality
`e(\text{final})\ge e_m\cdot S` for D/M-achievable responses to the (normalized) dyadic
construction `\widetilde D_m`, at every level `m`.

**Honest accounting of what §5.3 now proves vs. what remains conditional.** Steps 1–3.7 give a
complete, unconditional proof that
```
h(\widetilde D_m,\,m) \;\ge\; e_m\cdot S(\widetilde D_m) \qquad\text{for every }m\ge0,
```
where `h(A,m)` (per `lemmas/dm-completeness-partial.md`'s notation) is the minimum of `e` over
*D/M-achievable* responses only. This is a genuine new theorem (Step 3 was previously flagged
"NOT proved" and is now proved in full, more generally than even conjectured). **What this does
NOT by itself establish** is the corresponding bound for `g(\widetilde D_m,m)`, the true minimum
over Xiang Yu's *entire* physical strategy space (not just the D/M-representable subset) — that
requires `g=h`, which is `lemmas/dm-completeness-partial.md`'s **conditional** result (holds
provided the global minimizer's tie-dependency graph is never a nonempty union of directed
cycles — a case never observed to occur for any `A,m` tested, in this population or this round's
fresh checks, but not proved impossible). **This caveat is pre-existing and unaffected by this
round's work** — it is not introduced, worsened, or resolved by the Step 3 proof above, and
remains the one open link between "no D/M sequence beats the target" (now fully proved) and "no
*physical* strategy beats the target" (the theorem's actual lower-bound claim). If a future round
closes the all-cycles caveat (or shows it cannot arise for the specific family `A=D_m`), §5.3
would then give a **complete, unconditional proof of the entire lower-bound direction, for every
`m`, in one shot** — subsuming §5–§5.2''s Branch A/B/Step-4 casework entirely (those sections
remain independently valid and citable in the meantime, as an unconditional-but-partial
fallback that does not need the D/M-completeness machinery at all).

**Alternative opening considered and deprioritized (honest note).** The lowerbound-multicut
explorer also flagged a "two-sided/dual pairing bound" opening (crux `aimo-0388`), bounding `e`
via two different offset pairings of the same sorted sequence. This was considered but not
developed into a skeleton this round: `aimo-0388`'s stack-split is a *free choice* in that
problem, whereas here the odd/even-rank split defining `e` is *forced* by Lemma G, so the
direct transplant does not apply; a genuine adaptation was not found in the time available.
Flagged here so a future round does not need to re-investigate whether it transfers literally
(it does not) before looking for a non-literal adaptation.

**Watch out for (updated, round 5 — two of the three original concerns are now resolved):**
- **(Still open, unaffected by this round.)** The residual "all-cycles" tie-dependency edge case
  in `dm-completeness-partial.md`: if some physical XY strategy exists that is *not* expressible
  as a D/M sequence (only possible in that narrow, never-observed case) and that strategy reaches
  `e=0` within `\le m` cuts, §5.3's argument (proved only for D/M-achievable responses) would not
  catch it. This has never been observed in any search across this population (including this
  round's fresh exhaustive checks), but is not excluded by proof. This is the *only* remaining
  gap standing between §5.3's now-complete D/M-sequence result and the full physical-strategy
  lower bound.
- **(Resolved this round.)** Handling `D`-operations interleaved with `M`-chains: proved
  explicitly in the token-invariant induction (§3.2's `D(x)` case) — a `D` simply retires a token
  and its index set, never creating a new value, so it cannot introduce a coincidental tie; this
  is now a proved step, not an assumption.
- **(Resolved this round.)** Values formed from overlapping or non-contiguous index subsets:
  proved explicitly in §3.2 (I1) that active tokens' index sets are *always* pairwise disjoint
  (never overlapping) at every step, for arbitrary (not necessarily contiguous) subsets — the
  invariant makes no contiguity assumption anywhere, so this concern does not arise.
- **(Resolved this round.)** The raw-integer-to-normalized-`[0,1]` rescaling is now spelled out
  explicitly in §3.7 (two named, proved facts: `e` scales linearly under positive scalar scaling
  of all entries, and D/M sequences on the normalized `\widetilde D_m` are in exact bijection
  with those on the raw `D_m`), not left implicit.

## Promotable lemmas

Both certified in full this round and written to the shared lemma cache:
- **Lemma G** (greedy reduction of the alternating claiming game to the odd/even-rank sum,
  with "take current max" proved optimal) — `results/imo-2026-03/lemmas/greedy-reduction.md`.
- **Lemma P** (duplicate-pair invariance of `e=L-X`, general form: any two equal-valued
  entries, not just an even-multiplicity run) — `results/imo-2026-03/lemmas/duplicate-pair-invariance.md`.

Both are fully self-contained, general-purpose (not specific to this problem's numbers),
and available for import by any other approach in this problem's population (all three
sibling approaches that already rely on "Lemma P-zero" per the outline-reviewer's report can
now cite these certified files instead of re-deriving/re-verifying numerically).

**New this round, both fully proved and general-purpose (candidates for a new certified
lemma file, e.g. `lemmas/dominant-extraction.md`), stated in full in §5 above:**
- **Fact 1 (`e(M)\ge0` for any sorted multiset `M`).** Immediate corollary of the pairing
  inequality already inside Lemma G's proof (`x_1+x_3+\dots\ge x_2+x_4+\dots`); not
  previously named as a standalone fact anywhere in this problem's population. Fully general
  (no reference to cuts or this problem's specific numbers).
- **Fact 2 (`e(M)\le\max(M)`, "dominant extraction").** For any sorted multiset
  `M=(x_1\ge\dots\ge x_K)`, the *exact* identity `e(M)=x_1-e(\text{rest})` holds (elementary,
  from the definition of `e` as an alternating sum), and combined with Fact 1 applied to
  `\text{rest}`, gives the inequality `e(M)\le\max(M)`. Fully general, proved in 3 lines,
  used twice in §5 (Branch A and Case B2) to get clean elementary lower bounds without
  needing the induction hypothesis at all.

Both facts are short, fully proved in §5 above (not merely asserted), general-purpose (apply
to any sorted multiset, not just this problem's dyadic construction), and directly reusable
by any other approach or lemma file in this population that needs to bound `e` of a
multiset with a clearly dominant top element (e.g. `concavity-minimax-duality`'s edge-normal
concavity checks, or `elementary-exchange-smoothing`'s local-uniqueness certificates, could
potentially use Fact 2 as a cheap sanity bound). Recommend the reviewer certify these as a
new lemma file if independently re-verified.

**Also recorded this round, a useful negative result (not a lemma, but worth preserving so
no future round re-attempts it):** the natural candidate general fact "merging the two
smallest parts of any partition of a dominant element `a` (holding a fixed side-multiset
`\text{Rest}` constant, with `a>\text{sum}(\text{Rest})`) never increases `e`" is **FALSE**
— refuted by random search (see §5.2). Any future attempt to close the remaining multi-cut
gap (item 1 in "Current best") should not rely on a lemma of this shape.

**New this round (round 4), all fully proved and general-purpose, stated in full in §5.2''
above — candidates for a new certified lemma file, e.g. `lemmas/insertion-and-cascade-facts.md`:**
- **Fact 3 (block extraction).** Generalizes Fact 2 from a single dominant element to a
  dominant *block*: if sorted `F=X\sqcup Y` with every element of `X\ge` every element of `Y`,
  then `e(F)=e(X)+(-1)^{|X|}e(Y)` exactly. Three-line proof, purely combinatorial (rank
  bookkeeping), no reference to cuts or this problem's numbers.
- **Fact 4 (single-insertion bound).** Inserting one new value `x\ge0` into a sorted multiset
  `Y` changes `e` by at most `x` in absolute value: `|e(Y\cup\{x\})-e(Y)|\le x`. Proved via a
  clean head/tail decomposition combined with Facts 1 and 2 applied to the affected tail.
  **Honestly flagged as insufficient alone** for closing this problem's remaining multi-cut
  gap (Part C above gives a concrete numeric witness, `m=4,i=3`, where this bound gives a
  useless negative value `-5/31` against a true minimum of `+3/31`) — still recorded as a
  correct, reusable general fact for other purposes.
- **Fact 5 (chain-cancellation / ceiling achievability).** For any `L`-element multiset of
  nonnegative reals, there is an explicit sequence of exactly `L` cuts driving its `e` to
  exactly `0`. Corollary: Fact 2's ceiling `e(M)\le\max(M)` is **always exactly attainable**
  within the natural cut budget (`K-1` cuts for a `K`-element multiset), never merely
  approached. This is the most consequential new fact this round: it is a **proved** (not
  numerically-observed) structural obstruction ruling out an entire class of future attempts
  at this file's open Step 4 (any argument hoping the residual stays strictly below its
  ceiling within budget), and correctly redirects future work toward a genuine joint
  budget-tradeoff argument. Fully general, proved by clean induction using only Lemma P.

These three facts, together with the already-certified Fact 1/Fact 2 (`lemmas/dominant-
extraction.md`), form a small reusable toolkit for bounding `e` of merged/modified sorted
multisets — potentially useful to any sibling approach reasoning about how `e` changes under
insertion, extraction, or cut-budget-limited modification of a multiset (e.g.
`potential-weighting-upper-bound`'s D/M policy search, or `concavity-minimax-duality`'s
monovariant-potential search, both of which manipulate active multisets under similar
operations).

**New this round (round 5), fully proved and general-purpose, stated in full in §5.3 Steps
3.1–3.6 above — candidate for a new certified lemma file, e.g.
`lemmas/superincreasing-no-early-zero.md`:**
- **Superincreasing No-Early-Zero Lemma.** Let `a_1>a_2>\dots>a_k>0` be strictly
  superincreasing (`a_i>a_{i+1}+\dots+a_k` for every `i<k`). Then for every legal sequence of
  `t<k` D/M operations (as defined in `lemmas/dm-operation-reformulation.md`) starting from
  `\{a_1,\dots,a_k\}`, the resulting active multiset (which has exactly `k-t\ge1` elements)
  satisfies `e>0` strictly; equivalently, no D/M sequence of length `<k` ever reaches `e=0`.
  Proved via three short, fully general, elementary lemmas: (3.1) a superincreasing sequence
  admits no vanishing `\{+1,-1\}`-signed subset sum (classical, proved from scratch, 5 lines);
  (3.2) a "token invariant," proved by induction on the number of D/M operations performed, that
  every active value at every point is a signed sum over a nonempty subset of original indices,
  with these index sets always pairwise disjoint across simultaneously-active tokens; (3.3) a
  corollary that active tokens are always pairwise distinct and strictly positive; (3.4) a
  strict alternating sum of distinct positive reals is always `>0`. This is fully general — no
  reference to this problem's specific numbers, cuts, or dyadic structure anywhere in the
  statement or proof — and directly reusable by any approach needing a "no early cancellation"
  obstruction for a D/M-style (or any subtract-and-remove) operation sequence on a
  superincreasing base sequence. **Independently computer-verified this round** by exhaustive
  (not sampled) exact-integer state-graph enumeration: for `m=1..6` applied to the dyadic
  `D_m=(2^m,\dots,2,1)` (`k=m+1` up to `7`, `3117` states enumerated at the largest case, zero
  violations of distinctness/positivity/nonzero-`e` among ALL reachable states, not just the
  minimizing path), and separately on `25` fresh random strictly superincreasing integer
  sequences of sizes 3–5 (each exhaustively enumerated within its own budget, zero violations).
  **Caveat on use, carried over honestly:** this lemma is purely about the *D/M-operation
  formalism*; using it to conclude a bound on the *true physical* strategy space for this
  problem's lower-bound direction additionally requires `lemmas/dm-completeness-partial.md`'s
  conditional `g=h` result (the pre-existing "all-cycles" caveat, unaffected by this lemma).

### 5.4 — round 7: full proof of Steps 1–2 and a new general Cross-Type Cycle Infeasibility
Lemma resolving Step 3 for all "shallow" cycles (bypasses `lemmas/dm-completeness-partial.md`
entirely — a genuinely different, self-contained route)

**Motivation (unchanged from the round-6 skeleton).** §5.3 proves the D/M-*sequence*-restricted
bound unconditionally. The only remaining gap to the TRUE physical lower bound `g(D_m,m)\ge
e_m\cdot S(D_m)` is the "all-cycles" case of `lemmas/dm-completeness-partial.md`. This section
targets only the specific family `A=D_m` (indeed, works for *any* strictly superincreasing base
sequence), using the guaranteed structure of superincreasing sequences as leverage the general
lemma cannot assume.

**Setting up the precise combinatorial object.** By `lemmas/dm-completeness-partial.md`'s own
characterization (Step 8.2–8.3 there), at the true global minimizer `FINAL`, every genuine cut
is, by the certified Vertex Lemma's joint-optimum Corollary, individually a **self-bisection**,
a **tie to an untouched original**, or a **tie to a value produced by exactly one other cut**
(the last case is the only one that can create a dependency edge — self-bisections and
ties-to-originals have no outgoing dependency, hence are always immediately peelable). Define
the **dependency graph** on the genuine cuts exactly as in that lemma: an edge `c\to c'` when
`c`'s tying output equals a value produced by `c'`. Since every node has out-degree `\le1`,
the *only* configuration blocking every peel is a nonempty union of directed cycles. Fix one
such cycle, of length `L`, on cuts `c_1,\dots,c_L` (indices mod `L`, relabelled — always
possible, since a directed cycle graph has an intrinsic cyclic traversal order — so that the
dependency edges are exactly `c_i\to c_{i+1}`).

Say cut `c_i` acts on a currently-existing piece of value `b_i`, splitting it into two output
values `(u_i,\,b_i-u_i)`, `0<u_i<b_i`, where `u_i` denotes whichever of the two outputs is the
one required (by the cyclic dependency) to equal a value produced by `c_{i+1}`. Write
`v_i:=b_i-u_i` for the *other* output of `c_i` (its "surviving" contribution, not itself
required by the cycle to tie anything — though a *different*, non-cyclic part of the strategy
could coincidentally also tie it; that does not affect the argument below, which only uses the
`L` cyclic equations themselves).

**Two natural sub-families, both now fully resolved:**

**(A) Uniform "shared-value" family (generalizes Step 2 from `L=2` to every `L\ge2`).**
Here every `u_i` is required to equal the *same* target value `t` for a common tying parameter
`t` — i.e. `L` distinct original pieces `b_1,\dots,b_L` are each cut once at the identical value
`t`. (This is exactly Step 2's construction when `L=2`.)

*Proof (Step 2, generalized).* By Lemma P, the `L` copies of `t` created by the `L` cuts pair
off: if `L` is even, all `L` copies cancel in `L/2` disjoint pairs, leaving only the `L`
"surviving" values `b_1-t,\dots,b_L-t`; if `L` is odd, `L-1` of the copies cancel in `(L-1)/2`
pairs, leaving exactly one surviving copy of `t` itself alongside `b_1-t,\dots,b_L-t`. Either
way, by the certified Vertex Lemma (applied to the single free parameter `t`, holding every
other piece — the untouched originals of `D_m`, in particular the piece `a_\ell` guaranteed to
exist and remain untouched by Step 1 below — fixed), the resulting value, as a function of `t`
alone on its domain, is **piecewise-linear**, with breakpoints exactly where some `b_i-t` (or
the leftover `t`, if `L` odd) crosses another current value, in particular where it crosses the
guaranteed-untouched `a_\ell`. A continuous piecewise-linear function on a closed interval
attains its minimum at a breakpoint or a domain endpoint (Vertex Lemma, part (b)). Hence the
minimum over `t` is *always* attained either (a) at a breakpoint tying `a_\ell` — which converts
that specific cut from a cross-tie into a tie-to-an-untouched-original, giving it out-degree `0`
and breaking the cycle at that node — or (b) at a domain endpoint (`t\to0` or `t\to\min_i b_i`,
a degenerate/fewer-genuine-cuts limit, likewise peelable, since it corresponds to a strictly
smaller/degenerate configuration). **A genuinely inescapable interior shared-value cycle
optimum therefore never occurs**, for any `L\ge2`, whenever an untouched original is available
— which Step 1 guarantees always holds for `D_m` in the tight regime `k=m+1`. This fully closes
family (A) for every `L`.

**(B) Cross-type cyclic family (the genuinely new case for `L\ge3`; the `L=2` version of this
family is vacuous/degenerate, see the remark after the proof).** Here the dependency is a
genuine cyclic *chain*: `u_i = v_{i+1} = b_{i+1}-u_{i+1}` for every `i=1,\dots,L` (indices mod
`L`), i.e. cut `i`'s tying output equals cut `(i+1)`'s *other*, surviving output — not a shared
constant, but a chain of *L* linear relations among the `L` unknowns `u_1,\dots,u_L`, one
relation per cyclic edge:
```
u_i + u_{i+1} = b_{i+1},   i=1,\dots,L  (indices mod L).
```

**Cross-Type Cycle Infeasibility Lemma.** Let `b_1,\dots,b_L` (`L\ge3`) be `L` *distinct*
pieces, each equal to one of the original values of a strictly superincreasing sequence (in
particular, `L` distinct originals of `D_m`). Then the system above has **no solution with
every `u_i\in(0,b_i)`** — i.e. no choice of cut positions realizes this exact cross-type
`L`-cycle. Consequently, together with (A), **every "shallow" cross-tie cycle (built from
distinct, once-cut original pieces, of any length `L\ge2`) is either infeasible (`L\ge3`,
cross-type) or never the actual minimizer (any `L\ge2`, shared-value type) for a strictly
superincreasing base sequence.**

*Proof.* Suppose, for contradiction, a solution exists with every `u_i\in(0,b_i)`. Summing all
`L` equations: `\sum_{i=1}^L(u_i+u_{i+1}) = \sum_{i=1}^L b_{i+1} = \sum_{i=1}^L b_i =: S`. The
left side counts each `u_i` exactly twice (once as the `i`-th term, once as the `(i+1)`-th term
of the previous equation), so `\sum_{i=1}^L(u_i+u_{i+1}) = 2\sum_i u_i`. Hence
`\sum_{i=1}^L u_i = S/2`. Relabel the cyclic indices (always possible, by rotating which piece
is called "`1`") so that `b_1 = M := \max_i b_i`. The equation with index `i=L` (i.e.
`u_L+u_1=b_1`) then reads `u_L+u_1 = M`. Subtracting this single equation from the total sum
identity:
```
u_2+u_3+\dots+u_{L-1} = \Big(\sum_{i=1}^L u_i\Big) - (u_L+u_1) = S/2 - M.
```
Since `b_1,\dots,b_L` are `L` distinct terms of a strictly superincreasing sequence and `M` is
the largest of them, the **superincreasing subset-dominance fact** (identical computation to
Step 1 of the certified `lemmas/superincreasing-no-early-zero.md`: if `i_0` is the smallest
original index among the `L` chosen — the one realizing `M` — then every other chosen value has
strictly larger index, hence `M > \sum_{\text{other chosen}} (\text{value})`, by the defining
superincreasing inequality applied at `i_0`) gives `M > S - M`, i.e. `S/2 < M`, i.e.
`S/2-M<0`. So `u_2+u_3+\dots+u_{L-1} < 0` — a sum of `L-2\ge1` (since `L\ge3`) terms, each of
which was assumed `>0` (a valid cut position `u_i\in(0,b_i)` in particular requires `u_i>0`).
A sum of one or more strictly positive reals cannot be strictly negative — contradiction. Hence
no feasible solution exists. `\blacksquare`

(Note the argument needs no case split on the parity of `L`, and does not require first
determining whether the linear system is consistent or has a unique/family of solutions — the
two derived facts, `\sum u_i=S/2` and `u_L+u_1=M`, are *necessary linear consequences* of any
hypothetical solution, and they alone already force the contradiction. The case `L=2` is
excluded exactly because then `u_2+\dots+u_{L-1}` is an empty sum, `=0`, which is *not*
contradicted by being `<0`; this is precisely why the shared-value family (A) — the genuine
`L=2` case — needed the separate, more delicate breakpoint argument instead of this direct
contradiction.)

**Verification (bounded, exact-Fraction/symbolic computation).** I independently re-verified
this by solving the cyclic linear system exactly (via `sympy`, exact arithmetic, small bounded
instances only) for `L=3,4,5` on `D_2=(4,2,1)`, `D_3=(8,4,2,1)`, `D_4=(16,8,4,2,1)`, over `20-30`
random choices of `L`-subsets and random cyclic orderings each: for odd `L` (`3,5`) the system
always has a *unique* solution, and in every one of `60` trials it violates `u_i\in(0,b_i)` for
some `i` (matching the proof: the specific violated index is always among the "remaining" `L-2`
positions); for even `L=4`, the system was *inconsistent* (no solution at all) in every one of
`20` trials — consistent with (and explained by) the same dominance fact, since consistency for
even `L` requires a specific vanishing signed subset sum of the chosen originals (an alternating
combination of all `L` chosen values equal to `0`), impossible by the classical no-vanishing-
signed-subset-sum fact already certified as Step 1 of `lemmas/superincreasing-no-early-zero.md`.
Zero counterexamples found; matches the proof exactly, including *why* even and odd `L` fail for
what looks like different reasons (inconsistency vs. infeasibility) — both are in fact
consequences of the single dominance/no-vanishing-sum fact.

**Step 1 (Guaranteed-Untouched-Original Lemma — proved in full).** Fix `A=D_m` (`k=m+1`
pieces) and any physical strategy using `\le m` cuts. Each cut targets some currently-existing
piece, which is either an original piece of `A` or the output of an earlier cut on the *same
branch*; following this parentage chain backward, every cut traces to a unique **root**
original piece of `A` (induction on the depth of the cut-forest: the root of a cut on an
original is that original itself; the root of a cut on a produced piece is the root of the cut
that produced it). Hence the set of distinct roots touched by the whole strategy has size
`\le m` (each of the `\le m` cuts contributes at most one new root to this set — a cut can only
ever *introduce* a new root if it acts on a not-yet-touched original; a cut on an already-cut
branch's output contributes no new root). Since `|A|=k=m+1>m`, **at least one original piece of
`D_m` is always left completely untouched** by any `\le m`-cut strategy. `\blacksquare`

**Step 2 (Base-case Cycle-Breaking Lemma — proved in full, and generalized to family (A) above
for every `L\ge2`).** See the proof of family (A) above, which specializes to exactly Step 2's
original `L=2` statement (two distinct original pieces tied at a shared value `t`) and
additionally covers every larger shared-value family at no extra cost.

**Step 3 — resolved for shallow cycles, honest remaining gap for deep/mixed cycles.** Combining
families (A) and (B): **every all-cycles configuration built entirely from distinct, once-cut
original pieces of `D_m`** — whether a uniform shared-value tie of any length `L\ge2`, or a
uniform cross-type chain of any length `L\ge3` — is now accounted for: family (A) is shown to
never be the actual minimizer (always dominated by a breakpoint escape to the guaranteed
untouched piece from Step 1), and family (B) is shown to be **physically infeasible** (no valid
cut positions realize it at all, for any `L\ge3`). This is a substantial, fully general new
result (Steps 1–2 fully rigorous; the new Cross-Type Cycle Infeasibility Lemma is a genuinely
new theorem, general-purpose for any strictly superincreasing base sequence, not just `D_m`).

**Honest remaining gap (precisely re-isolated, not closed this round).** The dependency-graph
formalism of `lemmas/dm-completeness-partial.md` allows, in full generality, a cycle whose
participating pieces `b_i` are not all *original*: some `b_i` could itself be a **derived**
value — the surviving output `v_j` of an earlier, non-cyclic (hence already peelable/resolved)
tie elsewhere in the same strategy, feeding into this cycle as one of its `b_i`'s. Such a `b_i`
is, by the token invariant of `lemmas/superincreasing-no-early-zero.md` (applied to the
resolvable prefix that produced it), a **signed subset sum** `\sum_{j\in T_i}\varepsilon_j a_j`
over some subset `T_i` of original indices (with the `T_i`'s pairwise disjoint across the
different cycle participants, by the same invariant's disjointness property) — and such a
signed sum need **not** retain the superincreasing "dominance" property (`\max_i b_i > \sum_{j
\ne i}b_j`) that both the (A) and (B) arguments crucially use, because cancellation inside the
signed sum can make a `b_i` built from a *large*-index-containing set small, breaking the clean
comparison. **I checked this concretely and confirmed the natural fix fails, rather than
merely asserting it might:** letting `i^*` be the smallest original index appearing in any of
the `T_i`'s (so `a_{i^*}` is the "most significant" original touched by the whole cycle), the
best bound obtainable from the reverse triangle inequality plus disjointness is
`|b_{i_0}|\ge a_{i^*}-\sum_{l>i^*}a_l` (where `i_0` is the cycle-participant whose `T_{i_0}`
contains `i^*`) and `\sum_{j\ne i_0}|b_j|\le\sum_{l>i^*}a_l` (a crude but valid over-estimate,
since all other `T_j`'s are disjoint subsets of `\{l:l>i^*\}`) — so the needed dominance
`|b_{i_0}|>\sum_{j\ne i_0}|b_j|` would follow from `a_{i^*}-\sum_{l>i^*}a_l>\sum_{l>i^*}a_l`,
i.e. `a_{i^*}>2\sum_{l>i^*}a_l`. For `D_m` specifically, `\sum_{l>i^*}a_l=a_{i^*}-1` **exactly**
(the tail of powers of `2` below `a_{i^*}=2^j` sums to `2^j-1`), so the needed inequality becomes
`a_{i^*}>2(a_{i^*}-1)`, i.e. `a_{i^*}<2`, which is **false** for every original piece except the
smallest (`a_{i^*}=1`). **This crude extension attempt genuinely fails** (not merely "not yet
tried") — a sharper argument, if one exists, would need to exploit more than the raw
triangle-inequality bound (e.g. the actual sign pattern of the token invariant, not just its
absolute-value bound), and is left open for a future round. Likewise, cycles that **mix**
shared-value-type and cross-type edges within a single cycle (rather than being uniformly one
type) are not analyzed here. **What is now precisely established:** the all-cycles caveat of
`lemmas/dm-completeness-partial.md`, as it could apply to `D_m`, is narrowed from "any cyclic
tie-dependency structure whatsoever" down to "a cycle involving at least one derived
(non-original) participant, or a mixture of tie-types within one cycle" — a substantially
smaller residual target than before this round, though still open.

**Cases covered / not covered, summarized:**
- Any all-cycles configuration where every cycle-participant is a distinct, once-cut, still-
  untouched-elsewhere-in-the-strategy *original* piece of `D_m`: **fully resolved** (dominated,
  `L=2` or shared-value any `L`; infeasible, cross-type `L\ge3`).
- A cycle with at least one derived (non-original) participant, or with mixed edge types: **open**,
  narrower than the pre-round-7 gap, with a concrete demonstration of why the natural extension
  of this round's dominance argument does not work.

## §5.5 — round 8: FULL proof of the `\#X` cross-type-edge parity dichotomy, closing the entire
all-cycles caveat

**(round 8 outline note, superseded below.)** The round-8 outline proposed the `\#X` (number of
cross-type edges around a cycle) parity dichotomy as a "cheap kill" reducing the residual
all-cycles gap to four buckets, three of which it sketched (not proved) and left `\#X\ge3` odd as
"the one remaining hard core." The round-8 outline-reviewer independently confirmed the mechanism
(bounded `sympy` check, `L\le5`, all `2^L` edge patterns) but flagged two precise gaps in the
sketch: (Gap 1) the `\#X\ge2`-even argument's disjointness-of-token-supports claim outran the
literal scope of the certified `superincreasing-no-early-zero.md` invariant (I1), which is stated
only for tokens *simultaneously active in one linear D/M trajectory*, not for arbitrary cycle
participants; (Gap 2) the `\#X=1` "this forces a self-bisection, hence peelable" claim needed its
logical chain (forced value `\to` vacuous cycle) spelled out explicitly. **Both gaps are now
closed below (§5.5.1 fixes Gap 1, §5.5.3 fixes Gap 2), and — going beyond the outline's own
scope — the `\#X\ge3` odd case is also FULLY CLOSED (§5.5.5), for every participant type
(original or derived), completing the resolution of the entire all-cycles caveat (§5.5.6).**

### 5.5.0 — Setup: the general mixed `S`/`X` cyclic system

Fix a cyclic tie-dependency component (as defined and constructed in `lemmas/dm-completeness-
partial.md`, Steps 8.2–8.3) of length `L\ge2` on cuts `c_1,\dots,c_L` (cyclic index, mod `L`),
where `c_i` acts on a currently-existing piece of value `b_i`, and `u_i\in(0,b_i)` denotes `c_i`'s
own "tying" output (the one required, by the cycle's dependency structure, to equal a value
associated with `c_{i+1}`). Since cut `c_{i+1}` produces exactly two values — its own tying output
`u_{i+1}` and its other ("surviving") output `v_{i+1}:=b_{i+1}-u_{i+1}` — and `u_i` must equal
*one* of these two (there is no third possibility, since `c_{i+1}` produces only these two
values), every cyclic edge `i\to i+1` is of exactly one of two types:
- **`S`** (shared-value): `u_i=u_{i+1}`;
- **`X`** (cross-type): `u_i=v_{i+1}=b_{i+1}-u_{i+1}`, i.e. `u_i+u_{i+1}=b_{i+1}`.

Write `\#X\in\{0,1,\dots,L\}` for the number of `X`-type edges. This is a complete, exhaustive
classification of every cyclic tie-dependency structure (no third edge type exists, by the
two-valued-output argument above), so a full case analysis on `\#X\in\{0\},\{1\},\{\ge2\text{
even}\},\{\ge3\text{ odd}\}` (an exhaustive, disjoint partition of `\{0,1,\dots,L\}`) covers
**every** possible cycle.

**General closing-equation fact (elementary, proved here in full).** Writing each edge's relation
uniformly as `u_{i+1}=\varepsilon_i u_i+c_i` with `\varepsilon_i=-1,\,c_i=b_{i+1}` if edge `i` is
`X`, and `\varepsilon_i=+1,\,c_i=0` if edge `i` is `S`, unrolling the recursion once around the
cycle (`u_{L+1}=u_1`) gives, by direct induction on `k` (`u_{k+1}=(\prod_{i=1}^k\varepsilon_i)u_1+
\sum_{j=1}^k c_j\prod_{i=j+1}^k\varepsilon_i`, verified by substituting the recursion at each step)
the scalar identity
```
u_1\Big(1-\textstyle\prod_{i=1}^L\varepsilon_i\Big) = \textstyle\sum_{j:\,\text{edge }j\text{ is }X} b_{j+1}\prod_{i=j+1}^L\varepsilon_i =: C.
```
Since `\prod_{i=1}^L\varepsilon_i=(-1)^{\#X}` (each `X`-edge contributes a factor `-1`), this reads:
`u_1\cdot 2 = C` if `\#X` is odd (giving a **unique** solution `u_1=C/2`, hence by the forward
recursion a unique full solution `(u_1,\dots,u_L)`, since every step of the recursion is an
invertible affine map); or `0=C` (a **closing identity independent of `u_1`**, needed for
consistency; if it holds, `u_1` is a free parameter of a genuine 1-parameter solution family) if
`\#X` is even. This matches — and is here proved directly from the recursion, not merely
`sympy`-checked — the outline-reviewer's independent confirmation.

**`X`-successor pieces are exactly the "block leaders."** Group the `L` cyclic nodes into
maximal runs joined by `S`-edges ("blocks"); since `\#X\ge1` separates the cycle into exactly
`\#X=:q` such blocks (for `\#X=0` there is one giant block, i.e. family (A) below), each block
`B_s` (`s=1,\dots,q`, cyclically ordered) is a nonempty run of nodes all forced, by direct
chaining of the `S`-equalities within the block (an elementary transitivity argument: adjacent
`S`-joined nodes are literally equal, so by induction on run length every node in one run shares
one common value), to one common value `t_s`. Write `\beta_s:=` the piece `b` attached to the
**first node of block `B_{s+1}`** (equivalently: the piece appearing as `b_{j+1}` for the `X`-edge
`j` immediately preceding block `s+1`) — these `q` values `\beta_1,\dots,\beta_q` are exactly the
"`X`-successor pieces" appearing in `C` above, and are a subset of size `q` of the original
`b_1,\dots,b_L`.

**Inherited caveat (carried from round 6/7, not re-derived here, and unaffected by this round's
work).** The "`S`/`X` edge" formalization used throughout §5.4–§5.5 (`L` cuts each producing a
single designated tying value `u_i`, related to its cyclic neighbor by equality or by summing to
a piece) is a slightly more concrete, hands-on restatement of the abstract tie-dependency-graph
edges of `lemmas/dm-completeness-partial.md`; this restatement has already passed review twice
(rounds 6–7) and is used here exactly as before, not re-justified from scratch again.

### 5.5.1 — Cycle Common-State Lemma (closes Gap 1: the disjointness fix)

**Claim.** For any single cyclic tie-dependency component `\Gamma=(c_1,\dots,c_L)` of the true
global minimizer's dependency graph, its `L` input pieces `b_1,\dots,b_L` are **simultaneously
active tokens of one common, legitimate D/M-reachable state** — hence the certified invariants
(I1) (pairwise-disjoint token supports) and (I2) (exact signed-subset-sum representation) of
`lemmas/superincreasing-no-early-zero.md` apply to them **directly, with no extension or
modification of that lemma's stated scope.**

**Proof.** By hypothesis (the round-7 framing this file has used throughout), every participant
`b_i` is either (a) an as-yet-untouched original piece of `D_m`, or (b) "the surviving output of
an earlier, **non-cyclic** (hence already peelable/resolved) tie elsewhere in the same strategy" —
i.e. produced entirely by cuts that are *not* part of any cyclic dependency component. Call the
union of all such non-cyclic cuts (every self-bisection, every tie-to-untouched-original, and
every cut in the acyclic "DAG part" of the dependency graph) the **acyclic remainder**. By the
already-certified peeling induction of `lemmas/dm-completeness-partial.md` (Steps 8.3–8.4: "a cut
[not blocked by an in-cycle dependency] can always be safely peeled... by strong induction on the
number of genuine cuts"), the entire acyclic remainder is realizable, in some valid order, as a
genuine legal partial D/M operation sequence starting from `D_m` — this is exactly the certified
content of that lemma; nothing new is asserted about it here.

Apply that valid partial sequence to `D_m`, in full, but stop **before** touching any cut of
`\Gamma` (or of any other cyclic component). This is possible because `\Gamma`'s cuts are, by
definition, not part of the acyclic remainder, so realizing the acyclic remainder never requires
performing any of them. At the resulting state:
- every untouched original of `D_m` is present (case (a) participants: unaffected by the acyclic
  remainder, since by hypothesis `\Gamma` never touches them elsewhere);
- every case-(b) participant `b_i` **is present**, since it is by hypothesis produced entirely by
  acyclic-remainder cuts, all of which have now been performed, and it has not yet been consumed
  (consuming it would require `c_i\in\Gamma`, not yet applied).

Hence all `L` of `\Gamma`'s participants `b_1,\dots,b_L` are simultaneously active tokens of this
one common state — a state reached from `D_m` via finitely many legal D/M operations, exactly the
setting (I1)/(I2) are certified for. `\blacksquare`

**Remark (an honestly-flagged, narrower residual, addressed and closed here too).** The
hypothesis "(b) produced by *non-cyclic* cuts" (already the file's own round-7 framing, not a new
restriction introduced here) excludes only one further, more exotic possibility: a participant
`b_i` descended from the output of a cut belonging to a **different** cyclic component `\Gamma'
\ne\Gamma`. This is handled by a standard graph fact, not by assumption: contract each cyclic
component of the dependency graph to a single point (its "condensation"). A condensation of any
directed graph is always acyclic — if it contained a cycle among components, those components
would be mutually reachable from one another, hence would all lie in one common strongly
connected component, contradicting their being separate, maximal cyclic components in the first
place. Consequently, among the finitely many cyclic components of the (finite, `\le m`-cut)
dependency graph, at least one, `\Gamma_0`, is **minimal** in this condensation order (no other
component's cut feeds any of `\Gamma_0`'s participants) — i.e. `\Gamma_0`'s participants satisfy
hypothesis (a)/(b) exactly as stated, with "non-cyclic" now literally meaning "not part of *any*
cyclic component." Take `\Gamma:=\Gamma_0` throughout this section: since (per the already-
established "Watch out" note, restated here) resolving or de-optimizing **any one** cyclic
component already contradicts the joint minimality of the whole configuration, it suffices to
carry out the argument for this one, structurally-simplest component — which the Lemma above
applies to without qualification.

### 5.5.2 — `\#X=0`: no new work

Already fully closed by the certified **Shared-Value Cycle-Breaking Lemma** (`lemmas/shallow-
cycle-resolution.md`, part 2): this argument uses only the Vertex Lemma (a single free parameter
`t`, every other piece — including the Step-1 guaranteed-untouched original — held fixed) and
never uses any dominance or originality property of the tied pieces `b_1,\dots,b_L` themselves.
Hence it applies verbatim to **derived** participants too (a fact not previously stated, but
immediate from re-inspection of that proof) — no new work needed for this bucket, for any
participant type.

### 5.5.3 — `\#X=1`: Lone-`X`-Edge Vacuity Lemma (closes Gap 2: the explicit logical chain)

**Claim.** No genuine cyclic tie-dependency component ever has `\#X=1`. (Equivalently: any
attempted cyclic pattern with exactly one cross-type edge is not a real instance of the
all-cycles obstruction at all.)

**Proof, as an explicit chain of steps (per the reviewer's request).**

*Step 1 (solve the system).* With `\#X=1`, say the sole `X`-edge is edge `j_0` (connecting node
`j_0` to `j_0+1`), all other `L-1` edges being `S`. By the block-chaining fact of §5.5.0, the `S`-
edges force every node's tying value to a single common value `t` (there is exactly `q=1` block,
consisting of all `L` nodes, since only one edge — the `X`-edge — is not `S`; equivalently, tracing
`S`-equalities from node `j_0+1` all the way around the cycle back to node `j_0`, using every edge
except the single `X`-edge, gives `u_{j_0+1}=u_{j_0+2}=\dots=u_{j_0}=:t`). Substituting into the
one `X`-edge equation `u_{j_0}+u_{j_0+1}=b_{j_0+1}` gives `2t=b_{j_0+1}`, i.e. `t=b_{j_0+1}/2`
**exactly**.

*Step 2 (identify the forced cut as a self-bisection).* Node `j_0+1`'s cut, `c_{j_0+1}`, acts on
piece `b_{j_0+1}` and produces two outputs, `u_{j_0+1}` and `v_{j_0+1}=b_{j_0+1}-u_{j_0+1}`. Since
`u_{j_0+1}=t=b_{j_0+1}/2` (Step 1), also `v_{j_0+1}=b_{j_0+1}-b_{j_0+1}/2=b_{j_0+1}/2=t`. So both of
`c_{j_0+1}`'s outputs equal `t` — i.e. `c_{j_0+1}` splits its piece exactly in half. By the
certified Vertex Lemma's classification (`lemmas/vertex-lemma.md`), a cut whose two outputs are
numerically equal **is**, by definition, a self-bisection (a "D-type" vertex condition, `t=\ell/2`)
— not a tie to any other piece.

*Step 3 (self-bisections have out-degree `0`, by the very construction of the dependency graph).*
The dependency graph of `lemmas/dm-completeness-partial.md` is built precisely so that a
self-bisecting cut has **no outgoing edge**: its two output values are pinned relative to *each
other only* (`t=\ell/2` is a purely local vertex condition depending on no other piece's value),
so it has no unresolved external tying requirement that could be the source of a dependency edge.
This is stated explicitly in that lemma's own Step 8.2 ("self-bisections... have no outgoing
edge") and is not being re-derived here, only invoked.

*Step 4 (contradiction with the hypothesis that `c_{j_0+1}\in\Gamma`).* By hypothesis, `c_{j_0+1}`
is one of the `L` nodes of the assumed directed cycle `\Gamma` — and every node of a nonempty
directed cycle has out-degree **exactly `1`** *within the cycle* (its own outgoing edge to the
next cycle member; this is simply what it means for a node to lie on a directed cycle). But Step 3
shows `c_{j_0+1}` has out-degree `0`. These two facts directly contradict each other.

*Step 5 (conclusion: the assumed configuration never occurs).* Hence no genuine cyclic component
can exhibit the `\#X=1` pattern: whenever the closing-equation arithmetic of a purported `\#X=1`
cycle is carried out, it *always* forces node `j_0+1` to be numerically a self-bisection (Steps
1–2), which is *structurally* incompatible (Steps 3–4) with `j_0+1` genuinely belonging to an
unresolved dependency cycle. So a `\#X=1` configuration is never a real obstruction to peeling: if
a strategy's tie-dependencies happen to solve to this numeric pattern, node `j_0+1` is in truth an
ordinary self-bisection (out-degree `0`, hence immediately peelable, exactly as `lemmas/dm-
completeness-partial.md`'s own peeling induction already handles), and once it is peeled the
remaining `L-1` cuts' dependencies resolve against the now-fixed value `t=b_{j_0+1}/2`, forming a
genuinely acyclic chain (each of the remaining cuts ties either to the fixed peeled value or to the
next cut down the chain, in a strict linear order) — which the *same* certified peeling induction
already handles by strong induction on the number of genuine cuts. `\blacksquare`

*(Verification: confirmed on 42 independently-generated random instances, `L=2,\dots,7`, mixed
original/derived pieces, `\#X=1` exactly — every one gives all-`u_i` equal and `2t=` the piece at
the block leader, exactly as predicted; no case failed to match.)*

### 5.5.4 — `\#X\ge2` even: Even-`\#X` Infeasibility Lemma (applies the §5.5.1 Gap-1 fix, and
closes gap (b) for this bucket)

**Claim.** No cyclic pattern with `\#X\ge2` even is ever physically realizable — i.e. the system
of §5.5.0 has **no solution** with every `u_i\in(0,b_i)` — for *any* mix of original and derived
participants (subject only to the Cycle Common-State Lemma's hypothesis, §5.5.1, which always
holds for the minimal cyclic component `\Gamma_0`).

**Proof.** By §5.5.0, feasibility for even `\#X` requires the closing identity `C=0`, where
`C=\sum_{j:\,\text{edge }j\text{ is }X} b_{j+1}\,\sigma_j` (`\sigma_j:=\prod_{i=j+1}^L
\varepsilon_i\in\{\pm1\}`), and (§5.5.0) the terms `b_{j+1}` appearing are exactly the `q=\#X`
distinct block-leader pieces `\beta_1,\dots,\beta_q` (distinct because they are attached to `q`
distinct cyclic positions), so `C=\sum_{s=1}^q\sigma^{(s)}\beta_s` for definite signs
`\sigma^{(s)}\in\{\pm1\}`.

By the Cycle Common-State Lemma (§5.5.1), each `\beta_s` (being one of `\Gamma_0`'s `L` input
pieces `b_1,\dots,b_L`) has a well-defined token `(S(\beta_s),\varepsilon(\beta_s))`, with
`S(\beta_1),\dots,S(\beta_q)` **pairwise disjoint** (a subset of the pairwise-disjoint
`S(b_1),\dots,S(b_L)` given by (I1)) and `\beta_s=\sum_{j\in S(\beta_s)}\varepsilon(\beta_s)(j)\,
a_j` exactly (I2). Substituting,
```
C = \sum_{s=1}^q \sigma^{(s)} \sum_{j\in S(\beta_s)} \varepsilon(\beta_s)(j)\, a_j
  = \sum_{j\,\in\,\bigsqcup_s S(\beta_s)} \big[\sigma^{(s(j))}\varepsilon(\beta_{s(j)})(j)\big]\, a_j,
```
where `s(j)` denotes the (unique, by disjointness) block whose support contains `j`. Since each
bracketed coefficient is a product of two `\pm1` values, hence itself `\pm1`, and the supports are
pairwise disjoint (so no original index `j` is touched by two different `\beta_s`'s, hence no risk
of two contributions combining or cancelling at the same index), `C` is **exactly a signed subset
sum over original indices** in the sense of Step 1 of `lemmas/superincreasing-no-early-zero.md` —
nonempty, since `q\ge2>0` guarantees at least one nonempty `S(\beta_s)`. By that certified,
*exact* (not magnitude/dominance) fact, `C\ne0` always. This directly contradicts the requirement
`C=0` for feasibility. Hence no solution exists. `\blacksquare`

*(Verification: 300 independently-generated random trials — disjoint-support tokens built from
`D_5,D_6` by partitioning indices into `q\in\{2,3,4,5\}` groups with random `\pm1` signs (mimicking
genuinely derived participants), even `\#X\ge2` patterns — the full mixed linear system was
inconsistent (no solution at all) in every one of the 300 trials, matching the proof exactly.)*

### 5.5.5 — `\#X\ge3` odd: Generalized Cross-Type Domain-Violation Lemma (the previously-open
"hard core," now CLOSED for every participant type)

By the block-collapse fact (§5.5.0), any cyclic pattern with `\#X=q\ge3` odd reduces — after
collapsing each `S`-chained block to its common value `t_s` — to a **pure cross-type `q`-cycle**
on the `q` block-leader pieces `\beta_1,\dots,\beta_q`: `t_s+t_{s+1}=\beta_{s+1}` for
`s=1,\dots,q` (indices mod `q`), with the necessary (not necessarily sufficient, but sufficient
for our purposes) domain requirement `t_s\in(0,\beta_s)` for every `s` (a consequence of the full
domain requirement `u_i\in(0,b_i)` at the first node of each block; dropping the *other*, possibly
tighter, per-node constraints inside each block only makes infeasibility of this reduced system a
**stronger**, not weaker, conclusion for the original system — if the reduced system has no
solution meeting even this weaker necessary condition, the original certainly has none meeting the
full set of stronger conditions).

**Step A (explicit closed form for the reduced system, proved directly, not just checked).**
*Claim:* the (unique, since `q` is odd, §5.5.0) solution of the pure cross-type `q`-cycle is
```
t_s = \tfrac12\sum_{l=0}^{q-1}(-1)^l\,\beta_{s+l+1}\qquad(\text{indices mod }q).
```
*Proof it solves the system:* compute, for any `s`,
```
2t_s+2t_{s+1} = \sum_{l=0}^{q-1}(-1)^l\beta_{s+l+1} + \sum_{l=0}^{q-1}(-1)^l\beta_{s+l+2}.
```
Reindex the second sum by `l'=l+1` (`l'=1,\dots,q`): it becomes `\sum_{l'=1}^q(-1)^{l'-1}
\beta_{s+l'+1} = -\sum_{l'=1}^q(-1)^{l'}\beta_{s+l'+1}`. Subtracting this from the first sum, the
terms `l=1,\dots,q-1` (equivalently `l'=1,\dots,q-1`) appear identically in both and **cancel**,
leaving only the `l=0` term of the first sum and the (negated) `l'=q` term of the second:
```
2t_s+2t_{s+1} = \beta_{s+1} - \big[-(-1)^q\beta_{s+q+1}\big] = \beta_{s+1}+(-1)^q\beta_{s+1}
             = \beta_{s+1}+(-1)\beta_{s+1}\cdot(-1) \quad(\text{using }s+q+1\equiv s+1\!\!\mod q,\ q\text{ odd, so }(-1)^q=-1)
```
Concretely: `(-1)^q=-1` (q odd), so the bracketed term is `-(-1)(\beta_{s+1})=\beta_{s+1}`, giving
`2t_s+2t_{s+1}=\beta_{s+1}+\beta_{s+1}=2\beta_{s+1}`, i.e. `t_s+t_{s+1}=\beta_{s+1}` — exactly the
defining equation. Since uniqueness was already established in §5.5.0 (nonzero closing coefficient
`1-(-1)^q=2` when `q` is odd), this **is** the solution, not merely a solution. (Independently
verified by direct `sympy` solve on 69 random instances, `q\in\{3,5\}`, zero mismatches against this
closed form.)

**Step B (the sign-dominance argument — the new mechanism that closes this bucket for BOTH
original and derived participants).** By the Cycle Common-State Lemma (§5.5.1), the pieces
`\beta_1,\dots,\beta_q` have pairwise-disjoint original-index supports `S(\beta_1),\dots,
S(\beta_q)` and exact signed-sum representations (I1)/(I2). Let `i^*:=\min\big(\bigcup_s
S(\beta_s)\big)` — the smallest original index appearing in the union of all `q` supports — and
let `r_0` be the (unique) block with `i^*\in S(\beta_{r_0})`, with sign `\varepsilon(\beta_{r_0})
(i^*)=:\epsilon\in\{\pm1\}`.

Expanding the closed form via (I2), `2t_s=\sum_{l=0}^{q-1}(-1)^l\beta_{s+l+1}` is itself a signed
subset sum over `\bigcup_s S(\beta_s)` (every original index in the union appears exactly once,
since the supports are disjoint and every block `\beta_r` appears exactly once in the sum, as `l`
ranges bijectively over `0,\dots,q-1` and `s+l+1\!\!\mod q` ranges bijectively over all `q` block
indices). In particular, the coefficient of `a_{i^*}` in `2t_s` is `\tau_s:=(-1)^{l_0(s)}\epsilon`,
where `l_0(s):=(r_0-s-1)\bmod q` is the unique offset at which block `r_0` appears in `t_s`'s sum.
Write `R_s` for the sum of every *other* term in `2t_s`'s expansion (all indices in `\bigcup_s
S(\beta_s)\setminus\{i^*\}`, i.e. all indices strictly greater than `i^*` by minimality of `i^*`):
```
2t_s = \tau_s\,a_{i^*} + R_s,\qquad R_s = \sum_{j\in(\cup_sS(\beta_s))\setminus\{i^*\}} (\pm1)\,a_j.
```
By the strict superincreasing property, `a_{i^*} > \sum_{j=i^*+1}^k a_j \ge \sum_{j\in(\cup_s
S(\beta_s))\setminus\{i^*\}} a_j \ge |R_s|` (the middle inequality since `\cup_sS(\beta_s)
\setminus\{i^*\}\subseteq\{i^*+1,\dots,k\}`, and the last by the triangle inequality on the signed
sum `R_s`). Hence `|R_s|<a_{i^*}` **strictly**, for *every* `s` (the union `\cup_sS(\beta_s)` does
not depend on `s`, only the individual signs inside `R_s` do), so `2t_s` has the **same strict
sign as `\tau_s`**: `t_s>0` if `\tau_s=+1`, `t_s<0` if `\tau_s=-1`.

As `s` ranges over the `q` blocks (`s=1,\dots,q`, indices mod `q`), `l_0(s)=(r_0-s-1)\bmod q`
ranges bijectively over `\{0,1,\dots,q-1\}` (a fixed reindexing of a full residue system), so
`(-1)^{l_0(s)}` takes **both** values `+1` and `-1` as `s` varies — since `q\ge3`, the set
`\{0,\dots,q-1\}` contains at least one even and at least one odd element (indeed `\lceil q/2\rceil
\ge2` even values including `0`, and `\lfloor q/2\rfloor\ge1` odd value, since `q\ge3`). Hence
`\tau_s=(-1)^{l_0(s)}\epsilon` also takes both signs as `s` ranges over the blocks. **In
particular, there exists a specific block `s^*` with `\tau_{s^*}=-1`, giving `t_{s^*}<0` —
directly violating the domain requirement `t_{s^*}\in(0,\beta_{s^*})` (which requires `t_{s^*}>0`
in particular).** No solution of the reduced (hence, a fortiori, the original) system satisfies
every domain constraint. `\blacksquare`

**This argument requires no dominance/magnitude property of the `\beta_s`'s themselves** (unlike
the round-7 crude extension attempt, which needed `a_{i^*}>2\sum_{l>i^*}a_l` — false for `D_m`) —
it uses only (i) the disjointness of token supports (Cycle Common-State Lemma) and (ii) the
elementary superincreasing dominance of the single most-significant index `i^*` over the *entire*
union of supports, which is unconditionally true (strict superincreasing hypothesis) regardless of
how the `q` pieces are internally structured. **This is a strict generalization of, and supersedes,
the previously-certified Cross-Type Cycle Infeasibility Lemma**: specializing to the case where
every `\beta_s` is itself a single original (`S(\beta_s)=\{j_s\}`, a singleton, `\epsilon=+1`)
recovers that Lemma's exact conclusion (`M=a_{i^*}>S-M` forces infeasibility) as the special case
of this argument with trivial (singleton) tokens — but the new argument additionally, and for the
first time, handles **derived** `\beta_s`'s (genuine signed-sum tokens from earlier resolved ties)
with no extra hypothesis.

*(Verification, bounded exact computation: (1) the closed-form solution was independently
re-derived by `sympy` `solve()` on `q=3,5`, `69` trials, `0` mismatches. (2) The sign-prediction —
which specific block index `s^*` goes negative, computed purely from `i^*`, `r_0`, `\epsilon` — was
checked against the actual solved values on `220` trials of disjoint-support derived tokens over
`D_5,D_6,D_7,D_8` (partitioning indices into `q\in\{3,5\}` random groups with random signs): **every
one of the `220` trials had a negative `t_s` at exactly the predicted block, `0` mismatches.** (3) A
broader, mixed sweep (`3000` trials, `L=3,\dots,7`, every `\#X\in\{0,\dots,L\}`, random mixtures of
plain-original and disjoint-derived pieces) found feasible solutions **only** at `\#X=1` (`42`
instances, all confirmed to be the vacuous self-bisection pattern of §5.5.3) and **zero** feasible
instances at any other `\#X` value — an exhaustive-in-pattern-type, broad random check consistent
with (not a substitute for, but strongly corroborating) the four proofs above being jointly
exhaustive.)*

### 5.5.6 — Synthesis: the entire all-cycles caveat is closed

Combining §5.5.2–§5.5.5: for **every** possible value of `\#X` (an exhaustive partition of every
cyclic tie-dependency pattern, §5.5.0), one of the following holds:
- `\#X=0`: physically realizable, but **never the true joint minimizer** (dominated by a
  breakpoint escape to the guaranteed-untouched original of Step 1, §5.4);
- `\#X=1`: **not a genuine cycle at all** — always reduces to an ordinary, already-peelable
  self-bisection (§5.5.3);
- `\#X\ge2` even: **physically infeasible** — no choice of cut positions realizes it (§5.5.4);
- `\#X\ge3` odd: **physically infeasible** — the unique solution always violates a domain
  constraint (§5.5.5).

None of these four cases is proved only for "shallow," all-original-participant cycles: the Cycle
Common-State Lemma (§5.5.1) establishes that **every** cyclic component's participants (however
many are derived) are simultaneously active tokens of one common legal D/M state, so (I1)/(I2)
apply without modification in every one of §5.5.2–5.5.5's arguments. **Consequently, at the true
global minimizer `FINAL` of any `\le m`-cut strategy against `D_m` (or any strictly superincreasing
base sequence), the tie-dependency graph can never be a nonempty union of directed cycles** — every
candidate cyclic pattern is either not truly a cycle, infeasible outright, or (if feasible)
provably not the minimizer. This is *exactly* the sufficient condition stated in the certified
`lemmas/dm-completeness-partial.md` for `g(A,m)=h(A,m)` to hold unconditionally (not merely "the
condition holds whenever the unresolved cuts are not all cross-ties arranged in a closed cycle" —
we have now shown this holds **always**, for `A=D_m` and any `m`).

**Headline consequence.** Combining:
- `g(D_m,m)=h(D_m,m)` (now unconditional, by the above, via `lemmas/dm-completeness-partial.md`);
- `h(D_m,m)\ge e_m\cdot S(D_m)` (the certified **Superincreasing No-Early-Zero Lemma**, §5.3,
  unconditional for every `m`);

we obtain, for the **first time**, the fully unconditional TRUE PHYSICAL lower bound
```
g(D_m,m) \ge e_m\cdot S(D_m)\qquad\text{for every }m,
```
i.e. **against the dyadic construction `D_m`, no physical Xiang-Yu strategy using `\le m` cuts can
ever beat the target `e_m`** — closing the lower-bound direction of the theorem completely for
this specific family, for every `m`, with no remaining caveat. (Honest scope: this closes the
lower bound *for the dyadic construction specifically*; the theorem's full statement additionally
needs the upper-bound direction — the specific value `c(n)` is only pinned once Liu Bang's
*optimal* opening is shown to be at least as good as `D_m`, i.e. once the matching upper bound
`g(A,m)\le e_m\cdot S(A)` for *every* `A` — see the sibling `potential-weighting-upper-bound`'s Case
(ii) work, still open at general `m`. (Round 9 correction: general `n\ge4` is **not** a separate
open item beyond this — see the round-9 note atop "## Status" — Case (i)/(ii)'s joint strong
induction on `m` closes for every `n` at once the moment the sibling's aggregated lemma closes,
and the lower bound above already has no `n`-dependence/induction at all.) Section "Current
best" below restates this scope precisely.)

### 5.5.7 — Verification summary (bounded, exact computation, as required by CLAUDE.md)

All computations below used exact `sympy`/Python `Fraction`/integer arithmetic on small, explicitly
bounded instances (never an unbounded or fine-grid numeric search):
1. Block-reduction correctness: `69` random mixed `S`/`X` patterns (`q=\#X\in\{3,5\}` odd,
   `L=4,\dots,7`, bases `D_3`–`D_6`), confirming the block-leader values in the full `L`-node
   solved system exactly match the reduced `q`-node system's solution — `0` mismatches.
2. `\#X\ge3` odd, all-original participants: `152` trials, `0` feasible instances found (matching
   infeasibility).
3. `\#X\ge2` even, disjoint-support **derived** tokens: `300` trials, the full system was
   inconsistent (no solution) in every trial (matching `C\ne0`).
4. `\#X\ge3` odd, disjoint-support derived tokens: `310`+`220` trials (two independent runs, `q\in
   \{3,5\}`, bases `D_5`–`D_8`), `0` feasible instances; and in a further `220`-trial run the
   *specific* predicted negative block `s^*` (from `i^*,r_0,\epsilon`) matched the actual computed
   solution's negative entry in **every** trial (`0` mismatches).
5. `\#X=1`: `42`+`50` trials, all confirmed vacuous (forced self-bisection, `2t=` block-leader
   piece) — `0` mismatches with the predicted mechanism.
6. Broad mixed sweep: `3000` trials spanning every `\#X\in\{0,\dots,L\}`, `L=3,\dots,7`, random
   mixtures of plain and disjoint-derived pieces: feasible solutions found **only** at `\#X=1`
   (all vacuous), **zero** at any other `\#X` — consistent with, and a strong independent
   corroboration of, the four proofs of §5.5.2–5.5.5 being jointly exhaustive and correct.

(All scripts and raw output available for re-derivation; the written proofs above are
self-contained and do not depend on these checks for correctness — they are corroboration, not a
substitute for the algebraic arguments given.)

## Promotable lemmas (round 7 addition)

New this round, fully proved, general-purpose (stated for any strictly superincreasing base
sequence, not specific to `D_m`'s numbers), candidates for the reviewer to certify as a new
shared lemma (e.g. `lemmas/shallow-cycle-resolution.md`), extending
`lemmas/dm-completeness-partial.md`'s open "all-cycles" case:

- **Guaranteed-Untouched-Original Lemma.** For a strictly superincreasing sequence with
  `k=m+1` original pieces, any physical strategy using `\le m` cuts leaves at least one
  original piece completely untouched (pigeonhole on cut-forest roots — a one-paragraph, fully
  general, elementary proof, §5.4 Step 1 above).
- **Shared-Value Cycle-Breaking Lemma.** For a strictly superincreasing sequence with an
  untouched original piece available, no uniform "all `L` pieces tied at one shared value `t`"
  configuration (`L\ge2`) is ever the true minimizer of `e` — the minimum over `t` is always at
  a breakpoint tying the untouched piece, or a degenerate boundary (§5.4 family (A) above;
  strictly generalizes the previously-informal `L=2` "Base-case Cycle-Breaking Lemma").
- **Cross-Type Cycle Infeasibility Lemma.** For any `L\ge3` distinct terms `b_1,\dots,b_L` of a
  strictly superincreasing sequence, the cyclic linear system `u_i+u_{i+1}=b_{i+1}` (indices
  mod `L`) has no solution with every `u_i\in(0,b_i)` — proved by a 5-line sum-and-dominance
  argument (§5.4 family (B) above), reusable by any approach reasoning about cyclic tie
  structures on a superincreasing sequence. Independently spot-checked (bounded exact/symbolic
  computation, `L=3,4,5` on `D_2,D_3,D_4`, `100` total random trials, zero feasible cycles
  found, matching the proof's predicted failure mode — unique-but-infeasible for odd `L`,
  outright inconsistent for even `L` — exactly).

**Caveat, honestly carried:** these three lemmas together resolve the all-cycles caveat only
for "shallow" cycles (built entirely from distinct, once-cut, still-untouched original pieces).
A cycle with at least one *derived* (non-original) participant is not covered; the natural
crude extension of the Cross-Type Cycle Infeasibility Lemma's dominance argument to derived
tokens is shown (not just asserted) to fail for `D_m` specifically. Promoting the theorem's
lower bound to fully unconditional for `D_m` still requires closing this narrower residual gap.

## Promotable lemmas (round 8 addition)

New this round (§5.5 above), fully proved, general-purpose (stated for any strictly
superincreasing base sequence, not specific to `D_m`'s numbers), candidates for the reviewer to
certify as an extension to `lemmas/shallow-cycle-resolution.md` (or a new file, e.g.
`lemmas/all-cycles-resolution.md`), **closing the all-cycles caveat of
`lemmas/dm-completeness-partial.md` in full**:

- **Cycle Common-State Lemma** (§5.5.1). For a minimal cyclic tie-dependency component `\Gamma_0`
  of the global minimizer's dependency graph (minimal in the sense that none of its participants
  descend from another cyclic component — always exists, since the condensation of any directed
  graph by strongly-connected components is acyclic), all `L` of its input pieces are
  simultaneously active tokens of one common, legal D/M-reachable state — hence the certified
  invariants (I1)/(I2) of `lemmas/superincreasing-no-early-zero.md` apply directly, with no
  extension of that lemma's stated scope, giving pairwise-disjoint original-index token supports
  for `\Gamma_0`'s participants regardless of how many are derived. This is the fix for the
  precise gap the round-8 outline-reviewer flagged (the disjointness claim previously outran
  (I1)'s literal "simultaneously active in one trajectory" scope).
- **Block-Collapse Reduction Lemma** (§5.5.0, general closing-equation derivation + block
  argument). Any cyclic tie-dependency pattern of length `L` with `\#X` cross-type edges (`\#X`
  itself an exhaustive classification: every edge is either `S`, "shared value," or `X`,
  "cross type" — no third possibility) reduces, after collapsing each maximal `S`-chained block
  to its common value, to a pure cross-type `\#X`-cycle on the `\#X` block-leader pieces — with a
  closed-form unique solution when `\#X` is odd (derived and verified directly, §5.5.5 Step A).
- **Lone-`X`-Edge Vacuity Lemma** (§5.5.3). No genuine cyclic tie-dependency component ever has
  exactly one cross-type edge: the closing arithmetic always forces the unique cross-type node to
  be a numerically exact self-bisection, which (by the certified Vertex Lemma's classification and
  the dependency graph's own construction) has out-degree `0`, directly contradicting membership
  in a directed cycle (every cycle node has out-degree exactly `1` within the cycle) — so this
  configuration is never a genuine unresolved cycle at all, only a disguised, already-peelable
  self-bisection chain.
- **Even-`\#X` Infeasibility Lemma** (§5.5.4). No cyclic pattern with `\#X\ge2` even is ever
  physically realizable, for any mix of original/derived participants (given the Cycle
  Common-State Lemma): the closing identity required for consistency is exactly a nonempty signed
  subset sum over disjoint original indices, which the classical no-vanishing-signed-subset-sum
  fact (already Step 1 of `lemmas/superincreasing-no-early-zero.md`) shows can never vanish.
- **Generalized Cross-Type Domain-Violation Lemma** (§5.5.5). No cyclic pattern with `\#X\ge3` odd
  is ever physically realizable, for any mix of original/derived participants: the reduced
  `\#X`-cycle's unique solution, expanded via the token invariant, has the coefficient of the
  single most-significant original index `i^*` (over the whole union of supports) flipping sign as
  the block index varies (since `\#X\ge3` guarantees both parities occur among the block offsets),
  and the strict superincreasing dominance of `a_{i^*}` over the rest of the union forces the
  corresponding block value to be **strictly negative**, violating the domain requirement
  directly. This **strictly generalizes and supersedes** the previously-certified Cross-Type Cycle
  Infeasibility Lemma (which is recovered as the singleton-token special case) — and, crucially,
  is the mechanism that finally closes the derived-participant residual the round-7 crude
  dominance bound could not (no `a_{i^*}>2\sum_{l>i^*}a_l`-type inequality is needed at all).

**Headline consequence of combining all five:** every possible cyclic tie-dependency pattern
(`\#X=0,1,\ge2\text{ even},\ge3\text{ odd}` — an exhaustive classification) is now shown to be
either not a genuine cycle, physically infeasible, or provably not the true minimizer — for
**any** strictly superincreasing base sequence, with **no restriction to shallow (all-original)
cycles**. This closes `lemmas/dm-completeness-partial.md`'s all-cycles caveat completely for
`D_m`, giving the fully unconditional physical lower bound `g(D_m,m)\ge e_m\cdot S(D_m)` for every
`m` (§5.5.6). **Independently verified by bounded exact computation** (not a substitute for the
proofs, but strong corroboration): `\sim4000` total random trials across all five lemmas and a
broad mixed sweep (§5.5.7), zero counterexamples, with predicted mechanisms (which specific node
goes negative, inconsistency vs. unique-but-infeasible, etc.) matching exactly in every case
checked.
