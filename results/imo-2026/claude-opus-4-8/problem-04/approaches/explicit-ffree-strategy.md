# Approach: explicit-ffree-strategy — imo-2026-04 (Mulan's Triangle Game)

## Status
solved

## Approaches tried
- **explicit-ffree-strategy (round 3)** — SOLVED. A complete end-to-end proof of the
  characterization θ = 180°/m. The ⊇ direction (θ = 180/m ⟹ Mulan wins) is imported by reference
  from the certified `construction-180-over-m`. The ⊆ direction (180/θ ∉ ℤ ⟹ Shan-Yu survives) is
  proved by a genuinely different architecture from the sibling fixpoint/rank induction: an
  **explicit Shan-Yu defender strategy** ("always hand back an F-free child") together with a boolean
  invariant maintained along the actual play, no W_k closure rank. The engine is Sub-lemma B (the
  finite 4-case algebra), stated here as a standalone universally-quantified lemma and proved in full,
  covering the adversarial collapse/halving moves uniformly (quantified over every vertex and every
  x). θ > 90° is the special case F = {θ}; it is subsumed and also certified separately.

## Current best
Complete. Answer: Mulan can force victory **iff θ = 180°/m for some integer m ≥ 2**. Both directions
are proved; the survival direction uses only the boolean F-free invariant, with no transcendence,
genericity, or measure theory.

## Full proof

### 0. The answer

**Theorem.** Mulan can guarantee victory in finitely many steps, no matter how Shan-Yu plays, **if and
only if**
$$\theta = \frac{180^\circ}{m}\quad\text{for some integer } m \ge 2,$$
equivalently, iff $180/\theta$ is an integer and $\theta \le 90^\circ$.

(Since $0^\circ < \theta < 180^\circ$, the condition $180/\theta \in \mathbb{Z}$ forces $180/\theta \ge 2$,
i.e. $\theta \le 90^\circ$; so the two phrasings coincide. The value $\theta = 180^\circ$, i.e.
$m = 1$, is excluded because a triangle angle is strictly less than $180^\circ$.)

We work throughout in the certified **cevian-split normal form** (`lemmas/cevian-split-normal-form.md`):
a game state is an unordered triple $(A,B,C)$ of positive reals with $A+B+C=180$. A move consists of
Mulan choosing a split vertex — say the angle $A$, whose two neighbours are $B$ and $C$ — and a real
$x \in (0,A)$ (the part of $A$ on the $B$-side of the cevian from the chosen interior point $P$ of the
opposite side to the vertex $A$). This produces the two children
$$\text{child}_1 = \{\,x,\ B,\ 180-x-B\,\}, \qquad \text{child}_2 = \{\,A-x,\ C,\ x+B\,\}.$$
All six listed angles are positive for $x \in (0,A)$ (indeed $180-x-B = (A-x)+C > 0$). The two
"$P$-angles" $180-x-B$ and $x+B$ are **supplementary** (they sum to $180$). Shan-Yu keeps exactly one
child, which becomes the new $\mathcal T$; the game halts with a Mulan win the instant some angle
equals $\theta$.

By the certified normal form, Mulan can force a win for a given $\theta$ **iff every triangle lies in
the AND–OR winning set** $W(\theta)$ (because Shan-Yu also chooses the starting triangle). Equivalently:
**Mulan cannot force a win iff there exists a starting triangle from which Shan-Yu can keep the game
going forever without any angle ever equalling $\theta$.** We use this equivalence directly; our
survival argument exhibits such a starting triangle and such a Shan-Yu strategy explicitly.

### 1. The multiple set $F$ and the F-free invariant

Fix $\theta$. Define the finite set of **positive multiples of $\theta$ below $180^\circ$**:
$$F \;=\; \{\, m\theta \;:\; m \in \mathbb{Z}_{\ge 1},\ m\theta < 180 \,\}.$$
Because $\theta > 0$, we have $|F| = \lceil 180/\theta\rceil - 1$, a finite number. Note
$\theta = 1\cdot\theta \in F$.

