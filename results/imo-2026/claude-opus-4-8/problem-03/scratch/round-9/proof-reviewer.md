# Proof-reviewer — imo-2026-03, Round 9

Reviewed all three built approaches adversarially: re-derived each load-bearing new lemma from scratch
and re-ran budget-enforced exact-Fraction numeric checks (`/tmp/check1..4.py`, all <20s). No approach
claims `solved`; all three are honest partials with real, verified progress. No decertified/false move
re-imported (checked: no false Structural Lemma, no `max(Q)<2^{n−1}⟹A≥2`, no R3 deterministic cascade,
no SB-monotone route, no re-push of the DONE anchor T(ℓ)). Answer c(n)=2^n/(2^{n+1}−1) unchanged and not
re-litigated.

---

## 1. geometric-selfsimilar — CHANGES REQUESTED (Status: partial)

**Scores:** Correctness 10/10 · Completeness 4/10 (upper bound still open) · Progress: real (frontier
narrowed from "all b≥3" to one pinned budget; one clean lemma certified).

**Lemma AB (μ(X,b)=0 when b≥|X|) — VERIFIED, CERTIFIED** (`lemmas/abundant-budget.md`). Re-derived the
constructive pairing reduction: `≤ k−1` cuts reach `≤ 1` piece, one more midpoint cut zeroes a lone piece,
total `≤ k ≤ b`; all cuts strictly interior to distinct pieces (legal), invisible pairs leave A unchanged
(depends only on the multiset). Numeric: 0/5000 failures (A=0, cuts≤|X|). Corollary AB.1 (tight budget
b=m−1 the only nontrivial case) follows immediately from the budget invariant `|X|≤b+1`. Sound.

**(T) honestly open — no overclaim.** The tight-case reduction to the finite merge-family inequality (T)
is explicitly flagged "verified, not yet analytically proved" (0/9646 exact m=4 gap configs). This is the
whole remaining upper bound. Correctly NOT presented as established.

