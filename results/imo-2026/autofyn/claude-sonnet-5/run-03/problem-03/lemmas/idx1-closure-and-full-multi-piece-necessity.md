## Multi-Piece Necessity Theorem for the triangular family — now complete for every $idx$, every $n\ge3$

Certified round 8. Proved in `approaches/lp-duality-split-polytope.md`
(round 8 section "Main proof of $A(N,N,y)\ge1$ for all $N\ge4$"), closing
the single remaining case ($idx=1$, i.e. $k=N$ in Theorem A's
normalization) left open by the certified `non-top-piece-theorem-b.md`
(which covers $idx\ge2$, i.e. $k\le N-1$). Combining the two gives the
complete theorem stated below.

**Setup (imported from Theorem A / `non-top-piece-theorem-b.md`).** For
$N\ge4$ and a finite multiset $Y=\{y_1,\ldots,y_m\}$ ($m\ge2$) of positive
reals summing to $N$, define
$$A(N,N,y_1,\ldots,y_m):=\mathrm{AltSum}\bigl(\{1,\ldots,N-1\}\cup\{y_1,\ldots,y_m\}\bigr).$$

**Theorem (idx=1 closure).** For every $N\ge4$, every $m\ge2$, and every
choice of positive reals $y_1,\ldots,y_m$ with $\sum y_i=N$,
$$A(N,N,y_1,\ldots,y_m)\ \ge\ 1.$$

**Three elementary facts used** (all elementary, proved from scratch in
the approach file): for a finite multiset $T$ of nonnegative reals sorted
descending $t_1\ge\cdots\ge t_r\ge0$ ($\mathrm{AltSum}(\emptyset):=0$):
- Peel identity: $T\ne\emptyset\Rightarrow\mathrm{AltSum}(T)=\max(T)-\mathrm{AltSum}(T\setminus\{\max(T)\})$.
- Upper-bound fact: $\mathrm{AltSum}(T)\le\max(T)$.
- Nonnegativity fact: $\mathrm{AltSum}(T)\ge0$ (pair consecutive terms).

**Small-Tail Bound (STB).** For $L>0$ and a finite multiset $Y$ of
positive reals with $\max(Y)\le L$: $\mathrm{AltSum}(\{L\}\cup Y)\ge
L-\mathrm{sum}(Y)$. (Peel $L$; bound the residual's AltSum by its own max,
hence by its sum.)

**Lemma $f$.** Fix $t\in(0,1]$; for $r\ge1$ and any finite multiset $Y$ of
positive reals with $\mathrm{sum}(Y)=t$, $f(r):=\mathrm{AltSum}(\{1,\ldots,
r\}\cup Y)$ satisfies: $r$ odd $\Rightarrow f(r)\in[\tfrac{r+1}2-t,\tfrac{r+1}2]$;
$r$ even $\Rightarrow f(r)\in[\tfrac r2,\tfrac r2+t]$. (Induction on $r$,
base case via STB, inductive step by peeling the landmark $r$.)

**Lemma $g$.** Fix $u\in(1,2)$; for $r\ge2$ and any finite multiset $Y''$ of
positive reals with $\mathrm{sum}(Y'')=u$, $g(r):=\mathrm{AltSum}(\{1,\ldots,
r\}\cup Y'')$ satisfies: $r$ odd $\Rightarrow g(r)\in[\tfrac{r-1}2,\tfrac{r-1}2+u]$;
$r$ even $\Rightarrow g(r)\in[\tfrac r2+1-u,\tfrac r2+1]$. (Same induction
technique as Lemma $f$, both bounds carried through simultaneously.)

**Proof of the Theorem.** Let $y_{\max}:=\max(y_1,\ldots,y_m)$. Three
exhaustive, disjoint cases on $y_{\max}$ vs. $N-2,N-1$:

- **$y_{\max}\ge N-1$:** peel $y_{\max}$, then the landmark $N-1$ (unique
  max of the residual since the remaining fragments sum to $\le1$), reduce
  to Lemma $f$ at $r=N-2$; both parities give $\mathrm{AltSum}\ge1$ for
  $N\ge4$ (resp. $N\ge5$ for odd $N$), giving the target after unwinding
  the two peels.
- **$y_{\max}\le N-2$:** peel the landmark $N-1$ (unique max), bound the
  residual's AltSum by its max $\le N-2$ directly (Upper-bound fact), no
  induction lemma needed.
- **$N-2<y_{\max}<N-1$:** peel $N-1$, then $y_{\max}$ (now the unique max
  of the doubly-reduced residual), reduce to Lemma $g$ at $r=N-2$; both
  parities give the needed bound for $N\ge4$ (resp. $N\ge5$ odd), closing
  the case.

Full case-by-case algebra is in the approach file. $\blacksquare$

**Reviewer verification (round 8, independent, exact `Fraction`
arithmetic, from-scratch scripts, not reusing the builder's own).**
- Lemma $f$: 30,000 trials, $r=1..15$, $t\in(0,1]$ at denominator 1000
  granularity, random multiset splits of $Y$ — zero violations of the
  stated interval bounds.
- Lemma $g$: 30,000 trials, $r=2..15$, $u\in(1,2)$ at denominator-1000
  granularity — zero violations.
- Main theorem $A(N,N,y)\ge1$: 60,000 random trials ($N=4..40$, $m=2..12$,
  random positive rational compositions) plus a targeted boundary sweep
  (2000+ points per $N,m$ combination approaching $y_{\max}=N-2$ and
  $y_{\max}=N-1$ from both sides, $N=4..29$, $m=2..5$) — zero violations
  in every test; margin shrinks to exactly $0$ only in the sup/inf limit,
  matching the proof's own identified tightness. Confirmed the exact
  equality case $A(4,4,3,1/2,1/2)=1$ by direct exact computation.
- Independently re-verified Theorem A's reduction (the bridge from the
  original triangular-family excess claim to $A(N,k,y)\ge1$): reconstructed
  the actual triangular-family partition and split in original units for
  $n=3,\ldots,7$, every $idx$, and confirmed the claimed identity
  `excess = (d/2)*A(N,k,y)` exactly by direct exact-rational computation
  in every one of 28 instances checked (4 to 8 indices per $n$).

**Consequence — the full theorem, now certified.** Combined with
`non-top-piece-theorem-b.md` (idx≥2, i.e. $k\le N-1$): **for every $n\ge3$
and every choice of which single piece of the triangular family
$p_i=(n+2-i)/D_n$ is split into $\le n$ pieces (every other piece held
fixed), the resulting excess of $\mathrm{OddSum}$ over $c(n)$'s midpoint
$1/2$ is at least $1/((n+1)(n+2))$, strictly positive.** The Multi-Piece
Necessity Theorem for the triangular family (every $idx\in\{1,\ldots,n+1\}$,
every $n\ge3$) is now proved in full and complete, by a single argument
uniform in $n$ (Theorem A's reduction + Theorem B for $idx\ge2$ + this
theorem for $idx=1$).

**Scope note (do not overclaim beyond this).** This is a **necessity**
result about single-piece XY responses to one specific LB family (the
triangular family) — it does **not** by itself prove the upper-bound
direction of the whole `imo-2026-03` problem, nor does it establish that
some multi-piece response *does* close the gap to $\le c(n)$ for every
$n$ (only a genuine two-piece closing response was exhibited at $n=3$).
It is one ingredient among several toward the general upper-bound
direction, which remains open (see `current.md`).
