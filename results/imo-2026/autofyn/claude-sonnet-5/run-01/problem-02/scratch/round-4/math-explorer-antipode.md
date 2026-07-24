## imo-2026-02 (lens: what would prove L1/L2 synthetically; unsigned-angle bypass of the sign-error class)

- Distinct openings:
  1. **New numerically-robust theta-independent reformulation of L1/L2.**
     Found (via fresh `fsolve`-built configurations, 12+ triangle shapes
     including two obtuse-γ cases, agreement to 1e-4–1e-12):
     $$\angle KBA^* = \angle O'BA = 90^\circ-\gamma \quad\text{(acute-γ regime)},$$
     where `O'` = circumcenter of `ABC` (the same fixed point the builder's
     round-3 report already flagged). This is algebraically equivalent to L1
     (`∠ABA*=θ+90°-γ` when K sits angularly between rays BA, BA*, since then
     `∠ABA*=∠ABK+∠KBA*=θ+(90°-γ)`), but strips out θ, isolating exactly the
     "new" content beyond the classical fact `∠O'BA=90°-γ`. Symmetric fact at
     C: `∠LCA*=∠O'CA=90°-β`. **This is a genuine reformulation, not previously
     recorded as this specific form** (the round-3 file records `∠O'BA*=θ`,
     a *different* relation; both are numerically true and consistent, and
     together say BK, BO' are isogonal in angle `∠ABA*` — see below).
  2. **The correct general (signed-independent) unsigned formula, found by
     testing an obtuse-γ configuration.** `L1` as literally written
     (`∠ABA*=θ+90°-γ`) FAILS as an unsigned equality once γ is large enough
     that `θ+90°-γ<0` (confirmed at `(p,q,θ)=(1.5,0.8,10)`: `γ=122.0°`, so
     `θ+90°-γ=-22.0°`, and the actual unsigned `∠ABA*=22.0054°`, matching
     `|θ+90°-γ|`, NOT `θ+90°-γ`). Tested and confirmed on 5 further genuinely
     obtuse-γ configurations (`γ∈{122°,138°}`, several θ each, residuals
     <1e-8): the correct unsigned identity is
     $$\angle ABA^* = |\theta+90^\circ-\gamma|,\qquad \angle ACA^*=|\theta+90^\circ-\beta|,$$
     and the **geometric configuration flips exactly when the sign of
     `θ+90°-γ` flips**: for `θ+90°-γ>0` (i.e. `γ<90°+θ`), K lies angularly
     between rays BA and BA* as seen from B (additive: `∠ABK+∠KBA*=∠ABA*`);
     for `θ+90°-γ<0` (i.e. `γ>90°+θ`), instead A* lies angularly between BA
     and BK (`∠ABA*+∠A*BK=∠ABK`). **This is a clean, computable, single
     case-split** on comparing `γ` to `90°+θ` (resp. `β` to `90°+θ` at C) —
     it replaces the round-3 builder's unjustified "by symmetry, same sign
     convention" claim (which the reviewer correctly flagged as false/
     unjustified) with an explicit trichotomy that is checkable directly from
     the hypotheses' numeric data, not asserted by fiat. This looks like
     exactly the missing rigor step for the "unsigned angle chase" route.
  3. **Isogonality structure.** Combining finding (1) with the round-3
     file's own finding `∠O'BA*=θ` (`=∠ABK`): together these say
     `∠ABK=∠A*BO'=θ` and `∠ABO'=∠KBA*=90°-γ`, i.e. **rays BK and BO' are
     isogonal conjugates with respect to angle `∠ABA*`** (reflections of
     each other across its bisector). This is a strictly cleaner-looking
     synthetic target than L1 itself — "show BK, BO' are isogonal in
     `∠ABA*`" — but I could not find a mechanism producing it from
     H1∧H2∧H3 in the time available; flagging as a lead, not a proof.

- Candidate technique(s): isogonal-conjugate / reflection-in-angle-bisector
  argument (new, untried); explicit sign trichotomy on `γ` vs `90°+θ` (and
  `β` vs `90°+θ`) replacing directed-angle bookkeeping; the already-certified
  right-angle fact `∠AKA*=∠ALA*=90°` (from `lemmas/antipode-reduction.md`)
  combined with the classical `∠O'BA=90°-γ` "circumcenter isosceles" lemma
  (should be citable from `knowledge_base.md`'s standard circumcenter-angle
  facts, or proved in 2 lines via triangle `O'AB` isosceles with `O'A=O'B`).

