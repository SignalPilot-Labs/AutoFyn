# Exact Periodicity Theorem (certified, round 7)

Source: `approaches/covering-system-construction-exchange.md`, Theorem 4
(a general, reusable, sequence-independent fact; a variant of the
already-certified `periodicity-of-residue-class-union.md`, stated here in
the "increment map is an order isomorphism" form used by the round-7 solved
proof). Independently re-verified by the proof-reviewer.

## Statement

Let $S\subseteq\mathbb Z_{\ge a_1}$ be a set of integers (all $\ge$ some
fixed $a_1$) such that for every $x\ge a_1$: $x\in S \iff x+L\in S$, for
some fixed positive integer $L$. List $S$ increasingly as $a_1=s_1<s_2<
\cdots$ (assume $S$ is infinite, e.g. because it is unbounded above and the
"$\iff$" translation property propagates membership forward and backward
by $L$). Let $T:=|S\cap[a_1,a_1+L)|\ge1$ (finite, positive since $a_1\in S$).
Then $s_{n+T}=s_n+L$ for every $n\ge1$.

## Proof

The map $\varphi(x)=x+L$ is a strictly increasing bijection from $S$ onto
$S\cap[a_1+L,\infty)$ (injective as a translation; maps into that set by
the forward direction of the hypothesis and $x\ge a_1\Rightarrow
x+L\ge a_1+L$; surjective onto it by the backward direction, given
$y\ge a_1+L$, since $y-L\ge a_1$). Since $S\cap[a_1,a_1+L)$ and
$S\cap[a_1+L,\infty)$ partition $S$, and the former has exactly $T$
elements, the increasing enumeration of $S$ splits as $\{s_1,\dots,s_T\}=
S\cap[a_1,a_1+L)$ and $\{s_{T+1},s_{T+2},\dots\}=S\cap[a_1+L,\infty)$.
Since $\varphi$ is an order isomorphism onto the latter set, it sends the
$n$-th smallest element of $S$ to the $n$-th smallest element of
$S\cap[a_1+L,\infty)$, i.e. $\varphi(s_n)=s_n+L=s_{n+T}$ for every $n\ge1$.
$\blacksquare$

## Use in the solved proof

Applied with $S=\mathrm{Term}=\{a_n:n\ge1\}$ once term-membership for
$x\ge a_1$ is shown to depend only on $x\bmod L$ (via the Large-Prime
Elimination Theorem giving the finite prime set $P=\{p\le a_1^2\}$,
$L=\prod_{p\in P}p$), giving exact periodicity $a_{n+T}=a_n+L$ for every
$n\ge1$ with **no transient** — this is the key final step of the full
solution.
