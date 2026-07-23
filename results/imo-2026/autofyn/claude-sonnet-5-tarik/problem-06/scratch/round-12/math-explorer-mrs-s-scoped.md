## imo-2026-06 — (MRS_S) computational deep-dive, scoped to the doubly-infinite
pair `(S,S')=({103,197},{1061})`, `a_1=21528751`

### Summary verdict

**No proof found; (MRS_S) remains open for this instance.** But a genuinely
new, robust, deeply-verified STRUCTURAL PATTERN was found — **companion-pool
identity between complementary cores** — that is a strong candidate for a
narrower, more tractable target than the full antichain-freeze `(MRS_S)`
itself, and gives concrete positive evidence (not proof) for Stabilization on
this exact pair pushed far beyond any prior check in this workspace. I could
not identify a mechanism that is *logically* exclusive to being "one of ≤2
cores of a doubly-infinite pair" (i.e. does not generalize) — the pattern
found instead traces to the already-known GLOBAL antichain freeze (Hypothesis
(MRS), the original round-4/5 object), which is a cause common to ALL proper
cores of a fixed `a_1`, not a pair-specific interaction. This is reported
honestly below rather than forced into the requested framing.

### (a) Computational trace of core `S={103,197}`'s local antichain to `n=10^7`

Built and validated (against brute-force all-pairs-gcd on `a_1∈{15,21528751}`,
exact match) a fast generator: at each step, candidate `m` is accepted iff it
shares a prime with every element of the **current global minimal-radical
antichain** (cheap trial-divisibility against a handful of small sets, not
per-candidate full factorization); only accepted terms get fully factored
(trial division by a sieve of primes ≤20000). This makes `N=10^7` tractable
in ~430s.

**Result — pushed 10x past the dispatch's mandated `n~10^6`, to `n=10,000,000`
(~98x past the target core's own freeze index, ~16,800x past the companion
core's freeze index):**

- `S={103,197}`: local antichain `𝓜_n^S` **froze at `n=101957`** (matches
  round 6's already-documented freeze index exactly) with 5 elements —
  `{11,97,103,197}`, `{5,11,103,197}`, `{7,103,197}`, `{2,103,197}`,
  `{3,103,197}` — and **had ZERO further changes from `n=101957` all the way
  to `n=10,000,000`** (`change_count=228` total churn events, all before
  `n=101957`).
- `S'={1061}`: local antichain froze at `n=596` with 2 elements —
  `{2,3,7,11,1061}`, `{2,3,5,7,97,1061}` — **zero further changes to
  `n=10,000,000`**.
- The 4 other proper cores of this `a_1` (`{103,1061}`, `{197,1061}`,
  `{103}`, `{197}`) also froze early (`n≤112599`) and stayed frozen to
  `n=10^7`.

This is the deepest verification of these specific per-core local-antichain
objects in the workspace's history (prior checks tracked the different,
already-certified-hard GLOBAL antichain to 3–5M, or CLASS SIZE growth
`|I_S|` to 8000–160M, but not this specific local-freeze object at this
depth). Per this workspace's standing rule (3 prior false-plateau incidents),
this depth (10x mandate, ~100x past freeze) should be treated as strong,
not just suggestive, evidence — though still evidence, not proof: `(MRS_S)`
for this instance is not established by any finite computation.

### (b) Structural leverage from the OTHER core of the same pair — found, but honestly re-diagnosed

**Direct cross-pair verification (the actual target — Stabilization for this
pair, per Theorem SW / Termination-Sufficiency Lemma):** using the union of
both frozen local antichains' companion primes, `W:={2,3,5,7,11,97}` (only 6
primes), I directly checked **every realized cross pair** `(i,j)`,
`i∈I_S∩[1,N]`, `j∈I_{S'}∩[1,N]`:
- `N=10^6`: `|I_S|=5020`, `|I_{S'}|=293` → **1,470,860 cross pairs checked,
  0 failures** (every pair shares a prime from `W`).
- `N=3,000,000`: `|I_S|=15064`, `|I_{S'}|=875` → **13,181,000 cross pairs
  checked, 0 failures** (this exact pair-count matches round 10's own
  reported figure — cross-confirms both this run and round 10's independently
  — but round 10's covering set needed 16 primes via the "first-`K`-prefix"
  heuristic; the set found here, `W={2,3,5,7,11,97}`, is a genuine
  **tightening to 6 primes**, derived directly from the frozen local
  antichains rather than a heuristic prefix union).

