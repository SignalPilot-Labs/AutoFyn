# Theorem 2.2 (H-hitting characterization)

**Statement (reviewer-generalized; strictly stronger than, and proved by the
same argument as, the version in `approaches/intersecting-family-covering-
construction.md`).** Let `H` be **any** finite, nonempty set of primes such
that
$$\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap H\ne\varnothing\quad\text{for every }1\le i<j$$
(i.e. `H` need only be a *covering set* in the sense of `persistent-backbone-
monovariant`'s Finite Covering Backbone Conjecture — it need **not** contain
the specific minimal witness `w(i,j)` for every pair, only *some* common prime
of `\mathrm{rad}(a_i)` and `\mathrm{rad}(a_j)`). Write `\sigma(i):=
\mathrm{rad}(a_i)\cap H` and, for a finite family `\mathcal S` of nonempty
subsets of `H`, say `x` *hits* `\mathcal S` if `(\mathrm{rad}(x)\cap H)\cap
S\ne\varnothing` for every `S\in\mathcal S`. Let `\Sigma_n:=\{\sigma(1),
\dots,\sigma(n)\}`. Then for every `n\ge1`,
$$a_{n+1}=\min\{x>a_n : x\text{ hits }\Sigma_n\}.$$

(The special case `H=W:=\bigcup_{i<j}\{w(i,j)\}`, used in the source file,
satisfies this weaker hypothesis automatically, since `w(i,j)\in\mathrm{rad}
(a_i)\cap\mathrm{rad}(a_j)\cap W` for every pair.)

**Proof.** Fix `n\ge1`; write `x_H:=\min\{x>a_n:x\text{ hits }\Sigma_n\}`
(exists: the least multiple `x_0` of `L:=\mathrm{lcm}(H)` exceeding `a_n`
satisfies `a_n<x_0\le a_n+L` and `\mathrm{rad}(x_0)\supseteq H` since `L\mid
x_0`, so `\mathrm{rad}(x_0)\cap H=H` meets every nonempty subset of `H`, in
particular every member of `\Sigma_n`).

*(a) `x_H\le a_{n+1}`.* Fix `i\le n`. Since `i<n+1`, the covering hypothesis
gives some `h\in\mathrm{rad}(a_i)\cap\mathrm{rad}(a_{n+1})\cap H`. Then
`h\in H\cap\mathrm{rad}(a_{n+1})=\mathrm{rad}(a_{n+1})\cap H` and `h\in H\cap
\mathrm{rad}(a_i)=\sigma(i)`, so `h` is a common element of
`\mathrm{rad}(a_{n+1})\cap H` and `\sigma(i)`; hence
`(\mathrm{rad}(a_{n+1})\cap H)\cap\sigma(i)\ne\varnothing`. This holds for
every `i\le n`, so `a_{n+1}` hits `\Sigma_n`. Since also `a_{n+1}>a_n`,
`a_{n+1}` is a candidate for the minimum defining `x_H`, giving `x_H\le
a_{n+1}`.

*(b) `a_{n+1}\le x_H`.* Fix `i\le n`. Since `x_H` hits `\Sigma_n` and
`\sigma(i)\in\Sigma_n`, there is `h\in(\mathrm{rad}(x_H)\cap H)\cap\sigma(i)`.
Then `h\mid x_H` and `h\in\sigma(i)\subseteq\mathrm{rad}(a_i)`, so `h\mid a_i`,
giving `\gcd(x_H,a_i)\ge h>1`. This holds for every `i\le n`, so `x_H` is
admissible at step `n` in the problem's original sense; as `a_{n+1}` is by
definition the least admissible integer `>a_n`, `a_{n+1}\le x_H`.

Combining (a) and (b): `a_{n+1}=x_H`. `\blacksquare`

**Source.** Proved (for the special case `H=W`) in full in
`approaches/intersecting-family-covering-construction.md` (round 2), Part 2,
Step 2.2.

**Certification / reviewer note.** Independently re-derived from scratch. The
source file's proof, on inspection, never actually uses that `w(i,j)` is the
*minimum* of `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap H` — only that *some*
element of that intersection lies in `H` — so the statement above generalizes
the source's `H=W` version to any finite covering set `H` in the sense of
`persistent-backbone-monovariant`'s Finite Covering Backbone Conjecture, with
an identical proof (verified line by line: part (a) only needs a common
element `h\in\mathrm{rad}(a_i)\cap\mathrm{rad}(a_{n+1})\cap H`, not the
specific minimal one; part (b) does not reference `w(i,j)` at all). No gaps
in either version. Certified `solved`-quality (sorry-free).

**Cross-approach synergy (reviewer finding, round 2).** This generalization
means that a proof of `persistent-backbone-monovariant`'s (formally weaker)
Finite Covering Backbone Conjecture is **already sufficient**, via this
theorem plus `theorem-2.4-conditional-eventual-periodicity.md`, to get
conditional eventual periodicity — the stronger hypothesis `W` finite
(`(\dagger)`) is not actually needed for this specific bridge. Any future
round proving the covering conjecture can invoke this generalized statement
directly, without needing to also prove `W` itself is finite.
