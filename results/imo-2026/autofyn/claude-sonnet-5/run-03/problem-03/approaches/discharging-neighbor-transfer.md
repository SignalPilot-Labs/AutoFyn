## Status
partial

## Approaches tried

- **Round 15 (first build).** Mandatory cheap-kill executed exactly as
  dispatched: hand-derive (not guess) a rank-shift-based charge-transfer
  rule for a single cut, from the algebra of two structurally different
  worked examples (top-split and middle-split of the geometric partition
  $(8,4,2,1)/15$), in exact rational arithmetic. Outcome: **the cheap-kill
  passes** — a single, uniform, exact identity (the *Single-Cut Rank-Shift
  Identity*, below) reproduces the change in $\sum_i\sigma_im_i$ on both
  examples with zero residual. This is a genuine escalation past three
  previously-falsified fixed-formula attempts (Cut-Reallocation Exchange
  Lemma, per-cut-additive layer-cake, this round's own falsified
  $w(v,s)$), which never produced an exact identity at all. **However**,
  the round-15 write-up mislabeled the identity's quantity: it called
  $\sum_i\sigma_im_i$ ("$\sigma_i=(-1)^{i+1}$") "$\mathrm{OddSum}$", but
  this sum is literally the definition of $\mathrm{AltSum}$ (the certified
  Lemma AS, `lemmas/altsum-reformulation-and-single-insertion.md`, defines
  $\mathrm{AltSum}(X):=x_1-x_2+x_3-\cdots$, exactly this alternating sum);
  the true game quantity $\mathrm{OddSum}$ (sum of elements at odd rank
  only, no alternating signs — certified as the first-mover's exact value
  in `greedy-optimality-oddsum.md`) is a *different* number. Flagged by
  the round-15 reviewer, confirmed by an independent round-16 explorer
  (fresh exact-`Fraction` script, 60,000+ random single-split trials
  across generic and tie-heavy value pools, zero mismatches once the
  corollary below is used) as a pure labeling error, not an algebra error:
  the identity's derivation and both worked numerical checks are correct
  *as statements about $\mathrm{AltSum}$*.

