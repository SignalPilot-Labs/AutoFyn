# Build report — trig-decoupled-bash (imo-2026-02)

**Status: partial** (real, substantial progress; one scalar identity remains).

## What I proved (in full)
- **Lemma 1:** OM = ON ⟺ O_x = (M_x+N_x)/2 = (2c cos B + a)/4 (MN ∥ BC + perp-bisector). Complete.
- **Lemma 2:** the A-at-origin power-of-point identity **(★)**
  `|k|²[(γ⃗−β⃗)×l] − |l|²[(γ⃗−β⃗)×k] = ((b²−c²)/2)(k×l)` is exactly equivalent to OM = ON,
  via Cramer's rule on `2(O−A)·k=|k|², 2(O−A)·l=|l|²`. Complete, and constraint-free
  (this is the vector form of the shared crux MA′/NA″ = b/c).
- **Lemma 3:** full angle parametrization — `AK=c sinα/sin(α+u)`, `AL=b sinα/sin(α+w)`,
  the decoupled constraints **(I)** [α,γ] and **(II)** [α,β], the cotangent relations
  `cot u=cotα+2cotγ`, `cot w=cotα+2cotβ`, and the **unique interior-root selection**
  (γ∈(0,C−α), β∈(0,B−α)). All derived and numerically confirmed to 1e-15.
- **Lemma 4:** (★) reduces cleanly to the single scalar identity **(★★)**
  `AK·sin(C+w) − AL·sin(B+u) = ((b²−c²)/(2a))·sin(u+w−A)`.

So the ENTIRE problem is reduced, by an exact chain of equivalences, to (★★). (★★) is
verified to <1e-16 across five scalene configs (`verify_starstar.py`).

## Remaining gap (precise)
Prove (★★) symbolically from (I),(II). Equivalently: the cleared quantity
`E = |k|²l_y − |l|²k_y − s(k×l)` (s=(b²−c²)/(2a)) lies in the ideal ⟨R_I, R_II⟩ of the two
constraint polynomials. Established facts about this gap:
- E vanishes EXACTLY on {R_I=0, R_II=0} and is nonzero off it (both constraints are needed —
  matches the explorer's "identity fails for arbitrary (α,β,γ)").
- E is NOT of the form f(γ)·R_I + g(β)·R_II with single-variable coefficients (tested: small
  nonzero least-squares residual). The certificate coefficients are genuinely multivariable.
- Next-round route: produce the ideal-membership certificate via Gröbner/resultant elimination
  in sympy (converting sin/cos to polynomial variables with Pythagorean relations), transcribe
  as named trig steps; OR find a symmetric closed form for the common value
  `W_y = (|k|²−s k_x)/k_y` (the y-coordinate of the antipode A*−A), whose B↔C symmetry would
  give (★★) in one line. The antipode A* satisfies A*_x = a/2 (A* on ⊥-bisector of BC), which
  is exactly the antipode-approach reformulation — the two approaches meet here.

## Spec concerns
- None fatal. The outline's "balance lemma via B↔C symmetry" is real but the naive
  "same functional form f, ratio b/c" does not by itself close (★★) — the symmetry makes E
  antisymmetric under σ:(B↔C,u↔w,b↔c), which is a necessary check but not a proof; the
  coupling term `sin(u+w−A)` on the RHS still needs the constraints. The remaining work is
  the honest computational core, not a bookkeeping fix.
- The clean reduction to (★★) is new this round and is the most promotable asset; Lemmas 1,2
  are certifiable as shared lemmas immediately.
