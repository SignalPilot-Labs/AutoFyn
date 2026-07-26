# IMO 2026 P4 — Mulan's Triangle Game — approach `safe-unsafe-pairing`

**Target claim (full characterization, both directions):**
Mulan can guarantee victory in finitely many steps, no matter how Shan-Yu plays, if and only if $\theta = 180^\circ/n$ for some integer $n\ge 2$ (equivalently, $180^\circ/\theta\in\mathbb Z$).

This approach proves necessity via the **safe/unsafe external-angle dichotomy** (the canonical invariant, phrased here as a coset-arithmetic lemma proved from scratch) and sufficiency via the **deedy round-up / deficit-pairing** construction (a genuinely different entry mechanism from the altitude route: the load-bearing object is the "round-up deficit" $d(x)$, and the engine is a deficit-sum pigeonhole, not an altitude).

---

## Status

solved

## Approaches tried

- **safe-unsafe-pairing (this route, round 1):** necessity via four-coset closure of the "safe" complement (external-angle identity, proved from scratch); sufficiency via the round-up deficit function $d(x)=\lceil x/\theta\rceil\theta - x$, the deficit-sum lemma $d(a)+d(b)+d(c)\in\{\theta,2\theta\}$, the pairing lemma (cyclic-sum contradiction), and a $k$-descent. Both directions complete; all sub-lemmas proved; $n=2$ handled separately. Verified numerically across $n\in\{3,4,5,6,7,11,60,180\}$ and across non-winning $\theta\in\{40,50,72,80,89,91,100,110,70,33\}$. — worked.

## Current best

Complete rigorous proof of the characterization (see Full proof). Every case settled: $n=2$ (deficit argument degenerates, handled by a direct $90^\circ$-trick), $n\ge 3$ (the pairing route), the "already-won" cases (some angle a multiple of $\theta$, in particular some angle $=\theta$), and the Shan-Yu-defense cases (all $\theta\ne 180^\circ/n$). Move bound $\le n-1$.

## Full proof

We write all angles in degrees and abbreviate "$\theta$-marked" for "is a positive integer multiple of $\theta$" (i.e. lies in $\theta\mathbb Z_{>0}=\{\theta,2\theta,3\theta,\dots\}$). A triangle is **$\theta$-marked** if at least one of its three angles is $\theta$-marked; otherwise it is **$\theta$-safe** (or just *safe* when $\theta$ is fixed). Note that the winning condition — some angle equals exactly $\theta$ — is the special case of "$\theta$-marked with multiplier $1$," so Mulan wins the moment the state is $\theta$-marked with multiplier $1$.

### 0. Reduction to the angle game (cut-geometry lemma)

The state of play is completely described by the **angle multiset** $(a,b,c)$ with $a,b,c>0$ and $a+b+c=180^\circ$; side lengths are irrelevant (they are never read by the rules). We record how a move acts on this multiset.

**Cut-geometry lemma.** Let the current triangle have vertex angles $A,B,C$ (so $A+B+C=180^\circ$). If Mulan cuts from a point $P$ on side $BC$ (the side opposite $A$) to vertex $A$, and if $\alpha:=\angle BAP\in(0,A)$, the two children have angle multisets

$$\triangle ABP:\;(\alpha,\; B,\; 180^\circ-B-\alpha),\qquad \triangle ACP:\; (A-\alpha,\; C,\; B+\alpha).$$

Conversely, **every** $\alpha\in(0,A)$ is realizable: as $P$ moves along $BC$ from $B$ to $C$, the angle $\angle BAP$ varies continuously (and strictly increasingly) from $0$ to $A$, so by the intermediate value theorem it attains each value in $(0,A)$.

*Proof.* In $\triangle ABP$, the angles are $\angle BAP=\alpha$, $\angle ABP=B$ (since $P\in BC$), and the angle at $P$ equals $180^\circ-\alpha-B$. In $\triangle ACP$, the angles are $\angle CAP=A-\alpha$, $\angle ACP=C$, and the angle at $P$ (supplementary to the angle at $P$ in $\triangle ABP$, since $BC$ is a straight line through $P$) equals $B+\alpha$. ∎

