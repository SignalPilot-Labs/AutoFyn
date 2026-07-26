# proof-builder — essential-monovariant (round 2)

## What I built
Approach file: `/home/agentuser/repo/results/imo-2026-06/approaches/essential-monovariant.md` (Status: **solved**).
Free partial lemma certified: `/home/agentuser/repo/results/imo-2026-06/lemmas/multiple-of-r-satisfies-lemma-4.md`.

### Headline: the descent CLOSED via the game-of-numbers equivalence

The Route-D stripped-auxiliary-transversal descent the outline-reviewer dispatched does not close via the *direct* port (greedy minimality as the "move" — the outline-reviewer correctly flagged the transversal-enlargement-vs-$x\le a_i$ wall). It **does** close via the **indirect port through the game-of-numbers equivalence**:

- aimo-0030 ("game of numbers", Italy TST) constructs, in its Comment 2, the increasing enumeration of all good numbers by the EXACT greedy rule of P6 (smallest $b>b_n$ coprime to none of the predecessors), with $b_0=k$.
- Setting $k=A=a_1$ identifies P6's sequence with the good numbers of the game with parameter $k=A$ (Theorem GC, proved in §6 via the good/bad dichotomy G1–G2 and "$k$ good" G3).
- aimo-0030's Claim 5 (any two good numbers share a SMALL prime $\le k$), proved by the stripping descent (Claim 4 + minimal counterexample on $b'$ + the game's "move" $x\to b^*$), transfers directly to P6: every pair of terms shares a prime $\le a_1$. This is **Lemma 4'** (§7).

The key realization: the "move" structure that P6 seemed to lack (and that blocked the direct greedy-minimality port) IS available through the game — the move $x\to b^*$ is a statement about the *game* (a coprime smaller good number, furnished by the bad $\Rightarrow$ exists-good-coprime-predecessor dichotomy G2), NOT a statement about greedy minimality. The game is an auxiliary construction (defined independently of P6), and the transfer to P6 is a theorem (Theorem GC). No circularity.

### Why this is "from scratch" (not a citation)
The instructions forbid citing a retrieved crux without re-proving. I re-derived, in full prose, every load-bearing step of aimo-0030's solution inside P6's writeup:
- Lemma G1 (good-via-only-bad-moves), G2 (bad-via-good-move), G2' (good $\Leftrightarrow$ no good coprime predecessor).
- Lemma G3 ($k$ good), G4 (any two good share a prime).
- Lemma G5 (stripping) — full proof with the $x<pk\le ak<aq\le b$ inequality derived.
- Lemma G6 (Claim 5, the crux) — full minimal-counterexample descent.
- Theorem GC (greedy = good) — full induction with two-case split.
- Lemma 4' (transfer) + the periodicity machinery (§8, round-1 conditional now discharged).

The aimo-0030 crux is a *hint adapted*; every step is re-proven.

### Floor deliverable (DONE FIRST)
Certified `lemmas/multiple-of-r-satisfies-lemma-4.md`: if $a_j$ is a multiple of $R=\operatorname{rad}(a_1)$, then $(a_i,a_j)$ shares a prime $\le R$ for every $i<j$. Mechanism: $a_j$ mult of $R$ $\Rightarrow$ every prime of $a_1$ divides $a_j$; Lemma 1 gives $a_i$ a prime $q\in P(a_1)\subseteq Q_R$; $q\mid R\mid a_j$ and $q\mid a_i$. (Subsumed by Lemma 4' but a clean standalone.)

### Did the descent close?
**Yes.** Lemma 4' is proved unconditionally; combined with the round-1 periodicity machinery (run with threshold $B=a_1$, giving $L=L_0=\prod_{p\le a_1}p$, $T=|V|$), the theorem is proved for every $n\ge 1$ (no transient — the residue walk $\varphi$ is a cyclic permutation on $V$).

### Crude vs. tight bound
The game gives the bound $\le a_1$ (Claim 5 uses "small" $=$ prime $\le k=a_1$), which is WEAKER than the round-1 target $\le\operatorname{rad}(a_1)$ when $a_1$ is not squarefree. This is fine: the periodicity machinery only needs finiteness of the threshold set, and $Q=\{p\le a_1\}$ is finite. The resulting $L=\prod_{p\le a_1}p$ is cruder than the true minimal $L$ (e.g. for $a_1=15$ the true period is $(T,L)=(8,30)$, matching aimo-0030 Comment 3; my machinery gives a larger valid $(T,L_0=30030)$). The problem only asks to PROVE existence of $T,L$, not to minimize. Verified computationally: $a_1=15$ gives true $(8,30)$; Lemma 4' (pairwise share prime $\le a_1$) holds for all tested $a_1\in\{4,6,9,10,12,15,16,25,35,77,105\}$, including non-squarefree.

### STUCK-RECOVERY compliance
Did NOT grind. Floor lemma written first (minutes). The ceiling insight (game equivalence) came from reading the aimo-0030 corpus entry carefully — the Comment 2 greedy construction IS P6's rule. Wrote the proof in one pass, fixed two rigor points (the Theorem GC two-case split; the "$x$ is bad" via Lemma G4 not G2'; the $\tau(a_{n+1})\ne\emptyset$ via Lemma 4' pairing). No loops.

### Promotable lemmas (for reviewer certification)
- **Lemma G6** (good numbers share a small prime $\le k$) — the crux, §5.
- **Theorem GC** (greedy = good numbers) — §6.
- **Lemma 4'** (P6 pairwise share prime $\le a_1$) — §7.
- **Lemma 2** (gap bound $\le\operatorname{rad}(a_1)$) — Appendix, round 1.
- **Lemma 3** (consecutive only-small) — Appendix.
- **multiple-of-$R$ lemma** — `lemmas/`, certified.

### Honest caveats
- The proof is GENUINE (every step re-derived, no citation-as-black-box), but it IS an adaptation of aimo-0030's solution. The reviewer should verify (a) the game equivalence (Theorem GC) is airtight, especially the "$M$ is good" two-case split and the "no good in $(g_n, M)$" argument; (b) Lemma G5's inequality $x<pk\le ak<aq\le b$; (c) Lemma G6's minimality well-ordering and the final contradiction $(b^*,b)$ having larger element $b<b'$.
- If the reviewer judges the aimo-0030 adaptation too close to a citation (rather than a from-scratch re-proof), the fallback is: keep Lemma 4' as a claim referencing the game, and revert Status to partial with the game-equivalence as the named gap. But I believe the full re-derivations in §2–§7 satisfy the "prove from scratch" rule.
