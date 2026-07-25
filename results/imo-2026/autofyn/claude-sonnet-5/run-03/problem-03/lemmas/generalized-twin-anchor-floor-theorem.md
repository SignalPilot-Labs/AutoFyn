# Generalized Twin-Anchor Floor Theorem

Certified round 16 (proof-reviewer), from
`approaches/reciprocal-potential-induction-on-n.md` (round 16, first
build). Strictly generalizes the already-certified
`lemmas/twin-anchor-floor-theorem.md` (which is the single case
$\delta=1/(2^N-1)$) to an entire one-parameter family of $\delta$ per $N$.

**Statement.** Fix an integer $N\ge4$ and any real $\delta$ with
$0<\delta<\dfrac2{N(N-1)}$. Let
$$a:=\frac{1-\delta N(N-1)/2}{N}>0,\qquad p_i:=a+(N-i)\delta\ \ (i=1,\ldots,N),$$
so $p_1>p_2>\cdots>p_N=a>0$, $\sum_ip_i=1$. Then $p=(p_1,\ldots,p_N)$ is a
legal LB partition ($N-1$ pieces beyond the first, needing an $(N-1)$-cut
game budget), and there is a legal XY response using exactly $N-2\le N-1$
cuts, all resulting fragments strictly positive, achieving
$\mathrm{OddSum}=\tfrac12$ exactly — the universal absolute floor
($\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$ for any legal response $M$).
Hence $V_{N-1}(p)=\tfrac12$ exactly.

**Construction.** Piece $1$ splits into $p_{N-1}=a+\delta$ and
$p_1-p_{N-1}=(N-2)\delta$; piece $2$ splits into $p_N=a$ and
$p_2-p_N=(N-2)\delta$; each piece $j=3,\ldots,N-2$ (empty if $N\le5$)
bisects into two equal halves; pieces $N-1,N$ are left untouched. This
uses $2+\max(N-4,0)=N-2$ cuts.

**Why it works.** The construction is verbatim the certified Twin-Anchor
Construction, but its proof never actually uses the specific value
$\delta=1/(2^N-1)$ — only that $p$ is a strictly decreasing arithmetic
progression of positive reals summing to $1$. The key algebraic identity
$p_1-p_{N-1}=p_2-p_N=(N-2)\delta$ holds for every $\delta$ (direct
substitution of $p_i=a+(N-i)\delta$), giving $N-1$ exactly-equal pairs
($(p_{N-1},p_{N-1})$, $(p_N,p_N)$, $((N-2)\delta,(N-2)\delta)$, and the
$N-4$ bisection-halves). By the already-certified Even-Block-Neutrality
mechanism, every even-sized equal-value block contributes $0$ to
$\mathrm{AltSum}$ regardless of interleaving, so $\mathrm{AltSum}(M)=0$
and $\mathrm{OddSum}(M)=\tfrac12(\mathrm{sum}(M)+\mathrm{AltSum}(M))=
\tfrac12$.

**Reviewer independent verification.** Own from-scratch exact-`Fraction`
script (not the builder's): $N=4,\ldots,11$, $20$ random rational
$\delta\in(0,2/(N(N-1)))$ per $N$ (160 instances) — every fragment
strictly positive, $\mathrm{OddSum}=1/2$ exactly (as an identical
`Fraction`), zero deviations. Also independently re-verified the two
specific reduction-map applications the builder used this as a test point
for (the certified $e_0(n)$ itself, and the "drop the smallest piece,
renormalize" map $p'_i=p_i/(1-a)$ applied to $e_0(n)$, $n=4,\ldots,7$):
confirmed $p'$ is again a positive decreasing AP with the claimed
$\delta'=\delta/(1-a)$, and the theorem gives $V=1/2$ there too, matching
the builder's report exactly.

## Scope note

This is an elementary, general-purpose extension of an existing certified
fact (not itself a step toward either open gap of the whole problem). It
was used this round to refute the pointwise reciprocal-recursion
inequality $(\star)$ (`approaches/reciprocal-potential-induction-on-n.md`,
Status `unsolved`, that framing is a dead end) — see that file for the
refutation. Reusable by any future approach needing a large supply of
exact points where $V(p)=1/2$ (the universal floor), for cheap-killing
future proposed general inequalities on $V(p)$.
