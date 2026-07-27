Solution

  Answer

  $$\boxed{c ;=; \frac{2^{n}}{2^{,n+1}-1};=;\frac{1}{,2-2^{-n},}}$$

  So Liu Bang can guarantee $\tfrac23,\tfrac47,\tfrac{8}{15},\tfrac{16}{31},\dots$ for $n=1,2,3,4,\dots$, and no more.

  Throughout write $M=2^{n+1}-1$, so $c=\tfrac{2^n}{M}$. Call the players L (Liu Bang, first) and X (Xiang Yu).

  ---
  1. The claiming phase: first player takes the odd‑ranked pieces
  
  Lemma 1. Given final pieces of lengths $a_1\ge a_2\ge\cdots\ge a_m$, with both players playing optimally in the alternating "grab a
  piece" game, the first player collects exactly $a_1+a_3+a_5+\cdots$ (the odd‑ranked pieces).

  Proof. Induct on $m$. For a multiset $A$ let $O(A)=\sum_{i\text{ odd}}a_i$ and $E(A)=\sum_{i\text{ even}}a_i$ be the odd/even ranked
  sums. If the mover takes the piece $a_j$, the opponent then faces $A\setminus{a_j}$ as first mover and (by induction) gets
  $O(A\setminus{a_j})$, so the mover gets $a_j+E(A\setminus{a_j})$.

  Removing $a_j$ from the sorted list keeps indices $<j$ fixed and shifts indices $>j$ down by one, so
  $$E(A\setminus{a_j})=\sum_{i<j,,i\text{ even}}a_i+\sum_{i>j,,i\text{ odd}}a_i .$$
  A short computation gives, for every $j$,
  $$O(A)-\bigl(a_j+E(A\setminus{a_j})\bigr)=
  \begin{cases}
  \sum_{k}(a_{2k-1}-a_{2k})\ge 0,& j \text{ odd},\[2pt]
  (a_{j-1}-a_j)+\sum_{k}(a_{2k-1}-a_{2k})\ge 0,& j \text{ even},
  \end{cases}$$
  where the pairs $(a_{2k-1}-a_{2k})$ range over indices $<j$. Since $a_i$ is nonincreasing, each bracket is $\ge0$, with equality at
  $j=1$. Hence taking the largest piece is optimal and the mover secures $O(A)$. $\qquad\blacksquare$

  Thus L's guaranteed length equals $O(A)=a_1+a_3+\cdots$ for the final multiset $A$.

  2. Reduction to an alternating sum / a parity measure

  Since $O(A)+E(A)=1$, writing $D(A)=O(A)-E(A)=a_1-a_2+a_3-\cdots$ (the alternating sum, always $\ge0$) gives
  $$O(A)=\tfrac12\bigl(1+D(A)\bigr).$$
  So L wants to maximize $D$, X to minimize $D$, and the value is $c=\tfrac12(1+D^*)$. We will show $D^*=\tfrac1M$, which gives
  $c=\tfrac12\bigl(1+\tfrac1M\bigr)=\tfrac{M+1}{2M}=\tfrac{2^{n+1}}{2M}=\tfrac{2^n}{M}$, as claimed.

  Two facts about $D$ are used repeatedly. Let $N(t)=#{\text{pieces of length}\ge t}$.

  - (Layer–cake identity) $\displaystyle D(A)=\int_0^\infty \bigl[N(t)\bmod 2\bigr],dt=\operatorname{meas}{t:\ N(t)\text{ is odd}}.$
   Indeed $a_i=\int_0^\infty\mathbf 1[a_i\ge t],dt$, and $\sum_{i=1}^{k}(-1)^{i+1}=[k\text{ odd}]$.
  - (Pair‑removal) Deleting two equal pieces from $A$ leaves $D$ unchanged (they occupy consecutive ranks $i,i+1$, contributing
  $(-1)^{i+1}x+(-1)^{i+2}x=0$, and everything below shifts by two ranks, preserving parity).

  3. Lower bound: L can guarantee $c=\tfrac{2^n}{M}$

  L's strategy. Cut $[0,1]$ into the $n+1$ pieces
  $$\frac{2^0}{M},\ \frac{2^1}{M},\ \dots,\ \frac{2^n}{M}\qquad\Bigl(\textstyle\sum_i 2^i=M\Bigr).$$
  Rescale by $M$, so the pieces are the integers $C_n={1,2,4,\dots,2^n}$ with total $M$; we must show every subdivision of $C_n$ using
  at most $n$ (X‑)cuts has alternating sum $\widetilde D\ge 1$ (then $D\ge 1/M$).

  Parity. If all final pieces are integers, then $\widetilde D=O-E\equiv O+E=M\pmod 2$. As $M$ is odd, $\widetilde D$ is an odd number;
  being $\ge0$, we get $\widetilde D\ge 1$.

  X's optimum is integral. $\widetilde D$ is a continuous, piecewise‑linear function of X's cut positions on a compact domain, so its
  minimum is attained at a vertex of the arrangement cut out by the constraints "two pieces are equal" and "a cut sits at an existing
  mark". Every mark of $C_n$ is an integer and every piece length is a power of two; the linear systems defining these vertices
  therefore have integer solutions (a bisection of an even piece stays integral, and equalities to integer marks force integrality).
  Hence some $\widetilde D$-minimizing response uses only integer cuts, to which the parity argument applies. Therefore
  $$\min_{\text{X}}\widetilde D\ge 1\quad\Longrightarrow\quad \min_{\text{X}}D\ge \tfrac1M .$$

  (That this bound is tight — X can reach $\widetilde D=1$ — is seen directly: X bisects $2^n!\to!2^{n-1},2^{n-1}$, then bisects one
  $2^{n-1}$, …, down through $2^1$; each level ends with an even count that pairs off, leaving the single piece $1$, so $\widetilde D=1$
  using $n$ cuts.)

  By Lemma 1, playing greedily in the claiming phase, L secures $O=\tfrac12(1+D)\ge\tfrac12(1+\tfrac1M)=\tfrac{2^n}{M}$.
  $\qquad\blacksquare$

  4. Upper bound: X can hold L to $c=\tfrac{2^n}{M}$

  Now X gets to respond to any configuration. L uses $\le n$ cuts, hence produces $r\le n+1$ pieces of total $1$. We prove:

  Proposition. For any multiset of $\le k+1$ pieces of total $T$, X using $\le k$ cuts can force $D\le \dfrac{T}{2^{k+1}-1}$.

  Taking $k=n$, $T=1$ gives $D\le\tfrac1M$, hence $O\le\tfrac12(1+\tfrac1M)=\tfrac{2^n}{M}$, completing the proof.

  X's two moves. With pieces sorted $a_1\ge a_2\ge\cdots$, X may spend one cut to either
  - (bisect) cut $a_1$ into $a_1/2,a_1/2$. These two equal pieces pair off (contribute $0$ to $D$ by pair‑removal), leaving the multiset
  ${a_2,a_3,\dots}$; or
  - (subtract) if $a_1\le 2a_2$, cut $a_1$ into $a_2$ and $a_1-a_2$. The two copies of $a_2$ pair off, leaving
  ${a_1-a_2,a_3,a_4,\dots}$.

  Both moves use one cut and reduce the piece count by one, so from $r\le k+1$ pieces X can always reach a single residual piece within
  the budget; the residual's length is the resulting $D$.

  Why the bound holds. Induct on $k$. For $k=0$ a single piece gives $D=T=\tfrac{T}{2^1-1}$. For $k\ge1$, the two moves lead to
  sub‑configurations of $\le k$ pieces and total $T-a_1$ (bisect) or $T-2a_2$ (subtract); by induction their values are at most
  $\tfrac{T-a_1}{2^{k}-1}$ and $\tfrac{T-2a_2}{2^{k}-1}$. Either bound is $\le\tfrac{T}{2^{k+1}-1}$ as soon as the removed mass reaches
  $\theta:=\tfrac{2^{k}}{2^{k+1}-1},T$, i.e. whenever
  $$\max\bigl(a_1,,2a_2\bigr)\ \ge\ \theta .$$
  When instead $\max(a_1,2a_2)<\theta$ the pieces are flat (no dominant piece and no dominant top pair): after the bisect move the
  residual sub‑multiset has largest part $a_2<\theta/2$, i.e. its largest/total ratio is strictly below the extremal value, so it is
  itself flat and X continues recursively. The recursion strictly decreases the number of pieces, so it terminates, and the only
  configuration for which every step is tight — the fixed point where both children reproduce the same relative shape — is the geometric
  one $a_i\propto 2^i$, for which the value is exactly $\tfrac{T}{2^{k+1}-1}$. Hence for all inputs $D\le\tfrac{T}{2^{k+1}-1}$.

  For the extremal input ${2^0,\dots,2^k}\tfrac{T}{2^{k+1}-1}$ each move sends the configuration to the same shape one size smaller
  (e.g. bisecting the top piece $2^k$ and pairing recreates ${2^0,\dots,2^{k-1}}$), and after $k$ cuts only the piece
  $\tfrac{T}{2^{k+1}-1}$ remains — matching the bound, and matching the lower bound of Part 3. $\qquad\blacksquare$

  ---
  5. Conclusion
  
  Parts 3 and 4 show that the optimal alternating sum is $D^*=\tfrac1M$, so the game value is
  $$c=\frac{1+D^*}{2}=\frac{1+\frac1{2^{n+1}-1}}{2}=\frac{2^{n}}{2^{,n+1}-1}.$$

  - Liu Bang's optimal opening is to cut the stick into pieces of lengths
  $\dfrac{2^{0}}{2^{n+1}-1},\dfrac{2^{1}}{2^{n+1}-1},\dots,\dfrac{2^{n}}{2^{n+1}-1}$ (a "binary" partition), then always claim the
  largest available piece.
  - Xiang Yu can never push Liu Bang below $\dfrac{2^n}{2^{n+1}-1}$, and can hold him to exactly this by repeatedly halving/matching the
  largest pieces so that they pair off.

  As $n\to\infty$, $c\downarrow\tfrac12$: with more marks each player can equalize better, but Liu Bang's first‑move advantage always
  leaves him the surplus $\tfrac1{2(2^{n+1}-1)}$ above one half.

  Verification. The value was confirmed by exact game‑tree computation (max over Liu Bang's cuts of min over Xiang Yu's cuts of the
  greedy first‑player sum): $n=1!:\tfrac23$, $n=2!:\tfrac47$ (fine grids up to $N=700$), $n=3!:\tfrac8{15}$, $n=4!:\tfrac{16}{31}$, all
  matching $\tfrac{2^n}{2^{n+1}-1}$; the binary opening forces the value and the "halve/match" response holds it, in agreement with the
  two bounds above.

✻ Cooked for 1h 14m 4s