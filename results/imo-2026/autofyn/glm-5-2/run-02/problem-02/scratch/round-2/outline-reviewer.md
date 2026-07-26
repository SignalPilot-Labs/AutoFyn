# imo-2026-02 — round 2 outline-reviewer report

## Independent re-verification of the headline claim (the saturation identity)

This is the load-bearing question of the round. Round-1's approach file (the source of truth) records Proposition 4 — `Qt2·e3_line − et2·Q_line = D₀·G` — as **FALSE**, with an explicit counterexample `b=4, u=1, v=3, lx=1/2, ly=7/2, t=1/3` at which it claims the LHS evaluates to `11946.6̄ ≠ 0` (using `Q=256`). The round-2 complex explorer claims the round-1 verdict was an arithmetic slip (`Q` is `320/3`, not `256`) and that the identity holds.

I rebuilt `e1, e2, e3, Q` from the cross/dot tangent form (†) from scratch in sympy and re-ran the field division over `QQ.frac_field(b,u,v,lx,t)[ly]`. Findings:

1. **Homogeneous linearity (Lemma 1) and the cubic `D₀` factorisation confirmed.** `D(L) = −(b/4)·|C|²·D₀(L)` with `D₀` exactly as round-1 states.
2. **Lemma-3 et2 relation confirmed:** `et2 − ((b³/2)·|C|²·(v−ly)·|L−C|² − b²·D) ≡ 0` over the field.
3. **THE SATURATION IDENTITY IS TRUE.** `sp.div(Poly(Qt2·e3_line − et2·Q_line, ly, domain=QQ.frac_field(b,u,v,lx,t)), Poly(D₀, ly, domain=...))` returns remainder `0` with an **explicit quotient `G` linear in `t`** (and at most linear in `lx, ly`). This is a parameter-free polynomial identity — it holds for every non-degenerate triangle simultaneously, not just numerically.
4. **Counterexample numerics confirmed corrected.** At `b=4,u=1,v=3,lx=1/2,ly=7/2,t=1/3`: `K=(8/3,8/3)` (matches round-1), but `Q = 320/3` (recomputed from the cleared-target formula), NOT `256`. Round-1's `Q=256` was the arithmetic slip that fed the false "remainder nonzero" verdict.

The round-1 approach file's Section 6 / Reproducibility note claims to have run the field-domain `Poly(..., ly, domain=QQ.frac_field(...))` check and reported nonzero — that report is contradicted by my independent run, which returns remainder `0`. The most likely explanation: round-1's field-domain computation was contaminated by the same wrong `Q=256` value (the field reduction was fed an expression built from the mis-evaluated counterexample rather than the true polynomial), or the wrong polynomial was reduced. Either way, **the FALSE verdict does not survive an independent from-scratch rebuild.**

This is a genuine breakthrough: analytic-branch-cert's closing certificate is valid, and the route is essentially a solve candidate modulo rewriting the certificate cleanly.

## Per-approach verdicts

### `analytic-branch-cert` — APPROVE-field (leading solve candidate)

The whole theorem is targeted end-to-end via the coordinate reduction `OM=ON ⟺ Q=0` + the saturation identity forcing `Q_line=0` from `e3_line=0` on `D₀=0`. Skeleton is sound: Step 1 (normalisation), Step 2 (`OM=ON⇔Q=0` — the `analytic-target-line` promotable lemma, certified), Step 3 (tangent encoding), Step 4 (cubic+line reduction — `angle-linearity-cubic-reduction`, certified), Step 5 (field-reduced quadratics in `t`), Step 6 (`et2-on-D-zero-relation`, certified by direct subtraction), Step 7 (positivity, barycentric, certified), Step 8 (degenerate `L=C` exclusion, certified), Step 9 (the saturation identity — **now independently verified TRUE**), Step 10 (conclusion).

Load-bearing lemma with mechanism: the saturation identity `Qt2·e3_line − et2·Q_line = D₀·G` — mechanism is field division over `Q(b,u,v,lx,t)[ly]` leaving remainder `0` with explicit `G` linear in `t`. I verified this. The round-1 "FALSE" verdict was the arithmetic-slip trap the per-role rule warns about; the round-2 explorer's re-discovery is correct.

