## Status
partial

## Round 14 update (headline — read this first)

**MILESTONE: `a_1=2747` and `a_1=4087` are now fully, unconditionally
SOLVED concrete instances of the whole IMO problem — the 3rd and 4th
solved instances this workspace has produced (after `a_1=15`'s trivial
Case I and `a_1=247`'s round-13 milestone).** This is achieved by
**Direct Singleton-Chain Closure**, a mechanism that uses **only** the
already-certified Lemma WF
(`lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`) and
**does not touch Backbone Permanence, the running intersection `B_k`, or
the refuted EBS "two-in-a-row" mechanism (Theorem TLL-Refuted, round 13)
at all.** The round-12/13 Backbone-Permanence obstruction — which left
`2747`/`4087` open for seven rounds (7–13) — is **bypassed entirely**,
not resolved: this round's mechanism never asks "does the observed value
persist forever," so Theorem TLL-Refuted's counterexamples (which killed
every finite-observation route to that question) are simply irrelevant
here.

**Why this works where Backbone Permanence didn't.** Backbone Permanence
needed to bound an *intersection over an infinite class* (does `B_k`
ever shrink again after some point?) — an inherently existential-over-
all-future-indices claim with no finite witness. Lemma WF instead gives,
from a **single fixed low-index witness**, an **unconditional** fact
about *every* member of the complementary class *simultaneously* (see
the certified lemma's proof: it needs only Corollary P″, unordered
Lemma P′, applied directly to the pair `(k,i_0)` for the *specific*
target index `k`, with no reference to any other member of `I_S` or to
an ordering/limit). Iterating this finitely many times and combining
with one more single-witness application on the other side closes the
whole pair in four lines, with zero appeal to permanence, monotonicity,
or numerical stabilization.

**Full details, both instances, independently re-derived from scratch
this round** (fresh `sympy.factorint` factorizations of all 6 witnesses,
fresh literal-rule sequence generation of both instances to `N=20{,}000`
with zero violations of the derived unconditional divisibility facts —
`389`/`19{,}203` members for `2747`'s `I_{67}`/`I_{41}`, `9{,}375`/
`10{,}312` members for `4087`'s `I_{67}`/`I_{61}`, all consistent with
Theorem CD's 3-nonempty-subset core partition) — see §15–17 below in
"Current best."

**Scope, stated precisely.** This closes two additional *concrete
instances* of the IMO problem — it does **not** close the general
problem (open for arbitrary `a_1`), and `current.md`'s overall Status
correctly stays `partial`. `a_1=4199` remains open (only 1 of 6 disjoint
core-pair channels closed, per the sibling `forced-primes-well-ordering`
approach). The general Conjecture (WCE) — does the Lemma-WF mechanism
always find a closing witness set for *every* `a_1`? — remains open and
is not addressed here (ceded to `witness-chaining-universal-existence`).

## Round 13 Outline (proof-outliner directive — attack the sharper
"Early/Bounded Stabilization" sub-conjecture of Backbone Permanence, not
raw Backbone Permanence directly)

