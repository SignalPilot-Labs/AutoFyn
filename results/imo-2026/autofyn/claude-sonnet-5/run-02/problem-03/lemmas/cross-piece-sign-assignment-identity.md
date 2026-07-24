## Cross-Piece Sign-Assignment Identity

**Statement.** Fix a marking $p_1,\dots,p_m>0$, $T=\sum p_i$, and a legal
Xiang Yu move: split a subset $I\subseteq\{1,\dots,m\}$ of pieces (piece
$i\in I$ into $c_i+1\ge2$ fragments summing to $p_i$, using $c_i\ge1$ cuts;
pieces $i\notin I$ untouched, i.e. a single "fragment" of value $p_i$),
using $\sum_{i\in I}c_i\le n$ cuts total. Let $M$ be the resulting final
multiset.

Apply the certified `odd-run-reduction-lemma` to $M$: pairing off (in any
order) any two elements of $M$ with exactly equal value, repeatedly, until
every surviving value is distinct, produces a reduced multiset $M'$ with
$A(M)=A(M')$ (an exact identity, independent of pairing order). Attribute
each surviving element of $M'$ to the original piece that produced it (a
well-defined ledger fact, since $M'$ is literally a sub-collection of $M$'s
elements with some cancelled in equal-valued pairs — regardless of which
piece "owned" each cancelled copy, the *ledger* of which surviving element
came from which piece is unambiguous). For each piece $i$, let
$G_i\subseteq M'$ be its surviving elements and $q_i:=\sum_{f\in G_i}f\in[0,p_i]$
("piece $i$'s surviving mass"; $q_i=p_i$ if none of piece $i$'s fragments
were cancelled, $q_i<p_i$ if some were, $q_i=0$ if all were).

**Hypothesis (monochromaticity).** Suppose that, in $M'$'s (now unique,
tie-free) sorted descending order, every element of $G_i$ occupies a rank
of one common parity $\varepsilon_i\in\{+1,-1\}$ (reading rank $r$'s parity
as $(-1)^{r+1}$: odd ranks $\to+1$, even ranks $\to-1$), for every $i$ with
$G_i\ne\varnothing$.

