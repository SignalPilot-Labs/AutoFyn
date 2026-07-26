# imo-2026-02 — proof-builder: antipode-rightangle (round 2)

## Outcome
Status: **partial**. Three load-bearing corrections to the round-1 file plus a coordinate reformulation of the crux as an explicit, numerically-verified polynomial identity (T'). The symbolic CAS certificate did NOT terminate in the round budget. Written to `results/imo-2026-02/approaches/antipode-rightangle.md`.

## What was proved this round (rigorous)
1. **SIGN BUG in (C1),(C2) fixed.** Round 1 used directed angles `sin(α+γ−C)`, `sin(α+β−B)`. The directed-angle sine rule yields SIGNED lengths; on the inside-hypothesis branch (`α+γ<C`, `α+β<B`) these are the NEGATIVE of the positive `(K-pos)`/`(L-pos)` lengths. The corrected constraints use INTERIOR angles:
   - `(C1): 2 sin A sin(C−α−γ) sin(α+γ) = sin C sin γ sin(A+2α+γ)`
   - `(C2): 2 sin A sin(B−α−β) sin(α+β) = sin B sin β sin(A+2α+β)`
   Both verified to ~1e-16 across 7 hand-checked configs; round-1's signed versions differ by an overall minus on every config. (This is the same numpy-sign-trap class the round-2 rules warned about; it had infected the intermediate (C1)/(C2) formulas, though not the final (T), which round 1 verified by direct coordinate computation.)

2. **(R1) is a TRIG IDENTITY, not a constraint.** Symbolically confirmed: `expand_trig` of (R1)'s `sin k`/`cos k` coefficients (after `C=π−A−B`) is identically zero. (R1) = composition of three always-true sine rules in `△ABK,△ABL,△AKL`; it holds for any K on the α-ray and any L on the (α+β)-ray, carries NO info on `k=dir(KL)`. The round-1 gap formulation "derive (T) from (R1)+(C1)+(C2)" is therefore MIS-STATED — (R1) is vacuous. The real determinants of k (hence of (T)) are the incidence constraints (C1),(C2) + the coordinate relation `tan k=(Ly−Ky)/(Lx−Kx)`.

3. **Coordinate reformulation (T').** Substituting explicit coordinate expressions for `sin u,cos u,sin(A−w),cos(A−w),sin k,cos k` (clearing `1/(|KL||AK||AL|)`) reduces (T) to the explicit trig-polynomial identity (T') in five variables `A,B,α,γ,β` (with `C=π−A−B`):
   `cos C·(M−|AK|²)·Lfac = cos(C+β)·(cos α−par)·(|AL|²−M)`, with all quantities explicit (Section 7 of approach file). This is a single, machine-checkable polynomial target.

4. **Numerical certainty.** (T') verified to max residual `5.4e-13` across 47 random configs (7 hand-checked + 40 random; scalene/isoceles/obtuse/tall triangles; `α∈[0.1,0.4]`).

## The gap (precisely located)
The single unproved step: certify that the numerator of (T') (after Weierstrass `t_x=tan(x/2)` substitution + denominator-clearing) lies in the ideal `⟨(C1)_num,(C2)_num⟩` over `Q(t_A,t_B,t_α)[t_γ,t_β]`. Natural certificate: sequential field-reduction — reduce `(T')_num` mod `(C1)_num` over `Q(t_A,t_B,t_α,t_β)[t_γ]`, then mod `(C2)_num` over `Q(t_A,t_B,t_α,t_γ)[t_β]`; expected remainder 0.

**Why the CAS did not terminate:** the coordinate numerators are degree ~6 in each of `t_γ,t_β` with ~10⁴–10⁵ monomials after `expand_trig`. Three CAS strategies all timed out within the round budget:
- 10-variable Gröbner (sin/cos vars + unit circles, `grevlex`) — timed out at 120s.
- 5-variable Gröbner (Weierstrass `t_A,t_B,t_α,t_γ,t_β`, `lex`) — timed out at 120s.
- Weierstrass substitution + sequential field-reduction — the `expand_trig`+`xreplace`+`expand` step itself timed out at 300s (the unexpanded coordinate expression is too large for sympy to expand).

The reformulation (T') gives a single explicit polynomial target that a dedicated algebra system (or sympy with manual piecewise polynomial reduction / `grevlex` + careful variable ordering) should close. This is a write-up/termination task on a numerically-certain identity, not a new-mechanism task.

## Spec concerns
- The round-2 dispatch mandated "route (a) trig-Ceva cancellation on the (C) system" and asserted identity (T) follows from (R1)+(C1)+(C2). The mandate's dependency is WRONG: (R1) is an identity (vacuous), so (T) does NOT follow from `(R1)+(C1)+(C2)` in the sense the mandate intended — (R1) contributes nothing. The correct dependency is `(T) follows from (C1)+(C2)+coordinate-relation-for-k` (equivalently, the reformulated (T') vanishes mod {(C1),(C2)}). The approach file is updated to reflect this; the round-3 outliner should be told the closing target is (T') mod {(C1),(C2)}, NOT (T) from (R1)+(C1)+(C2).
- The round-1 approach file's (C1),(C2) had a SIGN BUG (directed vs interior angles). Any other approach that imported the round-1 (C1)/(C2) (e.g. `power-secant-product` if it touched them) should re-derive with interior angles. The corrected lemmas are in the `Promotable lemmas` section.
- The theorem is PROVEN this round by the parallel `analytic-branch-cert` approach (saturation identity, independently verified by the outline-reviewer). Since `OM=ON ⟺ (T)` is rigorous (Section 5 of this approach), identity (T) is TRUE; the open task here is a DIRECT derivation within the antipode framing (the (T') certificate), not a question about the theorem's truth. If `analytic-branch-cert` certifies `OM=ON` into `lemmas/`, the antipode approach can import it to close (T) immediately via the Section-5 equivalence — but that makes this approach dependent on the analytic one rather than a standalone synthetic proof.

## Files touched
- `results/imo-2026-02/approaches/antipode-rightangle.md` — rewritten with corrected (C1),(C2), the (R1)-is-identity finding, the (T') reformulation, and the precisely-located CAS-certification gap. `.ranking.json` NOT touched (per rules).
