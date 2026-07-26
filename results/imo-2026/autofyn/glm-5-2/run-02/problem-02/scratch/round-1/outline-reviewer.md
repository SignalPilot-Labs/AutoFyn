# Outline review — imo-2026-02 (round 1)

All four proposed approaches were vetted adversariallly, with the load-bearing claims checked numerically (Python/sympy) on the verified worked example A=(0,0), B=(4,0), C=(1,3), K=(3.12700295,0.56547641), L=(1.09481219,2.63333187) (angle-equality residuals to machine precision, OM−ON≈1e-14). Findings below.

## Cross-cutting numerical facts (verified this round)

1. **The three reductions are sound.**
   - Antipode: A':=2O−A (antipode of A on (AKL)); |A'B|=2|OM|, |A'C|=2|ON| ⟹ OM=ON ⟺ A'∈pbis(BC). Confirmed (|A'B|=|A'C| to 1e-9).
   - Power: OM=ON ⟺ pow_(AKL)(M)=pow_(AKL)(N) ⟺ AB·MA'_B=AC·NA'_C (secant through A). Sound.
   - Analytic: O·(C−B)=(|C|²−|B|²)/4 (A=0); e1,e2 are linear in K−B (const term 0 ⇒ K=B trivial branch always), determinant D(L) is cubic in L, so on D(L)=0 the system collapses to K=B+t·d(L). Reproduced exactly in sympy.
2. **The confirmed TRAP extends to ALL THREE "similarities", not just spiral-at-A.** The spiral-isogonal explorer's numerics were unreliable (numpy arccos picks supplements, as it itself warned). On the verified configuration:
   - Isogonality ∠BAK = ∠CAL is **FALSE**: 10.25° ≠ 4.14°.
   - △ABK∼△ACL (A↔A,B↔C,K↔L) is **FALSE**: AB/AC=1.265, AK/AL=1.114, BK/CL=2.746.
   - △LBK∼△LNC (L↔L,B↔N,K↔C) is **FALSE**: LB/LN=3.06, LK/LC=7.66.
   - △LCK∼△BMK (K↔K,L↔B,C↔M) is **FALSE**: LC/BM=0.189, LK/BK=2.79, CK/MK=2.56.
   - What IS true: the three raw angle equalities α=∠KBA=∠ACL, β=∠LBK=∠LNC, γ=∠LCK=∠BMK (verified to 1e-6), and the midpoint/parallel structure (MB∥AB, NC∥AC).
3. **The antipode target lemma is TRUE.** ∠A'BK = 90°−∠C = 26.565° and ∠A'CL = 90°−∠B = 45°, both numerically exact. This is the real crux of the problem and the right thing to chase — but NOT via the false similarities.
4. **The analytic 2-var ideal-membership certificate is FALSE**, and so is radical membership. Q (the cleared target) has a NONZERO Gröbner remainder mod `<D(L), e3|_{K=B+t·d(L)}>` in Q[lx,ly,t]; Rabinowitsch `<D, e3_sub, z·Q−1>` reduces 1 to 1 (Q ∉ radical). HOWEVER, Q vanishes on all 40/40 sampled REAL common zeros of `<D=0, e3_sub=0>`. So the 2-var reduction eliminates the spurious real branches (2094 in the 4-var ideal → ~0 here), but the vanishing is **real-variety-only**: a Real-Nullstellensatz / arc-parametrisation argument is genuinely required. The outline's step-5 claim "P is a multiple of e3_substituted" (plain ideal membership) is wrong as stated.

---

## antipode-rightangle — CHANGES REQUESTED

