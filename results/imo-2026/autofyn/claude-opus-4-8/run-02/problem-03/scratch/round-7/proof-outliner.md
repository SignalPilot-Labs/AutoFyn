## imo-2026-03

Context: the whole problem is ONE gap from solved. Answer `c(n)=2^n/(2^{n+1}-1)` pinned; upper
bound `c(n)≤2^n/D_n` fully certified. Lower bound reduces to (LBL): every ≤n-cut refinement of
`W_n={2^0,…,2^n}` has `f≥1`. This is proven for integer/dyadic, tie-free, and degenerate
minimizers. Sole residual: `f≥1` at the tied non-degenerate Φ-max minimizer `P*`, where
`Uw=b`, `f=sᵀw`, `ker U={0}` (S-core). By Cramer `f=Σ_j s_j det(U_j)/det(U)`, so **every** route
must control `det(U)` (square) or the gcd of maximal minors (rectangular) — the non-integrality
explorer proved no real-valued/continuous bypass exists. The residual = **minimality ⇒ benign
incidence matrix U**, attacked by three genuinely different machineries below.

---

self-similar-recursion: advance
Target: Prove `c(n)=2^n/(2^{n+1}-1)` end to end (imports certified upper bound; closes lower
  bound (LBL) via primal integrality of the Φ-max minimizer `P*`).
Technique: Primal incidence-graph machinery. `f(P*)∈ℤ` via leaf-peeling of the bipartite
  piece–component multigraph `H`, once `H` is shown to be a forest (Gap A′) with no `μ=3`
  even-block leaf (Gap B). Distinct object: graph acyclicity + distinct-powers-of-two positivity.
Skeleton (all steps 0–5 + Lemma CC already proven/certified; only Gap A′ and Gap B remain):
  1. Reduction (LBL), induction on cut count, degenerate leg — DONE (imported, certified).
  2. Lemma S-core `ker U={0}`, moves M2/M3/M4, block formula `f=Σ_{μ_j odd}σ_{a_j}w_j` — DONE.
  3. Lemma CC: `H` has no ISOLATED cycle (even via ker-U witness, odd via superincreasing
     powers-of-two) — DONE, certified round 6.
  4. **Gap A′ (open) — split into the two sub-cases the explorer isolated, attacked separately:**
     4a. EVEN sub-case: the explorer VERIFIED the even ker-U witness `d(Q_i)=(−1)^i` survives
         off-cycle PIECE attachment and uniform-multiplicity scaling. It dies on exactly three
         narrow shapes: {genuine chord} ∪ {cycle-COMPONENT touching an off-cycle piece (component
         degree ≥3)} ∪ {non-uniform cycle multiplicity}. In all three the local cycle sub-system
         gains full column rank. Close each by: (i) a θ-graph full-rank lemma (a chord splits a
         bipartite even cycle, rank-deficiency 1→0), then (ii) show the resulting det, still
         carrying the distinct powers `2^{a_i}` as the RHS, cannot admit an all-positive `w` — the
         SAME distinct-powers positivity machinery Lemma CC uses.
     4b. ODD sub-case: off-cycle-piece attachment genuinely escapes pure algebra (explorer's
         explicit cex `b=(1,2,2.5)→u=(0.75,0.25,1.75)` all positive). Close by MINIMALITY, not
         algebra: an S-core-style feasible-shift argument moving mass between a cycle component and
         its off-cycle attachment — show any such escaping positive solution is NOT a Φ-max
         minimizer of the real functional `f` over `K` (it admits a feasible flat/descent direction
         contradicting minimality or Φ-maximality), exactly as Lemma S-core excludes ker-U shifts.
  5. **Gap B (open) — Lemma BD (degenerate-Φ-domination):** for a `μ=3` even-block piece-leaf
     `2^k={v,v,v}`, `v=2^k/3` shared with another piece, construct a DEGENERATE competitor `P'∈G`
     (a `≤N−1`-cut refinement with `f(P')=f(P*)` EXACTLY), so Claim(N−1) gives `f(P*)≥1` with no Φ
     comparison. Track the moved value's new global rank to keep `f` exactly flat.
Key lemmas (claim + mechanism):
  - θ-full-rank — because a chord across a bipartite even cycle glues two cycles into a θ-graph
    whose incidence has trivial kernel (rank deficiency drops from 1 to 0), so the even ker-U
    witness cannot exist there; combined with distinct-powers RHS the surviving det has no positive
    solution.
  - Gap A′ odd via minimality — because the algebraic escape `b=(1,2,2.5)` corresponds to mass
    stolen from a cycle piece by an off-cycle attachment; that mass-transfer direction is feasible
    in `K`, so at a genuine Φ-max minimizer the S-core feasible-shift already forbids it.
  - Lemma BD — because for the shared `μ=3` even-leaf, sliding one copy to the block's shared
    partner produces a length-0 sub-piece (degenerate) while the block signs keep `f` unchanged.
