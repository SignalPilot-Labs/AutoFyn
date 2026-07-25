## Excess Growth Rate Lemma (negative result for affine-majorization mechanisms)

**Statement.** Let $(a_n)$ be any sequence with $a_{n+T}=a_n+L$ for all
$n\ge n_0$ (fixed $T,L,n_0$), and let $\hat a_n:=a_1+(n-1)c$ for any fixed
constant $c$. Define $e_n:=a_n-\hat a_n$. Then for every $n\ge n_0$,
$$e_{n+T}-e_n = L-Tc.$$

*Proof.* $\hat a_{n+T}-\hat a_n=Tc$ by definition of the affine candidate;
$a_{n+T}-a_n=L$ by the periodicity hypothesis. Subtracting gives the
claim. $\blacksquare$

**Corollary (unboundedness whenever rates mismatch).** If $L\ne Tc$, then
along any fixed residue class $n^\ast\pmod T$ with $n^\ast\ge n_0$, the
subsequence $e_{n^\ast},e_{n^\ast+T},e_{n^\ast+2T},\dots$ is an arithmetic
progression with common difference $L-Tc\ne0$, hence unbounded.

### Consequence for this problem
Any attempted proof strategy that majorizes/compares the true sequence
$(a_n)$ against a single fixed-rate affine candidate $\hat a_n=a_1+(n-1)c$
(for any constant $c$ chosen in advance of knowing the true eventual rate
$L/T$) produces an unbounded excess unless $c$ exactly equals the
(unknown, to-be-proven) true rate $L/T$ — and no route to determine $c=
L/T$ without already knowing $(T,L)$ (the theorem's own output) is
available from the currently certified lemma set (Positive-Density
Upgrade, Sharpened Bounded-Gap Lemma, Minimum Gap Lemma, Multiple-of-$R$
Realization): these bound gaps or witness recurring values with positive
density but do not establish that $a_n/n$ converges prior to periodicity
being known. Verified concretely for $a_1=35$: true $(T,L)=(34,210)$ (this
periodicity checked directly, holding exactly for $n=1,\dots,2966$ with
zero exceptions in the tested range), naive rate $c=p=5$ gives
$L-Tc=210-170=40\ne0$, so $e_n$ grows by exactly $40$ every $34$ steps
($e_6=0,e_{40}=40,e_{74}=80,\dots$), matching the Lemma's prediction
exactly.

### Caveat
This is a clean, general, unconditional algebraic fact (not specific to
this problem's gcd structure) — reusable by any future scalar-rate-
matching argument for this or other problems — but it is a **negative**
result here: it kills the single-affine-candidate majorization mechanism
for `imo-2026-06` (both the naive rate $c=\min R(a_1)$ and any "best
empirical rate" extracted from the Positive-Density Upgrade), not a
positive step toward the central gap.

### Provenance
Proved in `approaches/scalar-difference-majorization.md`, §2, round 6.
Independently re-derived by the proof-reviewer (three-line algebraic
identity, no gap) and the $a_1=35$ application independently re-simulated
exactly: $(T,L)=(34,210)$ holds with zero exceptions up to $n=200$ tested
directly, and $e_6=0,e_{40}=40,e_{74}=80$ confirmed by direct computation.
