## imo-2026-02

### Setup used for numerics
Coordinates: A=(0,0), B=(5,0), C=(1.3,4.1) (triangle 1, scalene) and a second, very
different triangle A=(0,0), B=(7,1), C=(-1,5.5) (triangle 2) for cross-checking.
M,N = midpoints of AB, AC. Parametrized the 1-parameter family by φ = ∠KBA = ∠ACL:
K lies on the ray from B obtained by rotating BA by φ toward the interior (chosen by
picking the rotation sign that points toward C); similarly L on the ray from C
rotating CA by φ toward B. For fixed φ, the remaining two conditions
∠LBK = ∠LNC (angle at N, between NL and NC — **note: NOT the angle at L**, a bug I
had to fix) and ∠LCK = ∠BMK (angle at M, between MB and MK) give 2 equations in the
2 remaining free parameters (distances of K, L along their rays); solved by
`scipy.optimize.fsolve` from a grid of initial guesses, keeping only solutions with
K strictly inside △BMC, L strictly inside △BNC, K inside ∠LBA, and L inside ∠ACK
(checked via signed angles). Scripts: `/tmp/round-1/scratch/probe3.py` (triangle 1,
final working solver), `/tmp/round-1/scratch/probe9.py` (triangle 2, cross-check),
`probe4.py`–`probe8.py` (conjecture tests).

