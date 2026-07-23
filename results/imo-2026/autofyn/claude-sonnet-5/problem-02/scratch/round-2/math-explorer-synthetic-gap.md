## imo-2026-02 (lens: synthetic route to the shared gap TI / O_x=p/2)

### The gap
pow_Γ(B) − pow_Γ(C) = (AB²−AC²)/2, Γ = circumcircle(AKL), from hypotheses
(1) ∠KBA=∠ACL=:θ, (2) ∠LBK=∠LNC, (3) ∠LCK=∠BMK, plus containment/orientation.
Equivalently O_x=p/2 in the coordinate frame B=(-1,0),C=(1,0),A=(p,q).

### Distinct openings tried this pass (all via direct numeric probing of a
genuine solved instance, A=(0.3,1.7), B=(-1,0), C=(1,0), θ=0.4 rad — same
instance style as prior rounds)

1. **Secant-through-A idea.** pow_Γ(B) can be computed as the signed product
   BA·BA′ where A′ is the second intersection of line BA with Γ (A∈Γ
   already). Computed A′, C′ (second intersection of CA with Γ) numerically:
   neither coincides with any named point (not M, not N, not C, not B) —
   dist(A′,N)=1.25, dist(A′,C)=1.67, no match. **Ruled out**: there is no
   "free" identification of the second secant point with a hypothesis point;
   this route needs the inscribed-angle theorem on Γ to *locate* A′, which in
   turn needs angles of triangle AKL (∠AKL, ∠ALK) that are not directly
   given — matches labeling-duality's own conclusion that this stalls.

2. **M, N on Γ?** Checked directly whether M or N lie on Γ (which would make
   pow_Γ(B)=BA·BM=2BM² trivially, closing TI immediately for that case).
   **Refuted numerically**: |OM|−R = |ON|−R = −0.296 (nonzero, and the two
   being *equal* is just OM=ON restated, not new information). So Γ does
   **not** pass through M or N — this "too easy" idea is dead.

3. **Spiral similarity at L sending B→N, K→C** (motivated by condition (2)
   ∠LBK=∠LNC being the AA "angle-at-the-image-vertex" half of the spiral
   similarity criterion). Checked the OTHER required angle pair
   ∠BLK vs ∠NLC and the ratio LB/LN vs LK/LC directly:
   ∠BLK=11.84°, ∠NLC=138.04° (not equal, not even supplementary in the
   useful sense), LB/LN=3.195, LK/LC=2.424 (not equal). **Refuted
   numerically** — this is the same mechanism already recorded as dead in
   current.md's "two-step-spiral-chain" entry (BKL~NLC); this pass
   independently re-confirms it with fresh numbers on a different instance.
   Do not resurrect it.

4. **Spiral similarity at K sending C→M, L→B** (the mirror-pattern guess
   from condition (3), ∠LCK=∠BMK). Same test: ∠CKL=12.33° vs ∠MKB=125.92°
   (wildly unequal), KC/KM=2.81 vs KL/KB=1.59 (unequal). **Refuted.** This
   is close to (likely identical in spirit to) the "concyclicity through
   C,K,M plus a 4th point" mechanism already ruled out in current.md — do
   not re-attempt this exact single-circle/single-spiral shape either.

5. **Direct concyclicity checks** B,N,K,L and C,M,K,L (determinant test):
   both nonzero (0.73, 0.38) — not concyclic. So no simple 4-point circle
   through {B or C, M or N, K, L} exists either.

### What remains promising (not yet tried, worth the outliner's attention)

- **Two-hop / chained construction, not a single circle.** Since every
  *single*-circle or *single*-spiral-similarity guess built directly from
  one hypothesis angle-pair fails, the mechanism connecting (2) and (3) to
  TI likely requires **composing** two auxiliary maps/circles (one governed
  by (2) near L, one by (3) near K) through an intermediate point — e.g. a
  Miquel point of the "quadrilateral" B,M,N,C together with K,L, or the
  radical center of Γ with two secondary circles ω_K (through K tied to
  condition 3) and ω_L (through L tied to condition 2). This is a genuinely
  different shape from the two refuted single-hop guesses and has not been
  tested.
- **Law-of-sines chase using the shared θ.** Condition (1) fixes a single
  parameter θ shared by both ∠KBA and ∠ACL. In triangle BMK, the extended
  law of sines gives BK/sin∠BMK = BM/sin∠BKM; condition (3) says ∠BMK=∠LCK,
  so sin∠BMK=sin∠LCK, giving a relation BK·sin∠LCK = BM·sin∠BKM. Likewise
  for CNL via condition (2). These two sine relations, combined with θ from
  (1) via triangle ABK (angle θ at B) and triangle ACL (angle θ at C), may
  be the right way to extract BK, CL (hence eventually pow_Γ(B), pow_Γ(C))
  as explicit trig functions of θ, β=∠ABC, γ=∠ACB, without ever solving the
  full nonlinear system for K, L in closed form. Not attempted numerically
  or symbolically this pass — flagged as the most promising untried
  synthetic lever.
