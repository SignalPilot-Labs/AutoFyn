## Lemma/Theorem: `a_1 = 5q` Literal Periodicity Theorem (CERTIFIED, round 26)

**Source.** `a1-5q-subfamily-theorem`, round 26. Independently re-verified in
full by the round-26 proof-reviewer (fresh Python/`sympy` scripts, distinct
from the builder's, for every numeric claim: the 12-cell `(s_0,K_0)` table,
the `Q_1` threshold table and its below-threshold prime lists, every
witness `gcd` computation in the `k=0` closure, the 13 flagged `(j,r,k)`
combinations in the `k≥1` residual band via an independently re-derived
tighter sieve bound, the 5 non-moot witness computations, the `s^*=5`
inequality by direct numeric check for `s=5..14`, and the full literal
sequence for every prime `q∈[7,2000)`).

**Depends on (certified).**
`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`,
`lemmas/legendre-sieve-gap-bound.md`, `lemmas/primorial-floor-bound.md`.

**Statement.** For every prime `q ≥ 7` with `q ∉ Bad(5) := {7,13,19}`, the
sequence with `a_1 = 5q` satisfies, literally from `n=1`:
`a_n = 5(q+n-1)` for every `n ≥ 1`, i.e. `T=1, L=5` periodicity from the
very first term. For each `q ∈ {7,13,19}`, the sequence deviates from this
closed form at a specific, exhibited index (`n=3,4,5` respectively), so
`Bad(5)` is a genuine, permanent (not merely delayed) exceptional set.

**Proof.** By strong induction on `n`, instantiating the certified
`p`-uniform `a_1=pq` machinery at `p=5`: base case + `j=1,5` bands
(consecutive-coprimality / shared-factor-5 legality); Case (a)/(b) split
for bands `j∈{2,3,4}` via the Generalized gcd-difference Witness Lemma;
`K_0`-boundedness giving the explicit 12-cell `(s_0(j,r),K_0(j,r))` table
at `p=5`; `k=0` closure via a sufficient-window criterion plus explicit
witness resolution of the 12 below-threshold candidates (3 of which are
genuine exceptions: `q=7,13,19`, each with an exhausted finite witness
window); `k≥1` closure via the certified Legendre Sieve Gap Bound and
Primorial Floor Bound, using a fresh `s^*=5` threshold inequality
`(s+1)! ≥ 9 + (5/7)·2^{s+1}(s+2)` (proved by induction), reducing to a
residual band `k∈{1,…,27}`, further reduced by an exact sieve-bound scan to
13 flagged `(j,r,k)` combinations, 8 of which are moot (involve
`q∈{7,13,19}`, outside the theorem's scope) and 5 of which are resolved by
explicit witnesses. Full derivation in `approaches/a1-5q-subfamily-theorem.md`.

**Independent verification (this review, fresh scripts).** (1) Reproduced
the 12-cell `(s_0,K_0)` table exactly via `pow(r,-1,5)`. (2) Reproduced the
`Q_1(j,r)` thresholds and their below-threshold prime lists exactly,
matching the file's 12 entries digit for digit. (3) Recomputed every `k=0`
witness `gcd` directly; confirmed the same 3 "no witness" exceptions
(`q=7,13,19`) and valid witnesses for the other 9 below-threshold
candidates (one witness-index label in the file's prose is off by one for
`(2,1,11)` — a cosmetic slip only, since a genuine witness at the correct
index does exist, independently confirmed). (4) Independently re-derived
the 13 flagged `(j,r,k)` combinations in the `k≥1` residual band using the
exact tighter sieve bound `2^{ω(K)+1}(ω(K)+2)` — exact match with the
file's list. (5) Confirmed the moot/non-moot classification (8 moot, all
`q∈{7,13,19}`; 5 non-moot, `q∈{11,17}`) and independently recomputed all 5
non-moot witnesses (`N`, and a genuine `i=3` witness in each case) — exact
match. (6) Verified the `s^*=5` inequality numerically for `s=5,…,14`. (7)
Full independent greedy re-simulation for every prime `q∈[7,2000)` (60
terms each): matches the closed form in every case except `q=7,13,19`,
which deviate exactly at `n=3,4,5` with the exact values reported
(`a_3=42`, `a_4=78`, `a_5=114`), confirming `Bad(5)={7,13,19}` is exact and
complete over this range.

**Status.** Correct, complete, unconditional, no load-bearing gaps found
(two minor witness-index mislabelings in the write-up's illustrative prose,
independently confirmed not to affect any conclusion). Reusable as a
standalone, self-contained addition to the population of certified
`a_1`-subfamily periodicity theorems (joining `2|a_1`, `a_1=p^k`, `a_1=3q`,
`a_1=3q^2`, `a_1=3q^3`, `a_1=3^a q` for `a=1..5`). This is the run's **6th
APPROVE**.
