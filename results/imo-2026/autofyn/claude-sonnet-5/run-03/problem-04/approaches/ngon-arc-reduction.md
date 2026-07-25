## Status
solved

## Approaches tried
- (round 1, fresh) The outline proposed reducing the θ=180/n case to a discrete
  divider/token game on n arcs, "forcing integrality of the units first" via a
  compactness/pigeonhole argument, and separately flagged the θ≤90°,
  non-divisor "only if" direction as the shared open core gap across all
  approaches.
- (this round) I abandoned the literal "discrete n-gon token game" packaging
  (it added a layer of translation without simplifying anything) and instead
  worked directly with the real-valued angle triples and the residues mod θ.
  This produced two clean, fully rigorous, and load-bearing new moves:
  (1) an explicit **residue-alignment cut** that, from ANY triangle with no
  angle a multiple of θ but some angle exceeding θ, forces BOTH possible
  children (regardless of Shan-Yu's choice) to acquire a new angle that IS an
  exact positive integer multiple of θ — closing the "if" direction in full
  generality (n≥3) without any discrete-game machinery; and (2) a **residue
  non-degeneracy invariant** ("no angle ≡ 0 mod θ") that I prove Shan-Yu can
  maintain against literally every possible cut (any vertex, any real
  parameter t) whenever θ ∤ 180 — this closes the "only if" direction in full
  generality, subsuming the previously-only-partial θ>90° case as a special
  instance of the same unified mechanism. Both directions were additionally
  checked numerically (exact-`Fraction` arithmetic, thousands of random
  trials) before being written up; the numerical checks are not part of the
  proof but caught no discrepancy with the algebra below. Outcome: complete
  proof of the full characterization, both directions, all cases (n=2, n≥3,
  θ>90°, θ≤90° non-divisor) covered without gaps.

## Current best
See Full proof below — the approach is complete.

## Full proof

**Answer.** Mulan has a winning strategy if and only if θ = 180°/n for some
integer n ≥ 2.

Throughout, angles are measured in degrees and treated as real numbers; all
arithmetic ("mod", floors) is on reals. For a triangle write its angle-triple
as (A,B,C) with A+B+C=180.

### 0. The cut formula

**Lemma 0 (cut formula).** Let a triangle have angles X (at vertex R), Y (at
vertex P), Z (at vertex Q), with X+Y+Z=180. If Mulan cuts from a point on side
PQ to the opposite vertex R, and t = ∠PRP' ∈ (0,X) is the portion of angle X
on the P-side of the cut, then the two resulting triangles have angle-triples
$$\text{child}_1=(Y,\,t,\,180-Y-t),\qquad \text{child}_2=(Z,\,X-t,\,Y+t),$$
and every t ∈ (0,X) is achievable, and every achievable cut of this triangle
(from any of its three vertices) has this form for some choice of which
vertex is "cut" and which two are "Y" and "Z".

*Proof.* Let the point be P'. In triangle RPP' (child 1): the angle at P is
the original angle Y (unchanged, since P' lies on segment PQ so ray PP' =
ray PQ); the angle at R is t by definition; the angle at P' is
180 − Y − t by the angle sum of a triangle. In triangle RQP' (child 2): the
angle at Q is the original angle Z (unchanged, same reasoning); the angle at
R is X − t (the remaining part of angle X); the angle at P' is the angle
∠RP'Q which is supplementary to ∠RP'P = 180 − Y − t, i.e. equals
Y+t. This matches (Z, X−t, Y+t) since 180−(180−Y−t) = Y+t. As P' ranges over
the open segment PQ (excluding the vertices, as required by the problem),
t = ∠PRP' ranges continuously and bijectively over the open interval (0,X)
(t→0 as P'→P, t→X as P'→Q, and ∠PRP' is a strictly monotonic function of the
position of P' on segment PQ). Since Mulan may choose any vertex of the
triangle to be "R" and, having fixed R, may call either of the other two
vertices "P" (equivalently "Y"), this describes every possible move. ∎

For a fixed θ with 0<θ<180, and any real x, write
$$\rho(x) = x - \theta\left\lfloor \frac{x}{\theta}\right\rfloor \in [0,\theta)$$
for the residue of x modulo θ. We say x is a **θ-multiple** if ρ(x)=0. Note
that "T has an angle equal to θ" implies (but is not implied by) "T has an
angle that is a θ-multiple"; we will sometimes prove the stronger statement
that some angle is forced to be an exact θ-multiple, which is enough to
finish the game off (Lemma 2 below), and we will show Shan-Yu can forbid
θ-multiples entirely, which certainly forbids angle = θ.

### 1. The "if" direction: θ = 180/n, n ≥ 2 integer ⟹ Mulan wins

**Lemma 1 (n=2 case, θ=90°).** From any starting triangle without a 90°
angle, Mulan wins in exactly one move.

*Proof.* Since the triangle has no angle equal to 90°, and it is impossible
for two angles to be ≥90° simultaneously (their sum would already be ≥180°,
leaving no positive room for the third angle), at least two of the angles
are strictly less than 90°, i.e. acute. Say the acute angles are at vertices
P and Q; let R be the third vertex. Set up coordinates with P at the origin
and Q on the positive x-axis at distance PQ. Let H be the foot of the
perpendicular from R to line PQ. Then the signed distance PH equals
$PR\cos(\angle P)$ and QH equals $QR\cos(\angle Q)$ (standard right-triangle
trigonometry applied to the two right triangles RPH, RQH, or their
degenerate/mirror versions). Since ∠P,∠Q ∈ (0°,90°), both cosines are
strictly positive, so PH>0 and QH>0; since also PH+QH=PQ (the two signed
projections onto line PQ from a point R always sum to PQ once R is on the
correct side, which it is since it's a vertex of a genuine triangle with P,Q
), it follows 0<PH<PQ, i.e. H lies strictly between P and Q on the open
segment. Hence H is a legal cut point P' for Mulan (interior to a side,
not a vertex). Cutting from H to R, by Lemma 0 the two children have angle
∠RHP and ∠RHQ at H; by construction RH⊥PQ, so both of these angles equal
90° exactly. So both children already contain a 90° angle: whichever child
Shan-Yu keeps, the game stops immediately with Mulan's win. ∎

**Lemma 2 (pure shave).** Suppose the current triangle has some angle
X > θ, at vertex R, with the other two angles Y (at P), Z (at Q). Cutting
from R to the point P' on PQ with t = θ gives
$$\text{child}_1 = (Y,\ \theta,\ 180-Y-\theta),\qquad
\text{child}_2 = (Z,\ X-\theta,\ Y+\theta).$$
Child 1 already has the angle θ, so if Shan-Yu keeps it the game stops in
Mulan's favor immediately; hence Shan-Yu is **forced** (on pain of an
immediate loss) to discard child 1 and keep child 2. Consequently:
whenever the current triangle has an angle that is a positive integer
multiple kθ (k≥1) at some vertex, Mulan can, by repeatedly applying this
move to that same vertex (choosing either of the other two angles as
"recipient" each time, her free choice), force — regardless of anything
Shan-Yu does — a deterministic sequence of k−1 further moves after which
that vertex's angle equals exactly θ, ending the game in her favor. (If
k=1 already, the game is already over.)

