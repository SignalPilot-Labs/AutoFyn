## Lens: extend Half-Window Vanishing Lemma from c_1=1 to general c_1≥2

Read: `problems.jsonl` (imo-2026-03), `knowledge_base.md`, `results/imo-2026-03/current.md`,
`results/imo-2026-03/approaches/rank-tie-vertex-reduction.md` (§5.1–5.4, the
Cross-Term Reduction Theorem and Half-Window Vanishing Lemma), and the cascade
lemma `results/imo-2026-03/lemmas/cascading-halving-family-characterization.md`.
The Half-Window lemma lives inline in `rank-tie-vertex-reduction.md` §5.2 — no
separate `lemmas/half-window-vanishing-lemma.md` file exists yet (not promoted).

All computations below use exact `fractions.Fraction` (no floats) on the
ladder $p_i=2^{n+1-i}/(2^{n+1}-1)$.

### 1. Hand data for c_1=2 (n=2, n=3, n=4)

**Setup recap.** Xiang Yu's response to piece $p_1$ with $c_1$ cuts produces
$c_1+1$ fragments $y_1\ge\dots\ge y_{c_1+1}>0$ summing to $p_1$. The window
formula generalizes immediately: $u(t):=\mathbb1[N_F(t)\text{ odd}]$ is, for
sorted fragments, the indicator of $\lceil (c_1+1)/2\rceil$ **disjoint
half-open intervals** ("teeth"), not one window. For $c_1=2$ (3 fragments
$y_1\ge y_2\ge y_3$): $u=\mathbb1_{[0,y_3)}\cup\mathbb1_{[y_2,y_1)}$, and
$A(F)=y_3+(y_1-y_2)$ — this is exactly the Odd-Run Reduction Lemma's content,
just written as an integral.

**n=2** ($p_1,p_2,p_3=4,2,1$ /7, $f(2)=1/7$): $c_1=2$, tail forced untouched
(budget exhausted). Exact vertex enumeration (all $\binom{d\text{-eqn
pairs}}{2}$ constraint intersections, $d=2$) gives global min $A=1/7$,
attained **only** at a degenerate vertex $u=0$ (one of the two cuts wasted),
i.e. this collapses to the already-solved $c_1=1$ symmetric split
$\{p_1/2,p_1/2\}=\{2/7,2/7\}$. No genuine ($u,v$ both interior) $c_1=2$
vertex beats or matches this — consistent with "$c_1\ge2$ always degenerates"
for $n=2$, but $n=2$'s tail is too small (only 2 pieces) to show anything
richer.

**n=3** ($p_1..p_4=8,4,2,1$ /15, $f(3)=1/15$): $c_1=2$, tail untouched. Exact
vertex enumeration finds the min $A=1/15=f(3)$ at a **genuine, non-degenerate**
vertex: fragments $(y_1,y_2,y_3)=(4/15,2/15,2/15)$, i.e. $p_1$ splits into
$\{p_2,p_3,p_3\}$ exactly (using $p_1=p_2+2p_3$, true because $p_1=2p_2=4p_3$
on the ladder). This looked at first like a *new* tie-vertex type not covered
by the $c_1\le1$ population. **But it is not new**: the resulting full
multiset $\{p_2,p_3,p_3\}\cup\{p_2,p_3,p_4\}=\{p_2,p_2,p_3,p_3,p_3,p_4\}$ is
**exactly** the certified cascade member $R_2$ (`cascading-halving-family-
characterization`, $k=n-1=2$), which physically cuts the *separate* pieces
$p_1\to\{p_2,p_2\}$ and $p_2\to\{p_3,p_3\}$ (composition $(1,1,0,0)$, not
$(2,0,0,0)$). The two compositions give literally the same multiset of
lengths only because of the ladder coincidence $p_1=2p_2=4p_3$: cutting
$p_1$'s own interval directly into $\{p_2,p_3,p_3\}$ with **2 cuts entirely
inside $p_1$** reproduces, length-for-length, what "cut $p_1$ in half, then
cut one resulting half again" does with cuts spread over two different
original pieces. So this data point is a **relabeling coincidence**, already
closed by the certified cascade lemma — not a gap, but also not evidence the
generic $c_1=2$ case is automatically safe.

