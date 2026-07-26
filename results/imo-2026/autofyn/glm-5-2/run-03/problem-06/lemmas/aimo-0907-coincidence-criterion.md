# Lemma (positive, reusable tool): aimo-0907 coincidence criterion

**Statement.** Let $X$ be a set and $f:X\to X$ an arbitrary single-valued map. For $x\in X$ write the forward orbit $O(x)=(x, f(x), f^2(x),\dots)$, and $f^k$ for the $k$-th iterate ($f^0=\mathrm{id}$).

**(A) One self-coincidence $\Rightarrow$ eventual periodicity.** If for some $x\in X$ and integers $0\le a<b$ one has $f^a(x)=f^b(x)$, then $O(x)$ is eventually periodic with period $\delta:=b-a>0$: $f^{a+k}(x)=f^{b+k}(x)$ for every $k\ge0$.

**(B) Two between-orbit coincidences at distinct offsets $\Rightarrow$ finiteness.** Suppose $O(x)$ and $O(y)$ are each self-coincidence-free (i.e. $f^r(x)=f^s(x)\Rightarrow r=s$, and likewise for $y$; equivalently each orbit is infinite as a set). Suppose further there exist two pairs of nonnegative integers $(n,m)$ and $(p,q)$ with $f^n(x)=f^m(y)$ and $f^p(x)=f^q(y)$, and that the iterate-offsets $n-m$ and $p-q$ are *distinct*. Then $O(y)$ is eventually periodic (hence finite as a set), contradicting the hypothesis that $O(y)$ is self-coincidence-free.

**Proof.** (A) From $f^a(x)=f^{a+\delta}(x)=f^b(x)$, apply $f^k$ to both sides. Since $f$ is single-valued, equal inputs give equal outputs: $f^{a+k}(x)=f^{a+\delta+k}(x)=f^{b+k}(x)$ for all $k\ge0$. This is exactly eventual periodicity of $(f^n(x))_{n\ge0}$ from index $a$ onward, with period $\delta$. $\square_{(A)}$

(B) WLOG $n-m>p-q$ (otherwise swap the two pairs). Set $\Delta:=(n-m)-(p-q)>0$. Compute $f^{p+m}(y)$ in two ways using the two coincidences and single-valuedness:
- From $f^n(x)=f^m(y)$, apply $f^p$: $f^{p+n}(x)=f^{p+m}(y)$.
- From $f^p(x)=f^q(y)$, apply $f^n$: $f^{n+p}(x)=f^{n+q}(y)$.

The left-hand sides are equal (both $f^{n+p}(x)$). Hence $f^{p+m}(y)=f^{n+q}(y)$. But $(n+q)-(p+m)=(n-m)-(p-q)=\Delta>0$, so $f^{p+m}(y)=f^{p+m+\Delta}(y)$. By part (A), $O(y)$ is eventually periodic with period $\Delta$. An eventually periodic orbit visits only finitely many points, so $O(y)$ is finite as a set — contradicting the hypothesis that $O(y)$ is self-coincidence-free (a self-coincidence-free orbit visits a new point at every step and is infinite as a set). $\square_{(B)}$

**Source / port.** This is the load-bearing move of `aimo-0907` (IMO-SL 2020 A6, Case 2), restated in set/map generality. The original writes it for $f:\mathbb Z\to\mathbb Z$ with orbits of integers; the proof uses only single-valuedness of $f$, so it ports verbatim to any map on any set. No finiteness assumption is made.

**Scope / consumer's responsibility.** The criterion is a *periodicity-via-coincidence* tool; it supplies NO forward-deterministic map. The consumer must exhibit (i) a single-valued transition $f$ on a candidate statistic $\alpha$ (so that part (A) applies to a self-coincidence), or (ii) two orbits with two cross-coincidences at distinct offsets (so that part (B) applies). In the imo-2026-06 setting, the greedy sequence is a SINGLE orbit, so the between-orbits mechanism (B) does not directly apply; the load falls on (A), which requires a forward-deterministic $\alpha$ — and that antecedent is exactly Gap A (see `two-coincidence-periodicity` approach, round 5).

**Status.** Reviewer-certified (round 5). Proof re-derived from scratch and checked: part (A) is the standard single-valuedness propagation; part (B) is the composition-of-two-equalities argument with $\Delta=(n-m)-(p-q)>0$. The lemma is sound and reusable; it does NOT by itself solve or bypass Gap A.
