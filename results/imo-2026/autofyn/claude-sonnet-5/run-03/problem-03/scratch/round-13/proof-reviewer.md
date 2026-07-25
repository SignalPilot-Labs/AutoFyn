# Round 13 proof-reviewer report

## Verdicts
- `self-similar-induction-on-n`: **CHANGES REQUESTED**
- `global-lp-vertex-sufficiency`: **CHANGES REQUESTED**

## self-similar-induction-on-n

Independently re-derived and re-verified both new results with fresh
exact-`Fraction` scripts (not the builder's), from scratch, using the
already-certified building blocks (Elementwise Monotonicity Lemma,
Global-max/Companion Peeling):

- **Monotonicity Reduction Lemma** (shrinking $D$'s coordinates at fixed
  count/cap toward any target sum $S_0\le\mathrm{sum}(D)$ can only
  decrease $\mathrm{OddSum}(D\cup T)$): re-verified, 2554 random trials,
  $m=1..6$, zero violations. The proof itself is a clean, correct
  chaining of the certified Elementwise Monotonicity Lemma over a
  finite/IVT coordinate-drain.
- **Corollary scoping checked explicitly** (this is the round's headline
  claim — closing the reviewer's round-12 flagged large-sum/$p\ge3$
  gap): the argument reduces any $D$ with $\mathrm{sum}(D)\ge2^m$ down to
  a $D'$ with $\mathrm{sum}(D')=2^m$ exactly, which sits inside the
  *already-certified* safe zone $\mathrm{sum}(D)<3\cdot2^{m-1}$ (since
  $2<3$). So for $m=0,1,2,3$ (where $\mathrm{GT}(m)$ is proved in the
  safe zone), this genuinely and fully removes the scope restriction —
  verified this is not circular and not overclaimed: the file correctly
  distinguishes the *conditional* "for every $m$" tool from the *actual*
  removal, which only holds for $m\le3$ where $\mathrm{GT}(m)$'s boundary
  case is already established.
- **Rank-Shift Identity**: re-verified, 18000 trials, $n=1..12$, all
  $q$, zero violations.
- **Unified Threshold-Pair-Peeling Lemma ($q\ge2$ trivial closure)**:
  re-verified under adversarial stress on $R$ (large count, large sum,
  values at the boundary $2^{k-1}$), 12600 trials, $k=1..7$, $q=2..7$,
  zero violations — confirms the claimed "regardless of $R$'s
  structure" strength, not just a typical-case check.
- **Two remaining sub-gaps confirmed real and precisely stated** (not
  vague "$O(\log m)$" hand-waving): (i) $q=1$ under excess $e\ge1$,
  target $2^k-a_1$, not reduced to a known family; (ii) the small-sum
  mirror of $\mathrm{GT}(k-1)$ itself, target $\mathrm{sum}(R)<2^{k-1}$,
  a genuinely different regime from the boundary-value family studied
  this round. Both gaps are stated with explicit target formulas, so a
  future round has a concrete target, not a vague direction.
- Base case at $k=0$ (uniform in $e$): elementary and correct
  ($2^e>e+1$ for $e\ge1$; direct check at $e=0$).

**Certified** both results into new lemma file
`lemmas/monotonicity-reduction-and-unified-threshold-pair-peeling.md`
(builder correctly did not self-certify). $\mathrm{GT}(m)$ for $m\ge4$
remains open; Status stays `partial`.

## global-lp-vertex-sufficiency

Independently reimplemented $V(p)$ from scratch (own Python:
exhaustive cut-allocation enumeration for $n=3$, softmax-parametrized
multi-restart Nelder–Mead per allocation — same general methodology as
the builder's, but a fresh, independent implementation, not their code)
and reproduced $V(p)$ to the file's own reported precision at all 3 of
round 13's hard $n=3$ points ($0.51140$, $0.51500$, $0.51660$, exact
match). Re-ran the response-side single-choice exchange construction
(closest cross-piece tie in the optimal shape's fragment structure,
rebalance the two owner pieces to make that tie exact) independently:
confirmed $V(q)<V(p)$ (mechanism fails) at all 3 points across two
independent runs (25 and 60 restarts), same sign as the file's finding
in every case (magnitudes differ somewhat run-to-run, consistent with
the file's own documented restart-count sensitivity — this is expected
noise in *which* exact tie-pair and coefficient the optimizer lands on,
not a sign of a bug, since the qualitative conclusion — genuine failure,
not near-zero noise — is robust across both runs). Spot-checked the
existential (best-of-all-ties) form too: found it fails robustly at one
point, holds robustly at another, and is borderline/noise-sensitive at
the third — consistent with the file's own characterization ("$\sim50\%$
failure rate," "not a clean pass"), though my lighter-restart run
disagreed with the file's table on which specific point holds. This
does not change the substantive conclusion (the existential form is
genuinely non-vacuous-failure, not a clean save) but does mean the
per-point existential table entries should be read as illustrative, not
exact-to-the-digit.

**One genuine overclaim found and fixed.** §4.7.4's closing sentence
claimed the entire exchange-mechanism family (region-side and
response-side) is "empirically refuted at $n=3,4$." But this round's
new content (response-side) was only substantively tested at $n=3$ —
its single $n=4$ data point is explicitly flagged two paragraphs earlier
(§4.7.3) as "not a substantive test" (a near-degenerate tie, gap
$<10^{-9}$), and the mechanism *held* there, not failed. Only round 12's
region-geometry mechanisms were substantively tested at $n=4$. Edited
§4.7.4 in place to scope the $n=4$ claim correctly to region-geometry
mechanisms and state plainly that response-side is refuted at $n=3$ and
untested substantively at $n=4$. This is a precision fix, not a
retraction — the practical recommendation (stop pursuing single-move
exchange mechanisms) is unaffected and still well-supported.

No lemma was proposed this round, correctly — a negative numeric finding
is not standalone-certifiable content, matching how prior rounds' negative
findings were handled. Status stays `partial`.

## Files touched
- `results/imo-2026-03/lemmas/monotonicity-reduction-and-unified-threshold-pair-peeling.md`
  (new, certified).
- `results/imo-2026-03/approaches/global-lp-vertex-sufficiency.md`
  (§4.7.4 wording corrected in place — scoping fix, no other change).
- `results/imo-2026-03/current.md` (round-13 "Approaches tried" and
  "Current best" sections added).
- Recorded outcomes for both slugs via `mcp__approach-ranker__record_outcome`
  (both `partial`).

## Independent verification scripts (this review, not the builders')
- `/tmp/round13_review/common.py`, `verify_mono.py`, `verify_qsplit.py`,
  `verify_q_trivial.py` — self-similar-induction-on-n's two results.
- `/tmp/round13_review/lpv_model.py` — independent $V(p)$/mechanism
  reimplementation for global-lp-vertex-sufficiency.
