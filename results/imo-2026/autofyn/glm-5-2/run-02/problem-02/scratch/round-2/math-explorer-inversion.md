## imo-2026-02

Lens: inversion / homothety / rotation-composition. I scouted a genuinely different framing (transformation-based) far from the round-1 antipode angle-chase and analytic reduction. Findings below are all NUMERICALLY VERIFIED on 6 triangles (scalene, obtuse, isosceles, small-A-angle) and ~40 configs along the 1-parameter family, residuals reported.

### Distinct openings

**Opening A — Inversion at A, radius²=AB·AC, target = Apollonius circle.** (MAIN RESULT, fully verified.)
- Choose inversion `I` at `A` with `r² = AB·AC`. Then `B'` on ray `AB` at distance `AC`, `C'` on ray `AC` at distance `AB`; `△AB'C' ≅ △ABC` (B,C swapped) — they are mirror images over the A-angle bisector. Midpoint property: `M'=2B'`, `N'=2C'` (holds for ANY radius, since `M=B/2` inverts to `2B'`).
- The circumcircle `Γ=(AKL)` passes through `A`, so `I(Γ\{A})` = line `ℓ = K'L'`. The circumcentre `O` maps to `O' = refl_ℓ(A)` (reflection of A over line `K'L'`). **Verified: `O' = 2P - A` where `P = foot` from A to `K'L'`; residual ≤ 3e-15 on all configs.** (Proof: `O` lies on ray `A·A''` at distance `r²/(2|AA''|)` where `A''=I(A')=I(2O-A)` is the foot from A to ℓ; inverting back, `O'` is at distance `2|AA''|` from A on the same ray, i.e. `A''` is the midpoint of `AO'`.)
- **Target reformulation (PROVED):** `OM=ON ⟺ |AM|·|O'M'|=|AN|·|O'N'|` (from `|I(X)I(Y)|=r²|XY|/(|AX||AY|)`, the `r²` and `|AO|` cancel) `⟺ AB·|O'M'|=AC·|O'N'|`. Since `O'=2P-A` and `M'=2B'-A`, `N'=2C'-A`, `|O'M'|=2|P-B'|`, `|O'N'|=2|P-C'|`, giving
  > **`OM=ON ⟺ AB·|PB'| = AC·|PC'| ⟺ |PB'|/|PC'| = AC/AB = |AB'|/|AC'|`**
  i.e. `P` (foot from `A` to line `K'L'`) lies on the **A-Apollonius circle of `△AB'C'`** (locus `|XB'|/|XC'|=|AB'|/|AC'|`), which passes through `A`. **Verified across 6 triangles: max error 1.3e-13.** The Apollonius circle is exactly `I(pbis(BC))` — the image of the perpendicular bisector of `BC` under inversion. (Because `pbis(BC)={X:|XB|=|XC|}` maps to `{X':|X'B'|/r²·...}` → the Apollonius circle of `B'C'` through `A`.)
- **This is the antipode reduction conjugated by inversion** (since `A'=2O-A` ↔ `A''=I(A')=P=foot`, and `pbis(BC)` ↔ `I(pbis(BC))=Ω`). So it is NOT a fundamentally new reduction — it is the round-1 antipode route viewed through `I`. **Honest verdict: the crux wall is hit ONE STEP LATER, in a different shape** — instead of the sine-product / trig-Ceva identities (T) or (**), the closing step is "P lies on the A-Apollonius circle of `B'C'`", equivalently (sine rule in `△PB'C'` vs `△AB'C'`) the sine-product identity `sin∠PC'B'·sin∠AB'C' = sin∠PB'C'·sin∠AC'B'`. Same crux, inverted variables.

