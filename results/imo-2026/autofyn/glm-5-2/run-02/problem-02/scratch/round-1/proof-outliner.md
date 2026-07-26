## imo-2026-02

Field note (round 1, fresh workspace — all approaches are `new`). The convergent signal from the three explorer reports is strong and numerics-backed: the target `OM=ON` is equivalent to `O` lying on the perpendicular bisector of `MN` (the midline, ∥ `BC`). Two clean synthetic reformulations follow from this, each suggesting a distinct rival route. The pure coordinate ideal-membership route is DEAD (spurious branches; inside-region hypotheses load-bearing) — do not re-open it as a standalone CAS bash. The "spiral similarity at A sends K→L" claim is FALSE numerically — do not assume it.

---

### antipode-rightangle
: new
Target: `OM = ON` for `O` the circumcentre of `△AKL`, `M,N` midpoints of `AB,AC`.
Framing (1 sentence): The homothety `h` centred at `A`, ratio `1/2`, sends `B→M`, `C→N`, so `OM=ON` ⟺ `h⁻¹(O)=2O−A` lies on the perpendicular bisector of `BC`; but `2O−A` is the antipode `A'` of `A` on `(AKL)` — so prove `A'B=A'C` by chasing the right angles that define `A'`.
Technique: Synthetic angle chase through the diameter; spiral-similarity reading of the three angle conditions as similar triangles; directed angles mod 180. KB: `Synthetic toolkit — spiral similarity`, `circumcentre / perpendicular-bisector characterizations`, `angle chasing`.
Skeleton:
  1. Reduction (equivalence, verified numerically to 1e-12): `OM=ON ⟺ A':=2O−A` lies on `pbis(BC)` ⟺ `A'B=A'C`. Mechanism: `A'−B = 2(O−M)`, `A'−C = 2(O−N)`, so `|A'B|=2|OM|`, `|A'C|=2|ON|`. — by homothety + `A'` is antipode (diameter `AA'`, `O` its midpoint).
  2. Characterise `A'` without `O`: `A' = (line through K ⟂ AK) ∩ (line through L ⟂ AL)`, since `∠AKA'=∠ALA'=90°` (angle in semicircle). — by Thales / angle-in-semicircle.
  3. (Lemma, free from cond. 1 + spiral at `A`): `∠BAK = ∠CAL`, i.e. `AK, AL` are isogonal cevians of `∠A`. — because `∠KBA=∠ACL` plus the shared angle at `A` forces `△ABK ∼ △ACL` (A↔A, B↔C, K↔L); certify the second angle equality from the ray picture (`BK` at angle `α` from `BA`, `CL` at angle `α` from `CA`).
  4. (Lemma) The other two similarities are genuine: `△LBK ∼ △LNC` (L↔L, B↔N, K↔C) and `△LCK ∼ △BMK` (K↔K, L↔B, C↔M). — because `MB∥AB`, `NC∥AC` make `∠LNC=∠(NL,AC)`, `∠BMK=∠(AB,MK)`; the ray parametrisation closes the second angle of each pair. Certify via directed angles, not raw interior angles.
  5. (KEY LEMMA / HARD STEP) `∠A'BK = 90° − ∠C` (and symmetrically `∠A'CL = 90° − ∠B`). — mechanism: combine the right angle `∠A'KA=90°` with the similarity `△LCK ∼ △BMK` (which links `∠CKL`-type angles to `∠BMK=∠γ`) and the isogonality at `A`; the chase passes through `K` and `L` and converts the `γ`- and `β`-data into the constant `90°−C`. Phrased throughout as directed angles mod 180.
  6. Conclude: `∠A'BK = 90°−C` ⟹ `∠A'BC = 90°−∠A−α` (since `∠KBA=α`), and symmetrically `∠A'CB = 90°−∠A−α`; hence base angles of `△A'BC` are equal, so `A'B=A'C`. — by angle chasing.
  7. By step 1, `OM=ON`. — done.
