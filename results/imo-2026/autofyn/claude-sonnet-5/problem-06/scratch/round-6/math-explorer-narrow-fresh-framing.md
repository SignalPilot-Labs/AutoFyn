## imo-2026-06

Lens: narrow mechanism hunt specifically at 𝓥_S-finiteness (S a proper nonempty
core ⊊P_1), using fresh, independent numerical simulation (not reusing any
builder script) on the three dispatched stress cases a_1=247, 2747, 21528751,
plus a_1=91, 15 as easy sanity checks. Simulator: exact greedy rule, sieve-based
trial-division factoring (fast to a_n≈4×10^7), frontier-restricted-to-minimal-
antichain admissibility check (justified: if candidate intersects every
*minimal* realized radical, it intersects every realized radical, since
minimality is w.r.t. ⊊ and intersecting a subset intersects its supersets —
this is exactly Lemma W3, already certified, so the fast simulator is provably
equivalent to the brute O(n²) definition, not just empirically close).

### Distinct openings surfaced this round

**Opening A (idea 1, dispatched lead) — validated as a genuine, reusable
PHENOMENON, but shown to be recursive/multi-layer, not flat like Case I.**
Directly tested "does Theorem CI's shape (a single explicit absorbing term
whose radical is a small fixed set, dominating an entire accumulated fan)
transfer to a per-core channel S?" **Yes, concretely, in every case checked**
— but the absorbing radical is essentially never S itself; it is `S∪{q}` for
one "companion" prime `q` (Case II's analogue of Case I's bare `{p}`):
- `a_1=2747`, `S={41}`: `a_163 = 41²·7` (radical `{41,7}`), absorbing an
  11-element fan `{41,7,q}` (`q∈{5,13,17,19,23,29,31,37}`) in one stroke.
  Verified stable (zero further channel events) through `n=100000` (600× past
  the absorption index).
