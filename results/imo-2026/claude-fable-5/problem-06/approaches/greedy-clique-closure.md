## Status
partial

## Approach outline

**Framing.** Work with the *limit object*: the fixed set $V_\infty = \{m > 1 : \gcd(m, a_i) > 1 \text{ for all } i \ge 1\}$ and the set of terms $A = \{a_1, a_2, \dots\}$. Show the sequence is exactly the increasing enumeration of $V_\infty \cap [a_1, \infty)$, then show $V_\infty$ is an *exactly periodic* set (a union of residue classes mod some $L$), which yields $a_{n+T} = a_n + L$ for **every** $n \ge 1$ (no transient — verified computationally for $a_1 = 15, 35, 77, 91, 105$).

The route: Clique → Bounded gaps → Reduction Lemma → Finite essential antichain (the hard gap, attacked by a density/first-moment argument) → Exact periodicity of $V_\infty$ → Greedy on a periodic set.

### Step 1: Clique Lemma
Any two distinct terms satisfy $\gcd(a_m, a_n) > 1$. — Immediate from the definition: for $m > n$, $a_m$ was chosen with $\gcd(a_m, a_i) > 1$ for all $i < m$, in particular $i = n$. (Provable in two lines; candidate for `lemmas/clique.md`.)

### Step 2: Universal validity of multiples, bounded gaps
For **every** term $a$ of the sequence, every multiple $m$ of $\mathrm{rad}(a)$ (with $m > 1$) satisfies $\gcd(m, a_i) > 1$ for all $i$. — Mechanism: by Step 1, $a_i$ shares some prime $p$ with $a$; then $p \mid \mathrm{rad}(a) \mid m$, so $\gcd(m, a_i) \ge p > 1$. Consequently, at every stage the next multiple of $\mathrm{rad}(a_1)$ is a valid candidate, so
$$a_{n+1} - a_n \le B := \mathrm{rad}(a_1) \quad \text{for all } n,$$
and hence $A$ has lower density $\ge 1/B$ in every long interval: $|A \cap [x, x+y]| \ge \lfloor y/B \rfloor$. Moreover every multiple of $\mathrm{rad}(a)$ that is $\ge a_1$ is itself a **term** (by Step 3). (Provable; candidate for `lemmas/bounded-gaps.md`.)

### Step 3: Reduction Lemma (the sequence enumerates $V_\infty$)
$a_{n+1} = \min\{m \in V_\infty : m > a_n\}$ for every $n$; consequently $A = V_\infty \cap [a_1, \infty)$ and the sequence is its increasing enumeration. — Mechanism: (i) every term lies in $V_\infty$: for $i < k$, $\gcd(a_k, a_i) > 1$ by definition of $a_k$; for $i > k$, by definition of $a_i$; and $\gcd(a_k, a_k) > 1$. (ii) Let $V_n = \{m > a_n : \gcd(m, a_i) > 1,\ i \le n\}$; then $V_\infty \cap (a_n, \infty) \subseteq V_n$, so $\min V_\infty \cap (a_n,\infty) \ge \min V_n = a_{n+1}$; but $a_{n+1} \in V_\infty \cap (a_n, \infty)$ by (i), forcing equality. Also $a_1 \in V_\infty$. (Provable; candidate for `lemmas/reduction.md`. This kills all worry about "old constraints being forgotten" — the constraint set is the fixed infinite family $\{\mathrm{primes}(a_i)\}_{i \ge 1}$.)

### Step 4: Finite essential antichain — **[GAP: the crux]**
Let $\mathcal{F} = \{\mathrm{primes}(a_i) : i \ge 1\}$ and let $E_\infty$ be the set of inclusion-minimal members of $\mathcal{F}$. Since each member is a finite set, every member contains a minimal member (take an inclusion-minimal member among the finitely many members contained in it), so
$$V_\infty = \{m > 1 : \mathrm{primes}(m) \cap F \neq \emptyset \ \text{ for all } F \in E_\infty\}.$$
**Claim (GAP): $E_\infty$ is finite.**

