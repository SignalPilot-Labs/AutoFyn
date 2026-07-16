## dyadic-multiples-and-thinness

**Verdict: APPROVE**  
**True Status: solved** (the builder's `solved` label is correct)

### Scores
- **Correctness: 10/10.** The stated characterization answers the actual compute-and-prove question, and all load-bearing formulas and implications check.
- **Completeness / rigor: 10/10.** The proof covers arbitrary real targets, all three cut vertices by cyclic permutation, strict cut legality, terminal states, the reciprocal exceptional case, nonuniform finite termination, and the endpoint case \(n=2\).
- **Progress: 10/10.** This closes the outliner's decisive affine-thinness gap and supplies a complete necessity-and-sufficiency proof.

### Adversarial verification

1. **Transition formula and geometric legality.** A cut from the vertex of normalized angle \(a\), splitting it into \(x\) and \(a-x\), where \(0<x<a\), gives
   \[
   C_1=(x,b,1-b-x),\qquad C_2=(a-x,c,b+x).
   \]
   Re-deriving by angle sums gives the second child's third angle as \(1-c-(a-x)=b+x\). Also \(1-b-x=a+c-x>c>0\), so the children are genuine triangles. Conversely every \(x\in(0,a)\) is realized by an interior ray from the vertex, which meets the opposite side at a nonvertex perimeter point.

2. **Constructive reciprocal strategy.** When \(t=1/n\), the cumulative marks \(jt\) cannot lie on a partition boundary in the no-multiple case: the first boundary makes the first interval a multiple, and the second makes the remaining interval \((n-j)t\). Hence an interior mark lies strictly in a cyclic interval \((b,b+a)\). The cut \(x=kt-b\) is strictly legal and creates \((n-k)t\) in the first child and \(kt\) in the second. Both coefficients lie in \(\{1,\ldots,n-1\}\). Splitting an existing \(kt\) into \(\lfloor k/2\rfloor t\) and \(\lceil k/2\rceil t\) is legal for \(k\ge2\), and the ceiling-log depth inequality is correct. This includes \(n=2\), where both children immediately contain \(t\).

3. **Finite-depth assertion and König lemma.** The nested recursion
   \[
   W_{r+1}=W_r\cup\operatorname{Pre}(W_r)
   \]
   exactly describes wins in at most \(r+1\) cuts. For a fixed initial state and fixed strategy that terminates against every response sequence, its response tree is binary. If it had unbounded depth, recursively choosing a child subtree of unbounded depth constructs an infinite branch, contradicting termination on every response sequence. Thus the strategy has a finite depth bound for that state; no unjustified global uniform bound is claimed.

4. **Load-bearing affine predecessor classification, independently re-derived.** Assume \(W_r\) is contained in finitely many coordinate lines with values \(pt\). For a cut from \(a\), if a child witness is inherited \(b\) or \(c\), the parent is already on a coordinate-multiple line. Excluding those inherited choices leaves exactly the Cartesian product
   \[
   \{x,1-b-x\}\times\{a-x,b+x\}.
   \]
   Eliminating \(x\) gives, respectively,
   \[
   a=(p+q)t,\quad b=(q-p)t,\quad c=(p-q)t,\quad 1=(p+q)t.
   \]
   Direct symbolic-resultant computation reproduced these four relations. Parent positivity forces the displayed differences to have positive coefficient and rules out zero. The fourth relation is the only projection that can lose all parent restriction, and it is exactly the exceptional reciprocal case forbidden in the necessity argument. Strict legality only shrinks a projection. Since each depth has finite prior indices, three vertex choices, and finitely many witness pairs, each new index set remains finite.

5. **Countable-line avoidance and necessity.** For nonreciprocal \(t\), every finite-rank set lies in finitely many proper coordinate lines, so their union lies in countably many such lines. The proof's elementary isosceles transversal is sufficient: on \((s,s,1-2s)\), each coordinate-multiple line excludes at most one value of \(s\), and the interval \((0,1/2)\) is uncountable. A state outside all \(W_r\) therefore exists; the finite-strategy/rank equivalence shows no Mulan strategy can guarantee finite victory there. This handles irrational \(t\) and non-unit rational \(t\) uniformly.

6. **Artifact-integrity recheck after repair.** The reviewer detected and repaired control-character corruption in the reviewer-authored `current.md` summary (escaped LaTeX commands had been interpreted during file generation). A byte-level scan of `current.md`, the approach file, all three certified lemma files, and this report now finds no control characters other than newlines. The `## Full proof` in `current.md` is byte-for-byte identical as text to the reviewed approach proof, and the load-bearing symbolic predecessor derivation was rerun successfully after the repair.

7. **Independent checks.** Exhaustive finite-grid retrograde analysis for total integer angles \(N=3,\ldots,15\) produced universal targets exactly when the target divides \(N\), agreeing with the claimed unit-fraction characterization. Random rational-state tests reproduced the prescribed grid-mark fork for \(n=2,\ldots,29\). These are sanity checks in addition to, not replacements for, the proof.

### Promotable lemmas
All three proposed lemmas pass the full rigor bar and were certified in the shared cache:
- `/home/agentuser/repo/results/imo-2026-04/lemmas/finite-rank-multiple-line.md`
- `/home/agentuser/repo/results/imo-2026-04/lemmas/finite-strategy-rank-equivalence.md`
- `/home/agentuser/repo/results/imo-2026-04/lemmas/grid-mark-fork-and-dyadic-descent.md`

The reviewer-owned complete solution was written to `/home/agentuser/repo/results/imo-2026-04/current.md`. The ranking outcome for `dyadic-multiples-and-thinness` was recorded as `verified-milestone`.

## Goal Progress

- **Target:** `imo-2026-04`
- **Status:** solved
- **Built approach:** `dyadic-multiples-and-thinness`
- **Verdict:** APPROVE
- **Characterization proved:** \(\theta=180^\circ/n\) for exactly the integers \(n\ge2\).
- **Constructive bound:** at most \(1+\lceil\log_2(n-1)\rceil\) cuts from any nonterminal initial triangle.
- **Necessity mechanism:** nonreciprocal finite-horizon attractors are finite unions of proper coordinate-multiple lines; their countable union misses a triangle, and König's lemma converts finite pointwise victory into finite-rank membership.
- **Ranking outcome:** `verified-milestone`; decisive affine predecessor gap closed.
- **Certified lemmas:** 3.