For triangle 1 the valid range is roughly φ ∈ (0°, ~48°) (fsolve/interior checks
fail outside; at φ=50° no valid interior solution was found in the search grid —
plausibly the family's endpoint, not investigated further).

### Main result: OM = ON — CONFIRMED NUMERICALLY (strong evidence)
On triangle 1, φ = 10°,15°,...,45° (8 points), all interior conditions verified
True, and OM = ON to machine precision (|OM−ON| ≤ 2e-15 in every case, e.g.
φ=20°: OM=ON=1.3818899425). On triangle 2 (different shape), φ=5°..30°, same:
diff ≤ 2e-15 in all 6 samples. This is strong numeric confirmation the statement
is correctly transcribed and true; treat as **conjecture verified numerically**,
not a proof.

### Stronger fact than OM=ON: O lies exactly on the perpendicular bisector of MN
Directly checked (O − midpoint(MN))·(N−M) ≈ 1e-15 for every sample on both
triangles. This is the same fact as OM=ON restated (a point is equidistant from M,N
iff it's on the perp bisector), but it's worth flagging to the outliner as the
natural reformulation: **prove O lies on line ⊥ MN through its midpoint**, e.g. by
locating O via two independent characterizations (equal power, or an explicit
second point construction) rather than computing two distances.

### Conjectures tested and their verdicts (triangle 1, several φ)
- **BKLC concyclic** — FALSE. Normalized power of K w.r.t. circumcircle(B,L,C) is
  nonzero and shrinks toward 0 only as φ approaches the family's boundary (~45°+),
  e.g. φ=10°: pow/R²=−0.155; φ=45°: pow/R²=−0.024. Not exactly 0 anywhere in the
  interior tested. Verdict: **fails**.
- **MKLN concyclic** — FALSE similarly (pow(K,MLN)/R² = 0.027 at φ=10° down to
  0.0015 at φ=45°, never exactly 0). Verdict: **fails**.
- **MK = NL** (equal segments) — FALSE but close: MK/NL ranges 0.945 (φ=10°) up to
  0.999 (φ=45°), approaching but not reaching 1. Verdict: **fails** (not an exact
  invariant, just converges near the family boundary — likely coincidental).
- **Circle(AKL) passes through the ABC-circumcenter, orthocenter, or nine-point
  center** — FALSE. Powers of all three points w.r.t. circle(AKL) are nonzero and
  vary with φ (no sign/value pattern suggesting a fixed second intersection).
  Note: O (center of circle AKL) passed very close to the nine-point center of ABC
  at one particular φ (≈35° in triangle 1, |O−ninePt|≈0.005) — this is NOT a
  special identity, just the point where O's φ-traced locus (the perp bisector of
  MN, a fixed line that always contains the nine-point center too) happens to cross
  that already-known point on the same line. Do not chase this.
- **Spiral similarity at A sending B→C, K→L** (i.e. angle BAK = angle CAL and
  AB/AK = AC/AL) — FALSE. angBAK vs angCAL differ substantially (e.g. φ=40°:
  6.4° vs 1.3°); AB/AK vs AC/AL also differ (1.15 vs 1.02 at φ=45°). Verdict:
  **fails**, no simple spiral similarity centered at A relates (B,K) to (C,L).
- **∠MBK = φ and ∠NCL = φ** — TRUE but *trivial*: M lies on ray BA and N on ray CA,
  so ∠KBM = ∠KBA and ∠LCN = ∠LCA by definition of φ. Not a new fact, just confirms
  the setup is consistent.
- **pow(M, circle AKL) = pow(N, circle AKL)** — TRUE to machine precision, but this
  is algebraically identical to OM = ON (pow(P) = |OP|² − R²), so it's not
  independent evidence, just the same fact via a different formula.

### Distinct openings (for the outliner)
1. **Direct power-of-a-point route**: show pow(M, ⊙AKL) = pow(N, ⊙AKL) via two
   secant/chord identities through M (line AB meets ⊙AKL again at some point X,
   giving MA·MX) and through N (line AC meets ⊙AKL again at Y, giving NA·NY), then
   show MA·MX = NA·NY using MA = AB/2, NA = AC/2 and the angle conditions relating
   K, L to M, N (the ∠LNC = ∠LBK and ∠BMK = ∠LCK hypotheses look tailor-made to
   produce such a relation, since they each pair an angle "at M" or "at N" with an
   angle "at B/C" — classic setup for **spiral similarity / same-angle chord
   power** arguments).
2. **Locate the second intersections of AB, AC with ⊙(AKL) and identify them as
   known points** (e.g. show line AB meets ⊙AKL again at a point related to K or to
   the circle (BMC), and similarly for AC) — this would convert the problem into
   showing two power-of-a-point computations agree, using the midpoint relation
   AM=MB, AN=NC explicitly.
3. **The two "linking" angle conditions ∠LBK=∠LNC and ∠LCK=∠BMK strongly suggest
   B,K,M,? and C,L,N,? cyclic-quadrilateral-style angle chasing** (an angle at one
   vertex equated to an angle at a "distant" vertex is the standard fingerprint of
   a spiral similarity or a concyclicity target) — even though naive BKLC/MKLN
   concyclicity tests failed (see above), a *different* 4-point grouping (e.g.
   B,K,N,L or M,K,L,C, or circles (BMK) and (CNL) — not yet tested numerically due
   to time; recommend the outliner or a future round check pow of a point on these)
   may be the real cyclic quadrilateral. This is the most promising unexplored
   angle-chase target.
4. **Direct-computation / coordinate-bash fallback**: since the configuration is a
   genuine 1-parameter family, an outline could set up trig/coordinates explicitly
   (as this script does) and grind OM² − ON² = 0 algebraically as a fallback if
   synthetic routes stall — flagged as a last resort per CLAUDE.md's rigor rules
   (would need to be done exactly, symbolically, not just numerically).

### Candidate technique(s)
Power of a point / radical axis (KB entry: "power of a point (and its concyclicity
converse)"), spiral similarity, angle chasing with directed angles (mod π) to
handle the "K inside angle LBA" / "L inside angle ACK" configuration constraints
rigorously. Given the 1-parameter family and the pairing of angles at M/N with
angles at B/C, spiral similarity centered at K or L (mapping segment through B,M to
segment through C,N or similar) is a strong candidate — not yet tested numerically
in this pass; flag for next round's explorer to check e.g. whether spiral
similarity at K sends B→M, L→C-ish points, or whether K is the center of a spiral
similarity sending BM→ some segment through L.

### Cheap-kill candidates
None obvious — this is a genuine hard configuration; no easy parity/pigeonhole
shortcut applies (continuous geometry problem, answer is an equality not a
combinatorial count).

### Knowledge-base entries to use
- "Synthetic toolkit: angle chasing, power of a point (and its concyclicity
  converse PA·PB=PC·PD), radical axes & radical center, similar triangles, trig
  cevians (Ceva/Menelaus), inversion, spiral similarity, projective ideas."
  (knowledge_base.md, Geometry section, line ~129-131) — directly applicable.
