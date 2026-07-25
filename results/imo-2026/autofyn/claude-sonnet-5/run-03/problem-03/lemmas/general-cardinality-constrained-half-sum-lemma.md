## Source
`approaches/self-similar-induction-on-n.md`, round 21, "Round 21: full
closure of the General Cardinality-Constrained Half-Sum Lemma (all
$k\ge2$)," Steps A–C. Certified by the round-21 proof-reviewer after full
independent re-derivation (own exact-`Fraction` and exhaustive-enumeration
scripts, not reusing the builder's): an exhaustive small-$k$ search
confirming Step A's pigeonhole with no random-sampling gaps
(`/tmp/verify_stepA_exhaustive.py`, $k=2,3,4$, zero counterexamples), an
exhaustive confirmation of Case (C1)'s forced unique allocation
(`/tmp/verify_C1_exhaustive.py`, $k=2,\dots,6$, every active level), a
1125-instance random canonical-form sweep across $k=2,\dots,7$ with zero
$\mathrm{AltSum}<1$ violations and zero Step-A failures
(`/tmp/verify_gch.py`), and a targeted 3000-instance fine-grid search
specifically stress-testing Case (C2)'s piecewise-affine floor
(`/tmp/verify_c2_finegrid.py`, $k=2,\dots,6$, $|A|\ge2$, 4000-point grids
per instance): zero violations of the floor $\min(\mathrm{AltSum}(A),
\min_i\mathrm{AltSum}(A\setminus\{v_i\}))\ge1$ in every case.

## Setting

$\mathrm{GCH}(k)$: $R$ a finite multiset, $\max(R)\le\mathrm{cap}:=
2^{k-1}$, $|R|\le k+1$, $\mathrm{sum}(R)=S\in[2^k,2^k+1)$; $\Gamma_{k-1}
=\{2^{k-1},\dots,2,1\}$ ($k$ levels, values $2^0,\dots,2^{k-1}$).
By the already-certified Finite Reduction Theorem
(`invisible-block-skip-fact-and-general-pairwise-reduction.md`), it
suffices to prove $\mathrm{AltSum}(R''\cup\Gamma_{k-1})\ge1$ for every
feasible **canonical form** $R''$: integer multiplicities $n_0,\dots,
n_{k-1}\ge0$ at the $\Gamma$-levels (level $j$ has value $2^j$) plus at
most one free block $(t,r)$, $t\ge0$ copies of $r\notin\Gamma_{k-1}$,
$r\in(0,\mathrm{cap}]$, subject to $\sum_j n_j2^j+tr=S$, $\sum_j n_j+t
\le k+1$.

By the already-certified Lemma BCF, level $j$ is **active** iff $n_j$ is
even (contributing $\pm2^j$ to $\mathrm{AltSum}$) and **inactive** iff
$n_j$ is odd (contributing $0$); the free block is **active** iff $t$ is
odd (contributing $\pm r$) and **inactive** iff $t$ is even (including
$t=0$). Writing $A:=\{2^j:j\text{ active}\}$, $\mathrm{AltSum}(R''\cup
\Gamma_{k-1})=\mathrm{AltSum}(A\cup\{r\}\text{ if free block active, else
}A)$.

## Theorem (General Cardinality-Constrained Half-Sum Lemma)

For every $k\ge2$ and every feasible $R$ of $\mathrm{GCH}(k)$,
$$\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge\frac{S+2^k}2,\qquad\text{equivalently}
\qquad\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1.$$

*Proof.* By the Finite Reduction Theorem it suffices to check every
feasible canonical form $R''$.

**Step A (Canonical-Form Pigeonhole Lemma).** It is impossible for every
level $j=0,\dots,k-1$ to be inactive (all $n_j$ odd) **and** the free
block inactive/absent ($t=0$ or $t$ even $\ge2$) simultaneously.
*Proof.* If all $n_j$ odd, each $n_j\ge1$ so $\sum_jn_j\ge k$; with budget
$\sum_jn_j+t\le k+1$ this forces $t\le1$. Inactive/absent free block needs
$t\in\{0,2,4,\dots\}$; the only such value $\le1$ is $t=0$. So $t=0$ is
forced, $S=\sum_jn_j2^j$ exactly. Writing $n_j=1+2m_j$, $S=(2^k-1)+2N$
for integer $N=\sum_jm_j2^j\ge0$, i.e. $S$ is an odd integer. But
$S\in[2^k,2^k+1)$ contains only the even integer $2^k$ — contradiction.
$\blacksquare$

Consequence: every feasible $R''$ has $A\ne\varnothing$ or the free block
active (or both), splitting into cases (B) $A\ne\varnothing$, free
inactive; (C0) $A=\varnothing$, free active; (C1) $|A|=1$, free active;
(C2) $|A|\ge2$, free active.

**Step B (Active-$\Gamma$-Subset Alternating Sum Lemma).** For any
nonempty $A'\subseteq\{2^0,\dots,2^{k-1}\}$ sorted decreasing $a_1>
\cdots>a_p$, $\mathrm{AltSum}(A')=a_1-a_2+\cdots\ge1$.
*Proof.* For distinct powers $2^x>2^y$, $2^x-2^y=2^y(2^{x-y}-1)\ge2^y\ge1$.
Pair $(a_1,a_2),(a_3,a_4),\dots$; each pair contributes $\ge1$; a leftover
term (if $p$ odd) contributes $\ge1$ directly. Sum of nonnegative,
$\ge1$-valued terms, at least one present, is $\ge1$. $\blacksquare$
This closes case (B) directly.

**Case (C0): $A=\varnothing$.** All $k$ levels inactive forces (as in
Step A) $t\le1$; $t$ odd $\ge1$ forces $t=1$, then $\sum n_j\le k$
combined with $\sum n_j\ge k$ forces $n_j=1$ for every $j$. So
$S=(2^k-1)+r$, $r=S-2^k+1\in[1,2)$; $r=1$ is excluded (would coincide
with $\Gamma$-level $0$, contradicting $r\notin\Gamma_{k-1}$, so this
degenerate case is simply not a valid canonical form and does not need to
be handled), giving $r\in(1,2)$ and $\mathrm{AltSum}(\{r\})=r>1\ge1$.

**Case (C1): $A=\{v\}$, $v=2^{j_A}$.** The other $k-1$ levels are
inactive, $\sum_{j\ne j_A}n_j\ge k-1$; budget gives $n_{j_A}+t\le2$; since
$n_{j_A}\ge0$ even and $t\ge1$ odd, only $(n_{j_A},t)=(0,1)$ fits. This
forces $\sum_{j\ne j_A}n_j\le k$, and since any $n_j>1$ must jump to
$\ge3$ (cost $\ge2$, but only $1$ unit of slack is available), $n_j=1$
for every $j\ne j_A$ is forced. Hence $S=(2^k-1-v)+r$, $r=S-2^k+1+v\in
[1+v,2+v)$, so $r>v$ and $\mathrm{AltSum}(\{v,r\})=r-v\in[1,2)\ge1$.

**Case (C2): $|A|\ge2$ (feasibility-free — holds for every $r\in(0,
\mathrm{cap}]\setminus\Gamma_{k-1}$).** Write $A=\{v_1>\cdots>v_p\}$,
$p\ge2$; cut $(0,\mathrm{cap}]$ at $v_1,\dots,v_p$ into open
sub-intervals. Within each, $r$'s rank among $A\cup\{r\}$ is constant (no
element of $A$ crossed, by the already-certified Fact 1 / Invisible-Block
Skip Fact), so $\mathrm{AltSum}(A\cup\{r\})=C+\sigma r$ is affine, slope
$\sigma=\pm1$. As $r\to v_i$ (either side), $A\cup\{r\}\to A\cup\{v_i\}$,
an even block that (already-certified Lemma TPC) contributes $0$ and can
be deleted, giving continuous boundary value $\mathrm{AltSum}(A\setminus
\{v_i\})$; as $r\to0^+$, the value $\to\mathrm{AltSum}(A)$. On the
topmost interval $(v_1,\mathrm{cap}]$, $r$ is always rank $1$ (sign
$+$), so the function is increasing, with minimum at the captured
endpoint $r\to v_1^+$ ($=\mathrm{AltSum}(A\setminus\{v_1\})$); on the
bottom interval $(0,v_p)$, whichever of the two possible signs occurs,
the interval's minimum is always at a captured endpoint ($0$ or $v_p$);
every internal interval has both endpoints captured. By Step B, every
endpoint value ($\mathrm{AltSum}(A)$ or $\mathrm{AltSum}(A\setminus
\{v_i\})$, each a nonempty subset since $|A|\ge2$) is $\ge1$; by
monotonicity of an affine function, every interior value lies between two
such endpoints, hence is also $\ge1$. $\blacksquare$

Combining (B)/(C0)/(C1)/(C2) covers every feasible canonical form, so
$\mathrm{AltSum}(R''\cup\Gamma_{k-1})\ge1$ always, and by the Finite
Reduction Theorem this extends to every feasible $R$. $\blacksquare$

**Scope note.** The cardinality cap $|R|\le k+1$ is load-bearing exactly
twice: in Step A (forcing $t=0$ in the all-inactive case) and in Case
(C1) (forcing the unique singleton allocation); consistent with round
18's independent finding that a counterexample exists once the cap is
relaxed. Case (C2) needs no cardinality argument at all.

## Consequence

Via the already-certified Half-Sum Corollary route, this closes
$\mathrm{GT}(m)$ sub-case (i) (odd excess $e=1$) for **every** $k\ge2$,
i.e. for the full range $a_1\in(2^{k-1},2^k]$ — superseding the round-18
"width-1 window" residual. It does **not** close $\mathrm{GT}(m)$ as a
whole: the $e=0$ sliver (`Case-B(m,k)`) and odd excess $e\ge3$ remain
open, untouched by this lemma.