Key lemmas (claim + one-line mechanism):
  - `OM=ON ⟺ A'∈pbis(BC)` — because `A'−B=2(O−M)` and `A'−C=2(O−N)` (homothety by 2 about `A`).
  - `AK, AL` isogonal in `∠A` — because `△ABK∼△ACL` (cond. 1 + ray picture forces the second angle).
  - `∠A'BK = 90°−∠C` — because the right angle at `K` (diameter) plus the similarities at `K` and `L` (conds. 2,3) chase the `β,γ` data into the constant `90°−C`. (THIS IS THE CRUX; numerics robust but unproved.)
Open gaps: step 5 (the `90°−C` chase) is the load-bearing unproved step; steps 3–4's "second angle equality is forced" needs a directed-angle certificate. Builder fills these.
Cases to cover: directed-angle sign conventions; `A'` lies on which side of `AK`/`AL` (pinned by `K∈△BMC`, `L∈△BNC`, `K∈∠LBA`, `L∈∠ACK`).
Watch out for: numpy's `arccos` picks the smaller angle — obtuse angles in the spiral triangles read as supplements; all angle equalities must be directed mod 180. The chase can branch on configuration; the inside hypotheses are exactly what fixes the signs.

---

### power-secant-product
: new
Target: `OM = ON` (whole claim).
Framing (1 sentence): `OM=ON ⟺ pow_{(AKL)}(M)=pow_{(AKL)(N) ⟺ AB·MA'_B = AC·MA'_C`, where `A'_B,A'_C` are the second intersections of `AB,AC` with `(AKL)`; prove that secant-product equality from the three angle conditions via similar triangles / a spiral similarity. (Adapts aimo-0266 / IMO-SL 2009 G2.)
Technique: Power of a point + concyclicity converse; similar-triangle ratio chase. KB: `power of a point (PA·PB=PC·PD converse)`, `similar triangles`, `spiral similarity`.
Skeleton:
  1. Reduction (equivalence): `OM=ON ⟺ pow_{(AKL)}(M)=pow_{(AKL)}(N)`. — because `OM²=R²−pow(M)`, `ON²=R²−pow(N)` (directed power, `R` circumradius of `AKL`).
  2. Expand the powers along the secants: line `AB` meets `(AKL)` at `A` and `A'_B`; `pow(M)=MA·MA'_B=(AB/2)·MA'_B`. Likewise `pow(N)=NA·NA'_C=(AC/2)·NA'_C`. So target is `AB·MA'_B = AC·MA'_C`. — by secant power.
  3. (Lemma) `AK, AL` isogonal in `∠A` (same as antipode route step 3) — gives `△ABK ∼ △ACL`, hence `AB/AC = AK/AL` and an angle relation at `A`. — by spiral similarity at `A` (direction only, NOT `K→L`).
  4. (KEY LEMMA / HARD STEP) Express `MA'_B` and `MA'_C` as ratios involving `AK, AL, BK, CL` (and the `β,γ` data) such that the isogonality of step 3 and the similarities `△LBK∼△LNC`, `△LCK∼△BMK` cancel to give `AB·MA'_B = AC·MA'_C`. Candidate mechanism: the second-intersection chord length `MA'_B` is governed by `∠AKA'_B` (= `∠ALA'_C` by concyclicity on `(AKL)`); translate `MA'_B = (AB·sin∠AKB)/sin∠AKA'_B`-type sine-rule identities and chain with the three similarities. — by sine rule in `△AMA'_B`, `△ANA'_C` + concyclicity on `(AKL)`.
  5. Conclude by step 1. — done.
Key lemmas (claim + one-line mechanism):
  - `OM=ON ⟺ AB·MA'_B = AC·MA'_C` — power of a point at the midpoints along secants `AB, AC`.
  - `MA'_B/MA'_C` ratio identity — sine rule + the three similarities reduce it to `AC/AB`. (CRUX, unproved.)
