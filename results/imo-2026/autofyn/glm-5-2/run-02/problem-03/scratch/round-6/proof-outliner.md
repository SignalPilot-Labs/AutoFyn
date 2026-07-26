## imo-2026-03

Field after round 5: `pairing-partner` (1598), `cell-complex-l3` (1596), `two-regime-disjunctive` (1540), `dyadic-halving-induction` (1487, RETHINK). Priorities: (1) close U(3) end-to-end via the explorer's 7-cap subfamily; (2) general-n L lift via D3's 2-adic/determinant handle or direct e_M≤o_R injection; (3) NEW genuinely-different G2 framing (self-reproducing invariant); (4) retire/re-conceive the dead dyadic-halving route.

---

### two-regime-disjunctive: ADVANCE
Target: `c(3) = 8/15` SOLVED end-to-end (Liu lower bound + Xiang upper bound for n=3); and the general-dyadic/non-dyadic upper-bound framing as the long-term vehicle for U(n).
Technique: Casework/exhaustion on a 7-cap subfamily (KB "Casework / exhaustion") — the direct n=3 generalization of the certified U(2) four-strategy lemma. This OVERTURNS round-5's "17-family necessary" ruling: the prior census used un-realizable cap *values* (`d−b−c` when `d<b+c`, `2d−1` when `d<1/2`); with realizability enforced, the 7-cap subfamily closes BOTH extreme sub-cases.

Skeleton (closing the LAST U(3) gap, the d<1/2 non-gap extreme sub-cases `w<−2α` or `z<−2α`):
  1. Import certified `lemma-u3-5cap-dominant` (d≥1/2 closed), `lemma-u3-sliver-gap` (d<1/2 gap G closed), and the 4 sub-case closure for d<1/2 non-gap `w,z≥−2α` — so the only remaining U(3) territory is `{w<−2α} ∪ {z<−2α}` with d<1/2.
  2. State the 7-cap family `{a, b−a, c−b, d−c, |a+b−c|, |a+c−d|, |a+b−d|}` (4 chain-difference caps + 3 abs-sum caps; the missing 4th abs-sum `|b+c−d|` is already used in the closed `z∈[−2α,0]` sub-case).
  3. Prove each of the 7 caps is **always-realizable** by an explicit ≤3-mark Xiang strategy: `a` (shave `a→(ε,a−ε)`), `b−a` (match `a` in `b`+...), `c−b` (match `b` in `c`+...), `d−c` (match `c` in `d`+...), and `|a+b−c|` / `|a+c−d|` / `|a+b−d|` via 2-mark bisect-and-match (split the larger of the two referenced pieces, pair up to leave the abs-difference as a leftover). NONE requires `d≥b+c` (that is the point — cap `d−b−c` is excluded from the 7).
  4. Assume for contradiction all 7 caps `> α(3)=1/15`. Chain caps give `a>α, b>2α, c>3α, d>4α` (so `a+b+c+d > 10α = 2/3`, consistent with `d<1/2 ⟹ a+b+c>1/2`). The 3 abs caps give 2^3=8 OR-sub-cases.
  5. **w<−2α sub-regime** (i.e. `c < a+b−2α < a+b−α`): this forces the `|a+b−c|` cap into the branch `a+b−c > α` (no OR), reducing to 2^2=4 sub-cases. Derive a ≤4-line inequality contradiction in each (combine chain bounds with the assumed abs-cap lower bounds).
  6. **z<−2α sub-regime** (i.e. `d < b+c−2α`): combine with chain-cap `d > c+α` and the abs-cap lower bounds; derive the 4 sub-case contradictions.
  7. Merge with the certified d≥1/2, gap-G, and non-gap `w,z≥−2α` closures: equality `min=α` iff the dyadic `(1,2,4,8)/15` (which lies in d≥1/2). Combined with CERTIFIED L(3) (cell-complex), this gives `c(3)=8/15` SOLVED.

Key lemmas:
  - "7-cap subfamily always-realizable" — because each cap is a leftover after a 2-mark bisect-and-match that pairs equal fragments; realizability does not require `d≥b+c`.
  - "8-sub-case contradiction" — because `w<−2α` collapses the `|a+b−c|` sign-OR (since `c<a+b−α` is forced), halving the case tree per sub-regime.

