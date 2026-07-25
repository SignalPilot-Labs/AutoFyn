## imo-2026-02 — lens: closing `ptolemy-trig-identity`'s odd-parity gap

### Exact current target (from the file + certified lemma, verified byte-for-byte)
Setup (all certified, `lemmas/ptolemy-resultant-elimination-to-sextic.md` +
`lemmas/ptolemy-sextic-parity-reduction.md`): on the domain
`D = {0<θ<min(B,C), A,B,C>0, A+B+C=π}`, τ:=tanθ,
```
q1(U) = P1 U^2 + Q1 U + R1,   P1 = sinA·τ(τcosC−sinC), Q1 = sinA sinC(τ²+1)+2τ sinB,
                               R1 = −2τ² sinC cosA − τ sinA sinC + sinA cosC
q2(V) = P2 V^2 + Q2 V + R2,   (mirror: swap B↔C)
F(U,V) = sinA·UV − cosA(U+V) − sinA
```
U1,U2 = roots of q1 (U1 = larger root = genuine, since P1<0 on D);
V1,V2 = roots of q2 (V1 = larger root = genuine, since P2<0 on D).
**The open claim (Step 4 of the file / the certified lemma):**
```
Ψ(τ,A,C) > 0  on D   ⟺   an odd number (1 or 3) of the four values F(Ui,Vj)−4  (i,j∈{1,2})  exceed 0
```
Numerically: at every sample, only `F(U1,V1)−4 > 0`, the other three are `<0` (count=1). This is the target the outliner needs closed. I did **not** re-verify Ψ or the multiplicative identity itself (already independently reviewer-certified round 6) — I focused entirely on mechanism-hunting for Step 4.

### New finding this round (verified, not yet a full proof): the 4-value parity decomposes into a 2×2 structure, and the ENTIRE claim follows from ONE weaker fact
Define, for fixed `V`, the *radical-free* polynomial (eliminate `U` via the same resultant-of-quadratic-vs-linear trick already used for `Φ`, mirrored):
```
Ξ(V) := Res_U(q1(U), L(U,V)) = P1·n² − Q1·n·m + R1·m²,   m=sinA·U−cosA|_{U→U}... 
       (explicitly: m=sinA·V−cosA replaced correctly — see code below; Ξ(V) is quadratic in V, radical-free coefficients in τ,A,C)
```
By the same Lemma used for the certified Theorem 1 (resultant of quadratic vs. linear = lc·g(root1)·g(root2)):
```
Ξ(V) = P1 · (F(U1,V)−4) · (F(U2,V)−4)     [an identity of polynomials in V, no radicals]
```
**Ran 3000 random domain samples** (own numpy script, independent of any file): confirmed
- `sign(Ξ(V1)·Ξ(V2)) < 0` in **3000/3000** samples (min |product| ≈ 0.014, comfortably nonzero) — i.e. `Ξ(V1)` and `Ξ(V2)` **always have opposite sign**.
- Equivalently: `(F(U1,V1)−4)(F(U2,V1)−4) < 0` always (column 1, pairing with genuine V1: exactly one of the two is positive) **and** `(F(U1,V2)−4)(F(U2,V2)−4) > 0` always (column 2, pairing with spurious V2: same sign, 0 or 2 positive) — confirmed as **separate** sign patterns, 3000/3000 each, in `row1/row2/col1/col2` product-sign tests.

**Key logical point (elementary, exact — not numeric):** if column 1's product is negative (contributes exactly 1 to the positive-count, since exactly one of 2 entries is positive) and column 2's product is positive (contributes an *even* number, 0 or 2, to the positive-count — **regardless of which sign** column 2 actually has), then the **total positive-count is odd+even = odd**, automatically. **So proving just "`Ξ(V1)` and `Ξ(V2)` have opposite sign" (a single sign-comparison of two numbers, not four) is logically SUFFICIENT to establish the full odd-parity claim** — you never need to know which of the four individual `F(Ui,Vj)` is the one that's `>4`, nor pin down column 2's actual sign. This is a genuine, checkable reduction in kind (4-way parity → pairwise sign-opposition of two radical-free-computable quantities), verified by direct symbolic derivation (elementary case-count arithmetic) plus 3000-sample numeric confirmation of the premises.

