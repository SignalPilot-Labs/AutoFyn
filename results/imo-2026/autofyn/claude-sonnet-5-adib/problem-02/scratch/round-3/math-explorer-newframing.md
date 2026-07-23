## imo-2026-02 (new-framing scouting, round 3)

### Context verified
Read `current.md` and all 6 approach files (`coordinate-trig-bash`,
`labeling-duality`, `antipode-perp-bisector`, `two-step-spiral-chain`,
`nine-point-link`, `complex-circle-power`) and the 5 certified lemmas. Confirmed
the diagnosis in the dispatch: three live approaches all provably reduce to
algebraically-equivalent scalar targets (`O_x=p/2`, `pow_Γ(B)-pow_Γ(C) =
(AB²-AC²)/2`, `A*B=A*C`), none derived yet from the three angle hypotheses.
`two-step-spiral-chain` (a genuinely different local rigid-map idea: spiral
similarity BKL~NLC, and concyclicity of {C,K,M,X}) is a confirmed, well-tested
dead end — both mechanisms fail numerically on two independent triangles, with
large (not marginal) deviations. `nine-point-link` is an untested outline
(inversion-at-A idea flagged but not carried through).

I set up an independent numerical rig (fsolve on the 4-equation system for
K,L given free parameter t=∠KBA=∠ACL, filtered to the valid branch by
containment tests) on two scalene triangles and used it to stress-test four
candidate "genuinely different" framings named in the dispatch.

### Framing 1: direct spiral similarity linking K,L to M,N,C bypassing O
**Tested and REFUTED as a fixed rigid map.** This overlaps what
`two-step-spiral-chain` already tried (BKL~NLC) and what it found false. I
additionally tried: ratios AK/AM, AL/AN, AK/AC, AL/AB, AK·AC, AL·AB — none is
constant across t on either test triangle (e.g. T1: AK/AM ranges 1.24→1.52,
AL/AN ranges 1.33→1.66 as t sweeps 0.2→0.5). So there is no fixed-ratio
similarity or homothety tying K (or L) rigidly to M (or N, or C) independent
of t. **Verdict: not a viable bypass — do not pursue a literal spiral
similarity BKL↔(M,N,C); the two natural candidates are both refuted
(one already by `two-step-spiral-chain`, the rest freshly here).**

### Framing 2: reflection symmetry swapping B↔C, M↔N across a fixed axis
**Tested and REFUTED in general.** Idea: if OM=ON with O on the perpendicular
bisector ℓ of MN (a *fixed* line depending only on A,B,C, not on t, since
M,N are fixed midpoints), maybe reflection across ℓ swaps B↔C, K↔L, A↔A. I
constructed ℓ numerically (through the computed O, direction ⊥ MN — since O
is confirmed on ℓ already by the known OM=ON numeric fact, this really is ℓ)
and reflected B, C, K, L, A across it. Result: reflecting B lands at distance
≈0.30 (T1) / ≈0.28 (T2) from C, **not 0** — i.e. **the reflection does NOT
swap B and C** (this constant is t-independent, as expected since ℓ itself
doesn't depend on t — it's a genuine geometric fact about the fixed
configuration, not a numerical artifact). Similarly A does not map to itself,
and K,L are swapped only approximately (residual ≈0.03–0.04, not zero to
solver precision ~1e-9). **Verdict: ℓ is the perpendicular bisector of MN,
not of BC — there is no clean B↔C /M↔N involution fixing the whole
configuration. This framing does not work for a general (non-isosceles)
triangle exactly as stated; a genuine symmetry argument would need a
different (non-rigid, e.g. projective or algebraic) notion of "swap," not a
literal reflection.** This is a clean, useful negative result — it forecloses
a whole family of "find an involution and argue by symmetry" attempts.

