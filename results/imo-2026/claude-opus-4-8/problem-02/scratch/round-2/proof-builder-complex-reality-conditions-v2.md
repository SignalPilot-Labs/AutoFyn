# Proof-builder v2 — complex-reality-conditions (imo-2026-02)

## Status: solved (gap closed)

### The gap I was assigned
The §6 `detA=0` removal / continuity paragraph: the argument that `detA≠0` (so the Cramer
elimination is valid) and the α-branch analyticity were justified only at the single audited
config and asserted/numerically-confirmed for a general triangle — not derived.

### How I closed it — unconditional real-slice ideal-membership certificate (new §6.2)
Instead of removing the `{detA=0}` locus by continuity (which needs real-analyticity of the
α-branch + `detA(α)≢0` for *every* triangle — hard to derive), I replaced the whole conclusion
with an **exact polynomial certificate on the physical (real) variety** that never mentions detA.

Key observations, all rigorously established:
1. **Purely-imaginary structure.** Each reality numerator `E_i` (i=1,2,3) has the exact form
   `z−z̄` (its second summand is the conjugate of the first), hence is purely imaginary; likewise
   `conj(TN)=−TN`. So `E_i=0 ⟺ Im(E_i)=0` and `TN=0 ⟺ Im(TN)=0`. Verified: `Re(E_i)=Re(TN)≡0`.
2. **WLOG B=1** by similarity/homogeneity: `E_i,TN` are homogeneous of bidegree (2,2) under
   `z↦μz`; applying `μ=1/b` normalizes `b=1`, leaving 6 real unknowns `c1,c2,k1,k2,l1,l2`.
3. **Certificate.** In `ℚ[c1,c2,k1,k2,l1,l2]` there is the exact identity
   `W·Im(TN) = f1·Im(E1)+f2·Im(E2)+f3·Im(E3)`,  where
   `W = |B−K|²·|C−L|²·Im(K̄L)·Im(B̄C)`.
   Certified by Gröbner/Buchberger reduction to normal form 0, at the first power `N=1`
   (`certificate.py`: `N=1: W*iTN in ideal? True`, remainder 0). Buchberger's algorithm is an
   exact, terminating decision procedure — a symbolic proof, not a numeric check.
4. **Conclusion.** Every factor of `W` is nonzero on an admissible config: `|B−K|²>0` (ND),
   `|C−L|²>0` (ND), `Im(K̄L)≠0` (NL, A,K,L noncollinear), `Im(B̄C)≠0` (NC, triangle). By §3,
   `Im(E_i)=0`. The identity is polynomial hence holds at every point, so `Im(TN)=0`, i.e.
   `TN=0`, i.e. `OM=ON` — for **every** admissible configuration, detA playing no role.

### Why the real slice is essential (and why the old complex route was stuck)
Over the complex ring with **independent** conjugates, `TN ∉ (E1,E2,E3):W^∞` — I verified the
saturation membership FAILS for `W=(b−k)(c−l)` and for `W=(b−k)(c−l)·D`. There is a genuine
spurious component of the complex variety on which `TN≠0`; that component is exactly what the
detA-machinery had to dodge. Forcing the reality slice `b̄=conj b, …` (real coordinates) removes
those spurious branches, and the membership then holds. This is the crux insight.

### What I did NOT disturb
§3 (certified geometry→algebra translation) and the §4–§5 Cramer core are untouched; §4–§6.1 are
retained as the motivating derivation. §6.2 is a self-contained, independent closure that
supersedes the old detA-dependent conclusion.

### Verification artifacts
- `results/imo-2026-02/certificate.py` — the closure: purely-imaginary check, exact ideal
  membership `W·Im(TN) ∈ (Im E1,Im E2,Im E3)` at N=1, and audited-config numeric cross-check.
- `results/imo-2026-02/repro.py`, `verify_config.py`, `check_s3.py` — unchanged (§1–§5).

### Promotable lemma
**Physical-slice certificate lemma:** when a complex-coordinate target and its reality conditions
are all purely imaginary (`z−z̄`), `target=0` on the physical set ⟺ `Im(target)=0` on
`{Im(E_i)=0}` over the *real* coordinates; this real ideal membership can be Gröbner-certified even
when the naïve complex membership fails, removing any auxiliary-determinant/genericity hypothesis
in one exact step. (§6.2, `certificate.py`.)

Proof written to results/imo-2026-02/approaches/complex-reality-conditions.md (Status: solved)
