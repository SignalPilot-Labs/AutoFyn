## Lemma (Pairwise, not just consecutive, non-coprimality)

For the problem's greedy sequence $(a_n)$, $\gcd(a_i, a_j) > 1$ for **every**
pair of distinct indices $i \neq j$ (not merely for $i \le n$ against
$a_{n+1}$ as the raw problem statement suggests when read only "locally").

### Proof
WLOG $i < j$. By definition, $a_j = a_{(j-1)+1}$ is the smallest integer
exceeding $a_{j-1}$ such that $\gcd(a_j, a_k) > 1$ for **every** $k =
1,2,\ldots,j-1$. Since $i \le j-1$, this includes $k = i$, i.e.
$\gcd(a_j,a_i) > 1$. $\blacksquare$

(No induction is actually needed beyond directly unpacking the definition:
the definition already quantifies over all $k \le j-1$, so any $i<j$ is
covered directly.)

### Why this is worth stating separately
The problem statement's constraint is easy to mis-read as relating only
consecutive terms; this lemma makes explicit that it in fact gives, for a
fixed early index $i$, a constraint against **every** later term
simultaneously — which is exactly the fact needed to run pigeonhole
arguments (e.g. the "every term meets the recurring set $S$" lemma) treating
$i$ as fixed and letting $j \to \infty$.

### Provenance
Proved in `approaches/state-compactness-pigeonhole.md` (Lemma 1). Certified
by the proof-reviewer, round 1: correct, elementary, and used as an
ingredient (implicitly or explicitly) by every approach that runs a
pigeonhole argument fixing $i$ against the infinite tail.
