## imo-2026-06 — outline review, round 9

### 0. Verdict on the headline reframing judgment call

**The reframing is mathematically sound. APPROVE the reframe as a matter of logic**,
subject to the per-approach corrections below. Verified directly:

- `lemmas/theorem-UBS-sufficiency.md`'s title and statement are literally
  `(UB_S) ⟹ Λ_S finite` (one arrow, not `⟺`); `lemmas/lemma-MS-minimal-radical-
  stabilization-sufficiency.md` is likewise `(MRS) ⟹ FCBC`, one direction. Round
  8's own reviewer report already checked the converse (`Λ_S`-finite `⟹ (UB_S)`)
  and found it **false** in general (a dominated/never-minimal index can carry an
  unboundedly large bundle while `Λ_S` stays finite). So there is no certified
  equivalence anywhere in the chain that `(UB_S)` false would contradict — the
  outliner's claim "`(UB_S)` was only ever sufficient, never necessary, for FCBC"
  is correct, not wishful reading.
- Checked directly whether FCBC (a fixed finite `H` hits every pair) forces any
  bound on `ω(a_n)`: it does not — `H` need only be present in every pair's
  intersection; nothing stops a term's radical from carrying arbitrarily many
  *extra* primes outside `H`. So "bundle size keeps growing, no plateau" and "a
  small fixed `H` still hits every pair" are logically compatible, not in tension.
  No hidden contradiction found.
- The one place a real trap lives is exactly where the outline itself flags it:
  "every term touches `H`" (individual, Step 3 in `explicit-window-backbone-
  construction`) is **not** the same claim as "every *pair* touches `H` at the
  *same* element" (Step 4). The outline states this distinction explicitly and
  does not conflate the two — this is the correct discipline (see §1 below for a
  finding that Step 3 is nonetheless mis-classified as "free").

### 1. Independent verification (fresh Python, own generator + antichain reduction
via the certified Lemma W3, cross-checked against the antichain-freeze method
used by prior rounds)

