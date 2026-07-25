## Theorem B (Non-Top-Piece Theorem): dimensionless AP-normalization, single-piece splits away from the top

Certified round 7. Proved in `approaches/lp-duality-split-polytope.md`
(round 7, Section 7.2–7.3), used to close $n$ of the $n+1$ index choices
(all except $idx=1$, the top piece) of the general-$n$ Multi-Piece
Necessity theorem for the triangular family, by a single argument uniform
in $n$.

**Setup (dimensionless AP-normalization).** For any AP-structured family
whose landmarks, divided by the common difference $d$, form the run of
consecutive integers $1,2,\ldots,N$ (the triangular family $p_i=(n+2-i)/D_n$
does this with $N=n+1$), define, for $k\in\{1,\ldots,N\}$ (the normalized
value of the landmark being split) and positive reals $y_1,\ldots,y_m$
($m\ge2$) summing to $k$:
$$S:=(\{1,\ldots,N\}\setminus\{k\})\cup\{y_1,\ldots,y_m\},\qquad
A(N,k,y_1,\ldots,y_m):=\mathrm{AltSum}(S).$$
(This is the normalized statement of "replace the landmark $k$ by $m$
positive fragments summing to $k$, leaving every other landmark fixed";
$idx=1$ corresponds to $k=N$, the top piece.)

**Theorem B.** For every $N\ge2$, every $k\in\{1,\ldots,N-1\}$ (i.e.
$idx\ge2$: any piece **other than** the top piece), and every $m\ge2$ and
positive $y_1,\ldots,y_m$ with $\sum y_i=k$:
$$A(N,k,y_1,\ldots,y_m)\ \ge\ 1.$$

**Two standard facts used.** For a finite multiset $T$ of nonnegative
reals, sorted descending $t_1\ge\cdots\ge t_r\ge0$: (Peel identity) if
$T\ne\emptyset$, $\mathrm{AltSum}(T)=t_1-\mathrm{AltSum}(T\setminus\{t_1\})$;
(Upper bound) $\mathrm{AltSum}(T)\le t_1=\max(T)$ (since
$\mathrm{AltSum}(T)=t_1-(t_2-t_3)-(t_4-t_5)-\cdots$ and every bracketed
difference is $\ge0$).

**Proof.** Let $S=(\{1,\ldots,N\}\setminus\{k\})\cup\{y_1,\ldots,y_m\}$.
Since $k\le N-1$, $N\in\{1,\ldots,N\}\setminus\{k\}\subseteq S$. Every
fragment $y_i<k$ (strict: $m\ge2$ and the other $m-1\ge1$ fragments are
positive, so $y_i=k-\sum_{j\ne i}y_j<k$), so $\max(y_1,\ldots,y_m)<k\le
N-1<N$; hence $N$ is the unique maximum of $S$.

By the Peel identity, $\mathrm{AltSum}(S)=N-\mathrm{AltSum}(S\setminus\{N\})$.
Now $S\setminus\{N\}=(\{1,\ldots,N-1\}\setminus\{k\})\cup\{y_1,\ldots,y_m\}$,
and every element of it is $\le N-1$ (remaining landmarks are $\le N-1$ by
construction; every $y_i<k\le N-1$). So by the Upper bound fact,
$\mathrm{AltSum}(S\setminus\{N\})\le N-1$. Combining:
$$\mathrm{AltSum}(S)=N-\mathrm{AltSum}(S\setminus\{N\})\ge N-(N-1)=1.
\qquad\blacksquare$$

**Consequence (for the triangular family).** For every $n\ge1$, every piece
$p_{idx}$ with $idx\ge2$, and every $\le n$-cut split of that piece (all
other pieces untouched), the excess over $c(n)$'s midpoint $1/2$ is at
least $1/((n+1)(n+2))$ — unconditionally, for every $n$ simultaneously, by
a single uniform argument. This closes $n$ of the $n+1$ possible index
choices, leaving exactly $idx=1$ (splitting the top piece) open; the proof
breaks down there because $N\notin S\setminus\{k\}$ when $k=N$, so
$\max(S)$ may come from $Y$ instead of the landmark set.

**Independent verification (proof-reviewer, round 7).** Reconstructed the
proof line by line: the max-uniqueness argument, the Peel identity
(standard, "remove the max, negate the rest"), and the Upper-bound fact
(immediate from alternating-sign telescoping) all check out with no hidden
case gap. Independently stress-tested with 200,000 exact-`Fraction` random
trials ($N\in[2,30]$, $k\in[1,N-1]$, $m\in[2,6]$, random rational
compositions of $k$): zero violations, and the bound is tight (exact value
$1$ found, e.g. $N=3,k=1,y=(1/2,1/2)$). Confirmed the theorem's scope is
exactly $idx=2,\ldots,N$ (i.e. $n$ of the $n+1$ values for the triangular
family, $N=n+1$) — found and corrected a minor off-by-one in the source
file's own summary sentence ("proved for $n-1$ of $n$" corrected to "$n$ of
$n+1$"; the proof and its scope were always correct, only that one summary
count was mislabeled).

**Source.** Proved in `approaches/lp-duality-split-polytope.md` (round 7,
Theorem B).

**Reuse.** A fully general, dimensionless tool: for any AP-structured
partition (landmarks forming a consecutive integer run after normalizing
by the common difference), splitting any landmark other than the top one
into $\ge2$ positive fragments summing to its own value always costs at
least $1$ unit of AltSum in normalized terms — reusable by any future
approach analyzing single-piece-split responses against such a family, not
specific to the triangular family.