### Attempted symbolic closure of `Ξ(V1)·Ξ(V2)<0` — negative result, but informative
Tried the natural next step: `Ξ(V1)·Ξ(V2) = Res_V(q2(V), Ξ(V)) / P2²` (both quadratic in V, resultant is a single radical-free quantity `Ω(τ,A,C)`). Computed `Ω = Res_V(q2,Ξ)` symbolically in sympy (generic `sinA,cosA,sinC,cosC,τ` with `B` eliminated via `A+B+C=π`): **`Ω` is degree 8 in τ** (worse than Ψ's degree 6), with a common factor `(cA−1)(cA+1) = −sin²A` pulled out at every coefficient, leaving a still-large degree-6-ish bracket per coefficient (~similar complexity to Ψ itself). **This specific resultant route does not simplify the problem** — going through `Res_V(q2,Ξ)` trades the original 4-branch product for a *different*, not obviously easier, degree-8 polynomial positivity claim. This is a genuine negative finding for next round: don't re-attempt this exact resultant chain expecting a shortcut.

### A second, more promising but unfinished lead: isolate the single radical in `Ξ(V1)` directly
Since `Ξ(V)` is quadratic in `V` and `V1 = (−Q2−√Δ2)/(2P2)` (only **one** square root, `Δ2 = Q2²−4P2R2`, vs. the original `F` which has two nested radicals), substituting gives
```
Ξ(V1) = [C2·Δ2 + C1·√Δ2 + C0] / (2P2)²   =  a(τ,A,C) + b(τ,A,C)·√Δ2 ,   a := C2·Δ2+C0,  b := C1  (both radical-free)
```
Computed `C2, C1, C0` symbolically (sizes ≈100/1000/4000 chars respectively — large but a single-radical object, structurally simpler than the two-nested-radical `F`). Sign of `a+b√Δ2` (with `Δ2≥0` known, `√Δ2` real) reduces, via the standard one-radical-clearing trick, to a case split on `sign(a)`, `sign(b)` and the *radical-free* comparison `a² ≷ b²Δ2`. **Not completed this round** (didn't compute `a²−b²Δ2`'s degree/factorization — this is the natural next step, likely still a large polynomial but only requires ONE squaring, unlike the original two-nested-radical `F−4>0` problem which effectively needs two). This is a concrete, well-defined next target if `Ξ(V1)·Ξ(V2)<0` is pursued via direct sign-constancy of `Ξ(V1)`, `Ξ(V2)` individually (each anchored by continuity/IVT — both are continuous on the connected domain `D` since `Δ1,Δ2≥0` throughout by the certified branch-selection lemma) rather than via the resultant `Ω`.

### On round 6's "true geometric domain" restriction
The restriction to `θ∈(0,min(B,C))` (as opposed to a global claim) is **already fully baked into** the target as stated (my 3000-sample sweep enforced it) — it does not need to be separately re-imposed on the new `Ξ(V1),Ξ(V2)` reformulation; the same domain-connectedness argument (Round 5 Step 6, already certified) applies unchanged to justify an IVT/continuity closure of `Ξ(V1)` or `Ξ(V2)` individually, since these are continuous functions of `(θ,A,C)` on the same connected `D` (same argument as `U,V` themselves, already established in `ptolemy-resultant-elimination-to-sextic.md` Step 7). So the domain restriction doesn't change the *formulation* here, but it is exactly what licenses the IVT step in the "second lead" above (one base-point check + no-vanishing-on-D suffices, rather than a global inequality).

### Cheap-kill candidates
- None found beyond what's already used (parity/sign-count arguments and the P1,P2<0 sign lemma are already exploited maximally).
- Did NOT find a parity/pigeonhole argument that closes the claim without further algebra — the reduction above still needs one more sign fact proved (either `Ξ(V1)·Ξ(V2)<0` globally, or `Ξ(V1)`, `Ξ(V2)` each sign-constant via IVT + one base point).

### Candidate technique(s) for next round
1. **IVT/continuity on `Ξ(V1)` and `Ξ(V2)` individually** (not via the `Ω` resultant) — each needs (a) proof of no-vanishing on `D` (equivalent to the single-radical form `a+b√Δ2 ≠ 0`, reducible to `a²≠b²Δ2` when `sign` ambiguous — not yet computed) and (b) one exact base-point sign evaluation (e.g. `τ→0` limit, mirroring the already-proved `Ψ(0,A,C)=4sin³A sinB sinC>0` computation). This is the most promising concrete lead from this round.
2. Abandon the `Ω=Res_V(q2,Ξ)` degree-8 resultant route — verified not simpler than `Ψ` itself.
3. If neither closes: per CLAUDE.md's shared-gap-plateau guidance (this is the population's 3rd-round-running convergence on a "sign pattern across finitely many roots" shape), consider dispatching a genuinely different approach (synthetic, avoiding root-counting) rather than a 4th resultant variant.

