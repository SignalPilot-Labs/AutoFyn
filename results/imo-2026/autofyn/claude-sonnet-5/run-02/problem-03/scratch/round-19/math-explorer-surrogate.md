## imo-2026-03 (surrogate-adversary / majorization lens, case (b2))

### What aimo-0560's crux move actually is (read from `past_crux_moves_database.json`,
4 entries for `aimo-0560`, domain `combinatorics`)
IMO 2022 P6 (Gardener–Lumberjack), a **multi-round** board game. The load-bearing
chain is: (1) replace the real lumberjack (whose 4 cuts can land anywhere, so
his effect on any one fixed 3x3 subboard is not localized) by a **surrogate**
that, after every gardener move, additionally decrements *every* tree outside
the played 3x3 block by 1 (a strict superset of the real lumberjack's power) —
since the surrogate damages weakly more, a gardener strategy that beats the
surrogate beats the real opponent too; (2) this collapses the surrogate's
reply, restricted to one fixed subboard, to a **finite menu of C(9,5)=126
maps** (which 5 of 9 cells get protected each visit); (3) **replay the same
subboard many times** and use **pigeonhole** over the finite menu to force one
map to recur $\ge l$ times, driving 5 specific trees to height $\ge l$; (4) an
induction/geometric-schedule argument sequences finitely many subboards so
each earlier build-up survives later decrements. **Every one of these four
steps depends on repeated play of the same position** — the pigeonhole step
literally requires replaying a subboard $M\cdot l$ times. This is the actual
technique, not merely "dominate the adversary by a coarser surrogate" in the
abstract.

### Does it transplant to imo-2026-03? No — reconfirms round 17's verdict,
for a sharper reason than round 17 stated
Round 17 already ruled out an `aimo-0560` transplant on structural grounds
(one-shot Stackelberg vs. multi-round replay) — I re-examined the crux
entries directly (not just round 17's paraphrase) and this verdict is
correct and, if anything, stronger than round 17's summary suggests: **three
of the four crux steps (surrogate-superset-damage, pigeonhole-via-replay,
geometric-schedule sequencing) have literally no object to attach to** in a
game where Liu Bang marks $n$ points exactly once and Xiang Yu cuts exactly
once. There is no "replay the same position" move available, so the
pigeonhole engine (the actual load-bearing step, not the surrogate-dominance
idea alone) cannot even be stated here. **Round 18's "surrogate adversary"
proposal for case (b2) borrows only the single word "surrogate" / "replace
the adversary with a dominating coarser one"** — a generic majorization idea
that is NOT specific to `aimo-0560` and does not reuse any of its actual
machinery. Labeling it an `aimo-0560` transplant was optimistic branding by
the round-18 explorer, correctly flagged there as weak/noisy evidence, not a
transplant that reuses a proven mechanism. Treat this as an independent
majorization idea to be judged on its own numeric/structural merits (below),
not as inheriting any credibility from `aimo-0560`.

### Numeric investigation of the majorization idea on its own merits (n=3)
I re-derived round 18's finding independently (`/tmp/round-19` scripts, not
reusing round 18's script) via `differential_evolution` over every cut-budget
composition (exact enumeration of compositions, continuum optimization over
split points within each) — this is a numeric optimizer, **not** exact-
`Fraction` computation (an exact vertex-enumeration evaluator for $m=4,
\text{budget}=3$ was judged too expensive to build reliably in the time
available; DE with `polish=True` and tol $10^{-10}$-$10^{-12}$ is a reasonable
proxy but treat all values below as numeric, not certified):

- At $p_1=0.4,p_2=0.25$ (tail total $0.35$): scanning tail ratio $r=p_3/p_4$
  from $1.5$ to $3.0$, $\Phi_{\min}$ is **not monotonic and peaks at
  $r\approx1.8$** ($\Phi_{\min}\approx0.5125$), strictly above the value at
  the canonical ladder ratio $r=2$ ($\Phi_{\min}\approx0.5083$), confirming
  round 18's finding independently.
- **New this round:** the optimal Xiang-Yu response *at* the argmax tail
  ($r=1.8$) has composition $(2,0,1,0)$ — 2 cuts on $p_1$ (3 fragments) plus
  1 cut on $p_3$ (2 fragments), leaving $p_2,p_4$ untouched — not a clean
  template from the Theorem A-D / Bisect-Top-$k$ / Cross-Piece-Sign family
  (each of those gives $\ge0.55$ at this point, far from the true
  $\approx0.5125$ minimum).
- **New this round, the key negative finding:** repeating the ratio-sweep at
  three more points in case (b2)'s box —
  $(p_1,p_2)=(0.35,0.20)\Rightarrow$ argmax ratio $\approx1.6$;
  $(0.45,0.28)\Rightarrow$ argmax ratio $\approx1.4$;
  $(0.30,0.15)\Rightarrow$ argmax ratio $\approx2.0$ —
  **the argmax tail ratio is not a universal constant; it drifts substantially
  (from $\approx1.4$ to $\approx2.0$) as $(p_1,p_2)$ move inside case (b2)'s
  box.** A quick, lower-precision check at $n=4$ (5 pieces, budget 4,
  geometric-ratio tail family) shows the same qualitative non-monotonicity,
  though the DE budget there is thin enough that individual numbers should
  be treated as very rough (noisy, not a stable characterization).

### Assessment: does a surrogate/majorized worst-tail argument produce a
sound upper bound, or is it unsound?
**Unsound as literally proposed, and likely unsalvageable in low-dimensional
closed form.** The logic required is: find an explicit "worst tail" family
$g(p_1,p_2)$ such that $\Phi_{\min}(p_1,p_2,\text{tail})\le\Phi_{\min}(p_1,p_2,
g(p_1,p_2))$ for *every* legal tail (a genuine dominance/majorization claim),
then prove the single-parameter-family bound $\Phi_{\min}(p_1,p_2,g)\le a_nT$
directly. The evidence above kills the natural candidate for $g$ (the
ratio-2 ladder): since the true argmax ratio is *not* 2 and drifts with
$(p_1,p_2)$, substituting the ladder tail as "the worst case" would
**underestimate** the sup over tails — a proof built on "the ladder tail is
hardest" would be **actively wrong**, not merely a simplification, because
some other ratio genuinely produces a strictly larger $\Phi_{\min}$ at the
same $(p_1,p_2)$. A *correct* dominance lemma would have to characterize the
true argmax as an explicit (possibly non-elementary) function of $(p_1,p_2)$
— but doing that is exactly the same joint vertex/tie-enumeration problem
that has resisted every approach on this front for 15+ rounds (the
$(2,0,1,0)$-composition witness above shows the true optimal response itself
has no obvious closed form even at one single point). So this framing does
not sidestep the shared obstruction (R11.5/R12.5/R14.3) — it just restates it
as "find the argmax tail shape," which needs the identical tool. A weaker,
*sound* substitute — a crude uniform ceiling $\Phi_{\min}(\text{tail-shape})
\le$ (something $n$-and-$p_2$-dependent but shape-agnostic) — is exactly
Theorem D's crude bound (`smoothing-compactness-certificate`/
`lp-duality-certificate`'s Theorem D corollary), already on file and already
shown insufficient to close case (b2) alone.

### Recommendation for the proof-outliner
**Do not build a "worst-tail surrogate" approach as literally proposed —
this is now a confirmed dead end, structurally (no `aimo-0560` machinery to
inherit) and numerically (the natural surrogate candidate, the ladder, is
provably not the true worst case, and the true worst case has no evident
closed form and moves around the box).** This is the fifth distinct
mechanism family to fail on case (b2) (after peel/bisect/recurse,
weighted-combination, boundary-continuity, Danskin/concavity) — per the
project's shared-gap-plateau rule, this crosses further into "the direction
(case-split into (a)/(b1)/(b2) plus a per-region explicit-strategy hunt) may
itself be the wrong top-level framing for this half of the problem," not
just "the technique within that framing is hard." A genuinely different
top-level target the outliner should consider instead of another
per-region-strategy hunt: attack $\Phi_{\min}(p)\le a_nT$ for **all** of
$p$ at once via a single global potential/monotonicity argument over the
*entire* marking simplex (not case-split by $p_1,p_2$ location at all) —
e.g. a strong-duality/minimax argument treating Xiang Yu's mixed extension
properly (not the already-refuted convex-combination-of-values idea, but an
actual LP over the *response polytope* with Liu Bang's marking as a
parameter), or revisiting whether $\Phi_{\min}$, viewed as a function of
$p_1$ alone with everything else on the simplex boundary co-varying by a
fixed rule, has an exploitable single-crossing/monotonicity property distinct
from the already-refuted tail-concavity (round 18) and value-combination
(round 17) attempts.

### Candidate technique(s)
None recommended as viable from this lens beyond the negative results above.
Generic exchange/majorization arguments remain a legitimate class of tools in
principle, but require the argmax characterization this round shows is not
low-dimensional — any future attempt in this family should first establish,
non-numerically, that the argmax tail lies in some finite-parameter family
*before* trying to prove a bound on it (this round's evidence is that no such
family is evident even at $n=3$).

### Cheap-kill candidates
- Confirmed cheap kill: ladder-tail-as-surrogate fails immediately (ratio-1.8
  beats ratio-2 at the tested point) — do not restart from "assume worst tail
  is the ladder."
- A parity/size cheap-kill for any future "collapse to $k$-parameter family"
  attempt: check whether the argmax ratio is even continuous/stable as
  $(p_1,p_2)$ vary smoothly within case (b2) (this round's 3-point spot check
  suggests it is at least smoothly varying, not chaotic, which is mildly
  encouraging for *some* future characterization — but the characterization
  itself was not found this round).

### Knowledge-base entries to use
No new `knowledge_base.md` entry stood out beyond what's already cited
(`exchange-smoothing-vertex-maximization` family, already fully mined by this
front). No LP/game-specific KB entry applies beyond what's on file.

### Analogous past problems (cruxes)
- `aimo-0560` (IMO 2022 P6): **not genuinely analogous** — its crux move is
  inseparable from repeated/replayable play (pigeonhole over many turns),
  which has no counterpart in this one-shot Stackelberg game. Round 17's
  verdict is reconfirmed here from the crux database's actual technique
  text, not just its title; do not cite it again for this front.
- No other `games-and-strategy` crux surfaced as a better match on this pass
  (consistent with round 18's own search of the subtopic).

### Prior progress
Unchanged from `current.md`: case (b2) ($p_1<T/2$, $T/D_n<p_2<a_nT/2$)
remains open; coverage from certified explicit constructions is
$\approx10$–$26\%$ of case-(b2) witnesses at $n=3$–$5$; four mechanism
families (peel/bisect/recurse, weighted-combination, boundary-continuity,
Danskin/concavity-in-tail) are confirmed dead. This round adds the
surrogate/majorization family as a fifth confirmed dead end (see above).

### Dead ends (do not retry)
- **Worst-tail-is-the-ladder surrogate / any low-dimensional closed-form
  majorizing tail family** (this round, new): the argmax tail ratio is not 2,
  is not a universal constant, and drifts with $(p_1,p_2)$ across case (b2)'s
  box — confirmed at 4 independent points, $n=3$ (numeric, DE-based, not
  exact-`Fraction`, but robust across seeds/tolerances in this round's
  scripts). Any future attempt assuming "the ladder tail is hardest" is
  unsound, not merely imprecise.
- All four previously-confirmed dead ends stand: peel/bisect/recurse + full
  IH (`peel-zero-slack-dead-end`, `bisect-containment-dead-end`,
  `recursive-image-escape-dead-end`), weighted/convex combination of primal
  strategies (`convex-combination-futility-theorem`), naive boundary
  continuity (round 18 explorer's finding, folded into the concavity
  refutation), and Danskin/concavity-in-Liu-Bang's-tail-marking (round 18
  build, robust interior local min at $p_3=p_1-p_2$).

### Small-case / intuition notes (all conjectural; DE-based, not exact)
- $n=3$: worst-tail ratio (as a function of $(p_1,p_2)$ inside case (b2))
  observed at $\approx1.4$–$2.0$ across 4 sample points, always giving
  $\Phi_{\min}$ comfortably below target $a_3T=8/15\approx0.533$ (values
  $0.505$–$0.517$) — consistent with round 14's independent finding of real
  slack (margins $\gtrsim0.015$) rather than a vanishing-margin family, but
  this remains numeric corroboration, not proof, of case (b2) being true.
- $n=4$: a rough, lower-confidence geometric-tail-ratio sweep shows the same
  qualitative non-monotonicity but individual numbers are noisy; not a
  reliable data point on its own, included only to flag the pattern likely
  persists rather than being an $n=3$-specific artifact.
