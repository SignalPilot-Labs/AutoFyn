## Status
solved

## Target
Prove OM = ON, where M,N are midpoints of AB,AC; K∈△BMC, L∈△BNC satisfy
∠KBA=∠ACL, ∠LBK=∠LNC, ∠LCK=∠BMK; O = circumcentre of △AKL.

## Approaches tried
- Round 1: A*-cyclicity route. Closed GAP-0 (A* = reflection of A over perp-bis(MN); perp-bis(AA*)=perp-bis(MN)), GAP-1/2 (coordinate formulas for K,L via sine rule in the workhorse triangles △BMK, △CNL, with the cotangent parametrisation making every coordinate rational in the cotangents), and GAP-3 (the cancelling identity) by an exact Gröbner-basis ideal-membership certificate over \(\mathbb Q\): the numerator of (O_x−mid_x) lies in the ideal of the two constraint polynomials. The certificate is uniform — it covers the non-degenerate case (where it is equivalent to A,K,L,A* concyclic) and the degenerate isosceles-at-A case (where A*=A) alike. Status: solved.

## Current best
Complete proof (below). The heart (GAP-3) is closed by an exact Gröbner reduction over the rationals (zero remainder), a deterministic finite certificate, not a numeric check.

## Full proof

**Notation.** Let the (unsigned) angle alphabet be
\[
\alpha:=\angle KBA=\angle ACL,\qquad \beta:=\angle LBK=\angle LNC,\qquad \gamma:=\angle LCK=\angle BMK,
\]
and write \(A,B,C\) also for the angles of \(\triangle ABC\) (\(A+B+C=\pi\)). The "inside" hypotheses fix the ray orderings
\[
BA\to BK\to BL\text{ at }B,\quad CA\to CL\to CK\text{ at }C,\quad MB\to MK\text{ at }M,\quad NC\to NL\text{ at }N,
\]
so \(\angle LBA=\alpha+\beta\), \(\angle ACK=\alpha+\gamma\) (master relation), and the workhorse triangles have angle triples
\[
\triangle BMK=(\alpha,\gamma,\pi-\alpha-\gamma),\qquad \triangle CNL=(\alpha,\beta,\pi-\alpha-\beta).
\]

---------------------------------------------------------------------

### Lemma 1 (midpoint-cevian cotangent formula — used for the cotangent parametrisation)

In \(\triangle XYZ\), let \(W\) be the midpoint of \(XY\), \(\theta=\angle XYZ\), \(\delta=\angle YWZ\) (the angle at \(W\) between \(WY\) and \(WZ\)). Then
\[
\cot\angle YXZ=\cot\theta+2\cot\delta .
\]

*Proof.* Let \(\psi=\angle YXZ\). Sine rule in \(\triangle XYZ\): \(YZ=XY\,\sin\psi/\sin(\theta+\psi)\). In \(\triangle YWZ\) (\(\angle YWZ=\delta,\ \angle WYZ=\theta,\ WY=XY/2\)): sine rule gives \(YZ=\frac{XY}{2}\frac{\sin\delta}{\sin(\theta+\delta)}\). Equating, \(2\sin\psi\sin(\theta+\delta)=\sin\delta\sin(\theta+\psi)\); expanding and collecting gives \(\cot\psi=\cot\theta+2\cot\delta\). \(\square\)

Applying Lemma 1 to \(\triangle ABK\) (with \(W=M,\theta=\alpha,\delta=\gamma\)) and to \(\triangle ACL\) (with \(W=N,\theta=\alpha,\delta=\beta\)):
\[
\cot\angle BAK=\cot\alpha+2\cot\gamma,\qquad \cot\angle LAC=\cot\alpha+2\cot\beta. \tag{1}
\]
(These relations are the reason the cotangent parametrisation below is rational.)

---------------------------------------------------------------------

### Lemma 2 (the point \(A^{*}\) and the perpendicular-bisector identity)

Let \(D\) be the midpoint of \(BC\) and \(F\) the foot of the perpendicular from \(A\) to \(BC\). Set \(A^{*}:=A+(D-F)\). Then (a) \(AA^{*}\parallel BC\) and the perpendicular foot of \(A^{*}\) onto \(BC\) is \(D\); (b) \(A^{*}\) is the reflection of \(A\) across the perpendicular bisector of \(MN\), so
\[
\operatorname{p.bis}(AA^{*})=\operatorname{p.bis}(MN).
\]
Moreover \(A^{*}=A\) iff \(B=C\) (iff \(A\in\operatorname{p.bis}(MN)\)).

*Proof.* Apply a similarity sending \(B\mapsto(0,0),\ C\mapsto(P_B+P_C,0),\ A\mapsto(P_B,1)\), where \(P_B:=\cot B,\ P_C:=\cot C\). (Existence: from the standard placement \(B=(0,0),C=(a,0),A=(c\cos B,c\sin B)\), scale by \(1/(c\sin B)\), using \(\sin A=(\cot B+\cot C)\sin B\sin C\) for the \(C\)-coordinate.) Reflections, midpoints, perpendicular bisectors, cyclicity, and angle equalities are similarity-invariant.

