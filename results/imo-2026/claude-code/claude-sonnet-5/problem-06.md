I spent extensive time on this (deep theoretical work plus computational experiments in Python), and I need to be upfront: I could not complete a fully rigorous proof. Given your instruction not to present partial work as if it
  were a finished solution, I want to explain honestly what happened rather than hand you something with a hidden gap.

  What I was able to prove rigorously:

  1. Bounded gaps. Every $a_i$ with $i\ge 2$ must satisfy $\gcd(a_i,a_1)>1$, so it's divisible by some prime factor of $a_1$. Consequently any multiple of $a_1$ larger than $a_n$ is automatically compatible with all of
  $a_1,\dots,a_n$ (it carries every prime factor of $a_1$, and every earlier term shares at least one such prime). Since $a_{n+1}$ is the smallest valid candidate, this forces $a_{n+1}-a_n\le a_1$ for all $n$ — gaps are uniformly
  bounded by the fixed constant $a_1$.
  2. A persistent core of primes. Since every term (from index 2 on) is hit by the finite set of primes dividing $a_1$, a pigeonhole argument shows some nonempty subset $S_1$ of those primes divides infinitely many terms, and in
  fact from some index $N_0$ on, every term is divisible by some element of $S_1$.
  3. Empirical confirmation. I wrote and ran Python simulations (tracking exact factorizations, searching for $T,L$ with $a_{n+T}=a_n+L$) on dozens of starting values, including semiprimes like
  $15,35,65,77,105,143,187,667,\dots$. In every case tested — including runs out to tens of thousands of terms — the sequence does become exactly periodic in this sense, with $L$ a product of a small number of primes not
  exceeding $a_1$.

  Where I got stuck. The natural strategy is to show that the family of "inclusion-minimal" prime-factor-sets obstructing compatibility stabilizes after finitely many terms (this would immediately give a fixed modulus and hence
  exact eventual periodicity, via a clean argument I did work out). I could show new minimal sets can only arise via a "fresh prime bridging" mechanism (tied by pigeonhole to a specific earlier term), and I could show
  density-type necessary conditions on that process — but I was not able to rule out, with full rigor, the possibility of infinitely many such bridging events in the worst case. Several plausible-looking finishing arguments
  (density/reciprocal-sum bounds, a "star" domination argument, a cofactor-minimality argument) each turned out, on skeptical review, to have a genuine gap or a counterexample-shaped hole once I pushed on them.

  So I have a solid, verified structural start (bounded gaps + persistent prime core) and strong computational evidence the full statement is true, but not a complete proof of the key finiteness/stabilization lemma that the rest
  of the argument depends on.

  I'd rather tell you that plainly than dress up an incomplete argument as

⏺ a complete one.

  Given the difficulty here, I'd suggest one of a few ways to proceed, rather than me continuing to grind alone against the same wall:

  1. I keep working on just the stabilization lemma, in a much narrower, more surgical way (e.g., trying to prove it via a sharper double-counting or an explicit potential function I haven't yet tried), reporting back only if I
  actually close the gap — not another wall of exploratory reasoning.
  2. You point me at a specific technique you suspect is the intended one (e.g., if you recall this being from a specific competition/year), which would let me target the right idea instead of searching blind.
  3. I write up the honest partial result (bounded gaps + persistent prime core + the precise statement of the remaining lemma) as a clean note, clearly labeled as incomplete, so at least the verified part is usable.

  Let me know which you'd like, or if you'd rather I just keep pushing on option 1 unprompted.

✻ Sautéed for 39m 11s