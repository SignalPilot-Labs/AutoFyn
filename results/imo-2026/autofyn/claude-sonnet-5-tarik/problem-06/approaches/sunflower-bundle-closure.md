## Status
partial

## Round 13 update (headline — read this first)

**Conjecture (WCE) is not established in full generality this round — and
this round's central, honestly-reported finding is that it is provably
*not* a strictly easier or genuinely independent target from Conjecture
(JW): a full, unconditional proof of (WCE) would in particular prove (JW)
itself for every Case-B pair, so (WCE)'s remaining difficulty is at least
as hard as the sole standing gap of this entire workspace (rounds
10–13).** What is new and fully rigorous this round: (a) a precise formal
definition of "witness-chaining proof" (§10.1) that captures exactly the
round-13 explorer's ad hoc `4199` case-tree mechanism as a special case;
(b) the **Chaining Sufficiency Theorem** (§10.2), a completely general,
fully proved theorem — for *any* doubly-infinite Case-B pair and *any*
finite witness collection `R`, a purely finite/mechanical combinatorial
check on `R`'s companion sets (no infinite quantifiers) suffices to prove
(JW) for the pair via `W:=\bigcup_{r\in R}\mathrm{comp}(a_r)` — verified
(§10.3) to reproduce the round-13 explorer's hand-built `4199:(13,17)`
argument exactly, prime for prime; (c) the **Single-Witness-Per-Side
Insufficiency Proposition** (§10.5), a clean *iff* characterization
(proved in full) subsuming and sharpening round 11's and round 12's ad hoc
counterexamples (Matched-Witness, `Π` from Lemma CB) into one general fact:
the minimal one-witness-per-side chaining candidate *never* works unless
the two witnesses' companion sets are literally equal singletons — which
never occurs in this workspace's tested instances; (d) an explicit,
fully-worked illustrative computation (§10.6) showing even the "free"
witness set already supplied unconditionally by the certified Lemma FT
transversal does **not** automatically satisfy the new theorem's
hypothesis on `a_1=247` (a concrete finite counterexample within the
theorem's own combinatorics, not a numerical sampling gap) — confirming
the theorem is genuine, non-vacuous content, not a disguised restatement
that trivially closes everything. **Net**: a new, general, reusable proof
technique is built and fully verified (usable by sibling
`forced-primes-well-ordering` to formalize its own concrete-instance case
trees, and by any future instance), but the existence question (WCE) asks
for is left honestly open, with a precise argument for why it cannot be
easier than (JW) and why no tool currently in this file's toolkit
guarantees the needed witnesses exist in general. `Status` stays
`partial`.

## Round 13 Outline (proof-outliner directive — attempt the GENERAL
existence argument for the new witness-chaining mechanism, complementing
`forced-primes-well-ordering`'s concrete-instance build)

**Target (unchanged): the whole problem**, via Theorem SW → Theorem 5.1
(both already certified, do not re-derive). The Row-Restriction Obstruction
(certified this file, round 12) remains the correct, honest diagnosis of
why Step 4′ (NIDF-pigeonhole applied directly to escape primes) cannot
close Case B — do not re-attempt that specific mechanism. Round 13's
case-b explorer (`/tmp/round-13/math-explorer-case-b.md`, see
`forced-primes-well-ordering`'s Round 13 Outline for the full mechanism
description) found a genuinely new, structurally different route — finite
disjunction-chaining from several FIXED low-index prefix witnesses via
Lemma P′ — that sidesteps the Row-Restriction Obstruction entirely (it
needs no same-side cross-index linking fact at all: every disjunction
comes from one fixed witness applied to the whole range of the
*complementary* class, exactly the "one side fixed, other side ranges
freely" shape Row-Restriction identified as available).

**This approach's role this round: the GENERAL existence question, not
the two concrete instances (owned by `forced-primes-well-ordering`).**
The explorer's construction is currently instance-specific — witnesses
`a_2,a_5,a_9,a_12` for `4199`, found by direct inspection of the first
~12–100 terms. The open, harder, and more valuable question for the whole
problem (not just the two mandatory instances) is:

**Conjecture (WCE — Witness-Chaining Existence):** for *every*
doubly-infinite disjoint core pair `(S,S')` in Case B (no class-wide
backbone on either side), there exist FINITELY MANY fixed low-index
witnesses `i_1,\dots,i_r\in I_S` (resp. `j_1,\dots,j_s\in I_{S'}`) whose
companion-set disjunctions, chained by finite Boolean case-analysis, force
every cross pair `(i,j)`, `i\in I_S,j\in I_{S'}`, `i>\max i_l`, `j>\max
j_m`, to share a prime.

**Skeleton:**
1. State (WCE) precisely and confirm it is genuinely a generalization
   (not a restatement) of what `forced-primes-well-ordering` verifies on
   the 2 mandatory instances — the difference is the EXISTENCE quantifier
   over witnesses/case-trees, not their explicit form.
2. Attempt a general existence mechanism: does the already-certified
   Realized–Blocked Dichotomy (Lemma ERD-C) plus Escape-Confinement
   guarantee that SOME finite prefix of each class always contains enough
   "singleton-or-small-companion" witnesses to build a closing case tree —
   i.e. is the depth/width of the needed Boolean case-tree itself bounded
   by a quantity already under control (e.g. `\omega(a_1)` or `|P_1|`), or
   can it grow without bound across different `a_1`? This is the load-
   bearing open question — do not assume a uniform bound without an
   argument (per this workspace's repeated "unexplained pattern ≠ proved
   characterization" lesson, rounds 3, 5, 7).
3. If a general bound is not found this round, report honestly (per the
   explorer's own scoping) which of the two mandatory instances' case
   trees was fully formalized vs. which remains a numerically-supported
   sketch, and what specifically blocks generalizing beyond low-index
   inspection (e.g. no known guarantee a singleton-companion witness, or
   even a small-companion witness, exists in the first `K` terms of an
   arbitrary class, for any explicit `K`).
4. Cross-check against Row-Restriction: confirm explicitly that (WCE), if
   proved, does NOT silently reduce to the already-refused NIDF-pigeonhole
   shape (verify the disjunction-chaining argument never needs to relate
   `\mathrm{comp}(a_j)` to `\mathrm{comp}(a_{j'})` for two same-side
   indices — per the explorer's "Why this differs" analysis, it does not,
   but this should be checked again in the general (WCE) formulation, not
   just the two worked instances).

**Not redundant with `forced-primes-well-ordering`:** that approach
completes the concrete case-trees for `4199:(13,17)` and `247:(13,19)`
(sufficient, if achieved, to fully resolve those two specific instances'
Case B content); this approach attempts the GENERAL statement needed to
close Case B for an arbitrary future `a_1` — a strictly harder, currently
fully open target, genuinely complementary rather than duplicated effort.

## Round 12 update (headline — read this first)

**Conjecture (JW) is not closed for Case B this round; two new, fully
rigorous pieces of content are added — one diagnostic (a precise proof of
*why* the Step 4′ NIDF-pigeonhole-on-escape-primes idea, as literally
proposed, cannot close the gap by itself) and one negative-but-concrete (a
natural refinement of the round-11 candidate `Π`, the "Matched-Witness"
construction, is built via already-certified machinery and then explicitly
refuted on **both** mandatory Case B instances, with hand-verifiable
counterexamples at index `≤11`).** Full detail in §9 below. **Net: real,
honest progress narrowing *how* the gap can be attacked next, no closure —
`Status` stays `partial`.**

**1. Diagnosed precisely why Step 4′ cannot close the gap by itself
(§9.2).** The NIDF-style injection argument, applied with one side's index
fixed (`j_0`), bounds the escape-prime set arising from pairs `(i,j_0)` as
`i` ranges over `I_S^\tau` — but this bound (`\subseteq\mathrm{comp}
(a_{j_0})\setminus\Pi`) is tied to the *specific* `j_0`; nothing in the
certified toolkit (Lemma P′, XC, NIDF, FT, CB, Escape-Confinement) relates
`\mathrm{comp}(a_{j_0})` to `\mathrm{comp}(a_{j_0'})` for a different
`j_0'\in I_{S'}^{\tau'}`, so the union over all of `I_{S'}^{\tau'}` is not
controlled. This is a genuine, previously-unstated structural reason (not
just "we tried and it stalled") that Step 4′ reduces to the *identical*
open requirement already diagnosed in §7.4/§8.4 (a cross-index rigidity
fact), just repackaged — worth recording so no future round re-attempts
this specific reframing without a new idea for the cross-reference gap.

**2. Matched-Witness construction + explicit refutation (§9.3–9.4), on
both `247:(13,19)` and `4199:(13,17)`.** Using the already-certified Lemma
CB + Escape-Confinement Lemma with a *smarter* witness choice than round
11's "first witness found" (round 11's witnesses gave mismatched companion
sets, e.g. `\{2,7\}` vs `\{2,5\}` for `247:(13,19)`), this round finds —
by direct search, then verifies by hand — witnesses with **identical**
companion sets on both sides (`\{2,3\}=\{2,3\}` in both instances,
independently). This is a natural, non-trivial refinement one might hope
closes the joint-coverage gap by symmetry. **It does not**: an explicit,
tiny, hand-verifiable counterexample is exhibited in each instance
(`a_2=260`/`a_5=285` for `247`, sharing only prime `5\notin\{2,3\}`;
`a_9=4316`/`a_5=4233` for `4199`, sharing only prime `83\notin\{2,3\}`),
confirming the gap is not a witness-selection artifact of round 11's
specific (unmatched) choice — a genuinely new negative finding, closing
off this natural next attempt before a future round spends effort on it.

## Round 12 Outline (proof-outliner directive — retire the refuted `Π`
construction; retarget Trace-Clash-Freedom/Cross-Permanent-Inadmissibility
explicitly to "Case B" pairs, the harder residual after this round's
Case-A/Case-B split)

**Target (unchanged): the whole problem**, via Theorem SW → Theorem 5.1
(both already certified, do not re-derive). Round 11's §8.3 candidate
`Π:=\mathrm{comp}(a_{j_3})\cup\mathrm{comp}(a_{j_3'})` (built from Lemma
CB's blocking witnesses) is **REFUTED** this round by an explicit,
independently-verified counterexample (this round's jw-rigidity explorer,
`/tmp/round-12/math-explorer-jw-rigidity.md`, Finding 1): `a_1=247`,
`i=51` (`\mathrm{comp}(a_{51})=\{2,3,7\}`), `j=739`
(`\mathrm{comp}(a_{739})=\{3,5\}`), shared prime `3\notin Π=\{2,5,7\}`
(998 total such failures in the sample sweep, all sharing prime `3`).
**Retire §8.3's specific `Π` as stated** — a single blocking witness's
companion set provably discards genuinely necessary primes in general.
This does **not** refute Conjecture (JW) itself (the larger Lemma FT
transversal `W:=U_S\cup U_{S'}` still shows zero violations, `~270`M
pairs checked across 7 instances this round) nor the Trace-Clash-Freedom
Reformulation skeleton below (Round 11 Outline, retained, Steps 1–3,5
unchanged) — only the specific `Π` construction of §8.3 dies. Do not
re-attempt it in any form.

**Retarget scope (new this round).** Sibling `sunflower-inadmissibility-
toolkit` (revised this round) now closes Conjecture (JW) unconditionally
— modulo one new Backbone Permanence Lemma — for "**Case A**" pairs (5/7
tested: those where one side's running companion-set intersection
freezes to an exactly-realized nonempty value; see that file's Round 12
Outline for the precise mechanism, via the already-certified Lemma UCR).
**This approach's job, sharpened by that split, is now: close Conjecture
(JW) for "Case B" pairs** — those where NEITHER side has such a
backbone. Confirmed Case B instances (2/7 tested): `247:(13,19)` (the
`S'=\{19\}` side's running intersection collapses to `\varnothing` by the
2nd realized member) and `4199:(13,17)` (`\{13\}`'s backbone freezes to
`\{2\}` but is never exactly realized bare; `\{17\}`'s own backbone is
`\varnothing`). Continue the Trace-Clash-Freedom Reformulation (Round 11
Outline below, Steps 1–3,5 unchanged and still valid) with **Step 4
(Cross-Permanent-Inadmissibility) as the sole remaining hard content, now
explicitly scoped to only these harder instances** rather than the
general pair.

**Technique (sharpened, not replaced):** fixed-`Π` clash-freedom via
adapting single-family Escape-Confinement/Permanent-Inadmissibility to
the cross-family setting, informed by this round's jw-rigidity explorer's
diagnosis that joint coverage in general comes from a
**redundancy/density** phenomenon (small primes `2,3,7,\dots` dominate
almost every companion set: prime `2` alone realizes the joint
intersection in `70\%`–`100\%` of pairs across `~270`M cross-pairs
checked this round), not a forced algebraic coincidence between two
independently-chosen witnesses ("does witness `u` equal witness `w`" is
the wrong question). Reframe Step 4's target accordingly: does the
small-prime redundancy that empirically closes every tested pair have a
combinatorial (pigeonhole) reason, rather than continuing to hunt for
exact rigidity.

**Skeleton (Steps 1–3, 5 retained verbatim from Round 11 Outline below;
Step 4 sharpened):**
4′. **Cross-Permanent-Inadmissibility for clash-freedom, scoped to Case B
   pairs, reframed via pigeonhole rather than rigidity.** Instead of
   forcing `u=w` coincidence, attempt to show the SET of possible escape
   primes for a clashing trace-type pair `(τ,τ')` is finite by applying
   the already-certified, size-agnostic Lemma NIDF (both parts — (a)
   every companion set nonempty, (b) no infinite pairwise-disjoint
   sub-family) directly to the *escape-prime set itself* (the family of
   primes indexed by clashing pairs), rather than inventing new
   cross-family machinery from scratch — a not-yet-attempted, concrete
   adaptation of an already-proven, unconditional injection argument.

**Key lemmas (retain Round 11's; the `Π`-specific ones are now dead, add:)**
- **Escape-prime finiteness via NIDF pigeonhole (Step 4′, new framing)**
  — because Lemma NIDF's injection argument (already certified, needs no
  size bound on either family) was originally proved for one class's
  companion-set family; the same technique (map each escape prime to a
  fixed finite "anchor" companion set) is a plausible, not-yet-attempted
  adaptation to the escape-prime set specifically — worth a dedicated
  attempt before further rigidity-hunting on Case B's two instances.

**Open gaps:** Step 3 (everywhere-nonempty trace, unchanged, still open),
Step 4′ (Case-B-scoped Cross-Permanent-Inadmissibility via pigeonhole,
the crux), Step 5's assembly (unchanged).

**Cases to cover:** Case B only this round (`247:(13,19)`,
`4199:(13,17)`) — Case A pairs are sibling `sunflower-inadmissibility-
toolkit`'s job this round, do not duplicate.

**Watch out for:** do NOT re-attempt `Π:=\mathrm{comp}(a_{j_3})\cup
\mathrm{comp}(a_{j_3'})` as constructed in round 11 §8.3 — refuted, see
above, explicit counterexample on record. Do not lose **Lemma CB (Core
Blocking)** — it remains valid, certified, and still useful (guarantees
both sides of every doubly-infinite pair are automatically blocked, so
Escape-Confinement is always structurally available, no case split
needed) even though the specific `Π` built from it failed.

## Round 11 update (headline — read this first)

**Conjecture (JW) is not closed this round, but the candidate witness set
is sharpened to its smallest form yet, and one previously-unstated fact
(Lemma CB) is proved that rules out a natural false shortcut and
simplifies all future case analysis on this gap.** New this round: **Lemma
CB (Core Blocking, §8.2)** — for any doubly-infinite disjoint core pair
`(S,S')`, both `S` and `S'` are *automatically* ERD-C-blocked (never
realized); this is proved in full from already-certified facts (Lemma
NIDF(a), Lemma ERD-C) and, as a byproduct, refutes (before it could be
mis-recorded as a result) a shortcut this round's build initially explored
("if a core is realized, `Λ_S` alone trivially closes Stabilization") by
showing its hypothesis never occurs in this setting — recorded honestly in
§8.2 so it is not re-attempted. Lemma CB is then used (§8.3) to replace
Lemma FT's multi-representative transversal `U_S\cup U_{S'}` with a
strictly smaller, single-witness-per-side candidate `Π:=\mathrm{comp}
(a_{j_3})\cup\mathrm{comp}(a_{j_3'})`, via the already-certified
Escape-Confinement Lemma, unconditionally available on *both* sides of
*every* doubly-infinite pair (no case split needed — Lemma CB guarantees
the "blocked" branch always applies). The Cross-Permanent-Inadmissibility
attempt (Step 4 of the outline, the hardest content) is carried out on
this sharper `Π` and **the identical rigidity wall persists** (§8.4):
no mechanism forces the companion-side witnesses from three separately-true
intersection facts to coincide, and a genuinely new obstruction is
identified (the blocking witness `j_3`'s core need not be disjoint from
`S'`, so even the natural direct-chain repair can fail to produce a
companion-prime witness at all). This is reported honestly as an open gap,
not patched around, per the outline's explicit instruction. **Net: one new
certifiable lemma (Lemma CB), a genuine sharpening of the candidate `Π`,
and a more precisely located remaining gap — Conjecture (JW) itself
remains open, `Status` stays `partial`.**

## Round 11 Outline (proof-outliner directive — attack Conjecture (JW)
directly via a fixed-Π trace-clash-freedom reformulation, replacing Lemma
FT's rigid transversal)

**Target (unchanged): the whole problem**, via Theorem SW → Theorem 5.1
(both already certified, do not re-derive). This round retargets the sole
open gap, Conjecture (JW) (§7 of this file), following this round's
jw-lens explorer's reformulation (`/tmp/round-11/math-explorer-jw.md`) and
its own §7.4 recommendation to reuse the single-family certified toolkit
instead of further pigeonhole/transversal work.

**Technique:** fix a candidate finite `Π` up front (not built as an
index-dependent transversal like Lemma FT); reduce (JW) to two purely
combinatorial trace properties of `Π` that are checkable independent of
any single companion set's size; close the harder property
(clash-freedom) by adapting the already-certified single-family
Realized–Blocked Dichotomy (Lemma ERD-C) / Permanent-Inadmissibility Lemma
/ Escape-Confinement Lemma / No-Resurrection Lemma to the cross-family
setting, plus reuse of the certified Greedy Augmentation +
Termination-Sufficiency Lemma (from `forced-primes-well-ordering`) for the
finite-enlargement termination argument.

**Skeleton:**
1. **Trace-Clash-Freedom Reformulation.** For a fixed finite `Π` (e.g.
   containing `B_0`), define `trace(i):=comp(a_i)\cap Π` for `i\in I_S`
   (resp. `I_{S'}`). If (a) `trace(i)\ne\emptyset` for every
   `i\in I_S\cup I_{S'}` ("everywhere-nonempty trace") and (b) no realized
   trace on the `S`-side is disjoint from any realized trace on the
   `S'`-side ("clash-freedom"), then `W:=Π` satisfies Stabilization for
   `(S,S')` directly — immediate from the definitions, no further
   machinery.
2. **Finite trace-type space** (the concrete leverage Lemma FT's
   index-dependent construction lacked). Once `Π` is fixed, each side has
   at most `2^{|Π|}` possible trace types; "realized trace types" is
   automatically a finite set by pigeonhole, independent of whether
   individual companion sets `comp(a_i)` are bounded in size — this
   sidesteps `(UB_S)`-false entirely (bundle size is unbounded per the
   certified Case-II refutation, but the TRACE against a FIXED finite `Π`
   cannot itself grow past `2^{|Π|}` distinct patterns).
3. **Everywhere-nonempty trace** (open, likely easy). Use the jw
   explorer's "growth adds, does not replace" empirical finding
   (companion-set-size growth strictly extends a small backbone, never
   omits it, zero counterexamples in every tested instance) as the
   guiding conjecture; attempt via the already-certified Escape-Confinement
   Lemma: if some `i` had `trace(i)=\emptyset` entirely, `i`'s companion
   set is disjoint from `Π`; adapt Escape-Confinement (a blocked-witness's
   escapes must hit the witness's own companion set) to show any such `i`
   is confined to finitely many possibilities, or absorb `Π`'s
   construction so this is automatic by choice.
4. **Cross-Permanent-Inadmissibility for clash-freedom** (the sharpest,
   hardest gap — genuinely new mathematics, not yet attempted anywhere in
   this workspace). Suppose trace type `τ` (`S`-side) and `τ'` (`S'`-side)
   are disjoint within `Π` and both realized at `i_0\in I_S`, `j_0\in
   I_{S'}`. By the already-certified Lemma P′, `\gcd(a_{i_0},a_{j_0})>1`,
   so some shared prime `p` exists — necessarily `p\notin Π` (else
   `τ\cap τ'\ni p`, contradiction), i.e. `p` is a shared "escape" prime
   outside `Π`. Adapt the certified Permanent-Inadmissibility Lemma
   (single-family: a witness's companion set permanently blocks a whole
   class of escapes) to this cross-family pair: show that once such a
   clash `(τ,τ')` is realized once, it can only be realized via finitely
   many distinct escape primes `p` (not unboundedly many), by an argument
   structurally parallel to the already-certified Escape-Confinement Lemma
   but applied across families instead of within one.
5. **Finite repair + termination.** If step 4 gives, for each clashing
   pair `(τ,τ')`, a fixed finite set of possible escape primes, enlarge
   `Π` by adjoining all of them (a finite enlargement, since only finitely
   many trace-type pairs exist by Step 2) and repeat. Reuse the
   already-certified Greedy Augmentation Lemma + Termination-Sufficiency
   Lemma (`forced-primes-well-ordering`,
   `lemmas/lemma-greedy-augmentation-and-termination-sufficiency.md`) to
   argue this repair process terminates after finitely many rounds
   (recasting "prefix recruitment" as "clash repair" — the same
   well-ordering skeleton, a different bookkeeping target).

**Key lemmas (claim + mechanism):**
- Trace-Clash-Freedom Reformulation ⟹ (JW) — immediate, `W:=Π` is
  literally the covering witness (elementary).
- Finite trace-type space — because `Π` is fixed BEFORE looking at any
  index, at most `2^{|Π|}` trace patterns exist per side, a pigeonhole
  fact independent of `(UB_S)`'s failure.
- Cross-Permanent-Inadmissibility (open, the crux gap) — conjectured
  because the single-family Permanent-Inadmissibility/Escape-Confinement
  mechanism already shows analogous "one witness blocks a whole family of
  would-be escapes" behavior; the cross-family adaptation needs Lemma P′
  applied to the SPECIFIC pair `(i_0,j_0)` realizing the clash, then
  bounding how many DIFFERENT escape primes can ever realize the SAME
  clashing trace-type pair `(τ,τ')` — not yet proved, flagged honestly as
  the open content.
- Repair-process termination — reuses (does not re-derive) the certified
  Greedy Augmentation + Termination-Sufficiency Lemma, whose
  well-ordering/pigeonhole skeleton transfers directly to "adjoin the
  escape primes forced by each clash" instead of "adjoin the greedy
  process's per-pair recruit."

**Open gaps:** Step 3 (everywhere-nonempty trace) and Step 4
(Cross-Permanent-Inadmissibility, the genuinely new, hardest content) and
the termination bound in Step 5 (needs Step 2's finitely-many-trace-pairs
fact combined with Step 4's per-pair finite bound, not yet assembled into
one convergence argument).

**Cases to cover:** none beyond the `(S,S')` symmetric roles; `Π` may need
per-pair (not universal) tuning — this is fine, Stabilization only needs
one witness set per doubly-infinite pair.

**Watch out for:** do not conflate this round's FIXED-`Π` clash-freedom
target with Lemma FT's index-dependent transversal `U_S\cup U_{S'}` — they
are different objects; `Π` can (and empirically should, per the
"backbone" finding) be much smaller. Also watch for the possibility (not
yet ruled out) that a clashing trace-pair has infinitely many distinct
escape primes — if found on ANY instance, this refutes the whole
approach's premise and should be reported immediately, not patched
around.

## Round 10 update (headline — read this first)

**The outline-reviewer's mandatory Step-0 gap is resolved — not by proving
the bounded-size hypothesis, but by replacing the certified Δ-system
Dichotomy Lemma's role in Step 1 with a strictly more general,
unconditional argument that needs no size bound at all.** The reviewer's
point stands as stated: `lemmas/theorem-UBS-false-case-II.md` only proves
`(UB_S)` fails for *some* proper core, never that it fails (or holds) for
the *specific* `S`, `S'` of a given doubly-infinite pair, so the outline's
Step 1 literally could not proceed as written (citing a lemma whose
bounded-size hypothesis is neither verified nor verifiable for the pair at
hand). This round replaces that citation entirely: three new lemmas —
**Lemma XC** (cross-companion reduction: `rad(a_i)\cap rad(a_j)=
\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)` for any disjoint-core pair),
**Lemma NIDF** (no infinite pairwise-disjoint sub-family of companion sets
on either side of *any* doubly-infinite disjoint core pair — proved from
Lemma P′ and finiteness of individual radicals alone, no size bound
needed), and **Lemma FT** (a finite one-sided transversal `U_S`, resp.
`U_{S'}`, exists on each side, meeting every companion set on that side) —
are proved in full, unconditionally, in every regime (bounded or unbounded
companion size). This is genuinely new content, not a reformulation, and it
is strictly more general than what the outline's Step 1 needed.

**What remains open, honestly and precisely diagnosed.** The natural
candidate `W:=U_S\cup U_{S'}` is tested empirically against **two**
independently-generated hard instances — `a_1=247` (10764/6910 realized
class members through `n=20000`, `10{,}764\times6{,}910\approx7.4\times10^7`
cross pairs checked) and the workspace's hardest case, `a_1=21528751`
(597,414 cross pairs on cores `\{103\}`,`\{197\}` checked through `n=6000`)
— with **zero** violations of the *full joint* Stabilization Conjecture in
either case (§7.2 below). But the natural proof attempt for this candidate
has a genuine, precisely-located logical gap (§7.1): the two one-sided
transversal facts alone do not force the *same* witnessing prime to lie in
both companion sets of a cross pair, only in each separately. This is now
the sharpest, most precisely stated form the gap has taken across all 10
rounds of this workspace's history on this problem — a concrete conjecture
(JW), backed by ~75 million verified pairs across two structurally very
different instances, with an exact diagnosis of where combinatorics alone
runs out and (very likely) genuine number-theoretic structure (of the kind
`ERD-C`/Escape-Confinement/No-Resurrection already supply for the
single-family case) is needed to close it.

**Scope.** This round's result does **not** solve the Stabilization
Conjecture or the whole problem. It fully repairs the flagged Step-0 gap
(the mechanism no longer depends on an unverifiable/likely-false
boundedness hypothesis), proves three new general-purpose lemmas
unconditionally, and sharpens the remaining gap to an explicit, heavily
tested conjecture with a precise failure diagnosis — genuine progress, but
`Status` remains `partial`.

## Round 10 Outline (proof-outliner directive — retarget from the retired
`(UB_S)` program to the Stabilization Conjecture, via a cross-family
Δ-system/extremal argument reusing this file's own certified machinery)

**Target (unchanged): the whole problem**, via Theorem SW → Theorem 5.1
(both already certified, do not re-derive). This file's round-9 headline
(`(UB_S)` refuted in Case II, `lemmas/theorem-UBS-false-case-II.md`) is a
completed, certified milestone — do not revisit it. Per the standing Rule,
`(UB_S)`/`(MRS)`/`𝓥_S`-finiteness-VIA-BUNDLE-SIZE is retired as a route to
the whole problem; this round's retarget attacks the Stabilization
Conjecture directly, reusing this approach's own certified **Δ-system
Dichotomy Lemma** (`lemmas/lemma-delta-system-dichotomy.md`) for a
genuinely different purpose (a CROSS-family covering argument, not a
single-family bundle-count bound) — the 4th distinct mechanism in this
round's field, alongside density/pigeonhole
(`intersecting-family-covering-construction`), finite-alphabet covering-
design (`explicit-window-backbone-construction`), and well-ordering/bridge-
prime (`forced-primes-well-ordering`).

**Technique: Δ-system dichotomy applied to the two-sided companion-family
covering problem.** Fix a doubly-infinite disjoint core pair `(S,S')`. Let
`\mathcal Q_S:=\{rad(a_i)\setminus S:i\in I_S\}` (companion bundles of the
`S`-side, each a finite, but per `(UB_S)`-false-Case-II possibly UNBOUNDED
in size, set of primes) and similarly `\mathcal Q_{S'}`. The Stabilization
Conjecture for `(S,S')` is exactly: **some finite `W` hits every
`Q\in\mathcal Q_S` and every `Q'\in\mathcal Q_{S'}` such that `Q,Q'`
actually co-occur as companions of a realized cross pair** — note this is
weaker than requiring `W` hit every `Q\cap Q'` pairwise; only realized
co-occurring pairs matter, but by the greedy rule (Lemma P′) EVERY pair
co-occurs, so it is exactly the same condition.

**Skeleton:**
1. Apply the already-certified Δ-system Dichotomy Lemma to `\mathcal Q_S$
   (an infinite family of finite sets, since `I_S` is infinite by
   hypothesis): either (a) `\mathcal Q_S` contains an infinite **sunflower**
   with core `K_S$ (possibly empty) — infinitely many `Q\in\mathcal Q_S`
   pairwise-intersect only in `K_S`, with pairwise-disjoint "petals"
   `Q\setminus K_S`; or (b) `\mathcal Q_S` has no infinite sunflower, hence
   (by the classical Δ-system finite-bound direction, already used in
   `lemmas/theorem-UBS-sufficiency.md`'s Δ-system dichotomy application)
   the family is "kernel-bounded": some FIXED finite kernel set repeats as
   a subset of infinitely many `Q\in\mathcal Q_S`.
2. **Case (b) (kernel-bounded) is the easy case:** the repeating finite
   kernel `K_S` itself (finite by construction) — combined with the
   already-certified Lemma P′ forcing SOME intersection with every
   `Q'\in\mathcal Q_{S'}` — gives a natural finite-`W` candidate to test:
   does `K_S\cup K_{S'}` (both sides' repeating kernels, if both are
   case-(b)) suffice? **Open step:** prove the intersection is forced to
   land IN the kernels specifically (not in the unboundedly-growing
   petals) for infinitely many pairs — attempt via a pigeonhole argument
   on how many petal-only intersections can occur before contradicting
   Lemma P′'s density (reuse Euler-divergence-style counting from
   `lemmas/theorem-UBS-false-case-II.md`, repurposed here for a positive
   construction instead of a refutation, per this round's H100-
   stabilization explorer's opening 3 suggestion,
   `/tmp/round-10/math-explorer-H100-stabilization.md`).
2'. **Case (a) (genuine infinite sunflower, empty or nonempty core) is the
   hard case, and the one where `(UB_S)`-false's unbounded-petal-size
   phenomenon actually bites** — if `\mathcal Q_S` is an infinite sunflower
   with core `K_S` and pairwise-DISJOINT unboundedly-growing petals, no
   finite `W$ can hit every petal directly; the ONLY hope is that `K_S`
   itself (finite) already suffices, forcing every cross pair to intersect
   in the (possibly empty) core. **If `K_S=\emptyset`, this case
   structurally CANNOT be closed by a finite `W` confined to `\mathcal Q_S`
   alone** — the covering prime must then come from `\mathcal Q_{S'}`'s
   own kernel/sunflower structure instead (symmetric argument), or from a
   genuine cross-term not visible in either single-family decomposition —
   **flag this sub-case honestly as the sharpest, hardest open gap of this
   entire round's field**: an empty-core sunflower on BOTH sides would mean
   neither side's companion bundles have any small repeating structure at
   all, and Lemma P′ alone (which only guarantees SOME shared prime per
   PAIR, not a shared prime across the whole family) would need a
   genuinely new argument to still force a finite `W` — check numerically
   first (per the H100-stabilization/bridge-primes explorers' data, no
   such doubly-empty-core case has been observed in 5+ hard channels
   tested) before attempting a proof; if found, this may indicate
   Stabilization itself can fail, a genuine risk to flag upward.

**Key lemmas (claim + mechanism):**
- **Δ-system dichotomy applies to `\mathcal Q_S`, `\mathcal Q_{S'}`** —
  because both are infinite families of finite (if unbounded-in-size,
  per the certified `(UB_S)`-false result) subsets of `\mathbb N`, exactly
  the hypothesis class the already-certified Δ-system Dichotomy Lemma
  covers (no new proof needed for this step, direct application).
- **Kernel-forced intersection (Case b, open)** — because a repeating
  finite kernel, combined with Lemma P′'s per-pair forcing, plausibly
  cannot always be "dodged" by petal-only intersections without violating
  a density/counting bound — mechanism NOT yet built, reuses the
  Euler-divergence counting TOOL (not the `(UB_S)` conclusion) from the
  already-certified refutation lemma for a new, positive purpose.

**Open gaps:** the whole of Step 2 (kernel-forcing) and Step 2' (whether
empty-core-on-both-sides can actually occur, and if so what replaces the
argument) are open — genuinely new mathematics, not yet attempted anywhere
in this workspace.

**Cases to cover:** the Δ-system dichotomy's own (a)/(b) split, on EACH
side (`S` and `S'`) independently, giving up to 4 joint sub-cases
(kernel/kernel, kernel/sunflower, sunflower/kernel, sunflower/sunflower) —
enumerate all 4 explicitly when building, do not just handle the "easy"
kernel/kernel case and assert the rest "similarly."

**Watch out for:** do not silently assume `K_S$ (the repeating kernel) is
nonempty — an empty kernel is a valid, and per Case 2' the HARDEST,
outcome of the Δ-system dichotomy; also do not confuse this file's
already-certified Δ-system application (bounding COUNT of same-family
bundles, from the `(UB_S)`-sufficiency proof) with this round's NEW
application (forcing a shared prime ACROSS two different families) — same
lemma, genuinely different use, keep the two applications' hypotheses
separate in the writeup.

## Round 9 update (headline — read this first)

**`(UB_S)` is now FULLY REFUTED, rigorously and unconditionally, within
Case II.** Precisely: **it is impossible for `(UB_S)` to hold for every
proper core `S⊊P_1` simultaneously**, whenever `|P_1|≥2` and no prime
divides every term (Case II — the only regime in which the notion of
"proper core" is even meaningful; Case I is already fully solved separately
by Theorem CI and untouched by any of this). This settles the question the
outline-reviewer flagged this round (§1d of `/tmp/round-9/outline-
reviewer.md`): the corrected, weaker Density Sub-Lemma
(`∃c>0: |I_{P_1}∩[1,N]|≤(1-c)N` for all large `N`) is proved **in full**
below (§6.1), the classical Landau Count Lemma is proved **in full from
scratch** (§6.2–6.3, via Turán's elementary second-moment argument plus
Euler's classical proof that `Σ_p1/p` diverges — neither previously in this
workspace), and the two are assembled into a complete contradiction (§6.4).

**The key structural finding this round**: the corrected Density Sub-Lemma
does **not** need an independent, unconditional proof about the greedy
recursion's own dynamics (which is what the round-9 outline's Step 3
envisioned, and what stalled every density-flavoured attempt in rounds
3–8). Instead, it follows almost for free **from the Step-1 assumption
`(UB_S)` itself**, via the already-certified `theorem-UBS-sufficiency.md` /
`§4c` chain: assuming `(UB_S)` gives *exact* periodicity `a_{n+T}=a_n+L`
for *every* `n≥1` (Theorem 5.1), and exact periodicity of `a_n` forces
exact periodicity of "which primes divide `a_n`" (elementary arithmetic of
an arithmetic progression), which forces the top-core membership `n∈I_{P_1}`
itself to be an exactly periodic subset of `ℕ` with some fixed period `τ`
— and a fixed-period set has density exactly `|R|/τ` for some `R⊆
\{0,\dots,\tau-1\}`, which **cannot be `τ/τ=1`** without contradicting the
standing Case II hypothesis. This is a materially easier route than the
outline anticipated, and it is the genuine new content of this round.

**Scope, stated honestly per dispatch instruction 4.** This refutes the
round-8 sufficient hypothesis `(UB_S)` (and hence retires the whole
`(UB_S)`/`(MRS)`/`𝓥_S`-finiteness-via-companion-bundle-size route opened in
round 8) — it does **not** refute FCBC or the whole problem, and does
**not** by itself solve anything. Per the outline's own Step 6, this is a
"kill" finding of the same kind as round 2/3's refutations of
`H_n`/`W`-finiteness: it redirects all future effort away from a dead
target. FCBC itself remains open, to be attacked by this round's sibling
approaches (`explicit-window-backbone-construction`,
`intersecting-family-covering-construction`).

## Round 9 Outline (proof-outliner directive — pivot from proving `(UB_S)`
to rigorously settling it, attempting the FALSE direction)

**Context (read first).** Round 9's explorers found strong, reproducible
numerical evidence, pushed ~100-400x past round 8's tested range, that
`(UB_S)` (this file's round-8 target, proved sufficient for the whole
problem via `theorem-UBS-sufficiency.md`) is very likely **FALSE**:
companion-bundle size keeps setting new records with no blocking witness
found in 1.3M terms. Per dispatch, either direction is valuable — a
rigorous refutation redirects all future effort away from a dead target,
exactly as round 2/3's refutations of `H_n`/`W`-finiteness did. **New
target this round: prove `(UB_S)` FALSE**, via a genuinely new tool for
this workspace — a classical analytic density argument (Landau/Hardy-
Ramanujan: integers with a bounded number, `k`, of distinct prime factors
have density 0), combined with the already-certified linear growth bound
(`lemmas/lemma-1-uniform-gap-bound.md`).

**Do not** continue trying to prove `(UB_S)` true via count-bounding
machinery (Δ-system/Escape-Confinement/RBD) — already diagnosed, this
file's own round-8 §5, as structurally unable to bound bundle *size*; round
9 additionally now doubts the target's truth.

Skeleton (full detail, key-lemma mechanisms, and explicit watch-outs in
`/tmp/round-9/proof-outliner.md` under `sunflower-bundle-closure`):
1. Assume `(UB_S)` for every proper core (finitely many, so a uniform bound
   `B` on `ω(a_n)` for `n∉I_{P_1}` follows by taking a max).
2. Growth Lemma (reuse, certified): `a_n=O(n)`, so `{a_n:n≤N}` packs into
   an interval of length `O(N)`.
3. **Density Sub-Lemma (new, needs proof):** `|I_{P_1}∩[1,N]|=o(N)` — the
   top core does not have density 1 (infinitude of proper-imprint indices
   is already certified content; the builder needs the *rate*).
4. **Landau Count Lemma (new, prove from scratch — classical but absent
   from `knowledge_base.md`/crux corpus, confirmed by round-9 search):**
   `|\{m≤X:ω(m)≤k\}|=o(X)` for fixed `k`, via a Mertens-induction sieve
   argument (`Σ_{p≤X}1/p→∞`).
5. Contradiction: Step 1's bound forces `N-o(N)` values of `ω≤B` inside an
   `O(N)`-length interval, but Step 4 caps that count at `o(N)` —
   `N=o(N)`, contradiction. `(UB_S)` is false.
6. Honest scope note: this kills the round 4-8 `(UB_S)`/`(MRS)`/`𝓥_S`
   route as a path to the whole problem (do not re-attempt it in any
   approach going forward), but does **not** itself resolve FCBC or the
   whole problem — that is left to this round's sibling approaches
   (`explicit-window-backbone-construction`, `intersecting-family-
   covering-construction`, `forced-primes-well-ordering`), all of which now
   attack FCBC directly, without needing `(UB_S)`.

Open gaps: Step 3 (explicit density rate) and Step 4 (from-scratch proof of
the classical count bound) are the two concrete tasks.

## Approaches tried (round 13, this round)

- **Round 13 (this round, full build).** Per the round-13 outline's
  directive (attempt the GENERAL existence argument for round 13's new
  low-index-witness-chaining mechanism, complementary in scope to sibling
  `forced-primes-well-ordering`'s concrete-instance work): formalized
  Conjecture (WCE) precisely (§10.0–10.1), proved the general **Chaining
  Sufficiency Theorem** (§10.2, full proof, no gaps) that turns any
  finite witness collection passing a purely finite combinatorial check
  into a valid proof of Conjecture (JW) for the pair, verified it
  reproduces the round-13 explorer's hand-built `4199:(13,17)` case tree
  exactly (§10.3), proved the **Single-Witness-Per-Side Insufficiency
  Proposition** (§10.5, a clean *iff* characterization subsuming round
  11/12's separate ad hoc counterexamples), and gave an explicit finite
  computation (§10.6, using this file's own already-recorded data) showing
  the theorem is non-vacuous — the "free" Lemma FT transversal does not
  automatically satisfy it. Attempted the outline's Step 2 (general
  existence mechanism via Lemma ERD-C + Escape-Confinement) and found,
  honestly, that no certified tool guarantees the needed witnesses exist
  in general (§10.7); proved instead that Conjecture (WCE) in full
  generality **cannot be easier than Conjecture (JW)** (WCE⟹JW, §10.4/
  10.7a) and that the natural converse construction (JW⟹WCE) is
  genuinely blocked by the same "off-`W_0`-companion-prime" issue as this
  file's own §7.4 rigidity gap (§10.7b) — i.e. (WCE) does not escape the
  workspace's sole standing gap, it reformulates it constructively. **Net:
  no closure of (WCE) or (JW), but a new, general, reusable proof
  technique (usable by sibling approaches on their own concrete instances)
  plus an honest, rigorous correction of this round's outline's "possibly
  easier/complementary" framing — `Status` stays `partial`.**

## Approaches tried (round 12, this round)

- **Round 12 (this round, full build).** Per the round-12 outline's
  directive (retire the refuted `Π` of round 11 §8.3, retarget the
  Trace-Clash-Freedom Reformulation to "Case B" pairs — those with no
  nonempty realized single-side backbone on either side — and attempt the
  new Step 4′ idea, applying the certified NIDF-pigeonhole injection
  argument directly to the escape-prime set): attempted the escape-prime
  finiteness idea on the two confirmed Case B instances (`247:(13,19)`,
  `4199:(13,17)`), (1) formally identified the exact structural reason
  the naive one-sided pigeonhole argument cannot bound the *joint*
  escape-prime set (§9.2 — new diagnostic content, not previously stated
  this precisely); (2) built a genuinely new, non-trivial refinement of
  round 11's `Π` construction — the **Matched-Witness** candidate, using
  smarter witness selection (still via already-certified Lemma CB +
  Escape-Confinement, no new machinery) to get *equal* companion sets on
  both sides of a pair (`\{2,3\}` in both tested instances, independently
  discovered) — and **explicitly refuted** it with hand-verifiable
  counterexamples on both instances (§9.3–9.4), closing off a natural next
  attempt before it could waste a future round's effort. Extensive fresh
  numerics (own from-scratch generator, ~101M cross-pairs checked across
  the two instances combined) support, but do not prove, Conjecture (JW)
  itself remains plausible via the already-known `W=\{2,3,5,7\}`-style
  candidates. **Net: no closure of Case B, but genuine new negative/
  diagnostic content that sharpens exactly what a future round's mechanism
  must supply (a cross-index/cross-witness linking fact that no currently
  certified lemma provides) — `Status` stays `partial`.**

## Approaches tried (round 11, this round)

- **Round 11 (this round, full build).** Per the round-11 outline's directive
  (attack Conjecture (JW) via a fixed finite `Π`, reduced to two checkable
  trace properties, closing clash-freedom by adapting the certified
  single-family toolkit — Lemma ERD-C, Permanent-Inadmissibility,
  Escape-Confinement — to the cross-family setting) and the jw-lens
  explorer's finding (`/tmp/round-11/math-explorer-jw.md`) that the
  everywhere-nonempty-trace step reduces to (b) alone (see §8.1), this round:
  (1) proved a clean, previously-unstated **Lemma CB (Core Blocking)**: for
  *any* pair of disjoint nonempty cores `S,S'` with `I_S,I_{S'}` both
  nonempty (in particular any doubly-infinite pair), **both `S` and `S'` are
  automatically ERD-C-*blocked*, never realized** — a genuine, fully proved
  new fact (§8.2) that also **rules out**, honestly and explicitly, a natural
  but false shortcut this round initially attempted (an "if `S` is
  ERD-C-realized, `Λ_S` alone trivially solves Stabilization" argument,
  refuted by Lemma CB itself before being written up as a claimed result —
  recorded in §8.2's remark so no future round re-attempts it); (2) used
  Lemma CB to derive a **strictly smaller, more natural one-sided covering
  pair** than Lemma FT's multi-representative transversal — a *single*
  witness set on each side, `comp(a_{j_3})`/`comp(a_{j_3'})`, via the
  already-certified Escape-Confinement Lemma applied directly to `κ:=S`
  (resp. `S'`), unconditionally available for *every* doubly-infinite pair
  (§8.3); (3) attempted Cross-Permanent-Inadmissibility (Step 4, the outline's
  hardest content) on this smaller candidate `Π:=\mathrm{comp}(a_{j_3})\cup
  \mathrm{comp}(a_{j_3'})` and found the identical rigidity wall persists
  (§8.4) — precisely diagnosed and reported honestly as still open, not
  patched around. **Net result: genuine new certified-quality content (Lemma
  CB, the sharper one-sided covering pair) plus a corrected sharpening of
  Conjecture (JW)'s statement to the smallest candidate `Π` yet found in
  this file's history — Conjecture (JW) itself remains open.**

## Approaches tried

- **Round 8 (this round, full build).** Filled in the outline's Δ-system
  (sunflower) closure mechanism completely and rigorously. **Result: a
  complete, unconditional proof of the implication**

  > For every proper nonempty core `S⊊P_1`, Hypothesis `(UB_S)` (companion
  > bundles realized on the class-`S` index set `I_S` have uniformly bounded
  > size) **implies** `Λ_S` is finite.

  This closes, in full, *both* open sub-gaps the outline had flagged as
  needed for this mechanism (core-avoiding witness existence, and the
  finite/infinite status of `I_S`) — not by proving them as separate
  hypotheses, but by proving they are never actually needed: a new bridge
  lemma (**Lemma ERD-C**, built from the already-certified Lemma ER + Lemma
  P′ + the Permanent-Inadmissibility Lemma) shows every proper core `S` is
  *automatically* in one of exactly two mutually exclusive situations —
  "`S` is itself realized as a bare radical" (in which case `Λ_S` is
  finite **unconditionally, with no need for `(UB_S)` at all** — a new,
  previously unstated shortcut, **Lemma SR**) or "`S` is permanently
  blocked by some witness" (in which case the outline's Δ-system machinery
  applies with the needed witness supplied for free). Combined with the
  already-certified reduction chain (Theorem 5.1 ← Lemma MS ← Theorem V +
  Theorem CD/Lemma TC ← Λ_S-Reduction Lemma), this yields:

  > **`ω(a_n)=O(1)`, restricted to indices outside the top-core class
  > `I_{P_1}` (equivalently, sup over the finitely many proper cores `S` of
  > `sup_{i\in I_S}ω(a_i)`, a strictly weaker requirement than a single
  > global bound) `⟹` the entire problem (`a_{n+T}=a_n+L` for every
  > `n≥1`).**

  This is a genuinely new complete conditional bridge from the
  `ω`-boundedness hypothesis all the way to the theorem — the round-3
  bridge (`lemmas/lemma-omega-bound-key-lemma.md`) only reached "the
  Domination Lemma's dominant primes form a finite set `Q`," and
  Propositions ND1/ND2 (round 3) proved the natural ways of turning that
  set into an FCBC covering set **fail**. This approach's bridge uses an
  entirely different mechanism (Δ-system/pigeonhole existence argument, not
  a Domination-Lemma argmax construction) and does not hit that obstruction.
  `(UB_S)`/`ω(a_n)=O(1)` **itself remains open** — this round did not close
  it, and a genuine, honestly-reported attempt (§5 below) to push further
  using the newly available machinery stalls at the same difficulty round 3
  identified (any bound derived from `a_n`'s numerical size alone gives at
  best `O(\log n/\log\log n)`, not `O(1)`; a true `O(1)` bound, if it holds,
  needs a combinatorial argument specific to the greedy recursion, not a
  size/divisor-count argument).

## Approaches tried (round 9, this round)

- **Round 9 (this round, full build).** Per the outline-reviewer's mandatory
  correction (§1d of `/tmp/round-9/outline-reviewer.md`: the literal `o(N)`
  form of the Density Sub-Lemma is very likely FALSE — independently
  measured stable positive top-core densities `0.1163` (`a_1=247`) and
  `0.0204` (`a_1=2747`) — but the weaker form
  `|I_{P_1}∩[1,N]|≤(1-c)N` suffices), retargeted Step 3 to this corrected
  weaker statement and **proved it in full** (§6.1 below), using a genuinely
  different and simpler mechanism than the outline envisioned: deriving it
  as a consequence of the very periodicity that `(UB_S)` (the Step-1
  contradiction hypothesis) already certifiably implies, rather than as an
  independent fact about the raw greedy recursion. Also proved, completely
  from scratch, the classical Landau Count Lemma (§6.2–6.3, via Turán's
  1934 elementary second-moment argument, itself resting only on Euler's
  classical elementary proof that `Σ_p 1/p` diverges — both confirmed absent
  from `knowledge_base.md`/the crux corpus by this round's outliner, both
  proved here without recourse to Mertens' theorem's precise `\log\log X`
  rate, only its qualitative divergence, which simplified the writeup
  considerably). Assembled the full contradiction (§6.4): **`(UB_S)` is
  false for every `a_1` with `|P_1|\ge2` in Case II.** This is a complete,
  unconditional, gap-free refutation — matching the outline's own honest
  framing that either truth-value would be valuable content, and
  successfully closing the FALSE direction.

## Approaches tried (round 10, this round)

- **Round 10 (this round, full build).** Per the outline-reviewer's
  mandatory Step-0 directive (`/tmp/round-10/outline-reviewer.md` §2): the
  outline's Step 1 cited the certified Δ-system Dichotomy Lemma
  (`lemmas/lemma-delta-system-dichotomy.md`) for the companion-bundle
  family `\mathcal Q_S` of a doubly-infinite pair's `S`-side, but that
  lemma's bounded-companion-size hypothesis is neither established nor
  establishable for a specific `S` (the certified refutation
  `theorem-UBS-false-case-II.md` only shows *some* proper core is
  unbounded, not the specific `S` in question) — so Step 1 could not
  literally proceed. Resolved this by building an entirely new,
  unconditional toolkit (Lemma XC, Lemma NIDF, Lemma FT, §7 below) that
  needs **no** size-boundedness hypothesis on either side of the pair at
  all, replacing the flawed citation outright rather than attempting to
  discharge its hypothesis. Pushed the resulting construction (`W:=U_S\cup
  U_{S'}`) as far as rigorously possible: it is proved to hit every
  companion set on *each side individually* (Lemma FT), but the *joint*
  Stabilization Conjecture (hitting `\mathrm{comp}(a_i)\cap\mathrm{comp}
  (a_j)` for every cross pair simultaneously) is not established — the
  natural combinatorial proof attempt is carried out in full and the exact
  point where it stalls is identified and explained (§7.1), then tested
  computationally against two independent, structurally different hard
  instances with zero violations found in either (§7.2, ~75 million pairs
  total, not previously reported at this scale for a *specific pair's
  joint* cross-covering check in this workspace). This is genuinely new
  content this round: three new certifiable lemmas, a fully repaired Step
  0, and the sharpest, most precisely diagnosed statement of the remaining
  gap in this file's 10-round history.

## Current best

This section contains the complete, self-contained proof of this round's
result. Everything through §4 is a full, gap-free proof (modulo already
reviewer-certified lemmas cited by name, imported rather than re-proved,
per this workspace's lemma-cache convention). §5 is the honest report of
where the remaining hypothesis `(UB_S)` stalls. §7 (round 10, new) is a
fully rigorous, unconditional cross-family reduction toward the
Stabilization Conjecture, with an honest, precisely diagnosed remaining
gap.

### 0. Notation and the reduction chain (cite, do not re-derive)

`P_i:=\mathrm{rad}(a_i)` (set of primes dividing `a_i`); `P_1:=\mathrm{rad}(a_1)`,
`k:=|P_1|`. For a nonempty finite set of primes `C`, write
`\mathrm{comp}_S(C):=C\setminus P_1` when convenient, and for an index `j`,
`\mathrm{comp}(a_j):=\mathrm{rad}(a_j)\setminus P_1`.

`M_n\subseteq\{1,\dots,n\}` is the set of `n`-minimal indices (Lemma W3,
`lemmas/lemma-W2-W3-patch-and-minimal-radical-reduction.md`): `i\in M_n`
iff no `k\in\{1,\dots,n\}` has `P_k\subsetneq P_i`. `\mathcal M_n:=\{P_i:i\in
M_n\}`, `\mathcal V:=\bigcup_{n\ge1}\mathcal M_n` (every radical value ever
`n`-minimal, at any finite `n`).

For a proper nonempty core `S\subsetneq P_1`: `I_S:=\{i\ge1:P_i\cap
P_1=S\}` (all indices with exact `P_1`-imprint `S`); `\mathcal
V_S:=\{C\in\mathcal V: C\cap P_1=S\}` (Theorem CD notation); `\Lambda_S:=
\bigcup_{C\in\mathcal V_S}(C\setminus S)`.

**Already-certified facts used, cited by name (imported, not re-proved
here):**

- **Theorem 5.1** (Master Conditional Theorem,
  `lemmas/theorem-5.1-master-conditional-theorem.md`): if a finite set of
  primes `H` satisfies `H\cap P_i\cap P_j\ne\varnothing` for every `i<j`
  (FCBC), then `a_{n+T}=a_n+L` for every `n\ge1`, explicit `T,L`.
- **Lemma MS** (`lemmas/lemma-MS-minimal-radical-stabilization-
  sufficiency.md`): Hypothesis (MRS) — `\mathcal M_n` eventually constant —
  implies FCBC.
- **Theorem V** (`lemmas/theorem-V-veto-finite-iff-MRS.md`): `\mathcal V`
  finite `\iff` (MRS).
- **Theorem CD / Lemma TC**
  (`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`): `\mathcal V=
  \bigsqcup_{\varnothing\ne S\subseteq P_1}\mathcal V_S`; `\mathcal V` finite
  `\iff \mathcal V_S` finite for each of the `\le2^k-1` nonempty `S\subseteq
  P_1`; and `\mathcal V_{P_1}=\{P_1\}` unconditionally (the top core needs no
  hypothesis).
- **Λ_S-Reduction Lemma**
  (`lemmas/lemma-lambda-S-reduction-and-single-companion-finiteness.md`):
  `\mathcal V_S` finite `\iff \Lambda_S` finite.
- **Lemma P′** (pairwise global intersection,
  `lemmas/lemma-P-prime-pairwise-intersecting.md`): `P_i\cap P_j\ne
  \varnothing` for every `i<j` of the whole sequence.
- **Lemma ER** (Eventual Realization Dichotomy,
  `lemmas/lemma-ER-eventual-realization-dichotomy.md`): if `y>a_1` and
  `\gcd(y,a_i)>1` for every `i\ge1`, then `y=a_m` for some `m\ge1`.
- **Permanent-Inadmissibility Lemma**
  (`lemmas/lemma-permanent-inadmissibility.md`): if some index `j` has
  `\mathrm{rad}(a_j)\cap C=\varnothing`, no term with radical exactly `C`
  can appear at any index `>j`.
- **No-Resurrection Lemma** (part of `theorem-V-veto-finite-iff-MRS.md`,
  Route 1): if some `k\ge1` has `P_k\subsetneq C`, then `C\notin\mathcal
  M_m` for every `m\ge k`.
- **Escape-Confinement Lemma** (`lemmas/lemma-escape-confinement.md`): fix a
  proper core `S` and a bare value `\kappa=S\cup Q` (`Q\cap P_1=
  \varnothing`) blocked by witness `j_3` (`\mathrm{rad}(a_{j_3})\cap\kappa=
  \varnothing`). Then every "escape" `i\in I_S` with `P_i\supsetneq\kappa`
  satisfies `P_i\cap\mathrm{comp}(a_{j_3})\ne\varnothing`.

**Consequence used repeatedly below (immediate from the definitions):**
for `C\in\mathcal V_S`, `C\cap P_1=S`, so `S\subseteq C`, and the map
`C\mapsto C\setminus S` is a **bijection** `\mathcal V_S\to\{C\setminus S:
C\in\mathcal V_S\}=:\mathcal Q_S` (injective: if `C\setminus S=C'\setminus
S` and `C\cap P_1=C'\cap P_1=S`, then `C=(C\cap P_1)\cup(C\setminus P_1)=
S\cup(C\setminus S)=S\cup(C'\setminus S)=C'`, using `S=C\cap P_1` and
`C\setminus S=C\setminus P_1` since `S\subseteq P_1`). Consequently
`\mathcal V_S` finite `\iff\mathcal Q_S` finite, and `\Lambda_S=\bigcup
\mathcal Q_S`.

**Target of this file.** Prove: `\mathrm{(UB_S)}\implies\mathcal V_S`
finite, for every proper nonempty core `S\subsetneq P_1`, where

`\mathrm{(UB_S)}`: `\sup\{|P_i\setminus S| : i\in I_S\}<\infty`.

Combined with the certified chain above, this gives: **if `(UB_S)` holds
for every one of the finitely many (`\le2^k-2`) proper cores, the whole
problem is solved** (no hypothesis is needed on the top core `S=P_1`, by
Lemma TC).

### 1. Lemma ERD-C (Eventual Realization Dichotomy for radical classes)

**Statement.** Let `C` be a nonempty finite set of primes. Exactly one of
the following holds:

(i) **`C` is realized**: `\exists` a finite index `m\ge1` with `P_m=C`.

(ii) **`C` is blocked**: `\exists` a finite index `j\ge1` with
`\mathrm{rad}(a_j)\cap C=\varnothing`; and then `C` is **never** realized at
any index.

**Proof.** *Well-definedness of a canonical test integer.* Let
`n(C):=\prod_{p\in C}p`. For `t\ge1`, `n(C)^t` has radical exactly `C`
(squarefree kernel unaffected by repeated powers), and `n(C)^t\to\infty` as
`t\to\infty`; also `a_1` is a fixed integer, so some `t_0` gives
`n(C)^{t_0}>a_1`. Let `T_C:=\min\{x>a_1:\mathrm{rad}(x)=C\}`, well-defined
by well-ordering (the set is nonempty, containing `n(C)^{t_0}`, or a larger
power if needed).

*Mutual exclusion.* Suppose (ii) holds with witness `j`. Suppose toward a
contradiction some index `i` had `P_i=C`. Two exhaustive cases: if `i>j`,
this is directly excluded by the Permanent-Inadmissibility Lemma
(contradiction). If `i\le j`: first, `i\ne j`, since `P_j\cap C=
\varnothing` (witness property) while `P_i=C\ne\varnothing` would force
`P_i\cap C=C\ne\varnothing`, i.e. `P_i\ne P_j` is needed — concretely, `i=j`
would give `P_j=C`, so `P_j\cap C=C\ne\varnothing`, contradicting the
witness property directly; so `i\ne j`, and combined with `i\le j` this
gives `i<j` strictly. Lemma P′ then gives `\gcd(a_i,a_j)>1`, i.e. `P_i\cap
P_j\ne\varnothing`, i.e. `C\cap P_j\ne\varnothing` (using `P_i=C`),
contradicting the witness property again. Both cases (`i>j` and `i\le j`)
give a contradiction, so no index realizes `C` — (i) fails whenever (ii)
holds, confirming exclusivity, and (ii)'s "never realized" clause is proved
as a byproduct.

*Exhaustiveness.* Suppose (ii) fails: `\mathrm{rad}(a_j)\cap C\ne
\varnothing` for **every** `j\ge1`. In particular `\gcd(T_C,a_j)>1` for
every `j` (since `\mathrm{rad}(T_C)=C` and `C\cap\mathrm{rad}(a_j)\ne
\varnothing` produces a common prime factor). Since `T_C>a_1`, Lemma ER
applies directly to `y:=T_C`, giving `T_C=a_m` for some `m\ge1`, i.e.
`P_m=\mathrm{rad}(T_C)=C`: (i) holds. `\blacksquare`

*(This is a genuinely new bridge lemma — Lemma ER as certified is stated
for a single integer `y`; Lemma ERD-C upgrades it to a radical-class-level
dichotomy by supplying the canonical test integer `T_C` and combining with
Lemma P′ and Permanent-Inadmissibility for the mutual-exclusion direction.
No circularity: only already-certified facts are used.)*

### 2. Lemma SR (Self-Realized core shortcut) — unconditional, no `(UB_S)` needed

**Statement.** If a proper nonempty core `S\subsetneq P_1` is realized in
the sense of Lemma ERD-C (case (i) applied to `C:=S`, i.e. some index `n_0`
has `P_{n_0}=S` exactly), then `\mathcal V_S` is finite; explicitly
`\mathcal V_S\subseteq\{S\}\cup\bigcup_{n=1}^{n_0-1}\mathcal M_n`, a finite
set.

**Proof.** Let `C\in\mathcal V_S` with `C\ne S`. Since `S=C\cap P_1
\subseteq C` always (Consequence in §0) and `C\ne S`, `S\subsetneq C`
strictly. Since `C\in\mathcal V`, `C\in\mathcal M_n` for some `n\ge1`
(definition of `\mathcal V`). If `n\ge n_0`: `P_{n_0}=S\subsetneq C`, so the
No-Resurrection Lemma (with `k:=n_0\le n`) gives `C\notin\mathcal M_n`,
contradiction. So `n<n_0`, i.e. `n\in\{1,\dots,n_0-1\}`, giving `C\in
\mathcal M_n\subseteq\bigcup_{n=1}^{n_0-1}\mathcal M_n`. Hence every element
of `\mathcal V_S` other than `S` itself lies in the fixed finite set
`\bigcup_{n=1}^{n_0-1}\mathcal M_n` (a union of `n_0-1` finite sets, each of
size `\le n\le n_0-1`, so finite). `\blacksquare`

**No hypothesis beyond `S` being realized is used** — in particular
`(UB_S)` plays no role in this case.

### 3. The trivial finite-`I_S` case

If `I_S` is finite, `\mathcal V_S\subseteq\{P_i:i\in I_S\}` (every element
of `\mathcal V_S` equals `P_i` for some actual index `i`, which necessarily
has imprint `S`, i.e. `i\in I_S`, by Theorem CD's proof), a finite set, so
`\mathcal V_S` is finite. (This case needs no hypothesis either, and shows
the argument below — which derives a contradiction from `\mathcal V_S`
infinite — never actually needs "`I_S` infinite" as a separate standing
assumption: `\mathcal V_S` infinite forces `I_S` infinite automatically, so
no gap of the kind the outline flagged as "Open gap 2" arises.)

### 4. Main Theorem: `(UB_S)\implies\Lambda_S` finite

Fix a proper nonempty core `S\subsetneq P_1`. By §3, assume `I_S` infinite
(else done). Apply Lemma ERD-C to `C:=S`.

**Case (i): `S` is realized.** Lemma SR gives `\mathcal V_S` finite
directly (no use of `(UB_S)`), hence `\Lambda_S` finite by the
Λ_S-Reduction Lemma. Done.

**Case (ii): `S` is blocked**, by some fixed witness `j_3`
(`\mathrm{rad}(a_{j_3})\cap S=\varnothing`), and `S` is never realized at
any index. Assume `(UB_S)` holds, with bound `M:=\sup_{i\in I_S}|P_i
\setminus S|<\infty`. Suppose, toward a contradiction, `\mathcal V_S` is
infinite; equivalently (§0) `\mathcal Q_S:=\{C\setminus S:C\in\mathcal
V_S\}` is infinite, a family of **pairwise distinct** finite sets (the
bijection of §0), each of size `\le M` (since every `C\in\mathcal V_S`
equals `P_i` for some actual `i`, necessarily `i\in I_S`, so `|C\setminus
S|=|P_i\setminus S|\le M` by `(UB_S)`).

#### 4a. The Δ-system (sunflower) dichotomy — proved from scratch

**Lemma (Δ-system dichotomy for uniformly bounded finite-set families).**
Let `\mathcal F` be an infinite family of pairwise distinct finite sets,
each of size `\le M` (`M\ge0` fixed), drawn from an arbitrary — possibly
infinite — universe. Then `\mathcal F` has an infinite sub-family
`\mathcal F'` that is either

(a) **pairwise disjoint**, or

(b) a **sunflower**: there is a fixed nonempty set `Y` (the *core*) with
`Y\subsetneq F` for every `F\in\mathcal F'`, and the *petals*
`\{F\setminus Y:F\in\mathcal F'\}` are pairwise disjoint and nonempty.

**Proof.** By induction on `M`.

*Base case `M=0`.* Every `F\in\mathcal F` has `|F|\le0`, i.e. `F=
\varnothing`. Since `\mathcal F`'s members are pairwise distinct, `\mathcal
F` has at most one member — contradicting infinitude, so this case is
vacuous (never occurs for an infinite family); no statement to prove.
[Equivalently one may simply note infinite families with `M=0` cannot
exist, so the base case is trivially satisfied by vacuity. The same
vacuity argument shows, more generally, that an infinite family of
pairwise-distinct sets all containing a fixed element `u`, each of size
`\le t`, forces `t\ge1` whenever the family has more than one member with
size exactly `1` — since two distinct sets of size `\le1` both containing
`u` would both equal `\{u\}`, contradicting distinctness. This resolves
the only place the induction could look circular: in the inductive step
below, when the pigeonhole argument produces an infinite family `\mathcal
F_u'` of sets of size `\le M-1`, this **automatically forces** `M-1\ge1`
(i.e. `M\ge2`) unless `\mathcal F_u'` is itself impossible for the same
distinctness reason as here — so if `M=1`, the "process terminates" branch
of the inductive step below can never actually produce an infinite
`\mathcal F_u`, and the dichotomy is satisfied instead directly by the
"process does not terminate" branch (case (a)). No contradiction, no gap:
the induction hypothesis at `M-1=0` is invoked, if at all, only vacuously
(on a family that provably cannot be infinite), so it is never used to
derive a false conclusion.]

*Inductive step.* Assume the Lemma holds for bound `M-1` (`M\ge1`). Let
`\mathcal F` be infinite, sets of size `\le M`.

Build a sub-family greedily: pick `F_1\in\mathcal F` arbitrarily; having
picked pairwise disjoint `F_1,\dots,F_r`, if some `F\in\mathcal F` is
disjoint from `F_1\cup\dots\cup F_r`, pick `F_{r+1}:=F` and continue.

- If this process never terminates, `\{F_1,F_2,\dots\}` is an infinite
  pairwise-disjoint sub-family: case (a) holds (with `\mathcal
  F':=\{F_1,F_2,\dots\}`).
- If it terminates after finitely many steps, we obtain a **finite**
  maximal pairwise-disjoint collection `F_1,\dots,F_r` (`r\ge1`, or `r=0`
  if `\mathcal F=\varnothing`, excluded since `\mathcal F` infinite) such
  that **every** `F\in\mathcal F` intersects `U:=F_1\cup\dots\cup F_r`
  (else the process would have continued). `U` is finite, `|U|\le rM`.
  Since `\mathcal F\setminus\{F_1,\dots,F_r\}` is still infinite (removed
  only finitely many sets) and every member of it intersects the finite set
  `U`, by pigeonhole some fixed `u\in U` lies in infinitely many members of
  `\mathcal F\setminus\{F_1,\dots,F_r\}` — call this infinite sub-family
  `\mathcal F_u` (every `F\in\mathcal F_u` has `u\in F`).

  Consider `\mathcal F_u':=\{F\setminus\{u\}:F\in\mathcal F_u\}`, an
  infinite family (the map `F\mapsto F\setminus\{u\}` is injective on
  `\mathcal F_u` since all `F\in\mathcal F_u` contain `u` and are pairwise
  distinct, so `F\setminus\{u\}` determines `F=(F\setminus\{u\})\cup\{u\}`
  back) of pairwise distinct sets of size `\le M-1`. By the inductive
  hypothesis, `\mathcal F_u'` has an infinite sub-family `\mathcal F_u''`
  that is pairwise disjoint or a sunflower with some core `Y'`.

  - If `\mathcal F_u''` is pairwise disjoint: let `\mathcal F':=\{F\in
    \mathcal F_u : F\setminus\{u\}\in\mathcal F_u''\}` (infinite, in
    bijection with `\mathcal F_u''`). Every `F\in\mathcal F'` contains `u`,
    and the petals `F\setminus\{u\}` (`=` the corresponding member of
    `\mathcal F_u''`) are pairwise disjoint by hypothesis and nonempty
    unless `F=\{u\}` for more than one `F` — impossible since members of
    `\mathcal F_u''`, hence of `\mathcal F'`, are pairwise distinct, so at
    most one `F\in\mathcal F'` has `F\setminus\{u\}=\varnothing`; discard it
    if present (still leaves an infinite sub-family). So `\mathcal F'` is a
    sunflower with core `Y:=\{u\}`: case (b).
  - If `\mathcal F_u''` is a sunflower with core `Y'` (petals
    `F\setminus\{u\}\setminus Y'` pairwise disjoint and nonempty, for
    `F\setminus\{u\}` ranging over `\mathcal F_u''`): let `\mathcal
    F':=\{F\in\mathcal F_u:F\setminus\{u\}\in\mathcal F_u''\}`, infinite.
    Every such `F` contains `u` and `Y'` (so contains `Y:=Y'\cup\{u\}`), and
    the petals `F\setminus Y=(F\setminus\{u\})\setminus Y'` are exactly the
    (pairwise disjoint, nonempty) petals of `\mathcal F_u''`. So `\mathcal
    F'` is a sunflower with core `Y=Y'\cup\{u\}\ne\varnothing`: case (b).

  Either sub-case gives case (b) for `\mathcal F`. `\blacksquare`

*(No finiteness of the ambient universe of primes is used anywhere in this
proof — only that each set has bounded finite size, so `U` and each
`\mathcal F_u`-pigeonhole step involve only finite index sets, regardless
of how large the universe is.)*

#### 4b. Applying the dichotomy to `\mathcal Q_S`

`\mathcal Q_S` is infinite, pairwise distinct, size `\le M`. Apply the
Δ-system dichotomy: get an infinite sub-family `\mathcal Q_S'\subseteq
\mathcal Q_S` that is pairwise disjoint (case a) or a sunflower with
nonempty core `Y` (case b).

**Case (a) — pairwise disjoint.** Since `S` is blocked by `j_3` (Case (ii)
top-level hypothesis) and no `C\in\mathcal V_S` equals `S` (Lemma ERD-C:
`S` is never realized), every `Q\in\mathcal Q_S'` corresponds to a
realized `C=S\cup Q\in\mathcal V_S` with `Q\ne\varnothing`, hence `C=P_i
\supsetneq S` for the (actual) realizing index `i\in I_S`. So `i` is an
"escape" from `\kappa:=S` (`P_i\supsetneq\kappa=S`) in the sense of the
Escape-Confinement Lemma. Applying it (with `\kappa=S=S\cup\varnothing`,
witness `j_3`): `P_i\cap\mathrm{comp}(a_{j_3})\ne\varnothing`. Since
`\mathrm{comp}(a_{j_3})\cap P_1=\varnothing` and `P_i=S\cup Q`, the
intersection cannot come from `S\subseteq P_1`, so `Q\cap
\mathrm{comp}(a_{j_3})\ne\varnothing`. This holds for every `Q\in\mathcal
Q_S'`.

Now: `\mathcal Q_S'` is pairwise disjoint, and each member meets the
**fixed finite** set `\mathrm{comp}(a_{j_3})`. Choose, for each `Q\in
\mathcal Q_S'`, one element `w_Q\in Q\cap\mathrm{comp}(a_{j_3})`. If `Q\ne
Q'` in `\mathcal Q_S'`, then `Q\cap Q'=\varnothing` (pairwise disjoint), so
`w_Q\ne w_{Q'}` (else this common element would lie in `Q\cap Q'`). Hence
`Q\mapsto w_Q` is an **injection** `\mathcal Q_S'\hookrightarrow
\mathrm{comp}(a_{j_3})`, giving `|\mathcal Q_S'|\le|\mathrm{comp}(a_{j_3})|`
— finite. This **contradicts** `\mathcal Q_S'` infinite.

**Case (b) — sunflower with nonempty core `Y`.** Let `L` index the
infinite sub-family, `\mathcal Q_S'=\{Q_l\}_{l\in L}`, `Y\subsetneq Q_l`
for all `l`, petals `Q_l\setminus Y` pairwise disjoint and nonempty.
(`Y\ne\varnothing` by the Δ-system dichotomy's case (b) definition; the
case `Y=\varnothing` is exactly case (a) applied to `\mathcal Q_S'`
directly, already excluded above, so this branch genuinely has `Y\ne
\varnothing`.)

Let `\kappa':=S\cup Y`, a nonempty finite set of primes (`S\ne\varnothing`).
Apply Lemma ERD-C to `C:=\kappa'`.

*Sub-case (b-i): `\kappa'` is realized*, at some index `k` (`P_k=\kappa'`).
For each `l\in L`: `S\cup Q_l=P_{i_l}` for the realizing index `i_l\in
I_S` of `Q_l` (an actual index, since `S\cup Q_l\in\mathcal V_S\subseteq
\{P_i:i\ge1\}`), and `S\cup Q_l\supsetneq\kappa'=S\cup Y` strictly (since
`Q_l\supsetneq Y`). So `P_k=\kappa'\subsetneq S\cup Q_l`; the No-Resurrection
Lemma (with this `k`) gives `S\cup Q_l\notin\mathcal M_m` for every `m\ge
k`. Since `S\cup Q_l\in\mathcal V_S\subseteq\mathcal V`, it lies in
`\mathcal M_n` for **some** `n` (definition of `\mathcal V`); combined with
the exclusion for `n\ge k`, this forces `n<k`, i.e. `S\cup Q_l\in\mathcal
M_n` for some `n\in\{1,\dots,k-1\}`. Hence

`\{S\cup Q_l:l\in L\}\subseteq\bigcup_{n=1}^{k-1}\mathcal M_n`,

a **fixed** finite set (independent of `l`, finite since each `\mathcal
M_n` is finite and there are only `k-1` of them). But `\{S\cup Q_l:l\in
L\}` consists of pairwise **distinct** elements (the `Q_l` are pairwise
distinct, being distinct members of the set `\mathcal Q_S'`), and `L` is
infinite — infinitely many distinct elements cannot fit in a fixed finite
set. **Contradiction.**

*Sub-case (b-ii): `\kappa'` is blocked*, by some witness `j_3'`
(`\mathrm{rad}(a_{j_3'})\cap\kappa'=\varnothing`). In particular
`\mathrm{rad}(a_{j_3'})\cap Y=\varnothing` (since `Y\subseteq\kappa'`), so
`\mathrm{comp}(a_{j_3'})\cap Y\subseteq\mathrm{rad}(a_{j_3'})\cap Y=
\varnothing`, i.e. **`Y` and `\mathrm{comp}(a_{j_3'})` are disjoint.**

For each `l\in L`, the realizing index `i_l\in I_S` of `S\cup Q_l` has
`P_{i_l}=S\cup Q_l\supsetneq S\cup Y=\kappa'` (shown above), so `i_l` is an
escape from `\kappa'` in the Escape-Confinement Lemma's sense. Applying it
(with `\kappa=\kappa'`, `Q=Y`, witness `j_3'`):
`P_{i_l}\cap\mathrm{comp}(a_{j_3'})\ne\varnothing`, i.e. `(S\cup
Q_l)\cap\mathrm{comp}(a_{j_3'})\ne\varnothing`. Since `S\subseteq P_1` is
disjoint from `\mathrm{comp}(a_{j_3'})` (which is disjoint from `P_1` by
definition), this intersection comes from `Q_l`:
`Q_l\cap\mathrm{comp}(a_{j_3'})\ne\varnothing`. Moreover, since `Y\cap
\mathrm{comp}(a_{j_3'})=\varnothing` (shown above), any element of
`Q_l\cap\mathrm{comp}(a_{j_3'})` lies outside `Y`, hence in the **petal**:

`(Q_l\setminus Y)\cap\mathrm{comp}(a_{j_3'})\ne\varnothing` for every
`l\in L`.

Now exactly the same pigeonhole/injection argument as Case (a) applies to
the **petals** `\{Q_l\setminus Y\}_{l\in L}` (pairwise disjoint, by the
sunflower structure) and the fixed finite set `\mathrm{comp}(a_{j_3'})`:
choosing a witness element in each petal's intersection with
`\mathrm{comp}(a_{j_3'})` gives an injection `L\hookrightarrow
\mathrm{comp}(a_{j_3'})`, so `|L|\le|\mathrm{comp}(a_{j_3'})|` — finite.
**Contradicts** `L` infinite.

Both sub-cases of Case (b) are contradictions; combined with Case (a),
**every** branch of the Δ-system dichotomy leads to a contradiction. Hence
the assumption "`\mathcal Q_S` infinite" is false: `\mathcal Q_S` (hence
`\mathcal V_S`, hence `\Lambda_S`) is finite. `\blacksquare` (Case (ii))

Combining Cases (i) and (ii) (Lemma ERD-C's exhaustive dichotomy): in
**both** cases, `\mathcal V_S` (hence `\Lambda_S`) is finite, given
`(UB_S)`. This proves the Main Theorem.

### 4c. Assembling the whole problem

**Theorem (this approach's main result).** Suppose `(UB_S)` holds for
every proper nonempty core `S\subsetneq P_1` (equivalently: `\sup\{\omega
(a_n):n\notin I_{P_1}\}<\infty`, a weaker requirement than a single global
bound `\omega(a_n)=O(1)` for *all* `n`, since indices with imprint exactly
`P_1` — the top core — impose no constraint by Lemma TC). Then
`a_{n+T}=a_n+L` for every `n\ge1`, for explicit `T,L` given by Theorem 5.1.

*(Justification of the parenthetical equivalence, since there are only
finitely many proper cores once `a_1` is fixed — `\le2^k-2` of them, `k=
|P_1|` — so a max over them is well-defined.* For `n\notin I_{P_1}`, `n\in
I_S` for exactly one proper core `S:=P_n\cap P_1` (Theorem CD), and
`\omega(a_n)=|P_n|=|S|+|P_n\setminus S|\le(k-1)+\sup_{i\in I_S}|P_i
\setminus S|`, so "`(UB_S)` for every proper `S`" gives `\sup_{n\notin
I_{P_1}}\omega(a_n)\le(k-1)+\max_S\sup_{i\in I_S}|P_i\setminus S|<\infty`
(a max of finitely many finite quantities). Conversely if `\sup_{n\notin
I_{P_1}}\omega(a_n)=:M'<\infty`, then for any proper `S` and `i\in I_S`,
`|P_i\setminus S|=\omega(a_i)-|S|\le M'`, giving `(UB_S)` with bound `\le
M'`. Both directions hold, so the two hypotheses are indeed equivalent.)*

**Proof.** By §4's Main Theorem, `\Lambda_S` is finite for every proper
core `S`. By the Λ_S-Reduction Lemma, `\mathcal V_S` is finite for every
proper core `S`. Together with Lemma TC (`\mathcal V_{P_1}=\{P_1\}`,
unconditional), Theorem CD gives `\mathcal V=\bigsqcup_{\varnothing\ne
S\subseteq P_1}\mathcal V_S` finite (finite union of finite sets). By
Theorem V, (MRS) holds. By Lemma MS, FCBC holds (with the explicit
covering set `H:=\bigcup_{S\in\mathcal M_{N_0}}S` from Lemma MS's
construction). By Theorem 5.1, `a_{n+T}=a_n+L` for every `n\ge1`.
`\blacksquare`

**Note on Case I.** If a single prime divides every `a_n` (Case I), the
problem is already fully closed unconditionally by Theorem CI
(`lemmas/theorem-CI-case-I-explicit-stabilization.md`) — irrelevant to,
and not assumed by, anything above; the above theorem's hypothesis and
conclusion are only exercised in Case II (where proper cores can be
nontrivial), consistent with every other approach in this workspace.

### 5. Attempt on `(UB_S)` / `ω(a_n)=O(1)` itself — honest report, not closed
(round 8; **superseded by §6 below, round 9** — `(UB_S)` is now fully
settled, in the FALSE direction: see §6.4's Theorem. Kept verbatim as
historical record per this workspace's "append, don't delete" convention;
Attempt 1's finding — that the pigeonhole/Δ-system machinery bounds
*count*, not *size* — remains correct and is exactly why round 9 needed a
genuinely different (analytic/density) tool, which §6 supplies.)

This is the sole remaining open hypothesis for the whole problem, via this
approach (as of round 8). Two attempts were made that round, neither closed
it; both are reported precisely so future rounds do not repeat them.

**Attempt 1 (the outline's suggested lever): combine the pigeonhole
Corollary of §4b Case (a) with a "distinct bundle shapes" count.** The
hope was that since every realized companion bundle `Q` (for `i\in I_S`)
must intersect the fixed finite set `\mathrm{comp}(a_{j_3})` (Case (a)'s
Corollary, proved unconditionally in §4b — it needs no `(UB_S)`), this
might force `|Q|` itself to be bounded. **This does not work, and the
precise reason is worth recording**: the Corollary only bounds how many
*pairwise-disjoint* bundles can exist (`\le|\mathrm{comp}(a_{j_3})|`); it
places **no constraint whatsoever** on the size of any *single* bundle `Q`
— a bundle could contain one element of `\mathrm{comp}(a_{j_3})` together
with arbitrarily many other primes disjoint from `\mathrm{comp}(a_{j_3})`,
and the Corollary would not notice. Concretely: nothing in §4's proof rules
out a hypothetical sequence of bundles `Q_1,Q_2,\dots` all sharing one
fixed element `p\in\mathrm{comp}(a_{j_3})` (so none of the pairwise-disjoint
pigeonhole arguments apply to this family — it's a "sunflower" with core
`\{p\}` in the Δ-system sense, not a disjoint family) while `|Q_n|
\to\infty`. This is exactly the sunflower Case (b) scenario, and §4's
argument handles it via `\kappa'=S\cup\{p\}`'s own realized-or-blocked
dichotomy — but that argument bounds the **number of such bundles** (given
they are already known to have bounded size `\le M`), not their **size**.
So the mechanism that closes `(UB_S)\Rightarrow\Lambda_S` finite is exactly
inapplicable to closing `(UB_S)` itself: it is a genuinely different
question (bounding cardinality of a family of bounded-size sets, vs.
bounding the size of the sets themselves), and no amount of the
pigeonhole/sunflower machinery developed here converts one into the other.

**Attempt 2: analytic size bound, to calibrate what "for free" gives.**
By Lemma 1 (`lemmas/lemma-1-uniform-gap-bound.md`, already certified),
`a_n\le a_1+(n-1)L` for the eventual period `L` — but this presupposes the
periodicity being proved, circular for bounding `\omega` a priori during
the argument. Ignoring that and using only that `a_n` is *some* positive
integer that is `\Theta(n)` in the best case: the classical bound on the
number of distinct prime factors of an integer `x` is `\omega(x)=O(\log
x/\log\log x)` (attained by primorials), which for `x=a_n=\Theta(n)` gives
only `\omega(a_n)=O(\log n/\log\log n)` — **not** `O(1)`. This matches
round 3's own finding ("the natural argument only visibly gives
`O(\log\log n)`," in the same spirit) and confirms, from a different
angle, that **no purely size-based argument can give `O(1)`**: if
`\omega(a_n)=O(1)` is true, it must follow from the specific recursive,
greedy structure of the sequence (which primes are compatible with which
earlier terms), not from `a_n`'s magnitude alone. This is a genuine, if
negative, piece of information: it rules out an entire *class* of possible
proof strategies (any argument that only uses `a_n\le\text{polynomial}(n)`
plus generic divisor-count bounds) rather than just reporting "we tried
and failed."

**Numerical support (not a proof step, consistent with round 3's
finding).** Re-ran a fresh independent simulation (own greedy generator,
`sympy.primefactors`) on three mandated hard cases:

```
a_1=247:      max ω(a_n) = 6 (at n=1039), through N=3000
a_1=2747:     max ω(a_n) = 6 (at n=1646), through N=3000
a_1=21528751: max ω(a_n) = 7 (at n=872),  through N=1200
```

`ω(a_n)` stays in the single digits throughout every tested range, fully
consistent with `(UB_S)`/`ω(a_n)=O(1)` — but this is evidence, not a proof,
per this workspace's standing rule that a numeric check is not a proof
step.

**Where it stalls, precisely.** `(UB_S)`/`ω(a_n)=O(1)` remains exactly as
open as it was after round 3, with one new, precise piece of negative
information from this round: the family of pigeonhole/Δ-system tools that
successfully close `(UB_S)\Rightarrow\Lambda_S` finite are structurally
incapable of closing `(UB_S)` itself, because they bound *how many*
bounded-size objects exist, not *how large* each individual object is —
these are different combinatorial questions, and a correct proof of
`(UB_S)` needs a tool of the second kind, not a variant of the first.

### 6. Full refutation of `(UB_S)` in Case II (Round 9, new, complete)

Throughout this section we work in **Case II** (no prime divides every
`a_n`) — the only regime in which "proper core" is a meaningful notion
(Case I is already fully and separately solved, unconditionally, by
Theorem CI; see the "Note on Case I" at the end of §4c). Case II forces
`k:=|P_1|\ge2`: if `k=1`, `P_1=\{p\}`, and the already-certified **Lemma P**
(`\gcd(a_n,a_1)>1` for every `n`) forces `p\mid a_n` for every `n` (since
`a_1` is composed only of the prime `p`), which is Case I. So `k\ge2` is
automatic in Case II, and there is at least one proper nonempty core
`S\subsetneq P_1` (e.g. `\{p_1\}` for any `p_1\in P_1`).

**Target.** Prove: it is impossible for `(UB_S)` to hold for **every**
proper nonempty core `S\subsetneq P_1` simultaneously.

**Proof strategy (proof by contradiction).** Assume, toward a contradiction,
that `(UB_S)` holds for every proper core `S\subsetneq P_1`. By §4c's
already-proved Theorem (this file, round 8, restated and reused without
re-proof), this hypothesis is equivalent to a single uniform bound
`B:=\sup_{n\notin I_{P_1}}\omega(a_n)<\infty`, and — via the certified chain
`\Lambda_S`-Reduction `\to` Theorem CD/Lemma TC `\to` Theorem V `\to` Lemma
MS `\to` **Theorem 5.1** — it forces **exact periodicity**:

`(\star)\qquad a_{n+T}=a_n+L\quad\text{for every }n\ge1,`

for fixed positive integers `T=|Good|`, `L=\mathrm{lcm}(H)` (`H` the
explicit finite covering set from Lemma MS's construction; both `T,L\ge1`
are guaranteed by Theorem 5.1's own statement). We now derive a numerical
contradiction from `(\star)` combined with the assumed bound `B`.

#### 6.1 The Imprint Periodicity Lemma (new) — the corrected Density
Sub-Lemma, proved as a *consequence* of `(\star)`, not independently

**Lemma (Imprint Periodicity).** Under `(\star)`, there is a **fixed**
positive integer `\tau` (depending only on `T,L,P_1`, not on `N`) such that
`n\in I_{P_1}\iff (n-1\bmod\tau)\in R` for a fixed set `R\subseteq
\{0,\dots,\tau-1\}`. Consequently the density of `I_{P_1}` exists exactly
and equals `|R|/\tau`.

**Proof.** Fix `r\in\{1,\dots,T\}` and set, for `m\ge0`, `n:=r+mT`. By
induction on `m` using `(\star)`: `a_{r+0\cdot T}=a_r` (base case), and if
`a_{r+mT}=a_r+mL` then `a_{r+(m+1)T}=a_{(r+mT)+T}=a_{r+mT}+L=a_r+(m+1)L`
(using `(\star)` with `n:=r+mT\ge1`). So

`a_{r+mT}=a_r+mL\qquad\text{for every }r\in\{1,\dots,T\},\ m\ge0.\quad(\dagger)`

Fix a prime `p`. By `(\dagger)`, `p\mid a_{r+mT}\iff p\mid a_r+mL\iff
mL\equiv-a_r\pmod p`.

- If `p\mid L`: the congruence `mL\equiv-a_r\pmod p` reads `0\equiv-a_r
  \pmod p`, independent of `m` — so `p\mid a_{r+mT}` holds for *all* `m` or
  for *no* `m` (determined by `r` alone). Hence "`p\mid a_n`" has period `T`
  in `n` (constant along each residue class mod `T`).
- If `p\nmid L`: since `p` is prime, `\gcd(L,p)=1`, so `L` is invertible mod
  `p`; as `m` ranges over `\{0,1,\dots,p-1\}`, `mL\bmod p` takes each of the
  `p` residues exactly once, so there is exactly one residue `m_0\pmod p`
  with `mL\equiv-a_r\pmod p`. Hence "`p\mid a_{r+mT}`" holds iff `m\equiv
  m_0\pmod p`, i.e. "`p\mid a_n`" has period `pT` in `n`.

Either way, "`p\mid a_n`" is an exactly periodic property of `n\ge1`, with
period `\tau_p:=T` (if `p\mid L`) or `\tau_p:=pT` (if `p\nmid L`) — a fixed
positive integer depending only on `p,T,L`. Let `\tau:=\mathrm{lcm}
(\tau_p:p\in P_1)`, a fixed positive integer (finite `\mathrm{lcm}` of the
`k=|P_1|` values `\tau_p`). Each "`p\mid a_n`" (`p\in P_1`) has period
dividing `\tau`, hence so does their conjunction "`P_1\subseteq
\mathrm{rad}(a_n)`", i.e. `n\in I_{P_1}`. This gives the stated periodic
characterization, with `R:=\{(r-1)\bmod\tau : r\ge1,\ r\in I_{P_1}\}`
(well-defined since membership only depends on `r\bmod\tau`). The density
of a `\tau`-periodic subset of `\mathbb N` equals `|R|/\tau` exactly
(standard: `|I_{P_1}\cap[1,N]|=|R|\lfloor N/\tau\rfloor+O(\tau)`, so
`|I_{P_1}\cap[1,N]|/N\to|R|/\tau`). `\blacksquare`

**Corollary (corrected Density Sub-Lemma).** `R\ne\{0,\dots,\tau-1\}`,
hence `|R|\le\tau-1`, and there is a fixed `c:=1/(2\tau)>0` with
`|I_{P_1}\cap[1,N]|\le(1-c)N` for all `N\ge2\tau^2`.

**Proof.** Suppose `R=\{0,\dots,\tau-1\}` (every residue). Then every
`n\ge1` has `n\in I_{P_1}`, i.e. `P_1\subseteq\mathrm{rad}(a_n)` for
**every** `n\ge1` — in particular, fixing any `p_1\in P_1` (nonempty, `k
\ge2\ge1`), `p_1\mid a_n` for every `n\ge1`. This makes `p_1` a prime
dividing every term, contradicting the standing Case II hypothesis. Hence
`R\subsetneq\{0,\dots,\tau-1\}`, so `|R|\le\tau-1`.

For the quantitative bound: since `I_{P_1}` is `\tau`-periodic with exactly
`|R|\le\tau-1` populated residues per period, in any block of `\tau`
consecutive integers `I_{P_1}` contains at most `\tau-1` of them, so over
`[1,N]` (at most `\lceil N/\tau\rceil` blocks):
`|I_{P_1}\cap[1,N]|\le(\tau-1)\lceil N/\tau\rceil\le(\tau-1)(N/\tau+1)=
\left(1-\frac1\tau\right)N+(\tau-1)`. Hence `|I_{P_1}^c\cap[1,N]|=N-
|I_{P_1}\cap[1,N]|\ge N/\tau-(\tau-1)\ge N/\tau-\tau`. For `N\ge2\tau^2`,
`N/\tau-\tau\ge N/\tau-N/(2\tau)=N/(2\tau)`, i.e.
`|I_{P_1}^c\cap[1,N]|\ge cN` with `c:=1/(2\tau)`, equivalently
`|I_{P_1}\cap[1,N]|\le(1-c)N`. `\blacksquare`

*(This is exactly the outline-reviewer's corrected weaker form, §1d of
`/tmp/round-9/outline-reviewer.md`, now proved in full — not cited from
numerics. Note the argument is entirely conditional on the standing
assumption `(\star)`, which is itself conditional on the Step-1 hypothesis
`(UB_S)` — this is legitimate and in fact the key simplification of this
round: the whole Density Sub-Lemma is proved *inside* the proof-by-
contradiction, using the contradiction hypothesis's own certified
consequence, rather than unconditionally.)*

#### 6.2 Euler's classical divergence of `\Sigma_p1/p` (proved from scratch)

**Lemma (Euler, 1737).** `S(X):=\sum_{p\le X}1/p\to\infty` as `X\to\infty`
(the sum over primes `p\le X`).

**Proof.** `S(X)` is non-decreasing in `X` (each larger `X` only adds
non-negative terms). Suppose, toward a contradiction, `S(X)` is bounded
above by some constant `C` for all `X`; then the increasing sequence of
partial sums `(S(X))` converges, so its tail vanishes: for `\delta:=1/4`
there is `r\ge1` such that `\sum_{i>r}1/p_i<1/4`, where `p_1<p_2<\cdots` is
the list of all primes. Let `Q_r:=\{p_1,\dots,p_r\}`.

Fix any `N\ge1`. Every integer `n\in[1,N]` falls into exactly one of:

(a) `n` has a prime factor `>p_r`: the count of such `n` is at most
`\sum_{i>r}\lfloor N/p_i\rfloor\le\sum_{i>r}N/p_i<N/4` (by choice of `r`);

(b) `n` has **no** prime factor `>p_r`, i.e. `n=p_1^{e_1}\cdots p_r^{e_r}`
for some integers `e_1,\dots,e_r\ge0` (this includes `n=1`, all `e_j=0`).
For `n\le N`, each `e_j` satisfies `p_j^{e_j}\le N`, so `e_j\le\log_2N`;
hence the count of such `n` is at most `(\lfloor\log_2N\rfloor+1)^r`, a
fixed-degree (`r`, fixed once and for all) polynomial in `\log N`.

Since a fixed-degree polynomial in `\log N` is `o(N)` as `N\to\infty`
(standard: for any fixed `r`, `(\log_2N)^r/N\to0`, e.g. because
`(\log_2N)^r=o(N^{1/2})` eventually and `N^{1/2}=o(N)`), there is `N_0`
(depending only on `r`, hence fixed) such that for `N>N_0`,
`(\lfloor\log_2N\rfloor+1)^r<N/4`.

For any `N>N_0`, the total count from (a)+(b) is `<N/4+N/4=N/2`. But (a)
and (b) are mutually exclusive and exhaustive over `[1,N]`, so this total
must equal exactly `N`. This gives `N<N/2`, false for every `N\ge1` —
contradiction. Hence `S(X)` is unbounded, i.e. `S(X)\to\infty`.
`\blacksquare`

#### 6.3 Landau Count Lemma (proved from scratch, via Turán's 1934
elementary second-moment argument)

**Lemma (Landau Count Lemma).** For every fixed integer `k\ge0`,
`A_k(X):=|\{m\in[1,X]:\omega(m)\le k\}|=o(X)` as `X\to\infty` (`\omega(m)`
= number of distinct prime factors of `m`).

**Proof.** Write `S(X):=\sum_{p\le X}1/p` as in §6.2. We first establish two
elementary counting identities/bounds, using only `\lfloor y\rfloor\le y`,
`\lfloor y\rfloor\ge y-1`, and the trivial bound `\pi(X)\le X` (`\pi(X)`
:= number of primes `\le X`) — no Mertens theorem needed.

*Mean.* `\sum_{m\le X}\omega(m)=\sum_{m\le X}\sum_{p\mid m}1=\sum_{p\le
X}\lfloor X/p\rfloor` (swap order of summation: for fixed prime `p\le X`,
it is counted once for each multiple of `p` up to `X`). Hence:
`XS(X)-X\le XS(X)-\pi(X)\le\sum_{m\le X}\omega(m)\le XS(X).\quad(1)`

*Second moment.* `\omega(m)^2=\left(\sum_{p\mid m}1\right)^2=
\sum_{p,q\text{ primes},\,p\mid m,\,q\mid m}1` (sum over **ordered** pairs,
including `p=q`). So `\sum_{m\le X}\omega(m)^2=\sum_{p,q\le X}
|\{m\le X:p\mid m,q\mid m\}|`. For `p=q` this count is `\lfloor X/p\rfloor`;
for `p\ne q` (distinct primes) it is `\lfloor X/(pq)\rfloor` (since `p\mid
m\wedge q\mid m\iff pq\mid m`, `p,q` coprime). So:
`\sum_{m\le X}\omega(m)^2=\sum_{p\le X}\lfloor X/p\rfloor+\sum_{p\ne
q\le X}\lfloor X/(pq)\rfloor\le XS(X)+\sum_{p,q\le X}X/(pq)=XS(X)+XS(X)^2,
\quad(2)`
using `\lfloor y\rfloor\le y` and dropping the `p\ne q` restriction (adds
only further non-negative terms, valid for an upper bound).

*Variance bound.* Using `(1)`,`(2)`:
`\sum_{m\le X}(\omega(m)-S(X))^2=\sum_{m\le X}\omega(m)^2-2S(X)\sum_{m\le
X}\omega(m)+\lfloor X\rfloor S(X)^2`
`\le\left[XS(X)+XS(X)^2\right]-2S(X)\left[XS(X)-X\right]+XS(X)^2`
`=XS(X)+XS(X)^2-2XS(X)^2+2XS(X)+XS(X)^2=3XS(X).\quad(3)`

*Chebyshev-type extraction.* Fix `k\ge0`. Whenever `S(X)>k`: for every `m`
with `\omega(m)\le k`, `S(X)-\omega(m)\ge S(X)-k>0`, so
`(\omega(m)-S(X))^2\ge(S(X)-k)^2`. Since all terms
`(\omega(m)-S(X))^2\ge0`:
`A_k(X)\cdot(S(X)-k)^2\le\sum_{m\in A_k(X)\text{'s underlying set}}
(\omega(m)-S(X))^2\le\sum_{m\le X}(\omega(m)-S(X))^2\le3XS(X)`

(the middle inequality extends the sum from the (index set of the)
`\omega(m)\le k` integers to all `m\le X`, valid since every added term is
`\ge0`). Hence, whenever `S(X)>k`:
`A_k(X)\le\frac{3XS(X)}{(S(X)-k)^2}.\quad(4)`

*Conclusion.* By §6.2, `S(X)\to\infty`. So there is `X_1` with `S(X)>2k`
for `X>X_1`; for such `X`, `S(X)-k>S(X)/2`, so `(S(X)-k)^2>S(X)^2/4`, and
`(4)` gives `A_k(X)\le\dfrac{3XS(X)}{S(X)^2/4}=\dfrac{12X}{S(X)}`, i.e.
`A_k(X)/X\le12/S(X)\to0` as `X\to\infty` (since `S(X)\to\infty`). Hence
`A_k(X)=o(X)`. `\blacksquare`

*(This is Turán's classical 1934 elementary proof of the Hardy–Ramanujan
normal-order theorem's density consequence, adapted here to avoid needing
the precise Mertens rate `S(X)=\log\log X+O(1)` — only the qualitative
divergence `S(X)\to\infty` from §6.2 is used, which simplifies the proof
and keeps every constant absolute, not depending on the unproven rate.)*

#### 6.4 Assembling the contradiction

Recall the standing assumption: `(UB_S)` holds for every proper core
`S\subsetneq P_1`, with uniform consequence `B:=\sup_{n\notin
I_{P_1}}\omega(a_n)<\infty` (§4c). By §6.1's Corollary, there is a fixed
`c=1/(2\tau)>0` with `|I_{P_1}^c\cap[1,N]|\ge cN` for all `N\ge2\tau^2`.

By the already-certified **Growth Lemma** (Lemma 1,
`lemmas/lemma-1-uniform-gap-bound.md`, with `D:=\mathrm{rad}(a_1)`, renamed
from `L` there to avoid clashing with `(\star)`'s `L`): `a_n\le
a_1+(n-1)D` for every `n\ge1`. So for `n\le N`, `a_n\le X_N:=a_1+(N-1)D`, a
quantity with `X_N=O(N)` (fixed `a_1,D`).

The set `\{a_n:n\in I_{P_1}^c\cap[1,N]\}` consists of **pairwise distinct**
positive integers (since `(a_n)` is strictly increasing, by the problem's
own definition of `a_{n+1}` as the smallest integer *greater than* `a_n`
with the stated property), each `\le X_N`, and each with `\omega(a_n)\le B`
(definition of `B`, since `n\notin I_{P_1}`). Hence:

`A_B(X_N)\ge|I_{P_1}^c\cap[1,N]|\ge cN\qquad\text{for all }N\ge2\tau^2.`

But by §6.3's Landau Count Lemma (applied with the fixed `k:=B`),
`A_B(X_N)=o(X_N)=o(N)` (since `X_N=O(N)`). Combining:

`cN\le A_B(X_N)=o(N)\qquad\text{as }N\to\infty,`

i.e. `c\le o(1)\to0`. This **contradicts** `c=1/(2\tau)` being a fixed
positive constant (independent of `N`). The contradiction is genuine and
unavoidable.

**Conclusion.** The standing assumption — `(UB_S)` holds for every proper
core `S\subsetneq P_1` — is **false**, for every `a_1` with `|P_1|\ge2` in
Case II. `\blacksquare`

**Theorem (this round's main result, restated).** *In Case II (no prime
divides every term of the sequence, forcing `|P_1|\ge2`): it is impossible
for `\sup\{|\mathrm{rad}(a_i)\setminus S|:i\in I_S\}` to be finite for
every proper nonempty core `S\subsetneq P_1` simultaneously. Equivalently,
`\sup_{n\notin I_{P_1}}\omega(a_n)=\infty` always.*

**Honest scope note (per dispatch instruction 4 and the outline's own Step
6).** This is a complete, unconditional refutation of the round-8 target
`(UB_S)`, closing the question the workspace has carried since round 8 as
"the sole remaining gap." It shows definitively that the entire
`(UB_S)`/`(MRS)`/`\mathcal V_S`-finiteness-via-companion-bundle-size
program (rounds 4–8's central thread) **cannot** be completed as a route to
the whole problem — future rounds should not attempt to prove `(UB_S)`,
`(MRS)`, or `\mathcal V_S`-finiteness (for a proper core) again in any
form, in any approach. It does **not**, however, refute FCBC itself (which
is a strictly weaker statement than `(UB_S)`-sufficiency, per the
already-certified Lemma W1: FCBC only needs a *fixed set of primes* `H` to
intersect every pair, not a *bound on companion-bundle size* — these are
logically independent conditions, as the outline-reviewer's own §0 checked
this round). Nor does it resolve the whole problem: that remains the task
of this round's sibling approaches attacking FCBC directly
(`explicit-window-backbone-construction`,
`intersecting-family-covering-construction`), unaffected by this section.

### 7. Round 10: cross-family companion reduction toward the Stabilization
Conjecture

**Target of this section.** Fix a **doubly-infinite disjoint core pair**
`(S,S')` in the sense of `theorem-SW-stabilization-sufficiency.md`: `S,S'`
nonempty, `S\cap S'=\varnothing`, `S,S'\subseteq P_1`, `I_S,I_{S'}` both
infinite. Recall `\mathrm{comp}(a_i):=\mathrm{rad}(a_i)\setminus P_1`
(Escape-Confinement Lemma's notation, imported) and `S(i):=\mathrm{rad}
(a_i)\cap P_1` (Theorem CD's core map). The **Stabilization Conjecture**
for `(S,S')` asks for a finite `W` with `\mathrm{rad}(a_i)\cap\mathrm{rad}
(a_j)\cap W\ne\varnothing` for every `i\in I_S,j\in I_{S'}`.

#### 7.0 Resolving the mandatory Step-0 gap

The round-10 outline's Step 1 invoked the certified Δ-system Dichotomy
Lemma (§4a above) on `\mathcal Q_S:=\{\mathrm{comp}(a_i):i\in I_S\}`,
which requires *every* member to have size `\le M` for a fixed `M`. The
outline-reviewer correctly found this unaddressed: `theorem-UBS-false-
case-II.md` proves only that **some** proper core has unbounded companion
size, never that the *specific* `S` of a given pair does or does not — so
neither "assume bounded" nor "assume unbounded" is licensed for a general
`(S,S')`, and Step 1 could not proceed as literally written.

**Resolution.** Lemmas XC, NIDF, FT below need **no** size-boundedness
hypothesis on `\mathcal Q_S`/`\mathcal Q_{S'}` at all — they hold whether
the companion sets are uniformly bounded or not. This replaces the
Δ-system Dichotomy Lemma's role in Step 1 outright (at the cost of a
weaker conclusion — a one-sided finite transversal, not a full
sunflower/kernel structure) rather than attempting to verify or refute its
hypothesis for the pair at hand. No appeal to `(UB_S)`, boundedness, or
any prior-round refutation is made anywhere in this section.

#### 7.1 Lemma XC (Cross-Companion Reduction)

**Statement.** For any two indices `i,j` with disjoint cores
`S(i)\cap S(j)=\varnothing`: `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)=
\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)`.

**Proof.** Write `\mathrm{rad}(a_i)=S(i)\sqcup\mathrm{comp}(a_i)` and
`\mathrm{rad}(a_j)=S(j)\sqcup\mathrm{comp}(a_j)` (disjoint unions, since
`\mathrm{comp}(a_i)\cap P_1=\varnothing` by definition and `S(i)\subseteq
P_1`). Then
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)=\bigl(S(i)\cap S(j)\bigr)\cup
\bigl(S(i)\cap\mathrm{comp}(a_j)\bigr)\cup\bigl(\mathrm{comp}(a_i)\cap
S(j)\bigr)\cup\bigl(\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\bigr)`.
The first term is `\varnothing` by hypothesis. The second term is
`\varnothing` since `S(i)\subseteq P_1` and `\mathrm{comp}(a_j)\cap
P_1=\varnothing`. The third term is `\varnothing` symmetrically. Hence the
union collapses to the fourth term. `\blacksquare`

#### 7.2 Lemma NIDF (Nonempty Companions, No Infinite Disjoint Sub-family)

**Statement.** Fix disjoint nonempty cores `S,S'\subseteq P_1` with
`I_S,I_{S'}\ne\varnothing`. Then:

(a) `\mathrm{comp}(a_i)\ne\varnothing` for every `i\in I_S`, and
`\mathrm{comp}(a_j)\ne\varnothing` for every `j\in I_{S'}`.

(b) `\{\mathrm{comp}(a_i):i\in I_S\}` contains no infinite pairwise-disjoint
sub-family: there is no infinite `L\subseteq I_S` with `\{\mathrm{comp}
(a_i)\}_{i\in L}` pairwise disjoint. Symmetrically for `I_{S'}`.

**Proof.** (a) Fix `j_0\in I_{S'}` (exists, `I_{S'}\ne\varnothing`). By the
already-certified Lemma P′, `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_{j_0})\ne
\varnothing` for every `i` (in particular `i\in I_S`); since `S(i)=S`,
`S(j_0)=S'` are disjoint, Lemma XC gives `\mathrm{comp}(a_i)\cap\mathrm{comp}
(a_{j_0})\ne\varnothing`, hence `\mathrm{comp}(a_i)\ne\varnothing`. The
`I_{S'}` case is symmetric, fixing any `i_0\in I_S`.

(b) Suppose, toward a contradiction, `L\subseteq I_S` is infinite with
`\{\mathrm{comp}(a_i)\}_{i\in L}` pairwise disjoint. Fix any `j_0\in
I_{S'}` (exists). By Lemma P′ and Lemma XC (as in (a)), `\mathrm{comp}
(a_{j_0})\cap\mathrm{comp}(a_i)\ne\varnothing` for **every** `i\in L`.
Choose `w_i\in\mathrm{comp}(a_{j_0})\cap\mathrm{comp}(a_i)` for each
`i\in L`. If `i\ne i'` in `L`: `\mathrm{comp}(a_i)\cap\mathrm{comp}
(a_{i'})=\varnothing` (pairwise-disjoint hypothesis), so `w_i\ne w_{i'}`
(else this common value would lie in `\mathrm{comp}(a_i)\cap\mathrm{comp}
(a_{i'})`). Hence `i\mapsto w_i` is an injection `L\hookrightarrow
\mathrm{comp}(a_{j_0})`. Since `\mathrm{comp}(a_{j_0})` is the (always
finite — a single integer's radical) companion set of **one fixed**
index, `|L|\le|\mathrm{comp}(a_{j_0})|<\infty`, contradicting `L` infinite.
The `I_{S'}` case is symmetric. `\blacksquare`

*(No hypothesis on the size of `\mathrm{comp}(a_i)` uniformly over `i\in
I_S` is used anywhere — only that `\mathrm{comp}(a_{j_0})`, a single fixed
set, is finite, which is automatic. This is what makes the Lemma
unconditional and immune to the Step-0 gap.)*

#### 7.3 Lemma FT (Finite One-Sided Transversal)

**Statement.** Under the hypotheses of Lemma NIDF, there exist finitely
many indices `i_1,\dots,i_r\in I_S` (`r\ge1`) with `\mathrm{comp}
(a_{i_1}),\dots,\mathrm{comp}(a_{i_r})` pairwise disjoint, such that
`U_S:=\mathrm{comp}(a_{i_1})\cup\dots\cup\mathrm{comp}(a_{i_r})` (finite)
satisfies `\mathrm{comp}(a_i)\cap U_S\ne\varnothing` for **every** `i\in
I_S`. Symmetrically there is a finite `U_{S'}` with `\mathrm{comp}(a_j)\cap
U_{S'}\ne\varnothing` for every `j\in I_{S'}`.

**Proof.** Greedy construction. `I_S\ne\varnothing`, so pick `i_1\in I_S`
arbitrarily. Having picked `i_1,\dots,i_t\in I_S` with `\mathrm{comp}
(a_{i_1}),\dots,\mathrm{comp}(a_{i_t})` pairwise disjoint, if some `i\in
I_S` has `\mathrm{comp}(a_i)` disjoint from `\mathrm{comp}(a_{i_1})\cup
\dots\cup\mathrm{comp}(a_{i_t})`, set `i_{t+1}:=i` and continue (this
preserves pairwise-disjointness of the whole growing collection: the new
set is disjoint from the union of the old ones, hence from each
individually). If this process continued forever, `\{\mathrm{comp}
(a_{i_t})\}_{t\ge1}` would be an infinite pairwise-disjoint sub-family of
`\{\mathrm{comp}(a_i):i\in I_S\}`, contradicting Lemma NIDF(b). So it
terminates after finitely many steps, at some `r\ge1` (the first pick
`i_1` always succeeds, so `r\ge1`). By termination (maximality — no
further index can be added), **every** `i\in I_S` has `\mathrm{comp}(a_i)`
intersecting `U_S:=\mathrm{comp}(a_{i_1})\cup\dots\cup\mathrm{comp}
(a_{i_r})` — else the process would not have stopped at `r`. `U_S` is a
finite union of `r` individually finite sets (each `\mathrm{comp}
(a_{i_k})` is the radical-complement of one fixed integer, hence finite;
`r` itself is finite, though its value — like the sizes of the individual
`\mathrm{comp}(a_{i_k})` — is not a priori bounded across different pairs
`(S,S')` or different `a_1`), hence `U_S` is finite. The `I_{S'}` case is
symmetric. `\blacksquare`

**Corollary (immediate).** `W:=U_S\cup U_{S'}` is finite and satisfies
`\mathrm{comp}(a_i)\cap W\ne\varnothing` for every `i\in I_S` **and**
`\mathrm{comp}(a_j)\cap W\ne\varnothing` for every `j\in I_{S'}`
(separately, one side at a time).

This fully discharges the outline's Step 0/Step 1 in the sense that a
genuine, unconditional finite structure is now available on each side,
without ever needing to resolve whether `\mathcal Q_S`/`\mathcal Q_{S'}`
are bounded-size — but, as the next sub-section shows honestly, it is
**not yet** the Stabilization Conjecture itself.

#### 7.4 The precisely-located remaining gap: Conjecture (JW)

**Conjecture (JW).** `W:=U_S\cup U_{S'}` (as constructed in Lemma FT)
satisfies the **joint** condition `\mathrm{rad}(a_i)\cap\mathrm{rad}
(a_j)\cap W\ne\varnothing` (equivalently, by Lemma XC, `\mathrm{comp}
(a_i)\cap\mathrm{comp}(a_j)\cap W\ne\varnothing`) for **every** `i\in
I_S,j\in I_{S'}` simultaneously — i.e. `W` solves the Stabilization
Conjecture for `(S,S')`.

**Why the natural proof attempt stalls (precise diagnosis).** Fix `i\in
I_S,j\in I_{S'}`. By Lemma FT, `\mathrm{comp}(a_i)\cap U_S\ne\varnothing`
at some element `u`, and `\mathrm{comp}(a_j)\cap U_{S'}\ne\varnothing` at
some element `u'`. Separately, by Lemma P′ + Lemma XC, `\mathrm{comp}
(a_i)\cap\mathrm{comp}(a_j)\ne\varnothing` at some element `p`. Nothing
forces `p\in\{u,u'\}`, nor `u=u'`: these are three a priori independent
witnesses to three different (though overlapping-in-flavor) intersection
facts, and `W` only contains `u` and `u'`, not necessarily `p`.

A natural refinement attempt: let `i_k\in\{i_1,\dots,i_r\}` be the specific
representative index (from Lemma FT's construction) whose `\mathrm{comp}
(a_{i_k})` meets `\mathrm{comp}(a_i)` at `u` (i.e. `u\in\mathrm{comp}
(a_{i_k})`). Since `i_k\in I_S` is an **actual** index, Lemma P′ + Lemma XC
give `\mathrm{comp}(a_{i_k})\cap\mathrm{comp}(a_j)\ne\varnothing` directly
(for **every** `j\in I_{S'}`, not just those meeting `U_{S'}`) — call a
witness `w\in\mathrm{comp}(a_{i_k})\cap\mathrm{comp}(a_j)`. This is
genuinely useful (it shows `\mathrm{comp}(a_{i_k})`, one of the *finitely
many* representative companion sets, already intersects *every* `j\in
I_{S'}`) but `w` need not equal `u` (`u,w\in\mathrm{comp}(a_{i_k})`, but
`\mathrm{comp}(a_{i_k})` can have more than one element — confirmed by the
computation below, where the representative sets found have size `2`, not
`1` — so `u=w` is not forced). If `\mathrm{comp}(a_{i_k})` were always a
**singleton** for every representative index the greedy process selects,
this argument would close Conjecture (JW) completely (`u=w` automatically,
giving `u=w\in\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap\mathrm{comp}
(a_{i_k})\subseteq\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap U_S\subseteq
\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap W`) — but nothing in Lemma FT's
construction forces the representative sets to be singletons, and the
worked example below shows they are not. **This is the exact, sole
remaining logical gap**: Conjecture (JW) reduces to (but is not
established by) the question of whether the specific shared prime `w`
furnished by Lemma P′ for `(i_k,j)` can always be taken equal to (or
replaced compatibly with) the specific shared prime `u` furnished for
`(i,i_k)` — a genuinely new coincidence/rigidity question about the
sequence's actual arithmetic, not resolvable by the purely combinatorial
tools (Lemma P′, finiteness, pigeonhole) used to prove Lemmas XC/NIDF/FT.
Closing it plausibly requires the deeper, sequence-specific machinery this
file's §1–§4 already built for the single-family case (Lemma ERD-C,
Escape-Confinement, No-Resurrection) — adapting *that* machinery to the
cross-family setting, rather than extending the purely combinatorial
argument of §7.1–7.3, is the recommended direction for a future round; it
was not completed this round for lack of time, and is reported here as the
honest boundary of this round's progress rather than attempted and
possibly gotten wrong under time pressure.

#### 7.5 Numerical evidence for Conjecture (JW) — not a proof step

Two independent, from-scratch computations (own greedy-sequence generator,
implementing the problem's exact rule "`a_{n+1}` = smallest integer `>a_n`
with `\gcd(a_{n+1},a_i)>1` for all `i\le n`"; `sympy.factorint` for exact
factorization):

**Instance 1: `a_1=247`, `(S,S')=(\{13\},\{19\})`** (the pair this round's
whole field targets, per the H100-stabilization explorer). Generated to
`n=20000`: `|I_{\{13\}}|=10764`, `|I_{\{19\}}|=6910`. Lemma FT's greedy
process gives representative sets `\{2,5\},\{3,7\}` on the `\{13\}`-side
(`U_S=\{2,3,5,7\}`, `r=2`) and `\{2,7\},\{3,5\}` on the `\{19\}`-side
(`U_{S'}=\{2,3,5,7\}`, `r=2` — coincidentally identical to `U_S` as a set
here). `W=U_S\cup U_{S'}=\{2,3,5,7\}`. Checked `\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)\cap W\ne\varnothing` for **all** `10764\times6910=
74{,}379{,}240` cross pairs: **zero violations**. (This matches, and gives
an independent from-scratch derivation of, the `W=\{2,3,5,7\}` set already
found by three sibling approaches/rounds via unrelated constructions —
`H100-stabilization`, `intersecting-family-covering-construction`'s Theorem
SW verification, `explicit-window-backbone-construction`'s window search —
strong convergent evidence, though still not a proof, that this specific
`W` is correct for this specific pair.)

**Instance 2: `a_1=21528751`, `(S,S')=(\{103\},\{197\})`** (a disjoint
core pair of the workspace's hardest known case, chosen for `|I_S|,
|I_{S'}|` both being non-trivial within a feasible computation range).
Generated to `n=6000`: `|I_{\{103\}}|=5857`, `|I_{\{197\}}|=102`, max
companion-bundle size `6` on both sides at this range. Lemma FT's greedy
process gives `U_S=\{2,3,7,13,19,41,193,2297,2549\}` (`r=3` representative
sets) and `U_{S'}=\{2,3,7,1301\}` (`r=1`). `W=U_S\cup U_{S'}` (12 primes).
Checked all `5857\times102=597{,}414` cross pairs: **zero violations**
(also independently confirmed the much smaller candidate `\{2,3,5,7,11,
13\}`, already known from prior rounds' universal-window search, has zero
violations on this exact pair too).

**Honest scope of this evidence.** Two structurally very different
instances (`a_1=247`: small `P_1=\{13,19\}`, moderate index density;
`a_1=21528751`: the workspace's hardest recorded case, `P_1=\{103,197,
1061\}`, needing the previously-discovered bridge prime `97` for a
*different* core pair), zero violations across `\sim75` million total
cross pairs, is strong support — but per this workspace's standing rule, a
numerical check is evidence, not a proof step, and Conjecture (JW) is
reported as **open**, not established.

### 8. Round 11: sharpening Conjecture (JW) via Lemma CB and single-witness
coverage — genuine progress, gap still open

Throughout, fix a doubly-infinite disjoint core pair `(S,S')` as in §7
(`S,S'` nonempty, disjoint, `\subseteq P_1`, `I_S,I_{S'}` both infinite,
hence in particular both nonempty — the only hypothesis actually used
below).

#### 8.1 Why "everywhere-nonempty trace" needs no separate argument

The round-11 outline's Step 1/Step 3 asked, for a fixed candidate `Π`,
for two properties: (a) `\mathrm{trace}(i):=\mathrm{comp}(a_i)\cap Π\ne
\varnothing` for every `i\in I_S\cup I_{S'}$, and (b) no realized `S`-side
trace is disjoint from any realized `S'`-side trace ("clash-freedom").
**Property (a) is not independent of (b): it follows from (b) alone,
given `I_S,I_{S'}` both nonempty.** Indeed, suppose some `i_0\in I_S` has
`\mathrm{trace}(i_0)=\varnothing`. Fix any `j_0\in I_{S'}` (exists,
`I_{S'}\ne\varnothing`); `\mathrm{trace}(i_0)=\varnothing` is (trivially)
disjoint from `\mathrm{trace}(j_0)`, so (b) fails at the pair
`(i_0,j_0)`. Hence (b) `\Rightarrow` (a), so it suffices to establish
clash-freedom (b) alone; this round's work below targets (b) directly,
avoiding redundant work on (a).

#### 8.2 Lemma CB (Core Blocking) — new, fully proved

**Statement.** Let `S,S'` be disjoint nonempty cores with `I_S,I_{S'}`
both nonempty. Then, in the sense of Lemma ERD-C (§1 above): **`S` is
blocked (not realized), and `S'` is blocked (not realized).**

**Proof.** Suppose toward a contradiction that `S` is realized: some
index `n_0\ge1` has `P_{n_0}=S$ exactly. Since `S\subseteq P_1`,
`P_{n_0}\cap P_1=S\cap P_1=S`, so `n_0\in I_S` (by definition of `I_S`,
§0). By Lemma NIDF(a) (§7.2 above — whose hypotheses are exactly
"`S,S'` disjoint nonempty cores with `I_S,I_{S'}\ne\varnothing`",
satisfied here), `\mathrm{comp}(a_i)\ne\varnothing$ for **every**
`i\in I_S`, in particular for `i=n_0`: `\mathrm{comp}(a_{n_0})\ne
\varnothing`. But `\mathrm{comp}(a_{n_0})=P_{n_0}\setminus P_1=S
\setminus P_1=\varnothing` (since `S\subseteq P_1`, using `P_{n_0}=S`).
This gives `\varnothing\ne\varnothing`, a contradiction. Hence `S` is not
realized; by Lemma ERD-C's exhaustive dichotomy (applied to `C:=S`;
Lemma ERD-C needs no hypothesis on `S` beyond being a nonempty finite set
of primes, satisfied), `S` is blocked. The `S'$ case is symmetric
(exchange the roles of `S,S'$ throughout — Lemma NIDF(a)'s hypotheses and
conclusion are stated symmetrically in `S,S'$, so the identical argument
applies verbatim with `S,S'$ interchanged). `\blacksquare`

**Remark (an honest record of a false shortcut this round ruled out
before writing it up as a claimed result — kept so no future round
re-attempts it).** Before proving Lemma CB, this round's build attempted
a shortcut: "if `S` is ERD-C-*realized* at some `n_0`, then Lemma SR
(§2 above) gives `\mathcal V_S` finite **unconditionally** (no `(UB_S)`
needed), so `Λ_S:=\bigcup\mathcal Q_S` is a fixed finite set, and one
might hope `\mathrm{comp}(a_i)\subseteq Λ_S` for *every* `i\in I_S`,
making `Π:=Λ_S` an immediate one-line solution to Stabilization whenever
either side is realized." **This does not work, for two independent
reasons, and moreover the premise itself never occurs.** First,
Lemma SR only bounds `\mathcal V_S$ — the set of radical values with
imprint `S` that are *ever `n`-minimal* (i.e. that lie in `\mathcal V=
\bigcup_n\mathcal M_n`) — not the set of *all actually-realized* radical
values with imprint `S`; an index `i\in I_S` whose radical `P_i` is
never `n`-minimal at any `n$ (e.g. because some earlier index's radical
is a proper subset of `P_i$ forever after) need not have `\mathrm{comp}
(a_i)\subseteq Λ_S` at all, so the inclusion "`\mathrm{comp}(a_i)
\subseteq Λ_S$ for every `i\in I_S`" is not justified by Lemma SR alone.
Second, and more fundamentally, **Lemma CB (just proved) shows the
premise "`S` is realized" can *never* hold whenever `I_{S'}\ne
\varnothing`** — exactly the situation of every doubly-infinite pair — so
this shortcut's hypothesis is vacuous in the very setting Conjecture (JW)
is about. This is recorded explicitly so that no future round re-derives
or re-attempts this specific line of reasoning under the impression it
might close (JW) unconditionally in some case split.

#### 8.3 A sharper one-sided covering pair via Escape-Confinement

**Corollary (single-witness one-sided coverage).** For any doubly-infinite
disjoint core pair `(S,S')`, there exist (fixed) indices `j_3,j_3'\ge1`
with `\mathrm{rad}(a_{j_3})\cap S=\varnothing`, `\mathrm{rad}(a_{j_3'})
\cap S'=\varnothing` (Lemma CB's blocking witnesses for `S,S'`
respectively), such that

`\mathrm{comp}(a_i)\cap\mathrm{comp}(a_{j_3})\ne\varnothing\text{ for
every }i\in I_S,\qquad\mathrm{comp}(a_j)\cap\mathrm{comp}(a_{j_3'})\ne
\varnothing\text{ for every }j\in I_{S'}.`

**Proof.** By Lemma CB, `S` is blocked: fix a witness `j_3` with
`\mathrm{rad}(a_{j_3})\cap S=\varnothing$ (Lemma ERD-C's case (ii)).
Since `S` is (by the same dichotomy) *never realized*, every `i\in I_S`
has `P_i\cap P_1=S$ and `P_i\ne S` (else `i` would realize `S`,
contradicting Lemma CB), so `P_i\supsetneq S` strictly: `i` is an
"escape" from `\kappa:=S` in the sense of the Escape-Confinement Lemma
(§0, cited). Applying it (with `\kappa=S=S\cup\varnothing`, witness
`j_3`): `P_i\cap\mathrm{comp}(a_{j_3})\ne\varnothing`. Since
`\mathrm{comp}(a_{j_3})\cap P_1=\varnothing` (definition of `\mathrm{comp}`)
and `P_i=S\cup\mathrm{comp}(a_i)$ with `S\subseteq P_1`, this intersection
cannot come from `S`, so `\mathrm{comp}(a_i)\cap\mathrm{comp}(a_{j_3})\ne
\varnothing`. This holds for every `i\in I_S`. The `S'` case is symmetric.
`\blacksquare`

This is a genuine improvement on Lemma FT (§7.3) for the specific purpose
of building a candidate `Π`: instead of a union of `r` (resp. `s`)
greedily-chosen representative companion sets, a **single** fixed
companion set per side already suffices, unconditionally, for *every*
doubly-infinite pair (no case split on whether the greedy process
terminates quickly is needed — Lemma CB guarantees the "blocked" branch
of Lemma ERD-C always applies here). Define the sharpened candidate

`Π:=\mathrm{comp}(a_{j_3})\cup\mathrm{comp}(a_{j_3'})`

— by construction, finite (union of two single companion sets, each
finite) and, per §8.1, automatically satisfies the "everywhere-nonempty
trace" property once (and only once) clash-freedom is established.

#### 8.4 Cross-Permanent-Inadmissibility attempted on `Π`: the wall persists
— honest report, gap not closed

**Attempted claim.** `Π` (as just constructed) is clash-free: for every
`i\in I_S,j\in I_{S'}`, `\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap Π
\ne\varnothing`.

**What is available.** Fix `i\in I_S,j\in I_{S'}`. Three facts hold, none
new:

1. `\mathrm{comp}(a_i)\cap\mathrm{comp}(a_{j_3})\ni u` for some `u`
   (§8.3, depending on `i`);
2. `\mathrm{comp}(a_j)\cap\mathrm{comp}(a_{j_3'})\ni v` for some `v`
   (§8.3, depending on `j`);
3. `\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\ni p` for some `p`
   (Lemma P′ + Lemma XC, §7.1, depending on the pair `(i,j)`).

**Attempted repair 1 (direct chain through `j_3`).** If the *core* of
`j_3` (i.e. `S(j_3):=\mathrm{rad}(a_{j_3})\cap P_1`) happened to be
disjoint from `S'`, Lemma XC would apply directly to the pair `(j_3,j)`
(unconditionally, via Lemma P′, no case split needed), giving a witness
`w\in\mathrm{comp}(a_{j_3})\cap\mathrm{comp}(a_j)\subseteq Π`. This shows
`\mathrm{comp}(a_j)\cap Π\ne\varnothing$ via `w` — but this is already
known from fact 2 above (`v$), and — critically — **nothing forces
`w\in\mathrm{comp}(a_i)`.** `w` witnesses a relation between `j_3` and
`j`, not between `i` and `j`; there is no established mechanism forcing
`w=u` or `w=p`. This is the *identical* rigidity gap already diagnosed in
§7.4 for the larger candidate `U_S\cup U_{S'}`, now confirmed to persist
verbatim for the smaller, more natural candidate `Π`.

**Attempted repair 2 (a joint bare-value dichotomy).** Considered
applying Lemma ERD-C to `\kappa'':=S\cup S'` (disjoint union, a nonempty
finite set of primes) to try to link the two sides through a single
witness. This does not connect to `I_S$ or `I_{S'}` directly: an index
realizing `\kappa''$ exactly would have `P_1`-imprint `S\cup S'` — a
*third* core, distinct from both `S` and `S'` — so Lemma ERD-C's
dichotomy for `\kappa''` says nothing about escapes from `S` or from `S'`
specifically (the Escape-Confinement Lemma requires the *same* core `S`
on both the blocked value and the escaping index; `\kappa''\ne S$ and
`\kappa''\ne S'`, so it does not apply to either side via this `\kappa''`).
This repair attempt does not yield a usable link and is recorded here so
it is not re-attempted verbatim by a future round without a genuinely new
idea for connecting the two sides' witnesses.

**Also checked and found not to apply: `S(j_3)$ need not be disjoint from
`S'` at all** — `j_3` is *only* known to satisfy `\mathrm{rad}(a_{j_3})
\cap S=\varnothing`; nothing in Lemma CB's proof constrains
`S(j_3)`'s relationship to `S'`. If `S(j_3)\cap S'\ne\varnothing`, Lemma
XC does not apply to `(j_3,j)` at all (its hypothesis is exactly
core-disjointness), and while Lemma P′ (unconditional, no core hypothesis)
still gives `\mathrm{rad}(a_{j_3})\cap\mathrm{rad}(a_j)\ne\varnothing`,
the shared prime this supplies could lie in `S(j_3)\cap S'\subseteq P_1`
— **not** a companion prime at all, hence not usable to place a witness
in `Π` (which is built entirely from companion primes). This is a
genuinely new obstruction identified this round (not present in the
§7.4 diagnosis, which implicitly worked entirely within companion
primes): even the *attempt* to chain through `j_3` can fail to produce a
companion-side witness at all, depending on `j_3`'s core.

**Conclusion of this round's attempt.** Cross-Permanent-Inadmissibility
(the outline's Step 4) is **not** established this round. The gap is the
same rigidity question as §7.4's Conjecture (JW), now confirmed to
persist for the smallest, most natural candidate `Π` produced in this
file's history (`\mathrm{comp}(a_{j_3})\cup\mathrm{comp}(a_{j_3'})`, a
union of exactly two single companion sets, replacing the larger
multi-representative `U_S\cup U_{S'}`), with one additional, precisely
located new obstruction (the possible core-overlap of `j_3` with `S'`)
that a future round must address if it attempts the direct-chain repair
further. Per the round-11 outline's explicit instruction, this is
reported honestly rather than patched around: **no instance found this
round contradicts Conjecture (JW) itself** (no computation was run this
round beyond re-using the already-reported §7.5 numerics, which remain
valid evidence for the *conjecture*, not for this round's specific
attempted proof mechanism), but the proof of Conjecture (JW) — even for
this sharper `Π` — remains open.

**What would close it.** Per the jw-lens explorer's own recommendation
(`/tmp/round-11/math-explorer-jw.md`, "Cross-Permanent-Inadmissibility"
opening), the missing ingredient is a genuine cross-family analogue of
the Permanent-Inadmissibility Lemma: a mechanism showing that once a
specific companion prime `p` is used to witness `\mathrm{comp}(a_i)\cap
\mathrm{comp}(a_j)\ne\varnothing` for one pair realizing a given pair of
"trace types" against `Π`, only **finitely many** distinct primes can
ever serve this role for *the same pair of trace types* — this is a
statement about the sequence's actual greedy/arithmetic structure
(which specific integers get realized, and when), not a fact reachable
from Lemma P′, Lemma XC, Lemma NIDF, Lemma FT, Lemma CB, or the
Escape-Confinement Lemma alone (all of which are purely
existential/pigeonhole in character). Building this mechanism is left
as the precise, sharply-located open target for a future round.

### 9. Round 12: Escape-Prime Finiteness via NIDF Pigeonhole, scoped to
Case B — diagnostic negative result, gap not closed

Throughout, `(S,S')` is a doubly-infinite disjoint core pair with **no
nonempty realized single-side backbone on either side** ("Case B", per
this round's outline-reviewer's confirmed classification,
`/tmp/round-12/outline-reviewer.md`): the two confirmed instances are
`a_1=247, (S,S')=(\{13\},\{19\})` and `a_1=4199, (S,S')=(\{13\},\{17\})`
(with `P_1=\{13,17,19\}` for the second instance — a 3-prime top core, so
`S,S'` are two of the three singleton proper cores). All computations
below use an independent, from-scratch greedy-sequence generator (own
Python, `sympy.factorint` for exact factorization, cross-checked against
this file's own §7.5 numbers for `a_1=247` — exact match on `|I_{13}|,
|I_{19}|` at `N=20000`, `10764/6910`, confirming the generator is correct
before trusting any new claim built on it).

#### 9.1 Setup: the Step 4′ target, restated precisely

Fix a finite `\Pi`. For `i\in I_S` write `\tau(i):=\mathrm{comp}(a_i)\cap
\Pi` ("trace"), similarly `\tau'(j)` for `j\in I_{S'}`. A pair of trace
values `(\tau,\tau')` is a **realized clash** if `\tau\cap\tau'=
\varnothing`, `I_S^\tau:=\{i\in I_S:\tau(i)=\tau\}\ne\varnothing`, and
`I_{S'}^{\tau'}:=\{j\in I_{S'}:\tau'(j)=\tau'\}\ne\varnothing`. By Lemma P′
+ Lemma XC (§7.1, already certified), every `(i,j)\in I_S^\tau\times
I_{S'}^{\tau'}$ has `\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\ne
\varnothing`, and (since `\tau\cap\tau'=\varnothing`) any witness of this
intersection necessarily avoids `\Pi`, i.e. lies in `\bigl(\mathrm{comp}
(a_i)\setminus\Pi\bigr)\cap\bigl(\mathrm{comp}(a_j)\setminus\Pi\bigr)`. The
round-12 outline's Step 4′ target: is the **escape-prime set**

`P(\tau,\tau'):=\bigcup_{i\in I_S^\tau,\,j\in I_{S'}^{\tau'}}
\bigl(\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\setminus\Pi\bigr)`

always **finite**, for every realized clash `(\tau,\tau')`, by an
adaptation of the already-certified Lemma NIDF injection argument applied
directly to this set (rather than to a companion-set family as in §7.2)?
If so, Step 5's repair process (enlarge `\Pi` by `\bigcup_{(\tau,\tau')}
P(\tau,\tau')$, a finite enlargement since there are only finitely many
trace-type pairs by Step 2's `2^{|\Pi|}`-pigeonhole) would terminate by the
already-certified Greedy Augmentation + Termination-Sufficiency Lemma
(`forced-primes-well-ordering`,
`lemmas/lemma-greedy-augmentation-and-termination-sufficiency.md`),
closing Conjecture (JW) for the pair.

**Reduction to the hard case (elementary, recorded for completeness).** If
`I_S^\tau` or `I_{S'}^{\tau'}` is *finite*, `P(\tau,\tau')` is trivially
finite: it is contained in the finite union `\bigcup_{i\in
I_S^\tau}\mathrm{comp}(a_i)$ (a finite union of finite sets, since each
`\mathrm{comp}(a_i)` — the companion set of *one* fixed integer — is
finite, and `I_S^\tau$ itself is finite by hypothesis in this branch). So
the only open case is **both `I_S^\tau` and `I_{S'}^{\tau'}` infinite** —
this is the case attempted below.

#### 9.2 Why the direct pigeonhole argument does not close the hard case
— new diagnostic content, fully rigorous

**Proposition (Row-Restriction Obstruction).** Fix a realized clash
`(\tau,\tau')` with `I_S^\tau,I_{S'}^{\tau'}` both infinite. For **any**
single fixed `j_0\in I_{S'}^{\tau'}`, Lemma P′ + Lemma XC give, for
**every** `i\in I_S^\tau`, a witness prime in `\bigl(\mathrm{comp}(a_i)
\setminus\Pi\bigr)\cap\bigl(\mathrm{comp}(a_{j_0})\setminus\Pi\bigr)
\subseteq\mathrm{comp}(a_{j_0})\setminus\Pi` — a set depending only on the
**fixed** `j_0`, hence finite (bounded by `|\mathrm{comp}(a_{j_0})|`).
Call this bound `R(j_0)\subseteq\mathrm{comp}(a_{j_0})\setminus\Pi`. This
is the exact adaptation of the Lemma NIDF(b) injection technique the
outline's Step 4′ envisioned, and it genuinely works — **for the
sub-collection of escape primes arising from pairs `(i,j_0)` with the
second coordinate fixed at `j_0`.**

**But this does not bound `P(\tau,\tau')=\bigcup_{j\in
I_{S'}^{\tau'}}R(j)`, the union over *all* `j\in I_{S'}^{\tau'}`.** The
obstruction: nothing in the already-certified toolkit (Lemma P′, Lemma XC,
Lemma NIDF, Lemma FT, Lemma CB, the Escape-Confinement Lemma) relates
`\mathrm{comp}(a_j)` to `\mathrm{comp}(a_{j'})` for two *different*
indices `j\ne j'` in `I_{S'}^{\tau'}` — every one of these lemmas is a
**"one side fixed, the other side ranges freely"** existence statement
(Lemma P′: fix one integer, get an intersection with every other; Lemma
NIDF(b)/FT: fix one companion set as a *target*, get that every member of
a family hits it; Escape-Confinement: fix one blocking witness, get that
every escape hits its companion set). None of them is a **"both sides
range together"** boundedness statement, which is exactly what
`\bigcup_{j}R(j)$ staying finite would require. This is a precise,
previously-unstated (in this file) structural reason — not merely an
empirical stall — that Step 4′, as literally proposed, reduces to the
*identical* open requirement already diagnosed in §7.4 (Conjecture (JW)'s
own "`u=w`" rigidity gap) and §8.4 (the CB-sharpened `\Pi`'s wall): a
cross-index linking fact between different `j`'s companion sets (or
different `i`'s), which no combinatorial/pigeonhole tool in this file's
toolkit supplies. Repackaging the target as "escape-prime set" rather than
"covering set `\Pi`" does not change which fact is missing — it is the
*same* fact, only relocated.

**Why Case B specifically blocks the natural repair.** In Case A (sibling
approach `sunflower-inadmissibility-toolkit`), the missing cross-index
link is supplied *for free* whenever a class-wide backbone freezes to a
nonempty, exactly-realized value `C`: every member of the class then
shares the *entire* fixed set `C`, so `R(j)\supseteq C$ for every `j`
automatically making `\bigcap_j R(j)\supseteq C\ne\varnothing` — no
cross-index argument needed, because the intersection is forced structurally.
**Case B pairs are, by their own defining property (§ the round-12 outline
and the outline-reviewer's confirmed classification), precisely those
where this class-wide freeze fails to be nonempty** — so this shortcut is
unavailable by construction, and the Row-Restriction Obstruction above is
not an accidental proof gap but a reflection of the actual scoping
difference between Case A and Case B.

#### 9.3 The Matched-Witness construction — new, fully proved existence
result on both instances

Despite §9.2's negative diagnosis for the general trace-pair mechanism, one
natural, concrete refinement of round 11's §8.3 `\Pi:=\mathrm{comp}
(a_{j_3})\cup\mathrm{comp}(a_{j_3'})$ remained untried: round 11 used
whichever witness `j_3` (resp. `j_3'`) was found **first** in the
generation order, giving *mismatched* companion sets (`\{2,7\}` vs
`\{2,5\}` for `247:(13,19)`, confirmed by direct re-computation this round
— see §9.4). Since the Escape-Confinement Lemma (§0, already certified)
holds for **any** valid blocking witness, not just the first one found, a
natural refinement is to search for witnesses giving **matched** (equal)
companion sets on both sides, hoping symmetry closes the joint-coverage
gap.

**Construction.** For `a_1=247`: searching indices `k=1,2,\dots` for
`13\notin\mathrm{rad}(a_k)` and `\mathrm{comp}(a_k)\subseteq\{2,3\}$
finds `k=7`: `a_7=342=2\cdot3^2\cdot19$ (direct division: `342/2=171$,
`171/3=57$, `57/3=19$, `19$ prime — confirms `342=2\cdot3^2\cdot19$
exactly), `\mathrm{rad}(a_7)=\{2,3,19\}`, `13\notin\{2,3,19\}` ✓,
`\mathrm{comp}(a_7)=\{2,3,19\}\setminus\{13,19\}=\{2,3\}`. Searching for
`19\notin\mathrm{rad}(a_k)$ and `\mathrm{comp}(a_k)\subseteq\{2,3\}` finds
`k=6`: `a_6=312=2^3\cdot3\cdot13` (`312/2=156,156/2=78,78/2=39,39/3=13,13`
prime — confirms `312=2^3\cdot3\cdot13`), `\mathrm{rad}(a_6)=\{2,3,13\}`,
`19\notin\{2,3,13\}` ✓, `\mathrm{comp}(a_6)=\{2,3\}`.

By Lemma CB (§8.2, already certified — applicable since `I_{13},I_{19}`
are both nonempty, being infinite as `(S,S')` is a doubly-infinite pair),
`\{13\}` is never realized, so **every** `i\in I_{13}` has `P_i\supsetneq
\{13\}` strictly, i.e. is an escape from `\kappa=\{13\}` in the sense of
the Escape-Confinement Lemma; applying that lemma with witness `j_3:=7`
gives `P_i\cap\mathrm{comp}(a_7)=P_i\cap\{2,3\}\ne\varnothing` for
**every** `i\in I_{13}`, i.e. `\mathrm{comp}(a_i)\cap\{2,3\}\ne
\varnothing` for every `i\in I_{13}` (using `\{2,3\}\cap P_1=\varnothing`,
so the intersection cannot come from the core part of `P_i`). Symmetrically,
witness `j_3':=6` gives `\mathrm{comp}(a_j)\cap\{2,3\}\ne\varnothing` for
every `j\in I_{19}`. **Matched candidate:** `\Pi_{\mathrm{mw}}:=
\mathrm{comp}(a_7)\cup\mathrm{comp}(a_6)=\{2,3\}` — a *single* set,
individually valid (one-sided) on **both** sides, unlike round 11's
mismatched `\{2,5,7\}`.

For `a_1=4199` (`P_1=\{13,17,19\}`, `(S,S')=(\{13\},\{17\})`): the
identical search finds `k=11` blocking `\{13\}`: `a_{11}=4332=2^2\cdot
3\cdot19^2$ (`4332/2=2166,2166/2=1083,1083/3=361,361=19^2$ — confirms
`4332=2^2\cdot3\cdot19^2`), `\mathrm{rad}(a_{11})=\{2,3,19\}`,
`13\notin$ ✓, `\mathrm{comp}(a_{11})=\{2,3,19\}\setminus\{13,17,19\}=
\{2,3\}`; and `k=2` blocking `\{17\}`: `a_2=4212=2^2\cdot3^4\cdot13`
(`4212/2=2106,2106/2=1053,1053/3=351,351/3=117,117/3=39,39/3=13`  —
confirms `4212=2^2\cdot3^4\cdot13`), `\mathrm{rad}(a_2)=\{2,3,13\}`,
`17\notin$ ✓, `\mathrm{comp}(a_2)=\{2,3,13\}\setminus\{13,17,19\}=\{2,3\}`.
Again `\Pi_{\mathrm{mw}}=\{2,3\}$ — matched, and (by Lemma CB + the same
Escape-Confinement application, `S=\{13\}` never realized since `I_{13},
I_{17}` both nonempty) individually valid on both sides: `\mathrm{comp}
(a_i)\cap\{2,3\}\ne\varnothing` for every `i\in I_{13}`, `\mathrm{comp}
(a_j)\cap\{2,3\}\ne\varnothing` for every `j\in I_{17}`.

**Independent numerical confirmation (one-sided coverage, exhaustive on
the tested range, not sampled).** `a_1=247,N=20000`: `\mathrm{comp}(a_i)
\cap\{2,3\}\ne\varnothing` for **all** `10764/10764$ members of `I_{13}`
and **all** `6910/6910` members of `I_{19}` — zero exceptions.
`a_1=4199,N=15000`: **all** `3488/3488` members of `I_{13}` and **all**
`7695/7695` members of `I_{17}` — zero exceptions. Both exactly as
Escape-Confinement guarantees (a confirmation of an already-certified
lemma's consequence, not new content by itself — the new content is the
matched *choice* of witness, §9.4 shows it is still insufficient jointly).

#### 9.4 Explicit refutation of the Matched-Witness candidate — new
negative result, on both instances

**Claim.** `\Pi_{\mathrm{mw}}=\{2,3\}` does **not** solve the joint
Stabilization/Conjecture-(JW) condition for either instance: there exist
`i\in I_S,j\in I_{S'}` with `\mathrm{comp}(a_i)\cap\{2,3\}` and
`\mathrm{comp}(a_j)\cap\{2,3\}` nonempty but **disjoint** (a clash within
`\Pi_{\mathrm{mw}}` itself), so `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap
\Pi_{\mathrm{mw}}=\varnothing`.

**Proof, instance `a_1=247`.** Take `i=2`, `j=5`. `a_2=260=2^2\cdot5\cdot13`
(`260/2=130,130/2=65,65/5=13,13$ prime — confirms `260=2^2\cdot5\cdot13`),
so `\mathrm{rad}(a_2)=\{2,5,13\}$, `\mathrm{comp}(a_2)=\{2,5\}`, core `=
\{2,5,13\}\cap\{13,19\}=\{13\}`, so `2\in I_{13}`. `\mathrm{comp}(a_2)\cap
\{2,3\}=\{2\}`. `a_5=285=3\cdot5\cdot19` (`285/3=95,95/5=19,19$ prime —
confirms `285=3\cdot5\cdot19`), `\mathrm{rad}(a_5)=\{3,5,19\}`,
`\mathrm{comp}(a_5)=\{3,5\}`, core `=\{3,5,19\}\cap\{13,19\}=\{19\}`, so
`5\in I_{19}`. `\mathrm{comp}(a_5)\cap\{2,3\}=\{3\}`. `\{2\}\cap\{3\}=
\varnothing`: a genuine clash within `\Pi_{\mathrm{mw}}`. Indeed
`\gcd(260,285)=\gcd(2^2\cdot5\cdot13,\,3\cdot5\cdot19)=5` (the only common
prime factor is `5`), and `5\notin\{2,3\}`: `\mathrm{rad}(a_2)\cap
\mathrm{rad}(a_5)\cap\Pi_{\mathrm{mw}}=\{5\}\cap\{2,3\}=\varnothing`,
confirming the clash directly (not just via disjoint traces).
`\blacksquare`

**Proof, instance `a_1=4199`.** Take `i=9,j=5`. `a_9=4316=2^2\cdot13\cdot83`
(`4316/2=2158,2158/2=1079,1079/13=83,83$ prime — confirms `4316=
2^2\cdot13\cdot83`), `\mathrm{rad}(a_9)=\{2,13,83\}`, core `=\{2,13,83\}
\cap\{13,17,19\}=\{13\}`, so `9\in I_{13}`, `\mathrm{comp}(a_9)=\{2,83\}`,
`\mathrm{comp}(a_9)\cap\{2,3\}=\{2\}`. `a_5=4233=3\cdot17\cdot83`
(`4233/3=1411,1411/17=83,83$ prime — confirms `4233=3\cdot17\cdot83`),
`\mathrm{rad}(a_5)=\{3,17,83\}`, core `=\{3,17,83\}\cap\{13,17,19\}=
\{17\}`, so `5\in I_{17}`, `\mathrm{comp}(a_5)=\{3,83\}`, `\mathrm{comp}
(a_5)\cap\{2,3\}=\{3\}`. `\{2\}\cap\{3\}=\varnothing`: clash. Indeed
`\gcd(4316,4233)=83` (the only common prime factor), `83\notin\{2,3\}`.
`\blacksquare`

**Assessment.** Both counterexamples use indices `\le11`, are fully
hand-verifiable by direct division (shown above), and were found on the
**first** natural refinement attempt of round 11's construction, on
**both** confirmed Case B instances independently. This closes off, with a
rigorous proof rather than a numeric scan, the natural next idea a future
round might otherwise spend a session on ("choose matched witnesses via
Escape-Confinement, symmetry will close the gap") — it does not, and the
reason is exactly the Row-Restriction Obstruction of §9.2: `\mathrm{comp}
(a_7)=\mathrm{comp}(a_6)=\{2,3\}` links index `7` to *every* `i\in I_{13}`
and index `6` to *every* `j\in I_{19}` separately, but supplies no relation
between an arbitrary `i` and an arbitrary `j` directly — precisely the
missing cross-index link.

**Numerical scope of the joint failure (exhaustive on tested range, both
instances).** `a_1=247`: of `10764\times6910=74{,}379{,}240` cross pairs,
`3{,}920{,}643` (`\approx5.3\%`) clash against `\Pi_{\mathrm{mw}}=\{2,3\}`
(compare: round 11's mismatched `\{2,5,7\}` clashes on `9{,}534{,}512`
pairs, `\approx12.8\%` — matched witnesses are a genuine, measurable
improvement, just not a closure). `a_1=4199`: of `3488\times7695=
26{,}840{,}160` cross pairs, `2{,}542` (`\approx0.0095\%`) clash — a much
smaller failure rate on this instance, still strictly positive. In both
cases, the already-known candidate `\{2,3,5,7\}` (this file's §7.5,
round-10 finding) resolves the failures observed on `247` completely
(zero violations, previously verified); this round did not re-derive that
fact, only confirmed the matched-witness refinement alone is insufficient.

#### 9.5 Honest summary of this round's Case B attempt

Conjecture (JW) is **not** closed for either Case B instance this round.
What is new and fully rigorous: (a) a precise structural diagnosis (§9.2)
of exactly which certified tool is missing for Step 4′ to work in general
— a cross-index (not one-side-fixed) linking fact, absent from every
lemma in this file's toolkit, and explicitly absent *by definition* in
Case B (no class-wide backbone to supply it for free, unlike Case A); (b) a
genuinely new construction (Matched-Witness, §9.3) and its explicit,
hand-verified refutation on both mandatory instances (§9.4) — closing off
a natural next attempt with a proof, not a stall. **What would close the
gap**, restated precisely per this round's diagnosis: a mechanism showing
that `\mathrm{comp}(a_j)` and `\mathrm{comp}(a_{j'})` (for two different
`j,j'` on the same side, both in some `I_{S'}^{\tau'}`) share enough
common structure to force a common escape prime with an *arbitrary*
`i\in I_S^\tau` — genuinely new mathematics about the sequence's specific
arithmetic (why small primes like `2,3` — and, per §7.5, `5,7` — recur so
densely and so consistently in tandem across unrelated indices), not
reachable from the purely existential/pigeonhole machinery (Lemma P′, XC,
NIDF, FT, CB, Escape-Confinement) this file has built to date.

### 10. Round 13: Conjecture (WCE) — General Witness-Chaining Existence,
formalized into a proved sufficiency theorem; general existence honestly
left open, shown not easier than (JW)

Throughout, `(S,S')` is a doubly-infinite disjoint-core Case-B pair as in
§9 (no nonempty realized single-side backbone on either side). All facts
cited (Lemma P′, Lemma XC §7.1, Lemma NIDF §7.2, Lemma FT §7.3, Lemma CB
§8.2, Escape-Confinement Lemma §0) are already certified/proved earlier in
this file and are imported here, not re-derived.

#### 10.0 Precise statement of Conjecture (WCE)

Round 13's outline states (WCE) informally as: "every doubly-infinite
Case-B pair admits finitely many fixed low-index witnesses whose
companion-set disjunctions, chained by finite Boolean case-analysis, force
full pairwise coverage." This needs a precise formalization before it can
be proved or refuted — §10.1 supplies one, chosen specifically so that (i)
it captures the round-13 explorer's hand-built `4199` argument exactly
(verified in §10.3) and (ii) it is a genuinely *finite*, mechanically
checkable object (no hidden appeal to already knowing (JW) holds), matching
the explorer's own description ("a finite, checkable case tree, not an
asymptotic/magnitude argument"). We drop the requirement that witnesses be
"low-index" — nothing in the mechanism below uses the *numerical size* of
an index, only that it is an *actual* term of the sequence with a
*computable* (finite) companion set; low-index witnesses are simply the
ones that happen to be easy to search for by direct inspection, not a
mathematically distinguished class. This is a strictly more general (hence
harder to satisfy vacuously, easier to invoke) formalization than
requiring the witnesses to lie below some fixed bound.

#### 10.1 Formal definition: `R`-admissible patterns and witness-chaining sets

**Definition.** A **witness collection** for `(S,S')` is a pair of finite
sets `R_S\subseteq I_S`, `R_{S'}\subseteq I_{S'}`, both nonempty, with
`R:=R_S\cup R_{S'}`. Write `W:=\bigcup_{r\in R}\mathrm{comp}(a_r)` (finite:
a finite union of finite companion sets, each companion set being the
radical-complement of one fixed integer). For `\rho\in R_S` write
`W_\rho:=\mathrm{comp}(a_\rho)`, similarly for `\rho\in R_{S'}`.

Define the **`R`-admissible `S`-side patterns**
`\mathcal T_S(R):=\{\tau\subseteq W:\tau\cap W_\rho\ne\varnothing\text{ for
every }\rho\in R_{S'}\}` and symmetrically `\mathcal T_{S'}(R):=\{\tau'
\subseteq W:\tau'\cap W_\rho\ne\varnothing\text{ for every }\rho\in
R_S\}`. Both are finite sets of subsets of the finite set `W` (at most
`2^{|W|}` each), fully computable from the finitely many explicit sets
`\{W_\rho\}_{\rho\in R}` by direct enumeration — no reference to any index
outside `R` is needed to compute them.

**Definition (Chaining Success).** `R` **succeeds** for `(S,S')` if
`\tau\cap\tau'\ne\varnothing` for **every** `\tau\in\mathcal T_S(R)` and
**every** `\tau'\in\mathcal T_{S'}(R)`. This is a finite check: at most
`2^{|W|}\times2^{|W|}` pairs, each an elementary set-intersection test on
explicit finite sets of primes.

**Conjecture (WCE), precisely.** For every doubly-infinite Case-B pair
`(S,S')`, some witness collection `R` succeeds.

#### 10.2 Theorem (Chaining Sufficiency Theorem) — proved in full

**Statement.** If a witness collection `R=R_S\cup R_{S'}` succeeds for
`(S,S')` (§10.1), then `W:=\bigcup_{r\in R}\mathrm{comp}(a_r)` solves
Conjecture (JW) for `(S,S')`: `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap
W\ne\varnothing` for **every** `i\in I_S`, `j\in I_{S'}`.

**Proof.** Fix arbitrary `i\in I_S`, `j\in I_{S'}`. Let `\tau:=\mathrm{comp}
(a_i)\cap W` and `\tau':=\mathrm{comp}(a_j)\cap W` (both `\subseteq W`).

*Claim: `\tau\in\mathcal T_S(R)`.* Fix any `\rho\in R_{S'}\subseteq I_{S'}`.
Since `i\in I_S`, `\rho\in I_{S'}`, and `S\cap S'=\varnothing` (disjoint
cores, hypothesis on the pair), Lemma P′ gives `\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_\rho)\ne\varnothing`, and Lemma XC (applicable, disjoint
cores) upgrades this to `\mathrm{comp}(a_i)\cap\mathrm{comp}(a_\rho)\ne
\varnothing`, i.e. `\mathrm{comp}(a_i)\cap W_\rho\ne\varnothing`. Since
`W_\rho\subseteq W` (definition of `W`), `\tau\cap W_\rho=(\mathrm{comp}
(a_i)\cap W)\cap W_\rho=\mathrm{comp}(a_i)\cap W_\rho\ne\varnothing`
(using `W_\rho\subseteq W` to drop the redundant `\cap W`). This holds for
**every** `\rho\in R_{S'}$, proving `\tau\in\mathcal T_S(R)` by definition.

*Claim: `\tau'\in\mathcal T_{S'}(R)`.* Symmetric, fixing `\rho\in
R_S\subseteq I_S$ and applying Lemma P′+XC to the pair `(\rho,j)` (cores
`S(\rho)=S`, `S(j)=S'`, disjoint).

Since `R` succeeds, `\tau\cap\tau'\ne\varnothing`. But `\tau\cap\tau'=
(\mathrm{comp}(a_i)\cap W)\cap(\mathrm{comp}(a_j)\cap W)=\mathrm{comp}
(a_i)\cap\mathrm{comp}(a_j)\cap W`, so `\mathrm{comp}(a_i)\cap\mathrm{comp}
(a_j)\cap W\ne\varnothing`. Since `S(i)=S`, `S(j)=S'` are disjoint, Lemma XC
gives `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)=\mathrm{comp}(a_i)\cap
\mathrm{comp}(a_j)`, and `W\cap P_1=\varnothing` (every `W_\rho=\mathrm{comp}
(a_\rho)$ is disjoint from `P_1` by definition of `\mathrm{comp}`, so their
finite union `W` is too), so `\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap
W=\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap W`. Combining: `\mathrm{rad}
(a_i)\cap\mathrm{rad}(a_j)\cap W\ne\varnothing`. Since `i\in I_S,j\in
I_{S'}` were arbitrary, this holds for every cross pair. `\blacksquare`

**Remark (this theorem needs no size or index-order hypothesis on `R`
whatsoever)** — unlike the round-9/10 `(UB_S)`-flavoured attempts, nothing
here assumes `R`'s companion sets are small, nor that `R`'s indices are
"low." The theorem is unconditionally true for *any* successful `R`, of
any size; what it does **not** do is guarantee a successful `R` exists —
that is exactly Conjecture (WCE), addressed honestly in §10.7.

#### 10.3 Sanity check: the Theorem reproduces the explorer's `4199:(13,17)`
argument exactly

Take (per §9's data, this file, and the round-13 explorer's independently
verified factorizations) `S=\{13\}`, `S'=\{17\}`, `R_{S'}:=\{5,12\}\subseteq
I_{17}` (`\mathrm{comp}(a_5)=\{3,83\}`, `\mathrm{comp}(a_{12})=\{2\}`),
`R_S:=\{2,9\}\subseteq I_{13}` (`\mathrm{comp}(a_2)=\{2,3\}`, `\mathrm{comp}
(a_9)=\{2,83\}`). `W=\{2,3,83\}`.

`\mathcal T_S(R)=\{\tau\subseteq\{2,3,83\}:\tau\cap\{3,83\}\ne\varnothing,\,
\tau\cap\{2\}\ne\varnothing\}=\{\tau:2\in\tau,\,\tau\cap\{3,83\}\ne
\varnothing\}=\bigl\{\{2,3\},\{2,83\},\{2,3,83\}\bigr\}`.

`\mathcal T_{S'}(R)=\{\tau'\subseteq\{2,3,83\}:\tau'\cap\{2,3\}\ne
\varnothing,\,\tau'\cap\{2,83\}\ne\varnothing\}`. Direct enumeration of all
`2^3=8` subsets of `\{2,3,83\}`: `\varnothing` fails both; `\{2\}` hits
both (`2\in\{2,3\}`,`2\in\{2,83\}`) — included; `\{3\}` hits `\{2,3\}` but
`\{3\}\cap\{2,83\}=\varnothing` — excluded; `\{83\}` hits `\{2,83\}` but
`\{83\}\cap\{2,3\}=\varnothing` — excluded; `\{2,3\}` — included; `\{2,83\}`
— included; `\{3,83\}` hits `\{2,3\}` via `3` and `\{2,83\}` via `83` —
included; `\{2,3,83\}` — included. So `\mathcal T_{S'}(R)=\bigl\{\{2\},
\{2,3\},\{2,83\},\{3,83\},\{2,3,83\}\bigr\}`.

Checking all `3\times5=15` pairs `(\tau,\tau')\in\mathcal T_S(R)\times
\mathcal T_{S'}(R)$ for nonempty intersection (every `\tau\in\mathcal
T_S(R)` contains `2`, and every `\tau'\in\mathcal T_{S'}(R)` either
contains `2` or, if not, equals `\{3,83\}` which meets both `\{2,3\}` and
`\{2,83\}` via `3` resp. `83` — a direct case check on the 3 non-trivial
`\tau` values against the 5 `\tau'` values confirms all 15 pairs intersect,
matching exactly the case-split the explorer performed by hand in
`/tmp/round-13/math-explorer-case-b.md`): **`R` succeeds.** By the Chaining
Sufficiency Theorem, `W=\{2,3,83\}` solves Conjecture (JW) for
`4199:(13,17)` for all `i\in I_{13}\setminus\{2,9,12\}`, `j\in
I_{17}\setminus\{2,5,9,12\}` — matching the explorer's construction
exactly, now derived from a single general theorem rather than an ad hoc
case tree specific to this instance. (The finitely many excluded small
indices — those `\le12` used as witnesses themselves, or coinciding with
them — need a direct finite check, exactly as the explorer flagged; this
is elementary and not carried out here since it is instance-specific
bookkeeping, not part of the general theorem.)

#### 10.4 Corollary and cross-check against the Row-Restriction Obstruction

**Corollary.** If Conjecture (WCE) holds for `(S,S')` (some `R` succeeds),
then Conjecture (JW) holds for `(S,S')` (§10.2), hence — by this file's
already-certified reduction chain, Theorem SW → Theorem 5.1 (cited
verbatim, not re-derived here; see `results/imo-2026-06/current.md` and
`forced-primes-well-ordering`'s file for Theorem SW's statement) — the
pair contributes no obstruction to the whole problem's conclusion
`a_{n+T}=a_n+L`.

**Cross-check (the outline's Step 4).** The proof of the Chaining
Sufficiency Theorem (§10.2) applies Lemma P′+XC exactly twice per fixed
`(i,j)` pair: once to `(i,\rho)` for `\rho\in R_{S'}` (a **fixed** `S'`-side
index against the **free**, arbitrary `i`) and once to `(\rho,j)` for
`\rho\in R_S` (fixed `S`-side index against free `j`). At **no point** does
the proof compare `\mathrm{comp}(a_j)` to `\mathrm{comp}(a_{j'})` for two
different `j\ne j'\in I_{S'}`, nor `\mathrm{comp}(a_i)` to `\mathrm{comp}
(a_{i'})` for `i\ne i'\in I_S` — every application is "one side fixed
(a witness in `R`), the other side free (an arbitrary index of the
complementary class)," exactly the shape the Row-Restriction Obstruction
(§9.2) identified as available and unconditionally provided by Lemma P′.
This confirms, in the fully general formulation (not just the two worked
instances), that the Chaining Sufficiency Theorem's proof mechanism
structurally sidesteps the Row-Restriction Obstruction — as the outline
asked to re-confirm. **This does not mean the obstruction is defeated
in general**: §10.7 shows the obstruction re-appears, in a different
guise, in the *existence* question (does a successful `R` exist at all),
which the Theorem does not address.

#### 10.5 Proposition (Single-Witness-Per-Side Insufficiency) — proved in
full

**Statement.** Let `R_S=\{i_0\}`, `R_{S'}=\{j_0\}` (the minimal case,
`|R|=2$ — in particular the case supplied "for free," unconditionally, by
Lemma CB + the Escape-Confinement Lemma applied to a single blocking
witness on each side, §8.3, and by round 12's Matched-Witness construction
§9.3). Write `A:=\mathrm{comp}(a_{i_0})`, `B:=\mathrm{comp}(a_{j_0})` (both
nonempty by Lemma NIDF(a)). Then `R` succeeds **if and only if** `A=B` and
`|A|=1`.

**Proof.** `W=A\cup B`. `\mathcal T_S(R)=\{\tau\subseteq W:\tau\cap B\ne
\varnothing\}`, `\mathcal T_{S'}(R)=\{\tau'\subseteq W:\tau'\cap A\ne
\varnothing\}`.

(⟸) If `A=B=\{p\}` (singleton, equal): any `\tau\in\mathcal T_S(R)` has
`\tau\cap B=\tau\cap\{p\}\ne\varnothing`, forcing `p\in\tau`; symmetrically
`p\in\tau'` for every `\tau'\in\mathcal T_{S'}(R)`. So `p\in\tau\cap\tau'`
always — `R` succeeds.

(⟹) Suppose `R` succeeds; suppose toward a contradiction `A\ne B` or
`|A|\ge2$ or `|B|\ge2` (i.e. not both `A=B` and `|A|=1`). We produce a
failing pair `(\tau,\tau')`.

Case `|B|\ge2`: pick distinct `b_1\ne b_2\in B`, and any `a\in A` (`A`
nonempty). At most one of `b_1,b_2` equals `a`; pick `b\in\{b_1,b_2\}` with
`b\ne a`. Set `\tau:=\{b\}` (`\tau\cap B\ni b`, so `\tau\in\mathcal
T_S(R)`), `\tau':=\{a\}` (`\tau'\cap A\ni a`, so `\tau'\in\mathcal
T_{S'}(R)`). `\tau\cap\tau'=\{b\}\cap\{a\}=\varnothing` since `b\ne a` —
contradicts success. Case `|A|\ge2` is symmetric (swap roles).

Remaining case: `|A|=|B|=1`, say `A=\{a_0\}`, `B=\{b_0\}`, with `A\ne B`,
i.e. `a_0\ne b_0`. Set `\tau:=\{b_0\}\in\mathcal T_S(R)` (`\tau\cap B=
\{b_0\}\ne\varnothing`), `\tau':=\{a_0\}\in\mathcal T_{S'}(R)`. `\tau\cap
\tau'=\varnothing$ since `a_0\ne b_0` — contradicts success.

All cases contradict `R` succeeding, so `A=B` and `|A|=1` is forced.
`\blacksquare`

**Consequence.** This subsumes round 11's §8.4 rigidity-wall diagnosis and
round 12's §9.4 explicit Matched-Witness refutations (`4199`: `A=\{2,3\}=
B$, `|A|=2\ne1`; `247`: `A=\{2,3\}=B`, `|A|=2\ne1` — both fail the
proposition's criterion exactly, matching the hand-found counterexamples
`\gcd=83$/`\gcd=5$ respectively) into a single clean *characterization*,
not merely two isolated numeric counterexamples: **no** single-witness-
per-side chaining candidate can ever succeed unless the two witnesses
happen to share the exact same singleton companion set — an event never
observed in this workspace's data and with no known mechanism to force it.
This is why the round-13 explorer's `4199` construction genuinely needed
`\ge2` witnesses per side (`R_{S'}=\{5,12\}`, `R_S=\{2,9\}`, `|R|=4`), not
merely a refinement of the single-witness idea.

#### 10.6 The "free" Lemma FT transversal does not automatically succeed —
an explicit finite counterexample within the Theorem's own combinatorics
(`a_1=247`)

A natural hope: since Lemma FT (§7.3, already certified, unconditional for
*every* doubly-infinite pair) already supplies a finite transversal `U_S,
U_{S'}` for free, perhaps `R_S:=` FT's own representative indices,
`R_{S'}:=` FT's own representative indices, *always* succeeds — which
would make Conjecture (WCE) an immediate corollary of the already-certified
Lemma FT, with no further work. **This is false**, shown by an explicit
finite computation using this file's own already-recorded §7.5 data (no
new sequence generation needed — the four companion sets below are already
cited, reviewer-visible content from round 10's build).

For `a_1=247`, `(S,S')=(\{13\},\{19\})`: §7.5 records Lemma FT's greedy
construction giving `S`-side representatives with companion sets `A_1=
\{2,5\}`, `A_2=\{3,7\}` (so `R_S`'s witness set is `\{A_1,A_2\}`,
`U_S=\{2,3,5,7\}`), and `S'`-side representatives with companion sets
`B_1=\{2,7\}`, `B_2=\{3,5\}` (`U_{S'}=\{2,3,5,7\}`). Take `R:=R_S\cup
R_{S'}` accordingly, `W=\{2,3,5,7\}$.

`\mathcal T_S(R)=\{\tau\subseteq W:\tau\cap B_1\ne\varnothing,\,\tau\cap
B_2\ne\varnothing\}$. Take `\tau:=\{2,3\}`: `\tau\cap B_1=\{2,3\}\cap
\{2,7\}=\{2\}\ne\varnothing`; `\tau\cap B_2=\{2,3\}\cap\{3,5\}=\{3\}\ne
\varnothing`. So `\tau=\{2,3\}\in\mathcal T_S(R)`.

`\mathcal T_{S'}(R)=\{\tau'\subseteq W:\tau'\cap A_1\ne\varnothing,\,
\tau'\cap A_2\ne\varnothing\}`. Take `\tau':=\{5,7\}`: `\tau'\cap A_1=
\{5,7\}\cap\{2,5\}=\{5\}\ne\varnothing`; `\tau'\cap A_2=\{5,7\}\cap\{3,7\}=
\{7\}\ne\varnothing`. So `\tau'=\{5,7\}\in\mathcal T_{S'}(R)`.

`\tau\cap\tau'=\{2,3\}\cap\{5,7\}=\varnothing`. **`R` does not succeed** —
a genuine, exhaustively-checked failure of the Chaining Sufficiency
Theorem's hypothesis for this specific (fully explicit, already-certified)
`R`, even though `W=\{2,3,5,7\}` is *already numerically confirmed
(§7.5, ~75 million pairs, zero violations) to solve Conjecture (JW) for
this exact pair*. This is an important, honest scope note: the theorem's
combinatorial hypothesis is **strictly stronger** than the conclusion it
proves — a witness collection can fail the check while the resulting `W`
nonetheless happens to work (because not every abstract pattern
`\tau\in\mathcal T_S(R)` is actually *realized* by some `i\in I_S`; the
theorem, to stay unconditional and index-free in its hypothesis, must
account for all abstractly-admissible patterns, not just the realized
ones, which are unknown without deeper information). **Consequence**:
Conjecture (WCE) is not automatically true "for free" from Lemma FT — a
successful `R`, if it exists, must be found by a more careful search than
simply invoking the greedy transversal construction; a real,
non-trivial existence question remains, confirmed non-vacuous by this
computation rather than merely asserted.

#### 10.7 The general existence question — honest report: (WCE) is open,
and is not established to be easier than (JW)

**(WCE) itself is not proved or refuted this round, for arbitrary `a_1`.**
Here is the precise mathematical reason, argued rigorously rather than
merely asserted:

**(a) `\text{(WCE)}\Rightarrow\text{(JW)}` for every pair (proved, §10.4).**
So a hypothetical *general, unconditional* proof of Conjecture (WCE) for
*every* doubly-infinite Case-B pair would in particular constitute a
general, unconditional proof of Conjecture (JW) — the sole standing gap of
this workspace since round 10 (see `current.md`, this file's own §7.4/§8.4/
§9.5, and sibling `sunflower-inadmissibility-toolkit`/`forced-primes-well-
ordering`'s files, all independently converging on the identical
unresolved fact). **Hence (WCE), in its fully general form, cannot be
strictly easier than (JW)** — it is, at best, an equally hard,
constructively-strengthened restatement, not a bypass. This directly
corrects the round-13 outline's framing of this approach as attacking "a
genuinely complementary" (implicitly, potentially easier or independent)
question; the outline's own Step 3 anticipated this possibility ("if no
general bound found, report honestly") and this is exactly that honest
report.

**(b) The converse — does `\text{(JW)}` (abstract existence of *some*
finite `W`) imply `\text{(WCE)}` (existence of an actual, finite, provably-
successful witness collection `R`)? — is genuinely unclear, and the
natural attempt to derive it fails.** Given `W_0` solving (JW) abstractly,
one can define, for every realized companion-trace value `\tau\subseteq
W_0` on the `S`-side, a representative index `i_\tau` realizing it. But
showing that *these specific* representatives generate a **successful**
witness collection `R=\{i_\tau\}\cup\{j_{\tau'}\}` in the sense of §10.1
requires knowing `\mathrm{comp}(a_{i_\tau})\cap W_0` (a fact about `W_0`-
*trace* only) forces the corresponding **full-set** disjunctive constraint
`\mathrm{comp}(a_j)\cap\mathrm{comp}(a_{i_\tau})\cap W_0\ne\varnothing`
that the Chaining Sufficiency Theorem's proof needs — and Lemma P′ only
supplies `\mathrm{comp}(a_j)\cap\mathrm{comp}(a_{i_\tau})\ne\varnothing`
**without confining the witnessing prime to `W_0`**: the shared prime for
the pair `(i_\tau,j)` could be an "off-`W_0`" companion prime of
`\mathrm{comp}(a_{i_\tau})$ (which may be much larger than its `W_0`-trace,
exactly as `(UB_S)` is proven false in general — Case II companion sizes
are unbounded, §9). Concluding it lands in `W_0` requires *already knowing*
(JW) holds for the pair — circular, not a free construction. So the
implication `\text{(JW)}\Rightarrow\text{(WCE)}` is **not** established
either; the two conjectures' precise logical relationship (equivalent?
strictly ordered? independent modulo some third condition?) is itself
an open question this round newly identifies but does not resolve.

**(c) Why no tool currently in this file's certified toolkit guarantees a
successful `R` exists.** Every existence mechanism certified so far
(Lemma FT §7.3, Lemma CB + Escape-Confinement §8.2–8.3) supplies **one**
witness per side with an *a priori uncontrolled* companion set (possibly
very large, by the certified `(UB_S)`-false result, §9/round 9) and gives
**no information about which specific primes** occur in it beyond
nonemptiness (Lemma NIDF(a)) and pairwise nonempty intersection with any
fixed other index (Lemma P′+XC). None of these facts control **how many**
witnesses are needed, nor whether their companion sets will "interlock"
combinatorially in the sense §10.1–10.2 require (as opposed to, say,
`\S10.6`'s failing example, where two pairs of representative companion
sets are "orthogonal" — `\{2,5\},\{3,7\}` vs `\{2,7\},\{3,5\}` — a
combinatorial accident of which specific integers the greedy sequence
happened to produce at those specific indices, not a phenomenon derivable
from Lemma P′/XC/NIDF/FT/CB/Escape-Confinement alone). The recurring
"rescue prime" phenomenon (`83` in `4199`, occurring as a companion of
*two* low-index witnesses on opposite sides) that made the `4199`
construction work is, per the round-13 explorer's own honest assessment
(quoted, `/tmp/round-13/math-explorer-case-b.md`), "a direct, explicable
consequence of which two specific integers the greedy process produced at
those two positions" — i.e. genuine number-theoretic content about the
specific recursion's arithmetic, of exactly the kind rounds 6 and 9 already
confirmed (by exhaustive search of `knowledge_base.md` and the crux corpus)
has **no** applicable classical analytic or combinatorial tool. Proving
(WCE) in general would require either (i) a structural argument that small
primes must recur with sufficient density/interlocking across low-index
terms of *every* possible Case-B pair (a genuinely new number-theoretic
claim, not yet attempted, and likely as hard as (JW) itself per (a) above),
or (ii) abandoning the "explicit, hand-checkable" requirement and falling
back to an abstract compactness argument for (JW) directly — which, per
(b), is not known to follow from (WCE)-style reasoning either.

#### 10.8 Summary of this round's contribution

Conjecture (WCE) is **not** established, in either direction, for
arbitrary `a_1` this round. What is new and rigorous: a precise formal
definition (§10.1) turning the round-13 explorer's ad hoc mechanism into a
general, reusable object; the Chaining Sufficiency Theorem (§10.2, full
proof, verified against the explorer's own worked example in §10.3); the
Single-Witness-Per-Side Insufficiency Proposition (§10.5, a clean *iff*
characterization subsuming two rounds' worth of separate ad hoc
counterexamples); an explicit demonstration (§10.6) that the theorem is
non-vacuous (the "obvious free" witness choice fails it, on data already in
this file); and a precise, honest argument (§10.7) that Conjecture (WCE),
in full generality, is **not established to be easier than Conjecture
(JW)** — the hoped-for "genuinely complementary, possibly easier" framing
from this round's outline is not confirmed, and the report is that (WCE)'s
one-directional implication to (JW) means closing it in general would
close the whole problem, while the reverse implication (and hence any
claim that (WCE) is a strictly *weaker*, easier target) is neither proved
nor available from the certified toolkit. This is a genuine, if negative in
part, contribution: it gives the workspace reusable general machinery
(§10.2, usable directly by `forced-primes-well-ordering` to formalize its
own two concrete case trees rigorously instead of ad hoc, and by any future
instance) while correcting the scope of what "the general WCE question"
can be expected to deliver.

## Promotable lemmas

- **Chaining Sufficiency Theorem** — §10.2 above (round 13, new). Statement:
  for any doubly-infinite disjoint-core pair `(S,S')` and any witness
  collection `R=R_S\cup R_{S'}` (`R_S\subseteq I_S,R_{S'}\subseteq I_{S'}`
  finite nonempty) that "succeeds" (a purely finite, mechanically checkable
  combinatorial condition on the explicit companion sets of `R`'s members,
  §10.1), `W:=\bigcup_{r\in R}\mathrm{comp}(a_r)` solves Conjecture (JW)
  for `(S,S')`. Proved in full from already-certified Lemma P′ and Lemma
  XC alone, unconditionally (no size/index-order hypothesis on `R`).
  Genuinely reusable: `forced-primes-well-ordering` can cite it directly
  to formalize its own concrete case-tree work on `247:(13,19)` and
  `4199:(13,17)` instead of ad hoc per-instance reasoning; any future
  instance/approach attacking Conjecture (JW) for a specific pair can cite
  it as the target sufficient condition instead of re-deriving the
  disjunction-chaining mechanism from scratch.
- **Single-Witness-Per-Side Insufficiency Proposition** — §10.5 above
  (round 13, new). Statement: a witness collection `R=\{i_0\}\cup\{j_0\}`
  (the minimal, single-witness-per-side case) succeeds in the sense of the
  Chaining Sufficiency Theorem if and only if `\mathrm{comp}(a_{i_0})=
  \mathrm{comp}(a_{j_0})` and this common set is a singleton. Proved in
  full (elementary set-theoretic case analysis, no external citations
  beyond the definitions of §10.1). Subsumes and sharpens round 11's §8.4
  rigidity-wall diagnosis and round 12's §9.4 explicit Matched-Witness
  refutations into one reusable *iff* characterization — any future
  approach considering a single-witness-per-side construction can cite
  this directly instead of re-running an ad hoc search for a
  counterexample.

- **Lemma CB (Core Blocking)** — §8.2 above (round 11, new). Statement: for
  any disjoint nonempty cores `S,S'` with `I_S,I_{S'}` both nonempty (in
  particular, for either side of any doubly-infinite pair), `S` is
  automatically ERD-C-*blocked*, never realized (and symmetrically for
  `S'`). Proved in full from the already-certified Lemma NIDF(a) and Lemma
  ERD-C's dichotomy, by a short direct contradiction (a realized `S` would
  force some `i_0\in I_S$ with `\mathrm{comp}(a_{i_0})=\varnothing`,
  contradicting NIDF(a)'s unconditional nonemptiness). Reusable by any
  future cross-core-pair approach: it guarantees the Escape-Confinement
  Lemma's single-witness mechanism is *always* available on both sides of
  a doubly-infinite pair, with no case split on whether the core happens
  to be realized (that branch provably never occurs in this setting) —
  a genuine simplification of the case analysis for any future attempt at
  Conjecture (JW)/Stabilization.

- **Imprint Periodicity Lemma + corrected Density Sub-Lemma** — §6.1 above.
  Statement: if `a_{n+T}=a_n+L` for every `n\ge1` (exact periodicity, e.g.
  from Theorem 5.1), then `n\in I_{P_1}` is an exactly `\tau`-periodic
  property of `n` for a fixed, computable `\tau` (in fact `\tau\mid
  T\cdot\prod_{p\in P_1}p`); consequently, in Case II (no global hub prime),
  `\exists c=1/(2\tau)>0` with `|I_{P_1}\cap[1,N]|\le(1-c)N` for all large
  `N`. Proved in full from elementary arithmetic-progression periodicity
  arguments (no analytic tools). Reusable by any future approach needing a
  quantitative density statement about the top-core class, *conditional on*
  already having exact periodicity in hand (as any FCBC-based approach
  will, once it closes).

- **Euler's classical divergence of `\Sigma_p1/p`** — §6.2 above. Standard
  classical fact (1737), proved here from scratch via a self-contained
  smooth/rough-number split argument (no citation, no external Mertens
  machinery). General-purpose, reusable outside this problem's context.

- **Landau Count Lemma (via Turán's 1934 elementary second-moment
  argument)** — §6.3 above. Statement: for fixed `k`, `|\{m\le
  X:\omega(m)\le k\}|=o(X)`. Proved from scratch using only Euler's
  divergence (§6.2) and elementary floor/counting bounds — deliberately
  avoids needing the precise Mertens rate `S(X)=\log\log X+O(1)`, using
  only qualitative divergence `S(X)\to\infty`, which keeps every
  constant in the proof absolute. Confirmed absent from
  `knowledge_base.md`/the crux corpus by this round's outliner search.
  General-purpose, reusable outside this problem's context — a genuinely
  new tool for this workspace (rounds 6/6-confirmed analytic tools absent).

- **Theorem: `(UB_S)` is false in Case II, unconditionally** — §6.4 above
  (this round's central result). Combines the Imprint Periodicity Lemma,
  the Landau Count Lemma, and the already-certified Growth Lemma (Lemma 1)
  and `theorem-UBS-sufficiency.md`/§4c chain into a complete, gap-free
  refutation: it is impossible for `(UB_S)` to hold for every proper core
  simultaneously, for any `a_1` with `|P_1|\ge2` in Case II. This retires
  the entire round 4–8 `(UB_S)`/`(MRS)`/`\mathcal V_S`-finiteness-via-
  bundle-size program as a route to the whole problem; future rounds should
  not re-attempt proving `(UB_S)`, `(MRS)`, or `\mathcal V_S`-finiteness
  (for a proper core) in any form.

- **Lemma ERD-C (Eventual Realization Dichotomy for radical classes)** —
  §1 above. Statement: for any nonempty finite set of primes `C`, exactly
  one of (i) `C` is realized as some `P_m` (`m` finite), or (ii) `C` is
  permanently blocked by some witness `j` and never realized at any index.
  Proved in full from the already-certified Lemma ER, Lemma P′, and the
  Permanent-Inadmissibility Lemma; no circularity. Reusable by any approach
  needing to determine the fate of a candidate radical class (a genuine
  strengthening of Lemma ER, upgrading it from single integers to whole
  radical classes).

- **Lemma SR (Self-Realized core shortcut)** — §2 above. Statement: if a
  proper core `S` is itself realized as some actual term's exact radical,
  `\mathcal V_S` is automatically finite (`\subseteq\{S\}\cup\bigcup_{n<
  n_0}\mathcal M_n` for `n_0` any realizing index), **with no boundedness
  hypothesis on companion sizes needed**. Proved in full from the
  already-certified No-Resurrection Lemma. This is a clean, previously
  unstated unconditional partial result: it shows the whole `\Lambda_S`-
  finiteness question only has genuine open content in the "`S` blocked"
  branch of Lemma ERD-C, never in the "`S` realized" branch.

- **Δ-system (sunflower) dichotomy for uniformly bounded finite-set
  families** — §4a above. Standard classical combinatorial fact (confirmed
  absent from `knowledge_base.md` and the crux corpus by this round's
  keyword search, per the outline), proved here from scratch by induction
  on the size bound `M`, with an explicit, checked verification that the
  proof needs only bounded set size (not a finite ambient universe).
  General-purpose, reusable outside this problem's context.

- **Escape-Confinement Pairwise-Disjoint-Bundle-Count Corollary** — §4b
  Case (a) above (shared mechanism with `persistent-backbone-monovariant`'s
  Step 1 this round; proved independently here in the specific form needed
  for this approach). Statement: if a proper core `S` is blocked by witness
  `j_3`, every realized companion bundle for `S` meets the fixed finite set
  `\mathrm{comp}(a_{j_3})`, so any pairwise-disjoint family of realized
  bundles has size `\le|\mathrm{comp}(a_{j_3})|`. Unconditional (no
  `(UB_S)` needed for this Corollary itself).

- **Main Theorem (`(UB_S)\Rightarrow\Lambda_S` finite, for every proper
  core `S`, unconditionally beyond `(UB_S)`)** — §4 above (the file's
  central result). Combines Lemma ERD-C, Lemma SR, the Δ-system dichotomy,
  the Escape-Confinement Lemma, and the No-Resurrection Lemma into a single
  gap-free proof. This closes both sub-gaps ("core-avoiding witness
  existence," "`I_S` finite-vs-infinite") that the round-8 outline had
  flagged as needed but unproved — they turn out not to be independent
  hypotheses at all, only case distinctions the proof itself resolves.

- **Lemma XC (Cross-Companion Reduction)** — §7.1 above (round 10, new).
  Statement: for any two indices `i,j` with disjoint cores `S(i)\cap
  S(j)=\varnothing`, `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)=\mathrm{comp}
  (a_i)\cap\mathrm{comp}(a_j)` (the shared prime guaranteed by Lemma P′ for
  a disjoint-core pair is necessarily a companion prime, never a `P_1`
  prime). Proved in full, elementary, unconditional (3-line disjoint-union
  argument). Reusable by any future approach reasoning about cross-core
  pairs — reduces every "does `rad(a_i)\cap rad(a_j)\cap W\ne\varnothing`"
  question for a disjoint-core pair to a purely companion-side question.

- **Lemma NIDF (Nonempty Companions, No Infinite Disjoint Sub-family)** —
  §7.2 above (round 10, new). Statement: for disjoint nonempty cores
  `S,S'` with `I_S,I_{S'}\ne\varnothing`: every companion set on either
  side is nonempty, and neither side's companion-set family contains an
  infinite pairwise-disjoint sub-family. Proved in full from Lemma P′ +
  Lemma XC + a pigeonhole injection into one fixed (always-finite)
  companion set — **needs no size-boundedness hypothesis on either
  family**, unlike the certified Δ-system Dichotomy Lemma. This is the
  key new tool that resolves this round's mandatory Step-0 gap: it applies
  regardless of whether `(UB_S)`/`(UB_{S'})` hold for the specific pair,
  which (per `theorem-UBS-false-case-II.md`) can never be verified in
  general.

- **Lemma FT (Finite One-Sided Transversal)** — §7.3 above (round 10,
  new). Statement: for any doubly-infinite disjoint core pair `(S,S')`,
  there is a finite set `U_S` (a union of finitely many actual companion
  sets from a greedily-chosen pairwise-disjoint sub-collection of `I_S`)
  meeting every companion set of `I_S`; symmetrically `U_{S'}`. Proved in
  full via a greedy-maximal-disjoint-collection argument terminating by
  Lemma NIDF(b), unconditional. Reusable by any future approach needing a
  one-sided (not yet joint) finite covering fact for a class `I_S`. Comes
  with an honestly-reported, precisely diagnosed open gap (Conjecture
  (JW), §7.4) for upgrading it to the full two-sided Stabilization
  Conjecture — not itself a promotable "solved" result, but the Lemma
  proper (one-sided covering) is fully proved and certifiable as stated.
