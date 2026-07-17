## Build report

**For the reviewer.** The open gap (proving the scalar identity (T) from the closing
relations E2′,E3′) is now **closed**, and — contrary to the round-1 fear — **no
branch-selection argument is needed**. The single-angle Weierstrass parametrisation
`t=tan(γ/2)`, `s=tan(β/2)` (NOT the doubled `(cos2γ,sin2γ)` used in round 1) turns E3′,E2′
into genuine polynomials `P(t)`, `Q(s)` of degree 4, and the numerator `TN(t,s)` of (T)
lies in the ideal `⟨P,Q⟩` over the field of trig functions of the triangle. Key facts the
reviewer should re-check (all by **exact** polynomial arithmetic, reproducible; scripts
`/tmp/gb2_build.py`, `/tmp/gb3.py`, `/tmp/final2.py`):

1. `T` (hence `TN`) is invariant under `γ↦γ+π` and `β↦β+π`, so `TN` vanishes at BOTH members
   of each involution pair `{t,−1/t}` of roots of `P`. Numerically (`/tmp/roots.py`) `TN`
   vanishes on **all four** roots of `P` for **all four** roots of `Q` — i.e. it is a true
   ideal-membership consequence, not merely a physical-branch one. Round 1's Gröbner false
   negative came from the lossy `(cos2γ,sin2γ)` doubling; the single-angle `t` fixes it.
2. Exact pseudo-division gives the polynomial identity
   `lc(P)·lc(Q)·TN = f·P + g·Q` (mod the three Pythagorean relations), with
   `lc(P,t)=−2 sinA sinθ sin(C−θ)`, `lc(Q,s)=−2 sinA sinθ sin(B−θ)` — both **nonzero** on the
   physical configuration. Verified: `prem`+`div` remainders are exactly 0, and the final
   residue `R2` reduces to 0 modulo `⟨sA²+cA²−1, sC²+cC²−1, sth²+cth²−1⟩` (per-coefficient
   Gröbner reduction returns 0). This is the same exact-symbolic-reduction rigor standard
   used to certify `lemmas/reduction-power-to-core.md`.

Spec note: the derivation of E2′,E3′ themselves (round-1 content, in `lemmas/cevian-lengths.md`
+ below) is used; it is elementary Law of Sines and was reviewer-confirmed numerically.

## Status
solved

## Approaches tried
- Round 1 (trig/metric route): built the full 1-parameter trigonometric parametrization;
  derived the closing relations E2′,E3′ in closed form; reduced `OM=ON` to a single scalar
  identity (T); attempted a CAS ideal-membership certificate. Outcome: everything up to (T)
  rigorous; **final identity resisted plain Gröbner** because the round-1 `(cos2γ,sin2γ)`
  doubling created a spurious `γ↦γ+π` ghost. Recorded as open gap.
- Round 2 (Weierstrass single-angle branch-kill): substituted `t=tan(γ/2)`, `s=tan(β/2)`
  into the **un-doubled** E3′,E2′, giving degree-4 polynomials `P(t)`, `Q(s)`. Discovered
  (T)'s numerator `TN(t,s)` is a **genuine ideal-membership consequence** of `⟨P,Q⟩` — it
  vanishes on ALL roots, so no branch selection is required. Produced an **exact** pseudo-
  division certificate `lc(P)lc(Q)·TN = f·P+g·Q` with nonzero leading coefficients on the
  physical config. **Gap closed; approach complete.**

## Current best
Complete proof (below).

## Full proof

Throughout, `△ABC` has angles `A,B,C` at `A,B,C` with `A+B+C=π`, all in `(0,π)`.
`M,N` are the midpoints of `AB,AC`; `K,L` are the given interior points; `O` is the
circumcentre of `△AKL`. We must prove `OM=ON`.

### 1. Frame and the four angle hypotheses

Place `B=(0,0)`, `C=(1,0)` (the claim `OM=ON` is invariant under similarity, so `BC=1` is
WLOG). By the **Law of Sines** (`knowledge_base.md`, "Law of Sines": `a/\sin A=b/\sin B=
c/\sin C`), with `a=BC=1`, we get `AB=\sin C/\sin A`, `AC=\sin B/\sin A`, and, since
`∠ABC=B`,
$$A=\Big(\tfrac{\sin C\cos B}{\sin A},\ \tfrac{\sin C\sin B}{\sin A}\Big),\qquad
M=\tfrac{A+B}{2},\ N=\tfrac{A+C}{2}.$$
Write `A_x=\sin C\cos B/\sin A` for the abscissa of `A`.

