## Lemma: Unconditional $p_2$-Threshold Closure

**Statement.** Fix $n\ge1$, $m=n+1\ge2$, and any Liu Bang marking
$p_1\ge p_2\ge\cdots\ge p_m>0$ with total $T=\sum p_i$. Write
$D_n=2^{n+1}-1$ and $a_n=2^n/D_n$. If
$$p_2\ \le\ \frac{T}{D_n},$$
then Xiang Yu has a legal response using exactly $1$ cut (bisecting $p_1$,
leaving $p_2,\dots,p_m$ untouched) achieving $\Phi\le a_nT$. In particular
$\Phi_{\min}\le a_nT$ at this marking. **This holds with no induction
hypothesis of any kind** — it is a standalone, fully unconditional fact
true for every $n\ge1$ and every marking satisfying the threshold.

**Proof.** By the certified `bisect-top-identity` (Theorem C), bisecting
$p_1$ alone (1 cut, legal for every $m\ge2$) gives exactly
$$\Phi=\frac{p_1}{2}+\Phi_{\mathrm{tail}},\qquad
\Phi_{\mathrm{tail}}=\frac{(T-p_1)+A(\{p_2,\dots,p_m\})}{2},$$
where $A(\{p_2,\dots,p_m\})$ is the sorted alternating sum of the
untouched tail. By the certified `max-domination-lemma` applied to this
tail (whose own maximum is $p_2$, since the marking is sorted),
$A(\{p_2,\dots,p_m\})\le p_2$. Substituting,
$$\Phi\ \le\ \frac{p_1}{2}+\frac{(T-p_1)+p_2}{2}\ =\ \frac{T}{2}+\frac{p_2}{2}.$$
It remains to check $T/2+p_2/2\le a_nT$, i.e. $p_2\le(2a_n-1)T$. By the
certified Telescoping Threshold Lemma (`telescoping-threshold-identity`'s
companion fact, proved there for every $n\ge0$: $a_n-\tfrac12=
\tfrac1{2D_n}$), $2a_n-1=1/D_n$. Hence the required condition is exactly
$p_2\le T/D_n$, which is the hypothesis. $\blacksquare$

**Remarks.** This closes a sub-case of the general upper bound
$c(n)\le a_n$ that is disjoint from — and not implied by — every other
sufficient condition on file: it does not require $p_1\ge T/2$ (Theorem
A/C′'s regime), does not require $p_2\ge a_nT/2$ (Theorem B's regime,
itself only conditionally valid via an induction hypothesis one level
down), and is not restricted to symmetric/near-degenerate markings
(`equal-pieces-closure`) or markings where a greedy-peel construction has
spare cut budget (`spare-cut-bisection-corollary`). It is the first
sufficient condition in this project's toolkit for the general upper
bound that requires **zero** induction.

**Verification.** Independently re-checked with a fresh `Fraction` script:
$20{,}000$ random markings, $m=2,\dots,8$; $2917$ trials satisfied
$p_2\le T/D_n$, and in every one the bisect-$p_1$ construction achieved
$\Phi\le a_nT$ exactly as claimed — zero violations.

**Certified in:** round 13, `results/imo-2026-03/approaches/lp-duality-certificate.md`
§R13.2 (`imo-2026-03`). Depends on `max-domination-lemma` (this round,
same file) and the already-certified `bisect-top-identity`,
`telescoping-threshold-identity`.

**Reviewer certification note (round 13).** Independently re-verified with
a fresh 20,000-trial exact-`Fraction` script (`/tmp/round-13/verify.py`,
using the certified `Phi=(T+A)/2` formula on the bisect-$p_1$ construction
directly, not the builder's own script): 2,374 trials satisfied the
threshold $p_2\le T/D_n$, and the bound $\Phi\le a_nT$ held in every one,
zero violations. Statement and proof correct as written; the trichotomy
framing in the parent approach file (case (a)/(b1)/(b2)) is an accurate,
non-overclaiming restatement of what this lemma covers. **Certified.**
