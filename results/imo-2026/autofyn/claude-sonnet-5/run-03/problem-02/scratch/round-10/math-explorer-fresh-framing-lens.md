## imo-2026-02

### Headline: no genuinely new top-level target found; one clean synthetic repackaging discovered, confirmed algebraically equivalent to the existing shared gap (not a bypass)

Per my assigned lens (search for a framing not tried in 9 rounds), I re-derived from
scratch — independent of the coordinate/rotation-parametrization pipeline — the
following clean synthetic reformulation of the target, then checked whether it opens
any new leverage. **It does not**, but it is worth handing to the outliner as a
possibly more tractable *packaging* of the same content, and it is genuinely new (not
in any of the 9 approach files, confirmed by reading all of them).

**The antipode reformulation.** Let ω = ⊙(AKL), O its center. Since A ∈ ω, let
A' be the antipode of A on ω (i.e. A' = 2O − A, so O is the midpoint of AA').
Elementary fact: a homothety h(A, 1/2) sends B↦M, C↦N (since M,N are midpoints of
AB,AC), and homothety scales distances, so for ANY point P, PB=PC ⟺ h(A,1/2)(P) is
equidistant from M,N. Applying this to P = A' = h(A,2)(O) gives, after inverting the
homothety direction: **OM = ON ⟺ A'B = A'C**, i.e. the antipode of A on the circle
AKL lies on the perpendicular bisector of BC. This is elementary and gap-free (pure
homothety algebra, verified both symbolically — with A at the origin, A'=2O,
A'B=A'C ⟺ O·(C−B) = (|C|²−|B|²)/4, matching the known reduction lemma exactly — and
numerically to machine precision on 3 independently-solved valid (K,L) configurations,
script below).

Synthetic content this gives "for free": A' is characterized purely by two right
angles, ∠AKA' = ∠ALA' = 90° (angle in a semicircle) — i.e. A' is the intersection of
the line through K perpendicular to AK and the line through L perpendicular to AL.
So the whole problem reduces to a perpendicularity-based synthetic claim: **the
intersection of (perpendicular to AK at K) and (perpendicular to AL at L) lies on the
perpendicular bisector of BC.**

**Why this does not bypass the gap.** I verified explicitly (algebra above, A at
origin) that "A'B=A'C" is *literally* the identity O·(C−B) = (|C|²−|B|²)/4 — the same
reduction lemma already central to `fixed-point-concyclic`, `coordinate-bash*`, and
(independently) `power-of-point-secants` (which reaches an isomorphic pow(B,ω)−pow(C,ω)
= (AB²−AC²)/2 form via a different route — I confirmed by direct substitution these
three phrasings, "antipode on perp-bisector," "power-of-B/C," and "O·(C−B)=..." are
the same single polynomial identity, not independent). So this is a fourth dressing
of the identical wall, not new leverage — consistent with `power-of-point-secants`'s
own round-1 finding and round-9's `orthogonal-framing-lens` conclusion that the
population has already found (and exhausted) the natural equivalent reformulations.

I also tested, numerically (script below, 3 independently fsolve'd valid (K,L)
configurations on a scalene triangle), whether A' lands on any other recognizable
fixed object as a sanity/exploration check: it is NOT on the circumcircle of ABC
(dist(A', O_ABC) varies across the family, ≠ R_ABC), and (as expected, since it's
algebraically forced to) it does lie exactly on the perpendicular bisector of BC —
no other special locus found.

### Spiral similarity at A — re-tested numerically, confirmed dead (matches round-9's finding)
Tested directly (not from the coordinate pipeline) whether triangles ABK, ACL are
similar via a spiral similarity centered at A (i.e. ∠BAK = ∠CAL and AK/AB = AL/AC).
Neither holds at any of 3 independently-solved valid configurations (angles differ by
up to several degrees, ratios AK/AB vs AL/AC differ by 0.05–0.15) — confirms and
independently reproduces the `spiral-similarity-bootstrap.md` file's own numeric
finding and round-9's dead-end list. **Do not retry a one-shot spiral similarity
centered at A.**

### Isogonal-conjugate structure — considered, no clean lever found
Examined whether hypotheses (∠KBA=∠ACL), (∠LBK=∠LNC), (∠LCK=∠BMK) encode K,L as
isogonal conjugates of some natural point w.r.t. triangles ABK-adjacent or w.r.t.
ABC itself. The mismatched-spoke structure (e.g. hypothesis 2 compares an angle at B
between rays to L,K against an angle at N between rays to L,C — different second
rays, K vs C) is exactly the pattern already flagged as a permanent dead end in the
per-role memory (`NEVER: assume a one-angle-equality hypothesis with mismatched
spokes gives a clean concyclicity fact`, round 2) — I did not find an isogonal
reading that avoids this mismatch. No new isogonal-conjugate lever found.

### Assessment for this round
Consistent with round 9's `orthogonal-framing-lens` conclusion (branch-independence
of the target identity is decisively false; 8+ rounds of increasingly targeted
synthetic searches — nine-point circle, BC-circle, target-circle-itself, inversion at
A, spiral similarity at A/K/L, isogonal conjugation, and now the antipode/power-of-
point repackagings — all converge on the identical algebraic wall). I found **no
genuinely new top-level target this round either.** My own independent contribution
(the antipode-of-A / right-angle-pair reformulation) is real and previously
undocumented in the approach files, and may be worth a small write-up as an
alternative, possibly more geometrically intuitive vehicle for attacking the shared
gap directly (e.g. a builder might find it easier to reason about "two perpendiculars
meeting on perp-bisector(BC)" than about a raw dot-product identity or a Cramer's-rule
determinant) — but it is NOT independent leverage, and should not be sold to the
outliner as a bypass. My recommendation matches round 9's: do not spend a build slot
forcing a "new framing" for its own sake; the population's convergence onto branch
selection is very likely the genuine crux of the problem, and effort is best spent
closing the `Y(γ)<0` / `G2b`-exclusion algebraic sub-case directly (per round 9's
adjudication), possibly reframed in the antipode/perpendicularity language if a
builder finds that clarifies the case analysis.

