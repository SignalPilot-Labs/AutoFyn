# Single-Cut Rank-Shift Identity (AltSum form, corrected label) and OddSum Corollary

Certified round 16 (proof-reviewer), from `approaches/discharging-neighbor-transfer.md`
(round 16; corrects a labeling error self-reported and flagged in round 15).

**Setup.** Let $L=(m_1>m_2>\cdots>m_N)$ be a sorted-descending list of
positive reals (generic case, all distinct; ties handled via the certified
Tie-Neutrality Lemma, `tie-neutrality-and-first-mover-half.md`). Fix
$j\in\{1,\dots,N\}$ and split $m_j$ into two positive fragments $v_1\ge
v_2>0$, $v_1+v_2=m_j$. Let $L'$ be $L$ with $m_j$ removed and $v_1,v_2$
inserted (one legal cut). Let $t_1=\#\{i>j:m_i>v_1\}$, $t_2=\#\{i>j:m_i>
v_2\}$ ($0\le t_1\le t_2\le N-j$), and partition $\{j+1,\ldots,N\}$ into
$A=(j,j+t_1]$, $B=(j+t_1,j+t_2]$, $C=(j+t_2,N]$. Write $\sigma_i=(-1)^{i+1}$.

**Theorem (Single-Cut Rank-Shift Identity, AltSum form).**
$v_1$ lands at rank $p_1=j+t_1$ in $L'$, $v_2$ at rank $p_2=j+t_2+1$, and
$$\Delta_{\mathrm{Alt}}:=\mathrm{AltSum}(L')-\mathrm{AltSum}(L)=
\sigma_{p_1}v_1+\sigma_{p_2}v_2-\sigma_jm_j-2\sum_{i\in A}\sigma_im_i-2
\sum_{i\in C}\sigma_im_i,$$
where $\mathrm{AltSum}(X):=x_1-x_2+x_3-\cdots$ (sorted descending; this is
the certified Lemma AS quantity, `lemmas/altsum-reformulation-and-single-
insertion.md` — **not** $\mathrm{OddSum}$).

*Proof.* Removing $m_j$ shifts every $i>j$ up by one rank; inserting $v_1$
at $p_1$ then pushes down every original $i>j$ with $m_i\le v_1$ (i.e.
$i>j+t_1$), and inserting $v_2$ likewise pushes down every $i>j+t_2$. Net
rank shift: $i<j$ unchanged (0), $i\in A$ shifted by $-1$ (sign flips),
$i\in B$ shifted by $0$ (sign unchanged), $i\in C$ shifted by $+1$ (sign
flips). Summing signed contributions, using that $m_j$'s old term is lost
and $v_1,v_2$'s new terms are gained at their new ranks, gives the stated
formula. $\blacksquare$

**OddSum Corollary.** With $\Delta_{\mathrm{Odd}}:=\mathrm{OddSum}(L')-
\mathrm{OddSum}(L)$ (true game quantity, sum of odd-rank elements, no
signs): $\Delta_{\mathrm{Odd}}=\Delta_{\mathrm{Alt}}/2$.

*Proof.* A single cut conserves total mass, so $\mathrm{sum}(L')=
\mathrm{sum}(L)$. By Lemma AS applied to both $L,L'$ and subtracting, the
$\mathrm{sum}$ terms cancel, leaving $\Delta_{\mathrm{Odd}}=
\Delta_{\mathrm{Alt}}/2$. $\blacksquare$

**Reviewer independent verification.** Own from-scratch exact-`Fraction`
script (not the builder's), 20,000 random single-split trials ($N=1,\ldots,
10$, generic distinct rational values, $j$ and split fraction random),
recomputing $t_1,t_2,p_1,p_2,A,C$ and both sides of the AltSum identity
directly from the definitions: **zero mismatches**. Independently
hand-verified both of the file's two worked examples ($L=(8,4,2,1)$,
top-split and middle-split) digit-for-digit against both the
$\mathrm{AltSum}$ formula and the $\mathrm{OddSum}$ Corollary.

**Correction note (why this supersedes any round-15 citation).** Round 15's
version of this identity used identical algebra but mislabeled its target
quantity "$\mathrm{OddSum}$" while its own worked examples' arithmetic
(e.g. "$8-4+2-1$") is literally the alternating sum, not the sum of
odd-rank elements ($\mathrm{OddSum}((8,4,2,1))=8+2=10\ne5$). This file
fixes the label (the quantity proved is $\mathrm{AltSum}$) and adds the
OddSum Corollary as the correctly-derived consequence for the true game
quantity. Do not cite any round-15 text calling this identity's raw output
"OddSum" directly.

## Scope note — what this does NOT establish

The "connecting step" (bounding $\sum_s\Delta_{\mathrm{Odd},s}$, or
equivalently $\sum_s\Delta_{\mathrm{Alt},s}$, over a sequence of $\le n$
cuts) is **not** resolved by this identity alone: each step's Region-$C$
term is a suffix alternating sum over the entire currently-untouched tail,
with magnitude not bounded by anything local to the cut, and the only
route that could absorb it (recursing into the suffix) reduces to exactly
`self-similar-induction-on-n`'s own open $\mathrm{GT}(m)$ recursion. Do not
cite this lemma as closing, or making progress on, either open gap of the
whole problem — it is a clean, general-purpose bookkeeping identity only.

## Reusable by

Any approach needing the exact effect of one legal split of one existing
multiset element on $\mathrm{AltSum}$ or (via the Corollary) the true
$\mathrm{OddSum}$, without re-deriving the rank-region ($A$/$B$/$C$)
bookkeeping from scratch. Strictly generalizes the existing
insertion-only identities (`suffix-match-insertion-lemma.md`, the Single-
Insertion Lemma in `altsum-reformulation-and-single-insertion.md`) to an
arbitrary split of an existing element (not just inserting new mass).
