## imo-2026-06

### Context this round (why these 4)

All 3 math-explorers converged on the SAME underlying mechanism —
Lemma WF (Witness Forcing, certified `lemmas/lemma-WF-witness-forcing-and-
theorem-FW-instances.md`) plus the certified Chaining Sufficiency Theorem
(`lemmas/theorem-chaining-sufficiency-and-single-witness-insufficiency.md`)
— applied three different ways: (a) a cheap "Multi-Singleton Forcing"
special case that closed 10/10 fresh test pairs; (b) an extension of the
SAME mechanism, using witnesses drawn from a THIRD disjoint core class
(not just the two classes of the target pair), that derives all 6 of
`a_1=4199`'s disjoint core-pair channels; (c) a direct application
(no running intersection / no Backbone Permanence at all) that closes
`a_1=2747` and `a_1=4087`, bypassing the refuted Early/Bounded
Stabilization mechanism entirely. None of this is new mathematics beyond
Lemma WF/XC/Chaining Sufficiency (already certified, unconditional) — it
is new, high-value **instantiation and generalization work**. Per the
dispatch, the field below separates the low-risk concrete-instance
closures (approaches 2–3) from the high-risk general-theorem attempt
(approach 1), and keeps a structurally independent route alive
(approach 4) so the population does not collapse onto one framing.

---

### witness-chaining-universal-existence — revise (of `sunflower-bundle-closure`)

**Target: the whole problem** — prove Conjecture (WCE) (existence of a
successful finite witness collection `R`, per the certified Chaining
Sufficiency Theorem, for **every** doubly-infinite disjoint core pair
`(S,S')` and every `a_1`), which — via the already-certified chain
Chaining Sufficiency Theorem ⟹ Conjecture (JW) ⟹ Theorem SW ⟹ FCBC ⟹
Theorem 5.1 — would close the ENTIRE Stabilization Conjecture and hence
the whole IMO problem for every `a_1`.

**Technique.** Two separate, explicitly-ranked sub-goals, cheap-then-hard
(do not skip straight to the hard one):

1. **(Cheap, near-certain, do this first.)** Certify "Multi-Singleton
   Forcing" as a formal named Corollary of the already-certified Chaining
   Sufficiency Theorem: if class `I_{S'}` has `k` fixed low-index members
   with singleton companion sets `\{p_1\},\dots,\{p_k\}` (`k` distinct
   primes), Lemma WF forces every member of `I_{S'}` — wait, of the
   COMPLEMENTARY class `I_S` — to be divisible by ALL of `p_1,\dots,p_k`
   simultaneously (each application of Lemma WF is an independent,
   unconditional `∀`-fact, not a case split); if `I_S` also has one
   low-index member whose companion set is a subset of `\{p_1,\dots,p_k\}`,
   that member forces every member of `I_{S'}` to hit at least one of
   them — closing the pair with **zero** Boolean case analysis. This is a
   literal instantiation of the certified theorem (no new proof content),
   but should be written up once, named, and cited by name from every
   future instance-closure (approaches 2 and 3 below both use it).
