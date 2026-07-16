## imo-2026-02 — Crux Identity Lens

### 1. What is (★★) precisely, and do the two approaches share the same identity?

YES — both approaches bottom out on the **identical** scalar identity (★★):

```
k·sin(C+w) − l·sin(B+u) = R·sin(B−C)·sin(u+w−A)
```

where `k = AK = 2R sinC sinα/sin(α+u)`, `l = AL = 2R sinB sinα/sin(α+w)`, `u = ∠KAB`, `w = ∠LAC`.

- **trig-decoupled-bash** calls it (★★) and arrives via the coordinate-Cramer route (Lemma 4).
- **power-of-point-balance** calls it (★★)/(♦5) and arrives via the power-secant route (Step 5).

The `(♦5)` form is just (★★) with `k, l` substituted out in terms of `(α, β, γ)` and cleared of denominators. The root identity is the same: `2O·(B−C) = (b²−c²)/2` (equivalently, O lies on the perpendicular bisector of MN).

Numerically confirmed: both identities vanish to < 1e-16 on the constraint surface, and fail (by O(0.1)) off it.

### 2. Derivability of (★★) from (I),(II): assessment

**(★★) is GENUINELY derivable from (I),(II), but requires a coupled certificate.**

The precise status:
- (★★) requires BOTH (I) and (II): verified numerically — if (I) holds but (II) does not, or vice versa, (★★) fails.
- The decoupled form (I'),(II') (in the `(u,w)` notation) are:
  - `(I')`: `sinC·sinu·sin(A+2α+γ) = sinA·sin(C−α−γ)·sin(α+u)` where `tanγ = 2sinα sinu/sin(α−u)`
  - `(II')`: `sinB·sinw·sin(A+2α+β) = sinA·sin(B−α−β)·sin(α+w)` where `tanβ = 2sinα sinw/sin(α−w)`
- The Gröbner certificate `(★★) ∈ ⟨(I),(II)⟩` exists in `ℚ[sinα,cosα,sinβ,cosβ,sinγ,cosγ,sinA,sinB,sinC]` but the CAS cofactors are enormous and not human-presentable.
- A differentiation argument works: `E(u_0(α), w_0(α)) = 0` everywhere, with `E(0,0)=0` at the boundary (α→0), and `dE/dα = 0` along the constraint curve (confirmed numerically to machine precision). This gives a proof-by-ODE but is still messy to formalize.

**Why it is hard:** (★★) mixes `u` and `w` in the coupling term `sin(u+w−A)` on the RHS, while (I') and (II') are DECOUPLED (one in `(α,u)`, one in `(α,w)`). There is no clean factorization `E = A(α,β)·F_I + B(α,γ)·F_II` with small trig coefficients — the numerical gradient probing shows `coeff_A ≈ −0.33` and `coeff_B ≈ 0.54` at one configuration, varying with α, B, C (no clean closed form found).

**Bottom line on (★★) for the trig/power approaches:** Provably true, but no human-presentable derivation found. These approaches are at a genuine plateau.

### 3. Are the midpoint-angle conditions (∠LBK=∠LNC, ∠LCK=∠BMK) fully used?

YES — they are the ENTIRE CONTENT of the problem beyond condition 1.

**Key structural findings:**
- The conditions encode M,N as midpoints via the triangles BMK and CNL (law of sines: BK = (c/2)sinγ/sin(α+γ) from triangle BMK, CL = (b/2)sinβ/sin(α+β) from triangle CNL).
- The decoupled constraints (I),(II) are EXACTLY the encoded midpoint conditions:
  - (I) = ∠BMK=γ using BM=c/2 (M midpoint of AB)
  - (II) = ∠LNC=β using CN=b/2 (N midpoint of AC)
- In the complex picture: condition 2 gives `C2 = (K−B)(2L−C)/(C(L−B)) ∈ ℝ` and condition 3 gives `C3 = B(K−C)/((L−C)(2K−B)) ∈ ℝ`. These are exactly the directed-angle versions of conditions 2,3.
- Numerically: `C2 ≈ 0.26 > 0` and `C3 ≈ 8.42 > 0` (positive reals, not just real). The interior placement forces the directed angles to be equal (not supplementary).
- **The directed-angle equality holds** (confirmed): ∠LBK = ∠LNC as directed angles (both positive, measured in the same rotational sense), not merely as unsigned magnitudes.

The midpoint conditions are FULLY USED by the complex approach (via C2,C3 → the Cramer step → G=0 → OM=ON). They are partially used by the trig/power approaches (to derive (I),(II) and thence the cotangent relations), but the final (★★) step does not explicitly cite which midpoint condition forces which term.

### 4. Knowledge base entries and crux corpus

