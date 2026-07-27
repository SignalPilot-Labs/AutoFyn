Bottom line: I could not produce a complete, rigorous solution. Here's exactly what I have.

  Setup (rigorous)

  The game reduces to a purely angle-combinatorial game: a state is a triple of positive angles $(A,B,C)$, $A+B+C=180°$. A move picks one angle (say $A$, with the other two $B,C$) and a real $x\in(0,A)$, producing two candidate
  triangles
  $${x,,B,,180-B-x} \quad\text{and}\quad {A-x,,C,,B+x},$$
  and Shan-Yu keeps whichever he prefers. Mulan wins iff she can force some angle to equal $\theta$ in finitely many moves.

  What I proved

  1. If $\theta=90°$: Mulan wins in one move, always. (Split any angle at its altitude foot — some altitude foot is always interior — giving both children a $90°$ angle at $P$ simultaneously, since $90°$ is self-supplementary.)

  2. If some current angle equals $2\theta$: Mulan wins in one move (bisect it; both halves are $\theta$).

  3. (Peeling lemma) If some current angle equals $j\theta$ for a positive integer $j$ (with $j\theta<180°$): Mulan wins in at most $j-1$ more moves — repeatedly split off exactly $\theta$ from that angle; whichever piece Shan-Yu
  is forced to keep still carries a smaller multiple of $\theta$, until $j=1$.

  4. For $\theta = 180°/n$, any integer $n\ge 3$: I found a universal one-move construction — split the largest angle $r$, with middle angle $q$ and smallest angle $p$ as the other two. A pigeonhole argument (an open interval of
  length $r/\theta>1$, which holds since $r\ge 60°>\theta$ for $n\ge3$, must contain an integer) guarantees an integer $k\in{1,\dots,n-1}$ and a valid $x$ such that one child gets angle exactly $k\theta$ and the other gets
  exactly $(n-k)\theta$ — regardless of the starting triangle. Combined with the peeling lemma, this gives a finite winning strategy for every $\theta=180°/n$, $n\ge2$ (with $n=2$, i.e. $\theta=90°$, covered separately by the
  altitude trick).

  So: Mulan wins whenever $\theta = 180°/n$ for an integer $n\ge2$ — this direction is solid.

  Where it broke down

  I could not establish the converse (that Mulan loses for every other $\theta$), which is needed for a complete answer. I tried to show Shan-Yu has a permanent "safe set" of triangles avoiding $\theta$ forever when $\theta\ne
  180°/n$.

  Concretely, for $\theta=50°$ (not of the form $180/n$), starting from $(80°,70°,30°)$, every peeling/multiple-targeting strategy I tried against an adversarial Shan-Yu cycled back through
  ${80,70,30}\to{20,80,80}\to{30,20,130}\to{30,30,120}\to{80,70,30}$ without ever reaching $50°$ or $100°$. That's evidence for a trap, not a proof — I only checked finitely many of Mulan's continuum of choices at each stage, not
  all of them, and never built an explicit invariant certifying the set is closed under Shan-Yu's escape.

  I also checked algebraically why the universal one-move construction genuinely requires $\theta=180/n$ exactly (writing $\theta=180a/b$ in lowest terms, the mechanism needs $a=1$), which is consistent with the conjecture but
  doesn't prove it.

  Honest conclusion

  My best-supported conjecture is
  $$\boxed{\theta = \frac{180°}{n},\ n=2,3,4,\dots}$$
  with the "if" direction rigorously proved above, but the "only if" direction unproved — I have one suggestive example (θ=50°) and no general argument. I don't want to hand you the converse as settled when it isn't.

  If you'd like, I can keep pushing specifically on constructing Shan-Yu's safe-set invariant for non-$180/n$ values (that's the one missing piece), rather than redoing everything above.


Time:

add those up
✻ Cogitated for 45m 25s
  Churned for 44m 47s
  ✻ Churned for 12m 31s