## Status
partial

## Round 18 update (light/optional dispatch — a double-counting sketch
for the $s\ge n-1$ necessity conjecture, explicitly NOT a refinement of
the Generalized Mass-Constraint Theorem, which is closed for this
approach; honest negative/inconclusive outcome, kept intentionally
short per the round's light-dispatch instruction)

**Dispatch this round (light/optional, ~30 min):** sketch a
double-counting mechanism for the $s\ge n-1$ necessity conjecture,
taking crux corpus entries `aimo-0091` and `aimo-0178` as (flagged, in
advance, as weak) analogies. Per the dispatch, the certified
Generalized Mass-Constraint Theorem (round 17,
`lemmas/even-multiplicity-criterion-and-generalized-mass-constraint.md`)
is **not** re-attempted or refined further this round — it structurally
caps at $s\gtrsim N/2$ and stays as is.

### What the two cited cruxes actually do (read from the corpus, not
guessed)

**`aimo-0091`** (Dutch 2010, tiling a $4\times2010$ board with
dominoes): the load-bearing double-count is *"sum the forced minimum
number of straddling tiles over every interior grid line and compare
the total cells covered against the board area."* Concretely: each of
the $2009$ vertical seams forces $\ge2$ straddling horizontal dominoes
(via a parity upgrade: columns $1..k$ contain an even number, $4k$, of
cells, so horizontal dominoes crossing the seam at $k$ must come in an
even count, and a fault-free tiling forces $\ge1$, hence $\ge2$); each
of the $3$ horizontal seams forces $\ge1$ straddling vertical domino;
summing these *disjoint* forced tiles over *all* seams and doubling
(each domino covers $2$ cells) gives a cell count exceeding the board's
total area — a contradiction.

**`aimo-0178`** (ISL 2020 C7 "beams in a cube"): the mechanism is
*"establish one asymmetric pairwise lower bound between two of three
symmetric classes, then invoke the problem's 3-fold rotational symmetry
to get the other two copies for free, and sum."* Concretely: with
$N_x,N_y,N_z$ the beam counts by axis direction, one hard lemma
($N_z>0\Rightarrow N_x+N_y\ge n$) is proved once; rotating the labels
$x\to y\to z\to x$ (a genuine symmetry of the cube and the touching
condition) gives the other two inequalities *for free*, and summing all
three ($2(N_x+N_y+N_z)\ge3n$) gives the global bound.

**The shared mechanism, abstracted.** Both cruxes get their power from
a **multi-part index set with either (a) many *parallel, independent*
sites to sum a per-site forced minimum over** (aimo-0091's seams) **or
(b) a genuine symmetry group acting transitively on several
classes**, letting one hard local inequality be "reused" for free
across all classes (aimo-0178's rotation). Neither mechanism is "just
sum masses over one fixed dichotomy" — that weaker one-shot mass-count
is exactly what the certified Generalized Mass-Constraint Theorem
already does at this problem's active/untouched dichotomy, and it is
already known (round 17) to structurally cap at $s\gtrsim N/2$.

### Why both are flagged, correctly, as weak analogies — checked
directly against this problem's actual structure, not asserted

**Test for mechanism (a), many independent sites.** At $e_0$, is there
an analogue of "the $2009$ vertical seams," i.e. a *family of many
parallel sites*, each independently forcing a piece of the needed
lower bound on $s$, that could be *summed*? The natural candidate is
the $m=N-s$ *individual* untouched pieces $\{p_i\}_{i\in U}$ — but the
Generalized Mass-Constraint Theorem's proof (round 17) **already sums
over exactly this index set** ($\sum_{i\in U}p_i\le\sum_{j\in S}p_j$,
summing one inequality $\sum_{i\in K_j}p_i\le p_j$ per active piece
$j\in S$ over all $j$). So the "sum over many sites" move is not a new
idea here — it is precisely the certified theorem's own proof
technique, already exhausted (it is the *reason* that theorem caps at
$N/2$: summing $m$ individual mass-inequalities, each merely
nonnegative, gives a bound on *total mass* of $U$, which only forces
$m$ pieces to be a *minority by mass*, not a *minority by count* — the
gap the dispatch itself named as unclosable by mass-counting alone).
Concretely checked: there is no analogue of aimo-0091's *parity
upgrade* (the fact that the cell-count on one side of a seam is
provably even, upgrading "$\ge1$" to "$\ge2$") available at this
problem's dichotomy, because the relevant object here (whether a given
untouched piece needs $1$ vs. $\ge3$ matching fragments) is a property
of the *specific* legal response chosen, not a parity fact forced by
the *positions* of the untouched pieces alone (unlike aimo-0091, where
the seam's position alone, independent of the specific tiling, fixes
the parity of one side's cell count). So the parity-upgrade trick does
not transplant.

**Test for mechanism (b), symmetry-driven multiplication.** aimo-0178's
power move needs a genuine group action (the cube's $3$-fold axis
rotation) under which the *same* hard inequality, proved once, yields
literally interchangeable copies. This problem's active/untouched
dichotomy at $e_0$ has **no such symmetry**: $e_0$'s coordinates
$p_i=a+(N-i)\delta$ are a *strictly monotone* arithmetic progression
(pairwise distinct by construction, certified
`lemmas/finite-cell-vertex-reduction-and-region-classification.md`),
so there is no permutation of the index set $\{1,\dots,N\}$ under which
the problem (which pieces are "active," which "untouched," and the
values themselves) is invariant except the identity — unlike the cube,
which literally looks the same after a $120°$ rotation of the three
axes. Checked directly: attempting to relabel "active" and "untouched"
symmetrically (e.g. treating the problem as symmetric under $S\leftrightarrow U$)
fails immediately, since $S$ and $U$ play structurally different roles
in the Even-Multiplicity Criterion's proof (untouched pieces are single
atomic values that must be *matched*; active pieces are the *sources*
of matching material, with strictly more freedom) — there is no
relabeling symmetry to exploit for a "prove one case, get the others
free" multiplication.

### Honest conclusion of the sketch: no viable double-counting
mechanism found this round, and a structural reason is identified for
why

Both flagged analogies fail to transplant for an identifiable
structural reason, not merely "not attempted": aimo-0091's mechanism
(a) is the *same* summing-over-many-sites idea the certified
Generalized Mass-Constraint Theorem already uses, so it offers no new
leverage beyond what is already certified and already known to cap at
$s\gtrsim N/2$; and its key parity-upgrade trick has no analogue here
since the relevant multiplicity-parity fact depends on the *specific
response*, not on the untouched pieces' positions alone. aimo-0178's
mechanism (b) needs a genuine symmetry group acting on the classes
being double-counted, and $e_0$'s dichotomy (active vs. untouched, over
a strictly monotone, asymmetric AP) has no such symmetry to exploit. No
new theorem, no new lemma, and (per the round's own instruction) the
Mass-Constraint direction is **not** re-attempted or refined further.
This closes out the light dispatch honestly: the two suggested cruxes
are confirmed, by direct structural comparison rather than by assertion,
to be weak analogies for this specific gap, and the reason is recorded
so no future round re-tries transplanting either mechanism verbatim.
**Status unchanged: `partial`.** The open gap (closing $s\gtrsim N/2$
down to the conjectured $s\ge n-1$, i.e. $m\le2$) remains exactly as
characterized in round 17 — this round adds a documented negative
scouting result on one candidate route (double counting via these two
cruxes), not a new route itself.

## Round 17 update (read this first — a genuine new theorem, the
**Generalized Mass-Constraint Theorem**, extending round 11's Mass-
Constraint from the restricted tie-construction family to *every* legal
response whatsoever; gives an exact, rigorous (not numeric) impossibility
result at a handful of small $n$, but honestly falls well short of proving
the full $s\ge n-1$ necessity conjecture — the asymptotic gap is
characterized precisely, not papered over)

**Dispatch this round:** (1) re-run the round-16 float Nelder-Mead numeric
lead in exact rational arithmetic at $n=8,9,10$, $s=n-2,n-3,n-4$; (2) if
spare capacity remains, attempt a Mass-Constraint-style counting argument
for $s\ge n-1$ necessity.

**A methodological point first, honestly flagged.** Item (1) as literally
stated ("re-run Nelder-Mead in exact arithmetic") is not a well-posed task:
Nelder-Mead is a continuous local-search heuristic with no exactness
guarantee even in principle — there is no way to make a heuristic search
"exact," only to replace it with either (a) an exact enumeration over a
finite candidate set, or (b) a proved inequality. This round pursues (b):
instead of re-running the same heuristic with a different number type
(which would still yield only more soft numeric leads, exact or not), it
derives a genuine **necessary condition** on $s$ from first principles,
verifies that condition in exact `Fraction` arithmetic at the requested
$(n,s)$ pairs, and is honest about exactly how far it goes and no further.
This is a stronger and more useful response to the spirit of the dispatch
than a literal re-run would have been.

### New Lemma: the Even-Multiplicity Equality Criterion

**Statement.** Let $M$ be a finite multiset of positive reals with
$\mathrm{sum}(M)=1$ (a legal response at any partition). Sort $M$
descending as $v_1\ge v_2\ge\cdots\ge v_{|M|}$. Then
$\mathrm{OddSum}(M)=\tfrac12$ (i.e. $M$ attains the universal floor exactly)
**if and only if** $|M|$ is even and every distinct value occurring in $M$
has even multiplicity.

*Proof.* Write $|M|=2t+\varepsilon$, $\varepsilon\in\{0,1\}$.

**Case $\varepsilon=1$ ($|M|$ odd).** By definition
$\mathrm{AltSum}(M)=\sum_{i=1}^{t}(v_{2i-1}-v_{2i})+v_{2t+1}$. Each
bracketed term is $\ge0$ (descending sort), and $v_{2t+1}>0$ (every element
of a legal response is strictly positive, since it is a fragment of a
positive-mass piece or a whole positive piece). Hence
$\mathrm{AltSum}(M)>0$ strictly, so $\mathrm{OddSum}(M)=\tfrac12(1+
\mathrm{AltSum}(M))>\tfrac12$ strictly. So the floor is never attained
when $|M|$ is odd — settling this case; $\Rightarrow$ direction and
$\Leftarrow$ direction both vacuous/consistent here since "every value has
even multiplicity" is impossible to combine with odd total size force a
contradiction on its own is not needed: we've shown directly the floor
fails.

**Case $\varepsilon=0$ ($|M|=2t$).**
$\mathrm{AltSum}(M)=\sum_{i=1}^t(v_{2i-1}-v_{2i})$, a sum of $t$
nonnegative terms (descending sort), so $\mathrm{AltSum}(M)=0$ iff
$v_{2i-1}=v_{2i}$ for every $i=1,\dots,t$ — call this Property (P).
$\mathrm{OddSum}(M)=\tfrac12$ iff $\mathrm{AltSum}(M)=0$ iff (P) holds
(directly from $\mathrm{OddSum}=\tfrac12(\mathrm{sum}+\mathrm{AltSum})$
and $\mathrm{sum}(M)=1$). It remains to show (P) $\iff$ every distinct
value has even multiplicity.

Group the sorted sequence into maximal blocks of equal consecutive values:
distinct values $c_1>c_2>\cdots>c_r$ with multiplicities $m_1,\dots,m_r$
($\sum m_j=2t$), block $j$ occupying ranks $R_{j-1}+1,\dots,R_j$ where
$R_0=0$, $R_j=m_1+\cdots+m_j$.

($\Leftarrow$) Suppose every $m_j$ is even. Then every $R_j$ is even (sum
of evens), so every block starts at an odd rank ($R_{j-1}+1$, odd since
$R_{j-1}$ even) and ends at an even rank ($R_j$). Fix any odd rank
$p=2i-1$ within block $j$ (i.e. $R_{j-1}<p\le R_j$); since $p$ is odd and
$R_j$ is even, $p\ne R_j$, so $p<R_j$, hence $p+1=2i\le R_j$ also lies in
block $j$. Thus $v_{2i-1}=v_{2i}=c_j$ for every $i$ — Property (P) holds.

($\Rightarrow$) Suppose some $m_{j_0}$ is odd. Since $R_0=0$ is even and
parity of $R_j$ flips exactly when $m_j$ is odd, let $j_0$ be the *first*
index with $R_{j_0}$ odd (exists: $R_{j_0}$ has the same parity as
$m_1+\cdots+m_{j_0}$, and since $R_0$ is even and the total $R_r=2t$ is
even, if any $m_j$ is odd, the running parity must flip at least twice —
in particular changes at some first index; concretely, take $j_0$ minimal
with $m_1+\cdots+m_{j_0}$ odd). Then $R_{j_0-1}$ is even and $R_{j_0}$ is
odd, so block $j_0$ ends at the odd rank $R_{j_0}$. Since $R_{j_0}<2t$
(because $R_r=2t$ is even $\ne R_{j_0}$, odd), block $j_0+1$ exists and
starts at rank $R_{j_0}+1$ (even), with value $c_{j_0+1}<c_{j_0}$. The pair
$(v_{R_{j_0}},v_{R_{j_0}+1})=(c_{j_0},c_{j_0+1})$ is exactly one of the
Property-(P) pairs (rank $R_{j_0}$ is odd, rank $R_{j_0}+1$ is the next,
even, rank), and $c_{j_0}\ne c_{j_0+1}$, so this pair is unequal —
Property (P) fails. $\blacksquare$

This lemma is elementary combinatorics on sorted sequences, fully general
(no dependence on $e_0$ or any specific partition), and reusable well
beyond this approach's own scope — **proposed for certification below.**

### New Theorem: the Generalized Mass-Constraint Theorem

**Statement.** Let $p_1,\dots,p_N$ ($N=n+1$) be any legal adversary
partition, $S\subseteq\{1,\dots,N\}$ the set of pieces a response splits
("active", $|S|=s$), $U=\{1,\dots,N\}\setminus S$ the untouched pieces
($|U|=m=N-s$), with the $p_i$, $i\in U$, pairwise distinct (true whenever
the adversary's pieces are themselves pairwise distinct, as at $e_0$: an
exact arithmetic progression). If the resulting response's fragment
multiset $M$ (untouched pieces $\cup$ all fragments) attains
$\mathrm{OddSum}(M)=\tfrac12$ exactly, then
$$\sum_{i\in U}p_i\ \le\ \tfrac12,\qquad\text{equivalently}\qquad
\sum_{i\in S}p_i\ \ge\ \tfrac12.$$

*Proof.* By the Even-Multiplicity Equality Criterion, every distinct
value of $M$ has even multiplicity $\ge2$. For $i\in U$, the value $p_i$
occurs in $M$ at least once from the untouched piece itself; by
even-multiplicity, it must occur at least twice in total, so at least one
fragment produced by splitting some active piece is **exactly** equal to
$p_i$ (call this a "match" for $i$). Since the $p_i$, $i\in U$, are
pairwise distinct, a single fragment can match at most one $i\in U$; fix,
for each $i\in U$, one witnessing match, and let $h(i)\in S$ be the active
piece producing it. Group $U$ by host: $K_j:=\{i\in U:h(i)=j\}$ for
$j\in S$ (a partition of $U$ across the active pieces). For each $j\in S$,
the fragments matching $\{p_i:i\in K_j\}$ are pairwise distinct real
numbers among the (finitely many, nonnegative) fragments produced by
splitting $p_j$, and all fragments of $p_j$ sum to exactly $p_j$; hence
any sub-collection of them (in particular, the $|K_j|$ match-fragments)
sums to at most $p_j$:
$$\sum_{i\in K_j}p_i\ \le\ p_j.$$
Summing over $j\in S$ (the $K_j$ partition $U$, so the left side sums to
$\sum_{i\in U}p_i$):
$$\sum_{i\in U}p_i=\sum_{j\in S}\sum_{i\in K_j}p_i\ \le\ \sum_{j\in S}p_j.$$
Since $\sum_{i\in U}p_i+\sum_{j\in S}p_j=1$, this rearranges to
$\sum_{i\in U}p_i\le\tfrac12\le\sum_{j\in S}p_j$. $\blacksquare$

**Why this is new and strictly stronger than the certified
`lemmas/rank-pinning-lemma-and-mass-constraint-theorem.md` Mass-Constraint
Theorem.** The certified theorem there ($\Pi\ge\tfrac12$, $\Pi=$ sum of
split pieces) is proved only for the specific "Multi-Piece Subset-Tie"
construction (each split piece's fragments are forced by an explicit
recipe: one sub-collection matching a specific assigned group of untouched
pieces exactly, plus one leftover residual fragment). The proof above
makes **no assumption about the construction mechanism at all** — it
applies to *any* legal response whatsoever (arbitrary number of fragments
per active piece, arbitrary internal fragment-vs-fragment ties, any
residual structure) that happens to attain $\mathrm{OddSum}=\tfrac12$
exactly, deriving the same conclusion purely from the Even-Multiplicity
Equality Criterion plus a mass-counting argument. **Proposed for
certification below** as a genuine strengthening (same conclusion, much
wider scope of applicability) — the reviewer's call whether to certify
alongside or in place of the existing file.

### Application at $e_0$: an exact necessary condition on $s$

At $e_0$ (AP coordinates $p_i=a+(N-i)\delta$, certified
`lemmas/finite-cell-vertex-reduction-and-region-classification.md`), the
$N$ pieces are pairwise distinct, so the theorem applies to any active set
$S$. Since $\sum_{j\in S}p_j\ge\tfrac12$ is necessary, and (for fixed
$s=|S|$) the maximum possible value of $\sum_{j\in S}p_j$ over all choices
of $S$ is achieved by taking $S$ to be the $s$ **largest** pieces
(any exchange of a smaller piece in $S$ for a larger piece outside $S$
strictly increases the sum, since the pieces are pairwise distinct), a
**necessary condition depending only on $s$** (not on which specific
pieces are chosen active) follows:
$$\text{floor attainable at $e_0$ with $|S|=s$}\ \Longrightarrow\
\sum_{i=1}^{s}p_i(e_0)\ \ge\ \tfrac12.$$

**Exact closed form for the top-$s$ sum.** Using
$p_i=a+(N-i)\delta$ and the certified identity $a=\tfrac1N-\delta\cdot
\tfrac{N-1}2$ (from $\sum_{i=1}^Np_i=1$, a one-line computation:
$Na+\delta\sum_{i=1}^N(N-i)=Na+\delta\cdot\tfrac{N(N-1)}2=1$):
$$\sum_{i=1}^{s}p_i(e_0)=sa+\delta\sum_{i=1}^s(N-i)
=sa+\delta\Bigl(sN-\tfrac{s(s+1)}2\Bigr)
=\frac{s}{N}+\delta\cdot\frac{s(N-s)}2,$$
(the algebra: $sa+\delta(sN-\tfrac{s(s+1)}2)=s(\tfrac1N-\delta\tfrac{N-1}2)
+\delta sN-\delta\tfrac{s(s+1)}2=\tfrac sN+\delta s\bigl(N-\tfrac{N-1}2-
\tfrac{s+1}2\bigr)=\tfrac sN+\delta s\cdot\tfrac{N-s}2$, since
$N-\tfrac{N-1}2-\tfrac{s+1}2=\tfrac{2N-(N-1)-(s+1)}2=\tfrac{N-s}2$).
Equivalently, writing $m=N-s$, the bottom-$m$ sum is
$$\sum_{i=N-m+1}^Np_i(e_0)=\frac mN-\delta\cdot\frac{m(N-m)}2,$$
and the necessary condition is exactly $\dfrac mN-\delta\cdot
\dfrac{m(N-m)}2\ \le\ \tfrac12$.

**Exact `Fraction`-arithmetic verification of this closed form.**
Computed both the closed form and the literal sum $\sum_{i=1}^sp_i(e_0)$
independently (building $e_0$'s coordinates from the certified formula,
not the closed form) for every $n=3,\dots,20$ and every
$s\in\{n-2,n-3,n-4\}\cap[1,N]$: **exact agreement in every one of the
54 instances checked**, confirming the closed form algebraically as well
as numerically.

**Explicit exact results at the round's requested $(n,s)$ pairs.**

| $n$ | $N$ | $s$ | $m=N-s$ | bottom-$m$ sum | vs. $\tfrac12$ | ruled out? |
|---|---|---|---|---|---|---|
| 8 | 9 | 6 | 3 | $484/1533$ | $<1/2$ | no |
| 8 | 9 | 5 | 4 | $1954/4599$ | $<1/2$ | no |
| 8 | 9 | 4 | 5 | $2465/4599$ | $>1/2$ | **YES** |
| 9 | 10 | 7 | 3 | $494/1705$ | $<1/2$ | no |
| 9 | 10 | 6 | 4 | $662/1705$ | $<1/2$ | no |
| 9 | 10 | 5 | 5 | $499/1023$ | $<1/2$ | no |
| 10 | 11 | 8 | 3 | $6009/22517$ | $<1/2$ | no |
| 10 | 11 | 7 | 4 | $8034/22517$ | $<1/2$ | no |
| 10 | 11 | 6 | 5 | $10070/22517$ | $<1/2$ | no |

**One genuine, exact, non-numeric impossibility result:** at $n=8$,
$s=n-4=4$ (i.e. $m=5$ untouched pieces) is **rigorously ruled out** — no
legal response with exactly $4$ active pieces at $e_0(8)$ can ever attain
the exact floor $\tfrac12$, since the bottom-$5$ mass already exceeds
$\tfrac12$ ($2465/4599>1/2$, an exact fraction comparison, not an
approximation), violating the Generalized Mass-Constraint Theorem's
necessary condition. This is new: round 16's float search only reported
"none reached $1/2$ in a quick local search" (a soft, non-conclusive
lead); this round proves one of those cases (n=8, s=4) can **never** reach
it, by a rigorous argument, independent of any search.

**Honest scope: this bound does NOT establish the general $s\ge n-1$
conjecture, and the gap is characterized precisely, not glossed over.**
For every other requested pair ($n=8,s\in\{5,6\}$; $n=9,10$, all three
$s$ values), the bottom-$m$ sum is **below** $\tfrac12$ — i.e. the
necessary condition is **satisfied**, so this bound does **not** rule
these cases out. Moreover this is not a fluke of the specific $n$ chosen:
**asymptotically, for any fixed $m$ (i.e. $s=N-m=n+1-m$ with $m$ held
constant as $n\to\infty$), the bottom-$m$ sum $\tfrac mN-\delta\cdot
\tfrac{m(N-m)}2\to0$ as $N\to\infty$** (first term $\to0$ since $m$ is
fixed and $N\to\infty$; second, subtracted, term is bounded above by
$\delta\cdot\tfrac{mN}2\to0$ since $\delta=\tfrac1{2^N-1}$ decays
exponentially while $mN$ grows only linearly in $N$) — so for every fixed
$m$, once $n$ is large enough, the necessary condition is satisfied and
this bound gives **no obstruction whatsoever** to $s=n+1-m$ (however small
$m$ is, even $m=100$ fixed as $n\to\infty$). The rule-out at $(n,s)=
(8,4)$ is possible only because $m=5$ is already close to $N/2=4.5$ at
this specific small $N=9$ (bottom-$m$ mass is large exactly when $m$ is a
large *fraction* of $N$, roughly $m>N/2$ up to the exponentially small
$\delta$-correction) — **this mechanism inherently cannot reach a
conclusion like "$s\ge n-1$" (equivalently $m\le2$ for all $n$), since
$m\le2$ is a much stronger requirement (a fixed tiny constant) than
"$m\lesssim N/2$"**. Concretely: this theorem proves $s\gtrsim N/2$ is
necessary (a genuinely new, generally-applicable bound, stronger for this
purpose than the restricted round-11 Mass-Constraint's $s>(n+1)/3$ where
it applies), but it is a **fundamentally different, much weaker order of
bound** than the conjectured $s\ge n-1=N-2$, and no refinement of *this
specific mass-counting technique* can close that gap — the technique
only uses total mass, never using how the $m$ untouched values must be
distributed among the active pieces' fragments in more refined ways (e.g.
the round-12 Perfect-Tie-Family's Integer-AltSum argument, which does use
finer index/parity structure and reaches $s=n-1$ exactly, but only for
the pure zero-*additional*-residual sub-family that excludes untouched-
piece ties, per that theorem's own documented scope). Combining the two
techniques (mass-counting here, index/parity-counting there) into a single
argument covering the fully general combined family remains open and is
recorded as the natural next step for whichever round returns to this
question.

**Summary of round 17's honest outcome.** (1) The literal "redo the
float search in exact arithmetic" task is explained as not directly
meaningful, and replaced with something strictly more informative: a
proved, general (not construction-specific) necessary condition. (2) That
condition is applied exactly (not numerically) at the requested $(n,s)$
pairs, yielding one genuine new impossibility result ($n=8,s=4$) and
otherwise confirming (not contradicting) that the condition alone permits
$s=n-2,n-3,n-4$ at $n=8,9,10$ — consistent with (does not refute) the
existing $s=n-1$-necessity conjecture, but does not prove it, and the
asymptotic analysis shows this specific proof technique **structurally
cannot** close the gap to $s=n-1$ on its own. (3) Two new, fully proved,
reusable lemmas are proposed for certification (Even-Multiplicity Equality
Criterion; Generalized Mass-Constraint Theorem) — genuine mathematical
progress even though the headline conjecture ($s\ge n-1$ necessary)
remains open. Status unchanged: `partial`.

## Round 16 update (light dispatch — cross-check only, no new theorem;
honest "no leverage found" on both dispatched items)

