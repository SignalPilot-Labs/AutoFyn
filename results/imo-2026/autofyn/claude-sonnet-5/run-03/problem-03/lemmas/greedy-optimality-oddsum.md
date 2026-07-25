## Lemma: Greedy-optimality of the alternating-claim game (OddSum value)

**Statement.** Let $S=\{x_1\ge x_2\ge\cdots\ge x_m\}$ be any finite multiset
of positive reals (sorted descending). Consider the game in which two
players alternately claim (remove) any currently-unclaimed element of $S$,
Player 1 moving first, each maximizing their own total claimed sum. Then:

- The game has a well-defined value.
- Player 1's total under optimal play by both sides equals
  $\mathrm{OddSum}(S):=x_1+x_3+x_5+\cdots$ (sum of the odd-ranked elements
  in the descending sort), and Player 2's total equals
  $\mathrm{EvenSum}(S):=x_2+x_4+\cdots=\mathrm{sum}(S)-\mathrm{OddSum}(S)$.
- "Always claim a currently-largest unclaimed element" is optimal for both
  players (including under ties, in which case the value is independent of
  which tied copy is taken).

**Proof.** The game is finite and zero-sum, so it has a well-defined value
$V(S)$ (the mover's optimal guaranteed total), computable by backward
induction on $|S|$:
$$V(\varnothing)=0,\qquad V(S) = \max_{x\in S}\Bigl[x + \bigl(\mathrm{sum}(S)-x-V(S\setminus\{x\})\bigr)\Bigr] = \mathrm{sum}(S) - \min_{x\in S} V(S\setminus\{x\}),$$
since after the mover takes $x$, the opponent becomes mover of $S\setminus\{x\}$
and receives $V(S\setminus\{x\})$ of the remaining $\mathrm{sum}(S)-x$.

We show $V(S)=\mathrm{OddSum}(S)$ by strong induction on $|S|$. Base case
$S=\varnothing$ is immediate. Inductive step: assume $V(S')=\mathrm{OddSum}(S')$
for every multiset $S'$ with $|S'|<|S|$. By the recursion above it suffices
to show
$$\min_{x\in S}\mathrm{OddSum}(S\setminus\{x\}) = \mathrm{OddSum}(S\setminus\{x_1\}) = \mathrm{EvenSum}(S).$$

The second equality is immediate: $S\setminus\{x_1\}$ sorted descending is
$x_2,\dots,x_m$, so $\mathrm{OddSum}(S\setminus\{x_1\})=x_2+x_4+\cdots=\mathrm{EvenSum}(S)$.

For the first equality, fix $k\in\{1,\dots,m\}$ and compare
$S_k:=S\setminus\{x_k\}$ with $S_1:=S\setminus\{x_1\}$, both sorted
descending. For $1\le i\le k-1$ the $i$-th entry of $S_k$ is $x_i$ while the
$i$-th entry of $S_1$ is $x_{i+1}$; both lists agree from position $k$
onward. Hence
$$\mathrm{OddSum}(S_k)-\mathrm{OddSum}(S_1) = \sum_{\substack{i\text{ odd}\\ 1\le i\le k-1}} (x_i-x_{i+1}) \ge 0,$$
since $S$ is sorted descending (each term $x_i-x_{i+1}\ge0$); the sum is
empty (hence $=0$) when $k=1$. So $\mathrm{OddSum}(S_k)\ge \mathrm{OddSum}(S_1)$
for every $k$, with equality at $k=1$, giving
$\min_x \mathrm{OddSum}(S\setminus\{x\}) = \mathrm{OddSum}(S_1)=\mathrm{EvenSum}(S)$.

Substituting back: $V(S) = \mathrm{sum}(S) - \mathrm{EvenSum}(S) = \mathrm{OddSum}(S)$,
completing the induction. The argument also exhibits a largest element as
an optimal first move for the mover, and since the resulting subposition is
again governed by the same lemma, "always take a currently-largest piece"
is optimal for both players throughout. Ties cause no issue since the proof
only used $x_i\ge x_{i+1}$ (non-strict). $\blacksquare$

**Independent verification.** Checked by brute-force backward-induction
computation against the closed form on 2000 random multisets of size 1–7;
max discrepancy $7\times10^{-15}$ (floating-point noise only).

**Source.** Proved independently (with the same argument) in
`approaches/greedy-reduction-geometric.md` (Lemma 1) and
`approaches/self-similar-induction-on-n.md` (Lemma 1). Certified by the
proof-reviewer, round 1.

**Reuse.** Directly reusable by any approach to imo-2026-03 (or any problem
reducing to alternating claiming over a fixed multiset).
