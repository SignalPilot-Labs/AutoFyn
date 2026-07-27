# IMO 2026 Problem 6

Let $a_1, a_2, \ldots$ be an infinite sequence of integers $>1$. $a_{n+1}$ is the smallest integer $> a_n$ with $\gcd(a_{n+1}, a_i)>1$ for every $i\le n$. Prove $\exists\, T,L>0$ with $a_{n+T}=a_n+L$ for all $n\ge1$.

## Status
solved

## Approaches tried
- `transversal-single-cycle-finish` (mechanism δ) — verified-milestone. Conditional theorem "if $\mathcal M=\min\{P(a_i):i\ge1\}$ is finite then $a_{n+T}=a_n+L$ for every $n\ge1$" fully rigorous and computationally verified ($a_1=15\to T=8,L=30$; $a_1=429\to T=908,L=4290$; $a_1=30\to T=1,L=2$). The **imported finish** (Piece C) composed into the solved proof below.
- `large-prime-descent` (round 130) — SOLVED. Reproduces the published IMO 2026 P6 solution (Evan Chen's notes, 2026-07-23). Three pieces: Piece A (unconditional "appears $\iff$ valid against $\prec$-minimal terms below $x$") proved inline, no finiteness, no circularity; Direction B ($\mathcal M\subseteq\{$$\prec$-minimal supports$\}$) proved, Direction A flagged false and unused; Crux 1 (large-prime descent by induction on $n$) proved with all four sub-lemmas (landing, index-descent, shared-prime transfer, rad-divisibility); corollary $\mathcal M$ finite; Piece C imported from certified `post-stabilization-theorem`. Reviewer APPROVED round 130.
- `density-promotion-bound` (α), `bounded-gap-lcm-reduction` (γ), `pstar-core-straggler`, `smooth-window-crash` — frozen (round 130); the descent closes the wall they were attacking uniformly, without their machinery (SPT/$p^*$, $W_1$/$W_2$, Cov, mtp-window, regime split). Their certified lemmas retained as imports.
- `bertrand-dickson-eviction` (β), `omega-induction-loaded` (ε) — RETIRED (dead).

## Current best
**SOLVED** — the complete proof below. Wall "$\mathcal M$ finite" closed by the large-prime descent; period conclusion by the certified δ finish.

**Self-contained writeup:** `results/imo-2026-06/self-contained-solution.md` — the complete proof with every lemma (Piece A, Direction B, the large-prime descent, the Corollary, and the entire Finish: pairwise intersection, transversal residue characterization via CRT, universal membership / no transient, greedy = cyclic successor, single-cycle with period-sum $L$) proved IN FULL inside the one document, no proof-step imports. Reviewer APPROVE (round 131, `verified-milestone`).

## Full proof

Let $P(m)$ denote the set of prime divisors of $m>1$ and $\mathrm{rad}(m)=\prod_{p\in P(m)}p$. Define the index-ordered radical partial order
$$a_m\prec a_n \iff m<n\ \text{and}\ \mathrm{rad}(a_m)\mid\mathrm{rad}(a_n)\quad(\text{i.e.}\ P(a_m)\subseteq P(a_n),\ m<n).$$
A term is **$\prec$-minimal** if no earlier term subsumes it rad-wise. The sequence is strictly increasing, so $i<n\iff a_i<a_n$.

**Piece A (unconditional).** For every $x\ge a_1$: $x$ appears $\iff$ $\gcd(x,a_i)>1$ for every term $a_i<x$ $\iff$ $\gcd(x,a_i)>1$ for every $\prec$-minimal term $a_i<x$. (Proved in `appears-criterion-unconditional`; uses only the greedy no-skip argument and the $\prec$-minimal chain reduction — no finiteness.)

**Direction B.** Every $M\in\mathcal M=\min\{P(a_i)\}$ is the support of some $\prec$-minimal term. (Take the first-appearing term with support $M$; if a still-earlier term subsumed it rad-wise, $\subseteq$-minimality of $M$ would force equality, contradicting first-appearance. Direction A is false and unused.)

**Large-prime descent.** Call a prime **large** if $p>a_1^2$. We prove by induction on $n$:

> (IH$_n$) Every $\prec$-minimal term $a_i$ with $i<n$ is $a_1^2$-smooth (carries no large prime).

*Base $n=1$:* vacuous; also $a_1$'s primes are $\le a_1<a_1^2$.

*Inductive step:* assume (IH$_n$); suppose $a_n=pc$ with $p>a_1^2$ large; show $a_n$ is not $\prec$-minimal. By Piece A applied to $x=a_n$, $\gcd(a_n,a_1)>1$; pick a prime $q\mid\gcd(a_1,a_n)$. Then $q\le a_1$, $q\neq p$ (as $p>a_1^2\ge a_1\ge q$), and $q\mid c$. Since
$$a_n/a_1=pc/a_1\ge p/a_1>a_1\ge q,$$
let $k$ be the smallest nonnegative integer with $q^k c\ge a_1$. If $k=0$: $c\ge a_1$ and $c<a_n=pc$ (as $p>1$). If $k\ge1$: $q^{k-1}c<a_1$, so $q^k c<q\,a_1\le a_1^2<a_n$ (as $a_n\ge p>a_1^2$). In both cases $q^k c\in[a_1,a_n)$.

To see $q^k c$ appears: by Piece A it suffices that $\gcd(q^k c,a_i)>1$ for every $\prec$-minimal $a_i<q^k c<a_n$, so $i<n$ and (IH$_n$) gives $p\nmid a_i$. Since $a_n$ appears after $a_i$ ($i<n$), the greedy rule gives $\gcd(a_n,a_i)>1$; pick a prime $r\mid\gcd(a_n,a_i)$. As $p\nmid a_i$ while $p\mid a_n$, $r\neq p$; so $r\mid c\mid q^k c$, giving $\gcd(q^k c,a_i)\ge r>1$. Hence $q^k c$ appears.

Let $j=\mathrm{idx}(q^k c)$. Since $q^k c<a_n$, $j<n$. And $q\mid c$ gives $P(q^k c)=P(c)\subseteq P(c)\cup\{p\}=P(a_n)$, i.e. $\mathrm{rad}(q^k c)\mid\mathrm{rad}(a_n)$. So $a_j\prec a_n$ with $j<n$; $a_n$ is not $\prec$-minimal. Contrapositively, if $a_n$ is $\prec$-minimal it is $a_1^2$-smooth, extending (IH$_n$) to (IH$_{n+1}$). ∎

**Corollary ($\mathcal M$ finite).** Every $\prec$-minimal term is $a_1^2$-smooth (descent). By Direction B every $M\in\mathcal M$ is the support of a $\prec$-minimal term, so $M\subseteq P_0=\{p\le a_1^2\}$. Hence $\bigcup\mathcal M\subseteq P_0$ (finite) and $\mathcal M\subseteq 2^{P_0}$ (finite).

**Finish.** With $\mathcal M$ finite, the certified `post-stabilization-theorem` applies: set $P=\bigcup\mathcal M$, $L=\prod_{p\in P}p$ (squarefree), and $V=\{r\in\{0,\ldots,L-1\}:\{p\in P:p\mid r\}\text{ is a transversal of }\mathcal M\}$, $T=|V|$. Then
$$a_{n+T}=a_n+L\qquad\text{for every }n\ge1.$$
(The theorem composes `transversal-residue-characterization`, `universal-membership-no-transient` (zero transient: dynamics hold from $n=1$), `greedy-equals-cyclic-successor`, `cyclic-successor-single-cycle` (single $|V|$-cycle with period-sum $L$); all reviewer-certified, conditional on $\mathcal M$ finite, which the Corollary supplies. The composition is non-circular: the descent establishes $\mathcal M$ finite and uses only the unconditional Piece A, not the conditional finish.) ∎

*Verified numerically:* $a_1=15\to T=8,L=30$; $a_1=429\to T=908,L=4290$; $a_1=30\to T=1,L=2$; period $a_{n+T}=a_n+L$ confirmed for all $n\ge1$ (no transient) on $a_1\in\{15,30,175,323,385\}$.
