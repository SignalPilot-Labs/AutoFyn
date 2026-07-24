# Spare-Cut Bisection Corollary

**Source:** `results/imo-2026-03/approaches/lp-duality-certificate.md`, §R12.2 (round 12).

**Statement.** Fix $n\ge0$, $m=n+1$, and an arbitrary Liu Bang marking.
Suppose the certified Iterated Greedy-Peel Construction
(`iterated-greedy-peel-identity`), run to completion, uses $c<n$ cuts (a
"spare cut" remains in Xiang Yu's budget) and produces a nonzero leftover
value $v_{\mathrm{final}}>0$. Then Xiang Yu has a legal response using
$c+1\le n$ cuts achieving $\Phi=T/2<a_nT$ — strictly better than the
greedy-peel construction's own value whenever $v_{\mathrm{final}}>0$.

**Proof.** By `iterated-greedy-peel-identity`, the process's actual
physical final multiset $M$ (using $c\le n-1$ cuts) satisfies
$A(M)=v_{\mathrm{final}}$, where $v_{\mathrm{final}}$ is the single real
surviving fragment; every other value in $M$ occurs in an exact pair (this
is exactly what makes the identity's proof telescope to a single
leftover). Bisect $v_{\mathrm{final}}$ (one further legal cut, $c+1\le n$
total): the new multiset is
$M':=(M\setminus\{v_{\mathrm{final}}\})\cup\{v_{\mathrm{final}}/2,
v_{\mathrm{final}}/2\}$. By `pair-cancellation-identity` applied to this
new exact pair, $A(M')=A(M\setminus\{v_{\mathrm{final}}\})$, and since
$M\setminus\{v_{\mathrm{final}}\}$ consists entirely of already-paired
values, $A(M\setminus\{v_{\mathrm{final}}\})=0$. Hence $A(M')=0$,
$\Phi(M')=T/2$. Since $a_n>1/2$ for every $n\ge0$ (Telescoping Threshold
corollary, `lp-duality-certificate.md` §2), $\Phi_{\min}\le T/2<a_nT$.
$\blacksquare$

**Dependencies (all already certified, not re-derived):**
`iterated-greedy-peel-identity`, `pair-cancellation-identity`, the
Telescoping Threshold fact $a_n>1/2$.

**Verification.** Independently re-checked: a fresh 500-trial exact
`Fraction` search confirmed every trial where the greedy-peel process ends
with $c<n$ (spare budget) also has $v_{\mathrm{final}}\ge0$ consistent
with the construction, and $a_n>1/2$ verified directly for the range
tested. See round-12 proof-builder transcript.

**Combined dichotomy (not itself a separately certified lemma, but the
immediate joint corollary of this lemma and `equal-pieces-closure`):** for
every marking and every $n\ge0$, $\Phi_{\min}\le a_nT$ holds automatically
whenever the Iterated Greedy-Peel process either (i) encounters at least
one mid-process exact tie, or (ii) finishes using strictly fewer than $n$
cuts. The residual — case (ii) fails and (i) fails simultaneously, i.e.
the process uses all $n$ cuts and never ties — is, per round-12's
independent 4000-trial genericity check (`lp-duality-certificate.md`
§R12.3), the *generic* case for markings without exact symmetry, **not**
a small corner case; it remains open.

**Certified by:** proof-reviewer, round 12 — independently re-derived and
re-verified with a fresh script (`/tmp/round-12/verify_sparecut2.py`, not
the builder's own), physically simulating the Iterated Greedy-Peel
Construction's *actual* fragment-by-fragment cuts (not just the abstract
working-set bookkeeping) for $n=1,\dots,6$, 2400 random markings: the
underlying identity $A(M)=v_{\text{final}}$ held in every trial (zero
mismatches), and in every trial where $c<n$ and $v_{\text{final}}>0$,
bisecting the real physical fragment equal to $v_{\text{final}}$ gave
$A=0$ exactly and $\Phi=T/2<a_nT$ (zero violations). CERTIFIED.
