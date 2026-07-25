# Chain-Correction Floor Theorem

Certified round 14 (proof-reviewer), from `lp-duality-split-polytope.md`.

## Statement

Let $n\ge6$, $N:=n+1$, $\delta:=\gamma(n)=1/(2^N-1)$, and let $e_0$ be the
region vertex of $\overline{B(n)}$ with coordinates $p_i(e_0)=a+(N-i)\delta$
for $i=1,\dots,N$ (an exact arithmetic progression with common difference
$\delta$), where $a:=p_N(e_0)=\dfrac{2-n(n+1)\delta}{2(n+1)}$ (certified,
`lemmas/finite-cell-vertex-reduction-and-region-classification.md`).

Then there is a legal XY response at $e_0$ — splitting exactly the $N-2=n-1$
pieces $p_1,\dots,p_{N-2}$ (leaving $p_{N-1},p_N$ untouched), using exactly
$n-1\le n$ cuts, all resulting fragments strictly positive — achieving
$$\mathrm{OddSum}(M)=\frac12$$
exactly: the universal absolute floor for *any* legal response at *any*
partition (immediate from $\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$, since a
descending sort's consecutive-pair differences are each $\ge0$).

**Construction.** Write $u_1:=(N-1)\delta$, $u_2:=(N-3)\delta$.
- Piece $1=a+(N-1)\delta$ splits as $(a,\,u_1)$.
- Piece $2=a+(N-2)\delta$ splits as $(a+\delta,\,u_2)$.
- Piece $3=a+(N-3)\delta$ splits as $(u_1,\,a-2\delta)$.
- Piece $5=a+(N-5)\delta$ splits as $(u_2,\,a-2\delta)$.
- Piece $4$ and every piece $j=6,\dots,N-2$ bisect into two exact halves.
- Pieces $N-1,N$ are left untouched.

**Key algebraic identity.** Piece $3$'s second fragment $p_3-u_1$ and piece
$5$'s second fragment $p_5-u_2$ both equal $a-2\delta$ identically (the
$N$-dependence cancels in each).

**Positivity.** All fragments are positive iff $a>2\delta$, equivalent to
$(n+1)(n+4)<2^{n+2}-2$, which holds for all $n\ge6$ (proved by induction:
base $n=6$, $70<254$; inductive step uses $2^{n+2}\ge256>2n+6$ for $n\ge6$).

**Why OddSum $=1/2$.** The $2N-2$ fragments partition into $N-1$
equal-valued pairs: $(p_N,a)$, $(p_{N-1},a+\delta)$, $(u_1,u_1)$,
$(u_2,u_2)$, $(a-2\delta,a-2\delta)$, and the bisection-halves of pieces
$4,6,\dots,N-2$. By the Even-Block-Neutrality mechanism (an even-sized block
of one repeated value occupies consecutive ranks in the descending sort and
contributes exactly $0$ to $\mathrm{AltSum}$, regardless of interleaving
with other groups, since insertion of an even block shifts every other
element's rank by an even number, preserving parity), every group
contributes $0$, so $\mathrm{AltSum}(M)=0$ and
$\mathrm{OddSum}(M)=\tfrac12(1+0)=\tfrac12$.

## Consequence (correction to a prior overclaim)

The certified `finite-cell-vertex-reduction-and-region-classification.md`
and `global-lp-vertex-sufficiency.md`'s Section 4.3 prove
$V(e_0)\le c(n)$ via the $k$-Anchor-Merge construction (attaining exactly
$c(n)$ when the AP-pair count $k$ is odd, which is the case realized at
$e_0$) — an upper-bound witness only. This theorem exhibits a strictly
better (smaller) legal response at the same $e_0$ for $n\ge6$, so the true
value is $V(e_0)=\tfrac12$ (not $c(n)$) for every $n\ge6$. This is strictly
compatible with, and does not threaten, the Existence Theorem's actual
target ($V(p)\le c(n)$ for every $p$) — it only corrects a specific
mis-stated equality claim ("$V(e_0)=c(n)$ exactly, the tightest possible
case") found in `global-lp-vertex-sufficiency.md` (corrected in place by the
reviewer this round); it does not affect any downstream derivation there
(the Mass-Constraint Theorem's corollary uses only $e_0$'s coordinates, not
the value of $V(e_0)$).

## Reviewer independent verification

Re-implemented the construction from scratch in exact `Fraction` arithmetic
for $n=6,7,8,9,10,12,15,20$ (own script, not the builder's): confirmed every
fragment strictly positive, total mass exactly $1$, $\mathrm{AltSum}=0$
exactly (hence $\mathrm{OddSum}=1/2$ exactly) in all 8 cases; confirmed the
Positivity Lemma's inequality $(n+1)(n+4)<2^{n+2}-2$ holds for
$n=6,\dots,24$; confirmed algebraically (symbolic Fraction check) that
$p_1(e_0)=1/(n+1)+n\gamma(n)/2$ and $p_N(e_0)=1/(n+1)-n\gamma(n)/2$ match
the builder's and the certified vertex-classification file's formulas
exactly. Zero deviation found. Fully proved, no gaps.
