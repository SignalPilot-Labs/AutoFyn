# Audit of `claude-code/claude-fable-5`

## Grading standard

I checked each submission against the corresponding statement in `problems.jsonl`. I used a strict IMO-style, completion-based standard: a proof with a load-bearing gap receives no credit merely for having the right idea, while an argument that is complete up to an unmistakably local wording or presentation repair can receive full credit. Computational checks are accepted as corroboration, but the mathematical proof itself must establish the result unless the problem explicitly permits computation.

## Score summary

| Problem | Score | Verdict |
|---|---:|---|
| 1 | 7/7 | Correct |
| 2 | 7/7 | Correct |
| 3 | 7/7 | Correct; one harmless base-case wording omission |
| 4 | 7/7 | Correct |
| 5 | 7/7 | Correct |
| 6 | 7/7 | Correct |
| **Total** | **42/42** | |

These scores are not awards for plausible approaches. In each case I found a complete route through the part of the argument on which the result depends.

## Problem 1 — 7/7

### Outline of the submitted proof

The solution uses two ingredients:

1. the lexicographic monovariant consisting of the product of all entries and the number of entries; and
2. for every prime $p$, invariance of the gcd of the list of $p$-adic valuations.

If two selected numbers are $m,n$ and $d=\gcd(m,n)$, replacing them by $d$ changes the total product by the factor $1/d$. Thus the product strictly falls if $d>1$. If $d=1$, the product stays fixed and the number of entries falls. Since both coordinates are positive integers, this proves termination.

The proof then observes that a move cannot remove all non-unit entries, so the terminal singleton is greater than $1$. For each prime $p$, the valuation of the inserted gcd is the minimum of the two selected valuations. Replacing two integers in a list by their minimum preserves the gcd of the whole valuation list. Hence the exponent of $p$ in the terminal number is forced to be

$$
\gcd\bigl(v_p(a_1),\ldots,v_p(a_n)\bigr).
$$

This determines the terminal number uniquely, independently of the sequence of moves.

### Audit findings

- The lexicographic descent is valid in both cases $d>1$ and $d=1$.
- The non-unit claim is sufficient to exclude termination at $1$.
- The valuation invariant is stated and used correctly, including primes that divide only some of the initial numbers: zero valuations cause no problem.
- The prime-by-prime exponents uniquely determine the final integer.

There is no missing case or unjustified inference. **Score: 7/7.**

## Problem 2 — 7/7

### Outline of the submitted proof

This is the longest solution and the one most vulnerable to hidden sign or algebra errors. The proof normalizes the triangle in the complex plane by taking

$$
A=0,\qquad B=c,\qquad C=b e^{i\alpha},
$$

and parametrizes the two constructed points in the forms

$$
K=c(1-\rho e^{-i\varphi}),\qquad
L=b e^{i\alpha}(1-\sigma e^{i\varphi}),
$$

with positive real parameters $\rho,\sigma$. The containment assumptions in the problem are used to choose the correct directed-angle branches.

The two angle conditions are converted into two real algebraic relations, denoted $E_1=0$ and $E_2=0$. With the abbreviations used in the solution, these are

$$
E_1=b t-c s_1+c\rho(2s+s_2)-2c\rho^2s_1,
$$

$$
E_2=c t-b s_1+b\sigma(2s+s_2)-2b\sigma^2s_1.
$$

The circumcenter of $\triangle AKL$ is then written explicitly as

$$
O=\frac{|K|^2L-|L|^2K}{\overline K L-K\overline L}.
$$

The desired equality $OM=ON$ is reduced to a polynomial-trigonometric expression $F=0$. The central algebraic certificate is the identity

$$
2s_1F=igl((cs_1-bt)\sigma-cs\bigr)E_1
      +\bigl((ct-bs_1)\rho+bs\bigr)E_2.
$$

Therefore the two relations supplied by the hypotheses imply the goal.

### Audit findings

- I checked the geometric parametrizations and their signs. In particular, the branch for $K-B$ and the corresponding branch on $AC$ for $L$ agree with the stated containment conditions.
- The uses of angle additivity are legitimate precisely because of those containment hypotheses; this is not an illicit equality of directed angles modulo $180^\circ$.
- The passage from the two angle equalities to $E_1=E_2=0$ is valid. Only the vanishing of the relevant imaginary parts is required.
- The circumcenter formula is correct for the chosen normalization.
- The reduction of equality of the two distances to $F=0$ has the correct signs.
- I independently entered the displayed expressions for $F,E_1,E_2$ and the two coefficients into SymPy. Exact expansion and trigonometric simplification returned zero for the difference between the two sides of the certificate. This checks the load-bearing algebra rather than relying on numerical examples.
- The solution treats $A,K,L$ as non-collinear when using the circumcenter formula. The statement itself calls $AKL$ a triangle and supplies its circumcenter, so this is a legitimate use of the problem's setup rather than a gap.

