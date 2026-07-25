## Status
partial

## Approaches tried
- (round 1, prior) Setup of the state space, and three anchor lemmas (θ=90°
  win-in-one, doubling/bisection, "shave" forcing) stated with a numeric
  sanity check but not yet assembled into a full two-directional proof. Left
  as an open skeleton.
- (round 1, this pass) Rebuilt every lemma from a clean, fully algebraic
  derivation (no numerics-only checks); proved a considerably stronger and
  more general **Bisection Lemma** and **Altitude Lemma** than previously
  stated (both hold from *any* triangle, not just special ones); used them to
  give a **complete, rigorous construction for every even n ≥ 2** (i.e.
  θ = 90°, 45°, 30°, 22.5°, ... — θ of the form 180°/(2m)); gave a **complete,
  rigorous defense proof for every θ > 90°**. Identified precisely why the
  same toolkit does *not* immediately finish odd n (a residue obstruction
  that is invariant under the one tool — "shave" — that changes values by
  exactly θ, together with a proof that the other universal tool — bisection
  chained off the altitude — only ever manufactures values of the form
  90°/2^k, which never lands on a multiple of θ when n is odd). This
  obstruction and a concrete partial numeric fact (90° ≡ θ/2 (mod θ) when n
  is odd) are recorded below as the precise open gap, rather than an outline
  placeholder. Outcome: real, verified progress on both halves of the
  characterization, but the full result (all odd n ≥ 3, and the general
  "only if" for 0 < θ ≤ 90° not of the form 180°/n) remains open.

## Current best

**Target.** Mulan has a winning strategy iff θ = 180°/n for some integer
n ≥ 2.

### 0. Setup (re-derived from scratch)

Represent the current triangle $\mathcal T$ by its angle triple $(A,B,C)$
with $A,B,C>0$ and $A+B+C=180°$. If $\mathcal T$ has a cut from the vertex
with angle $A$ to a point $P$ on the opposite side, write $t=\angle$(between
one side of $A$ and segment $AP$) $\in(0,A)$; this is exactly Mulan's free
choice (any point $P\neq$ the two adjacent vertices on the side opposite $A$
corresponds bijectively to a value $t\in(0,A)$, by the standard
correspondence between points on a segment and the angle they cut off at the
opposite vertex — elementary, since the two rays from $A$ to the endpoints
of the opposite side bound the full angle $A$ and $P$ ranges continuously
between them). Writing the un-cut angles adjacent to $A$ as $B$ (near one
endpoint) and $C$ (near the other), the two resulting triangles are, by the
triangle angle sum applied to each of the two sub-triangles $ABP$ and $ACP$:
$$\text{child}_1=\{B,\,t,\,180-B-t\},\qquad \text{child}_2=\{C,\,A-t,\,B+t\}.$$
(Both triples sum to $180$: $B+t+(180-B-t)=180$ and $C+(A-t)+(B+t)=A+B+C=180$.
Both are genuine triangles for $t\in(0,A)$: in child$_1$, $B>0$ is given and
$t>0$, and $180-B-t>0$ because $t<A$ so $B+t<A+B<180$; in child$_2$, $A-t>0$
since $t<A$, $C>0$ given, and $B+t>0$ trivially.) Shan-Yu then picks either
child$_1$ or child$_2$ to be the new $\mathcal T$. Mulan may cut from *any*
of the three vertices, so by symmetry the same formulas apply with
$(A,B,C)$ permuted; this is the entire rule set of one move.

### 1. Three general lemmas (all proved in full generality — no special
hypotheses on the starting triangle beyond it not already containing θ)

**Lemma 1 (Altitude / universal 90° insertion).** From *any* triangle
$(A,B,C)$ (whatever its values), Mulan has a move such that **both**
possible resulting triangles contain an angle of exactly $90°$, regardless
of Shan-Yu's choice.

*Proof.* At most one of $A,B,C$ can be $\ge 90°$: if two were, their sum
would already be $\ge180°$, leaving no room for a positive third angle,
contradicting $A+B+C=180°$. Hence at least two of the three angles are
$<90°$. Let $M=\max(A,B,C)$ and cut the vertex with angle $M$; call the other
two angles $X,Y$ (so $\{M,X,Y\}=\{A,B,C\}$). Since $X,Y\le M$ and at most one
angle can be $\ge90°$, if $M\ge90°$ then $M$ is the (unique) angle that may
be $\ge90°$, forcing $X,Y<90°$; if $M<90°$ then trivially $X,Y\le M<90°$. In
either case $X<90°$ and $Y<90°$.

