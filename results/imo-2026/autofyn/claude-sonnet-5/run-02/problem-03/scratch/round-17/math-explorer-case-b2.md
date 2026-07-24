## imo-2026-03 (case (b2) deep-dive)

### (1) aimo-0560 "strengthen-the-adversary" crux — what it actually is, and adaptability

Read both `past_crux_moves_database.json` and `past_problems_database.json` for
`aimo-0560` (the "majestic trees" gardener/lumberjack game, N^2 subboards,
lower-bound/achievability half). The crux with `subtopic: games-and-strategy`
is:

> "Replace the adversary with a strictly stronger surrogate whose reply is
> pointwise at least as damaging, so a win against the surrogate transfers
> down and the reply collapses to a finite per-region menu." Concretely: the
> real lumberjack's 4 cuts can land anywhere (non-local), so instead they pass
> to a modified game where the surrogate lumberjack decrements EVERY tree
> outside the played 3x3 block by 1, in addition to his 4 real cuts inside it.
> The surrogate does a pointwise-superset of damage, so a gardener strategy
> that wins against the surrogate also wins against the real lumberjack. This
> collapses the reply to a finite menu of C(9,5)=126 maps, which is then
> exploited by **pigeonhole over repeated play** (the SAME 3x3 subboard is
> replayed many times, forcing some map to recur, driving 5 trees arbitrarily
> high) and a **geometric-schedule ordering** across N^2 subboards to make the
> repeated damage cancel out.

Important: this crux is used for the GARDENER's (constructor's) lower bound
— i.e. it makes an *achievability* argument easier by making the adversary's
reply space finite and analyzable. It is not, in the source problem, used to
prove an upper bound.