2. **(Hard, exploratory, honestly may not close this round.)** State
   precisely, as the actual open general claim — **do not overclaim**:
   *Conjecture (WCE), for arbitrary `a_1`, remains open.* The explorers
   only checked finitely many instances (10 fresh pairs for (1); 5 more
   channels of one `a_1` and 2 more `a_1` values for (2)/(3) below) — this
   is strong instance-by-instance evidence, not a proof for arbitrary
   `a_1`. Attempt (but do not force) a genuine existence argument for a
   weaker, well-posed sub-claim: **Small-Companion Existence Lemma
   (candidate, unproved):** does every infinite class `I_S` contain
   infinitely many members `k` with `|\mathrm{comp}(a_k)|\le2`? Note
   explicitly for the builder: this is **NOT** already refuted by
   `theorem-UBS-false-case-II.md` — that theorem refutes a *uniform upper
   bound* on `|\mathrm{comp}(a_k)|` over **all** `k\in I_S` (i.e. `\sup`
   is infinite); it says nothing about whether *some* (even infinitely
   many) members have small companion sets. These are logically
   independent — `\sup=\infty` is fully consistent with the `\liminf`
   (or even positive-density occurrence) of small values. If provable,
   this would make Multi-Singleton/small-disjunction witnesses always
   eventually available, giving a real route to general WCE. If NOT
   provable this round, the approach must say so plainly and record
   exactly which sub-step failed (do not paper over with "empirically
   true").

**Skeleton:**
1. Formalize Multi-Singleton Forcing as **Corollary MSF** of the Chaining
   Sufficiency Theorem — statement + 1-paragraph proof (pure logic from
   already-certified Lemma WF).
2. Re-derive (not just cite) the 10 fresh-pair closures from the
   wce-general explorer's report as worked instantiations of Corollary
   MSF, independently checking every cited factorization by hand/sympy —
   these become citable mini-corollaries (e.g. `a_1=143,391,713,...`),
   cheap additional solved-instance evidence even if the general claim
   stalls.
3. State Conjecture (WCE) and the Small-Companion Existence Lemma
   precisely, as the two live open general targets (not proven,
   not refuted).
4. Attempt the Small-Companion Existence Lemma via a density-style
   argument dual to the certified Landau Count Lemma / Euler divergence
   machinery already built for `theorem-UBS-false-case-II.md` (reusable
   ingredient: that proof already analyzes the distribution of `ω(a_n)`
   for periodic-tail sequences — check whether the SAME machinery, run
   in the other direction, bounds the *frequency* of small-`ω` terms
   within a class rather than only the *existence* of unboundedly-large
   ones). If this stalls, record the precise obstruction (most likely:
   the same "off-`W` magnitude" issue already flagged by `sunflower-
   bundle-closure`'s round-13 finding that JW⟹WCE needs information of
   the same shape `(UB_S)` was proven unable to supply).
5. Do NOT claim WCE proved in general unless step 4 produces a complete,
   gap-free argument — if it doesn't, Status stays `partial` and the
   file should state exactly "N instances closed, general claim open,
   here is the precise obstruction" (matching this workspace's
   established honesty standard).

**Key lemmas (claim + mechanism):**
- Corollary MSF — because Lemma WF applied independently to `k` fixed
  singleton-companion witnesses gives `k` independent unconditional
  `∀`-facts (no interaction between them), and a matching subset witness
  on the other side turns "all k" vs. "at least one of k" into an
  automatic common-prime guarantee for every cross pair.
- Small-Companion Existence Lemma (OPEN, candidate only) — would follow
  from a lower bound on the density of `ω`-small values within a class,
  dual to the already-certified upper-bound-refutation machinery
  (Landau Count Lemma / Euler `Σ1/p` divergence) — genuinely new content
  if it can be made to work, not yet established.

**Open gaps:** Conjecture (WCE) for general `a_1` (step 3–4); whether the
Small-Companion Existence Lemma is even true (not just whether it's
provable with current tools) is itself unverified — flag as a testable
numerical sub-question if the analytic argument stalls (check density of
`|comp|≤2` members across several classes at large `N`, several `a_1`,
before investing further analytic effort).

**Cases to cover:** none (existence claim over all `a_1`, all pairs) —
this is exactly why it's hard; do not attempt exhaustive casework here.

**Watch out for:** (a) do not conflate "true for every tested instance"
with "proved for general `a_1`" — this is the exact overclaim shape this
workspace has caught and corrected multiple times (rounds 11, 12, 13);
(b) the Small-Companion Existence Lemma, even if numerically very
plausible, needs an actual proof mechanism named — a bare "seems to
happen often" note is not a lemma; (c) if step 4 fails, this approach's
honest fallback contribution is Corollary MSF + the re-derived 10-instance
evidence table, which is still valuable, certifiable content — don't let
a stalled hard target erase the cheap win.

---

### forced-primes-well-ordering — advance

