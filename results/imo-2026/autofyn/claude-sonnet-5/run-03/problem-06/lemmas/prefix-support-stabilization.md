## Lemma (Prefix-Support Stabilization)

For a prime $p$ and modulus $M\ge1$, and $n\ge1$, let
$$S_n(p,M):=\{r\in\mathbb Z/M\mathbb Z : \exists i\le n,\ i\equiv r
\!\!\pmod M,\ p\mid a_i\}\subseteq\mathbb Z/M\mathbb Z.$$
Then $(S_n(p,M))_{n\ge1}$ is non-decreasing under $\subseteq$ and hence
stabilizes: there is $n_0(p,M)$ with $S_n(p,M)=S_\infty(p,M)$ for all
$n\ge n_0(p,M)$. For a finite prime set $Q$ and fixed $M$, taking
$n_1(Q,M):=\max_{p\in Q}n_0(p,M)$, stabilization holds simultaneously for
every $p\in Q$ once $n\ge n_1(Q,M)$.

### Proof
Adding index $n+1$ to the prefix can only add the single residue
$(n+1)\bmod M$ to $S_n(p,M)$ (if $p\mid a_{n+1}$) or leave it unchanged, so
$S_n(p,M)\subseteq S_{n+1}(p,M)$. This is a non-decreasing chain of subsets
of the fixed finite set $\mathbb Z/M\mathbb Z$ (size $M$), so it can
strictly increase at most $M$ times, hence stabilizes. The simultaneous
statement for finite $Q$ follows by taking the max of finitely many
individual stabilization indices. $\blacksquare$

### Content and limits
Generalizes the trivial fact that the "universally-dividing prime set" $U_n$
(primes of $R(a_1)$ dividing *every* term so far) is non-increasing and
stabilizes: taking $M=1$ recovers a one-way ("divides *some* term")
weakening of $U_n$. The genuinely new content is tracking a *union of
residue classes* rather than a single membership bit. This lemma only says
the set of *ever-observed* hit residues stops growing — it does **not**
assert $p$ divides every term at those residues from then on (that would be
an actual periodicity claim, unproved).

### Provenance
Proved in `approaches/frozen-invariant-monovariant.md`, §2.1, round 5.
Independently re-derived by the proof-reviewer; standard finite-monotone-
stabilization argument, no gap.
