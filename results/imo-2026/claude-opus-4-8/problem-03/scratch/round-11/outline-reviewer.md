# Outline Review — imo-2026-03, Round 11

Reviewed the outliner's 3-approach field (advance geometric-selfsimilar; revise ll-inclusion-gap;
advance ll-dyadic-symdiff). All three are whole-attempt advances of the three live leaders, each
carrying a concrete new opening. I independently verified the three load-bearing points flagged in
the dispatch. All three PASS.

---

## geometric-selfsimilar (advance) — VERDICT: APPROVE

**Load-bearing check — the Σ′ arithmetic correction: VERIFIED CORRECT for all m.**
Condition (2) of the residual gap case is `p₂ < τ/2 = 2^{m−2}·t` (confirmed against the certified
`T4-tight-m4.md`, which states for m=4 exactly `p₂ < τ/2 = 4Σ/15 = 2^{2}·t`, so τ = 8t = 2^{m−1}t).
The outliner's correction is right; the explorer's line-137 "critical observation" (that the Σ′-bound
fails for general m) was based on **misquoting condition (2) as `p₂ < 2^{m−1}t`** (that is the scale of
condition (1), not (2)). With the correct `p₂ < 2^{m−2}t`:
`Σ′ = Σ − 2p₂ > (2^m−1)t − 2·2^{m−2}t = (2^m−1)t − 2^{m−1}t = (2^{m−1}−1)t`, since
`2^m − 2^{m−1} − 1 = 2^{m−1} − 1`. Exact for every m. I re-verified symbolically m=3..8 (all match).
So after the universal `p₁@p₂` cut the subproblem sum `Σ′ > (2^{m−1}−1)t` strictly, always. The
induction is NOT blocked here.

**Caveat the builder MUST keep in view (the outliner already flags it, Watch-out (i)):** the Σ′-bound is
only a *sanity* condition — it says the subproblem is a valid gap-case with enough sum. It does NOT
close the step. The subproblem's own tight threshold is `Σ′/(2^{m−1}−1) > t`, so the certified
self-similar `T_{m−1}` applied at the subproblem's own threshold gives `μ ≤ Σ′/(2^{m−1}−1) > t` — too
weak (correctly forbidden). The real open content is the **threshold-invariant descent**: proving the
STRONGER `T_{m−1}-at-t` on the subproblem, which requires **condition inheritance** (does
`{d₁,p₃,…,p_m}` inherit (1′) `q₁≤Σ′/2` and (2′) `q₂<2^{m−3}t` at threshold t, or else fall into an
easy case closed by Lemma MK?). This is honestly open, not circular, and is THE hard step. Good.

**Lemma MK** (`μ(k,k−1) ≤ min`): mechanism stated and sound — halve p₁ into an invisible equal pair
(certified R1), drop to k−1 pieces with k−2 cuts, induct; bases k=1,2 check. Must be certified as a
standalone tool (flagged as an open gap). No objection.

**Issues to close while building** (CHANGES-level, do NOT block the build):
- Certify Lemma MK.
- The hard step is condition-inheritance of (1′)/(2′) at threshold t; where a subproblem condition
  fails it must instead land in an easy case (Lemma MK). Prove this dichotomy — it is the whole gap.
- Sub-B (d_m > d₁) is genuinely non-vacuous for m≥5 — do NOT mimic the m=4 vacuousness argument.
- Keep Opening 3 (explicit (u,v) with A=min(v,u−v)≤t) as the base-of-recursion fallback if
  condition-inheritance stalls at the 2-effective-piece hard case.
- Do NOT overclaim: the whole UB is NOT closed until the general-m descent + Lemma MK are proven.

This remains the field leader and closest to a solve (UB = just the m≥5 case of (T); n=3 UB already
rigorous). Build it.

---

## ll-inclusion-gap (revise) — VERDICT: APPROVE

**Load-bearing check — is the parametric family `R_k = {a}∪G_{k−1}` (a<1) genuinely distinct from the
REFUTED abstract {Claim_R,T_R} class? YES, genuinely distinct.**
The R10 refutation had two prongs: (O1) `h_{R_lo}` parity breaks for LOWER-BAND cuts at
`k₀∈{n−4,n−3}` (witness {1,2,2,2,8,16,32}); and Claim_R is FALSE for arbitrary non-refinement R
(R={1,3,3}). For the fixed-`a<1` TOP-cut family this specific obstruction provably does NOT fire:
the cut only splits the top piece into `{2^{n−1}−a, a}`; the tiny `a<1` never reaches any descent
threshold `2^{k−4}` (for k≥6; k=4,5 direct), so the G-structure below is preserved and
`h_{R_lo} = #{2^{k−3},2^{k−4}} = 2` (even) at EVERY level, and `R_lo = {a}∪G_{k−3} = R_{k−2}` — the
same family two levels down, descent-closed. This is a *specific descent-closed parametric family*,
not the abstract structure-free class, and the false witnesses (R={1,3,3}, the lower-band witness) are
not in it. Per my standing rule (re-approve a cut route once its exact blocking obstruction is
certified-resolved): the O1 parity break is provably inapplicable to this family, so this is legitimate,
not a re-tread of the refuted route.

