# Build report — grid-counting-shared-primes (round 2)

## Status
partial (as instructed — STUCK-RECOVERY bounded deliverable; did not attempt to sharpen the threshold to R).

## Deliverables completed

### 1. Large-prime-span lemma — CERTIFIED
File: `/home/agentuser/repo/results/imo-2026-06/lemmas/large-prime-span-divides-at-most-one-term.md`

Statement: with $S_N:=a_N-a_1\le(N-1)R$ (Gap bound Lemma 2, telescoped), a prime $p>S_N$ divides at most one of $a_1,\ldots,a_N$.
Proof: if $p\mid a_i,a_j$ ($i<j$) then $p\mid(a_j-a_i)$, a nonzero multiple of $p$, so $a_j-a_i\ge p$; but $0<a_j-a_i\le S_N<p$, contradiction. One paragraph, rigorous, no gaps. Corollary: every shared prime among the first $N$ terms is $\le S_N\le(N-1)R$ (growing window).

### 2. Cell-count bound (Step 5) — DERIVED
Cell $(i,j)$ carries $P(a_i)\cap P(a_j)$; for prime $p\le S_N$, $c_p:=\#\{i:p\mid a_i\}\le\lfloor S_N/p\rfloor+1\le S_N/p+1$ (multiples of $p$ in an interval of length $S_N$ number $\le S_N/p+1$). So $p$ covers $\le(S_N/p+1)^2$ cells. Expanding:
$$\sum_{p\le S_N}(S_N/p+1)^2 = S_N^2\sum1/p^2+2S_N\sum1/p+\pi(S_N).$$

### 3. Analytic input $\sum_p1/p^2<1/2$ — PROVED elementarily (no PNT/Siegel/Jacobsthal)
knowledge_base has NO Euler-product / prime-sum entry; re-derived from scratch:
- Euler product for $\zeta(2)=\pi^2/6$: $\sum_{\gcd(n,6)=1}1/n^2=\zeta(2)\prod_{p\mid6}(1-1/p^2)=\pi^2/9$.
- Primes $\ge5$ are coprime to 6, so $\sum_{p\ge5}1/p^2\le\sum_{n\ge5,\gcd(n,6)=1}1/n^2=\pi^2/9-1-1/25$.
- $\sum_p1/p^2 \le 1/4+1/9+\pi^2/9-26/25$.
- Archimedes $\pi<22/7\Rightarrow\pi^2<484/49<10\Rightarrow\pi^2/9<10/9$.
- $\Rightarrow\sum_p1/p^2 < 1/4+11/9-26/25 = 389/900 < 1/2$.

Verified numerically (prime zeta $P(2)\approx0.45225<1/2$; rigorous bound $389/900\approx0.4322$). Lower-order terms: $\sum_{p\le x}1/p\le1+\log x$, $\pi(x)\le x$ (elementary).

### 4. Central gap (Step 6) — STATED EXPLICITLY [GAP]
Two structural ceilings, both characterized honestly:
- **(G1) Growing window.** The threshold is $S_N\le(N-1)R$ (grows with $N$), NOT the fixed $R$ of crux Lemma 4. Sharpening $S_N\rightsquigarrow R$ is exactly the free-rider dichotomy = the crux itself; no counting argument lowers the threshold without assuming the conclusion (large primes $p\in(R,S_N]$ can divide two terms without contradicting the span bound).
- **(G2) Aggregate vs. per-cell.** The bound (7) is multiplicity-weighted; an aggregate upper bound on small-prime coverage does NOT force every cell to be small-prime-covered (coverage can be uneven; double-counting inflates the sum). Counting is intrinsically too coarse for the per-cell conclusion.

### 5. Steps 1–3, 7 — WRITTEN
- §1 inherits Lemmas 1,2,3 from `essential-monovariant` + span bound (1) by telescoping.
- §2 forms the $N\times N$ shared-prime grid; every off-diagonal cell nonempty (greedy).
- §3 = Lemma 4 (large-prime-span) + Corollaries 4a/4b.
- §7 inherits the conditional Theorem (Lemma 4 $\Rightarrow$ $a_{n+T}=a_n+L_0$ for all $n\ge1$, no transient) from `essential-monovariant` §5.

## Output
- Approach file: `/home/agentuser/repo/results/imo-2026-06/approaches/grid-counting-shared-primes.md` (Status: partial).
- Certified lemma: `/home/agentuser/repo/results/imo-2026-06/lemmas/large-prime-span-divides-at-most-one-term.md`.
- Promotable lemmas listed at the bottom of the approach file: large-prime-span (certified) + prime-zeta-2 bound ($\sum_p1/p^2<389/900<1/2$).

## Honest ceiling (for next round's orchestrator)
Counting alone cannot close the crux. The growing-window bound $\le(N-1)R$ is the structural ceiling; reaching the fixed $\le R$ requires the free-rider dichotomy via Route D (`essential-monovariant`) or Route P (`propagation-bezout`). The certified large-prime-span lemma is the route's durable contribution. The counting route should NOT be re-dispatched to "close the gap" — the gap is the crux itself.
