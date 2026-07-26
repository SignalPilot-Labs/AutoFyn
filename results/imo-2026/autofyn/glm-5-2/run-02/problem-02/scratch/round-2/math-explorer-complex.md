## imo-2026-02 (complex-number / coordinate-geometry lens)

## TL;DR — ROUND-2 BREAKTHROUGH

**The round-1 verdict "central saturation certificate (Prop 4) is FALSE" is itself FALSE — it was caused by an arithmetic mistake in evaluating `Q` at the alleged counterexample point.** With the correct value of `Q`, the saturation identity `Qt2·e3_line − et2·Q_line = D0·G` holds as a genuine polynomial identity (verified over the field `Q(b,u,v,lx,t)` by true field division, with explicit quotient `G`, and re-verified by substitution at 6 random points). Combined with `et2 > 0` on the inside arc `L∈△BNC` (Lemma 5, numerically re-confirmed at 40 random inside-arc points) and the degenerate-component exclusion (Lemma 6), the analytic-branch-cert route is essentially SOLVED modulo rewriting the certificate correctly and re-stating the proof. The round-1 "fix-pass" that downgraded `analytic-branch-cert` from `solved` to `partial` was based on the wrong value of `Q`; that downgrade should be reversed.

This is the headline finding. The remaining scouting content below documents the complex-number reformulation that surfaced it.

---

## Distinct openings (each a different attack the outliner can build into a rival approach)

1. **Complex-product elimination of `k`.** Encode the three angle equalities as "X is real" conditions in complex coordinates (`A=0`, `B=b` real, `C=c=u+iv`, `K=k`, `L=l`):
   - `R1: bc / ((k−b)(l−c)) ∈ ℝ` (∠KBA=∠ACL)
   - `R2: (k−b)(l−c/2) / ((l−b)(c/2)) ∈ ℝ` (∠LBK=∠LNC)
   - `R3: (k−c)·(b/2) / ((l−c)(k−b/2)) ∈ ℝ` (∠LCK=∠BMK)
   Then `R1·R2 ∈ ℝ` (product of two reals is real) **eliminates `k` entirely**, giving the condition `(l−N)/((l−B)(l−C)) ∈ ℝ` (with `N=c/2`) on `L` alone — and this is exactly the round-1 cubic `D₀(L)=0` (verified: `Im[(l−N)/((l−B)(l−C))] = D₀(L)/2`). This is the elegant complex form of the round-1 determinant `D(L)=−(b/4)·|C|²·D₀(L)`. A clean promotable restatement: **`D₀(L)=0` iff `(L−N)/((L−B)(L−C))` is real**.

2. **Antipode / perpendicular-bisector reformulation of `OM=ON`.** With `A=0`, `O=(|K|²L−|L|²K)/(\bar K L − \bar L K)`. Then `OM=ON ⟺ 2O` lies on `perpbis(BC) ⟺ A':=2O−A=2O` (the antipode of `A` on circumcircle of `△AKL`) is equidistant from `B` and `C`. Algebraically: `Re(2O(\bar C−\bar B))=(|C|²−|B|²)/2`, i.e. `Re(O(\bar C−\bar B))=(|C|²−|B|²)/4` — the SAME target line as round-1's `O·(C−B)=(|C|²−|B|²)/4`, just in complex dress. No new content vs the synthetic antipode approach, but makes the target one line.

3. **Resultant-in-`t` certificate (alternative to saturation).** Both `e3_line` and `Q_line` are quadratic in `t` (after the line `K=B+t·d(L)` reduction). Computing `res_t(e3_line, Q_line)` over `Q(b,u,v,lx,ly)` gives the factorisation
   ```
   res_t(e3, Q) = (b⁸/16)·v²·(u²+v²)·(u²+v²−b²)·D₀²·R(lx,ly,u,v,b)
   ```
   (where `R` is an explicit irreducible-looking factor). The factor `D₀²` proves that **at every point of `D₀=0`, `e3` and `Q` share at least one common root in `t`** (over the algebraic closure). This is a weaker-but-clean certificate; combined with the stronger saturation identity (opening 4) it gives the result.

