## Status
partial

## Round 15 Outline (proof-outliner directive — attack Bounded
Forced-Set Existence Conjecture using this round's calibration data
and reusable witness-search tool)

**Target (unchanged): the whole problem** — via a GENERAL proof (not
instance-by-instance) that Corollary MSF / the Chaining Sufficiency
Theorem's hypothesis (some finite closing witness collection) is
satisfied for EVERY `a_1` and disjoint core pair (Conjecture WCE /
Bounded Forced-Set Existence). This is the sharpest general target per
round 14's recommendation, still open.

**Technique**: unchanged top-level target, but this round formalizes
the general-unification explorer's validated **witness-search tool**
(`/tmp/round-15/gen.py`, `/tmp/round-15/wce_search3.py` — a provably
exact, faster-than-powerset procedure for checking the Chaining
Sufficiency Theorem's success condition via minimal-hitting-set/
choice-function enumeration) as a certifiable **decision-procedure
lemma**, then uses it to sharpen exactly which class of pairs resist.

**Skeleton:**
1. **Certify the witness-search reduction as a lemma**: for a fixed
   dedup'd pool of witness companion-sets per side, checking whether
   SOME sub-collection satisfies the Chaining Sufficiency Theorem's
   success condition is equivalent to checking only choice-function-
   generated candidate collections (not the full powerset) — because
   the success predicate `T_S(R)` is an up-set in the witness-collection
   lattice, so its minimal witnesses are exactly realized by choice
   functions over the defining family. Builder must write this proof
   formally (the explorer verified it holds numerically/reproduces
   published closures exactly for `247`,`4199`, but did not write a
   formal up-set proof — that's the gap to close here).
2. **Recalibrate the Bounded Forced-Set Existence Conjecture against
   this round's sharper negative data**: `a_1=21528751`'s classes
   `\{197\}`,`\{1061\}`,`\{197,1061\}` have a companion-floor/min-comp-
   size that is FROZEN EXACTLY (not just "no smaller example found")
   across a 3.3x-8x depth increase (`N=150,000→500,000` and
   `N=27,832→250,000` respectively, two independent explorers). State
   precisely: this refutes the conjecture **in its MSF-singleton-shaped
   form** for these classes (a companion set of size ≤2 or exactly-
   floor-achieving-with-few-primes will not appear for `\{1061\}`-type
   classes from this data) but does NOT bear on whether the full
   Chaining Sufficiency Theorem (larger, non-singleton, disjunctive
   witness collections — the general mechanism, not MSF's special
   case) still succeeds — this is the correct, careful reading per this
   workspace's own standing rule (never confuse a refuted sufficient
   mechanism with a refutation of the target).
3. **Run the certified witness-search tool (once formalized) against
   the 6th channel of `a_1=21528751`** (`\{1061\}` vs `\{103,197\}`,
   confirmed still open by both this round's structural-obstruction and
   alternative-mechanism explorers via independent diagnoses) and
   against the fresh instance `a_1=20677=23·29·31` (found by the
   general-unification explorer this round, deliberately checked NOT to
   degenerate to Case I, 5/6 pairs closed by the bounded search) — a
   concrete new candidate 7th solved instance if the last pair
   `\{23\}`/`\{29\}` also closes.
