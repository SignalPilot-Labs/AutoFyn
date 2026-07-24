## Lemma: Window Resolution Lemma (CERTIFIED, round 10)

**Source.** `greedy-exchange-cost-potential`, round 10.

**Depends on (certified).** `free-facts-gcd.md`,
`extended-earliest-witness-intersection.md` (Lemma G, for the setup/definitions of
a rogue pair and its extended-persistent refinements).

**Setup.** Fix a rogue pair `(A',B')` (disjoint `S₀`-extended-persistent types
refining disjoint base types), and let `n_1 < n_2 < ...` enumerate all indices `n`
with `ρ(n) = A'` past some fixed threshold.

**Lemma.** There are infinitely many `j` with `n_{j+1} > n_j + 1`.

**Proof.** `A', B'` are both `S₀`-extended-persistent, nonempty (`ρ(n) ⊇ τ(n) ≠ ∅`
by Free Facts applied against `a_1`), and disjoint (`A'∩B'=∅` by the rogue-pair
hypothesis), so `A' ≠ B'`. Let `N_{B'} := {n : ρ(n) = B'}`, infinite since `B'` is
extended-persistent. Fix any `n_0 ∈ N_{B'}` with `n_0 > n_1` (possible since
`N_{B'}` is infinite hence unbounded). Since `ρ(n_0) = B' ≠ A'`, `n_0` is not an
`A'`-occurrence, so letting `j := max{i : n_i < n_0}` (well-defined and finite,
since `n_0` exceeds only finitely many of the increasing sequence `n_1<n_2<...`),
`n_j < n_0 < n_{j+1}` (the second inequality since `n_0 ≠ n_{j+1}`, as
`ρ(n_0)=B'\ne A'=\rho(n_{j+1})$, combined with maximality of `j`). Hence
`n_{j+1}-n_j \ge 2` for this `j`. Since each finite interval `(n_j,n_{j+1})`
contains only finitely many elements of the infinite set `N_{B'}\cap(n_1,\infty)`,
the map `n_0 \mapsto j` from this infinite set to `\{1,2,\dots\}` has infinite
image, so infinitely many `j` satisfy `n_{j+1}-n_j\ge2`. ∎

**Scope.** Rules out, for any rogue pair, the naive "single-step" reading of a
successor-style argument's window (i.e. the false special case
`a_{n_{j+1}}=a_{n_j+1}` for all large `j`) — the window relevant to any Successor
Claim / Escape-Budget-style mechanism must be the fully telescoped interval
`(a_{n_j}, a_{n_{j+1}})`, whose length has no certified uniform ceiling (see
`greedy-exchange-cost-potential` round-10 section, Growing-Constraint Obstruction
and the empirically-open Return-Time Boundedness discussion). Purely structural;
does not itself resolve FAH, the Successor Claim, or any open hypothesis.

**Status.** Proved in full from Free Facts alone (via the definitions of
extended-persistent type and rogue pair); no dependence on any open hypothesis.
Independently confirmed on `a_1=4807` (26 sampled extended-persistent types, every
minimum gap ≥ 5, none equal to 1). **Independently re-verified by the round-10
proof-reviewer**: re-derived the pigeonhole argument from scratch, and reran an
independent fresh simulation on `a_1=4807` (own trial-division generator, `S₀=
{2,3,5,7,11,19,23}`, `A'={3,5,19}`) confirming all 3 sampled consecutive-occurrence
gaps exceed 1 (gaps found among 4 occurrences at indices 6, 561, 1114, 2223),
consistent with the proof. Certified.
