## imo-2026-06

a1-11q-subfamily-theorem: new
Target: For every prime `q>11` with `q∉Bad(11)={13,17,19,31,37,43}`,
`a_1=11q` gives `a_n=11(q+n-1)` for all `n≥1` (literal `T=1,L=11`
periodicity), a new fully-general infinite subfamily instance.
Technique: Direct instantiation of the already-certified `p`-uniform
machinery (Generalized `K_0`-Boundedness + gcd-difference Witness Lemma)
at `p=11`, exactly the recipe that closed `a1-5q` (round 26) and `a1-7q`
(round 27) — third consecutive application, zero technique risk, purely
a `p=11`-scaled mechanical build. Also gets the round-27 Universal
Look-Back Witness Identity's `r=1` corollary for free, shrinking the
table work relative to what `a1-5q`/`a1-7q` had to do by hand.
Skeleton:
  1. Strong induction `H(n)`: `a_i=11(q+i-1)`, base case `n=1` — copy
     `a1-pq` Setup verbatim at `p=11`.
  2. `a_n+11` legal (shared factor), `a_n+1` illegal (consecutive
     integers) — `p`-independent, verbatim.
  3. `a_n+j` illegal for `j∈{2,...,10}`: Case (a) `q∤N` (witness `i=1`),
     Case (b) `q|N` (reduces to `gcd(K,m)=1`, `K=N/q`) — by the
     gcd-difference Witness Lemma at `p=11`.
  4. Build the 90-cell `(j,r)` table (`j∈{2,...,10}`, `r∈{1,...,10}`):
     `s_0(j,r)`, `K_0(j,r)=11+s_0(j,r)` via `pow(r,-1,11)` — by the
     Generalized `K_0`-Boundedness Lemma.
  5. `r=1` column's `k=0` layer free unconditionally (`gcd(N,a_n)=
     gcd(k+1,j)`) — by the certified Universal Look-Back Witness
     Identity `r=1` corollary.
  6. Remaining 81 `(j,r≠1)` cells: Legendre Sieve Gap Bound +
     Primorial Floor Bound reduce each to a short below-threshold list.
  7. Hand-check every below-threshold combination for an explicit
     witness or a genuine deviation.
  8. Assemble `Bad(11)` = union of genuine (witness-free) deviations;
     state and verify the final periodicity theorem.
Key lemmas (already certified, reused, not re-derived):
  - Generalized K_0-Boundedness Lemma — because `s_0(j,r)` solves
    `s_0·r≡j (mod p)`, `q`-independent by construction.
  - Generalized gcd-difference Witness Lemma — because
    `gcd(N,a_n)=gcd(N,N-a_n)=gcd(N,j)` (Euclidean subtraction identity).
  - Legendre Sieve Gap Bound + Primorial Floor Bound — because a
    modulus with `r=ω(M)` distinct prime factors has max gap
    `≤2^r(r+1)`, and `ω(M)=r ⟹ M≥(r+1)!` forces `r` small for bounded `M`.
  - Universal Look-Back Witness Identity (`r=1` corollary) — because
    `s_0(j,1)=j` exactly, collapsing the general closed form to
    `gcd(k+1,j)`, threshold-free.
Open gaps: the 90-cell table itself has not yet been mechanically
computed/verified in this workspace (only a raw greedy simulation, by
the explorer, giving `Bad(11)` as a numeric hypothesis); each of the 6
candidate exceptions needs an explicit no-witness hand-check (not just
"simulation deviated"); the claim that `Bad(11)` is exhaustive beyond
`q<6000` needs the full sieve/threshold closure, not a longer numeric
scan (per the round-26 rule against conflating "numerically confirmed"
with "proved").
Cases to cover: 9 bands `j` × 10 residues `r` = 90 cells; `r=1`'s `k=0`
layer free, 81 cells need full threshold/witness treatment.
Watch out for: do not assume the (still unproved) Minimal-Window
Necessity Conjecture — use "all found exceptions are diagonal" only as a
search heuristic, still verify non-diagonal cells; `a1=9q` is NOT a
valid target here (9 not prime; already covered by certified `a1-3aq`,
`a=2`) — do not waste a build slot re-deriving it.

a1-pq-subfamily-theorem: revise (open-gap re-plan, appended new §"Round
28 target" to results/imo-2026-06/approaches/a1-pq-subfamily-theorem.md,
prior content kept verbatim)
Target: (unchanged, parent target) for every fixed odd prime `p`, an
explicit finite `Bad(p)` such that `a_1=pq` gives literal `T=1,L=p`
periodicity for all primes `q>p`, `q∉Bad(p)`, for every residue class `r`
of `q mod p` — this round narrows (does not close) the `r≠1` `k=0`-layer
sub-gap.
Technique: elementary modular-inverse algebra, generalizing round 27's
`r=1`-only Universal Look-Back Witness Identity corollary to a
`q`-independent closed form valid for every residue `r`, by reducing the
defining `s_0`-relation mod `j` from the start (the round-28 explorer's
one new trick) instead of substituting `q`'s explicit residue form.
Skeleton:
  1. From `p(n_0-1)+j=s_0q`, reduce mod `j`: `n_0-1≡s_0qp^{-1} (mod j)`
     — by `gcd(p,j)=1` (Euclidean inverse).
  2. At the `k`-th Case-(b) occurrence, `q+n-1≡q(k+1+s_0p^{-1}) (mod j)`,
     so `gcd(N,a_n)=gcd(j,(k+1+c(p,j,r))\bmod j)`,
     `c(p,j,r):=(s_0(j,r)p^{-1})\bmod j`, `q`-independent — by direct
     substitution, generalizing the certified `r=1` case's derivation.
  3. Prove Uniqueness of r=1: `c(p,j,1)=0` for all `j` (since
     `1^{-1}\equiv1`, forcing `s_0(j,1)=j` exactly); for every `r\ne1`
     some band `j` has `c(p,j,r)\ne0` with `\gcd(j,1+c)>1` (explicit
     non-vanishing case, e.g. `r=p-1`: `s_0=p-j`, `j\nmid(p-j)`) — by
     case analysis on modular inverses mod `p`.
  4. Conclude: the closed form gives an `O(p^2)` table-lookup
     simplification of the `k=0` at-risk-cell bookkeeping for every `r`,
     but proves (not just observes) that no residue other than `r=1`
     admits an unconditional threshold-free `k=0` closure via this
     witness mechanism.
Key lemmas (claim + mechanism):
  - Universal Look-Back Closed Form (general r) — because the `s_0`
    defining relation, reduced mod `j` directly, yields a `q`-independent
    constant `c(p,j,r)`.
  - Uniqueness of r=1 Theorem — because `r=1` is the unique
    multiplicative-identity residue mod `p`, the only one forcing
    `j | s_0(j,r)` for every `j` simultaneously.
Open gaps: not yet formalized as a certified lemma file (currently
explorer-derived + numerically verified on 9762 instances, zero
mismatches, `p∈{5,7,11,13}`); does not touch the `r=1`, `k≥1`,
`gcd(k+1,j)>1` residual, nor does it close the `r≠1` `k=0` cells
(reduces their bookkeeping cost only) — both remain open, requiring the
pre-existing per-`p` sieve/threshold machinery.
Cases to cover: all `r∈{1,...,p-1}` for the closed form; `r=1` vs `r≠1`
split for uniqueness, with an explicit non-vanishing instance required
for every `r≠1` (not just `r=p-1`) to fully prove uniqueness in general
— the explorer only checked `r=p-1` and `r=(p-1)/2` at small `p`; the
builder must either prove the general case algebraically or check it
exhaustively for every `p` instantiated so far (3,5,7,11,13).
Watch out for: do not let the `O(p^2)` table-lookup simplification be
mistaken for new closure — it speeds up the SAME sieve computation, it
does not resolve any cell the existing machinery couldn't already reach
in principle.

a1-7q-subfamily-theorem: no further action (solved, certified — 7th
APPROVE, round 27). Left as is; not part of this round's build set.

covering-system-construction: no further action this round (dual-seed
capped per explorer findings, both known hard seeds — 4807, 11305 — now
fully closed; low priority; no new lever surfaced). Housekeeping only,
no content change.

direct-s0-self-absorption / H2 generic: parked this round per the
math-explorer-h2-direct-attack finding — round 19's Proposition 3
already proves no finite-data method can resolve H2's "no extra primes
outside the core" claim, and this round's large-scale (700k-750k term)
resimulation found nothing new (consistent with prior findings; mild
11305 near-flattening caution noted but not actionable). Do not dispatch
a builder here this round.

H1/FAH generic fresh-corridor search: parked this round — no viable new
mechanism surfaced by any of the three explorer lenses; per the standing
rule (3+ consecutive null fresh-corridor sweeps ⟹ shift effort to
concrete narrower targets), effort stays on the per-p subfamily closures
(a1-11q) and the a1-pq internal generalization (r-uniqueness) instead.

Build set recommendation for outline-reviewer: a1-11q-subfamily-theorem
(new, near-certain 8th APPROVE candidate, same template thrice-verified),
a1-pq-subfamily-theorem (revise, formalize the new closed-form +
uniqueness lemmas as a genuine gap-narrowing, not full closure).
