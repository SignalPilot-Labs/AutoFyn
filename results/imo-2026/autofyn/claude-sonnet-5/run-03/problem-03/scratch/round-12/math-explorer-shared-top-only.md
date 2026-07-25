# Math-explorer report: the shared TOP-ONLY(m-1) / Branch-I.A-window claim

Lens: the open claim that round 11 found shared between
`greedy-reduction-geometric`'s Case B (via Theorem N) and
`self-similar-induction-on-n`'s Branch-I.A-restricted window. **I did not
attempt a proof** (out of scope for an explorer); this is terrain-scouting
plus numerical stress-testing of candidate mechanisms.

## 1. The claim really is the same statement (verified, not just similar)

**In `greedy-reduction-geometric.md`, Section 15.3, Theorem N** (lines
2671–2765): on the $S'''$-unsplit-full-budget slice of Level-Absorption's
Case B, with $m':=m-1$, the target
$$\mathrm{OddSum}(P\cup\{2^{m-2}\}\cup S''')\ge2^{m-1}$$
is shown symbol-for-symbol identical to
$$\mathrm{OddSum}(P\cup\Gamma_{m'-1})\ge2^{m'}\qquad\text{(TOP-ONLY}(m')\text{)},$$
restricted to $\max(P)<2^{m'-1}$ (TOP-ONLY's complementary,
non-Dominance-Chain regime).

**In `self-similar-induction-on-n.md`, "Reduction B" (lines 1190–1208)**:
for the file's own TOP-ONLY object ($B$ partitions $2^m$, $S$ a refinement
of $\Gamma_{m-1}$; here specialized to $S=\Gamma_{m-1}$ untouched, so
$\mu=\max(S)=2^{m-1}$), the identity
$$\mathrm{OddSum}(B\cup\Gamma_{m-1})\ge2^m\iff\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$$
is proved (a linear duality via the Peeling Lemma, not an approximation).
The right-hand inequality, restricted to $\max(B)<2^{m-1}$, is exactly
`Case-B(m,k)` (Section "Round 5", line 1252), the file's own name for
TOP-ONLY's complementary regime.

**Cross-check:** substituting greedy's $P\leftrightarrow$ self-similar's
$B$, $m'\leftrightarrow m$: both are the *same* two-sided statement — one
side states it as $\mathrm{OddSum}(\cdot\cup\Gamma)\ge2^{\bullet}$, the
other (via the proved duality identity) as
$\mathrm{OddSum}(\cdot\cup\Gamma_{\bullet-1})\le2^{\bullet}-1$ — genuinely
equivalent, not coincidentally similar. **Confirmed: this is one shared
open claim, not two.**

## 2. Once both files' partial closures are combined, the true open residual is much narrower than either file alone reports

- `greedy-reduction-geometric`'s own machinery (Dominant-Chain Theorem +
  Large-Violation-Depth closure, Theorem 6) only closes $\max(P)<2^{m'-3}$
  — leaving $2^{m'-3}\le\max(P)<2^{m'-1}$ open by that file's own count.
- But `self-similar-induction-on-n`'s Theorem 2 (Case-B(m,k) sliver
  reduction, lines 1377–1387) closes **all** of $\max(B)\in[0,2^{m-1}-1]$
  — everything except a **width-1 sliver** $b_1\in(2^{m-1}-1,2^{m-1})$.
  Within that sliver, Branch II (round 8, strong induction) and Branch I.B
  (round 7, certified `lemmas/branch-ib-two-peel-theorem.md`) are **both
  fully closed unconditionally**. The *only* piece left open is the
  **Branch-I.A-restricted window**:
$$c_1\in\bigl[2^{\ell-1},\,2^{\ell-1}+1-\varepsilon\bigr),\quad
\max(C\setminus\{c_1\})<2^{\ell-1},\quad \mathrm{sum}(C)=2^\ell+\varepsilon,\quad
|C|\le\ell+1,$$
  target $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ge2^\ell$ ($\ell=m-1$,
  $\varepsilon\in(0,1)$).

**So the actual joint gap is far smaller than "the whole complementary
regime, one level down"** — it is this one specific, width-shrinking-to-0
window. Neither approach file states this combined fact explicitly (each
only reports its own partial progress); this synthesis is new. Next
round's builder on *either* approach should attack exactly this window,
not the wider regime.

## 3. What's already proved about the window

- **Theorem W** (`lemmas/theorem-w-window-endpoint-witness.md`): at the
  left endpoint $c_1=2^{\ell-1}$ exactly, the witness
  $C=\{2^{\ell-1}\}\cup(\Gamma_{\ell-2}\setminus\{1\})\cup\{r,r\}$,
  $r=1+\varepsilon/2$, gives $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})=
  2^\ell+\varepsilon/2$ exactly (margin $\varepsilon/2>0$). **I
  independently re-verified this in exact `Fraction` arithmetic for
  $\ell=2,\dots,6$, $\varepsilon\in\{1/10,3/10,1/2,7/10,9/10\}$ (25
  instances) — exact match every time**, confirming the certified lemma.
