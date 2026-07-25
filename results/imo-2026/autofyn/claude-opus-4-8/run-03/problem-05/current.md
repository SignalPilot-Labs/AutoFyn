## Status
solved

## Approaches tried
- **orbit-crossing** (APPROVE): orbit-marching (R-test) kills two distinct positive d-values;
  residual {0,b} closed by "F open + boundary-point limit" via R at a fixed/shift pair. Correct.
- **monotonicity-orbits** (APPROVE): same spine; residual {0,b} closed by the clean separation
  |p−q|≥b (from L at (q,p)) making both F and G open, contradicting connectedness. Correct.
- **shift-family-sos** (APPROVE): same spine; residual {0,b} closed by two failure-band quadratics
  (L* and R*) forcing both F and G open. Correct.

All three establish the same characterization by the same core (Lemmas A/C + marching lemma) and
differ only in the endgame packaging; each endgame is independently rigorous.

## Current best
Complete. Answer: **f(x) = x + c for every constant c ≥ 0, and no others.**

## Full proof

We determine all f : ℝ_{>0} → ℝ_{>0} with
$$\sqrt{\tfrac{x^2+f(y)^2}{2}} \ \ge\ \tfrac{f(x)+y}{2} \ \ge\ \sqrt{x\,f(y)}\qquad(\star)\quad\forall x,y>0.$$

**Answer.** Exactly the functions **f(x) = x + c with a constant c ≥ 0.**

### 0. Squared form
All three quantities are positive (f>0, x,y>0), and t↦t² is strictly increasing on [0,∞), so (★)
is equivalent to: for all x,y>0,
$$\mathbf L(x,y):\ 2(x^2+f(y)^2)\ge (f(x)+y)^2,\qquad \mathbf R(x,y):\ (f(x)+y)^2\ge 4x\,f(y).$$

### 1. Every f(x)=x+c with c≥0 is a solution (and c≥0 is forced)
For f(x)=x+c to map into ℝ_{>0} we need x+c>0 for all x>0; letting x→0⁺ forces c≥0, and c≥0 gives
x+c>0. With f(t)=t+c both defects equal the same perfect square:
$$(f(x)+y)^2-4x f(y)=(x+y+c)^2-4x(y+c)=((x-y)-c)^2\ge0,$$
$$2(x^2+f(y)^2)-(f(x)+y)^2=2x^2+2(y+c)^2-(x+y+c)^2=((x-y)-c)^2\ge0.$$
So both **L** and **R** hold; f is a solution. Now fix an arbitrary solution f.

### 2. Structural lemmas
**Lemma A.** f(f(y))=2f(y)−y. *Proof.* Put x=f(y). **R**(f(y),y): (f(f(y))+y)²≥4f(y)², and both
sides positive ⇒ f(f(y))+y≥2f(y). **L**(f(y),y): 4f(y)²≥(f(f(y))+y)² ⇒ f(f(y))+y≤2f(y). Equal. ∎

**Lemma B (injectivity).** f(a)=f(b) ⇒ f(f(a))=f(f(b)) ⇒ 2f(a)−a=2f(b)−b ⇒ a=b. ∎

**Lemma C.** With d(y):=f(y)−y: (i) d(f(y))=d(y); (ii) fⁿ(y)=y+n·d(y), n≥0; (iii) d(y)≥0.
*Proof.* (i) d(f(y))=f(f(y))−f(y)=(2f(y)−y)−f(y)=d(y). (ii) Induction using (i) iterated:
d(fⁿ(y))=d(y), so f^{n+1}(y)=fⁿ(y)+d(y)=y+(n+1)d(y). (iii) fⁿ(y)=y+n·d(y)>0 for all n forces
d(y)≥0. ∎

### 3. R-test
For p,q>0 with a:=d(p), b:=d(q): f(p)=p+a, f(f(p))=p+2a (Lemma A + C), f(q)=q+b. Substituting
(x,y)=(f(p),q) into **R** and expanding gives the identity
$$(p+2a+q)^2-4(p+a)(q+b)=(p-q)^2+4(a-b)(p+a),$$
so **R**(f(p),q) is equivalent to $(p-q)^2\ge 4(b-a)(p+a).$  (†)

### 4. d takes at most one positive value
Suppose distinct positive values a<b occur, at p₀ (d=a) and q₀ (d=b). The orbits Pₘ=p₀+ma (d=a)
and Qₙ=q₀+nb (d=b) are all admissible (Lemma C). Since a>0, Pₘ→∞; for large m set
n=⌊(Pₘ−q₀)/b⌋≥0, giving 0≤Pₘ−Qₙ<b, so (Pₘ−Qₙ)²<b². Apply (†) with p=Pₘ (d=a), q=Qₙ (d=b):
$$(P_m-Q_n)^2\ge 4(b-a)(P_m+a)\to\infty\quad(m\to\infty),$$
since b−a>0. For m large, 4(b−a)(Pₘ+a)>b²≥(Pₘ−Qₙ)², a contradiction. Hence the positive values
of d coincide; with d≥0, d(x)∈{0,b} for a single b≥0.

### 5. Fixed points and shifts cannot coexist
If b=0 then d≡0, f(x)=x (c=0). Assume b>0 and, for contradiction, both values attained. Put
$$F=\{x:d(x)=0\}=\{f(x)=x\},\qquad G=\{x:d(x)=b\},$$
so F,G are nonempty, disjoint, F∪G=(0,∞). For p∈F, q∈G, apply **L**(q,p) (x=q, f(x)=q+b; y=p,
f(y)=p):
$$2(q^2+p^2)\ge(q+b+p)^2\ \Longleftrightarrow\ (p-q)^2\ge b^2+2b(p+q)\ge b^2,$$
so |p−q|≥b for every p∈F, q∈G.  (Sep)

**F open:** for p∈F take δ=min(b,p)/2>0. If x∈(p−δ,p+δ) then x>p/2>0, so x∈F∪G, and |x−p|<b, so
x∉G by (Sep); hence x∈F. **G open:** identically for q∈G with δ=min(b,q)/2. Thus F,G are disjoint
nonempty open sets covering the connected interval (0,∞) — impossible. So the case {0,b} cannot occur.

### 6. Conclusion
d is constant, d≡c with c≥0 (Lemma C(iii)); i.e. f(x)=x+c. By Section 1 each such f (c≥0) is a
solution and c≥0 is forced. Hence the complete solution set is
$$\boxed{f(x)=x+c,\quad c\ge0.}\qquad\blacksquare$$

### Named tools
- Squaring equivalence for positive reals (Section 0).
- Sum-of-squares / completing the square (Sections 1, 3, 5), verified symbolically.
- Archimedean/floor bounding: a bounded square cannot dominate a linear-growing term (Section 4).
- Connectedness of an interval: no partition into two nonempty open sets (Section 5).
