## Lemmas: Theorem-2-gen general-$V$ sub-case bounds (corrected), and the $L_0(\ell,\varepsilon)$ sliver reduction

**IMPORTANT CORRECTION (proof-reviewer, round 6).** The source file
(`approaches/self-similar-induction-on-n.md`, round 6) states the
sub-case-(i) bound $(\star\star)$ as
$\mathrm{OddSum}(D\cup T')\le(2^{\ell'-1}+W+d_1-1)/2$. This is **false as
literally written** — re-derivation from the stated proof method (peel
$d_1$, then bound the residual via Lemma B) gives $2^{\ell'}$, not
$2^{\ell'-1}$, in the numerator. Exact counterexample to the file's literal
formula: $\ell'=2$ ($T'=\Gamma_1=\{2,1\}$), $D=\{2\}$ ($W=2$, $d_1=2$):
file's formula gives bound $(2+2+2-1)/2=5/2$, but
$\mathrm{OddSum}(\{2,2,1\})=2+1=3>5/2$ — violated. The corrected formula
below (verified by exact symbolic algebra, and confirmed to match every
numeric threshold actually used in the source file's Branches I.A, II.i,
II.ii, none of which use the literal mis-stated formula) is certified in
its place; $(\star)$ (the sub-case-(ii) bound) is certified as stated,
verified correct (diff $=0$ exactly against independent re-derivation).

**Lemma ($\star$, sub-case-(ii) shape).** For $\ell'\ge1$, $T'=\Gamma_{\ell'-1}$
(max $2^{\ell'-1}$, sum $2^{\ell'}-1$), and any multiset $D$ with
$\mathrm{sum}(D)=W$, $\max(D)<2^{\ell'-1}$:
$$\mathrm{OddSum}(D\cup T')\ \le\ \frac{W+3\cdot2^{\ell'-1}-1}{2}.$$

*Proof.* Peel the unique global max $2^{\ell'-1}$ of $D\cup T'$ (Peeling
Lemma), giving $\mathrm{OddSum}(D\cup T')=2^{\ell'-1}+\mathrm{EvenSum}(D\cup T'')$,
$T''=\Gamma_{\ell'-2}$, $\mathrm{sum}(T'')=2^{\ell'-1}-1$. By Lemma B
(First-mover-half) applied to $D\cup T''$: $\mathrm{EvenSum}(D\cup T'')\le
\mathrm{sum}(D\cup T'')/2=(W+2^{\ell'-1}-1)/2$. Summing gives the claim.
$\blacksquare$

**Lemma ($\star\star$, sub-case-(i) shape, CORRECTED).** For $\ell'\ge1$,
$T'=\Gamma_{\ell'-1}$, and any multiset $D$ with $\mathrm{sum}(D)=W$,
$\max(D)=d_1\ge2^{\ell'-1}$:
$$\mathrm{OddSum}(D\cup T')\ \le\ \frac{2^{\ell'}+W+d_1-1}{2}.$$

*Proof.* Peel $d_1$ (global max of $D\cup T'$), giving
$\mathrm{OddSum}(D\cup T')=d_1+\mathrm{EvenSum}(D'\cup T')$, $D'=D\setminus\{d_1\}$
(sum $W-d_1$). By Lemma B applied to $D'\cup T'$:
$\mathrm{EvenSum}(D'\cup T')\le\mathrm{sum}(D'\cup T')/2=((W-d_1)+2^{\ell'}-1)/2$.
Summing: $\mathrm{OddSum}(D\cup T')\le d_1+((W-d_1)+2^{\ell'}-1)/2
=(2^{\ell'}+W+d_1-1)/2$. $\blacksquare$

**$L_0(\ell,\varepsilon)$ sliver reduction (CORRECTED, round 7 — see
`approaches/self-similar-induction-on-n.md`'s "Round 7: bug fix" section).**
With $\ell:=m-1$, $T:=\Gamma_{\ell-1}$: the sliver claim `Case-B(m,k)`'s
residual, $\mathrm{OddSum}(B\cup T)\le2^m-1$ for $b_1:=\max(B)\in
(2^{m-1}-1,2^{m-1})$ where $B$ has $\le m+1$ parts (the outer `Case-B(m,k)`
hypothesis), is **equivalent** (via one peel of $b_1$, using
$\mathrm{sum}(C)=2^\ell+\varepsilon$, $\varepsilon:=2^{m-1}-b_1\in(0,1)$,
$C:=B\setminus\{b_1\}$) to: for every finite multiset $C$ with **at most
$\ell+1$ parts** (inherited: $B$ has $\le\ell+2$ parts, minus the one
removed, $b_1$), $\mathrm{sum}(C)=2^\ell+\varepsilon$ and $\max(C)\le
2^\ell-\varepsilon$,
$$\mathrm{OddSum}(C\cup\Gamma_{\ell-1})\ \ge\ 2^\ell.$$

**Round-7 correction (bug found and fixed).** The statement above omits the
piece-count bound in the round-6 build (both here and in the source
approach file) — **false as literally written without it**: exact
counterexample (round-7 math-explorer), $\ell=2$, $\varepsilon=1/10$,
$C=\{2,\ 5649/10000,\ 1407/2500,\ 9723/10000\}$ (4 parts, exceeding
$\ell+1=3$): $\mathrm{sum}(C)=41/10=2^2+\varepsilon$ ✓, $\max(C)=2\le
2^2-\varepsilon=39/10$ ✓, but $\mathrm{OddSum}(C\cup\Gamma_1)=
\mathrm{OddSum}(\{2,\,9723/10000,\,5649/10000,\,1407/2500,\,2,1\})=
35649/10000<4=2^\ell$ — violated. Restoring the inherited piece bound
$\le\ell+1$ (which the derivation above always produced, since $C$ comes
from removing one element of the piece-bounded $B$) fixes the statement;
this bound was simply dropped when the target was first boxed. All
downstream branch closures (Branches II.ii, II.i-partial, I.A-partial,
$(\star)$/$(\star\star)$ themselves) use only $\mathrm{sum}(C)$ and $\max(C)$,
never the piece count, so they remain valid, now understood as proofs of
the (correctly) piece-bounded statement (a restriction of hypothesis can
only make a true claim easier, not invalidate it).

**Independent verification (proof-reviewer, round 6).** Re-derived the
peeling-algebra reduction to $L_0(\ell,\varepsilon)$ symbolically (sympy,
exact rational arithmetic): confirmed the target simplifies exactly to
$2^\ell$. Independently re-derived $(\star)$ and the corrected $(\star\star)$
from the stated proof method and confirmed both by direct symbolic
substitution (zero residual difference in both cases). Cross-checked that
the numeric thresholds actually claimed in the source file's Branches
II.ii ($2^\ell/8+\varepsilon/2-1/2$), II.i ($2^\ell/4-c_1/2+\varepsilon/2-1/2$),
and I.A ($c_1/2-2^\ell/4+\varepsilon/2-1/2$) all match exact symbolic
re-derivation from first principles (peel + Lemma B, not the mis-stated
abstract $(\star\star)$ formula) — i.e. the file's *specific branch
closures* are correct even though its *general abstract statement* of
$(\star\star)$ contained a typo; the branch closures do not rely on the
erroneous form.

**Source.** Proved in `approaches/self-similar-induction-on-n.md` (round 6,
"Round 6: toward Theorem 2'"), with the $(\star\star)$ typo corrected here
by the proof-reviewer.

**Reuse.** $(\star)$/$(\star\star)$ (corrected) are the genuine
generalization of Theorem 2's two sub-cases to arbitrary total mass $W$
(not just $W=2^m$); reusable by any approach needing a Case-B-style upper
bound on OddSum against a geometric tail with non-power-of-two total (e.g.
`greedy-reduction-geometric`'s leftover-mass targets). The $L_0(\ell,\varepsilon)$
reduction is the precise, reusable starting point for closing the
remaining sliver, whether by this approach or a future one.
