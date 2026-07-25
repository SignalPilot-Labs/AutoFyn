# Twin-Anchor Floor Theorem

Certified round 15 (proof-reviewer), from `lp-duality-split-polytope.md`.
**Supersedes/strengthens** `chain-correction-floor-theorem.md` (n≥6) by
covering every n≥3 with a simpler, unconditional construction. Both files
are kept; this one should be preferred for any future citation needing
V(e_0)=1/2 since its range is strictly larger and its proof has no side
condition to verify.

## Statement

Let $n\ge3$, $N:=n+1$, $\delta:=\gamma(n)=1/(2^N-1)$, and let $e_0$ be the
region vertex of $\overline{B(n)}$ with coordinates $p_i(e_0)=a+(N-i)\delta$
for $i=1,\dots,N$ (an exact arithmetic progression, common difference
$\delta$), $a:=p_N(e_0)>0$.

There is a legal XY response at $e_0$ using exactly $n-1\le n$ cuts, all
resulting fragments strictly positive, achieving $\mathrm{OddSum}(M)=\tfrac12$
exactly — the universal absolute floor for any legal response at any
partition (immediate from $\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$, since a
descending sort's consecutive-pair differences are each $\ge0$). Hence
$V(e_0)=\tfrac12$ exactly, for every $n\ge3$.

**Construction.**
- Piece $1$ ($=a+(N-1)\delta$) splits into $(p_{N-1},\,(N-2)\delta)$ where
  $p_{N-1}=a+\delta$.
- Piece $2$ ($=a+(N-2)\delta$) splits into $(p_N,\,(N-2)\delta)$ where
  $p_N=a$.
- Every piece $j=3,\dots,N-2$ (empty range when $N\le5$) bisects into two
  exact halves.
- Pieces $N-1,N$ are left untouched.

**Key algebraic identity.** Piece $1$'s second fragment
$p_1-p_{N-1}=(N-2)\delta$ and piece $2$'s second fragment
$p_2-p_N=(N-2)\delta$ — identically equal for every $N$, no induction or
side condition needed (contrast with the older Chain-Correction
construction's piece-3/piece-5 identity, valid only for $N\ge7$ under an
extra positivity hypothesis $a>2\delta$).

**Positivity.** Every fragment is one of $p_{N-1}=a+\delta>0$, $p_N=a>0$,
$(N-2)\delta>0$ (since $N\ge4$), or a half of an already-positive piece —
unconditionally positive for every $n\ge3$, no inequality between $a$ and
$\delta$ needed.

**Why OddSum $=1/2$.** The $2N-2$ fragments partition into $N-1$
equal-valued pairs: $(p_{N-1},p_{N-1})$, $(p_N,p_N)$,
$((N-2)\delta,(N-2)\delta)$, and the bisection-halves of pieces
$3,\dots,N-2$. By the Even-Block-Neutrality mechanism (an even-sized block
of one repeated value occupies consecutive ranks in the descending sort and
contributes exactly $0$ to $\mathrm{AltSum}$, regardless of interleaving
with other groups — inserting/removing an even block shifts every other
element's rank by an even number, preserving parity), every group
contributes $0$ to $\mathrm{AltSum}$, so $\mathrm{AltSum}(M)=0$ and
$\mathrm{OddSum}(M)=\tfrac12(1+0)=\tfrac12$.

## Scope note: $n=2$ genuinely out of scope

At $n=2$ ($N=3$) the parity/budget argument breaks (need an odd split-piece
count $s\in\{1,3\}$; $s=1$ fails combinatorially, $s=3$ exceeds the $n=2$
cut budget) — checked explicitly by direct computation, not claimed closed
by this theorem.

## Reviewer independent verification

Own from-scratch exact-`Fraction` script (not the builder's), re-deriving
$a$ from $\sum_i p_i(e_0)=1$ (i.e.
$a=(1-\delta N(N-1)/2)/N$) and building the literal fragment multiset for
every $n=3,\dots,40$ (38 instances): confirmed every fragment strictly
positive, total mass exactly $1$, cuts used $=n-1\le n$ (legal), and
$\mathrm{AltSum}(M)=0$ exactly (hence $\mathrm{OddSum}(M)=1/2$ exactly) —
**zero deviation in all 38 cases**, including a hand-checked $n=3$ instance
matching the file's own worked example digit-for-digit. Fully proved, no
gaps.

## Consequence

$V(e_0)=1/2$ (not $c(n)$) for every $n\ge3$ (not just $n\ge6$ as the older
Chain-Correction Floor Theorem established) — a strict extension of the
already-corrected finding recorded in that file. Does not by itself close
any open gap in the Existence Theorem's general-$p$ target
($V(p)\le c(n)$ for every $p$), but is a clean, general-purpose,
now-maximally-simple fact about the single vertex $e_0$, reusable by any
future approach needing $V(e_0)$'s exact value at any $n\ge3$.