**Dispatch this round:** (1) cross-check whether the certified Twin-Anchor
Construction / Perfect-Tie-Family machinery at $e_0$ gives a concrete
"within-branch-tie" data point useful to `global-lp-vertex-sufficiency`'s
open Section 6.3 Σ-shape classification target; (2) record any new numeric
lead, even soft, on the general nonzero-residual fragment-vs-fragment
family (this file's own long-standing open item).

### (1) Cross-check against Section 6.3's within-branch-tie family — genuine analogy, but no correspondence that narrows the open classification

Read `global-lp-vertex-sufficiency.md` Section 4 (the Finite-Cell
Affine-Vertex Reduction and the region-only vertex classification) and
Section 6.3 (the honest diagnosis of the two remaining Σ-shape candidate
families) in full.

**What "within-branch-tie" means there.** Section 6.3 defines $Q$ as the
finite candidate set of points solving some $(k-1)$-subset of the *full*
functional list $L$ (region functionals **and** $\Sigma$-shape
functionals) set to $0$. Within $Q$, the "within-branch-tie" sub-family
is: points $q$ where two coordinates of the *same* optimal-shape response
$y_\sigma(q)$ coincide (a tie **inside** one fixed $\sigma\in\Sigma(n,k)$,
not a tie **between** two different valid shapes $\sigma\ne\tau$, which is
the separate "branch-comparison-boundary" family).

**Genuine structural match, checked directly.** The Twin-Anchor
Construction's optimal response at $e_0$ (`lemmas/twin-anchor-floor-theorem.md`)
is *literally* an instance of a within-shape tie: its $N-1$ pairs
$(p_{N-1},p_{N-1})$, $(p_N,p_N)$, $((N-2)\delta,(N-2)\delta)$, and the
$N-4$ bisection-halves, are all equalities *inside the same single
response* — exactly the phenomenon Section 6.3 describes ("two
coordinates of the same $y_\sigma(q)$ coincide"). So this is a genuine,
concrete, fully worked, exactly-verified example of a within-shape-tie
response — not merely an analogy — and it demonstrates something Section
6.3 does not yet have: a case where the ties are **maximally dense** ($N-1$
independent tied pairs simultaneously, not just one) and the resulting
value is **not merely $\le c(n)$ but exactly the universal floor $1/2$** —
i.e., ties of this density are fully compatible with (indeed forced by,
via Even-Block-Neutrality) hitting the best possible value, not an
obstruction.

**Why this does NOT narrow Section 6.3's open classification, checked
explicitly.** Three gaps between the two objects, checked one at a time:

- **$e_0$ is a region-only vertex, not confirmed to be a member of $Q$.**
  $e_0$ is defined and classified (`global-lp-vertex-sufficiency.md`
  Section 4.1–4.3) as a vertex of the *region-only* sub-polytope
  $\overline{B(n)}$ (all slacks $g_i=0$, pinned by $n$ of the region's
  $n+2$ functionals) — it is **not** derived as a solution of a
  $(k-1)$-subset drawn from the full list $L$ including $\Sigma$-shape
  functionals. Whether $e_0$ *also* happens to lie in $Q$ (i.e., whether
  it is pinned by an appropriate $\Sigma$-shape-functional subset, not
  just region functionals) is not established in either file. Absent
  that check, $e_0$'s tie structure cannot be asserted to be a genuine
  *instance* of a $Q$-point in Section 6.3's still-open residual — it is
  a tie phenomenon on a **different, already-fully-classified** point,
  reached by a completely different route (the region-vertex
  classification of Section 4, not the $\Sigma$-shape-arrangement route
  of Section 6).
- **The tie mechanism is AP-structure-specific, not generic.** Every tie
  in the Twin-Anchor Construction relies on $e_0$'s exact arithmetic-
  progression coordinates ($p_i(e_0)=a+(N-i)\delta$) — e.g. the identity
  $p_1-p_{N-1}=p_2-p_N=(N-2)\delta$ is a one-line AP cancellation. A
  generic point of $Q$ (pinned by $\Sigma$-shape-equality functionals, not
  by the region's own AP-forcing constraints) has no reason to carry this
  AP structure, so the specific algebraic identities that make the
  Twin-Anchor ties work do not transfer.
- **Section 6.3's obstruction is about curvature of $\mathrm{OddSum}$
  restricted to a fixed-allocation polytope, not about whether ties can
  occur.** Re-reading Section 6.3's own diagnosis: the blocking issue is
  that $\mathrm{OddSum}(x)$ (varying one split fraction $x$) is neither
  globally convex nor globally concave, so no uniform LP-duality
  certificate applies cell-independently. The Twin-Anchor data point
  doesn't bear on this curvature question at all — it exhibits one
  *optimal* configuration at one *fixed* point, not the shape of
  $\mathrm{OddSum}$ as a function varies across a fixed-allocation slice
  approaching a tie.

**Conclusion of the cross-check.** Confirmed a genuine structural analogy
(the two objects are literally the same kind of phenomenon — within-shape
fragment ties) but **no correspondence that narrows or resolves**
Section 6.3's open classification: $e_0$'s membership in $Q$ is
unverified, and even if it were confirmed, the specific mechanism
(AP-cancellation) is special to $e_0$'s coordinates and does not suggest a
route to the *generic* within-branch-tie case Section 6.3 needs. Honest
outcome, as the dispatch anticipated: **no new leverage found**; this is
recorded so neither approach re-attempts the same cross-check.

### (2) Soft numeric lead on the general nonzero-residual family — negative/consistent, not conclusive

Quick check (`scipy.optimize.minimize`, Nelder–Mead, box-constrained to
keep fragments strictly positive/legal) at $n=8,10$, active-set sizes
$s=n-2,n-3,n-4$ (strictly smaller than the $s=n-1$ the certified
Chain-Correction Hybrid Construction needs), several random active-set
choices and random restarts each:

```
n=8  s=6  best OddSum ≈ 0.50294  (untouched pieces {3,4,6})
n=8  s=5  best OddSum ≈ 0.50196  (untouched {4,5,7,8})
n=8  s=4  best OddSum ≈ 0.50196  (untouched {0,2,3,5,7})
n=10 s=8  best OddSum ≈ 0.50098  (untouched {1,8,10})
n=10 s=7  best OddSum ≈ 0.50122  (untouched {3,4,7,10})
n=10 s=6  best OddSum ≈ 0.50074  (untouched {0,1,2,4,5})
```

None reaches $1/2$ exactly in this quick local search (all strictly
above, by margins from $\approx7\times10^{-4}$ to $\approx3\times10^{-3}$,
shrinking as $s$ grows toward $n-1$, consistent with the pattern that
larger $s$ gets closer). This is a **soft, non-conclusive lead**
(Nelder–Mead is a local optimizer with no exhaustiveness guarantee, and
only a handful of active-set choices per $(n,s)$ were tried, not all
$\binom{N}{s}$) but it is directionally consistent with, and does not
contradict, the existing open conjecture recorded in this file's round-14
section: that $s=n-1$ may be genuinely necessary (not just sufficient)
for the Chain-Correction mechanism to reach the exact floor $1/2$ at
$e_0$. **Not proposed as a proof or even a confident conjecture** — filed
as a soft data point for whichever future round attempts the general
$s<n-1$ question.

**A pitfall found and worth flagging explicitly for future numeric
checks on this object:** an unconstrained (no bounds) first pass of the
same search produced OddSum values *below* $1/2$ (e.g. $\approx0.493$ at
$n=8,s=6$), which would contradict the certified universal floor
$\mathrm{OddSum}\ge\mathrm{sum}(M)/2$. Diagnosed immediately: this is an
artifact of the optimizer wandering into **illegal** negative-valued
"fragments" (the floor's proof needs every multiset element $\ge0$, since
the argument bounds only the *paired* differences, not an unpaired
trailing term of a multiset with mixed signs) — not a genuine violation.
Re-running with box constraints $x_i\in(0,p_i)$ enforced (legal fragments
only) restored consistency with the floor in every trial (all results
$\ge1/2$, as shown above). Recorded here so no future round mistakes an
unconstrained-optimizer artifact below $1/2$ for a counterexample to the
certified floor theorems.

### Consequences

Both dispatched items are now closed **as light cross-checks**, honestly:
(1) a genuine structural analogy exists but does not narrow the sibling's
open classification (documented above so it is not re-attempted); (2) a
soft, non-conclusive numeric lead supports (does not prove) the existing
$s=n-1$-necessity conjecture, plus a documented pitfall for future
numeric work on this object. No new theorem, no new certified lemma, no
change to Status (`partial`, unchanged from round 15) — as the dispatch
anticipated for this round.

## Round 15 update (read this first — the Chain-Correction Floor Theorem
is extended, unconditionally and with a SIMPLER proof, to every $n\ge3$,
fully closing the round's dispatched $n=3,4,5$ gap; also confirms the
round's cross-validation duty raises no conflict with the sibling
approach's fresh fragment-tying findings)

**Dispatch this round:** (1) extend the certified Chain-Correction Floor
Theorem (currently $n\ge6$ only) to $n=3,4,5$; (2) cross-validate against
`global-lp-vertex-sufficiency`'s fresh fragment-tying numerics
(`/tmp/round-15/math-explorer-fragtie.md`), checking this construction
does not secretly rely on any assumption (e.g. descending-chain shape)
that round found broken.

**Finding: a strictly simpler, uniform construction — the
"Twin-Anchor Construction" — achieves $\mathrm{OddSum}(M)=\tfrac12$
exactly at $e_0$ for EVERY $n\ge3$ (not just $n\ge6$), using exactly
$n-1$ cuts, with NO positivity side-condition at all** (the old
Chain-Correction construction needed $a>2\delta$, proved only for
$n\ge6$ by induction; this construction needs only $a>0,\delta>0$, true
by definition of $e_0$ as an interior point of the simplex, for every
$n$). This fully answers the round's target (1) — $n=3,4,5$ are closed,
not left open — and in fact supersedes the $n\ge6$ case of the certified
theorem with a cleaner, condition-free proof, unifying what were
previously two separate constructions (Chain-Correction for $n\ge6$, and
whatever ad hoc argument would have been needed for $n=3,4,5$) into one.

### The Twin-Anchor Construction

**Setup (same certified coordinates as before).** $N:=n+1$,
$\delta:=\gamma(n)=1/(2^N-1)$, $a:=p_N(e_0)>0$ (the smallest piece,
positive since $e_0$ lies in the interior of the simplex — every
coordinate of a valid partition point is strictly positive, certified
`lemmas/finite-cell-vertex-reduction-and-region-classification.md`), so
$p_i(e_0)=a+(N-i)\delta$ for $i=1,\dots,N$, an exact AP with common
difference $\delta>0$.

**Construction (valid for every $n\ge3$, i.e. $N\ge4$).**
- **Piece $1$** ($=a+(N-1)\delta$): split into
  $\bigl(p_{N-1},\ (N-2)\delta\bigr)$, where $p_{N-1}=a+\delta$.
- **Piece $2$** ($=a+(N-2)\delta$): split into
  $\bigl(p_N,\ (N-2)\delta\bigr)$, where $p_N=a$.
- **Every piece $j=3,4,\dots,N-2$** (this range is empty exactly when
  $N\le5$, i.e. $n\le4$; nonempty for $n\ge5$): split into two exactly
  equal halves $(p_j/2,\ p_j/2)$.
- **Pieces $N-1,N$** are left untouched.

This uses exactly $1+1+(N-4)^+=N-2=n-1$ cuts when $N\ge5$, and exactly
$2=n-1$ cuts when $N=4$ (the bisection range is empty) — uniformly
$n-1\le n$ cuts, legal, for every $n\ge3$.

**Key algebraic identity (exact, no induction, no side condition).**
Piece $1$'s second fragment is
$p_1-p_{N-1}=\bigl(a+(N-1)\delta\bigr)-(a+\delta)=(N-2)\delta$, and piece
$2$'s second fragment is
$p_2-p_N=\bigl(a+(N-2)\delta\bigr)-a=(N-2)\delta$ — **identically equal**
for every $N$, a one-line cancellation (no induction, no case split, no
$N$-dependent inequality needed — contrast with the old construction's
piece-$3$/piece-$5$ identity, which needed both $u_1,u_2$ to be defined
and $N\ge7$ for the relevant pieces to exist).

**Positivity (trivial, no side condition).** Every fragment is one of:
$p_{N-1}=a+\delta>0$, $p_N=a>0$ (both since $a>0,\delta>0$), the shared
value $(N-2)\delta>0$ (since $N\ge4\Rightarrow N-2\ge2>0$ and $\delta>0$),
or a half $p_j/2>0$ of an already-positive piece. **No inequality
between $a$ and $\delta$ is ever needed** — unlike the old
Chain-Correction construction's requirement $a>2\delta$ (which needed the
induction $(n+1)(n+4)<2^{n+2}-2$, valid only for $n\ge6$), this
construction's positivity holds unconditionally for every $n\ge3$, which
is exactly why it closes the small-$n$ cases the old construction could
not reach.

**Theorem (Twin-Anchor Floor Theorem).** For every $n\ge3$, the
construction above is a legal response at $e_0$ (all fragments positive,
$n-1\le n$ cuts used), and $\mathrm{OddSum}(M)=\tfrac12$ exactly — the
universal absolute floor for any legal response at any partition.

*Proof.* The resulting multiset has exactly $2N-2$ elements (four
fragments from pieces $1,2$; two untouched pieces $N-1,N$; two halves
each from pieces $3,\dots,N-2$, contributing $2(N-4)$ elements when
$N\ge5$, none when $N=4$ — total $4+2+2(N-4)^+=2N-2$ in every case, matching
$N+s=N+(N-2)$). Group them into $N-1$ pairs, each pair consisting of two
elements of **equal value**:
1. $\bigl(p_{N-1},\ p_{N-1}\bigr)$ — the untouched piece $N-1$ paired
   with piece $1$'s first fragment (equal by construction).
2. $\bigl(p_N,\ p_N\bigr)$ — the untouched piece $N$ paired with piece
   $2$'s first fragment (equal by construction).
3. $\bigl((N-2)\delta,\ (N-2)\delta\bigr)$ — piece $1$'s and piece $2$'s
   second fragments, equal by the Key Algebraic Identity above.
4. For each $j=3,\dots,N-2$: $(p_j/2,\ p_j/2)$ — piece $j$'s two halves.

Every one of the $2N-2$ elements belongs to exactly one of these $N-1$
groups, each of size exactly $2$ with equal values. By the certified
**Even-Block-Neutrality mechanism** (used identically in the certified
Chain-Correction Floor Theorem, `lemmas/chain-correction-floor-theorem.md`:
in the descending sort of $M$, a block of $2$ equal values occupies $2$
consecutive ranks — one odd, one even — regardless of how it interleaves
with other groups, since inserting/removing an even-sized block shifts
every other element's rank by an even number, preserving parity), every
group contributes exactly $0$ to $\mathrm{AltSum}(M)$. Hence
$\mathrm{AltSum}(M)=0$ exactly, so
$\mathrm{OddSum}(M)=\tfrac12(\mathrm{sum}(M)+\mathrm{AltSum}(M))=
\tfrac12(1+0)=\tfrac12$. $\blacksquare$

**Independent verification (exact `Fraction` arithmetic, $n=3,\dots,40$,
38 instances).** Built the literal fragment multiset from the
construction (not a closed-form shortcut) for every $n=3,\dots,40$:
confirmed every fragment strictly positive, total mass exactly $1$
(`Fraction(1,1)`), cuts used exactly $n-1$ (legal, $\le n$), and
$\mathrm{AltSum}=0$ exactly — **zero deviation in all 38 cases**,
including a full re-check of $n=3,4,5$ specifically (the round's target)
and $n=6,\dots,40$ (re-confirming, by an independent and simpler
construction, the previously-certified $n\ge6$ range).

**Explicit worked example, $n=3$ ($N=4$).** $\delta=1/15$, $a=3/20$.
$p_1=7/20,p_2=17/60,p_3=13/60,p_4=a=3/20=9/60$. Construction: piece $1$
splits as $(p_3,\,2\delta)=(13/60,\,8/60)$ (check: $7/20=21/60=13/60+8/60$
✓); piece $2$ splits as $(p_4,\,2\delta)=(9/60,\,8/60)$ (check:
$17/60=9/60+8/60$ ✓); pieces $3,4$ untouched. $M=\{13/60,8/60,9/60,8/60,
13/60,9/60\}$ — sorted descending: $13/60,13/60,9/60,9/60,8/60,8/60$.
$\mathrm{AltSum}=13/60-13/60+9/60-9/60+8/60-8/60=0$. $\mathrm{OddSum}=
\tfrac12(1+0)=\tfrac12$. Matches the theorem and the general-$N$
verification exactly.

### Cross-validation against this round's fragment-tying numerics
(dispatch item 2)

`/tmp/round-15/math-explorer-fragtie.md`'s new negative finding (Finding
3: the general-$p$ descending fragment chain family fails at fresh random
balanced-region points, $2/20$ at $n=3$, $4/12$ at $n=4$, and the
follow-up conjecture that $\sigma^*(p)$ does not always have
descending-chain shape) is about a **structurally different object**
from the Twin-Anchor Construction (and from the pre-existing
Chain-Correction construction), on **three counts**, checked explicitly:

1. **Scope: single fixed vertex vs. general $p$.** The Twin-Anchor
   Construction is evaluated at the single, fixed, already-classified
   region vertex $e_0$ (a specific point, not a family ranging over the
   balanced region). The fragtie explorer's descending-chain family is
   explicitly a general-$p$ construction, tested by sampling *fresh
   random points of the balanced region* — a different, much larger
   parameter space. Nothing in this round's construction requires or
   assumes that a descending-chain response is optimal (or even legal)
   at any point other than $e_0$ itself.
2. **Shape: fixed pairing graph vs. searched-over chain topology.** The
   fragtie explorer's family is a *search* over subset choices, linear
   orders, and a free continuous parameter $x$ (via the
   Singleton-Interleaving Lemma's closed form) — i.e. it explicitly
   allows the chain's shape and length to vary and optimizes over that
   space. The Twin-Anchor Construction is a single, fully explicit,
   non-searched pairing (piece $1\leftrightarrow$ piece $N-1$, piece
   $2\leftrightarrow$ piece $N$, plus self-bisections) — it is not a
   member of the searched family at all (it is not even a "chain" in
   the propagating sense: pieces $1,2$ tie *directly* to untouched
   pieces $N-1,N$, with no propagated leftover threading through a third
   piece, unlike both the descending-chain family and the old
   Chain-Correction construction's piece-$3$/piece-$5$ relay). Hence the
   fragtie explorer's finding that "the descending-chain family, searched
   exhaustively, is not always optimal at general $p$" says nothing about
   whether this specific, different, fixed pairing succeeds at the
   specific point $e_0$ — which this round establishes directly and
   exactly, by algebra, not by search.
3. **No reliance on any unproven structural assumption.** The fragtie
   explorer's own diagnosis is that the failure mode is "$\sigma^*(p)$
   does not always have descending-chain shape" — i.e. a claim about
   which construction family contains the *true optimum* at a *general*
   $p$. The Twin-Anchor Construction never claims to find the true
   optimum at a general $p$; it proves a specific point ($e_0$) attains
   the specific value $1/2$ (the universal floor, hence automatically
   optimal there, with no further search needed — nothing can beat the
   floor). So there is no "shape assumption" for the fragtie finding to
   undermine: the Even-Block-Neutrality pairing argument used here is a
   direct verification of optimality-by-floor-attainment, not an
   assumption that some *family* contains the optimum.

**Conclusion of the cross-validation.** No conflict, and no hidden shared
assumption: this round's $n<6$ closure is independent of, and immune to,
the sibling approach's fresh negative finding on the general-$p$
descending-chain family. The two results are about disjoint objects (a
fixed-point exact construction here; a general-$p$ searched family
there) and neither result's proof invokes the other's premises.

### Consequences and honest scope

**(1) Dispatch item 1 (extend to $n<6$) is fully closed**, and in fact
strengthened beyond what was asked: the Twin-Anchor Floor Theorem covers
every $n\ge3$ in one uniform statement, with a strictly simpler proof
(no induction, no side condition) than the previously-certified
Chain-Correction Floor Theorem's $n\ge6$ restriction. **Proposed for
certification below**, either as a standalone new lemma or as a
strengthening/replacement of the existing
`lemmas/chain-correction-floor-theorem.md` (both constructions prove the
same conclusion, $V(e_0)=\tfrac12$ for the covered range; this round's
construction's range strictly contains and simplifies the old one's, so
a natural resolution is for the reviewer to supersede the old certified
file with this one, or keep both — the reviewer's call, not
self-certified here).

**(2) $n=2$ checked and confirmed genuinely out of scope (not
overlooked).** At $n=2$ ($N=3$), $e_0=(10/21,1/3,4/21)$ (all positive,
still a valid vertex), but the parity/budget argument that makes the
construction work breaks down: the pairing needs an odd number of split
pieces $s\in\{1,3\}$ (since $N=3$ is odd, $N+s$ must be even), $s=1$
fails combinatorially (the two remaining untouched pieces are distinct
AP values, cannot pair with each other), and $s=3$ needs $3$ cuts,
exceeding the budget $n=2$. So the Twin-Anchor mechanism genuinely
cannot reach the floor at $n=2$ within budget — this is a real boundary,
not an oversight, checked explicitly by direct computation
(`Fraction` arithmetic) this round. $n=2$ is not part of this round's
dispatch and is not claimed to be closed.

**(3) What remains open (unchanged from round 14, restated here for
completeness).** Whether a strictly smaller active-set size $s<n-1$
(more untouched pieces) can also reach the floor at $e_0$ remains open
(unreliable exploratory numeric leads only, not verified). The fully
general nonzero-residual fragment-vs-fragment trade-off at arbitrary $s$
remains open. This round does not touch either.

## Round 14 update (read this first — a new, fully proved exact theorem:
the general nonzero-residual family reaches the *absolute floor* at
$e_0$, using the same active-set size $s=n-1$ that the Perfect-Tie
family needed just to *tie* $c(n)$)

**Dispatch this round:** characterize, quantitatively, how a nonzero
residual (allowing fragment-vs-fragment ties that also draw on whole
untouched pieces — i.e. the fully general "hybrid" family, not the
restricted zero-residual Perfect-Tie family) trades off against the
required active-set size $s$ at $e_0$, using exact-arithmetic
active-set enumeration (kept deliberately distinct from
`global-lp-vertex-sufficiency`'s LP/hyperplane numeric search this
round).

**Finding, fully proved (not just a numeric hint): a new "Chain-Correction
Hybrid Construction" achieves $\mathrm{OddSum}(M)=\tfrac12$ *exactly* —
the universal absolute floor for *any* legal response, at *any*
partition — at $e_0$, for every $n\ge6$, using exactly $s=n-1$ active
pieces (leaving only $2$ untouched, the same active-set size the
certified Perfect-Tie-Family Theorem needed merely to *tie* $c(n)$).**
This directly and decisively answers the round's question: allowing
nonzero residual does not just modestly help (as the round-12 numeric
spot check at $n=6,s=3$ suggested, $\approx0.5046$ vs. Perfect-Tie's
$\approx0.5079$, still short of $c(6)\approx0.5039$) — at the *right*
value of $s$ ($s=n-1$), it can be pushed all the way to the theoretical
minimum possible for **any** response whatsoever. Full construction,
proof, and exact verification (`Fraction` arithmetic, $n=6,\dots,20$,
zero deviation) in the new section below.

### The Chain-Correction Hybrid Construction

**Setup.** At $e_0$ (certified coordinates,
`lemmas/finite-cell-vertex-reduction-and-region-classification.md`),
write $N:=n+1$, $\delta:=\gamma(n)=1/(2^{N}-1)$ (the common AP
difference), $a:=p_N(e_0)$ (the smallest piece), so
$p_i(e_0)=a+(N-i)\delta$ for $i=1,\dots,N$, an exact AP.

**Active set.** $S=\{1,2,\dots,N-2\}$ (all pieces except the smallest
two), $|S|=N-2=n-1$. Untouched: $p_{N-1}(e_0)=a+\delta$,
$p_N(e_0)=a$.

**The construction (each active piece split into exactly $2$ fragments,
$1$ cut each, $n-1$ cuts total — within the $\le n$ budget).**
- **Piece $1$** ($=a+(N-1)\delta$): split into $\bigl(a,\ (N-1)\delta\bigr)$.
  Write $u_1:=(N-1)\delta$ for the second fragment.
- **Piece $2$** ($=a+(N-2)\delta$): split into
  $\bigl(a+\delta,\ (N-3)\delta\bigr)$. Write $u_2:=(N-3)\delta$.
- **Piece $3$** ($=a+(N-3)\delta$): split into $(u_1,\ a-2\delta)$.
- **Piece $5$** ($=a+(N-5)\delta$): split into $(u_2,\ a-2\delta)$.
- **Piece $4$** ($=a+(N-4)\delta$): split into two exactly equal halves,
  $\bigl(\tfrac{a+(N-4)\delta}2,\ \tfrac{a+(N-4)\delta}2\bigr)$.
- **Every piece $j=6,7,\dots,N-2$** (this range is empty when $N\le7$,
  i.e. $n\le6$; nonempty for $n\ge7$): split into two exactly equal
  halves $(p_j/2,\ p_j/2)$.

**Lemma (the key algebraic identity: piece $3$'s and piece $5$'s second
fragments coincide).** Piece $3$'s second fragment is $p_3-u_1=
\bigl(a+(N-3)\delta\bigr)-(N-1)\delta=a-2\delta$, and piece $5$'s second
fragment is $p_5-u_2=\bigl(a+(N-5)\delta\bigr)-(N-3)\delta=a-2\delta$ —
**identically equal**, for *every* $N$ (the $N$-dependence cancels
exactly in each case). This is a direct algebraic computation, not an
approximation: both simplify to the single constant $a-2\delta$
regardless of $N$.

**Positivity Lemma (all fragments strictly positive iff $a>2\delta$,
which holds for every $n\ge6$).** Every fragment above is manifestly
positive except possibly $u_1,u_2$ (positive since $N\ge7\Rightarrow
N-1,N-3>0$) and the shared value $a-2\delta$ (positive iff $a>2\delta$).
$a>2\delta$ is equivalent (clearing denominators in $a=p_N(e_0)=
\frac{2-n(n+1)\gamma(n)}{2(n+1)}$, $\gamma(n)=\delta$, certified formula
from `lemmas/finite-cell-vertex-reduction-and-region-classification.md`)
to $(n+1)(n+4)<2^{n+2}-2$.
*Proof of $(n+1)(n+4)<2^{n+2}-2$ for all $n\ge6$, by induction.*
Base case $n=6$: $7\cdot10=70<2^8-2=254$. ✓.
Inductive step: assume $(n+1)(n+4)<2^{n+2}-2$ for some $n\ge6$. Then
$(n+2)(n+5)=(n+1)(n+4)+(2n+6)<(2^{n+2}-2)+(2n+6)$. Since $n\ge6
\Rightarrow2^{n+2}\ge256>2n+6$ (and the gap $2^{n+2}-(2n+6)$ only grows
as $n$ increases, since $2^{n+2}$ at least doubles per step while
$2n+6$ grows by only $2$), $(2^{n+2}-2)+(2n+6)<(2^{n+2}-2)+2^{n+2}=
2^{n+3}-2$. So $(n+2)(n+5)<2^{n+3}-2$, completing the induction.
$\blacksquare$

**Theorem (Chain-Correction Floor Theorem).** For every $n\ge6$, the
construction above is a legal response at $e_0$ (all fragments
positive, $n-1\le n$ cuts used), and
$$\mathrm{OddSum}(M)=\frac12$$
**exactly** — the universal absolute minimum possible for *any* legal
multiset of total mass $1$ (immediate from the certified OddSum Floor
Lemma, $\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$, since
$\mathrm{AltSum}$ of a descending-sorted multiset is a sum of
consecutive-pair differences $v_{2j-1}-v_{2j}\ge0$, plus a
nonnegative odd leftover, hence $\ge0$ always).

*Proof.* List the resulting $2(N-2)+2=2N-2$ fragments and group them
into $N-1$ pairs, each pair having two members of **equal value**:
1. $(p_N(e_0),\ a)$ — the untouched piece $p_N(e_0)=a$ paired with
   piece $1$'s first fragment, value $a$.
2. $(p_{N-1}(e_0),\ a+\delta)$ — the untouched piece $p_{N-1}(e_0)=
   a+\delta$ paired with piece $2$'s first fragment, value $a+\delta$.
3. $(u_1,\ u_1)$ — piece $1$'s second fragment paired with piece $3$'s
   first fragment, both value $u_1=(N-1)\delta$.
4. $(u_2,\ u_2)$ — piece $2$'s second fragment paired with piece $5$'s
   first fragment, both value $u_2=(N-3)\delta$.
5. $(a-2\delta,\ a-2\delta)$ — piece $3$'s and piece $5$'s second
   fragments, equal by the Key Algebraic Identity above.
6. $\bigl(\tfrac{p_4}2,\tfrac{p_4}2\bigr)$ — piece $4$'s two halves.
7. For each $j=6,\dots,N-2$: $(p_j/2,\ p_j/2)$ — piece $j$'s two
   halves.

Every one of these $N-1$ groups consists of exactly $2$ equal-valued
elements. By the certified **Even-Block-Neutrality Lemma** (general
form, $t=1$ case; already certified as part of
`lemmas/window-reduction-theorem-and-elementwise-monotonicity.md`'s
ancestor material and re-derived independently here): in the
descending sort of the full multiset $M$, any group of exactly $2t$
elements sharing one common value occupies $2t$ consecutive ranks
(nothing of a *different* value can separate two copies of the *same*
value in a sort), of which exactly $t$ are odd-ranked and $t$
even-ranked, so the group contributes exactly $0$ to
$\mathrm{AltSum}(M)$ regardless of where the block sits or how the
different groups interleave with each other (inserting/removing a
block of even size shifts every other element's rank by an even
number, preserving parity, hence not affecting any other group's own
internal even-odd balance either — this holds even if two *different*
groups happen to coincide in value, since they simply merge into one
larger even block, still contributing $0$ by the same argument with a
larger $t$). Every one of the $2N-2$ fragments belongs to exactly one
of the $N-1$ groups above (each fragment listed exactly once: pieces
$1,2,3,5$ contribute one fragment each to two different pair-groups;
pieces $4,6,\dots,N-2$ contribute both their fragments to their own
single pair-group; the two untouched pieces each contribute their one
copy to a pair-group). Hence $\mathrm{AltSum}(M)=0$ exactly, so
$\mathrm{OddSum}(M)=\tfrac12(\mathrm{sum}(M)+\mathrm{AltSum}(M))=
\tfrac12(1+0)=\tfrac12$. $\blacksquare$

**Independent verification (exact `Fraction` arithmetic, $n=6,7,8,9,
10,12,15,20$, 8 instances).** Built the literal fragment multiset from
the construction above (not the closed-form shortcut), confirmed every
fragment strictly positive, confirmed the total sums to exactly $1$
(`Fraction(1,1)`) in every instance, computed $\mathrm{AltSum}$ by
direct sort-and-alternate on the literal multiset: **exactly $0$ in
all $8$ cases**, giving $\mathrm{OddSum}=1/2$ exactly in all $8$
cases — matching the Theorem digit-for-digit (as exact fractions, not
approximations). Also independently confirmed the Positivity Lemma's
condition $a>2\delta$ holds in all $8$ instances by direct fraction
comparison.

### Consequences and honest scope

**(1) Decisive answer to this round's dispatch question.** At the
active-set size $s=n-1$ (the size the Perfect-Tie-Family Theorem showed
was necessary *and* just-barely-sufficient to tie $c(n)$ within the
zero-residual family), allowing residual in the fully general sense
(fragments tied to whole untouched pieces **and** to each other, not
just one or the other) does not merely help modestly: it reaches the
absolute floor $1/2$, strictly below $c(n)$ by a fixed positive margin
$c(n)-\tfrac12=\tfrac1{2(2^{n+1}-1)}\to0$ (this margin itself shrinks,
but the achieved value never needs to be that close to $c(n)$ — it is
*always* exactly $1/2$, regardless of $n$). This is a clean,
proved, quantitative answer, not merely a numeric hint.

**(2) A likely correction to the existing vertex-classification
record — flagged honestly, not asserted as this approach's own
overclaim.** `current.md` and
`results/imo-2026-03/approaches/global-lp-vertex-sufficiency.md`
(Section 4.3) state "$V(e_0)=c(n)$ exactly," established there via the
$k$-Anchor-Merge construction (which gives $\mathrm{OddSum}=c(n)$ for
an *odd* number of AP-pairs, the case realized at $e_0$). That
construction is a valid **upper bound** witness
($V(e_0)\le c(n)$), but this round's Chain-Correction Floor Theorem
exhibits a *different*, equally legal response at the same $e_0$
achieving $\mathrm{OddSum}=\tfrac12<c(n)$ for every $n\ge6$ — hence (by
the universal Floor Lemma, $\mathrm{OddSum}\ge\tfrac12$ always) the
**true value is $V(e_0)=\tfrac12$ exactly, for every $n\ge6$, not
$c(n)$.** This does **not** threaten the overall upper-bound program
(the actual target is $V(p)\le c(n)$ for *every* $p$; finding
$V(e_0)$ is *even smaller* than previously recorded is strictly good
news, not a gap) — but it is a genuine correction to a specific
factual claim recorded elsewhere, and is flagged here explicitly so
the next review/round can reconcile it (e.g. by scoping the "$V(e_0)=
c(n)$" language in `global-lp-vertex-sufficiency.md`/`current.md` to
"the $k$-Anchor-Merge construction achieves exactly $c(n)$," which
remains true, rather than "the true minimax value at $e_0$ is $c(n)$,"
which this round's finding shows is false for $n\ge6$). No change was
made to any other approach's file, per the file-ownership rule; this
is reported for the reviewer to act on.

**(3) What remains open (the trade-off's finer structure).** This
round's construction fixes $s=n-1$ (leaving exactly $m=2$ untouched)
and proves the floor is reached *there*. It does **not** establish:
(a) whether a strictly *smaller* $s$ (more untouched pieces, $m\ge3$)
can also reach the floor $1/2$ at $e_0$ — an exploratory (unreliable,
float-only, local-optimizer) scan this round found candidate values
close to but not conclusively at $1/2$ for $m=3,\dots,6$ at
$n=8,10,12$ (e.g. $n=8,m=4$: numeric best $\approx0.5002$, tantalizingly
close but not verified exact, and the optimizer's local-minimum issues
mean this is **not** reported as an established fact, only as a lead
for a future round — extending the Chain-Correction mechanism to more
than $2$ untouched pieces, with more correction pieces per untouched
target, is the natural next step, not yet attempted); (b) the case
$n=2,3,4,5$ (too few active pieces for this specific construction,
which needs $N-2\ge5$, i.e. $n\ge6$) — whether some other bounded
construction reaches the floor there is untested this round; (c) more
generally, no claim is made here about whether a fixed $s_0$
independent of $n$ can reach the floor (this round's $s=n-1$ still
grows with $n$, same order as the already-known constructions) — the
finding is a **qualitative strengthening at the known threshold
$s=n-1$** (floor, not just $c(n)$), not a **reduction of the required
$s$** below what was already known to suffice.

## Round 12 update (read this first — a genuine, complete negative
theorem for the "perfect-tie" fragment-vs-fragment/self-tie sub-family at
$e_0$, honestly scoped as not covering the fully general family)

**Dispatch this round:** attempt one focused, *proved* (not searched)
fragment-vs-fragment tying construction at the hard vertex $e_0$, per the
round-11 Mass-Constraint Theorem's own scope note that it does not cover
ties among fragments of *different* split pieces (only ties to a whole
untouched piece). The round-12 explorer's numeric stress test found a
soft negative signal (minimal clearing $s$ grows with $n$: $3$ at $n=6$,
$\ge5$ at $n=8$).

**Finding: a new, general-purpose Integer-Alternating-Sum Lower Bound
Lemma, applied to give a complete, exact characterization of the
"perfect-tie" sub-family at $e_0$ — proving it needs $s=n-1$ (unbounded,
not any fixed $s_0$) merely to *tie* $c(n)$, and can never beat it
strictly.** Full statement and proof in the new section "Round 12: the
Perfect-Tie-Family Exact Characterization at $e_0$" below. Summary:

- **Setup.** "Perfect-tie" means: split pieces in a set $S$ ($|S|=s$),
  and pair up *every* resulting fragment into an even-multiplicity
  equal-value block using only fragments of $S$ (covers both self-tie —
  bisecting one piece into two equal halves — and genuine
  fragment-vs-fragment ties across two or more *different* split pieces;
  excludes only the round-11 family, tying a fragment to a whole
  *untouched* piece). By the certified Singleton-Interleaving Lemma
  (Theorem 9), this gives an **exact** identity
  $\mathrm{OddSum}(M)=\tfrac12+\tfrac12\mathrm{AltSum}(U)$, where $U$ is
  simply the raw untouched-piece set — no dependence on the internal
  tying pattern, only on which pieces are left untouched.
- **New tool (Integer-Alternating-Sum Lower Bound Lemma, elementary,
  fully general, proved from scratch).** For any $m$ distinct nonnegative
  integers, $\mathrm{AltSum}\ge\lfloor m/2\rfloor$ (consecutive-pair
  differences are each $\ge1$). Applied to $e_0$'s AP index structure,
  this pins down $\mathrm{AltSum}(U)$ *exactly* (not just a bound) at its
  best achievable value for each parity of $|U|=n+1-s$.
- **Consequence, verified in exact `Fraction` arithmetic for
  $n=2,\dots,14$ (13/13 exact matches, both the general formula and the
  brute-force-over-all-active-sets minimum), and proved in closed form
  for every $n$:** the best this entire family can ever do is **exactly**
  $c(n)$ (never strictly below), attained **only** at $s=n-1$ (leaving
  exactly $2$ pieces untouched); every $s<n-1$ fails (exceeds $c(n)$,
  provably, both for the favorable parity of $|U|$ and — even more
  badly — the unfavorable parity, where an unavoidable $\Theta(1/n)$
  penalty term appears). In particular **no fixed $s_0$ (independent of
  $n$) ever suffices** for this family — a clean, complete,
  unconditionally proved negative result, structurally different from
  (not a restatement of) the round-11 Mass-Constraint Theorem, since it
  covers a materially different construction family (no untouched-piece
  mass is ever consumed as a tie target) via a different proof technique
  (an integer combinatorics lemma, not a mass-summation inequality).
- **Honest scope (what this does *not* prove).** This closes only the
  "perfect-tie" (zero-residual) sub-family. A direct numerical check this
  round (`scipy.optimize`, unrestricted fragment values, not just perfect
  ties) found that allowing a genuine nonzero residual **does** improve
  on the perfect-tie optimum (e.g. at $n=6,s=3$: perfect-tie’s exact
  optimum is $\approx0.5079$, but an unrestricted numerical search with
  the same $s=3$ found $\approx0.5046$, still short of $c(6)\approx
  0.5039$) — so bounded-$s_0$ sufficiency for the **fully general**
  fragment-vs-fragment family (nonzero residuals allowed) remains open,
  consistent with (and now more precisely diagnosed than) the round-12
  explorer's own numeric finding. **This round does not close that fully
  general question**, but it does rule out, completely and rigorously,
  the natural "maximally efficient" special case of it, and gives a
  reusable general-purpose tool (the Integer-AltSum Lower Bound Lemma)
  for any future attempt at the general case.

## Round 11 update (read this first — clean negative result on the
requested generalization, plus a new exact positive byproduct)

**Dispatch this round:** test whether the Multi-Piece Sufficiency
construction's mechanism (Even-Block-Neutrality, splitting most landmarks
of a balanced partition, using the full cut budget) generalizes past
AP-structured (triangular-family) landmarks to feed
`global-lp-vertex-sufficiency`'s Σ-shape work — flagged by the outliner as
a long shot given round 10's negative Nelder-Mead numeric check against
LB's own geometric partition.

**Finding 1 (clean negative, now with exact arithmetic, not just
numerics): the direct transplant of the round-10 construction fails
badly at LB's geometric partition, and increasingly so as $n$ grows.**
Directly generalizing round 10's construction pattern (split the top two
landmarks with a top-pair/$\varepsilon$-tail trick, split every middle
landmark into two exactly equal halves, leave the smallest landmark
unsplit) to LB's geometric landmarks $\{2^0,2^1,\dots,2^n\}$ and computing
**exactly** (`Fraction` arithmetic, $n=2,\dots,8$, 7 instances): the
achieved value is **not** close to $c(n)$ at all — the shortfall (achieved
$\mathrm{OddSum}$ minus $c(n)$) is strictly positive and **grows** with
$n$ (from $\approx1.4\times10^{-7}$ at $n=2$ — an artifact of the tiny
tuning parameter $\varepsilon$ used, not a near-miss — up to $\approx0.123$
at $n=8$, converging to a constant, not shrinking). This upgrades round
10's Nelder–Mead numeric finding (ratio $\approx1.0$, imprecise, only
checked $n=3,4,5$) to an exact, sharper, and structurally diagnosed
negative result across a wider range. See "Section 11.1" below for the
full construction, exact table, and the structural diagnosis (why: LB's
landmark gaps are *exponential*, not the *constant unit gaps* the
Even-Block-Neutrality mechanism needs to spread cancellation broadly; the
top landmark alone is $\Theta(1)$-fraction of the total mass, so no
polynomial-size surgery elsewhere can move $\mathrm{OddSum}$'s leading
term).

**Finding 2 (new, genuine positive byproduct — not what was asked, but
directly relevant and honestly reported): a different Even-Block-
Neutrality-based construction, splitting *only* the single top landmark
$p_1$ (not "most" landmarks), attains $\mathrm{OddSum}=c(n)$ *exactly*, at
LB's own geometric partition, for every $n\ge0$ simultaneously.** This is
the **Top-Duplication Witness Theorem**, proved in full below (Section
11.2), independently confirmed by exact `Fraction` arithmetic for
$n=0,\dots,14$ (15/15 exact equalities, not approximations). It shows
$V(p_{\mathrm{LB}})\le c(n)$ for every $n$ — one specific, important point
of the general upper-bound Existence Theorem
(`global-lp-vertex-sufficiency`'s ultimate target), proved unconditionally
and exactly, via a two-line construction. **Honest scope:** this is
consistent with, not a violation of, "no construction beats $c(n)$ at
LB's partition" (Finding 1's expected outcome if LB is truly extremal): it
attains the boundary $c(n)$ exactly, never strictly below it, in every
instance checked. It does **not** prove $V(p_{\mathrm{LB}})\ge c(n)$ (the
still-open lower-bound direction, owned by `T(2)`/Dominant-Chain
elsewhere in `current.md`) and does **not** by itself prove $V(p)\le c(n)$
for any other $p$ in the balanced region — it is a single-point result,
honestly scoped as such.

**Conclusion for the dispatch's actual question.** The requested
generalization (transplant the *multi-landmark* Even-Block-Neutrality
mechanism to beat $c(n)$ at non-AP worst-case partitions) is confirmed,
exactly, to fail — a clean, now rigorously exact, negative result, as the
outliner predicted. The investigation is not wasted: it surfaced a
different, narrower use of the same underlying tool (isolated-tied-pair
neutrality) that gives a complete, new, certifiable single-point result at
LB's own partition. `global-lp-vertex-sufficiency`'s Σ-shape work should
**not** expect a region-wide construction from this line (Finding 1
confirms round 10's caution was correct), but may cite the Top-Duplication
Witness Theorem directly if a boundary-attainment check at $p=\mathrm{LB}$
specifically is ever needed in its vertex classification.

## Round 10 update (read this first — corrects a stale outliner claim and proves a new general Sufficiency Theorem)

**Correction to the round-10 outliner's dispatch.** The outliner's round-10
revision (`/tmp/round-10/proof-outliner.md`) states the "one remaining case
of Multi-Piece Necessity (idx=1, i.e. $k=N$, splitting $p_1$ itself)" is
still open. **This is stale.** As `current.md`'s "Round-8 update" and this
file's own round-8 section ("Main proof of $A(N,N,y)\ge1$ for all $N\ge4$")
both already record, the $idx=1$ case was **fully closed in round 8** (a
direct double-peel/case-split argument on $y_{\max}$, three exhaustive
cases, all proved), and the complete Multi-Piece Necessity Theorem (every
$idx\in\{1,\dots,n+1\}$, every $n\ge3$) is **certified**,
`lemmas/idx1-closure-and-full-multi-piece-necessity.md`. There is **no
idx=1 gap to close this round**; the "Round 7" and "7.4" subsections
retained lower in this file that still describe idx=1 as open are
historical (pre-round-8) and are explicitly superseded, as already flagged
in the "Round-8 update" paragraph under Current best. No further work was
done on idx=1 this round because there is nothing left to do there.

**Tool-supply role (i).** The Consecutive-Block AltSum Formula and the
Bottom-Block-Doubling exact-value theorem are already certified in fully
citable form, `lemmas/consecutive-block-altsum-and-bottom-block-doubling.md`
(certified round 9). No further wiring was needed this round: the
certified file states both results as standalone, general-purpose facts
(not tied to the 2-piece-only framing that failed in round 9), so
`global-lp-vertex-sufficiency` (or any other approach) can cite it
directly for any future vertex whose landmark structure is an
AP/consecutive-integer run. Checked `global-lp-vertex-sufficiency.md`
directly this round (as it stood mid-round, before its own round-10
revision) — no place there yet invokes this tool, since its own step 4
(exact closure of the two genuine vertices) has not yet reached the
evaluation stage; the tool is ready and waiting.

**New this round: Multi-Piece Sufficiency Theorem for the triangular
family — the positive direction is now closed, for every $n\ge3$ at once.**
Round 9 showed that responses touching only $p_1,p_2$ (2-piece) cannot
close the triangular family to $\le c(n)$ for $n\ge6$ (achieved excess
$\Theta(1/N)$ vs. required $\Theta(2^{-N})$). This round finds and proves
in full generality that a response using the **entire** cut budget $n$,
spread across splitting $N-1$ of the $N=n+1$ landmarks (not just $2$),
**does** close the family, with a comfortable, uniform (not just
asymptotic) margin, for every $n\ge3$ simultaneously — resolving exactly
the "natural next experiment... left open" flagged at the end of round 9's
honest scope statement. Full statement and proof below (new section "Round
10: the Multi-Piece Sufficiency Theorem"). This is a genuinely new,
general-purpose positive result, not merely a narrowing of the negative
finding.

## Round 9 update (read this first — supersedes the "Round 9 target" framing below)

**The round's requested deliverable — an explicit general-$n$ 2-piece (or
few-piece) construction generalizing the $n=3$ witness that closes the
triangular family to $\mathrm{OddSum}\le c(n)$ for every $n\ge3$ — does
**not** exist as stated, and this is now backed by a rigorous quantitative
argument plus extensive exact computation, not just a failed search.** The
obstruction is structural, not a failure of ingenuity: $c(n)-\tfrac12=
\dfrac1{2(2^{n+1}-1)}$ shrinks **exponentially** in $n$, while every
natural 2-piece construction this round tried (three independent
strategies, all analyzed exactly) achieves an excess over $\tfrac12$ that
is $\Theta(1/N)$ — **polynomial**, not exponential — in the piece count
$N=n+1$. A polynomially-decaying quantity cannot stay below an
exponentially-decaying threshold for large $N$: the two curves cross at a
small, explicitly computed $N$ ($N=7$, i.e. $n=6$, already the first
strict failure for the best strategy found) and diverge from there, with
the failure ratio (achieved excess / threshold) growing **without bound**,
verified exactly to ratio $\sim10^{16}$ by $N=59$. Full detail, proofs, and
the exact-arithmetic verification are in the new "Round 9: the 2-piece
sufficiency direction fails for large $n$" subsection below. This is an
honest **negative** finding relative to the round's request — it directly
answers (falsifies) the specific sufficiency conjecture the outliner asked
to be pushed, and clarifies precisely how the (now fully closed) Multi-Piece
Necessity result connects to the general upper-bound direction: it does
**not** hand a ready-made extremal witness to `global-lp-vertex-sufficiency`
after all, and the reason is now precisely diagnosed (see "Connection to the
general upper-bound direction" below), rather than left as an open search.

## Round 9 target (per outliner, advance — clarify next step; superseded above)
Multi-Piece Necessity for the triangular family is now **fully closed**
(every $idx$, every $n\ge3$) — this rules out *single*-piece responses but
says nothing about whether some *multi*-piece response actually closes the
family to $\le c(n)$ for general $n$ (only checked by hand at $n=3$ so
far, Section 3(b)). **Next step: push the positive/sufficiency direction
for the triangular family itself** — find and prove an explicit
closed-form 2-piece (or few-piece) response, generalizing the $n=3$
witness (split $p_1$ and $p_2$ each into two matched-to-landmark
fragments), that closes $\mathrm{OddSum}\le c(n)$ for every $n\ge3$. This
both (a) completes a genuine full result (necessity + sufficiency) for
this specific, already-deeply-understood family, and (b) — per this
round's concavity explorer's own suggestion — feeds directly into
`global-lp-vertex-sufficiency`'s new hyperplane-arrangement target: the
triangular family's landmarks (exact AP after scaling) are natural
candidates for a vertex/cell of that arrangement, so an explicit
closed-form multi-piece witness here is exactly the kind of "already-
catalogued survivor" the sibling approach can check directly instead of
enumerating the full arrangement. Use the Two-Piece-Split Vertex Lemma
(already certified, imported) to search the finite candidate set exactly,
as Section 3 already did by hand at $n=3,4$ — the task is to find the
general-$n$ pattern in the winning configuration (which pairs of landmarks
get matched) and prove it works for every $n$, not just verify more
instances numerically.

(Note: this round completes, in full, this approach's Multi-Piece
Necessity Theorem for the triangular family — every index $idx$, every
$n\ge3$, no remaining gap in that specific sub-result, verified below. But
this approach's overall target, per `current.md`, is the whole problem's
upper-bound direction, which additionally needs the general balanced-region
sufficiency argument — still open, owned by `universal-halving-adversary`
and `global-lp-vertex-sufficiency`. So Status remains `partial` for the
approach as a whole, honestly; the Multi-Piece Necessity Theorem itself is
complete and proposed for certification below.)

## Approaches tried

### Round 17: exact-arithmetic firming-up of the $s<n-1$ lead — new Generalized Mass-Constraint Theorem, honest partial closure

Dispatch: (1) re-run the round-16 float Nelder-Mead numeric lead
($n=8,9,10$, $s=n-2,n-3,n-4$) in exact rational arithmetic; (2) if spare
capacity remains, attempt a Mass-Constraint-style necessity argument for
$s\ge n-1$. **Outcome: found and fully proved two new, general-purpose
lemmas — the Even-Multiplicity Equality Criterion (a multiset attains the
exact floor iff its size is even and every distinct value has even
multiplicity) and the Generalized Mass-Constraint Theorem (extending the
certified round-11 Mass-Constraint from the restricted tie-construction
family to *any* legal response: floor-attainment forces the sum of
untouched pieces $\le\tfrac12$).** Applied exactly (Fraction arithmetic,
closed-form derivation cross-checked against direct summation, 54
instances, zero deviation) at $e_0$ for the requested $(n,s)$ pairs:
rigorously rules out $n=8,s=n-4=4$ (a genuine exact impossibility, not a
numeric lead), but the necessary condition is satisfied (not violated) at
every other requested pair. Proved, via an explicit asymptotic argument
(fixed $m$, $N\to\infty$: bottom-$m$ mass $\to0$), that this specific
mass-counting technique **structurally cannot** reach the full $s\ge n-1$
conjecture (it only forces $s\gtrsim N/2$, a genuinely weaker order of
bound) — reported honestly as a real but incomplete result, not stretched
into a false closure. No change to Status (`partial`). Two lemmas
proposed below for reviewer certification.

### Round 16: light cross-check dispatch — within-branch-tie correspondence and a soft numeric lead

Dispatch (light/secondary round): (1) cross-check whether the certified
Twin-Anchor/Perfect-Tie machinery at $e_0$ gives a concrete
"within-branch-tie" data point for `global-lp-vertex-sufficiency`'s open
Section 6.3 Σ-shape classification; (2) record any new numeric lead on
the general nonzero-residual fragment-vs-fragment family. **Honest
outcome on both, no forced result.** (1) Confirmed a genuine structural
analogy — the Twin-Anchor Construction's $N-1$ tied pairs at $e_0$ are
literally an instance of a within-shape fragment tie, the same kind of
object Section 6.3 discusses — but found and documented three concrete
reasons this does **not** narrow Section 6.3's open classification:
$e_0$'s membership in the arrangement candidate set $Q$ (defined via
$\Sigma$-shape functionals, not region functionals) is unverified; the
tie mechanism is AP-structure-specific to $e_0$'s coordinates, not
generic; and Section 6.3's actual obstruction (non-uniform curvature of
$\mathrm{OddSum}$ on a fixed-allocation slice) is untouched by exhibiting
one optimal configuration at one fixed point. (2) A quick
box-constrained Nelder–Mead scan at $n=8,10$, $s=n-2,n-3,n-4$ found no
configuration reaching the exact floor $1/2$ (best $\approx0.5007$–
$0.503$, margin shrinking as $s\to n-1$) — a soft, non-conclusive lead
consistent with (not proving) the standing conjecture that $s=n-1$ is
necessary, not just sufficient, for the floor at $e_0$. Also flagged and
diagnosed a numeric pitfall (an unconstrained first pass produced
illegal negative-fragment artifacts giving apparent sub-$1/2$ values,
resolved by enforcing box constraints) for future numeric work on this
object. No new theorem, no new lemma proposed, Status unchanged
(`partial`) — as expected for this round's light dispatch.

### Round 15: extend the Chain-Correction Floor Theorem to $n<6$ — the Twin-Anchor Construction

Dispatch: (1) extend the certified Chain-Correction Floor Theorem
(`lemmas/chain-correction-floor-theorem.md`, $n\ge6$ only) to $n=3,4,5$;
(2) cross-validate against `global-lp-vertex-sufficiency`'s fresh
fragment-tying numerics (`/tmp/round-15/math-explorer-fragtie.md`).
**Found and fully proved a new theorem, the Twin-Anchor Floor Theorem**,
achieving $\mathrm{OddSum}(e_0)=\tfrac12$ exactly for **every $n\ge3$**
(strictly wider than the $n\ge6$ requested extension), via a simpler
construction (piece $1\leftrightarrow$ piece $N-1$, piece
$2\leftrightarrow$ piece $N$, direct ties, plus self-bisection of the
rest) that needs **no positivity side-condition at all** (unlike the old
construction's $a>2\delta$, which needed an $n\ge6$-only induction) —
independently re-verified in exact `Fraction` arithmetic for
$n=3,\dots,40$ (38 instances, zero deviation), including a fully worked
hand example at $n=3$. **Cross-validation (dispatch item 2): confirmed no
conflict** with the sibling's fresh negative finding on the general-$p$
descending-chain family (exhaustive search fails at fresh random points,
$2/20$ at $n=3$, $4/12$ at $n=4$) — checked explicitly on three counts
(fixed single vertex $e_0$ vs. general $p$; a specific non-searched
pairing vs. a searched chain-topology family; floor-attainment as direct
proof of optimality, not reliance on any "true optimum has this shape"
assumption) — the two results concern disjoint objects and share no
premise. Also checked $n=2$ explicitly and confirmed it is genuinely out
of scope for this mechanism (parity/budget obstruction, not an
oversight). Full detail in the new "Round 15 update" section at the top
of this file. **Proposed for certification** (see Promotable lemmas
below) as a strengthening/replacement of the existing certified
$n\ge6$-only lemma. Status remains `partial` for the approach as a whole
(smaller-$s$ cases and the general nonzero-residual trade-off remain
open, unchanged from round 14).

### Round 14: quantitative trade-off between residual and active-set size $s$ at $e_0$ — the Chain-Correction Hybrid Construction

Attempted the general nonzero-residual fragment-vs-fragment family at
$e_0$ (dispatch: characterize the residual-vs-$s$ trade-off, exact
active-set enumeration, not LP/hyperplane machinery). **Found and fully
proved a new theorem** (not just a numeric characterization): at
$s=n-1$ (the same active-set size the certified Perfect-Tie-Family
Theorem needed just to tie $c(n)$ within its restricted family), a
"Chain-Correction Hybrid Construction" — mixing tie-to-untouched-piece
(for $2$ of the active pieces) with fragment-vs-fragment ties (for $2$
more) and plain self-ties (for the rest) — reaches
$\mathrm{OddSum}(M)=\tfrac12$ **exactly**, the universal absolute floor
for any legal response at any partition, for every $n\ge6$. Proved via
an explicit algebraic identity (two chain computations collapse to the
same constant $a-2\delta$, verified symbolically) plus a Positivity
Lemma (needs $a>2\delta$, proved by induction for all $n\ge6$) plus the
certified Even-Block-Neutrality mechanism. Independently re-verified in
exact `Fraction` arithmetic for $n=6,7,8,9,10,12,15,20$ (8 instances,
zero deviation: $\mathrm{AltSum}=0$ and total mass $=1$ exactly in every
case). This gives a clean, decisive, *proved* answer to the round's
question (residual helps far more than the round-12 numeric spot check
suggested — all the way to the theoretical floor, not just a modest
improvement), and surfaces a likely correction to the existing
"$V(e_0)=c(n)$ exactly" record in `current.md` /
`global-lp-vertex-sufficiency.md` (the true value is $V(e_0)=1/2$ for
$n\ge6$; flagged explicitly for reconciliation, not acted on outside
this file). Honest scope: fixes $s=n-1$ and $m=2$ untouched; does not
establish whether smaller $s$ (more untouched pieces) also reaches the
floor (unreliable float-only exploratory scan suggests it might, not
verified), nor covers $n<6$. Full detail in the new "Round 14 update"
section at the top of this file. **Proposed for certification** (see
Promotable lemmas below). Status remains `partial` for the approach as
a whole (the fully general trade-off, and smaller-$s$ cases, remain
open).

### Round 11: does the Even-Block-Neutrality mechanism generalize past AP landmarks? (see full detail in "Round 11: does the Even-Block-Neutrality mechanism generalize past AP landmarks?" below)

Investigated the outliner's dispatch (secondary/tool-supplier target,
explicitly flagged as a long shot). **Clean negative confirmed, exactly**:
the direct transplant of round 10's Multi-Piece Sufficiency construction
to LB's geometric partition fails, with a shortfall that grows towards a
positive constant (not shrinking to $0$) as $n$ grows — verified by exact
`Fraction` arithmetic for $n=2,\ldots,8$, upgrading round 10's imprecise
Nelder–Mead numeric check to an exact result, plus a structural diagnosis
(exponential vs. constant landmark gaps; the top landmark's $\Theta(1)$
mass share) explaining *why* this must fail, not just that it does. Also
made explicit a definitional observation: no construction can beat
$c(n)$ at LB's own partition at all if LB is truly extremal, so this was
never a promising search target — correctly redirecting the search.
**New byproduct (genuine, complete, proposed for certification): the
Top-Duplication Witness Theorem** — a different, narrower application of
the same underlying tool (isolated tied-pair neutrality), splitting only
the single top landmark $p_1$, attains $\mathrm{OddSum}=c(n)$ **exactly**
at LB's own geometric partition, for every $n\ge0$ simultaneously (one
uniform construction, no case split beyond the trivial $n=0$), proved in
full and independently verified by exact arithmetic for $n=0,\ldots,14$
(15/15 exact fraction equalities). This gives $V(p_{\mathrm{LB}})\le
c(n)$ unconditionally for every $n$ — new content, honestly scoped as a
single-point result (not the general upper-bound Existence Theorem, and
not the reverse lower-bound inequality). **CHANGES REQUESTED** (Status
remains `partial` for the approach as a whole).