The same lemma applies (by relabelling) to a cut from a point on the side opposite any chosen vertex. Throughout, when we say "cut at vertex $A$ with parameter $\alpha$" we mean this move with $\alpha=\angle BAP$.

---

### I. NECESSITY: $\theta\ne 180^\circ/n\;\Longrightarrow\;$ Shan-Yu defends forever

Assume $\theta\ne 180^\circ/n$ for every integer $n\ge 2$; equivalently $180^\circ\notin\theta\mathbb Z$ (i.e. $180^\circ/\theta\notin\mathbb Z_{\ge 2}$). We exhibit a Shan-Yu strategy that keeps the state $\theta$-safe forever, which in particular keeps every angle different from $\theta$.

#### I.1. The four-coset closure lemma

**Lemma (safe triangles cannot split into two marked children).** Suppose $\theta\ne 180^\circ/n$. If the current state $(a,b,c)$ is $\theta$-safe (no angle is a positive multiple of $\theta$), then for **every** legal cut, at least one of the two children is $\theta$-safe.

*Proof.* By the reduction of §0 we may assume the cut is at vertex $A$ (angle $a$) with parameter $\alpha\in(0,a)$; the other two angles are $b,c$. The children are
$$ C_1=(\alpha,\;b,\;180^\circ-b-\alpha)=(\alpha,\;b,\;a+c-\alpha),\qquad C_2=(a-\alpha,\;c,\;b+\alpha), $$
where we used $a+b+c=180^\circ$ to write $180^\circ-b=a+c$.

Suppose, for contradiction, that **both** children are $\theta$-marked. Then $\alpha$ lies in the "marked-or-not" locus of each child. Since $b$ and $c$ are $\theta$-safe by hypothesis, the only angles in each child that can possibly be $\theta$-marked are the two *new* angles (those that depend on $\alpha$):

- $C_1$ is marked $\iff \alpha\in\theta\mathbb Z\;\cup\;(a+c-\theta\mathbb Z)$.
- $C_2$ is marked $\iff \alpha\in(a-\theta\mathbb Z)\;\cup\;(-b+\theta\mathbb Z)$.

(Here $\theta\mathbb Z$ denotes the set of *all* integer multiples $\{0,\pm\theta,\pm 2\theta,\dots\}$; membership includes the value $0$, which is irrelevant for angles since $\alpha>0$, but it is harmless in the algebra. The condition for an angle to be a *positive* multiple is what defines $\theta$-marked; the coset arithmetic is the same either way, since if e.g. $\alpha\in\theta\mathbb Z$ and $\alpha>0$ then $\alpha$ is a positive multiple.)

Both children marked forces $\alpha$ to lie in the intersection of these two two-element unions, hence in **one of the four pairwise intersections**:

| intersection | forces | contradicts |
|---|---|---|
| (i) $\theta\mathbb Z\cap(a-\theta\mathbb Z)$ | $\alpha=m\theta=a-k\theta\Rightarrow a=(m+k)\theta\in\theta\mathbb Z$ | $a$ safe ✗ |
| (ii) $\theta\mathbb Z\cap(-b+\theta\mathbb Z)$ | $\alpha=m\theta=-b+k\theta\Rightarrow b=(k-m)\theta\in\theta\mathbb Z$ | $b$ safe ✗ |
| (iii) $(a+c-\theta\mathbb Z)\cap(a-\theta\mathbb Z)$ | $a+c-m\theta=a-k\theta\Rightarrow c=(m-k)\theta\in\theta\mathbb Z$ | $c$ safe ✗ |
| (iv) $(a+c-\theta\mathbb Z)\cap(-b+\theta\mathbb Z)$ | $a+c-m\theta=-b+k\theta\Rightarrow a+b+c=(m+k)\theta\Rightarrow 180^\circ\in\theta\mathbb Z$ | $\theta\ne 180^\circ/n$ ✗ |

