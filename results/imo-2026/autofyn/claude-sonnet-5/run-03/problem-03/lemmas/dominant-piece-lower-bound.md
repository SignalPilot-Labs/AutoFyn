## Lemma: A piece exceeding the rest guarantees itself to the first claimer

**Statement (Global-max peeling identity).** Let $M$ be a finite multiset of
positive reals and let $g$ be (a copy of) $\max(M)$. Then
$$\mathrm{OddSum}(M) = g + \mathrm{EvenSum}(M\setminus\{g\}).$$
In particular, since $\mathrm{EvenSum}\ge0$ always, $\mathrm{OddSum}(M)\ge g$.

**Corollary (dominant-piece lower bound).** If a piece $T$ in a partition
strictly exceeds the sum of all other pieces present (equivalently, $T$ is
the unique maximum after any subsequent refinement of the *other* pieces
only, however many further cuts are used on them), then for *any* such
refinement, the first claimer's total (LB's, under the reduction of
`reduction-to-multiset-minimax.md`) is at least $T$.

**Proof of the identity.** Sort $M$ descending as $g=x_1\ge x_2\ge\cdots\ge x_m$
(choosing the removed copy of $\max M$ to sit at position $1$, always
possible). Then $M\setminus\{g\}$ sorted descending is exactly
$x_2,\dots,x_m$; its own position $j$ (for $2\le j\le m$) is $j-1$, so its
odd/even positions $1,2,\dots,m-1$ correspond to original positions
$2,3,\dots,m$ with parity flipped. Hence
$\mathrm{OddSum}(M)=x_1+x_3+x_5+\cdots = g+(x_3+x_5+\cdots)$, and
$x_3+x_5+\cdots$ is exactly $\mathrm{EvenSum}(M\setminus\{g\})$ (its own
positions $2,4,\dots$ correspond to original $3,5,\dots$). $\blacksquare$

**Proof of the corollary.** If $T$ strictly exceeds the sum of every other
piece present, then after any refinement of the other pieces (splitting
never increases a piece's length), every fragment is $<$ the sum of the
other pieces $\le T$... more precisely, since the *other* pieces' total
mass is fixed at (say) $R<T$ and refining only redistributes $R$ among more
(smaller-or-equal) pieces, no fragment of the other pieces can exceed $R<T$.
Hence $T$ remains the unique maximum $g=\max(M)$ of the resulting multiset
$M$ regardless of the refinement, and the identity above gives
$\mathrm{OddSum}(M)=T+\mathrm{EvenSum}(M\setminus\{T\})\ge T$. $\blacksquare$

**Source.** Peeling identity proved as Lemma 3 in
`approaches/greedy-reduction-geometric.md`; the corollary is proved (in
the specific form "if XY's cuts never touch LB's largest piece") as
"Theorem (Lower bound, Case 1)" there, and independently (in the form
"$j=0$ sub-case bound") in `approaches/self-similar-induction-on-n.md`.
Certified by the proof-reviewer, round 1.

**Reuse.** Gives, unconditionally and for every $n$: if LB uses the
geometric partition $r_i=2^i/(2^{n+1}-1)$ ($i=0,\dots,n$) and XY's response
never places a cut on LB's largest piece $r_n$, then LB's total is
$\ge r_n = c(n)$. This settles one whole branch of the still-open general
lower bound and is directly reusable by any future approach attacking the
remaining branch (XY spends $\ge1$ cut on LB's own largest piece).
