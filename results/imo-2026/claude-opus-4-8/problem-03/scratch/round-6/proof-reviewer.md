# Proof Review — imo-2026-03, Round 6

Reviewed 3 built approaches. All are honest partials with genuine new rigorous progress; none is a
complete solution. **All three → CHANGES REQUESTED (Status: partial).** No approach broke; no RETHINK.
Enforced the joint cut budget (#Q-cuts + #R-cuts ≤ n) in every numeric check.

Independent verifications I ran (bounded, exact Fractions):
- **Lemma REFL** `A(Q∪R) = max(Q) − A(Q'∪R)` for max(Q)≥2^{n−1}: 0 mismatches / 2282 n=3 instances.
- **R2/R3 arithmetic** equivalences: 0 failures / 20000 random (Σ,b,p₁,q). **Equal-pair invisibility**
  `A(Y∪{w,w})=A(Y)`: 0/5000. **R3 leftover identity** (q<p₁): 0/19264 (q=p₁ correctly excluded → R1).
- **n=3 INC base case** `A(Q)≤2` over all 52 INC configs partitioning 8: max exactly 2, 0 violations.
  **Parity-Condition** (h even; N_Q even on (1,2)): 0 failures.
- **Top-band decomposition identity** at n=4 (R=G_3): identity holds 0 failures, h even, both terms ≥0,
  min(A(G_3)−A(Q))=1.

---

## ll-inclusion-gap — CHANGES REQUESTED (Status: partial)
Scores: Correctness 9/10 · Rigor 8/10 · Progress 8/10.

**Verified correct and rigorous:**
- **Parity-Condition Lemma** (Step 3) — a genuine, correct replacement for the R5-decertified FALSE
  Structural Lemma. Proof (contrapositive of S_Q⊆S_R) is clean; (P1)/(P2)/(P3) all follow. It admits the
  even-multiplicity interior pair {3/2,3/2} that killed the old lemma. **CERTIFIED**
  (`lemmas/parity-condition-inc.md`).
- **Complete n=3 INC base case for R=G_2** (Step 7) — casework m∈{2,4}, and within m=2 the sub-cases
  e=2 (equal interior pair) and e=0 (ℓ=0,1,2) is exhaustive and each branch correctly gives A(Q)≤2. This
  FIXES the R5 hole. Analytic bound `q₁−q₂ ≤ 4−2 = 2` (from Forcing q₁≤4 and m=2 ⇒ q₂≥2) is valid.
- **Top-band decomposition identity** (Step 6) — (a)–(d) re-derived from scratch and confirmed; the
  algebra `A(G_{n−1})=2^{n−1}−A(G_{n−2})` and both non-negativity claims hold. **CERTIFIED**
  (`lemmas/top-band-decomposition.md`).

**Gap (why not solved):** the general-n INC "+1", **G-INC-1** `deficit_top + M ≥ 1`, is OPEN (only
reduced to this scalar inequality). Also **G-INC-2** (refined R general n) and **G-GAP** (non-containment
alignment) open.

**Overclaim to fix (minor, self-qualified):** the "Approaches tried" line and the "Current best" header
say the INC branch is "RIGOROUS AND COMPLETE for n=3 (all R)". It is proven only for **R=G_2**; refined R
at n=3 is only numerically checked (400 instances) — that is exactly the open G-INC-2. The parenthetical
admits this, but the header phrasing should be softened to "R=G_2" not "all R". I corrected the wording in
`current.md`.

## ll-dyadic-symdiff — CHANGES REQUESTED (Status: partial)
Scores: Correctness 9/10 · Rigor 8/10 · Progress 7/10.

**Verified correct and rigorous:**
- **General reflection identity (Lemma REFL)** — the set-theoretic proof (S_Q=[0,μ)∖S_{Q'}, then
  (U∖A)△B=U∖(A△B)) is fully rigorous and I re-derived it independently (0 mismatches/2282). Genuinely
  extends the R5 max(Q)=2^{n−1} identity to the whole band μ≥2^{n−1}. Non-circular (Q'∪R has sum
  2^{n+1}−μ−1, not a valid G_{n−1}-refinement). **CERTIFIED** (`lemmas/ll-reflection-identity.md`).
- **Deleting the FALSE "max(Q)<2^{n−1} ⟹ A≥2" step** is correct — I confirmed the tight witness
  Q={3,3,2}, R={2,2,2,1} (budget 2+1=3=n) gives A(Q∪R)=1 exactly, so B3 is tight and the A≥2 mechanism is
  dead. Honest, sharper record.

**Gap (why not solved):** Sub-3b reduces to **GAP-A** (`A(Q'∪R)≤max(Q)−1`, branches B1,B2) and **GAP-B**
(`A(Q∪R)≥1`, branch B3). Both OPEN. GAP-A is the alternating-tail bound = ll-inclusion-gap's G-INC-1;
GAP-B is the tight max(Q)<2^{n−1} branch.

## geometric-selfsimilar — CHANGES REQUESTED (Status: partial)
Scores: Correctness 9/10 · Rigor 8/10 · Progress 7/10.

**Verified correct and rigorous:**
- **Sum-bound reframe (SB)** `μ(X,b)≤Σ/(2^{b+1}−1)` correctly unifies the whole upper bound (LB config
  Σ=1,b=n gives val≤c(n)). Matches the game (XY distributes ≤n interior cuts).
- **R1/R2/R3 reduction lemmas** — each is an UNCONDITIONAL valid XY strategy bounding μ(X,b) by μ of a
  lex-smaller instance; the parity-invisible equal-pair mechanism and the R2/R3 arithmetic equivalences
  all check out (0 failures). Base case b=0 correct. **CERTIFIED** (`lemmas/sum-bound-reductions.md`).
- **Regime C rigorous opening cut** (R2 halves A₁) genuinely supersedes the unproven "dominant-chop".

**Gap (why not solved):** (SB) is proved only for reduction trees that never reach the **gap case**
(distinct X, p₁<τ, p₂<τ/2). The gap case — subsuming old B2-general and C — is OPEN. The builder honestly
records that partial-shadow does NOT preserve the sum invariant (Σ(R′)/D_{b−j}≤Σ/D_b fails
18/123/315/678 at n=3..6), so a stronger potential than the running sum is needed. Not papered over.

---

## Shared-residual finding (per orchestrator focus)
The two lower-bound routes **do genuinely converge on the same residual**: ll-inclusion-gap's G-INC-1
(`deficit_top+M≥1`) and ll-dyadic-symdiff's GAP-A (`A(Q'∪R)≤max(Q)−1`) are the same alternating-tail
bound `(p₂−p₃)+(p₄−p₅)+⋯≥1` for general n — confirmed by both builders and the outline-reviewer's
independent 574-instance check. This residual is **OPEN in both**. Each route additionally carries one
non-shared open branch (G-INC-2 / refined R; and G-GAP=GAP-B / max(Q)<2^{n−1} alignment). The upper-bound
gap case is a separate open residual owned by geometric-selfsimilar.

## Certifications this round
- `lemmas/ll-reflection-identity.md` (Lemma REFL) — **CERTIFIED**.
- `lemmas/parity-condition-inc.md` (Parity-Condition Lemma) — **CERTIFIED** (replaces the false
  Structural Lemma).
- `lemmas/top-band-decomposition.md` (Top-band decomposition identity) — **CERTIFIED** (the identity;
  the resulting inequality G-INC-1 is NOT closed).
- `lemmas/sum-bound-reductions.md` (R1/R2/R3) — **CERTIFIED** (unconditional reductions; the full (SB)
  is NOT closed — gap case open).
- Odd-index reformulation `A(P)=2·O_P−ΣP` and the n=3-specific base case: correct but not given separate
  files (elementary / subsumed).

## Goal Progress (for Eval History)
Status: **partial** (unchanged flip; genuine new rigorous progress). Ranking (outline-reviewer R6 Elo):
geometric-selfsimilar 1643.3 > ll-inclusion-gap 1545.0 > ll-dyadic-symdiff 1502.4 >
alternating-sum-value 1447.0 > extremal-smoothing 1362.4. All three built slugs recorded **advanced**.
4 new lemmas certified (12 total). Lower bound narrowed to a single shared residual G-INC-1=GAP-A (plus
G-INC-2 refined-R and GAP-B branches); upper bound unified to a single gap case. Both fronts sit on one
open crux each — a shared-gap plateau to challenge next round.
