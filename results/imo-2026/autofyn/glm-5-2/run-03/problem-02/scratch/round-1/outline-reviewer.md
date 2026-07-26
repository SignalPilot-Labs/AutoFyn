# Outline review — imo-2026-02 (IMO 2026 P2, geometry)

Round 1. Population starts empty; every survivor is registered. The explorers numerically verified the two target reductions (A,K,L,A* concyclic; OM=ON) across multiple triangles and the whole 1-parameter family, so the *targets* are well-supported. The review judges whether each framing's gap is closeable in principle, and whether the field diversifies or collapses to one wall.

I re-derived the A* reduction independently: with A=(0,0), B=(4,0), C=(1,3), the reflection of A across perp-bis(MN) is A*=(0.5,−0.5), and indeed |A*−M|=|A−N| and |A*−N|=|A−M| (the reflection swaps M,N). So `A,K,L,A* concyclic ⇒ O∈perp-bis(AA*)=perp-bis(MN) ⇒ OM=ON` is a valid one-line close. The a-star framing rests on a real reduction, not a circular relabeling.

---

## a-star-cyclicity — APPROVE

- **Framing sound.** The reduction (concyclic ⇔ O on perp-bis(AA*) = perp-bis(MN)) is exact and verified. The crux is a single 4-point concyclicity claim, numerically confirmed to ~1e-3 deg via two independent angle equalities (∠AKL=∠AA*L and ∠KAL=∠KA*L). This is the canonical technique for "prove X on a circle" and the cleanest route.
- **Gaps closeable in principle.** GAP-0 (A* characterization equivalence) is a trivial coordinate/rectangle check. GAP-1/2 (express ∠AKL, ∠AA*L via α,β,γ,A,B,C using sine rule in the workhorse triangles △BMK, △CNL) are finite trigonometric computations — the cevians AK, AL are determined by α,β,γ and the triangle, and △BMK=(α,γ,π−α−γ), △CNL=(α,β,π−α−β) give clean sine-rule handles. GAP-3 (the cancelling trig identity) is the genuine heart, but it is a *bounded* trig identity in 6 variables with A+B+C=π; the explorer's numeric evidence across the family says the identity holds identically, so a real cancellation exists to be found. The (E2) fallback (∠KAL=∠KA*L) gives a second shot at the same identity.
- **Mechanism identified.** The outline states a one-line reason the identity should cancel: the cevian lengths AK, AL, A*L are all governed by the same three sine triples (sin α, sin γ, sin(α+γ)) and (sin α, sin β, sin(α+β)), and A*=A+(D−F) is the unique translate making the subtended angles match. That is a mechanism, not a bare label.
- **Watch-outs are correct and recorded.** Directed angles mod π (cyclic quad non-convex, A* outside △ABC); avoids the dead-end AA-similarity and A-centered spiral. No casework needed (inside-configuration fixes signs).

Verdict: sound skeleton, right technique, closeable gap. Build it.

---

## dilation-equal-power — CHANGES REQUESTED

