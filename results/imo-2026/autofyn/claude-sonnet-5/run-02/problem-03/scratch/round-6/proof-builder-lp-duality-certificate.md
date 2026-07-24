# proof-builder report — lp-duality-certificate, round 6

## What was done
Filled the round-6 outline into a concrete, checked partial result, written
to `results/imo-2026-03/approaches/lp-duality-certificate.md`.

**Step 2 (mandatory deliverable): complete $n=2$ LP-dual certificate.**
Converted all 10 cut-distribution compositions of the already-certified
$c(2)=4/7$ lower bound (`n2-lower-bound-full-closure.md` /
`smoothing-compactness-certificate.md`) into explicit nonnegative-combination
certificates: for every one of the 17 leaf sub-cases, $\Phi-4 = \sum
\lambda_k g_k$ with $\lambda_k\in\{0,\frac12,1\}$, $g_k\ge0$ an elementary
fragment-nonnegativity fact, order/tie fact, or WLOG-labeling fact, using
**at most 2 nonzero terms** in every cell (plus, in some cells, a fixed
additive constant of exactly 1 coming from an untouched/telescoped piece).
Every case was numerically spot-checked against direct sort-and-sum
computation with concrete exact values (shown in the file); all matched.

**Step 3 (extra, beyond the mandatory ask): one $n=3$ consistency test.**
Tested composition $(1,1,0,0)$ at $n=3$ — the simplest one-level-deeper
instance (an $n=2$-shaped cell with one extra untouched piece $p_4=1$
inserted). Found the same "$\le2$ terms, coefficient $\le1$" certificate
shape survives, including at the boundary point that recovers the exact
tie-vertex $\{4,4,3,2,1,1\}$ already certified in `odd-run-reduction-lemma`.
Three numeric spot-checks (including that exact boundary point) all matched.

## Honest assessment: what remains open
- This is genuine partial progress (a complete, checked $n=2$ certificate is
  new, reusable content), but the outline's main target — a certificate
  *recursion* valid for general $n$ (step 4) — is **not proved**. Only 1 of
  many $n=3$ compositions was tested, and it deliberately avoided the
  genuine multi-way-tie regime (`odd-run-reduction-lemma`'s actual reason
  for existing: $\ge2$ *simultaneous* tie constraints, not a one-at-a-time
  cascade of insertions).
- Stated a precise, falsifiable "certificate sparsity" conjecture (at most
  $n$ elementary terms per cell) that would need to be proved for this
  approach to close the problem — this is flagged in the file as
  **equivalent in difficulty to the main theorem** unless a genuine
  induction on the certificate object (not the value) is found.
- Most importantly: it is **not yet shown** that this framing structurally
  escapes $(\star\star)$ (the shared wall every inductive approach hit).
  The one-shot certificate has simply not yet reached a composition where
  $(\star\star)$'s content would have to appear. This is stated explicitly
  as the central unresolved risk, per the outline's own honest flag.

Status set to `partial`. Recommended next step (in the file): test the
genuine `odd-run-reduction-lemma` multi-tie vertex directly (as a true
multi-constraint vertex, not a one-parameter-family boundary point) — if the
certificate there still stays small, that's real evidence for the
conjecture; if it grows to mirror $(\star\star)$'s own structure, that's a
valuable, precise negative result to record honestly rather than iterate on
further.

## Files touched
- `results/imo-2026-03/approaches/lp-duality-certificate.md` (rewritten,
  Status: partial).
