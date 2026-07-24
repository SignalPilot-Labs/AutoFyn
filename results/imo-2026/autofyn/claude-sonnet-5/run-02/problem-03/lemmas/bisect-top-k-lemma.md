## Bisect-Top-$k$ Lemma

**Statement.** For any $m\ge1$, any marking $p_1\ge\cdots\ge p_m>0$
($T=\sum p_i$, $n=m-1$), and any integer $0\le k\le n$: bisecting each of
the top $k$ pieces $p_1,\dots,p_k$ individually (exactly $k$ legal cuts,
one per piece, within Xiang Yu's budget $n$) and leaving
$p_{k+1},\dots,p_m$ untouched achieves, exactly,
$$\Phi = \frac{T+A(\{p_{k+1},\dots,p_m\})}{2},$$
and hence, by `max-domination-lemma`,
$$\Phi\ \le\ \frac{T+p_{k+1}}{2}\qquad(\text{reading }p_{k+1}:=0\text{ if }k=m).$$
Consequently $\Phi\le a_nT$ (where $a_n=2^n/(2^{n+1}-1)$) whenever
$p_{k+1}\le T/D_n$ ($D_n=2^{n+1}-1$) — an unconditional sufficient
condition, for every $n\ge0$ and every $k\in\{0,\dots,n\}$, with no
induction hypothesis of any kind.

## Proof

The final multiset after bisecting the top $k$ pieces is
$M_k:=\{p_1/2,p_1/2,\dots,p_k/2,p_k/2\}\cup R$, $R:=\{p_{k+1},\dots,p_m\}$.

We show $A(M_k)=A(R)$ by chaining $k$ applications of the certified
`pair-cancellation-identity` ($A(\{a,a\}\cup T)=A(T)$ for any $a>0$, any
finite multiset $T$ of positive reals, no domination/ordering hypothesis).
Define $R_0:=R$, $R_j:=\{p_j/2,p_j/2\}\cup R_{j-1}$ for $j=1,\dots,k$, so
$R_k=M_k$. By `pair-cancellation-identity` at each step (multiset union is
commutative/associative, so insertion order is immaterial), $A(R_j)=
A(R_{j-1})$ for each $j$, hence $A(M_k)=A(R_k)=\cdots=A(R_0)=A(R)$.

Since $\mathrm{Total}(M_k)=T$ (bisection preserves mass),
$\Phi(M_k)=(T+A(M_k))/2=(T+A(R))/2$. By `max-domination-lemma`, $A(R)\le
\max(R)=p_{k+1}$ (or $A(\varnothing)=0$ if $k=m$), giving $\Phi\le
(T+p_{k+1})/2$. Finally $(T+p_{k+1})/2\le a_nT\iff p_{k+1}\le(2a_n-1)T=
T/D_n$, using the certified telescoping identity $2a_n-1=1/D_n$.
$\blacksquare$

**Relation to prior work.** $k=1$ recovers the previously-certified
`unconditional-p2-threshold-closure` exactly.

## Certification note (proof-reviewer, round 14)

Independently re-derived and re-verified with a fresh 7000-trial
exact-`Fraction` script (n=1..7, every k=0..n, 200 random markings per
(n,k) pair): zero violations of $\Phi\le(T+p_{k+1})/2$ and of the
$p_{k+1}\le T/D_n\Rightarrow\Phi\le a_nT$ threshold implication. The chained
`pair-cancellation-identity` application is valid — each step's hypothesis
(a>0, T a finite multiset of positive reals) is satisfied regardless of
insertion order, since the lemma imposes no relation between $a$ and $T$.
`max-domination-lemma` and the telescoping identity $2a_n-1=1/D_n$ are
already certified/re-verified in this project. No gap found. Certified
correct as written.

**Coverage note (not part of the certified statement, informational only):**
the union over $k=0,\dots,n$ of this lemma's sufficient condition covers
only $\approx10$–$26\%$ of case-(b2) witnesses (per the builder's and this
reviewer's independent sampling) — it does not close case (b2) or Open Gap
1 in general.

**Origin:** `results/imo-2026-03/approaches/lp-duality-certificate.md`,
round 14, R14.1.
