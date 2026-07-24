# Concentration lemmas (Lemma 1, Concentration Exclusion, Reduction Lemma) — CERTIFIED round 7

Source: `concentration-exclusion-rigidity` §1–§3. Reviewer re-derived all three (cofactor arithmetic +
imported certified M2/M3) and numerically verified. Setting: the tied non-degenerate Φ-max minimizer
`P*`, incidence `U`, values `w_1>…>w_p`, `Uw=b`, `ker U={0}` (S-core), `f=Σ_j s_j w_j` (BF), `s_j=σ_{a_j}`
if `|C_j|` odd else `0`. A class `C_j` is **concentrated** if its column is `m·e_k` (`m=|C_j|≥2`, all
copies in one piece `2^k`, value not shared).

## Lemma 1 (concentration divides the determinant)
Square case (`p=n+1`): a concentrated class with column `m·e_k` forces `m∣det(U)`, so `|det U|≥m≥2`.
*Proof.* Cofactor-expand `det(U)` along column `j=m·e_k`: `det(U)=m·(-1)^{k+j}M_{k,j}`, an integer
multiple of `m`. `ker U={0}` ⟹ `det U≠0`. ∎

## Theorem 2 (Concentration Exclusion)
At `P*`, every concentrated class has `m=2`, and every such class is **invisible** (`s_j=0`); i.e. no
**visible** class is concentrated.
*Proof.* By certified `two-invisible-pairs-mult-bound` (M2), `μ_{k,j}≤3`, so `m∈{2,3}`. If `m=3` (odd),
certified `symmetric-odd-block-move` (M3) forces `μ_{k,j}≤1`, contradicting `μ_{k,j}=3` — excluded.
Hence `m=2`; then `|C_j|=2` even ⟹ `s_j=0`. ∎
Corollary: the fatal unshared instance `{2,4/3,4/3,4/3,1}` (column `3·e_k`, odd `m=3`) is excluded
directly by M3 — a variational/Φ-maximality argument, NOT reduced to another route's Gap B.

## Lemma 3 (invisible-concentration peeling)
Square case: an invisible `2·e_k` column `j` satisfies `det(U)=(-1)^{k+j}·2·det(U')` (`U'`=delete row
`k`, col `j`); the reduced system `U'w'=b'` (`b'=(2^l)_{l≠k}`) holds with every value unchanged
`w_i=w'_i`, and for each visible `i≠j`, `w_i=det(U'_i)/det(U')`. Hence
`f=Σ_{i≠j: s_i≠0} s_i det(U'_i)/det(U')`, a Cramer expression for the strictly smaller distinct-powers
instance `(U',b')`. Iterating removes every invisible concentrated column, giving a
concentration-free `(U^★,b^★)` with the SAME `f`.
*Proof.* Cofactor-expand `det(U)` and each `det(U_i)` along column `j=2e_k`; the factor `2·(-1)^{k+j}`
cancels in the ratio `w_i=det(U_i)/det(U)=det(U'_i)/det(U')`. Concentration in piece `k` only makes
every row `l≠k` read `Σ_{i≠j}μ_{l,i}w_i=2^l`, i.e. `U'w'=b'`. ∎

## Verification (reviewer, independent)
- `{2,4/3,4/3,4/3,1}`: `4/3`-column `=3·e_3`, `det U=3`, `3∣3`, `f=5/3`, `f·det U=5` — Lemma 1.
- `n=3` minimizer `{3,3,2,2,2,2,1}` (piece8=`{3,3,2}`): `Uw=b` confirmed, `f=1`; value `3` is an
  invisible `2·e_8` matched pair; the `4×3` maximal-minor gcd `=2` — confirming the **negative finding**
  that even matched pairs make the maximal-minor gcd even, so "benign-U = det/gcd `±1`" is literally
  FALSE; the correct target is benign-ness of the reduced **visible** (`s_j≠0`) subsystem.

## Scope / honest limits
Fully characterizes and removes the single-column concentration obstruction. Does NOT close the residual:
after peeling, the concentration-free visible subsystem `U^★` still needs `|det U^★|=1` (square) /
coprime maximal minors (rect) — the same minimality⇒benign-U wall as Gap A′/Gap D — plus Positivity.
The rectangular minor-gcd bookkeeping is stated, not fully carried out.
