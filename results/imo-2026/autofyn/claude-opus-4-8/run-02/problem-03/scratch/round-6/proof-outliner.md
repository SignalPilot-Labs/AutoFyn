## imo-2026-03

The whole problem is one gap from solved: answer `c(n)=2^n/D_n`, `D_n=2^{n+1}-1`, PINNED; upper
bound `V_n≤1/D_n` FULLY CERTIFIED; sole residual is the lower bound **(LBL)**: every ≤n-cut
refinement `Q` of `W_n={2^0,…,2^n}` has `f(Q)≥1`. Four independent framings (self-similar Φ-max
forest, block-recursion UPM-5, cut-budget count-profile, game BNF) have all bottomed out on the
SAME wall (primal integrality of the Φ-max minimizer ≡ Gap A acyclicity + Gap B μ=3 leaf). Per the
plateau rule I field ONE representative of that wall (self-similar, advanced with a genuinely new
Gap-A weapon) and TWO members that attack `f≥1` WITHOUT proving primal integrality — the strongest
being the dual/signed-power route, which numerically dissolves both Gap A and Gap B (verified below).

---

### self-similar-recursion: advance
Target: prove `c(n)=2^n/D_n` (whole problem; UB imported certified).
Technique: strong induction on cut count `N`; Φ=Σx²-maximal global minimizer `P*`; integrality of
`P*` ⇒ Theorem F ⇒ `f(P*)` positive odd integer ≥1. Spine unchanged (§0–§5 sound, certified). Only
the two residual graph facts are re-planned with NEW mechanisms.
Skeleton (only the open steps re-planned; §0–§5 stand):
  1. §0–§4 as certified: reduction to (LBL); induction + degenerate leg; `ker U=0` (S-core);
     `μ_{k,j}∈{1,2,3}`; odd blocks carry only `μ=1`; no piece has two odd-block sub-pieces; block
     formula `f(P*)=Σ_{μ_j odd} σ_{a_j} w_j`. — all certified.
  2. **Gap A (H is a forest)** — attack via aimo-0913 full-cycle superincreasing telescoping made
     rank-aware. Given a putative cycle in `H`, orient it and form the ALTERNATING-SIGN mass sum
     along the whole cycle path (not just the two edges at the max-exponent piece — the 2-endpoint
     port is PROVED insufficient, integrality explorer). Because the cycle's pieces have distinct
     budgets `2^{a_1}<…<2^{a_r}` and each block's sub-pieces occupy a CONTIGUOUS rank interval
     (laminar stick geometry), the telescoped alternating sum of block-values around the cycle is a
     signed combination of distinct powers of two whose top term `±2^{a_r}` strictly dominates the
     sum of all admissible shorter terms (`Σ_{i<r}2^{a_i} < 2^{a_r}`), forcing the cycle sum ≠ 0 —
     but a genuine cycle in `H` (a `ker U` witness by the round-4 0/1 argument, extended to carry
     the intermediate extra-mass terms with signs) forces it `=0`: contradiction with `ker U=0`.
  3. **Gap B (no μ=3 even-block piece-leaf)** — degenerate-domination lemma. A leaf `2^k={v,v,v}`,
     `v=2^k/3` shared (even block), is Φ-dominated: exhibit a DEGENERATE competitor `P'` with the
     same `f=m` and `Φ(P')>Φ(P*)` (explorer's `{2,3,3}`: `Φ=35<51=Φ({5,4,2,2,1,1})`, same `f=1`,
     latter degenerate). A degenerate `P'∈G` is handled by Claim(N−1), so its existence with
     `Φ(P')≥Φ(P*)` alone contradicts the Φ-maximal choice of `P*` (or drops `N`). Prove the
     competitor exists in general by rank-tracked block decomposition (Lemma BD), not a uniform
     "bisect instead" swap (that changes global ranks — REFUTED as a one-liner).
Key lemmas (claim + mechanism):
  - Gap A: full-cycle alternating block-sum ≠0 — because distinct piece budgets are distinct powers
    of two and `2^{a_r}>Σ_{i<r}2^{a_i}` (superincreasing), so the telescoped signed sum cannot close
    a cycle; rank-contiguity supplies the sign assignment the incidence matrix alone cannot (pure
    kernel/multiplicity data is PROVABLY insufficient — 479-instance refutation, integrality lens).
  - Gap B: a μ=3 even leaf admits a degenerate Φ-dominator of equal `f` — because the shared value
    `v=2^k/3` lets mass be pushed to a length-0 boundary preserving every count-parity while
    strictly raising `Σx²`.
