# Proof builder — `analytic-branch-cert` (round 2)

## Outcome
**Status: solved.** The full proof is written to `/home/agentuser/repo/results/imo-2026-02/approaches/analytic-branch-cert.md`.

## What I verified from scratch (independent re-derivation)

The dispatch's headline mandate was to NOT trust prior rounds' verification and re-derive the saturation identity myself. I did:

1. **Rebuilt `e1, e2, e3, Q`** from the cross/dot tangent form (†) in sympy from scratch (script `/tmp/verify_sat4.py`, the reviewer's, re-run; plus my own `/tmp/verify_G.py`, `/tmp/verify_ce.py`, `/tmp/verify_inside.py`).
2. **Field division over `Q(b,u,v,lx,t)[ly]`** (NOT ring pseudo-remainder): `sp.div(Poly(Qt2·e3_line − et2·Q_line, ly, domain=QQ.frac_field(b,u,v,lx,t)), Poly(D₀, ly, domain=...))` returns **remainder `0`** with an **explicit quotient `G` linear in `t`** (degree 1). Confirmed by the round-2 reviewer AND by my independent run.
3. **Derived a clean factored form of `G`**:
   `G = (b⁴·v·|C|²/4)·{ t·[|C|²·(3b²+b·lx−b·u) − 3·b²·(lx·u+ly·v)] + [b²+b·lx−b·u − 3·lx·u − 3·ly·v + 2·|C|²] }`
   and confirmed `LHS − D₀·G_prop ≡ 0` by direct symbolic simplification (`sp.simplify == 0`). This is a polynomial identity in `Q[b,u,v,lx,ly,t]`.
4. **Recomputed the round-1 "counterexample"** at `b=4,u=1,v=3,lx=1/2,ly=7/2,t=1/3`: the cleared target `Q` from its defining formula (Q) is **`320/3`**, NOT `256` (the round-1 slip). With the corrected `Q`, the full polynomial-in-`t` `Qt2·e3 − et2·Q` is identically `0` at this `(b,u,v,lx,ly)` — exactly as the saturation identity predicts at a `D₀=0` point. (Note: this point has `ly=7/2 > v=3`, so it is NOT inside `△BNC`; `et2=−80<0` there. It is irrelevant to the theorem but confirms the polynomial identity.)
5. **Inside-arc sampling** (117 valid configurations satisfying ALL inside hypotheses, with `K ∈ △BMC`, `L ∈ △BNC`, `D₀=0`, `e3=0`): `max|Q| ≤ 1.4e-10`, `max|OM−ON| ≤ 2.1e-6` (numerical root error), `min et2 = 0.09 > 0`. The theorem and `et2>0` on the inside arc both confirmed.
6. **Lemma-3 relation** by direct subtraction: `et2 − ((b³/2)|C|²(v−ly)|L−C|² − b²·D) ≡ 0` over the field.
7. **Complex reformulation** of `D₀`: `Im[(L−N)/((L−B)(L−C))] = −D₀(L)/(2·|L−B|²·|L−C|²)`, so `D₀=0 ⇔ (L−N)/((L−B)(L−C)) ∈ ℝ`. (The explorer's "D₀/2" was off by a sign; the equivalence still holds.)

## Why the round-1 "FALSE" verdict was wrong

Round 1 evaluated `Q` at the alleged counterexample point and got `Q = 256`; recomputing from the defining formula (Q) with `K=(8/3,8/3)`, `L=(1/2,7/2)` gives `Q = 320/3`. The slip fed a nonzero LHS, which round 1 then (mis-)interpreted as "saturation identity false" + "field-remainder nonzero." Both the corrected point-evaluation AND the from-scratch field-division (remainder 0, explicit G) confirm the identity is TRUE. The round-1 reproducibility note's claim to have run the field-domain check and gotten nonzero was contaminated by the same wrong `Q` value.

## Spec concerns / residual notes

- None that block the proof. The saturation identity is verified by two independent methods (true field division returning remainder 0 with explicit G; AND direct symbolic simplification of `LHS − D₀·G_prop`), plus point-evaluation at the (corrected) round-1 counterexample. The proof deploys the hypotheses `K≠B` (strict `K∈△BMC`), `L∈△BNC` strictly (gives `ly<v`, `L≠C`, hence `et2>0`), `e3=0` (third angle), and `det(K,L)≠0` (circumcentre exists). The hypotheses `K∈∠LBA`, `L∈∠ACK` are ordinary-angle branch-selection conditions; they are not separately needed because the directed-angle encoding `e1=e2=e3=0` (which ordinary angles imply) plus the strict inside-arc conditions already give the full algebraic implication. This is a valid use of a subset of hypotheses.
- The proof is parameter-free over `Q[b,u,v,lx,ly,t]`, so it holds for every non-degenerate triangle (`b>0, v>0, |C|²>0`) simultaneously.

## Files written
- `/home/agentuser/repo/results/imo-2026-02/approaches/analytic-branch-cert.md` — the complete proof (Status: solved).
- Verification scripts: `/tmp/verify_sat4.py` (reviewer's, re-run), `/tmp/verify_G.py`, `/tmp/verify_ce.py`, `/tmp/verify_complex2.py`, `/tmp/verify_inside.py`.