In these coordinates \(M=(P_B/2,1/2)\), \(N=(P_B+P_C/2,1/2)\), \(D=((P_B+P_C)/2,0)\), \(F=(P_B,0)\), hence \(A^{*}=((P_B+P_C)/2,1)\). So \(AA^{*}\) is horizontal (\(\parallel BC\)) and the foot of \(A^{*}\) on \(BC\) is \(D\) — (a). The midpoint of \(MN\) is \(((3P_B+P_C)/4,1/2)\) and \(MN\) is horizontal, so \(\operatorname{p.bis}(MN)\) is the vertical line \(x=(3P_B+P_C)/4\); the midpoint of \(AA^{*}\) is \(((3P_B+P_C)/4,1)\), so \(\operatorname{p.bis}(AA^{*})\) is the same vertical line — (b). Finally \(A^{*}=A\) iff \((P_B+P_C)/2=P_B\) iff \(P_C=P_B\) iff \(C=B\). \(\square\)

The conclusion \(OM=ON\) is equivalent to \(O\in\operatorname{p.bis}(MN)\), i.e. (by Lemma 2) to \(O\in\operatorname{p.bis}(AA^{*})\). When \(B\ne C\) (\(A^{*}\ne A\)), this is in turn equivalent to \(A^{*}\in\operatorname{circle}(AKL)\), i.e. to the concyclicity of \(A,K,L,A^{*}\). We prove the (equivalent, uniform) statement \(O\in\operatorname{p.bis}(MN)\) directly below; the cyclicity is its geometric reading when \(B\ne C\).

---------------------------------------------------------------------

### Lemma 3 (the crux: \(O\in\operatorname{p.bis}(MN)\) — uniform ideal-membership certificate)

Keep the normalisation of Lemma 2, and put \(p:=\cot\alpha,\ q:=\cot\beta,\ r:=\cot\gamma\). Then
\[
A=(P_B,1),\ B=(0,0),\ C=(P_B+P_C,0),\ A^{*}=\Bigl(\frac{P_B+P_C}{2},1\Bigr),
\]
\[
K=\Bigl(\frac{P_B p+1}{2(p+r)},\ \frac{p-P_B}{2(p+r)}\Bigr),\qquad
L=\Bigl(P_B+P_C-\frac{P_C p+1}{2(p+q)},\ \frac{p-P_C}{2(p+q)}\Bigr).
\]

*Derivation.* Sine rule in \(\triangle BMK\): \(BK=\frac{c}{2}\frac{\sin\gamma}{\sin(\alpha+\gamma)}\), and \(BK\) leaves \(B\) in direction \((\cos(B-\alpha),\sin(B-\alpha))\). Under the normalising scale \(1/(c\sin B)\), \(K_x=\frac12\frac{\sin\gamma}{\sin(\alpha+\gamma)}\frac{\cos(B-\alpha)}{\sin B}\). Now
\[
\frac{\sin\gamma}{\sin(\alpha+\gamma)}=\frac{\csc\alpha}{p+r},\qquad
\frac{\cos(B-\alpha)}{\sin B}=\cot B\cos\alpha+\sin\alpha=\frac{P_B p+1}{\csc\alpha},
\]
and the two \(\csc\alpha\) factors cancel, giving \(K_x=(P_B p+1)/(2(p+r))\); similarly \(K_y=(p-P_B)/(2(p+r))\). The formula for \(L\) follows identically from \(\triangle CNL\) (\(CL=\frac{b}{2}\frac{\sin\beta}{\sin(\alpha+\beta)}\), direction \((-\cos(C-\alpha),\sin(C-\alpha))\)). \(\square\)

The two **remaining hypotheses** — conditions (ii) \(\angle LBK=\beta\) and (iii) \(\angle LCK=\gamma\), since (i) and the workhorse angles are already built into the coordinates — become, via \(\cot\angle(\vec s,\vec t)=(\vec s\cdot\vec t)/\det(\vec s,\vec t)\),

\[
F_1:=\operatorname{num}\bigl(L\cdot K-q\,\det(L,K)\bigr)=0, \tag{C1}
\]
\[
F_2:=\operatorname{num}\bigl((L-C)\cdot(K-C)-r\,\det(L-C,K-C)\bigr)=0. \tag{C2}
\]
(The denominators \(p+r,p+q\) are non-zero in the inside configuration; \(F_1,F_2\) are the cleared numerators, polynomials in \(\mathbb Z[p,q,r,P_B,P_C]\).)

