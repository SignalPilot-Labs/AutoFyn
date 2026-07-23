# Theorem (UB_S) ⟹ Λ_S finite, and the whole-problem conditional bridge

**Source.** `results/imo-2026-06/approaches/sunflower-bundle-closure.md`
(round 8, §4, §4c). Depends on: `lemmas/lemma-ERD-realized-blocked-
dichotomy.md`, `lemmas/lemma-SR-self-realized-core-shortcut.md`,
`lemmas/lemma-delta-system-dichotomy.md`, `lemmas/lemma-escape-
confinement.md`, the No-Resurrection Lemma
(`lemmas/theorem-V-veto-finite-iff-MRS.md`), Lemma P′
(`lemmas/lemma-P-prime-pairwise-intersecting.md`), and the certified
reduction chain (Theorem 5.1 ← Lemma MS ← Theorem V + Theorem CD/Lemma TC ←
Λ_S-Reduction Lemma).

## Statement

Fix a proper nonempty core `S⊊P_1`. Define Hypothesis `(UB_S)`:
`sup{|rad(a_i)∖S| : i∈I_S}<∞`. Then `(UB_S)⟹Λ_S` is finite.

Consequently (main theorem): if `(UB_S)` holds for **every** proper nonempty
core `S⊊P_1` — equivalently, `sup{ω(a_n):n∉I_{P_1}}<∞` (a strictly weaker
requirement than a single global bound `ω(a_n)=O(1)` for *all* `n`, since
indices with imprint exactly `P_1` impose no constraint) — then
`a_{n+T}=a_n+L` for every `n≥1`, for explicit `T,L` given by Theorem 5.1.

## Proof

Fix `S`. If `I_S` is finite, `𝓥_S⊆{rad(a_i):i∈I_S}` is finite trivially.
Assume `I_S` infinite. Apply the Realized–Blocked Dichotomy to `C:=S`.

**Case `S` realized.** Lemma SR gives `𝓥_S` finite directly, no use of
`(UB_S)`.

**Case `S` blocked** by witness `j_3`. Assume `(UB_S)` with bound
`M:=sup_{i∈I_S}|rad(a_i)∖S|<∞`. Toward a contradiction suppose `𝓥_S` (hence,
via the bijection `C↦C∖S`, the family `𝓠_S:={C∖S:C∈𝓥_S}` of pairwise
distinct sets of size `≤M`) is infinite. Apply the Δ-system dichotomy to
`𝓠_S`:

- **Pairwise-disjoint sub-family `𝓠_S'`.** Each `Q∈𝓠_S'` corresponds to a
  realized `C=S∪Q` with realizing index `i∈I_S`, an escape from `κ:=S`
  (blocked by `j_3`); the Escape-Confinement Lemma forces
  `Q∩comp(a_{j_3})≠∅`. Choosing one witness per `Q` gives an injection
  `𝓠_S'↪comp(a_{j_3})` (using pairwise disjointness), so `|𝓠_S'|≤
  |comp(a_{j_3})|` — contradicts infinitude.

- **Sunflower sub-family with core `Y≠∅`.** Apply the Realized–Blocked
  Dichotomy to `κ':=S∪Y`.
  - If `κ'` realized at index `k`: every `S∪Q_l` (`l∈L`, the sunflower's
    index set) strictly contains `κ'` and lies in `𝓥_S`, so by
    No-Resurrection it lies in `⋃_{n=1}^{k-1}𝓜_n`, a fixed finite set —
    contradicts the `Q_l` (hence `S∪Q_l`) being pairwise distinct and `L`
    infinite.
  - If `κ'` blocked by `j_3'`: `Y∩comp(a_{j_3'})=∅`, so Escape-Confinement
    applied to each escape `i_l` (realizing `S∪Q_l⊋κ'`) forces
    `(Q_l∖Y)∩comp(a_{j_3'})≠∅` — a pigeonhole injection
    `L↪comp(a_{j_3'})` via the (pairwise disjoint) petals `Q_l∖Y`,
    contradicting `L` infinite.

Both branches of the dichotomy give a contradiction, so `𝓥_S` (hence
`Λ_S=⋃𝓠_S`) is finite. `∎`

**Whole-problem bridge.** If `(UB_S)` holds for every proper core `S`,
`Λ_S` finite for every `S` (above), so `𝓥_S` finite for every `S`
(Λ_S-Reduction Lemma); combined with Lemma TC (`𝓥_{P_1}={P_1}`
unconditionally), Theorem CD gives `𝓥` finite; by Theorem V, (MRS) holds;
by Lemma MS, FCBC holds; by Theorem 5.1, `a_{n+T}=a_n+L` for every `n≥1`.
`∎`

## Certification

Independently re-derived and re-checked step-by-step by the round-8
proof-reviewer, including the equivalence `(UB_S)` for all proper `S`
`⟺ sup_{n∉I_{P_1}}ω(a_n)<∞`. No gap found. Certified `solved`-quality for
the conditional statement — **`(UB_S)` itself (equivalently
`sup_{n∉I_{P_1}}ω(a_n)<∞`) remains open**, not proved by this lemma. This
is now the single sharpest known sufficient hypothesis for the entire
remaining problem: strictly weaker than round 3's global `ω(a_n)=O(1)`
(restricted away from the top-core indices `I_{P_1}`), and equivalent to a
single, clean numeric statement rather than a family of conjectures.

**Numerical support (not a proof, independently reproduced by the
proof-reviewer with a fresh generator, exact match with the source's
claims):** `max ω(a_n)` through the stated ranges: `a_1=247`: `6` (at
`n=1039`, `N=3000`); `a_1=2747`: `6` (at `n=1646`, `N=3000`);
`a_1=21528751`: `7` (at `n=872`, `N=1200`). Consistent with `(UB_S)` in
every tested case; no counterexample found.
