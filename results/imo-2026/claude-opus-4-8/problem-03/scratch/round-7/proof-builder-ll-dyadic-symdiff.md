# Build report — ll-dyadic-symdiff (Round 7)

Status: **partial** (advanced). File: `results/imo-2026-03/approaches/ll-dyadic-symdiff.md`.

## What was proved this round (GAP-B, double-REFL telescoping; anchor R = G_{n−1})
- **Lemma REFL-gen (NEW, promotable, proved in full):** relaxes certified Lemma REFL's `μ ≥ 2^{n−1}` to
  the weaker `max(R) ≤ μ = max(Q)`, giving `A(Q∪R) = μ − A(Q'∪R)`. Same set-theoretic proof; the only
  touched step is `S_R ⊆ [0,μ)`. Needed for the SECOND reflection (removed max `q_1 < 2^{n−1}` is outside
  certified REFL's range). Verified 0/4000 random rational tests.
- **Double-REFL formula (II)** `A(Q∪G_{n−1}) = 2^{n−1} − q_1 + A(Q'∪G_{n−2})`: rigorous as certified REFL
  on global max `2^{n−1}`, then REFL-gen on `q_1` (valid since `q_1 > 2^{n−2}`). 0 mismatches, 90+1205
  instances (reviewer 0/3031).
- **B3a** (`q_1 ≤ 2^{n−2}`) and **B3b** (`2^{n−2} < q_1 ≤ 2^{n−1}−1`): CLOSED rigorously **for all n**
  (A ≤ max and A ≥ 0 respectively, both via Lemma M0).
- **B3c** (`2^{n−1}−1 < q_1 < 2^{n−1}`) reduced to the single clean tight residual **(B2\*)**
  `A(Q'∪G_{n−2}) ≥ 1` (equiv. `Σ_odd(Q'∪G_{n−2}) ≥ 2^{n−1}`), and **(B2\*) PROVED IN FULL at n = 3**
  (exhaustive `|Q'|∈{2,3}` casework via `S_{{1,2}}=[1,2)` + merge lemma; every sub-case ≥ 1, tight at 1).
  So **GAP-B is closed at n = 3 for the anchor R = G_2.**

## What remains open (isolated honestly)
- **(B2\*) general n** — the one residual for GAP-B/anchor. Shown to be the shared crux: a third
  reflection splits into (i) `q_2 ≤ 2^{n−2}` = a GAP-A-shape upper bound `A(Q'∪G_{n−3}) ≤ 2^{n−2}−1`, and
  (ii) `q_2 > 2^{n−2}` = the reviewer's non-terminating recursion. So (B2\*) coincides with the
  alternating-tail bound `(p_2−p_3)+⋯ ≥ 1` = GAP-A = ll-inclusion-gap's G-INC-1. Addressed the reviewer's
  `q_2 > 2^{n−2}` termination concern head-on: the naive "recurse" does NOT terminate, so it is not
  claimed — the residual is instead reduced to the shared crux.
- **GAP-A** (branches with `max(Q) ≥ 2^{n−1}`): unchanged, = ll-inclusion-gap's G-INC-1. Import when
  either route closes the alternating-tail `+1`. ll-inclusion-gap's two-step induction closes G-INC-1
  sub-cases h≥4 / h=2,deficit≥1 / h=2,a≥b, leaving 2b-ii (a<b) — the same residual from the parallel side.
- **Refined R for GAP-B:** double-REFL covers only R = G_{n−1} unrefined; refined R (min A = 3/2) is a
  further residual.

## Rigor notes obeyed
- Did NOT revive the FALSE "max(Q) < 2^{n−1} ⟹ A ≥ 2". B3-anchor min is 3/2 (never 1, never 2). The old
  "tight A=1" witness Q={3,3,2},R={2,2,2,1} is correctly a **Sub-3a** case (I_0 fully odd, N_P(0+)=7),
  NOT B3 — stated in the file.
- All numeric checks are tiny/bounded (<20s), joint cut budget enforced (R=G_{n−1} ⟹ #Q-cuts ≤ n ⟹
  |Q| ≤ n+1), incremental prints. n=3 B3c casework re-verified on 1/8-grid (0 violations).

## Proposed lemma for certification
- `results/imo-2026-03/lemmas/ll-reflection-identity-gen.md` — Lemma REFL-gen (statement + proof in the
  approach file's Promotable section). Strictly generalizes the certified `ll-reflection-identity.md`.

## Spec concerns:
(none)
