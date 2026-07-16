## imo-2026-02

### Problem recap
Triangle ABC, M = midpoint AB, N = midpoint AC. K inside BMC, L inside BNC. Three angle conditions:
(1) ∠KBA = ∠ACL, (2) ∠LBK = ∠LNC, (3) ∠LCK = ∠BMK. O = circumcenter(AKL). Prove OM = ON.

---

### Distinct openings

**Opening 1 — Power-of-a-point reformulation (most concrete).** OM = ON is equivalent to
pow(B, circumcircle(AKL)) − pow(C, circumcircle(AKL)) = (AB² − AC²)/2.
This was verified numerically to 10 decimal places on multiple scalene triangles. For B outside the circumcircle ω of AKL, the power can be expressed via the second intersection of line AB with ω: pow(B, ω) = AB² · (1 − t_P) where P = A + t_P (B − A) is on ω, and similarly pow(C, ω) = AC² · (1 − t_Q) for Q on line AC ∩ ω. The condition reduces to AB²·t_P − AC²·t_Q = (AB² − AC²)/2, which is a single linear identity in the projections of O onto the lines AB and AC. The outliner should try to derive this identity directly from the angle conditions using law of sines in triangles ABK and ACL.

**Opening 2 — Algebraic reformulation via circumcenter coordinates.** Since O = circumcenter(AKL) satisfies 2(K−A)·O = |K|²−|A|² and 2(L−A)·O = |L|²−|A|², one can write B−C = λ(K−A) + μ(L−A) and the condition OM = ON becomes exactly λ·AK² + μ·AL² = (AB²−AC²)/2. This is a polynomial identity in the coordinates of A, B, C, K, L that the angle conditions must imply. The symmetry of the conditions under (B,M,K)↔(C,N,L) makes the left side transform to −λ·AL² − μ·AK² under this swap, which negates both sides (B²−C² sign flip). This self-consistency is a check but not a proof.

**Opening 3 — Spiral similarity / conformal approach.** The directed angle formulation of condition 2 is: ∠(BL, BK) = ∠(NL, NC) (mod π). The numerical evidence shows that this also equals the angle from line BL to line NL (verified: both equal −75.3°). Thus condition 2 says: ∠(BL, NL) = ∠(BK, NC) as directions. This is the angle-equality condition for a spiral similarity centered at L mapping B→N and K→C (if accompanied by a ratio condition). Similarly condition 3 may encode a spiral similarity centered at K. The route: identify the two spiral similarities from conditions 2 and 3 and compose them; the composition may fix a point or axis that forces O onto the perp bisector of MN.

**Opening 4 — B↔C symmetry and hidden involution.** The angle conditions are fully symmetric under the simultaneous swap (B,M,K) ↔ (C,N,L): conditions 2 and 3 interchange, and condition 1 maps to itself. This means the map sending a valid configuration (A,B,C,K,L) to (A,C,B,L,K) sends the circumcircle of AKL to itself (same triangle AKL vs ALK = same circle). The circumcenter O is fixed. The map sends M→N and N→M. So OM = ON would follow IF we can show this swap is realized by an actual involution (isometry or Möbius map) fixing A and O. For a scalene triangle this cannot be a simple reflection. The route: identify what geometric transformation the conditions impose and show it fixes O while exchanging M and N.

**Opening 5 — Reduction to a single power condition.** The equivalence pow(B) − pow(C) = (AB²−AC²)/2 can be written as: (|BO|² − |CO|²) = (AB²−AC²)/2. By the identity |XO|² = |XA|² + R² + 2(X−A)·(A−O), this expands in terms of AK, AL and their angles with AB, AC. The condition simplifies to a single trigonometric identity that the angle conditions must force. Law of sines in triangles ABK and ACL directly gives AK in terms of α = ∠KBA = ∠ACL.

---

### Candidate technique(s)

Power of a point (primary): show pow(B, ω) − pow(C, ω) = (AB²−AC²)/2 using law of sines applied to the angle conditions. This is the direct analogue of the IMO-SL 2009 G2 strategy.

Law of sines + angle chasing: the three angle conditions give AK/sin α = AB/sin(∠AKB) and similar, expressing the relevant distances and powers in terms of the triangle's angles.

Spiral similarities (secondary): conditions 2 and 3 each encode a spiral similarity relation; composing them may be the key technical step.

---

### Cheap-kill candidates

- Parity/symmetry check: the three conditions are symmetric under (B,M,K)↔(C,N,L); this immediately implies OM = ON IF a symmetric configuration is the only solution. It is NOT (the one-parameter family of solutions is generally asymmetric), so this is not a kill but explains the structure.
- Check if condition 1 alone implies OM = ON: numerically NO. All three conditions are needed.
- Check if M and N lie on the circumcircle of AKL: numerically NO (OM = ON but OM ≠ OA).