- Gap (b)(i) (piece-cap-unsaturated monotonicity) is fully closed (Lemma
  TPI). Gap (a) (is the endpoint witness optimal?) is reduced, via an exact
  duality identity, to $\mathrm{OddSum}(D\cup\Gamma_{\ell-2})\ge2^{\ell-1}$
  for $D$ with $\le\ell$ parts, $\max(D)<2^{\ell-1}$,
  $\mathrm{sum}(D)=2^{\ell-1}+\varepsilon$ — **this is a genuine one-level-down
  recursive instance of the same family of claims** (not literally the same
  window, but structurally self-similar — see §5 below). Gap (b)(ii)
  (piece-cap-saturated monotonicity) is untouched.

## 4. Stress-testing candidate mechanisms — negative/methodological finding

I tried two numerical approaches to find the window's true minimum margin,
per the mandatory stress-test rule, **before** trusting any mechanism:

1. **Gradient-based search (`scipy.optimize.minimize`, SLSQP, many random
   restarts)** over admissible $D$ at various $(\ell,\varepsilon,c_1)$.
   Result: it could not find margins anywhere near Theorem W's exact
   $\varepsilon/2$ — it reported spuriously large "minimum" margins
   (typically $\ge\varepsilon$, sometimes far larger). This is expected:
   $\mathrm{OddSum}$ is **piecewise-linear and non-smooth** (kinks at every
   tie/reordering event), so gradient descent from generic starts gets
   stuck at non-optimal kinks. **Lesson: do not trust float-optimizer
   "confirmations" of margins on this objective — they are unreliable
   here, consistent with this repo's established rule to always
   re-verify with exact `Fraction` arithmetic, not floats.**
2. **Exact box-polytope vertex enumeration** (all $D$ with at most one
   "fractional" coordinate, rest pinned to $0$ or the cap $2^{\ell-1}$,
   computed in exact `Fraction`s): this *also* failed to reach Theorem W's
   value — it found strictly larger margins at every $(\ell,\varepsilon)$
   tested ($\ell=2,\dots,5$). **Diagnosis:** Theorem W's actual extremal
   witness is not a "box corner" at all — its structure is two internally
   **tied** blocks ($R\cup R$, i.e. pairs of exactly-equal free elements),
   not elements pinned to $0$ or to the cap. So naive box-vertex
   enumeration, which only considers corners of $\{x_i\in[0,M]\}$, **misses
   the true extremal family entirely** — the real vertex set of the
   piecewise-linear problem must also include candidates where several free
   coordinates of $D$ are tied to each other (a genuinely different kind of
   "vertex," arising from the boundary between sort-order cells, not from
   the box constraints). This is a load-bearing methodological finding for
   whoever attempts the LP-vertex route next: **the candidate list must
   include internal-tie configurations among $D$'s own coordinates**, not
   just corners against $0$/cap/$T$-values. This is presumably why the
   round-11 Middle-Regime Vertex Reduction Theorem (Affine-Rank +
   Vertex-Attainment Lemma) only closed two small hand-checked instances
   $(j,c)=(2,1)$ at $m=3,4$ rather than a general vertex list — a full
   general-$\ell$ vertex enumeration for the window needs this richer tie
   structure, which is a nontrivial combinatorial classification, not a
   simple box-corner search.

## 5. Concrete routes for next round's builder (most to least promising)

