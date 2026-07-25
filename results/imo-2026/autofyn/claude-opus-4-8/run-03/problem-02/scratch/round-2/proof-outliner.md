## imo-2026-02

Field this round: PRIORITY is closing **coordinate-identity** by installing a rigorous
Orientation Lemma in place of its hand-wavy §3 parenthetical. That lemma is extracted as a
shared certified lemma (`lemmas/orientation-sign.md`) so synthetic-sigma-spiral can import it.
pow-reduction-trig is advanced as genuinely-different-framing insurance (its open gap is a trig
balance identity, a different wall from the orientation wall — the field is NOT collapsed to one
framing). Build set at bottom.

---

coordinate-identity: revise
Target: The problem's actual claim — for the admissible configuration (ABC triangle; M,N midpoints
  of AB,AC; K∈int△BMC, L∈int△BNC with K inside ∠LBA, L inside ∠ACK, and ∠KBA=∠ACL, ∠LBK=∠LNC,
  ∠LCK=∠BMK; O=circumcentre of AKL), prove OM=ON. End to end.
Technique: Complex/coordinate bash (unchanged, verified engine) + a NEW elementary planar-orientation
  Orientation Lemma (signed-area / half-plane + ray-betweenness sign chain) that upgrades the three
  UNSIGNED angle hypotheses to the DIRECTED equations EA=EB=0 (sign ε=+1). No numerics, no global
  continuity/connectedness.
Skeleton (only §3's orientation justification changes; §1,§2,§4,§5 algebraic engine is CERTIFIED-correct
  and imported verbatim):
  1. §1 Reduction OM=ON ⟺ T:=det1−(M_x+N_x)·det2 = 0 — CERTIFIED (equal-height circumcentre reduction,
     lemmas/reduction-OMeqON.md). Import unchanged.
  2. §2 Parametrisation K=B+u·e^{−iθ}(A−B), L=C+v·e^{+iθ}(A−C), u,v>0 — but the CLOCKWISE sign of the
     BA→BK rotation and CCW sign of CA→CL is now JUSTIFIED by the Orientation Lemma (step 4 below,
     part (i)), not asserted "confirmed by /tmp/num.py". Delete the numerical-model sentence.
  3. §3 Decoupling: EA=u·FL(v), EB=v·FK(u), each a quadratic in one variable — algebra CERTIFIED. Keep.
  4. **NEW — Orientation Lemma (the gap-closer).** Replace the parenthetical after (4) [lines 65–68]
     and the numerical sentence after (3) with a proof that EA=0 and EB=0 hold with the + sign, i.e.
     the DIRECTED equalities
        arg((L−B)/(K−B)) = arg((L−N)/(C−N))   [Condition A, gives FL(v)=0]
        arg((K−C)/(L−C)) = arg((K−M)/(B−M))   [Condition B, gives FK(u)=0]
     hold as literal directed-angle equalities (not merely mod π, not merely up to sign). Mechanism in
     Key lemmas below. This is the ONLY new content.
  5. §4 Ideal identity a_K·a_L·T = a_L·QK·FK + QL·FL (pseudo-division remainder exactly 0) — CERTIFIED.
     Import. §5 non-degeneracy a_K·a_L = −¼|AB|²|CA|²W², W a sinusoid with cos-coeff h(p+q)>0 — keep.
  6. Conclude FK=FL=0 ⟹ a_K·a_L·T=0 ⟹ T=0 ⟹ O_x=(M_x+N_x)/2 ⟹ OM=ON. (The §5 continuity-over-θ
     step remains ONLY for the finitely-many a_K·a_L=0 points, which is legitimate; it is NOT the
     orientation step. Keep it but scope it explicitly to the a_K a_L=0 zero-set.)