**The leverage I looked for (per the dispatch): does interaction with the
OTHER core of the pair help?** I found a striking numerical fact: the
**companion-prime pool** (i.e. `∪(C\S)` over the frozen local antichain `C`)
of `S={103,197}` is `{2,3,5,7,11,97}`, and the companion pool of `S'={1061}`
is **exactly the same set** `{2,3,5,7,11,97}` — not merely overlapping, but
identical. This pattern reproduced **9/9 times** across 3 independent `a_1`
values and all their complementary-core pairs:

| `a_1` | pair `(S, P_1∖S)` | `S`'s companion pool | `P_1∖S`'s companion pool | match? |
|---|---|---|---|---|
| 21528751 | `({103,197},{1061})` | `{2,3,5,7,11,97}` | `{2,3,5,7,11,97}` | yes |
| 21528751 | `({103,1061},{197})` | `{2,3,7}` | `{2,3,7}` | yes |
| 21528751 | `({197,1061},{103})` | `{2,3,7}` | `{2,3,7}` | yes |
| 4199 | `({13,19},{17})` | `{2,3,83}` | `{2,3,83}` | yes |
| 4199 | `({13,17},{19})` | `{2,3}` | `{2,3}` | yes |
| 4199 | `({17,19},{13})` | `{2,3,83}` | `{2,3,83}` | yes |
| 9674419 | `({79,151},{811})` | `{2,5}` | `{2,5}` | yes |
| 9674419 | `({79,811},{151})` | `{2,3,5,7,23}` | `{2,3,5,7,23}` | yes |
| 9674419 | `({151,811},{79})` | `{2,3,5,7,23}` | `{2,3,5,7,23}` | yes |

For the `4199` pair `(S,S')=({13,19},{17})` I also directly cross-checked at
`N=10^6` (not just via the union heuristic): `|I_S|=12922`,
`|I_{S'}|=513064`, every member's companion intersects `{2,3,83}` (0
exceptions each side), and the finitely many "early" (pre-local-freeze)
members on each side (24 on the `S` side, 5 on the `S'` side) were checked
directly against every element of the other side's frozen antichain — 0
failures.

**Honest re-diagnosis (do not oversell this as pair-specific).** I checked
whether this identity is really about the *complementary* relationship `S
↔ P_1∖S` specifically, or just a symptom of a much smaller shared cause. For
`21528751`, the 6 proper cores fall into only **2** distinct companion pools
total (`{2,3,7}` used by 4 cores, `{2,3,5,7,11,97}` used by 2 cores) — i.e.
`{103}` and `{197}` (NOT complementary to each other) also share a pool. The
**global** minimal-radical antichain `𝓜_n` (Theorem CD's object, the
original round-4/5 Hypothesis (MRS) — a DIFFERENT, already-partially-tracked
object) froze even earlier, at `n=44,967` for `21528751`, with exactly 9
elements whose companion primes union to exactly `{2,3,5,7,11,97}` — the
SAME set found above. This strongly suggests the real mechanism is: **once
the GLOBAL antichain freezes (already the subject of round 4–8's now-retired
`(MRS)`/`𝓥` program, and independently evidenced to depth 3–5M in round 7),
every proper core's eventual companions are forced to be drawn from that one
small global pool** — companion-pool identity between `S` and `P_1∖S` is a
*corollary* of global-antichain freezing shared by ALL cores simultaneously,
not a two-core-specific interaction unavailable to the general (dead)
multi-core program. **This means the mechanism, if provable, would NOT be
"genuinely specific" to the ≤2-cores-per-pair scope in the sense the dispatch
asked for** — it is exactly the kind of "all cores of `a_1`" claim that
round 7's `global-recruiter-finiteness` proved gives *zero new leverage*
(logically equivalent to the per-core statements). I flag this explicitly so
the outliner does not mistake this finding for an escape from that
already-proven equivalence.

### (c) Second doubly-infinite pair instance

Tested `a_1=4199=13·17·19` (all 3 complementary pairs, to `n=10^6`) and
`a_1=9674419=79·151·811` (all 3 complementary pairs, to `n=2·10^6`) — see
table above. The companion-pool-identity pattern held in **all 9/9** tested
pairs across the 3 instances, and the direct cross-pair check (done fully for
one `4199` pair) again found zero violations. The mechanism (if real) is not
an artifact of `21528751` specifically.

### What this does and does not give the outliner