Intersections (i)–(iii) contradict the hypothesis that $a,b,c$ are $\theta$-safe; intersection (iv) contradicts $180^\circ\notin\theta\mathbb Z$. The four intersections are **exhaustive** (the intersection of two two-element unions is exactly the union of the four pairwise intersections). Hence no $\alpha$ makes both children marked, i.e. at least one child is safe. ∎

*(Same lemma via external angles.)* The identical fact can be read geometrically: the four new angles created by the cut satisfy the external-angle identities $\angle CDA = \angle B+\angle BAP$ and $\angle DAC=\angle A-\angle BAP=\angle ADB-\angle C$ (exterior-angle theorem of $\triangle ABD$ at $D$ and $\triangle ACD$ at $D$). The sum or difference of a $\theta$-safe angle and a $\theta$-marked angle is $\theta$-safe (else the safe angle would be a difference of two multiples of $\theta$, hence itself a multiple — contradiction). With $180^\circ$ itself safe (the load-bearing input, from $\theta\ne 180^\circ/n$), this forces: if one child is marked, the other is safe. This is the same four-coset argument in geometric language; we use the algebraic form above for the proof.

#### I.2. Shan-Yu's strategy

Shan-Yu opens with the **equilateral** triangle $(60^\circ,60^\circ,60^\circ)$. We check it is $\theta$-safe: if $60^\circ=k\theta$ for some positive integer $k$, then $\theta=60^\circ/k=180^\circ/(3k)$, contradicting $\theta\ne 180^\circ/n$. So the opening state is safe.

Thereafter, by the four-coset closure lemma, after every Mulan cut at least one child is $\theta$-safe; Shan-Yu keeps a safe child. By induction the state is $\theta$-safe forever. A $\theta$-safe state has no angle that is any positive multiple of $\theta$, in particular no angle equals $\theta$. So Mulan never wins. ∎

This completes the **necessity** direction: $\theta\ne 180^\circ/n\Rightarrow$ Mulan cannot guarantee victory.

---

### II. SUFFICIENCY: $\theta=180^\circ/n\;\Longrightarrow\;$ Mulan wins in $\le n-1$ moves

Fix $\theta=180^\circ/n$ for an integer $n\ge 2$, so $180^\circ=n\theta$.

We begin with a standard descent that handles any state already containing a multiple of $\theta$.

#### II.1. Halving descent (the $k$-monovariant)

**Lemma (halving).** If the current triangle has an angle equal to $k\theta$ for an integer $k\ge 1$, then Mulan wins in $\le k-1$ further moves.

*Proof by strong induction on $k$.* Base $k=1$: the angle $\theta$ is present, Mulan has already won (0 moves). Step $k\ge 2$: cut at the vertex with angle $k\theta$, choosing parameter $\alpha=\theta$. This is legal since $0<\theta<k\theta$. By the cut-geometry lemma (with $a=k\theta$), the children are
$$ C_1=(\theta,\; b,\; 180^\circ-b-\theta),\qquad C_2=((k-1)\theta,\; c,\; b+\theta), $$
using $a-\alpha=k\theta-\theta=(k-1)\theta$ and $b+\alpha=b+\theta$ for the relevant entries. Child $C_1$ contains $\theta$: if Shan-Yu keeps it, Mulan wins. Otherwise Shan-Yu keeps $C_2$, which contains the angle $(k-1)\theta$; by the induction hypothesis Mulan then wins in $\le k-2$ more moves. Either way, $\le k-1$ moves total. ∎

(*Validity/positivity check.* The cut $\alpha=\theta$ is legal because $0<\theta<k\theta$ for $k\ge 2$. Every angle of $C_2$ is positive: $(k-1)\theta>0$ since $k\ge 2$; $c>0$ is an original angle; $b+\theta>0$ trivially; and the sum $((k-1)\theta+c+b+\theta)=(k\theta+b+c)=180^\circ$ checks out.)

So it remains to show Mulan can **force** a multiple of $\theta$ into the state in the first place, starting from an arbitrary triangle. The construction below does this in **one** move when $n\ge 3$, and in one move when $n=2$ by a separate argument.