Open gaps: step 5–6 — the 8 analytic sub-case contradictions (the explorer verified 0 violations on 105k exact-rational configs; worst cap `0.0598 < α=0.0667`, margin `0.007`; the algebra needs writing). Watch: the 6-cap subset `{a,b−a,c−b,d−c,|a+b−c|,|a+c−d|}` is a boundary failure (passes 600k, fails 2M by 0.003) — the 7th cap `|a+b−d|` is genuinely load-bearing. Watch: do NOT add cap `d−b−c` (un-realizable in `z<−2α`). Watch: do NOT use the gap-G sliver for the `z<−2α` half (sliver requires `d≥b+c`, opposite).

Distinct from: all other approaches — this is the ONLY route that closes c(3) end-to-end this round. Pairing-partner and cell-complex attack general-n L (lower bound); the new self-reproducing-invariant attacks general-n U (different framing).

---

### cell-complex-l3: ADVANCE (D3 via 2-adic-valuation / determinant)
Target: L(n) for ALL n (Liu lower bound for the dyadic config, general n) via a structural theorem, NOT per-n enumeration.
Technique: Linear-algebra method (Cramer's rule) + 2-adic valuation of `0/±1`-determinants with power-of-2 RHS — KB "Invariants & monovariants" + "Linear-algebra-method". This is the higher-leverage general-n L target per the explorer (ONE theorem vs Hall route's TWO matchings PLUS R-refined sub-cases).