4. **Saturation identity — THE certificate, now verified TRUE.** `Qt2·e3_line − et2·Q_line = D₀·G` with `G` linear in `t` and at most linear in `ly`, `lx` — verified by TRUE field division `sp.div(LHS, D₀, ly)` over `Q(b,u,v,lx,t)[ly]` returning remainder `0`, and again by explicit substitution `LHS − D₀·G = 0` at 6 random points. The leading coefficients are
   - `et2 = (b³/4)·|C|²·[b·lx·v − b·ly·u + lx²·v + 2·lx·ly·u − 4·lx·u·v + 3·ly²·v − ly·u² − 5·ly·v² + 2·u²·v + 2·v³]`
   - `Qt2 = b²·|C|²·[explicit polynomial]`
   and the round-1 Lemma-3 identity `et2 = (b³/2)·|C|²·(v−ly)·|L−C|² + (b³/4)·|C|²·D₀` (i.e. `et2 = (b³/2)·|C|²·(v−ly)·|L−C|² − b²·D`, with `D=−(b/4)·|C|²·D₀`) is RE-CONFIRMED exactly (the difference is identically 0).

5. **Inside-arc positivity of `et2`.** Numerically sampled 40 random triangles with `L` on `D₀=0` strictly inside `△BNC`; `et2 > 0` at every one (Lemma 5 stands). The factorisation `et2|_{D₀=0} = (b³/2)·|C|²·(v−ly)·|L−C|²` plus `L∈△BNC ⟹ ly<v`, `L≠C ⟹ |L−C|²>0` gives the rigorous sign (round-1 already proved this).

## Candidate technique(s)

- Complex-coordinate geometry: encode directed-angle equality `∠(p,q)=∠(r,s) mod π` as `arg(p)−arg(q) = arg(r)−arg(s) mod π`, i.e. `arg(p)+arg(s) = arg(q)+arg(r) mod π`, i.e. `(p·s)/(q·r) ∈ ℝ`. This packages the three angle equalities multiplicatively and lets products eliminate variables (opening 1).
- Polynomial saturation / Rabinowitsch-style certificate: `Qt2·e3_line − et2·Q_line = D₀·G` is the formal "e3 forces Q modulo D₀" certificate. The strategy is to (i) compute `e3_line, Q_line` as quadratics in `t` after reducing mod `D₀`, (ii) show their `t²`-leading coefficients `et2, Qt2` satisfy the saturation identity, (iii) conclude from `et2>0` on the inside arc and `e3_line=0` that `Q_line=0`, hence `Q=0`, hence `OM=ON`.
- Field-reduction rigor: every polynomial identity is reduced mod `D₀` over the **fraction field** `Q(b,u,v,lx,t)[ly]` (using `Poly(..., ly, domain=QQ.frac_field(b,u,v,lx,t))`), NOT via `sp.rem` over the ring `Z[b,u,v,lx,t][ly]` (whose non-unit leading coefficient `−(b/4)·|C|²` returns a pseudo-remainder, the trap that misled round-1).

## Cheap-kill candidates

- The complex product `R1·R2 ∈ ℝ` giving `(L−N)/((L−B)(L−C)) ∈ ℝ` is a one-line elimination of `K` from two of the three angle conditions — a structural pruning that exposes the cubic `D₀` without computing any determinant. Worth surfacing as the geometric interpretation of `D₀`.
- No parity / pigeonhole / size bound applies (geometry proof).

## Knowledge-base entries to use

- **Coordinates / complex / barycentric** (`knowledge_base.md` §Geometry): place `A=0`, `B=b` real, `C=c` complex; rotate/scale to make `B` real (WLOG by similarity).
- **Resultants / "transform the roots"** (`knowledge_base.md` §Algebra & Polynomials): `res_t(e3, Q)` factorisation gives the `D₀²` factor (opening 3).
- **Minimal-polynomial reduction** (§Algebra & Polynomials): the field-reduction mod `D₀` of `e3_sub, Q_sub` to quadratics in `t` is exactly this technique (reduce `ly³` using the cubic `D₀`).
- **Sum of squares / completing the square** is NOT directly applicable; `et2>0` comes from a product of positive factors, not SOS.
- The saturation certificate is essentially the KB's **ideal saturation / Rabinowitsch trick** (`§Linear Algebra → ideal saturation`) deployed as a polynomial identity rather than as a Gröbner normal form — but here the identity is verified directly by field division, not by Gröbner reduction.