Open gaps: Gap A′ even (3 narrowed shapes) — step 4a; Gap A′ odd (off-cycle attachment) — step 4b;
  Gap B (`μ=3` even-leaf) — step 5.
Cases to cover: Gap A′ even {chord, component-off-cycle-deg≥3, non-uniform mult}; Gap A′ odd;
  Gap B. (Isolated cycles both parities: DONE by Lemma CC.)
Watch out for: the DEAD "stick-position/laminar geometry" lever — `K` is the unconstrained product
  of simplices, `f`/`Φ` depend only on the sub-piece MULTISET (explorer confirmed). Off-cycle
  attachment for the EVEN case is a false alarm (Lemma CC already covers it) — do not waste it as a
  residual; only the three narrowed even shapes and the odd off-cycle case are open. Do NOT retry
  full-cycle superincreasing telescoping on non-isolated cycles (refuted, 479 cex).

dual-integer-certificate: advance
Target: Prove `c(n)=2^n/(2^{n+1}-1)` end to end via the DUAL certificate `f=λᵀb=Σ_k λ_k 2^k` with
  integer `λ` solving `Uᵀλ=s` (imports certified upper bound + Lemma DUAL).
Technique: Dual lattice / congruence machinery. Distinct object from primal: `s∈Uᵀℤ^{n+1}`
  (coprime maximal minors), NOT primal forest/unimodularity. Merge Gap D + Positivity into ONE
  minimality-derived congruence invariant (aimo-0281 template).
Skeleton:
  1. Reduction, S-core, block formula, Lemma DUAL `f=Σλ_k2^k` for every rational λ — DONE, certified.
  2. Cramer restatement (square `p=n+1`): `f=Σ_j s_j det(U_j)/det(U)`, an exact ratio of integers,
     so `f·det(U)∈ℤ`. Reduces Gap D + Pos to: `|det U|=1` AND numerator `≠0` at the minimizer.
  3. **Small-p reduction (open, new lever):** the explorer found Gap-D failures concentrate at
     `p=n+1` (maximal distinct value-classes). Show minimality/Φ-maximality biases `P*` toward
     SMALL `p` (few value-classes), where the distinct-powers RHS `2^k` makes the minor-gcd
     tractable. Pigeonhole/extremal on the number of distinct values.
  4. **Unified congruence invariant (open, aimo-0281 template) — MERGE Gap D + Positivity:** find a
     SINGLE minimality-derived congruence on `(U,s)` that simultaneously (a) forces `s∈Uᵀℤ^{n+1}`
     (integer λ ⇒ `f∈ℤ`) and (b) forces `f≢0`, rather than proving the two as independent gaps.
     The concentration obstruction (a class column `= m·e_k`, `m≥2`, in a single piece) is exactly
     what breaks BOTH gcd-1 and the invariant — exclude it once.
Key lemmas (claim + mechanism):
  - Cramer integrality — because `U,b` are integer, `w_j=det(U_j)/det(U)` so `f·det(U)=Σ_j s_j
    det(U_j)∈ℤ`; hence `f≥1 ⇔ |det U|=1 ∧ numerator≠0` (square case). Verified: `{2,4/3,4/3,4/3,1}`
    gives `det U=3`, `f=5/3`, `f·det U=5∈ℤ` exactly.
  - Concentration exclusion at minimizers — because a value-class carried with multiplicity `m≥2`
    inside ONE piece and absent from every other piece makes its `U`-column `= m·e_k`, forcing
    `m∣det U` (verified: the `4/3` column `[0,0,3]ᵀ` forces `3∣det U=3`); minimality must exclude
    it since it is the exact structure making `f∉ℤ` off the minimizer set.
  - Unified invariant (aimo-0281) — because the same mod-`p` selection condition that makes the
    minimality-selected `P*` unique can simultaneously certify integer dual-solvability AND `f≠0`.
Open gaps: Gap D at minimizers (integer λ / gcd-1 of maximal minors), Positivity (`f≠0`) — steps
  3,4 aim to merge these into one concentration-exclusion + congruence invariant.
Cases to cover: square `p=n+1` (via det, small-p bias) and rectangular `p<n+1` (via minor-gcd);
  Positivity sub-cases all-even (budget: `f=0` needs `≥n+1` cuts, one over budget) and
  odd-cancellation.
