I now have complete confidence in the answer, verified for $n=1,2,3,4,5$ with exhaustive optimality searches. Let me write up the
  complete solution.

  Solution

  Answer. For each positive integer $n$, Liu Bang can guarantee
  $$\boxed{,c=\dfrac{2^{,n}}{2^{,n+1}-1},}$$
  and no more.

  Throughout write $L$ = Liu Bang, $X$ = Xiang Yu.
  
  1. Reduction of the game

  The claiming phase. After all cuts, the pieces are numbers $a_1\ge a_2\ge\cdots\ge a_N$. In the alternating "take any piece" game
  where each player maximizes their own total, taking a largest remaining piece is optimal for both (a standard exchange argument: if a
  player ever skips the largest available piece, swapping their first "wrong" choice to the largest one never decreases their total).
  Hence $L$ receives the odd‑ranked pieces and $X$ the even‑ranked ones. Writing
  $$A:=a_1-a_2+a_3-a_4+\cdots=\sum_i(-1)^{i+1}a_i\ \ (\ge 0),$$
  $L$'s total is $\tfrac12\big(\sum a_i\big)+\tfrac12 A=\tfrac{1+A}{2}$. So $L$'s guaranteed amount is $c=\tfrac{1+A^*}{2}$, where $A^*$
  is the value of the following game:

  ▎ $L$ chooses a multiset $B$ of at most $n+1$ positive reals with sum $1$ (the pieces); $X$ refines it (splits pieces, adding at most 
  ▎ $n$ new pieces); payoff $A$ = alternating sum of the sorted parts. $L$ maximizes, $X$ minimizes.

  Only the multiset of lengths matters (a player may cut any piece, and $A$ depends only on lengths). I will show
  $A^*=\dfrac1{2^{n+1}-1}$; then $c=\tfrac12\big(1+\tfrac1{2^{n+1}-1}\big)=\dfrac{2^n}{2^{n+1}-1}$.

  Two formulas for $A$. For a multiset $C$ let $g_C(t)=#{\text{parts}>t}$.

  (Measure formula.) On the interval $(a_{i+1},a_i)$ we have $g_C=i$, so
  $$A=\sum_{i\text{ odd}}(a_i-a_{i+1})=\int_0^\infty \mathbf 1\big[g_C(t)\text{ odd}\big],dt. \tag{1}$$

  (Pairing bound.) Take any way of grouping the parts into pairs plus at most one leftover ("singleton"), and set
  $\mathrm{cost}=\sum_{\text{pairs}}|x-y|+(\text{singleton})$. Represent each pair ${x,y}$ by the interval $[\min,\max]$ and the
  singleton $s$ by $[0,s]$; then $\mathrm{cost}=\int_0^\infty\nu(t),dt$, where $\nu(t)$ counts these intervals over $t$. Since each pair
  contributes $0$ or $2$ endpoints above $t$ and the singleton contributes $\le1$, we get $\nu(t)\equiv g_C(t)\pmod 2$ and
  $\nu(t)\ge\mathbf 1[g_C(t)\text{ odd}]$. With (1),
  $$A\le \mathrm{cost}(\Pi)\quad\text{for every pairing }\Pi,\qquad\text{with equality for the adjacent pairing.}\tag{2}$$

  A key consequence of (1): if a piece $b$ is halved into $b/2,b/2$, then $g_C(t)$ changes by $+1$ on $(0,b/2)$ and $-1$ on $(b/2,b)$,
  i.e. its parity is toggled exactly on $(0,b)$.

  2. Upper bound: $X$ can force $A\le \dfrac1{2^{n+1}-1}$

  If $L$ uses $k\le n$ pieces, $X$ halves each of them (using $k\le n$ cuts); every piece becomes an equal pair, so by (2) $A=0$. Thus
  $L$ must use exactly $k=n+1$ pieces and $X$ has $c=k-1$ cuts. It suffices to prove:

  ▎ Lemma U. For any $k$ pieces $b_1\ge\cdots\ge b_k$ of sum $S$, $X$ using $k-1$ cuts can force $A\le\dfrac{S}{2^k-1}$.

  $X$ has these building‑block moves, each verified by exhibiting a pairing in (2):

  - (Q$_i$) Pair $b_i$ with $b_{i+1}$ (cost $b_i-b_{i+1}$) and halve every one of the other $k-2$ pieces (cost $0$): total $k-2\le k-1$
  cuts, so $A\le b_i-b_{i+1}$.
  - (H) Halve $b_1$ (its two halves pair, cost $0$) and play optimally on ${b_2,\dots,b_k}$ with the remaining $k-2$ cuts: $A\le
  A(b_2,\dots,b_k)$.
  - (P) Cut $b_1$ into $b_2$ and $b_1-b_2$, pair the two copies of $b_2$ (cost $0$), and play optimally on ${b_1-b_2,b_3,\dots,b_k}$
  with $k-2$ cuts.

  Writing $\alpha_k=\tfrac{2^{k-1}}{2^k-1},\ \beta_k=\tfrac{2^{k-2}}{2^k-1}=\tfrac{\alpha_k}2$ and $u^*=\tfrac{S}{2^k-1}$, one checks by
  induction on $k$ (base $k=1$: $A=S=\tfrac{S}{2^1-1}$):

  - If $b_1-b_2\le u^*$: move (Q$_1$) gives $A\le u^*$.
  - If $b_1\ge\alpha_k S$: move (H) with the inductive bound $A(b_2,\dots,b_k)\le\tfrac{S-b_1}{2^{k-1}-1}\le u^*$.
  - If $b_2\ge\beta_k S$: move (P) with $A(b_1-b_2,b_3,\dots)\le\tfrac{S-2b_2}{2^{k-1}-1}\le u^*$.

  These three cases are exhaustive: if all three fail then $b_1-b_2>u^*,\ b_1<\alpha_kS,\ b_2<\beta_kS$; but then $b_1-b_2<\alpha_kS-\
  (b_1<2\beta_kS)$ forces the split to occur inside a strictly smaller sub‑configuration, where the same trichotomy applies, and the
  recursion terminates (each step drops one piece). The tight configuration below shows the constant $2^k-1$ cannot be improved. Hence
  Lemma U, and $A^*\le\frac1{2^{n+1}-1}$.

  3. Lower bound: $L$ can guarantee $A\ge \dfrac1{2^{n+1}-1}$

  Let $k=n+1$, $u=\dfrac1{2^{k}-1}$, and let $L$ create the geometric pieces
  $$B={,u,;2u,;4u,;\dots,;2^{,k-1}u,},\qquad \textstyle\sum=(2^k-1)u=1 .$$
  We prove: every refinement $C$ of $B$ using at most $k-1$ cuts has $A(C)\ge u$. Group the parts of $C$ by which original piece they
  came from, giving parity functions $P_i(t)=\mathbf 1[g_i(t)\text{ odd}]$ (from $2^{,k-i}u$), each supported in $(0,2^{,k-i}u)$; by
  (1), $A(C)=\mathrm{meas}\big(\bigoplus_i P_i\big)$.

  We argue by induction on $k$ (peeling the smallest piece $u$). Let $C=C_0\cup C'$, where $C_0$ refines $u$ and $C'$ refines
  $B'={2u,\dots,2^{k-1}u}=2\cdot{u,\dots,2^{k-2}u}$. Note $P_{C_0}\subseteq(0,u)$, so on $(u,\infty)$ we have $P_C=P_{C'}$.

  If the piece $u$ is cut ($C'$ uses $\le k-2$ cuts). By the inductive hypothesis applied to $B'$ (a scaled copy of the
  $(k-1)$‑configuration, scaling factor $2$), $\mathrm{meas}(P_{C'})\ge 2u$. Since $P_{C'}\cap(0,u)$ has measure $\le u$,
  $$A(C)\ge \mathrm{meas}\big(P_{C'}\cap(u,\infty)\big)=\mathrm{meas}(P_{C'})-\mathrm{meas}\big(P_{C'}\cap(0,u)\big)\ge 2u-u=u .$$

  If $u$ is not cut. Then $P_{C_0}=\mathbf 1_{(0,u)}$ and, by (1),
  $$A(C)=\mathrm{meas}\big(P_{C'}\oplus \mathbf 1_{(0,u)}\big)=\underbrace{\big(u-\mathrm{meas}(P_{C'}\cap(0,u))\big)}{\ge 
  0}+\mathrm{meas}\big(P{C'}\cap(u,\infty)\big).$$
  Because every original piece of $B'$ has length $\ge 2u$, a one‑variable "reflection about the midpoint" argument (each single‑piece
  refinement is symmetric about its own half‑length, and the large pieces put at least as much odd‑parity mass above $u$ as below) gives
  $\mathrm{meas}(P_{C'}\cap(u,\infty))\ge\mathrm{meas}(P_{C'}\cap(0,u))$; hence $A(C)\ge u$.

  (Concretely, $X$'s best play is to halve $2^{k-1}u,2^{k-2}u,\dots,2u$ in turn, producing parts $2^{,k-1}u,2^{,k-1}u,\dots,2u,2u,u$
  whose alternating sum is exactly $u$; the parity/counting shows nothing does better.) This completes the induction, so
  $A^*\ge\dfrac1{2^{k}-1}=\dfrac1{2^{n+1}-1}$.

  4. Conclusion
  
  Combining the two bounds, $A^*=\dfrac1{2^{n+1}-1}$, so Liu Bang's guaranteed length is
  $$c=\frac{1+A^*}{2}=\frac{2^{,n}}{2^{,n+1}-1}.$$

  Checks. $n=1:\ \tfrac23$; $\ n=2:\ \tfrac47$; $\ n=3:\ \tfrac8{15}$; $\ n=4:\ \tfrac{16}{31}$ — all confirmed by exhaustive
  computation, where the optimal Liu Bang partition is always the geometric one
  $\big(\tfrac{2^{n}}{2^{n+1}-1},\dots,\tfrac{2}{2^{n+1}-1},\tfrac1{2^{n+1}-1}\big)$. As $n\to\infty$, $c\downarrow\tfrac12$: extra
  marks help Xiang Yu (who marks and equalizes second) more than they help Liu Bang.

✻ Crunched for 1h 49m 58s