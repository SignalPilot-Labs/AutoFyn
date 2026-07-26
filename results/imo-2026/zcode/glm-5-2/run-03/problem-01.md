Worked for 11 m 43 s

## Rigorous Proof

**Notation.** For a prime $p$ and integer $x$, let $v_p(x)$ be the $p$-adic valuation, with $v_p(1)=0$. Write the board at any time as $(a_1,\dots,a_N)$ with $N=2026$.

---

### Step 1 — The per-prime behavior

Fix a prime $p$. A move acts on two positions $i,j$. Let $a = v_p(a_i)$, $b = v_p(a_j)$. The two new valuations are:
$$v_p(\gcd(a_i,a_j)) = \min(a,b), \qquad v_p\!\left(\tfrac{\operatorname{lcm}(a_i,a_j)}{\gcd(a_i,a_j)}\right) = \max(a,b)-\min(a,b)=|a-b|.$$

So at the valuation level the move is the **subtraction-Euclid operation**
$$(a,b)\;\longmapsto\;(\min(a,b),\,|a-b|).\tag{$\star$}$$

Two elementary facts about $(\star)$:
- $\min(a,b)+|a-b|=\max(a,b)$, so the sum of the two touched valuations is **non-increasing**, and strictly decreases whenever both $a,b>0$ (since then $\min(a,b)\geq 1$).
- $\gcd(\min(a,b),|a-b|)=\gcd(a,b)$, so the **gcd of the two touched valuations is invariant**.

---

### Step 2 — Per-prime termination lemma

**Lemma (valuation game).** Let $S=(s_1,\dots,s_N)$ be a multiset of non-negative integers. Define a move as choosing two entries and replacing them by $(\min,|\,-|)$ as in $(\star)$. Then from any $S$, every sequence of moves terminates, and the terminal multiset has the form $(0,0,\dots,0,g)$ where
$$g \;=\; \gcd(s_1,\dots,s_N)$$
(with $\gcd$ taken to be the gcd of all entries, using the convention $\gcd(0,\dots,0)=0$; equivalently gcd of the positive entries, ignoring zeros).

**Proof.** Define $E(S)=\sum_i s_i$ and $Z(S)=$ number of zero entries.

*Termination.* Consider the lexicographic pair $(E,\,-Z)$. A move on $(a,b)$ changes the sum by $\max(a,b)-(a+b)=-\min(a,b)\leq 0$; it is strictly negative when both entries are positive. The number of zero entries can change: if exactly one of $a,b$ is $0$, the move gives $(0,|a-b|)$ — one stays zero, the other stays positive, so $Z$ is unchanged and $E$ is unchanged. If both positive, $E$ strictly decreases. Hence **$(E,-Z)$ strictly decreases lexicographically at every move**: either $E$ drops (both entries positive) or $E$ stays equal and... we must check the "exactly one zero" case cannot loop. In that case the move is $(a,0)\to(0,a)$ — it merely swaps the zero and nonzero between the two positions, and **all other entries are untouched**, so the sorted multiset is unchanged. Thus such a move does not change the state up to permutation. For termination of *states*, we may ignore permutation-trivial moves; every non-trivial move strictly decreases $E\geq 0$. Hence termination.

*Terminal value.* At a terminal multiset, no move with two positive entries is possible (else $E$ could drop), so **at most one entry is positive**; the terminal multiset is $(0,\dots,0,g)$. By the gcd-invariance noted above, $g=\gcd(s_1,\dots,s_N)$, which is independent of the path. $\square$

---

### Step 3 — Coupling the primes: termination of the full game (Part (a))

The full board is a single object; one move acts on all primes at once, so we cannot run the per-prime games independently. We use the global quantity
$$\Phi \;=\; \sum_{i=1}^{N} \Omega(a_i), \qquad \Omega(x)=\text{(number of prime factors of }x\text{, with multiplicity)}.$$

For a move on $m=a_i$, $n=a_j$, summing the per-prime change $\Delta_p=-\min(v_p(m),v_p(n))$ over all primes gives
$$\Phi_{\text{new}}-\Phi_{\text{old}} \;=\; -\sum_p \min(v_p(m),v_p(n)) \;=\; -\Omega(\gcd(m,n)) \;\leq\; 0.$$

So $\Phi$ is non-increasing. A move leaves $\Phi$ unchanged **only if** $\gcd(m,n)=1$. In that coprime case the new pair is $(1, mn)$: one of the two positions becomes $1$, the other becomes $mn$. Thus a $\Phi$-preserving move **strictly decreases the number of positions holding a value $>1$** (two such positions become one).

Now run any sequence of moves. Consider the pair $(\Phi,\, C)$ where $C$ is the number of entries $>1$. Between two consecutive moves, either $\Phi$ drops, or $\Phi$ is constant and $C$ drops by $1$. Since $\Phi\geq 0$ is bounded below and a fixed $\Phi$ can accompany at most finitely many $C$-drops ($C\le N$), after finitely many moves we must stop being able to make $\Phi$-constant moves — but more directly:

