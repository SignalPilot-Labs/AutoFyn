# Single-Rung-Removal Closed Form and Vertex-5 Closure

**Source:** `greedy-halving-adversary`, round 30 build (§ "Round 30" section,
Steps 1-6).

**Statement.** Let `tail = {a_1,...,a_m}` be the standard ladder tail with
`a_i = f(m)*2^(m-i)`, `i=1,...,m`. For any `p in {1,...,m}`:

  A(tail \ {a_p}) = f(m) * (2^m + (-1)^p * 2^(m-p) + (-1)^m) / 3.

Moreover this quantity is `>= f(m)` for every `p=1,...,m` and every `m>=3`,
with the unique minimum over `p` (for fixed `m`) attained at `p=1`, equal to
`f(m)` exactly only when `m=3` (strictly larger for every `m>=4`).

**Consequence (Vertex 5 closure).** Combined with the Exact-Slope
Monotonicity step (a direct application of the already-certified
`single-insert-point-vertex-lemma`'s `+-1`-slope fact — not re-certified
here as a separate lemma) and the pair-cancellation identity
`A({t} U {x,q1-x} U tail) = A({x,q1-x} U T)` for `T = tail \ {t}`, this
closes Vertex 5 of `h(m)`'s "single-cut-on-q1, tail-untouched" piece for
every `m>=3`: `A({t} U {x,q1-x} U tail) >= f(m)` for every
`x in (0,q1/2]`, `t in tail`.

**Scope / caveat.** This closes exactly the "single cut on q1, tail
completely untouched" piece. It does NOT close `h(m)`'s general q1-cut
sub-case (the complementary piece where the tail is also refined remains
open), nor `h(m)` overall for `m>=3`.

**Proof technique.** Direct finite-geometric-series prefix-sum computation
(`P(k) = sum_{i<=k} (-1)^(i-1) a_i`, closed form `P(k)/f(m) =
(2^m-(-1)^k 2^(m-k))/3`), then `A(tail\{a_p}) = P(p)+P(p-1)-A(tail)`
via a rank-shift argument (removing element at position `p` shifts every
later element down one rank, flipping its sign). The final inequality
`2^m+(-1)^p 2^(m-p)+(-1)^m >= 3` is proved by a two-case parity split on
`p` (even `p`: trivial, margin >= 2^m-1; odd `p`: reduces to
`2^(m-1)+(-1)^m >= 3`, checked by parity of `m`, tight only at `m=3,p=1`).

**Reviewer certification (round 30).** Independently re-derived the closed
form and re-verified both the closed form and the final inequality by a
fresh exact-`Fraction` script for `m=3,...,9` and every `p=1,...,m`: zero
mismatches, matching the builder's own `m=3,...,14` check. Also
independently re-verified, via a dense rational grid, that `F(x) :=
(q1-x) - A({x} U T)` is non-increasing on `(0,q1/2)` for every `t`,
`m=3,...,9` (corroborating, not replacing, the cited slope-lemma proof).
No gap found. Certified.
