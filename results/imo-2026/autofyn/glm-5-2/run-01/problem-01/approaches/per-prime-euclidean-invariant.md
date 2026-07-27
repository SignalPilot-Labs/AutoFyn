# imo-2026-01 — per-prime-euclidean-invariant

Approach: per-prime p-adic valuation decomposition + Euclidean-gcd
identity (invariant) + lexicographic (W, c) monovariant. Both parts (a) and
(b) end to end. This is the clean intended solution.

## Status
solved

## Approaches tried
- Round 1: built the full per-prime Euclidean-invariant proof end to end
  (Lemmas 1–8 + Theorems for (a) and (b)). Numerically sanity-checked 6
  boards × 50 random play orders each; all matched M = ∏_p p^{D_p}.
  No gaps remaining. — solved.

## Current best
Complete rigorous proof of both parts. The survivor is
M = ∏_p p^{D_p}, where D_p = gcd of the positionwise p-adic valuations of
the initial board (gcd(x,0)=x); this depends only on the initial board.

## Full proof

Throughout, N = 2026. Board positions are labelled 1,…,N; each position
holds a positive integer throughout (gcd and lcm/gcd of positive integers
are positive integers). Initially every entry is > 1. A **move** picks two
positions i ≠ j whose entries m, n are both > 1 and replaces them by
gcd(m, n) and lcm(m, n)/gcd(m, n). Recall the valuation identities
(knowledge_base, "Divisor analysis: gcd structure"):

  v_p(gcd(m, n)) = min(v_p(m), v_p(n)),   v_p(lcm(m, n)) = max(v_p(m), v_p(n)),

with v_p(1) = 0. We use the conventions gcd(x, 0) = x and gcd(0,…,0) = 0
for nonneg integers. Ω(x) = Σ_p v_p(x) denotes the total number of prime
factors of x counted with multiplicity (Ω(1) = 0).

---

**Lemma 1 (the move on valuations).** Fix a prime p. If a move replaces the
entries m, n (in positions i, j) by gcd(m, n) and lcm(m, n)/gcd(m, n), then
the pair of valuations (α, β) = (v_p(m), v_p(n)) is replaced by
(min(α, β), |α − β|).

*Proof.* By the gcd/lcm valuation identities,
v_p(gcd(m, n)) = min(α, β), and
v_p(lcm(m, n)/gcd(m, n)) = v_p(lcm(m, n)) − v_p(gcd(m, n)) = max(α, β) − min(α, β) = |α − β|.
 ∎

**Lemma 2 (Euclidean identity).** For nonneg integers α, β,
gcd(min(α, β), |α − β|) = gcd(α, β).

*Proof.* By symmetry of gcd assume α ≥ β. Then min(α, β) = β and
|α − β| = α − β. The Euclidean step gcd(a, b) = gcd(a, b − a) (valid for
nonneg a, b with b ≥ a, together with gcd(x, 0) = x) applied to a = β,
b = α gives gcd(β, α) = gcd(β, α − β). Hence
gcd(min(α, β), |α − β|) = gcd(β, α − β) = gcd(β, α) = gcd(α, β).
(The case β = 0 gives gcd(0, α) = α = gcd(α, 0), consistent.) ∎

**Lemma 3 (list-gcd preservation).** Let L be a list of nonneg integers and
let L′ be obtained from L by replacing two entries α, β (in some two
positions) by α′, β′. If gcd(α, β) = gcd(α′, β′), then gcd(L) = gcd(L′).

*Proof.* The gcd of a list equals the gcd of any one entry-combination with
the rest (associativity of gcd): gcd(a_1, …, a_N) = gcd(gcd(a_i, a_j),
a_1, …, a_{i−1}, a_{i+1}, …, a_{j−1}, a_{j+1}, …, a_N). Applying this to the
two touched positions, gcd(L) = gcd(gcd(α, β), rest) and
gcd(L′) = gcd(gcd(α′, β′), rest); the two are equal since
gcd(α, β) = gcd(α′, β′). ∎

**Lemma 4 (invariant D_p).** For each prime p, define
D_p := gcd of the list {v_p(x_i) : i = 1, …, N} (with gcd(x, 0) = x and
gcd(0, …, 0) = 0). Then D_p is invariant under every move.