**Claim.** The process cannot continue forever. Suppose it did. Since $\Phi$ is a non-negative integer and non-increasing, it eventually stabilizes at some value $\Phi_0$. Thereafter every move is coprime, so each move reduces $C$ by exactly $1$. After at most $N-1$ such moves, $C\le 1$ and no move (which requires two entries $>1$) is possible — contradiction with "continues forever."

Hence **the process terminates**. At termination, no two entries exceed $1$, so **at most one entry exceeds $1$**. Finally, at least one entry exceeds $1$: if all entries were $1$, then $\Phi=0$; but $\Phi$ started at $\sum\Omega(a_i)\geq N\cdot 1 = 2026>0$ (each $a_i>1$), and $\Phi$ can reach $0$ only if every entry is $1$, which would require each $\Omega(\gcd)\geq 1$ drop to erase $2026$ units — possible in total, but let me argue termination state has $\geq 1$ entry $>1$ more cleanly:

Actually, $\Phi$ is non-increasing but the final $\Phi$ equals $\Omega$ of the single remaining $>1$ entry. The product $\prod_i a_i$ — let me check invariance of the product:

Let me reconsider the termination state carefully. The cleaner statement: at termination, no move is possible, which means fewer than two entries are $>1$. Combined with the per-prime invariants, I'll pin down that exactly one entry is $>1$. Let me think about why not all entries become $1$.

For a prime $p$ dividing at least one initial entry, consider $g_p = \gcd$ of all $v_p(a_i)$ over the entries (positive ones; if exactly one entry has $p$, $g_p = v_p$ of that entry $\geq 1$). The valuation lemma shows that throughout the game, the multiset of $p$-valuations has the same gcd $g_p$, and at termination has the form $\{0,\dots,0,g_p\}$. So at termination, $p$ divides exactly one entry, to the power $g_p \geq 1$. Therefore **every prime that initially appeared still appears in exactly one terminal entry** — so the terminal board is **not** all $1$s.

This also shows there is exactly **one** entry $>1$: if two terminal entries $u,v>1$ existed, both being $>1$ means a move is still possible — contradiction. Hence the terminal state has a single entry $M>1$, with $v_p(M)=g_p$ for every $p$. This completes Part (a).

But wait — I need to be careful that the per-prime valuation lemma applies *even though moves are coupled*. Let me verify the key point: the **multiset of $p$-valuations evolves by the rule $(\star)$ regardless of what happens at other primes**, because a move on positions $i,j$ updates $v_p$ at exactly those positions by $(\star)$, independent of other primes. The *choice* of which positions to move is influenced by other primes, but that doesn't matter: **whatever sequence of position-pairs is chosen, the induced sequence of $p$-valuation multisets is a legal play of the valuation game.** Hence the valuation lemma applies, and at termination the $p$-valuation multiset is $\{0,\dots,0,g_p\}$.

Let me now confirm termination of the *full* game rigorously once more and confirm the invariant $g_p$ — and double-check the subtle point that the full game actually does terminate (Part (a)) using the $(\Phi, C)$ argument, which I've now verified is correct.

Let me also verify the claim "terminal ⇒ at most one entry > 1" rules out the all-ones board via the per-prime argument, with one more computational sanity check on edge cases (all entries equal; two entries coprime; etc.):

All 50000 random trials and edge cases pass: terminal $M$ always matches the formula, and there is always exactly one entry $>1$.

One more rigorous check on the termination argument — I want to make sure the "$(\Phi, C)$ lexicographic decrease" is truly airtight, including that a $\Phi$-preserving move strictly decreases $C$:

All mechanics verified. The proof is complete and airtight. Let me write it up cleanly.

---

# Solution

Let the integers on the board be $a_1,\dots,a_{2026}$ (the count stays fixed at $N=2026$). For a prime $p$ write $v_p(x)$ for the $p$-adic valuation, and let $\Omega(x)=\sum_p v_p(x)$.

## A per-prime lemma

**Lemma.** Fix a prime $p$ and let $s_i=v_p(a_i)\geq 0$. Under any move, the induced operation on the multiset $\{s_1,\dots,s_N\}$ is the *subtraction–Euclid* rule: a chosen pair $(s_i,s_j)=(a,b)$ becomes
$$(a,b)\;\longmapsto\;\bigl(\min(a,b),\,|a-b|\bigr). \tag{$\star$}$$
Consequently, throughout the entire process, $\gcd(s_1,\dots,s_N)$ is invariant.

*Proof of the operation.* For the chosen entries $m,n$,
$$v_p(\gcd(m,n))=\min(a,b),\qquad v_p\!\Bigl(\tfrac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\Bigr)=\max(a,b)-\min(a,b)=|a-b|.$$
For the invariant: $\gcd(\min(a,b),|a-b|)=\gcd(a,b)$, so the gcd of the two touched entries — hence of the whole multiset — is unchanged. $\square$

