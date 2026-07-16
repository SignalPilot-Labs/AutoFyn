# Proof-outliner field report — round 1

## imo-2026-05

**Consensus answer (all three explorers, verified symbolically by me):** f(x) = x + c for every constant c ≥ 0. For this family both squared inequalities equal the same SOS margin (x − y − c)²/4 (sympy-verified), i.e. the chain is exactly QM ≥ AM ≥ GM for the pair (x, y+c). The verification direction is trivial in every approach; the whole game is uniqueness.

**Shared rigorous base (3 lines each, no regularity assumptions):** x = f(y) in the left inequality gives f(f(y)) ≤ 2f(y) − y; in the right, f(f(y)) ≥ 2f(y) − y; hence f∘f = 2f − id. With h := f − id this gives h(f(y)) = h(y), fⁿ(y) = y + n·h(y) (AP orbits), and h ≥ 0 (else the orbit exits R_{>0}). These should be certified as shared lemmas in `results/imo-2026-05/lemmas/` at first APPROVE so rivals can import them.

**Cheap kill assessment:** the substitution x = f(y) IS the cheap kill and all approaches use it; what remains (h globally constant, without continuity) has no one-move argument I could find — the three fields below are three genuinely different mechanisms for it. I verified every load-bearing expansion symbolically (SOS margin, the h-coordinate forms of both inequalities, the forbidden-interval roots, the chain inequality).

---

### chain-lipschitz-squeeze: new
File: `results/imo-2026-05/approaches/chain-lipschitz-squeeze.md`
Target: Determine all f: R_{>0} → R_{>0} with sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ sqrt(x·f(y)); prove the answer is exactly {f = id + c : c ≥ 0}, both directions.
Technique: **Two-variable chain inequality + telescoping increment squeeze** (no orbits, no casework, no fixed-point analysis; adapts the "sandwich/pinch from both sides" crux of aimo-0008 and the shift-relation pinning of aimo-0234).
Skeleton:
  1. Verification: both squared inequalities = (x−y−c)²/4 ≥ 0 — by SOS identity / QM-AM-GM [knowledge_base: Standard inequalities]; c < 0 dies on the codomain.
  2. Chain inequality (*): 2·sqrt(f(y1)f(y2)) ≤ 2f(y2) + y1 − y2 for ALL y1, y2 — by left inequality at (f(y2), y2) giving f(f(y2)) ≤ 2f(y2) − y2, right inequality at (f(y2), y1) giving f(f(y2)) ≥ 2sqrt(f(y1)f(y2)) − y1, and chaining. **This never combines the two into the functional equation — only one-sided bounds — so it is the hedge against any subtlety in the f∘f = 2f − id derivation.**
  3. Upper increment bound: f(z+t) ≤ f(z) + t + t²/(4f(z)) — by (*) with (y1,y2) = (z+t, z) and completing the square in sqrt(f).
  4. Strict monotonicity + lower bound: (*) with (y1,y2) = (z, z+t) gives t ≤ 2p(p−q) with p = sqrt(f(z+t)), q = sqrt(f(z)), forcing f strictly increasing and f(z+t) − f(z) ≥ t − t²/(4m) − O(t³) with m = uniform lower bound of f on the interval (m = f(y) by monotonicity).
  5. Telescope over n subdivisions of [y, y+T]: upper sum → T, lower sum → T, hence f(y+T) − f(y) = T exactly — by summing 3–4, errors O(1/n).
  6. f − id constant =: c; c ≥ 0 from positivity as y → 0⁺; combine with step 1.
Key lemmas (claim + mechanism):
  - (*) 2sqrt(f(y1)f(y2)) ≤ 2f(y2) + y1 − y2 — because at x = f(y2) the left inequality's QM collapses to f(y2) (both entries equal), and the right inequality's GM collapses to sqrt(f(y2)f(y1)); chaining the two bounds on f(f(y2)) eliminates f∘f.
  - f strictly increasing — because (*) with roles swapped reads 2pq ≤ 2p² − t, impossible unless p > q.
  - f(y+T) − f(y) = T — because per-piece increments are t ± O(t²/m) with a uniform m, and the quadratic error telescopes to O(T²/n) → 0.
Open gaps: GAP 1 (uniform quantitative lower bound constants), GAP 2 (rigorous telescoping writeup). Both elementary — this approach is closest to a full proof.
Cases to cover: none (no casework; c = 0 handled uniformly).
Watch out for: never assume continuity — monotonicity is DERIVED in step 4 and is all that's needed for the uniform m; justify every squaring (positivity); state the c ≥ 0 codomain argument explicitly.

---

### orbit-forbidden-zone: new
File: `results/imo-2026-05/approaches/orbit-forbidden-zone.md`
Target: same full characterization, both directions.
Technique: **Functional equation + AP-orbit analysis + LEFT-inequality forbidden zones** (the consensus route of all three explorers, openings A–C/3–5).
Skeleton:
  1. Verification (as above) — by SOS identity.
  2. f∘f = 2f − id — by x = f(y) in both inequalities.
  3. h := f − id ≥ 0, h(f(y)) = h(y), fⁿ(y) = y + n·h(y) — by induction + orbit escape.
  4. Left inequality ⇔ (x − f(y))² ≥ 2c(x + f(y)) + c² with c = h(x) − h(y) — by exact expansion (sympy-verified).
  5. Two positive values a < b of h impossible — because the a-orbit's f-values form an unbounded step-a AP that can chase within a of any large point x of the b-orbit, making LHS < a² while RHS ≥ 4(b−a)x → ∞.
  6. Fixed points (h = 0) cannot coexist with h = a > 0 — because step 4 at (u, y₀) forbids u ∈ P from an interval I(y₀) around each fixed point y₀ of length 2·sqrt(4a·y₀ + 2a²) > a (length² − a² = a(7a + 16y₀) > 0, sympy-verified); the step-a orbit can't cross it, so all of P sits above sup I(y₀) > y₀ + a for every y₀ ∈ F; then T = sup F = inf P and squeezing y₀ ↑ T, u ↓ T forces a < 2ε for all ε, i.e. a = 0.
  7. h ≡ c ≥ 0 constant; combine with step 1.