No forbidden moves (no spiral similarities, no isogonality ∠BAK=∠CAL). No skipped cases (the only degenerate `L=C` is excluded at Step 8). The leading-coefficient `et2>0` argument uses the inside hypotheses (barycentric `ly<v`, `L≠C`) — this is the legitimate deployment of the hypotheses (NOT the unused-α-hand-wave the round-1 file worried about; the α-condition enters via `e3_line=0`, the third angle equality, which IS used at Step 10).

**Builder instructions (mandatory):** do NOT trust this review's verification or the explorer's — re-verify from scratch. (a) Recompute `Q` at the round-1 counterexample from the cleared-target formula and confirm `320/3` (I did; you must too). (b) Re-run `sp.div(Poly(LHS, ly, domain=QQ.frac_field(b,u,v,lx,t)), Poly(D₀, ly, domain=...))` and STATE the explicit quotient `G` in the proof body (it is linear in `t`, degree ~4 in `lx,ly` — give the full expression). (c) Confirm `G` is linear in `t`. (d) State Lemma 3 in its corrected on-`D=0` form (NOT the round-2 draft's mis-stated exact factorisation). Then conclude `et2·Q_line = Qt2·e3_line − D₀·G = 0` on `D₀=0` with `e3_line=0`, `et2>0` ⟹ `Q_line=0` ⟹ `OM=ON`. This is a write-up task on a verified certificate, not a new-mechanism task.

### `analytic-resultant-cert` — APPROVE-field (insurance, untested)

Whole-theorem target via the same coordinate reduction and a DIFFERENT closing certificate: `res_t(e3_line, Q_line)` divisible by `D₀²` forces a common root in `t` on `D₀=0`; `et2>0` + inside hypotheses select the configuration's `t` as that root ⟹ `Q_line=0`. The reduction prefix (Steps 1–5) is imported from `analytic-branch-cert`'s certified promotable lemmas — a verified shared prefix, NOT a single-gap trap (if the prefix were wrong, both die, but the prefix IS verified). The divergence is genuinely in the last step (saturation vs resultant), so they are rival closings on a solid foundation, not pieces of one proof.

The mechanism for Step 6 (resultant factorisation) is plausible and the explorer reports a concrete factor `D₀²` with explicit cofactors. The mechanism for Step 7 (root-selection) is the genuinely hard part and is NAMED BUT NOT DERIVED: the resultant gives existence of a common root over the algebraic closure, but the configuration's `t` is a REAL root, and the argument that the inside hypotheses pin the configuration's `t` to the resultant's common root is unproved. This is a real gap, not a hand-wave — but it is the named load-bearing step and the outline flags it honestly.

**Builder instructions:** (a) verify `res_t(e3_line, Q_line)` factorisation over the field and state `R` explicitly; (b) the root-selection argument is the hard step — argue that `et2>0` (real, nonzero) makes `e3_line`'s `t²`-leading coefficient nonzero, so `e3_line=0` has finitely many real roots, and the inside hypotheses (`K∈△BMC` strictly, `K≠B`, `det(K,L)≠0`) pick the configuration's real `t`, which the resultant forces to be a `Q_line`-root. If the root-selection cannot be made rigorous, fall back to the (verified-TRUE) saturation certificate — this approach is insurance.

### `power-secant-product` — CHANGES REQUESTED

Whole-theorem target via `OM=ON ⟺ MK·MV = NL·NW` + corrected crux identity `(**)_corr` with `sin(b+β)`, closed by α arc-sum + pencil cross-ratio + Ptolemy. Reduction (Steps 1–2), sine-rule expressions (Step 3), and directed-angle lemmas (Step 4) are certified from round 1. The REVISE fixes a CONFIRMED sign error: `∠CAW = −(b+β)`, not `b−β` (round-1's trap). The corrected crux `(**)&_corr` with `sin(b+β)` is verified ~1e-13 (per explorer).

**Issues (fixable gaps):**
- **Step 5 α arc-sum (SUM form, not DIFFERENCE):** the outline asserts `2α = arc(RA)+arc(KP) = arc(AS)+arc(QL)` (SUM) as the directed external-angle theorem. Round-1's file used the DIFFERENCE form `2α = arc(KP) − arc(AR)` and the outline now flags this as WRONG. The SUM vs DIFFERENCE distinction is load-bearing and the mechanism (which arc combination reproduces `∡(BA,BK)=−α`) is stated but not derived in the outline. The builder must derive the SUM form from the directed external-angle theorem explicitly (the directed external angle at an exterior point B is `½(arc(far₁→far₂)+arc(near₁→near₂))` mod π) and verify it reproduces `−α` numerically. I could not independently numerically verify the sign correction `∠CAW=−(b+β)` (my config generator failed to find inside-hypothesis configs for the test triangle in the time budget); the builder MUST re-verify both the sign fix AND the SUM-form arc claim numerically before building on them.
- **Step 6 (pencil cross-ratio `(A,P;R,V)=(A,P;B,M)`):** the mechanism "M midpoint fixes `(A,P;B,M)` and the pencil at K sends line AP to Γ" is stated but UNPROVED. This is a genuinely hard projective argument and is the load-bearing bridge. The outline flags it as a gap honestly. The builder must either prove this projectivity or find an alternative elimination of R.
- **Step 7 (Ptolemy + arc-sum + cross-ratio ⟹ (**)_corr):** named but NOT derived. The combination of three mechanisms into the trig identity is the genuinely hard algebraic step and is handed off without a derivation. This is the second load-bearing gap and it is under-specified — a "then it follows" risk.

No forbidden moves (the false spiral similarities were already cut in round 1; this round's revision does not reintroduce them). Whole attempt, not a fragment. The two load-bearing gaps (Steps 6, 7) are flagged but their mechanisms are under-specified — a "CHANGES REQUESTED" not "RETHINK" because the technique (cross-ratio + Ptolemy) is in principle capable, but the builder must flesh out the derivations, not just assert them.

### `antipode-rightangle` — CHANGES REQUESTED

Whole-theorem target via `OM=ON ⟺ A'∈pbis(BC)` (homothety+antipode, certified) + trig-Ceva identity (T) in △BKL. The reduction (Section 1), Thales characterisation (Section 2), direction table (Section 3), metric constraints (Section 4), trig-Ceva reformulation (Section 5), and sine-rule relation (R1, Section 6) are ALL certified from round 1. The single gap is Step 7: derive (T) from (R1)+(C1)+(C2).

**Issues:**
- **Step 7 closing is still a gap.** The outline proposes two routes: (a) CAS-assisted trig cancellation (round-1 sympy did not terminate; try again with explicit (C1),(C2) in angle variables `α,β,γ,A,B,C`, reduce mod `A+B+C=π`); (b) synthetic via α arc-sum + Ptolemy (importing the cross-ratio link from `power-secant-product` once certified). Route (b) makes `antipode-rightangle` and `power-secant-product` share the SAME closing mechanism — the outline notes `(T) ⟺ (**)_corr ⟺ OM=ON`, so a closing of one transfers. This is honest about the equivalence but it means the two synthetic approaches CONVERGE on the same α-crux closing. **Diversity concern (see below).**
- No forbidden moves. Whole attempt. Cases covered (directed mod π; inside hypotheses select branches). The `∠A'BK=90°−C` lemma is α-independent along the family (verified), which is the load-bearing incidence claim and is certified.

The technique is right (trig Ceva is the standard concurrency tool); the gap is the closing trig cancellation, which is a legitimate hard step, not a wrong technique. CHANGES REQUESTED: the builder must actually derive (T) (route (a) or (b)), not just re-state it.

## Diversity-of-thought assessment

Two diversity concerns:

1. **The two analytic approaches (`analytic-branch-cert`, `analytic-resultant-cert`) share their entire reduction prefix.** This is acceptable here because (a) the shared prefix is VERIFIED (Lemma 1, cubic D₀, et2-on-D=0, degenerate exclusion — all certified), so they do not share a wall; (b) they diverge in the closing certificate (saturation vs resultant), which is genuinely different mechanism. They are rival closings on a solid foundation, not pieces of one proof. The risk is only that `analytic-resultant-cert` is insurance against a re-verification failure of saturation — and since I verified saturation holds, `analytic-resultant-cert` is lower-urgency. Worth one builder as insurance, but if saturation's write-up goes through cleanly this round, `analytic-resultant-cert` can be retired next round.

2. **The two synthetic approaches (`antipode-rightangle`, `power-secant-product`) converge on the SAME α-crux closing.** The outline makes this explicit: `(T) ⟺ (**)_corr`, so a closing of one transfers to the other. They have DIFFERENT verified prefixes (antipode+trig-Ceva vs power-of-a-point+sine-rule), so they are not one proof split into pieces — but their closings collapse to the same mechanism (α arc-sum + cross-ratio + Ptolemy). This is a genuine shared-gap risk: if the cross-ratio link `(A,P;R,V)=(A,P;B,M)` cannot be proved, BOTH synthetic approaches stall together. The outline does not diversify the closing mechanism across the two. **Flag for the orchestrator:** if the synthetic approaches stall again this round on the cross-ratio link (the shared-gap plateau condition), next round's outliner should open ≥1 approach on a genuinely different framing (the outliner already lists candidates: a direct-coordinate trig-identity proof on the (C1),(C2) system; a Möbius/cross-ratio-only proof on Γ; a pure-projective proof exploiting the midpoint pencil as spine rather than bridge). The analytic route's verified breakthrough makes this less urgent (the theorem is essentially solved), but the synthetic field has collapsed to one closing mechanism.

## Ranking rationale

Comparisons anchored to evidence (last outcomes + my verification):
- `analytic-branch-cert` beats all three: its saturation identity is now VERIFIED TRUE by independent from-scratch field division (remainder 0, explicit G); the others' closings are unverified (resultant: factorisation unverified, root-selection unproved; antipode: (T) derivation unproved; power: bridge unproved + sign error pending fix). Strongest signal in the field.
- `analytic-resultant-cert` vs `antipode-rightangle` (draw): both have verified prefixes and unverified closings; the resultant route's closing is at least concretely stated (a specific factorisation), while antipode's closing is a sympy-termination hope. Roughly even.
- `analytic-resultant-cert` beats `power-secant-product`: shared verified prefix with `analytic-branch-cert` is a stronger foundation; `power-secant-product` has a CONFIRMED sign error still pending fix.
- `antipode-rightangle` beats `power-secant-product`: antipode has no pending correction; power has a confirmed sign error to fix first before its bridge can even be attempted.

Updated Elo (from `update_ranking`):
- `analytic-branch-cert`: 1559.6 (leader, stale cleared)
- `antipode-rightangle`: 1512.9
- `analytic-resultant-cert`: 1499.3 (cold-start, anchored)
- `power-secant-product`: 1428.2

## New registration

- `analytic-resultant-cert` registered at cold-start Elo 1500 (now 1499.3 after ranking). Body to be seeded by the outliner/builder.

## Build set

`analytic-branch-cert` is the leading solve candidate (verified certificate, write-up task). `analytic-resultant-cert` is insurance (one builder, lower urgency). `power-secant-product` and `antipode-rightangle` remain worth one builder each — their closings are equivalent, so a closing of either transfers; building both is parallel insurance on the synthetic side, and `power-secant-product`'s sign fix is cheap. Four parallel builders, one per slug (no collision — each owns its own file).

**If budget forces a cut:** keep `analytic-branch-cert` (solve candidate) + `antipode-rightangle` (most-verified synthetic, no pending correction); drop `analytic-resultant-cert` (insurance, lower urgency) and `power-secant-product` (sign fix first, bridge same as antipode's).

build set: analytic-branch-cert, analytic-resultant-cert, power-secant-product, antipode-rightangle