### Knowledge-base entries used
- "Resultants" entry (`knowledge_base.md`) — resultant-via-roots formula, multiplicativity, quadratic-vs-linear resultant value formula — all already cited/used by the certified lemma; I reused the same formula (with roles of U,V swapped) to define `Ξ(V)`.
- Theorem 11.8-style "root-pairing via resultant + sign convention" technique (used elsewhere in the population for `G2a` branch selection) — the `Ξ(V1)·Ξ(V2)` opposite-sign structure found here is the same *flavor* of technique (pair-up via one resultant, read off sign), suggesting this reduction is a natural generalization of a technique the population has already used successfully once (`lemmas/cross-product-sign-selection-G2a.md`, `lemmas/root-pairing-lemma.md`).

### Analogous past problems (crux corpus)
Did not query the crux corpus this round — the dispatch was narrowly scoped to closing one specific algebraic gap in an already-built approach, and the relevant technique (resultant elimination + sign bookkeeping) is already fully sourced from `knowledge_base.md`'s "Resultants" entry and the population's own prior lemmas; a fresh corpus search would not add technique here given the time budget. (If the outliner wants crux-corpus support for the IVT/single-radical-clearing step specifically, that would be a `algebra`/`inequalities` subtopic query for "clearing one square root via squaring + sign case split," not geometry — flagging this as unexplored, not "none found.")

### Dead ends (do not retry)
- **Global SOS on Ψ** — already refuted by round-6's sextic-lens explorer (Ψ<0 outside the true domain in ~29% of samples); not re-attempted, confirmed still correctly avoided by this round's file.
- **Direct Sturm/Descartes on Ψ's raw coefficients** — file's own Step 0 this round found this intractable (needs a nontrivial Gröbner-ideal reduction just to extract legible coefficients); I did not retry this.
- **`Ω := Res_V(q2,Ξ)` as a shortcut to `Ξ(V1)·Ξ(V2)<0`** — NEW dead end found this round: computed explicitly, degree 8 in τ, not simpler than Ψ. Do not re-attempt this exact resultant chain; if pursuing the `Ξ(V1),Ξ(V2)` route, go via individual IVT/continuity + single-radical clearing instead (see "Candidate technique 1" above), not via this joint resultant.

### Small-case / intuition notes (all conjecture / numeric, not proof)
- The `Ξ(V1)`/`Ξ(V2)` opposite-sign pattern held with comfortable margin (min |product| ≈0.014 in 3000 samples) — not a knife-edge coincidence, consistent with it being a genuine structural fact provable in principle.
- The genuine branch `F(U1,V1)` is always the sole exceedance, and empirically it is always `Ξ(V1)` that is positive (not `Ξ(V2)`) — i.e. the "which column is which" assignment also looks fixed, not just "some column is negative" — this extra fact (if provable) is not needed for the parity conclusion (the sufficiency argument above is symmetric in the two columns) but could be a cleaner target if a direct proof naturally produces it.