**Opening B — Inverted angle conditions (inscribed-angle form).** The three angle conditions become inscribed-angle equalities on circles through `A` (all verified mod π):
- (1) `∠KBA=∠ACL` becomes `∠AK'B' = ∠C'L'A` (equivalently `∠AK'B' + ∠AL'C' ≡ 0` mod π) — inscribed at `K'` on circle `AB'K'` subtending `AB'` equals inscribed at `L'` on circle `AC'L'` subtending `AC'`. (Note: `∠ACL = -∠AL'C'` mod π, so (1) is `∠AK'B' = -∠AL'C'`.)
- (2) `∠LBK=∠LNC` becomes `∠AL'B' - ∠AK'B' = ∠AL'N'` mod π, i.e. (subtracting `∠AL'N'`) **`∠N'L'B' = ∠AK'B'`** (clean). (Angle between circles `AB'L'`, `AB'K'` at A = `∠AL'B'-∠AK'B'`; angle at N between `NL`→circle `AN'L'` and `NC`→line `AC` = inscribed `∠AL'N'`.)
- (3) `∠LCK=∠BMK` becomes `∠AL'C' - ∠AK'C' = ∠M'K'A` mod π, i.e. `∠M'C'L'... ` (sign-asymmetric to (2)).
- These are DIFFERENT in algebraic shape from round-1's `α,β,γ` direction table — they live on the pencil of circles through `A` rather than on `Γ=(AKL)` — but they do NOT collapse to a 4-point concyclicity. I tested 17 candidate 4-point concyclities among `{A,B',C',K',L',M',N'}`; **NONE hold** (all residuals >0.07). So there is no obvious Miquel structure to exploit in the inverted picture.

**Opening C — Rotation-composition / spiral similarity (NUMERICALLY REJECTED as a clean bypass).** The dispatch warned round-1's naive spiral sims at `A` are FALSE; I verified and extended:
- The three angle conditions pair rotations by equal angles: `R_B^α` (BA→BK) = `R_C^α` (CA→CL); `R_B^β` (BK→BL) = `R_N^β` (NC→NL); `R_C^γ` (CL→CK) = `R_M^γ` (MB→MK). Each pair `(R_X^θ, R_Y^θ)` composes (with opposite signs) to a translation.
- I tested 8 compositions of these paired rotations (including the full `R_M^{-γ}∘R_C^{γ}∘R_N^{-β}∘R_B^{β}∘R_C^{-α}∘R_B^{α}` and several orderings) asking whether any maps `M→N`. **NONE do** (errors 2.2–3.8). So the naive "composition of paired rotations sends `M` to `N`" is FALSE.
- A genuine NON-A spiral similarity DOES exist: centered at `S` (the Miquel point of segments `BK`, `CL`), it sends `B→C` and `K→L` exactly (cost ~1e-32, errors ≤9e-16, verified on 4 triangles). BUT it does NOT send `M→N` (error 0.75–1.27), is NOT `O` (`|O-S|`=0.03–0.46, varying), is NOT on `pbis(MN)`, and is not the arc-midpoint of `BC`. So this spiral sim (which exists for ANY two segments, not special to the config) does not load-bearingly encode the midpoint symmetry `(B,K,M)↔(C,L,N)`.

