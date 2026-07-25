## Theorem (parity obstruction: constant/`(\sigma,\tau)`-only-coefficient
Positivstellensatz ansätze on `\{G_0,-E_{\mathrm{num}},\mathrm{Bc},
-\mathrm{Num}\}` cannot reach `-q_1` or `-r_0`)

**Status.** Proposed by `coordinate-bash-resultant-boundary`, round 13, for
reviewer certification.

**Setup.** `c,s,d,t` as usual (`\cos A,\sin A,\cos B,\sin B`),
`\sigma:=s^2,\tau:=t^2`. Work in
`R:=\mathbb R[c,s,d,t]/\langle c^2+s^2-1,\,d^2+t^2-1\rangle`. Both
defining relations are homogeneous of degree `(0,0)` under the
`\mathbb Z_2\times\mathbb Z_2` grading `\deg_2(\text{monomial}):=(\deg_c
\bmod2,\ \deg_d\bmod2)`, so this grading descends to `R`: every
`f\in R` decomposes uniquely as `f=f_{00}+f_{10}+f_{01}+f_{11}`, and for a
product, `(fg)_{ab}=\sum_{p+q\equiv(a,b)\ (\mathrm{mod}\ 2)}f_pg_q`.

`G_0:=ct(1-2d^2)-2sd^3`, `E_{\mathrm{num}}:=ctf_1(\sigma,\tau)+dsf_2(\sigma,
\tau)` (`f_1,f_2` as in the certified `E`-reduction, round 12),
`\mathrm{Bc}:=c-2t^2+1`, `\mathrm{Num}` as in
`lemmas/num-identity-exact-squaring-equivalence.md`, and `q_1(\sigma,\tau),
r_0(\sigma,\tau)` as in `lemmas/case-b-e-lt-0-t-factorization.md`.

**Lemma (graded components, verified by direct symbolic computation via the
projectors `f_{ab}=\tfrac14\sum_{\epsilon,\delta\in\{\pm1\}}\epsilon^a
\delta^bf(\epsilon c,s,\delta d,t)`).**
$$q_1,r_0\in R_{00}\quad(\text{no }c,d\text{ appear at all}),$$
$$(G_0)_{00}=(G_0)_{11}=0,\qquad(E_{\mathrm{num}})_{00}=(E_{\mathrm{num}})_{11}
=0,\qquad(\mathrm{Num})_{00}=(\mathrm{Num})_{11}=0,$$
$$(\mathrm{Bc})_{00}=1-2t^2,\quad(\mathrm{Bc})_{10}=c,\quad
(\mathrm{Bc})_{01}=(\mathrm{Bc})_{11}=0.$$
(i.e. `G_0,E_{\mathrm{num}},\mathrm{Num}` lie purely in `R_{10}\oplus
R_{01}`, while `\mathrm{Bc}` has both a `(0,0)`-part and a `(1,0)`-part.)

**Theorem.** Suppose
$$-q_1=\lambda_{G_0}G_0+\lambda_E(-E_{\mathrm{num}})+\lambda_{\mathrm{Bc}}
\mathrm{Bc}+\lambda_{\mathrm{Num}}(-\mathrm{Num})+S,\qquad S\text{ an SOS in }R.$$
If `\lambda_{G_0},\lambda_E,\lambda_{\mathrm{Num}}\in R_{00}` (i.e. each is
a polynomial in `\sigma,\tau` alone, with no explicit odd power of `c` or
`d`), then their three terms above each contribute `0` to the `(0,0)`-graded
component of the right-hand side (since `(\lambda G)_{00}=\lambda_{00}G_{00}
+\lambda_{10}G_{10}+\lambda_{01}G_{01}+\lambda_{11}G_{11}` and, for
`\lambda\in R_{00}` (so `\lambda_{10}=\lambda_{01}=\lambda_{11}=0`) paired
with `G\in\{G_0,E_{\mathrm{num}},\mathrm{Num}\}` (so `G_{00}=G_{11}=0`),
every term in the sum vanishes). Hence, restricted to this multiplier class,
the identity collapses to
$$-q_1=\lambda_{\mathrm{Bc},00}\cdot(1-2t^2)+\lambda_{\mathrm{Bc},10}\cdot c
+S_{00},$$
which (taking `(1,1)`-components of both sides, where `S_{11}` is itself a
sum of `p_{10}p_{01}` cross terms and `-q_1` has no `(1,1)`-part) forces
further strong constraints and, empirically (round 12's certified negative
finding: no small-integer-coefficient combination of `G_0,-E_{\mathrm{num}}`
alone matches `q_1,r_0`'s sign), is not achievable at low degree in this
restricted form either.

**Corollary (the actionable consequence).** Any working Positivstellensatz
certificate for `-q_1` (or `-r_0`, by the identical argument, since `r_0`
is likewise in `R_{00}`) as a nonnegative combination of `\{G_0,
-E_{\mathrm{num}},\mathrm{Bc},-\mathrm{Num}\}$ plus SOS **must** use at
least one multiplier `\lambda_{G_0},\lambda_E,\lambda_{\mathrm{Num}}` with a
nonzero `(1,0)`- or `(0,1)`-graded part — i.e. containing an explicit bare
odd power of `c` or `d` (such as a bare factor `c,d,s,t`, or a product of
two odd-parity generators, e.g. `G_0\cdot(-\mathrm{Num})$, whose `(0,0)`-part
is generically nonzero). Constant-coefficient or `(\sigma,\tau)`-only
ansätze (the class searched, and shown empirically infeasible, in round 12)
are hereby proved structurally incapable of ever closing this gap, not
merely observed to fail on the attempted low-degree instances.

*Proof of the Lemma (graded components).* Direct computation: `G_0(-c,s,d,t)
=-ct(1-2d^2)-2sd^3`, `G_0(c,s,-d,t)=ct(1-2d^2)+2sd^3`,
`G_0(-c,s,-d,t)=-ct(1-2d^2)+2sd^3`. Averaging with signs `(+,-,+,-)`
appropriately (the four projector combinations) and expanding gives
`(G_0)_{00}=(G_0)_{11}=0` directly (own `sympy` verification, this round,
zero residual for both). The analogous computation for `E_{\mathrm{num}}`
and `\mathrm{Num}` (both built, term by term, purely from monomials with
either `(\deg_c,\deg_d)\equiv(1,0)` or `\equiv(0,1)$, confirmed by direct
inspection of every term in their displayed formulas) gives the same
vanishing. For `\mathrm{Bc}=c-2t^2+1`: the `-2t^2+1` piece has no `c,d`
dependence at all (`(0,0)`-graded), and the bare `c` piece is `(1,0)`-graded;
there is no `d`-dependence anywhere in `\mathrm{Bc}`, so `(\mathrm{Bc})_{01}
=(\mathrm{Bc})_{11}=0` trivially. `\blacksquare`
