## Status
solved

## Approaches tried
- **trig-lawofsines** (SOLVED, APPROVE, round 2): complete rigorous proof. Law of Sines
  parametrisation by `θ`; closing relations E3′,E2′ from the certified cevian lengths;
  `OM=ON` reduced to a single scalar identity (T); (T) proved by an **exact** Weierstrass
  (`t=tan(γ/2)`, `s=tan(β/2)`) pseudo-division certificate
  `lc(P)·lc(Q)·TN = f·P + g·Q` modulo the Pythagorean relations, with
  `lc(P)=−2 sinA sinθ sin(C−θ)`, `lc(Q)=−2 sinA sinθ sin(B−θ)` nonzero on the physical
  configuration. Reviewer independently re-derived the whole chain: (T)⟺OM=ON via
  `OM²−ON² = TN/(4D·Tden)` (D,Tden ≠ 0), rebuilt P,Q,TN from scratch, reproduced the
  pseudo-division (R2 ≡ 0 mod Pythagorean), and confirmed both leading coefficients.
- **power-of-point-BC** (partial, CHANGES REQUESTED, round 2): certified reduction chain
  (round 1) + **now-proven E2′,E3′** (§E, gap-free from cevian lengths). OPEN: G3 (the
  final scalar identity) not closed synthetically; Lemma O ordering and one G2 betweenness
  sub-step argued but not fully closed.
- **inversion-at-A** (partial, CHANGES REQUESTED, round 2): exact circle→line
  reformulation (`ℓ*=ι(ω)` is the polar of `A`), honestly shown tautological (pinning `ℓ*`
  ≡ pinning `O`); residual reduced to the intercept identity but the E2/E3 coupling
  (G-scalar) is OPEN.
- **complex-swap-symmetry** (partial, round 1): L1 clean; crux `Tnum=0` numeric only.

## Current best
The problem is **solved** by `trig-lawofsines`. See the Full proof below.

## Full proof

Throughout, `△ABC` has angles `A,B,C` at `A,B,C` with `A+B+C=π`, all in `(0,π)`.
`M,N` are the midpoints of `AB,AC`; `K,L` are the given interior points; `O` is the
circumcentre of `△AKL`. We prove `OM=ON`.

### 1. Frame and the four angle hypotheses
`OM=ON` is invariant under similarity, so put `B=(0,0)`, `C=(1,0)` (`BC=1` WLOG). By the
**Law of Sines** (`knowledge_base.md`, "Law of Sines"), with `a=BC=1`,
`AB=\sinC/\sinA`, `AC=\sinB/\sinA`, and since `∠ABC=B`,
`A=(\sinC\cosB/\sinA,\ \sinC\sinB/\sinA)`, `M=(A+B)/2`, `N=(A+C)/2`. Write
`A_x=\sinC\cosB/\sinA`.

Set `θ:=∠KBA=∠ACL` (E1), `β:=∠LBK=∠LNC` (E2), `γ:=∠LCK=∠BMK` (E3). Because `K` lies
inside `∠LBA` and inside `△BMC`, ray `BK` lies strictly between `BA` and `BC`; likewise
`L` inside `∠ACK∩△BNC` puts `CL` strictly between `CA` and `CB`. With `∠ACK=∠ACL+∠LCK=
θ+γ` and `∠ABL=∠ABK+∠KBL=θ+β` (interior containments), this gives the strict inequalities
`0<θ<B`, `0<θ<C`, `0<γ<C−θ`, `0<β<B−θ`  (⋆),
whence `\sinA,\sinθ,\sin(C−θ),\sin(B−θ)>0`.

### 2. Parametrisation of K and L
Measuring ray-angles from the positive `x`-axis: `BK` has angle `B−θ`, `BL` has angle
`B−θ−β`. In `△BCK`, `∠KBC=B−θ`, `∠KCB=C−θ−γ`, so `∠BKC=π−(B−θ)−(C−θ−γ)=A+2θ+γ`, and by
the Law of Sines `BK=\sin(C−θ−γ)/\sin(A+2θ+γ)`. In `△BCL`, `∠LBC=B−θ−β`, `∠LCB=C−θ`,
`∠BLC=A+2θ+β`, so `BL=\sin(C−θ)/\sin(A+2θ+β)`. Hence
`K=BK(\cos(B−θ),\sin(B−θ))`, `L=BL(\cos(B−θ−β),\sin(B−θ−β))`  (2.1).

### 3. The closing relations E3′, E2′
By the **cevian-length lemma** (`lemmas/cevian-lengths.md`, certified): in `△BMK`,
`∠MBK=∠KBA=θ`, `∠BMK=γ` (E3), `BM=AB/2`, so `BK=(AB/2)\sinγ/\sin(θ+γ)`. Equating with the
`△BCK` value of §2, substituting `AB=\sinC/\sinA` and clearing denominators (all factors
`\sinC,\sin(θ+γ),\sin(A+2θ+γ)>0` on (⋆)):
**(E3′)** `\sinγ\,\sinC\,\sin(A+2θ+γ)=2\sinA\,\sin(θ+γ)\,\sin(C−θ−γ)`.
The `B↔C, M↔N, γ↔β` mirror (E2 reads `∠CNL=∠LBK=β`, `∠NCL=θ`, `CN=AC/2`) gives
**(E2′)** `\sinβ\,\sinB\,\sin(A+2θ+β)=2\sinA\,\sin(θ+β)\,\sin(B−θ−β)`.
E3′ constrains `γ`, E2′ constrains `β`, each holds at the physical configuration.
(Certified lemma `lemmas/closing-relations.md`.)