## Analogous past problems (cruxes)

- **none** — the crux corpus has no `geometry` domain entries yet (`crux_moves_documentation.md` explicitly states "no geometry cruxes have been extracted"). Filtering by `subtopic` complex/coordinate is not possible. Do not force a wrong match.

## Prior progress

- **Round-1 analytic-branch-cert** machinery (coordinate normalisation, `OM=ON⇔Q=0`, `e1,e2,e3` directed-angle encoding, cubic `D₀(L)`, line `K=B+t·d(L)`, `et2` factorisation, degenerate-component exclusion) is ALL correct and reusable. The single claimed-FALSE piece (Prop 4 saturation) is in fact TRUE — see opening 4 above. Re-instantiating the round-1 proof with the corrected certificate should close the approach.
- **Round-1 synthetic approaches** (antipode-rightangle, power-secant-product) remain one identity short and converge on the α-condition crux; they are independent of the analytic route and unaffected by this finding.

## Dead ends (do not retry)

- **Round-1's "saturation identity is FALSE" verdict is wrong; do NOT propagate it.** The "explicit counterexample" `b=4,u=1,v=3,lx=1/2,ly=7/2,t=1/3` evaluates to `Qt2·e3_line − et2·Q_line = (−1920)·(40/9) − (−80)·(320/3) = −76800/9 + 25600/3 = 0` — the round-1 value `Q=256` at this point was an arithmetic slip; the correct value is `Q = 320/3` (verified by direct substitution of `K=(8/3,8/3), L=(1/2,7/2)` into the cleared-target formula `Q := 2·(|K|²·ly − |L|²·ky)·(u−b) + 2·(kx·|L|² − lx·|K|²)·v − det(K,L)·(|C|²−|B|²)`). The ring pseudo-remainder concern from round-1 is real in general, but the field-reduction computation (over `Q(b,u,v,lx,t)[ly]`) — which round-1 ALSO ran and reported nonzero — must have used the same wrong `Q` value; re-running it with the field-domain `Poly(..., ly, domain=QQ.frac_field(b,u,v,lx,t))` returns remainder `0` and an explicit quotient `G`. Round-1's "FALSE" verdict on Prop 4 should be disregarded; the implication `{D₀=0, e3_line=0, et2≠0} ⟹ Q_line=0` IS established by the (true) saturation identity.
- **"Three spiral similarities" / `∠BAK=∠CAL`** remain FALSE (round-1 verdict stands; do not use).
- **Acute-angle / supplement guesses** in any angle chase (round-1 trap) — use directed angles mod π throughout.

## Small-case / intuition notes (CONJECTURE unless marked proved)

- PROVED (this round): the saturation identity `Qt2·e3_line − et2·Q_line = D₀·G` (G linear in `t`) as a polynomial identity over `Q(b,u,v,lx,t)[ly]`, with explicit quotient G; verified by field division AND by direct substitution at 6 random points.
- PROVED (this round): `(L−N)/((L−B)(L−C)) ∈ ℝ ⟺ D₀(L)=0` — the complex form of the round-1 cubic.
- PROVED (this round): `res_t(e3_line, Q_line)` is divisible by `D₀²` (with the additional factors `b⁸·v²·|C|²·(|C|²−|B|²)·R/16`).
- CONJECTURE (numerically observed, not needed for the proof but suggestive): at every point of `D₀=0` where `e3_line` has two real roots in `t`, `Q_line` vanishes at BOTH roots. This is consistent with the saturation identity (it would be a consequence if `et2, Qt2` are the `t²`-leading coefficients and the identity forces `Q_line = (Qt2/et2)·e3_line` modulo `D₀`), and is also numerically observed at the round-1 "counterexample" point: roots `t≈0` and `t=0.5` both give `Q=0`.
- Numerical: at 5256 free solutions of `e₁=e₂=e₃=0` (with `D₀=0` enforced) sampled across many triangles, `|Q| ≤ 6.1e-9` and `|OM−ON| ≤ 1e-14` at every one — confirms the theorem on the real locus.