The verification material is useful corroboration, but the exact certificate is already present in the written proof and makes it independently checkable. I found no mathematical gap. **Score: 7/7.**

## Problem 3 — 7/7

### Outline of the submitted proof

The claimed value is

$$
c_n=\frac{2^n}{2^{n+1}-1}.
$$

For the lower bound, the solution lets the first player cut the stick into lengths proportional to

$$
1,2,4,\ldots,2^n.
$$

After the second player's cuts, the fragments are ordered by length and paired consecutively. Each pair is represented by an edge between the two original first-player pieces containing its fragments. There are $n+1$ vertices and at most $n$ edges, so some connected component is a tree. Bipartition of that tree, combined with the binary uniqueness of the original piece lengths, produces a discrepancy of at least the smallest original length. This bounds the sum of even-ranked fragments by $(1-s)/2$, and consequently the sum of odd-ranked fragments by $(1+s)/2$, where $s=1/(2^{n+1}-1)$.

The proof also establishes that, under optimal play in the claiming phase, the first player obtains exactly the sum of the odd-ranked fragment lengths.

For the upper bound, if the first player makes fewer than $n$ cuts, the second player simply bisects every first-player piece. If exactly $n$ cuts are made, a subset-sum pigeonhole argument finds two disjoint collections whose total lengths differ by at most $s$. A folding/Euclidean-algorithm lemma then uses at most $n$ cuts to create equal pairs covering all but at most that discrepancy. The even-ranked sum is therefore at least $(1-s)/2$, giving the matching upper bound.

### Audit findings

- The backward-induction analysis of the claiming phase is correct.
- The consecutive-pair inequality for the even-ranked sum is valid, including a possible final unpaired fragment.
- The graph has the required vertex/edge count. A connected component with fewer edges than vertices is a tree, and no paired edge leaves that component.
- Binary uniqueness yields the asserted positive discrepancy; it is not merely a parity heuristic.
- The treatment of fragments outside the selected component combines correctly with the component estimate.
- The subset-sum pigeonhole estimate in the upper bound has the right scale and produces disjoint indexed collections after canceling their intersection.
- The folding lemma gives exactly the number of additional cuts claimed and creates genuine equal-length pairs.
- In the equal-total base case of the folding lemma, the written recursive formulation formally permits the residual family to have size zero even though the lemma was introduced for size at least one. The intended action there is simply to stop immediately. This is an unmistakable local base-case wording repair and does not hide an unproved mathematical step.

I also ran the supplied verification script with bytecode generation disabled. Its exhaustive/sampled small-$n$ checks passed. The score rests on the proof, not on that experiment. **Score: 7/7.**

## Problem 4 — 7/7

### Outline of the submitted proof

The solution proves that the winning angles are exactly

$$
\theta=\frac{180^\circ}{n}
$$

for integers $n\ge 2$.

For these angles, the first direction uses descent on angle multiples. If the current triangle already has an angle equal to a positive multiple of $\theta$, one cuts off $\theta$ from it and retains a triangle with a smaller multiple. If no angle is a multiple, the solution chooses the largest angle and uses the integer parts of the other two angles divided by $\theta$ to locate a cut for which both resulting triangles contain an angle that is a positive multiple of $\theta$. Induction then gives a winning strategy in either branch.

For the converse, the proof defines a triangle to be safe when none of its angles is a multiple of $\theta$. Starting from a generic safe triangle, it shows that after any legal cut at least one child remains safe. Indeed, if one child acquires a multiple of $\theta$, the two possible modular conditions on the cutting angle force the other child not to acquire one. The second player always chooses a safe child, so an angle equal to $\theta$ can never occur.

### Audit findings

- The descent lemma preserves positivity of every angle and strictly lowers the relevant integer multiple.
- In the no-multiple case, the floor estimates correctly give $b+c\le n-2$.
- The selected cut lies strictly inside the largest angle, and both children receive a positive multiple of $\theta$; endpoint and zero-angle cases are excluded.
- The special small case $n=2$ is handled.
- A generic safe initial triangle exists when $180^\circ$ is not an integer multiple of $\theta$.
- The modular two-child argument is exhaustive and proves that the second player can maintain safety forever.
- A later computational remark suggests a stronger characterization on a finite lattice. That remark is not needed anywhere in the proof of the stated result and therefore creates no dependency on an unproved computation.

The supplied exact-arithmetic verification script also passed, including exhaustive finite-lattice checks and explicit strategy checks, but the written argument is complete on its own. **Score: 7/7.**

## Problem 5 — 7/7

### Outline of the submitted proof