Set $t=90-X\in(0,M)$: it is positive since $X<90$, and it is $<M$ because
$t<M \iff 90-X<M \iff X+M>90 \iff Y<90$ (using $X+M+Y=180$), which holds.
So $t$ is a legal cut of the $M$-vertex. Using the formulas of §0 with
$A=M,B=X,C=Y$:
$$\text{child}_1=\{X,\ 90-X,\ 180-X-(90-X)\}=\{X,\,90-X,\,90\},$$
$$\text{child}_2=\{Y,\ M-(90-X),\ X+(90-X)\}=\{Y,\ M-90+X,\ 90\}.$$
(The middle entry of child$_2$ is positive because $M-90+X=180-Y-90=90-Y>0$,
using $Y<90$.) Both triples explicitly contain the entry $90$. $\blacksquare$

**Lemma 2 (Bisection).** From *any* triangle $(A,B,C)$, cutting the
$A$-vertex at $t=A/2$ produces, regardless of Shan-Yu's choice, a triangle
containing the angle $A/2$ exactly. Concretely
$$\text{child}_1=\{B,\,A/2,\,180-B-A/2\},\qquad \text{child}_2=\{C,\,A/2,\,B+A/2\},$$
both containing $A/2$.

*Proof.* Immediate substitution $t=A-t=A/2$ into the two formulas of §0
(both are legal cuts since $0<A/2<A$ for $A>0$). $\blacksquare$

**Lemma 3 (Shave — forced $\theta$-transfer).** Suppose the current triangle
$(A,B,C)$ has some angle $A>\theta$ (and no angle already $=\theta$, i.e. the
game has not yet stopped). Mulan may cut the $A$-vertex at $t=\theta$
(valid: $0<\theta<A$), giving
$$\text{child}_1=\{B,\,\theta,\,180-B-\theta\},\qquad \text{child}_2=\{C,\,A-\theta,\,B+\theta\}.$$
Then child$_1$ contains the angle $\theta$ exactly, so if Shan-Yu keeps
child$_1$ the game *already stops with Mulan winning*. Hence for Mulan's
purposes she may assume Shan-Yu keeps child$_2 = \{C,\,A-\theta,\,B+\theta\}$
— i.e. either Mulan already won, or the position deterministically becomes
$(C,\,A-\theta,\,B+\theta)$. By the symmetric argument (cutting at
$t=A-\theta$ instead, which poisons child$_2$), Mulan may instead force
$(B,\,A-\theta,\,C+\theta)$; so Mulan freely chooses which of $B,C$ receives
the $+\theta$.

*Proof of validity.* $t=\theta\in(0,A)$ since $0<\theta<A$ by hypothesis.
child$_1=\{B,\theta,180-B-\theta\}$: need $180-B-\theta>0$, i.e.
$B<180-\theta$; since $A>\theta$ and $C>0$, $B=180-A-C<180-\theta$, so this
holds. child$_2=\{C,A-\theta,B+\theta\}$: $A-\theta>0$ by hypothesis, $C>0$
given, $B+\theta>0$ trivially; sum $=A+B+C=180$. Both are legitimate
triangles, and child$_1$ visibly contains $\theta$. $\blacksquare$

**Corollary 3′ (clearing an exact multiple).** If some angle of the current
triangle equals $q\theta$ exactly for an integer $q\ge1$, Mulan wins in at
most $q-1$ further moves: if $q=1$ she has already won; if $q\ge2$, repeatedly
apply Lemma 3 with that same vertex as source (valid at each step since the
value is $q\theta,(q-1)\theta,\dots$, each $>\theta$ until it reaches
$\theta$ after $q-1$ shaves — the vertex persists as the same physical
vertex throughout, because at each shave Shan-Yu's only alternative to
keeping it is an immediate loss). This uses Lemma 3 exactly $q-1$ times.

### 2. Full proof of the "only if" direction for θ > 90°

**Claim.** If $\theta>90°$, Shan-Yu can defend forever (so $\theta$ is *not*
a winning value for Mulan). Note this automatically excludes all
$\theta=180°/n$ with $n\ge2$, since those satisfy $\theta\le90°$.

*Proof.* Shan-Yu starts with the equilateral triangle $(60°,60°,60°)$; this
is legal since $\theta>90°>60°$ means no angle equals $\theta$ yet. He
maintains, as an invariant across the whole game, that **every current
angle is $<\theta$**. This invariant holds initially since $60°<90°<\theta$.

Suppose the invariant holds for the current triangle $(A,B,C)$ (all
$<\theta$) and Mulan cuts the $A$-vertex at some $t\in(0,A)$, producing
child$_1=\{B,t,180-B-t\}$ and child$_2=\{C,A-t,B+t\}$ as in §0. The two
"new" entries $180-B-t$ (in child$_1$) and $B+t$ (in child$_2$) sum to
exactly $180$. Since $\theta>90°$, $2\theta>180°$, so it is impossible for
both of these to be $\ge\theta$ (else their sum would be $\ge2\theta>180$).
Hence at least one of the two children has its new entry $<\theta$; call
this child the *safe* one. In the safe child, the entry $B$ or $C$
(whichever survives) is $<\theta$ by the invariant, the entry $t$ or $A-t$
is $<A<\theta$ (again by the invariant on $A$, since $t<A$ and $A-t<A$), and
the new entry is $<\theta$ by construction. So the safe child has all three
angles $<\theta$. Shan-Yu keeps the safe child, restoring the invariant.