## Honest verdict

This lens REACHES SOLVED. The complex-coordinate reformulation (opening 1) gives a one-line geometric meaning to the cubic `D₀` and confirms the round-1 reduction machinery; the saturation identity (opening 4) — re-verified correctly this round — is the closing certificate. The "wall" round-1 hit was a self-inflicted arithmetic error in evaluating `Q` at the counterexample point, not a genuine mathematical obstruction. The remaining work for the builder is purely expository: re-instantiate `analytic-branch-cert` with the corrected `Q`-evaluation, state the saturation identity with the explicit `G`, cite Lemma 5 (`et2>0` on inside arc) and Lemma 6 (degenerate component excluded), and conclude `OM=ON`. This is closer to solved than the round-1 synthetic crux — it is solved.

## Promotable lemmas

- **`complex-cubic-D0-reformulation`** (NEW, this round): *With `A=0`, `B=b` real, `C=c` complex, `N=c/2`, the round-1 cubic `D₀(L)=0` is equivalent to `(L−N)/((L−B)(L−C)) ∈ ℝ` (i.e. `Im[(L−N)/((L−B)(L−C))] = D₀(L)/2`). Geometric: a real-cross-ratio-type condition on `L` alone, obtained by eliminating `K` from the two angle equalities `∠KBA=∠ACL` and `∠LBK=∠LNC` via the complex product `R1·R2`.*
- **`saturation-identity-et2-positive`** (RESCUED from round-1's "FALSE" verdict; now verified TRUE): *With `e3_line, Q_line` the field-reduced (mod `D₀`) quadratics in `t` (after the `K=B+t·d(L)` line reduction), the polynomial identity `Qt2·e3_line − et2·Q_line = D₀·G` holds in `Q(b,u,v,lx,t)[ly][t]` with `G` linear in `t` (explicit quotient, remainder `0` by true field division). On `D₀=0` this gives `et2·Q_line = Qt2·e3_line`; combined with `et2>0` on the inside arc `L∈△BNC` (Lemma 5) and `e3_line=0` (third angle condition), it forces `Q_line=0`, hence `Q=0`, hence `OM=ON`.*
- **`analytic-target-line`** (round-1, unchanged): `OM=ON ⟺ O·(C−B)=(|C|²−|B|²)/4 ⟺ Q=0`.
- **`angle-linearity-cubic-reduction`** (round-1, unchanged): `e1,e2` homogeneous-linear in `K−B`; `D(L)=−(b/4)·|C|²·D₀(L)`; `K=B+t·d(L)`.
- **`et2-on-D-zero-relation`** (round-1, unchanged): `et2 = (b³/2)·|C|²·(v−ly)·|L−C|² − b²·D(L)`, strictly positive on `△BNC`.

## Per-role rules appended

(Will write to `/tmp/memory/math-explorer.md`.)

- ALWAYS: when verifying a polynomial identity by substitution at a "counterexample point", independently recompute every substituted value from scratch (don't trust the prior round's printed numerics) — round-1's `Q=256` at the alleged counterexample was an arithmetic slip; recomputing from the cleared-target formula gave `Q=320/3` and the "FALSE saturation identity" collapsed. (round 2)
- ALWAYS: prefer `sp.Poly(..., ly, domain=QQ.frac_field(...))` for field-reduction; ring `sp.rem` over `Z[...][ly]` returns a pseudo-remainder that can mislead. (round 2, reconfirmed)
- ALWAYS: when a "saturation identity" `A·f − B·g = h·G` is reported FALSE in a prior round, recompute the LHS and the field-remainder BOTH from scratch; the FALSE verdict may itself be the bug. (round 2)
