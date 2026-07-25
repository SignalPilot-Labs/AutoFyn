## imo-2026-02

### Task recap
Dispatch: find a technique ORTHOGONAL to root-counting/resultant algebra
(synthetic/projective/inversive/Möbius/direct-trig-identity) that could close
one of the three shared-shape gaps (`coordinate-bash-resultant-boundary`'s
G2b 3-way exclusion, `-pointwise`'s exactly-one-survivor claim,
`ptolemy-trig-identity`'s odd-parity claim), OR find a slicker synthetic
characterization of the branch-selection gap itself. Do not re-litigate
top-level target search (round 3 already did that exhaustively).

## Two distinct findings, both new this round

### Finding 1 (sharper, more tractable reformulation — NOT orthogonal in
mechanism, but a real strengthening of `ptolemy-trig-identity`'s open gap)

Round 6 reduced the sextic positivity `Ψ(τ,A,C)>0` to: **an odd number
(1 or 3) of the four values `F(U_i,V_j)`, `i,j∈{1,2}`, exceed 4** (certified
`lemmas/ptolemy-sextic-parity-reduction.md`). I independently re-implemented
`F(U,V)=\sin A\,UV-\cos A(U+V)-\sin A` and the certified closed forms for
`U_{1,2}` (roots of `\tilde P_1U^2+\tilde Q_1U+\tilde R_1`, genuine root
`U_1` = larger, `\tilde P_1<0`) and `V_{1,2}` (mirror, `B\leftrightarrow C`)
from scratch (own numpy script, `/tmp/test_ptolemy.py`,
`/tmp/test_ptolemy_stress.py`) and tested the *literal parity claim* against
a **sharper, cleaner conjecture**: not just "an odd number exceed 4" but
**exactly the (genuine,genuine) pair `F(U_1,V_1)` exceeds 4, and the other
three `F(U_1,V_2),F(U_2,V_1),F(U_2,V_2)` never do** — i.e. the answer isn't
"1 or 3," it's always exactly 1, and always the same one.

- 20,000 random domain samples (normal sampling across the whole domain
  `0<θ<min(B,C)`, `A,B,C>0`, `A+B+C=π`): **0/20,000 mismatches** — the
  exceeding set is `{(1,1)}` every time, never `{(1,1),(1,2),(2,1)}` (which
  would also be "odd," 3 exceeding) or any other combination.
- 40,000-sample **stress test** specifically targeting corners (thin
  triangles `A→0`, near-isosceles `B≈C`, `θ` near the domain boundary
  `0` or `min(B,C)`): **0/40,000 mismatches**. Margins shrink toward 0 in
  both directions as expected near the known degenerate boundary (min
  genuine margin `F(U_1,V_1)-4 ≈ 0.0032`, max spurious value found
  `≈ 4-4.7×10^{-5}`, i.e. spurious values also approach 4 at the same
  corner but never cross it) — consistent, not a counterexample, but shows
  the bound is genuinely tight at the boundary, not slack.

**Why this matters:** this is *exactly* the direction the approach file's
own Step 4(a) speculated about but didn't pursue ("prove `U≠U_1` forces
`F(U,V)<4` for *either* `V`") — my numerics confirm this stronger,
decomposable claim holds with no exceptions across 60,000 samples total. It
decomposes the single 4-term global parity claim into **two independent,
simpler one-spurious-variable lemmas**:
1. If `U=U_2` (the spurious root of `q_1`), then `F(U_2,V)<4` for **both**
   roots `V_1,V_2` of `q_2` — a claim about one linear form (`F` is linear
   in `V` for fixed `U`) evaluated at both roots of a fixed quadratic.
2. Symmetrically, if `V=V_2`, then `F(U,V_2)<4` for both roots of `q_1`.

Each of these is now the *exact same algebraic shape* as the
already-certified `lemmas/g2b-true-supplementary-parity.md` technique
(product of a linear form at the two roots of a quadratic, via
`Res(quadratic,linear)=lc·L(r_1)L(r_2)`, and showing the sign is forced) —
**directly reusable machinery from a sibling approach**, not a new
technique to invent. To fully pin down "both negative" (not just
same-sign product) one additional piece is needed (e.g. a value/derivative
check at one point, or a sum check), but this is a much smaller ask than
the raw sextic or than a genuine 4-way parity argument. **Recommend**: next
round's `ptolemy-trig-identity` builder attempt Lemma (1)/(2) above via
`Res_V(q_2, L_{U_2})` and `Res_U(q_1, L_{V_2})` exactly as done for
`g2b-true-supplementary-parity.md`.

### Finding 2 (genuinely orthogonal technique — a previously-flagged-but-never-tried mechanism in `fixed-point-concyclic`)

`fixed-point-concyclic` (last touched round 5, dormant since) reduces the
**entire problem** to a complex-number statement with **no branch-selection
ambiguity of the root-counting kind at all**: with `A=0` and `B,C,K,L∈ℂ`,
$$\text{(H1)}\ \frac{(B-K)(C-L)}{BC}\in\mathbb R_{>0},\quad
\text{(H2)}\ \frac{(K-B)(L-N)}{(L-B)(C-N)}\in\mathbb R_{>0},\quad
\text{(H3)}\ \frac{(L-C)(K-M)}{(K-C)(B-M)}\in\mathbb R_{>0}$$
(each fully derived, general, sign-correct — certified). Target:
`\chi:=\frac{(A-L)(K-Q)}{(A-Q)(K-L)}\in\mathbb R` (cross-ratio criterion for
`A,K,L,Q` concyclic; standard Möbius-invariance fact, certified). Round 5
**conclusively retired** the "adjoin more polynomial ideal generators"
lever with a structural argument: the obstruction is that
`\mathrm{Kb}=\bar K,\mathrm{Lb}=\bar L` (antiholomorphic reality) is
*invisible to any polynomial ideal* in the independent (K,Kb,L,Lb)
variables — no finite extension by "ratio-is-real"-species generators can
ever force it. This is a fundamentally different failure mode than the
sign/parity-among-real-roots problem plaguing the other three routes: it's
not "too many candidate roots," it's "the elimination method is the wrong
tool, full stop."

Crucially, **the file's own §5.4 explicitly names an untried, structurally
different lever**: *"an entirely different complex-analytic identity not
based on raw ideal membership (e.g. expressing `χ` as an explicit
product/power of the hypothesis ratios (H1),(H2),(H3) — untried)."* This
would sidestep elimination entirely: since (H1),(H2),(H3) are each
*already known* to be positive real, if `χ` can be shown to equal (or be a
simple rational function of) `H1·H2·H3` or similar, `χ∈\mathbb R` would
follow *immediately*, with no ideal-membership computation and no
root-counting at all — a genuinely different mechanism (algebraic identity
construction, Möbius-map bookkeeping) from all three currently-live
routes.

**I built an independent numeric instance to sanity-check the setup** (not
the conjecture itself — that's builder work): using the population's
rotation parametrization `K=B+t_1(-\cos\beta,\sin\beta)`,
`L=C+s_2R(\beta)(A-C)`, I solved the **true (unsquared) angle equalities**
directly via `scipy.optimize.fsolve` (own script, `/tmp/test_chi.py`) for a
scalene triangle `A=(0,0),B=(3,0),C=(0.9,1.6)`, found a genuine solution
(`t_1≈1.305,s_2≈0.286,u=\tan(\beta/2)=0.1`) satisfying containment, and
confirmed: `H1,H2,H3` are indeed real and positive (`≈0.1246,0.2349,0.0758`)
and `χ` is indeed real (imaginary part `≈2×10^{-12}`, i.e. machine zero) —
consistent with the certified reduction. **I did not find a clean closed
form** for `χ` in terms of `H1,H2,H3` in the time available (`χ/(H1H2H3)`
was not a recognizable constant at this one sample — likely `χ` depends on
`B,C` themselves too, not purely on the three ratios) — this specific
closed-form search is genuinely open and would need either more structure
(e.g. writing `χ` and each `H_i` as explicit rational functions of `K,L,B,C`
and doing the algebra symbolically) or a cleverer choice of what to
multiply/combine. This is real, unsolved work — **flagging it as the
concrete next step for a revival of `fixed-point-concyclic`, not a closed
finding.**

## Distinct openings surfaced
1. (Sharpened, tractable) Decompose `ptolemy-trig-identity`'s odd-parity
   claim into two "linear-form-at-both-roots-of-a-quadratic" sub-lemmas
   (Finding 1) — reuses the exact resultant technique already certified in
   `g2b-true-supplementary-parity.md`.
2. (Genuinely orthogonal) Revive `fixed-point-concyclic` and attempt to
   express `χ` as an explicit algebraic combination of `(H1),(H2),(H3)`
   (Finding 2) — a Möbius/complex-identity mechanism with zero
   root-counting content, explicitly flagged as untried by the approach's
   own file.
3. (Considered, not pursued) A directed-angle-mod-`π` synthetic chase was
   considered as a way to sidestep the "genuine vs. supplementary" root
   ambiguity common to all three coordinate/trig routes, but on reflection
   this does **not** help: directed angles mod `π` *already* conflate an
   angle with its supplement, which is precisely the ambiguity causing the
   branch-selection problem in the first place (the problem's hypotheses
   are genuine, non-directed angle equalities, a strictly stronger
   condition) — a directed-angle proof would establish a weaker fact.
   **Not recommended.**

## Candidate technique(s)
- Finding 1: resultant-of-(quadratic, linear-form-at-its-roots) sign
  argument, same shape as `lemmas/g2b-true-supplementary-parity.md`.
- Finding 2: Möbius-invariance / cross-ratio algebra, explicit identity
  construction (not ideal elimination) — genuinely orthogonal to root
  counting.

## Cheap-kill candidates
None obvious beyond what's already found. Finding 1's decomposition is
itself a form of "cheap kill" in spirit (turns one global parity claim
into two much smaller local sign claims using existing certified
machinery) — recommend trying it first since it's the lowest-effort lead
with the most reuse.

## Knowledge-base entries to use
- "Resultants" entry (`knowledge_base.md`) — for both Finding 1's two new
  sub-lemmas and re-derivable from `g2b-true-supplementary-parity.md`'s
  exact template.
- Cross-ratio / Möbius-invariance concyclicity criterion (already used by
  `fixed-point-concyclic`, `ptolemy-trig-identity`'s "General Ptolemy
  equality theorem") — the natural tool for Finding 2 if a closed form for
  `χ` in terms of `H1,H2,H3` is found.

## Analogous past problems (cruxes)
Not queried this round — dispatch instructions targeted a *technique*
scout within the existing approach population, not a fresh problem framing
search (round 3 already did the crux/framing search). No new crux corpus
query performed; if useful, a future round could search the corpus for
"cross-ratio expressed as product of sub-ratios" or "Ptolemy inequality
strict-vs-equality branch selection" style cruxes, but this wasn't
attempted here for lack of a clean subtopic match to either finding.

## Prior progress
See `current.md`'s Round 6 summary (reproduced faithfully above). All three
live approaches remain exactly as described there — no change to their
certified status this round; both findings above are new leads on top of
that state, not modifications to it.

## Dead ends (do not retry)
- Directed-angle-mod-`π` synthetic chase as a way to bypass branch
  selection (see "Considered, not pursued" above) — does not help, the
  ambiguity is inherent to the undirected-angle hypotheses themselves.
- (Reconfirmed from round 5) Adjoining more "ratio-is-real"-species ideal
  generators to `fixed-point-concyclic`'s elimination — conclusively
  retired, do not revisit with more generators of the same species; only
  a genuinely different mechanism (Finding 2, or real-coordinate
  reformulation which collapses into the coordinate route) can work.

## Small-case / intuition notes (labeled conjecture)
- **Conjecture (Finding 1, strong numeric support, 60,000 samples, 0
  exceptions across normal + 4 stress-test corner regimes):** for every
  valid `(θ,A,B,C)`, exactly the pair `(U_1,V_1)` (both genuine roots) has
  `F(U_1,V_1)>4`; all three other index combinations have `F<4`, with
  margins shrinking to 0 together only in the shared degenerate limit
  (`A→0` / `θ`→domain boundary). This is strictly sharper than the
  certified "odd number exceed" parity claim and looks more tractable to
  prove via the decomposition above.
- **Not a conjecture (numerically sanity-checked only, not a new claim):**
  the `fixed-point-concyclic` (H1),(H2),(H3)-real / `χ`-real reduction
  reproduces correctly on an independently-constructed genuine solution
  found via `fsolve` on the true unsquared angle system (own script, own
  triangle, not reusing any file's numbers) — this is just a
  cross-check that the certified reduction is implemented/stated
  correctly, not new mathematical content.
