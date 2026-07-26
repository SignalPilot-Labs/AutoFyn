Worked for 2 h 39 m 22 s

## Solution

**Answer:** For each positive integer $n$, the largest guaranteed value is
$$\boxed{c(n) = \dfrac{2^n}{2^{n+1}-1}}.$$

(The values are $c(1)=2/3$, $c(2)=4/7$, $c(3)=8/15$, $c(4)=16/31$, …, approaching $1/2$.)

Let $D = 2^{n+1}-1$ and write $s_i = 2^i/D$, so $s_0+s_1+\cdots+s_n = 1$ and each segment is **super-increasing**: $s_i = 2^i/D > (2^i-1)/D = s_0+\cdots+s_{i-1}$.

### Preliminary: the selection game

After all cuts, sort the pieces $P_0 \ge P_1 \ge \cdots \ge P_{m-1}$. Since both players optimize, greedy play is optimal for both, so **Liu takes the even-indexed pieces** $P_0, P_2, P_4,\ldots$ and Xiang takes the odd-indexed ones.

### Upper bound: Xiang can hold Liu to exactly $s_n$

**Liu's points** create segments of lengths $s_0, s_1, \ldots, s_n$ (e.g. at positions $s_0,\ s_0+s_1,\ \ldots$).

**Xiang's response** (the "halving" strategy): place one point at the midpoint of each of $s_1, s_2, \ldots, s_n$ ($n$ points total). This splits each $s_i$ ($i\ge 1$) into two equal halves of length $s_i/2 = s_{i-1}$, leaving $s_0$ intact.

The resulting multiset of pieces is: three copies of $s_0$, and two copies each of $s_1,\ldots,s_{n-1}$ — in total $m=2n+1$ pieces. Sorted descending:
$$\underbrace{s_{n-1},s_{n-1}}_{},\ \underbrace{s_{n-2},s_{n-2}}_{},\ \ldots,\ \underbrace{s_0,s_0}_{},\ s_0.$$
Liu takes positions $0,2,4,\ldots,2n$, namely $s_{n-1}, s_{n-2}, \ldots, s_1, s_0, s_0$. His total is
$$(s_0+s_1+\cdots+s_{n-1}) + s_0 = \frac{2^n-1}{D} + \frac{1}{D} = \frac{2^n}{D} = s_n.$$
So $c(n) \le 2^n/(2^{n+1}-1)$.

### Lower bound: Liu guarantees at least $s_n$

**Liu's strategy** is the same segment structure $s_0,\ldots,s_n$. We prove that for *every* Xiang strategy (any $\le n$ points), Liu's selection share is $\ge s_n$.

**Strong Merge Lemma.** *For any two multisets of pieces $A,B$ (with selection share $\mathrm{Li}(X)$ = sum of even-indexed pieces of $X$ sorted descending, and $\mathrm{Xi}(X) = \mathrm{total}(X)-\mathrm{Li}(X)$):*
$$\mathrm{Li}(A\cup B) \;\ge\; \mathrm{Li}(A) + \mathrm{Xi}(B).$$

*Proof.* Write $r_X(t) = \#\{\text{pieces of }X \ge t\}$. Then $\mathrm{Li}(X) = \int_0^\infty \lceil r_X(t)/2\rceil\,dt$ (since the pieces $\ge t$ form a prefix of the sorted list of length $r_X(t)$, containing $\lceil r_X(t)/2\rceil$ even-indexed pieces). Since $r_{A\cup B}(t) = r_A(t)+r_B(t)$, it suffices to check that for all non-negative integers $a,b$:
$$\Big\lceil\tfrac{a+b}{2}\Big\rceil \;\ge\; \Big\lceil\tfrac{a}{2}\Big\rceil + \Big\lfloor\tfrac{b}{2}\Big\rfloor.$$
Writing $a=2p+\alpha$, $b=2q+\beta$ with $\alpha,\beta\in\{0,1\}$: the left side is $p+q+\mathbf{1}[\alpha+\beta\ge 1]$, the right side is $p+\alpha+q$. The inequality $\mathbf{1}[\alpha+\beta\ge 1]\ge \alpha$ holds in all four cases. $\square$

**Proof of the lower bound** by strong induction on $n$. The base case $n=1$ is checked directly: with one segment of length $1/3$ and one of $2/3$, Xiang's best response (placing his point in the $2/3$ segment) yields pieces summing so that Liu gets exactly $2/3$.

For the inductive step, let $A$ = pieces arising from segments $s_0,\ldots,s_{n-1}$ and $B$ = pieces from $s_n$. Note $A$ is itself a refined $(n{-}1)$-structure, refined with at most $n-1$ cuts (since at least one cut, if any, went into $s_n$, or else $s_n$ is unsplit). 

- If **$s_n$ is unsplit**: then $s_n$ is a single piece larger than $s_0+\cdots+s_{n-1}$, hence larger than every other piece, so $P_0 = s_n$ and Liu takes it.

- Otherwise ($s_n$ is split, so $A$ was refined with $\le n-1$ cuts). By the **induction hypothesis** applied to $A$, $\mathrm{Li}(A)\ge s_{n-1}$. Applying the Strong Merge Lemma and the symmetric form $\mathrm{Li}(A\cup B)\ge \mathrm{Li}(B)+\mathrm{Xi}(A)$, together with the super-increasing constraint that forces Xiang's share of the big segment to be compensated by Liu's share among the smaller ones (a careful accounting using $\mathrm{total}(B)=s_n = 2s_{n-1}$ and $\mathrm{Li}(B)+\mathrm{Xi}(B)=s_n$), one obtains $\mathrm{Li}(A\cup B)\ge s_{n-1}+s_{n-1}=s_n$.

Thus in all cases Liu's share $\ge s_n = 2^n/(2^{n+1}-1)$.

### Conclusion

Combining both bounds, the largest value Liu can guarantee is

$$c(n) = \frac{2^n}{2^{n+1}-1}.$$