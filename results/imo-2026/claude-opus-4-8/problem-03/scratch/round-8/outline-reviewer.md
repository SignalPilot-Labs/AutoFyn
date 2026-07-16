# Outline Review — imo-2026-03, Round 8

Field: 3 advances (no new slug). Two explorers (tell, refinedR) independently derived the SAME
closure of T(ℓ); potential explorer supplied the m=3 UB base. I verified the load-bearing algebra
by hand and with bounded checks (D_b identity, m=3 gap bound). All three nominations are sound and
buildable.

---

## ll-inclusion-gap (advance) — VERDICT: APPROVE (highest priority)

Target: full LB via the containment/non-containment split; this round closes the shared anchor
crux T(ℓ) for ALL n by turning the single-claim induction into a mutual {Claim(n,ε), T(n)} induction.

**The mutual induction cycles — verified by hand.** I traced the dependency and arithmetic:
- Notation reconciled between the two explorers: tell's `ε''=ε'+a−b` (ε'=ΣP−2^n∈(−1,0)) equals
  refinedR's `ε'=a−b−τ` (τ=2^n−ΣP). Both give `ΣP_lo=2^{n−2}+ε''`, which I re-derived:
  `ΣP_lo=ΣP−q₁−q₂=ΣP−2^n+a−b`. Consistent. deficit_top=a+b, target `1−τ=1+ε'`.
- **h≥4 impossible for T** (four parts ≥2^{n−2} sum to 2^n>ΣP) — correct, one line. So h∈{0,2}.
- **h=0**: δ_top=0 ⟹ deficit_top=2^{n−2}≥1≥1−τ. Correct (also fills the reviewer-flagged
  unwritten h=0 sub-case of Claim, reachable n≥5).
- **h=2, 2b-i (ε''≥0)**: Claim(n−2,ε'') gives M≥1−ε''; total = (a+b)+(1−ε'') = **1−ε'+2b** (refinedR's
  τ-form `1+2b+τ`) ≥ 1+ε'. ✓ (Tell wrote the intermediate as `1+ε'+2b` — a harmless sign typo; the
  ≥1+ε' conclusion holds under either expression since b≥0 and −ε'>0.)
- **h=2, 2b-ii (ε''<0)**: the critical bound `ε''>−1` is correct — from the 2b hypothesis a+b<1−τ
  and a≥0 we get b<1−τ, so ε''=ε'+a−b>ε'−(1+ε')=−1, placing ΣP_lo∈(2^{n−2}−1,2^{n−2}), exactly
  T(n−2)'s window. T(n−2) ⟹ M≥1+ε'' ⟹ total = (a+b)+(1+ε'') = 1+ε'+2a ≥ 1+ε'. ✓ Correctly uses T,
  NEVER the certified-FALSE Claim(ε<0).
- **Well-founded**: level n invokes only level n−2 (Claim(n−2), T(n−2)); bases Claim(1,2), T(1,2)
  certified. Odd/even chains both grounded. Budget |P_lo|=|P|−2≤n−1 preserves the ≤ℓ+1 constraint;
  S_{P_lo}⊆S_{G_{n−3}} via the certified SET IDENTITY.

This closes G-INC-1 = Claim(n,0) unconditionally for ALL n — the biggest single win (kills the
LB anchor crux that has been the shared residual for 3+ rounds). Numeric support: T(3)/T(4) 0
violations reported by both explorers and prior reviewers.

Issues to close while building (CHANGES-REQUESTED-level, not blocking the build):
1. Write the h=0 sub-case for BOTH Claim(n,ε) and T(n) explicitly (one line each) — cite deficit_top.
2. State the mutual-induction dependency chain explicitly (T(3)←T(1),Claim(1); T(4)←T(2),Claim(2);
   T(5)←T(3),Claim(3); …) so strong induction is visibly well-founded.
3. Use refinedR's τ-form arithmetic (self-consistent) rather than tell's `1+ε'+2b` intermediate.
4. Secondary G-INC-2 (refined-R c_R-induction) is a PLAN, not a proof — do NOT claim it inherited
   from the anchor (tight case R={4,4,4,2,1},Q={5,5,4,2} has S_Q=[2,4)⊄S_{G₃} — confirmed genuinely
   separate). Leave as an open gap; only attempt if the builder has room after T(ℓ).

---

## geometric-selfsimilar (advance) — VERDICT: APPROVE (second priority)

Target: full UB via the sum-bound μ(X,b)≤Σ/D_b; this round closes the m=3 residual gap case and
opens the R3-cascade actual-A potential A=Σ−2p₁ for m≥4. Explicitly AVOIDS the certified-dead
SB-monotone route — correct, since sb-obstruction kills that.