Ammunition for the builder (all provable inputs):
- Every $F \in E_\infty$ is the prime set of a term, so by Step 2 (applied with the density bound), $A \subseteq \bigcup_{p \in F} p\mathbb{Z}$, hence counting multiples in $[x, 2x]$: $\sum_{p \in F} 1/p \ge 1/B - o(1)$, so $\sum_{p \in F} 1/p \ge 1/B$. In particular every $F \in E_\infty$ contains a prime $\le B \cdot |F|$, and more usefully the *small-prime part* of $F$ carries at least density weight $1/B - \sum_{p > z} (\text{contribution})$.
- Members of $E_\infty$ pairwise intersect (Step 1) and are pairwise incomparable (minimality).
- Joint density bound: for any $F_1, \dots, F_k \in E_\infty$, $A \subseteq \bigcap_j \bigcup_{p \in F_j} p\mathbb{Z}$, so
  $$\frac{1}{B} \le \sum_{(p_1, \dots, p_k) \in F_1 \times \dots \times F_k} \frac{1}{\mathrm{lcm}(p_1, \dots, p_k)}.$$
  If the $F_j$ were "spread out" (transversals mostly with distinct primes), the right side would decay geometrically in $k$; so large subfamilies must concentrate on a common small kernel. Suggested plan: fix a threshold $z$ (e.g. a function of $B$), split each $F$ into $F^{\le z} \cup F^{>z}$, show that (a) only finitely many distinct $F^{\le z}$ occur (trivial), and (b) at most finitely many $F \in E_\infty$ have $F^{>z} \neq \emptyset$ playing an essential role — e.g. show that if infinitely many minimal $F$ share the same small part $F^{\le z}$ but differ in large primes, then the constraint "$\text{hit } F$" is implied for all sufficiently large candidates by "hit $F^{\le z}$", contradicting minimality/essentiality; this is where the greedy minimality (a term with a large prime was chosen because everything smaller was invalid) must be used.
- Alternative sub-route for the same gap: the monovariant $B^*_n = \min_{i \le n} \mathrm{rad}(a_i)$ is a non-increasing positive integer, hence eventually constant $= B^*$; all bounds above improve from $B$ to $B^*$, and the term $a^*$ realizing $B^*$ gives a fixed finite prime set $\mathrm{primes}(a^*)$ hit by *every* term.

### Step 5: Exact periodicity of $V_\infty$
Assume Step 4. Let $P = \bigcup_{F \in E_\infty} F$ (finite), $L = \prod_{p \in P} p$. For $m > 1$: whether $\mathrm{primes}(m)$ hits $F \subseteq P$ depends only on $\gcd(m, L)$, i.e. only on $m \bmod L$. — Mechanism: $p \in F \Rightarrow p \mid L$, and $p \mid m \iff p \mid \gcd(m \bmod L$ lifted$, L)$. Hence $V_\infty \cap (1, \infty) = \{m > 1 : m \bmod L \in R\}$ where $R = \{r \in \mathbb{Z}/L : \gcd(r, L) \text{ has a prime factor in every } F \in E_\infty\}$. $R \neq \emptyset$ ($0 \in R$ via multiples of $L$). Exactly periodic in both directions: $m \in V_\infty \iff m + L \in V_\infty$ (for $m > 1$).

### Step 6: Greedy enumeration of a periodic set is arithmetic-periodic
Let $T = |R|$. The increasing enumeration $x_1 < x_2 < \dots$ of $\{m \ge a_1 : m \bmod L \in R\}$ satisfies $x_{n+T} = x_n + L$ for all $n \ge 1$. — Mechanism: the map $m \mapsto m + L$ is an order-preserving bijection of this set onto its elements $\ge a_1 + L$, and each window $[x, x+L)$ contains exactly $T$ elements. Since $a_1 \in V_\infty$ (so $a_1 \bmod L \in R$) and by Step 3 the sequence is exactly this enumeration, $a_{n+T} = a_n + L$ for **every** $n \ge 1$. $\blacksquare$

## Current best
Steps 1, 2, 3, 5, 6 are complete-modulo-writing (mechanisms verified, computationally sanity-checked on $a_1 \in \{15, 35, 77, 91, 105\}$: exact periodicity from $n = 1$, gaps $\le \mathrm{rad}(a_1)$, antichains stabilize). The entire problem is reduced to Step 4: the family of inclusion-minimal prime sets among $\{\mathrm{primes}(a_i)\}$ is finite.

## Gaps remaining
- **Step 4 (crux):** finiteness of the minimal antichain $E_\infty$. Suggested attack: density/first-moment bounds ($\sum_{p \in F} 1/p \ge 1/B$ for every constraint, joint transversal bound for subfamilies), plus the greedy minimality to show large primes cannot appear in infinitely many minimal constraints.
- Minor: in Step 6, write out the enumeration argument rigorously (bijection $+L$, counting per window).

## Watch out for
- Do NOT claim the set of primes appearing in the sequence stabilizes — it does not (recorded explorer dead end). Only the *minimal* constraints stabilize.
- $|F|$ (number of prime factors of a term) is unbounded across terms; any bound used must not assume $|F| = O(1)$.
- The pairwise-intersecting + incomparable structure alone does NOT force finiteness (e.g. $\{x, y_i\}_{i\ge1}$); the density lower bound $1/B$ and greedy minimality are essential inputs.
