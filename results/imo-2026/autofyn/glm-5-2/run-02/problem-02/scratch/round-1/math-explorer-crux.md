## imo-2026-02  (IMO 2026 P2, geometry, hard, proof_only)

**Lens:** crux-corpus & knowledge-base retrieval — mine solved-problem cruxes for transferable moves.
Note: the crux DB (`past_crux_moves_database.json`) carries NO geometry cruxes (only NT/combo/algebra; doc states "geometry — not in the corpus yet"). So I mined the **problems DB** (`past_problems_database.json`, 295 geometry problems with full solutions) by keyword on statements+solutions instead. Every borrowed move below is a HINT to adapt, not a citation.

### Load-bearing features of THIS problem
- **Target:** `OM = ON` where `O` = circumcentre of `△AKL`; `M,N` midpoints of `AB,AC`. Equidistance of a circumcentre from two side-midpoints.
- **Midline structure:** `MN ∥ BC`, `MN = BC/2`. `OM=ON` ⟺ `O` lies on the **perpendicular bisector of MN**, a line ∥ the perp-bisector of `BC` (both ⟂ BC).
- **Configuration is angle-defined, not length-defined:** three angle equalities `∠KBA=∠ACL`, `∠LBK=∠LNC`, `∠LCK=∠BMK`, plus containments `K∈△BMC`, `L∈△BNC`, `K∈∠LBA`, `L∈∠ACK`. Three scalar equations for 4 coordinates (K,L) ⇒ a **1-parameter family**; the conclusion is an invariant of that family.
- **Circle (AKL):** its circumcentre O is the target; A is on the circle, so lines `AB` (through A,M) and `AC` (through A,N) are secants of `(AKL)` through A — natural setup for **power of a point** at M and N.

### Numerical confirmation (conjecture, not proof)
Triangle A=(0,0), B=(4,0), C=(1,3). Solved the 3 angle eqs (fixed `kx`, unknowns `ky,lx,ly`) by multistart `fsolve`; obtained a 1-parameter family. For every valid instance with containments satisfied:
- `OM − ON ≈ 1e-10` (machine precision).
- `O` lies exactly on the perp bisector of `MN` (line through `(M+N)/2` ⟂ `MN`); verified `⟨O−(M+N)/2, N−M⟩ = 0`.
- So the **reformulation `O ∈ perp_bisector(MN)` is the live target** — confirmed as conjecture.

### Best retrieved cruxes (problems DB), best-first

1. **`aimo-0266` (IMO-SL 2009 G2).** "Triangle ABC, circumcentre O, P∈CA, Q∈AB; circle through midpoints of BP,CQ,PQ; if PQ tangent to that circle, prove `OP=OQ`." **Crux move:** `OP=OQ` ⟺ powers of P,Q w.r.t. circumcircle of ABC are equal ⟺ `AP·PC = AQ·QB`; then prove that product equality via midline parallels + similar triangles `△APQ ∼ △MKL`. **Why it adapts:** identical conclusion shape (circumcentre equidistant from two points on the two sides from A). Transfer: `OM=ON` ⟺ `pow_{(AKL)}(M) = pow_{(AKL)}(N)`. Secant through M is line `AB` (= line `MA`), meets `(AKL)` at `A` and a second point `A'`; `pow(M)=MA·MA'=(AB/2)·MA'`. Similarly `pow(N)=NA·NA''=(AC/2)·NA''` (line `AC`, second intersection `A''`). So `OM=ON` ⟺ `AB·MA' = AC·NA''`. **The three angle equalities are almost certainly engineered to force exactly this product equality** via a pair of similar triangles / a spiral similarity — this is the single most promising route.

2. **`aimo-0366` (USAMO 2018 5).** **Crux move:** "the centre `M*` of the spiral similarity sending segment `BG*` to `F*D` also maps the **midpoint K of `BG*`** to the **midpoint L of `F*E`**; hence `M*` lies on the circumcircle `KLC`." **Why it adapts:** the midpoint-to-midpoint mapping under a spiral similarity is exactly our `M↔N` situation (midpoints of `AB`, `AC`). A spiral similarity sending one segment to another sends midpoints to midpoints and has its centre on the circle through the two midpoints and the segment-intersection — directly relevant to locating `O` on a perp-bisector / circumcircle through midpoints. Strong candidate to combine with crux 1.

