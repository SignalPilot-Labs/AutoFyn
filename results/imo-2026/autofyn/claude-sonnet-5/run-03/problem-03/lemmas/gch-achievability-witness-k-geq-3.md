## Source
`approaches/self-similar-induction-on-n.md`, round 19, "Exact
achievability" theorem. Certified **in corrected form** by the round-19
proof-reviewer — the round's own statement, "for every $k\ge2$," is
**false at $k=2$** (found by independent verification); the theorem is
genuinely true and fully proved, exactly as the round's argument shows,
for $k\ge3$.

## Corrected statement (Chain+Pair Achievability, $k\ge3$)

Fix $k\ge3$ and $S\in[2^k,2^k+1)$. Define
$$R^*:=\{2^{k-1},2^{k-2},\dots,4\}\ \cup\ \{r,r\},\qquad r:=\frac{S-2^k}2+2,$$
where the chain has $k-2\ge1$ elements. Then $R^*$ is feasible for
GCH($k$) ($|R^*|=k\le k+1$, every entry $\le\mathrm{cap}=2^{k-1}$ since
$r<2.5\le2^{k-1}$ for $k\ge3$, $\mathrm{sum}(R^*)=S$ exactly), and
$$\mathrm{AltSum}(R^*\cup\Gamma_{k-1})=1\quad\text{exactly, for every
}k\ge3,\ S\in[2^k,2^k+1).$$

*Proof.* Exactly as in the source file: the chain part of $R^*$ matches
$\Gamma_{k-1}$'s own values at levels $4,\dots,2^{k-1}$ ($k-2$ shared
levels), each now with even multiplicity $2$, hence contributing $0$ by
the certified Corollary of Lemma BCF (see
`lemmas/tied-pair-cancellation-and-block-contribution-formula.md`),
regardless of position. What remains is $\{r,r,2,1\}$ (the pair plus
$\Gamma_{k-1}$'s own bottom two elements), and since $r\in[2,2.5)$ this
sorts as $r,r,2,1$, giving $\mathrm{AltSum}=r-r+2-1=1$. $\blacksquare$

*Independent verification.* Own exact-`Fraction` script: for every
$k=3,\dots,8$ and $S=2^k+\{0,0.01,0.5,0.9,0.99\}$, confirmed $R^*$ is
feasible ($r\le\mathrm{cap}$ in every case) and
$\mathrm{AltSum}(R^*\cup\Gamma_{k-1})=1$ exactly, matching also the true
numeric minimizer found by an independent multi-restart `scipy.optimize`
constrained search at $k=3$ (the minimizer's shape and value match $R^*$
digit-for-digit at every tested $S$).

## Genuine gap found and NOT covered by this certification: $k=2$

**The source file's claim that this formula extends to $k=2$ is false.**
At $k=2$ the chain is empty (by the file's own definition, "$k-2=0$
elements"), so the formula collapses to $R^*=\{r,r\}$ with
$r=(S-4)/2+2\in[2,2.5)$ — but $\mathrm{cap}=2^{k-1}=2$ at $k=2$, so
$r>\mathrm{cap}$ for every $S>4$ (only $S=4$, giving $r=2$, is feasible).
**Confirmed by direct exact-`Fraction` computation**: e.g. $S=4.5$ gives
$r=2.25>2=\mathrm{cap}$ — $R^*=\{2.25,2.25\}$ is **infeasible** for
GCH($2$) (violates $\max(R)\le\mathrm{cap}$). The source file's own
closing cross-check, "there, $R^*=\{2,r,r\}$ exactly matches this
formula's $k=2$ specialization, chain empty," is **internally
inconsistent**: a chain-empty specialization of $\{2^{k-1},\dots,4\}\cup
\{r,r\}$ is $\{r,r\}$ (two elements), not $\{2,r,r\}$ (three elements) —
these do not match, and the claimed cross-check does not actually verify
anything.

**However, the underlying mathematical fact (achievability at $k=2$
too) remains true**, via the already-certified, structurally *different*
construction in `lemmas/sharper-odd-residual-and-k2-cardinality-half-sum.md`
(Lemma 2): independently re-verified this round (own multi-restart
`scipy` search, exact-`Fraction` spot-check) that the true $k=2$ equality
locus is $R=\{2,b,b\}$ with $b=(S-2)/2\in[1,1.5)$ for $S\in[4,5)$ — note
this construction *retains* the cap element $2=2^{k-1}$ in addition to
the tied pair, unlike the round-19 general-$k$ formula's chain (which,
for $k=2$, has no room to include the cap element since the chain's
stated range stops at value $4>2^{k-1}$). This also identifies a small,
non-load-bearing labeling slip in the already-certified Lemma 2's own
worked example, which reads "$R=\{b,b,1\}$" — this should read
"$R=\{2,b,b\}$" (confirmed by independent `scipy` search to be the actual
equality-attaining configuration; $\{b,b,1\}$ does not even satisfy
$\mathrm{sum}(R)=S$ for the stated $b=(S-2)/2$). This does not affect
Lemma 2's proof or certified inequality, only this one parenthetical
example.

## Net effect

Achievability of $\mathrm{AltSum}(R\cup\Gamma_{k-1})=1$ (tightness of
GCH($k$)) is now established for **every** $k\ge2$: $k=2$ via the
already-certified Lemma 2 (corrected witness $\{2,b,b\}$), $k\ge3$ via
this round's chain+pair family $R^*$ (as corrected above). The round-19
source file's single-formula, single-proof claim of covering "every
$k\ge2$" is **not** certified as literally stated; this corrected,
split-by-case version is.
