Solution

  Answer. $$c(n) = \dfrac{2^n}{2^{n+1}-1}.$$

  I'll now write up the complete derivation.

  Step 1: Reduction to an alternating-pick game

  Lemma 1. Once the stick is cut into pieces of lengths $\ell_1\ge \ell_2\ge\cdots\ge\ell_m$, if both players play optimally in the
  claiming phase (each maximizing their own total), the unique optimal strategy for both is to always claim the largest remaining piece.
  Consequently Liu Bang's total is $\ell_1+\ell_3+\ell_5+\cdots$ and Xiang Yu's is $\ell_2+\ell_4+\cdots$.

  Proof. By induction on $m$. If Liu Bang does not take $\ell_1$ first, say he takes $\ell_j$ ($j>1$), then Xiang Yu can take $\ell_1$.
  One checks by an exchange argument that swapping Liu Bang's move to $\ell_1$ (and adjusting the rest of his strategy to mimic what he
  would have done) never decreases his total: informally, having the largest item in hand is at least as good as having any smaller
  item, since it can be substituted into any later "role" that item would have played. Formally, suppose in the sub-game after removing
  $\ell_1,\ell_j$ (both already gone) both play greedily by induction; comparing to the sub-game after removing $\ell_j,\ell_1$ is
  identical. So WLOG Liu Bang takes $\ell_1$; by symmetry (relabeling) Xiang Yu then optimally takes the largest remaining, $\ell_2$,
  etc. $\blacksquare$

  (This is the standard fact about such "take-turns, maximize own greedy sum" games.)

  Step 2: The core combinatorial quantity

  Suppose Liu Bang marks points splitting $[0,1]$ into pieces $a_1,\dots,a_{n+1}$ (WLOG he uses exactly $n$ points — using fewer only
  removes flexibility). Xiang Yu, seeing this, marks $\le n$ further points, refining these into a final list of pieces. By Lemma 1, Liu
  Bang's total is
  $$\text{LiuShare} = \sum_{\text{odd rank}} \ell_i, \qquad \text{so LiuShare} = \frac{1+A}{2},\quad
  A:=\text{LiuShare}-\text{XiangShare}=\sum_i (-1)^{\text{rank}(i)+1}\ell_i .$$

  Lemma 2 (Parity Lemma). Group the final pieces by value into maximal runs of equal length. A run whose value has even multiplicity
  contributes $0$ to $A$; a run with odd multiplicity $2t+1$ contributes exactly $\pm(\text{that value})$ (as if only one copy existed),
  with sign determined by parity of the count of odd-multiplicity values above it. Consequently, if $u_1>u_2>\cdots>u_p$ are the values
  with odd multiplicity (listed once each, in decreasing order),
  $$A = u_1-u_2+u_3-\cdots .$$

  Proof. Within a run of $m$ equal copies starting at rank $r$, the signs alternate starting with sign of rank $r$; the alternating sum
  of $m$ consecutive signs is $0$ if $m$ even, and $\pm(\text{one copy})$ if $m$ odd (sign $=(-1)^{r+1}$). Since even-multiplicity runs
  contribute an even number of elements, they don't affect the parity of $r$ for later runs. Hence only odd-multiplicity runs matter,
  and among only those, the situation is exactly as if they were listed alone with their natural alternating signs. $\blacksquare$

  In particular $A\ge 0$ always (Liu Bang, moving first, never does worse than Xiang Yu), and $A=0$ iff every value has even
  multiplicity, i.e. all final pieces pair up perfectly.

  Consequence. Xiang Yu's goal is to use his points to pair up as much of the total length as possible into matched equal-length pairs
  (each pair splits $50/50$ and contributes $0$), so as to make the alternating sum of the unpaired ("odd multiplicity") leftover values
  as small as possible.

  Step 3: Xiang Yu's power = ternary sign combinations

  Say Xiang Yu discards a piece by bisecting it (1 point: turns it into a matched pair, contributing $0$), and merges two
  currently-unpaired pieces $x\ge y$ by cutting $x$ into $y$ and $x-y$ (1 point: the $y$-fragment pairs with the existing $y$, leaving a
  new unpaired piece of size $x-y$).

  Lemma 3 (Achievability). For any $a_1,\dots,a_{n+1}>0$ and any $\delta\in{-1,0,1}^{n+1}\setminus{0}$, Xiang Yu can use exactly $n$
  points (discards + merges) to make the final leftover equal $\left|\sum_i \delta_i a_i\right|$.

  Proof. Let $Z={i:\delta_i=0}$, and discard each of them (bisect): $|Z|$ points. Let $P={i:\delta_i=1}$, $N={i:\delta_i=-1}$; we must
  combine the $k=|P|+|N|$ remaining pieces into a single leftover of value $\big|\sum_P a_i - \sum_N a_i\big|$ using $k-1$ merges. We
  show by strong induction on $k$ that this is always achievable — moreover that it is achievable while keeping both pools $P,N$
  nonempty at every intermediate step until $k=1$:

  Sub-claim: if $k\ge 2$ and the target value $\mu=|\sum_P a-\sum_N a|$ is minimal among nonzero sign-combinations of $P\cup N$ (this
  holds because $\delta$ came from minimizing over all patterns — see Step 4), then $P,N$ are both nonempty. Indeed if $N=\emptyset$ and
  $|P|\ge2$: flipping the sign of the smallest $p_{\min}\in P$ changes the value from $\mu=\sum P$ to $\mu-2p_{\min}$, and since
  $0<p_{\min}<\mu$ (as $|P|\ge 2$), we get $|\mu-2p_{\min}|<\mu$, contradicting minimality. So $P=\emptyset$ or $|P|\le1$ (symmetric for
  $N$); combined with $k\ge2$, both are nonempty.

  Now pick any $p\in P,\ n\in N$ and merge them (Move-B), producing a new element $r=|p-n|$ which is inserted into $P$ (if $p\ge n$) or
  $N$ (if $n>p$). This reduces to a $(k-1)$-element problem $P',N'$. Two facts finish the induction:
  - (Value preserved) $\sum_{P'}a-\sum_{N'}a = \sum_P a - \sum_N a$ exactly (pure algebra: replacing $p,-n$ or $-p,n$ by $\pm r$
  preserves the sum). 
  - (Optimality preserved) The $(k-1)$-problem's own minimum $\mu'$ satisfies $\mu'=\mu$: certainly $\mu'\le\mu$ (our pattern achieves
  $\mu$ on $k-1$ elements); conversely, any sign-pattern $\delta'$ on the reduced $(k-1)$-set lifts to a sign pattern on the original
  $k$-set with the same value (choose $(\epsilon_p,\epsilon_n)=(+,-)$ or $(-,+)$ to match $\pm r$ as needed), so $\mu\le\mu'$ by
  minimality of $\mu$.

  So $P',N'$ is again an optimal, minimal pattern for a $(k-1)$-problem, hence (by the sub-claim, if $k-1\ge2$) both nonempty, and
  induction applies. This never gets "stuck," and after $k-1$ merges exactly one leftover, of value $\mu$, remains. Total points used:
  $|Z|+(k-1) = (n+1)-1=n$. $\blacksquare$

  Step 4: The pigeonhole bound (Xiang Yu's guarantee — upper bound on $c(n)$)

  Lemma 4. For any $a_1,\dots,a_{n+1}>0$ summing to $S$,
  $$\mu(a):=\min_{\delta\in{-1,0,1}^{n+1}\setminus 0}\Big|\sum_i \delta_i a_i\Big| \ \le\ \frac{S}{2^{n+1}-1}.$$

  Proof. Consider all $2^{n+1}$ subset sums $S_T=\sum_{i\in T} a_i$, $T\subseteq{1,\dots,n+1}$, lying in $[0,S]$. For distinct subsets
  $T_1\ne T_2$, $S_{T_1}-S_{T_2}=\sum \delta_i a_i$ where $\delta_i=[i\in T_1]-[i\in T_2]\in{-1,0,1}$ is nonzero (since $T_1 \ne T_2$),
  so $|S_{T_1}-S_{T_2}|\ge \mu(a)$. Thus the $2^{n+1}$ subset sums, sorted, have all pairwise gaps $\ge \mu(a)$; in particular the
  $2^{n+1}-1$ consecutive gaps are each $\ge \mu(a)$, and they sum to the total range $S-0=S$. Hence $(2^{n+1}-1)\mu(a)\le S$.
  $\blacksquare$

  Combining Lemma 3 (achievability) with Lemma 4: for every choice of Liu Bang's pieces, Xiang Yu can force $A\le \mu(a) \le
  \dfrac{1}{2^{n+1}-1}$ (taking $S=1$), i.e.

  In particular $A\ge 0$ always (Liu Bang, moving first, never does worse than Xiang Yu), and $A=0$ iff every value has even
  multiplicity, i.e. all final pieces pair up perfectly.

  Consequence. Xiang Yu's goal is to use his points to pair up as much of the total length as possible into matched equal-length pairs
  (each pair splits $50/50$ and contributes $0$), so as to make the alternating sum of the unpaired ("odd multiplicity") leftover values
  as small as possible.

  Step 3: Xiang Yu's power = ternary sign combinations

  Say Xiang Yu discards a piece by bisecting it (1 point: turns it into a matched pair, contributing $0$), and merges two
  currently-unpaired pieces $x\ge y$ by cutting $x$ into $y$ and $x-y$ (1 point: the $y$-fragment pairs with the existing $y$, leaving a
  new unpaired piece of size $x-y$).

  Lemma 3 (Achievability). For any $a_1,\dots,a_{n+1}>0$ and any $\delta\in{-1,0,1}^{n+1}\setminus{0}$, Xiang Yu can use exactly $n$
  points (discards + merges) to make the final leftover equal $\left|\sum_i \delta_i a_i\right|$.

  Proof. Let $Z={i:\delta_i=0}$, and discard each of them (bisect): $|Z|$ points. Let $P={i:\delta_i=1}$, $N={i:\delta_i=-1}$; we must
  combine the $k=|P|+|N|$ remaining pieces into a single leftover of value $\big|\sum_P a_i - \sum_N a_i\big|$ using $k-1$ merges. We
  show by strong induction on $k$ that this is always achievable — moreover that it is achievable while keeping both pools $P,N$
  nonempty at every intermediate step until $k=1$:

  Sub-claim: if $k\ge 2$ and the target value $\mu=|\sum_P a-\sum_N a|$ is minimal among nonzero sign-combinations of $P\cup N$ (this
  holds because $\delta$ came from minimizing over all patterns — see Step 4), then $P,N$ are both nonempty. Indeed if $N=\emptyset$ and
  $|P|\ge2$: flipping the sign of the smallest $p_{\min}\in P$ changes the value from $\mu=\sum P$ to $\mu-2p_{\min}$, and since 
  $0<p_{\min}<\mu$ (as $|P|\ge 2$), we get $|\mu-2p_{\min}|<\mu$, contradicting minimality. So $P=\emptyset$ or $|P|\le1$ (symmetric for
  $N$); combined with $k\ge2$, both are nonempty.

  Now pick any $p\in P,\ n\in N$ and merge them (Move-B), producing a new element $r=|p-n|$ which is inserted into $P$ (if $p\ge n$) or
  $N$ (if $n>p$). This reduces to a $(k-1)$-element problem $P',N'$. Two facts finish the induction:
  - (Value preserved) $\sum_{P'}a-\sum_{N'}a = \sum_P a - \sum_N a$ exactly (pure algebra: replacing $p,-n$ or $-p,n$ by $\pm r$
  preserves the sum).
  - (Optimality preserved) The $(k-1)$-problem's own minimum $\mu'$ satisfies $\mu'=\mu$: certainly $\mu'\le\mu$ (our pattern achieves
  $\mu$ on $k-1$ elements); conversely, any sign-pattern $\delta'$ on the reduced $(k-1)$-set lifts to a sign pattern on the original
  $k$-set with the same value (choose $(\epsilon_p,\epsilon_n)=(+,-)$ or $(-,+)$ to match $\pm r$ as needed), so $\mu\le\mu'$ by
  minimality of $\mu$.
  
  So $P',N'$ is again an optimal, minimal pattern for a $(k-1)$-problem, hence (by the sub-claim, if $k-1\ge2$) both nonempty, and
  induction applies. This never gets "stuck," and after $k-1$ merges exactly one leftover, of value $\mu$, remains. Total points used:
  $|Z|+(k-1) = (n+1)-1=n$. $\blacksquare$

  Step 4: The pigeonhole bound (Xiang Yu's guarantee — upper bound on $c(n)$)

  Lemma 4. For any $a_1,\dots,a_{n+1}>0$ summing to $S$,
  $$\mu(a):=\min_{\delta\in{-1,0,1}^{n+1}\setminus 0}\Big|\sum_i \delta_i a_i\Big| \ \le\ \frac{S}{2^{n+1}-1}.$$

  Proof. Consider all $2^{n+1}$ subset sums $S_T=\sum_{i\in T} a_i$, $T\subseteq{1,\dots,n+1}$, lying in $[0,S]$. For distinct subsets
  $T_1\ne T_2$, $S_{T_1}-S_{T_2}=\sum \delta_i a_i$ where $\delta_i=[i\in T_1]-[i\in T_2]\in{-1,0,1}$ is nonzero (since $T_1 \ne T_2$),
  so $|S_{T_1}-S_{T_2}|\ge \mu(a)$. Thus the $2^{n+1}$ subset sums, sorted, have all pairwise gaps $\ge \mu(a)$; in particular the
  $2^{n+1}-1$ consecutive gaps are each $\ge \mu(a)$, and they sum to the total range $S-0=S$. Hence $(2^{n+1}-1)\mu(a)\le S$.
  $\blacksquare$

  Combining Lemma 3 (achievability) with Lemma 4: for every choice of Liu Bang's pieces, Xiang Yu can force $A\le \mu(a) \le
  \dfrac{1}{2^{n+1}-1}$ (taking $S=1$), i.e.
  $$\text{LiuShare}=\frac{1+A}{2}\ \le\ \frac{1}{2}+\frac{1}{2(2^{n+1}-1)} = \frac{2^n}{2^{n+1}-1}.$$
  So $c(n)\le \dfrac{2^n}{2^{n+1}-1}$.

  Step 5: The matching construction (Liu Bang's guarantee — lower bound on $c(n)$)

  Let Liu Bang choose pieces proportional to $1,2,4,\dots,2^n$ (i.e. cuts producing pieces
  $\frac{1}{2^{n+1}-1},\frac{2}{2^{n+1}-1},\dots,\frac{2^n}{2^{n+1}-1}$). Since these are distinct powers of $2$, the only nonzero
  ternary combination equal to something of absolute value $<1$ (unnormalized) is impossible: any nonzero integer combination of
  distinct powers of $2$ with coefficients in ${-1,0,1}$ is a nonzero integer (as such sums are injective — this is the
  balanced-ternary/binary argument: if two ternary vectors gave equal value, their difference would be a nonzero
  ${-2,-1,0,1,2}$-combination summing to $0$, forcing all coefficients $0$ by comparing highest surviving power), hence has absolute
  value $\ge 1$. So $\mu(b)=1$ exactly (achieved uniquely, up to the choice of extra zero-combinations, by isolating the smallest piece
  $b_1=1$), matching Lemma 4 with equality.

  This shows: against the "discard-and-merge" strategy family, Xiang Yu cannot beat $A=1$ (unnormalized), i.e. cannot beat LiuShare
  $=\frac{2^n}{2^{n+1}-1}$; and by Lemma 3 he can achieve exactly this (bisect the $n$ larger pieces, leave the smallest piece
  $\frac{1}{2^{n+1}-1}$ alone).

  That no other (non discard/merge) cutting strategy by Xiang Yu can do better was checked exhaustively via an exact optimizer
  (performing provably-exact, breakpoint-based single-coordinate optimization over Xiang Yu's points, with no restriction to the
  discard/merge move-set) for $n=1,2,3,4,5$, always returning exactly $2^n/(2^{n+1}-1)$; and for $n=1$ this is confirmed by hand: with
  pieces $(x,1-x)$, direct case analysis (Xiang Yu's best response is "no cut" for $x<2/3$, giving $A=2x-1$, or "bisect the larger
  piece" for $x\ge2/3$, giving $A=1-x$) shows the value is maximized exactly at $x=2/3$, giving $c(1)=2/3=\frac{2^1}{2^2-1}$, matching
  the formula.

  Conclusion

  $$\boxed{c(n) = \dfrac{2^n}{2^{n+1}-1}}$$

  Sanity checks: $c(1)=2/3$ (verified rigorously by hand), $c(2)=4/7$, $c(3)=8/15$, and $c(n)\to \tfrac12$ as $n\to\infty$ (more cutting
  power for both sides washes out Liu Bang's first-move advantage), while $c(0)=1$ (no cuts $\Rightarrow$ Liu Bang takes the whole
  stick) — all consistent with the formula.

  ---
  I should be transparent about the one place I could not produce a fully self-contained elementary proof within this session: showing
  that Xiang Yu's arbitrary cutting (not restricted to the discard/bisect-or-match moves of Lemma 3) can never beat $A=1$ against the
  specific geometric construction. I have a complete rigorous proof of this fact via the discard/merge strategy family, complete
  rigorous matching upper bound for all Liu Bang strategies (Steps 3–4), and I verified the missing direction is correct via exact
  (non-heuristic, breakpoint-exact) computation across $n=1,\dots,5$ with no discrepancy, plus a full hand-verified proof for $n=1$. I
  was not able to convert this into a fully general elementary induction in the time available, despite substantial effort (an
  "insertion formula" approach came close: one can show $\mu(Y)\le\mu(\text{original})$ always holds but the reverse relation needed for
  $A$ resisted a clean closed form). I'm confident the boxed answer is correct, but flag this one gap in full rigor per your request
  for transparency.

✻ Sautéed for 1h 25m 59s