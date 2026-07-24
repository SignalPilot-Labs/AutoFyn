# proof-builder r2 — trig-metric-identity (imo-2026-02)

Status: solved. The single reviewer-diagnosed gap (`0·∞` at `f=0` in `T=q_G·G+q_H·H`) is closed.

## What I changed

1. **Replaced the rational-cofactor identity by a polynomial one.** In `verify.py` I cleared
   the denominators introduced by the two exact polynomial divisions. The denominator content
   `c=lcm(denom q_G, denom q_H)` turns out to equal `f` **exactly** (`c−f=0`, asserted), giving
   the exact polynomial identity
   `f·T = Q_G·G + Q_H·H` with `Q_G,Q_H ∈ ℚ[p,q,a,s,t_K,t_L]` (denominators of `Q_G,Q_H` are
   `1`, asserted). Residual `f·T−(Q_G·G+Q_H·H)=0` is an exact symbolic zero. This eliminates
   the `0·∞` entirely: the cofactors are polynomials, so the identity holds unconditionally
   and specializes to `f·T=0` whenever `G=H=0`, with no denominators.

2. **Identified the vanishing quantity and proved it positive.** The role of the reviewer's
   `f` is now explicit: it is the shared (up to positive factors `½(1+s²)²·AB²`, `½(1+s²)²·AC²`)
   leading coefficient of `G` (in `t_K`) and `H` (in `t_L`) — I display both factorizations
   (eq. (7)), matching the script's `lcG/lcH`. I proved
   `f = (1+s²)·AB·AC·sin(∠A+θ)` (eq. (9)) from the two identities
   `AB·AC·cos∠A = dot(B−A,C−A) = p²+q²−ap` and `AB·AC·sin∠A = |cross(B−A,C−A)| = qa`, plus the
   sine addition formula (also checked exact-zero in `verify.py`).

3. **Proved `∠A+θ ∈ (0,π)`, hence `f>0`.**
   - `θ = ∠KBA < ∠ABC`: `M` is the midpoint of `AB`, so ray `BM` = ray `BA` and the angle of
     `△BMC` at `B` equals `∠ABC`; since `K` lies strictly inside `△BMC`, ray `BK` is strictly
     between sides `BM(=BA)` and `BC`, so `∠KBA < ∠ABC`. (This is the exact point where the
     region hypothesis `K∈△BMC` enters the metric argument.)
   - `∠A + ∠ABC = π − ∠ACB < π` by the triangle angle sum with `∠ACB>0`.
   - Therefore `0 < ∠A+θ < ∠A+∠ABC < π`, so `sin(∠A+θ)>0`, and with `1+s²,AB,AC>0`, `f>0`
     (eq. (10)).

4. **Conclusion rewritten.** `G=H=0 ⟹ f·T=0` (polynomial identity) and `f>0` ⟹ `T=0` ⟹
   `O_x=(2p+a)/4` ⟹ `OM=ON`, for every admissible `(K,L)`. Added a remark noting the `0·∞`
   pitfall is now structurally impossible (polynomial cofactors + one positive scalar divided
   out). Updated Approaches tried / Current best / Remark, and added promotable lemma **L-pos**.

## Confirmation the gap is closed

`python3 results/imo-2026-02/verify.py` passes all asserts (exact symbolic zeros):
- `T−(qG·G+qH·H)=0` (original rational identity, still there);
- `c−f=0` (content equals `f`);
- `f·T−(QG·G+QH·H)=0` with `denom(QG)=denom(QH)=1` (polynomial identity);
- `f−(1+s²)·AB·AC·sin(∠A+θ)=0` (geometric meaning of `f`).

The logic "any admissible (K,L) ⟹ G=H=0" (Steps 3–4, unchanged, reviewer-verified) + "f>0"
(Step 5, new) + the exact polynomial identity (8) gives `O_x=(2p+a)/4` with no remaining gap.

## Spec concerns
None. `proof_only`, no numeric answer to verify. Region hypotheses used minimally and exactly:
`K∈△BMC` and `L∈△BNC` fix branches (Steps 2–3) and now also force `f>0` (Step 5); inside-angle
hypotheses give the two oriented-angle equalities. All three angle equalities used.

File: /home/agentuser/repo/results/imo-2026-02/approaches/trig-metric-identity.md
Script: /home/agentuser/repo/results/imo-2026-02/verify.py
