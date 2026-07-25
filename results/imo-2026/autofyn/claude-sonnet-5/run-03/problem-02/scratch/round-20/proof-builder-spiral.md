## imo-2026-02 — spiral-similarity-bootstrap, round 20

Status: partial (unchanged from round 19; genuine incremental progress, main
gap not closed).

### What was done this round

1. **Fully rigorous, new proof of the simplified `Q` characterization**
   (the outline's Step 1), promoted as a new lemma
   `q-as-two-line-intersection`: with `A` at the origin,
   `Q = (line through A parallel to BC) ∩ (perpendicular bisector of BC)`,
   proved by a direct two-line vector computation (substitute the
   already-certified closed form `P = (|C|²-|B|²)/(2|C-B|²)·(C-B)` into both
   lines' defining equations, confirm it satisfies both, use non-parallelism
   for uniqueness). This is a strict simplification of the previously
   certified "foot of perpendicular from `O_ABC`" description — no
   circumcenter arithmetic needed — and gives `QB=QC`, `AQ∥BC` for free.
   Zero gaps in this part.

2. **Attempted the main angle chase** (`A,K,L,Q` concyclic, i.e.
   `∠(KA,KQ) = ∠(LA,LQ) mod π`) using the new `QB=QC` fact alongside the
   already-certified Lemma A, Lemma B, and Corollary. Found and precisely
   recorded the obstruction: every certified relation is stated purely in
   terms of the fixed lines `BK, CL, AB, AC` and points `B,C,M,N` — none of
   them ties `Q` to `K` or `L` directly, so `QB=QC` alone cannot be chained
   into `(∗)` without a new bridging fact (an angle or length relation
   linking `Q` to at least one of `K,L`). This is a genuine, honestly-scoped
   negative finding, not a "clearly it follows" hand-wave — the exact
   missing ingredient is named.

3. **Attempted the systematic point-assignment sweep** of the general
   one-angle lemma against H1 (only one assignment had been tested before,
   and it drifted as `2φ`). Two further relabelings were considered and
   discarded on inspection (they don't correctly encode H1's literal
   statement without extra unproved assumptions). A from-scratch numeric
   solver to test further candidates was attempted (fsolve-based, mirroring
   the population's established H1–H3-solving methodology) but did not
   converge to genuine interior solutions within this round's time budget —
   recorded honestly as a tooling gap, not a mathematical dead end, so a
   future round should retry with a better-conditioned parametrization
   rather than treat the sweep as exhausted.

4. Inversion centered at `Q` (the outline's other suggested alternative
   mechanism) was not attempted at all this round — no time remaining.

### Dependency-chain check before finalizing Status

Traced the full chain: `OM=ON ⟺ O ∈ ℓ ⟺ A,K,L,Q concyclic` is proved
unconditionally (certified in prior rounds, re-confirmed structurally this
round). The *only* remaining piece for the whole `OM=ON` proof via this
route is `A,K,L,Q` concyclic using H1–H3. This is **not** established this
round — the chase stalled at the diagnosed obstruction above. Therefore
Status is honestly `partial`, not `solved`. No step was papered over.

### File updated

`/home/agentuser/repo/results/imo-2026-02/approaches/spiral-similarity-bootstrap.md`
— appended a new "Round 20" entry under Approaches tried with the full
derivation and honest negative findings, added Open-gaps item 4 sharpening
the load-bearing gap's precise missing ingredient, updated the Skeleton
(new step 4b, expanded step 5 with 5 candidate mechanisms including the
untried inversion and the incomplete sweep), and added a new Promotable
lemma `q-as-two-line-intersection` (complete, gap-free, a genuine
simplification of the existing certified `Q`/`P` characterization).

### Recommendation for next round

The main gap needs either: (a) a fixed numeric solver for the H1–H3 family
(current fsolve setup did not converge — needs a better initial-guess/
parametrization strategy) to complete the assignment sweep and test the
inversion-at-`Q` idea numerically first (per the standing memory rule: check
φ-independence before investing in a hand proof); or (b) a genuinely new
bridging fact tying `Q` to `K` or `L` directly (e.g. via a circle through
`Q` and one of `B,C` that also passes through `K` or `L` — the explorer's 5
tested guesses were all refuted, but combinations/radical-axis arguments
using multiple circles remain untried).
