# Build report — ll-inclusion-gap, Round 12 (LB, G-INC-2nt a≥1 via Opening C)

**Status: partial** (real advance; one sharply-stated crux remains open, not overclaimed).

## What was built (all in Step 25 of `approaches/ll-inclusion-gap.md`)

1. **Floor Lemma (HS-B1) — FULLY PROVEN, all `j`.** `A({a}∪G_j) ≥ A(G_{j−1})`, equality iff `a=2^j`.
   Clean measure-form proof: `f(a)=A(G_j)+a−2·measure(S_{G_j}∩[0,a))` is piecewise-linear slope `∓1` on
   allowed/forbidden dyadic bands; local minima at `a=2^i`, and `f(2^{i+2})−f(2^i)=−2^i<0` pins the
   unique global min at `a=2^j` with value `A(G_{j−1})`. Verified 0-violation `j=1..6`, equality only at
   `a=2^j`. Proposed as `lemmas/floor-a-union-Gj.md` for certification.

2. **h=2 reduction (NEW, exact).** One Gen-Decomp step + `A=2O−Σ` give the exact identity
   `A(R)−A(Q) = 1 + 2a_v + 2(O_{R_lo}−O_{Q_lo})`, so the whole `a≥1` top-cut goal collapses to the single
   odd-position inequality **`O_{Q_lo} ≤ O_{R_lo} + a_v`** (`a_v=max(R)−q_1≥0`). Verified exact (663
   configs, 0 mismatch). This is the load-bearing new structural result.

3. **h≥4 and h=0 (`a ≤ 2^{n−2}−1`): CLOSED all `n`.** `h≥4` forces `Q_lo=∅`, `A(R)−A(Q)=deficit_top+
   A(R_lo)≥1`; `h=0` gives `deficit_top=2^{n−2}−a≥1`.

4. **HS-B2 fully-tight forcing — PROVEN (pinch `n∈{4,5}`).** At `a=2^{n−3}`, `a_v=b=0`: `S_{R_lo}=
   S_{G_{n−4}}`, `ΣQ_lo=3·2^{n−3}` with `S_{Q_lo}⊆S_{G_{n−4}}`, `|Q_lo|≤n−2` **force `Q_lo` = equal pair**,
   `A(Q_lo)=0` ⟹ `A(R)−A(Q)=1`. Matches the machine tight witnesses `n=4,Q=[6,4,3,3]` / `n=5,Q=[12,8,6,6]`.

## The honest open crux (isolated, sharply stated)
**(DFB)** `A(R_lo)−A(Q_lo) ≥ min(σ_lo,2−σ_lo)` for `R_lo={a}∪G_{n−3}`, `a≥1` — equivalently
`(★) O_{Q_lo} ≤ O_{R_lo}+a_v` in the `h=2` case — for **general `h=2, a≥1`** (plus the thin
`h=0, a∈(2^{n−2}−1,2^{n−2})` sliver, `n≥5`, reducing to the same DFB). DFB is the certified `a<1`
Family-Lemma bound extended to `a≥1`; its `k→k−2` descent proof is NOT available for `a≥1` (the family
`{a}∪G_{n−3}` is not descent-closed once `a≥2^{n−4}`; O1 fires — the R10 refuted-route obstruction). A
DIRECT (non-recursive) proof of DFB / `(★)` is the remaining work. Numerics: `a≥1` closure holds
0-violation (`n=4` 123 cfgs, `n=5` 662 cfgs, margin 1) — the statement is true, only the general proof
is open.

## Spec concerns (for orchestrator/outliner)
- The outline framed HS-B2 as "tight forcing `A(Q_lo)=0`", but that closes ONLY the *fully-tight* config
  (`a=2^{n−3}, a_v=b=0`). The tight branch `a=2^{n−3}` with `a_v+b∈(0,1)` still needs `A(Q_lo)≤a_v+b`,
  i.e. the DFB — so HS-B2 alone does NOT close even `n∈{4,5}` for all configs. The genuine single crux is
  DFB / `(★)`, now cleanly reduced. Next round should target a DIRECT proof of `(★) O_{Q_lo}≤O_{R_lo}+a_v`
  (e.g. via the odd-position/`T(ℓ)`-style machinery adapted to the perturbed base `{a}∪G_{n−3}`), NOT the
  refuted descent.
- Reminder of scope: even fully closing G-INC-2nt `a≥1` does not finish the LB — multi-cut refined `R`
  and G-GAP remain. This is one sub-branch of Lemma LL.

## Files written
- `results/imo-2026-03/approaches/ll-inclusion-gap.md` (Status/Approaches/Current best updated; Step 25
  appended; promotable lemmas 14–15 added).
- `results/imo-2026-03/lemmas/floor-a-union-Gj.md` (proposed, for certification).
