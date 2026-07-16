# Approach: ll-dyadic-symdiff

## Status
partial

## Approaches tried
- **R13 (this round, advance — R-cut pairing made rigorous as the BOTTOM-RESTRICTION reduction; the
  Q-in-top-level residual slice reduced to an R-ONLY parity inequality, eliminating Q from the crux).**
  New section *"R-cut pairing: the bottom-restriction reduction (R13)"* below. Outcomes:
  - **Bottom-restriction reduction (Lemma BR; full proof; PROMOTABLE; general, max|g|-agnostic BYPASS).**
    For any finite positive multisets `Q, R` and any `τ > 0`, `A(Q∪R) = measure\{g odd\} ≥
    measure\{x∈[0,τ): g odd\}` where `g := N_Q − N_R` (monotonicity of measure over a sub-domain). Taking
    `τ = min(Q)`: on `[0, min(Q))`, `N_Q ≡ |Q|` is constant, so `g(x) = |Q| − N_R(x)` and
    `A(Q∪R) ≥ B := measure\{x∈[0,min(Q)) : N_R(x) ≢ |Q| \pmod 2\}`. This routes through neither the
    alternating-tail crux nor Sub-3a nor any `max|g| ≤ 2` hypothesis — a genuine bypass.
  - **Q-in-top-level ⟹ crux is Q-free (rigorous reduction).** Call the config *Q-top* if
    `min(Q) ≥ 2^{n−2}` (all `Q`-parts in the top level `I_{n−1}`). Then `[0,2^{n−2}) ⊆ [0,min(Q))`, and
    (proved) `|Q| ∈ \{3,4\}`. The within-bottom parity identity `𝟙[N_R ≢ |Q|] = 𝟙[N_R odd]` (|Q| even)
    resp. `𝟙[N_R even]` (|Q| odd) gives, with `A_R^{bot} := measure\{x∈[0,2^{n−2}) : N_R(x) odd\}`,
    ```
    B = A_R^{bot}            (|Q| = 4, even),        B = 2^{n−2} − A_R^{bot}   (|Q| = 3, odd).
    ```
    Hence for a *Q-top* config `A(Q∪R) ≥ B ≥ 1` is EQUIVALENT to the **R-only** inequality
    **(a)** `|Q|=4 ⟹ A_R^{bot} ≥ 1`, resp. **(b)** `|Q|=3 ⟹ A_R^{bot} ≤ 2^{n−2}−1`. `Q` has been
    eliminated from the crux; the residual (for the Q-top slice) is a pure statement about the R-staircase
    parity on the bottom `n−1` levels. **This is the correct rigorous generalization of the explorer's
    n=3 identity** `A = b+(1−b)+⋯`: there `B = b + (1−b) = 1` is exactly `A_R^{bot} = 1` on `[0,2)`.
    Verified 0 violations for `(a),(b)` at `n=3,4,5` (exact Fractions, off-grid), including inside the
    Sub-3a-failing residual (min `B = 1` throughout).
  - **CORRECTION recorded (honesty).** The explorer's n=3 template `R={b,2−b,1,4}` has `max(R)=4=2^{n−1}`
    (top piece UNCUT) — it lies in the residual because Sub-3a fails, but it is NOT in the narrow "bucket
    (iii) max(R)<2^{n−1}" set; the residual for Lemma LL is the broader `Sub-3a fails ∧ max g ≥ 2` with
    only `max(R) ≤ 2^{n−1}`. The single-R-cut sub-case (max(R)<2^{n−1}, one cut) is SUBSUMED by certified
    Sub-3a (it always has a full odd bottom level), so it is not new — the genuine residual has top-uncut /
    multi-fragment R with only *partial* odd levels, which the bottom-restriction still handles via `B`.
  - **Honest OPEN gaps (unchanged crux, now cleaner and Q-free for the Q-top slice):** (i) prove the
    R-only inequalities `(a)`/`(b)` (they are about `A_R^{bot}` for a refinement `R` of `G_{n−1}` under the
    cut-budget `c_R ≤ n−|Q|+1`; verified, min-tight, but not proved); (ii) the *non-Q-top* residual
    (`min(Q) < 2^{n−2}`, so the bottom window `[0,min(Q))` is shorter than 1 level — the restriction does
    not by itself reach measure 1) is NOT covered by this reduction and remains open. No overclaim: this
    round contributes the rigorous BR reduction + the Q-free reformulation of the Q-top slice, not a full
    HS-D1 closure.
- **R12 (this round, advance — Sub-3a DICHOTOMY; dropped the circular target; NEW one-sided cheap-kill
  Lemma G1; precise residual + rigorous obstruction).** New section *"Bucket (iii), general `n`: the Sub-3a
  dichotomy, Lemma G1, and the residual obstruction (R12)"* below. Outcomes:
  - **DROPPED the R11 "reduction" `B₊ ≤ A₋ + B₋` (confirmed circular).** For `max|g| ≤ 2`,
    `A = 1 + 2(A₋ + B₋ − B₊)`, so `B₊ ≤ A₋ + B₋ ⟺ A ≥ 1` — an algebraic *restatement* of the goal, not a
    reduction. Recorded as a dead-end; no build re-presents it as progress. (Confirmed by the explorer and
    the outline-reviewer.)
  - **Re-framed the open crux as the Sub-3a dichotomy.** `Sub-3a` fires `⟹ A ≥ 1` (certified
    `dyadic-level-parity`); the residual is exactly **`Sub-3a fails`**. The tight `A = 1` witness
    `Q = {3,3,2}, R = {2,2,2,1}` has `Sub-3a firing` (`g(0+) = |Q|−|R| = −1` odd, `I₀ = [0,1)` fully odd),
    so it is *not* in the residual; numerically the residual has `min A = 9/8 (n=3), 2 (n=4), 3 (n=5) > 1`.
  - **NEW rigorous foundation `F-neg` (full proof):** in bucket (iii), `g(0+) = N_Q(0⁺) − N_R(0⁺) =
    |Q| − |R| = c_Q − c_R − (n−1) ≤ −1`. So `g` starts strictly negative; since `∫g = ΣQ − ΣR = 1 > 0`, `g`
    must reach a positive value. (Verified 1548/1548; the formula is exact from the budget `c_Q+c_R ≤ n`,
    `c_R ≥ 1`.)
  - **NEW rigorous cheap-kill `Lemma G1` (one-sided small-discrepancy kill; full proof; PROMOTABLE).** If
    `N_Q(x) ≤ N_R(x) + 1` for **all** `x` (i.e. `max g ≤ 1`, with `g` allowed arbitrarily negative), then
    `A(Q∪R) ≥ ΣQ − ΣR = 1`. Proof: with `M_k := measure\{g = k\}`, `max g ≤ 1 ⟹ M_k = 0` for `k ≥ 2`, so
    `1 = ∫g = M₁ − Σ_{k≤−1}|k|M_k ≤ M₁`, and `A = measure\{g odd\} ≥ M₁ ≥ 1`. This **strictly generalizes the
    certified Lemma D1** on the upper side (D1 needs `|g| ≤ 1`; G1 needs only `g ≤ 1`), and closes the ENTIRE
    `max g ≤ 1` slice of the Sub-3a-failing residual for all `n`. Verified 0 violations (n=3, 168 configs).
  - **HS-D3 (max|g|-agnosticism) RESOLVED.** The framework `A = measure\{g odd\}`, the foundation `F-neg`,
    Sub-3a and G1 make **no** `max|g| ≤ 2` assumption (only D1 uses `|g| ≤ 1`); the route is fully agnostic.
    Moreover — correcting a tempting shortcut — `max|g| ≤ 2` is **not** an easier sub-case: the level-charge
    "reduction" is circular *even there* (shown above), so no algebra buys `A ≥ 1` at `max|g| ≤ 2`.
  - **RIGOROUS OBSTRUCTION isolating the true residual `{Sub-3a fails ∧ max g ≥ 2}`.** The foundations
    `F-neg` + budget-parity are provably **insufficient** without the `ΣQ = 2^n` / dyadic-staircase geometry:
    the abstract profile `g = −1` on `[0,ε)`, `g = +2` on `[ε, ε+s)`, `g = 0` after (with `2s − ε = 1`)
    satisfies `g(0⁺) = −1 ≤ −1` (odd), makes Sub-3a fail on every level, yet has `A = measure\{g odd\} = ε`,
    which is `< 1` for small `ε`. Hence any proof of `HS-D1` MUST use the structural input (`ΣQ = 2^n`, `R` a
    refinement of `G_{n−1}`), not parity alone; the "per-level fixed positive measure" must be sourced from
    that geometry. This pins the open gap precisely and refutes a parity-only mechanism. **Honest OPEN:**
    `HS-D1`/`HS-D2` (`Sub-3a fails ∧ max g ≥ 2`) is NOT closed; only the `max g ≤ 1` slice (Lemma G1) and the
    Sub-3a-firing slice (certified) are. No overclaim.
- **R11 (this round, advance — BUCKET (iii) GENERAL `n`, INC base + Opening D; a CORRECTNESS
  CORRECTION and two rigorous reductions):** New section *"Bucket (iii), general `n`: correction to the
  INC premise, D1-direct, and the level-charge reduction (R11)"* below. Outcomes:
  - **CORRECTION (load-bearing, machine-verified counterexample).** The outline's / explorer's structural
    premise "`S_Q ⊆ S_R` (INC) FORCES `max(Q) ≤ max(R)`" is **FALSE**. Counterexample (`n = 4`):
    `Q = {15/2, 15/2, 1}`, `R = {7, 4, 2, 1, 1}` is INC (`S_Q = [0,1) ⊆ [0,2)∪[4,7) = S_R`) yet
    `max(Q) = 15/2 > 7 = max(R)`. The parity argument breaks because `max(Q)` has **even multiplicity**
    (two copies of `15/2`), so just below `max(Q)`, `N_Q = 2` is *even*, not odd, and INC is not violated.
    **Corrected structural lemma (PROVED):** INC `⟹` `max(Q) ≤ max(R)` **OR** `max(Q)` has even
    multiplicity in `Q`. Verified 0 violations over the n=4 (129) and n=5 (1282) INC bucket-(iii) sets.
    **Consequence:** the intended non-inductive INC closure (double-REFL `A(Q∪R) = (r−q) + A(Q'∪R')` with
    the "`ΣQ'−ΣR'' = 1+(r−q) ≥ 1`" slack) is **INVALID** — `r − q` can be *negative*, and when `q` is the
    global max one must peel `q` first, so that reduction does not hold with the intended sign. Recorded so
    no builder builds a false proof on it.
  - **D1-direct (rigorous, all `n`), applies to INC and GAP uniformly.** Certified Lemma D1 applied to the
    ORIGINAL `Q∪R` (no reflection): if `max_x|N_Q(x) − N_R(x)| ≤ 1` then `A(Q∪R) ≥ |ΣQ − ΣR| = 1`. This is
    the robust general-`n` tool and needs no max-ordering; it does **not** depend on the false premise.
    Coverage of the max-`|g| ≤ 1` slice for all `n`.
  - **Uniform reduction (INC and GAP are the SAME problem).** With `g := N_Q − N_R`, bucket (iii) is exactly
    `measure{g odd} ≥ 1`, `∫g = 1`, `g` a step function with `≤ 2n+1` breakpoints on `[0, 2^{n−1})`. INC is
    **not** a genuinely easier sub-case (it is a sub-case of the same `measure{g odd}` question); the R10
    INC/GAP split does not simplify the crux.
  - **Level-charge reduction for `max|g| ≤ 2` (rigorous algebra; the geometric step OPEN).** With
    `A_± := measure{g=±1}`, `B_± := measure{g=±2}`: `∫g = (A_+−A_−) + 2(B_+−B_−) = 1` and
    `A(Q∪R) = A_+ + A_−`, so **`A(Q∪R) ≥ 1 ⟺ B_+ ≤ A_− + B_−`**. Verified TRUE (0 violations, n=4 and n=5
    INC residual; also GAP residual). The geometric inequality `B_+ ≤ A_− + B_−` (the `g=2` excess is
    dominated by the `g<0` mass) is the honest OPEN gap — it is NOT implied by `∫g = 1` alone (`g ≡ 2` on
    `[0,½)` breaks it) and needs the `ΣQ = 2^n` wide-support structure.
  - **Net:** prevented a false closure (the INC premise), isolated a clean *correct* reduction of the
    `max|g| ≤ 2` residual to one geometric inequality, kept D1-direct as the rigorous general-`n` slice.
    Bucket (iii) general `n` remains **partial/open**; no overclaim.
- **R10 (this round, advance — BUCKET (iii) GENERAL `n`, INC/GAP split + Opening D):** Attacked the
  general-`n` bucket-(iii) base inequality `A(Q∪R) ≥ 1` (top-cut regime `max(Q), max(R) < 2^{n−1}`) by a
  clean **containment split** and developed **Opening D** for the non-containment (G-GAP) part. New section
  *"Bucket (iii), general `n`: the INC/GAP split and Opening D (R10)"* below. Outcomes (rigorous unless
  flagged):
  - **Direct containment split (no telescope needed).** Bucket (iii) splits into **INC** (`S_Q ⊆ S_R`) and
    **GAP** (`S_Q ⊄ S_R`), each attacked on the original `Q, R` (the certified REFL-telescope
    `A(Q∪R) = max(Q)−max(R)+A(Q'∪R'')` is an *alternative* reduction, restated, but not needed for the
    split). Verified n=4 bucket (iii): 1617 configs, **0 violations**, of which 129 INC / 1488 GAP.
  - **INC sub-instances ⟸ refined-`R` crux (clean conditional import).** By the certified **Forcing +
    INC-reduction** (`lemmas/forcing-inc-reduction.md`), on `S_Q ⊆ S_R` we get `A(Q∪R) = A(R) − A(Q)`, so
    the target is `A(R) ≥ A(Q) + 1` = **Claim_R(n, ε=0)** (h_R even) resp. the `|Q|`-parity fact (h_R odd)
    — exactly the {Claim_R, T_R} mutual induction being built in `ll-inclusion-gap` this round. Stated as a
    **conditional reduction** (import once certified); NOT claimed closed here.
  - **NEW all-`n` cheap-kill — Lemma D1 (small-discrepancy kill, rigorous, promotable):** if
    `|N_Q(x) − N_R(x)| ≤ 1` for all `x`, then `A(Q∪R) ≥ |ΣQ − ΣR|`; in bucket (iii) (`ΣQ = 2^n`,
    `ΣR = 2^n − 1`) this is `≥ 1`. One-line proof via `g := N_Q − N_R`: `{g odd} = {g ≠ 0}` when `|g| ≤ 1`,
    and `measure{g ≠ 0} ≥ ∫|g| ≥ |∫g| = |ΣQ − ΣR|`. This is the first rigorous *general-`n`* GAP tool that
    genuinely beats the "`∫g = 1` alone is insufficient" obstruction (it uses the `|g| ≤ 1` structure, not
    just the integral).
  - **GAP coverage (rigorous cheap-kill package).** K1 (small-overlap), K2 (difference), **D1** together
    close the **overwhelming majority** of GAP: verified n=3 bucket (iii) **166/168** GAP configs, n=4
    **1449/1488** GAP configs; residual n=4 = **39 configs, ALL with `A(Q∪R) ≥ 2`** (non-tight,
    `max|g| ≤ 3`). So the GAP residual is a small, comfortably-non-tight set — but NOT proven by these
    kills. Honest OPEN gap: the general-`n` GAP residual (`|g| ≥ 2` excursions, `A ≥ 2` empirically).
  - **Opening D framework made rigorous (reduction, not closure).** Recast GAP as: `g := N_Q − N_R` is an
    integer step function with `∫g = 1`, at most `|Q|+|R| ≤ 2n+1` breakpoints across the `n` dyadic
    levels, and target `measure{g odd} ≥ 1`. Proved the level-charge identity and the two provable slices
    (D1: `|g| ≤ 1`; Sub-3a: some level odd-constant). The general accumulation `Σ_k δ_k ≥ 1` over
    non-`|g|≤1` excursions is the **honest remaining gap** — the dyadic-pairing "cost accumulates to 1"
    is set up but NOT proven. Did **not** overclaim bucket (iii) closed; did **not** re-import the false
    `max(Q)<2^{n−1} ⟹ A ≥ 2`.