---

### Knowledge-base entries to use

- **Power of a point**: `knowledge_base.md` entry: "Synthetic toolkit: power of a point (and its concyclicity converse PA·PB=PC·PD), radical axes." Direct application: compute pow(B, ω) and pow(C, ω) and show they differ by (AB²−AC²)/2.
- **Trig cevians (Ceva/Menelaus)**: angle conditions can be translated via law of sines into ratio conditions, then combined.
- **Circumcircle / inscribed angle theorem**: used in the power-of-a-point computation via second intersections P, Q of lines AB, AC with ω.
- **Spiral similarity**: mentioned under "circle/triangle configuration facts → Miquel point of complete quadrilateral."

---

### Analogous past problems (cruxes)

**1. aimo-0266 (IMO-SL 2009 G2) — closest analogue.** Problem: triangle ABC, circumcenter O, P on CA, Q on AB. Circle k through midpoints of BP, CQ, PQ. Tangency of PQ to k implies OP = OQ. Crux move: tangency implies AP·PC = AQ·QB (equal products), hence P and Q have equal power w.r.t. circumcircle of ABC, hence OP = OQ. The analogy: in our problem, prove that B and C have equal "adjusted power" w.r.t. circumcircle of AKL. The three angle conditions play the role of the tangency condition.

**2. aimo-0878 (IMO-SL 2021 G7, difficulty 8) — structural analogue.** Point D inside ABC with ∠BAD = ∠DAC. Points E on AC, F on AB with ∠ADE = ∠DCB, ∠ADF = ∠DBC. These are angle conditions at D mixing with the sides — exactly the same flavor as our conditions 2 and 3 mixing angles at M, N with the angles at C, B. The proof used: isogonal conjugate Q of D (since D is on the angle bisector, Q = D), concyclicity QBDF and QDEC follows, then TD² = TE·TF = TB·TC via power of a point, then inversion. The analogous crux for our problem may be: identify a "key point" analogous to Q (the isogonal conjugate), establish concyclicity, then use power arguments.

**3. aimo-0525 (USA_TSTST 2017 1) — configuration analogue.** Triangle ABC with M = midpoint AB, N = midpoint AC. A specific point P defined by line MN and the tangent to circumcircle at A, and Q via circumcircle of AEF. Proof: show P and R lie on the radical axis of circumcircle Γ and nine-point circle γ, using PA² = PM·PN (power of point on radical axis). The analogy: M and N appear as midpoints of AB and AC, and the radical axis / power-of-a-point framework is used to derive equidistance.

---

### Prior progress

None (round 1, baseline).

---

### Dead ends (do not retry)

- **Trying to find concyclicity among BKLN, BLNC, BKMC, etc.**: Numerically, NONE of the natural quadruples involving B, C, K, L, M, N are concyclic. Checked: BKLN, BKMC, BLNC, AKBL, AKCL, BKLM, BMNL, CMNK, BMKN, CNLM, AKMN — all have large determinants. Do not pursue this route.
- **Reflection symmetry giving K↔L directly**: The configuration does NOT have a global reflection symmetry (for scalene ABC). The swap (B,M,K)↔(C,N,L) is a "formal" symmetry of the conditions but not an isometry. Do not treat this as a proof by symmetry.
- **Claiming M and N lie on the circumcircle of AKL**: False numerically. OM = ON but OM ≠ OA.

---

### Small-case / intuition notes (all conjectural from numerics)

- **OM = ON confirmed** to 10+ digits for several scalene triangles (AB ≠ AC). The result is real.
- **Equivalent reformulation (computed)**: OM = ON ⟺ pow(B, circ(AKL)) − pow(C, circ(AKL)) = (AB²−AC²)/2. Confirmed: in scalene example A=(1,3), B=(−2,0), C=(3,0): LHS = 2.500000, RHS = 2.500000.
- **One-parameter family**: fixing one coordinate of K (1 DOF removed), the three conditions uniquely determine K,L. So solutions form a 1-parameter family, and OM = ON holds throughout.
- **Condition 1 is essential**: numerically, conditions 2+3 alone do NOT give OM = ON (error ~1.3−2.0). All three conditions interact.
- **Directed angle of condition 2**: ∠(BL, BK) = ∠(NL, NC) also equals the angle from line BL to line NL. Equivalently: ∠(BK, NC) = ∠(BL, NL). This looks like a spiral-similarity angle condition centered at some undetermined point.
- **The perp bisector of MN passes through (2A+B+C)/4** = weighted centroid. O lies on the vertical through this point (when BC is horizontal). Numerically confirmed.
