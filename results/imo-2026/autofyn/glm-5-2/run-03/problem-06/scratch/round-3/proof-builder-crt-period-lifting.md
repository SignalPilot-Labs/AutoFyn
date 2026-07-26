# proof-builder report — crt-period-lifting (IMO 2026 P6), round 3

## Status
**partial.** Gap A (finiteness of governing primes) remains the single open wall.

## What I proved

1. **Lemma F2 (unconditional divisibility-progression structure).** $\mathcal B_\infty=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\{m:\operatorname{rad}(T)\mid m\}$, proved unconditionally via the finite-sub-transversal argument (no Zorn needed — $S(m)$ finite). This isolates a representation that `distinct-supports-stabilize`'s corollary uses only conditionally.

2. **Lemma F2 (squarefree period, conditional on Gap A).** Under Gap A, $\mathcal B_\infty$ is $L$-periodic with $L=\prod_{p\in G}p$ squarefree ($G$ = governing primes). This sharpens `distinct-supports-stabilize` by making squarefree-ness explicit.

3. **Lemma F1 (fiber-count lift bound; unconditional combinatorial identity).** For $A\subseteq\mathbb Z/L\mathbb Z$ and $L=L_k\cdot p$ ($p$ prime), $|A|\le p\cdot|A\bmod L_k|$. Trivially true (fiber counting); **verified computationally** on $a_1\in\{6,30,145,15,35,77,105,175,221,385,847,1309\}$: lift ratio $|A_k|/|A_{k-1}|\le p_k$ in every case (slack 1.0×–11×), and $L$ is squarefree in every case.

4. **Conditional theorem (endgame).** Gap A + F2 + certified `greedy-equals-cyclic-successor` + certified `cyclic-successor-bijection` ⇒ $a_{n+T}=a_n+L$ for all $n\ge1$, with $T\le L=\prod G$ squarefree. Fully rigorous.

## Gaps remaining

**Gap A (the wall, unchanged).** Finiteness of the governing set $G$. The CRT-lift framing does NOT close it:

- The `aimo-0231` nontrivial content (return time of a *polynomial iterate* grows by $\le p$) **does not port**: our cyclic-successor map is structurally a single $|A|$-cycle, so the return time equals $|A|$ and the lift bound is the trivial fiber-count identity (F1), capturing no greedy structure.
- The cofactor-bounding induction (outline Step 4) is **circular**: the actual greedy uses full admissibility (including transient primes), not the $L_k$-skeleton, so the "smallest $L_k$-admissible multiple" cofactor is not determined by the skeleton; bounding which transient primes appear in term supports IS a restatement of Gap A (same circularity certified dead for `witness-density-recurrence` round 2).

## Lemma-candidates (for `results/imo-2026-06/lemmas/`)

1. `binfinity-divisibility-progression-structure` — unconditional F2 representation. Promotable.
2. `squarefree-period-under-gap-A` — conditional F2+F1 refinement of `distinct-supports-stabilize`. Promotable (refinement, not a new gate).

## Key empirical data (lift factors)

| $a_1$ | $L$ | $G$ | $T$ | stage ratios $|A_k|/|A_{k-1}|$ |
|---|---|---|---|---|
| 6 | 2 | {2} | 1 | (2) |
| 385 | 43890 | {2,3,5,7,11,19} | 5088 | 2, 3, 3.67, 5.09, 3.32, 13.68 |
| 1309 | 7854 | {2,3,7,11,17} | 912 | 2, 3, 2, 9.33, 8.14 |
| 847 | 18942 | {2,3,7,11,41} | 1744 | 2, 3, 4, 2.67, 27.25 |
| 175 | 2730 | {2,3,5,7,13} | 274 | 2, 3, 3.67, 1.55, 8.06 |

Every ratio $\le$ the prime added; $L$ squarefree in every case. Lift bound trivially satisfied.

## Approach file
`/home/agentuser/repo/results/imo-2026-06/approaches/crt-period-lifting.md` (Status: partial)
