# Lemma N (WLOG b2 = 2^(m-1)), and Theorem N (Case B ≡ TOP-ONLY(m-1) complementary regime, on the S'''-unsplit slice)

Certified round 11. Proved in `approaches/greedy-reduction-geometric.md`
(round 11, Section 15.1 and 15.3).

## Lemma N (WLOG $b_2=2^{m-1}$)

**Statement.** To prove the Level-Absorption Base Case ($k=2$) for every
$b_2\in[2^{m-2},2^{m-1}]$, it suffices to prove it for $b_2=2^{m-1}$ exactly
(with the hypothesis specialized to $\max(P)<2^{m-1}$, which is automatic
whenever $|P|\ge2$ — itself forced by the Base Case's own hypotheses, since
a single piece $\max(P)=2^{m-1}\ge b_2$ would contradict $\max(P)<b_2$).

**Proof.** Fix $b_2'\in[2^{m-2},2^{m-1}]$ and an instance $(P,S''')$
satisfying the Base Case's hypotheses at $b_2'$ ($\mathrm{sum}(P)=2^{m-1}$,
$\max(P)<b_2'$, $S'''$ a refinement of $\Gamma_{m-3}$, cut budget
$(|P|-1)+\mathrm{cuts}(S''')\le m-1$). None of these depend on $b_2'$ except
$\max(P)<b_2'$; since $b_2'\le2^{m-1}$, this implies $\max(P)<2^{m-1}$, so
$(P,S''')$ is also a valid instance at $b_2=2^{m-1}$. If the Base Case holds
there, $\mathrm{OddSum}(P\cup\{2^{m-2}\}\cup S''')\ge2^{m-1}\ge b_2'$
(the last step using $b_2'\le2^{m-1}$), exactly the conclusion needed at
$b_2'$. $\blacksquare$

## Theorem N (Case B $\equiv$ TOP-ONLY$(m-1)$, complementary regime, on the $S'''$-unsplit-full-budget slice)

**Statement.** Fix $m\ge3$, $m':=m-1$. In the sub-case of the Base Case
(with $b_2=2^{m-1}$, via Lemma N) where $S'''=\Gamma_{m-3}$ exactly (zero
cuts spent inside $S'''$, so the full budget $m-1$ is available for
splitting $P$, i.e. $|P|\le m=m'+1$), the target
$$\mathrm{OddSum}(P\cup\{2^{m-2}\}\cup S''')\ge2^{m-1}$$
is literally identical, term for term, to
$$\mathrm{OddSum}(P\cup\Gamma_{m'-1})\ge2^{m'}\qquad\text{(TOP-ONLY$(m')$)},$$
and Case B's hypothesis $\max(P)<2^{m-2}=2^{m'-1}$ is exactly the hypothesis
of TOP-ONLY$(m')$'s complementary (non-Dominance-Chain) regime.

**Proof.** $\{2^{m-2}\}\cup S'''=\{2^{m-2}\}\cup\Gamma_{m-3}=\Gamma_{m-2}
=\Gamma_{m'-1}$ by definition of $\Gamma$. So the left side is literally
$\mathrm{OddSum}(P\cup\Gamma_{m'-1})$, and $2^{m-1}=2^{m'}$ matches the right
side. $\mathrm{sum}(P)=2^{m-1}=2^{m'}$ (Base Case hypothesis), so $P$ is a
genuine partition of $2^{m'}$, and $|P|\le m'+1$ matches TOP-ONLY$(m')$'s own
admissible piece count. Finally $\max(P)<2^{m-2}=2^{m'-1}$ is verbatim the
complementary-regime hypothesis (negation of Dominance-Chain's
$a_1\ge2^{m'-1}$). $\blacksquare$

**Corollaries (immediate, no new proof).**
- Theorem 6 (Large-Violation-Depth closure, already certified,
  `lemmas/large-violation-depth-closure.md`) applies verbatim whenever
  $m-1\ge3$ and $\max(P)<2^{m-4}$, closing this sub-slice of Case B
  outright — vacuous until $m\ge9$ (pigeonhole, same argument as Theorem
  6's own scope note).
- For $2^{m-4}\le\max(P)<2^{m-2}$: this sub-slice coincides exactly with
  `self-similar-induction-on-n`'s own Branch-I.A-restricted window (still
  open there).

## Reviewer verification

Independently re-verified the exact stress-test counterexample cited as
motivation for Theorem N (Section 15.2), by a from-scratch exact-`Fraction`
script (not the builder's), at $m=4$:
$P=(327889/81977,\,203653/81977,\,97214/81977,\,27060/81977)$,
$\mathrm{sum}(P)=8$ exactly, $\max(P)=327889/81977<4$, and
$\mathrm{OddSum}(P\cup\{4,2,1\})-8=19/81977$ — matched the file's claimed
margin exactly, digit for digit. Also independently re-derived Lemma N's
monotonicity argument (elementary, no gap) and Theorem N's symbol-matching
identity $\{2^{m-2}\}\cup\Gamma_{m-3}=\Gamma_{m-2}$ and the piece-cap
arithmetic $|P|\le m=m'+1$, both confirmed correct.

## What this does and does not resolve

Theorem N is an exact equivalence on the $S'''$-unsplit-full-budget slice of
Case B only; the general Case B statement (allowing $S'''$ itself to be
split) is not covered and remains open, as does Case A (only a scope
diagnosis, not a proof, is recorded for it in Section 15.4). Level-Absorption
and Theorem 7'$(m,k;L)$'s inductive step remain open.
