## imo-2026-06

### Setup / validation
Wrote a fresh, fast generator (trial-division sieve to 6000, minimal-antichain
admissibility test — provably equivalent to "hits every prior radical" since
hitting every antichain-minimal set hits every superset too) at
`/tmp/round-9/scripts/gen.py`, `analyze.py`, `gen_track.py`. Cross-validated
against a slow O(n²) brute-force all-pairs-gcd generator on `a_1=247`,
n≤500: **exact match**, per the standing rule to always sanity-check a fast
generator against brute force before trusting large runs.

### Headline finding: a concrete extremal-bundle mechanism, and it is NOT yet
### observed to stop growing

For every one of 4 tested `a_1` with `|P_1|=2` (`247`, `2747`, `21528751`
[via its singleton cores `{103}`,`{197}`], `10403=101·103`), the **maximum
observed companion-bundle size** `comp_size(i):=|rad(a_i)∖S|` for a singleton
core `S={s}` (`P_1={s,t}`) is achieved, every single time, by a term whose
radical is **exactly** `{first m primes other than t}∪{s}` — i.e. a
"primorial, skipping the sibling top-core prime `t`" set. This is not a
coincidence across cases; it is the *same* mechanism 4/4 times:

| `a_1` | `P_1` | comp_size record | realizing `n` | realizing `a_n` | comp (exact) |
|---|---|---|---|---|---|
| 247 | {13,19} | 6→**7** | 17770→**408816** | 510510→**11741730** | {2,3,5,7,11,17}→**{2,3,5,7,11,17,23}** |
| 2747 | {41,67} | 6→**7** | 21958→**374037** | 1231230→**20930910** | {2,3,5,7,11,13}→**{2,3,5,7,11,13,17}** |
| 21528751 | {103,197,1061}, `S={103}` | 6→**7** | 872→**219146** | 21651630→**52582530** | {2,3,5,7,11,13}→**{2,3,5,7,11,13,17}** |
| 10403 | {101,103} | →6 (N=30000 only) | — | 24892 | 3033030={2,3,5,7,11,13} |

In every "→7" case, the size grew by exactly one **only when `N` was pushed
70×–250× past round 8's tested range** (round 8 tested to `N≤3000`/`1200`;
these are found at `N∈[219146,408816]`). **This is the exact same failure
mode flagged by this workspace's own standing rule** ("extend the search
≥10× before trusting a 'max observed' claim," round 5/7): round 8's
"single-digit, `247→6`, `2747→6`, `21528751→7`" claim is not wrong as far as
it was tested, but it is *not* the true maximum even within easily-reachable
`N` — the true record (within `N≤1.3M` explored here) is `comp_size=7`
(`ω(a_n)=8`) for `247` and `2747`, found in every case by the identical
"skip-the-sibling-prime primorial" construction. **Recommend correcting
`current.md`'s numerical claim before it is cited further as reassuring
evidence.**

Pushed `a_1=247` to `N=1{,}300{,}000` (`a_n` up to `37M`) without finding
`comp_size=8`. The next predicted record (by the same mechanism:
`{2,3,5,7,11,17,23,29}∪{13}`, skipping `19`) has `T_C=340{,}510{,}170`,
requiring `n≈11.9M` at the observed linear growth rate (~28.7/step) — outside
what was computationally feasible this round. **Not tested; genuinely open
whether it appears.**

### The concerning counter-evidence: no blocking witness found for the
### relevant smooth sets, at any scale tried

Checked directly (on the `a_1=247`, `N=1.3M` run) how many terms have a
radical **disjoint** from small "smooth" prime sets — i.e. candidate
*blocking witnesses* for a primorial-type companion bundle (per the
already-certified Realized–Blocked Dichotomy: every such bundle is either
eventually realized, or permanently blocked by one witness disjoint from
it):

- disjoint from `{2,3,5,7}`: **34,552 / 1,300,000** terms (2.7%) — plenty of
  witnesses exist.
- disjoint from `{2,3,5,7,11,13}`: **0 / 1,300,000** — none, at all, in 1.3
  million terms.
- disjoint from `{2,3,5,7,11,13,17}`: **0 / 1,300,000**.