The proposed translations are checked first by standard quadratic-mean/arithmetic-mean/geometric-mean inequalities. To prove uniqueness, the solution substitutes $x=f(y)$ into the equality and obtains

$$
f(f(y))=2f(y)-y.
$$

Iterating this relation and using positivity forces $f(y)\ge y$. Writing

$$
g(y)=f(y)-y\ge0,
$$

the proof then substitutes $x=f(z)$ into the left-hand inequality. After exact simplification, if $\delta=g(z)-g(y)$, it obtains

$$
(A-B)^2\ge 2(A+B)\delta+\delta^2
$$

for the quantities $A,B$ defined in the solution. When $\delta\ge0$, this yields

$$
0\le g(z)-g(y)\le\frac{(z-y)^2}{4y}.
$$

Interchanging $y,z$ gives the corresponding absolute estimate. Dividing an interval into $N$ equal pieces and telescoping makes the total variation at most a constant times $1/N$, so $g$ is constant. Thus $f(x)=x+c$ with $c\ge0$, and the initial verification shows all and only these functions work.

### Audit findings

- The self-composition identity follows from a legal positive substitution.
- The orbit argument forcing $f\ge\operatorname{id}$ is correct and does not assume continuity.
- I checked the exact algebra leading to the quadratic inequality in $\delta$.
- The one-sided estimate and its symmetric form follow with the stated denominator.
- The telescoping argument is valid on every compact positive interval and forces equality of any two values of $g$.
- No regularity assumption is silently used.

The accompanying symbolic/numerical verification script passed and agrees with the hand check. **Score: 7/7.**

## Problem 6 — 7/7

### Outline of the submitted proof

Let $S$ be the set of positive integers sharing a common prime factor with every term already generated. The recursive sequence is exactly the increasing enumeration, from $a_1$ onward, of the integers in $S$. In particular, every integer greater than $a_1$ outside $S$ has an earlier sequence term coprime to it.

The solution encodes each sequence term by its finite set of prime divisors and lets $\mathcal F$ be the resulting family. It proves:

- members of $\mathcal F$ pairwise intersect;
- a finite prime set is a transversal of $\mathcal F$ exactly when it itself belongs to $\mathcal F$.

It then considers the antichain $\mathcal B$ of inclusion-minimal members. For $B\in\mathcal B$ and $p\in B$, a descent argument constructs $B'\in\mathcal B$ with

$$
B'\cap B=\{p\},\qquad
\prod B'<\frac{\prod B}{p},
$$

whenever the latter product is still above $a_1$. Iterating gives a minimal set

$$
C_p=\{p\}\cup D_p,
$$

where the product of the primes in $D_p$ is at most $a_1$.

Only finitely many sets $D_p$ are possible. If the union of all minimal members were infinite, infinitely many primes $p$ would share one fixed $D$. If $D$ were empty, pairwise intersection would fail. If $D$ were nonempty, the transversal property would force $D$ to contain a minimal member, contradicting the antichain property because that member would be a proper subset of $C_p$. Thus the union $U$ of the minimal members is finite.

Membership in $S$ now depends only on divisibility by primes in the finite set $U$, hence only on the residue modulo

$$
L=\prod_{p\in U}p.
$$

If there are $T$ acceptable residues in one block of length $L$, translation by $L$ gives

$$
a_{n+T}=a_n+L
$$

for every $n$. This is the required periodicity.

### Audit findings

- The identification of the sequence with the increasing enumeration of $S$ follows directly from minimality in the recurrence.
- The self-duality statement for $\mathcal F$ is proved in both directions. For a finite transversal, taking a sufficiently large power of the product supplies an integer beyond $a_1$ with exactly the required prime support.
- The descent lemma correctly obtains an earlier coprime term and then an inclusion-minimal prime support; all strict product inequalities have the right direction.
- The descent terminates because it strictly decreases a positive integer product.
- The finite-choice argument for $D_p$ is valid: all its primes and its product are bounded by $a_1$.
- The infinite-pigeonhole and antichain contradiction handles both $D=\varnothing$ and $D\ne\varnothing$.
- Once $U$ is finite, residue-class periodicity of membership is immediate, and the counting argument correctly turns it into periodicity of the enumerated sequence. There is no hidden transient range.

The supplied script tested several starting values and reported no violations of the intermediate lemmas. Again, that is corroborative only; the combinatorial proof is complete. **Score: 7/7.**

## Final verdict

This batch is unusually strong. I specifically looked for branch mistakes in Problem 2, an unjustified extremal step in Problem 3, a modular endpoint failure in Problem 4, hidden continuity in Problem 5, and circularity in the self-dual-family argument of Problem 6. None materialized. The only defect I found is the harmless zero-size stopping case in the wording of Problem 3's folding lemma. Under ordinary IMO coordination, that is well within full-credit territory.

**Final score: 42/42.**