Open gaps: the two closures above (Gap A cycle-sum sign bookkeeping incl. off-cycle multiplicity;
Gap B general existence of the degenerate Φ-dominator). Everything else certified.
Cases to cover: Gap A — cycles whose blocks also touch off-cycle pieces, and multiplicity-≠1 cycle
edges (the two shapes S-core alone does NOT exclude). Gap B — only the μ=3 even leaf (μ=1,2 give
integer `w_j` directly; μ=3 odd excluded by M3).
Watch out for: do NOT re-attempt a pure linear-algebra/kernel closure of Gap A (refuted, 479
counterexamples with distinct-power budgets + private extra mass) — the argument MUST invoke
rank-contiguity. Do NOT present a bare "bisect the leaf" move for Gap B (changes global ranks).

---

### dual-integer-certificate: new
Target: prove `c(n)=2^n/D_n` (whole problem; UB imported certified). This is the genuinely
different framing FAR from the primal forest wall: it proves `f(P*)∈ℤ` WITHOUT proving any `w_j∈ℤ`
(primal integrality is FALSE — round-4 non-integer continuum), by exhibiting an INTEGER DUAL
certificate. Numerically it dissolves BOTH Gap A and Gap B (see below).
Technique: linear-programming/integer-duality. At the Φ-max minimizer `P*`, `f=s^T w` where
`s_j=σ_{a_j}·[μ_j\ odd]` (block formula, certified `odd-block-formula`) and `Uw=b`, `b_k=2^k`
(★). Since `ker U=0` (S-core), `U^Tλ=s` is ℚ-solvable and `f=s^Tw=(U^Tλ)^Tw=λ^T(Uw)=λ^T b=Σ_kλ_k2^k`
for EVERY solution `λ` — a signed combination of the ORIGINAL powers of two. If some `λ∈ℤ^{n+1}`
solves `U^Tλ=s`, then `f=Σλ_k2^k∈ℤ`; with `f>0` (min is positive) this is a nonzero integer, hence
`f≥1`. The "distinct powers of two ⇒ nonzero signed sum ⇒ ≥1" superincreasing floor is exactly the
reverse-reachability signed-power floor the count-profile/integrality explorers flagged.
Skeleton:
  1. Import (LBL) reduction, induction, degenerate leg, and the certified structural theory of `P*`
     (S-core `ker U=0`; M2/M3/M4; block formula `f=s^T w`, `Uw=b`). — certified.
  2. Reformulate `f∈ℤ` as: `U^Tλ=s` has an integer solution `λ` (then `f=λ^T b∈ℤ`). Prove
     `f=λ^T b` is independent of the choice of `λ` (holds because `Uw=b` exactly). — one-line
     linear algebra, verified numerically (f=λ·b=1 on the {2,3,3} minimizer).
  3. **Gap D (integer dual solvability):** `U^Tλ=s` has a solution `λ∈ℤ^{n+1}`. Attack by explicit
     laminar construction: order pieces by exponent and build `λ` bottom-up from the rank-contiguous
     block structure; each block equation `Σ_kμ_{k,j}λ_k=s_j∈{−1,0,1}` is resolved against the
     partially-built `λ` using that a block's sub-pieces sit in one rank interval touched by a
     laminar set of pieces. The specific alternating RHS `s` (not a generic RHS) is what makes
     integer solvability plausible where full unimodularity of `U` FAILS (TU/consecutive-ones
     REFUTED — but we do NOT need TU, only that this one `s` lies in the integer row-lattice of `U`).
  4. `f=Σλ_k2^k∈ℤ`, `f=m>0` ⇒ `f≥1`. Closes the inductive step, hence (LBL), hence the problem.
