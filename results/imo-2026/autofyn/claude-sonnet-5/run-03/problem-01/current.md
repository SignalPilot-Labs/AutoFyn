## Status
solved

## Approaches tried
- `lex-potential-gcd-invariant`: complete two-part proof (lexicographic potential
  `(N,\Sigma)` for termination, `G_p` gcd invariant for uniqueness). Reviewer found a
  genuine false intermediate claim in the Setup (`g\cdot q = \gcd(m,n)\cdot
  \operatorname{lcm}(m,n) = mn`, asserted as a "standard identity" derived from
  `v_p(g)+v_p(q)=\min(a,b)+\max(a,b)`, which is wrong: `v_p(q)=|a-b|\ne\max(a,b)`
  unless `\min(a,b)=0`). Numerically false in general (`m=4,n=6`: `gq=12\ne mn=24`).
  The claim is used to justify "`g,q` not both `1`" in Claim 1's case-split
  exhaustiveness. The *conclusion* is still true (correctly via `gq=\operatorname{lcm}(m,n)\ge
  m>1`, as `induction-on-active-count`'s Lemma L1 shows), so the approach's overall
  logic is sound and easily repaired, but as written it rests on a false statement.
  Downgraded from claimed `solved` to `partial`; see review below. Outcome: **partial
  (real progress, one false intermediate identity to fix)**.
- `induction-on-active-count`: strong induction on active count `k`, nested with a
  second strong induction on the quadratic potential `\Sigma` to handle "stalling"
  moves (those with `k(g,q)` still both `>1`), proving termination for *every*
  sequence of legal moves (not a fixed strategy), correctly closing the round-1
  interleaving gap and the outline-reviewer's arithmetic slip (active count drops by
  at most 1, never 2, via a correctly-proved Lemma L1: `gq=\operatorname{lcm}(m,n)\ge
  m>1`). Part (b) proved from scratch via the `G_p`-invariant. Reviewed in full,
  independently re-derived the load-bearing identities and re-checked all case splits:
  no gap found. Outcome: **solved**.

## Current best
(superseded — Status is `solved`, proof below is `induction-on-active-count`'s,
verified correct and complete by the proof-reviewer in round 1.)

## Full proof

*(Reproduced verbatim from `results/imo-2026-01/approaches/induction-on-active-count.md`,
verified correct and complete by the proof-reviewer.)*

