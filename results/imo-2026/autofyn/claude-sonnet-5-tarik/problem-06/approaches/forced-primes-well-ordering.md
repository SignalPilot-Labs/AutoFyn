## Status
partial

## Round 15 Outline (proof-outliner directive — apply this round's
cheap Common-Recruiter Reuse finding to close more channels of
`a_1=21528751`)

**Target (unchanged): the whole problem** — via the already-certified
Theorem SW → Theorem 5.1 chain, plus concrete instance/channel
closures using Lemma WF as the mechanism (unchanged top-level route;
this round adds a cheap corollary + a new worked closure, not a new
mechanism).

**Technique**: unchanged (finite low-index witness-chaining via Lemma
WF / Chaining Sufficiency Theorem), but this round packages a
genuinely cheap generalization found independently by two of this
round's explorers: **Common-Recruiter Reuse** — the SAME finite
witness set already used to close one channel closes EVERY OTHER
disjoint-core channel whose two sides are each either equal to, or
disjoint from, one of the two original recruiting cores, for free (no
new search, no new witnesses).

**Skeleton:**
1. **Formalize Common-Recruiter Reuse as a corollary of the
   already-certified Lemma WF** (not a new mechanism — a bookkeeping
   observation about which target classes a fixed witness's Lemma-WF
   conclusion applies to): if witness `a_{i_0}` (companion set `C`
   disjoint from core `S`) forces `C∩comp(a_k)≠∅` (or `q∣a_k` if
   singleton) for every `k∈I_{S'}` with `S'` disjoint from `S` — this
   holds for literally EVERY core `S'` disjoint from `S`, not only the
   one core the witness was originally chosen to close. State this
   explicitly as **Corollary CRR** and give its 1-line proof (Lemma
   WF's own hypothesis is exactly "target core disjoint from witness's
   core" — nothing else about the specific target core is used).
2. **Apply Corollary CRR to `a_1=21528751`'s 4 already-on-file
   witnesses** (`a_{1405},a_{11812},a_{27832}` — core `{103}`, singleton
   companions `2,3,7` respectively; `a_{2575}` — core `{197}`, comp
   exactly `{2,3,7}`) against every target core disjoint from `{103}`
   or `{197}` (not just the originally-closed `{197}` vs `{103}`
   channel): this gives, unconditionally, `{2,3,7}⊆comp(a_k)` for every
   `k∈I_{\{197\}}∪I_{\{1061\}}∪I_{\{197,1061\}}`, and
   `comp(a_k)∩\{2,3,7\}≠∅` for every `k∈I_{\{103\}}∪I_{\{103,1061\}}`.
   Conclude: 4 more disjoint-core-pair channels close for free —
   `(\{103\},\{1061\})`, `(\{197\},\{1061\})`,
   `(\{103\},\{197,1061\})`, `(\{197\},\{103,1061\})` — bringing
   `a_1=21528751` to **5 of its 6 disjoint-core-pair channels closed**.
3. **Re-verify the numerical claim independently** (builder must
   re-derive, not copy, the explorer's `N=100,000` check: zero
   exceptions to `{2,3,7}⊆comp` on `I_{197}` (1695/1695), `I_{1061}`
   (30/30), `I_{197,1061}` (2/2); zero exceptions to
   `comp∩{2,3,7}≠∅` on `I_{103}` (97677/97677), `I_{103,1061}` (92/92)).
4. **Honestly scope the 6th channel** `(\{1061\},\{103,197\})` as NOT
   closed by this mechanism: the target core `\{103,197\}` is not
   disjoint from either recruiting core `\{103\}`/`\{197\}`, so Lemma
   WF/Corollary CRR cannot be aimed at it via those witnesses; the only
   disjoint recruiter is `\{1061\}` itself, whose class is sparse
   (30/100000) with no singleton witnesses and a companion floor that
   always includes one extra prime beyond `\{2,3,7\}` (varies:
   `11,17,13,19,...`). This channel needs either (a) a genuinely new
   witness search targeting the escape structure of core `\{103,197\}`
   (already-certified Permanent Bundle Lemma names `Q=\{11,97\}` as one
   permanent escape bundle for this exact core — check whether
   `W=\{2,3,7,11,97\}` closes it, i.e. does EVERY member of
   `I_{\{103,197\}}` have `comp∩\{2,3,7,11,97\}≠∅`?), or (b) leave open
   and report as the sole remaining channel of this instance.
5. **If (4a) succeeds**, this would be the workspace's SIXTH fully
   solved concrete instance (`21528751`) — a major addition since this
   has been the longstanding hardest recurring test case (flagged
   rounds 6-11). Check exhaustiveness (`|P_1|=3` gives `2^3-1=7`
   nonempty subsets, `15` intersecting-with-both-sides pairs `+` the `6`
   disjoint-core pairs enumerated above `=21` total pairs, matching the
   workspace's own established `4199` exhaustiveness-count template)
   before claiming the instance closed.

**Key lemmas (claim + mechanism):**
- Corollary CRR — because Lemma WF's proof only uses "witness's
  companion set is disjoint from the TARGET core," a hypothesis that
  doesn't reference which specific target core was originally intended
  — so the same witness's conclusion holds against every core disjoint
  from it, for free.
- (4a)'s candidate `W=\{2,3,7,11,97\}` closing channel 6 — because the
  Permanent Bundle Lemma already certifies `\{11,97\}` as one exhaustive
  escape route past `\{2,3,7\}` for core `\{103,197\}`; IF it is the
  ONLY escape route (open, not yet proven), the union closes the
  channel. **This "if" is the crux of whether channel 6 is easy or
  hard — flag explicitly, do not assume it.**

**Open gaps**: whether channel 6 closes (step 4/5); if not, it remains
the sole open channel of this instance, same status as before this
round but now precisely isolated (nothing else about `21528751` is
open).

**Cases to cover**: the 21-pair exhaustiveness count (15 intersecting +
6 disjoint) must be re-verified for `a_1=21528751`'s `P_1=\{103,197,
1061\}` before claiming full closure.

**Watch out for**: do not claim the general Bounded Forced-Set
Existence Conjecture is supported just because Common-Recruiter Reuse
is cheap and works here — this is instance-specific bookkeeping, not a
general existence proof (see `witness-chaining-universal-existence`
for the general-existence angle).

## Round 13 Outline (proof-outliner directive — attack Case B via a
genuinely new "finite low-index witness-chaining" mechanism, concrete
enough to complete for the two mandatory instances)

**Target (unchanged): the whole problem**, via Theorem SW → Theorem 5.1
(both already certified, do not re-derive). Round 12's Sandwich Uniqueness
Lemma (certified, unaffected, keep as-is) rigorously shows the
Realized-Backbone/UCR mechanism (Theorem CAC) cannot close `4199:(13,17)`
via either anchor — that negative result stands and is cited, not
re-derived. This round pivots this approach's *positive* content to a
genuinely new mechanism found by round 13's case-b explorer
(`/tmp/round-13/math-explorer-case-b.md`), structurally different from all
three previously-refuted mechanisms for Case B (Realized-Backbone/UCR,
Matched-Witness, NIDF-pigeonhole-on-escape-primes — see "Why this differs"
below and do not re-attempt any of the three as stated).

**The mechanism: finite disjunction-chaining from several FIXED low-index
prefix witnesses.** For a doubly-infinite disjoint pair `(S,S')` lacking a
class-wide backbone (Case B), pick finitely many fixed early indices
`i_1,\dots,i_r` with core disjoint from `S` (resp. `S'`). By the
already-certified elementary pairwise-gcd fact (Lemma P′ /
`lemma-P-prime-pairwise-intersecting.md`), **every** later member `a_k` of
the complementary class satisfies `\mathrm{comp}(a_k)\cap
\mathrm{comp}(a_{i_l})\ne\varnothing` for *each* fixed `l` — i.e. a
disjunction over `\mathrm{comp}(a_{i_l})` (this needs no permanence claim
about any running intersection, unlike Theorem CAC's route — it is a
direct, one-shot consequence of Lemma P′ applied to a single already-known
factorization, so it is unconditionally TRUE for every `k`, no asymptotic
or "eventually" content at all). Chaining `r` such disjunctions (one per
fixed witness) via finite Boolean case-analysis, cross-referenced against
the analogous disjunctions on the OTHER side, closes full pairwise
coverage. Worked out concretely on `4199:(13,17)` with 4 witnesses
(`a_2,a_5,a_9,a_12`, giving forced facts `2|a_i` (all `i\in I_{13}`,
`i>12`, since `\mathrm{comp}(a_{12})=\{2\}` is a **singleton** — a
degenerate, extra-easy special case of the general disjunction with only
one branch), `3|a_i\vee83|a_i`, `2|a_j\vee3|a_j`, `2|a_j\vee83|a_j`;
case-split on `2|a_j` closes every branch — see the explorer report for
the full worked case tree) and verified with **zero exceptions** at
`N=2{,}000{,}000` (complete signature cross-check, not sampled) on both
mandatory Case B instances (`4199:(13,17)` with `\{2,3,5,7,83\}`;
`247:(13,19)`, reconfirming the already-known `\{2,3,5,7\}` at 4× the
previous scale).

**Skeleton for this round's build (in order):**
1. Formalize and prove, in full, the ONE-LINE special case: a singleton
   companion set `\mathrm{comp}(a_{i_0})=\{q\}` at a fixed low index `i_0`
   (core disjoint from the target class `\bar S`) forces `q\mid a_k` for
   **every** `k\in I_{\bar S}` with `k>i_0` — via Lemma P′ alone, no
   further machinery. (Already a complete proof per the explorer's note;
   just needs to be written up rigorously with the exact indices.)
2. Formalize the general multi-witness disjunction step: `r` fixed
   low-index witnesses on one side give `r` disjunctive constraints on
   every later member of the complementary class — again a direct,
   unconditional consequence of Lemma P′, no permanence/asymptotic content.
3. For `4199:(13,17)`: carry out the full Boolean case-chain (both sides,
   4 witnesses) to a complete, hand-checkable proof that
   `\{2,3,5,7,83\}` covers every cross pair `(i,j)`, `i\in I_{13},j\in
   I_{17}`, past the finitely many low indices (`\le12` on the `I_{13}`
   side, `\le9` on the `I_{17}` side) — those finitely many small-index
   pairs need a separate direct finite check (finitely many gcd
   computations), not covered by the chaining argument itself.
4. For `247:(13,19)`: no singleton witness exists in the first 100 terms
   (confirmed by the explorer) — carry out the fuller multi-prime
   disjunction-chaining argument (denser case tree, not yet worked out in
   detail) to close `\{2,3,5,7\}` as a genuine covering set with a
   complete proof, not just the numerical re-confirmation already in hand.
5. **(Open, harder, flag honestly if not reached this round.)** Both
   Step 3 and Step 4 are currently INSTANCE-SPECIFIC (the witnesses were
   found by inspection). State clearly, as the approach's own honest
   remaining gap if reached, whether a general existence argument for
   "suitable low-index witnesses always exist for an arbitrary Case B
   pair" was found — do not claim this generalizes beyond the two
   mandatory instances unless actually proved.

**Why this differs from the three recorded dead ends (do not re-conflate):**
Realized-Backbone/UCR needs a class-WIDE frozen intersection (an
"eventually" claim); Matched-Witness used exactly one witness per side
hoping symmetry alone closes coverage (refuted by explicit counterexample);
NIDF-pigeonhole-on-escape-primes needs a missing cross-index linking fact
between `\mathrm{comp}(a_j)` and `\mathrm{comp}(a_{j'})` for two different
`j,j'` on the SAME side (Row-Restriction Obstruction). This mechanism uses
NO running intersection, NO single fixed pair, and NO same-side
cross-referencing — every disjunction is derived from ONE fixed low-index
witness applied to the whole range of the OTHER class, then combined by
finite Boolean case-analysis across several such witnesses. Sandwich
Uniqueness Lemma (certified) is unaffected and still correctly shows the
UCR-anchor mechanism specifically cannot close `4199:(13,17)` — this new
mechanism does not use UCR/Theorem CAC at all, so it is not threatened by
that negative result.

## Round 13 update (headline — read this first)

**Conjecture (JW) is now FULLY, UNCONDITIONALLY PROVED for both mandatory
Case B pairs — `4199:(13,17)` with explicit witness set `W=\{2,3,83\}`, and
`247:(13,19)` with explicit witness set `W=\{2,3,5,7\}`.** Both proofs are
complete (every factorization independently re-derived from scratch by
hand and by an independent fresh generator, every logical step a finite,
exhaustively-checked case split, no numeric/asymptotic content, no
dependence on any open hypothesis in this workspace) — see §L below for
the full derivations. This closes the round-13 outline's Step 3 and Step 4
in full (not merely "verified numerically," as the outline's own §3/§4
predicted might be needed) and additionally proves the outline's Step 1/2
special cases are subsumed by a cleaner general fact: **Lemma P′ forces
the disjunctive constraint on EVERY member of the complementary class, not
just members with index greater than the witness's** (Corollary P″ below)
— so the outline's flagged worry ("the finitely many small-index terms
below each witness threshold need a direct finite check") turns out to be
unnecessary: the mechanism, correctly formalized, needs no such separate
check at all.

**Bonus corollary found while formalizing this (not part of the assigned
task, but a direct, low-cost consequence worth recording): `a_1=247` is
now a FULLY, UNCONDITIONALLY SOLVED CONCRETE INSTANCE of the whole IMO
problem.** Since `P_1=\{13,19\}` has exactly `k=2` elements, the only
nonempty subsets are `\{13\},\{19\},\{13,19\}`, and the only disjoint pair
of them is `(\{13\},\{19\})` — so Theorem SW's exhaustive 3-case split
(intersecting cores / one side finite / doubly-infinite disjoint) has, for
this specific `a_1`, only ONE possible "hard" case, and §L's Theorem FW2
resolves it unconditionally (for literally every `i\in I_{13},j\in
I_{19}`, not merely eventually or for large indices). Consequently
`H:=P_1\cup\{2,3,5,7\}=\{2,3,5,7,13,19\}` satisfies FCBC
(`H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing`
for every `1\le i<j`, unconditionally — see §L, Corollary FW2-FCBC for the
3-line derivation from Theorem SW), and the already-certified Theorem 5.1
(`lemmas/theorem-5.1-master-conditional-theorem.md`) gives explicit
`T,L>0` with `a_{n+T}=a_n+L` for **every** `n\ge1`. This does **not** solve
the general problem (still open for arbitrary `a_1`) — the problem asks to
prove the conclusion for every sequence satisfying the hypotheses, and
`a_1=247` is only one instance — but it is, to this workspace's knowledge,
the hardest instance closed to date (past Case I's single-saturating-prime
triviality and past every previously-closed Case A/small-`k` instance),
and its full closure is a genuine, load-bearing test that the overall
architecture (Theorem SW → Theorem 5.1, both already certified) is sound
end-to-end on a real Case B example, not just conditionally.

For `4199:(13,17)`, `P_1=\{13,17,19\}` has `k=3` elements, hence `6`
possible disjoint nonempty-core pairs (`(\{13\},\{17\})`,
`(\{13\},\{19\})`, `(\{17\},\{19\})`, `(\{13\},\{17,19\})`,
`(\{17\},\{13,19\})`, `(\{19\},\{13,17\})`) — §L closes only the one
mandated channel, `(\{13\},\{17\})`. The other `5` remain open, so
`a_1=4199` itself is **not** (yet) fully solved by this round's work; only
the one assigned channel is closed.

## §L. Finite Low-Index Witness-Chaining: complete proofs of Conjecture
(JW) for `4199:(13,17)` and `247:(13,19)`

### L.0. Tools imported (already certified, cited verbatim, not re-proved)

- **Lemma P′** (`lemmas/lemma-P-prime-pairwise-intersecting.md`): for
  every `1\le i<j`, `\gcd(a_i,a_j)>1`.
- **Corollary P″ (unordered form of Lemma P′), proved here in one line
  since it is used repeatedly below and the round-13 outline's Step 1/2
  did not state it explicitly.** For every `i\ne j` (no ordering
  assumed), `\gcd(a_i,a_j)>1`. *Proof*: `\gcd` is symmetric, so WLOG
  `i<j`; apply Lemma P′ directly. `\blacksquare` This is the fact that
  removes the outline's flagged need for a separate check of "small
  indices below the witness threshold": Lemma P′ (via Corollary P″) gives
  the shared-prime fact for **every** pair of distinct indices
  simultaneously, with no dependence on which one is numerically smaller
  or was constructed first.
- **Theorem CD** (`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`):
  every index `i\ge1` has a well-defined, nonempty core
  `S(i):=\mathrm{rad}(a_i)\cap P_1\subseteq P_1`, and `\{I_S\}_{\varnothing
  \ne S\subseteq P_1}` (`I_S:=\{i:S(i)=S\}`) partitions `\mathbb N`.
- **Lemma XC** (`lemmas/lemma-XC-NIDF-FT-cross-companion-transversal.md`):
  writing `\mathrm{comp}(a_i):=\mathrm{rad}(a_i)\setminus P_1`, if
  `S(i)\cap S(j)=\varnothing` then `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)
  =\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)`.
- **Theorem SW** (`lemmas/theorem-SW-stabilization-sufficiency.md`): the
  precise formal content of "Conjecture (JW) holds for a doubly-infinite
  disjoint core pair `(S,S')`" is exactly the **Stabilization Conjecture**'s
  per-pair statement: *there is a finite `W_{S,S'}` with
  `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap W_{S,S'}\ne\varnothing` for
  every `i\in I_S,j\in I_{S'}`.* If this holds for every doubly-infinite
  disjoint core pair of a given `a_1`, then (Theorem SW) FCBC holds for
  that `a_1`, and (Theorem 5.1) `a_{n+T}=a_n+L` for every `n\ge1`.

### L.1. General Witness-Forcing Lemma (formalizes the outline's Steps 1–2 in one clean statement, strictly more general than the outline asked for)

**Lemma WF (Witness Forcing).** Fix disjoint nonempty cores `S,S'\subseteq
P_1$ and a fixed index `i_0` with `S(i_0)=S'` (so `i_0\notin I_S`, since
`S\cap S'=\varnothing`). Then for **every** `k\in I_S` (with no
restriction on `k` relative to `i_0` — `k` may be smaller or larger than
`i_0`), `\mathrm{comp}(a_k)\cap\mathrm{comp}(a_{i_0})\ne\varnothing`.

**Proof.** `k\ne i_0` (since `S(k)=S\ne S'=S(i_0)`). By Corollary P″,
`\gcd(a_k,a_{i_0})>1`, i.e. `\mathrm{rad}(a_k)\cap\mathrm{rad}(a_{i_0})\ne
\varnothing`. Since `S(k)=S` and `S(i_0)=S'$ are disjoint by hypothesis,
Lemma XC gives `\mathrm{rad}(a_k)\cap\mathrm{rad}(a_{i_0})=\mathrm{comp}
(a_k)\cap\mathrm{comp}(a_{i_0})`. Combining, `\mathrm{comp}(a_k)\cap
\mathrm{comp}(a_{i_0})\ne\varnothing`. `\blacksquare`

**Corollary (Disjunctive Forcing).** If `\mathrm{comp}(a_{i_0})=
\{q_1,\dots,q_r\}$ (`r\ge1`), then every `k\in I_S` satisfies `q_1\mid
a_k\vee\dots\vee q_r\mid a_k`. (Immediate: `\mathrm{comp}(a_k)\cap
\{q_1,\dots,q_r\}\ne\varnothing` means some `q_l\in\mathrm{comp}(a_k)$,
i.e. `q_l\mid a_k`.) When `r=1` this is an unconditional single forced
prime, not merely a disjunction — the "singleton witness" special case the
outline's Step 1 asked for, now recovered as the `r=1$ instance of one
uniform lemma rather than a separately-argued case.

This single lemma (needing only Lemma P′/Corollary P″ and Lemma XC, both
already certified) is the entire mechanism; §L.2–L.3 below apply it to
finitely many fixed low-index witnesses and combine the resulting
disjunctions by finite, exhaustively-checked Boolean case analysis.

### L.2. `4199:(13,17)`: complete proof, `W=\{2,3,83\}`

**Setup, independently re-derived.** `a_1=4199=13\times17\times19` (hand
check: `13\times17=221`, `221\times19=4199`), so `P_1=\{13,17,19\}`.
Generating the sequence directly from the problem's recursive rule
(independently, via a fresh Python implementation using the standard
minimal-radical-antichain admissibility test, and cross-checked by hand
factorization of each value below) gives, for `n=1,\dots,12`:

```
a_2 = 4212 = 2^2 · 3^4 · 13     S(2)={13}   comp(a_2)={2,3}
a_5 = 4233 = 3 · 17 · 83        S(5)={17}   comp(a_5)={3,83}
a_9 = 4316 = 2^2 · 13 · 83      S(9)={13}   comp(a_9)={2,83}
a_12= 4352 = 2^8 · 17           S(12)={17}  comp(a_12)={2}
```

*Hand verification of each factorization*: `4212/13=324=2^2\cdot3^4`
(`324=4\cdot81`), so `4212=2^2\cdot3^4\cdot13`, `\mathrm{rad}=\{2,3,13\}`.
`4233/17=249=3\cdot83`, so `4233=3\cdot17\cdot83`,
`\mathrm{rad}=\{3,17,83\}`. `4316/13=332=2^2\cdot83`, so
`4316=2^2\cdot13\cdot83`, `\mathrm{rad}=\{2,13,83\}`. `4352=2^8\cdot17`
(`2^8=256`, `256\times17=4352`), `\mathrm{rad}=\{2,17\}`. All four
factorizations, and hence all four `(S(\cdot),\mathrm{comp}(\cdot))$ pairs
above, match this round's math-explorer's report exactly and were
independently re-derived here (not merely trusted) both by hand and by a
freshly-written generator, cross-validated for consistency.

**Applying Lemma WF (Corollary, Disjunctive Forcing) with each witness:**

- `i_0=12\in I_{\{17\}}$, `\mathrm{comp}(a_{12})=\{2\}` (singleton):
  **for every `i\in I_{13}$, `2\mid a_i`.** [FACT1]
- `i_0=5\in I_{\{17\}}$, `\mathrm{comp}(a_5)=\{3,83\}`: for every
  `i\in I_{13}`, `3\mid a_i\vee83\mid a_i`. [FACT2]
- `i_0=2\in I_{\{13\}}$, `\mathrm{comp}(a_2)=\{2,3\}`: for every
  `j\in I_{17}`, `2\mid a_j\vee3\mid a_j`. [FACT3]
- `i_0=9\in I_{\{13\}}$, `\mathrm{comp}(a_9)=\{2,83\}`: for every
  `j\in I_{17}`, `2\mid a_j\vee83\mid a_j`. [FACT4]

(Each application of Lemma WF is legitimate: `S(12)=S(5)=\{17\}`,
`S(2)=S(9)=\{13\}`, and `\{13\}\cap\{17\}=\varnothing`, so the hypothesis
"`S(i_0)` disjoint from the target class's core" holds in every case, and
by Lemma WF's own statement the conclusion holds for **every** member of
the target class, with no restriction to indices larger than `i_0`.)

**Theorem FW1.** For every `i\in I_{13},j\in I_{17}`, `\mathrm{rad}(a_i)
\cap\mathrm{rad}(a_j)\cap\{2,3,83\}\ne\varnothing`. Hence Conjecture (JW)
holds for `4199:(\{13\},\{17\})` with witness set `W=\{2,3,83\}`.

**Proof.** Fix arbitrary `i\in I_{13},j\in I_{17}`. Two exhaustive,
mutually exclusive cases on whether `2\mid a_j`:

- **Case (a): `2\mid a_j`.** By FACT1, `2\mid a_i` as well (this holds for
  *every* `i\in I_{13}`, in particular this one). So `2\in\mathrm{rad}
  (a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,83\}`.
- **Case (b): `2\nmid a_j`.** By FACT3 (`2\mid a_j\vee3\mid a_j`), since
  `2\nmid a_j`, we get `3\mid a_j`. By FACT4 (`2\mid a_j\vee83\mid a_j`),
  since `2\nmid a_j`, we get `83\mid a_j`. So `a_j` has both `3` and `83`
  in its radical. Now apply FACT2 to this specific `i$: `3\mid a_i\vee
  83\mid a_i`. Whichever disjunct holds, that same prime (`3` or `83`)
  divides both `a_i` and `a_j` (since `a_j$ has both), so it lies in
  `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,83\}`.

Both cases give a nonempty intersection; since `i,j` were arbitrary
members of `I_{13},I_{17}` respectively, the claim holds for every such
pair. `\blacksquare`

**Independent numerical cross-check (supporting, not part of the proof):**
re-generated `a_1=4199` to `N=300{,}000` with a fast antichain-based
generator (independent of the explorer's own script), enumerated the
complete set of realized `\mathrm{rad}(\cdot)\cap\{2,3,83\}` signatures on
each side (`I_{13}`: `69{,}776` members, `3` distinct signatures,
`\{2,3\},\{2,83\},\{2,3,83\}` — all containing `2`, exactly as FACT1
predicts; `I_{17}`: `153{,}920` members, `5` distinct signatures,
`\{2\},\{3,83\},\{2,3\},\{2,3,83\},\{2,83\}` — every one either contains
`2` or contains both `3` and `83`, exactly matching Theorem FW1's case
split), and checked all `3\times5=15` signature pairs intersect: zero
failures. This matches the hand proof exactly and is offered only as a
sanity check, not as a substitute for the proof above.

### L.3. `247:(13,19)`: complete proof, `W=\{2,3,5,7\}`

**Setup, independently re-derived.** `a_1=247=13\times19`, so
`P_1=\{13,19\}`. Generating the sequence for `n=1,\dots,7` gives:

```
a_2 = 260 = 2^2 · 5 · 13     S(2)={13}   comp(a_2)={2,5}
a_3 = 266 = 2 · 7 · 19       S(3)={19}   comp(a_3)={2,7}
a_4 = 273 = 3 · 7 · 13       S(4)={13}   comp(a_4)={3,7}
a_5 = 285 = 3 · 5 · 19       S(5)={19}   comp(a_5)={3,5}
a_6 = 312 = 2^3 · 3 · 13     S(6)={13}   comp(a_6)={2,3}
a_7 = 342 = 2 · 3^2 · 19     S(7)={19}   comp(a_7)={2,3}
```

*Hand verification*: `260/13=20=2^2\cdot5`, so `260=2^2\cdot5\cdot13`,
`\mathrm{rad}=\{2,5,13\}`. `266/19=14=2\cdot7`, `\mathrm{rad}=\{2,7,19\}`.
`273/13=21=3\cdot7`, `\mathrm{rad}=\{3,7,13\}`. `285/19=15=3\cdot5`,
`\mathrm{rad}=\{3,5,19\}`. `312/13=24=2^3\cdot3`, `\mathrm{rad}=
\{2,3,13\}`. `342/19=18=2\cdot3^2`, `\mathrm{rad}=\{2,3,19\}`. All six
factorizations match this round's math-explorer's raw sequence listing and
were independently re-derived here by hand and by a fresh generator.

**Applying Lemma WF (Corollary) with each witness:** three witnesses in
`I_{13}` force three disjunctions on **every** `j\in I_{19}`, and three
witnesses in `I_{19}` force three disjunctions on **every** `i\in I_{13}`:

- (from `a_2`, `\mathrm{comp}=\{2,5\}`) `\forall j\in I_{19}$:
  `2\mid a_j\vee5\mid a_j`. [C1]
- (from `a_4`, `\mathrm{comp}=\{3,7\}`) `\forall j\in I_{19}$:
  `3\mid a_j\vee7\mid a_j`. [C2]
- (from `a_6`, `\mathrm{comp}=\{2,3\}`) `\forall j\in I_{19}$:
  `2\mid a_j\vee3\mid a_j`. [C3]
- (from `a_3`, `\mathrm{comp}=\{2,7\}`) `\forall i\in I_{13}$:
  `2\mid a_i\vee7\mid a_i`. [D1]
- (from `a_5`, `\mathrm{comp}=\{3,5\}`) `\forall i\in I_{13}$:
  `3\mid a_i\vee5\mid a_i`. [D2]
- (from `a_7`, `\mathrm{comp}=\{2,3\}`) `\forall i\in I_{13}$:
  `2\mid a_i\vee3\mid a_i`. [D3]

(Each application is legitimate by the same check as in §L.2:
`S(2)=S(4)=S(6)=\{13\}`, `S(3)=S(5)=S(7)=\{19\}`, `\{13\}\cap\{19\}=
\varnothing`.)

**Lemma A (I_{19} minimal-pattern reduction).** For every `j\in I_{19}`:
`(2\mid a_j\wedge3\mid a_j)\vee(2\mid a_j\wedge7\mid a_j)\vee(3\mid
a_j\wedge5\mid a_j)`.

**Proof.** Case split on `2\mid a_j`.
- If `2\mid a_j`: by C2, `3\mid a_j\vee7\mid a_j`. If `3\mid a_j`, the
  first disjunct (`2\wedge3`) holds. If `7\mid a_j` (whether or not `3\mid
  a_j`), the second disjunct (`2\wedge7`) holds. Either way the claim
  holds.
- If `2\nmid a_j`: by C1 (`2\vee5`), `5\mid a_j`. By C3 (`2\vee3`),
  `3\mid a_j`. So the third disjunct (`3\wedge5`) holds.

These two cases are exhaustive. `\blacksquare`

**Lemma B (I_{13} minimal-pattern reduction).** For every `i\in I_{13}`:
`(2\mid a_i\wedge3\mid a_i)\vee(2\mid a_i\wedge5\mid a_i)\vee(3\mid
a_i\wedge7\mid a_i)`.

**Proof.** Identical structure, case split on `2\mid a_i`.
- If `2\mid a_i`: by D2 (`3\vee5`), if `3\mid a_i` the first disjunct
  (`2\wedge3`) holds; if `5\mid a_i` the second disjunct (`2\wedge5`)
  holds.
- If `2\nmid a_i`: by D1 (`2\vee7`), `7\mid a_i`. By D3 (`2\vee3`),
  `3\mid a_i`. So the third disjunct (`3\wedge7`) holds.

`\blacksquare`

**Theorem FW2.** For every `i\in I_{13},j\in I_{19}`, `\mathrm{rad}(a_i)
\cap\mathrm{rad}(a_j)\cap\{2,3,5,7\}\ne\varnothing`. Hence Conjecture (JW)
holds for `247:(\{13\},\{19\})` with witness set `W=\{2,3,5,7\}`.

**Proof.** Fix arbitrary `i\in I_{13},j\in I_{19}`. By Lemma B, `i`'s
prime-divisibility pattern on `\{2,3,5,7\}` contains (at least) one of the
three pairs `\pi_i\in\{\{2,3\},\{2,5\},\{3,7\}\}` (meaning: both primes of
`\pi_i` divide `a_i`). By Lemma A, `j`'s pattern contains one of `\pi_j\in
\{\{2,3\},\{2,7\},\{3,5\}\}`. It suffices to check every one of the
`3\times3=9` combinations `(\pi_i,\pi_j)` shares a common prime — an
exhaustive, finite, hand-checkable list:

| `\pi_i` | `\pi_j` | shared prime |
|---|---|---|
| `\{2,3\}` | `\{2,3\}` | `2` (also `3`) |
| `\{2,3\}` | `\{2,7\}` | `2` |
| `\{2,3\}` | `\{3,5\}` | `3` |
| `\{2,5\}` | `\{2,3\}` | `2` |
| `\{2,5\}` | `\{2,7\}` | `2` |
| `\{2,5\}` | `\{3,5\}` | `5` |
| `\{3,7\}` | `\{2,3\}` | `3` |
| `\{3,7\}` | `\{2,7\}` | `7` |
| `\{3,7\}` | `\{3,5\}` | `3` |

All `9` combinations share a common prime lying in `\{2,3,5,7\}`. Since
`i` realizes at least one `\pi_i` and `j` at least one `\pi_j` (Lemmas
B, A), whichever combination applies gives a prime dividing both `a_i`
and `a_j`, hence lying in `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap
\{2,3,5,7\}`. `\blacksquare`

**Independent numerical cross-check (supporting, not part of the proof):**
re-generated `a_1=247` to `N=300{,}000` (fast antichain-based generator),
enumerated the complete set of realized `\mathrm{rad}(\cdot)\cap
\{2,3,5,7\}` signatures on each side (`I_{13}`: `8` distinct signatures —
`\{2,5\},\{3,7\},\{2,3\},\{2,3,5\},\{2,3,7\},\{2,5,7\},\{3,5,7\},
\{2,3,5,7\}`; `I_{19}`: `8` distinct signatures —
`\{2,7\},\{3,5\},\{2,3\},\{2,3,5\},\{2,3,7\},\{2,5,7\},\{3,5,7\},
\{2,3,5,7\}`), and checked all `64` signature pairs intersect: zero
failures. Notably, `I_{13}` never (in `300{,}000` terms) realizes the
2-element sets `\{2,7\}` or `\{3,5\}` and `I_{19}` never realizes `\{2,5\}`
or `\{3,7\}` — consistent with, though not needed by, Lemmas A/B (the
proof above only needs that whatever a member's pattern *is*, it contains
one of the three listed minimal pairs; it does not need — and does not
claim — that no other pattern could occur).

### L.4. Corollary FW2-FCBC: `a_1=247` is a fully solved concrete instance

**Statement.** For `a_1=247`, `H:=\{2,3,5,7,13,19\}` satisfies FCBC:
`H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing` for every
`1\le i<j`.

**Proof.** Fix `1\le i<j`. By Theorem CD, `S(i),S(j)` are well-defined,
nonempty subsets of `P_1=\{13,19\}`. Two exhaustive cases:

- **`S(i)\cap S(j)\ne\varnothing`** (Lemma SW1, `lemmas/theorem-SW-
  stabilization-sufficiency.md`): some prime of `S(i)\cap S(j)\subseteq
  P_1\subseteq H` lies in `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)`.
- **`S(i)\cap S(j)=\varnothing`**: since `P_1=\{13,19\}` has only the
  three nonempty subsets `\{13\},\{19\},\{13,19\}`, and `\{13,19\}`
  intersects both others, the only disjoint unordered pair of nonempty
  subsets is `\{\{13\},\{19\}\}`. So `\{S(i),S(j)\}=\{\{13\},\{19\}\}`,
  i.e. (up to swapping `i,j`) `i\in I_{13},j\in I_{19}`. Theorem FW2
  gives `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,5,7\}\ne
  \varnothing`, and `\{2,3,5,7\}\subseteq H`.

Both cases give `H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne
\varnothing`. `\blacksquare`

**Consequence.** By the already-certified Theorem 5.1
(`lemmas/theorem-5.1-master-conditional-theorem.md`, hypothesis `(†')`
= FCBC), there exist explicit positive integers `T=|Good|`,
`L=\mathrm{lcm}(2,3,5,7,13,19)=51870`, with `a_{n+T}=a_n+L` for **every**
`n\ge1`. This is a complete, unconditional proof of the IMO problem's
conclusion for the specific instance `a_1=247` — not a claim about the
general problem, which remains open for arbitrary `a_1` (see "Cases to
cover" / "Open gaps" below), but a genuine, fully rigorous solved
instance, independently re-verifiable end to end from this section alone
plus the two already-certified imported theorems.

*(Numeric note, not part of the proof: `\mathrm{lcm}(2,3,5,7,13,19)=
2\cdot3\cdot5\cdot7\cdot13\cdot19=51{,}870`, computed directly as the
product since all six primes are distinct: `2\cdot3=6`, `6\cdot5=30`,
`30\cdot7=210`, `210\cdot13=2730`, `2730\cdot19=51870`.)*

## §M. Complete closure of all 6 disjoint core-pair channels for
`a_1=4199` (`P_1=\{13,17,19\}`), and Corollary FW1-FCBC: `a_1=4199` is a
SECOND fully solved concrete instance

### M.0. Tools imported (already certified, cited verbatim, not re-proved)

Identical import list to §L.0: **Corollary P″** (unordered Lemma P′),
**Theorem CD** (core decomposition), **Lemma XC** (cross-companion
intersection = companion intersection for disjoint cores), **Lemma SW1**
and **Theorem SW** (`lemmas/theorem-SW-stabilization-sufficiency.md`),
**Theorem 5.1** (`lemmas/theorem-5.1-master-conditional-theorem.md`), and
**Lemma WF (Witness Forcing) + Corollary (Disjunctive Forcing)**, proved in
§L.1 and certified in `lemmas/lemma-WF-witness-forcing-and-theorem-FW-
instances.md`:

> Fix disjoint nonempty cores `S,S'\subseteq P_1` and a fixed index `i_0`
> with `S(i_0)=S'`. Then for **every** `k\in I_S`, `\mathrm{comp}(a_k)\cap
> \mathrm{comp}(a_{i_0})\ne\varnothing`. If `\mathrm{comp}(a_{i_0})=
> \{q_1,\dots,q_r\}`, every `k\in I_S` satisfies `q_1\mid a_k\vee\dots\vee
> q_r\mid a_k`; if `r=1` this is unconditional.

### M.1. Setup: exact factorizations (independently re-derived), and
exhaustiveness of the 6-channel enumeration

**Setup.** `a_1=4199=13\times17\times19` (hand check: `13\times17=221`,
`221\times19=4199`), so `P_1=\{13,17,19\}`, `k=|P_1|=3`.

**Witnesses used below (indices and factorizations independently
re-derived here, both by hand and by a freshly-written Python generator
implementing the problem's literal recursive rule — `a_{n+1}` is the
smallest integer `>a_n` with `\gcd(a_{n+1},a_i)>1` for every `i\le n` —
cross-validated against `sympy.factorint`, exact match on every value):**

```
a_2  = 4212 = 2^2 · 3^4 · 13     S={13}      comp={2,3}
a_5  = 4233 = 3 · 17 · 83        S={17}      comp={3,83}
a_9  = 4316 = 2^2 · 13 · 83      S={13}      comp={2,83}
a_11 = 4332 = 2^2 · 3 · 19^2     S={19}      comp={2,3}
a_12 = 4352 = 2^8 · 17           S={17}      comp={2}
a_92 = 5967 = 3^3 · 13 · 17      S={13,17}   comp={3}
```

*Hand verification of each factorization*: `a_2/13=324=2^2\cdot3^4`
(`324=4\cdot81`), so `\mathrm{rad}(a_2)=\{2,3,13\}` (re-derived in §L.2,
reused here). `a_5/17=249=3\cdot83`, `\mathrm{rad}(a_5)=\{3,17,83\}`
(§L.2). `a_9/13=332=2^2\cdot83`, `\mathrm{rad}(a_9)=\{2,13,83\}` (§L.2).
`a_{11}=4332`: `4332/4=1083=3\cdot361=3\cdot19^2` (`19^2=361`,
`3\times361=1083`), so `4332=2^2\cdot3\cdot19^2`,
`\mathrm{rad}(a_{11})=\{2,3,19\}`. `a_{12}=4352=2^8\cdot17` (`2^8=256`,
`256\times17=4352`), `\mathrm{rad}(a_{12})=\{2,17\}` (§L.2). `a_{92}=5967`:
`5967/17=351=3^3\cdot13` (`351=27\times13`; `27\times13=351`), so
`5967=3^3\cdot13\cdot17`, `\mathrm{rad}(a_{92})=\{3,13,17\}`.

**Note on the witness `a_{82}` (honest simplification of the round-14
outline).** The outline/explorer also proposed a seventh witness,
`a_{82}=5746=2\cdot13^2\cdot17` (`S=\{13,17\}`, `\mathrm{comp}=\{2\}`,
independently confirmed correct by the same generator). Working through
every one of the 6 channels below (§M.3) shows this witness is **not
needed**: `a_{82}` can only be applied against target class `I_{19}` (its
core `\{13,17\}` is disjoint only from `\{19\}` among the 6 relevant
classes), and it would force `2\mid a_k` for every `k\in I_{19}` — a fact
already, and more directly, supplied by `a_{12}` (core `\{17\}`, also
disjoint from `\{19\}`, `\mathrm{comp}(a_{12})=\{2\}`). So the closure
below uses exactly **6** witnesses (`a_2,a_5,a_9,a_{11},a_{12},a_{92}`),
one fewer than the outline proposed; `a_{82}`'s factorization is recorded
above only as a cross-check, not cited again.

**Exhaustiveness of the 6-channel enumeration.** `P_1=\{13,17,19\}` has
`2^3-1=7` nonempty subsets: `\{13\},\{17\},\{19\},\{13,17\},\{13,19\},
\{17,19\},\{13,17,19\}`. An unordered pair `\{A,B\}` of *distinct* such
subsets is either **intersecting** (`A\cap B\ne\varnothing`) or
**disjoint**. There are `\binom{7}{2}=21` unordered pairs of distinct
nonempty subsets in total. Direct hand enumeration of all 21:

- The top core `\{13,17,19\}`, paired with any of the other 6 subsets,
  always intersects it (every nonempty subset of a 3-element set meets the
  full set) — `6` intersecting pairs.
- Each of the 3 pair-cores `\{13,17\},\{13,19\},\{17,19\}`, paired with
  each of the OTHER two pair-cores, intersects (any two distinct 2-element
  subsets of a 3-element set share exactly one element) — `\binom{3}{2}=3`
  intersecting pairs.
- Each of the 3 pair-cores, paired with each of the 2 singleton cores it
  contains, intersects (e.g. `\{13,17\}\cap\{13\}=\{13\}\ne\varnothing`,
  `\{13,17\}\cap\{17\}=\{17\}\ne\varnothing`) — `3\times2=6` intersecting
  pairs.
- Each of the 3 pair-cores, paired with the ONE singleton core it does
  NOT contain, is **disjoint** (e.g. `\{13,17\}\cap\{19\}=\varnothing`) —
  exactly `3` disjoint pairs: `(\{19\},\{13,17\})`, `(\{13\},\{17,19\})`,
  `(\{17\},\{13,19\})`.
- Each pair of distinct singleton cores is **disjoint** (e.g.
  `\{13\}\cap\{17\}=\varnothing`) — `\binom{3}{2}=3` disjoint pairs:
  `(\{13\},\{17\})`, `(\{13\},\{19\})`, `(\{17\},\{19\})`.

Totals: `6+3+6=15` intersecting pairs, `3+3=6` disjoint pairs,
`15+6=21=\binom{7}{2}` — the count matches exactly, confirming the
enumeration is exhaustive with no double-count or omission. **The 6
disjoint unordered core pairs of `P_1=\{13,17,19\}` are exactly:**
`(\{13\},\{17\})`, `(\{13\},\{19\})`, `(\{17\},\{19\})`,
`(\{13\},\{17,19\})`, `(\{17\},\{13,19\})`, `(\{19\},\{13,17\})`. Channel
1, `(\{13\},\{17\})`, is already **Theorem FW1** (§L.2, certified,
`W=\{2,3,83\}`) — cited, not re-derived below. The other 5 are closed for
the first time in §M.3.

### M.2. Per-class disjunctive facts (Lemma WF applied to the 6 witnesses)

For each of the 6 proper (non-top) cores `S\in\{\{13\},\{17\},\{19\},
\{13,17\},\{13,19\},\{17,19\}\}`, we list every witness among the 6 above
whose core is disjoint from `S` (this is the *only* legitimate source of a
Lemma WF fact about `I_S`, by Lemma WF's own hypothesis), and the
resulting fact.

**`S=\{13\}`.** Witnesses with core disjoint from `\{13\}`: `a_5` (core
`\{17\}`, `\{17\}\cap\{13\}=\varnothing`) and `a_{12}` (core `\{17\}`,
same). By Lemma WF: every `i\in I_{13}` satisfies `3\mid a_i\vee83\mid
a_i` (from `a_5`, `\mathrm{comp}=\{3,83\}`) and `2\mid a_i` unconditionally
(from `a_{12}`, `\mathrm{comp}=\{2\}`, singleton). **[Fact `I_{13}`]:
`2` (unconditional) `\wedge(3\vee83)`.**

**`S=\{17\}`.** Witnesses with core disjoint from `\{17\}`: `a_2` (core
`\{13\}`) and `a_9` (core `\{13\}`). By Lemma WF: every `j\in I_{17}`
satisfies `2\mid a_j\vee3\mid a_j` (from `a_2`, `\mathrm{comp}=\{2,3\}`)
and `2\mid a_j\vee83\mid a_j` (from `a_9`, `\mathrm{comp}=\{2,83\}`).
**[Fact `I_{17}`]: `(2\vee3)\wedge(2\vee83)`.**

**`S=\{19\}`.** Witnesses with core disjoint from `\{19\}`: `a_2,a_5,a_9,
a_{12}` (cores `\{13\}` or `\{17\}`, both disjoint from `\{19\}`) and
`a_{92}` (core `\{13,17\}`, `\{13,17\}\cap\{19\}=\varnothing`). The two
sharpest (singleton) facts: `2\mid a_j` unconditionally (from `a_{12}`)
and `3\mid a_j` unconditionally (from `a_{92}`, `\mathrm{comp}(a_{92})=
\{3\}`, singleton). (`a_2,a_5,a_9` supply only the weaker disjunctions
`2\vee3`, `3\vee83`, `2\vee83` respectively, already implied by the two
unconditional facts, so are not needed here.) **[Fact `I_{19}`]: `2\wedge3`
(both unconditional) — the strongest of the 6.**

**`S=\{13,17\}`.** Witnesses with core disjoint from `\{13,17\}`: only
`a_{11}` (core `\{19\}`, `\{19\}\cap\{13,17\}=\varnothing`; no witness of
core `\{13\}` or `\{17\}` qualifies, since e.g. `\{13\}\cap\{13,17\}=
\{13\}\ne\varnothing`). By Lemma WF: every `k\in I_{\{13,17\}}` satisfies
`2\mid a_k\vee3\mid a_k` (from `a_{11}`, `\mathrm{comp}=\{2,3\}`). **[Fact
`I_{13,17}`]: `(2\vee3)` — the weakest of the 6 (only one witness
available).**

**`S=\{13,19\}`.** Witnesses with core disjoint from `\{13,19\}`: only
witnesses of core `\{17\}` qualify (`\{17\}\cap\{13,19\}=\varnothing`),
i.e. `a_5,a_{12}` — the identical pair used for `S=\{13\}` above. **[Fact
`I_{13,19}`]: `2` (unconditional, from `a_{12}`) `\wedge(3\vee83)` (from
`a_5`) — identical shape to `I_{13}`.**

**`S=\{17,19\}`.** Witnesses with core disjoint from `\{17,19\}`: only
witnesses of core `\{13\}` qualify, i.e. `a_2,a_9` — the identical pair
used for `S=\{17\}` above. **[Fact `I_{17,19}`]: `(2\vee3)\wedge(2\vee83)`
— identical shape to `I_{17}`.**

### M.3. Channel-by-channel closure: all 6 disjoint core-pair channels,
exhaustive case splits

**Channel 1: `(\{13\},\{17\})`.** Already **Theorem FW1** (§L.2,
certified): `W=\{2,3,83\}`. Not re-derived.

**Channel 2: `(\{13\},\{19\})`, `W=\{2\}`.**

*Claim.* For every `i\in I_{13},j\in I_{19}`, `\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)\cap\{2\}\ne\varnothing`.

*Proof.* By [Fact `I_{13}`], `2\mid a_i` unconditionally. By [Fact
`I_{19}`], `2\mid a_j` unconditionally. Hence `2\in\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)`. No case split is needed — both unconditional facts
give `2` directly. `\blacksquare`

**Channel 3: `(\{17\},\{19\})`, `W=\{2,3\}`.**

*Claim.* For every `i\in I_{17},j\in I_{19}`, `\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)\cap\{2,3\}\ne\varnothing`.

*Proof.* By [Fact `I_{19}`], `2\mid a_j` and `3\mid a_j`, both
unconditionally. By [Fact `I_{17}`], `2\mid a_i\vee3\mid a_i` (this is the
`(2\vee3)` half of the fact; the `(2\vee83)` half is not needed for this
channel). Two exhaustive cases on which disjunct holds for `i`: if `2\mid
a_i`, then since `2\mid a_j` too, `2` is a common factor; if `3\mid a_i`
(the only remaining possibility, since the disjunction is exhaustive),
then since `3\mid a_j` too, `3` is a common factor. Either way
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3\}\ne\varnothing`.
`\blacksquare`

**Channel 4: `(\{13\},\{17,19\})`, `W=\{2,3,83\}`.**

*Claim.* For every `i\in I_{13},j\in I_{17,19}`, `\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)\cap\{2,3,83\}\ne\varnothing`.

*Proof.* By [Fact `I_{13}`]: `2\mid a_i` unconditionally, and `3\mid
a_i\vee83\mid a_i`. By [Fact `I_{17,19}`] (identical shape to `I_{17}`):
`2\mid a_j\vee3\mid a_j`, and `2\mid a_j\vee83\mid a_j`. Two exhaustive
cases on `2\mid a_j`:

- **Case (a): `2\mid a_j`.** Since `2\mid a_i` unconditionally, `2` is a
  common factor.
- **Case (b): `2\nmid a_j`.** From `2\mid a_j\vee3\mid a_j`, since `2\nmid
  a_j`, `3\mid a_j`. From `2\mid a_j\vee83\mid a_j`, since `2\nmid a_j`,
  `83\mid a_j`. So `a_j` has both `3` and `83`. From `3\mid a_i\vee83\mid
  a_i`, whichever disjunct holds for `i` is also a factor of `a_j`
  (`a_j` has both), giving a common factor.

Both cases give `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,83\}\ne
\varnothing`. `\blacksquare`

**Channel 5: `(\{17\},\{13,19\})`, `W=\{2,3,83\}`.**

*Claim.* For every `i\in I_{17},j\in I_{13,19}`, `\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)\cap\{2,3,83\}\ne\varnothing`.

*Proof.* By [Fact `I_{17}`]: `2\mid a_i\vee3\mid a_i`, and `2\mid a_i\vee
83\mid a_i`. By [Fact `I_{13,19}`] (identical shape to `I_{13}`): `2\mid
a_j` unconditionally, and `3\mid a_j\vee83\mid a_j`. Two exhaustive cases
on `2\mid a_i` (note: this is the mirror image of Channel 4's case split,
with the roles of `i,j` swapped relative to which side has the
unconditional `2`):

- **Case (a): `2\mid a_i`.** Since `2\mid a_j` unconditionally, `2` is a
  common factor.
- **Case (b): `2\nmid a_i`.** From `2\mid a_i\vee3\mid a_i`, since `2\nmid
  a_i`, `3\mid a_i`. From `2\mid a_i\vee83\mid a_i`, since `2\nmid a_i`,
  `83\mid a_i`. So `a_i` has both `3` and `83`. From `3\mid a_j\vee83\mid
  a_j`, whichever disjunct holds for `j` is also a factor of `a_i`
  (`a_i` has both), giving a common factor.

Both cases give `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,83\}\ne
\varnothing`. `\blacksquare`

**Channel 6: `(\{19\},\{13,17\})`, `W=\{2,3\}`.**

*Claim.* For every `i\in I_{19},j\in I_{13,17}`, `\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)\cap\{2,3\}\ne\varnothing`.

*Proof.* By [Fact `I_{19}`], `2\mid a_i` and `3\mid a_i`, both
unconditionally. By [Fact `I_{13,17}`], `2\mid a_j\vee3\mid a_j`. Two
exhaustive cases on which disjunct holds for `j`: if `2\mid a_j`, then
since `2\mid a_i` too, `2` is a common factor; if `3\mid a_j`, then since
`3\mid a_i` too, `3` is a common factor. Either way `\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)\cap\{2,3\}\ne\varnothing`. `\blacksquare`

**Summary.** All 6 channels close under the single fixed set
`H_{\mathrm{extra}}:=\{2,3,83\}` (Channels 2, 3, 6 need only its subset
`\{2\}` or `\{2,3\}`; this does not affect the correctness of using the
uniform superset `\{2,3,83\}` for the final assembly in §M.4). This uses
exactly the 6 witnesses `a_2,a_5,a_9,a_{11},a_{12},a_{92}` (§M.1), each
applied only where its core is disjoint from the target class (verified
explicitly in §M.2 for every one of the 6 applications) — in particular
`a_2,a_9` (core `\{13\}`) are used **only** for `I_{17}` and `I_{17,19}`,
never for `I_{13,17}` or `I_{13,19}` (whose cores are not disjoint from
`\{13\}`); `a_5,a_{12}` (core `\{17\}`) are used **only** for `I_{13}` and
`I_{13,19}`, never for `I_{13,17}` or `I_{17,19}`; `a_{11}` (core
`\{19\}`) is used **only** for `I_{13,17}`; `a_{92}` (core `\{13,17\}`) is
used **only** for `I_{19}`.

### M.4. Corollary FW1-FCBC: `a_1=4199` is a fully solved concrete instance

**Statement.** For `a_1=4199`, `H:=P_1\cup\{2,3,83\}=\{2,3,13,17,19,83\}`
satisfies FCBC: `H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing`
for every `1\le i<j`.

**Proof.** Fix `1\le i<j`. By Theorem CD, `S(i),S(j)` are well-defined,
nonempty subsets of `P_1=\{13,17,19\}`. Two exhaustive cases:

- **`S(i)\cap S(j)\ne\varnothing`**: by Lemma SW1, some prime of
  `S(i)\cap S(j)\subseteq P_1\subseteq H` lies in `\mathrm{rad}(a_i)\cap
  \mathrm{rad}(a_j)`.
- **`S(i)\cap S(j)=\varnothing`**: by the exhaustiveness argument of §M.1,
  `\{S(i),S(j)\}` is (up to swapping `i,j`) one of the 6 disjoint pairs
  enumerated there, i.e. one of the 6 channels closed in §M.3. Each
  channel's closure gives `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap
  \{2,3,83\}\ne\varnothing` (Channel 1 via the already-certified Theorem
  FW1; Channels 2–6 via §M.3), and `\{2,3,83\}\subseteq H`.

Both cases give `H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne
\varnothing`. `\blacksquare`

**Consequence.** By the already-certified Theorem 5.1
(`lemmas/theorem-5.1-master-conditional-theorem.md`, hypothesis `(†')` =
FCBC), there exist explicit positive integers `T=|\mathrm{Good}|`,
`L=\mathrm{lcm}(2,3,13,17,19,83)=2{,}091{,}102`, with `a_{n+T}=a_n+L` for
**every** `n\ge1`. This is a complete, unconditional proof of the IMO
problem's conclusion for the specific instance `a_1=4199` — a second
fully solved concrete instance (after `a_1=247`, §L.4), larger in the
sense that `|P_1|=3` gives 6 disjoint core-pair channels (all now closed)
rather than `247`'s single channel. It does NOT prove the general problem
(open for arbitrary `a_1`).

*(Numeric note, not part of the proof: `\mathrm{lcm}(2,3,13,17,19,83)`.
All six primes distinct, so the lcm is their product: `2\cdot3=6`,
`6\cdot13=78`, `78\cdot17=1326` (`78\times17=78\times10+78\times7=
780+546=1326`), `1326\cdot19=25{,}194` (`1326\times19=1326\times20-1326=
26{,}520-1{,}326=25{,}194`), `25{,}194\cdot83=2{,}091{,}102`
(`25{,}194\times83=25{,}194\times80+25{,}194\times3=2{,}015{,}520+
75{,}582=2{,}091{,}102`).)*

### M.5. Independent numerical verification (supporting, not part of the
proof)

Re-generated `a_1=4199` to `n=12{,}000` terms with a freshly-written,
efficient generator (own sieve-based factorization, independent of any
prior round's script) implementing the problem's literal recursive rule.
Class sizes at this depth: `|I_{13}|=2791`, `|I_{17}|=6156`,
`|I_{19}|=1816`, `|I_{13,17}|=681`, `|I_{13,19}|=156`, `|I_{17,19}|=343`,
`|I_{13,17,19}|=57` (top core). For each of the 6 channels, enumerated
the complete set of realized `\mathrm{rad}(\cdot)\cap\{2,3,83\}`
signatures on each side and checked every pair of realized signatures
intersects — **zero violations on all 6 channels**, and the realized
signature sets match the hand-derived facts of §M.2 exactly:

- `I_{13}` signatures: `\{2,3\},\{2,83\},\{2,3,83\}` — all contain `2`,
  matching `2\wedge(3\vee83)`.
- `I_{17}` signatures: `\{2\},\{3,83\},\{2,3\},\{2,3,83\},\{2,83\}` —
  every one contains `2` or contains both `3,83`, matching
  `(2\vee3)\wedge(2\vee83)`.
- `I_{19}` signatures: `\{2,3\},\{2,3,83\}` — both contain `2` **and**
  `3`, matching the strongest fact `2\wedge3`.
- `I_{13,19}` signatures: `\{2,3\},\{2,3,83\}` — identical to `I_{13}`'s
  shape (both contain `2`), matching the predicted identical shape.
- `I_{17,19}` signatures: `\{2\},\{3,83\},\{2,3\},\{2,3,83\},\{2,83\}` —
  identical to `I_{17}`'s shape, matching the predicted identical shape.
- `I_{13,17}` signatures: `\{2\},\{2,3\},\{3,83\},\{2,3,83\},\{2,83\},
  \{3\}` — every one contains `2` or `3`, matching `(2\vee3)`.

This matches the hand proof (§M.2–M.3) exactly on every point and is
offered only as a sanity check, not as a substitute for the proof.

## §N. Corollary CRR (Common-Recruiter Reuse) and closure of 4 more
disjoint core-pair channels of `a_1=21528751` (Round 15)

### N.0. Tools imported (already certified, cited verbatim, not re-proved)

**Corollary P″** (unordered Lemma P′), **Theorem CD** (core decomposition,
total and nonempty core map), **Lemma XC** (for disjoint cores `S,S'`,
`\mathrm{rad}(a_k)\cap\mathrm{rad}(a_{i_0})=\mathrm{comp}(a_k)\cap
\mathrm{comp}(a_{i_0})`), **Lemma SW1/Theorem SW**
(`lemmas/theorem-SW-stabilization-sufficiency.md`), **Theorem 5.1**
(`lemmas/theorem-5.1-master-conditional-theorem.md`), **Lemma WF (Witness
Forcing)** and **Corollary MSF (Multi-Singleton Forcing)**, both certified
in `lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md` and
`lemmas/corollary-MSF-multi-singleton-forcing.md` respectively, and the
**Permanent Bundle Lemma** (`lemmas/lemma-permanent-bundle.md`). Lemma WF's
exact certified statement, quoted verbatim (this is the only fact Corollary
CRR needs):

> Fix disjoint nonempty cores `S,S'\subseteq P_1` and a fixed index `i_0`
> with `S(i_0)=S'`. Then for **every** `k\in I_S` (no restriction on `k`
> relative to `i_0`), `\mathrm{comp}(a_k)\cap\mathrm{comp}(a_{i_0})\ne
> \varnothing`. If `\mathrm{comp}(a_{i_0})=\{q_1,\dots,q_r\}`, every `k\in
> I_S` satisfies `q_1\mid a_k\vee\dots\vee q_r\mid a_k`; if `r=1` this is
> unconditional.

### N.1. Corollary CRR (Common-Recruiter Reuse): statement and proof

**Statement.** Fix a sequence satisfying the problem's hypotheses,
`P_1:=\mathrm{rad}(a_1)`, and a fixed index `i_0` with core
`S(i_0)=:S'\ne\varnothing` (well-defined by Theorem CD). Then, for
**every** nonempty `S\subseteq P_1` with `S\cap S'=\varnothing` — not just
one particular `S` the witness `i_0` may originally have been chosen to
target — the conclusion of Lemma WF holds verbatim: for every `k\in I_S`,
`\mathrm{comp}(a_k)\cap\mathrm{comp}(a_{i_0})\ne\varnothing` (with the
sharper singleton/unconditional form when `|\mathrm{comp}(a_{i_0})|=1`).
Equivalently: once a witness `i_0` and its exact companion set
`\mathrm{comp}(a_{i_0})` are on file, that single witness is simultaneously
valid, at no extra cost, against **every** target core disjoint from
`S(i_0)`, not merely the one target the discoverer had in mind.

**Proof.** Fix any nonempty `S\subseteq P_1` with `S\cap S'=\varnothing`
and any `k\in I_S`. Lemma WF, as certified, has hypothesis exactly "`S,S'`
disjoint nonempty cores `\subseteq P_1`, `i_0` a fixed index with
`S(i_0)=S'`" — this hypothesis is satisfied by our chosen `S` (disjointness
from `S'` is assumed, nonemptiness is assumed, and `i_0` is unchanged from
whatever witness search originally produced it). Re-examine Lemma WF's own
proof (`lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`): it
uses only (a) `k\ne i_0` (from `S(k)=S\ne S'=S(i_0)`, valid for our `S`
since `S\ne S'` as they are disjoint and nonempty), (b) Corollary P″,
`\gcd(a_k,a_{i_0})>1` — a fact depending on `k,i_0` alone, not on `S`, (c)
Lemma XC applied to the disjoint pair `S(k)=S,\ S(i_0)=S'` — valid because
`S,S'` are disjoint, which is exactly our hypothesis on the new `S`. None
of the three ingredients references any property of `S` beyond
"`S\ne\varnothing`, `S\cap S'=\varnothing`, `S\subseteq P_1`" — precisely
the hypothesis re-verified above for our arbitrary choice of `S`. Hence the
identical proof (verbatim, symbol for symbol) establishes the claim for
this `S`. Since `S` was an arbitrary nonempty subset of `P_1` disjoint from
`S'`, the conclusion holds for **every** such `S` simultaneously, using the
same fixed `i_0`. `\blacksquare`

**Remark (why this needed stating, despite being a one-line proof).**
Lemma WF's certified statement already universally quantifies over `S`; no
new mathematics is added by Corollary CRR. What it adds is a *named,
reusable bookkeeping fact*: once a witness closing one disjoint core pair
`(S_0,S')` is on file with its companion set exactly computed, checking
whether it *also* closes some other pair `(S_1,S')` (`S_1\ne S_0`, both
disjoint from `S'`) requires **zero new search or computation** — only
re-reading Lemma WF's hypothesis against the new target. This is the
"Common-Recruiter Reuse" mechanism identified independently by two of this
round's math-explorers.

### N.2. Setup for `a_1=21528751`: witnesses, factorizations, exhaustiveness

`a_1=21{,}528{,}751=103\times197\times1061` (hand check: `103\times197=
20{,}291`; `20{,}291\times1061=20{,}291\times1000+20{,}291\times61=
20{,}291{,}000+1{,}237{,}751=21{,}528{,}751`, using `20{,}291\times61=
20{,}291\times60+20{,}291=1{,}217{,}460+20{,}291=1{,}237{,}751`). So
`P_1=\{103,197,1061\}`, `k=|P_1|=3`.

**Witnesses used below (all four already on file from Corollary MSF's
round-14 closure of channel `(\{197\},\{103\})`,
`lemmas/corollary-MSF-multi-singleton-forcing.md`; factorizations
independently re-derived here both by hand and by a freshly-written
sieve-based generator implementing the problem's literal recursive rule,
cross-checked against `sympy.factorint`, exact agreement):**

```
a_1405  = 21,727,232 = 2^11 · 103^2     core={103}   comp={2}
a_11812 = 23,201,883 = 3^7  · 103^2     core={103}   comp={3}
a_27832 = 25,472,209 = 7^4  · 103^2     core={103}   comp={7}
a_2575  = 21,893,004 = 2^2·3^4·7^3·197  core={197}   comp={2,3,7}
```

*Hand verification of each factorization.* `2^{11}=2048`, `103^2=10{,}609`,
`2048\times10{,}609=2048\times10{,}000+2048\times609=20{,}480{,}000+
1{,}247{,}232=21{,}727{,}232` (`2048\times609=2048\times600+2048\times9=
1{,}228{,}800+18{,}432=1{,}247{,}232`) — matches `a_{1405}`. `3^7=2187`,
`2187\times10{,}609=2187\times10{,}000+2187\times609=21{,}870{,}000+
1{,}331{,}883=23{,}201{,}883` (`2187\times609=2187\times600+2187\times9=
1{,}312{,}200+19{,}683=1{,}331{,}883`) — matches `a_{11812}`. `7^4=2401`,
`2401\times10{,}609=2401\times10{,}000+2401\times609=24{,}010{,}000+
1{,}462{,}209=25{,}472{,}209` (`2401\times609=2401\times600+2401\times9=
1{,}440{,}600+21{,}609=1{,}462{,}209`) — matches `a_{27832}`. `2^2\cdot
3^4\cdot7^3=4\times81\times343=324\times343=97{,}200+13{,}932=111{,}132`
(`324\times343=324\times300+324\times43`), and `111{,}132\times197=
111{,}132\times200-111{,}132\times3=22{,}226{,}400-333{,}396=21{,}893{,}004`
— matches `a_{2575}`. Independently confirmed with `sympy.factorint` this
round (fresh check, not copied): all four factorizations reproduce exactly
as listed, and `\mathrm{rad}(a_{1405})=\{2,103\}`,
`\mathrm{rad}(a_{11812})=\{3,103\}`, `\mathrm{rad}(a_{27832})=\{7,103\}`,
`\mathrm{rad}(a_{2575})=\{2,3,7,197\}` — giving `\mathrm{core}=\{103\}`
(resp. `\{197\}`) and `\mathrm{comp}` exactly as tabulated, since
`103,197\notin\{2,3,7\}` and `\{2,3,7\}\cap P_1=\varnothing`.

**Exhaustiveness of the 6-channel enumeration.** Identical template to
§M.1. `P_1=\{103,197,1061\}` has `2^3-1=7` nonempty subsets:
`\{103\},\{197\},\{1061\},\{103,197\},\{103,1061\},\{197,1061\},
\{103,197,1061\}`. There are `\binom{7}{2}=21` unordered pairs of distinct
such subsets. Direct hand enumeration (identical structure to §M.1's,
since both `P_1`'s have size 3): the top core paired with any other subset
always intersects (`6` pairs); each of the 3 pair-cores paired with either
of the other 2 pair-cores intersects (`3` pairs); each pair-core paired
with either singleton core it contains intersects (`3\times2=6` pairs);
each pair-core paired with the ONE singleton it does not contain is
disjoint (`3` pairs: `(\{1061\},\{103,197\})`, `(\{197\},\{103,1061\})`,
`(\{103\},\{197,1061\})`); each pair of distinct singleton cores is
disjoint (`\binom32=3` pairs: `(\{103\},\{197\})`, `(\{103\},\{1061\})`,
`(\{197\},\{1061\})`). Totals: `6+3+6=15` intersecting, `3+3=6` disjoint,
`15+6=21=\binom72` — matches exactly. **The 6 disjoint unordered core pairs
of `P_1=\{103,197,1061\}` are exactly:** `(\{103\},\{197\})`,
`(\{103\},\{1061\})`, `(\{197\},\{1061\})`, `(\{103\},\{197,1061\})`,
`(\{197\},\{103,1061\})`, `(\{1061\},\{103,197\})`. Channel
`(\{103\},\{197\})` is already closed by the certified **Corollary MSF**
(round 14, `P=\{2,3,7\}`) — cited, not re-derived below. The other 5 are
addressed in §N.3–N.4.

### N.3. Per-class facts via Corollary CRR

Corollary CRR lets us re-aim the 4 already-on-file witnesses at **every**
core disjoint from their own core, not only `\{197\}`/`\{103\}`.

**Witnesses of core `\{103\}` (`a_{1405},a_{11812},a_{27832}`, singleton
comps `2,3,7`).** Cores disjoint from `\{103\}`: `\{197\}`, `\{1061\}`,
`\{197,1061\}` (the 3 nonempty subsets of `P_1` not containing `103`). By
Corollary CRR (three independent applications of Lemma WF, one per
witness, each unconditional since each companion set is a singleton):

**[Fact A]** for every `k\in I_{197}\cup I_{1061}\cup I_{197,1061}`:
`2\mid a_k`, `3\mid a_k`, and `7\mid a_k`, i.e. `\{2,3,7\}\subseteq
\mathrm{comp}(a_k)` (full containment, unconditional, no disjunction).

**Witness of core `\{197\}` (`a_{2575}`, `\mathrm{comp}=\{2,3,7\}`, not a
singleton).** Cores disjoint from `\{197\}`: `\{103\}`, `\{1061\}`,
`\{103,1061\}`. By Corollary CRR (one application of Lemma WF's disjunctive
Corollary, `r=3`):

**[Fact B]** for every `k\in I_{103}\cup I_{1061}\cup I_{103,1061}`:
`2\mid a_k\vee3\mid a_k\vee7\mid a_k`, i.e. `\mathrm{comp}(a_k)\cap
\{2,3,7\}\ne\varnothing`.

### N.4. Channel-by-channel closure of the 4 new channels, `W=\{2,3,7\}`
throughout

**Channel `(\{103\},\{1061\})`.** *Claim.* For every `i\in I_{103},
j\in I_{1061}`, `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,7\}\ne
\varnothing`. *Proof.* `I_{1061}\subseteq` the union in [Fact A] (since
`\{1061\}` is disjoint from `\{103\}`), so `\{2,3,7\}\subseteq
\mathrm{comp}(a_j)`. `I_{103}\subseteq` the union in [Fact B] (since
`\{103\}` is disjoint from `\{197\}`), so `\mathrm{comp}(a_i)\cap
\{2,3,7\}\ne\varnothing`; pick `q\in\mathrm{comp}(a_i)\cap\{2,3,7\}`. Since
`\{2,3,7\}\subseteq\mathrm{comp}(a_j)`, `q\in\mathrm{comp}(a_j)` too. Hence
`q\in\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap\{2,3,7\}\subseteq
\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,7\}`. `\blacksquare`

**Channel `(\{197\},\{1061\})`.** *Claim.* For every `i\in I_{197},
j\in I_{1061}`, `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,7\}\ne
\varnothing`. *Proof.* Both `\{197\}` and `\{1061\}` are disjoint from
`\{103\}`, so both are covered by [Fact A]: `\{2,3,7\}\subseteq
\mathrm{comp}(a_i)` **and** `\{2,3,7\}\subseteq\mathrm{comp}(a_j)`. In
particular `2\in\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)`. No case split
is needed — this is the cleanest of the 4 channels, both sides fully
determined by the same witness triple. `\blacksquare`

**Channel `(\{103\},\{197,1061\})`.** *Claim.* For every `i\in I_{103},
j\in I_{197,1061}`, `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,7\}\ne
\varnothing`. *Proof.* `\{197,1061\}` is disjoint from `\{103\}`
(`\{197,1061\}\cap\{103\}=\varnothing`), so `j\in I_{197,1061}` is covered
by [Fact A]: `\{2,3,7\}\subseteq\mathrm{comp}(a_j)`. `\{103\}` is disjoint
from `\{197\}`, so `i\in I_{103}` is covered by [Fact B]:
`\mathrm{comp}(a_i)\cap\{2,3,7\}\ne\varnothing`; pick `q` in this
intersection. Since `\{2,3,7\}\subseteq\mathrm{comp}(a_j)`, `q\in
\mathrm{comp}(a_j)` too, giving the common factor. `\blacksquare`

**Channel `(\{197\},\{103,1061\})`.** *Claim.* For every `i\in I_{197},
j\in I_{103,1061}`, `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,7\}\ne
\varnothing`. *Proof.* `\{197\}` is disjoint from `\{103\}`
(`\{197\}\cap\{103\}=\varnothing`), so `i\in I_{197}` is covered by [Fact
A]: `\{2,3,7\}\subseteq\mathrm{comp}(a_i)`. `\{103,1061\}` is disjoint from
`\{197\}` (`\{103,1061\}\cap\{197\}=\varnothing`), so `j\in I_{103,1061}`
is covered by [Fact B]: `\mathrm{comp}(a_j)\cap\{2,3,7\}\ne\varnothing`;
pick `q` in this intersection. Since `\{2,3,7\}\subseteq\mathrm{comp}
(a_i)`, `q\in\mathrm{comp}(a_i)` too, giving the common factor.
`\blacksquare`

**Summary.** All 4 new channels close under the identical `W=\{2,3,7\}`
already certified for channel `(\{103\},\{197\})` (Corollary MSF) — no new
witness search, no new factorization beyond the 4 already on file. Combined
with Corollary MSF's channel, `a_1=21528751` now has **5 of its 6
disjoint core-pair channels closed**: `(\{103\},\{197\})` (Corollary MSF),
`(\{103\},\{1061\})`, `(\{197\},\{1061\})`, `(\{103\},\{197,1061\})`,
`(\{197\},\{103,1061\})` (all four via §N.4 above).

### N.5. Independent numerical verification (supporting, not part of the
proof)

Wrote a fresh generator (own trial-division-based factorization, an
independent implementation from any prior round's script, checked against
`sympy.factorint` on the 4 witnesses above) implementing the problem's
literal recursive rule, and ran it to `n=30{,}000` (87.8s runtime, this
round, not reused from any prior cache). Class sizes at this depth:
`|I_{103}|=29{,}301`, `|I_{197}|=509`, `|I_{1061}|=10`,
`|I_{103,197}|=152`, `|I_{103,1061}|=27`, `|I_{197,1061}|=0` (not yet
populated at this depth — no violation possible, vacuous), `|I_{P_1}|=1`.
Checked, over all `519` indices with core disjoint from `\{103\}`
(`I_{197}\cup I_{1061}\cup I_{197,1061}`), whether `\{2,3,7\}\subseteq
\mathrm{comp}(a_k)` ([Fact A]'s prediction): **zero violations** (519/519).
Checked, over all `29{,}338` indices with core disjoint from `\{197\}`
(`I_{103}\cup I_{1061}\cup I_{103,1061}`), whether `\mathrm{comp}(a_k)\cap
\{2,3,7\}\ne\varnothing` ([Fact B]'s prediction): **zero violations**
(29,338/29,338). This matches [Fact A]/[Fact B] exactly and is consistent
with, though independent of (own generator, own run, smaller `N` than, but
not copied from, the round-15 explorer's `N=100{,}000` check reported in
`/tmp/round-15/math-explorer-alternative-mechanism.md`), the explorer's own
finding. Offered only as a sanity check, not as a substitute for the §N.4
proof, which uses only certified facts and holds for the entire infinite
classes regardless of any finite-`N` check.

### N.6. Channel 6, `(\{1061\},\{103,197\})`: honestly scoped, NOT closed

**Why Corollary CRR cannot reach this channel.** Corollary CRR (and the
underlying Lemma WF) requires the two witnesses' cores (`\{103\}`,
`\{197\}`) to each be disjoint from the *target* core being constrained.
The target core `\{103,197\}` intersects **both** `\{103\}`
(`\{103,197\}\cap\{103\}=\{103\}\ne\varnothing`) and `\{197\}`
(`\{103,197\}\cap\{197\}=\{197\}\ne\varnothing`) — so neither of the two
witness families can legally be aimed at `I_{103,197}` via Lemma WF at all;
this is not a matter of insufficient search, but a structural mismatch of
Lemma WF's own hypothesis. The only core disjoint from `\{103,197\}` is
`\{1061\}` itself — so the only legitimate source of a Lemma WF fact about
`I_{103,197}` would be a witness of core `\{1061\}`, and symmetrically the
only legitimate source of a fact about `I_{1061}` (from the other
direction) would again have to come from a witness of core `\{103,197\}`.
No such singleton-companion witness is known or (per the round-15
explorer's search and this round's independent check below) exists at
small index.

**Fresh evidence this round that the escape structure resists a simple
fixed `W`.** Over the `152` members of `I_{103,197}` found up to
`n=30{,}000` (own independent generation, §N.5), exactly `2` have
`\mathrm{comp}(a_k)\cap\{2,3,7\}=\varnothing` (an "escape" from the
`\{2,3,7\}`-floor): one has `\mathrm{comp}=\{11,97\}` — this is exactly
the bundle `Q=\{11,97\}` whose permanence for `S=\{103,197\}` is already
**rigorously certified** by the Permanent Bundle Lemma
(`lemmas/lemma-permanent-bundle.md`: once realized, `S\cup Q` can never be
dominated) — but the other has `\mathrm{comp}=\{11,5,23\}`, a **different**
escape pattern, sharing only the prime `11` with the first, and not
addressed by the certified Permanent Bundle Lemma instance at all (that
lemma proves permanence of the *specific* bundle `\{11,97\}`; it makes no
claim that `\{11,97\}` is the *only* bundle by which `I_{103,197}` can
escape `\{2,3,7\}`). This is independent, fresh confirmation — not a
repetition of a prior round's finding — that `I_{103,197}`'s escape
structure is not known to be captured by a single bundle: even the
candidate `W=\{2,3,7,11,97\}` floated in the round-15 outline (step 4a)
is **not established** to close this channel, since a second, structurally
different escape (`\{11,5,23\}`) already exists at `n\le30{,}000` and there
is no proof (only these two data points) that no third, further-different
escape bundle exists at higher index — precisely the open Multi-Companion
Escape-Completeness question already flagged as equi-hard to `(MRS_S)`
for this exact core in prior rounds. Symmetrically, `I_{1061}` (`10`
members at this depth) has minimum `|\mathrm{comp}|=4`, every member's
`\mathrm{comp}\supseteq\{2,3,7\}` plus one or two further primes that vary
across members (`11,17,13,19,23,47`, and once `97` alone without `11`,
`\mathrm{comp}=\{2,3,5,7,97\}`) — so no singleton-companion witness of
core `\{1061\}` is available at this depth either, matching the round-15
explorer's independent finding verbatim.

**Conclusion (honest scope, per this round's dispatch): channel 6 is NOT
claimed closed.** It is the sole remaining open channel of
`a_1=21528751`; closing it (if possible at all) would require either (a) a
complete resolution of `I_{103,197}`'s (or symmetrically `I_{1061}`'s)
escape-bundle structure — i.e., a proof that only finitely many bundles
can ever occur, which is exactly this workspace's long-standing open
`(MRS_S)`/Multi-Companion-Escape-Completeness question, not resolved by
this round's mechanism — or (b) a structurally different technique
entirely. **`a_1=21528751` therefore remains an open instance (5 of 6
channels closed, not a fully solved concrete instance of the whole IMO
problem)**, in contrast to `a_1=247` and `a_1=4199`, which are fully
closed. This is a strict, honest narrowing of the instance's open content
to one precisely identified channel — a genuine improvement over the
prior round's state (only 1 of 6 channels closed) — but not a full
closure, and is reported as such.

## Round 12 Outline (proof-outliner directive — pivot away from stuck
`(MRS_S)`-for-`\{103,197\}`; contribute the Local No-Resurrection/
Interval/Equivalence toolkit to Backbone Permanence for "Case B" pairs, a
second, independent mechanism alongside `sunflower-bundle-closure`)

**Target (unchanged): the whole problem**, via Theorem SW → Theorem 5.1
(both already certified, do not re-derive). **Pivot away from direct
`(MRS_S)`-for-`\{103,197\}` as this approach's headline target.** This
round's mrs-s-scoped explorer (`/tmp/round-12/math-explorer-mrs-s-
scoped.md`) pushed the local antichain-freeze simulation to `n=10^7`
(`~100`x past the already-known freeze index `n=101957`, `10`x the
mandate), found ZERO further changes, and explicitly confirmed this gives
**no new leverage** beyond the already-certified No-Shortcut Corollary
(round 11: `(MRS_S)` for this concrete core is equi-hard to the
already-abandoned Multi-Companion hitting-set target). Per this round's
dispatch, do not build further around that specific finding — treat
direct `(MRS_S)`-for-`\{103,197\}` pursuit as a recorded dead line for
now (the No-Shortcut Corollary itself remains valid, certified content;
only *further* direct attack on closing `(MRS_S)` for this instance is
discouraged).

**Pivot target (new this round): contribute this approach's own
certified single-family machinery — the Local No-Resurrection Lemma,
Local Interval Lemma, and Local Equivalence Theorem (all §J, round 11,
unconditional, reusable) — to the Backbone Permanence Lemma needed for
"Case B" doubly-infinite pairs** (this round's jw-rigidity explorer's
new opening, see `sunflower-bundle-closure`'s and `sunflower-
inadmissibility-toolkit`'s Round 12 Outlines for the full context). This
is a SECOND, independently-derived route to the same open content as
`sunflower-bundle-closure`'s Case-B target, via a genuinely different
technique (poset/first-occurrence/interval-lemma machinery here, vs.
`sunflower-bundle-closure`'s trace-clash/NIDF-pigeonhole machinery) — the
population's most concrete near-term target this round, worth two rival
mechanisms since it is the harder residual (only 2/7 tested pairs, but
the general remaining case for any pair lacking a backbone).

**Key insight enabling the pivot (from this round's two explorers'
explicit joint diagnosis).** Backbone Permanence
(`\bigcap_{j\in I_{S'}}\mathrm{comp}(a_j)` stabilizes and is never
shrunk again by a later class member) is a STRICTLY WEAKER,
single-class-scoped statement than `(MRS_S)` (full local
minimal-radical-antichain freeze) — the No-Shortcut Corollary's
equi-hardness proof is specifically about the FULL antichain object
`\mathcal V_S^{\mathrm{loc}}`, and does not touch this coarser
running-intersection object (both this round's mrs-s-scoped and
jw-rigidity explorers independently flag Backbone Permanence as "a much
more elementary intersection-never-shrinks-again statement," explicitly
NOT to be conflated with `(MRS_S)`). This means the already-built **Local
No-Resurrection Lemma** (proves: a locally-minimal radical value, once
dropped from the class-restricted antichain `\mathcal M_n^S`, never
resurfaces) is a natural, not-yet-tried tool to adapt to a DIFFERENT,
coarser target object.

**Technique:** adapt the Local No-Resurrection Lemma's proof (§J Step 1
below, cite the exact mechanism: it restricts the competitor pool to
`I_S` itself, a self-contained argument needing no cross-family
reasoning) to the running-intersection sequence `B_k` (defined identically
to `sunflower-inadmissibility-toolkit`'s Round 12 Outline Step 1 — SHARED
DEFINITION, cite that file, do not redefine independently) instead of the
full antichain `\mathcal M_n^S`.

**Skeleton:**
1. **Restate Backbone Permanence Lemma precisely** — identical statement
   to `sunflower-inadmissibility-toolkit`'s Round 12 Outline Step 2 (a
   SHARED TARGET between the two approaches; cite that file's exact
   statement, do not re-derive independently — only the proof TECHNIQUE
   differs).
2. **Attempt the Backbone-to-Antichain Bridge** (the genuinely new,
   open content this round). The Local No-Resurrection Lemma's argument
   crucially uses MINIMALITY of the antichain member (an extremal
   property: `j`'s radical is locally minimal among `I_S\cap[1,n]`);
   `B_k` is NOT itself a minimal radical value, it is an intersection —
   so the direct transplant is not immediate. Open task: find the right
   extremal reformulation, e.g. does `B(S')`'s stabilization value equal
   the radical (or companion set) of some ACTUAL locally-minimal antichain
   element at index `k_0`, i.e. is there a bridge lemma connecting
   "running intersection freezes" to "coincides with a genuine locally-
   minimal antichain member" that would let Local No-Resurrection apply
   directly? **Cheap sanity check to run FIRST** (before attempting the
   general proof): does `B_k`'s stabilization index empirically coincide
   with (or closely track) this approach's own already-computed local
   antichain freeze indices, on the instances where both are computable?
   If yes, this is concrete evidence for the bridge; if the two indices
   diverge substantially, report that as a genuine negative finding
   against this route.
3. **If Step 2's bridge exists**, apply the Local Interval Lemma / Local
   Equivalence Theorem machinery (§J Steps 3–4, cite, do not re-derive)
   to conclude Backbone Permanence in full.
4. **Combine with sibling's Lemma UCR** (`sunflower-inadmissibility-
   toolkit` §1, cite, do not re-derive) exactly as in that file's Round
   12 Outline Step 3, to close (JW) for whichever Case-B pair this route
   succeeds on.

**Key lemmas (claim + mechanism):**
- **Local No-Resurrection Lemma** (already certified, §J Step 1 below) —
  restated as the source technique; its exact hypothesis (competitor
  pool restricted to `I_S`, well-ordering on realization index) is why it
  is a plausible transplant target for a single-class object like `B_k`.
- **Backbone-to-Antichain Bridge (Step 2, new, open)** — conjectured
  because `B_k`'s stabilization empirically coincides with the same
  general index range as this approach's own local antichain freeze
  computations in the instances checked so far (worth the builder's
  first-pass numerical check, cheap, before attempting the proof) — NOT
  yet proved, flagged honestly as speculative; if it turns out the
  extremal argument fundamentally cannot transfer to a non-extremal
  object like `B_k`, report this as a clean negative finding, do not
  force it.

**Open gaps:** the Backbone-to-Antichain Bridge (Step 2) is the crux,
genuinely new, unproved; Steps 3–4 are conditional on Step 2.

**Cases to cover:** Case B pairs specifically (`247:(13,19)`,
`4199:(13,17)`) — same scope as sibling `sunflower-bundle-closure`,
deliberately a second rival mechanism for the same hard residual, not a
duplicate of the whole-problem target.

**Watch out for:** do NOT silently re-attempt `(MRS_S)`-for-`\{103,197\}`
under a new name — the No-Shortcut Corollary stands, unrefuted,
re-confirmed this round by mrs-s-scoped's `n=10^7` push; Backbone
Permanence is a DIFFERENT, weaker object and must be kept explicitly
distinct in the write-up (both this round's explorers independently
stress this point — do not let it blur). Also: if Step 2's bridge fails
to materialize within this round, this is legitimate, reportable open
content — do not force a false analogy just to show progress.

## Round 12 update (headline — read this first)

**Scope correction from the outline-reviewer, confirmed by fresh
independent computation before any proof attempt (per the dispatch's
mandatory Step (a)).** The Round 12 Outline above (as originally drafted)
proposed applying the Backbone-to-Antichain Bridge to "Case B" pairs
generally, including `247:(13,19)`. This is wrong: `247:(13,19)` has
**no nonempty backbone on either side** — I independently re-verified this
from scratch (own generator, own factorization sieve, not reusing any
builder/explorer script), confirming the outline-reviewer's finding: both
the `\{13\}`-class and the `\{19\}`-class of `a_1=247` have running
companion-intersection `=\varnothing`, collapsing already at the 2nd
realized class member. Since the entire mechanism this approach owns
(Backbone Permanence + Lemma UCR) needs a **nonempty**, exactly-realized
class intersection to supply the set `C` in Lemma UCR (`C` nonempty is
part of Lemma UCR's hypothesis, `lemmas/lemma-UCR-universal-class-
realization.md`), it is **structurally vacuous** for `247:(13,19)` — not a
hard instance of this mechanism, but outside its domain of applicability
entirely. Per the dispatch, `247:(13,19)` is ceded in full to
`sunflower-bundle-closure` this round; it is not attempted here.

**Live target this round, per the dispatch: `a_1=4199`'s pair
`(S,S')=(\{13\},\{17\})`, specifically whether the `\{13\}`-side's
nonempty (but not-yet-exactly-realized) backbone `\{2\}` can still be
leveraged.** §K below gives the full, independent verification and the
complete rigorous analysis. **Headline finding: it cannot — and this is
now a *proved*, not merely empirical, negative result, covering *both*
sides of the pair, via a short direct argument from the already-certified
Lemma ERD-C (`lemmas/lemma-ERD-realized-blocked-dichotomy.md`) and a new
general-purpose Sandwich Uniqueness Lemma (§K, Step 1, proposed for
certification) that pins down, for any doubly-infinite pair, exactly what
the Realized-Backbone/UCR mechanism requires and shows the requirement is
an all-or-nothing dichotomy needing no unproven Backbone Permanence
hypothesis to evaluate.** Concretely: the `\{17\}`-side's true full class
intersection is proved `=\varnothing` outright (two concrete companion
sets, `\{2,31\}` and `\{3,83\}`, already disjoint — no asymptotic
verification needed, and no further class member can undo a disjointness
already witnessed). The `\{13\}`-side is handled by an exhaustive
case-split that needs no resolution of whether its running intersection
stays at `\{2\}` forever or shrinks further: either way, the mechanism
fails (Step 3 below). **This is a clean, honestly negative but fully
rigorous finding for this specific mechanism on this specific pair — not
a stall, and not an overclaim** — exactly what the dispatch asked for if
the constructive route did not materialize. It does not threaten any
certified content (Lemma UCR, Corollary UCR-JW, the Local No-
Resurrection/Interval/Equivalence Theorem, the Subset Lemma, or the
No-Shortcut Corollary all remain valid and untouched), nor does it affect
`sunflower-inadmissibility-toolkit`'s Case A mechanism (which targets a
disjoint set of 5 pairs where the backbone genuinely is both nonempty and
apparently realized) or `sunflower-bundle-closure`'s independent Case B
route (which never requires a per-class backbone to exist at all, so is
not structurally blocked here the way this approach's own mechanism is).

## §K. Complete resolution of the Realized-Backbone/UCR mechanism for
`a_1=4199`'s pair `(\{13\},\{17\})` (Round 12, new)

### Setup

`a_1=4199=13\cdot17\cdot19`, so `P_1=\{13,17,19\}`. I generated the
sequence independently (own smallest-prime-factor sieve up to
`6{,}000{,}000`, own factorization routine, own greedy-construction loop —
not reused from any prior round's script) to `N=12{,}000` terms
(`a_{12000}=242556`), and classified every term by its `P_1`-imprint
`S(i):=\mathrm{rad}(a_i)\cap P_1`. This recovers `2791` members of
`I_{\{13\}}` and `6156` members of `I_{\{17\}}$ within the generated range
— consistent with (and, for `\{13\}`, a superset of) the outline-reviewer's
figures, confirming both generators agree. The first six terms, needed
below, are:

| `i` | `a_i` | `\mathrm{rad}(a_i)` | `S(i)` |
|---|---|---|---|
| 1 | 4199 | `\{13,17,19\}` | `\{13,17,19\}` |
| 2 | 4212 | `\{2,3,13\}` | `\{13\}` |
| 3 | 4216 | `\{2,17,31\}` | `\{17\}` |
| 4 | 4218 | `\{2,3,19,37\}` | `\{19\}` |
| 5 | 4233 | `\{3,17,83\}` | `\{17\}` |
| 6 | 4250 | `\{2,5,17\}` | `\{17\}` |

### Step 1 — Sandwich Uniqueness Lemma (new, general-purpose, fully proved)

**Lemma.** Fix a doubly-infinite disjoint core pair `(S,S')` (`I_S,I_{S'}`
both infinite, `S\cap S'=\varnothing`). Fix `z\in\{S,S'\}` and let `y` be
the other core. Suppose `W` is a nonempty finite set of primes disjoint
from `P_1` witnessing Conjecture (JW) for `(S,S')` **via the specific
Realized-Backbone/UCR mechanism**, i.e.: (a) `W\subseteq\mathrm{comp}(a_k)`
for every `k\in I_z` (full-class containment on side `z`), and (b) `W` is
*exactly realized* on side `z`: `\mathrm{comp}(a_m)=W` for some `m\in
I_z`. Then `W=B_{\mathrm{full}}(z):=\bigcap_{k\in I_z}\mathrm{comp}(a_k)`
exactly.

**Proof.** By (a), `W\subseteq\mathrm{comp}(a_k)` for every `k\in I_z`,
hence `W\subseteq\bigcap_{k\in I_z}\mathrm{comp}(a_k)=B_{\mathrm{full}}(z)`.
Conversely, `m\in I_z` (by (b)), so `B_{\mathrm{full}}(z)$ (an intersection
over *all* of `I_z`, in particular over the single index `m`) satisfies
`B_{\mathrm{full}}(z)\subseteq\mathrm{comp}(a_m)=W$ (using (b) again).
Combining both containments: `W=B_{\mathrm{full}}(z)`. `\blacksquare`

*(Remark: this needs no appeal to Backbone Permanence, No-Resurrection, or
any other conditional machinery — it is a two-line consequence of the
mechanism's own two hypotheses (a),(b), which is exactly why it applies
uniformly regardless of which of the two cases in Step 3 below actually
holds for `\{13\}`.)*

**Consequence used below.** For the mechanism to close (JW) for `(S,S')`
via anchor `z`, `W` is *forced* to equal `B_{\mathrm{full}}(z)` — there is
no freedom to pick a smaller or different realized set. Hence the
mechanism succeeds via anchor `z` **if and only if** `B_{\mathrm{full}}(z)`
is (i) nonempty and (ii) exactly realized as some `I_z`-member's full
companion set. Both conditions must be checked; failing either kills that
anchor choice.

### Step 2 — Anchor `z=\{17\}` fails: `B_{\mathrm{full}}(\{17\})=\varnothing` outright

Indices `3,5\in I_{\{17\}}$ (table above): `\mathrm{comp}(a_3)=\{2,31\}`,
`\mathrm{comp}(a_5)=\{3,83\}`. These are disjoint:
`\{2,31\}\cap\{3,83\}=\varnothing`. Since
`B_{\mathrm{full}}(\{17\})=\bigcap_{k\in I_{\{17\}}}\mathrm{comp}(a_k)
\subseteq\mathrm{comp}(a_3)\cap\mathrm{comp}(a_5)=\varnothing`, we get
`B_{\mathrm{full}}(\{17\})=\varnothing`. This uses only two concrete,
already-computed terms — no asymptotic or infinite verification is
needed, and no later class member can ever undo an intersection already
forced to `\varnothing` (intersecting `\varnothing` with anything stays
`\varnothing`). By Step 1's Consequence, anchor `z=\{17\}` requires
`B_{\mathrm{full}}(\{17\})` nonempty — **fails, unconditionally, by direct
computation.**

### Step 3 — Anchor `z=\{13\}` fails, via an exhaustive two-case dichotomy needing no unresolved hypothesis

By Step 1's Consequence, anchor `z=\{13\}` requires
`W=B_{\mathrm{full}}(\{13\})`, nonempty and exactly realized on
`I_{\{13\}}`. The running prefix intersection (`B_k` of the Round 12
Outline's Step 1) is `\{2,3\}\cap\{2,3,5,11\}\cap\{2,83\}\cap\cdots
=\{2\}` by the 3rd realized class-`13` member (confirmed independently:
first three `I_{\{13\}}$ members are `i=2$ (`\mathrm{comp}=\{2,3\}`),
`i=8` (`\mathrm{comp}=\{2,3,5,11\}`), `i=9` (`\mathrm{comp}=\{2,83\}`);
running intersection `\{2,3\}\to\{2,3\}\to\{2\}`), and stays `=\{2\}$
through all `2791` tested members to `N=12{,}000` (0 further shrinkage
observed) — matching the outline-reviewer's figures. Since `B_k` is a
non-increasing sequence of subsets of the fixed 2-element set `\{2,3\}`
(after the first shrink) that has already reached the singleton `\{2\}`,
exactly two outcomes are possible for the true infinite intersection
`B_{\mathrm{full}}(\{13\})`:

**Case (i): `B_{\mathrm{full}}(\{13\})=\{2\}$** (i.e. Backbone Permanence
holds for this side — no later `I_{\{13\}}` member ever drops `2`). By
Step 1's Consequence, `W` would have to equal `\{2\}` exactly and be
exactly realized: `\exists m\in I_{\{13\}}` with `\mathrm{rad}(a_m)=
\{13\}\cup\{2\}=\{2,13\}$ exactly. But the already-certified **Lemma
ERD-C** (`lemmas/lemma-ERD-realized-blocked-dichotomy.md`) applies
directly: taking `\kappa:=\{2,13\}` (a nonempty finite set of primes) and
witness `j:=5`, `\mathrm{rad}(a_5)\cap\kappa=\{3,17,83\}\cap\{2,13\}=
\varnothing`, so `\kappa` is **blocked** by `j=5` — and Lemma ERD-C's
statement (ii) gives, unconditionally, that `\kappa=\{2,13\}` is **never
realized at any index** `m` (not just no `m\in I_{\{13\}}`, no `m` at
all). Hence no such `m` exists — anchor `z=\{13\}` fails in this case.

**Case (ii): `B_{\mathrm{full}}(\{13\})\subsetneq\{2\}`** (some later,
not-yet-generated `I_{\{13\}}` member drops `2` from its companion set).
Since `\{2\}` has exactly one element, the only proper subset is
`\varnothing`, so `B_{\mathrm{full}}(\{13\})=\varnothing`. By Step 1's
Consequence, anchor `z=\{13\}` requires `B_{\mathrm{full}}(\{13\})`
nonempty — fails immediately, for the same reason as Step 2.

**These two cases are exhaustive** (`B_{\mathrm{full}}(\{13\})\subseteq
B_k=\{2\}` for every tested `k`, in particular `B_{\mathrm{full}}(\{13\})
\subseteq\{2\}`, so it is either `\{2\}` or `\varnothing` — no third
possibility) **and mutually exclusive** (a set cannot both equal `\{2\}`
and equal `\varnothing`). In both cases, anchor `z=\{13\}` fails. Note
this dichotomy sidesteps the question of whether Backbone Permanence
actually holds on the `\{13\}` side — the mechanism fails either way,
so this approach does not need to (and does not) resolve that question
here.

### Conclusion of §K

Both possible anchors (`z=\{13\}`, `z=\{17\}`) for the Realized-Backbone/
UCR mechanism are proved, unconditionally and exhaustively, to fail for
`a_1=4199`'s pair `(\{13\},\{17\})`. By Step 1 (Sandwich Uniqueness), no
other choice of `W` is available to this specific mechanism (it forces
`W` to be one side's full class intersection, exactly, with no freedom).
**This is a complete, gap-free proof that this approach's headline
Round-12 mechanism cannot close Conjecture (JW) for this pair — not an
unfinished search, and not merely "not yet realized within the tested
range."** Conjecture (JW) *itself* remains open for this pair (this only
rules out one specific route to it); per the dispatch, closing it (if
possible at all) is `sunflower-bundle-closure`'s independent
NIDF-pigeonhole mechanism, which does not require a per-class backbone
and is therefore not affected by this negative result.

## Round 11 Outline (proof-outliner directive — attack `(MRS_S)` (per-core
antichain freeze) directly for the two cores of a fixed doubly-infinite
pair, via the poset/first-occurrence toolkit, NOT as a route to global
`𝓥`/(MRS))

**Target (unchanged): the whole problem**, via Theorem SW →
Termination-Sufficiency Lemma → Theorem 5.1 (all already
certified/conditional, do not re-derive). This round retargets the
First-`K`-Prefix Recruitment Conjecture (§I) using this round's fk-lens
explorer's sharpened bridge (`/tmp/round-11/math-explorer-fk.md`):
`(MRS_S)` (the per-core, class-locally-restricted minimal-radical
antichain `𝓜_n^S:=\{rad(a_i):i\in M_n^S\}`,
`M_n^S:=\{i\in I_S\cap[1,n]:` no `k\in I_S\cap[1,n]` has
`rad(a_k)\subsetneq rad(a_i)\}`, freezes at a finite index `n^*`) directly
implies First-`K`-Prefix with `K:=|I_S\cap[1,n^*]|` (already certified in
`lemmas/lemma-freeze-confinement-domination-and-Splus.md`'s
Freeze-Confinement Domination Lemma — cite, do not re-derive).

**Scope discipline — read before building (the dispatch's mandated
scrutiny, resolved this round).** Re-reading `lemmas/theorem-UBS-false-
case-II.md` directly (not the summary) confirms its Main Theorem refutes
only "`(UB_S)` for every proper core simultaneously" (a bundle-*size*
boundedness hypothesis); it neither states nor needs anything about
`(MRS_S)` (a minimal-*generator*-antichain-freeze hypothesis), and the two
are logically different and can diverge — the certified round-9 finding
`ω(a_n)=8` (`a_1=247`, large `n`) is a *dominated, non-minimal* value, not
a new antichain element, so bundle-size unboundedness and antichain
freezing are empirically and structurally consistent, not contradictory
(this matches Lemma XC/NIDF/FT's own size-agnostic construction in
`sunflower-bundle-closure`). **So `(MRS_S)` is genuinely not touched by
the Case-II refutation, and fk's technical claim holds up.**

**However — a further check this round performed, not in fk's report,
that must temper how `(MRS_S)` is used.** `(MRS_S)` with freeze index
`n^*` implies (short argument: the union of the finitely many antichains
`\mathcal M_1^S,\dots,\mathcal M_{n^*}^S`, each finite, is finite, and no
new locally-minimal value ever appears past `n^*`) that `𝓥_S` (the
GLOBAL-minimality-restricted-to-imprint-`S` set, Theorem CD's notation) is
finite, since `𝓥_S\subseteq\bigcup_n\mathcal M_n^S`. Combined with the
ALREADY-CERTIFIED whole-problem bridge in
`lemmas/theorem-UBS-sufficiency.md` (which uses `(UB_S)` ONLY to get
`Λ_S`/`𝓥_S` finite for every proper core — every subsequent step, Theorem
CD → Theorem V → Lemma MS → Theorem 5.1, needs no further boundedness
hypothesis), **`(MRS_S)` holding for *every* proper core `S` would
re-derive the ENTIRE whole-problem conclusion — i.e. it would be
logically equivalent in strength to the original round 4–8
`(MRS)`/`𝓥`-finiteness program**, which is precisely what round 6's
already-certified Multi-Companion Reduction Proposition showed reduces to
"a local, restricted instance of FCBC itself" (equi-hard, not easier)
once a core's realized companion bundles have size `\ge2`. **Do NOT
pursue `(MRS_S)`-for-every-proper-core as a shortcut to the whole problem
this round — that is the same wall via a new vocabulary, exactly the
pattern CLAUDE.md warns against, and the round-6 finding was never
refuted.** The legitimate, narrower target — and the one this outline
commits to — is `(MRS_S)` **only for the specific (at most
`\binom{2^k-1}{2}`, a fixed finite number of) cores appearing in
doubly-infinite pairs**, used only as an input to the already-certified,
strictly weaker Termination-Sufficiency Lemma (Stabilization for ONE
pair, not global `𝓥`-finiteness).

**Technique:** prove `(MRS_S)` for a fixed proper core `S` with `I_S`
infinite using the poset/first-occurrence toolkit already certified for a
DIFFERENT original purpose (escape-depth bounding, now retired) — Lemma
FOM (`T_C` first-occurrence formula), the No-Resurrection Lemma, and the
Generation-Chain Lemma — pointed directly at antichain finiteness as the
terminal goal, per fk's own diagnosis that this specific combination has
never been tried this way.

**Skeleton:**
1. Recall (cite): `M_n^S`, `𝓜_n^S`, Hypothesis `(MRS_S)`, and the
   certified Freeze-Confinement Domination Lemma (`(MRS_S)`+freeze index
   `n^*` ⟹ every `i\in I_S` has `rad(a_i)\supseteq` some frozen `C'`).
2. Adapt Lemma FOM: every locally-minimal radical `C\in\mathcal M_n^S` is
   realized first at a fixed, `a_1`-and-`C`-computable index `T_C` (same
   formula as the certified global version, restricted to class `S`).
   `(MRS_S)` fails iff infinitely many DISTINCT locally-minimal `C`'s are
   ever realized, i.e. infinitely many distinct `T_C` values occur as
   class-`S`-minimal.
3. Apply the Generation-Chain Lemma (domination chains have finite
   length, already certified) to bound how a locally-minimal `C` can
   later be "dethroned" (superseded by a strictly smaller later-arriving
   `C'\subsetneq C` within class `S`) — use this to argue the sequence of
   successive locally-minimal-antichain states is a well-founded process
   (each dethroning strictly shrinks a monovariant, e.g.
   `\Sigma_{C\in\mathcal M_n^S}|C|`), the open content being whether this
   process can run for only FINITELY many steps for an ARBITRARY core `S`
   (not just the tested instances).
4. **Key open lemma: No-Perpetual-Churn.** For a proper core `S` with
   `I_S` infinite, the sequence of distinct antichains
   `\mathcal M_1^S,\mathcal M_2^S,\dots` changes only finitely many
   times. Attempt via a magnitude argument (each dethroning event
   requires a STRICTLY smaller realized radical, but by the Growth Lemma
   `a_n=O(n)` and Lemma FOM's `T_C` formula, `T_C` is monotonic in some
   computable sense in `|C|` — make this precise) bounding the total
   number of possible dethroning events by a function of `S` and `a_1`
   alone (not by `n`).
5. Conclude: apply the Freeze-Confinement Domination Lemma + fk's bridge
   (`K:=|I_S\cap[1,n^*]|`) to get First-`K`-Prefix for that side; combine
   both sides' `(MRS_S)`/`(MRS_{S'})` via the already-certified Greedy
   Augmentation + Termination-Sufficiency Lemma to close Stabilization for
   the pair `(S,S')`.

**Key lemmas (claim + mechanism):**
- `(MRS_S)` ⟹ First-`K`-Prefix (already certified via the bridge, cite
  `lemmas/lemma-freeze-confinement-domination-and-Splus.md` + fk's
  one-line argument, do not re-derive).
- No-Perpetual-Churn (Step 4, the crux open gap) — conjectured because
  every one of this round's fresh, independently-generated numeric
  instances (up to 20,000,000 for `a_1=247`, 49,000× past freeze) shows
  literal set-identity freezing at SMALL indices despite the antichain's
  own size fluctuating non-monotonically beforehand (as with the
  certified global `4087` collapse phenomenon) — a real, not-yet-explained,
  but strongly evidenced pattern; the mechanism must explain WHY churn
  stops, not just that it numerically does.

**Open gaps:** Step 3–4 (the entire "why does churn stop" mechanism —
genuinely new content, no existing lemma in this workspace proves
antichain termination directly; Lemma FOM/No-Resurrection/
Generation-Chain were built for escape-depth, and their applicability to
THIS specific finiteness question is conjectural, not yet verified even
at the level of "the right monovariant exists").

**Cases to cover:** none beyond the single fixed core `S` (the outline is
per-core; repeat for `S'` symmetrically; only finitely many `(S,S')`
pairs need this, per Theorem SW).

**Watch out for:** (a) the temptation to prove `(MRS_S)` for EVERY proper
core as a "free" route to the whole problem — explicitly barred above,
re-collapses to the certified-equi-hard round-6 finding; only attack it
for the specific pair's two cores. (b) Do not conflate this file's own
already-refuted `K_0:=S^+_S\cup S^+_{S'}` candidate with the new target —
`(MRS_S)`'s frozen antichain is a different (and, per this round's
numerics, much better-behaved) object than the intersection-based `S^+`.
(c) If, on any single instance, the per-core antichain is found to churn
indefinitely (no freeze even at very large `N`), this refutes `(MRS_S)`
for that instance and the whole revised plan for that pair — report
immediately and do not force a fit.

## Round 11 update (headline — read this first)

**Scope, as mandated by the dispatch: `(MRS_S)` restricted strictly to the
two cores of the fixed doubly-infinite pair `(\{1061\},\{103,197\})`
(`a_1=21528751`) that feeds the already-certified Termination-Sufficiency
Lemma — NOT `(MRS_S)`-for-every-core, which stays barred.**

**What this round establishes (full detail in §J below).** (1) A genuinely
new, fully proved pair of lemmas — the **Local No-Resurrection Lemma** and
**Local Interval Lemma** — adapting the certified GLOBAL machinery behind
Theorem V (`lemmas/theorem-V-veto-finite-iff-MRS.md`) to the class-`S`-
restricted competitor pool `I_S`, giving a clean **Local Equivalence
Theorem**: `(MRS_S) \iff \mathcal V_S^{\mathrm{loc}}` finite, where
`\mathcal V_S^{\mathrm{loc}}:=\bigcup_n\mathcal M_n^S` is the local analogue
of Theorem CD's `\mathcal V_S`. This upgrades the outline-reviewer's
numerically-checked containment `\mathcal V_S\subseteq\mathcal
V_S^{\mathrm{loc}}` to a full, unconditional **proof** (the Subset Lemma,
§J Step 4), not merely a verified inequality. (2) Using this chain, a
**No-Shortcut Corollary**: `(MRS_S)\Rightarrow\Lambda_S` finite (via the
already-certified `\Lambda_S`-Reduction Lemma), and — applied concretely to
`S=\{103,197\}`, one of the two cores THIS ROUND'S OWN mandated pair
targets, which the certified Permanent Bundle Lemma
(`lemmas/lemma-permanent-bundle.md`) shows realizes a genuine size-`2`
multi-companion bundle `Q=\{11,97\}` — shows that closing `(MRS_S)` for
this specific in-scope core would, via an unconditional chain of already-
certified lemmas (not a new hypothesis), resolve exactly the "local,
restricted instance of FCBC itself" that the certified round-6
**Multi-Companion Reduction Proposition** already diagnosed as equi-hard.
**This is a rigorous confirmation, not a numeric hunch, of the precise
residual risk the round-11 outline-reviewer flagged** ("if the builder's
No-Perpetual-Churn attempt bottoms out in exactly the same hitting-set shape
as round 6's Multi-Companion Reduction, report this honestly"). (3) A
precise diagnosis of exactly why the outline's named toolkit (Lemma FOM,
No-Resurrection, Generation-Chain) cannot by itself close No-Perpetual-Churn:
the Generation-Chain Lemma bounds domination-chain **length** (vertical
depth along one lineage) but supplies no bound whatsoever on antichain
**width** (the number of pairwise-incomparable locally-minimal branches that
can coexist before a common dominator is ever realized) — and it is width,
not length, that must be finite for `(MRS_S)`. This is shown by an explicit
combinatorial construction (§J Step 6) of how unboundedly many incomparable
transient elements can in principle appear above a single not-yet-realized
permanent element, with no tool in the named toolkit ruling this out.

**No approach closes `(MRS_S)` this round; Status stays `partial`.** Two new
lemmas are fully proved and proposed for certification (Local
No-Resurrection/Interval/Equivalence; the Subset Lemma). The central open
gap (No-Perpetual-Churn) is not closed and is now rigorously — not just
suspectedly — shown to be at least as hard as the already-certified
equi-hard Multi-Companion Reduction target for the concrete in-scope core
`\{103,197\}`. This is exactly the honest negative finding the outline asked
for if the mechanism failed to buy tractability — reported here with a full
proof chain, per CLAUDE.md's rigor rules, rather than papered over.

## §J. Local No-Resurrection / Local Interval Lemma, the Local Equivalence
Theorem, and the No-Shortcut Corollary (Round 11)

### Setup (extends §H's notation; self-contained)

Fix `a_1=21528751`, `P_1=\{103,197,1061\}`, and the doubly-infinite disjoint
core pair `(S,S')=(\{1061\},\{103,197\})` (the pair this round's outline
targets, per fk's math-explorer report and Theorem SW). Everything below is
stated for a general proper core `S\subsetneq P_1` with `I_S` infinite —
this is deliberate: the Local No-Resurrection/Interval/Equivalence lemmas
hold for *any* such `S` (they need no hypothesis beyond `I_S` infinite, the
already-established hypothesis for doubly-infinite pairs), and are applied
concretely below only to the two in-scope cores `S=\{1061\}`,
`S=\{103,197\}`. Recall from §H: `M_n^S:=\{i\in I_S\cap[1,n]:$ no
`k\in I_S\cap[1,n]$ has `\mathrm{rad}(a_k)\subsetneq\mathrm{rad}(a_i)\}`,
`\mathcal M_n^S:=\{\mathrm{rad}(a_i):i\in M_n^S\}`. Hypothesis `(MRS_S)`:
`\exists n^*` with `\mathcal M_n^S=\mathcal M_{n^*}^S` for all `n\ge n^*`.
Define `\mathcal V_S^{\mathrm{loc}}:=\bigcup_{n\ge1}\mathcal M_n^S` (every
radical value ever locally-`S`-minimal, at any finite `n`) — the exact
local analogue of the already-certified global object `\mathcal
V:=\bigcup_n\mathcal M_n` from `lemmas/theorem-V-veto-finite-iff-MRS.md`.

Recall also (Theorem CD notation, `lemmas/theorem-CD-core-decomposition-
and-lemma-TC.md`): `M_n\subseteq\{1,\dots,n\}` is the set of GLOBALLY
`n`-minimal indices (no `k\in\{1,\dots,n\}$, any core, has
`\mathrm{rad}(a_k)\subsetneq\mathrm{rad}(a_i)`); `\mathcal
M_n:=\{\mathrm{rad}(a_i):i\in M_n\}`; `\mathcal
V:=\bigcup_n\mathcal M_n=\bigsqcup_S\mathcal V_S` where `\mathcal
V_S:=\{C\in\mathcal V:C\cap P_1=S\}`.

### Step 1 — Local No-Resurrection Lemma (new, fully proved)

**Lemma.** Fix a proper core `S` with `I_S` infinite, and a finite prime set
`C` realized as `\mathrm{rad}(a_i)` for some `i\in I_S`. If some `k\in I_S`
has `\mathrm{rad}(a_k)\subsetneq C`, then `C\notin\mathcal M_m^S` for every
`m\ge k`.

**Proof.** Suppose, for contradiction, `C\in\mathcal M_m^S` for some `m\ge
k`. Then `C=\mathrm{rad}(a_j)` for some `j\in M_m^S`, i.e. `j\in
I_S\cap[1,m]` and no `l\in I_S\cap[1,m]` has `\mathrm{rad}(a_l)\subsetneq
\mathrm{rad}(a_j)=C`. But `k\in I_S` and `k\le m` (hypothesis `m\ge k`), so
`k\in I_S\cap[1,m]`, and `\mathrm{rad}(a_k)\subsetneq C` by hypothesis —
contradicting the previous sentence with `l:=k`. `\blacksquare`

*(This is the exact restriction of the already-certified global No-
Resurrection Lemma's proof, `lemmas/theorem-V-veto-finite-iff-MRS.md` Route
1, to the competitor pool `I_S` in place of `\{1,\dots,n\}`; the proof goes
through verbatim because the argument never uses anything about the
competitor pool beyond it being a fixed set closed under "restrict to
`[1,m]`," which `I_S\cap[1,m]` satisfies for every `m`.)*

### Step 2 — Local Interval Lemma (new, fully proved)

**Lemma.** Fix a proper core `S` with `I_S` infinite. For every `v\in
\mathcal V_S^{\mathrm{loc}}`, the set `A_v^S:=\{n\ge1:v\in\mathcal
M_n^S\}` is a contiguous interval of one of two shapes:
`[n_v,\infty)` or `[n_v,e_v)`, where `n_v:=\min A_v^S`.

**Proof.** `A_v^S` is nonempty (since `v\in\mathcal V_S^{\mathrm{loc}}$
means `v\in\mathcal M_n^S` for some `n`) and a subset of `\mathbb N$, so
`n_v:=\min A_v^S` exists (well-ordering). Let `E_v^S:=\{n>n_v:
v\notin\mathcal M_n^S\}`. **Case `E_v^S=\varnothing`.** Then `v\in\mathcal
M_n^S` for every `n\ge n_v` (else some `n>n_v` would witness
`n\in E_v^S`), giving `A_v^S=[n_v,\infty)`. **Case
`E_v^S\ne\varnothing`.** Let `e_v^S:=\min E_v^S` (exists, well-ordering).
By minimality of `e_v^S`, `v\in\mathcal M_n^S` for every
`n_v\le n<e_v^S$ (no such `n` lies in `E_v^S`), giving
`A_v^S\supseteq[n_v,e_v^S)`. It remains to show `v\notin\mathcal M_c^S`
for every `c\ge e_v^S`. Since `v\in\mathcal M_{n_v}^S`, some
`i\in M_{n_v}^S\subseteq I_S` realizes `\mathrm{rad}(a_i)=v`, with
`i\le n_v<e_v^S`. Since `v\notin\mathcal M_{e_v^S}^S$ (definition of
`e_v^S\in E_v^S`) but `i\in I_S\cap[1,e_v^S]$ (as `i\le n_v<e_v^S$) still
realizes `\mathrm{rad}(a_i)=v`, the only way `v` can fail to be in `\mathcal
M_{e_v^S}^S` is that `i\notin M_{e_v^S}^S`, i.e. some `k\in
I_S\cap[1,e_v^S]` has `\mathrm{rad}(a_k)\subsetneq\mathrm{rad}(a_i)=v`. By
the Local No-Resurrection Lemma (Step 1, applicable since `k\le e_v^S`),
`v\notin\mathcal M_c^S` for every `c\ge e_v^S`. Combined with the earlier
containment, `A_v^S=[n_v,e_v^S)` exactly. `\blacksquare`

### Step 3 — Local Equivalence Theorem (new, fully proved)

**Theorem.** Fix a proper core `S` with `I_S` infinite. `(MRS_S)`
holds **if and only if** `\mathcal V_S^{\mathrm{loc}}` is finite.

**Proof.** `(\Leftarrow)` Suppose `\mathcal V_S^{\mathrm{loc}}` is finite.
For each `v\in\mathcal V_S^{\mathrm{loc}}`, let `m_v:=n_v` (Case `E_v^S=
\varnothing` of Step 2) or `m_v:=e_v^S` (Case `E_v^S\ne\varnothing`).
Set `n^*:=\max_{v\in\mathcal V_S^{\mathrm{loc}}}m_v` (a finite maximum
over a finite set). For every `n\ge n^*` and every `v\in\mathcal
V_S^{\mathrm{loc}}`: if `E_v^S=\varnothing`, `v\in\mathcal M_n^S`
(`A_v^S=[n_v,\infty)\supseteq[n^*,\infty)`); if `E_v^S\ne\varnothing`,
`v\notin\mathcal M_n^S` (since `n\ge n^*\ge e_v^S`, so `n\notin
A_v^S=[n_v,e_v^S)`). Either way, membership of `v` in `\mathcal M_n^S` is
the same for all `n\ge n^*` — and since every element of every `\mathcal
M_n^S$ (`n\ge1`) lies in `\mathcal V_S^{\mathrm{loc}}` by definition of the
latter as a union, this gives `\mathcal M_n^S=\mathcal M_{n^*}^S` for all
`n\ge n^*`: `(MRS_S)` holds with freeze index `n^*`.

`(\Rightarrow)` Suppose `(MRS_S)` holds with freeze index `n^*`. For
`n>n^*`, `\mathcal M_n^S=\mathcal M_{n^*}^S\subseteq\bigcup_{m\le
n^*}\mathcal M_m^S`; for `n\le n^*` trivially `\mathcal M_n^S\subseteq
\bigcup_{m\le n^*}\mathcal M_m^S`. So `\mathcal
V_S^{\mathrm{loc}}=\bigcup_{n\ge1}\mathcal M_n^S=\bigcup_{m=1}^{n^*}
\mathcal M_m^S`, a finite union (`n^*` terms) of finite sets (`|\mathcal
M_m^S|\le|M_m^S|\le m`), hence finite. `\blacksquare`

*(This is the exact local analogue of the certified Theorem V/Theorem
V-MRS equivalence — the same two-lemma architecture, applied to the
class-restricted competitor pool `I_S` in place of the whole index set. It
is genuinely new: `theorem-V-veto-finite-iff-MRS.md` never states or proves
this for a restricted competitor pool, and the outline-reviewer's round-11
numerical check of the related but logically DIFFERENT object `\mathcal
V_S\subseteq\mathcal V_S^{\mathrm{loc}}$ containment did not establish
this equivalence.)*

### Step 4 — Subset Lemma: `\mathcal V_S\subseteq\mathcal V_S^{\mathrm{loc}}` (new, fully proved — upgrades the round-11 outline-reviewer's numerical finding to a proof)

**Lemma.** For every proper core `S`, `\mathcal V_S\subseteq\mathcal
V_S^{\mathrm{loc}}`.

**Proof.** Let `C\in\mathcal V_S`. By definition (Theorem CD), `C\in
\mathcal M_n` for some `n$, with realizing index `i\in M_n` (so `i\le n`,
`\mathrm{rad}(a_i)=C`), and `C\cap P_1=S`, i.e. `i\in I_S`. Since `i\in
M_n`: no `k\in\{1,\dots,n\}` (competing against **all** of `[1,n]`) has
`\mathrm{rad}(a_k)\subsetneq C`. In particular, since `I_S\cap[1,n]
\subseteq\{1,\dots,n\}`, no `k\in I_S\cap[1,n]` has
`\mathrm{rad}(a_k)\subsetneq C` either — a strictly weaker requirement
(fewer competitors to fail against). Since also `i\in I_S\cap[1,n]`, this
gives `i\in M_n^S`, hence `C=\mathrm{rad}(a_i)\in\mathcal M_n^S\subseteq
\mathcal V_S^{\mathrm{loc}}`. `\blacksquare`

*(This one-line "fewer competitors ⟹ weaker minimality requirement ⟹
easier to satisfy" argument is the precise mechanism behind the outline-
reviewer's round-11 numeric finding that the containment can be strict —
e.g. `a_1=21528751,S=\{197\}`: global-restricted `\mathcal V_S=\varnothing`
while `\mathcal M_n^S` already has 3 elements — confirming `(MRS_S)` is
generically a strictly stronger requirement than the already-known-hard
`\mathcal V_S$-finiteness target, not a restatement of it.)*

### Step 5 — No-Shortcut Corollary: `(MRS_S)` for the in-scope core `S=\{103,197\}` entails the already-certified equi-hard Multi-Companion hitting-set target

**Chain (all already-certified except Steps 3–4 above, proved this
round).** For a proper core `S` with `I_S` infinite:
$$(MRS_S)\ \overset{\text{Step 3}}{\Longrightarrow}\ \mathcal
V_S^{\mathrm{loc}}\text{ finite}\ \overset{\text{Step 4, subset of a finite
set}}{\Longrightarrow}\ \mathcal V_S\text{ finite}\ \overset{\Lambda_S
\text{-Reduction Lemma}}{\Longleftrightarrow}\ \Lambda_S\text{ finite},$$
where the last equivalence is the already-certified `\Lambda_S`-Reduction
Lemma (`lemmas/lemma-lambda-S-reduction-and-single-companion-
finiteness.md`): `\Lambda_S:=\bigcup_{C\in\mathcal V_S}(C\setminus S)`, and
`\mathcal V_S$ finite `\iff\Lambda_S$ finite.

**Concrete instantiation, `S:=\{103,197\}` (the second core of this round's
mandated pair).** The already-certified **Permanent Bundle Lemma**
(`lemmas/lemma-permanent-bundle.md`, round 7) proves — unconditionally, by
two explicit named witnesses, not by sampling — that the companion set
`Q:=\{11,97\}` (realized at some index `i` with `\mathrm{rad}(a_i)=
\{103,197\}\cup\{11,97\}`, a genuine multi-companion bundle, `|Q|=2`) is
**permanently undominated**: no later index ever realizes a proper subset
of `\{103,197,11,97\}` containing `S`, so `\{103,197,11,97\}\in\mathcal
V_{\{103,197\}}` (it is, in particular, an eventual permanent member of
the global antichain restricted to this core). Hence `\{11,97\}\subseteq
\Lambda_{\{103,197\}}`, so `\Lambda_{\{103,197\}}\supseteq\{11,97\}`, and by
the Multi-Companion Reduction Proposition (`lemmas/lemma-lambda-S-
reduction-and-single-companion-finiteness.md`, already certified,
unconditional): since `|Q|=2\ge2`, `Q\cap\mathrm{rad}(a_j)\ne\varnothing`
for **every** `j\in J_{\{103,197\}}` (the `\{103,197\}`-avoiding index
set) — a genuine hitting-set condition on the infinite family
`\{\mathrm{rad}(a_j):j\in J_{\{103,197\}}\}`, which that Proposition's own
certified scope note proves is **not** reducible to the Generalized-Lemma-C
stabilization mechanism that closes the `|Q|=1` case, and is instead "of
the same order of difficulty as FCBC itself" (quoted verbatim from the
certified file).

**Conclusion of Step 5.** Establishing `(MRS_S)` for `S=\{103,197\}` —
exactly one of the two cores this round's outline targets — would, via the
unconditional chain above (Steps 3–4, both proved this round, composed
with the already-certified `\Lambda_S`-Reduction Lemma), establish
`\Lambda_{\{103,197\}}` finite; and since `\Lambda_{\{103,197\}}` already
demonstrably contains the multi-companion witness `\{11,97\}` (certified,
concrete, not hypothetical), this is not a vacuous/degenerate instance of
the Multi-Companion Reduction's scope note — it is the **exact** situation
that Proposition diagnoses as equi-hard to FCBC. **This is a rigorous
demonstration — a full proof chain, not a numeric hunch — that this
round's assigned target (`(MRS_S)` for the pair's cores, via the
poset/first-occurrence toolkit) cannot bypass the already-known hardest
open sub-problem in this workspace for at least this concrete, in-scope
core.** This directly and honestly answers the residual concern the
round-11 outline-reviewer flagged ("if the builder's No-Perpetual-Churn
attempt bottoms out in exactly the same hitting-set shape as round 6's
Multi-Companion Reduction, report this honestly, not force a fit") — the
answer is **yes, it does**, for the concrete mandated instance, established
by proof.

### Step 6 — why the outline's named toolkit (Lemma FOM, No-Resurrection,
Generation-Chain) cannot close No-Perpetual-Churn: depth vs. width

The round-11 outline's Step 3–4 proposed bounding "dethroning events" via
a monovariant (e.g. `\sum_{C\in\mathcal M_n^S}|C|`) and the certified
Generation-Chain Lemma. This is examined directly, not merely cited.

**The Generation-Chain Lemma only bounds chain LENGTH.** Recall (already
certified, `lemmas/lemma-FOM-first-occurrence-minimality.md`): a domination
chain `C_1\supsetneq C_2\supsetneq\cdots\supsetneq C_r\supseteq S` (each
`C_{l+1}` a witness permanently excluding `C_l`) has `r\le|C_1|-|S|+1`
— a bound on how many times a **single lineage** of successive
dominators can strictly shrink before reaching `S`. This says nothing
about how many **pairwise-incomparable** chains (or singleton chains,
`r=1`) can coexist at once.

**A monovariant like `\sum_{C\in\mathcal M_n^S}|C|` is not controlled by
chain length alone.** A single dethroning event (an existing minimal
element `C` replaced by a new element `C'\subsetneq C$ realized at `I_S`)
strictly decreases `\sum|C|` by at least `1` (removes `C`, the new element
`C'$ that dominates it is strictly smaller, though it may also add
elements incomparable to both if it doesn't dominate everything). But an
event where a **genuinely new, incomparable** value `D` is realized (no
existing member of `\mathcal M_n^S` is a subset of `D`, and `D` is not a
superset of any existing member either) only **adds** `D` to `\mathcal
M_n^S` — the sum strictly *increases*, and no dethroning occurs at all.
The Generation-Chain Lemma is silent on how many such genuinely new,
mutually incomparable branches can appear, because it only ever discusses
a fixed chain's own internal length, never the antichain's cardinality
(width) at a fixed time.

**Explicit construction showing width is genuinely unconstrained by the
named toolkit (not merely "the toolkit doesn't discuss it," but a positive
demonstration no combination of Lemma FOM + No-Resurrection + Generation-
Chain rules out unbounded width).** Fix a not-yet-realized 2-element set
`C_0=S\cup\{p\}` (`p` prime, `p\notin P_1`) — i.e. no `i\in I_S` has
`\mathrm{rad}(a_i)=C_0$ yet. For any finite set of distinct primes
`\{q_1,\dots,q_r\}\setminus\{p\}$ disjoint from `P_1\cup\{p\}`, the values
`D_l:=S\cup\{p,q_l\}` (`l=1,\dots,r`) are pairwise incomparable (each
strictly contains `S\cup\{p\}`-worth of one extra prime `q_l\ne q_{l'}`,
neither `D_l\subseteq D_{l'}` nor `\supseteq$ for `l\ne l'`) and each
strictly contains `C_0`. Lemma FOM guarantees each `D_l`, if realized at
all, is first realized at the fixed computable index `T_{D_l}`; nothing in
Lemma FOM, the (Local) No-Resurrection Lemma, or the Generation-Chain
Lemma prevents **all `r`** of the `D_l` from being realized (in increasing
order of `T_{D_l}`) as successive NEW locally-minimal antichain elements
*before* `C_0` itself is ever realized — each `D_l`, upon realization, adds
a new element to `\mathcal M_n^S$ without dethroning any of the earlier
`D_{l'}` (`l'<l`), since they are pairwise incomparable; only if and when
`C_0` itself is eventually realized does the Local No-Resurrection Lemma
retroactively dethrone all `r` of them at once. Since `r` was an arbitrary
finite number in this construction, **no bound on `r` is supplied by any
lemma in the named toolkit** — bounding it requires an entirely different
argument (a bound on how many primes `q` can have `T_{S\cup\{p,q\}}$
occur before `T_{S\cup\{p\}}$ itself, which is exactly a magnitude/
recruitment-order question of the same flavor as the `(UB_S)`/Recruiter-
Alignment/First-K-Prefix "count vs. magnitude" wall documented across
rounds 7–10, not a poset-structural fact). This does **not** prove
unbounded width actually occurs for any specific `S` (the certified
numerics in `/tmp/round-11/math-explorer-fk.md` show it does not, up to
the tested range, for the two in-scope cores) — it proves the **named
toolkit's proof method** supplies no mechanism ruling it out, so
"No-Perpetual-Churn" cannot be certified by this toolkit alone; consistent
with, and giving a structural explanation for, the equi-hardness finding of
Step 5.

### Honest conclusion of §J

`(MRS_S)` for the two in-scope cores of `(\{1061\},\{103,197\})` is **not
established** this round. Two new lemmas (Local No-Resurrection/Interval/
Equivalence, Step 1–3; the Subset Lemma, Step 4) are fully proved and give
a clean, correct, previously-unstated equivalence and containment — genuine
reusable content. But composing them (Step 5) with already-certified
lemmas proves, rather than merely suggests, that closing `(MRS_S)` for
`S=\{103,197\}` specifically requires resolving the already-flagged
equi-hard-to-FCBC Multi-Companion hitting-set target — and Step 6 pins down
precisely why the outline's named toolkit structurally cannot supply the
missing antichain-width bound (it only ever bounds chain length or
first-occurrence identity, never width). This is the same "count vs.
magnitude" wall this workspace has hit repeatedly (rounds 3, 6–10), now
reached via the poset/first-occurrence route specifically, with a full
proof of why that route reaches it rather than bypasses it — an honest,
rigorous negative result, not a restatement of prior rounds' numerics.

## Round 10 update (headline — read this first)

**The well-ordering/greedy-augmentation scheme is now fully and rigorously
formalized (§I, Steps 1–2, two new certified-quality lemmas), and the
outline's own proposed `q_0`-bounding candidate (`S^+_S\cup S^+_{S'}`) is
**refuted** by a fresh, independent, exhaustive computation on the
workspace's hardest known instance — an honest correction, not a
completion.** Concretely:

1. **Greedy Augmentation Lemma (§I, Step 1, new, fully proved).** Makes
   precise and *proves* (not just describes) the well-ordering step the
   round-10 outline sketched informally: the process of repeatedly finding
   the `\max(i,j)`-minimal uncovered cross pair and adjoining a forced new
   companion prime is well-defined, and every prime it ever adjoins is a
   **fresh** prime outside `P_1` (a fact the outline needed but did not
   prove).
2. **Termination-Sufficiency Lemma (§I, Step 2, new, fully proved).** If
   there is *any* fixed finite set `K_0` (depending only on `a_1,S,S'`, not
   on the step number) containing every prime the process ever adjoins,
   then the process halts within `|K_0|` steps and the Stabilization
   Conjecture holds for `(S,S')`, with an explicit witness
   `W_{S,S'}\subseteq B_0\cup K_0`. This converts the outline's vague
   "Termination Lemma (open, the real content)" into a clean, provable
   **conditional theorem** — real, reusable progress even though the
   hypothesis (`K_0` exists) is not itself established in general.
3. **The specific candidate `K_0:=S^+_S\cup S^+_{S'}` is refuted, with a
   fresh independent computation (§I, Step 3), not merely re-cited from
   the bridge-primes explorer.** On `a_1=21528751`,
   `(S,S')=(\{1061\},\{103,197\})` (the workspace's own hardest documented
   instance): freshly computed (own script, `sympy.primefactors`, no reuse
   of any cached numeric table) `S^+_{\{1061\}}=\{2,3,7,1061\}` and
   `S^+_{\{103,197\}}=\{103,197\}` from the full `N=3{,}000{,}000` cache
   (`|I_{\{1061\}}|=875`, `|I_{\{103,197\}}|=15064`) — **both entirely
   contained in `B_0:=P_1\cup\{2,\ldots,13\}` already**, so the candidate
   `B_0\cup K_0` adds *zero* new primes and is provably insufficient: it
   still misses the bridge prime `97`, which is needed to cover exactly `3`
   (exhaustively enumerated) `\{2,3,5,7,11,13\}`-signature bucket-pairs,
   realizing `94` of the `13{,}181{,}000` cross-pairs at `N=3{,}000{,}000`.
   This is a decisive, not merely partial, refutation of the outline's
   Step 2 as literally stated.
4. **A sharper, precisely-stated (still open) replacement target: the
   First-`K`-Prefix Recruitment Conjecture (§I, Step 4).** Instead of an
   intersection (`S^+`), use a **union** of the companion primes of the
   first `K` realized members on each side. Verified, by fresh independent
   exhaustive computation, that `K=5` already gives a covering `W` on the
   hardest instance (zero violations among all `13{,}181{,}000` cross
   pairs at `N=3{,}000{,}000`) — matching the general shape of the outline's
   Step 3 idea exactly, but now stated precisely and tested rigorously
   rather than merely cited. **This conjecture is not proved.** The
   precise open content — why the greedy process's forced primes must
   always come from a fixed early prefix rather than drifting later — is
   identified as exactly "Opening B" from the bridge-primes explorer's
   report (pinning Lemma P′'s forced common prime to a computable finite
   set), and is honestly reported as unresolved this round.

**Conclusion.** Genuine new rigor (two fully proved lemmas turning an
informal well-ordering sketch into a clean conditional theorem) plus one
honest, decisive negative finding (the outline's own candidate fails,
demonstrated on a fresh independent computation) plus one sharper,
precisely-tested replacement conjecture, explicitly not closed. Status
remains `partial`.

## Round 10 Outline (proof-outliner directive — revive with a
well-ordering/minimal-counterexample argument on the Stabilization
Conjecture, seeded by round 10's bridge-prime empirical characterization)

**Target (unchanged): the whole problem**, via Theorem SW → Theorem 5.1
(both already certified, do not re-derive). This approach was deferred
(not built) rounds 9 as redundant with `explicit-window-backbone-
construction`'s `H_100` search — round 10's dispatch and the round-9 "Next"
notes both flag it as worth reviving with a genuinely different mechanism
now that Theorem SW narrows the target to the Stabilization Conjecture.

**Technique: minimal-counterexample / well-ordering argument directly on
the Stabilization Conjecture**, seeded by round 10's bridge-primes
explorer's empirical **Smooth-Multiple Recurrence** finding
(`/tmp/round-10/math-explorer-bridge-primes.md`) — genuinely different from
`intersecting-family-covering-construction`'s density/pigeonhole mechanism
and `explicit-window-backbone-construction`'s finite-alphabet covering-
design mechanism this round. This is **dispatch's suggested approach (c)**.

**Key empirical seed (not proof, motivates the construction):** in every
tested hard doubly-infinite channel, the members of `I_S` needing a bridge
prime beyond a small base window are exact integer multiples of one fixed
minimal generator `T_C=\prod_{p\in C}p` for a specific realized radical `C`
— and exactly ONE extra prime beyond `\{2,3,5,7,11,13\}` suffices in every
one of 5 tested hard channels across 3 `a_1` values (bridge-primes
explorer, 3/3 falsification attempts failed to grow the window).

**Skeleton:**
1. Fix a doubly-infinite disjoint core pair `(S,S')`. Suppose, for
   contradiction, that NO finite `W_{S,S'}` exists (Stabilization
   Conjecture false for this pair). Then for every finite candidate
   `W\supseteq\{2,3,\ldots,13\}`, there exist arbitrarily large uncovered
   pairs `(i,j)\in I_S\times I_{S'}` with `rad(a_i)\cap rad(a_j)\cap W=\emptyset`.
2. Well-order the uncovered pairs by `\max(i,j)` (or by `i+j`); let
   `(i_0,j_0)` be `W`-minimal for the CURRENT `W` at each stage. By Lemma
   P′ (already certified, unconditional), `\gcd(a_{i_0},a_{j_0})>1` — some
   prime `q_0\notin W` is forced. **Key step (the actual gap, do not
   assume):** show `q_0` is bounded — specifically, show `q_0` is drawn
   from the already-certified **`S^+`** necessary-witness machinery
   (`lemmas/lemma-freeze-confinement-domination-and-Splus.md`) applied to
   BOTH `S` and `S'` simultaneously (not the already-refuted single-sided
   `S^{++}`, which is a pure-intersection mechanism proven insufficient by
   the certified Vacuity/Intersection-Fragility Propositions — this is a
   **different, union-flavored** construction: `q_0` need not be forced by
   intersection alone, only shown to lie in a fixed finite set determined
   by the FIRST FEW occurrences of each core, not by an intersection over
   the whole infinite class).
3. Augment `W\leftarrow W\cup\{q_0\}` and repeat. **Termination lemma
   (open, the real content):** this process terminates after finitely many
   augmentations. Attempt via: the process only adds a NEW prime `q_0` when
   the current `W` fails on some minimal pair; if each augmentation can be
   charged to one of finitely many "first-collision events" between the
   finite prefixes of `I_S` and `I_{S'}` realized by index `\max(i_0,j_0)`
   — i.e., show `q_0` is always already a companion prime of one of the
   FIRST `K` members of `I_S` or `I_{S'}` for some `a_1`-and-`(S,S')`-
   dependent but N-INDEPENDENT constant `K` (this is exactly what the
   bridge-primes explorer's "one extra prime per hard channel, found early,
   never grows" numerics suggest, but is NOT yet proven) — then `W` is
   bounded by `\{2,\ldots,13\}\cup\bigcup_{i\le K,i\in I_S}rad(a_i)\cup
   \bigcup_{j\le K,j\in I_{S'}}rad(a_j)`, manifestly finite.
4. If Step 3's termination lemma holds, `W_{S,S'}$ exists finite, closing
   this channel; repeat across the finitely many doubly-infinite disjoint
   pairs (Theorem SW bounds the count).

**Key lemmas (claim + mechanism):**
- **Bridge primes are drawn from a fixed finite prefix, not growing with
  N** — because (conjecturally) the greedy process's "first collision"
  between two disjoint-core branches always recruits a prime already
  present among the first `K` realized members of one side, not a fresh
  one at every later collision — evidenced by the bridge-primes explorer's
  finding that the SAME single extra prime (`97`, `23`, or `83`) covers
  every violation found from `N=60{,}000` up to `N=3{,}000{,}000` with NO
  new prime ever appearing, in 3/3 tested channels. **This is the sharpest
  open sub-target of this approach — do not assume it, attempt a direct
  argument bounding `K$ via the already-certified Domination Lemma's rate
  inequality applied to the FIRST few terms of each side specifically
  (not the whole infinite class, sidestepping the already-refuted
  `S^{++}`/Vacuity obstruction, which only rules out INTERSECTION-based
  arguments over the whole class).**

**Open gaps:** Step 2's "`q_0` bounded" claim and Step 3's termination
lemma are both open — this is the actual new mathematics to attempt. Do
NOT re-attempt `S^{++}` or any pure-intersection sufficiency fix (Vacuity
Proposition, Intersection-Fragility Proposition, already certified,
structurally rule out that whole family) — this skeleton's `q_0`-bounding
mechanism must be a UNION/first-K-prefix argument, not an intersection
over `I_S$ or `I_{S'}` as a whole.

**Cases to cover:** repeat across each doubly-infinite disjoint core pair
(bounded count, Theorem SW).

**Watch out for:** the well-ordering argument in Step 2 needs the set of
uncovered pairs to genuinely have a well-founded minimal element at each
stage — since `\mathbb N\times\mathbb N` under `\max` is well-ordered, this
is fine, but be careful the "current `W`" is re-fixed at each stage (not
accidentally treating `W` as fixed throughout, which would beg the
question); also do not conflate this with the round-7-refuted "single-
witness Freeze Criterion" (that was about single-CORE freezing via one
witness's companion set; this is about a genuinely different object, a
CROSS-core covering set for a fixed pair, augmented incrementally).

## Round 9 Outline (proof-outliner directive — abandon `S^{++}`/`(UB_S)`-
family sufficiency routes; use `S^+` as a seed for a direct FCBC covering
set instead)

**Context (read first).** Round 9's explorers found strong numerical
evidence that `(UB_S)` (the round-8-established sole sufficient hypothesis
for the whole problem) is very likely **FALSE** (companion-bundle size sets
new records — ω=8 confirmed for two hard cases — with no blocking witness
found in 1.3M terms). This does not refute FCBC itself (strictly weaker,
never requires bounding bundle size) — and round 9's own data (0/1.3M terms
disjoint from `{2,3,5,7,11,13}`, `a_1=247`) is evidence a small explicit
covering set works. **New target this round: build FCBC's `H` directly**
using this file's own certified `S^+` necessity machinery as a seed,
**not** by trying to fix `S^{++}`'s already-refuted pure-intersection
sufficiency mechanism (Vacuity/Intersection-Fragility Propositions — that
specific route stays dead; do not revisit it, even relabeled).

Skeleton (full detail in `/tmp/round-9/proof-outliner.md` under
`forced-primes-well-ordering`):
1. For proper core `S` with `I_S` infinite, `S^+_S` (already certified
   finite) is necessary but not sufficient (documented failure:
   `a_1=21528751,S=\{1061\}`, missing prime `11`).
2. Candidate `H_S := S^+_S ∪ \{2,3,5,7,11,13\}` — the same small-prime
   patch `explicit-window-backbone-construction` uses this round (a shared
   candidate, not independently guessed; cross-check with that sibling
   file, cite rather than duplicate work).
3. **Patch Sufficiency Claim:** the gap between `S^+_S` and full
   sufficiency is always repaired by this same small fixed patch — test
   against every one of this file's own documented `S^+`-failure examples
   (the `a_1=21528751` case is repaired by construction since `11` is in
   the patch; verify at least 2 more before trusting this).
4. Extend to the pairwise requirement (shared open content with sibling
   approaches — cite, don't re-derive, if `explicit-window-backbone-
   construction`'s Step 4 closes it first).
5. `H := P_1 ∪ ⋃_S H_S`; invoke Theorem 5.1.

Open gaps: Step 3 (is the patch always small and fixed, or does some core
need an arbitrarily large patch — report either finding honestly) and Step
4 (pairwise sharing, shared with siblings).

## Round 8 Outline (proof-outliner directive — depth-boundedness is now
PROVEN to be a one-directional corollary of the master gap, not an
independent sub-problem; retire independent depth-hunting, certify the
cheap corollary, and pivot this file's real content to the explicit
recruiter-set (extended-imprint) mechanism)

**Context (read first — this changes this file's whole mandate).** Round
8's dedicated thread-unification explorer
(`/tmp/round-8/math-explorer-thread-unification.md`) proved, by regenerating
both of this file's own documented depth-3 escape events from scratch, that
**`(MRS_S)` (the antichain freezing) ⟹ a uniform escape-recursion depth
bound**, via a short new elementary lemma (the poset of realized class-`S`
radicals: once the minimal-element antichain stops changing, every later
realized radical is a superset of some fixed frozen minimal element — proved
in 3 cases below). Concretely: **every single one of the "deep" escape
events this file spent round 7 investigating (`a_1291`, `a_5844`, `a_7831`,
`a_19617`, `a_30017`, `a_807`, `a_1110`) turned out, on direct
recomputation, to be either (i) a re-realization, at a much later and
*immediately-dominated* index, of an already-permanent bundle established
early for the same core, or (ii) a genuinely transient member later
swallowed by that same eventual absorber** — i.e. depth was never an
independently-varying quantity; it is a shadow of the (already-mysterious,
still-open) early antichain freeze. **This means: (a) §G's whole round-7
program (find a self-contained well-founded measure bounding escape
recursion, independent of `(MRS_S)`) cannot succeed as an independent route
— it was already trending this way per §G Step 4's own honest finding that
the naive branching tree doesn't terminate, and this round's check confirms
*why* — and (b) this file's genuinely useful going-forward content is a
different, complementary question: constructing an EXPLICIT finite
recruiter set for each core (necessity + sufficiency), which round 8's
cross-bucket-direct explorer found real new partial traction on (the `S^+`
extended-imprint mechanism, below). Do not revive the Recruiter-Alignment/
`W(a_1)` pattern (already refuted for nested cores) or the naive branching-
tree induction (already refuted, §G Step 4) — both are now doubly dead.**

**Step 1 — certify the Freeze-Confinement Corollary (cheap, ~15 lines, do
this first; formally retires independent depth-hunting).**

*Statement.* Fix a proper core `S` with `I_S≠∅`. If `(MRS_S)` holds — the
antichain `𝓜_n^S` freezes at some finite index `n^*` (`𝓜_n^S=𝓜_{n^*}^S` for
all `n≥n^*`) — then every index `i∈I_S` with `i` "past the freeze" (formally:
every realized radical `rad(a_i)` for `i∈I_S`) is a superset of some fixed
element of the frozen antichain `𝓜_{n^*}^S`, hence the escape-recursion
depth from any blocked bare value reachable after `n^*` is bounded by
`max_{C'∈𝓜_{n^*}^S}|C'\S|` (plus a trivial finite max over the finitely
many pre-`n^*` escapes).

*Proof sketch (write up in full rigor — mechanism: elementary
antichain-maintenance case split, no new machinery).* In the poset of
realized class-`S` radicals ordered by `⊆`, tracking minimal elements as
more sets are added over increasing `n`: a newly realized radical either
(i) becomes a new minimal element, (ii) is a strict subset of an existing
minimal element (an antichain-changing event), or (iii) is a proper
superset of some already-minimal element (no antichain change). If the
antichain has genuinely stopped changing past `n^*` (hypothesis `(MRS_S)`),
only (iii) can occur for `i` with `n^*<i`-realizing-index — giving the
stated superset containment, hence the depth bound. `∎` (Full proof: write
out the three-way case split rigorously and confirm (iii) is forced.)

**This settles, with an actual proof (not intuition), this round's
dispatch question "does depth-bounding reduce trivially given
`Λ_S`-finiteness" — YES, one-directionally, cheaply.** Certify it, then
stop pursuing an independent depth mechanism.

**Step 2 — pivot this file's real content: the `S^+` (extended-imprint)
explicit recruiter-set mechanism (round 8's cross-bucket-direct explorer,
genuinely new, partial).**

*Definition.* `S^+:=⋂_{i∈I_S}rad(a_i)` (the imprint's OWN self-intersection
over its matching class `I_S`, as opposed to `D_S:=⋂_{j∈J_S}rad(a_j)`, the
already-certified avoiding-class intersection used by the Single-Companion
Finiteness Lemma — a different object, do not conflate). Already provably
finite whenever `I_S` is infinite, by the identical already-certified
**Generalized Lemma C** stabilization mechanism
(`lemmas/lemma-C-generalized-subsequence.md`) applied with the index set
`I_S` in place of `J_S` — a substitution not previously made explicit for
this purpose; certify this one-line application as its own small corollary.

*Necessity Lemma (cheap, ~3 lines, certify).* Every exactly-realized bare
value `C=rad(a_i)` for `i∈I_S` satisfies `C⊇S^+` (immediate: `S^+⊆rad(a_i)`
by definition of the intersection). So `S^+\P_1` is an unconditional
necessary lower bound on every companion bundle ever realized for `S`.

*Numerical status (round 8, reuse directly, do not re-derive).* Exact match
(as a **tight**, not just necessary, explanation) on 7 of 8 tested
core/bucket-family instances spanning all 5 mandated hard cases. One
genuine, honestly-reported gap: `a_1=21528751,S={1061}` (a sparse class, 19
realized members through `n=60000`) needs **exactly one extra prime** (`11`)
beyond `S^+\P_1={2,3,7}` in both of its populated buckets — `S^+` is
necessary but demonstrably **not sufficient** there.

**Step 3 — this round's genuinely open target: close the sufficiency gap
(the `S={1061}`-style "extra recruitment") via the explorer's own proposed
second-order refinement, `S^{++}`.** Define, for a coarse bucket `κ`,
`S^{++}_κ:=⋂_{i∈I_S,\,κ⊆rad(a_i)}rad(a_i)` (the extended imprint restricted
to the sub-class of `I_S` whose realized radical *also* contains `κ` — a
strictly smaller, hence potentially strictly larger-intersection, index
set). Attempt to show `S∪S^{++}_κ` is **sufficient** (not just necessary) to
pin down the actual dominator for bucket `κ`, for at least the one failing
instance (`S={1061}`) — this was **not attempted** by the round-8 explorer
(flagged as out of scope for the lens, "worth a focused follow-up"), so it
is genuine, unattempted content this round's builder should try first.
Report honestly if `S^{++}` also falls short — the next natural fallback
(not yet formulated) would need to be named explicitly, not faked.

**Watch out.** (1) `S^+`/`S^{++}`'s finiteness needs `I_S` infinite (same
standing unproved-in-general hypothesis flagged for `D_S`/`J_S` in rounds
6–7 — do not silently assume it). (2) Do not claim `S^+` (or `S^{++}`)
closes `Λ_S`-finiteness even if sufficiency is shown for every *tested*
instance — sufficiency must be shown to hold for an *arbitrary* proper core,
not case-by-case, to actually close the problem; report partial/exemplary
sufficiency honestly as such. (3) Share the core-avoiding-witness existence
sub-lemma with `persistent-backbone-monovariant`'s Step 1 this round (prove
once, cite from both files, do not duplicate the proof).

## Round 8 update (headline — read this first)

**Dispatch.** Certify the Freeze-Confinement Corollary; push the `S^+`
(extended-imprint) mechanism toward an `S^{++}` sufficiency fix for the
`S=\{1061\}` counterexample found by round 8's cross-bucket-direct explorer.

**What this round establishes, precisely and honestly (full detail in §H
below).**

1. **The domination half of the Freeze-Confinement Corollary is now fully
   proved, unconditionally given `(MRS_S)`, by a direct 6-line minimality
   argument** (§H Step 1): every realized class-`S` radical — early or late,
   not merely those "past" the freeze index — contains some element of the
   eventually-frozen minimal-radical antichain `𝓜_{n^*}^S`. This is a
   genuine, general, reusable fact (certified below) and fully retires round
   7's "independent depth-hunting via unbounded branching" program (§G Step
   4): the small depth observed there is now *explained* as a downstream
   consequence of this domination fact, not evidence of a self-contained
   well-founded recursion.
2. **The outline's literal follow-on numeric depth-bound formula does NOT
   follow from domination alone — found and corrected before it could be
   miscertified** (§H Step 2). Domination only forces a realized superset to
   *contain* the frozen element (a LOWER bound on how many extra primes it
   needs), never an upper bound on incidental extra primes; I traced the
   natural derivation two different ways and both times got the reverse
   inequality from the one claimed. This is reported as an honest correction
   of the round-8 outline, not a fatal flaw in the underlying diagnosis.
3. **A sharper, precisely-scoped replacement is identified and reported
   honestly as an open conjecture, not a theorem** (§H Step 3, "Singleton
   Recruiter Identity"): when `𝓜_{n^*}^S` is a singleton `\{C'\}` (true for
   both hard-case cores checked), escape depth equals `|C'\setminus\kappa|`
   **exactly**, verified with zero exceptions across all 9 populated-bucket
   data points now on record spanning both hardest known cores. This
   explains and sharpens round 7's empirical Recruiter-Alignment pattern (its
   mysterious `W(a_1)` is `C'\setminus S`, now a provably finite object) but
   is explicitly NOT proved — closing it looks to be of the same difficulty
   as the underlying sufficiency gap itself.
4. **The `S^+` (extended-imprint) Necessity + Finiteness Lemma is certified
   in full** (§H Step 4): every exactly-realized bare value for a proper core
   contains `S^+`, and `S^+` is finite whenever `I_S` is infinite, via a
   one-line application of the already-certified Generalized Lemma C to
   `I_S` (a substitution not previously made explicit for this purpose).
5. **The `S^{++}` sufficiency fix is tested directly against the exact
   failing instance it was designed for (`a_1=21528751,S=\{1061\}`) and
   FAILS — reported honestly, not papered over** (§H Step 5). I prove a
   general **Vacuity Proposition** (`\kappa\subseteq S^+\Rightarrow
   S^{++}_\kappa=S^+` identically) that explains, structurally, why one of
   the two populated buckets gives zero improvement, and show the other
   "succeeds" only degenerately/circularly (a singleton restricted subclass).
   A further general **Intersection-Fragility Proposition** (proved in full)
   shows NO pure intersection-over-a-subclass invariant (`S^+`, `S^{++}`, or
   the already-certified `D_S`) can ever recover a prime absent from even one
   member of the relevant class — exactly the shape of this counterexample
   (the missing prime `11` is absent from exactly `1` of `19` known members).
   This is a genuine, structurally-proved negative result: `S^{++}` as
   literally proposed is a confirmed dead end for this gap; any future fix
   needs a mechanism robust to finitely many exceptions, not set intersection.

**Conclusion.** Two new certified lemmas (Freeze-Confinement Domination
Lemma; `S^+` Necessity + Finiteness Lemma), one honest correction of the
outline's own claimed corollary with the exact obstruction pinned down, one
new precisely-scoped open conjecture replacing it, and one clean, fully
proved negative result (plus the general-purpose Intersection-Fragility
Proposition explaining it). The sufficiency gap for proper cores
(equivalently `(MRS_S)`/local FCBC) remains open. Status stays `partial`.

## §I. The Greedy Augmentation / Termination-Sufficiency scheme, and the refutation of the `S^+`-union candidate (Round 10)

### Setup (extends Theorem SW's notation; self-contained)

Fix a doubly-infinite disjoint core pair `(S,S')` of a fixed `a_1`
(`S,S'\subseteq P_1` nonempty, `S\cap S'=\varnothing`, `I_S,I_{S'}` both
infinite — the exact hypothesis of the Stabilization Conjecture, per the
already-certified `theorem-SW-stabilization-sufficiency.md`). Write
`B_0:=P_1\cup\{2,3,5,7,11,13\}` (finite). For a finite `W\supseteq B_0`,
say `W` is **covering** (for `(S,S')`) if
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap W\ne\varnothing` for every
`i\in I_S,j\in I_{S'}`. The **Stabilization Conjecture** for `(S,S')` is:
some finite covering `W` exists. Note covering-ness is monotone: if
`W\subseteq W'` and `W` is covering, so is `W'` (the intersection can only
grow).

### Step 1 — the Greedy Augmentation Lemma (new, fully proved)

**Definition (the greedy process).** Set `W_0:=B_0`. Suppose `W_t` has been
defined and is **not** covering. Let
`U_t:=\{(i,j)\in I_S\times I_{S'}:\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap
W_t=\varnothing\}\ne\varnothing`. The set `\{\max(i,j):(i,j)\in U_t\}` is a
nonempty subset of `\mathbb N`, hence (well-ordering of `\mathbb N`) has a
least element `m_t`; the pairs `(i,j)` with `i,j\le m_t` are finite in
number, so among those in `U_t` with `\max(i,j)=m_t` there is one,
`(i_t,j_t)`, lexicographically least (a fixed deterministic tie-break).
Define `q_t:=\min\{q\text{ prime}:q\in\mathrm{rad}(a_{i_t})\cap
\mathrm{rad}(a_{j_t}),\,q\notin W_t\}` and `W_{t+1}:=W_t\cup\{q_t\}`. If at
some finite `t=T` the resulting `W_T` **is** covering, the process **halts**
with output `W_T`.

**Lemma (Greedy Augmentation).** (a) At every non-halted step `t`, `q_t` is
well-defined (the minimum above is over a nonempty finite set). (b)
`q_t\notin P_1` for every `t`. (c) The primes `q_0,q_1,q_2,\ldots` produced
before halting (if the process runs for `t` steps without halting) are
pairwise distinct, and `W_t=B_0\cup\{q_0,\ldots,q_{t-1}\}` for every `t`.

**Proof.** (a) By the already-certified **Lemma P′**
(`lemmas/lemma-P-prime-pairwise-intersecting.md`: `\gcd(a_i,a_j)>1` for
every `i<j`, and by symmetry for every `i\ne j`) applied to `i_t\ne j_t`
(distinct since `i_t\in I_S,j_t\in I_{S'}` and `I_S\cap I_{S'}=\varnothing`,
as `S\ne S'$ are distinct nonempty cores — indeed disjoint), `\gcd(a_{i_t},
a_{j_t})>1`, i.e. `\mathrm{rad}(a_{i_t})\cap\mathrm{rad}(a_{j_t})
\ne\varnothing`. Since `(i_t,j_t)\in U_t`, this intersection is disjoint
from `W_t`; so the set defining `q_t` is nonempty, and it is a set of
primes bounded by `a_{i_t}` (hence finite), so the minimum exists. (b)
Since `i_t\in I_S`, `\mathrm{rad}(a_{i_t})\cap P_1=S(i_t)=S` (definition of
the core partition, Theorem CD); likewise
`\mathrm{rad}(a_{j_t})\cap P_1=S'`. Since `S\cap S'=\varnothing`,
`\mathrm{rad}(a_{i_t})\cap\mathrm{rad}(a_{j_t})\cap P_1\subseteq S\cap
S'=\varnothing`. As `q_t\in\mathrm{rad}(a_{i_t})\cap\mathrm{rad}(a_{j_t})`,
`q_t\notin P_1`. (c) By induction on `t`: `W_0=B_0` (empty union, base
case holds vacuously). If `W_t=B_0\cup\{q_0,\ldots,q_{t-1}\}` and the
process has not halted, then by construction `q_t\notin W_t`, so
`q_t\notin\{q_0,\ldots,q_{t-1}\}` — a prime distinct from every earlier one
— and `W_{t+1}=W_t\cup\{q_t\}=B_0\cup\{q_0,\ldots,q_t\}`, completing the
induction. `\blacksquare`

**Remark.** Part (b) proves precisely the claim the round-10 outline's Step
2 asserted informally ("some prime `q_0\notin W` is forced," together with
the unstated-but-needed fact that this prime is genuinely new, not already
inside `P_1`) — here given a complete, self-contained proof from Lemma P′
alone, with no appeal to `(MRS_S)`/`S^+`/any conditional machinery. Part
(c) is what licenses treating "how many distinct primes get adjoined" as a
legitimate finite-or-infinite dichotomy: since the `q_t` are pairwise
distinct, if they were ever confined to a fixed finite set, the process
could not run indefinitely (a pigeonhole fact made precise next).

### Step 2 — the Termination-Sufficiency Lemma (new, fully proved)

**Lemma.** Suppose there is a finite set `K_0` (depending only on
`a_1,S,S'`, not on `t`) such that, for the greedy process of Step 1, every
`q_t` produced while the process has not yet halted satisfies `q_t\in K_0`.
Then the process halts at some step `T\le|K_0|`, and `W_T\subseteq
B_0\cup K_0` is a finite covering set: the Stabilization Conjecture holds
for `(S,S')`.

**Proof.** Suppose, for contradiction, the process does not halt by step
`|K_0|+1$ — i.e. `q_0,\ldots,q_{|K_0|}` are all defined (the process ran at
least `|K_0|+1` non-halted steps). By Lemma (Greedy Augmentation)(c), these
are `|K_0|+1` **pairwise distinct** primes, and by hypothesis every one of
them lies in `K_0`, a set of size `|K_0|`. This is impossible (a set of
`|K_0|+1` pairwise distinct elements cannot inject into a set of size
`|K_0|` — pigeonhole). So the process halts at some step `T\le|K_0|+1`;
tightening: if it has not halted by step `|K_0|`, the same argument with
`|K_0|+1` replaced by `|K_0|` already gives a contradiction once
`q_0,\ldots,q_{|K_0|-1},q_{|K_0|}` (i.e. `|K_0|+1` primes) exist, so in
fact it must halt at some `T\le|K_0|`. When it halts, by definition `W_T`
is covering, and by Lemma (Greedy Augmentation)(c),
`W_T=B_0\cup\{q_0,\ldots,q_{T-1}\}\subseteq B_0\cup K_0`. `\blacksquare`

**Remark.** This Lemma is the rigorous replacement for the round-10
outline's informally-stated "Termination lemma (open, the real content)":
it converts the open content into a clean conditional implication
(`K_0` exists `\Rightarrow` Stabilization Conjecture holds for `(S,S')`),
proved unconditionally here, so that all remaining open content is
isolated exactly in the existence of `K_0` — nothing else. Together, Steps
1–2 fully discharge the "well-ordering setup" and "augmentation" parts of
the outline's Steps 1–3 with complete rigor; only the boundedness of the
recruited primes (the outline's Step 2's "key step," honestly flagged
there as the actual gap) remains.

### Step 3 — the outline's candidate `K_0:=S^+_S\cup S^+_{S'}` is refuted (new computation this round)

**Candidate (as literally proposed by the round-10 outline's Step 2).**
`K_0:=(S^+_S\setminus P_1)\cup(S^+_{S'}\setminus P_1)`, where
`S^+_S:=\bigcap_{i\in I_S}\mathrm{rad}(a_i)` is the already-certified
`S^+` Necessity + Finiteness Lemma object
(`lemmas/lemma-freeze-confinement-domination-and-Splus.md`).

**Fresh computation (this round, own script, not reused from any cached
report — `sympy.primefactors`, exact, no probabilistic shortcuts).** Using
the round-9 cache `/tmp/round-9/work/seq_21528751.pkl`
(`N=3{,}000{,}000$, independently loaded and re-processed here, factorized
member-by-member rather than trusting any prior report's summary numbers):
`a_1=21528751`, `P_1=\{103,197,1061\}`, `(S,S')=(\{1061\},\{103,197\})`.
Classifying all `3{,}000{,}000` terms by `\mathrm{rad}(a_n)\cap P_1$ (cheap
divisibility check, no full factorization needed for the classification
step) gives `|I_{\{1061\}}|=875$, `|I_{\{103,197\}}|=15064$. Factorizing
(via `sympy.primefactors`) every one of these `875+15064=15939` terms and
intersecting:
$$S^+_{\{1061\}}=\{2,3,7,1061\},\qquad S^+_{\{103,197\}}=\{103,197\}.$$
(The first figure matches the round-8 §H table's independently-certified
`19`-member computation done at `N=60000`; the second is new — computed
here for the first time on the `\{103,197\}` side, from all `15064`
members through `N=3{,}000{,}000$, not merely the earlier small-sample
generator value.)

**Observation: `K_0\subseteq B_0` identically — the candidate adds
nothing.** `S^+_{\{1061\}}\setminus P_1=\{2,3,7\}\subseteq\{2,3,5,7,11,13\}
\subseteq B_0`; `S^+_{\{103,197\}}\setminus P_1=\varnothing$ (the
intersection over all `15064$ members of `I_{\{103,197\}}` is exactly the
core itself, `\{103,197\}\subseteq P_1$, with no companion prime common to
*all* of them). So `K_0=\varnothing$ as a genuinely new contribution:
`B_0\cup K_0=B_0` exactly.

**`B_0` alone is not covering (fresh exhaustive check).** Restricting each
term's signature to `\{2,3,5,7,11,13\}` (a bucket-mask, exact — every
`a_n$'s divisibility by each of these `6` small primes is checked directly,
no sampling) and enumerating all realized bucket pairs across the two
sides: exactly `3` bucket-pairs are mutually disjoint (i.e. unresolved by
`B_0`), jointly realized by `94$ of the `875\times15064=13{,}181{,}000`
cross pairs at `N=3{,}000{,}000` (matching the bridge-primes explorer's
independently-cited `94` figure, here reproduced from a from-scratch
re-load and re-factorization of the cache, not copied). Adding the single
prime `97` (verified: `97\notin K_0$, confirming the refutation is not an
artifact of an incomplete `S^+` computation) resolves all `3` bucket-pairs:
exhaustive re-check with `W=B_0\cup\{97\}$ finds **zero** violating bucket
pairs among all realized signatures at `N=3{,}000{,}000`.

**Conclusion.** `K_0:=S^+_S\cup S^+_{S'}` (as literally proposed) is
**refuted** as a candidate for the Termination-Sufficiency Lemma's
hypothesis: it is identically contained in `B_0` for this instance, hence
supplies zero new information, and `B_0` alone is demonstrably not
covering. This is consistent with, and gives an independent, from-scratch
confirmation of, the already-certified **Intersection-Fragility
Proposition** (`lemmas/lemma-vacuity-and-intersection-fragility.md`): `97`
fails to divide `847` of the `875` members of `I_{\{1061\}}` (present in
only `28`) and `14904` of the `15064` members of `I_{\{103,197\}}`
(present in only `160`), so no pure intersection over either whole class
can ever contain it — exactly the mechanism that Proposition already rules
out, now shown to defeat the *union* of two such intersections as well
(the union of two things individually too small to contain `97` is of
course still too small to contain `97`; this was not previously checked
concretely for a cross-core pair, only for a single side's sufficiency
gap in §H).

### Step 4 — the First-`K`-Prefix Recruitment Conjecture (sharper replacement, honestly open)

Since a pure-intersection object cannot supply `K_0` (Step 3, and the
already-certified Vacuity/Intersection-Fragility Propositions), the
natural replacement — matching the outline's own Step 3 intent and the
bridge-primes explorer's empirical "Smooth-Multiple Recurrence" finding —
is a **union**, not an intersection, over a *bounded prefix* of each side.

**Definition.** List `I_S=\{i_1<i_2<\cdots\}`, `I_{S'}=\{j_1<j_2<\cdots\}$.
For `K\in\mathbb N`, define
$$\mathrm{Comp}_K(S):=\bigcup_{l=1}^{K}\bigl(\mathrm{rad}(a_{i_l})
\setminus P_1\bigr),\qquad
\mathrm{Comp}_K(S'):=\bigcup_{l=1}^{K}\bigl(\mathrm{rad}(a_{j_l})
\setminus P_1\bigr)$$
(finite unions of finite sets — finite for every fixed `K`).

**Conjecture (First-`K`-Prefix Recruitment).** For every doubly-infinite
disjoint core pair `(S,S')`, there is a finite `K=K(a_1,S,S')` such that
`W:=B_0\cup\mathrm{Comp}_K(S)\cup\mathrm{Comp}_K(S')` is covering.

**Fresh verification on the hardest instance (this round, exhaustive, not
sampled).** With `K=5` (the smallest `K` for which `97$ enters, since `97`
first appears at prefix position `2` of `I_{\{1061\}}$ — at `a_{596}` —
and at prefix position `5` of `I_{\{103,197\}}$ — at `a_{863}`):
`\mathrm{Comp}_5(\{1061\})=\{2,3,5,7,11,23,47,97\}`,
`\mathrm{Comp}_5(\{103,197\})=\{2,3,5,7,11,13,19,41,59,71,97\}`, giving
`W=\{2,3,5,7,11,13,19,23,41,47,59,71,97,103,197,1061\}` (16 primes).
Exhaustive re-check against **all** `13{,}181{,}000` cross pairs at
`N=3{,}000{,}000`: **zero** violations. (This is a strictly stronger check
than the bridge-primes explorer's own report, which verified
`B_0\cup\{97\}` — here the *mechanism* generating `97` from a bounded
prefix, not just the value `97` itself, is directly exhibited and
verified.)

**Why this is not proved, honestly (this is exactly "Opening B" from the
bridge-primes explorer's report, restated precisely in this file's own
vocabulary).** The Termination-Sufficiency Lemma (Step 2) would close the
Stabilization Conjecture for `(S,S')` **if** the greedy process's forced
primes `q_0,q_1,\ldots` were shown to always lie in
`\mathrm{Comp}_K(S)\cup\mathrm{Comp}_K(S')` for a fixed `K`. Lemma P′
(used in Step 1(a) to produce `q_t`) only guarantees *existence* of a
common prime between `a_{i_t}` and `a_{j_t}` — it says nothing about that
prime's *magnitude* or which earlier-realized term's companion set it
belongs to. Proving "the shared prime forced by two independently-greedy-
constructed branches on disjoint cores is always already a companion of an
early, `N`-independent-bounded member of one side" would require a
genuinely new argument sharpening Lemma P′ from an existence statement to
a magnitude/provenance statement — not attempted successfully in this
workspace across 10 rounds on closely related formulations (the `(UB_S)`,
`S^{++}`, Recruiter-Alignment, and cross-bucket-domination programs all
independently ran into a version of this same "count vs. magnitude"
wall, per `current.md`'s round 8–9 headlines). **This step is not achieved
this round; it is reported honestly as the sole remaining open content of
this approach, not papered over.**

### Reproducibility

All computations in this section use `sympy.primefactors` for exact prime
factorization, on the round-9 cache `/tmp/round-9/work/seq_21528751.pkl`
(`N=3{,}000{,}000$, a pre-existing pickle of the raw sequence values only —
re-classified and re-factorized from scratch by this round's own script,
not by reusing any prior report's derived tables). Scripts:
`/tmp/round-10/proof-builder-fpwo-gen_check2.py`,
`/tmp/round-10/proof-builder-fpwo-analyze2.py` (this round).

## §H. The Freeze-Confinement Domination Lemma, the depth-bound correction, and the `S^+`/`S^{++}` mechanism (Round 8)

### Setup (extends §B/§F/§G's notation; self-contained)

Fix a proper nonempty core `S\subsetneq P_1` with `I_S` infinite (the only
case not already fully resolved — finite `I_S` is unconditionally closed by
§D). Recall from §B: `M_n^S:=\{i\in I_S\cap[1,n]: \text{no }k\in I_S\cap[1,n]
\text{ has }\mathrm{rad}(a_k)\subsetneq\mathrm{rad}(a_i)\}`,
`𝓜_n^S:=\{\mathrm{rad}(a_i):i\in M_n^S\}`. Hypothesis `(MRS_S)`: `\exists n^*`
with `𝓜_n^S=𝓜_{n^*}^S` for all `n\ge n^*`.

### Step 1 — Freeze-Confinement Domination Lemma (certified, unconditional given `(MRS_S)`)

**Lemma.** If `(MRS_S)` holds with freeze index `n^*`, then for **every**
`i\in I_S` (not merely those "past" `n^*`), there exists `C'\in𝓜_{n^*}^S`
with `\mathrm{rad}(a_i)\supseteq C'`.

**Proof.** Fix `i\in I_S`. Let `n:=\max(i,n^*)\ge n^*`, so `i\le n` and, by
`(MRS_S)` (applicable since `n\ge n^*`), `𝓜_n^S=𝓜_{n^*}^S`. Consider
`T:=\{k\in I_S\cap[1,n]:\mathrm{rad}(a_k)\subseteq\mathrm{rad}(a_i)\}`;
`i\in T` (trivially, `\mathrm{rad}(a_i)\subseteq\mathrm{rad}(a_i)`), so
`T\ne\varnothing`, and `T` is finite (`\subseteq[1,n]`). Choose `j^*\in T`
minimizing `|\mathrm{rad}(a_{j^*})|` (exists, `T` finite nonempty). If
`j^*\notin M_n^S`, some `k\in I_S\cap[1,n]` has
`\mathrm{rad}(a_k)\subsetneq\mathrm{rad}(a_{j^*})\subseteq\mathrm{rad}(a_i)`;
then `k\in T` and `|\mathrm{rad}(a_k)|<|\mathrm{rad}(a_{j^*})|`, contradicting
the minimality of `j^*`. So `j^*\in M_n^S`, giving
`\mathrm{rad}(a_{j^*})\in𝓜_n^S=𝓜_{n^*}^S`. Set `C':=\mathrm{rad}(a_{j^*})`; by
construction `C'\subseteq\mathrm{rad}(a_i)`, i.e. `\mathrm{rad}(a_i)
\supseteq C'`. `\blacksquare`

**Remark.** This is the identical minimality argument already certified as
"Local Corollary W3′" (§A, Step 2) and "Step 1" of Local Lemma MS (§A, Step
3), here specialized from the channel index set `J=I_S\cup I_{S'}` to the
single class `I_S` alone; the specialization is valid verbatim because the
proof uses no property of the ambient index set beyond finiteness of its
truncation `\cdot\cap[1,n]`. No new machinery, but this is the first time it
has been stated and applied to a single proper core in isolation (not as
half of a two-sided channel), which is exactly what the round-8 outline's
Step 1 needed. This proof gives a **stronger** conclusion than the outline's
literal statement: domination holds for every `i\in I_S`, with no
restriction to indices "past" `n^*` — an index realized long before `n^*` is
dominated too, since freeze at `n^*` retroactively certifies the eventual
antichain covers everything.

**This fully and rigorously retires round 7's independently-hunted "unbounded
branching tree" concern** (§G Step 4): the branching tree not visibly
terminating is now explained — the small observed depth in practice is a
downstream consequence of this domination fact (once frozen, any realized
value is guaranteed to sit above a fixed finite frozen element), not evidence
that some independent well-founded recursion governs the escape process;
there is no need to look for one.

### Step 2 — Why the outline's literal depth-bound formula does not follow (honest correction)

The round-8 outline additionally claimed: "the escape-recursion depth from
any blocked bare value reachable after `n^*` is bounded by
`\max_{C'\in𝓜_{n^*}^S}|C'\setminus S|`." Recall (§G, Step 2) the realized
escape depth of a blocked bare value `C=S\cup\kappa` is
`d(C):=\min\{|C'|-|C|:C\subsetneq C', C'\text{ realized exactly by some
}a_i,i\in I_S\}`.

**Attempted derivation and where it breaks.** Suppose `C^*` is the (existing,
by hypothesis) smallest realized superset of `C`, realized at some
`i^*\in I_S`, so `d(C)=|C^*|-|C|`. By Step 1 (applied to `i^*`),
`C^*\supseteq C'` for some `C'\in𝓜_{n^*}^S`. If `C'\not\subseteq C`, then
`C^*\supseteq C\cup C'`, giving
$$d(C)=|C^*|-|C|\ \ge\ |C\cup C'|-|C|\ =\ |C'\setminus C|.$$
This is a **lower** bound on `d(C)`, not an upper bound — the reverse of what
the outline claimed. Domination (Step 1) constrains what a realized superset
must *contain* (at least `C'`), but places no ceiling on how many further,
"incidental" extra primes that superset might also carry before it is
actually realized; those extra primes are not controlled by `𝓜_{n^*}^S` at
all. I checked this obstruction is not an artifact of one bad proof attempt
by trying the natural alternative route (applying the trichotomy directly to
`C^*` itself, treating it as a "new arrival") — it produces the identical
inequality `C^*\supseteq C'` and hence the identical lower-bound direction,
not an upper bound. **I could not complete this derivation and do not
certify it.** This is reported as a genuine correction of the round-8
outline, in the same spirit as round 6's refutation of the single-witness
Freeze Criterion and round 7's correction of the "max depth 2" claim — a
real, useful finding for the next round, not a failure to try.

### Step 3 — The Singleton Recruiter Identity (new sharper conjecture, honestly unproved)

**Numerical setup (fresh computation this round; own `sympy.factorint`-based
generator, cross-validated against `/tmp/round-7/seq_21528751_30k.json` and
`/tmp/round-7/seq_2747.json` on their overlapping range before trusting any
extension).** Using `/tmp/round-8/seq_21528751_60k.json` (`n=60000`) and
`/tmp/round-8/seq_2747_40k.json` (`n=40000`):

- `a_1=21528751`, `S=\{197\}`: `|I_S|=1017`. The single-class antichain
  `𝓜_n^S` freezes at `n^*=2575` (last add/remove event, of 43 total) to the
  **singleton** `𝓜_{n^*}^S=\{C'\}`, `C'=\{2,3,7,197\}` — zero further changes
  observed through `n=60000`.
- `a_1=2747`, `S=\{67\}`: `|I_S|=777`. `𝓜_n^S` freezes at `n^*=3` (the very
  first realized class-`\{67\}` term already dominates all subsequent ones,
  a single add event) to the singleton `\{C'\}`, `C'=\{2,3,7,67\}` — zero
  further changes through `n=40000`.

**Identity checked exactly on every populated coarse bucket recorded across
both cores (§G Step 2's original data, re-verified from the cached sequences
this round):**

| `a_1` | `\kappa` | `C'\setminus\kappa` | predicted depth | actual depth (§G) | dominator `=\kappa\cup C'`? |
|---|---|---|---|---|---|
| 21528751 | `\{2,3,197\}` | `\{7\}` | 1 | 1 | yes |
| 21528751 | `\{3,41,197\}` | `\{2,7\}` | 2 | 2 | yes |
| 21528751 | `\{2,193,197\}` | `\{3,7\}` | 2 | 2 | yes |
| 21528751 | `\{2,19,197\}` | `\{3,7\}` | 2 | 2 | yes |
| 21528751 | `\{19,41,197\}` | `\{2,3,7\}` | 3 | 3 | yes (`a_{30017}`) |
| 2747 | `\{2,3,67\}` | `\{7\}` | 1 | 1 | yes |
| 2747 | `\{3,17,67\}` | `\{2,7\}` | 2 | 2 | yes |
| 2747 | `\{2,23,67\}` | `\{3,7\}` | 2 | 2 | yes |
| 2747 | `\{17,23,67\}` | `\{2,3,7\}` | 3 | 3 | yes (`a_{19617}`) |

**Zero exceptions across all 9 rows.** In every instance, `d(\kappa)=
|C'\setminus\kappa|` **exactly** (not merely `\le`), and the minimal realized
superset equals `\kappa\cup C'` exactly (no "incidental" extra primes beyond
exactly what is needed to reach `C'`).

**Conjecture (Singleton Recruiter Identity, unproved).** If
`𝓜_{n^*}^S=\{C'\}` is a singleton, then for every blocked bare value
`\kappa=S\cup Q`, `d(\kappa)=|C'\setminus\kappa|` and the minimal realized
superset equals `\kappa\cup C'`.

**Why this is not proved, honestly.** As Step 2 showed, domination only
forces `d(\kappa)\ge|C'\setminus\kappa|`; the matching upper bound would
require proving `\kappa\cup C'` is **itself** always realized (never further
blocked), which is precisely the kind of "does this specific finite
candidate value actually get hit" statement that is, in general, exactly as
hard as the underlying sufficiency/covering gap this whole approach has
chased since round 3 — proving it in general would essentially resolve
`(MRS_S)` for these cores outright. This conjecture is offered as a
sharpened, precisely-defined, and (unlike Hypothesis (GW)) provably-
well-founded replacement for round 7's Recruiter-Alignment pattern — it
explains *why* that pattern held (the recruiter set `W` was secretly
`C'\setminus S`, a finite object made rigorous the moment `(MRS_S)` holds)
— but it is a conjecture, not a theorem, and is reported as such.

### Step 4 — The `S^+` (extended-imprint) Necessity and Finiteness Lemma (certified)

**Definition.** `S^+:=\bigcap_{i\in I_S}\mathrm{rad}(a_i)`.

**Lemma (`S^+` Necessity + Finiteness).** (a) Every exactly-realized bare
value `C=\mathrm{rad}(a_i)` for `i\in I_S` satisfies `C\supseteq S^+`. (b) If
`I_S` is infinite, `S^+` is finite; explicitly, listing `I_S=\{i_1<i_2<
\cdots\}` and `C_m:=\bigcap_{l=1}^m\mathrm{rad}(a_{i_l})`, there is a finite
`m_0` with `C_m=S^+` for all `m\ge m_0`, and `|S^+|\le\omega(a_{i_1})`.

**Proof.** (a) Immediate from the definition of intersection:
`S^+=\bigcap_{i\in I_S}\mathrm{rad}(a_i)\subseteq\mathrm{rad}(a_i)=C` for the
specific `i` realizing `C`. (b) This is a direct, one-line application of the
already-certified **Generalized Lemma C**
(`lemmas/lemma-C-generalized-subsequence.md`) to the index subsequence
`I=I_S`: `C_m` is non-increasing (each new intersectand can only shrink it)
and bounded below (by `\varnothing`), so it stabilizes at some finite `m_0`,
and (exactly as in the proof of the Single-Companion Finiteness Lemma applied
to `J_S`) the stabilized value `C_{m_0}` equals the full infinite
intersection `S^+`: for `l\le m_0`, `S^+\subseteq C_{m_0}=C_l\subseteq
\mathrm{rad}(a_{i_l})` trivially; for `l>m_0`, stabilization gives
`C_{m_0}=C_{m_0}\cap\mathrm{rad}(a_{i_l})`, so `C_{m_0}\subseteq
\mathrm{rad}(a_{i_l})`; hence `C_{m_0}\subseteq\bigcap_{i\in I_S}
\mathrm{rad}(a_i)=S^+`, and the reverse inclusion `S^+\subseteq C_{m_0}` is
immediate (a full intersection is a subset of any partial one), giving
equality. `|S^+|=|C_{m_0}|\le|C_1|=|\mathrm{rad}(a_{i_1})|=\omega(a_{i_1})`.
`\blacksquare`

**Note on the standing open hypothesis.** As with `D_S`/`J_S` (Single-
Companion Finiteness Lemma, rounds 6–8), "`I_S` infinite" is not proved for a
general proper core `S` — verified numerically in every tested case but not
established in general; this Lemma inherits, not introduces, that gap.

**Numerical confirmation this round.** `7` of `8` core/bucket-family
instances tested by round 8's cross-bucket-direct explorer match
`S^+\setminus P_1` exactly as a **tight** explanation of every populated
bucket's recruited primes; independently cross-checked here by direct
computation for `a_1=21528751,S=\{1061\}` (`S^+=\{2,3,7,1061\}`, matching)
and `a_1=21528751,S=\{197\}` (`S^+`, computed as the intersection of all
`1017` known members' radicals, equals `\{2,3,7,197\}`, matching `C'` from
Step 3 exactly — here the frozen antichain *is* a singleton and coincides
with `S^+`, a consistency check between the two independent mechanisms). One
honest exception: `a_1=21528751,S=\{1061\}` needs an extra prime `11` beyond
`S^+\setminus P_1=\{2,3,7\}` in both of its 2 populated buckets, examined in
full next.

### Step 5 — Testing `S^{++}` on the failing instance, and why it fails (new, this round's genuine attempted content)

**Setup (all fresh computation this round, `a_1=21528751`, `S=\{1061\}`,
using `/tmp/round-8/seq_21528751_60k.json`).** `P_1=\{103,197,1061\}`.
`|I_S|=19`, indices `\{280,596,3741,7201,10658,14118,17577,21037,24495,
27954,31413,34872,38332,41791,45250,48710,52169,55627,59086\}`. Direct
computation of every member's radical (exact factorization,
`sympy.factorint`):
$$\mathrm{rad}(a_{280})=\{2,3,7,11,1061\},\qquad \mathrm{rad}(a_{596})=
\{2,3,5,7,97,1061\},$$
and every one of the remaining 17 members has radical
`\{2,3,7,11,1061\}\cup\{q\}` for one extra prime
`q\in\{5,13,17,19,23,29,47,53,59,61\}` (`q=5` recurs for `4` of the `17`
members, `n=3741,21037,38332,55627`; the other `9` values of `q` occur once
each) or exactly `\{2,3,7,11,1061\}` (`4` members, `n=14118,17577,34872,
41791`). **Every one of these `17` members, and `a_{280}`, contains `11`;
`a_{596}` is the unique exception among all `19`.** Hence
`S^+=\bigcap_{i\in I_S}\mathrm{rad}(a_i)=\{2,3,7,1061\}` (`11` is killed by
`a_{596}` alone; every other prime beyond `\{2,3,7\}` is already killed by
disagreement among the other 18 members).

Applying the already-certified Companion-Disjointness Coarsening Lemma (§F)
with witnesses `j_1=2` (`\mathrm{comp}(a_2)=\{2,41,2549\}`), `j_2=4`
(`\mathrm{comp}(a_4)=\{3,19,193\}`) gives `9` coarse buckets; exactly `2` are
populated (matching round 8's explorer table exactly): `\kappa=\{2,3,1061\}`
(minimal realized dominator `\{2,3,7,11,1061\}`) and `\kappa=\{2,19,1061\}`
(minimal realized dominator `\{2,3,7,11,19,1061\}`). Both dominators need the
extra prime `11`, which is **not** in `S^+\setminus P_1=\{2,3,7\}`.

**Testing `S^{++}_\kappa:=\bigcap_{i\in I_S,\,\kappa\subseteq
\mathrm{rad}(a_i)}\mathrm{rad}(a_i)` on both buckets.**

**Bucket `\kappa=\{2,3,1061\}`.** Since `\{2,3\}\subseteq S^+`, every one of
the 19 members of `I_S` (all of which contain `S^+`, hence `2,3`) satisfies
the restricting condition `\kappa\subseteq\mathrm{rad}(a_i)` trivially. So the
"restricted subclass" is all of `I_S`, unchanged, and `S^{++}_\kappa=
S^+=\{2,3,7,1061\}` — **identical to `S^+`, no improvement; the prediction
still misses `11`.**

**Vacuity Proposition (general, proved here).** *If `\kappa\subseteq S^+`,
then `S^{++}_\kappa=S^+` identically.* **Proof.** Since `S^+\subseteq
\mathrm{rad}(a_i)` for every `i\in I_S` (definition of `S^+` as the
intersection over all of `I_S`), `\kappa\subseteq S^+\subseteq
\mathrm{rad}(a_i)` holds for every `i\in I_S`, so the restricting condition
`\kappa\subseteq\mathrm{rad}(a_i)` used to define `S^{++}_\kappa` is
satisfied by *every* `i\in I_S`, not a proper subset of it — hence
`S^{++}_\kappa=\bigcap_{i\in I_S,\,\kappa\subseteq\mathrm{rad}(a_i)}
\mathrm{rad}(a_i)=\bigcap_{i\in I_S}\mathrm{rad}(a_i)=S^+`. `\blacksquare`
This applies directly to `\kappa=\{2,3,1061\}` (since `\{2,3\}\subseteq
S^+\setminus P_1=\{2,3,7\}`), so the failure above is an instance of a
completely general, provable phenomenon, not a coincidence of this specific
bucket — and it will recur whenever a Coarsening-Lemma bucket's primes happen
to lie inside the already-recruited `S^+`, which is common precisely because
`S^+` is where the "generic" companion primes concentrate.

**Bucket `\kappa=\{2,19,1061\}`.** Here `19\notin S^+` (`19\ne7`), so the
Vacuity Proposition does not apply. Direct computation: among the 19 members
of `I_S`, exactly **one** contains `19`, namely `\mathrm{rad}(a_{45250})=
\{2,3,7,11,19,1061\}`. So the restricted subclass is the singleton
`\{45250\}`, and `S^{++}_\kappa=\mathrm{rad}(a_{45250})=\{2,3,7,11,19,1061\}`
— this does happen to equal the correct dominator exactly. **But this is a
degenerate, circular success, not a genuine derivation**: with only one known
member in the restricted subclass, `S^{++}_\kappa` is trivially equal to that
member's own (already fully known) radical — it is not a prediction computed
independently of already knowing the answer; a second future member of `I_S`
containing `19` with a different (larger or unrelated) radical — not ruled
out by anything proved so far — would only ever *shrink* `S^{++}_\kappa`
further (Intersection-Fragility Proposition below), and could just as easily
destroy the correct answer as confirm it.

**Intersection-Fragility Proposition (general, proved here).** *Let `I` be
any subset of `\mathbb N` and `q` a prime. If `q\notin\mathrm{rad}(a_i)` for
even one `i\in I`, then `q\notin\bigcap_{k\in I}\mathrm{rad}(a_k)`.*
**Proof.** Immediate: `q\notin\mathrm{rad}(a_i)\Rightarrow q\notin
\bigcap_{k\in I}\mathrm{rad}(a_k)`, since the intersection is a subset of
`\mathrm{rad}(a_i)`. `\blacksquare` **Consequence for this problem.** Every
one of `S^+`, `S^{++}_\kappa`, and the already-certified `D_S` (Single-
Companion Finiteness Lemma) is defined as an intersection over some index
subclass. By the Proposition, none of them can *ever* contain a prime that
fails to divide even one member of the relevant subclass — no matter how
large or "typical" that subclass is otherwise. Here, `11` fails to divide
exactly `1` of `19` known members of `I_S` (`a_{596}`), so `11\notin S^+`
**by design**, permanently, regardless of how many further members of `I_S`
are examined (the running intersection is non-increasing, §H Step 4's proof
— once `11` is excluded by `a_{596}` it can never return). **This is not a
fixable defect of the specific bucket choice `\kappa=\{2,3,1061\}` — it is a
structural limitation of the entire family of pure-intersection invariants**
(`S^+`, `S^{++}` as literally defined by the round-8 outline, and `D_S`):
none of them can recover a prime that is "almost always but not quite
always" present in the relevant class, which is exactly the shape of the
`S=\{1061\}` counterexample.

**Honest conclusion of Step 5.** `S^{++}`, as literally proposed by the
round-8 outline, **does not close the `S=\{1061\}` sufficiency gap** — it
either reduces to `S^+` vacuously (whenever `\kappa\subseteq S^+`, which the
Vacuity Proposition shows is unavoidable exactly when the Coarsening Lemma's
witness-recruited bucket primes coincide with primes already inside `S^+`,
a common occurrence, not a rare edge case) or degenerates to a circular
single-member intersection with no genuine predictive content. This is a
real, structurally-proved negative result (via the Intersection-Fragility
Proposition), not merely an unsuccessful search — any future fix for this
sufficiency gap needs a mechanism robust to finitely many exceptional class
members (e.g. a co-finite/"eventually always" notion, or a mechanism from an
entirely different family than set intersection), and identifying which
specific mechanism that should be is left as the concrete open question for
the next round.

### Reproducibility

All computations in this section use `sympy.factorint` for exact prime
factorization (no probabilistic primality shortcuts) on the cached sequence
files `/tmp/round-8/seq_21528751_60k.json` (`n=60000`) and
`/tmp/round-8/seq_2747_40k.json` (`n=40000`), both generated by round 8's
math-explorer and cross-validated against the earlier round-7 caches
`/tmp/round-7/seq_21528751_30k.json`, `/tmp/round-7/seq_2747.json` on their
overlapping index range before being extended — not reused blindly.

## Round 7 Outline (proof-outliner directive — certify the Escape-Confinement
Lemma, target bounded-depth escape recursion; do NOT attempt any bundle-size
or core-size induction, both now provably foreclosed — see
`persistent-backbone-monovariant`'s Round 7 Outline for why)

**Context.** This file's own §F diagnosis ("Why the Coarsening Lemma alone
does not finish the proof") is the sharpest open statement of the shared gap:
blocking a coarse bucket's *bare* value does not block its proper supersets,
and cross-bucket domination for an "escaped" fan was left fully open. This
round's dedicated explorer
(`/tmp/round-7/math-explorer-cross-bucket-domination.md`) found a genuine,
unconditional, proved partial mechanism closing part of this.

**Step 1 — certify the Escape-Confinement Lemma (unconditional, 3 lines from
the already-certified Lemma P′; do this first).**

*Statement.* If bare value `\kappa=S\cup Q` is blocked by witness `j_3`
(`\mathrm{rad}(a_{j_3})\cap\kappa=\varnothing`), then for **every**
`i\in I_S` with `\mathrm{rad}(a_i)\supsetneq\kappa` (an "escape"), some prime
`p\in\mathrm{comp}(a_{j_3}):=\mathrm{rad}(a_{j_3})\setminus P_1` satisfies
`p\in\mathrm{rad}(a_i)`.

*Proof sketch (write up in full rigor).* By Lemma P′, `\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_{j_3})\ne\varnothing`. Since `i\in I_S`, `\mathrm{rad}(a_i)
\cap P_1=S\subseteq\kappa`, and `\kappa\cap\mathrm{rad}(a_{j_3})=\varnothing`
(blocking hypothesis), so `S\cap\mathrm{rad}(a_{j_3})=\varnothing`; the
nonempty intersection above cannot come from `S`, so it comes from
`\mathrm{comp}(a_i):=\mathrm{rad}(a_i)\setminus P_1`, giving the claimed
`p`. `\blacksquare` This converts "escape prime unconstrained" into "escape
prime confined to one fixed, small, enumerable set" — a genuine (if partial)
sharpening: cross-bucket domination becomes finite-branching, not
open-ended, at each step.

**Step 2 — this round's real target: prove the escape-confinement recursion
has uniformly bounded depth.** Applying the Lemma recursively (a candidate
`\kappa\cup\{p\}` may itself be blocked, forcing a further escape confined to
a *new* witness's companion set) was confirmed by the explorer to reach depth
`\ge2` on a concrete instance (`a_1=21528751,S=\{197\}`, bucket
`\{3,41,197\}`) before resolving. **This is a genuinely different
well-founded structure from the now-doubly-refuted size-induction family**
(`|S|`, bundle size `|Q|`) — it is a recursion on nested witness-blocking, not
a reduction of a size-`k` object to a size-`(k-1)` fact, so it is legitimate
to pursue even though raw size-induction is foreclosed; do not conflate the
two. Candidate mechanisms to try: (a) show each recursion step strictly
decreases some measure tied to the blocking witnesses' indices (forcing
termination by well-ordering of `\mathbb{N}`); (b) connect to
`persistent-backbone-monovariant`'s newly-certified Permanent Pair Lemma —
an escape branch that lands on a bundle disjoint from `D_S\setminus P_1` is
*permanent* by that Lemma, so bounding recursion depth may reduce to
bounding how many such permanent landings can occur, the same counting
sub-target flagged in that file's Round 7 Outline Step 3. Report honestly if
no bound is found — a precise "here is exactly where it resists" is valuable.

**Step 3 — do NOT independently develop the "global recruiter set `W(a_1)`"
reformulation here.** The explorer's §4 finding (every proper core of a fixed
`a_1` seems to draw its eventual antichain support from the same small
`S`-independent set `W(a_1)`) is a candidate new reformulation, but it is
**not confirmed** and appears to be in tension with
`persistent-backbone-monovariant`'s own round-7 finding on the *same*
`a_1=21528751`: the depth-2 core `S=\{103,197\}`'s proven-permanent bundle
`\{11,97\}` (Permanent Pair Lemma, `D_S\setminus P_1=\{2,3,7\}` for this `S`
too) lies entirely outside the claimed `W(21528751)=\{2,3,7\}` (which was
only checked against *singleton* cores of this `a_1`). This tension is
assigned to the new `global-recruiter-finiteness` approach this round, not to
this file — keep this file's scope to the local, per-core cross-bucket
mechanism (Steps 1–2 above) so the two approaches do not duplicate effort;
cross-reference the other file's findings but do not re-derive them here.

## Round 7 update (headline — read this first)

**The Escape-Confinement Lemma is now certified in full, self-contained
rigor (§G below), and this round's real target — a uniform bound on
escape-recursion depth — is honestly NOT achieved, with a precisely
diagnosed obstruction and a genuine (but conditional, and not fully
general) empirical pattern found instead. Status remains `partial`.**

1. **Escape-Confinement Lemma — certified (§G, Step 1).** Proved in full
   from the already-certified Lemma P′ alone (3 lines, no new machinery):
   if a coarse bare value `\kappa` is permanently blocked by witness `j_3`,
   every actual "escape" (a realized radical of class `S` properly
   containing `\kappa`) must contain a prime from `\mathrm{comp}(a_{j_3})`,
   the witness's own fixed, finite companion set. This is genuinely new,
   general (not tied to any one `a_1`), and reusable — proposed for
   certification (§G, "Promotable lemmas" below).
2. **Escape-recursion depth: real (data-grounded) depth is `\le2` in
   every instance tested this round** — 13 distinct coarse buckets across
   **two** proper cores of **two** different `a_1` (`21528751,S=\{197\}`:
   9 buckets; `2747,S=\{67\}`: 4 buckets), plus a further check across 6
   more cores of 6 more `a_1` (`247`, `4199`, `385`, `1001`, `1155`, `4087`)
   where the Coarsening Lemma's hypothesis applies at all — **no instance
   of depth `\ge3` was found despite a deliberate, targeted search** (§G,
   Step 2). This is real, new numerical content (13 of the 13 buckets
   independently traced to an exact witness chain and, where populated, an
   exact realized index — not merely a size count).
3. **A genuine, precise, but conditional empirical pattern (§G, Step 3): the
   "Recruiter-Alignment" observation.** In all 13 populated-or-empty buckets
   checked, depth exactly equals `3` minus the number of a fixed 3-element
   "recruiter" set (`\{2,3,7\}` for both `a_1=21528751` and `a_1=2747`,
   matching this round's cross-bucket-domination explorer's `W(a_1)`)
   already present in the bucket's own 2 primes — and every bucket
   containing **zero** recruiter primes is **entirely unpopulated** (zero
   real terms ever land there, checked exhaustively over the tested range)
   rather than harboring a deep escape chain. This would give a clean
   conditional depth bound `\le|W(a_1)|-1`, **but it is only as strong as
   the existence of a fixed finite `W(a_1)` — Hypothesis (GW) — which this
   round's outline-reviewer independently found FALSE in its literal global
   form for nested cores** (`persistent-backbone-monovariant`'s Permanent
   Pair Lemma bundle `\{11,97\}` for `a_1=21528751,S=\{103,197\}` lies
   outside `W(21528751)=\{2,3,7\}`). So this pattern is real and verified
   but explicitly **not** a proof, and not obviously salvageable in full
   generality without first fixing (GW) itself — reported honestly, not as
   a closed mechanism.
4. **A genuine negative finding: the naive full-branching formalization of
   the recursion does not visibly terminate (§G, Step 4).** If one tries to
   turn "bounded depth" into a structural-induction proof by branching on
   *every* prime the confinement set offers at each level (not just the one
   a real term actually uses) and demanding every branch resolve, the tree
   explodes: on the concrete `a_1=21528751,S=\{197\},\kappa=\{3,41,197\}`
   instance, dozens of branches are still unresolved (`depth\_exceeded` or
   no witness/realization found in range) at depth 6, with new, larger,
   apparently-unrelated primes (`29863,29867,52259,104513,20903,\dots`)
   introduced at every successive level and no visible mechanism forcing
   the branching to stop. This is a real, concrete obstruction to proving a
   depth bound by induction on the raw confinement tree — **the true
   (small, `\le2`) depth found in the actually-realized escape paths comes
   from an external fact (domination by a value derived from a *different*
   bucket/witness choice, i.e. the very cross-bucket domination already
   flagged as open in §F), not from anything internal to iterating the
   Escape-Confinement Lemma itself.**

**Conclusion.** Real progress (one newly certified reusable lemma, 13 new
verified data points, a precise if conditional pattern, and a precisely
located obstruction), but the round's central ask — a uniform,
unconditional escape-recursion depth bound — is **not achieved**. This is
reported honestly as `partial`/CHANGES REQUESTED, not oversold.

## §G. The Escape-Confinement Lemma (certified) and the escape-recursion
depth investigation (Round 7)

### Setup (extends §F's notation; self-contained)

Fix a proper nonempty core `S\subsetneq P_1` with `I_S\ne\varnothing`, and
suppose the Companion-Disjointness Coarsening Lemma's hypothesis holds for
`S` (indices `j_1\ne j_2` with `G_{j_1}\cap S=G_{j_2}\cap S=\varnothing` and
disjoint nonempty `\mathrm{comp}(a_{j_1}),\mathrm{comp}(a_{j_2})`), giving
the finite bucket family `\mathcal K` and, for each `\kappa\in\mathcal K`,
the bare value `S\cup\kappa`. Recall from §F: a bare value `C` is
**blocked** by an index `j_3` if `\mathrm{rad}(a_{j_3})\cap C=\varnothing`
(Permanent-Inadmissibility then forbids `C` from ever being realized
exactly past `j_3`). Call an index `i\in I_S` with `\mathrm{rad}(a_i)
\supsetneq C` (for a blocked `C=S\cup\kappa`) an **escape** from `C`.

### Step 1 — The Escape-Confinement Lemma (certified)

**Lemma (Escape-Confinement).** Let `C:=S\cup\kappa` be a bare value
blocked by witness `j_3` (`\mathrm{rad}(a_{j_3})\cap C=\varnothing`). Then
for **every** escape `i` (i.e. every `i\in I_S` with `\mathrm{rad}(a_i)
\supsetneq C`), there exists a prime
$$p\in\mathrm{comp}(a_{j_3}):=\mathrm{rad}(a_{j_3})\setminus P_1$$
with `p\in\mathrm{rad}(a_i)`.

**Proof.** By the already-certified **Lemma P′** (pairwise global
intersection, unconditional for every pair of indices of the whole infinite
sequence), `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_{j_3})\ne\varnothing`. Since
`i\in I_S`, `\mathrm{rad}(a_i)\cap P_1=S`. Since `S\subseteq C` and
`C\cap\mathrm{rad}(a_{j_3})=\varnothing` (the blocking hypothesis),
`S\cap\mathrm{rad}(a_{j_3})=\varnothing`. Hence the nonempty intersection
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_{j_3})` cannot be witnessed by any
element of `S=\mathrm{rad}(a_i)\cap P_1`; it must come from
`\mathrm{comp}(a_i):=\mathrm{rad}(a_i)\setminus P_1`. So there is
`p\in\mathrm{comp}(a_i)\cap\mathrm{rad}(a_{j_3})`. Since `p\notin P_1`,
`p\in\mathrm{rad}(a_{j_3})\setminus P_1=\mathrm{comp}(a_{j_3})`, as claimed.
`\blacksquare`

**Discussion.** This converts the a priori unconstrained statement "some
extra prime `q` may be appended to a blocked bare value, for arbitrarily
many `q`" into "the extra prime is confined to one specific, finite, fixed
set determined by the single witness that did the blocking" — a genuine
sharpening of what §F's honest diagnosis left open, though (as Steps 2–4
below show precisely) it is not by itself sufficient to bound anything.

**Iterated form (immediate, not a new proof).** If `C':=C\cup\{p\}` (for
`p` as furnished by the Lemma) is *itself* blocked by some (possibly
different) witness `j_3'`, the Lemma applies again verbatim with `C'` in
place of `C` (nothing in the proof used any property of `C` beyond
`C\supseteq S` and `C\cap\mathrm{rad}(a_{j_3})=\varnothing`, both of which
persist under the substitution). So the Lemma can be iterated as many times
as blocking continues to occur, defining an **escape-recursion**: a chain
`\kappa=\kappa_0\subsetneq\kappa_1\subsetneq\cdots` of candidate bundles,
each obtained from the last by adjoining one confinement prime, terminating
(if it terminates) either when some `\kappa_t` is itself realized exactly,
or when the confinement set at some stage offers no prime outside
`\kappa_t` (an uninformative/stuck step — see Step 4).

### Step 2 — Real (data-grounded) escape depth: `\le2` in every case tested

Define, for a blocked bare value `C=S\cup\kappa`, the **realized escape
depth** `d(C):=\min\{|C'|-|C| : C\subsetneq C'\text{ and }C'\text{ is
realized exactly by some }a_i,\ i\in I_S\}$ (the number of extra primes
needed to reach an *actually realized* superset — undefined/`\infty` if no
realized superset exists in the tested range).

**Fresh computation this round** (code:
`/tmp/round-7/builder-fpwo/real_depth.py`, `escape_tree.py`; independent of
any prior round's scripts, built from scratch on the certified sequence
caches `/tmp/round-7/seq_*.json`, `seq_21528751_30k.json`):

- **`a_1=21528751`, `S=\{197\}`** (`j_1=2,j_2=4`, `\mathrm{comp}(a_2)=
  \{2,41,2549\}`, `\mathrm{comp}(a_4)=\{3,19,193\}`, 9 buckets). Of the 9,
  **5 are entirely unpopulated** (zero terms of `I_{\{197\}}` ever have
  radical containing that bare value, checked exhaustively through
  `n=30000`: `\{41,193\},\{19,41\},\{3,2549\},\{193,2549\},\{19,2549\}`,
  each paired with `197`) and **4 are populated with depth exactly `2`**:
  - `\{3,41,197\}`: blocked by `j_3=5` (`\mathrm{rad}(a_5)=21529060=
    2\cdot5\cdot7\cdot103\cdot1493`, `\mathrm{comp}=\{2,5,7,1493\}`).
    Escape adds `2`: `\{2,3,41,197\}`, itself blocked by `j=10`
    (`\mathrm{comp}=\{7,13,2297\}`). Escape adds `7`:
    `\{2,3,7,41,197\}`, **realized exactly at `a_{1291}`** (independently
    recomputed, matches the round-7 explorer's finding exactly).
  - `\{2,193,197\}` (new this round, not in the explorer's report): blocked
    by `j_3=8` (`a_8=21529575=3\cdot5\cdot103\cdot929`,
    `\mathrm{comp}=\{3,5,929\}`). Escape adds `3`: `\{2,3,193,197\}`,
    blocked by `j=10` (`\mathrm{comp}=\{7,13,2297\}`). Escape adds `7`:
    `\{2,3,7,193,197\}`, **realized exactly at `a_{5844}`**.
  - `\{2,19,197\}` (new this round): identical chain (`j_3=8\to`add `3\to`
    blocked by `j=10\to`add `7`), **realized exactly at `a_{7831}`**.
  - `\{2,3,197\}`: blocked by `j=10` directly (`\mathrm{comp}=
    \{7,13,2297\}`), escape adds `7`: `\{2,3,7,197\}`, realized (matches
    the already-certified `S=\{197\}` final-antichain value, collapse at
    `n=2575` per the round-7 explorer). **Depth `1`**, not `2` — the
    smallest depth among the four populated buckets.
- **`a_1=2747`, `S=\{67\}`** (`j_1=2,j_2=4`, `\mathrm{comp}(a_2)=\{2,17\}`,
  `\mathrm{comp}(a_4)=\{3,23\}`, 4 buckets). One bucket, `\{17,23,67\}`, has
  **zero occupants** (checked exhaustively through `n=6000`). The other
  three are
  populated: `\{2,3,67\}` depth `1` (dominator `\{2,3,7,67\}`); `\{3,17,67\}`
  depth `2` (dominator `\{2,3,7,17,67\}`); `\{2,23,67\}` depth `2`
  (dominator `\{2,3,7,23,67\}`).
- **Six further cores checked** (`a_1=247,S\in\{\{13\},\{19\}\}`;
  `a_1=4199,S\in\{\{13\},\{19\},\{13,19\}\}`; `a_1=385,S=\{5\}`), wherever
  the Coarsening Lemma's hypothesis holds at all: **every** bucket found is
  either unpopulated or has depth `\le1`. (`a_1=4087,1001,1155` and several
  other cores of `4199,385` have **no** disjoint-companion witness pair at
  all in the tested range — the Coarsening Lemma is simply inapplicable
  there, a separate, already-known limitation, re-confirmed broadly this
  round: it is common, not rare, for a companion set of small `a_1` to be
  vacuous of any disjoint pair, typically because `2` divides essentially
  every witness's companion set.)

**Summary: across 13 populated-or-empty buckets spanning 2 cores of the
two hardest known `a_1`, plus 6 more cores of smaller `a_1`, the maximum
realized escape depth found is `2`, and no instance of depth `\ge3` was
found despite deliberately searching cores/buckets likely to be hard**
(the 3-prime-core, 9-bucket case `a_1=21528751,S=\{197\}` was the single
best candidate for deeper recursion and still tops out at `2`).

### Step 3 — The Recruiter-Alignment pattern (real, verified, but conditional — not a proof)

**Observation.** Let `W:=\{2,3,7\}` for both `a_1=21528751` and `a_1=2747`
(matching this round's cross-bucket-domination explorer's empirically-found
`W(a_1)`, §4 of `/tmp/round-7/math-explorer-cross-bucket-domination.md`).
For every one of the 13 buckets checked in Step 2:
$$d(S\cup\kappa)\ =\ 3-|\kappa\cap W|\quad\text{whenever }S\cup\kappa\text{ is
populated, and }|\kappa\cap W|=0\implies S\cup\kappa\text{ is unpopulated.}$$
Checked exactly: `\{2,3,197\}` (`|\kappa\cap W|=2`, depth `1=3-2`);
`\{3,41,197\},\{2,193,197\},\{2,19,197\}` (`|\kappa\cap W|=1` in each,
depth `2=3-1`); the 5 unpopulated `S=\{197\}` buckets and the 1 unpopulated
`S=\{67\}` bucket all have `\kappa\cap W=\varnothing`. Symmetric match on
`a_1=2747`: `\{2,3,67\}` (`|\kappa\cap W|=2`, depth `1`); `\{3,17,67\},
\{2,23,67\}` (`|\kappa\cap W|=1` each, depth `2`); `\{17,23,67\}`
(`\kappa\cap W=\varnothing`, unpopulated). **Zero exceptions across all 13
buckets.**

**Why this is not a proof, honestly.** This pattern, if it held in general,
would give a clean conditional bound `d(C)\le|W(a_1)|-1` for any populated
bucket. But it presupposes a single, `S`-independent, finite recruiter set
`W(a_1)` — exactly **Hypothesis (GW)** — which this round's
outline-reviewer independently refuted in its literal global form: for
`a_1=21528751`'s **nested** core `S=\{103,197\}`, the (already-certified,
via `persistent-backbone-monovariant`'s Permanent Pair Lemma) permanent
bundle `\{11,97\}` lies entirely **outside** `W(21528751)=\{2,3,7\}` — so
whatever recruits that bundle, it is not the same fixed `W(a_1)` this
pattern relies on. The pattern above is checked only for **singleton**
cores (`\{197\},\{67\}`), exactly the sub-case the outline-reviewer flagged
as unaffected by the nested-core counterexample — so it is not internally
contradicted by that refutation, but it is not established for nested cores
either, and no proof that it holds even for singleton cores in general was
found this round. Reported as a real, verified, but strictly empirical and
conditional pattern — not a lemma, not a bound, not cited as closing
anything.

### Step 4 — Why the naive branching recursion does not visibly terminate (honest obstruction)

The natural way to try to turn the Escape-Confinement Lemma into a *proof*
of a uniform depth bound is structural induction on the confinement tree:
at each blocked `\kappa`, branch on **every** prime the confinement set
offers (not only the one a real term happens to use), and show every
branch resolves (reaches a realized value, or a "stuck" node with no new
primes to offer) within a bounded number of levels.

**This does not work, concretely.** Exploring the full branching tree
rooted at `a_1=21528751,S=\{197\},\kappa=\{3,41,197\}` to depth 6 (code:
`escape_tree.py`, run against `seq_21528751_30k.json`, memoized, budget-
capped at 4000 nodes — the run completed within budget, it did not hit the
cap): dozens of leaves remain either `depth\_exceeded` (still blocked, still
branching, at depth 6) or `unresolved` (no blocking witness found and not
realized, within the tested range, `n\le30000`) — the tree does not close
up. New, large, mutually distinct primes are introduced at every
successive level with no visible pattern forcing them to run out: level 1
introduces `\{2,5,7,1493\}`; level 2 (from the `+5` branch) introduces
`\{2,23,71\}`; level 3 introduces `\{2,104513\}`; level 4 introduces
`\{2,5,20903\}`; level 5 introduces `\{2,17,29,53\}`; level 6 introduces
`\{2,52259\}` — each a *different* witness's companion set, apparently
unrelated to the ones before it. (Full tree printout, ~150 lines, retained
at `/tmp/round-7/builder-fpwo/escape_tree.py` output; not reproduced in
full here for length, but the branching pattern is exactly as described.)

**Interpretation.** This is a real, concrete obstruction to this specific
proof strategy — not merely "not yet found," but a demonstrated failure of
the natural approach: the raw confinement recursion, taken as an abstract
branching process over *all* syntactically possible extensions, shows no
sign of the well-foundedness a bounded-depth theorem would need. The
*actual* small depth found in Step 2 is not explained by this branching
process terminating — it is explained by the fact that the real,
data-realized escape values happen to get **directly and immediately
dominated once realized** (e.g. `\{2,3,7,41,197\}`, realized at depth 2, is
later swallowed by the shorter, independently-realized `\{2,3,7,197\}` from
a *different* bucket path — exactly as already noted by the round-7
explorer). In other words: **the mechanism actually bounding depth in
practice is cross-bucket domination (the same open gap §F already
diagnosed), not anything internal to the Escape-Confinement recursion.**
This round's attempt to find a *different*, self-contained well-founded
measure (as the outline hoped, distinct from the now-foreclosed
bundle-size/`|S|`-size families) has not succeeded: the escape-recursion,
examined honestly, reduces back to the same residual cross-bucket
difficulty rather than resolving it independently.

### Honest summary of §G

1. Escape-Confinement Lemma: **proved, certified, general-purpose.**
2. Uniform depth bound: **not found.** Real depth is `\le2` in all 13
   instances checked (new, verified data), a genuinely useful negative
   search result (no depth-`\ge3` example found), but not a proof of any
   bound.
3. A clean conditional pattern (depth `=3-|\kappa\cap W(a_1)|`) was found
   and verified exactly on every instance checked, but it presupposes
   Hypothesis (GW), independently refuted (in its global, all-cores form)
   by this round's outline-reviewer — so it is not a route to an
   unconditional bound as stated, only a restatement of the same
   dependency.
4. The natural proof strategy for depth-boundedness (structural induction
   on the full confinement-branching tree) demonstrably fails to visibly
   terminate on a concrete case — a real obstruction, not a gap in effort.
5. **This approach's residual open gap is unchanged in substance**:
   cross-bucket domination (§F) is still the thing actually doing the work
   whenever depth stays small, and it is not established in general. The
   escape-recursion, while a legitimately different-looking well-founded
   structure from bundle-size/`|S|`-induction (as the outline correctly
   noted), does not, on this round's investigation, turn out to be an
   *independent* route to closing the gap — it is entangled with the same
   cross-bucket difficulty, not a way around it.

## Round 6 update (headline — read this first)

**Dispatch.** Fill in the Round-6-outline's open Freeze Criterion: find a
correct criterion distinguishing "proper core `S` permanently freezes" from
"`S` undergoes collapses," working correctly on both the confirmed freeze
example (`a_1=247`, `S=\{13\},\{19\}`) and the confirmed collapse example
(`a_1=2747`, `S=\{41\}`), and prove the collapse case is still finite
(bounded collapse count).

**What this round establishes, precisely, and honestly.**

1. **The outline's literal Step-2 Freeze Criterion (a single witness `j_S`
   blocking *every* candidate extension `C\supsetneq S`) is FALSE as stated
   — refuted directly on the very case it was designed for.** Working out
   `a_1=247`, `S=\{13\}` by hand (§F below): the single witness `a_3=266`
   (`\mathrm{rad}=\{2,7,19\}`) blocks only candidates disjoint from
   `\{2,7,19\}`; it does **not** block, e.g., `\{2,13\}` or `\{3,13\}` or
   `\{7,13\}` (each shares a prime with `\{2,7,19\}`). The freeze in this
   example genuinely requires **at least two** witnesses with **disjoint**
   companion primes (`a_3`, companion `\{2,7\}`, and `a_5=285`, companion
   `\{3,5\}`), not one. So the outline's Step 2 as literally written needed
   correction, not just completion; this round replaces it with a corrected,
   fully proved mechanism.
2. **New: the Companion-Disjointness Coarsening Lemma (§F, proved in full,
   unconditional, using only the already-certified Lemma P′).** If two
   indices `j_1,j_2` exist with `G_{j_1}\cap S=G_{j_2}\cap S=\varnothing` and
   disjoint nonempty "companion" sets `\mathrm{comp}(a_{j_1})\cap
   \mathrm{comp}(a_{j_2})=\varnothing` (where `\mathrm{comp}(a_j):=
   \mathrm{rad}(a_j)\setminus P_1`), then **every** term of class `I_S`, at
   every index past or future, has radical containing `S\cup\{p,p'\}` for
   some `p\in\mathrm{comp}(a_{j_1})`, `p'\in\mathrm{comp}(a_{j_2})` — a fixed
   fan of at most `|\mathrm{comp}(a_{j_1})|\cdot|\mathrm{comp}(a_{j_2})|`
   "coarse buckets." This is a real, new, rigorously proved structural
   result, not previously in the population.
3. **Verified in complete numerical/hand detail on both mandatory examples
   (§F), and the criterion correctly separates them:**
   - `a_1=247`, `S=\{13\}`: two disjoint-companion witnesses exist
     (`j_1=3,j_2=5`), giving exactly 4 coarse buckets; 3 of the 4 are
     realized exactly (matching the final 3-element antichain found in round
     5) and the 4th (`\{5,7\}`) is shown, by direct application of the
     already-certified Permanent-Inadmissibility Lemma with a **third**
     witness `a_7` (companion `\{2,3\}`, disjoint from `\{5,7\}`), to be
     permanently blocked at its bare value — fully explaining the observed
     freeze, not just restating it.
   - `a_1=2747`, `S=\{41\}`: **no two disjoint-companion witnesses exist**
     (checked exhaustively over every witness through `n=400` — every single
     one has companion set `\supseteq\{2,3,7\}`, so no two are disjoint) —
     the Coarsening Lemma's hypothesis genuinely fails here, correctly
     explaining (not just numerically confirming) why this channel does
     **not** freeze via this mechanism and instead grows an unbounded-until-
     absorbed fan of the shape `\{7,q,41\}`.
4. **The second half of the dispatch — proving the collapse case (b) is
   still finite in general — is NOT closed this round, and I am reporting
   this honestly rather than overclaiming.** The natural completion of the
   Coarsening Lemma into a full freeze/finiteness proof runs into a genuine
   additional obstruction, found and precisely diagnosed this round (§F,
   "Why the Coarsening Lemma alone does not finish the proof"): blocking the
   *bare* value of a coarse bucket (Permanent-Inadmissibility) does **not**
   block proper supersets of that bare value within the same bucket, so a
   "blocked bucket" can still, in principle, harbor an unboundedly growing
   fan of its own unless that fan is independently dominated by an
   *already-realized* minimal value from a **different** bucket — a
   genuinely cross-bucket phenomenon that the Coarsening Lemma alone does not
   control. Closing this is, on inspection, of the same essential difficulty
   as the shared open gap (`(MRS_S)`/companion-count boundedness) attacked by
   every sibling approach; no new mechanism closing it was found this round.

**Conclusion.** Real, new, fully proved structural content this round (the
corrected Coarsening Lemma, §F), verified against both mandatory examples
with the correct mechanism identified in each. The dispatch's second ask
(prove case (b) finite in general) is **explicitly not achieved** — reported
as an honest gap, not papered over. Status remains `partial`.

## §F. The Companion-Disjointness Coarsening Lemma (Round 6, replaces the
refuted single-witness Freeze Criterion)

### Setup (matches §A–§E notation)

Fix a proper nonempty core `S\subsetneq P_1`. Recall `G_i:=\mathrm{rad}(a_i)
\cap P_1` (Lemma P: `G_i\ne\varnothing$ always), `I_S:=\{i:G_i=S\}`. For any
index `j`, write `\mathrm{comp}(a_j):=\mathrm{rad}(a_j)\setminus P_1` (the
"companion" primes of `a_j`, i.e. its prime factors outside `P_1`).

**Refutation of the outline's literal Step 2, worked by hand.** The outline
proposed: a single witness `j_S` (first index with `G_{j_S}\cap S=
\varnothing`) blocking *every* candidate extension of `S` suffices for
freeze. On `a_1=247`, `S=\{13\}`: the sequence begins `a_1=247=13\cdot19`,
`a_2=260=2^2\cdot5\cdot13`, `a_3=266=2\cdot7\cdot19`, `a_4=273=3\cdot7\cdot
13`, `a_5=285=3\cdot5\cdot19`, `a_6=312=2^3\cdot3\cdot13`, `a_7=342=2\cdot
3^2\cdot19`. Here `j_S=3` (`\mathrm{rad}(a_3)=\{2,7,19\}`, disjoint from
`\{13\}`). By the (already-certified, elementary) **Permanent-Inadmissibility
Lemma** — *if some index `j` has `\mathrm{rad}(a_j)\cap C=\varnothing` for a
candidate radical `C`, no term with radical exactly `C` can appear at any
index `>j`, since admissibility requires `\gcd(x,a_i)>1` for every `i\le n`
including `i=j`, and this requirement is never relaxed as `n` grows* — the
witness `a_3` blocks every `C` disjoint from `\{2,7,19\}`. But `C=\{2,13\}`
is **not** disjoint from `\{2,7,19\}` (shares `2`), so `a_3` does **not**
block it; nor does `a_3` block `\{3,13\}$ or `\{7,13\}$ similarly (share `7`
resp. neither, but `\{3,13\}` is not disjoint from... wait check directly:
`\{3,13\}\cap\{2,7,19\}=\varnothing`, so `a_3` *does* block `\{3,13\}`; the
point still stands for `\{2,13\}` and `\{7,13\}`, each of which intersects
`\{2,7,19\}` and is therefore not blocked by `a_3` alone). Yet none of
`\{2,13\},\{3,13\},\{7,13\},\{13\}` is ever realized as an exact radical
across the whole tested range (`n=15000`, round 5 §E) — so something *beyond*
the single witness `a_3` is doing the blocking. This is the refutation: a
single witness is demonstrably insufficient to account for the observed
freeze; **at least two** witnesses, used jointly, are needed, as the Lemma
below makes precise.

### The Coarsening Lemma

**Lemma (Companion-Disjointness Coarsening).** Let `S\subsetneq P_1` be
nonempty with `I_S\ne\varnothing`. Suppose there exist indices `j_1\ne j_2`
with `G_{j_1}\cap S=\varnothing`, `G_{j_2}\cap S=\varnothing`, and
`\mathrm{comp}(a_{j_1})\cap\mathrm{comp}(a_{j_2})=\varnothing`, with both
`\mathrm{comp}(a_{j_1})` and `\mathrm{comp}(a_{j_2})` nonempty. Then for
**every** `i\in I_S$ (of the whole infinite sequence, regardless of whether
`i` is `<j_1,j_2`, between them, or later), there exist `p\in
\mathrm{comp}(a_{j_1})`, `p'\in\mathrm{comp}(a_{j_2})` with
`\{p,p'\}\subseteq\mathrm{rad}(a_i)`. Consequently every `T\in𝓜_n^S` (for
every `n`) satisfies `T\supseteq S\cup\{p,p'\}` for some
`(p,p')\in\mathrm{comp}(a_{j_1})\times\mathrm{comp}(a_{j_2})` — i.e. `𝓜_n^S`
refines the fixed finite set of at most
`|\mathrm{comp}(a_{j_1})|\cdot|\mathrm{comp}(a_{j_2})|` "coarse buckets"
`\mathcal K:=\{S\cup\{p,p'\}:p\in\mathrm{comp}(a_{j_1}),p'\in
\mathrm{comp}(a_{j_2})\}`.

**Proof.** Fix `i\in I_S`, so `\mathrm{rad}(a_i)=S\cup Q` for some `Q`
disjoint from `P_1` (by definition of `I_S`: `\mathrm{rad}(a_i)\cap P_1=S`,
so `Q:=\mathrm{rad}(a_i)\setminus P_1$ is disjoint from `P_1`). By the
already-certified **Lemma P′** (pairwise global intersection, holds
unconditionally for every pair of indices of the whole infinite sequence),
`\gcd(a_i,a_{j_1})>1`, i.e. `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_{j_1})\ne
\varnothing`. Now
$$\mathrm{rad}(a_i)\cap\mathrm{rad}(a_{j_1})=(S\cup Q)\cap(G_{j_1}\cup
\mathrm{comp}(a_{j_1}))=(S\cap G_{j_1})\cup(S\cap\mathrm{comp}(a_{j_1}))
\cup(Q\cap G_{j_1})\cup(Q\cap\mathrm{comp}(a_{j_1})).$$
`S\cap G_{j_1}=\varnothing` by hypothesis. `S\cap\mathrm{comp}(a_{j_1})=
\varnothing` since `S\subseteq P_1` and `\mathrm{comp}(a_{j_1})\cap P_1=
\varnothing` by definition. `Q\cap G_{j_1}=\varnothing` since `Q\cap P_1=
\varnothing` and `G_{j_1}\subseteq P_1`. So the only term that can be
nonempty is `Q\cap\mathrm{comp}(a_{j_1})`, forcing
`Q\cap\mathrm{comp}(a_{j_1})\ne\varnothing`: some `p\in\mathrm{comp}(a_{j_1})$
lies in `Q\subseteq\mathrm{rad}(a_i)`. The identical argument with `j_2` in
place of `j_1` gives `p'\in\mathrm{comp}(a_{j_2})\cap Q$. Since
`\mathrm{comp}(a_{j_1})\cap\mathrm{comp}(a_{j_2})=\varnothing`, `p\ne p'`
automatically, and both lie in `\mathrm{rad}(a_i)=S\cup Q`. So
`\{p,p'\}\subseteq\mathrm{rad}(a_i)`, i.e. `\mathrm{rad}(a_i)\supseteq
S\cup\{p,p'\}$ with `(p,p')\in\mathrm{comp}(a_{j_1})\times\mathrm{comp}
(a_{j_2})`, as claimed. Since `𝓜_n^S\subseteq\{\mathrm{rad}(a_i):i\in I_S\}`
for every `n` (by construction), the antichain statement follows
immediately. `∎`

**Degenerate-case remark (why nonemptiness of both companion sets is not an
extra restriction, just a needed hypothesis check).** If
`\mathrm{comp}(a_{j_1})=\varnothing` (so `\mathrm{rad}(a_{j_1})=G_{j_1}
\subseteq P_1\setminus S`) while `G_{j_1}\cap S=\varnothing`, the same
computation as in the proof gives, for any `i\in I_S`: `\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_{j_1})=\varnothing` always (the `Q\cap\mathrm{comp}(a_{j_1})`
term is `Q\cap\varnothing=\varnothing` too), contradicting Lemma P′. So if
such a `j_1` exists, `I_S=\varnothing` — the core `S` is never realized at
all, and `(MRS_S)` holds trivially (vacuously, `𝓜_n^S=\varnothing` for every
`n`). This case is excluded by the standing hypothesis `I_S\ne\varnothing`
in the Lemma statement, consistently.

**Corollary (Bucket exclusion via Permanent-Inadmissibility).** For a coarse
bucket `\kappa=\{p,p'\}\in\mathcal K$ (notation as above), if there exists an
index `j_3` (any index, not required to satisfy `G_{j_3}\cap S=\varnothing`)
with `\mathrm{rad}(a_{j_3})\cap(S\cup\kappa)=\varnothing`, then the bare value
`S\cup\kappa` is never realized as an exact radical at any index `>j_3`, by
direct application of the Permanent-Inadmissibility Lemma with `C:=S\cup
\kappa`.

### Full worked verification on `a_1=247`, `S=\{13\}` (both mandatory checks)

Sequence (first 7 terms, exact factorizations, independently recomputed this
round): `a_1=247=13\cdot19`, `a_2=260=2^2\cdot5\cdot13`, `a_3=266=2\cdot
7\cdot19`, `a_4=273=3\cdot7\cdot13`, `a_5=285=3\cdot5\cdot19`,
`a_6=312=2^3\cdot3\cdot13`, `a_7=342=2\cdot3^2\cdot19`.

Take `j_1=3` (`G_3=\{19\}$, disjoint from `S=\{13\}`; `\mathrm{comp}(a_3)=
\{2,7\}`) and `j_2=5` (`G_5=\{19\}`, disjoint from `S`; `\mathrm{comp}(a_5)=
\{3,5\}`). `\{2,7\}\cap\{3,5\}=\varnothing`, both nonempty: the Coarsening
Lemma's hypothesis holds. `\mathcal K=\{2,7\}\times\{3,5\}=\{\{2,3\},\{2,5\},
\{7,3\},\{7,5\}\}` — 4 coarse buckets, giving candidate bare values
`\{2,3,13\},\{2,5,13\},\{3,7,13\},\{5,7,13\}`.

**Realized buckets (matches round 5's independently confirmed final
antichain exactly):** `\{2,5,13\}` is realized at `a_2$ (`a_2=260`, first
occurrence, matching Lemma FOM: `T_{\{2,5,13\}}=2\cdot5\cdot13=130<247`, so
by the greedy rule the actual first-occurrence value is the least integer
`>a_1=247` with radical `\{2,5,13\}`, which is `260=2^2\cdot5\cdot13`,
exactly `a_2`). `\{3,7,13\}` is realized at `a_4=273=3\cdot7\cdot13`.
`\{2,3,13\}` is realized at `a_6=312=2^3\cdot3\cdot13`. Three of the four
buckets are hit exactly, matching round 5's independently-confirmed final
3-element antichain `\{\{2,5,13\},\{3,7,13\},\{2,3,13\}\}` precisely.

**Excluded bucket (this round's new explanation of the "missing" 4th
element):** `\{5,7,13\}` — apply the Bucket-Exclusion Corollary with
`j_3=7`: `\mathrm{rad}(a_7)=\{2,3,19\}`, and `\{2,3,19\}\cap\{5,7,13\}=
\varnothing`. So `\{5,7,13\}` is permanently blocked from index `7` onward
by the Permanent-Inadmissibility Lemma — it can never be realized as an exact
radical. This is a **complete, rigorous explanation**, not merely a
numerical observation, of why the final antichain has exactly 3 (not 4)
elements: all 4 candidate coarse bare values are accounted for (3 realized,
1 permanently blocked), and — since every future class-`\{13\}` term's
radical is, by the Coarsening Lemma, a superset of `S\cup\kappa` for one of
these 4 `\kappa`, and the blocked one can never itself be hit exactly while
larger radicals containing it are already dominated by whichever of the
other 3 (already-realized) buckets they also happen to be supersets of — the
antichain content is fully pinned down by index `7`. (The subtlety of
whether a radical `\supsetneq S\cup\kappa_{\text{blocked}}` might still slip
through undominated is addressed honestly below — in this specific example
it does not, verified numerically through `n=15000` with zero further
changes, but this is not yet shown to hold in general; see "Why the
Coarsening Lemma alone does not finish the proof.")

### Verification on `a_1=2747`, `S=\{41\}` (the mandatory non-freezing
self-check: criterion must correctly NOT apply here)

Every index `j` with `G_j\cap\{41\}=\varnothing` (i.e. `j\in I_{\{67\}}`, the
only other class present) was enumerated for `n\le400` (fresh computation
this round): `j=3,54,103,154,205,254,305,355`, with `\mathrm{comp}(a_j)=
\{2,3,7\}` at every one of these except `j=205` where
`\mathrm{comp}(a_{205})=\{2,3,5,7\}` (a strict *superset* of `\{2,3,7\}`, not
disjoint from it). **No two of these companion sets are disjoint** — every
single one contains the fixed prime set `\{2,3,7\}` as a subset, so any two
share at least `2,3,7`. Hence the Coarsening Lemma's hypothesis (existence of
two witnesses with disjoint companion sets) **genuinely fails** for
`S=\{41\}` on `a_1=2747`, checked exhaustively through `n=400`, not merely
asserted. This correctly identifies why this channel does not freeze via
this mechanism: with only a single "companion shape" (`\{2,3,7\}`, always
containing `7`) ever offered by the other class, any candidate `C=\{41\}\cup
Q` with `7\in Q` automatically survives every witness seen so far regardless
of what else `Q` contains, permitting the observed unbounded-until-absorbed
fan `\{7,q,41\}` for growing companion primes `q\in\{11,13,17,19,23,29,31,
37\}` (verified this round, fresh computation, indices `10,20,40,50,71,101,
112,142$ respectively) before the bare value `\{7,41\}` is finally realized
at `a_{163}=11767=7\cdot41^2` (matching Lemma FOM exactly:
`T_{\{7,41\}}=\min\{7^a41^b>2747:a,b\ge1\}`; checking all such values —
`287,2009,11767,14063,82369,\dots` — the least one exceeding `2747` is
`11767`, confirmed `=a_{163}` exactly), simultaneously dominating and
removing all 9 prior fan elements in a single collapse, leaving the final
3-element antichain `\{\{2,41\},\{3,41\},\{7,41\}\}` (verified: zero further
changes through `n=400`, i.e. `\ge237` further class-`\{41\}` terms past the
collapse with no effect on the antichain).

### Why the Coarsening Lemma alone does not finish the proof (honest
diagnosis of the remaining gap, per the dispatch's explicit instruction not
to overclaim)

The natural next step — argue that once each coarse bucket `\kappa\in
\mathcal K` is resolved (either permanently blocked, or its bare value
`S\cup\kappa` realized), the whole antichain freezes — runs into a genuine
obstruction not present in the `a_1=247` numerics (where it happens not to
bite) but not ruled out in general: **the Bucket-Exclusion Corollary blocks
only the bare value `S\cup\kappa` itself, not proper supersets of it.** If
`S\cup\kappa` is permanently blocked, a term with radical `S\cup\kappa\cup
\{q\}` for some *extra* prime `q` disjoint from the blocking witness's
radical is **not** ruled out by this mechanism alone, and could in principle
recur for infinitely many distinct `q`, growing an unbounded fan *within* a
"blocked" bucket. In the worked `a_1=247` example this does not happen
(verified through `n=15000`: no such superset radical is ever realized,
because any candidate `\{13,5,7,q\}` is dominated the moment it would appear,
since it is automatically a superset of the *already-realized* bucket
`\{2,5,13\}` or `\{3,7,13\}` whenever `q\in\{2,3\}$, and no term with
`q\notin\{2,3\}$ intersecting `\{13,5,7,q\}` against `a_7=\{2,3,19\}` is
possible unless `q\in\{2,3,19\}`, and `19\notin P_1\setminus S`-companion
territory is excluded by imprint — so `q` is forced into `\{2,3\}`, and both
choices land inside an already-dominated bucket). This is a real but
*ad hoc*, example-specific verification, not a general theorem: proving, for
an **arbitrary** proper core `S` satisfying the Coarsening Lemma's
hypothesis, that every candidate escaping bare-value blocking is *always*
eventually dominated by some other bucket's realized minimal value, requires
controlling the full lattice of cross-bucket domination relationships — a
genuinely harder combinatorial question, of the same essential order of
difficulty as the shared open companion-count/chain-count bound attacked
(and not closed) by every sibling approach (`persistent-backbone-
monovariant`'s Growth-Budget Lemma, `imprint-automaton-periodicity`'s
Companion-Count Bound, `core-depth-induction`'s depth-reduction conjecture).
**No mechanism closing this was found this round.** This is the precise,
honest scope of what remains open for this approach.

**On the dispatch's second explicit ask (prove case (b), the non-freezing
/collapsing cores, is still finite in general): NOT achieved this round.**
The `a_1=2747`, `S=\{41\}` example *is* numerically finite (stabilizes at
`n=163`, verified with zero further changes through `n=400`), consistent
with `(MRS_S)` being true there, but no general argument bounding the
collapse count (or the fan size before the eventual bare-value hit) for an
arbitrary non-freezing core was found. This reduces, honestly, to exactly the
same open gap already on record from round 5 (`(MRS_S)` for doubly-infinite
imprint classes) — this round narrows *when* the freeze mechanism applies
(a genuinely new, correct, and useful partial criterion) but does not add
new machinery for the complementary "genuinely absorbs" case beyond what was
already known.

## Round 6 Outline (proof-outliner directive — Permanent-Freeze Dichotomy
for proper cores, a structural/extremal mechanism distinct from counting or
induction)

**Context.** This file already owns the Channel Assembly Theorem + Channel
Splitting Lemma (certified here): global FCBC `\Leftarrow` `(MRS_S)` for
every nonempty `S\subseteq P_1`, with channels touching a finite imprint
class already fully and unconditionally resolved (§D). The remaining gap —
`(MRS_S)` for doubly-infinite proper cores — is the same shared gap the
whole population is attacking. This round's mechanism is a **structural
dichotomy**, not a counting or induction argument: use cross-channel
permanent inadmissibility to show some proper cores *freeze* (their
antichain reaches a small size and NEVER changes again, zero collapse
events) rather than *absorb* — generalizing Lemma TC's mechanism
(`S=P_1\Rightarrow𝓥_{P_1}=\{P_1\}`) down to general proper cores, motivated
by this round's fan-structural explorer's `a_1=247` finding: `S=\{13\}` and
`S=\{19\}` each freeze permanently at exactly 3 elements with zero collapse
events ever, because the "bare" target `T_{\{13\}}=13^3` can never become
admissible once a `\{19\}`-imprint term exists (a permanent, not transient,
obstruction).

**Step 1 (elementary, certify in full — no new machinery needed).**
**Permanent-Inadmissibility Lemma.** If some index `j` has
`\mathrm{rad}(a_j)\cap C=\varnothing$ for a candidate radical `C`, then no
term with radical exactly `C` can appear at any index `>j` (admissibility
against `a_j` fails permanently — the greedy rule's admissibility condition
only ever adds constraints as `n` grows, it never relaxes). *Proof*: one
line from the definition of admissibility (`\gcd(x,a_i)>1$ for all `i\le n`
required at every step `n\ge j`, in particular for `i=j`, which already
fails if `\mathrm{rad}(x)=C$ and `C\cap\mathrm{rad}(a_j)=\varnothing`).

**Step 2 — Freeze Criterion (OPEN, this round's genuine attempted content,
DO NOT claim closed).** For a proper core `S`, let `j_S$ be the first index
(if any) with `\mathrm{rad}(a_{j_S})\cap S=\varnothing` (witnessing some
other channel `S'$, disjoint from `S`, is active). **First prove `j_S`
always exists for `S\ne P_1`** (candidate: since `S\subsetneq P_1`, some
prime `p\in P_1\setminus S` exists; some index must eventually have imprint
not containing `S` fully — needs a short unconditional pigeonhole argument
using Lemma P′, not yet written down; likely easy but not yet done).
**Then attempt**: if `\mathrm{rad}(a_{j_S})\cap C=\varnothing` also holds for
*every* candidate extension `C\supsetneq S` with `T_C$ small enough to
matter (not just `C=T_S$ itself, as in the worked `a_1=247` example), the
Permanent-Inadmissibility Lemma blocks all of them after `j_S`, so `𝓥_S`
only contains values realized *before* `j_S` — automatically finite.
**Explicitly not proved**; the "every candidate extension" clause is the
hard part and is not established even in outline form.

**Mandatory self-check before trusting this mechanism (per this round's
dispatch, run this before writing more of Step 2 as if it worked).**
`a_1=2747`, `S=\{41\}` genuinely absorbs (8 companions before absorbing at
`n=163`) rather than freezing — verify explicitly that the Freeze
Criterion's hypothesis (blocking of every extension) FAILS in this case
(it must, since freezing did not happen numerically); if the builder cannot
show this, the Freeze Criterion as stated is likely wrong, not merely
incomplete, and should be reported as refuted, not left as an open
conjecture.

**Step 3 — Dichotomy conclusion (conditional).** Every proper core `S`
either satisfies the Freeze Criterion (`𝓥_S` finite directly, no absorption
machinery needed) or does not, in which case this approach falls back to
needing the same absorption-count bound left open by the sibling
approaches (`persistent-backbone-monovariant`'s Growth-Budget Lemma,
`imprint-automaton-periodicity`'s Companion-Count Bound, `core-depth-
induction`'s inductive step) — do not re-derive that bound here, just note
the fallback explicitly.

**Honesty warning.** The `a_1=247` example is small (`|P_1|=2`, no
multi-level nesting). This round's other explorer data (fan-structural,
narrow-framing) shows most channels in the harder stress cases (`a_1=2747,
21528751`) genuinely absorb rather than freeze — be prepared for the Freeze
Criterion to apply only to a small, "easy" minority of channels, and report
this honestly rather than overselling the dichotomy's coverage.

## Round 5 update (headline — read this first)

**Dispatch.** (1) Write a full, rigorous proof that global FCBC follows from
independent local stabilization within each of the `≤3^{ω(a_1)}` channels
(the "Channel Assembly Theorem" sketched by the round-5 outline), with zero
cross-channel leakage, naming Lemma FH explicitly. (2) Attempt to actually
close each channel type's local stabilization hypothesis `(LMRS_{S,S'})`.
(3) If not fully closed, be exact and precise about what remains open and
why. (4) Numerically stress-test on `a_1=2747` (multi-hub nested fan) and
`a_1=247` (the historical counterexample to the refuted "extended-imprint-
overlap" mechanism), making sure not to repeat that refuted mechanism.

**What this round establishes, precisely:**

1. **The Channel Assembly Theorem is now fully proved** (§A below): if
   `(LMRS_{S,S'})` holds for *every* channel `{S,S'}` of `P_1` (a finite,
   `a_1`-dependent family, `≤3^{ω(a_1)}` of them), then the explicit finite
   set `H:=P_1∪⋃_{\{S,S'\}}H^{(S,S')}` satisfies FCBC. Every step is proved
   from scratch in this file (local domination, local Lemma MS, and the
   global assembly step using Lemma FH), not merely cited. This is real,
   complete, unconditional (modulo `(LMRS_{S,S'})`) machinery — the outline's
   Steps 1–4 are all discharged in full.
2. **A genuinely new structural lemma, the Channel Splitting Lemma (§B),
   found and proved this round, not in the original outline**: for any
   channel `{S,S'}`, the local minimal-radical antichain `𝓜_n^{(S,S')}`
   splits *exactly*, for every `n`, into a disjoint union `𝓜_n^S⊔𝓜_n^{S'}`
   of two **single-class** antichains (`𝓜_n^S` computed using *only*
   indices with imprint exactly `S`, entirely independent of the channel
   partner `S'`), because cross-side domination is impossible whenever `S,S'`
   are disjoint and nonempty. Consequently `(LMRS_{S,S'})` holds **iff**
   `(MRS_S)` and `(MRS_{S'})` both hold, where `(MRS_S)`: the single-class
   antichain `𝓜_n^S` is eventually constant. This reduces the `≤3^{ω(a_1)}`
   two-sided channel conjectures to at most `2^{ω(a_1)}-1` **one-sided**
   conjectures (one per nonempty `S⊆P_1`, automatic for finite `I_S`) — a
   real further reduction, independently verified numerically (§C) at
   multiple checkpoints on 12 diverse `a_1`, zero mismatches. **This is
   not the refuted "extended-imprint-overlap" mechanism** — that mechanism
   tried to make the *intersection*-stabilization `S^+∩S'^+≠∅` itself the
   covering witness and was refuted on `a_1=247`; the Channel Splitting
   Lemma makes no claim about intersections at all, it is a purely
   structural decomposition of the *antichain* construction, and the
   covering argument still goes through local Lemma MS's pairwise-
   intersecting step (citing the unconditional global Lemma P′), exactly as
   in the already-certified global Lemma MS. Explicitly checked this is a
   different mechanism (§B, Discussion).
3. **Finite imprint classes are resolved by an even stronger, fully
   unconditional argument (§D), superseding Lemma FX2's weaker
   "`F_{S,S'}` finite" conclusion**: if `I_S` is finite, then
   `H_S:=⋃_{i∈I_S}\mathrm{rad}(a_i)` (finite, no antichain/LMRS machinery
   needed at all) already covers **every** pair with one index in `I_S`,
   *regardless of the other index* — not just pairs within one channel.
   Proved in 4 lines from the already-certified Lemma P′. So `(LMRS_{S,S'})`
   is now known **unconditionally** for every channel touching a finite
   imprint class (matches and strengthens Lemma FX2's consequence); only
   channels between **two doubly-infinite** imprint classes need
   `(MRS_S)`/`(MRS_{S'})` for the (necessarily few, `≤2^{ω(a_1)}-1`)
   doubly-infinite classes.
4. **`(MRS_S)` for doubly-infinite classes is NOT closed this round** —
   confirmed, with a new and important numerical finding (§E), to be
   genuinely of the *same difficulty* as global `(MRS)`, not easier: a
   direct stress test on `a_1=21528751` (the round-4 refutation explorer's
   hardest known FCBC case) shows the *global* `𝓜_n` (and, since one class
   there contains `>97%` of all indices, essentially the corresponding
   *local* `𝓜_n^S` too) undergoes a **dramatic single-step collapse from
   1103 antichain elements down to 8** at `n=27831`, only fully settling
   (no further changes observed) at `n=44966` — nearly **500× later** than
   the previously known worst case (`n≤92` across the 12 `a_1` tested in
   round 4). This is *positive* evidence `(MRS)`/`(MRS_S)` can still be true
   in general (no actual counterexample — a *later*, much bigger
   stabilization point was found, not non-stabilization), but it is a
   **negative finding against any proof strategy that bounds the
   stabilization index `N_0` by a small/uniform function of `ω(a_1)`** —
   confirmed by an independent brute-force recomputation (§E) that this is
   not a simulator artifact. This sharpens, rather than weakens, why
   `(MRS_S)` remains open: any correct proof must survive stabilization
   points in the tens of thousands, not dozens.
5. **`a_1=2747` and `a_1=247` stress tests (per the explicit dispatch
   instruction), reported precisely (§C, §E)**: both channels stabilize
   comfortably early (`a_1=247`: position 2 of ~8000/~5000;
   `a_1=2747`: position 154 of ~9600 for the dominant class, position 0 for
   the sparse class) — **no counterexample to `(LMRS_{S,S'})` found on
   either dispatch-specified case**, and the Channel Splitting Lemma's
   exact decomposition identity is confirmed on both, at multiple
   checkpoints, with zero mismatches.

**Conclusion on the dispatch's central question ("can these channel types
now be shown to stabilize?"): NOT in general.** The localized machinery
(Channel Assembly Theorem + Channel Splitting Lemma) is fully proved and is
real, new, reusable progress — it correctly and completely reduces FCBC to
finitely many *single-class* stabilization conjectures `(MRS_S)`, strictly
sharper than the `≤3^{ω(a_1)}` two-sided channels the outline started with,
and it unconditionally disposes of every channel touching a finite imprint
class. But `(MRS_S)` for doubly-infinite classes is not proved, is
numerically confirmed to have the same fan/collapse pathology as the global
`(MRS)` hypothesis (with an even more extreme instance found this round),
and no new mechanism found this round closes it. **Status remains
`partial`** — this is not an overclaim of `solved`.

## §A. The Channel Assembly Theorem — full proof

### Notation (self-contained; matches `lemmas/lemma-FN-FX-FX2-forced-primes-reduction.md` and `lemmas/lemma-FH-uncovered-pair-localization.md`)

`P_1:=\mathrm{rad}(a_1)`, `k:=|P_1|=\omega(a_1)`. For `i\ge1`,
`G_i:=\mathrm{rad}(a_i)\cap P_1` (the `P_1`-imprint of `i`; `G_i\ne\varnothing`
for every `i` by the already-certified **Lemma P**). For nonempty
`S\subseteq P_1`, `I_S:=\{i\ge1:G_i=S\}`; these sets partition `\mathbb N`
(every index has exactly one imprint value) over the (at most `2^k-1`)
nonempty subsets of `P_1`.

A **channel** is an unordered pair `\{S,S'\}` of nonempty, disjoint subsets
of `P_1`. The number of channels is at most `3^k` (a standard bound: each of
the `k` elements of `P_1` is independently assigned to `S`, `S'`, or
neither, giving `\le3^k` ordered pairs, hence at most that many unordered
ones) — this is the same bound used by the already-certified Lemma FX
corollary.

### Local antichain construction (Step 1 of the outline, self-contained)

Fix a channel `\{S,S'\}` and set `J:=I_S\cup I_{S'}`. For `n\ge1`, call
`i\in J\cap[1,n]` **`(n,S,S')`-minimal** if there is no `k\in J\cap[1,n]`
with `\mathrm{rad}(a_k)\subsetneq\mathrm{rad}(a_i)`. Let
`M_n^{(S,S')}\subseteq J\cap[1,n]` be the set of `(n,S,S')`-minimal indices,
and `𝓜_n^{(S,S')}:=\{\mathrm{rad}(a_i):i\in M_n^{(S,S')}\}` (a finite
antichain of finite prime-sets, since `J\cap[1,n]` is finite).

**Hypothesis `(LMRS_{S,S'})`** (open, this is the content flagged below):
there exists `N_0` such that `𝓜_n^{(S,S')}=𝓜_{N_0}^{(S,S')}` for every
`n\ge N_0` (with `n` ranging over all positive integers, not just those in
`J`). Write `𝓜_\infty^{(S,S')}:=𝓜_{N_0}^{(S,S')}` and
`H^{(S,S')}:=\bigcup_{T\in𝓜_\infty^{(S,S')}}T`.

### Step 2 — Local domination (proved in full; verbatim adaptation of Corollary W3′)

**Lemma (Local Corollary W3′).** For every `n\ge1` and every
`i_0\in J\cap[1,n]`, there exists `j^*\in M_n^{(S,S')}` with
`\mathrm{rad}(a_{j^*})\subseteq\mathrm{rad}(a_{i_0})`.

**Proof.** Let `T:=\{k\in J\cap[1,n]:\mathrm{rad}(a_k)\subseteq
\mathrm{rad}(a_{i_0})\}`; `i_0\in T` so `T\ne\varnothing`. Choose `j^*\in T`
minimizing `|\mathrm{rad}(a_{j^*})|`. If `j^*\notin M_n^{(S,S')}`, some
`k\in J\cap[1,n]` has `\mathrm{rad}(a_k)\subsetneq\mathrm{rad}(a_{j^*})
\subseteq\mathrm{rad}(a_{i_0})`, so `k\in T` with
`|\mathrm{rad}(a_k)|<|\mathrm{rad}(a_{j^*})|`, contradicting minimality of
`j^*`. Hence `j^*\in M_n^{(S,S')}`, and `\mathrm{rad}(a_{j^*})\subseteq
\mathrm{rad}(a_{i_0})` by construction. `∎`

This is the identical argument used for the already-certified (global)
Corollary W3′ (`lemmas/lemma-MS-minimal-radical-stabilization-
sufficiency.md`), with the ambient index set `\{1,\dots,n\}` replaced by
`J\cap[1,n]` throughout; the proof uses no property of the ambient set
beyond finiteness, so the substitution is valid verbatim.

### Step 3 — Local Lemma MS (proved in full, conditional on `(LMRS_{S,S'})`)

**Lemma (Local MS).** If `(LMRS_{S,S'})` holds, then `H^{(S,S')}` is finite
and `H^{(S,S')}\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing` for
**every** `i\ne j` in `J` (not merely cross-channel pairs — this includes
pairs with both indices in `I_S`, or both in `I_{S'}`, though those are
already covered trivially by `P_1` alone, see the Remark below).

**Proof.**

*Finiteness.* `𝓜_\infty^{(S,S')}=𝓜_{N_0}^{(S,S')}` is a finite set (it is
literally the value `𝓜_n^{(S,S')}` at the specific index `n=N_0`, and each
`𝓜_n^{(S,S')}` is finite by construction — a subset of the finite set
`\{\mathrm{rad}(a_i):i\in J\cap[1,n]\}`). Each `T\in𝓜_\infty^{(S,S')}` is
itself a finite set of primes (`T=\mathrm{rad}(a_i)` for some actual
integer `a_i>1`). Hence `H^{(S,S')}=\bigcup_{T\in𝓜_\infty^{(S,S')}}T` is a
finite union of finite sets, so finite.

*Step 1 (every index of `J` is dominated by `𝓜_\infty^{(S,S')}`).* Fix
`i\in J`. Let `n:=\max(i,N_0)\ge N_0`, so `𝓜_n^{(S,S')}=𝓜_\infty^{(S,S')}`
by `(LMRS_{S,S'})`. Apply the Local Corollary W3′ with this `n` and
`i_0:=i` (valid since `i\le n`): there is `j^*\in M_n^{(S,S')}` with
`\mathrm{rad}(a_{j^*})\subseteq\mathrm{rad}(a_i)`. Since
`j^*\in M_n^{(S,S')}`, `\mathrm{rad}(a_{j^*})\in𝓜_n^{(S,S')}=
𝓜_\infty^{(S,S')}`. So every `i\in J` has `\mathrm{rad}(a_i)\supseteq S_i`
for some `S_i\in𝓜_\infty^{(S,S')}`.

*Step 2 (`𝓜_\infty^{(S,S')}` is pairwise intersecting).* Every
`T\in𝓜_\infty^{(S,S')}` equals `\mathrm{rad}(a_k)` for some actual index
`k` (of the whole infinite sequence, not just `J` — every element of every
`𝓜_n^{(S,S')}` is, by construction, the radical of some `a_k`). Given
`T=\mathrm{rad}(a_k)`, `T'=\mathrm{rad}(a_{k'})\in𝓜_\infty^{(S,S')}`: if
`T=T'`, `T\cap T'=T\ne\varnothing` (radicals of integers `>1` are
nonempty). If `T\ne T'` then `k\ne k'`, and the already-certified **Lemma
P′** (pairwise global intersection — holds for *every* pair of indices of
the *whole* infinite sequence, not just pairs within `J`) gives
`\gcd(a_k,a_{k'})>1`, i.e. `T\cap T'\ne\varnothing`.

*Step 3 (`H^{(S,S')}` covers every pair in `J`).* Fix `i\ne j` in `J`. By
Step 1, `\mathrm{rad}(a_i)\supseteq S_i`, `\mathrm{rad}(a_j)\supseteq S_j`
for some `S_i,S_j\in𝓜_\infty^{(S,S')}`. By Step 2, `S_i\cap S_j\ne
\varnothing`; pick `p\in S_i\cap S_j`. Then `p\in S_i\subseteq H^{(S,S')}`,
`p\in S_i\subseteq\mathrm{rad}(a_i)`, `p\in S_j\subseteq\mathrm{rad}(a_j)`,
so `p\in H^{(S,S')}\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)`. As `i\ne j`
in `J` were arbitrary, done. `∎`

**Remark.** This proof covers *every* pair in `J`, including
same-side pairs (`i,j\in I_S`), not only cross-channel pairs
(`i\in I_S,j\in I_{S'}`) — a strictly stronger conclusion than the outline's
Step 3 literally asked for, obtained for free from the identical argument.
(Same-side pairs are, in any case, already covered unconditionally by
`P_1\subseteq H` since `G_i=G_j=S\ne\varnothing` there, so this extra
strength is not needed for the assembly below, but it is recorded since it
falls out of the proof at no extra cost.)

### Step 4 — Assembly (proved in full: global FCBC from local stabilization, citing Lemma FH)

**Theorem (Channel Assembly Theorem).** Suppose `(LMRS_{S,S'})` holds for
*every* channel `\{S,S'\}` of `P_1` (a finite family, `\le3^k` of them, `k`
fixed since `a_1` is one fixed integer). Then
$$H:=P_1\cup\bigcup_{\{S,S'\}\text{ a channel}}H^{(S,S')}$$
is a finite set satisfying FCBC: `H\cap\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)\ne\varnothing` for **every** `1\le i<j` of the whole
infinite sequence.

**Proof.**

*Finiteness of `H`.* `P_1` is finite (`a_1` is one fixed integer). By Local
Lemma MS, each `H^{(S,S')}` is finite, and there are at most `3^k` channels
(a fixed finite number depending only on `a_1`). A finite union of finite
sets is finite, so `H` is finite.

*Coverage (this is the "zero cross-channel leakage" content).* Fix `i<j`
arbitrary. Suppose, for contradiction, `H\cap\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)=\varnothing`. Since `P_1\subseteq H`, the already-proved
**Lemma FH** (uncovered-pair localization,
`lemmas/lemma-FH-uncovered-pair-localization.md`) applies directly: `H`
failing to cover `(i,j)` forces `G_i\cap G_j=\varnothing`. Since `G_i,G_j`
are both nonempty (Lemma P) and disjoint subsets of `P_1`, the unordered
pair `\{G_i,G_j\}` is, *by definition*, one of the (at most `3^k`) channels
of `P_1` — call it `\{S,S'\}` with (without loss of generality) `S:=G_i`,
`S':=G_j`. Then `i\in I_{G_i}=I_S\subseteq J:=I_S\cup I_{S'}` and
`j\in I_{G_j}=I_{S'}\subseteq J`, so `i,j\in J` with `i\ne j`. By
hypothesis, `(LMRS_{S,S'})` holds for this specific channel, so Local
Lemma MS applies and gives `H^{(S,S')}\cap\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)\ne\varnothing`. But `H^{(S,S')}\subseteq H` by
construction, so `H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\supseteq
H^{(S,S')}\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing`,
contradicting the assumption. Hence `H\cap\mathrm{rad}(a_i)\cap
\mathrm{rad}(a_j)\ne\varnothing`. As `i<j` were arbitrary, `H` satisfies
FCBC. `∎`

**Why there is zero cross-channel leakage (explicit discussion, as
requested).** Two distinct features of the argument together rule out any
interaction between channels: (i) *Uniqueness of routing* — a pair `(i,j)`
that could possibly be uncovered has its imprints `G_i,G_j` **exactly**
determined by `i,j` themselves (not a choice), so it is assigned to exactly
one channel, `\{G_i,G_j\}`, with no ambiguity and no pair ever needing
contributions from two different channels simultaneously. (ii)
*Non-interference of the local constructions* — the Step 1–3 machinery for
channel `\{S,S'\}` only ever references indices in `J=I_S\cup I_{S'}` and
the *unconditionally already-proved* global Lemma P′; it never uses any
fact about, or result from, any other channel's local antichain. So
proving/assuming `(LMRS_{S,S'})` for one channel neither requires nor
supplies any information relevant to a different channel `\{T,T'\}` — the
`\le3^k` hypotheses are logically independent, and the assembly step
(Step 4) is a pure union with a routing argument, not a synthesis that
could accidentally double-count or drop a pair. This closes the dispatch's
"zero cross-channel leakage" requirement rigorously, not just by assertion.

**Corollary (finish, conditional on all local hypotheses).** If
`(LMRS_{S,S'})` holds for every channel, then by the Channel Assembly
Theorem `H` satisfies FCBC, so the already-certified **Theorem 5.1**
(`lemmas/theorem-5.1-master-conditional-theorem.md`) gives
`a_{n+T}=a_n+L` for **every** `n\ge1` (`T=|\mathrm{Good}|`,
`L=\mathrm{lcm}(H)`) — the problem's exact headline conclusion. This
Theorem is honestly still conditional: see §B–§E for exactly how far the
antecedent is established.

## §B. The Channel Splitting Lemma (new this round)

**Statement.** Fix a channel `\{S,S'\}` (`S,S'` nonempty, disjoint,
`\subseteq P_1`). For nonempty `S\subseteq P_1`, define the **single-class**
local antichain `M_n^S:=\{i\in I_S\cap[1,n]:\text{no }k\in I_S\cap[1,n]
\text{ has }\mathrm{rad}(a_k)\subsetneq\mathrm{rad}(a_i)\}` and
`𝓜_n^S:=\{\mathrm{rad}(a_i):i\in M_n^S\}` — the ordinary minimal-radical
antichain construction applied to the subsequence `(a_i)_{i\in I_S}` alone.
Then for **every** `n\ge1`:
$$𝓜_n^{(S,S')}=𝓜_n^S\ \sqcup\ 𝓜_n^{S'}\qquad(\text{disjoint union}).$$
Consequently, `(LMRS_{S,S'})` holds **iff** `𝓜_n^S` is eventually constant
AND `𝓜_n^{S'}` is eventually constant. Write `(MRS_S)` for "`𝓜_n^S` is
eventually constant."

**Proof.**

*Every element of `𝓜_n^{(S,S')}` lies on exactly one side.* If
`T\in𝓜_n^{(S,S')}`, `T=\mathrm{rad}(a_i)` for some `i\in M_n^{(S,S')}
\subseteq J\cap[1,n]=(I_S\cup I_{S'})\cap[1,n]`. Since `I_S,I_{S'}` are
disjoint (they are imprint classes for the distinct values `S\ne S'`),
exactly one of `i\in I_S`, `i\in I_{S'}` holds. If `i\in I_S`, then
`T\cap P_1=\mathrm{rad}(a_i)\cap P_1=G_i=S` (by definition of `I_S`); if
`i\in I_{S'}`, `T\cap P_1=S'`. So every `T\in𝓜_n^{(S,S')}` satisfies
`T\cap P_1\in\{S,S'\}`, giving a well-defined partition
`𝓜_n^{(S,S')}=𝓐_n\sqcup𝓑_n` with `𝓐_n:=\{T:T\cap P_1=S\}`,
`𝓑_n:=\{T:T\cap P_1=S'\}` (disjoint since `S\ne S'`, so no `T` can satisfy
both).

*No cross-side domination.* Suppose `i\in I_S`, `k\in I_{S'}`, and
`\mathrm{rad}(a_k)\subseteq\mathrm{rad}(a_i)` (as sets). Intersecting both
sides with `P_1`: `\mathrm{rad}(a_k)\cap P_1\subseteq\mathrm{rad}(a_i)\cap
P_1`, i.e. `S'\subseteq S`. Since `S,S'` are disjoint, `S'\subseteq S`
forces `S'\subseteq S\cap S'=\varnothing`, contradicting `S'\ne\varnothing`.
By the symmetric argument (swap `S,S'`), no `i\in I_{S'}` can have its
radical contained in the radical of some `k\in I_S` either. So domination
(`\mathrm{rad}(a_k)\subsetneq\mathrm{rad}(a_i)`, a special case of
`\subseteq`) between an element of `I_S` and an element of `I_{S'}` never
occurs in either direction.

*Consequence.* For `i\in I_S\cap[1,n]`: `i\in M_n^{(S,S')}` (survives
domination against all of `J\cap[1,n]`) iff no `k\in J\cap[1,n]` dominates
it; by the previous paragraph, only `k\in I_S\cap[1,n]` can possibly
dominate `i` (domination from `I_{S'}` is impossible), so this is
equivalent to: no `k\in I_S\cap[1,n]` dominates `i`, i.e. `i\in M_n^S`.
Hence `M_n^{(S,S')}\cap I_S=M_n^S`, so `𝓐_n=𝓜_n^S`; symmetrically
`𝓑_n=𝓜_n^{S'}`. This proves `𝓜_n^{(S,S')}=𝓜_n^S\sqcup𝓜_n^{S'}` for every
`n`. `∎`

**Equivalence of eventual constancy.** If `𝓜_n^{(S,S')}` is eventually
constant (say `=V` for `n\ge N_0`), then since `𝓜_n^S=\{T\in𝓜_n^{(S,S')}:
T\cap P_1=S\}` is recoverable from `𝓜_n^{(S,S')}` alone (a fixed,
`n`-independent rule), `𝓜_n^S=\{T\in V:T\cap P_1=S\}` is also constant for
`n\ge N_0`; symmetrically for `𝓜_n^{S'}`. Conversely if `𝓜_n^S=A` for
`n\ge N_1` and `𝓜_n^{S'}=B` for `n\ge N_2`, then `𝓜_n^{(S,S')}=A\sqcup B`
for `n\ge\max(N_1,N_2)`, constant. `∎`

**Discussion — why this is not the refuted "extended-imprint-overlap"
mechanism.** The refuted mechanism (`lemmas/lemma-C-generalized-
subsequence.md`, round 3) conjectured that the *intersection*-stabilization
`S^+:=\bigcap_{i\in I_S}\mathrm{rad}(a_i)` (extended imprint) satisfies
`S^+\cap S'^+\ne\varnothing` for every doubly-infinite channel, and tried to
use *that intersection itself* as the covering witness — refuted directly
on `a_1=247` (`S^+=\{13\}`, `S'^+=\{19\}`, disjoint, yet the channel is
forced-finite anyway by some other mechanism). The Channel Splitting Lemma
makes **no claim about any intersection of all of `I_S`'s radicals** — it
is a purely combinatorial fact about how the *antichain* (minimal-element)
construction behaves under a disjointness hypothesis on `S,S'`, and the
actual covering argument (Local Lemma MS, §A Step 3) still goes through
**pairwise intersection of individual antichain elements** via the
unconditional global Lemma P′ — structurally the same mechanism as the
already-certified global Lemma MS, not the refuted one. Re-verified this
distinction explicitly by checking the `a_1=247` case directly (§E below):
the Channel Splitting decomposition is confirmed to hold exactly here (not
vacuously — both `𝓜_n^{\{13\}}` and `𝓜_n^{\{19\}}` are nontrivial,
3-element antichains), while the extended-imprint-overlap mechanism it
supersedes remains refuted and is not resurrected.

**Reduction summary.** Combining the Channel Splitting Lemma with the
Channel Assembly Theorem (§A): if `(MRS_S)` holds for **every** nonempty
`S\subseteq P_1`, then `(LMRS_{S,S'})` holds for every channel `\{S,S'\}`
(apply the equivalence to both sides), so `H` (as constructed in §A) is a
finite covering set and FCBC holds. This replaces the `\le3^k` two-sided
channel conjectures with at most `2^k-1` **one-sided** conjectures — a real
reduction (roughly a square-root-order shrinkage in the family size, and,
more importantly, each `(MRS_S)` is a conceptually simpler object: the
ordinary minimal-radical antichain of a single homogeneous-imprint
subsequence, with no cross-class bookkeeping at all).

## §C. Numerical confirmation of the Channel Splitting identity

Independently implemented both the joint local antichain
`𝓜_n^{(S,S')}` and the two single-class antichains `𝓜_n^S,𝓜_n^{S'}`
(three separate incremental computations, no shared state), and checked
the identity `𝓜_n^{(S,S')}=𝓜_n^S\sqcup𝓜_n^{S'}` at **multiple checkpoints**
`n\in\{50,100,200,500,1000,2000,3000,4000\}` (not just the final `n`), for
every channel with `|J|\ge20`, across **12 diverse `a_1`**:
`221, 375, 247, 4087, 4199, 2747, 65, 105, 143, 15, 17017, 10403`.

**Result: zero mismatches across every channel, every checkpoint, every
`a_1` tested** (code: `/tmp/round-5/splitting_test.py`). This is strong
computational confirmation that the proof in §B is implemented and stated
correctly (the deductive proof already establishes the identity
unconditionally; this is a correctness check on the implementation and a
sanity check per project convention, not itself a proof step).

## §D. Finite imprint classes: unconditional, LMRS-free resolution (strengthens Lemma FX2)

**Lemma (Finite-class direct covering).** If `I_S` is finite (`S` nonempty,
`\subseteq P_1`), then `H_S:=\bigcup_{i\in I_S}\mathrm{rad}(a_i)` is finite
and satisfies `H_S\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing`
for **every** `i\in I_S` and **every** `j\ne i` of the whole infinite
sequence (not merely `j` in some fixed channel partner class).

**Proof.** `H_S` is a finite union (`I_S` finite) of finite sets
(`\mathrm{rad}(a_i)`, `a_i` a fixed integer for each `i`), hence finite. Fix
`i\in I_S`, `j\ne i` arbitrary. By construction `\mathrm{rad}(a_i)\subseteq
H_S`. By the already-certified **Lemma P′**, `\gcd(a_i,a_j)>1`, i.e.
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing`. Since
`\mathrm{rad}(a_i)\subseteq H_S`, any element of
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)` also lies in
`H_S\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)`, so this set is nonempty.
`∎`

**Consequence.** For every channel `\{S,S'\}` with `I_S` finite (whichever
side), `(LMRS_{S,S'})` holds **automatically and unconditionally** — indeed
more is true, `H_S` alone (not even needing the partner side) covers every
pair touching `I_S`, so no antichain/local-MS machinery is needed for such
channels at all. This is a genuine strengthening of the already-certified
**Lemma FX2** (`lemmas/lemma-FN-FX-FX2-forced-primes-reduction.md`), which
only established finiteness of the *forced-primes* set `F_{S,S'}`, not a
full covering-set sufficiency statement. Combined with the (at least one,
possibly several, but always `\le2^k-1`) doubly-infinite imprint classes
that must exist (the finitely many `I_S` partition the infinite set
`\mathbb N`, so by pigeonhole at least one is infinite), **the only channels
whose `(LMRS_{S,S'})` is not already unconditionally known are those
between two doubly-infinite imprint classes** — matching and sharpening the
consequence already drawn in round 3's Lemma FX2, now upgraded from "the
open content is finiteness of `F_{S,S'}`" to the cleaner "the open content
is `(MRS_S)` and `(MRS_{S'})` for the doubly-infinite classes involved."

## §E. Stress tests on the dispatch-specified cases, and the new `a_1=21528751` finding

All code in `/tmp/round-5/` (`sim.py`, `channel_test.py`, `splitting_test.py`,
`mrs_s_test.py`, plus inline scripts). Sequence generation independently
validated: for `a_1=21528751`, exhaustively re-checked the first 30 terms
against *both* the admissibility condition (`\gcd(a_n,a_i)>1` for all
`i<n`) *and* minimality (every candidate strictly between `a_{n-1}` and
`a_n` fails admissibility) by brute force over the whole gap — all 30 terms
pass (script output reproduced: "All minimality + validity checks passed
for first 30 terms").

### `a_1=247` (`P_1=\{13,19\}`, historical counterexample to extended-imprint-overlap)

Only one channel, `\{\{13\},\{19\}\}` (`k=2`). At `N=15000`
(`|I_{13}|=8072`, `|I_{19}|=5183`): single-class antichains
`𝓜_n^{\{13\}}` stabilizes at position `2` (final: `\{2,13,5\},\{2,3,13\},
\{3,13,7\}`, 3 elements) and `𝓜_n^{\{19\}}` stabilizes at position `2`
(final: `\{2,19,7\},\{19,2,3\},\{19,3,5\}`, 3 elements) — both extremely
early, no counterexample to `(MRS_{\{13\}})` or `(MRS_{\{19\}})`. The joint
local antichain `𝓜_n^{(\{13\},\{19\})}` correspondingly stabilizes (checked
at `N=15000`, `|J|=13255`) with **zero further changes** after this point,
confirming `(LMRS_{\{13\},\{19\}})` holds up to the tested range. This
directly re-tests the exact case that broke the earlier refuted mechanism,
with the new mechanism (Channel Splitting + Local Lemma MS) — no failure
found.

### `a_1=2747` (`P_1=\{41,67\}`, multi-hub nested fan, non-hidden-Case-I, per dispatch)

Only one channel, `\{\{41\},\{67\}\}`. At `N=10000`: `I_{41}` has `9601`
elements (dominant), `I_{67}` has `195` (sparse but **confirmed genuinely
infinite**, not a finite class — growing from `157` at `N=8000` to `195` at
`N=10000`, roughly periodically, e.g. occurring at indices
`2,53,102,153,204,\dots`; this is a genuine doubly-infinite channel, not one
automatically resolved by §D). The joint local antichain exhibits a visible
"fan" structure before settling: many minimal radicals of the shape
`\{41,7,p\}` for growing primes `p` (a nested fan, matching the "multi-hub
nested fan" label), then a collapse at position `158` (of `9601`) down to a
final 4-element antichain `\{41,2\},\{41,3\},\{41,7\},\{67,2,3,7\}`
(`H^{(\{41\},\{67\})}=\{2,3,7,41,67\}`), confirmed **stable with zero
further changes through `N=10000`** (`|J|=9796`). Splitting-Lemma check:
single-class `𝓜_n^{\{41\}}` stabilizes at position `154` to
`\{41,2\},\{41,3\},\{41,7\}`; single-class `𝓜_n^{\{67\}}` stabilizes at
position `0` to `\{67,2,3,7\}` — union matches the joint result exactly.
No counterexample to `(LMRS_{\{41\},\{67\}})` found.

### `a_1=21528751` (`P_1=\{103,197,1061\}`, the round-4 refutation explorer's hardest known FCBC case) — new finding, not in the original dispatch but investigated because the class `I_{\{103\}}` is `>97\%` of all indices, a severe stress case worth reporting

At `N=25000`, class `S=\{103\}` has `24417` of `25000` indices (near-
saturating but genuinely not all — `S\ne P_1`, other classes are nonempty
and infinite too, so this is Case II, not Case I). The single-class
antichain `𝓜_n^{\{103\}}` was found to be **still changing at the very last
tested index at `N=25000`** (antichain size grown to `1001`, up from `1`),
a red flag prompting a deeper investigation. Extending to `N=50000`
(re-run, ~150s for sequence generation, ~3s for the antichain scan)
revealed the full picture:

- A long "fan" phase: the antichain grows roughly linearly from a handful
  of elements up to **1103 elements** by `n=27821`, structurally many
  minimal radicals of the shape `\{103,7,p\}` for hundreds of distinct
  large primes `p` (visually confirmed in the raw output, e.g.
  `\{32497,103,7\},\{30181,103,7\},\dots`) — a much larger instance of the
  same "nested fan" phenomenon seen (at far smaller scale) in `a_1=2747`
  above.
- A **single, dramatic collapse event** at `n=27831`: the antichain drops
  from `1103` elements to **`8`** in one step — a new term with radical
  containing `\{103,7\}` (a strict subset of every fan element
  `\{103,7,p\}`) appears and simultaneously dominates the *entire* fan.
  This is the same qualitative phenomenon as the already-documented
  `a_1=4087` global-MRS collapse (`17\to3` at `n=54`), but roughly `65\times`
  larger in magnitude (`1103\to8` vs `17\to3`) and at an index roughly
  `500\times` later (`n\approx27800` vs `n=54`).
- One further minor change (`8\to9` elements) at `n=29214`, then a single
  **lateral swap** (same size, `9`, one element replaced by another) at
  `n=44966` — the last change observed anywhere in the range
  `n\in[1,50000]`. **No further changes from `n=44967` through `n=50000`**
  (confirmed by an exhaustive scan of the whole antichain-history, not a
  sample).
- **Independent verification the `1012`-element antichain at `n=25000` is
  correct, not a bug**: recomputed it via a completely different,
  brute-force `O(|\text{distinct radicals}|^2)` pairwise-inclusion scan
  over the `24137` distinct radical values among the first `25000` terms
  (not the incremental algorithm) — **exact match, `1012` minimal
  elements**, confirming the incremental algorithm (and hence the collapse
  finding above, which reuses the same algorithm) is not a simulator
  artifact.

**Interpretation.** This is **not** a counterexample to `(MRS)` or
`(MRS_S)` — the sequence does eventually stabilize (`N_0\approx44966`), so
this data point is *consistent with* `(MRS_S)`/`(MRS)` being true in
general. But it is important negative information for *how* any future
proof of `(MRS_S)` must work: the worst-case stabilization index found
across the whole project to date jumps from `n\le92` (round 4's 12 tested
`a_1`) to `n\approx44966` for this single case — a `\sim500\times` increase
— and the mechanism (a fan of `>1000` elements collapsing in one step) is
exactly the "Bounded Core Family" difficulty this round's outline-reviewer
flagged as the genuinely open content of the sibling `imprint-automaton-
periodicity` approach's Step 3. **Since the local class `S=\{103\}`
contains `>97\%` of all indices here, the local and global antichain
problems are nearly the same object in this case** — this is additional,
independent evidence (not previously reported by any approach) that
localization does not, by itself, make the hard case easier: the identical
fan/collapse pathology appears whether one asks the question globally or
locally, exactly as this round's outline honestly flagged as a possibility
("Honesty check: why this is not obviously easier").

## Approaches tried

- **Round 3 (new approach, copy-branch of `persistent-backbone-monovariant`
  targeting FCBC via a well-ordering/structural-reduction technique).**
  Proved Lemma FN, Lemma FX (+ channel corollary), Lemma FX2, a Generalized
  Lemma C, a conditional Markov density bound. Two closing mechanisms
  (extended-imprint overlap; conditional Domination-Lemma Markov bound)
  tried and found insufficient. Verdict: genuine reduction, `partial`.
- **Round 4 — density/patch bridge investigation.** Verified the
  `H_\rho=F` identity numerically on 9 cases; proved Lemma FH
  (uncovered-pair localization, unconditional); ran the most exhaustive
  sufficiency stress test on `H=F\cup P_1` to date (~181M pair-checks, zero
  failures); precisely separated "sufficiency" into Lemma FF (finiteness)
  and the new Lemma FS (forced-sufficiency), neither proved.
- **Round 5 (this round) — channel-localized `(LMRS)`/Channel Assembly.**
  Fully proved the Channel Assembly Theorem (§A: local stabilization in
  every channel `\Rightarrow` global FCBC, citing Lemma FH for the
  cross-channel routing, zero leakage). Discovered and proved the new
  Channel Splitting Lemma (§B: two-sided channel stabilization reduces to
  two independent one-sided single-class stabilization conjectures,
  `(MRS_S)`) — genuinely new content beyond the outline, not the refuted
  extended-imprint-overlap mechanism (explicitly checked, §B Discussion).
  Proved finite imprint classes need no LMRS machinery at all (§D,
  strengthens Lemma FX2). Stress-tested `a_1=2747` and `a_1=247` per
  dispatch (§E): no counterexample on either. Found and diagnosed a new,
  much harder stabilization instance on `a_1=21528751` (§E): `(MRS)`/
  `(MRS_S)` still holds there but only stabilizes at `n\approx44966`
  (`\sim500\times` later than any previously known case), independently
  confirmed by brute force. **`(MRS_S)` for doubly-infinite classes was NOT
  closed this round** — confirmed to be the same fundamental difficulty as
  global `(MRS)`, now with sharper evidence of how bad the worst case can
  be. Status remains `partial`, honestly. **(Correction, recorded by the
  round-5 proof-reviewer and in `current.md`: §E's `a_1=21528751`
  "single-class local `\{103\}`" numbers `1103\to8` etc. actually match the
  plain global antichain, not the properly `I_S`-restricted local one; the
  correctly-restricted local antichain collapses more simply, `1092\to3`
  directly, with no further changes through `n=30000` — see
  `lemmas/channel-splitting-lemma.md`'s Caution section. This does not
  affect any certified lemma, only the interpretive claim in §E; not
  recomputed this round due to time, flagged here for the next round.)**
- **Round 6 (this round) — corrected Freeze Criterion via the
  Companion-Disjointness Coarsening Lemma.** The outline's literal Step 2
  (single witness `j_S` blocks every extension of `S`) was found FALSE by
  direct hand computation on its own motivating example (§F) — refuted, not
  merely incomplete. Replaced it with a new, fully proved, unconditional
  **Companion-Disjointness Coarsening Lemma** (§F): two witnesses with
  disjoint companion prime-sets force every realized radical of class `S`
  into one of finitely many "coarse buckets." Verified in complete detail on
  both mandatory examples: correctly explains the `a_1=247` freeze (4 coarse
  buckets, 3 realized, 1 permanently blocked via a third witness, matching
  the independently-confirmed 3-element final antichain exactly) and
  correctly predicts the `a_1=2747`, `S=\{41\}` non-freeze (no two
  disjoint-companion witnesses exist, checked exhaustively through `n=400` —
  every witness's companion set contains `\{2,3,7\}`). **Honestly diagnosed,
  not closed:** going from "finitely many coarse buckets" to a full freeze/
  finiteness proof requires controlling cross-bucket domination (blocking a
  bucket's bare value does not block its proper supersets, which can only be
  ruled out by domination from a *different*, already-realized bucket — not
  established in general). The dispatch's second ask (prove the non-freezing
  case is finite in general) was **not achieved** — same open gap as every
  sibling approach. Status remains `partial`, honestly.
- **Round 7 (this round) — Escape-Confinement Lemma + escape-recursion
  depth investigation.** Proved the **Escape-Confinement Lemma** (§G, Step
  1): an escape from a blocked bucket must contain a prime from the
  blocking witness's own fixed companion set. Investigated (§G, Steps 2–4)
  whether the resulting escape-recursion has uniformly bounded depth — the
  round's real target, a genuinely different well-founded structure from
  the now-foreclosed bundle-size/`|S|`-induction families. **Result:
  honestly not achieved.** Real (data-grounded) depth is `\le2` in all 13
  fresh instances checked (2 cores × 2 hard `a_1`, plus 6 more cores of 6
  more `a_1`); a precise Recruiter-Alignment pattern was found and verified
  exactly on every instance but depends on Hypothesis (GW), independently
  refuted this round (in its global form, for nested cores) by the
  outline-reviewer; and the naive full-branching formalization of the
  recursion was shown, concretely, not to terminate within depth 6 on the
  hardest tested case — a genuine obstruction. Diagnosed that the actual
  small depth observed is explained by cross-bucket domination (§F's
  already-open gap), not by anything internal to the escape-recursion
  itself — so this mechanism, while structurally distinct from size
  induction as the outline hoped, does not turn out to be an independent
  route around the shared gap. Status remains `partial`, honestly.
- **Round 8 (this round) — Freeze-Confinement Domination Lemma, depth-bound
  correction, `S^+`/`S^{++}` mechanism.** Fully proved the **Freeze-
  Confinement Domination Lemma** (§H Step 1): unconditional, given
  `(MRS_S)`, every realized class-`S` radical (not just late ones) contains
  some frozen minimal-antichain element — retires round 7's independent
  depth-hunting for good. Found and reported an honest **correction** to the
  round-8 outline's own claimed numeric depth-bound corollary (§H Step 2):
  domination gives a lower, not upper, bound on escape depth; the literal
  claim does not follow and is not certified. Replaced it with a sharper,
  numerically PERFECT (zero exceptions on 9 data points, both hardest known
  cores) but explicitly unproved **Singleton Recruiter Identity** conjecture
  (§H Step 3), which explains round 7's Recruiter-Alignment pattern rather
  than merely restating it. Certified the **`S^+` Necessity + Finiteness
  Lemma** (§H Step 4, one-line application of the already-certified
  Generalized Lemma C to `I_S`). Tested the outline's `S^{++}` sufficiency
  fix directly against its own motivating counterexample
  (`a_1=21528751,S=\{1061\}`) and found it **fails**, proving two new general
  facts explaining why (the **Vacuity Proposition** and the
  **Intersection-Fragility Proposition**, §H Step 5) — a genuine, structural
  negative result, not an unfinished search. Status remains `partial`,
  honestly; the sufficiency gap for proper cores is unchanged in substance
  but now has one more confirmed-insufficient mechanism (and the general
  reason why the whole *family* of intersection-based mechanisms cannot
  work) on record.
- **Round 10 (this round) — Greedy Augmentation / Termination-Sufficiency
  scheme, targeting the Stabilization Conjecture directly (Theorem SW's
  narrowed target, superseding the old `(MRS_S)` framing).** Fully proved
  two new lemmas (§I, Steps 1–2) converting the outline's informal
  well-ordering sketch into a rigorous conditional theorem: the greedy
  process of repeatedly forcing a new common prime on the `\max(i,j)`-
  minimal uncovered cross pair is well-defined and only ever adjoins fresh
  primes outside `P_1` (Greedy Augmentation Lemma), and *if* the adjoined
  primes are ever confined to a fixed finite set `K_0`, the process halts
  and the Stabilization Conjecture follows (Termination-Sufficiency
  Lemma, a clean pigeonhole argument). Tested the outline's own proposed
  candidate `K_0=S^+_S\cup S^+_{S'}` with a fresh, independent, exhaustive
  computation (own script, not reused) on the workspace's hardest known
  instance and found it **refuted**: `S^+_{\{1061\}}\setminus P_1=\{2,3,7\}`
  and `S^+_{\{103,197\}}\setminus P_1=\varnothing` are both already inside
  `B_0`, so the candidate adds nothing, while `B_0` alone provably fails to
  cover (`94` violating cross pairs at `N=3{,}000{,}000`, matching and
  independently reproducing the bridge-primes explorer's figure). Proposed
  and verified (on the same instance, `K=5`, exhaustive over all
  `13{,}181{,}000` cross pairs) a sharper replacement, the First-`K`-Prefix
  Recruitment Conjecture — a union, not intersection, over a bounded
  prefix of each side — and honestly identified the precise reason it is
  not proved (Lemma P′ gives existence, not magnitude/provenance, of the
  forced common prime; sharpening it is "Opening B," not achieved this
  round or in 10 prior rounds of closely related attempts). Status remains
  `partial`, honestly — real new rigor and one decisive negative finding,
  no closure.
- **Round 11 (this round) — Local No-Resurrection/Interval/Equivalence
  Lemmas, the Subset Lemma, and the No-Shortcut Corollary (§J), scoped
  strictly to `(MRS_S)` for the two cores of the pair
  `(\{1061\},\{103,197\})`, per the dispatch's mandated scoping.** Adapted
  the certified GLOBAL Theorem V machinery (No-Resurrection + Interval
  Lemma) to the class-`S`-restricted competitor pool `I_S`, giving a new,
  fully proved **Local Equivalence Theorem**: `(MRS_S)\iff\mathcal
  V_S^{\mathrm{loc}}` finite (§J Steps 1–3). Proved, for the first time
  (previously only checked numerically by the round-11 outline-reviewer),
  the **Subset Lemma** `\mathcal V_S\subseteq\mathcal V_S^{\mathrm{loc}}`
  (§J Step 4). Composed these with the already-certified `\Lambda_S`-
  Reduction Lemma and Multi-Companion Reduction Proposition to prove the
  **No-Shortcut Corollary** (§J Step 5): for the concrete in-scope core
  `S=\{103,197\}`, which the already-certified Permanent Bundle Lemma shows
  realizes a genuine size-`2` multi-companion bundle `\{11,97\}`, closing
  `(MRS_S)` would necessarily resolve exactly the already-flagged
  equi-hard-to-FCBC hitting-set target — a rigorous, not merely numeric,
  confirmation of the residual risk the round-11 outline-reviewer flagged.
  Also gave an explicit combinatorial construction (§J Step 6) proving the
  outline's named toolkit (Lemma FOM, No-Resurrection, Generation-Chain)
  structurally cannot bound antichain WIDTH (only chain length/first-
  occurrence identity), pinpointing exactly why "No-Perpetual-Churn" is not
  reachable by this toolkit alone. **No approach closes `(MRS_S)` this
  round — Status stays `partial`, honestly**, with two new lemmas proposed
  for certification and one precise, proof-backed negative finding, per the
  dispatch's explicit request to report such a finding rather than force a
  fit.
- **Round 12 (this round) — pivoted to the Backbone Permanence/Lemma UCR
  mechanism for "Case B" pairs (a second, independent route alongside
  `sunflower-bundle-closure`'s), per the outline-reviewer's scope
  correction restricting the live target to `a_1=4199`'s pair
  `(\{13\},\{17\})`'s `\{13\}`-side only (`247:(13,19)` confirmed, by fresh
  independent computation, to have no nonempty backbone on either side —
  structurally vacuous for this mechanism, ceded to `sunflower-bundle-
  closure`).** Proved a new general-purpose **Sandwich Uniqueness Lemma**
  (§K, Step 1): the Realized-Backbone/UCR mechanism, for either anchor
  choice, forces the covering set `W` to equal exactly the anchor class's
  full companion intersection — no freedom to use a smaller or different
  realized set. Applied this to BOTH possible anchors for `4199:(13,17)`:
  the `\{17\}`-anchor fails outright (`B_{\mathrm{full}}(\{17\})=
  \varnothing`, proved from two concrete disjoint companion sets, §K Step
  2); the `\{13\}`-anchor fails via an exhaustive, hypothesis-free
  two-case dichotomy (§K Step 3) — whether or not Backbone Permanence
  holds on this side, the mechanism fails, because in the "permanence
  holds" case the required exact realization `\mathrm{rad}(a_m)=\{2,13\}`
  is proved impossible at ANY index (via the already-certified Lemma
  ERD-C, witness `a_5=4233`), and in the "permanence fails" case the
  backbone collapses to `\varnothing`, again failing the mechanism's
  nonemptiness requirement. **Outcome: a complete, gap-free proof (not a
  numeric hunch, and not a stall) that this approach's headline mechanism
  cannot close Conjecture (JW) for `4199:(13,17)`** — an honest negative
  finding exactly as the dispatch requested when the constructive route
  does not materialize. Does not affect any previously certified content
  (Lemma UCR, Corollary UCR-JW, the Local No-Resurrection/Interval/
  Equivalence Theorem, the Subset Lemma, the No-Shortcut Corollary) or
  `sunflower-inadmissibility-toolkit`'s disjoint Case A target. Status
  remains `partial`.
- **Round 13 (this round) — Finite Low-Index Witness-Chaining: Conjecture
  (JW) fully proved for both mandatory Case B pairs (§L).** Formalized the
  round-13 case-b explorer's scouted mechanism into a complete, gap-free
  proof, generalizing its two-fold "singleton special case / general
  disjunction case" split into one uniform **Lemma WF** (Witness Forcing,
  §L.1): a fixed low-index witness with core disjoint from a target class
  forces a disjunctive (or, for a singleton companion set, unconditional)
  constraint on **every** member of that class, via Corollary P″ (the
  unordered form of the already-certified Lemma P′) + the already-certified
  Lemma XC — with no restriction to indices past the witness (removing the
  outline's flagged worry about needing a separate finite check for small
  indices; that check turns out to be unnecessary once Lemma P′ is applied
  in its correct unordered form). Proved **Theorem FW1**: `W=\{2,3,83\}`
  covers `4199:(\{13\},\{17\})$ (a clean 2-case proof from 4 low-index
  witnesses). Proved **Theorem FW2**: `W=\{2,3,5,7\}` covers
  `247:(\{13\},\{19\})` (a 2-lemma reduction to 3 minimal patterns per side,
  each pair of a `3\times3=9`-case exhaustive table checked to share a
  common prime, from 6 low-index witnesses) — closing the harder of the two
  mandated instances (no singleton witness exists, as the explorer found)
  with a complete proof, not merely the numerical re-confirmation the
  explorer left in hand. Every factorization independently re-derived both
  by hand and by a freshly-written generator (further cross-validated
  against an independent brute-force full-history generator on the first
  200 terms of both sequences, exact match), and both theorems additionally
  spot-checked by a complete (not sampled) signature cross-check at
  `N=300{,}000` on each instance, zero violations. **Bonus, low-cost
  corollary (§L.4): `a_1=247` is now a fully, unconditionally SOLVED
  CONCRETE INSTANCE of the whole IMO problem** (`H=\{2,3,5,7,13,19\}`
  satisfies FCBC because `P_1=\{13,19\}` has only one possible disjoint
  core pair, which Theorem FW2 resolves unconditionally; Theorem 5.1 then
  gives explicit `T,L=51{,}870` with `a_{n+T}=a_n+L` for every `n\ge1`) —
  this does not solve the general problem (open for arbitrary `a_1`), but
  it is the hardest instance closed in this workspace to date.
  `4199:(13,17)` remains only one of `6` open channels for that `a_1`, so
  `a_1=4199` itself is not fully solved. Status remains `partial` for the
  whole problem (the general-`a_1$ claim is what the IMO problem actually
  asks for), but this is genuine, complete, unconditional progress on both
  assigned instances, strictly stronger than every prior round's negative/
  conditional findings on Case B.
- **Round 14 (this round) — closed all 5 remaining channels of
  `a_1=4199`: `a_1=4199` is now a SECOND fully solved concrete instance
  (§M).** Extended §L's Lemma WF mechanism with 2 new low-index witnesses
  (`a_{11}=4332`, core `\{19\}`; `a_{92}=5967`, core `\{13,17\}` — the
  first witness this workspace has used with a non-singleton, "pair-core"
  companion source) to derive per-class disjunctive facts for all 6
  proper cores of `P_1=\{13,17,19\}` (§M.2), then closed the 5 channels
  Theorem FW1 did not cover (§M.3) with exhaustive 2-case Boolean splits
  each (Channels 2, 3, 6 need only `\{2\}`/`\{2,3\}`; Channels 4, 5 need
  the full `\{2,3,83\}`). Independently re-derived, from scratch, the
  full exhaustiveness proof that `P_1`'s 7 nonempty subsets yield exactly
  6 disjoint unordered core pairs (§M.1, a direct `\binom{7}{2}=21=15+6`
  hand count, not merely asserted). **Found and corrected a genuine
  simplification versus the round-14 outline**: the outline's proposed
  7th witness `a_{82}=5746` (core `\{13,17\}`, `\mathrm{comp}=\{2\}`) is
  provably redundant — the only class it could constrain (`I_{19}`)
  already has an identical, and in this case strictly not-weaker, fact
  from `a_{12}` — so the closure uses exactly `6`, not `7`, witnesses (§M.1
  note). Assembled **Corollary FW1-FCBC** (§M.4, same template as §L.4's
  Corollary FW2-FCBC): `H=\{2,3,13,17,19,83\}` satisfies FCBC for
  `a_1=4199`, giving explicit `T=|\mathrm{Good}|`,
  `L=\mathrm{lcm}(2,3,13,17,19,83)=2{,}091{,}102` via the already-certified
  Theorem 5.1. Every witness factorization independently re-derived (fresh
  sieve-based generator implementing the problem's literal recursive rule,
  cross-checked against `sympy.factorint`) and every one of the 6 channel
  closures independently re-verified by a complete (not sampled) signature
  cross-check to `n=12{,}000` (§M.5), zero violations, exact match to the
  hand-derived facts. Status remains `partial` for the whole problem (the
  general-`a_1` claim, still open) — this round's contribution is a second,
  larger, fully rigorous concrete instance, not a general theorem.
- **Round 15 (this round) — formalized Corollary CRR (Common-Recruiter
  Reuse) and closed 4 more disjoint core-pair channels of `a_1=21528751`
  (§N).** Corollary CRR (§N.1) is a one-line, fully rigorous corollary of
  the already-certified Lemma WF: since Lemma WF's hypothesis and proof
  never reference which particular target core `S` was intended, a fixed
  witness `i_0` (core `S'`) forces its companion-set constraint on
  **every** core disjoint from `S'`, not just the one originally targeted
  — no new search needed. Applied this to the 4 witnesses already on file
  for `a_1=21528751` from Corollary MSF (`a_{1405},a_{11812},a_{27832}`,
  core `\{103\}`, singleton comps `2,3,7`; `a_{2575}`, core `\{197\}`,
  comp `=\{2,3,7\}`): re-derived, independently, exactly the same 4
  channel closures the round-15 explorer and outline-reviewer found
  (`(\{103\},\{1061\})`, `(\{197\},\{1061\})`, `(\{103\},\{197,1061\})`,
  `(\{197\},\{103,1061\})`, all `W=\{2,3,7\}`, §N.4) — bringing
  `a_1=21528751` to **5 of its 6 disjoint core-pair channels closed**.
  Independently re-verified the exhaustiveness of the 21-pair (`15`
  intersecting `+` `6` disjoint) enumeration for `P_1=\{103,197,1061\}`
  by direct hand count (§N.2), all 4 witness factorizations by hand and
  by fresh `sympy.factorint` check, and the two per-class facts ([Fact
  A],[Fact B], §N.3) numerically on a freshly-written, independent
  generator run to `n=30{,}000` (§N.5: `519/519` and `29{,}338/29{,}338`,
  zero violations). **Honestly did NOT close the 6th channel**
  `(\{1061\},\{103,197\})` (§N.6): proved (not merely asserted) that
  Corollary CRR structurally cannot reach it (target core `\{103,197\}`
  intersects both witness cores `\{103\}`,`\{197\}`), and found **fresh**
  evidence — a second escape pattern `\mathrm{comp}=\{11,5,23\}` in
  `I_{103,197}` at `n\le30{,}000`, distinct from the certified Permanent
  Bundle Lemma's `Q=\{11,97\}` — that the escape structure of core
  `\{103,197\}` is not known to be captured by a single bundle, so the
  outline's speculative `W=\{2,3,7,11,97\}` candidate for channel 6 is
  explicitly NOT claimed to close it. `a_1=21528751` remains open (5/6
  channels), a strict narrowing of the instance's content to one
  precisely identified channel, not a full closure. Status remains
  `partial` for the whole problem.

## Current best

### Imported (already certified — see `lemmas/`, no re-proof needed)
- **Lemma P** / **Lemma P′** (pairwise global intersection).
- **Lemma Q** / **Lemma S′** — Case I (single saturating prime) completely
  solved.
- **Lemma 1** (linear gap bound), **Domination Lemma**, **Lemma C**.
- **Lemma FN, Lemma FX + Corollary, Lemma FX2** (channel necessity
  reduction) — now strengthened by §D above (finite classes need no LMRS at
  all, a full covering set not just finite `F_{S,S'}`).
- **Lemma FH** (uncovered-pair localization) — the key tool cited in §A's
  assembly step.
- **Corollary W3′, Lemma MS** (global version, `imprint-automaton-
  periodicity`) — the template this round's local versions (§A) adapt.
- **Theorem 5.1** (Master Conditional Theorem): FCBC `\Rightarrow` the
  whole problem, exact periodicity from `n=1`.
- The reformulated open target for the whole "Gap 1" population: FCBC.
- **Corollary MSF** (`lemmas/corollary-MSF-multi-singleton-forcing.md`):
  closes channel `(\{103\},\{197\})` of `a_1=21528751` (round 14).
- **Permanent Bundle Lemma** (`lemmas/lemma-permanent-bundle.md`): proves
  bundle `Q=\{11,97\}` permanent for core `\{103,197\}` of `a_1=21528751`
  — does not claim this is the only escape bundle for that core.

### New this round (Round 15, §N — see above for the full statements/proofs)
- **Corollary CRR (Common-Recruiter Reuse), §N.1** — new, fully proved,
  general-purpose, one-line corollary of the already-certified Lemma WF:
  a fixed witness's Lemma WF conclusion holds against **every** core
  disjoint from the witness's own core, not merely the one core the
  discoverer originally targeted. Zero new search cost to apply.
- **Closure of 4 more channels of `a_1=21528751`** (§N.3–N.4):
  `(\{103\},\{1061\})`, `(\{197\},\{1061\})`, `(\{103\},\{197,1061\})`,
  `(\{197\},\{103,1061\})`, all via `W=\{2,3,7\}`, reusing the 4 witnesses
  already certified by Corollary MSF — no new witness search. Combined
  with Corollary MSF's own channel, `a_1=21528751` now has **5 of 6**
  disjoint core-pair channels closed.
- **Exhaustiveness re-verification (§N.2)**: `P_1=\{103,197,1061\}`'s 7
  nonempty subsets give exactly `15` intersecting `+` `6` disjoint `=21`
  unordered pairs, hand-counted independently.
- **Honest non-closure of channel 6, `(\{1061\},\{103,197\})` (§N.6)**:
  proved Corollary CRR structurally cannot reach it (target core
  intersects both witness cores); found fresh evidence (a second, distinct
  escape pattern `\{11,5,23\}` in `I_{103,197}` at `n\le30{,}000`, beyond
  the certified Permanent Bundle Lemma's `\{11,97\}`) that the escape
  structure is not known to be single-bundle, so the outline's speculative
  `W=\{2,3,7,11,97\}` is explicitly NOT claimed to close this channel.
  `a_1=21528751` remains open (5/6 channels) — not yet a third fully
  solved concrete instance.

### New this round (Round 14, §M — see above for the full statements/proofs)
- **Closure of Channels 2–6** of `a_1=4199` (`(\{13\},\{19\})`,
  `(\{17\},\{19\})`, `(\{13\},\{17,19\})`, `(\{17\},\{13,19\})`,
  `(\{19\},\{13,17\})`) — fully proved, unconditional, each via an
  exhaustive 2-case Boolean split from the per-class disjunctive facts of
  §M.2 (themselves Lemma WF applications to 6 fixed low-index witnesses,
  one fewer than the outline proposed — `a_{82}` shown redundant, §M.1).
- **Exhaustiveness proof (§M.1)** that `P_1=\{13,17,19\}`'s 7 nonempty
  subsets yield exactly 6 disjoint unordered core pairs (direct hand count,
  `\binom{7}{2}=21=15\text{ intersecting}+6\text{ disjoint}`) — reusable
  template for any future `|P_1|=3` instance.
- **Corollary FW1-FCBC**: `a_1=4199` fully, unconditionally solved
  (explicit `H=\{2,3,13,17,19,83\}`, `T=|\mathrm{Good}|`,
  `L=2{,}091{,}102`) — a SECOND complete concrete instance of the whole
  IMO problem, and the largest (`|P_1|=3`, 6 channels) closed to date.

### New this round (Round 13, §L — see above for the full statements/proofs)
- **Lemma WF (Witness Forcing) + Corollary P″** — new, fully proved,
  unconditional, general-purpose (any doubly-infinite or finite disjoint
  core pair, any sequence satisfying this problem's hypotheses): a fixed
  low-index witness forces a disjunctive constraint on **every** member
  (not just later ones) of a complementary-core class.
- **Theorem FW1**: Conjecture (JW) holds for `4199:(\{13\},\{17\})`,
  `W=\{2,3,83\}` — fully proved, unconditional, instance-specific.
- **Theorem FW2**: Conjecture (JW) holds for `247:(\{13\},\{19\})`,
  `W=\{2,3,5,7\}` — fully proved, unconditional, instance-specific.
- **Corollary FW2-FCBC**: `a_1=247` fully, unconditionally solved (explicit
  `H,T,L`) — a complete concrete instance of the whole IMO problem.

### New this round (round 5)
- **Channel Assembly Theorem (§A)** — fully proved: `(LMRS_{S,S'})` for
  every channel `\Rightarrow` FCBC, with an explicit finite `H`, citing
  Lemma FH for zero-leakage routing.
- **Channel Splitting Lemma (§B)** — fully proved: `(LMRS_{S,S'})`
  `\Leftrightarrow` `(MRS_S)` and `(MRS_{S'})`, reducing to `\le2^k-1`
  one-sided conjectures.
- **Finite-class direct covering (§D)** — fully proved, strengthens Lemma
  FX2: finite imprint classes need no conditional machinery at all.
- **Numerical findings (§C, §E)** — Channel Splitting identity confirmed
  exactly (zero mismatches, 12 `a_1`, multiple checkpoints); `a_1=2747`,
  `a_1=247` both pass with no counterexample; `a_1=21528751` gives a new,
  far harder data point for `(MRS)`/`(MRS_S)` (§E's specific "local
  `\{103\}`" numbers were later found by the round-5 proof-reviewer to
  actually describe the global antichain, not the local one — see the
  correction note above; the *existence* of a much harder stabilization
  instance for the *global* antichain stands, cross-validated by brute
  force, but is not established as a *local* `(MRS_S)` phenomenon).

### New this round (round 6)
- **Companion-Disjointness Coarsening Lemma (§F)** — fully proved,
  unconditional (from Lemma P′ alone): if two witnesses with disjoint
  companion prime-sets exist for a proper core `S`, every realized radical of
  class `S` is a superset of one of finitely many "coarse bucket" bare
  values. Genuinely new, not previously in the population; corrects (does
  not merely complete) the round-6 outline's literal Step 2, which is false
  as stated (refuted by hand on `a_1=247`, §F).
- **Bucket-Exclusion Corollary (§F)** — fully proved: a coarse bucket's bare
  value can be permanently blocked (Permanent-Inadmissibility) by a third
  witness disjoint from it; used to fully explain (not just numerically
  observe) why `a_1=247`'s `S=\{13\}` antichain has exactly 3, not 4,
  elements.
- **Full verification on both mandatory examples (§F)** — `a_1=247`: the
  criterion's hypothesis holds, correctly predicting and explaining the
  freeze. `a_1=2747`, `S=\{41\}`: the criterion's hypothesis fails
  (exhaustively checked through `n=400`, every witness's companion set
  `\supseteq\{2,3,7\}`), correctly predicting the observed non-freeze
  (fan growth `\{7,q,41\}` until the bare value `\{7,41\}=T_{\{7,41\}}`, an
  exact FOM value confirmed `=a_{163}=11767`, is finally realized).

### New this round (round 7)
- **Escape-Confinement Lemma (§G, Step 1)** — fully proved, unconditional
  (from Lemma P′ alone): an escape from a blocked coarse bucket must
  contain a prime from the specific blocking witness's own companion set —
  not an arbitrary new prime. Genuinely new, general-purpose, proposed for
  certification.
- **Escape-recursion depth data (§G, Step 2)** — 13 fresh (bucket, core,
  `a_1`) instances traced to an exact witness/prime chain; maximum
  realized depth found is `2`, no depth-`\ge3` instance found.
- **Recruiter-Alignment pattern (§G, Step 3)** — a precise, exactly-matched
  (zero exceptions across 13 instances) empirical relation between depth
  and alignment with a small recruiter set `W(a_1)`, explicitly flagged as
  conditional on the (refuted-in-general) Hypothesis (GW), not a proof.
- **Branching-tree non-termination finding (§G, Step 4)** — a concrete,
  reproducible demonstration that the naive full-branching formalization of
  escape-confinement recursion does not visibly terminate within depth 6 on
  the hardest tested case, diagnosing why: the actual small depth in
  practice comes from cross-bucket domination (§F), an external fact, not
  from the recursion's own structure.

### New this round (round 8)
- **Freeze-Confinement Domination Lemma (§H, Step 1)** — fully proved,
  unconditional given `(MRS_S)`: every realized class-`S` radical (for
  every `i\in I_S`, not merely late ones) contains some element of the
  eventually-frozen minimal antichain `𝓜_{n^*}^S`. Genuinely new (first
  time stated/applied to a single core in isolation, not as half of a
  two-sided channel), reuses only the already-certified minimality argument.
- **Honest correction of the round-8 outline's numeric depth-bound
  corollary (§H, Step 2)** — the claimed bound `d(\kappa)\le\max_{C'}
  |C'\setminus S|` does not follow from domination (which gives a *lower*
  bound, `d(\kappa)\ge|C'\setminus\kappa|`, the reverse direction); not
  certified, reported as a genuine correction with the exact obstruction
  identified.
- **Singleton Recruiter Identity (§H, Step 3)** — new, sharper, precisely-
  scoped conjecture (not proved): if `𝓜_{n^*}^S` is a singleton `\{C'\}`,
  `d(\kappa)=|C'\setminus\kappa|` exactly. Verified with zero exceptions on
  all `9` populated-bucket data points across both hardest known cores
  (`a_1=21528751,S=\{197\}`; `a_1=2747,S=\{67\}`) — explains, rather than
  restates, round 7's Recruiter-Alignment pattern.
- **`S^+` Necessity + Finiteness Lemma (§H, Step 4)** — fully proved: every
  exactly-realized bare value of class `S` contains `S^+:=\bigcap_{i\in
  I_S}\mathrm{rad}(a_i)`, finite whenever `I_S` is infinite (one-line
  application of the already-certified Generalized Lemma C to `I_S`).
- **Vacuity Proposition and Intersection-Fragility Proposition (§H, Step
  5)** — both fully proved, general-purpose: (i) if a coarse bucket
  `\kappa\subseteq S^+`, the outline's proposed `S^{++}_\kappa` refinement
  equals `S^+` identically (no improvement possible); (ii) no
  intersection-over-a-subclass invariant (`S^+`, `S^{++}`, or the
  already-certified `D_S`) can ever recover a prime absent from even one
  member of the relevant class. Together these prove `S^{++}`, as literally
  proposed by the round-8 outline, is a confirmed dead end for the
  `S=\{1061\}` sufficiency counterexample — a genuine negative result with
  full worked computation (§H, Step 5), not an unfinished search.

### New this round (round 10)
- **Greedy Augmentation Lemma (§I, Step 1)** — fully proved, unconditional
  (from Lemma P′ alone): the greedy `\max(i,j)`-minimal-pair augmentation
  process is well-defined and every prime it adjoins lies outside `P_1`.
- **Termination-Sufficiency Lemma (§I, Step 2)** — fully proved: if the
  adjoined primes are ever confined to a fixed finite set `K_0`, the
  process halts within `|K_0|` steps and the Stabilization Conjecture
  holds for `(S,S')`, with explicit witness `W\subseteq B_0\cup K_0`.
- **Refutation of the `S^+_S\cup S^+_{S'}` candidate for `K_0` (§I, Step 3)**
  — fresh, independent, exhaustive computation: on `a_1=21528751`,
  `(S,S')=(\{1061\},\{103,197\})`, this candidate is identically contained
  in `B_0`, adding no new primes, while `B_0` alone provably fails to
  cover (`94` violating cross pairs at `N=3{,}000{,}000`).
  Cross-confirms the already-certified Intersection-Fragility Proposition
  in a new setting (a cross-core union of two intersections, not
  previously checked).
- **First-`K`-Prefix Recruitment Conjecture (§I, Step 4)** — new, sharper,
  precisely-stated open replacement target; verified with `K=5`,
  exhaustively, on the hardest known instance (zero violations among all
  `13{,}181{,}000` cross pairs); explicitly reported as unproved, with the
  precise obstruction (Lemma P′ gives existence, not magnitude/
  provenance) identified.

### New this round (round 12)
- **Sandwich Uniqueness Lemma (§K, Step 1)** — fully proved, general-purpose
  (any doubly-infinite disjoint core pair): the Realized-Backbone/UCR
  mechanism forces its covering set `W` to equal exactly the anchor class's
  full companion intersection `B_{\mathrm{full}}(z)`, for either anchor
  choice `z\in\{S,S'\}` — no freedom to substitute a smaller or different
  realized set. Needs no Backbone Permanence hypothesis to state or prove.
- **Complete resolution of `a_1=4199`'s pair `(\{13\},\{17\})` for this
  mechanism (§K, Steps 2–3)** — proved, not merely tested, that both
  possible anchors fail: `\{17\}`-anchor fails because
  `B_{\mathrm{full}}(\{17\})=\varnothing` (two concrete disjoint companion
  sets, `\mathrm{comp}(a_3)=\{2,31\}`, `\mathrm{comp}(a_5)=\{3,83\}`);
  `\{13\}`-anchor fails via an exhaustive, hypothesis-free dichotomy citing
  the already-certified Lemma ERD-C (witness `a_5=4233`, radical
  `\{3,17,83\}`, blocks `\kappa=\{2,13\}` from ever being realized at any
  index).

## Open gaps

1. **`(MRS_S)` (single-class minimal-radical antichain stabilization) for
   doubly-infinite imprint classes — the sole remaining gap for this
   approach, further sharpened but still not closed.** Equivalent (§A + §B)
   to FCBC's entire remaining content: prove, for every nonempty
   `S\subseteq P_1` with `I_S` infinite (finitely many, `\le2^k-1`), that
   the minimal-radical antichain of the subsequence `(a_i)_{i\in I_S}`
   eventually stabilizes. Round 6's Coarsening Lemma (§F) gives a genuine,
   verified partial mechanism (reduces the *coarse shape* of the antichain
   to finitely many buckets whenever two disjoint-companion witnesses
   exist), but **does not close `(MRS_S)`**: the precise obstruction (§F,
   "Why the Coarsening Lemma alone does not finish the proof") is that
   blocking a bucket's bare value does not block its proper supersets, and
   ruling those out requires a cross-bucket domination argument not
   established in general — of the same essential difficulty as the shared
   companion-count/chain-count bound left open by every sibling approach.
   Additionally, for cores like `a_1=2747`'s `S=\{41\}` where the
   Coarsening Lemma's own hypothesis fails (no two disjoint-companion
   witnesses), no mechanism at all — from this approach — currently bounds
   the resulting fan; the numerically observed finiteness there (collapse at
   `n=163`, stable through `n=400`) is not backed by a general proof.
   **Round 7 addendum**: attempted to close this via a bound on
   escape-recursion depth (§G) — a genuinely different candidate
   well-founded structure from bundle-size/`|S|`-induction (both foreclosed,
   see `current.md`'s Rules). Real depth stayed `\le2` in every one of 13
   fresh instances tested, but no uniform bound was proved: the
   Recruiter-Alignment pattern that would give one (§G, Step 3) presupposes
   Hypothesis (GW), itself refuted in general this round, and the natural
   proof strategy (branching-tree induction) was shown not to visibly
   terminate (§G, Step 4). The escape-recursion approach, on investigation,
   reduces to the same cross-bucket domination gap rather than resolving it
   independently — this open gap is unchanged in substance, now with one
   more confirmed-insufficient attack on record.
   **Round 8 addendum**: fully proved the domination half of the gap's
   natural corollary (Freeze-Confinement Domination Lemma, §H Step 1) —
   this closes off any lingering hope of an *independent* well-founded
   depth recursion once and for all, unconditionally (given `(MRS_S)`
   itself, which remains the open hypothesis). Corrected the round-8
   outline's own claimed depth-bound formula (§H Step 2 — does not follow,
   wrong direction) and replaced it with a sharper, numerically exact but
   still-conjectural Singleton Recruiter Identity (§H Step 3): proving this
   conjecture is diagnosed to be of essentially the same difficulty as
   `(MRS_S)` itself, not an easier stepping stone. The `S^+`/`S^{++}`
   extended-imprint program (§H Steps 4–5) gives a genuine necessary
   condition (`S^+`, certified) but is proved (Vacuity + Intersection-
   Fragility Propositions) structurally incapable of supplying a *sufficient*
   condition in general — any prime that is "almost always" but not always
   present in a class (as with `11` for `S=\{1061\}`, present in `18` of
   `19` known members) is invisible to this entire family of mechanisms.
   **This narrows what a correct proof must look like**: it cannot be a pure
   set-intersection construction over any subclass of `I_S`; it needs either
   a density/eventual (co-finite) argument robust to finitely many
   exceptions, or a fundamentally different combinatorial mechanism not yet
   identified by any approach in this population.
2. **Periodicity from `n=1`** — not this approach's concern; fully closed
   by `intersecting-family-covering-construction`'s Theorem 5.1, imported.
3. **Round 10 addendum (supersedes item 1 above as this approach's live
   target, per Theorem SW narrowing the whole problem to the Stabilization
   Conjecture): existence of `K_0` for the Termination-Sufficiency Lemma
   (§I, Step 2).** The well-ordering scaffolding is now fully rigorous
   (§I, Steps 1–2); the sole remaining content is showing the greedy
   process's forced primes are confined to a fixed finite set. The
   outline's own candidate (`S^+_S\cup S^+_{S'}`, a pure intersection) is
   refuted (§I, Step 3, fresh computation). The sharper First-`K`-Prefix
   Recruitment Conjecture (§I, Step 4, a union over a bounded prefix) is
   strongly evidenced (exhaustive verification on the hardest known
   instance) but not proved — the missing ingredient is a magnitude/
   provenance sharpening of Lemma P′ (pinning the identity of the forced
   common prime, not just its existence), which this and every closely
   related program in this workspace (`(UB_S)`, `S^{++}`, Recruiter-
   Alignment, cross-bucket domination) has independently failed to supply
   across 10 rounds — the "count vs. magnitude" wall, restated here in its
   sharpest and most precisely scoped form yet.
4. **Round 11 addendum — `(MRS_S)` restricted to the pair's two cores,
   proved (not just conjectured) to entail the already-flagged equi-hard
   Multi-Companion hitting-set target for `S=\{103,197\}` (§J Step 5), with
   the toolkit's structural inability to bound antichain width pinned down
   explicitly (§J Step 6).** This does not newly close anything, but it
   converts the round-10/round-11-outline's suspicion ("this may just be
   the same wall in new vocabulary") into a proved fact for the concrete
   mandated instance — the open content going forward is the same
   already-identified hitting-set/antichain-width-boundedness gap, now
   known via a full derivation (not merely observed numerically) to be
   unavoidable via this route. Two new lemmas (Local Equivalence Theorem,
   Subset Lemma) are genuine reusable content even though they do not close
   the gap.
5. **Round 12 addendum — the Realized-Backbone/UCR mechanism this
   approach contributed as a second, independent route to closing
   Conjecture (JW) for "Case B" pairs is proved (§K) not to close
   `a_1=4199`'s pair `(\{13\},\{17\})`.** `247:(13,19)` was never in scope
   (structurally vacuous for this mechanism, confirmed by fresh
   computation, ceded to `sunflower-bundle-closure`). This does not open a
   new gap in the whole-problem architecture — Conjecture (JW) for
   `4199:(13,17)` remains open via `sunflower-bundle-closure`'s independent
   NIDF-pigeonhole mechanism, unaffected by this finding — it only closes
   off one specific route this approach explored, honestly reported as a
   complete negative result rather than left as a stall.
6. **Round 13 addendum — Conjecture (JW) for `4199:(13,17)` and
   `247:(13,19)` is now CLOSED (§L, Theorems FW1/FW2), superseding item 5's
   "remains open" status for `4199:(13,17)` (closed via a genuinely
   different mechanism than the Realized-Backbone/UCR route item 5 refuted
   — Finite Low-Index Witness-Chaining, §L.1, needs no Backbone Permanence
   or class-wide intersection at all).** What remains open, precisely: (a)
   generalizing this mechanism beyond the two mandated instances (whether
   suitable low-index witnesses always exist for an *arbitrary* Case B pair
   — Conjecture (WCE), explicitly assigned to sibling `sunflower-bundle-
   closure` this round, not attempted here); (b) `4199`'s other `5`
   disjoint core-pair channels (`(\{13\},\{19\})`, `(\{17\},\{19\})`,
   `(\{13\},\{17,19\})`, `(\{17\},\{13,19\})`, `(\{19\},\{13,17\})`) — none
   of these were examined this round, so `a_1=4199` is not fully solved
   even though its one mandated channel is; (c) the general problem for
   arbitrary `a_1`, unaffected in difficulty by this round's work (two
   concrete instances closed, no new general technique beyond Lemma WF
   itself, which is already fully general-purpose but still needs
   instance-specific witnesses supplied by inspection, exactly as items
   (a)/(b) above make precise).
7. **Round 14 addendum — item 6(b) is now CLOSED: all 6 disjoint
   core-pair channels of `a_1=4199` are proved (§M), so `a_1=4199` is now
   a SECOND fully solved concrete instance (Corollary FW1-FCBC, §M.4),
   after `a_1=247` (§L.4).** What remains open, precisely, is unchanged in
   *kind* from item 6(a)/(c) — only the instance count has grown: (a)
   Conjecture (WCE) — does a suitable finite low-index witness collection
   always exist for an *arbitrary* Case B pair, of arbitrary `a_1`? Still
   open in general (assigned to sibling `witness-chaining-universal-
   existence`/`sunflower-bundle-closure`, not attempted here); the two
   fully closed instances (`247`, one channel; `4199`, six channels) are
   strong constructive evidence the mechanism is broadly applicable, but
   are not a proof for arbitrary `a_1` — each required inspecting actual
   low-index terms by hand/computer to find suitable witnesses, with no
   a-priori guarantee (yet) that such witnesses always exist or are always
   low-index; (b) no other `a_1` instances attempted by this approach this
   round (`2747`, `4087` are the concern of sibling `sunflower-
   inadmissibility-toolkit`); (c) the general problem for arbitrary `a_1`
   remains open, unaffected in difficulty by this round's work — this is
   instantiation of an already-general mechanism (Lemma WF) to one more
   concrete `a_1`, not a new proof technique.
8. **Round 15 addendum — Corollary CRR closes 4 more channels of
   `a_1=21528751` for free (§N), but the instance is NOT yet a third
   fully solved concrete instance.** `a_1=21528751` now has 5 of its 6
   disjoint core-pair channels closed (`(\{103\},\{197\})` via the
   already-certified Corollary MSF; the other 4 via §N.3–N.4). The 6th,
   `(\{1061\},\{103,197\})`, resists this approach's own mechanism for a
   structural reason proved in §N.6 (not merely observed): the target
   core `\{103,197\}` is not disjoint from either of the two witness
   cores `\{103\}`,`\{197\}` on file, so Lemma WF/Corollary CRR cannot be
   aimed at it at all, and the only alternative source of a witness
   (core `\{1061\}`) has no singleton-companion member at any depth
   checked. Fresh evidence this round (§N.6: a second, distinct escape
   pattern `\{11,5,23\}` in `I_{103,197}`, beyond the certified Permanent
   Bundle Lemma's `\{11,97\}`) shows the core `\{103,197\}`'s escape
   structure is not known to be captured by any single fixed bundle,
   so closing channel 6 (if possible) needs a genuine resolution of that
   open Multi-Companion-Escape-Completeness question — equivalent in
   difficulty to `(MRS_S)` for this specific core, i.e. exactly item 1's
   gap, not a shortcut around it. This item does not change the kind of
   gap remaining (still `(MRS_S)`/Conjecture (WCE) in general), only
   sharpens exactly which one channel of one instance is still open.

## Cases to cover

Case I (single saturating prime) — fully solved, Lemma S′. Case II — the
entire content of this approach; within Case II: channels touching a finite
imprint class are now **fully and unconditionally resolved** (§D, no
conditional hypothesis needed at all — a strengthening over round 3–4's
"resolved modulo Lemma FF/FX2"); channels between two doubly-infinite
classes reduce (§B) to `(MRS_S)` for each of the (finitely many, `\le2^k-1`)
doubly-infinite classes individually — this remains open in general, but as
of round 14 **two concrete instances have ALL their disjoint core-pair
channels fully closed via a different, independent route** (§L/§M:
`a_1=247` (1 channel) and `a_1=4199` (all 6 channels), via Conjecture
(JW)/the Stabilization Conjecture directly, not via `(MRS_S)`) — these are
genuine exhibited, complete instances, not merely reductions, of the general
"doubly-infinite disjoint core pair" case.

## Full proof
(Not present — Status is `partial` for the whole problem (the IMO problem's
claim is for arbitrary `a_1`; general `(MRS_S)`/Conjecture (JW) for an
arbitrary doubly-infinite disjoint core pair remains open). §A's Channel
Assembly Theorem and §B's Channel Splitting Lemma are complete, unconditional
(modulo `(MRS_S)`) proofs; §D's finite-class resolution is fully
unconditional; **§L's Theorem FW1/FW2 and §M.3's Channels 2–6 are complete,
unconditional proofs of Conjecture (JW)** for `4199:(\{13\},\{17\})`,
`247:(\{13\},\{19\})`, and all 5 remaining disjoint core-pair channels of
`4199`. **§L.4's Corollary FW2-FCBC and §M.4's Corollary FW1-FCBC are each a
complete, unconditional proof of the *entire* IMO problem's conclusion for
one specific instance** (`a_1=247`, `H=\{2,3,5,7,13,19\}`, `L=51{,}870`;
`a_1=4199`, `H=\{2,3,13,17,19,83\}`, `L=2{,}091{,}102` — both stated and
proved in full above, self-contained modulo the two already-certified
imported theorems Theorem SW and Theorem 5.1). The general-`a_1` claim is
not established by this approach — see "Open gaps" item 7 for the precise,
minimal remaining content.)

## Promotable lemmas

- **Theorem FW1-Full (§M.3) + Corollary FW1-FCBC (§M.4), new this round** —
  proposed for certification. Fully proved, unconditional: all 6 disjoint
  core-pair channels of `a_1=4199` (`P_1=\{13,17,19\}`) satisfy Conjecture
  (JW) with a uniform witness set `\{2,3,83\}` (a strict subset,
  `\{2\}`/`\{2,3\}`, suffices for 3 of the 6 channels); consequently
  `H=\{2,3,13,17,19,83\}` satisfies FCBC for `a_1=4199`, and (via the
  already-certified Theorem 5.1) `a_1=4199` is a fully, unconditionally
  solved concrete instance of the whole IMO problem
  (`T=|\mathrm{Good}|`, `L=2{,}091{,}102`). Uses only Lemma WF (already
  certified) applied to 6 fixed, exactly-computed low-index witnesses
  (`a_2,a_5,a_9,a_{11},a_{12},a_{92}`) — no new general-purpose lemma
  beyond Lemma WF itself, but a complete, reusable, instance-specific
  result (parallel to `a_1=247`'s already-certified Corollary FW2-FCBC).
  **Reusable technique** (not a certified general theorem, but worth
  recording as a template): for a general `|P_1|=3` instance, look for a
  witness with a *pair-core* (2-element core, e.g. `\{13,17\}`) with a
  small companion set — its complement in `P_1` is always a single
  element, so it gives an unusually strong (often unconditional-singleton)
  fact about that one complementary singleton class, exactly the mechanism
  that closed Channel 6 (`(\{19\},\{13,17\})`) via `a_{92}`.
- **Channel Assembly Theorem (§A)** — new, proposed for certification.
  Fully proved: if `(LMRS_{S,S'})` holds for every channel of `P_1`, then
  the explicit finite union `H:=P_1\cup\bigcup H^{(S,S')}` satisfies FCBC.
  Includes a fully self-contained proof of the local domination lemma and
  local Lemma MS (verbatim adaptations of the already-certified global
  Corollary W3′/Lemma MS to a restricted finite-per-step index universe).
  General-purpose: applies to any sequence satisfying Lemma P/P′ (i.e. any
  instance of this problem's hypotheses), not specific to any particular
  `a_1`.
- **Channel Splitting Lemma (§B)** — new, proposed for certification. Fully
  proved: for disjoint nonempty `S,S'\subseteq P_1`, the local channel
  antichain `𝓜_n^{(S,S')}` splits exactly as `𝓜_n^S\sqcup𝓜_n^{S'}` for
  every `n`, because cross-side domination is provably impossible.
  Consequently `(LMRS_{S,S'})\Leftrightarrow(MRS_S)\wedge(MRS_{S'})`.
  General-purpose, unconditional, no dependency on any open hypothesis.
- **Finite-class direct covering (§D)** — new, proposed for certification.
  Fully proved: if `I_S` is finite, `H_S:=\bigcup_{i\in I_S}
  \mathrm{rad}(a_i)` unconditionally covers every pair touching `I_S`
  (4-line proof from Lemma P′). Strengthens the already-certified Lemma FX2
  from "`F_{S,S'}` finite" to a full covering-set sufficiency statement;
  supersedes the weaker conclusion for practical use (any future approach
  needing to dispose of finite-imprint-class channels should cite this, not
  re-derive Lemma FX2's finiteness-only conclusion).
- **The `a_1=21528751` stabilization data (§E)** — not a lemma (numerical,
  though independently cross-validated by brute force), but flagged as
  reusable **regression data and a difficulty benchmark** for the *global*
  antichain (see the round-5 correction note above: the specific numbers
  reported in §E describe the global antichain `𓜓_n`, not the properly
  `I_{\{103\}}`-restricted local one, which the round-5 proof-reviewer found
  collapses more simply, `1092\to3` directly, with no further changes
  through `n=30000`). Any future mechanism for global `(MRS)` should still
  be checked against `n\approx44966`/`1103\to8`; a mechanism specifically for
  local `(MRS_S)` should instead be checked against the corrected `1092\to3`
  local trajectory.
- **Companion-Disjointness Coarsening Lemma (§F, new this round)** — proposed
  for certification. Fully proved, unconditional (uses only the
  already-certified Lemma P′): for a proper core `S` with `I_S\ne\varnothing`,
  if two indices `j_1,j_2` exist with `G_{j_1}\cap S=G_{j_2}\cap S=
  \varnothing` and disjoint nonempty companion sets `\mathrm{comp}(a_{j_1})
  \cap\mathrm{comp}(a_{j_2})=\varnothing`, then every radical realized by
  class `I_S` (at any index, past or future) is a superset of `S\cup\{p,p'\}`
  for some `(p,p')\in\mathrm{comp}(a_{j_1})\times\mathrm{comp}(a_{j_2})` — a
  fixed finite set of "coarse buckets." Includes the Degenerate-case remark
  (if either companion set is empty, `I_S=\varnothing`) and the
  Bucket-Exclusion Corollary (a coarse bucket's bare value can be
  permanently blocked by a third witness via the already-certified
  Permanent-Inadmissibility Lemma). General-purpose: applies to any proper
  core of any sequence satisfying this problem's hypotheses; genuinely new
  content, not a restatement of the Channel Assembly/Splitting machinery.
  **Honest scope note for certification**: this lemma is a real structural
  reduction (unconditionally true, useful for narrowing candidate radicals)
  but is **not** by itself a proof of `(MRS_S)` — it does not bound
  cross-bucket domination (see §F's diagnosis), so a future approach citing
  it should not treat "Coarsening Lemma applies" as equivalent to "channel
  freezes."
- **Permanent-Inadmissibility Lemma** — elementary (one line from the
  definition of admissibility: the greedy rule's requirement `\gcd(x,a_i)>1`
  for all `i\le n` only ever gains constraints as `n` grows, so a single
  failure at some fixed `i=j` is never subsequently repaired), used
  repeatedly in §F (Bucket-Exclusion Corollary, the `a_1=247` bucket-4
  exclusion). Proposed for certification as a standalone reusable fact,
  distinct from and more primitive than the Coarsening Lemma.
- **Escape-Confinement Lemma (§G, new this round)** — proposed for
  certification. Fully proved, unconditional (uses only the
  already-certified Lemma P′, exactly as the Coarsening Lemma does): if a
  coarse bare value `\kappa=S\cup Q` is blocked by witness `j_3`
  (`\mathrm{rad}(a_{j_3})\cap\kappa=\varnothing`), then every `i\in I_S`
  with `\mathrm{rad}(a_i)\supsetneq\kappa` has `\mathrm{rad}(a_i)\cap
  \mathrm{comp}(a_{j_3})\ne\varnothing`, i.e. every escape is confined to
  the specific blocking witness's own companion set, not an arbitrary new
  prime. General-purpose: applies to any proper core of any sequence
  satisfying this problem's hypotheses, independent of `a_1`.
  **Honest scope note for certification**: this is a genuine sharpening of
  what an "escape" can look like, but (per §G's Steps 2–4, an
  investigation this round did in full, not merely flagged) it is **not**
  by itself sufficient to bound escape-recursion depth uniformly — the
  Recruiter-Alignment pattern that would give a conditional bound
  presupposes the (refuted-in-general) Hypothesis (GW), and the natural
  branching-tree proof strategy for an unconditional bound was shown not to
  visibly terminate on a concrete case. A future approach citing this
  Lemma should not treat "escape-confinement applies" as equivalent to
  "escape depth is bounded" — exactly analogous to the existing honest
  scope note on the Coarsening Lemma above.
- **Recruiter-Alignment data (§G, Step 3, new this round)** — not a lemma
  (empirical, conditional on the unproved/refuted-in-general Hypothesis
  (GW)), but flagged as reusable regression data: on every one of 13 fresh
  (bucket, core, `a_1`) instances tested (`a_1\in\{21528751,2747\}`, cores
  `\{197\},\{67\}`, plus 6 more cores of `a_1\in\{247,4199,385\}`), realized
  escape depth exactly equals `3` minus the bucket's overlap with the
  recruiter set `\{2,3,7\}`, and zero-overlap buckets are always
  unpopulated. Any future attempt reviving a `W(a_1)`-based mechanism
  should be checked against this exact data (and against the outline-
  reviewer's nested-core counterexample) before being trusted.
- **Freeze-Confinement Domination Lemma (§H, Step 1, new this round)** —
  proposed for certification. Fully proved, unconditional given `(MRS_S)`
  (uses only the identical minimality argument already certified as Local
  Corollary W3′/Local Lemma MS's Step 1, §A, here applied to a single
  core's own class `I_S` rather than a two-sided channel): if `𝓜_n^S`
  freezes at `n^*`, then every `i\in I_S` (with no restriction to "late"
  indices) has `\mathrm{rad}(a_i)\supseteq C'` for some `C'\in𝓜_{n^*}^S`.
  General-purpose: applies to any proper core of any sequence satisfying
  this problem's hypotheses. **Honest scope note**: this Lemma does *not*
  imply any numeric upper bound on escape-recursion depth (§H, Step 2 shows
  the natural derivation gives a lower bound instead) — a future approach
  citing it should not conflate "domination holds" with "depth is bounded."
- **`S^+` Necessity + Finiteness Lemma (§H, Step 4, new this round)** —
  proposed for certification. Fully proved: `S^+:=\bigcap_{i\in I_S}
  \mathrm{rad}(a_i)` is a lower bound on every exactly-realized bare value
  of class `S` (one line), and is finite whenever `I_S` is infinite (one-line
  application of the already-certified Generalized Lemma C to the index set
  `I_S`, with the stabilized value shown to equal the full infinite
  intersection exactly as in the already-certified Single-Companion
  Finiteness Lemma's proof for `D_S`/`J_S`). General-purpose. **Honest scope
  note**: necessary, not sufficient — see the Vacuity/Intersection-Fragility
  Propositions below for the proved reason this cannot be strengthened to a
  sufficiency statement by any pure-intersection refinement.
- **Vacuity Proposition and Intersection-Fragility Proposition (§H, Step 5,
  new this round)** — both proposed for certification, both fully proved,
  both general-purpose (apply to any index subclass and any prime, not
  specific to any `a_1` or core). Vacuity: if a candidate refinement
  condition `\kappa\subseteq S^+`, the restricted-subclass intersection
  `S^{++}_\kappa` (as defined by the round-8 outline) equals `S^+`
  identically. Intersection-Fragility: an intersection over any index set
  `I` can never contain a prime absent from even one member of `I`. Together
  these constitute a genuine, structural negative result: no member of the
  entire family of pure set-intersection invariants (`S^+`, `S^{++}`, `D_S`)
  can close the sufficiency gap for a core whose recruited primes are only
  "almost always" (not universally) present — the concrete, worked
  counterexample is `a_1=21528751,S=\{1061\}`'s missing prime `11` (absent
  from exactly `1` of `19` known class members). Any future sufficiency
  mechanism for this gap must be provably robust to finitely many
  exceptional class members; a future approach should cite these two
  Propositions to immediately rule out re-deriving another pure-intersection
  variant without first addressing this obstruction.
- **Greedy Augmentation Lemma (§I, Step 1, new this round)** — proposed for
  certification. Fully proved, unconditional (from Lemma P′ alone, no
  `(MRS_S)`/`S^+`/any conditional machinery): for any doubly-infinite
  disjoint core pair `(S,S')`, the greedy `\max(i,j)`-minimal-uncovered-
  pair augmentation process is well-defined at every non-halted step, and
  every prime it adjoins lies outside `P_1` and is distinct from every
  previously adjoined prime. General-purpose: applies to any doubly-
  infinite disjoint core pair of any sequence satisfying this problem's
  hypotheses, not specific to `a_1=21528751`.
- **Termination-Sufficiency Lemma (§I, Step 2, new this round)** — proposed
  for certification. Fully proved: if the greedy process's adjoined primes
  are ever confined to a fixed finite set `K_0` (depending only on
  `a_1,S,S'`), the process halts within `|K_0|` steps and produces an
  explicit finite covering set `W\subseteq B_0\cup K_0`, so the
  Stabilization Conjecture holds for `(S,S')`. General-purpose; a clean
  pigeonhole argument, no dependency on any specific instance. **Honest
  scope note for certification**: this is a *conditional* theorem — the
  hypothesis (`K_0` exists) is not established for any doubly-infinite
  pair in general; §I, Step 3 shows the natural candidate `S^+_S\cup
  S^+_{S'}` does not supply it. A future approach citing this Lemma should
  treat it as isolating, not discharging, the remaining open content.
- **Refutation of the `S^+`-union candidate for `K_0` (§I, Step 3, new
  this round)** — a fresh, independent, exhaustive numerical refutation
  (not a lemma, but reusable regression data plus a cross-confirmation of
  the already-certified Intersection-Fragility Proposition in a new,
  cross-core setting): on `a_1=21528751`, `(S,S')=(\{1061\},\{103,197\})`,
  `S^+_{\{1061\}}\setminus P_1=\{2,3,7\}` and
  `S^+_{\{103,197\}}\setminus P_1=\varnothing`, both already inside `B_0`,
  so `S^+_S\cup S^+_{S'}` provably cannot serve as `K_0`. Any future
  attempt reviving an intersection-based (as opposed to union/prefix-
  based) candidate for `K_0` should be checked against this exact instance
  before being trusted.
- **Local No-Resurrection Lemma, Local Interval Lemma, and Local
  Equivalence Theorem (§J, Steps 1–3, new this round)** — proposed for
  certification as a merged file (analogous to the existing merged
  `theorem-V-veto-finite-iff-MRS.md`). Fully proved, unconditional (given
  only `I_S` infinite, the same standing hypothesis every other lemma in
  this family already carries): `(MRS_S)\iff\mathcal V_S^{\mathrm{loc}}:=
  \bigcup_n\mathcal M_n^S` finite. General-purpose: applies to any proper
  core `S` (with `I_S` infinite) of any sequence satisfying this problem's
  hypotheses, not specific to `a_1=21528751` or to doubly-infinite pairs
  specifically (the restriction to pair-cores is this round's *scope*
  choice, not a mathematical restriction of the lemma itself). **Honest
  scope note**: this is a pure equivalence between two ways of stating
  `(MRS_S)`, exactly parallel to how the already-certified Theorem V is a
  pure equivalence for the global object — it does not prove `(MRS_S)`
  itself, which remains open (see §J Step 5's No-Shortcut Corollary for
  why it is not expected to be free).
- **Subset Lemma `\mathcal V_S\subseteq\mathcal V_S^{\mathrm{loc}}` (§J,
  Step 4, new this round)** — proposed for certification. Fully proved
  (a four-line "fewer competitors ⟹ weaker minimality requirement"
  argument), upgrading the round-11 outline-reviewer's numerically-checked
  containment to an unconditional proof. General-purpose, no dependency on
  `I_S` infinite even (holds for any proper core `S`). **Use note**: this
  is the key link used in the No-Shortcut Corollary (§J Step 5) to show
  `(MRS_S)\Rightarrow\mathcal V_S` finite; any future approach wanting to
  relate the local (per-core, `I_S`-restricted) and global
  (Theorem-CD-style) antichain-freezing hypotheses for the same core
  should cite this Lemma rather than re-derive the containment.
- **No-Shortcut Corollary (§J, Step 5, new this round)** — a proof, not
  merely a numerical finding: composing the Local Equivalence Theorem, the
  Subset Lemma, the already-certified `\Lambda_S`-Reduction Lemma, and the
  already-certified Permanent Bundle Lemma + Multi-Companion Reduction
  Proposition, shows that `(MRS_S)` for `S=\{103,197\}` (a concrete
  in-scope core with a certified genuine multi-companion bundle
  `\{11,97\}`) entails resolving the already-flagged equi-hard-to-FCBC
  hitting-set target. Proposed for certification as a worked instance of a
  general pattern: **any** proper core `S` with a certified realized
  multi-companion bundle of size `\ge2` inherits this same entailment (the
  proof uses no property of `\{103,197\}` beyond "a certified size-`\ge2`
  permanent bundle exists for `S`" — stated generally in §J Step 5's chain
  of implications). A future approach should cite this to avoid re-deriving
  the "does `(MRS_S)` buy tractability" question from scratch for any
  other core with a known multi-companion bundle.
- **Sandwich Uniqueness Lemma (§K, Step 1, new this round)** — proposed for
  certification. Fully proved, general-purpose (any doubly-infinite
  disjoint core pair `(S,S')`, either anchor `z\in\{S,S'\}$, of any
  sequence satisfying this problem's hypotheses): if a nonempty finite set
  `W` disjoint from `P_1` witnesses Conjecture (JW) for `(S,S')` via the
  Realized-Backbone/UCR mechanism (full-class containment on side `z`,
  plus exact realization of `W` as some `I_z`-member's companion set), then
  `W` is forced to equal `B_{\mathrm{full}}(z):=\bigcap_{k\in
  I_z}\mathrm{comp}(a_k)` exactly — a two-line sandwich argument needing no
  Backbone Permanence hypothesis. **Use note**: this is the general
  mechanism-level fact behind why the Realized-Backbone/UCR route, if it
  works at all for a pair, has no flexibility in choosing `W` — a future
  approach attempting this mechanism on a different pair should first
  compute `B_{\mathrm{full}}(z)$ for each candidate anchor and check both
  (i) nonemptiness and (ii) exact realizability (e.g. via Lemma ERD-C)
  before investing further effort, exactly as done in §K for
  `4199:(13,17)`.
- **Resolution of `a_1=4199`'s pair `(\{13\},\{17\})` for the
  Realized-Backbone/UCR mechanism (§K, Steps 2–3, new this round)** — not a
  general lemma (instance-specific), but a complete, reusable proof
  disposing of this instance for this mechanism: `B_{\mathrm{full}}
  (\{17\})=\varnothing` (direct 2-witness computation) and
  `B_{\mathrm{full}}(\{13\})\in\{\{2\},\varnothing\}` with **both**
  possibilities shown to fail the mechanism (the `\{2\}` case via
  Lemma ERD-C applied to `\kappa=\{2,13\}`, blocked by `a_5=4233`). Any
  future approach revisiting this exact pair via this exact mechanism
  should cite this instead of re-deriving it.
- **Lemma WF (Witness Forcing) + Corollary P″ (§L.1, new this round)** —
  proposed for certification. Fully proved, unconditional, general-purpose
  (any two disjoint nonempty cores `S,S'\subseteq P_1`, any fixed index
  `i_0\in I_{S'}`, any sequence satisfying this problem's hypotheses — not
  specific to any `a_1`): every `k\in I_S`, with **no restriction relative
  to `i_0`**, satisfies `\mathrm{comp}(a_k)\cap\mathrm{comp}(a_{i_0})\ne
  \varnothing`; if `|\mathrm{comp}(a_{i_0})|=1` this is an unconditional
  single forced prime, not merely a disjunction. Uses only the already-
  certified Lemma P′ (in its unordered/symmetric form, Corollary P″, proved
  here in one line) and Lemma XC. **Use note**: this is the general
  mechanism behind the Finite Low-Index Witness-Chaining technique — any
  future approach wanting to force a disjunctive or singleton constraint on
  a whole complementary-core class from one fixed low-index term should
  cite this lemma directly rather than re-deriving the Lemma P′ + Lemma XC
  composition; the "no restriction relative to `i_0`" clause is the key
  improvement over informally stated "later-index" versions of this idea
  (e.g. the round-13 outline's own Step 1/2 phrasing), and removes any need
  for a separate finite check of small indices below a witness's position.
- **Theorem FW1 (§L.2, new this round)** — a complete, instance-specific,
  fully proved, unconditional resolution: Conjecture (JW) holds for
  `4199:(\{13\},\{17\})` with explicit witness set `W=\{2,3,83\}`, via 4
  low-index witnesses (`a_2,a_5,a_9,a_12`) and a 2-case proof (Lemma WF's
  singleton case at `a_{12}` does the heavy lifting). Every factorization
  independently re-derived by hand and by two independent generators (a
  fast antichain-based one and a brute-force full-history one, cross-
  checked against each other on the first 200 terms). Any future approach
  needing Conjecture (JW) for this exact pair should cite this instead of
  re-deriving it.
- **Theorem FW2 (§L.3, new this round)** — a complete, instance-specific,
  fully proved, unconditional resolution: Conjecture (JW) holds for
  `247:(\{13\},\{19\})` with explicit witness set `W=\{2,3,5,7\}`, via 6
  low-index witnesses (`a_2,\dots,a_7`), two supporting lemmas (Lemma A,
  Lemma B — each a clean 2-case proof reducing to 3 "minimal patterns" per
  side) and an exhaustive `3\times3=9`-case table verifying every pair of
  minimal patterns shares a common prime. This closes the harder of the two
  mandated Case B instances (no singleton witness exists in this instance,
  confirmed both by the round-13 explorer's search of the first 100 terms
  and independently re-confirmed here) with a complete proof, not the
  numerical-only confirmation on record from prior rounds. Any future
  approach needing Conjecture (JW) for this exact pair should cite this
  instead of re-deriving it.
- **Corollary FW2-FCBC (§L.4, new this round)** — a complete, instance-
  specific, fully proved, unconditional result: `a_1=247` is a fully
  solved concrete instance of the whole IMO problem (`H=\{2,3,5,7,13,19\}`
  satisfies FCBC; Theorem 5.1 then gives explicit `T=|Good|`,
  `L=\mathrm{lcm}(H)=51{,}870`, `a_{n+T}=a_n+L` for every `n\ge1`). The
  3-line derivation (Theorem CD's core map is total and nonempty on every
  index + `P_1=\{13,19\}` has a unique disjoint core pair + Theorem FW2)
  is general-purpose in shape and directly reusable: **any future `a_1`
  with `|P_1|=2` for which the single resulting disjoint core pair's
  Conjecture (JW) is proved is automatically, by the identical 3-line
  argument, a fully solved concrete instance of the whole problem** — this
  observation (not itself a new lemma, but a reusable proof template) is
  worth recording for any future approach targeting other small-`|P_1|`
  hard instances.
- **Corollary CRR (Common-Recruiter Reuse) (§N.1, new this round)** —
  proposed for certification. Fully proved, unconditional, one-line,
  general-purpose (any sequence satisfying the problem's hypotheses, any
  fixed witness index `i_0` with core `S'`): Lemma WF's conclusion for a
  fixed witness `i_0`, once established, holds simultaneously against
  **every** core `S\subseteq P_1` disjoint from `S(i_0)`, not only the one
  core `i_0` was originally found to constrain — because Lemma WF's own
  hypothesis and proof (Corollary P″ + Lemma XC) never reference any
  property of the target core `S` beyond "nonempty and disjoint from
  `S'`." Zero new search or computation cost: any already-computed witness
  factorization can be looked up against every other disjoint target for
  free. **Use note**: this is now the cheapest first step for any future
  approach holding one or more Lemma-WF/Corollary-MSF witnesses for a
  disjoint core pair `(S_0,S')` of an `|P_1|\ge3` instance — before
  searching for any new witness, check every other core disjoint from
  `S'` (or from the other witness's core) for a free channel closure, as
  demonstrated on `a_1=21528751` (§N.3–N.4: 4 channels closed this way
  from witnesses already on file, no new search).
- **Instance-specific application: 4 more channels of `a_1=21528751`
  closed via Corollary CRR (§N.3–N.4, new this round)** — fully proved,
  unconditional: `(\{103\},\{1061\})`, `(\{197\},\{1061\})`,
  `(\{103\},\{197,1061\})`, `(\{197\},\{103,1061\})`, all with
  `W=\{2,3,7\}`, reusing the 4 witnesses already certified in Corollary
  MSF. Combined with Corollary MSF's own channel `(\{103\},\{197\})`,
  `a_1=21528751` has 5 of its 6 disjoint core-pair channels closed. The
  6th, `(\{1061\},\{103,197\})`, is explicitly NOT claimed closed (§N.6) —
  any future approach should not assume `a_1=21528751` is a fully solved
  concrete instance without separately resolving that one channel.