**(a) Self-referential strong induction on $\ell$, mirroring round 8's
Branch-II mechanism.** Round 8 proved Branch II reduces exactly (via a
well-founded strong induction, $\ell$ strictly decreasing) to the
Branch-I.A window recurring at lower levels — and it worked because Branch
II's recursion always *terminates* (bottoms out in the window, not an
infinite regress). Round 10's gap-(a) reduction shows the window's own
*optimality-at-the-endpoint* question again lands in a structurally
self-similar one-level-down instance
($\mathrm{OddSum}(D\cup\Gamma_{\ell-2})\ge2^{\ell-1}$, itself expressible via
the very same dichotomy machinery: peel $\max(D)$, split by comparison to
$2^{\ell-2}$, landing in "Branch II"-like (closed), "Branch I.B"-like
(closed), or "Branch I.A window"-like (recurse) sub-cases). **This has not
yet been carried out as an explicit strong induction.** The concrete task:
apply the *exact same* three-way dichotomy used for $L_0(\ell,\varepsilon)$
itself to the reduced gap-(a) target, show two of the three branches close
by already-certified tools (Branch-II-analogue, Branch-I.B-analogue), and
the third recurses to $L_0(\ell-1,\varepsilon')$ or a close cousin — then
induct on $\ell$ down to a small, exactly-computable base case ($\ell=2,3$,
matching round 11's `self-similar-induction-on-n` exact hand closures at
$m=3,4$). **Caution:** verify carefully whether the recursion is *exactly*
$L_0(\ell-1,\varepsilon')$ or a strictly relaxed version (gap (a)'s reduced
target has $\max(D)<2^{\ell-1}$, a **weaker** cap than $L_0(\ell-1,
\varepsilon')$'s own $\max(C)\le2^{\ell-1}-\varepsilon'$ hypothesis) — the
file itself flags this as "no easier, only possibly easier in degree," so
the induction hypothesis may need strengthening (prove a slightly more
general statement than $L_0$ itself) before it can close the loop. Stress
test any proposed recursion in exact `Fraction` arithmetic on several
$(\ell,\varepsilon)$ pairs before trusting it — per §4, do not rely on
gradient search for this.

**(b) Exchange-smoothing to the tied-pair canonical family, directly.**
Crux `aimo-0146` (already tried, round 9, for the endpoint only) and a
newly-found related crux `aimo-0119` ("pick the configuration minimizing
the maximum part load... so that any single-item transfer... is
non-improving") both suggest: prove directly that the *maximizer* of
$\mathrm{OddSum}(D\cup T)$ over admissible $D$ at fixed budget is always of
Theorem W's tied-pair shape ($R\cup R\cup\{\text{small}\}$), by showing any
two unequal free elements of $D$ can be smoothed toward equality (or one
pushed to the cap $2^{\ell-1}$) without decreasing $\mathrm{OddSum}$, using
the already-certified Single-Insertion/General-Insertion Lemma
(`lemmas/perfect-pairing-subadditivity-and-general-insertion.md`) as the
one-unit-move primitive. This directly targets gap (a) (optimality of the
witness) and, if it also handles varying $W$ within the window, gap (b)(ii)
simultaneously. Given §4's finding that the true extremal structure is
tie-based rather than box-corner-based, this route is more likely to reach
the right family than blind vertex search.

**(c) Full LP-vertex machinery, but only if the candidate list is
corrected.** If pursuing `self-similar-induction-on-n`'s own Middle-Regime
Vertex Reduction Theorem route (Affine-Rank Lemma + Vertex-Attainment
Lemma) for the window specifically, the candidate vertex list **must**
include configurations with multiple tied free coordinates among $D$
itself (not just ties against $T$-elements or against $0$/cap), matching
Theorem W's own witness shape. Enumerating this richer finite family
generally (as a function of $\ell$, not just by numeric search at fixed
small $\ell$) is a concrete, well-scoped task, but is more work than (a) or
(b) and is likely to reproduce (b)'s conclusion by a more mechanical route.

## Summary for next round

Status: still open, nothing solved this round (as expected for scouting).
Key new information to hand to the builder: (1) the shared claim is
confirmed genuinely identical across both approach files (§1); (2) the
*actual* remaining joint gap, once both files' progress is combined, is
narrow and precise — exactly the Branch-I.A-restricted window (§2), not the
wider "complementary regime" either file describes in isolation; (3)
Theorem W (the window's left-endpoint exact value) is independently
re-verified correct; (4) naive numerical search (both gradient-based and
box-vertex) is unreliable/misleading on this objective and should not be
trusted without accounting for internal-tie configurations (§4); (5) route
(a), self-referential strong induction mirroring round 8's successful
Branch-II mechanism, is the most promising concrete next step, with (b)
exchange-smoothing as a strong alternative/complement.
