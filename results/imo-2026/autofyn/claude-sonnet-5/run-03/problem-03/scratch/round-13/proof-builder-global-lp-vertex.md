# Round 13 report — `global-lp-vertex-sufficiency`

## Target

Per the outline: close the remaining Σ-shape Existence-Theorem gap via the
one untried mechanism — build the boundary candidate $q$ from the optimal
**adversary response** $\sigma^*(p)$'s own near-tie structure, rather than
from region-slack geometry (all of which round 12 and this round's earlier
explorer pass refuted).

## What was done

1. Formalized the mechanism precisely (approach file, new Section 4.7.1):
   at interior $p$, take the optimal shape $\sigma^*$ (Global Vertex
   Lemma), find the pair of $\sigma^*(p)$'s fragment/untouched values
   owned by two *different* pieces with the smallest gap (the tie
   "closest to breaking"), and build $q$ by moving exactly those two
   pieces' mass (holding $\sigma^*$'s own fragment coefficients fixed)
   until that tie becomes exact. Also formalized the maximally weak
   **existential** form (best of all cross-piece tie pairs, not just the
   closest).
2. Implemented an independent numerical estimator of $V(p)$ and of
   $\sigma^*(p)$'s fragment structure (exhaustive cut-allocation
   enumeration + multi-restart Nelder–Mead, the same methodology already
   used and reported in the file's Section 4.6.1), re-verified against
   the file's own certified exact $V(e_0)$ values and against round-13's
   explorer's reported digits. Code: `/tmp/round-13/lpv_test/model.py`,
   `/tmp/round-13/lpv_test/mechanism.py`.
3. **Stress-tested numerically before any proof investment** (mandatory
   gate, per the dispatch): re-ran the mechanism at the exact three $n=3$
   interior points that broke every region-geometry mechanism this round
   (excess up to $\approx0.0098$ against the best region-geometry
   candidate), plus 6 fresh random interior points.

## Result: refuted, genuinely (not noise)

- **Single-choice form**: fails at all 3 of round 12's hard points, with
  excess $0.00065$–$0.00587$, confirmed stable at $2.5$–$4\times$ more
  restarts (established noise floor is $10^{-6}$–$10^{-10}$, so these are
  3–4 orders of magnitude above noise — genuine).
- **Maximally weak existential form** (best of every cross-piece tie
  candidate): still fails at 2 of the same 3 points (excess
  $\approx0.0031,0.0041$); holds at the third.
- **Fresh random sample** ($n=3$, 6 points, not cherry-picked): 3/6 fail
  — essentially the same $\approx50\%$ failure rate as every
  region-geometry mechanism tried in round 12.

No violation of $V(p)\le c(n)$ itself was found anywhere (consistent with
every prior round) — only this specific proof mechanism fails.

## Conclusion / recommendation

Per the dispatch's own contingency plan: this closes off **exchange
arguments as a class** (region-side and response-side, single-choice and
existential) as a route to the endpoint-inequality bypass of
$\Sigma(n,k)$-classification. Documented in full (Sections 4.7.1–4.7.4)
in `results/imo-2026-03/approaches/global-lp-vertex-sufficiency.md`. The
two remaining genuinely open routes, unchanged from round 12's
assessment: (a) direct $\Sigma(n,k)$-classification (already fully closed
for $Q_{\text{region}}$, Sections 1–4.4), and (b) fragment-vs-fragment
tying (Section 4.5, not yet attempted with a real proof, only soft
numeric signal). **Recommend the next round not spend further effort on
exchange-move variants of this shape** — the mechanism space (fixed
vertex, tightest-slack, existential-region, closest-response-tie,
existential-response) is now exhausted and consistently fails at a
$\sim50\%$ rate.

Status remains `partial`. No lemma was proposed for certification this
round (the finding is negative/numerical, matching how round 12's own
negative numerical findings were handled — not standalone-certifiable
content, fully captured in the approach file's Section 4.7).
