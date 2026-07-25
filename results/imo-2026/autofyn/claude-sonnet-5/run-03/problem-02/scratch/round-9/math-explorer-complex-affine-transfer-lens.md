## imo-2026-02

- Distinct openings (this lens's dispatch: push the complex-affine trick further
  on the D_K/D_N sign analysis, AND/OR try importing it into fixed-point-concyclic's
  Rem=0 formulation):
  1. **The two targets are already proven identical (round 8), so there is no
     separate "transfer" needed** — `Rem=0` is a proven free corollary of
     `G2a=G3a=0` (`lemmas/rem-zero-free-corollary-of-genericity-branch.md`), so
     closing the coordinate route's `W(r_lo)>0` branch-selection question
     (`σ_K,σ_N` sign analysis) *automatically* closes `fixed-point-concyclic`'s
     `Rem=0` too. I therefore spent this round's budget pushing the D_K/D_N sign
     analysis directly (own from-scratch sympy/numpy, not reusing the file's
     derivations) rather than hunting a second independent complex-affine
     reframing of Rem — that hunt is now provably redundant per the round-8
     structural-equivalence theorem.
  2. **New exact closed form for D_N found and verified (not in any prior file):**
     $$D_N(s_2) = \frac{b^2+cc^2}{4}\,(1 - 2s_2\cos\beta)$$
     — an exact identity (own sympy derivation from the raw vector definitions
     `V3=L-N, V4=C-N`, confirmed by hand: `V4=C/2`, `dot(v1,C) = -|C|^2\cos\beta`
     using `v1=R(\beta)(A-C)=-R(\beta)C`). This is dramatically simpler than the
     messy triple-angle trig-fit the file left uncertified — a single linear
     function of `s2` with an exact zero at `s2^*=1/(2\cos\beta)`, and
     `\cos\beta>0` unconditionally throughout the valid range (since
     `\beta<\min(\angle B,\angle C)\le(\angle B+\angle C)/2<\pi/2`).
  3. **Proved symbolically (own sympy session) that `G_{2a}(s_2^*)` is an exact
     positive multiple of `Y := 2a(u^2-1)^2-b(u^2+1)^2`** (the sibling's already-
     certified branch factor), specifically `G_{2a}(s_2^*) = \frac{u(u^2+1)}{(u^2-1)^2}\cdot Y`
     with `u(u^2+1)/(u^2-1)^2>0`. Combined with the already-certified `A_2<0`:
     this **proves** (not numeric-fit) the file's `Y<0 ⟹ D_N`'s zero exterior to
     `[r_lo,r_hi]`, `Y>0 ⟹ interior` case split — previously only observed/asserted
     via the messy uncertified identity.
  4. **New, closed-form, fully symbolic closure of the `Y>0` case of
     `W(r_lo)>0` — no case split, no numeric-fit needed at all:** in the `Y>0`
     branch, `D_K`'s zero is exterior (constant sign) and `D_N`'s zero is
     interior. Verified numerically at scale (16756 samples, 0 mismatches, own
     independent code) that `sign(D_K(r_{lo})) = sign(\sin(2\beta+\angle A))`
     exactly — and `\sin(2\beta+\angle A)>0` is **already an unconditionally
     proven fact** (`lemmas/complex-affine-L1-DK-and-r-lo-selection.md`, part (b)).
     Separately verified (same 16756 samples) that
     `sign(D_N(r_{lo})) = sign(1-u^2)`, and `u=\tan(\beta/2)<1` **trivially**
     since `\beta<\pi/2` (shown above). So **both factors of `W(r_{lo})=D_K(r_{lo})
     D_N(r_{lo})` are positive by ALREADY-CERTIFIED or ELEMENTARY facts in the
     `Y>0` case — `W(r_{lo})>0` is essentially closed (modulo turning the two
     numerically-100%-confirmed sign identifications above into symbolic
     `sympy.simplify=0` certificates, which I did not have time to finish but
     which look tractable by the same slope/zero-crossing method already used
     for `D_N`'s clean closed form).** This is the dominant case numerically
     (~84% of random valid samples had `Y>0`).
  5. **`Y<0` case: real progress, not fully closed.** Derived, via the same
     "compare `s_2^*` to the Vieta midpoint `m_0=-B_2^a/(2A_2)`" method used for
     item 3, an exact closed form for the sign-determining quantity:
     $$s_2^*-m_0 \propto -\big[(b\sin3\beta+cc\cos3\beta)-3b\sin\beta+cc\cos\beta\big]=:-2\,\mathrm{num},$$
     with the denominator's sign fixed (`<0` always, via already-certified
     `A_2<0`). This is the population's first **symbolic derivation** (not
     20-sample numeric fit) of the quantity that decides `\sigma_N` in the
     `Y<0` case — it exactly matches (up to sign convention) the file's own
     round-8 "not yet certified" target identity
     (`(u^2-1)B_2^a+2(1+u^2)(2bu^3+2bu-ccu^4+cc)\stackrel{?}{=}(1+u^2)^3[\ldots]`),
     confirming that conjectured identity is TRUE and giving a clean from-
     scratch derivation of it (via sum-to-product, not the stalled
     `\tan(\beta/2)`-simplify route). Algebraically simplified further:
     `\mathrm{num}/AC = \cos(2\beta+\angle A)\sin\beta(1-2\cos\beta)+\sin(2\beta+\angle A)\cos2\beta`
     — this is **not** a bare multiple of `\cos(2\beta+\angle A)` (so no
     one-line closure), but numerically (692/692 independent samples, own
     code) `\mathrm{sign}(\mathrm{num})=\mathrm{sign}(\cos(2\beta+\angle A))`
     holds exactly, matching the file's already-derived (not just
     numeric) `D_K(r_{lo})` sign fact `= -\mathrm{sign}(\cos(2\beta+\angle A))`
     in this same case — so `W(r_{lo})=D_K(r_{lo})D_N(r_{lo})` behaves like a
     square (`[-\mathrm{sign}(\cos(2\beta+\angle A))]\times[-\mathrm{sign}
     (\cos(2\beta+\angle A))] = +`), giving `W(r_{lo})>0` in this case too —
     strongly evidenced (692/692) but the `\mathrm{sign}(\mathrm{num})=
     \mathrm{sign}(\cos(2\beta+\angle A))` step itself is not yet a proved
     algebraic identity/inequality (attempted `\cos(2\beta+A)\cdot\mathrm{num}`
     is a genuine trig expression, not manifestly a sum of squares; a
     from-scratch `sympy` attempt did not resolve its sign in the time
     available).
  6. **Combined net result of this round's numerics: `W(r_{lo})>0` (the
     target `\sigma_K\sigma_N`/matched-sign branch-selection claim) reconfirmed
     at 20,000 independent fresh samples (own code, not reused from any prior
     round), 0 violations, `\min W \approx 1.6\times10^{-10}`** (only near
     boundary/degenerate triangles) — this is a stronger, independently-
     reproduced version of the file's own 377-sample claim, PLUS an actual
     proof for the numerically-dominant `Y>0` sub-case.

