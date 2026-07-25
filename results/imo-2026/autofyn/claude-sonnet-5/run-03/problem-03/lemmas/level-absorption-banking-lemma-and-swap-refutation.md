# Certified (round 10): B''-Banking Lemma (Lemma M); Candidate Swap Lemma
# refuted (negative result, recorded to rule out a family of future attempts)

Certified from `approaches/greedy-reduction-geometric.md` (round 10, Section 14).

## Lemma M (B''-Banking Lemma)

**Setting (Level-Absorption, Subcase (b) of Theorem 7'$(m,k;L)$'s inductive
step).** $B''=\{b_3,\dots,b_k\}$ has the Dominance-Chain property (Theorem 5,
`lemmas/dominant-chain-theorem-and-prefix-run-decomposition.md`) at level
$m-2$, with $\mathrm{sum}(B'')\le2^{m-2}$ (itself a consequence of $B'=\{b_2\}
\cup B''$ having the property at level $m-1$ with $\mathrm{sum}(B')\le2^{m-1}$
and $b_2\ge2^{m-2}$). $S''=\{2^{m-2}\}\cup S'''$ is a refinement of $\Gamma_{m-2}$
with the top $k-1$ levels unsplit, so $S'''$ refines $\Gamma_{m-3}$ with the
top $k-2$ levels unsplit.

**Statement.** $\mathrm{OddSum}(B''\cup S''')\ge\mathrm{sum}(B'')$.

**Proof.** Direct instance of the already-certified general **Theorem 7**
(Joint Dominance-Chain Closure, top-levels-clear;
`approaches/greedy-reduction-geometric.md`, Section 9.2, proved and used
repeatedly within that same file since round 5) applied at parameters
$(m',k'):=(m-2,k-2)$: $B''$ plays the role of Theorem 7's dominance chain at
level $m'$, $S'''$ plays the role of its top-$k'$-levels-unsplit refinement of
$\Gamma_{m'-1}=\Gamma_{m-3}$. All of Theorem 7's hypotheses are met exactly
($0\le k'\le m'$ inherited from $k\le m$ at the outer level; the Dominance-Chain
property and sum cap on $B''$; the unsplit-top-levels shape of $S'''$), giving
the claim directly.

**Correction to the round-10 outliner's citation.** The outliner proposed citing
Theorem 7a (the $k'=1$ base case of Theorem 7) for this step; Theorem 7a is
insufficient once $B''$ has $\ge2$ elements ($k\ge4$). The correct, fully
general tool is Theorem 7 itself. (At $k=2$, $B''=\varnothing$, the lemma is
vacuous via Theorem 7's own $k'=0$ base case; at $k=3$, $B''$ is a singleton and
Theorem 7's $k'=1$ inductive step reduces to exactly Theorem 7a, so the
outliner's citation was correct only in that one sub-case.)

**Reviewer verification.** Traced Theorem 7's hypotheses against Lemma M's
instantiation line by line; every hypothesis is met exactly as claimed, with no
gap. Theorem 7 itself is part of this same approach's own already-established
content (proved in round 5, used repeatedly since), not a borrowed crux
citation.

## Candidate Swap Lemma — refuted (negative result)

**Statement tested.** "Let $Q$ be any finite multiset of positive reals, $b>0$,
$P$ a finite multiset of positive reals with $\mathrm{sum}(P)\ge b$ and
$\max(P)<b$. Then $\mathrm{OddSum}(Q\cup P)\ge\mathrm{OddSum}(Q\cup\{b\})$."

**Refutation.** False. Counterexample (reviewer-verified by hand): $Q=
\varnothing$, $b=10$, $P=\{6,6\}$. Hypotheses hold ($\mathrm{sum}(P)=12\ge10$,
$\max(P)=6<10$), but $\mathrm{OddSum}(P)=6$ (only the top-ranked element of a
$2$-element multiset counts toward OddSum) while $\mathrm{OddSum}(\{b\})=10$;
$6<10$, violating the claim. The approach file additionally reports a $\sim36\%$
violation rate over $12{,}598$ randomized exact-`Fraction` trials.

**Why this is worth recording.** This rules out, as a class, any future attempt
to close Level-Absorption (or a similarly-shaped "split value $b$, still beat
the unsplit baseline" claim) via a structure-agnostic swap/replacement bound
depending only on $b,\max(P),\mathrm{sum}(P)$ and ignoring the background
multiset $Q$'s actual shape. Complements the round-9 finding that ruled out
degradation bounds depending only on $(g,q_1)$ — together these close off two
distinct natural "prove an abstract bound, then combine" attempts at
Level-Absorption.

## Scope

Level-Absorption itself remains open. This certifies only: (1) Lemma M, a
genuine positive fact, reusable for banking a Dominance-Chain sub-block's
contribution independently of an outer/parallel structure; (2) the Candidate
Swap Lemma's refutation, a negative result to prevent future rounds from
re-attempting this specific closure mechanism.
