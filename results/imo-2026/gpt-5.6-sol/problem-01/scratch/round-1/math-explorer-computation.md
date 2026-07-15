## imo-2026-01
- Distinct openings:
  1. **Prime-exponent / subtractive-Euclidean encoding.** Encode each board integer by its vector \((v_p)_{p\in P}\), where \(P\) is the finite union of primes initially present. On a selected pair, each coordinate \((a,b)\) changes to \((\min(a,b),|a-b|)\). The computationally visible invariant is the gcd of all entries in each prime coordinate. A separate strictly decreasing global potential handles termination. This points to the conjectural terminal formula
     \[
     M=\prod_{p\in P}p^{d_p},\qquad d_p=\gcd\bigl(v_p(a_1),\ldots,v_p(a_{2026})\bigr),
     \]
     with zeros included in the gcd in the usual way.
  2. **Factorization-free product/support potential.** If \(P_B\) is the product of all current board entries and \(r_B\) is the number of entries greater than \(1\), experiments suggest the single integer \(2^{r_B}P_B\) strictly decreases at every move. This is a cheap whole-solution route for part (a), after which the same valuation-gcd invariant identifies the unique survivor for part (b). It avoids introducing \(\Omega\) or summing over primes in the termination argument.
  3. **Additive arithmetic potential.** Let \(\Omega(x)\) count prime factors with multiplicity. The state statistic \(\sum_i\Omega(a_i)+r_B\) also strictly decreases in every tested transition: the \(\Omega\)-part drops when the chosen gcd is nontrivial, while the support count drops when the chosen pair is coprime. This is a more transparent primewise route than opening 2 and comes with a direct move bound, though it is not genuinely independent of the valuation picture.
  4. **Finite divisor-lattice state space.** Every exponent created is a minimum or absolute difference of earlier exponents, hence never exceeds the initial coordinatewise maximum; all board values therefore remain divisors of the initial lcm, giving a finite state graph. Exhaustive graphs are acyclic in all small examples. Finiteness alone is insufficient (cycles still must be excluded), so this route needs either one of the above potentials or a new acyclicity order; it is a secondary framing, not currently the strongest opening.
- Candidate technique(s): p-adic valuation vectors; the subtractive Euclidean operation \((a,b)\mapsto(\min(a,b),|a-b|)\); gcd invariance under Euclidean replacement; an integer-valued monovariant combining product size with the count of nonunits, or combining total \(\Omega\) with that count; finite-state divisor-lattice encoding.
- Cheap-kill candidates:
  - Let \(g=\gcd(m,n)\). The product of all board entries is divided by exactly \(g\) in the move. If \(g=1\), the product stays fixed but two nonunits become \(1\) and \(mn\), so the number of nonunits drops by one. Thus either the product decreases or the support count decreases; combining them multiplicatively as \(2^{r_B}P_B\), or lexicographically, looks like the cleanest termination kill.
  - Prime support (the union of primes dividing at least one board entry) is preserved coordinatewise: \((a,b)\neq(0,0)\) cannot map to \((0,0)\). Hence a terminal state cannot consist entirely of ones.
  - For each fixed prime, \(\gcd\) of the full multiset of valuations is preserved by the two-variable Euclidean identity \(\gcd(\min(a,b),|a-b|)=\gcd(a,b)\). At a terminal board this invariant directly reads off the survivor's exponent.
- Knowledge-base entries to use:
  - **Invariants & monovariants** (Combinatorics section): exactly the board-process mechanism needed for termination and terminal-state identification.
  - **Invariant / monovariant** (General Proof Methods): the named general method for the strictly decreasing integer potential.
  - **Divisor analysis** (Number Theory): relevant for gcd structure and prime-factor/exponent encoding.
  - **Induction / infinite descent** (General Proof Methods): optional language for why a positive-integer potential cannot descend forever; direct well-ordering is simpler here.