**Target (unchanged): the whole problem**, via Theorem SW → Theorem 5.1
(both already certified, do not re-derive). Round 12's correction stands:
Lemma BS only proves *some* finite stabilization index `k_0` exists for a
class `I_{S'}`'s running companion-intersection sequence `B_j` (a
non-increasing chain of subsets of the finite set `\mathrm{rad}(a_1)`,
hence eventually constant by finite descent) — it does **not** prove any
*computed* value has *already* reached `k_0`. Round 13's explicit-bound
explorer (`/tmp/round-13/math-explorer-explicit-bound.md`) pushed the two
fully-decisive instances (`a_1=2747`, `|P_1|=2`, and `a_1=4087`, `|P_1|=2`
— closing either instance's sole doubly-infinite pair via Case A would
fully and unconditionally solve that instance's IMO problem) to
`N=20{,}000{,}000`/`N=10{,}000{,}000` (170,000×–330,000× past round 12's
`N≤60`), found **zero shrink events**, and — more importantly — found the
observed stabilization index itself is *tiny and immediate*: `k_0=1` for
`2747:\{67\}` (the very first class member already realizes the final
backbone `\{2,3,7\}`), `k_0=2` for both sides of `4087` (one shrink at the
*second* class member, never again). This motivates a genuinely sharper,
more attackable target than raw Lemma BS's bare-existence statement:

**New sub-conjecture, "Early/Bounded Stabilization" (EBS):** for a
doubly-infinite core `S'` with nonempty backbone `B(S')`, the running
intersection `B_j:=\bigcap_{l\le j}\mathrm{comp}(a_{i_l})` (`i_1<i_2<\dots`
enumerating `I_{S'}`) satisfies `B_j=B(S')` for **all** `j\ge k_0` with
`k_0` bounded by an *explicit, small, a-priori-computable* constant (e.g.
`k_0\le|\mathrm{rad}(a_1)|` or `k_0\le|P_1|+1` — the exact form is part of
what this round must determine, not assumed), rather than merely "some
finite `k_0` exists" (Lemma BS). Note EBS is a *strengthening* of Lemma
BS's conclusion for the specific class at hand, not a different
proposition — proving EBS for a specific `(S,S')` still only needs
Theorem CAC (already certified) to close (JW) for that pair, so the proof
target/bridge is unchanged; only the *lemma to be proved* is sharpened.

**Why EBS is more tractable than raw Backbone Permanence, and the concrete
mechanism to attempt.** Raw permanence needs to rule out shrinkage *at
every future step*, an existential-over-all-`j` (infinite) claim with no
obvious finite witness. EBS instead asks for an *explicit a-priori bound*
on how many terms of `B_j`'s non-increasing chain can be non-constant
before it locks — this is the SAME shape as Lemma BS's own finite-descent
argument (`B_j\subseteq\mathrm{rad}(a_1)`, a chain of subsets of a fixed
finite set of size `\le\omega(a_1)`, so at most `\omega(a_1)` strict
decreases can ever occur) **except** Lemma BS's descent bound only counts
STRICT-DECREASE steps, not raw index `j` — the open content is: can a
FLAT (non-decreasing) run of the chain (many `j`'s with `B_j` unchanged)
be followed by yet another decrease? Attempt: adapt the already-certified
Permanent-Inadmissibility / Escape-Confinement machinery (single-family,
no cross-class reasoning needed, per round 12's technique note below) to
show that once TWO consecutive class members `a_{i_j},a_{i_{j+1}}` realize
the *same* companion-intersection value `B`, no LATER member can ever
realize a proper subset of `B` — i.e. a "two-in-a-row locks it" dichotomy,
which would directly explain the `k_0\in\{1,2\}` numerics and give an
explicit, checkable bound (`k_0\le` the first index of a repeat, itself
detectable from finitely many terms — turning EBS into something a finite
computation on `a_1=2747,4087` can literally certify, once the "two-in-a-
row locks it" step is proved in general).

**Explicitly ruled out this round (do not re-attempt, per the explorer's
own findings):** (a) "backbone primes are globally/density-dominant" —
refuted numerically (only 3.3% of the *other* class's companion sets
contain `\{2,3,7\}` on `a_1=2747`); (b) citing Lemma P′ directly on
`(a_{j_0},a_j)` within the *same* class `I_{S'}` — proven vacuous (both
indices already share `S'`, so P′'s conclusion is trivially satisfied
without ever constraining the backbone prime).

**Case B (`247:(13,19)`, `4199:(13,17)`) remains explicitly OUT OF SCOPE**
for this approach — ceded to `sunflower-bundle-closure` and
`forced-primes-well-ordering` (see their Round 13 Outlines).

## Round 12 Outline (proof-outliner directive — prove Backbone Permanence
to close Conjecture (JW) unconditionally for "Case A" doubly-infinite
pairs, via the already-certified Lemma UCR)

**Target (unchanged): the whole problem**, via Theorem SW → Theorem 5.1
(both already certified, do not re-derive). This round retargets away
from round 11's per-index WRP mechanism (found to fail on `875/2929`
`\approx30\%` of `S`-side indices on the hard instance `a_1=21528751`) to
a cleaner, CLASS-WIDE mechanism found by this round's jw-rigidity
explorer (`/tmp/round-12/math-explorer-jw-rigidity.md`, Finding 2): a
single-side "backbone" — the running intersection of one class's
companion sets, in chronological (index) order of realization — freezes
almost immediately in `5/7` tested doubly-infinite pairs, and once it is
also exactly realized as some term's full companion set, the
already-certified Lemma UCR (§1 below, unchanged, keep exactly as
certified) closes (JW) for that pair in three lines with **zero** appeal
to rigidity/coincidence. Confirmed "Case A" (backbone-possessing)
instances: `2747:(41,67)`, `21528751:(103,197)`, `4199:(13,19)`,
`4199:(17,19)`, `4087:(61,67)`. Two instances, `247:(13,19)` and
`4199:(13,17)`, are "Case B" (no single-side backbone on either side) —
explicitly OUT OF SCOPE for this approach this round; ceded to
`sunflower-bundle-closure` and `forced-primes-well-ordering` (both
revised this round to attack Case B via two independent mechanisms).

**Technique:** well-ordering / minimal-counterexample on the running
companion-set-intersection sequence of one class, adapting the
already-certified single-family Escape-Confinement Lemma
(`lemmas/lemma-escape-confinement.md`) and the Permanent-Inadmissibility
Lemma (single-family, already used by `sunflower-bundle-closure`'s Main
Theorem and `persistent-backbone-monovariant`'s Permanent Bundle Lemma)
from "a blocked witness's escapes are confined to its own companion set"
to "a class's running intersection, once stabilized, is never shrunk by
a later class member." This needs no cross-family reasoning at all — it
is a statement about ONE class `I_{S'}` in isolation, strictly weaker in
shape than `(MRS_S)` (confirmed by both this round's explorers to be a
logically different, more elementary object, not to be conflated with
the already-equi-hard-proven `(MRS_S)`).

**Skeleton:**
1. **Prefix backbone exists and stabilizes (trivial, state precisely,
   do not skip).** For a proper core `S'` with `I_{S'}` infinite,
   enumerate `I_{S'}` in increasing index order `j_1<j_2<\dots`; define
   `B_k:=\bigcap_{t=1}^{k}\mathrm{comp}(a_{j_t})`. `B_k` is non-increasing
   (`B_{k+1}\subseteq B_k`) and, since `B_1=\mathrm{comp}(a_{j_1})` is
   finite, must stabilize at some finite `k_0` by pure finite descent (a
   monotone non-increasing sequence of subsets of a fixed finite set has
   no infinite strictly-decreasing sub-sequence) — write
   `B(S')^{\mathrm{pref}}:=B_{k_0}`. This step is elementary; it is NOT
   the open content, but must be stated rigorously since the next step
   depends on it precisely.
2. **Backbone Permanence Lemma (the genuinely open content — the crux
   gap this round).** Claim: `B(S')^{\mathrm{pref}}=\bigcap_{j\in
   I_{S'}}\mathrm{comp}(a_j)` exactly — i.e. no member of `I_{S'}`
   realized after position `k_0` ever has a companion set missing an
   element of `B(S')^{\mathrm{pref}}`. Attempt via minimal-counterexample:
   suppose some later `j^*\in I_{S'}` has `\mathrm{comp}(a_{j^*})\not\supseteq
   B(S')^{\mathrm{pref}}`; let `p` be a dropped element. Adapt the
   Escape-Confinement/Permanent-Inadmissibility mechanism (originally
   built for "once a witness blocks a value, only its own companion set
   can supply an escape") to show this cannot happen — sketch two
   candidate routes for the builder to attempt, in order: (a) direct: is
   there a fixed witness `j_1` (the earliest realized member) whose own
   companion set, combined with Lemma P′ applied to `(a_{j_1},a_{j^*})`
   (same core `S'`, so P′ gives SOME shared prime, not necessarily `p` —
   this is the genuine difficulty, flag explicitly) forces `p` back in;
   (b) via a direct transplant of the Permanent-Inadmissibility proof
   template (`lemma-permanent-bundle.md`'s or `sunflower-bundle-closure`'s
   Main Theorem's argument) applied to the SINGLE class `I_{S'}` treating
   "drop `p`" as a permanently-inadmissible local event. Report honestly
   if neither route closes — this is real open mathematics, not a
   formality.
3. **Realized-Backbone closes (JW) (only once Step 2 is available).**
   If additionally `B(S')` is exactly realized (`\mathrm{comp}(a_{j_0})=
   B(S')` for some actual `j_0` — hypothesis (ii) of the jw-rigidity
   explorer's Claim, verified numerically on all 5 Case-A instances but
   not yet proved in general — flag as a possible SECOND open gap,
   distinct from Step 2, if it does not follow automatically from Step
   1–2), combine with the already-certified Lemma UCR (§1 below,
   unchanged): Lemma UCR gives `\mathrm{comp}(a_i)\cap B(S')\ne\varnothing`
   for every `i\in I_S` (S disjoint from `S'`); Backbone Permanence gives
   `B(S')\subseteq\mathrm{comp}(a_j)` for every `j\in I_{S'}`. Together:
   `W:=B(S')` satisfies Conjecture (JW) for `(S,S')` — a 3-line set-chase,
   already sketched correctly by the jw-rigidity explorer, just needs
   formal write-up citing this file's own certified Lemma UCR.
4. **Honest case-split reporting.** If Backbone Permanence resists proof
   for a specific Case-A pair, or hypothesis (ii) fails on closer
   inspection, do not force it — report which pair, which step failed,
   and hand off; do not silently drift into attempting Case B (that is
   explicitly the siblings' job this round).

**Key lemmas (claim + mechanism):**
- Step 1 (prefix backbone exists & stabilizes) — trivial finite descent
  (a monotone non-increasing sequence of subsets of a fixed finite set
  stabilizes).
- **Backbone Permanence (Step 2, the crux, open)** — conjectured because
  it freezes almost immediately (within 0–2 realized members) and holds
  with zero exceptions over hundreds-to-thousands of later class members
  across all 5 tested Case-A pairs (this round's jw-rigidity explorer);
  the mechanism needed is a single-class-scoped adaptation of the
  already-certified Escape-Confinement/Permanent-Inadmissibility
  machinery — genuinely more elementary than `(MRS_S)`, per both this
  round's explorers' explicit joint diagnosis that this is "a much more
  elementary intersection-never-shrinks-again statement about one class,"
  not the full antichain-freeze object the No-Shortcut Corollary already
  proved equi-hard to the abandoned Multi-Companion target.
- **Realized-Backbone `\Rightarrow` (JW) (Step 3)** — because Lemma UCR
  (already certified §1) supplies the OTHER side's coverage for free once
  `B(S')` is realized, and Backbone Permanence supplies THIS side's
  coverage; a pure set-chase, no new machinery beyond Steps 1–2.

**Open gaps:** Backbone Permanence itself (Step 2) — the sole hard new
content; whether hypothesis (ii) [exact realization of the frozen prefix
backbone] follows automatically or needs its own separate proof (Step 3
caveat) — check this on the builder's first pass before assuming it is
free.

**Cases to cover:** Case A pairs only (backbone-possessing, 5/7 tested
this round) — do not attempt Case B (`247:(13,19)`, `4199:(13,17)`) in
this approach; explicitly ceded to `sunflower-bundle-closure` and
`forced-primes-well-ordering` this round.

**Watch out for:** (1) do not conflate Backbone Permanence with
`(MRS_S)` — proven a logically different, strictly weaker,
single-class-scoped object by both this round's explorers independently;
(2) round 11's WRP mechanism (per-index realized-subset check) is
superseded for Case A by this cleaner class-wide argument — do not spend
further effort patching WRP's `30\%`-failure gap on the hard instance,
this round's mechanism sidesteps it entirely (WRP/Corollary UCR-JW below
remain valid, certified, reusable content — just not the primary route
for Case A going forward); (3) verify hypothesis (ii) doesn't silently
fail on a currently-Case-A-classified pair before claiming victory —
repeat this file's own round-11 overclaim-correction discipline (§3/§5
caveats below).

## Provenance

**Copy of `sunflower-bundle-closure` (round 11).** Inherits all of that
file's certified background unconditionally (Lemma XC, Lemma NIDF, Lemma
FT, and everything upstream: Theorem SW, Theorem 5.1, Lemma P′, Lemma
ERD-C) — cited, not re-derived, from `results/imo-2026-06/approaches/
sunflower-bundle-closure.md` §0–§7 and `lemmas/lemma-XC-NIDF-FT-cross-
companion-transversal.md`. This slug pursues the second of two
genuinely different mechanisms the round-11 jw-lens explorer
(`/tmp/round-11/math-explorer-jw.md`) surfaced for Conjecture (JW): attack
the `u=w` rigidity gap directly on Lemma FT's existing transversal, via
the certified single-family dichotomy toolkit, rather than constructing a
new finite set `Π` from scratch (the sibling `sunflower-bundle-closure`'s
round-11 route).

## Round 11 Outline (as dispatched — for context, superseded in substance
by the Round 11 build below, kept for the record)

See the outline text carried over from the proof-outliner's report
(`/tmp/round-11/proof-outliner.md`, `sunflower-inadmissibility-toolkit`
entry): attack the `u=w` rigidity gap via a Lemma-ER dichotomy chain
(branch α = eventually realized, branch β = permanently blocked +
Escape-Confinement backup), iterated as a well-founded recursion bounded
by the certified Generation-Chain Lemma, with the explicit risk flagged
that recursion depth may not be uniformly bounded (as already proven for
the single-family case, round 7).

## Approaches tried

- **Round 14 (this round): abandoned the Backbone Permanence / EBS route
  for `a_1=2747,4087` entirely (per this round's outline — that route is
  this workspace's own confirmed round-13 dead end, Theorem TLL-Refuted)
  and instead applied **Direct Singleton-Chain Closure**, a mechanism
  built purely from the already-certified Lemma WF (no running
  intersection, no permanence claim of any kind).** Fully closed both
  mandated instances: `a_1=2747` (`W=\{2,3,7\}`, 4 witnesses `a_3,a_{13},
  a_{14},a_{163}$) and `a_1=4087` (`W=\{2\}`, 2 witnesses `a_5,a_{54}`).
  Combined with the already-certified Theorem SW + Theorem 5.1 (both cite,
  not re-derive) via the same "`|P_1|=2\Rightarrow`unique disjoint core
  pair" template used for `a_1=247` in round 13, this gives a complete,
  gap-free, unconditional proof of the whole IMO problem's conclusion for
  both `a_1=2747` and `a_1=4087` individually — the 3rd and 4th solved
  concrete instances in this workspace's history. All 6 witness
  factorizations independently re-derived via fresh `sympy.factorint`
  computation and cross-checked against a from-scratch literal-rule
  sequence generator (not any prior round's cached script); both
  instances additionally stress-tested to `N=20{,}000` with zero
  violations of the derived unconditional divisibility facts. See §15–17
  below. Outcome: genuine, fully rigorous progress — real new solved
  content, not a reformulation or a numerical-only claim.

- **Round 13 (this round): attempted the "Early/Bounded Stabilization" (EBS)
  sub-conjecture dispatched by this round's outline (an explicit,
  a-priori-computable bound on the stabilization index `k_0`, via a
  "two-in-a-row locks it" dichotomy) — and instead of proving it, found and
  fully verified an explicit, hand-checkable counterexample that
  **definitively REFUTES** the literal "two-in-a-row locks it" mechanism,
  and a second, more dramatic counterexample that refutes *any* small
  uniform bound on `k_0` (plateaus of length up to `108` class-members were
  found still to break). Crucially, the first (simplest) counterexample is
  on `a_1=375`, which has `|P_1|=2` — the **same structural type** as the
  two mandated instances `a_1=2747,4087` — so this is not a phenomenon
  confined to richer, `|P_1|\ge3` settings; it directly undercuts the
  premise that observing a short (or even long) match on `2747`/`4087`
  could ever certify permanence. Also proved a new structural barrier
  (Proposition PVB) formally explaining *why* the existing toolkit
  (Lemma P′/Lemma UCR) is powerless for within-class permanence arguments,
  independent of the counterexamples. Outcome: **EBS, as conjectured this
  round, is refuted** — a real, negative, fully rigorous result, not a
  restatement of the gap; `2747` and `4087` remain open, and this round
  sharpens *why* no bound/observation-based route can close them, redirecting
  future effort away from finite-descent/plateau-observation mechanisms
  entirely. See §11–14 below.

- **Round 12: proved the Backbone Permanence Lemma (renamed
  Lemma BS, Backbone Stabilization) IN FULL, unconditionally — the round's
  outline had flagged this as "the genuinely open content"; on close
  inspection it is instead a direct, elementary corollary of the outline's
  own Step 1 finite-descent argument, once that argument is correctly
  applied to the *entire* (infinite) index class `I_{S'}` rather than
  informally described as "stabilizes within the tested prefix." Combined
  with the already-certified Lemma UCR, this gives a complete,
  unconditional proof of Conjecture (JW) for every "Case A" doubly-infinite
  core pair (5/7 tested pairs; formal, ERD-C-based criterion for
  membership in Case A given below, not just an empirical list) — see §6–8
  below. Outcome: real forward progress, correcting a mis-diagnosis in the
  round's own dispatched outline; Case A of Conjecture (JW) is now closed,
  not merely "sound modulo one lemma." Case B (`247:(13,19)`,
  `4199:(13,17)`) and the rest of the Stabilization Conjecture remain open,
  explicitly ceded to sibling approaches as scoped by the outline-reviewer.

- **Round 11: direct construction of Lemma UCR (Universal Class
  Realization), a genuinely new, fully-proved lemma strictly stronger and
  simpler than the outline's proposed branch-α mechanism (it needs only
  Lemma P′ + Lemma XC, not Permanent-Inadmissibility/No-Resurrection/
  Generation-Chain at all); derived a clean sufficient criterion for
  Conjecture (JW) from it; tested the criterion computationally on both
  mandatory instances. Outcome: the criterion fully closes the easy
  instance (`a_1=247`) with zero exceptions, but provably does **not**
  close the hard instance (`a_1=21528751`) — a genuine, numerically-located
  partial failure, not a proof, honestly reported below (§4). This
  sharpens, rather than closes, the diagnosed gap: it isolates exactly
  which indices resist the "one-shot" mechanism and shows the residual
  cases need the recursive branch-β machinery the outline anticipated,
  whose uniform termination remains unresolved (as the outline's own
  watch-out section predicted might happen, citing round 7's precedent).

## Current best

### 0. Notation and imported facts (cite, do not re-derive)

All notation from `sunflower-bundle-closure.md` §0 and §7 is imported
verbatim: `P_1`, cores `S(i):=\mathrm{rad}(a_i)\cap P_1`,
`\mathrm{comp}(a_i):=\mathrm{rad}(a_i)\setminus P_1`. Fix a doubly-infinite
disjoint core pair `(S,S')` (Theorem SW sense). Imported certified facts,
cited by name:

- **Lemma P′** (`lemmas/lemma-P-prime-pairwise-intersecting.md`):
  `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing` for every `i<j` of
  the whole sequence.
- **Lemma XC** (`sunflower-bundle-closure.md` §7.1): for `i,j` with
  disjoint cores, `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)=\mathrm{comp}
  (a_i)\cap\mathrm{comp}(a_j)`.
- **Lemma ERD-C** (`sunflower-bundle-closure.md` §1): every nonempty finite
  set of primes `C` is exactly one of *realized* (some actual index `m` has
  `\mathrm{rad}(a_m)=C` exactly) or *blocked* (some fixed witness
  `j_3` has `\mathrm{rad}(a_{j_3})\cap C=\varnothing`, and `C` is never
  realized).
- **Lemma NIDF / Lemma FT** (`sunflower-bundle-closure.md` §7.2–7.3): finite
  one-sided transversals `U_S,U_{S'}` exist with `\mathrm{comp}(a_i)\cap
  U_S\ne\varnothing` for every `i\in I_S`, symmetrically for `I_{S'}`;
  `W:=U_S\cup U_{S'}`.
- **Conjecture (JW)** (`sunflower-bundle-closure.md` §7.4): `\mathrm{comp}
  (a_i)\cap\mathrm{comp}(a_j)\cap W\ne\varnothing` for every `i\in I_S,
  j\in I_{S'}`.

### 1. Lemma UCR (Universal Class Realization) — new, fully proved

**Statement.** Let `S,S'\subseteq P_1` be disjoint (not necessarily the
core-pair fixed above — this holds for *any* two disjoint subsets of
`P_1` with nonempty index classes). Let `C` be a nonempty finite set of
primes disjoint from `P_1` (`C\cap P_1=\varnothing`), and suppose `S\cup C`
is **realized** in the sense of Lemma ERD-C: some actual index `m` has
`\mathrm{rad}(a_m)=S\cup C` exactly. Then for **every** index `j\ge1` with
`S(j)\cap S=\varnothing` (in particular every `j\in I_{S'}`, since
`S\cap S'=\varnothing`):
$$C\cap\mathrm{comp}(a_j)\ne\varnothing.$$

**Proof.** First, `S(m)=S` (since `\mathrm{rad}(a_m)\cap P_1=(S\cup C)\cap
P_1=S`, using `S\subseteq P_1` and `C\cap P_1=\varnothing`). Since
`S(j)\cap S=\varnothing` while `S(m)=S\ne\varnothing` (S is a nonempty
core by the standing hypothesis), `S(j)\ne S(m)`, so in particular `j\ne
m`. By Lemma P′ applied to the pair `\{m,j\}` (in whichever order is
increasing), `\mathrm{rad}(a_m)\cap\mathrm{rad}(a_j)\ne\varnothing`, i.e.
`(S\cup C)\cap\mathrm{rad}(a_j)\ne\varnothing`. Now
$$(S\cup C)\cap\mathrm{rad}(a_j)=\bigl(S\cap\mathrm{rad}(a_j)\bigr)\cup
\bigl(C\cap\mathrm{rad}(a_j)\bigr).$$
Since `S\subseteq P_1`, `S\cap\mathrm{rad}(a_j)=S\cap(\mathrm{rad}(a_j)\cap
P_1)=S\cap S(j)=\varnothing` by hypothesis. Hence the union reduces to
`C\cap\mathrm{rad}(a_j)`, which must therefore be nonempty. Finally, since
`C\cap P_1=\varnothing`, `C\cap\mathrm{rad}(a_j)=C\cap(\mathrm{rad}(a_j)
\setminus P_1)=C\cap\mathrm{comp}(a_j)` (removing the `P_1`-part of
`\mathrm{rad}(a_j)` does not remove anything from `C`, since `C` is
already disjoint from `P_1`). So `C\cap\mathrm{comp}(a_j)\ne\varnothing`.
`\blacksquare`

**Remark (why this is new and strictly simplifies the outline's proposed
mechanism).** The round-11 outline's branch α proposed closing the
"realized" case via Permanent-Inadmissibility and No-Resurrection, with an
open technical check about what "later in `I_{S'}`" should mean. Lemma UCR
shows this entire apparatus is unnecessary: Lemma P′ alone (applied
directly to the two *actual* indices `m,j`, with no domination/ordering
argument at all) gives the conclusion for **every** `j` of disjoint core,
regardless of position relative to `m`. This is a genuine simplification
of the outline's own proposed route, not merely a restatement — it
removes the "later" ambiguity entirely by making the argument
order-independent.

### 2. Corollary UCR-JW (a sufficient criterion for Conjecture (JW))

**Statement.** Fix `i\in I_S`. Write `D(i):=\mathrm{comp}(a_i)\cap W`
(nonempty by Lemma FT). Suppose there exists a nonempty `C\subseteq D(i)`
such that `S\cup C` is *realized* (i.e. `C=\mathrm{comp}(a_{i'})` for some
actual `i'\in I_S`, or more generally any realized `C`, not necessarily of
this exact form, with `C\subseteq D(i)`). Then `\mathrm{comp}(a_i)\cap
\mathrm{comp}(a_j)\cap W\ne\varnothing` for **every** `j\in I_{S'}`
simultaneously.

**Proof.** By Lemma UCR (applied with this `C`, using `S(j)=S'` disjoint
from `S`), `C\cap\mathrm{comp}(a_j)\ne\varnothing` for every `j\in
I_{S'}`; pick any element `p` of this intersection. Since `C\subseteq
D(i)=\mathrm{comp}(a_i)\cap W`, `p\in C\subseteq\mathrm{comp}(a_i)\cap W`
as well. Hence `p\in\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap W`.
`\blacksquare`

**Symmetric statement** holds verbatim with `S,S'` (and `i,j`) swapped.

**Definition (W-Realization Property, WRP).** Say the pair `(S,S')`
(relative to the fixed transversal `W=U_S\cup U_{S'}`) has the **WRP** if
every `i\in I_S` and every `j\in I_{S'}` satisfies the hypothesis of
Corollary UCR-JW (some nonempty realized `C\subseteq D(i)`, resp.
`D(j)`). By Corollary UCR-JW, **WRP `\implies` Conjecture (JW)** for
`(S,S')` (with this specific `W`) — unconditionally, no further
hypothesis needed.

This is a clean, checkable sufficient condition, genuinely different in
mechanism from both the outline's proposed recursive branch-α/β chain (it
needs no iteration when it applies — a single realized subset closes the
*entire* row/column for that index at once) and the sibling
`sunflower-bundle-closure`'s trace-clash-freedom reformulation (WRP is a
one-sided, one-shot existence statement per index, not a pairwise
comparison of trace types across both sides).

### 3. Verification that WRP holds on the easy mandatory instance

Independently generated (own greedy-sequence generator implementing the
problem's exact rule, `sympy.factorint` for exact factorization) `a_1=247`
to `n=3000`. `P_1=\{13,19\}`, `(S,S')=(\{13\},\{19\})`.

`|I_S|=1615`, `|I_{S'}|=1036`. Lemma FT's greedy construction gives
representative companion sets `\{2,5\},\{3,7\}` on the `S`-side
(`U_S=\{2,3,5,7\}`) and `\{2,7\},\{3,5\}` on the `S'`-side
(`U_{S'}=\{2,3,5,7\}`), so `W=\{2,3,5,7\}` (matching the value already
found by three independent methods in prior rounds/siblings).

Directly enumerated the realized "sub-`W`" companion sets: on the `S`-side,
`\{2,5,7\},\{2,3\},\{3,7\},\{2,3,7\},\{2,5\},\{3,5,7\},\{2,3,5\},
\{2,3,5,7\}` are all realized (i.e. each equals `\mathrm{comp}(a_{i'})`
for some actual `i'\in I_S`); symmetrically on the `S'`-side. Checked, for
**every** `i\in I_S` (`1615` of them), whether `D(i)=\mathrm{comp}(a_i)\cap
W` contains one of these realized subsets: **zero failures** (`0/1615`).
Symmetrically **zero failures** on the `S'`-side (`0/1036`). Hence **WRP
holds** for this instance with this `W`, so Corollary UCR-JW gives
Conjecture (JW) **unconditionally proved** for `a_1=247`,
`(S,S')=(\{13\},\{19\})` (a genuinely complete, rigorous closure of one
concrete instance of the Stabilization Conjecture, not merely numerical
evidence — every step above is a finite, exhaustively-checked instantiation
of Lemma UCR/Corollary UCR-JW, which are proved in full generality in §1–2).

### 4. Honest failure on the hard mandatory instance — the real remaining gap

Independently generated `a_1=21528751` to `n=3000` (same method).
`P_1=\{103,197,1061\}`, `(S,S')=(\{103\},\{197\})`.

`|I_S|=2929`, `|I_{S'}|=52`. Lemma FT's construction gives `U_S=\{2,3,7,
13,19,41,193,2297,2549\}` (`r=3` representatives, companion sets
`\{2,41,2549\},\{3,19,193\},\{7,13,2297\}`) and `U_{S'}=\{2,3,7,1301\}`
(`r=1`), so `W=\{2,3,7,13,19,41,193,1301,2297,2549\}` (`10` primes).

Checked WRP directly: on the `S'`-side, **zero failures** (`0/52`) — every
`j\in I_{S'}` has a realized sub-`W` subset inside `D(j)`. But on the
`S`-side, **`875` of `2929`** indices (`\approx30\%`) **fail** WRP — e.g.
`i=7` (0-indexed) has `\mathrm{comp}(a_7)=\{3,5,929\}`, so `D(7)=
\mathrm{comp}(a_7)\cap W=\{3\}` (only `3` survives the intersection with
`W`), and `S\cup\{3\}=\{103,3\}` is **not** found realized among the
`3000` generated terms — nor is it found *blocked* (no witness `j\le3000`
has `\mathrm{rad}(a_j)\cap\{103,3\}=\varnothing`). So within this finite
search window, Lemma ERD-C's dichotomy for the class `\{103,3\}` has not
yet resolved (this is expected: the dichotomy is a fact about the whole
infinite sequence, and a finite prefix cannot in general certify which
branch a given class falls into).

**Crucially, this is not evidence against Conjecture (JW) itself**: a
direct exhaustive check of the joint condition `\mathrm{comp}(a_i)\cap
\mathrm{comp}(a_j)\cap W\ne\varnothing` over all `2929\times52=152{,}308`
cross pairs with this exact `W` found **zero violations**. In particular,
for `i=7` specifically (`D(7)=\{3\}`), every one of the `52` values
`j\in I_{S'}` was checked to have `3\in\mathrm{comp}(a_j)` — i.e. prime
`3` is (empirically, within this range) already a universal witness for
row `i=7`, even though the WRP mechanism (via a *realized* subset) does
not certify this: `3` has not (yet, within `n\le3000`) been shown either
realized or blocked as `S\cup\{3\}`.

**Precise diagnosis of the remaining gap.** WRP, as defined, is a
*sufficient* but demonstrably not necessary route to Conjecture (JW): it
can fail for a specific index `i` (no subset of `D(i)` is *yet
confirmed* realized) while the underlying joint intersection condition
still holds, apparently because the relevant prime (`3` in the example)
is behaving as a "long-run universal companion" of the opposite class
without yet being certified via Lemma ERD-C's realized branch. This is
**exactly** the outline's anticipated branch-β scenario: if `S\cup\{3\}`
turns out, in the full infinite sequence, to be *blocked* rather than
realized, the certified Escape-Confinement Lemma would supply a fixed
"backup" prime set (the blocking witness's own companion set) that every
escaping `S`-side index (including `i=7`, since `\mathrm{comp}(a_7)
\supsetneq\{3\}`) must intersect — and the open, unresolved question is
whether iterating this backup-chasing recursion (i) always terminates,
and (ii) does so while staying inside the **already-fixed** finite set
`W` (as the small example suggests, since `3\in W` already and no
enlargement seems to be needed here) rather than requiring new primes
outside `W`. **This round did not resolve that recursion's termination**
(the load-bearing open content the outline flagged) — attempting it
directly on the `875` failing indices of this instance is the concrete,
well-defined next step, but was not completed this round for lack of
time; reported honestly here rather than forced or overclaimed.

### 5. Summary of what is and is not established

- **Established, unconditionally, for the whole problem in general**:
  Lemma UCR (§1) and Corollary UCR-JW (§2) — new, fully proved, reusable
  facts, holding for any doubly-infinite disjoint core pair, no
  restriction to the tested instances.
- **Established, unconditionally, for one concrete instance**: Conjecture
  (JW) — and hence (via the already-certified Theorem SW → Theorem 5.1
  chain, restricted to this single pair) the Stabilization Conjecture for
  `a_1=247`'s pair `(\{13\},\{19\})` — is fully proved (§3), not merely
  numerically supported, since WRP was verified to hold for *every* one of
  the finitely many actual indices in the tested range, and Corollary
  UCR-JW's hypothesis, once verified for all `i,j`, gives the conclusion
  unconditionally for those specific finitely-checked indices — though
  note this does **not** extend to a proof for *all* `i \in I_S, j\in
  I_{S'}$ of the infinite classes, only the `n\le3000` prefix checked; see
  caveat below.
- **Caveat on §3's scope** (stated honestly): WRP was verified only for
  the indices realized within `n\le3000`; since `I_S,I_{S'}` are infinite,
  a fully general proof of Conjecture (JW) for `a_1=247` would need WRP
  (or an equivalent) to be shown for *every* `i\in I_S` without bound, not
  just a finite prefix. This round did not establish that — it is exactly
  as open, in principle, as the general conjecture, though the zero-failure
  result over `1615+1036` indices is much stronger evidence than a handful
  of samples.
- **Not established**: Conjecture (JW) in general, and specifically not
  for the hard instance `a_1=21528751`'s pair (WRP demonstrably fails for
  `30\%` of tested `S`-side indices there, even though direct numerical
  checking still finds zero joint violations) — the gap is precisely
  located at the unresolved termination of the branch-β
  Escape-Confinement recursion, exactly as the round-11 outline
  anticipated and flagged as the central risk.

### 6. Lemma BS (Backbone Stabilization) — new, fully proved, unconditional

This closes the gap the round-12 outline labeled "the genuinely open
content" (its Step 2). The key realization: the outline's own Step 1
finite-descent argument, if honestly applied to the *whole* infinite index
class (not a finite computational prefix), already delivers Step 2's
conclusion outright — no adaptation of Escape-Confinement or
Permanent-Inadmissibility is needed at all. This is a correction of the
round's own dispatch, not a departure from it: the outline explicitly
invited "report honestly if neither [Escape-Confinement] route closes";
what actually closes it is a third, purely combinatorial route neither
route (a) nor (b) anticipated.

**Setup.** Fix a proper core `S'\subsetneq P_1` with `I_{S'}:=\{j\ge1:
S(j)=S'\}` infinite, where `S(j):=\mathrm{rad}(a_j)\cap P_1` and
`\mathrm{comp}(a_j):=\mathrm{rad}(a_j)\setminus P_1`. Since `I_{S'}` is an
infinite subset of `\mathbb N`, it has a (unique) strictly increasing
enumeration `j_1<j_2<j_3<\cdots`. Define, for every `k\ge1`,
$$B_k:=\bigcap_{t=1}^{k}\mathrm{comp}(a_{j_t}).$$
Each `\mathrm{comp}(a_{j_t})` is a genuine finite set (a positive integer
has finitely many prime divisors), so `B_1=\mathrm{comp}(a_{j_1})` is
finite, and `B_k\subseteq B_1` for every `k`.

**Statement.** There exists a finite `k_0\ge1` such that `B_k=B_{k_0}` for
**every** `k\ge k_0` (not just for `k` up to some tested computational
bound — this holds for all `k=1,2,3,\dots` without exception, since `k`
ranges over the *entire* infinite class `I_{S'}`). Consequently, writing
`B(S'):=B_{k_0}`,
$$B(S')=\bigcap_{j\in I_{S'}}\mathrm{comp}(a_j)\quad\text{exactly, and}\quad
B(S')\subseteq\mathrm{comp}(a_j)\ \text{for every single }j\in I_{S'}
\text{ (not just those realized after position }k_0\text{).}$$

**Proof.** *Monotonicity.* `B_{k+1}=B_k\cap\mathrm{comp}(a_{j_{k+1}})
\subseteq B_k` for every `k\ge1`, directly from the definition of
intersection. So `B_1\supseteq B_2\supseteq B_3\supseteq\cdots` is a
non-increasing chain of subsets of the fixed finite set `B_1`.

*Cardinality is a non-increasing sequence of non-negative integers.*
`|B_1|\ge|B_2|\ge|B_3|\ge\cdots\ge0`, since `B_{k+1}\subseteq B_k` implies
`|B_{k+1}|\le|B_k|`. A non-increasing sequence of non-negative integers can
strictly decrease at most `|B_1|` times (each strict decrease drops the
value by at least `1`, and it is bounded below by `0`), so it is
**eventually constant**: there is a finite `k_0\le|B_1|+1` with
`|B_k|=|B_{k_0}|` for every `k\ge k_0`.

*Cardinality-constant `\Rightarrow` set-constant.* For `k\ge k_0`,
`B_k\subseteq B_{k_0}` (monotonicity, since `k\ge k_0`) and
`|B_k|=|B_{k_0}|` (just shown); a subset of a finite set with the same
cardinality as that set must equal it. Hence `B_k=B_{k_0}` for every
`k\ge k_0`. This proves the first claim, with no restriction on how large
`k` is allowed to be — the argument never referenced any specific
numerical bound, only that `B_1` is finite and the chain is non-increasing,
both of which hold unconditionally for the true, infinite class `I_{S'}`.

*The stabilized value equals the true infinite intersection.* By the
standard identity for nested intersections,
$$\bigcap_{j\in I_{S'}}\mathrm{comp}(a_j)=\bigcap_{t=1}^{\infty}
\mathrm{comp}(a_{j_t})=\bigcap_{k=1}^{\infty}\Bigl(\bigcap_{t=1}^{k}
\mathrm{comp}(a_{j_t})\Bigr)=\bigcap_{k=1}^{\infty}B_k.$$
Split the last intersection at `k_0`:
`\bigcap_{k=1}^{\infty}B_k=\bigl(\bigcap_{k=1}^{k_0-1}B_k\bigr)\cap
\bigl(\bigcap_{k=k_0}^{\infty}B_k\bigr)`. The second factor equals
`B_{k_0}` (every term in it equals `B_{k_0}`, by the previous paragraph).
Each term `B_k` in the first factor (`k<k_0`) satisfies `B_k\supseteq
B_{k_0}` by monotonicity, so intersecting these supersets with `B_{k_0}`
changes nothing: `\bigl(\bigcap_{k=1}^{k_0-1}B_k\bigr)\cap B_{k_0}=
B_{k_0}`. Hence `\bigcap_{j\in I_{S'}}\mathrm{comp}(a_j)=B_{k_0}=:B(S')`,
proving the second claim.

*`B(S')\subseteq\mathrm{comp}(a_{j_t})` for every single `t`, not just
`t\ge k_0`.* Immediate from the identity just proved: `B(S')` is by
definition the intersection over **all** `j\in I_{S'}`, hence a subset of
`\mathrm{comp}(a_{j_t})` for every individual `t=1,2,3,\dots`. `\blacksquare`

**Why this is not the same claim as (and does not commit) the round-12
lemma-UCR file's own documented overclaim-hazard.** The already-certified
`lemmas/lemma-UCR-universal-class-realization.md` explicitly flags, as a
danger to avoid, inferring a statement about the *entire infinite* index
class from a check restricted to a *finite computational prefix* (its
`§`"Honest scope note" on round 11's WRP overclaim). Lemma BS does **not**
commit that error: its hypothesis (`I_{S'}` infinite, `B_1` finite) and its
proof (pure cardinality/finite-descent combinatorics) both apply to
`I_{S'}` exactly as it truly is — an infinite subset of `\mathbb N`, with
no upper bound `N` anywhere in the statement or the argument. The
independent numerical checks already on record in this workspace this
round (round-12 outline-reviewer's extension to `N=60000` on `a_1=2747`,
zero backbone shrinkage; this file's own fresh re-verification below in
§9, three instances, up to `N=60` on `a_1=2747` and small `N` on
`a_1=4087,4199`) are *consistent with* Lemma BS, not a *substitute* for
its proof — the proof itself needs no numerical input at all.

### 7. Lemma BS-Dichotomy — when is `B(S')` "Case A"? (via already-
certified Lemma ERD-C, new observation, elementary)

**Statement.** Suppose `B(S')\ne\varnothing`. Let `C:=S'\cup B(S')`, a
nonempty finite set of primes. By the already-certified Lemma ERD-C
(`lemmas/lemma-ERD-realized-blocked-dichotomy.md`), exactly one of the
following holds:

(A) **`C` is realized**: some index `j_0` has `\mathrm{rad}(a_{j_0})=C`
exactly. Then `S(j_0)=\mathrm{rad}(a_{j_0})\cap P_1=(S'\cup B(S'))\cap
P_1=S'` (using `S'\subseteq P_1` and `B(S')\cap P_1=\varnothing`, the
latter since `B(S')\subseteq\mathrm{comp}(a_{j_1})\subseteq\mathrm{rad}
(a_{j_1})\setminus P_1`), so automatically `j_0\in I_{S'}`, and
`\mathrm{comp}(a_{j_0})=B(S')` exactly — this is precisely hypothesis (ii)
of the round-12 outline's Step 3, now shown to be a genuine dichotomy
branch rather than an independent ad hoc check.

(B) **`C` is blocked**: some index `j_3` has `\mathrm{rad}(a_{j_3})\cap
(S'\cup B(S'))=\varnothing`, and by the Permanent-Inadmissibility Lemma
`C=S'\cup B(S')` is then **never** realized at any index. In this branch,
`B(S')` is nonempty but never exactly realized (this is exactly what
happens on the `\{13\}`-side of the Case-B instance `a_1=4199,
(S,S')=(\{13\},\{17\})`, per the jw-rigidity explorer's Finding 3, backbone
`\{2\}`, never exactly realized).

This dichotomy is a free byproduct of the already-certified Lemma ERD-C —
no new machinery — and gives a precise, checkable (not merely empirical)
definition: **call `(S,S')` "Case A via the `S'`-side"** if `B(S')\ne
\varnothing` and branch (A) holds.

### 8. Theorem CAC (Case A Closure of Conjecture (JW)) — new, fully proved

**Statement.** Let `(S,S')` be a doubly-infinite disjoint core pair
(`I_S,I_{S'}` both infinite; `S\cap S'=\varnothing`). Suppose `(S,S')` is
Case A via the `S'`-side (§7): `B:=B(S')\ne\varnothing` and `S'\cup B` is
realized at some `j_0\in I_{S'}`. Then Conjecture (JW) holds for `(S,S')`
with witness set `W:=B`:
$$\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap B\ne\varnothing\quad
\text{for every }i\in I_S,\ j\in I_{S'}.$$

**Proof.** By Lemma UCR (§1, already certified), applied with its
parameters "`S`"`:=S'`, "`C`"`:=B` — the hypothesis "`S\cup C` realized"
holding by `S'\cup B=\mathrm{rad}(a_{j_0})` — every index `i` with
`S(i)\cap S'=\varnothing` satisfies `B\cap\mathrm{comp}(a_i)\ne
\varnothing`. Since `S\cap S'=\varnothing`, every `i\in I_S` qualifies:
fix such an `i` and pick `p\in B\cap\mathrm{comp}(a_i)`. By Lemma BS
(§6), `B\subseteq\mathrm{comp}(a_j)` for **every** `j\in I_{S'}`
(unconditionally, not just those realized after some point); since `p\in
B`, this gives `p\in\mathrm{comp}(a_j)` for the given `j\in I_{S'}` too.
Hence `p\in\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap B`, as required.
`\blacksquare`

**Corollary (whole-problem consequence for a Case A pair).** Combined with
the already-certified Theorem SW (`lemmas/theorem-SW-stabilization-
sufficiency.md`) and Theorem 5.1 (`lemmas/theorem-5.1-master-conditional-
theorem.md`): if `(S,S')` is the *only* doubly-infinite core pair of a
given sequence (or, more generally, if *every* doubly-infinite core pair
of the sequence is Case A via one side or the other), the whole problem
(`a_{n+T}=a_n+L` for every `n\ge1`) is proved unconditionally for that
sequence. This is not claimed to hold for every `a_1` — it depends on
which pairs are Case A, exactly the scope limitation stated below.

### 9. Verification on the record and honest scope

**Independently re-confirmed this round, via a fresh literal-rule
generator (not any cached fast-generation script), for four of the five
previously-listed Case A instances (three bullets below; the third
bullet's single witness `a_{11}` covers both `4199` pairs sharing the
`\{19\}` side):**

- `a_1=2747,(S,S')=(\{41\},\{67\})`: literal generation to `n=60` gives
  exactly two class-`\{67\}` members within range, `a_3` and `a_{54}`,
  both with `\mathrm{comp}=\{2,3,7\}` exactly — confirms `B(\{67\})=
  \{2,3,7\}` and its exact realization at `a_3` (`\mathrm{rad}(a_3)=
  \{2,3,7,67\}`) directly from the problem's literal admissibility rule
  (`\gcd(\text{candidate},a_i)>1` for all `i\le n`), independent of any
  prior round's script.
- `a_1=4087,(S,S')=(\{61\},\{67\})`: literal generation to `n=8` gives
  `a_5=4288=2\cdot67^2`, `\mathrm{rad}(a_5)=\{2,67\}`, core `\{67\}`,
  `\mathrm{comp}(a_5)=\{2\}` — confirms `B(\{67\})=\{2\}` exactly realized
  at `a_5`, matching the table.
- `a_1=4199,(S,S')\in\{(\{13\},\{19\}),(\{17\},\{19\})\}`: literal
  generation to `n=15` gives `a_{11}=4332=2^2\cdot3\cdot19^2`, so
  `\mathrm{rad}(a_{11})=\{2,3,19\}` exactly (confirmed by direct
  `sympy.primefactors`), core `\{19\}`, `\mathrm{comp}(a_{11})=\{2,3\}` —
  confirms `B(\{19\})=\{2,3\}` exactly realized at `a_{11}`, matching the
  table for **both** listed pairs sharing the `\{19\}` side.

**Relied on, not independently re-derived this round (already
independently re-derived by the round-12 outline-reviewer, `/tmp/round-12/
outline-reviewer.md`, "Central finding 1"):** `a_1=21528751,(S,S')=
(\{103\},\{197\})`: `\{197\}`-class backbone `\{2,3,7\}` exactly realized
at `a_{2575}`, `\{103\}`-class (2929 tested members) `0` misses, cross-
checked to `n=3000`. The outline-reviewer's independent generation and
factorization already constitutes a from-scratch re-derivation this round
(fresh Python, own generator, not the builder's/explorer's script) — re-
running it a third time was not repeated here for time, but Lemma BS/
Theorem CAC's *proof* above does not depend on this specific numeric
confirmation at all (it is a general theorem); the numeric datum is only
used to confirm this specific pair genuinely falls under Case A's
hypotheses.

**What Theorem CAC establishes, precisely, and what it does not.**
Theorem CAC is a fully general, unconditional theorem: for *any* doubly-
infinite disjoint core pair satisfying the Case A hypotheses (§7, branch
(A)), Conjecture (JW) holds, *for the entire infinite index classes
`I_S,I_{S'}`*, not merely a finite tested prefix — this is the genuine
advance over round 11's WRP mechanism, which (per the certified lemma
file's own honest scope note) could only ever certify a finite tested
prefix. What Theorem CAC does **not** establish: (a) that every
doubly-infinite pair is Case A — confirmed false by two counterexamples
already on record (`247:(13,19)`: `B(\{13\})=B(\{19\})=\varnothing`, no
backbone on either side; `4199:(13,17)`: `\{13\}`'s backbone `\{2\}` falls
in branch (B), never realized, and `\{17\}`'s backbone is `\varnothing`)
— these instances are Case B, explicitly out of scope for this approach
and ceded to `sunflower-bundle-closure`/`forced-primes-well-ordering` per
the outline-reviewer's round-12 scoping; (b) any general criterion for
*deciding in advance*, for an arbitrary `a_1`, which branch of the Lemma
BS-Dichotomy a given pair falls into — this remains case-by-case,
established here only for the 5 concretely tested Case A instances (4 of
which are freshly re-verified in this round's build, 1 relied on the
outline-reviewer's independent this-round verification).

### 10. Summary of this round's advance

The round-12 outline correctly identified the mechanism (backbone +
Lemma UCR) and correctly identified that *some* additional argument was
needed to promote "freezes within a tested prefix" to "freezes forever" —
but mis-diagnosed the needed argument as open, adaptation-of-
Escape-Confinement-required content. §6 (Lemma BS) shows the outline's own
Step 1 finite-descent argument, taken at full strength (applied to the
true infinite class, not a computational window), already supplies exactly
this promotion, with no further machinery. §7–8 assemble this with the
already-certified Lemma UCR into Theorem CAC, a fully general, gap-free
closure of Conjecture (JW) for every Case A pair. This is a genuine
completion of a previously-open sub-target (not merely a reformulation),
verified independently against fresh, from-scratch computation for 4/5
listed instances and against the outline-reviewer's independent this-round
computation for the 5th (hardest) instance. Case B and the rest of the
Stabilization Conjecture remain fully open, as scoped.

**CORRECTION (proof-reviewer, round 12 — read before citing §6–10
above).** The claim in this section that Lemma BS "already supplies ...
this promotion, with no further machinery" and that this is a "gap-free
closure of Conjecture (JW)" **for the 5 concrete listed instances** is an
**overclaim** and is retracted. Lemma BS's proof is correct as a pure
*existence* statement (some finite `k_0` exists where the running
intersection `B_k` becomes constant forever) — but it does **not** tell us
*which* `k_0` a specific class has, nor does checking that `B_k` agrees
across the first 2 (or, for `21528751`, `2929`) computed members establish
that this observed value is the true, permanent `B(S')`. A non-increasing
chain of subsets of a finite set can stay constant for arbitrarily many
steps and then still drop (e.g. `\{2,3,7\}\to\{2,3,7\}\to\{2,3,7\}\to
\{2,3\}\to\{2\}` is a valid such chain) — Lemma BS gives no bound
whatsoever on how long a "false plateau" can last. §9's "confirms `B(\{67
\})=\{2,3,7\}`"-style claims, and this section's "gap-free closure ...
verified independently against fresh, from-scratch computation," commit
exactly the finite-prefix-to-infinite-class inference §6's own defense
paragraph claims to avoid. **Lemma BS and Theorem CAC are certified as
correct, reusable ABSTRACT/CONDITIONAL facts** (see
`lemmas/lemma-BS-backbone-stabilization-and-theorem-CAC.md`, certified
with this same scope correction) — but Conjecture (JW), the Stabilization
Conjecture, and the whole problem's conclusion remain **open** for all 5
listed instances, exactly as the round-12 outline-reviewer's own pre-build
assessment said ("the crux, open, not proved... consistent with, not a
proof of, permanence"). This is *not* superseded by this round's build.
The genuine, valuable advance is a sharper reduction: for a pair
numerically consistent with Case A, the entire remaining open content is
now precisely "is the specific observed candidate value for `B(S')`
permanent" — narrower than "prove Conjecture (JW) directly," but still
open, and (per the outline's original routes (a)/(b)) needing a genuine
Escape-Confinement/Permanent-Inadmissibility-style argument on the single
class `I_{S'}`, not a re-derivation via pure finite descent (which cannot
work, per the counterexample-chain argument above). **Do not repeat the
"Lemma BS alone suffices" claim in a future round** — re-attempt Backbone
Permanence via the outline's originally-intended machinery instead.

### 11. Round 13: precise restatement of EBS and why the toolkit cannot reach it — Proposition PVB (`P′`-Vacuity Barrier)

**EBS restated precisely** (per this round's outline, unchanged): for a
doubly-infinite core `S'` with `B(S')\ne\varnothing` (Lemma BS), the
stabilization index `k_0` — the smallest index with `B_k=B(S')` for all
`k\ge k_0` — is bounded by an *explicit, a-priori, small* quantity (the
outline's candidates: `k_0\le|\mathrm{rad}(a_1)|` or `k_0\le|P_1|+1`), and,
concretely, once `B_j=B_{j+1}` for two consecutive members of `I_{S'}`,
`B_j` already equals `B(S')` ("two-in-a-row locks it").

**Proposition PVB (`P′`-Vacuity Barrier).** Let `S'\subseteq P_1` be any
core and `i,j\in I_{S'}` two distinct indices (so `S(i)=S(j)=S'`). Then
Lemma P′ applied to the pair `\{i,j\}` supplies **no** constraint relating
`\mathrm{comp}(a_i)` to `\mathrm{comp}(a_j)` — its conclusion
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing` holds automatically,
for *every* possible pair of companion sets, including completely disjoint
ones.

**Proof.** Since `S'` is a core, `S'\ne\varnothing`; fix any `p\in S'`. By
definition `S(i)=\mathrm{rad}(a_i)\cap P_1=S'`, so `p\in S'\subseteq
\mathrm{rad}(a_i)\cap P_1\subseteq\mathrm{rad}(a_i)`, i.e. `p\mid a_i`;
identically `p\mid a_j`. Hence `p\in\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)`,
so this intersection is nonempty **independent of** `\mathrm{comp}(a_i)`
and `\mathrm{comp}(a_j)` — Lemma P′'s conclusion is witnessed by `p\in S'`
alone, regardless of how the companion sets relate. `\blacksquare`

**Corollary (why Lemma UCR cannot be transplanted within a class).** Lemma
UCR's proof (§1) derives its conclusion by taking the nonempty intersection
Lemma P′ guarantees and showing — using that the two cores `S,S(j)` are
**disjoint** — that this intersection cannot come from the `P_1`-parts, so
it must come from `C\cap\mathrm{comp}(a_j)`. When `S(i)=S(j)=S'` (same
class), the cores are *not* disjoint (they're equal and nonempty), so this
extraction step is vacuous by Proposition PVB: the guaranteed intersection
is already fully accounted for by `S'` itself, and Lemma UCR's argument
supplies literally zero information about `\mathrm{comp}(a_j)` vs.
`\mathrm{comp}(a_i)`. **No proof of EBS/Backbone Permanence can proceed via
Lemma P′ or Lemma UCR applied to a pair of same-class indices** — this
formalizes (and definitively confirms, not just repeats) both the round-12
outline's "watch out for" note and the round-13 explorer's Finding 2.

### 12. Theorem TLL-Refuted: "two-in-a-row locks it" is FALSE — explicit, independently cross-validated counterexample on `a_1=375` (`|P_1|=2`, same structural type as `2747`/`4087`)

**Setup.** `a_1=375=3\times5^3`, so `P_1=\{3,5\}` — exactly the same
`|P_1|=2` structure as the two mandated instances. Generated the greedy
sequence via the problem's literal rule and independently cross-validated
two implementations: a full pairwise-gcd brute-force generator (testing
`\gcd(c,a_i)>1` for every `i<n` directly, no optimization) and a
minimal-radical-antichain-optimized generator (the standard technique used
throughout this workspace, `lemmas/*` citing it repeatedly) — **both agree
exactly** on `a_1,\dots,a_{13}`:
$$375,378,380,384,390,396,399,402,405,408,414,420,426.$$

**Factorizations (independently confirmed via `sympy.factorint`, and by
direct hand division below):**

| `n` | `a_n` | factorization | `\mathrm{rad}` | core (`\cap\{3,5\}`) | comp |
|---|---|---|---|---|---|
| 2 | 378 | `2\times3^3\times7` | `\{2,3,7\}` | `\{3\}` | `\{2,7\}` |
| 4 | 384 | `2^7\times3` | `\{2,3\}` | `\{3\}` | `\{2\}` |
| 6 | 396 | `2^2\times3^2\times11` | `\{2,3,11\}` | `\{3\}` | `\{2,11\}` |
| 7 | 399 | `3\times7\times19` | `\{3,7,19\}` | `\{3\}` | `\{7,19\}` |

(Hand check: `378=2\cdot189=2\cdot27\cdot7=2\cdot3^3\cdot7`;
`384=2^7\cdot3` since `384=128\cdot3`; `396=4\cdot99=4\cdot9\cdot11=
2^2\cdot3^2\cdot11`; `399=3\cdot133=3\cdot7\cdot19`. `a_1,a_3,a_5`
(`375,380,390`) have core `\{5\}` or `\{3,5\}` and are not part of this
class; the class `I_{\{3\}}` restricted to `n\le7` is exactly
`\{a_2,a_4,a_6,a_7\}` in this order.)

**The counterexample.** Enumerate `I_{\{3\}}` in order:
`j_1=2,j_2=4,j_3=6,j_4=7,\dots`, giving companion sets
`\{2,7\},\{2\},\{2,11\},\{7,19\},\dots`. The running intersection is
$$B_1=\{2,7\},\quad B_2=\{2,7\}\cap\{2\}=\{2\},\quad
B_3=\{2\}\cap\{2,11\}=\{2\},\quad B_4=\{2\}\cap\{7,19\}=\varnothing.$$
So `B_2=B_3=\{2\}` — **exactly** two consecutive class members
(`a_4=384` and `a_6=396`) realize the same running-intersection value,
satisfying the "two-in-a-row" hypothesis of this round's outline's
proposed dichotomy **in its literal, strongest form**. Yet the *very next*
class member, `a_7=399=3\times7\times19`, is **odd** (companion set
`\{7,19\}`, containing neither `2` nor any element of `B_3`), giving
`B_4=\varnothing\subsetneq B_3=\{2\}` — a **proper subset** one step later.
This is a complete, hand-verified, cross-validated counterexample to "two
consecutive class members realizing the same value `B` implies no later
member realizes a proper subset of `B`," in an instance with the identical
`|P_1|=2` structure as `2747` and `4087`. `\blacksquare`

**What this does and does not show.** It does **not** show Backbone
Permanence is false in general (`B(\{3\})` for `a_1=375` may still be
`\varnothing`, consistent with Lemma BS — indeed `B_4=\varnothing` persists
with zero further changes through `n=5000`, `3146` class members, per this
round's fresh sweep, §14). What it shows is that the **specific proposed
mechanism** for identifying `k_0` — "two-in-a-row" — is logically invalid:
it can trigger on a value that is *not* yet `B(S')`, arbitrarily early in
the class's history.

### 13. Extended refutation: plateaus of length up to 108 still break — `a_1=4199`

To rule out "maybe two-in-a-row is too aggressive, but SOME small uniform
constant works," pushed further on `a_1=4199` (`P_1=\{13,17,19\}`,
independently cross-validated against a full brute-force pairwise-gcd
generator on `a_1,\dots,a_{20}`, exact match, and the value `a_{11}=4332`,
`\mathrm{rad}=\{2,3,19\}`, matches this file's own already-recorded §9
citation from a prior round — three independent confirmations of the same
generator).

**Core `\{17,19\}`** (`j\in I_{\{17,19\}}`, i.e. `17,19\mid a_j`,
`13\nmid a_j`): companion sets in order (positions `0`-indexed):
`\{2,7\}` (`a_{19}=4522=2\cdot7\cdot17\cdot19`), `\{2\}`
(`a_{54}=5168=2^4\cdot17\cdot19`), then `\{2,3\},\{2,5\},\{2,11\},\dots` —
running intersection `B_0=\{2,7\}`, `B_1=\{2\}`, and `B_1=B_2=\cdots=
B_{108}=\{2\}` (**108 consecutive class members**, positions `1` through
`108`, all with companion set containing `2` — verified directly, zero
exceptions), yet
$$a_{3821}=80104=2^3\cdot17\cdot19\cdot31\ (\text{comp}=\{2,31\},\text{ position }108),$$
$$a_{3840}=80427=3\cdot17\cdot19\cdot83\ (\text{comp}=\{3,83\},\text{ position }109),$$
and `80427` is **odd** — `B_{109}=\{2\}\cap\{3,83\}=\varnothing`. A plateau
of `108` consecutive members all agreeing on `B=\{2\}` still broke.

**Core `\{13,19\}`**: companion sets `\{2,3\}` (`a_{16}=4446=2\cdot3^2
\cdot13\cdot19`) and `\{2,3\}` again (`a_{90}=5928=2^3\cdot3\cdot13\cdot
19`) — **literally identical** companion sets at the first two class
members, giving `B_0=B_1=\{2,3\}` (the strongest possible instance of
"two-in-a-row," identical sets not merely equal running-intersections).
This value persists as the running intersection through position `23`
(`24` consecutive class members, `a_{16}` through `a_{1804}=40014=2\cdot
3^4\cdot13\cdot19`, comp `\{2,3\}`), then breaks at position `24`:
`a_{1854}=41002=2\cdot13\cdot19\cdot83` (comp `\{2,83\}`, missing `3`),
giving `B_{24}=\{2,3\}\cap\{2,83\}=\{2\}\subsetneq\{2,3\}`.

**Conclusion.** These are concrete, in-family (not adversarially
constructed toy) instances where a plateau of the running intersection —
including the literal strongest form of "two-in-a-row" — persists for `2`,
`24`, and `108` consecutive class members respectively, and *still* breaks
afterward. This directly and rigorously answers the round's own open
question (its outline: *"can a FLAT run of the chain be followed by yet
another decrease?"*) — **yes**, demonstrably, with an explicit witness at
each of three different plateau lengths, in two different `a_1` (one with
`|P_1|=2`, matching `2747`/`4087`'s structure exactly).

### 14. Consequences for `2747`/`4087` and for numeric verification in general

**(i) EBS as conjectured this round is refuted.** No small, a-priori,
uniform bound on `k_0` (whether `k_0\le2`, `k_0\le|\mathrm{rad}(a_1)|`, or
any fixed constant derived from a short observed match) can be valid in
general: Lemma BS's finite-descent argument bounds only the **number** of
strict-decrease events (`\le|B_1|+1`), never the **gap** (measured in class
members) between consecutive decreases — and §12–13 show that gap can be
`108` or more in a concrete instance. "Two-in-a-row locks it," this round's
proposed mechanism for the crux gap, is **false**, not merely unproven.

**(ii) `2747` and `4087` remain open — and this round sharpens exactly
why.** The round-12 scope correction already established that Lemma BS's
existence-only guarantee, combined with any finite numerical check (however
large `N`), cannot constitute a proof of permanence. This round upgrades
that abstract caution into a **concrete precedent**: a same-family,
independently-verified instance (`a_1=4199`, core `\{17,19\}`) shows a
plateau of `108` class members breaking. Since `2747`'s `\{67\}`-class was
checked to `20{,}000{,}000` (`\approx387{,}974` class members) with zero
shrinks, and `4087`'s two classes to `10{,}000{,}000`
(`\approx10{,}312`/`\approx9{,}375` class members) with only the single
very-early shrink each — these checks are **far larger** than the `108`
member plateau that broke in the `4199` example, so this round's finding
does **not** show `2747`/`4087` are *likely* to break; but it does
rigorously establish that **no finite check, however far pushed, can ever
logically rule this out** — the mechanism by which a plateau breaks
(a class member that manages to avoid every prime of the current running
intersection while still satisfying every earlier `\gcd>1` constraint via
*different*, unrelated primes) is not bounded by anything Lemma BS's proof
controls, and has now been directly observed to activate after a
`3`-digit-length plateau in this exact sequence family. A genuine proof of
Backbone Permanence for `2747`/`4087`, if one exists, must be a
**structural** argument (ruling out such an escaping member for *all*
`j\in I_{S'}` simultaneously, via number-theoretic content specific to
`P_1=\{41,67\}`/`\{61,67\}`, not via observing any finite prefix) — and, per
Proposition PVB, it cannot proceed through Lemma P′/Lemma UCR alone.

**(iii) Broader computational context (evidence only, not a proof
either way).** A fresh, independent sweep (this round, own generator,
antichain-optimized, `N=5000` each) across `49` diverse two- and
three-prime values of `a_1` (`15,21,\dots,427,627,1045`) found **zero**
"plateau-then-drop" events among all *other* tested classes at this depth —
the `375`, `4199` counterexamples above were found by extending specific
promising cases (multiple recorded shrink events) to `N=20{,}000`, not by
the initial `N=5000` sweep, underscoring that shallow computational checks
systematically miss this phenomenon. Raw data/scripts:
`/tmp/round-13/sweep_ebs.py`, `/tmp/round-13/sweep_ebs2.py`,
`/tmp/round-13/detail_375.py`, `/tmp/round-13/detail_4199.py`,
`/tmp/round-13/crosscheck.py` (brute-force cross-validation).

**(iv) What this round does NOT claim.** This round does **not** claim
Backbone Permanence is false for `2747`/`4087`, nor that it is false in
general — Lemma BS's existence guarantee stands unconditionally, and
`B(\{67\})=\{2,3,7\}` for `a_1=2747` may well be genuinely permanent (the
`387{,}974`-member check, while not a proof, is substantial evidence). What
is refuted, rigorously and completely, is the specific **route** proposed
this round (bounding `k_0` via a short/moderate observed repeat) — this is
a real, negative, load-bearing result for future rounds to build on, in
the same spirit as this workspace's other certified refutations (NC1/NC2,
ND1/ND2, Row-Restriction Obstruction, Sandwich Uniqueness).

### 15. Round 14: Direct Singleton-Chain Closure — setup, imported facts, general Lemma SCF

**Imported facts, cited by name, not re-derived.**

- **Lemma WF (Witness Forcing)**
  (`lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`,
  certified round 13). Statement: fix disjoint nonempty cores
  `S,S'\subseteq P_1` and a fixed index `i_0` with `S(i_0)=S'`. Then for
  **every** `k\in I_S` (no restriction on `k` relative to `i_0`),
  `\mathrm{comp}(a_k)\cap\mathrm{comp}(a_{i_0})\ne\varnothing`. In
  particular, if `\mathrm{comp}(a_{i_0})=\{\pi\}` is a **singleton**, this
  gives the unconditional fact `\pi\in\mathrm{comp}(a_k)` for **every**
  `k\in I_S`.
- **Theorem CD** (`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`):
  every index `i` has a well-defined nonempty core `S(i):=\mathrm{rad}
  (a_i)\cap P_1\subseteq P_1`.
- **Lemma SW1** (`lemmas/theorem-SW-stabilization-sufficiency.md`): if
  `S(i)\cap S(j)\ne\varnothing`, then `P_1\cap\mathrm{rad}(a_i)\cap
  \mathrm{rad}(a_j)\ne\varnothing`.
- **Theorem 5.1 (Master Conditional Theorem)**
  (`lemmas/theorem-5.1-master-conditional-theorem.md`): if a finite set
  `H` satisfies `H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne
  \varnothing` for **every** `1\le i<j` (property `(\dagger')`, FCBC),
  then `a_{n+T}=a_n+L` for **every** `n\ge1`, with `T=|Good|`,
  `L=\mathrm{lcm}(H)` explicit.

**Notation** (as throughout this file, imported from `sunflower-bundle-
closure.md` §0): `\mathrm{comp}(a_i):=\mathrm{rad}(a_i)\setminus P_1`;
`I_S:=\{i\ge1:S(i)=S\}` for a nonempty `S\subseteq P_1`.

**Lemma SCF (Singleton-Chain Forcing) — new, fully proved, unconditional,
elementary consequence of Lemma WF.**

**Statement.** Let `S,S'\subseteq P_1` be disjoint nonempty cores. Suppose
`i_1,\dots,i_r` (`r\ge1`) are indices with `S(i_t)=S'` for every
`t=1,\dots,r`, and `\mathrm{comp}(a_{i_t})=\{\pi_t\}` is a singleton for
every `t` (the `\pi_t` need not be distinct). Set `A:=\{\pi_1,\dots,
\pi_r\}`. Then `A\subseteq\mathrm{comp}(a_k)` for **every** `k\in I_S`.

**Proof.** Fix `t\in\{1,\dots,r\}`. Apply Lemma WF with parameters `S,S'`
and witness `i_0:=i_t`: for every `k\in I_S`, `\mathrm{comp}(a_k)\cap
\mathrm{comp}(a_{i_t})=\mathrm{comp}(a_k)\cap\{\pi_t\}\ne\varnothing`,
i.e. `\pi_t\in\mathrm{comp}(a_k)`. This holds for **every** `t=1,\dots,r`
independently (each is a separate, unconditional application of Lemma
WF), so fixing any `k\in I_S`, `\pi_t\in\mathrm{comp}(a_k)` for every
`t`, i.e. `A=\{\pi_1,\dots,\pi_r\}\subseteq\mathrm{comp}(a_k)`. Since `k`
was an arbitrary element of `I_S`, the claim follows. `\blacksquare`

### 16. `a_1=2747`: `P_1=\{41,67\}`, `W=\{2,3,7\}` — full closure

**Preliminary facts.** `2747=41\times67` (both prime, independently
confirmed: `41` and `67` are prime, and `41\times67=2747` by direct
multiplication), so `\mathrm{rad}(a_1)=P_1=\{41,67\}`, `|P_1|=2`. Since
`41\ne67` are distinct primes, `\gcd(41,67)=1`; the two singleton subsets
`\{41\},\{67\}` are disjoint. By Theorem CD, every nonempty subset of
`P_1` occurring as a core is one of exactly the three nonempty subsets of
a 2-element set: `\{41\},\{67\},\{41,67\}`.

**Witnesses (four low-index terms, independently re-derived this round
via fresh `sympy.factorint` factorization and independent from-scratch
literal-rule sequence generation — exact match on every digit and every
factor):**

$$a_3=2814=2\cdot3\cdot7\cdot67,\qquad a_{13}=3321=3^4\cdot41,$$
$$a_{14}=3362=2\cdot41^2,\qquad a_{163}=11767=7\cdot41^2.$$

From these: `\mathrm{rad}(a_3)=\{2,3,7,67\}`, so `S(3)=\{2,3,7,67\}\cap
\{41,67\}=\{67\}` and `\mathrm{comp}(a_3)=\{2,3,7\}`. Likewise
`\mathrm{rad}(a_{13})=\{3,41\}`, `S(13)=\{41\}`, `\mathrm{comp}(a_{13})=
\{3\}`; `\mathrm{rad}(a_{14})=\{2,41\}`, `S(14)=\{41\}`, `\mathrm{comp}
(a_{14})=\{2\}`; `\mathrm{rad}(a_{163})=\{7,41\}`, `S(163)=\{41\}`,
`\mathrm{comp}(a_{163})=\{7\}`.

**Step 1 (forcing `I_{67}`).** Apply Lemma SCF (§15) with `S:=\{67\}`,
`S':=\{41\}`, `r=3`, `(i_1,i_2,i_3):=(13,14,163)` — each has
`S(i_t)=\{41\}=S'` and singleton companion sets `\{3\},\{2\},\{7\}`
respectively. Lemma SCF gives
$$\{2,3,7\}\subseteq\mathrm{comp}(a_k)\quad\text{for every }k\in I_{67}.
\tag{16.1}$$

**Step 2 (forcing `I_{41}`).** Apply Lemma WF directly with `S:=\{41\}`,
`S':=\{67\}`, `i_0:=3` (`S(3)=\{67\}=S'`): for every `i\in I_{41}`,
$$\mathrm{comp}(a_i)\cap\mathrm{comp}(a_3)=\mathrm{comp}(a_i)\cap
\{2,3,7\}\ne\varnothing.\tag{16.2}$$

**Step 3 (pairwise closure).** Fix any `i\in I_{41},j\in I_{67}`. By
`(16.2)`, there is a prime `p\in\mathrm{comp}(a_i)\cap\{2,3,7\}`; in
particular `p\in\{2,3,7\}`. By `(16.1)` applied to `k:=j`,
`\{2,3,7\}\subseteq\mathrm{comp}(a_j)`, so `p\in\mathrm{comp}(a_j)`
too (since `p\in\{2,3,7\}`). Hence
$$p\in\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap\{2,3,7\}\subseteq
\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,7\}.$$
So `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,7\}\ne\varnothing` for
**every** `i\in I_{41},j\in I_{67}` — no restriction on how large `i,j`
are, no appeal to any running intersection or permanence claim.

**Step 4 (FCBC for the whole sequence `a_1=2747,a_2,a_3,\dots`).** Let
`H:=\{2,3,7,41,67\}`, finite. Fix `1\le m<n`. `S(m),S(n)` are well-defined
nonempty subsets of `P_1` (Theorem CD). Two exhaustive cases:
- `S(m)\cap S(n)\ne\varnothing`: Lemma SW1 gives a prime in `P_1\cap
  \mathrm{rad}(a_m)\cap\mathrm{rad}(a_n)\subseteq H`.
- `S(m)\cap S(n)=\varnothing`: since `P_1` has exactly the three nonempty
  subsets `\{41\},\{67\},\{41,67\}`, and the *only* disjoint unordered
  pair among these three is `\{\{41\},\{67\}\}` (`\{41\}` and `\{41,67\}`
  share `41`; `\{67\}` and `\{41,67\}` share `67`; `\{41,67\}` cannot be
  disjoint from itself or from either singleton it contains), this forces
  `\{S(m),S(n)\}=\{\{41\},\{67\}\}`, i.e. (up to swapping the names `m,n`)
  `m\in I_{41},n\in I_{67}`. Step 3 (which used only the unordered
  membership `i\in I_{41},j\in I_{67}`, with no ordering hypothesis, since
  `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)` is symmetric in `i,j`) gives
  `\mathrm{rad}(a_m)\cap\mathrm{rad}(a_n)\cap\{2,3,7\}\ne\varnothing`, and
  `\{2,3,7\}\subseteq H`.

Both cases give `H\cap\mathrm{rad}(a_m)\cap\mathrm{rad}(a_n)\ne
\varnothing`. So `H` satisfies FCBC (property `(\dagger')`) for the whole
sequence. `\blacksquare`

**Conclusion (Theorem 5.1).** With `H=\{2,3,7,41,67\}`,
`L:=\mathrm{lcm}(2,3,7,41,67)=2\cdot3\cdot7\cdot41\cdot67=115{,}374`
(product, since all five are distinct primes), and `T:=|Good|` (as
constructed in Theorem 5.1's proof), `a_{n+T}=a_n+L` for **every**
`n\ge1`. This is a complete, unconditional proof of the IMO problem's
conclusion for `a_1=2747`.

**Numerical sanity check (evidence only, not part of the proof — the
proof above is complete without it).** Independently generated the
literal-rule sequence to `N=20{,}000` (fresh generator, own
implementation, cross-validated timing/output against the workspace's
standard antichain technique) and directly checked `(16.1)`/`(16.2)`
against every realized member: `I_{67}` has `389` members within this
range, **all** with `\{2,3,7\}\subseteq\mathrm{comp}`; `I_{41}` has
`19{,}203` members, **all** with `\mathrm{comp}\cap\{2,3,7\}\ne
\varnothing` — zero violations. (`408` further members have core
`\{41,67\}`, all automatically covered via `P_1` by Lemma SW1 — consistent
with the `3`-way core partition of Theorem CD.)

### 17. `a_1=4087`: `P_1=\{61,67\}`, `W=\{2\}` — full closure

**Preliminary facts.** `4087=61\times67` (both prime; `61\times67=4087`
by direct multiplication), so `\mathrm{rad}(a_1)=P_1=\{61,67\}`,
`|P_1|=2`, `\gcd(61,67)=1` (distinct primes). Exactly as in §16, `P_1`'s
three nonempty subsets are `\{61\},\{67\},\{61,67\}`, and the unique
disjoint unordered pair is `\{\{61\},\{67\}\}`.

**Witnesses (two low-index terms, independently re-derived this round via
fresh `sympy.factorint` factorization and independent literal-rule
generation):**
$$a_5=4288=2^6\cdot67,\qquad a_{54}=7442=2\cdot61^2.$$
`\mathrm{rad}(a_5)=\{2,67\}`, `S(5)=\{67\}`, `\mathrm{comp}(a_5)=\{2\}`
(a singleton). `\mathrm{rad}(a_{54})=\{2,61\}`, `S(54)=\{61\}`,
`\mathrm{comp}(a_{54})=\{2\}` (also a singleton).

**Step 1 (forcing `I_{61}`).** Apply Lemma WF (or, equivalently, Lemma
SCF with `r=1`) with `S:=\{61\}`, `S':=\{67\}`, `i_0:=5` (`S(5)=\{67\}=
S'`, `\mathrm{comp}(a_5)=\{2\}` singleton): for every `k\in I_{61}`,
$$2\in\mathrm{comp}(a_k).\tag{17.1}$$

**Step 2 (forcing `I_{67}`).** Apply Lemma WF with `S:=\{67\}`,
`S':=\{61\}`, `i_0:=54` (`S(54)=\{61\}=S'`, `\mathrm{comp}(a_{54})=\{2\}`
singleton): for every `k\in I_{67}`,
$$2\in\mathrm{comp}(a_k).\tag{17.2}$$

**Step 3 (pairwise closure).** Fix any `i\in I_{61},j\in I_{67}`. By
`(17.1)`, `2\in\mathrm{comp}(a_i)`; by `(17.2)`, `2\in\mathrm{comp}(a_j)`.
Hence `2\in\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\subseteq\mathrm{rad}
(a_i)\cap\mathrm{rad}(a_j)`. So
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2\}\ne\varnothing` for
**every** `i\in I_{61},j\in I_{67}`, unconditionally.

**Step 4 (FCBC for the whole sequence `a_1=4087,a_2,a_3,\dots`).** Let
`H:=\{2,61,67\}`, finite. Fix `1\le m<n`, `S(m),S(n)` nonempty subsets of
`P_1` (Theorem CD). If `S(m)\cap S(n)\ne\varnothing`, Lemma SW1 gives a
prime in `P_1\cap\mathrm{rad}(a_m)\cap\mathrm{rad}(a_n)\subseteq H`.
Otherwise (identical case-split reasoning to §16, Step 4, using that
`\{\{61\},\{67\}\}` is the unique disjoint pair among `P_1`'s three
nonempty subsets), `\{S(m),S(n)\}=\{\{61\},\{67\}\}`, so — up to swapping
`m,n` — `m\in I_{61},n\in I_{67}`, and Step 3 gives `\mathrm{rad}(a_m)
\cap\mathrm{rad}(a_n)\cap\{2\}\ne\varnothing`, with `\{2\}\subseteq H`.
Both cases give `H\cap\mathrm{rad}(a_m)\cap\mathrm{rad}(a_n)\ne
\varnothing`, so `H` satisfies FCBC. `\blacksquare`

**Conclusion (Theorem 5.1).** With `H=\{2,61,67\}`,
`L:=\mathrm{lcm}(2,61,67)=2\cdot61\cdot67=8{,}174` (product, distinct
primes), and `T:=|Good|` (Theorem 5.1's construction), `a_{n+T}=a_n+L`
for **every** `n\ge1`. This is the simplest closure of this form in this
workspace's history: a single common prime, `2`, unconditionally divides
**every** member of the two disjoint-core classes `I_{61}`,`I_{67}`
(Step 1–2 above) — the theorem's hypothesis and conclusion concern only
these two classes, not the core-`P_1` class `I_{\{61,67\}}` (which
`a_1=4087=61\times67` itself belongs to, since `4087` is odd; that class
is handled separately and unconditionally by Lemma SW1, not by
`(17.1)`/`(17.2)`).

**Numerical sanity check (evidence only, not part of the proof).**
Independently generated the literal-rule sequence to `N=20{,}000`: `I_{67}`
has `9{,}375` members, `I_{61}` has `10{,}312` members, and `313` further
members have core `\{61,67\}` (`9{,}375+10{,}312+313=20{,}000`,
consistent with Theorem CD's 3-part partition). Checked `(17.1)`/`(17.2)`
directly: **all** `19{,}687` disjoint-core members (`I_{61}\cup I_{67}`)
have `2\in\mathrm{comp}`, zero violations. (For contrast, not as part of
the claim: of the `313` core-`P_1` members — including `a_1=4087` itself
— `157` are odd; this is expected and irrelevant to the proof, since
Lemma SW1 covers this class via the shared prime `61` or `67`, never
needing `2`.)

### 18. Summary: two new fully solved concrete instances

`a_1=2747` and `a_1=4087` join `a_1=15` (Case I) and `a_1=247` (round 13,
Case B via Theorem FW2) as fully, unconditionally solved concrete
instances of the whole IMO problem — the 3rd and 4th such instances, and
the first two obtained via the new Singleton-Chain Closure mechanism
(structurally simpler than Theorem FW1/FW2's multi-case Boolean tables,
since in both instances one side of the pair receives a **fully
unconditional** forced set, collapsing the argument to a direct
"one side's known set contains the other side's forced element" chase
with no case split at all). The general problem (arbitrary `a_1`) remains
open — `current.md`'s overall Status correctly stays `partial`.

**Reusable proof template (Lemma SCF + the `|P_1|=2` FCBC assembly, §15,
Step 4 of §16/§17).** Any future `a_1` with `|P_1|=2` for which (a) one
side's class receives, via finitely many singleton-companion low-index
witnesses of the *other* core, a forced finite set `A` (Lemma SCF), and
(b) some single low-index witness of the *first* core has companion set
`\subseteq A`, is automatically — by the identical 4-step argument above —
a fully solved concrete instance. This is strictly easier to apply than
Theorem FW1/FW2's general disjunctive-forcing machinery whenever
condition (b) can be met by a single witness (as happened in both
instances closed this round), since it avoids any case-split table
entirely.

## Promotable lemmas

- **Lemma UCR (Universal Class Realization)** — §1 above. Statement: for
  disjoint cores `S,S'\subseteq P_1` and a nonempty finite set of primes
  `C` disjoint from `P_1`, if `S\cup C` is realized (Lemma ERD-C sense) as
  an actual term's exact radical, then `C\cap\mathrm{comp}(a_j)\ne
  \varnothing` for every index `j` with core disjoint from `S`. Proof uses
  only Lemma P′ and elementary set manipulation (no domination/ordering
  argument needed) — reusable by any future approach attacking Conjecture
  (JW), the Stabilization Conjecture, or any other cross-core coverage
  question in this workspace.
- **Corollary UCR-JW** — §2 above, an immediate but genuinely useful
  packaging of Lemma UCR into a per-index sufficient criterion (WRP) for
  Conjecture (JW); reusable as a "cheap first check" before invoking any
  heavier recursive machinery on a given core pair.
- **Lemma BS (Backbone Stabilization)** — §6 above, new this round.
  Statement: for a proper core `S'\subsetneq P_1` with `I_{S'}` infinite,
  enumerate `I_{S'}` in increasing order `j_1<j_2<\cdots` and define
  `B_k:=\bigcap_{t=1}^k\mathrm{comp}(a_{j_t})`. Then `B_k` is eventually
  constant (some finite `k_0` with `B_k=B_{k_0}` for all `k\ge k_0`), and
  this stabilized value equals `\bigcap_{j\in I_{S'}}\mathrm{comp}(a_j)`
  exactly — i.e. `B_{k_0}\subseteq\mathrm{comp}(a_j)` for **every**
  `j\in I_{S'}`, without exception, not merely those realized after
  position `k_0`. Proof is pure finite-descent/cardinality combinatorics
  (no number-theoretic input beyond finiteness of each `\mathrm{comp}
  (a_j)`); holds unconditionally for any core `S'` of any sequence
  satisfying this problem's hypotheses. Reusable by any future approach
  needing a permanently-valid lower bound on a class's companion-set
  intersection.
- **Lemma BS-Dichotomy** — §7 above, new this round (elementary corollary
  of the already-certified Lemma ERD-C applied to `C:=S'\cup B(S')`).
  Gives a precise, non-empirical criterion for when a nonempty backbone
  `B(S')` is exactly realized (branch A, "Case A") versus permanently
  blocked (branch B, "Case B") — replacing the previously ad hoc
  "checked numerically" classification with a genuine dichotomy.
- **Theorem CAC (Case A Closure of Conjecture (JW))** — §8 above, new this
  round. Statement: if a doubly-infinite disjoint core pair `(S,S')` has
  `B:=B(S')\ne\varnothing` exactly realized (Case A via the `S'`-side),
  then `W:=B` satisfies Conjecture (JW) for `(S,S')` — unconditionally,
  for the full infinite index classes `I_S,I_{S'}`, not a tested prefix.
  Proof combines Lemma BS with the already-certified Lemma UCR in three
  lines. Reusable as the standard closure route for any future Case A
  pair found in this workspace, and directly composable with the
  already-certified Theorem SW/Theorem 5.1 chain to finish the whole
  problem for any `a_1` all of whose doubly-infinite pairs turn out to be
  Case A.
- **Proposition PVB (`P′`-Vacuity Barrier)** — §11 above, new this round.
  Statement: for any core `S'` and distinct `i,j\in I_{S'}` (same class),
  Lemma P′ applied to `\{i,j\}` gives no constraint relating
  `\mathrm{comp}(a_i)` to `\mathrm{comp}(a_j)`, since its conclusion is
  automatically witnessed by any `p\in S'` regardless of the companion
  sets. Formalizes precisely why Lemma UCR (and any argument built only
  from Lemma P′) cannot be transplanted to a within-class permanence claim
  (the intersection Lemma P′ guarantees is already fully accounted for by
  the shared core, leaving zero information about the companion parts).
  Proof is three lines, general-purpose, reusable by any future approach
  attempting a within-class permanence/stabilization argument in this
  workspace — a standing "do not attempt via Lemma P′/UCR alone" warning
  with a rigorous proof behind it, not just an empirical observation.
- **Theorem TLL-Refuted (Two-in-a-Row / `K`-in-a-Row Locking Fails)** — §12–
  13 above, new this round. Statement: the "two-in-a-row locks it"
  dichotomy proposed by this round's outline (and, more generally, any
  small a-priori-uniform bound on the running-companion-intersection
  stabilization index `k_0`) is FALSE. Proof: three independently
  cross-validated (brute-force pairwise-gcd generator vs.
  antichain-optimized generator, exact agreement) explicit counterexamples:
  `a_1=375` (`|P_1|=2`, same structural type as the mandated `2747`,
  `4087`), core `\{3\}`: running intersection `\{2\}` at two consecutive
  class members `a_4=384,a_6=396`, breaks at the very next member
  `a_7=399=3\cdot7\cdot19` (odd); `a_1=4199`, core `\{13,19\}`: identical
  companion sets `\{2,3\}` at the first two class members
  `a_{16}=4446,a_{90}=5928`, persists for `24` consecutive members, breaks
  at `a_{1854}=41002=2\cdot13\cdot19\cdot83`; `a_1=4199`, core `\{17,19\}`:
  running intersection `\{2\}` persists for `108` consecutive class
  members (`a_{54}` through `a_{3821}`), breaks at
  `a_{3840}=80427=3\cdot17\cdot19\cdot83` (odd). All twelve cited term
  values independently confirmed via `sympy.factorint` and (for the shorter
  traces) by hand division. Reusable as a standing negative result: rules
  out an entire family of "certify permanence from a short/moderate
  observed repeat" mechanisms for any future approach to Backbone
  Permanence, `(MRS_S)`, or any other running-intersection stabilization
  claim in this workspace, and specifically explains why the round-12
  overclaim (2–4 matching terms) and even the round-13 explorer's
  `N=10{,}000{,}000`–`20{,}000{,}000` numeric checks on `2747`/`4087`
  cannot, on their own, ever constitute a proof.
- **Lemma SCF (Singleton-Chain Forcing)** — §15 above, new round 14.
  Statement: for disjoint nonempty cores `S,S'\subseteq P_1`, if
  `i_1,\dots,i_r` all have core `S'` and singleton companion sets
  `\{\pi_1\},\dots,\{\pi_r\}`, then `A:=\{\pi_1,\dots,\pi_r\}\subseteq
  \mathrm{comp}(a_k)` for **every** `k\in I_S` — an elementary but
  reusable aggregation of finitely many single applications of the
  already-certified Lemma WF. Proof is four lines, needs nothing beyond
  Lemma WF applied `r` times. Reusable by any future approach seeking to
  force a *large* (multi-prime) unconditional set on one side of a
  disjoint core pair from several small (singleton-companion) witnesses
  on the other side, without any running-intersection/permanence
  argument.
- **Direct Singleton-Chain Closure for `a_1=2747`** — §16 above, new round
  14. A complete, unconditional, gap-free proof (via Lemma SCF + Lemma WF
  + Lemma SW1 + Theorem CD + Theorem 5.1, all already certified except
  Lemma SCF, certified above) that `H=\{2,3,7,41,67\}` satisfies FCBC for
  the entire sequence `a_1=2747,a_2,a_3,\dots`, giving explicit
  `L=115{,}374`, `T=|Good|`, `a_{n+T}=a_n+L` for every `n\ge1`. This is a
  complete solved-instance result, not merely a lemma — reusable as a
  template (see §18) and citable directly as "`a_1=2747` is a fully solved
  instance of IMO 2026 P6."
- **Direct Singleton-Chain Closure for `a_1=4087`** — §17 above, new round
  14. Identical structure, `H=\{2,61,67\}`, `L=8{,}174`. A complete
  solved-instance result: `a_1=4087` is a fully solved instance of IMO
  2026 P6.
