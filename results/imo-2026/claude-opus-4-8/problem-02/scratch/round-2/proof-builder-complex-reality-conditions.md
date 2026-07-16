# Proof-builder report — complex-reality-conditions (imo-2026-02), Round 2

## Outcome: SOLVED (Status flipped partial → solved)

The one remaining gap — a rigorous synthetic derivation of the three reality conditions
`C1,C2,C3 ∈ ℝ` from the unsigned-angle equalities and the interior hypotheses — is now closed.
The certified algebraic core (§4–§6: Cramer elimination in monomials `(k̄l̄, k̄, l̄)`, consistency
relation, factorizations `Rnum=(b−k)(c−l)·G`, `num=qN·G` forcing `G=0`, continuity removal of
`detA=0`) was left completely intact and re-verified (`repro.py` still prints identities (I),(II) = True).

## What I rewrote (entire §3)

Replaced the round-1 "asserted + numerically confirmed" §3 (which was the exact reason for the
round-1 downgrade) with a genuine signed-area / directed-angle derivation:

- **§3.0 Conventions + orientation reduction.** Fixed signed area `[P,Q,R]=½Im(conj(Q−P)(R−P))`
  (standard: >0 ⟺ CCW; sanity-checked on `0,1,i`). WLOG CCW via the reflection `z↦z̄` (isometry,
  preserves unsigned angles/interior/distances, flips orientation). Side-of-line dictionary (SIDE):
  `z` on C-side of AB ⟺ `Im(b̄z)>0`; `z` on B-side of AC ⟺ `Im(c̄z)<0`.
- **§3.1 Reality hinge (Lemma 2) — the load-bearing hinge the reviewer demanded be written out.**
  Sign rule (SGN) `∠(PU→PV)∈(0,π) ⟺ [P,U,V]>0`. Lemma 2: if `θ1=arg z1, θ2=arg z2 ∈(0,π)` with
  equal unsigned angles then `arg(z1/z2)=θ1−θ2` **exactly** (both principal values in `(−π,π]`,
  congruent mod 2π ⇒ equal), and `θ1=θ2` so `z1/z2>0`. This kills the supplementary branch:
  difference of two numbers in `(0,π)` is in `(−π,π)` and equals 0, not π.
- **§3.2 Interior facts (K1),(L1),(L2)** each derived as a one-line consequence of "interior of the
  named triangle" via edges on lines AB / AC: `K∈BMC ⇒ Im(b̄k)>0`; `L∈BNC ⇒ Im(c̄l)<0` and `Im(b̄l)>0`.
- **§3.3/§3.4/§3.5 — C1, C2, C3.** For each: (a) express `arg Ci = angle1 − angle2` as an exact
  quotient of ray-ratios (midpoint factors written out: `L−N=(2l−c)/2`, `K−M=(2k−b)/2`, and line
  `BM=`line `AB`, line `NC=`line `AC`); (b) prove both directed angles ∈(0,π). The two subtle
  "inside-angle" cases handled by convex-sector betweenness:
  - `β1` (K inside ∠LBA): (L2) gives `[B,L,A]>0`, so `φ=∠(BL→BA)∈(0,π)`; K in the convex sector
    ⇒ `β1∈(0,φ)⊂(0,π)`.
  - `γ1` (L inside ∠ACK): reuse `θ2=∠(CA→CL)∈(0,π)` from §3.3; L interior forces `∠(CA→CK)∈(θ2,π]`,
    so `γ1=∠(CA→CK)−θ2∈(0,π)`.
  Then Lemma 2 ⇒ each `Ci∈ℝ_{>0}`.
- **§3.6** Reality ⇒ the polynomial system `E1=E2=E3=0` (unchanged; feeds §4).

## Convention pitfall caught
The round-2 explorer's report asserts `signed_area(N,C,L)>0` / `signed_area(B,M,C)>0`, which use the
OPPOSITE signed-area sign convention (`Im((Q−P)conj(R−P))`). Under the standard convention those are
negative. I did NOT rely on the explorer's sign claims; I re-derived every inequality from scratch in
terms of `Im` of monomials `b̄k, c̄l, b̄l, b̄c`. Conclusions (each Ci real & positive) unchanged.

## Verification (sanity only, not the proof)
- `check_s3.py` (new artifact): on a valid CCW config, confirms `Im(b̄c)=3>0`, `Im(b̄k)=0.199>0`,
  `Im(c̄l)=−0.556<0`, `Im(b̄l)=1.80>0`; all six directed angles θ,β,γ ∈(0,π) with θ1=θ2, β1=β2,
  γ1=γ2; exact arg-identities `arg Ci = angle1−angle2` (True); `C1,C2,C3 ∈ ℝ_{>0}`.
- `repro.py`: identities (I) `Rnum=(b−k)(c−l)G` and (II) `num=qN·G` still True; core intact.

## Files
- Proof: `results/imo-2026-02/approaches/complex-reality-conditions.md` (Status: solved)
- New verification artifact: `results/imo-2026-02/check_s3.py`
- Core certificate (unchanged): `results/imo-2026-02/repro.py`

## Promotable lemma proposed to reviewer
- **Lemma 2 (reality hinge for directed angles)** with companions (SGN),(SIDE): mechanism to turn an
  unsigned angle equality into an exact directed-angle equality (mod 2π) once both directed angles are
  pinned to (0,π). Reusable in any complex-coordinate angle-condition geometry problem.

## Residual risk for the reviewer
None identified in §3. Every inequality is a signed-area statement; every arg step is exact (principal
values). The `∠(CA→CK)∈(θ2,π]` betweenness claim for γ1 and the analogous β1 sector argument are the
only spots relying on a geometric "inside the convex sector" description of the hypothesis — stated
explicitly, not hand-waved. §4–§6 were already certified in round 1.