Key lemmas (claim + mechanism):
  - AP-hits-interval: an unbounded increasing AP with step s starting at or below an interval of length > s contains a point of it — because the first term past the left endpoint overshoots by < s < length.
  - P lies strictly above F — because a point of P at or below sup I(y₀) is either inside I(y₀) (direct violation) or its orbit lands in I(y₀).
  - Supremum squeeze — because (T,∞) ⊆ P and F accumulates at T from below, so the gap "u ≥ y₀ + a" collapses a to 0.
Open gaps: GAP 1 (writeup of step 5 with thresholds), GAP 2 (writeup of step 6 incl. AP-hits-interval and (T,∞) ⊆ P).
Cases to cover: {a, b > 0 distinct} vs {0 coexisting with a > 0} vs {h constant} — exactly the trichotomy of steps 5–6; within step 6: u inside I vs u below I.
Watch out for: the chase in step 5 needs the SMALLER step positive — a = 0 is not covered by it, hence step 6 is mandatory, not optional; keep the order (two-valuedness of h is available only after step 5).

---

### right-spreading-fixed-points: new
File: `results/imo-2026-05/approaches/right-spreading-fixed-points.md`
Target: same full characterization, both directions.
Technique: **Functional equation + AP orbits + RIGHT inequality only**: orbit chase via exact expansion for two positive values; fixed-point case via a *spreading* argument (fixed set absorbs a growing neighborhood and swallows the non-fixed orbit). Genuinely different mixed-case mechanism from orbit-forbidden-zone.
Skeleton:
  1–3. Verification, f∘f = 2f − id, h ≥ 0 + orbits — shared with orbit-forbidden-zone (certify once as lemmas, import).
  4. Right inequality expansion: (x + y + α)² − 4x(y + β) = 4y(α − β) + (s + α)² − 4sβ with s = x − y, α = h(x), β = h(y) — sympy-verified.
  5. Two positive values 0 < a < b impossible — because chasing x (step-a orbit) to within [0, a) of y (step-b orbit) gives 0 ≤ −4y(b − a) + (s + a)² − 4sb ≤ −4y(b−a) + 4a² < 0 for y > a²/(b−a).
  6. Mixed case h ∈ {0, a}, a > 0, F, P ≠ ∅ impossible — because the right inequality at (y₀ ∈ F, y ∈ P) gives (y − y₀)² ≥ 4a·y₀, so J(y₀) = (y₀ − 2√(a·y₀), y₀ + 2√(a·y₀)) contains no point of P, hence J(y₀) ⊆ F; the radius 2√(a·y) is bounded below on [y₀, ∞), so F spreads: [y₀, ∞) ⊆ F by a supremum argument; but any p ∈ P has an unbounded orbit inside P that must enter [y₀, ∞). Contradiction.
  7. h ≡ c ≥ 0; combine with verification.
Key lemmas (claim + mechanism):
  - J(y₀) ⊆ F — because (y − y₀)² ≥ 4a·y₀ constrains every element of P, and h is two-valued after step 5, so the excluded points are fixed.
  - F spreads to [y₀, ∞) — because each fixed y pushes F forward by 2√(a·y) ≥ 2√(a·y₀) > 0, so sup{s : [y₀,s) ⊆ F} cannot be finite.
  - Orbit escape — because p + ma → ∞ stays in P yet must exceed y₀.
Open gaps: GAP 1 (chase writeup), GAP 2 (spreading supremum writeup).
Cases to cover: same trichotomy as orbit-forbidden-zone.
Watch out for: in step 5 use the EXACT expansion — the crude bound (x+y+a) ≤ 2y+2a only kills b > 2a (I checked; this is a real trap); the deduction J(y₀) ⊆ F needs two-valuedness, so step 5 must precede step 6.

---

## Rejected / not opened

- **Differentiability route** (computation explorer's d'(y) = 0 argument): assumes regularity the problem doesn't grant — recorded as a trap, not opened.
- **Full Legendre/envelope route** (sup/inf cross-inequality over all x): optimizing the cross bound over x lands exactly at x = f(y2), i.e. it collapses to the chain inequality (*) of chain-lipschitz-squeeze — not a distinct rival.
- **Rational/irrational step casework** (analogy explorer's opening 4): unnecessary — chasing within one step of the smaller AP avoids any rationality split; do not let builders reintroduce it.

## Notes for the reviewer

- chain-lipschitz-squeeze is the strongest: no casework, smallest gaps, and it doubles as the hedge against the (unlikely) failure of the f∘f = 2f − id combination since it only chains one-sided bounds.
- The two orbit approaches share steps 1–3; on first APPROVE of either, certify those as `lemmas/` entries (functional-equation, orbit-invariance, h-nonnegative) for import.
- All three are complete end-to-end attempts at the characterization (verification + uniqueness), differing in the mechanism that kills non-constant h.

## Proposed approaches

- chain-lipschitz-squeeze: new — build this round (highest priority)
- orbit-forbidden-zone: new — build this round
- right-spreading-fixed-points: new — build this round if builder capacity allows, else next round
