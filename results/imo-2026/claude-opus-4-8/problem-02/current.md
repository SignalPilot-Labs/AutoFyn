## Status
solved

## Approaches tried
- complex-reality-conditions — **SOLVED (proof-reviewer APPROVE, round 2 v2).** Complex-number bash
  with `A=0`: the three unsigned angle equalities + interior/inside-angle hypotheses are translated
  (rigorously, via signed areas / directed angles, §3) into three *reality* conditions
  `C_1,C_2,C_3 ∈ ℝ`, i.e. polynomial equations `E_1=E_2=E_3=0`; and `OM=ON ⟺ TN=0`. Both former gaps
  are now closed: (i) §3 geometry→algebra translation (Lemma 2 "reality hinge" pinning both directed
  angles into `(0,π)`; interior facts (K1),(L1),(L2); convex-sector betweenness) — certified round 2;
  (ii) the `detA=0` locus removal — replaced by an **unconditional exact real-slice ideal-membership
  certificate** `W·Im(TN) = f_1 Im(E_1)+f_2 Im(E_2)+f_3 Im(E_3)` with
  `W=|B−K|²·|C−L|²·Im(K̄L)·Im(B̄C)` (§6.2). None of the four factors of `W` can vanish on an admissible
  configuration (K≠B, L≠C, A,K,L non-collinear, ABC non-degenerate), and `Im(E_i)=0` by §3, so
  `Im(TN)=0`, i.e. `TN=0`, i.e. `OM=ON` on **every** admissible configuration — `detA` plays no role.
  Verified independently by the reviewer: purely-imaginary structure (`Re(E_i)=Re(TN)≡0`), the exact
  Gröbner membership reproduced (target = exact combination of Gröbner-basis elements, remainder `0`),
  bidegree-(2,2) homogeneity justifying WLOG `B=1`, and all four `W`-factors genuinely non-vanishing.
- antipode-perp-bisector — **partial (independent synthetic route).** Proven: Step 1 antipode
  equivalence `OM=ON ⟺ A*B=A*C`; Step 2 Thales; Step 4 isosceles synthesis modulo Step 3. Gap: Lemma
  B/C (`∠A*BK=90−C`, `∠A*CL=90−B`) numeric-only. Superseded by the solved complex approach.
- trig-decoupled-bash / power-of-point-balance — partial reductions to a residual trig identity (★★).

## Current best
`complex-reality-conditions` is a **complete, rigorous proof** (Full proof below). Certified reusable
lemmas: `lemmas/circumcenter-of-0-k-l.md`, `lemmas/product-to-sum-S.md`,
`lemmas/reality-hinge-directed-angle.md` (Lemma 2), `lemmas/antipode-perp-bisector-equivalence.md`,
`lemmas/physical-slice-imaginary-certificate.md` (the §6.2 mechanism).

## Full proof

Throughout we use directed angles and complex coordinates. Place the plane as ℂ with **A = 0**; write
the affixes of B,C,K,L as `b,c,k,l ∈ ℂ` and `b̄,c̄,k̄,l̄` for their conjugates.

### 0. Setup and non-degeneracies
Since M,N are midpoints of AB,AC and A=0, `M=b/2`, `N=c/2`. Because ABC is a genuine triangle,
`b,c≠0` and A,B,C are non-collinear, i.e. `b c̄ − b̄ c = −2i·Im(b̄c) ≠ 0` **(NC)**. Since K is inside
triangle BMC and L inside triangle BNC, in particular `k−b≠0`, `l−c≠0` **(ND)** (K,L differ from the
vertices B,C). Finally A,K,L are three distinct non-collinear points (the circumcentre O of AKL is
well-defined), so `D := k l̄ − k̄ l = −2i·Im(k̄l) ≠ 0` **(NL)**.

### 1. Circumcentre of {A,K,L}
**Lemma 1.** For non-collinear `0,k,l`, the circumcentre is
`O = (k|l|² − l|k|²)/(k l̄ − k̄ l) = k l(l̄−k̄)/(k l̄ − k̄ l)`.
*Proof.* O is equidistant from 0,k,l. `|O|²=|O−k|²` gives `O k̄ + Ō k = |k|²`; `|O|²=|O−l|²` gives
`O l̄ + Ō l = |l|²`. This linear system in `(O,Ō)` has determinant `k̄l − k l̄ = −D ≠ 0` (NL);
Cramer's rule solving for `O` gives the formula, and `k|l|²−l|k|² = kl(l̄−k̄)`. ∎

