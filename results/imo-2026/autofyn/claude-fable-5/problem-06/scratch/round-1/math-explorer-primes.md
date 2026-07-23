## imo-2026-06 (prime factorization and sieve structure lens)

### What the problem is really asking

$a_{n+1}$ is the smallest integer $> a_n$ such that $\gcd(a_{n+1}, a_i) > 1$ for EVERY $i \leq n$. In prime-factorization language: the prime set of $a_{n+1}$ must INTERSECT the prime set of each previous element. This is a **hitting-set / transversal condition** on primes.

### Key structural object: the constraint antichain $E_n$

Define $E_n$ = the **antichain of minimal prime sets** among $\{a_1, \ldots, a_n\}$: a set $F \subseteq \text{primes}(a_i)$ is in $E_n$ iff no other $a_j$'s prime set is a proper subset of $F$. Then:

- $m$ is **valid** for step $n+1$ iff $\text{primes}(m)$ intersects every $F_i \in E_n$.
- Redundant constraint: if $\text{primes}(a_i) \supseteq \text{primes}(a_j)$, then the constraint from $a_i$ is implied by the constraint from $a_j$, so $a_i$ is redundant.
- The valid set $\mathcal{V}_n$ depends ONLY on $E_n$, not on the full sequence.

### Computational findings (verified)

For $a_1 = 15 = 3 \times 5$:
- $E_1 = \{\{3,5\}\}$
- $E_2 = \{\{3,5\},\{2,3\}\}$ (after $a_2 = 18 = 2 \times 3$)
- $E_3 = \{\{3,5\},\{2,3\},\{2,5\}\}$ (after $a_3 = 20 = 4 \times 5$) — **stabilizes here**

After stabilization with $E^* = \{\{2,3\},\{2,5\},\{3,5\}\}$, $L = 2 \times 3 \times 5 = 30$:
- Valid residues mod 30 = $\{0,6,10,12,15,18,20,24\}$ ($T = 8$ residues)
- These are exactly the integers mod 30 divisible by AT LEAST 2 OF $\{2,3,5\}$
- $a_{n+8} = a_n + 30$ for ALL $n \geq 1$ (verified computationally up to $n=40$)

For $a_1 = 77 = 7 \times 11$: stabilizes at $E^* = \{\{2,7\},\{2,11\},\{7,11\}\}$, $L = 154$, $T = 18$.

For $a_1 = 6 = 2 \times 3$: $a_2 = 8 = 2^3$ has prime set $\{2\} \subsetneq \{2,3\}$, so $E^* = \{\{2\}\}$, $L = 2$, $T = 1$ (all even numbers).

### The critical "self-consistency" property

$E^*$ is **self-consistent** if every valid integer $m$ has $\text{primes}(m)$ CONTAINING some $F_i \in E^*$ (i.e., $m$ is dominated). Self-consistency means:
- Any new element $a_k$ (for $k > N$) is dominated: $\text{primes}(a_k) \supseteq F_j$ for some $F_j \in E^*$.
- The constraint from $a_k$ ("hit $\text{primes}(a_k)$") is WEAKER than the constraint from $F_j$ ("hit $F_j$"), since $F_j \subseteq \text{primes}(a_k)$.
- Therefore, adding $a_k$ does NOT change the valid set: $\mathcal{V}_{k} = \mathcal{V}_{k-1}$.

**VERIFIED:** For $a_1 = 15$, once $E^*$ is reached at $n=3$:
- All valid residues mod 30 are dominated (no non-dominated valid residues exist mod 30).
- Every sequence element from $n=4$ onward has prime set containing $\{2,3\}$, $\{2,5\}$, or $\{3,5\}$.
- The valid set $\mathcal{V}$ is constant from $n=3$ onward.

### Why the sequence becomes arithmetic-periodic (ONCE $E^*$ is stable)

