# Partition Chamber Theorem

**Source:** `lp-duality-certificate`, round 30 build (§R30.1).

**Statement.** Fix `m` pieces `p_1,...,p_m > 0`, `T = sum p_i` (any
marking, sortedness not required for the statement). Let
`{1,...,m} = B_1 ⊔ ... ⊔ B_r` be any partition of the index set into
disjoint nonempty blocks. For each block `B_j` with `|B_j| >= 2`, choose a
host index `h_j in B_j` and suppose the feasibility condition
`p_{h_j} >= sum_{i in B_j \ {h_j}} p_i` holds; define the residual
`rho_j := p_{h_j} - sum_{i in B_j\{h_j}} p_i >= 0`. For each singleton
block `B_j = {i}`, independently choose "leave untouched" or "bisect."

**Strategy.** For each block with `|B_j|=s>=2`: cut `p_{h_j}` into `s`
fragments, one matching each non-host member exactly plus one residual
`rho_j` (costs `s-1` cuts); leave non-host members untouched. For each
bisected singleton: split into two equal halves (1 cut). For each
untouched singleton: do nothing.

**Formula.**
  Phi = (T + A(Q)) / 2,
  Q := {rho_j : |B_j|>=2} U {p_i : {i} an untouched singleton block},
where `A` is the alternating-sum-of-sorted-descending-order functional.

**Proof.** The full fragment multiset decomposes as `Q` plus, for every
non-host block member and every bisected singleton, an exactly-matched
pair `{v,v}`. By the certified `pair-insensitivity-corollary` (iterated,
no genericity hypothesis needed since its proof is pure parity-counting
via `odd-run-reduction-lemma`), these pairs contribute nothing to `A`, so
`A(M) = A(Q)`. Mass conservation is checked by direct telescoping
(`rho_j` def unwinds to give each block's own total mass). Then
`Phi = (T + A(M))/2 = (T+A(Q))/2` by the shared claiming-subgame
reduction.

**Special cases.** `bisect-subset-lemma` (all-singleton partition),
Double-Bisect-Pin (`double-bisect-pin-family-n4`: two bisected singletons
+ one 2-block + one untouched singleton), the corrected Triple-Pin (one
4-block + one bisected singleton), and Double-Pin-Pair (one 3-block + one
2-block, no singletons) are all one-line instantiations.

**Scope / caveat.** This is a strategy-construction theorem giving an
upper bound on `Phi_min` for any legal instantiation of the partition
family. It does NOT establish that this family of strategies is
exhaustive over all legal <=n-cut strategies, nor that any particular
sub-family (e.g. the specific chambers used for n=4) covers the full
residual region `R` — coverage claims are separate and must be
established (or refuted) independently per instance.

**Reviewer certification (round 30).** Independently re-derived the proof
and re-verified the formula against a from-scratch direct
sort-and-alternating-sum simulation for `m=3,...,7`, random partitions,
hosts, and bisection choices (1913 feasible trials, `Fraction` exact
arithmetic, zero mismatches) — a broader sweep than the builder's own
`m=5`-only check. Also independently re-verified both round-30 witnesses
($p=(11,7,6,3,2)/29$ via Triple-Pin, $p=(14,7,5,3,1)/30$ via
Double-Pin-Pair) close exactly to `Phi=1/2 < 16/31=a_4 T`. No gap found.
Certified.
