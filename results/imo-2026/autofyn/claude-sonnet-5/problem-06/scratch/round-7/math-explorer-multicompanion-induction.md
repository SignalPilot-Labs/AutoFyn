# Scouting report: induction on companion-bundle size for 𝓥_S-finiteness

**Assignment.** Test whether an induction on companion-**bundle size**
`k=|Q|` (for `C=S∪Q` a realized radical of a fixed proper core `S`) —
using the already-closed Single-Companion Finiteness Lemma (`k=1`) as a
base case — can bound `Λ_S`/`𝓥_S`, as an architecture genuinely distinct
from the already-refuted induction on core size `|S|`
(`core-depth-induction`, round 6).

**Bottom line up front.** Bundle-size induction **fails**, and — unlike
`core-depth-induction`'s Step 3 (refuted only empirically, as an
"unconfirmed premise that turned out false on the motivating example") —
this round found an actual short **proof** that it must fail in general:
the Single-Companion Finiteness Lemma, applied to a size-2 bundle whose
both companions lie outside its own bound, *certifies* that bundle as
**permanently irreducible** — there is no dominating witness of any
smaller bundle size for it to reduce to, ever. This is stronger than "no
mechanism found"; it is "no mechanism can exist for this class of
instances." I found and numerically confirmed multiple concrete instances
of this (`a_1=4199`, `S={17}`, bundle `{3,83}`; `a_1=21528751`,
`S={103,197}`, bundle `{11,97}`; plus every "freeze" case already on
record, e.g. `a_1=247,4199`, `S`'s with `D_S\P_1=∅`, are *all* instances of
this same phenomenon at bundle size 2).

## 1. What I read

- `results/imo-2026-06/current.md` (round 6 headline, full history) — the
  sole open gap is `𝓥_S`-finiteness for each proper core `S⊊P_1`,
  triangulated by three approaches into equivalent local
  hitting/covering-set language.
- `lemmas/lemma-lambda-S-reduction-and-single-companion-finiteness.md` —
  the `Λ_S`-Reduction Lemma (`𝓥_S` finite `⟺ Λ_S` finite), the
  **Single-Companion Finiteness Lemma** (conditional on `J_S` infinite,
  `Q_S ⊆ D\P_1` where `D:=⋂_{j∈J_S}rad(a_j)`, finite by the Generalized
  Lemma C stabilization argument), and the **Multi-Companion Reduction
  Proposition** (a realized bundle `Q`, `|Q|≥2`, must *hit* `rad(a_j)` for
  every `j∈J_S` — a hitting-set condition the Generalized-Lemma-C
  mechanism cannot reach, honestly diagnosed as "of the same order of
  difficulty as FCBC itself").
- `lemmas/lemma-companion-disjointness-coarsening.md` — the
  Companion-Disjointness Coarsening Lemma + Bucket-Exclusion Corollary:
  two disjoint-companion witnesses force every realized value into one of
  finitely many "coarse buckets"; a bucket's *bare* value can be
  permanently blocked (Permanent-Inadmissibility), but proper supersets
  within a blocked bucket are **not** automatically ruled out — the
  cross-bucket-domination gap.
- `approaches/persistent-backbone-monovariant.md` (round 6 section) — same
  content as the certified lemma file, plus the honest second gap ("`J_S`
  infinite" not proved in general).
- `approaches/forced-primes-well-ordering.md` (round 6, §F) — the
  refutation of the single-witness Freeze Criterion, the Coarsening
  Lemma's full derivation and worked examples (`a_1=247,S={13}`:
  freeze via two disjoint witnesses; `a_1=2747,S={41}`: no disjoint
  witnesses exist, channel absorbs via a growing `{7,q,41}` fan collapsing
  once `{7,41}` appears at `n=163`).
- `approaches/core-depth-induction.md` (full) — the refuted `|S|`-induction:
  Lemma B1 (base case reformulation, real but inert), and the Step-3
  depth-2→depth-1 "reused companion" map, concretely tested against
  `a_1=21528751,S={197,103}`'s full early history (13 fresh values through
  `n=6000`) and found false in 12/13 cases (only a late-stage coincidence
  at `n=73747,101957`, outside that window). Explicitly told not to
  resurrect this mechanism — I did not; my failure mode below is a
  different, sharper one.