- **Framing (the reduction) sound.** OM=ON ⇔ O*∈perp-bis(BC) ⇔ Pow_{(AK*L*)}(B)=Pow_{(AK*L*)}(C) under D(A,2). I checked: D is a similarity sending perp-bis(MN)→perp-bis(BC) and O→O*; O*A=O*K*=O*L*=R*, so |O*B|=|O*C| ⇔ equal powers. Exact.
- **But GAP-2's mechanism is currently muddled, and it must be tightened before the builder can responsibly pursue this.** The outline's "one-line reason" claims: "under D, condition (ii) becomes ∠L*B'K* = ∠L*CK* — i.e. the chord K*L* of circle(AK*L*) is seen from B' and from C under equal angles, so B' and C lie on a circle through K*,L*." This is fine as far as it goes, BUT the power we need is at the ORIGINAL B and C, not at B'=2B and C'=2C. The outline itself flags the B'/B conflation as a watch-out, yet the load-bearing mechanism still uses B',C' to argue about B,C. The missing step is: how does a concyclicity involving B',C' (which are the dilations of B,C, NOT on circle(AK*L*) in general) translate into equal power of the original B,C wrt circle(AK*L*)? The original B is the midpoint of AB' (since B'=2B from A=origin); that midpoint relationship must be the bridge, but the outline does not state it.
- **Diversity concern (single-gap trap).** The synthetic explorer explicitly noted this is "Equivalent to opening 1 (A* is the point making the chord AA* ∥ BC; P,Q are the same coaxal picture)." Equal power of B,C wrt circle(AK*L*) is the dilated image of the concyclicity of A,K,L,A* (the radical axis of (AK*L*) and circumcircle(ABC) is perp-bis(BC) iff A* = D^{-1}-reflection... is on circumcircle(ABC)). So dilation-equal-power is a SIBLING framing of a-star-cyclicity — same underlying crux, attacked via power rather than angle-chase. If a-star's GAP-3 (trig identity) is a wall, this route hits the same wall one step later, because the power computation's secant lengths BQ, CR reduce to the same sines.
- **Required changes (for the builder, if this is built):**
  1. State explicitly the bridge from "B',C,K*,L* concyclic" (or whatever the dilated conditions give) to "Pow_{(AK*L*)}(B)=Pow_{(AK*L*)}(C)". The midpoint relation (B = midpoint of AB', C = midpoint of AC') is the only candidate mechanism — name it and verify it numerically.
  2. Decide whether the route is genuinely a power computation or whether it collapses back to a concyclicity (B',C,K*,L* cyclic) — in which case it is a-star-cyclicity in disguise and should be merged, not pursued separately.

Verdict: technique (power of a point) is appropriate and the reduction is exact, but the load-bearing mechanism conflates B' with B. Fixable, but it is a sibling of a-star; on round 1, with an empty population, building a-star in preference is more efficient. Defer to the population (registered, ranked below a-star); do NOT build this round.

---

## analytic-resultant — APPROVE

- **Framing sound.** The conclusion OM=ON is an algebraic identity on the 1-parameter solution curve; ideal membership (N_T ∈ (n1,n2)) is the *exact* algebraic counterpart of "the identity holds on the curve." This is a guaranteed-existence route: a finite computation either verifies the identity or it does not. No inspiration needed, no circular reasoning.
- **Verified scaffolding.** The isosceles special case (p=0,q=1) is already symbolically reduced: the 268-term numerator of OM²−ON² has remainder 0 in a 2-polynomial Groebner basis. This is strong evidence the general-(p,q) identity also reduces to 0. The circumcenter linear-solve (2O·K=|K|², 2O·L=|L|²; rows are K,L — matches the stated Ox, Oy formula) is correct. The linearity of OM²−ON² in O (quadratic terms cancel because M,N fixed) is a real simplification, correctly noted.
- **Gaps closeable in principle.** GAP-1/2 (ray orientations + rational K,L) are mechanical (the orientation dead-end is recorded and avoided by the parametric construction). GAP-3/4 (polynomial n1,n2 + O formula) are mechanical. GAP-5 (general-(p,q) elimination) is the heart; the outline gives a concrete tractability strategy (GAP-5a: specialize tα to several values, bound degree, interpolate; GAP-5b: specialize (p,q), interpolate) that avoids the recorded 9-min 5-var lex Groebner timeout. The mechanism — "the conclusion is an algebraic identity on the solution curve, so it MUST reduce to 0" — is sound and is the strongest guarantee in the field.
- **Independent framing.** Pure algebra; shares no wall with the cyclicity/power routes. If the synthetic chase stalls on a trig identity, this route still closes. Critical for field diversity.
- **Risk.** Computational: the elimination might still time out even with interpolation, and orientation/transpose bugs are easy (two already recorded). But the builder can verify each step numerically before trusting the symbolic reduction, as the outline instructs.

Verdict: sound, guaranteed-existence, independent framing. Build it.

---

## miquel-spiral — CHANGES REQUESTED

- **Framing genuinely different.** This is the only transformation-based route (Miquel point / spiral or indirect similarity). It does not construct A*, does not eliminate polynomials, does not chase a concyclicity identity. If the cyclicity and algebra routes both stall, this is the third, independent wall-attack. That diversity is valuable — keep it in the population.
- **BUT the skeleton is three conjectures, not a proof plan.** The load-bearing claim is CONJECTURE S ("there is a spiral/indirect similarity S₀ sending (B,K)→(C,L) or (M,K)→(N,L), with S₀ on perp-bis(MN)"). It is UNVERIFIED — the outline itself makes GAP-2 a numeric gate ("if it fails, this route dies"). The three sub-routes (S-route-1/2/3) are "pick whichever survives numerics," i.e., a scout mission. The recorded dead ends are serious: the A-centered spiral does NOT send BK→CL; no AA-similarity exists; the unique indirect similarity centered at A swapping B↔C is a similarity only when |AB|=|AC|. So the center must be ≠A and is currently unidentified. The Miquel-point sub-route (S-route-2) has no stated reason Mq should lie on perp-bis(MN) beyond "an angle chase" — that is a bare label, not a mechanism.
- **Required changes (builder must do these FIRST, before any proof prose):**
  1. Run the GAP-2 numeric gate on at least two triangles: compute the spiral-similarity center for (B,K)→(C,L) and for (M,K)→(N,L); check whether it equals O or lies on perp-bis(MN). Report which (if any) holds. If none, the route is dead for this round and goes back to the outliner — do not write proof prose on top of an unverified conjecture.
  2. If a center is found, identify which single sub-route survives and drop the other two; the outline cannot stay as three parallel conjectures.
  3. For the surviving sub-route, state the mechanism for the load-bearing step (e.g., "Mq ∈ perp-bis(MN) because the Miquel angle chase gives ∠MqMB = ∠MqNC, which together with MN∥BC forces..."), not just the conclusion.

Verdict: right to keep as a diverse transformation framing, but it is currently a research direction, not a sound skeleton. Build it ONLY as a numeric-gate scout first; if the gate fails, it returns to the outliner. Acceptable for round 1 because the diversity payoff is high and the gate is cheap.

---

## Field diversity assessment

Three genuinely distinct framings:
1. **Cyclicity family** — a-star-cyclicity + dilation-equal-power (siblings; same underlying crux, the concyclicity/equal-power duality). a-star is the cleaner instance.
2. **Algebra** — analytic-resultant (independent; pure ideal-membership).
3. **Transformation** — miquel-spiral (independent; Miquel/spiral similarity).

No single-gap trap across the field: if the cyclicity trig identity (a-star GAP-3) is a wall, the algebra route (independent) and the transformation route (independent, pending its numeric gate) still attack. The only sibling-pair risk is a-star ↔ dilation-equal-power, addressed by deferring dilation this round.

---

## Ranking (round 1, all new, cold-start 1500)

Anchored to feasibility, gap-closability, and independence:
- a-star-cyclicity beats analytic-resultant (draw-leaning): a-star has the cleaner target (single concyclicity, numerically verified, canonical technique) but analytic has the stronger guarantee (ideal-membership must close). Slight edge to a-star for elegance and verified crux; call it a draw but rank a-star first for round-1 priority.
- a-star beats dilation-equal-power (sibling with muddier mechanism).
- a-star beats miquel-spiral (miquel is unverified conjecture; a-star's crux is numerically confirmed).
- analytic beats dilation (guaranteed-existence vs sibling-with-shaky-mechanism).
- analytic beats miquel (guaranteed-existence vs unverified conjecture).
- dilation beats miquel (dilation's reduction is exact even if mechanism needs tightening; miquel is pure conjecture).

Comparisons fed to update_ranking:
- a-star > analytic (slight, both strong)
- a-star > dilation
- a-star > miquel
- analytic > dilation
- analytic > miquel
- dilation > miquel
- analytic = a-star draw (to keep them close — both are legitimate leaders)

I'll register all four survivors (the population is empty). I will NOT copy-branch (no approach asked to twin).

## build set: a-star-cyclicity, analytic-resultant, miquel-spiral

- a-star-cyclicity: the cleanest synthetic route; builder closes GAP-0..3, with (E2) as fallback for GAP-3.
- analytic-resultant: the guaranteed-existence algebraic route; builder closes GAP-1..5 via the interpolation strategy (GAP-5a/5b), avoiding the 5-var Groebner timeout.
- miquel-spiral: builder runs the GAP-2 numeric gate FIRST; proceeds only if a spiral center is found on perp-bis(MN) or equal to O; otherwise reports back for outliner revision.

dilation-equal-power is registered and ranked (live in the population) but deferred from the build set this round: it is a sibling of a-star and its GAP-2 mechanism needs the B'/B bridge clarified before it is worth builder effort. If a-star stalls on GAP-3 next round, dispatch dilation with the bridge-mechanism change-request in hand.
