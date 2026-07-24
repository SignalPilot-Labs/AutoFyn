## Status
partial

## Approaches tried
- **round 19 (advance, numeric hardening only)** — Per dispatch, folded in
  this round's H2-subfamily explorer's two new adversarial-seed results,
  both cross-checked by the explorer against a naive brute-force `gcd`
  generator before being trusted, and both following the now-familiar
  "apparent single-occurrence type resolves once the window is extended"
  pattern: (i) `a_1 = 510510 = 2·3·5·7·11·13·17` (`|Q|=7`, the **largest**
  seed tested to date across all rounds) — at window 60,000, three
  single-occurrence types were flagged (the trivial `τ(1)=Q`, plus two
  genuine candidates `{2,3,5,11,13,17}` first at `n=36466` and
  `{2,3,7,11,13,17}` first at `n=51052`); extending to window 200,000, both
  candidates recur, leaving zero surviving exceptions; (ii) `a_1 = 209370 =
  2·3·5·7·997` (a deliberately **skewed** seed — one huge prime paired with
  four small ones, a structurally different shape from every previously
  tested seed, which were either roughly-balanced primorial-type products or
  prime powers) — at window 60,000 a genuine single `{2,3,5,7,997}` appeared
  at `n=34896`; extending to window 300,000, it recurs, and even the trivial
  full-`Q` type `τ(1)` itself (which had not yet recurred at the smaller
  window) recurs by this larger window, leaving zero singles of any kind.
  Both data points are recorded below (§4, new subsection) with full
  methodology, exactly as reported by the explorer, and are explicitly
  flagged as evidence only — no proof route is claimed or implied. No new
  proof mechanism was attempted this round (per dispatch: the
  counting/pigeonhole corridor remains confirmed-exhausted, §6, and is not
  re-probed). Also recorded, per dispatch, the round-19 H2-subfamily
  explorer's separate finding that **NTBT is sufficient but not necessary**
  for H2: the Master Conditional Theorem's H2 hypothesis only actually
  requires *some* self-absorbing core `S*` to exist (however large), of
  which `S*=Q` (NTBT) is the cleanest special case, not the only sufficient
  one. This weaker existence-only target is a logically distinct question
  from NTBT (NTBT ⟹ the weaker target trivially via §2's Lemma, but not
  conversely — a seed could conceivably fail NTBT, i.e. have some transient
  base type at `S_0=Q`, while the absorption chain still terminates at a
  strictly larger `S*`) and is being separately attacked this round by the
  sibling `core-growth-monotonicity` slug (its own dispatch mandate); this
  approach file does not duplicate that attempt and records only the
  logical relationship for cross-reference. Verdict (self-assessed): honest,
  purely additive numeric record-keeping plus one cross-reference
  clarification; no new proof content; NTBT (and its sufficient-but-not-
  necessary status relative to H2) remains exactly as open as after round
  18; Status stays `partial`.
- **round 18 (revise, record correction)** — Per dispatch, corrected the
  round-17-flagged "genuine, currently-unresolved candidate exception"
  language for `a_1=255255`, type `{5,7,11,13,17}` (first occurrence
  `n=27184`, previously unconfirmed to recur through window 65000). The
  round-18 H2/NTBT explorer extended the exact brute-force greedy simulation
  to 500,000 terms and found the type recurs at `n=135914` (a runway of
  108,730 terms past the first occurrence — nearly 4× the 65,000-term window
  that had left it unresolved, exactly the same window-artifact shape already
  seen and resolved for `a_1=30030,15015`). This was confirmed **twice**,
  independently: once by the explorer's own bitmask-per-prime simulation
  (cross-checked byte-for-byte against a naive `gcd`-based reimplementation
  on small `n`), and again independently by this round's outline-reviewer,
  who reran a from-scratch, differently-implemented simulation out to
  `n=140000` and reproduced the *exact same* occurrence list `n=27184,
  135914` for the same type. Two independent scripts, exact match — this is
  not a re-trust of a single number, it is a genuinely cross-validated
  computational fact. Consequently: the round-17 "one open candidate
  exception" is RESOLVED in NTBT's favor, and **zero open numeric
  counterexamples to NTBT remain** across the ~50+ seeds tested across
  rounds 17–18 (in fact, at the 500,000-term window, every one of the 63
  distinct observed types for `a_1=255255` has recurred at least 6 times,
  including the full-`Q` type itself, which recurs exactly periodically at
  gap 81548 — the strongest and cleanest recurrence evidence for any tested
  seed to date). This is a bookkeeping/record-correction round only: it does
  NOT constitute or claim a proof of NTBT — see §3/§4 below, updated
  accordingly, and the explicit caution restated in §5. Separately, this
  round's H2 explorer completed a systematic audit of the H2
  "counting/pigeonhole" corridor (bounding total self-absorption rounds, or
  `|S_∞|`, or `|𝒫'(S_k)|`, via `|𝒫'(S)|`-type combinatorial bounds) and found
  all three sub-routes tried collapse to already-known dead ends (see new §6
  below) — recorded here as a permanent negative finding so future rounds do
  not re-probe this specific corridor without a genuinely new idea. No new
  proof route for NTBT itself was found or attempted this round. Verdict
  (self-assessed): honest record correction plus one new permanent negative
  finding; NTBT remains open, Status stays `partial`.
