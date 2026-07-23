## imo-2026-06

### Raw Experimental Data

**Sequences computed** (50-100+ terms, all verified periodic):

| a1 | factorization | T | L | L = product of |
|---|---|---|---|---|
| 2 | [2] | 1 | 2 | {2} |
| 3 | [3] | 1 | 3 | {3} |
| 4 | [2] | 1 | 2 | {2} |
| 6 | [2,3] | 1 | 2 | {2} |
| 10 | [2,5] | 1 | 2 | {2} |
| 15 | [3,5] | 8 | 30 | {2,3,5} |
| 21 | [3,7] | 1 | 3 | {3} |
| 35 | [5,7] | 34 | 210 | {2,3,5,7} |
| 77 | [7,11] | 18 | 154 | {2,7,11} |
| 91 | [7,13] | 20 | 182 | {2,7,13} |

**First 30 terms for a1=15:** 15, 18, 20, 24, 30, 36, 40, 42, 45, 48, 50, 54, 60, 66, 70, 72, 75, 78, 80, 84, 90, 96, 100, 102, 105, 108, 110, 114, 120, 126

**Differences (a1=15, stable):** 3,2,4,6,6,4,2,3 repeating with period T=8, sum L=30.

**First 30 terms for a1=35:** 35, 40, 42, 45, 50, 60, 70, 75, 80, 84, 90, 100, 105, 110, 120, 126, 130, 135, 140, 150, 160, 165, 168, 170, 175, 180, 190, 195, 200, 210

**Differences (a1=77, stable):** 7,4,10,12,2,14,6,8,14,14,8,6,14,2,12,10,4,7 repeating with period T=18, sum L=154.

Periodicity verified: a_{n+T} = a_n + L holds for all n >= 1 (from index 1 in all tested cases except a1=35 where it holds from index 2).

---

### Key Structural Discovery: The Stable Prime Set S

Each sequence has a "stable prime set" S (a finite set of primes) determined by the dynamics. The period is L = product(S) and T = |R| where R is the set of stable residues mod L.

**What determines S:** S is NOT simply the prime factors of a_1. Examples:
- a1=6=2*3: S={2} only (3 drops out)
- a1=15=3*5: S={2,3,5} (2 is ADDED, not in a1)
- a1=35=5*7: S={2,3,5,7} (2 and 3 are added)
- a1=77=7*11: S={2,7,11} (2 is added, 3 enters at a2=84=2*3*7 but then drops out)

**Why 3 drops out for a1=77 but not a1=35:**
- a1=77: a2=84={2,3,7}, a3=88={2,11}, a4=98={2,7}. The term 98 has P(98)∩S={2,7} ⊆ {2,3,7}=P(84)∩S. So constraint from 84 is dominated by constraint from 98. Prime 3 is never "essential" — its constraint is always covered by 2 or 7.
- a1=35: a2=40={2,5}, a3=42={2,3,7}, a4=45={3,5}. The term 45 introduces constraint "must share 3 or 5." This is NOT dominated by {2,7}-type constraints. Prime 3 becomes essential via the pair {3,5}.

---

### Key Structural Discovery: The Stable Residue Set R

**VERIFIED FACT:** The stable residues mod L are exactly those r in {1,...,L} such that r is divisible by at least one "minimal valid S-prime set."

The minimal valid S-prime sets are the minimal subsets F of S such that: every other element of R shares at least one prime from S with any number whose S-prime set = F. Equivalently: F is a minimal prime set consistent with ALL constraints imposed by the initial terms.

For a1=15 (S={2,3,5}, L=30): minimal valid sets = {2,3}, {2,5}, {3,5}.
R = {numbers mod 30 divisible by 6, 10, or 15} = {0,6,10,12,15,18,20,24}. T=8. ✓

For a1=77 (S={2,7,11}, L=154): minimal valid sets = {2,7}, {2,11}, {7,11}.
R = {numbers mod 154 divisible by 14, 22, or 77} = 18 elements. T=18. ✓

For a1=35 (S={2,3,5,7}, L=210): minimal valid sets = {2,5}, {3,5}, {5,7}, {2,3,7}.
R = {numbers mod 210 divisible by 10, 15, 35, or 42} = 34 elements. T=34. ✓

**CRUCIAL OBSERVATION:** The stable residue set R is self-consistent: any two elements of R share at least one prime from S. This is exactly why once the sequence enters R, it can stay there forever.

**Proof of self-consistency:** Any two elements r, r' of R have S-prime sets containing some minimal valid sets F, F' respectively. By the definition of "valid," F and F' share at least one prime (otherwise one would exclude the other, contradicting both being in R). Hence gcd(r, r') > 1 for any two stable-regime terms.