4. **Honestly report whichever of the following actually happens**:
   (a) the tool finds a closing collection for the previously-stuck
   pairs (real progress, extends the toolkit's reach); (b) the tool
   fails to find one within a reasonable search bound (evidence only
   about this specific bounded search per the explorer's own
   documented caution — `4199` needed witnesses beyond this bound for
   3/6 pairs even though it's fully solved); (c) neither — report a
   sharper, still-open recalibrated statement of Bounded Forced-Set
   Existence.

**Key lemmas (claim + mechanism):**
- Choice-function reduction — because the success predicate is
  monotone (an up-set) in the collection of witnesses used, so testing
  minimal elements via choice functions over the defining families
  suffices; this is a standard finite-lattice fact, needs a short formal
  write-up, not new machinery.
- Refuted-in-MSF-form vs. general Chaining Sufficiency distinction —
  because MSF is a strictly narrower special case (singleton-heavy
  witnesses) of the general theorem (arbitrary finite witness
  collections via full Boolean case-split), so evidence against the
  narrow mechanism is silent on the general one (already the
  workspace's own standing methodological rule, applied here to fresh
  data).

**Open gaps**: the general existence question (Conjecture WCE /
Bounded Forced-Set Existence) itself remains fully open — this round's
work is calibration + tooling + possibly 1-2 more concrete closures,
not a proof of the general conjecture.

**Cases to cover**: none beyond the specific instances/channels
attempted.

**Watch out for**: do not let a successful bounded search on
`a_1=20677` or partial channels of `21528751` create pressure toward
believing the general conjecture is close — per the round-14 standing
rule, instance count is not evidence about the general theorem's truth.

## Approaches tried

- **Round 14 (this round, first build of this file — see note below on
  provenance).** Two-part dispatch, cheap-then-hard, per the round-14
  outline (`/tmp/round-14/proof-outliner.md`) and the outline-reviewer's
  caution (`/tmp/round-14/outline-reviewer.md`).
  **(1) Certified Corollary MSF** (Multi-Singleton Forcing) as a new,
  general, fully-proved corollary of the already-certified Chaining
  Sufficiency Theorem + Lemma WF — **worked**, certified to
  `lemmas/corollary-MSF-multi-singleton-forcing.md`. Independently
  re-derived (not copied) and re-verified by fresh `sympy`/hand
  factorization all 10 fresh-pair closures reported by
  `/tmp/round-14/math-explorer-wce-general.md`, plus discovered and
  proved **one new instance closure the explorer did not find**: the
  disjoint core pair `\{103\}` vs. `\{197\}` of `a_1=21528751` — this workspace's own
  longest-standing "hardest recurring instance" (flagged rounds 6–11) —
  closes via Corollary MSF with `W=\{2,3,7\}`, **despite** class
  `I_{\{197\}}` never once exhibiting `|\mathrm{comp}|\le2` in an
  extensive search (509 members checked to sequence-depth 30,000, sizes
  always `\ge3`). This is a genuinely new finding this round, not in the
  explorer's report, and it materially corrects the framing of Part (2)
  below.
  **(2) Attempted the Small-Companion Existence Lemma** — **inconclusive,
  now with much stronger evidence of likely falsity as a universal
  claim**, and, more importantly, **shown to be the wrong target**: the
  `21528751:(\{103\},\{197\})` closure above proves Corollary MSF succeeds
  on pairs where the Small-Companion Existence Lemma provably fails on one
  side (over the tested range) — so even a full proof of the Lemma would
  not have been necessary for, and a refutation of the Lemma would not
  threaten, this round's actual applicable mechanism. Reported honestly as
  an open, likely-false-as-stated conjecture, with a precise, weaker,
  still-open replacement target identified (`Bounded Forced-Set Existence`
  below). Conjecture (WCE) itself, for general `a_1`, remains open — no
  overclaim.

- **Provenance note.** This file did not exist on disk before this round
  (the round-14 outline-reviewer's report confirms: `witness-chaining-
  universal-existence.md does not exist on disk at all`, only described in
  `/tmp/round-14/proof-outliner.md`). This is the first build of the
  slug. It is registered in the ranker as a `copy_approach` branch of
  `sunflower-bundle-closure` (inheriting that approach's inherited
  content: the Chaining Sufficiency Theorem, the Single-Witness-Per-Side
  Insufficiency Proposition, and the honest §10.7 finding that Conjecture
  (WCE) is not established to be easier than Conjecture (JW) — all already
  certified in `lemmas/theorem-chaining-sufficiency-and-single-witness-
  insufficiency.md`, cited, not re-derived, below).

## Current best

**Inherited, already-certified content (cited, not re-derived here).**
The Chaining Sufficiency Theorem and the Single-Witness-Per-Side
Insufficiency Proposition
(`lemmas/theorem-chaining-sufficiency-and-single-witness-insufficiency.md`)
reduce Conjecture (JW) for any doubly-infinite disjoint core pair `(S,S')`
to the existence of a finite "successful" witness collection `R`; the
existence of such an `R` for *every* pair, for *every* `a_1`, is
Conjecture (WCE), proved (§10.7 of that file's source) to satisfy
`\text{(WCE)}\Rightarrow\text{(JW)}` but not conversely established — so a
general proof of (WCE) would already close the whole problem, and is not
known to be an easier target. This remains true; nothing in this round
changes it.

### Part 1 — Corollary MSF (Multi-Singleton Forcing): certified, general,
new

**Statement (full statement + proof in `lemmas/corollary-MSF-multi-
singleton-forcing.md`, certified this round).** Fix `a_1`, `P_1:=
\mathrm{rad}(a_1)`, disjoint nonempty `S,S'\subseteq P_1`. If (i) there are
`r\ge1` fixed indices `i_1,\dots,i_r` with `S(i_m)=S'` and `\mathrm{comp}
(a_{i_m})=\{q_m\}` singleton for each `m` (writing `P:=\{q_1,\dots,q_r\}`),
and (ii) there is a fixed index `j_0` with `S(j_0)=S` and `\mathrm{comp}
(a_{j_0})\subseteq P`, then `W:=P` solves Conjecture (JW) for `(S,S')`:
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap P\ne\varnothing` for every
`i\in I_S,j\in I_{S'}` — with **zero Boolean case analysis** (the proof is
three lines of set manipulation once Lemma WF is applied `r+1` times: `r`
independent singleton applications give `P\subseteq\mathrm{comp}(a_i)` for
every `i\in I_S`; one more application gives `\mathrm{comp}(a_j)\cap
P\ne\varnothing` for every `j\in I_{S'}`; any element of the latter
nonempty intersection lies in `\mathrm{comp}(a_i)` too since `P\subseteq
\mathrm{comp}(a_i)`). Also shown to be a strict instantiation of the
Chaining Sufficiency Theorem with `R_{S'}=\{i_1,\dots,i_r\}`,
`R_S=\{j_0\}` (cross-checked via that theorem's own `\mathcal T_S(R),
\mathcal T_{S'}(R)` machinery — `\mathcal T_S(R)` collapses to the
singleton `\{W\}`, making success automatic). **No new mathematics beyond
already-certified Lemma WF/Lemma NIDF(a)/Theorem CD — this names and
certifies a reusable pattern.**

**Independent computational verification, round 14 (fresh generator, cross-
validated against a naive `O(n)`-per-step brute-force generator on the
first 30–40 terms of every tested `a_1`, exact match in every case; every
cited factorization independently re-derived via `sympy.factorint`).**

Generator: implemented the literal problem definition (`a_{n+1}` = least
integer `>a_n` with `\gcd(a_{n+1},a_i)>1` for all `i\le n`), using a sieve
of smallest-prime-factors up to `2\times10^6` for fast factorization, and
checking every candidate against the *full* set of prior radicals (no
shortcut/approximation). Cross-validated exactly against a naive
`math.gcd`-based generator on the first 30–40 terms of all 9 tested `a_1`
values (`2747,4087,143,391,713,1073,1517,1001,21528751`) — bit-for-bit
match in every case.

| `a_1` | `P_1` | pair `(S,S')` | singleton witnesses on `S'`-side (idx, value, prime) | subset witness `j_0` on `S`-side (idx, value, `\mathrm{comp}`) | `W=P` |
|---|---|---|---|---|---|
| 2747 | `\{41,67\}` | `(\{67\},\{41\})` | `a_{13}=3321=3^4\cdot41` (`3`); `a_{14}=3362=2\cdot41^2` (`2`); `a_{163}=11767=7\cdot41^2` (`7`) | `a_3=2814=2\cdot3\cdot7\cdot67`, `\mathrm{comp}=\{2,3,7\}` | `\{2,3,7\}` |
| 4087 | `\{61,67\}` | `(\{67\},\{61\})` | `a_{54}=7442=2\cdot61^2` (`2`) | `a_5=4288=2^6\cdot67`, `\mathrm{comp}=\{2\}` | `\{2\}` |
| 143 | `\{11,13\}` | `(\{13\},\{11\})` | `a_5=176=2^4\cdot11` (`2`); `a_{13}=297=3^3\cdot11` (`3`) | `a_3=156=2^2\cdot3\cdot13`, `\mathrm{comp}=\{2,3\}` | `\{2,3\}` |
| 391 | `\{17,23\}` | `(\{23\},\{17\})` | `a_5=459=3^3\cdot17` (`3`); `a_8=544=2^5\cdot17` (`2`) | `a_3=414=2\cdot3^2\cdot23`, `\mathrm{comp}=\{2,3\}` | `\{2,3\}` |
| 713 | `\{23,31\}` | `(\{31\},\{23\})` | `a_2=736=2^5\cdot23` (`2`); `a_{32}=1587=3\cdot23^2` (`3`) | `a_3=744=2^3\cdot3\cdot31`, `\mathrm{comp}=\{2,3\}` | `\{2,3\}` |
| 1073 | `\{29,37\}` | `(\{37\},\{29\})` | `a_{19}=1682=2\cdot29^2` (`2`); `a_{37}=2349=3^4\cdot29` (`3`) | `a_9=1332=2^2\cdot3^2\cdot37`, `\mathrm{comp}=\{2,3\}` | `\{2,3\}` |
| 1517 | `\{37,41\}` | `(\{37\},\{41\})` | `a_{25}=2624=2^6\cdot41` (`2`); `a_{39}=3321=3^4\cdot41` (`3`) | `a_7=1776=2^4\cdot3\cdot37`, `\mathrm{comp}=\{2,3\}` | `\{2,3\}` |
| 1001 | `\{7,11,13\}` | `(\{7\},\{11\})` | `a_{59}=1408=2^7\cdot11` (`2`) | `a_{54}=1372=2^2\cdot7^3`, `\mathrm{comp}=\{2\}` | `\{2\}` |
| 1001 | | `(\{7\},\{13\})` | `a_{51}=1352=2^3\cdot13^2` (`2`) | `a_{54}=1372`, `\mathrm{comp}=\{2\}` | `\{2\}` |
| 1001 | | `(\{11\},\{13\})` | `a_{51}=1352` (`2`) | `a_{59}=1408`, `\mathrm{comp}=\{2\}` | `\{2\}` |
| **21528751** | `\{103,197,1061\}` | `(\{197\},\{103\})` | `a_{1405}=21727232=2^{11}\cdot103^2` (`2`); `a_{11812}=23201883=3^7\cdot103^2` (`3`); `a_{27832}=25472209=7^4\cdot103^2` (`7`) | `a_{2575}=21893004=2^2\cdot3^4\cdot7^3\cdot197`, `\mathrm{comp}=\{2,3,7\}` | `\{2,3,7\}` |

(Every row's `(S,S')` label is oriented so that `S'` is exactly the core
supplying the singleton witnesses (column 4) and `S` is exactly the core
supplying `j_0` (column 5), matching the general statement's roles exactly
— e.g. row 1: `2747`'s singleton witnesses `a_{13},a_{14},a_{163}` have
core `\{41\}`, so `S'=\{41\}`, and `j_0=a_3` has core `\{67\}`, so
`S=\{67\}`, giving the pair label `(\{67\},\{41\})`. In the `21528751`
row, `S'=\{103\}` supplies the three singleton witnesses, `S=\{197\}`
supplies `j_0`, and Corollary MSF's proof gives:
every member of `I_{\{197\}}` is divisible by all of `2,3,7`
simultaneously (matches the observed data below exactly — the only
`|\mathrm{comp}|=3` members of `I_{\{197\}}` in the tested range have
`\mathrm{comp}=\{2,3,7\}` exactly, and every member has `\{2,3,7\}
\subseteq\mathrm{comp}`), and every member of `I_{\{103\}}` is divisible
by at least one of `2,3,7`.)

**All 11 pairs verified to close by Corollary MSF, independently, from
scratch — matches the explorer's 10, plus one new instance.** For
`2747` and `4087`, since `|P_1|=2` each has only one disjoint core pair,
so — following the already-certified Corollary-FW2-FCBC template
(Lemma SW1 for intersecting cores + this pair's (JW)-closure for the sole
disjoint pair `\Rightarrow` FCBC `\Rightarrow` Theorem 5.1) — Conjecture
(JW) being closed here is the sole remaining ingredient for
`a_1=2747,4087` to become fully solved concrete instances of the whole
problem; the explicit `H`/`T`/`L` assembly for these two is the dispatched
task of the sibling approach `sunflower-inadmissibility-toolkit` this
round (not duplicated here to avoid conflicting/duplicate certification —
see that approach's file for the full Theorem-5.1-level write-up). For
`143,391,713,1073,1517,1001`, no claim is made about full-instance closure
(these `a_1` were chosen by the explorer purely as fresh disjoint-core-pair
test cases, not as targets this workspace has separately confirmed are
otherwise fully covered by intersecting-core pairs via Lemma SW1 — that
check was not performed and is out of this round's scope). For
`21528751`, `|P_1|=3`, so 6 disjoint core-pair channels exist in total;
only `(\{103\},\{197\})` is closed here — the other 5 remain open (see
Part 2's data below for what is and is not known about them).

### Part 2 — Small-Companion Existence Lemma: genuinely open, likely false
as stated, and shown to be the wrong target

**Restatement of the candidate lemma (per the outline).** *For every
`a_1` and every proper core `S\subsetneq P_1`, does the infinite class
`I_S` contain infinitely many members `k` with `|\mathrm{comp}(a_k)|\le2`?*
Already confirmed by the outline-reviewer (independently re-verified here)
that this is **not** already refuted by `theorem-UBS-false-case-II.md`
(that theorem is about `\sup_{n\notin I_{P_1}}\omega(a_n)=\infty`, a
statement about unbounded *large* values occurring *somewhere*; this
Lemma is about *recurring small* values within one *specific* class — the
two are logically independent).

**New numerical evidence this round, substantially extending the
outline-reviewer's finding (independently reproduced and pushed
further).** Generated `a_1=21528751` to sequence-depth `N=30{,}000`
(values up to `25{,}779{,}355`), independently fresh, cross-validated
against a naive generator on the first 30 terms (exact match). Examined
every one of the 6 core classes of `P_1=\{103,197,1061\}`:

| core | `\#` members (`N=30{,}000`) | `\#` with `|\mathrm{comp}|\le2` | `\%` | `\#` singletons | `|\mathrm{comp}|` distribution |
|---|---|---|---|---|---|
| `\{103\}` | 29,301 | 6,593 | 22.5% | 3 | `\{1:3,2:6590,3:13271,4:7909,5:1473,6:55\}` |
| `\{197\}` | 509 | **0** | **0%** | 0 | `\{3:8,4:286,5:204,6:11\}` |
| `\{1061\}` | 10 | **0** | **0%** | 0 | `\{4:3,5:7\}` |
| `\{103,197\}` | 152 | 75 | 49.3% | — | `\{2:75,3:66,4:11\}` |
| `\{103,1061\}` | 27 | 18 | 66.7% | 1 | `\{1:1,2:17,3:8,4:1\}` |
| `\{197,1061\}` | 0 | — | — | — | (no member observed in this range — not shown to be finite, only sparse/absent here) |

Class `I_{\{197\}}`, checked across all 509 tested members (first 15 and
last 15 sizes: `4,5,4,5,4,5,4,4,5,4,4,5,4,5,4,\dots,4,5,5,4,5,4,5,4,4,5,5,
4,5,4,5`), shows **zero** occurrences of `|\mathrm{comp}|\le2` and **no
downward trend whatsoever** across an order-of-magnitude-larger sample
than the outline-reviewer's own check (509 vs. 136 members) — a materially
stronger negative signal, still short of a proof (an "infinitely many"
existence claim can never be refuted by any finite prefix, however large —
this is the same asymmetry `CLAUDE.md`'s own rigor rules flag for
"infinitely many" claims in the other direction: absence of a witness in a
finite search is evidence, not proof, of non-existence). Class
`I_{\{1061\}}` shows the identical pattern (0/10, sizes always `\ge4`).
By contrast, `I_{\{103\}}` (which contains the smallest prime of `P_1`)
and the two cores that include `103` both have abundant small-companion
members, including actual singletons.

**Second data point (also computed this round, `a_1=4199`, `P_1=\{13,17,
19\}`, generated to `N=30{,}000`, cross-validated).**

| core | `\#` members | `\#` with `|\mathrm{comp}|\le2` | `\%` | `\#` singletons |
|---|---|---|---|---|
| `\{13\}` | 6,977 | 112 | 1.6% | 0 |
| `\{17\}` | 15,391 | 5,009 | 32.5% | 24 |
| `\{19\}` | 4,542 | 80 | 1.8% | 0 |
| `\{13,17\}` | 1,703 | 962 | 56.5% | 50 |
| `\{13,19\}` | 389 | 60 | 15.4% | 0 |
| `\{17,19\}` | 856 | 465 | 54.3% | 25 |

Here `I_{\{13\}}` and `I_{\{19\}}` have **no** singleton witnesses in this
range (matching the explorer's finding exactly — `24` singleton-`\{2\}`
witnesses on `I_{17}` only) but **do** have a small, non-vanishing,
roughly-stable fraction (`1.6\%,1.8\%`) of `|\mathrm{comp}|=2` members —
so the weaker literal statement of the Lemma (`|\mathrm{comp}|\le2`, not
necessarily singleton) is **not** contradicted here; the negative signal
is specific to `a_1=21528751`'s classes `\{197\},\{1061\}`, where the
minimum observed `|\mathrm{comp}|` is `3`, `4` respectively with a stable,
non-shrinking distribution over the whole tested range.

**Attempted proof mechanism, per the outline's Step 4 (dual of
`theorem-UBS-false-case-II.md`'s Landau Count Lemma / Euler-divergence
machinery) — attempted, does not transfer, precise obstruction
identified.** Re-read `theorem-UBS-false-case-II.md`'s proof in full. Its
density *lower* bound on the complement class `I_{P_1}^c` (Corrected
Density Sub-Lemma, giving `|I_{P_1}^c\cap[1,N]|\ge cN`) is derived **from
an assumed exact periodicity** `a_{n+T}=a_n+L` (the very hypothesis being
contradicted, reached via the certified `theorem-UBS-sufficiency.md`
chain) combined with the Imprint Periodicity Lemma's mod-`p` residue
analysis — i.e. that density lower bound is a *consequence of assumed
global periodicity*, not a fact derivable from the raw greedy recursion
alone. The Landau Count Lemma itself is a pure **upper** bound
(`A_k(X)=o(X)`, the count of *all* integers `\le X` with `\omega\le k` is
asymptotically negligible) — it structurally cannot supply a **lower**
bound on how often a specific, recursively-defined sub-class `I_S`
(defined by an arbitrary greedy process, not an arithmetic progression or
periodic set) hits small-`\omega` values; combining an upper bound on a
superset (`\{m\le X:\omega(m)\le k\}`) with no density information about
`I_S` itself gives no conclusion in either direction. Assuming periodicity
to get a density lower bound on `I_S` (as the certified proof did for
`I_{P_1}^c`) would be circular here, since establishing periodicity
*is* the whole Stabilization Conjecture this file exists to help prove.
**Conclusion: the dual-direction attempt genuinely stalls, for a precise,
identifiable reason (upper-bound tool, wrong-shaped target, no periodicity
to exploit) — not "did not have time," a real structural obstruction,
matching exactly the "off-`W` magnitude" diagnosis already on record in
`sunflower-bundle-closure`'s §10.7b (round 13) and flagged by this round's
own outline.** No tool in `knowledge_base.md` or the crux corpus supplies
a lower-density bound on small-`\omega` occurrence within an arbitrary
recursively-defined subclass (consistent with rounds 6/9/11's repeated,
independent confirmations that no classical analytic tool transfers to
this specific gcd-chain structure).

**Most important finding of Part 2: the Small-Companion Existence Lemma is
the wrong target, independent of whether it is true or false.** The new
`21528751:(\{103\},\{197\})` closure in Part 1 is a fully rigorous,
zero-case-split closure via Corollary MSF, on a pair where **one side
(`I_{\{197\}}`) is empirically shown (509/509, no exceptions) to never
satisfy `|\mathrm{comp}|\le2`.** Corollary MSF's actual hypothesis is
strictly weaker than "both sides have small companion sets": it only needs
(a) **one** side to carry `r` independent singleton witnesses, for **any**
finite `r` (no bound on `r` or on `|P|=r` needed), and (b) the **other**
side to carry a single witness whose companion set is a *subset* of the
resulting `P` — which can be large (here `|P|=3`). So even a hypothetical
proof of the Small-Companion Existence Lemma would not have been *needed*
to obtain this round's new closures, and the negative evidence against it
does **not** threaten Corollary MSF's applicability. **This round
downgrades the Small-Companion Existence Lemma from "candidate stepping
stone toward general WCE" to a mis-aimed sub-target**, and proposes, in
its place, the following still-open, more accurate replacement (stated
here as a precise open conjecture, NOT claimed proved):

> **Bounded Forced-Set Existence Conjecture (open, new this round, not
> attempted further beyond statement).** For every `a_1` and every
> doubly-infinite disjoint core pair `(S,S')`, does there exist (in either
> direction) a finite `r\ge1` and `r` fixed low-index witnesses on one side
> with pairwise-independent singleton companion sets, plus one fixed
> witness on the other side whose companion set is a subset of the union
> of those `r` singletons? This is exactly Corollary MSF's hypothesis, is
> strictly *weaker* than the Small-Companion Existence Lemma (as
> demonstrated by the `21528751` instance above, which satisfies this but
> not the Small-Companion Lemma on the `\{197\}` side), and — if it held
> for every pair — would resolve Conjecture (WCE) via Corollary MSF alone,
> with no case-split machinery ever needed. **Not proved or refuted this
> round**; flagged as the more accurate open target for any future attempt
> at general (WCE), replacing the Small-Companion Existence Lemma.

**Honest summary of Part 2, per the dispatch's three options.** (a) No
proof found. (b) No genuine refutation found either — the numerical
evidence (509 zero-exceptions on one class, extended from the reviewer's
136) is strong but, per the standing "infinitely many" rigor rule, cannot
constitute a proof of falsity for an existence-over-an-infinite-set claim.
(c) The gap is narrowed precisely: the Small-Companion Existence Lemma
itself is now understood to be very likely false as a *universal* claim
(strong, extended numerical evidence against it on at least one class),
true with substantial margin on most other tested classes, and — most
importantly — **not the correct sub-target to pursue further**, since
Corollary MSF's actual (weaker) hypothesis, the new Bounded Forced-Set
Existence Conjecture, already succeeds on the one case where the stronger
Lemma clearly fails. Conjecture (WCE), for general `a_1`, remains open;
no overclaim is made.

## Promotable lemmas

- **Corollary MSF (Multi-Singleton Forcing)** — general statement + full
  proof in `lemmas/corollary-MSF-multi-singleton-forcing.md` (written this
  round, ready for reviewer certification). Depends only on already-
  certified Lemma WF, Lemma NIDF(a), Theorem CD; shown to be a strict
  instantiation of the already-certified Chaining Sufficiency Theorem.
  Reusable by any future approach attacking Conjecture (JW)/(WCE) for a
  specific pair — try this (search for independent singleton witnesses on
  one side plus a covering witness on the other) before a full FW1/FW2-
  style case table.
- The 11-row worked-instantiation table above (Part 1) is reusable
  evidence/citable data for any future approach wanting concrete solved-
  pair examples, in particular the `21528751:(\{103\},\{197\})` closure,
  which resolves — for this specific disjoint pair only, not the whole
  `a_1=21528751` instance — this workspace's own longest-standing
  "hardest recurring instance" flag (rounds 6–11).
- The **Bounded Forced-Set Existence Conjecture** (Part 2) is stated here
  as a new, precise, still-open replacement target for general (WCE) —
  not proved, not certified as a lemma, but recorded as the honest,
  sharper open gap for future rounds (weaker and better-targeted than the
  Small-Companion Existence Lemma it replaces).