By induction, the invariant "all angles $<\theta$" holds after every move,
forever. In particular no angle is ever exactly $\theta$, so the game never
stops and Mulan never wins. $\blacksquare$

### 3. Full proof of the "if" direction for all even n ≥ 2 (θ = 180°/n, n even)

**Claim.** If $n=2m$ is even ($m\ge1$), i.e. $\theta=90°/m$, Mulan wins from
*any* starting triangle in exactly $m$ moves.

*Proof.* Suppose Shan-Yu's triangle has no angle $=\theta$ already (else
Mulan has already won in $0$ moves). Apply Lemma 1: in one move, Mulan
forces (regardless of Shan-Yu's choice) a resulting triangle containing the
angle $90°$. Since $\theta=90°/m$, we have $90°=m\theta$, an exact integer
multiple of $\theta$ with $m\ge1$.

- If $m=1$ ($n=2$, $\theta=90°$): this $90°$ angle already equals $\theta$,
  so the game has already stopped and Mulan has won, in $1$ move total.
- If $m\ge2$: apply Corollary 3′ to this angle, which equals $q\theta$ with
  $q=m$: Mulan wins in $q-1=m-1$ further forced moves (Lemma 3 applied
  $m-1$ times to the same vertex, each time it is $>\theta$ until it hits
  $\theta$ exactly). Total moves: $1+(m-1)=m$.

In both cases Mulan forces a win in exactly $m=n/2$ moves, from any starting
triangle, against any play by Shan-Yu. $\blacksquare$

This fully settles $\theta=90°,45°,30°,22.5°,18°,\dots$ (every $\theta=180°/n$
with $n$ even).

### 4. Where the proof is genuinely incomplete

**(a) Odd $n\ge3$ (e.g. $\theta=60°,36°,180°/7,\dots$), "if" direction.**

The obstruction, precisely: call two triangle-states *shave-equivalent* if
one is reachable from the other by a sequence of Lemma-3 moves only. Since
each Lemma-3 move changes exactly one current angle by $-\theta$ and another
by $+\theta$ (and leaves the third untouched), by induction on the number of
shaves, **every angle present at every stage of a shave-only sequence is
congruent mod $\theta$ to one of the three original angles** $A_0,B_0,C_0$
of the triangle at the start of that sequence (the residue "belongs" to a
persistent physical vertex and is never altered or mixed by a shave: the
source's value changes by exactly $-\theta$, the recipient's by exactly
$+\theta$, both preserving residue mod $\theta$; the untouched vertex is
literally unchanged). Consequently pure shaving can only ever produce an
angle $\equiv0\pmod\theta$ (needed to reach exactly $\theta$ via Corollary
3′) if the state already contains such an angle. Shan-Yu can trivially avoid
this at the start (e.g. choose all three initial angles to have irrational
ratio to $\theta$).

The one *value-independent* tool available (Lemma 1) always inserts exactly
$90°$, never any other absolute value; chaining Lemma 1 with Lemma 2
(bisection) on the same forced vertex only ever produces the dyadic family
$90°,\,90°/2,\,90°/4,\dots$ In units of $\theta$: $\dfrac{90}{2^k\theta}=
\dfrac{n}{2^{k+1}}$, which is an integer for some $k\ge0$ **iff $n$ is a
power of $2$ times such** — in particular never for odd $n\ge3$. So neither
tool alone, nor the two chained in this way, ever manufactures a multiple of
$\theta$ when $n$ is odd.

A partial refinement was computed: for $n$ odd, $90°\equiv \theta/2
\pmod\theta$ exactly. (Derivation: $90/\theta=n/2$; write $n=2j+1$, so
$\lfloor n/2\rfloor=j$ and $90-j\theta=90-\tfrac{j\cdot180}{n}
=\tfrac{90n-180j}{n}=\tfrac{90(n-2j)}{n}=\tfrac{90}{n}=\tfrac\theta2$, using
$n-2j=1$.) So Lemma 1 followed by $\tfrac{n-1}2$ applications of Lemma 3 on
the same vertex (each valid, since the intermediate values
$90,90-\theta,\dots,90-(\tfrac{n-3}2)\theta=\tfrac{3\theta}2$ all exceed
$\theta$) forces, after $\tfrac{n+1}2$ moves and regardless of Shan-Yu, an
angle of exactly $\theta/2$ — one shave short of $\theta$, and shaving is
unavailable below $\theta$. This is genuine, verified partial progress
(a forced exact value strictly between $0$ and $\theta$, with a known exact
relation to $\theta$), but it does **not** by itself produce a win: no tool
in hand converts a forced $\theta/2$ into a forced $\theta$. Whether some
different combination of cuts (not restricted to re-cutting a single tracked
vertex, and not restricted to the altitude+shave toolkit) forces a win for
every odd $n\ge3$ is the central open question of this approach.

**(b) $0<\theta\le90°$ with $\theta$ not of the form $180°/n$, "only if"
direction.** No Shan-Yu invariant analogous to §2's "all angles $<\theta$"
has been found or proved here: that invariant relies on $2\theta>180°$
(pigeonhole giving a safe child), which fails precisely for $\theta\le90°$.
A natural guess — that Shan-Yu can maintain "no reachable finite sequence of
moves forces an angle whose value mod $\theta$ is $0$" using an argument
dual to §4(a)'s obstruction — has **not** been turned into an actual
strategy: §4(a) only shows one *specific* Mulan algorithm (shave, or
shave-after-altitude) fails to finish; it does not rule out an entirely
different, more clever Mulan algorithm succeeding even when $180°/\theta$
is not an integer. This is flagged as open, not conjectured true or false
beyond the "if" direction already proved for divisors.

### 5. Summary of what is established

- $\theta>90°$: Shan-Yu wins (Mulan cannot). **Fully proved (§2).**
- $\theta=180°/n$, $n$ even $\ge2$ (i.e. $\theta\in\{90°,45°,30°,\dots\}$):
  Mulan wins, in exactly $n/2$ moves from any start. **Fully proved (§3).**
- $\theta=180°/n$, $n$ odd $\ge3$: **not settled.** Strong partial tool
  (forces $\theta/2$ deterministically) but no complete win.
- $0<\theta\le90°$, $\theta\ne180°/n$ for any integer $n$: **not settled.**
  No Shan-Yu defense found yet.

## Open gaps
- Complete the "if" direction for odd $n\ge3$: find a finite forced (or
  branching-but-exhaustively-handled) sequence of cuts that produces an
  angle exactly $\theta$ from any starting triangle, when $180/\theta=n$ is
  odd. The obstruction in §4(a) rules out the "single tracked vertex via
  altitude+shave+bisection" family of algorithms; a genuinely different
  combination (e.g. using two different vertices' bisections in tandem,
  exploiting the fixed total $180°=n\theta$) is needed.
- Prove the "only if" direction for all $\theta\le90°$ not of the form
  $180°/n$: construct an explicit Shan-Yu strategy/invariant defeating every
  possible Mulan algorithm (not just the shave-based ones). This is the
  deepest gap in the whole problem.
- If the above two gaps are closed, the answer "$\theta=180°/n,\ n\in
  \mathbb Z_{\ge2}$" would be fully verified; as it stands the characterization
  is proved only for $\theta>90°$ (no) and $\theta=180°/n$ with $n$ even (yes).

## Full proof
(Not present — Status is `partial`; see §2, §3 above for the two fully
rigorous pieces obtained, and §4 for the precise remaining gaps.)

## Promotable lemmas
- **Altitude Lemma** (§1, Lemma 1): from any triangle, one move forces an
  angle of exactly 90° into the resulting triangle regardless of the
  opponent's choice. Proved in full (existence of a valid vertex via the
  "at most one angle ≥90°" pigeonhole, plus explicit algebraic verification
  that both children contain 90°).
- **Bisection Lemma** (§1, Lemma 2): from any triangle, bisecting any vertex
  forces that vertex's halved value into the resulting triangle regardless
  of the opponent's choice. Proved by direct substitution.
- **Shave Lemma** (§1, Lemma 3) and its **Corollary 3′**: from any triangle
  with an angle $A>\theta$, Mulan can force a deterministic
  $\theta$-transfer $(A,B,C)\to(C,A-\theta,B+\theta)$ (recipient of her
  choice) unless Shan-Yu hands her an immediate win; iterating on the same
  vertex clears any angle that is an exact multiple $q\theta$ down to exactly
  $\theta$ in $q-1$ moves. Proved in full.
- **θ>90° defense invariant** (§2): "all angles $<\theta$" is preserved by
  Shan-Yu against every Mulan move whenever $\theta>90°$, via the
  supplementary-pair pigeonhole $180°-\theta<\theta$. Proved in full,
  reusable verbatim by any other approach attacking the same direction.
- **Even-n construction** (§3): $\theta=180°/n$ for even $n$ is won by Mulan
  in exactly $n/2$ moves via Altitude + Corollary 3′. Proved in full.
