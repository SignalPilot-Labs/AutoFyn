## imo-2026-01

### Lens: TERMINATION / MONOVARIANT (part a primarily, part b also addressed)

---

### Stopping condition (precise)

A legal move requires BOTH chosen entries to be > 1. The process stops when no such pair exists, i.e., when **at most one board entry is > 1**. There is no other obstruction: if two entries are > 1 (even if they are equal or coprime), a move is always legal.

---

### Best monovariant

**W = (sum of Omega(x_i) over all i) + (count of x_i > 1)**

where Omega(n) = total number of prime factors of n counted with multiplicity (Omega(1)=0).

W is a non-negative integer. It strictly decreases by >= 1 at every legal move.

**Case analysis for a move (m, n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)) with m,n > 1:**
Write m = g*a, n = g*b where g = gcd(m,n), gcd(a,b) = 1. Outputs are g and a*b.

- **Case 1: g=1** (m,n coprime). Outputs are (1, m*n).
  - Omega change: Omega(1) + Omega(mn) - Omega(m) - Omega(n) = 0 + (Omega(m)+Omega(n)) - Omega(m) - Omega(n) = 0.
  - Count change: -1 (the output 1 is not > 1, losing one contributor).
  - W change: 0 + (-1) = **-1**.

- **Case 2: g > 1, m = n** (so a = b = 1). Outputs are (g, 1).
  - Omega change: Omega(g) + 0 - 2*Omega(g) = -Omega(g) <= -1.
  - Count change: -1 (output 1 is not > 1).
  - W change: -Omega(g) + (-1) <= **-2**.

- **Case 3: g > 1, m != n** (so max(a,b) >= 2, hence a*b >= 2 > 1). Outputs are (g, a*b), both > 1.
  - Omega change: Omega(g) + (Omega(a)+Omega(b)) - (Omega(g)+Omega(a)) - (Omega(g)+Omega(b)) = -Omega(g) <= -1.
  - Count change: 0 (both outputs > 1, same as both inputs > 1).
  - W change: -Omega(g) + 0 <= **-1**.

In all cases W decreases by at least 1. Since W >= 0, the process terminates after at most W_initial steps. W_initial = sum_i Omega(x_i) + 2026 is finite.

**Why the termination argument for W is complete:** W is a non-negative integer. It decreases by at least 1 per step. An infinite process would require W to decrease infinitely, contradicting W >= 0. So the process halts in finitely many steps.

---

### Why exactly ONE entry > 1 at termination (not zero)

At termination, at most 1 entry > 1 (stopping condition).

