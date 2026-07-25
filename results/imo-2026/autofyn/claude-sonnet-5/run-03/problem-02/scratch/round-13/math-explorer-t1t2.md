## imo-2026-02

- Distinct openings:
  1. **New reformulation bypassing the T1/T2 split entirely: work with `f-g` instead of `S=f²-g²`.**
     Since `S=(1+\cos B)^2X_0-\mathrm{RHS}^2` is literally a difference of
     two squares, write `f:=(1+\cos B)\sqrt{X_0}\ (\ge0$, real since
     `X_0\ge0` on `\mathcal D` — `A<\pi/2` and `\cos A\ge0` already proven
     in the `-tangent` file), `g:=\mathrm{RHS}`. Then `S=f^2-g^2=(f-g)(f+g)`
     exactly (trivial algebra, but not previously used as a *working tool*
     in this exact non-squared form by the population — the closest
     relative is the `-twopoint` sibling's `D_1D_2` factorization, which
     only exists **on the boundary curve** `\mathcal C=\{X_0=\cos^2B\}`,
     not on the whole 2-D domain). **This is the concrete "reformulate `S`
     itself and use a different monotonicity argument" opening the dispatch
     asked for.**
  2. **New, independently-confirmed numeric fact: `\partial(f-g)/\partial B>0` throughout `\mathcal D`, with a MUCH stronger margin than `T_1+T_2`.**
     Own from-scratch finite-difference sweep (`h=10^{-6}`, `2{,}000{,}000`
     random `(A,B)` pairs, domain-membership test rebuilt directly from the
     certified exact `\mathcal D` characterization in
     `coordinate-bash-resultant-boundary-pointwise-tangent.md`): `129{,}609`
     valid pairs, **zero** violations, `\partial(f-g)/\partial B\in
     (0.540,\,0.889)$ — never close to `0`. Compare `T_1+T_2`'s own
     reported margin of only `\approx0.177$-`0.19` (round 12). This
     suggests `f-g` is a structurally "cleaner" quantity than `S` itself —
     plausible since squaring `RHS` (to get `S`) introduces the large
     cancellation between `T_1` and `T_2` that made `T_1` alone go as
     negative as `-0.644`; working with `f-g` avoids that cancellation
     altogether.
  3. **Sub-finding: `\partial f/\partial B<0` and `\partial g/\partial B<0` BOTH hold throughout `\mathcal D`** (own sweep: `\partial f/\partial B\in(-0.388,-0.0006)`,
     `\partial g/\partial B\in(-0.989,-0.797)`, both intervals entirely
     negative, `0/129609` violations each). So the real content of finding
     2 is a **magnitude comparison of two same-signed quantities**:
     `|\partial g/\partial B| > |\partial f/\partial B|` — i.e. `\mathrm{RHS}`
     decreases in `B` strictly faster than `f=(1+\cos B)\sqrt{X_0}` does.
     `\partial g/\partial B=\partial\mathrm{RHS}/\partial B` is exactly the
     already-certified closed form (D2) in `lemmas/rhs-partial-b-derivative-
     and-decomposition.md`; `\partial f/\partial B` is new but elementary:
     `\partial f/\partial B=-\sin B\sqrt{X_0}+\dfrac{(1+\cos B)}{2\sqrt{X_0}}
     \dfrac{\partial X_0}{\partial B}`, reusing the certified `\partial
     X_0/\partial B` (`lemmas/x0-partial-b-derivative.md`). Both pieces of
     the new target are built entirely from already-certified exact
     formulas — no new differentiation machinery needed, only a new
     combination and a magnitude-comparison argument (e.g. via `(\partial
     g/\partial B)^2>(\partial f/\partial B)^2`, which may be more tractable
     since both are negative — squaring here is "safe," it does not
     reintroduce the T1-style sign-flip problem because we are squaring two
     same-signed quantities to compare magnitudes, not squaring `\mathrm{RHS}`
     itself against a compound sum).
  4. **The boundary-curve reduction reuses existing, already-partially-analyzed content, cheaply.**
     Directly evaluated `f-g` along the certified boundary curve
     `\mathcal C=\{X_0(A,B)=\cos^2B\}$ (own `scipy.optimize.brentq` root
     find, 40 fresh `A$-samples spanning `[0.42,1.30]`): the values match
     the `-twopoint` sibling's certified `D_1` **almost exactly** (min
     `\to0` at the corner `A^*\approx0.406`, rising to a max
     `\approx0.4054` at `A\approx0.98`, matching the sibling's reported
     `\approx0.4054` at the same location to 4 significant figures) — i.e.
     **`f-g` restricted to `\mathcal C` literally IS `D_1`** (up to the
     sibling's own normalization), and `f+g` restricted to `\mathcal C`
     matches the sibling's `D_2` range (`\approx1.95\to1.00` here vs. the
     file's `1.975\to1.102`). This is a genuine cross-consistency check
     (independent construction, same numbers) — it means **finding 1
     above is the natural 2-variable generalization of the already-
     existing, partially-analyzed `-twopoint` boundary factorization, not
     a disconnected new idea** — a proof of `\partial(f-g)/\partial B>0`
     everywhere on `\mathcal D`, combined with the `-twopoint` sibling's
     still-open `D_1\ge0` on `\mathcal C` (its own open gap: concavity/
     unimodality, currently only `\approx90\%$-confirmed numerically), would
     together give `f\ge g$ on all of `\mathcal D`, hence `S\ge0` there
     (given `\mathrm{RHS}>0`, still needed and still open, so `f\ge g
     \Rightarrow f\ge|g|`).

- Candidate technique(s): work directly with the non-squared difference
  `f-g=(1+\cos B)\sqrt{X_0}-\mathrm{RHS}` and prove it monotone increasing
  in `B` (magnitude comparison of two already-certified derivative closed
  forms, both negative — compare `(\partial g/\partial B)^2` vs. `(\partial
  f/\partial B)^2`, or bound `-\partial g/\partial B` below by a function
  that dominates `-\partial f/\partial B` pointwise), then reduce to the
  boundary curve `\mathcal C=\{X_0=\cos^2B\}` where the target coincides
  with the `-twopoint` sibling's already-partially-closed `D_1\ge0`. This
  is the "combined, non-termwise" mechanism the dispatch asked for: it is
  combined in the sense that `f-g`'s sign is what actually matters (not
  `T_1,T_2` separately), but it sidesteps the squaring that created the
  `T_1$-vs-`T_2` cancellation problem in the first place, rather than
  trying to directly bound `|T_1|\le T_2`.

