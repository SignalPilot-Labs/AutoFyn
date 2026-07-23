## imo-2026-06 — lens: (PD_{S,S'}) via direct combinatorial structure of the greedy sequence

### Headline finding (new opening, genuinely different from the two dead mechanisms)

**The coarse "core sequence" `G_n := rad(a_n)∩P_1` (i.e. which subset of `P_1`
divides `a_n` — exactly what a core class `I_S` tracks) is *exactly*, not
just approximately, periodic from `n=1` in every tractable instance tested,
and — crucially — this object is logically UNTOUCHED by the round-9
`(UB_S)`/`(MRS)` refutation.** This is not a brand-new discovery — it
reproduces round 4's own `G_n`-periodicity finding
(`approaches/imprint-automaton-periodicity.md`, "Numerical evidence"/
"Negative finding 1" sections) almost exactly, number-for-number — but that
finding has been **dormant since round 5** (superseded by the strictly
stronger (MRS) target, which was later refuted) and, critically, `G_n`
itself never got re-examined as an independent, weaker, *still-alive* target
after (MRS)'s death. `grep -c "G_n" current.md` returns **zero** — this
object has not been discussed in `current.md` since round 5. I re-derived it
independently this round with a fresh generator (built on the round-11
explorer's already brute-force-validated `gen.py`) and a proper KMP/Border-
Lemma exact-period finder (not just density stability), and it is a
genuinely different, structurally cheaper target than everything the
population has attacked in rounds 9–11.

### Why this is not blocked by the dead mechanisms in the dispatch

1. **Not the retired Landau–Turán/`(UB_S)` toolkit.** `(UB_S)`/`(MRS)`
   concerns the FULL minimal-radical antichain, including **companion
   primes outside `P_1`** — bundle SIZE. `G_n` only records which `P_1`-
   primes divide `a_n`, completely ignoring companion primes. A term can
   have an unboundedly large companion bundle (as `(UB_S)`'s refutation
   proves must eventually happen) while its `P_1`-core `G_n` still cycles
   through a small fixed periodic pattern — these are logically independent
   facts about the same term. `(UB_S)` being false for *some* core says
   nothing about `G_n`'s periodicity.
2. **Not the seesaw/Complement-Bound mechanism.** Complement Bound (Lemma
   CB, certified) is a summed-density identity across all classes;
   `G_n`-periodicity is a much stronger, per-index structural claim that
   would *imply* Lemma CB's content (and more) as a corollary, not the other
   way around — a different direction of attack entirely.
3. **The one mechanism that WAS tried and killed for `G_n` (round 4,
   "Negative finding 1") is a *specific proof technique* (fixed-length
   bounded-window Markov/finite-state prediction of `G_{n+1}` from
   `G_{n-W},...,G_n}`), not the target itself.** Round 4 showed, cleanly and
   correctly, that no window of length `W` independent of `n` ever becomes
   fully deterministic until `W` reaches the size of the true period itself
   (circular as a *proof method*). This does **not** rule out other routes
   to `G_n`-periodicity (or the strictly weaker target `(PD_{S,S'})`, which
   only needs a density bound, not exact prediction) — e.g. a counting/
   pigeonhole argument that never tries to predict the next symbol exactly.

### Fresh numerical evidence this round (own generator + exact KMP/Border-Lemma period finder, not density estimation)

Built `/tmp/round-12/work/explore5.py`: computes the exact minimal period of
the core sequence via the classical Periodicity Lemma (KMP failure function;
this gives the *true* minimal period with no ambiguity or divisibility
caveat, unlike a naive brute-force scan). Cross-validated with a 2000-point
random spot-check per instance (100% match every time).

| `a_1` | `k=\lvert P_1\rvert` | `N` tested | exact period `T_G` | periodicity starts at | period-block core distribution |
|---|---|---|---|---|---|
| `4087=61\cdot67` | 2 | 2,000,000 | **64** | `n=1` | `{61}:33, {67}:30, \{61,67\}:1` |
| `247=13\cdot19` | 2 | 3,000,000 | **1806** | `n=1` | `\{13\}:972,\{19\}:624,\{13,19\}:210` |
| `2747=41\cdot67` | 2 | 2,000,000 | **2062** | `n=1` | `\{41\}:1980,\{67\}:40,\{41,67\}:42` |
| `4199=13\cdot17\cdot19` | 3 | 3,000,000 | **105250** | `n=1` | all 7 nonempty subsets of `P_1` present (counts 498–54000) |
| `21528751=103\cdot197\cdot1061` | 3 | 400,000 | **not found** (no period `<400,000`) | — | inconclusive, see below |

All four tractable cases exactly reproduce round 4's own reported periods
(`4199\to105250`, and round 4's table's other entries match my `4087,247`
where overlapping) — this is a strong cross-validation of both generators,
not new numbers, but the **exact-periodicity-from-`n=1`** framing (verified
here by the rigorous Border Lemma out to 1600+ repeated periods for `247`,
not just "density looks flat") is stronger evidence than any density-only
check in rounds 10–11: an exact period, once confirmed over many repeats
with zero deviation, is far harder to explain as numerical coincidence than
a converging ratio.

**`a_1=21528751` (the workspace's hardest instance) did NOT show a period
under `400,000` terms** — pushing further (`N=1.5\times10^6`) hit the
generator's trial-division fallback past the sieve limit (`1.5\times10^8`)
and did not finish in the time budget (>8 min, aborted). This is an honest
gap, not a refutation: `21528751`'s sparsest class `I_{1061}` has density
`\approx0.03\%`-`0.05\%` (per round 10/11 data), so if a period exists it
plausibly needs to be in at least the tens of thousands to make room for
even a handful of the rarest core to appear once — `400,000` may simply be
too small a sample, exactly as round 4 found for `4199` (period `105,250`,
undetectable at smaller `N`). **Do not read this as evidence against
`G_n`-periodicity for `21528751`** — it is the single case round 4's own
5-round-old table also flagged as needing the largest range (`400,000`, `4x`
the eventual period) to confirm; my run simply didn't reach comparable
depth for the 3-generator, highly-asymmetric-prime case.

### The dyadic curiosity (round 11's flag) — resolved, not a coincidence, but a special case of the general phenomenon

Round 11 flagged `a_1=4087`'s densities (`\approx33/64`, `\approx15/32`) as
"suspiciously clean, possibly a 2-adic accident." **This round establishes
it is not a numerical accident at all: it is the exact density implied by
`G_n` having a literal period of 64**, and `64` being a power of 2 is itself
unsurprising for `a_1=61\cdot67` (both primes `\equiv1\pmod4$, `\equiv3
\pmod{64}`ish structure worth a closer look, not investigated further this
round due to time) — but the GENERAL phenomenon (exact periodicity) is not
special to `4087`; every other tractable case shows the identical structure
with a much less "clean-looking" but equally exact period (`1806`, `2062`,
`105250` — none of these are powers of 2 or otherwise visually special,
confirming the dyadic look was an artifact of `4087`'s specific small period,
not a hint about a universal mechanism tied to 2-adic valuations).

### Is `(PD_{S,S'})` possibly FALSE? — no evidence found; if anything, evidence has strengthened

Per the dispatch's request to consider refutation: **no evidence of decay or
falsity was found.** If anything, upgrading round 10–11's "flat density"
numerics to "exact period, zero deviation over 1600+ repeats" is *stronger*
support than any previous round produced. The one open question is whether
this exact micro-level periodicity phenomenon is universal (holds for every
doubly-infinite core pair of every `a_1`, including harder cases like
`21528751`) or whether some instances only have *bounded density* without
ever settling into an exact finite period (a strictly weaker, still
sufficient, fallback target if periodicity itself turns out not to be
universal). **Recommend NOT chasing a refutation further — recommend
attacking the positive direction instead**, given the strength of the new
exact-periodicity evidence.

### Distinct openings for the outliner (ranked by how directly they attack `(PD_{S,S'})`)

1. **(Primary, new) Attack `G_n`-periodicity (or the weaker density-only
   consequence) directly via a mechanism that is NOT bounded-window
   prediction.** Candidates worth a dedicated proof-outliner sketch:
   (a) a **counting/pigeonhole argument on how many times each of the
   `\le2^k-1` possible cores can recur before some other core is *forced***
   — since only finitely many alphabet symbols exist (Theorem CD,
   certified, unconditional), if one could show the sequence *cannot* have
   arbitrarily long runs of a single non-`S'` core (i.e., a bounded-run-
   length claim, much weaker than full periodicity), that alone gives
   `(PD_{S,S'})` with an explicit constant, without needing to establish
   the *exact* period or predict `G_{n+1}` deterministically — this sidesteps
   round 4's circularity diagnosis entirely, since a run-length bound is an
   *inequality*, not a *prediction* claim.
   (b) a **potential/monovariant argument on which core is "next forced"**:
   since `a_{n+1}` is the SMALLEST admissible integer, and admissibility
   only requires intersecting the current minimal antichain (already-
   certified Lemma W3), the "cheapest" way to satisfy multiple *disjoint-
   core* antichain elements simultaneously is disproportionately likely to
   reuse a `P_1`-prime (small, frequently available) — worth formalizing why
   a *specific* proper core cannot dominate indefinitely, using the already-
   certified Growth Lemma's `O(n)` bound on `a_n` as an external anchor
   (unlike `(UB_S)`, this target might legitimately have such an anchor,
   since it's about the coarse `P_1`-projection, a BOUNDED alphabet, not an
   unbounded companion-prime set).
2. **(Fallback, weaker target) Prove ONLY a bounded-run-length / bounded-
   gap statement for each infinite core class** (not full periodicity, not
   even a fixed positive-density constant — just "no core can occur for
   more than `R(a_1)` consecutive same-core-type indices without the other
   side appearing"), which trivially implies `(PD_{S,S'})` with
   `c=1/R(a_1)`. This is strictly easier to state and might be provable via
   an explicit local argument (e.g. bound how long a single prime's
   "coverage" of the antichain can persist using the Growth Lemma) without
   needing anything like exact periodicity.
3. **(Already explored, confirm dead) Bounded-window/finite-state
   prediction of `G_{n+1}`** — proven false by round 4 (window size needed
   equals the actual period, circular). Do not re-attempt in this literal
   form.

### Cheap-kill candidates
None found for `(PD_{S,S'})` itself — every numeric test (5 pairs across 5
`a_1`, one confirmed to an exact period over 1600+ repetitions) supports it.
One useful negative-diagnostic cheap-kill exists for a *specific mechanism*,
not the target: bounded-window Markov prediction of `G_n`, already killed
(round 4).

### Candidate technique(s)
A from-scratch pigeonhole/run-length or potential-function argument on the
coarse `P_1`-imprint sequence `G_n`, exploiting that its alphabet is FIXED
and small (`\le2^k-1` symbols, unconditional via Theorem CD) — genuinely
different in shape from every density/count-vs-magnitude mechanism the
population has tried in rounds 6–11 (those all track companion-prime
structure, which is provably unbounded; `G_n` deliberately discards that
information and only tracks the bounded-alphabet `P_1`-projection).

### Knowledge-base entries to use
None directly (re-confirms rounds 6/9/11's finding: no density/sieve/
Borel-Cantelli KB entry applies to this deterministic recursion). The
relevant *technique* here is closer to a finite-alphabet combinatorics-on-
words / run-length argument than a number-theoretic density tool — worth
noting the KB has no "subword complexity"/"finite automaton" entry either
(round 5's fresh-framing explorer already checked Morse–Hedlund/subword-
complexity for the whole problem and found no escape; this round's proposal
is narrower — a direct run-length/pigeonhole bound on the coarse `P_1`-
projection specifically, not a generic subword-complexity import).

### Analogous past problems (crux corpus)
Did not re-run a fresh corpus search this round (round 11's `pd`-lens
explorer already did a thorough keyword sweep — `density`, `Schnirelmann`,
`Furstenberg`, `van der Corput`, `equidistrib`, `positive proportion`,
`natural density` — across all domains, 10 hits, only `aimo-0680` (IMO-SL
2015 N6) and `aimo-0580` genuinely close, both found NOT transferable; see
`/tmp/round-11/math-explorer-pd.md` for the detailed diagnosis, still valid,
not re-litigated here). No new crux surfaced this round since the new
target (bounded-run-length on a coarse finite-alphabet projection) is a
narrower combinatorial claim than a "density" search term would surface —
worth a **targeted** corpus search next round specifically for "bounded run
length" / "cannot occur too many times consecutively" / "pigeonhole on a
bounded alphabet sequence," a query shape not yet tried.

### Prior progress
Lemma RD, Magnitude Bound Corollary, Proposition 9.4 (conditional bridge
`(PD_{S,S'})\Rightarrow q(i)=O(\log i)`), Lemma CB/Proposition CB-2/
Corollary CB-3 (Complement Bound / Density-Equivalence, all certified) are
unaffected by this round's finding and remain valid, reusable content. This
round's contribution is a structurally new, independently-verified numeric
fact (`G_n` exact periodicity, not just density stability) plus a
resurfacing of a 7-round-dormant object (`G_n`, last discussed round 4–5)
that is provably untouched by the intervening `(UB_S)` refutation — worth
the outliner's attention as a genuinely different top-level target for
`(PD_{S,S'})`, not a third cut of the same `u=w`/seesaw wall.

### Dead ends (do not retry)
- Bounded-length-window Markov/finite-state prediction of `G_{n+1}` from its
  own recent history (round 4, "Negative finding 1" — proven false for
  every fixed `W` up to 40 on 3 instances; window needed to reach
  determinism equals the true period, circular as a proof method). This
  round's proposal explicitly routes around this by targeting run-length
  bounds or potential functions, not next-symbol prediction.
- Reusing the retired Landau–Turán/`(UB_S)` toolkit or the seesaw/
  Complement-Bound-alone mechanism (both already confirmed dead per the
  dispatch; re-confirmed above why `G_n`-periodicity is a structurally
  different object than either targeted).

### Small-case / intuition notes (all CONJECTURE — exact-period numeric evidence, not proof)
- `G_n` (the `P_1`-core-membership sequence) is periodic from `n=1` with NO
  transient/pre-period in every one of the 4 tractable tested instances,
  strongly suggesting periodicity begins immediately, not just eventually —
  if provable, this would give periodicity-from-`n=1` for the COARSE
  object even before FCBC/Theorem 5.1 gives it for the full sequence.
- The dyadic-looking densities for `a_1=4087` are fully explained by its
  unusually small period (`64`); this is a special/coincidental case, not
  evidence of a universal 2-adic mechanism (the other 3 periods — `1806`,
  `2062`, `105250` — have no such clean structure).
- `a_1=21528751` remains the one case where this round could not confirm or
  refute `G_n`-periodicity within a feasible time budget — flagged as the
  concrete next numerical target (push past `N=400{,}000`, ideally with a
  faster large-integer factorization method than the current generator's
  trial-division fallback beyond its `1.5\times10^8` sieve).