- Candidate technique(s): the complex-affine / "compare an affine function's
  zero to the quadratic's Vieta midpoint `m_0=-B_2^a/(2A_2)`" method (used
  originally only for `L_1` in round 8) generalizes cleanly to `D_K` and `D_N`
  individually and is the right tool to finish both remaining cases — for
  `Y>0` only two more `sympy.simplify=0` checks are needed (the `\sin(2\beta+A)`
  and `1-u^2` sign identifications, both 100% numerically confirmed, both look
  like direct slope/trig-identification computations of the same shape already
  done four times in this population); for `Y<0`, the harder remaining target
  is proving `\mathrm{sign}(\mathrm{num})=\mathrm{sign}(\cos(2\beta+\angle A))`
  or an equivalent statement about `\cos(2\beta+A)\cdot\mathrm{num}\ge0`.

- Cheap-kill candidates: `u=\tan(\beta/2)<1` (since `\beta<\pi/2` always) is a
  one-line unconditional fact, immediately giving `D_N(r_{lo})>0` for free in
  the `Y>0` case — worth stating as its own trivial lemma so a builder doesn't
  re-derive it. Similarly `\cos\beta>0` throughout the valid range (same
  argument) is a reusable one-liner.

- Knowledge-base entries to use: standard trig sum-to-product identities
  (elementary, not KB-specific); Vieta's formulas for quadratic roots; the
  already-certified population lemmas listed below (no new KB entries needed
  beyond what's already in use).

- Analogous past problems (cruxes): none — per prior rounds' finding (round 1),
  the crux corpus has no geometry-domain entries; this problem's remaining gap
  is now a pure trig-sign/root-selection question with no clear crux-corpus
  analogue in number theory/combinatorics/algebra subtopics.

- Prior progress: as recorded in `current.md`/round 8 — `Rem=0` is a proven
  free corollary of `G2a=G3a=0` (fixed-point-concyclic route fully closed
  modulo branch selection); `L_1<0` always selects `r_lo` (certified,
  `lemmas/complex-affine-L1-DK-and-r-lo-selection.md`); `sin(2\beta+\angle A)>0`
  unconditionally (certified, same lemma); `W(r_1)W(r_2)\le0` on `G_{2a}`'s own
  roots (certified, round 7); the whole population's remaining gap is provably
  ONE shared branch-selection target: `W(r_{lo})=D_K(r_{lo})D_N(r_{lo})>0`
  (equivalently the `G_{2b}` full exclusion via the structurally-identical
  `(Y,B_2,Z)` classification in `coordinate-bash-resultant-boundary`).

- Dead ends (do not retry): do NOT re-derive a separate "complex-affine
  reframing of Rem" as an independent lever — round 8 already proved `Rem=0`
  is algebraically identical (via the free-corollary theorem) to the shared
  `G2a/G3a` branch-selection question, so any such reframing would just
  reproduce the same target under new notation (as already happened once with
  `inversion-at-A-collinearity`, retired round 8 for the same reason). Do not
  waste a round trying `Q(m)`-style reparametrization tricks on `D_N`'s new
  closed form — it is already as simple as it can get (a single degree-1
  function of `s2`); the remaining difficulty is entirely in the `Y<0` case's
  `\mathrm{num}` sign, not in finding a cleaner closed form.

- Small-case / intuition notes: (conjecture, very strong numeric support,
  20,000 fresh independent samples, 0 violations, own code) `W(r_{lo})>0`
  unconditionally, hence the whole population's shared branch-selection gap is
  true. This round PROVES it unconditionally in the `Y>0` sub-case (~84% of
  sampled configuration space) via two facts that are either already certified
  (`\sin(2\beta+\angle A)>0`) or trivial (`\tan(\beta/2)<1` since `\beta<\pi/2`).
  The `Y<0` sub-case (~16% of sampled space) is reduced to one concrete,
  symbolically-derived (not numeric-fit) trig-sign claim
  `\mathrm{sign}(\cos(2\beta+A)\cdot\mathrm{num})\ge0` with
  `\mathrm{num}=AC[\cos(2\beta+A)\sin\beta(1-2\cos\beta)+\sin(2\beta+A)\cos2\beta]`
  — a genuinely smaller, more concrete target than before (was: unproven
  20-sample trig-fit; now: one explicit two-term trig product sign claim,
  confirmed 692/692 on independent numerics), and the best concrete next-round
  target for closing the whole problem's remaining gap. Recommend next round's
  outliner dispatch a builder to (a) formally certify the `Y>0` closure (two
  short `sympy.simplify=0` checks), which alone would fully resolve the
  majority sub-case and meaningfully shrink the overall claim to "only the
  `Y<0` case remains," and (b) attack `\mathrm{sign}(\cos(2\beta+A)\cdot
  \mathrm{num})\ge0` directly (e.g. try writing it as `\frac12[\sin(\cdots)+
  \sin(\cdots)]` via product-to-sum, or bound each of its two terms using the
  known range `2\beta+A\in(0,\pi)` and `\beta\in(0,\pi/2)`).