For each prime p, define **d_p = gcd(v_p(x_1), ..., v_p(x_2026))** where v_p(n) = p-adic valuation. (By convention gcd includes 0's: gcd(a,0) = a, so gcd = 0 only if all values are 0.)

**Key invariant (for part b):** d_p is preserved by every move. Proof: A move on (m,n) changes the pair of p-exponents from (a_p, b_p) to (min(a_p,b_p), |a_p-b_p|). The key identity is **gcd(min(a,b), |a-b|) = gcd(a,b)** — this is just the subtraction step of the Euclidean algorithm (gcd(a,b) = gcd(a, b-a)). The gcd of the pair is preserved. The gcd of the entire board (which factors as gcd(gcd of the pair, gcd of the rest)) is thus unchanged.

So d_p is the same before and after every move, equal to its initial value throughout.

**M := prod_p p^{d_p}** (finite product since d_p = 0 for all but finitely many primes).

Since all initial x_i > 1, take x_1: it has a prime factor p_1, so v_{p_1}(x_1) > 0, hence d_{p_1} = gcd(v_{p_1}(x_1), ...) >= 1 (since gcd(a, 0,...,0) = a > 0 when a > 0). Thus M >= p_1^{d_{p_1}} >= p_1 >= 2 > 1.

If the process ended with 0 entries > 1 (all = 1), then gcd(0,...,0) = 0 = d_{p_1} — contradicting d_{p_1} >= 1. So the process cannot end with 0 entries > 1.

Therefore the process ends with **exactly 1** entry > 1. That entry is M: if the single entry > 1 is y, then v_p(y) = gcd(v_p(y), 0,...,0) = d_p (invariant), so y = prod_p p^{d_p} = M.

---

### Candidate techniques from knowledge_base.md

- **Invariants & monovariants** (Combinatorics section): exactly this technique; W is the monovariant and d_p is the invariant.
- **Divisor analysis / p-adic valuation** (Number Theory section): the v_p structure on board entries is the heart of the proof.
- **Direct proof** + **casework/exhaustion** (General Proof Methods): the 3-case W analysis is direct casework.
- The identity gcd(a,b) = gcd(a, b-a) is an elementary number theory fact, used as the key step.

---

### Distinct openings for the outliner

1. **W = Omega-sum + count monovariant (RECOMMENDED MAIN APPROACH)**: As described above. Clean 3-case argument. Simultaneously proves termination and gives M > 1 for the "exactly one" conclusion. This is the most direct attack and probably the intended solution.

2. **Product monovariant (weaker alone, combine)**: P = product of all board entries satisfies P_after = P_before * lcm(m,n)/(m*n) = P_before / gcd(m,n). So P is non-increasing (strictly at gcd>1 moves, flat at gcd=1 moves). Alone this doesn't prove termination (gcd=1 moves could run indefinitely). But: at gcd=1 moves, the count of entries >1 decreases by 1. The combination P + N_{>1} in some form is equivalent to W.

3. **Per-prime argument**: Track each prime p independently. For prime p, the multiset {v_p(x_i) : i=1,...,N} evolves by the subtraction-GCD step on two chosen entries. This multiset's sum (= sum_i v_p(x_i)) strictly decreases when both chosen entries have v_p > 0, and is unchanged otherwise. The process for prime p terminates (reaches at most one nonzero entry) because: the sum is a non-negative integer that decreases each time both entries have v_p > 0, and when it stops decreasing for p, any remaining gcd=1 moves reduce the count of entries > 1. This per-prime view naturally gives the invariant for part (b). Slightly more technical but very illuminating.

4. **Sum of entries is NOT a monovariant** (dead-end to avoid): gcd=1 move on (m,n) -> (1, mn) can increase the max entry. E.g., (2,3) -> (1,6): sum goes 5 -> 7. So sum is not a monovariant.

5. **LCM of all entries is non-increasing but not strict**: LCM(g, a*b) = g*a*b/gcd(g,a*b) <= g*a*b = lcm(m,n). Non-increasing. But can be flat. Not a strict monovariant alone.

---

### Analogous past problems (cruxes)

1. **aimo-0193** [combinatorics:invariants-and-monovariants]: "Several positive integers in a row; operation on adjacent pair (x>y left of y) replaces with (y+1,x) or (x-1,x). Prove only finitely many iterations." Crux: use a strictly increasing monovariant S = sum i*a_i (weighted position sum) bounded above by (1+2+...+n)*M where M = max (invariant). Direct parallel: monovariant for a process on a sequence of integers. Analogous because: a process on a finite multiset of integers terminates by a monovariant strictly increasing/decreasing.

2. **aimo-0295** [combinatorics:invariants-and-monovariants]: "Social network refriending event: A friends B and C, B and C not friends; replace A-B, A-C friendships with B-C. Prove terminates in finite steps." Crux: edge count strictly decreases each move (one edge added, two removed = net -1). Terminated exactly because the integer monovariant (edge count) is non-negative. Analogous: monovariant for a process termination, same structural argument.

3. **aimo-0236** [combinatorics:invariants-and-monovariants]: "Token game with addition/halving; p-adic valuation threshold." Crux: p-adic valuation provides a monovariant for termination. Closely analogous because: uses v_p as the key quantity for both termination and invariance, exactly what d_p = gcd(v_p(x_i)) does here.

The closest analogy in structure (not just subtopic): **aimo-0295** for the pure termination argument, and **aimo-0236** for the p-adic invariant viewpoint.

---

### Prior progress

None. Empty approach population; Status unsolved.

---

### Dead ends (do not retry)

- **Sum of entries as monovariant**: fails (gcd=1 moves can increase the maximum and sum).
- **Product of entries as sole monovariant**: not strictly decreasing at gcd=1 moves. Valid only as non-strict.
- **LCM of entries as sole monovariant**: non-increasing but not strictly decreasing at all moves.

---

### Small-case / intuition notes (all labeled as conjecture verified computationally)

- Conjecture (verified for many cases): M = prod_p p^{gcd(v_p(x_1),...,v_p(x_N))} where the gcd is taken over the initial board. Verified: (4,6)->M=6, (8,12,18)->M=6, (6,10,15)->M=30, (4,8)->M=2, (36,48,60)->M=60, (2,3,5,7)->M=210. All correct.

- Key identity (proved): gcd(min(a,b), |a-b|) = gcd(a,b) for all non-negative integers a,b. This is the core of both the W analysis (Omega decreases) and the d_p invariance. Verified computationally and by elementary GCD theory.

- The monovariant W strictly decreases by exactly 1 at "pure subtraction" steps (when Omega(g)=1 and count unchanged or gcd=1 steps), and by 2 or more at "big reduction" steps. Verified on several random sequences.

- The case 2026 entries is not special; the proof works for any N >= 2 initial entries all > 1.

---

### Summary for the outliner

The proof of (a) uses W = sum Omega(x_i) + count_{x_i > 1} as a strict monovariant (3 clean cases). The proof of (b) uses d_p = gcd(v_p(x_i)) as the invariant per prime p, with the key step gcd(min(a,b),|a-b|) = gcd(a,b). The "exactly one entry > 1" conclusion bridges the two: at termination, at most 1 entry > 1 (by W stopping condition), and the invariant forces d_{p_1} >= 1 for some prime p_1 (since all initial entries > 1), so the terminal state cannot be all-1's; therefore exactly 1 entry > 1, equal to M = prod_p p^{d_p}.
