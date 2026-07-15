## imo-2026-02

### Problem restatement
Triangle $ABC$, $M = $ midpoint $AB$, $N = $ midpoint $AC$. Points $K$ inside $\triangle BMC$, $L$ inside $\triangle BNC$ with:
- (C1) $K$ inside $\angle LBA$, $L$ inside $\angle ACK$
- (C3) $\angle KBA = \angle ACL$ (call this $\alpha$)
- (C4) $\angle LBK = \angle LNC$
- (C5) $\angle LCK = \angle BMK$

$O = $ circumcenter of $\triangle AKL$. Prove $OM = ON$.

---

### Distinct openings

**Opening A — Power-of-a-point reduction:**
$OM = ON \iff \text{pow}(M, \odot AKL) = \text{pow}(N, \odot AKL)$.  
By the midpoint power formula (parallelogram law applied to $OM^2$): for any midpoint $M$ of $AB$ with circumcircle $\omega$ of $AKL$:
$$\text{pow}(M, \omega) = \frac{\text{pow}(B, \omega)}{2} - \frac{AB^2}{4}$$
(since $|MO|^2 = (|AO|^2 + |BO|^2)/2 - |AB|^2/4 = (R^2 + R^2 + \text{pow}(B))/2 - AB^2/4$ — then subtract $R^2$). Similarly for $N$ with $C$. Therefore:
$$OM = ON \iff \text{pow}(B, \odot AKL) - \text{pow}(C, \odot AKL) = \frac{AB^2 - AC^2}{2}$$
equivalently $OB^2 - OC^2 = (AB^2 - AC^2)/2$. **Numerically confirmed** for all tested scalene triangles and $\alpha$ values (errors $< 10^{-9}$). This is the cleanest single reformulation — the whole proof reduces to establishing this one identity.

