## imo-2026-02

a-star-cyclicity: new
Target: Prove OM = ON (M,N midpoints of AB,AC; K,L as in statement; O = circumcenter of △AKL).
Technique: Synthetic angle chase + converse of the inscribed-angle theorem (concyclicity).
Skeleton:
  1. Define the angle alphabet α=∠KBA=∠ACL, β=∠LBK=∠LNC, γ=∠LCK=∠BMK; derive the workhorse triangles △BMK=(α,γ,π−α−γ), △CNL=(α,β,π−α−β) and the master relation ∠ACK=α+γ. — by angle arithmetic + condition (i)+(iii).
  2. Construct A* = A+(D−F) (D=midpoint BC, F=foot of altitude from A to BC); equivalently A* = reflection of A across perp-bis(MN). — by elementary coordinate/rectangle argument. [GAP-0]
  3. CRUX: prove A, K, L, A* concyclic by chasing ∠AKL = ∠AA*L (subtend chord AL), with both expressed in terms of (A,B,C,α,β,γ) via sine rule in △BMK, △CNL. [GAP-1,2,3] — by angle chase + sine rule.
  4. Conclude O (circumcenter of △AKL) lies on perp-bis(AA*) = perp-bis(MN), hence OM=ON. — by circumcenter characterization + step 2.
Key lemmas:
  - △BMK has angles (α,γ,π−α−γ) — because MB lies on BA so ∠MBK=∠KBA=α, and ∠BMK=γ by (iii).
  - A, K, L, A* concyclic — because the chord AA* (parallel to BC) subtends the same angle at K as at L, via the common alphabet (α,β,γ) and the midpoint-induced translate A*=A+(D−F).
Open gaps: GAP-0 (clean A* equivalence), GAP-1/2 (formulas for ∠KAL, ∠ALK, ∠AA*L), GAP-3 (the trig identity equating them — the heart).
Cases to cover: none.
Watch out for: directed angles mod π (cyclic quad is not convex); A* is outside △ABC; do NOT use △ABK~△ACL or the A-centered spiral S_A (recorded dead ends).

dilation-equal-power: new
Target: Prove OM = ON.
Technique: Dilation D(A,2) + power of a point (radical-axis / secant computation).
Skeleton:
  1. Apply D = dilation centered A, factor 2: D(M)=B, D(N)=C, D(K)=K*, D(L)=L*, D(O)=O* = circumcenter of △AK*L*. — by similarity.
  2. Reduce OM=ON ⟺ O*∈perp-bis(BC) ⟺ Pow_{(AK*L*)}(B)=Pow_{(AK*L*)}(C). — by similarity + power-of-point definition.
  3. Rewrite the three angle conditions under D, introducing B'=D(B)=2B, C'=D(C)=2C; identify the secant lines BK*, CL* through the circle. [GAP-1] — by angle transport under dilation.
  4. CRUX: compute Pow(B)=BK*·BQ and Pow(C)=CL*·CR (Q,R = second intersections of lines BK*, CL* with circle(AK*L*)) and prove equality via sine rule + (i)-(iii). [GAP-2] — by inscribed-angle theorem + sine rule.
  5. (Fallback) Exhibit a second circle Γ through B,C whose radical axis with (AK*L*) is perp-bis(BC). [GAP-3]
Key lemmas:
  - OM=ON ⟺ Pow_{(AK*L*)}(B)=Pow_{(AK*L*)}(C) — because D is a similarity sending perp-bis(MN)→perp-bis(BC) and O*A=O*B's-difference equals R*.
  - Pow(B)=Pow(C) — because condition (ii) under D becomes ∠L*B'K*=∠L*CK* (chord K*L* seen equally from B' and C), forcing the secant lengths to match via inscribed angles.
Open gaps: GAP-1 (clean transformed conditions with B',C'), GAP-2 (the power computation — the heart), GAP-3 (fallback radical-axis circle).
Cases to cover: none.
Watch out for: B'=2B ≠ original B; power is taken at original B,C but conditions involve B',C' — keep distinct. Different framing from cyclicity (no A*, no concyclicity converse). Verify on isosceles case first.

