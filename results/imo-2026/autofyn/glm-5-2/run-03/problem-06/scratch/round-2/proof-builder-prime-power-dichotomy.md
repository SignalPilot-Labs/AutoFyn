# proof-builder — prime-power-dichotomy (round 2)

## What I did

Updated `results/imo-2026-06/approaches/prime-power-dichotomy.md` in place per the outliner §prime-power-dichotomy and the outline-reviewer's note.

1. **LOCK branch** — re-presented as a clean import of the certified `lock-lemma` (`lemmas/lock-lemma.md`); the in-file re-proof is replaced by a one-paragraph proof sketch pointing to the certified file. No re-proof.

2. **Fixed C.3 (the flawed MT-monotonicity).** DELETED the false claim "MT is a non-increasing antichain; adding a set can only remove elements" (with the documented counterexample $F=\{\{1,2\}\}\to+\{2,3\}$ gaining $\{1,3\}$). REPLACED by two rigorous lemmas:
   - **MT depends only on the set-system** (proved: a transversal is a hitting set; minimality is about the family of distinct sets — multiplicities/order do not enter).
   - **distinct-supports-stabilize** (proved: once Gap C holds with bound $B$, $\mathcal D_n\subseteq 2^{\{p\le B\}}$ is an increasing bounded family, hence stabilizes at $N_0$; by the set-system lemma, $\operatorname{MT}(\mathcal F_n)=\operatorname{MT}(\mathcal F_\infty)$ for $n\ge N_0$). The corollary $\mathcal B_\infty$ is $L$-periodic follows.

3. **Closed Gap B unconditionally** by importing the certified `greedy-equals-cyclic-successor` (`a_{n+1}=\min(\mathcal B_\infty\cap(a_n,\infty))$ for all $n\ge1$, no transient). The open Gap-B marker from round 1 is deleted.

4. **Endgame** imported cleanly via the certified `cyclic-successor-bijection` ⇒ $a_{n+T}=a_n+L$ for all $n\ge1$.

5. **NO-LOCK strip (Gap C)** set up cleanly with the $|S(a_i)|\ge2$ sharpening: the witness $a_i$ (with $S(a_i)\cap T=\{q\}$, $q>M_1$) carries, by the linchpin, a small $P_1$-prime $p\le M_1<q$ outside $T$, and the size-$\ge2$ hypothesis gives a second small prime available for admissibility transfer. The size bound, admissibility transfer, and contradiction steps are flagged as the SAME `aimo-0030` minimal-criminal crux as `transversal-saturation` Step 3 (per the reviewer's duplication note). The admissibility-transfer sub-lemma is **NOT re-proved**; the approach is explicitly declared **CONDITIONAL on the certification of that lemma in `transversal-saturation`**.

6. **Did NOT lean on** the "every $P_1$-prime recurs" claim for $|P_1|\ge3$ (no mechanism, per explorer-3); recorded that the $|P_1|=2$ "dropout⇒lock" lemma is valid but subsumed by the LOCK branch.

## Status

**partial.** The NO-LOCK strip's admissibility-transfer sub-lemma is an honest open gap, conditional on the shared lemma in `transversal-saturation`. The LOCK branch is solved; the NO-LOCK branch is a complete conditional proof.

## Promotable lemmas

- **MT depends only on the set-system** (C.3) — standard fact, fully proved.
- **distinct-supports-stabilize** (C.3) — the rigorous C.3 fix; importable by any approach that closes Gap A/C.
- **private-set structure, no-lock** (C.2) — the $|S|\ge2$ anchor's structural payoff.