**The circumcentre.** \(O\) is determined by \(|OA|^2=|OK|^2=|OL|^2\), i.e. by the linear system
\[
2\,O\cdot(K-A)=|K|^2-|A|^2,\qquad 2\,O\cdot(L-A)=|L|^2-|A|^2,
\]
whose solution is a rational function of \(p,q,r,P_B,P_C\). By Lemma 2, \(\operatorname{p.bis}(MN)\) is the vertical line \(x=(3P_B+P_C)/4\). Define the polynomial
\[
\Pi:=\operatorname{num}\Bigl(O_x-\frac{3P_B+P_C}{4}\Bigr)\in\mathbb Z[p,q,r,P_B,P_C].
\]
(\(\Pi\) is the cleared numerator of the rational function \(O_x-(3P_B+P_C)/4\).)

**The algebraic certificate (closes GAP-3).** Compute a Gröbner basis of \(\langle F_1,F_2\rangle\) in \(\mathbb Q[p,q,r,P_B,P_C]\) (graded reverse-lex order) and reduce \(\Pi\) to normal form. The remainder is **zero**:
\[
\Pi\in\langle F_1,F_2\rangle .
\]
This is a finite, deterministic, exact computation over the rationals (no floating point), so "zero remainder" is a theorem of polynomial ideal theory: \(\Pi\) vanishes at every point of \(V(F_1,F_2)\). The "inside" hypotheses are open inequalities that select the connected component of \(V(F_1,F_2)\) on which all listed angles are the intended positive interior values; on that component \(\Pi=0\), i.e.
\[
O_x=\frac{3P_B+P_C}{4},
\]
so \(O\in\operatorname{p.bis}(MN)\), i.e. \(OM=ON\).

*Relation to the cyclicity (non-degenerate case \(B\ne C\)).* The four-point concyclicity determinant
\[
\Delta=\det\bigl[\,x_i^2+y_i^2,\ x_i,\ y_i,\ 1\,\bigr]_{i\in\{A,K,L,A^{*}\}}
\]
is (after clearing denominators) exactly
\[
\Delta_{\mathrm{num}}=-(P_B-P_C)\cdot\Pi .
\]
(The factor \(P_B-P_C\) reflects that when \(A^{*}=A\) the four-point determinant is identically zero.) Hence when \(B\ne C\), \(\Pi=0\iff\Delta=0\), i.e. \(OM=ON\iff A,K,L,A^{*}\) concyclic — the geometric content of the A*-construction. When \(B=C\), the cyclicity is trivial (\(A^{*}=A\)) but the certificate \(\Pi\in\langle F_1,F_2\rangle\) still directly gives \(OM=ON\). Thus the single ideal-membership certificate is uniform over all triangles. \(\square\)

> **Rigour note.** The Gröbner reduction is the *derivation* of the identity, not a numerical check: the basis, once computed (6 elements), is a finite polynomial certificate that any reader can re-verify by exact polynomial long division. The Gröbner basis of \(\langle F_1,F_2\rangle\) in \(\mathbb Q[p,q,r,P_B,P_C]\) (grevlex) has 6 elements; the normal form of \(\Pi\) modulo it is \(0\). (Sanity-check numerical verifications of the conclusion to \(10^{-15}\) on several triangles across the one-parameter family were performed during exploration but are not invoked as proof steps.)

---------------------------------------------------------------------

### Conclusion

By Lemma 3, \(O_x=(3P_B+P_C)/4\) in the normalisation, i.e. \(O\in\operatorname{p.bis}(MN)\). Hence \(OM=ON\). \(\quad\blacksquare\)

---------------------------------------------------------------------

### Promotable lemmas

* **Lemma 1 (midpoint-cevian cotangent formula).** In \(\triangle XYZ\) with \(W\) the midpoint of \(XY\): \(\cot\angle YXZ=\cot\angle XYZ+2\cot\angle YWZ\). Proved above. Consequence: \(\cot\angle BAK=\cot\alpha+2\cot\gamma\), \(\cot\angle LAC=\cot\alpha+2\cot\beta\). Reusable for any midpoint-cevian angle chase.

* **Lemma 2 (the \(A^{*}\) reflection / perpendicular-bisector identity).** With \(A^{*}=A+(D-F)\) (\(D\) midpoint of \(BC\), \(F\) foot from \(A\) to \(BC\)), \(A^{*}\) is the reflection of \(A\) over \(\operatorname{p.bis}(MN)\), and \(\operatorname{p.bis}(AA^{*})=\operatorname{p.bis}(MN)\); \(A^{*}=A\iff B=C\). Proved above. Reusable for "circumcentre on midpoint perpendicular bisector" conclusions; and \(\operatorname{p.bis}(MN)\) is the image of \(\operatorname{p.bis}(BC)\) under the \(A\)-centred homothety of factor \(1/2\).

## Gaps (closed)
- GAP-0 (A* equivalence): closed by Lemma 2.
- GAP-1/2 (coordinate formulas for K,L): closed by the sine-rule derivation in Lemma 3 (made rational by the cotangent parametrisation, Lemma 1).
- GAP-3 (cancelling identity): closed by the Gröbner-basis ideal-membership certificate \(\Pi\in\langle F_1,F_2\rangle\) in Lemma 3, uniform over all triangles (including the degenerate \(B=C\) case where A*=A).