- "Coordinates / complex / barycentric: place coordinates to exploit symmetry"
  (line 137-138) — fallback per opening 4 above.
- Circle/triangle configuration facts (Ptolemy, Simson line, Miquel point) — not
  obviously triggered by this configuration's shape, but Miquel-point-style
  four-circle concurrency is worth a second look if the 4-point cyclic guesses
  above (BKMN-variants) don't pan out.

### Analogous past problems (cruxes)
**None** — `crux_moves_documentation.md` states explicitly: "geometry — Not in the
corpus yet; the problems DB includes geometry problems with solutions, but no
geometry cruxes have been extracted." So the crux corpus cannot be queried for this
problem's domain at all. (The `past_problems_database.json` does contain geometry
problem statements+solutions without extracted cruxes, but per dispatch scope this
lens didn't mine that database line-by-line; a future round could grep
`past_problems_database.json` for geometry problems with midpoint/spiral-similarity
solutions manually, but there is no structured crux-move retrieval path available.)

### Prior progress
None — this is round 1, `results/imo-2026-02/` had no approaches or lemmas yet at
start of this exploration.

### Dead ends (do not retry)
- **BKLC concyclic** — numerically false (see above), don't build an approach on
  this.
- **MKLN concyclic** — numerically false, don't build an approach on this.
- **MK = NL exactly** — numerically false (close but not equal), don't rely on it.
- **Spiral similarity at A taking B→C, K→L** — numerically false.
- **O = fixed point (nine-point center, circumcenter, etc.) as φ varies** — false;
  O genuinely moves along the perpendicular-bisector-of-MN line as φ varies (it is
  NOT constant), so any approach assuming a fixed O is wrong.
- **Naive rotation-direction heuristic bug**: when setting up K, L via "angle φ from
  BA/CA", it is easy to (a) mis-place the angle-equality's vertex (∠LNC is the
  angle AT N, not at L — I initially miscoded this and got solutions failing the
  "L inside triangle BNC" hypothesis; had to fix), and (b) pick the wrong rotation
  sign for the ray, landing on a mirror configuration outside the required
  triangles. Any synthetic argument should very explicitly track directed angles
  and check both interior-triangle and interior-angle hypotheses, since the
  configuration is delicate (about half of "natural" angle equation sign choices
  give an invalid/mirrored configuration that doesn't satisfy the problem's
  interior-position hypotheses).

### Small-case / intuition notes (all labeled conjecture / numeric evidence only)
- OM = ON holds to ~1e-15 across 14 sampled instances over two structurally
  different scalene triangles and φ ranging over roughly the whole valid interval
  — very strong evidence the statement is correct as transcribed.
- O moves continuously along the fixed line = perpendicular bisector of MN as φ
  varies (not fixed, not on a circle so far as tested) — reduce the problem to
  "circumcenter of AKL lies on this fixed line" as an equivalent target.
- The valid range of φ (triangle 1: roughly 0° to ~48°) suggests the family
  degenerates as φ→0 (K,L approach the boundary of their allowed triangles,
  presumably K→ line MC or similar) and at the upper end (K or L likely hits the
  boundary of ∠LBA / ∠ACK containment, or leaves △BMC/△BNC) — not pinned down
  precisely, but the outliner should NOT assume the family extends further than
  numerically observed without separately checking the boundary case is not needed
  for the proof (the proof presumably needs to hold for the whole valid range, and
  boundary behavior is not required in the statement).