- `a_1=21528751`, `S={103}`: `a_27832 = 7⁴·103²` (radical `{103,7}`),
  absorbing a **1090-element** fan in one stroke — the local antichain went
  1092→3 directly (independently reproducing the round-5 reviewer's
  correction of `forced-primes-well-ordering`'s §E numerics exactly).
  Additionally found: the other two final survivors `{2,103}` and `{3,103}`
  are **themselves** absorption events, not trivial insertions — `a_1405`
  (radical `{2,103}`) absorbed 624 elements, `a_11812` (radical `{3,103}`)
  absorbed 1670 elements. So the channel's history is *three independent
  companion-prime absorption events* (`q=2,3,7`), not one.
- `a_1=21528751`, `S={197}`: absorbing term is a **4-prime** power
  `a_2575 = 2²·3⁴·7³·197` (radical `{2,3,7,197}`) — here there is no
  isolated-singleton-survivor structure at all; the whole channel collapses
  to ONE minimal element that already "pre-bundles" three companions
  (`2,3,7`) simultaneously.
- `a_1=21528751`, `S={197,103}` (a **depth-2** core, `|S|=2`): confirms the
  recursive picture directly — pushed simulation to `n=130000` (well beyond
  round 5's `n=30000` "still growing" report) and found the channel
  stabilizes at `n=101957` via **two separate, later absorption events**:
  `a_73747=2³·103·197²` (radical `{2,103,197}`, absorbs 90 elements) and
  `a_101957=3²·103·197²` (radical `{3,103,197}`, absorbs 62 elements),
  landing on a final 5-element antichain with no further events through
  `n=130000`. This is a **new numerical result** (round 5 only knew this
  channel was still growing at `n=30000`/`60000`; it does stabilize, later,
  via the expected recursive mechanism).

**Honest assessment of Opening A:** the "shape" (an explicit finite absorbing
set eventually gets hit) is now confirmed on 5 independent channels including
the deepest tested case, so it is real structural content worth keeping in
any outline. But pushed to its natural general statement — "for every core
S there is a finite set of primes 𝒬_S such that eventually a term with
radical exactly `S∪{q}` (or a small bundle) appears for each `q∈𝒬_S`, and
these events happen only finitely often" — this is **not a new sufficient
condition**, it is essentially a restatement of 𝓥_S-finiteness itself (same
circularity trap round 5 already flagged for "H=rad(L_per)"). Do not present
Opening A as a route that avoids proving finiteness; it only sharpens *what
shape* a proof must produce (a recursive/nested collapse structure, generalizing
Theorem CI's single-layer template to a depth-`|S|`-ish cascade of absorptions,
each individual absorption looking like a miniature, prime-restricted analogue
of Case I but with no known closed form to predict *when* it will occur or
*which* companion prime `q` will be the one that gets absorbed vs. survives
forever as an isolated pair).

**Opening B (idea 2, probabilistic/second-moment on 𝓥_S) — did NOT find a
clean convergent quantity; flagging why, concretely.** The natural discriminator
(Σ 1/q over companion primes q ever recruited into a channel, or a Mertens-type
density sum) is the wrong shape: what actually needs bounding is not a density
but "how many distinct companion primes get their own absorption event before
the channel goes permanently quiet" — a *count* (2–3 in every tested case,
never observed to grow with `a_1`'s size or with core depth in absolute terms,
only the absorption *index* n and *fan size* grow, sometimes to 1000+
elements). This reframes idea 2 more sharply: the open quantity is bounded
**empirically** (2 or 3 companions per channel in all 6 tested channels across
3 stress cases) but no invariant was found this round that provably bounds
it — a genuine second-moment/Cauchy–Schwarz argument was not attempted (out
of scope per dispatch: "do not attempt a full proof"), only the numerical
groundwork was laid. This count-of-companions quantity (not Σ1/q) is the
concrete object a future round's second-moment attempt should target.

**Opening C (idea 3, direct pigeonhole via greedy minimality) — scouted, not
developed; flagged the natural obstruction.** Tried to see whether Lemma 1's
bounded-gap fact (`a_{n+1}-a_n≤L`) plus linear growth (`a_n~Ln`, Lemma 1)
gives a forcing/ordering constraint on which companion prime gets recruited
next (e.g. "smallest available" or "in increasing order"). **Checked and
refuted this specific natural guess**: for `a_1=2747`, `S={41}`, companion
primes were recruited in order `13,17,19,23,5,29,31,37` — `5` arrives *after*
`13,17,19,23`, not first, so there is no simple "smallest unused prime first"
monovariant to exploit directly. No pigeonhole argument was found this round;
this remains open ground, not ruled out, just not yet found.

### Candidate technique(s)
- A **recursive/nested finite-descent argument on core depth** (`|S|`, or
  more precisely on the "companion-count" quantity from Opening B) — the
  numerics strongly suggest an induction where proving depth-`(d-1)` channels
  finite is a genuine ingredient for depth-`d` channels (the `S={197,103}`
  depth-2 case's two absorbing events `{2,103,197}`,`{3,103,197}` look like
  two depth-1-style absorptions happening inside the depth-2 channel, echoing
  how depth-1 `S={103}`'s own absorptions `{2,103}`,`{3,103}`,`{103,7}` looked
  like miniature Case-I events). This induction is NOT written down anywhere
  in the workspace yet — it is a genuinely new organizing idea from this
  round's numerics, worth proposing to the outliner as its own approach
  (distinct from the existing DM-multiset-order and Event-Counting framings,
  which operate on 𝓜_n/𝓥 directly rather than on core depth).
- Second-moment/pigeonhole on the **companion-count**, not density (sharpened
  target for Opening B, per above).

### Cheap-kill candidates
- None found that close the gap. One useful negative cheap-kill: "companion
  primes are recruited in increasing order" is FALSE (a_1=2747 example above)
  — don't let a future round assume this without re-checking.
- A genuine unbounded-fan check (paranoia test, per memory rule about not
  trusting small-sample stabilization claims): pushed `a_1=21528751`'s
  hardest-still-open channel `S={197,103}` 4× past round 5's last checkpoint
  and it DID eventually stabilize (`n=101957`) — this is reassuring evidence
  against "maybe some channels never stabilize," but is still only evidence
  for 3 values of `a_1`, not a proof for all sequences.

### Knowledge-base entries to use
Nothing new identified beyond what prior rounds already found absent
(Mertens/Borel–Cantelli-type analytic density tooling, confirmed absent from
`knowledge_base.md` and the crux corpus in round 4). No entry in
`knowledge_base.md` was found this round that supplies a ready-made
"recursive/nested absorption" or "companion-count" combinatorial tool — this
would need to be built from scratch, as with every other certified lemma in
this workspace so far.

### Analogous past problems (cruxes)
Not queried fresh this round (out of scope for this narrow numerical lens
per dispatch instructions; round 2's memory rule already found aimo-0678
(IMO-SL 2015 N4) as the one genuinely analogous crux for the *overall*
monovariant/stabilization framing of this problem — still the best match,
already on file, nothing new to add specific to the depth/companion-count
structure found this round).

### Prior progress
Unchanged from `current.md`'s Round 5 update: whole problem reduces to
𝓥_S-finiteness for each proper core `S⊊P_1` (Theorem CD); Case I and the top
core are fully closed (Theorem CI, Lemma TC). This round did not close any
piece of the remaining gap — it produced new *empirical* structural
detail (the recursive/nested-absorption picture above) plus one genuinely
new numerical result (S={197,103} for a_1=21528751 DOES stabilize, at
n=101957, previously only known to be "still growing at n=30000/60000").

### Dead ends (do not retry)
- "Companion primes are recruited in increasing size order" — false,
  refuted by `a_1=2747`, `S={41}` (round 6, this file).
- Presenting "a finite absorbing set eventually gets hit for each core" as a
  new sufficient condition distinct from 𝓥_S-finiteness — it is circular,
  same trap as round 5's already-refuted `H=rad(L_per)` characterization
  (round 6, this file; consistent with round 5's Rule).
- Σ1/q (density-style) as the natural quantity for a second-moment argument
  on 𝓥_S — the right quantity looks like a *count* of companion primes with
  their own absorption event, not a density sum (round 6, this file;
  refines but does not contradict round 3's already-certified finding that a
  pointwise-in-N Markov/Cauchy–Schwarz bound only gives per-time-slice
  control, not global finiteness).

### Small-case / intuition notes (all CONJECTURE, not proof)
- Every tested Case-II channel (6 channels across 3 stress cases) is finite,
  with a small number (2–4) of distinct "companion prime" absorption events,
  regardless of how large the individual fans grow before absorption (fans
  up to 1670 elements observed). This is consistent with, but does not
  prove, 𝓥_S-finiteness in general.
- Deeper cores (larger `|S|`) take much longer to stabilize (S={197,103}
  depth 2: n≈101957 vs. S={103} depth 1: n≈27832 vs. S={41} depth 1 for a
  smaller `a_1`: n≈163) and involve absorbing sets that are themselves
  larger (3-prime combos vs. 2-prime combos) — suggestive of a genuine
  depth-dependent difficulty escalation, i.e. an inductive proof on `|S|`
  is the shape most consistent with the data, not a uniform bound
  independent of depth.
- No case was found (yet) where a channel fails to stabilize after
  aggressive re-testing well past its previously-reported "still growing"
  checkpoint — mild evidence 𝓥_S-finiteness is true in general (as already
  believed), not evidence of *how* to prove it.

### Concrete next steps for the outliner
1. Consider opening a genuinely new approach built around the **recursive/
   nested-absorption induction on core depth `|S|`** (Opening A's
   generalization) — distinct in mechanism from the existing DM-multiset-order
   (imprint-automaton-periodicity) and Event-Counting (persistent-backbone-
   monovariant) approaches, since it operates on the *core-decomposition
   structure* (Theorem CD) directly rather than on 𝓜_n/𝓥 as flat objects.
   The base case (`|S|=1`) already has 3 independently-verified worked
   examples in this report to build intuition/lemma statements from.
2. If pursuing this, the central unproved fact to isolate as its own
   sub-lemma (mirroring how round 4/5 isolated (MRS)/Theorem V) should be
   something like: "within a depth-`d` channel, the number of *maximal*
   simultaneously-growing companion-prime sub-fans is finite, and each
   sub-fan's growth is itself governed by a depth-`(d-1)`-style channel" —
   this is NOT proved or even fully formalized here, only observed
   numerically; a real formalization attempt is next round's/this round's
   outliner's job, not this explorer's.
3. Opening B (companion-count second moment) is a viable parallel target if
   Opening A's induction stalls — the quantity to bound is small and
   concrete (empirically ≤4 in every tested channel) which may make a direct
   combinatorial argument (not requiring Mertens/Borel–Cantelli machinery)
   more tractable than prior rounds' abandoned density approaches.
