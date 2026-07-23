## imo-2026-06 — Round 14 outline review

### CRITICAL PROCESS FINDING (checked first, applies to all 4 approaches)

**None of this round's outline content was actually persisted to
`results/imo-2026-06/approaches/`.** Verified directly:
- `witness-chaining-universal-existence.md` does not exist on disk at all.
- `forced-primes-well-ordering.md`, `sunflower-inadmissibility-toolkit.md`,
  `intersecting-family-covering-construction.md` are **byte-identical to
  the round-13 committed version** (`git diff HEAD` shows zero change;
  `diff` against `git show HEAD:...` is empty for all three). `git status`
  confirms only `.ranking.json` is modified in the whole `results/`
  tree.

This is the exact failure mode this workspace's own outline-reviewer
memory already warns about (round 1: "NEVER assume approach files exist
just because the outliner's report describes them in detail"). All of
the round-14 skeleton content (Corollary MSF, the 6-channel closure
skeleton, the 2747/4087 singleton-chain skeleton, the minimality-tool
skeleton) exists **only** in `/tmp/round-14/proof-outliner.md`. Builders
must be pointed there explicitly and told to seed/append their own
`results/imo-2026-06/approaches/<slug>.md` files themselves — do not
assume the outline is already in the approach files.

Given this, my review below is of the **mathematical content of the
outline as reported** (independently re-derived from scratch where
possible, not just read), since that is the only content that exists
to review pre-build.

---

### 1. `forced-primes-well-ordering` — a_1=4199 six-channel closure

**Independently re-verified from scratch, not just re-read.** Fresh
`sympy.factorint` brute-force generation of `a_1=4199` reproduces all 7
cited witnesses exactly: `a_2=4212=2^2·3^4·13`, `a_5=4233=3·17·83`,
`a_9=4316=2^2·13·83`, `a_11=4332=2^2·3·19^2`, `a_12=4352=2^8·17`,
`a_82=5746=2·13^2·17`, `a_92=5967=3^3·13·17` — exact match on value,
factorization, core, and companion set.

I then independently re-derived (not copied) the per-class disjunctive
facts directly from the already-certified Lemma WF's exact statement
(`lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`: witness
`i_0` with core `S'` forces `comp(a_k)∩comp(a_{i_0})≠∅` for **every**
`k∈I_S`, `S` disjoint from `S'`) and confirmed:
- `I_13`: unconditional `2` (from `a_12`, core `{17}`, disjoint), `(3∨83)` (from `a_5`).
- `I_17`: `(2∨3)` (from `a_2`, core `{13}`), `(2∨83)` (from `a_9`, core `{13}`).
- `I_19`: unconditional `2` (from `a_12`), unconditional `3` (from `a_92`, core `{13,17}`).
- `I_{13,19}`: unconditional `2`, `(3∨83)` (same witnesses as `I_13`, both core `{17}` disjoint from `{13,19}`).
- `I_{17,19}`: `(2∨3)`, `(2∨83)` (same witnesses as `I_17`, both core `{13}` disjoint from `{17,19}`).
- `I_{13,17}`: only `(2∨3)` (from `a_11`, core `{19}`, disjoint from `{13,17}`).

I then case-split all 6 channels by hand: **all 6 close**, 5 of them
needing the full `{2,3,83}` (identical 2-case Boolean split each time:
"if 2 divides the disjunctive side, done; else both `3,83` divide it,
matched by the other side's `(3∨83)`/`(3∨83)`-shaped fact"), and channel
`({19},{13,17})` closing on just `{2,3}` (since `I_19` has BOTH `2,3`
unconditionally, it automatically intersects `I_{13,17}`'s `(2∨3)`
regardless of which disjunct holds) — **exactly matching the outline's
claim, independently confirmed, not just trusted.**

**The specific "witness-scoping issue" (item 1 of the dispatch).**
Verified directly: `a_2,a_9` have core `{13}`. Core `{13}` is NOT
disjoint from `{13,17}` (shares `13`), so they cannot license a
Lemma-WF application against target class `I_{13,17}` — I checked the
outline's actual channel-5/6 constructions and confirmed `a_2,a_9` are
used ONLY for `I_17` and `I_{17,19}` (both have core `{13}` disjoint from
the target), never for `I_{13,17}` or `I_{13,19}`\`s complement — the fix
is applied correctly everywhere in the skeleton, not just claimed fixed.
Channel enumeration (7 nonempty subsets of a 3-set, 6 disjoint unordered
pairs) is exhaustive — verified by hand.

**Verdict: mathematically sound as scoped, no gap found in the outline
logic.** The only real risk is transcription (writing out all 6 case
splits explicitly, not skipping any) — flagged correctly by the outline
itself as remaining bookkeeping, not a logic gap.

### 2. `sunflower-inadmissibility-toolkit` — a_1=2747 (W={2,3,7}), a_1=4087 (W={2})

**Independently re-verified from scratch.** Fresh brute-force generation
confirms all 6 cited witnesses exactly: `2747`: `a_3=2814=2·3·7·67`
(core `{67}`, comp `{2,3,7}`), `a_13=3321=3^4·41` (comp `{3}`),
`a_14=3362=2·41^2` (comp `{2}`), `a_163=11767=7·41^2` (comp `{7}`);
`4087`: `a_5=4288=2^6·67` (comp `{2}`), `a_54=7442=2·61^2` (comp `{2}`).

Re-derived the logic from Lemma WF directly (not trusting the outline's
prose): three independent singleton-comp witnesses of core `{41}`
(`a_13,a_14,a_163`) each force class `I_{67}` to be divisible by `3`,
`2`, `7` respectively — so **every** member of `I_{67}` is divisible by
all of `2,3,7` simultaneously (a strong but logically valid consequence
of applying Lemma WF three times to the same target class). Symmetric
witness `a_3` (comp `{2,3,7}`, core `{67}`) forces `I_{41}` to intersect
`{2,3,7}`. Since `I_{67}` has all three unconditionally, whichever of
`2,3,7` divides an `I_{41}` member also divides the `I_{67}` partner —
`W={2,3,7}` covers the pair. Same argument gives `W={2}` for `4087`
(both singleton witnesses `2`, on both sides).

**I additionally ran a numerical sanity check the outline itself does
not report** (per my own standing rule to test one claim per approach
on fresh data): generated both sequences to `N=20{,}000` with the
workspace's certified antichain generator and checked every `I_67`/`I_41`
member (`2747`) and every `I_67`/`I_61` member (`4087`) against the
claimed unconditional divisibility. **Zero violations**: `2747` — 389
`I_67` members all divisible by `{2,3,7}`, 19203 `I_41` members all hit
`{2,3,7}`; `4087` — 9375 `I_67` and 10312 `I_61` members all divisible
by `2`. Confirms the logic is not just valid in principle but matches
the real sequence.

**Verdict: mathematically sound, essentially a sure thing given
already-certified Lemma WF.** No gap found.

### 3. `witness-chaining-universal-existence` (new slug, branch of `sunflower-bundle-closure`)

**Step 1 (Corollary MSF)** is a correct, low-risk formalization —
literally what I independently re-derived and used above for both
sibling approaches (multiple singleton Lemma-WF applications combine by
plain conjunction/disjunction). Sound.

**Step 3-4 check against `theorem-UBS-false-case-II.md` (item 3 of the
dispatch) — independently re-verified, the outliner's claim holds up.**
Read the certified theorem's literal statement:
`sup_{n∉I_{P_1}} ω(a_n) = ∞` (Case II, always) — a statement about the
**supremum** being infinite (unboundedly large companion sets occur
somewhere off the top core). The proposed **Small-Companion Existence
Lemma** asks whether a *specific* infinite class `I_S` contains
*infinitely many* members with `|comp(a_k)|≤2` — a statement about
recurring **small** values, logically independent of the sup being
infinite (a class can have both arbitrarily large and infinitely many
small values, or the sup could live entirely in a different class from
the one being asked about). Confirmed: **not already refuted**, the two
propositions genuinely don't touch.

**However, I found evidence the outliner did not check that pushes
against this lemma being true, and it should be flagged as a caution,
not treated as a safe fallback target.** I ran a direct numerical test
on the workspace's own standing "hardest case" (`a_1=21528751`,
per this workspace's Rule on always testing the hardest case, not just
the outline's own examples) to `N=8000`: the singleton class `S={197}`
has 136 members, of which **zero** have `|comp|≤2` (sizes at the tail:
`4,5,4,4,4,4,5,4,5,4` — no downward trend at all). This is a real,
concrete counter-signal (not a proof of falsity, but the opposite of
"strong numerical support") for exactly the class this workspace has
repeatedly found to be its hardest recurring obstruction (`S={103,197}`
nesting, rounds 6-11). The outline's own instruction ("check density of
`|comp|≤2` members across several classes at large N... before investing
further analytic effort") is right — but the builder should be told
this specific check has already turned up a bad sign, so if the builder's
own broader sweep confirms it, they should not spend the round chasing a
likely-false lemma; report the counterexample and move on.

**Verdict: honestly scoped, no overclaim, Step 1 sound and cheap;
Step 3-4 legitimately open but flag the negative numerical signal above
so the builder doesn't over-invest in an analytic proof of something
that may simply be false for this class.**

### 4. `intersecting-family-covering-construction` — minimality mechanism (advance)

Purely exploratory this round (Proposition BI's redirection toward
minimality, not feasibility). No new lemma is claimed yet — nothing to
independently verify beyond confirming Lemma WO / Proposition BI remain
correctly cited (already certified, unchanged). Sound as scoped; genuine
open territory, appropriately labeled low-certainty.

### Diversity check (item 4 of the dispatch)

**Real concern, not fully offset.** 3 of the 4 candidates
(`forced-primes-well-ordering`, `sunflower-inadmissibility-toolkit`,
`witness-chaining-universal-existence`) all rest on the **identical**
certified mechanism (Lemma WF / Corollary MSF), differing only in which
instance or generality they apply it to. This is weaker diversity than
it looks: two of the three (`forced-primes-well-ordering`,
`sunflower-inadmissibility-toolkit`) are pure instantiation work with no
independent mathematical idea between them — if a future round finds
Lemma WF's mechanism fundamentally can't reach the *general* `a_1` case
(a real risk `witness-chaining-universal-existence` itself flags), all
three die together. `intersecting-family-covering-construction` is
confirmed structurally independent (density/pigeonhole on the coarse
core sequence, no witness-chaining, no Lemma WF citation anywhere in its
Step 2-4) — the outliner's diversity claim for this one approach is
correct.

This round's concentration is acceptable as a one-time "harvest the
newly-certified tool" round (Lemma WF was only certified last round and
these are genuinely fast, high-confidence wins worth taking), but **flag
for the orchestrator**: if `witness-chaining-universal-existence`'s
general WCE attempt also stalls next round, do not open a 3rd or 4th
sibling that merely re-instantiates Lemma WF on more concrete `a_1`
values — that would be the single-gap trap in a new guise. The next
genuinely-new-framing approach, if needed, should not be
`intersecting-family-covering-construction` again either (2 rounds
without traction on minimality) — it should be a fresh top-level idea.

### Registration / ranking actions taken

- `witness-chaining-universal-existence` did not exist in the ranker —
  registered via `copy_approach` (source `sunflower-bundle-closure`,
  inherits its Elo/counts per the tool's semantics — legitimate branch,
  not a fresh cold-start, since it inherits the exact proven prefix
  `WCE⟹JW`/Chaining Sufficiency Theorem).
- `forced-primes-well-ordering`, `sunflower-inadmissibility-toolkit`,
  `intersecting-family-covering-construction` already registered
  (advance/revise of existing slugs) — no re-registration needed.
- Ranked the field (comparisons below), clearing `stale` on all touched
  entries.

### Verdicts

- `forced-primes-well-ordering` — **APPROVE**. Content independently
  re-derived and confirmed sound; only remaining work is the explicit
  write-up (bookkeeping, not logic).
- `sunflower-inadmissibility-toolkit` — **APPROVE**. Same standing;
  independently confirmed sound and numerically verified to N=20,000.
- `witness-chaining-universal-existence` — **APPROVE with a flagged
  caution**: build Step 1 (Corollary MSF) as a sure thing; treat Step
  3-4 (Small-Companion Existence Lemma) as genuinely open and possibly
  FALSE per the negative signal found above — the builder must not
  present a stalled or refuted Step 4 as anything but an honest gap or
  refutation, consistent with this workspace's standing anti-overclaim
  rule.
- `intersecting-family-covering-construction` — **APPROVE**. Exploratory
  but legitimately scoped, no flaw found, preserves population diversity.

No RETHINK. All 4 approaches are mathematically sound as outlined; the
only defect found is the process gap (outline not persisted to disk),
which builders must route around by reading
`/tmp/round-14/proof-outliner.md` directly and seeding their own
approach files (including creating
`results/imo-2026-06/approaches/witness-chaining-universal-existence.md`
from scratch, starting from `sunflower-bundle-closure.md`'s content per
the outline's own instructions, since no such file exists yet).

### Ranking

Comparisons submitted this round (anchored to round-13's recorded
outcomes — all touched approaches were "advanced" last round; no
`dead-end` siblings in this comparison set):
- `intersecting-family-covering-construction` beats
  `witness-chaining-universal-existence` (more established, holds the
  master conditional theorem, and is the confirmed structurally
  independent one — diversity value plus higher historical Elo).
- `forced-primes-well-ordering` beats `witness-chaining-universal-existence`
  (this round's concrete, independently-verified-sound closure work vs.
  a step whose hard sub-target I found active negative evidence
  against).
- `sunflower-inadmissibility-toolkit` beats
  `witness-chaining-universal-existence` (same reasoning).
- `forced-primes-well-ordering` vs `intersecting-family-covering-construction`
  — draw (both top-tier, both real independently-confirmed progress,
  no basis to separate them this round).
- `sunflower-inadmissibility-toolkit` vs `forced-primes-well-ordering` —
  draw (both concrete instance-closures via the identical mechanism,
  equally strong this round).
- `intersecting-family-covering-construction` beats
  `sunflower-inadmissibility-toolkit` (higher established Elo/more
  mature master-theorem holder; marginal only).

build set: forced-primes-well-ordering, sunflower-inadmissibility-toolkit, witness-chaining-universal-existence, intersecting-family-covering-construction