*Proof.* A move on positions i, j replaces (α, β) = (v_p(x_i), v_p(x_j)) by
(min(α, β), |α − β|) (Lemma 1). By Lemma 2 the gcd of the two replaced
entries is unchanged. By Lemma 3 the gcd of the full list is unchanged. Hence
D_p is the same before and after the move. ∎

Note D_p is determined by the initial board. For every prime p that divides
no initial entry, D_p = 0; since each initial entry is a finite integer, all
but finitely many primes have D_p = 0.

**Lemma 5 (W-drop).** Define W := Σ_{i=1}^{N} Ω(x_i). Under a move on the
pair (m, n) with g = gcd(m, n), W drops by exactly Ω(g) ≥ 0; the drop is
≥ 1 iff g > 1, and equals 0 iff g = 1.

*Proof.* W = Σ_i Σ_p v_p(x_i) = Σ_p Σ_i v_p(x_i) = Σ_p S_p where
S_p = Σ_i v_p(x_i). The move touches only two positions, so only S_p for
the pair (α, β) = (v_p(m), v_p(n)) changes; by Lemma 1 the new pair-sum is
min(α, β) + |α − β| = max(α, β), while the old pair-sum is α + β. The
per-prime drop is (α + β) − max(α, β) = min(α, β) = v_p(g). Summing over p,
the total drop is Σ_p v_p(g) = Ω(g). ∎

**Lemma 6 (lexicographic monovariant).** Let c := #{i : x_i > 1}. Consider
the pair Φ = (W, c) ∈ ℕ², ordered lexicographically (W primary). Every move
strictly decreases Φ.

*Proof.* The chosen pair (m, n) (both > 1, distinct positions) falls into
exactly one of three disjoint cases.

*Case A: m ≠ n and gcd(m, n) > 1.* Write m = gx, n = gy with g =
gcd(m, n) ≥ 2 and gcd(x, y) = 1. The new entries are g and xy (since
lcm(m, n)/gcd(m, n) = gxy/g = xy). Because m ≠ n, (x, y) ≠ (1, 1), so
xy ≥ 2; both new entries are > 1, hence c is unchanged. By Lemma 5, W drops
by Ω(g) ≥ 1. Thus Φ strictly decreases in the W-coordinate.

*Case B: gcd(m, n) = 1.* Then g = 1, so m = x, n = y with m, n coprime.
Two integers > 1 that are coprime are necessarily distinct (m = n > 1 would
give gcd = m > 1). The new entries are g = 1 and xy = mn > 1. Exactly one of
the two touched positions now holds 1 (previously it held an entry > 1), so
c drops by exactly 1. By Lemma 5, W drops by Ω(g) = Ω(1) = 0, i.e. W is
unchanged. Thus Φ strictly decreases in the c-coordinate.

*Case C: m = n.* Then g = m > 1 and x = y = 1, so xy = 1. The new entries
are m and 1; one touched position drops from > 1 to 1, so c drops by 1. By
Lemma 5, W drops by Ω(m) ≥ 1. Thus Φ strictly decreases in the W-coordinate
(and also in c).

The three cases are exhaustive and disjoint: either m = n (Case C) or
m ≠ n; when m ≠ n, gcd(m, n) is either > 1 (Case A) or = 1 (Case B), and
Case B cannot coincide with m = n (as just noted). In every case Φ strictly
decreases lexicographically. ∎

**Lemma 7 (termination).** The process terminates after finitely many moves.

*Proof.* By Lemma 6 each move strictly decreases Φ = (W, c) in the
lexicographic order on ℕ². This order is well-founded: there is no infinite
strictly-decreasing sequence. Indeed, in any such sequence the first
coordinate W — a nonneg integer — can strictly drop only finitely many times
(each drop is ≥ 1 and W ≥ 0 is a lower bound). Once W has stabilized, every
subsequent move must be of the W-preserving kind (Case B), which drops c by
exactly 1 each time; but c is a nonneg integer, so only finitely many such
moves are possible before c reaches 0. Contradiction. Hence only finitely
many moves occur. ∎

**Lemma 8 (exactly one > 1 at termination).** At the terminal board exactly
one entry is greater than 1.

*Proof.* A move is possible precisely when at least two entries are > 1
(a move picks two entries m, n > 1 from distinct positions). Hence at a
terminal board — one where no move is possible — at most one entry is > 1,
i.e. c ≤ 1.

