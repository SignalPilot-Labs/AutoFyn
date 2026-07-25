## Lemma (f(β)>0 on the full interval [0,γ), not just (β0,γ))

**Setup.** WLOG `∠B≤∠C` (so `γ:=min(∠B,∠C)=∠B≤π/2`, `cosB>0`). Write
`f(β):=K_c+P sinβ+Q cosβ`, `P:=½sin(A−B)+3/2 sin(A+B)`, `Q:=−sinA sinB`,
`K_c:=2 sinA sin(A+B)` (as in `lemmas/claim-I-closed-and-claim-II-caseA-
closed.md`). `β0:=(π−A)/3`.

**Theorem.** `f(β)>0` for every `β∈[0,γ)`, for every triangle with
`β0<γ` (the standing domain-nonempty condition), not merely for
`β∈(β0,γ)` as established by Theorem A of `claim-I-closed-and-claim-II-
caseA-closed.md`.

**Proof.**
1. *`f'(β)>0` on all of `(0,γ)`.* This is already established inside the
   certified proof of Theorem A: `f'(β)=P cosβ−Q sinβ=sin(A+β)cosB+
   sin(A+B−β)`, and the sign argument (`cosB>0` since `B<π/2`;
   `A+β∈(0,A+B)⊂(0,π)` so `sin(A+β)>0`; `A+B−β∈(A,A+B)⊂(0,π)` so
   `sin(A+B−β)>0`) uses only `β∈(0,γ)`, never `β>β0` — the certified proof
   never needed the restriction to `(β0,γ)` for this particular fact.
2. *`f(0)=sinA(2sinC−sinB)>0` strictly.* `f(0)=K_c+Q=2sinA sin(A+B)−
   sinA sinB=sinA(2sin(A+B)−sinB)=sinA(2sinC−sinB)` (using `A+B=π−C`,
   `sin(A+B)=sinC`). Since `A∈(0,π)`, `sinA>0`; it suffices to show
   `2sinC−sinB>0`, i.e. `sinB≤sinC` (given, then `2sinC−sinB≥sinC>0`).
   *Proof of `sinB≤sinC`* (`B≤C` by WLOG), by exhaustive cases on `C` vs
   `π/2`:
   - If `C≤π/2`: `0<B≤C≤π/2`, `sin` strictly increasing on `[0,π/2]`, so
     `sinB≤sinC`.
   - If `C>π/2`: `A>0` (genuine triangle angle) gives `π−C=A+B>B`, and
     `π−C<π/2` (since `C>π/2`), so `0<B<π−C<π/2`; `sin` strictly
     increasing on `[0,π/2]` gives `sinB<sin(π−C)=sinC`.
   Both cases exhaust `C∈(0,π)`. Hence `2sinC−sinB≥sinC>0` (using
   `sinC∈(0,1]`, `C∈(0,π)⟹sinC>0`), so `f(0)>0` strictly.
3. *Combine via MVT.* `f` is smooth on `[0,γ)` with `f'>0` on `(0,γ)`. For
   any `β1∈(0,γ)`, MVT on `[0,β1]` gives `ξ∈(0,β1)` with `f(β1)−f(0)=
   f'(ξ)β1>0`, so `f(β1)>f(0)>0`. `∎`

**Caveat (explicit, load-bearing for how this is used).** This does **not**
establish `G(β1)≥0` (where `G(β):=2K_c−f(β)`), which is the actual target
needed in `coordinate-bash-resultant-boundary-pointwise-tangent`'s Case (a)
(`β1≤β0(A)`) — `f` and `G` are related by the fixed exact shift
`G=2K_c−f`, not proportional or co-monotone, so `f>0` says nothing about
the sign of `G`. An explicit counterexample (triangle
`A≈0.010023227880759093, B≈1.4992571585875281`) has `f(β1)≈0.7195>0` but
`G(β1)≈−0.6795<0` — independently reproduced by the proof-reviewer, round
19, from the raw definitions, to 50-digit precision.

## Independent verification (proof-reviewer, round 19)
Re-derived `f(0)`'s closed form, the `sinB≤sinC` two-case argument, and the
MVT combination entirely by hand from the raw definitions — all correct,
no gap. Confirmed the `f'>0`-on-`(0,γ)` fact is already present, unmodified,
inside `claim-I-closed-and-claim-II-caseA-closed.md`'s existing certified
proof of Theorem A (it does not use `β>β0` anywhere).

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-
pointwise-tangent.md` (round 19, "Full proof" Step 3, Sub-result A).

## Status
Certified.
