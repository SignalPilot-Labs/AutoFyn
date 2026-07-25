# Build report — coordinate-identity (imo-2026-02), round 1

**Status: solved.** Full rigorous proof written to
`results/imo-2026-02/approaches/coordinate-identity.md`.

## What closed the problem
The heavy-bash worry (reviewer's caveat) evaporated because the two secondary angle
conditions **decouple**. After writing K−B=u·e^{−iθ}(A−B), L−C=v·e^{iθ}(A−C) (u=λ_K,
v=λ_L>0), the positive ray-length factor cancels out of each condition:
- ∠LBK=∠LNC ⟺ FL(v)=0, a quadratic in v ONLY (no u).
- ∠LCK=∠BMK ⟺ FK(u)=0, a quadratic in u ONLY (no v).

So K and L are pinned independently. The target OM=ON reduces (equal-height M,N; power of
a point) to a single scalar T:=det1−(M_x+N_x)det2=0, and the payoff is an **exact
polynomial identity**
    a_K·a_L·T = a_L·QK·FK + QL·FL     in ℤ[a,p,q,h,c,s,u,v],
verified by full expansion to residual 0 — NOT a numeric check. No c²+s²=1 relation is
even needed (the remainder R2 came out exactly 0). Branch selection (the reviewer's other
caveat) is a non-issue: T vanishes at BOTH roots of each quadratic (confirmed both by the
ideal identity and by evaluating at all 4 root combinations).

## Rigor handling of the two flagged caveats
1. GAP-2 "must be a written identity, not sympy-returned-0": delivered as the explicit
   pseudo-division identity (8a),(8b),(8) — an equality of polynomials the reader expands
   by hand; scripts merely regenerate the cofactors.
2. GAP-1 "closed form / which root": the decoupling makes each unknown a single quadratic;
   since T vanishes for both roots, no root selection is required. The only degeneracy is
   the leading coefficient a_K·a_L = −¼|AB|²|CA|²W² with W a nonzero sinusoid in θ,
   vanishing at isolated θ; those isolated θ are closed by continuity of T along the
   connected admissible family.

## Spec concerns / minor caveats for the reviewer
- **Orientation of the directed-angle equalities (4),(6).** The hypotheses give the
  *unsigned* equalities ∠LBK=∠LNC etc.; I use the *directed* versions. Justification: the
  interiority hypotheses ("K inside ∠LBA", "L inside ∠ACK", K∈△BMC, L∈△BNC) fix the
  orientation, preserved on the connected family (a flip needs an excluded collinearity),
  and the numerical model confirms the directed equality holds throughout. This is the one
  step that leans on the configuration rather than pure algebra; it is standard and, I
  believe, airtight, but it is the place a picky reviewer would look. Everything downstream
  is an exact polynomial identity.
- The proof is coordinate/analytic and genuinely distinct from pow-reduction-trig (which
  avoids O) and the synthetic routes.

## sympy scripts (reproducible, exact rational arithmetic)
- `/tmp/num.py` — numerical model: parametrisation, directed-angle equalities,
  interiority, 2·O_x=M_x+N_x (≤1e-13 across the family).
- `/tmp/sym5.py` — EA=u·FL, EB=v·FK (decoupling).
- `/tmp/clean.py` — the exact identities a_K·T=QK·FK+R1, a_L·R1=QL·FL (R2=0),
  a_K·a_L·T−(a_L·QK·FK+QL·FL)=0.  ← the load-bearing certificate.
- `/tmp/final.py` — leading-coefficient factorisations (7); root-combination cross-checks.

## Promotable lemmas
- Equal-height circumcentre reduction (OM=ON ⟺ det1=(M_x+N_x)det2 when M_y=N_y).
- Decoupling lemma (the two secondary conditions determine K, L independently) — likely
  useful to the other approaches.