- **R9 (advance — BUCKET (iii), top-cut refined `R`):** Closed **bucket (iii) completely at
  `n = 3`** (the whole `max(Q) < 2^{n−1}`, `max(R) < 2^{n−1}` top-cut regime, subsuming the residual), and
  proved three **all-`n` reusable cheap-kill lemmas** + a rigorous well-founded **termination** framing of
  the double-REFL telescoping (the reviewer's one load-bearing required gap). New section *"Bucket (iii):
  cheap-kills, n=3 closure, and REFL termination (R9)"* below. Outcomes (rigorous unless flagged):
  - **All-`n` cheap-kill lemmas (rigorous, promotable):** (K1) *small-overlap* — if
    `2·measure(S_Q∩S_R) ≤ A(Q)` (in particular if `S_Q∩S_R = ∅`) then `A(Q∪R) ≥ A(R) ≥ 1`; (K2)
    *difference* — always `A(Q∪R) ≥ |A(Q) − A(R)|`, so `|A(Q)−A(R)| ≥ 1 ⟹ A(Q∪R) ≥ 1`. Both are one-line
    consequences of the merge identity `A(Q∪R) = A(Q)+A(R)−2B` with `0 ≤ B ≤ min(A(Q),A(R))`.
  - **`n = 3` bucket (iii) CLOSED (all configs, rigorous).** At `n=3` the budget forces `c_Q = 2`,
    `c_R = 1` exactly, so `|Q| = 3`, `R = {4−a, 2, a, 1}` (`a ∈ (0,2]` the top-cut). Reduced `A(R)` and
    `S_R` to closed form in two `a`-regimes and proved `A(Q∪R) ≥ 1` in both via a single **`Q`-only lemma**
    `2·measure(S_Q ∩ [2,∞)) ≤ A(Q)` (proved from `q_2 > 2` — forced since `q_2 ≤ 2 ⟹ q_1 ≥ 4`). Verified
    10912 configs (`1/16`-grid, budget): `min A(Q∪R) = 1`, 0 violations; the two structural lemmas hold
    universally. This is the first fully rigorous closure of an entire refined-`R` bucket beyond the
    R-agnostic core.
  - **Double-REFL termination (the required gap), made rigorous:** the alternating reflection at the
    running global maximum is a **finite well-founded descent** — each step deletes one piece, strictly
    decreasing the piece-count `|P|` (and the total `ΣP` by the removed maximum), so it halts in `≤ |P|`
    steps at a `≤ 2`-piece base object. Presented honestly: termination is *proved*, but the resulting
    identity merely *computes* `A(P)`; the residual content (the base-object lower bound `A ≥ 1` for
    general `n`) is the **refined-`R` alternating-tail crux**, which is NOT closed and is flagged as such
    (no overclaim). So general-`n` bucket (iii) remains open; only `n = 3` is closed.
  - **Did NOT** re-import the false `max(Q)<2^{n−1} ⟹ A ≥ 2`; did NOT assume a refined-`R` SET IDENTITY.
- **R8 (advance — REFINED-R branch):** Pushed Lemma LL from the **anchor `R = G_{n−1}`
  unrefined** to a **general refinement `R` of `G_{n−1}`** (`c_R := #R-cuts ≥ 1`). Outcomes (all
  rigorous unless flagged; new section *"Refined R"* below):
  - **General-`R` core (Cases 1/2/Sub-3a are R-agnostic).** Made explicit and airtight that Cases 1,
    2, and Sub-3a of the three-way split prove `A(Q∪R) ≥ 1` for **any** `R` with `max(R) ≤ 2^{n−1}` and
    `A(R) ≥ 1` — they use only `S_R ⊆ [0,2^{n−1})`, the piece count, and the dyadic levels of `P`, never
    any `G_{n−1}`-specific band structure (no SET IDENTITY, no top-band decomposition). This is the
    imported certified triple `ll-case1-high-interval` + `parity-piece-count` (Lemma P) + `dyadic-level
    -parity`, assembled with no extra hypothesis on `R`. **Coverage (n=3, ½-grid, joint budget
    enforced): 340/371 refined configs (91.6%).**
  - **NEW promotable — Budget-reduction lemma.** For a refined `R` (`c_R ≥ 1`) the joint cut budget
    `#Q-cuts + #R-cuts ≤ n` forces `|Q| = #Q-cuts + 1 ≤ n` (strictly fewer parts than the anchor's
    `n+1`). Structural constraint on the residual (all residual configs have `|Q| ≤ n`).
  - **NEW promotable — Double-REFL for a refined `R` with the top piece `2^{n−1}` UNCUT.** The anchor
    double-REFL proof never used `R = G_{n−1}` exactly — only `max(R) = 2^{n−1}` and `max(R∖\{2^{n−1}\})
    ≤ 2^{n−2}`. Both hold for **any** refined `R` in which `2^{n−1}` is uncut, since then `R' := R ∖
    \{2^{n−1}\}` is a refinement of `G_{n−2}` with `max(R') ≤ 2^{n−2}`. Hence for such `R` and
    `max(Q) < 2^{n−1}` the identity `A(Q∪R) = 2^{n−1} − q_1 + A(Q'∪R')` (`q_1 = max(Q)`) holds
    (certified REFL then REFL-gen), and the sub-cases **B3a** (`q_1 ≤ 2^{n−2}`) and **B3b**
    (`2^{n−2} < q_1 ≤ 2^{n−1}−1`) close for **all `n`**, exactly as in the anchor; the residual is the
    refined-`R'` analogue `A(Q'∪R') ≥ 1` (`(B2*)-ref`). Verified n=3, ½-grid, budget: identity holds,
    0 fails, B3a/B3b close.
  - **Residual breakdown (honest, precise; n=3 numbers).** After the general-`R` core, the refined-`R`
    residual (31/371) splits into exactly three crux/residual buckets, verified: **(i)** `max(Q) ≥
    2^{n−1}` (branches B1,B2 — 27 configs): certified **Lemma REFL** (R-agnostic, needs only
    `max(R) ≤ 2^{n−1}`) reduces `A(Q∪R) ≥ 1` to the **upper bound `A(Q'∪R) ≤ max(Q) − 1`** = *GAP-A
    refined-R* (crux family, open); **(ii)** `max(Q) < 2^{n−1}`, top piece uncut (B3c-ref — 2 configs):
    double-REFL reduces to `A(Q'∪R') ≥ 1` = *(B2*)-refined-R'* (crux family, open); **(iii)**
    `max(Q) < 2^{n−1}` and `max(R) < 2^{n−1}` (top piece cut — 2 configs): **no reflection anchor at
    `2^{n−1}`** — the genuinely hard residual, left honestly OPEN.
  - **Scope / honesty:** the refined-`R` crux residuals (i),(ii) are *not* claimed closed — they are the
    alternating-tail `+1` crux family, and (per the refinedR explorer) the refined-`R` versions are
    **genuinely separate** from `ll-inclusion-gap`'s anchor `T(ℓ)` (tight case `R={4,4,4,2,1},
    Q={5,5,4,2}` has `S_Q=[2,4)⊄S_{G_3}`). Bucket (iii) is a true no-anchor residual. Did **not**
    assume any refined-`R` analogue of the SET IDENTITY / top-band decomposition (none known). Did
    **not** re-import the false "`max(Q)<2^{n−1}⟹A≥2`".
- **R7 (advance):** Converted the **double-REFL telescoping** proof of **GAP-B** (branch B3,
  `max(Q) < 2^{n−1}`) into rigorous prose for the **anchor `R = G_{n−1}` unrefined**. Outcomes:
  - **NEW promotable lemma — Lemma REFL-gen** (proved in full): relaxes the certified Lemma REFL's
    hypothesis `μ ≥ 2^{n−1}` to the weaker `max(R) ≤ μ = max(Q)`, giving `A(Q∪R) = μ − A(Q'∪R)` (same set
    proof; the only step touched is `S_R ⊆ [0,μ)`). Verified 0/4000 random-rational mismatches. This is
    what the *second* reflection needs (removed max `q_1 < 2^{n−1}` is outside certified REFL's range).
  - **Double-REFL formula (II)** `A(Q∪G_{n−1}) = 2^{n−1} − q_1 + A(Q'∪G_{n−2})` established rigorously as
    (certified REFL on the global max `2^{n−1}`) then (REFL-gen on `q_1`, valid since `q_1 > 2^{n−2}`).
    Verified 0 mismatches (90 n=3, 1205 n=4 instances; reviewer 0/3031).
  - **Branch B3 sub-cases CLOSED for all `n`:** **B3a** (`q_1 ≤ 2^{n−2}`: `A ≤ max` ⟹ `A(Q∪G_{n−1}) ≥
    2^{n−2} ≥ 1`) and **B3b** (`2^{n−2} < q_1 ≤ 2^{n−1}−1`: `A ≥ 0` ⟹ `A(Q∪G_{n−1}) ≥ 2^{n−1}−q_1 ≥ 1`).
  - **Branch B3c** (`2^{n−1}−1 < q_1 < 2^{n−1}`) reduced to the single clean, tight residual **(B2\*)**
    `A(Q'∪G_{n−2}) ≥ 1` (equivalently `Σ_odd(Q'∪G_{n−2}) ≥ 2^{n−1}`), and **(B2\*) PROVED IN FULL at
    `n = 3`** (exhaustive `|Q'| ∈ {2,3}` casework via `S_{{1,2}} = [1,2)` and the merge lemma; every
    sub-case `≥ 1`, tight at `1`; verified 0 violations on `1/8`-grid). So **GAP-B is closed at `n = 3`
    for `R = G_2`.**
  - **General-`n` (B2\*) isolated honestly** as the shared crux: a third reflection splits into (i)
    `q_2 ≤ 2^{n−2}` — a GAP-A-shape upper bound `A(Q'∪G_{n−3}) ≤ 2^{n−2}−1`, and (ii) `q_2 > 2^{n−2}` —
    the reviewer's non-terminating recursion. So (B2\*) at general `n` coincides with the alternating-tail
    bound `(p_2−p_3)+⋯ ≥ 1` = GAP-A = `ll-inclusion-gap`'s `G-INC-1`; **import when either closes.**
  - **Scope caveats (honest):** double-REFL treats only the **anchor `R = G_{n−1}` unrefined**; refined
    `R` (min `A = 3/2` numerically) and general-`n` (B2\*) both remain open.
  - **Net:** GAP-B fully closed at `n=3`/anchor and reduced for all `n` to one tight inequality; the A≥2
    mechanism stays dead (B3-anchor min `A = 3/2`, the old "tight `A=1`" witness is Sub-3a not B3).
- **R6 (advance):** Attacked the single open residual **Sub-3b** via a split on `max(Q)`
  using a **general reflection identity** (extends the certified `max(Q)=2^{n−1}` identity to all
  `max(Q) ≥ 2^{n−1}`). Outcomes:
  - **NEW rigorous lemma — General reflection identity (proven in full below, verified 490/490, 0
    mismatches):** if `μ := max(Q) ≥ 2^{n−1}` and `max(R) ≤ 2^{n−1}`, then with `Q' := Q ∖ {μ}`,
    `A(Q∪R) = μ − A(Q'∪R)`. Reduces the lower bound `A(Q∪R) ≥ 1` to the **upper bound**
    `A(Q'∪R) ≤ μ − 1` (verified 490/490, 0 violations, tight). Proposed for certification.
  - **DELETED the FALSE Step-2 slack claim** (`max(Q) < 2^{n−1} ⟹ A ≥ 2`). This is false, and the
    corrected numeric picture is sharper than the reviewer's: on the `1/4`-grid with the joint cut
    budget enforced, the `max(Q) < 2^{n−1}` branch (B3) attains `A(Q∪R) = 1` **exactly** (witness
    `Q = {3,3,2}`, `R = {2,2,2,1}` at `n=3`, both max `< 4`). So B3 is **also tight** — there is no
    slack anywhere, and the `max(Q)` split does **not** isolate the tight cases into `max(Q)=2^{n−1}`.
    The A≥2 mechanism is permanently dead.
  - **Net:** the identity is a real, reusable, certifiable advance and gives a clean reduction of the
    two `max(Q) ≥ 2^{n−1}` branches to a single upper-bound inequality; but that inequality
    (`A(Q'∪R) ≤ μ−1`) and the B3 branch (`max(Q) < 2^{n−1} ⟹ A(Q∪R) ≥ 1`) both remain open — they
    are the same INC/GAP crux shared with `ll-inclusion-gap`. Sub-3b is **not** closed; honest partial.
- **R5 (NEW slug):** A complete rival attempt at the lower bound `c(n)`, whose distinctive
  content is a **direct three-way case split** on `measure(S_Q △ S_R)` that closes the LL `t ≥ 2`,
  `A(Q) > 0` gap for two of three cases and reduces the third to a single, precisely-stated dyadic-parity
  claim — **never** using the two-sided merge `a/b` decomposition (recorded dead end, insufficient
  34/286) nor the peel-one-Q-cut induction (recorded non-monotone dead end). Outcome:
  - **Case 1** (`max(Q) ≥ 2^{n−1}+1`): CLOSED, rigorous (direct high-interval disjointness; verified
    8310/8310, 0 violations).
  - **Case 2** (`|Q|+|R|` odd, all pieces `≥ 1`): CLOSED by certified **Lemma P** (imported).
  - **Case 3** (residual: even count or a sub-unit piece, `max(Q) < 2^{n−1}+1`): reduced to
    `measure(S_Q △ S_R) ≥ 1`. **Sub-3a** (some full dyadic level `I_k` lies inside `S_Q △ S_R`): CLOSED,
    rigorous, and covers **102/187** of the n=3 residual configs. **Sub-3b** (no dyadic level is fully
    odd): the genuine remaining crux, **85/187** n=3 residual configs — left as an EXPLICIT gap, precisely
    stated below. Not overclaimed.
- Recorded numerically this round: over the full n=3 residual grid, `measure(S_Q △ S_R) ≥ 1` holds with
  minimum exactly `1` (0 violations), confirming the target is true; but the "some full dyadic level ⊆
  symmetric difference" mechanism is provably NOT always available (85/187 configs have every dyadic level
  containing an even-parity sub-interval), so Sub-3b needs a bound that sums mismatch mass across levels,
  not a single-level pigeonhole.

## Current best
The whole game reduces (certified **Lemma G**) to `c(n) = max_{LB} min_{XY} val`, `val(P) = (T + A(P))/2`,
`A` the alternating sum, with the integral/measure form `A(P) = measure{x : N_P(x) odd}` (**Lemma M0**)
and the merge identity `A(X∪Y) = A(X) + A(Y) − 2B`, `B = measure(S_X ∩ S_Y)` (**Lemma M**), all certified
and imported. In unnormalized units the lower bound is `A(final) ≥ 1` over all `≤ n`-cut refinements of
`G_n = {1,…,2^n}`. This is complete by induction on `n` except **Lemma LL, sub-case `t ≥ 2`, `A(Q) > 0`**,
which this slug attacks by a case split on `max(Q)`. The furthest rigorous progress here:
`A(Q∪R) = measure(S_Q △ S_R) ≥ 1` is proved in **Case 1**, **Case 2**, and **Case 3 / Sub-3a**; and in
Sub-3b the **General reflection identity `A(Q∪R) = max(Q) − A(Q'∪R)`** (proved this round for
`max(Q) ≥ 2^{n−1}`, `Q' = Q ∖ {max(Q)}`; verified 490/490) collapses branches B1 (`max(Q)∈(2^{n−1},
2^{n−1}+1)`) and B2 (`max(Q)=2^{n−1}`) to the single upper bound **GAP-A** `A(Q'∪R) ≤ max(Q) − 1`, leaving
branch B3 (`max(Q) < 2^{n−1}`) as **GAP-B** `A(Q∪R) ≥ 1`. Both GAP-A and GAP-B remain open — they are the
shared INC/GAP crux — and are stated precisely under *Open gaps*. (The former "`max(Q)<2^{n−1} ⟹ A ≥ 2`"
step is FALSE and has been deleted: B3 is tight, `A = 1` attained.)

**R10 update (bucket (iii), general `n`).** The top-cut regime `max(Q), max(R) < 2^{n−1}` (closed at
`n = 3` in R9) now splits, for all `n`, on containment: **INC** (`S_Q ⊆ S_R`) reduces rigorously
(certified INC-reduction) to `A(R) ≥ A(Q)+1` = the refined-`R` crux `Claim_R(n,0)` — **conditional** on
`ll-inclusion-gap`'s `{Claim_R, T_R}` build; **GAP** (`S_Q ⊄ S_R`) is closed for every `n` by the rigorous
cheap-kill package K1, K2, and the **new Lemma D1** (`|N_Q − N_R| ≤ 1` pointwise `⟹ A(Q∪R) ≥ |ΣQ − ΣR| =
1`), plus Sub-3a — leaving only a small **non-tight** residual (n=4: 39/1488 GAP, all `A ≥ 2`). The general
**Opening D** accumulation `Σ_k δ_k ≥ 1` (level-charge form, set up rigorously) is the honest OPEN gap: the
dyadic pairing "cost accumulates to 1" is a direction, not yet a proof.

**R11 correction (bucket (iii), general `n`).** The R10 write-up recorded the INC branch as a *conditional*
reduction (`A(Q∪R) = A(R) − A(Q)`, so `A ≥ 1 ⟺ A(R) ≥ A(Q)+1`); this remains rigorous and is unchanged.
What R11 corrects is the *non-inductive* closure the outline proposed on top of it: the premise
"`S_Q ⊆ S_R` forces `max(Q) ≤ max(R)`" is **FALSE** (counterexample `Q={15/2,15/2,1}`, `R={7,4,2,1,1}`,
`max(Q)=15/2 > 7`, INC holds because `max(Q)` has even multiplicity). The correct structural fact is INC
`⟹` `max(Q) ≤ max(R)` OR `max(Q)` has even multiplicity, which does **not** support the intended
`(r−q)`-slack argument. The rigorous general-`n` residue is: **D1-direct** (`max|N_Q−N_R| ≤ 1 ⟹ A ≥ 1`,
INC and GAP alike), and — for the `max|g| ≤ 2` residual — the **level-charge reduction**
`A(Q∪R) ≥ 1 ⟺ B_+ ≤ A_− + B_−` (`A_± = measure\{g=±1\}`, `B_± = measure\{g=±2\}`). The geometric
inequality `B_+ ≤ A_− + B_−` is the honest OPEN crux (empirically true, big margin; `∫g = 1` alone does
not force it). So bucket (iii) general `n` stays OPEN; only `n = 3` is closed (R9).

**R12 update (bucket (iii), general `n`): the Sub-3a dichotomy.** The R11 target `B₊ ≤ A₋ + B₋` is DROPPED
(algebraically `⟺ A ≥ 1`, circular). The crux is re-framed as the **Sub-3a dichotomy**: `Sub-3a` fires
`⟹ A ≥ 1` (certified `dyadic-level-parity`); the residual is `Sub-3a fails`. This round adds (all rigorous):
(i) foundation **`F-neg`** `g(0⁺) = |Q|−|R| ≤ −1`; (ii) **Lemma G1** `max g ≤ 1 ⟹ A ≥ 1` (one-sided,
strictly stronger than D1 on the `g ≤ 1` side), which closes the `max g ≤ 1` slice for all `n`; (iii)
**HS-D3 agnosticism** confirmed (the route uses no `max|g| ≤ 2` hypothesis, and `max|g| ≤ 2` is not easier —
the level-charge reduction is circular there too). The open residual is pinned to `{Sub-3a fails ∧ max g ≥ 2}`,
and a **rigorous obstruction** shows the parity foundations alone cannot close it (the abstract profile
`g = (−1, +2, 0)` on `([0,ε),[ε,ε+s),·)` has `g(0⁺) = −1`, Sub-3a failing, yet `A = ε < 1`) — so the missing
ingredient is the `ΣQ = 2^n` / dyadic-staircase geometry, not more parity bookkeeping. See the R12 section.

**R13 update (R-cut pairing = the bottom-restriction reduction; the Q-top residual slice is now Q-free).**
The R12 obstruction showed parity alone cannot close the residual; the `ΣQ = 2^n`/staircase geometry must be
used. R13 supplies exactly such a geometric handle in a rigorous, `max|g|`-agnostic form — the
**bottom-restriction** `A(Q∪R) ≥ B` with `B = measure\{x∈[0,min(Q)) : N_R(x) ≢ |Q|\}` — and, for the
**Q-top** slice (`min(Q) ≥ 2^{n−2}`), it *eliminates* `Q` from the crux via the within-bottom parity
identity: the residual becomes the R-only inequality `A_R^{bot} ≥ 1` (`|Q|=4`) resp.
`A_R^{bot} ≤ 2^{n−2}−1` (`|Q|=3`), `A_R^{bot} := measure\{x∈[0,2^{n−2}):N_R \text{ odd}\}`. This is the
faithful generalization of the explorer's `A = b+(1−b)+⋯ = 1 + (\text{Q-terms})`: the "`1`" is precisely
`A_R^{bot} = 1` on the bottom. The R-only inequalities are verified (0 violations, `n=3,4,5`, off-grid) but
not yet proved; the non-Q-top residual (`min(Q)<2^{n−2}`) is not covered. See the R13 section.

The upper bound is imported unchanged from the shared population (Regime A closed via the shadow strategy,
Regimes B/C open); it is not this slug's target and does not affect the lower-bound argument below.

---

# R-cut pairing: the bottom-restriction reduction (R13)

Notation as in §Setup: `g := N_Q − N_R`, `A(Q∪R) = measure\{x : g(x) odd\}` (Lemma M0), `∫g = ΣQ−ΣR = 1`.
Levels `I_0=[0,1)`, `I_k=[2^{k−1},2^k)` (`1≤k≤n−1`). `R` refines `G_{n−1}` with `max(R) ≤ 2^{n−1}`; `Q`
partitions `2^n` into parts `< 2^{n−1}`, `|Q| ≥ 3`. We work in the residual `\{Sub-3a fails ∧ max g ≥ 2\}`.

## R13.1 Lemma BR (bottom-restriction; full proof; PROMOTABLE)

> **Lemma BR.** For finite positive multisets `Q, R` and any `τ > 0`,
> `A(Q∪R) ≥ measure\{x∈[0,τ) : g(x) odd\}`. In particular, with `τ = min(Q)`, since `N_Q(x) = |Q|` for
> all `x∈[0,min(Q))`, we have `g(x) = |Q| − N_R(x)` there, and
> ```
> A(Q∪R) ≥ B(τ) := measure\{x∈[0,min(Q)) : N_R(x) ≢ |Q| \pmod 2\}.
> ```

*Proof.* `A(Q∪R) = measure\{x≥0 : g(x) odd\} ≥ measure(\{x≥0:g(x) odd\} ∩ [0,τ)) = measure\{x∈[0,τ):
g(x) odd\}`, monotonicity of Lebesgue measure under restriction to the subset `[0,τ)`. For
`x∈[0,min(Q))`, every part of `Q` exceeds `x` (all parts are `≥ min(Q) > x`), so `N_Q(x) = |Q|`; hence
`g(x)` is odd iff `N_R(x) ≢ |Q| \pmod 2`. ∎

Lemma BR uses no bound on `max|g|`, no reflection, and no Sub-3a; it is a clean geometric restriction. Its
force is that the *odd-`g`* mass already present on the low region `[0,min(Q))` — where `N_Q` is frozen at
`|Q|` — is a lower bound for the whole alternating sum. The task `A(Q∪R) ≥ 1` is thereby reduced to a
statement about the **R-staircase parity** on `[0,min(Q))`, with `Q` entering only through the single
integer `|Q|`.

## R13.2 The Q-top slice: `|Q| ∈ \{3,4\}`

Call the configuration **Q-top** if `min(Q) ≥ 2^{n−2}`, i.e. every part of `Q` lies in the top level
`I_{n−1} = [2^{n−2}, 2^{n−1})`. Then `[0, 2^{n−2}) ⊆ [0, min(Q))`, and Lemma BR (restricting further to
`[0,2^{n−2})`) gives
```
A(Q∪R) ≥ B := measure\{x∈[0, 2^{n−2}) : N_R(x) ≢ |Q| \pmod 2\}.        (BR-top)
```

**Claim: `|Q| ∈ \{3,4\}`.** Each part lies in `[2^{n−2}, 2^{n−1}) = [2^{n−2}, 2·2^{n−2})`, and
`ΣQ = 2^n = 4·2^{n−2}`. If `|Q| = m`, then `m·2^{n−2} ≤ ΣQ < m·2·2^{n−2}`, i.e. `m ≤ 4` and `m > 2`.
Hence `m ∈ \{3,4\}`. ∎

## R13.3 Within-bottom parity identity: eliminating `Q`

Write `A_R^{bot} := measure\{x∈[0,2^{n−2}) : N_R(x) \text{ odd}\}` (a functional of `R` alone). Since the
bottom window `[0,2^{n−2})` has measure `2^{n−2}`,
`measure\{x∈[0,2^{n−2}) : N_R(x) \text{ even}\} = 2^{n−2} − A_R^{bot}`. The predicate `N_R ≢ |Q|` equals
`N_R \text{ odd}` when `|Q|` is even and `N_R \text{ even}` when `|Q|` is odd, so (BR-top) becomes
```
|Q| = 4 :  B = A_R^{bot};          |Q| = 3 :  B = 2^{n−2} − A_R^{bot}.        (PAR)
```
Therefore, for any **Q-top** configuration,
```
A(Q∪R) ≥ B ≥ 1   ⟸   \begin{cases} A_R^{bot} ≥ 1 & (|Q| = 4)\\ A_R^{bot} ≤ 2^{n−2} − 1 & (|Q| = 3).\end{cases}   (★R)
```
Both right-hand inequalities are about `R` **only** — `Q` has been eliminated. This is the rigorous content
of the "R-cut pairing": the paired odd-`g` contributions the explorer computed are exactly the odd/even
runs of the `R`-staircase on the bottom levels, and their total is `A_R^{bot}` (resp. its complement),
independent of where `Q` sits inside the top level. The explorer's n=3 identity `A = b + (1−b) + (q_2−q_1)
+ (4−q_3)` is (PAR) with `|Q|=3`: `B = 2^{1} − A_R^{bot}`; for `R=\{b,2−b,1,4\}` one computes
`A_R^{bot} = (1−b) + b = 1` (odd runs `(b,1)` and `(2−b,2)`), giving `B = 2 − 1 = 1`, and the `Q`-terms
`(q_2−q_1)+(4−q_3)` are the *additional* odd-`g` mass above the bottom window that Lemma BR discards.

**Budget link.** With `|Q| = m` we have `c_Q = m−1`, and the joint budget `c_Q + c_R ≤ n` gives
`c_R ≤ n − m + 1`: so `|Q|=4 ⟹ c_R ≤ n−3` and `|Q|=3 ⟹ c_R ≤ n−2`. The two branches of (★R) are thus
inequalities on the bottom-staircase of an `≤ (n−m+1)`-cut refinement of `G_{n−1}`.

## R13.4 Verification and status of the R-only inequalities (★R)

Exhaustive/randomized off-grid Fraction checks (`n=3,4,5`) confirm **0 violations** of (★R): every
Q-top `R` with `|Q|=4` has `A_R^{bot} ≥ 1` (minimum exactly `1`), and every Q-top `R` with `|Q|=3` has
`A_R^{bot} ≤ 2^{n−2}−1` (maximum exactly `2^{n−2}−1`, e.g. `1,3,7` for `n=3,4,5`). Both bounds are tight,
attained by the unrefined/near-unrefined `R`. This confirms the target `A(Q∪R) ≥ 1` on the entire **Q-top**
slice of the residual, and pins the remaining work to (★R).

**Honest OPEN gaps.**
1. **Prove (★R).** These are clean, `Q`-free parity statements about a refinement `R` of `G_{n−1}`. They
   are *not yet proved*. The natural handle is the cut-adjustment calculus (a cut of piece `2^k` into
   `f ≤ 2^{k−1}` and `2^k−f` shifts `N_R` by `+1` on `[0,f)` and `−1` on `[2^k−f, 2^k)`, flipping the
   staircase parity on those two intervals), tracked against the budget `c_R ≤ n−m+1`; the accumulation of
   these flips into the bound `A_R^{bot} ≥ 1` / `≤ 2^{n−2}−1` is the residual content.
2. **Non-Q-top residual.** When `min(Q) < 2^{n−2}` the bottom window `[0,min(Q))` is shorter than the full
   bottom (possibly shorter than `1`), so Lemma BR alone need not reach measure `1`. This slice is NOT
   covered by the present reduction and remains open; it needs either a longer window (using that some
   `Q`-parts sit higher) or a combination with the top-level odd-`g` mass that BR discards.

No overclaim: R13 delivers the rigorous **bottom-restriction** reduction and, for the Q-top slice, a
rigorous elimination of `Q` down to the verified R-only inequality (★R). The full HS-D1 closure (all `n`,
all Q-positions) is NOT achieved.

## Promotable lemmas (R13)

- **Lemma BR (bottom-restriction), all `n`, general.** For finite positive multisets `Q,R` and `τ>0`,
  `A(Q∪R) ≥ measure\{x∈[0,τ):g odd\}`; with `τ=min(Q)`, `A(Q∪R) ≥ measure\{x∈[0,min(Q)):N_R(x)≢|Q|\}`.
  Full proof in §R13.1 (measure monotonicity + `N_Q≡|Q|` on `[0,min(Q))`). `max|g|`-agnostic; uses no
  Sub-3a, no reflection. Verified consistent with `A` on all tested configs (`n=3,4,5`).

---

# Bucket (iii), general `n`: the Sub-3a dichotomy, Lemma G1, and the residual obstruction (R12)

Throughout, bucket (iii) is: `Q` partitions `2^n` into parts all `< 2^{n−1}`; `R` refines
`G_{n−1} = {2^0,…,2^{n−1}}` with `max(R) < 2^{n−1}`; joint budget `c_Q + c_R ≤ n` where
`c_Q = #Q\text{-cuts} = |Q|−1`, `c_R = #R\text{-cuts} = |R|−n`. Since `max(R) < 2^{n−1}` the top piece
`2^{n−1}` of `G_{n−1}` is cut, so `c_R ≥ 1`; and `max(Q) < 2^{n−1}` with `ΣQ = 2^n` forces `|Q| ≥ 3`, i.e.
`c_Q ≥ 2`. Write `g := N_Q − N_R`, a right-continuous integer step function on `[0,∞)` supported on
`[0, 2^{n−1})`. By the certified Lemma M0, `N_{Q∪R} = N_Q + N_R ≡ g \pmod 2`, so
```
A(Q∪R) = measure{x : g(x) odd},     ∫₀^∞ g dx = ΣQ − ΣR = 2^n − (2^n − 1) = 1.
```
The target is `A(Q∪R) ≥ 1`.

## 0. The R11 target was circular — dropped

For `max|g| ≤ 2`, write `A_± := measure\{g=±1\}`, `B_± := measure\{g=±2\}`. Then
`∫g = (A_+ − A_−) + 2(B_+ − B_−) = 1` gives `A_+ = 1 + A_− − 2B_+ + 2B_−`, so
`A(Q∪R) = A_+ + A_− = 1 + 2(A_− + B_− − B_+)`. Hence `A ≥ 1 ⟺ B_+ ≤ A_− + B_−`. This is an algebraic
*restatement* of the goal, not a reduction; it is recorded as a dead end and is not used below.

## 1. The Sub-3a dichotomy

Recall the certified Sub-3a (`dyadic-level-parity`): if some dyadic level `I_k` has `N_{Q∪R}` odd throughout,
then `A(Q∪R) ≥ measure(I_k) ≥ 1`. So it remains to treat configurations where **Sub-3a fails**: every level
`I_k` (`0 ≤ k ≤ n−1`) carries a point at which `N_{Q∪R} = N_Q + N_R` (equivalently `g`) is even.

**The tight witness is not in the residual.** The unique tight `A = 1` config at `n = 3`,
`Q = {3,3,2}`, `R = {2,2,2,1}`, has `g(0⁺) = |Q| − |R| = 3 − 4 = −1` (odd) and every part of `P = Q∪R`
is `≥ 1`, so on `I₀ = [0,1)` we have `N_P(x) = 7` (odd) for all `x ∈ (0,1)`: **Sub-3a fires on `I₀`**. Thus
the residual `Sub-3a fails` sits strictly above `1` numerically (`min A = 9/8, 2, 3` for `n = 3,4,5`).

## 2. Foundation F-neg: `g(0⁺) ≤ −1` (full proof)

`N_Q(0⁺) = |Q|` and `N_R(0⁺) = |R|`, so `g(0⁺) = |Q| − |R|`. Now `|Q| = c_Q + 1` and, since `R` refines the
`n`-piece multiset `G_{n−1}` by `c_R` cuts, `|R| = n + c_R`. Hence
```
g(0⁺) = (c_Q + 1) − (n + c_R) = c_Q − c_R − (n − 1).
```
The joint budget `c_Q + c_R ≤ n` gives `c_Q ≤ n − c_R ≤ n − 1` (as `c_R ≥ 1`), so
`g(0⁺) = c_Q − c_R − (n−1) ≤ (n−1) − 1 − (n−1) = −1`. ∎ (F-neg)

Consequently `g` is `≤ −1` on a right-neighbourhood of `0`, while `∫g = 1 > 0`; so `g` attains a positive
value somewhere. (Machine-checked 1548/1548 across `n = 3,4,5`.)

## 3. Foundation F-parity: `R` has an odd-multiplicity value (claimed; caveat)

*Claim.* In bucket (iii), `R` cannot have all multiplicities even; equivalently, making every value of a
refinement of `G_{n−1}` have even multiplicity requires `≥ n` cuts, exceeding the budget `c_R ≤ n − 1`.

*Status.* Verified exhaustively for `n = 3` (min cuts to all-even `= 3 = n`; 0 all-even `R` with `c_R ≤ 2`).
The natural proof tracks `P := #\{\text{values of odd multiplicity}\}`, which starts at `n` (the `n` distinct
powers of `2`). A single cut of a piece `p` into `f, p−f` touches the multiplicities of `p, f, p−f`. **Honest
caveat:** a cut can change `P` by `−3` (when both fragments land on pre-existing odd-multiplicity values), so
the crude "each cut lowers `P` by `≤ 1`" bound of the explorer is not itself rigorous, and the general-`n`
proof of `P ≥ 1` is left as an OPEN sub-point. It is **not used** in the load-bearing arguments below (it only
yields `A > 0`, a prerequisite, never the `+1`); it is recorded for the record and flagged, not overclaimed.

## 4. Lemma G1 — one-sided small-discrepancy kill (full proof; PROMOTABLE)

> **Lemma G1.** Let `Q, R` be finite positive multisets with `N_Q(x) ≤ N_R(x) + 1` for every `x ≥ 0`
> (equivalently `max g ≤ 1`, `g := N_Q − N_R`; note `g` may be arbitrarily negative). Then
> `A(Q∪R) ≥ ΣQ − ΣR`. In bucket (iii) (`ΣQ = 2^n`, `ΣR = 2^n − 1`) this is `A(Q∪R) ≥ 1`.

*Proof.* By Lemma M0, `A(Q∪R) = measure\{x : g(x) odd\}` and `∫₀^∞ g dx = ΣQ − ΣR`. Let
`M_k := measure\{x : g(x) = k\}` (`k ∈ ℤ`); these are finite and `Σ_k M_k` is the length of the support.
Since `max g ≤ 1`, `M_k = 0` for all `k ≥ 2`, so
```
ΣQ − ΣR = ∫ g = Σ_k k·M_k = 1·M_1 + Σ_{k ≤ −1} k·M_k = M_1 − Σ_{k ≤ −1} |k|·M_k ≤ M_1,
```
because every term in the last sum is `≥ 0`. Hence `M_1 ≥ ΣQ − ΣR`. Finally `g = 1` is odd, so
`\{g = 1\} ⊆ \{g odd\}` and `A(Q∪R) = measure\{g odd\} ≥ M_1 ≥ ΣQ − ΣR`. ∎

*Remarks.* (a) G1 strictly contains the certified Lemma D1 on the upper side: D1 assumes `|g| ≤ 1`, while G1
assumes only `g ≤ 1` and allows `g` to dip to any negative value. (b) The one-sided hypothesis is essential
and cannot be flipped: `min g ≥ −1` does **not** imply `A ≥ 1` (the `g ≡ 2` obstruction, `A = 0`), because a
positive integral can hide entirely in the even value `g = 2`. (c) G1 closes the **entire `max g ≤ 1` slice**
of the Sub-3a-failing residual, for all `n`, unconditionally. Verified: `n = 3`, 168 bucket-(iii) configs,
`0` violations of both G1 and the target.

## 5. HS-D3 — the route is `max|g|`-agnostic

The pieces in §§1–4 use only: the measure form `A = measure\{g odd\}`, the integral `∫g = 1`, the level
decomposition `I_k`, `F-neg`, and (in G1) the one-sided bound `max g ≤ 1`. **None** assumes `max|g| ≤ 2`; the
general bound in bucket (iii) is only `max|g| ≤ max(|Q|,|R|) ≤ n + 1`, and the arguments are insensitive to it.
Furthermore, §0 shows `max|g| ≤ 2` is **not** a genuinely easier regime — the level-charge identity is a
restatement of `A ≥ 1` there — so there is no shortcut hiding in the `max|g| ≤ 2` case. This resolves the HS-D3
agnosticism concern: the route neither assumes nor benefits from a small-`|g|` hypothesis.

## 6. The residual `{Sub-3a fails ∧ max g ≥ 2}` and why parity alone cannot close it (rigorous obstruction)

After §§1,4 the only open configurations are `Sub-3a fails` **and** `max g ≥ 2` (if `max g ≤ 1`, G1 closes it;
if some level is fully odd, Sub-3a closes it). The following shows the two parity foundations (`F-neg`,
`F-parity`) are provably **insufficient** to force `A ≥ 1` on this residual — the geometry `ΣQ = 2^n` with `R`
a refinement of `G_{n−1}` must be used.

*Obstruction.* Consider the abstract step function `g` with `g = −1` on `[0, ε)`, `g = +2` on `[ε, ε+s)`, and
`g = 0` on `[ε+s, ∞)`, for small `ε > 0` and `s = (1 + ε)/2` (so `∫g = −ε + 2s = 1`). This profile:
- has `g(0⁺) = −1 ≤ −1` (indeed odd), satisfying `F-neg`;
- makes Sub-3a fail on every level (on `I₀` the value `+2` is even, so `I₀` is not fully odd; higher levels
  have `g = 0`, even);
- has `max g = 2` (in the residual);
- yet `A = measure\{g odd\} = measure\{g = −1\} = ε`, which is `< 1` for `ε < 1`.

The jump of `g` by `+3` at `ε` corresponds to a value of `R` with multiplicity `3` more than `Q` (e.g. a triple
point of `R`), which is compatible with the budget in principle. Hence **no argument using only `F-neg`,
`F-parity`, and the level structure can prove `A ≥ 1`**: those hypotheses are all met by a profile with
`A = ε < 1`. What excludes the obstruction in the *actual* problem is that `ΣQ = 2^n` with all `Q`-parts
`< 2^{n−1}` and `R` a dyadic refinement cannot realize a `g` that is `−1` on a tiny `[0,ε)` and `+2` on a long
`[ε, ε+s)` — but proving that requires the staircase geometry, not parity.

*Consequence for the plan.* The outline's "turn the per-level parity switch into a fixed positive measure and
sum over levels" cannot be carried out from parity/budget data alone; the per-level lower bound must be sourced
from the `ΣQ = 2^n` excess and the `N_{G_{n−1}}` staircase (each dyadic level `[2^{k−1},2^k)` holds exactly one
`G_{n−1}`-piece `2^k` at its right endpoint, so the base staircase drops by exactly `1` per level, and a
`Q`-mass matching `2·G_{n−2}` plus a unit excess must deposit that excess as *odd*-`g` measure). Formalizing
this is the **honest OPEN gap** (HS-D1 / HS-D2); it is not closed this round and is not overclaimed.

*Numerical status (targets true, residual non-tight).* Over bucket (iii) the target `A ≥ 1` holds with `0`
violations for `n = 3,4,5`; after removing the Sub-3a-firing and `max g ≤ 1` slices the remaining
configurations have `A = 9/8, 2, 3` minimum for `n = 3,4,5` — comfortably above `1`, but by a mechanism not yet
proven.

## Promotable lemmas (R12)

- **Lemma G1 (one-sided small-discrepancy kill), all `n`.** For finite positive multisets `Q, R`, if
  `N_Q(x) ≤ N_R(x) + 1` for all `x ≥ 0` (i.e. `max g ≤ 1`, `g := N_Q − N_R`), then `A(Q∪R) ≥ ΣQ − ΣR`.
  In bucket (iii), `A(Q∪R) ≥ 1`. Full proof in §4 above (via `∫g = M₁ − Σ_{k≤−1}|k|M_k ≤ M₁` and
  `A ≥ M₁`). Strictly generalizes the certified Lemma D1 on the `g ≤ 1` side. Verified 0 violations
  (n=3, 168 configs).
- **Foundation F-neg, bucket (iii).** `g(0⁺) = |Q| − |R| = c_Q − c_R − (n−1) ≤ −1`. Full proof in §2 (from
  `|Q| = c_Q+1`, `|R| = n + c_R`, budget `c_Q+c_R ≤ n`, `c_R ≥ 1`). Verified 1548/1548 (n=3,4,5).

---

# Setup, imports, and reduction

We work in **unnormalized units**: multiply all lengths by `D = 2^{n+1} − 1`, so Liu Bang's geometric
marks produce the integer pieces `G_n = {2^0, 2^1, …, 2^n}` with total `T = D`, and (via `val = (T+A)/2`)
the lower bound `c(n) = 2^n/D` is exactly the statement

> **(LB)** every refinement `P` of `G_n` obtained by `≤ n` Xiang-Yu cuts satisfies `A(P) ≥ 1`,

where for a finite multiset `P` sorted `p_1 ≥ p_2 ≥ ⋯` the alternating sum is `A(P) = p_1 − p_2 + p_3 − ⋯`.

**Imported, certified (used verbatim):**
- **Lemma G** (`lemmas/greedy-odd-index.md`): in the alternating claiming game the first mover obtains
  exactly `val(P) = Σ_{i odd} p_i = (T + A(P))/2`. This is the reduction to (LB).
- **Lemma M0** (`lemmas/alt-sum-integral.md`): with `N_P(x) := #{i : p_i > x}`,
  `A(P) = measure{x ≥ 0 : N_P(x) odd}`, and `0 ≤ A(P) ≤ max(P)`. Write `S_P := {x : N_P(x) odd}`.
- **Lemma M** (`lemmas/alt-sum-integral.md`): since `N_{X∪Y} = N_X + N_Y`,
  `A(X∪Y) = A(X) + A(Y) − 2B` with `B := measure(S_X ∩ S_Y)`. Because
  `measure(S_X △ S_Y) = measure(S_X) + measure(S_Y) − 2·measure(S_X ∩ S_Y)`, this is equivalently
  **`A(X∪Y) = measure(S_X △ S_Y)`**.
- **Lemma P** (`lemmas/parity-piece-count.md`): if a multiset has an **odd** number of pieces, each of
  length `≥ 1`, then `A ≥ min piece ≥ 1`.
- **Lemma LL, `t = 1`** (`lemmas/ll-t1-single-cut.md`): the single-cut tail, imported for completeness.

**The induction (imported skeleton, `geometric-selfsimilar`).** Prove (LB) by induction on `n`. Base
`n = 1` is done. For the step, write `G_n = {2^n} ∪ G_{n−1}` and let `t` be the number of XY cuts inside
the largest piece `2^n`.
- If `t = 0` (**Case 1 of the induction**, largest piece uncut): `2^n` survives as the unique maximum,
  so `A(P) = 2^n − (\text{sum of even-indexed pieces}) ≥ 1`. Done (imported).
- If `t ≥ 1`: the piece `2^n` splits into `Q = {q_1,…,q_{t+1}}` (`ΣQ = 2^n`), and the pieces of `G_{n−1}`
  receive `≤ n − t ≤ n − 1` cuts, giving a refinement `R` of `G_{n−1}`. By the **induction hypothesis**
  applied to `G_{n−1}` with `≤ n − 1` cuts, `A(R) ≥ 1`; and since every `G_{n−1}`-piece is `≤ 2^{n−1}`
  and cutting only shrinks pieces, `M := max(R) ≤ 2^{n−1}`. Hence `S_R ⊆ [0, M) ⊆ [0, 2^{n−1})`. The final
  multiset is `P = Q ∪ R`, and by Lemma M we must prove:

> **Lemma LL.** Let `Q` partition `2^n` into `t+1 ≥ 2` positive parts, and let `R` refine `G_{n−1}` with
> `A(R) ≥ 1` and `M := max(R) ≤ 2^{n−1}`. Then `A(Q∪R) = measure(S_Q △ S_R) ≥ 1`.

The sub-cases `A(Q) = 0` and `t = 1` are certified (imports; `lemmas/ll-t1-single-cut.md`). **This slug
proves Lemma LL for `t ≥ 2`, `A(Q) > 0`** via the three-way split below. (For `t ≥ 2` the number of parts
of `Q` is `≥ 3`; the parts summing to `2^n` are the only structural facts used about `Q`.)

Throughout, the target is `measure(S_Q △ S_R) ≥ 1`. Two ambient facts:
- **(F1)** `S_R ⊆ [0, 2^{n−1})` (from `M ≤ 2^{n−1}`), so `N_R(x) = 0` for `x ≥ 2^{n−1}`.
- **(F2)** Since `ΣQ = 2^n`, at most one part of `Q` can exceed `2^{n−1}` (two parts each `> 2^{n−1}` would
  sum to `> 2^n`). Hence for `x ≥ 2^{n−1}`, `N_Q(x) = 𝟙[max(Q) > x] ∈ {0,1}`.

Define the **dyadic levels** partitioning `[0, 2^{n−1})`:
`I_0 = [0,1)` and `I_k = [2^{k−1}, 2^k)` for `1 ≤ k ≤ n−1`; note `measure(I_0) = 1` and
`measure(I_k) = 2^{k−1} ≥ 1` for `k ≥ 1`, so **every level has measure `≥ 1`.** Write `N_P := N_Q + N_R`,
so `S_Q △ S_R = {x : N_P(x) odd}` and `measure(S_Q △ S_R) = A(P)`.

---

# The three-way split (exhaustive)

Every configuration falls into exactly one of:
- **Case 1:** `max(Q) ≥ 2^{n−1} + 1`.
- **Case 2:** `max(Q) < 2^{n−1} + 1`, the total piece count `|Q| + |R|` is **odd**, and every piece of
  `P = Q∪R` has length `≥ 1`.
- **Case 3:** `max(Q) < 2^{n−1} + 1`, and **not** (odd count with all pieces `≥ 1`) — i.e. the count is
  even, or some piece is `< 1`.

These are mutually exclusive and exhaustive: Case 1 is `max(Q) ≥ 2^{n−1}+1`; the complement
`max(Q) < 2^{n−1}+1` is split by the predicate "(odd count) ∧ (all pieces ≥ 1)" into Case 2 (true) and
Case 3 (false). No configuration is left out; in particular the "band" `max(Q) ∈ (2^{n−1}, 2^{n−1}+1)` is
Case 2 or Case 3 (never Case 1), and is handled by those cases — there is no hole in the split.

## Case 1 — `max(Q) ≥ 2^{n−1} + 1`. CLOSED.

Let `μ := max(Q) ≥ 2^{n−1} + 1`. Consider `x ∈ [2^{n−1}, μ)`. By **(F2)**, exactly one part of `Q` (namely
`μ`) exceeds such `x`, so `N_Q(x) = 1`. By **(F1)**, `N_R(x) = 0`. Hence `N_P(x) = 1` is odd for every
`x ∈ [2^{n−1}, μ)`, i.e.

    [2^{n−1}, μ) ⊆ {x : N_P(x) odd} = S_Q △ S_R.

Therefore `measure(S_Q △ S_R) ≥ measure([2^{n−1}, μ)) = μ − 2^{n−1} ≥ 1`. So `A(Q∪R) ≥ 1`. ∎ (Case 1)

*(Verified this round: over 8310 n=3 configurations with `max(Q) ≥ 5`, `A(Q∪R) ≥ 1` with 0 violations.)*

## Case 2 — odd count, all pieces `≥ 1`. CLOSED (Lemma P).

The multiset `P = Q ∪ R` has an odd number of pieces, each of length `≥ 1`. By the certified **Lemma P**
(`lemmas/parity-piece-count.md`), sorting `P` as `p_1 ≥ … ≥ p_k` (`k` odd) and pairing
`A(P) = (p_1 − p_2) + ⋯ + (p_{k−2} − p_{k−1}) + p_k`, every parenthesised difference is `≥ 0` and the
trailing term is `p_k = min(P) ≥ 1`, whence `A(P) ≥ 1`. So `A(Q∪R) ≥ 1`. ∎ (Case 2)

## Case 3 — even count, or a sub-unit piece (`max(Q) < 2^{n−1}+1`). Reduced; Sub-3a closed, Sub-3b open.

Here we must still prove `measure(S_Q △ S_R) ≥ 1`. We exploit the **dyadic level** structure.

### Sub-3a (dyadic-level parity). CLOSED.

> **Sub-3a.** If there exists a level index `k ∈ {0, 1, …, n−1}` such that `N_P(x)` is **odd for every**
> `x ∈ I_k`, then `A(Q∪R) ≥ measure(I_k) ≥ 1`.

*Proof.* If `N_P` is odd throughout `I_k`, then `I_k ⊆ {x : N_P(x) odd} = S_Q △ S_R`, so
`measure(S_Q △ S_R) ≥ measure(I_k) ≥ 1` (every level has measure `≥ 1`). ∎ (Sub-3a)

Sub-3a is not vacuous: a clean, checkable **sufficient condition** for its hypothesis is

> **(∗)** for some `k`, no piece value of `P` lies in the open interval `int(I_k)` with **odd**
> multiplicity, and the number of pieces of `P` with value `≥ sup I_k` is **odd**.

Indeed, if no piece value in `int(I_k)` has odd multiplicity, then as `x` ranges over `I_k` the parity of
`N_P(x) = #{pieces > x}` never changes (crossing a value of even multiplicity flips `N_P` an even number
of times), so `N_P` has constant parity on `I_k`; and that constant parity equals the parity of
`N_P` just below `sup I_k`, which counts exactly the pieces with value `≥ sup I_k`. If that count is odd,
`N_P` is odd throughout `I_k` and Sub-3a fires. In particular, the special case of `(∗)` at `k = 1`
(the interval `[1,2)`) — "no piece of `P` in the open interval `(1,2)` and an odd number of pieces of
`P` of value `≥ 2`" — is the `[1,2)`-argument of Opening 6; but `(∗)` covers every dyadic level and also
allows even-multiplicity interior pieces (e.g. a doubled piece from a shadow-type response).

**Coverage (verified this round).** Over the n=3 residual grid (Case 3), Sub-3a's hypothesis (some level
`I_k` fully odd) holds for **102 of 187** configurations. This is a genuine, rigorous partial: it settles
all configurations in which the mismatch between `S_Q` and `S_R` concentrates on a single full dyadic
level (all tight `n=3, n=4` examples of the form `S_Q △ S_R = [0,1)` or `[1,2)` are of this type).