**Issues to close / honest scope (CHANGES-level, does NOT block the build):**
- The `a<1` mutual induction {Claim_a(k), T_a(k)} claims arithmetic "IDENTICAL to the anchor". The
  builder MUST hand-trace that it actually cycles with the extra piece `a` present in `S_{R_lo}`
  (deficit_top = a_val′+b, ε′ = ε+a_val′−b, h∈{0,2}), exactly as the certified
  `t-ell-mutual-induction` was hand-verified — do not assume transfer. Bases k=4,5 are open.
- **The `a≥1` sub-branch is the genuine hard residual** — there `h_{R_lo}` CAN go odd, so the family
  is NOT guaranteed descent-closed. Treat it as an honest open gap, NOT as covered. Do NOT claim the
  WHOLE lower bound is solved.
- G-INC-2lb (lower-band): Opening D's clean h=2 descent is sound (top two pieces always uncut).
- G-INC-2e general n (>6) and G-GAP (non-containment) remain open.
- Forbidden (rules): do NOT re-open the abstract {Claim_R,T_R} class; do NOT use generalized-L1 without
  fixed-R structure (2880 viol).

Build it — but the honest deliverable this round is the `a<1` family + lower-band, NOT the full LB.

---

## ll-dyadic-symdiff (advance) — VERDICT: APPROVE

**Load-bearing check 1 — is the containment-base closure genuinely NON-inductive (no reliance on the
refuted mutual induction)? YES.** The INC-base argument uses only: (a) INC forces `max(Q)≤max(R)`
(clean point-parity argument, no induction); (b) double-REFL via certified REFL / REFL-gen; (c)
certified D1; (d) certified Sub-3a for the residual. None is the refuted {Claim_R,T_R}. This is exactly
the shared-gap bypass CLAUDE.md wants. The explorer's report self-corrected the reduction (its first
pass wrongly wrote `A(Q∪R)=q−A(Q'∪R')` and "ΣQ′−ΣR″≥1 ⟹ A≥1"; the CORRECTED and correct relation is
`A(Q∪R) = (r−q) + A(Q'∪R')`, with D1 supplying `A(Q'∪R') ≥ 1+(r−q)`, total `≥ 1+2(r−q) ≥ 1`). The
outliner absorbed the correction and explicitly warns against the wrong version. Good.

**Load-bearing check 2 — is the double-REFL precondition `q≥max(R')` checked? It is FLAGGED and is
genuinely load-bearing — I confirmed it numerically.** The reduction is really the trivial
"peel-the-global-max" identity `A(whole)=max − A(rest)`. Peeling `r=max(R)` is always valid (r is the
global max since q≤r). Peeling `q` next is valid ONLY if `q≥max(R')`; otherwise the next max is R's
second piece `r₂>q` and one must keep peeling R. I tested ~3000 INC-shaped configs: the identity
`A(Q∪R)=(r−q)+A(Q'∪R')` holds whenever `q≥max(R')` and BREAKS in cases where it fails. INC does NOT
force `q≥max(R')` (for x∈(q,r₂), N_Q=0 even and N_R=2 even — consistent with S_Q⊆S_R), so the
precondition can genuinely fail. This is NOT fatal: when `r₂>q` the builder continues the certified
REFL-telescope (peel r₂ from R next), whose termination is already certified. The builder MUST branch
on this — treat `q≥max(R')` failing as the "continue peeling R" case, not as an oversight.

**Issues to close (CHANGES-level, does NOT block the build):**
- Handle the `q<max(R')` branch via the certified REFL-telescope (peel further R pieces).
- General-n Sub-3a firing (max|g|≥2 ⟹ max(Q)=max(R)=μ∈(2^{n−2}+1,2^{n−1}), so I_{n−1} has one piece,
  measure μ−2^{n−2}≥1): proved n=4, conjectured n≥5 — must be proven for general n.
- GAP residual A≥1 via Opening-D charge/budget: honestly OPEN (empirically A≥2). Do NOT claim
  "∫g=1 ⟹ A≥1" (FALSE), and do NOT re-import "max(Q)<2^{n−1} ⟹ A≥2" (FALSE) or K2 for INC (circular).

Build it — the non-inductive INC base is the clean new traction; GAP residual stays honest-open.

---

## Ranking (updated this round; stale flags cleared)

geometric-selfsimilar 1730.7 > ll-inclusion-gap 1631.2 > ll-dyadic-symdiff 1507.6 >
alternating-sum-value 1384.7 > extremal-smoothing 1245.8.

Rationale: geometric-selfsimilar is closest to a solve (UB = just m≥5; n=3 UB rigorous) and its advance
rests on a verified arithmetic correction — it wins over both LB routes. ll-inclusion-gap keeps its edge
over ll-dyadic (deeper accumulated progress + a concrete descent-closed a<1 family), though ll-dyadic's
non-inductive INC base is the lower-risk opening this round; both beat the two dormant approaches
convincingly. alternating-sum-value > extremal-smoothing (extremal's S1 stuck 5+ rounds, last-placed).
No new slugs to register (all three live leaders already in the population); no copy requested.

## Notes for the orchestrator
- All three are legitimate advances with distinct routes covering the whole remaining frontier (UB m≥5;
  refined-R LB via containment/parametric-family and via double-REFL non-inductive base). No RETHINK.
- Every verdict is APPROVE with build-time CHANGES to close; each builder owns its own file, parallel
  builds do not collide.

build set: geometric-selfsimilar, ll-inclusion-gap, ll-dyadic-symdiff