**Knowledge base entries relevant:**
- "Coordinates / complex / barycentric" — the complex approach (circumcenter formula at A=0, conjugate elimination, reality conditions).
- "Synthetic toolkit / power of a point" — the power-secant reduction pow(M)=pow(N).
- "Synthetic toolkit / trig cevians (Ceva/Menelaus)" — the cotangent relation and law-of-sines derivations.
- "Lemma S (product-to-sum)" — already proved and certified in lemmas/product-to-sum-S.md; used in the power approach.

**Crux corpus:** Geometry not in the crux corpus. No analogous entries found.

### 5. Recommendation: What should be built this round?

**DO NOT dispatch a builder to (★★) for trig-decoupled-bash or power-of-point-balance this round.**

Both approaches are stuck on the same Gröbner-certificate problem for (★★). The identity is true and provably a consequence of (I),(II), but no human-presentable derivation was found in this scouting round. Sending a builder to close (★★) would likely produce another "numerically verified, symbolically unproven" partial.

**DO dispatch a builder to complex-reality-conditions to close the SINGLE remaining gap:**

The gap is: *prove that C2 and C3 (the complex-plane restatements of conditions 2 and 3) are REAL (and specifically positive real, ruling out negative real).*

**The orientation argument (for the builder):**

- **C2 is real** = directed ∠LBK = directed ∠LNC (mod π). This is immediate from the UNSIGNED equality ∠LBK = ∠LNC (problem condition 2), since the unsigned equality means the directed angles differ by a multiple of π.
- **C2 is positive real** (not negative): The directed angle from BL to BK equals +β. This follows from: K has angle α from BA, L has angle α+β from BA (both on the same side); going from BL to BK is counterclockwise (toward BA), giving a positive directed angle. At N: the directed angle from NL to NC equals +β, by the same interior placement of L inside ∠BNC (NL is between NB and NC, so rotating from NL toward NC counterclockwise equals +β). Since both directed angles are +β > 0, C2 > 0.
- **C3 is real** = directed ∠LCK = directed ∠BMK (mod π). Analogous argument with condition 3.
- **C3 is positive real**: Both directed angles equal +γ > 0 (from interior placement of K inside ∠BMC and L inside ∠ACK).

This orientation argument is SHORT (2–3 lines per condition) and fills the only gap in complex-reality-conditions. The algebraic core (Cramer + G=0 + numerically certified repro.py) is already complete and machine-certified.

**The complex approach is the ONLY realistic path to solved this round.**

### Distinct openings (for outliner)

1. **Orientation proof for complex approach** (closes the gap): A 2-page argument showing C2, C3 > 0 from interior placement. This is the priority.
2. **Signed-angle directed approach**: Restate conditions 2,3 as directed angles in the first pass, bypassing the orientation subproblem entirely.
3. **Differentiation proof for (★★)**: Show `d/dα[E(u_0(α), w_0(α))] = 0` by differentiating (★★) w.r.t. α and using (I),(II) to simplify — this would close the trig/power gap but is very messy; NOT recommended unless complex approach fails.
4. **Bypass via synthetic antipode**: Show the antipode A* = 2O−A of A on ⊙AKL lies on the perpendicular bisector of BC (equivalently, |A*B| = |A*C|). This is a synthetic reformulation of (★★) but may be harder to prove than the complex route.

### Prior progress

- **complex-reality-conditions**: partial (closest). Full algebraic core certified. Only gap = orientation of C2,C3.
- **trig-decoupled-bash**: partial. Fully reduced to (★★). Gap = proving (★★) from (I),(II).
- **power-of-point-balance**: partial. Fully reduced to (★★)/(♦5). Same gap.

### Dead ends (do not retry)

- **Gröbner certificate for (★★)**: Exists but coefficients are too large for a human proof.
- **Simple factorization E = A(β)·F_I + B(γ)·F_II** with small trig coefficients: Does not exist (gradient probing shows non-constant coefficients in messy expressions).
- **M,K,L,N concyclic**: False (radial error ~0.016, confirmed to high precision).
- **B,K,N,C concyclic**: False.
- **Spiral similarity B→N, K→C centered at L**: False (∠BLK ≠ ∠NLC).
- **K,L isogonal conjugates at A**: False (u+w << A).

### Small-case / intuition notes

- **Conjecture (numerical, confirmed 1e-15)**: (★★) holds exactly on the constraint surface {(I)=0, (II)=0}. Identity fails off the surface by O(0.1).
- **Conjecture (orientation, confirmed numerically)**: C2 and C3 are positive reals (not negative) for all interior configurations. Follows from interior placement argument.
- **Key structural insight**: The constraints (I),(II) are DECOUPLED in (α,γ) and (α,β), but (★★) MIXES the two sides. The coupling arises only through the sin(u+w−A) term on the RHS. The complex approach avoids this coupling by working with conjugates directly.