#### II.2. The case $n=2$ ($\theta=90^\circ$): direct $90^\circ$-trick

For $n=2$ we have $\theta=90^\circ$ and $180^\circ=2\theta$. If some angle is already a positive multiple of $\theta$, the only such multiple strictly between $0$ and $180^\circ$ is $90^\circ=\theta$ itself, so Mulan has already won. Otherwise, **no** angle equals $90^\circ$.

**A triangle has at most one angle $\ge 90^\circ$** (two such angles would sum to $\ge 180^\circ$, leaving $\le 0$ for the third). Hence at least two angles are $<90^\circ$; call them $B$ and $C$, and let $A=180^\circ-B-C$ be the third. So $B,C<90^\circ$, and $A\ne 90^\circ$ (excluded); thus either $A<90^\circ$ (all-acute) or $A>90^\circ$ (one obtuse). Cut at the vertex with angle $A$, choosing parameter $\alpha=90^\circ-B$. We verify legality $\alpha\in(0,A)$:
- **Lower bound** $\alpha>0$: equivalent to $B<90^\circ$, given.
- **Upper bound** $\alpha<A$: equivalent to $90^\circ-B<A\iff 90^\circ<A+B=180^\circ-C\iff C<90^\circ$, given.

So the cut is legal. By the cut-geometry lemma (§0), the children are
$$ C_1=(\alpha,\,B,\,180^\circ-B-\alpha)=(90^\circ-B,\,B,\,90^\circ),\qquad C_2=(A-\alpha,\,C,\,B+\alpha)=(A-90^\circ+B,\,C,\,90^\circ). $$
Both children contain the angle $90^\circ=\theta$. Whichever Shan-Yu keeps, $\theta$ is present, so Mulan wins in **1** move. ∎ (This matches the $n-1=1$ bound; all child-angles are positive — $\alpha=90^\circ-B>0$, $A-\alpha=A-90^\circ+B=(180^\circ-B-C)-90^\circ+B=90^\circ-C>0$ since $C<90^\circ$, and the displayed $90^\circ$ and the carried $B,C$ are positive.)

#### II.3. The deficit function (round-up)

For the rest of sufficiency, assume $n\ge 3$ (so $\theta=180^\circ/n\le 60^\circ$). For any angle $x\in(0,180^\circ)$ define the **round-up deficit**
$$ d(x)\;=\;\bigl\lceil x/\theta\bigr\rceil\,\theta - x \;\in\; (0,\theta]. $$
If $x$ is a positive multiple of $\theta$ then $d(x)=\theta$ (by convention, $\lceil x/\theta\rceil\theta=x$ would give $0$; we resolve this conventionally below). To avoid ambiguity, fix the convention
$$ m_x := \min\{m\in\mathbb Z_{\ge 1}:\; m\theta \ge x\},\qquad d(x):=m_x\theta - x \;\in\; [0,\theta), $$
so that $m_x\in\{1,\dots,n\}$ (since $x<180^\circ=n\theta$ gives $m_x\le n$, and $x>0$ gives $m_x\ge 1$), and $x+d(x)=m_x\theta$ is a positive multiple of $\theta$, with $d(x)\in[0,\theta)$ and $d(x)=0\iff x=m_x\theta$ is already a multiple.

With this convention, $d(x)=0$ exactly when $x$ is $\theta$-marked. So if the current state has any $\theta$-marked angle, we are in the halving regime of §II.1 and done. Hence **for the rest of the construction we may (and do) assume all three angles are $\theta$-safe**, so $d(a),d(b),d(c)\in(0,\theta)$ strictly (each angle lies strictly between two consecutive multiples of $\theta$).

#### II.4. The deficit-sum lemma

**Lemma.** If $a+b+c=180^\circ=n\theta$ and none of $a,b,c$ is a multiple of $\theta$, then
$$ d(a)+d(b)+d(c)\in\{\theta,\,2\theta\}. $$