**Opening B — Antipode characterization (geometric reformulation):**
Let $A' = 2O - A$ be the antipode of $A$ on $\odot AKL$ (diametrically opposite $A$). Then:
$$OM = ON \iff A'B = A'C \iff A' \text{ lies on perp bisector of } BC.$$
This follows from expanding $|2O - A - B|^2 = |2O - A - C|^2$, which gives $(4O - 2A - B - C) \perp (C - B)$, i.e., $O$ lies on the perpendicular to $BC$ through the midpoint of $MN$ (= midpoint $(2A+B+C)/4$). **Numerically confirmed:** the $x$-coordinate of $A'$ exactly equals the midpoint of $BC$ in all tested configurations. The point $A'$ is characterized by $\angle AKA' = 90°$ and $\angle ALA' = 90°$ (angles in the semicircle over diameter $AA'$), i.e., $A'$ is the intersection of:
- the line through $K$ perpendicular to $KA$, and
- the line through $L$ perpendicular to $LA$.

The goal becomes: **the unique intersection of these two perpendiculars is equidistant from $B$ and $C$.**

**Opening C — Derived angle equality (bridge from conditions to proof):**
From conditions (C3) and (C5) alone one can derive:
$$\angle CKM = 180° - \angle BAC - \alpha$$
Proof: In $\triangle AKM$, $\angle KMA = 180° - \epsilon$ (supplement of $\angle BMK = \epsilon$), and $\angle MAK = \angle BAK$; so $\angle AKM = \epsilon - \angle BAK$. In $\triangle AKC$, $\angle AKC = 180° - \angle ACK - \angle KAC = 180° - (\alpha + \epsilon) - \angle KAC$. Then $\angle CKM = \angle AKC + \angle AKM = 180° - \alpha - (\angle KAC + \angle BAK) = 180° - \alpha - \angle BAC$. Similarly (by symmetry of (C3) and the coupling in (C4)): $\angle BLN = 180° - \angle BAC - \alpha = \angle CKM$. This is a proved, non-obvious angle equality available to any proof strategy.

**Opening D — Trig-cevian / law of sines cascade:**
Express $OB^2 - OC^2$ directly via the sine rule. Since $O$ is the circumcenter of $AKL$, the key formula (from Opening A) is:
$$OB^2 - OC^2 = \text{pow}(B) - \text{pow}(C) = BA \cdot BX - CA \cdot CY$$
where $X$ (resp. $Y$) is the second intersection of line $AB$ (resp. $AC$) with $\odot AKL$. Since $A$ is on $\odot AKL$, by the inscribed angle theorem:
$$\angle XLK = \angle XAK = \angle BAK, \quad \angle YKL = \angle YAL = \angle CAL.$$
Express $BX$ using law of sines in $\triangle ABX$ and the circumradius $R$ of $AKL$; express $CY$ similarly. The ratio $BX/BA$ involves $\sin(\angle BAK) / \sin(\angle AKB)$, which is related to conditions (C3)–(C5) through the angles $\alpha$, $\epsilon$, $\delta$.

**Opening E — Projective / spiral similarity (cross-ratio):**
The "crossing" structure of conditions (C4)–(C5) — angle at $B$ involves $N$ (midpt $AC$), angle at $C$ involves $M$ (midpt $AB$) — suggests a spiral similarity or projective duality is encoded. Specifically, the coupling $(K, B, M) \leftrightarrow (L, C, N)$ via (C5) and the coupling $(L, B, K) \leftrightarrow (L, N, C)$ via (C4) hints at a transformation exchanging the $(B, M)$-side data with $(C, N)$-side data. If a spiral similarity $\sigma$ can be found mapping $(B, K, M)$ to $(C, L, N)$ (in some order), then $\sigma$ would preserve circumcircle properties and directly force the power identity. (Not yet verified — a promising candidate for investigation.)

---

### Candidate technique(s)

- **Power of a point** (primary): the reformulation $\text{pow}(B) - \text{pow}(C) = (AB^2-AC^2)/2$ is the load-bearing step. See knowledge_base.md "Synthetic toolkit" entry.
- **Circumcircle / inscribed angle / diameter properties**: the antipode $A'$ with $\angle AKA' = \angle ALA' = 90°$ encodes the key right-angle conditions. Angles in a semicircle.
- **Midpoint power formula** (parallelogram law): $|MO|^2 = (|AO|^2 + |BO|^2)/2 - |AB|^2/4$, a standard identity.
- **Law of sines** in subtriangles $ABK$, $ACL$, $BMK$, $CLN$ to express distances and angles.
- **Trig cevian / angle chasing** to connect conditions (C3)–(C5) to the power identity.

---

### Cheap-kill candidates

- **Symmetry check (isoceles $AB = AC$):** When $AB = AC$, by the symmetry of conditions (C3)–(C5), $K$ and $L$ are reflections across the axis, so $O$ lies on the axis of symmetry, giving $OM = ON$ trivially. This is consistent but doesn't prove the general case.
- **Power parity:** The identity $\text{pow}(B) - \text{pow}(C) = (AB^2-AC^2)/2$ is a linear relation in $O$; it says $O$ lies on a specific hyperplane. The three conditions (C3)–(C5) constrain $K$ and $L$ to a $0$-parameter family (for each $\alpha$), so checking the identity on this family is well-defined.

---

### Knowledge-base entries to use

1. **"Synthetic toolkit"** — power of a point ($PA \cdot PB = PC \cdot PD$ and its concyclicity converse); radical axes and radical center; the formula relating power to center distance $\text{pow}(P) = |PO|^2 - R^2$.
2. **"Circle/triangle configuration facts"** — Ptolemy, Miquel point, Simson line. The antipode $A'$ over diameter $AA'$ gives the Simson line = line $KL$ (degenerate but relevant).
3. **"Coordinates / complex / barycentric"** — place coordinates to reduce to the identity $(4O - 2A - B - C) \perp (C - B)$.
4. **"Trig identities"** — law of sines in the subtriangles $ABK$, $ACL$, $BMK$, $CLN$, $LNC$.
5. **"Direct proof / contrapositive"** — the power-of-a-point path is a direct chain.
6. **"Reformulate"** (meta-strategy): the problem is a circumcenter equality problem best viewed via power of a point, not direct distance computation.

---

### Analogous past problems (cruxes)

The crux corpus covers NT/combinatorics/algebra only, and explicitly notes "geometry — not in the corpus yet." No analogous cruxes retrievable. Searching for IMO geometry problems with circumcenter-equidistance conclusions from the corpus is not possible. **None found.**

---

### Prior progress

None — this is round 1, workspace empty.

---

### Dead ends (do not retry)

- **Searching for four-point concyclicity among basic quadruples** (e.g., $B,K,L,N$ or $C,K,L,M$ or $B,M,K,C$): numerically, none of these are concyclic (determinants non-zero). Conditions (C4) and (C5) do not encode simple four-point concyclicity.
- **Spiral similarity centered at $K$ or $L$ mapping $(B,M) \to (C,L)$** etc.: checked numerically, the complex ratios don't match. No simple spiral similarity among the six points.
- **Trying to find $A'$ as circumcenter of a specific triangle:** $A'$ is not the circumcenter of $BKC$, $BLC$, $BKL$, or $CKL$ (checked numerically).

---

### Small-case / intuition notes

**Conjecture (strongly supported by numerics, not proved):**
- For each value of $\alpha \in (0, \angle ABC)$, there is a unique pair $(K, L)$ satisfying conditions (C3)–(C5).
- The family parametrized by $\alpha$ gives a one-dimensional locus of circumcenters $O(\alpha)$, all satisfying $OM = ON$.
- The power identity $\text{pow}(B) - \text{pow}(C) = (AB^2-AC^2)/2$ holds for every $\alpha$ in this family.

**Key derived fact (provable from (C3) and (C5)):**
$$\angle CKM = \angle BLN = 180° - \angle BAC - \alpha.$$
This equality holds rigorously and is available as a lemma.

**Key observation on antipode:**
The antipode $A' = 2O - A$ has its $x$-projection (onto $BC$) exactly at the midpoint of $BC$, for all tested triangle shapes and all $\alpha$ values (errors $< 10^{-9}$). This is the most sharply focused numerical observation.

**Formula (useful for builders):** $\cos(\angle A'KB) = -\sin(\angle AKB)$ (from the $90°$-clockwise rotation of $KA$ at $K$ giving $KA'$, and then the angle to $KB$). This gives:
$$A'B^2 = A'K^2 + BK^2 + 2 \cdot A'K \cdot BK \cdot \sin(\angle AKB)$$
and by the sine rule in $\triangle ABK$: $BK \sin(\angle AKB) = AB \sin(\angle BAK)$, so:
$$A'B^2 = A'K^2 + BK^2 + 2 \cdot A'K \cdot AB \cdot \sin(\angle BAK).$$
Similarly $A'C^2 = A'L^2 + CL^2 + 2 \cdot A'L \cdot AC \cdot \sin(\angle CAL)$.
These formulas (in terms of $R$, $\alpha$, and the inscribed angles $\angle AKL$, $\angle ALK$) are the trig tools for Opening D/E.