- **round 17 (new, this build)** — Per dispatch, investigated FIRST (before building
  any enlarged `S_0'`) whether `S_0 = Q` itself is already self-absorbing in
  general, i.e. whether `N(Q) = 0` (equivalently `N(Q) ≤ 1`, see below) for every
  `a_1`. Proved one new unconditional lemma in full (the **Vacuous/Weak
  Self-Absorption Lemma**, below — reusable, no open hypothesis), then ran an
  extensive numerical investigation of the underlying question `N(Q) = 0`,
  explicitly designed to catch the round-16-diagnosed "window artifact" failure
  mode (a proxy that looks stabilized only because the sampling window is too
  short). Found and *resolved* three apparent counterexamples (`a_1 = 30030,
  15015, 255255`, all with `|Q| ∈ {5,6}`) that at first looked like genuine
  transient (non-recurring) base types, but which resolved to `N(Q) = 0` once
  the simulation window was extended far enough to see the true, long
  recurrence period of the rare type in question. No genuine counterexample was
  found in any of ~50 seeds tested across a wide range of `|Q|` (1 to 6) and
  structures (prime, prime-power, squarefree, non-squarefree). However, **no
  general proof was found or is claimed** — this is reported honestly as a
  strongly-supported but open conjecture (named **NTBT** below), not a theorem.
  This is real, permanent, honestly-scoped progress: it identifies and sharply
  states a new open sub-question, distinct in content from the 18 confirmed-dead
  FAH mechanisms and from H1 itself, and shows precisely what a proof of it would
  buy (H2 fully resolved with the *minimal possible* core `S* = Q`, collapsing
  the Master Conditional Theorem's remaining content to bare FAH at `Q` — no
  enlargement of the core needed at all). Verdict (self-assessed): genuine
  partial progress on H2; the central open question (NTBT) is not resolved.

## Current best

### 1. Setup (recalled, unconditional)

Fix the sequence `(a_n)` with `a_1 > 1`. Let `Q := P(a_1)` (the prime factors of
`a_1`, a nonempty finite set — Q is what the workspace calls the "base" prime
set). For `n ≥ 1` write `τ(n) := P(a_n) ∩ Q`, the **base type** of index `n`. By
the certified **Free Facts Lemma** (`lemmas/free-facts-gcd.md`), `gcd(a_i,a_j) >
1` for all `i ≠ j`; in particular `gcd(a_n,a_1) > 1` for `n ≥ 2`, so `τ(n) ≠ ∅`
for every `n ≥ 1` (and `τ(1) = P(a_1) ∩ Q = Q` since `Q := P(a_1)`).

By the certified **Persistent-Type Pigeonhole** (`lemmas/persistent-type-
pigeonhole.md`), there is a finite, nonempty set `𝒫(Q) ⊆ 2^Q \ {∅}` of
*persistent* types (types occurring at infinitely many indices), and a
threshold
```
N(Q) := max{ n : τ(n) ∉ 𝒫(Q) }     (0 if this set is empty)
```
— the largest index whose base type is NOT one of the persistent types (an
"exceptional" index). `N(Q)` is exactly the quantity written `N(S)` in
`lemmas/self-absorbing-core-theorem.md` and `lemmas/termination-criterion-
lemma.md`, instantiated at `S = Q` (the starting point `S_0` of the absorption
chain, per the Finite Core Theorem's convention `S_0 ⊇ Q`; here we take the
literal minimal choice `S_0 = Q`).

