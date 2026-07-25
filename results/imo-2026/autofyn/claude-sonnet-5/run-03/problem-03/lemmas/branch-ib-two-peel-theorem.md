## Branch I.B Two-Peel Theorem, and the base fact OddSum(Γ_n) ≥ 2^n

Certified round 7. Two related results, proved in
`approaches/self-similar-induction-on-n.md` ("Round 7: bug fix, Branch I.B
closed in full, Step 2 attempted"), reused by the `self-similar-induction-on-n`
approach to close Branch I.B of the residual sliver `L_0(ℓ,ε)` in full.

### Base fact: OddSum(Γ_n) ≥ 2^n for all n≥0, equality iff n∈{0,1}

**Statement.** For $\Gamma_n=(2^n,2^{n-1},\ldots,2,1)$,
$$\mathrm{OddSum}(\Gamma_n)=\begin{cases}(2^{n+2}-1)/3, & n\text{ even}\\
(2^{n+2}-2)/3, & n\text{ odd}\end{cases}\ \ge\ 2^n,$$
with equality exactly at $n\in\{0,1\}$.

**Proof.** From the certified $\mathrm{AltSum}(\Gamma_m)$ closed form
($(2^{m+1}+1)/3$ for $m$ even, $(2^{m+1}-1)/3$ for $m$ odd) and Lemma AS
($\mathrm{OddSum}=(\mathrm{sum}+\mathrm{AltSum})/2$, $\mathrm{sum}(\Gamma_n)
=2^{n+1}-1$), direct substitution for both parities gives the displayed
closed form. Comparing to $2^n$: for $n$ even,
$(2^{n+2}-1)/3\ge2^n\iff4\cdot2^n-1\ge3\cdot2^n\iff2^n\ge1$ (always true,
equality iff $n=0$); for $n$ odd, $(2^{n+2}-2)/3\ge2^n\iff2^n\ge2$ (true
for $n\ge1$, equality iff $n=1$). $\blacksquare$

**Independent verification (proof-reviewer, round 7).** Re-derived the
closed form symbolically and checked against direct computation of
$\mathrm{OddSum}(\Gamma_n)$ for $n=0,\ldots,10$: exact match in every case,
with the excess over $2^n$ strictly positive for $n\ge2$ and zero exactly
at $n=0,1$, matching the claimed equality case.

### Branch I.B Two-Peel Theorem

**Statement.** Let $\ell\ge1$, $\varepsilon\in(0,1)$, and let $C$ be any
finite multiset of positive reals with $\mathrm{sum}(C)=2^\ell+\varepsilon$.
Suppose $c_1:=\max(C)\ge2^{\ell-1}$ and $C$ has a second element
$c_1'\ge2^{\ell-1}$ (i.e. $\max(C\setminus\{c_1\})\ge2^{\ell-1}$). Then
$$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ \ge\ 2^\ell,$$
**unconditionally — no bound on the piece count of $C$ is needed.**

**Proof.** Write $T:=\Gamma_{\ell-1}$ ($\max(T)=2^{\ell-1}$,
$\mathrm{sum}(T)=2^\ell-1$), $R:=C\setminus\{c_1,c_1'\}$.

1. *Peel $c_1$* (valid: $c_1\ge2^{\ell-1}=\max(T)$ and $c_1\ge c_1'\ge$
   everything else in $C$, so $c_1=\max(C\cup T)$). By the certified
   Peeling Lemma: $\mathrm{OddSum}(C\cup T)=c_1+\mathrm{EvenSum}(C'\cup T)$,
   $C'=\{c_1'\}\cup R$.
2. *Peel $c_1'$* (valid: $c_1'\ge2^{\ell-1}=\max(T)$ and $c_1'\ge$
   everything in $R$). By the certified Companion Peeling Lemma,
   $\mathrm{EvenSum}(C'\cup T)=\mathrm{OddSum}(R\cup T)$.
3. *Bound $R$'s effect.* $c_1+c_1'\ge2^\ell$, so $\mathrm{sum}(R)=
   (2^\ell+\varepsilon)-c_1-c_1'\le\varepsilon<1=\min(T)$: every element of
   $R$ is positive and $<1$, hence sorts strictly below all of $T$ in
   $R\cup T$. So $T$'s elements keep ranks $1,\ldots,\ell$ unchanged, and
   $\mathrm{OddSum}(R\cup T)=\mathrm{OddSum}(T)+(\text{nonneg. contribution
   from }R)\ge\mathrm{OddSum}(T)$.
4. *Apply the base fact:* $\mathrm{OddSum}(T)=\mathrm{OddSum}(\Gamma_{\ell-1})
   \ge2^{\ell-1}$.

Combining: $\mathrm{OddSum}(C\cup T)=c_1+\mathrm{OddSum}(R\cup T)\ge
c_1+\mathrm{OddSum}(T)\ge2^{\ell-1}+2^{\ell-1}=2^\ell$. $\blacksquare$

**Independent verification (proof-reviewer, round 7).** Re-derived the
algebra step by step; no gap found. Independently stress-tested with exact
`Fraction` arithmetic: 2800 random trials, $\ell=1,\ldots,7$, random
$\varepsilon\in(0,1)$, random $c_1\ge c_1'\ge2^{\ell-1}$, random composition
of $R$ — zero violations. A finer 20,000-trial sweep at $\ell=2$ confirmed
the margin can be pushed arbitrarily close to $0$ as $\varepsilon\to0$,
$c_1,c_1'\to2^{\ell-1}$, consistent with the file's claimed exact equality
case $\ell\in\{1,2\}$, $c_1=c_1'=2^{\ell-1}$, $R=\emptyset$.

**Source.** Proved in `approaches/self-similar-induction-on-n.md` (round 7,
"Step 1: Branch I.B closed in full").

**Reuse.** Closes, unconditionally, the entire "$C$ has two elements
$\ge2^{\ell-1}$" sub-case of any Case-B-style lower bound against a
geometric tail $\Gamma_{\ell-1}$ — the mechanism (peel top two elements
consecutively, discard the small remainder's contribution as nonnegative,
then invoke the geometric tail's own OddSum floor) generalizes beyond this
specific application; the base fact $\mathrm{OddSum}(\Gamma_n)\ge2^n$ is
independently useful anywhere a lower bound on an untouched geometric
tail's own OddSum is needed.
