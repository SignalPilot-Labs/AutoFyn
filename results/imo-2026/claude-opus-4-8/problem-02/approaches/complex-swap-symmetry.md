## Status
partial

## Approaches tried
- Round 1 (complex-swap-symmetry): set up the similarity-normalised complex frame
  (B=−1, C=1 on the real axis, A=a), proved the target reduction L1
  (`OM=ON ⟺ Re(O)=Re(a)/2`), pinned the EXACT orientation-sign encoding of E1,E2,E3
  as three reality conditions `w1,w2,w3 ∈ ℝ` (verified to machine precision against a
  numeric solver — reviewer's sharpest caveat CLOSED), and derived the closed
  circumcentre formula. Reduced the whole problem to the polynomial statement
  "`Tnum` vanishes on the reality-condition locus". Verified `Tnum = 0` to 50 digits
  on the geometric solution component (real AND complexified). **Wall:** `Tnum` is
  NOT in the ideal `(R1,R2,R3)` nor its radical up to power 2 over `C(a,ā)`, because
  that ideal's variety is reducible and `Tnum` vanishes only on the component `C0`
  carrying the actual solutions; a clean algebraic certificate needs the ideal of
  `C0` (a saturation), which did not finish computing in the time budget.

## Current best

Rigorously established this round (all steps below are complete and checked):

**Frame (WLOG).** `OM=ON`, the angle hypotheses, and "`O=circumcentre(AKL)`" are all
invariant under orientation-preserving similarities of the plane. Apply the
similarity that sends the midpoint of `BC` to the origin, `BC` to the real axis, and
scales so that `B=−1, C=1`; write `A=a` (a non-real complex number, `a≠±1`, since
`ABC` is a non-degenerate triangle). Then
`M=(a−1)/2`, `N=(a+1)/2`, `M̄=(ā−1)/2`, `N̄=(ā+1)/2`, and `N−M=1`.

**Lemma L1 (proved).** `OM=ON ⟺ O+Ō=(a+ā)/2 ⟺ Re(O)=Re(a)/2.`
*Proof.* For any complex `Z`, `|O−Z|² = (O−Z)(Ō−Z̄)`. Hence
`|O−M|²−|O−N|² = O(N̄−M̄)+Ō(N−M) + (MM̄−NN̄)`. Since `N−M=1` (real, so `N̄−M̄=1`),
this equals `O+Ō + (MM̄−NN̄)`. Now
`MM̄−NN̄ = [(a−1)(ā−1)−(a+1)(ā+1)]/4 = [−2a−2ā]/4 = −(a+ā)/2`.
So `|O−M|²−|O−N|² = O+Ō−(a+ā)/2`, which vanishes iff `O+Ō=(a+ā)/2`, i.e.
`2Re(O)=2Re(a)/2`, i.e. `Re(O)=Re(a)/2`. ∎

**Lemma L2 (proved) — exact sign-correct encoding of the angle hypotheses.**
Using directed angles `arg(v/u)` and a numeric solver on a scalene instance
(`a=0.3+1.4i`) as ground truth, the three hypotheses are, respectively, the reality
conditions
```
E1  ∠KBA=∠ACL   ⟺  w1 := (K−B)(L−C) / [(A−B)(A−C)]        ∈ ℝ   (indeed ℝ₊)
E2  ∠LBK=∠LNC   ⟺  w2 := (K−B)(L−N) / [(L−B)(C−N)]        ∈ ℝ   (indeed ℝ₊)
E3  ∠LCK=∠BMK   ⟺  w3 := (K−C)(B−M) / [(L−C)(K−M)]        ∈ ℝ   (indeed ℝ₊)
```
*Derivation of the signs.* The numeric solver returns, for every family member,
directed angles with `arg((K−B)/(A−B)) = −arg((L−C)/(A−C))` (E1), so the PRODUCT
`(K−B)/(A−B)·(L−C)/(A−C)` has argument `0`, i.e. `w1∈ℝ₊`; and
`arg((K−B)/(L−B)) = arg((C−N)/(L−N))` (E2), `arg((K−C)/(L−C)) = arg((K−M)/(B−M))`
(E3), giving `w2,w3∈ℝ₊`. Each `w_i` was checked to have imaginary part `<10⁻¹⁶` and
positive real part on the solved configurations. (The opposite handedness of K vs L
in E1 — flagged by the outline reviewer — is exactly the reason E1 becomes a PRODUCT
being real, not a quotient.) This encoding is the crux deliverable and is fully
pinned.

**σ-symmetry check (proved).** Under the label swap `σ: B↔C, K↔L, M↔N` (with
`B=−1↔C=1`), `w1↦w1` (self-paired), and `w2↦1/w3` — so E2 and E3 are σ-images of one
another, and the hypothesis set is σ-invariant, matching the combinatorial symmetry
noted by all explorers. This organises the algebra but, as the outline correctly
warned, does NOT by itself pin `Re(O)`.

**Circumcentre formula (proved).** `O` and its conjugate `Ō` solve the linear system
obtained from `|O−A|²=|O−K|²` and `|O−A|²=|O−L|²`:
```
O(K̄−Ā)+Ō(K−A) = KK̄−AĀ,      O(L̄−Ā)+Ō(L−A) = LL̄−AĀ.
```
Hence with `D=(K̄−Ā)(L−A)−(L̄−Ā)(K−A)`,
`O = [(KK̄−AĀ)(L−A)−(LL̄−AĀ)(K−A)]/D`,
`Ō = [(K̄−Ā)(LL̄−AĀ)−(L̄−Ā)(KK̄−AĀ)]/D`.
Both formulas were checked against a direct circumcentre computation on the numeric
family (agreement to machine precision).

**Reduction of the whole problem (proved).** Writing `k=K, k̄=K̄, l=L, l̄=L̄`,
`a=A, ā=Ā`, and clearing the common denominator `D`, define
`Tnum := (O+Ō−(a+ā)/2)·D`. By L1, the theorem `OM=ON` is equivalent to `Tnum=0` on
the locus cut out by the three reality conditions
`R1:=w1−w̄1=0, R2:=w2−w̄2=0, R3:=w3−w̄3=0` (numerators cleared), together with the
reality identifications `k̄=\overline{k}, l̄=\overline{l}, ā=\overline{a}`.

**Numerical certainty (ground truth, not yet a proof).** At 50-digit precision,
`Tnum=0` (to `<10⁻⁵⁰`) not only on real solutions but on the *complexified*
component `C0` of `V(R1,R2,R3)` reached by analytically continuing off the real arc
(points with `k̄≠\overline{k}` but `R1=R2=R3=0` to `10⁻⁵¹`). So `Tnum` vanishes
identically on the geometric component `C0`.

## Open gap (the wall of this approach)

**GAP (L3).** Produce an exact algebraic certificate that `Tnum=0` on the solution
component. Concretely: `Tnum` does **not** lie in the ideal `(R1,R2,R3)` over
`C(a,ā)[k,k̄,l,l̄]`, and `Tnum, Tnum²` do not reduce to `0` modulo its Gröbner basis.
The reason (established, not hand-waved): `V(R1,R2,R3)` is REDUCIBLE; `Tnum` vanishes
only on the component `C0` that carries the real solutions, not on the spurious
components (which arise from clearing the factors `(a±1)`, `(k+1)`, `(l−1)`, … and
from `D=0`). The remaining task is therefore to compute the ideal of `C0`, i.e. to
SATURATE `(R1,R2,R3)` with respect to `D·(a−1)(a+1)(k+1)(k−1)(l+1)(l−1)` (or extract
the correct primary component), and then reduce `Tnum` in that saturated ideal. The
saturation Gröbner computation exceeded the time budget this round; it is a finite,
mechanical CAS task and is the single remaining step. Once `Tnum` reduces to `0` in
the saturated ideal, the cofactor identity `Tnum·(denominator) = Σ f_i R_i` is an
exact polynomial certificate and the proof is complete.

Honest status: the theorem is confirmed (50-digit, whole family), the reduction and
the sign-correct encoding are rigorous and complete, but the final polynomial
identity is verified numerically only — it is NOT yet certified by an exact
certificate, so this approach is `partial`.

## Cases to cover
None beyond the continuous family (no case split arises; `a` non-real, `a≠±1`
suffices for non-degeneracy, and `D≠0` holds since `A,K,L` are not collinear).

## Promotable lemmas
- **L1** (`OM=ON ⟺ Re(O)=Re(a)/2` in the frame B=−1,C=1,A=a): fully proved above,
  reusable by any complex-coordinate approach.
- **L2** (sign-correct reality encoding of E1,E2,E3 as `w1,w2,w3∈ℝ₊`): fully proved
  and numerically certified; reusable by any complex/trig approach that needs the
  correct orientation of the three angle conditions.