- **Framing sound.** Step 1 (homothety+antipode equivalence, verified 1e-12) and step 2 (A' characterised by the two Thales right angles ∠AKA'=∠ALA'=90°) are correct and clean.
- **Target lemma (step 5) is verified TRUE** (∠A'BK=90°−∠C, ∠A'CL=90°−∠B). Good crux to attack.
- **FATAL FLAW in the proposed mechanism (steps 3–4).** The outline's engine for the crux is the isogonality of AK,AL and the three similarities △ABK∼△ACL, △LBK∼△LNC, △LCK∼△BMK. ALL FOUR ARE FALSE (verified above; this is the confirmed TRAP, which the spiral-isogonal explorer misreported as true due to arccos-supplement errors). The reasoning "the shared angle at A forces △ABK∼△ACL" is also invalid: ∠BAK and ∠CAL are not a shared angle. Step 5's chase is built entirely on these false lemmas and cannot work as written.
- **Required changes for the builder:**
  - DROP steps 3 and 4 entirely. Do NOT use isogonality ∠BAK=∠CAL or any of the three "similarities" — they are false and the trap.
  - Rebuild the crux chase from the TRUE ingredients: the three angle equalities α,β,γ + the two Thales right angles (A'K⊥AK, A'L⊥AL) + the midpoint/parallel structure (MB∥AB, NC∥AC) + the containments (which fix directed-angle signs). The target ∠A'BK=90°−∠C is verified; find a correct directed-angle-mod-180 chase for it.
  - Phrase everything as directed angles mod 180 from the start; the inside-hypotheses (K∈△BMC, L∈△BNC, K∈∠LBA, L∈∠ACK) are what fix the signs — do not drop them.
- Verdict: the technique (synthetic angle chase to the antipode) is right and the target is verified; the specific lemmas are false and must be replaced. Buildable once corrected.

## power-secant-product — CHANGES REQUESTED

- **Framing sound.** Steps 1–2 (OM=ON ⟺ AB·MA'_B = AC·NA'_C via power of a point at the midpoints along secants AB, AC) are correct and verified. Note A'_B (second intersection of AB with (AKL)) is a DIFFERENT point from the antipode A' of approach 1, so this is a genuinely distinct synthetic target — good diversity.
- **FATAL FLAW in the crux mechanism (steps 3–4).** Same as antipode: step 3 leans on the false isogonality/false similarity △ABK∼△ACL to get AB/AC=AK/AL; step 4's "candidate mechanism" chains the three false similarities △LBK∼△LNC, △LCK∼△BMK. All are false (verified). The crux (the MA'_B/MA'_C ratio identity reducing to AC/AB) has no valid engine.
- **Required changes for the builder:**
  - DROP the isogonality and three-similarities lemmas.
  - The secant-product target AB·MA'_B=AC·NA'_C stands; find a different way to compute or bound MA'_B and MA'_C (e.g. sine rule in △AMA'_B, △ANA'_C combined with concyclicity on (AKL) and the THREE TRUE angle equalities α,β,γ). The outline's step-4 "sine-rule + concyclicity" idea is the right shape, but it must not import the false similarities.
  - Watch directed-power signs (A'_B may lie on either ray of AB; pinned by K∈△BMC). The TRAP "spiral at A sends K→L" remains forbidden.
- Verdict: right technique (power of a point + sine-rule/similar-triangle ratio chase), clean verified reduction, but the crux engine is broken and must be rebuilt from the true angle equalities. Buildable once corrected.

## analytic-branch-cert — APPROVE (with one required correction)

- **Framing sound and reduction verified.** I reproduced steps 1–4 exactly in sympy: e1,e2 linear in (kx,ky) with zero constant (so K=B is the always-present trivial branch), the 2×2 determinant D(L) is cubic in (lx,ly), and on D(L)=0 the system collapses to the line K=B+t·d(L) with d(L)=(b1,−a1). The cubic structure and the line parametrisation are real.
- **Central certificate needs correction (step 5).** The outline claims "P is a multiple of e3_substituted" (plain ideal membership in `<D(L), e3_sub>`). This is **FALSE**: the Gröbner remainder of the cleared target Q mod `<D, e3_sub>` in Q[lx,ly,t] is nonzero, and Q is not in the radical either (Rabinowitsch returns 1). The builder MUST NOT claim ideal membership — it is the same shape of trap as the dead 4-var route, just hidden one level down.
- **What IS true (and the basis to build on):** Q vanishes on all sampled REAL common zeros of `<D=0, e3_sub=0>` (40/40 in a wide box, vs 2094/5657 spurious in the dead 4-var ideal). So the 2-var reduction has already eliminated the spurious real branches — the real-variety vanishing holds. The hard step is to prove this real-variety vanishing rigorously.
- **Required mechanism for step 5 (replacing the false ideal-membership claim):**
  - EITHER a Real-Nullstellensatz / Positivstellensatz certificate with the inside-inequalities (barycentric positivity of K∈△BMC, L∈△BNC; signed-angle tests for K∈∠LBA, L∈∠ACK) appended as constraints, certifying Q≥0 on the feasible arc with equality;
  - OR (more tractable) parametrise the real arc of the cubic D(L)=0 selected by the inside-conditions, substitute into e3_sub (a real quadratic in t) and Q, and verify Q vanishes identically as a real-analytic function on that arc (the inside-conditions pick the correct root of the quadratic and the correct arc of the cubic).
- **Step 6 (branch selection) is confirmed load-bearing** — not removable, because Q is not in the radical (there are complex spurious components; real-variety reasoning is genuinely needed). The outline correctly flags this; the builder must produce a human-auditable branch argument, not a blind "CAS says P=0".
- **Free-parameter risk (honest).** The symbolic certificate in (u,v,lx,ly,t) (free triangle) is unverified — only the fixed triangle is tested. If the general symbolic certificate fails, the route yields a fixed-triangle verification only, which is `partial` not `solved`. The builder must flag this honestly. The fixed-triangle certificate + real-arc argument is already a strong verification backstop for the synthetic approaches.
- Verdict: sound, verified reduction; genuinely distinct (computational) framing; the one required correction (replace ideal-membership with real-variety/Rabinowitsch-arc argument) is identified and attackable. Build.

## spiral-compose-midpoints — RETHINK (hold out of build set, do not register)

- The central conjecture Φ(M)=N (a composition of the three spiral similarities centred at A, L, K swaps the midpoint pair) is **unverified** — the outline itself admits "numerics not yet confirming this route." The mechanism (step 2) is hand-wavy: "the composition order and the exact segment pairs are the open question."
- Given that the three component "spiral similarities" themselves are numerically false (see cross-cutting fact 2 above — the angle conditions give direction coincidences, not full spiral similarities with matching ratios), the composition premise is doubly suspect: there is no spiral similarity at A sending BK→CL with the right ratio, so there is nothing clean to compose.
- The framing IS genuinely different (image-of-midpoint/circumcentre under a composed spiral). Worth a round-2 explorer revisit IF a verifier can exhibit ANY genuine spiral/affine map sending M→N built from the configuration. Until then, RETHINK: do not build, do not register. (The outliner already held it out; I concur.)

---

## Diversity check (build set)

The three build-set members attack from genuinely different framings — no shared-gap trap:
- **antipode-rightangle**: synthetic; target = antipode A' on pbis(BC); crux = angle chase to ∠A'BK=90°−∠C.
- **power-secant-product**: synthetic; target = secant-product AB·MA'_B=AC·NA'_C (different algebraic target, different point A'_B≠A'); crux = sine-rule ratio identity.
- **analytic-branch-cert**: computational; target = polynomial Q=0 on the real arc of the L-cubic; crux = real-variety vanishing + branch selection.

The two synthetic approaches share the *type* of tool (directed angles / sine rule) but target different quantities (antipode vs secant second-intersection), so a failure of the angle chase in one does not force a failure in the other's ratio chase. The analytic route is fully independent (polynomial computation) and doubles as a verification backstop. Good diversity.

---

## Ranking (round 1, cold-start 1500)

Pairwise, anchored to expected viability:
- antipode-rightangle vs analytic-branch-cert: **draw** — both have verified reductions and a verified concrete target (synthetic crux / real-variety vanishing); different framings, comparable promise.
- antipode-rightangle **beats** power-secant-product — both have verified reductions but antipode's crux (∠A'BK=90°−∠C) is a concrete verified target lemma, while power's crux (the MA'_B/MA'_C ratio identity) is vaguer and less pinned.
- analytic-branch-cert **beats** power-secant-product — verified reduction + numerically-confirmed real-variety vanishing + fixed-triangle backstop value, vs power's unspecified ratio engine.

(spiral-compose-midpoints is RETHINK, not registered, excluded from ranking.)

## Build set

The three nominated approaches, with the corrections above folded into the builder dispatch:
- **antipode-rightangle** (CHANGES REQUESTED — drop false isogonality/similarities; rebuild crux chase from the three true angle equalities + Thales right angles).
- **power-secant-product** (CHANGES REQUESTED — drop false similarities; rebuild the MA'_B/MA'_C ratio identity from the true angle equalities via sine rule + concyclicity).
- **analytic-branch-cert** (APPROVE with correction — replace the false ideal-membership claim with a real-variety/Rabinowitsch-arc argument; branch selection is load-bearing).

build set: antipode-rightangle, power-secant-product, analytic-branch-cert