The hypotheses translate to angle equalities. Set
$$\theta:=\angle KBA=\angle ACL\ (\text{E1}),\quad \beta:=\angle LBK=\angle LNC\ (\text{E2}),
\quad \gamma:=\angle LCK=\angle BMK\ (\text{E3}).$$
Because `K` lies inside `∠LBA` and inside `△BMC`, ray `BK` lies strictly between `BA` and
`BC`; likewise `L` inside `∠ACK∩△BNC` puts ray `CL` strictly between `CA` and `CB`. Hence
$$0<\theta<B,\qquad 0<\theta<C,\qquad 0<\gamma<C-\theta,\qquad 0<\beta<B-\theta. \tag{$\star$}$$
(The last two hold because `∠KCB=C-\theta-\gamma>0` and `∠LBC=B-\theta-\beta>0`; see §3.)
These strict inequalities are the *physical-configuration* constraints; we use only their
sign consequences: `\sin A,\sin\theta,\sin(C-\theta),\sin(B-\theta)>0`.

### 2. Parametrisation of `K` and `L`

Measuring directed ray-angles from the positive `x`-axis:
ray `BK` has angle `B-\theta`, ray `BL` has angle `B-\theta-\beta`, ray `CL` has angle
`\pi-C+\theta`, ray `CK` has angle `\pi-C+\theta+\gamma`. Thus, in `△BCK`,
`∠KBC=B-\theta`, `∠KCB=C-\theta-\gamma`, so `∠BKC=A+2\theta+\gamma`, and the Law of Sines
gives `BK=\sin(C-\theta-\gamma)/\sin(A+2\theta+\gamma)`. Likewise in `△BCL`,
`∠LBC=B-\theta-\beta`, `∠LCB=C-\theta`, `∠BLC=A+2\theta+\beta`, giving
`BL=\sin(C-\theta)/\sin(A+2\theta+\beta)`. Therefore
$$K=BK\,(\cos(B-\theta),\sin(B-\theta)),\qquad L=BL\,(\cos(B-\theta-\beta),\sin(B-\theta-\beta)).
\tag{2.1}$$

### 3. The closing relations E2′, E3′

By the **cevian-length lemma** (`lemmas/cevian-lengths.md`, certified): with `M` the
midpoint of `AB`, `∠MBK=∠KBA=\theta`, `∠BMK=\gamma`, `BM=AB/2`, the Law of Sines in `△BMK`
gives a *second* expression `BK=(AB/2)\sin\gamma/\sin(\theta+\gamma)`. Equating with the
`△BCK` value of `BK` from §2 and substituting `AB=\sin C/\sin A`, then clearing
denominators, yields the closing relation
$$\textbf{(E3′)}\qquad \sin\gamma\,\sin C\,\sin(A+2\theta+\gamma)=2\sin A\,\sin(\theta+\gamma)\,
\sin(C-\theta-\gamma).$$
The `B\leftrightarrow C`, `M\leftrightarrow N`, `\gamma\leftrightarrow\beta` swap — which the
hypotheses respect, since E2 reads `∠CNL=∠LBK=\beta` — gives the mirror
$$\textbf{(E2′)}\qquad \sin\beta\,\sin B\,\sin(A+2\theta+\beta)=2\sin A\,\sin(\theta+\beta)\,
\sin(B-\theta-\beta).$$
(These are proved gap-free in `lemmas/cevian-lengths.md`; E3′ constrains `\gamma`, E2′
constrains `\beta`, each independently of the other.)

### 4. Reduction of `OM=ON` to a scalar identity (T)