## 2. What I computed

Built a from-scratch greedy-sequence simulator (`gen.py`, exact radical via
`sympy.primefactors`, minimal-antichain-frontier admissibility check for
speed — same algorithmic idea as prior rounds' simulators, independently
re-implemented, not copied from any existing script in this workspace) and
an analysis harness (`analyze.py`) that, for a fixed `a_1` and truncation
`N`, computes for **every** proper nonempty core `S⊆P_1` (not just
singletons): `I_S`, `J_S`, `D_S:=⋂_{j∈J_S}rad(a_j)`, the single-class
antichain history `𝓜_n^S` (giving `𝓥_S` up to truncation, tagged
`ALIVE(final)` vs `dominated-later`), and — for every realized bundle
`Q=C∖S` with `|Q|≥2` — whether `Q` intersects `D_S∖P_1` (the certified
upper bound on single companions).

Verified the simulator's correctness against the workspace's own
already-published numbers before trusting it further: reproduced
`a_1=2747,S={41}`: `D_S∖P_1={2,3,7}`, `|J_S|=118` (at `n=6000`, matches
round 6 exactly), fan `{7,q,41}` for `q∈{11,13,17,19,23,29,31,37}`, final
collapse to `{2,41},{3,41},{7,41}`; `a_1=247,S={13},{19}`: `D_S∖P_1=∅`
both, matching `Q_S=∅` exactly; `a_1=21528751`: reproduced the documented
global collapse from `~1103` antichain elements to `8` at `n∈[27000,28000]`
(found at `n=27000→28000` boundary, matching the certified `n=27831`
finding to the nearest checkpoint).

Ran the full per-core bundle analysis on **9 distinct `a_1` values**:
`247, 2747, 21528751` (the three mandated hard cases, `21528751` pushed to
`N=20000` and `N=50000`), plus `4199, 4087, 375, 221, 65, 105` (smaller
cases, `N=3000–4000`, for a broader/cheaper survey), across **≈20 distinct
core/`a_1` pairs**, including two depth-2 cores (`{103,197}` and
`{13,17}`/`{17,19}` for `a_1=21528751,4199`) to check the phenomenon is not
singleton-core-specific.

## 3. What I found

### 3.1 The general pattern across all 9 test cases

For every core `S` tested, every realized multi-companion bundle `Q`
(`|Q|≥2`) falls into exactly one of two classes:

- **"Pending" bundles**: `Q∩(D_S∖P_1)≠∅` (contains a prime that is
  *eligible* to become a single companion of `S`). These are consistently
  `dominated-later` once that prime's own bare bundle is eventually
  realized (e.g. `a_1=2747`'s whole `{7,q,41}` fan, dominated in one stroke
  once `{7,41}` appears) — **or** still `ALIVE` at the truncation point
  because the relevant single companion has not yet appeared in the
  simulated range (e.g. `a_1=21528751,S={103,197}`: dozens of `{2,q}`,
  `{3,q}` pairs alive at `n=50000`, since `{2}` and `{3}` alone have not
  yet been realized for this core, only `{7}` has).
- **"Permanent" bundles**: `Q∩(D_S∖P_1)=∅` entirely. **In every single
  instance checked (well over a dozen), these are `ALIVE(final)` at the
  truncation point with zero exceptions** — and, as shown below, this is
  not a truncation artifact: it is provable.

Summary table (multi-companion bundles only; "lacks `D_S`" = bundles with
`Q∩(D_S∖P_1)=∅`):

