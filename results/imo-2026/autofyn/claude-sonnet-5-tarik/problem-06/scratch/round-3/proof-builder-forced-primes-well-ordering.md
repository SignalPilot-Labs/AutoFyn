## proof-builder report — forced-primes-well-ordering (round 3)

**File written:** `results/imo-2026-06/approaches/forced-primes-well-ordering.md`
(Status: `partial`).

### What I did

The outline-reviewer's CHANGES REQUESTED verdict specifically flagged that
Key Lemma FF's contradiction mechanism (forced primes `F` finite, via
well-ordering on first-forced index + tension with the Domination Lemma) had
"no stated quantitative bridge" — just "suggesting," not a mechanism. I spent
the round trying to build that bridge as far as it rigorously goes.

**New content, all fully proved (no gaps):**

1. **Lemma FN (necessity)** — every valid FCBC covering set `H` contains `F`.
   Trivial, one line, but the correct starting point.
2. **Lemma FX (new this round)** — if a pair `(i,j)` is forced by a prime
   `p` outside `rad(a_1)`, then the "`P_1`-imprints" `G_i:=rad(a_i)∩rad(a_1)`
   and `G_j:=rad(a_j)∩rad(a_1)` must be **disjoint**. This is a genuinely new
   structural necessary condition, proved from Lemma P alone, and it gives an
   explicit finite bound (`≤3^ω(a_1)`, depending only on `a_1`) on the number
   of "channels" (imprint pairs) that can ever contain a forcing pair —
   converting "is the union over infinitely many pairs finite?" into finitely
   many independent sub-questions.
3. **Lemma FX2 (new)** — every channel touching a *finite* imprint class is
   automatically resolved (forced primes bounded by an explicit finite union
   of radicals). This narrows the genuinely open content to channels between
   two *doubly-infinite* disjoint imprint classes only.
4. **Generalized Lemma C (new)** — the already-certified Global Intersection
   Collapse argument re-derived for an arbitrary infinite index subsequence,
   not just `1,2,3,...`. Used to attempt an "extended-imprint-overlap"
   closing mechanism for the remaining doubly-infinite channels.
5. **Tested that mechanism computationally and found it FALSE in general**
   (`a_1=247`, channel `({13},{19})`: extended imprints stay exactly `{13}`
   and `{19}`, no overlap, yet the channel is empirically forced-finite
   anyway with only 4 primes `{2,3,5,7}`) — a genuine negative finding that
   saves future rounds from retrying this specific mechanism.
6. **Attempted the reviewer's literal request** (a precise inequality
   connecting forced-prime count to `ω`-growth): derived a correct Markov/
   counting bound — conditional on the sibling approach's own open
   `ω(a_n)=O(1)` hypothesis, at most `M_0^2` primes can be the Domination
   Lemma's dominant prime *at any single fixed time N* — and then identified
   **precisely why this doesn't close global finiteness**: the bound is
   pointwise in `N`, not a bound on the union over all `N`, because the
   threshold `N/M_0` grows while a prime's accumulated count can plateau,
   letting primes "cycle through" dominance without ever collecting in one
   bounded pool. This matches, and gives a concrete mechanism-level
   explanation for, the round-3 explorer's independent finding that the
   naive Cauchy–Schwarz approach gives the wrong-direction inequality.

### Bottom line

Lemma FF (finiteness of `F`) is **not proved**. What I did prove is a
genuine, checked reduction of it to a strictly smaller, better-posed open
question (finiteness of `F_{S,S'}` for finitely many channels between
doubly-infinite `P_1`-imprint classes), plus two ruled-out closing
mechanisms with their exact obstructions documented. This satisfies the
"fill this gap as far as you rigorously can" instruction honestly — real
progress, gap still open, nothing overclaimed. Status is `partial`.

Confirmed (per the outline-reviewer's shared-wall warning) that this
approach and `persistent-backbone-monovariant` do bottom out on the same
underlying difficulty (persistence/concentration of dominant primes), even
though reached via different technique (structural channel-reduction +
well-ordering here vs. inductive `ω`-boundedness there) — this is reported
explicitly in the approach file, not hidden.

### Promotable lemmas (see file for full statements/proofs)
- Lemma FN (necessity)
- Lemma FX + finite channel-count corollary (`≤3^ω(a_1)` channels)
- Lemma FX2 (finite-imprint-class channels resolved for free)
- Generalized Lemma C (arbitrary index-subsequence stabilization)
- Conditional Markov density bound (flagged as insufficient alone, reusable
  only with an added persistence argument)

### Numerical checks (supporting evidence only, not proof steps)
Ran `/tmp/round-3/channel_test.py` and `/tmp/round-3/extimprint.py` (new
scripts, reusing `/tmp/round-3/sim.py`'s exact-integer greedy simulator) on
11 values of `a_1` including the adversarial `4199,4087,247,375,221` cases
to verify Lemma FX's disjointness conclusion holds on every observed forced
external prime, and to test (and refute) the extended-imprint-overlap
mechanism.