- **Round 16 (this build, final for this approach).** Two tasks executed.
  **(1) Correction and full write-up.** Relabeled the Single-Cut
  Rank-Shift Identity's target quantity as $\mathrm{AltSum}$ throughout
  (no change to any line of algebra — the proof was already a valid proof
  of an $\mathrm{AltSum}$ statement), and added a new, fully proved
  **OddSum Corollary** deriving the true-game-quantity consequence,
  $\Delta\mathrm{OddSum}=\Delta\mathrm{AltSum}/2$, from the already-certified
  Lemma AS plus the elementary observation that a single cut conserves
  total mass ($v_1+v_2=m_j\Rightarrow\mathrm{sum}(L')=\mathrm{sum}(L)$).
  This closes the round-15 gap completely: the identity is now correctly
  stated, fully proved, and re-verified against both worked examples using
  the *true* $\mathrm{OddSum}$ (not the mislabeled quantity), matching the
  independent explorer's numbers exactly ($\Delta\mathrm{OddSum}=-1$ and
  $0$ on the two examples, both equal to $\Delta\mathrm{AltSum}/2$). **(2)
  Honest re-assessment of whether the fix unlocks new leverage on either
  open gap.** It does not, and this was checked directly (not assumed):
  the $\mathrm{OddSum}\leftrightarrow\mathrm{AltSum}$ relation is a global
  affine rescaling under fixed total mass ($\mathrm{OddSum}=(\mathrm{sum}+
  \mathrm{AltSum})/2$, $\mathrm{sum}$ normalized to $1$), so it changes no
  boundedness property of any term in the identity and transforms the
  target inequality into an affinely equivalent one
  ($\mathrm{OddSum}(\text{final})\ge c(n)\iff\mathrm{AltSum}(\text{final})
  \ge2c(n)-1$). The obstruction diagnosed in round 15 — the identity's
  Region-C suffix term has magnitude not bounded by anything local to the
  cut, so no per-cut charge budget can bound $\sum_s\Delta_s$ over a
  sequence of cuts, and the only route that could absorb it (recursing
  into the suffix) reduces to exactly the recursion `self-similar-
  induction-on-n` already works with (its `GT(m)`, open at $m\ge4$) —
  survives the relabeling and halving unchanged, term for term. This
  approach is therefore recommended for retirement as an independent line
  toward either open gap of the whole problem (see "Current best" and the
  closing recommendation below), while its one reusable, fully-proved
  positive result (the corrected AltSum identity + OddSum corollary) is
  proposed for certification.

## Current best

**Fully proved this round: the corrected Single-Cut Rank-Shift Identity
(stated for $\mathrm{AltSum}$, its native quantity) together with a new
OddSum Corollary** (see the full write-up below). This supersedes the
round-15 version, which stated the same proof under the wrong name.

**Open gap (unchanged in substance from round 15, now checked twice, not
just carried forward): the connecting step.** Telescoping the identity
over a sequence of $\le n$ cuts gives an exact tautology for the game's
final $\mathrm{OddSum}$ (or, equivalently by the affine relation,
$\mathrm{AltSum}$), but bounding the telescoped sum $\sum_s\Delta_s$
requires controlling each step's Region-C suffix term, whose magnitude is
not bounded by anything local to the cut. The only route that could
absorb it — recursing into the suffix as a sub-instance of the same
identity — produces exactly the peel-and-recurse recursion that
`self-similar-induction-on-n` already formalizes (its `GT(m)`, currently
open for $m\ge4$, narrowed to a width-1 window as of round 15), with
strictly less supporting machinery built up here (no analogue of that
approach's Theorem 7, AltSum Corollary in its own sense, or Growth
Lemma). **This has now been checked twice** — once at the (mislabeled)
$\mathrm{AltSum}$-formula level in round 15, and again this round after
the label fix, confirming the affine rescaling changes nothing about the
obstruction's shape. Recorded as an explicit, honest gap, not a forced
closure: *"bound $\sum_k\Delta_k$ over a full sequence of $\le n$ splits
using only the Single-Cut Rank-Shift Identity, without importing the
peeling induction already used by `self-similar-induction-on-n`."* No
future round should attempt to close this gap under this approach's name;
see the retirement recommendation below.

---

### The Single-Cut Rank-Shift Identity (AltSum form — corrected label)

**Setup.** Let $L=(m_1>m_2>\cdots>m_N)$ be a sorted-descending list of
positive reals, generic case (all values distinct); ties are handled
afterward via the certified Tie-Neutrality Lemma
(`tie-neutrality-and-first-mover-half.md`). Write $\sigma_i=(-1)^{i+1}$
for the rank-$i$ sign, so by definition
$$\mathrm{AltSum}(L):=\sum_i\sigma_im_i=m_1-m_2+m_3-\cdots$$
(this is exactly the $\mathrm{AltSum}$ of the certified Lemma AS,
`lemmas/altsum-reformulation-and-single-insertion.md`: *not*
$\mathrm{OddSum}$, which is $\sum_{i\text{ odd}}m_i$ with no signs). Lemma
AS states, for any finite multiset $X$ of positive reals,
$$\mathrm{OddSum}(X)=\tfrac12\bigl(\mathrm{sum}(X)+\mathrm{AltSum}(X)\bigr).\tag{AS}$$

Fix $j\in\{1,\dots,N\}$ and split $m_j$ into two positive fragments
$v_1\ge v_2>0$ with $v_1+v_2=m_j$ (so $v_1<m_j$ since $v_2>0$). Let $L'$
be the sorted-descending list obtained from $L$ by deleting $m_j$ and
inserting $v_1,v_2$ (a single legal cut of the piece at rank $j$).

**Definition (region counts).** Let
$$t_1=\#\{i>j: m_i>v_1\},\qquad t_2=\#\{i>j: m_i>v_2\}.$$
Since $v_1\ge v_2$, $0\le t_1\le t_2\le N-j$. Partition $\{j+1,\dots,N\}$
into three consecutive blocks:
$$A=(j,\,j+t_1],\qquad B=(j+t_1,\,j+t_2],\qquad C=(j+t_2,\,N].$$

**Claim 1 (rank placement).** $v_1$ lands at rank $p_1=j+t_1$ in $L'$, and
$v_2$ lands at rank $p_2=j+t_2+1$ in $L'$.

*Proof.* $m_1,\dots,m_{j-1}>m_j>v_1\ge v_2$, so all $j-1$ elements above
rank $j$ exceed both fragments. Among elements originally below rank $j$,
exactly $t_1$ exceed $v_1$ and exactly $t_2\,(\ge t_1)$ exceed $v_2$; and
$v_1>v_2$ (generic case; $v_1=v_2$ is handled by Tie-Neutrality). The
number of elements of $L\setminus\{m_j\}$ exceeding $v_1$ is
$(j-1)+t_1$, so $v_1$'s rank in $L'$ is $(j-1)+t_1+1=j+t_1=p_1$. The
number of elements of $L\setminus\{m_j\}$ exceeding $v_2$ is $(j-1)+t_2$,
and $v_1$ also exceeds $v_2$, so the number of elements of
$L'\setminus\{v_2\}$ exceeding $v_2$ is $(j-1)+t_2+1$, giving $v_2$ rank
$p_2=(j-1)+t_2+2=j+t_2+1$. $\blacksquare$

**Claim 2 (sign changes of untouched elements).** For $i\ne j$:
- $i<j$: rank in $L'$ is still $i$; sign unchanged, $\sigma_i$.
- $i\in A$ ($j<i\le j+t_1$): new rank $i-1$; sign flips to $-\sigma_i$.
- $i\in B$ ($j+t_1<i\le j+t_2$): new rank $i$; sign unchanged, $\sigma_i$.
- $i\in C$ ($i>j+t_2$): new rank $i+1$; sign flips to $-\sigma_i$.

*Proof.* Removing $m_j$ shifts every element originally below rank $j$ up
by one ($i\mapsto i-1$ for $i>j$) before either insertion. Inserting
$v_1$ at $p_1=j+t_1$ pushes down (by one) every element that, after the
removal-shift, is ranked at or below $p_1$ among $L\setminus\{m_j\}$ —
equivalently every $m_i$, $i>j$, with $m_i\le v_1$, i.e. every $i>j+t_1$.
Inserting $v_2$ likewise pushes down every $m_i$, $i>j$, with $m_i\le
v_2$, i.e. every $i>j+t_2$. So: region $A$ (pushed by neither insertion)
has net shift $-1$; region $B$ (pushed by $v_1$'s insertion only) has net
shift $-1+1=0$; region $C$ (pushed by both) has net shift $-1+2=+1$. An
odd net shift ($\pm1$) flips $\sigma$; a shift of $0$ preserves it.
$\blacksquare$

**Theorem (Single-Cut Rank-Shift Identity, AltSum form).** With notation
as above,
$$
\Delta_{\mathrm{Alt}}:=\mathrm{AltSum}(L')-\mathrm{AltSum}(L)
= \sigma_{p_1}v_1+\sigma_{p_2}v_2-\sigma_jm_j
\;-\;2\sum_{i\in A}\sigma_im_i\;-\;2\sum_{i\in C}\sigma_im_i.
$$

*Proof.* Compare $\mathrm{AltSum}(L')=\sum_{\text{ranks of }L'}
\sigma_{(\cdot)}(\text{value})$ term by term against $\mathrm{AltSum}(L)$.
Elements with $i<j$ contribute the same signed value $\sigma_im_i$ to
both sums (Claim 2), so they cancel in $\Delta_{\mathrm{Alt}}$. Region $B$
elements also keep the same sign (Claim 2), so they cancel too. $m_j$
contributes $\sigma_jm_j$ to $\mathrm{AltSum}(L)$ and is absent from $L'$:
net $-\sigma_jm_j$. Region $A$ and $C$ elements flip sign (Claim 2), so
each contributes its $L'$-signed value minus its $L$-signed value
$=-\sigma_im_i-\sigma_im_i=-2\sigma_im_i$. Finally $v_1,v_2$ are new,
contributing $\sigma_{p_1}v_1+\sigma_{p_2}v_2$ (Claim 1) to
$\mathrm{AltSum}(L')$ only, with no counterpart in $L$. Summing every
contribution gives the stated formula. $\blacksquare$

### The OddSum Corollary

**Corollary (true-OddSum consequence of one cut).** With notation as
above, let $\Delta_{\mathrm{Odd}}:=\mathrm{OddSum}(L')-\mathrm{OddSum}(L)$
(the actual first-mover game quantity, $\mathrm{OddSum}(X)=\sum_{i\text{
odd}}x_i$, no signs). Then
$$
\Delta_{\mathrm{Odd}}=\frac{\Delta_{\mathrm{Alt}}}{2}
=\frac12\Bigl(\sigma_{p_1}v_1+\sigma_{p_2}v_2-\sigma_jm_j
-2\sum_{i\in A}\sigma_im_i-2\sum_{i\in C}\sigma_im_i\Bigr).
$$

*Proof.* A single cut conserves total mass: $L'$ is obtained from $L$ by
deleting $m_j$ and inserting $v_1,v_2$ with $v_1+v_2=m_j$, so
$\mathrm{sum}(L')=\mathrm{sum}(L)-m_j+v_1+v_2=\mathrm{sum}(L)$. Apply
Lemma AS (identity (AS) above) to both $L$ and $L'$:
$$\mathrm{OddSum}(L)=\tfrac12\bigl(\mathrm{sum}(L)+\mathrm{AltSum}(L)\bigr),
\qquad
\mathrm{OddSum}(L')=\tfrac12\bigl(\mathrm{sum}(L')+\mathrm{AltSum}(L')\bigr).$$
Subtracting, and using $\mathrm{sum}(L')=\mathrm{sum}(L)$ so the
$\mathrm{sum}$-terms cancel:
$$\Delta_{\mathrm{Odd}}=\mathrm{OddSum}(L')-\mathrm{OddSum}(L)
=\tfrac12\bigl(\mathrm{AltSum}(L')-\mathrm{AltSum}(L)\bigr)
=\tfrac12\Delta_{\mathrm{Alt}}.$$
Substituting the Theorem's formula for $\Delta_{\mathrm{Alt}}$ gives the
stated expression. $\blacksquare$

Note this Corollary needs no genericity/tie hypothesis beyond what the
Theorem itself needs to define $\Delta_{\mathrm{Alt}}$ correctly (Lemma
AS holds for every finite multiset, ties or not); once
$\Delta_{\mathrm{Alt}}$ is computed correctly (generic case above, or the
tie-robust convention below), halving gives $\Delta_{\mathrm{Odd}}$
unconditionally.

**Locality reading (unchanged by the relabeling).** Every term in both
the Theorem and the Corollary involves only the split piece $m_j$ and
pieces originally ranked at or below $j$ (regions $A,B,C\subset
\{j+1,\dots,N\}$; region $B$ contributes $0$ net). No piece ranked above
$j$ ever appears — a genuine locality/transfer-rule structure, not a
fixed formula per object, since which of $A,B,C$ a lower piece $m_i$
falls in depends on its relative order against $v_1,v_2$.

### Verification on the two worked examples (exact arithmetic, corrected labels)

**Example 1 (top-split).** $L=(8,4,2,1)$, $j=1$, split $m_1=8$ into
$v_1=24/5=4.8$, $v_2=16/5=3.2$.
- $t_1=0$ (since $4,2,1<4.8$); $t_2=1$ (only $m_2=4>3.2$).
- $A=\varnothing$, $B=\{2\}$, $C=\{3,4\}$; $p_1=1$ ($\sigma_{p_1}=+1$),
  $p_2=3$ ($\sigma_{p_2}=+1$).
- Direct computation: $L'=(4.8,4,3.2,2,1)$.
  $\mathrm{AltSum}(L')=4.8-4+3.2-2+1=3$; $\mathrm{AltSum}(L)=8-4+2-1=5$;
  so $\Delta_{\mathrm{Alt}}=-2$. Formula check:
  $\sigma_1v_1+\sigma_3v_2-\sigma_1\cdot8-2\sum_{i\in C}\sigma_im_i
  =4.8+3.2-8-2[(+1)(2)+(-1)(1)]=8-8-2(1)=-2$. **Matches.**
- **True OddSum:** $\mathrm{OddSum}(L)=m_1+m_3=8+2=10$ (check via Lemma
  AS: $(15+5)/2=10$ ✓). $\mathrm{OddSum}(L')=4.8+3.2+1=9$ (ranks 1,3,5;
  check: $(15+3)/2=9$ ✓). $\Delta_{\mathrm{Odd}}=9-10=-1$. Corollary
  check: $\Delta_{\mathrm{Alt}}/2=-2/2=-1$. **Matches.**

**Example 2 (middle-split).** Same $L=(8,4,2,1)$, $j=3$, split $m_3=2$
into $v_1=6/5=1.2$, $v_2=4/5=0.8$.
- $t_1=0$ (only $m_4=1<1.2$); $t_2=1$ ($m_4=1>0.8$).
- $A=\varnothing$, $B=\{4\}$, $C=\varnothing$; $p_1=3$ ($\sigma_{p_1}=+1$),
  $p_2=5$ ($\sigma_{p_2}=+1$).
- Direct computation: $L'=(8,4,1.2,1,0.8)$. $\mathrm{AltSum}(L')
  =8-4+1.2-1+0.8=5$; $\mathrm{AltSum}(L)=5$; $\Delta_{\mathrm{Alt}}=0$.
  Formula: $\sigma_3v_1+\sigma_5v_2-\sigma_3\cdot2-0-0=1.2+0.8-2=0$.
  **Matches.**
- **True OddSum:** $\mathrm{OddSum}(L)=8+2=10$. $\mathrm{OddSum}(L')=
  8+1.2+0.8=10$ (ranks 1,3,5). $\Delta_{\mathrm{Odd}}=0$. Corollary check:
  $\Delta_{\mathrm{Alt}}/2=0/2=0$. **Matches.**

Both examples — a top-split with nonzero $\Delta$ and a middle-split with
zero $\Delta$ — are reproduced exactly, for *both* the $\mathrm{AltSum}$
Theorem and the $\mathrm{OddSum}$ Corollary, by the single mechanism above
with zero residual, and (independently of this file) an explorer's
exact-`Fraction` script confirmed the Corollary on 60,000+ further random
single-split trials (generic values and tie-heavy values, $N$ up to 15),
zero mismatches.

**Tie handling.** If $v_1=v_2$, or a fragment ties some $m_i$, rank
placement is not pinned by strict inequality alone. By the certified
Tie-Neutrality Lemma (`tie-neutrality-and-first-mover-half.md`),
$\mathrm{OddSum}$ (and hence, by Lemma AS with $\mathrm{sum}$ fixed,
$\mathrm{AltSum}$) of a block of mutually tied elements depends only on
the block's starting parity and size, not on which physical element sits
at which internal rank — so the identity, computed under any fixed
tie-breaking convention (e.g. "new fragments rank just below any tied
original value"), gives the correct $\mathrm{AltSum}(L')$ (and, via the
Corollary, the correct $\mathrm{OddSum}(L')$) regardless of convention,
with $t_1,t_2$ redefined consistently on both sides under that
convention. This was independently stress-tested by the round-16
explorer on 20,000 tie-heavy trials (small value pool forcing repeated
values and $\sim30\%$ exactly-equal fragments), zero mismatches.

### The connecting step: honest diagnosis, unaffected by the correction

The outline's second stage asked for global conservation (summing the
identity over a sequence of cuts) to yield a bound on the game's final
$\mathrm{OddSum}$. Starting from Liu Bang's partition $p$, Xiang Yu
performs a sequence of at most $n$ single-piece splits — exactly one
application of the Corollary per step (matching the Reduction Lemma's
description of XY's refinement, `reduction-to-multiset-minimax.md`).
Telescoping over $k\le n$ splits gives
$$\mathrm{OddSum}(\text{final})=\mathrm{OddSum}(p)+\sum_{s=1}^k
\Delta_{\mathrm{Odd},s},$$
an exact tautology (both sides compute the same quantity two ways), not
yet a bound. To obtain the target inequality one needs to bound
$\max_{\text{XY}}\sum_s(-\Delta_{\mathrm{Odd},s})$ over XY's choices.

**Why the correction does not help here.** By the Corollary,
$\Delta_{\mathrm{Odd},s}=\Delta_{\mathrm{Alt},s}/2$ for every $s$, so
$\sum_s\Delta_{\mathrm{Odd},s}=\tfrac12\sum_s\Delta_{\mathrm{Alt},s}$: the
entire telescoped sum is rescaled by the *same fixed constant* $1/2$,
step by step. Consequently:
- Every boundedness (or unboundedness) statement about the sequence
  $(\Delta_{\mathrm{Alt},s})_s$ transfers unchanged in kind to
  $(\Delta_{\mathrm{Odd},s})_s$ under multiplication by $1/2$. In
  particular, the round-15 obstruction — the dominant Region-C term
  $-2\sum_{i\in C_s}\sigma_im_i^{(s)}$ is a suffix alternating sum over
  *all* pieces currently below the cut, whose magnitude is not bounded by
  any quantity attached to the split itself (it can be as large as the
  entire untouched tail) — is exactly as unbounded after halving: a
  quantity "as large as the whole tail" divided by $2$ is still "as large
  as the whole tail," up to the same constant factor, so no fixed
  per-cut charge budget becomes available where none existed before.
- The target inequality itself transforms affinely and equivalently:
  proving $\mathrm{OddSum}(\text{final})\ge c(n)$ (normalizing
  $\mathrm{sum}=1$) is, by Lemma AS, *literally the same statement* as
  proving $\mathrm{AltSum}(\text{final})\ge2c(n)-1$ — so there is no
  hidden translation gap the mislabeling could have concealed: the
  connecting-step analysis (peel the top piece, bound the residual
  multiset's alternating/odd sum, recurse) examines the same recursion
  whether the working quantity is called $\mathrm{OddSum}$ or
  $\mathrm{AltSum}$, since Lemma AS makes the two interchangeable for
  exactly this "is there a per-cut budget" question.
- The only route that could absorb the Region-C term — treating it
  recursively as (up to sign bookkeeping) the $\mathrm{AltSum}$ of the
  sub-multiset below the cut, and applying the identity again inside that
  sub-multiset — is precisely a peel-and-recurse induction on shrinking
  residual multisets, i.e. exactly the structure `self-similar-
  induction-on-n` already formalizes with its `GT(m)` case analysis
  (currently open at $m\ge4$, narrowed to a width-1 window as of round
  15). Re-examining Example 1's own Region-C recursion above under this
  lens confirms the shape matches: "peel the max, bound the residual
  multiset's alternating/odd sum" is exactly `GT(m)`'s own recursive
  step, with none of that approach's supporting machinery (Theorem 7, the
  AltSum Corollary of that approach, the Growth Lemma) reproduced here.

**Gap (honest, explicit, unchanged by the correction).** No bound on
$\sum_s\Delta_{\mathrm{Odd},s}$ (equivalently $\sum_s\Delta_{\mathrm{Alt},s}$)
over a general sequence of $\le n$ splits has been established from the
Single-Cut Rank-Shift Identity/Corollary alone, and the natural way to
obtain one (recursing into Region C) reduces to the already-open $GT(m)$,
$m\ge4$ obstruction rather than bypassing it. This is now confirmed at
*both* the (mislabeled) $\mathrm{AltSum}$-formula level (round 15) and,
independently, after the label fix and under the $\mathrm{OddSum}$
Corollary (round 16) — the affine rescaling genuinely changes nothing
about this obstruction's shape or severity.

### Recommendation: retire this approach as an independent line

Per the round-16 dispatch, this is a final build for this approach. The
approach has produced one genuine, fully-proved, reusable piece of
mathematics (the corrected identity + corollary below), but two
consecutive rounds — under two different, correct labelings of the same
algebra — confirm it supplies **no independent leverage** on either open
gap of the whole problem. The connecting step it produces is, term for
term, the same recursion `self-similar-induction-on-n` already works with
using strictly more developed machinery. **Recommendation:** do not
dispatch another builder round on this approach chasing the connecting
step; retire `discharging-neighbor-transfer` as a distinct line toward
the problem's open gaps. Any future work on "bound the Region-C suffix
term over a sequence of cuts" should be filed as a contribution to
`self-similar-induction-on-n`'s `GT(m)` directly, not as a revival of
this file. (One narrow, unexplored opening was flagged by this round's
scouting explorer but not pursued: whether the identity's explicit
region-$A/B/C$ decomposition gives a *cleaner restatement* of `GT(m)`'s
open sub-case — a possible simplification of an existing approach's
machinery, not a new independent route, and out of scope for this file
going forward.)

## Promotable lemmas

**Single-Cut Rank-Shift Identity (AltSum form) and OddSum Corollary**
(both stated and proved in full above). The Theorem is a clean, general,
closed-form expression for $\Delta\mathrm{AltSum}$ under one legal split
of one existing element of a sorted list, with an explicit rank-region
decomposition ($A$/$C$ flip sign, contributing $-2\sigma_im_i$ each; $B$
is unaffected). The Corollary derives the corresponding exact
$\Delta\mathrm{OddSum}=\Delta\mathrm{AltSum}/2$ from the already-certified
Lemma AS (`lemmas/altsum-reformulation-and-single-insertion.md`) plus
mass conservation, in two lines. Both are verified exactly on two
structurally different worked examples (top-split, $\Delta\ne0$;
middle-split, $\Delta=0$) and independently stress-tested by a round-16
explorer on 60,000+ exact-`Fraction` random trials (generic and
tie-heavy value pools, $N$ up to 15), zero mismatches. This strictly
generalizes the existing insertion-only identities already certified
(`suffix-match-insertion-lemma.md`,
`altsum-reformulation-and-single-insertion.md`'s own Single-Insertion
Lemma, which handle inserting brand-new mass at a chosen rank) to an
arbitrary single split of an arbitrary existing element, with both the
$\mathrm{AltSum}$ and true-$\mathrm{OddSum}$ consequences stated
correctly. Proposed for certification into `lemmas/` (not
self-certified, per protocol): any future approach needing the exact
effect of one cut on $\mathrm{OddSum}$ or $\mathrm{AltSum}$ can cite it
directly instead of re-deriving the region-$A/B/C$ bookkeeping from
scratch.