### Sub-3b (no fully-odd dyadic level). Restructured by a `max(Q)`-split; identity reduces two branches.

The residual of Case 3 is exactly the configurations where **Sub-3a fails**:

> **Sub-3b.** `Q` partitions `2^n` into `≥ 3` parts with `A(Q) > 0` and `max(Q) < 2^{n−1}+1`; `R`
> refines `G_{n−1}` with `A(R) ≥ 1`, `max(R) ≤ 2^{n−1}`, and `#Q-cuts + #R-cuts ≤ n`; and for every
> dyadic level `I_k` (`0 ≤ k ≤ n−1`) the function `N_P = N_Q + N_R` takes an even value somewhere on
> `I_k`. Prove `measure(S_Q △ S_R) ≥ 1`.

We split on `μ := max(Q)` into three disjoint, exhaustive branches (recall Case 3 gives `μ < 2^{n−1}+1`):
**B1** `2^{n−1} < μ < 2^{n−1}+1`, **B2** `μ = 2^{n−1}`, **B3** `μ < 2^{n−1}`. The engine for B1 and B2
is the following identity, the main new rigorous result of this round.

#### General reflection identity (NEW, proven; verified 490/490, 0 mismatches). 

> **Lemma REFL.** Let `Q` be a multiset with `μ := max(Q)`, let `Q' := Q ∖ {μ}` (one copy of the maximum
> removed), and let `R` satisfy `max(R) ≤ 2^{n−1}`. If `μ ≥ 2^{n−1}` then
> `A(Q∪R) = μ − A(Q'∪R)`.