It remains to show c ≥ 1 throughout. Initially all N = 2026 entries are
> 1, so some entry has at least one prime divisor p; for that p the list
{v_p(x_i)} contains a nonzero entry, hence D_p = gcd of the list satisfies
D_p ≥ 1 (because gcd(x, 0) = x for any nonzero x among the list entries, and
including further entries cannot increase the gcd above that nonzero value…
more directly: a gcd of a list containing a nonzero entry divides that
entry and is positive, so is ≥ 1). By Lemma 4, D_p ≥ 1 holds forever. If
the board ever became all 1's, then v_p(x_i) = 0 for every i, giving
D_p = gcd(0, …, 0) = 0, contradicting D_p ≥ 1. Hence the board is never all
ones: c ≥ 1 always.

Combining c ≤ 1 (terminal) with c ≥ 1 (always) gives c = 1 at termination.
 ∎

**Theorem (part (a)).** Regardless of the choices made, after finitely many
moves exactly one integer M > 1 remains on the blackboard.

*Proof.* Lemma 7 gives finitely many moves; Lemma 8 gives exactly one
survivor > 1 at the terminal board. ∎

**Theorem (part (b)).** The value M does not depend on the choices made.

*Proof.* By part (a), every play terminates at a board with exactly one
entry M > 1 and N − 1 entries equal to 1. Fix such a terminal board and a
prime p. The list of valuations at the terminal board is
{v_p(M), 0, 0, …, 0} (one nonzero entry v_p(M), the rest zero). Its gcd is
gcd(v_p(M), 0, …, 0) = v_p(M), using gcd(x, 0) = x extended to
gcd(x, 0, …, 0) = x (repeated application of gcd(x, 0) = x). By invariance
(Lemma 4) this equals D_p computed from the **initial** board:

  v_p(M) = D_p(initial)   for every prime p.

Therefore

  M = ∏_p p^{v_p(M)} = ∏_p p^{D_p(initial)},

the right-hand side being a finite product: D_p(initial) = 0 for every
prime p that divides no initial entry, and only finitely many primes divide
any initial entry (each is a finite integer). The right-hand side depends
solely on the initial board, not on the sequence of moves. Hence M is the
same for every legal play, i.e. independent of Confucius's choices. ∎

---

**Summary of the formula.** The unique survivor is

  M = ∏_{p} p^{D_p},    D_p = gcd(v_p(x_1), …, v_p(x_{2026}))   (initial board),

a function of the initial board alone. The two ingredients are: (i) the
lexicographic monovariant (W, c) of Lemmas 5–6, giving termination and
exactly-one-survivor (Lemmas 7–8); (ii) the per-prime invariant D_p of
Lemma 4, whose engine is the Euclidean identity gcd(min(α,β), |α−β|) =
gcd(α, β) (Lemma 2), pinning each v_p(M) to D_p and hence M to the initial
board (part (b)).

(The move never introduces new prime divisors: each new entry — gcd(m, n)
or lcm(m, n)/gcd(m, n) — divides lcm(m, n), whose prime support is contained
in primes(m) ∪ primes(n), itself a subset of the primes already present. So
the prime support is non-increasing throughout, consistent with the finite
product above.)

Numerical sanity (not part of the proof): boards {6, 10, 15} → 30,
{4, 8, 16} → 2, {4, 8, 3} → 6, {12, 18, 30} → 30, {2, 3, 5, 7} → 210,
{100, 200, 50, 75} → 150 — each matching ∏_p p^{D_p} over 50 random play
orders. ∎

## Promotable lemmas
- **Euclidean valuation invariant (Lemmas 1–4 here).** Statement: under the
  move (m, n) ↦ (gcd(m, n), lcm(m, n)/gcd(m, n)), for each prime p the
  pair (v_p(m), v_p(n)) is sent to (min, |α−β|) (Lemma 1), and the
  quantity D_p = gcd of all positionwise v_p-valuations is invariant
  (Lemmas 2–4, engine = identity gcd(min(α,β),|α−β|) = gcd(α,β)). Proved in
  full above; importable by any approach needing the part-(b) pin.
- **Lexicographic (W, c) termination monovariant (Lemmas 5–7 here).**
  Statement: with W = Σ Ω(x_i) and c = #{x_i > 1}, every move strictly
  decreases (W, c) lexicographically (three disjoint cases: gcd>1 & m≠n;
  gcd=1; m=n); ℕ² lex is well-founded ⇒ finitely many moves. Proved in
  full above.