Recall the **absorption operator** from `lemmas/self-absorbing-core-theorem.md`:
for finite `S ⊇ Q`,
```
S⁺ := S ∪ ⋃_{j=1}^{N(S)} P(a_j),
```
and `S` is called **self-absorbing** if `S⁺ = S`.

### 2. Vacuous / Weak Self-Absorption Lemma (proved, unconditional)

**Lemma.** If `N(Q) ≤ 1`, then `S_0 := Q` is self-absorbing (`Q⁺ = Q`), and
hence the absorption chain terminates in **zero** rounds with `S* = Q` — in
particular the Termination Criterion Lemma's hypothesis (boundedness of
`N(S_k)`) holds trivially in this case, since the chain is already constant
(`S_k = Q` for all `k ≥ 0`).

**Proof.** Two cases, both fully covered (`N(Q) ≤ 1` means `N(Q) = 0` or
`N(Q) = 1`; these are the only two possibilities and are mutually exclusive by
definition of `N(Q)` as a specific nonnegative integer).

- **Case `N(Q) = 0`.** The union `⋃_{j=1}^{0} P(a_j)` ranges over the index set
  `{j : 1 ≤ j ≤ 0}`, which is empty (there is no integer `j` with `1 ≤ j ≤ 0`).
  An empty union of sets is `∅`. Hence `Q⁺ = Q ∪ ∅ = Q`. So `Q` is self-absorbing
  — **vacuously**, i.e. the self-absorption *condition* "`P(a_j) ⊆ Q` for every
  `j = 1,...,N(Q)`" is true because it quantifies over an empty range, not
  because any nontrivial containment was checked.

- **Case `N(Q) = 1`.** The union ranges over `j = 1` only: `⋃_{j=1}^{1} P(a_j) =
  P(a_1)`. But `P(a_1) = Q` by the very definition of `Q`. Hence `Q⁺ = Q ∪ P(a_1)
  = Q ∪ Q = Q`. So `Q` is self-absorbing again — this time **automatically**
  (not vacuously: the range `j=1,...,1` is nonempty, but the single required
  containment `P(a_1) ⊆ Q` holds by definition, with no work needed).

In both cases `Q⁺ = Q`, i.e. `S_0 = Q` is self-absorbing, so the absorption
chain `S_0 ⊆ S_1 ⊆ ...` (defined by `S_{k+1} := S_k⁺`) satisfies `S_1 = S_0⁺ =
S_0`, hence `S_k = Q` for every `k ≥ 0` by induction: it terminates at `k = 0`
with terminal core `S* = Q`, and `N(S*) = N(Q) ≤ 1`. ∎

