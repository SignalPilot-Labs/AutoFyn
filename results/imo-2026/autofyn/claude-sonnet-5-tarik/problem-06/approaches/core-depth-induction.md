## Status
partial

## Round 7 note (proof-outliner — stays parked, not rebuilt this round)

No builder dispatched to this file this round. Recorded for the historical
record only: round 7's `multicompanion-induction` explorer
(`/tmp/round-7/math-explorer-multicompanion-induction.md`) independently
found that induction on companion-**bundle** size `k=|Q|` also fails, for a
structurally analogous reason to this file's own refuted Step 3 (induction
on core size `|S|`) — both die to the same "self-similarity across scale"
phenomenon (peeling one element of a size-`k` object lands back on a
same-order-difficulty hitting-set question with a genuinely fresh prime, not
a reduction to a size-`(k-1)` fact). This reinforces, rather than changes,
this file's own standing conclusion: **do not revive this architecture with
a third syntactic size-induction** (`T_C`-magnitude, recruitment count, or
any other single well-founded measure on companion/core structure) without
first hand-checking a concrete instance for this exact obstruction. Lemma B1
remains certified and reusable; Step 3 as conceived remains dead.

## Round 6 Build (proof-builder — this round's work, read first)

Following the round-6 outline below and the outline-reviewer's explicit
**early-feasibility instruction** ("before elaborating Step 3's machinery,
spend effort trying to construct — or definitively fail to construct — a
concrete injective/count-preserving map from `a_1=21528751`'s `S={197,103}`
depth-2 absorption events into some object derived from the already known
singleton results for `S={197}` or `S={103}`... if no such map can be found
even in this one concrete case, report this as evidence the induction schema
itself is unsound"), this round:

1. **Proved the base-case reformulation (Lemma B1) in full**, using Lemma FOM
   (reproved here inline, self-contained, so this file does not depend on the
   timing of `persistent-backbone-monovariant`'s certification pass) combined
   with the already-certified Record Characterization Lemma and Theorem CD.
   This converts "is `𝓥_{\{p\}}` finite" into a purely combinatorial statement
   about which finite prime-sets `C⊇\{p\}` (disjoint from `P_1\setminus\{p\}`)
   are ever `n`-minimal, with **no reference to the sequence's actual growing
   values** — a genuine (if modest) simplification, proved rigorously below,
   not merely asserted.
2. **Ran the mandated early-feasibility check, with fresh, independent
   computation** (not reusing any prior round's script; own simulator,
   verified against the certified Record Characterization Lemma's "fresh
   index" definition, and independently spot-checked Lemma FOM's pinning
   claim by exact computation on 4 fresh instances — see "Numerical work,"
   below). **Result: the proposed depth-2→depth-1 map FAILS.** The round-6
   explorer's two data points (`{2,103,197}` at `n=73747`, `{3,103,197}` at
   `n=101957`, each superficially matching a "companion of `\{103\}`" `\cup
   \{197\}` shape) are shown, on computing the **full** early history of the
   same channel `S=\{197,103\}` (13 fresh values through `n=6000`, not just
   the two late ones), to be an artifact of near-terminal convergence, **not**
   a law governing the channel's history: none of the 12 non-trivial fresh
   values found in the window `n\le6000` has the conjectured shape (see
   "Negative finding 1," below, full table).
3. **Found a second, independent negative finding** directly undermining the
   premise that `|S|` tracks proof difficulty: for a *fixed* `a_1`, singleton
   cores (`|S|=1`) already vary in complexity by **three orders of
   magnitude** — `a_1=21528751`: core `\{103\}` has `2363` distinct fresh
   values by `n=6000`, core `\{197\}` has `41`, core `\{1061\}` has only `2`
   (see "Negative finding 2," below). This is a fresh, independently-computed
   confirmation (own simulator, three cores compared side-by-side at
   identical `a_1`, not merely quoting the outline-reviewer's single-example
   citation) that `|S|` alone carries essentially no information about proof
   difficulty, undermining the rationale for using it as the induction's
   well-founded measure.
4. **Conclusion, following the outline-reviewer's own instruction to report
   honestly rather than build ornamental machinery on an unconfirmed
   premise:** the base case (`|S|=1`) is reformulated (Lemma B1, genuine
   progress, certified-quality) but **not closed** — no mechanism bounding
   the number of ever-fresh values in a singleton channel was found. The
   inductive step's central premise (Step 3, a depth-`d`-to-depth-`(d-1)`
   reduction) was **concretely tested against the one example the outline
   itself proposed, and failed** — the map does not exist as a general fact,
   only as a coincidental late-stage resemblance. Per the outline-reviewer's
   own stated criterion, this is reported honestly as evidence the
   strong-induction-on-`|S|` architecture, **as currently conceived, does not
   work** — a genuine RETHINK-level finding for this approach's Step 3, not
   papered over. Lemma B1 remains a valid, reusable, certified-quality
   contribution regardless of this finding (see "Promotable lemmas").