Watch out for: Gap D is FALSE as a universal S-core property (certified `gap-d-not-universal`) —
  the proof MUST use minimality. Do NOT retry naive per-piece KKT / same-sign-per-piece (REFUTED
  this round: subgradient at a tied class is the full interval `[-1,1]`, vacuous), nor `μ_j odd ⇒
  μ_j=1` (REFUTED), nor the λ₀-parity Positivity mechanism (REFUTED, λ non-unique).

concentration-exclusion-rigidity: new
Target: Prove `c(n)=2^n/(2^{n+1}-1)` end to end by showing directly that the Φ-max minimizer's
  incidence matrix `U` is BENIGN (`|det U|=1` square / gcd-1 minors rectangular), then Cramer gives
  `f=Σ_j s_j det(U_j)/det(U)∈ℤ`, `≥1`.
Technique: GLOBAL variational-rigidity / exchange machinery — a third object, distinct from
  primal cycle-exclusion and dual λ-construction. Directly forbid the ONE structure that breaks
  benign-U in BOTH live routes: a "concentrated" value-class (multiplicity `m≥2` inside a single
  piece, with no coprime witness in another piece). This is the crispest shared target
  (minimality ⇒ benign-U) attacked head-on — it could crack both routes at once.
Skeleton:
  1. Import reduction (LBL), S-core `ker U={0}`, block formula `f=sᵀw`, `Uw=b`, and Cramer
     `f·det U=Σ_j s_j det(U_j)∈ℤ` (square) / lattice form (rectangular) — all certified/immediate.
  2. **Concentration lemma (open, the whole content):** at the Φ-max minimizer, no value-class `C_j`
     has a `U`-column with a single nonzero entry `m≥2` (i.e. `C_j` lives entirely inside one piece
     `2^k` as `μ_{k,j}=m≥2` copies) UNLESS `m` is coprime to the rest of the minor structure.
     Mechanism: if `C_j=m·(2^k/m)` is concentrated, `2^k/m` shared with another piece is the only
     way it enters other rows; a mass-EXCHANGE between piece `2^k` and the sharing piece is a
     feasible direction in `K` that either lowers `f` (contra minimality) or is flat and raises `Φ`
     (contra Φ-max) — the same feasible-shift engine as Lemma S-core, but applied to the
     concentration column rather than a kernel vector.
  3. **Benign-U from no-concentration (open):** with concentration excluded, prove the maximal-minor
     gcd is 1 by induction on `p` — peel the bottom-rank value-class (which, being non-concentrated,
     has a `±1` pivot after row reduction against the distinct powers `2^k`), reducing `det U` by a
     unit each step. Distinct-powers RHS is load-bearing (generic RHS fails, det=2 cex known).
  4. Conclude `f=Σ_j s_j det(U_j)/det(U)∈ℤ`; Positivity via the same concentration-free structure
     (the block formula cannot cancel to 0 without a concentrated even class, excluded in step 2)
     ⇒ `f≥1` ⇒ (LBL) ⇒ `c(n)=2^n/D_n`.
Key lemmas (claim + mechanism):
  - Concentration ⇒ non-minimizer — because a concentrated class column `m·e_k` (`m≥2`) forces
    `m∣det U` hence `f=N/det U` can be `<1` (`{2,4/3,4/3,4/3,1}`: `m=3`, `f=5/3`); the defining
    exchange direction (move mass between the two pieces that share the value) is feasible in the
    product-of-simplices `K`, so it contradicts minimality or Φ-maximality.
  - Benign-U by rank-contiguous peeling — because each value-class occupies a contiguous rank
    interval and, once non-concentrated, contributes a `±1` pivot against the superincreasing
    powers `2^k`, so the maximal-minor gcd telescopes to 1.
Open gaps: the concentration lemma (step 2) and benign-U peeling (step 3) — both new, both
  minimality/variational.
Cases to cover: concentration with `m=2` (bisection-like) vs `m=3` (the `5/3` structure);
  square vs rectangular `U`; Positivity (no concentrated even class).
Watch out for: must NOT reduce to the primal cycle question (that is self-similar's object) — this
  targets SINGLE-column concentration, a different obstruction (`{2,4/3,4/3,4/3,1}` is NOT a cycle).
  Must use minimality (concentration is S-core-compatible, so pure algebra insufficient, per
  `gap-d-not-universal`). Verify the exchange direction stays inside `K` and keeps distinct ordered
  values for small step (chamber-affinity of `f`). Do NOT invoke stick-position geometry (dead).