**Both spec concerns confirmed valid.** (a) Cutting p₁ at offset pⱼ vs p₁−pⱼ yields the *identical*
fragment pair {pⱼ, p₁−pⱼ} and identical A — the outline's "triple pⱼ / odd parity" single-cut distinction
is illusory (it is just Lemma R3). (b) The outline's one-cut m=4→3→R4 mechanism gives `|2max(sub)−Σ'|`,
which exceeds the target on a genuine fraction of near-equal configs (builder: 141/367) — the sub needs
its full budget b−1. Both are legitimate corrections, not evasions.

**Gap (for next round):** the closed-form analytic proof of the tight-case inequality (T) at b=m−1. Now a
concrete bounded 4-variable (m=4) algebraic min-inequality — the most tractable the m≥4 frontier has been.

## 2. ll-inclusion-gap — CHANGES REQUESTED (Status: partial)

**Scores:** Correctness 10/10 · Completeness 5/10 (refined-R lower bound partly open) · Progress: real
(two certified refined-R tools + equal-split closed but for one edge).

**Gen-Decomp (Step 16) — VERIFIED, CERTIFIED** (`lemmas/gen-decomp-refined.md`). Re-derived: Forcing
Lemma + Parity-Condition give (i) h even, (ii) the [0,thr) restriction, (iii) the clean descent
`S_{Q_lo}⊆S_{R_lo}`; the identity is a straight split of `[0,2^{n−1})=[0,thr)⊔I_{n−1}`. Both summands ≥0.
Numeric: 0 failures over budget-valid n=3,4,5 INC configs. This is the correct refined-R engine and uses
NO SET IDENTITY (the anchor tool with no refined-R analogue).

**Lemma L1 (Step 17) — VERIFIED, CERTIFIED** (`lemmas/L1-budget-anchor.md`). Re-derived the m→m−2 strong
induction: bases m=1,2 sound; step splits on h̄ (even) into h̄=0 (deficit_top=2^{m−2}≥1) and h̄≥2
(`|P_lo|≤(m−2)−1` invokes L1 at level m−2, giving M≥1). Descent grounds on m∈{1,2}, well-founded, no ε,
no T-companion. The strict `−1` is genuinely forced by the budget deficit `|P|<m`. Numeric: tight
`max A(P)=A(G_{m−1})−1`, 0 violations for m=2..6 (integer) and 0/9806 random rational configs.

**Spec concern valid:** the outline's step-1 cheap-kill (`f⁺≥f⁻` AND `f⁺=0`) forces no cut (vacuous); the
builder's corrected cheap-kill (`S_Q⊆S_{G_{n−1}}` AND `A(R)≥A(G_{n−1})`, then certified G-INC-1) is honest.

**Gaps (for next round):** G-INC-2e (equal-split edge g=0, h̄≥2, q₁>q₂ — numerically comfortable, not
near-tight); G-INC-2lb (lower-band cut cross-position mutual recursion + unpinned ΣQ_lo — not well-founded
yet); G-INC-2nt (non-equal top cut incl. a<1). An ε/τ `{Claim_R,T_R}` over the joint cut-position family,
now that Gen-Decomp supplies the descent identity, is the suggested route.

## 3. ll-dyadic-symdiff — CHANGES REQUESTED (Status: partial)

**Scores:** Correctness 10/10 · Completeness 5/10 (general-n bucket iii open) · Progress: real (first full
refined-R bucket closed at n=3; three reusable tools certified).

**K1, K2 — VERIFIED, CERTIFIED** (`lemmas/dyadic-cheap-kills.md`). Both are one-line consequences of the
certified merge identity `A(Q∪R)=A(Q)+A(R)−2B`, `B≤min(A(Q),A(R))`. Correct.

**n=3 bucket (iii) closure — VERIFIED.** Budget forces `c_Q=2, c_R=1` exactly (two parts <4 cannot sum to
8, and top piece 4 is cut). Lemma Q3 (`2·measure(S_Q∩[2,∞))≤A(Q)`, from forced q₂>2) re-derived in both
Q3 cases; Regime I algebra `(3−2a)−2(1−a)=1` and the Regime II q₃-trichotomy (all three sub-cases give
`2B≤A(Q)`) check out. Reviewer re-ran the full 1/16-grid: **min A(Q∪R)=1, 0 violations over 10912
configs** (matches the builder). Complete and rigorous for n=3.

**REFL-telescope termination — VERIFIED, CERTIFIED.** Well-founded piece-count descent, each step certified
`ll-reflection-identity-gen` (`max(R)≤μ_i` holds). Correctly flagged HONEST: termination only *recomputes*
A; it does NOT deliver the bottom object `A(Q'∪R'')≥1`. No overclaim — the outline's "termination is the
blocker" framing is correctly rejected in favour of "the base-object bound is the crux."

**Gap (for next round):** general-n bucket (iii) — the refined-R alternating-tail crux for the smaller
system `Q'∪R''` (no 2^{n−1} anchor, no refined SET IDENTITY), open for n≥4. K1/K2 cover the near-disjoint
and `|A(Q)−A(R)|≥1` sub-cases only.

---

## Certified this round (5 new lemma files → 26 total)
`abundant-budget`, `gen-decomp-refined`, `L1-budget-anchor`, `dyadic-cheap-kills` (K1+K2+REFL-telescope).
(Q3 folded into the n=3 closure, internal.)

## Goal Progress (for Eval History)
- Status: **partial** (unchanged; problem NOT solved). Ranking order unchanged:
  geometric-selfsimilar 1685.7 > ll-inclusion-gap 1619.9 > ll-dyadic-symdiff 1516.6 >
  alternating-sum-value 1398.9 > extremal-smoothing 1279.0.
- UPPER BOUND (geometric): m≥4 frontier narrowed to the single tight budget b=m−1 (Lemma AB certified);
  whole UB residual = the finite merge-family inequality (T), verified 0/9646 but analytically open.
- LOWER BOUND (ll-inclusion-gap): refined-R engine Gen-Decomp + budget anchor L1 certified; equal-split
  top cut closed all n≥4 except edge G-INC-2e. Open: G-INC-2lb (cross-position recursion), G-INC-2nt.
- LOWER BOUND (ll-dyadic-symdiff): n=3 bucket (iii) fully closed; K1/K2/REFL-telescope certified;
  general-n bucket (iii) refined alternating-tail crux open.
- All three verdicts: **CHANGES REQUESTED** (honest partials, no overclaim, no decertified move reused).