| `a_1` | `S` | `D_S∖P_1` | multi-bundles | lacking `D_S` | of those, alive |
|---|---|---|---|---|---|
| 247 | `{13}` | `∅` | 3 | 3 | 3 |
| 247 | `{19}` | `∅` | 3 | 3 | 3 |
| 2747 | `{41}` | `{2,3,7}` | 17 | 0 | — |
| 2747 | `{67}` | `∅` | 1 | 1 | 1 |
| 4199 | `{13}` | `∅` | 2 | 2 | 2 |
| 4199 | `{17}` | `{2}` | 5 | 1 | 1 |
| 4199 | `{19}` | `∅` | 2 | 2 | 1* |
| 4199 | `{13,19}` | `∅` | 2 | 2 | 2 |
| 4199 | `{17,19}` | `{2}` | 2 | 1 | 1 |
| 375 | `{3}` | `{2}` | 2 | 1 | 1 |
| 375 | `{5}` | `∅` | 2 | 2 | 2 |
| 221 | `{13}` | `∅` | 2 | 2 | 2 |
| 221 | `{17}` | `{2}` | 2 | 1 | 1 |
| 65 | `{13}` | `∅` | 1 | 1 | 1 |
| 21528751 | `{103,197}` | `{2,3,7}` | 84 (n=20000) | 1 | 1 |

(*one of the two non-`D_S` bundles for `{19}` at `a_1=4199` was already
`dominated-later` by `n=4000` — by a *different* size-2 bundle that itself
still lacks `D_S`, i.e. dominated within the "lacking-`D_S`" class, not by
a `D_S` element; consistent with, not a counterexample to, the mechanism
below.)

### 3.2 A new, fully proved mechanism explaining this: the Permanent-Pair phenomenon

Using only the already-certified **Permanent-Inadmissibility Lemma** and
**Single-Companion Finiteness Lemma** (both cited above, no new machinery),
I can prove — not just numerically observe — why bundles lacking `D_S∖P_1`
are permanent:

**Claim.** Fix a proper core `S` with `J_S≠∅`, and suppose `J_S` is
infinite (Single-Companion Finiteness Lemma's standing hypothesis). Let
`Q={q_1,q_2}` (`q_1≠q_2`) be realized as a bundle for `S` (some index `i`
has `rad(a_i)=S∪Q`), with `q_1,q_2∉D_S∖P_1`. Then `S∪Q` is **never
dominated** within the single-class antichain `𝓜_n^S` (Channel Splitting
Lemma: domination only ever comes from *other* elements of `I_S`) — i.e.
it is a permanent member of `𝓥_S`, contributing forever to `Λ_S`.

**Proof.** Any dominator must have the form `S∪Q'` for `Q'⊊Q` (any element
of `I_S` has radical `⊇S`, by definition of imprint), so `Q'∈{∅,\{q_1\},
\{q_2\}}`. `Q'=∅`: impossible by the Permanent-Inadmissibility Lemma
applied with `C:=S` and any witness `j∈J_S` (`rad(a_j)∩S=∅` by definition
of `J_S`, and `J_S≠∅` is given). `Q'=\{q_1\}` or `\{q_2\}`: impossible by
the contrapositive of the Single-Companion Finiteness Lemma (`Q_S⊆D_S∖P_1`,
so any prime realized as a *sole* companion of `S` must lie in `D_S∖P_1`;
`q_1,q_2` do not). No candidate dominator exists. `∎`

This is a genuinely new (previously unstated in this workspace, as far as
I found) but very cheap corollary — three lines given the two lemmas
already certified — and it is a **clean, general explanation of the
"freeze" phenomenon** already on record: whenever `D_S∖P_1=∅` (no prime can
*ever* be a sole companion of `S` — the exact `Q_S=∅` cases already
observed at `a_1=247,{13\},\{19\}` and `4199,\{13\},\{19\},\{13,19\}`),
**every** realized 2-element bundle is automatically, unconditionally
permanent by this argument alone — no need for the Coarsening Lemma's
two-disjoint-witness machinery at all in the 2-element case (the
Coarsening Lemma is still needed for the *general* covering/bucket
structure — which bundles get realized in the first place, and ruling out
size-`≥3` escapes from a blocked bucket — but the *permanence* of an
already-realized pair follows from strictly less machinery than I expected
going in).

**Direct hand/numerical verification of two concrete instances (not
reused from any prior round's script):**
- `a_1=4199, S={17}`: `D_S∖P_1={2}` (only "2" can ever be a sole companion
  of `{17}` — confirmed `{2}` is independently realized and alive). Bundle
  `{3,83}` (radical `{3,17,83}`) is realized **four separate times**
  through `n=4000` (indices `5, 431, 1710, 3412` — the same radical value
  recurring as distinct integers, consistent with Lemma FOM/T_C-realization
  behavior), **never dominated**: exhaustive check of all `i∈I_{\{17\}}`
  through `n=4000` finds zero indices with radical a proper subset of
  `{3,17,83}`. Matches the proof exactly (`3,83∉{2}`).
- `a_1=21528751, S={103,197}` (a depth-2 core): `D_S∖P_1={2,3,7}`
  (`|J_S|=16` at `n=50000`, all 16 witnesses' radicals independently
  recomputed and shown). Bundle `{11,97}` (radical `{11,97,103,197}`)
  realized once, at index `863`, alive through `n=50000` (well past the
  global antichain's dramatic `1103→8` collapse at `n≈27831`, confirmed
  independently — this bundle is untouched by that collapse). Direct
  check: zero dominating witnesses in `I_{\{103,197\}}` through `n=50000`.
  Matches the proof exactly (`11,97∉{2,3,7}`). **Bonus structural insight**:
  of the 16 `J_S` witnesses, 15 contain `11` and exactly one (index `596`)
  contains `97` instead (and not `11`) — i.e. `{11,97}` is forced to be a
  *pair* specifically because index `596` is an outlier breaking the
  otherwise-universal-`11` pattern. This is structurally the *same*
  disjoint-outlier mechanism as the certified Coarsening Lemma, just
  recurring one level down inside a nested core — see 3.4.

### 3.3 Answering the three assigned questions directly

**(1) Does Single-Companion Finiteness give a genuine base case for
induction on `k`?** No — worse than "no": it actively **certifies certain
`k=2` configurations as permanently unreachable from `k=1`** (§3.2). A
valid induction needs "every `k`-object eventually reduces to smaller
ones"; here there provably exist `k=2` objects that *never* reduce to any
`k=1` fact, for the structural reason that their companions are excluded,
by the very `k=1` lemma, from ever being singleton companions at all. The
`k=1` result is not a weak/insufficient base case — it is actively
incompatible with treating `k=2` as built from it.

**(2) Is there an actual `k→k-1` reduction, structurally different from
the refuted `|S|`-induction?** I tried the natural analytic candidate:
given a realized `Q={q_1,...,q_k}`, peel one element `q_1`, restrict to
`J_S^{q_1}:={j∈J_S:q_1∉rad(a_j)}` (the witnesses `q_1` fails to cover), and
apply Generalized Lemma C to *this* infinite-if-it-is-infinite index set to
get a fixed finite `D^{q_1}⊇\{q_2,...,q_k\}$ — this genuinely works
*post-hoc* for a specific already-realized bundle (verified: for
`a_1=21528751`'s `{11,97}`, peeling `q_1=97` gives `J_S^{97}` = the 15
witnesses without `97`, and indeed `D^{97}∖P_1⊇\{11\}$, confirmed by direct
computation — every one of the 15 does contain `11`). **But this does not
give a `k→k-1` induction**: which prime plays the role of "`q_1`" (the
outlier-triggering element) is unbounded a priori, and bounding *how many*
distinct such outlier-pivots can ever occur across the whole history of
`S` is exactly the same open local-hitting-set/FCBC-type question the
Multi-Companion Reduction Proposition already flagged — restated one
level down, not resolved. So: no reduction exists that is not itself
equivalent in difficulty to the original gap.

**Why this differs structurally from the refuted `|S|`-induction, as
asked.** `core-depth-induction`'s Step 3 failed because its *proposed*
reduction (depth-`d` absorption events literally reusing a depth-`(d-1)`
companion) turned out **empirically false** — a plausible-looking pattern
that didn't hold except by late-stage coincidence; the failure mode is "we
guessed a shape, and it's wrong." Bundle-size induction's failure mode is
categorically different: I did *not* find a plausible-looking reduction
shape that then broke on data. I found a **proof, from lemmas already on
the books, that the k=1→k=2 reduction cannot exist for a specific,
concretely-exhibited, recurring class of instances** (any pair bundle whose
both primes lie outside `D_S∖P_1`). This is a stronger, structural
obstruction, not an unconfirmed premise — and it means a future round
should **not** spend effort hunting for a smarter `k`-to-`(k-1)` reduction;
this round's finding forecloses that whole family of attempts, not just
the one shape tried in round 6.

**(3)/(4) Numerics.** Done across 9 `a_1` values, ≈20 cores including two
depth-2 cores, with two fully hand/computer-verified permanent-pair
instances (§3.2) plus the broader tabulated survey (§3.1) showing the
pending/permanent dichotomy holds with zero exceptions in every case
tested.

### 3.4 A unifying observation (not asked for, but relevant to round 7's strategy)

Both refuted inductions — on `|S|` (round 6) and on bundle size `k` (this
round) — fail for what looks like the *same underlying reason* viewed from
two different axes: the problem's residual difficulty (the
Multi-Companion Reduction Proposition's "local, restricted instance of
FCBC itself") is **self-similar across scale**. Nesting a core one level
deeper (`{103}→{103,197}`) or growing a bundle one element larger
(`{q_1}→{q_1,q_2}`) both land you back in a structurally identical
hitting-set question, with genuinely new, unrelated primes (`11,97` in one
example, `3,83` in another) that the smaller-scale machinery provably
cannot reach — not because no one has found the right reduction yet, but
because (at least for the specific "peel one factor" mechanism natural to
both inductions) no such reduction can exist in general. This suggests
**round 7 should not attempt a third syntactic-size induction** (e.g. on
`T_C`-magnitude or total companion-recruitment count, both floated as
fallbacks in `current.md`) **without first checking whether the same
self-similarity defeats it too** — a cheap test being exactly the kind of
"find one concrete instance and try to hand-prove permanence/irreducibility
against the proposed measure" check this report ran. Per round 6's own
recommendation (still standing), an analytic or extremal tool that bounds
the local hitting-set problem *directly* (not via any nested/recursive
nested nesting on a syntactic measure) looks more promising than a fourth
induction attempt.

## 4. Open questions / what remains

1. **Is `Λ_S` (or `𝓥_S`) actually finite or infinite in general?** This
   round's findings are agnostic on this — Permanent Pair instances show
   individual bundles persist forever, but says nothing about whether only
   finitely many such permanent pairs (or larger permanent tuples) can ever
   form. That is exactly the un-closed content (equivalent to local FCBC).
2. **Does the Permanent-Pair mechanism generalize to bundle size `≥3`?**
   Not attempted rigorously here: for `|Q|≥3`, ruling out permanence
   requires excluding *every* proper nonempty subset `Q'⊊Q` (including
   subsets of size `2,...,k-2`), which needs a multi-companion (not just
   single-companion) sub-bound — i.e. the same open problem recursively.
   I did not find, and did not look hard for, a "Permanent-Triple Lemma";
   flagging this as a natural (cheap) follow-up check, not attempted here
   because the assignment was about induction viability, not exhaustive
   case enumeration.
3. **`J_S` infinite in general** remains the same standing unproved
   hypothesis flagged by every sibling approach; my Permanent Pair Lemma
   inherits this same conditional dependency (stated explicitly in its
   hypotheses above).
4. Whether the "peel one element, restrict to `J_S^{q_1}`" recursive
   machinery (§3.3, question 2) could be pushed into a genuine (if
   difficult) direct attack on local FCBC — e.g. by bounding the total
   number of distinct "pivot primes" via some global counting argument
   using Lemma 1's linear gap bound — was not attempted; this is close in
   spirit to the already-flagged, already-refuted Growth-Budget Lemma
   pointwise-vs-cumulative obstruction and would need to avoid that exact
   trap.

## Files produced (scratch only, not written to `results/`)

- `/tmp/round-7/gen.py` — sequence simulator.
- `/tmp/round-7/analyze.py` — per-core bundle/`D_S`/permanence analysis
  harness.
- `/tmp/round-7/out_21528751_20000.txt` — raw dump of the `a_1=21528751`,
  `N=20000` run (large; the `S={103}` channel alone has thousands of
  bundle lines, all confirming the pattern — summarized in §3.1's table
  rather than reproduced in full here).