All code below is fresh this round (not reused from any prior round's or
explorer's scripts), using a numpy smallest-prime-factor sieve + an
inclusion-minimal-radical antichain to decide admissibility (Lemma W3, already
certified, used only as a speed-up — the check itself is the literal
`gcd(x,a_i)>1` definition).

**1a. Confirms the round-9 explorers' headline numeric claim independently.**
For `a_1=247`, pushed to `N=500,000` (`a_n` to `14,360,619`, sieve to `15M`):
found the record `ω=8` term at **exactly** `n=408816`, `a_{408816}=11,741,730 =
2·3·5·7·11·13·17·23`, off the top core — matches
`math-explorer-minimality.md`'s claim to the digit. **The `current.md` round-8
numeric-claim correction flag is confirmed correct**: `247→6` (round 8) should
read `247→8` (`n=408816`); by the same explorer's independently-reproduced
number, `2747→8` (`n=374037`). The proof-reviewer should apply this correction
to `current.md` after this round's builds (per dispatch, not done here).

**1b. Extends Step 3's empirical support (`explicit-window-backbone-
construction`) to a fresh range/case.** For `a_1=247`, 0/500,000 terms have
radical disjoint from `{2,3,5,7,11,13}` (extends the explorer's `0/1,300,000`
claim with an independent implementation). For `a_1=2747` (`P_1={41,67}`), to
`N=357,399`: 1395 terms are disjoint from the *small-6* set alone (fine — they
touch `P_1`), but **0** are disjoint from the *full* candidate `H:=P_1∪
{2,3,5,7,11,13}` — i.e. Step 3 holds for both tested cases in the extended
range.

**1c. NEW finding — genuine counterexample to the literal Step 4 (Pairwise
Small-Sharing) conjecture on the hardest case, found within `n<1000`.** Checked
directly whether the *specific* candidate `H:=P_1∪{2,3,5,7,11,13}` satisfies
Pairwise Small-Sharing (i.e. whether the family of realized `H`-signatures is
pairwise intersecting) — this had **not** been tested by any round-9 explorer.
Result:
- `a_1=247` (to `n=500,000`, 64 distinct `H`-signatures) and `a_1=2747` (to
  `n=357,399`, 125 distinct signatures): **zero** violating pairs — the literal
  candidate `H` already satisfies FCBC's pairwise requirement on the entire
  tested range for both cases.
- `a_1=21528751` (the workspace's hardest case, `P_1={103,197,1061}`): **found
  a genuine, concrete violation** at `n=596` (`a_{596}`, radical `∩H=
  {2,3,5,7,1061}`) vs. `n=863` (`a_{863}`, radical `∩H={11,103,197}`) — these
  two realized signatures are disjoint, so the literal candidate `H` **fails**
  FCBC on this pair. (These are a genuine *cross-core* pair — exactly the "hard
  case" the outline names.) By Lemma P′ they must still share some prime; direct
  computation finds it: **`97`**, not in `H`. Adding just this one bridge prime
  (`H':=H∪{97}`) restores pairwise-sharing with **zero** further violations
  through `n=300,000` (231 distinct signatures checked).

This is exactly the fallback the outline itself anticipated ("(b) find and
report a genuine counterexample... which would itself be valuable negative
content" / "(a)... strengthening H with a finite, explicitly-constructed extra
set of bridge primes"). **Action for the builder**: do not spend effort trying
to prove the literal unpatched `H:=P_1∪{2,3,5,7,11,13}` suffices — it is
already known to fail on the hardest case, cheaply. Start directly from the
"bridge primes" version, and use `97` (bridging cross-core pair
`n=596`/`n=863` for `a_1=21528751`) as the first concrete data point. The real
open question sharpens to: **does the total bridge-prime patch stay finite (and
ideally small/`a_1`-computable) as more cross-core pairs are checked, or does it
grow without bound the way `(UB_S)`'s bundle sizes did?** This is the one
question that would actually decide this approach's fate — flag it explicitly
in the built file, do not let a small-N "zero violations" reading substitute for
addressing it.

**1d. NEW finding — `sunflower-bundle-closure`'s literal Density Sub-Lemma
(Step 3, `|I_{P_1}∩[1,N]|=o(N)`) is very likely FALSE as stated.** Directly
measured the top-core fraction `|I_{P_1}∩[1,N]|/N` for both `a_1=247` and
`a_1=2747` at ten checkpoints each from `N=50,000`/`30,000` up to
`500,000`/`210,000`: in **both** cases the fraction is already a **stable
positive constant** by the first checkpoint and does not move at all
thereafter — `0.1163` for `247`, `0.0204` for `2747`. This is the opposite of
`o(N)` (vanishing density); it looks like `Θ(N)` at a fixed rate (plausibly
because the sequence's residue-class behaviour has already locked into its
long-run pattern by `n~50,000`, consistent with this workspace's repeated
finding that these antichains freeze early). **This does not kill the
approach — the Step 5 contradiction only actually needs the *weaker* fact
`|I_{P_1}∩[1,N]|≤(1-c)N` for some fixed `c>0` (density bounded away from `1`,
not from `0`)**, which is exactly what the observed stable ~2–12% top-core
density gives directly, with room to spare. The outline's own "Watch out" note
half-anticipates this ("Step 3 needs a LOWER bound on `|I_{P_1}^c|`") but the
formal Skeleton Step 3 states the stronger, apparently-false `o(N)` form.
**Required correction for the builder**: retarget Step 3 to `∃c>0` with
`|I_{P_1}∩[1,N]|≤(1-c)N` for all large `N` (equivalently `|I_{P_1}^c∩[1,N]|=
Ω(N)`, not `o(N)`) — re-verified by hand that this weaker form, combined with
the Growth Lemma and the Landau Count Lemma exactly as before, still gives the
identical contradiction (`cN≤o(N)`⟹`c≤o(1)`, contradiction, since `c` is a
fixed positive constant). This is a "wrong quantifier direction" bug of
exactly the kind this workspace's Rules warn about (round 2's `H_n` mixup);
catching it before the builder invests in proving a false o(N) claim is the
main value of this review pass.

### 2. Per-approach review

**explicit-window-backbone-construction — APPROVE (with one required fix
to the "free" claim).** Sound technique, genuinely different in kind from
rounds 4–8's count-bounding machinery (never bounds a bundle's size, only
asks pairs to share a fixed witness), correctly built on the already-certified
Lemma W1 (FCBC `⟺` Key Lemma) and Theorem 5.1 (gap-free). Steps 1/2/5 are
genuinely free. **Issue found**: the outline's "Open gaps" paragraph
mis-classifies Step 3 (Small-Uniform-Hit) as "free or... with a named
mechanism," implying it needs no independent proof — but the cited mechanism
(Domination Lemma) only shows *some* prime factor of the next term already
divides many prior terms; it does **not** say that prime lies in a fixed small
set like `{2,3,5,7,11,13}`. Step 3 is a genuine, unproven (though well-
supported, §1b above) empirical claim, not a free consequence, and the built
file must say so plainly rather than treating only Step 4 as open. Case
coverage (same-core / cross-core / top-core pairs) is complete and correctly
laid out. Hand the builder §1c's concrete counterexample and bridge-prime
finding directly — it saves a wasted attempt at the unpatched claim and gives
a first real data point for the "does the patch stay bounded" question, which
is the approach's actual crux.

**sunflower-bundle-closure — CHANGES REQUESTED (fixable, not fatal).**
Genuinely new tool for this workspace (an elementary Landau/Mertens-induction
density argument), logically valid contradiction structure, and a clean,
high-value target (a rigorous refutation of `(UB_S)` would retire the entire
`(UB_S)`/`(MRS)`/`Λ_S` family for every future round, exactly as round 2/3's
refutations retired `H_n`/`W`-finiteness). **Required fix**: replace the
Density Sub-Lemma's literal `o(N)` statement with the weaker, apparently-true
`|I_{P_1}∩[1,N]|≤(1-c)N` form per §1d — the stronger form is very likely false
and should not be pursued. With that correction the argument's logic is intact
end-to-end; the two remaining tasks (the corrected density lower bound, and
the from-scratch Landau count lemma) are both concrete and of a difficulty
this workspace has handled before (classical, elementary, Mertens-based).
Watch-outs are otherwise correctly stated (no casework needed, `o(N)`≠`0`
already flagged).