**n=4** ($p_1..p_5=16,8,4,2,1$ /31, $f(4)=1/31$): tested whether the n=3
coincidence generalizes.
- $c_1=2$ with tail **fully** untouched (only 2 of the 4 available cuts
  used): exact vertex enumeration gives min $A=3/31 > f(4)=1/31$ — this
  composition alone does **not** reach the target. (Fragments at the min:
  $\{p_2,p_3,p_3\}$ again, tail untouched; odd-run reduces the full multiset
  $\{p_2,p_2,p_3,p_3,p_3,p_4,p_5\}$ to $\{p_3,p_4,p_5\}\to A=p_3-p_4+p_5=3/31$.)
  This shows the n=3 "$c_1=2$ alone matches $R_{n-1}$" coincidence is
  **special to $n=3$** and does not hold verbatim at $n=4$ — reproducing
  $R_3$ (which needs 3 cuts, one each in $p_1,p_2,p_3$) requires *also*
  spending budget on the real $p_3$.
- $c_1=2$ (giving $\{p_2,p_3,p_3\}$) **plus** 1 more cut on the real $p_3$
  (composition $(2,0,1,0,0)$, using 3 of the 4 available cuts, budget to
  spare): exact vertex enumeration on the remaining free pair finds min
  $A=1/31=f(4)$ **exactly**, attained where $p_3$'s two cut-parameters
  degenerate to one real cut splitting $p_3\to\{p_4,p_4\}$ (the other
  parameter is $0$, wasted). The resulting full multiset
  $\{p_2,p_3,p_3\}\cup\{p_4,p_4\}\cup\{p_2,p_4,p_5\}
  =\{p_2,p_2,p_3,p_3,p_4,p_4,p_4,p_5\}$ is again **exactly $R_3$'s multiset**
  — reached this time via composition $(2,0,1,0,0)$ instead of $R_3$'s own
  $(1,1,1,0,0)$, again purely by the ladder-ratio coincidence
  $p_1=2p_2=4p_3$, applied telescopically one level at a time.

**Takeaway of the hand data.** Every minimizing $c_1\ge2$ vertex found so far
(across $n=2,3,4$) is, as a final multiset, **identical to** an already-
certified cascade member $R_k$ reached by a *different*, equivalent-length
composition — never a genuinely new value. But this equivalence is not
automatic/structural in the way I first assumed (the $n=4$ "$c_1=2$, tail
untouched" test shows a *naive* front-loading is NOT enough by itself; it
only reaches the target once the *matching* deeper cut is also present).

### 2. Does the midpoint-splitting idea recurse? — breaks down, concretely

The Half-Window Vanishing Lemma's proof needs exactly **one** window
$W=[p_1-x,x)$ straddling the single midpoint $p_2=p_1/2$, split into a left
half (trivial bound $v\le1$) and a right half (proved $\equiv0$ since no
tail element exceeds $p_2$). For $c_1=2$ this breaks in two concrete ways:

1. **The window is no longer one interval.** With 3 fragments $y_1\ge y_2\ge
   y_3$, $u$ is supported on **two** disjoint intervals $[0,y_3)$ and
   $[y_2,y_1)$ (shown above from the Odd-Run structure). The second interval
   $[y_2,y_1)$ can still be handled by an analogue of the half-window trick
   *if* it straddles $p_2$ appropriately, but the **first interval $[0,y_3)$
   is anchored at the origin**, not at a ladder-forced midpoint — there is no
   analogue of "$p_2$ is exactly the midpoint" to split it at, since it
   already starts at $t=0$.
