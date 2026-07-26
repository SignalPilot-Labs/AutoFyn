# Build report — crude-reduced-type (round 2)

## What I built
A second complete **conditional-on-crux** proof of IMO 2026 P6, mirroring `essential-monovariant`'s certified Theorem but at the cruder threshold $Q=\{p:p\le a_1\}$ (vs $Q_R=\{p\le\operatorname{rad}(a_1)\}$). File: `/home/agentuser/repo/results/imo-2026-06/approaches/crude-reduced-type.md`.

## Certified scaffold (Steps 1–6) — DONE
- **Lemma 1 (cheap anchor):** every $a_n$ has a prime divisor in $Q$ (for $n=1$ tautological; for $n\ge 2$ the greedy forces $\gcd(a_n,a_1)>1$, shared prime $p\mid a_1$ so $p\le a_1$). Full proof.
- **Reduced types in finite lattice:** $r(m)=P(m)\cap Q\in 2^Q\setminus\{\varnothing\}$, finite because $Q$ is finite.
- **Lemma 2 (stabilization):** $F_n$ nested-increasing, $H_n$ nested-decreasing on $2^Q$ ⟹ both eventually constant (monotone-on-finite, KB "Invariants & monovariants"). Fixed limits $F,H$; threshold $N_0=\max(N,N')$.
- **$V_0$ definition:** fixed finite set of residues mod $L_0=\prod_{p\le a_1}p$ whose $Q$-type is a transversal of $F$.

## Free-rider wall (Step 7) — marked [GAP], NOT attacked
- Stated explicitly as the inherited crux = Lemma 4 of `essential-monovariant` (with $Q\supseteq Q_R$ so the present statement is a priori weaker and is implied by that Lemma 4). One paragraph. Not closed. Honest about the flaw the skeleton buried: Step 6's "$a_{n+1}\bmod L_0\in V_0$" *requires* Lemma 4 to upgrade "shares a prime" to "shares a $Q$-prime" — without it the greedy's shared prime can be a free rider $>a_1$.

## Lift (Steps 8–10) — DONE, conditional on Lemma 4
- **Free-rider irrelevance (Claim):** $a_{n+1}=\min\{m>a_n:m\bmod L_0\in V_0\}$ for *every* $n\ge 1$ (two directions; uses Lemma 4 in the admissible-$\Rightarrow$-transversal direction). Index-free, so holds from $n=1$.
- **Deterministic walk $\varphi:V_0\to V_0$:** cyclic successor in natural order, wrapping by $+L_0$. $r_{n+1}=\varphi(r_n)$.
- **Cyclic permutation, no transient:** $\varphi$ is the cyclic-successor bijection on the finite ordered set $V_0=\{v_1<\dots<v_T\}$, single orbit of length $T=|V_0|$; bijective ⟹ purely periodic from $n=1$ (KB "Order of an element / eventual periodicity"; the bijection upgrades "eventual" to "from the start"). This defuses the round-1 reviewer's "for all $n$ / transient" flag.
- **Telescoping lift:** over one full period the residues traverse all of $V_0$ exactly once ⟹ exactly one wrapping transition; sum of value-gaps $=(v_2-v_1)+\dots+(v_1+L_0-v_T)=L_0$. Hence $a_{n+T}=a_n+L_0$ for every $n\ge 1$, with $T=|V_0|$, $L=L_0$.

## Status
`partial` — the crux Lemma 4 is inherited, not closed. Output is a second complete conditional-on-crux proof with the free-rider wall as the single marked [GAP]. All requested bounded-deliverable items (1)–(4) done; the stuck-recovery constraint (do not attack Step 7) was respected.