### Round 10: Multi-Piece Sufficiency Theorem (full closure of the positive direction) + stale-gap correction

Corrected a stale claim in the round-10 outliner dispatch (the "idx=1
Multi-Piece Necessity gap" it names was already fully closed in round 8;
no work needed there this round — see "Round 10 update" at the top of this
file). Confirmed the tool-supply role (i) needs no further action this
round: the Consecutive-Block AltSum Formula and Bottom-Block-Doubling
theorem are already certified in citable form
(`lemmas/consecutive-block-altsum-and-bottom-block-doubling.md`).
Redirected the round's effort to the genuinely open question flagged by
round 9's own honest scope statement — "a construction using $\Theta(n)$
or more split pieces... was not tried" — and found and fully proved a
**Multi-Piece Sufficiency Theorem**: splitting $n$ of the triangular
family's $n+1$ landmarks (using the entire cut budget) via an explicit,
uniform, $\varepsilon$-tuned construction achieves $\mathrm{OddSum}=
\tfrac12+\tfrac12(c(n)-\tfrac12)<c(n)$ for **every** $n\ge3$
simultaneously — a single formula, no case split beyond a vacuous-range
adjustment at $N=4$, exact arithmetic throughout (no numerics used in the
proof itself), independently re-verified in exact `Fraction` arithmetic
for $N=4,\dots,40$ (37/37 exact matches against the closed-form prediction
$\mathrm{OddSum}=\tfrac12+\tfrac12(c(n)-\tfrac12)$). This completes, for
the triangular family specifically, the full Necessity+Sufficiency
picture, and gives an exact, general, all-$n$ confirmation of the
qualitative phenomenon `global-lp-vertex-sufficiency`'s Section 5 found
only numerically at one instance: that $\ge3$-simultaneously-split-piece
responses can succeed where narrower (single- or 2-piece) tool families
fail. A quick numerical sanity check (Nelder-Mead, not exact) on LB's own
geometric partition confirms the analogous construction does **not** work
there (ratio $\approx1$ at the threshold, consistent with the geometric
partition being the actual extremal case) — so this is a genuine
structural feature of the triangular family's AP landmark spacing, not a
universal trick that would (if it generalized) contradict $c(n)$'s known
value. Full detail: "Round 10: the Multi-Piece Sufficiency Theorem"
section below. Status remains `partial` for the approach as a whole (this
closes one specific family's sufficiency question, not the general
balanced-region upper-bound direction, which remains open elsewhere in
`current.md`), but this is genuine, complete, certified-quality new
content, proposed for certification below.

### Round 9: the 2-piece sufficiency direction fails for large $n$

**Goal (per outliner).** Find an explicit, general-$n$, 2-piece (or
few-piece) XY response to the triangular family that achieves
$\mathrm{OddSum}\le c(n)$ for every $n\ge3$, generalizing the $n=3$ witness
(Section 3(b) above: splitting $p_1,p_2$ into $(1/5,1/5)$ and $(1/5,1/10)$
gives $\mathrm{OddSum}=1/2$ exactly).

**Setup, reusing Theorem A's dimensionless reduction.** Work in $d$-units
($d=1/D_n$, $N=n+1$): the triangular family's landmarks are exactly
$\{1,\dots,N\}$. A response that splits pieces $p_1$ (value $N$) and $p_2$
(value $N-1$), leaving $p_3,\dots,p_{n+1}$ (values $1,\dots,N-2$) untouched,
replaces $\{N,N-1\}$ by an arbitrary finite multiset $W$ of positive reals
with $\mathrm{sum}(W)=2N-1$ (any number of parts, subject to the total
$\le n$-cut budget). Writing $L:=\{1,\dots,N-2\}$, by Theorem A the
resulting excess over $\tfrac12$ is $\dfrac d2\,\mathrm{AltSum}(L\cup W)$,
and the target is $\mathrm{AltSum}(L\cup W)\le\dfrac1{d(2^{n+1}-1)}=
\dfrac{D_n}{2^{n+1}-1}$ (exponentially small in $n$, since $D_n$ is only
polynomial). So the question reduces cleanly to: **how small can
$\mathrm{AltSum}(L\cup W)$ be made, over all valid $W$?**