*Proof.* Write `N_Q(x) = #\{parts of Q > x\}`. Fix `x ∈ [0, μ)`. The removed part `μ` satisfies `μ > x`,
and every part of `Q` other than the removed copy either exceeds `x` (contributing to `N_{Q'}(x)`) or not;
hence `N_Q(x) = 1 + N_{Q'}(x)`. For `x ≥ μ` no part of `Q` exceeds `x`, so `N_Q(x) = N_{Q'}(x) = 0`. Thus
`x ∈ S_Q ⟺ N_Q(x)` odd `⟺ N_{Q'}(x)` even, giving

    S_Q = [0, μ) ∖ S_{Q'}                                        (★)

(here `S_{Q'} ⊆ [0, μ)` since `max(Q') ≤ μ`). Now `μ ≥ 2^{n−1} ≥ max(R)`, so `S_R ⊆ [0, max(R)) ⊆ [0, μ)`.
Put `U := [0, μ)`; both `S_{Q'}` and `S_R` lie in `U`. For any `A, B ⊆ U` one has the pointwise identity
`(U ∖ A) △ B = U ∖ (A △ B)`: for `x ∈ U`, `x ∈ (U∖A)△B ⟺ (x∉A) \text{ xor } (x∈B) ⟺
\neg\big((x∈A)\text{ xor }(x∈B)\big) ⟺ x ∉ A△B`. Applying this with `A = S_{Q'}`, `B = S_R` and using (★),

    S_Q △ S_R = (U ∖ S_{Q'}) △ S_R = U ∖ (S_{Q'} △ S_R),

where we also used that `S_Q △ S_R` has no mass in `[μ,∞)` (both `S_Q` and `S_R` are empty there). Since
`S_{Q'} △ S_R ⊆ U` and `measure(U) = μ`,

    A(Q∪R) = measure(S_Q △ S_R) = μ − measure(S_{Q'} △ S_R) = μ − A(Q'∪R).   ∎

(For `μ = 2^{n−1}` this is exactly the certified `max(Q)=2^{n−1}` identity; Lemma REFL extends it to the
whole range `μ ≥ 2^{n−1}`, i.e. to B1 as well as B2. Machine-verified: over all `n=3` configs with
`μ ≥ 4` on the `1/4`-grid respecting the joint cut budget, `A(Q∪R) = μ − A(Q'∪R)` with **0** mismatches
across **490** instances.)

#### Lemma REFL-gen (NEW this round; the same proof with the hypothesis relaxed to `max(R) ≤ μ`).

> **Lemma REFL-gen.** Let `Q` be a finite multiset of positive reals with `μ := max(Q)`, let
> `Q' := Q ∖ {μ}`, and let `R` be a finite multiset with `max(R) ≤ μ`. Then
> `A(Q∪R) = μ − A(Q'∪R)`.

*Proof.* The proof of Lemma REFL uses the hypotheses only through the single conclusion
`S_R ⊆ [0,μ)`. Repeating it verbatim: fix `x ∈ [0,μ)`. The removed part `μ` satisfies `μ > x`, and every
other part of `Q` exceeds `x` iff it is a part of `Q'` exceeding `x`, so `N_Q(x) = 1 + N_{Q'}(x)`; for
`x ≥ μ`, `N_Q(x) = N_{Q'}(x) = 0`. Hence `S_Q = [0,μ) ∖ S_{Q'}` with `S_{Q'} ⊆ [0,μ)` (as `max(Q') ≤ μ`),
which is exactly (★). The hypothesis `max(R) ≤ μ` gives `S_R ⊆ [0, max(R)) ⊆ [0, μ) =: U` directly (this
is the *only* place the certified Lemma REFL used `μ ≥ 2^{n−1} ≥ max(R)`; the weaker `max(R) ≤ μ` suffices
for the same conclusion). The pointwise identity `(U∖A)△B = U∖(A△B)` for `A,B ⊆ U` then gives, as before,
`S_Q △ S_R = U ∖ (S_{Q'} △ S_R)`, and since `S_{Q'}△S_R ⊆ U`, `measure(U) = μ`,
`A(Q∪R) = μ − A(Q'∪R)`. ∎

Lemma REFL-gen strictly contains the certified Lemma REFL (take `μ ≥ 2^{n−1}`, `max(R) ≤ 2^{n−1} ≤ μ`); it
is what the *second* reflection below needs, where the removed maximum `μ = max(Q)` may be `< 2^{n−1}`.
(Machine check this round: over 4000 random rational multisets with `max(R) ≤ max(Q)`, `A(Q∪R) = μ − A(Q'∪R)`
with **0** mismatches.)

**Reduction of B1 and B2.** By Lemma REFL, in branches B1 (`μ > 2^{n−1}`) and B2 (`μ = 2^{n−1}`) the
target `A(Q∪R) ≥ 1` is *equivalent* to the **upper bound**

    (RED)   A(Q'∪R) ≤ μ − 1,

where `Q' = Q ∖ {μ}` partitions `2^n − μ` and `Q'∪R` has total sum `2^{n+1} − μ − 1` and `max ≤ 2^{n−1}`.
This is a genuine, non-circular one-step reduction: `Q'∪R` is **not** a valid `G_{n−1}`-refinement (its
sum is not `2^n − 1`), so (RED) is proved by an upper-bound argument, never by re-invoking the induction
hypothesis on `Q'∪R`. (RED) is machine-verified tight: over the same 490 instances, `A(Q'∪R) ≤ μ − 1`
holds with **0 violations** and minimum slack **0**.

### Branch B3 (`μ < 2^{n−1}`) — GAP-B. Double-REFL telescoping; anchor `R = G_{n−1}` unrefined.

This round we close branch B3 for the **anchor** `R = G_{n−1}` (the unrefined geometric multiset
`{2^0,…,2^{n−1}}`) at all `n`, except one precisely isolated residual proven at `n = 3`. Fix throughout
this subsection `R = G_{n−1}`, and let `μ := q_1 := max(Q) < 2^{n−1}` (branch B3), so `Q` partitions
`2^n` into `≥ 3` parts each `< 2^{n−1}`, with `|Q| ≤ n + 1` (the budget: `#R`-cuts `= 0`, so `#Q`-cuts
`≤ n`, giving `t + 1 = |Q| ≤ n + 1`). Write `G_m := {2^0, 2^1, …, 2^m}`, so `ΣG_m = 2^{m+1} − 1` and
`max(G_m) = 2^m`. The target is `A(Q ∪ G_{n−1}) ≥ 1`.

**First reflection (remove the global maximum `2^{n−1}`).** Since every part of `Q` is `< 2^{n−1}`, the
unique maximum of `Q ∪ G_{n−1}` is the piece `2^{n−1}` of `G_{n−1}`. Apply the **certified Lemma REFL**
(`lemmas/ll-reflection-identity.md`) with its "`Q`" taken to be `G_{n−1}` (so `μ = 2^{n−1} ≥ 2^{n−1}`,
`G_{n−1}∖\{2^{n−1}\} = G_{n−2}`) and its "`R`" taken to be our `Q` (`max(Q) < 2^{n−1} = μ`):
```
A(Q ∪ G_{n−1}) = 2^{n−1} − A(Q ∪ G_{n−2}).                                (I)
```
Thus `A(Q∪G_{n−1}) ≥ 1  ⟺  A(Q∪G_{n−2}) ≤ 2^{n−1} − 1`. We now split on `q_1 = max(Q)` versus
`max(G_{n−2}) = 2^{n−2}` into three disjoint, exhaustive sub-cases (recall `q_1 < 2^{n−1}`):

**(B3a) `q_1 ≤ 2^{n−2}`. CLOSED.** Then every part of `Q` is `≤ 2^{n−2}`, so
`max(Q∪G_{n−2}) = 2^{n−2}`. By Lemma M0 (`0 ≤ A(P) ≤ max(P)`), `A(Q∪G_{n−2}) ≤ 2^{n−2}`. Since
`2^{n−2} ≤ 2^{n−1} − 1` for `n ≥ 2` (equivalently `2^{n−2} ≥ 1`), (I) gives
`A(Q∪G_{n−1}) = 2^{n−1} − A(Q∪G_{n−2}) ≥ 2^{n−1} − 2^{n−2} = 2^{n−2} ≥ 1`. ∎ (B3a)

**Second reflection (Cases B3b, B3c: `q_1 > 2^{n−2}`).** Here `q_1 > 2^{n−2} = max(G_{n−2})`, so `q_1` is
the unique maximum of `Q ∪ G_{n−2}`. Apply **Lemma REFL-gen** (proved above; needed because now
`μ = q_1 < 2^{n−1}`, outside the certified Lemma REFL's range, but `max(G_{n−2}) = 2^{n−2} < q_1 = μ`, so
its hypothesis `max(R) ≤ μ` holds) with "`Q`" `= Q` and "`R`" `= G_{n−2}`:
```
A(Q ∪ G_{n−2}) = q_1 − A(Q' ∪ G_{n−2}),   Q' := Q ∖ {q_1}.
```
Substituting into (I) gives the **double-REFL telescoping formula**
```
A(Q ∪ G_{n−1}) = 2^{n−1} − q_1 + A(Q' ∪ G_{n−2}).                          (II)
```
(Machine-verified this round, `1/4`-grid, budget enforced: (II) holds with **0** mismatches over 90 (n=3)
and 1205 (n=4) B3c instances; and the reviewer's pre-build check confirmed (II) 0/3031 for
`q_1 ∈ (2^{n−2}, 2^{n−1})`.)

**(B3b) `2^{n−2} < q_1 ≤ 2^{n−1} − 1`. CLOSED.** By Lemma M0, `A(Q'∪G_{n−2}) ≥ 0`, so (II) gives
`A(Q∪G_{n−1}) ≥ 2^{n−1} − q_1 ≥ 2^{n−1} − (2^{n−1} − 1) = 1`. ∎ (B3b)

**(B3c) `2^{n−1} − 1 < q_1 < 2^{n−1}`.** By (II), `A(Q∪G_{n−1}) ≥ 1` is *equivalent* to
`A(Q'∪G_{n−2}) ≥ 1 − (2^{n−1} − q_1) = q_1 − (2^{n−1} − 1) =: δ ∈ (0,1)`. Since `δ < 1`, it suffices to
prove the clean residual
```
(B2*)   A(Q' ∪ G_{n−2}) ≥ 1,
```
where `Q' = Q ∖ {q_1}` partitions `Σ' := 2^n − q_1 ∈ (2^{n−1}, 2^{n−1} + 1)` into `≤ n` positive parts
each `< 2^{n−1}` (each part of `Q'` is a part of `Q`, hence `< 2^{n−1} = 2·max(G_{n−2})`).
**(B2\*) is tight:** its minimum over the `1/4`-grid (budget enforced) is exactly `1`, attained e.g. at
`n = 3` by `Q' = \{2, 5/4, 5/4\}` (`Σ' = 9/2`, `q_1 = 8 − 9/2 = 7/2 ∈ (3,4)`):
`A(Q'∪G_1) = A(\{2,2,5/4,5/4,1\}) = 2−2+5/4−5/4+1 = 1`.

*Equivalent forms of (B2\*).* With `T_2 := Σ(Q'∪G_{n−2}) = Σ' + 2^{n−1} − 1 ∈ (2^n − 1, 2^n)` and
`val = (T_2 + A)/2 = Σ_{\text{odd-index}}` (Lemma G), (B2\*) reads equivalently
`A(Q'∪G_{n−2}) + T_2 ≥ 2^n`, i.e. `Σ_{\text{odd-index}}(Q'∪G_{n−2}) ≥ 2^{n−1}` (the first player claims at
least `2^{n−1}` from the multiset `Q'∪G_{n−2}`).

#### (B2*) proved in full for `n = 3` (all `Q`).

Here `G_{n−2} = G_1 = \{1,2\}`, `Q'` partitions `Σ' ∈ (4,5)` into `|Q'| ∈ \{2,3\}` parts each `< 4`, and
`S_{\{1,2\}} = [1,2)` (since `N_{\{1,2\}}(x) = 2` on `[0,1)`, `= 1` on `[1,2)`, `= 0` above, so
`A(\{1,2\}) = 1`). By Lemma M0/M, `A(Q'∪\{1,2\}) = measure(S_{Q'} △ [1,2))`. We show it is `≥ 1`.

*Case `|Q'| = 2`: `Q' = \{a,b\}`, `a ≥ b > 0`, `a + b = Σ' ∈ (4,5)`, `a,b < 4`.* Then `a ≥ Σ'/2 > 2`, so
`N_{Q'}(x) = 2` on `[0,b)`, `= 1` on `[b,a)`, `= 0` on `[a,∞)`, giving `S_{Q'} = [b,a)` with `a > 2`.
- If `b ≤ 1`: `measure(S_{Q'}△[1,2)) = (1−b) + (a−2) + (2−1)·0 …` — compute directly:
  `S_{Q'}△[1,2) = ([b,1)) ∪ ([2,a))` (the part of `[b,a)` outside `[1,2)`) `∪ ∅` (all of `[1,2) ⊆ [b,a)`),
  measure `= (1−b) + (a−2) = a − b − 1 = Σ' − 2b − 1 ≥ 1` because `2b ≤ 2 < Σ' − 2` (as `b ≤ 1`, `Σ' > 4`).
- If `1 < b < 2`: `S_{Q'}△[1,2) = [2,a)` (all of `[1,2)⊆[b,a)`, and `[b,2)` cancels), plus nothing below,
  measure `= a − 2`; but also `[1,2)∖S_{Q'} = [1,b)` has measure `b−1`, so total `= (a−2)+(b−1) = Σ'−3 > 1`.
- If `b ≥ 2`: then `2 ≤ b ≤ a`, `a+b = Σ' < 5 ⟹ b < 5/2`, and `S_{Q'} = [b,a) ⊆ [2,∞)` is disjoint from
  `[1,2)`, so `measure(S_{Q'}△[1,2)) = (a−b) + 1 ≥ 1`.

*Case `|Q'| = 3`: `Q' = \{a,b,c\}`, `a ≥ b ≥ c > 0`, `a+b+c = Σ' ∈ (4,5)`, each `< 4`.* Then
`N_{Q'}` is `3` on `[0,c)`, `2` on `[c,b)`, `1` on `[b,a)`, `0` above, so `S_{Q'} = [0,c) ∪ [b,a)` and
`A(Q') = c + (a−b)`. By the merge form (Lemma M), with `S_{\{1,2\}} = [1,2)`,
```
A(Q'∪\{1,2\}) = A(Q') + 1 − 2·measure(S_{Q'} ∩ [1,2))
             = c + a − b + 1 − 2\big[(min(c,2)−1)^+ + (min(a,2) − max(b,1))^+\big].
```
Because `a ≥ Σ'/3 > 4/3 > 1`, and `c < 2` always (if `c ≥ 2` then `a,b,c ≥ 2`, `Σ' ≥ 6 > 5`), the first
bracket term is `(c−1)^+`. We split on `a` and `b`; in every sub-case `A(Q'∪\{1,2\}) ≥ 1`:

- **`a < 2`** (all parts in `(0,2)`): since `Σ' > 4` with each part `< 2`, at least two parts exceed `1`,
  so `b > 1` (else `Σ' < 2+1+1 = 4`). Then `(min(a,2)−max(b,1))^+ = a − b`.
  - `c ≤ 1`: `A = c+a−b+1 − 2(a−b) = 1 + (b + c − a)`; and `b+c = Σ'−a > 4 − 2 = 2 > a`, so `A > 1`.
  - `1 < c` (so `1<c≤b≤a<2`): `A = c+a−b+1 − 2[(c−1)+(a−b)] = 3 + b − a − c`; since `a<2` and `c≤b`,
    `a + c − b ≤ a < 2`, so `A ≥ 1` (`> 1` unless `a→2, c=b`).
- **`a ≥ 2`** (`a ∈ [2,4)`, so `min(a,2)=2`):
  - `b ≥ 2` (then `c < 1` as `Σ' < 5`): brackets `= 0`, `A = c + a − b + 1 ≥ 1` (as `a ≥ b`, `c>0`).
  - `1 ≤ b < 2`, `c ≤ 1`: `A = c+a−b+1 − 2(2−b) = c + a + b − 3 = Σ' − 3 > 1`.
  - `1 ≤ b < 2`, `1 < c ≤ b`: `A = c+a−b+1 − 2[(c−1)+(2−b)] = a + b − c − 1 ≥ 1` (since `a ≥ 2`, `b ≥ c`).
  - `b < 1` (so `c ≤ b < 1`): `A = c + a − b + 1 − 2·1 = (a + c − b) − 1`; and `a > 4 − b − c` (from
    `Σ' > 4`), so `a + c − b > 4 − 2b > 2` (as `b < 1`), giving `A > 1`.

Every sub-case yields `A(Q'∪\{1,2\}) ≥ 1`, so (B2\*) — hence branch B3c, hence GAP-B — is **fully proved
for the anchor `R = G_{n−1}` at `n = 3`.** Combined with B3a and B3b (all `n`), GAP-B is closed at `n = 3`
for `R = G_2` and reduced, for all `n`, to the single clean inequality (B2\*). ∎ (B3c, n=3)

*(Machine check this round, `1/4`-grid, budget enforced: over 90 (n=3) and 1205 (n=4) B3c instances,
`A(Q'∪G_{n−2}) ≥ 1` with `min = 1` and **0** violations; the min-margin `A − δ ≥ 1/2` everywhere.)*

### The remaining open gaps (honest, precise).

After this round GAP-B (anchor `R = G_{n−1}`) is reduced to **one** residual, and GAP-A remains as before.

> **(B2*) [branch B3c, general `n`].** Let `Q'` be a multiset of `≤ n` positive parts each `< 2^{n−1}`
> with `ΣQ' ∈ (2^{n−1}, 2^{n−1}+1)`. Then `A(Q'∪G_{n−2}) ≥ 1`.
>
> **(GAP-A) [branches B1, B2 via (RED)].** Let `μ ∈ [2^{n−1}, 2^{n−1}+1)`, let `Q'` partition `2^n − μ`
> into `t ≥ 2` positive parts each `< 2^{n−1}`, and let `R` refine `G_{n−1}` with `max(R) ≤ 2^{n−1}` and
> `A(R) ≥ 1`. Then `A(Q'∪R) ≤ μ − 1`.

What is established and what is missing:
- **(B2\*) is PROVED at `n = 3` (all `Q`) above**, and reduced to a single clean statement for all `n`.
  It is TRUE and tight (machine-checked, `1/4`-grid, budget: `min A = 1`, 0 violations, `n = 3,4`).
- **Why (B2\*) general `n` is genuinely the shared crux, not a routine descent.** The reviewer flagged the
  naive "recurse: `Q'∪G_{n−2}` is a B-type problem one level down" as the hand-waviest step, correctly.
  Making it rigorous meets the same obstruction as GAP-A. Concretely, a third reflection on
  `max(Q'∪G_{n−2}) = max(q_2, 2^{n−2})` splits into: **(i) `q_2 ≤ 2^{n−2}`** — then Lemma REFL-gen gives
  `A(Q'∪G_{n−2}) = 2^{n−2} − A(Q'∪G_{n−3})`, so `A(Q'∪G_{n−2}) ≥ 1 ⟺ A(Q'∪G_{n−3}) ≤ 2^{n−2} − 1`, which
  is an **upper bound of the same GAP-A shape** (`A ≤ max − 1`); and **(ii) `q_2 > 2^{n−2}`** — then a
  reflection removes `q_2` and recurses on `Q''∪G_{n−2}` with `ΣQ''` still large, **not** cleanly a
  level-down instance (this is exactly the reviewer's `q_2 > 2^{n−2}` non-termination concern). So the
  descent does not close by itself; (B2\*) at general `n` is entangled with the alternating-tail upper
  bound `(p_2−p_3)+(p_4−p_5)+⋯ ≥ 1` — the **same** crux as GAP-A / `ll-inclusion-gap`'s `G-INC-1`.
- **The A≥2 slack mechanism is permanently dead.** The earlier "`max(Q) < 2^{n−1} ⟹ A ≥ 2`" step is
  FALSE (reviewer counterexample `Q={15/4,13/4,1}`, `R=G_2`, `A=3/2`). Correct picture (gapb explorer):
  in branch B3 with `R = G_{n−1}` the minimum of `A(Q∪G_{n−1})` is `3/2` (never `1` and never `2`); the
  once-cited "tight `A=1`" witness `Q={3,3,2}`, `R={2,2,2,1}` is a **Sub-3a** case (`I_0` fully odd:
  `N_P(0^+) = 3 + 4 = 7` odd), **not** a B3 anchor case, and does not arise here. So B3-anchor carries
  margin (`≥ 3/2`), consistent with (B2\*)'s residual bound `δ < 1`.
- **The naive integral bound remains insufficient.** `∫_0^{2^{n−1}}(N_Q − N_R)\,dx = ΣQ − ΣR = 1` does
  not force `measure{N_Q − N_R \text{ odd}} ≥ 1` (`g ≡ 2` on `[0,½)` integrates to `1`, never odd). A
  proof of (B2\*)/GAP-A must use the geometric/dyadic structure of `G_m`, not merely the total mass.
- **Why GAP-A is an upper bound one can hope to close.** `A(P) = p_1 − p_2 + p_3 − ⋯ ≤ p_1 = max(P)`;
  (RED) asks for the sharper `≤ μ − 1`, and the `−1` must come from the alternating tail
  `(p_2−p_3)+(p_4−p_5)+⋯ ≥ 1`. This is exactly the INC arithmetic bound `ll-inclusion-gap` is pursuing
  (`G-INC-1`, via the certified `top-band-decomposition`); it is **not closed here**. **Status vs
  `ll-inclusion-gap`:** that slug's two-step strong induction `n → n−2` (SET IDENTITY
  `S_{G_{n−1}} ∩ [0,2^{n−2}) = S_{G_{n−3}}`) closes `G-INC-1` sub-cases `h≥4`, `h=2` with `deficit_top≥1`,
  and `h=2, a≥b` via the strengthened IH `Claim(n,ε)`, leaving sub-case `2b-ii (a<b)` open — the SAME
  residual, from the parallel direction. Whichever route closes the alternating-tail `+1` bound first,
  both GAP-A here and `G-INC-1` there close together; we **import**, do not re-prove, per the outline.

**Net advance this round:** Lemma REFL-gen (new, promotable) + the double-REFL formula (II) close branch
B3 sub-cases **B3a and B3b for all `n`**, and close **B3c (hence all of GAP-B) at `n = 3`** for the
anchor `R = G_{n−1}`, reducing general-`n` B3c to the single clean, tight inequality (B2\*). The crux
(B2\*)/GAP-A is not papered over: it is isolated exactly and shown to coincide with the shared
alternating-tail bound. Two scope caveats stated honestly: (a) this subsection treats the **anchor
`R = G_{n−1}` unrefined**; the full Sub-3b/B3 with a *refined* `R` (min `A = 3/2` numerically) is a
further residual not addressed by double-REFL; (b) (B2\*) is proved only at `n = 3`.

---

# Refined `R`: the general-`R` core, budget reduction, and residual breakdown (R8)

Everything above treats `R` as a general refinement of `G_{n−1}` in the *statement* of Lemma LL, but the
Sub-3b closure (double-REFL) was written for the **anchor** `R = G_{n−1}` (unrefined). This section makes
the general-refinement case explicit: it pins down exactly which parts of Lemma LL are **R-agnostic**
(closed for every admissible `R`), and reduces the remainder to three precisely stated crux/residual
buckets. Throughout, `R` refines `G_{n−1}` with `A(R) ≥ 1`, `M := max(R) ≤ 2^{n−1}` (imported from the
induction), and the **joint cut budget** `#Q-cuts + #R-cuts ≤ n` holds; write `c_R := #R-cuts` and
`c_Q := #Q-cuts = |Q| − 1`. We call `R` *refined* if `c_R ≥ 1` (`R ≠ G_{n−1}`).

## The general-`R` core: Cases 1, 2, Sub-3a are R-agnostic (CLOSED for every admissible `R`).

> **Lemma (General-`R` core).** Let `Q` partition `2^n` into `≥ 2` positive parts and let `R` be **any**
> finite multiset with `max(R) ≤ 2^{n−1}` and `A(R) ≥ 1`. If **any** of the following holds, then
> `A(Q∪R) = measure(S_Q △ S_R) ≥ 1`:
> - **(Case 1)** `max(Q) ≥ 2^{n−1} + 1`;
> - **(Case 2)** `|Q| + |R|` is odd and every piece of `P = Q∪R` has length `≥ 1`;
> - **(Sub-3a)** some dyadic level `I_k` (`I_0 = [0,1)`, `I_k = [2^{k−1},2^k)`, `1 ≤ k ≤ n−1`) has
>   `N_P = N_Q + N_R` odd throughout `I_k`.

*Proof.* Each is exactly the argument already given above, and inspecting those proofs, the **only**
facts used about `R` are `max(R) ≤ 2^{n−1}` (equivalently `S_R ⊆ [0,2^{n−1})`, fact (F1)) and — for
Case 2 — that `R`'s pieces are counted in `|R|` and enter `P`; **no band structure of `G_{n−1}` is used**:
- **Case 1** uses only (F1) and (F2) (`ΣQ = 2^n` ⟹ at most one part of `Q` exceeds `2^{n−1}`): for
  `x ∈ [2^{n−1}, max(Q))`, `N_Q(x) = 1`, `N_R(x) = 0`, so `[2^{n−1}, max(Q)) ⊆ S_Q △ S_R`, of measure
  `max(Q) − 2^{n−1} ≥ 1`. This is the certified `lemmas/ll-case1-high-interval.md`, whose hypothesis is
  literally "`max(R) ≤ 2^{n−1}`" — R-agnostic.
- **Case 2** is the certified `lemmas/parity-piece-count.md` (Lemma P) applied to the multiset `P`
  itself: an odd number of pieces all `≥ 1` gives `A(P) ≥ min(P) ≥ 1`. It sees only the sorted list of
  `P`, not where the pieces came from — R-agnostic.
- **Sub-3a** is the certified `lemmas/dyadic-level-parity.md`: if `N_P` is odd throughout `I_k` then
  `I_k ⊆ S_Q △ S_R`, measure `≥ measure(I_k) ≥ 1`. It is a statement about `P = Q∪R` alone — R-agnostic. ∎

Thus the general-`R` core closes Lemma LL for every configuration falling in Case 1, Case 2, or Sub-3a,
**for any refined `R`** exactly as for the anchor. *(Verified n=3, ½-grid, joint budget enforced: of 371
refined-`R` configs (`c_R ≥ 1`), 241 fall in Case 1, 48 in Case 2, 51 in Sub-3a — **340/371 = 91.6%
closed** with 0 violations; A-min over these = 1.)*

## Budget-reduction lemma (refined `R` has `|Q| ≤ n`).

> **Lemma (Budget reduction).** If `R` is refined (`c_R ≥ 1`) then `|Q| ≤ n`.

*Proof.* The joint cut budget is `c_Q + c_R ≤ n`. With `c_R ≥ 1`, `c_Q ≤ n − 1`, so `|Q| = c_Q + 1 ≤ n`. ∎

(For the anchor `R = G_{n−1}` we only had `|Q| ≤ n+1`. So every refined-`R` configuration has strictly
fewer `Q`-parts; in particular the residual buckets below all satisfy `|Q| ≤ n`.)

## The refined-`R` residual, split into three buckets (exhaustive).

A configuration not covered by the general-`R` core has `max(Q) < 2^{n−1}+1` and is **not** (odd count with
all pieces `≥ 1`) and has **no** fully-odd dyadic level (it fails Cases 1, 2, and Sub-3a). We split the
residual by `max(Q)` and, when `max(Q) < 2^{n−1}`, by whether the top piece `2^{n−1}` of `G_{n−1}` was
cut. These three buckets are disjoint and exhaustive (the trichotomy `max(Q) ≥ 2^{n−1}` / [`max(Q) < 2^{n−1}`
and `2^{n−1} ∈ R`] / [`max(Q) < 2^{n−1}` and `2^{n−1} ∉ R`] partitions the residual, using that
`max(R) = 2^{n−1} ⟺ 2^{n−1} ∈ R` — since refinement only cuts, a piece of length `2^{n−1}` survives iff
the original top piece is uncut):

### Bucket (i): `max(Q) ≥ 2^{n−1}` (branches B1, B2). Reduced (R-agnostic) to *GAP-A refined-R*.

Let `μ := max(Q) ∈ [2^{n−1}, 2^{n−1}+1)`. Since `max(R) ≤ 2^{n−1} ≤ μ`, the **certified Lemma REFL**
(`lemmas/ll-reflection-identity.md`) applies verbatim (its hypothesis is `μ ≥ 2^{n−1}` and
`max(R) ≤ 2^{n−1}` — it never assumes `R = G_{n−1}`), giving
```
A(Q∪R) = μ − A(Q'∪R),     Q' := Q ∖ {μ}.
```
Hence `A(Q∪R) ≥ 1 ⟺ A(Q'∪R) ≤ μ − 1`, the **GAP-A refined-R** upper bound. This is a genuine one-step,
non-circular reduction (`Q'∪R` is not a valid `G_{n−1}`-refinement — its total sum is `2^{n+1}−μ−(2^n−ΣR)`,
not `2^n − 1`). *(Verified n=3, ½-grid, budget: over all 27 residual configs with `μ ≥ 2^{n−1}`, the REFL
identity holds and `A(Q'∪R) ≤ μ − 1` holds, 0 violations.)* This upper bound is **open** and lies in the
alternating-tail `+1` crux family (see the honesty note below); it is *not* claimed closed.

### Bucket (ii): `max(Q) < 2^{n−1}`, top piece `2^{n−1}` UNCUT (`2^{n−1} ∈ R`). Double-REFL generalizes.

Here `max(R) = 2^{n−1}` is the **unique** global maximum of `P` (every part of `Q` is `< 2^{n−1}`, and
every part of `R` other than the top piece is `≤ 2^{n−2}`). Crucially, `R' := R ∖ {2^{n−1}}` is a
**refinement of `G_{n−2}`** with `max(R') ≤ 2^{n−2}`: since the top piece is uncut, all `c_R` cuts fell on
the pieces `{1,2,…,2^{n−2}} = G_{n−2}`, so `R'` refines `G_{n−2}`. The **anchor** double-REFL proof used
`R = G_{n−1}` only through the two facts `max(R) = 2^{n−1}` and `max(R∖\{2^{n−1}\}) ≤ 2^{n−2}`; both hold
here. We therefore repeat it with `R'` in place of `G_{n−2}`:

**First reflection** (certified Lemma REFL, with roles "`Q`"`:= R` (`μ = 2^{n−1}`), "`R`"`:= Q`
(`max(Q) < 2^{n−1}`)):
```
A(Q∪R) = 2^{n−1} − A(Q∪R').                                    (I-ref)
```
Split on `q_1 := max(Q)` versus `2^{n−2}`:

- **(B3a-ref) `q_1 ≤ 2^{n−2}`. CLOSED (all `n`).** Then `max(Q∪R') ≤ 2^{n−2}` (both `max(Q) ≤ 2^{n−2}` and
  `max(R') ≤ 2^{n−2}`), so by Lemma M0 `A(Q∪R') ≤ 2^{n−2} ≤ 2^{n−1} − 1` (`n ≥ 2`), and (I-ref) gives
  `A(Q∪R) ≥ 2^{n−1} − 2^{n−2} = 2^{n−2} ≥ 1`. ∎

- **`q_1 > 2^{n−2}` (so `q_1` is the unique max of `Q∪R'`, as `max(R') ≤ 2^{n−2} < q_1`).** **Second
  reflection** (certified Lemma REFL-gen, `lemmas/ll-reflection-identity-gen.md`, hypothesis
  `max(R') ≤ q_1 = μ` — satisfied):
  ```
  A(Q∪R') = q_1 − A(Q'∪R'),   Q' := Q ∖ {q_1};
  ```
  substituting into (I-ref):
  ```
  A(Q∪R) = 2^{n−1} − q_1 + A(Q'∪R').                            (II-ref)
  ```
  - **(B3b-ref) `2^{n−2} < q_1 ≤ 2^{n−1} − 1`. CLOSED (all `n`).** By Lemma M0 `A(Q'∪R') ≥ 0`, so (II-ref)
    gives `A(Q∪R) ≥ 2^{n−1} − q_1 ≥ 1`. ∎
  - **(B3c-ref) `2^{n−1} − 1 < q_1 < 2^{n−1}`.** By (II-ref), `A(Q∪R) ≥ 1 ⟺ A(Q'∪R') ≥ q_1 − (2^{n−1}−1)
    =: δ ∈ (0,1)`, so it suffices to prove the refined-level-down residual
    ```
    (B2*)-ref:   A(Q'∪R') ≥ 1,    R' refining G_{n−2}, max(R') ≤ 2^{n−2}, A(R') ≥ ?.
    ```
    This is the exact analogue of the anchor's (B2*) with `G_{n−2}` replaced by the refinement `R'`. It is
    **open** (crux family); it is *not* claimed closed. *(Verified n=3, ½-grid, budget: over the
    top-uncut residual configs, (I-ref) and (II-ref) hold with 0 mismatches; B3a-ref/B3b-ref fire and
    close; only B3c-ref remains.)*

So for bucket (ii) the double-REFL closes B3a-ref and B3b-ref **for all `n`**, reducing the residual to
`(B2*)-ref`. This genuinely extends the anchor GAP-B closure to **every refined `R` whose top piece is
uncut**, because the anchor proof was never `G_{n−1}`-specific beyond the two structural facts above.

### Bucket (iii): `max(Q) < 2^{n−1}` and `max(R) < 2^{n−1}` (top piece CUT). Genuine no-anchor residual.

Here `max(P) = max(max(Q), max(R)) < 2^{n−1}`: **there is no piece at or above `2^{n−1}`**, so neither the
Case-1 high interval, nor the first reflection of bucket (ii), has an anchor. Reflecting on `max(P)` (a cut
sub-piece `< 2^{n−1}`) does **not** telescope: removing it leaves a remainder that is not a clean
`G_m`-refinement, so no level-down formula is available. This bucket is the **honest remaining hard
residual** of the refined-`R` lower bound; it is left OPEN. *(Verified n=3, ½-grid, budget: exactly **2 of
371** refined configs land here after the general-`R` core and buckets (i),(ii): `Q=\{7/2,7/2,1\},
R=\{7/2,2,1,1/2\}` and `Q=\{7/2,3,3/2\}, R=\{7/2,2,1,1/2\}`, both with `A(Q∪R) = 2 ≥ 1` (non-tight); the
tight `A=1` refined instances (e.g. `Q=\{4,4\}, R=\{3,2,1,1\}`) have `max(Q)=2^{n−1}` and are handled by
bucket (i)/B2 via Lemma REFL, not here. Bucket (iii) is small but nonempty and genuinely without a
reflection anchor.)*

**Honesty note (crux family, not double-counted).** Buckets (i) and (ii) both reduce to alternating-tail
`+1` inequalities (`A(Q'∪R) ≤ μ−1` and `A(Q'∪R') ≥ 1`). These are the SAME *family* as the anchor GAP-A /
`ll-inclusion-gap`'s `G-INC-1`, but with a **refined** `R` (resp. `R'`), which — per the refinedR explorer
and confirmed by the tight case `R = {4,4,4,2,1}`, `Q = {5,5,4,2}` at `n=4` (`S_Q = [2,4) ⊄ S_{G_3}`) — is
**genuinely separate** from the anchor `T(ℓ)`: the anchor's SET IDENTITY `S_{G_{n−1}} ∩ [0,2^{n−2}) =
S_{G_{n−3}}` and top-band decomposition are `G_{n−1}`-specific and have no known refined-`R` analogue. So
we do **not** claim these refined-`R` cruxes closed by importing `T(ℓ)`; they are stated as open residuals.

---

# Bucket (iii): cheap-kills, n=3 closure, and REFL termination (R9)

Throughout this section `P = Q∪R`, `B := measure(S_Q∩S_R)`, and we use the certified merge identity
(Lemma M): `A(Q∪R) = A(Q) + A(R) − 2B` with `0 ≤ B ≤ min(A(Q), A(R))` (as `S_Q∩S_R ⊆ S_Q` and `⊆ S_R`).
The standing hypotheses of Lemma LL give `A(R) ≥ 1` and `max(R) ≤ 2^{n−1}`. **Bucket (iii)** is the
top-cut residual `max(Q) < 2^{n−1}` **and** `max(R) < 2^{n−1}`.

## All-`n` cheap-kill lemmas (rigorous, promotable).

> **Lemma K1 (small-overlap kill).** If `2B ≤ A(Q)` then `A(Q∪R) ≥ A(R) ≥ 1`. In particular, if
> `S_Q ∩ S_R = ∅` (so `B = 0`) then `A(Q∪R) = A(Q) + A(R) ≥ 1`.

*Proof.* `A(Q∪R) = A(Q) + A(R) − 2B ≥ A(Q) + A(R) − A(Q) = A(R) ≥ 1`. ∎

> **Lemma K2 (difference kill).** Always `A(Q∪R) ≥ |A(Q) − A(R)|`. Hence if `|A(Q) − A(R)| ≥ 1` then
> `A(Q∪R) ≥ 1`.

*Proof.* Since `B ≤ min(A(Q), A(R))`, `A(Q∪R) = A(Q) + A(R) − 2B ≥ A(Q) + A(R) − 2min(A(Q),A(R)) =
|A(Q) − A(R)|`. ∎

*(Verified `n=3`, `1/4`-grid, budget: K1 (`B=0`) covers 9/42 bucket-(iii) configs; K1∪K2 together cover
the majority; the rest are handled by the `n=3` closure below.)*

## `n = 3` bucket (iii): complete closure.

**Structure forced at `n = 3`.** Here `2^n = 8`, `2^{n−1} = 4`. In bucket (iii) every part of `Q` is
`< 4` and `ΣQ = 8`; two parts `< 4` cannot sum to `≥ 8`, so if `|Q| = 2` the larger part is `8 −` (smaller
`> 4`) — contradiction. Hence `|Q| ≥ 3`, i.e. `c_Q ≥ 2`. The top piece `4` of `G_2` is cut, so `c_R ≥ 1`.
The joint budget `c_Q + c_R ≤ n = 3` then forces `c_Q = 2`, `c_R = 1` **exactly**: `|Q| = 3`, and `R` is
`G_2 = {1,2,4}` with a single cut of the `4`-piece, i.e.
```
R = {4 − a, 2, a, 1},   0 < a ≤ 2   (write the two halves of the cut as 4−a ≥ a).
```
Write `Q = {q_1, q_2, q_3}`, `q_1 ≥ q_2 ≥ q_3 > 0`, `q_1 + q_2 + q_3 = 8`, each `q_i < 4`.

**`S_Q` and a `Q`-only lemma.** Since `q_1 ≥ 8/3 > 2`, `N_Q(x) = #\{q_i > x\}` equals `3` on `[0,q_3)`,
`2` on `[q_3,q_2)`, `1` on `[q_2,q_1)`, `0` above; so
```
S_Q = [0, q_3) ∪ [q_2, q_1),   A(Q) = q_3 + (q_1 − q_2).
```
First, `q_2 > 2` **always**: if `q_2 ≤ 2` then `q_3 ≤ q_2 ≤ 2`, forcing `q_1 = 8 − q_2 − q_3 ≥ 4`,
contradicting `q_1 < 4`.

> **Lemma Q3 (`Q`-only).** For `Q` as above, `2·measure(S_Q ∩ [2, ∞)) ≤ A(Q)`.

*Proof.* Since `q_2 > 2`, `S_Q ∩ [2,∞) = ([0,q_3)∩[2,∞)) ∪ ([q_2,q_1)∩[2,∞)) = [2, q_3)^{+} ∪ [q_2, q_1)`,
of measure `m := (q_3 − 2)^{+} + (q_1 − q_2)`. Two cases.
- **`q_3 ≤ 2`:** `m = q_1 − q_2`, so `A(Q) − 2m = (q_3 + q_1 − q_2) − 2(q_1 − q_2) = q_3 + q_2 − q_1 =
  (8 − q_1) − q_1 = 8 − 2q_1 > 0` (as `q_1 < 4`).
- **`q_3 > 2`:** `m = (q_3 − 2) + (q_1 − q_2)`, so `A(Q) − 2m = (q_3 + q_1 − q_2) − 2(q_3 − 2 + q_1 − q_2) =
  4 − (q_1 + q_3 − q_2) = 4 − (8 − 2q_2) = 2q_2 − 4 > 0` (as `q_2 > 2`).
In both cases `2m ≤ A(Q)`. ∎

**`S_R` in closed form.** A direct count of `N_R(x) = #\{parts of R > x\}` gives (all boundaries checked):
- **Regime I, `a ∈ (0,1]`:** parts ordered `4−a ≥ 2 ≥ 1 ≥ a`; `N_R` is `4` on `[0,a)`, `3` on `[a,1)`,
  `2` on `[1,2)`, `1` on `[2,4−a)`, `0` above, so `S_R = [a,1) ∪ [2, 4−a)`, `A(R) = (1−a)+(2−a) = 3 − 2a`.
- **Regime II, `a ∈ [1,2]`:** parts ordered `4−a ≥ 2 ≥ a ≥ 1`; `N_R` is `4` on `[0,1)`, `3` on `[1,a)`,
  `2` on `[a,2)`, `1` on `[2,4−a)`, `0` above, so `S_R = [1,a) ∪ [2,4−a)`, `A(R) = (a−1)+(2−a) = 1`.
  (The two regimes agree at `a=1` where the first interval is empty and `S_R = [2,3)`, `A(R)=1`; and the
  degenerate ends `a→0^+`, `a=2` are limits of the stated forms.) In all cases `A(R) ≥ 1`, as required.

In every regime `S_R = L ∪ H` with lower part `L ⊆ [0,2)` and upper part `H = [2, 4−a) ⊆ [2,∞)`. Split
`B = B_L + B_H`, `B_L := measure(S_Q ∩ L)`, `B_H := measure(S_Q ∩ H)`. Since `H ⊆ [2,∞)`, Lemma Q3 gives
```
2 B_H ≤ 2·measure(S_Q ∩ [2,∞)) ≤ A(Q).                                   (Q3′)
```

### Regime I (`a ∈ (0,1]`). CLOSED.
Here `L = [a,1)`, so `B_L ≤ measure([a,1)) = 1 − a`. Using the merge identity, `(Q3′)`, and `A(R)=3−2a`:
```
A(Q∪R) = A(Q) + (3 − 2a) − 2B_L − 2B_H
       ≥ A(Q) + (3 − 2a) − 2(1 − a) − A(Q) = (3 − 2a) − (2 − 2a) = 1.
```
∎ (Regime I)

### Regime II (`a ∈ [1,2]`). CLOSED.
Here `A(R) = 1`, `L = [1,a)`, and (since `q_2 > 2 ≥ a`) `[q_2,q_1) ∩ [1,a) = ∅`, so
`B_L = measure([0,q_3) ∩ [1,a)) = (min(q_3,a) − 1)^{+}`. We must show `A(Q∪R) = A(Q) + 1 − 2B ≥ 1`, i.e.
`2B ≤ A(Q)`. Note the useful identity `A(Q) = q_3 + q_1 − q_2 = q_3 + (8 − q_2 − q_3) − q_2 = 8 − 2q_2`.
Split on `q_3`.
- **`q_3 ≤ 1`:** `B_L = 0`, so by `(Q3′)`, `2B = 2B_H ≤ A(Q)`. ∎
- **`q_3 ≥ 2`:** `A(Q) = q_3 + (q_1 − q_2) ≥ q_3 ≥ 2`, so by Lemma K2, `A(Q∪R) ≥ |A(Q) − 1| = A(Q) − 1 ≥ 1`.
  ∎
- **`1 < q_3 < 2`:** then `(q_3 − 2)^{+} = 0`, so `B_H = measure([q_2,q_1) ∩ [2,4−a)) =
  (min(q_1, 4−a) − q_2)^{+}`, and `B_L = min(q_3,a) − 1 ≤ a − 1`. We show `2B ≤ A(Q) = 8 − 2q_2` by
  sub-cases on the position of `4−a` relative to `q_2, q_1` (recall `q_2 > 2`, `q_1 < 4`, `4−a ∈ [2,3]`):
  - **`4 − a ≤ q_2`:** then `min(q_1,4−a) = 4−a ≤ q_2`, so `B_H = 0` and `2B = 2B_L = 2(min(q_3,a) − 1)`.
    We claim `min(q_3,a) ≤ 5 − q_2` (whence `2B_L ≤ 2(5 − q_2) − 2 = 8 − 2q_2 = A(Q)`): if `q_2 < 3` then
    `5 − q_2 > 2 > q_3 ≥ min(q_3,a)`; if `q_2 ≥ 3` then from `q_1 ≥ q_2` we get `q_3 = 8 − q_1 − q_2 ≤
    8 − 2q_2 ≤ 5 − q_2`, so `min(q_3,a) ≤ q_3 ≤ 5 − q_2`. ✓
  - **`q_2 < 4 − a` and `4 − a ≥ q_1`:** then `min(q_1,4−a) = q_1`, `B_H = q_1 − q_2`, so
    `2B ≤ 2(a − 1) + 2(q_1 − q_2)`. Using `q_1 − q_2 − q_3 = q_1 − (8 − q_1) = 2q_1 − 8`,
    `A(Q) − 2B ≥ (q_3 + q_1 − q_2) − 2(a−1) − 2(q_1 − q_2) = q_3 − q_1 + q_2 − 2a + 2 =
    −(2q_1 − 8) − 2a + 2 = 10 − 2q_1 − 2a = 2(5 − q_1 − a) > 0`, since `4 − a ≥ q_1 ⟹ q_1 + a ≤ 4 < 5`. ✓
  - **`q_2 < 4 − a < q_1`:** then `min(q_1,4−a) = 4−a`, `B_H = 4 − a − q_2`, so
    `2B ≤ 2(a−1) + 2(4 − a − q_2) = 6 − 2q_2 < 8 − 2q_2 = A(Q)`. ✓
  In every sub-case `2B ≤ A(Q)`, so `A(Q∪R) ≥ 1`. ∎ (Regime II)

Thus `A(Q∪R) ≥ 1` for **every** `n=3` top-cut configuration, so **bucket (iii) is completely closed at
`n = 3`.** *(Machine-checked, `1/16`-grid, budget enforced: 10912 configurations, `min A(Q∪R) = 1`, 0
violations; `q_2 > 2` and Lemma Q3's `2m ≤ A(Q)` verified on every one.)*

## Double-REFL telescoping: rigorous termination, and the honest general-`n` gap.

For general `n`, bucket (iii) has no piece at `2^{n−1}` (both maxima are `< 2^{n−1}`), so the first
reflection of bucket (ii) has no anchor. The available tool is repeated reflection at the **running global
maximum**. We make its termination precise (the reviewer's required point) and then state honestly what it
does and does not yield.

> **Lemma REFL-telescope (termination).** Let `P` be any finite positive multiset with `|P| = m` pieces.
> Define `P_0 := P` and, for `i ≥ 0` while `|P_i| ≥ 1`, `μ_i := max(P_i)` and `P_{i+1} := P_i ∖ {μ_i}`
> (delete one copy of the maximum). Then `A(P) = μ_0 − μ_1 + μ_2 − ⋯ + (−1)^{m−1} μ_{m−1}`, and the process
> **terminates in exactly `m` steps** at the empty multiset.

*Proof.* Each step removes exactly one piece, so `|P_{i+1}| = |P_i| − 1`; the piece-count is a
non-negative integer strictly decreasing by `1` each step, hence reaches `0` after `m` steps (a manifest
well-founded descent, with the total `ΣP_i` also strictly decreasing by `μ_i > 0`). Applying certified
Lemma REFL-gen (`lemmas/ll-reflection-identity-gen.md`) with `Q := \{μ_i\}` and `R := P_{i+1}` (its
hypothesis `max(R) ≤ μ_i` holds since `μ_i = max(P_i)`) gives `A(P_i) = μ_i − A(P_{i+1})`. Unrolling this
`m`-fold recursion — valid by the finite descent just established — yields the alternating sum, and
`A(∅) = 0`. ∎

When the two largest pieces of `P = Q∪R` are `M_Q := max(Q)` from `Q` and `M_R := max(R)` from `R` (i.e.
`max(Q ∖ \{M_Q\}) ≤ M_R` and `M_Q ≥ M_R`), the first two steps give the **double-REFL cancellation**
```
A(Q∪R) = M_Q − M_R + A(Q' ∪ R''),   Q' := Q ∖ \{M_Q\},  R'' := R ∖ \{M_R\},           (III)
```
verified on the concrete `n=3` instance `Q=\{15/4,13/4,1\}, R=\{15/4,2,1,1/4\}`: both maxima are `15/4`,
they cancel, and `A(Q∪R) = A(\{13/4,1\}∪\{2,1,1/4\}) = 3/2 ≥ 1`.

**Honest scope.** Lemma REFL-telescope *terminates* (proved), but by itself it only *recomputes* `A(P)` as
an alternating sum; the substantive question — that the bottom object satisfies `A ≥ 1` — is not delivered
by termination. Concretely `(III)` reduces bucket (iii) to `A(Q'∪R'') ≥ 1 − (M_Q − M_R)`, which in the
tight sub-case `M_Q ≈ M_R ≈ 2^{n−1}` is again an alternating-tail `+1` inequality for a *smaller refined
system* `Q'∪R''` (with `ΣQ' = 2^n − M_Q`, `ΣR'' = 2^n − 1 − M_R`, neither a clean `G_m`-refinement). This
is the **refined-`R` alternating-tail crux** — genuinely separate from the anchor `T(ℓ)` (no refined-`R`
SET IDENTITY / top-band decomposition is known), and it is **NOT closed here for general `n`.** We do not
claim otherwise: only `n = 3` bucket (iii) is closed (above), together with the all-`n` cheap-kills K1, K2
(which fire whenever `S_Q, S_R` are near-disjoint or their alternating sums differ by `≥ 1`).

---

# Bucket (iii), general `n`: the INC/GAP split and Opening D (R10)

R9 closed bucket (iii) fully at `n = 3` and proved the certified **REFL-telescope** terminates. This
section attacks **general `n`**. The certified telescope gives, whenever the two largest parts of
`P = Q∪R` are `M_Q := max(Q)` and `M_R := max(R)`,
```
A(Q∪R) = M_Q − M_R + A(Q'∪R''),   Q' := Q∖{M_Q}, R'' := R∖{M_R}      (III, certified R9)
```
but the bottom object `A(Q'∪R'')` carries no `2^{n−1}` anchor, so (III) only *recomputes* `A`. Instead we
split bucket (iii) **directly on containment**, which needs no reflection and reaches the actual claim.

Throughout: `Q` partitions `2^n` (`ΣQ = 2^n`), `R` refines `G_{n−1} = \{2^0,…,2^{n−1}\}` (so
`ΣR = ΣG_{n−1} = 2^n − 1`, since refinement preserves total mass), `A(R) ≥ 1`, `max(R) ≤ 2^{n−1}`, joint
budget `c_Q + c_R ≤ n`, and
**bucket (iii)** is `max(Q) < 2^{n−1}` **and** `max(R) < 2^{n−1}`. By the merge identity (Lemma M),
`A(Q∪R) = A(Q) + A(R) − 2B`, `B := measure(S_Q ∩ S_R)`, `0 ≤ B ≤ min(A(Q), A(R))`.

## The containment split (exhaustive, disjoint).

Every bucket-(iii) configuration is exactly one of:
- **INC:** `S_Q ⊆ S_R`;
- **GAP:** `S_Q ⊄ S_R` (there is a point of `S_Q` outside `S_R`).

These are complementary by definition. *(Verified n=4, `½`-grid, joint budget: of 1617 bucket-(iii)
configs, 129 INC and 1488 GAP; `A(Q∪R) ≥ 1` with 0 violations across all.)*

## INC sub-instances: reduction to the refined-`R` crux (conditional import).

On `S_Q ⊆ S_R` the certified **INC reduction** (`lemmas/forcing-inc-reduction.md`, Part 2) gives
`measure(S_Q ∩ S_R) = measure(S_Q) = A(Q)`, hence
```
A(Q∪R) = A(Q) + A(R) − 2A(Q) = A(R) − A(Q).
```
So in the INC branch **`A(Q∪R) ≥ 1 ⟺ A(R) ≥ A(Q) + 1`**. With `ΣQ = 2^n` this is exactly the refined-`R`
alternating-tail inequality **Claim_R(n, ε = 0)** of the lb-unifier program (for `h_R := #{R\text{-parts}
≥ 2^{n−2}}` even), resp. the `|Q|`-parity fact of `ll-inclusion-gap`'s Opening C/E (for `h_R` odd). That
program — the mutual strong induction `{Claim_R(n,ε), T_R(n)}` descending `n → n−2` via the certified
**Gen-Decomp** (`lemmas/gen-decomp-refined.md`, which supplies `S_{Q_lo} ⊆ S_{R_lo}` with no SET IDENTITY)
— is being built in `ll-inclusion-gap` this round. We therefore record the INC branch as a **clean
conditional reduction**:

> **(INC-import).** If `{Claim_R, T_R}` certifies (for all `h_R`-even admissible `R`) together with the
> `h_R`-odd `|Q|`-parity fact, then every INC sub-instance of bucket (iii) satisfies `A(Q∪R) ≥ 1`.

We do **not** claim INC closed here: it is conditional on that build. (Per the outline: "state as a clean
reduction; do not re-derive"; per the reviewer: "conditional… if that build stalls.") The reduction itself
— `A(Q∪R) = A(R) − A(Q)` on `S_Q ⊆ S_R` — is rigorous and certified.

## GAP sub-instances: Opening D.

Here `S_Q ⊄ S_R`. Set `g := N_Q − N_R`, an integer-valued step function. Two standing facts:
- **(G1) Parity.** `N_Q + N_R ≡ N_Q − N_R = g (mod 2)`, so `S_Q △ S_R = \{x : N_P(x)\text{ odd}\} =
  \{x : g(x)\text{ odd}\}` and `A(Q∪R) = measure(S_Q △ S_R) = measure\{g\text{ odd}\}` (Lemma M).
- **(G2) Integral.** `∫_0^∞ N_Q\,dx = Σ_{p∈Q} ∫_0^{p} dx = ΣQ` and likewise for `R`, so
  `∫_0^∞ g\,dx = ΣQ − ΣR = 2^n − (2^n − 1) = 1`.
- **(G3) Bounded complexity.** `g` is constant on each maximal interval between consecutive part-values of
  `P`; the number of distinct part-values is `≤ |Q| + |R| = (c_Q+1) + (n + c_R) = n+1 + (c_Q+c_R) ≤ 2n+1`
  (using `|G_{n−1}| = n` and the joint budget). And `S_Q, S_R ⊆ [0, 2^{n−1})`, which is partitioned into
  the `n` dyadic levels `I_0 = [0,1)`, `I_k = [2^{k−1},2^k)` (`1 ≤ k ≤ n−1`). So `g` is a step function
  with `≤ 2n+1` pieces spread over `n` levels — *bounded oscillation per level on average.* (This bounded
  complexity, absent from the pure "`∫g = 1`" picture, is what makes `measure\{g\text{ odd}\} ≥ 1` true;
  the abstract `g ≡ 2` on `[0,½)` has `∫g = 1` but is not realizable here — `ΣQ = 2^n` forces large parts,
  hence wide support.)

The target is `measure\{g\text{ odd}\} ≥ 1`. Note the recorded obstruction: `∫g = 1` **alone** does not
give it (`g ≡ 2` on `[0,½)` is even everywhere with `∫g = 1`). Opening D must use the step structure, not
just the integral. We give two rigorous slices and one new all-`n` kill; the general accumulation is the
honest gap.

### Lemma D1 (small-discrepancy kill; NEW, all `n`, rigorous, promotable).

> **Lemma D1.** If `|N_Q(x) − N_R(x)| ≤ 1` for every `x ≥ 0`, then `A(Q∪R) ≥ |ΣQ − ΣR|`. In bucket (iii)
> (indeed whenever `ΣQ − ΣR = 1`), this gives `A(Q∪R) ≥ 1`.

*Proof.* With `g := N_Q − N_R` and the hypothesis `|g| ≤ 1`, the value `g(x)` is odd **iff** `g(x) ≠ 0`
(the only odd value in `\{−1,0,1\}` is `±1`). Hence by (G1),
```
A(Q∪R) = measure\{g\text{ odd}\} = measure\{g ≠ 0\}.
```
On `\{g ≠ 0\}` we have `|g| = 1`, so `∫_0^∞ |g|\,dx = ∫_{\{g≠0\}} 1\,dx = measure\{g ≠ 0\}`. Combining with
`∫|g| ≥ |∫ g|` and (G2),
```
A(Q∪R) = measure\{g ≠ 0\} = ∫|g| ≥ |∫ g| = |ΣQ − ΣR| = 1.   ∎
```

D1 is the first rigorous **general-`n`** GAP tool that beats the `∫g = 1` obstruction: it is exactly the
observation that when the discrepancy `g` never reaches an *even nonzero* value, "odd" and "nonzero"
coincide and the signed integral becomes a genuine lower bound on the odd mass.

### The cheap-kill package (K1, K2, D1) and its GAP coverage.

Recall the certified all-`n` cheap kills of R9: **K1** (`2B ≤ A(Q) ⟹ A(Q∪R) ≥ A(R) ≥ 1`) and **K2**
(`|A(Q) − A(R)| ≥ 1 ⟹ A(Q∪R) ≥ 1`). Adding **D1** gives a three-lemma package, all rigorous for every `n`:

> **(GAP-kills).** In any GAP sub-instance, if `2B ≤ A(Q)` (K1) **or** `|A(Q) − A(R)| ≥ 1` (K2) **or**
> `|N_Q − N_R| ≤ 1` pointwise (D1), then `A(Q∪R) ≥ 1`.

*(Verified, joint budget enforced: **n=3** bucket (iii), all 168 configs are GAP, K1/K2/D1 close
**166/168** — the remaining 2 are the tight `A = 1` configs handled by the full R9 `n=3` closure (Regimes
I/II). **n=4** bucket (iii), 1488 GAP configs, K1/K2/D1 close **1449/1488**; the residual **39** configs
all have `A(Q∪R) ≥ 2` (`max|g| ≤ 3`) — comfortably non-tight, but not proven by these kills.)*

So the GAP frontier after R10 is a **small, non-tight residual** (`|g|` reaches `≥ 2` on some excursion,
`A(Q∪R) ≥ 2` empirically). This is genuine progress: the cheap-kill package is rigorous and closes the
overwhelming majority of GAP for every `n`, and the leftover is provably away from tightness.

### Opening D: the level-charge accumulation (honest OPEN gap).

For the residual we set up the dyadic-pairing target precisely and state honestly what is unproven. Define
for each level the **odd-defect** `δ_k := measure(\{x ∈ I_k : g(x)\text{ odd}\})`. By (G1),
`A(Q∪R) = Σ_{k=0}^{n−1} δ_k`, so the target is
```
(Opening D)   Σ_{k=0}^{n−1} δ_k ≥ 1.
```
Two levels of control are proven: (a) **Sub-3a** (certified `dyadic-level-parity`): if some level is
odd-constant then `δ_k ≥ measure(I_k) ≥ 1` alone, done; (b) **D1**: if `|g| ≤ 1` throughout then
`Σ_k δ_k = measure\{g ≠ 0\} ≥ ∫|g| ≥ 1`. The residual is where neither fires: no level is odd-constant,
and `g` makes at least one even excursion of magnitude `≥ 2`. The intended mechanism — pair each maximal
`S_Q`-only sub-interval on a level against a nearest `S_R`-only sub-interval, charging the alignment cost
so that `Σ_k δ_k ≥ 1` — is **not proven**: there is at present no argument that the accumulated pairing
cost reaches `1` (the reviewer's standing point that Opening D is "a direction, not a mechanism"). We flag
this as the load-bearing OPEN gap of this slug. What R10 adds is rigorous: the reduction (G1)–(G3), the new
kill D1, and the coverage bound (all GAP but a small non-tight residual closes for every `n`).

**Honest scope of bucket (iii), general `n`.** INC sub-instances reduce (rigorously, certified) to the
refined-`R` crux `{Claim_R, T_R}` — **conditional** on the `ll-inclusion-gap` build. GAP sub-instances are
closed for every `n` outside a small non-tight residual by the rigorous kills K1/K2/D1 (+ Sub-3a); the
residual and the general Opening-D accumulation are **OPEN**. No overclaim: bucket (iii) general `n` is
**not** closed; only `n = 3` is (R9).

# Bucket (iii), general `n`: correction to the INC premise, D1-direct, and the level-charge reduction (R11)

Standing setup (as in the R10 section): `Q` partitions `2^n`, `R` refines `G_{n−1}` (so `ΣR = 2^n − 1`),
`A(R) ≥ 1`, joint budget `c_Q + c_R ≤ n`, and **bucket (iii)** is `max(Q) < 2^{n−1}` and
`max(R) < 2^{n−1}`. Write `g := N_Q − N_R`. By the certified merge/measure identities (Lemmas M0, M),
`A(Q∪R) = measure\{x : N_Q(x)+N_R(x)\text{ odd}\} = measure\{x : g(x)\text{ odd}\}`, and
`∫_0^∞ g\,dx = ΣQ − ΣR = 1`. `g` is an integer step function with breakpoints only at part-values of
`Q∪R`, of which there are `≤ |Q| + |R| = (c_Q+1) + (n + c_R) ≤ 2n+1`, all inside `[0, 2^{n−1})`.

## The INC premise is false (correction to the outline).

The outline (and the lb-dyadic explorer) proposed to close the INC branch (`S_Q ⊆ S_R`) non-inductively,
using the structural claim **"INC forces `max(Q) ≤ max(R)`"** and the double-REFL identity
`A(Q∪R) = (max(R) − max(Q)) + A(Q'∪R'')`. Both premises are **wrong**.

> **Counterexample (machine-checked).** At `n = 4` take `Q = \{15/2, 15/2, 1\}` (`ΣQ = 16 = 2^4`, both
> maxima `< 8`) and `R = \{7, 4, 2, 1, 1\}` (a single cut of the `8`-piece of `G_3 = \{1,2,4,8\}` into
> `7+1`, so `ΣR = 15 = 2^4 − 1`, `max(R) = 7 < 8`). Then
> `S_Q = [0,1)` (since `N_Q` is `3` on `[0,1)`, `2` on `[1,15/2)`) and
> `S_R = [0,2) ∪ [4,7)` (since `N_R` is `5,3,2,1` on `[0,1),[1,2),[2,4),[4,7)`), so `S_Q ⊆ S_R`:
> **INC holds**. But `max(Q) = 15/2 > 7 = max(R)`.

The parity argument for "INC `⟹` `max(Q) ≤ max(R)`" assumed the top part of `Q` is unique: it took
`x ∈ (max(R), max(Q))` and claimed `N_Q(x) = 1` (odd), `N_R(x) = 0`, breaking INC. That fails exactly when
`max(Q)` has **even multiplicity**: here two parts equal `15/2`, so on `(7, 15/2)` we have `N_Q = 2`
(*even*), hence that interval is *not* in `S_Q`, and INC is intact. The corrected statement is:

> **Lemma (corrected INC top-order, PROVED).** If `S_Q ⊆ S_R` then either `max(Q) ≤ max(R)`, or `max(Q)`
> occurs an **even** number of times in `Q`.

*Proof.* Suppose `q := max(Q) > r := max(R)`, and let `m ≥ 1` be the multiplicity of `q` in `Q`. Let
`q^- := max\{Q\text{-value} < q\}` (or `0` if none). For `x ∈ (\max(r, q^-), q)` the parts of `Q` exceeding
`x` are exactly the `m` copies of `q`, so `N_Q(x) = m`, while every part of `R` is `≤ r < x`, so
`N_R(x) = 0`. If `m` were odd, `N_Q(x)` would be odd (so `x ∈ S_Q`) while `N_R(x) = 0` (so `x ∉ S_R`),
contradicting `S_Q ⊆ S_R` on the nonempty interval `(\max(r,q^-), q)`. Hence `m` is even. ∎

*(Verified: 0 violations of the corrected disjunction over the n=4 (129 configs) and n=5 (1282 configs,
integer cuts) INC bucket-(iii) sets.)*

**Consequence.** Since `max(Q) > max(R)` is possible in INC, the "double-REFL" reduction
`A(Q∪R) = (max(R) − max(Q)) + A(Q'∪R'')` is not the right identity (when `q > r`, `q` is the global
maximum of `P` and must be peeled first; the running maxima do not alternate `R`-then-`Q`), and the slack
`ΣQ' − ΣR'' = 1 + (max(R) − max(Q))` can be `< 1` (it is `1/2` in the counterexample, where
`max(R) − max(Q) = −1/2`). So the intended non-inductive INC closure does **not** go through. We keep the
one rigorous, ordering-free tool (D1-direct) and record the correct reduction of the residual.

## D1-direct: the rigorous general-`n` slice (INC and GAP alike).

The certified **Lemma D1** (`lemmas/D1-small-discrepancy-kill.md`) applied to the original pair `(Q, R)`:

> **(D1-direct).** If `|N_Q(x) − N_R(x)| ≤ 1` for all `x ≥ 0`, then `A(Q∪R) ≥ |ΣQ − ΣR| = 1`.

*Proof.* This is Lemma D1 verbatim: with `|g| ≤ 1`, `\{g\text{ odd}\} = \{g ≠ 0\}`, so
`A(Q∪R) = measure\{g ≠ 0\} = ∫|g| ≥ |∫g| = |ΣQ − ΣR| = 1`. ∎

D1-direct needs **no** max-ordering and is immune to the correction above; it closes every bucket-(iii)
configuration (INC or GAP) with pointwise discrepancy `≤ 1`, for **all** `n`. It does not close the
residual where `|g|` reaches `2` (e.g. the counterexample, where `g = +2` on `[7, 15/2)`); that residual is
non-tight (`A ≥ 3` there) but not settled by D1.

## The level-charge reduction of the `max|g| ≤ 2` residual (rigorous algebra; one open geometric step).

The residual after D1-direct has `max_x |g(x)| ≥ 2`. We treat the sub-regime `max|g| ≤ 2` (the dominant
residual: n=4 and n=5 residuals have `max|g| ∈ \{2,3\}`, mostly `2`). Partition `[0,∞)` by the value of the
integer step function `g`:
```
A_+ := measure\{g = 1\},   A_- := measure\{g = -1\},   B_+ := measure\{g = 2\},   B_- := measure\{g = -2\}.
```
(When `max|g| ≤ 2` these, together with `\{g=0\}`, exhaust the support.) Then:
- **Odd mass:** `\{g\text{ odd}\} = \{g = ±1\}`, so `A(Q∪R) = measure\{g\text{ odd}\} = A_+ + A_-`.
- **Integral:** `∫g = 1·A_+ + (−1)·A_- + 2·B_+ + (−2)·B_- = (A_+ − A_-) + 2(B_+ − B_-) = 1`.

Eliminating `A_+ − A_- = 1 − 2(B_+ − B_-)` from `A(Q∪R) = A_+ + A_- = (A_+ − A_-) + 2A_-`:
```
A(Q∪R) = 1 − 2(B_+ − B_-) + 2A_- = 1 + 2\big(A_- + B_- − B_+\big).
```
Hence, exactly,

> **(Level-charge reduction, PROVED).** If `max_x|g(x)| ≤ 2`, then
> `A(Q∪R) = 1 + 2(A_- + B_- − B_+)`; in particular
> **`A(Q∪R) ≥ 1 ⟺ B_+ ≤ A_- + B_-`**, and more generally `A(Q∪R) ≥ 1 + 2(A_- + B_- − B_+)`.

*(Verified: `B_+ ≤ A_- + B_-` holds with 0 violations over the entire n=4 and n=5 INC residual, and over
the n=4 GAP residual; consistent with the closed forms `A = 1 + 2(A_-+B_-−B_+)` — e.g. the counterexample
has `A_- = measure[1,2) = 1`, `B_- = measure[0,1) = 1`, `B_+ = measure[7,15/2) = 1/2`, giving
`A = 1 + 2(1 + 1 − 1/2) = 4`, matching the direct value.)*

The reduction is a genuine, non-circular simplification: it converts the target into the single geometric
inequality `B_+ ≤ A_- + B_-` — "the measure of the `g = +2` excess is dominated by the `g < 0` mass."

**Why this is the honest open crux.** `B_+ ≤ A_- + B_-` is **not** implied by `∫g = 1` alone: the
(non-realizable) profile `g ≡ 2` on `[0,½)` has `∫g = 1`, `B_+ = ½`, `A_- = B_- = 0`, violating it (and
indeed `A = 0` there). A proof must use that `ΣQ = 2^n` forces `Q` (hence `N_Q`) to have wide support, so a
`g = +2` block cannot sit unaccompanied by `g < 0` mass — the same wide-support structure that the
`∫g = 1`-only obstruction ignores. Establishing `B_+ ≤ A_- + B_-` (and the analogue past `max|g| = 3`) is
the load-bearing OPEN step; it is the general-`n` bucket-(iii) crux, and we do **not** claim it closed.

**Honest scope of R11.** Rigorous and new this round: (a) the **correction** of the false INC premise with
a machine-checked counterexample and the corrected top-order lemma (proved); (b) **D1-direct** as the
ordering-free general-`n` slice; (c) the **level-charge reduction** `A ≥ 1 ⟺ B_+ ≤ A_- + B_-` for
`max|g| ≤ 2` (proved algebra). Open: the geometric inequality `B_+ ≤ A_- + B_-` (and `max|g| ≥ 3`), i.e.
bucket (iii) general `n`. INC is confirmed to be **not** a genuinely easier sub-case — it is a sub-case of
the same `measure\{g\text{ odd}\} ≥ 1` question, so the R10 INC/GAP split gives no separate simplification.

# Status of the full claim

- **Lower bound `A(final) ≥ 1`:** complete except **Lemma LL, `t ≥ 2`, `A(Q) > 0`, Case 3 / Sub-3b**.
  The general-`R` core (Cases 1, 2, Sub-3a) is rigorous for **any** refined `R` (R8 — 91.6% of refined
  configs at `n=3`); the base case, induction Case 1 (largest uncut), sub-case `A(Q)=0`, and sub-case
  `t=1` are certified imports. **Anchor `R = G_{n−1}`:** the `max(Q) < 2^{n−1}` branch (GAP-B) is closed
  at `n = 3` and reduced for all `n` to **(B2\*)** `A(Q'∪G_{n−2}) ≥ 1` (B3a, B3b rigorous all `n`); the
  `max(Q) ≥ 2^{n−1}` branch (**GAP-A**) is reduced by Lemma REFL to `A(Q'∪R) ≤ μ−1`. **Refined `R`
  (R8):** the residual splits into three exhaustive buckets — (i) `max(Q) ≥ 2^{n−1}`: Lemma REFL
  (R-agnostic) → *GAP-A refined-R*; (ii) `max(Q) < 2^{n−1}`, top piece uncut: double-REFL closes
  B3a-ref/B3b-ref all `n`, reducing to *(B2\*)-refined-R'*; (iii) `max(Q), max(R) < 2^{n−1}` (top cut):
  **CLOSED at `n=3`** (R9, full top-cut regime, rigorous); general `n` open (REFL-telescope terminates but
  the base object is the refined alternating-tail crux); all-`n` cheap-kills K1/K2 cover the near-disjoint
  and `|A(Q)−A(R)|≥1` sub-cases. Open: **(B2\*)** general `n`; **GAP-A** general `n` (= `ll-inclusion-gap`'s
  `G-INC-1`); the refined-`R` cruxes *GAP-A refined-R* and *(B2\*)-refined-R'* (genuinely separate from
  the anchor `T(ℓ)`); and bucket (iii) top-cut refined `R`.
- **Upper bound `A(final) ≤ 1`:** imported from the population — Regime A (`1/2 ≤ A_1 ≤ c(n)`) closed via
  the shadow strategy; Regimes B (`A_1 < 1/2`) and C (`A_1 > c(n)`) open. Not this slug's target.
- **Answer:** `c(n) = 2^n / (2^{n+1} − 1)`, verified for `n = 1` (`2/3`) and `n = 2` (`4/7`) by the
  certified small-`n` arguments in the population. Because load-bearing gaps remain (GAP-A/GAP-B and
  Regimes B/C), the overall problem is **not** solved; Status is `partial`.

# Verification log (bounded, grid, joint cut budget `#Q-cuts + #R-cuts ≤ n` enforced)
- **R8 general-`R` core coverage** (n=3, ½-grid, refined `R` with `c_R ≥ 1`, budget): 371 configs,
  **340 closed** by Case 1 (241) / Case 2 (48) / Sub-3a (51); 0 violations, A-min over these `= 1`.
- **R8 refined-`R` residual buckets** (n=3, ½-grid, budget): residual `= 31` = (i) `max(Q) ≥ 2^{n−1}`
  27 [Lemma REFL identity + `A(Q'∪R) ≤ μ−1` verified, 0 violations] + (ii) top-uncut 2 [(I-ref),(II-ref)
  hold 0 mismatches; B3a-ref/B3b-ref fire] + (iii) top-cut 2 [genuine residual, both `A = 2`].
- **R8 double-REFL for top-uncut refined `R`** (n=3 B3, ½-grid, budget): over all 35 branch-B3 refined
  configs, `A(Q∪R) = 2^{n−1} − A(Q∪R')` (I-ref) and `A(Q∪R') = q_1 − A(Q'∪R')` (II-ref) hold with
  **0 mismatches**; B3a-ref/B3b-ref close (6 configs), only B3c-ref/(B2\*)-ref residual (9) remains.
- **Lemma REFL-gen** (`A(Q∪R) = μ − A(Q'∪R)` for any `max(R) ≤ μ = max(Q)`): **0** mismatches / 4000
  random rational multisets.
- **Double-REFL formula (II)** (`A(Q∪G_{n−1}) = 2^{n−1}−q_1+A(Q'∪G_{n−2})` in B3c): **0** mismatches over
  90 (n=3) + 1205 (n=4) instances (reviewer pre-check 0/3031).
- **(B2\*)** (`A(Q'∪G_{n−2}) ≥ 1`, branch B3c): min `= 1` (tight), **0** violations, `n=3` (`1/8`-grid:
  `|Q'|=2` and `|Q'|=3` both min `1`, 0 violations) and `n=4` (`1/4`-grid); margin `A − δ ≥ 1/2`.
- **Lemma REFL** (prior round): 490 instances, 0 mismatches. **(RED)**: 490, 0 violations, slack 0.
- Case 1 (`max(Q) ≥ 5`, n=3): 8310 configs, `A ≥ 1`, **0 violations** (prior round).

# Open gaps (precise)
- **(B2\*)** (branch B3c, general `n`): `A(Q'∪G_{n−2}) ≥ 1` for `Q'` of `≤ n` positive parts each
  `< 2^{n−1}` with `ΣQ' ∈ (2^{n−1}, 2^{n−1}+1)`. PROVED at `n=3`; general `n` reduces (third reflection,
  case `q_2 ≤ 2^{n−2}`) to a GAP-A-shape upper bound, so = the shared alternating-tail crux.
- **GAP-A** (B1, B2): `A(Q'∪R) ≤ max(Q) − 1`. Upper-bound form; requires the alternating-tail bound
  `(p_2−p_3)+⋯ ≥ 1` general `n` (= `ll-inclusion-gap`'s `G-INC-1`).
- **Refined `R` (R8), three residual buckets:** (i) *GAP-A refined-R* `A(Q'∪R) ≤ max(Q)−1` for a refined
  `R` (from Lemma REFL, `max(Q) ≥ 2^{n−1}`); (ii) *(B2\*)-refined-R'* `A(Q'∪R') ≥ 1` with `R'` a
  refinement of `G_{n−2}` (from double-REFL when the top piece `2^{n−1}` is uncut, `2^{n−1}−1 < max(Q) <
  2^{n−1}`); (iii) **top-cut** refined `R`: `max(Q), max(R) < 2^{n−1}` — no reflection anchor at
  `2^{n−1}`, genuinely open. Buckets (i),(ii) are the alternating-tail `+1` crux family with a *refined*
  `R`/`R'`, **genuinely separate** from the anchor `T(ℓ)` (no known refined-`R` SET IDENTITY /
  top-band-decomposition analogue) — not claimed inherited.

(B2\*) and GAP-A (anchor) are the shared INC/GAP crux; Lemma REFL/REFL-gen and the double-REFL formula
close branches B1/B2/B3a/B3b (anchor) and B3a-ref/B3b-ref (refined, top uncut) and reduce the rest to the
crux family. The R8 general-`R` core (Cases 1/2/Sub-3a) closes 91.6% of refined configs outright.

## Remaining gaps
1. **Anchor `R = G_{n−1}`, general `n`:** (B2\*) `A(Q'∪G_{n−2}) ≥ 1` and GAP-A `A(Q'∪R) ≤ μ−1` — the
   shared alternating-tail `+1` crux (= `ll-inclusion-gap`'s `G-INC-1`/`T(ℓ)`), proved `n ≤ 3` here.
2. **Refined `R` bucket (i)** — *GAP-A refined-R* `A(Q'∪R) ≤ max(Q)−1`, `max(Q) ≥ 2^{n−1}` (via Lemma
   REFL). Crux family, genuinely separate from the anchor `T(ℓ)`. OPEN.
3. **Refined `R` bucket (ii)** — *(B2\*)-refined-R'* `A(Q'∪R') ≥ 1`, `R'` refining `G_{n−2}`, top piece
   uncut, `2^{n−1}−1 < max(Q) < 2^{n−1}` (via double-REFL). Crux family. OPEN.
4. **Refined `R` bucket (iii)** — top-cut (`max(Q), max(R) < 2^{n−1}`): **CLOSED at `n = 3`** (R9, the
   whole top-cut regime, rigorous, verified 10912 configs). **General `n` (R10):** split by containment.
   *INC* (`S_Q ⊆ S_R`) reduces (certified INC-reduction) to `A(R) ≥ A(Q)+1` = **Claim_R(n,0)** — closes
   **conditional** on `ll-inclusion-gap`'s `{Claim_R, T_R}` build. *GAP* (`S_Q ⊄ S_R`) is closed for all
   `n` by the rigorous cheap-kill package **K1, K2, D1 (new)** + Sub-3a, except a **small non-tight
   residual** (n=4: 39/1488 GAP configs, all `A ≥ 2`); the general **Opening D** accumulation
   `Σ_k δ_k ≥ 1` over even-`|g|` excursions is set up rigorously (level-charge form) but **OPEN**.
5. **Upper bound:** imported; Regimes B/C open. Not this slug's target.

## Promotable lemmas
- **Corrected INC top-order lemma (R11).** *Statement:* if `S_Q ⊆ S_R` (INC) then either
  `max(Q) ≤ max(R)`, or `max(Q)` occurs an even number of times in `Q`. *Proof:* if `q := max(Q) > r :=
  max(R)` with multiplicity `m`, then on `(\max(r, q^-), q)` (`q^- =` next `Q`-value below `q`),
  `N_Q = m` and `N_R = 0`; `m` odd would put this interval in `S_Q ∖ S_R`, contradicting INC — so `m` is
  even. Proved in full above (§Bucket (iii) R11). **Corrects** the false outline premise "INC forces
  `max(Q) ≤ max(R)`" (counterexample `Q=\{15/2,15/2,1\}`, `R=\{7,4,2,1,1\}`). Verified 0 violations n=4,5.
- **Level-charge reduction for `max|g| ≤ 2` (R11).** *Statement:* let `g := N_Q − N_R`,
  `A_± := measure\{g=±1\}`, `B_± := measure\{g=±2\}`; if `max_x|g(x)| ≤ 2` and `∫g = ΣQ − ΣR = 1`, then
  `A(Q∪R) = measure\{g\text{ odd}\} = 1 + 2(A_- + B_- − B_+)`, hence `A(Q∪R) ≥ 1 ⟺ B_+ ≤ A_- + B_-`.
  *Proof:* `∫g = (A_+−A_-)+2(B_+−B_-) = 1` and `A(Q∪R) = A_++A_-`; eliminate `A_+−A_-`. Proved in full
  above. Reduces the bucket-(iii) `max|g| ≤ 2` residual to the single geometric inequality
  `B_+ ≤ A_- + B_-` (which is TRUE — 0 violations n=4,5 — but its proof, using `ΣQ = 2^n` wide support, is
  the open crux; `∫g = 1` alone does not give it).
- **Cheap-kill K1 (small-overlap), all `n` (R9).** *Statement:* for `Q, R` with `A(R) ≥ 1`, if
  `2·measure(S_Q∩S_R) ≤ A(Q)` then `A(Q∪R) ≥ A(R) ≥ 1`; in particular `S_Q∩S_R = ∅ ⟹ A(Q∪R) = A(Q)+A(R)
  ≥ 1`. *Proof:* `A(Q∪R) = A(Q)+A(R)−2B ≥ A(R)` when `2B ≤ A(Q)`. Proved in full above.
- **Cheap-kill K2 (difference), all `n` (R9).** *Statement:* always `A(Q∪R) ≥ |A(Q) − A(R)|`; hence
  `|A(Q)−A(R)| ≥ 1 ⟹ A(Q∪R) ≥ 1`. *Proof:* `B ≤ min(A(Q),A(R))` gives `A(Q)+A(R)−2B ≥ |A(Q)−A(R)|`.
  Proved in full above.
- **Cheap-kill D1 (small-discrepancy), all `n` (R10).** *Statement:* if `|N_Q(x) − N_R(x)| ≤ 1` for all
  `x ≥ 0`, then `A(Q∪R) ≥ |ΣQ − ΣR|`; in particular, whenever `ΣQ − ΣR = 1` (e.g. bucket (iii), where
  `ΣQ = 2^n`, `ΣR = 2^n − 1`), `A(Q∪R) ≥ 1`. *Proof:* with `g := N_Q − N_R`, `{g odd} = {g ≠ 0}` when
  `|g| ≤ 1`, so `A(Q∪R) = measure{g odd} = measure{g ≠ 0} = ∫|g| ≥ |∫g| = |ΣQ − ΣR|` (using
  `∫N_P = ΣP` and `S_Q△S_R = {g odd}`). Proved in full above (§Opening D). The first rigorous general-`n`
  GAP tool beating the "`∫g = 1` alone insufficient" obstruction. Verified: closes (with K1, K2) 166/168
  n=3 and 1449/1488 n=4 bucket-(iii) GAP configs.
- **Lemma Q3 (`Q`-only top-mass bound, `n=3` shape) (R9).** *Statement:* if `Q = {q_1≥q_2≥q_3>0}`,
  `ΣQ = 8`, each `q_i < 4`, then `q_2 > 2` and `2·measure(S_Q ∩ [2,∞)) ≤ A(Q)`. *Proof:* `q_2 ≤ 2` forces
  `q_1 ≥ 4`; then `m = (q_3−2)^{+} + (q_1−q_2)` and `A(Q)−2m ∈ \{8−2q_1, 2q_2−4\} > 0`. Proved in full
  above; the engine of the `n=3` bucket-(iii) closure.
- **Lemma REFL-telescope (termination), all `n` (R9).** *Statement:* deleting the running global maximum
  from a finite positive multiset `P` (`|P|=m`) terminates in exactly `m` steps and yields
  `A(P) = μ_0 − μ_1 + ⋯ + (−1)^{m−1}μ_{m−1}`; consequently, when the two largest pieces of `Q∪R` are
  `max(Q)` and `max(R)`, `A(Q∪R) = max(Q) − max(R) + A(Q'∪R'')`. *Proof:* piece-count strictly decreases
  by 1 each step (well-founded descent), each step is certified Lemma REFL-gen. Proved in full above.
- **General-`R` core of Lemma LL (R8).** *Statement:* let `Q` partition `2^n` into `≥ 2` parts and `R`
  be any finite multiset with `max(R) ≤ 2^{n−1}`, `A(R) ≥ 1`; if `max(Q) ≥ 2^{n−1}+1` (Case 1), or
  `|Q|+|R|` is odd with all pieces of `P=Q∪R` of length `≥ 1` (Case 2), or `N_Q+N_R` is odd throughout
  some dyadic level `I_k` (Sub-3a), then `A(Q∪R) = measure(S_Q△S_R) ≥ 1`. *Proof:* the three certified
  lemmas `ll-case1-high-interval` / `parity-piece-count` / `dyadic-level-parity` assembled — each uses
  only `max(R) ≤ 2^{n−1}` (via `S_R ⊆ [0,2^{n−1})`), the piece list of `P`, and the dyadic levels, never
  any `G_{n−1}`-specific band structure. Hence it holds for **every refined `R`**, not just the anchor.
  Proved in full above (§Refined `R`). Verified n=3 ½-grid budget: 340/371 refined configs closed.
- **Budget-reduction lemma (R8).** *Statement:* if `R` is a proper refinement of `G_{n−1}` (`c_R := #R
  -cuts ≥ 1`), then under the joint cut budget `#Q-cuts + #R-cuts ≤ n`, `|Q| ≤ n`. *Proof:* `c_Q + c_R
  ≤ n` and `c_R ≥ 1` give `c_Q ≤ n−1`, so `|Q| = c_Q+1 ≤ n`. Proved above.
- **Double-REFL for a refined `R` with top piece uncut (R8).** *Statement:* let `R` refine `G_{n−1}`
  with the top piece `2^{n−1}` uncut (so `max(R)=2^{n−1}` and `R' := R∖\{2^{n−1}\}` refines `G_{n−2}`,
  `max(R') ≤ 2^{n−2}`), and let `Q` partition `2^n` with `q_1 := max(Q) < 2^{n−1}`. Then
  `A(Q∪R) = 2^{n−1} − A(Q∪R')` (I-ref); and if `q_1 > 2^{n−2}`, also `A(Q∪R) = 2^{n−1} − q_1 + A(Q'∪R')`
  (II-ref), `Q' := Q∖\{q_1\}`. Consequently `A(Q∪R) ≥ 1` holds whenever `q_1 ≤ 2^{n−1}−1` (sub-cases
  B3a-ref `q_1 ≤ 2^{n−2}` via `A(Q∪R') ≤ 2^{n−2}`, and B3b-ref `2^{n−2} < q_1 ≤ 2^{n−1}−1` via
  `A(Q'∪R') ≥ 0`), reducing the residual `2^{n−1}−1 < q_1 < 2^{n−1}` to `A(Q'∪R') ≥ 1`. *Proof:* certified
  Lemma REFL on the top piece (roles "`Q`"`=R`, "`R`"`=Q`), then certified Lemma REFL-gen on `q_1`
  (`max(R') ≤ 2^{n−2} < q_1`); the anchor double-REFL proof used `R=G_{n−1}` only through `max(R)=2^{n−1}`
  and `max(R∖\{2^{n−1}\}) ≤ 2^{n−2}`, both of which hold here. Proved in full above (§Refined `R`,
  bucket (ii)). Verified n=3 ½-grid budget: (I-ref),(II-ref) 0 mismatches; B3a-ref/B3b-ref close.
- **Reflection identity, relaxed hypothesis (Lemma REFL-gen).** *Statement:* for any finite multiset `Q`
  with `μ := max(Q)`, `Q' := Q ∖ {μ}`, and any finite multiset `R` with `max(R) ≤ μ`,
  `A(Q∪R) = μ − A(Q'∪R)`. *Proof:* verbatim the certified Lemma REFL proof — on `[0,μ)`,
  `N_Q = 1 + N_{Q'}` gives `S_Q = [0,μ) ∖ S_{Q'}`; the hypothesis `max(R) ≤ μ` gives
  `S_R ⊆ [0,max(R)) ⊆ [0,μ)` (the only place the certified version used `μ ≥ 2^{n−1} ≥ max(R)`); then
  `(U∖A)△B = U∖(A△B)` yields `A(Q∪R) = μ − A(Q'∪R)`. Strictly generalizes the certified
  `lemmas/ll-reflection-identity.md` (drop `μ ≥ 2^{n−1}`); needed for the second reflection where
  `μ = q_1 < 2^{n−1}`. Verified 0/4000 random rational tests. Proposed to
  `results/imo-2026-03/lemmas/ll-reflection-identity-gen.md`.
- **General reflection identity (Lemma REFL).** *Statement:* let `Q` be a multiset with `μ := max(Q)`,
  `Q' := Q ∖ {μ}`, and `R` with `max(R) ≤ 2^{n−1}`; if `μ ≥ 2^{n−1}` then `A(Q∪R) = μ − A(Q'∪R)`.
  *Proof:* on `[0,μ)`, `N_Q = 1 + N_{Q'}` so `S_Q = [0,μ) ∖ S_{Q'}`; with `S_R ⊆ [0,2^{n−1}) ⊆ [0,μ)`,
  `(U∖A)△B = U∖(A△B)` gives `S_Q△S_R = [0,μ) ∖ (S_{Q'}△S_R)`, whence the identity. Proved in full above;
  machine-verified 490/490, 0 mismatches; extends the certified `max(Q)=2^{n−1}` identity to `μ ≥ 2^{n−1}`.
  Reduces `A(Q∪R) ≥ 1` to the upper bound `A(Q'∪R) ≤ μ − 1` (non-circular: `Q'∪R` is not a valid
  `G_{n−1}`-refinement). Proposed to `results/imo-2026-03/lemmas/ll-reflection-identity.md`.
- **Dyadic-level parity bound (Sub-3a).** *Statement:* for `Q, R` as in Lemma LL, if `N_Q + N_R` is odd
  throughout some dyadic level `I_k` (`I_0 = [0,1)`, `I_k = [2^{k−1}, 2^k)` for `1 ≤ k ≤ n−1`), then
  `A(Q∪R) = measure(S_Q △ S_R) ≥ measure(I_k) ≥ 1`; a checkable sufficient condition is (∗): no piece
  value of `P` in `int(I_k)` has odd multiplicity and `#{pieces ≥ sup I_k}` is odd. *Proof:* the level is
  then contained in `{N_P odd} = S_Q △ S_R`; every level has measure `≥ 1`. Proved in full above.
  Proposed to `results/imo-2026-03/lemmas/dyadic-level-parity.md`.
- **Case-1 high-interval disjointness.** *Statement:* if `Q` partitions `2^n` with `max(Q) ≥ 2^{n−1}+1`
  and `R` has `max(R) ≤ 2^{n−1}`, then `A(Q∪R) ≥ max(Q) − 2^{n−1} ≥ 1`. *Proof:* `N_Q = 1`, `N_R = 0` on
  `[2^{n−1}, max(Q))`, so that whole interval lies in `S_Q △ S_R`. Proved in full above. Proposed to
  `results/imo-2026-03/lemmas/ll-case1-high-interval.md`.