**Target: the whole problem**, via the already-certified chain
Theorem SW → Theorem 5.1, exactly as `a_1=247`'s Corollary FW2-FCBC
already demonstrates end to end. This round: complete the SAME template
for `a_1=4199`, all 6 disjoint core-pair channels (`P_1=\{13,17,19\}`),
giving a SECOND fully solved concrete instance (larger than `247`'s,
since `|P_1|=3` gives 6 channels instead of 1).

**Technique.** Lemma WF (already certified) applied to 7 low-index
witnesses, including — this is the new ingredient this round —
witnesses drawn from a **pair-core** class (`S(i_0)=\{13,17\}`, whose
complement in `P_1` is the single class `\{19\}`), not only from the
three singleton-core classes Theorem FW1 already used. This works because
Lemma WF only needs `S,S'` disjoint nonempty subsets of `P_1` — it does
not require either side to be a singleton.

**Skeleton:**
1. Recall (do not re-derive) Theorem FW1 (`4199:(\{13\},\{17\})`,
   `W=\{2,3,83\}`, certified) — this is channel 1 of 6, done.
2. Enumerate the 6 disjoint unordered core-pair channels of
   `P_1=\{13,17,19\}` explicitly:
   `(\{13\},\{17\})`, `(\{13\},\{19\})`, `(\{17\},\{19\})`,
   `(\{13\},\{17,19\})`, `(\{17\},\{13,19\})`, `(\{19\},\{13,17\})`.
   Verify by hand this is exhaustive (7 nonempty subsets of a 3-element
   set, all unordered disjoint pairs) — cite/adapt Theorem SW's own
   3-way case split (intersecting cores auto-covered by Lemma SW1;
   these 6 are the only disjoint-core content needed, per that theorem's
   own certified exhaustiveness).