- Cheap-kill candidates: none new found for ruling anything out; the
  reformulation itself functions as a structural simplification (removing
  the T1/T2 cancellation) rather than a pruning device. One useful
  sanity check already performed: `f,g>0` throughout the sampled domain
  (min `f\approx0.751`, min `g\approx0.315`, matching the already-known
  `\mathrm{RHS}>0` numeric finding) — confirms `f-g\ge0\iff S\ge0` is the
  right equivalence to use (no sign subtlety from `f+g` needing separate
  handling, given `\mathrm{RHS}>0` is assumed/needed anyway).

- Knowledge-base entries to use: none of `knowledge_base.md`'s generic
  entries are specific to this trig-derivative-comparison step; the
  relevant tools remain elementary calculus (product/quotient rule,
  already used throughout this route) plus, if a symbolic magnitude
  comparison is attempted, a possible AM-GM/Cauchy-Schwarz-style bound on
  `(\partial g/\partial B)^2-(\partial f/\partial B)^2` (standard, not a
  named KB entry).

- Analogous past problems (cruxes): did not query the crux corpus this
  round — this lens is a targeted algebraic-mechanism scout building
  directly on certified in-repo lemmas (D1, D2, D3, and the `-twopoint`
  sibling's boundary factorization), not a fresh geometric framing that
  would benefit from corpus search. If a future round wants external
  technique hints for "prove `f`-magnitude-decreases-slower-than-`g`" type
  derivative-comparison inequalities, that would be the natural point to
  query the corpus (subtopic: trigonometric inequalities / calculus
  comparison arguments).

- Prior progress: the D1 (`\partial X_0/\partial B`, certified), D2
  (`\partial\mathrm{RHS}/\partial B`, certified), and D3 (`\partial
  S/\partial B=T_1+T_2$, certified) closed forms in
  `lemmas/x0-partial-b-derivative.md` and `lemmas/rhs-partial-b-derivative-
  and-decomposition.md` are reused verbatim (no new differentiation
  content needed beyond what's already certified) to build both `\partial
  f/\partial B` (new, elementary, one line) and to reuse `\partial
  g/\partial B=\partial\mathrm{RHS}/\partial B$ (already certified, D2).
  The `-twopoint` sibling's `D_1,D_2` boundary-curve factorization
  (`lemmas/star-factorization-on-boundary-curve.md`) is independently
  confirmed (this round, from a completely different construction route —
  `f-g$ and `f+g$ evaluated via `brentq` root-finding of the curve,
  not the sibling's own method) to be numerically identical to `f-g,f+g`
  restricted to `\mathcal C` — a genuine, useful cross-validation, and it
  means the `-twopoint` sibling's still-open `D_1\ge0` gap (unimodality/
  concavity, `\approx90\%$ confirmed) is *exactly* the boundary case this
  new mechanism would still need, so no duplicated future work.

- Dead ends (do not retry): the naive termwise split (`T_1\ge0` alone) is
  confirmed dead per the dispatch and independently reconfirmed this round
  (`T_1$ never observed `\ge0` in the reused domain-membership test,
  consistent with round 12's finding) — do not re-attempt bounding `T_1`
  in isolation. Also: a direct symbolic `sympy.simplify`/`trigsimp` of
  `\partial f/\partial B-\partial g/\partial B` in raw `(A,B)` form does
  NOT collapse to a recognizable closed form or visible sign certificate
  (own attempt, `sympy.trigsimp(method` default), result is a long
  irreducible expression retaining the `\sqrt{X_0}` radical) — a further
  attempt should either (a) clear the radical properly via `2\sqrt{X_0}\,
  (\partial f/\partial B-\partial g/\partial B)$ and handle the resulting
  mixed radical/non-radical terms via a case split on the sign of `T_1`
  (already known, `T_1=(1+\cos B)\partial_BX_0-2\sin B\,X_0$, i.e. `2\sqrt
  {X_0}\cdot\partial f/\partial B\cdot(1+\cos B)`-related — needs a clean
  relation to be worked out, not yet done) or (b) go straight to the
  squared-magnitude-comparison route (`(\partial g/\partial B)^2>(\partial
  f/\partial B)^2`), which is fully radical-free in principle since
  `(\partial f/\partial B)^2` involves `X_0$ (from the `\sqrt{X_0}$ term
  squared) not `\sqrt{X_0}$ alone — NOT yet attempted symbolically this
  round due to time; flagged as the natural next concrete step.

- Small-case / intuition notes: (conjecture only, from numeric sampling)
  `\partial(f-g)/\partial B$ stays comfortably in `(0.54,0.89)` across
  `\approx130{,}000` domain samples — a much wider margin than `T_1+T_2$'s
  own `(0.177,0.19)`-ish range reported in prior rounds, suggesting `f-g`
  (equivalently, the un-squared comparison) is a genuinely less-cancelled,
  more robust quantity to try to certify symbolically than `S`'s own
  derivative. `f-g$ restricted to the boundary curve `\mathcal C` matches
  the `-twopoint` sibling's `D_1$ almost exactly (both numerically found
  independently) — strong (not yet proof-level) evidence that finding 1's
  reformulation and the existing `-twopoint` approach are two views of the
  *same* underlying reduction, meaning progress on either can be directly
  transplanted to the other, and any future build attempting this route
  should coordinate with (not duplicate) the `-twopoint` file's open `D_1
  \ge0` gap.