**Remark (why this is the right question to ask first, confirming the
outline-reviewer's guidance).** This lemma shows the reviewer's suggested
simplification is not just a shortcut but the *sharp* first question: checking
"`N(Q) ≤ 1`?" is both necessary in the easy direction (if it holds, we are done
with zero absorption rounds and the *smallest possible* terminal core `S* = Q`)
and strictly weaker than building any enlarged `S_0'` — the outline's
`S_0' := S ∪ Q ∪ ⋃_{j≤M} P(a_j)` construction is only needed as a fallback if
`N(Q) ≥ 2` for some `a_1` (an exceptional index `j ≥ 2` whose own factorization
is not contained in `Q`, e.g. an early term with a genuinely new prime, forces
enlargement). We did not encounter this case on any tested seed (see below), so
the enlarged construction was not needed to be built or tested this round —
honestly disclosed as *unattempted*, not as *ruled out*.

### 3. The remaining open question: NTBT (No-Transient-Base-Type)

By the Lemma above, H2 (chain termination) is **completely resolved with the
minimal core `S* = Q`** provided:

> **NTBT Conjecture.** For every positive integer `a_1 > 1`, `N(Q) ≤ 1` — i.e.
> every nonempty subset `A ⊆ Q` that occurs as `τ(n)` for *some* index `n ≥ 2`
> occurs for *infinitely many* indices (no base type is genuinely transient:
> occurring a positive but finite number of times).

(`N(Q) ≤ 1` is literally equivalent to: the only index whose base type could
fail to be persistent is `n=1` itself, and even that failure is harmless by the
Lemma's Case `N(Q)=1` — so the substantive content of NTBT is really "every
`τ(n)` for `n ≥ 2` that occurs at all is persistent.")

**This is honestly NOT proved.** We did not find a proof, and record here
exactly what was tried and why it did not close the gap, per the "no
hand-waving" rule.

- *Attempted proof route 1 (density/recurrence forcing).* We looked for a
  direct forcing argument — e.g. via the certified **Sandwich Genericity
  Theorem** (`lemmas/sandwich-genericity-theorem.md`, `n-m ≤ a_n-a_m ≤
  (n-m)·a_1`) or the **Bounded Gap Lemma** (`lemmas/bounded-gap-lemma.md`) —
  that would force any base type occurring once to occur again. These lemmas
  are, by the Sandwich Genericity Theorem's own certified scope note, provably
  **class-blind**: both bounds are the identical formula for every pair of
  indices regardless of `τ(m), τ(n)`, so no argument built only from them can
  distinguish "this specific subset of `Q` recurs" from "it doesn't" — they
  carry zero divisor-class-discriminating information. This route is a dead
  end for the same reason it was already dead for FAH mechanisms 9–16 (the
  recurrence's defining rule, `gcd(c,a_i)>1`, is a Boolean predicate blind to
  *which* prime realizes the shared factor — `lemmas/density-argument-
  vacuity-corollary.md`).
- *Attempted proof route 2 (reduction to FAH).* We checked whether NTBT is
  secretly equivalent to, or a restatement of, standard FAH. It is not,
  logically: FAH (as used throughout this workspace, e.g.
  `lemmas/self-absorbing-core-theorem.md`'s hypothesis) asks whether two
  *different*, already-established-as-persistent types intersect as sets;
  NTBT asks whether a type that occurs at all is persistent (an existence/
  recurrence question about a single type, prior to and independent of any
  intersection question about two types). Neither the builder nor any cited
  certified lemma supplies a reduction in either direction. This matches, and
  extends to a new instance, the round-15-certified finding
  (`lemmas/termination-criterion-lemma.md`) that H2-native quantities are
  logically distinct objects from FAH's own content — analogous in
  non-constructivity shape, not equivalent.
- *No counterexample found either*, despite a substantial and methodologically
  careful numeric search (below). NTBT is left as a precisely-stated, open
  conjecture — genuinely new content, not a restatement of prior dead
  mechanisms, and not overclaimed as proved.

### 4. Numerical investigation (evidence, not proof — reported with full
methodology per the "no hand-waving" rule)

**Method.** For a given `a_1`, generate the greedy sequence by trial division
(`a_{n+1}` := smallest integer `> a_n` with `gcd(a_{n+1}, a_i) > 1` for all `i ≤
n`, checked directly against every earlier term — an exact, brute-force
computation of the actual sequence, not an approximation) up to length `L`,
compute `τ(n) := P(a_n) ∩ Q` for each `n`, and classify a type as
"tail-persistent" if it occurs at least once in the second half of the window
(`n > L/2`); an index `n` is flagged exceptional if `τ(n)` is not
tail-persistent. This proxy is the same one used (and independently
re-verified) by the round-17 outline-reviewer, and it is well known (flagged
explicitly in round 16) to have a **false-positive failure mode**: a type that
recurs only very rarely (period comparable to or larger than the window) can
be misclassified as non-persistent purely because the window did not run long
enough to see its next occurrence — this is not a data bug but a fundamental
limitation of finite-window sampling of an infinite recurrence, so every
positive finding below was cross-checked by re-running at (much) longer
windows before being trusted.

**Round 1 (broad sweep, |Q| ≤ 4, window 4000–8000).** Seeds `175, 4807, 11305,
15, 35, 105, 210, 1155, 693, 385, 5005` and a further sweep of ~35 seeds with
`|Q| = 2,3,4` (varied structure: prime, prime-power, squarefree,
non-squarefree, e.g. `6, 36, 108, 216, 4, 8, 16, 32, 49, 25, 121, 9, 27, 81,
90, 175, 539, 225, 143, 2431, 4199`) — **zero exceptions found** at these
window sizes; `N(Q) = 0` (hence `≤ 1`) in every case.

**Round 2 (larger |Q|, |Q| = 5, 6 — apparent counterexamples found, then
resolved).** Three seeds initially showed nonzero exceptions:
- `a_1 = 30030 = 2·3·5·7·11·13` (`|Q|=6`): window 4000/8000 showed a single
  exceptional index `n=1` (the type `Q` itself, i.e. `τ(1)`, appeared
  non-recurring). Extending the window to 16000, 30000: the exception
  *vanished* (`N(Q)=0`); a direct check of the occurrence list of the full-`Q`
  type up to window 60000 found it recurring exactly periodically at indices
  `1, 15016, 30031, 45046` (constant gap `15015`), confirming the type is
  genuinely persistent with a long period — the earlier "exception" at
  windows ≤ 8000 was a pure window artifact (the type's second occurrence,
  index 15016, is simply past those windows).
- `a_1 = 15015 = 3·5·7·11·13` (`|Q|=5`): window 4000 showed exceptions at
  `n = 1, 1544`; window 8000 and beyond showed **zero** exceptions (`N(Q)=0`);
  a direct occurrence check of the full-`Q` type up to window 30000 found it
  recurring at `1, 4629, 9257, 13885, 18513, 23141, 27769` (gap `≈4628`,
  constant) — again a resolved window artifact.
- `a_1 = 255255 = 3·5·7·11·13·17` (`|Q|=6`): window 5000/10000/15000 all
  showed 5–7 exceptions, including several persisting across window sizes —
  the least clear-cut case encountered. Direct per-type occurrence analysis
  (window 15000) showed every flagged "exceptional" type *except one* recurs
  sparsely but genuinely (e.g. type `{3,5,7,11,17}` recurs at `6274, 18820,
  31366` — gap exactly `12546` twice — and type `{3,5,7,13,17}` at `7414,
  22242, 37069`, gap `≈14827` twice), consistent with true low-frequency
  persistence rather than transience; extending the window to 40000 confirmed
  a **second occurrence** for every one of these five previously-single-
  occurrence types (`{5,11,13,17}` at `3884, 19417`; `{7,11,13,17}` at `5438,
  38057`; `{3,5,11,13,17}` at `11652, 34951`; plus the two already-recurring
  types above). At window 40000, a further, then-unflagged single-occurrence
  type was found by round 17's outline-review (`{5,7,11,13,17}` at `n=27184`,
  no second occurrence through window 65000) — this was the round-17
  "genuine, currently-unresolved candidate exception," honestly left open at
  the time.

  **Round-18 update (this round; record correction).** The round-18 H2/NTBT
  explorer extended the exact brute-force greedy simulation for this seed to
  500,000 terms (cross-checked against a naive `gcd`-based reimplementation
  on small `n` before trusting it at scale) and found `{5,7,11,13,17}`
  **does recur**, at `n=135914` — full occurrence list through `n=500000`:
  `27184, 135914, 190280, 299010, 353376, 462106`. This was independently
  reconfirmed by the round-18 outline-reviewer using a second, differently
  implemented simulation (a per-prime bitmask method) out to `n=140000`,
  reproducing the identical pair `27184, 135914` exactly. Two independent
  scripts, exact match — the candidate exception is resolved, not merely
  re-asserted. At the 500,000-term window, **every one of the 63 distinct
  observed types for this seed has recurred at least 6 times**, including the
  full-`Q` type `τ(1)={3,5,7,11,13,17}` itself, which recurs exactly
  periodically at `n = 1, 81549, 163097, 244645, 326193, 407741, 489289`
  (constant gap `81548`) — so even the weaker fallback argument via the
  Lemma's Case `N(Q)=1` (which would have sufficed regardless) is now moot:
  this seed is fully consistent with `N(Q)=0` outright, the strongest
  possible outcome, confirmed to a greater depth than any other tested seed.

**Round 3 (round 19: largest seed and skewed-shape seed, both resolved).**
Two new adversarial seeds, chosen specifically to probe shapes not yet
tested (largest `|Q|`, and a skewed prime-size distribution), run by this
round's H2-subfamily explorer using a fast bitmask-per-prime simulator
(cross-checked against the naive brute-force `gcd` generator on small `n`
before being trusted at scale, matching the methodology standard set in
round 18):

- `a_1 = 510510 = 2·3·5·7·11·13·17` (`|Q|=7`, the **largest seed tested to
  date** in this workspace across all 19 rounds). At window 60,000, three
  single-occurrence types were flagged: the trivial `τ(1)=Q`, and two
  genuine candidates, `{2,3,5,11,13,17}` (first occurrence `n=36466`) and
  `{2,3,7,11,13,17}` (first occurrence `n=51052`). Extending the window to
  200,000: **both candidates recur** (no longer singles) — another resolved
  window artifact, exactly the round-17/18 pattern, now confirmed on a
  `|Q|=7` seed, one prime larger than the previous largest tested (`|Q|=6`,
  `a_1=255255,30030`). Zero surviving exceptions at window 200,000.
- `a_1 = 209370 = 2·3·5·7·997` (a deliberately **skewed** seed: one huge
  prime, `997`, paired with four small primes — structurally different from
  every previously tested seed, which were either roughly-balanced
  primorial-type products or pure prime powers). At window 60,000 a genuine
  candidate single `{2,3,5,7,997}` appeared at `n=34896` (besides the
  trivial `τ(1)=Q` at `n=1`, also unresolved at this window). Extending the
  window to 300,000: `{2,3,5,7,997}` **recurs**, and — notably — even the
  trivial full-`Q` type `τ(1)` itself **recurs** by this window (it had not
  yet recurred at window 60,000), leaving **zero** singles of any kind
  surviving. This is evidence (not proof) that skewing the seed's prime
  factorization toward one very large prime paired with several small ones
  does not, on this data point, produce a genuine NTBT counterexample
  either — a structurally different failure mode than "many
  similarly-sized primes" (the primorial-type seeds) was tested and also
  resolved.

No genuine (non-resolving) counterexample was found in either new seed.
This strengthens, but — exactly as with every prior round's numeric
finding — does **not** change the proof status of NTBT: it remains an open
conjecture, and this is explicitly a data point, not a step toward a proof.

**Conclusion of the numeric investigation (round 19: updated again).** Across
every one of the ~50+ seeds tested through round 18, and now including the two
round-19 adversarial seeds (largest `|Q|=7` tested to date; a skewed
one-huge-prime shape not previously tried), `N(Q) ≤ 1` held, and — with the
sole historical exception of the transient windows already discussed above —
`N(Q) = 0` outright holds on **every** tested seed with no remaining
ambiguity. **Zero open numeric counterexamples to NTBT (or even to the weaker
`N(Q) ≤ 1`) remain anywhere in the workspace's tested seed set, across ~52
seeds spanning `|Q|=1` to `7`, prime, prime-power, squarefree,
non-squarefree, roughly-balanced-primorial, and skewed-one-large-prime
shapes.** This is real, if non-rigorous, support for the conjecture — and it
continues to reinforce, on two more independent data points, that the
round-16-flagged window-artifact failure mode is a genuine and recurring
hazard: **every single one** of the five "apparent counterexamples" found
across rounds 17–19 (`a_1=30030,15015,255255` twice, `510510`, `209370`) has,
without exception, resolved into a genuine (if slow) recurrence once the
simulation window was pushed to roughly 3–5× the window at which it first
looked transient. This pattern is now stated explicitly, as a standing
methodological rule for future rounds (per the dispatch's own instruction):
**never trust an "`N(S)=0` on seed X" or "type T is non-recurring" claim from
a single finite window without re-running at 3–5× that window and, where
practicable, independently re-implementing the simulator**; every reported
positive finding in this file has followed that discipline, and every case
where it was skipped (the round-17 `a_1=255255` initial miss) was later
caught and corrected precisely because a later round applied the discipline.
**This strengthened numeric record is still evidence, not a proof** — see §3
and §5, which are unchanged in their honest "NOT established" verdict on NTBT
itself; five-for-five window-artifact resolutions, however uniform, is
inductive evidence over finitely many seeds, not a proof over all `a_1`, and
must not be read as approaching one.

### 5. What this does and does not establish

- **Cross-reference (round 19, logical clarification, not new proof
  content):** NTBT is **sufficient but not necessary** for H2. The Master
  Conditional Theorem's H2 hypothesis is exactly "the absorption chain
  `S_0 ⊆ S_1 ⊆ ...` terminates" (equivalently, by the certified Termination
  Criterion Lemma, that `(N(S_k))` is bounded) for *some* terminal core
  `S*`, taken at `S_0 = Q`. NTBT, as stated in §3, is the strictly stronger
  claim `N(S_0) = N(Q) ≤ 1`, i.e. the chain terminates **immediately, in
  zero rounds, at the smallest possible core**. If NTBT holds, H2 holds
  (trivially, via §2's Lemma). But the converse direction is not claimed
  and not established anywhere in this file: it is logically possible for
  some `a_1` to have `N(Q) ≥ 2` (violating NTBT) while the chain still
  terminates after one or more rounds at a strictly larger `S* ⊋ Q` — a
  weaker existence-only target ("some self-absorbing `S*` exists, however
  large") that would equally suffice for H2 without requiring `S*=Q`. This
  weaker target is a genuinely distinct open question from NTBT, is **not**
  attacked in this file (this round's numeric work and lemma are entirely
  about `N(Q)` at the minimal core `S_0=Q` specifically), and is being
  separately attacked this round by the sibling `core-growth-monotonicity`
  approach, per this round's dispatch — recorded here only so the logical
  relationship between the two open targets is on record and future rounds
  do not conflate them.
- **Established (unconditional, proved in full):** the Vacuous/Weak
  Self-Absorption Lemma (§2) — `N(Q) ≤ 1 ⟹ S_0=Q` is self-absorbing, chain
  terminates at `k=0`, `S*=Q`.
- **Established (empirical, not a proof):** strong, artifact-checked numeric
  support for `N(Q) ≤ 1` (usually `=0`) across a wide range of seed structures
  and sizes. **As of round 18, this support is unqualified**: after resolving
  the last remaining candidate exception (`a_1=255255`, see §4), `N(Q) = 0`
  holds on every one of the ~50+ tested seeds with no outstanding ambiguity —
  zero open numeric counterexamples to NTBT remain in the workspace. This
  remains empirical evidence only, explicitly not proof-strength (see the
  next bullet and the CLAUDE.md rule against overclaiming); the phrase "zero
  counterexamples across 50+ seeds" must not be read as approaching a proof.
- **NOT established:** a general proof of `N(Q) ≤ 1` for every `a_1` (the NTBT
  conjecture) — this is the honest, precisely-stated open gap. Two proof
  routes were tried and shown to be dead ends (class-blindness of the only
  certified magnitude tools; no reduction to/from FAH found); no third route
  was found this round. **Round-18 status: the numeric evidence for NTBT is
  now stronger (zero open counterexamples, up from "one unresolved candidate"
  in round 17 — see §4 below), but this changes nothing about the proof
  status: NTBT is still a conjecture, not a theorem, and no new proof route
  was found or attempted this round.** In addition, round 18 established that
  the natural "counting/pigeonhole" corridor for the closely related H2
  termination question is exhausted (see new §6 below) — this is a negative
  finding about H2's own machinery, not a proof route for NTBT itself, but is
  recorded here since a proof of NTBT is the cleanest way this approach's
  own machinery could still close H2.
- **Consequence if NTBT is ever proved:** combined with the certified
  Termination Criterion Lemma and the Master Conditional Theorem
  (`n1-periodicity-reconciliation` §2), H2 would be *fully* and
  *unconditionally* resolved (not just "for this seed" — NTBT is stated for
  every `a_1`), with the *smallest possible* terminal core `S* = Q` (no
  enlargement needed at all, simplifying the Self-Absorbing Core Theorem's
  `G*`/`sig`/CRT construction to operate directly at level `Q`). The problem's
  entire remaining content would then be **exactly** standard FAH at `S*=Q` —
  i.e. literally the standing, 18-confirmed-dead-mechanisms crux, with no new
  H2-side conditions layered on top. This is a clean, sharp reduction, but it
  is conditional on NTBT, which remains open.
- **The outline's enlarged `S_0'` construction (fallback):** not built or
  tested this round. Given the strong evidence that `N(Q) ≤ 1` already holds
  on every tested seed, building the more complex `S_0'` was not necessary to
  make progress; it remains available as a documented fallback if a future
  round finds a genuine `a_1` with `N(Q) ≥ 2`, but its own open question (does
  enlarging the core manufacture a NEW, larger exceptional index — the
  round-16 Binary Refinement non-monotonicity risk) is correspondingly
  untouched and still fully open.

### 6. H2 "counting/pigeonhole" corridor — confirmed exhausted (round 18,
documented dead end, not a new attempt)

This section records, as a permanent negative finding (per the round-18 H2
explorer's Task 2, cited and not re-derived here), that the natural family of
attacks on H2 via bounding a *combinatorial count* — as opposed to bounding a
specific *index* like `N(S_k)` — is exhausted in all three forms tried. This
matters for this approach because it closes off the most natural "cheaper
than NTBT" fallback route to H2: if NTBT itself resists proof, one might hope
to sidestep it by bounding some other, more tractable combinatorial quantity
that still forces the absorption chain to terminate. All three concrete
attempts collapse:

- **(a) Bound total absorption rounds via `|𝒫'(S)|` resolved per round.**
  The Binary Refinement Lemma (`lemmas/binary-refinement-and-threshold-
  recursion.md`) gives `|𝒫'(S∪{p})| ≤ 2|𝒫'(S)|`, so `|𝒫'(S)| ≤ 2^{|S|}-1` is
  finite at every stage — but bounding the *number of rounds* by "each round
  permanently resolves a disjoint base-type pair, and pairs are bounded by
  `|𝒫'(S)|`" is, on inspection, **literally the same statement** as bounding
  `N(S_k)` itself: a round of the absorption process is defined (via the
  Termination Criterion Lemma, `lemmas/termination-criterion-lemma.md`) as
  exactly one application of `S ↦ S⁺`, and "finitely many rounds occur" is
  the termination-criterion's own iff-characterization of "`N(S_k)` is a
  bounded sequence" — proving this via a type-count argument would only be
  reproving `N(S_k)`-boundedness in different vocabulary, not providing new
  leverage on the open, non-constructive `M_B` quantity (round 16,
  Proposition 3 of `lemmas/binary-refinement-and-threshold-recursion.md`).
  This exact framing was independently dispatched and RETHINK'd pre-build in
  round 17 (`type-alphabet-counting-bound`) on precisely this one-line
  equivalence. **Confirmed dead; do not retry.**
- **(b) Bound `|S_∞| := |⋃_k S_k|` directly**, then use `|𝒫'(S_∞)| ≤
  2^{|S_∞|}-1` to bound the type-alphabet (hence the rounds) outright. This
  is circular: there is no independent source of finiteness for `S_∞` in this
  workspace's certified toolkit — the only proven fact about total recruited
  prime support (that it is generically unbounded as `n → ∞`) cuts *against*
  an a priori bound on `S_∞`, not for one. Assuming `S_∞` finite is
  assuming H2's own conclusion (the absorption chain stabilizing) as a
  hypothesis. **Confirmed dead, circular; do not retry.**
- **(c) A genuinely weaker target: does `|𝒫'(S_k)|` (the type-count, not
  `S_k` or `N(S_k)`) stabilize/become eventually constant, even while `S_k`
  itself keeps growing?** This is the one framing among the three that is not
  literally identical to (a) or (b). But even granting it, it would **not**
  close H2 as needed: the Master Conditional Theorem's own chain
  (`n1-periodicity-reconciliation` §2, via `lemmas/self-absorbing-core-
  theorem.md`) requires a genuinely *fixed* terminal core `S*` with
  `S* = S*⁺` — the absorption process itself halting, index and all — not
  merely a bounded persistent-type *count* while the underlying core
  continues absorbing new primes forever. A bounded type-count with an
  ever-growing core is logically consistent and does not supply the fixed
  `S*` the downstream theorem needs; this is the identical "vacuous/wrong-
  strength weaker target" trap round 12's `subword-complexity-periodicity`
  documented for its own "finitely many colliding residue classes" headline
  (see `current.md` round 12 entry) — a plausible-looking side fact that,
  even if proved, would not discharge the actual required hypothesis.

**Conclusion.** No genuinely new H2 corridor exists within the
"counting/pigeonhole"-on-a-fixed-quantity family; every concrete framing
tried either restates the already-non-constructive `N(S_k)`/`M_B` obstruction
in new notation, is circular with H2's own conclusion, or targets a
provably-insufficient weaker statement. This is recorded here as a permanent
negative finding, parallel in role to H1's growing list of confirmed-dead FAH
mechanisms: **future rounds should not re-probe this specific corridor
(index-count bounds via `|𝒫'(S)|`, `|S_∞|`, or type-count stabilization)
without a genuinely new idea outside this family** — e.g., an arithmetic or
density-based argument on the *identity* of recruited primes (untried,
speculative, flagged by the round-18 explorer as a possible future
direction, not vetted or attempted here).

## Promotable lemmas

- **Vacuous/Weak Self-Absorption Lemma** — statement and proof in full in §2
  above. Unconditional (depends only on the definitions of `Q`, `τ`, `N(Q)`,
  and the absorption operator, all already certified elsewhere in this
  workspace — `persistent-type-pigeonhole.md`, `self-absorbing-core-
  theorem.md`). Reusable: gives the sharp, minimal sufficient condition
  (`N(Q) ≤ 1`, not just `N(Q)=0`) for the absorption chain to terminate
  immediately at the smallest possible core `S* = Q`. Recommended for
  certification to `results/imo-2026-06/lemmas/vacuous-self-absorption-lemma.md`.
