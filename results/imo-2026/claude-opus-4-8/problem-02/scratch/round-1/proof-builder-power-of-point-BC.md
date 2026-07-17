# Build report — power-of-point-BC (imo-2026-02), round 1

**Status: partial.**

## Closed rigorously this round
- **Step 1 (L2a):** `OM=ON ⟺ pow(M,ω)=pow(N,ω)`, `ω=⊙(AKL)`, `R=OA`. Full proof.
- **Step 2 (L1):** power along a line is the MONIC quadratic `s(s−a')` in the arc-length
  parameter (clean unit-speed derivation — leading coeff is 1 because `|u|=1`, and `A∈ω`
  kills the constant term). Gives `pow(M)=pow(B)/2−AB²/4`, mirror for `N`. Full proof,
  sympy-cross-checked.
- **Step 3 (L2):** reduction `OM=ON ⟺ pow(B)−pow(C)=(AB²−AC²)/2`. Proven exact; sympy
  confirms `pow(B)−pow(C)−(AB²−AC²)/2 = 2·(pow(M)−pow(N))` identically.
- **L4 (cevian lengths):** `BK=(AB/2)sinγ/sin(θ+γ)`, `CL=(AC/2)sinβ/sin(θ+β)`. Full
  Law-of-Sines proof in △BMK, △CNL; verified exact numerically on the admissible branch.

All of the above is gap-free.

## Remaining gap (the single wall, unchanged from the outline)
**Core identity** `pow(B,ω)−pow(C,ω)=(AB²−AC²)/2`, equivalently pin the second
intersections `A'` (AB∩ω), `A''` (AC∩ω): show `AB²(f−½)=AC²(g−½)` with `f=AA'/AB`,
`g=AA''/AC`. I could NOT close this synthetically. What I established toward it:
- `pow(B)=BA·BA'`, `pow(C)=CA·CA''` (secant power) — so the whole thing is "locate A',A''".
- `A,K,L,A'` concyclic ⇒ inscribed relation `∠(A'A,A'K)=∠(LA,LK)` (confirmed 1e-15) — but
  this is automatic from concyclicity and does NOT inject E1–E3. Insufficient alone.
- Every cheap incidence is dead (re-confirmed numerically): A' not on BK/BL/CK/CL, BKLC not
  cyclic, ω not tangent to BK/CL, AK/BK≠AL/CL.

The honest reading: closing this needs a real Law-of-Sines closure in △BA'K / △CA''L against
L4, or a spiral-similarity/Miquel point tying K,L,A',A'' — a full round of work. The identity
is numerically exact (2.6250 constant across 300+ admissible members of a scalene triangle).

## Spec concerns
- The approach is **sound and not circular** (L1/L2 verified symbolically), but its wall is
  the SAME "locate A',A'' / prove pow(M)=pow(N)" content that every framing ultimately meets —
  the reduction is genuinely free but converts the problem to an identity that is itself the
  crux. No CAS fallback here (purely synthetic target), as the reviewer noted. If next round
  this approach is advanced, the outliner should give the builder a concrete sub-plan for the
  A',A'' pin-down (Law of Sines in △BA'K with the inscribed angle = ∠ALK, closed against L4),
  not just "prove the core." Otherwise it re-stalls at exactly this line.
- Diversity note for orchestrator: this route and the trig route both bottom out on the same
  underlying identity (pow(M)=pow(N)); the complex-swap route is the genuinely different
  object. If both power+trig stall next round on the coupled β,γ,θ system, seed a Miquel /
  spiral-similarity framing (auxiliary point T = 2nd intersection of ⊙(ABK)-type circles) as
  a genuinely new attack on A',A''.

## Promotable lemmas
L1 (power-along-a-line / midpoint-power `pow(M)=pow(B)/2−AB²/4`), L2a, L4 — all proven in
full in the approach file; propose certifying to `results/imo-2026-02/lemmas/`.