- **Radical axis of Γ and circumcircle(ABC).** Not tested this pass. Since
  TI is a statement about pow_Γ at B and C specifically (vertices of ABC),
  and the circumcircle Ω of ABC passes through both B and C with pow_Ω(B)=
  pow_Ω(C)=0 trivially, the *difference* pow_Γ(B)−pow_Γ(C) equals
  [pow_Γ(B)−pow_Ω(B)] − [pow_Γ(C)−pow_Ω(C)], i.e. it is controlled by how
  far B, C are from the radical axis of Γ and Ω (a fixed line, independent
  of K,L once Γ is fixed). This reframing might make (AB²−AC²)/2 emerge
  naturally if the radical axis of Γ,Ω can be located via A (both circles
  pass through A, so the radical axis is the line through A perpendicular
  to line O–O_Ω — i.e. the radical axis is COMPLETELY determined once you
  know the direction O_Γ O_Ω, i.e. really just need one more point on it,
  or the perpendicular direction). Worth a quick symbolic check next round.

### Candidate technique(s)
Power of a point / radical axis machinery (knowledge_base.md "Synthetic
toolkit": power of a point, radical axes & radical center, spiral
similarity) remains the right family, but a **single** application (one
secant, one spiral similarity, one concyclicity) is not enough — confirmed
again this pass on top of the prior round's confirmation. The unexplored
lever is a **two-step composition** (radical center of three circles, or
chained spiral similarities via an intermediate point) or a **trig/law-of-
sines derivation via the shared parameter θ** that computes BK, CL, hence
pow_Γ(B), pow_Γ(C), explicitly rather than seeking a slick synthetic
identification.

### Cheap-kill candidates
None new found beyond what's already ruled out (see Dead ends). No parity/
pigeonhole applicable — this is a continuous configuration problem.

### Knowledge-base entries to use
"Synthetic toolkit" (power of a point + concyclicity converse, radical axes
& radical center, spiral similarity) — knowledge_base.md lines ~129-131.
No other KB entry (Ptolemy, Simson, Miquel of complete quadrilateral,
inversion) has an obvious direct fit yet, though the classical "Miquel
point of a complete quadrilateral" entry is worth trying against the
four lines BK, BM(=BA), CL, CN(=CA) as the two-hop idea above.

### Analogous past problems (cruxes)
None. Confirmed via crux_moves_documentation.md: the corpus covers only
`number_theory`, `combinatorics`, `algebra` domains (2434 cruxes total,
0 geometry) — there is no geometry subtopic to filter by, so no crux can be
genuinely analogous to this circle/power-of-a-point configuration. Do not
force a match.

### Prior progress
See current.md: two independent, reviewer-certified equivalent reductions
(labeling-duality's power-of-a-point identity TI; coordinate-trig-bash's
O_x=p/2 + explicit circumcenter formula + Gröbner-basis negative result)
both converge on the same single open gap described above. Nothing in this
pass closes it, but it adds two new confirmed-refuted mechanisms (items 3-4
above, extending the existing two-step-spiral-chain dead end with fresh
numeric evidence on a different instance) plus one new negative check
(item 2, M/N ∉ Γ) and two untried, more promising directions (radical axis
of Γ vs circumcircle(ABC); law-of-sines chase via shared θ).

### Dead ends (do not retry)
- Spiral similarity / concyclicity B,K,L,N with center/pivot L sending B→N,
  K→C (this pass's items 3, and prior round's two-step-spiral-chain
  BKL~NLC): refuted twice now, independently, on different instances.
- Mirror spiral similarity / concyclicity C,K,L,M with pivot K sending
  C→M, L→B (this pass's item 4, closely related to prior round's
  "concyclicity through C,K,M plus a 4th point"): refuted.
- M, N lying on Γ (this pass, item 2): refuted — would have made the
  secant-through-A idea trivial but does not hold.
- Direct concyclicity of {B,N,K,L} or {C,M,K,L} as 4-point circles: refuted
  by determinant test.
- (Carried over from current.md) Pure ideal-membership / Gröbner-basis
  proof of O_x=p/2 from the three raw angle-equality polynomials alone:
  proven to fail (nonzero remainder) — the containment/orientation branch
  must be isolated by other means, not by algebra on the equalities alone.

### Small-case / intuition notes
All numeric evidence (this pass's one solved instance, consistent with
prior rounds' ~35 test points across 4 triangles) continues to support
OM=ON / O_x=p/2 / TI holding on the genuine branch — this is solid
confirmatory evidence for the claim itself (conjecture-grade, not proof),
but does not by itself indicate *which* synthetic mechanism proves it. The
consistent pattern across all refuted single-hop guesses (angle equal but
the companion angle/ratio wildly unequal, e.g. 11.8° vs 138.0°) suggests
the true mechanism is not a "nearby" spiral similarity at all, but
something that uses the *specific* value of θ (shared between K and L via
hypothesis (1)) in an essential, non-local way — reinforcing the law-of-
sines-via-θ direction as more promising than further local-concyclicity
guessing.
