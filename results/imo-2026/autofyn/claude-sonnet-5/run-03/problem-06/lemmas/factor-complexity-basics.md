## Factor-complexity basics for the gap sequence $(d_n)$

Let $d_n:=a_{n+1}-a_n$ (the gap sequence, an infinite word over the finite
alphabet $A=\{2,\dots,R\}$, $R=\mathrm{rad}(a_1)$, by
`lemmas/minimum-gap-lemma.md` and `lemmas/bounded-gap-via-rad-a1.md`). Let
$p(k)$ denote its factor-complexity function (the number of distinct
length-$k$ contiguous factors $(d_n,\dots,d_{n+k-1})$ occurring for some
$n\ge1$).

### Lemma 6.0.1 (monotonicity)
$p(k)\le p(k+1)$ for every $k\ge1$.

*Proof.* The "drop the last coordinate" map $\pi:A^{k+1}\to A^k$ sends
every occurring length-$(k+1)$ factor to an occurring length-$k$ factor
(the prefix), surjectively onto the set of occurring length-$k$ factors.
Hence the latter set has size $\le$ the former. $\blacksquare$

### Corollary 6.1.3 (negative result: window-sum counting does not bound $p(k)$)
The naive "Complexity Bound Lemma" (count distinct window sums
$g_n(k):=d_n+\cdots+d_{n+k-1}\in[2k,kR]$ to bound $p(k)$) is **false as a
bound on $p(k)$**: the sum map is not injective, even restricted to
factors genuinely realized by an actual instance.

*Abstract witness.* For any $k\ge2,R\ge4$: $w_1=(2,4,2,\dots,2)$,
$w_2=(3,3,2,\dots,2)\in A^k$ are distinct tuples with equal sum.

*Realized witness ($a_1=35$).* The gap sequence begins
$d_1,\dots,d_{17}=5,2,3,5,10,10,5,5,4,6,10,5,5,10,6,4,5$ (from
$a_1,\dots,a_{18}=35,40,42,45,50,60,70,75,80,84,90,100,105,110,120,126,
130,135$). The length-2 factors $(d_8,d_9)=(5,4)$ and
$(d_{16},d_{17})=(4,5)$ both occur, are distinct as ordered pairs, and both
sum to $9$. Direct computation over a longer range gives $p(2)=16$
distinct length-2 factors but only $S(2)=8$ distinct sums for this
instance — confirming $p(2)>S(2)$, i.e. the window-sum count is a
strictly smaller (and hence invalid as an upper bound on $p(k)$) quantity
whenever such a collision occurs among realized factors.

*Consequence.* No repair of the same map/counting argument can bound
$p(k)$ via window sums; the failure is genuine non-injectivity on
realized inputs, not a looseness in the counting.

### Theorem 6.2.2 (conditional: Unified Central Claim $\Rightarrow$ exact factor-complexity bound)
If the Unified Central Claim holds for some finite $Q\supseteq R(a_1)$
(i.e. $\mathrm{Good}_Q(a_n)$ for every $n\ge1$), then $(d_n)$ is purely
periodic from $n=1$ (no transient, by `lemmas/transient-free-finishing-theorem.md`)
with some period $T=|\mathrm{GoodRes}(Q)|$, and consequently $p(k)\le T$
for every $k\ge1$.

*Proof.* Immediate: a purely periodic word with period $T$ has at most $T$
distinct starting positions mod $T$, hence at most $T$ distinct length-$k$
factors for any $k$, since each factor is determined by its starting
residue mod $T$. $\blacksquare$

### Caveats
- These results are about $p(k)$, a reformulated vocabulary for the
  syndeticity/periodicity target; they do **not** by themselves close the
  central existence gap.
- Theorem 6.2.2 is conditional on the still-open Unified Central Claim; it
  is a free corollary once that claim is established, chaining two
  already-certified lemmas.
- The converse direction ($p(k)$ bounded $\Rightarrow$ the IMO conclusion)
  is NOT established: Morse-Hedlund only gives *eventual* periodicity
  (not periodicity for every $n\ge1$ as the problem requires), and no
  transient-removal argument independent of the $Q$-machinery is known.

### Provenance
Proved in `approaches/scalar-difference-pigeonhole.md`, §6.0–6.2, round 6.
Independently re-verified by the proof-reviewer (Claim 6.1.2's realized
collision re-simulated exactly: $p(2)=16$, $S(2)=8$ for $a_1=35$, matching
the file's claim precisely).