### Framing 3: K or L as a named triangle center / trig-Ceva pin-down
**No match found; genuinely open, worth a dedicated attempt.** I checked
whether K, L match simple named-point constructions (ratios AK/AM, AL/AN,
AK/AC, AL/AB, AK·AC, AL·AB, and whether O lies on circle(AKL) through the
circumcenter, orthocenter, or midpoint of BC of ABC) — none is constant or
zero across t. This eliminates the *simplest* guesses but does **not**
eliminate a genuine trig-Ceva-style closed form: the three angle hypotheses
give exactly 3 equations for the 2 unknowns (∠KBA=t is the free parameter,
then ∠LBK, ∠LCK are pinned by ∠LNC, ∠BMK respectively) — a full trig-Ceva /
extended-law-of-sines chase in the four sub-triangles ABK-ish, ACL-ish, BMK,
CNL (using the *actual* triangles formed, e.g. △BMK has known ∠BMK, and
△BNC-adjacent has known ∠LNC) could produce closed-form expressions for AK,
AL, and the angles ∠OAK, ∠OAL *purely in terms of the base triangle's angles
A,B,C and t* — never solving a nonlinear system for coordinates. This is a
plausible route to the same target but via a route (pure trig identity, no
coordinate frame at all) that none of the three live approaches use — they
all eventually fix a coordinate frame (Cartesian with B,C on the x-axis, or
O at the origin). A pure-angle/pure-ratio chase might make the "closing"
algebra (currently stuck for 2 rounds) tractable by working with sines/cosines
of A,B,C,t directly instead of Cartesian coordinates of K,L.

