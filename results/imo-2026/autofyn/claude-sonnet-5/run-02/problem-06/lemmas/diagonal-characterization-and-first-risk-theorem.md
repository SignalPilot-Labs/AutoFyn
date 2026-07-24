## Lemmas: Diagonal Characterization and First-Risk Theorem for `a_1=pq` (CERTIFIED, round 26)

**Source.** `a1-pq-subfamily-theorem`, round 26 build (Minimal-Window
Necessity Conjecture investigation). Independently re-verified in full by
the round-26 proof-reviewer.

**Depends on (certified).**
`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`.

### Lemma 1 (Diagonal Characterization)

**Statement.** Fix odd prime `p`. For `j∈{2,…,p-1}` and `r∈{1,…,p-1}`, let
`s_0(j,r)∈{1,…,p-1}` be the unique solution of `s_0·r≡j (mod p)` (the
certified `K_0`-Boundedness Lemma's defining relation). Then `s_0(j,r)=1`
if and only if `j=r`.

**Proof.** Two-line congruence argument: `s_0=1 ⟺ r≡j (mod p) ⟺ r=j`
(literal equality, since both lie in `{1,…,p-1}`). Full proof in
`approaches/a1-pq-subfamily-theorem.md` §(1).

### Lemma 2 (First-Risk Theorem)

**Statement.** Fix odd prime `p`, prime `q>p`, `r:=q\bmod p`. For each band
`j∈{2,…,p-1}`, let `n_0(j):=1+(s_0(j,r)q-j)/p` be its first Case-(b)
occurrence index. Then `n_0(j)` is a strictly increasing function of
`s_0(j,r)`: for any two bands `j,j'` with `s_0(j,r)<s_0(j',r)`,
`n_0(j)<n_0(j')`. **Corollary:** when `r≥2`, the diagonal band `j=r`
(`s_0=1`, the minimum) is the unique band with the smallest `n_0` — the
first Case-(b) risk encountered as `n` increases.

**Proof.** `n_0(j')-n_0(j) = [(s'-s)q-(j'-j)]/p > 2/p > 0` using `q>p`,
`s'-s≥1`, and `|j'-j|≤p-3<p-2`; since both `n_0` values are integers, the
difference is a positive integer. Full proof in
`approaches/a1-pq-subfamily-theorem.md` §(2).

**Independent verification (this review, fresh scripts).** (1) Reproduced
Lemma 1 on a large random/exhaustive sample. (2) Reproduced Lemma 2 by an
exhaustive scan over `p∈primes(5,60)`, `q∈primes(p+1,p+200)`, all band
pairs `j≠j'` — **282,089 pairs tested, zero failures**. (3) Independently
re-simulated the greedy recurrence (correct "for all `i`" legality
semantics) and confirmed the `p=13,q=19` worked example in the source
file's §(3) exactly (diagonal band `j=6` deviates first, at `n=3`,
matching direct greedy simulation digit for digit) and, in a from-scratch
1049-pair sweep (`p<40`, `q∈(p,p+600)`, full-length simulation
`maxn=3q+50`), found **zero** counterexamples to "every genuine deviation
has `s_0=1`" (73 deviations found, all `s_0=1`) and **zero** deviations
with `r=1`, matching the source file's corrected 1763-pair sweep's
qualitative claims.

**Status.** Both lemmas correct, complete, unconditional, no gaps found.
Reusable by any future `a_1=pq`-type closure. Note: these lemmas do **not**
by themselves prove the Minimal-Window Necessity Conjecture ("only
diagonal-band deviations are ever genuine exceptions") — that conjecture
remains open; see `approaches/a1-pq-subfamily-theorem.md` for the precise,
honestly-reported residual gap (a genuine "isolated fragility" instance
for a non-diagonal band exists, §(3) of that file, so a full proof needs
more than ordering/size arguments).