- Analogous past problems (cruxes):
  - `aimo-0678` — a genuinely relevant gcd/lcm process. Its crux constructs an integer monovariant adapted to the recurrence and then reduces to a finite state. The exact invariant there does not transfer, but the analogy is strong: isolate a quantity controlled by gcd/lcm, use it to bound/terminate the process, and only then read the eventual state.
  - `aimo-0324` — a blackboard game whose crux is to replace the visible integer by a prime-factor statistic (squarefree part) that is one-sided under every allowed operation. Analogous in the design principle of compressing the arithmetic state to prime-exponent data; its specific squarefree-part statistic does not transfer.
  - `aimo-0440` — a blackboard subtraction process terminated by a strictly decreasing nonnegative integer \(L^1\)-potential. Analogous to the proposed \(\sum\Omega+r_B\) potential and to the valuation-coordinate subtraction; unlike the present problem, its moves are chosen strategically rather than arbitrarily, so only the monovariant crux is transferable.
- Prior progress: none. The run state records no existing workspace, no current proof, no ranked approaches, and no certified lemmas; `results/imo-2026-01/` was absent when inspected. The problem is `number_theory`, task `proof_only`, answer type `none` (difficulty metadata is medium, and the explicit user selection overrides the hard-only default).
- Dead ends (do not retry):
  - **Product alone** is not strict: for a coprime pair, e.g. \((2,3)\mapsto(1,6)\), the board product is unchanged.
  - **Number of entries greater than 1 alone** is not strict: \((6,10)\mapsto(2,15)\) leaves that count unchanged.
  - **Total \(\Omega\) alone** is not strict on coprime pairs, again \((2,3)\mapsto(1,6)\).
  - **Sum of board entries** is not monotone: \((2,3)\mapsto(1,6)\) increases it from 5 to 7.
  - **Ordinary gcd or lcm of all board entries** is not invariant: \((4,8)\mapsto(4,2)\) changes both the global gcd (4 to 2) and lcm (8 to 4).
  - **Maximum p-adic exponent** is not invariant: for the 2-adic pair \((1,3)\), corresponding to \((2,8)\), one move gives exponents \((1,2)\).
  - **Finite state space by itself** does not prove termination; an exclusion of directed cycles is still required.
- Small-case / intuition notes:
  - Exhaustive state-graph search (states sorted as multisets) gave a unique terminal state in every tested example, matching the conjectured valuation-gcd formula:
    - \((4,8)\): 4 states, terminal \((1,2)\), all paths length 3.
    - \((6,10,15)\): 11 states, terminal \((1,1,30)\), path lengths 3–4.
    - \((12,18,20)\): 45 states, terminal \((1,1,30)\), path lengths 5–8.
    - \((8,12,18)\): 35 states, terminal \((1,1,6)\), path lengths 5–9.
    - \((6,6,10,15)\): 59 states, terminal \((1,1,1,30)\), path lengths 4–8.
    - \((4,9,25,49)\): 15 states, terminal \((1,1,1,44100)\), all paths length 3.
  - Conjecture strongly supported: the terminal value need not equal any familiar global gcd/lcm/product, but its prime support is exactly the union of all initial prime supports, and each terminal exponent is the gcd of that prime's initial exponents. For instance, \((4,8)\) has terminal value 2 although its initial gcd is 4; \((4,9,25,49)\) has terminal value equal to the product 44100 because each prime appears with exponent 2 in only one entry and exponent 0 elsewhere, whose gcd is 2.
  - Move counts depend substantially on choices even though terminal values do not. Thus no fixed-step-count invariant should be expected; the useful object is a strict potential giving only a bound.
  - Hard step assessment: no computationally indicated exceptional case. The main exposition hazards are (i) explicitly treating zero valuations in the coordinate gcd, (ii) showing a prime present somewhere cannot disappear globally, and (iii) not claiming that finiteness of the divisor state space alone gives termination.