3. **`aimo-0389` (USA-TSTST 2019 5).** **Crux move:** "the spiral similarity sending `△SEF` to `△SBC` maps `H`→`G` on `BC`, and maps the **circumcentre `K` of `△AEF`** to the **circumcentre `O` of `△ABC`**" — i.e. **a spiral similarity maps circumcentres to circumcentres** (it sends circumcircles to circumcircles). **Why it adapts:** our `O` is a circumcentre (of `AKL`). If a spiral similarity centred at a usable point sends some reference triangle to `△AKL` (or to a triangle whose circumcentre is a midpoint / a known point), `O` is the image of a known circumcentre — this could turn `OM=ON` into an image-of-midpoint statement. Worth building a rival approach on.

4. **`aimo-1007` (IMO-SL 2016 G5).** "Circumcentre of `△XSY` is equidistant from `P` and `M`." **Crux move:** translate equidistance to "circumcentre lies on the perpendicular bisector of `PM`"; locate it via nine-point-centre `N`, `QM∥AO`, concyclicity `D,S',S,Q` from a directed-angle chase. **Why it adapts:** same conclusion phrasing ("circumcentre of a constructed triangle is equidistant from two points"); the **perp-bisector reformulation** is the transferable move, plus the directed-angle → concyclicity technique that this problem's three angle conditions invite.

5. **`aimo-0346` (IMO-SL 2010 G5).** **Crux move:** "Let `K` be the reflection of `D` across the midpoint `M`; then `OM` is the perpendicular bisector of `DK`, so `OD=OK`, hence `K` lies on the circumcircle of `BCD`." **Why it adapts:** reflection across a midpoint + "circumcentre lies on the perp-bisector of the joining segment" is exactly the `M`-midpoint mechanism. With `M` midpoint of `AB`, reflecting `B`↔`A` across `M` is free; reflecting `K` or `L` across `M`/`N` and using `O∈perp-bisector` of the image segment is a cheap structural opening.

### Knowledge-base entries to use (named in `knowledge_base.md`, §Geometry)
- **Power of a point + concyclicity converse** (`PA·PB=PC·PD`) — the engine for crux 1: `OM=ON` ⟺ `pow(M,(AKL))=pow(N,(AKL))`.
- **Radical axes & radical centre** — alternative: `OM=ON` ⟺ `M,N` have equal power w.r.t. `(AKL)` ⟺ `MN` is a (piece of a) radical axis; could compare with another circle.
- **Spiral similarity** — cruxes 2 & 3; the natural language for "circumcentre maps to circumcentre" and "midpoint maps to midpoint".
- **Similar triangles / angle chasing** — to convert the three given angle equalities into the product equality of crux 1.
- **Coordinates / complex / barycentric** — the perp-bisector reformulation is a one-line complex-coordinate statement (`|o−m|=|o−n|`); a fallback analytic approach if synthetic stalls.

### Synthesis — what the outliner should build around, and what's a trap
**Build approach around crux `aimo-0266` + perp-bisector reformulation (cleanest):**
- Step 1 (reduction, already conjecture-confirmed): `OM=ON ⟺ O∈perp_bis(MN) ⟺ pow_{(AKL)}(M)=pow_{(AKL)}(N) ⟺ AB·MA' = AC·NA''`, where `A'`/`A''` are the second intersections of `AB`/`AC` with `(AKL)`.
- Step 2 (the real work, open): use the three angle equalities to prove `AB·MA' = AC·NA''`. Likely via exhibiting a spiral similarity (crux 2/3) or a pair of similar triangles that links `MA'` to `NA''`.