- **Does not bypass the No-Shortcut Corollary.** `forced-primes-well-
  ordering`'s round-11 finding (already certified, `lemmas/lemma-local-
  equivalence-and-no-shortcut.md`) that `(MRS_S)` for `S={103,197}` is
  logically equi-hard to the Multi-Companion Reduction hitting-set target
  stands unrefuted; nothing here challenges that proof. My numerics are
  simply much deeper confirmation that the (still open, still equi-hard-in-
  general) target appears TRUE for this concrete instance.
- **Does give a sharper, more tractable NARROWER target than `(MRS_S)`
  itself for Stabilization specifically**: instead of proving the full local
  antichain freezes (hard, per the width-vs-depth diagnosis in §J Step 6 of
  `forced-primes-well-ordering.md`), the concrete, falsifiable, and now
  heavily-tested claim needed for THIS pair's Stabilization is just: "the
  companion primes of `I_S` and `I_{S'}`, past a computable finite prefix,
  are always drawn from the fixed 6-prime set `{2,3,5,7,11,97}`" — a
  magnitude/recruitment-pool claim, not a full poset-freeze claim. This is
  the same shape as the already-flagged (round 9–10) "count vs. magnitude"
  wall, restated at the pair level, but now with much deeper (10x-mandate,
  ~100x-past-freeze) empirical support specifically for this pair's own
  companion pool being exactly the union of the two per-core frozen local
  antichains — a slightly sharper, cheaper-to-state object than round 10's
  `H_100`/`K=5`-prefix heuristics (6 explicit primes here vs. 16–25 there).
- **A cross-check with this round's other explorer** (`math-explorer-jw-
  rigidity.md`, different lens, Conjecture (JW)) is worth the outliner
  reading together with this report: that explorer independently found
  `{2,3,7,...}`-type small-prime domination is the real content behind joint
  coverage (their "redundancy/density" framing) rather than a rigidity/
  coincidence mechanism — consistent with, and possibly the same
  phenomenon as, the companion-pool-identity finding here, from a different
  angle (Lemma UCR vs. frozen-antichain companion pools). Worth checking for
  synergy before the outliner commits to one of the two framings.

### Recommendation for the proof-outliner

1. **Do not target full `(MRS_S)` for `S={103,197}` directly** — the
   No-Shortcut Corollary's equi-hardness proof stands, and my depth-10^7
   check, while very strong, is still just numerics for one instance.
2. **Consider retargeting at the sharper, narrower claim**: "the companion
   primes recruited by BOTH sides of a doubly-infinite pair, past a
   computable finite prefix, coincide with the (already provably finite,
   per Generalized Lemma C) companion pool of the GLOBAL antichain" — this
   reduces Stabilization-for-a-pair to a statement about the ALREADY-STUDIED
   global antichain (round 4–8's `(MRS)`/`𝓥`, tracked to depth 3–5M and
   frozen with 7–9 elements in every tested case) rather than requiring a
   NEW per-core local-antichain-freeze proof. This is a genuinely different
   reduction from anything currently in the approach files (they target
   `(MRS_S)`, the LOCAL object, directly) — but note it inherits the
   already-known difficulty of proving the GLOBAL antichain freezes in
   general, which the workspace has evidenced very deeply but never proven.
3. **Flag honestly**: no mechanism was found that is logically exclusive to
   the ≤2-cores-of-one-pair scope (as the dispatch hoped) — the companion-
   pool-identity pattern traces to a cause (global antichain freeze) shared
   by every proper core of the same `a_1`, so it does not escape round 7's
   already-proven "global recruiter set gives zero new leverage" equivalence.
   If the outliner wants a target that is provably NOT equi-hard to the
   general multi-core program, this report does not supply one — only a
   sharper restatement plus much deeper numerical support for the existing
   restatement.

### Numerics artifacts (for reference, not re-derivation)
- `/tmp/round-12/sim.py`, `/tmp/round-12/sim2.py` — validated generators
  (brute-force-checked against `a_1=15` and cross-checked against
  `a_1=21528751`'s first 150 terms, exact match).
- `/tmp/round-12/sim_21528751_1e7.log` — full `n=10^7` run, all 6 proper
  cores' frozen local antichains.
- `/tmp/round-12/run3m.log` — `N=3,000,000` direct cross-pair check
  (13,181,000 pairs, 0 failures, `W={2,3,5,7,11,97}`).
- `/tmp/round-12/sim_4199_1e6.log`, `/tmp/round-12/sim_9674419_2e6.log` —
  second/third instance full core tables.
