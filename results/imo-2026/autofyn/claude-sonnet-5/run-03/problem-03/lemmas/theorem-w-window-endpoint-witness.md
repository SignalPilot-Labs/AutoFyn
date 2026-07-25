# Theorem W (Branch-I.A window-endpoint exact witness)

Certified round 9. Proved in `approaches/self-similar-induction-on-n.md`
(round 9, "Theorem W" section). Corrects a computational slip in the
round-9 dispatched conjecture.

**Statement.** Fix $\ell\ge2$, $\varepsilon\in(0,1)$. Let
$$C:=\{2^{\ell-1}\}\ \cup\ \bigl(\Gamma_{\ell-2}\setminus\{1\}\bigr)\ \cup\
\{r,r\},\qquad r:=1+\varepsilon/2$$
(for $\ell=2$, $\Gamma_{\ell-2}\setminus\{1\}=\varnothing$, $C=\{2,r,r\}$).
Then $C$ is admissible for the Branch-I.A-restricted window at its left
endpoint $c_1=2^{\ell-1}$ (i.e. $\mathrm{sum}(C)=2^\ell+\varepsilon$,
$\max(C)=2^{\ell-1}$, $\max(C\setminus\{2^{\ell-1}\})<2^{\ell-1}$, and $C$
has exactly $\ell+1$ parts, matching the piece cap), and
$$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ =\ 2^\ell+\varepsilon/2$$
**exactly**. In particular the target margin
$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})-2^\ell=\varepsilon/2>0$.

**Proof.** Write $M:=C\cup\Gamma_{\ell-1}$. Since $\Gamma_{\ell-1}=
\{2^{\ell-1}\}\cup\Gamma_{\ell-2}=\{2^{\ell-1}\}\cup(\Gamma_{\ell-2}
\setminus\{1\})\cup\{1\}$, as multisets
$$M=\{2^{\ell-1},2^{\ell-1}\}\cup(\Gamma_{\ell-2}\setminus\{1\})\cup
(\Gamma_{\ell-2}\setminus\{1\})\cup\{r,r\}\cup\{1\}.$$
Set $R:=\{2^{\ell-1}\}\cup(\Gamma_{\ell-2}\setminus\{1\})\cup\{r\}$; then
term-by-term $M=R\cup R\cup\{1\}$ exactly. By the certified **General
Insertion Lemma** (Theorem 4,
`lemmas/perfect-pairing-subadditivity-and-general-insertion.md`): for any
finite multiset $R$ of positive reals with $\mathrm{sum}(R)=S$ and any
$\ell_0>0$, $\mathrm{OddSum}(R\cup R\cup\{\ell_0\})=S+\ell_0$ (no ordering
hypothesis needed). With $\ell_0=1$ and
$\mathrm{sum}(R)=2^{\ell-1}+(2^{\ell-1}-2)+r=2^\ell-2+r$:
$$\mathrm{OddSum}(M)=(2^\ell-2+r)+1=2^\ell-1+r=2^\ell-1+1+\varepsilon/2
=2^\ell+\varepsilon/2.\qquad\blacksquare$$

**Correction of the dispatched conjecture.** The round-9 dispatch's
proposed witness used $r=(1+\varepsilon)/2$; checking sums shows this
value is inadmissible ($\mathrm{sum}(D_0)$ falls short of the required
$2^{\ell-1}+\varepsilon$ by exactly $1$). The corrected value is
$r=1+\varepsilon/2$, verified above.

**Reviewer verification.** Independently re-derived $M=R\cup R\cup\{1\}$
by direct exact-`Fraction` construction of $C$, $\Gamma_{\ell-1}$, and
their union, sorted-and-summed by hand (not via the Theorem-4 shortcut),
for $\ell=2,\dots,8$ and $\varepsilon\in\{1/10,3/10,1/2,7/10,9/10\}$ (40
instances): exact agreement with $2^\ell+\varepsilon/2$ in every case,
zero deviation. Also independently re-verified the cited General Insertion
Lemma itself by direct random exact-`Fraction` testing (2000 trials,
$\mathrm{OddSum}(R\cup R\cup\{\ell_0\})=\mathrm{sum}(R)+\ell_0$, zero
violations).

**What this does and does not resolve.** Theorem W proves the
Branch-I.A-restricted window's target *exactly at one point* — the left
endpoint $c_1=2^{\ell-1}$, via one specific witness $C$. It does **not**
establish that this $C$ is the true maximizer of $\mathrm{OddSum}(D\cup T)$
over all admissible $D$ at that budget (only exhibits one qualifying $D$,
with strict margin $\varepsilon/2$ to spare), and it does **not** address
any other $c_1$ in the window's interior. The window as a whole (all
$c_1\in[2^{\ell-1},2^{\ell-1}+1-\varepsilon)$) remains open; see
`approaches/self-similar-induction-on-n.md` round 9 for the precise
remaining gap (single-endpoint optimality and cross-$W$ monotonicity, both
unproved).