**Conclusion.**
$$A(M) = A(M') = \sum_{i=1}^m \varepsilon_i q_i,\qquad
\Phi(M) = \frac{T+\sum_{i=1}^m\varepsilon_iq_i}{2}$$
(the sum implicitly omitting terms with $q_i=0$, for which $\varepsilon_i$
is irrelevant).

## Proof

**Step 1 ($A(M)=A(M')$).** This is exactly the certified
`odd-run-reduction-lemma`, applied with no modification: $M'$ is obtained
from $M$ by, for each distinct value $v$ occurring with multiplicity
$\mu(v)$ in $M$, keeping one copy if $\mu(v)$ is odd and zero copies if
$\mu(v)$ is even — a purely value-based operation, entirely blind to which
original piece contributed which copy. The lemma's proof (repeated
adjacent-pair removal, or equivalently repeated `pair-cancellation-identity`)
shows $A(M)=A(M')$ unconditionally, for *any* finite multiset $M$; nothing
in that proof needs pieces or attribution, so it applies verbatim here,
before any piece-ledger bookkeeping is introduced.

**Step 2 (regroup $A(M')$ by piece).** Since $M'$ has all distinct values,
its descending sort is unique, so
$$A(M') = \sum_{r=1}^{|M'|} (-1)^{r+1} M'_{(r)}$$
is simply the definition of the alternating sum (the base case underlying
`integral-alternating-sum-formula` for a multiset with no repeated values).
The index set $\{1,\dots,|M'|\}$ of ranks is partitioned, by the piece
ledger, into the disjoint blocks $\{r: M'_{(r)}\in G_i\}_{i=1}^m$ (every
surviving element belongs to exactly one piece's ledger, and every piece's
ledger is a subset of $M'$'s elements — this is a literal partition of a
finite index set, so regrouping a finite sum by this partition is a
trivial, exact rearrangement, no convergence or ordering subtlety
involved). Hence
$$A(M') = \sum_{i=1}^m \sum_{r:\,M'_{(r)}\in G_i} (-1)^{r+1}M'_{(r)}.$$
By the monochromaticity hypothesis, every rank $r$ in the inner sum for a
fixed $i$ has the same sign $\varepsilon_i$, so
$$\sum_{r:\,M'_{(r)}\in G_i}(-1)^{r+1}M'_{(r)} = \varepsilon_i
\sum_{r:\,M'_{(r)}\in G_i}M'_{(r)} = \varepsilon_i\sum_{f\in G_i}f=\varepsilon_iq_i.$$
Summing over $i$ gives $A(M')=\sum_i\varepsilon_iq_i$. Combined with Step 1,
$A(M)=\sum_i\varepsilon_iq_i$, and $\Phi(M)=(T+A(M))/2$ gives the stated
formula. $\blacksquare$

## Relation to prior certified results (special cases, all consistent)

- **No ties at all ($M'=M$).** Then $q_i=p_i$ for every $i$ (nothing
  cancelled), recovering the "generic" form
  $A(M)=\sum_i\varepsilon_ip_i$ — this is the mechanism behind the round-15
  scout's $n=3$ flat-face witness (§ below).
- **`pair-cancellation-identity`/`bisect-top-k-lemma`.** Bisecting the top
  $k$ pieces into equal fragments $p_i/2,p_i/2$ is the special case where,
  for $i\le k$, piece $i$'s two fragments are *equal in value* and hence
  odd-run-reduce to $q_i=0$ (an even-multiplicity self-pair, contributing
  nothing) — consistent with, and now shown to be a corollary of, this
  identity (Bisect-Top-$k$ never needed the "same-parity, non-adjacent"
  freedom this identity exposes; it only ever used the $q_i=0$ corner).
- **Cross-piece ties (the $n=4$ pinned-tie witness, verified below).** If a
  fragment of piece $i$ coincides exactly in value with a fragment (or an
  untouched value) of a *different* piece $i'$, both cancel in the
  odd-run-reduction (an even-multiplicity pair spanning two pieces), so
  $q_i,q_{i'}$ are reduced accordingly — this is the mechanism `odd-run-
  reduction-lemma` supplies that a naive "assume no ties" statement would
  miss, and is exactly round 9's flagged-but-previously-unexecuted
  suggestion to reuse it on the upper-bound side.

## Verification

**General identity (with forced ties), fresh exact-`Fraction` script,**
`/tmp/round-15/verify_crosspiece2.py`: 20000 random constructions (random
markings $m=2,\dots,6$, random subsets split into 2 fragments with random
split points, ties forced in $\approx30\%$ of trials by copying a value
across pieces), of which 6989 satisfied the monochromaticity hypothesis;
**zero mismatches** between the predicted $\sum\varepsilon_iq_i$ and the
directly-computed $A(M)$ on every one of the 6989.

**Both round-14 near-tight case-(b2) witnesses, exact fractions:**

- **$n=3$ witness** $p=(4468,2591,2251,691)/10001$ (normalized exactly):
  explicit legal split ($p_1\to(f_1,f_2)$, $p_3\to(f_3,f_4)$, exact
  fractions in `/tmp/round-15/verify_witnesses3.py`) realizing sorted order
  $f_1>p_2>f_2>f_3>p_4>f_4$ — i.e. $I=\{1,3\}$, no ties, $\varepsilon_1=+1,
  \varepsilon_2=-1,\varepsilon_3=-1,\varepsilon_4=+1$. Predicted
  $\Phi=(T+p_1-p_2-p_3+p_4)/2=5159/10001$ **exactly equals** the direct
  computation on the constructed multiset, and $5159/10001\approx0.51585 <
  a_3T=8/15\approx0.53333$: **this specific witness is unconditionally
  closed** (a legal 2-cut Xiang Yu response beats the target exactly).
- **$n=4$ witness** $p=(2933,2514,2131,1338,1085)/10001$: explicit legal
  split (`/tmp/round-15/verify_witness_n4b.py`) — $p_1$ split into 3
  fragments, one exactly equal to $p_3$ (a genuine cross-piece tie) and the
  other two equal to each other (an ordinary same-piece pair); $p_2$ split
  into 2 fragments straddling $p_4,p_5$. Odd-run-reduction cancels both the
  $p_1$-fragment/$p_3$ tie ($q_1=q_3=$ their shared value cancels to net
  $0$ each once matched — more precisely the surviving ledger has $q_1=0$
  from that fragment plus $0$ from its self-paired pair, so $q_1=0$
  overall; $q_3=0$) and the same-piece pair ($q_1$ unaffected further,
  already $0$), leaving $G_2$ (both $p_2$ fragments, monochromatic
  $\varepsilon_2=+1$, $q_2=p_2$), $G_4=\{p_4\}$ ($\varepsilon_4=-1$),
  $G_5=\{p_5\}$ ($\varepsilon_5=-1$). Predicted $\Phi=(T+p_2-p_4-p_5)/2=
  5046/10001$ **exactly equals** the direct computation, and
  $5046/10001\approx0.50455<a_4T=16/31\approx0.51613$: **this witness too
  is unconditionally closed**.

Both witnesses — of the two *qualitatively different* vertex/face types the
round-15 scout identified (a flat no-tie face at $n=3$, a genuine pinned-tie
vertex at $n=4$) — are covered exactly by this single general identity,
confirming it strictly contains, and correctly specializes to, both known
vertex shapes, as the round-15 outline required.

## Certification note (proof-builder, round 15)

Proved directly from the already-certified `odd-run-reduction-lemma` (Step
1, no modification) and an elementary finite-sum regrouping (Step 2, no
further lemma needed — a partition of a finite index set). No case is
skipped: the statement is unconditional given its hypothesis
(monochromaticity of $M'$'s ranks per piece), which is a hypothesis to be
*checked* for each candidate construction, not assumed to always hold (see
`alternating-gap-cross-lemma.md` for the companion feasibility analysis of
when a useful monochromatic assignment is legally realizable). Verified
computationally as described above (20000 random trials for the general
identity, exact-fraction reconstruction of both named witnesses). Not yet
independently re-reviewed by the proof-reviewer as of this writing —
pending round-15 review.

**Origin:** `results/imo-2026-03/approaches/lp-duality-certificate.md`,
round 15, executing the round-15 outline's Task 1 (and round 9's originally
flagged, previously-unexecuted suggestion to reuse `odd-run-reduction-lemma`
for the upper-bound direction's evaluation half).