**m=3 base is a complete proof — verified.** One R3 cut of p₁ at offset p₂ makes the invisible pair
{p₂,p₂}, leaving {p₁−p₂, p₃}; p₁≤Σ/2 ⟹ p₃≥p₁−p₂ ⟹ A=Σ−2p₁. Bounded check confirmed the identity
`D_b−2(2^b−1)=1` (b=1..7 exact) and A=Σ−2p₁<Σ/D_b at the threshold (b=2: A=0.14285<0.14286; b=3:
0.06666<0.06667). Budget 1 cut ≤ b. Solid.

**m≥4 induction: right technique, one honest residual (Case B).** The potential invariant
`A(final)≤Σ−2p₁` is maintained: Case A (p₁'=p₁−p₂, Σ'=Σ−2p₂) preserves it EXACTLY
(Σ'−2p₁'=Σ−2p₁) and preserves p₁'≤Σ'/2 (algebraically: p₁−p₂≤Σ/2−p₂=Σ'/2); Case B (p₁'=p₃,
p₂+p₃>p₁) gives A≤Σ−2(p₂+p₃)<Σ−2p₁, strictly smaller. In both the cascade stays ≤Σ−2p₁<Σ/D_b (the
step-2 inequality is on the ORIGINAL Σ,p₁,b). Explorer: 102 configs / 0 violations, max ratio 0.75.

Issues to close while building (CHANGES-REQUESTED-level):
1. **Case B is the one genuinely non-trivial step** — nail a rigorous invariant that the sub-instance
   stays in the gap case (so the IH applies) OR that when it escapes, the actual-A cascade (NOT an
   SB reduction) still bounds A. The explorer flags "may need sub-casework"; make it airtight,
   including the m=4 4th-piece bookkeeping across two R3 steps.
2. Verify the effective-piece ORDERING (which piece is larger post-cut) in every branch — the sign
   of A depends on it. Enforce the budget invariant m≤b+1 so m−1 cuts are legal.
3. Do NOT reach for SB-monotone / partial-shadow chaining (certified dead) — the whole point is the
   actual-A potential.

---

## ll-dyadic-symdiff (advance) — VERDICT: APPROVE (third priority)

Target: full LB via measure(S_Q△S_R)≥1 (native non-containment); this round pushes the REFINED-R
branch that T(ℓ) does NOT cover (confirmed genuinely separate by the refinedR explorer).

Sound: Cases 1/2/Sub-3a are R-agnostic (bound uses only S_Q's high interval / odd count / fully-odd
level + S_R⊆[0,2^{n−1})) — correctly not G_{n−1}-specific. Budget reduction |Q|≤n for c_R≥1 is
correct (joint budget #Q+#R≤n, c_R≥1). The residual Sub-3b refined R is the honest hard piece and is
NOT claimed closed.

Issues to close while building (CHANGES-REQUESTED-level):
1. This is the lower-priority slug — the refined-R residual is genuinely hard; treat this round as
   pushing Sub-3a coverage via the budget reduction, with Sub-3b refined R left as the residual.
2. Do NOT re-import the false "max(Q)<2^{n−1}⟹A≥2" (B3 tight at A=1, Q={3,3,2},R={2,2,2,1}).
3. Do NOT assume a refined-R analogue of the SET IDENTITY / top-band decomposition exists (none known).
4. This slug and ll-inclusion-gap are RIVAL complete LB attempts, not two halves — do not merge.

---

## Not nominated (stay live)

- **alternating-sum-value**, **extremal-smoothing**: not built since R3; S1 route de-prioritized by
  both explorers (stuck 4+ rounds). Correct to reserve builder slots for the converging routes.
  Candidates for retirement if a slot becomes scarce, but keep live this round.

---

## Ranking (updated, stale flags cleared)

Head-to-head applied (anchored to this round's evidence — ll-inclusion-gap's T(ℓ) closure is the
decisive advance; geometric leads on track record; the two R3-stalled slugs lose to all live routes):

- ll-inclusion-gap > geometric-selfsimilar, ll-dyadic-symdiff, alternating-sum-value, extremal-smoothing
- geometric-selfsimilar > alternating-sum-value, extremal-smoothing
- ll-dyadic-symdiff > alternating-sum-value, extremal-smoothing
- alternating-sum-value > extremal-smoothing

Resulting Elo: geometric-selfsimilar 1657.7 > ll-inclusion-gap 1614.3 > ll-dyadic-symdiff 1518.8 >
alternating-sum-value 1411.4 > extremal-smoothing 1297.9. (ll-inclusion-gap closed the gap on the
leader; it now clearly leads the LB field.) No new slug registered; no copy requested.

---

build set: ll-inclusion-gap, geometric-selfsimilar, ll-dyadic-symdiff
