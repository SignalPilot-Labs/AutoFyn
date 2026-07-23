# Lemma RD (Restricted Domination Lemma) + Magnitude Bound Corollary + Proposition 9.4 (conditional)

**Source.** `approaches/intersecting-family-covering-construction.md`, Part 9.1–9.4
(round 10).

## Lemma RD (Restricted Domination Lemma) — unconditional, fully proved

**Statement.** For any index `m\ge1` and any nonempty subset `J\subseteq\{1,\dots,m-1\}`,
there is a prime `q=q(J,m)\in\mathrm{rad}(a_m)` such that
$$|\{j\in J: q\mid a_j\}|\ \ge\ |J|/\omega(a_m).$$

**Proof.** Write `\mathrm{rad}(a_m)=\{q_1,\dots,q_r\}` (`r=\omega(a_m)`). For each
`j\in J`, `j\ne m`, the already-certified Lemma P′
(`lemma-P-prime-pairwise-intersecting.md`, unconditional: `\gcd(a_i,a_j)>1` for
*every* pair of distinct indices, not just consecutive/construction-order ones)
gives `\mathrm{rad}(a_m)\cap\mathrm{rad}(a_j)\ne\varnothing`, so some `q_l` divides
`a_j`. Writing `S_l:=\{j\in J:q_l\mid a_j\}`, `J=\bigcup_{l=1}^rS_l`, so by finite
subadditivity `|J|\le\sum_l|S_l|`, giving `\max_l|S_l|\ge|J|/r` by averaging. Take
`q(J,m)` to be a `q_l` attaining the max. $\blacksquare$

This is a genuine generalization of the already-certified `domination-lemma.md`:
that lemma only ever supplies `J=\{1,\dots,m-1\}` (the specific construction-time
prefix of `a_m=a_{n+1}`, using its own admissibility). Lemma RD replaces this with
the unconditional, order-independent Lemma P′, which holds for *every* pair of
distinct indices regardless of order — this is what licenses `J` to be an
*arbitrary* subset of `\{1,\dots,m-1\}`, in particular a cross-class-restricted one.

## Magnitude Bound Corollary — unconditional, fully proved

**Statement.** With `q(J,m)` as in Lemma RD, `q(J,m)\le\omega(a_m)\cdot a_m/|J|`.

**Proof.** Let `D:=|\{j\in J:q(J,m)\mid a_j\}|\ge|J|/\omega(a_m)`. The `D` values
`\{a_j:j\in J,\,q(J,m)\mid a_j\}` are pairwise distinct positive multiples of
`q(J,m)`, each `<a_m` (strict monotonicity of `(a_n)`). The count of positive
multiples of `q(J,m)` below `a_m` is `\le a_m/q(J,m)`, so `D\le a_m/q(J,m)`; combined
with `D\ge|J|/\omega(a_m)` gives the bound. $\blacksquare$

**Explicit constants.** Using the already-certified Growth Lemma
(`lemma-1-uniform-gap-bound.md`: `a_m\le a_1+(m-1)L<(a_1+L)m`, `L:=\mathrm{rad}(a_1)`)
and `\omega(a_m)\le\log_2a_m<\log_2(a_1+L)+\log_2m`:
$$q(J,m)\ <\ \frac{(a_1+L)m\cdot(\log_2(a_1+L)+\log_2m)}{|J|}\qquad(m\ge1,\ J\subseteq\{1,\dots,m-1\}\text{ nonempty}).$$

## Proposition 9.4 (conditional `O(\log i)` magnitude cap) — CONDITIONAL, hypothesis open

**Hypothesis `(PD_{S,S'})` (NOT proved — open).** For a doubly-infinite disjoint
core pair `(S,S')`: `\exists c=c(S,S')>0,i_0` such that `|I_{S'}\cap[1,i)|\ge c\cdot i`
for all `i\in I_S`, `i\ge i_0`.

**Statement.** Under `(PD_{S,S'})`, for every `i\in I_S`, `i\ge i_0`, the pigeonhole
witness prime `q(i):=q(I_{S'}\cap[1,i),i)$ from Lemma RD satisfies
`q(i)<K_1+K_2\log_2i` for explicit constants `K_1,K_2` depending only on
`a_1,S,S',c`. In particular `q(i)=O(\log i)`.

**Proof.** Direct substitution of `|J_i|\ge ci` into the Magnitude Bound Corollary's
explicit inequality; the `i` factors cancel. $\blacksquare$

**Status of the hypothesis.** `(PD_{S,S'})` is open. It is *not* a free consequence
of Theorem CD's finite-core-count decomposition alone: a finite partition of `\mathbb N`
can have an infinite member of density exactly `0` (e.g. squares vs. non-squares —
this is a fact about arbitrary partitions, demonstrating the general inference
pattern "finitely many classes, one infinite ⟹ positive density" is invalid; it is
*not* a counterexample to `(PD_{S,S'})` itself for this specific sequence). The one
density tool in this workspace (`theorem-UBS-false-case-II.md`'s Euler-divergence/
Landau-Count machinery) cannot be repurposed to prove `(PD_{S,S'})` without
circularity: its density conclusion is derived *from* assumed exact periodicity,
which is only available *after* FCBC/Stabilization is established.

## Certification

**Lemma RD and the Magnitude Bound Corollary are certified `solved`-quality
(sorry-free, unconditional)** — independently re-derived and re-verified by the
round-10 proof-reviewer (fresh Python, pigeonhole check on 500 random `(m,J)` pairs
for `a_1=247` to `N=3000`, zero violations of either inequality; independently
reproduced the `a_1=618` density-stability numerics exactly — `\{2\}\to0.6602`,
`\{2,3\}\to0.3301`, `\{2,103\}\to0.00647`, `\{2,3,103\}\to0.00324`, bit-for-bit,
5 checkpoints `N=5000` to `50000`).

**Proposition 9.4 is certified as a CONDITIONAL result** — the implication
`(PD_{S,S'})\Rightarrow q(i)=O(\log i)` is fully proved; the hypothesis
`(PD_{S,S'})` itself remains open and must be cited as an open hypothesis by any
future approach using this proposition, not silently assumed.

**Reusable by:** any future approach needing a pigeonhole-selected shared prime for
an arbitrary earlier index subset (Lemma RD/Magnitude Bound, unconditional); any
approach that separately establishes `(PD_{S,S'})` for a specific core pair
(Proposition 9.4, conditional bridge).