3. Fix and independently re-verify (by hand + `sympy.factorint`, do not
   trust the explorer report's arithmetic uncritically) the 7 witnesses:
   `a_2=4212=2^2\cdot3^4\cdot13` (core `\{13\}`, comp `\{2,3\}`),
   `a_5=4233=3\cdot17\cdot83` (core `\{17\}`, comp `\{3,83\}`),
   `a_9=4316=2^2\cdot13\cdot83` (core `\{13\}`, comp `\{2,83\}`),
   `a_{11}=4332=2^2\cdot3\cdot19^2` (core `\{19\}`, comp `\{2,3\}`),
   `a_{12}=4352=2^8\cdot17` (core `\{17\}`, comp `\{2\}`),
   `a_{82}=5746=2\cdot13^2\cdot17` (core `\{13,17\}`, comp `\{2\}`),
   `a_{92}=5967=3^3\cdot13\cdot17` (core `\{13,17\}`, comp `\{3\}`).
4. **For EACH of the 6 channels, explicitly verify witness-core
   disjointness from BOTH sides before invoking Lemma WF** — this is
   the exact step the explorer caught itself getting wrong once
   (`a_2,a_9` have core `\{13\}`, which is NOT disjoint from
   `\{13,17\}`, so they cannot be used to constrain `I_{\{13,17\}}` or
   its complement-class applications incorrectly) — write out this
   disjointness check as an explicit line for every witness/channel
   pairing, not just for the ones that "obviously" work.
5. Derive the per-class disjunctive facts (pure deduction from Lemma WF,
   cite Corollary MSF from `witness-chaining-universal-existence` where
   applicable):
   `I_{13}`: `2` (from `a_{12}`, singleton) and `(3\vee83)` (from `a_5`).
   `I_{19}`: `2` (from `a_{12}`) and `3` (from `a_{92}`) — both
   unconditional.
   `I_{17}`: `(2\vee3)` (from `a_2`) and `(2\vee83)` (from `a_9`).
   `I_{\{13,19\}}`: same shape as `I_{13}` (witnesses `a_5,a_{12}` have
   core `\{17\}`, disjoint from `\{13,19\}`).
   `I_{\{17,19\}}`: same shape as `I_{17}` (witnesses `a_2,a_9` have core
   `\{13\}`, disjoint from `\{17,19\}`).
   `I_{\{13,17\}}`: `(2\vee3)` (from `a_{11}`, core `\{19\}`, disjoint
   from `\{13,17\}`).
6. Case-split-close all 6 channels with `H_{\mathrm{extra}}=\{2,3,83\}`
   (channel `(\{19\},\{13,17\})` needs only `\{2,3\}`) — write out each
   of the 5 remaining channels' case split explicitly and exhaustively
   (2-3 cases each, all elementary Boolean splits on which disjunct
   holds).
7. Assemble via the Corollary-FW2-FCBC template: `H=P_1\cup
   \{2,3,83\}=\{2,3,13,17,19,83\}` satisfies FCBC for `a_1=4199` (Lemma
   SW1 for intersecting cores + the 6 channel closures for disjoint
   cores), hence Theorem 5.1 gives explicit `T=|Good|`,
   `L=\mathrm{lcm}(2,3,13,17,19,83)=2{,}091{,}102`, with
   `a_{n+T}=a_n+L` for every `n\ge1`.

**Key lemmas (claim + mechanism):**
- Lemma WF instantiated at 7 fixed witnesses gives 6 per-class
  disjunctive facts — because each application is an independent
  unconditional consequence of the pairwise-gcd fact (Lemma P′/XC), valid
  for literally every member of the target class regardless of index.
- All 6 channels close under `\{2,3,83\}` — because in every channel, one
  side either has an unconditional single prime or a 2-way disjunction
  that the other side's own (unconditional-or-disjunctive) facts always
  intersects; this is an exhaustive finite Boolean check, not an
  asymptotic argument.

**Open gaps:** the full case-split write-up for the 5 new channels (only
sketched by the explorer, not reviewer-grade); the final FCBC assembly
step (§7) needs to be written out in the same explicit 2-case form as
Corollary FW2-FCBC; `T=|Good|` needs to be computed/described explicitly
per Theorem 5.1's own construction (same open bookkeeping task as
`a_1=247`'s case, not yet done there either beyond stating the formula).

**Cases to cover:** all 6 disjoint core-pair channels of `P_1=\{13,17,
19\}` — explicitly enumerated above; do not skip any, and do not assume
the pattern "obviously" repeats without writing each one out (channel
`(\{19\},\{13,17\})` in particular uses a DIFFERENT, smaller witness set
`\{2,3\}` than the other 4 disjoint channels, so is not a copy-paste of
another channel's argument).

**Watch out for:** the exact self-caught error described in the
explorer's report — re-verify from scratch (do not trust the "already
fixed" claim) that every witness's core is disjoint from BOTH sides of
whichever channel it's cited for; a single wrong disjointness claim
invalidates that channel's closure silently. Also verify the channel
enumeration itself (7 nonempty subsets, 6 disjoint unordered pairs) is
exhaustive, the same way Theorem FW2/Corollary FW2-FCBC verified it for
the `|P_1|=2` case.

---

### sunflower-inadmissibility-toolkit — revise (reframe away from Backbone Permanence)

**Target: the whole problem**, via the same certified Theorem SW →
Theorem 5.1 chain. This round: **abandon** the Backbone Permanence /
Early-Bounded-Stabilization route for `a_1=2747` and `a_1=4087` (already
proven this workspace's own dead end — Theorem TLL-Refuted, round 13,
three independently-reproduced counterexamples including on these exact
two `a_1`) and instead close both instances directly via **Singleton-
Chain Closure**, a mechanism that uses NO running intersection and NO
permanence claim at all — so the still-open explicit-stabilization-index-
bound gap becomes irrelevant to these two instances, not merely
bypassed-for-now.

**Do not delete or contradict the standing round-13 record**: Lemma BS
and Theorem CAC (existence-only backbone stabilization) remain valid,
certified facts — only the EBS "two-in-a-row locks it" mechanism for
finding the stabilization point is refuted (Theorem TLL-Refuted). This
round's mechanism does not use Lemma BS/Theorem CAC/EBS at all, so it is
not affected by, and does not resurrect, that refutation.

**Technique.** Both `a_1=2747` (`P_1=\{41,67\}`) and `a_1=4087`
(`P_1=\{61,67\}`) have `|P_1|=2`, so — exactly as with `a_1=247` — the
ONLY disjoint core pair is the single pair `(\{41\},\{67\})` /
`(\{61\},\{67\})`. Close it directly with Corollary MSF (cite from
`witness-chaining-universal-existence`, or re-derive inline if that
approach isn't built first — this mechanism needs only the already-
certified Lemma WF, so it does not actually depend on the sibling
approach being built).

**Skeleton:**
1. **`a_1=2747`.** Independently re-verify (sympy + hand) the 4 witnesses:
   `a_3=2814=2\cdot3\cdot7\cdot67` (core `\{67\}`, comp `\{2,3,7\}`),
   `a_{13}=3321=3^4\cdot41` (core `\{41\}`, comp `\{3\}`),
   `a_{14}=3362=2\cdot41^2` (core `\{41\}`, comp `\{2\}`),
   `a_{163}=11767=7\cdot41^2` (core `\{41\}`, comp `\{7\}`).
   By Lemma WF (3 independent singleton applications, `i_0=13,14,163`,
   core `\{41\}` disjoint from `\{67\}`): every `k\in I_{67}` has
   `\{2,3,7\}\subseteq\mathrm{comp}(a_k)`. By Lemma WF (`i_0=3`, core
   `\{67\}` disjoint from `\{41\}`): every `k\in I_{41}` has
   `\mathrm{comp}(a_k)\cap\{2,3,7\}\ne\varnothing`. Combine: for any
   `i\in I_{41},j\in I_{67}`, whichever prime of `\{2,3,7\}` divides
   `a_i` also divides `a_j` (since `a_j`'s companion set contains all
   three) — `\gcd(a_i,a_j)>1`. `W=\{2,3,7\}`.
2. **`a_1=4087`.** Independently re-verify the 2 witnesses:
   `a_5=4288=2^6\cdot67` (core `\{67\}`, comp `\{2\}`),
   `a_{54}=7442=2\cdot61^2` (core `\{61\}`, comp `\{2\}`).
   By Lemma WF (both directions, singleton each time): every
   `k\in I_{61}` has `2\mid a_k`; every `k\in I_{67}` has `2\mid a_k`.
   `\gcd(a_i,a_j)\ge2` for any `i\in I_{61},j\in I_{67}`. `W=\{2\}` —
   the simplest possible closure in this whole workspace's history.
3. Assemble both via the Corollary-FW2-FCBC template: for `2747`,
   `H=\{2,3,7,41,67\}` satisfies FCBC (Lemma SW1 for intersecting cores
   + step 1 for the sole disjoint pair); for `4087`, `H=\{2,61,67\}`.
   Theorem 5.1 then gives explicit `T,L` for each (
   `L=\mathrm{lcm}(2,3,7,41,67)` for 2747;
   `L=\mathrm{lcm}(2,61,67)=8174` for 4087) with `a_{n+T}=a_n+L` for
   every `n\ge1`.
4. State clearly: this makes `a_1=2747` and `a_1=4087` the 3rd and 4th
   fully solved concrete instances of the whole problem in this
   workspace (after `247`, and pending `4199`'s completion in the sibling
   approach this round) — still `partial` for the general problem.

**Key lemmas (claim + mechanism):** identical mechanism to Corollary MSF
above — three (resp. two) independent singleton applications of Lemma WF
combine additively (AND, not OR, since each is unconditional) on one
side, and a single disjunctive application on the other, giving automatic
common-prime coverage; because it needs no running intersection or "the
observed value is the true limit" claim, it is fully immune to the
exact permanence-vs-observation gap that killed EBS.

**Open gaps:** none expected to remain for these two specific instances
if steps 1–3 check out (this is the cheapest, most template-following
build in this round's field) — the only real risk is an arithmetic/
factorization error, not a logical gap.

**Cases to cover:** the two instances `2747` and `4087`, each with
exactly one disjoint core pair (no casework beyond the direct
computation above).

**Watch out for:** re-verify every cited factorization independently
(do not trust the explorer report uncritically, per this workspace's
standing rule) — in particular confirm `a_{163}=11767` for `2747` really
is index 163 of that specific sequence (a large, easy-to-mistype index)
and that no smaller witness with a smaller index was missed that would
simplify the write-up (not required for correctness, but worth a quick
sanity pass). Also double check `\gcd(41,67)=1`, `\gcd(61,67)=1` (trivial,
but state it — `P_1`'s primes must be genuinely distinct for the
core-disjointness argument to typecheck).

---

### intersecting-family-covering-construction — advance

**Target: the whole problem**, via the same certified Theorem 5.1 chain,
but through a **structurally independent technique** (density/pigeonhole
on the coarse core sequence `G`, not witness-chaining) — kept live
specifically for population diversity, per CLAUDE.md's single-gap-trap
warning: if the entire field pursues only Lemma-WF-style witness
chaining and that route stalls on general `a_1` (a real risk — see
`witness-chaining-universal-existence`'s honestly-flagged obstruction),
this is the one approach in the population NOT resting on the same
underlying mechanism.

**Technique.** Continue from the certified Lemma WO (exact CRT
window-occupancy count) and Proposition BI (Backbone Permanence, even if
established, cannot force `\mathrm{BRL}(S')`/`G`-periodicity — a
feasibility-vs-minimality diagnosis). Proposition BI's own positive
redirection: attack **minimality** directly (which admissible candidate
is numerically *smallest* among a class of options), not feasibility —
no certified tool in this workspace currently reasons about minimality
as a first-class object.

**Skeleton:**
1. Recall Lemma WO and Proposition BI (already certified, do not
   re-derive).
2. Formalize a genuinely new minimality-sensitive tool: for a fixed
   window of `L_0=\mathrm{rad}(a_1)` consecutive integers, among the
   (Lemma WO-counted) integers of a given `P_1`-type, characterize which
   one the greedy process actually selects as the next term — this
   requires reasoning about the OTHER primes present (not just the
   `P_1`-type), i.e. a joint minimality-over-two-coordinates argument
   (which of Lemma WO's counted candidates is smallest AND satisfies the
   as-yet-unresolved-non-`P_1` gcd constraints).
3. Test the new tool on a small worked instance (`a_1=15` or `a_1=247`,
   both already fully understood/solved by other means, so any claim
   here is independently checkable) before generalizing — a concrete,
   numerically-verifiable minimality statement about which residue class
   mod `L_0` gets selected next, for a specific window, is the right
   size of first target.
4. If a minimality mechanism is found, connect it back to
   `\mathrm{BRL}(S')`/`G`-eventual-periodicity via the already-certified
   Lemma PD-from-BRL / Theorem PD-Conditional chain (round 12, cite, do
   not re-derive).

**Key lemmas (claim + mechanism):** none new certified yet this branch —
this round's job is to produce the first candidate minimality lemma
(open), building on Lemma WO's exact count as the raw material.

**Open gaps:** the entire minimality mechanism (Proposition BI's
redirection) — genuinely unattempted territory in this workspace; no
prior round has built any minimality-reasoning tool.

**Cases to cover:** none yet (exploratory step).

**Watch out for:** do not re-attempt a pure feasibility/counting argument
dressed up as "minimality" — Proposition BI already proves feasibility
alone cannot work; the new content must actually reason about "smallest
among admissible candidates," which is a different logical shape (an
order/extremal argument, not a covering/counting one).

---

### Summary for outline-reviewer

Build set candidates (in priority order): `forced-primes-well-ordering`
(advance — concrete, near-certain, high value, needs careful gap-checking
per "Watch out for"), `sunflower-inadmissibility-toolkit` (revise —
concrete, cheapest/lowest-risk build this round), `witness-chaining-
universal-existence` (revise of `sunflower-bundle-closure` — high-risk/
high-reward general theorem attempt, honestly scoped, real value even if
only step 1 (Corollary MSF) completes), `intersecting-family-covering-
construction` (advance — structurally independent technique, preserves
population diversity against a possible field-wide stall on witness-
chaining).