Throughout, the blackboard is modeled as a fixed set of 2026 **positions**
`1,...,2026`; a *board* `B` is an assignment of a positive integer to each position.
Call a position **active** in `B` if its entry is `>1`. A **legal move** on `B` picks
two distinct active positions `i≠j` with entries `m,n>1`, and produces the board `B'`
that agrees with `B` outside `{i,j}` and has, at `{i,j}` (in either order), the values
`g=gcd(m,n)`, `q=lcm(m,n)/gcd(m,n)`. A move is possible on `B` iff `B` has at least
two active positions. Confucius plays a **maximal sequence** of legal moves (per the
problem's rule); we must show every such sequence, for every possible sequence of
pair-choices, is finite, ends with exactly one active position, and that the
surviving value `M` there is the same for every such sequence.

### 0. The per-prime reduction

Fix a prime `p`. Write `v_p(x)` for the `p`-adic valuation of `x>0`. By unique
factorization, `v_p(gcd(m,n))=min(v_p(m),v_p(n))`, `v_p(lcm(m,n))=max(v_p(m),v_p(n))`.
Since `gcd(m,n) | lcm(m,n)`, `q=lcm(m,n)/gcd(m,n)` is a positive integer with
`v_p(q)=max(v_p(m),v_p(n))-min(v_p(m),v_p(n))=|v_p(m)-v_p(n)|`. So writing `a=v_p(m)`,
`b=v_p(n)`, a legal move replaces `(a,b)` simultaneously for every prime `p` by
`(v_p(g),v_p(q))=(min(a,b),|a-b|)`. (∗)

**Lemma I1 (monovariant inequality).** For nonnegative integers `a,b`,
`min(a,b)^2+|a-b|^2 ≤ a^2+b^2`, with equality iff `min(a,b)=0`.
*Proof.* WLOG `a≤b`. `a^2+b^2-(a^2+(b-a)^2) = b^2-(b-a)^2 = a(2b-a) ≥ 0` since
`2b-a≥2a-a=a≥0`. Strict unless `a=0`. ∎

**Lemma I2 (gcd invariance under one Euclidean step).**
`gcd(min(a,b),|a-b|) = gcd(a,b)` for nonnegative integers `a,b` (convention
`gcd(x,0)=x`, `gcd(0,0)=0`).
*Proof.* If `a=b` both sides are `a`. Else WLOG `a<b`: `d|a,b ⟺ d|a,b-a`, so `{a,b}`
and `{a,b-a}` share the same common-divisor set, hence the same gcd. ∎

**Lemma L1 (not both trivial).** If `m,n>1`, `g=gcd(m,n)` and `q=lcm(m,n)/gcd(m,n)`
are not both `1`.
*Proof.* By definition `g·q = lcm(m,n)` (directly from `q=lcm(m,n)/g`, so no separate
identity is needed). Since `m | lcm(m,n)`, `lcm(m,n) ≥ m > 1`, so `gq>1`, impossible
if `g=q=1`. ∎

### 1. Two global quantities
`k(B) = #{active positions}`, `Σ(B) = Σ_i Σ_p v_p(B(i))^2` (well-defined finite sum
since each `B(i)` has finitely many prime factors).

### 2. Single-Move Lemma
**Lemma SM.** Let `B` have `k(B)≥2`, `B'` obtained by one legal move. Exactly one of:
(Drop) `k(B')=k(B)-1`; or (Stall) `k(B')=k(B)` and `Σ(B')<Σ(B)`.
*Proof.* The move touches only `i,j$ with `m,n>1`. `k(B')-k(B) = #{x∈{g,q}:x>1}-2`.
By L1 this count is `1` or `2`, giving Drop or Stall respectively. For `Σ`: writing
`Δ_p = v_p(g)^2+v_p(q)^2-v_p(m)^2-v_p(n)^2`, (∗) and I1 give `Δ_p≤0` for every `p`,
strict exactly when `min(v_p(m),v_p(n))>0`, i.e. `p|gcd(m,n)`. In the Stall case
`g=gcd(m,n)>1` so some such `p` exists, forcing `Σ(B')-Σ(B)=Σ_p Δ_p<0`. ∎

### 3. Part (a): termination with exactly one survivor, for every move sequence
**Theorem P(k).** For every board `B` with `k(B)=k`, there is no infinite sequence of
legal moves starting at `B`; every maximal sequence from `B` is finite with terminal
active count `1` if `k≥1`, `0` if `k=0`.

*Base `k=0,1`:* no legal move exists; the empty sequence is the unique maximal one.

*Inductive step `k≥2`, outer strong induction on `k` (hypothesis: `P(k')` for `k'<k`),
nested with strong induction on `s=Σ(B)` for fixed `k` (Claim `Q(s)`):* Let `B` have
`k(B)=k≥2`, `Σ(B)=s`, and let `σ` be *any* sequence of legal moves starting at `B`
(arbitrary choice of pairs at every step). If `σ` is nonempty, its first move produces
`B_1`. By Lemma SM (which places no restriction on which pair was chosen), either
(Drop) `k(B_1)=k-1<k`, so the outer hypothesis `P(k-1)` applies to `B_1`: there is no
infinite sequence of legal moves from `B_1`, so the tail of `σ` from `B_1` — hence `σ`
itself — is finite, and if `σ` is maximal it ends at active count `1`; or (Stall)
`k(B_1)=k`, `Σ(B_1)=s_1<s`, so the inner hypothesis `Q(s_1)` applies, giving the same
conclusion. Since `σ` was an arbitrary sequence of legal moves from `B`, this proves
`Q(s)`, hence (all `s`) `P(k)`. This closes the induction: `P(k)` holds for all
`k≥0`, for *every* sequence of legal moves regardless of Confucius's choices at every
step (no strategy assumption anywhere in the argument).

**Application.** The initial board has `k=2026≥2`; Confucius's actual play is by rule
a maximal sequence of legal moves, hence by `P(2026)` finite, terminating at exactly
one active position with value `M>1`. This proves part (a).

### 4. Part (b): `M` is independent of Confucius's choices
For each prime `p`, `G_p = gcd(v_p(a_1),...,v_p(a_2026))` computed from the initial
board (convention `gcd(0,...,0)=0`).

**Lemma GP.** `G_p(B)` is unchanged by every legal move, for every prime `p`.
*Proof.* Let `R` be the multiset of `p`-valuations at the 2024 untouched positions,
`r=gcd(R)`. Since a common divisor of a multiset union is exactly a common divisor of
the gcds of its parts, `gcd(R∪{a,b}) = gcd(r,gcd(a,b))`. Applying this before and
after the move (touched pair valuations `(a,b) → (min(a,b),|a-b|)` by (∗)) and using
Lemma I2 (`gcd(min(a,b),|a-b|)=gcd(a,b)`), the two expressions for `G_p(B)` and
`G_p(B')` coincide. ∎

**Reconstruction.** Iterating Lemma GP across all moves of any legal play,
`G_p(B*) = G_p(B^{(0)}) = G_p` for every prime `p`, where `B*` is the terminal board.
By part (a), `B*` has one active position (value `M`) and 2025 positions equal to `1`,
so its multiset of `p`-valuations is `{v_p(M),0,...,0}`, whose gcd is `v_p(M)`. Hence
`v_p(M) = G_p` for every prime `p`, and by unique factorization
$$M = \prod_{p \text{ prime}} p^{G_p}.$$
This product is well-defined and finite: `G_p=0` for every prime `p` dividing none of
`a_1,...,a_2026` (all such valuations are `0`), so only the finitely many primes
dividing some `a_i` contribute. The right-hand side depends only on the initial
board, not on Confucius's choices — this proves part (b). Also `M>1`: since
`a_1>1`, some prime `p_0` has `v_{p_0}(a_1)>0`, giving `G_{p_0}>0`, so
`M≥p_0^{G_{p_0}}>1`, consistent with part (a). ∎∎

### Theorems/facts invoked
- Fundamental Theorem of Arithmetic (unique factorization): `v_p(gcd)=min`,
  `v_p(lcm)=max`, and integers are determined by their exponent vectors.
- Euclidean algorithm identity `gcd(a,b)=gcd(a,b-a)` (Lemma I2).
- gcd distributes over multiset union / is associative-commutative (Lemma GP proof).
- Strong induction / well-foundedness of `\mathbb{Z}_{\ge0}`, used twice (nested),
  built from first principles rather than cited as lexicographic well-ordering.
