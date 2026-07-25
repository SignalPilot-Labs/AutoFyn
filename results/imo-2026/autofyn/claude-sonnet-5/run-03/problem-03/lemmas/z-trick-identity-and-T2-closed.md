# Certified (round 3): the z-trick identity (Lemma Z) and T(2) fully closed (Theorem 1)

Certified from `approaches/self-similar-induction-on-n.md` (round 3).
Notation: $\Gamma_m=(2^m,\dots,1)$; $T(m,k)$: every refinement of $\Gamma_m$
using $\le k$ cuts has $\mathrm{OddSum}\ge2^m$; $T(m)$: $T(m,k)$ for all
$0\le k\le m$.

## Lemma Z (z-trick identity)

**Statement.** For any finite multiset $X$ of positive reals and
$z\ge\max(X)$: $\mathrm{EvenSum}(X)=\mathrm{OddSum}(\{z\}\cup X)-z$.

**Proof.** $z\ge\max(X)\Rightarrow z=\max(\{z\}\cup X)$. By the Global-max
Peeling Lemma, $\mathrm{OddSum}(\{z\}\cup X)=z+\mathrm{EvenSum}(X)$
(removing the adjoined copy of $z$ leaves exactly $X$). Rearrange.
$\blacksquare$

*(Reviewer: elementary two-line consequence of an already-certified fact,
verified by direct algebraic re-derivation — no further numeric check
needed, but consistent with the numerics below.)*

## Theorem 1 ($T(2)$ fully closed)

**Statement.** For every refinement of $\Gamma_2=(4,2,1)$ using $\le2$ cuts,
$\mathrm{OddSum}\ge4$.

**Proof.** Suffices to prove $T(2,2)$. Case on $j$ = cuts spent on top piece
"4": $j=0$ by the certified Case-1 result (Fact 2); $j=1$ by the certified
`element-bound-and-j1-theorem.md` (needs $T(1)$, itself certified). New
content, $j=2$: top splits into three fragments $a_1\ge a_2\ge a_3>0$
($\sum=4$), tail exactly $\{2,1\}$ untouched. Two cases on $a_1$ vs. $2$:

- **$a_1>2$:** sort is $(a_1,2,m_1,m_2,m_3)$ where $(m_1,m_2,m_3)=\mathrm{sort}(a_2,a_3,1)$;
  $\mathrm{OddSum}=a_1+m_1+m_3=5-m_2$ (using $m_1+m_2+m_3=5-a_1$), and
  $m_2=\mathrm{median}(a_2,a_3,1)\le1$ (shown by casing on $a_2\ge1$ vs $<1$,
  using $a_2+a_3<2$), so $\mathrm{OddSum}\ge4$.
- **$a_1\le2$:** sort is $(2,n_1,n_2,n_3,n_4)=\mathrm{sort}(2;a_1,a_2,a_3,1)$;
  $\mathrm{OddSum}=2+n_2+n_4=7-(n_1+n_3)$, and $n_1+n_3\le3$ (shown by
  casing on $a_1\ge1$ vs $<1$, using $a_3\le(4-a_1)/2$), so
  $\mathrm{OddSum}\ge4$.

$\blacksquare$

## Verification (proof-reviewer, round 3)
- Formula check: $10^5$-scale random trials confirm $\mathrm{OddSum}=5-\mathrm{median}(a_2,a_3,1)$
  (case $a_1>2$) and $\mathrm{OddSum}=7-(n_1+n_3)$ (case $a_1\le2$) match direct
  sorted computation exactly, zero mismatches (reviewer independently ran
  200,000 random trials, zero mismatches).
- Minimum-value check: 500,000 random splits confirm $\mathrm{OddSum}\to4$
  as infimum (attained in the limit $a_3\to1^-,a_2\to1^+$, or similar
  boundary configurations), never below 4.

## Reuse notes
$T(2)$ is a genuine new complete small case, usable as a certified base
case by any inductive approach (e.g. enables `element-bound-and-j1-theorem.md`'s
Step 1 to be applied at $m=3$, previously blocked on $T(2)$ being
unestablished). Lemma Z is fully general (no geometric structure needed)
and reusable by any approach needing to convert an EvenSum target into an
OddSum target on an augmented multiset.

## Note on Proposition C (Case-A circularity) — NOT separately certified as a lemma
`approaches/self-similar-induction-on-n.md`'s Proposition C (showing the
natural single-peel completion of Case A, $b_1\ge2^{m-1}$, is logically
equivalent via Lemma Z to an instance of the generalized target $G(m,k;V'')$
with the same fragment count as the *original* split, i.e. no net reduction
in problem size) was independently re-derived and verified algebraically by
the proof-reviewer (exact symbolic check plus 16,681 random-instance
numeric check of the claimed equivalence, zero mismatches, after correcting
an initial reviewer setup bug that had failed to enforce $\mathrm{sum}(S)=2^m-1$).
The mathematical content is correct, but it is a **documented negative
result / obstruction**, not a positive reusable tool other approaches would
import — it is recorded here in `current.md` and the approach file itself
rather than as a separate `lemmas/` entry, consistent with how other
documented dead ends (e.g. the Q-priority and tail-priority strategy
refutations) have been handled in prior rounds.