We will also use two simple inequalities for $(\star)$, valid for all $a,b\geq 0$:
$$\min(a,b)+|a-b|=\max(a,b)\leq a+b,\quad\text{with strict inequality iff }a,b>0. \tag{1}$$

## Part (a): termination with exactly one entry $>1$

Define the global potential
$$\Phi=\sum_{i=1}^{N}\Omega(a_i)=\sum_{p}\sum_{i=1}^{N}v_p(a_i)\;\geq\;0.$$

For a move on $m,n$, summing (1) over all primes (using the per-prime operation $(\star)$),
$$\Phi_{\text{new}}-\Phi_{\text{old}}=-\sum_{p}\min\bigl(v_p(m),v_p(n)\bigr)=-\Omega(\gcd(m,n))\leq 0. \tag{2}$$
Equality holds **iff** $\gcd(m,n)=1$.

Let $C$ be the number of entries $>1$. A move requires $C\geq 2$. Consider two cases for a move on $m,n>1$:

- If $\gcd(m,n)>1$: by (2) the non-negative integer $\Phi$ strictly decreases.
- If $\gcd(m,n)=1$: the new pair is $\bigl(1,\operatorname{lcm}(m,n)\bigr)=(1,mn)$. Two entries $>1$ are replaced by $1$ and $mn>1$, so **$C$ decreases by exactly $1$**, while $\Phi$ is unchanged.

Track the pair $(\Phi,-C)$ in lexicographic order. It strictly decreases at every move: either $\Phi$ drops, or $\Phi$ is constant and $C$ drops by $1$. Since $\Phi\geq 0$ is an integer and, between two drops of $\Phi$, the value $C$ (an integer $\leq N$) can drop only finitely many times, the process **must terminate** after finitely many moves.

At termination no move is possible, i.e. $C<2$: **at most one entry exceeds $1$.** It remains to rule out $C=0$ (all entries equal to $1$). Pick any prime $p$ dividing at least one initial entry, and let $g_p=\gcd\{v_p(a_i)\}\geq 1$ (this gcd is taken over all entries; equivalently over the positive ones, and $g_p\geq 1$ since some entry is divisible by $p$). By the Lemma this gcd is invariant, so the terminal multiset of $p$-valuations has gcd $g_p\geq 1$; in particular at least one terminal entry is divisible by $p$. Hence the board is **not** all $1$'s.

Combining: **exactly one entry $M>1$ remains.** $\quad\blacksquare_{(a)}$

## Part (b): $M$ is independent of the choices

Keep, for each prime $p$, the invariant
$$g_p:=\gcd\bigl\{v_p(a_1),\dots,v_p(a_N)\bigr\}=\gcd\bigl\{v_p(a_i):v_p(a_i)>0\bigr\},$$
computed at the **initial** board (and hence, by the Lemma, equal to the same gcd at every later board, in particular at termination).

At termination, by part (a), the board is $(1,1,\dots,1,M)$. The multiset of $p$-valuations is therefore $\{0,0,\dots,0,\,v_p(M)\}$, whose gcd is $v_p(M)$. By invariance this equals $g_p$. Thus
$$\boxed{\;v_p(M)=g_p=\gcd\bigl\{v_p(a_i):v_p(a_i)>0\bigr\}\;}\qquad\text{for every prime }p,$$
and consequently
$$\boxed{\;M\;=\;\prod_{p\text{ prime}}p^{\,g_p}\;=\;\prod_{p\,\mid\,\prod_i a_i}p^{\,\gcd\{v_p(a_i)\,:\,v_p(a_i)>0\}}\,.}$$

The right-hand side depends **only on the initial board**, not on any choices made by Confucius. Therefore the value of $M$ is independent of the moves chosen. $\quad\blacksquare_{(b)}$

---

### Summary of the two key ideas

1. **Per-prime reduction to subtraction–Euclid.** Under a move, the $p$-adic valuations of the two touched entries undergo $(a,b)\mapsto(\min(a,b),|a-b|)$ — one Euclidean step — and this holds *independently for every prime*, regardless of how the position-pair is chosen. The gcd of the valuation multiset is therefore an invariant for each prime.

2. **Global termination via $(\Phi,C)$.** The total $\Omega$-mass $\Phi=\sum\Omega(a_i)$ never increases, drops strictly whenever the chosen pair is non-coprime, and is preserved (with the count $C$ of large entries dropping by exactly $1$) whenever the pair is coprime. The lexicographic pair $(\Phi,-C)$ strictly decreases at every move, forcing termination; the per-prime invariant then pins down the unique survivor $M=\prod_p p^{g_p}$.

Both parts are thus established. $\blacksquare$