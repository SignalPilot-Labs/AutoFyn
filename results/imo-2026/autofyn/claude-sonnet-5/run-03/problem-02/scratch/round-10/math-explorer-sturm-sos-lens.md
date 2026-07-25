## imo-2026-02 (lens: Sturm/SOS/Schur machinery for the Y(gamma)<0 sub-case)

### The exact target (pulled from the approach files, re-derived independently)
From `coordinate-bash-resultant-boundary.md` §16 (Theorem 16.2's open remainder):
Writing `K=2 sinA sin(A+B)`, `f(β)=2sin(A+B)(sinβ+sinA)-sinB sin(A+β)`, the
open gap is exactly:

**Prove `G(β1):=2K-f(β1) ≥ 0`, where `β1∈(0,γ)` (`γ:=∠B≤∠C`) is the unique
root of `Y(β1)=0`, `Y(β):=2cos²β - (sinB cosA)/sin(A+B)`, in the sub-case
`Y(γ)<0` (⟺ `β1<γ`), and additionally `sin(A+3β1)<0` (⟺ `β1>β0:=(π-A)/3`,
the domain-nonempty threshold shared with Claim (I)).**

Equivalently: `G(β)=2sin(A+B)(sinA-sinβ)+sinB sin(A+β)`, and `β1` satisfies
`cos²β1 = X0 := sinB cosA/(2sin(A+B))` (so real `β1` needs `cosA≥0`, i.e.
`A≤π/2`).

I independently re-verified (own numpy, ≥300k samples, restricted exactly to
`Y(γ)<0 ∧ sin(A+3β1)<0 ∧ B≤C`) that this claim holds with **zero exceptions**
— consistent with round 8/9's own 0-violation reports. I also confirmed a
methodological pitfall to flag: testing `Y(β1)=0` **without** also imposing
`sin(A+3β1)<0` gives ~50% violations (`G<0` in ~18k/36k samples) — so the
`sin(A+3β1)<0` hypothesis is load-bearing and must appear in any certificate,
not droppable.

### Distinct openings tried this round (technique-focused, not framing-focused)

1. **Radical-isolation + double squaring (the "SOS-adjacent" classical
   move).** `G=P+sQ` with `s=sinβ1=√(1-X0)`, `Q=-(sinB cosA+2sin(A+B))<0`,
   `P=2sin(A+B)sinA+sinB sinA·√X0>0` (both `P,Q` explicit, `P` itself still
   contains a nested `√X0`). Isolating and squaring twice (standard
   two-radical technique — same shape as the already-certified
   `radical-isolation-equals-psi` lemma on the sibling Ptolemy route) produces
   a fully rational final certificate `H(sinA,cosA,sinB,cosB)≥0` (needed only
   in the sub-case `R'<0`, where `R'` is an explicit quadratic-in-`X0`
   expression — computed exactly via `sympy`). **Result: `H`'s numerator is a
   genuine degree-16 polynomial in 4 variables (with two Pythagorean
   constraints), fully expanded via `sympy.factor` with NO nontrivial
   factorization found** — it stays as one irreducible-looking blob of ~20
   monomial terms with mixed-sign coefficients, no visible SOS structure.
   This is a **negative result**, and matches the population's own prior
   experience (§7/`radical-isolation-equals-psi`, `lemma-a-equals-psi`): the
   double-square route is *provably equivalent in difficulty* to the direct
   claim, not a shortcut. I do not recommend the outliner pursue raw SOS on
   this degree-16 object directly — it is exactly the kind of heavy
   unstructured target CLAUDE.md's cheap-kill-first guidance warns against.

2. **Schur-type inequality**: does not obviously apply — the target is not a
   cyclic 3-variable polynomial inequality in a natural Schur form; no
   promising Schur substitution found. Not pursued further (structural
   mismatch, not a real candidate).

3. **NEW finding — the actual promising lever: a boundary/degeneration
   argument, not a global algebraic certificate.** I ran (a) 300 independent
   Nelder-Mead searches for the global minimum of `G(β1)` over the exact
   valid sub-region (`Y(γ)<0`, `sin(A+3β1)<0`, `B≤C`), and (b) an independent
   250×250 fine grid sweep. **Both methods agree: the infimum of `G(β1)` on
   this region is `0`, and it is approached ONLY as the case-(b) domain
   itself degenerates** — i.e. as `β0=(π-A)/3 → γ=B` (the domain-nonempty
   threshold from Claim (I) colliding with the right endpoint), which
   *simultaneously* forces `Y(γ)→0` (the case-(a)/(b) boundary) and
   `β1→β0→γ`. Concretely: restricting the sweep to domain-width
   `γ-β0 ≥ ε` gives a minimum of `G` that **shrinks roughly linearly in
   `ε`** (`ε=0.3→minG≈0.19`; `ε=0.1→minG≈0.126`; `ε=0.02→minG≈0.036`;
   `ε=0.005→minG≈0.030`, own script, own random/grid seeds) — i.e. `G(β1)`
   is bounded strictly away from `0` whenever the domain has any fixed
   positive width, and only threatens to vanish exactly where the whole
   sub-case configuration is itself becoming vacuous. This is genuinely
   different from (and looks more tractable than) chasing a single global
   polynomial-positivity certificate: it suggests bounding `G(β1)` below by
   an explicit multiple of `(γ-β0)` (or of `Y(γ)`, or of `sin(A+3β1)`, the
   three quantities that jointly vanish at the bad corner), using the
   **already-certified** monotonicity `(2K-f)'=-f'<0` (Theorem 16.1) plus a
   mean-value/derivative-bound argument, rather than a fresh SOS search. I
   did **not** attempt to complete this — it is a lead, not a proof — but it
   is a genuinely different technique from what the last 2 rounds tried
   (pure algebraic squaring/resultant), and directly explains *why* the
   double-radical squaring route produces an ugly, non-SOS degree-16 object:
   the true inequality is "tight" only at a codimension-2 degenerate corner,
   which is exactly the situation where a naive global polynomial
   certificate is hardest to find but a local/boundary argument is easiest.

4. **Sturm sequences**: not directly applicable as a single-variable tool
   here since the live gap is inherently 2-parameter (`A,B`); a literal
   Sturm-sequence root-count only bites after fixing one parameter. I did
   not find a clean 1-variable reduction this round (unlike, e.g., the
   already-certified `magnitude-bound-and-sign-coincidence.md`/root-pairing
   machinery, which does reduce to genuine 1-variable resultant-root
   arguments). If the outliner wants to push Sturm specifically, the
   degeneration finding above suggests the right target is a 1-variable
   slice **along the degenerating boundary** (parametrize by domain-width
   `t=γ-β0` with `A` free, or by `Y(γ)` itself) rather than the raw 2-var
   `(A,B)` sweep — that could turn into a genuine single-variable Sturm-style
   sign-chart problem worth trying next round.

### Candidate technique(s)
- Boundary/degeneration (limiting) argument connecting `G(β1)` to the
  vanishing of `(γ-β0)` and/or `Y(γ)`, leveraging the already-certified
  monotonicity `(2K-f)'=-f'<0` — **the most promising lever found this
  round**.
- Raw double-radical isolation + squaring to a polynomial SOS target:
  **attempted, produces an unstructured degree-16 polynomial, no
  factorization found — not recommended as the next step** (matches the
  population's own established "equivalent in difficulty" pattern for this
  problem's other radical-isolation attempts).
- Schur: does not apply (structural mismatch).
- Sturm sequences: not directly usable in 2 variables; possibly usable after
  reparametrizing along the degenerating boundary (untested).

### Cheap-kill candidates
None new beyond what's certified. The `sin(A+3β1)<0` hypothesis is confirmed
load-bearing (dropping it causes ~50% violation rate) — a useful sanity
check for whoever builds the next attempt, to avoid accidentally trying to
prove the unconditional (hypothesis-free) version, which is false.

### Knowledge-base entries to use
- **Sum of squares (SOS) / completing the square** and **Quadratic forms /
  PSD** entries (`knowledge_base.md` lines ~17-41) — tried, see negative
  result above; the raw target is not naturally SOS-shaped.
- No Sturm-sequence or Schur-specific named entry found in
  `knowledge_base.md` (only the generic "standard inequalities: AM-GM,
  Cauchy-Schwarz, QM-AM, Schur" line) — nothing further to cite.

### Analogous past problems (cruxes)
The crux corpus has no `geometry` domain (only `number_theory`,
`combinatorics`, `algebra` — confirmed via `crux_moves_documentation.md`),
and this problem's live gap, while now a pure trig-inequality, is downstream
of a full olympiad geometry configuration; per the standing team rule
("NEVER assume a crux corpus match exists for geometry problems"), I did not
force a match. I did check the `algebra` domain's
`inequalities-SOS-and-convexity` subtopic conceptually but found no crux
whose shape (a two-nested-square-root conditional inequality tied to an
implicitly-defined root of a second equation) genuinely resembles this gap
closely enough to be more than generic SOS folklore already captured in
`knowledge_base.md`. **None** genuinely analogous — reporting honestly rather
than forcing a weak match.

### Prior progress
Claim (I) closed unconditionally (Theorem 16.1). Claim (II) closed on
`Y(γ)≥0` (Theorem 16.2, Case a). The sole remaining gap for this entire
approach (and, per round 8's structural-equivalence theorem, for the whole
population) is `G(β1)≥0` in Case (b) (`Y(γ)<0`), as stated above.

### Dead ends (do not retry)
- Raw double-radical isolate-and-square to get a single global polynomial
  SOS certificate: produces a degree-16, 4-variable, apparently-irreducible
  polynomial with no visible SOS decomposition (this round, own `sympy`
  session). Consistent with the already-certified population finding
  (`radical-isolation-equals-psi.md`, `lemma-a-equals-psi.md`) that this
  problem's radical-isolation moves are provably equivalent in difficulty to
  the master claim, not shortcuts — don't re-attempt this exact move without
  a new idea for taming the degree-16 object (e.g. substituting the
  degeneration variables `t=γ-β0`, `Y(γ)` as new coordinates before
  squaring, which was NOT tried this round due to time).
- Schur-form inequality: no applicable substitution found; structural
  mismatch (not a 3-variable cyclic form).

### Small-case / intuition notes (all conjectural, numeric-only)
- Confirmed (0/4474+ samples, own independent code) `G(β1)≥0` holds
  throughout the true hypothesis domain — matches round 8/9's own reports,
  independently reproduced.
- **New, not previously reported**: `inf G(β1) = 0`, attained only in the
  limit where the Case-(b) domain's width `γ-β0 → 0` (a codimension-2
  degenerate corner where `Y(γ)→0` and `sin(A+3β1)→0` simultaneously);
  `G(β1)` appears to scale roughly linearly with domain-width `γ-β0` near
  that corner and stays bounded well away from 0 elsewhere (own Nelder-Mead
  + grid sweeps, consistent across both methods). This is evidence (not
  proof) that a boundary/degeneration argument, not a global positivity
  certificate, is the natural proof shape for this gap.