2. **Concrete numeric failure of the naive per-window sufficient condition.**
   At the n=3 vertex above ($y_1,y_2,y_3=4/15,2/15,2/15$, tail untouched,
   $r=7/15$): $u=\mathbb1_{[0,4/15)}$ (the two "teeth" merge into one interval
   because $y_2=y_3$). The natural generalized sufficient condition would be
   $\int_{[0,r)}uv\le A(F)/2$ (mirroring $(\star\star)$, with $A(F)$ playing
   the role of $\Delta$). Here $A(F)=y_3+(y_1-y_2)=4/15$, so the needed bound
   is $\int uv\le 2/15$. Direct computation of $v$ (tail's own odd-parity
   indicator, tail untouched, $T=\{4,2,1\}/15$): $v=1$ on $[0,1/15)$, $0$ on
   $[1/15,2/15)$, $1$ on $[2/15,4/15)$, giving $\int_{[0,4/15)}v=1/15+2/15=
   3/15=1/5$. **This exceeds $2/15$** — the naive per-window bound genuinely
   fails here (by a factor of $1.5$), even though the final $A(F\cup T)=1/15$
   still equals $f(3)$ exactly. The reason it still works out is that
   $A(G')=A(T)=3/15$ has *slack* over its floor $f(n-1)\cdot r$ that
   compensates — i.e. the failure is a failure of the **decoupled**
   bound (bound the cross-term and the tail-floor independently), not of the
   final inequality itself. This is a genuine, reproducible obstruction to
   "just copy the same lemma with more windows": **the two-piece decomposition
   $A(F)+A(G')-2\int uv$ is not separable window-by-window once $F$ has $\ge3$
   fragments**, because the origin-anchored window $[0,y_3)$ interacts with
   the *exact value* of $A(G')$, not just its floor.

**Verdict: midpoint-splitting does not recurse verbatim.** It needs the
window to be anchored at a ladder-forced midpoint of a *symmetric* pair; a
$\ge3$-fragment $F$ generically produces a window touching $t=0$, where there
is no such symmetric structure to exploit directly.

### 3. A different, more promising mechanism: peel-one-cut induction on $c_1$

The concrete data in §1 (every found $c_1\ge2$ extremal vertex equals a
cascade member reached by re-timing one cut at a time) points at a cleaner
recursive mechanism, distinct from "generalize the same lemma":

**Idea.** Instead of treating all $c_1$ cuts on $p_1$ at once, peel off the
*first* cut: any $c_1$-cut fragmentation of $p_1$ can be written as one cut
splitting $p_1\to\{z,\,p_1-z\}$ ($z\ge p_1-z$ WLOG, using the Vertex-Minimum
Theorem's symmetry) **followed by** an arbitrary legal $(c_1-1)$-cut
fragmentation applied to the *smaller* piece $p_1-z$ only (the case where the
remaining cuts split $z$ instead is a separate, symmetric sub-case, not yet
ruled out — see gap below). This is exactly item (1)'s Cross-Term Reduction
Theorem applied once, with $G' := (\text{fragmentation of }p_1-z)\cup T$
treated as a single enlarged "tail" of total mass $r':=(p_1-z)+r$. By
`tail-self-similarity` applied at *this* combined tail (already the
mechanism `symmetric-split-c1-lower-bound`/§5.1 use for the real tail), one
would hope to get $A(G')\ge f(n)$ by an **inductive hypothesis on $c_1$**
(not on $n$): "every legal $(c_1-1)$-cut fragmentation of $p_1-z$ combined
with the real tail dominates," with base case $c_1-1\in\{0,1\}$ already fully
closed (untouched / Half-Window). This would turn "general $c_1$" into an
ordinary induction with a clean base case, **provided** two things are
established (neither done here, both flagged as concrete next steps, not
claimed):
(a) the "WLOG further cuts land in the smaller piece $p_1-z$" reduction is
    actually valid (i.e. that the alternative — further cuts inside the
    larger piece $z$ — is dominated by, or reduces to, this case via the
    Vertex-Minimum Theorem's tie/degeneracy structure);
(b) the analogue of $(\star\star)$ for this induction step (bounding the new
    cross-term between $\{z,p_1-z\}$ and the enlarged tail $G'$) — this is
    *exactly* the already-solved $c_1=1$ Half-Window Vanishing Lemma applied
    verbatim (since at the top level it's genuinely a 1-cut split), so **no
    new inequality needs to be invented at the top level** — only the
    induction hypothesis on the enlarged tail's own $A(G')\ge f(n)$-type
    floor needs to be established, recursively.

This reframes "general $c_1$" as: apply the **already-proved** $c_1=1$
Half-Window Lemma once at the top, then recurse into a strictly smaller
sub-instance. The n=3/n=4 hand data is consistent with this: in both found
extremal examples, the vertex is literally "cut $p_1$ into $\{p_2,p_1-p_2\}$
[a $c_1=1$-shaped top-level split, since $p_1-p_2=p_2$ here — the symmetric
case], then recurse into the second $p_2$-sized piece with the remaining
$c_1-1$ cuts" — precisely this peeling pattern.

**Open technical risk (not resolved by this exploration):** the induction
needs $A(G')\ge f(n)$ where $G'$ is a fragmentation of $(p_1-z)\cup T$, a
mass strictly less than the full $(1-p_1+{}$ nothing$)$... concretely $G'$'s
total mass is $r'=(p_1-z)+r$, which is **not** simply $r$ from an
$(n-1)$-ladder — it's $p_1-z$ (a piece of the *first* ladder level) glued to
the *whole* original tail $T$ (all of levels $2,\dots,n+1$). This is **not**
literally an $(n-1)$-ladder rescaled (that would need total mass exactly
$r=1-p_1$ and shape $p_2,\dots,p_{n+1}$ rescaled) — it is a genuinely
different shape (an extra "foreign" piece of size $p_1-z$ spliced in), so
`tail-self-similarity` does **not** apply verbatim; a genuinely new
self-similarity/rescaling lemma for "ladder tail plus one foreign piece"
would need to be proved first. This is the real remaining gap, and it looks
tractable (the foreign piece has a known size relative to the ladder, namely
$z\le p_1$ so $p_1-z\ge0$, and by the vertex-minimum structure $z$ is itself
either $0$, $p_1$, or tied to some $p_j$ or to another fragment — a finite
list of shapes) but was **not attempted or closed** in this exploration.

### 4. Knowledge base / crux corpus check

`knowledge_base.md` has no entries specific to nested/recursive interval
decompositions beyond generic "induction" and "generalize the hypothesis"
advice (lines ~183–228) — nothing to borrow directly. The crux corpus
subtopics most likely to have a load-bearing analogous move are, in
`combinatorics`: `extremal-principle`, `invariants-and-monovariants`,
`induction-and-construction`, and `games-and-strategy` (this problem's own
domain/flavor); in `algebra`: `size-bounding-and-descent` and
`telescoping-and-summation` (the alternating-sum machinery here is exactly a
telescoping/size-bounding argument). I did not query the corpus API itself
(out of scope for an explorer's time budget) — flagging these subtopics as
the ones worth a targeted retrieval pass by the outliner/builder before
inventing the peel-induction machinery from scratch, since "peel the extremal
element and recurse" is a very standard extremal-principle/induction move
that likely has a directly adaptable crux.

### 5. Recommendation for the outliner

- **Do not** pursue "generalize Half-Window Vanishing to $c_1\ge2$ directly"
  as a single lemma — §2 gives a concrete, reproducible counterexample to the
  natural per-window sufficient condition (the origin-anchored window issue),
  so this is a real dead end, not just an unproven risk.
- **Do** pursue the peel-one-cut induction on $c_1$ (§3): it is structurally
  clean, its base case is already fully proved, and it matches 100% of the
  hand data collected (every $c_1\ge2$ extremal vertex found in $n=2,3,4$
  decomposes exactly this way). Its one real gap is a new self-similarity
  lemma for "ladder tail spliced with one foreign piece of size $p_1-z$" —
  this is a concrete, scoped, likely-tractable target for a builder, not a
  vague direction.
- Flag explicitly for whoever attacks (a) in §3: the "WLOG further cuts land
  in the smaller piece" step needs its own justification (possibly via the
  Vertex-Minimum Theorem's affine-on-each-cell structure, comparing the two
  symmetric sub-cases directly) — this was assumed, not proved, here.
