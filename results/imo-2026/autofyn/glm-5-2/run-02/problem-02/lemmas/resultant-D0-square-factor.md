# Lemma: resultant-D0-square-factor

**Statement.** Over the field `Q(b,u,v,lx,ly)`, the resultant-in-`t` of the field-reduced quadratics `e3_line, Q_line` (mod `D₀`) factors as
```
res_t(e3_line, Q_line) = (b⁸/16)·v²·(u²+v²)·(u²+v²−b²)·D₀(L)²·R(lx,ly,u,v,b),
```
where `D₀²` is **exact** (multiplicity exactly 2): `R mod D₀ ≠ 0`, and the prefactor is not divisible by `D₀`. Hence on `D₀=0` (over the algebraic closure), `e3_line` and `Q_line` share at least one common root in `t`.

The cofactor `R` is:
```
R = −b²(u²+v²) − 3b·lx²·u − 3b·lx·ly·v + 4b·lx·u² + b·lx·v² + 3b·ly·u·v − b·u³ − b·u·v²
   + 9·lx²·u² + 18·lx·ly·u·v − 12·lx·u³ − 12·lx·u·v² + 9·ly²·v² − 12·ly·u²·v − 12·ly·v³
   + 4·u⁴ + 8·u²·v² + 4·v⁴.
```

**Proof.** Computed via `sp.resultant` over `QQ.frac_field(b,u,v,lx,ly)`; `sp.factor(res)` gives the displayed factorisation. Exact multiplicity 2: field-division of `res` by `D₀²` (as `Poly(...,ly,domain=QQ.frac_field(b,u,v,lx))`) leaves remainder `0`, and field-division of `R` by `D₀` leaves a nonzero remainder. ∎

**Reviewer note (round 2).** Independently re-verified: `sp.factor(sp.resultant(...))` produces exactly the displayed form; `res mod D₀²` remainder is zero; `R mod D₀` remainder is nonzero (exact multiplicity 2 confirmed).

**Source.** `analytic-resultant-cert` Section 7 (Proposition 7). Reviewer-certified round 2.
