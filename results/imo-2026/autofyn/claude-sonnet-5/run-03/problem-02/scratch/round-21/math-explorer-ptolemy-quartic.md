## imo-2026-02 (lens: resolvent quartic root-count proof)

### What I did
Re-derived Round 8's four-branch resolvent quartic `P(t)` from scratch
(fresh `sympy`/`mpmath`, independent of the approach file's script), using
the exact `(III)',(IV)'` quadratic coefficients `a1,b1,c1` (in `\psi`) and
`a2,b2,c2` (in `\varphi`) from `approaches/ptolemy-trig-identity.md` Step 2
(Round 3/4), and the boxed target `F(p,x,y)=\sin A(p+2x)(p+2y)-\sin A-\cos
A(2p+2x+2y)` from Round 4 Step 1. Ran a much larger sample sweep (1100
samples total, `mpmath dps=30`, uniform random valid `(A,C,\theta)` with
`\theta\in(0,\min(B,C))`) and attempted a genuine symbolic root-count proof
via the quartic's Vieta-coefficient / resultant structure.

### Distinct openings
1. **Confirmed at scale (1100/1100 samples, zero exceptions)**: the "3
   negative + 1 positive real root" pattern for `P(t)` holds, and the
   positive root's branch is *always* the specific sign combination
   `(s_1,s_2)=(+,+)` in my own labeling (a labeling convention, not
   necessarily matching the approach file's `(-,-)`; the substantive fact —
   there is exactly one uniformly-consistent positive branch — matches).
2. **New structural finding (proved, not just observed): `P(t)` factors
   exactly into two real quadratics via Vieta grouping by the sign of the
   `U:=\cot\alpha`-branch** (`s_1`, i.e. group by which root `x=\cot\psi`
   is used, holding it fixed while the other radical `y=\cot\varphi`
   ranges over its two roots). Concretely, since `F` is affine in `y` for
   fixed `x` (equivalently affine in `V:=p+2y` for fixed `U:=p+2x`),
   $$P(t) = Q_{U_+}(t)\cdot Q_{U_-}(t), \qquad Q_U(t):=\bigl(t-F(U,V_+)\bigr)\bigl(t-F(U,V_-)\bigr) = t^2 - S(U)\,t+\mathrm{Pr}(U),$$
   with `S(U):=F(U,V_+)+F(U,V_-)`, `\mathrm{Pr}(U):=F(U,V_+)F(U,V_-)`, both
   explicit **quadratics in `U`** (no more `y`-radical) via Vieta on the
   `V`-quadratic — this is an exact algebraic identity, verified by direct
   expansion (own `sympy`) and confirmed numerically at every sample.
3. **This reduces the whole 4-branch root-count claim to exactly two
   independent, much smaller 2-branch claims** (confirmed numerically,
   1100/1100, zero exceptions, at a *finer* grain than the raw quartic
   claim):
   - (a) For `U=U_{\text{genuine}}` (the branch containing the genuine
     `F>0` value): `\mathrm{Pr}(U)<0` — i.e. the two `y`-branch values of
     `F` at this fixed `U` have **opposite sign**. This alone forces `Q_U`
     to have one positive and one negative real root, **regardless of the
     sign of `S(U)`** — a single scalar-sign condition, strictly simpler
     than the full quartic claim.
   - (b) For `U=U_{\text{spurious}}` (the other branch): `\mathrm{Pr}(U)>0`
     **and** `S(U)<0` — forcing both roots of `Q_U` negative (real, same
     sign by `\mathrm{Pr}>0`, and that sign is negative by `S<0`).
4. **Traced `\mathrm{Pr}(U)` to the same resultant-elimination machinery
   as the certified `\Psi(\tau,A,C)` sextic** (`lemmas/ptolemy-resultant-
   elimination-to-sextic.md`): writing `F=mV+n` with `m:=\sin A\,U-\cos A`,
   `n:=-\cos A\,U-\sin A` (i.e. the certified lemma's own `m,n` but with
   the `-4` shift removed — the lemma's target is `F=4`, threshold `4`;
   `\mathrm{Pr}(U)` is the *same* construction at threshold `0`), Vieta on
   the certified `\tilde P_2V^2+\tilde Q_2V+\tilde R_2` gives
   `\mathrm{Pr}(U)\cdot\tilde P_2 = \Phi_0(U):=\tilde P_2n^2-\tilde
   Q_2nm+\tilde R_2m^2` (i.e. exactly the certified lemma's `\Phi(U)` with
   the threshold shift undone). Consequently `\mathrm{Res}_U(\tilde
   P_1U^2+\tilde Q_1U+\tilde R_1,\ \Phi_0(U))` is, by the *identical* proof
   technique as the certified lemma (same two spurious linear factors
   `\theta=B,C`, same degree-6-ish sextic residue after removing them),
   a sibling polynomial `\Psi_0(\tau,A,C)` — computed the raw resultant
   symbolically (own fresh `sympy`, degree up to `\tau^8` before removing
   spurious factors, matching the expected shape). **This is the honest,
   load-bearing finding of this round**: the "new" resolvent-quartic route
   is not actually independent of, or easier than, the population's
   already-open `\Psi>0` sextic — it reduces to a *sibling* resultant
   construction of the exact same type and (based on the raw resultant's
   size) comparable or greater algebraic complexity, using the same
   certified machinery just at a different threshold constant.

### Candidate technique(s)
Descartes'/Sturm attempted directly on the raw quartic's 5 coefficients
`(1,-4R,e_2,-e_3,e_4)`: **not tractable** — `R,e_2,e_3` do not have a
uniform sign across the domain (confirmed: `R<0` at 2/8 of Round 8's own
sample points), so Descartes' rule of signs gives no clean bound without
first pinning signs region-by-region. The Vieta-grouping decomposition
above (item 2) is a genuine simplification in *structure* (4-root claim →
two independent 2-root claims), but does not by itself yield a proof:
claims (a) and (b) above are each reducible (via item 4) to the sign of a
sibling degree-6-ish sextic in `\tau`, i.e. exactly the same order of
difficulty as the already-20-round-open `\Psi>0`. No simpler technique
(SOS, direct trig identity) was found or attempted symbolically to
completion this round for `\mathrm{Pr}(U)`'s sign — this is the concrete
next target if this route is pursued further, but it should not be
expected to be easier than `\Psi>0` itself.

### Cheap-kill candidates
None found that shortcut the sign proof. One useful cheap fact: claim (a)
above (`\mathrm{Pr}(U_{\text{genuine}})<0`) is a *single* scalar-sign
condition (not requiring the extra `S(U)<0`/`\mathrm{Pr}(U)>0` conjunction
needed for the spurious branch) — if a future round wants to attack this
route, (a) is the cheaper of the two remaining pieces to try first.

### Knowledge-base entries to use
No new entries beyond what the existing route already cites (resultant
elimination / Vieta on quadratics, IVT for branch selection). This is a
pure elimination-theory computation; `knowledge_base.md`'s general
symmetric-function / resultant techniques (already in use by this whole
approach) are the relevant class, no sharper tool identified.

### Analogous past problems (cruxes)
Did not find a genuinely new crux-corpus match this round (this is a
narrow, problem-specific elimination-theory sub-question); the existing
approach file already draws on standard resultant/Vieta technique, not a
named crux move. No new match to report.

### Prior progress
- `lemmas/ptolemy-resultant-elimination-to-sextic.md` (certified): the
  degree-6 `\Psi(\tau,A,C)` sextic, `\Psi>0` still open (numeric-only,
  20,000+ samples zero violations).
- `approaches/ptolemy-trig-identity.md` Round 8 (partial, no overclaiming):
  four-branch resolvent quartic `P(t)` constructed and verified as an exact
  Vieta identity; "3 negative + 1 positive root" pattern reported as
  numeric-only (8 samples).
- **This round's addition**: (i) confirmed the root pattern at 1100 samples,
  zero exceptions; (ii) proved the quartic factors into two real quadratics
  by `U`-branch grouping (an exact algebraic fact, not numeric); (iii)
  traced the resulting two sub-claims to a sibling sextic `\Psi_0` built via
  the *same* certified resultant machinery as `\Psi`, at a different
  threshold — establishing that this route is not a shortcut around `\Psi>0`,
  just a re-parametrization of a problem of the same difficulty.

### Dead ends (do not retry)
- **Direct Descartes'/Sturm on the raw quartic's 5 coefficients**: not
  viable without first pinning down region-by-region signs of `R,e_2,e_3`,
  which are not uniformly signed — confirmed this round, matches Round 8's
  own partial finding (`e_4<0` alone insufficient to pin the root pattern).
- **Treating the resolvent-quartic route as independent of/easier than
  `\Psi>0`**: this round's finding (item 4 above) shows it reduces to a
  sibling sextic of the same construction — do not dispatch future rounds
  on this route expecting an easier win than `\Psi>0` itself; if pursued,
  it should be pursued *as* an attack on `\Psi`-type sextics generally
  (e.g. a genuinely different technique — SOS/Positivstellensatz search,
  or a direct geometric/trigonometric argument for `\mathrm{Pr}(U)<0`
  rather than resultant elimination), not as a "cheaper" alternative target.

### Small-case / intuition notes (all conjectural / numeric)
- The "3 negative + 1 positive" pattern for `P(t)` holds with substantial
  numeric margin at every one of 1100 random samples (positive root always
  much larger in magnitude, matching Round 4's own diagnostic that the
  genuine branch's `F` is typically far above the spurious branches').
- The finer `U`-branch-grouped pattern — genuine-`U` group gives mixed
  signs, spurious-`U` group gives both negative — also holds with zero
  exceptions at 1100 samples, and is *equivalent* (via the exact
  factorization) to the quartic's root pattern, not merely correlated with
  it.
- This strongly suggests the true underlying fact is Round 4's original
  diagnostic dichotomy ("(genuine,genuine) branch always gives `F>0`; every
  other of the 3 spurious sign combinations always gives `F<0`") — a fact
  open since round 4 (17 rounds ago) — and the resolvent-quartic
  construction is a reformulation of that same fact via Vieta, not a new
  independent target. Recommend the outliner treat `\Psi>0` (or
  equivalently this branch-sign dichotomy) as the single true bottleneck
  for this whole `ptolemy-trig-identity` route, and consider it in the
  same "shared-gap plateau" category as the coordinate-bash cluster's
  Case-(a) gap — both are long-standing (17+ and multi-round respectively)
  polynomial-positivity claims resistant to pure elimination-theory
  pressure, suggesting a genuinely different technique (SOS/Positivstellensatz
  certificate search, or synthetic/geometric reformulation) is needed
  rather than further resultant restructuring.