Key lemmas (claim + mechanism):
  - Dual identity `f=λ^T b` for any `λ` with `U^Tλ=s` — because `f=s^Tw` and `Uw=b` give
    `f=λ^TUw=λ^Tb`; the value is invariant across solutions since `b` is fixed by (★).
  - Gap D: `U^Tλ=s` integer-solvable — target mechanism: rank-contiguity makes `U` an interval
    (laminar) incidence up to multiplicity, so the specific alternating `s` is spanned integrally by
    the rows even though `U` is not TU; build `λ` by peeling the smallest-value block (bottom rank
    interval), which is touched by the smallest laminar sub-pieces, and inducting.
  - Superincreasing floor: a nonzero integer `Σλ_k2^k` has `|·|≥1` — trivially (nonzero integer),
    and specifically `≥1` matching `φ(W_n)=1` (min nonzero signed power sum, certified
    `subset-sum-pigeonhole` tightness).
Open gaps: Gap D (integer solvability of `U^Tλ=s`) — the SOLE gap of this route.
Cases to cover: none beyond Gap D; the μ=1,2,3 leaf distinction and cycles are NOT separate cases
here (the dual does not branch on graph shape — its advantage).
Watch out for: verify Gap D really is weaker than Gap A/B, not a disguise of them. Numerical
evidence it is: on the {2,3,3} minimizer (which round-4 used to REFUTE the primal Lemma W), an
integer `λ=(1,0,0,0)` gives `f=1` directly; and a μ=3 even leaf leaves `λ_k` free (its even-block
row `3λ_k+…=0` does not force a fraction), so **Gap D appears to bypass Gap B entirely**. Confirm
this on n≤4 exhaustively before committing; if some Φ-max minimizer has `s` OUTSIDE the integer
row-lattice, report it as the sharpened residual (still a NEW, non-Gap-A object).

---

### game-value-recursion: revise
Target: prove `c(n)=2^n/D_n` (whole problem) from the claiming-game side. Kept as the third,
genuinely different GENRE (combinatorial-game strategy space) to preserve breadth off the algebraic
wall — but re-planned onto its ONE untried mechanism, since re-deriving its Case A / LB-claim is
redundant (already certified).
Technique: strategy-stealing / involution on Xiang Yu's ≤n cuts (aimo-0225 symmetry template,
aimo-0596 floating-unpaired-element pairing) to pin the worst adversary line WITHOUT Φ-maximality.
Skeleton:
  1. Import LB-claim reformulation + Lemma R0 (`0≤f≤Σ`, `f(S)=a_1−f(S∖a_1)`) as free infra (certify
     them — cheap, currently uncertified) and Theorem LB-A (Case A, top uncut). — sound scaffold.
  2. Reduce to BNF: XY splits ≤n cuts as `j` on top `2^n` (fragments `T`) and `n−j` on `R=W_{n−1}`
     (giving `R'`); show `f(T⊔R')≥1`.
  3. **Gap (strategy-stealing instantiation):** define an involution on XY's cut multiset that maps
     any BNF response to a canonical one (e.g. pair each interior cut of `T` with a "mirror" cut,
     hand off Liu Bang's odd-mover floating element per aimo-0596) and show `f` is monotone /
     invariant under it, reducing to a canonical extremal line where the dyadic-domination chain
     `2^n>2^{n−1}+…+2^0` closes `f≥1`.
Key lemmas (claim + mechanism):
  - Lemma R0 peel identity — certifiable now (`f(S)=a_1−f(S∖a_1)` from layer-cake), reusable infra.
  - BNF involution — HYPOTHETICAL: no instantiation found this round (game explorer). The obstacle
    is that XY's cuts on `T` and `R'` are at different scales than Liu Bang's marks, so no obvious
    symmetric position exists. Flagged as exploratory; its value is genre-diversity, not a likely
    close.
Open gaps: the involution instantiation (Gap; currently no concrete construction). Also import UB.
Cases to cover: `j=0` (=Case A, done); `1≤j≤n` (BNF, incl. the numerically-confirmed `j=n`
all-cuts-on-top extremal at `f=1`).
Watch out for: this genre PROVABLY reduces to the same `f≥1` target (endgame-greedy pins the
claiming phase) — do NOT re-present Case A / LB-claim as progress; the only fresh content is the
involution. If the builder cannot instantiate it, harvest R0 + LB-claim as certified infra and
report the involution as still-open (honest partial), do not overclaim.
