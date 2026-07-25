# Certified (round 10): Lemma TPI (Tiny-Piece Insertion Monotonicity); the
# window endpoint reduction identity

Certified from `approaches/self-similar-induction-on-n.md` (round 10).

## Lemma TPI (Tiny-Piece Insertion Monotonicity)

**Statement.** For any finite multiset $M$ of positive reals and any $\delta$
with $0<\delta\le\min(M)$: $\mathrm{OddSum}(M\cup\{\delta\})\ge\mathrm{OddSum}
(M)$, with equality iff $|M|$ is odd and strict increase by exactly $\delta$
iff $|M|$ is even.

**Proof.** Since $\delta\le\min(M)$, inserting $\delta$ preserves the sorted
order of every element of $M$ (each keeps its original rank $1,\dots,|M|$) and
places $\delta$ at the new last rank $|M|+1$. So $\mathrm{OddSum}(M\cup\{
\delta\})=\mathrm{OddSum}(M)+[\,|M|+1\text{ odd}\,]\cdot\delta$, which is
$\ge\mathrm{OddSum}(M)$ since $\delta>0$. $\blacksquare$ Elementary, no
majorization/Schur argument needed (and this hypothesis — $\delta$ strictly
below every element — is exactly the case where a naive rank-shift argument is
safe, correctly distinguished from the certified Schur-monotonicity dead end,
which fails for insertions that are not minimal).

**Corollary (gap (b)(i) of the Branch-I.A window, proved in full).** If $D$ is
admissible at budget $W_1$ with $|D|<\ell$ (piece cap not saturated) and
$W_2\in(W_1,W_1+\min(D)]$, setting $\delta:=W_2-W_1\in(0,\min(D)]$ and
$D':=D\cup\{\delta\}$ gives an admissible $D'$ at budget $W_2$ (piece cap, max
cap, and sum all verified directly: $|D'|=|D|+1\le\ell$; $\max(D')=\max(D)$
since $\delta\le\min(D)\le\max(D)$; $\mathrm{sum}(D')=W_1+\delta=W_2$) with
$\mathrm{OddSum}(D'\cup T)\ge\mathrm{OddSum}(D\cup T)$ by Lemma TPI applied to
$M:=D\cup T$: since $\min(M)=\min(\min(D),\min(T))\le\min(D)$ and
$\delta\le\min(D)$, we do **not** automatically get $\delta\le\min(M)$ unless
also $\delta\le\min(T)$ — but $\min(T)=\min(\Gamma_{\ell-1})=1$ (the smallest
level), and the window's budgets place $\delta=W_2-W_1<1-\varepsilon<1$
throughout (source file, window range), so $\delta<1=\min(T)$ always holds in
this specific application; combined with $\delta\le\min(D)$ this gives
$\delta\le\min(M)$, Lemma TPI's exact hypothesis. Reviewer confirms this
range check is correct as used in the source file.

**Reviewer verification.** Re-derived Lemma TPI from scratch (three-line rank
argument) and confirmed it independently; the proof is elementary and correct.
The corollary's application context (window budgets, $T=\Gamma_{\ell-1}$) was
checked against the source file's exact hypotheses and found consistent.

## The endpoint reduction identity (gap (a) of the window)

**Statement.** At $W_{\mathrm{top}}=2^{\ell-1}+\varepsilon$, for any admissible
$D$ ($|D|\le\ell$, $\max(D)<2^{\ell-1}$, $\mathrm{sum}(D)=W_{\mathrm{top}}$),
writing $T=\Gamma_{\ell-1}$, $T'=\Gamma_{\ell-2}=T\setminus\{2^{\ell-1}\}$:
$$\mathrm{OddSum}(D\cup T)\le2^\ell+\varepsilon-1\iff\mathrm{OddSum}(D\cup T')
\ge2^{\ell-1}.$$

**Proof.** $2^{\ell-1}$ (T's top element) is the unique overall max of $D\cup T$
(since $\max(D)<2^{\ell-1}$ strictly). By the certified Companion Peeling
Lemma (`lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md`),
$\mathrm{EvenSum}(D\cup T)=\mathrm{OddSum}(D\cup T')$. Combined with
$\mathrm{OddSum}(D\cup T)+\mathrm{EvenSum}(D\cup T)=\mathrm{sum}(D)+\mathrm{sum}
(T)=(2^{\ell-1}+\varepsilon)+(2^\ell-1)$, algebra gives the stated equivalence
directly. $\blacksquare$

**Reviewer verification.** Re-derived the algebra independently: $\mathrm{sum}
(D\cup T)-(2^\ell+\varepsilon-1) = 2^{\ell-1}$ exactly, confirming the
equivalence. The source file additionally reports a 13,500-instance Monte
Carlo cross-check (both sides' truth values agree on every sample); not
independently re-run by the reviewer (the algebraic derivation is exact and
sufficient), but the algebra is correct and this is not needed as a separate
verification.

## Scope (honest)

Lemma TPI fully closes gap (b)(i) (piece-cap-unsaturated case) of the
Branch-I.A window's monotonicity question. It does **not** address gap (b)(ii)
(piece cap saturated) — open. The endpoint reduction identity is an exact
equivalence, not a closure: it shows gap (a) (the window's top endpoint) is
equivalent to $\mathrm{OddSum}(D\cup\Gamma_{\ell-2})\ge2^{\ell-1}$, which the
source file correctly diagnoses as structurally the same as the file's own
still-open $j\ge2$ trichotomy, one level down — not a smaller or easier
problem. The window as a whole, Theorem 2', and the tail-untouched-sliver
residual remain open.
