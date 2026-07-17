## imo-2026-02 — lens: genuinely different framing (avoid the shared scalar-identity wall)

### Context read
All three round-1 approaches (power-of-point-BC, trig-lawofsines, complex-swap-symmetry)
independently derive the SAME free reduction `OM=ON ⟺ pow(B,ω)-pow(C,ω)=(AB²-AC²)/2`
("core identity"), equivalently `AB²(f-½)=AC²(g-½)` where `f=AA'/AB`, `g=AA''/AC` pin
the second intersections `A'=AB∩ω`, `A''=AC∩ω` (`ω=⊙(AKL)`). All three stall on
*injecting* E1-E3 into this identity: power-of-point can't locate `A',A''` synthetically;
trig and complex both reduce to a scalar polynomial identity that is true only on the
"physical" real branch of the constraint variety, and a bare CAS ideal-membership /
Gröbner test fails because of a spurious `γ↦γ+π` (resp. conjugate) branch. I verified this
is a real wall, not a write-up gap: I independently re-derived `f,g` on a fresh numeric
family (triangle `A=(0,0),B=(4,0),C=(1,3)`, `θ∈{0.15,...,0.4}`, solved E1-E4 with
`scipy.fsolve`) and confirmed `AB²(f-½)=AC²(g-½)` to 1e-9..1e-12 — the identity is real,
only the derivation is missing.

### Distinct openings

**1. Inversion centered at A (the genuinely new lever — recommend this as the diversifying approach).**
Since `A∈ω`, inversion `ι` centered at `A` (any radius `r`) sends `ω` to a **line**
`ℓ* = K*L*` (images of `K,L`). Key fact I verified numerically (not just recalled): the
second intersections `A'=AB∩ω`, `A''=AC∩ω` are the *inverse images* of the intersections
of the FIXED lines `AB`, `AC` with `ℓ*`:
`A' = ι(AB ∩ ℓ*)`, `A'' = ι(AC ∩ ℓ*)`.
(Numeric check: computed `K*,L*` via `ι`, intersected line `AB` with `K*L*` to get a
point `P*`, inverted back to `P`; confirmed `pow(P,ω)=0` to `<1e-14` for every sampled
`θ`, i.e. `P=A'` exactly, and matched the previously-found position `f∈(0.5,1)`.)
This converts the two-circle-secant problem ("locate `A'` on `ω`, locate `A''` on `ω`")
into a **single-line problem**: locate ONE line `ℓ*=K*L*` and intersect it with the two
FIXED lines `AB,AC` — one object to characterize from E1-E3 instead of two. The standard
inversion lemma `△AXY ~ △AY*X*` (reversed similarity, ratio `r²/(AX·AY)`) turns each of
E1-E3 (angle equalities at `B`,`L`(apex),`K`(apex) involving `K,L`) into an equivalent
angle/ratio statement about `K*,L*,B*,C*` — untried by any round-1 approach. This is a
concrete, checkable synthetic handle (knowledge_base.md "Synthetic toolkit": *inversion,
power of a point*) that has NOT been tried and does not obviously reduce to the same
polynomial-branch problem, because it trades "circle through 3 points" for "line through
2 points," a strictly lower-complexity object to pin down.
*Honest risk:* pinning `ℓ*` from E1-E3 via the reversed-similarity relations is still
real work — I did not carry it further than the numeric confirmation above — so this
could still bottom out in an equivalent scalar identity. But it is a structurally
different reduction (line-meets-two-fixed-lines vs. circle-meets-two-secants), so it is
unlikely to hit the *literal same* branch-selection wall; worth a full round to see how
far the reversed-similarity relations go before any CAS is needed.
Difficulty: comparable to the existing approaches (needs one nontrivial new synthetic
lemma — the reversed-similarity translation of E1-E3 — then the line-intersection
computation), but genuinely unexplored terrain.

**2. Rational (Weierstrass) reparametrization to kill the spurious branch — a fix, not a new framing; still worth seeding as a 4th approach if the outliner wants a low-risk way to finish trig/complex instead of gambling everything on opening 1.**
Both trig-lawofsines and complex-swap-symmetry independently found that the closing
relation for `γ` (resp. `β`) is **linear in `(cos2γ,sin2γ)`** once expanded (see
trig-lawofsines "Structural fact"). Treating `(cos2γ,sin2γ)` as a point on the unit
circle intersected with that line is exactly what creates the double branch
(`γ` and `γ+π` both solve the doubled-angle system). Instead, substitute
`t=tan γ` (or `tan(γ/2)`) directly into the *original* (non-doubled) closing relation
E3′ before squaring/doubling anything: E3′ is `sinγ·sinC·sin(A+2θ+γ) = 2 sinA·sin(θ+γ)·sin(C-θ-γ)`,
which is a genuine (single-valued) equation in `γ` alone — expand every `sin`/`cos` of
`γ` via `t=tan(γ/2)` (Weierstrass) to get one **rational** equation in `t` of bounded
degree (≤2, since only `sinγ,cosγ` appear, no `sin2γ`), with a UNIQUE root on the
physical branch `γ∈(0,C-θ)` picked out by sign/interval constraints on `t`. Substitute
this rational `t(θ)` (and the mirror `s(θ)` for `β`) into the target identity `(T)` and
simplify — this is a determinate single-branch computation, avoiding the artificial
doubling that created the `γ+π` ghost. This does not evade the "core identity" wall,
it is a mechanical way to *close* it without hunting for a saturation ideal.
Difficulty: routine CAS grind (bounded-degree resultant), medium risk of just being
heavy algebra, but no conceptual gap remains once done.