Open gaps: step 4 — the explicit sine-rule / similar-triangle computation of `MA'_B`, `MA'_C` and the cancellation. Builder fills.
Cases to cover: `A'_B` on the correct ray of `AB` (inside vs outside) — pinned by `K∈△BMC`; directed power signs.
Watch out for: the trap "spiral at A sends K→L" is false; do not use `AK/AL = AB/AC` as `K↔L` correspondence — only as a ratio relation. Watch the sign of `MA'_B` (directed length) carefully.

---

### spiral-compose-midpoints
: new
Framing (1 sentence): Compose the three spiral similarities (centred at `A`, `L`, `K`) into a single spiral (or Möbius) map that swaps the midpoint pair `M↔N` (or sends a known circumcentre to `O`), so that `OM=ON` becomes an "image of a midpoint is a midpoint" statement. (Adapts aimo-0366 / aimo-0389.)
Technique: Spiral-similarity composition; "spiral sim maps midpoints to midpoints and circumcentres to circumcentres." KB: `spiral similarity`, `Miquel point of a complete quadrilateral`.
Skeleton:
  1. Identify the three spiral centres: `S_A` at `A` (sends `BK→CL`, ratio `AB/AC`, rot `∠BAC`), `S_L` at `L` (sends `BK→NC`), `S_K` at `K` (sends `LC→BM`). — by the three angle equalities + `MB∥AB`, `NC∥AC`.
  2. (Lemma) The three spirals compose to a map `Φ` with `Φ(B)=C`-direction-related and `Φ(M)=N`. — because `S_K` sends `M`-related segment `BM` to `LC`, and `S_L` sends `NC` to `BK`-related; the midpoint links `BM=AB/2`, `CN=AC/2` chain the ratios. (UNVERIFIED; the composition order and the exact segment pairs are the open question.)
  3. (KEY LEMMA / HARD STEP) The centre `X` of the composed spiral `Φ` lies on `(AKL)` (or `Φ` maps the circumcircle of a reference triangle to `(AKL)`), so `O` is the image of a known circumcentre. — mechanism (aimo-0389): a spiral similarity sends circumcircles to circumcircles, hence circumcentres to circumcentres. Candidate reference triangle: `△ABM` or `△ABC` itself.
  4. Conclude: `O = Φ(O_0)` for a known circumcentre `O_0` equidistant from `M,N`'s preimages; or `Φ(M)=N` with `X` on `pbis(MN)` so `OM=ON`. — by the image-of-midpoint / image-of-circumcentre property.
Key lemmas (claim + one-line mechanism):
  - The three spiral centres compose to a map `Φ` with `Φ(M)=N` — midpoint-to-midpoint under spiral similarity (chained via `BM=AB/2`, `CN=AC/2`). (UNVERIFIED; the load-bearing conjecture.)
  - `Φ` maps a known circumcentre to `O` — spiral similarities send circumcentres to circumcentres (aimo-0389 crux).
Open gaps: step 2 — identify the exact composition order and segment pairs making `Φ(M)=N`; step 3 — prove the centre of `Φ` lies on `(AKL)` (or pick the right reference triangle). Both speculative; numerics not yet confirming this route. Builder should first verify the composition numerically before committing.
Cases to cover: none beyond configuration signs.
Watch out for: this is the MOST speculative framing — the composition may not close cleanly. Flag to the reviewer as higher-risk. If the composition does not yield `Φ(M)=N` exactly, the approach dies; do not force it.

---

