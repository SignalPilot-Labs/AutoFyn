## Theorem 38 — standalone induction target h(m), exhaustively closed at m=1

**Source:** `greedy-halving-adversary`, round 24.

**Definition.** Fix m>=0 and the unit m-ladder q_1>...>q_{m+1}
(q_i := 2^{m+1-i} f(m), Total(q)=1). Define
h(m) := inf{ A({c} ∪ S) : c in (0,q_1], S a legal (<=m-1)-cut refinement of
the full m-ladder q }.

**Certified claim (m=1 only).** h(1) = f(1) = 1 (in unit-f(1) terms;
q_1=2,q_2=1). Proof: at m=1, S's budget is m-1=0, forcing S to be the
entire, completely untouched unit-1-ladder {2,1}. The function
c |-> A({c,2,1}) is then piecewise linear (3 exact pieces, computed by
direct sort-and-alternate-sum, no numerics):
- c in (0,1]: A = 2-1+c = 1+c (>= 1, equality only as c->0+)
- c in [1,2]: A = 2-c+1 = 3-c (>= 1, equality only at c=2)
so the minimum over c in (0,2] is exactly 1, attained only at the two
endpoints c=0 (limit) and c=2. This matches the general Claims (I)
(c=0: A({0}∪S)=A(S)>=f(m) via (star_m)) and (II) (c=q_1 with S leaving
q_1 untouched: A({c}∪S)=A(S'')>=f(m) via the certified
`general-cross-level-rescaling-lemma` + (star_{m-1})) of Theorem 38,
which for general m are proved individually but NOT shown exhaustive;
at m=1 they ARE jointly exhaustive since S has no free parameters, so
every point of h(1)'s 1-dimensional domain is covered by the direct
hand computation above.

**Reviewer independent re-verification:** re-derived the three-piece
formula by hand from scratch, confirmed it matches; also confirmed
(§ below) that combining this with Theorem 37 does NOT by itself
establish "Case (b)'s whole v>=a branch is closed at n=5" — see the
certification scope note.

**Certification scope — READ BEFORE REUSING.**
- CERTIFIED: h(1) = f(1), exactly, with a complete (no residual case)
  proof, as stated above. This is a genuine, reusable, fully rigorous
  fact.
- CERTIFIED (general m, but each only a partial vertex family, NOT
  jointly exhaustive for m>=2): Claim (I) (c=0 branch, conditional on
  (star_m)) and Claim (II) (c=q_1-untouched branch, conditional on
  (star_{m-1})) individually. The builder's own file explicitly and
  correctly flags that for m>=2 these two vertex types are NOT known to
  be exhaustive — a fresh numeric finding this same round (a 3000-trial
  exact-Fraction search) shows "deeper ties" (c tied to the 3rd, 5th,
  ... largest element of S) can beat the top-tie/boundary candidates in
  a nontrivial fraction (~3.7%) of legal ladder-refinement trials for
  m=2..5. So do NOT treat h(m)>=f(m) as proved for m>=2; it is only
  strong (60k-trial, zero-violation) numerical evidence there.
- NOT CERTIFIED (a genuine gap, not just an m>=2 issue): the downstream
  claim in the approach file's "Open gaps" section that combining
  Theorem 37 (which itself explicitly states it closes only ONE vertex
  of the "v>=a" branch's "T'-leaves-p4-untouched" family, NOT the whole
  sub-branch or its global minimality) with this Theorem 38 m=1
  corollary fully closes "Case (b)'s whole v>=a branch...at n=5". This
  requires additionally ruling out, on Theorem 37's own side, that the
  joint (b,T')-vertex minimizer could have b tied to a NON-maximal
  element of T' (e.g. a fragment produced by T' splitting p5 or p6
  instead of p4) rather than b=p4=max(T'). Theorem 37's proof does not
  address this (it only needs, and only proves, the specific identity
  at b=p4); no argument on file rules out this vertex type. The proof-
  reviewer independently stress-tested n=5 numerically (400k+ random
  exact-Fraction trials, including deep ties) and found ZERO violations
  of A(B)>=f(5) — so the underlying claim is very likely true — but this
  is not a substitute for the missing case in the written proof. See
  `results/imo-2026-03/current.md` round-24 entry for the precise gap
  statement.
