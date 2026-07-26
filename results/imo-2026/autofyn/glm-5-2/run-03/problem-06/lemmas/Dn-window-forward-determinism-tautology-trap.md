# Lemma (negative, structural): $D_n$-window forward-determinism tautology-trap

*Certified: round 7 (reviewer). Source: `approaches/f-of-a1-bounded-nonresidue-statistic.md`. Reviewer independently reproduced the tautology (0 conflicts on $\sigma_n\to d_{n+1}$ at $k=1$ universally) and the set-to-set $k_*\approx T$ / realized$\approx T$ table on $a_1\in\{15,77,375\}$ (corrected naive $O(N^2)$ gcd-greedy; $a_1=375$: $k_*=100$, realized $858$ vs $T=852$; $a_1=77$: $k_*=1$, realized $21$ vs $T=18$; $a_1=15$: $k_*=1$, realized $10$ vs $T=8$).*

## Statement

Let $a_1,a_2,\dots$ be the IMO 2026 P6 greedy sequence, $P_1$ the prime divisors of $a_1$, $M_1=\operatorname{rad}(a_1)$, and $D_n=\{d\in\{1,\dots,M_1\}:\gcd(a_n+d,a_i)>1\ \forall i\le n\}$ the admissible-increment set (so $d_{n+1}=\min D_n$ by the greedy rule, certified `linchpin-and-gap-bound` + `D_n-slack-obstruction` Step 1). For window length $k\ge1$ let $\sigma_n=(D_{n-k+1},\dots,D_n)$.

(a) **The increment-projection $\sigma_n\mapsto d_{n+1}$ is trivially single-valued at $k=1$ (and every $k\ge1$) for every $a_1$**, because $d_{n+1}=\min D_n$ is a function of $D_n\subseteq\sigma_n$. A "0-conflict" probe of this map establishes NOTHING — it is a restatement of the greedy rule. (This was the error behind the round-7 outline-reviewer's false-positive "$k_*=1$" verification.)

(b) The **load-bearing** map for any `aimo-0907-coincidence-criterion` (part A) pigeonhole route is the **set-to-set** forward map $\sigma_n\mapsto\sigma_{n+1}$ (equivalently $\sigma_n\mapsto D_{n+1}$). A self-coincidence $\sigma_a=\sigma_b$ propagates to $d$-periodicity ONLY through single-valuedness of THIS map; the increment-projection (a) gives only the single step $d_{a+1}=d_{b+1}$, not full propagation.

(c) **Empirically** (corrected naive $O(N^2)$ gcd-greedy, cross-checked bit-exact vs `/tmp/round-6/mt_greedy.py`; $N>2T$ per case), the minimal forward-deterministic window-length $k_*$ for the set-to-set map and the realized state count at $k_*$ satisfy $k_*\le T$ and realized $\approx T$:

| $a_1$ | $M_1$ | $T$ | $k_*$ (set-to-set) | realized states @ $k_*$ | realized$/T$ |
|---|---|---|---|---|---|
| 15 | 15 | 8 | 1 | 10 | 1.25 |
| 77 | 77 | 18 | 1 | 21 | 1.17 |
| 375 | 15 | 852 | 100 | 858 | 1.01 |

($k_*$ is finite in every case but tracks $T$ roughly linearly; the realized state count at $k_*$ is $\approx T$.) This is the round-4 `increment-window-automaton` / `T-unbounded-in-M_1` fence signature ("realized window states $\approx T$, unbounded in $M_1$"), **extended to the set-valued $D_n$-window**: although $|D_n|\ge2$ almost everywhere (certified `D_n-slack-obstruction`) makes the $D_n$-window a richer PER-STEP symbol than the single-valued $d_n$-window, the orbit visits $\approx T$ distinct $D$-configurations — the per-step richness is exactly offset by greater orbit-wide variety. The slack does NOT translate into a smaller realized state set.

(d) **Circularity (structural).** In any periodic regime with period $T$, $D_{n+T}=D_n$ (by periodicity of $a$ and the constraint structure), hence $\sigma_{n+T}=\sigma_n$, so the set-to-set forward map is single-valued at every $k\ge T$. Therefore $k_*\le T$ always in the periodic regime, and "finiteness of $k_*$" is equivalent to "finiteness of $T$" (eventual periodicity). A non-circular proof would require a LOCAL structural bound on $k_*$ independent of $T$; the linear $k_*\approx cT$ tracking is empirical evidence that no such local-only bound exists.

## Fence-conclusion

The $D_n$-window pigeonhole route to periodicity — and any variant that tests "forward-determinism" only via the increment-projection $\sigma_n\mapsto d_{n+1}=\min D_n$ — is fenced: the increment-projection is a tautology (proves nothing), and the set-to-set map (the one actually needed) collapses to the round-4 `increment-window-automaton` / `T-unbounded-in-M_1` fence (realized $\approx T$, extended to set-valued windows) plus the $k_*\le T$ circularity. Future "$D_n$-window forward-deterministic at small $k$" claims MUST be tested on the set-to-set map, not the min-projection.

## Proof

(a) $d_{n+1}=\min D_n$ by `linchpin-and-gap-bound` (gap bound $d_{n+1}\le M_1$) + `D_n-slack-obstruction` Step 1 (greedy rule = smallest admissible increment). Since $D_n\subseteq\sigma_n$ (for $k\ge1$), $d_{n+1}$ is a function of $\sigma_n$; hence $\sigma_n=\sigma_{n'}\Rightarrow d_{n+1}=d_{n'+1}$ trivially. (b) `aimo-0907-coincidence-criterion` part A requires a single-valued map $F$ on the state with $\alpha(n+1)=F(\alpha(n))$; for $\alpha=\sigma$ this is the set-to-set map $F(\sigma_n)=\sigma_{n+1}$. A self-coincidence $\sigma_a=\sigma_b$ propagates to $\sigma_{a+k}=\sigma_{b+k}$ (all $k\ge0$) ONLY through single-valuedness of $F$; the increment-projection (a) gives only the single step $d_{a+1}=d_{b+1}$, not full propagation. (c) Computational table (reviewer-reproduced bit-exact; hand-verified $D_0=\{3,5,6,9,10,12,15\}$ for $a_1=15$, size 7, matching `D_n-slack-obstruction`). (d) Periodicity $a_{n+T}=a_n+L$ implies $a_{n+T}+d=a_n+d+L$ for each $d$, and the constraint set $\mathcal F_{n+T}$ stabilizes to the periodic admissible structure (every term lies in $\mathcal B_\infty$ by `every-term-in-binfinity`; the stabilized admissible set is $L$-periodic by `distinct-supports-stabilize`'s corollary conditional on Gap A — which the periodic regime presupposes). Hence $D_{n+T}=D_n$ and $\sigma_{n+T}=\sigma_n$, forcing single-valuedness of the forward map at $k\ge T$. $\square$

## Tools / status

`linchpin-and-gap-bound`, `D_n-slack-obstruction`, `aimo-0907-coincidence-criterion`, `every-term-in-binfinity`, `distinct-supports-stabilize`. Reviewer-certified (round 7). This fence EXTENDS the round-4 `increment-window-automaton` / round-5 `T-unbounded-in-M_1` fence from single-valued ($d_n$) windows to SET-VALUED ($D_n$) windows, and records the tautology-trap (the specific mis-testing error that produced the round-7 false-positive).