*Proof.* Write $a=m_a\theta-d(a)$, $b=m_b\theta-d(b)$, $c=m_c\theta-d(c)$ with $m_a,m_b,m_c\in\{1,\dots,n\}$. Summing,
$$ 180^\circ \;=\; (m_a+m_b+m_c)\,\theta \;-\;\bigl(d(a)+d(b)+d(c)\bigr). $$
Since $180^\circ=n\theta$, rearranging gives
$$ d(a)+d(b)+d(c) \;=\; (m_a+m_b+m_c-n)\,\theta. \tag{$\star$} $$
So the deficit-sum is a (possibly zero or negative) integer multiple of $\theta$. Each $d(\cdot)\in(0,\theta)$, so the deficit-sum lies in the open interval $(0,\,3\theta)$, hence (being a multiple of $\theta$) it lies in $\{\theta,2\theta\}$ — *provided it is positive*, which we now check.

**Positivity and ruling out $3\theta$.** Equation $(\star)$ shows $m_a+m_b+m_c\ge n+1$ would give a positive deficit-sum. Could we have $m_a+m_b+m_c=n$ (deficit-sum $0$)? That would force $d(a)+d(b)+d(c)=0$, impossible since each $d>0$. Could we have $m_a+m_b+m_c<n$ (negative deficit-sum)? Impossible, since the deficit-sum is a sum of three positive terms. Hence $m_a+m_b+m_c\ge n+1$, and the deficit-sum is positive.

Finally, the deficit-sum $<3\theta$ strictly (three terms each $<\theta$), so it cannot be $3\theta$ either. Hence $d(a)+d(b)+d(c)\in\{\theta,2\theta\}$. ∎

*(Equivalent direct ruling-out of $3\theta$.)* The excluded case $d(a)+d(b)+d(c)=3\theta$ would force each $d(\cdot)\to\theta$, i.e. each angle just below a multiple of $\theta$; in the extreme, $m_x=n$ for all three would give $a,b,c>180^\circ-\theta\ge 120^\circ$ (since $\theta\le 60^\circ$ for $n\ge 3$), three angles all $>120^\circ$ cannot sum to $180^\circ$. The argument above rules this out cleanly via the strict bound.

#### II.5. The pairing lemma

**Lemma (pairing, refined).** Under the hypotheses of §II.4 (in particular $n\ge 3$), there exist two **distinct** angles $u,v$ among $\{a,b,c\}$ with $d(u)<v$ **and** $m_u\le n-1$.

(The extra condition $m_u\le n-1$ ensures $u+d(u)=m_u\theta<n\theta=180^\circ$, so the supplementary multiple $(n-m_u)\theta$ is *positive* — needed in §II.6.)

*Proof.* Recall $m_x=\min\{m\ge 1:m\theta\ge x\}\in\{1,\dots,n\}$, and $m_x=n$ iff $x\in(180^\circ-\theta,\,180^\circ)$. Call an angle **top** if $m=n$, i.e. it lies in $(180^\circ-\theta,180^\circ)$. Since $\theta\le 60^\circ$ (as $n\ge 3$), a top angle is $>120^\circ$; two such would sum to $>240^\circ>180^\circ$. Hence **at most one** of $a,b,c$ is top. Let $T$ be the set of top angles, $|T|\in\{0,1\}$.

We argue by contradiction: assume no valid pairing exists, i.e. for every distinct pair $(u,v)$ with $m_u\le n-1$ (so $u\notin T$) we have $d(u)\ge v$ for all $v\ne u$.

**Case 1: $|T|=0$ (all three angles non-top, $m\le n-1$).** The assumption applies to all three. Specialize to the cyclic pairs $(u,v)=(a,b),(b,c),(c,a)$:
$$ d(a)\ge b,\qquad d(b)\ge c,\qquad d(c)\ge a. $$
Summing,
$$ d(a)+d(b)+d(c)\;\ge\; a+b+c \;=\; 180^\circ \;=\; n\theta. $$
But by the deficit-sum lemma (§II.4) the left side is $\le 2\theta$, so $n\theta\le 2\theta$, i.e. $n\le 2$ — contradicting $n\ge 3$.

