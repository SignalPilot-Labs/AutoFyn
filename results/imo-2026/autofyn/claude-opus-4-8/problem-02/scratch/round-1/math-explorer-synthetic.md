## imo-2026-02 (synthetic / angle-chase / spiral-similarity lens)

### Setup sanity check (numeric, sympy/numpy, done in /home/agentuser/repo scratch)
The three angle equations are only **3 scalar constraints on 4 unknowns** (K has 2
coordinates, L has 2), so for a fixed triangle ABC the admissible (K,L) form a
genuine **1-parameter family**, not a single point. I solved the system with
`scipy.optimize.least_squares` from many random interior seeds (triangle A=(0,0),
B=(4,0), C=(1,3)), filtered to solutions with K strictly inside △BMC, L strictly
inside △BNC, and the two betweenness conditions ("K inside ∠LBA", "L inside
∠ACK") holding (checked via `angle(P,X,Z)+angle(P,Z,Y)=angle(P,X,Y)`). This
produced ~85 genuinely admissible (K,L) pairs sweeping a visible arc. **For every
one of them, OM = ON to ~1e-8 (solver tolerance)** — strong numerical confirmation
of the claim, and confirmation that the theorem is a statement about a whole
*family* of configurations, so any proof must not secretly assume K,L are pinned
down by more than the stated conditions.

Pitfall for future numeric checks: naively solving the angle equalities with
`arccos` (unsigned) finds spurious branches with K,L far outside the triangle
(e.g. K below AB) that satisfy the *unsigned* angle equalities but violate the
containment/betweenness hypotheses — always filter by the "inside" and
"between-the-rays" conditions before trusting a numeric solution.

### Distinct openings

1. **Fixed-line reframing (strongest, recommend leading with this).** OM=ON is
   *equivalent* to O lying on the perpendicular bisector of segment MN. Since M,N
   are midpoints of AB, AC, this perpendicular bisector is a **fixed line ℓ**
   independent of K, L: it is MN⊥, and because M, N are the images of B, C under
   the homothety h(A, 1/2), ℓ is exactly the image of the perpendicular bisector
   of BC under h(A, 1/2) — equivalently, ℓ passes through the point (2A+B+C)/4
   (midpoint of MN) perpendicular to BC. Algebraically (verified by expanding
   OM²−ON²): OM=ON ⟺ (O − midpoint(MN))·(C−B) = 0. So the problem reduces to:
   **as (K,L) ranges over the whole admissible family, the circumcenter O of AKL
   always has the same projection onto the BC-direction, equal to the projection
   of midpoint(MN).** This is a clean invariance target and suggests looking for
   a quantity like "O·(C−B)" that a proof can show equals a fixed constant using
   only the three angle relations — a good organizing principle for whichever
   technique (synthetic, trig, or coordinate) is used to finish.

2. **Equal-power reframing (verified numerically, promising bridge to power-of-a-
   point / radical axis tools).** OM=ON ⟺ M and N have equal power with respect
   to ω := circumcircle(AKL) (trivial since pow(P)=OP²−R²). Since M ∈ AB and
   N ∈ AC, let P = second intersection of line AB with ω (P≠A), Q = second
   intersection of line AC with ω. Then pow(M) = MA·MP (signed), pow(N)=NA·NQ, so
   the target becomes **MA·MP = NA·NQ**, i.e. (since MA=AB/2, NA=AC/2)
   AB·MP = AC·NQ. I verified numerically that P lies on segment MB (strictly
   between M and B) and Q lies on segment NC — i.e. the second intersection of
   AB with ω(AKL) is "past the midpoint, toward B" and symmetrically for AC.
   This is a genuine equivalent target but the location of P, Q still needs a
   synthetic handle from the angle hypotheses (e.g. via pow(B), pow(C) w.r.t. ω,
   or via some circle through B,C tangent/secant to ω) — **this is the load-
   bearing gap** an approach built on this framing must close.

3. **Combinatorial "swap symmetry" of the three angle conditions.** Relabelling
   B↔C, K↔L, M↔N (A fixed) is an involution σ of the *hypotheses*: condition 1
   (∠KBA=∠ACL) is self-paired under σ (maps to itself, just relabeled); condition
   2 (∠LBK=∠LNC) and condition 3 (∠LCK=∠BMK) are σ-images of each other. So the
   whole hypothesis set — and the conclusion OM=ON — is invariant under this
   relabeling. This is *not* a geometric symmetry of a scalene triangle (there is
   no isometry fixing A and swapping B,C unless AB=AC), but it is strong evidence
   that any correct proof should treat B/K/M and C/L/N in a manifestly parallel
   (dual) way, and that the target quantity (e.g. O·(C−B) from opening 1, or
   MA·MP−NA·NQ from opening 2) should be expressible as (expression in B,K,M) −
   (same expression with C,L,N substituted) — i.e. look for a single function
   f(B,K,M) such that the goal is f(B,K,M) = f(C,L,N). This symmetry is a good
   organizing check on any candidate lemma: if a proposed intermediate identity
   is NOT symmetric under this swap, it is very likely not the right lemma (or is
   only "half" of the needed argument).

4. **Two apex-angle conditions look like (but are NOT) spiral similarities —
   ruled out as a shortcut.** Condition 2, ∠LBK=∠LNC, has common apex L
   (triangles LBK and LNC share the angle at L... wait, common vertex is L, rays
   to B,K vs to N,C) — this LOOKS like the spiral-similarity-at-L pattern
   (equal apex angle ⇒ triangles LBK ~ LNC if additionally LB/LN = LK/LC).
   Condition 3, ∠LCK=∠BMK, similarly looks like a spiral similarity at apex K
   (triangles KCL ~ KMB). **I checked numerically and the side ratios do NOT
   match** (e.g. LB/LN ≈ 3.30 vs LK/LC ≈ 5.40; KC/KM ≈ 2.78 vs KL/KB ≈ 2.38), so
   these are single angle equalities only, not full similarities — do not assume
   triangle similarity from these two conditions alone; that is a trap. The
   angle equalities must be combined with the OTHER two conditions (and the
   third one, ∠KBA=∠ACL, which has no common apex at all) via a longer chain,
   e.g. law of sines in several triangles, or auxiliary circle constructions,
   not a single similar-triangle read-off.

5. **Condition 1 as a "directed angle" bridge, not concyclicity.** ∠KBA=∠ACL
   pairs an angle at B (between BA and BK) with an angle at C (between CA and
   CL) — no common vertex, no common segment. I tested several natural
   concyclicity guesses this might encode (B,K,L,C concyclic; A,K,B,M concyclic;
   A,L,C,N concyclic; K,M,L,N concyclic) via the signed Cayley–Menger /
   determinant concyclicity test — **none vanish** (all give nonzero
   determinants of order 1–30 on the test triangle), so none of these four
   points sets are concyclic in general. Likewise BK is **not** tangent to
   ω(AKL) at K, and CL is **not** tangent to ω(AKL) at L (checked
   `(O−K)·(K−B) ≠ 0` and `(O−L)·(L−C) ≠ 0` numerically). These are useful
   negative results — do not waste a round trying to force any of these as a
   cheap intermediate lemma.

### Candidate technique(s)
- Directed-angle chase (mod 180°) combined with the **power-of-a-point /
  radical-axis** toolkit (opening 2) is the most promising purely synthetic
  route, targeting MA·MP = NA·NQ or equivalently pow(M,ω)=pow(N,ω).
- The fixed-line reframing (opening 1) is technique-agnostic and should be
  stated as the actual target regardless of which method finishes the proof
  (synthetic, trig-Ceva/law-of-sines bash, or coordinates) — it turns "prove an
  equality of two lengths to a moving point O" into "show a fixed dot product
  vanishes," which is often easier to attack term-by-term.
- Given how tightly coupled the three conditions are (no simple similar-
  triangle or concyclicity shortcuts — see openings 4,5), a **trig-Ceva /
  law-of-sines system** (writing each of the 3 angle conditions as a sine-rule
  relation in the triangles at B, C, N, M, K, L and eliminating unknowns
  algebraically) is a realistic fallback if the pure synthetic chase stalls;
  this is likely to be a distinct rival approach from another explorer's
  "trig" lens, and it should be seeded independently, not treated as a small
  patch on the synthetic route.

### Cheap-kill candidates
- None of the "one-shot" concyclicity/tangency/similarity guesses hold (see
  point 5) — do not re-check BKLC, KMLN, AKBM, ALCN concyclic, or BK/CL tangent
  to ω(AKL); these are dead ends, verified numerically above.
- Genuine cheap structural fact to use: MN ∥ BC and MN = BC/2 (midline), and
  M,N are the images of B,C under homothety h(A,1/2) — this converts "perp
  bisector of MN" into "homothetic image of perp bisector of BC," which may
  let a proof reuse triangle-ABC-level facts (e.g. circumcenter of ABC lies on
  perp bisector of BC) transported by h(A,1/2).

### Knowledge-base entries to use
- `knowledge_base.md` "Geometry (synthetic & analytic)" section: **power of a
  point (and concyclicity converse PA·PB=PC·PD)**, **spiral similarity**,
  **angle chasing** are explicitly listed and directly applicable (though note
  point 4: spiral similarity does NOT drop out trivially from the given
  conditions — it has to be built, not assumed).
- The KB's "Coordinates / complex / barycentric: place coordinates to exploit
  symmetry" entry is relevant as a fallback/verification technique given the
  swap symmetry found in opening 3 (a symmetric coordinate setup, e.g. with BC
  on the x-axis, would make the σ-swap manifest as x → (const − x) reflection
  and could shortcut the "same fixed projection" claim of opening 1).

### Analogous past problems (cruxes)
`crux_moves_documentation.md` states plainly: **geometry is not yet in the crux
corpus** ("Not in the corpus yet; the problems DB includes geometry problems
with solutions, but no geometry cruxes have been extracted"). So there is
nothing to query for subtopic filtering — confirmed by reading the doc, not
guessed. No analogous crux moves available; rely on `knowledge_base.md` plus
first-principles synthetic/trig work.

### Prior progress
None — `results/imo-2026-02/` is empty (only `approaches/` and `lemmas/`
directories exist, no files). This is round 1 for this problem.

### Dead ends (do not retry)
- Assuming ∠LBK=∠LNC ⟹ △LBK ∼ △LNC (spiral similarity at L) — false, side
  ratios mismatch numerically (see opening 4).
- Assuming ∠LCK=∠BMK ⟹ △KCL ∼ △KMB (spiral similarity at K) — false, same
  reason.
- Assuming any of B,K,L,C / A,K,B,M / A,L,C,N / K,M,L,N are concyclic — all
  fail the determinant concyclicity test on a generic triangle.
- Assuming BK tangent to ω(AKL) at K, or CL tangent at L — both fail
  numerically.

### Small-case / intuition notes (conjectural, numerically supported)
- OM=ON holds across the entire ~85-point sampled family of admissible (K,L)
  for one fixed scalene triangle, to solver precision (~1e-8) — strong evidence
  the statement is true and that it is genuinely a "moving locus" phenomenon:
  O sweeps some curve as (K,L) vary, but always stays on the fixed line
  (perp bisector of MN).
- The second intersection P of line AB with ω(AKL) lands strictly between M
  and B (not between A and M) in the sampled instance, and symmetrically Q
  (second intersection of AC with ω) lands between N and C — this is a
  reproducible pattern worth re-checking on other triangles before leaning on
  it, but suggests P, Q are "far" intersections (close to B, C respectively)
  rather than "near" ones (close to A), which may help identify them
  synthetically (e.g. via power of B or C rather than power of A).