### 4. Reduction of OM=ON to a scalar identity (T)
By the **certified reduction** (`lemmas/reduction-power-to-core.md`), with `ω=⊙(AKL)`,
`R=OA`, `pow(X)=|XO|²−R²`, `OM=ON ⟺ pow(M)=pow(N)`. Put `u=K−A`, `v=L−A`,
`D=u_1v_2−u_2v_1` (signed double area of `△AKL`, `≠0` since `A,K,L` non-collinear). The
**circumcentre formula** (`knowledge_base.md`, "Circumcentre / perpendicular bisector")
gives the circumcentre of `△AKL`, and substituting `B=(0,0)`, `C=(1,0)` into
`pow(M)−pow(N)`, `OM=ON` becomes equivalent to the single scalar identity
**(T)** `2(|u|²v_2−|v|²u_2)=D(1−2A_x)`.
(Explicitly `OM²−ON² = [2(|u|²v_2−|v|²u_2)−D(1−2A_x)]/(4D)`; since `D≠0`, `OM=ON ⟺ (T)`.)
Via (2.1), `u,v,D,A_x` are explicit trigonometric functions of `A,C,θ,γ,β` (`B=π−A−C`).

### 5. Weierstrass substitution and leading coefficients
Set `t=\tan(γ/2)`, `s=\tan(β/2)` (**tangent half-angle substitution**, `knowledge_base.md`,
"rational parametrisation"). By (⋆), `γ∈(0,C−θ)⊂(0,π)` and `β∈(0,B−θ)⊂(0,π)`, so `t,s`
are finite and positive. Substituting `\cosγ=(1−t²)/(1+t²)`, `\sinγ=2t/(1+t²)` (and the
`s`-analogues) into (E3′),(E2′) and clearing `(1+t²)²`, `(1+s²)²` gives degree-4
polynomials `P(t)=0`, `Q(s)=0`, with `\mathrm{lc}(P,t)=−2\sinA\,\sinθ\,\sin(C−θ)`,
`\mathrm{lc}(Q,s)=−2\sinA\,\sinθ\,\sin(B−θ)` (using `\sin(A+C+θ)=\sin(B−θ)`), both
**nonzero** on the physical configuration by (⋆).

### 6. The polynomial certificate
Clearing the (strictly positive on (⋆)) factors `\sin²A`, `\sin²(A+2θ+γ)`,
`\sin²(A+2θ+β)` and the powers of `(1+t²),(1+s²)`, the difference (LHS−RHS) of (T)
becomes a polynomial `TN(t,s)` (`\deg_t=\deg_s=4`) in `t,s` with coefficients polynomial in
`\cosA,\sinA,\cosC,\sinC,\cosθ,\sinθ` (with `\cosB=\sinA\sinC−\cosA\cosC`,
`\sinB=\sinA\cosC+\cosA\sinC`); the clearing factors being nonzero,
`TN=0 ⟺ (T) ⟺ OM=ON`  (6.1).

**Claim.** `TN∈⟨P,Q,ρ_1,ρ_2,ρ_3⟩` where `ρ_1=\sin²A+\cos²A−1`, `ρ_2=\sin²C+\cos²C−1`,
`ρ_3=\sin²θ+\cos²θ−1`.

*Proof.* Euclidean pseudo-division of `TN` by `P` in `t` (`\deg_t TN=\deg_t P=4`, one
step) gives the exact identity `\mathrm{lc}(P,t)·TN=q_1P+R_1`, `\deg_t R_1≤3` (6.2).
Pseudo-dividing `R_1` by `Q` in `s` gives `\mathrm{lc}(Q,s)·R_1=q_2Q+R_2`, `\deg_s R_2≤3`
(6.3). Each coefficient of `R_2` reduces to `0` modulo `⟨ρ_1,ρ_2,ρ_3⟩` (equivalently,
substituting `\cos²=1−\sin²`, `R_2≡0` identically), so `R_2` vanishes for every angle
triple. Combining, `\mathrm{lc}(P,t)\mathrm{lc}(Q,s)·TN=\underbrace{\mathrm{lc}(Q,s)q_1}_{f}P
+\underbrace{q_2}_{g}Q`  (6.4), an identity of trig functions of `A,C,θ,t,s`. ∎
The three exact identities (6.2),(6.3) and `R_2≡0 (\mathrm{mod}\ ρ_1,ρ_2,ρ_3)` are a
from-scratch symbolic reduction to `0` by exact rational polynomial arithmetic (the same
rigor standard used for `lemmas/reduction-power-to-core.md`), independently reproduced by
the reviewer.

### 7. Conclusion
On the physical configuration, `γ,β` satisfy (E3′),(E2′), i.e. `P(t)=0`, `Q(s)=0`.
Substituting into (6.4), `\mathrm{lc}(P,t)\mathrm{lc}(Q,s)·TN=f·0+g·0=0`. By §5 both
leading coefficients are nonzero on (⋆), so `TN=0`; by (6.1), `(T)` holds and `OM=ON`. ∎
