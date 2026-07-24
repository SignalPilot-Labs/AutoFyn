## Lemma: Escape-Cost Vacuity Theorem (CERTIFIED, round 10)

**Source.** `covering-system-construction`, round 10, Step 11.6.

**Depends on (certified).** `sandwich-genericity-theorem.md` (proposed alongside
this lemma), `confined-gcd-lemma.md` (for the definition of the divisor-class
alphabet `Div(b)`, `D_bad`, and the class function `g_n`).

**Definitions.** Call a fact about a pair of indices `m < n` (of the sequence)
**class-blind** if it is a statement of the form "property `P(m,n)` holds," where `P`
is defined using only `m`, `n`, and constants depending on `a_1` alone — with no
reference anywhere to `g_m`, `g_n` (or any other divisor-class datum) as inputs. Call
a conclusion **class-sensitive** if it is stated in terms of divisor-class equality
or repetition (e.g., "if `g_{n_j} = g_{n_{j'}} = d` for some `d` in a bad-class set,
then [bound depending on `d`, or on how many times `d` has recurred]").

**Statement.** No finite deductive argument whose premises are all class-blind (in
particular, any argument built solely from the Sandwich Genericity Theorem together
with other class-blind certified facts, such as the static definition of `D_bad`)
can establish a class-sensitive conclusion.

**Proof.** Suppose such an argument exists. Fix any pair of indices `n_j < n_{j'}`
(occurrences of some fixed extended-persistent type, or any indices at all). Every
premise the argument uses is, as a mathematical object, a function of `n_j, n_{j'}`
alone (and the fixed constant `a_1`) — by the definition of class-blind, none of the
premises take `g_{n_j}` or `g_{n_{j'}}` as an argument. Logical deduction is
deterministic: applying the same finite sequence of deductive steps to the same
numerical inputs `n_j, n_{j'}` produces the same output every time, regardless of
what other data (such as `g_{n_j}, g_{n_{j'}}`) happens to accompany those indices in
a particular instance. Hence the argument's output, for the fixed pair `(n_j,
n_{j'})`, is the same whether `g_{n_j} = g_{n_{j'}}` (same class) or `g_{n_j} ≠
g_{n_{j'}}` (different classes) — the argument cannot see `g_{n_j}, g_{n_{j'}}` at
all. So its conclusion cannot depend on divisor-class equality or repetition count,
contradicting the assumption that it establishes a class-sensitive conclusion. ∎

**Scope.** A general-purpose screening lemma: before investing effort in any future
"magnitude squeeze" mechanism (aimo-0680-style or otherwise) aimed at FAH/Cofinite
FAH, check whether every premise used is class-blind in this precise sense. If so,
by this Theorem, the mechanism cannot possibly produce a class-sensitive divisibility
conclusion (such as the Escape-Cost Lemma's claimed index-gap-vs-repetition-count
bound), and should not be pursued further without first identifying a genuinely new
class-sensitive ingredient (a fact relating `g_n` for two or more different indices
`n` directly). This is a structural companion to the round-6 Lemma I diagnosis
(which examined a different, non-magnitude toolkit) and the round-9 Witness
Discontinuity Obstruction (which screens a different mechanism family); together they
now cover both the qualitative (existential/pigeonhole) and quantitative
(magnitude/AP-identity) proof-shape families attempted so far.

**Status.** Correct, complete, no gaps; a short, general "blindness cannot produce
sight" determinism-of-deduction argument, fully unconditional. **Independently
re-verified by the round-10 proof-reviewer** — reviewer note: unlike the round-3
Lemma F / round-6 Lemma I / round-10 Growing-Constraint Obstruction precedent
(diagnostics phrased as "the CURRENT certified toolkit cannot do X," hence not
portable and correctly kept in-file), this theorem is phrased and proved as a
general, toolkit-independent logical principle (any class-blind premises, defined
intrinsically, not by enumerating today's certified lemma list) — it therefore
remains true even as new class-blind lemmas are certified in future rounds, matching
the portability bar the round-9 Witness Discontinuity Obstruction was certified
under. Certified as a standalone reusable screening lemma.
