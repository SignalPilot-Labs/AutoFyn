# Round 6 proof-reviewer report — imo-2026-03

## Headline

`rank-tie-vertex-reduction`'s claimed closure of $(\star\star)$ via the
**Half-Window Vanishing Lemma** is **CONFIRMED CORRECT, and correctly
scoped** — no hidden gap found. This is genuine, verified progress that
breaks the 4+-round shared-gap plateau, but only for the precisely delimited
sub-case **$c_1=1$ (exactly one cut on $p_1$)**, against an arbitrary legal
tail refinement. The approach's own §5.4 honestly flags $c_1\ge2$ and the
full vertex enumeration as still open — this scoping is accurate, not an
overclaim.

## Verification of the Half-Window Vanishing Lemma (line-by-line + independent computation)

Re-derived independently:
- Ladder identity $p_1 = 2p_2$ holds exactly ($p_i = 2^{n+1-i}/D$).
- Window $W = [p_1-x, x)$ for a single cut at $x\in[p_1/2,p_1)$ is, by
  elementary algebra, always centered at $p_1/2$ regardless of $x$ — the
  ladder identity's role is only that this center equals $p_2$, the
  tail's own maximum possible fragment value.
- **Right half vanishes**: every fragment of any legal tail refinement is
  $\le$ its parent piece $\le p_2$ (ladder decreasing), so for $t\ge p_2$,
  $N_{G'}(t)=0$ (even) $\Rightarrow v(t)=0$. This is airtight — a direct
  consequence of "a positive sum of $\ge2$ positive terms has every term
  less than the total," applied piece by piece.
- **Left half**: bounded trivially by $v\le 1$, length $\Delta/2$.
- Sum: $\int_{W\cap[0,r)} v \le 0 + \Delta/2$, exactly $(\star\star)$.

I wrote an independent Python script (exact `fractions.Fraction`, no
floating point) generating random legal tail refinements (random cut counts,
random rational cut positions) for $n=2,\dots,6$, 400 trials each (2000
total), directly computing the window integral via breakpoint decomposition
and comparing to $\Delta/2$: **zero violations**. This corroborates the hand
proof independently of the approach's own verification script.

**Scoping check (the specific risk flagged in the assignment):** the proof
uses $F=\{x,p_1-x\}$ — exactly two fragments of $p_1$ — throughout (window
formula, Cross-Term Reduction Theorem). It does **not** claim to cover
$c_1\ge2$ (more than one cut on $p_1$, producing $\ge3$ fragments), and the
approach file explicitly says so in §5.4 ("the round-5 explorer's exhaustive
$n=3,4$ search found every such vertex degenerates to $c_1\le1$ via a
zero-length fragment, but no proof that this must always happen for
$c_1\ge2$ was attempted here"). No overclaim detected — the write-up is
careful to distinguish "closes $(\star\star)$" (true, for $c_1=1$) from
"closes the general lower bound" (not claimed).

**Conclusion:** the Half-Window Vanishing Lemma and the resulting
$(\star\star)$ theorem are correct, complete, and honestly scoped. This is
real, verified plateau-breaking progress — the first round since the
plateau was declared (rounds 2–5) that any approach has fully closed a piece
of the shared obstruction rather than further reducing or reformulating it.

## Per-slug verdicts

### rank-tie-vertex-reduction — CHANGES REQUESTED
Vertex-Minimum Theorem and Odd-Run Reduction Lemma (round 3, already
certified) remain sound and are reused correctly. The Cross-Term Reduction
Theorem (round 5, already certified) and the new Half-Window Vanishing
Lemma / $(\star\star)$ closure (round 6) are correct as verified above. The
approach fully closes the "single cut on $p_1$, arbitrary tail refinement"
domination case for every $n\ge2$ — a complete, non-numeric, general-$n$
result. Remaining gaps, honestly stated: general $c_1\ge2$, the full
tie-vertex enumeration, and the general upper bound. Recommend promoting
`half-window-vanishing-lemma` to `lemmas/`.

### rank-pigeonhole-budget — CHANGES REQUESTED
Achievability half of Claim (A) (§2): checked the cancellation argument by
hand, correct (each of $p_2,\dots,p_n$ appears exactly twice — contributes
0 — and $p_{n+1}$ appears exactly three times at an odd starting rank,
contributing $+p_{n+1}=a_n$). Case II (Theorem GC($m$), §3): re-verified the
strong induction by hand (base case $m=1$ via median argument is correct;
inductive step's peel via `sharp-dominant-removal-identity` and the general
rank-shift identity is correctly derived) and by an independent 20000-trial
exact-`Fraction` simulation of the theorem statement directly (not reusing
the approach's own script): zero violations. This is a genuine, unconditional,
general-$n$ closure of Case II, correctly superseding round 5's
numerics-only status. Case I is honestly left open and precisely diagnosed
(reduces to an inequality (4.1) requiring an upper bound on $A$ of a smaller
instance — correctly identified as equivalent in kind to the project's
central obstruction, not a simpler residual). No hand-waving found. Recommend
promoting `case-ii-closure-theorem` to `lemmas/` after the outline-reviewer's
own pass.

### lp-duality-certificate — CHANGES REQUESTED
Step 2 (complete $n=2$ certificate, 17 leaf cells): spot-checked several
cells by hand against the already-certified `n2-lower-bound-full-closure`
case analysis — consistent, no errors found in the $\lambda$-combinations
shown. Step 3 test (one $n=3$ composition, $(1,1,0,0)$): the three numeric
cross-checks shown (at $a=b=4,c=3,d=1$; $a=4.2,\dots$; $a=4.5,\dots$) are
arithmetically correct as computed. This is genuine but narrow progress —
only one composition, no genuine simultaneous multi-way tie tested, and (as
the approach itself honestly flags) it is not established that this
framing structurally avoids re-encountering $(\star\star)$'s content in new
notation. No overclaim; Status `partial` is correct.

### integer-lattice-reduction — RETHINK
Both negative results were checked and are correct: (1) the $4/21$
counterexample to "denominator divides $D$" is arithmetically valid ($p_1=
4/7$ split into three equal $4/21$ fragments via two independent tie
constraints, a genuine vertex per `vertex-minimum-theorem`; $21\nmid 7$).
(2) The bisection non-invariance counterexample ($n=4$, window integral
moving $5/31\to7/31$ upon bisecting $p_3$) is a real effect, not a
computational artifact — bisecting a piece changes $N_{G'}(t)$'s value from
1 to 2 in the band it used to solely occupy, which is an even change in
count but can still interact with neighboring parity in a way that increases
the integral; the approach's diagnosis of *why* the naive claim fails is
sound. The core mechanism (digit/carry model transplanted from crux corpus)
has now failed at two independent, load-bearing points. The two positive
lemmas (Rationality Lemma R1, repaired $D\cdot L$ bound R2) are correct and
reusable but do not by themselves make progress on $(\star\star)$ or its
generalizations. Recommend the approach be re-planned rather than continued
in its current form — hence RETHINK, matching the file's own `unsolved`
status and its own recommendation against further iteration on this
mechanism.

### bijective-mersenne-pairing — RETHINK
The falsifying computation (Step 1c, composition $(2,0,0)$, $p_1\to\{3,
7/10,3/10\}$) was independently re-verified by hand: $A(S)=3-2+1-0.7+0.3=
1.6=8/5$, exact match. The diagnosis (the $2{:}1$ ratio is a property of the
cascading-halving family's construction, not of the functional $A$ or of
generic legal responses) is correct and the approach was abandoned per its
own pre-declared stop condition after failing the outline's own required
generic test. Correctly recorded as a dead end; RETHINK matches the file's
own `unsolved` status.

## current.md updated

Updated `results/imo-2026-03/current.md`:
- Added a full Round 6 entry under "Approaches tried" summarizing all 5
  slugs' outcomes, with explicit note that $(\star\star)$ is closed **only**
  for $c_1=1$.
- Added three new bullets to "Current best" reflecting: (1) the verified
  $(\star\star)$/$c_1=1$ closure, (2) the verified Case II closure
  (`case-ii-closure-theorem`), (3) the two confirmed dead ends.
- Status remains `partial` (correct — the general lower bound, general
  upper bound, and full vertex enumeration are all still open; this round's
  results are real but narrower than a full solve).

## Ranker outcomes recorded

- `rank-tie-vertex-reduction`: verified-milestone
- `rank-pigeonhole-budget`: verified-milestone
- `lp-duality-certificate`: partial
- `integer-lattice-reduction`: dead-end
- `bijective-mersenne-pairing`: dead-end

## Recommendation for round 7

The natural next targets, per both approaches' own honest scoping:
1. **General $c_1\ge2$**: extend the Half-Window Vanishing mechanism to
   $\ge3$ simultaneous fragments of $p_1$ — the window/midpoint structure
   needs to be redone from scratch (flagged, not attempted, by
   `rank-tie-vertex-reduction`).
2. **Case I of Claim (A)** (`rank-pigeonhole-budget`): needs an upper bound
   on $A$ of a smaller self-similar instance — try importing whichever of
   `lp-duality-certificate` (LP duality is naturally two-sided) or a
   revived, re-planned lattice/counting approach can supply one.
3. **Full vertex enumeration** beyond single-cut-on-$p_1$ (e.g. multiple
   simultaneous tail cuts with no cut on $p_1$) and **the general upper
   bound** (untouched by any approach so far) remain the deepest open items.