Key lemmas (claim + the one-line mechanism):

  - **Lemma H (half-plane containment).** If edge PQ of triangle PQR lies on a line ℓ, every point
    strictly interior to △PQR is strictly on the same side of ℓ as R. — because an interior point is a
    strictly-positive barycentric combination αP+βQ+γR (α,β,γ>0, sum 1); its signed distance to ℓ equals
    γ·dist(R,ℓ) with γ>0, same sign as R's.

  - **Lemma R (ray-betweenness).** If X is strictly interior to triangle VYZ, ray VX lies strictly
    between rays VY, VZ; equivalently cross(VY,VX), cross(VX,VZ), cross(VY,VZ) all share one sign.
    — because X−V = β(Y−V)+γ(Z−V) with β,γ>0, so cross(VY,VX)=γ·cross(VY,VZ) and cross(VX,VZ)=β·cross(VY,VZ),
    all a positive multiple of cross(VY,VZ).

  - **Fixed-reference-sign identities (fully quantitative, no case split).**
      N−B = ½(A−B)+½(C−B)  ⟹  cross(N−B, C−B) = ½·cross(A−B, C−B) = ½·cross(BA,BC).
      M−C = ½(A−C)+½(B−C)  ⟹  cross(M−C, B−C) = ½·cross(A−C, B−C) = ½·cross(CA,CB).
    With the standing convention A above BC (h>0, B=(−p,0), C=(q,0)): cross(BA,BC) = (a+p)·0 − h·(p+q)
    = −h(p+q) < 0, and cross(CA,CB) = +h(p+q) > 0. — These pin the reference orientations of △NBC (same
    as △ABC, since cross(NB,NC)=−cross(N−B,C−B)=… same sign as cross(AB,AC)) and △MCB with NO
    continuity/limiting argument: N is a positive combination of A,C so slides along segment AC without
    crossing line-through-B (B∉line AC in a nondegenerate triangle).

  - **Condition-A sign pin (chain for EA's + sign).**
      (i) K∈int△BMC, edge BM⊂line AB (M is midpoint of AB, so B,M∈line AB), opposite vertex C ⟹ by
          Lemma H, K is on the C-side of line AB ⟹ sign(cross(BA,BK)) = sign(cross(BA,BC)) < 0. This
          also fixes §2's clockwise rotation sign of BA→BK.
      (ii) "K inside ∠LBA" ⟹ ray BK between rays BA,BL ⟹ by Lemma R (at B) sign(cross(BK,BL)) =
          sign(cross(BA,BK)) < 0.
      (iii) L∈int△BNC ⟹ by Lemma R at vertex N, ray NL between NB,NC ⟹ sign(cross(NC,NL)) =
          sign(cross(NC,NB)); and cross(NC,NB) = −cross(N−B,C−B) = −½cross(BA,BC) = +½h(p+q) > 0 flipped
          to the (NC,NL) orientation gives sign(cross(NC,NL)) < 0 (builder: carry the two-swap sign
          carefully — target is sign(cross(NC,NL)) = sign(cross(BK,BL)) = −1, matching the numerics).
      (iv) Signs of cross(BK,BL) and cross(NC,NL) agree (both <0) ⟹ the two directed line-angles
          arg((L−B)/(K−B)) and arg((L−N)/(C−N)) have the SAME sign. The UNSIGNED hypothesis ∠LBK=∠LNC
          gives their magnitudes are equal and in (0,π). Same sign + equal magnitude ⟹ literal directed
          equality ⟹ EA = Im[(L−B)(C−N)conj((K−B)(L−N))] = 0 with ε=+1 (not the +π branch). — this is
          the mechanism converting unsigned to directed.

  - **Condition-B sign pin.** The σ-mirror (B↔C, M↔N, K↔L, θ→−θ): K∈int△BMC and "L inside ∠ACK" and
    the M-identity give sign(cross(CL,CK)) = sign(cross(MB,MK)) > 0 (both +1), hence EB=0 with +sign.
    Prove it by applying the SAME two lemmas + the M-identity at C and M — do NOT re-derive from scratch;
    invoke the symmetry so the writeup is half the length.

Open gaps (builder fills): (a) State+prove Lemma H, Lemma R (2–3 lines each, barycentric). (b) The four
  sign-chain steps (i)–(iv) for Condition A with exact sign bookkeeping through each cross-product argument
  swap. (c) The Condition-B mirror via σ. (d) The final "same sign + equal unsigned magnitude ⟹ directed
  equality" step stated explicitly (magnitudes are literal angle values in (0,π), equal by hypothesis).
  (e) Extract steps (a)–(d) as `lemmas/orientation-sign.md` for reviewer certification and reuse.
Cases to cover: none by case split — the fixed-reference-sign identities are parameter-free (hold for ALL
  admissible triangles/θ), so there is a single universal sign. Confirm no reflex-angle reading of
  "K inside ∠LBA" / "L inside ∠ACK": ∠LBA<π always (A,B fixed, K,L on one side), so betweenness is the
  literal reading — state this one-line check.
Watch out for:
  - Do NOT reintroduce any "numerical model confirms the directed equality" sentence — that was the
    exact round-1 overclaim the reviewer rejected. Delete lines 55–56 and 65–68's numerics; replace only
    with the Orientation Lemma.
  - Do NOT cite "collinearity of L,B,K" as Condition A's excluded degeneracy — the reviewer flagged this
    as the WRONG collinearity; the relevant boundary for Condition A's betweenness is L,N,C collinear
    (∠LNC=0), excluded by L∈int△BNC.
  - Keep the §5 continuity argument scoped strictly to the finite a_K·a_L=0 zero-set (legitimate there);
    it must NOT be used to justify orientation.
  - Sign bookkeeping through cross-product argument reversals (cross(NC,NL) vs cross(NB,NC) vs cross(N−B,C−B))
    is where an off-by-a-sign slip hides — the target signs are cross(BK,BL)=cross(NC,NL)=−1,
    cross(CL,CK)=cross(MB,MK)=+1 (analytic explorer verified over 97 interior configs). Match these.

---

orientation-sign (shared lemma target, built INSIDE coordinate-identity's build, certified separately):
  Not a rival whole-problem slug — it is the load-bearing lemma above, to be written as
  `lemmas/orientation-sign.md` and certified by the reviewer so synthetic-sigma-spiral can import it to
  replace its "[Verified numerically]" sign bullets in Steps 3–4. Statement to certify:
  "Under the admissible interiority + betweenness hypotheses, sign(cross(BK,BL))=sign(cross(NC,NL))=−1 and
  sign(cross(CL,CK))=sign(cross(MB,MK))=+1; consequently the unsigned equalities ∠LBK=∠LNC, ∠LCK=∠BMK
  upgrade to the directed equalities arg((L−B)/(K−B))=arg((L−N)/(C−N)) and arg((K−C)/(L−C))=arg((K−M)/(B−M))."
  Mechanism = Lemma H + Lemma R + the two half-vector cross-identities, exactly as in coordinate-identity's
  Key lemmas. Coordinate-free (cross products / signed areas only), so importable by the synthetic route.

---

pow-reduction-trig: advance (insurance — genuinely different framing: trig balance identity, a DIFFERENT wall)
Target: same problem claim OM=ON, via the power-of-a-point/law-of-sines route.
Technique: Lemma 1 origin-at-A reduction (CERTIFIED) + Lemma 2 circumcentre relations + Lemma 3
  sub-triangle law-of-sines lengths/constraints (★),(★★) — all rigorous per round-1 review — reducing to
  the single balance identity E(β)≡0.
Skeleton: import Lemmas 1–3 as reviewed; the remaining step is a from-scratch symbolic derivation of
  E(β)≡0 (currently numeric-only, |E|≤1.4e-13 on three triangles).
Key lemmas:
  - Balance identity E(β)≡0 — because after substituting the (★),(★★) law-of-sines lengths the two powers
    pow(M,ω), pow(N,ω) each expand into a sum of products of sines of the sub-triangle angles; the identity
    should reduce to a product-to-sum / sum-to-product sine collapse. Builder: derive E(β) symbolically
    (sympy: express all lengths via law of sines in △BMK,△BKC and σ-images, expand pow(M,ω)−pow(N,ω),
    simplify to 0) rather than sampling β.
Open gaps: GAP-2 — the symbolic proof of E(β)≡0. This is the whole remaining work.
Cases to cover: none new.
Watch out for: this route does NOT share the orientation wall (its reduction already used the
  law-of-sines magnitudes, unsigned) — keep it live precisely so the field is not one framing. If its
  E(β)≡0 resists a clean sine collapse, that is a separate difficulty, not the orientation gap.

---

Build set: coordinate-identity, pow-reduction-trig

(coordinate-identity is the priority — closing its Orientation Lemma promotes it to solved and produces
lemmas/orientation-sign.md; pow-reduction-trig advances the independent-framing insurance. If capacity
allows a third builder, synthetic-sigma-spiral can advance by importing lemmas/orientation-sign.md to
discharge its Steps 3–4 sign bullets — but its separate crux c·MX=b·NY remains open, so it is lower
priority than the two above.)
