# Proof review r2 — IMO 2026 P2 (imo-2026-02), slug `trig-metric-identity`

**Is imo-2026-02 SOLVED? YES.** Verdict: **APPROVE**. True Status: **solved**.
Builder's recorded Status `solved` is correct.

## Scope
Final verification of the single reviewer-diagnosed gap from round 1 (the `0·∞` hole at
`f=0` in the ideal-membership step `T=q_G·G+q_H·H`), plus a no-regression check on the
rest of the chain. Everything else was already verified exactly last review.

## The closure — all four sub-checks pass

**(a) Vanishing quantity correctly identified as a positive multiple of `f`.** Confirmed
independently: I re-ran the reduction of `T` mod `⟨G,H⟩` from scratch and recovered
`lc_{t_K}(G)=\tfrac12(1+s²)²(p²+q²)·f` and `lc_{t_L}(H)=\tfrac12(1+s²)²((p−a)²+q²)·f`; the
denominator content `c=lcm(denom q_G,denom q_H)` equals `f` exactly (`c−f=0`). So `f` is
precisely the quantity whose vanishing caused the `0·∞`, and the two leading coefficients
are positive multiples of it. The builder replaced the rational identity by the
**polynomial** identity `f·T=Q_G·G+Q_H·H`; I re-derived `Q_G=f·q_G`, `Q_H=f·q_H` from
scratch and confirmed `denom(Q_G)=denom(Q_H)=1` (genuine polynomials) and
`expand(f·T−(Q_G·G+Q_H·H))=0` (exact symbolic zero). This structurally eliminates the
`0·∞`: the cofactors are polynomials, so (8) holds unconditionally.

**(b) `θ<∠ABC` from region membership.** Rigorous. `M` is the midpoint of `AB`, so ray
`BM`=ray `BA`, and the angle of `△BMC` at `B` is `∠ABC`. `K` strictly inside `△BMC` ⟹ ray
`BK` strictly between sides `BM(=BA)` and `BC` ⟹ `θ=∠KBA<∠ABC`. Standard and correct; this
is the exact and only point where `K∈△BMC` enters the metric argument.

**(c) `∠ABC<π−∠A`.** Rigorous: `∠A+∠ABC=π−∠ACB<π` since `∠ACB>0` (angle sum). Correct.

**(d) `f>0` genuinely closes `G=H=0 ⟹ T=0` with NO `0·∞` hole.** Yes. Chain:
`f=(1+s²)·AB·AC·sin(∠A+θ)` (exact symbolic zero, re-derived), `0<∠A+θ<∠A+∠ABC<π` ⟹
`sin(∠A+θ)>0` ⟹ `f>0`. Then `G=H=0 ⟹ f·T=Q_G·G+Q_H·H=0` (polynomial identity, evaluated
at exact reals — no division anywhere), and `f>0 ⟹ T=0`. The only division is by the
strictly-positive scalar `f`. Clean; the hole is gone.

I also spot-checked `f` numerically over a range of `θ` on a concrete scalene triangle:
`f>0` throughout, and for admissible `θ<∠ABC` one has `∠A+θ<∠A+∠ABC=125°<180°`. (At a
non-admissible `θ=85.9°>∠ABC`, `f` happens to stay positive too — irrelevant, since the
builder's `θ<∠ABC` is a correct *sufficient* condition, not claimed necessary.)

## No regression in the rest of the chain
`python3 results/imo-2026-02/verify.py` passes all asserts as exact symbolic zeros:
`T−(q_G·G+q_H·H)=0`, reduction remainder `=0`, `c−f=0`, `f·T−(Q_G·G+Q_H·H)=0` with
polynomial cofactors, and `f−(1+s²)·AB·AC·sin(∠A+θ)=0`. The reduction (§1), branch/
orientation lemma (§2–3), sine-decoupling `E2=t_K·H`, `E3=t_L·G` (§4), and the cofactor
identity (§5) are all unchanged from the round-1 verification and remain valid. r2 only
ADDS the polynomial identity and the positivity argument; nothing was removed or weakened.
The proof answers the actual question (`OM=ON`, `proof_only`, no numeric answer). All seven
hypotheses are used, all cases (both branches, all four orientations) settled. No
hand-waving, no circularity, no crux-move citation.

## Scores
- Correctness 10/10 — every step independently re-derived; identities are exact symbolic
  zeros, the geometry is fully justified.
- Completeness/rigor 10/10 — the sole prior gap is closed; no skipped cases, no `0·∞`.
- Progress — decisive: partial → solved. Full rigorous proof of `OM=ON` for the whole
  admissible family.

## Actions taken
- Recorded outcome `verified-milestone` for `trig-metric-identity`.
- Wrote `results/imo-2026-02/current.md`: Status `solved` + complete self-contained
  Full proof of `OM=ON`.
- Certified promotable lemma **L-pos** → `results/imo-2026-02/lemmas/leading-content-positive.md`
  (statement matches what is proved; `f>0` argument sorry-free). The three round-1 lemmas
  (goal-reduction, branch-orientation, sigma-and-supplementary) remain certified.