---

### Key Structural Discovery: Large Primes are Locally Irrelevant

Every stable-regime term a_n has the form: (product of some primes from S) * (possibly one large prime q > max(S)). The large prime q appears only in a_n and no other term. The constraint from a_n via q is automatically satisfied by all future stable terms because every future term shares an S-prime with a_n (by self-consistency of R).

**Verified:** For a1=35 (S={2,3,5,7}), terms like 110=2*5*11, 130=2*5*13, 165=3*5*11, etc. have large primes, but every subsequent stable term shares 2 or 5 (or 3 or 7) with them. Checked 40 terms — no failures.

**Why this happens:** All minimal valid S-prime sets for a1=35 contain 5 OR contain {2,3,7}. So every stable term is divisible by 5, or divisible by 2 and 3 and 7. Either way it shares a prime with 110=2*5*11 (via 2 or 5).

---

### Key Structural Discovery: Greedy Traversal of R

**VERIFIED FACT:** In the stable regime, a_{n+1} is the smallest element of R + k*L (for appropriate k) greater than a_n. This is exactly the greedy traversal of the residue set R.

This means: the sequence of differences (a_{n+1} - a_n) is the cyclic sequence of gaps between consecutive elements of R (ordered on the circle Z/LZ), with period T and sum L.

For a1=15: greedy gaps through R={0,6,10,12,15,18,20,24} are [6,4,2,3,3,2,4,6] (reading from 0). Actual stable differences are exactly this cyclic sequence. ✓

For a1=77: greedy gaps through R match the actual stable differences (same cyclic sequence, starting at different phase). ✓

---

### What the Proof Must Do

**Step 1: Show S stabilizes.** The stable prime set S is finite and determined after finitely many terms. Informally: only primes dividing numbers in a bounded range near a_1 can become "essential." Large primes that enter the sequence alongside existing S-primes never become essential because their constraints are dominated.

**Step 2: Show the "effective constraint" reduces to a finite window.** The constraint on a_{n+1} from all prior terms reduces (after the transient) to the constraint from terms within one period (the last T terms). Old constraints are dominated: constraint from a_j (old) is dominated by constraint from a_i (newer, i > j) when P(a_i) ∩ S ⊆ P(a_j) ∩ S. Within each period, all "minimal valid S-prime types" appear, so all old constraints get dominated.