Once $\mathcal{V}_n$ stabilizes to $\mathcal{V}$ (a fixed set of integers):
1. $\mathcal{V}$ is **periodic** with period $L = \prod_{p \in \bigcup E^*} p$: it's determined by which primes from $\bigcup E^*$ divide $m$, which is a residue condition mod $L$.
2. $\mathcal{V}$ has exactly $T$ residue classes mod $L$ (the valid residues), call them $r_0 < r_1 < \ldots < r_{T-1}$.
3. The elements of $\mathcal{V}$ in increasing order form the sequence $r_j + kL$ for $k = 0, 1, 2, \ldots$ (in cycling order through $j = 0, \ldots, T-1$).
4. The greedy picks these in order: $a_{n+T} = a_n + L$ for all $n$ large enough.
5. **Key fact:** The greedy function satisfies $f(m+L) = f(m) + L$ for all $m \geq $ some threshold, directly from the periodicity of $\mathcal{V}$ mod $L$.

### The HARD GAP: Why does $E_n$ reach a self-consistent state?

This is the central obstacle. For small starting values, it happens in $O(10)$ steps. For large starting values (e.g., $a_1 = 3 \times 5 \times 7 \times 11 \times 13 = 15015$), the antichain grows slowly with the sequence and involves very large primes (up to 2500+ by step 150 of the computation), but the computation is too slow to see stabilization.