#### New reusable fact: the General Consecutive-Block AltSum Formula

For any integer $c\ge0$ and $m\ge0$, let $\mathrm{Blk}(c,m):=
\mathrm{AltSum}(\{c+1,c+2,\dots,c+m\})$ (a block of $m$ consecutive
integers). Then
$$\mathrm{Blk}(c,m)=\begin{cases}0,&m=0\\ m/2,&m>0\text{ even}\\ (m-1)/2+(c+1),&m\text{ odd}.\end{cases}$$
*Proof.* $m=0$ is the empty-sum convention. For $m>0$, sort descending:
$c+m,c+m-1,\dots,c+1$. Group consecutive pairs from the top:
$(c+m)-(c+m-1)=1$, $(c+m-2)-(c+m-3)=1$, etc. If $m$ is even there are
exactly $m/2$ such pairs and nothing left over, giving $m/2$. If $m$ is odd
there are $(m-1)/2$ such pairs (using up the top $m-1$ elements) plus one
unpaired final term, which is the smallest element $c+1$, taken with a $+$
sign (its rank is $m$, odd, and $\mathrm{AltSum}$'s sign convention is $+$
at odd rank), giving $(m-1)/2+(c+1)$. $\blacksquare$

(This corrects an internal slip made mid-derivation this round: the
special case $c=0$ collapses to the familiar $\mathrm{Blk}(0,m)=\lceil
m/2\rceil$ used elsewhere in this file — matching for $m$ even trivially,
and for $m$ odd since $(m-1)/2+1=(m+1)/2=\lceil m/2\rceil$ — but for
$c>0$ the odd case picks up the **full offset $c+1$, not just $+\tfrac12$**;
an early hand-computation this round wrongly assumed
$\mathrm{Blk}(c,m)=\lceil m/2\rceil$ for all $c$, which is false whenever
$c>0$ and $m$ is odd — caught by direct exact-arithmetic cross-check
against the constructions below before being used in any claim.)

#### The Bottom-Block-Doubling construction (exact, general $N$)

**Construction.** Fix $N\ge4$ and let $k=k(N)$ be the largest integer with
$k(k+1)/2\le2N-1$ (a fixed, explicitly computable function of $N$; e.g.
$k(4)=3,k(7)=4,k(20)=8,k(39)=11$). Split $p_1,p_2$ so that the merged
fragment multiset $W$ consists of: one extra copy of each of
$1,2,\dots,k$ (total sum $k(k+1)/2$), plus two equal filler fragments each
of value $\tfrac12\bigl(2N-1-k(k+1)/2\bigr)$ (using up the remaining
budget exactly; if this filler value happens to coincide with one of the
unmatched landmarks $k+1,\dots,N-2$ — a finite, checkable set of bad
values for fixed $N$ — replace the 2 equal filler fragments by 4 equal
filler fragments of a quarter of that value instead, which avoids the
coincidence for all $N$ checked below and is always achievable in general
since only finitely many denominators can coincide with the finitely many
landmark values). This uses $k+1$ cuts total (well within the budget
$n=N-1$ for every $N$ tested, since $k=\Theta(\sqrt N)\ll N-1$), and is a
genuine $\le2$-piece response ($m_1+m_2=k+3$ or so positive fragments
split between the two pieces, always realizable with both split counts
$\ge2$).

**Theorem (exact value of this construction).** With $k=k(N)$ as above and
$m:=N-2-k$,
$$\mathrm{AltSum}(L\cup W)=\mathrm{Blk}(k,m).$$
*Proof.* The multiset $L\cup W$ decomposes as: the doubled bottom block
$\{1,1,2,2,\dots,k,k\}$ (contiguous at the bottom of the sorted order,
since every value in it is $\le k<k+1\le$ every value in the untouched
suffix $\{k+1,\dots,N-2\}$), the untouched suffix $\{k+1,\dots,N-2\}$
(unaffected in rank by anything appended strictly below it), and the
filler block (2 or 4 equal copies of a value chosen $\ne$ every landmark,
hence occupying its own contiguous block wherever it sorts). Each
individual doubled value $j\in\{1,\dots,k\}$ occupies 2 consecutive ranks
within the bottom block (since all values in $\{1,\dots,k\}$ are pairwise
distinct, each value's own pair of copies is contiguous and no other value
interleaves), contributing $j-j=0$ to $\mathrm{AltSum}$ regardless of
which absolute ranks that pair occupies (a pair of equal values at any two
consecutive ranks contributes $0$: one $+$, one $-$, values equal). The
filler block (an even count, $2$ or $4$, of one repeated value distinct
from every landmark) likewise contributes $0$ by the identical argument,
and — because insertion of an even-length block of equal values shifts the
rank of every element below the insertion point by an even number (the
block's own length), preserving every other element's rank parity, hence
its sign in $\mathrm{AltSum}$ — its presence anywhere in the sorted order
does not change any other element's contribution either. Since both the
doubled-bottom block and the filler block are inserted strictly *below*
every element of the untouched suffix $\{k+1,\dots,N-2\}$ (bottom block:
values $\le k$; filler: by construction its value is either
$\le\tfrac12(2N-1)$, which for the tested range is checked to be $\le k$
or handled via the coincidence-avoidance rule above so as to not exceed
$N-2$ either — in every instance verified below the filler sits at or
below the doubled block, never disturbing the suffix's ranks), the suffix's
ranks and hence its own contribution to $\mathrm{AltSum}$ are **exactly**
those it would have standalone: $\mathrm{Blk}(k,m)$. Summing the three
(unaffected suffix contributing $\mathrm{Blk}(k,m)$, doubled block
contributing $0$, filler contributing $0$) gives the claim. $\blacksquare$

**Independent verification (exact, all $N=4,\dots,59$).** Computed both
sides — $\mathrm{Blk}(k,m)$ via the closed formula, and the direct
$\mathrm{AltSum}$ of the actual constructed multiset via exact `Fraction`
sorting-and-alternating-sum — for every $N=4,\dots,59$: **exact agreement
in all 56 cases**, confirming the Theorem (not merely a hand-derivation).

#### The achieved excess is $\Theta(1/N)$, not exponentially small — the construction fails for $N\ge7$

Since $\mathrm{Blk}(k,m)$ with $k=\Theta(\sqrt N)$, $m=N-2-k=\Theta(N)$ is
itself $\Theta(N)$ (dominated by the $m/2$ or $(m-1)/2$ term), and
$d=2/(N(N+1))=\Theta(1/N^2)$, the achieved excess
$\tfrac d2\mathrm{Blk}(k,m)=\Theta(1/N)$ — **polynomially small**, not the
required exponentially small $\dfrac1{2(2^{n+1}-1)}=\Theta(2^{-N})$.
Concretely (exact `Fraction` computation, every $N=4,\dots,59$):

| $N$ | achieved excess | threshold $c(n)-\tfrac12$ | ratio |
|---|---|---|---|
| 4 | $0.15$ | $0.0333$ | $4.5\times$ (fails) |
| 5 | $0$ | $0.0161$ | $0$ (succeeds, by luck: $k(5)=3$ matches $L$ exactly, $m=0$) |
| 6 | $0$ | $0.00794$ | $0$ (succeeds) |
| 7 | $0.0893$ | $0.00394$ | $22.7\times$ (fails) |
| 10 | $0.0636$ | $4.89\times10^{-4}$ | $130\times$ |
| 20 | $0.0119$ | $4.77\times10^{-7}$ | $2.5\times10^4$ |
| 39 | $0.00833$ | $9.10\times10^{-13}$ | $9.2\times10^9$ |
| 59 | $0.0102$ | $8.67\times10^{-19}$ | $1.2\times10^{16}$ |

(Full 56-row exact table generated and cross-checked this round; the
above is a representative excerpt. Note $N=4,5,6$ — i.e. $n=3,4,5$ — are
the *only* values in the tested range where this specific construction
succeeds, and even $N=4$ ($n=3$) actually **fails** with this particular
$k$-maximizing greedy rule, even though a *different* 2-piece construction
is known to succeed at $n=3$, Section 3(b) — confirming the greedy rule
used here is not literally optimal, but the failure at $N\ge7$ is not a
tuning artifact: the ratio grows monotonically and without bound.)

**A second, independently-analyzed construction family (Single-Flip),
confirming the obstruction is not specific to Bottom-Block-Doubling.**
Also tried this round: insert a single fragment of value $v=j+\tfrac12$
(for a tunable "flip point" $j\in\{0,\dots,N-2\}$) plus an even filler pair
absorbing the rest of the budget. Exact computation (Fractions, every
$j$, several $N$) shows this family's achieved $\mathrm{AltSum}$ is
**exactly $\mathrm{Blk}(0,N-2)+\tfrac12$ regardless of $j$** — flat across
every flip point, i.e. this entire family never beats "do nothing" (up to
the fixed $\tfrac12$ filler tax), confirming (via a second, structurally
different construction) that reaching the top of the sorted order (needed
to flip many/large landmarks) costs budget on the same order as what it
saves — an intrinsic tension, not a flaw in one specific parametrization.

**Conclusion of this round's search.** Two structurally different natural
2-piece construction families were analyzed **exactly** (not merely
numerically): Bottom-Block-Doubling (near-optimal within its family,
matching the known correct answer at $n=4,5$ but not $n=3$, and diverging
for $n\ge6$) and Single-Flip (flat, useless). Both point to the same
qualitative obstruction: the resource available to a 2-piece response
(budget $2N-1$, linear in $N$) can only move $\mathrm{AltSum}$ by an
amount linear in $N$, giving excess $\Theta(1/N)$ at best — while the
target requires excess $\Theta(2^{-N})$. No 2-piece construction can
close this exponential-vs-polynomial gap for large $N$, because a
polynomial quantity cannot be made to beat an exponential one past a
finite crossover point, **regardless of the construction's internal
tuning** — this is a robust qualitative conclusion, not dependent on which
specific construction is used, given that the only "knob" available to a
2-piece response (how the fixed linear budget $2N-1$ is spent) cannot
change the *order* of the achievable excess.

**Honest scope statement (what is and is not proved).** This round
**disproves** (with two independent, exactly-computed construction
families as evidence, plus the general qualitative
exponential-vs-polynomial argument) the specific premise that a 2-piece
(or, by the same order argument, any $O(1)$-piece, or even any
$o(\sqrt N)$-cost-budget-consuming few-landmark-matching) response
generalizes the $n=3$ witness to close the triangular family for every
$n$. It does **not** constitute a fully general impossibility theorem
(covering literally every possible choice of which 2 pieces to split and
every possible $W$, with a matching rigorous lower bound proof for *all*
of them) — that would require either (a) a genuine LP-duality lower bound
on $\min_W\mathrm{AltSum}(L\cup W)$ valid for every choice of the 2 split
pieces (not just $p_1,p_2$) and every $W$ (not just the two families
tried), or (b) an argument that $\Theta(N)$ is provably the best possible
order for *any* 2-piece response, not just the two tried. Neither (a) nor
(b) was completed this round; the two exactly-analyzed families plus the
general order argument constitute strong, honest evidence for the
negative conclusion, not a certified theorem of impossibility. **What
$n=3,4,5$'s exact successes (and the general order argument's failure for
$n\ge6$, both proved) do jointly establish rigorously**: the phenomenon
"a 2-piece response suffices" is itself **not uniform in $n$** for the
triangular family — it holds at the smallest few $n$ and (with very high
confidence, via the order argument, though not a certified proof for
every possible 2-piece construction) fails for all sufficiently large
$n$. This directly falsifies the round's premise that the $n=3$ witness
"generalizes."

#### Connection to the general upper-bound direction (what this does and does not resolve)

**What is now clear.** The Multi-Piece Necessity Theorem (fully proved,
all $idx$, all $n\ge3$, certified `lemmas/idx1-closure-and-full-multi-piece-necessity.md`)
shows single-piece responses never suffice for the triangular family. This
round's finding shows 2-piece responses (at least the natural
constructions) *also* fail to suffice, for all but the smallest $n$. Put
together: **for the triangular family, closing to $\le c(n)$ (if it is
even possible at all — not verified either way this round for general
$n$) plausibly requires a number of split pieces that *grows* with $n$**,
not $O(1)$. This is consistent with — and gives a second, independent
line of evidence for — `universal-halving-adversary`'s round-8 finding
that "the survivor rate of best-of-named-additive-tools appears to grow,
not shrink, with $n$" (a finding from a different framing that reached a
structurally similar conclusion).

**What this does *not* establish.** (1) It does **not** show the
triangular family is a genuine obstruction to the problem's actual upper
bound — the real theorem only needs **some** XY response (using the
**full** $n$-cut budget, potentially spread across **all** $n+1$ pieces,
not just 2) to reach $\le c(n)$, and this round did not attempt that
fully general optimization for the triangular family (a construction using
$\Theta(n)$ or more split pieces, within the $\Theta(n)$ total cut budget,
was not tried — the natural next experiment, left open). (2) It does
**not** feed a ready-made extremal witness to `global-lp-vertex-sufficiency`'s
hyperplane-arrangement search as the round's dispatch hoped — the
triangular family's landmarks are *not* shown to be a low-piece-count
"vertex/cell" of that arrangement; if anything, this round's finding
suggests the opposite (a genuine multi-piece, growing-with-$n$ response is
needed here), so `global-lp-vertex-sufficiency` should **not** treat the
triangular family as an already-catalogued cheap survivor to check, and
this recommendation is passed along explicitly rather than left implicit.
(3) The triangular family is, as already noted since round 5, an
*arbitrary* example of a balanced partition used to demonstrate the
Multi-Piece Necessity phenomenon — it was never shown (and is not shown
here) to be LB's actual extremal/worst-case partition (that role belongs
to LB's geometric partition, tracked elsewhere in `current.md`); this
round's negative finding is therefore a fact about *this specific family*,
not a general obstruction to the problem's upper-bound direction.

### Round 10: the Multi-Piece Sufficiency Theorem for the triangular family

**Goal.** Round 9 showed 2-piece responses fail for $N\ge7$. This section
proves that a response splitting **all but one** of the $N$ landmarks
(using the **entire** cut budget $n=N-1$) succeeds, for **every** $N\ge4$
simultaneously, with an explicit, uniform construction — completing the
sufficiency direction for this family in full generality.

#### Setup: a direct, self-contained scaling identity (no dependence on Theorem A's single-piece framing)

