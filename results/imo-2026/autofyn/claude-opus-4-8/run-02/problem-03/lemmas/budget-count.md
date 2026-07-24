# Lemma: budget-count (Lemma BUDGET-COUNT, counting reformulation + receiver bound)

**Certified round 8** (dual-integer-certificate). Reviewer-verified.

Notation: `R` an all-even refinement of `W_n`; `r_k≥1` = # sub-pieces of piece `2^k`;
`T=Σ_k r_k=(n+1)+N` total sub-pieces; `N` = cut count. `Budget(n)` = "every all-even `R` has `N≥n+1`".

## Statement
1. **Reformulation.** `Budget(n) ⟺ T≥2(n+1) ⟺ Σ_k(r_k−2)≥0` (all-even forces `T` even, so
   `T≤2n+1 ⟺ T≤2n < 2(n+1)`).
2. **Uncut pieces point strictly upward.** Fix a perfect matching `Π` of the sub-pieces by equal
   value (each even value-class paired internally). If piece `2^k` is uncut (`r_k=1`), its lone
   sub-piece of value `2^k` is matched by `Π` to a sub-piece of value `2^k` inside a strictly larger
   piece `2^m`, `m>k` (no other whole piece equals `2^k`).
3. **Receiver residual bound.** For a piece `2^m`, let `d_m` = # uncut pieces whose `Π`-partner lies
   in `2^m`. If `d_m≥1` (`2^m` is a *receiver*), then `r_m≥d_m+1`.
4. **Partial budget bound.** With `U`=#uncut pieces, `R`=#receivers: `T≥2(n+1)−R`, i.e.
   `N≥(n+1)−R`.

## Proof
(1) Immediate from `T=(n+1)+N` and `T` even.

(3) The `d_m` partner sub-pieces inside `2^m` have values `2^{k_1}<…<2^{k_{d_m}}<2^m` (distinct
powers, each `<m` by (2)). Their total is `Σ_i 2^{k_i}≤2^0+…+2^{m-1}=2^m−1<2^m`, so the residual mass
`ρ_m=2^m−Σ_i 2^{k_i}≥1>0` is carried by `≥1` further sub-piece; hence `r_m≥d_m+1`.

(4) Every uncut piece matches into some receiver (by (2)), so `Σ_{receivers} d_m=U`. Then
```
  Σ_k(r_k−2) = Σ_{uncut}(1−2) + Σ_{cut}(r_k−2)
             = −U + Σ_{cut}(r_k−2)
             ≥ −U + Σ_{receivers}(d_m−1)    (fact 3; non-receiver cut pieces have r_k−2≥0)
             = −U + (U−R) = −R.
```
So `T−2(n+1)≥−R`, giving `T≥2(n+1)−R` and `N≥(n+1)−R`. ∎

## Scope
The deficit `−R` is exactly "one lost cut per receiver": a receiver's residual mass `ρ_m` may sit in
a single extra sub-piece whose own matched partner sits in yet another piece — the residual-mass
recursion. Recovering the missing `R` is precisely the OPEN Budget-Lemma case (b) ≅ Gap A′. NOT a
full proof of `Budget(n)`.

## Verification
On the `n=2` example (`piece1={1}, piece2={½,½,1}, piece4={2,2}`): `Σ(r_k−2)=0` (`T=6=2(n+1)`,
tight); uncut `={2^0}` (`U=1`), receiver `={2^1}` (`R=1`), `d_1=1`, `r_1=3≥d_1+1=2` ✓; partial bound
`T≥6−1=5`, actual `6`. Distinct-power residual bound `Σ_i 2^{k_i}≤2^m−1` is exact.