### analytic-branch-cert
: new
Framing (1 sentence): Use the analytic target line `O·(C−B) = (|C|²−|B|²)/4` (A at origin) as the goal, but reach it by reducing the 4-variable angle-ideal to a 2-variable (L-cubic, parameter `t`) identity and certifying divisibility on the correct real branch selected by the inside-region inequalities — NOT a blind ideal-membership (which is dead).
Technique: Coordinate geometry + polynomial ideal reduction (solve e1,e2 linear-in-K for K=B+t·d(L) on the cubic `det(L)=0`; substitute into e3 and the target `P`; verify `P` vanishes on the correct arc). KB: `Coordinates / complex / barycentric`, `Gröbner-basis ideal membership / Rabinowitsch trick`, `resultants`.
Skeleton:
  1. WLOG (similarity): `A=(0,0)`, `B=(4,0)`, `C=(u,v)` (two free params `u,v`; fix `u=1,v=3` for the test certificate, then attempt symbolic in `u,v`). Target polynomial `P := 2·det(K,L)·[O·(C−B) − (|C|²−|B|²)/4]`.
  2. Encode the three angle equalities as directed-angle tangent polynomials `e1,e2,e3`. Note: `e1` degree 2 linear in `K` (given `L`); `e2` degree 3 linear in `K`; `e3` degree 3 quadratic in `K` (only via `kx²+ky²`).
  3. (Reduction) Solve `e1,e2` (both linear in `K−B`) for `K = B + t·d(L)`, valid on the cubic `D(L):=det(coeffs)=0` (degree 3 in `L`). — by 2×2 linear solve + Rabinowitsch.
  4. Substitute `K=B+t·d(L)` into `e3` → quadratic in `t` with coefficients in `L` (on `D(L)=0`); and into `P`. — by substitution.
  5. (KEY LEMMA / HARD STEP) On the cubic `D(L)=0`, `P` is a multiple of `e3_substituted` (i.e. `P ∈ ⟨D(L), e3|_{K=B+t·d(L)}⟩` as a 2-var identity in `(L,t)`). — by polynomial divisibility / gcd check. Verify first numerically on the test triangle (Gröbner in 0.02 s reported), then symbolically in `(u,v,lx,ly,t)`.
  6. (BRANCH SELECTION) The inside-conditions (`K∈△BMC`, `L∈△BNC`, `K∈∠LBA`, `L∈∠ACK`) select the correct real arc of `D(L)=0` (barycentric positivity, sign of crosses/dots). On this arc, `e3=0` picks the correct `t`; the spurious branches (e.g. `K=B`) are excluded. — by inequality analysis / CAD-lite on the arc.
  7. Conclude `P=0` ⟺ `OM=ON`. — done.
Key lemmas (claim + one-line mechanism):
  - `e1,e2` are linear in `K−B`, so `K=B+t·d(L)` on the cubic `D(L)=0` — 2×2 linear solve structure.
  - `P` is divisible by `<D(L), e3|_{K=B+t·d(L)}>` on the correct branch — the 2-var divisibility (the crux; tested true on fixed triangle, unverified in general params).
  - The inside-conditions pick the correct real arc — barycentric positivity + signed-angle tests.
Open gaps: step 5 — general-` (u,v)` symbolic divisibility certificate (only fixed-triangle tested); step 6 — rigorous branch-selection argument (not just numerical). Builder fills; expect a CAS-assisted but human-auditable certificate.
Cases to cover: the spurious branches (K=B trivial; wrong arcs of mod-π) must be enumerated and excluded explicitly.
Watch out for: the DEAD end is `P ∈ <e1,e2,e3>` as a 4-var ideal — that is FALSE (2094 spurious solutions with `P≠0`). This route MUST use the reduced 2-var form + branch selection; do not re-attempt the 4-var ideal membership. Free-parameter symbolic certificate is the risk; if it fails, the route produces a fixed-triangle verification only (not a full proof) — flag honestly.

---

## Build set nomination

Nominate for building this round (3, kept far apart in framing):
- **antipode-rightangle** (synthetic, antipode/perp-bisector-of-BC target; strongest numerics; crux = the `90°−C` chase).
- **power-secant-product** (synthetic, secant-product target; clean reduction + analogous crux aimo-0266; crux = sine-rule cancellation).
- **analytic-branch-cert** (computational, 2-var divisibility on the correct branch; distinct framing, fallback if synthetic chases stall, and a verification backstop).

Hold **spiral-compose-midpoints** out of the build set this round — it is the most speculative (composition not numerically confirmed); flag it for a round-2 explorer to verify the composition `Φ(M)=N` before a builder commits to it.

build set: antipode-rightangle, power-secant-product, analytic-branch-cert