There is a sharp cliff between 4 and 6 smooth primes: once `{11,13}` are
added to the required set, **every single term for 1.3 million steps** uses
at least one of them. This means the specific "primorial-skip-`t`" companion
candidates that keep setting new size records have, empirically, **no
blocking witness in sight** at any scale tried — the mechanism that (per the
Escape-Confinement / Realized–Blocked machinery) *should* eventually cap
bundle growth has not actually been observed to fire even once for these
particular candidates. This is the closest thing to evidence *against*
`(UB_S)` found this round: **the growth mechanism (reuse-the-smallest-primes,
driven by the greedy rule minimizing candidates) is real and reproducible;
the hoped-for blocking mechanism that should eventually stop it has not been
seen to activate, in any of the 4 tested cases, up to the largest `N`
computationally reachable this round.** This does not prove `(UB_S)` is
false — the next blocking event could occur at `n` far beyond what was
tested (just as the size-7 record itself only appeared 100×+ past round 8's
range) — but it reverses the interpretive weight of the round-8 "stays
single-digit" numerics: the single-digit values are a *sampling* artifact of
insufficient `N`, not evidence of a plateau.

### Candidate invariant / mechanism (conjectural, not proved)

**Primorial-Skip Extremality Conjecture.** For singleton core `S={s}`,
`P_1={s,t}`, the maximum companion-bundle size ever realized equals the
largest `m` such that `C_m:={q_1,...,q_m}∪{s}` (`q_1<q_2<...` = primes other
than `t`, in order) is not blocked. Equivalently: the record-setting bundle
is *always* the cheapest possible (smallest `T_C`, via the already-certified
Lemma FOM) companion set that still avoids `t` — because the greedy
minimality rule systematically prefers reusing the smallest available primes
(smaller candidate value) over recruiting a fresh large prime. `T_{C_m}`
grows roughly like a primorial in `m` (super-exponential), while `a_n` grows
only linearly in `n` (already-certified Lemma 1 gap bound) — so reaching
record `m` requires `n≈T_{C_m}/L`, itself growing enormously (consistent
with why size 8 needs `n≈11.9M` while size 7 needed `n≈2×10^5`–`4×10^5`).
**This gives a genuinely new, concrete reformulation of `(UB_S)`:** instead
of an abstract "bound the size of an arbitrary realized bundle," ask whether
the *specific, explicitly-enumerable, totally-ordered* family
`C_1⊊C_2⊊C_3⊊...` (skip-`t` primorials) is eventually-permanently blocked.
This family is far more concrete than the general Δ-system/pigeonhole
targets rounds 6-8 exhausted (bounding count of *arbitrary* bundles) — it is
a single ascending chain, and the "blocking cliff" data above shows the
obstruction, if it exists, must come from a term whose radical excludes ALL
of `{2,3,5,7,11,13,...,q_m}` simultaneously, which the data shows is
*extremely* rare and gets rarer as `m` grows (fewer terms can avoid more
small primes) — arguably making both directions (bounded vs. unbounded)
equally plausible from the data alone, but it turns `(UB_S)` into a
**concrete race**: does the density of "all-large-prime" witness terms decay
slower or faster than the primorial-driven growth in `T_{C_m}`? Neither this
round nor any prior round has framed the question this way; it is a genuinely
different angle from the count-bounding (Δ-system/pigeonhole/Escape-
Confinement) machinery in `lemmas/theorem-UBS-sufficiency.md`.

### Multi-prime-core observation (secondary, `a_1=5005=5·7·11·13`, `|P_1|=4`)

Through `N=30000`, max `comp_size` stayed at only **4** across all 14 proper
cores (vs. 6-7 for the `|P_1|=2` cases at comparable/smaller `N`). Plausible
reading (conjecture, weak evidence, only one `a_1` tested, not pushed to
comparable `N`-scale): more top-core primes give the top core more chances
to "absorb" a growing smooth bundle early (any subset hitting ≥2 of the 4
`P_1` primes simultaneously escapes into `I_{P_1}`, which is unconditionally
finite by Lemma TC), so proper-core bundles for richer `P_1` may have less
room to grow before absorption — the opposite regime from `|P_1|=2`, where
avoiding just one sibling prime is comparatively "cheap." **Not pushed far
enough to know if this holds at scale — flagged as an idea for a future
round, not a finding.**

