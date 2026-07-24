# Theorem 2.4 (conditional eventual periodicity)

**Statement (reviewer-generalized, same weakened hypothesis as `theorem-2.2-
H-hitting-characterization.md`).** Suppose there exists a finite, nonempty set
`H` of primes with `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap H\ne\varnothing`
for every `1\le i<j` (in particular this holds if `W:=\bigcup_{i<j}\{w(i,j)\}`
is finite, taking `H=W`, but is a formally weaker hypothesis — see
`theorem-2.2`'s cross-approach note). Let `L:=\mathrm{lcm}(H)`. Then there
exist positive integers `T\le L`, `N_2\ge1`, and an integer `L_{\mathrm{per}}`
such that
$$a_{n+T}=a_n+L_{\mathrm{per}}\qquad\text{for every }n\ge N_2.$$

**Proof.** By Theorem 2.2 (applied with this `H`) and Lemma 2.3, there is a
finite `N_1` with `\Sigma_n=\Sigma_\infty` for all `n\ge N_1`, and for
`n\ge N_1`, `a_{n+1}=\min\{x>a_n:x\text{ hits }\Sigma_\infty\}`. Whether an
integer `x` hits `\Sigma_\infty` depends only on `\mathrm{rad}(x)\cap H`,
which depends only on `x\bmod L` (every `h\in H` divides `L`, so divisibility
of `x` by `h` is determined by `x\bmod L`). Define
`g:\mathbb Z/L\mathbb Z\to\{1,\dots,L\}` by `g(r):=\min\{d\ge1:(r+d)\bmod L`
represents an integer hitting `\Sigma_\infty\}` (well-defined and `\le L`,
since the next multiple of `L` after any representative of `r` always hits
`\Sigma_\infty`, as in Theorem 2.2's existence argument). For `n\ge N_1`,
writing `r_k:=a_{N_1+k}\bmod L` (`k\ge0`),
$$a_{N_1+k+1}=a_{N_1+k}+g(r_k),\qquad r_{k+1}=(r_k+g(r_k))\bmod L=:G(r_k),$$
where `G:\mathbb Z/L\mathbb Z\to\mathbb Z/L\mathbb Z` does not depend on `k`.

Among the `L+1` values `r_0,\dots,r_L` (a set of size `L`), by pigeonhole two
coincide: `r_{k_1}=r_{k_2}` for some `0\le k_1<k_2\le L`. Since `r_{k+1}=
G(r_k)` depends only on `r_k`, induction on `j\ge0` gives `r_{k_1+j}=
r_{k_2+j}` for all `j\ge0`, so `(r_k)_{k\ge k_1}` is periodic with period
`T:=k_2-k_1\in\{1,\dots,L\}`.

Set `N_2:=N_1+k_1`. For `n\ge N_2`, write `k:=n-N_1\ge k_1`. Then
$$a_{n+T}-a_n=\sum_{j=0}^{T-1}\bigl(a_{N_1+k+j+1}-a_{N_1+k+j}\bigr)=\sum_{j=0}^{T-1}g(r_{k+j}).$$
Since `(r_k)_{k\ge k_1}` is exactly periodic with period `T`, `r_{k+j}=
r_{k_1+((k-k_1+j)\bmod T)}` for `k\ge k_1`, so `\sum_{j=0}^{T-1}g(r_{k+j})` is
a sum of the same `T` values `g(r_{k_1}),\dots,g(r_{k_1+T-1})`, each counted
exactly once, independent of the starting point `k` (a sum over one full
period is invariant under cyclic rotation of the starting index). Hence
`a_{n+T}-a_n=\sum_{j=0}^{T-1}g(r_{k_1+j})=:L_{\mathrm{per}}` is constant for
every `n\ge N_2`. `\blacksquare`

**Source.** Proved (for `H=W`) in full in `approaches/intersecting-family-
covering-construction.md` (round 2), Part 2, Step 2.4.

**Certification.** Independently re-derived from scratch: the well-
definedness of `g`, the pigeonhole argument producing a period `T\le L` in
the functional graph of `G`, and the "sum over one period is rotation-
invariant" step were each checked directly (the rotation-invariance is
elementary: a periodic sequence summed over any `T` consecutive terms
produces the same multiset of values, hence the same sum). No gaps. Depends
only on Theorem 2.2 and Lemma 2.3 (both certified above), and on the
existence of the covering set `H` (an open hypothesis — see `current.md` for
what remains to be proved). Certified `solved`-quality (sorry-free) as a
conditional theorem.

**What this closes and what it does not.** This is the first fully rigorous
bridge in the problem's whole approach population from "a finite covering set
of primes exists" to "the gap sequence is eventually periodic," with an
explicit period bound `T\le L=\mathrm{lcm}(H)`. It does **not** establish
existence of such an `H` (the shared open gap, `persistent-backbone-
monovariant`'s Finite Covering Backbone Conjecture or the stronger `W`-finite
statement `(\dagger)`), and it does **not** establish periodicity from `n=1`
exactly (only for `n\ge N_2`, which may exceed `1`) — both remain open, see
`current.md`.