### 2. Reducing OM=ON to a polynomial identity
`OM=ON ⟺ |O−b/2|²=|O−c/2|²`. Expanding `|O−z|²=|O|²−(Oz̄+Ōz)+|z|²` and cancelling `|O|²`,
`OM=ON ⟺ T:=2[O(c̄−b̄)+Ō(c−b)] − (cc̄−bb̄) = 0`. With `Ō = k̄l̄(k−l)/D` (since `D̄=−D`), both O,Ō have
denominator `D`; multiplying by `D`,
`T·D = TN := 2kl(l̄−k̄)(c̄−b̄) + 2k̄l̄(k−l)(c−b) − (cc̄−bb̄)D`.
Since `D≠0` (NL), **`OM=ON ⟺ TN=0`.** (One checks `conj(TN)=−TN`, so `TN` is purely imaginary.)

### 3. The three angle conditions as reality conditions
Define signed area `[P,Q,R]:=½Im(conj(Q−P)(R−P))` (`>0 ⟺` CCW). All hypotheses and the conclusion are
invariant under `z↦z̄`, so **WLOG A,B,C is CCW**, i.e. `Im(b̄c)>0` **(CCW)**. Side-of-line dictionary
**(SIDE)**: `z` on the C-side of AB `⟺ Im(b̄z)>0`; `z` on the B-side of AC `⟺ Im(c̄z)<0`.

For distinct P,U,V let `∠(PU→PV):=arg((V−P)/(U−P))∈(−π,π]`. **(SGN)** `∠(PU→PV)∈(0,π) ⟺ [P,U,V]>0`.
**Lemma 2 (reality hinge).** If `θ_1=arg z_1, θ_2=arg z_2 ∈ (0,π)` have equal *unsigned* values, then
`θ_1=θ_2`, so `arg(z_1/z_2)=0` and `z_1/z_2∈ℝ_{>0}`. *Proof.* Each `θ_i∈(0,π)` equals its unsigned
value, so equality of unsigned values gives `θ_1=θ_2` as reals; `arg(z_1/z_2)≡θ_1−θ_2 (mod 2π)` with
`θ_1−θ_2∈(−π,π)` and principal value in `(−π,π]` forces `arg(z_1/z_2)=θ_1−θ_2=0`. ∎

**Interior sign facts.** K inside △BMC (edge BM on line AB, opposite vertex C) ⟹ **(K1)** `Im(b̄k)>0`.
L inside △BNC (edge NC on line AC, opposite vertex B) ⟹ **(L1)** `Im(c̄l)<0`; and since both N,C lie
strictly on the C-side of AB (`Im(b̄N)=½Im(b̄c)>0`, `Im(b̄C)=Im(b̄c)>0`) while B lies on AB, the whole
open interior of △BNC lies on the C-side ⟹ **(L2)** `Im(b̄l)>0`.

**C₁ (`∠KBA=∠ACL`).** `θ_1:=∠(BK→BA)=arg(−b/(k−b))`, `θ_2:=∠(CA→CL)=arg((l−c)/(−c))`; their quotient
is `C_1:=bc/((k−b)(l−c))`. `[B,K,A]=½Im(b̄k)>0` (K1) so `θ_1∈(0,π)`; `[C,A,L]=−½Im(c̄l)>0` (L1) so
`θ_2∈(0,π)`. Lemma 2 ⟹ `C_1∈ℝ`.

**C₂ (`∠LBK=∠LNC`).** With `N=c/2`, `L−N=(2l−c)/2`, `C−N=c/2`, so `β_1:=∠(BL→BK)=arg((k−b)/(l−b))`,
`β_2:=∠(NL→NC)=arg(c/(2l−c))`; quotient `C_2:=(k−b)(2l−c)/(c(l−b))`. `β_2∈(0,π) ⟺ Im(c/(2l−c))>0 ⟺
Im(c̄l)<0` (L1). For `β_1`: (L2) gives `[B,L,A]=½Im(b̄l)>0`, so `φ:=∠(BL→BA)∈(0,π)` equals `∠LBA`; the
hypothesis "K inside ∠LBA" places ray BK in the convex sector, `β_1∈(0,φ)⊂(0,π)`. Lemma 2 ⟹ `C_2∈ℝ`.