analytic-resultant: new
Target: Prove OM = ON.
Technique: Cartesian coordinates + tangent-parametrization of K,L by (tα,tβ,tγ) + resultant/Groebner elimination.
Skeleton:
  1. Place A=(0,0), B=(2,0), C=(2p,2q); then M=(1,0), N=(p,q). — by coordinate choice.
  2. Parametrize K,L by ray intersection from B,C,M,N using tangents (tα,tβ,tγ), baking in conditions (i)-(iii). [GAP-1,2] — by linear ray intersection.
  3. Write the two residual polynomial equations n1,n2 (the remaining occurrences of (ii) at B and (iii) at C) via tan(angle)=cross/dot. [GAP-3] — by tangent-of-angle formula.
  4. Solve the 2×2 linear system for circumcenter O (rows are K,L). [GAP-4] — by equidistance from A.
  5. Form T = 2(p−1)Ox + 2q·Oy + 1 − p² − q² (= OM²−ON²); let N_T = numerator after clearing denominators. — by expanding |O−M|²−|O−N|².
  6. CRUX: show N_T ∈ (n1,n2) by resultant elimination / degree-bounded interpolation, generalizing the already-proved isosceles case (p=0,q=1). [GAP-5] — by ideal membership / Groebner basis.
Key lemmas:
  - OM²−ON² = 2(p−1)Ox + 2q·Oy + 1 − p² − q² (linear in O) — because M,N are fixed and the quadratic terms cancel.
  - O is a linear solve (no quadratic) — because A=origin, equidistance from A,K,L gives 2O·K=|K|², 2O·L=|L|².
  - N_T ≡ 0 mod (n1,n2) — because OM=ON is an algebraic identity on the 1-parameter solution curve (verified for isosceles; general case is GAP-5).
Open gaps: GAP-1 (ray orientations — dead end recorded for wrong orientation), GAP-2 (K,L rational expressions), GAP-3 (n1,n2), GAP-4 (O formula), GAP-5 (general-(p,q) elimination — the heart; use degree-bounding+interpolation to avoid the 9-min timeout of naive 5-var lex Groebner).
Cases to cover: isosceles (p=0,q=1) ALREADY PROVED (certified lemma); general scalene is the gap.
Watch out for: orientation/transposition bugs (two recorded); naive 5-var Groebner times out; verify each step numerically before trusting the symbolic reduction.

miquel-spiral: new
Target: Prove OM = ON.
Technique: Miquel point of a complete quadrilateral + spiral/indirect similarity centered at a constructed point (NOT A).
Skeleton:
  1. Observe the four lines AB, AC, BK, CL form a complete quadrilateral; let Mq be its Miquel point. [GAP-1] — by Miquel theorem.
  2. GATE (numerics first): verify CONJECTURE S — does a spiral/indirect similarity with center S₀ (≠A) send (B,K)→(C,L) or (M,K)→(N,L), and does S₀ lie on perp-bis(MN)? [GAP-2] — by numeric test on 2+ triangles.
  3. (S-route-1) If O = S₀: prove O is the spiral center sending K→L (and another pair); conclude |OM|=|ON| from the spiral's defining property. [GAP-3] — by spiral-similarity characterization.
  4. (S-route-2) If Mq lies on perp-bis(MN): prove Mq∈perp-bis(MN) by the Miquel angle-chase using (i)-(iii); relate Mq rigidly to O. [GAP-4] — by Miquel angle chase.
  5. (S-route-3) Find a general indirect-similarity center (candidates: midpoint BC, circumcenter Ω of ABC, midpoint of arc BC) numerically, then prove. [GAP-5] — by indirect-similarity construction.
Key lemmas:
  - The angle chain (α,β,γ) + midpoint structure is the hallmark of a spiral similarity — because a spiral similarity is determined by two point-pairs and a rotation angle, and the equal-angle conditions supply exactly that data.
  - If S₀ is the center of a spiral/indirect similarity swapping B↔C (or M↔N) and K↔L, then S₀ ∈ perp-bis(BC) (or perp-bis(MN)) — because |S₀B|=|S₀C| (resp. |S₀M|=|S₀N|) by the similarity.
Open gaps: GAP-1 (Miquel point identification), GAP-2 (numeric gate — if fails, route dies), GAP-3/4/5 (the three sub-routes).
Cases to cover: isosceles case as sanity check (S-route-3 = reflection over A-bisector there).
Watch out for: A-centered spiral S_A is a RECORDED DEAD END (does not send BK→CL); any similarity here must have center ≠ A. △ABK≁△ACL and △BMK≁△CNL are dead ends — the spiral is NOT witnessed by a triangle similarity. Highest-risk route; if GAP-2 fails, revise back to cyclicity with transformation data as a lemma.

build set: a-star-cyclicity, dilation-equal-power, analytic-resultant, miquel-spiral