### Candidate technique(s)
- No new technique beyond what's live. The antipode/right-angle-pair packaging above
  could in principle be a vehicle for a Sturm-sequence or trigonometric-identity
  argument on the SAME target, phrased as "the two perpendiculars from K, L to AK, AL
  meet on the perpendicular bisector of BC" — a builder fluent in synthetic
  perpendicularity chasing (e.g. via projections: BA'² − CA'² = 2(C−B)·A', reducible
  to projecting A' onto line BC) might find this easier to case-split by sign than the
  existing dot-product/Cramer's-rule forms, but it is algebraically the identical
  target, not a reduction in difficulty.
- Per round 9 and round 6: Sturm sequences post-ideal-reduction remain the one
  substantially untried *technique* (as opposed to framing) on the shared target.

### Cheap-kill candidates
None new found this round. (The "spiral similarity at A" and "u→−u reflection of
G2b" cheap-kill candidates from rounds 2/9 remain refuted, reconfirmed here
independently for the spiral-similarity one.)

### Knowledge-base entries to use
- Same as prior rounds: Gröbner-basis ideal membership (Cox–Little–O'Shea); the
  cevians/inversion/spiral-similarity/projective entry (`knowledge_base.md` line
  ~131) — exhaustively searched against this problem across rounds 2,3,5,8,9, and
  again this round with the antipode framing; no new match. No other
  circumcenter/midpoint-specific entry exists in `knowledge_base.md` (grepped for
  "spiral", "isogonal", "antipode", "nine-point", "circumcenter", "midpoint" — only
  the one generic cevians/inversion/spiral-similarity/projective line hits).

### Analogous past problems (cruxes)
None. `crux_moves_documentation.md` has no `geometry` subtopic/domain (confirmed
again, standing finding since round 1) — no crux search is possible for this
problem.

### Prior progress
Unchanged from round 9's adjudication (see `results/imo-2026-02/current.md` round 9
entry): claim (I) fully closed unconditionally; claim (II) closed on the
`Y(γ)≥0` sub-case; `W(r_lo)>0` closed unconditionally in both `Y≷0` cases via the
"evaluate at sibling's zero" technique. The sole remaining shared gap across every
live route is precisely the `Y(γ)<0` sub-case of claim (II), equivalently the
`G2b`-exclusion / three-way `(Y,B2,Z)` sign classification (round 8's proven
structural-equivalence theorem) — no route bypasses this, confirmed yet again this
round from a fresh, independent synthetic angle.

### Dead ends (do not retry)
- Spiral similarity centered at A sending B↦C, K↦L (or B↦K, C↦L) — refuted
  independently this round (3 fresh numeric configurations, angles/ratios both
  mismatched by degrees/tenths, not noise) — matches rounds 2 and 9's findings.
- Antipode-of-A / power-of-point / dot-product-identity — all three confirmed (this
  round, by direct algebraic substitution) to be literally the same single polynomial
  identity; treating any one as independent of the others is a trap.
- Mismatched-spoke angle equalities (hypotheses 2, 3) as clean 4-point-concyclicity
  or isogonal-conjugate facts — re-examined, no new reading found; matches the
  standing round-2 dead end.
- Nine-point circle, BC-circle, target-circle-itself, inversion at A — all previously
  ruled out (rounds 5, 8), not re-litigated in depth this round beyond the antipode
  check (which found no relation to the ABC circumcircle either).

### Small-case / intuition notes
Numerically (3 independently-solved valid (K,L) pairs via least-squares + containment
filtering on a scalene triangle A=(0,0),B=(5,0),C=(1.3,3.7)): OM=ON confirmed to
~1e-7–1e-9 relative precision (solver-limited) in every valid configuration; A' (the
antipode of A on ⊙AKL) confirmed on the perpendicular bisector of BC to the same
precision, and confirmed NOT on the ABC circumcircle (distances to O_ABC vary across
samples, none matching R_ABC). This is consistent with — not additional evidence
beyond — the already-established fact that OM=ON holds only on the correct
(non-extraneous) branch, per round 9's branch-independence refutation.