**C₃ (`∠LCK=∠BMK`).** With `M=b/2`, `K−M=(2k−b)/2`, `B−M=b/2`, so `γ_1:=∠(CL→CK)=arg((k−c)/(l−c))`,
`γ_2:=∠(MB→MK)=arg((2k−b)/b)`; quotient `C_3:=b(k−c)/((l−c)(2k−b))`. `γ_2∈(0,π) ⟺ Im((2k−b)/b)>0 ⟺
Im(b̄k)>0` (K1). For `γ_1`: from C₁, `θ_2=∠(CA→CL)∈(0,π)`; "L inside ∠ACK" forces `∠(CA→CK)∈(θ_2,π]`,
so `γ_1=∠(CA→CK)−θ_2∈(0,π−θ_2)⊂(0,π)`. Lemma 2 ⟹ `C_3∈ℝ`.

Clearing denominators (all non-zero on an admissible configuration), `C_i∈ℝ ⟺ E_i=0` where
```
E_1 = bc(k̄−b̄)(l̄−c̄) − b̄c̄(k−b)(l−c),
E_2 = (k−b)(2l−c)c̄(l̄−b̄) − (k̄−b̄)(2l̄−c̄)c(l−b),
E_3 = b(k−c)(l̄−c̄)(2k̄−b̄) − b̄(k̄−c̄)(l−c)(2k−b).
```

### 4. Unconditional real-slice certificate (the closure)
Each `E_i` has the form `z−z̄` (its second summand is the conjugate of the first), hence is purely
imaginary, so `E_i=0 ⟺ Im(E_i)=0`; likewise `TN` is purely imaginary, `TN=0 ⟺ Im(TN)=0`. Writing
`b=b_1+ib_2, …, l=l_1+il_2`, all of `Im(E_i), Im(TN)` are real polynomials in the eight real
coordinates.

`E_i` and `TN` are homogeneous of bidegree (2,2) under the similarity `z↦μz` (unbarred `×μ`, barred
`×μ̄`): each scales by `μ²μ̄²`. Applying `μ=1/b` normalizes `b=1` and sends the admissible
configuration to a similar (hence admissible) one, multiplying `TN` by `b^{−2}b̄^{−2}≠0`. So `TN=0`
for the original configuration iff after normalizing `b=1`. Set `b=1` (`b_1=1,b_2=0`), leaving real
unknowns `c_1,c_2,k_1,k_2,l_1,l_2`.

Let `W := |B−K|²·|C−L|²·Im(k̄l)·Im(b̄c) = ((k_1−1)²+k_2²)·((l_1−c_1)²+(l_2−c_2)²)·(k_1l_2−k_2l_1)·c_2`.
On every admissible configuration each factor is non-zero: `|B−K|²>0` (K≠B, ND), `|C−L|²>0` (L≠C, ND),
`Im(k̄l)≠0` (A,K,L non-collinear, NL), `Im(b̄c)=c_2≠0` (A,B,C non-collinear, NC). Hence `W≠0`.

**Certificate.** In `ℚ[c_1,c_2,k_1,k_2,l_1,l_2]` there is the exact polynomial identity
```
W·Im(TN) = f_1·Im(E_1) + f_2·Im(E_2) + f_3·Im(E_3),
```
i.e. `W·Im(TN) ∈ (Im E_1, Im E_2, Im E_3)`. This is an exact, decidable fact, established by reducing
`W·Im(TN)` to normal form `0` modulo a Gröbner basis of the ideal (Buchberger's algorithm — a finite,
exact decision procedure); the reduction succeeds at the first power `W^1`.

Since the identity is polynomial it holds at every real point, in particular at every admissible
configuration (normalized `b=1`), where `Im(E_1)=Im(E_2)=Im(E_3)=0` by §3, so the right side vanishes.
As `W≠0`, `Im(TN)=0`, hence `TN=0`. By §2, `T=TN/D=0` (`D≠0`, NL), so `OM=ON`. Un-normalizing (by the
bidegree-(2,2) homogeneity) gives `OM=ON` for **every** admissible configuration. ∎

### Verification artifacts
`certificate.py` (§4 closure: purely-imaginary check, exact Gröbner membership at `W^1`),
`repro.py` (§1–§3 algebra + the affine/Cramer motivation), `check_s3.py` (§3 sign facts, sanity),
`verify_config.py` (end-to-end `OM=ON` on many valid configurations, sanity). The certificate and the
bidegree-(2,2) homogeneity were reproduced independently by the proof-reviewer.