**Rival approach — spiral-similarity-maps-circumcentres (crux `aimo-0389`):** exhibit a spiral similarity that sends a triangle with known circumcentre (a midpoint, or `△ABC`'s circumcentre) to `△AKL`, making `O` the image; then `OM=ON` becomes "image of a point is equidistant..." — needs the centre of similitude chosen so that `M,N` are corresponding points. More speculative but genuinely different framing.

**Partial structural opening (note, do not develop):** the condition `∠KBA=∠ACL` is a *directional* spiral-similarity hint at `A` (rotation by `∠BAC` sends the `BK`-direction to the `CL`-direction). Numerics show it does **not** make the spiral sim at `A` send `K→L` (ratio fails: `S(K)` vs `L` off by ~0.25 in a unit triangle) — so it is a *direction* coincidence, not a direct `K→L` map. The other two angle conditions must close the ratio gap. Flag for the outliner: don't assume "spiral sim at A sends K to L" — it doesn't.

**Traps (look similar, won't adapt):**
- **`aimo-0525`, `aimo-0644`** — M,N midpoints of AB,AC + circumcentre, BUT the engine is the **nine-point circle / orthocentre H / Euler line**. Our problem has no orthocentre or altitude structure; nine-point machinery is a trap.
- **`aimo-0801`** — angle bisector + perpendicular bisectors of BC,CA + equal-area conclusion. The angle-bisector/perp-bisector-of-sides structure does not match our three-angle condition; superficial similarity only.
- **`aimo-0152`, `aimo-0203`** — rely on incenter/bisector+tangent or reflection-across-midpoint-of-BC mechanics specific to those configs; the moves (arc-midpoint, tangent-at-A rhombus) don't transfer.

### Distinct openings surfaced (for rival-approach diversity)
1. **Power-of-a-point reduction** (crux `aimo-0266`): reduce `OM=ON` to `AB·MA'=AC·NA''`, prove via similar triangles from the three angles. [synthetic]
2. **Perp-bisector-of-MN as locus of O** (crux `aimo-1007`): show `O∈perp_bis(MN)` by a directed-angle chase producing a concyclicity that pins O onto that line. [synthetic, different target line]
3. **Spiral similarity mapping circumcentres** (crux `aimo-0389`): `O` is the image of a known circumcentre under a spiral sim; equidistance becomes an image statement. [spiral-sim framing]
4. **Spiral-sim centre maps midpoint to midpoint** (crux `aimo-0366`): centre of spiral sim sending one segment to another lies on the circle through the two midpoints; use to locate O on a circle through M,N. [spiral-sim framing, different from 3]
5. **Reflection across midpoint** (crux `aimo-0346`): reflect K/L across M/N, use `O∈perp-bis` of image segment. [cheap structural pruning]
6. **Complex/barycentric coordinates**: `|o−m|=|o−n|` as a one-line target; compute `o` (circumcentre of AKL) in complex coords on a unit circle. [analytic fallback]

### Cheap-kill candidates (before heavy computation)
- **Perp-bisector reformulation** (free): `OM=ON ⟺ O∈perp_bis(MN)`; since `MN∥BC`, this line is `∥` perp-bisector of `BC`. Confirms the target is a single line — focus all angle-chasing on landing O on it.
- **Power-of-a-point at M,N along secants AB, AC** (crux 1): converts the target to a product equality `AB·MA' = AC·NA''` — the natural algebraic form the three angle conditions should feed.
- **Parity/symmetry in the angle chain:** the three conditions pair `B↔C`, `M↔N`, `K↔L` symmetrically across the A-midline — suggests a `B↔C, M↔N` involution (swap the two sides) that fixes O; worth checking whether the configuration is invariant under the swap exchanging the roles (would make `OM=ON` tautological once O is fixed by the swap). Conjecture; not verified.

### Prior progress
- Round 1, fresh workspace: `results/imo-2026-02/current.md` empty, `approaches/` empty, no lemmas. No prior approaches to avoid or build on.

### Dead ends (do not retry)
- None recorded yet (round 1). One self-observed non-result: "spiral similarity centred at A sends K→L" is FALSE numerically (`S(K)≠L`); do not build an approach assuming it. The angle condition only gives a *direction* coincidence, the ratio is forced by the other two conditions.

### Small-case / intuition notes (conjecture, not proof)
- Triangle (0,0),(4,0),(1,3): a 1-parameter family of (K,L) satisfies the three angle eqs + containments; for all instances found, `OM−ON ≈ 1e-10` and `O` lies on `perp_bis(MN)` (line `y = x − 0.5` in this triangle, passing through `(M+N)/2 = (1.25,0.75)` with direction `(1,1)`, i.e. ⟂ to `MN∥BC`).
- Strong evidence the **perp-bisector-of-MN** line is the invariant locus of O (conjecture). The angle conditions are tailored to land O there.
- `MA'`/`NA''` (second intersections of AB/AC with (AKL)) are the load-bearing quantities; the angle chain likely proves `AB·MA' = AC·NA''` (conjecture).
