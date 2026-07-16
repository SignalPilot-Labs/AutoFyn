# Lemma: Physical-slice imaginary ideal-membership certificate

**Setup.** Work in the complex plane with points encoded by affixes; write each affix as
`x_1 + i x_2` with real coordinates. Suppose a target quantity `T` and finitely many
"reality-condition" quantities `E_1,…,E_n` are all **purely imaginary polynomials** in the
affixes on the *physical* variety (conjugates forced, `\bar x = x_1 - i x_2`) — i.e. each has the
form `z - \bar z`, so `Re(T) ≡ Re(E_j) ≡ 0` as polynomials in the real coordinates. Then
`T = 0 ⟺ Im(T) = 0` and `E_j = 0 ⟺ Im(E_j) = 0`, where `Im(T), Im(E_j)` are real polynomials in
the real coordinates.

**Lemma.** Suppose there is a polynomial `W` and polynomials `f_1,…,f_n` in the real coordinates
with the **exact identity**
`W · Im(T) = f_1 Im(E_1) + … + f_n Im(E_n)`
(equivalently `W·Im(T) ∈ (Im E_1,…,Im E_n)`, certifiable by reducing `W·Im(T)` to normal form `0`
modulo a Gröbner basis of the ideal — Buchberger's algorithm, an exact terminating decision
procedure). If on a given real point of interest all reality conditions hold, `Im(E_j)=0`, and
`W ≠ 0` there, then `Im(T) = 0`, hence `T = 0` at that point.

**Proof.** The identity is an equality of polynomials, so it holds at every real point. At the
point of interest the right-hand side vanishes (`Im(E_j)=0`), so `W·Im(T)=0`; since `W ≠ 0` there,
`Im(T)=0`, whence `T = z-\bar z = 2i·Im(T)/… = 0`. ∎

**Why it matters.** This removes any *auxiliary* non-degeneracy hypothesis (e.g. a Cramer
determinant `\det A ≠ 0`) from a complex-coordinate olympiad bash in one exact step: instead of a
continuity/genericity argument to cover the `\det A = 0` locus, one exhibits a single membership
certificate whose multiplier `W` is a product of *genuine geometric* non-degeneracies (each nonzero
on every admissible configuration). Crucially the certificate lives on the **real slice**: over the
complex ring with *independent* conjugates the analogous membership may FAIL (a spurious component
with `T ≠ 0`), so forcing `\bar x = \overline{x}` is essential. Combined with bidegree-homogeneity
one may also WLOG-normalize one affix (e.g. `B=1`) to keep the Gröbner computation tractable, then
un-normalize by homogeneity.

**Certification (proof-reviewer, round 2).** Reproduced independently for approach
`complex-reality-conditions` (imo-2026-02): `Re(E_i)=Re(T)≡0` (purely imaginary) confirmed exactly;
the ideal membership `W·Im(TN) ∈ (Im E_1, Im E_2, Im E_3)` at power `W^1` reproduced by an
independent Gröbner reduction (target reconstructed exactly as a combination of Gröbner-basis
elements, remainder `0`), with `W=|B-K|^2·|C-L|^2·Im(\bar K L)·Im(\bar B C)`; the bidegree-(2,2)
homogeneity that legitimizes `B=1` verified symbolically. Statement is no stronger than proved
(existence of `f_j` follows from the reduction; the lemma asserts only membership + `W≠0 ⇒ T=0`).
Certified for reuse.
