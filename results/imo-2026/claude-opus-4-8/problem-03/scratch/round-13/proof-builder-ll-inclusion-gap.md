# Build report — ll-inclusion-gap, round 13 (Status: partial)

## Proved (rigorous, all `n`)
- **Size-2 `Q_lo` closure for the `a ≥ 1` top cut, ALL `a ∈ [1, 2^{n−2})`** (Step 26, promotable
  `lemmas/size2-Qlo-closure.md`). Upgrades the round-12 pinch `n∈{4,5}` to every `n`, via two regimes
  (`j := n−3`):
  - `a < 2^j`: **equal-pair forcing** (vacuousness). `S_{R_lo} ⊆ [0,2^j)` and `p_1 > 2^j` force
    `p_1 = p_2`, so `A(Q_lo) = 0`, `A(R_lo)−A(Q_lo) = A(R_lo) ≥ A(G_{j−1}) ≥ 1` (Floor Lemma). My proof
    is cleaner than and corrects the range of the explorer's draft (the explorer stated `a<2^j` as the
    whole range; the true range is `a<2^{j+1}`, and its Case-A/B split is replaced by the single fact
    `S_{R_lo}⊆[0,2^j)`).
  - `a ≥ 2^j`: forcing **fails** (non-equal admissible pairs exist), but `A(R_lo)=a−A(G_j)` and the
    top-band forcing `p_2 ≥ 2^j`, `p_1 ≤ a` give `A(Q_lo) ≤ a−2^j`, hence
    `A(R_lo)−A(Q_lo) ≥ 2^j−A(G_j) = A(G_{j−1}) ≥ 1`.
- **Parity** (Step 26.3): even `|R_lo| = j+2` (even `j`) forces even `|Q_lo|`, excluding odd sizes.
- **Equal-top-pair size-3** (Step 26.4(ii)): `A(Q_lo) ≤ 1 < A(G_{j−1})`, closed.

## Verified (exact Fractions, budget-enforced)
- `min(A(R)−A(Q)) = 1`, **0** configs `< 1` at `n=4,5,6` (dens to 4) for the `h=2` `a≥1` top cut.
- Size-2: 0 non-equal admissible pairs for `a<2^j` (`j=1,2,3`); for `a≥2^j`, `min DFB = A(G_{j−1})`,
  0 violations. `A({a}∪G_j)=a−A(G_j)` for `a≥2^j` (`j=1..4`).
- Residual (deficit_top<1) min-margin by size at `n=6`: size-2 → 2 (or 0 at fully-tight),
  size-3 → 1, **size-4 → 0 (TIGHT)**.

## KEY NEGATIVE FINDING (reshapes the frontier)
The outline/reviewer premise **"large slack for size ≥ 3" is FALSE.** There is a **tight** size-4
residual config: `n=6, a=2, R=G_4∪{2,30}, Q={30,16,8,4,3,3}, Q_lo={8,4,3,3}` with
`A(R_lo)=5, A(Q_lo)=4, deficit_top=0`, so `A(R)−A(Q)=1` exactly. Structurally `S_{R_lo}=[0,1)∪[4,8)`,
`S_{Q_lo}=[4,8)` (the top band), and the entire deficit `1` is the **uncovered bottom band `[0,1)`**.
So the size-≥3 crux is genuinely tight — same difficulty tier as the anchor's mutual induction — and
CANNOT be closed by a band-accounting slack argument. Any future outline proposing "size ≥ 3 closes by
large slack" should be rejected on this witness.

## Gaps (honest, still OPEN)
- **Distinct-top size ≥ 3** (the primary target): tight; reduced to the quantitative claim "sum + budget
  cannot cover both the top region and the bottom band `[0,1)`", which is unproven (Step 26.4(i)).
- The `h=0, a∈(2^{n−2}−1,2^{n−2})` sliver (reduces to the same).
- Multi-cut refined `R` (G-INC-2 beyond the `G_{n−1}` top cut) and G-GAP (non-containment) — the full
  lower bound remains OPEN. Not overclaimed anywhere.

## Honesty compliance
- Did NOT revive the perturbed `T'(j)` / `{Claim_R,T_R}` mutual induction (declined per reviewer).
- Did NOT use "perturbed L1 without sum constraint" or "INC forces max(Q)≤max(R)".
- Verified numerically with exact Fractions at `n=4,5,6`; reported the tight configs.

## Spec concerns
None new. The `answer_type` is a fixed constant `c(n)=2^n/(2^{n+1}−1)`; this approach targets the LOWER
bound; the upper bound is `geometric-selfsimilar`'s track.

## Deliverable
- Approach file updated: `results/imo-2026-03/approaches/ll-inclusion-gap.md` (Status: partial).
- New promotable lemma: `results/imo-2026-03/lemmas/size2-Qlo-closure.md`.