**intersecting-family-covering-construction — APPROVE.** Legitimate third,
independent technique (necessity/witness-pool stabilization per pair of cores,
not a single universal small window and not S^+-seeded) built on top of this
file's own already-certified, gap-free Theorem 5.1 — the strongest existing
infrastructure in the population (Elo 1720 going into this round, now 1721).
The Stabilization Conjecture (Step 3) is honestly scoped as "the real new
content," correctly distinguished from `(UB_S)` (a finite *used-witness pool*
per core-pair is compatible with individual bundles growing unboundedly — this
distinction is checked and correct, matching §0's own logic check above). This
is meaningfully more general than `explicit-window`'s fixed universal `H` (it
allows different core-pairs to need different witness primes), so it is not a
redundant restatement of that sibling's Step 4, even though both attack the
same underlying difficulty from different angles — legitimate diversity per
CLAUDE.md's "different route to the same target lemma" allowance. Cross-check
candidate `H`s against the sibling as the outline itself requests.

**forced-primes-well-ordering — CHANGES REQUESTED / DEFER this round (not
cut).** Technique (per-core `S^+`-seeded patch) is a legitimate, distinct
mechanism in principle — `S^+_S` already encodes core-specific necessary
primes that a universal window does not — but as scoped this round it uses
**the identical small-prime patch** (`{2,3,5,7,11,13}`) as
`explicit-window-backbone-construction`'s Step 2, on the identical remaining
difficulty (pairwise sufficiency). Given §1c's finding — the plain small patch
already fails on exactly this file's own hardest documented `S^+`-failure
instance (`a_1=21528751,S={1061}`) and needs a bridge prime (`97`, found this
round) not obviously reachable from `S^+_S` alone — building both approaches
in the same round risks re-discovering the identical wall twice with the
identical fix. Recommend the outliner/builder next round explicitly test
whether `S^+_S∪{97}∪{2,3,5,7,11,13}` (or similar) closes the documented
`S={1061}` gap, informed by whatever `explicit-window`'s build this round
finds about the bridge-prime patch's growth. Not RETHINK — the `S^+`
machinery is real, certified, reusable content regardless.

### 3. Diversity check

Four techniques this round: (1) analytic-density refutation of `(UB_S)`
(sunflower), (2) explicit universal small window + pairwise-sharing
(explicit-window), (3) per-core-pair witness-pool stabilization
(intersecting-family), (4) per-core `S^+`-seeded patch (forced-primes). (2)
and (4) share a candidate set and the identical open sub-question this round
(flagged above); (1) is genuinely orthogonal (attacks the sufficient-condition
side, not FCBC itself); (3) is the most general FCBC-direct formulation. This
is real diversity of *route*, not four variations of one framing — consistent
with CLAUDE.md's standing allowance for genuinely different routes to a shared
target — but the (2)/(4) overlap is real enough to justify deferring one this
round rather than building both in full.

### 4. `current.md` numeric-claim correction (flag for builders/proof-reviewer,
not fixed here per instructions)

Confirmed independently (§1a): round-8's `current.md` claim "max ω(a_n) stays
single-digit: 247→6, 2747→6, 21528751→7" needs updating to the round-9-
confirmed true values within reach this round: **`247→8` (n=408816),
`2747→8` (n=374037)**; `21528751` not yet pushed past 7 (its core primes are
much larger, needs proportionally larger `N`). The proof-reviewer should apply
this correction to `current.md` after this round's builds land.

### 5. Whole-attempt check

All four approaches target the problem's actual claim end-to-end: each, if it
closes its stated open content, invokes the already-certified, gap-free
Theorem 5.1 chain to finish the *entire* problem (`a_{n+T}=a_n+L` for every
`n≥1`) — none is a sub-lemma fragment split across slugs. No violation of the
single-gap-trap rule found.

### 6. Ranking

Ranked the whole sampled field (`update_ranking` called), anchoring this
round's redirected quartet against the standing population
(`persistent-backbone-monovariant`, deprioritized this round per the
outline's own explicit "not advanced" call; `core-depth-induction`,
`global-recruiter-finiteness`, `bounded-gap-density-covering`, all unchanged
dead/parked). Within the quartet: `intersecting-family-covering-construction`
and `explicit-window-backbone-construction` rank highest (soundest
infrastructure, cleanest verified support, no found flaw beyond the Step-3
mis-classification, which is a labeling fix not a mechanism flaw);
`sunflower-bundle-closure` next (sound technique, but its central sub-lemma as
literally stated is likely false, a real if fixable issue found this round);
`forced-primes-well-ordering` ranked above the deprioritized
`persistent-backbone-monovariant` but below the other three FCBC-direct
approaches, reflecting this round's redundancy finding.

build set: sunflower-bundle-closure, explicit-window-backbone-construction, intersecting-family-covering-construction