### Numerical work (own, fresh computation this round)

Simulator: exact greedy rule (`math.gcd`/radical via `sympy.primefactors`,
trial-division-based, exact — not approximate), frontier restricted to the
current minimal antichain for speed (justified by the already-certified
Lemma W3: a candidate is admissible against the whole prefix iff it
intersects every *minimal* element, since minimality is w.r.t. `⊊` and
intersecting a subset intersects every superset). Cross-checked against the
certified Record Characterization Lemma's "fresh index" definition of `𝓥`
(agree by construction — the "fresh" test, no `k<i` with `P_k\subsetneq
P_i`, is exactly what is used to build the fresh-value list).

**Sanity check (Lemma FOM's exact-value pinning claim, re-verified
independently here — not just cited from `persistent-backbone-monovariant`).**
For `a_1=21528751`, computed `T_C:=\min\{x>a_1:\mathrm{rad}(x)=C\}` via an
exact heap-based smooth-number search (not brute force) for four fresh
values found by the simulator and compared against the actual term:
`idx=280,\ C=\{2,3,7,11,1061\}`: `a_{280}=21568008=T_C` (exact match).
`idx=3,\ C=\{2,3,7,197,1301\}`: `a_3=21528948=T_C` (exact match).
`idx=146,\ C=\{2,3,59,103,197\}`: `a_{146}=21549042=T_C` (exact match).
`idx=1,\ C=P_1=\{103,197,1061\}`: `a_1=21528751\ne T_C=2217461353` — the
**expected** exception (FOM's hypothesis requires `n\ge2`; `a_1` realizes
its own radical without needing to exceed itself, exactly as documented in
every prior round's statement of FOM). Zero unexplained discrepancies.

**Negative finding 1 (Step 3's premise, concrete test, full early history).**
For `a_1=21528751`, `S=\{197,103\}` (the exact channel the round-6 outline
and explorer used to motivate Step 3), computed **every** fresh value with
core `\{103,197\}` through `n=6000` (not just the two late absorption events
at `n=73747,101957` reported by the round-6 narrow-framing explorer, which
only searched from `n=30000` onward and did not record the channel's earlier
history):

| idx | radical `C` |
|---|---|
| 1 | `\{103,197,1061\}` (`=P_1`, the trivial top-core value) |
| 146 | `\{2,3,59,103,197\}` |
| 433 | `\{2,7,19,103,197\}` |
| 576 | `\{3,5,71,103,197\}` |
| 720 | `\{2,13,41,103,197\}` |
| 863 | `\{11,97,103,197\}` |
| 1294 | `\{2,5,103,107,197\}` |
| 2296 | `\{3,103,197,359\}` |
| 3154 | `\{3,19,103,197\}` |
| 3441 | `\{5,7,31,103,197\}` |
| 4015 | `\{3,11,103,197\}` |
| 4873 | `\{3,5,73,103,197\}` |
| 5446 | `\{7,103,157,197\}` |
| 5733 | `\{3,103,197,367\}` |

**None** of these 13 non-trivial fresh values has the shape "`\{q,103\}\cup
\{197\}`" for `q` one of the depth-1 channel `S=\{103\}`'s own companion
primes (`2,3,7` — the three companions that eventually became `\{103\}`'s
permanent survivors `\{2,103\},\{3,103\},\{7,103\}` per the round-6
explorer's report). Every one of these 13 values is instead a genuinely
distinct, "messy" multi-prime bundle unrelated to any previously-established
depth-1 fact — e.g. `\{2,3,59,103,197\}` bundles *both* companions `2,3`
*and* an unrelated large companion `59` simultaneously; `\{11,97,103,197\}`
uses neither `2`, `3`, nor `7` at all. **Only** the round-6 explorer's two
much-later events (`n=73747,101957`, outside this table's range, per that
report) happen to match the "single companion, reused from depth 1" shape —
and by that late point in the process, the depth-1 channel `\{103\}` has
*already* permanently settled into exactly its three survivors `\{2,103\},
\{3,103\},\{7,103\}` (per the round-6 explorer's own report, no further
change through `n=30000`), so it is unsurprising that whichever primes are
"in the air" (globally recruited, needed to satisfy admissibility against
many other channels simultaneously — see discussion below) at that late
stage happen to already coincide with `\{103\}`'s own settled companions:
this is a **plausible byproduct of both channels drawing on the same small,
globally-useful pool of primes as `a_1`'s sequence matures**, not a
depth-hierarchy relationship between the channels. **Conclusion: the
proposed depth-2→depth-1 reduction does not hold as a general fact even
in the one example that motivated it** — the two matching events are a
late-stage coincidence, not evidence of a governing law across the channel's
full 13-generation history.

**Negative finding 2 (`|S|=1` does not track difficulty, own fresh
comparison).** Computed fresh-value counts, at identical truncation `n=6000`,
for all three singleton cores of `a_1=21528751` (`P_1=\{103,197,1061\}`):

| core `S` (`|S|=1`) | # distinct fresh values by `n=6000` |
|---|---|
| `\{103\}` | `2363` |
| `\{197\}` | `41` |
| `\{1061\}` | `2` |

A **1000-fold** spread at the identical core size `|S|=1`, for the identical
`a_1`. A second, independent instance (`a_1=2747`, `P_1=\{41,67\}`, `n=3000`):
core `\{41\}` has `20` distinct fresh values (including its own internal
"sub-fan" structure around companion prime `7` — radicals `\{7,13,41\}`,
`\{7,17,41\}`, `\{7,19,41\}`, `\{7,23,41\}`, `\{7,29,41\}`, `\{7,31,41\}`,
`\{7,37,41\}` appear as **seven separate fresh generations** before finally
being absorbed into `\{7,41\}` at index `163` — itself a genuine miniature
multi-generation structure, not a single clean event), while core `\{67\}`
has only `1`. **This directly confirms and sharpens** the outline-reviewer's
concern (raised there from a single depth-1-vs-depth-2 comparison): the
measure `|S|` used for the induction carries essentially no information
about how hard a given core's finiteness is to prove — a singleton core can
already be dramatically more complex than a depth-2 core of the *same*
`a_1` (as the reviewer found) *and*, independently, than another singleton
core of the *same* `a_1` at the *same* depth (this round's new finding). Any
correct measure for a well-founded induction on this problem would need to
track something else — perhaps a genuine "companion-recruitment count" (as
`imprint-automaton-periodicity`'s sibling approach attempts) or a
`T_C`-magnitude/prime-size-based order — not core cardinality.

## Round 6 Outline (proof-outliner directive — new approach, opened this round)

**Why a new slug, not a revision of a sibling.** Every live approach
(`persistent-backbone-monovariant`, `imprint-automaton-periodicity`,
`forced-primes-well-ordering`) attacks the shared remaining gap — finiteness
of `𝓥_S` (equivalently `(MRS_S)`) for each proper nonempty core `S⊊P_1` —
by working with `𝓥_S`/`𝓜_n` as a flat object (counting, chain-length,
companion-count, or freeze/dichotomy arguments). This approach instead
commits to a **strong induction on `|S|`**, the size of the core, which is a
genuinely different top-level architecture: the induction's well-founded
measure is `|S|∈\{1,\dots,k-1\}` (`k:=ω(a_1)`, a fixed finite integer once
`a_1` is fixed), not any property of the antichain's history. This is the
architecture this round's narrow-framing explorer flagged as the candidate
escape from the "recursive but circular" trap in the Case-I-template-
transfer idea: the resemblance between a depth-`d` channel's absorption
events and a depth-1 channel's absorption events becomes a legitimate
inductive step, not a restatement, **only if** it is accompanied by an
actual reduction (a map from depth-`d` unknowns to depth-`(d-1)` knowns),
which is exactly what this approach's Step 3 below attempts to construct
and is honest about not yet having.

**Target:** the problem's exact headline conclusion `a_{n+T}=a_n+L` for
every `n≥1`, via the already-certified chain Theorem CD + Lemma TC (`𝓥`
finite ⟺ `𝓥_S` finite for `1≤|S|≤k-1`) + Theorem V + Theorem 5.1 —
imported unchanged from `imprint-automaton-periodicity`/`persistent-
backbone-monovariant`'s certified lemmas; this approach's sole content is
closing the `𝓥_S`-finiteness gap via induction on `|S|`.

**Technique:** strong induction on core size `|S|`, base case `|S|=1`
(singleton cores), inductive step `|S|=d≥2` assuming `𝓥_{S'}` finite for
every proper core `S'` with `|S'|<d`.

**Step 1 (import, no new work).** `𝓥` finite ⟺ `𝓥_S` finite for every
`1≤|S|≤k-1` — cite Theorem CD (`lemmas/theorem-CD-core-decomposition-and-
lemma-TC.md`) and Lemma TC directly.

**Step 2 (base case `|S|=1`, OPEN, this round's genuine attempted content).**
For a singleton core `S=\{p\}` (`p\in P_1`), attempt to prove `𝓥_{\{p\}}`
finite directly. **This is NOT Case I** (Theorem CI, already certified, is
about a prime dividing *every* term of the *whole* sequence; here `p`
divides only the terms with imprint exactly `\{p\}`, a genuine subsequence
with no known closed form) — do not import Theorem CI's proof verbatim; it
needs its own argument. Candidate mechanism: use Lemma FOM (this round's new
tool — see the shared preamble in `/tmp/round-6/proof-outliner.md`, cite
whichever sibling approach certifies it first, or reprove it inline if this
approach's builder runs first) to pin every element of `𝓥_{\{p\}}` to an
exact value `T_C` (`C\supseteq\{p\}`), converting the question into "which
`C\supseteq\{p\}` are ever admissible, restricted to indices with imprint
`\{p\}`." **Not proved.** Numerical basis to build from (this round's
narrow-framing explorer, independently verified): `a_1=2747`, `S=\{41\}`
absorbs 8 companions once at `n=163` and freezes; `a_1=21528751`, `S=
\{103\}` absorbs 3 separate times (`n=1405,11812,27832`, radicals
`\{2,103\},\{3,103\},\{7,103\}`) before freezing; `a_1=21528751`, `S=
\{197\}` absorbs once with a 4-prime bundle (`\{2,3,7,197\}`) — **the base
case must handle both single- and multi-companion bundling and both
single- and multi-event channels**, not assume a uniform shape.

**Step 3 (inductive step `|S|=d\ge2`, OPEN, the approach's central novel
content).** Assuming `𝓥_{S'}` finite for every proper `S'` with `|S'|<d`,
attempt to show `𝓥_S` finite. Candidate mechanism, from this round's
`a_1=21528751`, `S=\{197,103\}` (`d=2`) example: the channel's own two
absorption events (`\{2,103,197\}` at `n=73747`, `\{3,103,197\}` at
`n=101957`) each have the shape `S\cup\{q\}` for a single companion `q` —
structurally identical to a depth-1 absorption "one level up." **The open
task is to formalize this as an actual reduction**: e.g., define a map from
"absorption events within channel `S`, `|S|=d`" to "absorption events within
some depth-`(d-1)`-scale object" and show it is injective (or otherwise
count-preserving), so that the already-assumed finiteness of the
depth-`(d-1)` case genuinely bounds the depth-`d` case, rather than merely
resembling it. **This is not constructed this round.** Two honest
obstacles, flagged explicitly (do not let the builder paper over either):
(a) there is no fixed finite ambient index set at "depth `d-1`" analogous to
`P_1` at the top level — companions `q` are unbounded in magnitude, so a
literal transplant of Theorem CD's partition-by-subset-of-`P_1` argument
does not apply one level down; (b) the "one companion at a time" shape is
not universal (see `S=\{197\}`'s 4-prime bundle in Step 2) — any reduction
map must account for multi-companion absorption events, not just
single-companion ones.

**Step 4 (conclusion, conditional on Steps 2–3).** If both close for a
fixed `a_1`, induct up from `|S|=1` to `|S|=k-1` (a finite induction, since
`k=ω(a_1)` is one fixed integer once `a_1` is fixed) to get `𝓥_S` finite for
every proper core, hence `𝓥` finite (Theorem CD), hence FCBC (Theorem
V + Lemma MS), hence the whole problem (Theorem 5.1).

## Approaches tried
- (Round 6, opening round.) Newly opened by the proof-outliner, per the
  dispatch's explicit suggestion to try a strong-induction-on-core-nesting-
  depth architecture as a genuinely different route from the existing
  counting/DM-order/channel-splitting mechanisms already tried by the
  sibling approaches in rounds 3–6. Not yet built; both the base case and
  the inductive step were open, honestly flagged as such (no false claim of
  progress beyond stating the correct target and diagnosing precisely why
  the naive "resemblance" argument is not yet a proof).
- **(Round 6, this round's build.)** Followed the outline-reviewer's mandatory
  early-feasibility instruction. **Proved Lemma B1** (base-case
  reformulation via Lemma FOM, reproved inline, plus the already-certified
  Record Characterization Lemma and Theorem CD) — genuine, certified-quality
  content, though it does not by itself bound anything (matches the
  outline's own honesty requirement). **Concretely tested Step 3's central
  premise** (the depth-2→depth-1 map) against the one example the outline
  itself proposed and **found it fails**: computing the *full* early history
  of `a_1=21528751`'s `S=\{197,103\}` channel (13 fresh values through
  `n=6000`, not just the two late events reported previously) shows 12 of
  13 non-trivial fresh values do **not** have the conjectured "reused
  depth-1 companion" shape; the two matching events reported by this round's
  explorer are shown to be a late-stage coincidence (once the depth-1
  channel `\{103\}` has already permanently settled), not a governing law.
  **Also found a second independent negative result**: `|S|=1` does not
  track difficulty even holding `a_1` fixed — three singleton cores of
  `a_1=21528751` have `2363`, `41`, and `2` fresh values respectively
  (`n=6000`), a 1000-fold spread at identical core size. **Verdict on this
  round's work**: honest, substantive negative findings plus one genuine
  reusable lemma (B1); the induction-on-`|S|` architecture's central premise
  (Step 3) does not survive its own mandated feasibility test. Status stays
  `partial` (not `unsolved`, since Lemma B1 is a real, correct, if modest,
  contribution; not `solved`, since neither the base case nor the inductive
  step closes).

## Current best

**Lemma B1 (Singleton-Core Value Pinning) — proved this round, in full.**

*Setup.* `P_1:=\mathrm{rad}(a_1)`, `k:=|P_1|`. Assume `k\ge2` (else there is
no proper singleton core to speak of — every prime divides every term, i.e.
Case I, already completely solved by the certified Lemma S′/Theorem CI, no
new work needed). Fix `p\in P_1` and set `S:=\{p\}` (a proper core, since
`k\ge2` gives `S\subsetneq P_1`).

*Statement.* Every `C\in𝓥_S` satisfies `a_{n_C}=T_C`, where `n_C` is `C`'s
first-occurrence index in the sequence `(a_n)` (i.e. the unique minimal
`n\ge1` with `\mathrm{rad}(a_n)=C`) and `T_C:=\min\{x\in\mathbb Z:x>a_1,\
\mathrm{rad}(x)=C\}` (well-defined and finite, since `(\prod_{q\in C}q)^t`
has radical `C` for every `t\ge1` and is unbounded in `t`). Equivalently:
`𝓥_{\{p\}}` finite `\iff` only finitely many finite prime sets `C` with
`p\in C` and `C\cap(P_1\setminus\{p\})=\varnothing` are ever `n`-minimal for
some `n\ge1` — a statement about which *static* sets `C` are ever admissible
at the moment they would be minimal, with no reference to the sequence's
growing numeric values beyond the fixed map `C\mapsto T_C`.

*Proof.* First, **Lemma FOM** (reproved here in full, self-contained;
independently verified by this round's outline-reviewer and by two other
sibling approaches this round — see "Cross-approach note" below): *if
`n\ge2` is the first index with `\mathrm{rad}(a_n)=C`, then `a_n=T_C`.*

Proof of Lemma FOM: admissibility of a candidate integer against a fixed
prefix `a_1,\dots,a_m` depends only on its radical (via
`\gcd(x,y)>1\iff\mathrm{rad}(x)\cap\mathrm{rad}(y)\ne\varnothing`), not its
magnitude. Suppose, for contradiction, `n\ge2` is `C`'s first occurrence
with `a_n\ne T_C`. Since `T_C` is an integer `>a_1` with radical `C`,
minimality of `T_C` among such integers gives `T_C\le a_n`; and `T_C` cannot
equal any `a_i$ (`i<n`), since that would give `\mathrm{rad}(a_i)=C`,
contradicting "`n` is `C`'s first occurrence" — so `T_C<a_n` strictly.
Hence `T_C$ lies in a unique gap `a_i<T_C<a_{i+1}` for some `i$ with
`i+1\le n` (using `a_1<T_C`, immediate from `T_C`'s definition). Since `a_n`
is admissible against every `a_j`, `j<n$ (definition of the greedy rule),
`\mathrm{rad}(a_n)\cap\mathrm{rad}(a_j)=C\cap\mathrm{rad}(a_j)\ne\varnothing`
for every `j\le i` (as `i\le n-1`); since `\mathrm{rad}(T_C)=C`, `T_C` is
also admissible against `a_1,\dots,a_i`. Combined with `T_C>a_i`, greedy
minimality of `a_{i+1}` (the smallest admissible integer `>a_i`) gives
`a_{i+1}\le T_C`; combined with `T_C\le a_{i+1}` (choice of `i`), this
forces `a_{i+1}=T_C`. But `i+1\le n-1<n` (from `a_n>T_C=a_{i+1}` and strict
monotonicity of `(a_n)`), so index `i+1<n` already realizes `C` —
contradicting "`n` is the first occurrence." Hence `a_n=T_C`. `∎` (Lemma
FOM)

Now, let `C\in𝓥_S` (`S=\{p\}`). By the already-certified Theorem CD,
`C\cap P_1=S=\{p\}$, so `C\ne P_1$ (since `|P_1|=k\ge2>1=|S|`, `C=P_1$
would force `C\cap P_1=P_1\ne\{p\}`). By the already-certified Record
Characterization Lemma, `C=P_i$ for a fresh index `i`, and (from that
lemma's own proof) `i` is in particular `C`'s first occurrence: if some
`j<i$ also had `\mathrm{rad}(a_j)=C=P_i`, freshness of `i` is not directly
violated by *equality* — but we instead take `n_C:=\min\{n\ge1:
\mathrm{rad}(a_n)=C\}\le i` directly (this minimum exists and is `\le i`
since `i` itself has radical `C`), which is `C`'s true first-occurrence
index by definition, independent of whether it coincides with a *fresh*
index. Since `C\ne P_1$ and only `a_1` has radical `P_1$ at index `1` (as
`\mathrm{rad}(a_1)=P_1$ by definition, and no other set equals `P_1$ at
index `1`), `n_C\ne1`, so `n_C\ge2`. Lemma FOM applies directly with
`n:=n_C`: `a_{n_C}=T_C`. `∎` (Lemma B1)

**Discussion.** This is genuine, if modest, progress: it removes the need
to reason about the sequence's actual growing integer values when studying
`𝓥_{\{p\}}$'s finiteness, replacing them with the fixed, `a_1`-and-`C`-
computable quantity `T_C`. It does **not**, by itself, bound anything — the
open content is entirely "which `C$ are ever `n`-minimal," exactly as
honestly flagged in the round-6 outline. This is the same status as the
already-certified Fan-Size Corollary (conditional bound on fan size given
absorption) cited in the sibling `persistent-backbone-monovariant` file:
real, correct, structural simplification, not a finiteness proof.

**Cross-approach note.** Lemma FOM's statement and proof here are
line-for-line the same content as `persistent-backbone-monovariant`'s Step 1
(round-6 outline) and this round's fan-structural explorer report; this file
reproves it inline for self-containedness (per the outline's own
instruction, "reprove it inline if this approach's builder runs first" —
timing between parallel builders this round is not guaranteed). If
`persistent-backbone-monovariant` certifies `lemmas/lemma-FOM-first-
occurrence-minimality.md` this round, this file's inline proof should be
replaced by a citation in a future round; no conflict, since both proofs are
identical in substance.

### The two negative findings (see "Round 6 Build" above for full detail and tables)

1. **The Step-3 depth-2→depth-1 map does not hold as a general fact.**
   Computed the *full* early history (not just the two late events
   previously reported) of `a_1=21528751`'s `S=\{197,103\}` channel through
   `n=6000`: `12` of `13` non-trivial fresh values do not have the
   conjectured "reused depth-1 companion" shape; only the two much-later
   events (`n=73747,101957`, outside this window) match, and are argued
   (not merely asserted) to be a late-stage coincidence — once the depth-1
   channel `\{103\}` has already permanently settled into its final three
   survivors, whichever primes are globally "in the air" for `a_1`'s
   sequence at that late stage happen to coincide with them, rather than
   being *derived from* them via any hierarchy.
2. **`|S|=1` does not track difficulty**, even for fixed `a_1`: singleton
   cores of `a_1=21528751` have `2363`, `41`, `2` fresh values respectively
   (`n=6000`) — a `1000`-fold spread at identical `|S|`.

**Conclusion.** Per the outline-reviewer's own explicit instruction, these
findings are reported as evidence that the strong-induction-on-`|S|`
architecture, **as currently conceived (Step 3's specific reduction), does
not work** — this is honestly a RETHINK-level finding for Step 3, not a
"still open, keep trying the same shape" finding. It does not rule out
*some* well-founded induction working (e.g. on companion-recruitment count,
or on `T_C`-magnitude), only that core cardinality `|S|` is not the right
measure and the specific "single companion, reused one level up" reduction
shape is not the right mechanism.

## Open gaps
1. **Base case (`|S|=1`).** Reformulated (Lemma B1, proved) but **not
   closed**: no mechanism bounds the number of ever-fresh values `C` within
   a singleton channel. This is, precisely, the identical open content
   (companion-count/generation-count finiteness) that every sibling
   approach already attacks under a different name — Lemma B1 does not
   avoid this difficulty, it only restates it in a cleaner, value-free form.
2. **Inductive step (`|S|=d\ge2`).** The specific candidate reduction
   (depth-`d` absorption events `\to` depth-`(d-1)` companion reuse) is now
   **concretely refuted** as a general law by this round's Negative finding
   1 (see above) — not merely "not yet constructed" as in the round-6
   outline, but tested against the outline's own proposed example and found
   false beyond a late-stage coincidence. A future round attempting this
   architecture would need either (a) a fundamentally different reduction
   mechanism (not "single companion reused one level up"), or (b) a
   different well-founded measure entirely (not `|S|`, given Negative
   finding 2).

## Cases to cover
Case I: fully closed, imported (Lemma S′/Theorem CI, no new work needed).
Case II: organized by `|S|=1,\dots,k-1` per Theorem CD; the base case is
reformulated but open (Lemma B1); the inductive step's proposed mechanism is
refuted (see Open gaps above); no level of the induction closes this round.

## Full proof
(Not present — Status is `partial`. Lemma B1 is a complete, correct,
certified-quality lemma, but the approach's overall target — `𝓥_S` finite
for every proper core `S` — remains open, and this round found concrete
evidence, not just an unconfirmed premise, that the approach's central
Step-3 mechanism does not work as conceived.)

## Promotable lemmas

**Lemma B1 (Singleton-Core Value Pinning).** *Statement:* for `k=|P_1|\ge2`,
`p\in P_1`, `S=\{p\}$: every `C\in𝓥_S$ is realized at its first-occurrence
index `n_C\ge2` with `a_{n_C}=T_C$ (`T_C:=\min\{x>a_1:\mathrm{rad}(x)=C\}`).
*Proved in full* above ("Current best" section of this file), building on
Lemma FOM (reproved inline here, matching `persistent-backbone-monovariant`'s
independent proof) plus the already-certified Record Characterization Lemma
and Theorem CD. Reusable by any future approach that wants to work with
`T_C`-values directly for singleton (or, with routine modification of the
`C\ne P_1$ step, any proper) core; recommend certifying into
`lemmas/lemma-B1-singleton-core-value-pinning.md` if the reviewer finds no
gap, alongside (or merged with) Lemma FOM itself if
`persistent-backbone-monovariant`'s independent proof is certified first.

**Lemma FOM (First-Occurrence Minimality) — reproved inline, not new
content beyond what `persistent-backbone-monovariant` and this round's
fan-structural explorer already established, but included here in full for
self-containedness.** See "Current best" above for the complete statement
and proof; identical in substance to the sibling approach's Step 1, so
certify only once (whichever approach's version the reviewer reaches first).