Skeleton:
  1. At any arrangement vertex of the level-n dyadic, the pieces `p_i = det_i / L` where `L = det(active hyperplane subsystem)` (Cramer's rule; integer coeff matrix; RHS in `{0,1,2,4,…,2^n}`).
  2. The advantage `A = (Σ(−1)^{i+1} det_i) / L`; target `A ≥ 1` (integer scale, i.e. `A ≥ α(n)·D(n)` real) ⟺ `Σ(−1)^{i+1} det_i ≥ L`.
  3. At INTEGER-valued vertices, certified `lemma-parity-integer-vertices` gives `A` odd non-neg ≥ 1 (the D2 stall — parity gives weaker `A ≥ 1/L` for odd L).
  4. **D3 GAP (the new handle):** prove `v_2(Σ(−1)^{i+1} det_i) < v_2(L)` OR directly `Σ(−1)^{i+1} det_i ≥ L`, using (a) the dyadic RHS structure (powers of two), (b) `D(n)` odd, (c) the `0/±1` hyperplane rows. The handle is that the numerator's 2-adic valuation is forced strictly below `v_2(L)`, so `num/L > 1`.
  5. First build step: compute `v_2(det)` and `Σ(−1)^{i+1} det_i − L` for ALL n=3,4 fractional arrangement vertices (census exists from the L(3)/L(4) certification) — find the signature (explorer conjectures L often even, numerator's v_2 strictly less, forcing `A>1`).

Key lemma:
  - "v_2(numerator) < v_2(L) at fractional vertices" — because the dyadic RHS (powers of two) plus `0/±1` rows make the numerator's alternating sum lose factors of 2 that L (the determinant) retains; crux `aimo-0917` ("preserve a 2-adic residue as a game invariant; split N=N_++N_− so odd-valuation total forces one branch to inherit") is the template to adapt.

Open gaps: step 4 — the 2-adic-valuation bound on `det_i`-numerators for `0/±1`-matrices with power-of-2 RHS (a number-theoretic lemma, not standard olympad toolkit but in scope); step 5 census computation. Watch: this lemma must be PROVEN, not just numerically observed; the slack-grows-with-n evidence (0 violations n=3..7) is a green light, not a proof. Watch: the D3-dual risk (opening 3) shares this technique with U — flag the shared-wall.

Distinct from: pairing-partner (Hall matchings, sum-level not det-level — genuinely different G1 route). Distinct from two-regime (n=3 upper bound, this is general-n lower bound). Distinct from self-reproducing-invariant (upper bound).

---

### pairing-partner: ADVANCE (direct injection for e_M ≤ o_R, bypassing factor-of-2)
Target: L(n) for ALL n via the certified `e_M ≤ o_R` reduction (lower bound, general n).
Technique: Hall's marriage / SDR (sum-level, not termwise) + superincreasing-R identity — KB "Hall's marriage theorem / SDR". The explorer found the factor-of-2 gap is a PROOF-TOOLING gap (0 violations n=3..7, slack `o_R−e_M` GROWS with n: 0,0,0.10,0.64,1.15) — so a direct injection bypassing the L(n)-on-R induction should exist.

Skeleton:
  1. Import certified `lemma-em-or-reduction` (`L(n+1) ⟺ e_M ≤ o_R`), `lemma-self-compensation` (RM pairs self-compensate → residual Match `Σ_MM m_even ≤ Σ_RR r_odd`), `lemma-superincreasing-R` (`a_j − Σ_{l>j} a_l = α(n+1)`).
  2. The m_1-split fix (round 5) gives TWO Hall matchings: **(H1)** on rank indices (Branch 1, `m_1≥a_1`), **(H2)** on the rest polytope (Branch 2, `m_1<a_1`), both verified n=1..5 OPEN.
  3. **NEW GAP (direct injection):** construct an injection `φ` from each M-subpiece at a global even rank to a distinct R'-piece at a global odd rank with `φ(piece) ≥ piece` — using the superincreasing identity on the merged-sort interleaving (rank indices, NOT piece sizes — per-position bound `s_{2j} ≤ a_{j+1}` is FALSE, `b=(4/3,4/3,4/3)` counterexample). The injection is sum-level: `Σ_MM m_even ≤ Σ_RR r_odd`.
  4. Branch 2 (`m_1<a_1`): reduce to `oddsum(rest) ≥ 4` on the rest polytope — the round-5 6-piece casework settles n=3; generalize to a Hall-type (H2) on the rest polytope.
  5. Conclude `e_M ≤ o_R`, hence `L(n+1)`; induct.

Key lemma:
  - "Sum-level Hall injection on rank indices" — because the superincreasing identity `a_j − Σ_{l>j} a_l = α(n+1)` geometrically forces each even-rank M-subpiece to be dominated by some odd-rank R'-piece across the merged sort; the slack-grows-with-n signature confirms the injection is loose, not tight.

Open gaps: step 3 — the explicit injection `φ` (sum-level, on merged-sort interleaving); step 4 — the (H2) general-n Hall matching on the rest polytope; R-refined sub-cases (k≤n) where refinement breaks the superincreasing lever. Watch: do NOT use the FALSE `σ≤M/2=a_1` corollary (removed round 5). Watch: the per-position bound fails — the matching must be on the SUM.

Distinct from: cell-complex-l3 (determinant/2-adic, not Hall). Distinct from two-regime (n=3 upper). Far from dyadic-halving (dead 2-adic-strict-decrease).

---

### self-reproducing-invariant: NEW
Target: U(n) for ALL n (general upper bound, non-strict `cap(P) ≤ α(n)`), via a self-reproducing invariant (crux `aimo-0262` Cinderella/Stepmother template), FAR from the dead 2-adic strict-decrease AND the two-regime sliver casework.

Technique: Self-reproducing invariant on the pair-excess vector `(e_1,…,e_n, ℓ)` — KB "Invariants & monovariants" + "Constructive / incremental". The pair-pile IS such an invariant (it reproduces under level-1-exact perturbations, ridge `R_e` witnesses tight non-strict cap). The equality locus `E_n` (Opening 1) is the set where it reproduces exactly.

Skeleton:
  1. Formalize the pair-pile as a self-reproducing invariant on `(e_1,…,e_n, ℓ)`: after Xiang's marks, the invariant is `{e_i ∈ {0,1}, ℓ ∈ {0,1}, Σ e_i + ℓ = 1}` (integer scale, `A = α(n)` real). State the reproduction rule: how a Liu perturbation (breaking level-`j` exactness) maps to an `e_i`-shift.
  2. Prove `E_n` (equality locus) contains the dyadic + the ridge family `R_e` (level-1 exact, deeper levels perturb with compensating excesses `(1−e)+e=1`); conjecture general form: `P` such that for some `j`, levels 1..j are exact and levels j+1..n perturb with pair-excesses summing to `α(n)` (the self-reproduction condition).
  3. **GAP (the hard case, far-from-dyadic):** for `P ∉ E_n`, prove the invariant REPRODUCES with residual cap staying `≤ α(n)` (non-strict). If the bare pair-pile fails (mirror overshoots to `A=0.8` on extreme-dominant, the explorer PROBED dead this round), ENRICH the invariant to a FAMILY indexed by which halving-level is broken — a non-strict version of the Φ organization.
  4. Conclude `cap(P) ≤ α(n)` for ALL `P`; combined with L(n) gives `c(n) = f(n)` for ALL n.

Key lemma:
  - "Self-reproduction of the pair-excess invariant" — because the pair-pile's binary structure (each `e_i ∈ {0,1}`) is the fixed-point of the halving operator, and perturbations off the fixed-point redistribute mass into compensating pair-excess shifts (the `(1−e)+e=1` signature of the ridge); crux `aimo-0262` disjoint-pair averaging is the template for bounding `Σ e_i + ℓ`.

Open gaps: step 2 — the characterization of `E_n`; step 3 — the far-from-dyadic enriched invariant family (the WALL with two-regime re-emerges here; the genuine escape is to prove far-from-dyadic by a DIFFERENT mechanism, e.g. the S1/S3 sliver lemmas already certified, leaving the pair-pile invariant for the near-dyadic equality locus). Watch: **single-gap-trap risk** — if step 3 reduces to the two-regime sliver casework, this approach dies with two-regime. Mitigation: field the invariant as a FAMILY (one per structural class), and use the S1/S3 certified slivers as the far-from-dyadic members so the family is heterogeneous, not one wall.

Cases to cover: near-dyadic (pair-pile invariant reproduces); balanced (S1 sliver, certified); extreme-dominant (S3 sliver, certified); moderate-dominant (the gap — needs a new invariant member).

Distinct from: dyadic-halving-induction (strict-decrease DEAD; this is non-strict + structural invariant, not Φ-monovariant). Distinct from two-regime (one invariant family, not per-config 17-family casework). Distinct from cell-complex (upper bound, not lower).

---

### dyadic-halving-induction: RETIRE
Target: was U(n) via 2-adic Φ strict-decrease; central route FALSIFIED (ridge `R_e`, certified `lemma-ridge-falsification.md`). Two harvestable lemmas (Φ=0 uniqueness, local-kink) ALREADY certified to cache. The non-strict far-from-dyadic remnant overlaps two-regime (single-gap-trap risk, flagged round 5). Recommendation: **RETIRE** — the Φ structural-identity is captured in the cache (importable by `self-reproducing-invariant` as the non-strict organization if useful), and the live upper-bound work is carried by `two-regime-disjunctive` (n=3) and `self-reproducing-invariant` (general-n). No live engine remains; keeping the slug starves the field. The outliner does NOT re-conceive — the genuinely-different G2 route is the NEW `self-reproducing-invariant`, which is far from the dead strict-decrease.

---

### Diversity check
- `two-regime-disjunctive` (ADVANCE): n=3 upper bound, 7-cap casework — closes c(3).
- `cell-complex-l3` (ADVANCE): general-n lower bound, 2-adic/determinant (D3) — number-theoretic.
- `pairing-partner` (ADVANCE): general-n lower bound, Hall injection — combinatorial matching.
- `self-reproducing-invariant` (NEW): general-n upper bound, aimo-0262 invariant — structural.
- `dyadic-halving-induction` (RETIRE): dead strict-decrease; lemmas harvested.

The two general-n lower-bound routes (cell-complex D3 vs pairing-partner Hall) share the GOAL but diverge in MECHANISM (determinant/2-adic vs Hall matching on merged sort) — they do NOT share a wall: D3 fails only if the 2-adic-lemma is false (a number-theoretic obstruction); Hall fails only if the injection doesn't exist (a combinatorial obstruction). The two general-n upper-bound routes (two-regime n=3 casework vs self-reproducing general-n invariant) share the sliver wall only in the far-from-dyadic extreme — mitigated by using the certified S1/S3 slivers as heterogeneous family members. No two approaches collapse to one wall.