### Candidate technique(s)
- **Inversion at A** (KB `Geometry — synthetic toolkit, inversion`) + **Apollonius circle** characterization of the perpendicular bisector's image + **reflection-over-line** reformulation of the circumcentre's image. The reduction machinery is clean and fully rigorous.
- **Sine rule** in `△PB'C'` and `△AB'C'` to convert Apollonius-membership to a sine-product identity (the closing step).
- Rotation-composition / spiral-similarity (KB `spiral similarity`) — NOT promising for this problem (naive compositions numerically fail; the genuine non-A spiral sim doesn't carry the midpoints).

### Cheap-kill candidates
- None obvious via parity/pigeonhole (geometry problem). The cheapest structural observation is the inversion radius `r²=AB·AC` choice, which makes `△AB'C'≅△ABC` and `M'=2B'`, `N'=2C'` — this is the single simplification that makes the target readable.

### Knowledge-base entries to use
- `Geometry — synthetic toolkit: inversion, spiral similarity, power of a point` (inversion + reflection-over-line for circumcentre image).
- `Geometry — synthetic toolkit: trig cevians / sine rule` (closing sine-product identity).
- `Geometry — circle/triangle configuration facts` (Apollonius circle = image of perpendicular bisector under inversion at a vertex).
- NOT `spiral similarity` as the primary engine (numerically rejected for the midpoint-symmetry claim).

### Analogous past problems (cruxes)
- None — the crux corpus has NO geometry entries (confirmed in `crux_moves_documentation.md`); the `past_problems_database.json` geometry solutions are unstructured. No load-bearing move retrieved.

### Prior progress
- The inversion route REDISCOVERS the round-1 antipode reduction in inverted form: `OM=ON ⟺ P∈Ω` (Ω = A-Apollonius circle of `B'C'` = `I(pbis(BC))`) is exactly `OM=ON ⟺ A'∈pbis(BC)` conjugated by `I`. The promotable new content: (i) the image of the circumcentre `O' = refl_{K'L'}(A)` (a clean reflection formula, no `O` or `R` left); (ii) the inverted angle conditions (1'),(2'),(3') as inscribed-angle equalities on the pencil of circles through `A`; (iii) the Apollonius-circle target as a single circle-membership (alternative to the trig-Ceva identity (T) and the secant crux (**)).

### Dead ends (do not retry)
- **Naive rotation compositions mapping M→N**: 8 tested, ALL FAIL numerically (errors 2–4). Do not propose "composition of paired rotations sends M to N" — it is FALSE.
- **Spiral similarity at the Miquel point S of BK, CL sending (B,K,M)→(C,L,N)**: the B→C, K→L part is exact but M→N FAILS (error 0.75–1.27). Do not propose "one spiral sim realizes the (B,K,M)↔(C,L,N) symmetry."
- **4-point concyclities among `{A,B',C',K',L',M',N'}`**: 17 tested, NONE hold. No Miquel structure in the inverted picture.
- **"AP along the A-bisector" as the target**: my initial derivation was WRONG (B', C' are not on line K'L', so △APB' is not right-angled). The correct target is Apollonius-circle membership, NOT "AP bisects A".

### Small-case / intuition notes (CONJECTURE, numerically certain)
- The theorem holds to 1e-13 on all 6 triangles and ~40 configs; the Apollonius characterization `|PB'|/|PC'|=AC/AB` holds identically along the whole 1-param family. (Conjecture only in the sense that no closed-form proof of the closing step is given here.)
- The inversion route is the antipode route in disguise: same crux, different shape. It is worth offering the outliner as a RIVAL framing ONLY IF the inverted sine-product identity `sin∠PC'B'·sin∠AB'C' = sin∠PB'C'·sin∠AC'B'` (with conditions (1'),(2'),(3')) admits a cleaner closing lemma than round-1's (T)/(**) — e.g. via an Apollonius-angle lemma or a Miquel point on the pencil of circles through A. The three inverted conditions are inscribed-angle statements, which a builder might combine more cleanly than the round-1 direction-table chase, but I could not find the combination in this round.

### Promotable lemmas
- **Lemma (inversion image of the circumcentre).** *Under inversion at A of any radius, with Γ=(AKL)→line ℓ=K'L', the circumcentre O of Γ maps to `O' = refl_ℓ(A)`, the reflection of A over ℓ.* Proof: antipode `A'=2O-A` is the farthest point of Γ from A; `A''=I(A')` is the foot of the perpendicular from A to ℓ; `O'` lies on ray `AA''` at distance `2|AA''|`, so `A''` bisects `AO'`. VERIFIED 1e-15. (Reusable by any inversion-based approach to circumcentre-equidistance problems.)
- **Lemma (inversion reduction of OM=ON).** *Under inversion at A with `r²=AB·AC`, `OM=ON ⟺ P∈Ω` where `P`=foot from A to line `K'L'` and `Ω`=A-Apollonius circle of `△AB'C'` (≡ of `△ABC`), equivalently `|PB'|/|PC'|=AC/AB`.* Proof + 6-triangle verification above. (This is the antipode reduction conjugated by inversion; importable as an alternative target.)
- **Lemma (inverted angle conditions).** *Under the same inversion, the three hypotheses become: (1') `∠AK'B' + ∠AL'C' ≡ 0`; (2') `∠N'L'B' = ∠AK'B'`; (3') `∠AL'C' - ∠AK'C' = ∠M'K'A` (all mod π).* Verified mod π. (Reusable by any approach building on the inverted picture.)
