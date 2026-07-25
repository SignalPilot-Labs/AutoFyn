# Lemma: General cut formula (Lemma 0)

**Source.** Certified from `approaches/ngon-arc-reduction.md` (also independently re-derived,
in equivalent form, in `shave-and-halve-forcing.md`, `mod-theta-invariant.md`, and
`maximal-safe-set-fixedpoint.md` — this is the shared kinematic model of one move of the game).

**Statement.** Let a triangle have angles X (at vertex R), Y (at vertex P), Z (at vertex Q),
X+Y+Z=180°. If Mulan cuts from a point P' on side PQ (P' distinct from P and Q) to the
opposite vertex R, and t = ∠PRP' ∈ (0,X) denotes the portion of angle X on the P-side of the
cut, then the two resulting triangles have angle-triples
$$\text{child}_1=(Y,\,t,\,180-Y-t),\qquad \text{child}_2=(Z,\,X-t,\,Y+t),$$
every t ∈ (0,X) is achieved by exactly one choice of P' on the open segment PQ, and every
legal move of the game (cutting from any of the three vertices to the opposite side) is of
this form for some choice of which vertex is R and which of the other two is labelled P
(equivalently Y).

**Proof.** In triangle RPP' (child 1): the angle at P is the original angle Y (unchanged,
since P' lies on segment PQ so ray PP′ = ray PQ); the angle at R is t by definition; the
angle at P' is 180 − Y − t by the triangle angle-sum. In triangle RQP' (child 2): the angle
at Q is the original angle Z (unchanged, same reasoning); the angle at R is X − t (the
remaining part of angle X); the angle at P' is ∠RP'Q, supplementary to ∠RP'P = 180 − Y − t,
i.e. equals Y + t (consistent with 180 − (180−Y−t) = Y+t). As P' ranges over the open segment
PQ, t = ∠PRP' ranges continuously and strictly monotonically over (0,X) (t → 0 as P' → P,
t → X as P' → Q), giving a bijection between legal cut points and t ∈ (0,X). Since Mulan may
choose any of the triangle's three vertices to play the role of R, and having fixed R may
label either of the other two vertices "P", this describes every possible move. ∎

**Status.** No `sorry`/gap; elementary triangle angle-sum and supplementary-angle argument
plus the (standard, monotone) correspondence between a point sliding along a segment and the
angle it subtends at an external point. Certified for reuse by any approach in this
population.