**3. Ruled out — checked and confirmed dead this round.** Tested whether the spiral
similarity `σ_A` centered at `A` sending `B↦C` (rotation by `∠BAC`, scale `AC/AB`) also
sends `K↦L` (the simplest possible "single global similarity" explanation of E1-E3, which
would trivialize the problem via `M↦N` under the *same* map — since `σ_A` sends midpoint
of `AB` to midpoint of `AC`, i.e. `M↦N`, that would give `OM/ON` related by the
similarity ratio, not literally `OM=ON`, so this was already suspect, but worth a hard
numeric check). **Confirmed false**: `σ_A(K)` differs from `L` by `0.4`–`0.73` (absolute,
on a triangle with `AB≈4`), a large discrepancy across the whole family, not numerical
noise. Do not retry a single spiral similarity centered at `A` mapping `B↦C,K↦L`.

**4. Fixed-line / homothety framing (from round-1 synthetic explorer, still valid, not yet exploited as its own top-level target).** `OM=ON ⟺ O` lies on the perpendicular bisector `ℓ` of `MN`, and `ℓ = h(A,½)(perp-bisector of BC)` since `M,N=h(A,½)(B,C)`. No round-1 approach tried to find a circle or line *naturally forced by E1-E3* whose radical axis (or whose own perpendicular-bisector-type relation) coincides with `ℓ` directly — i.e., skip computing `pow(B),pow(C)` individually and instead look for an auxiliary circle `Γ` through `B,C` such that `ω` and `Γ` share `A` or the E1-E3 conditions force the radical axis of `ω,Γ` to be exactly the perpendicular bisector of `BC` (transported by `h(A,½)`). I did not find such a `Γ` numerically in the time available (checked circle with diameter `BC`, circumcircle of `ABC`: neither has this radical-axis property against `ω`), so this remains speculative — flag as low-confidence, not a concrete lever this round.

### Candidate technique(s)
- **Opening 1 (lead recommendation): inversion centered at A**, `knowledge_base.md`
  "Synthetic toolkit: ... inversion ...". Converts the circle `ω` to a line, and the two
  circle-secant unknowns `A',A''` to intersections of that one line with the two fixed
  lines `AB,AC`.
- **Opening 2: rational (Weierstrass) substitution** to remove the spurious `γ+π`
  branch from the existing trig/complex reductions — a finishing technique for the
  approaches already in the population, not a new top-level approach.

### Cheap-kill candidates
- Spiral similarity at `A` sending `B↦C,K↦L` — **ruled out numerically this round**
  (see opening 3). Do not retry.
- (Carried from round 1, still valid, do not re-check): `BKLC`, `AKBM`, `ALCN`, `KMLN`
  not concyclic; `BK`,`CL` not tangent to `ω`; no side-ratio match for spiral similarity
  at `K` or `L`.

### Knowledge-base entries to use
- "Synthetic toolkit" (§Geometry): **inversion**, **power of a point**, **spiral
  similarity** — inversion specifically is listed but untried by any round-1 approach.
- "Coordinates / complex / barycentric" — underlies opening 2's Weierstrass fix.

### Analogous past problems (cruxes)
Per round-1 explorer, `crux_moves_documentation.md` confirms geometry is **not yet in the
crux corpus** (no geometry cruxes extracted). Re-confirmed: nothing to query for this
domain. No analogous crux moves available.

### Prior progress
Full reduction to the core identity `pow(B,ω)-pow(C,ω)=(AB²-AC²)/2` is proven and
reviewer-certified in `lemmas/reduction-power-to-core.md`, `lemmas/cevian-lengths.md`,
`lemmas/complex-OM-ON-reduction.md`. See `results/imo-2026-02/current.md`. The core
identity itself is confirmed true numerically (multiple independent checks, including
mine this round, to 1e-9..1e-14) but not yet proven from E1-E3 in any approach.

### Dead ends (do not retry)
- Spiral similarity at `A` mapping `B↦C, K↦L` (this round, numeric, false — see above).
- All round-1 dead ends carried forward: no simple concyclicity/tangency (`BKLC`,
  `AKBM`, `ALCN`, `KMLN`, tangency of `BK`/`CL` to `ω`); no spiral similarity at `K` or
  `L` alone (side ratios mismatch); plain Gröbner/ideal-membership on the doubled-angle
  system (spurious `γ+π` branch makes it fail — this is exactly what opening 2 is
  designed to route around).

### Small-case / intuition notes (conjecture, numerically supported)
- Re-verified on an independent triangle (`A=(0,0),B=(4,0),C=(1,3)`, not the one used by
  round-1 explorers) that `OM=ON` and the core identity both hold to `<1e-9` across
  `θ∈[0.15,0.4]`, and that `A'` (`=AB∩ω`) lands strictly between `M` and `B` (`f∈(0.56,
  0.65)` in this sample), matching round-1's finding on a different triangle — this
  "A' beyond the midpoint, toward B" pattern looks structural, not triangle-specific,
  and is exactly the fact opening 1's line `ℓ*=K*L*` must reproduce via `AB∩ℓ*`.
- The inversion-based recomputation of `A',A''` (opening 1) reproduces the same `f,g`
  values as the direct circle-power computation to `<1e-9`, confirming the two
  characterizations agree — opening 1 is a genuine equivalent reformulation, not a
  different (wrong) target.