**Mapping to imo-2026-03's case (b2):** case (b2) is exactly the opposite
polarity — we need an UPPER bound on c(n), i.e. we need to exhibit *some*
Xiang-Yu (adversary-from-Liu-Bang's-perspective) response with Phi <= a_n T.
This is already what every on-file construction (Bisect-Top-k, peel-then-
dominate, Cross-Piece-Sign-Assignment, Iterated Greedy-Peel, ...) does: each
is literally an explicit Xiang-Yu strategy (a "surrogate", in aimo-0560's
language) whose outcome pointwise bounds the true Phi_min from above
(Phi_min <= Phi(any legal Xiang-Yu strategy)). So **the "strengthen the
adversary" idea in the relevant polarity is not new here — it is exactly the
whole existing peel/bisect/cross-piece construction family**, which is
already proven (via `recursive-image-escape-dead-end.md` and
`peel-and-bisect-ih-dead-ends.md`) to top out short of case (b2).

What aimo-0560 adds beyond what's on file is specifically the **pigeonhole-
over-repeated-play** mechanism and the **geometric cancellation-schedule**
mechanism for chaining many finite-menu replies together. Neither has an
analog here: imo-2026-03 is a **one-shot** Stackelberg game on a single
stick — there is no "replay the same subboard many times" structure to
exploit (this exact non-transplant diagnosis was already made and certified
in round 4 for a different crux, `aimo-0117`'s defer-commitment mechanism,
for the same underlying reason — no multi-round loop exists in this
problem). So the genuinely load-bearing parts of aimo-0560's technique
(finite-menu-via-surrogate-domination is fine; pigeonhole-via-replay is not)
do not transplant as a package.

**Verdict: aimo-0560 is not a strong analog for closing case (b2).** The
"replace with a pointwise-dominating surrogate" idea it exemplifies is
already the operating principle of every construction the population has
tried (all are surrogates in this sense); the genuinely novel machinery in
that crux (pigeonhole-over-many-replays) requires repeated-round structure
this problem does not have. This should NOT be pursued as a new mechanism —
flag as a checked-and-rejected transplant, similar in spirit to round 4's
aimo-0117 finding, so no future round re-attempts it.

### (2) Has an actual LP dual (weighting) certificate ever been constructed for case (b2), or only primal constructions?

Checked every `lp-duality-certificate.md` section (R6 through R16) that
touches case (b2) specifically (R13.1-13.4, R14.1-14.3, R15.1-15.2, R16.1-16.3).
**Finding: despite the slug's name, no genuine LP dual (a system of weights/
multipliers on the primal feasibility constraints, verified via weak/strong
duality) has ever been constructed for case (b2) — every attempt on file is
a primal construction** (an explicit Xiang-Yu strategy: Bisect-Top-k, peel-
then-dominate, Cross-Piece-Sign-Assignment/Alternating-Gap-Cross, Iterated
Greedy-Peel), each giving an upper bound on Phi_min by direct exhibition,
not by dual weighting. The one place an actual dual certificate was built
(round 6, `lp-duality-certificate`'s original R"complete explicit dual
certificate for all 17 leaf cells of the fully-closed n=2 case") was for
n=2 only and was never generalized past a "one consistency check one level
into n=3" — it has not been revisited since round 6/9, and specifically
never applied to case (b2)'s box. This is a genuine gap in what's been
tried, not just a re-labeling issue.

**Why this might matter:** the joint vertex fixed-point obstruction
(R11.5/R12.5/R14.3, cited repeatedly as "the genuinely hard, unsolved
obstruction") is a min-max/LP-vertex-enumeration difficulty by nature — the
population has repeatedly proved Phi_min is attained at a finite polytope
vertex (`vertex-minimum-theorem`, `per-piece-vertex-decomposition-theorem`),
but has always then tried to CONSTRUCT a good vertex explicitly rather than
DUALIZE the whole finite-vertex LP (i.e., exhibit weights lambda_v >= 0
summing to 1 over a small finite candidate-vertex set such that a convex
combination of their Phi-values, or a weighted-averaging argument over
several simultaneous primal strategies, certifies the bound without pinning
down which single vertex is optimal). This is a genuinely different,
not-yet-tried mechanism: **average several of the already-certified
constructions (Bisect-Top-k for varying k, Cross-Piece-Sign-Assignment at
varying j) with data-dependent weights chosen as a function of (p1,p2,p3,T)
to interpolate between them, rather than taking a pointwise min of a fixed
finite family (as R16.3's grid check did) or committing to one family per
case.** This is speculative — not attempted or verified this round — but
concretely different from anything on file, and worth flagging to the
outliner as an unexplored direction distinct from "yet another single
explicit strategy."

### (3) Numeric probe: where do the 212/214 residual grid failures cluster, and does a genuine gap exist?

Ran an independent (not the builder's own script) `scipy.differential_evolution`-based
true Phi_min solver for n=3 (m=4 pieces, budget 3 cuts, exhaustive over all
15 cut-count compositions of 3 among 4 pieces, continuous optimization of cut
positions within each piece) at:
- the exact R16.3 case-(b2) witness `(0.45,0.15,0.25,0.15)`: found true
  Phi_min ≈ 0.50015, vs target a_3*T = 8/15 ≈ 0.53333 — **comfortable
  margin ≈ 0.033, not tight.**
- a 15-point scan around p1=0.45 varying p2 ∈ {0.10,...,0.26} (spanning
  case (b2)'s band T/D_3≈0.067T to a_3T/2≈0.267T) and the p3/p4 split:
  every point found true Phi_min in [0.500, 0.515], target 0.5333 — **slack
  0.018–0.033 throughout, no near-zero-margin point found in this scan.**

This is consistent with (not stronger than) round 14/16's own finding: the
*only* near-tight witness on file is
`(0.4468, 0.2591, 0.2251, 0.0691)` (round 14), which is a highly specific
point right at case (a)'s own boundary (p2 close to a_3T/2), not a generic
interior case-(b2) point — and it is already unconditionally closed by
`cross-piece-sign-assignment-identity.md`. My independent scan found no
second tight point and no violation anywhere sampled. **This corroborates
(as conjecture, not proof) that the "212/214 grid failures" in R16.3 are
indeed an artifact of that check's crude midpoint-parameter choice within
multi-parameter families, not evidence of a real second obstruction** —
consistent with round 16's own honest caveat. I did not find any new
clustering pattern suggesting a missing lemma; the data continues to point
toward "case (b2) has genuine slack almost everywhere, with a razor-thin
boundary band near case (a)'s edge already closed by other means" rather
than toward a specific uncharacterized sub-family needing a new lemma.

### Cheap-kill / structural notes
- No cheap parity/pigeonhole kill found for case (b2) specifically — it
  genuinely appears to need either full vertex enumeration or a smarter
  averaging/dual argument, not a size-bound trick.
- The one concrete cheap thing NOT yet tried: numerically checking the
  informal "average-of-constructions" idea above at the R16.3 uncovered
  points (p1=0.45 vicinity) to see if a fixed simple weighting (e.g.
  50/50 between Bisect-Top-1 and Cross-Piece j=1) already covers them,
  before committing to a full dual-LP formalization — a 10-minute check
  that could validate or kill idea (2) above cheaply.

## Summary for outliner
- Distinct openings: (a) an explicit convex/weighted-averaging LP-dual
  certificate over the already-certified construction family
  (Bisect-Top-k, Cross-Piece-Sign-Assignment at varying j), genuinely
  untried in this polarity — candidate new mechanism; (b) accept
  aimo-0560's surrogate-domination idea is already subsumed by the
  existing construction family and is a dead transplant due to lack of
  repeated-round structure — do not pursue further.
- Candidate technique(s): weighted/convex combination of multiple
  already-proved explicit Xiang-Yu strategies as a function of
  (p1,p2,p3,...,T), rather than a pointwise min over a fixed finite
  family or a single-strategy-per-case argument.
- Cheap-kill candidates: quick check whether a fixed 50/50 (or other
  simple rational) mix of two on-file constructions already closes
  R16.3's two uncovered grid points, before any heavier dual-LP
  formalization — none found yet, not yet tried.
- Knowledge-base entries to use: none new beyond what's already cited
  (`knowledge_base.md` has no dedicated LP-duality/minimax entry to
  invoke by name — checked, not present).
- Analogous past problems (cruxes): `aimo-0560` (subtopic
  games-and-strategy, combinatorics) — checked in full; its
  "strengthen-the-adversary" surrogate-domination move is the same
  polarity as the already-tried peel/bisect construction family (not new
  content), and its pigeonhole-over-repeated-play machinery does not
  transplant (this problem is one-shot, not multi-round) — same class of
  non-transplant as round 4's `aimo-0117` finding. No other genuinely
  analogous crux found for this specific min-max/vertex-fixed-point
  obstruction.
- Prior progress: case (b2) (T/D_n < p2 < a_nT/2) remains the sole open
  region of the general upper bound; peel/bisect/recurse and vertex-enum
  (small n) are all confirmed dead or capped (see
  `peel-and-bisect-ih-dead-ends.md`, `recursive-image-escape-dead-end.md`).
  Both round-14 hard witnesses are unconditionally closed via
  `cross-piece-sign-assignment-identity.md`. A genuine, actually-constructed
  LP dual/weighting certificate has never been attempted specifically for
  case (b2) — only for n=2 (round 6, not generalized).
- Dead ends (do not retry): peel-p1-p2+IH, bisect-p1+IH, recursive-image-
  escape (all proven algebraically inert, zero slack, see the two dead-end
  lemma files); peel-then-dominate 2-cut hybrid (refuted by exact witness,
  ~10% failure rate); aimo-0560-style pigeonhole-over-replay transplant
  (no repeated-round structure to exploit, confirmed by this round's
  analysis — do not re-attempt).
- Small-case / intuition notes (conjecture, not proof): independent
  numeric re-scan (differential_evolution, n=3, exhaustive over all cut-
  count compositions) of case (b2)'s box, including the exact R16.3
  witness and a 15-point scan around p1=0.45, found comfortable slack
  (0.018–0.033 in Phi units) everywhere sampled, no second near-tight
  point — corroborates (does not prove) that case (b2)'s only genuine
  tightness is at the single already-closed round-14 witness near case
  (a)'s own boundary, and that a smarter single argument (rather than
  exhaustive vertex enumeration) may suffice if it can handle that one
  boundary regime cleanly.
