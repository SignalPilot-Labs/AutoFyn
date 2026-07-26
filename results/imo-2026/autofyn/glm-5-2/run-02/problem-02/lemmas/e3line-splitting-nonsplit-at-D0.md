# Lemma: e3line-splitting-nonsplit-at-D0

**Statement.** Let `Δ = et1²−4·et2·et0` be the discriminant of `e3_line` (as a quadratic in `t`), and `Δ_red` its reduction modulo `D₀` (an element of `κ=Q(b,u,v,lx,ly)/(D₀)`). Then:
(a) `D₀ ∤ Δ` (`Δ_red≢0`): `e3_line` has distinct roots at the generic point of `D₀=0`.
(b) `Δ_red` is **not a square** in `κ`.
Consequently the prime `(D₀)` is **inert** (unramified, residue degree 2, single prime above) in the splitting field `L=F(√Δ)` of `e3_line` over `F=Q(b,u,v,lx,ly)`.

**Proof.** (a) Field-reduce `Δ` mod `D₀` (over `Q(b,u,v,lx,t)[ly]`): the remainder `Δ_red` is nonzero (a polynomial of positive degree), so `D₀∤Δ`.

(b) By specialization. Specialize `b=1,u=0,v=2` (then `D₀_s = 2(ly³−3ly²+6ly−6)` is nonzero). If `Δ_red=f²` in `κ`, specializing gives `Δ_red|_s=(f|_s)²` in `κ_s=Q(lx,ly)/(D₀_s)`. Specialize further `lx=−2`: `D₀_s` becomes `2(ly³−3ly²+6ly−6)`, which takes value `−4` at `ly=1` and `+4` at `ly=2`, so by IVT it has a real root `ly₀∈(1,2)`. At this specialization,
```
Δ_red|_{b=1,u=0,v=2,lx=−2} (reduced mod D₀_s) = −(101/4)·ly² + 89·ly − 175/2,
```
a quadratic with discriminant `89²−4·(−101/4)·(−175/2) = −1833/2 < 0` and leading coefficient `−101/4<0`, hence **strictly negative for every real `ly`**; in particular `Δ_red(lx=−2,ly₀)<0`. A square of a real-valued rational function is `≥0` wherever defined; since `Δ_red(lx=−2,ly₀)` is finite nonzero, `f|_s` is finite there, so `(f|_s)²≥0`, contradicting `<0`. Hence `Δ_red` is not a square in `κ`.

(c) `Δ` is not a square in `F` either (else its reduction `Δ_red` would be a square). Hence `L=F(√Δ)` is a genuine quadratic Galois extension. The prime `(D₀)` (height-one, since `D₀` irreducible — lemma `D0-irreducible`) is unramified (`v_{D₀}(Δ)=0`) and inert (residue field extension degree 2, since `Δ_red` not a square). ∎

**Reviewer note (round 2).** Independently re-verified: `Δ_red mod D₀` is nonzero; at `b=1,u=0,v=2,lx=−2`, `D₀_s=2(ly³−3ly²+6ly−6)` (real root in (1,2) by IVT), `Δ_red` reduced mod `D₀_s` equals `−101/4·ly²+89·ly−175/2` (discriminant `−1833/2<0`, leading coeff `<0`, value at `ly=1.5` is `−10.8125<0`). The specialization-then-real-point argument is sound (a square rational function is ≥0 at real points where finite).

**Source.** `analytic-resultant-cert` Section 8 (Lemma 9). Reviewer-certified round 2.
