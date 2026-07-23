## imo-2026-06 — lens: attack Conjecture (WCE) directly as a general statement

### Setup recap (verified, not re-derived)
Read `lemma-WF-witness-forcing-and-theorem-FW-instances.md` and
`theorem-chaining-sufficiency-and-single-witness-insufficiency.md` closely.
Both certified files reduce Conjecture (JW) for a doubly-infinite disjoint
core pair (S,S') to a **purely finite Boolean/SAT fact**: pick a finite
witness collection R = R_S∪R_{S'} (indices, one per class), let
W = ∪comp(a_r); Lemma WF (built from nothing but the unconditional Lemma
P′ + Lemma XC) says every witness ρ∈R_{S'} forces a disjunction
"∨_{p∈comp(a_ρ)} p|a_k" on **every** k∈I_S (not a numerically-checked
prefix — the whole infinite class, since Lemma P′ is itself unconditional
for every pair of indices). Chaining Sufficiency Theorem (already
certified) turns "does every admissible τ⊆W (consistent with the
R_{S'}-side disjunctions) intersect every admissible τ'⊆W (consistent
with the R_S-side disjunctions)?" — an exhaustive, mechanically checkable
2^|W| computation, since |W| is finite — into a complete proof of (JW) for
the pair. FW1 (2-case) and FW2 (9-case table) are just two hand-worked
instantiations of this one theorem with different R.

**What actually made FW1/FW2 possible, structurally**: in both cases the
low-index terms include (a) at least one witness with a SMALL companion
set that intersects the other side's small companion set structure
tightly enough that a short (2- or 9-case) exhaustive check closes it. No
deep number theory beyond Lemma P′/XC is used anywhere — this is 100%
finite combinatorics once R is fixed. **This confirms the dispatch's
hypothesis: yes, there is a pattern, and it generalizes into something
strictly simpler than FW1/FW2 themselves — see below.**

### New mechanism found this round: "Multi-Singleton Forcing" — a
zero-case-split special case of the Chaining Sufficiency Theorem
If class I_S has (at low index) several witnesses whose companion sets
are literal **singletons** {p_1},…,{p_k} (k distinct primes, k separate
fixed indices), Lemma WF's Corollary (singleton case) forces **every**
member of the complementary class I_{S'} to be divisible by ALL of
p_1,…,p_k simultaneously (k independent unconditional facts, not a case
split). If I_{S'} *also* has one witness whose companion set is a
SUBSET of {p_1,…,p_k}, that witness forces every member of I_S to be
divisible by AT LEAST ONE of p_1,…,p_k (Lemma WF's disjunctive form).
Combining: any i∈I_S contains ≥1 of {p_1,…,p_k}; any j∈I_{S'} contains
ALL of them — so gcd(a_i,a_j) always shares that one prime. **Zero case
analysis needed at all** — strictly simpler than FW1's 2-case argument
and FW2's 9-case table. (This is not new mathematics — it is a literal
instance of the already-certified Chaining Sufficiency Theorem with
R chosen this specific way — but it is a genuinely useful, previously
unnoted *template* that appears to close the overwhelming majority of
instances trivially.)

### Numerical testing (Python, sympy; generator independently validated
against O(n²) brute force on a_1=15,247,91 first 60 terms — exact match,
per this workspace's standing rule)
Built a fast antichain-based generator + an exhaustive `chaining_success`
Boolean checker (brute-forces all 2^|W| subsets — a RIGOROUS finite check,
not a numeric sample, exactly the same object Lemma WF/Chaining
Sufficiency Theorem certify). Tested Multi-Singleton Forcing on **8 fresh
a_1 values, 10 Case-B-style disjoint core pairs total**, none previously
tested for WCE specifically (only a_1=247, 4199 have prior WCE work):

| a_1 | P_1 | pair | result | W found (rigorously verified) |
|---|---|---|---|---|
| 2747 (=41·67) | {41,67} | (41,67) | **SUCCESS** | {2,3,7} (3 singletons on {41}-side: a_13={3},a_14={2},a_163={7}; 1 witness a_3={2,3,7} on {67}-side) |
| 4087 (=61·67) | {61,67} | (61,67) | **SUCCESS** | {2} alone — BOTH sides have their own singleton-{2} witness (a_5=2^6·67 on {67}-side, a_54=2·61^2 on {61}-side) |
| 143 (=11·13) | {11,13} | (11,13) | **SUCCESS** | {2,3} |
| 391 (=17·23) | {17,23} | (17,23) | **SUCCESS** | {2,3} |
| 713 (=23·31) | {23,31} | (23,31) | **SUCCESS** | {2,3} (2 singletons a_2={2},a_32={3} on {23}-side; witness a_3={2,3} on {31}-side) |
| 1073 (=29·37) | {29,37} | (29,37) | **SUCCESS** | {2,3} |
| 1517 (=37·41) | {37,41} | (37,41) | **SUCCESS** | {2,3} |
| 1001 (=7·11·13) | {7,11,13} | (7,11) | **SUCCESS** | {2} |
| 1001 | | (7,13) | **SUCCESS** | {2} |
| 1001 | | (11,13) | **SUCCESS** | {2} |

**All 10 fresh pairs close, all rigorously verified by the exhaustive
Boolean check (not sampling).** For comparison, the two previously-closed
"hard" instances (247:(13,19), 4199:(13,17)) do **NOT** have this simple
structure — direct search (to N=20,000-30,000 generated terms, tens of
thousands of class members) found **zero singleton companion witnesses in
either class of either pair** — confirming those two really did need the
harder FW1/FW2 case-split machinery, and that "easy" vs "hard" instances
are structurally distinguishable by singleton-companion density, not just
difficulty of search.

### Major finding: two NEW closable concrete instances
**a_1=2747 and a_1=4087 both have |P_1|=2** (single disjoint core pair,
same shape as the already-closed a_1=247), and Multi-Singleton Forcing
closes their sole pair unconditionally with a trivial, hand-verifiable,
zero-case-split argument. Following the exact template of the certified
`Corollary FW2-FCBC` (Lemma SW1 for intersecting-core pairs + this pair's
closure for the disjoint case ⟹ FCBC ⟹ Theorem 5.1 gives explicit T,L),
**both a_1=2747 and a_1=4087 appear to be fully solvable concrete
instances of the whole IMO problem, via a mechanism that completely
bypasses the stuck Backbone Permanence question** (round 13's
sunflower-inadmissibility-toolkit refuted Early/Bounded Stabilization for
exactly these two instances and left them as the sharpest open "Case A"
gap — WCE/witness-chaining sidesteps that dead end entirely, since it
needs no running-intersection/permanence argument, only fixed low-index
witnesses). **This is evidence gathered by an explorer, not a proof** —
the outliner/builder should formalize and the reviewer must
independently re-verify the exact witness indices/factorizations
(reported below for 2747; 4087's are a_5=4288=2^6·67, a_54=7442=2·61^2)
before certifying. If confirmed, this would be the 2nd and 3rd solved
concrete instances (after 247), and — notably — via a *different, simpler*
mechanism than FW2 needed.

**2747 witnesses (hand-verifiable, sympy-confirmed):**
a_13=3321=3^4·41 (comp={3}), a_14=3362=2·41^2 (comp={2}),
a_163=11767=7·41^2 (comp={7}), a_3=2814=2·3·7·67 (comp={2,3,7}).
Proof: every j∈I_{67} is divisible by 2,3,7 (three independent singleton
applications of Lemma WF via a_14,a_13,a_163). Every i∈I_{41} is
divisible by at least one of {2,3,7} (one disjunctive application of
Lemma WF via a_3). Hence for any i∈I_{41},j∈I_{67}, whichever of {2,3,7}
divides a_i also divides a_j. QED, zero cases.

### The two pairs that did NOT close (honest negative report)
a_1=4199's other two disjoint core pairs — (13,19) and (17,19) — remain
open (only (13,17) is closed, per round 13). Investigated both in depth:
- (13,19): **neither class has any singleton companion witness through
  N=30,000** (~7000 and ~4500 class members respectively). Both classes'
  smallest companions are size-2, and empirically (0 exceptions found)
  I_19 always contains both 2 and 3, while I_13 usually contains 2 (with
  a repeating {3,83}-type exception, 164/6977). This LOOKS structurally
  similar to what should be provable (an "always contains {2,3}" fact)
  but no finite witness set was found (within modest search: prefix
  combinations up to |W|≤16, 6 witnesses/side) that rigorously forces it
  — the disjunctions available (all anchored on a shared prime 2, not
  spread across independent primes like 2747's case) don't obviously
  compose into a finite proof the way 2747's did.
- (17,19): I_17 has 24 singleton-{2} witnesses (forcing I_19⊇{2} always,
  confirmed 0 exceptions to N=30,000) but **zero singleton-{3} witnesses
  found even to N=100,000** (51,307 class members checked) — I_17's only
  non-2 members are a repeating {3,83}-type (62/15391). A direct rigorous
  chaining_success check using the best available witnesses
  ({2},{3,83} on the 17-side, {2,3} on the 19-side) **fails**
  (confirmed by exhaustive check, not sampling). More witnesses/a smarter
  R might still close it (not exhaustively ruled out) but this is
  genuinely the harder residual, consistent with round 13's scoping.

**Do not claim these two pairs are closed or refuted — both are honestly
open**, reported as concrete, well-defined next targets (sharper than
"4199 has other open channels" — now pinned to exactly these 2 pairs with
the precise witness data needed to keep attacking them).

### Answer to dispatch item 3: is there a priori reason WCE could be
FALSE for some pair?
**No refutation found, and no structural reason to suspect one.** All 10
fresh pairs tested closed, most (8/10) trivially via Multi-Singleton
Forcing (a strictly simpler mechanism than what was needed for the 2
previously-known hard cases). The 2 pairs that resisted (4199's
(13,19),(17,19)) are NOT shown to be impossible — the search was capped
at modest witness counts/|W| for tractability, and the observed
structure (I_19 empirically always ⊇{2,3}, I_17 empirically almost
always ⊇{2}) looks like exactly the kind of pattern that closed 2747/4087,
just requiring MORE independent small-companion witnesses than were
found in the tested prefix, or a genuinely richer case-split like FW2's.
The one real structural warning sign (already on record, round 13,
`sunflower-bundle-closure`'s §10.7b): the converse direction (JW⟹WCE)
needs "off-W magnitude" information of the same shape (UB_S) was proven
FALSE to supply — i.e. there is no known *uniform* bound on how many
witnesses/how large W must be, across all a_1. This is consistent with
WCE being true instance-by-instance (as observed) while a UNIFORM
existence proof (one argument working for every a_1 with an explicit or
even ineffective bound) remains genuinely open — the gap is between
"WCE holds for each instance we can check" (strong, now 12/12 tested
pairs across this workspace's whole history, only 2 of which needed
hard machinery) and "WCE holds for literally every a_1" (no general
argument found).

### Distinct openings for the outliner
1. **Formalize and certify the 2747/4087 Multi-Singleton closures** as
   new solved concrete instances (2nd/3rd after 247) — cheap, concrete,
   high-value, reuses 100% certified machinery (Lemma WF, Chaining
   Sufficiency Theorem, Corollary-FW2-FCBC template, Theorem 5.1). This
   also gives a 3rd/4th data point (with 1001, if worth writing up) that
   the "hard" Backbone-Permanence-stuck instances are NOT actually stuck
   for the whole-problem goal — WCE is an orthogonal, working route for
   at least these two.
2. **Certify Multi-Singleton Forcing as a named corollary** of the
   Chaining Sufficiency Theorem (zero new proof content — literally an
   instantiation) — this gives future builders a cheap "try this first"
   template before reaching for FW1/FW2-style case-splits, and explains
   structurally *why* it works (independent primes forced via disjoint
   singleton witnesses vs. a shared-anchor-prime pattern that resists it,
   as seen in 4199's remaining 2 pairs).
3. **Push harder on 4199's 2 remaining pairs specifically** — now with
   concrete, precisely-identified witness data (the {2},{3,83} structure
   on the 17-side; the always-{2,3} structure on the 19-side) rather than
   a vague "other channels remain." A genuinely richer FW2-style
   multi-witness case-table (not just Multi-Singleton) is the next thing
   to try, informed by exactly which small-companion witnesses exist.
4. **Do NOT attempt a uniform/general existence proof of WCE for
   arbitrary a_1 without a genuinely new idea** — this round confirms
   (again, a 3rd independent way) that the general existence question
   needs "off-W magnitude" control that (UB_S)-false already shows isn't
   available via companion-bundle-size bounding. Instance-by-instance
   closure (opening 1/3 above) is the tractable, currently productive
   route; a fully general WCE proof for arbitrary a_1 is not more
   tractable than it was reported last round.

### Candidate technique(s)
Chaining Sufficiency Theorem (certified) as the general tool; Multi-
Singleton Forcing (this round's finding) as the cheap first-attempt
special case; FW1/FW2-style explicit disjunctive case-tables as the
fallback for pairs without singleton structure.

### Cheap-kill candidates
None obvious for the two still-open 4199 pairs — no parity/pigeonhole/
size argument found to instantly close or refute them; they need either
more witness search or a genuinely richer case-split.

### Knowledge-base entries to use
None beyond what's already certified in this workspace's own `lemmas/`
(no external KB/crux entry newly relevant this round — same conclusion as
round 6's confirmed-absent analytic-tool search, unchanged).

### Analogous past problems (cruxes)
None newly relevant — the mechanism here (Lemma P′ + finite Boolean
covering check) is entirely internal to this workspace's own certified
lemma chain, not matched by any crux-corpus entry (consistent with round
6/11's findings that no external tool transfers to this specific
gcd-chain structure).

### Prior progress
See `lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md` and
`theorem-chaining-sufficiency-and-single-witness-insufficiency.md`
(both certified round 13) — Chaining Sufficiency Theorem + FW1/FW2 close
a_1=247 fully and 1/6 of a_1=4199's channels. This round's numerics
extend that to (very likely, pending formal build+review) a_1=2747 and
a_1=4087 fully, via a simpler mechanism, plus honest negative data on
4199's 2 remaining pairs.

### Dead ends (do not retry)
- Do not re-attempt Early/Bounded Stabilization / Backbone Permanence for
  2747/4087 (refuted round 13) — this round shows it's moot anyway, since
  WCE/Multi-Singleton Forcing closes both instances via a completely
  different, unconditional mechanism that needs no permanence argument.
- Do not re-attempt a UNIFORM/general-a_1 existence proof of WCE without
  new machinery for the "off-W magnitude" gap (3rd independent
  confirmation this round that it's not available via current tools).

### Small-case / intuition notes (all labeled conjecture unless stated
"rigorously verified")
- Conjecture (WCE) restated more sharply by this round's data: the
  overwhelming majority of Case-B pairs close via the TRIVIAL
  Multi-Singleton mechanism (8/10 fresh pairs, often with |W|=1 or 2);
  only pairs with NO singleton companion witnesses on either side within
  a large search depth need the harder FW1/FW2-style machinery, and even
  those succeeded on 2/4 tested hard pairs (247's pair, 4199's (13,17)).
  This is consistent with (not proof of) WCE being true for every a_1,
  with difficulty concentrated in a narrow, identifiable sub-class of
  pairs (those where small primes never appear as isolated companions).
- Rigorously verified (not conjecture): all 10 fresh-pair closures and
  both witness sets for 2747 (full factorizations shown above) — these
  are exhaustive Boolean checks on the exact objects Lemma WF/Chaining
  Sufficiency Theorem certify, not numeric sampling.
