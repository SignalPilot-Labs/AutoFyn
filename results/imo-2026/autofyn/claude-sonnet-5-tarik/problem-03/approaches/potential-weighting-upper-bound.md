## Status
partial

**(this builder, round 19 note — see new §33-§34 below.)** Dispatched to (1) prove §32's candidate
target in full (the Two-Touch KEEP `b_0\le w_1` sub-case at `|W|=3`), (2) attempt §31's Generalized
Touch-Bound Lemma at `k=2`. **Item 1: PROVED IN FULL, closing the exact gap round 18's proof-reviewer
flagged.** §33.1 gives a complete, independently re-derived 3-case proof of the new Two-Variable
Reflection Bound (`w_1-|b_0-w|\ge|b_0-(w_1-w)|` for `0\le b_0,w\le w_1`); §33.3 gives a complete,
exhaustive-case proof of all 5 per-term bounds needed by §32's reduction (including a genuinely
necessary 2-region, 4-sub-case split for the match-term `A_4`, and a 3-case split for the
keep-all-three term `A_5`, both fully worked out with no step skipped); combined via §32's own
(re-verified) min-of-terms reduction, this proves target (*) unconditionally:
`w_1-\mathrm{ThreeTouch}(b_0,\mathrm{rest})\ge\mathrm{TwoTouch}(\{b_0\},W)` for all `0\le b_0\le w_1`,
`|\mathrm{rest}|=2`. **§33.5 traces the consequence carefully and confirms — this time with an actual
complete proof of every ingredient, not a restated corroboration count — that Two-Touch
(`\mathrm{OPT}_{+1}(C,W)=\mathrm{TwoTouch}(C,W)`, `|C|\le1`) is now fully, unconditionally proved for
`|W|\le3`**: `C=\emptyset` is free at every `W` (certified Empty-Background Lemma); `|W|\le2` is the
certified base case; at `|W|=3`, DELETE (certified induction step), KEEP `b_0>w_1` (certified
unconditional), KEEP `b_0\le w_1` (this round's §33.3), and MATCH (certified
Match-Branch-Domination-via-Per-Partner-Domination, with its residual Per-Partner-Domination
dependency fully discharged at `q=|W|=3\le3`, the already-certified unconditional range) are all
`\ge\mathrm{TwoTouch}`, giving equality via the trichotomy. Computational corroboration
(`/tmp/round-19-build/verify_32.py`): `0` failures across a `462`-tuple exhaustive integer grid and a
`19{,}894`-trial random half-integer sweep on the target, all 5 per-term bounds, and the reflection
bound; two negative controls (dropping each load-bearing hypothesis) both fail `100\%` of the time,
confirming neither hypothesis is vacuous. New reusable lemma proposed for certification: the
Two-Variable Reflection Bound. **Item 2: NOT proved — genuine, honestly-reported partial progress
only, Status of §31 remains CONJECTURAL.** §34.1 finds and confirms a concrete negative result (the
cheapest possible single-witness shortcut, "drop the smallest element of `W`," fails `12.2\%` of the
time at the first genuine excess instance `|C|=2,|W|=5`); §34.2's shape census shows all 6 touch-`\le4`
selection shapes occur as the unique dominating witness in a non-trivial fraction of instances, ruling
out any small fixed witness set; §34.3 gives a structural (non-computational) finding that the natural
"peel-`W`" induction route to `k=2` requires, recursively, a brand-new `k=2,\sigma=-1` mirror (a
"Four-Touch"-type object, exactly analogous to how `k=1`'s Two-Touch needed Three-Touch) plus the same
unbounded-MATCH-background-growth obstruction the touch-bound framework exists to avoid — i.e. this
route is **not independently easier** than the already-multi-round-open `k=1` general induction. The
outline's own recommended "peel-`C`" Step-3 mechanism was not attempted this round (flagged as the
best next concrete target). **Net this round: one full gap closed (Two-Touch fully proved for
`|W|\le3`, a genuine milestone after 6+ rounds of the KEEP `b_0\le w_1` sub-case sitting open), one new
certified-candidate lemma, and honest, well-diagnosed non-progress on §31 (two new negative/structural
findings, no proof). None of Gap 1a's general-`q` Per-Partner Domination, Gap 1b, Gap 1c is closed;
Three-Touch's own MATCH branch remains open; Status correctly stays `partial`.**

**(this builder, round 18 note — see new §30 below.)** Dispatched, in priority order, to (1) certify
§29.1's Match-Branch-Domination-via-Per-Partner-Domination reduction in full, (2) attempt a full proof of
§29.2's Three-Touch MATCH Sibling-Domination Lemma (`\sigma=-1` only), (3) fix §29.3's `\delta_d\ge0`
provenance wording and attempt the `\delta_c` bound. **Item 1: the core reduction is closed, a complete
rigorous proof — but the round-18 write-up's further claim "Two-Touch fully proved for `|W|\le3`" was an
OVERCLAIM, caught and corrected by the round-18 proof-reviewer.** Match-Branch-Domination-via-Per-Partner-
Domination is now a certified lemma (§30.1, narrowed): Two-Touch's MATCH branch, at every size, is an
exact corollary of Gap 1a's Per-Partner Domination Lemma (itself proved `q\le3`, open `q\ge4`, fully
general/provenance-free) — this delivers a genuine result and correctly retires "Match-Branch Domination"
as a separately-tracked open item (it is not independent content at any size). **What it does NOT
deliver: "Two-Touch fully proved for `|W|\le3`."** That Corollary additionally needs the KEEP branch's
`b0\le w1` sub-case at `|W|=3`, i.e. `w1-\mathrm{ThreeTouch}(b0,\mathrm{rest})\ge\mathrm{TwoTouch}
(\{b0\},W)` (`|\mathrm{rest}|=2`) — the file below cites Lemma B (Three-Touch's base case) as if it
supplied this, but Lemma B only proves the *value* `\mathrm{OPT}_{-1}(\{b0\},\mathrm{rest})=
\mathrm{ThreeTouch}(b0,\mathrm{rest})`, not this comparison against `\mathrm{TwoTouch}`. §27.2(d)
(round 17) had already logged this exact inequality as "corroborated `0/1{,}239`, not proved" — it
remains exactly that status; the round-18 write-up's Corollary silently (and incorrectly) treated it as
discharged. **Corrected scope: Two-Touch's MATCH branch is closed at every size where Per-Partner
Domination is proved (`q\le3` unconditionally); Two-Touch itself is NOT yet fully closed even at
`|W|=3` — the KEEP `b0\le w1` sub-case there is still open (strongly corroborated, not proved).** See the
proof-reviewer's report and `lemmas/match-branch-domination-via-per-partner-domination.md`'s "Scope note"
for the precise gap and a concrete recommended next attempt (a Lemma-A-style case split mirroring
§28.4(d), applied in the `min` direction). **Item 2: attempted directly,
NOT proved.** Three separate proof-route candidates (a union-of-three-naive-exchange bound; a
general-background-size induction; a "matching the second-largest partner is always optimal"
simplification) were each tested and refuted with concrete counterexamples, precisely narrowing the
search space for a future attempt; the target itself remains corroborated with zero counterexamples
across a fourth independent codebase (`0/24{,}099` fresh trials this round, `\approx54{,}000+` combined
with the population's prior findings) but no proof mechanism was found. **Item 3: wording corrected as
required** (`\delta_d\ge0` is confirmed, via a third independent harness, to be FALSE outside genuine
`\mathcal F`-provenance, `148/944\approx15.7\%` failures — the file no longer risks the "provenance-free"
misreading the outline-reviewer flagged); within `\mathcal F`-provenance, a new structural finding
(`h_d$, the parity governing the Insertion-Difference Identity's sign, was even in all `949` fresh
case-(a) checks — previously undocumented) narrows what a future proof of `\delta_d\ge0` would need to
show, but neither `\delta_d\ge0` nor `\delta_c`'s magnitude bound was proved; two candidate closed-form
bounds for `\delta_c` were tested and refuted (`\approx68\%`, `\approx49\%` failure rates). **No gap is
fully closed among §29.2/§29.3. Two-Touch is now unconditionally proved for `|W|\le3` (new); Three-Touch
remains 4/5 pieces proved (MATCH branch open); Gap 1a's general-`q` Per-Partner Domination, Gap 1c's
case (a), remain open. Status correctly stays `partial`.** Full detail in §30; new lemma submitted for
certification (Match-Branch-Domination-via-Per-Partner-Domination, see "Promotable lemmas").

**(this builder, round 17 note — see new §28 below.)** Dispatched to (1) fix two precision notes
(quantifier scoping in §27.1's Gap1a/1b equivalence; the `\xi^*` LHS/RHS labeling drift), (2)
construct an explicit witness confirming Gap 1c's rare case (b) is non-vacuous, (3) attempt Three-Touch
(§27.2(d)'s candidate closed form) via the same induction-on-`|W|` technique that closed 3/5 of
Two-Touch's own pieces, (4) if time remained, attempt Match-Branch Domination. **All four items
attempted. Items 1-2 fully closed** (both precision notes fixed; two independently hand-verified
explicit case-(b) witnesses found and checked against Lemma P). **Item 3 substantially advanced: 4 of
5 structural pieces of Three-Touch are now fully proved** (DELETE branch, base case `|W|\le3`, and
BOTH KEEP-branch parity sub-cases `h=0`/`h=1` — the `h=0` sub-case via a genuine joint/mutual
induction with Two-Touch itself) — **only the MATCH branch remains open, mirroring Two-Touch's own
still-open MATCH branch exactly.** Two new lemmas submitted (Max-Element Triple Identity, Three-Touch
Base Case), `lemmas/max-element-triple-identity-and-threetouch-basecase.md`. **Item 4: one concrete
reduction idea for Two-Touch's MATCH branch tried and REFUTED** (exact counterexample,
`55/3000` — recorded so it is not re-attempted). **Neither Two-Touch nor Three-Touch is fully closed;
none of Gaps 1a, 1b (general induction), 1c (case (a)) is closed — Status correctly stays `partial`.**
Full detail in §28.

**(this builder, round 16 note — see new §26 below.)** Dispatched to (1) certify the Sum-Bound Base
Case Lemma, (2) certify the Insertion-Difference Identity, (3) attempt Gap 1c's half-step half-step
construction (pinning down `\xi^*`'s well-definedness first), (4) if time remains, attempt Gap 1a's
Two-Touch induction. **All four items were attempted; items 1-2 fully closed (certified); item 3
partially closed (the `\xi^*=\emptyset` boundary case fully resolved, conditional on Gap 1a's Step 2;
the nonempty case remains open); item 4 substantially advanced (3 of 5 structural sub-pieces proved,
the remaining 2 precisely re-scoped away from the confirmed-dead general route).** Three new lemmas
certified this round: `lemmas/sum-bound-base-case.md`, `lemmas/insertion-difference-identity.md`,
`lemmas/delete-suffices-insertion-domination.md`. **None of Gaps 1a, 1b (general induction), or 1c
(nonempty-`\xi^*` case) is fully closed — Status correctly stays `partial`.** Full detail in §26.

**(this builder, round 15 note — see new §24 below.)** Dispatched to work through the outline-
review's 4 action items in priority order: (1) re-verify §23.1's contested `\sim15\%` "argmin
dropped one level deeper" claim with a completely fresh harness; (2) check whether `q=4`'s
DELETE/KEEP branches close with the certified `q=3` bounds; (3) attempt Gap 1b's base case
(`w_1\ge2|c_1-c_2|`) as a standalone lemma; (4) certify the Background-Release Domination Lemma if
time allows. **Item 1 RESOLVED in favor of the outline-reviewer's finding:** a completely fresh,
independently-written harness (not reusing the outliner's, any explorer's, or the outline-reviewer's
code) tested the half-step against **every** second-level partner (not just the argmin) given a
genuine top-level triggered base generator and found **`0/15{,}175`** violations across `q=5,6,7` —
confirms the outline-reviewer's finding, contradicts §23.1's own `\sim15\%` figure. Two plausible
"bug" scenarios (comparing against the wrong background root `B_0` instead of `B_1`; or an
accidentally-untriggered top level) were shown to independently reproduce a violation rate of the
right order of magnitude (`19$–`36\%`), strong evidence the `\sim15\%` figure is a scoping artifact,
not a real fact about second-level partner choice. **Per the dispatch's own decision rule, the
half-step's hypothesis is correspondingly SIMPLIFIED** — no requirement that any match strictly
deeper than the base generator's own top-level match be its own local/global argmin; only the base
generator's own genuine trigger+argmin provenance is needed. **Item 2 answered precisely and
unfavorably for the old build-order assumption:** `q=4`'s DELETE and KEEP branches close with the
natural 3-bound extension of the certified `q=3` family (`0/62{,}580`), but the **MATCH branch does
NOT** — it already needs a piece of the "generalized `A_1`-bound family" previously assumed
necessary only at `q\ge5` (root cause pinned down exactly: `A_1` exploiting internal
duplicate/matching cancellation below the whole simple bound family, in every one of `439/62{,}580`
diagnosed cases). Also proved a new general **Three-Bound Domination Lemma** ruling out one entire
candidate direction (the "keep both `\mathrm{Res}` elements" bound) for that family. **Item 3: real
new partial progress, NOT closed.** Proved two new general elementary facts (**Keep-Top Bound**;
the **exact `q=3` dichotomy** `M=\min(D_{k^*},w_1-D_{k^*})`) that reduce the base case to the exact
equivalent claim "DELETE beats KEEP in `A_{3,k^*}`'s own decomposition," plus one concrete forced
consequence (`D_{k^*}>b_0`) of the negation, as a not-yet-completed contradiction-argument lead.
**Item 4: the Background-Release Domination Lemma is STRENGTHENED** to a fully unconditional form
(no `\min`-with-`e(C)` cap needed), with a clean one-line search-space-inclusion proof, ready to
certify. See new §24 for full detail, all fresh exact-`Fraction` computation
(`/tmp/round-15/verify-builder/`).

**(proof-outliner, round 15 note — see new §23 below.)** Three round-15 explorers scouted Gap 1a's
general-`q` closure, the suspected Gap 1a/Gap 1c shared-mechanism link, and Gap 1b's breakpoint
induction, in parallel. **Headline finding (positive, load-bearing):** Gap 1a's Deletion-Suffices/
general-`q` Per-Partner Domination and Gap 1c's half-step lemma are literally the SAME underlying
inequality (`OPT_{+1}(C\cup\{d\},X)\ge OPT_{+1}(C,X)`), confirmed once (and only once) correctly
scoped to `\mathcal F`'s TRUE root `(B_1,Z_1,+1)` (`k^*`'s own matched sub-instance, per §17.2 item
1 — not the raw top-level `(B_0,Z_0,+1)`) and restricted to background values produced by a
recursively-descending chain of TRUE global-argmin matches (not merely a locally trigger-satisfying
partner at any one level). Direct computation confirms: `0/3270` (`q=5`) and `0/690` (`q=6`) under
correct scope; `\sim15$–`91\%` failure under the wrong scope (root or restriction) — exactly
reproducing round 14's own negative control on the half-step, now understood as the identical
phenomenon. This sharpens (not merely restates) the target: `q=4` is separable and mechanical (the
`q=3` technique extends directly, no half-step needed — `\mathrm{Res}` has only 2 elements, so
matching its own top element always empties the residual `X`); `q\ge5` genuinely needs the
half-step lemma, now precisely rescoped to true-argmin-descended `\mathcal F` only, not the whole
of `\mathcal F` as loosely stated before. A new general **Background-Release Domination Lemma**
was also found this round (unconditional, any background size) but **both natural ways to chain it
into a Gap 1a closure are refuted** (full telescoping to a background-free bound is too lossy, `38\%`
violations; the direct one-step chain comparing a released quantity against `A_1` is false, `16\%`
violations — swapping `z_l` for the derived `d_l` is not monotone) — recorded as a real,
independently useful lemma candidate, NOT (yet) part of the closing mechanism. **Gap 1b gets a
base-case-first correction:** the `\mathrm{rest}=\emptyset` case (`w_1\ge2|c_1-c_2|`) is honestly
NOT proved anywhere on file (only numerically corroborated through round 14) and must be proved
first, as its own standalone lemma, before any inductive step is attempted; the inductive step
itself must induct on DELETE/KEEP/MATCH recursion DEPTH, not the flat outer `|\mathrm{rest}|`,
since real breakpoints occur strictly inside the inner recursion too, argmin ties spawn
simultaneous out-of-scope (`h=1`) sibling branches that must be explicitly filtered, and exact
equality is confirmed to hold along a continuous sub-interval in at least one family, not merely at
isolated points. **No un-benching of `dyadic-cascade-induction`/`concavity-minimax-duality`** —
nothing in this round's three reports gives either bench-mate new leverage on the open items (both
already fully served the lower bound; neither targets an `A`-generic/general-`n` upper-bound
statement). **Single approach file retained, no split** — all three named gaps remain sub-goals of
one whole-problem route (Claim A / Sharp Argmin Recovery via the Non-Matching-Witness criterion,
§17.2/§17.4), per the single-gap-trap rule.

**(this builder, round 14 note — see new §22 below.)** Dispatched to (1) certify Shrink-List
Monotonicity, (2) attack Gap 1a's Deletion-Suffices-for-`k^*`, (3) the half-step lemma, (4) the Sum
Bound breakpoint induction, in priority order. Certified Shrink-List Monotonicity in full (also filed
as `lemmas/shrink-list-monotonicity.md`) and used its Corollary to isolate Deletion-Suffices' "easy
half" (`M\le D`) as a one-line unconditional fact. Found a new, strictly more general **Per-Partner
Domination Lemma** (`A_{3,l}\ge\min(A_1,D_l)` for every `l`, no trigger, no argmin needed) that
provably implies Deletion-Suffices-for-`k^*` WITHOUT needing `k^*`'s global-argmin property — a
genuine simplification of what remains to prove — and **proved this new lemma in full for `q\le3`**
(a complete, from-scratch elementary case-analysis proof, not merely corroboration) via the Shrink-
List Corollary plus one other trivial delete-candidate bound and the certified Rank-Extraction
Identity; `q\ge4` remains open (corroborated only, `0` violations up to `q=6`). Did not reach Gaps
1b/1c this round (budget went entirely into (1)/(2) since (2) surfaced a substantial new mechanism
worth following to completion). **Gap 1a not fully closed (needs general `q`, only `q\le3` proved).
Status stays `partial`.**

**(this builder, round 13 note — see new §20 below.)** Dispatched to resolve Gap 1a's flagged
precision issue (No-Gap Lemma's exact scope) and attempt Gaps 1b/1c. **None of Gaps 1a/1b/1c is
closed this round.** Gap 1a's statement is corrected to the precisely-needed half-open form and
corroborated far more thoroughly, including the specific tie/boundary sub-case the round-13
outline-reviewer flagged as previously untested (now `0/15,819` fresh checks); one new elementary
identity is proved (not a full proof of Gap 1a); Gap 1b's corroboration is extended to deep
DELETE-closure chains and a tractable sub-case is isolated with a quantified safety margin; Gap 1c
has one new decisive negative result (the cheapest possible provenance-free shortcut is FALSE) plus
much larger corroboration of the correctly-scoped claim. See §20 for full detail. Status correctly
stays `partial`.

**(this builder, round 12 note — see new §18 below.)** Dispatched to close Gap 1 (Claim A /
"No-Second-Trigger at every depth" — the sole remaining gap identified by round 12's outliner and
independently re-verified by round 12's outline-reviewer, per §17). **Gap 1 is NOT closed this
round** — the theorem is not solved. What was achieved: **Gap 2 is closed in full** (a real proof,
not an assertion); **two new general-purpose lemmas** (Empty-Background, Background-Splitting) are
proved and together unconditionally resolve Claim A on the "eventually dominant" tail of every
recursion path in `\mathcal F` (reached within a handful of steps in every case checked); **one new
structural fact** sharpens the base generator (`B_0=\emptyset` can never trigger — `\mathcal F`'s
own base case needs `|B_0|=1` exactly); **a clean iff-criterion** (Non-Matching-Witness) reduces
Gap 1's exact remaining content to a single crisp existence question; and **the outline's own
explicitly-flagged open question — does an FSI-shaped argument reproduce Claim A? — is answered,
decisively, NO**, with the precise structural reason spelled out (FSI relates *sibling* match-branch
values to each other, not a node's MATCH branch to its own DELETE/KEEP branches). A sharpened
negative result also shows size-boundedness of the background (Gap 4's `|C|\le2`) is not, by
itself, doing any of the real work — arbitrary same-size backgrounds already violate Claim A, even
at `|C|=1` and even at the smallest list sizes `|W|=2,3` (correcting the outline's implicit
expectation that these would be an easy base case). **Status stays `partial` — no overclaim: Gap 1's
residual content (the non-dominated-background case) is real, precisely stated, and still open.**

**(this builder, round 11 note — see new §16 below; the Refined Delete-Recovery Conjecture (§15.4)
is NOT proved this round, and NOT refuted at its stated `|B|\le1` scope — a strictly sharper
reformulation (Sharp Argmin Recovery, §16.1) was found and survived the most adversarial testing
yet (a purpose-built embedding attack), one new general lemma was proved in full (the Forced Swap
Inequality, §16.2), and three precise negative results (§16.3) narrow exactly where a correct
general proof would have to live — but no proof was completed. Status stays `partial`; the theorem
is not solved this round.)**

**(proof-outliner, round 12 note — see new §17 below.)** Two of round 12's three explorers
(`math-explorer-global-witness.md`'s "No-Second-Trigger" and `math-explorer-recursive-invariant.md`'s
"Delete-Suffices") independently converged on the same underlying mechanism from different
directions; the third (`math-explorer-aimo0198-averaging.md`) confirmed a second, precisely-diagnosed
dead end for averaging-style arguments (do not revisit). §17 below reconciles the two convergent
findings into one precise unified target, the **Match-Free Recovery Lemma**, shows it is (up to
routine induction bookkeeping) literally the same claim as both explorers' candidates, shows it
trivially implies SAR/RDRC, and lays out a strong-induction-on-`q` proof skeleton with the hard
steps left as explicit, named gaps. This remains within `potential-weighting-upper-bound` — no new
slug opened.

**(proof-outliner, round 11 note — see new §15 below; §14 is now formally retired too.)** Round
11's three explorers (`math-explorer-charging.md`, `math-explorer-hall.md`,
`math-explorer-fresh-framing.md`) delivered: **(1) §14's Fixed-Support Uncrossing Conjecture
(round 10's primary route) is FALSE as stated — a concrete counterexample.** `Y=(7,5,4,4,3,1)`,
`p=6`, budget `b=5`: `OPT(Y,5)=NC(Y,5)=0` (the aggregate top-level fact is fine), but among the
`30` selections achieving this optimum, at least one has a **crossing** matching
(`K=\emptyset,D=\{0,5\},M=\{(1,3),(2,4)\}`) whose SAME-SUPPORT non-crossing re-pairing strictly
*increases* the value (`0\to2`) — directly violating §14's own precise statement ("if `M` has a
crossing, re-pairing the SAME support... achieves `v(K,D,M')\le v(K,D,M)`" for ANY `OPT`-achieving
selection). Recovery in this instance comes from a genuinely *different* optimal selection
(`K=\{2,3\},D=\{0,1,4,5\}`, no match at all), not a repair of the crossing one — the identical
"existential-support, not positional" failure mode already diagnosed for the flat-background route
in §13.6. **§14 is therefore doubly dead, alongside §13's flat-background generalization — do not
re-attempt the Fixed-Support Uncrossing Conjecture, nor the flat-background Match-Recovery Lemma,
in either of their previously-stated forms.** **(2) A Hall's-theorem/bipartite-matching
reformulation is a genuine, structural DEAD END**, not merely unproductive: the Match-Recovery gap
is a value/optimality question inside a globally rank-coupled objective (every element's sign
contribution depends on its rank among *all* currently-selected values), whereas Hall's theorem
only has content for separable, per-edge, multi-way *existence* questions — and existence of a
non-crossing completion for any candidate match partner is *always* trivially true here (`0`
failures across `2000+` exact trials, including every counterexample instance already on file), so
there is no Hall-deficient set to exploit even in principle. Do not re-attempt any Hall/defect-Hall
framing of this gap. **(3) Three candidate "fresh whole-problem framings" all collapse into
already-explored territory, no new leverage:** global concavity/KKT-duality on the opening
(re-confirmed FALSE, extending the already-certified `lemmas/non-concavity-of-g-at-n2.md`
counterexample to `m=3`); a layer-cake "toggle-pair" measure-theoretic recasting (verified correct
but mathematically isomorphic to the existing Lemma-P/D-M cancellation mechanism — a re-derivation
in different notation, not new attack surface); a "merge-tree/repeated-pairwise-difference"
recasting (collapses into the already-built-and-falsified Rule 1/Rule 2 greedy policies plus the
already-certified Superincreasing No-Early-Zero Lemma's own invariant). None of these three
warrants a build dispatch; do not re-open any of them in a dressed-up form. **(4) NEW primary route
for this round, replacing §14 (see new §15 below):** the **Refined Delete-Recovery Conjecture** —
a narrower-scope (restricted to `|B|\le1`, i.e. exactly the regime the theorem's own top-level
target needs, never touching the dead `|B|\ge2` family), single-condition reformulation of
Match-Recovery. Survives `~10,000+` combined random+exhaustive exact-integer trials (zero
violations) and comes with a concrete two-case induction skeleton reducing the entire remaining
gap to it. **This is this round's build target.** **(5) A genuinely different *technique*
(not a whole-problem framing) — an `aimo-0198`-style averaging/weighted-sum bound across the
DELETE/KEEP/MATCH branches — is queued as an unverified mechanism note (§15.5), not dispatched for
a build this round:** the explorer who surfaced it ran out of budget before any numerical test at
all (not even a single worked instance), so there is nothing yet to build against; a cheap
verification pass (checking the known hard instance `Y=(39,36,30,28,22,18,14)` at `b=6`) is the
correctly-scoped next step for a future round, not a build dispatch now.

**(proof-outliner, round 10 note — CORRECTION, see new §13.6 and new §14 below.)** Round 10's
explorer (`math-explorer-direct-attack.md`) found that §13.2-13.3's generalized Full-Slack
Insertion Lemma / unified "Match-Recovery Lemma" — the claim this file's entire §12.2 recursive
strong-induction-on-`p` skeleton depends on, for arbitrary flat background `B` with `|B|\ge2` — is
**FALSE**, not merely open. Minimal hand-verifiable counterexample: `B=\{2,4\}, Z=(6,3,2,1)`:
`\mathrm{OPT}_{+1}(B,Z)=0\ne1=\mathrm{TAGGED}_{+1}(B,Z,0)`. This directly contradicts §13.4's own
claimed `500/500` zero-mismatch check (a fresh independent sweep found `22/500` mismatches at
`|B|=2`); confirmed by two independent codebases plus full hand verification (§13.6 records this
formally, so no future round re-attempts the generalized form). **§12.2's recursive skeleton, as
framed (a flat, growing background set with no memory of which arcs produced it), cannot be
completed — it needs restructuring (carry positional/arc history, not a flat value set) or outright
replacement.** New primary route this round: the **Fixed-Support Uncrossing Conjecture** (new §14,
found independently by `math-explorer-plateau-check.md`, computationally very well supported —
204+ zero-failure crossing-optimal instances at the theorem's actually-needed budget `b=p-1`,
survives all 5 known adversarial instances including the round-6 local-exchange dead end's own
witness) — a genuinely different, non-recursive mechanism: uncross an `OPT`-achieving crossing
matching in place, on the SAME support, using bounded-depth pairwise swaps. This directly targets
`OPT(Y,p-1)=NC(Y,p-1)` (`|B|=0`, the theorem's actual top-level need) without any background-set
machinery. Both §13's certified lemmas (General Rank-Extraction Identity, the DELETE/KEEP branch
closed forms) remain valid and reusable — only the further generalization built on top of them in
§12.2/§13.3 is retired.

**(round 9 build note — see new §13 below, which sharpens/corrects §12's plan; PARTIALLY RETRACTED
by round 10, see the note above and §13.6 — the "no independent reduction in difficulty" diagnosis
below remains valid, but its claimed unification into one provable-looking "Match-Recovery Lemma"
is now known to be a unification into a FALSE statement at `|B|\ge2`, not merely a hard one.)**
Proved the
**General Rank-Extraction Identity** in full (new, general, promotable) and used it to fully close
the Generalized Multi-Background Peeling Lemma's DELETE and KEEP branches (the outline-reviewer's
flagged "KEEP is not free" concern is now genuinely resolved with an exact closed formula, not
deferred). Then found, via an exact branch-by-branch accounting (not just numerics), that the
Full-Slack Insertion Lemma (§12.1) is **not** an independently-easier base case as §12.1–§12.2
framed it — proving it in general requires exactly the aggregated Small-Gap Crossing-Domination
Lemma's own content, recursively, at every level. Unified both open items into a single **Core
Open Lemma ("Match-Recovery Lemma")**, still unproved, plus a genuine negative sub-result (a naive
unconditional strengthening of it is FALSE, exact counterexamples). See §13 for full detail.

**(proof-outliner, round 9 note — see new §12 below.)** This round's dispatch confirms the
aggregated Small-Gap Crossing-Domination Lemma (§11.4/§11.5) is the sole remaining gap for the
ENTIRE upper-bound direction, at every `m` and every `n` simultaneously (per
`dyadic-cascade-induction`'s round-9 correction: Case (i)/(ii) share one joint induction, so this
lemma alone — not a separate "general `n`" argument — closes the whole upper bound once proved).
New this round: (1) the "re-route to an endpoint of the crossing arc" lead flagged in §11.5 is
**now refuted** (fails `~14%` of the time, concrete counterexample) — do not pursue as a one-step
technique. (2) A new unconditional "full-slack degenerate-split" base case is found and isolated
as a concrete open sub-lemma. (3) §12 lays out a recursive strong-induction-on-`p` skeleton,
applying the certified Extreme-Element Peeling Lemma one level deeper (inside `INSERT_OPT`/
`INSERT_NC` themselves), anchored by the new base case — the most promising untried lead. (4) A
fallback proof-shape lead from crux `aimo-0558` is flagged for if the recursive route stalls.

**(round 8 build note — see new §11 below.)** Fixed the reviewer-identified imprecision in §10(b)
(the MATCH-branch's "reduces to a same-gap `(p-1)`-instance" phrasing): proved, in full and in
general (not just checked numerically), the **Extreme-Element Peeling Lemma** — a rigorous
three-way exact decomposition of `OPT(Y,b)`/`NC(Y,b)` on `y_1`'s fate, in which the DELETE and
KEEP branches are honest recursive calls to the *same* functions at strictly smaller parameters
(no caveat), while the MATCH branch is proved to reduce **exactly** (not approximately) to a
genuinely different quantity — `INSERT_OPT`/`INSERT_NC`, in which the produced difference `y_1-y_j`
is a *fixed, non-recursable, externally-inserted value* and the sub-selection ranges only over the
remaining `p-2` *original* elements. This is precisely the "block-extraction, not a fresh `OPT`
call" reading the reviewer asked for, now with a full proof (a bijection argument on selections,
not an appeal to Fact 3's sign bookkeeping, which turns out not even to be needed at this level).
Then found, by exact computation, that the *natural* next guess — a **per-fixed-partner** "Small-Gap
Crossing-Domination" claim (`INSERT_OPT(y_1-y_j,Z_j,p-2) = INSERT_NC(y_1-y_j,Z_j,p-2)` for
*each* `j` individually) — is **FALSE**, with a clean, fully hand-verified minimal counterexample at
`p=4`. The **correct** open lemma is the *aggregated* (min-over-`j`) version, which survives 1280
(MIN side) + 780 (MAX side) fresh exact-integer trials with zero mismatches — a real sharpening of
the round's target, precisely isolating what must still be proved. Full detail in §11.



**(round 7 build note — see new §9 below, which supersedes this file's central open claim.)**
This round fully proved §8 Step 1 (Layer-cake identity, general, promotable) and formalized
Step 2 (`NC(Y,b)` well-defined, with the inside/outside independence fact proved rigorously as
a genuine structural lemma about non-crossing partitions — also promotable). For Step 3 (the
"non-crossing matching+deletion" conjecture itself): **the conjecture AS LITERALLY STATED in §7.3
("for every sorted `Y` and every budget `b`") is FALSE** — an exact, twice-independently-verified
integer counterexample is given (`Y=(39,36,30,28,22,18,14)`, budget `b=3`: true optimum `1`,
best non-crossing value `2`). However, tracing through exactly how this sub-problem is actually
used by the chain-prefix+tail family (§6) shows **the only budget ever actually needed is
`b=p-1` exactly** (one less than the list size — because in the tight case `k=m+1` isolated by
Slack Collapse, after any chain-prefix of length `c` the residual has `p=k-c` elements and
budget `m-c=p-1` exactly). The counterexample above uses `b=3≠p-1=6`, and **does NOT survive**
at `b=p-1` on the very same list (`OPT=NC=0` there) — nor does an earlier-round counterexample
candidate. A fresh, extensive stress test *specifically restricted to `b=p-1`* (2200+ exact-
integer trials, `p` up to `10`, including adversarial/near-tied/superincreasing-shaped
configurations) found **zero mismatches**. **Net effect: the general conjecture is refuted (a
real, useful negative result — do not re-propose it in full generality), and a corrected,
strictly narrower replacement conjecture (`OPT(Y,p-1)=NC(Y,p-1)` for every `Y` of size `p`) is
proposed, precisely matching what the proof actually needs, numerically re-supported, but still
NOT proved.** See §9 for full detail, both counterexamples, and the rescoped open gap.

**(proof-outliner, round 6 note — new §8 skeleton below: the local pairwise
uncrossing-exchange technique is now CONFIRMED DEAD (this round's explorer sharpened the
diagnosis: the winning global optimum changes WHICH elements participate in a match, not
merely how a fixed support is re-paired — a move class no local exchange can express). Do NOT
propose any further variant of "hold the rest fixed, swap two arcs." §8 replaces it with a
genuinely different, global mechanism: (1) a new "layer-cake" reformulation of `e` as a
threshold-counting integral (an easy, general identity, apparently not previously stated
anywhere in this population), which converts the rank-dependent-sign obstruction into a
threshold-coverage question; (2) a top-down peel-the-extreme-element induction (on the number
of surviving original elements `p`, using the certified Fact 3 block-extraction identity's own
`(-1)^{|X|}` sign-flip as the "running sign offset" — this is precisely the KB "invariant/
monovariant" mechanism carried recursively, not a local exchange), deciding element `y_1`'s
fate (kept / deleted / matched-to-some-`j`, ALL `j` considered, not one fixed "obvious"
partner) and recursing on the residual via the SAME induction, which is exactly the standard
non-crossing-partition DP recursion (as used for interval/RNA-folding-style optimization) — a
move class that, unlike local exchange, can and does re-select supports. See §8 for the full
skeleton, the two key lemmas, and the precisely-isolated open technical gap (proving the
unrestricted/possibly-crossing global optimum is never better than this DP's own non-crossing
value).**

**(round 5 build note — see new §7 below.)** This round turned §6's skeleton into: (a) one
genuinely new, fully-proved, general-purpose reduction (`k≤m ⟹ e=0` trivially, via the
certified Fact 5 — collapses the ENTIRE upper-bound induction, both cases, to the single tight
sub-case `k=m+1`), (b) an honest FALSIFICATION of the outline's literal "sorted-adjacency"
Step-4 conjecture (exact integer counterexample), (c) a refined replacement conjecture
("non-crossing matching+deletion suffices for the one-shot tail's exact optimum") that is
numerically supported wherever the false one was tested and beyond, but NOT proved, and (d) a
negative sub-result ("full chain alone, with no tail phase, is insufficient by itself" —
confirms the two-component structure of §6 is load-bearing, not simplifiable to chain-only).
The central gap (closed-form/general proof of the chain-prefix+tail family, or of the
non-crossing conjecture) remains OPEN. Status stays `partial`.

**(proof-outliner, round 5 note — new §6 skeleton below: "chain-prefix + exact static
allocation," a genuinely different mechanism from the dead induction-loading family (§4/§5).
The critical distinction: induction-loading fell back to a LOSSY scalar bound
(`e_{m-\ell}\cdot S(\text{residual})`) after a bounded explicit prefix; this new family has NO
lossy fallback anywhere — after a chain-prefix of length `c\in\{0,\dots,m\}`, the remaining
budget is spent on the EXACT optimum of a restricted-but-fully-searched static (non-adaptive)
sub-problem, using the already-certified Fact 3 (block extraction). Stress-tested this round by
the case2-upper explorer against 650+ exact-`Fraction` trials (`m=2..6`) plus all three known
hard counterexamples on file, zero failures. A genuine partial dead end was also found and
recorded (pure one-shot allocation ALONE, without the chain-prefix, is insufficient — do not
propose dropping the chain-prefix component). No closed-form proof yet; see §6 for the
skeleton and the concrete next step (an exchange/rearrangement conjecture on the static
sub-problem).**

**(round 4 status note — the queued mechanism below (§4) has now been built and tested; see §5
for the result.)** Do NOT re-propose Rule 1 (top-two-ratio), Rule 2 (smallest-gap match), OR
the specific "induction-loading / bounded-K-level-lookahead-then-scalar-IH-fallback" mechanism
of §4/§5 in any dressed-up form — all three are now conclusively falsified with exact
counterexamples (Rule 1/Rule 2 in round 3; the bounded-lookahead family in round 4, §5.3–5.4
below, including a self-caught-and-fixed methodological trap worth reading before repeating the
experiment). The diagnosis common to all three: they each try to make do with a *fixed, small*
amount of extra structure (either none, or a bounded number of extra explicit levels) before
falling back to a *scalar* summary (`e_{m'}\cdot S(\cdot)`) of the residual — and round 4's
finding is that the scalar fallback is lossy in a way that a *bounded* prefix of exploration
cannot repair in general (the required exploration depth can be the *entire* remaining budget).
Any future attempt in this family needs either a genuinely non-scalar per-state invariant
carried through *every* level (not a bounded prefix), or an entirely different mechanism.

## Approaches tried
- **(round 19, this builder) §32's target proved in full — Two-Touch fully, unconditionally proved for
  `|W|\le3` (closing exactly the gap round 18's proof-reviewer flagged); §31's `k=2` Generalized
  Touch-Bound Lemma NOT proved, honest partial progress only (two negative/structural findings, no
  proof mechanism).** §33.1 proves the new Two-Variable Reflection Bound in full (3 exhaustive cases);
  §33.3 proves all 5 per-term bounds of §32's reduction in full (including a necessary 2-region,
  4-sub-case split for the match term and a 3-case split for the keep-all-three term, every sub-case's
  algebra derived and checked); §33.5 assembles these with already-certified pieces (Empty-Background
  Lemma, Three-Bound Domination Lemma, the certified `b_0>w_1` KEEP formula, Lemma B, and
  Match-Branch-Domination-via-Per-Partner-Domination with its residual dependency discharged at
  `q=|W|=3`) into a complete, non-circular proof that `\mathrm{OPT}_{+1}(C,W)=\mathrm{TwoTouch}(C,W)`
  for every `|C|\le1,|W|\le3`. `0` failures across `462`-tuple exhaustive + `19{,}894`-trial random
  computational corroboration, plus two `100\%`-failure negative controls confirming both hypotheses
  are load-bearing (not vacuous). One new lemma (Two-Variable Reflection Bound) submitted for
  certification. §34 attempts §31's `k=2` induction: finds the cheapest single-witness shortcut
  ("drop the smallest list element") is FALSE (`12.2\%$ failure at the first excess instance
  `|C|=2,|W|=5`); a shape census shows all 6 touch-`\le4` selection shapes occur as the unique
  dominating witness in a non-trivial fraction of instances, ruling out any small fixed witness set;
  a structural (non-computational) argument shows the natural "peel-`W`" induction route to `k=2`
  requires a brand-new `k=2,\sigma=-1` mirror plus the same unbounded-background-growth obstruction
  the touch-bound framework was introduced to avoid — **not independently easier** than the
  already-open `k=1` general induction. No proof found; the outline's "peel-`C`" route (§31.3 Step 3)
  was not attempted. **Two-Touch's own general-`q` closure (`q\ge4`), Three-Touch's MATCH branch, Gap
  1a's general-`q` Per-Partner Domination, Gap 1b, and Gap 1c remain fully open. Status correctly stays
  `partial`.** Full detail in §33-§34; verification scripts in `/tmp/round-19-build/`.
- **(round 18, this builder) §29.1 fully proved and certified in full (Match-Branch-Domination-via-
  Per-Partner-Domination): Two-Touch's MATCH branch, at every size, is an exact corollary of Gap 1a's
  Per-Partner Domination Lemma; delivers a new unconditional result, Two-Touch fully proved for
  `|W|\le3`.** §29.2 (Three-Touch MATCH Sibling-Domination, `\sigma=-1`) attempted directly via three
  distinct candidate proof routes (naive-exchange union bound; general-background-size induction;
  second-largest-partner-always-optimal simplification) — **all three refuted with concrete
  counterexamples**, narrowing the search space; the target itself remains fully corroborated (`0`
  counterexamples, `\approx54{,}000+` combined trials across 4 independent codebases) but **not proved**.
  §29.3's `\delta_d\ge0` wording corrected to require genuine `\mathcal F`-provenance (confirmed FALSE
  outside it, third independent reproduction); a new structural finding within `\mathcal F`-provenance
  (`h_d` even in `949/949` genuine case-(a) checks) narrows what a future proof would need; two candidate
  closed-form bounds for `\delta_c` tested and refuted. **Neither Two-Touch's own MATCH branch (reduced
  to, but not solved by, Per-Partner Domination's open `q\ge4` gap) nor Three-Touch nor Gap 1c case (a)
  is closed this round. Status correctly stays `partial`.** One new lemma submitted for certification.
  Full detail in §30.
- **(round 17, this builder) Fixed 2 precision notes; confirmed Gap 1c case (b) non-vacuous with
  explicit hand-verified witnesses; advanced Three-Touch (the `\sigma=-1` mirror needed for Two-Touch's
  `b_0\le w_1` KEEP-branch sub-case) from "not formulated" to "4 of 5 structural pieces fully proved"
  — DELETE branch, base case `|W|\le3`, and both KEEP-branch parity sub-cases (`h=0` via a genuine
  mutual/joint induction with Two-Touch, `h=1` unconditionally via the certified Empty-Background
  Lemma). Submitted 2 new lemmas (Max-Element Triple Identity; Three-Touch Base Case,
  `lemmas/max-element-triple-identity-and-threetouch-basecase.md`). Refuted one concrete reduction idea
  for the MATCH branch with an exact counterexample (recorded, not re-attempted). **The MATCH branch —
  a recurring open sub-problem of the same flavor across four instances (Gap 1a's
  Deletion-Suffices, Gap 1b's Sum-Bound, Two-Touch's own MATCH branch, and Three-Touch's own MATCH
  branch), NOT yet proved to be a single reducible lemma (only the DELETE-vs-KEEP half has an explicit
  proven reduction, §27.1; the DELETE-vs-MATCH half lacks one, and §27.2(d)'s touch-depth asymmetry
  between the two mirrors blocks a naive identification) — remains open in every manifestation; neither
  Two-Touch nor Three-Touch is fully closed; none of Gaps 1a, 1b, 1c is closed. Status correctly stays
  `partial`.** Full detail in new §28 above.**
- **(round 16, this builder) Certified 3 new lemmas (Sum-Bound Base Case, Insertion-Difference
  Identity, Delete-Suffices Insertion Domination); genuinely advanced Gap 1c's well-definedness gap
  (the `\xi^*=\emptyset` boundary case now fully resolved, conditional on Gap 1a's Step 2); proved 3
  of Two-Touch's 5 structural sub-pieces in full and precisely re-diagnosed the remaining 2 — but did
  NOT close Gaps 1a, 1b (general induction), or 1c (nonempty-`\xi^*` case) overall. Full detail in new
  §26 above.** (1) **Sum-Bound Base Case Lemma — CERTIFIED** (`lemmas/sum-bound-base-case.md`): the
  ~10-line contradiction proof from round-16's explorer/outliner independently re-derived and
  re-verified a third time with fresh code (`2{,}976/2{,}976` genuine triggered `h=0` `q=3` instances,
  `0` violations, brute-force `\mathrm{OPT}_{+1}`, not the closed-form dichotomy; isolated pure-algebra
  core `65{,}403` trials + `14{,}439`-trial boundary sweep, `0` violations both); wording fixed per the
  outline-reviewer's flag (the "`q=3` dichotomy" cited as a two-step combination of the certified
  Keep-Top Bound + a trivial singleton-list observation, not as a pre-existing standalone lemma).
  Closes ONLY the base case (`|Z_1|=1`) of Gap 1b — the general recursion-depth induction remains open.
  (2) **Insertion-Difference Identity — CERTIFIED** (`lemmas/insertion-difference-identity.md`): full
  self-contained derivation from two already-certified ingredients (Fact 3 + General Rank-Extraction
  Identity), independently re-derived via a route different from the outliner's own; `0/20{,}000`
  random + `0/780` exhaustive-grid trials, `0` violations. (3) **Gap 1c's `\xi^*=\emptyset` boundary
  case — new resolution, conditional on Gap 1a's Step 2 (Deletion-Suffices-for-`k^*`).** Discovered and
  proved a new general lemma (`lemmas/delete-suffices-insertion-domination.md`: if
  `\mathrm{OPT}_{+1}(C,W)=e(C)`, then `e(C)\le e(C\cup\{|w_a-w_b|\})` for any `w_a,w_b\in W`) that
  makes the chain `\mathrm{OPT}_{+1}(B_1,X)\le e(B_1)\le e(B_1\cup\{d\})=\mathrm{OPT}_{+1}(B_1\cup\{d\},
  X)` go through **exactly when Deletion-Suffices-for-`k^*` holds at that node** — already proved for
  `q\le3` (round 14), open for `q\ge4`. This fully, unconditionally closes the `\xi^*=\emptyset`
  sub-case at `q\le3`, and reduces it to an already-tracked open conjecture at `q\ge4` — a genuine,
  previously-unnoticed link between Gap 1a's Step 2 and Gap 1c. Pinned down `\xi^*`'s well-definedness
  via a canonical-choice convention (nonempty optimum preferred; `\emptyset` only if it is the unique
  optimum), resolving the outline-reviewer's precision flag. The nonempty-`\xi^*` case (Step 3's actual
  construction) remains open — two algebraic routes attempted and stalled, precisely reported (§26.4).
  (4) **Gap 1a's Two-Touch Lemma — 3 of 5 structural sub-pieces fully proved** (base case via Three-
  Bound Domination + a free `|C|=0` identity; the DELETE branch via the induction hypothesis + a subset
  argument; the KEEP branch's `b_0>w_1` sub-case via the certified Empty-Background Lemma, giving the
  KEEP branch = a candidate already in the target family, trivially); **the remaining 2 sub-pieces**
  (KEEP branch's `b_0\le w_1` sub-case, needing an unformulated `\sigma=-1` mirror bound; the MATCH
  branch) are **precisely re-diagnosed**: the general `|C|=2` Two-Touch route (already known false,
  `\approx24\%$ failure) is confirmed unnecessary — a much narrower "Match-Branch Domination" sub-claim
  (does the `|C|=2` MATCH sub-problem's value dominate the ORIGINAL `|C|=1` target, for this specific
  `d=|w_1-w_j|`, `w_1=\max(W)`?) is isolated as the actual remaining target, strongly corroborated
  (`0/7{,}265` optimal-value checks, `0/15{,}958` **exhaustive** every-candidate checks) but not proved.
  Widened the induction hypothesis from "`|C|=1`" to "`|C|\le1`" (both `\emptyset` and singleton
  backgrounds), a genuine, necessary correction to the outline's original skeleton (the KEEP branch's
  `b_0>w_1$ sub-case recurses into background `\emptyset`, outside the original "`|C|=1`" framing).
  **Net verdict: 3 new certified general-purpose lemmas, one genuine conditional closure (Gap 1c's
  `\xi^*=\emptyset` case at `q\le3`, reduced to a tracked open conjecture at `q\ge4`), and precise,
  well-corroborated (not proved) re-scoping of both Gap 1c's nonempty case and 2 of Two-Touch's 5
  pieces — no gap papered over, no overclaim. Status correctly stays `partial`.**
- **(round 15, this builder) Worked through the outline-review's 4 action items — did NOT close
  Gaps 1a, 1b, or 1c overall. Full detail in new §24 above.** (1) Re-verified §23.1's contested
  `\sim15\%` "second-level argmin required" claim with a completely fresh harness testing every
  second-level partner: `0/15{,}175` violations across `q=5,6,7`, confirming the outline-reviewer's
  finding and contradicting §23.1's own figure; pinned two plausible provenance-loss bugs (wrong
  background root; accidentally-untriggered top level) that independently reproduce a violation
  rate of the right order of magnitude (`19$–`36\%`). Per the dispatch's own decision rule,
  **simplified the half-step lemma's hypothesis** (drop the recursive/second-level argmin
  requirement; only the base generator's own top-level provenance is needed). (2) Directly checked
  `q=4`'s DELETE/KEEP branches: DEL/KEEP close with the natural `q=3`-style bound family
  (`0/62{,}580`), but **MATCH does not** (`439/62{,}580`, root cause pinned down exactly: `A_1`
  exploiting internal cancellation below the whole simple bound family) — `q=4`'s MATCH branch
  already needs the "generalized `A_1`-bound family" previously assumed to start only at `q\ge5`,
  correcting the recommended build order. Proved a new general **Three-Bound Domination Lemma**
  (`\min(x,|x-y|,|x-z|)\le e_{\mathrm{sorted}}(\{x,y,z\})`) ruling out one entire candidate
  direction for that family. (3) Attacked Gap 1b's base case (`w_1\ge2|c_1-c_2|`) as its own
  standalone lemma per the dispatch's priority order: proved two new general elementary facts
  (**Keep-Top Bound**: `\mathrm{OPT}_{+1}(C,W)\le w_1-|c_1-c_2|` when `h=0`; the **exact `q=3`
  dichotomy**: `M=\min(D_{k^*},w_1-D_{k^*})` exactly) reducing the base case to the precise
  equivalent claim "DELETE beats KEEP in `A_{3,k^*}`'s own top-level decomposition," plus one
  concrete forced consequence of the negation (`D_{k^*}>b_0`) as an unfinished contradiction-
  argument lead — **base case NOT closed**, but turned from zero attempts into a precisely-reduced,
  partially-attacked target. (4) **Strengthened** the Background-Release Domination Lemma to a
  fully unconditional form (no `\min`-with-`e(C)` cap needed), one-line search-space-inclusion
  proof, `0/36{,}000` fresh checks both signs — ready to certify. All computation fresh,
  independent code (`/tmp/round-15/verify-builder/`), validated against the file's own three
  worked examples before use.
- **(round 14, this builder) Certified Shrink-List Monotonicity in full (now `lemmas/shrink-list-
  monotonicity.md`); found a new, strictly more general Per-Partner Domination Lemma
  (`A_{3,l}\ge\min(A_1,D_l)` for every `l`, no trigger/argmin needed) that provably implies Gap 1a's
  Deletion-Suffices-for-`k^*` WITHOUT needing `k^*`'s global-argmin property, and PROVED this new
  lemma in full for `q\le3` (complete elementary case analysis, not just corroboration); `q\ge4`
  remains open (corroborated only, `0` violations to `q=6`) — did NOT close Gap 1a, 1b, or 1c
  overall (Deletion-Suffices' own instances can have arbitrary `q`). Full detail in new §22 above.**
- **(round 13, this builder) Resolved the outline-reviewer's flagged precision gap in the No-Gap
  Lemma's statement (Gap 1a), extended computational corroboration of Gaps 1a/1b/1c, proved one
  small elementary identity, and proved a decisive negative result narrowing Gap 1c's cheapest
  possible shortcut — did NOT close Gap 1a, 1b, or 1c. Full detail in new §20 above.** (1) **Gap
  1a fixed:** re-derived, from the certified `\ge`-convention `h:=|\{c\in C:c\ge w_1\}|`, that
  `h=1` occurs exactly on the half-open interval `(\min(b_0,d_{k^*}),\max(b_0,d_{k^*})]`, not the
  open interval the prior round's statement literally covered — corrected the Conjectured Lemma to
  this precise form and re-checked the propagation argument still goes through unchanged. (2)
  Extended corroboration specifically targeting the previously-untested tie/boundary sub-case:
  `9267` fresh checks (duplicate-allowing random sweep) plus `6552` exhaustive small-case checks,
  `0` violations of the strict, half-open, or either boundary-tie event, across all of them; a
  fine-grained rational hill-climb (step size down to `1/16`) found the margin's infimum shrinking
  toward but never crossing `0`, ruling out the "integer-artifact" reading of the prior round's
  hill-climb. (3) Proved one new elementary fact, the **Coincidence Identity**
  (`d_i-d_l=z_l-z_i` for any two indices `i,l\ne1`), and used it to identify a concrete
  two-element-shift reduction of (a sub-case of) Gap 1a — did not complete the sign argument
  (the shift amount's sign is not yet controlled, and the trigger condition `M<A_1` was not yet
  incorporated). (4) Extended Gap 1b's (Sum Bound) corroboration to deep DELETE-closure chains
  (`156`+`337` fresh checks, `0` violations) and isolated the `\mathrm{rest}=\emptyset` sub-case
  as a fully explicit numeric claim (`w_1\ge2|c_1-c_2|`), finding a `\ge3\times` margin
  computationally (stronger than the `2\times` needed) — not proved. (5) For Gap 1c, proved (with
  an explicit counterexample, background size `1`) that "forced matching never occurs" is FALSE as
  a general, provenance-free fact, ruling out the cheapest possible shortcut; extended the
  `\mathcal F`-restricted corroboration to `19{,}862` fresh checks (`\sim48\times` the prior
  `0/417`), `0` forced-matching events — still not proved, direct construction remains the
  recommended next step. **Honest net assessment: real, precisely-scoped incremental progress
  (a genuine precision fix, substantially deeper corroboration of previously-untested cases, one
  new elementary identity, one new decisive negative result) — none of Gaps 1a/1b/1c closed.**
  Status correctly stays `partial`.
- **(round 11, this builder) Attempted a full proof of the Refined Delete-Recovery Conjecture
  (§15.4). NOT completed — no proof found, no counterexample found at its stated scope. Full
  detail in new §16 above.** Summary: (1) found and heavily stress-tested a strictly sharper
  reformulation, **Sharp Argmin Recovery (SAR)** — recovery always happens at the SAME argmin
  match partner, not merely some partner as RDRC's raw existential form allows — surviving `0`
  violations across `~13,000+` fresh trials this round, including a purpose-built adversarial
  embedding of the already-dead `|B|=2` Match-Recovery failure mode into the exact structural slot
  where it would need to "leak through" to break SAR (`92` triggering embeddings, `0` failures,
  going beyond the outline-reviewer's own equivalent attack on the weaker RDRC form). (2) Proved,
  in full and in general (any background size, no triggering hypothesis needed), a genuinely new
  lemma: the **Forced Swap Inequality** — any single local re-pairing that reassigns `z_1`'s
  match partner to locally "fix" a crossing is provably no better than the value already
  established by global optimality (via a direct minimality argument, not requiring the Rank-
  Extraction Identity to be invoked explicitly, though in the same spirit). A first test-harness
  implementation showed apparent violations; hand-tracing the first one found the bug was in the
  *harness* (retaining a value that should have been replaced), not the lemma — corrected harness
  gives `3336/3336` clean checks. (3) Found three precise negative results narrowing where a
  correct general proof could live: averaging the Forced Swap Inequality's two alternatives does
  NOT recover the optimum (`0/81` successes); SAR's natural generalization to arbitrary background
  size is FALSE (exact `|B|=3` counterexample, confirming `|B|\le1` is load-bearing, not
  cosmetic); the natural "one-step compatible winner" strong-induction skeleton for SAR is FALSE
  in general (exact counterexample even at `|C|\le1`), precisely diagnosing that the correct
  inductive invariant must certify compatibility recursively down a specific (not arbitrary) family
  of sub-instances, not just at the top level. **No proof completed — Status stays `partial`, the
  theorem remains unsolved this round; this is honest, well-documented partial progress (one new
  certified-quality lemma, a sharper still-open conjecture, three negative results precisely
  narrowing the remaining search), not a closure.**
- **(round 11, outliner, revising the field per 3 explorer reports) §14's Fixed-Support Uncrossing
  Conjecture is FALSE — counterexample found; Hall's-theorem reformulation is a structural dead
  end; 3 candidate fresh whole-problem framings collapse into existing (2 of them already-dead)
  territory; new build target opened: the Refined Delete-Recovery Conjecture — full detail in new
  §15 below.** Summary: (1) `Y=(7,5,4,4,3,1),p=6,b=5` refutes §14 as literally stated — an
  `OPT`-achieving crossing selection's same-support non-crossing re-pairing strictly *increases*
  `e()` (`0\to2`); the true recovery uses a *different* optimal selection entirely, the same
  "existential-support, not positional" failure mode as §13.6's flat-background dead end. §14 is
  now doubly dead. (2) Hall's theorem is structurally the wrong tool (separable multi-way
  existence vs. this gap's globally rank-coupled value/optimality question) — not just untried,
  genuinely inapplicable; existence of a non-crossing completion is always trivial here (`0`
  failures, `2000+` exact trials), so there is no Hall-deficiency to exploit. (3) Concavity/KKT
  (re-confirmed dead, extends the round-3 certified counterexample to `m=3`), layer-cake
  toggle-pair (isomorphic to Lemma-P/D-M), and merge-tree/Euclidean (collapses into the
  already-falsified Rule 1/2 policies) framings: no new leverage, do not re-open any of them. (4)
  Opened the **Refined Delete-Recovery Conjecture** (§15.4) as the new build target — narrower
  than the dead flat-background Match-Recovery Lemma (scoped to `|B|\le1` only, never needing the
  refuted `|B|\ge2` machinery), survives `~10,000+` fresh trials, comes with a 2-case induction
  skeleton. (5) Queued (not dispatched) an `aimo-0198`-style averaging-bound mechanism note
  (§15.5) — flagged as a genuinely different *technique* for the same target, honestly reported as
  having zero numerical verification yet, so not ready for a build this round.
- **(round 9, this builder) Proved the General Rank-Extraction Identity in full (new lemma), used
  it to fully close the Generalized Multi-Background Peeling Lemma's DELETE and KEEP branches, and
  found — via an exact branch-by-branch accounting, not just numerics — that the Full-Slack
  Insertion Lemma is equivalent in content to the aggregated Small-Gap Crossing-Domination Lemma
  (not an independent, easier base case as §12.1–§12.2 assumed). Full detail in new §13.** Summary:
  (1) proved the **General Rank-Extraction Identity** (`e(F)=e(\mathrm{head})+(-1)^{r-1}x+(-1)^r
  e(\mathrm{tail})` for an element `x` at general sorted rank `r`, generalizing Fact 3's max-only
  case) — a short, clean, general, reusable lemma, verified `3000/3000` exact-integer trials,
  certified as `lemmas/general-rank-extraction-identity.md`. (2) Applied it to give the KEEP
  branch's exact closed form for a multi-background Peeling Lemma (governed by the parity of
  `h=`number of background elements exceeding the peeled element) — genuinely closing the
  outline-reviewer's flagged concern (KEEP is not "free," but is now completely derived, not left
  as "individually tractable, not written down"); confirmed DELETE and MATCH's *bijections* do
  generalize for free as the outline claimed. (3) By tracing exactly which recursive sub-instances
  the Full-Slack Insertion Lemma's own inductive proof needs (DELETE/KEEP reduce to strictly
  smaller instances of the *same* degenerate-split statement — free, by IH; MATCH reduces to a
  smaller instance of the *fully general, tagged* statement — **not free**, and in fact identical
  in shape to the main open aggregated lemma), showed the Full-Slack Insertion Lemma is **not**
  logically prior to/easier than the aggregated Small-Gap Crossing-Domination Lemma — they are the
  same statement recursively, confirmed concretely (the certified §11.3 counterexample is literally
  an instance of this recursion's own MATCH sub-case). Unified both into a single **Core Open Lemma
  (Match-Recovery Lemma)**. (4) Found a genuine negative sub-result: the naive unconditional
  strengthening of Match-Recovery ("the MATCH-branch aggregate alone, ignoring DELETE/KEEP
  compensation, always matches") is **FALSE** — `3/500` fresh exact-integer counterexamples, even
  though the *full* three-branch aggregate (including DELETE/KEEP compensation) continued to hold
  in all `500` trials. **No proof of the (correctly unified) central lemma completed this round**
  — reported honestly; the redirection toward the untried `aimo-0558` charging-argument lead
  (§12.3) or a fresh non-recursive technique is now more precisely motivated (the recursive route
  is shown, not just suspected, to be self-referential).
- **(round 8, this builder) Fixed the reviewer's precisely-identified §10(b) imprecision with a
  full, general proof (not a restatement), then found and honestly reported that the natural
  per-partner strengthening of the target lemma is FALSE, replacing it with the correctly
  aggregated version — full detail in new §11 below.** Summary: (1) proved the **Extreme-Element
  Peeling Lemma** in full generality (any sorted `Y`, any budget `b`, not just `b=p-1`): `OPT(Y,b)`
  (resp. `NC(Y,b)`) decomposes exactly as `min(DELETE, KEEP, min_j MATCH_j)`, where DELETE
  `=OPT(Y\{y_1},b-1)` and KEEP `=y_1-MAXOPT(Y\{y_1},b)` are proved by direct bijections on
  selections (clean, elementary, no gap), and MATCH_j is proved to equal `INSERT_OPT(y_1-y_j,
  Y\{y_1,y_j},b-1)` — a *different*, precisely-defined function in which the produced difference is
  fixed/externally-inserted and cannot be further deleted or re-matched (ruling out exactly the
  over-permissive misreading the reviewer caught, with a full proof, not just a corrected
  phrasing). Same three-way decomposition, same proofs essentially verbatim, for `NC`/`MAXNC`
  (MATCH_j `=INSERT_NC`, using the already-certified Non-crossing inside/outside independence
  lemma). Independently spot-checked computationally against direct exhaustive `OPT`/`NC` on 420+420
  fresh trials (`p=1..7`), zero mismatches, confirming the algebra. (2) Tested the natural
  strengthening of the "Small-Gap Crossing-Domination Lemma" the round-8 outline proposed — a
  **per-fixed-`j`** claim (`INSERT_OPT=INSERT_NC` for *each* partner `j` separately) — and found it
  **FALSE**, with an exact, fully hand-verified minimal counterexample at `p=4`
  (`Y=(92,89,77,73)`, partner `j=3`: `INSERT_OPT=1` via a crossing completion, `INSERT_NC=15`
  since that completion is forbidden — full hand arithmetic in §11). (3) Showed computationally
  (1280 MIN-side + 780 MAX-side fresh exact-integer trials, `p` up to `9`) that the counterexample
  above is compensated: the **aggregated** (min-over-`j`, resp. max-over-`j`) equality holds in
  *every* trial, even though the per-`j` equality fails in many of them (`345` per-`j` mismatches
  found among the MIN-side trials alone, all compensated in the aggregate). This is a genuine
  sharpening: the round-8 outline's phrasing did not distinguish per-`j` from aggregated, and the
  per-`j` reading (the more natural first guess, and arguably what the outline's own "no crossing
  configuration can strictly beat the best non-crossing completion" phrasing suggests) is
  definitively ruled out, while the correctly-aggregated statement remains open and well-supported.
  No proof of the aggregated lemma found this round (see honest gap in §11.5).
- **(round 7, this builder) Built §8's Steps 1-2 to full rigor (both now complete, general,
  promotable lemmas), and resolved Step 3 decisively but NEGATIVELY for the fully general
  conjecture, then rescoped it correctly to what the proof actually needs — full detail in new
  §9 below.** Summary: (1) proved the Layer-cake identity in full (elementary induction, matches
  the outline's sketch exactly). (2) Formalized `OPT(Y,b)` and `NC(Y,b)` precisely as minima over
  finite selection spaces, proved the trivial direction `NC≥OPT`, and proved (as a genuine new
  general lemma) that any selection that is *globally* non-crossing and matches `y_1` to `y_j`
  contains NO arc crossing between the open intervals `(1,j)`'s inside and outside — making the
  inside/outside independent-sub-problem decomposition in Step 2 exact, not approximate. (3)
  Found and twice-independently-verified an **exact integer counterexample refuting Step 3's
  conjecture in the fully general form stated in §7.3** (`Y=(39,36,30,28,22,18,14)`, `b=3`:
  `OPT=1<NC=2`, requiring a genuine 3-arc "crossing chain" — no violation found in extensive
  search at `p≤6`, so `p≥7` seems to be needed for this phenomenon). (4) Traced through the
  actual chain-prefix+tail family's usage and discovered the fully general conjecture was an
  *over-statement*: the only budget ever needed is `b=p-1` exactly (tight case), and **the
  counterexample vanishes exactly at `b=p-1`** on the same list. Proposed the correctly-scoped
  replacement conjecture `OPT(Y,p-1)=NC(Y,p-1)` and stress-tested it (2200+ fresh exact-integer
  trials, `p` up to `10`, adversarial/near-tied/superincreasing shapes) with **zero mismatches**
  — real, precisely re-scoped progress, still not proved.
- **(round 5, this builder) Turned §6's chain-prefix + exact static-allocation skeleton into
  real proof content, with one genuine new general lemma, one falsified conjecture (honestly
  reported, not forced), and one refined replacement conjecture — full detail in new §7
  below.** Summary: (1) proved, from the already-certified Fact 5, that the ENTIRE upper-bound
  induction (both Case (i) and Case (ii), every `m`) reduces to the single tight sub-case
  `k=m+1` — whenever `k≤m`, Xiang Yu trivially forces `e=0` using exactly `k` of his `≤m` cuts,
  beating any positive target outright; this had not been explicitly stated/proved anywhere in
  the population before (checked by `grep` across all approach files). (2) Tested the outline's
  literal Step-4 "sorted-adjacency" conjecture with a fresh, independent exact-integer random
  search (not reusing the outline's own ~15 instances) and found it **FALSE**: exact
  counterexample `A=(82,66,47,40)`, `m=3` — the adjacent-rank-only restricted search gives `7`,
  but the unrestricted (full) one-shot-tail exhaustive search gives `5` (both under target
  `47/3`, so §6's mechanism itself is unaffected, but the proposed simplification route is
  dead). Two more independent exact-integer counterexamples found at `m=4,5`. (3) Diagnosed the
  counterexamples' winning matchings (they pair non-adjacent original ranks while skipping a
  deleted interior element) and proposed a corrected, strictly more general replacement:
  **non-crossing matching + deletion** (arcs allowed to skip over points, but never cross one
  another) — implemented an independent exact search restricted to this class and found **zero
  mismatches** against the full unrestricted one-shot-tail optimum across 160 fresh random
  Case (ii) trials (`m=2..5`) plus both falsified-adjacency counterexamples; this is numerical
  support only, NOT a proof. (4) Tested "full chain alone, no tail phase" (i.e. always take
  `c=k-1`) as a possible simplification of the whole family and found it **also insufficient**
  by itself (many exact-integer counterexamples, e.g. `A=(33,19,5)`, `m=2`: full chain gives
  `9 > 57/7`) — but confirmed the full chain-prefix+tail family (searching all `c=0..m`) still
  handles every one of these via `c=0`, so this is a negative sub-result about oversimplifying,
  not a threat to §6's actual mechanism. **Net: the central gap (a full proof of the
  chain-prefix+tail family, or of the non-crossing conjecture, for the now-isolated `k=m+1`
  case) remains open**, but is more precisely characterized than at the start of the round.
- **(round 4, this builder) Built and stress-tested the queued induction-loading / 2-level-
  lookahead mechanism (§4 of the round-3/4 write-up). Result: NEGATIVE, but sharply
  informative — see full detail in new §5 below.** Summary: (1) the outline's literal
  Form E' candidate has an arithmetic bug as stated (double-counts `a_1-a_2`); corrected, it
  *does* now pass the `m=2` Rule-2 counterexample but **still fails the `m=3` Rule-1
  counterexample** (`69/875 > 1/15`) — exactly the "critical signal" the dispatch asked to
  watch for, reported honestly, not forced past. (2) Generalized to a broader "K-level,
  multi-branch lookahead, then fall back to the ordinary scalar IH" family and found, after
  **catching and fixing a self-introduced bug** (an accidental tautological self-comparison
  that made an early version of the test vacuously always pass — documented in full below as
  a cautionary methodological note), that **no fixed lookahead depth `K` independent of `m`
  suffices**: even full-width branching (every possible D/M move, not just 3 named
  candidates) at 2 explicit levels still fails on `12%` of random `m=4` trials, with the
  failure rate not shrinking as `m` grows. This shows the induction-loading mechanism, in the
  concrete "bounded extra lookahead + generic scalar fallback" shape the outline proposed, is
  **not viable** — the fallback bound `e_{m-\ell}\cdot S(\text{residual})` is too lossy
  regardless of how many explicit levels `\ell` precede it, unless `\ell` is allowed to grow
  with `m` (at which point it degenerates to full exhaustive search, i.e. no actual inductive
  shortcut). A clean, exact-fraction sharpening of the existing `m=2` Rule-2 counterexample was
  also found along the way (§5.2) and is recorded for reuse (no more decimals needed).
- **(round 3, outliner) UN-BENCHED** — see prior entry below for the diagnosis (the
  `dyadic-cascade-induction` two-candidate family provably fails to generalize to Case (ii)
  at `m≥3`, confirmed by the `m=3` near-uniform counterexample `(1/3,1/3,1/3)`).
- **(round 3, this builder) Turned the "greedy weighted-gap-priority rule" into a concrete,
  precisely-defined mechanism (the D/M operation reformulation), verified it on all the
  requested sanity checks, found and *falsified* the two simplest candidate greedy policies
  with exact, hand-checkable counterexamples, and established (by bounded exhaustive search)
  that the underlying operation space itself is sufficient at every point tested — the
  remaining gap is finding/proving a clean POLICY within that space, not the space itself.**
  This is genuine progress: a new certified-quality lemma (the D/M reformulation, in
  "Promotable lemmas" below), plus two precise, reproducible negative results narrowing where
  a correct greedy rule could live. Full detail below.

## Current best

**(round 19 pointer — most recent)** **Two-Touch (`\mathrm{OPT}_{+1}(C,W)=\mathrm{TwoTouch}(C,W)`,
`|C|\le1`) is now, for the first time, an actually COMPLETE, unconditional proof at `|W|\le3`** — not
merely corroborated, and not the round-18 overclaim the proof-reviewer caught and rejected. §33 supplies
the missing ingredient: a full proof of the KEEP `b_0\le w_1` sub-case at `|W|=3`
(`w_1-\mathrm{ThreeTouch}(b_0,\mathrm{rest})\ge\mathrm{TwoTouch}(\{b_0\},W)`), via a new elementary
Two-Variable Reflection Bound (§33.1, 3 exhaustive cases) applied across a fully-worked 5-term
case analysis (§33.3, including a 2-region/4-sub-case split and a 3-case split, every algebraic step
shown). §33.5 assembles this with the already-certified base case, DELETE branch, `b_0>w_1` KEEP
sub-case, and MATCH branch (Match-Branch-Domination-via-Per-Partner-Domination, with Per-Partner
Domination's dependency discharged at the certified `q\le3` range) into the full closure. This is the
population's first genuinely complete sub-theorem closure since Gap 1b's `\mathrm{rest}=\emptyset` base
case (round 16) and the DELETE/base-case pieces of Two/Three-Touch (round 16-17) — a real milestone,
though still only a `|W|\le3` boundary case, not the general-`q` theorem. §31's `k=2` Generalized
Touch-Bound Lemma remains open: a natural single-witness shortcut is now confirmed FALSE (`12.2\%`
failure), and a structural argument (§34.3) shows the natural extension route is not independently
easier than the still-open `k=1` general induction — narrowing, not closing, the search. **None of
Two-Touch's own general-`q` closure, Three-Touch's MATCH branch, Gap 1a's general-`q` Per-Partner
Domination, Gap 1b, or Gap 1c is closed. Status correctly stays `partial`.** See §33-§34 for full
detail.

**(round 18 pointer)** **Two-Touch is now unconditionally, fully proved for `|W|\le3`**
(new this round, §30.1): its MATCH branch, at every size, is a proved exact corollary of Gap 1a's
Per-Partner Domination Lemma (`MATCH_j\ge\min(A_1,D_j)\ge TT`, a complete 3-line proof from
already-certified/trivial ingredients), and Per-Partner Domination is itself already unconditionally
proved at `q\le3` — so at `|W|\le3` all three branches of Two-Touch's trichotomy (DELETE, KEEP, MATCH)
are unconditionally `\ge TT`, closing that size range fully. "Match-Branch Domination" is retired as a
separately-tracked open item — it is not independent content at any size, only Per-Partner Domination's
own already-top-priority general-`q` gap. Three-Touch's own MATCH branch (§29.2/§30.2, needed for
Two-Touch's `b_0\le w_1$ KEEP sub-case at general `q`) was directly attacked this round via three
distinct candidate proof strategies, all refuted with concrete counterexamples (narrowing, not closing,
the search) — the target itself (`\sigma=-1$ sibling-domination, true recursive branch values) remains
corroborated with zero counterexamples across `\approx54{,}000+` combined trials from 4 independent
codebases, but unproved. Gap 1c case (a)'s `\delta_d\ge0` sub-target is now correctly scoped as requiring
genuine `\mathcal F`-provenance (confirmed false without it, `148/944`), with a new narrowing structural
observation (`h_d` even in every genuine case-(a) instance checked, `949/949`) but still unproved;
`\delta_c`'s magnitude bound had two natural candidates tested and refuted. **None of Gap 1a (general
`q\ge4`), Gap 1c case (a), or Three-Touch's MATCH branch is closed. Status correctly stays `partial`.**
See §30 for full detail.

**(round 17 pointer)** Two precision notes fixed (quantifier scoping for the Gap
1a/1b equivalence; the `\xi^*` labeling drift, now standardized to "`\xi^*` optimizes the
AUGMENTED problem `\mathrm{OPT}_{+1}(B_1\cup\{d\},X)`"). Gap 1c's case (b) (sparsest optimal witness
Lemma-P-collapsing to a duplicate pair) is confirmed **non-vacuous** via two explicit, hand-verified
witnesses (e.g. `B_1=\{2,2\}`, `d=1`, `X=(18,12,6)`: `\mathrm{OPT}_{+1}(\{2,2,1\},X)=1`, achieved by
`\{6,6\}$, matching `e(\{2,2,1\})=1` via Lemma P exactly). **Three-Touch** (§27.2(d)'s candidate closed
form for `\mathrm{OPT}_{-1}(\{c\},W)`, the `\sigma=-1` mirror Two-Touch's own KEEP `b_0\le w_1`
sub-case needs) is now **4 of 5 structural pieces fully proved**: base case `|W|\le3` (new certified
lemma), DELETE branch, and BOTH KEEP-branch parity sub-cases (`h=1` unconditional; `h=0` via a genuine
mutual/joint induction with Two-Touch — legitimate, since each mirror's KEEP branch only ever needs
the OTHER mirror at strictly smaller `|W|`). **Only the MATCH branch remains open, in BOTH mirrors** —
this round's reconciliation (§28.4) confirms the MATCH-branch mechanism is the single shared
bottleneck across four manifestations: Gap 1a's Deletion-Suffices-for-`k^*`, Gap 1b's Sum-Bound
induction, Two-Touch's own MATCH branch, and (new) Three-Touch's own MATCH branch. One candidate
reduction idea for the MATCH branch (relax the forced background element `d` to an optional list
element) was tried and refuted with an exact counterexample. See §28 for full detail. Neither
Two-Touch nor Three-Touch is fully closed; none of Gaps 1a, 1b, 1c is closed this round.

**(round 15 pointer)** The half-step lemma's hypothesis is now simplified (drop the recursive
second-level argmin requirement, §24.1) — a fresh `0/15{,}175`-check re-verification decisively
resolved a cross-round discrepancy in favor of the simpler scope, removing bookkeeping from any
future strong-induction attempt at it. `q=4`'s DELETE/KEEP branches (Gap 1a) are confirmed free with
the natural bound-family extension, but its MATCH branch is confirmed to already need the
generalized `A_1`-bound family (§24.2, corrects the prior build-order assumption that this was only
needed at `q\ge5`); one candidate direction for that family is now proved permanently useless
(Three-Bound Domination Lemma). Gap 1b's base case (`w_1\ge2|c_1-c_2|`), previously totally
unattempted, is now reduced via two new proved elementary facts (Keep-Top Bound; the exact `q=3`
dichotomy `M=\min(D_{k^*},w_1-D_{k^*})`) to the precise equivalent claim "DELETE beats KEEP in
`A_{3,k^*}`'s own decomposition" — **still open**, but with one concrete forced-consequence lead
(`D_{k^*}>b_0$ if the target fails) for the next attempt. The Background-Release Domination Lemma is
strengthened to a fully unconditional form, ready to certify. See §24 for full detail. None of Gaps
1a/1b/1c is closed this round.

**(round 16 pointer)** Gap 1b's base case (`\mathrm{rest}=\emptyset`, `q=3`) is now a **certified,
complete proof** (`lemmas/sum-bound-base-case.md`) — the general recursion-depth induction
(`|Z_1|\ge2`) remains open. The **Insertion-Difference Identity** (a general, reusable tool) is
certified (`lemmas/insertion-difference-identity.md`). Gap 1c's `\xi^*=\emptyset` boundary case is now
**fully closed at `q\le3`** and reduced to Gap 1a's already-tracked open Deletion-Suffices-for-`k^*`
conjecture at `q\ge4`, via a new certified general lemma (`lemmas/delete-suffices-insertion-
domination.md`) — a genuine, previously-unnoticed link between the two gaps; Gap 1c's nonempty-`\xi^*`
case (Step 3's construction) remains open, two attempted algebraic routes recorded as stalled. Gap 1a's
Two-Touch Lemma has `3` of `5` structural sub-pieces fully proved (base case, DELETE branch, KEEP
branch's `b_0>w_1` sub-case); the remaining `2` (KEEP branch's `b_0\le w_1` sub-case; a narrower
"Match-Branch Domination" sub-claim replacing the confirmed-dead general `|C|=2` route for the MATCH
branch) are precisely identified and strongly corroborated but not proved. See §26 for full detail.
None of Gaps 1a, 1b (general induction), 1c (nonempty case) is fully closed this round.

**(round 15 pointer)** The half-step lemma's hypothesis is now simplified (drop the recursive
second-level argmin requirement, §24.1) — a fresh `0/15{,}175`-check re-verification decisively
resolved a cross-round discrepancy in favor of the simpler scope, removing bookkeeping from any
future strong-induction attempt at it. `q=4`'s DELETE/KEEP branches (Gap 1a) are confirmed free with
the natural bound-family extension, but its MATCH branch is confirmed to already need the
generalized `A_1`-bound family (§24.2, corrects the prior build-order assumption that this was only
needed at `q\ge5`); one candidate direction for that family is now proved permanently useless
(Three-Bound Domination Lemma). Gap 1b's base case (`w_1\ge2|c_1-c_2|`), previously totally
unattempted, is now reduced via two new proved elementary facts (Keep-Top Bound; the exact `q=3`
dichotomy `M=\min(D_{k^*},w_1-D_{k^*})`) to the precise equivalent claim "DELETE beats KEEP in
`A_{3,k^*}`'s own decomposition" — **still open**, but with one concrete forced-consequence lead
(`D_{k^*}>b_0$ if the target fails) for the next attempt. The Background-Release Domination Lemma is
strengthened to a fully unconditional form, ready to certify. See §24 for full detail. None of Gaps
1a/1b/1c is closed this round.

**(round 14 pointer)** Shrink-List Monotonicity is now certified in full (`lemmas/shrink-list-
monotonicity.md`), giving Deletion-Suffices-for-`k^*`'s easy half (`M\le D$) unconditionally in one
line. The hard half (`M\ge D`) is now known to follow from a new, strictly more general **Per-Partner
Domination Lemma** (`A_{3,l}\ge\min(A_1,D_l)` for every `l`, no trigger/argmin needed — §22.2), which
removes the need for `k^*`'s global-argmin property from the implication entirely (a genuine
simplification versus §21.1's two original routes, both of which needed it). **The new lemma is now
proved in full for `q\le3`** (base case `q=2`, and a complete elementary case-analysis proof for
`q=3`, every partner `l`, every sub-ordering — §22.2 — using only the certified Rank-Extraction
Identity and two trivial delete-candidate bounds on `A_1`); `q\ge4` remains open (corroborated only,
`0` violations to `q=6`, `3{,}100`-instance exhaustive `q=4` sweep). This is the largest fully-closed
chunk of Gap 1a's mechanism to date, though Gap 1a itself is not fully closed (Deletion-Suffices
instances can have arbitrary `q`). Gaps 1b (Sum Bound) and 1c (half-step) are unchanged from round 13
this round. See §22 for full detail.

**(round 13 pointer)** The furthest correct, fully rigorous progress on the sole remaining gap
(Gap 1 / Claim A, per §17's scope-family reduction) is: Gap 1 reduces (Background-Splitting
Corollary, certified) to `|C_{\mathrm{lo}}|\in\{0,1,2\}$; `|C_{\mathrm{lo}}|=0` is fully closed
(Empty-Background Lemma, certified); `|C_{\mathrm{lo}}|=1` is conjecturally vacuous within
`\mathcal F` (the No-Gap Lemma, corrected this round to its precisely-needed half-open form,
§20.1 — strongly corroborated, `0/15{,}819` fresh checks this round including the previously
untested tie/boundary sub-case, but **not proved**); `|C_{\mathrm{lo}}|=2` splits into KEEP-vs-DEL
(the Sum Bound, §19.5(a)/§20.2 — corroborated to deep closure depths, `0/493` fresh checks this
round, **not proved**) and MATCH-vs-DEL/KEEP (§19.5(b)/§20.3 — the cheapest possible provenance-free
shortcut is now known FALSE, and the correctly-scoped claim is corroborated to `19{,}862` fresh
checks, **not proved**). See §20 for this round's detail; §17-§19 for the full reduction chain.
The historical narrative below (§1 onward) records the full sequence of approaches tried since
round 1.

### 1. The D/M operation reformulation (proved in full — see Promotable lemmas)

Using the gap-decomposition identity `e(M) = Σ_{i odd}(a_i-a_{i+1})` (trivial telescoping,
confirmed correct by the outline-reviewer) together with the certified **Lemma P**
(`lemmas/duplicate-pair-invariance.md`), every one of Xiang Yu's single cuts, when restricted
to the two "vertex" move-types already isolated by `dyadic-cascade-induction`'s vertex lemma
(bisect or match-to-an-existing-value), has an exact effect on `e` that can be described
**without reference to the physical pieces at all** — purely as an operation on the *active
multiset* of values currently contributing to `e`:

- **Operation D(x)** ("bisect"): remove a value `x` from the active multiset (physically:
  split the piece of length `x` into two copies of `x/2`; these form a duplicate pair, so by
  Lemma P they contribute `0` to `e` and the rest of the multiset is exactly the active
  multiset with `x` deleted).
- **Operation M(x,y)**, for two active values `x ≥ y` (physically: split the piece of length
  `x` into `(y, x-y)`; the new piece of length `y` and the pre-existing piece of length `y`
  form a duplicate pair by Lemma P, contributing `0`, leaving the active multiset with `x,y`
  both removed and `x-y` inserted).

Each operation costs exactly one of Xiang Yu's cut points, and reduces the size of the active
multiset by exactly `1` (D: `k → k-1`; M: `k → k-1`, since two elements are removed and one is
added). This is proved rigorously as **Lemma D/M** below (Promotable lemmas section):
composing any legal sequence of `≤m` D/M operations starting from Liu Bang's opening multiset
`A` (`|A|=k≤m+1`) is always **achievable** by Xiang Yu using `≤m` real cuts, and the resulting
`e` of the true final (physical) multiset equals `e` of whatever active multiset the operation
sequence ends on (computed by the ordinary alternating-rank-sum formula, `e(∅)=0`).

This turns Case (ii)'s search for "the right strategy" into a **well-defined, purely
combinatorial optimization**: define
```
g(A,m) := min over all legal length-≤m sequences of D/M operations starting at A,
          of e(the multiset remaining at the end).
```
Since every operation sequence is realizable by an actual Xiang Yu response, `g(A,m)` is (by
construction) an **upper bound** for the true minimal value Xiang Yu can force — i.e. proving
`g(A,m) ≤ e_m·S(A)` for every admissible `A` (any `k≤m+1` nonnegative values) would close
Case (ii) (indeed the *whole* upper-bound induction) for every `m`. We do **not** need
`g(A,m)` to equal the true game value; being an achievable sufficient strategy is all the
upper-bound direction requires (as the outline-reviewer previously confirmed for the
narrower two-candidate family).

### 2. Sanity checks, as required by the dispatch — mixed result

**(a) The literal "greedy weighted-gap-priority" rule, made concrete.** The simplest concrete
instantiation of "close whichever gap dominates" is: **at each step, compare the two largest
active values `a_1 ≥ a_2`; if `a_1 ≥ 2a_2` apply D(a_1) (Case i), else apply M(a_1,a_2) (Case
ii); recurse on the residual with one fewer cut.** Call this **Rule 1**. This is exactly
`dyadic-cascade-induction`'s Case (i)/(ii) split, but now executed as a genuine deterministic
recursive algorithm on the whole residual (not a one-shot "min of two IH IH-bound candidates"
— the previous source of the `0.081` false alarm, see below).

- **n=1 dyadic `(2/3,1/3)`, m=1:** Rule 1 gives `1/3` — matches the known exact value `1/3`
  exactly (verified with exact `Fraction` arithmetic).
- **n=2 dyadic `(4/7,2/7,1/7)`, m=2:** Rule 1 gives `1/7` — matches exactly.
- **n=2's two attained Case-(ii) extremal points** (from `dyadic-cascade-induction`'s hand
  casework): `(5/11,4/11,2/11)` gives `1/11`, `(4/9,3/9,2/9)` gives `1/9` — both match the
  hand-derived exact values exactly.
- **`m=3` near-uniform counterexample `(1/3,1/3,1/3)`:** Rule 1 gives **`0`**, not the false
  `0.081` the old (lossy, IH-bound-based) two-candidate family reported. This confirms the
  diagnosis in the outline: the earlier "0.081 > 1/15" failure was an artifact of bounding the
  residual with a *lossy* induction-hypothesis inequality, not a defect in the underlying
  strategy family itself — when the same match/bisect moves are *executed exactly* (recursing
  on the literal residual, not an upper-bound formula for it), they already give the correct
  value `0` here, using only 1 of the 3 available cuts (matches the outline's own hand
  computation).

  So Rule 1 **passes** every sanity check the dispatch asked for.

**(b) Broader stress test — Rule 1 is FALSIFIED by an exact, hand-checkable `m=3`
counterexample.** A bounded randomized search (200,000 uniform random 4-piece configurations
at `m=3`, `k=4=m+1`) found configurations where Rule 1's value *exceeds* the target
`e_3=1/15`. Refining and simplifying to exact fractions gives a clean, reproducible
counterexample:
```
A = (239/500, 28/125, 3/20, 37/250) = (239/500, 112/500, 75/500, 74/500),  sum = 1.
```
Tracing Rule 1 by hand (all arithmetic exact):
1. `a_1=239/500 ≥ 2a_2=224/500`: Case (i), apply D(a_1). Residual `(112/500,75/500,74/500)`.
2. `a_1=112/500 < 2a_2=150/500`: Case (ii), apply M(a_1,a_2), i.e. subtract:
   `a_1-a_2 = 37/500`. Residual `(74/500, 37/500)`.
3. `a_1=74/500 = 2·(37/500) = 2a_2`: boundary of Case (i) (`≥` triggers Case i by the rule's
   convention), apply D(a_1). Residual `(37/500)`.
4. Budget exhausted (all 3 cuts used); one active element `37/500` remains uncancelled, so
   `e = 37/500`.

`37/500 = 0.074`, versus target `e_3 = 1/15 ≈ 0.0667` (exactly, `37/500` vs `1/15`: common
denominator `1500` gives `111/1500` vs `100/1500`, so `37/500 = 111/1500 > 100/1500 = 1/15`
**strictly**). **So Rule 1 genuinely fails at `m=3`: it is not a valid greedy policy for
general `m`, confirmed with exact arithmetic, not a numerical artifact.**

Diagnosis: Rule 1 is *myopic* — it commits to bisecting/matching based only on the current
top two ranks, without regard to how many operations remain or what the *other* pieces look
like. In this example, spending 2 of the 3 cuts on the two largest pieces (deleting both
outright) leaves only 1 cut for the bottom two pieces `(75/500,74/500)`, which are nearly
equal (gap `1/500`) and would cancel almost to `0` if matched — but Rule 1 never gets to make
that match, because it already used its match-budget on the wrong pair at step 2. Indeed, an
**exhaustive search over all length-3 D/M sequences** on this same `A` (bounded — the state
space for `k≤4, m≤3` is small enough to enumerate completely, no unbounded search) finds the
truly optimal D/M sequence:
```
D(239/500) → D(112/500) → M(75/500,74/500) = 1/500,
```
giving `e = 1/500 = 0.002`, comfortably under the target `1/15`. **This confirms the D/M
operation space itself is rich enough to beat the target at this exact point — Rule 1 is
simply the wrong policy within that (adequate) space, not evidence the space is
insufficient.**

**(c) A natural refinement ("match the smallest gap, not the top two") also fails, at a
*different*, simpler point.** Define **Rule 2**: at each step, compare `D(a_1)` against
`M` applied to whichever *adjacent* pair `(a_i,a_{i+1})` has the smallest gap
`a_i-a_{i+1}` (not necessarily the top two), and recurse on whichever of the two candidates
gives the smaller value. Rule 2 does fix the Rule-1 counterexample above (`0.00244`, well
under target) and still passes n=1/n=2/near-uniform checks. But a further bounded random
search at `m=2` finds Rule 2 **also fails**, at:
```
A = (0.5006, 0.3331, 0.1664)  (m=2, k=3), Rule 2 value ≈ 0.1664 > target e_2 = 1/7 ≈ 0.1429.
```
Tracing: Rule 2 compares `D(a_1)` (giving, after the certified `n=1` closed form on the
residual `(a_2,a_3)`, value `≈0.1664`) against `M` on the *smallest-gap* adjacent pair, which
here is `(a_2,a_3)` (gap `≈0.1667`, slightly smaller than `(a_1,a_2)`'s gap `≈0.1675`) —
giving `≈0.1667`. Rule 2 picks the smaller of these, `0.1664`, and stops (budget exhausted).
**But the actual optimal single cut at `m=2` here is `M` on the *top two* `(a_1,a_2)`** (gap
`0.1675`, the *larger* gap, not the smaller one!): this gives residual `(a_1-a_2,a_3) ≈
(0.1675,0.1664)`, whose own near-equal pair (gap `≈0.0011`) essentially cancels once the
level-1 formula is applied, giving `e≈0.0011` — over 100× better than either of Rule 2's two
candidates. **So "always target the smallest gap" is also not a valid general rule**: here
the objectively-best move targets the *larger*-gap pair, because doing so creates a *new*
near-cancelling pair one level down that neither naive rule anticipates.

### 3. Honest assessment

- The **D/M operation reformulation is correct, general, and now a certified reusable lemma**
  (see "Promotable lemmas"): it is a genuine, non-trivial mechanistic description of Xiang
  Yu's effective strategy space, reducing "which cuts to make" to "which sequence of
  delete/match operations to apply to the active-value multiset" — this is a real
  contribution, independent of whether a clean closed-form policy is ever found within it.
- **Neither of the two simplest concrete greedy policies within this space is universally
  correct.** Rule 1 ("top-two ratio test") fails at `m=3` (exact counterexample above); Rule 2
  ("smallest-gap match") fails at `m=2` (exact-to-3-decimal counterexample above, exhibiting
  that the *correct* move is sometimes to target the *largest* gap specifically because it
  sets up a favorable cancellation one level deeper — a genuinely non-local effect that no
  purely local (single-step) comparison rule captures).
- **Bounded exhaustive search over the full D/M operation space** (feasible for the small `m`
  tested here) *does* find values `≤` target at every point checked so far, including both
  counterexamples above and the `m=1..3` random/refined searches — this is evidence (not
  proof) that the D/M space is sufficient in general, and that the missing piece is a
  **correct policy/proof technique**, not a richer strategy space. A clean, hand-provable
  general rule (e.g. some form of lookahead, or a global assignment of cuts to gaps solved as
  a matching/allocation problem rather than a greedy walk) was not found this round within the
  time budget.
- Consistent with the reviewer's guidance, this round's work stayed within the bounded
  sanity-check task and did not proceed to an unproven "general-`m` write-up" once the
  mechanism was found not to reduce to a simple provable greedy rule — the failure is reported
  honestly rather than papered over.

**Open gap (the central one, unresolved):** find a policy (not necessarily "greedy" in the
naive single-step sense — possibly a global allocation of the `m` operations to `m` chosen
gap-closing targets, decided by comparing *all* `O(k^2)` possible pairings at once rather than
picking one move at a time) within the D/M operation space that is (i) simple enough to state
and analyze in closed form, and (ii) provably achieves `g(A,m) ≤ e_m·S(A)` for every `A`. Both
tested single-step greedy candidates are now conclusively ruled out with exact
counterexamples, which meaningfully narrows the search for the next round: any future rule
must account for cancellations that occur *after* the current step (i.e. it cannot be
determined by a comparison local to the current top-ranked elements or gaps alone).

**Round-4 update to this open gap (see full §5 below):** the natural next idea — "induction
loading," strengthening the IH with a *bounded* amount of extra explicit lookahead before
falling back to the plain scalar bound — was built out precisely and **also refuted**, with a
sharper diagnosis than either Rule 1 or Rule 2 alone gave: the required lookahead depth to
rescue the `m=3` Rule-1 counterexample is the *entire* remaining budget (`\ell=m`), and the
failure rate of bounded-depth variants does not shrink as `m` grows (tested up to `m=4` with
both a 3-named-branch and a full-width-branching version). So the fix cannot be "a little more
lookahead" — it needs a genuinely richer per-state invariant carried through *every* level of
the induction, not a bounded prefix of extra explicit steps. No such invariant was found this
round.

### 4. Queued mechanism (round 4) — induction loading for Case (ii) at general `m`

**Target.** Prove `g(A,m) \le e_m\cdot S(A)` for every `A` (Case (ii) configurations, general
`m`), by strengthening the induction hypothesis rather than by naming a greedy policy.

**Diagnosis, made precise (why the naive scalar IH is information-poor).** The `m=3`
counterexample's *true* optimal D/M sequence is `D(a_1)\to D(a_2)\to M(a_3,a_4)`
(§2b above), reaching `e=1/500`. A naive "first move + IH bound on the residual" argument
instead only has access to `g(\text{residual},m-1) \le e_{m-1}\cdot S(\text{residual})` — a
lossy **upper bound**, not the true recursive optimum `g(\text{residual},m-1)` itself — and
substituting the lossy bound in place of the true value is exactly what makes Rule 1/Rule 2
(and any similar "first move + generic IH bound" scheme) provably insufficient: the bound
throws away the fact that the residual `\{a_3,a_4\}=\{75/500,74/500\}` happens to be almost
tied, information the scalar bound `e_{m-1}\cdot S` cannot see. **Any fix must therefore make
the IH itself carry some extra structural information about the residual, not merely apply
the existing scalar bound recursively.**

**Concrete bounded diagnostic task (do this FIRST, before any general-`m` write-up — cheap,
uses only the two counterexamples already on file, no new search).** For each of the two
falsified-rule counterexamples (`A=(239,112,75,74)/500` at `m=3`; `A\approx(0.5006,0.3331,
0.1664)` at `m=2`), compute by hand/exact-`Fraction`:
(a) the true optimal D/M value `g(A,m)` (already known: `1/500` and (from §2c(c) of the
`m=2` example, the "match top two" move) `\approx0.0011`, respectively);
(b) what extra piece of information about `A` (beyond `a_1,a_2,S`) the optimal sequence's
*first* move needed to "know about" to be chosen correctly — e.g. is it simply
`a_3-a_4` (the smallest gap among ranks `\ge3`), or something about the parity/count of
elements below rank 2, or the ratio `(a_3-a_4)/(a_1-a_2)`? Tabulate this for both examples.
This is a bounded (2-point), fully computable task that pins down the *shape* of the missing
IH term before committing to a general formula.

**First candidate richer-IH shape to test (to be verified/refuted against the diagnostic
above, NOT assumed correct).** Strengthen the claim from a single scalar bound to a **pair**:
```
(Form E) g(A,m) \le e_m\cdot S(A),   AND
(Form E') g(A,m) \le (a_1-a_2) + g(\{a_1-a_2\}\cup\{a_3,\dots,a_k\},\,m-1)   [exact, not a
          bound — this is literally the value of the specific strategy "M(a_1,a_2) then play
          optimally," which unlike Rule 1 does NOT commit to a specific continuation].
```
Form E' is trivially true (it's the definition of `g` applied to one specific first move), so
it adds nothing by itself — **the actual content to find** is a general-purpose bound on the
RHS of Form E' that is *tighter* than `e_{m-1}\cdot(S-a_2)$ precisely in the cases where the
naive bound fails (i.e., when the residual `\{a_1-a_2,a_3,\dots,a_k\}` contains a near-tied
pair). A natural candidate refinement, to test on the diagnostic examples first: bound
`g(M,m-1)` not by `e_{m-1}\cdot S(M)` alone but by
`\min\big(e_{m-1}\cdot S(M),\ (\text{2nd-smallest gap of }M) + e_{m-2}\cdot(S(M) -
\text{that gap's two elements})\big)` — i.e. recursively apply the SAME idea one level
further (an explicit 2-level lookahead baked into the IH statement itself, not chosen
greedily at runtime). This is exactly what "vectorizing" the IH into `(e, \text{deeper
lookahead term})` means concretely; it must be checked against both diagnostic examples
before any attempt at a general-`m` proof.

**Why this is a genuinely different mechanism from Rule 1/Rule 2 (not a re-skinned dead
end).** Rule 1/Rule 2 each committed to a *specific, single, greedy, m-independent* selection
rule evaluated once per level. Form E'/the 2-level-lookahead refinement instead strengthens
what the *induction hypothesis itself* asserts is achievable — the "choice" of which move is
optimal is never made explicit as a rule; it falls out of comparing the (now richer) bounds
after the fact, the same way Case (i)'s own closure (§2d) compared two IH-supplied bounds
(forms A/B) via a min, rather than picking one a priori. This is the same *shape* of fix that
worked for Case (i); the explorer's diagnosis is that Case (ii) needs a comparable but
*deeper* (2-level, not 1-level) version of the same idea.

**Cheap-kill check for the builder, before investing further:** if the 2-level-lookahead
candidate above, evaluated by hand on the two known counterexamples, does not beat both
`e_3=1/15` (for the `m=3` example) and `e_2=1/7` (for the `m=2` example), discard it
immediately and report which structural feature of the true optimal move it still fails to
capture — do not proceed to a general-`m` write-up on an unverified candidate.

### 5. Round-4 build: testing the induction-loading mechanism (negative result, in detail)

All computations in this section are exact (`fractions.Fraction`), independently re-runnable.

**5.1 Diagnostic task on the two known counterexamples (as required before any candidate
test).** Using the certified exhaustive D/M search (feasible at these small sizes — every
legal operation sequence of length `≤m` is enumerated, no heuristic pruning), the *true*
optimal first move was tabulated for both:

- **`m=3` example** `A_1=(239,112,75,74)/500` (the Rule-1 counterexample): the exhaustive
  search shows **four different first moves all tie for optimal** (`g(A_1,3)=1/500`):
  `D(a_1)`, `D(a_2)`, `M(a_1,a_2)`, and `M(a_3,a_4)` (the smallest-gap pair) — so no single
  "correct first move" exists to identify; what *is* pinned down is that the winning
  continuation from `D(a_1)`'s residual `(112,75,74)/500` needs a **second** correct choice
  (`D(a_2)`, *not* `M(a_1,a_2)` which Rule 1 picks and which is the losing branch scoring
  `37/500`) — i.e. the missing information is two moves deep, not encoded in any single-step
  local comparison at the top of the residual.
- **`m=2` example** (see §5.2 for a new, cleaner exact version): the true optimal first move
  is `M(a_1,a_2)` (matching the *larger*, not the smaller, adjacent gap), which happens to
  create an *exact tie* with `a_3`, giving `e=0` outright — confirming the outline's own
  diagnosis (the correct move is invisible to a same-step gap-size comparison; it only pays
  off because of a coincidence one level down).

**Conclusion of the diagnostic:** the "extra piece of information" needed is not a fixed
scalar feature of `A` (like "the smallest gap among ranks `≥3`") — it is different in kind in
the two examples (a *second* correct move in one, a *coincidental tie* in the other). This
already suggested skepticism that a single closed-form 2-level formula would generalize; §5.3
confirms this.

**5.2 A clean, exact-fraction sharpening of the `m=2` Rule-2 counterexample.** The round-3
version used decimals (`A\approx(0.5006,0.3331,0.1664)`). A direct search over exact fractions
(denominator `1000`) found an exact point with the identical qualitative behaviour and a
strikingly clean structure:
```
A_2 = (1/2, 333/1000, 167/1000),   sum = 1.
```
Note `a_1-a_2 = 500/1000-333/1000 = 167/1000 = a_3` **exactly**. Computing all `6` possible
single-move-then-closed-form-`m=1` values (using the exact closed form for a 2-element
residual `{p≥q}`, `g(\{p,q\},1)=\min(p-q,q)`, which is elementary — `D(p)\to q`, `D(q)\to p`,
`M(p,q)\to p-q`, and `p-q\le p` always, so the min of the three is `\min(p-q,q)`):

| first move | residual | `g(\text{residual},1)` |
|---|---|---|
| `M(a_1,a_2)` | `(167/1000,167/1000)` | **`0`** (exact tie) |
| `M(a_1,a_3)` | `(333/1000,333/1000)` | `0` |
| `D(a_1)` | `(333/1000,167/1000)` | `83/500` |
| `M(a_2,a_3)` | `(1/2,83/500)` | `83/500` |
| `D(a_2)` | `(1/2,167/1000)` | `167/1000` |
| `D(a_3)` | `(1/2,333/1000)` | `167/1000` |

So `g(A_2,2)=0` exactly (via `M(a_1,a_2)`, confirmed independently by the certified exhaustive
search). Rule 2 ("match the smallest gap") compares `D(a_1)` (`=83/500`) against matching the
smaller of the two adjacent gaps: `\text{gap}(a_1,a_2)=167/1000`, `\text{gap}(a_2,a_3)=166/1000`
— since `166<167`, Rule 2 matches `(a_2,a_3)`, scoring `83/500` — **and picks the minimum of
these two, `83/500 = 0.166`, which exceeds the target `e_2=1/7\approx0.142857` (exact check:
`83/500=415/2500` vs `1/7=357.14.../2500`, so `83/500>1/7` strictly, confirmed by cross-
multiplication `83\cdot7=581>500=500\cdot1`)**. This reconfirms Rule 2's failure with a fully
exact, minimal, hand-checkable example (superseding the round-3 decimal version — same
phenomenon, cleaner numbers): the objectively correct move targets the *larger* gap
(`a_1,a_2`) specifically because it happens to create an exact tie with `a_3`.

**5.3 Testing the outline's literal Form E' candidate — fails, as flagged by the cheap-kill
check.** The outline's Form E' (§4 above) reads `g(A,m)\le(a_1-a_2)+g(\{a_1-a_2\}\cup
\{a_3,\dots\},m-1)`. As literally written this **double-counts** `a_1-a_2` — the value
`a_1-a_2` is already an element of the residual multiset fed into `g`, so its contribution is
already reflected in `g(\text{residual},m-1)`; adding it again is not the value of "play
`M(a_1,a_2)` then continue" (that value is simply `g(\{a_1-a_2\}\cup\{a_3,\dots\},m-1)`, no
extra summand — confirmed directly from Lemma D/M's definition of the `M` operation and from
the certified exhaustive search agreeing with the un-added version, not the added one). Using
the corrected (non-double-counted) version, together with the outline's own proposed
"2nd-smallest-gap-of-the-residual, one level deeper" refinement, evaluated exactly on both
examples:

- **`A_2`, `m=2`:** the residual after `M(a_1,a_2)` is `(167/1000,167/1000)` — its own smallest
  (only) gap is `0`, giving the deeper bound `0+e_0\cdot0=0`. **Passes** (`0\le1/7`).
- **`A_1`, `m=3`:** the residual after `M(a_1,a_2)` is `(127/500,75/500,74/500)`; the deepest
  refinement tested (smallest-gap-of-that-residual `+ e_1\cdot(\text{rest})`) gives `13/150
  \approx0.0867`, and the plain-scalar fallback gives `69/875\approx0.0789` — **the corrected
  Form E', at every refinement level tried, gives at best `69/875>1/15\approx0.0667`. It
  FAILS.**

**Per the dispatch's cheap-kill instruction, this candidate is discarded, with the precise
diagnosis:** Form E' is permanently anchored to `M(a_1,a_2)` as the *mandatory* first move. But
`A_1`'s true optimal strategy uses `D(a_1)` (bisect) as its first move, a branch this specific
formula never considers at all (no amount of "deeper lookahead on the `M`-branch's residual"
can recover a fact that lives entirely in the sibling `D`-branch). **This is the critical
signal the dispatch asked to watch for** — the "2-level-lookahead" mechanism, taken literally
as scoped in the outline, does *not* correctly handle the very counterexample it was designed
to fix, once corrected for the arithmetic bug in its own statement.

**5.4 A broadened family — also refuted, with a self-caught methodological error along the
way (reported in full for honesty and to save the next round the same trap).** Reasoning that
Form E's failure was about *breadth* (only one branch considered) rather than *depth*, a
broadened candidate was built: at each of the first `\ell` levels, explicitly branch over
`3` named moves (`D(\text{top})`, `M(\text{top two})`, `M(\text{smallest-gap pair})`) — or, in
a further widened version, *every* legal D/M move — recursing on each residual; once `\ell`
levels are exhausted, fall back to the plain scalar bound `e_{m'}\cdot S(\text{residual})` at
whatever budget `m'` remains.

*The first implementation of this test had a bug that produced a false positive.* The initial
code computed, **at every level including the un-decremented top level**, `\min\big(e_{m}\cdot
S(A),\ [\text{branches}]\big)` — i.e. it included the *target itself* (evaluated at the
*current*, not yet reduced, budget `m`) as one of the candidates being minimized. This makes
the check **tautologically true by construction** (`\min(X,\dots)\le X` always), independent
of whether the branches do anything useful — so the resulting "0 failures across thousands of
random trials and hill-climbing adversarial search, `m=2` through `10`" was **vacuous, not
evidence of anything**. This was caught by re-deriving the exact trace on `A_1` and noticing
the reported winning "branch" was literally labelled `none (naive/e_of)` — i.e. the search
never used any operation at all. **This is recorded here explicitly as a warning for any
future round attempting a similar computational test: any inductive-hypothesis-based bound
check must apply the IH candidate only at a *strictly smaller* parameter than the one being
proved, never include the conclusion itself (at the same parameter) as a candidate in the
same `min`, or the test is vacuous.**

**Corrected test** (IH fallback only invoked after `\ell\ge1` real operations have already
been performed, i.e. only at strictly smaller `m`): re-run on both examples and via random
search:
```
levels=1: A_1(m=3) -> 261/3500 ≈ 0.0746 > 1/15 ≈ 0.0667   FAILS
levels=2: A_1(m=3) -> 37/500   = 0.074  > 1/15             FAILS
levels=3: A_1(m=3) -> 1/500    = 0.002  ≤ 1/15              passes (= full exhaustive search)
```
So `A_1` requires exploring the **entire** budget explicitly (`\ell=m=3`) before the bound
succeeds — the IH fallback is never legitimately reached with room to spare. Broader random
testing (300 trials each) at `m=3,4` with the 3-named-branch version, and separately with
**full-width branching** (every D and every M move explored, not just 3 named candidates) at
`\ell=1,2`:
```
3-branch,  m=3, levels=1: 42/300 fail (14%)      3-branch,  m=4, levels=1: 90/300 fail (30%)
3-branch,  m=3, levels=2:  3/300 fail (1%)        3-branch,  m=4, levels=3:  1/300 fail (<1%)
full-width, m=3, levels=1: 28/150 fail (19%)     full-width, m=4, levels=1: 40/150 fail (27%)
full-width, m=3, levels=2:  2/150 fail (1%)      full-width, m=4, levels=2: 18/150 fail (12%)
```
The failure rate does **not** shrink toward `0` as `m` grows for a *fixed* lookahead depth
(`m=4,` `\ell=2` fails on `12\%` of random trials, comparable to `m=3,\ell=1`'s `14\%`) — it is
the *ratio* `\ell/m` (roughly) that matters, not `\ell` alone. This is strong evidence
(computational, not a proof of impossibility, but consistent across two independent
branching-width choices) that **no fixed extra lookahead depth, independent of `m`, makes the
scalar IH fallback `e_{m-\ell}\cdot S(\cdot)` valid** — the mechanism needs `\ell` to grow with
`m`, at which point it is no longer a genuine inductive shortcut (it degenerates to running the
full exhaustive search, i.e. re-proving `g(A,m)\le e_m S(A)` from scratch at every `m` with no
reduction in work).

**5.5 Honest conclusion for this round.** The **induction-loading mechanism, in the concrete
form the outline proposed and in the natural broadenings tested here (more branches, more
levels, both separately and combined), is refuted as a route to closing Case (ii) at general
`m`.** The root cause, now precisely identified: `e_{m-1}\cdot S(\text{residual})` (the plain
scalar IH bound) is lossy in a way that is *not* repaired by a bounded number of extra
explicit levels — the information the bound is missing (which pair of elements will end up
tied, or nearly so, several operations from now) can be located arbitrarily deep in the
operation tree (confirmed concretely: `A_1` needs the *entire* `m=3` budget explored
explicitly). **This does not mean Case (ii) is false** — the D/M space itself continues to
contain a value beating the target at every point tested (now including the two counterexamples
plus hundreds of fresh random/adversarial trials) — it means a *correct proof* cannot take the
shape "cheap bounded lookahead, then invoke the same scalar claim recursively." A genuinely
different strengthening is needed: **the induction hypothesis itself would need to carry
non-scalar structural information about the residual forward through *every* level of the
induction (not just a bounded prefix)** — e.g. an explicit second potential function tracking
something like the sorted gap sequence, not merely `(e,S)`. No such richer *provable* IH shape
was found this round; this is now the sharpened open gap.

### 6. Round 5 — chain-prefix + exact static allocation (NEW skeleton, replaces the
induction-loading family as this file's primary Case (ii) mechanism)

**Target.** Prove `g(A,m)\le e_m\cdot S(A)` for every Case (ii) configuration `A` and every
`m`, via a **specific, explicitly-describable, non-adaptive strategy family** — not an adaptive
greedy walk (Rule 1/Rule 2, both dead) and not a bounded-lookahead-then-lossy-fallback scheme
(§4/§5, dead).

**Step 1 (define the family — mechanical, no new achievability lemma needed).** For an integer
`c` with `0\le c\le m`, define the **chain-prefix of length `c`**: starting from `A=(a_1\ge
a_2\ge\dots\ge a_k)`, apply `c` successive `M`-operations, each merging the *running top
result* against the next-largest untouched original element:
```
r_0 := a_1,   r_i := M(r_{i-1}, a_{i+1})  for i=1,\dots,c.
```
(Each step is literally an application of the certified `M` operation — Lemma D/M — so
achievability is automatic, no new lemma required.) This uses exactly `c` of XY's cuts and
leaves the multiset `\{r_c\}\cup\{a_{c+2},\dots,a_k\}` (size `k-c`) with `m-c` cuts remaining.

**Step 2 (the one-shot tail — a finite, non-adaptive optimization, exactly scoreable via Fact
3).** On the residual `\{r_c\}\cup\{a_{c+2},\dots,a_k\}` (size `k-c`, budget `m-c`), restrict to
**one-shot allocation**: every further operation acts only on the *original* `k-c` fixed
elements (never on a value produced by an earlier operation *within this phase* — no further
cascading). This is a finite combinatorial optimization (a partial matching + deletion problem
on `k-c` fixed numbers, `\le\binom{k-c}{2}` candidate operations), scoreable in closed form via
the certified **Fact 3** (block extraction, `lemmas/insertion-and-cascade-facts.md`) once the
matching/deletion pattern is fixed — take its **exact** minimum over the (finite) search space,
not a bound.

**Step 3 (the strategy and the conjecture).**
```
XY plays:  min_{0\le c\le m} [ value of chain-prefix-c, then exact one-shot-tail optimum ].
```
**Conjecture (numerically supported, NOT proved).** For every Case (ii) `A` and every `m`, this
quantity is `\le e_m\cdot S(A)`.

**Numerical evidence (this round, exact `fractions.Fraction`, not floats).**
- Re-derived both certified dead-end counterexamples independently (Rule 1's `m=3` example,
  Rule 2's `m=2` example) — both fail as documented; not re-litigated.
- **~650 fresh random Case-(ii) trials** (`m=2,\dots,6`; uniform random, boundary-focused
  `a_1\in[1.9a_2,2a_2)`, forced near-ties, one `m=6` spot check) — **zero failures** for the
  combined chain-prefix + one-shot-tail family.
- **All 3 known hard instances on file solved exactly**, including a new one found this round,
  `A=(23,12,6,3)`, `m=3` (target `44/15\approx2.933`; best *pure* one-shot value `3`, fails;
  true optimum `2`, requires a genuine 2-step cascade `M(23,12)=11\to M(11,6)=5`, giving
  `\{5,3\}`, `e=2` — reached by this family at `c=2`).
- **Observation (untested past `m=6`, flag for the builder to check early):** in every hard
  case found, the winning chain length `c` was small (`0`, `1`, or `2`), unlike the dead
  induction-loading family's pathology (needing the *entire* budget `\ell=m`). This is the key
  structural signal that this is not a repackaging of the dead mechanism, but it is untested
  for larger `m` — **re-run the search at `m=7,8` before investing in a general proof**, per
  this project's bounded-verification rule; if `c` is ever found to need to scale with `m`,
  report this immediately as a new dead end rather than pushing forward.

**Dead end found and recorded this round (do not re-propose): "pure one-shot allocation alone,
with NO chain-prefix" is insufficient by itself.** Concrete counterexample:
`A=(23,12,6,3)`, `m=3` — the best value achievable by ANY one-shot (non-cascading) allocation
of all 3 cuts is `3`, which **fails** the target `44/15\approx2.933` (`3>44/15`); the true
optimum `2` strictly requires cascading (matching `23,12\to11`, THEN matching `11,6\to5`) — a
genuine 2-deep chain. So the chain-prefix component of Step 1 is load-bearing, not an
optional simplification; any future attempt must keep both components.

**Step 4 (the concrete next task — an exchange/rearrangement conjecture on the one-shot
sub-problem, NOT verified this round).** To turn Step 3 into a closed-form bound (rather than
"search a finite space and take the min," which does not scale to a general-`m` proof by
itself), conjecture that the one-shot tail's optimal matching/deletion pattern is always
**sorted-adjacent** (matches and deletions only ever pair/act on consecutive ranks in the
sorted residual, never "crossing" — this is the natural rearrangement-inequality-style
structure, and if true it collapses the search from exponentially many matchings to `O(k-c)`
candidates, directly computable via Fact 3). **This is the single most concrete, cheaply
checkable next step**: before attempting a general proof, the builder should verify the
adjacency conjecture by brute force on the ~15 hardest instances already on file across all
approach files (small, bounded, reuses existing data — no new search needed) and report
pass/fail. If it holds, Fact 3 turns Step 2's search into a closed-form expression in
`a_1,\dots,a_k,c`, making Step 3's minimization over `c\in\{0,\dots,m\}` a genuinely tractable
1-parameter optimization, analogous in shape to how Case (i)'s form-A closure (§2d,
`dyadic-cascade-induction.md`) reduced to a single-variable min-of-monotone-functions argument.
If the adjacency conjecture fails on any of the 15 instances, report the counterexample
precisely (which non-adjacent pairing beats every adjacent one) — this would itself be a
useful negative result narrowing the search further.

**Secondary opening, not developed this round (flag only).** A majorization/Schur-convexity
argument (`e(M)` appears Schur-convex in `M` under majorization on the small examples checked)
was flagged by this round's explorer as a possibly-richer, vector-valued invariant, distinct
from the already-dead scalar `\Phi(M,r)=S(M)/(2^{r+1}-1)` (`concavity-minimax-duality.md`
§9) — not pursued this round, noted here in case Step 4's adjacency conjecture fails and a
richer invariant is needed instead.

**Why this is not a repackaged induction-loading scheme (explicit, since that is now a
confirmed dead end for this file — see the boxed warning at the top).** Induction-loading's
failure mode was structural: after a *bounded* explicit prefix, it fell back to the *lossy*
scalar bound `e_{m'}\cdot S(\text{residual})`, and the required prefix depth to make that
lossy bound valid was shown (round 4, §5.4) to scale with the *entire* remaining budget, not a
constant — an unfixable defect in that specific shape. This family has **no lossy fallback
anywhere**: the tail is scored by its own EXACT optimum over a fully-specified (if restricted)
finite search space, and `c` ranges over the whole `0,\dots,m`, so nothing is being bounded
away — only an achievability CLAIM about a specific, non-exhaustive strategy family is being
made, which is a difference in kind, not merely a cosmetic change to the failed shape.

**Open gaps for the next builder, in priority order:** (1) check the sorted-adjacency
conjecture (Step 4) on existing hard instances — cheap, decisive; (2) if it holds, derive the
closed-form expression via Fact 3 and attempt the 1-parameter (`c`) minimization directly; (3)
re-run the numerical search at `m=7,8` to confirm `c` stays bounded (cheap-kill per the
explorer's own flag); (4) if either (1) or (3) fails, report the precise counterexample as a
new, specific dead end (do not silently abandon — record exactly what broke).

### 7. Round 5 — the Slack Collapse lemma, and the fate of §6's Step 4 (sorted-adjacency)

All computations in this section are exact (`fractions.Fraction` / plain integers), no floats,
independently re-runnable (code kept in this round's scratch files, logic reproduced in full
below so the write-up is self-contained).

#### 7.1 The Slack Collapse lemma (proved in full — new, general-purpose, promotable)

**Lemma (Slack Collapse).** Let `A=(a_1≥…≥a_k)` be any sorted multiset of nonnegative reals
(no Case (i)/(ii) restriction) with `k≤m`. Then Xiang Yu can force `e(\text{final})=0` using
`≤m` cuts. Consequently, `g(A,m)=0≤e_m·S(A)` for every such `A` — this sub-case is **trivial**
and needs no induction, no chain-prefix search, and no case split at all.

*Proof.* Immediate from the already-certified **Fact 5** (chain-cancellation,
`lemmas/insertion-and-cascade-facts.md`): applying Fact 5 to the multiset `\{a_1,\dots,a_k\}`
itself (`L:=k`) gives an explicit sequence of exactly `k` physical cuts producing a final
multiset with `e=0`. Since `k≤m`, Xiang Yu has enough cuts available (using exactly `k` of his
`≤m`, the remaining `m-k` simply unused — legal since the problem only requires "at most `n`"
points). `e_m·S(A)≥0$ always (`e_m>0`, `S(A)≥0`), so `0≤e_m·S(A)` trivially. ∎

**Corollary (reduction of the whole upper-bound induction to `k=m+1`).** Fix any level `m` of
the upper-bound induction (Case (i) or Case (ii), no distinction needed here). If `k<m+1`
(equivalently `k≤m`), the Slack Collapse lemma closes this configuration **immediately**,
independent of which case it falls into and independent of the specific values `a_1,\dots,a_k`.
Hence **the only configurations that require any further argument at level `m` are those with
`k=m+1` exactly** — i.e. Liu Bang has used the maximum number of marks available to him at this
level (no "wasted" marks anywhere in the recursion). This was not previously stated explicitly
anywhere in the population (checked directly: `grep -n` across every `approaches/*.md` file for
`k=m+1`/`k<m`/`slack budget`-type phrasing returned nothing before this round) — it is a
genuine, general simplification, reusable by `dyadic-cascade-induction` as well as this file
(both cases benefit, not just Case (ii)), and is proposed for certification below.

**Verification.** This is a direct one-line corollary of a lemma already certified and
independently re-verified twice (rounds 4); no new computation is strictly required, but as a
sanity check the exact search harness built this round (`family_value`/`g_exact` in
`/tmp/round-5/work/dm.py`) was run on 30 fresh random configurations with `k<m` at
`m=3,\dots,7` and confirmed `g_exact(A,m)=0` in every case, matching the lemma exactly.

**Scope note (honest).** This closes an entire *regime* of configurations (all "slack" ones)
but does **not** touch the genuinely hard case `k=m+1`, which is exactly where every
counterexample on file (Rule 1's, Rule 2's, the `(23,12,6,3)` instance, all three at this
round's new counterexamples below) already lives — i.e. the hard case was already implicitly
being tested at `k=m+1` throughout this file's history; this lemma makes that fact explicit and
provable, narrowing (not yet closing) the target.

#### 7.2 The literal "sorted-adjacency" conjecture (§6 Step 4) is FALSE

**Independent stress test (fresh, not reusing the outline's own instances).** Using an
independently-built exact-integer search harness (`/tmp/round-5/work/stress.py`), 160 random
Case (ii) configurations (`m=2,\dots,5`, integer entries, denominators `20,50,100`) were tested,
comparing the **unrestricted** one-shot-tail exhaustive search (every matching, crossing or not,
plus deletions) against the **adjacent-rank-only** restricted search (matched pairs must be
literal sorted-order neighbors `(i,i+1)`, no skipping). Result: the *family value* (min over
`c`) using the unrestricted tail search met the target `e_m S(A)` in all 160 trials (0
failures — reconfirms §6's own headline claim, independently), but the *adjacent-only*
restriction **disagreed with the unrestricted search in 6 of the 160 trials**, always by giving
a strictly *worse* (larger) value. Two exact minimal counterexamples, verified by hand:

```
A = (82,66,47,40),  m=3  (k=4=m+1, Case (ii): 82<132=2·66).
  target = e_3·S = (1/15)·235 = 47/3 ≈ 15.667.
  Chain-prefix c=0, unrestricted one-shot tail, budget 3: BEST = 5
    (achieved by matching (82,47)→35, DELETING 66, keeping 40 untouched:
     final multiset {40,35}, e = 40-35 = 5).
  Chain-prefix c=0, adjacent-rank-only tail, budget 3: BEST = 7
    (adjacent-only can only pair (82,66), (66,47), or (47,40) as arcs, no
     skipping over an interior point; the exhaustive adjacent-only search's
     actual optimum uses NO match at all, only 2 deletions — delete 82 and
     66 [2 of the 3 ops, 1 unused], keeping 47 and 40 untouched: final
     {47,40}, e=47-40=7. Every adjacent-pairing alternative tested by the
     same search scores worse than 7, e.g. matching (66,47)→19 with 82,40
     kept untouched gives final {82,40,19}, e=82-40+19=61.)
  Both 5 and 7 are ≤ target 47/3≈15.67, so §6's mechanism is UNAFFECTED here —
  but the *adjacent-only* restriction is strictly suboptimal (7>5), refuting
  the literal Step-4 conjecture that adjacency always suffices to reach the
  TRUE one-shot-tail optimum.
```

The winning (non-adjacent) selection above pairs original ranks `1` and `3` (values `82,47`)
while *deleting* the intervening rank-`2` element (`66`) — i.e. the optimal matching "skips
over" a deleted point. This is not visible to a search restricted to literal `(i,i+1)`
adjacency, because deletion of an interior element is exactly what makes the two flanking
elements "adjacent" *after* deletion, not before. **Conclusion: the literal sorted-adjacency
conjecture as stated in §6 Step 4 is FALSE.** Per this round's dispatch instruction, this is
reported honestly as a negative result rather than forced through.

A second exact counterexample (found in the same search, useful as an independent check):
`A=(46,44,31,21,15)`, `m=4` (`k=5=m+1`, `44<92`): target `=e_4·S=157/31≈5.06`; unrestricted
one-shot tail at `c=0` achieves `0` exactly (pairing `(46,31)→15`, deleting `44` and `21`,
keeping `15`: final `{15,15}`, exact tie, `e=0`); adjacent-only achieves only `2` at the same
budget (still `≤` target, but again strictly worse than the true one-shot optimum, confirming
the pattern is not a one-off).

#### 7.3 A corrected, more general replacement conjecture: non-crossing matching

**Observation.** In both counterexamples above, the winning selection, while not
*adjacent*-only, *is* **non-crossing**: drawing an arc for each matched pair and a point for
each surviving/deleted singleton, no two arcs' index-intervals properly overlap (a pair `(i,j)`
and a pair `(i',j')` with `i<i'<j<j'` never both occur; nesting `i<i'<j'<j` and disjointness
`j<i'` are both allowed, and arcs may "skip over" deleted or kept singleton points freely).

**Refined conjecture (numerically supported, NOT proved — replaces §6 Step 4).** For every
sorted `Y` and budget `b`, the one-shot tail's exact optimum (over ALL matchings + deletions,
crossing or not) is always attained by some **non-crossing** matching+deletion selection.

**Verification performed this round.** An independent exact search restricted to non-crossing
matchings (standard recursive enumeration: for the leftmost point, either leave it unmatched
and recurse on the rest, or pair it with some point `k` places later and recurse independently
on the "inside" and "outside" sub-intervals — this is the classical non-crossing-partition
recursion) was implemented and run against the **full unrestricted** exhaustive search:
- Both counterexamples from §7.2 above: non-crossing search reproduces the unrestricted
  optimum EXACTLY (`5` and `0` respectively, not the worse adjacent-only values `7` and `2`).
- **160 fresh random Case (ii) trials** (`m=2,\dots,5`, independent RNG seed from §7.2's own
  search): **zero mismatches** between the non-crossing-restricted search and the full
  unrestricted search, at every single trial (not just where the family already beat target —
  literally the two search values agreed exactly on all 160 instances).
- **400 further generic trials** (not restricted to Case (ii) or to `k=m+1`; `p=2,\dots,7`
  elements, budget `b` random in `0,\dots,p`, integer denominators up to `60`): again **zero
  mismatches** — this extends the check well beyond the original scope (arbitrary sorted
  multisets and budgets, not tied to the game's specific `a_1<2a_2`/tight-`k` structure at all),
  making the conjecture's numerical support substantially broader than what the outline itself
  tested.

**A natural proof attempt was tried and FAILED — recorded so it is not retried.** The obvious
route to proving the conjecture is a **local uncrossing exchange argument**: if a selection
contains two crossing pairs `(i,k)` and `(j,l)` (indices `i<j<k<l`, so `Y_i\ge Y_j\ge Y_k\ge
Y_l`), show that replacing them by the nested pairing `(i,l),(j,k)` or the disjoint pairing
`(i,j),(k,l)` — **holding every other element of the selection fixed** — never increases `e`.
This was tested directly (3000 random trials, `p=4,\dots,8`, both alternative
re-pairings, arbitrary fixed "rest") and **is FALSE**: an explicit counterexample,
`Y=(43,33,20,16,11,8,2)`, indices `(0,3,4,6)` (values `43,16,11,2`), no deletions among the
remaining `\{33,20,8\}`: the crossing pairing `(43,11)\to32,(16,2)\to14` gives `e=15`
(`\{33,32,20,14,8\}`), while **both** alternatives are strictly worse — nested
`(43,2)\to41,(16,11)\to5` gives `e=25`, and disjoint `(43,16)\to27,(11,2)\to9` gives `e=25`
too. So a *local* uncrossing move, with the rest of the selection frozen, can strictly
*increase* `e` — **this specific proof technique cannot work**, and should not be re-attempted
in this form. (Interestingly, this does not refute the *global* conjecture: re-solving the
*full* one-shot problem on this exact `Y` at the matching budget, `b=2`, gives `7` — strictly
better than the crossing pairing's local value of `15` — via a *different* non-crossing
selection that also changes what happens with the "rest," confirmed by direct exhaustive
computation, `full=non-crossing=7` at `b=2`, matching exactly across all budgets `b=0,\dots,6`
tested on this `Y`. So the global conjecture survives this specific adversarial construction,
but only because a genuinely different global rearrangement compensates — any future proof
attempt must be global, not a pairwise local exchange.)

**Honest status.** This is a strictly more general, numerically well-supported candidate to
replace the false Step 4 with — non-crossing matchings are a natural "no distant swapping"
structure (the classical setting for rearrangement-inequality-style arguments, and the
underlying search space is Catalan-sized rather than exponential-in-all-matchings, so a genuine
DP/induction proof is plausible) — but **it has NOT been proved**, only tested. If it holds in
general, it would let a future round attempt an exchange-argument proof (a non-crossing
matching can be built by a greedy left-to-right or divide-and-conquer scan, which is a much
more tractable target for induction than "the arbitrary global matching optimum"). If it fails
on some larger instance, that failure should be reported precisely (which crossing pair beats
every non-crossing alternative), per this round's dispatch guidance on honest negative results.

#### 7.4 "Full chain alone" is also insufficient (confirms the family's two-component structure
is load-bearing)

As a further test of whether §6's mechanism could be *simplified* rather than *proved* as
stated, "always take the maximal chain-prefix `c=k-1` and never search a separate one-shot tail"
was tested directly (no tail phase at all — the whole budget spent on one serial chain).
**This fails too**, with many exact-integer counterexamples even restricted to the tight regime
`k=m+1` isolated by the Slack Collapse lemma (§7.1):
```
A=(33,19,5), m=2 (k=3=m+1, Case (ii): 33<38):
  target = e_2·S = 57/7 ≈ 8.14.
  Full chain: r_1=M(33,19)=14, r_2=M(14,5)=9.  e=9 > 57/7.  FAILS.
  But the family (chain-prefix search over c=0..2) succeeds at c=0
  (one-shot tail alone on the original 3 elements, budget 2, achieves 5 ≤ 57/7).
```
Combined with the already-recorded dead end that "pure one-shot alone, with NO chain-prefix" is
*also* insufficient (round 5's own §6, instance `A=(23,12,6,3)`), this confirms: **neither
extreme of the family (chain-only, or one-shot-only) suffices by itself; the mechanism's power
genuinely comes from searching the full range `c=0,\dots,m` and combining both components**,
exactly as §6 originally specified. This is a negative sub-result about a possible
*simplification*, not a threat to the family itself — recorded so a future round does not
waste time re-testing either extreme alone.

#### 7.5 Net assessment for this round

- **Genuine new proved content:** the Slack Collapse lemma (§7.1), reducing the *entire*
  upper-bound induction (both cases, every `m`) to the tight sub-case `k=m+1` — a clean,
  reusable, certifiable result.
- **One conjecture tested and refuted, honestly reported:** §6's literal "sorted-adjacency"
  Step 4 (§7.2), with exact minimal counterexamples.
- **One corrected, more general replacement conjecture proposed and numerically supported (not
  proved):** non-crossing matching+deletion suffices for the one-shot tail's exact optimum
  (§7.3) — extended to 560+ trials total (the original 160 Case-(ii) trials plus 400 further
  generic ones, `p` up to `7`, arbitrary budgets), zero mismatches — this is the concrete next
  target for a future round.
- **One proof technique tested and ruled out for the non-crossing conjecture:** the natural
  *local* uncrossing/exchange argument (repair one crossing pair at a time, holding the rest of
  the selection fixed) is **FALSE** (§7.3, exact counterexample) — any future proof of the
  non-crossing conjecture must be genuinely global (e.g. a direct DP/induction on the
  non-crossing-partition recursion comparing full sub-problem optima, not a pairwise swap
  lemma). This narrows the search for a proof technique, the same way round 3/4's negative
  results narrowed the search for a correct policy.
- **One further simplification tested and refuted:** "chain alone, no tail" is insufficient
  even restricted to the now-isolated tight case `k=m+1` (§7.4) — confirms the family's two
  components are both necessary.
- **What remains open:** a full proof (not just extensive exact-fraction/integer numerical
  support) that `\min_{0\le c\le m}[\text{chain-prefix-}c + \text{exact one-shot tail}]\le
  e_m\cdot S(A)$ for every Case (ii) `A` with `k=m+1` (the now-isolated hard case) and every
  `m` — either directly, or via first proving the non-crossing conjecture (§7.3) and then a
  closed-form Fact-3-based argument on the resulting Catalan-structured search space. Neither
  was completed this round; this is now the sharpened, precisely-scoped open gap.

## Full proof
(not present — Status is `partial`. Round 7 (see §9 below) fully closed §8 Steps 1-2, refuted
§8/§7.3's general "non-crossing matching+deletion" conjecture with an exact counterexample, and
proposed + numerically re-supported (not proved) a correctly-rescoped replacement restricted to
the budget `b=p-1` that the proof actually needs. Round 8 (§11) fully proved the general
Extreme-Element Peeling Lemma — the exact three-way `DELETE`/`KEEP`/`MATCH` decomposition of
`OPT(Y,b)`/`NC(Y,b)` for every `Y,b` — reducing the whole remaining gap to a single precisely-
stated (and corrected: the natural per-partner form is proved FALSE, the aggregated form is the
right target) Small-Gap Crossing-Domination Lemma, still open. The central mechanism gap remains
open, now narrowed further and more precisely scoped than at the start of any prior round.)

## Promotable lemmas

**Lemma (Two-Variable Reflection Bound) — new round 19, full proof, submitted for certification
(§33.1; proposed file `lemmas/two-variable-reflection-bound.md`).**

*Statement.* For `0\le b_0\le w_1` and `0\le w\le w_1`: `w_1-|b_0-w|\ge|b_0-(w_1-w)|`.

*Proof.* Three exhaustive cases on the sign of `b_0-w` (and, when `b_0>w`, on the sign of
`b_0-(w_1-w)`): (1) `b_0\le w`: LHS `=(w_1-w)+b_0\ge|b_0-(w_1-w)|` by `p+q\ge|p-q|` for `p,q\ge0`. (2)
`b_0>w,\,b_0\le w_1-w`: LHS`-`RHS`=2w\ge0`. (3) `b_0>w,\,b_0>w_1-w`: LHS`-`RHS`=2(w_1-b_0)\ge0`. Full
derivation: §33.1. `0` failures across a `462`-tuple exhaustive grid, `19{,}894`-trial random sweep,
and two `100\%`-failure negative controls confirming both hypotheses are load-bearing
(`/tmp/round-19-build/verify_32.py`).

**Corollary — Two-Touch is fully, unconditionally proved for `|W|\le3` (new round 19, full proof,
§33.5; supersedes the round-18 REJECTED overclaim above, this time with every ingredient actually
proved, not corroborated).**

*Statement.* For every `C` with `|C|\le1` and every `W` with `|W|\le3`:
`\mathrm{OPT}_{+1}(C,W)=\mathrm{TwoTouch}(C,W)`.

*Proof.* `C=\emptyset`: free at every `W` via the certified Empty-Background Lemma. `C=\{b_0\}`,
`|W|\le2`: certified base case (Three-Bound Domination Lemma / trivial). `C=\{b_0\}`, `|W|=3`: the
DELETE/KEEP/MATCH trichotomy's three branches are each `\ge\mathrm{TwoTouch}(\{b_0\},W)` — DELETE via
the base case plus candidate-list-inclusion; KEEP via the certified `b_0>w_1` unconditional formula
together with (for `b_0\le w_1`) target (*) proved in §33.3, using the certified Lemma B; MATCH via the
certified Match-Branch-Domination-via-Per-Partner-Domination Lemma, with Per-Partner Domination's
dependency fully discharged at `q=|W|=3` (already certified unconditionally). Combined with the free
reverse inequality, equality holds. Full derivation: §33.5.

**Lemma (Match-Branch-Domination-via-Per-Partner-Domination) — new round 18, full proof, CERTIFIED this
round in narrowed form (§30.1; `lemmas/match-branch-domination-via-per-partner-domination.md`).
[ROUND-18 PROOF-REVIEWER: the "Consequently…Two-Touch…fully proved for `|W|\le3`" clause below was in
the builder's original submission and is REJECTED — not established, see the §30.1 correction note
above. Only the `MATCH_j\ge TT` statement is certified.]**

*Statement (certified part only).* For a Two-Touch peeling instance `(\{b_0\},W)`, `w_1:=\max(W)`,
`\mathrm{rest}:=W\setminus\{w_1\}`, `d_j:=w_1-w_j` for `w_j\in\mathrm{rest}`,
`MATCH_j:=\mathrm{OPT}_{+1}(\{b_0,d_j\}, \mathrm{rest}\setminus\{w_j\})`,
`TT:=\mathrm{TwoTouch}(\{b_0\},W)`: conditional only on Gap 1a's Per-Partner Domination Lemma (`\lemmas/`,
certified `q\le3`, open `q\ge4`) at the specific size `|W|` and index `l=j`, `MATCH_j\ge TT` for every
`j`. **(NOT certified: "Consequently, Two-Touch is unconditionally, fully proved at `|W|\le3`" — this
additionally needs the KEEP `b_0\le w_1` sub-case, which is not established by this Lemma or by Lemma B;
remains open, strongly corroborated only.)**

*Proof.* The renaming `B_0:=\{b_0\}`, `Z_0:=W`, `l:=j` identifies `MATCH_j` with Per-Partner
Domination's own `A_{3,l}` literally (not by analogy). Two already-certified facts bound both terms of
`\min(A_1,D_j)` below by `TT`: `A_1$ (`=` Two-Touch's DELETE branch) `\ge TT` by the already-certified
strong induction (§26.5(b)); `D_j:=|b_0-d_j|\ge TT` trivially, since `e(\{b_0,d_j\})` is by definition
one member of `\mathrm{TwoTouch}`'s own candidate list, so the closed form's own value (a `\min` over
that list) cannot exceed it. Hence `\min(A_1,D_j)\ge TT`, and Per-Partner Domination at `l=j` gives
`MATCH_j\ge\min(A_1,D_j)\ge TT`. `\blacksquare` Full derivation, the `|W|\le3` corollary, and the precise
scope of the residual dependency (Per-Partner Domination's own open `q\ge4` gap): §30.1. **General, no
`\mathcal F`-provenance needed anywhere in the proof** — Per-Partner Domination itself is stated (§21.3)
"with no trigger hypothesis and no requirement that `l` be an argmin of anything," and F1/F2 are likewise
provenance-free.

**Lemma A (Max-Element Triple Identity) — new round 17, full proof, submitted for certification
(`lemmas/max-element-triple-identity-and-threetouch-basecase.md`, §28.4(a)).**

*Statement.* For nonnegative reals `a,b,c` with `a=\max(a,b,c)`: `e(\{a,b,c\})=a-|b-c|`.

*Proof.* WLOG `b\ge c`; sorted order is `(a,b,c)`, so `e(\{a,b,c\})=a-b+c=a-|b-c|`. `\blacksquare`
Fully general, unconditional, `0/1854` fresh trials.

**Lemma B (Three-Touch's Base Case, `|W|\le3`) — new round 17, full proof, submitted for
certification (same file, §28.4(a)).**

*Statement.* `\mathrm{OPT}_{-1}(\{c\},W)=\mathrm{ThreeTouch}(c,W)` for every `c\ge0`, `|W|\le3` (see
§27.2(d) for `\mathrm{ThreeTouch}`'s definition).

*Proof.* For `|W|\le2` every selection is already a literal `\mathrm{ThreeTouch}` candidate. For
`|W|=3` the one exceptional selection ("keep all three") is dominated by an explicit candidate via a
4-way case split on the rank of `c` among `W`'s sorted values, using Lemma A three times (two of the
four cases give exact equality). Full derivation: `lemmas/max-element-triple-identity-and-threetouch-
basecase.md`. Closes only the base case of the larger open Three-Touch induction (§28.4).

**Lemma (Sum-Bound Base Case) — new round 16, full proof, CERTIFIED this round
(`lemmas/sum-bound-base-case.md`, §26.1).**

*Statement.* At a genuine `q=3` `\mathcal F` base-generator instance with trigger `M<A_1` and `h=0` at
`k^*` (`b_0<w_1$, `d_{k^*}<w_1`): `M=D_{k^*}` exactly.

*Proof.* Contradiction: assume `2D_{k^*}>w_1`; combine the trigger with `A_1\le b_0` (Shrink-List
Corollary) and `A_1\le w_1-b_0` (§21.1 Step 1 `(†)`) to force both `w_1<D_{k^*}+b_0` and
`D_{k^*}>b_0`; the latter pins `D_{k^*}=d_{k^*}-b_0` exactly, and substituting gives `w_1<d_{k^*}`,
contradicting `h=0`'s own `d_{k^*}<w_1`. Full derivation: `lemmas/sum-bound-base-case.md`. Closes
Gap 1b's `\mathrm{rest}=\emptyset` base case only — the general `|Z_1|\ge2` induction remains open.

**Lemma (Insertion-Difference Identity) — new round 16, full proof, CERTIFIED this round
(`lemmas/insertion-difference-identity.md`, §26.2).**

*Statement.* For any multiset `M` of nonnegative reals and `d\ge0`, writing `h:=\#\{m\in M:m>d\}`,
`\mathrm{tail}_d:=\{m\in M:m\le d\}`: `e(M\cup\{d\})-e(M)=(-1)^h(d-2e(\mathrm{tail}_d))`.

*Proof.* Split `M` via Fact 3 into `\mathrm{head}_d\sqcup\mathrm{tail}_d`; extract `d` from
`M\cup\{d\}` at its rank `r=h+1` via the General Rank-Extraction Identity; eliminate
`e(\mathrm{head}_d)` between the two resulting equations. Fully general, no `\mathcal F`-provenance.

**Lemma (Delete-Suffices Insertion Domination) — new round 16, full proof, CERTIFIED this round
(`lemmas/delete-suffices-insertion-domination.md`, §26.3).**

*Statement.* If `\mathrm{OPT}_{+1}(C,W)=e(C)` (deletion suffices), then for any `w_a,w_b\in W`,
`e(C)\le e(C\cup\{|w_a-w_b|\})`.

*Proof.* "Match `w_a,w_b`, delete the rest" is one candidate for `\mathrm{OPT}_{+1}(C,W)`'s own
minimization, value `e(C\cup\{|w_a-w_b|\})`; since the minimum equals `e(C)` by hypothesis,
`e(C)\le e(C\cup\{|w_a-w_b|\})`. Two lines, fully general. **Application**: gives a full,
unconditional closure of Gap 1c's `\xi^*=\emptyset` boundary case whenever Gap 1a's Deletion-
Suffices-for-`k^*` holds (already proved `q\le3`) — a new link between the two gaps, §26.3.

**Lemma (Background-Release Domination, STRENGTHENED) — new round 15, full proof, promotable
(§24.4).**

*Statement.* For any background `C` (`|C|\ge1`), list `W`, `y\in C` (`C':=C\setminus\{y\}`):
`\mathrm{OPT}_{+1}(C,W)\ge\mathrm{OPT}_{+1}(C',W\cup\{y\})`, and dually
`\mathrm{OPT}_{-1}(C,W)\le\mathrm{OPT}_{-1}(C',W\cup\{y\})`. No `\min`/`\max`-with-`e(C)` cap needed
(strengthens the round-15-outline's originally-proposed, weaker capped form).

*Proof.* One-line search-space-inclusion argument, same shape as the certified Shrink-List
Monotonicity Lemma: `\mathrm{OPT}_{+1}(C,W)` equals the optimum of `\mathrm{OPT}_{+1}(C',W\cup\{y\})`
restricted to the sub-space of selections where `y` is forced kept; minimizing over a sub-space is
`\ge` minimizing over the full space. Full derivation: this file, §24.4. Independently verified
`0/18{,}000` (`\sigma=+1`) and `0/18{,}000` (`\sigma=-1`) fresh exact-`Fraction` trials
(`|C|=1$–`4`, `|W|=0$–`4`). General-purpose, no `\mathcal F`-restriction — reusable by any approach
reasoning about moving a background element into/out of a free list.

**Lemma (Three-Bound Domination) — new round 15, full proof, promotable (§24.2).**

*Statement.* For any nonnegative reals `x,y,z`: `\min(x,|x-y|,|x-z|)\le
e_{\mathrm{sorted}}(\{x,y,z\})` (`=\max-\mathrm{mid}+\min`).

*Proof.* Exhaustive 3-way case split on the rank of `x` among `\{x,y,z\}`; full derivation this
file, §24.2. Independently verified `200{,}000/200{,}000` fresh trials on fully arbitrary
`(x,y,z)$, plus `59{,}844` trials on the specific `q=4` construction it was found to resolve
(confirming the "keep both `\mathrm{Res}` elements" candidate bound is never independently useful,
always dominated by the simpler "delete-all-but-one" family). General-purpose elementary fact about
`e_{\mathrm{sorted}}` of a 3-element multiset, reusable wherever a "keep-two" candidate bound is
being considered against simpler "keep-one" alternatives.

**Lemma (Keep-Top Bound) — new round 15, full proof, promotable (§24.3).**

*Statement.* At any `(C,W,+1)$ with `C=\{c_1,c_2\}`, `h=0` (`c_1,c_2<w_1:=\max(W)`):
`\mathrm{OPT}_{+1}(C,W)\le w_1-|c_1-c_2|`.

*Proof.* One-line: "keep `w_1`, delete the rest of `W`" is a valid candidate selection, giving
`\mathrm{OPT}_{+1}(C,W)\le e_{\mathrm{sorted}}(\{c_1,c_2,w_1\})=w_1-|c_1-c_2|` (since `h=0` makes
`w_1` strictly dominant). Full derivation this file, §24.3. Holds for any `q`, not just the
`\mathrm{rest}=\emptyset` base case it was found to sharpen — general-purpose, no `\mathcal
F`-restriction beyond the `h=0` domination hypothesis (which is itself already a standing hypothesis
throughout the Sum Bound's own scope).

**Lemma (General Rank-Extraction Identity) — new round 9, full proof, promotable.**

*Statement.* For a sorted multiset `F`, an element `x\in F` at sorted rank `r` (`1`-indexed),
`\text{head}` = the `r-1` elements of `F` ranked above `x`, `\text{tail}` = the elements ranked
below `x`:
```
e(F) = e(\text{head}) + (-1)^{r-1} x + (-1)^r e(\text{tail}).
```
*Proof.* Two applications of the already-certified Fact 3 (block extraction): first split
`F=\text{head}\sqcup(\{x\}\cup\text{tail})`, then `\{x\}\cup\text{tail}=\{x\}\sqcup\text{tail}`.
Full derivation: this file, §13.1, round 9. Generalizes Fact 3 (its `r=1` special case).
Independently verified `3000/3000` exact-integer random trials. Certified as
`lemmas/general-rank-extraction-identity.md`. Reusable by any approach extracting a general-rank
(not just maximum) element from a sorted multiset with an exact sign/offset — used this round to
resolve the "KEEP-branch order case split" of a multi-background Extreme-Element Peeling Lemma
(§13.2), where the peeled element is not always the working multiset's global maximum.

**Lemma (Extreme-Element Peeling) — new this round, full proof.**

*Statement.* Let `Y=(y_1\ge\dots\ge y_p)` be any sorted list of nonnegative reals, `b\ge0` any
budget. With `OPT`, `NC`, `MAXOPT`, `MAXNC` as formalized in §9.2/§11.1 (finite minima/maxima of
`e` over one-shot selections, resp. non-crossing-restricted ones), and `INSERT_OPT`/`INSERT_NC`
as defined in §11.1 (a fixed external value `v^\dagger` inserted into a sub-list's own selection
value, `v^\dagger` itself never touchable by the sub-selection):
```
OPT(Y,b) = min( OPT(Y\{y_1},b-1) [if b\ge1],
                 y_1 - MAXOPT(Y\{y_1},b),
                 min_{j=2}^p INSERT_OPT(y_1-y_j, Y\{y_1,y_j}, b-1) [if b\ge1] ),
```
and identically with every `OPT`/`MAXOPT`/`INSERT_OPT` replaced by `NC`/`MAXNC`/`INSERT_NC`.

*Proof.* This file, §11.2 above, round 8. A case split on index `1`'s fate (deleted / kept /
matched to some `j`) is exhaustive and mutually exclusive by definition of "selection." The
DELETE and KEEP branches are each proved by an explicit bijection of selections (deleting index 1
from `D`, resp. peeling index 1 out of `K` and applying the certified Fact 3 block-extraction
identity with `X=\{y_1\}` a singleton — valid since `y_1=\max(Y)` remains the max of any
combined multiset built from the rest). The MATCH branch is proved directly from the raw
definition of a selection's value (no further identity needed for `OPT`; for `NC`, the already-
certified Non-crossing inside/outside independence lemma is invoked to show that "non-crossing
overall, with `(1,j)` matched" is exactly equivalent to "the residual sub-selection on
`Y\{y_1,y_j}` is itself non-crossing AND has no pair spanning the inside/outside split at `j`" —
precisely `INSERT_NC`'s defining conditions). Full derivation, all four sub-cases, in §11.2.

*Where proved:* this file, §11.2, round 8. General-purpose (holds for every `Y,b`, not just
`b=p-1`); self-contained modulo the already-certified Fact 3 and Non-crossing inside/outside
independence lemma (both already certified/promotable from round 7). Independently spot-checked:
the full three-branch decomposition reproduces direct exhaustive `OPT`/`NC` computation exactly
on 420+420 fresh random trials, `p=1,\dots,7`. Reusable by any future attempt at the
`OPT(Y,p-1)=NC(Y,p-1)` program (isolates the entire remaining difficulty into the single MATCH
branch, i.e. into the — now precisely, correctly restated — Small-Gap Crossing-Domination Lemma,
§11.4) and, more generally, by any approach needing an exact (not approximate) reduction of a
one-shot selection optimization by its extreme element.

**Lemma (Slack Collapse) — new this round.**

*Statement.* Let `A=(a_1≥…≥a_k)` be any sorted multiset of nonnegative reals (no restriction
to Case (i) or Case (ii)) with `k≤m`. Then Xiang Yu can force `e(\text{final})=0` using `≤m`
cuts; consequently `g(A,m)=0≤e_m·S(A)` trivially. Equivalently: **the entire upper-bound
induction, at every level `m`, both Case (i) and Case (ii), reduces to the single tight
sub-case `k=m+1`** — every configuration with `k<m+1` is disposed of immediately, with no
casework and no invocation of any inductive hypothesis.

*Proof.* Immediate corollary of the already-certified **Fact 5** (chain-cancellation,
`lemmas/insertion-and-cascade-facts.md`): apply Fact 5 to `\{a_1,\dots,a_k\}` with `L:=k`,
giving an explicit sequence of exactly `k` physical cuts producing `e=0`. Since `k≤m`, Xiang Yu
has `≤m` cuts available and uses exactly `k≤m` of them (the rest simply unused, which is legal
since the problem only requires "at most `n`" marked points, not exactly `n`). Since
`e_m>0` and `S(A)≥0`, `0≤e_m·S(A)` holds trivially (with equality only if `S(A)=0`). ∎

*Where proved:* this file, §7.1 above, round 5. Self-contained modulo the already-certified
Fact 5 (itself modulo nothing further); general-purpose (no dependence on the specific target
value `e_m=1/(2^{m+1}-1)` beyond `e_m>0`, and no dependence on Case (i)/(ii)); directly reusable
by `dyadic-cascade-induction` (both its Case (i) closure and its open Case (ii)/Step-4 work
could cite this to restrict attention to `k=m+1` throughout, rather than handling the `k=1`
sub-case only, as that file currently does ad hoc at line ~380). Independently sanity-checked
against the exact-search harness on 30 fresh random `k<m` configurations (`m=3,\dots,7`), all
giving `g_exact(A,m)=0` exactly, matching the lemma.

**Lemma D/M (operation-sequence reformulation of Xiang Yu's cutting phase).**

*Statement.* Let `A = (a_1≥…≥a_k)` be Liu Bang's opening multiset (`k≤n+1` pieces, `n` cuts
available to Xiang Yu). For a finite multiset of nonnegative reals `B`, define two operations:
- `D(x)` for `x∈B`: replace `B` by `B\{x}` (remove one copy of the value `x`).
- `M(x,y)` for `x,y∈B` with `x≥y` (as values, i.e. `x` and `y` are two elements of the
  multiset `B`, possibly equal): replace `B` by `(B\{x,y})∪\{x-y\}` (remove one copy each of
  `x,y`, insert one copy of `x-y`).

Then: (1) **each operation is realizable by exactly one of Xiang Yu's cut points** — `D(x)`
by bisecting the physical piece of length `x` into two length-`x/2` pieces; `M(x,y)` by
cutting the physical piece of length `x` at distance `y` from one end, producing pieces of
length `y` and `x-y`. (2) **After the operation, `e` computed on the new active multiset `B'`
equals `e` computed on the true full physical multiset (all real pieces, including the
"cancelled" duplicate copies)** — because in both cases the operation creates a pair of
equal-valued physical pieces (the two halves in `D`, or the new length-`y` piece and the
pre-existing length-`y` piece in `M`), and by the certified **Lemma P**
(`lemmas/duplicate-pair-invariance.md`) deleting any two equal-valued entries from a sorted
multiset leaves `e` exactly unchanged. (3) Consequently, for **any** legal sequence of
`≤n` such operations starting from `A`, the resulting `e` (computed on the final active
multiset by the ordinary alternating-rank-sum formula) equals the true `e = L-X` of the real
final dissection under that Xiang Yu response.

*Proof.* (1) is immediate from the definitions (each operation specifies exactly one cut
point). For (2): in the `D(x)` case, before the cut the active multiset (as physical pieces)
contained one copy of `x`; after, it contains two copies of `x/2` in its place. Since these
two copies are equal-valued, Lemma P applies directly with `M := $ physical multiset after the
cut, `M' := $ physical multiset with those two entries deleted `=$ physical multiset before the
cut with `x` itself deleted (since removing the two `x/2` copies from the *after* multiset and
removing `x` from the *before* multiset produce the identical remaining multiset — both equal
"all physical pieces except the one that was just split"). So `e(\text{after}) = e(\text{before
multiset with }x\text{ deleted})`, i.e. exactly the effect of the `D(x)` operation on the
active multiset. In the `M(x,y)` case: before the cut, the physical multiset contains one copy
of `x` and (separately) one copy of `y`; after, the copy of `x` is replaced by two new pieces
of length `y` and `x-y`, so the physical multiset now contains **two** copies of `y` (the
original untouched one, plus the new one) together with the new `x-y` piece and everything
else unchanged. The two copies of `y` are equal-valued, so Lemma P gives `e(\text{after}) =
e(\text{after multiset with the two }y\text{-copies deleted})`, and that reduced multiset is
exactly "everything except the original `x` and `y`, plus the new `x-y`" — i.e. exactly the
effect of `M(x,y)` on the active multiset. This proves the single-operation case of (2). For
sequences: apply this equality inductively — after each operation, the *current* active
multiset's `e`-value equals the *true* physical multiset's `e`-value at that point in the cut
sequence (by the single-operation argument, using Lemma P applied to the actual physical
multiset present at that step, which by the inductive hypothesis has the correct `e`); since
this holds after every operation, it holds after the final one, proving (3). (Composability of
repeated Lemma P applications, with no cross-terms between different cancelled pairs, is
already established in `lemmas/duplicate-pair-invariance.md`'s "Use" section.) ∎

*Consequence for the parent problem.* Xiang Yu's achievable values under `≤n` cuts include (as
a **subset**, not necessarily all) every value `e(B_{\text{final}})` obtainable by applying
`≤n` legal D/M operations starting from `A`; in particular
`g(A,n) := \min$ over such sequences $e(B_{\text{final}})` is always an upper bound for the
true value Xiang Yu can force Liu Bang's `e` down to. This is the reformulation used above to
generate and test candidate strategies (Rule 1, Rule 2), and to run the bounded exhaustive
search establishing that the D/M space itself suffices at the tested points even where both
tested greedy policies fail.

*Where proved:* this file, Section 1 above (statement) and this section (full proof), round 3.
Ready for certification into `results/imo-2026-03/lemmas/` — it is general-purpose (does not
depend on the specific numbers `2^n/(2^{n+1}-1)`), self-contained modulo the already-certified
Lemma P, and reusable by any sibling approach (in particular `dyadic-cascade-induction`, whose
Case (i)/(ii) strategies are literally special cases of D/M sequences, and whose §5 lower-bound
skeleton's Branch B "bisection dominates" question is exactly a question about D/M sequences
too).

**Lemma (Layer-cake identity for `e`) — new this round, full proof.**

*Statement.* For a sorted descending list `x_1≥x_2≥…≥x_n≥0` (`x_{n+1}:=0` by convention), define
`N(t):=#\{i: x_i>t\}` for `t≥0`. Then
```
e(x_1,…,x_n) := Σ_{i=1}^n(-1)^{i+1}x_i = ∫_0^∞ 1[N(t) is odd] dt.
```

*Proof.* For `t∈[x_{i+1},x_i)` (`i=1,…,n`; the interval is empty, contributing `0`, whenever
`x_{i+1}=x_i`), every one of `x_1,…,x_i` is `>t` (each is `≥x_i>t`) and every one of
`x_{i+1},…,x_n` is `≤t` (each is `≤x_{i+1}≤t`), so `N(t)=i` exactly throughout this interval,
which has length `x_i-x_{i+1}≥0`. Hence
```
∫_0^∞ 1[N(t) odd] dt = Σ_{i=1}^n (x_i-x_{i+1})·1[i odd] = Σ_{i odd, 1≤i≤n} (x_i - x_{i+1}).
```
It remains to show `Σ_{i odd,1≤i≤n}(x_i-x_{i+1}) = Σ_{i=1}^n(-1)^{i+1}x_i` for every `n` (an
identity independent of the actual numeric values, so it is proved by induction on `n` alone).
*Base case `n=1`:* LHS `=x_1-x_2=x_1-0=x_1` (the only odd `i≤1` is `i=1`); RHS `=x_1`. Equal.
*Inductive step, `n→n+1`* (IH: the identity holds for the list `x_1,…,x_n`, with its own
convention `x_{n+1}=0`): going to `n+1` elements, `x_{n+1}` becomes an actual list entry (no
longer forced to `0`), and a new convention `x_{n+2}=0` is introduced.
  - If `n` is odd (so `n+1` is even): the LHS's *last* odd-indexed term was `i=n`, previously
    `(x_n-x_{n+1}^{(\text{old})})=(x_n-0)=x_n`; now it becomes `(x_n-x_{n+1}^{(\text{new})})`
    with `x_{n+1}` the real value. No new odd-indexed term appears (`n+1` is even). So
    `\text{LHS}_{n+1} = \text{LHS}_n - x_n + (x_n-x_{n+1}) = \text{LHS}_n - x_{n+1}`. Meanwhile
    `\text{RHS}_{n+1}=\text{RHS}_n+(-1)^{n+2}x_{n+1}=\text{RHS}_n+(-1)^n x_{n+1}=\text{RHS}_n-x_{n+1}`
    (`n` odd). By the IH `\text{LHS}_n=\text{RHS}_n`, so `\text{LHS}_{n+1}=\text{RHS}_{n+1}`.
  - If `n` is even (so `n+1` is odd): `i=n+1` is now a genuine new odd-indexed term, contributing
    `(x_{n+1}-x_{n+2})=(x_{n+1}-0)=x_{n+1}`; every earlier term is unaffected (the last odd index
    was `n-1≤n`, whose interval endpoint `x_n` — an even index, not summed — is untouched). So
    `\text{LHS}_{n+1}=\text{LHS}_n+x_{n+1}`. And `\text{RHS}_{n+1}=\text{RHS}_n+(-1)^{n+2}x_{n+1}
    =\text{RHS}_n+(-1)^n x_{n+1}=\text{RHS}_n+x_{n+1}` (`n` even). By the IH, equal. `∎`

*Where proved:* this file, round 7, §9.1 below (statement first appeared as an unproved sketch
in the round-6 outline, §8 Step 1; this is its first full proof). General-purpose, no dependence
on this problem's specific numbers; reusable by any approach reasoning about `e` via threshold/
coverage arguments.

**Lemma (Non-crossing inside/outside independence) — new this round, full proof.**

*Statement.* Fix a sorted list `Y=(y_1≥…≥y_p)` and suppose a selection (partition of
`\{1,\dots,p\}` into Kept/Deleted/Matched-pairs, as formalized in §9.2 below) is **globally
non-crossing** and contains the matched pair `(1,j)` for some `j∈\{2,\dots,p\}`. Then no matched
pair of the selection has one endpoint in `I:=\{2,\dots,j-1\}` ("inside") and the other in
`O:=\{j+1,\dots,p\}` ("outside") — every other matched pair lies entirely within `I` or entirely
within `O`. Consequently the restriction of the selection to `I` and its restriction to `O` are
each themselves valid non-crossing selections on their own index sets, independently, and
conversely gluing together any non-crossing selection on `I` and any non-crossing selection on
`O` (plus the pair `(1,j)`) always yields a globally non-crossing selection on the whole list.

*Proof.* Suppose for contradiction a matched pair `(i',o')` has `i'∈I`, `o'∈O`, i.e.
`2≤i'≤j-1` and `j+1≤o'≤p`. Then `1<i'<j<o'`, which is exactly the crossing condition
(`i<i'<j<j'` with `i=1,j=j,i'=i',j'=o'`) applied to the pair `(1,j)` and `(i',o')` — so these two
matched pairs cross, contradicting global non-crossingness. Hence no such pair exists, proving
the first claim. For the converse: if `τ_I` is non-crossing on `I` and `τ_O` is non-crossing on
`O`, then any two pairs both drawn from `τ_I` (or both from `τ_O`) don't cross by assumption; any
pair from `τ_I` and any pair from `τ_O` are disjoint index ranges (`I` and `O` don't overlap, and
neither touches index `1` or `j`) so they cannot satisfy the crossing condition (crossing
requires the two pairs' index ranges to interleave, which is impossible for pairs drawn from
disjoint intervals `I<j<O`); and neither crosses `(1,j)` since one endpoint of `(1,j)` is `1`
(the global minimum index, so no pair can have exactly one endpoint strictly between `1` and
anything smaller) and by the same interleaving argument used above, no pair entirely inside `I`
or entirely inside `O` can cross `(1,j)` (an entirely-inside pair `(a,b)` with `2≤a<b≤j-1`
satisfies `1<a<b<j`, i.e. it is *nested inside* `(1,j)`, not crossing it; an entirely-outside
pair satisfies `1<j<a<b`, disjoint from `(1,j)`, not crossing). `∎`

*Where proved:* this file, round 7, §9.2 below. This is what makes Step 2's Fact-3-based
recursive definition of `NC(Y,b)` (independent optimization on the inside/outside sub-lists) an
**exact** identity for the best globally-non-crossing value achievable while matching `y_1` to
`y_j` — not merely a plausible simplification. General-purpose, reusable by any non-crossing-
partition-style DP argument.

**Lemma (Shrink-List Monotonicity) — new round 14, full proof, promotable.**

*Statement.* For any background multiset `C`, any list `W`, and any `x\in W`:
```
OPT_{+1}(C,W) \le OPT_{+1}(C, W\setminus\{x\})     (mirror: OPT_{-1}(C,W)\ge OPT_{-1}(C,W\setminus\{x\})).
```
*Proof.* One-line bijection: extend a `\sigma=+1`-optimal selection of `W\setminus\{x\}` by
additionally deleting `x` (contributes `0` to `e`, the standing convention). This is a valid
candidate selection of `W` with the identical value, so `OPT_{+1}(C,W)$, the minimum over `W`'s
whole search space, is at most that value. Full derivation: this file, §21.3/§22.1, round 14.
Independently verified `0/14{,}160+3{,}000` fresh exact-`Fraction` trials on fully arbitrary
`(C,W,x)` (no `\mathcal F`-restriction) by two independent agents. Filed standalone as
`lemmas/shrink-list-monotonicity.md`, recommended for certification. **Corollary** (repeated
application down to the empty list): `OPT_{+1}(C,W)\le e(C)` for any finite `W` — gives Gap 1a's
Deletion-Suffices-for-`k^*` sub-lemma's "easy half" (`M\le D`) unconditionally, isolating its
entire remaining content to the reverse inequality (§22.1-§22.2).

### 8. Round 6 skeleton — layer-cake reformulation + extreme-element peeling DP (replaces
local pairwise uncrossing-exchange as this file's Case (ii)/non-crossing-conjecture mechanism)

**Why the old mechanism is dead, restated precisely (do not re-attempt any variant).** This
round's explorer reconstructed the file's own hard counterexample's tied optimal witnesses
exactly and found both change *which* points are matched/deleted/kept relative to any fixed
support — the winning move is never a re-pairing of a frozen set of participants. Any argument
that holds "the rest of the selection" fixed while locally swapping one match's two arcs is
structurally blind to this move class. §8 below is a genuinely global mechanism instead.

**Step 1 (layer-cake identity for `e` — new, general, easy to prove).** For a sorted
descending list `x_1\ge x_2\ge\dots\ge x_n\ge0`, define `N(t):=\#\{i:x_i>t\}`. Then
```
e(\{x_1,\dots,x_n\}) = \int_0^\infty \mathbf{1}[N(t)\text{ is odd}]\,dt.
```
*Proof sketch:* on each interval `t\in(x_{i+1},x_i)`, `N(t)=i` is constant; the integral over
that interval contributes `(x_i-x_{i+1})` exactly when `i` is odd, `0` when `i` is even — this
reproduces the telescoping alternating sum `e=\sum_i(-1)^{i+1}x_i` term by term (elementary
induction on `n`, using `x_{n+1}:=0`). **Why this is useful:** it converts "which rank does a
survivor end up at" (the global, non-local quantity the explorer identified as the true
obstruction) into "for each threshold `t`, is the number of survivors exceeding `t` odd" — a
question that can be asked and answered incrementally, threshold by threshold, without first
knowing the whole final sorted order.

**Step 2 (peel-the-extreme-element induction — a DP, not a greedy/exchange rule).** Define,
for a sorted list `Y=(y_1\ge\dots\ge y_p)` and budget `b`, `NC(Y,b) :=` the value of the best
**non-crossing** matching+deletion selection, computed by the standard non-crossing-partition
recursion on `y_1` (the extreme element): considering all three fates of `y_1`,
```
NC(Y,b) = min(  KEEP:    (-1-\text{sign offset}) \cdot y_1  "prepended", combined via Fact 3
                          with NC(Y\setminus\{y_1\}, b),
                DELETE:  NC(Y\setminus\{y_1\}, b-1),
                MATCH_j: for each j=2,\dots,p:  match (y_1,y_j)\to y_1-y_j, insert it into
                          the correct rank position among Y\setminus\{y_1,y_j\}, recurse via
                          Fact 3 on the "inside" (ranks 2..j-1) and "outside" (ranks j+1..p)
                          sub-lists independently (this is the classical non-crossing/Dyck-path
                          recursion; both sub-lists get independent budget shares summing to
                          `b-1`), each combined with the correct `(-1)^{|X|}` sign flip from
                          Fact 3.
             )
```
**The "running rank/sign offset" is exactly Fact 3's `(-1)^{|X|}` factor**, carried recursively
through the peel — this is the concrete non-scalar invariant the round-4/5 induction-loading
postmortems identified as missing, now supplied not as a bounded lookahead but as the DP's own
recursive structure (unbounded depth, exact at every level, no scalar fallback anywhere).
`NC(Y,b)` is a **well-defined, fully computable, closed-form-via-Fact-3 quantity** — this part
requires no conjecture, only careful bookkeeping (the builder's first task: write this
recursion out precisely and confirm it matches the certified Fact 3 identity term-by-term).

**Step 3 (the actual open gap, restated as an induction claim, not a vague conjecture).**
**Claim:** `OPT(Y,b) = NC(Y,b)` for every `Y,b` (`OPT` = the true unrestricted, crossing-allowed
optimum). `\ge` is trivial (non-crossing selections are a subset of all selections). The
content is `OPT(Y,b)\ge NC(Y,b)`, i.e. no crossing selection ever beats the DP's own value.
**Proposed proof mechanism (strong induction on `p`, using Step 2's own recursion as the
induction's shape, NOT local exchange):** take ANY optimal (possibly crossing) selection
`\sigma^*` for `(Y,b)`; case on `y_1`'s fate in `\sigma^*` (kept / deleted / matched to some
`y_j`). In each case, apply the strong induction hypothesis to the residual sub-problem(s)
(`Y\setminus\{y_1\}` or the "inside"/"outside" split at `j`) to replace `\sigma^*`'s residual
selection by an equal-or-better *non-crossing* one — **this is a global replacement of the
entire residual, not a local swap of two arcs**, exactly the move class the explorer's
diagnosis says is required. **What is NOT yet proved:** that this residual replacement, when
`y_1` was matched to `y_j` in `\sigma^*` with OTHER selections crossing that arc, can be carried
out without those other crossing arcs increasing the value once forced to reroute around `j`'s
split — this is the genuine remaining technical content, not a restatement of the old dead
end (it is about the interaction between `y_1`'s match arc and everything *strictly inside*
`(1,j)` plus everything *strictly outside*, not about re-pairing `y_1`'s own arc).

**Key lemmas (claim + mechanism):**
- **Layer-cake identity** (Step 1) — because `e`'s alternating-sum telescoping is exactly the
  odd/even coverage count of nested threshold intervals; elementary, provable from scratch.
- **`NC(Y,b)` well-definedness / Fact-3 closed form** (Step 2) — because the non-crossing
  recursion's "inside"/"outside" split is exactly Fact 3's dominant-block extraction applied
  recursively; no new machinery, just composing already-certified Fact 3 with itself.
- **`OPT=NC` induction** (Step 3, OPEN) — because peeling the extreme element and replacing the
  ENTIRE residual selection (not one arc) via the strong IH is a fundamentally larger move than
  local exchange; whether it closes is the precise open question, isolated to the interaction
  between a matched arc `(1,j)` and crossing arcs from outside `(1,j)`.

**Open gaps:** Step 3's induction — specifically, whether an arc from outside `(1,j)` that
crosses `y_1`'s match can always be "pushed" to route around the split without loss (this is
the one place a genuinely new argument, not yet found, is needed).

**Cases to cover:** the three-way fate split for `y_1` (kept/deleted/matched-to-`j` for every
`j`) is already exhaustive by construction; within MATCH_j, the inside/outside recursion must
itself handle budget splits `b_{\text{in}}+b_{\text{out}}=b-1$ for every partition (standard
non-crossing DP bookkeeping, not a new case).

**Watch out for:** (1) confirm Step 1's identity is stated for the FINAL multiset (kept
elements plus match-difference values), not the original `Y` — the match-difference values'
thresholds interact with kept elements' thresholds in the integral, this interaction is exactly
where Step 3's difficulty lives, so do not silently assume it decouples; (2) do not conflate
this induction with the already-dead local-exchange technique — the distinguishing test is
whether the argument ever needs to compare two *entire* selections with different supports
(this one does, by construction) versus one arc-swap within a frozen support (the dead one);
if a proposed builder write-up only ever perturbs one arc at a time, it has silently regressed
to the dead mechanism and should be rejected.

**Secondary, not developed this round (flag only per the explorer's finding):** an LP-relaxation
of the cut-allocation-across-pieces problem, with a separate integrality-gap bound, was flagged
by this round's new-framing explorer as a genuinely different *technique* for this same
isolated `k=m+1` gap — untested, unbuilt, noted here as a fallback if Step 3 above stalls for
several more rounds.

### 9. Round 7 build — Steps 1-2 completed in full; Step 3 (non-crossing conjecture) DISPROVED
in its general form, and correctly rescoped to the regime the proof actually needs

All computations in this section are exact (`fractions.Fraction` / plain integers), independently
re-derivable; every claim below was checked by **two independently-written** enumeration scripts
(no shared code path for the decisive counterexample).

#### 9.1 Layer-cake identity — proved in full

See "Promotable lemmas" above for the complete proof (elementary induction on `n`, exactly
matching the outline's sketch, no gaps). This closes §8 Step 1 unconditionally.

#### 9.2 Precise formalization of `OPT(Y,b)` and `NC(Y,b)`

**Selections.** Given a sorted list `Y=(y_1≥\dots≥y_p)` and an integer budget `b≥0`, a
**selection** is a partition of `\{1,\dots,p\}` into three parts: a set of **kept** indices `K`,
a set of **deleted** indices `D`, and a set `M` of pairwise index-disjoint 2-element subsets
("matched pairs") `\{(i_1,j_1),\dots,(i_r,j_r)\}` (each written with `i_l<j_l`), such that
`K,D,` and `\bigcup M` partition `\{1,\dots,p\}` exactly and `|D|+|M|≤b` (the selection's
**cost**). Its **value** is
```
v(K,D,M) := e\big(\{y_k: k∈K\} ∪ \{y_i-y_j : (i,j)∈M\}\big),
```
the ordinary alternating-sum `e` of the sorted union multiset (this is precisely a "one-shot,
non-cascading" application of the certified D/M operations: each deleted index costs one `D`
operation and contributes nothing by Lemma P; each matched pair costs one `M` operation and
contributes its difference; kept indices cost nothing and are unchanged — matching §6 Step 2's
"one-shot allocation" definition exactly).

```
OPT(Y,b) := min over all selections (K,D,M) of v(K,D,M).
```
Two matched pairs `(i,j),(i',j')` (`i<j`, `i'<j'`) **cross** if `i<i'<j<j'` or `i'<i<j'<j`. A
selection is **non-crossing** if no two of its matched pairs cross.
```
NC(Y,b) := min over non-crossing selections (K,D,M) of v(K,D,M).
```
Since every non-crossing selection is in particular a selection, the search space defining
`NC` is a subset of the one defining `OPT`, so **`NC(Y,b) ≥ OPT(Y,b)` always** (this is the
"easy direction," needing no argument beyond "minimizing over fewer candidates gives a value no
smaller"). The content of §8 Step 3's conjecture is the reverse inequality `OPT(Y,b) ≥ NC(Y,b)`
(equivalently `OPT=NC`, "crossing never strictly helps").

Both `OPT(Y,b)` and `NC(Y,b)` are well-defined (finite minima over a finite, explicitly
enumerable set of selections — the number of selections of `\{1,\dots,p\}` is finite for every
finite `p`), so no existence issue arises; the only open question is the value of the two minima.

**Well-definedness of the recursive (Fact-3-based) computation of `NC(Y,b)`.** By the certified
Non-crossing inside/outside independence lemma (see "Promotable lemmas" above), peeling the
extreme element `y_1` and case-splitting on its fate (kept / deleted / matched to `y_j` for each
`j`) gives an *exact* recursion for `NC(Y,b)`: in the matched-to-`j` branch, the best non-crossing
completion decomposes as an independent choice of a non-crossing selection on `I=\{2,\dots,j-1\}`
(budget `b_{\text{in}}`) and one on `O=\{j+1,\dots,p\}` (budget `b_{\text{out}}`,
`b_{\text{in}}+b_{\text{out}}=b-1`), each scored via the certified Fact 3 block-extraction
identity once the three pieces (kept-`y_1`-or-not, the inside block's own final multiset, the
outside block's own final multiset, and the inserted difference `y_1-y_j`) are combined in
sorted order. (We do not belabor the exact sign bookkeeping here since it is not the load-bearing
content — Fact 3's `(-1)^{|X|}$ factor is applied deterministically once the relative rank
positions are fixed — the crucial, previously-unproved fact was the inside/outside independence
itself, now proved above.) This confirms `NC(Y,b)` is computable in closed recursive form with
no conjecture required — §8 Step 2 is fully closed.

#### 9.3 Step 3 (the conjecture `OPT=NC`) is FALSE in the fully general form stated in §7.3/§8

**Exact counterexample.**
```
Y = (39, 36, 30, 28, 22, 18, 14),  p = 7,  b = 3.
```
An exhaustive enumeration of every selection with cost `≤3` (`925` selections at this `p`,
fully enumerated, no heuristic pruning, confirmed by direct count) gives:
```
OPT(Y,3) = 1,   attained (among others) by
  kept = {14},  deleted = ∅,  matched = {(39,30), (36,22), (28,18)}
  → differences 9, 14, 10 → final multiset {14,14,10,9} (note 14 ties with kept 14 — by the
    certified Lemma P this duplicate pair cancels, leaving {10,9}) → e = 10-9 = 1.
```
The three matched pairs, at sorted positions `(0,2),(1,4),(3,5)` (`0`-indexed), have crossing
structure: `(0,2)` and `(1,4)` cross (`0<1<2<4`); `(1,4)` and `(3,5)` cross (`1<3<4<5`); `(0,2)`
and `(3,5)` are disjoint (do not cross). So this optimal selection uses a genuine **3-arc
"crossing chain"** (the middle arc crosses both others) — not expressible as any 2-arc local
exchange, which is exactly why this failure mode was never caught by the round-5/6 local-
uncrossing-exchange tests (those only ever compared 2-3 alternative pairings on a single frozen
4-point support).
```
NC(Y,3) = 2,   attained by e.g. kept = {30,28,14}, deleted = {39,18}, matched = {(36,22)}
  → final multiset {30,28,14,14} → (Lemma P cancels the duplicate 14s) → e = 30-28 = 2.
```
Since `1<2`, **`OPT(Y,3) < NC(Y,3)` strictly: the general non-crossing conjecture is FALSE.**

**Independent re-verification (two separate implementations, no shared code).** The first
implementation enumerates selections via a direct recursive "assign each remaining index to
kept/deleted/matched-with-some-later-index" procedure; the second is an independent
implementation built around involution-style "singles-and-pairs" partitions of `\{1,\dots,p\}`
followed by an independent subset choice of which singles to delete, using a differently-shaped
crossing-check routine. **Both agree exactly: `OPT=1`, `NC=2`.** A search over `p≤6` (`4000`
random trials, various budgets) found **no** analogous counterexample — this specific failure
mode appears to require `p≥7` (an experimental observation, not a proved lower bound).

**A second, independently-found counterexample** (general form, from an earlier stage of this
round's search, before the `p=7` minimal example above was isolated):
```
Y = (400,218,194,187,169,27,3), p=7:  OPT(Y,3)=4 < NC(Y,3)=6,  and also OPT(Y,4)=4 < NC(Y,4)=5.
```
(Both re-verified exactly; the winning `OPT` selections here also use 3-arc crossing-chain
matchings — e.g. at `b=3`: kept `{27}`, matched `(400,218),(194,169),(187,3)` → final multiset
`{182,184,25}` sorted `184,182,27... ` — exact recomputation: `184-182+27-25=4`, confirmed.)

**Conclusion:** §7.3's "non-crossing matching+deletion" conjecture, **stated for every sorted `Y`
and every budget `b`**, is **refuted**, with two independent exact counterexamples. This
definitively rules out the literal DP-via-non-crossing-partitions technique as a *fully general*
tool — **do not re-propose the unrestricted conjecture in any future round.**

#### 9.4 Rescoping: the ONLY budget the proof actually needs is `b=p-1`, and the counterexamples
vanish there

Tracing through exactly how `NC`/`OPT` are actually invoked by the chain-prefix+tail family
(§6): Slack Collapse (certified, `lemmas/slack-collapse.md`) reduces the whole upper-bound
induction to the tight case `k=m+1` (Liu Bang uses every one of his marks). Within that tight
case, after a chain-prefix of length `c∈\{0,\dots,m\}`, the "one-shot tail" sub-problem has
`p=k-c` elements (the chain result `r_c` plus the `k-c-1` untouched originals) and remaining
budget `m-c`. Since `k=m+1` in the tight case, `m-c = (k-1)-c = (k-c)-1 = p-1` **exactly, always**
— the one-shot tail's budget is never anything other than `p-1`. So the literal quantity
required by the proof is not "`OPT(Y,b)=NC(Y,b)` for every `Y,b`" but the strictly narrower:
```
(Rescoped Conjecture)  OPT(Y,p-1) = NC(Y,p-1)  for every sorted Y of size p (every p≥0).
```
**Both counterexamples above vanish at `b=p-1=6`:** direct recomputation gives
`OPT(Y,6)=NC(Y,6)=0` for `Y=(39,36,30,28,22,18,14)`, and `OPT(Y,6)=NC(Y,6)=0` for
`Y=(400,218,194,187,169,27,3)` too — both exactly re-verified. So neither known counterexample
threatens the rescoped conjecture; the general refutation and the actually-needed restricted
claim are logically independent, and only the former is settled (false).

**Fresh, extensive stress test of the Rescoped Conjecture (this round, exact integers, no
floats).**
- `2000` random trials, `p=2,\dots,7`, `b=p-1` exactly, integer values up to `200`: **0
  mismatches**.
- `150` further adversarial-shaped trials (`p=6,7,8`, `b=p-1`), mixing uniform-random,
  superincreasing-like, and near-tied (`base±3`) constructions: **0 mismatches**.
- `8` trials at `p=9`, `b=8`, integer values up to `300`: **0 mismatches** (also confirms the
  exhaustive search stays computationally feasible — under `0.35`s per instance — at this size).
- `60` further trials at `p=9,10`, `b=p-1`, integer values up to `400`: **0 mismatches**.
- **Total: 2218 exact-integer trials at the correctly-scoped budget `b=p-1`, zero mismatches,
  spanning `p=2` through `10`.**

**Honest status.** The Rescoped Conjecture is *not proved* — this round's stress testing is
evidence, not a proof, per this project's standing rule on numerical checks. But it is now the
**precisely correct target** (matching exactly what the theorem needs, no more and no less),
whereas the previous general form was demonstrably too strong and is now known to be false. This
is a genuine sharpening: a future round attempting a proof should target `OPT(Y,p-1)=NC(Y,p-1)`
specifically — e.g. by exploiting that budget `p-1` is exactly one short of Fact 5's
full-cancellation threshold `p` (at which `OPT=NC=0` trivially by Slack-Collapse-style
reasoning), suggesting an "almost full cancellation" structural argument might succeed where the
fully general claim fails. No such argument was found or attempted to completion this round (no
time remained); this is the concrete next step.

**Why this is not a repackaged dead end.** This is not local pairwise uncrossing-exchange (the
confirmed-dead mechanism from round 6): both counterexamples were found and are explained by
comparing **entire alternative global selections** (different kept/deleted/matched-set choices,
not a re-pairing of one frozen 4-point support), and the rescoping argument is a structural fact
about the proof's own recursion (which budget actually occurs), not a perturbation of any fixed
selection.

#### 9.5 Net assessment for this round

- **Steps 1 and 2 of §8 are now fully, rigorously proved** (Layer-cake identity; non-crossing
  inside/outside independence) — both certified-quality, general-purpose, promotable.
- **Step 3, as literally conjectured, is FALSE** — a decisive, useful negative result (two
  independent exact counterexamples, `p=7`), closing off the fully general form for good.
- **A correctly-rescoped replacement (`b=p-1` exactly) is proposed and extensively re-supported**
  (2218 fresh trials, `p` up to `10`, zero mismatches) — this is the sharp, precise remaining
  target, not yet proved.
- **What remains open:** a full proof of `OPT(Y,p-1)=NC(Y,p-1)` for every `p` (or a further
  counterexample at larger `p`, which the current stress-test budget did not rule out beyond
  `p=10`) — and, independently of that, still open even after any such proof: the closed-form
  Fact-3 evaluation of `NC(Y,p-1)` combined with the chain-prefix minimization over `c` would then
  need to be shown `≤e_m·S(A)` for every Case (ii) `A` — a further step not addressed this round.
  (See the file's single "## Full proof" section above — still absent, Status `partial`.)

## §10 (round 8 outline) — MAX-companion mutual induction for `OPT(Y,p-1)=NC(Y,p-1)`

**Technique:** strong induction on `p`, peeling the global max `y_1`, using the elementary
**telescoping identity** `e(y_1,\dots,y_p)=y_1-e(y_2,\dots,y_p)` (true because `y_1` is the max
of `Y` and hence remains the max of any final combined multiset produced by a selection on the
rest — every matched difference `y_i-y_j\le y_i\le y_1`). Case-split on `y_1`'s fate at
`\text{gap}=p-b=1` (i.e. `b=p-1`, the exact target):

**(a) DELETE `y_1`.** Cost `1`, residual `Y'=Y\setminus\{y_1\}` (size `p-1`), budget left `p-2`,
`\text{gap}=(p-1)-(p-2)=1$ — same gap, one smaller `p`. **Proved, elementary, no caveat:** a
direct self-similar application of the strong IH; closes cleanly.

**(b) MATCH `y_1,y_j`.** Cost `1`, new list `Y''=(Y\setminus\{y_1,y_j\})\cup\{y_1-y_j\}` (size
`p-1`), budget left `p-2`, `\text{gap}=1` again — but this is **NOT** directly reducible to the
IH as a fresh unconstrained `(p-1)`-instance: by the certified Non-crossing inside/outside
independence lemma, `NC`'s recursive value after this match decomposes into an **independent**
optimization on "inside" (`2,\dots,j-1`) and "outside" (`j+1,\dots,p`), whereas `OPT`'s
(crossing-allowed) recursive value need not respect this decomposition — it may use an arc with
one endpoint inside and one outside. This is exactly the mechanism of the certified `p=7`
counterexample (a genuine 3-arc crossing chain). **THIS IS THE ONE REMAINING OPEN GAP.**

*Open Gap — precise target lemma (hand to the builder):* **Small-Gap Crossing-Domination
Lemma** — at `\text{gap}\le1` (possibly `\le2`, per this round's data: zero violations found up
to `p=10$ at gap 1 and `p=9` at gap 2, while gap `3` breaks at `p=8` and gap `4` breaks at the
known `p=7` witness), no crossing configuration can strictly beat the best non-crossing
completion — i.e., `OPT`'s match-branch value always ties `NC`'s. *Proposed mechanism (budget
counting, not yet carried out):* a genuinely crossing-improving configuration is, by the known
counterexample's structure, a **chain of pairwise-crossing arcs** of some length `L\ge3`
touching `\ge L+1` distinct elements and spending `L` units of match-cost. Relate the *minimal*
`p` at which such a chain can improve on the best non-crossing alternative to the available
`\text{gap}$: the empirical trend (gap `4\to p=7`, gap `3\to p=8`, gap `2\to$ none found through
`p=9`, gap `1\to` none found through `p=10`) suggests a threshold of the rough shape "a
crossing-improving chain needs `p\ge f(\text{gap})` for some increasing `f`," and that
`f(1),f(0)$ exceed every `p` the recursion ever actually needs to handle at that gap (since `p`
shrinks by exactly `1` each induction step while gap stays fixed at `1` or `0`, so if the base
list itself is large, the induction will have already reduced to a genuinely small residual list
by the time the crossing question is live). **Concrete first step for the builder:** hand-verify,
for the smallest `p` where a crossing configuration is even combinatorially possible at
`\text{gap}=1` (`p\ge4$ or so), that the crossing chain's value never strictly beats the
non-crossing alternative, building up the counting argument from these small cases rather than
attempting the general bound directly.

*Fallback induction order (crux `aimo-0003`), only if the above stalls:* peel an **innermost
chord** (a matched pair `(i,j)` whose index-interval contains no other participant of the
selection) instead of the global max — an innermost pair has nothing "inside" it by definition,
so peeling it removes the inside/outside crossing subtlety entirely for *that* pair (there is no
"inside" to worry about). **Caution, explicit:** `aimo-0003`'s technique applies to a *given,
already-fixed* pairing's structure (an invariant-verification argument), not to a *greedy
construction* of the optimal matching — a builder using this order must be careful it becomes a
tool for *analyzing/bounding* a hypothetical crossing-optimal selection from the inside out, not
a re-introduction of the already-dead "sorted-adjacency" conjecture (round 3), which was about
literally restricting *which* pairs may be chosen (value-adjacency), a different claim entirely.
If this order is used, state precisely, before building, what "peel the innermost chord" means
when the optimal matching is not yet known.

**(c) KEEP `y_1`.** Cost `0`, residual budget UNCHANGED `=p-1`, residual size `=p-1`, so the
residual sub-problem sits at `\text{gap}=0` exactly. Since the total value is `y_1-e(R)`,
minimizing it means MAXIMIZING `e(R)` over the residual selection — define the companion
optimization
```
MAXOPT(Y',b') := max over selections on Y', cost<=b', of e(final)
MAXNC(Y',b')  := same, restricted to non-crossing selections.
```
**New sub-target (this round, numerically supported, 2000+2100 trials, zero mismatches):**
`MAXOPT(Y',p-1)=MAXNC(Y',p-1)` at `|Y'|=p-1` (i.e. `\text{gap}=0`). Recursing the SAME
DELETE/MATCH/KEEP split on the MAX-companion at gap `0`: the MAX-DELETE branch is self-similar
(gap stays `0`, smaller size); the MAX-KEEP branch reduces (by the identical telescoping
argument) to a MIN-problem at `\text{gap}=-1` (budget exceeds size), which is trivially `0` for
both `MINOPT` and `MINNC` by the certified Slack Collapse mechanism (delete everything); the
MAX-MATCH branch has **the exact same inside/outside crossing obstruction as (b) above**, just
one gap-level lower (`0` instead of `1`) — numerically it is *also* robust at gap `0` (2000
trials, zero mismatches) and *also* breaks at large gap (gap `5`, `p=8`: `MAXOPT=46>MAXNC=45`,
mirroring the MIN side's breakdown exactly).

**Net structural claim (state this precisely, not vaguely):** the whole induction — both the
`\text{MIN}` instance at gap `1` and its `\text{MAX}` companion at gap `0` — reduces to proving
the **Small-Gap Crossing-Domination Lemma once**, at gap `\in\{0,1\}`; DELETE/KEEP branches on
both sides are already fully reduced to trivial/self-similar/Slack-Collapse cases. This is a
single shared open lemma, not two separate ones — do not let a future build treat the MIN-side
and MAX-side match branches as independent tasks.

**Key lemmas (stated precisely):**
- Telescoping Identity `e(y_1,\dots,y_p)=y_1-e(y_2,\dots,y_p)` — proved, elementary (max stays
  max under any selection on the rest).
- DELETE-branch self-similarity (both MIN and MAX sides) — proved, elementary budget bookkeeping
  (`\text{gap}` is preserved exactly).
- MAX-companion's KEEP-branch reduction to a trivial gap`\le-1` MIN-problem — proved, via the
  certified Slack Collapse mechanism applied to the one-shot/non-cascading setting.
- **Small-Gap Crossing-Domination Lemma** (the CENTRAL open lemma) — because a crossing-improving
  configuration needs a chain of `\ge3` pairwise-crossing arcs, whose minimal-`p`-to-improve
  threshold empirically grows as gap shrinks, and gap `\in\{0,1\}` is conjectured (not yet
  proved) to be below every such threshold the induction actually encounters.

**Open gaps:** the Small-Gap Crossing-Domination Lemma itself (§10(b), the one substantive item);
the innermost-chord fallback order is untried, flagged only as a backup if the counting argument
does not close cleanly.

**Cases to cover:** MIN-side DELETE/MATCH/KEEP at gap `1`; MAX-side DELETE/MATCH/KEEP at gap `0`
— six branches total, four already closed (both DELETEs, MIN's own KEEP-reduction, MAX's own
KEEP-reduction), the two MATCH branches sharing one open lemma.

**Watch out for:** do not silently re-treat the reduced `(p-1)`-element MATCH-branch list as "just
another same-gap instance, apply the IH directly" — this is exactly the unsound step that
silently reintroduces the already-refuted *general* `OPT=NC` conjecture (round 7 dead end); any
MATCH-branch step must go through the Small-Gap Crossing-Domination Lemma explicitly, not around
it.

**On the probabilistic/averaging alternative (flagged by this round's `g*`-framing explorer, not
adopted as a separate mechanism here — see the outliner's summary for why):** a randomized
response distribution with `E[e]\le` target is a genuinely different *technique* for the same
Case (ii) upper-bound gap this section already owns; if a future round wants to test it
concretely (e.g. `E[e]` under the uniform choice among numerically-tied optimal responses at
`m=4,5`), it belongs as an alternative sub-mechanism *inside* this section's open MATCH-branch
gap, not as a new top-level route, since it still operates entirely within this same
D/M-formalism, one-shot-allocation framing.

### 11. Round 8 build — the Extreme-Element Peeling Lemma (fully proved), and the corrected
(aggregated) Small-Gap Crossing-Domination Lemma

All computations in this section are exact integer arithmetic (Python `int`, no floats), fully
reproducible; every enumeration is a genuine exhaustive search over the finite space of selections
defined in §9.2 (no heuristic pruning, no sampling of the search space itself — only the *test
instances* `Y` are randomly generated).

#### 11.1 Precise definitions used throughout (restating §9.2's framework with no ambiguity)

Fix a sorted list `Y=(y_1\ge y_2\ge\dots\ge y_p)` and a budget `b`. Recall from §9.2: a
**selection** is a partition of `\{1,\dots,p\}` into Kept `K`, Deleted `D`, and pairwise
index-disjoint Matched pairs `M` (each `(i,j)`, `i<j`), with cost `|D|+|M|\le b`; its value is
`v(K,D,M):=e(\{y_k:k\in K\}\cup\{y_i-y_j:(i,j)\in M\})`. `OPT(Y,b):=\min v`, `NC(Y,b):=\min v$
over non-crossing selections only.

**New definitions needed for the MATCH branch (this round).** For a fixed value `v^\dagger\ge0`
and a sorted-order-preserving list `Z=(z_1,\dots,z_q)` (a sub-list of some original `Y`, retaining
its relative order — in particular tagged, if relevant, with an **inside/outside split** at some
position `s\in\{0,\dots,q\}`, meaning `z_1,\dots,z_s$ are "inside" and `z_{s+1},\dots,z_q` are
"outside"), define:
```
INSERT_OPT(v^\dagger, Z, b') := min over selections (K',D',M') of Z's own index set,
                                  cost \le b', of  e(\{v^\dagger\} \cup \{z_k:k\in K'\}
                                  \cup \{z_i-z_j:(i,j)\in M'\}).
INSERT_NC(v^\dagger, Z, b')  := same, restricted to selections (K',D',M') that are (i)
                                  non-crossing among themselves, AND (ii) contain no matched
                                  pair with one endpoint inside \{1,\dots,s\} and the other
                                  inside \{s+1,\dots,q\} (i.e. no pair "spans" the tagged split).
```
`v^\dagger` itself is **never** a candidate for deletion or matching in either definition — it
is a fixed external constant contributing exactly one term to the multiset `e` is computed on.
This is the precise "block-extraction, non-recursable" reading the reviewer asked for: `v^\dagger`
is *not* an element of `Z`'s own index set at all, so no selection of `Z` can ever touch it.

#### 11.2 The Extreme-Element Peeling Lemma — full proof

**Lemma.** Let `Y=(y_1\ge\dots\ge y_p)`, `p\ge1`, and `b\ge0`. Then
```
OPT(Y,b) = min\Big( OPT(Y\setminus\{y_1\}, b-1)\ [\text{if } b\ge1],\quad
                     y_1 - MAXOPT(Y\setminus\{y_1\}, b),\quad
                     \min_{j=2}^p INSERT_OPT(y_1-y_j,\ Y\setminus\{y_1,y_j\},\ b-1)\ [\text{if }b\ge1]
             \Big),
```
where `MAXOPT` is defined identically to `OPT` but with `\max` in place of `\min`, and
`Y\setminus\{y_1,y_j\}` retains its original relative order with the inside/outside split at
`s=j-2$ (the elements originally ranked `2,\dots,j-1$ are "inside," those ranked `j+1,\dots,p` are
"outside"). The identical statement holds with every `OPT`/`MAXOPT`/`INSERT_OPT` replaced by
`NC`/`MAXNC`/`INSERT_NC` throughout.

*Proof.* Every selection `(K,D,M)$ of `Y` with cost `\le b` falls into exactly one of three
disjoint cases according to index `1`'s fate: `1\in D`, `1\in K`, or `1$ is matched to some `j`
(i.e. `(1,j)\in M$ for a unique `j\in\{2,\dots,p\}`). This trichotomy is exhaustive (every index is
in exactly one of `K,D,\bigcup M`) and mutually exclusive, so
`OPT(Y,b) = \min(\text{best over case 1},\ \text{best over case 2},\ \text{best over case 3})`
— an elementary case split on a finite partition of the search space, requiring no further
justification.

**Case `1\in D$ (the DELETE branch).** There is a bijection between {selections of `Y` with
`1\in D$, cost `\le b`} and {selections of `Y\setminus\{y_1\}`, cost `\le b-1`}: given
`(K,D,M)` with `1\in D`, map it to `(K,D\setminus\{1\},M)` — this is a valid selection of
`Y\setminus\{y_1\}$ (since `M` cannot involve index `1`, as `1\in D` already, so every pair of `M`
consists of indices `\ge2`, i.e. `M` is already a valid set of matched pairs on
`Y\setminus\{y_1\}$'s own index set) with cost `=(|D|-1)+|M|\le b-1`. Conversely, given any
selection `(K',D',M')` of `Y\setminus\{y_1\}` with cost `\le b-1`, map it to
`(K',D'\cup\{1\},M')` (a valid selection of `Y` with cost `\le b`, `1\in D`). These two maps are
mutually inverse, and **the value is identical under either map**: `v(K,D,M) =
e(\{y_k:k\in K\}\cup\{\text{diffs}\}) = v(K',D',M')` exactly, since deleting index `1` (in the
`D`-branch) never contributes anything to the multiset `e` is computed on, regardless of which
side of the bijection we are on — the two multisets being fed into `e` are *literally the same
multiset*. Hence the best value over case 1 equals `OPT(Y\setminus\{y_1\},b-1)` exactly (with the
convention that this term is simply absent/infeasible if `b=0`, since then no index can be
deleted). The identical bijection (unaffected by non-crossingness, since removing index `1` from
`D` changes nothing about `M`'s crossing structure — `M` is untouched by this map) proves the `NC`
statement, i.e. case 1's best value for `NC(Y,b)` is `NC(Y\setminus\{y_1\},b-1)`.

**Case `1\in K` (the KEEP branch).** First, the **telescoping identity**: for *any* selection
`(K',D',M')` of `Y\setminus\{y_1\}` (cost `\le b`, since keeping index `1` costs `0` and does not
consume budget), let `W:=\{y_k:k\in K'\}\cup\{y_i-y_j:(i,j)\in M'\}` be its final multiset. Every
element of `W` is `\le y_1`: kept elements `y_k$ (`k\ge2`) satisfy `y_k\le y_2\le y_1`; a
matched difference `y_i-y_j\le y_i\le y_1` (since `i\ge2`). So `y_1` is the maximum of
`\{y_1\}\cup W`. By the already-certified **Fact 3** (block extraction,
`lemmas/insertion-and-cascade-facts.md`, applied with `X:=\{y_1\}` a singleton and `Y:=W`, using
`|X|=1`):
```
e(\{y_1\}\cup W) = e(\{y_1\}) + (-1)^1 e(W) = y_1 - e(W).
```
The selection `(K,D,M)` of `Y` with `1\in K` corresponding to this residual selection has value
`v(K,D,M)=e(\{y_1\}\cup W)=y_1-e(W)`, and every selection of `Y` with `1\in K` arises this way
(from a unique residual selection of `Y\setminus\{y_1\}` with the same cost). So
`\min_{\text{case }1\in K} v = y_1 - \max_{(K',D',M')\text{ over }Y\setminus\{y_1\},\ \text{cost}\le b} e(W) = y_1 - MAXOPT(Y\setminus\{y_1\},b)`,
exactly as claimed. For `NC`: restricting to non-crossing selections of `Y` with `1\in K` is
identical to restricting the residual selection of `Y\setminus\{y_1\}` to be non-crossing (index
`1$ is not part of any pair in this case, so it cannot create or remove a crossing), giving case
2's best value for `NC(Y,b)` as `y_1-MAXNC(Y\setminus\{y_1\},b)`.

**Case `(1,j)\in M` for a fixed `j` (the MATCH branch).** There is a bijection between
{selections of `Y` with `(1,j)\in M`, cost `\le b`} and {selections of `Z_j:=Y\setminus\{y_1,y_j\}`
(retaining original order), cost `\le b-1`}: given `(K,D,M)$ with `(1,j)\in M`, map to
`(K,D,M\setminus\{(1,j)\})$, a valid selection of `Z_j`'s index set with cost
`=|D|+(|M|-1)\le b-1`. The value transforms as `v(K,D,M) = e(\{y_k:k\in K\}\cup
\{y_1-y_j\}\cup\{y_i-y_{i'}:(i,i')\in M\setminus\{(1,j)\}\}) = e(\{y_1-y_j\}\cup W_j)$ where `W_j`
is exactly the final multiset of the residual selection on `Z_j` — this is **by the raw
definition of `v`** (§9.2), requiring no further identity: `e` is computed on a multiset regardless
of the origin of its elements, so inserting the fixed value `y_1-y_j` and computing `e` on the
union is definitionally `INSERT_OPT(y_1-y_j, Z_j, b-1)`, minimized over exactly this residual
search space. So case 3 (fixed `j`)'s best value is `INSERT_OPT(y_1-y_j,Z_j,b-1)` exactly, and
minimizing further over `j\in\{2,\dots,p\}$ (since the *original* case-3 search ranges over every
possible partner `j` for index `1`) gives `\min_j INSERT_OPT(y_1-y_j,Z_j,b-1)$, completing the
proof for `OPT`.

For `NC`: a selection of `Y` with `(1,j)\in M` is non-crossing **iff** (a) `M\setminus\{(1,j)\}` is
non-crossing among itself, AND (b) no pair of `M\setminus\{(1,j)\}` crosses `(1,j)` itself. By the
already-certified **Non-crossing inside/outside independence lemma** (this file, "Promotable
lemmas"), condition (b) is *exactly* equivalent to: no matched pair has one endpoint in
`I=\{2,\dots,j-1\}` and the other in `O=\{j+1,\dots,p\}` — precisely the "no pair spans the tagged
split at `s=j-2`" condition built into `INSERT_NC`'s definition (§11.1). So the bijection above,
restricted to non-crossing selections on the `Y`-side, corresponds *exactly* to selections of
`Z_j` satisfying `INSERT_NC`'s two conditions — giving case 3 (fixed `j`)'s best value for `NC` as
precisely `INSERT_NC(y_1-y_j,Z_j,b-1)`, and the full case-3 minimum as
`\min_j INSERT_NC(y_1-y_j,Z_j,b-1)`. `\blacksquare`

**This is a complete, general, unconditional proof** — it holds for every sorted `Y`, every
`b\ge0`, not merely at `b=p-1`. It is exactly the fix the reviewer asked for: the MATCH branch is
proved (not merely re-described) to reduce to a genuinely different function (`INSERT_OPT`/
`INSERT_NC`), which cannot be mistaken for, and is not claimed to equal, a fresh
`OPT`/`NC(Y'',b-1)$ call on a list `Y''` where `y_1-y_j` is treated as an ordinary further-selectable
element (that reading is false, per the reviewer's own 60-trial counterexample using
`Y=[38,21,15,7,2],b=4`, independently reconfirmed by this round's own decomposition check below).

**Independent computational confirmation of the Lemma's bookkeeping** (a sanity check on the
proof's arithmetic, not a substitute for it): the full three-way decomposition (`\min` of the three
branch values above, each branch computed via its proven formula) was compared against direct
exhaustive computation of `OPT(Y,p-1)` (resp. `NC(Y,p-1)`) on `420` fresh random trials each
(`p=1,\dots,7`, integer entries up to `300`) — **zero mismatches in either direction** (§11's
accompanying scratch code, `/tmp/round-8/work/explore.py`, `/tmp/round-8/work/branch_test.py`).

#### 11.3 The naive per-partner strengthening of the Small-Gap Crossing-Domination Lemma is FALSE

At `b=p-1` (the tight case forced by Slack Collapse), the DELETE and KEEP branches of the Peeling
Lemma reduce cleanly to the induction hypothesis at strictly smaller parameters (DELETE: size
`p-1`, budget `p-2`, same gap `1`; KEEP: reduces via the identical telescoping mechanism to a
`MAXOPT`/`MAXNC` instance of size `p-1`, budget `p-1`, gap `0`) — so **the only place the
`OPT=NC` induction can fail is the MATCH branch**, i.e. whether
`\min_j INSERT_OPT(y_1-y_j,Z_j,p-2) = \min_j INSERT_NC(y_1-y_j,Z_j,p-2)`. Note `|Z_j|=p-2$ and the
sub-budget is also `p-2` — i.e. **full slack** on `Z_j` alone (Fact 5/Slack-Collapse territory for
`Z_j$ in isolation, but *not* for the combined problem with `v^\dagger:=y_1-y_j` also present).

The round-8 outline's "Small-Gap Crossing-Domination Lemma" phrasing ("no crossing configuration
can strictly beat the best non-crossing completion") most naturally reads as a **per-fixed-`j`**
claim: `INSERT_OPT(v^\dagger,Z_j,p-2) = INSERT_NC(v^\dagger,Z_j,p-2)$ for *every* `j`
individually. **This is FALSE**, refuted by an exact, fully hand-verified minimal counterexample:

```
Y = (92, 89, 77, 73),  p=4,  b=p-1=3.  Take j=3 (partner y_3=77).
v^\dagger = y_1-y_3 = 92-77 = 15.   Z_3 = (89, 73)  [inside = {89} (rank 2, between 1 and 3),
                                                       outside = {73} (rank 4, after 3)].
Sub-budget = b-1 = 2 = |Z_3|.
```
Enumerating all 5 selections of `Z_3=(89,73)$ with cost `\le2` (by hand):
```
KEEP both:        {15,89,73} -> sorted 89,73,15 -> e = 89-73+15 = 31
DELETE 89 only:   {15,73}    -> sorted 73,15    -> e = 73-15    = 58
DELETE 73 only:   {15,89}    -> sorted 89,15    -> e = 89-15    = 74
DELETE both:      {15}       -> e = 15
MATCH(89,73)=16:  {15,16}    -> sorted 16,15    -> e = 16-15    = 1
```
So `INSERT_OPT(15,(89,73),2) = 1$, achieved by matching `89` with `73` (indices `2,4` of the
original `Y` — an arc that **spans the inside/outside split at `j=3`**, i.e. crosses the
`(1,3)` arc). Since this is the *only* candidate selection using the `MATCH(89,73)` pair, and
that pair is exactly forbidden by `INSERT_NC`'s condition (ii) (the pair `(89,73)` has one
endpoint inside `\{2\}` and the other outside `\{4\}`, spanning the split), `INSERT_NC` may only
choose among the remaining four candidates: `\min(31,58,74,15)=15`. So
```
INSERT_OPT(15,(89,73),2) = 1  \ne\  15 = INSERT_NC(15,(89,73),2).
```
**The per-fixed-`j=3`equality strictly fails** — a genuine, clean, hand-verified counterexample at
`p=4` (independently re-confirmed by exhaustive computation, `/tmp/round-8/work/branch_test.py`,
which additionally found `345$ further such per-`j` mismatches among `560` fresh trials at
`p=2,\dots,7`, and an analogous phenomenon on the `MAX` side — `140` mismatches among `780`
trials). **This refutes the natural, most literal reading of the round-8 outline's Small-Gap
Crossing-Domination Lemma. It should not be re-attempted in this per-partner form.**

#### 11.4 The correct (aggregated) form survives extensive testing

However, the *same* instance's **overall** `OPT(Y,3)` and `NC(Y,3)` still agree:
`OPT(Y,3)=NC(Y,3)=1` (both independently recomputed by exhaustive search over all of `Y`'s
selections, confirming §9's machinery). The reason: `NC` achieves the *same* value `1` using a
**different** partner, `j=2` (`y_2=89`), not `j=3`. Checking by hand: `v^\dagger=y_1-y_2=3$,
`Z_2=(77,73)$ with inside `=\emptyset$ (no elements rank strictly between `1` and `2`), outside
`=\{77,73\}`, so *no* pair of `Z_2` can span the (empty) inside/outside split — `MATCH(77,73)=4`
is fully legal for `INSERT_NC` here, giving `\{3,4\}\to e=4-3=1`, matching `INSERT_OPT`'s own best
value at `j=2$ (also `1`, since there is no crossing obstruction at `j=2` at all — inside is
empty). So `\min_j INSERT_NC(\cdot,Z_j,2) = \min(1_{[j=2]}, 15_{[j=3]}, \dots) = 1 =
\min_j INSERT_OPT(\cdot,Z_j,2)$ — **the discrepancy at `j=3` is exactly compensated by choosing
`j=2` instead**, for both sides.

This motivates the **corrected statement**:

**Small-Gap Crossing-Domination Lemma (aggregated form — the actual open target).** For every
sorted `Y=(y_1\ge\dots\ge y_p)`,
```
\min_{j=2}^p INSERT_OPT(y_1-y_j,\ Y\setminus\{y_1,y_j\},\ p-2)\ =\ \min_{j=2}^p INSERT_NC(y_1-y_j,\ Y\setminus\{y_1,y_j\},\ p-2),
```
and the analogous statement with `\max` in place of `\min$ throughout (`MAXOPT`/`MAXNC` in place of
`OPT`/`NC`) for the companion problem at gap `0`.

**Numerical support (this round, exact integers, no floats, fresh code, independently re-run):**
- **MIN side:** `1280` trials (`p=2,\dots,9`, `200` trials each for `p\le7`, `40` for `p=8,9`,
  integer entries up to `500`) — **zero mismatches** in the aggregated (min-over-`j`) equality,
  despite `345` of the *individual* per-`j` comparisons (a strict subset of the same trials)
  disagreeing.
- **MAX side:** `780` trials (`q=2,\dots,8$ where `q=p-1` is the companion problem's own size,
  matching sizes reachable from `p\le9`, integer entries up to `400`) — **zero mismatches** in the
  aggregated (max-over-`j`) equality, despite `140` per-`j` disagreements in the same trials.
- Both the MIN-side and MAX-side per-`j` counterexamples were independently hand-traceable (the
  `p=4$ example above for MIN; an analogous `q=5` example, `Y=(340,331,284,164,82)`, `j=4`
  (`0`-indexed `jj=3`), `INSERT` sub-budget `2`, `MAXOPT`-branch value `305` vs `MAXNC`-branch value
  `237`, for MAX — not hand-verified digit-by-digit in this write-up for space, but independently
  recomputed by the exhaustive search code).

**Consistency check: the full Peeling-Lemma decomposition (§11.2) still reproduces the true
`OPT(Y,p-1)`/`NC(Y,p-1)$ exactly** in every one of the `420+420` trials of §11.2 — confirming that
proving the aggregated Small-Gap Crossing-Domination Lemma (plus the already-fully-proved
DELETE/KEEP branches and the base cases `p\le2` or so, checked directly) would indeed close
`OPT(Y,p-1)=NC(Y,p-1)` by strong induction on `p`, exactly as the round-8 outline intended — only
the *precise form* of the shared lemma needed correction (aggregated, not per-partner).

#### 11.5 Honest assessment — what is proved, what remains open

- **Proved in full, this round (general, promotable):** the Extreme-Element Peeling Lemma (§11.2)
  — an unconditional, general-purpose exact decomposition of `OPT(Y,b)` and `NC(Y,b)` for *every*
  sorted `Y` and budget `b`, fixing the reviewer's precisely-identified imprecision with a genuine
  proof (two bijection arguments plus one direct application of the certified Fact 3 and the
  certified Non-crossing inside/outside independence lemma — no new unproven machinery).
- **Refuted, this round (a real negative result, do not re-attempt):** the natural *per-fixed-`j`*
  reading of the Small-Gap Crossing-Domination Lemma — exact counterexample at `p=4$ (§11.3),
  hand-verified, plus `484` further computational instances confirming it is not an isolated
  fluke.
- **Correctly restated and extensively re-supported, still NOT proved:** the *aggregated*
  (min-over-`j`, resp. max-over-`j`) form of the Small-Gap Crossing-Domination Lemma (§11.4) —
  `2060` fresh exact-integer trials, zero mismatches, `p` up to `9`. This is now the single,
  precisely-correct remaining open lemma for the whole `OPT(Y,p-1)=NC(Y,p-1)` program (mutual with
  its `MAXOPT/MAXNC` companion at gap `0`, exactly as the outline anticipated structurally, now
  with the exact statement pinned down correctly).
- **No proof attempt of the aggregated lemma was completed this round** (time did not allow it
  after the decomposition proof and the counterexample search) — the natural next idea, not yet
  tried, is to show that whenever `INSERT_OPT(y_1-y_j,Z_j,p-2)$ strictly beats
  `INSERT_NC(y_1-y_j,Z_j,p-2)$ via a crossing arc `(a,c)` (`a$ inside, `c` outside), there is
  always an *alternative* partner `j'` (plausibly `j'=a$ or `j'=c`, i.e. re-routing `y_1`'s match
  to one endpoint of the crossing arc that "caused the trouble," as in the `p=4` example above
  where switching from `j=3` to `j=2$ — `y_2` being the *inside* endpoint of the winning crossing
  arc `(y_2,y_4)` at `j=3` — recovered the same value) for which `INSERT_NC` already matches or
  beats the original `INSERT_OPT` value. This "re-route to an endpoint of the offending crossing
  arc" idea is a concrete, checkable next step, **not yet attempted or verified this round** — it
  is flagged here as the most promising honest lead, not claimed as a proof.
- **Do not re-propose:** the per-fixed-`j` form of the lemma (§11.3, refuted); treating the MATCH
  branch as a literal recursive `OPT`/`NC` call on a list containing the produced difference as an
  ordinary further-selectable element (refuted independently by the reviewer and reconfirmed here).

## §12 (round 9 outline) — recursive strong induction on `p`, anchored by a new full-slack base
case; the "re-route to an endpoint" lead is now a confirmed dead end, do NOT use it

This round's explorer (`math-explorer-crossing-domination.md`) independently reproduced §11's
counterexamples/support and, per dispatch, tested the two concrete leads §11.5 left open. **One
is refuted outright; one new unconditional anchor is found.** This section replaces §11.5's "next
step" paragraph with a corrected, sharper plan.

### 12.0 Dead end confirmed this round — do NOT pursue "re-route to an endpoint of the crossing
arc" as a one-step surgery

§11.5 flagged, as its most promising untried lead, re-routing `y_1`'s partner from the mismatching
`j` to an endpoint (`a` or `c`) of the crossing arc `(a,c)` that caused `INSERT_OPT<INSERT_NC` at
that `j`. **This is now refuted**: on `400` random trials (`p` up to `7`, `347` observed per-`j`
mismatches), the endpoint-reroute recovers the aggregate optimum in `~86%` of cases but **fails in
`~14%`** — concrete counterexample `Y=(463,461,372,291,237,180)`, mismatch at `j=4` (crossing arc
`(2,5)`); neither endpoint `j'=2` nor `j'=5` recovers the optimum (`3\ne2`); the true compensating
partner is `j'=1` (matching `y_1,y_2`), whose winning selection is **pure deletion, structurally
unrelated to the crossing arc**. A weaker fallback ("the two extremes `j=1,p` always suffice")
also fails (`~19%` of `500` trials). **Conclusion: the compensating structure is not local — do
not build a proof around a one-step re-route of `y_1`'s partner.** Any future use of this idea
would need to be a fully recursive/global re-routing (a chain of several arcs) or a genuine
global counting/injection argument, not a one-shot swap; not attempted here.

### 12.1 New unconditional anchor — the "full-slack degenerate-split" base case

At the two extreme partners `j=1` (inside empty) and `j=p` (outside empty), the split is
*degenerate* (only one side is nonempty), and the sub-budget passed to `INSERT_OPT`/`INSERT_NC`
always equals `|Z_j|=p-2` exactly, i.e. **full slack, no genuine split**. This round's explorer
verified, in `1300` zero-failure trials, that `INSERT_OPT=INSERT_NC` holds **unconditionally**
(not just in the aggregate) whenever `j\in\{1,p\}`, and isolated the load-bearing condition
precisely: testing the fully general, un-tagged claim "`INSERT_OPT(v^\dagger,Z,b'=|Z|)=
INSERT_NC(v^\dagger,Z,b'=|Z|)` for *arbitrary* `v^\dagger\ge0`, arbitrary sorted `Z`, budget
exactly `|Z|`, no inside/outside split at all" gives `500/500` zero-failure trials. **This is a
clean, self-contained, `m`-independent structural fact, plausibly provable outright by the same
family of argument as the certified Fact 5 (chain-cancellation/full-budget achievability,
`lemmas/insertion-and-cascade-facts.md`)** — at full slack (`b'=|Z|`), *every* index of `Z` can be
independently deleted or matched with no budget constraint biting, so a non-crossing selection
never has to forgo a crossing match purely for budget reasons; the only way `INSERT_OPT` could
still beat `INSERT_NC` is via the actual crossing-vs-non-crossing *value* difference, which this
sub-lemma's own base-case scope (no genuine inside/outside split) removes entirely. **This gives
an unconditional anchor at 2 of the `p-1` candidate partners** — not by itself the aggregate
result (extremes don't always carry the global optimum, per §11.5's own numeric observation), but
a genuine, provable base case for an induction.

**Key sub-lemma to prove first (open gap, concrete, bounded):**
```
Full-Slack Insertion Lemma. For any v^\dagger\ge0 and any sorted Z=(z_1\ge...\ge z_q),
  INSERT_OPT(v^\dagger, Z, q) = INSERT_NC(v^\dagger, Z, q)      (budget = |Z| exactly, no split).
```
*Proposed mechanism:* at budget `=|Z|`, every element of `Z` can individually be deleted (cost 1
each), so `INSERT_OPT`'s optimal selection can always be "simulated" by a sequence of pairwise
non-crossing matches/deletions that achieves the same final multiset value — because a crossing
match `(z_i,z_k)`, `i<k`, contributing `|z_i-z_k|` to the multiset, can be replaced (at full
slack) by deleting the *smaller* of `z_i,z_k` and keeping the larger's role played by a
different index without changing the multiset up to the target `e`... **(this replacement step
is the actual hard content and is NOT yet spelled out rigorously — it is exactly the kind of
"full budget removes all obstructions" argument the certified Fact 5 already carries out for the
non-inserted case; adapting Fact 5's own proof technique, not just its statement, to the
inserted-`v^\dagger` setting is the concrete task).** Builder: attempt this first, by hand, on 2–3
small cases (`q=2,3`) before generalizing.

### 12.2 Main skeleton — recursive strong induction on `p`, peeling `Z_j`'s own extreme element

**Target:** the aggregated Small-Gap Crossing-Domination Lemma,
`\min_j INSERT_OPT(y_1-y_j,Z_j,p-2) = \min_j INSERT_NC(y_1-y_j,Z_j,p-2)`, by strong induction on
`p` (equivalently on `|Z_j|=p-2`), using the *already-certified* Extreme-Element Peeling Lemma
(§11.2) applied **one level deeper** — inside the computation of `INSERT_OPT`/`INSERT_NC`
themselves, not just at the top level of `OPT`/`NC`.

**Technique:** direct proof by strong induction (the same overall spine as §11's Peeling Lemma,
recursed one level), carrying the externally-fixed value `v^\dagger` as an inert background
element through every level of the recursion.

**Skeleton:**
1. **Base case `q=|Z|\le1`:** `INSERT_OPT=INSERT_NC` trivially (at `q\le1` there is nothing to
   cross) — direct case check, no induction needed.
2. **Base case, full slack (§12.1):** whenever the sub-budget passed down equals `|Z|` exactly
   (the degenerate-split anchor, `j\in\{1,p\}` at the top level, and — new — *any* level of the
   recursion where the remaining budget happens to equal the remaining list size), equality holds
   unconditionally by the Full-Slack Insertion Lemma (§12.1, once proved).
3. **Inductive step, general `q,b'<q`:** apply the same trichotomy the Extreme-Element Peeling
   Lemma used at the top level, now to `Z`'s own first (largest) element `z_1`, **with `v^\dagger`
   carried as a permanent extra background element throughout**:
   - `z_1\in D` (delete): `INSERT_OPT(v^\dagger,Z,b') \to INSERT_OPT(v^\dagger,Z\setminus\{z_1\},b'-1)`
     — same bijection argument as §11.2's DELETE branch (`v^\dagger` untouched, so the bijection's
     value-preservation proof carries over verbatim). Reduces to a strictly smaller `q`, IH applies.
   - `z_1\in K` (keep): now the fixed multiset going into `e` is `\{v^\dagger,z_1\}\cup W`(residual)
     — **this is the one genuinely new sub-case relative to §11.2**, since (unlike the top level,
     where `y_1` is always the global max) the relative order of `v^\dagger` and `z_1` is *not*
     fixed (`v^\dagger=y_1-y_j` can be larger or smaller than `Z_j`'s own top element, depending on
     `j`). **Open gap:** the telescoping/Fact-3 block-extraction argument that closed §11.2's KEEP
     branch needs the extracted element to be the current maximum — here it must be case-split on
     `v^\dagger\gtrless z_1` (2 sub-cases, each individually tractable by the same Fact-3 mechanism
     applied to whichever of `\{v^\dagger,z_1\}` is larger, but this case split is not yet written
     down). Either way it reduces to a `MAXINSERT`-type quantity (the max-companion of
     `INSERT_OPT`/`INSERT_NC`, analogous to `MAXOPT`/`MAXNC`) on `Z\setminus\{z_1\}` at the same
     budget `b'` — define this companion explicitly (mirrors §11.2's `y_1-MAXOPT(...)` step) and
     handle it by the *same* induction (it satisfies an identical recursive structure, by symmetry
     of the argument under `\min\leftrightarrow\max$).
   - `z_1` matched to some `z_k`, `k>1` (match): reduces to a **second level of insertion** —
     `INSERT_OPT` with **two** externally-fixed background values, `v^\dagger` and `z_1-z_k`, on
     the residual `Z\setminus\{z_1,z_k\}` at budget `b'-1`. **This is the key structural
     observation making the induction self-similar**: the natural generalization is to redefine
     `INSERT_OPT`/`INSERT_NC` to take a *finite set* of externally-fixed background values (not
     just one), so that peeling never leaves the family — `INSERT_OPT(\{v^\dagger\},Z,b')` peels
     to `INSERT_OPT(\{v^\dagger,z_1-z_k\},Z\setminus\{z_1,z_k\},b'-1)`, and so on. State and prove
     the generalized Peeling Lemma **for this whole family at once** (any finite background set,
     not just size 0 or 1), by the identical bijection arguments as §11.2 (none of those bijection
     proofs used anything about the background set being empty or a singleton — re-check this
     explicitly, it is likely a costless generalization, not a new obstruction).
4. **Close the induction:** with the base cases (1)-(2) and the generalized inductive step (3), a
   strong induction on `q=|Z|` (equivalently on the size of the background set plus `|Z|`, which
   strictly decreases at every step) proves the generalized `INSERT_OPT=INSERT_NC` family for
   *every* background set and every `q,b'`; specializing to background set `=\{y_1-y_j\}` and
   taking `\min_j` over the top level recovers exactly the aggregated Small-Gap
   Crossing-Domination Lemma.

**Key lemmas (claim + mechanism):**
- **Full-Slack Insertion Lemma** (§12.1) — because at budget `=|Z|` no crossing match is ever
  forced by budget scarcity, so the crossing/non-crossing value gap collapses; base case for the
  whole induction. **Open, not proved.**
- **Generalized (multi-background) Extreme-Element Peeling Lemma** — because the three
  bijection arguments proving §11.2's Peeling Lemma (DELETE/KEEP/MATCH) never actually used that
  the background set has size `\le1`; extending to arbitrary finite background sets should be a
  direct re-run of the same three proofs with an extra inert set of constants carried through.
  **Open, not proved, but plausibly a free generalization — the concrete task for the builder.**
- **KEEP-branch order case split** (`v^\dagger\gtrless z_1`) — because Fact 3's block-extraction
  identity needs its extracted singleton to be the current max; here the max of
  `\{v^\dagger\}\cup\{\text{remaining }Z\}` is not always `v^\dagger`, so the case split routes to
  whichever of `\{v^\dagger,z_1\}` is larger. **Open, but a bounded 2-way case check, not a new
  mechanism.**

**Open gaps:** the Full-Slack Insertion Lemma (§12.1); the Generalized Peeling Lemma's
multi-background extension (§12.2 step 3); the KEEP-branch order case split. None of these
requires new machinery beyond what is already certified (Fact 3, Fact 5, the Extreme-Element
Peeling Lemma's own bijection technique) — the task is to re-run existing proof techniques one
level deeper and with a generalized background-set bookkeeping, not to invent a new mechanism.

**Cases to cover:** the two base cases (§12.2 steps 1–2, including whichever level of the
recursion first hits full slack, not just the top level); the KEEP branch's `v^\dagger\gtrless z_1`
split; the MATCH branch's background-set growth (must confirm growth stays finite/terminating —
it does, since `|Z|` strictly decreases by 2 and the background set grows by exactly 1 each MATCH
step, and every recursive call has strictly smaller `|Z|+b'`, so ordinary strong induction on
`|Z|` terminates).

**Watch out for:** (1) do not silently assume `v^\dagger` is always the maximum of the working
multiset when applying Fact 3 — this failed exactly at the top level in the round-8 build's
careful KEEP-branch proof (§11.2) only because `y_1` genuinely is always the max there; one level
deeper this is **not** automatic and must be case-split explicitly (see above). (2) Confirm the
generalized multi-background Peeling Lemma's MATCH branch really does terminate with a
*shrinking* combined parameter (`|Z|` strictly decreases, background set size only grows by
exactly 1 per MATCH step, net `|Z|+b'` still strictly decreases) — do not let an unbounded
"background set could grow arbitrarily large across levels" concern block the induction; it
provably cannot exceed `p` total insertions since each MATCH step consumes one unit of the
original, finite total budget.

### 12.3 Untried proof-shape lead: crux `aimo-0558`'s forced-inclusion/charge-to-distinct-skip

Flagged (not attempted) by this round's plateau-break explorer (`math-explorer-n-general.md`):
crux `aimo-0558` (ISL-style `\pm1`-sequence, gap-`\le2` subsequence problem) proves its matching
upper bound via a **forced-inclusion charged to a distinct skipped element** argument — any
admissible selection touching `k` "majority blocks" is forced to draw `\ge1` element from each of
the `k-1` intervening "minority blocks" between them, capping the excess via a per-block charging
scheme, with a companion greedy achievability argument (take majority, skip a minority element
only when forced, charge every forced-keep to a distinct skip). This is a genuinely different
proof *shape* from the recursive-peeling route above — instead of inducting on `p`, it would
directly bound `OPT-NC` (or witness their equality) via an injective charging map from
"NC-suboptimal instances" to "a distinct structural feature of `Y` that bounds the gap." **Not
attempted this round** (out of scope for the crux-assessment lens); flagged as a genuine fallback
technique if §12.2's recursive induction stalls on the KEEP-branch order case split or the
multi-background generalization. A builder pursuing this should first translate `aimo-0558`'s
"majority/minority block" structure into this problem's language (candidate translation, untested:
"majority block" ~ a run of `Y`-elements matched among themselves in the `NC`-optimal solution;
"minority block" ~ elements between two crossing partners in the `OPT`-optimal solution) before
attempting to adapt the charging argument itself.

### 13. Round 9 build — the Full-Slack Insertion Lemma proved in the degenerate-split case, the
General Rank-Extraction Identity (new, closes the KEEP-branch order case split in full), and a
precise unification finding: the recursive route (§12.2) does not provide independent leverage —
its hard case is *exactly* the aggregated lemma, not a strictly easier sub-case

All computations in this section are exact-integer (Python `int`), fully reproducible
(`/tmp/round-9/work/fullslack.py`, `/tmp/round-9/work/verify_decomp.py`), and every check is over
a genuinely exhaustive enumeration of the finite selection space (no heuristic pruning; only test
instances are randomly generated).

#### 13.1 The General Rank-Extraction Identity (new, fully proved, promotable)

Fact 3 (block extraction) extracts the *maximum* of a multiset with a clean sign. The KEEP branch
of a multi-background Peeling Lemma needs to extract a *general-rank* element (the peeled list's
own top element `z_1`, which is **not** always the max of the *combined* working multiset once an
external background `B` is present — `B` may contain values exceeding `z_1`, unlike at the top
level of the original Peeling Lemma, where `y_1` genuinely is the global max). This round proves,
in full and in general (not just for the top-level case), the tool needed:

**General Rank-Extraction Identity.** For a sorted multiset `F`, an element `x\in F` at sorted
rank `r`, `\text{head}` = the `r-1` elements ranked above `x`, `\text{tail}` = the elements ranked
below `x`:
```
e(F) = e(\text{head}) + (-1)^{r-1} x + (-1)^r e(\text{tail}).
```
*Proof.* Apply the certified Fact 3 twice: first split `F=\text{head}\sqcup(\{x\}\cup\text{tail})`
(`\text{head}` dominates `\{x\}\cup\text{tail}` elementwise by definition of rank), giving
`e(F)=e(\text{head})+(-1)^{r-1}e(\{x\}\cup\text{tail})`; then split
`\{x\}\cup\text{tail}=\{x\}\sqcup\text{tail}` (`x` dominates `tail` by definition), giving
`e(\{x\}\cup\text{tail})=x-e(\text{tail})`. Substituting gives the claim. `\blacksquare`

This generalizes Fact 3 itself (`r=1` case: `\text{head}=\emptyset`, recovering `e(F)=x-e(\text{tail})`).
**Independently verified: 3000/3000 exact-integer random trials (`n=1,\dots,8`), zero mismatches.**
Certified as `lemmas/general-rank-extraction-identity.md`.

#### 13.2 The Generalized Multi-Background Peeling Lemma — DELETE and KEEP branches fully closed,
MATCH branch's bijection is free but its *aggregate content* is not (correcting the outline's
framing)

**Setup.** For a finite background multiset `B` (nonnegative reals, external/fixed, never
selectable), a sorted list `Z=(z_1\ge\dots\ge z_q)`, and a sign `\sigma\in\{+1,-1\}`, define (at
**full slack**, i.e. budget `=|Z|`, which — as shown below — is *always* the regime this
problem's recursion actually needs):
```
\mathrm{OPT}_\sigma(B,Z) := \sigma\text{-optimal (min if }\sigma=+1\text{, max if }\sigma=-1\text{)
                             value of } e(B\cup K\text{-values}\cup M\text{-differences})
                             \text{ over ALL selections }(K,D,M)\text{ of }Z\text{ (no crossing
                             restriction at all).}
\mathrm{TAGGED}_\sigma(B,Z,s) := \text{same, restricted to selections that are non-crossing AND
                             contain no matched pair spanning the split at position }s\in\{0,\dots,|Z|\}.
```
`\mathrm{OPT}_\sigma(B,Z)` and the **degenerate**-split case `\mathrm{TAGGED}_\sigma(B,Z,0)` (or
`s=|Z|`, equivalently — the split is empty on one side, so "spans the split" is vacuous, matching
the "no split at all" reading) recover exactly `\mathrm{OPT}`/untagged-`\mathrm{NC}` in §11/§12's
own notation (`B=\{v^\dagger\}`, `\sigma=+1`: `\mathrm{OPT}_{+1}(\{v^\dagger\},Z)=
\mathrm{INSERT\_OPT}(v^\dagger,Z,|Z|)`). **Full-slack is automatically the only regime that
matters**: for a size-`q` list, `\mathrm{cost}=|D|+|M|=q-|K|-|M|\le q` for *every* selection
(elementary index count `|K|+|D|+2|M|=q`), so budget `\ge q` is never a real restriction — and
every instance this problem's recursion ever generates already has budget exactly equal to list
size (§11.3 already noted this for the top-level `\mathrm{INSERT\_OPT}/\mathrm{INSERT\_NC}`
instances; it remains true at every recursion depth below, since DELETE decreases both budget and
size by `1`, KEEP decreases size by `1$ at unchanged budget (strictly *more* slack), and MATCH
decreases size by `2` and budget by `1` (still exactly full slack for the new size `q-2`, budget
`q-1\ge q-2`). So dropping the explicit budget argument entirely, as done here, costs nothing.

**Trichotomy on `z_1$'s fate** (exhaustive, mutually exclusive, exactly as in §11.2, now for a
general background `B` and sign `\sigma`):

- **DELETE** (`z_1\in D`): the same bijection as §11.2's DELETE branch (deleting `z_1` from `D`
  is a bijection onto selections of `Z\setminus\{z_1\}`, value-preserving, since `B` is
  completely untouched by this map). Gives branch value `\mathrm{OPT}_\sigma(B,Z\setminus\{z_1\})`
  (resp. `\mathrm{TAGGED}_\sigma(B,Z\setminus\{z_1\},0)` on the NC side — no split is introduced,
  since deleting `z_1` cannot create or remove any crossing). **Free generalization — the exact
  same bijection proof as §11.2, `B` and `\sigma$ irrelevant to the argument.**

- **KEEP** (`z_1\in K`): every element of the residual working multiset built from
  `Z\setminus\{z_1\}` (call it `W`) is `\le z_1` (exactly as in §11.2: kept `z_i,i\ge2\le z_2\le
  z_1`; differences `z_i-z_k\le z_i\le z_2\le z_1`), so `z_1$ is the max of `\{z_1\}\cup W` — but
  **not necessarily the max of `B\cup\{z_1\}\cup W`**, since `B$'s elements can exceed `z_1`. Let
  `h:=|B_{\text{hi}}|` where `B_{\text{hi}}:=\{b\in B: b>z_1\}` (ties broken to `B_{\text{lo}}`,
  WLOG — `e` is invariant under how equal elements are ordered). By the **General Rank-Extraction
  Identity** (§13.1), applied with `x:=z_1$ at rank `r=h+1$ in `F:=B\cup\{z_1\}\cup W`
  (`\text{head}=B_{\text{hi}}`, `\text{tail}=B_{\text{lo}}\cup W`):
  ```
  e(F) = e(B_{\text{hi}}) + (-1)^h z_1 + (-1)^{h+1} e(B_{\text{lo}}\cup W).
  ```
  `e(B_{\text{hi}})$ and `(-1)^h z_1` do not depend on `W`, so minimizing/maximizing `e(F)$ over
  the choice of `W` reduces **exactly** to minimizing/maximizing `e(B_{\text{lo}}\cup W)`, with a
  sign flip governed purely by the parity of `h`:
  ```
  \text{KEEP branch value} = e(B_{\text{hi}}) + (-1)^h z_1 + (-1)^{h+1}\cdot
       \mathrm{OPT}_{\sigma\cdot(-1)^{h+1}}\big(B_{\text{lo}}, Z\setminus\{z_1\}\big),
  ```
  and identically with `\mathrm{OPT}` replaced by `\mathrm{TAGGED}(\cdot,\cdot,0)` on the NC side
  (again no split introduced — `z_1` participates in no pair). **This is the exact closed form
  the outline flagged as an open "2-way case split" — now fully derived, not merely "individually
  tractable": it is governed by a single parity bit `h\bmod2`, reducing to a strictly smaller
  instance of the exact same family (background `B_{\text{lo}}`, size `q-1`, possibly flipped
  `\sigma`, still degenerate split).** Independently verified computationally against direct
  exhaustive search: `500/500` fresh random trials, the full DELETE+KEEP+MATCH decomposition
  (using this exact formula for KEEP) exactly reproduces the true `\mathrm{OPT}`/untagged-`\mathrm{NC}`
  value (`/tmp/round-9/work/verify_decomp.py`, second check, after fixing two bookkeeping bugs in
  the first draft of the harness — the constant offset `e(B_{\text{hi}})+(-1)^h z_1` and the
  correct background `\{v^\dagger\}$ vs `\emptyset` for the two parity cases, both must be carried
  exactly, not dropped).

- **MATCH** (`z_1` matched to some `z_k`, `k>1`): the same bijection as §11.2's MATCH branch
  (matching `z_1,z_k$ is a bijection onto selections of `Z\setminus\{z_1,z_k\}` with `z_1-z_k`
  inserted into the background) gives branch value
  `\mathrm{OPT}_\sigma(B\cup\{z_1-z_k\},\,Z\setminus\{z_1,z_k\})`, minimized/maximized over
  `k=2,\dots,q`. **The bijection itself is free** (identical argument to §11.2, `B` irrelevant).
  **But the NC-side branch is NOT `\mathrm{TAGGED}_\sigma(\cdot,\cdot,0)` (degenerate) — it is
  `\mathrm{TAGGED}_\sigma(B\cup\{z_1-z_k\},\,Z\setminus\{z_1,z_k\},\,k-1)`, a genuinely
  NON-degenerate split** (by the certified Non-crossing inside/outside independence lemma, "the
  whole selection is non-crossing, with `(1,k)` matched" is *equivalent to* — not merely
  implied by — "the residual is non-crossing on `\{2,\dots,k-1\}$, non-crossing on
  `\{k+1,\dots,q\}$, and no pair spans between them," which is exactly `\mathrm{TAGGED}$'s
  definition at a real split, whenever `2<k<q` — this is forced by the definition of crossing,
  not a modeling choice). **This is the one branch that does not reduce to a smaller instance of
  the SAME (degenerate-split) family — it reduces to a smaller instance of the STRICTLY MORE
  GENERAL (tagged, arbitrary-split) family**, confirmed by direct hand-tracing (the `p=4`
  counterexample of §11.3, `Z_3=(89,73)`, split at `k-1=1`, is literally an instance of exactly
  this MATCH-branch sub-problem) and by fresh computation this round (below).

**Summary correcting the outline's "Key lemmas" framing (per the outline-reviewer's flagged
concern):** DELETE and MATCH's *bijections* generalize to arbitrary background "for free," exactly
as the outline's first bullet claimed — **but this is not the same as saying the whole
Generalized Peeling Lemma is free.** KEEP requires genuinely new content (now supplied, §13's
exact closed form via the Rank-Extraction Identity — not "individually tractable, not yet written
down" as the outline left it, but a complete, general, parity-governed formula). And — a sharper
point than the outline-reviewer's own note — **MATCH's bijection being free does not make its
*branch value* easy**: the branch's own NC-side recursion needs the fully general TAGGED family at
a smaller size, not the easier degenerate-split family, so MATCH is the one branch that genuinely
carries forward the full difficulty of the problem, unreduced, to the next level.

#### 13.3 Precise diagnosis: the Full-Slack Insertion Lemma is not an independently-easier base
case — it is (via this exact branch accounting) equivalent in content to the aggregated Small-Gap
Crossing-Domination Lemma itself

Write `\mathrm{FSI}(q)`: "for every background `B` and every `\sigma`,
`\mathrm{OPT}_\sigma(B,Z)=\mathrm{TAGGED}_\sigma(B,Z,0)` for every `Z` with `|Z|=q$" — this is
exactly the (generalized-background) Full-Slack Insertion Lemma at size `q` (§12.1's target is the
`|B|\le1` special case).

By §13.2's decomposition, both sides of `\mathrm{FSI}(q)`'s claimed equality decompose *exactly*
(no approximation, an unconditional identity on both sides, by the same exhaustive
DELETE/KEEP/MATCH case split applied to both the unrestricted `\mathrm{OPT}_\sigma` and the
degenerate-split `\mathrm{TAGGED}_\sigma(\cdot,\cdot,0)`):
```
\mathrm{OPT}_\sigma(B,Z)         = \min/\max\big(A_1,\ A_2,\ \min/\max_k A_{3,k}\big)
\mathrm{TAGGED}_\sigma(B,Z,0)    = \min/\max\big(B_1,\ B_2,\ \min/\max_k B_{3,k}\big)
```
where (writing the min-case, `\sigma=+1`, for concreteness — the max-case is identical with every
`\min\leftrightarrow\max` swapped, by the fully symmetric argument, none of §13.2's three branch
proofs privileging `\sigma=+1` over `\sigma=-1`):
- `A_1=\mathrm{OPT}_{+1}(B,Z\setminus\{z_1\})`, `B_1=\mathrm{TAGGED}_{+1}(B,Z\setminus\{z_1\},0)` —
  by strong induction on `q` (IH `=\mathrm{FSI}(q-1)`, same background `B`), **`A_1=B_1`
  unconditionally, no new content.**
- `A_2,B_2` — the KEEP branch's exact closed form (§13.2) reduces both to
  `\mathrm{OPT}_{\tau}(B_{\text{lo}},Z\setminus\{z_1\})` / `\mathrm{TAGGED}_\tau(B_{\text{lo}},
  Z\setminus\{z_1\},0)` for the *same* flipped-or-not sign `\tau` on both sides, plus an identical
  additive constant — again, **by `\mathrm{FSI}(q-1)`, `A_2=B_2` unconditionally, no new
  content.**
- `A_{3,k}=\mathrm{OPT}_{+1}(B\cup\{z_1-z_k\},Z\setminus\{z_1,z_k\})`,
  `B_{3,k}=\mathrm{TAGGED}_{+1}(B\cup\{z_1-z_k\},Z\setminus\{z_1,z_k\},k-1)` — since `\mathrm{TAGGED}`
  is a *restriction* of `\mathrm{OPT}$'s search space, `A_{3,k}\le B_{3,k}$ trivially for every
  `k`, giving the *already-known* trivial direction `\min(A_1,A_2,\min_kA_{3,k})\le
  \min(B_1,B_2,\min_kB_{3,k})$, i.e. `\mathrm{OPT}_{+1}\le\mathrm{TAGGED}_{+1}(\cdot,0)` — nothing
  new. **The reverse inequality is the entire remaining content**, and it splits into exactly two
  cases:
  - If the global minimum `\min(A_1,A_2,\min_kA_{3,k})` is attained at `A_1` or `A_2`: then (since
    `A_1=B_1,A_2=B_2$ by IH) `\min(B_1,B_2,\dots)\le A_1$ or `\le A_2$, i.e. `\le` the global
    minimum — **done, by IH alone, no new argument needed.**
  - If the global minimum is attained *strictly* by some `A_{3,k^*}$ (beating both `A_1,A_2$ and
    every other `A_{3,k}`): we need **some** `k` (not necessarily `k^*`) with
    `B_{3,k}\le A_{3,k^*}$ — i.e. **some match partner's value is achievable within the
    non-crossing+split restriction, at least as cheaply as the (possibly different) globally
    optimal match partner's unrestricted value.** This is not automatic and is **exactly** the
    content of the aggregated Small-Gap Crossing-Domination Lemma (§11.4) — restated one level
    down, with a background of size `|B|+1$ instead of `|B|`, but **the identical shape of
    statement**, and (per the certified §11.3 counterexample, which is literally an instance of a
    single `A_{3,k}$ vs `B_{3,k}$ comparison at `|B|=2`) individual per-`k$ equality is known to
    be FALSE, so aggregation over `k` is unavoidably required here too.

**Conclusion (the honest deliverable of this round, sharper than either §12.1's or the outline-
reviewer's framing).** The recursive strong-induction-on-`q` skeleton of §12.2 is **logically
sound and well-founded** (background size grows by exactly `1` and list size shrinks by `\ge1` at
every step, so the recursion terminates — no circularity in the bad, infinite-regress sense). But
it provides **no independent reduction in difficulty**: `\mathrm{FSI}(q)`'s own inductive step, in
the one case that is not already free (IH via DELETE/KEEP), needs a smaller instance of a
STRICTLY MORE GENERAL fact — the aggregated, tagged, growing-background Small-Gap
Crossing-Domination phenomenon — which is not a "base case" logically prior to §11.4, but the
*same* statement, recursively, at every level down to the smallest cases (`|Z|=2`, one candidate
match partner, exactly the already-known `p=4` counterexample/recovery instance of §11.3/§11.4).
**In particular, the Full-Slack Insertion Lemma (§12.1) is NOT, contrary to its framing as an
"anchor"/"base case" in §12.1–§12.2, an independently easier fact that can be established first
and then cited — establishing it in general (arbitrary background, arbitrary `Z`) already requires
exactly the aggregated lemma's own content.** This does not mean §12.1's *narrow*, already-checked
special cases (`|B|\le1`, i.e. the literal Full-Slack Insertion Lemma as originally stated) are in
doubt — they remain fully consistent with `2060+`(inherited)`+3000`(this round)`+450`(reviewer)
zero-failure trials — but a *proof* of even that narrow statement, via this recursive route, would
first need the general aggregated lemma at smaller sizes, which is not known.

**A single, precisely-isolated Core Open Lemma, unifying both §12.1 and §11.4 (the honest
deliverable to hand to the next round).**
```
Match-Recovery Lemma (open). For any finite background B, sorted Z=(z_1\ge\dots\ge z_q), if
  \min_{k=2}^q OPT_{+1}(B\cup\{z_1-z_k\}, Z\setminus\{z_1,z_k\})
strictly beats both DELETE's and KEEP's branch values (§13.2), THEN there exists some
k\in\{2,\dots,q\} (not necessarily the arg-min above) with
  TAGGED_{+1}(B\cup\{z_1-z_k\}, Z\setminus\{z_1,z_k\}, k-1)  \le  \min_{k'} OPT_{+1}(\dots).
```
Proving this (for every `B,Z`, and the symmetric `\sigma=-1` companion) would close, in one shot,
**both** the Full-Slack Insertion Lemma (as its degenerate-split corollary, `B=\emptyset$ or
`|B|=1`) **and** the aggregated Small-Gap Crossing-Domination Lemma (as its top-level instance,
`B=\emptyset`, `Z=Y\setminus\{y_1\}`) — because, per this section's accounting, they are literally
the same statement at different background sizes, not two separate open items.

#### 13.4 Computational status (fresh this round, extends but does not exceed the outline's/
reviewer's own checks)

- **`|B|=1` (the literal Full-Slack Insertion Lemma, §12.1's original scope):** re-verified
  `\mathrm{OPT}_{+1}(\{v^\dagger\},Z)=\mathrm{TAGGED}_{+1}(\{v^\dagger\},Z,0)` on `3000` fresh
  random trials, `q=0,\dots,6`, integer entries up to `50` — **zero mismatches**, consistent with
  (not exceeding) the reviewer's own independent `q\le7`, `450`-trial check.
- **`|B|=2` (the Match-Recovery Lemma's smallest genuinely-recursive instance):** for `500` fresh
  trials, `q=2,\dots,7`, the *individual* per-`k` equality `A_{3,k}=B_{3,k}$ fails in `152/500`
  trials (at least one `k`) — confirming this is not a boundary artifact, it recurs at every
  background size, exactly as diagnosed. **The full three-branch decomposition (DELETE+KEEP+MATCH,
  aggregated) still reproduces the true `\mathrm{OPT}_{+1}/\mathrm{TAGGED}_{+1}(\cdot,0)` values
  exactly, `500/500`, zero mismatches** — i.e. the FULL statement `\mathrm{FSI}(q)` (aggregating
  over DELETE, KEEP, AND all MATCH partners together) continues to hold, even though the
  MATCH-only aggregate (`\min_k A_{3,k}` vs `\min_k B_{3,k}`, ignoring DELETE/KEEP) itself fails in
  `3/500` of those trials — in those `3` cases, DELETE or KEEP alone already recovers the
  optimum, compensating for the MATCH-branch's own aggregate shortfall. **This is new information
  this round:** the Match-Recovery Lemma's own hypothesis ("match strictly beats delete and keep")
  is precisely the residual scope where genuine new content is still needed — the un-conditioned
  MATCH-only aggregate is *not* generally true by itself (an important correction: a naive
  "`min_k A_{3,k}=\min_k B_{3,k}$ always" strengthening of the Match-Recovery Lemma is **FALSE**,
  refuted by these `3` counterexamples among the `500` trials — do not attempt to prove that
  stronger, unconditional form).

#### 13.5 Honest assessment

- **Proved in full, general, promotable:** the General Rank-Extraction Identity (§13.1); the
  Generalized Multi-Background Peeling Lemma's DELETE and KEEP branches, with KEEP's exact closed
  form (§13.2) — genuinely closing the outline-reviewer's flagged gap (KEEP is not "free," but is
  now fully derived, not merely case-split-and-deferred).
- **A precise, verified (not merely asserted) diagnosis, new this round:** the recursive
  strong-induction-on-`q` route of §12.2 is well-founded but does not reduce the problem's
  difficulty — its one non-free branch (MATCH) reduces to a smaller instance of the *same* general
  phenomenon (the aggregated crossing-domination equality), not an easier fact. This shows the
  Full-Slack Insertion Lemma (§12.1) is not logically prior to/independent of the main open lemma
  (§11.4) as its "anchor"/"base case" framing suggested — they are the same statement. **This
  redirects, with precision, where future effort should go:** a proof of the single unified
  **Match-Recovery Lemma** above (via a genuinely different, non-recursive technique — e.g. the
  untried `aimo-0558` charging-argument lead of §12.3, or a fresh global/injective argument) is now
  the correctly-scoped single remaining target, in place of treating §12.1 and §11.4 as two
  separate open items.
- **Not proved this round:** the Match-Recovery Lemma itself (central remaining gap, unchanged in
  ultimate difficulty, but now more precisely characterized and shown to unify two previously
  separately-tracked open lemmas into one).
- **A genuine negative sub-result, new this round:** the naive unconditional strengthening of
  Match-Recovery ("the MATCH-branch aggregate alone, ignoring DELETE/KEEP compensation, always
  matches") is **FALSE** (§13.4, `3/500` exact counterexamples) — do not attempt to prove that
  form; the DELETE/KEEP-compensation escape hatch in the Match-Recovery Lemma's own hypothesis
  ("...strictly beats both DELETE's and KEEP's branch values...") is load-bearing, not a
  convenience.

#### 13.6 Round 10 correction (proof-outliner, per `math-explorer-direct-attack.md`) — the
generalized Full-Slack Insertion Lemma / unified Match-Recovery Lemma of §13.2-13.3, for arbitrary
flat background `B` with `|B|\ge2`, is FALSE — formally retired, do NOT re-attempt in this form

**This is a decisive negative result, not an unproved conjecture — record it as a permanent dead
end for this exact formalism.**

**Minimal counterexample (hand-verifiable, triple-checked: two independent codebases + by-hand
arithmetic).**
```
B = {2,4},   Z = (6,3,2,1)   (q=4, |B|=2)

OPT_{+1}(B,Z) = 0:
  achieved by the CROSSING selection MATCH(z_1=6,z_3=2)=4, MATCH(z_2=3,z_4=1)=2, giving the
  combined multiset B ∪ {4,2} = {2,4,4,2} = {4,4,2,2}, e({4,4,2,2}) = 4-4+2-2 = 0.

TAGGED_{+1}(B,Z,0) = 1:
  the value "4" can only be produced as 6-2 (the only pair of Z-values differing by 4), and once
  index 2 (value 2) is consumed there, the only way to also produce a second "2" is MATCH(3,1).
  But the two matches (z_1,z_3)=(6,2) and (z_2,z_4)=(3,1) CROSS (positions 0<1<2<3, arcs (0,2) and
  (1,3) interleave) — forbidden under the non-crossing restriction TAGGED imposes. Exhaustive check
  of all 5 remaining candidate non-crossing/keep/delete combinations on Z gives e≥1 in every case,
  so TAGGED_{+1}(B,Z,0)=1 exactly.

Hence OPT_{+1}(B,Z) = 0 ≠ 1 = TAGGED_{+1}(B,Z,0).  §13's claimed FSI(4) equality FAILS.
```

**Confirmed three independent ways** (per `math-explorer-direct-attack.md`, not merely asserted):
(1) the minimal instance above, by hand; (2) two independently-coded exact-integer harnesses agree
on it and on a fresh random sweep replicating §13.4's own methodology (`q=2..7`, `|B|=2`, `500`
trials): **`22/500` mismatches (4.4%)** — directly contradicting §13.4's claimed `500/500`
zero-mismatch result (§13.4's own harness apparently missed these; the discrepancy is now resolved
in favor of the fresh, independently-reproduced failure, not the original claim); (3) a
*reachability* check confirms this is not a "constructed-but-unreachable `B`" artifact — simulating
genuine two-level top-down MATCH peeling on random `Y` (`p=7..9`) and testing the resulting
*actually-reachable* `(B,Z)` states still finds `5/300` failures (`~1.7%`). **Control (rules out a
systematic bug):** the same harnesses find **zero** failures at `|B|=0` (`400` trials) and `|B|=1`
(`400` trials) — matching every prior round's independent verification of the narrower (`|B|\le1`)
claim exactly; the failure is precisely localized to `|B|\ge2`.

**Why it breaks — a structural diagnosis, not just a counted failure.** `TAGGED_\sigma(B,Z,s)`
treats `B` as a **flat multiset of values with no memory of the arcs/original indices that produced
them.** This loses nothing at `|B|\le1` (a single external value's rank/sign relative to a sorted
list is a scalar fact, exactly what Fact 3/the General Rank-Extraction Identity compute). At
`|B|\ge2`, the *mutual crossing relationship between the background-generating arcs themselves* (or
between a background arc and a current match in `Z`) is exactly the information a flat value set
discards — and the minimal counterexample above is precisely a case where the winning `OPT`
selection needs its two match-generating arcs, `(6,2)` and `(3,1)` in original-index terms, to
cross each other; nothing in the flat-`B` formalism can express "these two background-producing
arcs already cross," because `B` no longer remembers they came from arcs at all.

**Formal verdict.** §13.2's Generalized Multi-Background Peeling Lemma's DELETE/KEEP branches
(§13.2, and the General Rank-Extraction Identity §13.1 they rely on) remain **fully valid and
certified** — the counterexample does not touch them, only the further claim built on top. But
**§13.3's "Core Open Lemma" / Match-Recovery Lemma, and hence the entire §12.2 recursive
strong-induction-on-`p` skeleton it was meant to close (which needs the identity at every
`|B|\ge2`, growing without bound as the recursion deepens), is now known to be unprovable as
stated — not merely stuck.** **DEAD END — do not re-attempt proving `\mathrm{OPT}_\sigma(B,Z)=
\mathrm{TAGGED}_\sigma(B,Z,0)` for arbitrary flat `B` with `|B|\ge2` in this form.** A correct
generalization, if this route is revisited, would need the induction's invariant to carry a
**non-crossing-tagged history** for every background element (which interval of original indices
its generating arc spanned, forbidding any new match from crossing *any* previously-recorded arc —
not just checking against the current split point `s`) rather than a flat value set — a strictly
richer bookkeeping, not attempted here, and not the route pursued this round (see §14 instead,
which sidesteps the whole recursive-background-set architecture).

**What is NOT threatened by this finding:** the top-level target itself, `OPT(Y,p-1)=NC(Y,p-1)`
(`|B|=0`), continues to hold in every trial tested (`400/400` fresh, consistent with `2200+` in
prior rounds) — only the specific recursive *proof strategy* pursued in §12-§13 for it is refuted,
not the truth of the theorem's needed fact.

### 14. Round 10 — NEW primary route: the Fixed-Support Uncrossing Conjecture (replaces §12.2's
recursive background-set skeleton; a genuinely non-recursive, local-exchange mechanism, correctly
scoped to the exact budget regime the theorem needs)

**Target.** The same top-level fact §12/§13 were built to establish:
`OPT(Y,p-1) = NC(Y,p-1)` for every sorted `Y=(y_1\ge\dots\ge y_p)` — the single remaining lemma
that, combined with the already-certified chain-prefix+tail rescoping (§9.4) and Slack Collapse
(§7.1), closes the entire upper-bound direction of the theorem, every `m`, every `n`.

**Technique.** Direct local-exchange/uncrossing argument on a FIXED optimal selection's support
(not an induction on list size `p`, not a growing background set) — strong induction on the
**number of crossings** in the matching `M` of an `OPT`-achieving selection, using the certified
Fact 3 / General Rank-Extraction Identity (`lemmas/general-rank-extraction-identity.md`) to track
the exact sign of `e()`'s change under one uncrossing swap. This is a fundamentally different proof
*shape* from §12/§13 (no recursive background-set bookkeeping needed at all).

**Precise statement (Fixed-Support Uncrossing Conjecture, per `math-explorer-plateau-check.md`,
independently computationally validated this round).** Fix sorted `Y`, budget `b=p-1` exactly (the
only budget the chain-prefix+tail construction ever actually needs, §9.4). Let `(K,D,M)` be ANY
selection achieving `OPT(Y,p-1)`. If `M` has a crossing (two matched pairs `(i,j),(i',j')` with
`i<i'<j<j'`), then re-pairing the SAME support `\bigcup M` (same matched index set, same `K`, same
`D` — only `M`'s internal pairing changes) into a non-crossing perfect matching `M'` on that support
achieves `v(K,D,M')\le v(K,D,M)=OPT(Y,p-1)`.

**Why this suffices.** If true: take any `OPT`-achieving selection, uncross its matching in place
(bounded number of swaps, see below), obtaining a *non-crossing* selection with value `\le OPT`.
Combined with the trivial direction `NC(Y,p-1)\ge OPT(Y,p-1)` (already established, §9.2 — `NC` is
a restriction of `OPT`'s search space), this forces `NC(Y,p-1)=OPT(Y,p-1)` exactly. **No recursive
background-set machinery, no aggregation over "which partner recovers the value" — the same
support is kept throughout, only its internal pairing changes.**

**Why this is NOT the already-dead round-6/7 "local pairwise uncrossing-exchange" mechanism (a
critical distinction, verified this round, not merely asserted).** The round-6/7 dead end (see
`run_state.md`'s DEAD END list, and §8 below in this file) killed a *different, more general*
claim: at an *arbitrary*, possibly loose budget `b`, a locally-frozen support's crossing pairing
can always be beaten by a same-support non-crossing alternative — refuted because "the global
optimum changes WHICH elements participate in a match, not just how a fixed support is re-paired"
(exact counterexample `Y=(43,33,20,16,11,8,2)`). **This round's explorer directly re-tested that
exact counterexample instance, restricted to `b=p-1`, and it does NOT fail there** — along with 4
other known adversarial instances on file (`Y=(92,89,77,73)`, `Y=(39,36,30,28,22,18,14)`,
`Y=(400,218,194,187,169,27,3)`, `Y=(463,461,372,291,237,180)`), all zero-failure at `b=p-1`. The
Fixed-Support Uncrossing Conjecture is a strictly NARROWER claim (restricted to the tight budget
regime `b\ge p-2`, and it never asks the support itself to change, only its internal pairing) that
the round-6/7 counterexamples (all found at loose/general budgets) never actually tested.

**Skeleton:**
1. **Reduce to a single swap type.** Any crossing matching on a finite point set can be sorted
   into a non-crossing one by a finite sequence of elementary "uncrossing swaps": pick any crossing
   pair `(i,j),(i',j')` (`i<i'<j<j'`), replace by the nested alternative `(i,i'),(j,j')` OR the
   other nested alternative `(i,j'),(i',j)` (`i<i'<j<j'`, which is also non-crossing relative to
   this pair, though it may cross others) — by the classical fact that the number of crossing pairs
   in a chord diagram on `2r` points strictly decreases under a correctly-chosen local swap, at most
   `\lfloor|M|/2\rfloor` such swaps fully sort any matching into non-crossing/laminar form. Strong
   induction on the number of crossings in `M`.
2. **Base case, `|M|=2` (a single crossing pair, nothing else matched).** Show directly (small,
   bounded computation): for `Y`'s two matched pairs `(i,j),(i',j')` with `i<i'<j<j'`, re-pairing
   to `(i,i'),(j,j')` (or the other nesting) does not increase `e()` of the resulting merged
   multiset — this is the base case the strong induction rests on; flagged by the explorer as the
   single fastest next diagnostic (extend the existing ~200 crossing-optimal instances' code to
   check whether `|M|=2` alone, isolated from any larger matching, already carries the whole
   mechanism).
3. **Inductive step.** Given a matching with `\ge2` crossings, apply one uncrossing swap (per Step
   1) to reduce the crossing count by `\ge1`; use the certified General Rank-Extraction Identity to
   compute the EXACT change to `e()` of the full merged multiset induced by replacing the two
   swapped values with their nested-pairing replacements (the two produced difference values
   change, hence their sorted rank and sign contribution in `e()` change — this is exactly the kind
   of sign bookkeeping Fact 3/Rank-Extraction was built for); show the net change is `\le0`; recurse
   on the (strictly fewer-crossings) resulting matching by the IH.
4. **Conclude.** After at most `\lfloor|M|/2\rfloor` swaps (bounded, terminating — a classical
   crossing-number fact, not an unbounded search), the matching is fully non-crossing and `e()` has
   only weakly decreased at each step, giving `v(K,D,M')\le v(K,D,M)=OPT(Y,p-1)$, hence
   `NC(Y,p-1)\le OPT(Y,p-1)$, hence (with the trivial reverse direction) equality.

**Key lemmas (claim + mechanism):**
- **Single-Swap Non-Increase Lemma** (the hard sub-step, open) — replacing one crossing pair
  `(i,j),(i',j')` by its nested non-crossing alternative never increases `e()` of the resulting
  merged multiset — because the General Rank-Extraction Identity expresses `e()`'s dependence on
  any one element's value and sorted rank exactly (`e(F)=e(\text{head})+(-1)^{r-1}x+(-1)^r
  e(\text{tail})`), so the net change from swapping the two produced difference-values is a
  concrete, computable two-term expression in the identity's sign bookkeeping — the sign of this
  expression, not merely its existence, is the content still to be pinned down.
- **Bounded Termination Lemma** — because a chord-diagram/matching on `2r` points has a crossing
  number `\le\binom{r}{2}` that strictly decreases (by a classical, easily-provable combinatorial
  fact about interval-swap sorting of matchings) under a well-chosen single swap, so at most
  `\lfloor|M|/2\rfloor` (a much better bound than the crossing-number one — needs its own short
  proof, or a citation of the standard "any matching can be uncrossed via bubble-sort-style
  adjacent-swaps in `O(|M|)` swaps" fact) swaps suffice; termination is not itself in doubt, only
  its exact bound.

**Open gaps:**
1. The Single-Swap Non-Increase Lemma (Step 3) — the actual hard content; not yet proved, only
   computationally supported (204+ zero-failure instances at `b=p-1`, 109 at `b=p-2`, sharp
   breakdown at `b=p-3` with `25/78` failures — pinning the valid window precisely to `b\ge p-2`).
2. The exact bound on required swap depth (Step 1/4) — plausibly `\lfloor|M|/2\rfloor` or better;
   not yet proved, though termination itself (SOME finite bound) is elementary.
3. **Cheap diagnostics flagged by the explorer, do FIRST, before any general-`|M|` write-up:**
   (a) does a single uncrossing swap always suffice (i.e., is `|M|=2` — one swap fixes everything —
   or must the argument genuinely handle iterated swaps for `|M|\ge3`)? Cheap: extend the existing
   ~200-instance crossing-optimal search to also record and report the minimum swap-depth actually
   needed on each instance found. (b) Is `|M|=2` a clean, fully hand-provable base case on its own
   (i.e., can Step 2 be closed by hand in a page, using only Fact 3/Rank-Extraction), before
   attempting the general inductive step? If `|M|=2` turns out to be genuinely hard even in
   isolation, that is itself important negative information (analogous to how §12.2's own attempt
   at "just the degenerate/full-slack case" turned out to be equivalent in difficulty to the general
   claim, §13.3) — check for this trap explicitly before declaring Step 2 "easy."

**Cases to cover:** the base case `|M|=2` (Step 2); the general inductive step for `|M|\ge3`,
which itself needs a case split on WHICH pair of crossing arcs is chosen to swap first (the
classical uncrossing-lemma technique typically picks a specific canonical crossing, e.g. the
"most nested" or "leftmost" one, to guarantee progress — this choice is not yet pinned down here);
confirm the swap choice interacts correctly with `K` and `D` (the conjecture holds `K,D` fixed —
verify no swap ever needs to also move an element between `K`/`D` and `M`, which would break the
"same support" framing entirely and collapse this route back into the already-dead round-6/7
mechanism).

**Watch out for:** (1) do not let a "provably decreases the crossing count" argument silently
assume it also weakly decreases `e()` — these are logically independent claims (Step 1 handles
termination, Step 3/the Single-Swap Non-Increase Lemma handles the value bound; a builder must
prove both, not conflate them). (2) The sharp empirical cutoff at `b=p-3` (`25/78` failures) is a
real signal the mechanism genuinely needs the tight-budget regime — do NOT attempt to prove the
Conjecture for general/loose `b` (that is exactly the already-dead round-6/7 claim); scope every
lemma explicitly to `b\ge p-2`. (3) All failing `b=p-3` instances found by the explorer had
selections using strictly less than the full budget (slack even beyond the nominal budget) — check
whether "the optimal selection uses the full budget exactly" is itself a hidden hypothesis the
Conjecture's proof needs to state and use, not merely an empirical correlation to note in passing.

**Possible accounting-step imports from the crux corpus (per `math-explorer-crux-search.md`,
untested, hints only — every borrowed step must still be proven from scratch here).** If the
Single-Swap Non-Increase Lemma (or its extension to cases where a single swap DOES locally increase
`e()` but is compensated by a later swap/by `K`/`D`) needs an amortized accounting argument rather
than a purely local sign computation:
- **Opening 1 (`aimo-0043`, obstacle-charging / resource transfer between branches).** If some
  uncrossing swaps turn out to be individually value-increasing but always compensated by a
  subsequent swap or by slack elsewhere, aimo-0043's mechanism — diagnose the specific obstruction
  (here: the specific crossing arc/element forcing the increase) and charge it against a
  compensating quantity's own budget (here: perhaps against the swap count / a value drop
  elsewhere in the sequence) — is the closest structural analog for turning an existential
  "eventually it's compensated" claim into a closed accounting identity. Adaptation is untested and
  would need real construction work.
- **Opening 2 (`aimo-0558`, greedy + injective charge-to-a-distinct-witness).** If the proof instead
  wants to be constructive (build the actual non-crossing `M'` directly, rather than reason about
  `OPT` abstractly), aimo-0558's technique — run one canonical uncrossing policy (e.g. always swap
  the leftmost/most-nested crossing first) and prove an aggregate bound via an explicit injection
  from "positions where uncrossing costs value" to "a distinct compensating structural feature" —
  is the natural fit; this is the same lead already flagged in §12.3, now re-targeted at the new
  §14 mechanism instead of the retired §12.2 one.

### 15. Round 11 outliner revision — §14 refuted, Hall's theorem and 3 fresh framings recorded as
dead ends, NEW primary route: the Refined Delete-Recovery Conjecture

Per this round's three explorers (`math-explorer-charging.md`, `math-explorer-hall.md`,
`math-explorer-fresh-framing.md`; all computation exact-integer Python, code in
`/tmp/round-11/work/`, reports archived at `/tmp/round-11/`). This section supersedes §14 as the
live route and records three dead ends so no future round re-attempts them.

#### 15.1 §14 (Fixed-Support Uncrossing Conjecture) is FALSE — do not re-attempt

**Counterexample.** `Y=(7,5,4,4,3,1)`, `p=6`, budget `b=p-1=5` — exactly the theorem's own target
regime. `OPT(Y,5)=NC(Y,5)=0` (the top-level aggregate fact is unaffected). Among the `30`
selections achieving this optimum, at least one has a **crossing** matching:
`K=\emptyset,\ D=\{0,5\},\ M=\{(1,3),(2,4)\}$ (positions `1<2<3<4`, arcs `(1,3)` and `(2,4)$
interleave). Re-pairing this SAME support `\{1,2,3,4\}$ into its non-crossing alternative
(`(1,2),(3,4)$ or `(1,4),(2,3)$) strictly **increases** the value, `0\to2$ — directly violating
§14's own precise statement (`v(K,D,M')\le v(K,D,M)$ for ANY `OPT`-achieving selection with a
crossing `M`). The optimum is still recovered — but by a genuinely **different** optimal selection
already present in the same 30-element solution set, `K=\{2,3\},D=\{0,1,4,5\}$ (no match at all),
which happens to already be non-crossing (vacuously, since it has no matched pairs) — not by
repairing the crossing selection found above.

**Diagnosis.** This is the identical "existential-support, not positional" failure mode §13.6
already diagnosed for the flat-background Match-Recovery Lemma: recovery of the optimal *value*
under the non-crossing restriction does not, in general, come from locally fixing up whichever
particular optimal selection happens to have a crossing — it comes from a *different* selection
(different support, different `K`/`D`/`M` split) that was non-crossing (or differently-crossing)
all along. A "fix the support, repair the pairing" strategy — which is precisely §14's whole
proof shape (Steps 1–4, the Single-Swap Non-Increase Lemma) — cannot express this: it commits to
one fixed support from the start and never considers switching to another.

**Verdict.** **§14 (Fixed-Support Uncrossing Conjecture, the Single-Swap Non-Increase Lemma, the
whole crossing-count-induction skeleton built on it) is FALSE as stated and is retired — do not
re-attempt fixed-support/same-support uncrossing arguments for `OPT(Y,p-1)=NC(Y,p-1)` in any form.**
Combined with §13.6 (the flat-background Match-Recovery Lemma at `|B|\ge2` is FALSE), the
remaining upper-bound gap has now had **two** independently-shaped proof strategies conclusively
refuted, both for the identical structural reason: neither can express "the recovering witness may
live on a different support/background-history than the one currently being repaired." Any future
attempt at this gap should either (a) work with an aggregate/existential quantifier over the WHOLE
solution space from the start (not fix a support/background and try to repair it), as §15.4 below
does, or (b) explain concretely why this obstruction does not apply to it.

#### 15.2 Hall's-theorem / bipartite-matching reformulation — structural dead end, do not re-attempt

Investigated (per the round-10 crux-search lead) as a possible reformulation of
`OPT(Y,p-1)=NC(Y,p-1)$ / the Match-Recovery gap via `aimo-0063`'s (USAMO 2025/6, cupcakes-on-a-
circle) Hall's-theorem mechanism. **Ruled out for two independent, structural (not merely
empirical) reasons:**
1. Match-Recovery's per-level decision is a single existential quantifier ("does some partner `k`
   satisfy an inequality"), not a simultaneous multi-way system of representatives — Hall's theorem
   specialized to one right-vertex degenerates to "at least one edge exists," i.e. a verbatim
   restatement of the claim, with zero mechanism supplied.
2. Even generalized to "does a non-crossing completion of the whole matching exist achieving the
   target value," the *existence* half is always trivially true: for any point set, some
   non-crossing perfect matching always exists (nested/nearest-neighbor construction), confirmed by
   exact computation (`0` existence failures across `2000+` trials, `q\le7`, `|B|\le3`, including
   every counterexample instance already on file, e.g. the §13.6 `B=\{2,4\},Z=(6,3,2,1)` instance —
   every candidate partner `k` is non-crossingly completable there; the failure is purely a
   **value** shortfall, never an unreachable partner). There is no Hall-deficient set for the
   theorem to find.
3. Structurally: `aimo-0063`'s Hall step works because "person `P` likes arc `A`" is checked
   **independently per edge**. `e()`'s alternating sum depends on the **joint sorted rank** of
   *every* currently-selected value at once — exactly why the population's actual tools are Fact 3
   / the General Rank-Extraction Identity (§13.1), which explicitly tracks how one element's rank
   *among all others* governs its sign. There is no way to assign a per-`k` binary
   compatible/incompatible label whose Hall-feasibility is equivalent to the needed inequality.

**Verdict: RULED OUT, do not re-attempt any Hall/defect-Hall reformulation of this gap** — the
gap is a value/optimality question in a globally rank-coupled objective, structurally the opposite
of the separable, per-edge, existence-only questions Hall's theorem has content for.

#### 15.3 Three candidate "fresh whole-problem framings" — all collapse, no new leverage

Checked as candidates for a genuinely different route to the whole theorem (not patching the
Match-Recovery gap from inside the existing D/M machinery):

- **Global concavity/KKT-duality on the opening.** Re-tested directly (independent exact-`Fraction`
  BFS for `h(A,m)`, `m=1,2,3`): concavity of `h(\cdot,m)$ is **FALSE**, `10` violations in `120`
  trials (e.g. `m=2`: `h(\text{midpoint})=1/18 < (h(A)+h(B))/2=1/12`). This is not new — it
  independently reconfirms and extends to `m=3` the already-certified
  `lemmas/non-concavity-of-g-at-n2.md` (round 3). **Already dead, re-confirmed; do not propose a
  concavity/KKT-based approach again in any dressed-up form.**
- **Layer-cake "toggle-pair" recasting.** A genuinely new, verified fact (a single cut's `N(t)`
  parity flips on exactly two origin/piece-length-anchored intervals, nowhere else) — but tracing
  its consequence shows the cumulative effect of several cuts' origin-anchored toggle intervals is
  *exactly* the same alternating-sum recursion the D/M formalism already encodes (a
  measure-theoretic re-derivation of the Lemma-P cancellation mechanism, not new content). **Not a
  new attack surface — a proof built on it would hit the identical Match-Recovery wall in different
  notation.** Not recommended as a replacement framing (may be worth keeping as an expository lens
  on already-proved facts, not pursued as an attack route).
- **Merge-tree / repeated-pairwise-difference (Euclidean-algorithm-flavored) recasting.** The
  natural policies this framing suggests ("always merge the top two," "always delete/match by a
  threshold") are exactly Rule 1 / Rule 2, **already built and falsified**
  (`potential-weighting-upper-bound.md` round 3/4, exact counterexamples at `m=2,3`); the invariant
  that would make a Euclidean-style extremal argument work is already the mechanism behind the
  certified Superincreasing No-Early-Zero Lemma. **Collapses into already-explored (partly
  already-dead) territory — not a new lead.**

**Verdict: none of the three warrants a build dispatch.** All three were genuinely attempted (not
dismissed on sight) and independently found, by direct construction/computation, to either
reproduce an existing dead end or be mathematically isomorphic to already-certified machinery.

#### 15.4 NEW primary route: the Refined Delete-Recovery Conjecture

**Why this is not a relabeling of the dead §13/§14 routes.** Both §13.6 (flat-background
Match-Recovery at `|B|\ge2`) and §15.1 (§14, fixed-support uncrossing) are dead for the same
underlying reason: they try to repair/complete a *specific* structure (a growing flat background,
or a fixed support) instead of asking an existential question over the *whole* selection space
directly. The Refined Delete-Recovery Conjecture below is deliberately **scoped to `|B|\le1`
only** — exactly the regime the theorem's own top-level target and its one level of INSERT_OPT/
INSERT_NC recursion actually use (§13.2's own "Full-slack is automatically the only regime that
matters" note) — so it never needs the refuted `|B|\ge2` flat-background machinery at all, and it
is stated as a direct existential claim about the tagged aggregate, not a repair of a fixed
support.

**Setup (restating §13.2's own notation, `|B|\le1`, sign `\sigma=+1`).** Fix background `B`
(`|B|\le1`), sorted `Z=(z_1\ge\dots\ge z_q)`. Write, exactly as in §13.2/§13.3:
- `A_1:=\mathrm{OPT}_{+1}(B,Z\setminus\{z_1\})` (DELETE, unrestricted), `B_1:=\mathrm{TAGGED}_{+1}
  (B,Z\setminus\{z_1\},0)` (DELETE, tagged) — by strong induction on `q` (IH: the whole claim below
  at size `q-1`), `A_1=B_1$ unconditionally, no new content (§13.3).
- `A_2,B_2` — the KEEP branch, reduced via the certified General Rank-Extraction Identity (§13.1/
  §13.2) to `\mathrm{OPT}_\tau(B_{\mathrm{lo}},Z\setminus\{z_1\})$ /
  `\mathrm{TAGGED}_\tau(B_{\mathrm{lo}},Z\setminus\{z_1\},0)$ for the same flipped-or-not sign
  `\tau` on both sides — again `A_2=B_2$ unconditionally by IH (§13.3).
- `A_{3,k}:=\mathrm{OPT}_{+1}(B\cup\{z_1-z_k\},Z\setminus\{z_1,z_k\})`,
  `M_{\mathrm{opt}}:=\min_{k=2}^q A_{3,k}$ (MATCH, unrestricted, minimized over partners).
- `B_{3,k}:=\mathrm{TAGGED}_{+1}(B\cup\{z_1-z_k\},Z\setminus\{z_1,z_k\},k-1)`,
  `M_{\mathrm{tag}}:=\min_{k=2}^q B_{3,k}$ (MATCH, tagged aggregate).

Note `B\cup\{z_1-z_k\}$ has size `\le2` whenever `|B|\le1` — **still outside the `|B|\le1` scope
this conjecture is stated for**, so proving it does NOT recurse into the dead `|B|\ge2` family;
see the two-case induction below for exactly how this is avoided.

**Refined Delete-Recovery Conjecture (`\sigma=+1$/min side, `|B|\le1`).**
```
Whenever M_opt < A_1  (matching z_1 to its best unrestricted partner strictly beats simply
DELETING z_1) — a weaker, more easily-triggered hypothesis than "beats both A_1 AND A_2" —
the tagged/non-crossing match aggregate achieves the identical value:  M_tag = M_opt.
```

**Two-case induction this closes the whole remaining upper-bound gap (skeleton, from the charging
explorer's report, restated precisely against this file's own §13.2/§13.3 notation).**
1. **Trivial case — the global minimum is attained at `A_1` or `A_2`.** Then, since `A_1=B_1,
   A_2=B_2$ by IH, `\mathrm{TAGGED}_{+1}(B,Z,0)=\min(B_1,B_2,M_{\mathrm{tag}})\le\min(B_1,B_2)=
   \min(A_1,A_2)=\min(A_1,A_2,M_{\mathrm{opt}})=\mathrm{OPT}_{+1}(B,Z)$ (the last equality since the
   min is attained outside the match branch). Combined with the always-true
   `\mathrm{OPT}_{+1}(B,Z)\le\mathrm{TAGGED}_{+1}(B,Z,0)` (restriction of the search space), done —
   **no new lemma needed, only the already-certified IH and §13.2's closed forms.**
2. **Nontrivial case — `M_opt` strictly beats both `A_1` and `A_2`.** Then in particular
   `M_{\mathrm{opt}}<A_1`, so the Refined Delete-Recovery Conjecture's hypothesis holds, giving
   `M_{\mathrm{tag}}=M_{\mathrm{opt}}$ directly. Hence `\mathrm{TAGGED}_{+1}(B,Z,0)\le
   M_{\mathrm{tag}}=M_{\mathrm{opt}}=\mathrm{OPT}_{+1}(B,Z)$ (the min is attained at the match
   branch here), and again the trivial reverse direction gives equality. **Done — this is the one
   case needing genuinely new content, exactly the target the conjecture supplies.**

Only case 2 needs the Refined Delete-Recovery Conjecture, and only in the sub-case where it is
actually necessary (`M_opt$ strictly below *both* `A_1,A_2`); the conjecture's own hypothesis
(`M_opt<A_1$ alone, not needing `<A_2$ too) is strictly weaker/broader than what case 2 needs — it
is stated independent of `A_2` deliberately, because that is what stress-tests cleanly (see below)
and because a broader-domain statement, if true, automatically covers the narrower one actually
required (a "strictly harder target subsumes the necessary case" argument, not a shortcut being
taken silently).

**Computational status (this round; exact-integer, both random and exhaustive, `/tmp/round-11/
work/`).** `\sigma=+1$: `7000+$ random trials (`q\in\{4,\dots,8\}$, values up to `25`) plus fully
exhaustive sweeps (`q=4,v_{\max}=8`: `2640$ instances, `450$ with the trigger active; `q=5,
v_{\max}=6`: `1512$ instances, `159$ triggered; `q=6,v_{\max}=5`: `1050$ instances, `74$ triggered)
— **zero violations found in every regime**, combined `\sim10{,}000+$ trials. Every one of the
`56$ raw match-only mismatches found during testing satisfies `M_{\mathrm{opt}}\ge A_1$ (i.e. lies
outside the conjecture's own trigger), confirming these are not counterexamples to the conditioned
form, only to the already-known-false unconditioned one (§13.4/round 9's `3/500`-instance negative
result).

**Two cheap, not-yet-verified auxiliary observations flagged for a future round's cheap
verification pass (NOT proved, do not cite as established):**
- `\sigma=-1$ (max companion, needed for the KEEP branch's flipped recursion): the natural analogous
  trigger `M_opt > \max(A_1,A_2)$ had **`0$ trigger events in `4000$ random trials** — suggesting
  the MATCH branch may be entirely vacuous (never the maximizer) for the max companion. Only
  sampled, not exhaustive; no proof attempted.
- `|B|=0` (the top-level KEEP branch's own recursion, no external background at all): the same
  trigger had **`0$ trigger events in `3000$ random trials** — suggesting deleting `z_1$ is never
  beaten by matching when there is no background at all. Also directly reconfirmed plain
  `\mathrm{OPT}(Z)=\mathrm{NC}(Z)` (no background) on `1000$ fresh random trials, `0$ mismatches.

**Honest scope — this is a conjecture, NOT a proof.** (1) No proof mechanism has been attempted yet
— *why* `M_{\mathrm{opt}}<A_1\implies M_{\mathrm{tag}}=M_{\mathrm{opt}}$ (candidate tools: the
General Rank-Extraction Identity/Fact 3 directly, or a direct argument identifying which specific
`k$ recovers) is the concrete task for the next build. (2) Sizes tested remain small (`q\le8`
random, `q\le6$ exhaustive); the known `|B|=2$ counterexample to the old (dead) unrestricted
Match-Recovery Lemma only needed `q=4`, so this is not a vacuously-easy regime, but larger `q$ is
untested here (combinatorial cost of exhaustive enumeration grows roughly `(2q)!!`). (3) The
`\sigma=-1$/`|B|=0` "vacuous match branch" observations above are sampled only, not exhaustive —
worth a cheap dedicated exhaustive check before relying on them in a proof. (4) Since this
conjecture, if proved, closes the Full-Slack Insertion Lemma (as its `B=\emptyset$/`|B|=1$
degenerate-split corollary) AND the aggregated Small-Gap Crossing-Domination Lemma (as its
top-level, `B=\emptyset$ instance) in one shot via the 2-case induction above — exactly as the old
(now-dead) Match-Recovery Lemma was meant to — closing it closes the **entire** remaining
upper-bound gap, every `m`, every `n` (via the already-certified chain-prefix+tail rescoping, §9.4,
and Slack Collapse, §7.1). **This is not a partial-progress target if it lands; it is the whole
remaining gap, just correctly re-scoped to avoid the two now-dead proof shapes.**

**Recommended build order for the next round (per the charging explorer's own recommendation,
adopted here):**
1. A cheap dedicated adversarial-counterexample hunt BEFORE any proof attempt: push the exhaustive
   check to `q=7` if feasible, and specifically construct instances shaped like the old dead
   `|B|=2` counterexample (`B=\{2,4\},Z=(6,3,2,1)`) but with `|B|=1` background only, to actively
   try to break the conjecture before investing in a proof.
2. If it survives, attempt a proof via the General Rank-Extraction Identity/Fact 3 directly —
   the shape of the claim ("if match beats the simplest fallback, it's already achievable
   non-crossing too") is exactly suited to that identity's sign-bookkeeping.
3. Separately and cheaply: exhaustively (not just by sampling) check whether the `\sigma=-1` and
   `|B|=0$ "vacuous match branch" observations above hold with zero exceptions — if so, they
   simplify the induction further (fewer live cases) at low cost, independent of item 2.

#### 15.5 Queued, NOT built this round — a genuinely different *technique*: `aimo-0198`-style
averaging bound (honest reasoning for not dispatching it now)

The fresh-framing explorer surfaced crux `aimo-0198` (IMO 2012 P3, "Liar's guessing game"), whose
load-bearing move is bounding a greedy minimizer's outcome by the **average** of its available
options (`\min(A,B)\le(A+B)/2`) rather than case-splitting on which option is actually smaller —
closing an induction via a clean sum/telescoping identity on the average, without ever identifying
the arg-min. Applied here, this would mean bounding
`\mathrm{OPT}_{+1}(B,Z)=\min(A_1,A_2,\min_kA_{3,k})$ by a weighted average of `A_1,A_2$, and the
`A_{3,k}$'s, and showing the average alone already meets the target via a closed-form identity in
`Z`'s entries — a genuinely different proof *architecture* (probabilistic/averaging) from every
technique tried so far (exact-matching recovery, greedy policies, lookahead induction), aimed at
the *same* necessary fact (not a different top-level target, so this is a technique note inside
this approach, not grounds for a new slug).

**Why queued, not dispatched:** the explorer who found this ran out of round budget before running
even a single numerical test — there is no confirmed instance where any weighted average of the
branch values sits at or below the target via any identity, clean or otherwise. Dispatching a
proof-builder against an untested idea risks a wasted round; the correctly-scoped next step is a
**cheap verification pass** (not a full build): for the known hard instance
`Y=(39,36,30,28,22,18,14)` at `b=p-1=6`, compute `A_1,A_2$, and every `A_{3,k}$ exactly, and check
whether any simple weighted average of them already sits at or below the target via a clean
closed-form identity analogous to the crux's `\varphi_1+\varphi_2=\lambda\varphi+(n+1)`. If that
cheap check finds a promising identity, a future round should promote this to a full build target;
if not, it should be recorded as a dead end here (§15.5) rather than in a separate approach file,
since it never rose to a distinct whole-problem attempt.

### 16. Round 11 build — attempted proof of the Refined Delete-Recovery Conjecture (§15.4): NOT
completed; one new general lemma proved (Forced Swap Inequality), a strictly sharper conjecture
found and heavily stress-tested (Sharp Argmin Recovery), and three precise negative results pinning
down exactly why the natural proof mechanisms tried do not close it

**Headline, stated honestly up front (per CLAUDE.md — no forced proof): the Refined Delete-Recovery
Conjecture (§15.4) is NOT proved this round. It is also NOT refuted** — on the contrary, this
round's testing (below) is the most extensive and most adversarial run against it yet, including a
genuine counterexample search that succeeded, but only *outside* the conjecture's own stated scope
(§16.3.2), which if anything corroborates that the `|B|\le1` restriction in §15.4 is exactly load-
bearing, not cosmetic. All computation this round is exact-integer Python (`fractions` not even
needed — every quantity in this problem is an integer difference), brute-force over the finite
selection space (no heuristic pruning of the correctness-critical enumerations), archived at
`/tmp/round-11/work/` (`defs.py` plus 12 driver scripts, one per finding below; `defs.py` was
independently re-derived from the file's own §13.2 definitions, then sanity-checked against the
file's own claimed `|B|=2` counterexample value (`B=\{2,4\},Z=(6,3,2,1)`: got `OPT=0,TAGGED=1`,
matching exactly) before being trusted for anything new).

#### 16.1 A strictly sharper reformulation, found and heavily corroborated: the Sharp Argmin
Recovery (SAR) property

Restating §15.4's own notation exactly: for background `B` (`|B|\le1`), sorted `Z=(z_1\ge\dots\ge
z_q)`, `A_1:=\mathrm{OPT}_{+1}(B,Z\setminus\{z_1\})`, `A_{3,k}:=\mathrm{OPT}_{+1}(B\cup\{z_1-z_k\},
Z\setminus\{z_1,z_k\})`, `M_{\mathrm{opt}}:=\min_kA_{3,k}`, `B_{3,k}:=\mathrm{TAGGED}_{+1}
(B\cup\{z_1-z_k\},Z\setminus\{z_1,z_k\},k-1)`, `M_{\mathrm{tag}}:=\min_kB_{3,k}`. The Refined
Delete-Recovery Conjecture (RDRC) asserts: `M_{\mathrm{opt}}<A_1\implies M_{\mathrm{tag}}=
M_{\mathrm{opt}}` — an **existential** claim (some, not-necessarily-the-same, partner `k'`
recovers).

**New finding: in every triggered instance tested (see below), recovery happens at the SAME
argmin partner — no aggregation over a different `k'` is ever actually needed.** Precisely:

```
Sharp Argmin Recovery (SAR, conjectural — strictly implies RDRC if true).
Same setup as RDRC. Let k* be ANY index achieving A_{3,k*} = M_opt. If M_opt < A_1, THEN
  B_{3,k*} = A_{3,k*}  (= M_opt).
```

SAR trivially implies RDRC (take `k'=k^*` in RDRC's existential). It is a strictly stronger,
cleaner statement — worth recording as the sharper target because a proof of SAR (a single
distinguished partner, not an aggregate minimum over all `k`) is structurally simpler to attempt
than a proof of RDRC's raw existential form, and because it may generalize better.

**Computational support (this round, all exact-integer, `q` up to `7`, background
`|B|\in\{0,1\}` throughout, matching RDRC's own scope):**
- `explore.py`/`explore3.py`: `3000` and `8000` random trials respectively (`q=2,\dots,7`), giving
  `457` and `1135` triggered instances (`M_{\mathrm{opt}}<A_1$ strictly) — **`0` SAR violations in
  either run** (checked as: does *some* `k^*\in\arg\min_kA_{3,k}` satisfy `B_{3,k^*}=A_{3,k^*}`?).
- `check_all_optima.py`: a stronger, *witness-level* check (not just comparing the two scalar
  values but enumerating **every** optimal `(K,D,M)` selection achieving `A_{3,k^*}$ and asking
  whether *at least one* is already non-crossing-and-split-compatible) — `3000` random trials,
  `397` triggered, **`0`** instances where every optimal witness at the argmin was incompatible
  (i.e. a compatible witness always existed among the ties).
- **Targeted adversarial embedding, going beyond the outline-reviewer's own §1.2 embedding attack
  (which tested the weaker RDRC, not this sharper SAR).** Constructed `|B|=1` parent instances
  whose specific argmin branch's own `(B\cup\{z_1-z_{k^*}\},\,Z\setminus\{z_1,z_{k^*}\})` is
  *literally* one of `150` freshly-found bad `|B|=2` instances (`\mathrm{OPT}<\mathrm{TAGGED}(\cdot,
  0)$ at background size 2 — the already-certified-dead §13.6 phenomenon), scanning multiple
  insertion offsets and both role-assignments of which background element plays which role
  (`embed_search.py`, `embed_search2.py`): **`92`** parent instances actually triggered SAR's own
  hypothesis via exactly this embedded-bad-background mechanism (`9+83`) — **`0`** SAR violations.
  This is a strictly harder adversarial test than the outline-reviewer's own (which found `60`
  triggering embeddings for the weaker existential form); SAR survives the same attack at the
  sharper, single-partner level.
- `deeper_check.py`: checked one level of RECURSIVE consistency — inside the argmin branch
  `A_{3,k^*}`, decompose it via its *own* trichotomy (peeling its own largest element) and ask
  whether the resulting sub-decomposition's own winning branch is automatically compatible with
  the inherited split `k^*-1` — `338` triggered top-level instances, `424` argmin-branch checks
  (accounting for ties), **`0`** incompatible-winner cases (i.e. the recursive structure "stays
  compatible" one level further in, at least in every instance tested).

**Net: SAR passed every test this round, including the single most adversarial test built for it
(a purpose-built embedding of the already-known-dead `|B|=2` phenomenon into the exact structural
slot where it would need to "leak through" to break SAR) — but SAR is NOT proved. §16.2–§16.4
below record the attempted proof routes, one genuine new lemma that came out of the attempt, and
precisely where each route stalls.**

#### 16.2 A new, fully proved, general-purpose lemma: the Forced Swap Inequality

While attempting a direct exchange-argument proof of SAR, the following clean fact was isolated,
proved rigorously (not merely tested), and then independently re-verified computationally after an
initial harness bug was caught and fixed (see the honest note at the end of this subsection — the
bug was in the *test*, not the lemma, and is recorded so no future round repeats it).

**Setup.** Background `B` (**any** size — this lemma needs no restriction on `|B|`), sorted
`Z=(z_1\ge\dots\ge z_q)`. For `2\le l\le q` write `d_l:=z_1-z_l\ge0` and
`A_{3,l}:=\mathrm{OPT}_{+1}(B\cup\{d_l\},Z\setminus\{z_1,z_l\})`. Let `k^*` achieve
`M:=\min_lA_{3,l}`. Let `\eta^*` be **any** `(K,D,M)`-selection of `Z\setminus\{z_1,z_{k^*}\}$
achieving `A_{3,k^*}=M` (i.e. `e\big(B\cup\{d_{k^*}\}\cup\mathrm{vals}(\eta^*)\big)=M`). Suppose
`\eta^*$ contains a matched pair `(i,j)` with `2\le i<k^*<j\le q` (using original positions in
`Z$ — i.e. this pair "crosses" the pair `(1,k^*)$, since `1<i<k^*<j`). Let
`R:=\big(B\cup\mathrm{vals}(\eta^*)\big)\setminus\{d_{k^*},\,z_i-z_j\}` (the achieving multiset
with these two specific values removed — well-defined as a multiset operation).

**Forced Swap Inequality.**
```
e(R \cup \{z_1-z_i,\ z_{k^*}-z_j\}) \ge M,     and symmetrically     e(R \cup \{z_1-z_j,\ z_i-z_{k^*}\}) \ge M.
```
(Both differences on the left are of correctly-ordered, nonnegative quantities: `z_1\ge z_i` and
`z_{k^*}\ge z_j` for the first; `z_1\ge z_j` and `z_i\ge z_{k^*}` for the second — all forced by the
position ordering `1<i<k^*<j`.)

*Proof.* Consider the two non-crossing re-pairings of the four points `\{1,i,k^*,j\}` (the
classical fact that a crossing pair of arcs on 4 points has exactly two non-crossing alternatives —
disjoint `(1,i)\ \&\ (k^*,j)`, or nested `(1,j)\ \&\ (i,k^*)`). Take the first: define a selection
`\eta''` of `Z\setminus\{z_1,z_i\}` by copying `\eta^*`'s own `(K,D,M)` structure on
`Z\setminus\{z_1,z_{k^*},i,j\}` **verbatim** (a well-defined common index set, since `\eta^*` was a
selection of `Z\setminus\{z_1,z_{k^*}\}$ and removing its own `(i,j)` pair leaves exactly this
set), and additionally placing `(k^*,j)` as a matched pair. This `\eta''` is a **valid** selection
of `Z\setminus\{z_1,z_i\}$ (every remaining index used exactly once), so it is *some* (not
necessarily optimal) witness for `A_{3,i}`, giving `A_{3,i}\le e\big(B\cup\{z_1-z_i\}\cup
\mathrm{vals}(\eta'')\big)=e(R\cup\{z_1-z_i,z_{k^*}-z_j\})`. Since `k^*` is a **global** argmin over
*all* `l` (not merely a locally-chosen one), `M=A_{3,k^*}\le A_{3,i}`. Chaining:
`M\le A_{3,i}\le e(R\cup\{z_1-z_i,z_{k^*}-z_j\})`, proving the first inequality. The second is
identical, using the nested re-pairing `(1,j)\ \&\ (i,k^*)` and `A_{3,j}$ in place of `A_{3,i}`.
`\blacksquare`

**This is a genuinely new, general, promotable lemma** — it needs no restriction on `|B|`, no
triggering hypothesis (`M_{\mathrm{opt}}<A_1`), and is a real, if partial, structural fact about
why *any* single "obvious" local repair of a crossing (matching `z_1` to whichever element it
crosses) cannot beat the already-optimal value — a rigorous, quantitative version of "you can't
locally out-optimize the global optimum," specialized to this problem's exact swap operation via
the certified General Rank-Extraction Identity's own bookkeeping style (§13.1; the multiset
manipulation above is exactly the kind of exact value-tracking that identity is built for, though
this proof does not need to invoke it explicitly — a direct minimality argument suffices).

**Independent re-verification, with an honestly-recorded self-caught bug.** `verify_fsi_lemma.py`'s
first version found `124` apparent "violations" in `3000` random trials (arbitrary background size
`0`–`4`) — investigated by hand (traced one instance, `B=[10,0,5],Z=[8,2,0,0,0]`, fully by hand
arithmetic) and found the bug was in the **test harness**, not the lemma: the harness's `R` was
constructed as `B\cup\{d_{k^*}\}\cup(\text{rest of }\eta^*)`, i.e. it *retained* `d_{k^*}$ inside
`R` and then added the swap values *on top of* it, effectively testing `e(B\cup\{d_{k^*}\}\cup
\text{rest}\cup\{z_1-z_i,z_{k^*}-z_j\})$ (six values) instead of the correct `e(R\cup\{z_1-z_i,
z_{k^*}-z_j\})$ (four values, with `d_{k^*}$ **replaced**, not retained). Fixed in
`verify_fsi_lemma2.py` (`R:=B\cup(\text{rest of }\eta^*)$, `d_{k^*}$ excluded), which also adds a
sanity check (`e(R\cup\{d_{k^*},z_i-z_j\})=M$, confirming `R` is correctly constructed) before
testing the swap inequality itself: **`3336` crossing-pair checks (arbitrary background size
`0$–`4`, `q=3,\dots,7`), `0` violations.** The lemma is correct; the bug was a one-line test-harness
error, caught by hand-tracing the first "counterexample" rather than trusting the numeric mismatch
— recorded here as a methodological note per this repo's own convention of documenting self-caught
bugs (cf. round 4's own such note).

#### 16.3 Three negative results this round, precisely narrowing where a correct general argument
could live

**16.3.1 The averaging idea (in the spirit of §15.5's queued `aimo-0198` lead) does not resolve a
crossing via the Forced Swap Inequality's two alternatives.** A natural hope, given §16.2 proves
*both* uncrossing alternatives are `\ge M`: if their **average** were always `\le M`, at least one
would have to equal `M` exactly, giving a non-crossing witness for free. **Tested and refuted**
(`averaging_test.py`): across `81` actual crossing-pair instances found in `4000` random trials
(`q=3,\dots,7`), the average of the two alternatives **exceeds** `M` in **all `81`** cases — **`0`**
cases where averaging alone would have sufficed. **Round-11 reviewer correction:** the worked
example originally cited here (`B=[1],Z=(9,8,8,8,5,3,0)`) does not reproduce under independent
recomputation — the reviewer's own from-scratch harness finds the two argmin-branch crossing
alternatives at this instance are `\{0,2\}` (`M=0`), not `\{1,1\}` as previously stated (average is
still `1>0`, so the qualitative conclusion is unaffected, but the specific numbers were a
transcription slip, not a verified computation). The reviewer independently re-confirmed the
substantive claim itself (averaging does not recover `M`) via a properly-rescoped fresh test
restricted to the actual SAR argmin branch and `|B|\le1`: `0` non-trivial successes out of `5776`
argmin-branch crossing instances (see `lemmas/forced-swap-inequality.md`'s verification note for
detail). This is a distinct (narrower, swap-specific) idea from
§15.5's own original proposal (which averages the *three* branch values `A_1,A_2,A_{3,k}$ directly,
not the two uncrossing alternatives of one already-chosen crossing) — it does **not** by itself
settle §15.5's own broader averaging lead, which remains untested and separately queued — but it
does rule out the most obvious way one might try to use the (real, proved) Forced Swap Inequality
to close SAR: **the resolution of a crossing, when it happens, must come from a genuinely
different selection than either of the two "obvious" local re-pairings, not from a simple average
or best-of-two of them** (confirmed directly: in the `B=[1],Z=(9,8,8,8,5,3,0)$ instance above,
`check_all_optima.py` independently confirms *some* optimal, fully compatible selection exists
achieving `M=0` — just not one reachable by swapping the specific crossing pair found).

**16.3.2 The natural full generalization of SAR to arbitrary background size is FALSE — a genuine
counterexample, confirming `|B|\le1` is load-bearing, not a convenience.** `sar_general_bg.py`
tested SAR's exact statement with `B$'s size drawn from `\{0,1,2,3\}` (not restricted to `\le1`):
`1314` triggered instances, **`1313`** hold, **`1`** genuine violation:
```
B = (0,6,4)  [|B|=3],  Z = (10,8,5,4,3,1).
A_1 = 1.  A_{3,k} values (k ranging over Z\{10\}'s positions): {1,1,0,1,2} — M_opt = 0, at k*
corresponding to z_{k*}=4 (i.e. matching z_1=10 to z_{k*}=4, d=6).
A_{3,k*} = OPT_{+1}((0,6,4,6), (8,5,3,1)) = 0.
B_{3,k*} = TAGGED_{+1}((0,6,4,6), (8,5,3,1), split=2) = 1  \ne  0.
```
Trigger holds (`M_{\mathrm{opt}}=0<A_1=1`), yet the SAME-argmin recovery fails when `|B|=3`. This
is directly hand-verifiable and was cross-checked against the same `defs.py` used throughout (no
new code path). **This precisely confirms the RDRC/SAR framing's own `|B|\le1` restriction (§15.4)
is essential** — not a simplifying convenience that happens to make testing cheaper, but a real
structural boundary: SAR (and presumably RDRC) can genuinely fail once the background grows past
size `1`. This matters for the correct proof strategy: **any future inductive attempt must use an
invariant that is never asked to certify the argmin-recovery property at background size `\ge2` in
general** — only at the *specific*, structurally-constrained background-size-`2` instances that
arise **one level inside** an `|B|\le1` computation (i.e. `B\cup\{z_1-z_{k^*}\}$ for the *actual*
global argmin `k^*` of an `|B|\le1$ problem, not an arbitrary size-`2$ background chosen
independently) — confirming the diagnosis in §16.3.3 below.

**16.3.3 A "one-step compatible winner" generalization of the two-case induction skeleton (the
most natural way to try to close SAR by strong induction on `q`, tracking an arbitrary background
and an arbitrary external split) is FALSE — a genuine counterexample, showing *why* a naive
induction does not close.** Precise candidate statement tested (`gml_test.py`), call it the
"Grand Master Lemma" (GML): *for any background `C`, sorted `W`, split `s`, if the decomposition of
`\mathrm{OPT}_{+1}(C,W)$ via peeling `w_1:=\max(W)$ into (DELETE, KEEP, `\mathrm{MATCH}_l$ for all
`l$) has **some** branch achieving the global minimum that is "compatible" with `s`
(DELETE/KEEP always compatible; `\mathrm{MATCH}_l$ compatible iff `w_1,w_l` lie on the same side of
`s`), THEN `\mathrm{TAGGED}_{+1}(C,W,s)=\mathrm{OPT}_{+1}(C,W)`.* **Refuted**, `34/2959` violations
in a `3000`-trial random sweep (background size `0$–`3`, `q=2,\dots,6`), including violations at
`|C|\le1` (e.g. `C=[6],W=(8,7,7,4,1),s=3`: DELETE wins with value `0`, a "compatible" branch by the
GML's own criterion, yet `\mathrm{TAGGED}_{+1}(C,W,3)=1\ne0`). **Diagnosis:** GML's hypothesis only
checks compatibility of the winning branch **at the top level** — it is not strong enough, because
even when e.g. DELETE trivially "is compatible," the *recursive* residual instance
`(C,W\setminus\{w_1\})$ can itself fail to have a compatible winner at **its own** top level, and
nothing in GML's one-step hypothesis rules this out. **This precisely explains why a naive
induction-on-`q` proof of SAR does not simply "go through": the correct inductive invariant cannot
be "some top-level branch is locally compatible" — it must be strong enough to certify
compatibility *all the way down* the recursion, and (per §16.3.2) cannot be allowed to assert this
for arbitrary background/split/list triples — only for the specific, narrower family of triples
that actually arise from repeatedly peeling the argmin branch of an `|B|\le1$-seeded instance.**
Formalizing *that* narrower recursive invariant precisely (not merely observing computationally, as
`deeper_check.py` does one level deep, that it seems to hold) is the concrete unresolved task.

#### 16.4 Honest assessment — Status, what is proved, what remains open

- **Proved in full this round, general, promotable:** the **Forced Swap Inequality** (§16.2) — any
  single local re-pairing that reassigns `z_1`'s match partner to "fix" a crossing is provably no
  better than the global optimum already established; a real, if partial, structural fact, with no
  restriction on background size.
- **Not proved, but substantially strengthened and re-corroborated:** the Refined Delete-Recovery
  Conjecture itself, via the new, strictly sharper **Sharp Argmin Recovery** reformulation (§16.1),
  survived the single most adversarial test built for it this round (a purpose-built embedding of
  the already-certified-dead `|B|=2$ Match-Recovery failure mode into the exact structural slot
  where the new conjecture would need to confront it) — `0` violations in `\sim13{,}000+` combined
  fresh trials this round (on top of the `\sim20{,}000+$ already accumulated by the outline-reviewer
  and outliner in round 11 for the (weaker) RDRC form).
- **Three genuine negative results, new this round, that narrow — but do not yet close — the
  search for a correct general proof technique:** (1) averaging the two natural "uncrossing repair"
  alternatives does not recover the optimum (§16.3.1); (2) SAR's natural generalization to
  arbitrary background size is FALSE, with a concrete `|B|=3` counterexample (§16.3.2), confirming
  the `|B|\le1` restriction in §15.4 is load-bearing; (3) the natural "one-step compatible winner"
  strong-induction skeleton for SAR is FALSE in general (§16.3.3, concrete counterexample even at
  `|C|\le1`), precisely diagnosing *why*: the correct inductive invariant must certify
  split-compatibility recursively, all the way down, for the specific (not arbitrary) family of
  background/split/list triples that arise from repeatedly peeling an argmin branch — and no such
  invariant was successfully formalized and proved this round.
- **What this means for the theorem.** The Refined Delete-Recovery Conjecture (§15.4) — and hence
  the Match-Recovery Lemma, the Full-Slack Insertion Lemma, the aggregated Small-Gap
  Crossing-Domination Lemma, and ultimately `\mathrm{OPT}(Y,p-1)=\mathrm{NC}(Y,p-1)` and the whole
  upper-bound direction of the theorem — **remains open.** This round did **not** close it, and
  found **no** counterexample to it at its correctly-stated scope (`|B|\le1`). **Status for this
  approach, and for the theorem as a whole, correctly stays `partial` — the theorem is NOT solved
  this round.** The lower bound (round 8's milestone) is unaffected and remains fully,
  unconditionally proved for `D_m`, every `m` (§5.5 of `dyadic-cascade-induction`); nothing in this
  round's work touches that direction.
- **Concrete next steps for a future round (in priority order):** (a) attempt to directly
  formalize and prove the "recursive compatible-family" invariant identified in §16.3.3 — i.e.
  characterize precisely which `(C,W,s)$ triples arise from peeling an argmin branch of an
  `|B|\le1$-seeded instance (not arbitrary triples), and show SAR-type recovery holds
  *specifically* on that family by induction; (b) since the local-swap/averaging mechanisms are now
  conclusively ruled out (§16.2–§16.3.1), any future attempt should look for the actual recovering
  witness via a **global** construction (as `check_all_optima.py`'s brute-force confirms one always
  exists, just not one produced by a local repair) — e.g. a direct bijective/injective construction
  of a non-crossing witness from the problem's own combinatorial data, in the spirit of the still-
  untried `aimo-0558` charge-to-distinct-witness lead (§14's own note, not yet adapted to this
  exact target); (c) separately and cheaply, §15.4's own queued auxiliary checks (`\sigma=-1$,
  `|B|=0$ "vacuous match branch") remain untested at exhaustive scale — still worth a cheap pass if
  a future round has spare budget, independent of the main gap.

### 17. Round 12 outliner revision — reconciling two independently-found mechanisms into one build
target: the Match-Free Recovery Lemma

**Provenance.** Round 12 ran three explorers. `math-explorer-aimo0198-averaging.md` tested the
queued §15.5 averaging lead directly (both the raw sum-identity route and the existential
"average-over-all-partners" route) and killed it decisively: no state-independent sum identity
survives past a vacuous `q=3` boundary case, and the existential-averaging bound succeeds in only
`1.5–17.7%` of triggered instances at `q\ge3`, trending to `0\%` by `q=6,7$, and — even where it
would numerically work — is structurally incapable of ever proving SAR itself (only the weaker
existential RDRC), since averaging is blind to *which* index recovers. **Do not revisit averaging
as a route to SAR in any form; both variants (§16.3.1's swap-average and this round's
all-partners-average) are now dead for precisely diagnosed, distinct reasons.** The other two
explorers, working independently and without seeing each other's reports, both landed on a
strengthening of the same idea: `math-explorer-global-witness.md`'s **No-Second-Trigger** and
`math-explorer-recursive-invariant.md`'s **Delete-Suffices**. §17.1–§17.4 below reconcile these
into one precise statement; §17.5–§17.8 lay out the proof skeleton, gaps, build order, and
pre-build sanity sweep.

#### 17.1 The two formulations, restated in this file's own §13.2/§16.1 notation

Both explorers work with the level-1 residual instance produced by an `|B_0|\le1`-seeded,
`\sigma=+1$, triggered instance: background `B_0` (`|B_0|\le1`), sorted `Z_0=(z_1\ge\dots\ge z_q)`,
`A_1:=\mathrm{OPT}_{+1}(B_0,Z_0\setminus\{z_1\})`, `A_{3,l}:=\mathrm{OPT}_{+1}(B_0\cup\{z_1-z_l\},
Z_0\setminus\{z_1,z_l\})`, `M:=\min_lA_{3,l}$, trigger hypothesis `M<A_1`, `k^*` a global argmin.
Write `(B_1,Z_1):=(B_0\cup\{z_1-z_{k^*}\},\,Z_0\setminus\{z_1,z_{k^*}\})` (so `A_{3,k^*}=
\mathrm{OPT}_{+1}(B_1,Z_1)=M`, `|B_1|\le2`).

- **No-Second-Trigger** (global-witness explorer): writing `w_1:=\max(Z_1)`, the trichotomy on
  `(B_1,Z_1)`'s own top element never has its own MATCH branch *strictly* beat its own DELETE
  branch — `\mathrm{OPT}_{+1}(B_1,Z_1\setminus\{w_1\})\le\min_m\mathrm{OPT}_{+1}(B_1\cup\{w_1-w_m\},
  Z_1\setminus\{w_1,w_m\})`. Tested only **one level deep** relative to `(B_1,Z_1)`, with a
  separately-flagged caveat (§4 of that report): safety requires *also* canonically preferring
  DELETE/KEEP over MATCH on exact ties, else a forced tie-break produces a genuine violation one
  level further in (`depth3_probe.py`).
- **Delete-Suffices** (recursive-invariant explorer): defining
  `\mathrm{OPT\_KD}(C,W):=\min_{S\subseteq W}e(C\cup S)` (Keep/Delete only, **no** matching branch
  at any depth), the claim is `\mathrm{OPT\_KD}(B_1,Z_1)=M=\mathrm{OPT}_{+1}(B_1,Z_1)` — the
  **entire** downstream sub-problem needs no internal matching at all, at any depth, to reach its
  true optimum, not just at the very next peel.

**These are not literally the same statement as tested** — Delete-Suffices is, on its face, the
stronger, "closed" claim (a value identity for the whole sub-problem), while No-Second-Trigger (as
tested) is a one-step fact about the very first peel of `(B_1,Z_1)`. §17.2 shows they are in fact
*the same claim* once No-Second-Trigger is correctly generalized to hold recursively, at every
depth, with the tie-break rule folded in — exactly what the global-witness report's own §4 flags
as untested ("the *combination*, all the way to arbitrary depth, was only spot-checked one level
further").

#### 17.2 Reconciliation: precisely defining the scope family, and the unified claim

Neither report needs to reason about an arbitrary `(C,W,s)` triple (the exact thing round 11's
§16.3.3 diagnosis warned against) — both are implicitly scoped to instances reachable by
repeatedly peeling via DELETE/KEEP only, starting from a base trigger. Make this precise. Let
`\mathcal F` be the smallest family of triples `(C,W,\sigma)` (`\sigma\in\{+1,-1\}`, `C` a
background multiset, `W` a sorted list) such that:

1. **(Base generator.)** `(B_1,Z_1,+1)\in\mathcal F` for every `|B_0|\le1`, every sorted `Z_0`,
   every trigger event `M<A_1`, and every global argmin `k^*` (ties broken arbitrarily — the
   family includes one triple per witnessing `k^*`).
2. **(DELETE closure.)** If `(C,W,\sigma)\in\mathcal F` and `W\ne\emptyset`, writing
   `w_1:=\max(W)`, then `(C,\,W\setminus\{w_1\},\,\sigma)\in\mathcal F`.
3. **(KEEP closure.)** With the same `(C,W,\sigma)`, `w_1`: writing `h:=|\{c\in C:c>w_1\}|` and
   `C_{\mathrm{lo}}:=\{c\in C:c\le w_1\}` (the certified General Rank-Extraction Identity's own
   `h`/`C_{\mathrm{hi}}$/`C_{\mathrm{lo}}` bookkeeping, §13.1/§13.2), `(C_{\mathrm{lo}},\,
   W\setminus\{w_1\},\,\sigma\cdot(-1)^{h+1})\in\mathcal F`.
4. **Nothing else is in `\mathcal F`** — in particular, `\mathcal F` is generated *without* a MATCH
   closure rule. (Excluding MATCH from the generation rule is exactly the content that needs
   proving safe — see below.)

This is precisely "the family of instances arising from repeatedly peeling an `|B|\le1`-seeded
argmin branch" that the round-11 diagnosis (§16.3.3) asked for, now spelled out as a closure under
DELETE/KEEP only, with both signs `\sigma` tracked (the KEEP branch's sign flip is exactly why
`\sigma=-1` instances enter `\mathcal F`, matching §15.4's own untested `\sigma=-1` auxiliary
observation — see §17.6, Gap 3).

**Unified candidate — the Match-Free Recovery Lemma.**
```
For every (C,W,\sigma)\in\mathcal F,   OPT_\sigma(C,W) = OPT_KD_\sigma(C,W)
      (where OPT_KD_\sigma(C,W) := \sigma-optimal value of e(C\cup S) over all S\subseteq W).
```

**Why this is exactly the same claim as both explorers', reconciled.** Define, for
`(C,W,\sigma)\in\mathcal F` with `W\ne\emptyset`: `\mathrm{DEL}:=\mathrm{OPT}_\sigma(C,
W\setminus\{w_1\})`, `\mathrm{KEEP}:=$ the (sign-flipped, constant-shifted) value from item 3 above,
`\mathrm{MATCH}:=\sigma\text{-opt}_m\,\mathrm{OPT}_\sigma(C\cup\{w_1-w_m\},W\setminus\{w_1,w_m\})`.
The Generalized Multi-Background Peeling Lemma (§13.2, already certified) gives
`\mathrm{OPT}_\sigma(C,W)=\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP},\mathrm{MATCH})` exactly, and
`\mathrm{OPT\_KD}` (matching forbidden by definition) obeys the *identical* two-branch trichotomy
with no MATCH term (Gap 2 below: this needs a one-line proof that the DELETE/KEEP bijections of
§13.2, which never touch any matched pair, restrict correctly to the `M=\emptyset` sub-search — an
easy but currently *unwritten* fact). Given that, by strong induction on `|W|`:
- **Match-Free Recovery `\implies` "No-Second-Trigger holds at every depth of `\mathcal F`, with
  the canonical tie-break":** if `\mathrm{OPT}_\sigma(C,W)=\mathrm{OPT\_KD}_\sigma(C,W)` for a
  *given* `(C,W,\sigma)`, and by the IH `\mathrm{DEL}` and `\mathrm{KEEP}$'s underlying value
  already equal their own `\mathrm{OPT\_KD}` counterparts (both are strictly smaller instances,
  in `\mathcal F$ by closure rules 2–3), then `\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})=
  \mathrm{OPT\_KD}_\sigma(C,W)=\mathrm{OPT}_\sigma(C,W)=\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP},
  \mathrm{MATCH})`, which forces `\mathrm{MATCH}` not to strictly beat
  `\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})` — exactly "no second trigger," at this node.
- **Conversely, "no second trigger at every node of `\mathcal F`" `\implies` Match-Free Recovery:**
  by the same induction run the other way — if MATCH never strictly beats
  `\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})` and (by IH) `\mathrm{DEL},\mathrm{KEEP}` already
  equal their `\mathrm{OPT\_KD}` values, then `\mathrm{OPT}_\sigma(C,W)=\sigma\text{-opt}
  (\mathrm{DEL},\mathrm{KEEP})=\mathrm{OPT\_KD}_\sigma(C,W)`.

So the two candidates are **the same claim up to routine strong-induction bookkeeping**:
Delete-Suffices is the "closed" (all-depths-at-once) statement; No-Second-Trigger, *correctly
promoted from "depth 2 only" to "every node of `\mathcal F`"* (which is exactly what the
global-witness report's own §4 flags as the untested combination), is precisely the single
inductive step that proves it. Neither report tested the fully-promoted, all-depths version
directly — this is exactly Gap 1 below and the primary target for a future build.

#### 17.3 Why the two explorers' own negative controls both validate `\mathcal F`'s scope

Both reports independently ran the same two negative controls the round-11 diagnosis demanded, on
the base-generator level:
- Dropping "`k=k^*`" (arbitrary match partner, no global-argmin requirement): global-witness's
  `arbitrary_bg2_test.py` found `28$–`37\%` failure; recursive-invariant's `driver3.py` found `84\%`
  failure. **Argmin-ness is load-bearing**, confirming `\mathcal F`'s base generator must use the
  *true* global argmin, not an arbitrary partner.
- Dropping the trigger condition `M<A_1` entirely: recursive-invariant's `driver4.py` found
  `85.5\%` failure. **The trigger is independently load-bearing.**

Both controls target only the base generator (item 1 of `\mathcal F`'s definition); no report has
yet stress-tested whether items 2–3 (DELETE/KEEP closure) could be dropped or loosened — but since
those two closure rules are exactly the certified, unconditional Generalized Multi-Background
Peeling Lemma's own DELETE/KEEP branches (§13.2, not a new hypothesis), they need no independent
negative control: they are forced, not chosen.

#### 17.4 Why Match-Free Recovery trivially implies SAR (hence RDRC), in one step

Suppose Match-Free Recovery holds for the single base-generator triple `(B_1,Z_1,+1)` produced by
a given trigger and argmin `k^*` (this is the *only* instance of the lemma actually needed for
SAR's own conclusion — the induction of §17.2/§17.5 is needed only to *prove* this one instance,
not to state SAR's consequence). Then `\mathrm{OPT\_KD}_{+1}(B_1,Z_1)=\mathrm{OPT}_{+1}(B_1,Z_1)=
A_{3,k^*}=M`, so some subset `S^*\subseteq Z_1` achieves `e(B_1\cup S^*)=M` using **zero** matched
pairs. The selection `(K,D,M{=}\emptyset)=(S^*,\,Z_1\setminus S^*,\,\emptyset)` is vacuously
non-crossing (no pairs to cross) and vacuously compatible with *every* split, in particular
`s_1:=k^*-1`. Hence `B_{3,k^*}=\mathrm{TAGGED}_{+1}(B_1,Z_1,k^*-1)\le e(B_1\cup S^*)=M`. Combined
with the always-true `\mathrm{TAGGED}\ge\mathrm{OPT}$ (restriction of the search space, §13.2),
`B_{3,k^*}=A_{3,k^*}=M` — **exactly SAR.** No case analysis on crossing structure is needed at the
top level at all; the entire non-crossing/split-compatibility burden is discharged for free by the
witness having no arcs whatsoever. **This is precisely why this mechanism could succeed where the
"one-step compatible winner" (GML) skeleton failed (§16.3.3):** GML's hypothesis was that *some*
branch's winner is "compatible" with the split — a crossing/split notion that has to be re-checked
at every recursion depth and was shown to evaporate one level down. Match-Free Recovery's
hypothesis ("no matching needed at all") is a strictly stronger, but **arc-free**, invariant: it
never needs split-compatibility bookkeeping at any depth, because an all-K/D witness has nothing
that could ever conflict with any future split. The entire proof burden is pushed into a claim
about raw, **unrestricted** `\mathrm{OPT}$ values (Match-Free Recovery is stated with no
`\mathrm{TAGGED}`/split/crossing notion anywhere in it) — a structurally simpler statement to
attempt than any of §14/§15/§16.3.3's crossing-based formulations.

#### 17.5 Proof skeleton: strong induction on `q:=|Z_0|` (equivalently, on `|W|` within `\mathcal F`)

1. **Base cases.** `|W|=0,1` (and, cheaply, `2,3`): `\mathrm{OPT}_\sigma(C,W)=\mathrm{OPT\_KD}_
   \sigma(C,W)` should be directly checkable by hand/small case analysis (at `|W|\le1` there is no
   possible matched pair inside `W` at all, so the two quantities coincide trivially; `|W|=2,3`
   needs a short direct argument, not yet written).
2. **Inductive step.** Assume Match-Free Recovery for every `(C',W',\sigma')\in\mathcal F` with
   `|W'|<|W|`. For `(C,W,\sigma)\in\mathcal F`, `|W|=w`: by §17.2's equivalence argument, it
   suffices to prove the single inequality **Claim A** — `\mathrm{MATCH}` (as defined in §17.2)
   does not strictly beat `\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})` — since `\mathrm{DEL}`,
   `\mathrm{KEEP}` already reduce to their `\mathrm{OPT\_KD}` values by the IH (they are strictly
   smaller `\mathcal F`-members).

**Claim A is the entire remaining hard content of the induction — it is precisely the "No-Second-
Trigger" inequality, now required to hold at *every* node of `\mathcal F`, not just the first.**
Recommended tools (per the dispatch, and the closest certified material on file):
- The **General Rank-Extraction Identity** (§13.1, `lemmas/general-rank-extraction-identity.md`)
  is already exactly what closure rule 3 (KEEP) needs for its closed form — reusable directly, no
  new content required there.
- The **Forced Swap Inequality** (`lemmas/forced-swap-inequality.md`) is the closest certified tool
  that bounds a MATCH-branch-related value against the global argmin's own optimum — but **its
  applicability to Claim A is not yet established and should be checked, not assumed**: FSI bounds
  a *specific* 4-point local re-pairing of an already-crossing optimal witness relative to the
  *top-level* argmin `M`; Claim A is a raw (no crossing/split notion at all) comparison of `(C,W)`'s
  *own* MATCH branch against its *own* DELETE/KEEP branches, at a generic node of `\mathcal F`, not
  necessarily tied to any single witness's crossing structure. It is plausible an FSI-*shaped*
  argument (chaining through the global-argmin-of-`(C,W)`-itself) reproduces Claim A, but this has
  not been attempted and may require a genuinely new inequality, not merely an invocation of the
  existing certified lemma.

#### 17.6 Hard steps, named as explicit gaps

- **Gap 1 (the central open gap — Claim A / "No-Second-Trigger at every depth").** Prove: for
  every `(C,W,\sigma)\in\mathcal F$ with `W\ne\emptyset`, the MATCH branch of `(C,W)`'s own
  trichotomy does not strictly beat `\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})`. Corroborated
  computationally at depth 1–2 relative to the base generator (global-witness: `\sim12{,}000`
  evaluations, `0` violations; recursive-invariant: `900+1600+110+240=2850$ direct checks plus
  `800` depth-2 chains, `0` violations) but **not proved**, and **not yet tested at depth `\ge3`
  under the correct (non-forced) tie-break**, nor at scale for `\sigma=-1`.
- **Gap 2 (bookkeeping, believed easy but not yet written down).** Prove `\mathrm{OPT\_KD}_\sigma`
  obeys the identical DELETE/KEEP-only trichotomy (with the same Rank-Extraction closed form) as
  `\mathrm{OPT}_\sigma` restricted to `M=\emptyset` selections — needed for the induction's
  base-case-free bookkeeping in §17.2/§17.5. Should follow directly from the fact that the §13.2
  DELETE/KEEP bijections never introduce or remove a matched pair, but this restriction has not
  been spelled out as its own short lemma.
- **Gap 3 (the `\sigma=-1` sub-case, flagged but unverified in §15.4) — round-12 outline-reviewer
  correction: the hoped-for vacuity premise is FALSE, but Claim A itself still holds directly.**
  Closure rule 3 (KEEP) introduces `\sigma=-1` instances into `\mathcal F` whenever `h` is even.
  §15.4 flagged (sampled only, `4000` trials, `0` triggers) that the max-side trigger
  `M_{\mathrm{opt}}>\max(A_1,A_2)` may never fire at all, which would make Claim A *vacuously*
  true at every `\sigma=-1` node (MATCH never even a candidate winner). **The round-12
  outline-reviewer independently re-tested this premise directly (fresh code, not reusing any
  prior harness) and found it FALSE at scale**: in the exhaustive `q=7` (depth `\le5`,
  `\mathrm{vmax}=6`) and `q=8` (depth `\le4`, `\mathrm{vmax}=5`) sweeps, `52{,}155/107{,}787` and
  `34{,}020/34{,}020` of the `\sigma=-1$ nodes checked had a *nonempty* MATCH candidate — i.e. the
  MATCH branch is a live competitor at `\sigma=-1$ nodes far more often than "never." **However,
  Claim A's actual conclusion (MATCH never *strictly beats* `\sigma\text{-opt}(\mathrm{DEL},
  \mathrm{KEEP})`) was independently confirmed to hold anyway at every one of these `\sigma=-1`
  nodes — `0` violations, matching the `\sigma=+1` result exactly** (see the round-12
  outline-reviewer report, `/tmp/round-12/outline-reviewer.md`, §2 and §4, for the full battery:
  exhaustive `q=7,8` sweeps, random `q=9$–`11` sweeps, 21-path adversarial hill-climbing). **Net
  correction: do not attempt to prove Gap 3 via a vacuity argument in the next build round — it
  would be trying to prove a false premise.** Instead, treat `\sigma=+1` and `\sigma=-1` uniformly
  under the single Claim-A argument (Gap 1) — both signs need, and both empirically get, the
  identical treatment; there is no separate, easier "vacuous" special case to peel off first.
- **Gap 4 (scope-closure sanity, essentially free once Gaps 1–3 are proved, but worth confirming
  independently).** Because `\mathcal F`'s generation rule deliberately excludes a MATCH closure,
  every member of `\mathcal F` has `|C|\le|B_1|\le2` **by construction** — so a correct proof of
  Gaps 1–3 automatically stays inside the region where SAR is known to hold and never revisits the
  confirmed-FALSE `|B|=3` generalization (§16.3.2). This is not an independent gap so much as an
  observation that the induction is self-scoping — but a future build should state it as an
  explicit corollary (not merely an empirical observation) once Gap 1 is proved, since it is the
  precise reason this route cannot accidentally wander into refuted territory.

#### 17.7 Recommended build order

1. Attempt Gap 2 first (cheap, mechanical) — establishes the equivalence of §17.2 rigorously, not
   just as a plausibility argument, and pins down exactly what induction is being run.
2. Attempt Gap 3 next (cheap if it goes through) — if the `\sigma=-1` MATCH branch is provably
   vacuous, Claim A only needs proving for `\sigma=+1`, roughly halving the remaining casework.
3. Attack Gap 1 (the central content) by induction on `q`, first trying to adapt the Forced Swap
   Inequality's global-argmin-chaining technique to `(C,W)`'s *own* argmin (i.e., treat `(C,W)`
   itself as a fresh top-level instance and ask whether an FSI-style "any local repair is no better
   than the already-established optimum" argument, applied to `(C,W)`'s own MATCH branch against
   its own DELETE/KEEP branches, reproduces Claim A) — and if that does not go through directly,
   treat it as requiring a genuinely new lemma, not a re-citation.
4. Only after Gap 1 is proved for the general `(C,W,\sigma)\in\mathcal F$ node, assemble the full
   induction (§17.5) and then close SAR via the one-line §17.4 corollary.

#### 17.8 Recommended cheap pre-build sanity sweep (before committing a full build round)

Per the recursive-invariant explorer's own flagged next step (§6 of its report) and the
global-witness explorer's own §4 caveat, before investing a build round in Gap 1:
- **Exhaustive (not sampled) sweeps at `q=7,8`** of the full Match-Free Recovery claim — not just
  at the base generator `(B_1,Z_1,+1)` (already done at `q\le9$, sampled) but propagated through
  **several levels of DELETE/KEEP recursion**, i.e. check the claim continues to hold on `(C,W)`
  nodes 2–3 closure-steps deep inside `\mathcal F`, upgrading the "0/800 second-level-trigger"
  sampled finding (recursive-invariant, `driver5.py`) to exhaustive at these sizes.
- **Adversarial hill-climbing/simulated annealing**, mirroring the technique both this round's
  global-witness explorer and the round-11 reviewer already used for SAR itself, explicitly
  minimizing (`\sigma=+1`) or maximizing (`\sigma=-1`) `\mathrm{OPT\_KD}_\sigma(C,W)-
  \mathrm{OPT}_\sigma(C,W)` toward a violation, seeded at multiple depths within `\mathcal F` (not
  just the depth-2 probe global-witness already ran) — including, importantly, the **forced-tie**
  adversarial variant global-witness's `depth3_probe.py` already used to *find* a genuine
  violation, to confirm the canonical tie-break rule (never take MATCH on a tie) is exactly what
  is needed and sufficient at depth 3, not merely necessary.
- **A dedicated exhaustive check of the `\sigma=-1`/`|B|=0` "vacuous match branch" observations**
  flagged unverified in §15.4 — these are exactly Gap 3 above and are currently the least-tested
  piece of the whole skeleton (sampled only, `4000`/`3000` trials, never adversarially attacked).
- If any of these sweeps finds a violation, it should be classified immediately against the same
  two negative controls both explorers already ran (§17.3): is the violation at an arbitrary
  (non-argmin) partner, an untriggered instance, or a forced (non-canonical) tie-break — i.e.,
  outside `\mathcal F`'s own scope — before being treated as a genuine counterexample to Gap 1
  itself.

### 18. Round 12 build — Gap 2 closed in full; Gap 1 (Claim A) NOT closed, but reduced by two new
general lemmas, one new structural fact about the base generator, and a decisive negative result
on the FSI-adaptation route

**Headline, stated honestly up front (per CLAUDE.md): Gap 1 — the central Claim A / "No-Second-
Trigger at every depth" inequality — is NOT proved this round.** What follows is genuine, checked
progress: Gap 2 is fully closed; two new general-purpose lemmas are proved (not merely tested) that
together resolve Claim A unconditionally on a large, precisely-characterized portion of every
recursion path in `\mathcal F`; one new structural fact sharpens the base generator itself; a
precise criterion reduces Gap 1's remaining content to a single crisp existence question; and the
outline's own flagged, unresolved question ("does an FSI-shaped argument reproduce Claim A?") is
answered **decisively, in the negative**, with the exact mechanism explained. All computation this
round is exact-integer Python (`fractions.Fraction`), brute-force over the finite selection space —
archived at `/tmp/round-12/work/` (`defs.py`, `gen_F.py`, plus one driver script per finding below).
`defs.py`'s `OPT`/`OPT_KD` were sanity-checked by direct hand-computation on two small cases before
being trusted (§18.1 first two lemmas below were verified against their own by-hand derivations, not
just against each other).

#### 18.1 Gap 2 — closed in full

**Claim.** `\mathrm{OPT\_KD}_\sigma(C,W) := \sigma\text{-opt}_{S\subseteq W}\,e(C\cup S)` obeys the
*identical* two-branch (DELETE/KEEP-only, no MATCH) trichotomy as `\mathrm{OPT}_\sigma(C,W)`'s own
DELETE/KEEP branches, with the identical closed KEEP formula from the General Rank-Extraction
Identity (`lemmas/general-rank-extraction-identity.md`).

**Proof.** Every `S\subseteq W` either contains `w_1:=\max(W)` or does not — exhaustive, mutually
exclusive (this is simply the definition of subset membership, nothing more is needed for
exhaustiveness; contrast with `\mathrm{OPT}_\sigma`'s three-way trichotomy, which needs the
Generalized Multi-Background Peeling Lemma's bijection argument because a *matched* pair is not a
subset-membership fact — here there is no matching option at all, so the case split is free).
- **`w_1\notin S`:** write `S=S'`, `S'\subseteq W\setminus\{w_1\}`. Branch value
  `=\sigma\text{-opt}_{S'\subseteq W\setminus\{w_1\}}\,e(C\cup S') = \mathrm{OPT\_KD}_\sigma(C,
  W\setminus\{w_1\})=:\mathrm{DEL\_KD}`.
- **`w_1\in S`:** write `S=\{w_1\}\cup S'`, `S'\subseteq W\setminus\{w_1\}` (every element of `S'`
  is `\le w_1$, exactly as in §13.2's own KEEP case). Apply the **General Rank-Extraction Identity**
  exactly as §13.2 does, with `x:=w_1` at rank `r=h+1` in `F:=C\cup\{w_1\}\cup S'`
  (`h:=|\{c\in C:c>w_1\}|`, `C_{\mathrm{hi}},C_{\mathrm{lo}}` as in §13.2):
  ```
  e(C\cup\{w_1\}\cup S') = e(C_{\mathrm{hi}}) + (-1)^h w_1 + (-1)^{h+1} e(C_{\mathrm{lo}}\cup S').
  ```
  Taking `\sigma`-opt over `S'\subseteq W\setminus\{w_1\}` on both sides (the left side ranges over
  exactly this as `S'$ varies, since `C,w_1,h` are fixed, independent of `S'`):
  ```
  \mathrm{KEEP\_KD} = e(C_{\mathrm{hi}}) + (-1)^h w_1 + (-1)^{h+1}\cdot
       \mathrm{OPT\_KD}_{\sigma\cdot(-1)^{h+1}}(C_{\mathrm{lo}}, W\setminus\{w_1\}),
  ```
  **identical in form** to §13.2's own `\mathrm{KEEP}` formula, with `\mathrm{OPT}` replaced by
  `\mathrm{OPT\_KD}` in the recursive inner term (and nowhere else — the constant offset
  `e(C_{\mathrm{hi}})+(-1)^hw_1` is untouched, since it never depended on the choice of `S'` in
  either derivation).
- `\mathrm{OPT\_KD}_\sigma(C,W) = \sigma\text{-opt}(\mathrm{DEL\_KD},\mathrm{KEEP\_KD})` follows
  immediately from the two-way exhaustive split. `\blacksquare`

**Consequence for the induction (§17.2/§17.5), spelled out.** At a node `(C,W,\sigma)\in\mathcal F`
with `|W|=w`, IH gives `\mathrm{OPT}_\sigma(C,W\setminus\{w_1\}) = \mathrm{OPT\_KD}_\sigma(C,
W\setminus\{w_1\})` (i.e. `\mathrm{DEL}=\mathrm{DEL\_KD}`, both instances being strictly-smaller
members of `\mathcal F$ by closure rules 2–3) and `\mathrm{OPT}_{\sigma(-1)^{h+1}}(C_{\mathrm{lo}},
W\setminus\{w_1\}) = \mathrm{OPT\_KD}_{\sigma(-1)^{h+1}}(C_{\mathrm{lo}}, W\setminus\{w_1\})` (i.e.
`\mathrm{KEEP}=\mathrm{KEEP\_KD}`, same reason). Substituting into this subsection's formula,
`\mathrm{OPT\_KD}_\sigma(C,W) = \sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})` exactly — so Claim A
(`\mathrm{MATCH}` does not strictly beat `\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})`), *once
proved*, gives `\mathrm{OPT}_\sigma(C,W)=\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP},\mathrm{MATCH})
=\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})=\mathrm{OPT\_KD}_\sigma(C,W)`, closing the inductive
step exactly as §17.2 described, now with Gap 2's own formula proved rather than merely asserted.
No independent computational check was needed beyond the identity's own derivation (it is a direct
corollary of the already-certified Rank-Extraction Identity, same proof method, verbatim), but as a
sanity cross-check `verify_gap2.py` confirmed `\mathrm{OPT\_KD}_\sigma(C,W)=\sigma\text{-opt}(
\mathrm{DEL\_KD},\mathrm{KEEP\_KD})` (computed via this subsection's closed forms, implemented as an
independent recursion) against a direct brute-force `\mathrm{OPT\_KD}` (enumerating all `2^{|W|}`
subsets) — `2000` random trials `\times` both signs `=4000` checks, `0` mismatches.

#### 18.2 Two new, fully proved, general-purpose lemmas

**Lemma (Empty-Background).** For **any** sorted `W` (any size) and `\sigma\in\{+1,-1\}`,
`\mathrm{OPT}_\sigma(\emptyset,W) = \mathrm{OPT\_KD}_\sigma(\emptyset,W)` — explicitly,
`\mathrm{OPT}_{+1}(\emptyset,W)=0` and `\mathrm{OPT}_{-1}(\emptyset,W)=\max(W)` (or `0` if
`W=\emptyset`).

*Proof.* `\sigma=+1`: deleting every element of `W` (`D=W`) gives `e(\emptyset)=0`, so
`\mathrm{OPT}_{+1}(\emptyset,W)\le0`; by the already-certified **Fact 1**
(`lemmas/dominant-extraction.md`, `e(M)\ge0` for any nonnegative multiset `M`), every selection's
value is `\ge0`, so `\mathrm{OPT}_{+1}(\emptyset,W)=0` exactly, achieved with **zero** matched pairs
— hence also `=\mathrm{OPT\_KD}_{+1}(\emptyset,W)$ (the same construction, `S=\emptyset`, is
available to `\mathrm{OPT\_KD}` too, and `\mathrm{OPT\_KD}\ge\mathrm{OPT}` always since it searches a
strictly smaller space). `\sigma=-1$ (`W\ne\emptyset`): keeping only `w_1:=\max(W)` (`K=\{w_1\}`,
`D=`rest) gives `e(\{w_1\})=w_1`, so `\mathrm{OPT}_{-1}(\emptyset,W)\ge w_1`; by the already-certified
**Fact 2** (same file, `e(M)\le\max(M)` for any nonnegative multiset `M`), *every* selection's
resulting multiset has all elements `\le w_1$ (kept values are literal elements of `W`, hence
`\le w_1`; a matched difference `w_i-w_j\le w_i\le w_1`), so every selection's value is `\le w_1`,
giving `\mathrm{OPT}_{-1}(\emptyset,W)\le w_1`. Hence `=w_1$ exactly, again achieved with zero
matched pairs, so `=\mathrm{OPT\_KD}_{-1}(\emptyset,W)$ too. `\blacksquare`

Independently re-verified computationally: `3000` random trials (`q=0,\dots,6`), `0` mismatches
(`verify_writeup_claims.py`, second block).

**Lemma (Background-Splitting).** For **any** background `C`, sorted `W`, `\sigma\in\{+1,-1\}`,
write `w_{\max}:=\max(W)` (or treat `C_{\mathrm{hi}}:=C`, `C_{\mathrm{lo}}:=\emptyset$ if
`W=\emptyset`), `C_{\mathrm{hi}}:=\{c\in C: c\ge w_{\max}\}`, `C_{\mathrm{lo}}:=C\setminus
C_{\mathrm{hi}}`, `h:=|C_{\mathrm{hi}}|`. Then
```
\mathrm{OPT}_\sigma(C,W) = e(C_{\mathrm{hi}}) + (-1)^h\cdot\mathrm{OPT}_{\sigma\cdot(-1)^h}
    (C_{\mathrm{lo}}, W),
```
and **identically** with `\mathrm{OPT}` replaced by `\mathrm{OPT\_KD}` throughout (same proof,
verbatim, restricting the "Rest" range to `K/D`-only selections).

*Proof.* Every value contributed to the final multiset by *any* selection of `W` — a kept value
(literally an element of `W`, hence `\le w_{\max}`) or a matched difference `w_i-w_j` (`\le w_i\le
w_{\max}`, since `i<j$ in sorted order forces `w_i\ge w_j\ge0`) — is `\le w_{\max}\le` every element
of `C_{\mathrm{hi}}` (by construction of `C_{\mathrm{hi}}`). So, for **every** selection with
resulting "Rest" multiset `R\subseteq` (kept values `\cup` matched differences), `C_{\mathrm{hi}}$
dominates `C_{\mathrm{lo}}\cup R` entirely, and the already-certified **Fact 3** (block extraction,
`lemmas/insertion-and-cascade-facts.md`) gives, for this *specific* selection,
`e(C\cup R) = e(C_{\mathrm{hi}}\cup C_{\mathrm{lo}}\cup R) = e(C_{\mathrm{hi}}) + (-1)^h
e(C_{\mathrm{lo}}\cup R)`. This holds selection-by-selection (the split point `|C_{\mathrm{hi}}|=h`
is the *same* for every selection, since `C_{\mathrm{hi}}` depends only on `C` and `w_{\max}`, not on
the selection itself — this is the key difference from the General Rank-Extraction Identity's own
per-selection rank bookkeeping, and why no recursion on `W` is needed here at all). Taking
`\sigma`-opt over all selections of `W$ on both sides (the constant `e(C_{\mathrm{hi}})+(-1)^h\cdot(
\text{nothing else depends on the selection})` factors out exactly as in §13.2's KEEP-branch
derivation) gives the claimed identity. Restricting the selection range to `K/D`-only (dropping
matched pairs) proves the `\mathrm{OPT\_KD}` version identically. `\blacksquare`

Independently re-verified computationally: `5000` random trials (`|C|=0,\dots,4`, `q=0,\dots,5`,
both signs), comparing the formula's right-hand side (computed from `C_{\mathrm{hi}}/C_{\mathrm{lo}}`
and a fresh call to `OPT`) against a direct call to `OPT(\sigma,C,W)$ — **`0` mismatches**
(`verify_writeup_claims.py`, first block).

**Corollary (reduction of Claim A).** Since `e(C_{\mathrm{hi}})+(-1)^h(\cdot)` is a fixed
order-preserving-or-reversing affine transform (multiply by `(-1)^h`, add a constant) applied
*identically* to `\mathrm{OPT}_{\sigma(-1)^h}(C_{\mathrm{lo}},W)` and to
`\mathrm{OPT\_KD}_{\sigma(-1)^h}(C_{\mathrm{lo}},W)`, and it commutes with `\sigma`-opt over the
DELETE/KEEP/MATCH trichotomy (an affine transform of the objective doesn't change which selection is
optimal, only relabels the optimal *value*), **Claim A holds at `(C,W,\sigma)` if and only if it
holds at `(C_{\mathrm{lo}},W,\sigma\cdot(-1)^h)`.** Since every member of `\mathcal F` has
`|C|\le2` (Gap 4), this reduces Claim A's remaining content, at every node, to the case
`|C_{\mathrm{lo}}|\in\{0,1,2\}` — and `|C_{\mathrm{lo}}|=0` (both, or the sole, element of `C`
dominates `\max(W)`) is **already fully closed** by the Empty-Background Lemma above (giving
`\mathrm{OPT}_{\sigma(-1)^h}(\emptyset,W)=\mathrm{OPT\_KD}_{\sigma(-1)^h}(\emptyset,W)`
unconditionally). **A genuine structural consequence, not just a special case:** because DELETE/KEEP
closure only ever *shrinks* `C` (closure rule 3, §17.2, replaces `C` by `C_{\mathrm{lo}}$, never
adds to it) while `\max(W)` is non-increasing along any DELETE/KEEP path (each step removes the
current maximum), `C_{\mathrm{hi}}` grows weakly monotonically and `\mathrm{OPT\_KD}(C_{\mathrm{lo}})`
above is a strictly easier target as depth increases — so **every DELETE/KEEP path in `\mathcal F`
eventually reaches, and permanently remains in, the fully-resolved `C_{\mathrm{lo}}=\emptyset` regime
after finitely many steps.** Confirmed concretely (`verify_writeup_claims.py`, third block): across
`447` genuine base generators (`q=3,\dots,8`), the simple all-DELETE path reaches
`C_{\mathrm{lo}}=\emptyset` within `\le4` steps in every case checked. **Net effect: Claim A is now
unconditionally, rigorously proved for a genuine, finite-codimension *tail* of every recursion path
in `\mathcal F`** (not merely numerically supported there) — the open content is confined to the
*prefix* of each path, before domination sets in, where `|C_{\mathrm{lo}}|\in\{1,2\}` and
`C_{\mathrm{lo}}` does **not** dominate `\max(W)`.

#### 18.3 A new structural fact about the base generator: `B_0=\emptyset` never triggers

**Fact.** In `\mathcal F`'s base-generator condition (§17.2, item 1: trigger `M<A_1`), `B_0` must
have size **exactly** `1` — `B_0=\emptyset` can never satisfy the trigger.

*Proof.* If `B_0=\emptyset`, then `A_1:=\mathrm{OPT}_{+1}(B_0,Z_0\setminus\{z_1\}) =
\mathrm{OPT}_{+1}(\emptyset, Z_0\setminus\{z_1\}) = 0` by the Empty-Background Lemma (§18.2). But
`M:=\min_lA_{3,l}` where each `A_{3,l}=\mathrm{OPT}_{+1}(B_0\cup\{d_l\}, \cdot)=\mathrm{OPT}_{+1}
(\{d_l\},\cdot)\ge0` by the already-certified Fact 1 (any selection's resulting multiset is
nonnegative, since `d_l=z_1-z_l\ge0` and all of `Z_0`'s entries are nonnegative). So `M\ge0=A_1`,
making the strict trigger `M<A_1` impossible. `\blacksquare`

Independently re-confirmed computationally: across `617` genuine triggered instances found in a
fresh `5000`-seed sweep (`gen_F.py`'s own generator, `q=2,\dots,7`), **`0`** had `B_0=\emptyset`
(`check_b0_empty.py`). This sharpens `\mathcal F`'s own base-generator definition (§17.2, item 1)
from "`|B_0|\le1`" to "`|B_0|=1` exactly" with no loss of generality — a small but genuine
correction to file, since it means the base generator's own `C=B_1` always starts at **exactly**
size `2` (`B_0`'s singleton plus `d_{k^*}`), only ever shrinking via the Background-Splitting
reduction or later KEEP-closure — never starting at size `0` or `1`.

#### 18.4 A clean necessary-and-sufficient criterion for Claim A, and why the Forced Swap
Inequality does not directly close it

**Criterion (Non-Matching-Witness).** For any `(C,W,\sigma)` with `W\ne\emptyset`, writing
`w_1:=\max(W)`, `V:=\mathrm{OPT}_\sigma(C,W)`: **Claim A holds at `(C,W,\sigma)` if and only if some
optimal witness achieving `V` does not match `w_1`.**

*Proof.* (`\Leftarrow`) If some optimal witness `\eta` achieves `V` without matching `w_1`, then
either `w_1\in D(\eta)` or `w_1\in K(\eta)$ in `\eta`. If `w_1\in D(\eta)`: `\eta$ restricted to
`W\setminus\{w_1\}` is a valid selection of `W\setminus\{w_1\}` with the same value (`w_1$
contributes `0` to `D`), so `\mathrm{DEL}\le V`; combined with `\mathrm{DEL}\ge V` (the Generalized
Multi-Background Peeling Lemma, §13.2, already certified, gives `V=\sigma\text{-opt}(\mathrm{DEL},
\mathrm{KEEP},\mathrm{MATCH})`, so every individual branch value is `\sigma`-*at least as extreme
as* `V`, i.e. `\mathrm{DEL}\ge V$ for `\sigma=+1`, `\le V$ for `\sigma=-1` — here stating the
`\sigma=+1` direction; `\sigma=-1$ is identical with inequalities reversed throughout), get
`\mathrm{DEL}=V` exactly. Then `\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})` is at least as
extreme as `\mathrm{DEL}=V`, and (again by the same trivial branch-value bound) at most as extreme
as `V`, so `\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})=V=\mathrm{OPT}_\sigma(C,W)`, i.e.
`\mathrm{MATCH}` cannot strictly beat it — Claim A. The `w_1\in K(\eta)$ case is identical with
`\mathrm{KEEP}` in place of `\mathrm{DEL}`. (`\Rightarrow`) If Claim A holds,
`\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})=V` exactly (combining Claim A with the trivial
direction `\sigma\text{-opt}(\mathrm{DEL},\mathrm{KEEP})` is never `\sigma`-better than `V`). Whichever
of `\mathrm{DEL},\mathrm{KEEP}` achieves this value has its own optimal witness (a selection of
`W\setminus\{w_1\}`, resp. of the KEEP sub-formula), which extends to a full selection of `W` (delete
`w_1`, resp. keep `w_1`) achieving `V` without matching `w_1`. `\blacksquare`

**So Gap 1's entire remaining content is exactly this: prove that for every `(C,W,\sigma)\in
\mathcal F` with `C_{\mathrm{lo}}\ne\emptyset` (i.e. genuinely outside the already-closed regime of
§18.2), `\mathrm{OPT}_\sigma(C,W)` admits a non-`w_1`-matching optimal witness.**

**Why the Forced Swap Inequality does not directly give this (a decisive negative finding,
resolving the question §17.5 explicitly left open) — precise numbers, corrected after actually
running the check (an earlier draft of this paragraph guessed at figures before the harness was
written; those guessed numbers are replaced below with the real, verified ones).** The natural
attempted adaptation: take `\eta^*` an optimal witness of `V=\mathrm{OPT}_\sigma(C,W)` (at depth
`0`, `V=A_{3,k^*}=M`, and `\eta^*` is exactly the witness the Forced Swap Inequality's own
hypothesis refers to). If `\eta^*` matches `w_1` to some `w_m`, is `(w_1,w_m)` a crossing pair
relative to `(1,k^*)` in the *original* `Z_0` indexing, and if so, does FSI's swap-repair inequality
help certify `\mathrm{DEL}=V` or `\mathrm{KEEP}=V`? **Traced through explicitly and tested
computationally (`fsi_adapt_check.py`, `417` genuine `|B_0|=1` base-generator instances, `q=4,
\dots,7`): `829` optimal witnesses were found matching `w_1`, of which `116` had their matched
partner crossing `(1,k^*)` (FSI's hypothesis applicable). Of those `116`, the FSI swap value
*coincidentally equalled* `\mathrm{DEL}` or `\mathrm{KEEP}` in `28` cases** — so FSI's bound is not
*never* numerically consistent with the target, but a **separate, decisive check
(`check_nonmatching_exists.py`) shows this coincidence is never load-bearing**: across the *same*
`417` instances, a non-`w_1`-matching optimal witness (§18.4's criterion) was found to **already
independently exist in all `417/417` cases** — i.e. **zero "forced-matching" instances occurred at
all**, so Claim A was already settled by the criterion alone, with or without FSI, in every case
checked. **FSI's occasional numerical coincidence is exactly that — a coincidence, never observed
to occur in a case where it was actually needed** (no forced-matching case has ever been produced,
by this or the outline-reviewer's much larger sweep, to test whether FSI could rescue one).
Structurally, this is expected: FSI's two inequalities bound the value of a *different* top-level
pairing (`(1,w_1)`-and-`(k^*,w_m)`, or `(1,w_m)`-and-`(w_1,k^*)`) against `M` — i.e. they relate the
*current* winning match-partner `k^*` to *other* top-level match-partners' own values
(`A_{3,i}`-type quantities, at the *same* recursion level as `k^*` itself), not to `(C,W)`'s own
DELETE/KEEP branches, which are not indexed by a match partner at all. **Net: this answers the
question §17.5 flagged as unattempted — FSI is not the right tool for Gap 1** (its rare numerical
agreement with DEL/KEEP is coincidental, not load-bearing, in every instance where it was checked);
a genuinely new inequality, relating a node's own MATCH branch directly to its own DELETE/KEEP
branches (not to sibling match branches), is needed. **A further, honestly-flagged observation:**
since forced-matching was never observed to occur at all (`0/417` this round, `0` across every
sweep on file), Gap 1's residual open content may be *easier* than the worst case the induction
skeleton demands — it is conceivable (not proved) that a direct existence argument for the
non-matching witness (not needing FSI, not needing case analysis on crossing structure at all) is
the right route; this is flagged as the concrete lead for the next round, not claimed as a proof.

#### 18.5 Sharpened negative results: size-boundedness of `C` is necessary but far from sufficient,
at every scale, not just at `|C|\ge3`

Round 11 established SAR fails at `|C|=3` (§16.3.2), which had been read as "the load-bearing scope
boundary is `|C|\le2`, i.e. Gap 4's bound." **This round's fresh computation shows this reading
significantly understates how essential the genuine trigger/argmin *provenance* is — arbitrary
(non-`\mathcal F`) backgrounds break Claim A/Match-Free Recovery already at `|C|=1`, and already at
the smallest possible list sizes:**
- **Arbitrary `|C|\le2`, arbitrary `W`** (`test_size2_mfr.py`): `4416/40000` trials violate Claim
  A/MFR (`q_C\le2`, `q_W\le6`, integer entries `0`–`12`) — e.g. `C=[5,8],W=(10,8,7,2),\sigma=+1`:
  true `\mathrm{OPT}=0` vs. `\mathrm{OPT\_KD}=2` (achieved only via `D=\{10\}, K=\{8\}, M=\{(7,2)\}`,
  i.e. genuinely needs an internal match one level into the DELETE/KEEP recursion — traced by hand,
  `investigate.py`).
- **Arbitrary `|C|=1`, arbitrary `W`** (`test_size1.py`): `6523/40000` trials violate, e.g.
  `c=1,W=(10,8,7),\sigma=+1`: `\mathrm{OPT}=0` vs `\mathrm{OPT\_KD}=1`.
- **Arbitrary `|C|\le2` (incl. `1`), restricted to the smallest nontrivial list sizes**
  (`test_small_W.py`): `|W|=2$: `2608/40000` violate; `|W|=3`: `6386/40000` violate — **correcting
  the outline's own §17.5 implicit expectation that `|W|=2,3` would be an easy, "short" base case**:
  the difficulty is driven entirely by provenance (genuine trigger+argmin ancestry), not by the size
  of `W` or `C` individually; small instances are exactly as capable of violating Claim A as large
  ones, once the background is not derived from a genuine trigger.
- **By contrast, restricting to a *dominant* background** (every element of `C`, of size `1` or `2`,
  `\ge\max(W)`) — **`0/40000`** violations in both cases (`test_dominant.py`), consistent with, and
  now fully *explained* (not just observed) by, the Background-Splitting/Empty-Background Lemmas of
  §18.2.

**Net:** genuine `\mathcal F`-membership (trigger + global-argmin ancestry, propagated only through
DELETE/KEEP closure) is now confirmed, precisely, to be doing essentially *all* of the work at every
background size and every list size — size-boundedness alone (Gap 4) explains none of why Claim A
holds on `\mathcal F`; only the Background-Splitting reduction's *dominance* mechanism (§18.2, a
completely general, provenance-independent fact) and the (still-unproved) provenance-dependent
content identified by §18.4's criterion do.

#### 18.6 Honest assessment — status of Gap 1 after this round

**Proved in full this round (general-purpose, reusable, independent of any conjecture):**
- Gap 2 (§18.1) — `\mathrm{OPT\_KD}_\sigma`'s own DELETE/KEEP trichotomy, closing exactly the
  bookkeeping item the induction (§17.2/§17.5) needed.
- The **Empty-Background Lemma** and **Background-Splitting Lemma** (§18.2) — together these
  unconditionally close Claim A on the "eventually dominant" tail of *every* DELETE/KEEP path in
  `\mathcal F` (confirmed to be reached within a handful of steps in every case sampled), reducing
  the open content to a genuinely small, precisely-bounded prefix of the recursion.
- The `B_0=\emptyset`**-never-triggers** fact (§18.3), sharpening `\mathcal F`'s own definition.
- The **Non-Matching-Witness Criterion** (§18.4) — an exact, general iff-reformulation of Claim A,
  reducing it to a single crisp existence question.

**Decisively ruled out this round (negative, not merely "not yet tried"):**
- The Forced Swap Inequality does **not** directly close Gap 1 — traced through explicitly (§18.4)
  and shown to bound the wrong pair of quantities (sibling match branches, not a node's own
  DELETE/KEEP branches). Answers §17.5's explicitly-flagged open question, negatively.
- Size-boundedness of the background (Gap 4's `|C|\le2`) is **not**, by itself, doing any of the
  real work (§18.5) — sharpening (not merely repeating) round 11's `|C|=3` counterexample.

**One more data point, honestly reported as corroboration only (not a proof technique):** across
every genuine base-generator instance checked this round for the "forced-matching" failure mode
(`check_nonmatching_exists.py`, `417` instances), **it never once occurred** — a non-`w_1`-matching
optimal witness was found to already exist in `417/417` cases. This is consistent with, and adds to,
the existing `\sim200{,}000+` zero-violation record, but it is a *different* kind of check (existence
of a specific witness type, not just a value comparison) and so is recorded as independent
corroboration, not a re-statement of previously-run tests.

**Still genuinely open — Gap 1's exact residual content, precisely stated:** for `(C,W,\sigma)\in
\mathcal F` with `C_{\mathrm{lo}}\ne\emptyset$ (background not yet dominated — the only regime
`\S`18.2 does not already resolve), prove `\mathrm{OPT}_\sigma(C,W)` always has an optimal witness
that does not match `\max(W)$ (§18.4's criterion). This is corroborated by every computational test
run so far, this round and prior (this round's own: `35{,}566` genuine `\mathcal F`-nodes checked
via a fresh independent harness, `0` violations, on top of the round-12 outline-reviewer's
`\sim200{,}000+`) — but **no proof mechanism attempted so far (domination, FSI-adaptation, direct
witness construction) succeeds on the non-dominated prefix**, and this round's own attempt to adapt
FSI is now known, specifically and structurally, not to work. **Status stays `partial` — no
overclaim: the theorem is not solved, and Gap 1 is not solved, but the remaining open content is now
substantially narrower and more precisely characterized than at the start of the round.**
**Concrete next step:** attack the non-dominated-prefix case directly, using the
Non-Matching-Witness Criterion — i.e. try to *construct* (not merely posit) a non-`w_1`-matching
optimal witness explicitly, using the specific fact (new this round, §18.3) that `B_0`'s single
element and `d_{k^*}` are the *only* two possible values `C_{\mathrm{lo}}` can ever contain at the
point domination has not yet occurred, and the fact that `d_{k^*}$'s defining property (global
argmin over *all* partners `l`, not just `k^*`) has not yet been used at all in §18's reductions —
it is very likely the missing ingredient, exactly as the outline-reviewer's own diagnosis (§17.5)
anticipated, but through a genuinely new inequality rather than a direct FSI citation.

### 19. Round 13 outliner revision — a new structural lemma ("No-Gap") that (conjecturally)
eliminates one whole branch of Gap 1's case split, plus a two-part attack plan for the sole
surviving hard case, reconciling this round's three independent explorer reports

**Provenance.** Three round-13 explorers scouted Gap 1 from different angles:
`math-explorer-argmin-construction.md` (direct construction using `k^*`'s global-argmin property),
`math-explorer-crux-search.md` (corpus search for a transferable proof shape), and
`math-explorer-shallowest-case.md` (hand-tracing the literal shallowest node of `\mathcal F`'s
`|C_{\mathrm{lo}}|` case split). **None of their findings are proved — every claim below is a
conjecture with computational corroboration only, unless explicitly marked otherwise.** §19.1–19.3
reconcile an apparent conflict between two of the reports; §19.4–19.6 lay out the resulting,
narrower two-part attack plan; §19.7 states the recommended build order.

#### 19.1 Restating the reduction so far

By the certified Background-Splitting Corollary (§18.2, `lemmas/empty-background-and-background-
splitting.md`), Claim A at any `(C,W,\sigma)\in\mathcal F` reduces to Claim A at
`(C_{\mathrm{lo}},W,\sigma\cdot(-1)^h)`, and (§18.3) `|C|=2$ always at the base generator, so
`|C_{\mathrm{lo}}|\in\{0,1,2\}`. `|C_{\mathrm{lo}}|=0` is already fully closed
(Empty-Background Lemma). The residual case split is `|C_{\mathrm{lo}}|\in\{1,2\}`.

#### 19.2 An apparent conflict between two explorer reports, resolved

`math-explorer-shallowest-case.md` treats `|C_{\mathrm{lo}}|=1` (background `\{c\}`, `\sigma=-1`,
`c<w_1:=\max(W)`) as "a real, reachable case... nothing in the base generator's definition prevents
this" and reports strong computational support (`0/5961`, `0/2949`) for a **fully general,
provenance-free** claim: for *arbitrary* `c\ge0` and *arbitrary* sorted `W$ with `c<\max(W)`,
`\mathrm{OPT}_{-1}(\{c\},W)` always has a non-`\max(W)`-matching optimal witness. It also flags a
possible **circularity**: the naive witness-swap proof attempt for this case fails pointwise, and
the MATCH branch of a `|C_{\mathrm{lo}}|=1` node's own recursive sub-search regenerates a
**2-element** background `\{c,w_1-w_m\}` — so a proof of `|C_{\mathrm{lo}}|=1` might need
`|C_{\mathrm{lo}}|=2$'s hard case already, not the reverse.

`math-explorer-argmin-construction.md`, independently, reports (POSITIVE finding 2, the **"No-Gap"**
fact) that at the base generator, **no element of `Z_1` ever lies strictly between `\min(b_0,
d_{k^*})` and `\max(b_0,d_{k^*})`** — `0` violations across `2059$ random trials — and, critically,
**independently verified this consequence directly** (not merely inferred): across an exhaustive-
feeling `3623`-node sweep of the *entire* DELETE/KEEP closure (depth `\le5`), **every single
non-dominated-or-empty node has `|C_{\mathrm{lo}}|` exactly `2`, never `1`** (`test_structure2.py`/
`test_structure3.py`, `0/1583` then `0/3623` "partially dominated" nodes found).

**These two findings are in tension, and the tension is worth resolving precisely, not glossing
over.** Since `h:=|\{c\in C:c\ge w_1\}|$ (the certified Background-Splitting definition,
`lemmas/empty-background-and-background-splitting.md`, uses `\ge`, not `>`), `h=1` at a node with
`C=\{c_1,c_2\}` means *exactly one* of `c_1,c_2` is `\ge w_1:=\max(W)$ and the other is `<w_1`. But
`w_1` is *itself* an element of the current `W` (its maximum) — and at the base generator, the
current `W` is `Z_1`. So "`h=1` occurs at the base generator" is **exactly** the statement "`w_1=
\max(Z_1)$, an element of `Z_1`, lies weakly between `\min(b_0,d_{k^*})` and `\max(b_0,d_{k^*})`" —
precisely the event the No-Gap fact (if true) rules out. **So if the No-Gap fact is correct, `h=1`
(equivalently `|C_{\mathrm{lo}}|=1`) never occurs at the base generator at all — matching
`math-explorer-argmin-construction.md`'s own direct computational confirmation, and contradicting
`math-explorer-shallowest-case.md`'s (untested) assumption that it is "a real, reachable case."**
`math-explorer-shallowest-case.md` did not itself check whether `h=1` actually arises from genuine
`\mathcal F`-provenance (its `|C_{\mathrm{lo}}|=1` tests are all on *arbitrary* `c,W`, deliberately
decoupled from provenance, to test a stronger, cleaner conjecture) — so there is **no actual
contradiction in the data**, only in what each report implicitly assumed about scope. The reconciled
picture: `math-explorer-shallowest-case.md`'s general lemma may well be true and is a nice,
independently interesting fact, but (**if** No-Gap holds) it is **not needed anywhere in the Gap-1
induction**, because the case it addresses never actually arises along a genuine `\mathcal F` path.

**This also defuses the flagged circularity concern**, at least conditionally: if `|C_{\mathrm{lo}}|
=1` is vacuous within `\mathcal F`, the induction of §17.5 never needs to invoke a
`|C_{\mathrm{lo}}|=1` lemma at all (matching or general), so it cannot depend circularly on
`|C_{\mathrm{lo}}|=2`. **This resolution is conditional on No-Gap actually being true and on it
propagating to every depth of `\mathcal F`, not just the base generator — currently corroborated
(`0/1583`, then `0/3623`, at depth `\le5`) but not proved.** If a future, deeper/adversarial sweep
*does* find a `|C_{\mathrm{lo}}|=1` node, the circularity concern becomes live again and
`math-explorer-shallowest-case.md`'s general lemma (or a `\mathcal F`-scoped version of it) would
become a real, needed target — flagged as an explicit fallback, not assumed away.

#### 19.3 The No-Gap Lemma: statement, why its inductive step is free, and where the real content is

**Conjectured Lemma (No-Gap).** At the base generator (`B_0=\{b_0\}`, `Z_0`, trigger `M<A_1`,
`k^*` a global argmin, `d_{k^*}:=z_1-z_{k^*}`): no element of `Z_1:=Z_0\setminus\{z_1,z_{k^*}\}`
lies strictly between `\min(b_0,d_{k^*})` and `\max(b_0,d_{k^*})`.

**Why, if true, it propagates to every node of `\mathcal F` for free (the inductive step costs
nothing).** While `|C|=2$ (i.e. before domination), DELETE closure leaves `C` untouched and only
ever *removes* elements from `W` — so "no surviving element of `W` is strictly between `c_1,c_2`"
is inherited automatically by any subset of `W`. KEEP closure at an `h=0` node (both `c_1,c_2<w_1`)
also leaves `C` unchanged (`C_{\mathrm{lo}}=C`, both elements survive, only `\sigma$ flips) and
removes `w_1$ from `W` — again inherited automatically. **So the entire content of the No-Gap
Lemma, at every depth, reduces to the single base-generator statement above** — matching this
round's dispatch's request to find "the first real use of `k^*`'s GLOBAL-argmin property": that
property is needed exactly once, at the base case, not at every node.

**A concrete, not-yet-attempted route to the base case (flagged for the builder, not executed
here).** Suppose for contradiction some `z_j\in Z_1` (`j\notin\{1,k^*\}`) lies strictly between
`b_0` and `d_{k^*}`. The natural candidate for a contradiction is to compare `A_{3,k^*}=M` against
`A_{3,j}=\mathrm{OPT}_{+1}(B_0\cup\{d_j\},Z_0\setminus\{z_1,z_j\})` (`k^*`'s own global-minimality
gives `M\le A_{3,j}`) — and try to show that `z_j` sitting in the forbidden gap forces the *reverse*
strict inequality `A_{3,j}<M`, a contradiction. The natural tool is the certified Background-
Splitting/Rank-Extraction machinery applied to `\{b_0,d_j\}` vs. `\{b_0,d_{k^*}\}` (both share `b_0`,
and each background's "other" element sits on the opposite side of `z_j`/`z_{k^*}` respectively from
the other's). **This has not been attempted — it is the single most promising, concretely
targetable next construction, and is exactly the first place `d_{k^*}`'s *global* (not just
pairwise) argmin property would be used.** Watch out for: the trigger hypothesis `M<A_1` itself may
also need to be invoked (not just `k^*`'s argmin-ness) — no report has yet checked whether No-Gap
survives with the trigger condition dropped.

#### 19.4 Consequence (conditional on 19.3): Gap 1 narrows to the single case `|C_{\mathrm{lo}}|=2`

If the No-Gap Lemma holds, Gap 1's entire residual content (per the Background-Splitting Corollary,
§18.2) is confined to nodes `(C,W,\sigma)\in\mathcal F` with `C=\{c_1,c_2\}$, `c_1<c_2<w_1:=
\max(W)` — i.e. exactly `math-explorer-shallowest-case.md`'s "harder, provenance-dependent" case
(its own minimal counterexample to the arbitrary-background version: `C=\{2,4\},W=(5,3)`,
`\mathrm{OPT}_{-1}=4$, achievable only by matching `5\leftrightarrow3`, confirming this case is
genuinely provenance-bound, not free). **Both signs `\sigma=\pm1` still occur at this case** (KEEP
closure flips `\sigma$ at every step while `h=0`, so a path can visit `|C_{\mathrm{lo}}|=2` nodes of
either sign — already correctly noted, non-vacuously, by the existing §17.6 Gap 3 discussion; no
change to that finding).

#### 19.5 A two-part decomposition of Claim A at `|C_{\mathrm{lo}}|=2`, using explorer (a)'s Sum
Bound and explorer (b)'s extremal-witness proof shape

At a node `(C,W,\sigma)\in\mathcal F` with `C=\{c_1,c_2\}$, both `<w_1:=\max(W)`, write
`\mathrm{rest}:=W\setminus\{w_1\}`. Claim A (`\mathrm{MATCH}` does not strictly beat `\sigma`-opt
(`\mathrm{DEL}`,`\mathrm{KEEP}`)) splits cleanly into two independent halves:

**(a) KEEP-vs-DEL (the easier half — a candidate closed sub-lemma already on the table).**
`math-explorer-argmin-construction.md`'s **Sum Bound** conjecture (POSITIVE finding 3): at `\sigma=
+1`,
```
w_1 \ge \mathrm{OPT}_{+1}(C,\mathrm{rest}) + \mathrm{OPT}_{-1}(C,\mathrm{rest}),
```
which (via the already-certified Rank-Extraction closed form, `\mathrm{KEEP}=w_1-\mathrm{OPT}_{-1}
(C,\mathrm{rest})` when `h=0`) is *exactly* "`\mathrm{KEEP}\ge\mathrm{DEL}`," i.e. KEEP never
strictly beats DEL at `\sigma=+1`. Corroborated (`112/112` genuine non-dominated base-generator
instances) but **decisively refuted as a free-standing, provenance-independent fact** (`4\%`–`12\%`
failure on arbitrary same-shape backgrounds) — so any proof must use `C=\{b_0,d_{k^*}\}`'s specific
relationship to `Z_0`/the trigger, not generic domination. **The `\sigma=-1` mirror statement (DEL
does not beat KEEP) has not yet even been formulated or tested** — flagged as a cheap, concrete
first task for the next round (should follow by an analogous Rank-Extraction manipulation, not yet
written down).

**(b) MATCH-vs-`\sigma`-opt(DEL,KEEP) (the hard half — the genuine, unaddressed content of Gap 1).**
No lemma on file bounds this directly (FSI decisively does not, §18.4). Recommended technique, per
`math-explorer-crux-search.md`'s corpus finding (Candidate 1, the "extremal witness + secondary
tie-break + local rewrite" shape, cf. `aimo-0960`, `aimo-0438`, `aimo-0666`, `aimo-0119`,
`aimo-0553` — adapted, not cited as authority, per CLAUDE.md): suppose for contradiction *every*
optimal witness of `V:=\mathrm{OPT}_\sigma(C,W)` matches `w_1` (the exact negation the certified
Non-Matching-Witness Criterion needs ruled out). Among all such witnesses, pick one under a
**secondary extremal criterion** — two natural candidates flagged by the crux-search and
argmin-construction explorers: (i) minimize `|w_1-w_m|$ (the matched gap), or (ii) maximize the
number of `C`'s own two elements left untouched by any match anywhere in the witness. Then attempt a
**local rewrite** (replace the `(w_1,w_m)` match by keeping or deleting both) whose *exact* value
change is computed via the certified General Rank-Extraction Identity (the analog of `aimo-0960`'s
closed-form `2\psi^e=\psi^{e-2}+\psi^{e+1}` rewrite — this problem's version does not yet exist and
must be derived, not assumed), and derive a contradiction with either `\eta`'s optimality or the
tie-break's own extremality.

**A promising shortcut, flagged by both `math-explorer-crux-search.md` and the existing §18.4/§18.6
record: the contradiction hypothesis above ("every optimal witness matches `w_1`") has *never once
been observed to occur* in any sweep on file (`0/417` in §18.4, reconfirmed this round).** If this
is later shown to be **vacuously true on `\mathcal F`** (i.e., a non-matching optimal witness always
exists trivially, with no repair/contradiction machinery needed), the heavier extremal-rewrite
argument in (b) above would be unnecessary — a **direct existence/construction** argument (build the
non-matching witness explicitly from `B_0`'s and `d_{k^*}`'s specific values, e.g. by exhibiting the
selection directly rather than arguing by contradiction) may be the right route and should be tried
*first*, before committing to the heavier machinery. This is exactly `math-explorer-shallowest-
case.md`'s own "value-level reduction" attempt (which got partway before getting stuck — see its
report for the exact place the direct approach currently fails: the abstraction `w_1\ge e(N\cup
\{w_m\})+e(N\cup\{w_1-w_m\})` for a general bounded multiset `N` is FALSE, `5859/50000`, so any
direct argument must keep `N`'s structural origin — a genuine sorted-list `K/D/M` selection, not an
arbitrary bounded multiset — intact throughout).

#### 19.6 Explicit gaps (for the builder)

- **Gap 1a (No-Gap Lemma, base case).** Prove: no `z_j\in Z_1` lies strictly between `\min(b_0,
  d_{k^*})` and `\max(b_0,d_{k^*})`, using `k^*`'s global-argmin property (§19.3). **Highest
  priority** — if this closes, it eliminates the `|C_{\mathrm{lo}}|=1` branch entirely (§19.2/19.4)
  and resolves the flagged circularity concern conditionally.
- **Gap 1b (KEEP-vs-DEL, `\sigma=+1`; the Sum Bound).** Prove `w_1\ge\mathrm{OPT}_{+1}(C,
  \mathrm{rest})+\mathrm{OPT}_{-1}(C,\mathrm{rest})` for genuine `\mathcal F`-provenance `C=
  \{c_1,c_2\}`, using the trigger/argmin structure, not generic domination (§19.5(a)).
- **Gap 1b' (KEEP-vs-DEL, `\sigma=-1` mirror).** Formulate and prove the analogous statement — not
  yet even written down; cheap to attempt in parallel with 1b.
- **Gap 1c (MATCH-vs-DEL/KEEP, the central hard content).** Either (i) show the "forced-matching"
  hypothesis is vacuous on `\mathcal F` (every node already has a non-`w_1`-matching optimal
  witness, constructively) — try this **first**, cheaper if it works — or (ii), if some genuine
  forced-matching node is ever found, run the extremal-witness+secondary-tie-break+local-rewrite
  argument of §19.5(b) to rule it out.
- **Gap 1d (fallback, only if Gap 1a fails at some depth).** `math-explorer-shallowest-case.md`'s
  general (provenance-free) `|C_{\mathrm{lo}}|=1` lemma (`\mathrm{OPT}_{-1}(\{c\},W)` always has a
  non-`\max(W)`-matching optimal witness, for arbitrary `c<\max(W)`) — corroborated (`0/5961$,
  `0/2949`) but with its own natural pointwise-swap proof attempt shown to fail (§ shallowest-case
  report), and a real circularity risk (its own MATCH branch regenerates a 2-element background).
  Not on the critical path if Gap 1a holds; keep as an explicitly named fallback, not a required
  target this round.

#### 19.7 Recommended build order

1. **Gap 1a (No-Gap base case)** — cheapest structural payoff: if proved, one whole branch of the
   case split vanishes and the flagged circularity concern is defused.
2. **Gap 1b + 1b' (Sum Bound, both signs)** — closes the easier "KEEP-vs-DEL" half of Claim A at
   `|C_{\mathrm{lo}}|=2`, isolating MATCH-vs-DEL/KEEP as the sole remaining content.
3. **Gap 1c(i) first (vacuity check/direct construction), then 1c(ii) (extremal-rewrite) only if
   forced-matching is ever actually exhibited** — the central hard content; per §19.5, attempt the
   cheaper direct-construction route before the heavier contradiction-based machinery.
4. Only if 1a fails at some depth, fall back to Gap 1d as a required (not merely optional) target.

**Watch out for:** (i) tie/boundary conventions — `h:=|\{c\in C:c\ge w_1\}|` uses `\ge`, so an
element of `C` exactly equal to `w_1` counts as dominating; any proof of Gap 1a/1b must track this
convention precisely, not "generic strict/weak" reasoning; (ii) Gap 1a's propagation argument
(§19.3) relies on the *specific* fact that DELETE/KEEP-while-`h=0` never changes `C` — re-verify
this still holds exactly as stated, not just "similarly," before using it as a free inductive step;
(iii) do not conflate `math-explorer-shallowest-case.md`'s general `|C_{\mathrm{lo}}|=1` lemma
(Gap 1d) with `math-explorer-argmin-construction.md`'s Sign-Determined DEL/KEEP-Suffices conjecture
(POSITIVE finding 1) — the latter is a claim about *which* branch wins at a generic
`\mathcal F`-node of *either* `|C_{\mathrm{lo}}|` size, and is exactly equivalent, once Gap 1b/1c are
both proved, to Claim A itself (DEL-suffices at `\sigma=+1$ = "KEEP doesn't beat DEL" (1b) + "MATCH
doesn't beat DEL" (1c); KEEP-suffices at `\sigma=-1` is the mirror) — it is a *repackaging* of the
same two gaps, not a third independent target.

### 20. Round 13 build — Gap 1a's statement corrected and precision-fixed (per the outline-review's
flagged issue), extended (deeper, tie-focused) corroboration of Gaps 1a/1b, a new genuine
structural identity for Gap 1a (not a full proof), and a decisive negative result narrowing Gap 1c
— **none of Gaps 1a/1b/1c is proved this round; Status honestly stays `partial`**

**Headline, stated up front per CLAUDE.md.** This round's build does **not** close Gap 1a, 1b, or
1c. What it does: (i) fixes the precise scope of the No-Gap Lemma exactly along the lines the
round-13 outline-reviewer flagged (the literal strict-betweenness statement under-covers the
tie/boundary event that also produces `h=1`); (ii) extends computational corroboration of the
*correctly-scoped* statement well beyond what was on file, specifically targeting the tie/boundary
case that had never been tested before this round; (iii) identifies one new, fully-proved (if
elementary) algebraic identity that pins down exactly what a swap-based proof of Gap 1a would need
to control, without completing the sign argument; (iv) extends the Sum Bound's (Gap 1b)
corroboration to much deeper DELETE-closure chains and isolates its cleanest nontrivial sub-case
(`\mathrm{rest}=\emptyset`) with a concrete numerical margin; (v) proves, with an explicit
counterexample, that Gap 1c's "forced-matching never occurs" cannot be a background-size-free
general fact (ruling out the cheapest possible shortcut) while extending its `\mathcal F`-restricted
corroboration to `19{,}862` fresh checks, `0` violations. All computation this round is fresh,
independent code (`/tmp/round-13/builder-work/`, not reusing the outliner's or any explorer's
`/tmp/round-13/work/` harness), exact-integer/exact-`Fraction` arithmetic, brute force over the
finite selection space, validated against the file's own three worked examples before being
trusted (`OPT_{+1}([5,8],(10,8,7,2))=0/2`, `OPT_{+1}([1],(10,8,7))=0/1`,
`OPT_{-1}([2,4],(5,3))=4`, all reproduced exactly).

#### 20.1 Gap 1a — the No-Gap Lemma's precise scope, fixed

**The exact issue (re-derived independently, matching the outline-reviewer's finding).** Recall
`h:=|\{c\in C:c\ge w_1\}|` (certified Background-Splitting convention, **`\ge`**, not `>`). For
`C=\{x,y\}` (`x\ne y`, WLOG `x<y`) and `w_1:=\max(Z_1)`, a direct four-way case check on where
`w_1` falls gives:
```
w_1 > y            =>  h=0   (both x,y < w_1)
w_1 = y            =>  h=1   (y\ge w_1 by equality; x<y=w_1)
x < w_1 < y        =>  h=1
w_1 = x            =>  h=2   (x\ge w_1 by equality; y>x=w_1 so y\ge w_1 too)
w_1 < x            =>  h=2
```
So **`h=1` occurs exactly when `x<w_1\le y`, i.e. `w_1` lies in the *half-open* interval
`(\min(x,y),\max(x,y)]`** — strict at the low end, but **including equality at the high end**. The
`\S19.3` "Conjectured Lemma" as literally written ("no element of `Z_1` lies *strictly* between
`\min(b_0,d_{k^*})` and `\max(b_0,d_{k^*})`") only rules out the open interval `(\min,\max)` and
says nothing about the boundary case `w_1=\max(b_0,d_{k^*})` exactly — exactly the gap the
round-13 outline-reviewer flagged. **Corrected statement (what is actually needed, and what this
round's computation targets):**

**No-Gap Lemma (corrected, half-open form).** At the base generator (`B_0=\{b_0\}`, `Z_0`, trigger
`M<A_1`, `k^*` a global argmin, `d_{k^*}:=z_1-z_{k^*}`, `b_0\ne d_{k^*}`): no element `z_j\in
Z_1:=Z_0\setminus\{z_1,z_{k^*}\}` satisfies `\min(b_0,d_{k^*})<z_j\le\max(b_0,d_{k^*})`. (If
`b_0=d_{k^*}` the interval is empty and the statement is vacuous — this degenerate case needs no
separate argument.)

The propagation argument of `\S19.3` (DELETE closure only removes elements of `W`, so "no
surviving element is in the forbidden interval" is inherited automatically; KEEP closure at an
`h=0` node leaves `C` unchanged and only removes `w_1`, so likewise inherited) goes through
**unchanged** for this corrected half-open statement — re-checked explicitly this round, no
additional case needed: the propagation step never touches the boundary/interior distinction, it
only uses "the forbidden interval attached to `(C,\text{current }W)` is a *fixed* set (depending
only on `C`, i.e. on `b_0,d_{k^*}`, not on `W`) and every future top element is drawn from
`Z_1\setminus\{\text{already-peeled elements}\}`" — true regardless of whether the interval is
open, closed, or half-open.

**New, extended computational corroboration (this round, fresh code, explicitly targeting the
previously-untested tie/boundary event).** Two independent batteries, both counting **four**
separate events per `(z_j,\text{instance})` check: strict-interior violations (the old, weaker
statement), half-open violations (`h=1`, the statement actually needed), and the two individual
boundary-tie events `z_j=\max(b_0,d_{k^*})` ("tie at hi", the specific case the strict statement
misses) and `z_j=\min(b_0,d_{k^*})` ("tie at lo", already excluded even by the strict statement,
checked as a sanity control).
- **Random, duplicate-allowing sweep** (deliberately *not* deduplicating `Z_0`, so exact ties
  between list entries — the regime most likely to produce a boundary tie — are heavily
  represented): `q\le7`, `v_{\max}\in\{1,2,3,4,5\}`, `4000` raw trials per `v_{\max}`, `20{,}000`
  total: **`4026`** triggered instances, **`9267`** total `z_j`-checks, **`0`** strict violations,
  **`0`** half-open violations, **`0`** tie-at-hi events, **`0`** tie-at-lo events.
- **Exhaustive (not sampled) sweep**, every `Z_0\in\{0,\dots,v_{\max}\}^q` with `\ge2` distinct
  values (duplicates allowed and common at these small alphabets), every `b_0\in\{0,\dots,
  v_{\max}\}`: `q=3,v_{\max}=3` (`96` triggered, `96` checks), `q=4,v_{\max}=3` (`360`/`720`),
  `q=4,v_{\max}=4` (`948`/`1896`), `q=5,v_{\max}=3` (`1280`/`3840`) — **`0`/`0`/`0`/`0`** on all
  four counters, every case.
- **Fine-grained rational adversarial hill-climb** (own implementation, independent of the
  outline-reviewer's `hillclimb_tie.py`): minimizing the signed margin to the forbidden half-open
  interval (negative = inside/violation) over `\mathbb Q`-valued `Z_0,b_0$, perturbation step sizes
  shrinking to `1/16`: best (smallest, i.e. closest to violating) margin found across `70+`
  restarts at `q=3,\dots,7` was **`+1/16`** with the finest step size tested — **never `0` or
  negative** — and the minimal margin found visibly *shrinks* as the step-size granularity is
  refined (`1/4\to1/16` across successive batteries), consistent with the true infimum of the
  margin being exactly `0` (the inequality is **tight**, i.e. sharp, not proved with slack) but
  never crossed. This is a materially stronger corroboration than the outline-reviewer's own
  integer-only hill-climb (which could not distinguish "true infimum `0`, never crossed" from "true
  infimum `1`, an integer artifact") — the present finding rules out the latter interpretation.

**A new, fully proved elementary identity, pinning down exactly what a swap-based proof needs (not
itself a proof of Gap 1a).** For any two indices `i,l\notin\{1\}$ in the same `Z_0`, writing
`d_i:=z_1-z_i,d_l:=z_1-z_l`:
```
d_i - d_l = z_l - z_i        (Coincidence Identity — immediate from the definitions, no proof needed
                               beyond substitution: d_i-d_l=(z_1-z_i)-(z_1-z_l)=z_l-z_i).
```
Applying this with `i=k^*,l=j` (the two indices at the heart of the No-Gap statement):
`d_j-d_{k^*}=z_{k^*}-z_j=:\delta`. **Consequence, checked concretely this round:** if an optimal
witness `\eta^*` for `A_{3,k^*}=M` keeps `z_j$ (does not match or delete it), then swapping
`d_{k^*}\to d_j` in the background *and simultaneously* `z_j\to z_{k^*}` in the kept-value set
(replacing the background element `d_{k^*}` by `d_{k^*}+\delta=d_j`, and the kept list-value `z_j`
by `z_j+\delta=z_{k^*}$, both by the identical shift `\delta`, leaving every other element of the
underlying multiset untouched) is a **valid** selection of `\big(Z_0\setminus\{z_1,z_j\},\,
\{b_0,d_j\}\big)`, giving a genuine upper bound `A_{3,j}\le e(F')` where `F'` is this shifted
multiset. **This reduces (this specific sub-case of) Gap 1a to a two-element-shift perturbation
question about `e`** — a strictly more tractable-looking target than the raw OPT comparison — but
**completing the sign argument (showing `e(F')<M` exactly when `z_j` is in the forbidden interval)
was not achieved this round**: the shift amount `\delta=z_{k^*}-z_j$ has no a priori controlled
sign or magnitude from the No-Gap hypothesis alone (only `k^*`'s *global* argmin-ness constrains it,
and the trigger condition `M<A_1` — flagged in `\S19.3` as possibly also needed — was **not** yet
incorporated into this attempt at all). Genuinely new, but **honestly not a proof**; flagged as the
single most concrete unfinished thread for the next round, including the explicit reminder that the
symmetric sub-case (`\eta^*` matches or deletes `z_j`, rather than keeps it) was not even attempted.

**Net status of Gap 1a.** Statement corrected to the precisely-needed half-open form (fixing the
outline-review's flagged issue); corroborated far more thoroughly than before, with the specific
new finding that the boundary/tie sub-case (previously entirely untested) also has `0` violations,
across `9267+6552=15{,}819` combined checks this round; one new proved identity narrows exactly what
a direct proof would need; the underlying inequality itself remains **unproved**.

#### 20.2 Gap 1b (Sum Bound) — deeper corroboration, a tractable sub-case isolated, not proved

Extended the existing `112/112` corroboration (base-generator level only) to **genuine DELETE-
closure chains several steps deep** (not merely the base generator), independently coded:
`q\le6,v_{\max}=5`, depth `\le4`: **`156`** genuine `|C_{\mathrm{lo}}|=2$ checks (`c_1,c_2<w_1`),
**`0`** violations of `w_1\ge\mathrm{OPT}_{+1}(C,\mathrm{rest})+\mathrm{OPT}_{-1}(C,\mathrm{rest})`;
`q\le8,v_{\max}=6`, depth `\le6`: **`337`** checks, **`0`** violations. Both batteries include
duplicate/tie-heavy instances (no deduplication of `Z_0`).

**A concrete, cleanly-isolated sub-case worth targeting directly: `\mathrm{rest}=\emptyset`
(`W$ has shrunk to the single element `w_1`).** Here the selection space over `\mathrm{rest}` is
trivial (nothing to select), so `\mathrm{OPT}_{+1}(C,\emptyset)=\mathrm{OPT}_{-1}(C,\emptyset)=
e(C)=|c_1-c_2|` **exactly** (no optimization at all — both signs are forced to the single available
value), so the Sum Bound at this sub-case reduces to the completely explicit numeric claim
`w_1\ge2|c_1-c_2|`. Checked directly (fresh code, this round): across every genuine
`\mathrm{rest}=\emptyset$ node found in a `20{,}000`-trial sweep (`q\le6,v_{\max}=7`, depth `\le5`,
`c_1\ne c_2`), the ratio `w_1/|c_1-c_2|` was **never below `3`** (minimum found: exactly `3`, e.g.
`C=(3,1),w_1=6`) — i.e. the sub-case is corroborated with a **comfortable factor-of-`1.5`
margin** over what the general Sum Bound would merely need (`\ge2`), suggesting real unused slack
and making this the most promising concrete foothold for a future direct proof (e.g. via a
dedicated argument bounding `w_1$ below by `3|c_1-c_2|` or at least `2|c_1-c_2|` using the specific
`b_0,d_{k^*}$ provenance) — **not attempted to completion this round**, honestly left open.

#### 20.3 Gap 1c — the cheap "fully general" shortcut is FALSE (new negative result); extended
`\mathcal F`-restricted corroboration; direct-construction route confirmed as the right target,
still not proved

**Per the dispatch's suggested cheap shortcut:** checked directly whether "forced matching"
(**every** optimal witness of `\mathrm{OPT}_\sigma(C,W)$ matches `w_1$) can be ruled out by a fully
general, background-size-bounded (not `\mathcal F$-provenance-tied) argument — i.e. whether the
`|C|\le2` structural bound alone (already shown, `\S18.5`, insufficient for the *value* inequality)
might at least suffice for this weaker *existence*-of-non-matching-witness question. **It does
not — decisive counterexample, background size `1` already suffices:**
```
C=[3], W=(4,1,0), sigma=+1:  OPT_{+1}([3],(4,1,0)) = 0,
  achieved ONLY by witnesses matching w_1=4 to 1 (diff 3, cancelling the background exactly):
  {('M',4,1),('K',0)} and {('M',4,1),('D',0)} — the only two optimal witnesses, BOTH matching.
  The best non-matching (DELETE/KEEP-only) value is 1 (achieved by KEEPing both 4 and 3... i.e.
  OPT_KD_{+1}([3],(4,1,0))=1 > 0), so this is a genuine forced-matching event.
```
Extended random sweep confirms this is not a fluke: background size `1,2,3` (arbitrary values, not
`\mathcal F`-provenance), `q\le6,v_{\max}=5`, `3000` trials each: forced-matching events **`99`**
(`bg=1`), **`116`** (`bg=2`), **`138`** (`bg=3`), versus **`0`/`3000`** at `bg=0` (matching the
already-certified Empty-Background Lemma, which explicitly constructs a non-matching optimum).
**Conclusion: the existence claim genuinely needs `\mathcal F`'s specific provenance (the trigger,
the global argmin, and the resulting relationship between `C`'s two elements and `Z_1`), exactly
mirroring the already-established pattern for the Sum Bound (`\S19.5(a)`, "decisively refuted as a
free-standing fact") — this is a real, useful negative result (parallel structure, independently
re-derived, not merely inferred by analogy) ruling out the single cheapest possible route to Gap
1c, not a setback relative to what was already known about the Sum Bound's own provenance-
dependence.**

**Extended `\mathcal F`-restricted corroboration (this round, fresh code, deeper than any prior
sweep on this specific question):** walking the full DELETE/KEEP closure from fresh base-generator
triggers to depth `3`–`4`, both signs tracked exactly via the `(-1)^{h+1}` rule: `q\le5,v_{\max}=4`
(depth `3`): `1001` nodes; `q\le6,v_{\max}=5` (depth `4`): `5299` nodes; `q\le6,v_{\max}\in
\{1,2,3\}` (depth `4`, duplicate-heavy): `4741+4099+4722=13{,}562` nodes. **Grand total `19{,}862`
genuine `\mathcal F`-provenance checks this round, `0` forced-matching events** — extends but does
not exceed the qualitative finding already on file (`0/417`, `\S18.4/\S18.6`); this round's
contribution is scale (`\sim48\times` more checks), duplicate-heavy stress-testing, and explicit
depth (not just base-generator-level). **The existence claim itself (a non-matching optimal witness
always exists at genuine `\mathcal F` nodes) remains unproved** — per `\S19.5`'s own recommended
order, the appropriate next step is still a **direct construction** (build the non-matching witness
explicitly from `b_0,d_{k^*}`'s specific relationship to the current `W`), not the heavier
extremal-rewrite/contradiction machinery, since no forced-matching instance has ever been found to
rewrite away from. No such direct construction was attempted this round beyond the shortcut check
above; this is the cleanest concrete target for a future round.

#### 20.4 Honest assessment — what changed, what remains open

**Fixed, not merely re-tested:** Gap 1a's literal statement now precisely matches what the `\S19.2`
reconciliation argument actually needs (half-open, not open, interval) — this was a genuine latent
imprecision (flagged by the round-13 outline-reviewer, confirmed real by re-deriving the `h=1`
case-by-case classification from the certified `\ge`-convention above), now corrected in this file.
**Strengthened, with new content, not just repeated:** (1) the tie/boundary sub-case of Gap 1a,
never tested by any prior round, now has `0/15{,}819` combined checks including exhaustive small
cases and a fine-grained rational hill-climb showing the margin's infimum is genuinely `0`
(tight), not a coarse integer artifact; (2) Gap 1b's corroboration now extends to deep DELETE
chains (not just the base generator) and isolates an explicit, fully-elementary sub-case
(`\mathrm{rest}=\emptyset`) with a quantified safety margin (`\ge3\times` vs. the needed `2\times`);
(3) Gap 1c has one new decisive negative result (the cheapest possible shortcut — a fully general,
provenance-free existence argument — is FALSE, concrete counterexample at background size `1`) plus
a `\sim48\times`-larger corroboration of the correctly-scoped claim. **None of Gaps 1a, 1b, 1c is
proved.** One new, fully-proved (elementary) identity (`\S20.1`'s Coincidence Identity,
`d_i-d_l=z_l-z_i`) is available for a future attempt but does not by itself close anything. Status
correctly stays `partial` — genuine, honestly-scoped incremental progress (a precision fix,
substantially more thorough corroboration specifically targeting previously-untested edge cases, a
new elementary identity, and a decisive negative result narrowing Gap 1c), not a closure of any of
the three remaining gaps.

### 21. Round 14 outliner revision — a much simpler route for Gap 1a (new "Deletion-Suffices-for-`k^*`"
sub-lemma), a piecewise-linear/breakpoint proof mechanism for Gap 1b (with a sharper, corrected
tightness diagnosis), and a proved general "Shrink-List Monotonicity" lemma that isolates Gap 1c to
one narrow "half-step" sub-lemma — **none of Gaps 1a/1b/1c is closed by this revision; it re-plans
the attack, it does not supply new proofs**

**Provenance.** Three round-14 explorers scouted Gap 1a (`math-explorer-gap1a.md`), Gap 1b
(`math-explorer-gap1b.md`), and Gap 1c (`math-explorer-gap1c.md`) in parallel, each targeting one of
round 13's three named gaps directly. All three findings are corroborated computationally, none is a
completed proof. `dyadic-cascade-induction` and `concavity-minimax-duality` remain benched — none of
this round's three reports surfaced anything usable by either (reconfirmed, no new leverage on the
already-unconditional lower bound or on an `A`-generic upper-bound statement) — no un-benching this
round.

#### 21.1 Gap 1a — retargeted to one new sub-lemma, "Deletion-Suffices for `k^*`" (**PRIORITY BUILD
TARGET 1**)

**A new, elementary, sign-unambiguous route, replacing the round-13 Coincidence-Identity swap
attempt as the primary mechanism** (the swap route is not refuted, only found to be fighting an
uphill battle — see Watch out for below; it is demoted, not deleted).

**Step 1 (proved, elementary, no hypothesis needed).** For any index `j`, the single selection
"keep `z_j`, delete every other element of `Z_0\setminus\{z_1\}`" is a valid witness for
`A_1:=\mathrm{OPT}_{+1}(\{b_0\},Z_0\setminus\{z_1\})`, so
```
A_1 \le |b_0-z_j|                                                    (†)
```
for every `j` — a one-line consequence of the DELETE branch contributing `0` to `e` (already the
standing convention throughout `\mathcal F`'s recursion, e.g. the certified Extreme-Element Peeling
Lemma). No further proof obligation here.

**Step 2 (the one real open sub-lemma — conjectural, computationally corroborated, NOT proved).**

**Deletion-Suffices-for-`k^*`.** At a genuine base-generator instance (trigger `M<A_1`, `k^*` a
global argmin, `d_{k^*}:=z_1-z_{k^*}`):
```
M = A_{3,k^*} = \mathrm{OPT}_{+1}(\{b_0,d_{k^*}\}, Z_1) = e(\{b_0,d_{k^*}\}) = |b_0-d_{k^*}|
```
exactly — i.e. `k^*`'s own recursive sub-problem is optimized by deleting **every** element of
`Z_1:=Z_0\setminus\{z_1,z_{k^*}\}`; no KEEP/MATCH combination inside `k^*`'s own residual list ever
helps, **conditional on the trigger `M<A_1` and `k^*`'s genuine global-argmin-ness**. **Not a free
fact in general** — a hand-built non-triggered counterexample kills the unconditional version
(`Z_0=[100,98,70,60],b_0=10`: `k^*` gives `z_{k^*}=98,d_{k^*}=2`, so the naive claim would need
`M=8`, but `M=2` via a Lemma-P duplicate cancellation matching the residual pair `(70,60)`) — so this
is a real, non-vacuous hypothesis about the trigger+global-argmin scope specifically, not a
disguised triviality. **Corroboration:** `0` violations across an exhaustive sweep (`q\le5,
v_{\max}=4`, `360` triggered instances), a broad random sweep (`1376` triggered `|B_0|=1` instances,
`q\in[3,8],v_{\max}\in\{2,\dots,12\}`), and three independent wide-range adversarial random searches
specifically hunting `M<D` inside genuine trigger+argmin scope (`v_{\max}` up to `25`, tens of
thousands of raw trials each) — over `27{,}000` combined genuine trigger+argmin checks, zero
exceptions.

**Step 3 (proved, given Step 2 — the "three-line" closure).** If `z_j\in(\min(b_0,d_{k^*}),
\max(b_0,d_{k^*})]`, monotonicity of `x\mapsto|b_0-x|` on each side of `b_0` gives `|b_0-z_j|\le
|b_0-d_{k^*}|=D`. By Step 2, `D=M`. By (†), `A_1\le|b_0-z_j|\le M`, contradicting the strict trigger
`M<A_1`. This **exactly** reproduces the half-open shape certified in `\S20.1`: at the boundary
`z_j=\max(b_0,d_{k^*})` exactly, `|b_0-z_j|=D=M$ (not `<M`), yet `A_1\le M` still contradicts the
*strict* trigger — so the boundary tie is forbidden too, with no separate case needed. **Free bonus
(not required, but costs nothing extra once Step 2 is proved):** the identical argument at
`z_j=\min(b_0,d_{k^*})` also gives `A_1\le M`, suggesting the fully **closed** interval
`[\min,\max]` is forbidden — strictly stronger than what `\S19/\S20` need (the `h=2` boundary is
already handled separately by the Background-Splitting machinery, so this costs nothing but should
be recorded if the builder gets it for free).

**Open gap — proving Step 2 (Deletion-Suffices-for-`k^*`).** Two candidate directions, **neither
worked out**, both flagged by the explorer as concrete next attempts:
  (a) Suppose for contradiction some selection `\eta` of `Z_1` beats `D=|b_0-d_{k^*}|`. Since `A_1`'s
      own search space is `Z_0\setminus\{z_1\}=Z_1\cup\{z_{k^*}\}` (exactly one element larger than
      `Z_1`), try extending `\eta` by also deleting `z_{k^*}` — this gives *some* concrete value for
      `A_1`'s search space, and the trigger (`A_1>M`) constrains how large `A_1` must be; the goal is
      to derive a contradiction with the trigger from this embedding. **Not completed** — the
      background for `\eta` (`\{b_0,d_{k^*}\}`, two elements) and the background for `A_1`
      (`\{b_0\}`, one element) differ, so a literal "same selection, bigger space" argument (as in
      the free Shrink-List Monotonicity Lemma of `\S21.3`) does not immediately apply; the two
      searches are not nested in the list-only sense, only in a sense that also changes the
      background. This mismatch is exactly why Step 2 is a genuine open sub-lemma, not a free
      corollary of already-certified machinery.
  (b) Alternatively, try to re-embed `\eta` (or a modification of it) as a witness for some *other*
      partner's sub-problem `A_{3,l}$ (`l\ne k^*`), and show it forces `A_{3,l}<M`, contradicting
      `k^*`'s **global** minimality (`M=\min_l A_{3,l}`). Also **not completed** — no explicit
      re-embedding has been constructed.
  Either route needs the trigger hypothesis and/or `k^*`'s *global* (not merely pairwise) argmin
  property invoked directly — per the explorer's perturbation experiments (`2000+` checks forcing
  `z_j` into the forbidden interval), forcing entry into the interval **always** broke the trigger
  and **never once** broke `k^*`'s global-argmin-ness (`0/129+`), a strong empirical signal that the
  trigger is the load-bearing hypothesis for Step 2, not just a side condition.

**Watch out for:** do not resurrect the round-13 Coincidence-Identity swap (`A_{3,k^*}` vs.
`A_{3,j}`, sign of `\delta=z_{k^*}-z_j`) as the primary mechanism — it is not disproved, but this
round's perturbation evidence suggests it is fighting the wrong hypothesis (it never found the
argmin property breaking, only the trigger). It may still be useful as an internal tool inside a
Step-2 proof attempt (e.g. formalizing route (b) above), just not as the top-level argument.

#### 21.2 Gap 1b — piecewise-linear/breakpoint proof mechanism, with sharper (corrected) tightness
diagnosis (**PRIORITY BUILD TARGET 3**)

**Sharper tightness finding (supersedes round 13's "asymptotically tight at ratio 2" note — that
correction stands, but was incomplete).** Round 13 found the *ratio* `w_1/|c_1-c_2|\to2` in the
`\mathrm{rest}=\emptyset` sub-case, with a *constant* additive gap (`w_1-2|c_1-c_2|\to2$, never
shrinking) in its one tested family. This round found a genuinely sharper 2-parameter family
(`Z_0=(n+t,n,n)`, `b_0\to n/2^-$, `t\to0^+`) driving the **additive** gap to `0` as well — there is
**no uniform additive slack at all**, only the multiplicative constant `2` survives, and the extremal
limit is exactly the simultaneous degeneration of (a) `z_{k^*}$ becoming an exact duplicate of `w_1`
(a Lemma-P-style duplicate pair) and (b) `b_0` sitting exactly at the tie point of `A_1`'s own two
candidate branches. **Stronger still:** exact equality of the **full** Sum Bound (not just the
`\mathrm{rest}=\emptyset$ sub-case) is attained at genuine *finite* `\mathcal F`-provenance
instances, not merely approached in a limit — `21/822$ (`\approx2.6\%`) of triggered checks in one
sweep, concrete exact-fraction witness on file (`Z_0=(8,25/4,25/4,55/12,13/3),b_0=23/6`, giving
`\mathrm{OPT}_{+1}+\mathrm{OPT}_{-1}=25/4=w_1` exactly). **Diagnosis:** this witness is precisely a
node where `\mathrm{KEEP}=\mathrm{DEL}$ exactly one level up (verified via the certified
Rank-Extraction identity) — a genuine tie, not a numeric coincidence. **Conclusion for the builder:
any proof of the Sum Bound must be an essentially-tight inequality with zero slack anywhere — do not
attempt any argument that loses even a constant amount of margin.**

**Candidate proof mechanism (not attempted — the concrete next construction).** Freeze every
coordinate of the instance except one continuously-varying parameter (`b_0`, or any single `z_i`).
`\mathrm{OPT}_{+1}` is a min, `\mathrm{OPT}_{-1}` a max, of finitely many affine functions of that
parameter (exactly what the DELETE/KEEP/MATCH recursion computes — a finite case split, each case
affine in any single frozen-shape coordinate), so `w_1-\mathrm{OPT}_{+1}(C,\mathrm{rest})-
\mathrm{OPT}_{-1}(C,\mathrm{rest})` is **piecewise-linear** in that parameter. A non-constant affine
function has no interior minimum, so the minimum over any interval occurs at a **breakpoint** — a tie
between two branches of some inner `\min`/`\max`. This is **exactly** the mechanism that already
closed the "all-cycles" gap (Shared-Value Cycle-Breaking Lemma, rounds 6-7) and underlies the
certified Vertex Lemma. **Concrete task for the builder:** enumerate the finitely many breakpoint
types for the Sum Bound's own recursion —
  (i) a tie between `A_1`'s own two candidate branches (reduces, via Lemma P, to a
      duplicate-cancellation instance — the mechanism behind this round's finding 1's extremal
      family),
  (ii) a `\mathrm{KEEP}=\mathrm{DEL}` tie one level up (the mechanism behind finding 2's exact
      finite witness),
  (iii) `d_{k^*}` colliding with another `z`-value (untested, flagged as a third possible breakpoint
      type, not yet observed but not ruled out),
and show the Sum Bound reduces, **at each breakpoint type**, to a lower-dimensional identity
dischargeable by already-certified machinery (Lemma P for (i); Rank-Extraction for (ii); unknown for
(iii)). **None of this enumeration or reduction has been attempted — this is the open gap.**

**Outline-reviewer precision note (round 14, fixable, not fatal):** the three breakpoint types above
are stated as if checking them once, at the outermost level, suffices. This is NOT automatic:
`\mathrm{OPT}_{+1}(C,\mathrm{rest})` and `\mathrm{OPT}_{-1}(C,\mathrm{rest})` are themselves defined by
the SAME recursive DELETE/KEEP/MATCH trichotomy one level down, so as the frozen parameter varies, a
breakpoint can also arise from a tie *inside* that inner recursion (e.g. two branches of
`\mathrm{rest}`'s own trichotomy crossing) — not only from `A_1`'s branches tying or a `\mathrm{KEEP}
=\mathrm{DEL}` tie at the one level named. Independently verified computationally (`w_1-
\mathrm{OPT}_{+1}(C,\mathrm{rest})-\mathrm{OPT}_{-1}(C,\mathrm{rest})` is genuinely piecewise-linear as
claimed, with a real breakpoint reproduced exactly where a frozen coordinate crosses a `\mathrm{rest}`
value — corroborating the *technique*), but the "three types" list is very likely INCOMPLETE as a flat
enumeration; the correct mechanism needs a **strong induction on `|\mathrm{rest}|`** (exactly the
shape that closed the all-cycles gap via the Vertex Lemma / Shared-Value Cycle-Breaking Lemma), with
the three named types serving only as the BASE-CASE breakpoint classification, not the full one. A
builder should state and use the inductive form explicitly, not attempt a single flat case check.

**Also queued (cheap, parallel task, not yet even formulated):** the `\sigma=-1$ mirror of the Sum
Bound.

**Watch out for:** do not report any "comfortable margin" for the `\mathrm{rest}=\emptyset` sub-case
or any other sub-case of the Sum Bound — this round's finding supersedes round 13's already-corrected
note with an even tighter (zero-slack) diagnosis; any future proof attempt that budgets slack anywhere
will fail against the exact finite equality witness above.

#### 21.3 Gap 1c — a proved general lemma (certify outright) plus a retargeted, narrower "half-step"
sub-lemma (**PRIORITY BUILD TARGET 2**)

**New general lemma — Shrink-List Monotonicity (recommend CERTIFYING OUTRIGHT this round, no further
computation needed beyond the write-up).**

**Lemma (Shrink-List Monotonicity).** For any background `C`, list `W`, and any `x\in W`:
```
\mathrm{OPT}_{+1}(C,W) \le \mathrm{OPT}_{+1}(C,W\setminus\{x\})          (mirror \ge at \sigma=-1)
```
**Proof (one-line bijection, fully general, no `\mathcal F`-restriction needed).** Take any selection
`\eta$ of `W\setminus\{x\}` achieving `\mathrm{OPT}_{+1}(C,W\setminus\{x\})`, and extend it to a
selection of `W` by additionally deleting `x`. Since a deleted element contributes `0` to `e` (the
standing convention throughout the `\mathrm{OPT}_\sigma$ recursion — the same convention the
certified Extreme-Element Peeling Lemma already relies on), this extension has the identical value.
It is one particular (not necessarily optimal) selection of the bigger space `W`, so
`\mathrm{OPT}_{+1}(C,W)\le` that value `=\mathrm{OPT}_{+1}(C,W\setminus\{x\})`. `\blacksquare`
Independently corroborated by the explorer on fully arbitrary `(C,W)`, no `\mathcal F`-restriction:
`0/14{,}160+` violations. **Builder's one required check (cheap, should be immediate): confirm this
"deleted element contributes `0`" convention is exactly how `\mathrm{OPT}_\sigma$ is defined in this
file (§13.2/§17.2), not merely assumed by analogy — a mismatched background/list convention here
would silently break the identity.** Given that check, this is ready to promote to `lemmas/`.

**Retargeted half-step sub-lemma (the actual remaining hard content of Gap 1c).** Writing
`d:=w_1-w_m` for a match partner `w_m\in W\setminus\{w_1\}`, `X:=\mathrm{rest}\setminus\{w_m\}`
(i.e. `W` with both `w_1` and `w_m` removed):
```
\mathrm{MATCH}_m = \mathrm{OPT}_{+1}(C\cup\{d\},X)
```
**Correction to the explorer's own report (important — the two steps in its chain are NOT the same
lemma, despite being labeled identically as "Step A/B: general shrink-the-list monotonicity"):**
```
MATCH_m = OPT_{+1}(C\cup{d}, X)
        >= OPT_{+1}(C, X)              <- NOT the Shrink-List lemma: background shrinks (C\cup{d}->C),
                                           the LIST X is unchanged. This is the load-bearing,
                                           F-specific "half-step" -- the one open sub-lemma.
        >= OPT_{+1}(C, rest) = DEL     <- IS the Shrink-List lemma (list shrinks, rest = X u {w_m},
                                           background C fixed) -- free, certified above.
```
The explorer's own bullet text mislabels the first inequality as "the same general lemma," but its
own very next paragraph correctly identifies it as **the entire locus of Gap 1c's difficulty** — the
outliner has resolved this internal inconsistency in favor of the (correct) second reading. **Only
the second inequality (list-shrinking, `C` fixed) is the free Shrink-List Monotonicity Lemma; the
first (background-shrinking, list fixed) is exactly this round's open "half-step" lemma:**
```
Half-step lemma (conjectural): OPT_{+1}(C\cup{d},X) >= OPT_{+1}(C,X)
  for genuine F-provenance (C,W,sigma=+1) and d = w_1-w_m.
```
**This is NOT a free consequence of Shrink-List Monotonicity, and is NOT the already-dead general
background-insertion monotonicity** (that unconditional statement, `\mathrm{OPT}_{+1}(C\cup\{d\},W)
\ge\mathrm{OPT}_{+1}(C,W)$ for *arbitrary* `d`, is confirmed FALSE this round — `817/4000`
violations, e.g. `C=[7],d=7`, a duplicate-cancellation instance). The half-step is a genuinely
narrower, `\mathcal F`-specific claim about the *particular* `d=w_1-w_m`: **corroborated `0`
violations across `3400+` checks restricted to genuine `\mathcal F`-provenance**, but **decisively
FALSE the instant `\mathcal F`-provenance is dropped even while keeping the exact structural relation
`d=w_1-w_m$ intact** (`2734/18{,}068$, `\approx15\%`, e.g. `C=[7],W=[5,3]`: `d=2`,
`\mathrm{OPT}_{+1}([7],[3])=7$ vs. `\mathrm{OPT}_{+1}([7,2],[3])=5<7`). **Two cheap sufficient
conditions already ruled out** (do not re-propose): "`d\ge\max(C)`" (domination) is NOT sufficient
(`695/4000` violations, e.g. `C=[8],d=8`: exact duplicate, `e([8,8])=0<8`); the failure mode is a
plain rank/parity-of-insertion effect on `e`, not a magnitude/domination phenomenon — pointing at a
**positional** (not magnitude) sufficient condition, structurally the same flavor as the No-Gap Lemma
(Gap 1a) and the Coincidence Identity (`\S20.1`).

**Suspected (untested) link to Gap 1a — flagged as the single most promising next experiment.** Both
the half-step lemma and Gap 1a's No-Gap Lemma are positional claims about where a *derived*
background value (`d_{k^*}` for 1a, `d=w_1-w_m` here) can sit relative to the current working list,
and both ultimately need `k^*`'s (or, here, an arbitrary partner's) relationship to the trigger.
**Recommended concrete test (not yet run): does the No-Gap property, or its natural generalization
propagated through the DELETE/KEEP closure, directly imply the half-step lemma?** If so, a single
unified positional lemma could close Gap 1a and this retargeted form of Gap 1c together. This is a
hypothesis, not a finding — no code has yet tested this implication directly.

**Per-partner strengthening (bonus simplification, already corroborated, use freely).** The half-step
(and hence Claim A's MATCH branch) has been verified to hold for **every individual partner**
`w_m\in W\setminus\{w_1\}`, not just the value-optimal one (`\sigma=+1`: `1336/1336`; `\sigma=-1`:
`\mathrm{KEEP}\ge\mathrm{MATCH}_m`, `180/180`) — a proof need not identify or track which partner is
optimal; "any partner works" as the non-matching alternative witness.

**Open gaps, explicit:** (1) the half-step lemma itself, `\sigma=+1` (**the main target**); (2) its
`\sigma=-1` mirror — not yet decomposed; flagged as possibly reducible to Gap 1b's Sum Bound plus the
certified Shrink-List lemma rather than independent new content (check this *before* attempting a
fresh proof of the mirror); (3) the suspected Gap-1a/half-step link above (untested).

#### 21.4 Recommended build order this round

1. **Gap 1c's Shrink-List Monotonicity Lemma** — certify outright (free, general, one-line proof,
   already corroborated on 14,000+ arbitrary instances); this costs nothing and is reusable well
   beyond this problem.
2. **Gap 1a's Deletion-Suffices-for-`k^*`** (`\S21.1` Step 2) — highest-leverage open target: it is
   the cheapest-looking remaining hard content in the whole population (a "three-line" closure of
   Gap 1a follows immediately once it is proved), and is exceptionally well corroborated
   (`27{,}000+` genuine trigger+argmin checks, zero exceptions, plus a concrete non-triggered
   counterexample proving it is a real, non-vacuous hypothesis, not disguised triviality).
3. **Gap 1c's retargeted half-step lemma** (`\S21.3`) — comparably well-isolated and corroborated
   (`3400+` checks, `0` violations within `\mathcal F`), with a suspected (untested) structural link
   to Gap 1a's own mechanism worth checking directly — attempt alongside/after Gap 1a, since progress
   on one may transfer to the other.
4. **Gap 1b's breakpoint/piecewise-linear mechanism** (`\S21.2`) — concrete, reuses certified
   machinery (Vertex Lemma technique), but requires a full breakpoint-type enumeration not yet
   attempted; more work than 2/3, third priority.
5. Only after 2-4: the `\sigma=-1` mirrors of both the Sum Bound and the half-step lemma.

**Watch out for (all three gaps):** (i) any claimed "general/provenance-free" version of Steps 2
(Gap 1a), the half-step (Gap 1c), or the Sum Bound (Gap 1b) is now confirmed FALSE in every case
tested this round and last — every valid proof must explicitly use the trigger `M<A_1` and/or `k^*`'s
*global* argmin-ness, not any generic domination/size/magnitude bound; (ii) do not conflate the
certified, general Shrink-List Monotonicity Lemma (`\S21.3`, background fixed, list shrinks — free)
with the retargeted half-step lemma (list fixed, background shrinks — the open, `\mathcal F`-specific
content) — they look superficially similar but are logically independent statements, and the
explorer's own report initially mislabeled them as the same; (iii) Gap 1a's Step 2 and Gap 1c's
half-step are both, independently, suspected to hinge on the *same* underlying positional fact about
derived background values — a proof of one may transfer to the other, but neither has been shown to
literally imply the other yet, so do not assume closing one automatically closes both without
checking.


### 22. Round 14 build — Shrink-List Monotonicity certified in full; a new, strictly more general
"Per-Partner Domination Lemma" found and corroborated that (if proved) closes Gap 1a's
Deletion-Suffices-for-`k^*` WITHOUT needing `k^*`'s global-argmin property at all; the trivial base
case of the new lemma proved in full, the first nontrivial case (`|Z_1|=1`) reduced to one precise
unclosed algebraic sub-case

**Summary of this round's dispatch order (per the outline-reviewer's recommendation): (1) certify
Shrink-List Monotonicity — DONE, see also the standalone `lemmas/shrink-list-monotonicity.md` file;
(2) attack Gap 1a's Deletion-Suffices-for-`k^*` — real progress, new sharper lemma found, not fully
closed; (3)/(4) half-step lemma (Gap 1c) and Sum Bound (Gap 1b) — not reached this round, budget
went entirely into (1)/(2) since (2) surfaced a substantial new mechanism worth following to the
end of the round's time budget rather than splitting effort.**

#### 22.1 Shrink-List Monotonicity Lemma — CERTIFIED (see `lemmas/shrink-list-monotonicity.md`)

The one-line bijection proof sketched in §21.3 is complete and fully general (no `\mathcal
F`-restriction, no hypothesis on `C`,`W`,`x` beyond `x\in W`): extend a `\sigma=+1`-optimal selection
of `W\setminus\{x\}` by additionally deleting `x` (contributes `0`, the standing convention already
used by the certified Extreme-Element Peeling Lemma and Generalized Multi-Background Peeling Lemma);
this is one particular candidate for `OPT_{+1}(C,W)`'s search space with the same value, so
`OPT_{+1}(C,W)\le OPT_{+1}(C,W\setminus\{x\})`; the `\sigma=-1` case mirrors verbatim (extension
witnesses a lower bound for a maximum instead of an upper bound for a minimum). The required
"convention check" the outline flagged (that "deleted `\Rightarrow` contributes `0`" is really how
`\mathrm{OPT}_\sigma$ is defined in this file, §13.2/§17.2, not merely assumed by analogy) is
confirmed directly from §13.2's own definition, which states the value fed to `e` is
"`C\cup K\text{-values}\cup M\text{-differences}`" — deleted elements of `W` are simply absent from
this union, i.e. contribute nothing, exactly the needed convention. Full write-up, with the useful
**Corollary (repeated application)** — `OPT_{+1}(C,W)\le e(C)` for any finite `W`, obtained by
applying the lemma once per element down to the empty list — filed as
`lemmas/shrink-list-monotonicity.md`, recommended for certification.

**Immediate consequence for Gap 1a (new, makes explicit something the population had not previously
isolated as its own clean statement):** applying the Corollary with `C=\{b_0,d_{k^*}\}`, `W=Z_1`
gives, completely unconditionally (no trigger, no argmin hypothesis of any kind):
```
M = A_{3,k^*} = OPT_{+1}(\{b_0,d_{k^*}\},Z_1) \le e(\{b_0,d_{k^*}\}) = |b_0-d_{k^*}| = D.
```
This is the "easy half" of Deletion-Suffices-for-`k^*`, and it is now a fully proved, one-line fact
citing only the certified Shrink-List Corollary — **the entire remaining content of Deletion-Suffices
is the reverse inequality `M\ge D`.** (This was implicit in the population's prior work but had not
been separated out and named; doing so is what makes §22.2 below possible — it isolates exactly the
one inequality that needs a genuinely new argument.)

#### 22.2 A new, strictly more general candidate lemma for Gap 1a's hard direction: the Per-Partner
Domination Lemma

**Motivation.** §21.1's Deletion-Suffices-for-`k^*` needs `k^*`'s *global* argmin-ness (`M=\min_l
A_{3,l}`) as a hypothesis — both of its own flagged proof routes (a)/(b) explicitly tried to invoke
this global property and neither succeeded (§21.1). This round, instead of trying to use the global
minimality directly, we tested whether a **per-partner** (single, fixed `l`, no minimality over other
partners at all) inequality already suffices:

**Conjecture (Per-Partner Domination Lemma).** For *every* index `l\in\{2,\dots,q\}` of a base
generator instance (`B_0=\{b_0\}$, sorted `Z_0=(z_1\ge\dots\ge z_q)`, `A_1:=OPT_{+1}(\{b_0\},
Z_0\setminus\{z_1\})`, `d_l:=z_1-z_l`, `D_l:=|b_0-d_l|`, `A_{3,l}:=OPT_{+1}(\{b_0,d_l\},
Z_0\setminus\{z_1,z_l\})`) — **with no trigger hypothesis and no requirement that `l` be an
argmin of anything**:
```
A_{3,l} \ge \min(A_1, D_l).
```

**Why this immediately gives Deletion-Suffices-for-`k^*` (proved in full, GIVEN the conjecture, and
strictly more cheaply than either of §21.1's two flagged routes — no global-argmin property is
needed at all, only the trigger at the specific index `k^*`):**
Suppose `M<A_1$ (the trigger) and `M=A_{3,k^*}$ (`k^*` is *merely* an index achieving this value at
all — not required to be the minimum over other `l`). Apply the Per-Partner Domination Lemma at
`l=k^*`: `A_{3,k^*}\ge\min(A_1,D_{k^*})`, i.e. `M\ge\min(A_1,D_{k^*})`. If `\min(A_1,D_{k^*})=A_1`,
this gives `M\ge A_1`, contradicting the trigger `M<A_1`. Hence `\min(A_1,D_{k^*})=D_{k^*}$ (so also
`D_{k^*}\le A_1`), giving `M\ge D_{k^*}`. Combined with `M\le D_{k^*}$ (§22.1's free Corollary), `M=
D_{k^*}=D` exactly. `\blacksquare` **This is a genuinely stronger and cleaner reduction than anything
on file before this round: it shows Deletion-Suffices does not need `k^*` to be the TRUE global
argmin — only that the trigger `M<A_1` holds AT `k^*` specifically.** (The global-argmin hypothesis is
of course still true and available in the actual base-generator setting; this finding just shows it
is not needed for *this particular* implication — a genuine simplification of what remains to prove,
even though the Per-Partner Domination Lemma itself is not yet proved.)

**Computational corroboration (fresh this round, three independent batteries, testing the conjecture
directly — no trigger, no argmin restriction, exactly as stated):**
- Random sweep: `q\in\{2,\dots,6\}`, `v_{\max}\in\{1,\dots,12\}`, half-integer `b_0`: `2{,}852`
  instances checked (every `l` at every instance), **`0` violations**.
- Exhaustive sweep, `q=3`, half-integer-valued `z_1,z_2,z_3,b_0\in\{0,\tfrac12,1,\dots,6\}`
  (`N=6`, step `1/2`): **`28{,}392`** `(z_1,z_2,z_3,b_0,l)` instances checked, **`0` violations**.
- Exhaustive sweep, `q=4`, integer-valued `z_i,b_0\in\{0,\dots,4\}`: **`3{,}100`** instances checked,
  **`0` violations**.
Total: **`>34{,}000`** combined checks, `0` violations, across both random and exhaustive coverage
and both integer and half-integer alphabets (the half-integer sweep specifically targets tie/boundary
configurations, per the round-13 lesson about strict-vs-weak boundary events).

**The base case `|Z_1|=0` (i.e. `q=2`) — proved in full, unconditionally.** When `q=2`, the only
possible `l$ is `l=2`, and `Z_0\setminus\{z_1,z_2\}=\emptyset`. By definition, `A_{3,2}=OPT_{+1}
(\{b_0,d_2\},\emptyset)=e(\{b_0,d_2\})=|b_0-d_2|=D_2` exactly (there is no other candidate selection
of the empty list — the search space is a single point). Since `\min(A_1,D_2)\le D_2` always (the
minimum of two quantities never exceeds either one), `A_{3,2}=D_2\ge\min(A_1,D_2)$ trivially. This
proves the Per-Partner Domination Lemma unconditionally whenever `q=2`. `\blacksquare`

**The first nontrivial case, `|Z_1|=1` (i.e. `q=3`, every `l`) — PROVED IN FULL this round (upgraded
from an initial partial reduction found earlier in the same build — see the note at the end of this
subsection on that false start).** Fix `q=3`, an arbitrary `l\in\{2,3\}$, and write `w` for the single
remaining element of `Z_0\setminus\{z_1,z_l\}` (so `\{l\}\cup\{w\text{'s index}\}=\{2,3\}$; the
argument below never uses which of `z_2,z_3` plays the role of `w` versus `z_l`, so it covers both
`l=2` and `l=3` simultaneously, not just one "WLOG" — **no ordering between `w` and `z_l` is assumed
anywhere in the proof**, only `w\ge0`, `b_0\ge0`, `d_l:=z_1-z_l\ge0`, exactly the general shape of the
Per-Partner Domination Lemma itself). Then, since a singleton list has exactly two selections (delete
or keep `w`):
```
A_{3,l} = \min\big(D_l,\ \mathrm{keepval}\big),\qquad \mathrm{keepval}:=e_{\mathrm{sorted}}(\{b_0,d_l,w\}),\qquad D_l:=|b_0-d_l|.
```
**Two free (unconditional, no hypothesis) bounds on `A_1`, both direct consequences of the search
space of `A_1:=OPT_{+1}(\{b_0\},\{z_l,w\})` containing the named candidate selection:**
```
A_1 \le e(\{b_0\}) = b_0                 (delete both z_l,w — Shrink-List Corollary, §22.1)
A_1 \le |b_0-w|                          (delete z_l, keep w — a single valid candidate selection)
```
**Key elementary fact (monotonicity of `\min` in one argument).** For any fixed `D_l`, the map
`x\mapsto\min(D_l,x)` is non-decreasing. Hence if `\mathrm{keepval}\ge A_1`, then
`\min(D_l,\mathrm{keepval})\ge\min(D_l,A_1)=\min(A_1,D_l)$ — **exactly the target inequality.** So it
suffices to show `\mathrm{keepval}\ge A_1` in every case (this already subsumes the earlier "trivial
half," `\mathrm{keepval}\ge D_l$, since if that holds then automatically `\min(D_l,\mathrm{keepval})=
D_l\ge\min(A_1,D_l)` regardless of `\mathrm{keepval}` vs. `A_1` — we do not even need to separate that
case out).

By the certified General Rank-Extraction Identity (`lemmas/general-rank-extraction-identity.md`),
inserting `d_l` into the sorted pair `\{b_0,w\}` gives, casing on where `d_l` falls (three exhaustive,
mutually exclusive cases — independently verified against `20{,}000` fresh random exact-`Fraction`
instances with `0` formula mismatches, `/tmp/round-14/verify_algebra.py`):
```
d_l\ge\max(b_0,w):            keepval = d_l - |b_0-w|                      (Case A)
\min(b_0,w)<d_l<\max(b_0,w):  keepval = b_0+w-d_l                          (Case B; max+min=b_0+w)
d_l\le\min(b_0,w):            keepval = |b_0-w| + d_l                      (Case C)
```

**Case C.** `\mathrm{keepval}=|b_0-w|+d_l\ge|b_0-w|$ (since `d_l\ge0`) `\ge A_1` (second free bound).
`\blacksquare`

**Case B.** Two sub-orderings, both closed by the SAME two free bounds:
- If `w\ge b_0` (so `\max(b_0,w)=w`): Case B's own defining upper bound gives `d_l<w`, i.e. `w-d_l>0`.
  So `\mathrm{keepval}=b_0+(w-d_l)>b_0\ge A_1` (first free bound). `\blacksquare`
- If `w<b_0` (so `\max(b_0,w)=b_0`): Case B's own defining upper bound gives `d_l<b_0`, so
  `D_l=|b_0-d_l|=b_0-d_l`. Then `\mathrm{keepval}=b_0+w-d_l = D_l+w\ge D_l$ (since `w\ge0`) — this is
  the "trivial" sub-case (`\mathrm{keepval}\ge D_l`), which (as noted above) needs no comparison with
  `A_1` at all: `\min(D_l,\mathrm{keepval})=D_l\ge\min(A_1,D_l)`. `\blacksquare`

**Case A.** `D_l=|b_0-d_l|=d_l-b_0` here (since `d_l\ge\max(b_0,w)\ge b_0`). Two sub-orderings:
- If `w\ge b_0` (so `\max(b_0,w)=w`, and Case A's condition becomes `d_l\ge w$, hence also `d_l\ge w
  \ge b_0`, and `|b_0-w|=w-b_0`): `\mathrm{keepval}=d_l-(w-b_0)=d_l+b_0-w=b_0+(d_l-w)\ge b_0\ge A_1`
  (first free bound, using `d_l\ge w$ from Case A's condition in this suborder). `\blacksquare`
- If `w<b_0` (so `\max(b_0,w)=b_0`, Case A's condition is `d_l\ge b_0$, and `|b_0-w|=b_0-w`):
  `\mathrm{keepval}=d_l-(b_0-w)=D_l+w\ge D_l` (since `w\ge0`, using `D_l=d_l-b_0` from above) — again
  the trivial sub-case, `\min(D_l,\mathrm{keepval})=D_l\ge\min(A_1,D_l)`. `\blacksquare`

**All three cases (and every sub-ordering within them) are covered, closing the Per-Partner
Domination Lemma completely and rigorously for `q=3`, every `l\in\{2,3\}`, with no numerical
corroboration needed to trust it — a genuine, from-scratch elementary proof** using only: the General
Rank-Extraction Identity (certified), the Shrink-List Monotonicity Corollary and one other trivial
delete-candidate bound (both free, §22.1), and elementary case-by-case algebra on where a single
inserted value falls relative to two others. Independently re-verified by fresh exact-`Fraction` code
this round, testing the mechanism directly (not just the end conclusion): for `4{,}000` random
`(b_0,w,z_2)` triples (`A_1` computed by brute-force `OPT`, `z_2\ge w`, `z_2$ otherwise free) and `5`
random `d_2` values each (`20{,}000` `(b_0,w,z_2,d_2)` instances total), **`0/20{,}000`** failures of
`A_1\le b_0`, **`0/20{,}000`** failures of `A_1\le|b_0-w|`, and **`0/20{,}000`** failures of the full
target `\min(D_2,\mathrm{keepval})\ge\min(A_1,D_2)` — exactly matching what the proof predicts, with
the specific bounds it relies on individually confirmed, not merely the end-to-end conclusion.

**Note on this subsection's own false start (recorded for transparency, not swept under the rug):**
an earlier pass this same round mistakenly used only the WEAKER bound `A_1\le|b_0-w|` throughout Case
A (rather than switching to the sharper `A_1\le b_0` bound where needed), which produced a spurious
"unclosed algebraic sub-case" — reducing to `A_1\le z_1-z_2-z_3+b_0` under `z_3>2b_0`, which looked
open. Revisiting with the CORRECT bound (`A_1\le b_0`, using `d_l\ge w$ from Case A's own defining
condition once `w\ge b_0`) closes it immediately, as shown above; the "z_3>2b_0, unclosed" framing in
that false start is now superseded and should not be reused.

**`q\ge4` remains open** — corroborated only (the exhaustive/random sweeps in §22.2 above cover
`q=4`, `0` violations, but the proof technique here relies on `Z_0\setminus\{z_1,z_l\}` being a
*singleton* — enough that "keep or delete" are the only two options; for `q\ge4` this residual list
has `\ge2` elements, opening up KEEP-both, MATCH, and mixed selections that this argument does not
address, and a genuine induction on `q` (peeling the top element of `Z_0\setminus\{z_1,z_l\}` via the
certified Generalized Multi-Background Peeling Lemma's own trichotomy, using the `q-1` result as an
inductive hypothesis) would be needed — not attempted this round).

**Honest assessment.** This round: (1) certified a genuinely reusable general lemma (Shrink-List
Monotonicity, now also `lemmas/shrink-list-monotonicity.md`) and used its Corollary to isolate
Deletion-Suffices' "easy half" (`M\le D`) as a one-line unconditional fact; (2) found, heavily
corroborated, and used to derive Deletion-Suffices-for-`k^*` in three lines (**without needing
`k^*`'s global-argmin property at all**, a genuine simplification versus §21.1's two original routes)
a new, strictly more general **Per-Partner Domination Lemma**; (3) **proved this new lemma in full for
`q\le3`** (the `q=2` base case, and now the complete `q=3` case, every `l`, every sub-ordering, via a
clean elementary case analysis with no remaining gap) — the largest fully-closed chunk of the Gap 1a
mechanism produced by any round to date; (4) left `q\ge4` open (corroborated only, `3{,}100` exhaustive
`q=4` checks, `0` violations, plus the broader random sweep up to `q=6`). **Gap 1a is NOT fully closed
this round** — the Per-Partner Domination Lemma is only proved through `q=3`, and Deletion-Suffices'
own base-generator instances can have arbitrarily large `q` — so **Status stays `partial`**. But the
remaining task is now unambiguously "extend the `q=3` proof technique to general `q` by induction,"
a concretely scoped target rather than an open-ended search.

**Recommended next steps (for a future builder/outliner):** (i) attempt the induction on `q` flagged
above: assume the Per-Partner Domination Lemma for all smaller `q$, peel the top element `w_1` of
`Res:=Z_0\setminus\{z_1,z_l\}` (`|Res|=q-2`) via the certified Generalized Multi-Background Peeling
Lemma's trichotomy on `A_{3,l}=OPT_{+1}(\{b_0,d_l\},Res)`, and try to reduce the DELETE/KEEP branches
to the IH plus the same two trivial `A_1$-bounds (`A_1\le b_0`, `A_1\le|b_0-w_1|` type facts, likely
generalized to `A_1\le OPT_{+1}(\{b_0\},Res\setminus\{w_1\})`-style bounds) used here, with the MATCH
branch (new at `q\ge4`, absent at `q=3`) as the one genuinely new sub-case to handle. (ii) Check
whether the technique used here (comparing `A_{3,l}$'s KEEP branch against `A_1`'s own trivial
delete-candidate bounds) has a clean general form not tied to the singleton-list case — e.g. try
`A_1\le OPT_{+1}(\{b_0\}, Res\setminus S)` for various small `S\subset Res` as a general family of
free bounds, analogous to how `A_1\le b_0` and `A_1\le|b_0-w|` were the `S=Res` and `S=Res\setminus\{w\}`
instances respectively at `q=3`. Do **not** re-attempt §21.1's original routes (a)/(b) (which explicitly
needed global-argmin-ness) as the primary mechanism — the Per-Partner Domination route is strictly more
promising since it sidesteps that need entirely, and is now proved through `q=3`.

**(iii, new observation, untested but flagged as important for the next round) Suspected — but NOT
yet checked — link between the `q\ge4` induction and Gap 1c's half-step lemma.** Attempting to
generalize the `q=3` technique (compare `A_{3,l}`'s KEEP-of-a-subset branch against a matching
DELETE-`z_l`-keep-the-same-subset candidate for `A_1`) to a general kept subset `S\subseteq Res`
reduces the comparison to exactly: does `e(\{b_0,d_l\}\cup S) \ge e(\{b_0\}\cup S)` (roughly — the
`q=3` proof's `S=\{w\}` special case used exactly this shape, via the free bound `A_1\le|b_0-w|=
e(\{b_0\}\cup\{w\})`)? **This is structurally the same "does adding one background element `d_l` help
a `\sigma=+1` minimizer" question as Gap 1c's still-open half-step lemma**
(`OPT_{+1}(C\cup\{d\},X)\ge OPT_{+1}(C,X)`, §21.3) — here with `C=\{b_0\}`, `d=d_l`, `X=S`. If this
connection is real (not yet verified — no code has tested whether the `q\ge4` induction literally
reduces to the half-step lemma, or only resembles it), then **fully closing the general-`q` Per-Partner
Domination Lemma may require solving Gap 1c's half-step lemma as a sub-step**, which would unify two
of the population's three named remaining gaps into one shared hard core — worth checking directly
(cheap: construct a `q=4` instance, trace exactly which inequality the induction's KEEP-subset branch
needs, and compare its statement word-for-word against the half-step lemma) before the next round
commits significant effort to either gap in isolation.

### 23. Round 15 outliner revision — the suspected Gap 1a/Gap 1c link is CONFIRMED (with the exact
scoping that makes it true), a new Background-Release Domination Lemma is found but its two obvious
chaining routes are dead, and Gap 1b is retargeted to a base-case-first, recursion-depth induction

**Provenance.** Three round-15 explorers: `math-explorer-gap1a-general-q.md` (general-`q` closure
attempt for the Per-Partner Domination Lemma), `math-explorer-shared-mechanism.md` (direct test of
the §22's iii-flagged suspected Gap-1a/Gap-1c link), `math-explorer-gap1b-breakpoint.md`
(induction-on-`|\mathrm{rest}|` breakpoint proof attempt for the Sum Bound). This section reconciles
all three into one revised skeleton for the file's single remaining route (Claim A, via the
Non-Matching-Witness criterion, §17.4/§17.5) — no new approach is opened, per CLAUDE.md's
single-gap-trap warning: these are three sub-goals of one whole-problem proof, not three problems.

#### 23.1 The unified Gap 1a/Gap 1c mechanism — precise statement, exact scoping, what it does and
does NOT give for free (**PRIORITY BUILD TARGET 1**)

**Precise restatement (this is the corrected, load-bearing form — do not use the looser wording of
§21.3/§22's "iii" note without this correction).** `\mathcal F`'s base generator (§17.2 item 1) is
rooted, after the first match, at `(B_1,Z_1,+1)` with `B_1=\{b_0,d_{k^*}\}`,
`Z_1=Z_0\setminus\{z_1,z_{k^*}\}` — i.e. `k^*`'s own matched sub-instance. Gap 1a's
`A_{3,l}=\mathrm{OPT}_{+1}(\{b_0,d_l\},Z_0\setminus\{z_1,z_l\})` is *exactly*
`\mathrm{OPT}_{+1}(B_1,Z_1)` when `l=k^*`. So Deletion-Suffices-for-`k^*` (`M=D`, §21.1) is literally
the claim that Claim A / Match-Free Recovery holds throughout the entire recursive subtree of
`\mathcal F` rooted AT `(B_1,Z_1,+1)` — not merely "structurally similar to" Gap 1c's half-step, but
a genuine instance of the same theorem the half-step lemma is trying to prove.

**Define, precisely, the scope that makes this true (new this round — was previously only "genuine
`\mathcal F`-provenance", which is NOT enough on its own).**

```
Def (true-argmin-descended). A node (C,W,+1) is true-argmin-descended if it is reachable from a
genuine base generator (B_0,Z_0,+1) by a chain of steps each of which is either:
  (a) DELETE/KEEP (does not change the background), or
  (b) MATCH at the CURRENT list's TRUE global argmin partner (the l minimizing OPT_{+1} of the
      resulting sub-instance among all valid match partners at that step) -- never merely a
      partner that satisfies a local trigger comparison.
```

**Half-step lemma, corrected scope (the actual open content — supersedes §21.3's looser
"`\mathcal F`-provenance" wording):**
```
Half-step lemma (conjectural, PRECISELY rescoped): OPT_{+1}(C\cup{d},X) >= OPT_{+1}(C,X)
  whenever (C,X-related node) is true-argmin-descended in the sense above, with d the difference
  produced by the most recent true-argmin match on the chain.
```
**Computational status (this round, decisive):** tested exactly as stated, one level deeper than
round 14's own test (inside `\mathrm{Res}`'s own further MATCH recursion, not just at the top
level) — `0/3270` (`q=5`, `1362` genuine trigger+true-argmin instances) and `0/690` (`q=6`, `163`
instances), zero violations. Tested with the restriction to "true global argmin" DROPPED (any
partner satisfying only the local trigger) — `1067/7216` (`\approx15\%`) violations, reproducing
round 14's own negative control almost exactly. **This is the single most important corroboration
in the population to date for this specific claim: it is not merely "the half-step survives
testing," it is "the half-step's truth boundary is exactly the true-argmin-descended condition,"
confirmed by explicitly probing both sides of that boundary and finding a sharp transition, not a
gradual one.**

**What proving the half-step (in this corrected scope) gives for Gap 1a, and what it does NOT
give — spelled out precisely so a builder does not overclaim:**
- **Gives:** the MATCH branch of the general-`q` Per-Partner Domination induction (peeling
  `\mathrm{Res}`'s own top element `u_1` and matching it with some `u_i\in\mathrm{Res}`, leaving
  `X=\mathrm{Res}\setminus\{u_1,u_i\}` — the branch that is new and unhandled at `q\ge5`) reduces,
  via [half-step] + [certified Shrink-List Monotonicity, chained exactly as in §21.3's two-step
  chain], to a term already covered by the induction's DELETE/KEEP machinery. This is a genuine,
  short, mechanical reduction (not automatic) — trace it explicitly in the writeup, do not merely
  cite "by the half-step lemma."
- **Does NOT give:** the DELETE and KEEP branches of the same induction still need the generalized
  `A_1`-bound family flagged in §22.2's recommended-next-step (ii) (`A_1\le\mathrm{OPT}_{+1}
  (\{b_0\},\mathrm{Res}\setminus S)` for small `S`, generalizing the `q=3` proof's two ad hoc
  bounds `A_1\le b_0`, `A_1\le|b_0-w|`) — a separate, likely-easier piece, structurally
  Shrink-List-flavored but NOT itself the half-step lemma. **A builder must supply both pieces; do
  not treat proving the half-step alone as closing Gap 1a.**
- **Direction of implication is one-way.** Half-step `\implies` (most of) Gap 1a's `q\ge5` case, via
  the explicit reduction above. The reverse (Per-Partner Domination `\implies` half-step) is NOT
  evident and should not be assumed — the half-step is more naturally its own self-contained strong
  induction on `|X|`.

**New, concrete simplification of scope (from this round's computation) — `q=4` does NOT need the
half-step at all.** At `q=4`, `|\mathrm{Res}|=2`, so matching `\mathrm{Res}`'s own top element
consumes BOTH remaining elements — `X=\emptyset` always, and `\mathrm{OPT}_{+1}(\emptyset\text{-list
plus the new background element})` is a plain `e(\cdot)` evaluation on (at most) a 4-element
multiset, structurally identical in kind to the already-closed `q=3` proof's own 3-element
Rank-Extraction case split (one more element, same technique, no new lemma). **Recommended build
order correction: close `q=4` FIRST, directly, by extending the certified `q=3` proof's exact
technique (Rank-Extraction on the 4-element multiset via the Generalized Multi-Background Peeling
Lemma's own DELETE/KEEP/MATCH split one level in) — likely mechanical, no half-step dependency, and
narrows what is genuinely still open to `q\ge5` only.**

#### 23.2 The Background-Release Domination Lemma — a new general fact, record but do NOT build the
main line on it yet (both chaining routes tested and refuted)

**Statement (new this round, unconditional, `|C|` arbitrary).** For any background `C`
(`|C|\ge1`), list `W`, and any `y\in C` (writing `C'=C\setminus\{y\}`):
```
OPT_{+1}(C,W) >= min( OPT_{+1}(C', W u {y}),  e(C) )        [and the sigma=-1 MAX-dual: max(...)]
```
i.e. releasing one background element back into the free list, or deleting the whole remaining
list, are both valid lower-bound witnesses. **Corroborated `0/6000` (`\sigma=+1`) and `0/6000`
(`\sigma=-1` dual), `|C|` up to 4, deliberately duplicate/tie-heavy alphabets — a strong,
independently useful, background-size-generic fact not previously on file.** **Recommend certifying
this outright as a standalone lemma** (general, no `\mathcal F`-restriction, likely reusable beyond
this specific gap — e.g. flagged by the explorer as a candidate cleaner replacement mechanism for
parts of the already-abandoned `|B|\ge2` Match-Recovery generalization, untested but worth keeping
on record) — **but do NOT make it load-bearing for Gap 1a's closure this round**, because:

**Two chaining routes tested and REFUTED — do not re-attempt either as the closing argument:**
  (a) **Full telescoping to a background-free bound.** Chaining the lemma repeatedly until `C` is
      empty gives a valid-but-useless bound: the chain inequality itself holds (`0/2500`), but the
      resulting background-free term `OPT_{+1}(\emptyset,\mathrm{Res}\cup\{b_0,d_l\})` is too lossy
      — `6918/17956` (`\approx38\%`) violations of `\ge\min(A_1,D_l)` directly. Releasing BOTH
      background elements at once lets them cancel/match against `\mathrm{Res}` or each other,
      destroying the structure the bound needs. **Dead — do not resurrect.**
  (b) **Single-release direct chain against `A_1`.** Releasing only `d_l` and trying to claim
      `OPT_{+1}(\{b_0\},\mathrm{Res}\cup\{d_l\})\ge A_1` (tempting: "same shape, one element
      swapped") — **FALSE**, `1923/12034` (`\approx16\%`) violations, concrete witness
      `z=[6,4,1],b_0=7,l=1`: `A_1=3` but the released quantity is `2<3`. Swapping the list element
      `z_l` for its derived value `d_l=z_1-z_l` is NOT monotone on `\mathrm{OPT}_{+1}` — no
      magnitude/domination relation rescues it. **Dead — do not resurrect.** (Not yet re-tested
      restricted to genuine `\mathcal F`-provenance specifically — flagged by the explorer as a
      cheap, not-yet-run sanity check before fully discarding route (b) in-scope; low priority given
      §23.1's more promising route is already found.)

**A related dead end, worth recording explicitly (same failure family, different mechanism).**
Naively generalizing the `q=3` proof's own Rank-Extraction technique — peeling the derived value
`d_l` directly out of the WHOLE candidate-optimal multiset `S=\{b_0,d_l\}\cup V(\eta)` (rather than
just the 3-element `\{b_0,d_l,w\}` the `q=3` proof actually uses) — produces the inequality
`A_{3,l}\le2e(\mathrm{head})\pm d_l-A_1`, an UPPER bound on `A_{3,l}`, not the LOWER bound
`A_{3,l}\ge\min(A_1,D_l)` actually needed. Hand-derived and confirmed this round; matches the
already-documented "false start" pattern (round 14's Case-A false start, §22.2's own note) — a third
independent instance of the same root cause (naively substituting/releasing a *derived* value in
place of, or alongside, the *original* list element breaks whatever monotonicity the argument
needs; any fix must be positional, not magnitude-based). **Do not re-attempt a flat Rank-Extraction
peel of `d_l` out of the full optimal multiset as the general-`q` mechanism.**

#### 23.3 Gap 1b (Sum Bound) — retargeted to base-case-first, recursion-depth induction (**PRIORITY
BUILD TARGET 2**, in parallel with/after 23.1's `q=4` closure)

**Correction to §21.2's build order (important — do not attempt the inductive step before this base
case is closed).** The `\mathrm{rest}=\emptyset` sub-case (`w_1\ge2|c_1-c_2|` for genuine triggered
`(b_0,d_{k^*})` pairs) has been treated in prior rounds as "the easy anchor" but **is honestly NOT
proved anywhere on file** — rounds 13/14 only computationally corroborated its asymptotic tightness
(ratio `\to2`, `Z_0=(n,n,n+1),b_0=n/2` family). **This must be proved FIRST, as its own standalone
lemma, using the trigger `M<A_1` and `k^*`'s global-argmin property directly** (neither has yet been
invoked in an actual proof attempt of this base case) — it is the anchor of the whole induction, not
a free starting point.

**Revised induction, precisely stated.** `P(k)`: "for every genuine `\mathcal F`-provenance node
`(C,W,+1)` with `C=\{c_1,c_2\}`, `h=0`, and `|\mathrm{rest}|=k`, the Sum Bound
`w_1\ge\mathrm{OPT}_{+1}(C,\mathrm{rest})+\mathrm{OPT}_{-1}(C,\mathrm{rest})` holds." **Correction
to §21.2's own precision note (now confirmed computationally, not just flagged as a risk): the
right induction variable is NOT the flat outer `|\mathrm{rest}|` but the recursion DEPTH of the
whole nested `\mathrm{OPT}_{\pm1}(C,\mathrm{rest})` DELETE/KEEP/MATCH evaluation** — real
breakpoints (slope changes of the piecewise-linear function `G(x):=w_1-\mathrm{OPT}_{+1}(C,
\mathrm{rest})-\mathrm{OPT}_{-1}(C,\mathrm{rest})` as one coordinate of the ORIGINAL `(B_0,Z_0)`
varies) occur strictly INSIDE the inner recursion computing `\mathrm{OPT}_{\pm1}(C,\mathrm{rest})`
itself, confirmed at `|\mathrm{rest}|=1` (a zigzag whose slope changes trace to values crossed
inside the inner `e(\cdot)` computation, not only the three outer breakpoint types of §21.2). A
correct inductive step must therefore be a strong induction on this depth, classifying each
breakpoint as either (a) a genuine value-tie reducible via Lemma P/Rank-Extraction to a strictly
smaller Sum-Bound instance (apply IH), or (b) an argmin/trigger-boundary event that changes which
`\mathcal F`-branch is live but is not itself a new inequality to prove (bookkeeping only).

**Three concrete bookkeeping subtleties a builder must handle explicitly (new this round, not dead
ends, but real extra content beyond a flat 3-type check):**
  1. **Argmin ties spawn simultaneous out-of-scope sibling branches — must filter `h=0` explicitly
     at EVERY branch, not just once.** When multiple `l` tie for the argmin at a swept coordinate,
     some resulting branches have `C` dominated by (containing an element `>w_1`, i.e. `h=1`) and
     are simply out of the Sum Bound's declared scope — these look like violations (`G=-2,-4`
     observed) but are not; restricting to genuine `h=0` branches only recovers `0/100` violations
     in the same sweep. **A future proof or computational check that walks argmin-tie branches
     without this filter will manufacture false counterexamples.**
  2. **Exact equality (`G\equiv0`) can hold along a continuous SUB-INTERVAL, not just isolated
     points.** Concrete witness: `c_1=2`, `\mathrm{rest}=(10,0)`, `w_1=10`, sweeping `c_2` over
     `[5/4,11/4]` gives `G=0` exactly throughout (not approximately) — a flat, zero-slope affine
     piece. Consistent with the breakpoint-induction logic (an extremum is realized throughout a
     zero-slope segment, not just at its endpoints) but the proof must explicitly allow for this,
     not assume finitely many isolated tie witnesses (a stronger tightness structure than round
     14's own finding of isolated exact-equality witnesses).
  3. **A tempting shortcut identity is FALSE — do not use it.** "`\mathrm{OPT}_{+1}(C,\mathrm{rest})
     +\mathrm{OPT}_{-1}(C,\mathrm{rest})=\max(\mathrm{rest})` whenever `C` is `h=0`-dominated by
     `\mathrm{rest}`" held in the specific example that surfaced finding 2 above, but is FALSE in
     general — `306/1888` violations (both directions) on arbitrary such `(C,\mathrm{rest})`
     pairs. **Confirmed dead this round — do not propose or re-derive it as a simplification.**

**Also queued, unchanged from §21.2:** the `\sigma=-1` mirror of the Sum Bound; check first whether
it reduces to the `\sigma=+1` form plus the certified Shrink-List lemma rather than needing
independent new content.

#### 23.4 Recommended build order this round (revised, supersedes §21.4)

1. **Gap 1a's `q=4` case** (§23.1, last paragraph) — closes directly by the already-certified `q=3`
   Rank-Extraction technique extended one element further; no new lemma needed, likely mechanical,
   narrows the open frontier to `q\ge5` only. Cheapest available win in the whole population.
2. **Gap 1b's base case** (`w_1\ge2|c_1-c_2|` for genuine triggered/true-argmin `(b_0,d_{k^*})`
   pairs, §23.3) — must be proved before any inductive step is attempted; currently the field's most
   under-attacked "should be easy but literally has zero proof attempts on file" item.
3. **The corrected half-step lemma** (§23.1) at true-argmin-descended scope — the highest-leverage
   open target: proving it (plus the flagged generalized `A_1`-bound family) closes Gap 1a's `q\ge5`
   MATCH branch via the explicit reduction in §23.1, and directly closes (the retargeted form of)
   Gap 1c. Attempt via strong induction on `|X|`, using the sharp true-argmin-descended/
   trigger-only-partner boundary this round pinned down exactly (do not weaken the hypothesis to
   "genuine `\mathcal F`-provenance" alone — that is not sufficient, per round 14's own negative
   control now correctly reinterpreted).
4. **Gap 1a's `q\ge5` DELETE/KEEP branches** (the generalized `A_1`-bound family, §22.2's
   recommended next step (ii)) — likely easier, Shrink-List-flavored, needed alongside item 3, not
   instead of it.
5. **Gap 1b's inductive step**, phrased as the recursion-depth strong induction of §23.3, using the
   three named bookkeeping subtleties.
6. **Certify the Background-Release Domination Lemma standalone** (§23.2) — cheap, free-standing,
   general; do this whenever convenient, it does not block any of items 1-5.
7. Only after 1-6: the `\sigma=-1` mirrors of the Sum Bound and (if not already subsumed) the
   half-step lemma.

**Watch out for (all items):** (i) do NOT test or use the half-step lemma at any scope other than
"true-argmin-descended" (§23.1's precise definition) — testing at the raw top-level root, or with
any non-argmin match partner at any recursion depth, reproduces large spurious failure rates that
are scoping artifacts, not counterexamples; (ii) do NOT resurrect either Background-Release chaining
route (§23.2(a)/(b)) or the flat-multiset Rank-Extraction peel of `d_l` — all three are now
confirmed dead, all three fail via the same "derived value substituted for original value breaks
monotonicity" root cause; (iii) do NOT attempt Gap 1b's inductive step before its base case is
proved — the base case is not "the easy part," it is currently unproved; (iv) when computationally
testing Gap 1b's induction, always filter `h=0` explicitly on every branch of an argmin tie, and do
not assume finitely many exact-equality witnesses — a continuous tight sub-interval is confirmed to
occur; (v) proving the half-step lemma alone does NOT close Gap 1a by itself — the DELETE/KEEP
branches (generalized `A_1`-bound family) are a separate, still-unproved piece.

**Open gaps, explicit (for the builder, supersedes §21's list):** (1) Gap 1a `q=4` — likely
mechanical, not yet attempted with the corrected scope; (2) Gap 1a `q\ge5` MATCH branch — reduces to
the half-step lemma (item 3 below) via an explicit, spelled-out chain, not yet executed; (3) Gap 1a
`q\ge5` DELETE/KEEP branches — needs the generalized `A_1`-bound family, not yet attempted; (4) the
half-step lemma itself, correctly rescoped to true-argmin-descended `\mathcal F` — the single
highest-leverage open item, well-corroborated (`0/3270+0/690` this round alone, on top of round 14's
`3400+`), not yet proved; (5) Gap 1b's base case (`w_1\ge2|c_1-c_2|`) — corroborated only, no proof
attempted; (6) Gap 1b's inductive step, as a recursion-depth strong induction — mechanism sound,
concrete bookkeeping identified, not yet executed.

**Cases to cover:** Gap 1a's induction must explicitly split `q=4` (mechanical, §23.1) from `q\ge5`
(needs the half-step, §23.1); the half-step's own induction on `|X|` should follow the same DELETE/
KEEP/MATCH trichotomy already certified (Generalized Multi-Background Peeling Lemma); Gap 1b's
induction must explicitly handle argmin-tie-spawned out-of-scope siblings (filter `h=0`) and
zero-slope (flat-interval) breakpoints, not only strict sign-change breakpoints.

### 24. Round 15 build — working through the outline-review's 4 action items: item 1 (the contested
`\sim15\%` claim) is RESOLVED in favor of the reviewer's finding and the half-step's hypothesis is
correspondingly SIMPLIFIED; item 2 (`q=4` DELETE/KEEP) is answered precisely — DEL/KEEP close with
the natural bound family, MATCH does NOT and already needs a piece of the generalized `A_1`-bound
family at `q=4`; item 3 (Gap 1b base case) gets genuine new partial progress (two new proved facts,
an exact reduction, one non-trivial forced-consequence lead) but is **NOT closed**; item 4
(Background-Release lemma) is STRENGTHENED (unconditional form found) and ready to certify. All
computation this round is fresh, independent code, written from the file's own definitions without
reading or reusing any prior round's harness (`/tmp/round-15/verify-builder/`, exact
`fractions.Fraction` arithmetic, brute-force `OPT_\sigma` via full enumeration of DELETE/KEEP/MATCH
selections, validated against the file's own three worked examples — `OPT_{+1}([5,8],(10,8,7,2))=0`,
`OPT_{-1}(\cdot)=10`, `OPT_{+1}([1],(10,8,7))=0`, `OPT_{-1}([2,4],(5,3))=4` — reproduced exactly
before being trusted for anything new, per every prior round's practice).

#### 24.1 Item 1 (highest priority) — the `\sim15\%` "argmin dropped one level deeper" claim is
NOT REPRODUCED; the outline-reviewer's finding is CONFIRMED; the half-step's hypothesis is
simplified

**Test performed, exactly as dispatched.** Built a genuine base generator `(b_0,Z_0)` with a real
trigger `M<A_1` and a real global argmin `k^*` (computed exactly as `\mathcal F`'s own item 1,
§17.2: `A_1:=\mathrm{OPT}_{+1}(\{b_0\},Z_0\setminus\{z_1\})`, `A_{3,l}` for every `l`, `M:=\min_l
A_{3,l}`, `k^*\in\arg\min`), giving `B_1=\{b_0,d_{k^*}\}`, `\mathrm{Res}:=Z_1=Z_0\setminus\{z_1,
z_{k^*}\}`. Peeled `\mathrm{Res}`'s own top element `u_1:=\max(\mathrm{Res})` and tested the
half-step `\mathrm{OPT}_{+1}(B_1\cup\{u_1-u_j\},X)\ge\mathrm{OPT}_{+1}(B_1,X)`
(`X:=\mathrm{Res}\setminus\{u_1,u_j\}`) against **every** possible partner `u_j\in
\mathrm{Res}\setminus\{u_1\}`, not merely the (level-2) argmin partner — exactly as item 1
specifies.

**Result: zero violations.** `q=5` (`v_{\max}\in\{2,3,6,9,12\}`): `4046` triggered instances,
`8092` `(instance,partner)` checks. `q=6` (`v_{\max}\in\{3,5,8,10\}`): `1233` triggered instances,
`3699` checks. `q=7` (`v_{\max}\in\{2,3,4,6,7\}`): `860` triggered instances, `3384` checks.
**Grand total `15{,}175` combined checks, `0` violations, minimum margin found `=0` exactly (never
negative)** — every single second-level partner, not just the true argmin, satisfies the half-step,
given a genuinely triggered top-level base generator. This **independently reproduces the
outline-reviewer's finding, from completely fresh code**, and directly **contradicts** §23.1's own
reported "`1067/7216` (`\approx15\%`) violations" for this exact test.

**Diagnosing the discrepancy (per the dispatch's request to pin down the exact cause, not just
report the mismatch).** Two negative-control experiments, run to see which one plausibly produces a
`\sim15$–`35\%`-scale failure rate close to the outliner's reported figure:
- **"Wrong root" test:** compare the second-level half-step against `B_0=\{b_0\}` (the
  *un-matched* top-level background) instead of the correct `B_1=\{b_0,d_{k^*}\}` — i.e. exactly
  the kind of root-confusion the outline-reviewer speculated about (§1 of its report: "testing
  `(B_0,Z_0)` instead of `(B_1,Z_1)`"). Result: **`19\%$–`36\%`** violation rate (`q=5`: `484/1352`,
  `36\%`; `q=6`: `187/870`, `21\%`; `q=7`: `62/328`, `19\%`) — the same order of magnitude as
  §23.1's reported figure.
- **Dropping the top-level trigger** (accepting `M\ge A_1` instead of requiring `M<A_1`, everything
  else unchanged): **`19\%$–`23\%`** violation rate (`q=5`: `1064/4606`; `q=6`: `1091/4929`; `q=7`:
  `669/3504`) — reconfirming, from fresh code, the already-established (round 12/14) fact that the
  top-level trigger is independently load-bearing, and *also* landing in the same `\sim15$–`35\%`
  ballpark.
- **Fully arbitrary (non-`\mathcal F`) `(C,X)` sanity control:** `23\%$ violation rate — confirms
  the harness correctly detects real violations at the expected background rate when genuine
  provenance is absent, ruling out a harness bug on my end.

Both plausible "bug" scenarios (wrong root; or an untriggered/mis-scoped top level accidentally
mixed in) reproduce a violation rate in the same `\sim20$–`35\%` neighborhood as §23.1's reported
`\sim15\%$ — while the literal, correctly-scoped question (genuine top-level trigger+argmin,
*every* second-level partner) gives a clean, robust, reproducible **zero**. This is not a proof that
I have identified §23.1's *exact* bug, but it is strong, independently-reproduced evidence that the
`\sim15\%` figure is a **scoping/provenance artifact of the outliner's own test setup**
(most likely comparing against the wrong background root, or otherwise losing genuine top-level
`\mathcal F`-provenance one level before the check), **not a real mathematical fact about the
half-step's second-level-partner dependence.**

**Conclusion (per the dispatch's explicit instruction for this outcome): this is GOOD NEWS —
simplify the half-step's hypothesis.** §23.1's "true-argmin-descended" definition (item (b): "MATCH
at the CURRENT list's TRUE global argmin partner ... never merely a partner that satisfies a local
trigger comparison") is **not needed as stated** for steps strictly deeper than the base generator's
own top-level match. The corrected, simplified scope:

```
Half-step lemma (SIMPLIFIED SCOPE, this round's finding): OPT_{+1}(C\cup{d},X) >= OPT_{+1}(C,X)
  whenever C = B_1 = {b_0, d_{k*}} for a genuine base-generator trigger+global-argmin pair
  (b_0, Z_0, k*), X (subset of Res = Z_1) is reached from Res by peeling any sequence of
  DELETE/KEEP/MATCH-WITH-ANY-PARTNER steps, and d is the difference produced by the LAST such
  step. No requirement that any step past the first (top-level) match be its own local or
  global argmin.
```

**What this changes for the build order.** §23.1's own "Gives" bullet (the MATCH branch of the
general-`q` Per-Partner Domination induction reduces via [half-step]+[Shrink-List] to a term already
covered by DELETE/KEEP machinery) still holds, and is now **easier to invoke**, not harder: a
builder attacking the half-step by strong induction on `|X|` no longer needs to separately verify,
at every recursive step, which partner is the "true" local argmin — every partner is licensed. This
does *not* itself prove the half-step (still open, see below), but it removes an entire layer of
bookkeeping (`\S23.4`'s watch-out-for (i), "do NOT test the half-step outside true-argmin-descended
scope," should be read as applying only to the *base generator's own root* being genuine
`\mathcal F`-provenance — not to any deeper match-partner choice).

**Honest scope note.** This round's finding is a *scoping correction*, not a proof of the half-step
itself — the half-step (`\mathrm{OPT}_{+1}(C\cup\{d\},X)\ge\mathrm{OPT}_{+1}(C,X)`, `C=B_1`) remains
an open, unproved (though now more strongly corroborated and more simply scoped) conjecture. Nor
does this round claim to have found §23.1's literal bug — only that two independently-tested,
structurally-plausible bugs reproduce a failure rate of the right order of magnitude, which is
enough to justify dropping the extra hypothesis per the dispatch's own stated decision rule ("If you
confirm 0 violations across all partners ... simplify §23.1's hypothesis").

#### 24.2 Item 2 — `q=4`'s DELETE/KEEP branches: checked directly, NOT free; DEL/KEEP close with the
natural bound family, MATCH already needs a piece of the generalized `A_1`-bound family

**Setup.** At `q=4`, fixed `l`, `\mathrm{Res}=Z_0\setminus\{z_1,z_l\}` has exactly `2` elements
`u_1\ge u_2`. Peeling `\mathrm{Res}`'s own top element `u_1` (Generalized Multi-Background Peeling
Lemma) gives the three branches of `A_{3,l}=\mathrm{OPT}_{+1}(\{b_0,d_l\},\mathrm{Res})`:
```
DEL   = OPT_{+1}({b_0,d_l}, {u_2})           = min( |b_0-d_l|, e_sorted({b_0,d_l,u_2}) )
KEEP  = min( e({b_0,d_l,u_1}), e({b_0,d_l,u_1,u_2}) )     (the two selections of {u_2} with u_1 kept)
MATCH = e({b_0,d_l,|u_1-u_2|})                              (X=\emptyset, confirming §23.1's own
                                                              elementary counting fact)
```
The candidate `q=3`-style free-bound family, extended in the obvious way to `q=4`'s now-3-element
`A_1`-search-space `\{z_l,u_1,u_2\}`: `A_1\le b_0` (delete all, Shrink-List Corollary), `A_1\le
|b_0-u_1|`, `A_1\le|b_0-u_2|` (delete `z_l` and one `\mathrm{Res}`-element, keep the other — the
direct `q=4` analogue of the `q=3` proof's `A_1\le|b_0-w|` bound, now with two instances since
`\mathrm{Res}` has two elements instead of one).

**Test: does `\min(D_l,X)\le V` for some `X` in this 3-bound family (or `V\ge D_l` outright) certify
each branch `V\in\{\mathrm{DEL},\mathrm{KEEP},\mathrm{MATCH}\}$ against the true target
`V\ge\min(A_1,D_l)`?** (This is a valid *sufficient* certification technique: since `A_1\le X$ for
every family member `X`, `V\ge\min(D_l,X)\implies V\ge\min(D_l,A_1)`.) Random + exhaustive sweep,
`q=4`, `v_{\max}\in\{1,2,3,5,8,12,20\}$, `3000` raw trials per `v_{\max}$ (`62{,}580` genuine
`(b_0,Z_0,l)` checks total):
```
DEL:   0/62580 family-certification failures.
KEEP:  0/62580 family-certification failures.
MATCH: 439/62580 family-certification failures  (~0.7%).
```
**The TRUE target (`V\ge\min(A_1,D_l)$, using the exact `A_1`, not a family proxy) holds in every
single one of the `62{,}580` checks, `0` violations** — consistent with, and extending, every prior
round's corroboration of the Per-Partner Domination Lemma. **So this is not a counterexample to the
lemma** — it is a precise diagnosis of exactly where the *proof technique* (the natural extension of
the certified `q=3` argument) runs out of power.

**Root cause, confirmed exactly (not merely suspected): every one of the `439` failures occurs
precisely when `A_1$ is strictly smaller than the ENTIRE simple bound family** (`A_1<\min(b_0,
|b_0-u_1|,|b_0-u_2|)`, confirmed in `439/439` cases, `0` counterexamples to this diagnosis) — i.e.
`A_1$ achieves its true (small) value via an *internal cancellation* within its own 3-element search
space `\{z_l,u_1,u_2\}` (concretely, in the worked example on file: `b_0=1/2`, `Z_0=(2,2,2,3/2)`,
`l=1` gives `z_l=2=u_1`-adjacent duplicate structure driving `A_1=0$ via a Lemma-P-style match/
cancellation, far below any of the three "delete-all-but-one" bounds `\{1/2,3/2,1\}`) — **exactly
the phenomenon the "generalized `A_1`-bound family" was meant to capture, previously assumed
(per §23.4's old item-4 scoping) to be needed only at `q\ge5`.**

**A genuine new elementary lemma, proved in full, that rules out one entire candidate direction for
the generalized family.** The outline-reviewer's own flagged concern (§3 of its report) was that
`q=4` has a genuinely new type of candidate bound unavailable at `q=3` — "keep both `\mathrm{Res}`
elements," i.e. `A_1\le e_{\mathrm{sorted}}(\{b_0,u_1,u_2\})`. **This candidate is NEVER
independently useful — it is always dominated by the simpler delete-all-but-one family:**
```
Lemma (Three-Bound Domination). For any nonnegative reals x,y,z:
    min(x, |x-y|, |x-z|)  <=  e_sorted({x,y,z})     (= max - mid + min).
```
*Proof.* Case-split on the rank of `x` among `\{x,y,z\}` (call the sorted values `M\ge\mathrm{md}
\ge m`). If `x=M`: the other two values are `\{\mathrm{md},m\}` in some order, so `\{|x-y|,|x-z|\}=
\{M-\mathrm{md},M-m\}`, and `\min(x,|x-y|,|x-z|)\le M-\mathrm{md}\le M-\mathrm{md}+m` (since
`m\ge0`), matching the RHS exactly. If `x=m`: `\min(x,\dots)\le x=m\le M-\mathrm{md}+m` (since
`M\ge\mathrm{md}$ gives `M-\mathrm{md}\ge0`). If `x=\mathrm{md}`: the other two are `\{M,m\}$, so
`\{|x-y|,|x-z|\}=\{M-\mathrm{md},\mathrm{md}-m\}`, and `\min(x,|x-y|,|x-z|)\le M-\mathrm{md}\le
M-\mathrm{md}+m`. All three (exhaustive, by rank) cases give the bound. `\blacksquare`
Independently confirmed computationally on `200{,}000` fully arbitrary (`x,y,z$, no `\mathcal
F`-connection at all) random trials, `0` violations, and specifically on the `q=4` construction
itself (`59{,}844$ genuine `(b_0,\mathrm{Res},l)$ triples across `5` values of `v_{\max}`, `0`
instances where the keep-both bound is strictly smaller than the delete-all-but-one family).
**This rules out "keep both `\mathrm{Res}` elements" as a component of the generalized `A_1`-bound
family — it never adds information beyond the simpler family — narrowing what the real
generalization must look like** (it must be a bound that, like `A_1$ itself in the failing
examples, captures *matching/cancellation* structure inside `A_1`'s own search space, not merely
more "keep a subset, delete the rest" candidates).

**Answer to item 2, stated precisely.** **NO — the `q=3` proof's exact two bounds do NOT suffice for
`q=4`; the DELETE and KEEP branches close with the natural 3-bound extension of that family, but the
MATCH branch already needs a genuine piece of the "generalized `A_1`-bound family" at `q=4`, not
first at `q\ge5` as §23.4's build order assumed.** This corrects the recommended build order: item 1
of §23.4 ("`q=4` case ... closes directly ... no new lemma needed, likely mechanical") is **not
accurate for the MATCH branch** — `q=4`'s MATCH branch needs the same generalized-bound-family
machinery previously reserved for `q\ge5`'s DELETE/KEEP branches (item 4 of the old build order), so
these two "separate" open items are in fact the same piece of work, needed one case earlier than
assumed. (DEL and KEEP at `q=4` genuinely are free with the natural extension, so that half of the
old claim survives.)

#### 24.3 Item 3 — Gap 1b's base case (`w_1\ge2|c_1-c_2|`, `\mathrm{rest}=\emptyset`): two new proved
facts, an exact reduction, one forced-consequence lead — **NOT closed**

Recall the target: at a genuine `\mathcal F`-node with `C=\{b_0,d_{k^*}\}`, `h=0` (`b_0,d_{k^*}<
w_1`), and `\mathrm{rest}=\emptyset` (i.e. `q=3`, so `Z_1=\{w_1\}` is a singleton — the base
generator's own residual, no further DELETE steps needed), prove `w_1\ge2D_{k^*}`,
`D_{k^*}:=|b_0-d_{k^*}|`.

**New Lemma (Keep-Top Bound) — fully proved, general, holds for ANY `q` (not just the base case).**
At any `\mathcal F`-node `(C,W,+1)$ with `C=\{c_1,c_2\}`, `h=0` (`c_1,c_2<w_1:=\max(W)`):
```
OPT_{+1}(C,W) <= w_1 - |c_1-c_2|.
```
*Proof.* The selection "keep `w_1`, delete every other element of `W`" is a valid candidate,
giving `\mathrm{OPT}_{+1}(C,W)\le e_{\mathrm{sorted}}(\{c_1,c_2,w_1\})`. Since `h=0` means `w_1$ is
strictly the largest of the three, `e_{\mathrm{sorted}}(\{c_1,c_2,w_1\})=w_1-\max(c_1,c_2)+
\min(c_1,c_2)=w_1-|c_1-c_2|$. `\blacksquare` Applied at the base generator (`C=\{b_0,d_{k^*}\}`,
`W=Z_1`, `w_1=\max(Z_1)`): `M\le w_1-D_{k^*}`, i.e. **`w_1\ge M+D_{k^*}`**. Independently confirmed
computationally, `0` violations across every `h=0` instance checked this round (folded into the
`\mathrm{rest}=\emptyset` sweep below).

**New Fact (exact `q=3` dichotomy) — fully proved, elementary.** At `\mathrm{rest}=\emptyset$
(`Z_1=\{w_1\}$ a singleton), `M:=A_{3,k^*}=\mathrm{OPT}_{+1}(\{b_0,d_{k^*}\},\{w_1\})` has **exactly
two** candidate selections (delete `w_1`, or keep it) — no other option exists for a 1-element
list — so
```
M = min( D_{k*},  w_1 - D_{k*} )     exactly (not merely <=), given h=0.
```
*Proof.* Delete `w_1`: value `e(\{b_0,d_{k^*}\})=D_{k^*}`. Keep `w_1`: value
`e_{\mathrm{sorted}}(\{b_0,d_{k^*},w_1\})=w_1-D_{k^*}` (as in the Keep-Top Bound proof, using
`h=0`). Since these are the *only* two selections of a singleton list, `M` equals the smaller of the
two exactly. `\blacksquare`

**Consequence — an exact, useful reformulation of the base case (not new information, but a
strictly sharper target).** `w_1\ge2D_{k^*}$ holds if and only if `D_{k^*}\le w_1-D_{k^*}`, i.e. **if
and only if `M=D_{k^*}$ (the DELETE branch of `A_{3,k^*}`'s own two-candidate dichotomy wins or
ties)** — equivalently, the base case is **exactly** the claim "the KEEP branch (`M=w_1-D_{k^*}`)
never strictly beats DELETE at `A_{3,k^*}`'s own top-level decomposition, given a genuine trigger
and `k^*`'s global argmin-ness." (Caution, confirmed by direct check: this reformulation is a
*restatement*, not an independent stepping stone — since `M=\min(D_{k^*},w_1-D_{k^*})` exactly, "`M
=D_{k^*}`" and "`w_1\ge2D_{k^*}`" are the same event by definition; an early attempt this round to
use "`M=D_{k^*}$ observed in `4227/4227$ fresh checks" as a separate lemma was recognized as circular
and discarded.)

**A genuine new necessary condition, derived but not yet closed into a full contradiction (the
concrete open thread for the next round).** Suppose, for contradiction, the KEEP branch strictly
wins: `M=w_1-D_{k^*}<D_{k^*}$ (i.e. `w_1<2D_{k^*}`). The free bound `A_1\le w_1-b_0` (delete `z_{k^*}`,
keep `w_1$, within `A_1`'s own 2-element search space `\{z_{k^*},w_1\}` at `q=3`) combined with the
trigger `M<A_1` gives `w_1-D_{k^*}<w_1-b_0`, i.e. **`D_{k^*}>b_0` strictly** — a genuine, new,
non-trivial forced consequence of the contradiction hypothesis (equivalently: `d_{k^*}>2b_0`, since
`D_{k^*}=|b_0-d_{k^*}|>b_0\ge0` forces `d_{k^*}>2b_0`, not `d_{k^*}<0$ which is impossible). A second
partial chain was set up but not reconciled with the first: applying `k^*`'s global-argmin property
at the *other* index `l'$ (`z_{l'}=w_1`) gives `M\le A_{3,l'}\le D_{l'}=|b_0-d_{l'}|`
(`d_{l'}:=z_1-w_1`, via the Shrink-List Corollary), i.e. `w_1-D_{k^*}\le D_{l'}`. **Both chains
involve the so-far-unconstrained relationship between `z_{k^*}` (equivalently `d_{k^*}`) and `w_1`,
`z_1$; closing the contradiction requires pinning this down, which was not completed this round.**
Computationally, the contradiction hypothesis (`w_1<2D_{k^*}`) was confirmed to **never actually
occur**: a fresh, independent sweep of `q=3`, `h=0`, genuinely triggered instances (`v_{\max}\in
\{1,2,3,5,8,12,20,30,50\}`, `4227` instances) found `M=D_{k^*}` in **`4227/4227`** cases, `0`
exceptions — strong corroboration that the base case is true, but **not a proof that the KEEP
branch winning is impossible.**

**Honest assessment.** Two new, fully general, fully proved elementary lemmas (Keep-Top Bound; the
exact `q=3` dichotomy identity) genuinely narrow and sharpen the base case's content — it is now
precisely equivalent to "DELETE beats KEEP in `A_{3,k^*}`'s own decomposition," with one concrete,
non-trivial forced consequence (`D_{k^*}>b_0`) available if a future attempt assumes the negation
for contradiction — but **the base case itself is NOT proved this round.** The dispatch's requested
priority ordering (base case before any inductive-step work) is respected: no inductive-step content
was attempted. This is genuine, precisely-scoped partial progress on a lemma that had zero proof
attempts on file before this round, not a closure.

#### 24.4 Item 4 — Background-Release Domination Lemma: STRENGTHENED to an unconditional statement,
ready to certify

**Finding: §23.2's stated form (with the `\min(\cdot,e(C))` hedge) is not tight — the lemma holds in
a cleaner, fully unconditional form, with a one-line proof.**

**Lemma (Background-Release Domination, STRENGTHENED).** For any background `C` (`|C|\ge1`), list
`W`, and any `y\in C` (`C':=C\setminus\{y\}`):
```
OPT_{+1}(C,W)  >=  OPT_{+1}(C', W u {y})          (and the sigma=-1 dual: OPT_{-1}(C,W) <= OPT_{-1}(C', W u {y})).
```
No `\min`/`\max` with `e(C)` is needed.

*Proof.* Every selection of `W` (with background `C` fixed) corresponds, under "`y` is *forced* to
be kept," to exactly one selection of `W\cup\{y\}$ with background `C'=C\setminus\{y\}` (the same
`\mathrm{K}/\mathrm{D}/\mathrm{M}` choices on `W`, plus `y\in K`) with the *identical* resulting
value `e(C\cup(\text{selection of }W))=e(C'\cup\{y\}\cup(\text{selection of }W))`. So
`\mathrm{OPT}_{+1}(C,W)$ equals the `\sigma=+1`-optimum restricted to the sub-space of
`\mathrm{OPT}_{+1}(C',W\cup\{y\})`'s own (strictly larger — `y` may now also be deleted or matched)
search space where `y$ is kept. Minimizing over a subset can only give a value `\ge` minimizing over
the full space, so `\mathrm{OPT}_{+1}(C,W)\ge\mathrm{OPT}_{+1}(C',W\cup\{y\})`. The `\sigma=-1` case
is identical (maximizing over a subset gives a value `\le` maximizing over the full space).
`\blacksquare` (This is the same search-space-inclusion proof shape as the already-certified
Shrink-List Monotonicity Lemma, applied to "releasing" a background element into the free list
instead of "shrinking" the free list.)

**Independently confirmed computationally, fresh code, this round:** `\sigma=+1`: `0/18{,}000`
violations of the strengthened (uncapped) form (`|C|=1$–`4`, `|W|=0$–`4`, `v_{\max}\in\{1,2,3,5,8,
12\}`); `\sigma=-1$ dual: `0/18{,}000`. Also independently reconfirmed the original (weaker, capped)
form from §23.2, `0/7500` — consistent, since the strengthened form trivially implies the capped one
(`\min(X,e(C))\le X\le` the true value whenever `X\le` the true value).

**Consequence for §23.2's dead-end diagnosis (unchanged, re-confirmed, not rescued).** The
strengthening does **not** revive either of §23.2's refuted chaining routes: route (a) (full
telescoping to `C=\emptyset`) still degenerates to the trivial bound `\mathrm{OPT}_{+1}(\emptyset,
\cdot)=0$ (Empty-Background Lemma) regardless of which form of the per-step inequality is used — the
information loss is inherent to releasing *all* background structure at once, not an artifact of the
old form's `\min`-with-`e(C)` cap. Route (b) (single-release direct chain against `A_1`) is a
different, unrelated (and separately, still correctly refuted) claim. **Recommendation: certify the
STRENGTHENED (uncapped) form above as `lemmas/background-release-domination.md`** — strictly more
general and more useful than what §23.2 originally proposed, same proof effort, no downside.

#### 24.5 Summary and update to the recommended build order

**Net effect on the open-gap list, per this round's findings:**
1. **The half-step lemma's hypothesis is simplified** (§24.1) — drop the "true-argmin-descended at
   every deeper level" requirement; only the base generator's own top-level `\mathcal F`-provenance
   (genuine trigger + genuine global `k^*`) is needed. The half-step itself remains open, but a
   future strong-induction-on-`|X|` attempt no longer needs to track which partner is locally
   optimal at each step — a genuine simplification of the proof's own bookkeeping burden.
2. **`q=4`'s MATCH branch needs the generalized `A_1`-bound family** (§24.2) — corrects the build
   order; this piece of work cannot be deferred to `q\ge5`. One candidate direction for that family
   ("keep both `\mathrm{Res}` elements") is now proved to be permanently useless (Three-Bound
   Domination Lemma, §24.2) — narrows the search for the correct generalization to bounds that
   capture *internal cancellation* inside `A_1`'s own search space (Lemma-P/duplicate-style), not
   more "delete-all-but-one" variants.
3. **Gap 1b's base case is reduced to an exact dichotomy** (§24.3) — "DELETE beats KEEP in
   `A_{3,k^*}`'s own top-level decomposition" — with one concrete forced consequence
   (`D_{k^*}>b_0$ if the target fails) available as a contradiction-argument starting point, but
   **not yet closed.**
4. **Background-Release Domination Lemma is strengthened and ready to certify** (§24.4).

**None of Gaps 1a, 1b, 1c is closed this round — Status correctly stays `partial`.** This round's
value is entirely in (a) resolving a genuine cross-round discrepancy in favor of a *simpler* target
(item 1 — arguably the highest-leverage outcome, since it removes bookkeeping from every future
attempt at the half-step), (b) precisely correcting a build-order assumption before a future builder
wastes effort assuming `q=4` is free (item 2), (c) turning a completely unattempted lemma into a
precisely-reduced, partially-attacked one with two new proved general facts (item 3), and (d) one
more certifiable general lemma in strengthened form (item 4).

**Recommended build order for the next round (revises §23.4):**
1. **Gap 1b's base case** (§24.3) — now precisely reduced to "rule out `M=w_1-D_{k^*}` (KEEP wins)";
   the `D_{k^*}>b_0` forced-consequence chain and the (unreconciled) global-argmin-at-`l'` chain are
   the two concrete threads to pursue; still the field's least-explored high-value target.
2. **The half-step lemma**, now at its simplified scope (§24.1) — attempt the strong induction on
   `|X|` with the lighter bookkeeping burden; this closes (most of) Gap 1a's `q\ge5` MATCH branch and
   the retargeted form of Gap 1c together, per §23.1's already-established reduction.
3. **The generalized `A_1`-bound family**, now confirmed needed starting at `q=4`'s MATCH branch
   (§24.2) — the concrete next construction should look for a bound capturing internal
   duplicate/matching cancellation within `A_1`'s own search space (not more delete-all-but-one
   variants, which are exhausted/dominated per the Three-Bound Domination Lemma).
4. Certify the strengthened Background-Release Domination Lemma (§24.4) — cheap, whenever
   convenient.
5. Only after 1–3: the `\sigma=-1` mirrors, as in §23.4's original items 5–7.

### 25. Round 16 outliner revision — Gap 1b's base case is now a genuine, independently re-verified
**PROOF** (not merely a reduction), and Gaps 1a/1c both get concrete, buildable construction targets
(a provable Two-Touch Lemma for Gap 1a's `A_1`-bound family; a provable Rank-Extraction closure of the
half-step's Step-3 nearest-neighbor construction for Gap 1c) — **this is the highest-confidence single
round of the whole SAR effort to date; recommend committing full build budget to these three items,
in the priority order below, before anything else.**

**Provenance.** Three round-16 explorers scouted Gap 1a (`math-explorer-gap1a-A1bound.md`), Gap 1b
(`math-explorer-gap1b-basecase.md`), and Gap 1c (`math-explorer-gap1c-halfstep.md`) directly. This
section independently re-verifies all three claims with **fresh, from-scratch code** (not reusing any
explorer's harness — `/tmp/round-16/verify/`, validated against the file's own four worked examples
first, all reproduced exactly) before committing them to the build plan, per the dispatch's explicit
instruction to check carefully rather than trust the explorers' own numbers. **No new slug is opened —
all three items are sub-goals of the single existing `potential-weighting-upper-bound` route (Claim A
via the Non-Matching-Witness Criterion, §17.4/§17.5), per CLAUDE.md's single-gap-trap warning.**

#### 25.1 Gap 1b's base case (`\mathrm{rest}=\emptyset`) — a complete, elementary proof
(**PRIORITY BUILD TARGET 1 — write up and certify this round**)

**Independent re-verification performed (outliner's own code, `/tmp/round-16/verify/gap1b.py`, brute-
force `\mathrm{OPT}_\sigma` via the raw DELETE/KEEP/MATCH definition, not the closed-form dichotomy):**
built genuine `q=3` base generators (`b_0`, sorted `Z_0`), computed `A_1`, `A_{3,l}` for both
`l\in\{2,3\}`, filtered to genuine trigger (`M<A_1`) and `h=0$ at the argmin `k^*`: **`1{,}541` genuine
triggered `h=0` instances found in `20{,}000` raw random trials (mixed integer/rational alphabets up to
`v_{\max}=30`), `w_1\ge2D_{k^*}` (equivalently `M=D_{k^*}`) held in every single one, `0` violations** —
independently reproduces the explorer's own `905/905` from a differently-coded harness. **Re-derived
the proof itself by hand, line by line, before trusting the computation:**

> **Lemma (Sum-Bound Base Case).** At a genuine `q=3` base-generator instance with trigger `M<A_1` and
> `h=0` at the argmin `k^*` (i.e. `b_0<w_1` and `d_{k^*}<w_1`, `w_1:=` the sole element of `Z_1`),
> `M=D_{k^*}$ exactly (DELETE beats or ties KEEP), equivalently `w_1\ge2D_{k^*}`.
>
> *Proof.* By the certified exact `q=3` dichotomy (`lemmas/three-bound-domination-and-keep-top-bound.md`),
> `M=\min(D_{k^*},w_1-D_{k^*})`. Suppose for contradiction `M=w_1-D_{k^*}<D_{k^*}` (i.e. `2D_{k^*}>w_1`).
> Two unconditional bounds on `A_1` (both free — the first is the Shrink-List Corollary, the second is
> Step 1 (†) of §21.1 instantiated at `w_1`'s own index):
> ```
> A_1 <= b_0            (delete both elements of Z_0\{z_1})
> A_1 <= w_1 - b_0       (keep w_1, delete z_{k*}; uses b_0 < w_1 from h=0)
> ```
> Combining the trigger `M<A_1` with each bound in turn:
> ```
> w_1 - D_{k*} < A_1 <= b_0            =>  w_1 < D_{k*} + b_0                  ... (i)
> w_1 - D_{k*} < A_1 <= w_1 - b_0      =>  D_{k*} > b_0                        ... (ii)
> ```
> From (ii), `D_{k^*}=|b_0-d_{k^*}|>b_0\ge0` forces `d_{k^*}>b_0` (else `D_{k^*}=b_0-d_{k^*}\le b_0`,
> contradicting (ii)), so `D_{k^*}=d_{k^*}-b_0`. Substituting into (i): `w_1<(d_{k^*}-b_0)+b_0=d_{k^*}`.
> But `h=0` requires `d_{k^*}<w_1` — so `w_1<d_{k^*}<w_1`, a direct contradiction. Hence `2D_{k^*}\le
> w_1`, i.e. `M=D_{k^*}$. `\blacksquare`

**This proof is airtight — no gap found on independent re-derivation.** It is a ~10-line contradiction
argument using only: the certified exact `q=3` dichotomy, the certified Shrink-List Corollary, the
already-on-file Step-1(†) bound, and elementary algebra on absolute values — no new machinery, no
computation needed to trust it (the `1{,}541`-instance sweep above is corroboration on top of a genuine
proof, not a substitute for one). **Tightness confirmed independently:** at the boundary `2D_{k^*}=
w_1`, `\min(D_{k^*},w_1-D_{k^*})=w_1/2$, while `\min(b_0,w_1-b_0)\le w_1/2` always (one of `b_0,w_1-b_0`
is `\le w_1/2`) — so the hypothesis `M<A_1\le\min(b_0,w_1-b_0)` is automatically vacuous exactly at the
boundary, which is why the conclusion is the tight, non-strict `\le` matching the dichotomy's own
convention (matches the previously-found exact-equality witnesses, e.g. round 15's `KEEP=DEL` finite
instance — this is not a coincidence, it is the proof's own tightness mechanism).

**Scope — do NOT overclaim.** This closes ONLY the base case `\mathrm{rest}=\emptyset` (`|Z_1|=1`,
`q=3`) of the general Sum Bound. **The general recursion-depth induction for arbitrary `|\mathrm{rest}|`
(§23.3) is a separate, much larger, still fully-open task** — its own three named bookkeeping
subtleties (argmin-tie branch filtering, continuous zero-slope tie intervals, the killed
`\max(\mathrm{rest})` shortcut) are untouched by this proof. A builder must state the result as "Sum
Bound: PROVED at `|Z_1|=1$; open for `|Z_1|\ge2`," not "Sum Bound: proved."

**Build task:** write this proof up formally (trivial — the proof above is already complete and
publication-ready), confirm the two cited inputs (Shrink-List Corollary, Step-1(†), the exact `q=3`
dichotomy) are correctly invoked with no silent extra hypothesis, and **certify as a new standalone
lemma `lemmas/sum-bound-base-case.md`**. This is the lowest-risk, highest-confidence build item in the
population this round.

#### 25.2 Gap 1a — the Single-Background Two-Touch Lemma: a provable-looking conjecture giving an
exact closed form for `A_1` (**PRIORITY BUILD TARGET 3**)

**Independent re-verification (outliner's own code, `/tmp/round-16/verify/gap1a_twotouch.py` and
`twotouch_c2.py`):**
```
Two-Touch (|C|=1): OPT_{+1}({b_0},W) = min( e({b_0}), min_w e({b_0,w}), min_{i<j} e({b_0,|w_i-w_j|}) )
```
`0/4000` violations (`|W|\in\{2,\dots,6\}`, mixed alphabets) — reproduces the explorer's finding on a
fresh harness. **The `|C|=2` boundary dead end is also independently reproduced exactly:** testing the
analogous "touch `\le2`" formula against `\mathrm{OPT}_{+1}(C,W)` for `|C|=2` gives `357/1500`
(`23.8\%`) violations — matches the explorer's reported `24\%` almost exactly, confirming this is a
genuine structural boundary (background size `2` needs strictly more touches), **not** a mechanism to
port to `A_{3,l}` or the half-step lemma.

**What this gives, precisely, if proved:** an exact, `O(q^2)`-term closed form for `A_1` at every `q`,
resolving the "generalized `A_1`-bound family" search (open since round 15's §23.4 item 4, needed
starting at `q=4$'s MATCH branch per §24.2) — turns an open-ended search for a sufficient bound family
into "plug in the exact value."

**What this does NOT give — critical, do not let a builder overclaim:** proving Two-Touch alone does
**not** close the general-`q` Per-Partner Domination Lemma (`A_{3,l}\ge\min(A_1,D_l)`). `A_{3,l}$'s own
recursive DELETE/KEEP/MATCH peeling over `\mathrm{Res}` (`q-2` elements) still needs its own per-`q`
case analysis (exactly as the certified `q=3` proof, §22.2, already does) — Two-Touch only removes the
opacity of `A_1` as an input to that case analysis, replacing an "opaque recursive quantity" with an
explicit expression. Two builders' tasks remain logically separate: (1) prove Two-Touch; (2) redo the
`q=3`-style case analysis at general `q` using the now-explicit `A_1`. Do not claim (2) is free once (1)
closes.

**Recommended proof route (the explorer's own pointer, confirmed structurally sound on inspection): 
strong induction on `|W|`.**
  - **Base case `|W|=2`:** this is *exactly* the already-**certified** Three-Bound Domination Lemma
    (`lemmas/three-bound-domination-and-keep-top-bound.md`), read as an inequality
    `\min(x,|x-y|,|x-z|)\le e_{\mathrm{sorted}}(\{x,y,z\})` — i.e. "keep both remaining elements is
    dominated by touch-`\le1`" — already proved, reusable directly.
  - **Inductive step:** peel `W`'s top element via the certified Generalized Multi-Background Peeling
    Lemma's own DELETE/KEEP/MATCH trichotomy; show any selection touching `k\ge3` elements is always
    dominated by a strictly-fewer-touch alternative, using repeated Three-Bound-Domination-style triple
    collapses (the same case-split shape that already closed the `q=3` Per-Partner Domination proof, one
    level of induction further) plus the General Rank-Extraction Identity for handling insertion
    position. **Not yet attempted — this is the open gap**, but the induction skeleton, base case, and
    tools are all already in hand; this looks like the population's most tractable open lemma right now
    after Gap 1b's base case.

**Watch out for:** do NOT attempt to port Two-Touch (or any "touch `\le k`" formula for a fixed small
`k`) to `|C|=2` (confirmed dead, `\ge23\%` failure, independently reconfirmed this round) — the
half-step lemma (`|C|=2$, Gap 1c) needs its own argument, not this one; do NOT treat a proof of
Two-Touch as closing Gap 1a's general-`q` induction by itself (see above).

#### 25.3 Gap 1c — the half-step lemma's Step-3 nearest-neighbor construction: a concrete algebraic
target using an independently-verified general identity (**PRIORITY BUILD TARGET 2**)

**Independent re-verification of the reusable identity (outliner's own code,
`/tmp/round-16/verify/rankextract.py`, fully general, no `\mathcal F`-provenance):**
```
e(M u {d}) - e(M) = (-1)^h * (d - 2*e(tail_d)),   h := #{m in M : m>d}, tail_d := {m in M : m<=d}
```
`0/3000` violations across arbitrary `(M,d)` (`|M|\le6`, mixed alphabets) — this is a **clean, fully
proved, general fact** (an elementary consequence of the alternating-sum structure of `e_{\mathrm{sorted}}`
under single-element insertion), independently reproduced from scratch. **Recommend certifying this
outright as a standalone lemma** (e.g. `lemmas/insertion-difference-identity.md`) **regardless of
whether Step 3 below closes** — it is reusable machinery, not a Gap-1c-specific artifact (it is already
used twice: once for the now-confirmed-dead Step-2 naive-transfer attempt, and it is the natural tool
for Step 3's residual algebra below).

**The half-step lemma, at its round-15-simplified scope (§24.1):**
```
OPT_{+1}(B_1 u {d}, X)  >=  OPT_{+1}(B_1, X),   d = u_1 - u_j for the peeled top element u_1 of Res
  and any partner u_j, X = Res\{u_1,u_j}, given genuine top-level F-provenance (trigger + true global k*).
```
**Dead end, reconfirmed — do not re-attempt:** the naive "same witness, just drop `d`" transfer (let
`\xi^*` be the LHS-optimal selection of `X`, try to show `e(B_1\cup\xi^*)` alone suffices) is FALSE — the
explorer found a concrete counterexample via the identity above (inserting `d` into `M:=B_1\cup\xi^*`
can *decrease* `e`, i.e. `\mathrm{tail}_d`'s value can make the sign-flip term negative). This confirms
the half-step is genuinely non-trivial, not a one-liner.

**The working (not yet proved, but concretely specified) construction — Step 3, "extremal witness +
secondary tie-break + local rewrite" (the crux-inspired shape flagged since round 13, finally
instantiated this round):**
```
Let c := argmin_{x in xi*} |x-d|  (the LHS-optimal-witness element closest to d).
Conjecture: e(B_1 u (xi* \ {c}))  <=  OPT_{+1}(B_1 u {d}, X).
```
Given this, the half-step follows in 3 lines: `\mathrm{OPT}_{+1}(B_1,X)\le e(B_1\cup(\xi^*\setminus
\{c\}))\le\mathrm{OPT}_{+1}(B_1\cup\{d\},X)` (first inequality: `\xi^*\setminus\{c\}` realized as an
`X`-selection, trivially upper-bounds the true `B_1`-optimum; second: the conjecture). **Corroborated
`0` violations across `1{,}267` combined checks (generic-large-value, duplicate-heavy, and an explicit
"does the nearest choice matter" exhaustiveness check ruling out that any single drop works) — not yet
independently re-verified by the outliner this round (time budget went to the other two items), flagged
for the builder's OWN first task: re-verify this construction fresh before building on it, per the
standing population rule to re-run a sole-load-bearing computational claim independently before
extending it (round 10's lesson).**

**Recommended proof route for Step 3 (the explorer's own pointer, algebraically concrete, not a
search):** apply the same insertion-difference identity, but comparing `e(B_1\cup(\xi^*\setminus
\{c\})\cup\{d\})` (a re-arrangement of the *same* multiset as `B_1\cup\{d\}\cup\xi^*`, with `c`
"extracted" instead of `d` staying in) against `e(B_1\cup(\xi^*\setminus\{c\}))` — i.e. insert `d` into
`M':=B_1\cup(\xi^*\setminus\{c\})` and show the resulting sign-flip term is favorable *because* `c` was
chosen nearest to `d` (this should directly control `\mathrm{tail}_d`'s value in the identity above,
using `|c-d|\le|x-d|` for every `x\in\xi^*`). **This is the open gap — a genuinely tractable algebra
task given the identity is already proved, not a fresh search.**

**Watch out for:** do NOT weaken the half-step's tested scope below "genuine top-level `\mathcal
F`-provenance" (round 15's simplification is correct and should be used, but the top-level trigger+
global-`k^*` requirement is still load-bearing, per round 15's own negative controls); do NOT resurrect
Step 2's naive witness-reuse; the equality set (margin `=0`) is exactly the duplicate/coincidence
configurations (Lemma-P-style) per the explorer's Step 1 finding — a case-split proof (generic vs.
duplicate case) is a reasonable fallback if the direct algebraic route stalls.

#### 25.4 Recommended build order this round

1. **Gap 1b's base case (§25.1)** — write up and certify `lemmas/sum-bound-base-case.md`. Essentially
   zero proof risk (independently re-derived and re-verified by the outliner); do this first, it is
   nearly free.
2. **Gap 1c's Step-3 construction lemma (§25.3)** — the algebraic closure using the (also-certifiable)
   insertion-difference identity; highest-leverage open item (closes the retargeted Gap 1c and, per
   §23.1's already-established reduction, most of Gap 1a's `q\ge5` MATCH branch). Re-verify the
   1,267-check corroboration independently FIRST (cheap), then attempt the algebra.
3. **Gap 1a's Two-Touch Lemma (§25.2)** — prove via induction on `|W|`, base case already certified
   (Three-Bound Domination). If proved, immediately re-attempt the `q=4` MATCH branch closure (§24.2)
   using the explicit formula, and note (do not silently skip) that the general-`q` Per-Partner
   Domination induction still needs its own per-`q` case analysis on top.
4. If time remains: attempt Gap 1b's inductive step (recursion-depth induction, general
   `|\mathrm{rest}|`, §23.3) — now anchored by a real base case, but still a large, separate task with
   three named bookkeeping subtleties; lower priority than 1-3 this round.
5. Certify the strengthened Background-Release Domination Lemma (§24.4) if not already done — cheap,
   whenever convenient, does not block anything above.
6. Only after 1-4: the `\sigma=-1` mirrors (Sum Bound, half-step).

**Watch out for (all three items, summary):** (i) Gap 1b's base-case closure is scoped to
`\mathrm{rest}=\emptyset` ONLY — do not report "Sum Bound proved" without qualification; (ii) Two-Touch,
even if proved, does not by itself close Gap 1a's general-`q` induction — the per-`q` case analysis on
`A_{3,l}$'s own recursion is separate, still-needed work; (iii) do not port Two-Touch to `|C|=2`
(re-confirmed dead, `23.8\%` failure); (iv) do not resurrect the half-step's Step-2 naive witness-reuse
(confirmed dead); (v) the half-step's Step-3 construction is corroborated but NOT yet independently
re-verified by anyone besides its discovering explorer this round — the builder's first move should be
a quick independent re-run of that specific check before spending build time on its algebraic proof.

**Independent verification summary performed by the outliner this round (fresh code,
`/tmp/round-16/verify/`, all validated against the file's own four worked examples first):** Gap 1b
pure algebra + game-level base case: `0/1{,}541` genuine triggered `h=0` instances (own harness, brute-
force `\mathrm{OPT}_\sigma`, not reusing the explorer's code) — proof independently re-derived by hand,
no gap found. Gap 1a Two-Touch (`|C|=1`): `0/4{,}000`. Gap 1a Two-Touch `|C|=2` boundary dead end:
`357/1{,}500` (`23.8\%`), matches the explorer's `24\%`. Gap 1c insertion-difference identity: `0/3{,}000`.
No overclaim found in any of the three explorer reports — all appropriately distinguish "proved" (Gap
1b's base case, upgraded this round from "corroborated" to "proved" by the outliner's own re-derivation)
from "corroborated, not proved" (Gap 1a's Two-Touch, Gap 1c's Step-3 construction).

### 26. Round 16 build — Sum-Bound Base Case Lemma and Insertion-Difference Identity CERTIFIED; a new
conditional resolution of Gap 1c's `\xi^*=\emptyset` boundary case; substantial (but incomplete)
progress on Gap 1a's Two-Touch induction, with the exact two remaining sub-lemmas isolated

This round executes the outline-reviewer's approved build order in full. **Items 1 and 2 are complete,
certified lemmas, re-verified by this builder with fresh code independent of the outliner's and
outline-reviewer's own harnesses** (`/tmp/round-16/verify_builder/`). **Item 3 (Gap 1c's `\xi^*`
well-definedness gap) is genuinely advanced**: the previously-undefined `\xi^*=\emptyset` boundary case
is now fully resolved, **conditional on Gap 1a's already-partially-proved Step 2** (Deletion-Suffices-
for-`k^*`), via a new certified general lemma; the well-definedness of `\xi^*` itself is pinned down by
a canonical-choice convention. The nonempty-`\xi^*` case (Step 3's actual nearest-neighbor construction)
remains open — attempted, not closed; the point where the algebra stalls is reported precisely. **Item 4
(Two-Touch)** is attempted with real effort (not merely noted) since time remained: three of its five
structural sub-pieces (base case, DELETE branch, KEEP branch's `b_0>w_1` sub-case) are now **fully
proved**; the remaining two (KEEP branch's `b_0\le w_1` sub-case; MATCH branch) are precisely
re-diagnosed — the naive "generalize Two-Touch to `|C|=2`" route is confirmed dead (as already known),
but a much narrower, still-open, strongly-corroborated **sub-claim** is identified as the actual missing
piece, a genuinely more tractable target than the false general `|C|=2` formula. **None of Gaps 1a, 1b
(general induction), 1c is fully closed this round — Status correctly stays `partial`.**

#### 26.1 Sum-Bound Base Case Lemma — CERTIFIED

Written up and certified verbatim as `lemmas/sum-bound-base-case.md` (full statement, proof, tightness
argument, scope note reproduced there — not repeated here). **Wording fix applied per the
outline-reviewer's flag**: the lemma's Ingredient 1 (dichotomy `M=\min(D_{k^*},w_1-D_{k^*})`) is cited
explicitly as "singleton-list dichotomy (a trivial enumeration fact: a 1-element residual list has
exactly two selections) + the certified Keep-Top Bound (`lemmas/three-bound-domination-and-keep-
top-bound.md`), combined" — **not** as if it were itself a pre-existing standalone certified lemma (the
`three-bound-domination-and-keep-top-bound.md` file explicitly declined to certify this exact identity
on its own, "too narrow"). This matches the outline-reviewer's exact recommendation.

**Independent re-verification performed by this builder (fresh code, not reusing the outliner's or
outline-reviewer's harnesses, `/tmp/round-16/verify_builder/`):**
- **Isolated pure-algebraic core** (`pure_algebra.py`): `65{,}403` filtered random trials (`0`
  violations), plus a dedicated boundary sweep (`14{,}439` trials forced onto `2D_{k^*}=w_1$ exactly,
  `0` cases where the hypothesis held — confirming the tightness argument's claim that the hypothesis
  is automatically vacuous there).
- **Full game-level statement** (`gap1b_check.py`, independently-coded brute-force `\mathrm{OPT}_{+1}`
  via complete enumeration of every Keep/Delete/Match selection — not the closed-form dichotomy): `2{,}976`
  genuine triggered `h=0` instances out of `29{,}126` raw random trials, **`0` violations** of `M=D_{k^*}`,
  and `0` mismatches between the brute-force `M` and the dichotomy formula (an independent sanity check
  on Ingredient 1's correctness).

**This is now the population's third independent confirmation** (round-16 explorer, round-16
outline-reviewer, round-16 builder), all from differently-coded harnesses, with the underlying `\sim10`-
line contradiction proof independently re-derived by hand by all three agents with no discrepancy.
**Scope, restated precisely (per the standing "watch out for" warning, do not drop this qualifier):**
this closes ONLY the base case `\mathrm{rest}=\emptyset` (`|Z_1|=1$, `q=3`) of the Sum Bound. The
general recursion-depth induction (`|Z_1|\ge2`) remains fully open, untouched by this result.

#### 26.2 Insertion-Difference Identity — CERTIFIED

Written up and certified verbatim as `lemmas/insertion-difference-identity.md`. **Proof route used
(self-contained, cited exactly): two certified ingredients only — Fact 3 (block extraction,
`lemmas/insertion-and-cascade-facts.md`) and the General Rank-Extraction Identity
(`lemmas/general-rank-extraction-identity.md`)** — split `M=\mathrm{head}_d\sqcup\mathrm{tail}_d` via
Fact 3 to get `e(M)=e(\mathrm{head}_d)+(-1)^h e(\mathrm{tail}_d)`, extract `d` from `M\cup\{d\}` at its
sorted rank `r=h+1` via the General Rank-Extraction Identity to get
`e(M\cup\{d\})=e(\mathrm{head}_d)+(-1)^h d+(-1)^{h+1}e(\mathrm{tail}_d)`, then eliminate
`e(\mathrm{head}_d)$ between the two equations. Full derivation on file in the lemma. This is a
different, independently-re-derived route from the outliner's own (which cited an already-embedded
step of Fact 4's own proof) — both routes agree, cross-validating the identity via two distinct
argument shapes.

**Independent re-verification performed by this builder (fresh code, `insertion_diff.py`):** `0/20{,}000`
random trials (`|M|\in\{0,\dots,7\}`, mixed-denominator rationals up to `v_{\max}=200`) **and** `0/780`
in a genuinely **exhaustive** small-value grid sweep (`|M|\le3`, all `M,d` from a 5-value grid including
`\tfrac12,\tfrac32`, every combination — deliberately stresses ties/coincidences, not just generic
values). This is the population's **third** independent confirmation (explorer, outline-reviewer,
builder), all `0` violations.

#### 26.3 Gap 1c's `\xi^*=\emptyset` boundary case — RESOLVED, conditional on Gap 1a's Step 2

**The precise well-definedness gap, restated (per the outline-reviewer's flag).** The half-step's Step-3
construction needs `c:=\mathrm{argmin}_{x\in\xi^*}|x-d|` for `\xi^*$ "the LHS-optimal witness" of
`\mathrm{OPT}_{+1}(B_1\cup\{d\},X)` — but `\xi^*` is frequently **not uniquely determined**, and in
particular the empty selection (`\xi^*=\emptyset`, "delete everything") is very often one of the
optimal witnesses (independently reconfirmed by this builder: **`720/1{,}813`** genuine partner-pair
checks at top-level `\mathcal F`-provenance instances, `q\in\{4,5,6\}`, have `\emptyset` among the
optimal witnesses — `/tmp/round-16/verify_builder/gap1c_explore.py`), in which case `c` is literally
undefined (empty set has no argmin).

**Fix — canonical choice.** Define `\xi^*` as: **a nonempty optimal witness if one exists among the
optima; the empty witness `\emptyset` only if it is the UNIQUE optimum.** This makes the half-step's
construction well-defined in every case: either a genuine nonempty `\xi^*` exists (Step 3's
nearest-neighbor construction applies, still open — see §26.4 below) or `\emptyset` is forced (handled
directly below, now fully resolved subject to one named open dependency).

**The `\xi^*=\emptyset$-forced sub-case — new proof, conditional on Gap 1a's Step 2.** Suppose
`\emptyset` is the *unique* optimum of `\mathrm{OPT}_{+1}(B_1\cup\{d\},X)`, i.e.
`\mathrm{OPT}_{+1}(B_1\cup\{d\},X)=e(B_1\cup\{d\})`. The chain
```
OPT_{+1}(B_1,X) <= e(B_1)                                    [Shrink-List Corollary, delete all of X]
           <= e(B_1 u {d})                                    [*]
            = OPT_{+1}(B_1 u {d}, X)                          [xi*=emptyset is the true optimum]
```
gives the half-step (`\mathrm{OPT}_{+1}(B_1,X)\le\mathrm{OPT}_{+1}(B_1\cup\{d\},X)`) directly, **provided
step `[*]` (`e(B_1)\le e(B_1\cup\{d\})`) holds.**

**Step `[*]` is proved via a new general lemma, `lemmas/delete-suffices-insertion-domination.md`
(CERTIFIED this round, fully general, no `\mathcal F`-provenance needed): if `\mathrm{OPT}_{+1}(C,W)=
e(C)$ (deletion suffices at a node), then `e(C)\le e(C\cup\{|w_a-w_b|\})` for any two elements
`w_a,w_b\in W`.** (Two-line proof: "match `w_a,w_b`, delete the rest" is one candidate for
`\mathrm{OPT}_{+1}(C,W)`'s own minimization, with value `e(C\cup\{|w_a-w_b|\})`; since `\mathrm{OPT}_{+1}
(C,W)$ is the true minimum and equals `e(C)` by hypothesis, `e(C)\le e(C\cup\{|w_a-w_b|\})`.)

Applying this with `C=B_1`, `W=\mathrm{Res}`, `w_a=u_1$, `w_b=u_j` (so `|w_a-w_b|=d`): step `[*]` holds
**exactly when `\mathrm{OPT}_{+1}(B_1,\mathrm{Res})=e(B_1)`** — i.e. exactly when **Deletion-Suffices-
for-`k^*`** (Gap 1a's own Step 2, `\S21.1`, already proved for `q\le3` by the round-14 builder, open for
`q\ge4`) holds at this node. **This is a genuine, previously unnoticed structural link between Gap 1a's
Step 2 and Gap 1c's `\xi^*=\emptyset` boundary case**: a future proof of Deletion-Suffices-for-`k^*` at
general `q` would, via this reduction, **also retire the `\xi^*=\emptyset` sub-case of Gap 1c's
half-step**, with zero extra work.

**Independent computational corroboration (this round, fresh code):**
- `gap1c_explore2.py`: at top-level genuine `\mathcal F`-provenance instances where `\emptyset` is the
  UNIQUE optimum of the LHS problem (`759` such instances out of `2{,}968` partner-pair checks,
  `q\in\{4,\dots,7\}`), step `[*]` (`e(B_1)\le e(B_1\cup\{d\})`) holds in **all `759/759`**, strictly in
  every case (`0` ties, `0` failures).
- `gap1c_reduction.py`: in the same instance family (`1{,}304` genuine trigger+global-`k^*` instances,
  `q\in\{4,\dots,8\}`), `M=D_{k^*}` (Deletion-Suffices-for-`k^*`) holds in **all `1{,}304/1{,}304`** —
  consistent with (not a proof of) the general-`q` conjecture, matching round 14's own corroboration.
- `delete_suffices_corollary.py`: the new general lemma itself, `\mathcal F$-provenance-free, `0/1{,}615`
  genuine "deletion-suffices" nodes tested (arbitrary `C,W`), `0` violations; negative control
  (dropping the hypothesis) gives `11{,}376/50{,}000$ (`\approx23\%`) failures, confirming the hypothesis
  is load-bearing.
- `gap1c_diag.py`: as an extra sanity check, the underlying free inequality `M\le e(B_1\cup\{d\})` (which
  needs no hypothesis at all — direct from `M`'s own minimality, the "match `u_1,u_j`, delete the rest"
  candidate) was independently confirmed for **every** pair `(u_i,u_j)\in\mathrm{Res}$, not only pairs
  involving `u_1=\max(\mathrm{Res})`: `0/15{,}162` failures.

**Honest scope of this sub-result:** this is a genuine, unconditionally-proved **reduction** (Gap 1a's
Step 2 `\Rightarrow` Gap 1c's `\xi^*=\emptyset` sub-case), not an unconditional closure of the
`\xi^*=\emptyset` sub-case itself — it still depends on Deletion-Suffices-for-`k^*`, proved only for
`q\le3`. At `q\le3` (where Deletion-Suffices-for-`k^*` IS proved), the `\xi^*=\emptyset` sub-case of the
half-step is now **fully, unconditionally closed**. At `q\ge4` it remains conditional on the still-open
general Deletion-Suffices-for-`k^*` conjecture.

#### 26.4 Gap 1c's nonempty-`\xi^*` case (Step 3's construction) — attempted, still open; precise
diagnosis of where the direct algebraic route stalls

**Re-verification of the corroboration (per the outline-reviewer's flagged first task):** confirmed via
this round's own instance generator (`gap1c_explore.py`/`gap1c_explore2.py`) that nonempty optimal
witnesses genuinely occur often (`1{,}174/1{,}813` partner-pair checks have a nonempty optimum among the
LHS optima) — the construction's target regime is real and common, not a corner case.

**Attempted algebraic closure (this round, not completed).** Tried the recommended route: write
`M:=B_1\cup(\xi^*\setminus\{c\})`. The trivial direction `\mathrm{OPT}_{+1}(B_1,X)\le e(M)` is free (`M`
is a valid `X`-selection). The needed direction is `e(M)\le\mathrm{OPT}_{+1}(B_1\cup\{d\},X)=e(M\cup
\{c,d\})`. Two paths were tried:

1. **Optimality of `\xi^*` gives the wrong-direction bound.** Since `\xi^*` is optimal for
   `\mathrm{OPT}_{+1}(B_1\cup\{d\},X)`, and `M=B_1\cup(\xi^*\setminus\{c\})` corresponds to a valid
   *alternative* `X$-selection (`\xi^*\setminus\{c\}`) for the *same* `(B_1\cup\{d\},X)` problem,
   optimality gives `e(M\cup\{d\})\ge e(M\cup\{c,d\})`(`=\mathrm{OPT}_{+1}(B_1\cup\{d\},X)`, since
   `\xi^*` achieves it). This is a genuine, free inequality — but it bounds `e(M\cup\{d\})` from below by
   the target, not `e(M)`; chaining it with the Insertion-Difference Identity's relation between `e(M)`
   and `e(M\cup\{d\})` does **not** close the gap, since the identity's sign term
   `(-1)^h(d-2e(\mathrm{tail}_d))` is not controlled in general (this is exactly why Step 2's naive
   transfer, using the *same* mechanism at `M':=B_1\cup\xi^*`, is confirmed false — the "nearest"
   property of `c` was supposed to fix this, but this particular chaining route doesn't use that
   property at all, so it cannot be the right mechanism).
2. **A two-insertion identity (inserting `c` then `d`, or `d` then `c`, into `M`) was set up** but
   requires controlling the relative sorted ranks of `c` and `d$ *and* their positions relative to `M`
   simultaneously — a genuine 2-variable case split (parity of `h_c`, parity of `h_d'` after `c`'s
   insertion) that was not resolved into a clean sufficient condition within this round's time budget.
   The "closest to `d`" property of `c` should enter via bounding `|c-d|`, but no clean way to convert
   this into control of the relevant `\mathrm{tail}` values was found.

**Status: honestly still open.** Both attempted routes are recorded so the next round does not repeat
them without a genuinely new idea. The explorer's own diagnostic (equality set coincides with
duplicate/coincidence configurations, per `math-explorer-gap1c-halfstep.md` Step 1) remains the most
promising unexploited lead — a case-split proof (generic vs. duplicate case, using Lemma P for the
duplicate case) is the recommended next attempt, not yet tried.

#### 26.5 Gap 1a's Two-Touch Lemma — three of five structural sub-pieces proved; the remaining two
precisely re-diagnosed (lower priority item, attempted since time remained)

**Setup, restated.** `\mathrm{Two}\text{-}\mathrm{Touch}(C,W):=\min\big(e(C),\ \min_{w\in W}e(C\cup
\{w\}),\ \min_{i<j}e(C\cup\{|w_i-w_j|\})\big)`, `C` of size `\le1` (either `\emptyset` or a singleton
`\{b_0\}`). Conjecture: `\mathrm{OPT}_{+1}(C,W)=\mathrm{Two}\text{-}\mathrm{Touch}(C,W)` for every such
`C` and every `W`. The trivial direction `\mathrm{OPT}_{+1}(C,W)\le\mathrm{Two}\text{-}\mathrm{Touch}
(C,W)` is free (every term on the right is a valid candidate selection). The content is the reverse
direction. **This round widens the induction hypothesis from "`|C|=1`" (the outliner's original framing)
to "`|C|\le1`" (both `\emptyset` and singleton backgrounds together) — this widening turns out to be
necessary, not optional, because the peeling recursion's KEEP branch switches background between the two
regimes (see below); this is a genuine correction to the outline's skeleton, worth recording.**

**Strategy: strong induction on `|W|`, peeling `w_1:=\max(W)` via the certified Generalized
Multi-Background Peeling Lemma's DELETE/KEEP/MATCH trichotomy.**

**(a) Base case `|W|\le2` — PROVED.**
- `|W|=0,1`: trivial (the search space has only `1` or `2` selections respectively, all already
  included in `\mathrm{Two}\text{-}\mathrm{Touch}$'s own candidate list).
- `|W|=2`, `C=\{b_0\}`: exactly the certified **Three-Bound Domination Lemma**
  (`lemmas/three-bound-domination-and-keep-top-bound.md`), read as `\min(b_0,|b_0-w_1|,|b_0-w_2|)\le
  e_{\mathrm{sorted}}(\{b_0,w_1,w_2\})` — the "keep both" candidate (the only one not already in
  `\mathrm{Two}\text{-}\mathrm{Touch}$'s list) is dominated. Already used exactly this way in §25.2.
- `|W|=2`, `C=\emptyset`: **trivial, no domination argument needed at all** — for a 2-element sorted
  list `\{w_1,w_2\}$ (`w_1\ge w_2`), `e_{\mathrm{sorted}}(\{w_1,w_2\})=w_1-w_2=|w_1-w_2|`, i.e. the
  "keep both" candidate's value is *identically equal to* the "match" candidate's value — not merely
  dominated by it, literally the same number. So the `C=\emptyset` base case needs no proof beyond this
  one-line observation.

**(b) DELETE branch — PROVED, for every `|W|\ge1`, by induction.** The DELETE branch of peeling `w_1` is
`\mathrm{OPT}_{+1}(C,W\setminus\{w_1\})`, which by the induction hypothesis (applied to the strictly
smaller list `W\setminus\{w_1\}`) equals `\mathrm{Two}\text{-}\mathrm{Touch}(C,W\setminus\{w_1\})`. Since
`\mathrm{Two}\text{-}\mathrm{Touch}(C,W\setminus\{w_1\})`'s candidate list is a **subset** of
`\mathrm{Two}\text{-}\mathrm{Touch}(C,W)`'s own candidate list (every delete/keep/match candidate not
using `w_1` is common to both; `\mathrm{Two}\text{-}\mathrm{Touch}(C,W)$ has strictly more candidates,
namely those additionally involving `w_1`), a minimum over a subset is `\ge` a minimum over the full set:
`\mathrm{Two}\text{-}\mathrm{Touch}(C,W\setminus\{w_1\})\ge\mathrm{Two}\text{-}\mathrm{Touch}(C,W)`.
Hence the DELETE branch `\ge\mathrm{Two}\text{-}\mathrm{Touch}(C,W)`, as needed.

**(c) KEEP branch, `b_0>w_1` sub-case (`C=\{b_0\}`) — PROVED, unconditionally, no induction needed.**
Peeling `w_1` with `b_0>w_1$ (so `b_0`'s rank is `1`, `w_1`'s rank is `2` in `\{b_0,w_1\}\cup
\mathrm{rest}`), the Generalized Multi-Background Peeling Lemma's KEEP-branch formula gives (Rank-
Extraction with `\mathrm{head}=\{b_0\}`, `x=w_1`, `r=2`) KEEP branch `=b_0-w_1+\mathrm{OPT}_{+1}(
\emptyset,\mathrm{rest})` where `\mathrm{rest}:=W\setminus\{w_1\}`. By the already-**certified**
**Empty-Background Lemma** (`lemmas/empty-background-and-background-splitting.md`, Statement 1),
`\mathrm{OPT}_{+1}(\emptyset,\mathrm{rest})=0` unconditionally (no induction, no hypothesis on `\mathrm{
rest}`). So KEEP branch `=b_0-w_1=|b_0-w_1|$ exactly (since `b_0>w_1`) `=e(\{b_0,w_1\})` — **this is
literally the "keep single `w_1`" candidate value, one of `\mathrm{Two}\text{-}\mathrm{Touch}(C,W)`'s own
terms**, so KEEP branch `\ge\mathrm{Two}\text{-}\mathrm{Touch}(C,W)` trivially, by definition of the
minimum. No induction hypothesis or further argument needed for this sub-case.

**(d) KEEP branch, `b_0\le w_1` sub-case — OPEN.** Here `w_1`'s rank is `1`, `b_0`'s rank is `2`, giving
KEEP branch `=w_1-\mathrm{OPT}_{-1}(\{b_0\},\mathrm{rest})` (the recursive sub-problem keeps the SAME
singleton background `\{b_0\}`, but flips to the `\sigma=-1$ (maximization) mirror problem — this is why
a `\sigma=-1` mirror bound on `\mathrm{Two}\text{-}\mathrm{Touch}` is needed here, not present anywhere
else in the induction). To show KEEP branch `\ge\mathrm{Two}\text{-}\mathrm{Touch}(\{b_0\},W)`, an upper
bound on `\mathrm{OPT}_{-1}(\{b_0\},\mathrm{rest})$ is needed — the `\sigma=-1` mirror of Two-Touch
itself (queued, "not yet even formulated" per §21.2), genuinely a separate piece of work. **Strongly
corroborated, not proved:** independently checked (`twotouch_keepbranch.py`) that the KEEP-branch
closed-form formula above is exactly correct (`0/2{,}182` formula mismatches against direct brute-force
`\mathrm{OPT}_{+1}(\{b_0,w_1\},\mathrm{rest})$, i.e. "`w_1` forced kept") and that it never beats
`\mathrm{Two}\text{-}\mathrm{Touch}` (`0/2{,}182` domination failures) — but no proof.

**(e) MATCH branch — OPEN, but the naive route (general `|C|=2` Two-Touch, already confirmed FALSE,
`\approx24\%` failure) is decisively NOT needed; a much narrower, still-open sub-claim is identified as
the actual remaining target.** The MATCH branch (peeling `w_1`, matching with partner `w_j`) is
`\mathrm{OPT}_{+1}(\{b_0,d\},X)` for `d:=|w_1-w_j|`, `X:=W\setminus\{w_1,w_j\}` — a `|C|=2` sub-problem.
**Critically, we do NOT need the general `|C|=2` Two-Touch closed form here (which is false) — we only
need this SPECIFIC comparison: does the MATCH branch's value dominate the ORIGINAL problem's own
`\mathrm{Two}\text{-}\mathrm{Touch}(\{b_0\},W)`, for THIS specific `d` (constructed from `w_1=\max(W)`,
not an arbitrary background pair)?** This narrower target was checked two ways this round:
- `twotouch_induction_diag.py`: does `\mathrm{OPT}_{+1}(\{b_0,d\},X)\ge\mathrm{Two}\text{-}\mathrm{Touch}
  (\{b_0\},W)` (the actual optimum of the `|C|=2` sub-problem, not merely one candidate)? `0/7{,}265`
  failures across genuine `(b_0,W,w_j)` triples, `|W|\in\{3,\dots,6\}`.
- `twotouch_stronger.py`: the even stronger, fully case-by-case version — does **every** candidate
  selection `\gamma` of `X` (not just the optimal one, exhaustively enumerated) satisfy `e(\{b_0,d\}\cup
  \gamma)\ge\mathrm{Two}\text{-}\mathrm{Touch}(\{b_0\},W)`? `0/15{,}958` failures, exhaustively enumerated
  (not sampled) across `288` genuine instances.

**This "Match-Branch Domination" sub-claim is a strictly narrower, more tractable target than the false
general `|C|=2` Two-Touch formula** (it only needs to hold for this one comparison, using the specific
structure `d=|w_1-w_j|` with `w_1=\max(W)`, against the specific target
`\mathrm{Two}\text{-}\mathrm{Touch}(\{b_0\},W)` — not for arbitrary `|C|=2` targets). **Not proved this
round** — no algebraic mechanism was found in the remaining time; flagged as the concrete next target
for Gap 1a, correctly re-scoped away from the dead general-`|C|=2` route.

**Honest summary for Two-Touch:** `3` of `5` structural pieces (base case, DELETE branch, KEEP branch's
`b_0>w_1` sub-case) are **fully, rigorously proved this round** — genuine, certifiable-quality progress,
though not yet packaged as a standalone certified lemma since the overall Two-Touch statement is not yet
closed. The remaining `2` pieces (KEEP branch's `b_0\le w_1` sub-case, needing a `\sigma=-1` mirror
result; MATCH branch, needing the narrower "Match-Branch Domination" sub-claim) are both **precisely
identified, strongly corroborated (`0` failures across `>25{,}000` combined checks this round), but not
proved** — genuinely open, correctly reported as such, not overclaimed as "Two-Touch proved."

#### 26.6 What remains (for the next round)

1. **Gap 1b:** the general recursion-depth induction (`|Z_1|\ge2`) — untouched, large, still fully open.
2. **Gap 1c:** Step 3's nonempty-`\xi^*` nearest-neighbor construction — attempted, two routes tried and
   stalled (§26.4); the case-split (generic/duplicate, per the explorer's own diagnostic) is the
   recommended next attempt.
3. **Gap 1a:** Two-Touch's two remaining sub-pieces — (i) the `\sigma=-1` mirror bound needed for the KEEP
   branch's `b_0\le w_1` sub-case; (ii) the "Match-Branch Domination" sub-claim (§26.5(e)) for the MATCH
   branch. Both are strongly corroborated, well-scoped, tractable-looking targets for a future round —
   genuinely narrower and more promising than the previously-flagged (and confirmed-false) general
   `|C|=2` Two-Touch route.
4. Even a full closure of Two-Touch would **not** by itself close Gap 1a's general-`q` Per-Partner
   Domination induction (§25.2's standing caveat, unchanged) — a separate per-`q` case analysis on
   `A_{3,l}`'s own recursion remains needed on top.

### 27. Round 17 outliner revision — **structural unification: Gap 1b's general step is NOT
independent content, it IS (half of) Gap 1a's general-`q` Deletion-Suffices/Per-Partner-Domination
conjecture; a new "Three-Touch" candidate closes Two-Touch's missing `sigma=-1` mirror; Gap 1c's
nonempty-`xi*` case refines to a 3-way split whose middle case reduces for free**

**Provenance.** Three round-17 explorers scouted the three named gaps directly:
`math-explorer-gap1a-two-touch.md` (Gap 1a's 2 open Two-Touch sub-pieces), `math-explorer-gap1c-
halfstep.md` (Gap 1c's nonempty-`\xi^*` construction), `math-explorer-gap1b-induction.md` (Gap 1b's
general induction). **This section reconciles all three into one precise picture — no claim below is
promoted to "proved" beyond what each explorer's own write-up supports; every closure below is either
already-certified machinery or an explicitly-flagged conditional/corroborated conjecture.** No new
slug is opened (single-gap-trap, per CLAUDE.md) — all findings are folded into the existing
`potential-weighting-upper-bound` route (Claim A via the Non-Matching-Witness Criterion, §17.4/§17.5).

#### 27.1 The headline structural discovery: Gap 1b's general induction collapses into Gap 1a

**Claim (this round's central reconciliation, from `math-explorer-gap1b-induction.md`).** At
recursion depth `k=|\mathrm{rest}|` (the pure DELETE/KEEP path, `C=\{b_0,d_{k^*}\}` fixed, `W=
\mathrm{rest}\cup\{w_1\}`), the Sum Bound's target inequality `w_1\ge\mathrm{OPT}_{+1}(C,\mathrm{
rest})+\mathrm{OPT}_{-1}(C,\mathrm{rest})` is **algebraically identical** (via the already-certified
`\S13.2` KEEP-branch closed form at `h=0`, `\mathrm{KEEP}=w_1-\mathrm{OPT}_{-1}(C,\mathrm{rest})`,
`\mathrm{DELETE}=\mathrm{OPT}_{+1}(C,\mathrm{rest})`) to **"DELETE beats-or-ties KEEP" in the
trichotomy computing `\mathrm{OPT}_{+1}(C,W)`** — which is *exactly* the DELETE-vs-KEEP half of Gap
1a's Deletion-Suffices-for-`k^*` claim (`\S21.1` Step 2, proved `q\le3`, open `q\ge4`). **This is a
genuine equivalence, not a loose analogy** — it is a direct substitution of the certified closed form,
independently re-derivable in 3 lines from `\S13.2` (verified by re-deriving it during this
reconciliation, before writing it up):
```
h=0: DELETE = OPT_{+1}(C,rest),  KEEP = w1 - OPT_{-1}(C,rest)   [certified peeling trichotomy]
Sum Bound target:  w1 >= OPT_{+1}(C,rest) + OPT_{-1}(C,rest)
              <=>  w1 - OPT_{-1}(C,rest) >= OPT_{+1}(C,rest)
              <=>  KEEP >= DELETE
```
so "Sum Bound holds at depth `k`" `\iff` "DELETE `\ge` KEEP at that node" — precisely half of what
Deletion-Suffices-for-`k^*` (`A_{3,k^*}=e(C)`, i.e. DELETE beats BOTH KEEP and MATCH) asserts at
general `q`. **Consequence: Gap 1b's general induction is not a separate open lemma — proving
Deletion-Suffices-for-`k^*` at general `q` (already the field's top-priority item since round 14) would
hand you Gap 1b's inductive step's DELETE-vs-KEEP half for free, at every recursion depth, via this
same substitution** (the explorer confirmed the two free bounds used at the base case, `A_1\le b_0`
via Shrink-List and `A_1\le|b_0-w_j|` via Step-1(†), are available unchanged at *every* depth, since
along the pure DELETE/KEEP chain the "current `w_1`" is always some original `z_j`, never a
MATCH-derived value — `A_1` itself never needs re-deriving deeper in the recursion).

**What is NOT free — the DELETE-vs-MATCH half.** Deletion-Suffices-for-`k^*` needs DELETE to beat
BOTH KEEP and MATCH; the equivalence above only accounts for the KEEP half. The MATCH branch "carries
forward the full difficulty of the problem, unreduced, to the next level" (the file's own pre-existing
`\S13.2` diagnosis) — this is the genuinely hard residual, common to **three** gaps at once (a third
link, not previously recorded): Gap 1a's own general-`q` Deletion-Suffices induction, Gap 1b's general
Sum-Bound induction (its DELETE-vs-MATCH half), and Two-Touch's still-open MATCH sub-piece
(`\S26.5(e)`, "Match-Branch Domination"). **These are not three independent open problems any more —
they are three faces of the same unresolved DELETE-vs-MATCH mechanism.**

**Negative control confirming a flat induction cannot work (from the same explorer, do not
re-attempt):** the trigger `M<A_1` references the TOP-level sibling `A_1`, not a locally-recomputed
analog at each recursion depth — dropping it while keeping `h=0` gives `10{,}901/29{,}429` (`37.0\%`)
failures at `q=4`, matching round 14's own base-case negative control almost exactly and newly
confirming the *same* failure persists at depth `k=1$. **Any inductive-step proof must carry the same
external `A_1` (not a re-derived per-level bound) through every recursion level** — ruling out a
"clean" flat induction on `(C,\mathrm{rest})` treated as a self-contained smaller instance, as already
suspected in `\S23.3` but now confirmed with a concrete failure rate at a second depth.

**A cheap pruning fact (useful for a future builder, not yet exploited):** in every triggered+`h=0`
instance sampled this round (`3{,}118/3{,}118` at `q=4`, `76/76` at `q=5`), `A_{3,k^*}` is achieved by
the PURE DELETE branch — never KEEP, never MATCH. A proof attempt therefore only needs to rule out KEEP
and MATCH winning, not characterize what happens when they do.

#### 27.2 Gap 1a's Two-Touch — the two open sub-pieces, reconciled

**(d) KEEP branch `b_0\le w_1` — a new closed-form candidate for the missing `\sigma=-1` mirror.** The
file (`\S26.5(d)`) had flagged the `\sigma=-1` mirror of Two-Touch as "not yet even formulated." This
round's explorer formulates and heavily corroborates a specific candidate:
```
Three-Touch({c},W) := max( e({c}), max_w e({c,w}), max_{i<j} e({c,|w_i-w_j|}),
                            max_{i<j} e({c,w_i,w_j}), max_{i<j,k distinct} e({c,|w_i-w_j|,w_k}) )
```
i.e. the maximization mirror needs **touch `\le3`** (not `\le2` like the `\sigma=+1` minimization
side) — a genuine, previously-undiscovered min/max asymmetry, mechanistically explained by the
maximizer being able to exploit Lemma P's duplicate-pair cancellation *adversarially* (manufacture a
duplicate of `c` via a MATCH, forcing cancellation that leaves only the untouched top elements
standing) — a mechanism with no minimization-side analogue (duplicate cancellation only ever *helps*
the `\sigma=+1` minimizer). The extra touch-3 term is load-bearing, not redundant (strict maximizer in
`193/1000` sampled instances). **Corroboration: `0` violations across `\sim3{,}480` combined checks**
(random `|W|\le7`, an exhaustive `\{0,1,2,3\}`-grid, a duplicate-heavy adversarial family) **for
Three-Touch itself**, plus **`0/1{,}239`** violations of the actual end-to-end target it needs to close
(`w_1-\mathrm{ThreeTouch}(b_0,\mathrm{rest})\ge\mathrm{TwoTouch}(\{b_0\},W)`). **This is genuinely
new, concrete content the file did not have — not proved, but no longer "not even formulated."**
Recommended proof route (explorer's own, structurally sound on inspection): the same
induction-on-`|W|`/peeling-trichotomy strategy that already closed 3/5 of the `\sigma=+1` pieces —
DELETE branch is free (subset-of-candidates argument, sign-independent, carries over verbatim); base
case `|W|\le3` should reduce to a "Four-Bound"-style finite case-split lemma (a larger analogue of the
already-certified Three-Bound Domination Lemma); KEEP/MATCH branches of Three-Touch's OWN recursive
proof need fresh case analysis (more sub-cases than Two-Touch's, since Three-Touch has 5 candidate
shapes vs. 3) — **none of this attempted yet, this round was scouting only.**

**(e) MATCH branch / Match-Branch Domination — narrowed further, still no closing mechanism.**
Confirmed the base case (`\gamma=\emptyset`, leave `X` fully deleted) is IMMEDIATE — `e(\{b_0,d\})` is
literally one of `\mathrm{TwoTouch}(\{b_0\},W)`'s own candidate terms, so the inequality holds trivially
there by definition of the min. **The entire open content is whether further touching `X` can ever push
the value below `\mathrm{TwoTouch}(\{b_0\},W)`** — a real, common phenomenon (touching `X` drops the
value below the base `e(\{b_0,d\})` in `148/300` sampled instances, `\approx49\%`), yet never below the
target `\mathrm{TwoTouch}(\{b_0\},W)` in any check run so far. **One candidate shortcut ruled out this
round, more sharply than previously documented:** using the confirmed-dead general `|C|=2` "touch
`\le2`" family merely as a ONE-DIRECTIONAL lower bound (not needing the false equality) is ALSO false —
`1{,}075/3{,}000` (`35.8\%`) of `|C|=2` instances have the true optimum strictly BELOW the naive
family's prediction. **This closes off even the weakest possible shortcut via the dead `|C|=2` route —
do not attempt it again in any form.** No closing mechanism found. **Recommended next angle (explorer's
own, not yet formulated as a concrete statement): a per-partner (per-`w_j`) indexed strengthened
hypothesis, mirroring how the Per-Partner Domination Lemma itself sharpened a similarly-stuck aggregated
claim in round 14** — flagged as the concrete next target for a future round, not attempted this round.

**Note on §27.1's unification:** Match-Branch Domination is the SAME underlying difficulty as Gap
1a/1b's shared DELETE-vs-MATCH residual identified in §27.1 (both ask "can a MATCH-based selection beat
a pure-touch/DELETE-style bound"), though the exact statements differ in shape (Two-Touch's MATCH branch
compares against `\mathrm{TwoTouch}` itself; Deletion-Suffices' MATCH half compares `A_{3,k^*}` against
`A_1`) — flagged as a structural kinship worth a future round checking directly (do NOT assume they are
literally the same lemma without checking; scouted as "closely related," not "identical," this round).

#### 27.3 Gap 1c's nonempty-`\xi^*` case — refined into a genuine 3-way split, middle case closes for free

**New finding (`math-explorer-gap1c-halfstep.md`): the choice of "the" optimal witness `\xi^*` among
ties is load-bearing, and the correct tie-break (sparsest/minimum-cardinality) was implicit but
untested until this round.** Testing the round-16 construction against the LARGEST-cardinality optimal
witness gives **5 concrete counterexamples** (exact-`Fraction`, e.g. `B_1=[22,22]`,
`\mathrm{Res}=[15,14,10,6,4]`, partner `m=1`, `d=1`: largest witness `\{6,6\}` gives `c=6`,
`e(B_1\cup\{6\})=4>\mathrm{RHS}=1`) — **do NOT use an arbitrary/first-found optimal witness; the
sparsest witness is the only tie-break tested that survives.** Even at minimum cardinality, the naive
construction is not unconditionally true — `726/728` succeed in a fresh sweep, and the **2 residual
"failures" are not real counterexamples**: both occur exactly when the sparsest `\xi^*` is a literal
duplicate pair `\{c,c\}`, and Lemma P then forces `\mathrm{RHS}=e(B_1\cup\{d\}\cup\{c,c\})=e(B_1\cup
\{d\})` exactly — collapsing the target to `\mathrm{LHS}\le e(B_1\cup\{d\})`, **exactly the certified
`delete-suffices-insertion-domination.md` conclusion, conditional on Deletion-Suffices-for-`k^*`
(the same conditional as §26.3's `\xi^*=\emptyset` closure).**

**Resulting 3-way case split (refines §26.4's flat "generic vs. duplicate" flag into a precise
taxonomy):**
- **(a) Sparsest optimal witness has no internal Lemma-P cancellation (generic/irreducible)** — the
  overwhelming majority tested (`726/728`, `\approx99.7\%` at this round's scale). **This is the true
  remaining hard core.** No proof found; `c=\mathrm{argmin}_{x\in\xi^*}|x-d|` construction succeeds
  unconditionally in every test across `\sim1{,}150$+ combined checks this round and last, but remains
  a corroborated conjecture, not a proof — the two algebraic routes already tried and stalled in §26.4
  remain the state of the art here, now correctly re-scoped to apply ONLY to this narrower sub-case.
- **(b) Sparsest optimal witness Lemma-P-collapses to `\emptyset`-equivalent (duplicate pair, or richer
  cancelling structure)** — **reduces for free** to the same conditional mechanism as case (c) below,
  via the identical certified lemma chain. **New this round, not previously identified as a distinct
  sub-case.** Untested at larger cancelling structures (e.g. two duplicate pairs, or a pair plus a value
  equal to `d`) — flagged, not yet generalized.
- **(c) `\xi^*=\emptyset` literally** — already closed (§26.3), same conditional (Deletion-Suffices-
  for-`k^*`, `q\le3` proved).

**Cases (b) and (c) are BOTH conditional on the same open Gap-1a conjecture as §26.3 — they do not add
new unconditional content, but they DO shrink case (a), the true residual, to a strictly smaller,
better-characterized set of instances** than the file previously tracked.

**Sharper crux mapping (supersedes the round-13/16 flat pointer).** Re-reading `aimo-0960`'s actual
solution in full: it kills a repeated exponent among *minimum-length* representations via an exact
rewrite identity (same length, strictly smaller lex order), but handles the two *boundary* repeats
(which the identity cannot reach) via a SEPARATE value-bound argument. This maps precisely onto the
refined picture: "minimum length" `\leftrightarrow` sparsest witness (confirmed the correct tie-break,
not a loose guess); "kill a repeat via an identity" `\leftrightarrow` case (b)'s Lemma-P collapse;
"boundary repeats via a different, value-bound argument" `\leftrightarrow` case (a)'s residual, which
needs the nearest-`c` algebraic bound, not a rewrite identity. **`aimo-0960` genuinely needed TWO
different techniques for two different structural sub-cases of its own minimal witness — recommend the
outliner/builder structure any future write-up of Step 3 as two sub-lemmas (cases (a) and (b)), not one
uniform mechanism**, per this sharper analogy. (`aimo-0438`/`aimo-0666`'s iterative local-swap-to-
canonical-shape machinery is confirmed LESS applicable — the objects don't match closely enough; do not
port it.)

**Cheap high-value next check, not yet done:** verify (bounded computation, larger `q`/`v_{\max}` than
this round's `\le9`/`\le60`) whether "sparsest `\Rightarrow` size `\le2$, and size-2 always a duplicate
pair" is a genuine dichotomy within `\mathcal F`-provenance, or whether larger irreducible sparsest
witnesses occur. If the dichotomy holds, case (a)'s residual is always a single element and may reduce
directly to a Two-Touch-style argument (§27.2) instead of needing the full 2-variable
insertion-difference algebra — this is the single highest-leverage cheap check before committing more
build budget to case (a)'s algebra.

#### 27.4 The unified picture — what the population's true remaining bottleneck now is

Reconciling all three findings: the population's 3 named gaps (1a general-`q`, 1b general induction, 1c
nonempty-`\xi^*`) have **effectively collapsed toward a smaller set of independent open items**:

1. **The DELETE-vs-MATCH mechanism at general `q`** (Deletion-Suffices-for-`k^*`'s MATCH half) — this
   is now understood to be shared load-bearing content for: (i) Gap 1a's own general-`q` Per-Partner
   Domination induction (unchanged top priority since round 14), (ii) Gap 1b's general Sum-Bound
   induction's DELETE-vs-MATCH half (§27.1, new this round — the DELETE-vs-KEEP half is a free
   corollary of (i)), and (iii) is structurally kin to (not proved identical to) Two-Touch's own
   Match-Branch Domination sub-piece (§27.2(e)). **This is now the single highest-leverage open item in
   the whole population** — a win here has 2-3x the payoff it appeared to have before this round's
   reconciliation.
2. **Gap 1c's case (a)** (sparsest, Lemma-P-irreducible nonempty `\xi^*`) — genuinely narrower than
   before (§27.3), but still an independent open construction (the nearest-`c` algebraic bound), not
   reducible to item 1 above (though possibly reducible to Two-Touch per the cheap check flagged in
   §27.3, untested).
3. **Two-Touch's `\sigma=-1$ mirror (KEEP branch `b_0\le w_1`)** — now has a concrete candidate
   (Three-Touch, §27.2(d)), unproved but no longer "not even formulated"; a genuinely tractable-looking
   induction target using already-certified base-case technique.
4. **Two-Touch's MATCH branch (Match-Branch Domination)** — kin to item 1 (not proved identical),
   narrowed (base case trivial, `35.8\%`-failure shortcut ruled out), no mechanism found.

**None of these is closed. Do NOT declare any gap closed this round — every closure above is either
already-certified (Sum-Bound base case, Insertion-Difference Identity, Delete-Suffices-Insertion-
Domination, all from round 16) or explicitly conditional/corroborated-not-proved.** The genuine
progress this round is structural: the population now understands its 3 nominally-separate gaps share
a smaller number of true independent mechanisms, sharpening where build effort should concentrate.

#### 27.5 Updated priority order and concrete build targets this round

1. **[HIGHEST LEVERAGE, per §27.4 item 1] Attack Deletion-Suffices-for-`k^*` / Per-Partner Domination
   at general `q`, specifically the DELETE-vs-MATCH half** (Gap 1a's own long-standing top-priority
   item, now confirmed to also close Gap 1b's inductive step's DELETE-vs-KEEP half for free via §27.1's
   equivalence, and to be structurally kin to Two-Touch's Match-Branch Domination). Use the cheap
   pruning fact (§27.1): under trigger+`h=0`, `A_{3,k^*}` is always achieved by pure DELETE in every
   sampled instance — the proof only needs to RULE OUT KEEP/MATCH winning, not characterize them. The
   KEEP half is free via §27.1's 3-line equivalence once stated; concentrate all algebraic effort on
   the MATCH half.
2. **[TRACTABLE, concrete target] Prove the Three-Touch closed form (§27.2(d))** via induction on
   `|W|`, following the already-successful `\sigma=+1` proof pattern: DELETE branch free, base case
   `|W|\le3` via a new finite case-split lemma. This closes Two-Touch's KEEP-branch `b_0\le w_1`
   sub-case once combined with the already-confirmed end-to-end target (`0/1{,}239`).
3. **[NARROWED, still hard] Attack Gap 1c's case (a)** (sparsest, Lemma-P-irreducible nonempty `\xi^*`)
   using the nearest-`c` algebraic construction, now correctly scoped away from the duplicate-pair case
   (b), which reduces for free. First perform the cheap dichotomy check (§27.3) at larger `q`/`v_{\max}`
   before committing to the algebra — if the dichotomy holds, this may reduce to a Two-Touch-style
   argument instead of needing fresh 2-variable insertion algebra.
4. **[CHEAP, do alongside anything] Formalize Gap 1c's case (b)** (duplicate-pair sparsest witness) as
   an explicit corollary of `delete-suffices-insertion-domination.md`, extending §26.3's write-up — a
   few lines once the "sparsest witness is Lemma-P-reducible" trigger condition is formally stated.
   Does not require closing item 1.
5. **[LOWER PRIORITY]** Match-Branch Domination (§27.2(e)) — attempt a per-partner-indexed strengthened
   hypothesis (mirroring round 14's Per-Partner Domination sharpening), no concrete candidate yet.

**Watch out for (all items, summary):** (i) do NOT claim Gap 1b's general induction is "closed" or
"free" — only its DELETE-vs-KEEP half reduces to Gap 1a's (still-open) conjecture; the DELETE-vs-MATCH
half is the genuinely hard remaining content, shared with items 1 and 4 above; (ii) do NOT use an
arbitrary/first-found optimal witness `\xi^*` for Gap 1c — confirmed to fail (5 counterexamples); use
the sparsest witness only; (iii) do NOT resurrect the general `|C|=2` Two-Touch formula, even as a
one-directional lower bound (now confirmed false both ways, `23.8\%$ and `35.8\%$ failure respectively);
(iv) do NOT drop the top-level trigger `A_1` when attempting Gap 1b's or Gap 1a's induction at any
depth — confirmed load-bearing at every depth tested (`37.0\%$ failure at `q=4$ without it, matching
round 14's base-case finding); (v) items 2 (Three-Touch) and 3 (Gap 1c case (a)) are logically
INDEPENDENT of item 1 (Deletion-Suffices general-`q`) — a builder can make progress on either without
waiting for the other.

**Cases to cover / no new casework introduced beyond what's already named above.**

**Recommended build order this round:** items 2 and 4 first (cheapest, most tractable, independent of
everything else); item 1 next (highest leverage, hardest); item 3 (Gap 1c case (a)) after item 1's
cheap dichotomy pre-check.
5. The `\sigma=-1` mirrors of the Sum Bound and the half-step (queued since round 15) remain unstarted.

### 28. Round 17 build — two precision fixes applied; Gap 1c case (b) confirmed non-vacuous with an
explicit witness; Three-Touch's DELETE branch, base case, and BOTH KEEP-branch parity sub-cases fully
proved (4 of 5 structural pieces now closed, mirroring Two-Touch's own 3/5) — MATCH branch (both
Two-Touch's and Three-Touch's) is a recurring open sub-problem of the same flavor for both mirrors,
not yet proved to be a single reducible lemma (see §28.4 for the precise scope of what is/isn't shown)

This round executes items 1, 2, and (a version of) item 2 from §27.5's priority list: the two
precision notes flagged by the outline-reviewer, an explicit witness for Gap 1c's rare case (b), and
a genuine attempt (not merely scouting) at Three-Touch (§27.2(d)), following the same
induction-on-`|W|`/peeling-trichotomy strategy that already closed 3/5 of Two-Touch's own pieces. All
computations use bounded exact-`Fraction` arithmetic (`/tmp/round-17/verify_builder/`), hand/small-case
proofs first, no unbounded symbolic search.

#### 28.1 Precision fix (a) — the Deletion-Suffices/Sum-Bound quantifier (§27.1), tightened per the
outline-reviewer's recommendation

**Fix applied.** §27.1's headline claim is restated with the precise, weaker (sufficient) quantifier
the outline-reviewer asked for: "Deletion-Suffices-for-`k^*` holds along the *specific* DELETE/KEEP-only
descent chain from one genuine top-level base generator, with the SAME external top-level `A_1` (not a
locally re-derived per-level trigger) threaded through every recursion depth" — **not** "for every
independently-sampled top-level instance of size `q'<q`" (the stronger, unneeded reading §27.1's prose
sometimes suggested). Concretely: the claim being used is that if a future proof establishes
Deletion-Suffices-for-`k^*` (`A_{3,k^*}=e(C)`, i.e. `M=D_{k^*}`) **for every node reachable by the pure
DELETE/KEEP descent from a single genuine base generator, at every depth, with the descent's own
external `A_1` carried through unchanged**, then Gap 1b's DELETE-vs-KEEP inductive step follows for
free at every depth of that one chain — it does **not** claim (and does not need) that Deletion-Suffices
holds for arbitrary freshly-sampled `(C,W)` pairs of size `q'<q` unrelated to any such chain (this
weaker/unneeded reading was never used computationally — the negative control in §27.1, dropping the
top-level `A_1`, already demonstrates that an unrelated/re-derived trigger is exactly what breaks the
claim, confirming the *chain-threaded* reading is the one that matters). This is a wording-only fix; no
computation changes, no claim is weakened or strengthened mathematically — only the English is now
unambiguous.

#### 28.2 Precision fix (b) — the `\xi^*` LHS/RHS labeling drift (§25.3 vs. §26.3/26.4/27.3)

**Diagnosis, traced precisely.** The confusion the outline-reviewer flagged has an exact source: §25.3's
own display (`OPT_{+1}(B_1\cup\{d\},X)\ge OPT_{+1}(B_1,X)`) writes the *augmented* quantity
`OPT_{+1}(B_1\cup\{d\},X)` first (as the literal left token of `\ge`), while §26.3's "the half-step
follows in 3 lines" display (`OPT_{+1}(B_1,X)\le e(B_1\cup(\xi^*\setminus\{c\}))\le OPT_{+1}(B_1\cup
\{d\},X)`) writes the *un-augmented* quantity `OPT_{+1}(B_1,X)` first instead — the SAME mathematical
statement, but with the two quantities swapped in reading order between the two displays. "`\xi^*` is
the LHS-optimal witness" is therefore genuinely ambiguous: consistent with §25.3's own display it means
`\xi^*` optimizes `OPT_{+1}(B_1\cup\{d\},X)`; consistent with §26.3's display it would mean the opposite.
**Fix — eliminate the LHS/RHS terminology entirely, replaced with an unambiguous name.** Throughout
§25.3, §26.3, §26.4, §27.3 (and this section), `\xi^*` is (and was always used as, per §26.3/26.4/27.3's
actual computations, cross-checked against their code) **the AUGMENTED-optimal witness**: an optimal
selection witness of `OPT_{+1}(B_1\cup\{d\},X)` (the quantity with `d` inserted into the background).
The canonical statement of the half-step, used consistently from here on, is
```
OPT_{+1}(B_1,X)  <=  OPT_{+1}(B_1 u {d}, X)          [the AUGMENTED problem, on the right]
```
and `\xi^*` always refers to an optimal witness of the right-hand (augmented) problem. This matches
every actual computation already performed (§26.3's `\xi^*=\emptyset$ analysis, §26.4's construction,
§27.3's 3-way split) — no result changes, only the label. (No file edit was made to the historical §25.3
prose itself, to preserve the round-by-round record per this project's convention of appending rather
than rewriting; this section is the authoritative disambiguation for all future reference.)

#### 28.3 Gap 1c case (b) — explicit, independently-verified non-vacuous witness (dispatch task 2)

**Task.** Confirm case (b) (§27.3: "sparsest optimal witness of `OPT_{+1}(B_1\cup\{d\},X)` Lemma-P-
collapses to a duplicate pair `\{c,c\}`") is a genuine, non-vacuous event within `\mathcal F`-provenance
by exhibiting one concrete instance — the outline-reviewer's own `2759`-trial sweep found `0` such
instances and flagged this as unverified.

**Search performed.** Reused the round-17 explorer's own genuine-`\mathcal F`-provenance generator
(`/tmp/round-17/gap1c_probe/probe1.py`'s `find_F_instance`, which enforces the real trigger `M<A_1` and
true global-argmin `k^*`) with a targeted extraction pass over `101` genuine `\mathcal F` instances
(`/tmp/round-17/verify_builder` via `/tmp/round-17/gap1c_probe/extract_caseb.py`), explicitly checking
every sparsest optimal witness of every partner-pair sub-problem for a duplicate-pair value pattern.

**Explicit witness found and hand-verified.**
```
B_1 = {16, 15},   Res = (11, 10, 9, 6, 3),   partner index m=1 (Res[1]=10),
d = |Res[0]-Res[1]| = |11-10| = 1,   X = Res \ {11,10} = (9, 6, 3).
```
Direct computation: `OPT_{+1}(B_1\cup\{d\},X) = OPT_{+1}(\{16,15,1\},(9,6,3)) = 2`, achieved (among
others) by the selection "keep `3`, match `9` and `6`" — contributed multiset `\{3,3\}` (the kept
literal `3` from `X`, plus `|9-6|=3` from the match), size-`2`, a literal duplicate pair. This is a
**sparsest** optimal witness (no size-`1` or size-`0` selection achieves the same value `2`: deleting
everything gives `e(\{16,15,1\})=16-15+1=2`... **this coincides**, so `\emptyset` is ALSO an optimal
witness here, but the point is a size-2 duplicate-pair witness exists among the optima, confirming case
(b)'s configuration is reachable). Take instead the reviewer's third found instance for a case where the
duplicate-pair witness is the *unique-cardinality-minimal nonempty* type on record:
```
B_1 = {2, 2},   Res = (24, 23, 18, 12, 6),   partner index m=1 (Res[1]=23),
d = |24-23| = 1,   X = Res \ {24,23} = (18, 12, 6).
```
`OPT_{+1}(\{2,2,1\},(18,12,6)) = 1`, achieved by "keep `6`, match `18,12`" — contributed multiset
`\{6,6\}` (kept `6` from `X`, plus `|18-12|=6` from the match). **Hand-verification via Lemma P**
(`lemmas/duplicate-pair-invariance.md`): `e(B_1\cup\{d\}\cup\{6,6\}) = e(\{2,2,1,6,6\})`; sorted
descending `(6,6,2,2,1)`, alternating sum `6-6+2-2+1=1`; by Lemma P the duplicate pair `\{6,6\}$ cancels,
giving `e(\{2,2,1\})=2-2+1=1` directly — matches `OPT_{+1}(\{2,2,1\},(18,12,6))=1` exactly, confirming
the mechanism (RHS `=e(B_1\cup\{d\})` exactly, as case (b)'s reduction requires). Both instances
independently re-derived by hand from the printed exact-`Fraction` search output, not merely trusted
from the search — **case (b) is now confirmed non-vacuous with a fully worked, hand-checked witness**,
closing the outline-reviewer's flagged verification gap. (This does not itself close case (b)'s
*general* reduction — that reduction, stated in §27.3, was already correctly proved as a conditional
consequence of `delete-suffices-insertion-domination.md` + Deletion-Suffices-for-`k^*`; this section
only supplies the missing existence witness the reviewer asked for.)

#### 28.4 Three-Touch (§27.2(d), dispatch task 3) — DELETE branch, base case `|W|<=3`, and BOTH
KEEP-branch parity sub-cases FULLY PROVED; MATCH branch remains open

**Strategy, mirroring Two-Touch's own successful proof shape exactly:** strong (mutual) induction on
`q:=|W|`, peeling `u_1:=\max(W)` via the `\sigma=-1` instance of the certified Generalized
Multi-Background Peeling Lemma's DELETE/KEEP/MATCH trichotomy (§13.2), with singleton background
`\{c\}`.

**(a) Base case `|W|\le3` — FULLY PROVED, unconditional.** See **Lemma B**,
`lemmas/max-element-triple-identity-and-threetouch-basecase.md` (submitted this round): for `|W|\le2`
every selection of `W` is *literally* one of `\mathrm{ThreeTouch}`'s own candidates, so equality is
immediate; for `|W|=3` the single non-candidate selection ("keep all three") is shown dominated by an
explicit `\mathrm{ThreeTouch}` candidate via a clean 4-way case split on the rank of `c` among the three
sorted values of `W`, using a new elementary fact (**Lemma A**, same file: if `a=\max(a,b,c)` then
`e(\{a,b,c\})=a-|b-c|`). Two of the four cases give **exact equality**, not merely domination — a clean,
tight proof, independently corroborated `0/6000` (case-split candidate dominance), `0/956` (case-2
exact-equality), `0/3000` (direct `|W|\le2` equality) at `/tmp/round-17/verify_builder/verify_basecase_
proof.py` and `basecase3.py`.

**(b) DELETE branch — FULLY PROVED, for every `q\ge1`, by the identical argument as Two-Touch's own
DELETE branch (§26.5(b)), verbatim, sign-independent.** Peeling `u_1$ into `D` gives branch value
`\mathrm{OPT}_{-1}(\{c\},W\setminus\{u_1\})`, which by the (strong) induction hypothesis equals
`\mathrm{ThreeTouch}(c,W\setminus\{u_1\})`. Since every candidate of `\mathrm{ThreeTouch}(c,
W\setminus\{u_1\})$'s own candidate list uses only elements of `W\setminus\{u_1\}\subseteq W`, it is
literally a subset of `\mathrm{ThreeTouch}(c,W)$'s candidate list; a **maximum** over a subset is
`\le` the maximum over the full set (the mirror-image of Two-Touch's DELETE argument, which used a
**minimum** over a subset being `\ge`), so `\mathrm{ThreeTouch}(c,W\setminus\{u_1\})\le\mathrm{ThreeTouch}
(c,W)`. Hence DELETE branch `\le\mathrm{ThreeTouch}(c,W)`, as needed (recall we need an UPPER bound on
`\mathrm{OPT}_{-1}`, the reverse direction from Two-Touch's lower-bound target, since `\sigma=-1` is a
maximization). No computation needed beyond the definitional subset argument; this is exact, general,
elementary.

**(c) KEEP branch, `h=1` sub-case (`c>u_1`) — FULLY PROVED, unconditional, no induction needed.** By
§13.2's Rank-Extraction closed form (background `\{c\}`, `B_{\mathrm{hi}}=\{c\}`, `B_{\mathrm{lo}}
=\emptyset` when `h=1`): `\text{KEEP} = c - u_1 + \mathrm{OPT}_{-1}(\emptyset,W\setminus\{u_1\})`. By the
already-**certified Empty-Background Lemma** (`lemmas/empty-background-and-background-splitting.md`),
`\mathrm{OPT}_{-1}(\emptyset,W')=\max(W')` (or `0` if `W'=\emptyset`) — an exact, unconditional value,
no induction. If `W\setminus\{u_1\}\ne\emptyset$, `\max(W\setminus\{u_1\})` is `W`'s second-largest
element `u_2`, giving `\text{KEEP}=c-u_1+u_2`. Since `c>u_1\ge u_2\ge0`, `c` is the max of `\{c,u_1,u_2\}`,
so by **Lemma A**, `c-u_1+u_2=e(\{c,u_1,u_2\})` exactly — **literally one of
`\mathrm{ThreeTouch}(c,W)`'s own touch-2 "keep-pair" candidates** (indices `u_1,u_2\in W`), so
`\text{KEEP}\le\mathrm{ThreeTouch}(c,W)` trivially, by definition of the max, with **equality**. (If
`W\setminus\{u_1\}=\emptyset`, i.e. `|W|=1`, this is already inside the proved base case.)

**(d) KEEP branch, `h=0` sub-case (`c\le u_1`) — FULLY PROVED, conditional on Two-Touch already holding
at the strictly smaller size `|W|-1` (a genuine mutual/joint induction, not an extra hypothesis).** By
§13.2's formula: `\text{KEEP}=u_1-\mathrm{OPT}_{+1}(\{c\},W\setminus\{u_1\})`. Writing `\mathrm{rest}':=
W\setminus\{u_1\}` (size `q-1<q`), the **joint induction hypothesis** (the SAME strong induction on
`q` simultaneously proving both Two-Touch's and Three-Touch's equalities for all sizes `<q` — a
legitimate, well-founded scheme, since Two-Touch's own KEEP-branch `b_0\le w_1` sub-case needs
`\mathrm{ThreeTouch}$ at size `|W|-1`, and Three-Touch's KEEP-branch `h=0` sub-case needs
`\mathrm{TwoTouch}$ at size `|W|-1` — always strictly smaller for both, so no circularity) gives
`\mathrm{OPT}_{+1}(\{c\},\mathrm{rest}')=\mathrm{TwoTouch}(\{c\},\mathrm{rest}')` **exactly** (Two-Touch's
full equality, both directions, from the IH). So `\text{KEEP}=u_1-\mathrm{TwoTouch}(\{c\},\mathrm{rest}')
=u_1-\min(A)=\max_{a\in A}(u_1-a)`, where `A` is `\mathrm{TwoTouch}`'s own candidate-value set for
`(\{c\},\mathrm{rest}')` (using the elementary identity `u_1-\min(A)=\max_{a\in A}(u_1-a)` for order
reversal under negation-plus-constant). Term-by-term, using `c\le u_1` throughout:
- `u_1-e(\{c\})=u_1-c=e(\{c,u_1\})$ (since `u_1\ge c`) — a literal `\mathrm{ThreeTouch}(c,W)` touch-1
  candidate (`w=u_1\in W`).
- For each `w\in\mathrm{rest}'`: `u_1-e(\{c,w\})=u_1-|c-w|`. Since `u_1\ge c` and `u_1\ge w` (as
  `u_1=\max(W)`), `u_1` is the max of `\{u_1,c,w\}`, so by **Lemma A**, `u_1-|c-w|=e(\{c,u_1,w\})` —
  a literal `\mathrm{ThreeTouch}(c,W)` touch-2 "keep-pair" candidate (indices `u_1,w\in W`).
- For each `i<j` in `\mathrm{rest}'`: `u_1-e(\{c,|w_i-w_j|\})=u_1-|c-d_{ij}|$ (`d_{ij}:=|w_i-w_j|`).
  Since `d_{ij}\le\max(w_i,w_j)\le u_1` and `c\le u_1`, `u_1$ is the max of `\{u_1,c,d_{ij}\}`, so by
  **Lemma A**, `u_1-|c-d_{ij}|=e(\{c,u_1,d_{ij}\})=e(\{c,u_1,|w_i-w_j|\})` — a literal
  `\mathrm{ThreeTouch}(c,W)` touch-3 candidate ("match `w_i,w_j`, keep `u_1`").

So every term of `\max_{a\in A}(u_1-a)` equals a literal `\mathrm{ThreeTouch}(c,W)` candidate value
(with equality throughout, via **Lemma A** applied three times), hence their max is `\le
\mathrm{ThreeTouch}(c,W)$ (which additionally has candidates beyond these — e.g. touch-2 "match" pairs
and touch-3 shapes not involving `u_1` — so the inequality need not be tight overall, only each term
individually matches a candidate). This gives `\text{KEEP}\le\mathrm{ThreeTouch}(c,W)`, as needed.
**Independently corroborated:** the Lemma-A sub-identity `e(\{u_1,c,w\})=u_1-|c-w|$ (`u_1=\max`):
`0/1854`; the full `h=0` chain `u_1-\mathrm{TwoTouch}(c,\mathrm{rest}')\le\mathrm{ThreeTouch}(c,W)`:
`0/3000` (`/tmp/round-17/verify_builder/verify_keep_identity.py`).

**(e) MATCH branch — OPEN, not attempted to closure this round; explicitly the sole remaining piece.**
Matching `u_1` with a partner `u_j$ gives branch value `\mathrm{OPT}_{-1}(\{c,d\},W\setminus\{u_1,u_j\})`
for `d:=|u_1-u_j|`, maximized over `j` — a `|C|=2` sub-problem for the `\sigma=-1$ side, structurally the
exact mirror of Two-Touch's own still-open MATCH branch / "Match-Branch Domination" sub-claim
(§26.5(e)/§27.2(e)). **Strongly corroborated, not proved:** `0/4475` violations of the true-optimum
target `\mathrm{OPT}_{-1}(\{c,d\},X)\le\mathrm{ThreeTouch}(c,W)` across genuine `(c,W,u_j)` triples
(`/tmp/round-17/verify_builder/threetouch_induction.py`). No algebraic mechanism found or attempted this
round (time budget went to the four proved pieces above); flagged as the concrete next target, exactly
symmetric to Two-Touch's own open MATCH piece.

**One concrete idea tried for Two-Touch's own MATCH branch this round — refuted, recorded so it is not
re-attempted.** Since `\mathrm{OPT}_{+1}(\{b_0,d\},X)` (`d` forced into the background, never
selectable) trivially `\ge\mathrm{OPT}_{+1}(\{b_0\},X\cup\{d\})` (`d` now an ordinary, optionally-
selectable list element — strictly more candidates to minimize over, so the minimum can only decrease;
`0/3000` sanity-confirmed, `/tmp/round-17/verify_builder/match_idea.py`), a tempting reduction chain
would be: if Two-Touch's hard direction already holds at the strictly smaller size
`|X\cup\{d\}|=|W|-1`, then `\mathrm{OPT}_{+1}(\{b_0\},X\cup\{d\})=\mathrm{TwoTouch}(\{b_0\},X\cup\{d\})`
exactly (IH), so it would suffice to show the purely combinatorial claim
`\mathrm{TwoTouch}(\{b_0\},X\cup\{d\})\ge\mathrm{TwoTouch}(\{b_0\},W)`. **This reduction target is
FALSE** — `55/3000` violations found (e.g. `b_0=5,W=(8,10,8),w_j=8`: `d=2`,
`\mathrm{TwoTouch}(\{5\},\{8,2\})=1<3=\mathrm{TwoTouch}(\{5\},\{8,10,8\})`), so "let `d` become
optional instead of forced" is **not** a valid weakening — the forced-background version can be
strictly harder to make large than the free-relaxation version suggests, i.e. this specific chain
cannot close the MATCH branch. Ruled out cleanly; do not re-attempt this exact reduction.

**Net result — a symmetric, precisely-characterized joint reduction.** Combining this round's results
with round 16's: **both Two-Touch (`\sigma=+1`) and Three-Touch (`\sigma=-1`) now have DELETE, base
case, and every KEEP-branch parity sub-case fully proved — in BOTH mirrors, the ONLY thing standing
between "fully proved" and the current partial state is each mirror's own MATCH branch** (Two-Touch's
"Match-Branch Domination," Three-Touch's newly-identified analogous MATCH gap). This sharpens §27.4's
"DELETE-vs-MATCH is the single shared bottleneck" finding: it is now confirmed to be the shared
bottleneck for **four** distinct manifestations (Gap 1a's Deletion-Suffices-for-`k^*` MATCH half, Gap
1b's Sum-Bound MATCH half, Two-Touch's MATCH branch, and — new this round — Three-Touch's own MATCH
branch), not three — but this remains a shared *flavor*, not a proven shared lemma: only the
DELETE-vs-KEEP half (Gap 1a/Gap 1b, §27.1) has an explicit proven reduction; no analogous explicit
reduction exists yet for the DELETE-vs-MATCH half, and §27.2(d)'s touch-depth asymmetry (Two-Touch
needs `\le2`, Three-Touch needs `\le3`) means Two-Touch's and Three-Touch's MATCH branches are not
even the same shape of statement without further work relating them. **Neither Two-Touch nor
Three-Touch is fully closed. Gap 1a's KEEP `b_0\le w_1`
sub-case (which needs full Three-Touch, all 5 pieces, not just 4) remains open. Status correctly stays
`partial`.**

#### 28.5 Honest summary of what remains after this round

1. **The MATCH branch, in all four manifestations named in §28.4** — this is now unambiguously the
   population's single highest-leverage open item, a recurring open sub-problem of the same flavor
   across Gap 1a, Gap 1b, and both Two-Touch and Three-Touch, though not yet proved to be one single
   reducible lemma (see above). No proof attempted this round beyond
   scouting/corroboration; a per-partner-indexed strengthened hypothesis (§27.2(e)'s suggestion,
   mirroring round 14's Per-Partner Domination sharpening) remains the recommended next angle, still
   not formulated concretely.
2. **Gap 1c's case (a)** (sparsest, Lemma-P-irreducible nonempty `\xi^*`) — untouched this round, still
   open, per §27.3/§27.5 item 3.
3. **Gap 1b's general recursion-depth induction** — the DELETE-vs-KEEP half is (per §27.1, precision-
   fixed §28.1) free once Deletion-Suffices-for-`k^*` closes; the DELETE-vs-MATCH half is item 1 above.
   Untouched directly this round (subsumed by item 1).
4. **Certifiable this round:** Lemma A (Max-Element Triple Identity, fully general) and Lemma B
   (Three-Touch's base case `|W|\le3`), submitted as
   `lemmas/max-element-triple-identity-and-threetouch-basecase.md`. The DELETE and KEEP-branch pieces
   of Three-Touch's induction (28.4(b)-(d)) are genuine proved content but, like Two-Touch's own 3/5
   pieces last round, are not packaged as a standalone certifiable lemma since the overall Three-Touch
   statement (needing the MATCH branch too) is not yet closed.

**No overclaim.** Two-Touch and Three-Touch both remain open (MATCH branches unproved in both); Gap 1a's
general-`q` induction, Gap 1b's general induction, and Gap 1c's case (a) all remain open exactly as
before this round. The genuine progress is: two precision fixes applied (wording only, no math change),
one previously-unverified rare case (Gap 1c case (b)) now confirmed non-vacuous with two independently
hand-checked explicit witnesses, and Three-Touch advanced from "0 of 5 pieces attempted" to "4 of 5
pieces fully proved," newly revealing the MATCH-branch bottleneck's fourth manifestation. Status
correctly stays `partial`.

### 29. Round 18 outline — three parallel MATCH-branch/Gap-1c-case-(a) scouting reports reconciled: one
exact reduction ready to certify (Two-Touch's MATCH branch is literally Per-Partner Domination), one
precise new candidate lemma for Three-Touch's MATCH branch (sibling-value domination, `\sigma=-1` only —
**do not conflate with the confirmed-dead `\sigma=+1` mirror**), and Gap 1c case (a) narrowed to a single
scalar sub-quantity (`delta_c`)

Three parallel explorers this round attacked (a) the MATCH-branch bottleneck directly (Two-Touch's own
MATCH branch), (b) Gap 1c's case (a) (the genuinely-irreducible sparsest witness), and (c) the recursive
dependency structure feeding Two-Touch's still-open KEEP `b_0\le w_1` sub-case (which surfaced a new
candidate for Three-Touch's own MATCH branch). All three reports independently verified from their own
raw computation before being written up here; I re-checked the algebra of each reduction below by hand
before recording it as a lemma.

#### 29.1 [READY TO CERTIFY, modulo Per-Partner Domination itself] Match-Branch-Domination-via-
Per-Partner-Domination — Two-Touch's own MATCH branch (`\sigma=+1`) is an exact corollary of Gap 1a's
Per-Partner Domination Lemma, not an independent open item

**Lemma (Match-Branch-Domination-via-Per-Partner-Domination).** Fix a genuine Two-Touch peeling instance
`(\{b_0\},W)`, `w_1:=\max(W)`, and let `\mathrm{MATCH}_j:=\mathrm{OPT}_{+1}(\{b_0,d_j\},W\setminus
\{w_1,w_j\})` (`d_j:=w_1-w_j`) be the MATCH-branch value for partner `w_j\in W\setminus\{w_1\}`. Write
`TT:=\mathrm{TwoTouch}(\{b_0\},W)` for Two-Touch's own closed-form candidate maximum. Then, **conditional
only on Gap 1a's Per-Partner Domination Lemma** (`A_{3,l}\ge\min(A_1,D_l)`, proved unconditionally for
`q\le3`, open/corroborated for `q\ge4`):
```
MATCH_j  >=  TT      for every partner j.
```

**Proof (3 lines, no new computation — every ingredient is either already certified or a one-line
observation).** Under the pure renaming `B_0=\{b_0\}\leftrightarrow\{b_0\}`, `Z_0\leftrightarrow W`,
`l\leftrightarrow j`, Gap 1a's own defined quantities are **literally** `\mathrm{MATCH}_j=A_{3,j}`,
`A_1=\mathrm{OPT}_{+1}(\{b_0\},W\setminus\{w_1\})`, `D_j=e(\{b_0,d_j\})` — not an analogy, the same
formulas with relabeled variables. Two facts, both already in hand with zero new work:
1. `A_1` **is** Two-Touch's own DELETE branch, already **unconditionally** proved `\ge TT` (§26.5(b),
   candidate-set-inclusion, every `|W|`, no gap).
2. `D_j=e(\{b_0,d_j\})` **is, by definition,** one of `\mathrm{TwoTouch}(\{b_0\},W)`'s own touch-`\le2`
   candidates (matching `w_1,w_j` is literally one term of the closed-form max), so `D_j\ge TT`
   **trivially**, no proof needed at all — it is the definition of the max.
So `\min(A_1,D_j)\ge TT$ unconditionally. Per-Partner Domination then gives `\mathrm{MATCH}_j=A_{3,j}\ge
\min(A_1,D_j)\ge TT`. `\blacksquare`

**What this closes outright, unconditionally, right now.** At `|W|=3` the MATCH sub-problem has residual
size `1` (i.e. `q=|Z_0|=3` in Gap 1a's own notation) — exactly the regime Per-Partner Domination is
**already fully, unconditionally proved** in (round 14). Combined with the already-unconditional DELETE
branch (every `|W|`) and the already-unconditional KEEP branch `b_0>w_1` sub-case (§26.5(c)) plus the
KEEP branch `b_0\le w_1` sub-case at `|W|=3` (needs Three-Touch at size `2`, which Lemma B — this round's
own §28.4(a) — already proves unconditionally), **Two-Touch is now fully, unconditionally proved for
`|W|\le3`** — a genuine new closed result, strictly extending the previous base case (`|W|\le2`).

**What this reduces going forward.** At every `q\ge4`, "Match-Branch Domination" is **not independent
open content** — it is entirely subsumed by Per-Partner Domination's own already-top-priority general-`q`
gap (§27.5 item 1). **Stop budgeting separate build effort for "Match-Branch Domination" as a
nominally distinct target** — closing Per-Partner Domination at general `q` closes this automatically, no
further work. This retires §27.5 item 5 ("Match-Branch Domination, per-partner-indexed strengthened
hypothesis") as a separate line item; fold it permanently into item 1.

**Computational corroboration (both the reduction's own two trivial ingredients, already certified, and
the Per-Partner-Domination target restated in Two-Touch's variables — a genuinely fresh code path,
`/tmp/round-18/explore_match/`): `0` failures across `\sim10{,}900` combined checks** (random `q\in\{3,
\dots,8\}`, two exhaustive small grids, dyadic/superincreasing families directly matching the theorem's
own extremal construction, and an adversarial near-tie/duplicate-cluster family after fixing one sampler
bug — see explorer report for the fixed-vs-buggy distinction). Negative controls (dropping `D_j` alone:
`\approx11$–`17\%` failure; dropping `A_1` alone: `\approx54$–`73\%` failure) confirm both terms of the
`\min` are load-bearing, matching Per-Partner Domination's own already-certified negative-control shape
exactly (as expected, since this IS that lemma).

**Open dependency, stated precisely.** This lemma does **not** close Gap 1a's general-`q` gap — it makes
Per-Partner Domination's general-`q` closure worth strictly more (it now also finishes Two-Touch's MATCH
branch at every `q`, for free, in addition to its previously-known consequences: Deletion-Suffices-for-
`k^*`, Gap 1b's DELETE-vs-KEEP half via §27.1). The dependency is one-directional and non-circular: this
section's reduction uses only Per-Partner Domination and two already-unconditional facts, nothing further.

#### 29.2 [NEW CANDIDATE, `\sigma=-1` ONLY — do not conflate with the dead `\sigma=+1` mirror] Three-
Touch MATCH Sibling-Domination Lemma

**Candidate Lemma (unproved, heavily corroborated, `\sigma=-1` peeling only).** For every background
singleton `c\ge0` and sorted list `Z`, peeling `z_1:=\max(Z)` via the certified `\sigma=-1` instance of
the Generalized Multi-Background Peeling Lemma's DELETE/KEEP/MATCH trichotomy (§13.2):
```
MATCH_val := max_j OPT_{-1}({c, |z_1-z_j|}, Z\{z_1,z_j})   <=   max(DELETE_val, KEEP_val)
```
where `DELETE_val:=\mathrm{OPT}_{-1}(c,Z\setminus\{z_1\})` and `KEEP_val:=\mathrm{OPT}_{-1}(\{c,z_1\},
Z\setminus\{z_1\})` are the **true recursive branch values** (not simplified closed-form/candidate
proxies).

**Why this closes Three-Touch's MATCH branch (§28.4(e)) in 2 lines, if proved.** Three-Touch's induction
(§28.4(b)-(d)) has **already fully and unconditionally proved** `DELETE_val\le\mathrm{ThreeTouch}(c,Z)`
and `KEEP_val\le\mathrm{ThreeTouch}(c,Z)` for every size. If the candidate lemma above holds, then
`\mathrm{MATCH}_val\le\max(DELETE_val,KEEP_val)\le\mathrm{ThreeTouch}(c,Z)` immediately — **no candidate-
shape casework against `\mathrm{ThreeTouch}`'s explicit touch-1/2/3 list is needed at all**, a strictly
simpler target than the file's current §28.4(e) framing (`MATCH_val\le\mathrm{ThreeTouch}(c,Z)` directly).
By the already-established (round 17, reconfirmed non-circular in §28.4(d)) joint/mutual induction with
Two-Touch, this would then also close Two-Touch's own still-open KEEP `b_0\le w_1` sub-case at every
size, completing Two-Touch's proof modulo only §29.1's separate, already-tracked Per-Partner-Domination
dependency.

**Computational support (true branch values, brute-force `OPT_\sigma` over ALL selections — not the
conjectural closed form, so this is a rigorous check of the actual target, not of unproven machinery;
`/tmp/round-18/touch_dep/`): `0` counterexamples across `\approx28{,}500` combined trials**, including:
random sweeps (`0/16{,}000`), exhaustive small grids `q\le4,v_{\max}<5` (`0/720`), an adversarial family
engineered to force Lemma-P cancellation in MATCH (`0/4{,}301`), duplicate-heavy stress instances
(`0/2{,}000`), and — most directly relevant — a test confined to **Two-Touch's own genuine `b_0\le w_1`
recursive-call scope**, both testing the candidate lemma itself (`0/4{,}000`) and testing the full
downstream target with `\max(DELETE_val,KEEP_val)` substituted as a literal surrogate for the true
`\mathrm{OPT}_{-1}(b_0,\mathrm{rest})` (`0/4{,}000`) — i.e. the surrogate-based bound closes the actually-
needed end-to-end inequality, not just the candidate lemma in isolation.

**CRITICAL — asymmetry, do not conflate with the dead `\sigma=+1` mirror.** The naive `\sigma=+1` analogue
of sibling-domination (does `\mathrm{MATCH}_val` ever *strictly* beat `\max(DELETE_val,KEEP_val)` on the
*minimization* side, i.e. Two-Touch's own MATCH branch, using the **true** branch values) — **fails at a
real, non-corner-case rate: `763/6{,}000` random, `28/600` exhaustive**. This is the *documented, already-
open* Two-Touch MATCH-branch difficulty (Match-Branch Domination, §29.1) — Two-Touch's MATCH branch is
handled separately, and correctly, by §29.1's exact reduction to Per-Partner Domination, **not** by any
sibling-domination claim (sibling-domination is FALSE for `\sigma=+1`). **Also distinct from, and not a
duplicate of, a weaker `\sigma=-1` claim that IS already confirmed dead**: a "Mirror Per-Partner
Domination" using a bare scalar proxy `D'_l:=|c-d_l|` in place of the true `KEEP_val` fails
`\approx7$–`15\%` of the time (the parallel match-branch explorer's own secondary finding, §29's sibling
report) — the genuinely new, robust claim above uses the **full recursive `KEEP_val`** (itself an
optimized sub-problem's value, typically far larger than the bare scalar `D'_l`), and this substitution is
exactly what turns the `7$–`15\%` failure into `0/28{,}500`. **Do not report these three claims (Two-Touch
MATCH sibling-domination [false], `\sigma=-1` scalar-proxy Mirror Per-Partner Domination [false,
`\approx7$–`15\%`], `\sigma=-1` true-branch-value sibling-domination [this section's candidate, `0/28{,}
500`]) as the same statement — they are three distinct claims with three distinct (two negative, one
positive-so-far) outcomes.**

**One refuted proof route, recorded so it is not re-attempted.** "Background-value monotonicity"
(`\mathrm{OPT}_{-1}(\{c,y\},X)` non-decreasing in `y`, fixed `c,X`) is **FALSE**, `486/3{,}000`
(`\approx16\%`) — concrete counterexample `c=13,X=[7,5,0]`: value goes DOWN as `y` increases from `2` to
`13`. So the tempting two-step chain ("KEEP's pool `\supseteq` MATCH's pool" [Shrink-List Monotonicity,
already certified] `+` "KEEP's background value `z_1\ge` MATCH's background value `d`" [background-value
monotonicity]) does **not** give a free proof. A real proof must use the specific algebraic relationship
`d=z_1-z_j` together with the pool difference `\{z_j\}` simultaneously — the recommended shape (untested)
is a direct exchange/domination argument comparing an optimal MATCH witness against an explicit KEEP-side
witness built from it (replace `d` by `z_1` in the background, return `z_j` to the pool, argue the
resulting KEEP-side selection dominates), not two separately-proved monotonicity lemmas.

**Status: open, no proof written, strongly corroborated (0 counterexamples, real adversarial effort
including engineered duplicate-cancellation cases) — the single most promising untried angle for finishing
Three-Touch found to date.**

#### 29.3 Gap 1c case (a) narrowed to bounding `delta_c` alone (`delta_d>=0` isolated as a free-standing
sub-target)

Recall case (a)'s setup: `B_1` (size-2 background), `\mathrm{Res}` the residual, `u_1:=\max(\mathrm{Res})`,
partner `u_j`, `d:=|u_1-u_j|`, `X:=\mathrm{Res}\setminus\{u_1,u_j\}`; half-step target
`\mathrm{OPT}_{+1}(B_1,X)\le\mathrm{OPT}_{+1}(B_1\cup\{d\},X)=:RHS`; `\xi^*` the sparsest optimal witness
of the RHS (augmented) problem; case (a) = `\xi^*` nonempty and `B_1\cup\{d\}\cup\xi^*` has no duplicate
value (not Lemma-P-reducible — the genuinely hard residual, cases (b)/(c) already reduce for free,
conditional on Deletion-Suffices-for-`k^*`). The candidate construction: `c:=\arg\min_{x\in\xi^*}|x-d|`,
`M:=B_1\cup(\xi^*\setminus\{c\})`; claim `e(M)\le RHS(=e(M\cup\{c,d\}))`, which trivially implies the
half-step (`M` is a valid `X`-selection, so `\mathrm{OPT}_{+1}(B_1,X)\le e(M)`).

**Decomposition via the certified Insertion-Difference Identity** (`lemmas/insertion-difference-identity.
md`, applied twice, inserting `d` **before** `c`): `e(M\cup\{c,d\})-e(M) = \delta_d+\delta_c`, where
`\delta_d:=e(M\cup\{d\})-e(M)` and `\delta_c:=e(M\cup\{d,c\})-e(M\cup\{d\})`. The claim needs
`\delta_d+\delta_c\ge0`.

**Sub-target 1 (new, appears independently true, recommended to attack FIRST):** `\delta_d\ge0`
unconditionally, for `M=B_1\cup(\xi^*\setminus\{x\})` and **any** `x\in\xi^*` — not just the specific
nearest-choice `c` (round 18's explorer tested both nearest and farthest tie-breaks explicitly and found
`\delta_d\ge0` in every one of `\approx1{,}800` case-(a) checks either way). This suggests `\delta_d\ge0`
is a fact about `B_1\cup(\xi^*\setminus\{\text{anything}\})` and `d` alone — plausibly provable by a
direct parity/rank argument (`\delta_d\ge0\iff h_d:=\#\{x\in M:x>d\}` is even, by the sign rule of the
Insertion-Difference Identity) **without needing the nearest-`c` property at all**. This is a strictly
smaller, self-contained target than the combined two-variable inequality every previous attempt (round
16's two stalled routes, round 17) tried to close in one shot.

**Sub-target 2 (the genuinely hard residual):** `\delta_c` is **negative `\approx94\%$ of the time**
(`1325/1403` checks) — so termwise positivity does NOT explain the sum; nearness of `c` to `d` (i.e.
`|c-d|\le|x-d|` for all `x\in\xi^*`) must be doing real *quantitative* work bounding how negative
`\delta_c` can get, not merely fixing its sign. **This is where all of case (a)'s actual remaining
difficulty lives**, once sub-target 1 is granted: prove `\delta_c\ge-\delta_d`, i.e. bound `\delta_c`'s
magnitude using the nearest-choice property specifically (not a generic insertion fact).

**Two ruled-out leads, do not re-attempt:**
- **Rank-adjacency of `c` and `d`** in the sorted multiset `B_1\cup\{d\}\cup\xi^*` — false in general
  (counterexample `B_1=\{11,12\},\mathrm{Res}=(17,4,3),m=1,d=13,\xi^*=\{3\}`: `d=13` is sorted-adjacent to
  `12\in B_1`, not to `c=3`, because `\xi^*$ has only one element and "nearest" is a forced, vacuous
  choice there). A proof route built on rank-adjacency will not work.
- **The "free bound via the unaugmented full-list problem"** (`\mathrm{OPT}_{+1}(B_1,\mathrm{Res})\le
  RHS`, true and unconditionally `0/14{,}970`, no `\mathcal F`-provenance needed) — provably **cannot**
  close the half-step: by the certified Shrink-List Monotonicity Lemma, `\mathrm{OPT}_{+1}(B_1,
  \mathrm{Res})\le\mathrm{OPT}_{+1}(B_1,X)` (removing list elements only increases OPT), so this free
  fact bounds the *smaller* quantity, the wrong direction to reach `\mathrm{OPT}_{+1}(B_1,X)\le RHS` from
  below. Confirmed dead end, do not re-derive this chaining again.

**Secondary corroborated fact (diagnostic, not yet load-bearing):** across `\approx1{,}558` case-(a)
checks, the margin `RHS-e(M)` was **never exactly `0`** (unlike cases (b)/(c), where equality is exact by
Lemma-P construction) — suggestive that case (a)'s inequality may always be strict, worth keeping in mind
as a sanity check on any future symbolic proof (a proof yielding a tight/`=0` bound in case (a) would be
suspicious and worth re-checking against this data point), but not itself swept for near-ties and not
used in any argument here.

**Also reconfirmed this round (non-vacuity, wider scale):** the dichotomy "case (a)'s `\xi^*` is always
size `\le1`" is **FALSE** — witnesses of size `1`, `2`, and larger were all observed among genuine case-(a)
sparsest witnesses (`/tmp/round-18/gap1c_case_a/`), so case (a) is a genuinely size-unbounded family; the
general (non-enumerable) nearest-`c` construction is the right shape of claim, not an over-engineered one.

#### 29.4 Reconciled priority order and recommended build order for round 18/19

**Priority, closest-to-done first:**
1. **[CERTIFY NOW, cheapest, real closed result]** §29.1's Match-Branch-Domination-via-Per-Partner-
   Domination reduction — a 3-line proof from already-certified/trivial ingredients, ready for the
   builder to write up formally and for the reviewer to certify as a lemma. This *also* delivers a
   genuinely new unconditional result (**Two-Touch fully proved for `|W|\le3`**) essentially for free.
   Retires "Match-Branch Domination" as a separately-tracked open item (folds into Gap 1a's existing
   general-`q` gap).
2. **[HIGH LEVERAGE, most promising untried angle for a long-stuck piece]** Attempt to PROVE §29.2's
   Three-Touch MATCH Sibling-Domination Lemma (`\sigma=-1` only). If closed, this finishes Three-Touch
   (5/5) and, via the already-established non-circular mutual induction, Two-Touch's own remaining KEEP
   `b_0\le w_1` sub-case too — leaving only Gap 1a's general-`q` Per-Partner Domination (item 3 below,
   now doing double duty per item 1) and Gap 1c's case (a) as the population's open items. Recommended
   proof shape: a direct exchange argument (MATCH witness vs. an explicit KEEP-side witness built from
   it), not background-value monotonicity (refuted) and not a re-attempt of the `\sigma=+1` mirror
   (refuted, different statement).
3. **[STANDING TOP PRIORITY, hardest, highest total leverage]** Gap 1a's Per-Partner Domination at
   general `q`, DELETE-vs-MATCH half — unchanged from §27.5 item 1, now doing quadruple duty (Gap 1a
   itself, Gap 1b's DELETE-vs-KEEP half via §27.1, and — new, §29.1 — Two-Touch's MATCH branch at every
   `q`).
4. **[NARROWED, now a concrete 2-step target]** Gap 1c case (a): first attempt `\delta_d\ge0`
   unconditionally (§29.3 sub-target 1, looks independently provable, no nearest-choice hypothesis
   needed) as a self-contained lemma; only then attack `\delta_c\ge-\delta_d$ using the nearest-choice
   property (§29.3 sub-target 2, the genuinely hard residual).
5. Gap 1c case (b) formalization as an explicit corollary — unchanged from §27.5 item 4, cheap, can be
   done alongside anything.

**Recommended build order this round:** item 1 first (near-zero cost, real certified result, immediately
un-blocks a false sense that Match-Branch Domination is separately hard); item 2 next (best risk-adjusted
payoff — closest any MATCH-branch angle has come to a real proof mechanism, not just corroboration);
item 4's sub-target 1 (`\delta_d\ge0`) as a third, independent, low-risk target a separate builder thread
can pursue in parallel with item 2, since it does not depend on item 2 or 3 at all.

**Watch out for (this section, additive to §27.5's existing list):** (i) do NOT write up §29.2 as already
proved — it is corroborated (`0/28{,}500`) but has no algebraic proof yet, only a diagnosed-but-refuted
naive route (background-value monotonicity) and a recommended-but-untested exchange-argument shape; (ii)
do NOT confuse §29.2's `\sigma=-1` true-branch-value sibling-domination with either the dead `\sigma=+1`
mirror (Two-Touch's own MATCH branch, `\approx13\%` failure, handled instead by §29.1) or the dead
`\sigma=-1` scalar-proxy "Mirror Per-Partner Domination" (`\approx7$–`15\%` failure) — three distinct
claims, do not merge their evidence; (iii) §29.1's reduction is airtight but still genuinely depends on
Per-Partner Domination's own open general-`q` gap — do NOT describe Two-Touch's MATCH branch as "closed"
at general `q`, only "reduced to an already-tracked gap, with no new content of its own"; (iv) for §29.3,
`\delta_d\ge0` is a conjecture with zero counterexamples across both tie-break choices, not yet proved —
do not skip straight to `\delta_c` without first attempting `\delta_d` as its own lemma, since a clean
proof of `\delta_d\ge0` would substantially simplify what remains.

**Cases to cover:** none newly introduced this section — §29.1 covers all partners `j` uniformly (the
Per-Partner Domination Lemma is itself per-partner); §29.2 covers all match partners `j` uniformly under
`\sigma=-1`; §29.3's case (a) is itself already one of an exhaustive 3-way split (a)/(b)/(c) established
in §27.3, unchanged here.

### 30. Round 18 build — §29.1 formally proved and certified (Two-Touch fully closed for `|W|\le3`);
§29.2 attempted directly, NOT closed, four new negative results narrow the search space; §29.3's
`\delta_d\ge0` wording corrected to require genuine `\mathcal F`-provenance, `\delta_c` attempted,
still open

All computation this round uses exact `fractions.Fraction` arithmetic and bounded (not unbounded)
search — every script referenced below terminates in seconds. Scripts live in `/tmp/round-18-build/`
(`t1_candC_alone.py`, `t3_candidate.py`, `t4_union.py`, `t5_general_B.py`, `t6_signB_table.py`,
`t7_match2.py`, `t8_candB_alone.py`, `t9_wide_sweep.py`, `t_a_alone.py`, `t_verify_301.py`,
`t_verify_F3.py`, `t_gap1c_free.py`, `t_final.py`, `t_final2.py`, `t_final3.py`), re-derived independently of the round-18 explorers'/outline-reviewer's
own harnesses (a fresh brute-force `e`/`OPT_\sigma` reimplementation, cross-validated first against
this file's own four canonical worked examples: `OPT_{+1}([5,8],(10,8,7,2))=0`,
`OPT_{-1}([5,8],(10,8,7,2))=10`, `OPT_{+1}([1],(10,8,7))=0`, `OPT_{-1}([2,4],(5,3))=4` — all four
reproduced exactly before anything below was trusted).

#### 30.1 [CERTIFIED] Match-Branch-Domination-via-Per-Partner-Domination — full formal proof

**Setting (restated precisely, no change from §29.1/§13.2).** Fix a Two-Touch peeling instance: a
single background element `b_0\ge0` and a sorted list `W=(w_1\ge\dots\ge w_q)`, `q\ge2`. Write
`\mathrm{rest}:=W\setminus\{w_1\}`. By the certified **Generalized Multi-Background Peeling Lemma**
(§13.2, an unconditional identity — not a conjecture — proved by the DELETE/KEEP/MATCH bijections on
the fate of `w_1`, the current max of `W`), for `\sigma=+1`:
```
OPT_{+1}(\{b_0\},W) = min( A_1,\ A_2,\ \min_j A_{3,j} )
```
where `A_1:=\mathrm{OPT}_{+1}(\{b_0\},\mathrm{rest})` (DELETE branch), `A_2` is the KEEP branch's exact
closed form, and `A_{3,j}:=\mathrm{OPT}_{+1}(\{b_0,d_j\},\mathrm{rest}\setminus\{w_j\})` (MATCH branch,
partner `w_j\in\mathrm{rest}`, `d_j:=w_1-w_j`) — this is *literally* the definition
`\mathrm{MATCH}_j:=A_{3,j}` used throughout §26–§29. Write `TT:=\mathrm{TwoTouch}(\{b_0\},W)` for
Two-Touch's closed-form candidate value (the file's own `\max`/`\min` of finitely many touch-`\le2`
expressions, §26.1). The already-**unconditionally proved** facts this proof cites, each already
certified elsewhere in this file with no dependency on anything in this section:

- **(F1) DELETE branch domination**, §26.5(b): `A_1\ge TT(\{b_0\},W)`, proved as the **inductive step**
  of the overall strong induction on `|W|` (via candidate-set inclusion:
  `\mathrm{TwoTouch}(\{b_0\},\mathrm{rest})`'s own candidate list is a subset of `\mathrm{TwoTouch}
  (\{b_0\},W)`'s, so `\mathrm{TwoTouch}(\{b_0\},\mathrm{rest})\ge\mathrm{TwoTouch}(\{b_0\},W)=TT`
  unconditionally, needing no hypothesis at all; combined with the **induction hypothesis** `A_1=
  \mathrm{OPT}_{+1}(\{b_0\},\mathrm{rest})=\mathrm{TwoTouch}(\{b_0\},\mathrm{rest})` — i.e. Two-Touch's
  full equality already established at the strictly smaller size `|\mathrm{rest}|=|W|-1` — gives
  `A_1\ge TT`). **This is available whenever Two-Touch's equality is already proved at size `|W|-1`; in
  particular, at `|W|=3` it is invoked with `|W|-1=2`, the already-certified base case (§26 (a) above),
  so no circularity or unproved dependency is introduced at the size this section actually uses.** This
  step uses no MATCH-branch fact of any kind, and in particular does not depend on §29.1's own claim
  below, on Per-Partner Domination, or on Three-Touch — **traced by hand this round, confirmed
  non-circular.**
- **(F2) `D_j:=|b_0-d_j|=e(\{b_0,d_j\})\ge TT` by definition, no proof needed.** `\mathrm{TwoTouch}
  (\{b_0\},W)`'s own candidate list is defined (§26.1) to include, for every `j`, the touch-`2` term
  `e(\{b_0,d_j\})` (matching `w_1,w_j`) as one of the finitely many quantities the closed form takes a
  `\max`/`\min` over. Since `TT` is (by definition) the extremal value of that finite list, and
  `e(\{b_0,d_j\})=D_j` is a member of that list, `TT\le D_j` follows immediately from the definition of
  a `\min`/`\max` over a list containing that member — no computation, no case analysis.
- **(F3) Per-Partner Domination Lemma** (`\S21.3`, certified for `q\le3`; open, corroborated, for
  `q\ge4$): for every index `l` of a base instance `(B_0=\{b_0\},Z_0)$ with `A_1:=\mathrm{OPT}_{+1}
  (B_0,Z_0\setminus\{z_1\})`, `d_l:=z_1-z_l`, `D_l:=|b_0-d_l|`, `A_{3,l}:=\mathrm{OPT}_{+1}(B_0\cup
  \{d_l\},Z_0\setminus\{z_1,z_l\})`, **with no trigger hypothesis and no requirement that `l` be any
  kind of argmin**:
  ```
  A_{3,l} \ge \min(A_1,D_l).
  ```
  This statement is **fully general** — it is a claim about *arbitrary* `(B_0,Z_0)`, not restricted to
  any generative provenance family `\mathcal F` (confirmed by re-reading its exact statement, §21.3:
  "with no trigger hypothesis and no requirement that `l` be an argmin of anything" — the qualifier is
  explicit in the lemma's own text). So the `q\le3` sub-case is an unconditional theorem usable in any
  context, not merely within `\mathcal F`.

**Lemma (Match-Branch-Domination-via-Per-Partner-Domination).** For every partner `j\in\{1,\dots,q-1\}`
(indexing `\mathrm{rest}`, i.e. every `w_j\in\mathrm{rest}$),
```
MATCH_j \ge TT,
```
**conditional only on Per-Partner Domination** (F3) **at the specific size `q_{\mathrm{sub}}:=|W|`
(the size of the base instance whose top element `w_1` is being peeled) and specific index `l=j`.**

**Proof.** The renaming `B_0:=\{b_0\}`, `Z_0:=W`, `z_1:=w_1`, `l:=j` (so `d_l=d_j`, `A_1$ in F3's own
notation is *the same object* as Two-Touch's DELETE-branch quantity, since both are defined as
`\mathrm{OPT}_{+1}(\{b_0\},\mathrm{rest})` with `\mathrm{rest}=Z_0\setminus\{z_1\}=W\setminus\{w_1\}`)
is a literal identification, not an analogy — every symbol on both sides denotes the identical
mathematical object once the renaming is applied; there is no reinterpretation, approximation, or
scope-narrowing anywhere in this step. Under this renaming, F3 reads exactly:
```
MATCH_j = A_{3,j} \ge \min(A_1, D_j).
```
By (F1), `A_1\ge TT`; by (F2), `D_j\ge TT`. A minimum of two quantities each individually `\ge TT` is
itself `\ge TT$ (elementary: if `x\ge TT$ and `y\ge TT$ then `\min(x,y)\ge TT`, since `\min(x,y)$ equals
whichever of `x,y` is smaller, and that one is still `\ge TT` by hypothesis). Hence `\min(A_1,D_j)\ge
TT`, and combining with the displayed inequality, `MATCH_j\ge TT`. `\blacksquare`

**Corollary (unconditional, no hypothesis beyond the `q\le3` case of F3 already being certified): Two-
Touch is fully, unconditionally proved for `|W|\le3`.** By the trichotomy, `OPT_{+1}(\{b_0\},W)=\min(A_1,
A_2,\min_j A_{3,j})`. At `|W|=3`: the MATCH branch's own sub-instance has base size `q_{\mathrm{sub}}=
|W|=3` (the renaming above identifies Two-Touch's ambient `|W|` with F3's own `q`, since F3 is applied
with `Z_0=W` directly, not to a smaller residual) — exactly the regime where F3 is **already
unconditionally proved** (§21.3, `q\le3`), so the Lemma above applies with no open hypothesis, giving
`MATCH_j\ge TT` for every `j`, hence `\min_j A_{3,j}\ge TT`. Combined with `A_1\ge TT` (F1's inductive
step, invoked here with the induction hypothesis at `|W|-1=2` — the already-certified base case, so
available with no open dependency at this size) and the already-unconditional KEEP branch (`A_2\ge TT`: the `b_0>w_1`
sub-case is unconditional at every `|W|`, §26.5(c); the `b_0\le w_1` sub-case at `|W|=3` needs
Three-Touch at size `|W|-1=2`, which Lemma B —§28.4(a), certified this population's own
`lemmas/max-element-triple-identity-and-threetouch-basecase.md` — already proves unconditionally, `|W|
\le3` being comfortably within its scope), **all three branches of the `|W|=3` trichotomy are
unconditionally `\ge TT`**, so `OPT_{+1}(\{b_0\},W)\ge TT`. Combined with the already-known reverse
inequality (`TT` is itself achieved by one of the trichotomy's own candidates, so `OPT_{+1}(\{b_0\},W)
\le TT$ always, unconditionally, by construction of the closed form as a `\min` over genuinely
achievable selections — this direction needs no new argument, it is how `\mathrm{TwoTouch}` was
defined to begin with), `OPT_{+1}(\{b_0\},W)=TT` exactly, for every `|W|\le3`. **This strictly extends
the previously-proved base case (`|W|\le2`, §26 base case) by one full level, via genuinely new content
this round.**

**[ROUND-18 PROOF-REVIEWER CORRECTION — this Corollary as stated above is an OVERCLAIM, do not treat it
as proved.]** The parenthetical "the `b_0\le w_1` sub-case at `|W|=3` needs Three-Touch at size `2`,
which Lemma B … already proves unconditionally" is a **non sequitur**: Lemma B proves the *value*
`\mathrm{OPT}_{-1}(\{b_0\},\mathrm{rest})=\mathrm{ThreeTouch}(b_0,\mathrm{rest})` for `|\mathrm{rest}|
\le3`; it does **not** prove the actually-needed inequality `w_1-\mathrm{ThreeTouch}(b_0,\mathrm{rest})
\ge\mathrm{TwoTouch}(\{b_0\},W)`, which is a different claim about a `\sigma=+1` KEEP branch dominating
`TT`, not a statement about `\mathrm{OPT}_{-1}`'s value. §27.2(d) (round 17) explicitly logged this exact
inequality as "corroborated `0/1{,}239`, not proved" and it remains exactly that: the proof-reviewer
independently re-tested it with fresh code (`0` failures across `>14{,}000` combined trials, including a
true-brute-force-`OPT` cross-check and a wide-value-range sweep to `v_{\max}=500`) — strongly
corroborated, **still not proved**. Consequently `A_2\ge TT$ at the `b_0\le w_1` sub-case is **NOT
established**, so the claim "all three branches of the `|W|=3` trichotomy are unconditionally `\ge TT`"
and "`OPT_{+1}(\{b_0\},W)=TT` exactly, for every `|W|\le3`" **do not follow** from what is proved above.
**What IS correctly established: Two-Touch's MATCH branch alone is closed at `|W|=3` (and at any `q`
where Per-Partner Domination is proved) — Two-Touch itself remains open at `|W|=3`, pending the KEEP
`b_0\le w_1` sub-case.** See `lemmas/match-branch-domination-via-per-partner-domination.md`'s "Scope
note" for the certified, narrowed version of this Lemma and a concrete recommended next attempt.

**Open dependency, stated with maximal precision (corrected/sharpened from an earlier, slightly looser
draft of this paragraph).** The Lemma's own proof combines F3 (Per-Partner Domination at `q_{\mathrm{sub}}
=|W|`) with F1 and F2. F2 is free at every size, no hypothesis. **But F1 (`A_1\ge TT`) is itself only the
*inductive step* of Two-Touch's own overall strong induction** (proved above to require, as its own
hypothesis, that Two-Touch's full equality already holds at the strictly smaller size `|W|-1`) — so the
Lemma's conclusion `\mathrm{MATCH}_j\ge TT` at a given `|W|=q_{\mathrm{sub}}\ge4` is available **only once
Two-Touch has already been fully closed at `|W|-1`**, which itself requires the SAME joint machinery
(Three-Touch for KEEP, Per-Partner Domination for MATCH) at every level below `|W|-1` too — exactly the
same well-founded, level-by-level joint-induction structure the outline-reviewer flagged this round as a
forward-looking requirement for any future proof combining these two lemmas, and the same structure
already verified for the Two-Touch/Three-Touch mutual induction itself (§28.4(d)). **Precisely stated:
closing Per-Partner Domination at a given `q`, PROVIDED the rest of the joint induction (Three-Touch's own
MATCH branch, and Per-Partner Domination itself, at every smaller size) has already closed, finishes
Two-Touch's MATCH branch at that `q` with no further content of its own.** It is *not* a claim that
Per-Partner Domination alone, isolated from the rest of the joint induction, suffices at an arbitrary
single level — that weaker, isolated reading would be an overclaim, and is explicitly NOT what is proved
here. This does **not** close Per-Partner Domination itself at `q\ge4` (still open, corroborated only),
and does **not** close Two-Touch at `q\ge4` (which also needs the KEEP `b_0\le w_1` sub-case, i.e.
Three-Touch's own still-open MATCH branch, per §28.4(d)'s mutual induction, at every level up to `|W|-1`
— an entirely separate, still-open dependency, unaffected by this section). **Any future round that
invokes this Lemma at general `q` must verify the full level-ordering explicitly (Two-Touch and
Three-Touch both closed through `|W|-1` before invoking F1 and the Lemma at `|W|`), exactly as the
outline-reviewer's report requested — this paragraph is that explicit verification requirement, now
recorded on file rather than left implicit.**

**Independent computational re-verification this round (fresh code, `/tmp/round-18-build/
t_verify_301.py` and `t_verify_F3.py`, validated against the four worked examples first — see
preamble; this harness is written independently, not reused from the round-18 explorers or the
outline-reviewer):**
- **The underlying Generalized Multi-Background Peeling Lemma trichotomy identity itself** (§13.2,
  already certified, `\mathrm{OPT}_{+1}(\{b_0\},W)=\min(A_1,A_2,\min_jA_{3,j})$, an unconditional
  identity, re-verified as a harness sanity check before trusting anything downstream): **`0/400`**
  random (`|W|\le5,v_{\max}\le8`) plus **`0/625`** fully exhaustive (`|W|=3$, all of `b_0,w_1,w_2,w_3\in
  \{0,\dots,4\}`) — both `0` mismatches, confirming the harness and re-confirming the already-certified
  identity independently.
- **F3 (Per-Partner Domination) restated verbatim in Two-Touch's own variables**, re-derived and
  re-tested from scratch (not merely cited): random sweep `q\in\{3,4,5\}$, `v_{\max}=6`: **`0/1{,}837`**;
  fully **exhaustive** `q=4` on the 5-value grid `\{0,1,2,3,4\}`: **`0/9{,}375`** (every `(b_0,W)`
  combination on that grid, all partners `j`, not sampled) — matches the population's standing
  "unconditionally proved `q\le3`, corroborated with zero known counterexample at `q=4$" status; no new
  failure found, no new proof of the open `q\ge4` case either (consistent with the "Open dependency"
  paragraph above).
- The trivial ingredient (F2, `D_j\ge TT` by definition of `TT` as a `\min` over a list containing
  `D_j`) needs no computational check — it is a one-line consequence of how `\mathrm{TwoTouch}` is
  defined (§26.1), not an empirical claim.
- **The `|W|\le3` Corollary itself was independently checked via the identity, not via a separately
  re-implemented `\mathrm{TwoTouch}` closed form** (this round's harness does not carry an independent
  reimplementation of §26.1's exact candidate-list closed form, only the raw trichotomy `\mathrm{OPT}`):
  since `TT\ge\mathrm{OPT}_{+1}$ always holds by construction (`TT` is the value of one particular,
  always-achievable selection drawn from `\mathrm{TwoTouch}`'s own candidate list, so it can never be
  *below* the true optimum), and the Lemma above shows `A_1,A_2,A_{3,j}\ge TT` for every branch at `|W|
  \le3` (citing already-certified §26.5(b)/(c), Lemma B, and F3 at `q\le3`), the already-reverified
  identity `\mathrm{OPT}_{+1}=\min(A_1,A_2,\min_jA_{3,j})\ge TT` combines with `TT\ge\mathrm{OPT}_{+1}`
  to force equality — this chain of reasoning is exact and needs no further numerical check beyond the
  identity and F3 sweeps already reported; a future round independently re-implementing `\mathrm{TwoTouch}`'s
  own closed form from §26.1 could add a fully independent third check of the headline equality, but this
  is not required for the proof's validity (the argument above is already complete and rigorous, only
  the *convenience* of an extra numerical cross-check is unavailable this round for lack of time to
  re-implement §26.1's closed form independently).

**Certification verdict for this subsection [ROUND-18 PROOF-REVIEWER: REVISED].** The Lemma
(Match-Branch-Domination-via-Per-Partner-Domination, i.e. `MATCH_j\ge\min(A_1,D_j)\ge TT`) IS a complete,
rigorous proof, each step either a literal renaming, an already-certified citation (F1, F2 by definition,
F3 at `q\le3`), or an elementary one-line fact about `\min` — **certified**, no `\mathcal
F`-provenance-specific machinery needed, general statement about arbitrary `(b_0,W)`. **The Corollary
("Two-Touch unconditionally proved for `|W|\le3`") is NOT a complete proof — REJECTED as submitted**; see
the correction note above and `lemmas/match-branch-domination-via-per-partner-domination.md`'s "Scope
note" for the precise missing inequality. Only the narrower Lemma (without the Corollary clause) is filed
below as a promotable, certified general-purpose result (see "Promotable lemmas").

#### 30.2 [ATTEMPTED, NOT CLOSED] Three-Touch MATCH Sibling-Domination Lemma (`\sigma=-1`) — four new
negative results narrow, but do not close, the search for a proof

**Restating the target precisely (§29.2).** For background singleton `c\ge0`, sorted list
`Z=(z_1\ge\dots\ge z_q)`, `\mathrm{rest}:=Z\setminus\{z_1\}`:
```
DELETE_val := OPT_{-1}(\{c\}, rest),           KEEP_val := OPT_{-1}(\{c,z_1\}, rest),
MATCH_j     := OPT_{-1}(\{c, d_j\}, rest\setminus\{z_j\}),   d_j := z_1-z_j,   MATCH_val:=\max_j MATCH_j.
```
Claim: `MATCH_val \le \max(DELETE_val, KEEP_val)`.

**Attempt 1 (three "obvious" exchange constructions, tried and refuted individually and jointly).**
Fix an optimal witness `T` (a value-multiset achieved by some selection of `\mathrm{rest}\setminus
\{z_j\}`) for the `\mathrm{MATCH}_j` sub-problem, so `\mathrm{MATCH}_j=e(\{c,d_j\}\cup T)`. Three
candidate alternative selections of `\mathrm{rest}` (reusing the *same* `T` on `\mathrm{rest}\setminus
\{z_j\}$, differing only in how `z_1,z_j` are handled) give three free lower bounds:
```
(a) delete z_j, delete z_1:     e({c}\cup T)         \le DELETE_val
(b) delete z_j, keep z_1:       e({c,z_1}\cup T)      \le KEEP_val
(c) keep z_j,   keep z_1:       e({c,z_1,z_j}\cup T)  \le KEEP_val
```
Each individual inequality (a)/(b)/(c) is a legitimate one-line "restriction of the search space" fact
(the right-hand quantity's own defining optimization ranges over the RHS selection space, which
literally contains the specific selection just described, so its optimum dominates that one selection's
value) — no computation needed, each is a valid **lower bound tool**. If the *union* `\max(\text{(a)},
\text{(b)},\text{(c)})\ge\mathrm{MATCH}_j` held as a **pure fact about `T,c,z_1,z_j` alone** (for
arbitrary `T\subseteq[0,z_1]$, `z_1\ge z_j\ge0`, any `c\ge0` — i.e. without using that `T` is
specifically an *optimal* witness of `\mathrm{MATCH}_j`'s own sub-problem), this would immediately
close the whole target. **This union bound is FALSE** — tested directly (`/tmp/round-18-build/
t4_union.py`, generalizing the round-18 explorer's own approach with a wider sweep): `3518/40000`
(`\approx8.8\%`) failures with `T$'s elements independently drawn from `[0,z_1]$ (not required to arise
from a genuine `\mathrm{MATCH}_j` witness), e.g. `c=1,z_1=4,z_j=1,d=3,T=\{4,1,3\}`: `e(\{1,3\}\cup T)=4 >
\max(e(\{1\}\cup T),\,e(\{1,4\}\cup T),\,e(\{1,4,1\}\cup T))=\max(1,3,2)=3`. **Each individual candidate
is also separately falsified as a stand-alone sufficient bound** (three fresh, separately-run tests,
`/tmp/round-18-build/t_a_alone.py`, `t1_candC_alone.py`, `t8_candB_alone.py`): (a) alone
(`e(\{c\}\cup T)\ge\mathrm{MATCH}_j`, i.e. is `\mathrm{MATCH}_j\le\text{DELETE-candidate}` always) fails
**`7573/20000`** (`\approx38\%`); (c) alone (`e(\{c,z_1,z_j\}\cup T)\ge\mathrm{MATCH}_j`, "keep both")
fails **`4121/20000`** (`\approx21\%`); (b) alone (`e(\{c,z_1\}\cup T)\ge\mathrm{MATCH}_j`, "keep `z_1`
only") fails **`13327/40000`** (`\approx33\%`) — all three individually far too weak, exactly mirroring
why the TRUE quantities `DELETE_val,KEEP_val` (each an optimum over a MUCH larger search space than the
single fixed-`T` candidate) are needed, not these single-witness proxies.

**Diagnosis.** These failures show the true proof (if one exists) cannot proceed by fixing `T$ and
comparing symbolically without using `T`'s own **optimality** for the `\{c,d_j\}` sub-problem — the
genuine content must come from `T` itself being extremal, not from generic bounds on an arbitrary
fixed multiset. This rules out an entire naive-exchange proof strategy (any argument of the shape
"reuse the same residual selection, only reroute `z_1,z_j`"), a decisive negative result narrowing
future attempts away from this whole family.

**Attempt 2 (generalize background size, seeking an inductive route).** Tested whether the **general**
version (arbitrary background size `|B|$, not just `1`) of the candidate holds — `\mathrm{MATCH}_val:=
\max_j\mathrm{OPT}_{-1}(B\cup\{d_j\},\mathrm{rest}\setminus\{z_j\})\le\max(\mathrm{OPT}_{-1}(B,
\mathrm{rest}),\mathrm{OPT}_{-1}(B\cup\{z_1\},\mathrm{rest}))$ for arbitrary background multisets `B`.
**FALSE**: `64/3217` (`\approx2\%`) failures across `|B|\in\{0,1,2,3\}$
(`/tmp/round-18-build/t5_general_B.py`), e.g. `B=\{3,2\},Z=(3,1)`: `\mathrm{DEL}=2,\mathrm{KEEP}=2,
\mathrm{MATCH}=3`. **This rules out any induction that tries to generalize the target to larger
backgrounds as an intermediate step** — `|B|=1` is genuinely special, not an arbitrary restriction one
could relax for convenience. Isolating exactly which background sizes hold or fail (fresh finding this
round, `/tmp/round-18-build/t6_signB_table.py`, `\ge3000` trials per cell):
```
|B|=0, sigma=-1:  HOLDS (0/3325)        |B|=0, sigma=+1:  HOLDS (0/3265)
|B|=1, sigma=-1:  HOLDS (0/3341, and a further 0/20758 wider sweep, q<=8 -- see below)
|B|=1, sigma=+1:  FAILS (259/3321, ~7.8%) -- this IS Two-Touch's own MATCH branch, already
                    handled separately and correctly by §30.1/§29.1, not attempted here
|B|>=2, both signs: FAILS (subsumed in the 64/3217 general sweep above)
```
The `|B|=0` fact (both signs) is new — not previously recorded on file — but its relationship to the
`|B|=1,\sigma=-1$ target is **not** a simple base case of a size-induction (a literal induction from
`|B|=0` to `|B|=1$ would need to pass through, or otherwise avoid, the `|B|=2` regime shown false above,
since a naive "peel the match-branch's own residual" step raises the background size by one at each
level); no such induction route was found working this round. Recorded honestly as a fact that MAY be
useful to a future attempt, not as progress toward a proof.

**Attempt 3 (does matching the second-largest partner dominate all others?).** Tested whether
`\mathrm{MATCH}_2$ (matching `z_1` with the immediately-next element `z_2`) is always the arg-max
partner, which would let a proof focus on one fixed partner instead of a `\max` over all `j`. **FALSE**:
`3458/8005$ (`\approx43\%`) of instances have some other partner strictly beating `\mathrm{MATCH}_2`
(`/tmp/round-18-build/t7_match2.py`) — the arg-max partner can be arbitrarily deep in the list, ruling out this
simplification.

**Positive corroboration, wider than any prior round (fresh, this round only, no route to a proof
found):** direct re-test of the true target itself (both branch values via full brute-force
`\mathrm{OPT}_{-1}`, not any of the refuted proxies above), `|Z|\in\{1,\dots,8\}`,
`v_{\max}\in\{4,\dots,8\}`: **`0/20{,}758`** failures (`/tmp/round-18-build/t9_wide_sweep.py`), combined with the
`0/3{,}341$ narrower sweep above: **`0/24{,}099`** total fresh failures this round, on top of the
population's already-reported `0/28{,}500` (round-18 explorers) and `0/400`+`0/400`+`0/999`
(outline-reviewer) — a fourth independent codebase corroborating zero counterexamples, no new failure
mode found anywhere.

**Honest status: NOT PROVED.** Despite four distinct fresh attempts this round (three refuted
proof-route candidates, one further-corroborating direct sweep), no proof mechanism was found. The
population's standing recommendation — a direct exchange/domination argument comparing an optimal MATCH
witness `T` against an explicit, **T-dependent** (not fixed-shape) KEEP-side witness, likely requiring
induction on `T`'s own recursive DELETE/KEEP/MATCH decomposition rather than treating `T` as an opaque
fixed multiset — remains the best untried lead, now with three additional concretely-refuted naive
alternatives (union-of-three-candidates; general-background induction; second-largest-partner
reduction) removed from consideration for the next round. This is genuine, precisely-scoped negative
progress (narrowing what a correct proof can look like), not a closure — §29.2/§30.2's target remains
open, exactly as before this round, with a strictly smaller remaining search space of plausible proof
strategies.

#### 30.3 Gap 1c case (a): `\delta_d\ge0` wording corrected to require genuine `\mathcal F`-provenance
(per outline-reviewer); `\delta_c` attempted, remains open

**Wording correction (mandatory per the outline-reviewer's finding, reproduced and confirmed this
round).** §29.3's original phrasing ("This suggests `\delta_d\ge0` is a fact about `B_1\cup(\xi^*
\setminus\{\text{anything}\})` and `d` alone... plausibly provable... without needing the nearest-`c`
property at all") is corrected here to state explicitly: **`\delta_d\ge0` is FALSE in general once
genuine `\mathcal F`-provenance is dropped, even holding the exact same construction shape fixed**
(`M:=B\cup(\xi^*\setminus\{x\})`, `\xi^*` any genuine sparsest optimal witness of
`\mathrm{OPT}_{+1}(B\cup\{d\},X)` for *arbitrary* `(B,X,d)`, not required to descend from a real
trigger+global-argmin instance). **Re-derived and re-confirmed this round** (`/tmp/round-18-build/
t_gap1c_free.py`, fresh instances, arbitrary `(B,X,d)` with `|B|=2`, `\xi^*` computed by brute force as
the genuine sparsest optimum, no `\mathcal F`-generator used at all): **`148/944\approx15.7\%`**
failures — the same order of magnitude as the outline-reviewer's independently-found
`178/1050\approx17\%`, confirming (a third time, via a third independent harness) that `\delta_d\ge0`
needs `\mathcal F`-provenance and is not a provenance-free structural fact about the `(B,\xi^*,d)` shape
alone. **Every future attempt to prove `\delta_d\ge0` (or, downstream, `\delta_c\ge-\delta_d`) must
explicitly invoke genuine `\mathcal F`-provenance** (the outer trigger `M<A_1` and `k^*`'s global-argmin
property that produced `B_1=\{b_0,d_{k^*}\}` and `\mathrm{Res}` in the first place) as a hypothesis, not
attempt a symbolic proof that only uses the shapes of `B_1,\xi^*,d`.

**Re-confirmation within genuine `\mathcal F`-provenance, plus a new structural finding.** Reusing the
round-17/round-18 explorer's own `\mathcal F`-generator (`/tmp/round-17/gap1c_probe/harness.py`'s
`find_F_instance`, read and manually verified to enforce a real trigger `M<A_1` and a real global-argmin
`k^*` before trusting it — the same generator independently audited by this round's outline-reviewer and
the case-(a) explorer), ran three independent sweeps (`/tmp/round-18-build/t_final.py`,
`t_final2.py`, `t_final3.py`, different random seeds, combined `949` genuine case-(a) instances,
`q\in\{4,\dots,8\},v_{\max}\in\{8,\dots,50\}`): **`0/949`** show `\delta_d<0$ (nearest-`c` tie-break) —
consistent with, and adding three more independent data points to, the population's now-repeated
(round-18 explorer `0/155`+`0/1{,}800` combined, outline-reviewer `0/155`, here `0/949`) finding that
`\delta_d\ge0` holds throughout genuine `\mathcal F`-provenance. **New this round: `h_d:=\#\{x\in M:x>d\}`
was EVEN in every single one of the `949` instances (`949/949`, zero odd occurrences)** — a cleaner,
previously-undocumented structural fact, not the "roughly evenly split" pattern one might have expected
absent any check.

**Attempted proof of `\delta_d\ge0` within `\mathcal F`-provenance — not completed, but narrowed by the
new parity finding.** By the Insertion-Difference Identity (certified, general, no provenance needed):
`\delta_d=(-1)^{h_d}(d-2e(\mathrm{tail}_d(M)))`, `h_d:=\#\{x\in M:x>d\}`, `\mathrm{tail}_d(M):=\{x\in
M:x\le d\}`. If `h_d` is **always** even within genuine case-(a) `\mathcal F`-provenance (corroborated,
`949/949`, but **not proved** — no argument was found this round for why `h_d` must be even, only
computational confirmation), then `\delta_d\ge0` **reduces to the single inequality**
`d\ge2e(\mathrm{tail}_d(M))`, with **no parity case-split needed at all** — a genuinely simpler target
than what §29.3 anticipated (which expected to need both parities). This is real progress on how to
*state* the remaining sub-lemma, even though neither "`h_d` is always even within `\mathcal
F`-provenance case (a)" nor "`d\ge2e(\mathrm{tail}_d(M))`" was proved this round — both remain open,
corroborated conjectures. An attempt to prove `d\ge2e(\mathrm{tail}_d(M))$ directly via `M`'s minimality
(i.e. `B_1\cup\xi^*\cup\{d\}` is optimal for the augmented problem `\mathrm{OPT}_{+1}(B_1\cup\{d\},X)`, so
no cheaper selection of `X` exists) by trying to exhibit an *alternative*, explicit selection of `X` built
from `\mathrm{tail}_d(M)`'s own elements — **not completed**: the obstruction is that `\mathrm{tail}_d(M)`
is a set of *values* (some from `B_1`, which is not part of `X` at all and so cannot be "reselected," some
from `\xi^*`, whose underlying raw elements of `X` are not tracked once we work purely at the value level)
rather than a set of raw list elements, so there is no immediate way to turn a value-level bound into a
concrete competing selection of `X` without re-deriving which raw elements of `X` gave rise to each value
in `\mathrm{tail}_d(M)$ — a genuine, precisely-identified translation gap, the same one that blocks
`\delta_c`'s bound below.

**`\delta_c` — attempted, remains fully open.** Re-confirmed `\delta_c<0` in the large majority of genuine
case-(a) instances (same `949`-instance combined sweep: **`876/949\approx92.3\%`**, consistent with the
file's previously-cited `\approx94\%` and the outline-reviewer's `100/100`). Tested two candidate
closed-form magnitude bounds for `\delta_c` motivated by the nearest-choice property `|c-d|\le|x-d|\,
\forall x\in\xi^*` (on the `419`-instance sub-sample from `t_final2.py`+`t_final3.py` that recorded
these specific bound checks): (i) `|\delta_c|\le|c-d|` — **FALSE**, **`285/419\approx68\%`** violations
(`\delta_c` is very often much more negative than `|c-d|` alone would allow); (ii) `|\delta_c|\le2|c-d|`
— also **FALSE**, **`206/419\approx49\%`** violations (a smaller but still large and clearly nonzero
failure rate, ruling out this natural doubling too). **Both candidate bounds fail at a substantial,
non-corner-case rate** — considerably worse than initially hoped — confirming that a correct bound on
`\delta_c` cannot be a simple function of `|c-d|` alone; **the true relationship needed
(`\delta_c\ge-\delta_d`) genuinely couples `\delta_c` to `\delta_d`/`M`'s other elements, not just to the
nearest-choice gap `|c-d|`**, sharpening (in the negative direction — ruling out two natural guesses) what
the file previously described as "nearness must be doing real quantitative work." **No proof of the
combined margin `\delta_d+\delta_c\ge0` was found this round.** The combined margin itself was
re-confirmed never negative in the full `949`-instance sweep (**`0/949`**, minimum margin `1`, integer
alphabets throughout this round's generator — consistent with, though not the same numeric value as, the
outline-reviewer's own `0/100`, min margin `1/2`, from a differently-parametrized rational-alphabet
sweep), consistent with all prior rounds — corroboration only, not a proof.

**Status of §29.3/§30.3: open.** Sub-target 1 (`\delta_d\ge0`) is now precisely and correctly scoped as
provenance-dependent (wording fixed, third independent confirmation of the necessity of `\mathcal
F`-provenance, one concrete obstruction to a direct proof identified — the value-to-selection
translation step). Sub-target 2 (`\delta_c`'s magnitude bound) had two natural closed-form candidates
tested and refuted this round, narrowing (slightly) what a correct bound could look like, but with no
proof found. Case (a) of Gap 1c's half-step remains open.

#### 30.4 Net verdict for this round's build

**[ROUND-18 PROOF-REVIEWER: this paragraph's "Two-Touch fully proved for `|W|\le3`" claim is an overclaim,
corrected above at §30.1 — do not treat Two-Touch as closed at `|W|=3`.] No gap is fully closed among
§29.2 (Three-Touch MATCH sibling-domination) or §29.3 (Gap 1c case (a)). §30.1
(Match-Branch-Domination-via-Per-Partner-Domination) is a complete, certified proof **of the MATCH-branch
reduction only** (`MATCH_j\ge TT` conditional on Per-Partner Domination), correctly, precisely reducing
Two-Touch's general-`q` MATCH branch to Per-Partner Domination's own already-tracked general-`q` gap
(together with the already-tracked joint-induction level-ordering requirement made explicit this round) —
no new open item is created, one is formally closed as "not independent content, given the rest of the
joint induction already closes at every smaller level." **Two-Touch itself remains open even at `|W|=3`
— the KEEP `b_0\le w_1` sub-case's needed inequality is still only corroborated, not proved (Lemma B does
not supply it, contrary to this round's original draft of this section).** §29.2 remains the
single most promising untried angle for finishing Three-Touch (still `0` counterexamples across the
population's now `\approx54{,}000+` combined trials, four new refuted proof-route candidates this round
narrowing future search), but no proof exists yet. §29.3's `\delta_d\ge0` wording is corrected to be
provenance-dependent (a genuine rigor fix, not merely cosmetic — the previous phrasing was one misreading
away from a false provenance-free claim, exactly the failure pattern flagged repeatedly in
`run_state.md`'s Rules), and `\delta_c` has two more candidate bounds ruled out, still fully open.
Two-Touch and Three-Touch both remain not-fully-closed (MATCH branches open in both, though Two-Touch's
is now a pure corollary of an already-tracked gap rather than separate content); Gap 1a's general-`q`
Per-Partner Domination, Gap 1b's general induction (subsumed in Per-Partner Domination per §27.1), and
Gap 1c's case (a) all remain open. **Status correctly stays `partial`.**

## §31 (round 19, proof-outliner reconciliation of `math-explorer-general-q.md`): a candidate
closed-form Generalized Touch-Bound Lemma at `|C|=2`, offering a non-inductive-in-`q` route to
Per-Partner Domination's general-`q` gap

**Status: CONJECTURAL / CORROBORATED ONLY, not proved.** Everything in this section is reported as a
candidate lemma with strong computational support (>10,000 combined trials this round, 0 counterexamples
at the claimed threshold) — the outliner has NOT independently re-derived it algebraically (only spot-
checked the pigeonhole-style threshold-identification logic in the explorer's report and confirmed no
internal contradiction). Treat every claim below as "corroborated, not proved" until a builder either
proves it or finds a counterexample.

### 31.1 The conjecture

**Generalized Touch-Bound Lemma (conjectural).** For background `C` with `|C|=k` and list `W`:
```
OPT_{+1}(C,W) = min over selections of W touching <= 2k raw elements, of e(C u kept u match-diffs)
OPT_{-1}(C,W) = max over selections of W touching <= 2k+1 raw elements, of the same
```
where "touching `j` elements" means Keep-set-size plus twice the Match-pair-count equals `j`. At
`k=1` this is exactly the already-certified Two-Touch closed form (`\sigma=+1`) and the corroborated
Three-Touch candidate (`\sigma=-1`) — both already on file (§21-§30). This section's new content is
`k=2` (the case `A_{3,l}=OPT_{+1}(\{b_0,d_l\},\mathrm{Res})` itself needs, since `A_{3,l}` is exactly a
`|C|=2` instance), with threshold `2k=4` (NOT `k+2=4`-coincidentally-equal-at-`k=2` — the explorer
pinned this down by testing `k=3`, where `2k=6\ne k+2=5` separates the two candidates and `2k=6` wins).

### 31.2 Why this is a genuinely different route from the round 14-18 induction-on-`q` attempts

Every prior Per-Partner Domination attempt (rounds 14-18) inducts on `|Res|` (`q`), peeling `Res`'s top
element via the certified Generalized Multi-Background Peeling Lemma — this forces the MATCH branch to
recurse into a **3-element** background (`\{b_0,d_l,e_i\}`) at the next level, growing unboundedly as
the induction proceeds (§27.1's own diagnosis: "MATCH carries forward the full difficulty of the problem,
unreduced"). The Generalized Touch-Bound Lemma instead fixes `|C|=k` and inducts (if provable) on `k`
itself, treating `|W|` as free from the start — if proved for `k=2`, Per-Partner Domination's DELETE-vs-
MATCH mechanism reduces to ONE finite (`O(q^4)`), `q`-independent case analysis, with no induction on `q`
in that half of the argument at all.

### 31.3 Skeleton for a future proof attempt (not attempted this round — this is the open gap)

**Technique:** strong induction on `|C|` (not `|W|`), mirroring how the certified Three-Bound Domination
Lemma (`lemmas/three-bound-domination-and-keep-top-bound.md`) is exactly this statement's own `k=1`
instance (in the "keep-both-of-two-remaining is dominated by touch-`\le1`" direction).

1. **Base case `k=0`:** `OPT_{+1}(\emptyset,W)` — trivially `0` (no background to combine with), and
   `\{0\}` is the unique "touch `\le0`" candidate. Free.
2. **Base case `k=1`:** already certified (Two-Touch / Three-Touch, `2k=2`/`2k+1=3`).
3. **Inductive step `k-1 \to k`:** peel one element `c^*` of `C` via a "release" argument — candidate
   mechanism (untested): adapt the certified Background-Release Domination Lemma's bijection (note its
   file already records two *chaining* routes into Gap 1a as dead — this would be a fresh, non-chaining
   use, peeling `C` by exactly one element rather than to background-free, and must be checked against
   those recorded counterexamples before being trusted), or a direct Rank-Extraction-based argument
   showing any selection touching `\ge2k+1` raw elements is dominated by a `\le2k`-touch alternative.
4. **Finite case analysis at `touch\le4$ (`k=2`):** once the closed form is established, verify
   `\mathrm{value}(\mathrm{candidate})\ge\min(A_1,D_l)` for each of the finitely many touch-`\le4`
   candidate shapes (0,1,2,3,4 raw elements touched, every keep/match combination) — structurally a
   larger but analogous generalization of the certified `q=3` Per-Partner Domination proof (§22.2),
   where `\mathrm{Res}` had only 1 element (touch-`\le1` candidates only); now up to 2 nested
   Rank-Extraction-Identity insertions per candidate (a match contributes a *derived* value).

### 31.4 Key lemmas needed (mechanism, not yet proved)

- **Generalized Touch-Bound Lemma at `k=2`** — because (conjectured mechanism) any selection using
  `\ge5` raw elements of `W` against a 2-element background can always be re-expressed, without loss,
  as a selection using `\le4`, via an argument analogous to Three-Bound Domination's redundancy
  elimination (untested at `k=2`, flagged in the explorer's report as a cheap first check for a
  builder: verify "match 2 pairs" (touch-4, no keep) is never the unique minimizer over a mixed
  keep+match alternative, mirroring how "keep-both" was eliminated at the old `k=2`,`touch\le2` attempt).
- **Redundancy-elimination step** — because Three-Bound Domination is exactly this statement's `k=1`
  mirror; the proof technique (case-split on rank, then apply the alternating-sum identity to show the
  wider-touch candidate never strictly beats the narrower one) is expected to generalize, but the
  larger candidate set at `k=2` has not been attempted.

### 31.5 Open gaps

1. Prove the Generalized Touch-Bound Lemma itself at `k=2` (Step 3 above) — no attempt made yet.
2. Carry out the finite `touch\le4` case analysis (Step 4) — no attempt made yet, expected to be
   large but mechanical (generalizes the certified `q=3` proof).
3. Cheap pre-check (recommended first, before the full case analysis): confirm the touch-4 candidate
   family reduces to a smaller sub-family via a redundancy-elimination pass (§31.4).

### 31.6 Watch out for

- Do NOT conflate this with the already-dead "`touch\le2` at `|C|=2`" formula (§25.2/§27.2(e), 18-24%
  failure) — that is a **different, wrong threshold**; this section's `touch\le4` claim is a
  previously-untested threshold with 0 failures across >10,000 combined checks (including on genuine
  `A_{3,l}`-shaped `\mathcal F`-provenance instances, 0/533).
- The Background-Release Domination Lemma's two known-dead chaining routes (recorded in that lemma's
  own file) must be re-checked against any new "peel one element of `C`" mechanism before reuse — a
  single-element peel is not automatically safe just because it isn't literally one of the two
  previously-tested chains.

## §32 (round 19, proof-outliner writeup of `math-explorer-27-2-d.md`): a candidate complete proof of
the §27.2(d)/§30.1 KEEP `b_0\le w_1` sub-case at `|W|=3` (`|rest|=2`)

**Status: STRONG CANDIDATE PROOF, not yet independently re-derived by anyone besides the reporting
explorer — needs a builder to formalize it in the file's own notation end-to-end and a reviewer to
independently re-check every one of the 5 sub-cases from scratch before it can be certified.** This is
exactly the gap round 18's proof-reviewer flagged as the missing ingredient for "Two-Touch fully proved
at `|W|\le3$" (rejected as an overclaim in round 18 because this inequality was then only corroborated,
`0/14{,}000+`). The outliner independently re-derived the pigeonhole-style reduction logic below and
found it internally consistent (min-of-terms `\ge Y` iff every term `\ge Y`, elementary) but did NOT
re-derive the 5 case-split sub-proofs by hand this round — that re-derivation is exactly the task for
the builder/reviewer.

### 32.1 Precise target

Fix `b_0\ge0`, sorted `W=(w_1\ge w_2\ge w_3)`, `\mathrm{rest}=(w_2,w_3)`, KEEP hypothesis `b_0\le w_1`.
Using the certified `\mathrm{ThreeTouch}(b_0,\mathrm{rest})` closed form (Lemma B,
`lemmas/max-element-triple-identity-and-threetouch-basecase.md`, unconditionally `=OPT_{-1}(\{b_0\},
\mathrm{rest})$ at `|\mathrm{rest}|\le3`) and `\mathrm{TwoTouch}(b_0,W)` (Two-Touch's own certified
`|C|=1` closed form):
```
Target (*):  w_1 - ThreeTouch(b_0,rest)  >=  TwoTouch(b_0,W)
```

### 32.2 The reduction (elementary, re-checked by the outliner)

`\mathrm{ThreeTouch}(b_0,\mathrm{rest})=\max(A_1,\dots,A_5)` over 5 explicit terms. Since
`w_1-\max_i(A_i)=\min_i(w_1-A_i)`, (*) is **equivalent** to `\min_i(w_1-A_i)\ge\mathrm{TwoTouch}(b_0,W)`,
which holds **iff each of the 5 per-term inequalities `w_1-A_i\ge\mathrm{TwoTouch}(b_0,W)` holds
separately** (elementary min/inequality fact, re-derivable in one line: if every term of a finite set is
`\ge Y` then the min is `\ge Y`, and conversely). Each per-term claim is then closed by exhibiting an
explicit `\mathrm{TwoTouch}` candidate `B_j` with `w_1-A_i\ge B_j\ge\mathrm{TwoTouch}(b_0,W)`. This
mirrors the per-term-domination proof shape that already closed 3/5 of both Two-Touch's and
Three-Touch's own general-induction pieces (§26.5(c)/(d), §28.4(c)/(d)) — a consistent methodology, not
an ad hoc trick.

### 32.3 The 5 per-term sub-claims (candidate proofs, need independent re-verification)

Notation: `A_1=e(\{b_0\})=b_0`, `A_2=|b_0-w_2|`, `A_3=|b_0-w_3|`, `A_4=|b_0-(w_2-w_3)|$,
`A_5=e(\{b_0,w_2,w_3\})$ (keep-all-three). `\mathrm{TwoTouch}$'s candidates:
`B_1=b_0,B_2=w_1-b_0,B_3=|b_0-w_2|,B_4=|b_0-w_3|,B_5=|b_0-(w_1-w_2)|,B_6=|b_0-(w_1-w_3)|,
B_7=|b_0-(w_2-w_3)|`.

1. **`A_1` (delete-all):** exact identity `w_1-A_1=w_1-b_0=B_2$ (using `b_0\le w_1`), so
   `\ge\mathrm{TwoTouch}(b_0,W)` trivially since `B_2` is itself a `\mathrm{TwoTouch}` candidate.
2. **`A_2,A_3` (keep-one):** via a new elementary sub-lemma (§32.4 below), `w_1-A_2\ge B_5`,
   `w_1-A_3\ge B_6`.
3. **`A_4` (match `w_2,w_3`):** 2-region split on `b_0` vs `w_2`. Region `b_0\ge w_2$: `A_4\le A_1`
   directly (algebra: `A_4=b_0-w_2+w_3\le b_0=A_1$ using `w_2\ge w_3`), so `w_1-A_4\ge w_1-A_1=B_2`.
   Region `b_0<w_2`: claim `w_1-A_4\ge B_4=|b_0-w_3|`, closed by a further split on `b_0` vs `w_3`
   (each sub-case reduces to `w_1+w_2\ge2b_0` or `w_1+2w_3\ge w_2` or `w_1+w_2\ge2w_3` or
   `w_1+2b_0\ge w_2` — all true from `w_1\ge w_2\ge w_3\ge0,\,0\le b_0<w_2\le w_1`).
4. **`A_5` (keep-all-three):** same 2-region split and same witnesses (`B_2`,`B_4`) as `A_4`, via the
   three sorted-order cases of `\{b_0,w_2,w_3\}`.

### 32.4 New sub-lemma needed: Two-Variable Reflection Bound

**Claim:** for `0\le b_0\le w_1` and `0\le w\le w_1`: `w_1-|b_0-w|\ge|b_0-(w_1-w)|`.

**Candidate proof (3-case split):**
- `b_0\le w`: LHS `=w_1-w+b_0=(w_1-w)+b_0\ge|b_0-(w_1-w)|=$RHS (using `p+q\ge|p-q|` for `p,q\ge0`,
  since `w_1-w\ge0,b_0\ge0`).
- `b_0>w,\,b_0\le w_1-w`: LHS `=w_1-b_0+w`, RHS `=(w_1-w)-b_0`; LHS−RHS`=2w\ge0`.
- `b_0>w,\,b_0>w_1-w`: LHS as above, RHS `=b_0-(w_1-w)`; LHS−RHS`=2(w_1-b_0)\ge0` (uses `b_0\le w_1`).

Applying with `w:=w_2$ gives sub-claim 2's `A_2` bound; with `w:=w_3$ gives the `A_3` bound. This
sub-lemma is general (not specific to `|W|=3`) and is a candidate for standalone certification if the
overall §32 route is confirmed — geometric remark: `w_1-|b_0-w|=e(\{w_1,b_0,w\})` by Lemma A (since
`w_1=\max`), so this says "keep-`b_0`-and-`w`, background `w_1`" dominates "match `b_0$ against
`w_1-w$" — related in flavor to, but not an instance of, the certified Three-Bound Domination Lemma.

### 32.5 Open gaps (for the builder)

1. **Independently re-derive all 5 per-term sub-claims by hand** (not just re-run the explorer's
   scripts) — this section reports a candidate proof, not a certified one.
2. **Formalize and independently verify the Two-Variable Reflection Bound** (§32.4) — a genuinely new,
   small, reusable lemma; candidate for standalone certification once confirmed.
3. **Trace the consequence carefully, without overclaiming:** IF §32's target (*) is confirmed proved,
   combined with the already-certified DELETE branch (general), KEEP `b_0>w_1` sub-case (round 16,
   unconditional), and MATCH branch via `lemmas/match-branch-domination-via-per-partner-domination.md`
   (conditional on Per-Partner Domination at `q\le3$, itself certified round 14) — this closes Two-Touch
   fully and unconditionally at `|W|\le3`. **Do NOT write this consequence into `current.md` or a
   headline claim until the reviewer independently confirms §32.1-§32.4** — this is exactly the overclaim
   pattern round 18's reviewer already caught once on this precise target; the fix must come from an
   actual independently-checked proof, not a restated corroboration count.
4. **Do not conflate with the general-`q` extension:** the explorer's cheap, unchased check at
   `|\mathrm{rest}|=3` (`0/20{,}000` for the aggregate and every per-term sub-claim) is a positive signal
   only — it is NOT attempted algebraically and would need (a) the general-`q` `\mathrm{TwoTouch}` closed
   form to itself be established as the true `OPT` (open, the joint induction), and (b) a larger case
   split (touch-3 terms appear once `|\mathrm{rest}|\ge3`). Do not claim this generalizes; flag it only
   as a positive sign for a future round's inductive-step attempt.

### 32.6 Watch out for

- The per-term reduction (§32.2) is only valid because it is a `\min`-of-terms identity — do NOT reuse
  it for a `\max`-of-terms target without re-deriving the direction of the inequality (the mirror
  direction needs "at least one term suffices," not "every term must hold").
- Sub-claim 3/4's region split is on `b_0` vs `w_2` (the *second-largest* element), not `b_0` vs `w_3`
  — the explorer flags this as the structurally meaningful threshold; a builder attempting the
  general-`q` extension (§32.5.4) should keep this framing, not rediscover it from scratch.

## §33 (round 19, proof-builder): §32's target proved in full — Two-Touch fully, unconditionally
proved for `|W|<=3`

**Status: PROVED (this round).** Every one of §32's 6 sub-claims (the Two-Variable Reflection Bound,
and all 5 per-term bounds) is re-derived below from scratch, by hand, with every case exhaustively
settled. Combined with the pieces already certified/proved on file (traced explicitly in §33.5), this
closes Two-Touch unconditionally for `|W|<=3`.

### 33.1 The Two-Variable Reflection Bound — full proof

**Lemma (Two-Variable Reflection Bound).** For `0<=b_0<=w_1` and `0<=w<=w_1`:
```
w_1 - |b_0-w|  >=  |b_0-(w_1-w)|.
```

**Proof.** Write `L:=w_1-|b_0-w|` (the claimed left side) and `R:=|b_0-(w_1-w)|` (the right side). Split
exhaustively on the sign of `b_0-w`, and (when `b_0>w`) further on the sign of `b_0-(w_1-w)`; these
three cases are mutually exclusive and exhaust all possibilities since `b_0-w` is either `<=0` or `>0`,
and (in the latter branch) `b_0-(w_1-w)` is either `<=0` or `>0`.

- **Case 1: `b_0<=w`.** Then `|b_0-w|=w-b_0`, so `L=w_1-w+b_0=(w_1-w)+b_0`. Both summands are
  nonnegative (`w_1-w>=0` since `w<=w_1`; `b_0>=0` by hypothesis). For any `p,q>=0`, `p+q>=|p-q|`
  (if `p>=q`, `|p-q|=p-q<=p+q` since `q>=0`; if `q>p`, `|p-q|=q-p<=p+q` since `p>=0`) — apply with
  `p:=w_1-w`, `q:=b_0`: `L=(w_1-w)+b_0>=|(w_1-w)-b_0|=|b_0-(w_1-w)|=R`.

- **Case 2: `b_0>w` and `b_0<=w_1-w`.** Then `|b_0-w|=b_0-w`, so `L=w_1-b_0+w`. Also
  `|b_0-(w_1-w)|=(w_1-w)-b_0$ (since `b_0<=w_1-w`), so `R=w_1-w-b_0`. Then
  `L-R=(w_1-b_0+w)-(w_1-w-b_0)=2w>=0` (using `w>=0`). Hence `L>=R`.

- **Case 3: `b_0>w` and `b_0>w_1-w`.** As in Case 2, `L=w_1-b_0+w`. Now `|b_0-(w_1-w)|=b_0-(w_1-w)`
  (since `b_0>w_1-w`), so `R=b_0-w_1+w`. Then `L-R=(w_1-b_0+w)-(b_0-w_1+w)=2w_1-2b_0=2(w_1-b_0)>=0`
  (using `b_0<=w_1`). Hence `L>=R`.

Every case gives `L>=R`; the three cases are exhaustive and pairwise non-overlapping in their
strict/non-strict boundary handling (`b_0<=w` vs `b_0>w`, and inside the latter `b_0<=w_1-w` vs
`b_0>w_1-w`, using `<=`/`>` consistently so no instance is double-counted or omitted, including the
boundary `b_0=w_1-w` which is validly assigned to Case 2). `\blacksquare`

**Remark.** This is a fully general, standalone lemma (no reference to any 3-element list), reusable
wherever `w_1=\max` of a background/candidate is being compared against a "keep-`b_0`-and-`w`" vs.
"match-`b_0`-against-`w_1-w`" pair of candidates. Proposed for standalone certification (§33.6).

### 33.2 The target and its reduction, restated precisely

Fix `b_0>=0`, sorted `W=(w_1>=w_2>=w_3)`, `rest=(w_2,w_3)`, and the KEEP hypothesis `b_0<=w_1`. Recall
(citing the certified closed forms):
```
ThreeTouch(b_0,rest) = max(A_1,A_2,A_3,A_4,A_5),   A_1=b_0, A_2=|b_0-w_2|, A_3=|b_0-w_3|,
                                                    A_4=|b_0-(w_2-w_3)|, A_5=e({b_0,w_2,w_3})
TwoTouch(b_0,W)      = min(B_1,...,B_7),  B_1=b_0, B_2=|b_0-w_1|, B_3=|b_0-w_2|, B_4=|b_0-w_3|,
                        B_5=|b_0-(w_1-w_2)|, B_6=|b_0-(w_1-w_3)|, B_7=|b_0-(w_2-w_3)|
```
By the certified Lemma B (`lemmas/max-element-triple-identity-and-threetouch-basecase.md`),
`\mathrm{OPT}_{-1}(\{b_0\},rest)=ThreeTouch(b_0,rest)` unconditionally, since `|rest|=2<=3`. The target
is
```
(*):  w_1 - ThreeTouch(b_0,rest)  >=  TwoTouch(b_0,W).
```

**Reduction.** Since `w_1-\max_i(A_i)=\min_i(w_1-A_i)` (an elementary identity: negating and adding a
constant to a finite set of reals turns its max into a min of the negated-and-shifted values), (*) is
equivalent to `\min_i(w_1-A_i)>=TwoTouch(b_0,W)`. This in turn holds **iff every one of the 5 terms**
`w_1-A_i>=TwoTouch(b_0,W)` holds individually: if `\min_i(w_1-A_i)>=Y` then, since the minimum of a
finite set does not exceed any individual member, every `w_1-A_i>=\min_i(w_1-A_i)>=Y`; conversely if
every `w_1-A_i>=Y` then `Y` is a lower bound for the whole set, hence `<=` its minimum. Applying this
with `Y:=TwoTouch(b_0,W)`, (*) is equivalent to the 5 separate claims `w_1-A_i>=TwoTouch(b_0,W)`,
`i=1,\dots,5`. It suffices, for each `i`, to exhibit **some** `B_j` with `w_1-A_i>=B_j`: since
`TwoTouch(b_0,W)=\min_j(B_j)<=B_j` for every `j`, this gives `w_1-A_i>=B_j>=TwoTouch(b_0,W)`.

### 33.3 The 5 per-term bounds — full proof

**Term `i=1` (`A_1=b_0`).** Since `b_0<=w_1`, `|b_0-w_1|=w_1-b_0`. So `w_1-A_1=w_1-b_0=B_2` exactly
(an identity, not merely an inequality). Since `B_2` is one of `TwoTouch`'s own candidates,
`w_1-A_1=B_2>=\min_j(B_j)=TwoTouch(b_0,W)`. `\checkmark`

**Term `i=2` (`A_2=|b_0-w_2|`).** Apply the Two-Variable Reflection Bound (§33.1) with `w:=w_2`
(valid since `0<=w_2<=w_1`, as `w_2<=w_1` because `W` is sorted descending, and `0<=b_0<=w_1` is the
KEEP hypothesis): `w_1-|b_0-w_2|>=|b_0-(w_1-w_2)|=B_5`. So `w_1-A_2>=B_5>=TwoTouch(b_0,W)`. `\checkmark`

**Term `i=3` (`A_3=|b_0-w_3|`).** Apply the Two-Variable Reflection Bound with `w:=w_3` (valid since
`0<=w_3<=w_2<=w_1`): `w_1-|b_0-w_3|>=|b_0-(w_1-w_3)|=B_6`. So `w_1-A_3>=B_6>=TwoTouch(b_0,W)`.
`\checkmark`

**Term `i=4` (`A_4=|b_0-(w_2-w_3)|`, the match-`w_2,w_3` term).** Write `d:=w_2-w_3>=0$ (since
`w_2>=w_3`), so `A_4=|b_0-d|`. Split into two regions on `b_0` vs `w_2`:

- **Region `b_0>=w_2`.** Then `b_0>=w_2>=d` (since `d=w_2-w_3<=w_2$ as `w_3>=0`), so
  `A_4=b_0-d=b_0-w_2+w_3`. Compare to `A_1=b_0`: `A_1-A_4=w_2-w_3>=0` (since `w_2>=w_3`), so
  `A_4<=A_1`, hence `w_1-A_4>=w_1-A_1=B_2>=TwoTouch(b_0,W)`.

- **Region `b_0<w_2`.** Claim `w_1-A_4>=B_4=|b_0-w_3|`. Split exhaustively into 4 mutually exclusive
  sub-cases on the sign of `b_0-d` and `b_0-w_3`:

  1. `b_0>=d` and `b_0>=w_3`: `A_4=b_0-d=b_0-w_2+w_3`, and `B_4=b_0-w_3`. Compute
     `(w_1-A_4)-B_4=\big(w_1-b_0+w_2-w_3\big)-\big(b_0-w_3\big)=w_1+w_2-2b_0`. Since `b_0<w_2$ (region
     hypothesis), `2b_0<2w_2`; since `w_2<=w_1`, `2w_2<=w_1+w_2`. Chaining: `2b_0<2w_2<=w_1+w_2`, so
     `w_1+w_2-2b_0>0>=0`.
  2. `b_0>=d` and `b_0<w_3`: `A_4=b_0-d=b_0-w_2+w_3`, and `B_4=w_3-b_0`. Compute
     `(w_1-A_4)-B_4=\big(w_1-b_0+w_2-w_3\big)-\big(w_3-b_0\big)=w_1+w_2-2w_3`. Since `w_1>=w_3` and
     `w_2>=w_3` (sorted order), `w_1+w_2>=2w_3`, so this is `>=0`.
  3. `b_0<d` and `b_0>=w_3`: `A_4=d-b_0=w_2-w_3-b_0`, and `B_4=b_0-w_3`. Compute
     `(w_1-A_4)-B_4=\big(w_1-w_2+w_3+b_0\big)-\big(b_0-w_3\big)=w_1-w_2+2w_3`. Since `w_1>=w_2`,
     `w_1-w_2>=0`; adding `2w_3>=0` gives `>=0`.
  4. `b_0<d` and `b_0<w_3`: `A_4=d-b_0=w_2-w_3-b_0`, and `B_4=w_3-b_0`. Compute
     `(w_1-A_4)-B_4=\big(w_1-w_2+w_3+b_0\big)-\big(w_3-b_0\big)=w_1-w_2+2b_0`. Since `w_1>=w_2` and
     `b_0>=0`, this is `>=0`.

  These 4 sub-cases exhaust every possibility (sign of `b_0-d` is `<0` or `>=0`; sign of `b_0-w_3` is
  `<0` or `>=0`, independently), so in every sub-case `w_1-A_4>=B_4>=TwoTouch(b_0,W)`.

The two regions (`b_0>=w_2`, `b_0<w_2`) are exhaustive and non-overlapping (using `>=`/`<` consistently),
so `w_1-A_4>=TwoTouch(b_0,W)` holds unconditionally. `\checkmark`

**Term `i=5` (`A_5=e(\{b_0,w_2,w_3\})`, the keep-both-`w_2,w_3` term).** Split exhaustively on the rank
of `b_0` among `\{b_0,w_2,w_3\}` (three cases, using `w_2>=w_3` already fixed):

1. **`b_0>=w_2$ (hence `b_0>=w_2>=w_3`, so `b_0` is the max of the three).** By the certified Lemma A
   (`lemmas/max-element-triple-identity-and-threetouch-basecase.md`, Max-Element Triple Identity),
   `A_5=e(\{b_0,w_2,w_3\})=b_0-|w_2-w_3|=b_0-(w_2-w_3)` (using `w_2>=w_3`). Compare to `A_1=b_0`:
   `A_1-A_5=w_2-w_3>=0`, so `A_5<=A_1`, hence `w_1-A_5>=w_1-A_1=B_2>=TwoTouch(b_0,W)`.
2. **`w_2>=b_0>=w_3$ (so `w_2` is the max of the three, since `w_2>=b_0` and `w_2>=w_3`).** By Lemma A
   (with max `=w_2`, the other two `=b_0,w_3`): `A_5=w_2-|b_0-w_3|=w_2-(b_0-w_3)$ (using `b_0>=w_3` in
   this case) `=w_2-b_0+w_3`. Then `w_1-A_5=w_1-w_2+b_0-w_3`, and `B_4=|b_0-w_3|=b_0-w_3` (since
   `b_0>=w_3`). Compute `(w_1-A_5)-B_4=(w_1-w_2+b_0-w_3)-(b_0-w_3)=w_1-w_2>=0` (since `w_1>=w_2`). So
   `w_1-A_5>=B_4>=TwoTouch(b_0,W)`.
3. **`b_0<=w_3$ (hence `b_0<=w_3<=w_2`, so `w_2` is the max of the three).** By Lemma A:
   `A_5=w_2-|w_3-b_0|=w_2-(w_3-b_0)` (using `w_3>=b_0` here) `=w_2-w_3+b_0`. Then
   `w_1-A_5=w_1-w_2+w_3-b_0`, and `B_4=|b_0-w_3|=w_3-b_0` (since `b_0<=w_3`). Compute
   `(w_1-A_5)-B_4=(w_1-w_2+w_3-b_0)-(w_3-b_0)=w_1-w_2>=0`. So `w_1-A_5>=B_4>=TwoTouch(b_0,W)`.

These three cases (`b_0>=w_2`; `w_2>=b_0>=w_3`; `b_0<=w_3`) are exhaustive (they cover every possible
value of `b_0`, since `w_2>=w_3`) and boundary-consistent (both non-strict inequalities agree at the
shared boundaries `b_0=w_2` and `b_0=w_3`). Hence `w_1-A_5>=TwoTouch(b_0,W)` unconditionally.
`\checkmark`

All 5 terms are established, so by the reduction of §33.2, **(*) holds unconditionally**:
```
w_1 - ThreeTouch(b_0,rest)  >=  TwoTouch(\{b_0\},W)   for all  0<=b_0<=w_1,  W=(w_1>=w_2>=w_3>=0).
```
`\blacksquare` (Target (*), i.e. Two-Touch's KEEP `b_0<=w_1` sub-case at `|W|=3`.)

### 33.4 Computational corroboration (not a proof step — a sanity check on the derivation above)

Independent `Fraction`-exact Python re-implementation of `TwoTouch`, `ThreeTouch`, and brute-force
`OPT_{+1}`/`OPT_{-1}` (`/tmp/round-19-build/verify_32.py`), validated first by cross-checking
`ThreeTouch(b_0,rest)` against a genuine brute-force `OPT_{-1}(\{b_0\},rest)$ and `TwoTouch(b_0,W)`
against a genuine brute-force `OPT_{+1}(\{b_0\},W)` (both `0` mismatches, confirming the closed forms
themselves are correctly implemented and — at `|W|<=3` — already known-equal to the true optimum by
the certified base case/Lemma B):
- Exhaustive integer grid `w_1,w_2,w_3,b_0\in\{0,\dots,6\}` with `w_1>=w_2>=w_3>=0,0<=b_0<=w_1$: `462`
  tuples, `0` failures on target (*), `0` failures on all 5 per-term bounds, `0` failures on the
  Two-Variable Reflection Bound (applied at `w=w_2` and `w=w_3`), `0` mismatches between `ThreeTouch`
  and brute-force `OPT_{-1}`, `0` mismatches between `TwoTouch` and brute-force `OPT_{+1}`.
- Random half-integer sweep, `v_{\max}=200`, `19{,}894` valid trials (`0<=b_0<=w_1`): `0` failures on
  target (*), `0` failures on all 5 per-term bounds, `0` failures on the reflection bound.
- **Negative controls (confirming every hypothesis is load-bearing, not vacuous):** dropping
  `0<=w<=w_1` in the Two-Variable Reflection Bound (testing `w>w_1`) gives **`3000/3000` (100%)**
  failures; dropping the KEEP hypothesis `b_0<=w_1` in the target (*) (testing `b_0>w_1`) gives
  **`5000/5000` (100%)** failures. Both hypotheses are therefore essential, exactly as used in the
  proofs above (the KEEP hypothesis is used in Case 3 of §33.1 and in Term `i=1` of §33.3; the
  `w<=w_1` hypothesis is used in Case 1 of §33.1).

Script saved at `/tmp/round-19-build/verify_32.py` (reproducible, exact-`Fraction` arithmetic
throughout, no floating point).

### 33.5 Consequence: Two-Touch is fully, unconditionally proved for `|W|<=3`

**Corollary (Two-Touch, `|W|<=3`).** For every `C` with `|C|<=1` and every `W` with `|W|<=3`:
```
OPT_{+1}(C,W) = TwoTouch(C,W).
```

**Proof.** By strong induction on `|W|`, tracking `C=\emptyset` and `C=\{b_0\}` together (as §26.5
already sets up).

- **`C=\emptyset`, any `W`.** By the certified Empty-Background Lemma (Statement 1 of
  `lemmas/empty-background-and-background-splitting.md`), `OPT_{+1}(\emptyset,W)=0` unconditionally,
  for every `W` (no restriction on `|W|`). Also `TwoTouch(\emptyset,W)=\min(e(\emptyset),
  \min_w e(\{w\}),\min_{i<j}e(\{|w_i-w_j|\}))=\min(0,\min_w w,\dots)=0`, since `e(\emptyset)=0` is
  itself one of the candidates and every candidate is `>=0` (all terms are absolute values or `0`, and
  `W`'s elements are nonnegative). So `OPT_{+1}(\emptyset,W)=0=TwoTouch(\emptyset,W)` for every `W`,
  in particular `|W|<=3`. This case needs no induction at all.
- **`C=\{b_0\}`, `|W|<=2`.** Certified base case (§26.5(a)): `|W|=0,1` trivial (search space has
  `<=2` selections, all already `TwoTouch` candidates); `|W|=2` is exactly the certified Three-Bound
  Domination Lemma (`lemmas/three-bound-domination-and-keep-top-bound.md`).
- **`C=\{b_0\}`, `|W|=3`.** By the certified Generalized Multi-Background Peeling Lemma's
  DELETE/KEEP/MATCH trichotomy (peeling `w_1:=\max(W)`), `OPT_{+1}(\{b_0\},W)=\min(\mathrm{DELETE},
  \mathrm{KEEP},\mathrm{MATCH})`, where each branch's own value is `>=OPT_{+1}(\{b_0\},W)$ trivially
  (each is the value of one restricted class of selections, hence `>=` the overall minimum), and the
  overall optimum equals the smallest of the three. It therefore suffices to show each of the three
  branches is `>=TwoTouch(\{b_0\},W)`, since this gives `OPT_{+1}(\{b_0\},W)=\min(\text{branches})
  >=TwoTouch(\{b_0\},W)`, which combined with the free/trivial reverse direction
  `OPT_{+1}(\{b_0\},W)<=TwoTouch(\{b_0\},W)$ (every `TwoTouch` candidate is the value of a genuine
  selection, so the true minimum cannot exceed it) gives equality:
  1. **DELETE `>=TwoTouch(\{b_0\},W)`.** DELETE `=OPT_{+1}(\{b_0\},rest)` where `rest=W\setminus\{w_1\}`,
     `|rest|=2`. By the already-established `|W|=2` base case (just above, no circularity — strictly
     smaller size), `OPT_{+1}(\{b_0\},rest)=TwoTouch(\{b_0\},rest)`. As computed explicitly in §33.2,
     `TwoTouch(\{b_0\},rest)=\min(B_1,B_3,B_4,B_7)`, a minimum over a subset of `TwoTouch(\{b_0\},W)`'s
     own 7-term candidate list `\{B_1,\dots,B_7\}` — a minimum over a subset is `>=` a minimum over the
     full set, so `TwoTouch(\{b_0\},rest)>=TwoTouch(\{b_0\},W)`. Hence
     `\mathrm{DELETE}=TwoTouch(\{b_0\},rest)>=TwoTouch(\{b_0\},W)`. (This is exactly §26.5(b)'s general
     argument, instantiated at `|W|=3`.)
  2. **KEEP `>=TwoTouch(\{b_0\},W)`.** Two exhaustive sub-cases on `b_0` vs `w_1` (the only two
     possibilities, since `b_0<=w_1` is not assumed at this level — this is a genuine dichotomy):
     - If `b_0>w_1`: by §26.5(c) (certified, unconditional, no induction needed), KEEP
       `=b_0-w_1=|b_0-w_1|=e(\{b_0,w_1\})=B_2`, one of `TwoTouch(\{b_0\},W)`'s own candidates, so
       KEEP `>=TwoTouch(\{b_0\},W)` trivially.
     - If `b_0<=w_1`: by §26.5(d), KEEP `=w_1-OPT_{-1}(\{b_0\},rest)`. Since `|rest|=2<=3`, the
       certified Lemma B gives `OPT_{-1}(\{b_0\},rest)=ThreeTouch(b_0,rest)$ exactly, so
       KEEP `=w_1-ThreeTouch(b_0,rest)`. By **§33.3's target (*), proved above** (using exactly the
       hypothesis `b_0<=w_1` active in this sub-case), KEEP `=w_1-ThreeTouch(b_0,rest)>=
       TwoTouch(\{b_0\},W)`.
     These two sub-cases (`b_0>w_1`, `b_0<=w_1`) are exhaustive and non-overlapping (using `>`/`<=`),
     so KEEP `>=TwoTouch(\{b_0\},W)` unconditionally.
  3. **MATCH `>=TwoTouch(\{b_0\},W)`.** MATCH `=\min_j MATCH_j` over partners `w_j\in rest` (the
     smallest of finitely many match-with-`w_1` candidate values, per the trichotomy's own definition
     — matching `w_1` with each possible partner is itself a further finite case split already
     absorbed into "the MATCH branch"). By the certified Lemma
     (`lemmas/match-branch-domination-via-per-partner-domination.md`), conditional only on Gap 1a's
     Per-Partner Domination Lemma at `q=|W|=3` (certified **unconditionally** for `q<=3` since round 14,
     §22.2 — so at `|W|=3` this dependency is fully discharged, not merely conditional), every
     `MATCH_j>=TwoTouch(\{b_0\},W)$ for `j=2,3` (the two possible match partners of `w_1` in a
     3-element `W`). Hence `\mathrm{MATCH}=\min_j MATCH_j>=TwoTouch(\{b_0\},W)`.

  All three branches are `>=TwoTouch(\{b_0\},W)`, giving `OPT_{+1}(\{b_0\},W)>=TwoTouch(\{b_0\},W)`,
  and combined with the free reverse inequality, **equality**.

By induction (base case `|W|<=2` above, inductive step `|W|=3` above, using the base case as the sole
input to the DELETE branch), `OPT_{+1}(C,W)=TwoTouch(C,W)` for every `C` with `|C|<=1` and every `W`
with `|W|<=3`. `\blacksquare`

**This is now a genuinely, unconditionally proved statement — not merely corroborated.** Every
ingredient used above is either (a) proved in full in this section (§33.1, §33.3), or (b) an
already-certified lemma cited by name and file (Empty-Background Lemma, Three-Bound Domination Lemma,
Lemma A, Lemma B, Match-Branch-Domination-via-Per-Partner-Domination, Per-Partner Domination Lemma at
`q<=3`, Generalized Multi-Background Peeling Lemma, §26.5(b)/(c)/(d)'s own DELETE/KEEP-branch formula
derivations — all independently re-verified by proof-reviewers in rounds 12-18, see `current.md`'s
history), traced explicitly above with no hidden gap and no unresolved conditional dependency at
`|W|<=3`.

### 33.6 Promotable lemma

**Two-Variable Reflection Bound** (§33.1) is fully general, elementary, and reusable beyond this
specific application — proposed for standalone certification as
`lemmas/two-variable-reflection-bound.md` (draft below in the Promotable lemmas section of this file's
Status block).

### 33.7 What this does NOT give — scope discipline (do not overclaim beyond this)

- This closes Two-Touch (`OPT_{+1}(C,W)=TwoTouch(C,W)`, `|C|<=1`) **only** for `|W|<=3`. The general-`q`
  induction (`|W|>=4`) remains fully open — it would need, at minimum, Per-Partner Domination at
  `q>=4` (open) for the MATCH branch, and a `q\ge4` extension of §33.1-§33.3's KEEP `b_0<=w_1` argument
  (flagged by §32.5.4 as needing a larger case split once `|rest|>=3`, not attempted here).
- This does **not** by itself close Gap 1a's general-`q` Per-Partner Domination Lemma, nor Three-Touch's
  own MATCH branch, nor Gap 1b/1c — those remain exactly as open as before this round (see `current.md`
  for the full standing list).
- This does **not** establish or depend on the still-conjectural Generalized Touch-Bound Lemma (§31);
  the two sections are logically independent (§33 is a self-contained `|W|=3` closure using only
  already-certified/already-proved machinery, not the `|C|=k` touch-bound framework).

## §34 (round 19, proof-builder): §31 attempt — Generalized Touch-Bound Lemma at `|C|=2`, honest
partial progress (Status remains CONJECTURAL / CORROBORATED, no proof found)

**Summary: no proof of the `k=2` case (or its inductive step) was found this round. Real, useful
negative and structural findings were established, narrowing the search for the next attempt; nothing
below should be read as progress toward a closure.**

### 34.1 The natural single-witness shortcut is FALSE — a concrete negative result

The most natural cheap conjecture for the "excess-touch" reduction at `k=2` — that dropping the single
smallest element of `W` always suffices to dominate the "keep-everything" (or, more generally, any
touch-`>4`) candidate — is **false**, with a substantial, non-negligible failure rate (ruling this out
as a shortcut, not merely "occasionally fails"):

**Test.** For `|C|=2` (`c_1,c_2` random in `\{0,\dots,10\}`) and `|W|=5` (`w_1\ge\dots\ge w_5` random in
`\{0,\dots,10\}`), compare `e(C\cup W)` (the touch-5 "keep-all" candidate) against
`e(C\cup\{w_1,w_2,w_3,w_4\})` (the touch-4 "drop-`w_5`" candidate):
```
keep-all-5 >= drop-w5(touch<=4):  366/3000 (12.2%) FAILURES
```
(`/tmp/round-19-build/explore_31.py`, `Fraction`-exact, seeded). I.e. in `12.2\%` of random instances,
dropping the smallest element of `W` alone does **not** produce a dominating touch`\le4` candidate — a
genuinely different (selection-dependent) witness is required, analogous in spirit to, but larger in
scope than, Lemma B's own 4-case "keep-all-three" domination argument for `k=1`. **This rules out the
cheapest possible general mechanism** (mirroring how the earlier "`touch\le2`" formula and "average"-
based routes were ruled out in prior rounds) but does **not** mean no simple witness exists — only that
"the smallest element" is not always the right one to drop.

**The Generalized Touch-Bound Lemma itself remains true at this instance** (re-confirmed,
`0/2000` failures on "`\mathrm{keep\text{-}all\text{-}5}\ge` the TRUE minimum over ALL touch`\le4`
candidates" — i.e. SOME touch-`\le4` candidate always dominates, just not always the same fixed one).

### 34.2 Diagnostic: which touch`\le4` shape wins, empirically

Recording, over `500` fresh random `(c_1,c_2,W)` instances (`|W|=5`), which selection shape
`(|\mathrm{keep}|,|\mathrm{match\ pairs}|)` achieves the minimum among all touch`\le4` candidates:
```
(1,1): 127   (2,0): 118   (0,0): 115   (1,0): 81   (0,2): 33   (0,1): 26
```
**No single shape (or small fixed pair of shapes) dominates the winning-witness distribution** — all
6 possible touch`\le4` shapes (`(0,0)` delete-all through `(0,2)` match-two-pairs) occur as the unique
minimizer in a non-negligible fraction of instances. This indicates a genuine, non-degenerate case
analysis (rank of `c_1,c_2` among the 5+2=7 combined values, likely `>=5` cases by analogy with how
Lemma B's simpler `k=1,|W|=3` instance already needed 4 cases) would be needed even for this single,
smallest excess instance (`|W|=5`) — before any attempt at the general induction. **Not attempted this
round due to time constraints** — flagged as the natural next concrete sub-target (smaller in scope
than the full induction) for a future round, more tractable than jumping straight to Step 3's general
inductive step.

### 34.3 Structural finding: the "peel-`W`" route to `k=2` requires a NEW `k=2`, `\sigma=-1` mirror,
recursively — genuinely not easier than the still-open `k=1` general induction

An alternative to the outline's "peel `C`" strategy (Step 3) is to mimic Two-Touch's own proof
technique directly: fix `|C|=2` and induct on `|W|`, peeling `w_1:=\max(W)` via the Generalized
Multi-Background Peeling Lemma, exactly as §26.5/§33.5 do for `|C|=1`. Tracing this through:

- **DELETE branch**: identical argument to §26.5(b)/§33.5(1) (candidate-list-inclusion) — free, given
  the claim already holds at `|W|-1`.
- **KEEP branch**: peeling `w_1` into the background `C\cup\{w_1\}=\{c_1,c_2,w_1\}` (3 elements) uses
  the General Rank-Extraction Identity, and the resulting formula **depends on the rank of `w_1` among
  `\{c_1,c_2\}`** (three sub-cases: `w_1\ge c_1(\ge c_2)`; `c_1\ge w_1\ge c_2`; `w_1\le c_2(\le c_1)`),
  each giving a **different** sign pattern for the recursive call. In the first sub-case (`w_1` becomes
  the new maximum of the 3-element background), the resulting recursive call is
  `w_1-OPT_{-1}(\{c_1,c_2\},\mathrm{rest})` — a genuinely new `\sigma=-1$, `|C|=2` sub-problem (a
  "Four-Touch"-type object, by direct analogy with how Two-Touch's own KEEP `b_0\le w_1` sub-case
  needed Three-Touch, the `\sigma=-1` mirror at `k=1`). **This mirror is not defined or proved
  anywhere on file for `k=2`** — it would need its own closed-form conjecture, its own base case, and
  its own (separate, mutually recursive) induction, paralleling but strictly larger than the already
  multi-round-old Two-Touch/Three-Touch joint induction at `k=1`.
- **MATCH branch**: peeling `w_1`, matched with a partner `w_j`, gives a `|C|=3` sub-problem
  `OPT_{+1}(\{c_1,c_2,d_j\},X)` — growing the background size by one, exactly the same
  "MATCH-carries-forward-unreduced-difficulty" phenomenon already diagnosed for `k=1` (§27.1) as the
  reason the naive `q`-induction route was abandoned in favor of the closed-form/touch-bound approach
  in the first place.

**Conclusion (honest, not a proof): the "peel-`W`" route to `k=2` is not independently easier than the
already-multi-round-open `k=1` general induction** — it requires, recursively, both a new `\sigma=-1`
mirror at `k=2` and (via MATCH) the same unbounded-background-growth obstruction the touch-bound
framework was introduced specifically to avoid. This is a genuine structural finding (in the spirit of
round 9's "Match-Recovery Lemma is not independently easier" and round 18's Two-Touch/Three-Touch
min/max-asymmetry finding), narrowing which route a future round should attempt — it does **not**
prove the outline's own "peel-`C`" Step-3 route is any better or worse; that route (via the certified
Background-Release Domination Lemma, which the file's own §31.6 already flags as having two known-dead
chaining routes) was **not attempted computationally or algebraically this round** due to time
constraints, and remains the recommended next attempt.

### 34.4 Verification scripts

`/tmp/round-19-build/explore_31.py` — `Fraction`-exact, seeded (`random.seed(7)`); contains: (i) the
`k=2`,`touch\le4` vs. true-`OPT` re-confirmation (`0/400`, `|W|\in\{5,6\}`), (ii) the "keep-all-5
dominated by best touch`\le4`" re-confirmation (`0/2000`), (iii) the "drop-smallest" negative result
(`366/3000`), (iv) the winning-shape distribution census (`500` instances). All runs reproducible by
re-executing the script (fixed seed, exact rational arithmetic, no floating point).

### 34.5 Open gaps (unchanged in substance, sharpened in detail)

1. Prove the Generalized Touch-Bound Lemma at `k=2` — still fully open. §34.1-§34.3 narrow the search
   (rule out the cheapest single-witness shortcut; identify that the natural "peel-`W`" alternative is
   at least as hard as the open `k=1` general induction) but supply no proof.
2. The outline's own recommended "peel-`C`" Step-3 mechanism (via Background-Release Domination) was
   not attempted this round — the most promising concrete next step, per both this round's and last
   round's assessment.
3. Even the single smallest excess instance (`|C|=2,|W|=5`, first case where touch exceeds `2k=4`) is
   not fully proved — §34.2's shape census suggests it needs a `\ge5`-case rank-based split, not yet
   carried out.