- Cheap-kill candidates:
  - **Refuted (do not retry): any 4-point concyclicity among
    `{A,A*,B,C,K,L,M,N}` beyond the two already-known trivial circles**
    (`A,K,L,A*` on Γ itself; `A,M,N,O'` on the circle with diameter `AO'`,
    a completely standard fact — perpendicularity `OM⊥AB`, `ON⊥AC`). I
    brute-force tested all `C(8,4)=70` unordered 4-subsets of
    `{A,B,C,M,N,K,L,A*}` across 5 configurations for concyclicity residual;
    only those two combos vanish in all trials. In particular **`B,K,L,N`
    and `C,K,L,M` are NOT concyclic** (residuals 0.15–0.46 — nowhere near
    zero), ruling out the tempting "the hypothesis angle equalities directly
    encode a cyclic quadrilateral BKLN / CKLM" idea.
  - **Refuted (do not retry): spiral similarity at B sending `(K,A*)↦(O',A)`**
    (or `(K,A*)↦(A,O')`). The angle condition holds (`∠KBA*=∠O'BA`, finding
    1 above) but the ratio condition fails badly: `BK/BO'` vs `BA*/BA` differ
    by 20–70% across 5 tested configurations (e.g. `0.75` vs `0.50`). Same
    refutation pattern as the round-2 "spiral similarity centered at B" already
    on file — angle-only matches are not enough, confirmed independently here
    with a different pairing.
  - A genuine cheap-kill for the outliner: **before attempting a general
    proof of L1, first split on `sign(θ+90°-γ)`** — this single comparison
    (computable from the hypothesis data, no construction needed) determines
    which of the two configuration cases applies, and the round-3 proof's own
    Case-3 degenerate/continuity handling likely still works verbatim once
    this split replaces the false "same sign convention" step.

- Knowledge-base entries to use: check `knowledge_base.md` for a named
  "circumcenter base-angle" or "isogonal conjugate" entry to cite for
  `∠O'BA=90°-γ` (standard fact, likely already listed under circle/triangle-
  center lemmas) and for the Isosceles Triangle Converse (Law of Sines
  argument), both already invoked in the certified round-3 lemma.

- Analogous past problems (cruxes): **none** — `crux_moves_documentation.md`
  states explicitly geometry is *not yet in the crux corpus* ("Not in the
  corpus yet; the problems DB includes geometry problems with solutions, but
  no geometry cruxes have been extracted"), so no crux-move matching is
  possible for this problem; do not force a match.

- Prior progress: `lemmas/antipode-reduction.md` (certified, unchanged):
  `OM=ON ⟺ A*B=A*C`, `A*` = intersection of perpendiculars to `AK` at `K` and
  to `AL` at `L`. `approaches/antipode-perp-bisector.md` round-3 content:
  the reduction `(L1∧L2)⟹A*B=A*C` is essentially sound (trichotomy on sign
  of `90°-α-θ` + isosceles converse + continuity for the degenerate case) but
  its *derivation* of the intermediate directed relations (†),(‡) rests on an
  unjustified/incorrect sign-convention step, per the reviewer. L1, L2
  themselves remain open. This round I did **not** attempt to fix that
  derivation or prove L1/L2 — only scouted for what mechanism could.

- Dead ends (do not retry, confirmed again this round or previously):
  "∠AKB+∠A*KB=270°" identity; L as spiral-similarity center for
  `(B,K)↦(N,C)`; tangency/secant identification of Γ with BC or named
  points; full spiral similarity at B via `∠O'BA*=θ` (ratio fails); local
  Law-of-Sines-in-`ABK` + `∠AKA*=90°` computation alone (A*'s position
  genuinely needs L too, confirmed again — same obstruction as round 2/3);
  **new this round:** any 4-point concyclicity linking A* to B or C via K,L
  beyond the two trivial known circles (tested exhaustively, all 70 combos);
  spiral similarity at B for `(K,A*)↦(O',A)` (angle matches, ratio doesn't).

- Small-case / intuition notes (all labeled CONJECTURE — numerical only,
  not proofs):
  - `∠ABA* = |θ+90°-γ|`, `∠ACA* = |θ+90°-β|` hold to 1e-4–1e-12 precision
    across 12+ tested `(p,q,θ)` triangle/parameter combinations, including
    both acute- and obtuse-γ shapes — strong numerical support that this
    (not the un-absolute-valued L1 as literally written) is the fully general
    unsigned identity.
  - The configuration flip (K between BA,BA* vs A* between BA,BK) is exactly
    governed by `sign(θ+90°-γ)`, confirmed on both sides in explicit test
    cases — conjectured to be provable as a clean, standalone "which side"
    lemma (e.g. via a limiting/continuity argument as θ crosses the critical
    value `γ-90°`, when that value lies in the valid range `(0,min(β,γ))`,
    which requires `γ>90°`), rather than needing directed-angle machinery.
  - Suggest to the outliner: **switching the whole L1/L2⟹A*B=A*C reduction
    to purely unsigned angles, with this explicit `sign(θ+90°-γ)` /
    `sign(θ+90°-β)` trichotomy replacing the directed-angle derivation of
    (†),(‡), looks like a concrete, checkable way to eliminate the sign-error
    risk class** that broke round 3's write-up — at the cost of needing this
    one extra (currently only numerically-verified) case-split fact proved
    rigorously, plus the existing continuity argument for the boundary case
    `θ+90°-γ=0` exactly as γ≈90°+θ. This has not been attempted as a full
    proof; it is a scouted opening only.