**Case 2: $|T|=1$.** Relabel so $c$ is the (unique) top angle: $c\in(180^\circ-\theta,180^\circ)$, $m_c=n$. Then $a,b$ are non-top ($m_a,m_b\le n-1$), and
$$ a+b \;=\; 180^\circ-c \;<\; \theta, $$
so in particular $a,b\in(0,\theta)$, giving $m_a=m_b=1$ and $d(a)=\theta-a,\;d(b)=\theta-b$.

The contradiction assumption (applied to the non-top $u=a$, against both $v=b$ and $v=c$) gives $d(a)\ge c$, i.e. $\theta-a\ge c\iff \theta\ge a+c=180^\circ-b\iff b\ge 180^\circ-\theta$. Symmetrically, applied to $u=b$ against $v=c$: $d(b)\ge c\iff\theta-b\ge c\iff a\ge 180^\circ-\theta$. So the assumption forces $a\ge 180^\circ-\theta$ and $b\ge 180^\circ-\theta$, hence
$$ a+b \;\ge\; 2(180^\circ-\theta)\;=\;360^\circ-2\theta \;\ge\; 360^\circ-120^\circ \;=\; 240^\circ $$
(since $\theta\le 60^\circ$). But $a+b=180^\circ-c<180^\circ<240^\circ$ — contradiction.

Both cases contradict, so a valid pairing (with $m_u\le n-1$) exists. ∎

#### II.6. The pairing cut — both children marked in one move

Pick distinct angles $u,v$ from the pairing lemma, with $d(u)<v$. We cut at the vertex with angle $v$. The other two angles are $u$ and $w$ (the third angle, $w=180^\circ-u-v$). Set the cut parameter $\alpha=d(u)$. This is a legal cut: $d(u)>0$ because $u$ is $\theta$-safe (not a multiple), and $d(u)<v$ is exactly the pairing lemma's conclusion. So $0<\alpha=d(u)<v$, placing $\alpha$ inside the legal range $(0,v)$.

By the cut-geometry lemma (cut at vertex $v$, with the angle $u$ on the "$B$" side — relabel the two other vertices so that the carried angle on the $C_1$ side is $u$), the two children are
$$ C_1=\bigl(d(u),\; u,\; 180^\circ-u-d(u)\bigr),\qquad C_2=\bigl(v-d(u),\; w,\; u+d(u)\bigr). $$
Now use the definition of $d$: $u+d(u)=m_u\theta$ is a positive multiple of $\theta$, and (since $180^\circ=n\theta$)
$$ 180^\circ-u-d(u)\;=\; n\theta-m_u\theta\;=\;(n-m_u)\theta. $$
By the refined pairing lemma, $m_u\le n-1$, so $n-m_u\ge 1$ and $(n-m_u)\theta$ is a **positive** multiple of $\theta$ (this is exactly why the refinement was needed: without it, the top case $m_u=n$ would give $(n-m_u)\theta=0$, a degenerate zero angle). Hence:
- $C_1$ contains the angle $(n-m_u)\theta$ (a positive multiple of $\theta$);
- $C_2$ contains the angle $m_u\theta$ (a positive multiple of $\theta$).

**Both children are $\theta$-marked**, regardless of which Shan-Yu keeps. ∎

#### II.7. Completing sufficiency and the move bound

From an arbitrary starting triangle with $n\ge 3$:
- If some angle is already a multiple of $\theta$: skip to the descent (§II.1). In particular, if some angle $=\theta$, done in 0 moves.
- Otherwise (all three $\theta$-safe): Mulan plays the pairing cut of §II.6. Both children are $\theta$-marked; whichever Shan-Yu keeps has an angle $k\theta$ with $1\le k\le n-1$. By the halving lemma (§II.1) Mulan wins in $\le k-1\le n-2$ further moves.

**Total move bound for $n\ge 3$:** $\;1\text{ (pairing cut)}+(n-2)\text{ (descent)}\le n-1$.

For $n=2$ (§II.2), the bound is $1=n-1$. For $n\ge 3$, the bound is $\le n-1$. In all cases Mulan wins in $\le n-1$ moves, finite.