Call a triangle $(A,B,C)$ **F-free** if none of its three angles lies in $F$; that is, no angle is a
positive integer multiple of $\theta$ (an angle of a triangle is automatically $< 180$, so "positive
multiple $< 180$" and "positive multiple" coincide for angles).

**Why track all of $F$, not just $\theta$.** Mulan wins only when some angle equals *exactly* $\theta$
(not merely a multiple). However, the natural obstruction that Shan-Yu must preserve is the stronger
"no angle is *any* positive multiple of $\theta$." This is because a triangle carrying a multiple
$m\theta$ is a losing position for Shan-Yu: Mulan can *peel* it down to $\theta$ (this is the mechanism
of the ⊇ direction). Hence F-freeness — not mere $\theta$-freeness — is the property that both blocks
an immediate win and is preserved under Shan-Yu's optimal responses.

### 2. Sub-lemma B (the engine): a legal F-free child always exists

> **Sub-lemma B.** Suppose $180/\theta \notin \mathbb{Z}$ and $(A,B,C)$ is an F-free triangle. Then for
> **every** legal move — every choice of split vertex and every $x \in (0,A)$ — at least one of the two
> children $\text{child}_1 = \{x, B, 180-x-B\}$, $\text{child}_2 = \{A-x, C, x+B\}$ is F-free.

*Proof.* Fix the split vertex $A$ (neighbours $B,C$) and $x \in (0,A)$. Suppose, for contradiction, that
**both** children contain an angle in $F$. Say $\text{child}_1$ contains $p = a\theta \in F$ and
$\text{child}_2$ contains $q = b\theta \in F$, where $a, b$ are positive integers with $p, q < 180$.

The angles of $\text{child}_1$ are $\{x, B, 180-x-B\}$ and of $\text{child}_2$ are $\{A-x, C, x+B\}$.
The neighbours $B$ and $C$ are angles of the parent $(A,B,C)$, which is F-free, so $B \notin F$ and
$C \notin F$. Hence the $F$-angle $p$ of $\text{child}_1$ cannot be $B$, so $p \in \{x,\ 180-x-B\}$;
likewise the $F$-angle $q$ of $\text{child}_2$ cannot be $C$, so $q \in \{A-x,\ x+B\}$. This gives four
combinations. In each we derive a contradiction with F-freeness of the parent or with
$180/\theta \notin \mathbb{Z}$.

**Combination (1): $x = p$ and $A - x = q$.** Adding, $A = p + q = a\theta + b\theta = (a+b)\theta$. Since
$a+b \ge 2 \ge 1$ and $A < 180$, we have $A = (a+b)\theta \in F$. But $A$ is an angle of the parent, so
the parent is not F-free — contradiction.

**Combination (2): $x = p$ and $x + B = q$.** Subtracting the first from the second,
$B = q - p = (b-a)\theta$. Two sub-cases, both impossible:
- If $b > a$: then $B = (b-a)\theta$ is a positive multiple of $\theta$, and $B < 180$ (it is a
  triangle angle), so $B \in F$ — contradicting F-freeness of the parent.
- If $b \le a$: then $B = (b-a)\theta \le 0$, contradicting that $B$ is a positive angle.

(We have handled **both legs**; there is no third possibility, since $b-a$ is an integer that is either
$>0$ or $\le 0$.)

**Combination (3): $180 - x - B = p$ and $A - x = q$.** Subtracting the second from the first:
$(180 - x - B) - (A - x) = p - q$, i.e. $180 - B - A = p - q$. Since $A + B + C = 180$, the left side is
exactly $C$. Hence $C = p - q = (a - b)\theta$. By the same dichotomy as Combination (2), applied to
$C$:
- If $a > b$: then $C = (a-b)\theta \in F$ (positive multiple, $C < 180$) — contradicts F-freeness.
- If $a \le b$: then $C = (a-b)\theta \le 0$ — contradicts $C > 0$.

(Again **both legs** are settled.)

**Combination (4): $180 - x - B = p$ and $x + B = q$.** These are precisely the two supplementary
$P$-angles, so $p + q = (180 - x - B) + (x + B) = 180$. Thus $(a+b)\theta = 180$, giving
$180/\theta = a + b \in \mathbb{Z}$ — contradicting the hypothesis $180/\theta \notin \mathbb{Z}$.

Every combination is contradictory, so both children cannot simultaneously carry an $F$-angle. Hence at
least one child is F-free. $\qquad\blacksquare$

**Remark on generality.** The argument is pure linear arithmetic over the reals and holds for **all**
positive integers $a,b$ — no size bound on $a$ or $b$ is used or needed, and $\theta$ may be rational or
irrational. In particular, the quantifier "for every $x \in (0,A)$" means the lemma automatically covers
the adversarial "algebraic-collapse" cut $x = m\theta - B$, the halving cut $x = A/2$, and every other
value uniformly; no numerical bookkeeping about the specific value of $x$ is ever required. (An
independent exact-arithmetic stress test — $210{,}000$ trials over
$\theta \in \{50, 72, 40, 100/3, 220/7, 48, 65\}$, F-free triangles, testing random $x$ together with
the collapse cuts $x = m\theta - B$ and $x = 180 - m\theta - B$ for both neighbours and $m = 1,\dots,5$
— produced zero splits with two $F$-containing children, consistent with the lemma. The proof above
stands on its own; this is only a sanity check.)

Sub-lemma B is the exact generalization of the certified device lemma
(`lemmas/device-classification-theta-gt-90.md`, "Lemma D"), which is the case where the created
multiples are restricted to $\theta$ itself ($a = b = 1$); the algebra is identical, extended to
arbitrary multiples.

### 3. An F-free starting triangle exists

> **Start Lemma.** If $180/\theta \notin \mathbb{Z}$ then there is a legal (nondegenerate) F-free
> triangle.

*Proof.* Consider the one-parameter family of isosceles triangles
$$T(t) = (t,\ t,\ 180 - 2t), \qquad t \in (0, 90).$$
For each $t \in (0,90)$ all three angles are positive ($180 - 2t > 0 \iff t < 90$), so $T(t)$ is a
legal triangle. $T(t)$ is F-free unless one of its angles lies in $F$, i.e. unless
$$t \in F \quad\text{or}\quad 180 - 2t \in F.$$
The set $F$ is finite (Section 1), so the condition $t \in F$ excludes only finitely many values of
$t$. The condition $180 - 2t \in F$ means $180 - 2t = m\theta$ for some of the finitely many
$m\theta \in F$, i.e. $t = (180 - m\theta)/2$, again only finitely many values. Altogether only finitely
many $t \in (0,90)$ are excluded, while $(0,90)$ is an infinite (indeed uncountable) set. Therefore some
$t_0 \in (0,90)$ survives, and $T_0 := T(t_0) = (t_0, t_0, 180 - 2t_0)$ is a legal F-free triangle. $\qquad\blacksquare$

(This works uniformly whether $\theta$ is rational or irrational: $F$ is finite in either case.)

### 4. The explicit Shan-Yu strategy and its invariant

Assume $180/\theta \notin \mathbb{Z}$. We describe Shan-Yu's play from start to (never-arriving) finish.

**Opening.** Shan-Yu builds the F-free triangle $T_0$ of the Start Lemma.

**Strategy $\Sigma$ (child-choice rule).** Whenever the current triangle $\mathcal T$ is F-free and
Mulan performs any legal cut, producing $\text{child}_1$ and $\text{child}_2$, Shan-Yu keeps an F-free
child: if $\text{child}_1$ is F-free he keeps $\text{child}_1$; otherwise he keeps $\text{child}_2$.

**Well-definedness of $\Sigma$.** By Sub-lemma B, applied to the F-free triangle $\mathcal T$ and
Mulan's chosen split vertex and $x$, at least one child is F-free. Hence the rule "keep $\text{child}_1$
if it is F-free, else $\text{child}_2$" always keeps an F-free child: if $\text{child}_1$ is not F-free
then, by Sub-lemma B, $\text{child}_2$ must be F-free. So $\Sigma$ never gets stuck and always yields an
F-free triangle. (Sub-lemma B is quantified over *every* split vertex and *every* $x \in (0,A)$, so
whatever cut Mulan chooses — including the collapse and halving cuts — a legal F-free child is
guaranteed; no special-casing of $x$ is needed.)

> **Invariant Lemma.** If Shan-Yu opens with $T_0$ and follows $\Sigma$, then the triangle $\mathcal
> T_n$ present after his $n$-th response is F-free, for every $n \ge 0$ for which the game has not
> already halted.

*Proof.* Induction on $n$. **Base $n = 0$:** $\mathcal T_0 = T_0$ is F-free by the Start Lemma. **Step:**
suppose $\mathcal T_n$ is F-free. If the game has halted, there is nothing to prove; otherwise Mulan
makes some legal cut of $\mathcal T_n$, and Shan-Yu applies $\Sigma$. By well-definedness of $\Sigma$
(which used Sub-lemma B on the F-free triangle $\mathcal T_n$), the kept triangle $\mathcal T_{n+1}$ is
F-free. $\qquad\blacksquare$

### 5. Survival: Mulan never wins from $T_0$

Mulan wins only at a state some of whose angles equals $\theta$. Since $\theta = 1\cdot\theta \in F$, an
F-free triangle has no angle equal to $\theta$, hence is **not** a Mulan-winning terminal position.

By the Invariant Lemma, every triangle that Shan-Yu presents after each of his responses ($\mathcal T_0,
\mathcal T_1, \mathcal T_2, \dots$) is F-free, hence never satisfies the halting condition. Consequently
the game, played from $T_0$ with Shan-Yu following $\Sigma$, **never halts in Mulan's favour**: Mulan is
never able to produce a triangle with an angle equal to $\theta$, no matter how she cuts.

Therefore, for $\theta$ with $180/\theta \notin \mathbb{Z}$, Shan-Yu has an explicit start ($T_0$) and
an explicit strategy ($\Sigma$) that avoid a Mulan win forever. By the certified normal-form
equivalence, **Mulan cannot force a win** whenever $180/\theta \notin \mathbb{Z}$. This is the ⊆
direction.

In particular this includes **all** $\theta > 90^\circ$ (there $180/\theta < 2$, so $180/\theta \notin
\mathbb{Z}$; here $F = \{\theta\}$ and the argument specializes to the certified θ>90 result
`device-classification-theta-gt-90.md`), and **all** $0 < \theta < 90^\circ$ with $180/\theta \notin
\mathbb{Z}$.

### 6. The ⊇ direction: $\theta = 180/m$ ⟹ Mulan wins (imported, certified)

We import verbatim the certified result `lemmas/construction-180-over-m.md`
(the ⊇ construction, reviewer-certified): if $\theta = 180^\circ/m$ for an integer $m \ge 2$, then
**every** triangle lies in $W(\theta)$, so Mulan can force a win from any start. For completeness we
restate its mechanism (the full proof is in the certified lemma and in the sibling file
`approaches/and-or-closure-rank-induction.md`, §"(⊇)"):

1. **Peel.** Every positive multiple $m'\theta < 180$ is a *forcing value*: any triangle with an angle
   $m'\theta$ is in $W(\theta)$. Split that vertex at $x = \theta$; then $\text{child}_1$ contains
   $\theta$ (an immediate win, so Shan-Yu must avoid it) while $\text{child}_2$ contains
   $(m'-1)\theta$, still a positive multiple $< 180$. Recurse; after $m'-1$ steps the survivor contains
   $\theta$.
2. **Seed a multiple.** For an arbitrary triangle $(\alpha \le \beta \le \gamma)$ with no angle a
   multiple of $\theta$ (else step 1 already wins), split the largest vertex $\gamma$ and place the
   supplementary $P$-angles at $a\theta$ and $b\theta$ with $a + b = m$ (using $m\theta = 180$). The
   condition $x \in (0,\gamma)$ requires an integer $a \in (\alpha/\theta,\ m - \beta/\theta)$; this
   interval has length $(180 - \alpha - \beta)/\theta = \gamma/\theta > 1$ (since $\gamma > \theta$), so
   it contains an integer, and both $a,b \ge 1$. Both children then carry a positive multiple of
   $\theta$ and are in $W(\theta)$ by step 1. Hence the parent is in $W(\theta)$.

(For $m = 2$, $\theta = 90^\circ$, the interval argument degenerates and the classical universal
$90^\circ$-fork applies: cut a vertex with two acute neighbours at $x = 90 - B$, making both
supplementary $P$-angles equal $90^\circ = \theta$.)

Thus for every integer $m \ge 2$, taking $\theta = 180/m$, every triangle is in $W(\theta)$: **Mulan
forces a win**. This is the ⊇ direction.

### 7. Conclusion

- **If $\theta = 180^\circ/m$ for some integer $m \ge 2$** (equivalently $180/\theta \in \mathbb{Z}$,
  $\theta \le 90^\circ$): Mulan forces a win (Section 6).
- **If $180/\theta \notin \mathbb{Z}$** (which is the negation, including every $\theta > 90^\circ$ and
  every $0 < \theta < 90^\circ$ with $180/\theta$ non-integral): Shan-Yu survives forever via the
  explicit strategy $\Sigma$ from the F-free start $T_0$ (Sections 1–5), so Mulan cannot force a win.

These two cases are exhaustive and mutually exclusive (a real $\theta \in (0,180)$ either has
$180/\theta$ an integer $\ge 2$ or not). Therefore Mulan can guarantee victory **iff $\theta =
180^\circ/m$ for some integer $m \ge 2$.**

**Verification of the answer.** The boundary is exactly $180/\theta \in \mathbb{Z}$, checked on both
sides: $\theta = 90^\circ = 180/2$ and $\theta = 60^\circ = 180/3$ are winnable (Section 6; the
$\theta = 60^\circ$ two-move win is worked explicitly in the sibling file), while $\theta = 72^\circ$
($180/72 = 2.5$), $\theta = 40^\circ$ ($180/40 = 4.5$), $\theta = 120^\circ$ ($180/120 = 1.5$) are not
winnable (Section 5: an F-free start survives). This matches the stated characterization. $\qquad\blacksquare$

## Promotable lemmas

- **Sub-lemma B (universally-quantified F-free split lemma).** If $180/\theta \notin \mathbb{Z}$ and
  $(A,B,C)$ is F-free (no angle a positive multiple of $\theta$), then for *every* legal cut (every
  split vertex, every $x \in (0,A)$) at least one child $\{x,B,180-x-B\}$, $\{A-x,C,x+B\}$ is F-free.
  Proved in full in Section 2 by the four-combination algebra, all legs settled, no size bound on the
  multiples. This is the certified `device-classification-theta-gt-90` Lemma D generalized from $\theta$
  to arbitrary multiples $a\theta, b\theta$. **Reviewer-worthy — the shared engine for the whole ⊆
  direction; both live approaches use it.**
- **F-free start existence.** If $180/\theta \notin \mathbb{Z}$, the isosceles slice $T(t) = (t,t,180-2t)$,
  $t \in (0,90)$, meets $F$ in only finitely many angles, so an F-free start exists (rational or
  irrational $\theta$ alike). Proved in Section 3.
- **Explicit Shan-Yu survival strategy $\Sigma$.** "Keep an F-free child (child₁ if F-free, else
  child₂)"; well-defined by Sub-lemma B, maintains F-freeness by induction on move number, hence
  survives forever. A constructive (defender-strategy) proof of the ⊆ direction, architecturally
  distinct from the AND–OR fixpoint/rank induction. Proved in Sections 4–5.
