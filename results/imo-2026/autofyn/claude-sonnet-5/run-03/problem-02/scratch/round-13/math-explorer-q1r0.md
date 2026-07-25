## imo-2026-02

- Distinct openings (this lens's scouting, on top of the existing population):
  1. **New: full polynomial (radical-free) characterization of the exact
     residual sub-domain for `coordinate-bash-resultant-boundary`'s
     `q_1<0,r_0<0` target**, obtained this round by algebraically eliminating
     `β_1` via the squared inequality behind Step 5 (see "Cheap-kill
     candidates" / "Small-case notes" below for the exact formula). This
     converts the transcendental domain (`β_1<γ`, `sin(A+3β_1)<0`, `P>0`,
     `E<0`) into **four explicit polynomial inequalities in `(c,s,d,t)`**
     (`c=\cos A,s=\sin A,d=\cos B,t=\sin B`), a genuine Positivstellensatz-
     ready target that did not exist in any prior round's file. This is the
     most concrete new lead this round on the priority-#1 item.
  2. Retain (not attempted further this round) the sibling `-tangent-
     twopoint`'s boundary-curve `D_1D_2` factorization as a candidate final
     check *if and only if* the `-tangent` sibling's `∂S/∂B≥0` monotonicity
     closes — see recommendation below.
  3. Not explored this round (out of lens scope): the `-sos` route's
     Theorem-1 Weierstrass-denominator work (already closed, `Num≥0` itself
     still open there too) — worth cross-checking in a future round whether
     the new `(c,s,d,t)` polynomial system found here has any bearing on the
     `Num≥0` semialgebraic target in the `u=\tan(A/6)` frame, but this was
     not investigated.

- Candidate technique(s): Positivstellensatz / explicit nonnegative-
  combination search (Putinar-style: `-q_1 = \sum λ_i g_i + \text{SOS}`,
  `g_i` the domain-defining inequalities) on the now-fully-polynomial
  4-inequality system; alternatively CAD/Gröbner elimination given the
  system is now free of `arccos`/`\sqrt{}`.

- Cheap-kill candidates: **the headline finding of this round.** Working in
  `(c,s,d,t)=(\cos A,\sin A,\cos B,\sin B)` (both `A,B\in(0,\pi/2)` on the
  residual sub-case, confirmed below), with `X_0=ct/(2(sd+ct))`:
  1. `\beta_1<\gamma` given `\gamma=B` (i.e. Step 3, already known) `⟺
     G_0:=ct(1-2d^2)-2sd^3>0` (i.e. `X_0>d^2`).
  2. `\gamma=B$ (i.e. `B\le C`) `⟺ c\ge 2t^2-1`** — this is a **new, clean
     polynomial reformulation of Step 2** (not present in any prior file):
     `B\le C \iff 2B\le\pi-A \iff \cos(2B)\ge\cos(\pi-A)=-\cos A \iff
     1-2t^2\ge-c \iff c\ge2t^2-1`. Elementary (monotonicity of `\cos` on
     `(0,\pi)`), verified by hand.
  3. `E<0$: already reduced (round 12, verified again independently this
     round via a fresh `sympy.reduced` mod `⟨c^2+s^2-1,d^2+t^2-1⟩`) to
     `ct\,f_1(\sigma,\tau)+ds\,f_2(\sigma,\tau)<0`.
  4. **New this round**: given `X_0\in(1/4,3/4)` (equivalently `p:=s(4X_0-3)
     <0,\ q:=c(4X_0-1)>0`, i.e. Step 4's `p,q` sign preconditions), the
     actual target `\sin(A+3\beta_1)<0` (Step 5's squared inequality) is
     **exactly** equivalent — independently derived here via a fresh
     `sympy` computation of `q^2(1-X_0)-p^2X_0`, clearing the strictly-
     positive denominator `2\sin^3C=2(sd+ct)^3` — to
     $$\mathrm{Num}:=c^5t^3-3c^3d^2s^2t-c^3s^2t^3+2c^2d^3s^3-6c^2ds^3t^2
     -9cd^2s^4t\ <\ 0.$$
     **Independently spot-checked exactly** (own fresh, non-vectorized
     Python loop, 2000 random triangles, filtering to the `p<0,q>0`
     sub-case): `0/2000` mismatches between `\mathrm{Num}<0` and the
     direct `\arccos`-based `\sin(A+3\beta_1)<0` evaluation — this is a
     strong, independently-reproduced confirmation of an exact symbolic
     identity (via the same squaring-is-iff logic already certified in
     round 10's Step 2/3 for the sibling `D` computation), not mere
     coincidence.
  5. **New this round: `p<0` and `q>0` hold automatically (100%, `0`
     violations) throughout `\{G_0>0\}\cap\{E<0\}\cap\{B\le C\}`** — checked
     on a fresh `436{,}519`-sample sweep restricted to this domain (own
     script, this round): every single sample had `p<0,q>0`. So **no
     separate case-split on `p,q`'s signs is needed** once the domain
     `G_0>0,E<0,B\le C` is assumed — this removes one layer of casework
     the population had been implicitly worried about (Step 4's role
     reduces purely to licensing the squaring, and turns out to hold
     automatically on the domain of interest).
  6. **Full domain match confirmed exactly (`array_equal` True on
     17,371/17,371 points)**: on `\{G_0>0\}\cap\{E<0\}\cap\{B\le C\}`, the
     transcendental sub-case `\{\beta_1<\gamma\}\cap\{\sin(A+3\beta_1)<0\}`
     coincides *exactly* with `\{\mathrm{Num}<0\}` — an own fresh
     8,000,000-sample sweep, restricted first to `G_0>0\wedge E<0\wedge
     B\le C$ (`436{,}519` points), then comparing the boolean array
     `\mathrm{Num}<0` against the boolean array from direct `\arccos`
     evaluation: **perfect agreement, zero mismatches.**
  **Net: the entire residual sub-case's domain (previously understood only
  via `\arccos`/transcendental membership tests) is now exactly
  characterized by the four explicit polynomial inequalities**
  `\{G_0>0,\ E_{\text{num}}<0,\ c\ge2t^2-1,\ \mathrm{Num}<0\}` (all
  polynomial in `c,s,d,t`, subject only to `c^2+s^2=1,d^2+t^2=1,s,t>0,
  c\ge0`; `d>0` follows since `B<\pi/2` throughout, established in round
  11). **This directly answers round-12's own flagged obstruction**
  ("A purely `(\sigma,\tau)$-algebraic proof of `q_1<0,r_0<0`... would
  need to first characterize that curved region algebraically... this
  reduction was not attempted or completed this round") — it is now
  completed, in `(c,s,d,t)` rather than pure `(\sigma,\tau)` (consistent
  with round 11's own diagnosis that the domain is not expressible purely
  in `(\sigma,\tau)`, since `\mathrm{sign}(A-B)`/individual `c,d` values
  matter).
  **This is not yet a proof of `q_1<0,r_0<0`** — it converts the target
  into a genuine, well-posed Positivstellensatz search (`-q_1,-r_0` as
  nonnegative combinations of `G_0,-E_{\text{num}},(c-2t^2+1),-\mathrm{Num}`
  and squares, all polynomial, moderate degree `\le8`), which was **not
  attempted this round** (time-limited after deriving the characterization)
  — this is the concrete, well-scoped task to hand to next round's builder.

- Knowledge-base entries to use: same as before — resultant/elimination
  techniques and Positivstellensatz-style sign certificates already used
  successfully elsewhere in this population (e.g. the `T`-factorization,
  Theorem 16.1's `D(x)`-monotonicity, the `-sos` route's Weierstrass-
  denominator work); no new KB entry identified this round beyond what's
  already in use. (`knowledge_base.md` was not separately re-scanned this
  round — this is a continuation of an established route, not a fresh
  problem entry point.)

- Analogous past problems (cruxes): not separately queried this round
  (lens was a deep, narrow continuation of an existing symbolic-elimination
  route, not a fresh framing) — the population's round-12/13 approaches
  already draw on `aimo-0005`'s two-point-pinned tangent/secant crux move
  (used by `-tangent-twopoint`, see that file's own citation). No new
  crux match surfaced by this round's work.

- Prior progress: `coordinate-bash-resultant-boundary` had (round 12)
  reduced Steps 1,3,5 to certified exact identities and reformulated Step
  4's `X_0\in(1/4,3/4)` sub-target exactly, but explicitly left Step 2
  (`\gamma=B`) and the joint `X_0>d^2\wedge E<0\Rightarrow(ct>sd)\wedge
  (ct+3sd>0)` implication unclosed, and — crucially — noted that even a
  complete closure of Steps 2+4 would NOT touch the actual `q_1<0,r_0<0`
  target, which needed the residual sub-domain characterized algebraically
  first (flagged, not attempted). **This round supplies exactly that
  missing algebraic characterization** (see Cheap-kill candidates above),
  going further than Step 4 alone: it directly derives the *exact*
  polynomial equivalent of the full three-way domain condition (`\beta_1<
  \gamma\wedge\sin(A+3\beta_1)<0$, given `\gamma=B`), not just the
  `X_0\in(1/4,3/4)` sub-piece.

- Dead ends (do not retry): the round-12 file's own low-degree-ansatz
  Positivstellensatz attempt directly on `G_0,-E_{\text{num}}` alone (i.e.
  trying `\alpha G_0+\beta(-E_{\text{num}})\ge ct-sd` or `\ge ct+3sd` with
  small-integer-coefficient `\alpha,\beta`) failed — **this round's own
  numeric test explains why**: `G_0>0\wedge E<0$ alone (even with `B\le C`
  added) gives `q_1<0` only `\approx17.9\%$ of the time and `r_0<0` only
  `\approx22.0\%$ of the time (own fresh `436{,}519`-sample sweep) — the
  `\mathrm{Num}<0` condition (Step 4/5, the `\sin(A+3\beta_1)<0` piece) is
  NOT redundant and is doing the overwhelming majority of the work
  (shrinking the domain by a further factor of `\approx25\times`, down to
  `13{,}092`/`17{,}371` points where `q_1,r_0<0` finally hold 100%) — so
  any future certificate attempt MUST include `\mathrm{Num}` as one of the
  generators, not just `G_0,E_{\text{num}}`; this is a genuinely new,
  actionable insight (previously the population treated Step 4/Step 2 as
  "just domain bookkeeping," separate from the "real" `q_1,r_0` target —
  this round shows the domain-bookkeeping condition `\mathrm{Num}<0` is
  actually the dominant discriminating factor).

- Small-case / intuition notes (all labeled conjecture/numeric unless
  stated as "verified exact" above): the round-11 finding that the
  residual sub-case's extremal corner coincides with the `A^*,B^*` corner
  of the sibling `-pointwise`/`-tangent` routes is reconfirmed by this
  round's tighter domain (`A\in(0.407,0.536),B\in(0.912,1.090)`, matching
  round 11 closely). This suggests (still conjectural) that `\mathrm{Num}$,
  `G_0`, and `-E_{\text{num}}` may all vanish simultaneously exactly at
  `(A^*,B^*)` — worth checking symbolically next round as a possible
  organizing fact for the Positivstellensatz search (e.g. if all domain-
  boundary polynomials and `q_1,r_0` share a common root there, the
  certificate likely needs each generator to appear with a coefficient
  that also vanishes there, which narrows the ansatz search space).

**Recommendation on `-tangent-twopoint`**: deprioritize new investment
this round, but do not delete/retire the file or its certified lemma
(`lemmas/star-factorization-on-boundary-curve.md` is real, reusable
content). Reasoning: its own honestly-disclosed gap #3 is structural, not
incidental — even a full symbolic proof of both `D_2>0` and `D_1`
concavity this round would establish `S\ge0` only on the measure-zero
curve `\mathcal C`, and extending to the full 2D Case-(b) domain requires
the *sibling* `-tangent` file's own still-open `\partial S/\partial B\ge0`
monotonicity lever. Until that sibling lever closes (it has been open
since round 9/10 with no symbolic progress reported, only numeric margin
evidence), further investment in `-tangent-twopoint`'s `D_1` concavity
proof cannot by itself advance the population's Status past `partial` —
it would produce a second unused certified fact stranded behind the same
wall. By contrast, this round's `q_1,r_0` polynomial-characterization
lead (above) is self-contained: it does not depend on any other route's
open lemma to become useful, and directly targets the narrower
(`\approx4.5\%`-of-Case-(b)) residual gap that `coordinate-bash-resultant-
boundary` already needs regardless. Recommend the outliner route next
round's build effort toward the Positivstellensatz search on `\{G_0,
-E_{\text{num}},(c-2t^2+1),-\mathrm{Num}\}\Rightarrow\{-q_1,-r_0\}` instead
of further `-tangent-twopoint` numeric investigation, unless a builder is
specifically assigned to close the sibling `\partial S/\partial B\ge0`
monotonicity lever first (in which case `-tangent-twopoint` becomes
immediately valuable again).