**What makes stabilization hard to prove:**
- New primes can enter the antichain at any step (the antichain doesn't have a bounded prime universe from the start).
- The antichain can grow (new elements incomparable to existing ones) or shrink (new elements that are proper subsets of existing ones).
- A new antichain element $F$ requires the element $a_k$ to "hit" each existing antichain element while avoiding at least one prime from each — this is a very specific structure.

**Potential proof approaches for stabilization:**
- **Dickson/Higman argument**: The antichain of finite sets of primes is well-quasi-ordered; any descending chain stabilizes. But the antichain changes in both directions (grows and shrinks), so direct application needs care.
- **Density/sieve argument**: The density of "non-dominated valid integers" within $\mathcal{V}$ is controlled. As the antichain grows, dominated elements become more common and the greedy eventually always picks dominated elements. (Needs formalization.)
- **Size bound on antichain elements**: The minimum non-dominated valid integer above $m$ grows with the antichain size. Once this minimum exceeds the minimum dominated valid integer in the same region, the greedy always picks dominated elements.
- **Direct construction**: Exhibit an explicit $N$ (depending on $a_1$) after which the greedy always picks dominated elements. This might use the structure of the initial terms.

### What $L$ and $T$ are (structurally)

$L$ = product of all primes appearing in the eventual antichain $E^*$. This equals the product of all "essential primes" (those that appear in MINIMAL prime sets of sequence elements, not just any prime appearing in the sequence). The large primes that enter via "dominated" elements (like $7$ in $42 = 2 \times 3 \times 7$ for the $a_1 = 15$ case) do NOT contribute to $L$.

$T$ = number of residue classes mod $L$ that: (a) are not coprime to $L$, and (b) have prime set hitting every element of $E^*$. This is the count of "valid residues" mod $L$.

### Distinct openings for the outliner

1. **Antichain stabilization via explicit bound**: Show the greedy algorithm, after a finite initial segment, always produces elements dominated by the current antichain. The bound might come from: the minimum non-dominated valid integer growing faster than the minimum dominated valid integer as the antichain grows. This gives a "crossing point" after which only dominated elements are picked.

2. **Direct periodicity via state-machine (bypassing antichain)**: Show the sequence of residues $a_n \bmod M$ (for $M = $ lcm of first few elements, or product of primes in initial terms) is eventually periodic. Once the residue sequence is periodic, so is the sequence itself. This might use the fact that there are only finitely many residue classes, giving eventual periodicity via Pigeonhole (in the "residue space").

3. **The "smooth subsequence" approach**: Show there's a subsequence $a_{n_1}, a_{n_2}, \ldots$ with $n_{k+1} - n_k$ bounded and each $a_{n_k}$ is "smooth" (divisible by ALL primes in $\bigcup E_{n_k}$). The smooth elements' residues mod $L$ determine the whole sequence's structure.

4. **Contradiction approach for non-stabilization**: If the antichain grew indefinitely, the density of valid integers would approach 0 (since increasingly many residue classes become forbidden). But the greedy always finds a next element, contradicting density → 0. This bounds the antichain size and gives stabilization.

### Dead ends to avoid

- **Trying to show the prime support literally stabilizes** (no new primes ever enter the sequence): FALSE. New primes keep entering (e.g., 7, 11, 13, ... in the $a_1 = 15$ case). The correct statement is that new primes enter only via "dominated" elements, not as new antichain elements.
- **Working with the LCM of all elements**: This grows without bound and is not the right $L$.
- **Assuming the gaps $a_{n+1} - a_n$ are constant**: They oscillate (e.g., for $a_1 = 15$ the diffs cycle $[3,2,4,6,6,4,2,3]$), not constant.

### Prior progress

None — first round.

### Candidate knowledge-base entries

- **Divisor analysis**: tracking gcd structure and prime support of sequence elements.
- **Linear recurrences / eventual periodicity**: sequences eventually periodic mod $m$.
- **Pigeonhole / extremal principle**: finite state space forcing eventual repetition.
- **Invariants & monovariants**: the antichain as a "quasi-invariant" (eventually constant).
- **Bertrand's postulate**: might be used to bound the structure of new primes entering the antichain.
- **CRT / Modular arithmetic**: the valid set mod $L$ is determined by which primes from $\bigcup E^*$ divide each residue.

### Analogous past problems (cruxes)

1. **aimo-0678** (`number_theory/modular-arithmetic-and-CRT`): "Once one coordinate of a coupled integer recurrence is bounded, reduce the other coordinate modulo the lcm of the bounded coordinate's attainable values, turning the state pair into a deterministic map on a finite set." This is structurally analogous: once the valid set stabilizes (the "bounded coordinate"), reducing the sequence modulo $L$ gives a deterministic finite-state map. The crux move — reduce to a finite state space once one component is constrained — is directly applicable.

2. **aimo-0477** (`number_theory/divisibility-and-gcd`): "Track gcd(fixed term, current term) and show it divides the next one, producing a divisor-chain bounded by the fixed term that must stabilize." The antichain stabilization is analogous: the gcd constraint chain is bounded and must stabilize. The technique of "ascending chain of divisors of a fixed element stabilizes" mirrors our "ascending/changing chain of antichains stabilizes."

3. **aimo-0514** (`combinatorics/processes-and-algorithms`): "Show a deterministic process is reversible so its state graph is a union of cycles, forcing the orbit to be purely periodic." While our sequence grows (not cyclic), the idea of reducing to a finite deterministic state machine (once the valid set is periodic mod $L$) is the same crux.

### Small-case intuition notes (labeled as conjectures)

- **Conjecture (strongly supported by computation):** The antichain $E_n$ always stabilizes to a self-consistent antichain $E^*$ after finitely many steps. This conjecture is the KEY hypothesis the proof must establish.
- **Conjecture:** $L = \prod_{p \in \bigcup E^*} p$ and $T = $ number of residues mod $L$ divisible by at least one pair of primes from each element of $E^*$.
- **Conjecture:** The periodicity $a_{n+T} = a_n + L$ holds from $n = 1$ (not just "eventually"), at least for simple starting values like $a_1 = 15$.
- **Observation:** For starting values that are prime powers ($a_1 = p^k$), the antichain immediately reduces to $\{\{p\}\}$ and the sequence is the arithmetic progression of multiples of $p$.
- **Observation:** For $a_1$ a product of $k$ distinct primes, the antichain can involve many elements (size up to $k$ or more), and larger starting values make the transient longer.