### Cheap-kill candidates
None found this round that refute `(UB_S)` outright with a concrete
counterexample — the search only shows *unresolved growth*, not a proven
violation. No parity/pigeonhole/injection shortcut found beyond what's
already certified (Escape-Confinement, Δ-system dichotomy, S^+
necessity — all already in `lemmas/`).

### Candidate technique(s)
- Directly analyze the single ascending chain `C_1⊊C_2⊊...` (primorial-skip-
  sibling-prime) via the already-certified Realized–Blocked Dichotomy +
  Escape-Confinement Lemma, rather than a general count-bounding argument —
  a genuinely narrower, more concrete target than anything tried in rounds
  6-8.
- A "density race" framing: bound (or lower-bound) the density of indices `j`
  whose radical avoids a growing smooth prefix `{2,3,...,q_m}`, and compare
  against `T_{C_m}`'s growth rate. This would need either an explicit
  construction of infinitely many such witnesses (proving `(UB_S)`) or a
  proof that no such witness exists for `m` beyond some threshold and thus
  the chain grows forever (refuting `(UB_S)`, meaning the whole round 8
  reduction, though still logically correct as a conditional theorem, would
  point at a genuinely false target — a major, if unwelcome, finding).

### Knowledge-base entries to use
No new KB/crux entries found beyond what's already cited in
`lemmas/theorem-UBS-sufficiency.md`, `lemma-escape-confinement.md`,
`lemma-ERD-realized-blocked-dichotomy.md`, `lemma-FOM-first-occurrence-
minimality.md` — this round's contribution is purely computational/
structural, not a new external tool.

### Analogous past problems (cruxes)
None searched fresh this round (out of scope for this lens per dispatch —
purely computational); round 6's confirmed-twice finding that no
analytic/probabilistic crux tool applies to this deterministic sequence
still stands and is not contradicted by anything found here.

### Prior progress
See `current.md` Round 8 update: whole problem ⟺ `(UB_S)` for every proper
core (Theorem-UBS-sufficiency, unconditional beyond `(UB_S)`, reviewer-
verified). This round's findings **do not close or refute `(UB_S)`** — they
sharpen what's known about it: (a) round 8's "stays single-digit" numeric
claim is confirmed to be a `N`-too-small artifact, true record within reach
is `comp_size=7`/`ω=8`, not 6/7 as stated; (b) no blocking witness for the
record-setting candidate bundles has been found at any tested scale, which
is mild evidence *against* easy boundedness, not for it; (c) a new, sharper,
concrete reformulation (Primorial-Skip Extremality) is available for next
round to attack directly instead of general count-bounding tools.

### Dead ends (do not retry)
Nothing new refuted this round. Reaffirm existing rules: do not re-attempt
count-bounding (Δ-system/pigeonhole/Escape-Confinement-alone) as sufficient
for bundle SIZE (round 8 finding, unaffected). Do not assume "single-digit
through `N≤3000`" is meaningful evidence of a true plateau — it isn't (this
round).

### Small-case / intuition notes (all conjecture, not proof)
- Extremal companion bundles are, in every case checked, literal
  "primorial-skip-the-other-top-core-prime" sets — a strong, reproducible
  structural pattern (4/4 tested `a_1`), not previously identified in any
  prior round's reports.
- The growth in bundle-size record is **slow but so far uninterrupted**: 6→7
  required ~100-250× more terms than round 8 tested; no counter-evidence
  (blocking witness) for continued growth was found despite specifically
  searching for one directly.
- The "0 out of 1.3M terms avoid `{2,3,5,7,11,13}`" statistic is the
  single most concerning number found this round for `(UB_S)`'s truth —
  worth an explorer next round specifically trying to construct (by
  targeted search, not blind simulation) a term whose radical avoids a
  larger smooth prefix, since blind simulation clearly won't reach it in
  reasonable time (the natural next blocking candidate would need to reach
  around `n≈10^7`-`10^8` before any of the observed all-small-prime density
  patterns have a chance to break, based on the observed cliff and growth
  rate).