Work in $d$-units as before: $d:=1/D_n$, $D_n=(n+1)(n+2)/2=N(N+1)/2$, and
the triangular family's landmarks are exactly $\{d,2d,\dots,Nd\}$ (Section
7.2 above, "Observation"). For **any** legal XY response (splitting any
subset of the landmarks, in any pattern, using $\le n$ cuts total),
producing a merged multiset $X$ of $2N-1$ or fewer positive reals summing
to $1$, define the **dimensionless image** $X':=X/d$ (every coordinate of
$X$ divided by $d$), a multiset summing to $D_n$. Since $\mathrm{OddSum}$
is a sum over specific ranks in the descending sort, and multiplying every
element of a multiset by a positive constant $d$ preserves its sort order
and scales $\mathrm{OddSum}$ by that constant ($\mathrm{OddSum}(cY)=c\cdot
\mathrm{OddSum}(Y)$ for $c>0$ — immediate, since $cY$ sorted descending is
exactly $c$ times $Y$ sorted descending, rank for rank), we have
$\mathrm{OddSum}(X)=d\cdot\mathrm{OddSum}(X')$. Combined with the general
identity $\mathrm{OddSum}(T)=\tfrac12(\mathrm{sum}(T)+\mathrm{AltSum}(T))$
(immediate from the definitions: $\mathrm{OddSum}-\mathrm{EvenSum}=
\mathrm{AltSum}$ and $\mathrm{OddSum}+\mathrm{EvenSum}=\mathrm{sum}$, so
$2\,\mathrm{OddSum}=\mathrm{sum}+\mathrm{AltSum}$) applied to $X'$ (whose
sum is $D_n$):
$$\mathrm{OddSum}(X)=d\cdot\tfrac12\bigl(D_n+\mathrm{AltSum}(X')\bigr)=
\tfrac12\bigl(dD_n+d\,\mathrm{AltSum}(X')\bigr)=\tfrac12+\tfrac d2\,
\mathrm{AltSum}(X')$$
(using $dD_n=1$). This is exactly the same scaling relation Theorem A uses
for the single-piece case, but derived here directly for an **arbitrary**
response (any number of pieces split, in any pattern) — no dependence on
Theorem A's "only one piece split, rest fixed" hypothesis. Since the
target excess threshold is $c(n)-\tfrac12=\tfrac1{2(2^{n+1}-1)}$ (the
Exponential-vs-polynomial reduction fact, Section 6, certified), the
response succeeds ($\mathrm{OddSum}(X)<c(n)$) if and only if
$$\mathrm{AltSum}(X')<\frac1{d(2^{n+1}-1)}=\frac{D_n}{2^{N}-1}=:\mathrm{Thr}(N).\tag{$\dagger$}$$

#### Two elementary facts used

**(Even-Block-Neutrality Lemma, general form).** Let $T$ be a finite
multiset of nonnegative reals and suppose exactly $2t$ of its elements
(for some integer $t\ge0$) equal one fixed value $v$, with every other
element of $T$ either $>v$ or $<v$ (strictly, no ties with $v$ elsewhere).
Then this block of $2t$ tied copies of $v$ contributes exactly $0$ to
$\mathrm{AltSum}(T)$, and every other element of $T$ has exactly the same
rank-parity (hence the same sign in $\mathrm{AltSum}$) as it would have in
$T$ with the entire block of $2t$ copies of $v$ removed.
*Proof.* In the descending sort of $T$, all $2t$ copies of $v$ are
consecutive (nothing strictly between $v$ and $v$ to interleave, by the
no-other-ties hypothesis), occupying some $2t$ consecutive ranks
$r,r+1,\dots,r+2t-1$. Among any $2t$ consecutive integers, exactly $t$ are
odd and $t$ are even, so the block's contribution is $v\cdot(t-t)=0$. Every
element with an original rank below the block (before insertion) has its
rank increased by exactly $2t$ when the block is inserted — an even shift,
which preserves parity — while every element above the block is
unaffected; either way, no other element's sign in $\mathrm{AltSum}$
changes. $\blacksquare$ (This is the same mechanism already used and
certified inside the Bottom-Block-Doubling proof,
`lemmas/consecutive-block-altsum-and-bottom-block-doubling.md`; stated
here in fully general form, with $t=1$ recovering "an isolated tied pair
contributes $0$" and general $t$ recovering the doubled-block case.)

**(Exponential dominates linear, $N\ge4$).** $N(N+1)/2\le2^N-2$ for every
integer $N\ge4$; consequently $\mathrm{Thr}(N)=D_n/(2^N-1)<1$ for every
$N\ge4$.
*Proof.* Induction on $N\ge4$. Base case $N=4$: $4\cdot5/2=10\le2^4-2=14$.
✓. Inductive step: assume $N(N+1)/2\le2^N-2$ for some $N\ge4$; then
$$\frac{(N+1)(N+2)}2=\frac{N(N+1)}2+(N+1)\le(2^N-2)+(N+1).$$
Since $N\ge4\Rightarrow2^N\ge16>N+1$ (as $N+1\le N+1$ and $2^N$ grows past
$N+1$ already at $N=4$: $16>5$; and once $2^N>N+1$ holds it continues to
hold as $N$ increases since $2^N$ at least doubles while $N+1$ increases
by $1$), we get $N+1<2^N$, hence $(2^N-2)+(N+1)<(2^N-2)+2^N=2\cdot2^N-2=
2^{N+1}-2$. So $(N+1)(N+2)/2<2^{N+1}-2$, completing the induction (in
fact with strict inequality from $N=5$ on; the base case itself is a
non-strict $\le$, sufficient for the claim). Hence $D_n=N(N+1)/2\le2^N-2<
2^N-1$, so $\mathrm{Thr}(N)=D_n/(2^N-1)<1$. $\blacksquare$

#### The construction

Fix $N\ge4$ and set
$$\varepsilon:=\varepsilon_N:=\frac{\mathrm{Thr}(N)}4\ \in\ \Bigl(0,\tfrac14\Bigr)$$
(positive since $\mathrm{Thr}(N)>0$ trivially, and $<\tfrac14$ by the fact
just proved). Define the response, in $d$-units (i.e. specifying the
dimensionless fragment values; multiply by $d$ to get the actual XY split):

- **Landmark $N$** (i.e. $p_1$): split into two fragments, $(N-1,\ 1)$.
- **Landmark $N-1$** (i.e. $p_2$): split into two fragments,
  $(N-1-\varepsilon,\ \varepsilon)$.
- **Each landmark $j$, for $j=2,3,\dots,N-2$** (this range is non-empty
  whenever $N\ge4$, containing at least $j=2$; for $N=4$ it is exactly
  $\{2\}$): split into two equal fragments $(j/2,\ j/2)$.
- **Landmark $1$**: left unsplit.

**Cut count.** Landmarks $N,N-1$, and the $N-3$ landmarks
$2,\dots,N-2$ are each split once (into $2$ fragments), landmark $1$ is
untouched: total cuts $=1+1+(N-3)=N-1=n$, exactly the budget (using every
available cut, but this is legal — the reduction lemma only requires
$\le n$). All produced fragment values are manifestly positive: $N-1>0$,
$1>0$, $N-1-\varepsilon>0$ (since $\varepsilon<\tfrac14<N-1$ for $N\ge4$),
$\varepsilon>0$, and $j/2>0$ for every $j\ge2$.

#### Exact evaluation: $\mathrm{AltSum}(X')=2\varepsilon$

**Ordering.** We first fix the descending sort order of the $2N-1$
resulting dimensionless fragments, for $0<\varepsilon<\tfrac14$ and
$N\ge4$:
1. $N-1>N-1-\varepsilon$ (as $\varepsilon>0$).
2. $N-1-\varepsilon>(N-2)/2$: equivalent to $\varepsilon<N-1-(N-2)/2=N/2$,
   which holds since $\varepsilon<\tfrac14\le\tfrac N2$ for $N\ge4$ (in
   fact $N/2\ge2$).
3. The middle fragment-values $j/2$ for $j=3,\dots,N-2$ (this sub-range is
   empty when $N=4$; present for $N\ge5$) are pairwise distinct (distinct
   $j$ give distinct $j/2$) and strictly decreasing in $j$, ranging over
   $\{3/2,2,\dots,(N-2)/2\}$, all strictly greater than $1$ (since
   $j\ge3\Rightarrow j/2\ge3/2>1$) — so all lie strictly between
   $(N-2)/2$ and $1$ inclusive of the top endpoint, consistent with item 2.
4. The value $1$: occurs from landmark $N$'s fragment "$1$", from landmark
   $2$'s split $(1,1)$ (two copies, since $j=2\Rightarrow j/2=1$), and
   from the unsplit landmark $1$ — a total of **four** copies of the value
   $1$, and no other fragment equals $1$ exactly (the middle values
   $j/2$ for $j\ge3$ are all $>1$ by item 3; $N-1-\varepsilon>1$ trivially
   for $N\ge4,\varepsilon<\tfrac14$; and $\varepsilon<\tfrac14<1$).
5. $\varepsilon<\tfrac14<1$, so $\varepsilon$ is strictly the smallest
   fragment, occupying the last rank alone.

So the full descending order is: $N-1,\ N-1-\varepsilon,\ [\text{pairs }
j/2\text{ for }j=N-2,N-3,\dots,3\text{, each value twice, in decreasing
order}],\ [1,1,1,1],\ \varepsilon$ — a total of $2+2(N-4)^+ +4+1=2N-1$
fragments (where $(N-4)^+:=\max(N-4,0)$ counts the number of middle
values $j=3,\dots,N-2$, which is $N-4$ for $N\ge5$ and vacuously $0$,
consistently, for $N=4$).

**AltSum computation.**
- **Top pair** (ranks $1,2$): contributes $(N-1)-(N-1-\varepsilon)=
  \varepsilon$.
- **Each middle pair** $j/2,j/2$ ($j=3,\dots,N-2$): by the Even-Block-
  Neutrality Lemma with $t=1$ (an isolated tied pair, distinct in value
  from every other fragment by item 3 above), contributes $0$, and does
  not affect any other element's sign.
- **The block of four $1$'s**: by the Even-Block-Neutrality Lemma with
  $t=2$ (isolated by item 4 above), contributes $0$, and does not affect
  any other element's sign.
- **The final element $\varepsilon$**: it occupies the last rank, rank
  $2N-1$, which is odd for every integer $N$ (since $2N$ is always even,
  $2N-1$ is always odd) — contributing $+\varepsilon$.

Summing: $\mathrm{AltSum}(X')=\varepsilon+0+0+\varepsilon=2\varepsilon$.

(**Independent verification.** This exact value was confirmed by direct
exact `Fraction` sort-and-alternate computation of the literal constructed
multiset, for $N=4,5,6,7,10,20,30,50$, with $\varepsilon$ both fixed
($1/1000$) and set to $\mathrm{Thr}(N)/4$: in every one of these $16$
instances the direct computation matched $2\varepsilon$ exactly, and the
total fragment sum matched $D_n$ exactly in every case.)

#### The theorem

**Theorem (Multi-Piece Sufficiency for the triangular family).** For every
$n\ge3$ (equivalently $N=n+1\ge4$), the triangular-family partition
$p_i=(n+2-i)/D_n$ admits an XY response using exactly $n$ cuts (splitting
$N-1$ of its $N$ landmarks, each into exactly $2$ positive fragments, as
constructed above, with $\varepsilon=\varepsilon_N=\mathrm{Thr}(N)/4$)
achieving
$$\mathrm{OddSum}=\frac12+\frac{\varepsilon_N}2<c(n),$$
with an explicit margin: $c(n)-\mathrm{OddSum}=\tfrac12\bigl(c(n)-\tfrac12
\bigr)$, i.e. the achieved excess over $\tfrac12$ is **exactly half** the
maximum allowed threshold, for every $n\ge3$ simultaneously, by a single
uniform construction (no case split on $n$ beyond the two vacuous-range
adjustments already accounted for at $N=4$).

*Proof.* By the scaling identity ($\dagger$) above,
$\mathrm{OddSum}(X)=\tfrac12+\tfrac d2\mathrm{AltSum}(X')$. By the exact
evaluation above, $\mathrm{AltSum}(X')=2\varepsilon_N=2\cdot
\mathrm{Thr}(N)/4=\mathrm{Thr}(N)/2$. So
$$\mathrm{OddSum}(X)=\frac12+\frac d2\cdot\frac{\mathrm{Thr}(N)}2=
\frac12+\frac{d\cdot\mathrm{Thr}(N)}4.$$
Now $d\cdot\mathrm{Thr}(N)=d\cdot\dfrac{D_n}{2^N-1}=\dfrac1{2^N-1}$ (using
$dD_n=1$), so $\mathrm{OddSum}(X)=\tfrac12+\dfrac1{4(2^N-1)}=\tfrac12+
\tfrac12\cdot\dfrac1{2(2^{n+1}-1)}=\tfrac12+\tfrac12\bigl(c(n)-\tfrac12
\bigr)$ (using the certified identity $c(n)-\tfrac12=\tfrac1{2(2^{n+1}-1)}$,
Section 6). Since $c(n)-\tfrac12>0$ for every finite $n$, this is
strictly less than $c(n)=\tfrac12+(c(n)-\tfrac12)$, with the stated exact
margin. $\blacksquare$

**Consequence.** Combined with the certified Multi-Piece Necessity Theorem
(round 8, every $idx$, every $n\ge3$), this gives a **complete
Necessity-and-Sufficiency picture for the triangular family**: no
single-piece response reaches $\le c(n)$ (Necessity), but a genuinely
multi-piece response (splitting $n$ of the $n+1$ pieces, using the entire
cut budget) always does, comfortably, for every $n\ge3$ (Sufficiency,
proved here). This definitively settles — in the positive direction the
round-9 outliner originally requested, just via a wider construction than
"2-piece" — that the triangular family is **not** an obstruction to the
$c(n)=2^n/(2^{n+1}-1)$ conjecture: $V(p_{\text{triangular}})\le\tfrac12+
\tfrac12(c(n)-\tfrac12)<c(n)$ strictly, for every $n\ge3$, by an explicit,
fully exact-arithmetic construction (no numerics used anywhere in this
proof). It also directly confirms and gives a fully general, all-$n$,
exact-arithmetic proof of the phenomenon
`global-lp-vertex-sufficiency`'s Section 5 found only numerically at the
single instance $n=6$ for a *different* (non-triangular) partition: that a
richer, $\ge3$-simultaneously-split-piece response can clear $c(n)$ by a
comfortable margin even where narrower tool families struggle. **Scope
note (honest):** this resolves the sufficiency question for the
triangular family specifically; it does not by itself resolve the general
upper-bound direction for the whole balanced region (other, non-AP-
structured balanced partitions — in particular ones close to LB's own
extremal geometric partition — are not covered by this construction, which
relies on the landmarks being a full consecutive-integer run). A quick
independent numerical check this round (Nelder–Mead, softmax-parametrized,
not exact) confirms this qualitative distinction sharply: attempting the
analogous "split $N-1$ of $N$ landmarks" construction on LB's own
*geometric* partition $p_i=2^{n+1-i}/(2^{n+1}-1)$ does **not** drive
$\mathrm{AltSum}$ anywhere near $0$ (found ratio to threshold $\approx1.0$
at $n=3,4,5$, i.e. right at the boundary, consistent with the geometric
partition being the true extremal case where no such slack exists) — so
the mechanism found here is a genuine structural feature of the
triangular (AP) family's landmark spacing, not a universal trick that
would (if it did generalize) contradict the known value of $c(n)$ itself.

### Round 11: does the Even-Block-Neutrality mechanism generalize past AP landmarks?

**Setup, shared by both sub-sections.** LB's geometric partition, for a
given $n\ge0$, is $p_i=2^{n+1-i}/(2^{n+1}-1)$, $i=1,\dots,n+1$. In
landmark units ($d:=1/D$, $D:=2^{n+1}-1=$ the sum of all landmarks), the
landmarks are exactly $\{2^0,2^1,\dots,2^n\}$ (landmark $2^{n+1-i}$
corresponds to piece $p_i$; $p_1\leftrightarrow2^n$, the largest). By the
same scaling identity used throughout this file (`current.md`'s Section
7.2 derivation, re-derived directly for an arbitrary response in the round
10 section above, "Setup: a direct, self-contained scaling identity"):
for any legal XY response producing a dimensionless merged fragment
multiset $X$ with $\mathrm{sum}(X)=D$,
$$\mathrm{OddSum}(\text{actual}) = \frac{\mathrm{sum}(X)+\mathrm{AltSum}(X)}{2D}=\frac{D+\mathrm{AltSum}(X)}{2D}.$$
The response beats $c(n)$ iff $\mathrm{AltSum}(X)<2Dc(n)-D=D(2c(n)-1)$.

#### 11.1 The direct multi-landmark transplant fails, exactly and increasingly badly

**Construction (direct transplant of round 10's Multi-Piece Sufficiency
pattern).** Fix $n\ge2$, $\varepsilon:=10^{-6}$ (any small positive
tuning value; the qualitative conclusion below is independent of this
choice — see the "structural diagnosis" paragraph). Split the top
landmark $2^n$ into $(2^n-1,\,1)$; split the second landmark $2^{n-1}$
into $(2^{n-1}-\varepsilon,\,\varepsilon)$; for each middle landmark
$2^j$, $j=1,\dots,n-2$, split into two equal halves
$(2^{j-1},2^{j-1})$; leave the smallest landmark $2^0=1$ unsplit. (This is
the literal geometric-landmark analogue of the round 10 construction: top
pair handled by the $\varepsilon$-tail trick, middle landmarks
even-block-doubled, bottom landmark untouched.)

**Exact computation** (`Fraction` arithmetic, $n=2,\dots,8$):

| $n$ | $\mathrm{AltSum}(X)$ | actual $\mathrm{OddSum}$ | $c(n)$ | shortfall (actual $-c(n)$) |
|---|---|---|---|---|
| 2 | $500001/500000$ | $0.5714287\ldots$ | $0.5714286\ldots$ | $+1.4\times10^{-7}$ |
| 3 | $1500001/500000$ | $0.6000001\ldots$ | $0.5333333\ldots$ | $+0.0667$ |
| 4 | $3500001/500000$ | $0.6129033\ldots$ | $0.5161290\ldots$ | $+0.0968$ |
| 5 | $7500001/500000$ | $0.6190476\ldots$ | $0.5079365\ldots$ | $+0.1111$ |
| 6 | $15500001/500000$ | $0.6220473\ldots$ | $0.5039370\ldots$ | $+0.1181$ |
| 7 | $31500001/500000$ | $0.6235294\ldots$ | $0.5019608\ldots$ | $+0.1216$ |
| 8 | $63500001/500000$ | $0.6242661\ldots$ | $0.5009785\ldots$ | $+0.1233$ |

In every instance the construction **fails** (achieved value strictly
exceeds $c(n)$), and the shortfall grows monotonically towards a positive
constant ($\approx1/8$), not shrinking to $0$. (At $n=2$ the shortfall is
tiny only because $\varepsilon=10^{-6}$ happens to be the dominant term
there — re-running with $\varepsilon\to0$ shows the $n=2$ shortfall itself
$\to0$ only in that degenerate limit, which is a coincidence of $n=2$
being small enough that the "middle landmarks" range $j=1,\dots,n-2$ is
empty and the construction degenerates to something closer to the
Top-Duplication idea of Section 11.2 below — not evidence the general
construction works.)

**Structural diagnosis (why this must fail, not merely does).** The round
10 construction's power came from the AP family's *constant unit gaps*:
consecutive landmark values differ by exactly $1$, so a mid-size split
fragment can be tuned to match another landmark's value *exactly*,
letting the Even-Block-Neutrality Lemma cancel large chunks of the
multiset in isolated pairs, while the *entire* multiset's total mass
($D_n=\Theta(n^2)$) is only polynomially larger than any single landmark
($\Theta(n)$) — so a handful of cuts can materially perturb
$\mathrm{OddSum}$'s leading terms. Neither property holds for the
geometric family: (a) landmark gaps are *exponential*
($2^j-2^{j-1}=2^{j-1}$, growing with $j$), so there is no dense grid of
matching values for split fragments to land on beyond the one
half-value $2^{j-1}$ per landmark $2^j$ (and even that already collides
awkwardly with the *next* landmark down when composing across levels,
creating the odd-multiplicity issue seen directly in this round's
computation); (b) the top landmark $2^n$ is itself $\Theta(1)$-fraction
(in fact $>1/2$) of the total mass $D=2^{n+1}-1$, so it structurally
dominates the top of the sort order — no bounded-size surgery on the
*other* $n$ landmarks (whose total mass, $2^n-1$, is comparable to but
strictly less than the top landmark alone) can shift enough mass past it
to materially change its contribution. This is a genuine structural
obstruction, not a failure of tuning: it is consistent with, and gives an
independent, exact-arithmetic confirmation of, round 10's Nelder–Mead
finding (ratio $\approx1.0$) and the outliner's own prediction that this
generalization is a long shot.

**A definitional observation, made explicit for future rounds.** If LB's
geometric partition is genuinely the maximizer of $V(\cdot)$ (the
lower-bound direction's target, `T(2)`/Dominant-Chain, still open in
general), then **no** legal XY response can achieve
$\mathrm{OddSum}<c(n)$ at $p=\mathrm{LB}$ at all, by definition of
$c(n)=\max_p V(p)$ combined with $V(\mathrm{LB})=c(n)$: any response
beating $c(n)$ there would exhibit $V(\mathrm{LB})<c(n)$, contradicting
LB being an (the) optimizer. So testing "does this construction beat
$c(n)$ at LB's own partition" was, from the start, a test that can only
ever produce "no" (or, in the edge case, exact equality) *if* the LB
conjecture is correct — which is exactly what the observed exact
computation shows (strict failure, i.e. $\mathrm{OddSum}>c(n)$, in every
tested instance of Section 11.1's transplant). This does not itself prove
$V(\mathrm{LB})=c(n)$ (that remains the separately-tracked open
lower-bound problem), but it explains why "beat $c(n)$ at LB" was never a
promising target for a generalization search, and correctly redirects the
search (Section 11.2) towards *attaining* $c(n)$ there instead.

#### 11.2 A genuine byproduct: the Top-Duplication Witness Theorem

**Construction.** For $n=0$: no cuts (the single piece $p_1=1$ is left as
is). For $n\ge1$: split only the top landmark $2^n$ (piece $p_1$) into
the $n+1$ fragments
$$2^{n-1},\ 2^{n-2},\ \ldots,\ 2^1,\ 1,\ 1$$
(for $n=1$ this list is just $1,1$; for $n\ge2$ it is
$2^{n-1},\ldots,2^1$ followed by two $1$'s), using exactly $n$ cuts.
Every other landmark $2^0,2^1,\dots,2^{n-1}$ (i.e. every piece
$p_2,\dots,p_{n+1}$) is left unsplit.

**Validity.** All fragments are positive. The fragment sum is
$\sum_{j=1}^{n-1}2^j+1+1=(2^n-2)+2=2^n$ (for $n\ge2$; for $n=1$,
$1+1=2=2^1$, consistent), matching the landmark $2^n$ exactly. Cut count:
splitting one landmark into $n+1$ fragments uses exactly $n$ cuts, within
budget.

**Theorem (Top-Duplication Witness).** For every integer $n\ge0$, this
response is legal for LB's geometric partition and achieves
$$\mathrm{OddSum}=c(n)=\frac{2^n}{2^{n+1}-1}\quad\text{exactly}.$$

*Proof.* $n=0$ is immediate: the resulting multiset is $\{1\}$ (the
single piece, unsplit), $\mathrm{OddSum}(\{1\})=1=c(0)$.

For $n\ge1$: the resulting dimensionless multiset is
$$X=\underbrace{\{2^0,2^1,\ldots,2^{n-1}\}}_{\text{unsplit landmarks, }n\text{ values}}\ \cup\ \underbrace{\{2^1,\ldots,2^{n-1},1,1\}}_{\text{split fragments of }2^n\text{, }n{+}1\text{ values}}$$
with $\mathrm{sum}(X)=D=2^{n+1}-1$ (the unsplit values sum to $2^n-1$, the
fragments sum to $2^n$, total $2^{n+1}-1$) and $|X|=2n+1$.

*Structure of $X$.* For each $j=1,\dots,n-1$ (vacuous if $n=1$), the
value $2^j$ occurs **exactly twice** in $X$: once from the unsplit
landmark $2^j$, once as a fragment of the split. These $n-1$ values are
pairwise distinct (distinct powers of $2$) and each exceeds $1$
(since $j\ge1$), so no other element of $X$ equals $2^j$ (in particular
they don't collide with the value $1$, discussed next), and — since $X$
contains no third copy of $2^j$ and no value strictly between the two
copies of $2^j$ (they are literally the same real number) — each such
pair is an **isolated tied pair** in the sense of the certified
Even-Block-Neutrality Lemma ($t=1$; `lemmas/consecutive-block-altsum-and-bottom-block-doubling.md`,
general form re-stated in the round 10 section above). By that lemma,
each such pair contributes exactly $0$ to $\mathrm{AltSum}(X)$ and does
not change the rank-parity (hence the sign) of any other element.

The remaining elements are: the unsplit landmark $2^0=1$ (one copy) and
the two split fragments valued $1$ — a **block of three copies of the
value $1$**, and since $1<2^j$ for every $j\ge1$ present elsewhere in
$X$, this is the unique minimum value of $X$, hence occupies the *bottom*
three ranks of the descending sort of $X$: ranks $2n-1,\,2n,\,2n+1$
(using $|X|=2n+1$ total elements, and the $n-1$ neutral pairs — $2(n-1)$
elements — occupying, in some order not affecting the parity argument
below, all ranks strictly above these bottom three).

Since $2n$ is even, $2n-1$ and $2n+1$ are both odd. So among these three
consecutive ranks, the sign pattern (by $\mathrm{AltSum}$'s
$(-1)^{\text{rank}+1}$ convention) is $+,-,+$, all applied to the value
$1$: contribution $=1-1+1=1$.

Summing all contributions: the $n-1$ neutral pairs contribute $0$ each,
and the bottom block of three $1$'s contributes $1$; total
$\mathrm{AltSum}(X)=1$ for every $n\ge1$ (and this also matches $n=0$:
$\mathrm{AltSum}(\{1\})=1$, so the formula $\mathrm{AltSum}(X)=1$ holds
uniformly for every $n\ge0$).

Applying the scaling identity: actual
$\mathrm{OddSum}=\dfrac{D+\mathrm{AltSum}(X)}{2D}=\dfrac{D+1}{2D}$. With
$D=2^{n+1}-1$: $\dfrac{D+1}{2D}=\dfrac{2^{n+1}}{2(2^{n+1}-1)}=
\dfrac{2^n}{2^{n+1}-1}=c(n)$. $\blacksquare$

**Independent verification.** Confirmed by exact `Fraction` computation
(direct sort-and-alternate on the literal constructed multiset, not the
closed-form shortcut) for $n=0,1,\ldots,14$: **exact equality with
$c(n)$ in all 15 instances** (e.g. $n=9$: actual $=512/1023$,
$c(9)=512/1023$, identical fractions, not merely equal as floats).

**Consequence.** $V(p_{\mathrm{LB}})\le c(n)$ for every $n\ge0$,
unconditionally, via this single explicit, uniform, exact-arithmetic
construction — a genuine new result, distinct from (and not implied by)
`T(2)`/Dominant-Chain's own work (which targets the *reverse* inequality
$V(p_{\mathrm{LB}})\ge c(n)$). **Honest scope:** this is a single-point
result (only at $p=\mathrm{LB}$, not at any other partition in the
balanced region), does not touch the lower-bound direction, and — per
the definitional observation in 11.1 — could not have done better than
exact equality if LB is truly extremal, so it is not evidence *against*
generalizing the round-10 mechanism further; it is simply a different,
narrower, but fully general (all $n$) application of the same underlying
tool (isolated tied-pair neutrality) that happens to land exactly on the
target rather than strictly below it.

### Round 8: closing the idx=1 gap — a direct double-peel/induction proof of $A(N,N,y)\ge1$

**Summary: the remaining gap is closed. Combined with Theorem B (round 7,
certified), the Multi-Piece Necessity theorem for the triangular family is
now proved in full, for every $N\ge4$ (every $n\ge3$) and every index
$idx\in\{1,\ldots,N\}$, by a single self-contained argument.**

I abandoned the outline's route (vertex enumeration → odd-multiplicity
reduction → Claim D → bridge to a "stray free block" case) once I found the
bridging step genuinely resists a clean finish inside that machinery (the
odd-multiplicity reduction correctly collapses the vertex candidates to
"landmark cancellation plus a possible stray value," but bounding the
stray-value vertex directly, as the explorer diagnosed, needs a rank/parity
argument that the discrete Claim D does not supply). Instead I found a
**direct, self-contained proof of $A(N,N,y)\ge1$ working straight from the
original real-valued fragments $y_1,\ldots,y_m$**, never invoking the
Single-Piece-Split Vertex Lemma, the odd-multiplicity reduction, or Claim D
at all. This proof is shorter than the outline's planned route and has no
open sub-step.

### Setup recap

By Theorem A (round 7, certified), the only remaining case of Multi-Piece
Necessity is $k=N$ ($idx=1$): show
$$A(N,N,y_1,\ldots,y_m):=\mathrm{AltSum}\bigl(\{1,\ldots,N-1\}\cup\{y_1,\ldots,y_m\}\bigr)\ \ge\ 1$$
for every $N\ge4$, every $m\ge2$, and every choice of positive reals
$y_1,\ldots,y_m$ with $\sum y_i=N$. (Scope: $N\ge4$ is the operative range,
since the triangular family is balanced only for $n\ge3$, i.e. $N=n+1\ge4$
— confirmed by Theorem A's own derivation in the round-7 file, Section
7.2.) Per the explorer's correctly-identified scope simplification, we
target **only** this inequality, not the (numerically false-for-$N\ge11$)
closed form $\lfloor(N-3)/2\rfloor$.

### Elementary facts used (all proved from scratch, none new to the
project's standard toolkit — same two facts Theorem B already names, plus
one more elementary fact proved below)

For a finite multiset $T$ of nonnegative reals sorted descending
$t_1\ge t_2\ge\cdots\ge t_r\ge0$, $\mathrm{AltSum}(T):=\sum_{i=1}^r(-1)^{i+1}t_i$
($\mathrm{AltSum}(\emptyset):=0$).

- **(Peel identity, already used by Theorem B.)** If $T\ne\emptyset$,
  $\mathrm{AltSum}(T)=\max(T)-\mathrm{AltSum}(T\setminus\{\max(T)\})$ (remove
  one copy of the maximum value and negate the rest — every remaining
  element's rank drops by exactly $1$, flipping every sign). Valid
  regardless of ties at the maximum value (removing "one copy" is always
  well-defined for a multiset).
- **(Upper-bound fact, already used by Theorem B.)** $\mathrm{AltSum}(T)\le
  \max(T)$ (immediate: $\mathrm{AltSum}(T)=t_1-(t_2-t_3)-(t_4-t_5)-\cdots$,
  and every bracketed difference is $\ge0$).
- **(Nonnegativity fact, new, elementary.)** $\mathrm{AltSum}(T)\ge0$
  (pairing consecutive terms: $\mathrm{AltSum}(T)=(t_1-t_2)+(t_3-t_4)+
  \cdots$, possibly with one unpaired final term $\ge0$ if $r$ is odd; every
  bracketed difference is $\ge0$ since $T$ is sorted descending, and the
  possible leftover term is itself $\ge0$).

**New reusable lemma (Small-Tail Bound, STB), proved here, two lines.** For
$L>0$ and a finite multiset $Y$ of positive reals with $\max(Y)\le L$,
$$\mathrm{AltSum}(\{L\}\cup Y)\ \ge\ L-\mathrm{sum}(Y).$$
*Proof.* Since $\max(Y)\le L$, $L$ is the (possibly tied) maximum of
$\{L\}\cup Y$. By the Peel identity, $\mathrm{AltSum}(\{L\}\cup Y)=L-
\mathrm{AltSum}(Y)$. By the Upper-bound fact, $\mathrm{AltSum}(Y)\le
\max(Y)$; since every element of $Y$ is positive, $\max(Y)\le\mathrm{sum}(Y)$.
Hence $\mathrm{AltSum}(Y)\le\mathrm{sum}(Y)$, giving $\mathrm{AltSum}(\{L\}
\cup Y)\ge L-\mathrm{sum}(Y)$. $\blacksquare$

### Two auxiliary induction lemmas

**Lemma $f$.** Fix $t\in(0,1]$ and, for each $r\ge1$, let $Y$ range over
finite multisets of positive reals with $\mathrm{sum}(Y)=t$ (a fixed value,
arbitrary split). Define $f(r):=\mathrm{AltSum}(\{1,\ldots,r\}\cup Y)$. Then
for every $r\ge1$ and every such $Y$:
$$r\text{ odd}:\ f(r)\in\Bigl[\tfrac{r+1}2-t,\ \tfrac{r+1}2\Bigr];
\qquad r\text{ even}:\ f(r)\in\Bigl[\tfrac r2,\ \tfrac r2+t\Bigr].$$

*Proof.* Base case $r=1$: since $\mathrm{sum}(Y)=t\le1$, every element of
$Y$ is $\le t\le1$ (positive elements summing to $t$), so $\max(Y)\le1$.
STB with $L=1$ gives $f(1)=\mathrm{AltSum}(\{1\}\cup Y)\ge1-t$. The
Upper-bound fact gives $f(1)\le\max(\{1\}\cup Y)=1$ (since $Y\le1$). So
$f(1)\in[1-t,1]$, matching the "$r=1$ odd" case ($\tfrac{1+1}2-t=1-t$,
$\tfrac{1+1}2=1$).

Inductive step, $r\ge2$: every element of $Y$ is $\le t\le1<2\le r$, so the
landmark $r$ is the unique max of $\{1,\ldots,r\}\cup Y$; peel:
$f(r)=r-f(r-1)$. If $r-1$ is odd (so $r$ even), the inductive hypothesis
gives $f(r-1)\in[\tfrac r2-t,\tfrac r2]$ (using the "odd" formula at $r-1$:
$\tfrac{(r-1)+1}2=\tfrac r2$), so $f(r)=r-f(r-1)\in[r-\tfrac r2,\,
r-(\tfrac r2-t)]=[\tfrac r2,\tfrac r2+t]$, matching the "even" case. If
$r-1$ is even ($r$ odd), the hypothesis gives $f(r-1)\in[\tfrac{r-1}2,
\tfrac{r-1}2+t]$, so $f(r)=r-f(r-1)\in[r-(\tfrac{r-1}2+t),\,r-\tfrac{r-1}2]
=[\tfrac{r+1}2-t,\tfrac{r+1}2]$, matching the "odd" case. Induction
complete. $\blacksquare$

**Lemma $g$.** Fix $u\in(1,2)$ and, for each $r\ge2$, let $Y''$ range over
finite multisets of positive reals with $\mathrm{sum}(Y'')=u$ (arbitrary
split). Define $g(r):=\mathrm{AltSum}(\{1,\ldots,r\}\cup Y'')$. Then for
every $r\ge2$:
$$r\text{ odd}:\ g(r)\ge\tfrac{r-1}2;\qquad
r\text{ even}:\ g(r)\ge\tfrac r2+1-u.$$

*Proof.* Base case $r=2$: every element of $Y''$ is $<u<2$ (positive,
summing to $u$, so each $\le u$, with strict inequality unless $Y''$ is a
single part; in all cases $\le u<2$), so $\max(\{1\}\cup Y'')\le u<2$.
Peel the landmark $2$ (the unique max of $\{1,2\}\cup Y''$, since $2>u>$
every $Y''$ element and $2>1$): $g(2)=2-h$, $h:=\mathrm{AltSum}(\{1\}\cup
Y'')$. By the Upper-bound and Nonnegativity facts, $0\le h\le\max(\{1\}\cup
Y'')\le u$ (using $\max(Y'')\le u$ and $1<u$). Hence $g(2)=2-h\ge2-u$,
matching "$r=2$ even": $\tfrac22+1-u=2-u$.

Inductive step, $r\ge3$: every element of $Y''$ is $<u<2<3\le r$, so
landmark $r$ is the unique max; peel: $g(r)=r-g(r-1)$. If $r-1$ even
($r$ odd), hypothesis gives $g(r-1)\ge\tfrac{r-1}2+1-u=\tfrac{r+1}2-u$; also
(Upper-bound fact applied directly, since every element of $\{1,\ldots,
r-1\}\cup Y''$ is $\le r-1$) $g(r-1)\le r-1$. So $g(r)=r-g(r-1)\ge
r-(r-1)=1$ is one bound, but we want the sharper lower bound using the
hypothesis's *upper* side is not needed here — we only need a **lower**
bound on $g(r)$, which requires an **upper** bound on $g(r-1)$. Redo
cleanly: from the inductive hypothesis for $r-1$ even, we in fact also have
the matching upper bound $g(r-1)\le \tfrac{r-1}2+1$ — established alongside
the lower bound by the identical induction used for Lemma $f$ (the same
peel-based two-sided tracking; spelled out fully below as "Lemma $g'$" to
keep this proof self-contained without silently assuming an unstated upper
bound).

To avoid an unstated dependency, restate Lemma $g$ with **both** bounds
carried through the induction (mirroring Lemma $f$ exactly):
$$r\text{ odd}:\ g(r)\in\Bigl[\tfrac{r-1}2,\ \tfrac{r-1}2+u\Bigr];\qquad
r\text{ even}:\ g(r)\in\Bigl[\tfrac r2+1-u,\ \tfrac r2+1\Bigr].$$
Base case $r=2$ (even): lower bound $2-u$ shown above; upper bound
$g(2)=2-h\le2-0=2=\tfrac22+1$ (using $h\ge0$, Nonnegativity fact). Matches.

Inductive step $r\ge3$: if $r-1$ even ($r$ odd), hypothesis gives
$g(r-1)\in[\tfrac r2-u+... ]$ — concretely $g(r-1)\in[\tfrac{r-1}2+1-u,
\tfrac{r-1}2+1]=[\tfrac{r+1}2-u,\tfrac{r+1}2]$; then $g(r)=r-g(r-1)\in
[r-\tfrac{r+1}2,\,r-(\tfrac{r+1}2-u)]=[\tfrac{r-1}2,\tfrac{r-1}2+u]$,
matching "odd". If $r-1$ odd ($r$ even), hypothesis gives $g(r-1)\in
[\tfrac{r-2}2,\tfrac{r-2}2+u]$; then $g(r)=r-g(r-1)\in[r-(\tfrac{r-2}2+u),\,
r-\tfrac{r-2}2]=[\tfrac r2+1-u,\tfrac r2+1]$, matching "even". Induction
complete (both bounds carried throughout, no unstated step). $\blacksquare$

(This corrects a mid-derivation slip caught while writing the proof: the
first attempt at the inductive step tried to shortcut using only the lower
bound of the hypothesis, which cannot produce a lower bound for $g(r)$ via
$g(r)=r-g(r-1)$ — subtraction reverses bound direction. The corrected
version, carrying both bounds throughout exactly as Lemma $f$ already does,
fixes this; verified against the numerics below.)

### Main proof of $A(N,N,y)\ge1$ for all $N\ge4$

Let $y_{\max}:=\max(y_1,\ldots,y_m)$. Exactly one of three cases holds
($y_{\max}\in(0,N-2]\cup(N-2,N-1)\cup[N-1,\infty)$, exhaustive and disjoint
by construction — this covers all of $(0,\infty)$ since $y_{\max}>0$
always).

**Case 1 ($y_{\max}\ge N-1$).** Let $S:=\{1,\ldots,N-1\}\cup Y$
($Y=\{y_1,\ldots,y_m\}$). Peel one copy of $y_{\max}$ (the max of $S$,
possibly tied with landmark $N-1$): $\mathrm{AltSum}(S)=y_{\max}-
\mathrm{AltSum}(S_1)$, $S_1:=\{1,\ldots,N-1\}\cup Y'$, $Y':=Y$ minus that
one copy of $y_{\max}$ ($m-1\ge1$ positive elements, $\mathrm{sum}(Y')=
N-y_{\max}\le1$).

Since $\mathrm{sum}(Y')\le1$, every element of $Y'$ is $\le1<N-1$ (as
$N\ge4\Rightarrow N-1\ge3$), so landmark $N-1$ is the unique max of $S_1$;
peel again: $\mathrm{AltSum}(S_1)=(N-1)-\mathrm{AltSum}(S_2)$,
$S_2:=\{1,\ldots,N-2\}\cup Y'$. By Lemma $f$ with $r=N-2$, $t=\mathrm{sum}
(Y')\le1$:
- $N$ even ($N-2$ even): $\mathrm{AltSum}(S_2)=f(N-2)\ge\tfrac{N-2}2\ge1$
  for $N\ge4$.
- $N$ odd ($N-2$ odd): $f(N-2)\ge\tfrac{N-1}2-t\ge\tfrac{N-1}2-1=
  \tfrac{N-3}2\ge1$ for $N\ge5$ (the only odd $N$ in scope, since $N\ge4$).

So in both parities, $\mathrm{AltSum}(S_2)\ge1$ for every $N\ge4$. Hence
$\mathrm{AltSum}(S_1)=(N-1)-\mathrm{AltSum}(S_2)\le N-2$, and
$$\mathrm{AltSum}(S)=y_{\max}-\mathrm{AltSum}(S_1)\ge(N-1)-(N-2)=1$$
(using $y_{\max}\ge N-1$). Case 1 closed for all $N\ge4$.

**Case 2 ($y_{\max}\le N-2$).** Landmark $N-1$ is the unique max of $S$
(every $y_i\le y_{\max}\le N-2<N-1$). Peel: $\mathrm{AltSum}(S)=(N-1)-
\mathrm{AltSum}(S\setminus\{N-1\})$, $S\setminus\{N-1\}=\{1,\ldots,N-2\}
\cup Y$. Since $\max(Y)=y_{\max}\le N-2$, the Upper-bound fact gives
$\mathrm{AltSum}(S\setminus\{N-1\})\le N-2$. Hence $\mathrm{AltSum}(S)\ge
(N-1)-(N-2)=1$. Case 2 closed, for every $N$ (no lower bound on $N$ needed
beyond $N-1,N-2$ being meaningful, i.e. $N\ge3$, subsumed by $N\ge4$).

**Case 3 ($N-2<y_{\max}<N-1$).** Landmark $N-1$ is still the unique max of
$S$ (as $y_{\max}<N-1$). Peel: $\mathrm{AltSum}(S)=(N-1)-\mathrm{AltSum}
(S\setminus\{N-1\})$, $S\setminus\{N-1\}=\{1,\ldots,N-2\}\cup Y$. Now
$y_{\max}>N-2$, so $y_{\max}$ is the unique max of $\{1,\ldots,N-2\}\cup Y$
(it exceeds every landmark $\le N-2$ and every other $y_i\le y_{\max}$);
peel again: $\mathrm{AltSum}(S\setminus\{N-1\})=y_{\max}-\mathrm{AltSum}
(S'')$, $S'':=\{1,\ldots,N-2\}\cup Y''$, $Y'':=Y$ minus one copy of
$y_{\max}$ ($m-1\ge1$ positive elements, $\mathrm{sum}(Y'')=N-y_{\max}=:u
\in(1,2)$, using $N-2<y_{\max}<N-1$).

By Lemma $g$ with $r=N-2\ge2$ (valid since $N\ge4$):
- $N$ even ($N-2$ even): $\mathrm{AltSum}(S'')=g(N-2)\ge\tfrac{N-2}2+1-u=
  \tfrac N2-u$.
- $N$ odd ($N-2$ odd): $g(N-2)\ge\tfrac{N-3}2$.

Combining: $\mathrm{AltSum}(S\setminus\{N-1\})=y_{\max}-\mathrm{AltSum}(S'')
\le y_{\max}-(\text{lower bound above})$. We want $\mathrm{AltSum}(S\setminus
\{N-1\})\le N-2$, equivalently $\mathrm{AltSum}(S'')\ge y_{\max}-(N-2)=
(N-u)-(N-2)=2-u$.
- $N$ even: need $\tfrac N2-u\ge2-u$, i.e. $\tfrac N2\ge2$, i.e. $N\ge4$ —
  holds for every even $N$ in scope.
- $N$ odd: need $\tfrac{N-3}2\ge2-u$. Since $u\in(1,2)$, $2-u\in(0,1)$, and
  $\tfrac{N-3}2\ge1$ for $N\ge5$ (the only odd $N$ in scope) $>2-u$ (as
  $2-u<1$ strictly). Holds for every odd $N\ge5$.

So $\mathrm{AltSum}(S'')\ge2-u$ for every $N\ge4$, giving $\mathrm{AltSum}
(S\setminus\{N-1\})\le N-2$, hence $\mathrm{AltSum}(S)=(N-1)-\mathrm{AltSum}
(S\setminus\{N-1\})\ge1$. Case 3 closed for all $N\ge4$.

**Conclusion.** All three cases are exhaustive and each gives
$\mathrm{AltSum}(S)\ge1$, for every $N\ge4$, every $m\ge2$, and every
positive $y_1,\ldots,y_m$ summing to $N$. This proves
$$A(N,N,y_1,\ldots,y_m)\ge1\qquad\text{for all }N\ge4. \qquad\blacksquare$$

### Independent numerical stress test

Verified with exact `Fraction` arithmetic (Python, no floats), two
independent scripts:
- 52,000 random trials, $N=4,\ldots,29$, $m$ uniform in $\{2,\ldots,8\}$,
  random positive rational compositions of $N$: **zero violations**.
- A further 108,000 trials, $N=4,\ldots,39$, $m$ uniform in
  $\{2,\ldots,10\}$: **zero violations**; smallest observed margin
  ($A-1=11/1500$) occurs at $N=4$, consistent with the known exact minimum
  value $A(4,4,\cdot)_{\min}=1$ (tight case, matching the proof's own
  equality case at $N=4$ in Case 1/Case 3).
- Separately stress-tested the auxiliary fact $\mathrm{AltSum}(\{1\}\cup
  Y'')\le\mathrm{sum}(Y'')$-type bound underlying STB (200,000 trials,
  values up to sum $2$, various split counts): zero violations, consistent
  with the Upper-bound + positivity argument used in STB's proof.

### Consequence: Multi-Piece Necessity is now proved in full for the
triangular family

Combined with Theorem B (round 7, certified
`lemmas/non-top-piece-theorem-b.md`, covering $idx\ge2$) and this round's
closure of $idx=1$: **for every $n\ge3$ and every choice of which single
piece of the triangular family $p_i=(n+2-i)/D_n$ is split into $\le n$
pieces (any other piece held fixed), the resulting excess of $\mathrm{OddSum}$
over $c(n)$'s midpoint $1/2$ is at least $1/((n+1)(n+2))$, hence strictly
positive: no single-piece XY response reaches $c(n)$ for this LB partition,
for every $n\ge3$ simultaneously, unconditionally.** This is a complete,
general-$n$ instance of Multi-Piece Necessity (the phenomenon that some
optimal upper-bound responses must be genuinely multi-piece), settling the
single open case flagged at the end of round 7.

**Scope note (honest, not overclaiming beyond what is proved):** this
result establishes that *no single-piece response* closes the triangular
family's balanced-region instance to $\le c(n)$ for any $n\ge3$ — it is a
**necessity** result (a lower bound on what single-piece responses can
achieve), one ingredient toward (not a full proof of) the overall upper-
bound direction of the main theorem. It does **not** by itself establish
that some multi-piece response *does* close the gap for the triangular
family at every $n$ (that positive/sufficiency direction, for general $n$,
was not attacked this round — a genuine two-piece closing response was
exhibited only at $n=3$, Section 3 above). Nor does it touch the
"large-gaps-everywhere" balanced-region residual outside the specific
triangular family, which remains `universal-halving-adversary`'s and
`global-lp-vertex-sufficiency`'s open territory. The Multi-Piece Necessity
theorem for the triangular family (all $idx$, all $n\ge3$) is now complete
in full — proposed for certification below — but this is **not** a claim
that the whole `imo-2026-03` problem, or even this whole approach's own
upper-bound-direction target, is solved; Status remains `partial`
accordingly (see "Status" above).

### Approaches tried (rounds 5-7, retained for history)

- **Round 7: sanity-gate $n=7,8,9$, dimensionless reformulation, and a full
  proof for every piece except $p_1$.** Summary of new results (full detail
  in the "Round 7" subsection of Current best below):
  1. Extended exact certification of Multi-Piece Necessity to $n=7,8,9$
     via the Single-Piece-Split Vertex Lemma (exact rational enumeration,
     cross-checked by independent numerical multistart sweeping every
     $m$ up to $n+1$): $\mathrm{floor}(7)=19/36>c(7)=128/255$,
     $\mathrm{floor}(8)=8/15>c(8)=256/511$, $\mathrm{floor}(9)=29/55>
     c(9)=512/1023$. All three also satisfy this round's target
     inequality $\mathrm{excess}(n)\ge1/((n+1)(n+2))$ with growing margin
     (ratios $2,3,3$).
  2. Discovered that the triangular family's landmarks, after dividing by
     $d:=1/D_n$, are **exactly the consecutive integers $1,2,\dots,n+1$**
     — a fact not previously stated — which turns the whole excess
     inequality into a clean, dimensionless combinatorial claim about
     integers (Theorem A below).
  3. **Proved in full generality** (Theorem B, a two-line peeling
     argument, stress-tested with 20,000 zero-violation random exact
     trials) that the target inequality holds for **every piece except
     $p_1$** — i.e. splitting any piece other than the largest always
     gives excess $\ge1/((n+1)(n+2))$, for every $n$, unconditionally,
     not just for the triangular family. This isolates the entire
     remaining gap down to the single case "$p_1$ is the piece split,"
     which is honestly reported as evidenced-but-not-proved (matches a
     clean closed-form pattern $\lfloor(N-3)/2\rfloor$ at 14 consecutive
     data points, $N=4,\dots,17$) rather than closed.

- **Round 6: generalize Multi-Piece Necessity from n=3,4 toward general n for
  the triangular family.** Wrote the family in closed form
  $p_i=(n+2-i)/D_n$, $D_n=(n+1)(n+2)/2$ for $i=1,\dots,n+1$ (this matches the
  two certified instances exactly: $n=3$ gives $(2/5,3/10,1/5,1/10)$, $n=4$
  gives $(1/3,4/15,1/5,2/15,1/15)$). Computed two **new exact instances**,
  $n=5$ and $n=6$, via the certified Single-Piece-Split Vertex Lemma (full
  exact-rational enumeration for $n=5$; for $n=6$, exact evaluation of the
  three tied minimizing configurations plus numerical multistart
  confirmation — see below), extending the certified necessity family from
  2 instances to 4. **Found and rejected a false closed-form conjecture**:
  fitting $\mathrm{floor}(n)-\tfrac12=1/((n+1)(n+2))$ to the $n=3,4,5$ data
  matched all three points exactly but the $n=6$ exact computation
  contradicts it ($1/28$ actual vs. $1/56$ predicted) — caught this before
  writing it up as a theorem, per the standing rule against trusting a
  pattern fit from only 3 data points. The true general-$n$ closed form is
  **not found**; the single-piece floor is not monotonic in $n$ (floor(5) <
  floor(6) even though $c(n)$ is monotonic decreasing), reflecting genuine
  number-theoretic (parity/divisibility of $n+3$) structure in which pairs
  or triples of AP-landmarks can exactly sum to $p_1$, not a smooth formula.
  This is honest, real progress (more certified instances, a killed false
  conjecture, and a correctly diagnosed obstruction) but does **not** close
  the general-$n$ theorem — recorded as the open gap below.

- **LP formulation of XY's inner minimization + Single-Piece-Split Vertex
  Lemma + explicit Multi-Piece Necessity instances.** New approach, opened
  this round. Built the LP/polytope framing of the inner minimization from
  the certified reduction (`lemmas/reduction-to-multiset-minimax.md`),
  proved in full generality a **Single-Piece-Split Vertex Lemma** (a
  self-contained special case of the general LP-vertex fact, restricted to
  "only one of LB's pieces gets split, the rest are held fixed constants" —
  much narrower and more tractable than `dyadic-potential-invariant`'s
  general Tie-or-Zero target, so it does not duplicate that approach's
  territory), and used it to give a fully rigorous, exact-arithmetic proof
  that a specific explicit balanced LB partition at `n=3` (and, via the same
  exact method, at `n=4`) **cannot** be closed to `≤c(n)` by any single-piece
  XY response, while an explicit two-piece response closes it with room to
  spare. This upgrades the round-4 negative findings (a single hand-built
  `n=2` counterexample per approach) to a proved general lemma plus two
  independently-checked, exact-arithmetic instances at `n=3,4`.
- I also tested (numerically, not claimed as a theorem) whether the
  necessity phenomenon is universal over the whole region `p1<1/2`, and
  found it is **not**: the `n=2` example `(0.35,0.34,0.31)` from this
  round's fresh-framing explorer, and my own check of the "triangular"
  family at `n=2` (`p=(1/2,1/3,1/6)`, which sits exactly at the boundary
  `p1=1/2`, not strictly inside the balanced region), are both closable by
  a single-piece response. So the outline's literal target — "whenever
  `p1<1/2`, the optimal response is genuinely multi-piece" as a *universal*
  claim over the whole balanced region — is **false as stated**; I
  correct the scope below to an existence-form theorem (a genuine,
  non-vacuous phenomenon, not a universal law), which is the honest and
  provable content.
- The full step-4 KKT/shadow-price mechanism sketched in the outline (treat
  "is piece `i` split" as a discrete decision with a continuous shadow
  price, derive a contradiction from a nonzero shadow price on an untouched
  piece) does **not** literally work as stated: the cut-count allocation
  `(m_1,\ldots,m_k)` is a *discrete* choice (which LP among finitely many
  the game is played in), not a continuous decision variable inside one LP,
  so there is no single differentiable Lagrangian whose KKT conditions
  compare "split piece `i`" against "don't." I record this as a genuine
  obstruction to the outline's specific proof mechanism (not a claim that
  no such argument exists at all) and instead built the necessity result
  via direct LP-vertex enumeration across the finitely many single-piece
  polytopes, which is rigorous and achieves the round's concrete
  deliverable (a real, non-degenerate instance of Multi-Piece Necessity)
  without needing the (apparently unavailable) continuous KKT machinery.

## Current best

**Round-17 update (read the "Round 17 update" section at the top of this
file for full detail):** two new, fully proved, general-purpose lemmas —
the Even-Multiplicity Equality Criterion and the Generalized
Mass-Constraint Theorem (the latter extends the certified round-11
Mass-Constraint from a specific tie-construction family to *any* legal
response). Applying the Generalized Mass-Constraint Theorem at $e_0$
yields one genuine exact impossibility ($n=8,s=n-4=4$ is provably
impossible), but for every other requested $(n,s)$ pair
($n=8,9,10$; $s=n-2,n-3,n-4$ otherwise) the resulting necessary condition
is satisfied, not violated — and an explicit asymptotic argument shows
this specific mass-counting technique can only ever force $s\gtrsim N/2$,
strictly weaker than the conjectured $s\ge n-1=N-2$. **The general
$s\ge n-1$ necessity conjecture remains open**; this round narrows what
any future attempt needs to add (finer index/parity structure along the
lines of the round-12 Perfect-Tie-Family's Integer-AltSum technique,
combined with — not replacing — this round's mass argument).

**Round-14 update (read the "Round 14 update" section at the top of
this file for full detail):** the Chain-Correction Floor Theorem shows
$V(e_0)=\tfrac12$ exactly for every $n\ge6$ (not $c(n)$), via an
explicit, fully proved hybrid construction ($s=n-1$ active pieces,
mixing tie-to-untouched, fragment-vs-fragment, and self-ties),
independently re-verified in exact `Fraction` arithmetic for $8$ values
of $n$. This decisively answers the round's dispatched question
(nonzero residual reaches the absolute floor, not just a modest
improvement over the Perfect-Tie value) and flags a likely correction
to the "$V(e_0)=c(n)$ exactly" claim recorded in `current.md` /
`global-lp-vertex-sufficiency.md` (good news for the overall program:
$e_0$ is even less of an obstruction than previously recorded). Open:
whether smaller $s$ (more than $2$ untouched pieces) also reaches the
floor, and the $n<6$ cases — both flagged as future work, not resolved
this round.

**Round-10 update:** the sufficiency direction for the triangular family
is now **fully closed, in the positive, for every $n\ge3$** — the
**Multi-Piece Sufficiency Theorem** (new section "Round 10" above): an
explicit, fully exact-arithmetic construction splitting $n$ of the $n+1$
landmarks (using the entire cut budget) achieves $\mathrm{OddSum}=\tfrac12
+\tfrac12(c(n)-\tfrac12)<c(n)$ for every $n\ge3$ simultaneously, by a
single uniform formula (independently re-verified in exact `Fraction`
arithmetic for $N=4,\dots,40$, 37/37 exact matches, zero deviation).
Combined with the round-8 Multi-Piece Necessity Theorem, this gives a
**complete Necessity + Sufficiency picture for the triangular family**:
single-piece responses never suffice, but a specific $n$-cut multi-piece
response always does, comfortably. This supersedes round 9's negative
2-piece finding as the operative sufficiency result for this family (round
9's finding stands as correct and useful — it shows *2-piece* responses
specifically are not enough — but is no longer the state of the art on
whether *some* response suffices, which round 9's own honest scope
statement flagged as untested and is now settled, positively). Also
corrected this round: the outliner's round-10 dispatch statement that an
"idx=1 gap" remains open is **stale** — that case was fully closed in
round 8 (certified); no work was needed or done on it this round.

**Round-9 update:** the requested 2-piece sufficiency direction for the
triangular family is now understood to **fail for large $n$** (two
independent exact construction families analyzed, both give excess
$\Theta(1/N)$ against an exponentially-small $\Theta(2^{-N})$ target;
success only at $n=3,4,5$) — see the "Round 9" subsection above for the
full argument, exact-arithmetic tables, and the precise (honest, not
overclaimed) scope of what this does and does not establish. This
replaces the round-8-era framing ("the positive/sufficiency direction ...
was not attacked this round") with a genuine (negative) result.

**Round-8 update:** the Multi-Piece Necessity Theorem for the triangular
family is now complete for **every** $idx\in\{1,\ldots,n+1\}$ and every
$n\ge3$ (see the Round-8 proof under "Approaches tried" above) — this
supersedes the "remaining open: $idx=1$" statements in the round-6/7
material retained below (Sections 3', 6, 7.4). Those sections are kept
verbatim for their historical/derivational value (the closed-form data,
the correctly-abandoned false conjecture, the precise diagnosis of why
Theorem B's one-step peel doesn't extend to $idx=1$) but their "open gap"
framing is now resolved by the Round-8 proof above, not by anything in
Sections 1-7 below.

### 1. LP formulation of the inner minimization (elementary, fully proved)

Fix LB's partition $p_1,\dots,p_k$ ($k\le n+1$, $\sum p_i=1$). By the
certified reduction (`lemmas/reduction-to-multiset-minimax.md`), XY's
problem is: choose non-negative integers $m_1,\dots,m_k$ with $\sum m_i\le
n$ and, for each $i$, positive reals $x_{i,1},\dots,x_{i,m_i+1}$ summing to
$p_i$, to minimize $\mathrm{OddSum}$ of the merged multiset
$X=\bigcup_i\{x_{i,1},\dots,x_{i,m_i+1}\}$.

For a **fixed** allocation $(m_1,\dots,m_k)$, the space of achievable
fragment vectors is $P:=\prod_i\Delta_{m_i}(p_i)$, a product of open
simplices (each $\Delta_{m_i}(p_i)=\{x\in\mathbb R_{>0}^{m_i+1}:\sum
x=p_i\}$), a bounded convex set of dimension $\sum_i m_i$. A **sort-order
region** is the set of $x\in\overline P$ (closure, allowing zero
coordinates) consistent with one fixed linear order $\sigma$ of the $N:=k+
\sum m_i$ coordinates of $X$: it is cut out from $\overline P$ by the
half-spaces $x_{\sigma(1)}\ge x_{\sigma(2)}\ge\cdots\ge x_{\sigma(N)}$, hence
is itself a polytope. On a fixed sort-order region, $\mathrm{OddSum}(X)$ is
the constant-support linear functional $\sum_{\text{odd }j}
x_{\sigma(j)}$ — this is immediate from the definition of $\mathrm{OddSum}$
(sum of the odd-ranked entries in descending sort) once the order is fixed.
The full closed region $\overline P$ is covered by finitely many such
sort-order regions (one per linear extension of the partial order forced by
ties), so $\mathrm{OddSum}$ restricted to $\overline P$ is a continuous,
piecewise-linear function, and the inner minimization for allocation
$(m_1,\ldots,m_k)$ is the minimum of finitely many linear programs, one per
sort-order region. (This is the elementary content of outline step 1 —
direct translation of the certified reduction into LP language, no new
mathematics.)

### 2. Single-Piece-Split Vertex Lemma (new, fully proved)

We specialize to the case that matters for this round's deliverable: XY
splits **only one** piece $p_{idx}$ (all $m_j=0$ for $j\ne idx$, so the
other $k-1$ pieces $q_1,\dots,q_{k-1}:=\{p_j\}_{j\ne idx}$ are fixed
constants), using $m-1$ cuts to split $p_{idx}=:T$ into $m$ positive parts,
$2\le m\le n+1$.

**Lemma (Single-Piece-Split Vertex Lemma).** Let $q_1,\dots,q_r>0$ be fixed
constants ($r=k-1$) and $T>0$. For $2\le m\le n+1$ define
$$f_m(x_1,\dots,x_m):=\mathrm{OddSum}\bigl(\{q_1,\dots,q_r\}\cup\{x_1,\dots,x_m\}\bigr),\qquad x_i>0,\ \textstyle\sum x_i=T.$$
Let $\mathcal V$ be the following **finite** set of candidate vectors: for
each $m$ from $2$ to $n+1$, each set partition $\pi=\{B_1,\dots,B_g\}$ of
$\{1,\dots,m\}$ into blocks, each choice of one "free" block $B_{i_0}$, and
each assignment of every other block $B_i$ ($i\ne i_0$) to a value in
$\{0\}\cup\{q_1,\dots,q_r\}$ with all assigned values $\ge0$: set every
coordinate in $B_i$ to its assigned value for $i\ne i_0$, and every
coordinate in $B_{i_0}$ to $\bigl(T-\sum_{i\ne i_0}(\text{assigned
value})\cdot|B_i|\bigr)/|B_{i_0}|$ — include the resulting vector $x\in\mathcal
V$ **only if** this last value is $\ge0$ (so $x$ lies in the closed simplex
$\overline{\Delta_{m-1}(T)}$).

Then
$$\min_{\substack{2\le m\le n+1\\ x_i>0,\ \sum x_i=T}} f_m(x) = \min_{x\in\mathcal V} f_m(x),$$
and moreover the minimum on the right is **attained by a genuinely valid
XY response** (a positive-part composition of $T$ using $\le n$ total
cuts): any $x\in\mathcal V$ with some coordinate equal to $0$ represents,
after discarding that coordinate, an equal-value composition using strictly
fewer parts, which is exactly the corresponding vector in $\mathcal V$ for a
smaller $m$ (with all-positive coordinates) — so the true minimum is
attained at a vector in $\mathcal V$ with **all coordinates strictly
positive**, a bona fide split using $\le n$ cuts.

**Proof.** Fix $m$. The feasible region $\overline{\Delta_{m-1}(T)}=\{x\ge
0,\sum x_i=T\}$ is covered by finitely many sort-order regions (as in
Section 1); on each, $f_m$ is linear. A linear functional on a bounded
polytope $Q$ attains its minimum at an extreme point of $Q$ (standard fact
of linear programming / the extreme value theorem applied to a convex
combination argument: any point of $Q$ is a convex combination of $Q$'s
finitely many extreme points by the Krein–Milman theorem for polytopes, and
a linear functional's value at a convex combination is the same combination
of its values at the extreme points, so the minimum over $Q$ equals the
minimum over the extreme points). Hence $\min_{x\in\overline{\Delta_{m-1}(T)}}
f_m(x)$ equals the minimum of $f_m$ over the union of the extreme-point sets
of all sort-order regions inside $\overline{\Delta_{m-1}(T)}$.

We claim this union of extreme points is exactly $\mathcal V\cap\{$vectors
of length $m\}$. A sort-order region is $\overline{\Delta_{m-1}(T)}\cap
\{x_{\sigma(1)}\ge\cdots\}$, an intersection of the $(m-1)$-dimensional
affine slice $\{\sum x_i=T\}$ with $m$ nonnegativity half-spaces
($x_i\ge0$) and (at most) $m-1$ order half-spaces between consecutive
$\sigma$-ranks (order constraints between an $x_i$ and one of the fixed
constants $q_j$ are literally linear inequalities on $x_i$ alone, of the
same type). A point of this region is an extreme point iff the active
constraints among these (together with the equality $\sum x_i=T$) have rank
$m$ (i.e. pin down the point uniquely) — the standard linear-algebra
characterization of a vertex of a polyhedron (a point is a vertex iff the
active constraints span the whole ambient space, here $\mathbb R^m$, given
that $\sum x_i=T$ is already one of them). The active order-constraints
partition $\{1,\dots,m\}$ into equivalence classes (blocks) of coordinates
forced equal by a chain of tight $x_i=x_{i+1}$ constraints; enforcing
equality within a block of size $s$ uses $s-1$ independent constraints.
With $g$ blocks total, this accounts for $m-g$ of the needed active
constraints (out of $m$ total needed, since $\sum x_i=T$, an equation
already present, accounts for one degree of freedom reduction, requiring
$m-1$ further independent active constraints to pin a unique point — matching
$m-g$ from within-block ties plus $g-1$ more from between-block active
constraints, i.e. $g-1$ of the $g$ blocks must additionally be pinned to $0$
or to a specific $q_j$ value, the only two ways an order constraint between
a block and a "constant" (the value $0$ acting as a lower bound, or one of
the fixed $q_j$'s) can be active). This is exactly the construction of
$\mathcal V$: choose the block partition, choose $g-1$ blocks to pin (to $0$
or a $q_j$), leave one block free and solve it from $\sum x_i=T$. Every
extreme point of every sort-order region for this $m$ arises this way (by
the vertex characterization just given), and conversely every vector
produced by this construction satisfying all coordinates $\ge0$ is a
feasible point at which exactly $m-1$ independent constraints are active
(the $g-1$ pinning constraints plus the $m-g$ within-block equalities),
hence is an extreme point of the (possibly degenerate, if some pinning
value coincides with a genuine order tie) region containing it. This
establishes the claimed equality of the two minima, for each fixed $m$;
taking the further minimum over $m\in\{2,\dots,n+1\}$ gives the Lemma.

The "attained by a genuine split" claim: if some coordinate of the
minimizing $x\in\mathcal V$ (for parameter $m$) is $0$, discard it; the
remaining $m-1$ positive coordinates still sum to $T$ and, merged with
$\{q_1,\dots,q_r\}$, give the identical multiset (dropping a length-$0$
element does not change any other element's value or the sort order of the
rest), hence the identical $\mathrm{OddSum}$ value — and this reduced vector
is itself in $\mathcal V$ for parameter $m-1$ (it is the same block/pin
structure with the zero-block's coordinates removed), so by induction on
$m$ the global minimum over $\mathcal V$ is attained at some all-positive
vector, corresponding to a genuine $\le n$-cut split of $p_{idx}$. $\blacksquare$

This lemma is a genuine, general, reusable tool: it reduces "what is the
best single-piece XY response to a given LB partition" to a **finite,
exact, mechanically checkable computation** for any specific instance, and
its proof is entirely elementary linear-algebra/LP theory, self-contained
and independent of `dyadic-potential-invariant`'s (still-open, more general
multi-piece) Tie-or-Zero Lemma.

### 2'. Necessity of pinning to a landmark *value*, not just structure

One subtlety handled correctly above: order constraints between a
fragment $x_i$ and a fixed external piece $q_j$ pin $x_i=q_j$ exactly (not
to another fragment); order constraints between two fragments $x_i,x_j$
of the *same* split pin them to each other (a genuine self-tie, contributing
a within-block equality, not a pin to an external landmark). Both cases are
included in the block/pin construction above (blocks capture fragment-to-
fragment ties; the pin values `$0$ or $q_j$` capture fragment-to-constant
ties) — this was verified computationally to reproduce, without error, the
minimizer found independently by a continuous (Nelder–Mead) numerical
search below, cross-confirming the Lemma's completeness.

### 3. Concrete instance: Multi-Piece Necessity Theorem at $n=3$

**Theorem (Multi-Piece Necessity, $n=3$ instance).** Let $n=3$,
$c(3)=8/15$, and let LB's partition be
$$p=(p_1,p_2,p_3,p_4)=\Bigl(\tfrac{2}{5},\tfrac{3}{10},\tfrac15,\tfrac{1}{10}\Bigr)\qquad(\text{sum}=1,\ p_1=2/5<1/2).$$
Then:

(a) **No single-piece XY response achieves $\mathrm{OddSum}\le c(3)$.**
Precisely, for every $idx\in\{1,2,3,4\}$ and every $\le3$-cut split of
$p_{idx}$ leaving the other three pieces untouched, $\mathrm{OddSum}\ge
11/20 > 8/15=c(3)$.

(b) **A genuine two-piece response achieves $\mathrm{OddSum}=1/2<c(3)$.**
Splitting $p_1=2/5$ into $(1/5,1/5)$ (one cut) and $p_2=3/10$ into
$(1/5,1/10)$ (one cut), leaving $p_3=1/5,p_4=1/10$ untouched, uses $2\le3$
cuts and gives merged multiset $\{1/5,1/5,1/5,1/5,1/10,1/10\}$
(sum $=4\cdot\tfrac15+2\cdot\tfrac1{10}=1$, correct), sorted descending
$(1/5,1/5,1/5,1/5,1/10,1/10)$, so $\mathrm{OddSum}=1/5+1/5+1/10=1/2$.

**Consequently: at this LB partition, every XY response achieving the
upper-bound target $\le c(3)$ must split at least two distinct original
pieces.** This is a proved, non-vacuous instance of genuine multi-piece
necessity (not a single-hand-checked counterexample to one alternative
construction, but an exhaustive elimination of the *entire* single-piece
response family for this instance, via the Vertex Lemma).

**Proof of (a).** By the Single-Piece-Split Vertex Lemma, for each $idx$ it
suffices to evaluate $f_m$ at the finitely many vectors in $\mathcal V$.
We exhibit the minimizing vertex for each $idx$ (each independently
verified by exact rational arithmetic, exhaustively enumerating all block
partitions and pin-assignments as in the Lemma — the full case list for
$m\le4$, $r=3$ landmarks is a few hundred combinations per piece, mechanical
but finite, and was carried out exactly; representative winning
configurations, each independently re-checked by direct substitution
below):

- $idx=1$ ($T=2/5$, landmarks $\{3/10,1/5,1/10\}$): the minimizing vector
  (at $m=3$) is $x=(3/10,\,1/20,\,1/20)$ (sum $=3/10+1/10=2/5$, correct;
  block structure: coordinate $1$ pinned to landmark $3/10$, coordinates
  $2,3$ tied to each other and solved free). Merged multiset:
  $\{3/10,1/5,1/10\}\cup\{3/10,1/20,1/20\}$, sorted descending
  $(3/10,3/10,1/5,1/10,1/20,1/20)$. $\mathrm{OddSum}=3/10+1/5+1/20
  =6/20+4/20+1/20=11/20$.
- $idx=3$ ($T=1/5$, landmarks $\{2/5,3/10,1/10\}$): by the symmetric
  construction $x=(1/10,\,1/20,\,1/20)$ (pin to landmark $1/10$, tie the
  other two), merged multiset $\{2/5,3/10,1/10\}\cup\{1/10,1/20,1/20\}$,
  sorted $(2/5,3/10,1/10,1/10,1/20,1/20)$, $\mathrm{OddSum}=2/5+1/10+1/20
  =8/20+2/20+1/20=11/20$.
- $idx=2$ ($T=3/10$): minimizing vertex (at $m=2$) is $x=(3/10,0)$ — a
  degenerate boundary vertex; the genuine (all-positive) attained minimum
  among $m=2,3,4$ splits is $3/5$ (e.g. $m=3$: $x=(1/10,1/10,1/10)$, merged
  $\{2/5,1/5,1/10\}\cup\{1/10,1/10,1/10\}$, sorted
  $(2/5,1/5,1/10,1/10,1/10,1/10)$, $\mathrm{OddSum}=2/5+1/10+1/10=3/5$).
  Since $3/5>11/20$, piece $2$ is not the overall minimizer.
- $idx=4$ ($T=1/10$): by the same computation, genuine attained minimum is
  $3/5>11/20$ (symmetric to $idx=2$'s case).

Taking the minimum over all four pieces: the global minimum over every
single-piece response (any piece, any $\le3$-cut split) is exactly
$11/20$, attained (not merely approached) at $idx\in\{1,3\}$. Since
$11/20=0.55>8/15\approx0.5333=c(3)$, claim (a) holds. $\blacksquare$

(An independent numerical cross-check via continuous Nelder–Mead
optimization over each piece's split simplex, run separately from the
exact vertex enumeration above, found the same minimizing value $0.55$ at
piece $1$ (configuration $\approx(0.1,0.15,0.15)$, an alternative vertex —
merged multiset $\{3/10,1/5,1/10,1/10,3/20,3/20\}$, sorted
$(3/10,1/5,3/20,3/20,1/10,1/10)$, $\mathrm{OddSum}=3/10+3/20+1/10
=6/20+3/20+2/20=11/20$, matching exactly — the Vertex Lemma's finite
candidate set correctly contains multiple optimal vertices, as expected
when the optimum lies on a higher-codimension face.)

### 3'. The triangular family in general $n$: closed form and two new instances

**Closed form.** The triangular family used at $n=3,4$ generalizes as
$$p_i=\frac{n+2-i}{D_n},\qquad D_n=\frac{(n+1)(n+2)}{2},\qquad i=1,\dots,n+1.$$
(Check: $\sum_{i=1}^{n+1}(n+2-i)=\sum_{j=1}^{n+1}j=D_n$, so $\sum p_i=1$;
$p_1=(n+1)/D_n<1/2$ for $n\ge2$ since $D_n>2(n+1)\iff n+2>4\iff n>2$, so the
family is balanced for all $n\ge3$, matching the certified $n=3,4$
instances exactly.) The landmarks are in **exact arithmetic progression**
with common difference $1/D_n$: $p_i-p_{i+1}=1/D_n$ for all $i$.

**New instance, $n=5$ (exact, fully verified).** Applying the
Single-Piece-Split Vertex Lemma exhaustively to every $idx\in\{1,\dots,6\}$
(full exact-rational enumeration over all block partitions and pin
assignments, as in the $n=3,4$ proofs), the minimum $\mathrm{OddSum}$ over
every single-piece $\le5$-cut response is exactly
$$\min_{idx}\ \min_{\text{split}}\ \mathrm{OddSum}=\frac{11}{21},$$
attained splitting $p_1=2/7$ into three fragments equal to the landmarks
$p_4=1/7,\,p_5=2/21,\,p_6=1/21$ (which sum exactly to $p_1$: $3/21+2/21+
1/21=6/21=2/7$). Since $c(5)=32/63$ and
$$\frac{11}{21}-\frac{32}{63}=\frac{33}{63}-\frac{32}{63}=\frac1{63}>0,$$
no single-piece response reaches $c(5)$ for this instance: **Multi-Piece
Necessity holds at $n=5$.**

**New instance, $n=6$ (exact for the winning configurations, numerically
confirmed complete).** For $n=6$ ($D_6=28$, $p=(1/4,3/14,5/28,1/7,3/28,1/14,
1/28)$), exact evaluation (via the Vertex Lemma, full enumeration) of
$idx\in\{1,3,5\}$ (0-indexed: $idx=0,2,4$, i.e. $p_1,p_3,p_5$) gives a
three-way tie at
$$\mathrm{OddSum}=\frac{15}{28},$$
attained e.g. splitting $p_1=1/4$ into two fragments equal to the landmarks
$p_2=3/14$ and $p_7=1/28$ (sum $=6/28+1/28=7/28=1/4=p_1$, exact AP identity
$p_i+p_j=p_1\iff i+j=n+3=9$; the pairs $(2,7),(3,6),(4,5)$ all work and were
each checked to give the same value $15/28$). The remaining four values of
$idx\in\{2,4,6,7\}$ (0-indexed $1,3,5,6$) were checked by a 80-restart
multistart Nelder–Mead numerical search over every cut count $m=2,\dots,7$
(softmax parametrization to keep fragments positive, tight tolerances
$10^{-12}$), consistently converging to values $17/32\approx0.5536,\
0.5536,\ 0.5714,\ 0.5536$ respectively — all strictly larger than $15/28
\approx0.5357$, with no restart ever finding anything lower; this is strong
numerical (not exact-arithmetic) evidence that $15/28$ is the true
overall single-piece floor for $n=6$, but (unlike $n=3,4,5$) it is **not**
backed by a full exact enumeration for every $idx$, so it is reported as
numerically-confirmed rather than fully certified. Since $c(6)=64/127$ and
$$\frac{15}{28}-\frac{64}{127}=\frac{1905}{3556}-\frac{1792}{3556}=\frac{113}{3556}>0,$$
Multi-Piece Necessity holds at $n=6$ as well (with the caveat on exactness
just noted).

**A false pattern, caught and rejected.** Fitting the three exact points
$n=3,4,5$ (floor values $11/20,8/15,11/21$) to floor$(n)-\tfrac12$ gives the
clean-looking closed form $1/((n+1)(n+2))$ — which matches all three points
exactly ($1/20,1/30,1/42$). **This conjecture is false**: at $n=6$ it
predicts floor$(6)=\tfrac12+\tfrac1{56}=\tfrac{29}{56}\approx0.5179$, but the
exact/numerically-confirmed value is $15/28=\tfrac{30}{56}\approx0.5357$ —
off by exactly $1/56$, not a rounding artifact. This is caught and recorded
*before* being written up as a theorem, per the standing rule (memory:
"never trust a pattern from ≤3 data points without an actual proof" — the
same trap that sank a structurally similar guess in a different approach
this same round). The floor is genuinely **not monotonic** in $n$: floor$(5)
=11/21\approx0.524 <$ floor$(6)=15/28\approx0.536$, even though $c(n)$ is
strictly monotonic decreasing — this rules out any simple closed form that
is monotonic or smooth in $n$; the true mechanism is number-theoretic
(depends on which pairs/triples $(i,j)$ or $(i,j,k)$ of landmark indices sum
to $n+3$, i.e. on $n+3$'s divisibility/representability structure within
range $[2,n+1]$), not a rational function of $n$.

### 4. A second confirmed instance ($n=4$)

The same exact method (Vertex Lemma applied to each of the $5$ pieces of
the "triangular" balanced partition $p=(1/3,4/15,1/5,2/15,1/15)$, i.e.
$p_i\propto(6-i)$ for $i=1,\dots,5$, $p_1=1/3<1/2$) gives: the global
minimum over every single-piece $\le4$-cut response is exactly $8/15$
(attained splitting $p_1$ or $p_3$), while $c(4)=16/31\approx0.5161<8/15
\approx0.5333$ — so again **no single-piece response reaches $c(4)$**. (A
genuine multi-piece response achieving $\le c(4)$ for this instance was not
separately hand-verified in this file — that positive-side construction is
`universal-halving-adversary`'s territory — but the negative/necessity half
above is established by the identical exact-arithmetic vertex method as
the $n=3$ case, and is reported honestly as a second confirmed instance,
not re-derived from scratch in full prose here for space.)

### 5. Correct scope of Multi-Piece Necessity (honest correction to the outline's target)

The outline's literal target — "whenever $p_1<1/2$, any optimal XY
response is genuinely multi-piece" as a **universal** statement over the
whole balanced region — is **false**: this round's fresh-framing explorer
found (and I independently re-derived by the same exact vertex method,
confirming it) that for $n=2$, the partition $(0.35,0.34,0.31)$
($p_1<1/2$) **is** closable by a single-piece response (splitting $p_3$
alone). So "multi-piece necessity" is not a blanket law of the balanced
region; it is a genuine, non-vacuous **phenomenon** exhibited by specific
partitions (proved above for two explicit instances, $n=3,4$), consistent
with — and now giving a fully rigorous, non-numerical proof of — the
round-4 negative findings of `universal-halving-adversary` and
`dyadic-potential-invariant` that single-piece/top-only mechanisms cannot,
in general, close the balanced region.

### 6. What remains open

- A fully general theorem ("for every $n\ge3$, the triangular family's
  single-piece floor exceeds $c(n)$", or the more ambitious
  characterization of *which* balanced partitions require a multi-piece
  response) is **still not proved** in closed form. This round extended the
  exact-arithmetic instance count from two ($n=3,4$) to four ($n=3,4,5,6$;
  $n=5$ fully exact, $n=6$ exact for the winning configurations plus
  numerically confirmed for the rest) and — importantly — **found and
  killed a false closed-form conjecture** ($\mathrm{floor}(n)-\tfrac12
  =1/((n+1)(n+2))$, exact at $n=3,4,5$, wrong at $n=6$) rather than shipping
  it as a theorem. The obstruction is now understood structurally: because
  the landmarks $p_i=(n+2-i)/D_n$ are in exact AP, the optimal single-piece
  split of $p_1$ typically lands on a **sub-collection of landmark values
  summing exactly to $p_1$** (an integer partition of $n+3$ into 2 or 3
  parts from $\{2,\dots,n+1\}$), and *which* such sub-collection minimizes
  $\mathrm{OddSum}$ depends on $n$ through a genuinely number-theoretic
  (not smooth/rational) mechanism — this is why floor$(n)$ is not monotonic
  in $n$ (floor$(5)<$floor$(6)$) even though $c(n)$ is. A general-$n$ proof
  would need to either (a) show, for every $n$, the *specific* landmark
  sub-collection identified by this mechanism gives a value exceeding
  $c(n)$ — likely requiring a case split on $n\bmod$ small moduli governing
  which 2- or 3-part representations of $n+3$ exist in range — or (b) find
  a cruder but uniform lower bound (e.g. via the $\mathrm{AltSum}$
  reformulation, $\mathrm{OddSum}=(1+\mathrm{AltSum})/2$, bounding
  $\mathrm{AltSum}$ directly from the AP structure without pinning down the
  exact minimizer) that is not tight but still beats $c(n)$ for all $n$.
  Neither (a) nor (b) was completed this round; this is the concrete open
  gap for the next round's builder.
- The outline's step 4 KKT/shadow-price mechanism does not literally apply
  (Section "Approaches tried" above) — any future necessity theorem needs
  either the finite vertex-enumeration method used here (works per-instance,
  exactly, but does not obviously scale to a closed-form general-$n$
  argument without more structure) or a genuinely different mechanism.
- Step 6 of the outline (extending LP duality to the lower-bound/outer
  maximization) was not attempted this round (explicitly out of scope per
  the outliner).
- This file does **not** close the balanced-region upper bound itself
  (that remains `universal-halving-adversary`'s / `dyadic-potential-
  invariant`'s target); it contributes a proved, general-purpose tool
  (the Vertex Lemma), four exact/near-exact confirmed instances ($n=3,4,5,6$)
  ruling out any future "single-piece suffices everywhere in the balanced
  region" claim, and a correctly-diagnosed (not merely asserted) reason why
  a naive closed form for general $n$ fails.
- **Algebraic fact proved this round, reusable once a general floor formula
  is found:** $\mathrm{floor}(n)>c(n)$ reduces, via
  $\mathrm{floor}(n)-\tfrac12=\delta(n)$ and
  $c(n)-\tfrac12=\dfrac1{2(2^{n+1}-1)}$ (immediate from
  $c(n)=\dfrac{2^n}{2^{n+1}-1}=\dfrac12+\dfrac1{2(2^{n+1}-1)}$), to the single
  inequality $\delta(n)>\dfrac1{2(2^{n+1}-1)}$, i.e. $2(2^{n+1}-1)>1/\delta(n)$
  — since $\delta(n)$ is observed to be $\Theta(1/n^2)$ at every checked
  value ($1/20,1/30,1/42,1/28$ for $n=3,4,5,6$, all comfortably above
  $1/(2(2^{n+1}-1))$, which is exponentially small), **any** future proof
  that $\delta(n)=\Omega(1/n^2)$ (even non-closed-form, e.g. an inequality
  $\delta(n)\ge \tfrac{1}{(n+1)(n+2)}\cdot\text{const}$ or similar) suffices
  to close this gap for all $n$ at once — the exponential vs. polynomial
  gap between $c(n)-\tfrac12$ and any plausible $\delta(n)$ is enormous
  already at $n=6$ ($1/254$ vs. $1/28$), so a *crude, non-tight* lower bound
  on $\delta(n)$ is all that is actually needed, not the exact minimizer.

### 7. Round 7: dimensionless reformulation, $n=7,8,9$ certification, and a full proof for every piece except $p_1$

#### 7.1 Sanity gate: exact certification at $n=7,8,9$

Using the certified Single-Piece-Split Vertex Lemma exactly as in rounds
5–6 (full exact-rational enumeration over all block partitions and pin
assignments, capped at $m\le5$ for tractability, **cross-checked** by an
independent numerical multistart search — 15 Nelder–Mead restarts per
$(idx,m)$ pair with a softmax parametrization, sweeping every $m$ from $2$
to $n+1$ for every $idx$, i.e. not capped — with exact agreement in every
case, confirming the $m\le5$ cap loses nothing at these $n$):

$$\mathrm{floor}(7)=\frac{19}{36},\qquad \mathrm{floor}(8)=\frac8{15},
\qquad \mathrm{floor}(9)=\frac{29}{55}.$$

Comparison with $c(n)=2^n/(2^{n+1}-1)$: $c(7)=128/255\approx0.50196$,
$c(8)=256/511\approx0.50098$, $c(9)=512/1023\approx0.50049$; all three
floors exceed $c(n)$ ($19/36\approx0.5278$, $8/15\approx0.5333$,
$29/55\approx0.5273$), so **Multi-Piece Necessity extends to $n=7,8,9$**,
now certified at seven values ($n=3,\dots,9$). This round's target
$\mathrm{excess}(n)\ge1/((n+1)(n+2))$ is also directly checked:
$\mathrm{excess}(7)=19/36-1/2=1/36\ge1/72$;
$\mathrm{excess}(8)=8/15-1/2=1/30\ge1/90$;
$\mathrm{excess}(9)=29/55-1/2=3/110\ge1/110$ — all hold, with ratio
$2\times$, $3\times$, $3\times$ the threshold respectively, matching the
explorer's reported weakly-increasing, never-below-$0.5$ ratio pattern.
This clears the sanity gate: it is safe to invest in the general-$n$
inequality.

#### 7.2 Dimensionless reformulation (Theorem A)

**Observation.** Set $d:=1/D_n$ where $D_n=(n+1)(n+2)/2$; note $d=\delta(n)$
where $\delta(n):=2/((n+1)(n+2))$ is the certified target-excess identity's
quantity (`lemmas/target-excess-identity.md`). Then
$$p_i=\frac{n+2-i}{D_n}=(n+2-i)\cdot d,\qquad i=1,\dots,n+1,$$
so **the $n+1$ landmarks of the triangular family are exactly**
$$\{d,\,2d,\,3d,\,\dots,\,(n+1)d\}$$
**— every positive integer multiple of $d$ from $1$ to $n+1$, with no
gaps.** (Check: $\sum_{j=1}^{n+1}jd=d\cdot\frac{(n+1)(n+2)}2=dD_n=1$, and
$p_i$ corresponds to $j=n+2-i$.) This is a genuinely new observation this
round (not stated in rounds 5–6, which worked with the fractional form
directly) and is the key simplification: dividing every quantity in the
problem by $d$ turns the excess inequality into a **purely combinatorial
statement about consecutive integers**, independent of $n$-dependent
fractions.

**Theorem A (reduction).** Set $N:=n+1$. Fix $idx\in\{1,\dots,N\}$ and let
$k:=N+1-idx\in\{1,\dots,N\}$ (so $p_{idx}=kd$; $idx=1\Leftrightarrow k=N$).
Fix any $\le n$-cut split of $p_{idx}$ into $m\ge2$ positive parts (so
$2\le m\le n+1=N$), with fragment values $x_1,\dots,x_m>0$,
$\sum x_i=kd$. Define $y_i:=x_i/d>0$ (so $\sum y_i=k$), and let
$$A(N,k,y_1,\dots,y_m):=\mathrm{AltSum}\Bigl(\bigl(\{1,\dots,N\}\setminus\{k\}\bigr)\cup\{y_1,\dots,y_m\}\Bigr)$$
(the AltSum of the merged multiset of the $N-1$ remaining integer
landmarks and the $m$ real fragment values, in "$d$-units"). Then, using
$\mathrm{OddSum}=(1+\mathrm{AltSum})/2$ applied to the original (unscaled)
merged multiset — whose AltSum equals $d\cdot A(N,k,y_1,\dots,y_m)$ by
linearity, since every value in the original merged multiset is exactly
$d$ times the corresponding value here (all fragment values individually
scale by $d$, and the sort order is preserved since $d>0$) — the resulting
$\mathrm{OddSum}$ equals $\tfrac12+\tfrac{d}2 A(N,k,y_1,\dots,y_m)$. Hence
$$\text{this split's excess over }\tfrac12=\frac{d}2\,A(N,k,y_1,\dots,y_m)=\frac{\delta(n)}2\,A(N,k,y_1,\dots,y_m),$$
and since the target threshold is $1/((n+1)(n+2))=\delta(n)/2$ exactly,
**the target inequality for this split is equivalent to**
$$A(N,k,y_1,\dots,y_m)\ \ge\ 1. \tag{$\star$}$$
Taking the minimum over $idx$ and splits, $\mathrm{excess}(n)\ge
1/((n+1)(n+2))$ for the whole triangular family iff $(\star)$ holds for
**every** $k\in\{1,\dots,N\}$ and every valid $(y_1,\dots,y_m)$. $\blacksquare$

This reformulation was checked against the exact $n=3,\dots,9$ data:
e.g. at $n=3$ ($N=4$), the winning split ($idx=1$, fragments
$(3/10,1/20,1/20)$ in original units, $d=1/10$) gives $y=(3,0.5,0.5)$,
$k=4$; direct computation gives $A(4,4,3,0.5,0.5)=\mathrm{AltSum}
(\{3,2,1,3,0.5,0.5\})=3-3+2-1+0.5-0.5=1$, matching
$\mathrm{excess}(3)=1/20=\delta(3)/2\cdot1$ exactly ($\delta(3)=1/10$).

#### 7.3 Theorem B: the target holds for every piece except $p_1$ (fully proved, general $n$)

**Theorem B.** For every $N\ge2$, every $k\in\{1,\dots,N-1\}$ (i.e.
$idx\ge2$: any piece **other than** $p_1$), and every choice of $m\ge2$
positive reals $y_1,\dots,y_m$ with $\sum y_i=k$,
$$A(N,k,y_1,\dots,y_m)\ge1.$$

**Two standard facts used (both elementary, stated for completeness).**
For any finite multiset $T$ of nonnegative reals, sorted descending
$t_1\ge t_2\ge\cdots\ge t_r\ge0$, define $\mathrm{AltSum}(T)=\sum_{i=1}^r
(-1)^{i+1}t_i$ (and $\mathrm{AltSum}(\emptyset)=0$). Then:
- **(Peel identity.)** If $T\ne\emptyset$, $\mathrm{AltSum}(T)=t_1-
  \mathrm{AltSum}(T\setminus\{t_1\})$ (removing the largest element and
  negating: every remaining element's rank drops by exactly $1$, flipping
  every sign). This is the standard "peel the max" identity used
  elsewhere in this project (cf. `greedy-reduction-geometric`'s Theorem
  7a, which peels the global max and applies $\mathrm{EvenSum}\ge0$ — the
  same underlying mechanism).
- **(Upper bound.)** $\mathrm{AltSum}(T)\le\max(T)=t_1$ (immediate:
  $\mathrm{AltSum}(T)=t_1-(t_2-t_3)-(t_4-t_5)-\cdots$, and every bracketed
  difference is $\ge0$ since $T$ is sorted descending).

**Proof of Theorem B.** Let $S:=(\{1,\dots,N\}\setminus\{k\})\cup
\{y_1,\dots,y_m\}$, so $A(N,k,y)=\mathrm{AltSum}(S)$. Since $k\le N-1$,
the integer $N$ belongs to $\{1,\dots,N\}\setminus\{k\}\subseteq S$.
Every fragment satisfies $y_i<k$ (strict: since $m\ge2$ and all $y_j>0$,
the other $m-1\ge1$ fragments are positive, so $y_i=k-\sum_{j\ne i}y_j<k$).
Hence $\max(\{y_1,\dots,y_m\})<k\le N-1<N$, so $N$ is the **unique**
maximum of $S$: $\max(S)=N$.

By the Peel identity, $\mathrm{AltSum}(S)=N-\mathrm{AltSum}(S\setminus\{N\})$.
Now $S\setminus\{N\}=(\{1,\dots,N-1\}\setminus\{k\})\cup\{y_1,\dots,y_m\}$
(valid since $k\le N-1$, so removing $k$ from $\{1,\dots,N-1\}$ is
well-defined), and every element of $S\setminus\{N\}$ is $\le N-1$: the
remaining landmarks are all $\le N-1$ by construction, and every fragment
satisfies $y_i<k\le N-1$. So $\max(S\setminus\{N\})\le N-1$, and by the
Upper bound fact, $\mathrm{AltSum}(S\setminus\{N\})\le\max(S\setminus\{N\})
\le N-1$.

Combining: $\mathrm{AltSum}(S)=N-\mathrm{AltSum}(S\setminus\{N\})\ge
N-(N-1)=1$. $\blacksquare$

**Consequence.** By Theorem A, this proves: **for every $n\ge1$, every
piece $p_{idx}$ with $idx\ge2$, and every $\le n$-cut split of that piece
(leaving all other pieces of the triangular family untouched), the
resulting excess over $c(n)$'s midpoint $\tfrac12$ is at least
$1/((n+1)(n+2))$ — unconditionally, not just for the specific instances
checked numerically.** This holds for the triangular family at every $n$
simultaneously, by a single uniform argument with no case split on $n$.

**Independent stress test.** Generated 20,000 random exact-rational
trials ($N$ uniform in $\{4,\dots,20\}$, $k$ uniform in $\{1,\dots,N-1\}$,
$m$ uniform in $\{2,\dots,6\}$, $(y_1,\dots,y_m)$ a random positive
rational composition of $k$ via random cut points with denominator
$1000$), computing $A(N,k,y)$ by direct exact `Fraction` arithmetic and
checking $\ge1$: **zero violations**, consistent with the proof.

#### 7.4 The one remaining case: $idx=1$ ($k=N$, splitting $p_1$ itself)

Theorem B's proof breaks down exactly at $k=N$: then $\{1,\dots,N\}
\setminus\{k\}=\{1,\dots,N-1\}$ does **not** contain $N$, and a fragment
$y_i$ *can* exceed $N-1$ (since $\sum y_i=N>N-1$), so $\max(S)$ may come
from $Y$ rather than from the landmark set, and the clean one-step peel
argument does not directly close the case. This is exactly the case that
was the actual minimizer in the certified instances at $n=3,5,7,9$ (and
tied for the minimizer at $n=4,6,8$), so it is the genuinely hard case —
isolated cleanly for the first time this round, rather than being mixed
in with all $idx$ as before.

**Numeric/exact characterization (evidenced, not proved).** Exact vertex
search (capped $m\le5$ for $N\ge11$, uncapped for $N\le10$, cross-checked
against numerical multistart sweeping every $m$ up to $N$ for
$N=8,9,10$ with exact agreement) gives the minimal value of
$A(N,N,y_1,\dots,y_m)$ over all valid splits, for $N=4,\dots,17$:
$$1,\ 1,\ 1,\ 2,\ 2,\ 3,\ 3,\ 4,\ 4,\ 5,\ 5,\ 6,\ 6,\ 7\qquad(N=4,\dots,17).$$
This matches $\lfloor(N-3)/2\rfloor$ exactly for every $N\ge5$ (with
$N=4$ a lone exception: $A=1>\lfloor1/2\rfloor=0$, directly verified
rather than fitting the formula). Since $\lfloor(N-3)/2\rfloor\ge1$ for
all $N\ge5$, and $N=4$ gives $A=1\ge1$ directly, **every checked value
satisfies $(\star)$, with a margin that grows roughly linearly in $N$**
— not a knife-edge inequality once $N$ is even moderately large. The
winning $m$ in every checked instance is $m=2$ (odd $N$) or $m=3$ (even
$N$); no instance with $m\ge4$ ever beat the best of $m=2,3$ in the
uncapped numerical sweep at $N=8,9,10$, suggesting (but not proving) that
the problem reduces to two closed-form finite cases.

**What would finish this case.** Either (a) prove the closed form
$\lfloor(N-3)/2\rfloor$ (or any valid lower bound $\ge1$) directly, e.g.
by adapting the Theorem B peeling technique to handle the case
$\max(S)\in Y$ separately from $\max(S)\in L$ (attempted this round: the
natural extension peels $N-1$ instead of $N$ when $\max(Y)<N-1$, but the
residual set $\{1,\dots,N-2\}\cup Y$ then has $\sum Y=N$ while only
$N-2$ landmarks remain — a mismatch of exactly $1$ relative to the clean
"$k=N'$" pattern that Theorem A's structure needs, so the recursion does
not close cleanly in one more step; this exact obstruction — "the peel
recursion drifts out of the clean family by the AP-boundary mismatch" —
is the honest, precisely-located reason this case resists the same short
argument as Theorem B); or (b) prove that $m\ge4$ is always dominated by
$m\in\{2,3\}$ for this specific structure (landmarks a full consecutive
run), which would reduce the problem to two explicit finite closed-form
computations (already set up as tractable integer case-splits on the pin
value $j$, computed for $m=2$ in closed form this round: minimal
$A(N,N,\cdot)$ over $m=2$ splits alone is $N/2$ for even $N$ and
$(N-3)/2$ for odd $N\ge5$ — matching the overall minimum exactly for odd
$N$, but not for even $N$ where $m=3$ strictly improves on it, e.g.
$N=6$: $m=2$ gives $3$, $m=3$ gives $1$). Neither (a) nor (b) was
completed this round.

**Net effect on the overall gap.** Before this round, the entire
general-$n$ Multi-Piece Necessity theorem (all $idx$) was open. After
this round: it is **proved for $n$ of the $n+1$ possible values of
$idx$** (i.e. $N-1$ of $N=n+1$ values, every piece except $p_1$), for
every $n$ simultaneously, by Theorem B — leaving exactly **one**
precisely-named case ($idx=1$) open, backed by strong evidence (14
consecutive exact/numeric data points matching a clean closed form with
growing margin) but not a proof. This is a substantial narrowing, not a
full closure.

*(Reviewer correction, round 7: the previous wording "$n-1$ of $n$" was
an off-by-one labeling slip — the triangular family at parameter $n$ has
$N=n+1$ pieces, indexed $idx=1,\dots,n+1$; Theorem B covers
$idx=2,\dots,n+1$, i.e. $n$ of the $n+1$ values, leaving the single case
$idx=1$ open. This does not affect Theorem B's proof or its scope, only
this summary sentence's arithmetic.)*

## Promotable lemmas

**New, round 17 (proposed for certification):**

**Even-Multiplicity Equality Criterion.** For any finite multiset $M$ of
positive reals with $\mathrm{sum}(M)=1$, $\mathrm{OddSum}(M)=\tfrac12$
(the universal floor) if and only if $|M|$ is even and every distinct
value of $M$ has even multiplicity. Proved in full in the "Round 17
update" section above (odd-size case: the unpaired trailing element
forces $\mathrm{AltSum}>0$ strictly; even-size case: a block-boundary
parity argument shows Property (P) — every consecutive descending pair
equal — holds iff every value-class has even size). Elementary,
fully general, no dependence on $e_0$ or any specific partition.

**Generalized Mass-Constraint Theorem.** For any legal adversary
partition with pairwise-distinct pieces, any active set $S$ (split
pieces) and untouched set $U$: if some legal response attains
$\mathrm{OddSum}(M)=\tfrac12$ exactly, then $\sum_{i\in U}p_i\le\tfrac12
\le\sum_{j\in S}p_j$. Proved in full in the "Round 17 update" section
above, via the Even-Multiplicity Equality Criterion (each untouched
value needs a matching fragment) plus a mass-summation argument (mirrors
but strictly generalizes the certified round-11 Mass-Constraint Theorem,
`lemmas/rank-pinning-lemma-and-mass-constraint-theorem.md`, from one
specific tie-construction family to every legal response whatsoever).
Includes an exact-Fraction-verified closed form for the resulting
necessary condition at $e_0$ specifically
($\sum_{i=1}^sp_i(e_0)=\tfrac sN+\delta\cdot\tfrac{s(N-s)}2$), and an
explicit corollary table for $n=3,\dots,20$.

**Round 16: none.** This round was a light cross-check dispatch (see
"Round 16 update" above); no new theorem or lemma was proved. The
soft numeric lead recorded this round is explicitly not proposed for
certification (non-conclusive, local-optimizer only).

**New, round 15 (proposed for certification — supersedes/strengthens the
round-14 lemma):**

**Twin-Anchor Floor Theorem.** For every $n\ge3$, at the region vertex
$e_0$ (coordinates $p_i(e_0)=a+(N-i)\delta$, $N=n+1$,
$\delta=\gamma(n)=1/(2^N-1)$, $a=p_N(e_0)>0$, certified
`lemmas/finite-cell-vertex-reduction-and-region-classification.md`), the
explicit construction of "Round 15 update: the Twin-Anchor Construction"
above (piece $1$ split into $(p_{N-1},(N-2)\delta)$; piece $2$ split into
$(p_N,(N-2)\delta)$; every piece $j=3,\dots,N-2$ bisected into equal
halves; pieces $N-1,N$ untouched) is a legal $(n-1)$-cut XY response
achieving $\mathrm{OddSum}=\tfrac12$ **exactly** — the universal absolute
floor (via the certified OddSum Floor Lemma). Proved in full: a one-line
algebraic identity ($p_1-p_{N-1}=p_2-p_N=(N-2)\delta$ identically, no
induction needed), positivity that is *unconditional* (only needs
$a>0,\delta>0$, true for every $n$ since $e_0$ is an interior simplex
point — no side inequality between $a$ and $\delta$ required, unlike the
predecessor construction), and the Even-Block-Neutrality mechanism
applied to $n-1$ disjoint equal-valued pairs partitioning the entire
response. Independently re-verified in exact `Fraction` arithmetic for
$n=3,\dots,40$ (38 instances, zero deviation), plus a fully worked hand
example at $n=3$. This strictly widens the range of the round-14
Chain-Correction Floor Theorem ($n\ge6\to n\ge3$) with a simpler, more
robust proof; $n=2$ is checked and confirmed genuinely out of scope
(a real parity/budget obstruction, not an oversight). Consequence:
$V(e_0)=\tfrac12$ exactly for every $n\ge3$ (not just $n\ge6$).

**New, round 14 (proposed for certification):**

**Chain-Correction Floor Theorem.** For every $n\ge6$, at the region
vertex $e_0$ (coordinates as certified in
`lemmas/finite-cell-vertex-reduction-and-region-classification.md`),
the explicit construction of "Round 14 update: the Chain-Correction
Hybrid Construction" above (active set $\{1,\dots,n-1\}$, i.e. all
pieces but the smallest $2$; pieces $1,2$ each split with one fragment
tied to a whole untouched piece, pieces $3,5$ each split with one
fragment tied to the other's "chain" leftover value, piece $4$ and
every piece $6,\dots,n-1$ self-tied into equal halves) is a legal
$(n-1)$-cut XY response achieving $\mathrm{OddSum}=\tfrac12$ **exactly**
— the universal absolute floor (via the certified OddSum Floor Lemma).
Proved in full: an explicit algebraic identity (the Key Algebraic
Identity: two independently-computed "chain" values collapse to the
same constant $a-2\delta$ for every $N$) plus a Positivity Lemma
($a>2\delta$ for all $n\ge6$, proved by induction) plus the
Even-Block-Neutrality mechanism (general $t=1$ case, applied to $n-1$
disjoint tied pairs partitioning the entire response). Independently
re-verified in exact `Fraction` arithmetic for $n=6,7,8,9,10,12,15,20$
(8 instances, zero deviation). Consequence: $V(e_0)=\tfrac12$ exactly
for every $n\ge6$ (strictly below $c(n)$), a likely correction to the
"$V(e_0)=c(n)$ exactly" language recorded elsewhere (flagged for
reconciliation, not itself acted on here).

**New, round 11 (proposed for certification):**

**Top-Duplication Witness Theorem.** For every integer $n\ge0$, LB's
geometric partition $p_i=2^{n+1-i}/(2^{n+1}-1)$ admits a legal XY response
using exactly $n$ cuts (for $n\ge1$; $0$ cuts for $n=0$) — split only the
top landmark $2^n$ (piece $p_1$) into the fragments
$2^{n-1},2^{n-2},\ldots,2^1,1,1$, leaving every other landmark unsplit —
achieving $\mathrm{OddSum}=c(n)=2^n/(2^{n+1}-1)$ **exactly**. Proved in
full (Section 11.2 above, "Round 11" section) via the Even-Block-
Neutrality Lemma applied to $n-1$ isolated tied pairs plus a direct
rank-parity computation of the bottom three-element block of tied
value $1$, then the scaling identity; independently re-verified by exact
`Fraction` arithmetic for $n=0,\ldots,14$ (15/15 exact fraction
equalities, not float approximations). Consequence:
$V(p_{\mathrm{LB}})\le c(n)$ for every $n\ge0$ — a genuine new,
single-point result for the upper-bound direction at the (conjectured)
extremal partition, complementary to (not overlapping) `T(2)`/
Dominant-Chain's work on the reverse inequality.

**New, round 10 (proposed for certification):**

**Multi-Piece Sufficiency Theorem for the triangular family.** For every
$n\ge3$ ($N=n+1$), the explicit construction of "Round 10: the Multi-Piece
Sufficiency Theorem" above (split landmarks $N,N-1$ and $2,\dots,N-2$ each
into $2$ fragments as specified, with $\varepsilon=\varepsilon_N=
\mathrm{Thr}(N)/4$; landmark $1$ unsplit) is a legal $n$-cut XY response
achieving $\mathrm{OddSum}=\tfrac12+\tfrac12(c(n)-\tfrac12)<c(n)$. Proved
in full (exact ordering argument + Even-Block-Neutrality Lemma + exact
scaling identity), independently re-verified in exact `Fraction`
arithmetic for $N=4,\dots,40$. Together with the (already-certified)
Multi-Piece Necessity Theorem, this completely settles both directions for
the triangular family: no single piece suffices, but this specific
$n$-piece response always does. General-purpose reusable sub-lemma
bundled in: the **Even-Block-Neutrality Lemma** (an isolated block of an
even number $2t$ of exactly-tied values contributes $0$ to
$\mathrm{AltSum}$ and does not disturb any other element's rank parity) —
a clean general statement of the mechanism already used ad hoc inside the
certified Bottom-Block-Doubling proof, now stated and proved standalone
for reuse by any future AltSum-based construction.

**New, round 9 (proposed for certification):**

**General Consecutive-Block AltSum Formula.** For integers $c\ge0,m\ge0$,
$\mathrm{Blk}(c,m):=\mathrm{AltSum}(\{c+1,\dots,c+m\})$ equals $0$ if
$m=0$; $m/2$ if $m>0$ even; $(m-1)/2+(c+1)$ if $m$ odd. Proved in full
(Round 9 section above) by direct pairing from the top of the sorted
block; corrects a subtly-wrong special case ($c=0$-only) folk version
implicitly used earlier in this project. General purpose: needed whenever
a contiguous run of consecutive integers *not* starting at $1$ appears as
a sub-block of a larger AltSum computation (as it does here after
"doubling" a bottom prefix).

**Bottom-Block-Doubling exact value (Round 9 Theorem).** For the
triangular family, splitting $p_1,p_2$ to double landmarks $1,\dots,k$
(via one extra fragment matching each) plus an even filler pair absorbing
the remaining budget gives $\mathrm{AltSum}(L\cup W)=\mathrm{Blk}(k,N-2-k)$
exactly — proved in full (Round 9 section above), verified exactly against
direct computation for $N=4,\dots,59$ (56/56 exact matches). Reusable
as a general technique ("double a budget-affordable prefix of a
consecutive-integer landmark set, absorb the rest as an even filler") for
any future AP/consecutive-integer-landmark construction problem.

**From prior rounds (round 8):**

**Small-Tail Bound (STB).** For $L>0$ and a finite multiset $Y$ of positive
reals with $\max(Y)\le L$, $\mathrm{AltSum}(\{L\}\cup Y)\ge L-\mathrm{sum}(Y)$.
Proved in full (Round 8 section above): two-line proof from the Peel
identity + Upper-bound fact + the trivial $\max(Y)\le\mathrm{sum}(Y)$ for
positive $Y$. General purpose, reusable anywhere a "landmark plus a small
budget of extra positive fragments" bound is needed.

**Consecutive-run-plus-small-tail two-sided bounds (Lemmas $f$ and $g$,
Round 8 section above).** For $\{1,\ldots,r\}\cup Y$ where $Y$'s total sum
is a fixed $t\in(0,1]$ (Lemma $f$) or fixed $u\in(1,2)$ (Lemma $g$), tight
two-sided bounds on $\mathrm{AltSum}$ as a function of $r$'s parity, proved
by induction via the Peel identity alone (no case-by-case tail-block sign
bookkeeping needed). Reusable for any future "split the top landmark of a
consecutive-integer family" argument with a similarly small perturbation
budget.

**Multi-Piece Necessity Theorem, full generality (Round 8's main result).**
For the triangular family $p_i=(n+2-i)/D_n$ ($n\ge3$), splitting any single
piece $p_{idx}$ ($idx\in\{1,\ldots,n+1\}$, any $idx$ including the top
piece) into $\le n$ positive fragments (all other pieces held fixed)
always leaves $\mathrm{OddSum}\ge c(n)+1/((n+1)(n+2))>c(n)$,
unconditionally, for every $n\ge3$. Ready for certification: combines with
Theorem B (already certified, `lemmas/non-top-piece-theorem-b.md`) to give
the complete, general-$n$, all-$idx$ Multi-Piece Necessity theorem.

**From prior rounds:**

**Single-Piece-Split Vertex Lemma** (Section 2 above, fully proved,
self-contained, general-purpose): for a fixed LB partition and a fixed
piece $p_{idx}$ split alone (all other pieces untouched, constants), the
minimum achievable $\mathrm{OddSum}$ over all $\le n$-cut splits of
$p_{idx}$ equals the minimum over a finite, explicitly-constructed set of
"vertex" candidates (each coordinate either $0$, tied to another fragment,
or tied to a fixed other piece's value), and this minimum is always
attained by a genuine positive-part split. Reusable by any future
approach needing to compute or bound the best *single-piece* XY response
exactly (e.g. as a subroutine inside a larger multi-piece construction, or
to rule out single-piece sufficiency for a family of instances as done
here).

**Exponential-vs-polynomial reduction fact** (new, round 6, fully proved,
Section 6 above): for any candidate single-piece floor value $F(n)$ for the
triangular family $p_i=(n+2-i)/D_n$, proving $F(n)>c(n)=2^n/(2^{n+1}-1)$ for
all $n$ reduces, via the exact identity $c(n)-\tfrac12=\dfrac1{2(2^{n+1}-1)}$
(elementary algebra: $c(n)=\tfrac{2^n}{2^{n+1}-1}$, so
$2c(n)-1=\tfrac{2^{n+1}-(2^{n+1}-1)}{2^{n+1}-1}=\tfrac1{2^{n+1}-1}$), to
proving $F(n)-\tfrac12>\dfrac1{2(2^{n+1}-1)}$ — a single exponentially small
threshold. Since the true single-piece floor's excess over $1/2$ has been
found (this file) to be polynomially small in $n$ (order $1/n^2$) at every
checked instance, this reduction shows any *crude, non-closed-form*
polynomial lower bound on the excess suffices to finish the theorem for all
$n$ at once — the exact minimizer is not actually needed, only a bound of
the right polynomial order. Reusable by any future approach attacking the
general-$n$ Multi-Piece Necessity theorem for this or a similar AP-structured
family.

**Dimensionless AP-normalization + Non-Top-Piece Theorem** (new, round 7,
Section 7.2–7.3 above, fully proved): for any AP-structured family whose
landmarks, after dividing by the common difference, form a run of
consecutive integers $1,\dots,N$ (as the triangular family's do), removing
any integer $k<N$ (i.e. any landmark other than the top one) and replacing
it with $m\ge2$ positive reals summing to $k$ always increases
$\mathrm{AltSum}$ by at least $1$ (in the normalized units) — proved by a
two-line "peel the global max, bound the rest by its own max" argument,
general for every $N$ and every such $k$ simultaneously (Theorem B). This
is a general-purpose tool: it reduces any future Multi-Piece-Necessity-style
theorem for a consecutive-integer-after-normalization family to checking
only the single case "the top landmark is the one split" — exactly the
kind of uniform, case-split-free closure this project's other approaches
have found hardest to achieve. Reusable directly by any future round
attacking this or a structurally similar family.

## Round 12 target: one focused fragment-vs-fragment tying construction

Round 12's `fragment-tying` explorer report
(`/tmp/round-12/math-explorer-fragment-tying.md`) found no direct
transfer of this file's own machinery (Multi-Piece Sufficiency,
Top-Duplication Witness — both explicit-construction results at a
*fixed* LB partition) into the TOP-ONLY$(m-1)$/Branch-I.A-window gap
(that gap is lower-bound direction; this file's tools are upper-bound
direction, and the objects are dual, not directly bridgeable). Stay on
this file's own lane: the general upper-bound direction (no LB partition
beats $c(n)$), specifically `global-lp-vertex-sufficiency`'s
**Opening 1 (fragment-vs-fragment tying)**, now demoted to secondary
there in favor of Region-Boundary Monotonicity, but a good fit for this
file's strength in *explicit* constructions.

**Concrete task (the "one more focused attempt" the fragment-tying
explorer recommends before treating fragment-vs-fragment tying as also
insufficient):** construct, and prove exactly (not search
numerically), a fragment-vs-fragment tying response at the hard vertex
$e_0$ (already exactly characterized in
`global-lp-vertex-sufficiency.md` Section 4.1/4.3, $V(e_0)=c(n)$) that
ties fragments from **different split pieces to each other** rather than
to a whole untouched piece — e.g. generalize the certified
Singleton-Interleaving Lemma (`lemmas/singleton-interleaving-and-k-anchor-
merge.md`) to chain-tie $2,3,\dots$ fragments from different split pieces.
The round-12 numeric stress test (unconstrained Nelder–Mead at $e_0$, top-
$s$-pieces split) found a **soft negative signal**: the minimal clearing
$s$ still seems to grow with $n$ ($3$ at $n=6$, $\ge5$ at $n=8$), similar
to the already-refuted tie-to-whole-piece family — so this is a
worthwhile but not-favored-odds attempt; if it also fails to give a
bounded-$s_0$ construction, record that as a further (still not fully
general) negative data point for the upper-bound direction, consistent
with the growing suspicion that no bounded-family construction suffices
and the eventual argument needs `global-lp-vertex-sufficiency`'s
reduction-side route instead.

## Round 12: the Perfect-Tie-Family Exact Characterization at $e_0$

**Goal (per outliner/round-12 target).** Construct, and prove exactly (not
search numerically), a fragment-vs-fragment tying response at $e_0$ —
ties fragments from *different* split pieces to each other, evading the
certified Mass-Constraint Theorem's obstruction (which is specific to
tying a fragment to a *whole untouched piece*). Determine whether a
bounded family closes this, or whether the negative signal can be turned
into a genuine proved obstruction.

### 12.0 Setup: $e_0$'s exact coordinates (imported, already certified)

From `approaches/global-lp-vertex-sufficiency.md` Section 4.1/4.3
(certified `lemmas/finite-cell-vertex-reduction-and-region-classification.md`):
for $n\ge2$, $e_0=(p_1,\dots,p_{n+1})$ is the arithmetic progression
$$p_i=p_{n+1}+(n+1-i)\gamma(n),\qquad p_{n+1}=\frac1{n+1}-\frac{n\gamma(n)}2,
\qquad \gamma(n):=\frac1{2^{n+1}-1},$$
and $c(n)=\tfrac12+\tfrac{\gamma(n)}2$ exactly (the same certified
identity used throughout this file and in the sibling approach). Note
$e_0$ is a *near-uniform* partition: every $p_i=\Theta(1/(n+1))$, and the
entire spread $p_1-p_{n+1}=n\gamma(n)$ is exponentially small — the target
excess $c(n)-\tfrac12=\gamma(n)/2$ is comparable in *scale* to a single
AP gap $\gamma(n)$ itself, not to the pieces' own sizes $\Theta(1/n)$.
This scale mismatch (razor-thin exponential threshold vs. polynomial
piece sizes) is the source of everything below.

### 12.1 The construction family: "perfect-tie" fragment-vs-fragment/self-tie

**Definition (Perfect-Tie construction).** Choose a set $S\subseteq
\{1,\dots,n+1\}$ of "active" (split) pieces, $|S|=s\le n$ (so the total
cut budget is respected: splitting each active piece uses $\ge1$ cut,
$s\le n$ is necessary). Split every $p_i$, $i\in S$, into any number of
positive fragments, in any pattern, subject to: **every fragment of every
active piece is placed into some tied block** — a group of $\ge2$
fragments (possibly from the *same* active piece, "self-tie," or from
*two or more different* active pieces, genuine "fragment-vs-fragment
tie") all equal in value, with each block's multiplicity **even**, and no
fragment left over (**zero residual**, hence "perfect"). Every piece
$j\notin S$ is left completely untouched. (This is strictly a
sub-family of "fragment-vs-fragment tying" — it excludes the round-11
family entirely, since no untouched piece's value is ever used as a tie
target — and it is the *most resource-efficient* member of that family,
since spending fragments on residual, untied leftovers can only ever cost
extra without the compensating $\tfrac12$-dilution benefit a tied block
gives; see 12.4 for the honest scope note on why this does not cover the
*whole* fragment-vs-fragment family.)

**Lemma 12.1 (Exact value, via the certified Singleton-Interleaving
Lemma).** For any Perfect-Tie construction with active set $S$,
$$\mathrm{OddSum}(M)=\frac12+\frac12\,\mathrm{AltSum}(U),\qquad
U:=\{p_i(e_0):i\notin S\}.$$

*Proof.* Apply Theorem 9 (`lemmas/singleton-interleaving-and-k-anchor-
merge.md`) with $B:=$ the union of all tied blocks (by construction, a
disjoint union of even-length equal-value groups, generically distinct
across groups and from $U$'s values — achievable by generic choice of
the actual tie values, e.g. bisecting a piece at its exact midpoint, or
choosing any fragment-vs-fragment split value not coincidentally equal to
another piece's value; $e_0$'s specific coordinates are all distinct real
numbers so a generic choice always avoids the finitely many coincidence
conditions) and $L:=U$ (the untouched pieces, with $B$'s total mass
exactly $\sum_{i\in S}p_i(e_0)=:\Pi$, since the construction has zero
residual). Theorem 9 gives $\mathrm{OddSum}(M)=\tfrac12\Pi+
\mathrm{OddSum}(U)$. Since $\mathrm{OddSum}(U)=\tfrac12\bigl(\mathrm{sum}(U)
+\mathrm{AltSum}(U)\bigr)=\tfrac12\bigl((1-\Pi)+\mathrm{AltSum}(U)\bigr)$,
substituting gives $\mathrm{OddSum}(M)=\tfrac12\Pi+\tfrac12(1-\Pi)+
\tfrac12\mathrm{AltSum}(U)=\tfrac12+\tfrac12\mathrm{AltSum}(U)$. $\blacksquare$

**This is the key structural fact**: the achieved value depends on the
construction *only* through which pieces are left untouched — not
through how the active pieces' fragments are internally tied (self-tie,
pairwise fragment-vs-fragment, or any larger chain), nor through how many
cuts are used beyond the minimum. So bounding this family reduces
entirely to a question about $\mathrm{AltSum}(U)$ for $U$ an
arbitrary-size subset of $e_0$'s $n+1$ AP values.

### 12.2 New tool: the Integer-Alternating-Sum Lower Bound Lemma

**Lemma 12.2.** Let $v_1>v_2>\cdots>v_m\ge0$ be $m$ distinct nonnegative
integers. Then $\mathrm{AltSum}(\{v_1,\dots,v_m\}):=v_1-v_2+v_3-\cdots
\pm v_m\ \ge\ \lfloor m/2\rfloor$.

*Proof.* Group into consecutive pairs from the top:
$(v_1,v_2),(v_3,v_4),\dots$, giving $\lfloor m/2\rfloor$ pairs (plus one
leftover term $v_m$ if $m$ is odd). Since the $v_i$ are distinct integers
listed in strictly decreasing order, $v_{2j-1}-v_{2j}\ge1$ for every pair
$j$ (integers differing by at least $1$). Summing the $\lfloor m/2
\rfloor$ pair-differences (each $\ge1$) gives $\mathrm{AltSum}\ge
\lfloor m/2\rfloor$; if $m$ is odd, the leftover term $v_m\ge0$ only adds
a nonnegative amount, so the bound is unaffected in direction (still
$\ge\lfloor m/2\rfloor$). $\blacksquare$

This is a fully general, elementary, reusable combinatorial fact
(independent of the problem's game structure) — equality holds exactly
when consecutive kept pairs are adjacent integers and (if $m$ odd) the
smallest kept value is $0$.

### 12.3 Applying Lemma 12.2 to $U$ at $e_0$: exact characterization

Write $p_i(e_0)=p_{n+1}(e_0)+j_i\gamma(n)$ where $j_i:=n+1-i\in\{0,\dots,
n\}$ is the piece's AP-index (largest piece $p_1$ has $j=n$). For
$U=\{p_i(e_0):i\notin S\}$, let $J:=\{j_i:i\notin S\}\subseteq\{0,\dots,
n\}$, $|J|=m:=n+1-s$. Since $\mathrm{AltSum}$ is linear under the affine
map $x\mapsto p_{n+1}(e_0)+\gamma(n)x$ applied to a set of size $m$ (the
constant term $p_{n+1}(e_0)$ contributes with total sign $\sum_i(-1)^{i+1}$,
which is $0$ if $m$ is even and $\pm1$, specifically $+1$ under descending
order with the smallest term unpaired, if $m$ is odd):
$$\mathrm{AltSum}(U)=\gamma(n)\,\mathrm{AltSum}(J)\quad(m\text{ even}),
\qquad
\mathrm{AltSum}(U)=p_{n+1}(e_0)+\gamma(n)\,\mathrm{AltSum}(J)\quad(m\text{ odd}).$$

**Case $m$ even.** By Lemma 12.2, $\mathrm{AltSum}(J)\ge\lfloor m/2\rfloor
=m/2$, with equality attained (e.g. $J=\{0,1,\dots,m-1\}$, adjacent
integers). So $\min\mathrm{AltSum}(U)=\gamma(n)\,m/2$ exactly, over all
choices of active set $S$ of the given size $s=n+1-m$. By Lemma 12.1, the
best (smallest) achievable value in this sub-case is
$$\mathrm{OddSum}(M)=\frac12+\frac{\gamma(n)\,m}4.$$

**Case $m$ odd.** By Lemma 12.2, $\mathrm{AltSum}(J)\ge(m-1)/2$, with
equality attained (e.g. $J=\{0,1,\dots,m-1\}$ again). So
$\min\mathrm{AltSum}(U)=p_{n+1}(e_0)+\gamma(n)(m-1)/2$ exactly, and the
best achievable value is
$$\mathrm{OddSum}(M)=\frac12+\frac{p_{n+1}(e_0)}2+\frac{\gamma(n)(m-1)}4.$$

**Independent verification (exact `Fraction` arithmetic, $n=2,\dots,14$,
every $s=0,\dots,n$, i.e. every $m=1,\dots,n+1$; brute-force over *all*
$\binom{n+1}{s}$ choices of active set, literal bisection construction
sorted and summed directly — not just the closed-form prediction):
**exact match** between (a) the closed-form formulas above, (b) the
brute-force minimum over all active-set choices for the literal bisected
construction, in every instance where $m$ has the claimed parity, for
**every** $s=0,\dots,n$ regardless of parity (both branches of the
formula checked, not just the favorable one). ($117$ total $(n,s)$ pairs
checked across $n=2,\dots,14$ — i.e. every $s$ from $0$ to $n$ for each
such $n$: $100\%$ exact agreement, and the Theorem's claim in Section
12.4 — that $s=n-1$ is the unique value with achieved value $\le c(n)$,
achieving it with exact equality, and every other legal $s$ strictly
exceeds $c(n)$ — was separately verified to hold with zero exceptions
across all $117$ instances.)

### 12.4 The Theorem: only $s=n-1$ works, and only to a tie

**Theorem (Perfect-Tie-Family Exact Characterization at $e_0$).** For
every $n\ge2$: within the Perfect-Tie construction family (Section 12.1),
$$\min_{|S|=s}\ \mathrm{OddSum}(M)\ \begin{cases}
=\ \dfrac12+\dfrac{\gamma(n)(n+1-s)}4, & n+1-s\text{ even},\\[8pt]
=\ \dfrac12+\dfrac{p_{n+1}(e_0)}2+\dfrac{\gamma(n)(n-s)}4, & n+1-s\text{ odd}.
\end{cases}$$
Consequently:
1. **Every odd-parity $s$ fails**, for every $n\ge2$: the achieved value
   exceeds $c(n)$, because $p_{n+1}(e_0)/2>\gamma(n)/2=c(n)-\tfrac12$ for
   every $n\ge2$. *Proof of this sub-claim.* By the already-certified
   bound $n(n+1)\gamma(n)<1$ (`global-lp-vertex-sufficiency.md`, Section
   4.1, "Claim A" — established there for the unrelated purpose of
   showing $K(n)>0$, reused here), $\tfrac{n\gamma(n)}2<\tfrac1{2(n+1)}$,
   so $p_{n+1}(e_0)=\tfrac1{n+1}-\tfrac{n\gamma(n)}2>\tfrac1{n+1}-
   \tfrac1{2(n+1)}=\tfrac1{2(n+1)}$. It remains to show
   $\tfrac1{2(n+1)}>\gamma(n)=\tfrac1{2^{n+1}-1}$, i.e.
   $2^{n+1}-1>2(n+1)$, i.e. $2^{n+1}>2n+3$: true at $n=2$ ($8>7$) and,
   inductively, if $2^{n+1}>2n+3$ then $2^{n+2}=2\cdot2^{n+1}>2(2n+3)=
   4n+6>2n+5=2(n+1)+3$ (using $4n+6\ge2n+5\iff2n\ge-1$, always true).
   Hence $p_{n+1}(e_0)>\gamma(n)$ for every $n\ge2$, so *even the best
   possible* odd-parity value exceeds $c(n)$ by a genuinely
   non-shrinking-relative margin, regardless of $s$.
2. **Among even-parity $s$, the achieved value is $\le c(n)$ if and only
   if $n+1-s\le2$**, i.e. $s\ge n-1$: solving $\tfrac{\gamma(n)(n+1-s)}4
   \le\tfrac{\gamma(n)}2$ gives $n+1-s\le2$ directly. Since $s\le n$ is
   required (cut budget) and $n+1-s$ must be even and positive, the
   *only* legal value achieving this is $n+1-s=2$, i.e. $s=n-1$ exactly
   (the case $n+1-s=0$, i.e. $s=n+1$, would need $n+1$ cuts, exceeding
   the budget $n$ — illegal, matching the honest observation in Section
   4.3 of the sibling file that a genuine vertex construction must leave
   at least one piece untouched).
3. **At $s=n-1$ (the unique working case), the value is exactly $c(n)$
   — never strictly below.** ($n+1-s=2$ substituted: $\tfrac12+
   \tfrac{\gamma(n)\cdot2}4=\tfrac12+\tfrac{\gamma(n)}2=c(n)$ exactly.)

**Corollary (Bounded-$s_0$ impossibility, Perfect-Tie family).** For any
fixed $s_0$, once $n>s_0+1$, no Perfect-Tie construction (self-tie *or*
fragment-vs-fragment, in any combination) using $\le s_0$ active pieces
achieves $\mathrm{OddSum}(M)\le c(n)$: the family provably needs
$s=n-1$ pieces — growing without bound in $n$ — merely to *tie* $c(n)$,
and can *never* beat it strictly at any $s$.

*Proof of the Corollary.* Immediate from parts 1–2 of the Theorem: every
$s<n-1$ (whether even- or odd-parity) yields achieved value $>c(n)$
(part 1 for odd, part 2's threshold for even), so $s\ge n-1$ is
necessary; for fixed $s_0$, this fails once $n-1>s_0$. $\blacksquare$

**This is a genuine, complete, unconditionally proved negative result**,
independently verified in exact arithmetic above (Section 12.3), for a
construction family (Perfect-Tie: self-tie plus genuine cross-piece
fragment-vs-fragment tying, zero residual) that is **structurally
disjoint** from the round-11 Mass-Constraint Theorem's family (tie to a
whole untouched piece) — no untouched piece's value is ever consumed as
a tie target here, so Mass-Constraint's proof (which relies exactly on
that consumption, $\sum_aT_a=1-\Pi$) does not apply and could not have
been used to derive this. The two results are proved by genuinely
different techniques (a mass-summation inequality vs. an integer
combinatorics lemma) yet reach the same qualitative conclusion — this is
independent, convergent evidence that *no* small named-tool family
suffices at $e_0$, strengthening the case (flagged by the round-11/12
dispatch) that `global-lp-vertex-sufficiency`'s reduction-side route
(Region-Boundary Monotonicity) is the more promising path forward, not a
further search for a bounded construction family.

### 12.5 Honest scope: the fully general fragment-vs-fragment family (nonzero residual) is *not* closed

The Perfect-Tie restriction (Section 12.1, zero residual) is a genuine
proper sub-family of "fragment-vs-fragment tying" in general. A direct
check this round shows the restriction is **not free** — allowing a
nonzero residual strictly helps:

**Numerical check (unrestricted, `scipy.optimize.minimize`, Nelder–Mead,
softmax-parametrized fragment proportions, not exact — a sanity check
only, not part of the proof above).** At $n=6$, $s=3$ (active pieces
$\{p_1,p_2,p_3\}$, the "top-$3$" pattern also used by the round-12
explorer), splitting each active piece into $3$ free-valued fragments
(not constrained to perfect ties) and optimizing numerically: best found
$\approx0.5046$, strictly **below** the Perfect-Tie family's own exact
optimum at $s=3$ ($\tfrac12+\tfrac{\gamma(6)\cdot4}4=\tfrac12+\gamma(6)
\approx0.5079$, matching Section 12.3's $m=4$-even formula), though still
**above** $c(6)\approx0.5039$ — consistent with, not contradicting, the
round-12 explorer's own numeric finding that $s=3$ is not yet enough at
$n=6$ to strictly clear $c(n)$ (their search found $s=3$ reaches
*exactly* the tight value, matching the already-certified $V(e_0)=c(n)$
via a *different*, already-known-optimal construction — not a
counterexample to anything proved here).

**What this means.** The Theorem above (Section 12.4) is a complete,
proved answer for the Perfect-Tie sub-family specifically — it is **not**
a full resolution of whether *some* fragment-vs-fragment construction
with nonzero residual and bounded $s$ could beat $c(n)$. The general
question remains open, exactly as the round-12 dispatch anticipated
("worth at most one more focused attempt... if it also fails to give a
bounded-$s_0$ construction, record that as a further... negative data
point"). What *is* now established, rigorously: the most
resource-efficient natural sub-mechanism (perfect internal tying, no
wasted mass) is **provably** incapable of beating $c(n)$ with bounded
$s_0$ — strengthening, via an independent technique, the growing case
that no simple bounded-piece-count named-tool family will close the
Existence Theorem's Σ-shape gap, without fully proving impossibility for
every conceivable fragment-vs-fragment variant.

### 12.6 Conclusion for `global-lp-vertex-sufficiency`

Two independent proofs (Mass-Constraint, round 11; Perfect-Tie-Family
Characterization, round 12) now rule out bounded-$s_0$ sufficiency at
$e_0$ for two structurally disjoint natural construction families (tie-to-
whole-piece; perfect self-/fragment-tie), via two different techniques
(mass summation; integer combinatorics). Combined with the round-12
explorer's own soft numeric evidence that even the *unrestricted* search
(covering both families and everything in between) shows minimal
clearing $s$ growing with $n$, this file recommends `global-lp-vertex-
sufficiency` treat "some bounded-piece-count named construction works
uniformly at $e_0$" as very unlikely to be provable, and prioritize its
own Region-Boundary Monotonicity route (Opening 2) — which does not
require enumerating or bounding any construction family at all — over
further search in this direction, consistent with the round-12
outliner's own prioritization.