### Framing 4: complex numbers on circumcircle of ABC as ambient frame
**Untested, genuinely unexplored — distinct from `complex-circle-power`**
(which places O, the circumcenter of AKL, at the origin — a different,
already-attempted complex framing). Framing 4 instead places the *original*
triangle's circumcircle as the unit circle, with A,B,C at complex points
a,b,c on |z|=1 (or more generally uses barycentric/trig parametrization
w.r.t. ABC's own angles). Since M=(a+b)/2, N=(a+c)/2 are then simple
combinations of a,b,c, and OM²-ON² expands as a bilinear form in a,b,c and
O (unknown, depends on K,L), this could let the target `OM=ON` be restated
purely in terms of a,b,c and O without ever fixing B,C on an axis — i.e. it
keeps full rotational symmetry of ABC visible throughout, which the existing
Cartesian frame (B,C fixed on the x-axis) breaks immediately. This may or may
not simplify the actual angle-hypothesis translation (K,L still need their
own complex-number formulas from the angle conditions, which is the same
hard part as in `complex-circle-power`) — so it is speculative, but it is a
frame genuinely orthogonal to all three live approaches' frames (Cartesian
B,C-on-axis; O-at-origin; radical-axis/power abstraction). Flag as the
best "genuinely far" opening among the four, since it changes what's held
fixed (the base triangle's own circle, not O or the B,C axis) rather than
just changing which equivalent scalar to chase.

### Cheap-kill / pruning notes
- The reflection-symmetry framing (2) is now cheaply ruled out — do not
  re-attempt "find an isometry that swaps B,C,M,N,K,L" in any form; it's a
  structural fact (ℓ is only the perp bisector of MN, and MN's perp bisector
  passing through the fixed points does not coincide with any natural
  B↔C symmetry axis of the whole figure unless AB=AC).
- The "K,L are named centers" hope (3, simple version) is cheaply ruled out
  by the ratio/distance checks above; only a full trig-Ceva derivation (not
  a lookup) remains viable.
- No cheap parity/pigeonhole argument applies (this is a continuous geometry
  identity, not combinatorial).

### Knowledge-base entries relevant
- "Synthetic toolkit" (spiral similarity, inversion, radical axis, power of
  a point) — already the basis of all 3 live approaches; framing 1 and 2
  exhaust the natural "rigid transformation" ideas from this toolkit and both
  fail, so further mileage from this KB entry likely requires the trig-Ceva
  / extended-law-of-sines angle-chase direction (framing 3) rather than
  another transformation guess.
- "Coordinates / complex / barycentric — rotate axes to align with a key
  line" — directly suggests framing 4 (circumcircle-of-ABC frame) as an
  alternative axis choice not yet tried.
- No entry on trig Ceva explicitly, but "trig cevians (Ceva/Menelaus)" is
  named in the Synthetic toolkit line — supports framing 3 as
  knowledge-base-grounded.

### Crux corpus check
Per `crux_moves_documentation.md`: **"geometry — Not in the corpus yet; the
problems DB includes geometry problems with solutions, but no geometry cruxes
have been extracted."** So the crux corpus has zero geometry entries to query
— there is no analogous crux move to retrieve for this problem. (Confirmed by
reading the subtopics list: only number_theory, combinatorics, algebra are
listed as domains with cruxes.) **No analogous past problem available from
this resource; do not force a match.**

### Small-case / numeric evidence recap (all conjectural, not proofs)
- `powB - powC = (AB²-AC²)/2` holds to machine precision on both test
  triangles across all sampled t (re-confirms `labeling-duality`'s certified
  TI — consistent, not new).
- Reflection of B across ℓ=perp-bisector(MN) lands at fixed nonzero distance
  from C (≈0.30 and ≈0.28 on the two triangles) — confirms framing 2 is
  structurally false, not a near-miss.
- No tested ratio (AK/AM, AL/AN, AK/AC, AL/AB) or named point (orthocenter,
  midpoint BC) is constant/incident across the family — rules out the
  "K or L is a simple named point" shortcut, leaving only a full derivation.

### Prior progress (unchanged from current.md, restated for outliner)
Three certified equivalent reductions exist (`lemmas/coordinate-om-on-reduction.md`,
`lemmas/median-length-power-reduction.md` + `lemmas/radical-axis-form-of-TI.md`,
`lemmas/antipode-reduction.md`), plus the Decoupling Lemma and Sweep Lemma
(`lemmas/decoupling-and-sweep-lemma.md`). All three live approaches are
genuinely stuck on deriving any one of the equivalent targets from the three
angle hypotheses — this is the single shared gap.

### Dead ends (do not retry)
- `two-step-spiral-chain`: BKL~NLC spiral similarity, and {C,K,M,X}
  concyclicity for any natural X — both refuted numerically on two
  triangles, large deviations, confirmed round 1, reconfirmed structurally
  sound reasoning by me this round.
- Reflection across perp-bisector(MN) swapping B↔C (and K↔L, A↔A) — refuted
  numerically this round (new finding, add to dead-end list).
- `antipode-perp-bisector`'s three refuted mechanisms (right-triangle
  identity assuming the conclusion; L as spiral-similarity center for
  (B,K)↦(N,C); Γ tangent to BC / named second intersections) — do not retry.
- Simple named-point identification of K or L (ratios to M,N,C,A;
  orthocenter/midpoint-of-BC lying on circle(AKL)) — refuted numerically
  this round.

### Recommendation for the outliner
Put up **framing 3 (pure trig-Ceva / extended-law-of-sines chase, no
coordinate frame at all — work directly with angles A,B,C of the base
triangle and parameter t)** as the genuinely-far new approach: it changes the
*computational medium* (trig identities in the sub-triangles, not Cartesian
or complex coordinates) rather than proposing yet another equivalent scalar
target. **Framing 4 (circumcircle-of-ABC as ambient complex frame)** is a
credible second candidate if framing 3 stalls — it is a different frame from
all three live approaches (which fix B,C on an axis, or O at the origin) and
preserves the base triangle's rotational symmetry throughout, which may make
the eventual identity more transparent. Framings 1 and 2 (rigid maps /
reflections) are now cheaply exhausted for this problem — do not spend
further builder time on literal spiral-similarity or reflection-symmetry
mechanisms unless a genuinely new candidate map (not a variant of the ones
tested) is proposed.