---

### III. Conclusion

Combining parts I and II:

- ($\Rightarrow$, §I) If $\theta\ne 180^\circ/n$ for every integer $n\ge 2$, Shan-Yu opens with the equilateral triangle (which is $\theta$-safe) and, by the four-coset closure lemma, maintains a $\theta$-safe child after every Mulan cut, so no angle ever equals $\theta$ and Mulan never wins. Hence Mulan **cannot** guarantee victory.
- ($\Leftarrow$, §II) If $\theta=180^\circ/n$ for some $n\ge 2$, Mulan wins: for $n=2$ by the $90^\circ$-trick (one move), for $n\ge 3$ by the deficit-pairing cut (one move to reach a marked state) followed by the halving descent ($\le n-2$ moves). Total $\le n-1$ moves.

Therefore Mulan can guarantee her victory in finitely many steps, no matter how Shan-Yu plays, **if and only if $\theta=180^\circ/n$ for some integer $n\ge 2$**. ∎

---

## Promotable lemmas

1. **Cut-geometry lemma** — Statement and proof in §0. Cutting at vertex $A$ (angle $A$) with parameter $\alpha\in(0,A)$ gives children $(\alpha,B,180^\circ-B-\alpha)$ and $(A-\alpha,C,B+\alpha)$; every $\alpha\in(0,A)$ is realizable by IVT. (Reusable by any approach; proved from scratch here.)
2. **Four-coset closure lemma (safe triangles cannot split into two marked children)** — Statement and proof in §I.1. If $180^\circ\notin\theta\mathbb Z$ and a state is $\theta$-safe, no cut makes both children $\theta$-marked; proved by exhaustive four-way coset-intersection analysis. (Reusable for any necessity direction; proved from scratch here.)
3. **Halving / $k$-descent lemma** — Statement and proof in §II.1. An angle equal to $k\theta$ ($k\ge 1$) is a $\le k-1$-move win, by strong induction cutting at that vertex with $\alpha=\theta$. (Reusable by any sufficiency approach.)
4. **Deficit-sum lemma** — Statement and proof in §II.4. For $\theta=180^\circ/n$, $n\ge 3$, if $a+b+c=180^\circ$ and no angle is a multiple of $\theta$, then $d(a)+d(b)+d(c)\in\{\theta,2\theta\}$ where $d(x)=\lceil x/\theta\rceil\theta-x$ (with the convention $m_x=\min\{m:m\theta\ge x\}$).
5. **Pairing lemma (refined)** — Statement and proof in §II.5. Under the hypotheses of the deficit-sum lemma ($n\ge 3$), there exist distinct angles $u,v$ with $d(u)<v$ **and** $m_u\le n-1$. Proof splits on whether a "top" angle ($m=n$, i.e. in $(180^\circ-\theta,180^\circ)$) exists: at most one does ($\theta\le 60^\circ$ for $n\ge 3$, so two top angles would sum $>240^\circ$); the no-top case is the cyclic-sum contradiction, the one-top case uses $a+b<\theta$ forcing $a,b<\theta$ and a second contradiction from $a,b\ge 180^\circ-\theta$.
6. **Pairing cut (one-move entry into the marked set)** — Statement and proof in §II.6. For $n\ge 3$, cutting at vertex $v$ with $\alpha=d(u)<v$ (from the refined pairing) makes both children contain a *positive* multiple of $\theta$ (namely $m_u\theta$ and $(n-m_u)\theta$, the latter positive because $m_u\le n-1$).
7. **$n=2$ ($\theta=90^\circ$) one-move trick** — Statement and proof in §II.2. From any triangle with no angle equal to $90^\circ$ (so at least two acute angles $B,C<90^\circ$, third angle $A=180^\circ-B-C\ne 90^\circ$), cut at the vertex with angle $A$, parameter $\alpha=90^\circ-B$ (legal since $0<90^\circ-B<A\iff C<90^\circ$); both children contain $90^\circ=\theta$.