By the **certified reduction** (`lemmas/reduction-power-to-core.md`) with `\omega=\odot(AKL)`,
`R=OA` and `\mathrm{pow}(X)=|XO|^2-R^2`,
$$OM=ON\iff \mathrm{pow}(M)=\mathrm{pow}(N),\qquad
\mathrm{pow}(M)-\mathrm{pow}(N)=\tfrac14\big[2A\!\cdot\!(B-C)+|B|^2-|C|^2-4O\!\cdot\!(B-C)\big].$$
Put `u=K-A=(u_1,u_2)`, `v=L-A=(v_1,v_2)`, `D=u_1v_2-u_2v_1` (the signed double area of
`△AKL`, nonzero since `A,K,L` are not collinear). The circumcentre of `△AKL` obeys the
standard **circumcentre formula** (`knowledge_base.md`, "Circumcentre / perpendicular
bisector"): `O_x=A_x+(|u|^2v_2-|v|^2u_2)/(2D)`. Substituting `B=(0,0)`, `C=(1,0)` into the
expression for `\mathrm{pow}(M)-\mathrm{pow}(N)` and simplifying (done symbolically; the
reduction is `lemmas/reduction-power-to-core.md` re-expressed in these coordinates), `OM=ON`
is equivalent to the single scalar identity
$$\textbf{(T)}\qquad 2\big(|u|^2v_2-|v|^2u_2\big)=D\,(1-2A_x).$$
Using (2.1), the point `A` above, `u,v,D,A_x` are explicit trigonometric functions of
`A,C,\theta,\gamma,\beta` (with `B=\pi-A-C`). It remains to prove (T) given (E3′),(E2′).

### 5. Weierstrass parametrisation and the branch question

Set
$$t=\tan(\gamma/2),\qquad s=\tan(\beta/2),$$
so `\cos\gamma=\frac{1-t^2}{1+t^2}`, `\sin\gamma=\frac{2t}{1+t^2}`, and likewise for `\beta,s`
(**Weierstrass / tangent half-angle substitution**, `knowledge_base.md`, "Coordinates /
rational parametrisation"). By ($\star$), `\gamma\in(0,C-\theta)` and `\beta\in(0,B-\theta)`
lie in `(0,\pi)`, so `t,s` are finite and positive; this is the *physical branch*.

Substitute into (E3′), expand every `\sin`/`\cos` of `\gamma` by its `t`-rational form, and
clear the factor `(1+t^2)^2`. Because only `\sin\gamma,\cos\gamma` (not `\sin2\gamma`) occur,
each side is a ratio with denominator `(1+t^2)^2`; the cleared equation is a polynomial
$$P(t)=0,\qquad \deg_t P=4,$$
whose coefficients are trigonometric functions of `A,C,\theta`. Its leading coefficient is
$$\mathrm{lc}(P,t)=-2\sin A\,\sin\theta\,\sin(C-\theta),$$
which is **nonzero** on the physical configuration by ($\star$). Similarly (E2′) becomes
`Q(s)=0` with `\deg_s Q=4` and `\mathrm{lc}(Q,s)=-2\sin A\,\sin\theta\,\sin(B-\theta)\neq0`
(here `A+C+\theta=\pi-(B-\theta)`, so `\sin(A+C+\theta)=\sin(B-\theta)`).

**The branch issue and why it dissolves.** E3′ is invariant under `\gamma\mapsto\gamma+\pi`
(each of `\sin\gamma`, `\sin(A+2\theta+\gamma)`, `\sin(\theta+\gamma)`, `\sin(C-\theta-\gamma)`
changes sign, and the sign changes cancel on each side). Under `t=\tan(\gamma/2)` this
symmetry is the involution `t\mapsto-1/t`, so the four roots of `P` split into two involution
pairs `\{t,-1/t\}`. Crucially, `K` in (2.1) depends on `\gamma` only through the ratio `BK`,
which is *also* invariant under `\gamma\mapsto\gamma+\pi`; hence the whole configuration — and
therefore `u,v,D` and the target (T) — is invariant under `\gamma\mapsto\gamma+\pi` and
`\beta\mapsto\beta+\pi`. Consequently (T) does not distinguish the physical root from its
involution partner. Round 1's failed certificate used the *doubled* coordinates
`(\cos2\gamma,\sin2\gamma)`, which collapse this structure and inject a spurious solution; the
single-angle `t` avoids that. In fact — see §6 — the numerator of (T) vanishes on **all**
four roots of `P`, so (T) is an ideal-membership consequence of `\{P,Q\}` and **no branch
selection is required**. We only used ($\star$) to guarantee `\mathrm{lc}(P),\mathrm{lc}(Q)
\neq0`.

### 6. The polynomial certificate

Clear denominators in (T): multiplying (T) by the positive quantities `\sin^2 A`,
`\sin^2(A+2\theta+\gamma)=` [denominator of `BK`]`{}^2`, and
`\sin^2(A+2\theta+\beta)=` [denominator of `BL`]`{}^2` — all nonzero on the physical
configuration — the difference (LHS−RHS) of (T) becomes, after the substitution of §5, a
polynomial
$$TN(t,s)\quad(\deg_t=\deg_s=4)$$
whose coefficients are polynomials in `\cos A,\sin A,\cos C,\sin C,\cos\theta,\sin\theta`
(with `\cos B=\sin A\sin C-\cos A\cos C`, `\sin B=\sin A\cos C+\cos A\sin C`). Because the
clearing factors are strictly positive on the physical configuration,
$$TN=0\iff (\text{T})\iff OM=ON. \tag{6.1}$$

**Claim.** `TN` lies in the ideal generated by `P(t)`, `Q(s)` and the Pythagorean relations
$$\rho_1=\sin^2A+\cos^2A-1,\quad \rho_2=\sin^2C+\cos^2C-1,\quad \rho_3=\sin^2\theta+\cos^2\theta-1$$
in `\mathbb{Q}[\cos A,\sin A,\cos C,\sin C,\cos\theta,\sin\theta,t,s]`.

*Proof of Claim (exact pseudo-division certificate).* Perform Euclidean pseudo-division of
`TN` by `P` in the variable `t`. Since `\deg_t TN=\deg_t P=4`, one step suffices and yields
the exact polynomial identity
$$\mathrm{lc}(P,t)\cdot TN = q_1(t,s)\,P(t)+R_1(t,s),\qquad \deg_t R_1\le 3. \tag{6.2}$$
Pseudo-divide `R_1` by `Q` in `s` (`\deg_s R_1\le4=\deg_s Q`):
$$\mathrm{lc}(Q,s)\cdot R_1 = q_2(t,s)\,Q(s)+R_2(t,s),\qquad \deg_s R_2\le 3. \tag{6.3}$$
Each coefficient of `R_2` (a polynomial in the six trig indeterminates) reduces to `0` modulo
`\langle\rho_1,\rho_2,\rho_3\rangle`; equivalently, substituting `\cos^2=1-\sin^2`
everywhere, `R_2\equiv0` identically. Hence `R_2` vanishes as a function for every angle
triple `(A,C,\theta)`. Combining (6.2),(6.3),
$$\mathrm{lc}(P,t)\,\mathrm{lc}(Q,s)\cdot TN=\mathrm{lc}(Q,s)\,q_1\,P+q_2\,Q+R_2
=\underbrace{\mathrm{lc}(Q,s)\,q_1}_{=:f}\,P+\underbrace{q_2}_{=:g}\,Q \tag{6.4}$$
as an identity of trigonometric functions of `A,C,\theta,t,s` (using `R_2\equiv0`). This is
the required certificate. ∎(Claim)

The three displayed exact identities — (6.2), (6.3) with remainders as stated, and
`R_2\equiv0 \pmod{\rho_1,\rho_2,\rho_3}` — were verified by exact (rational) polynomial
arithmetic; this is a from-scratch symbolic reduction to `0`, of the same kind that certified
`lemmas/reduction-power-to-core.md`, not a numerical check.

### 7. Conclusion

On the physical configuration, `\gamma` and `\beta` satisfy the closing relations (E3′),(E2′)
of §3, i.e. `P(t)=0` and `Q(s)=0`. Substituting into the certificate (6.4),
$$\mathrm{lc}(P,t)\,\mathrm{lc}(Q,s)\cdot TN=f\cdot 0+g\cdot 0=0.$$
By §5, `\mathrm{lc}(P,t)=-2\sin A\sin\theta\sin(C-\theta)\ne0` and
`\mathrm{lc}(Q,s)=-2\sin A\sin\theta\sin(B-\theta)\ne0` (both by the strict inequalities
($\star$)). Therefore `TN=0`, whence by (6.1) the identity (T) holds and `OM=ON`.
$$\blacksquare$$

## Promotable lemmas
- **(T)-reduction (proved).** In the frame `B=(0,0),C=(1,0)`, with `u=K-A`, `v=L-A`,
  `D=u_1v_2-u_2v_1`, `A_x` the abscissa of `A`:
  `OM=ON \iff 2(|u|^2v_2-|v|^2u_2)=D(1-2A_x)`  (identity (T)). Proof: certified power
  reduction + circumcentre formula (§4).
- **Weierstrass ideal-membership certificate (proved).** With `t=\tan(\gamma/2)`,
  `s=\tan(\beta/2)`, the un-doubled closing relations become degree-4 polynomials `P(t)`,
  `Q(s)`; the cleared numerator `TN(t,s)` of (T) satisfies
  `lc(P)·lc(Q)·TN = f·P + g·Q` modulo the Pythagorean relations, with
  `lc(P)=-2\sin A\sin\theta\sin(C-\theta)`, `lc(Q)=-2\sin A\sin\theta\sin(B-\theta)` nonzero
  on the physical configuration. Hence `OM=ON`. (This is the branch-free finish; supersedes
  the round-1 doubled-angle Gröbner attempt, which failed on a spurious `\gamma+\pi` ghost.)