**KEY SUBTLETY:** The constraint from term a_j with S-prime set F is dominated by term a_i with S-prime set F' if F' ⊆ F (any future term sharing a prime from F' also shares a prime from F). Since terms with each minimal valid S-prime set appear repeatedly (once per period), all old constraints eventually become dominated.

**Step 3: Show a_{n+1} depends only on a_n mod L.** Once the effective constraint is just "a_{n+1} ≡ r (mod L) for some r in R and a_{n+1} > a_n," the sequence of residues mod L is determined purely by the current residue. The greedy selection picks the next element of R after a_n mod L.

**Step 4: Conclude periodicity.** Since the greedy traversal of R is periodic with period T and increment L, we get a_{n+T} = a_n + L for all large n.

---

### Distinct Openings / Proof Angles

**Opening 1: Finite-state automaton argument.**
The "effective state" of the sequence at time n (for determining a_{n+1}) is a function of (1) a_n mod L and (2) which old constraints remain. Show (2) becomes periodic, hence state is eventually periodic. Periodicity of a finite-state deterministic system.

**Opening 2: Direct constraint domination within a window.**
Show explicitly: for each term a_j in the stable regime, its constraint is dominated by some a_i with i in [j+1, j+T]. Since T is a fixed window size, the effective constraints only come from the last T terms. Since (a_{n-T+1} mod L, ..., a_n mod L) cycles with period T and the greedy selection is deterministic given this window, the sequence is periodic.

**Opening 3: Self-consistency of R and greedy selection.**
Directly prove R is self-consistent (any two elements share an S-prime). Then prove: if all of a_{n-K}, ..., a_n are in R-classes (for large K), then a_{n+1} is also the smallest R-class element > a_n, i.e., the greedy selection. This gives the periodicity directly.

**Opening 4: Primorial structure and Chinese Remainder Theorem.**
L = product(S) is squarefree. The stable residues mod L are those r with gcd(r, L) having ≥ 2 distinct prime factors (in cases where all minimal valid sets have size 2). By CRT, the sequence mod each prime p in S satisfies a local periodicity condition, and these combine to give global periodicity with period L = lcm of periods mod each p.

**Opening 5: Infinite graph / "Divisibility graph" approach.**
Define the graph G on positive integers where i~j iff gcd(i,j)>1. The sequence is a path in G that greedily extends to the left. The path eventually follows the structure of a "comb" — periodic arithmetic progressions. The periodicity is equivalent to the comb having period L.

---

### Candidate Techniques

- **Finite-state / pigeonhole:** The effective state (residues of last T terms mod L) takes finitely many values, so by pigeonhole it repeats, giving periodicity. This is the cleanest approach.
- **Constraint domination / sliding window:** Show old constraints become redundant within a fixed window. Key: elements of each minimal S-prime type appear in every window of length T.
- **Greedy selection on a fixed arithmetic structure:** Once R is established as self-consistent, the greedy minimum through R is purely periodic.
- **Invariant theory:** The set S is an invariant of the sequence. Once S is determined, the "residue class mod L" of each term is a monovariant that stabilizes.

---

### Cheap-Kill Candidates

- **Parity / prime count:** For a1=2, all terms are even (trivial). The simplest case shows the structure.
- **Pigeonhole on finite-window states:** The tuple (a_n mod L, ..., a_{n+T-1} mod L) has finitely many values; eventually repeats.
- **Size bound on S:** S ⊆ {primes dividing some a_k for k ≤ N} where N can be bounded. This bounds L and T explicitly.

---

### Knowledge-Base Entries to Use

- **Divisor analysis / gcd structure:** The core of the problem. See "Divisor analysis" and "Divisibility graphs" entries.
- **Pigeonhole / extremal principle:** For the finite-state argument (window of T terms has finitely many patterns).
- **Invariants and monovariants:** The set S of essential primes is an invariant that stabilizes.
- **Order of an element / eventual periodicity:** "Sequences are eventually periodic mod m" (Linear recurrences entry). The sequence mod L is eventually periodic.
- **Bertrand's postulate:** May be needed to bound the size of S (ensuring no "new" large prime enters S after the transient).

---

### Analogous Past Problems (Cruxes)

1. **aimo-0514** (combinatorics/invariants-and-monovariants): "Show a deterministic process is reversible so its state graph is a union of cycles, forcing the orbit to be purely periodic." The crux: augment the state with enough local information to make the one-step map a bijection on a finite state set. Directly analogous: our sequence's "effective state" (window of T residues mod L) is finite; if we show the transition is deterministic and injective on this state space, we get periodicity. The key difference: our sequence is NOT reversible (it's a greedy construction), but the forward map on states IS deterministic and on a finite set, so it must eventually repeat.

2. **aimo-0079** (number_theory/pigeonhole): "Among infinitely many length-L windows of a {0,1}-valued function, pigeonhole over finitely many possible window-patterns to find two starting positions whose windows agree." Directly applicable: windows of T consecutive residues mod L (from the stable regime) take finitely many values; two identical windows give the same next term, implying periodicity. The crux move is pigeonhole on sliding windows.

3. **aimo-0387** (combinatorics/processes-and-algorithms): "Reduce an infinite process to a finite one-shot lemma 'exit a bounded region' and iterate." Analogous idea: show the sequence exits the "transient phase" (reaches the stable prime set S) in finitely many steps, then is periodic. The one-shot lemma is "within K steps the sequence stabilizes."

---

### Prior Progress

None (current.md status = unsolved, no approaches yet).

---

### Dead Ends (Do Not Retry)

None recorded yet.

---

### Small-Case / Intuition Notes

**Conjecture (strongly supported by data):** The stable prime set S, the period L = product(S), and the stable residue set R are all well-defined for every starting value a_1. Moreover:

1. S stabilizes after finitely many (typically very few) terms.
2. L = product of distinct primes in S (squarefree).
3. T = |R| = number of integers in {1,...,L} whose S-prime support contains some minimal valid S-prime set.
4. The stable regime begins when the sequence first hits a stable residue class, which happens by term O(a_1) or so.

**Critical structural fact (conjecture, strongly supported):** In the stable regime, a_{n+1} = min{m > a_n : m mod L ∈ R}. This is purely a function of a_n mod L.

**Consequence:** The proof reduces to:
(A) Show the sequence eventually has all its terms in stable residue classes (i.e., mod L in R).
(B) Show that once in stable classes, the constraint from ALL prior terms is equivalent to the constraint from the last T terms (one period).
(C) This makes the selection of a_{n+1} depend only on a_n mod L, giving periodicity with period T and increment L.

The hardest part is likely (B) — showing old constraints are dominated. The key lemma is: every minimal valid S-prime type appears in every window of T consecutive stable terms.