*Proof.* The formula for child1, child2 is Lemma 0 with t=θ, valid since
0<θ<X. Child1 contains θ as one of its angles by inspection, so keeping it
is an immediate loss for Shan-Yu (per the game's stopping rule), while the
other choice, child2, is forced. In child2 the designated vertex's angle has
become X−θ = (k−1)θ, the "recipient" has increased by θ, and the third angle
Z is untouched. If k−1 ≥ 1, repeat the same move at the same vertex (now
with angle (k−1)θ), forcing (k−2)θ next, and so on; after k−1 total
applications the vertex's angle is exactly θ, and the game has already
ended (in fact it ends the moment that vertex's angle first equals θ, i.e.
after exactly k−1 applications of this forced move, with no other outcome
possible since each application forces Shan-Yu's hand). This is a finite
process since k is a fixed positive integer. ∎

**Lemma 3 (residue-alignment move).** Fix n≥3 and θ=180°/n. Suppose the
current triangle (X,Y,Z) has NO angle that is a θ-multiple (i.e.
ρ(X),ρ(Y),ρ(Z) all lie in (0,θ), all strictly positive), and suppose
X>θ (cut vertex R has angle X, the other two vertices P,Q carry angles Y,Z
respectively). Let $r_Y=\rho(Y)$ and set $t=\theta-r_Y\in(0,\theta)\subset(0,X)$.
Cutting from R to the point on PQ realizing this t produces
$$\text{child}_1=(Y,\ \theta-r_Y,\ (n-m-1)\theta),\qquad
\text{child}_2=(Z,\ X-\theta+r_Y,\ (m+1)\theta),$$
where $m=\lfloor Y/\theta\rfloor$, and both $n-m-1$ and $m+1$ are integers
with $1\le n-m-1\le n-1$ and $1\le m+1\le n-1$. In particular **both possible
children already have some angle equal to an exact positive integer
multiple of θ**, regardless of which one Shan-Yu keeps.

*Proof.* Write $Y=m\theta+r_Y$ with $m=\lfloor Y/\theta\rfloor\ge 0$ integer
and $r_Y\in(0,\theta)$ (strict, since Y is not a θ-multiple by hypothesis).
By Lemma 0 with this t:
$$\text{child}_1\text{'s third angle} = 180-Y-t = n\theta-(m\theta+r_Y)-(\theta-r_Y)
= (n-m-1)\theta,$$
using $180=n\theta$ (since θ=180/n) and the $r_Y$ terms cancelling exactly.
This is a positive integer multiple of θ provided $n-m-1\ge 1$, i.e. $m\le n-2$.
We verify $m\le n-2$ always holds under our hypotheses: since X>θ and Z>0,
$Y=180-X-Z<180-\theta=(n-1)\theta$, so $\lfloor Y/\theta\rfloor\le n-2$
(as $Y/\theta<n-1$ forces the floor to be at most $n-2$). Hence $n-m-1\ge1$,
confirmed, and also $n-m-1\le n-1$ trivially since $m\ge0$.

For child2: $Y+t = (m\theta+r_Y)+(\theta-r_Y) = (m+1)\theta$, exactly, a
positive integer multiple of θ with $1\le m+1\le n-1$ (the upper bound
again from $m\le n-2$). Also $X-t = X-\theta+r_Y$; since $X>\theta$, this is
positive, and it is less than X, so child2 = $(Z,\,X-\theta+r_Y,\,(m+1)\theta)$
is a genuine triangle with positive angles summing to $Z+(X-\theta+r_Y)+(m+1)\theta
= X+Z+r_Y-\theta+(m+1)\theta = X+Z+r_Y+m\theta = X+Z+Y=180$, consistent.
Likewise child1's three angles $Y,\ \theta-r_Y,\ (n-m-1)\theta$ are all
positive real numbers (the middle one since $r_Y<\theta$) summing to 180 by
construction, so child1 is a genuine triangle too. ∎

**Theorem 1 ("if" direction).** If θ = 180°/n for an integer n≥2, Mulan wins
in a finite number of moves against any Shan-Yu play.

*Proof.* Case n=2: Lemma 1, done in exactly one move.

Case n≥3: First, a pigeonhole fact.

*Claim: if the current triangle has no angle equal to θ, some angle
exceeds θ.* Suppose not: all three angles are ≤θ, and (since none equals θ)
all are strictly <θ. Then their sum is <3θ≤nθ=180 (using n≥3), contradicting
that the angle sum of a triangle is exactly 180. This proves the claim.

Now, starting from any triangle T (Shan-Yu's arbitrary choice) with no angle
equal to θ:

- **Case A: some angle of T is already a θ-multiple.** Say that angle is
  kθ for an integer k≥1; since no angle equals θ, in fact k≥2 (k=1 would
  already mean an angle equals θ). Apply Lemma 2 to that vertex: after
  k−1 further forced moves (Shan-Yu has no real choice at each step, as
  shown in Lemma 2), the game ends in Mulan's win. This uses ≤n−1 moves in
  total, since $k\le n$ (an angle can be at most the total sum $180=n\theta$,
  in fact strictly less, so $k\le n-1$).

- **Case B: no angle of T is a θ-multiple.** By the pigeonhole claim above,
  some angle of T exceeds θ; call it X (at vertex R), and call the other
  two Y, Z (at the other two vertices, in either order — fix an arbitrary
  choice of which is "Y"). By hypothesis of Case B, Y is not a θ-multiple,
  so Lemma 3 applies: after the single residue-alignment cut of Lemma 3,
  **both** possible resulting triangles (child1 and child2) already contain
  an angle that is a positive integer multiple of θ, with multiplier
  between 1 and n−1. Whichever child Shan-Yu keeps, that triangle satisfies
  the hypothesis of Lemma 2 (an angle equal to $j\theta$ for some integer
  $1\le j\le n-1$): if $j=1$, the game is already over (Mulan has won,
  0 further moves needed); if $j\ge2$, Lemma 2 applies and forces a win in
  $j-1\le n-2$ further moves. So Case B produces a win in at most
  $1+(n-2)=n-1$ moves total.

In both cases the total number of moves is finite (bounded above by
$n-1$, a fixed number depending only on n, hence only on θ), and the outcome
does not depend on any choice Shan-Yu makes along the way — every step
after Mulan's residue-alignment cut (if any) is a forced Lemma-2 shave, and
Shan-Yu's only two genuine choices in the whole argument are which child to
keep after Lemma 3's alignment cut (both branches are shown to lead to a
Mulan win) and the initial triangle itself (arbitrary, both cases A and B
are covered). Hence Mulan wins in at most $n-1$ moves from every possible
initial triangle Shan-Yu could choose, and every possible sequence of his
subsequent choices. ∎

### 2. The "only if" direction: θ ≠ 180/n for any integer n≥2 ⟹ Shan-Yu wins

Write $r_0 = \rho(180) = 180 - \theta\lfloor 180/\theta\rfloor \in[0,\theta)$,
a fixed constant determined by θ alone. Note $r_0=0$ if and only if
$\theta\mid 180$, i.e. $180/\theta$ is a positive integer; since $0<\theta<180$
forces $180/\theta>1$, this integer is automatically $\ge2$. So:
$$\theta = 180/n \text{ for some integer } n\ge2 \iff r_0=0,$$
and the case to handle is exactly $r_0\ne0$.

**Theorem 2 ("only if" direction).** If $r_0\ne 0$ (equivalently θ is not of
the form 180/n for an integer n≥2), Shan-Yu can choose an initial triangle
and play forever so that no angle of the triangle is ever equal to θ; hence
Mulan does not have a winning strategy.

*Proof.* Define the invariant property
$$\mathcal{I}:\quad \text{none of the triangle's three angles is a θ-multiple}
\ \ (\rho(A),\rho(B),\rho(C)\in(0,\theta)\text{ for the current angles }A,B,C).$$
Since $\theta=1\cdot\theta$ is itself a θ-multiple, $\mathcal I$ in
particular implies no angle equals θ exactly, so maintaining $\mathcal I$
forever is a valid defense for Shan-Yu.

**Step 1: $\mathcal I$ is achievable initially.** We must exhibit a triangle
(A,B,C), A+B+C=180, A,B,C>0, with none of A,B,C a θ-multiple. Consider the
one-parameter family $A=\theta/2$ (fixed; note $\theta/2\in(0,\theta)$, not a
θ-multiple, and $\theta/2<180$), $B=s$, $C=180-\theta/2-s$ for
$s\in(0,\,180-\theta/2)$. For each fixed choice of s, B fails to satisfy
"not a θ-multiple" only for s in the discrete (countable) set
$\theta\mathbb Z\cap(0,180-\theta/2)$, and C fails only for s in the discrete
set $\{180-\theta/2-k\theta : k\in\mathbb Z\}\cap(0,180-\theta/2)$. The union
of these two countable sets is countable, while the interval
$(0,180-\theta/2)$ is uncountable; hence some $s$ avoids both bad sets,
giving a triangle with A,B,C all non-θ-multiples. Shan-Yu opens with this
triangle.

**Step 2: $\mathcal I$ is preserved by Shan-Yu's optimal reply to every
possible Mulan move.** Suppose the current triangle (X,Y,Z) satisfies
$\mathcal I$ and Mulan cuts from the vertex carrying angle X (WLOG, by the
symmetry of the argument below under relabelling which of the three angles
is "the one being cut" — the identical computation applies verbatim if she
cuts the Y- or Z- vertex instead, with the roles permuted), with parameter
$t\in(0,X)$, other two angles Y (adjacent, becomes Y+t in child2), Z
(untouched in child2). By Lemma 0:
$$\text{child}_1=(Y,\,t,\,180-Y-t),\qquad \text{child}_2=(Z,\,X-t,\,Y+t).$$

Write $r_X=\rho(X), r_Y=\rho(Y), r_Z=\rho(Z)$, all in $(0,\theta)$ by
$\mathcal I$, and let $s=\rho(t)\in[0,\theta)$. We compute, working modulo
θ throughout (i.e. all displayed congruences are mod θ, and $180\equiv r_0$):

- child1 contains a θ-multiple angle iff $Y\equiv0$ (false, since $r_Y\ne0$),
  or $t\equiv0$ (i.e. $s=0$), or $180-Y-t\equiv0$, i.e.
  $s\equiv r_0-r_Y \pmod\theta$.
  So **child1 is "bad"** (has a θ-multiple angle) exactly when
  $s\in\{0,\ (r_0-r_Y)\bmod\theta\}$.

- child2 contains a θ-multiple angle iff $Z\equiv0$ (false, since $r_Z\ne0$),
  or $X-t\equiv0$, i.e. $s\equiv r_X\pmod\theta$, or $Y+t\equiv0$, i.e.
  $s\equiv -r_Y\pmod\theta$.
  So **child2 is "bad"** exactly when $s\in\{r_X,\ (-r_Y)\bmod\theta\}$.

We claim the two bad-sets are disjoint, i.e.
$\{0,(r_0-r_Y)\bmod\theta\}\cap\{r_X,(-r_Y)\bmod\theta\}=\varnothing$, given
$r_X,r_Y,r_Z\in(0,\theta)$, $r_0\ne0$, and the relation
$r_X+r_Y+r_Z\equiv X+Y+Z=180\equiv r_0\pmod\theta$ (this relation holds since
the sum of the three current angles is always exactly 180, invariant under
the game). Check all four possible coincidences:

  (i) $0\equiv r_X\ (\mathrm{mod}\ \theta)$: false, since $r_X\in(0,\theta)$
      means $r_X\ne0$.

  (ii) $0\equiv -r_Y\ (\mathrm{mod}\ \theta)$: this would force $r_Y\equiv0$,
       false since $r_Y\in(0,\theta)$.

  (iii) $r_0-r_Y\equiv r_X\ (\mathrm{mod}\ \theta)$: this rearranges to
        $r_0\equiv r_X+r_Y\ (\mathrm{mod}\ \theta)$. Combined with
        $r_X+r_Y+r_Z\equiv r_0\ (\mathrm{mod}\ \theta)$, subtracting gives
        $r_Z\equiv0\ (\mathrm{mod}\ \theta)$ — false, since $r_Z\in(0,\theta)$.

  (iv) $r_0-r_Y\equiv -r_Y\ (\mathrm{mod}\ \theta)$: this rearranges to
       $r_0\equiv0\ (\mathrm{mod}\ \theta)$ — false, since $r_0\ne0$ is our
       standing hypothesis (this is the unique place where $r_0\ne0$, i.e.
       $\theta\ne180/n$, is used).

All four coincidences are false, so the two bad-sets are disjoint two- (or
fewer-) element subsets of $[0,\theta)$. Since $s=\rho(t)$ is a single value,
it cannot lie in both bad-sets simultaneously. Hence **at least one of
child1, child2 is "good"** (has no θ-multiple angle, i.e. satisfies
$\mathcal I$). Shan-Yu keeps a good child (if both are good, either choice
works). This shows: for every vertex Mulan might cut and every $t\in(0,X)$
she might choose, Shan-Yu has a response preserving $\mathcal I$.

**Step 3: conclude.** By Step 1, Shan-Yu can start in a state satisfying
$\mathcal I$. By Step 2 and induction on the number of moves played, Shan-Yu
can always respond to Mulan's move so that $\mathcal I$ continues to hold.
Since $\mathcal I$ implies "no angle equals θ," the game never reaches
Mulan's winning condition, no matter how many moves are played and no
matter how Mulan plays. Hence Mulan has no strategy that forces a win in
finitely many moves against this Shan-Yu play (indeed against this specific
opening triangle and this specific defensive response the game runs
forever, i.e. never stops — Shan-Yu survives indefinitely), so Mulan does
not have a winning strategy for this θ. ∎

### 3. Conclusion

Combining Theorem 1 (θ=180/n, n≥2 integer ⟹ Mulan wins in finitely many
moves against every Shan-Yu strategy) and Theorem 2 (θ not of this form ⟹
Shan-Yu can choose an opening triangle and play so the game never reaches a
θ-angle, i.e. Mulan cannot force a win), we conclude:

$$\boxed{\text{Mulan has a winning strategy} \iff \theta = \dfrac{180^\circ}{n}\ \text{for some integer } n\ge2.}$$

**Verification of the answer.** The characterization is verified directly by
the two theorems above, which are proofs, not mere consistency checks; as
an additional sanity check, both directions were confirmed by exact
rational-arithmetic computer search (thousands of random trials: for the
"if" direction, verifying Lemma 3's claim that both children of the
alignment cut acquire a θ-multiple angle, for random n from 3 to 12 and
random non-θ-multiple starting triangles; for the "only if" direction,
verifying that the two "bad" residue sets found in Theorem 2 are always
disjoint for random non-divisor θ, random $\mathcal I$-satisfying triangles,
and random cut parameters $t$) — zero discrepancies found in either
direction, consistent with the algebraic proofs above. ∎

## Promotable lemmas

- **Lemma 0 (cut formula)** — proved in full above (elementary triangle
  angle-sum / supplementary-angle argument). Shared setup used by every
  approach in this problem's population; safe to certify as a base lemma.

- **Lemma 1 (θ=90° / n=2 base case, altitude-drop)** — proved in full above
  (existence of a vertex with two acute base angles, and that the altitude
  foot from it lies strictly inside the opposite side). Matches the
  informally-stated "Lemma 1" in the sibling approach files; this write-up
  makes the geometric justification (why the foot lands strictly between
  the two acute-angle vertices) fully rigorous rather than asserted.

- **Lemma 2 (pure shave / forced-shave chain)** — proved in full above.
  Matches the "Shave lemma" used informally across all sibling approach
  files; here stated and proved with the explicit forced-chain consequence
  (k−1 further forced moves to finish from a kθ angle).

- **Lemma 3 (residue-alignment move, new)** — proved in full above: a single
  explicit cut (t=θ−ρ(Y)) from any vertex with angle >θ, given no current
  angle is a θ-multiple, forces BOTH possible children to acquire an exact
  θ-multiple angle. This is the new mechanism that finally closes the "if"
  direction's previously-open reduction-to-normal-form gap, without any
  discrete token/divider game machinery.

- **Theorem 2's disjoint-bad-sets argument (new)** — proved in full above:
  the invariant "no angle is a θ-multiple" is preserved by Shan-Yu against
  every possible Mulan cut (any vertex, any real parameter), whenever
  θ∤180. This closes the "only if" direction in full generality (unifying
  the previously-separate θ>90° partial argument with the θ≤90° open gap
  into one mechanism) and is the single most reusable result for any other
  approach file or for `results/imo-2026-04/current.md`.
