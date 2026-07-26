# proof-builder — integer-monovariant-transfer (round 3)

## Status: partial

The `aimo-0134` integer-monovariant-transfer framing does NOT close the theorem and is fenced off as a dead framing, with a rigorous structural reason.

## What I proved

1. **Lemma A (block-index advance), rigorous & unconditional** — `results/imo-2026-06/approaches/integer-monovariant-transfer.md`. $b_n=\lfloor(a_n-a_1)/M_1\rfloor$ satisfies $b_{n+1}-b_n\in\{0,1\}$, from the certified gap bound $d_n\le M_1$. Depends only on `linchpin-and-gap-bound`.

2. **Lemma B (bounded integer shortfall)** — the shortfall $c_n=M_1b_n-(a_n-a_1)\in\{0,\dots,M_1-1\}$ is a bounded integer (the skeleton's candidate statistic).

3. **Obstruction Theorem (negative, the load-bearing finding)** — the `aimo-0134` integrality-upgraded-monotonicity mechanism does NOT port to this problem, for a rigorous reason:
   - The cumulative defect $C_n=nM_1-(a_{n+1}-a_1)$ is non-decreasing (forced by $d_n\le M_1$) but **unbounded** in every non-LOCK case (a bounded non-negative integer series $\sum(M_1-d_k)$ would force $d_n\equiv M_1$ eventually = LOCK, contradicting $L/T<M_1$ in non-LOCK cases).
   - The running-average floor $b_n^{\rm avg}=\lfloor(a_n-a_1)/(n-1)\rfloor$ is bounded and eventually constant (= $\lfloor L/T\rfloor$) **only conditional on periodicity** (Cesàro), and is **non-monotone** in every non-LOCK case (concrete counterexample $a_1=15$: $3,2,3,\dots$).
   - **Root cause:** the `aimo-0134` monotonicity step needs a *shrinking* range bound ($a_{k+1}\le k$ shrinks vs. $k+1$, giving $b_{k+1}<b_k+1$); our gap bound $d_n\le M_1$ is *constant*, producing no strict-against-the-average inequality for integrality to upgrade.

4. **Transfer step is also Gap A.** Even granting an eventually-constant statistic, finite-state pigeonhole on $(c_n,\text{recent }d\text{-window})$ fails: the transition is not a function of the state (89 conflicts for $a_1=385$ on $a_n\bmod M_1$; certified finite-statistic explorer). Closing the state = bounding free-rider governing primes = Gap A.

## Computational verification

`sympy` greedy generator, 400–600 terms, 22 starting values incl. 6,15,35,77,91,105,143,385,1309,2085,145,116,1001,847,175,65,221,667,1763,1517,1147,2491. No candidate statistic (shortfall $c_n$, running-avg floor, $|S(a_n)|$, cumulative defect, max-gap-so-far) is simultaneously bounded/eventually-constant AND greedy-monotone-forced in any non-LOCK case. $b_n^{\rm avg}$ stabilizes to $\lfloor L/T\rfloor$ in every resolved case (8 for 385, 6 for 35, 8 for 1309, 4 for 2085) — confirming it is a *consequence* of periodicity, not a cause.

## Gaps remaining

- **Engine gap (load-bearing, unfillable in this framing):** no integer statistic on the orbit is both bounded/eventually-constant and monotone-forced by the greedy rule in non-LOCK cases. The `aimo-0134` shrinking-range mechanism is provably absent here.
- **Transfer gap:** the finite-state pigeonhole is gated by Gap A (the certified transition leak).
- The framing is fenced off: future rounds should NOT re-dispatch the integer-monovariant framing.

## Lemma-candidates for certification

1. **`block-index-advance`** (Lemma A): rigorous, unconditional, reusable. → `results/imo-2026-06/lemmas/block-index-advance.md`.
2. **`aimo-0134-obstruction`** (negative): fences off the `aimo-0134` framing for future outliners. → `results/imo-2026-06/lemmas/aimo-0134-obstruction.md`.

## Per-role rule learned

NEVER: re-dispatch the `aimo-0134` integer-monovariant framing on imo-2026-06 — the eventual-constancy-via-monovariant mechanism requires a *shrinking* range bound (aimo-0134 has $a_{k+1}\le k$); the only available bound here is the *constant* gap bound $d_n\le M_1$, which produces no integrality-upgraded strict inequality, and the running-average floor is provably non-monotone in every non-LOCK case (round 3, integer-monovariant-transfer).
