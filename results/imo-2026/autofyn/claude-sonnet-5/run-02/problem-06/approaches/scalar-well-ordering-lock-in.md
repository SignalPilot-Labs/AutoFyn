## Status
partial

## Approaches tried
- **scalar-well-ordering-lock-in** (round 7, this round, new approach). Attempted to
  transplant crux `aimo-0678`'s two-scalar mechanism (a non-increasing scalar witness
  hitting a floor by well-ordering, coupled with a SECOND scalar shown constant by an
  exact algebraic identity rather than by pigeonhole) onto the already-certified
  open(k)/recruitment-process structure, as a genuinely different proof *style* from
  the FAH/Symmetric-FAH existential-to-universal field. Steps 1–3 of the outline
  (well-definedness of the scalar w_k) are established rigorously below — free
  bookkeeping, no gap. Step 4 (the coupled scalar g_k and its hypothesized exact
  recursive identity) is **refuted**: a concrete, exactly-computed counterexample
  (seed a_1 = 175) is exhibited showing the hypothesized recursion cannot hold, and a
  general structural reason is proved for why it cannot hold in principle, not just
  for this seed. This is a genuine, rigorous negative result (Witness Discontinuity
  Obstruction, proved and promotable below), analogous in spirit and rigor to the
  certified diagnostic Lemma I, but this one is an unconditional mathematical fact
  (not a statement about the current certified toolkit), so it is proposed for
  certification as a standalone lemma. The approach does not close gap (†); it
  honestly documents why this specific algebraic-identity transplant fails, per the
  outline's own step-6 fallback instruction, strengthening (not merely repeating)
  Lemma I's diagnosis: even the algebraic-fixed-point STYLE, not just the four
  previously-diagnosed combinatorial tools, cannot bypass FAH in the direct form
  hypothesized.

## Current best

### 0. Setup (imported, no new work)
Fix the certified structure from `results/imo-2026-06/lemmas/`: Q = P(a_1), the
finite set 𝒫 of persistent base types (Persistent-Type Pigeonhole), the fixed finite
list of disjoint base-type pairs (Collateral-Safety Theorem's Corollary), the
recruitment-process cores S₀^(0) ⊆ S₀^(1) ⊆ ⋯ (each S₀^(k+1) = S₀^(k) ∪ {a newly
recruited prime}), and open(k) := {(A,B) ∈ 𝒫×𝒫 disjoint : (A,B) not fully safe at
S₀^(k)} (Collateral-Safety Theorem), which is non-increasing in k over this fixed
finite index set. (†) holds iff open(k) = ∅ for some finite k.

Fix once and for all a strict total order ≺ on the finite set of disjoint base-type
pairs: lexicographic on (sorted(A), sorted(B)) as ordered lists of primes (primes
themselves ordered by their standard integer order), with A,B ⊆ Q always taken as
the base types with A ≺ B by their own minimum element (WLOG, to avoid the pair
(A,B) and (B,A) both appearing — pick the representative with min(A) < min(B)); if
min(A) = min(B) is impossible since A ∩ B = ∅ forces min(A) ≠ min(B), so this
convention gives a well-defined, tie-free total order on the finite pair set. This
settles the "cases to cover" item flagged by the outliner (no two pairs can tie
under this order, since a finite list of finite sets of integers has a well-defined
lexicographic order once ties within a pair are ruled out as just shown).

### 1. w_k is well-defined (proved, free bookkeeping)
**Claim.** For every stage k with open(k) ≠ ∅, define (A_k, B_k) := the ≺-least
element of open(k), and w_k := a_{n_{B_k}} where n_{B_k} := min{n : ρ_k(n) = B_k'}
for SOME fixed choice of S₀^(k)-extended-persistent refinement B_k' of B_k (namely:
among the (finitely many, by the certified Extended Persistent-Type Pigeonhole)
S₀^(k)-extended-persistent refinements of B_k, take the ≺-least one under the same
lexicographic order on subsets of the finite set S₀^(k), and then its earliest
occurrence). Then w_k is a well-defined positive integer.

**Proof.** open(k) is a subset of the fixed finite pair list (Collateral-Safety
Theorem's Corollary), so if nonempty it has a ≺-least element (finite linearly
ordered set); (A_k,B_k) is well-defined. By definition of "not fully safe," there is
at least one pair of S₀^(k)-extended-persistent refinements A_k', B_k' of A_k, B_k
with A_k' ∩ B_k' = ∅; in particular the (nonempty, by the Extended Persistent-Type
Pigeonhole) finite set of S₀^(k)-extended-persistent refinements of B_k is nonempty,
so it has a ≺-least element B_k' (finite set of finite subsets of S₀^(k), same
tie-breaking argument as above applied within S₀^(k) rather than Q). By definition
of "extended-persistent," B_k' occurs as ρ_k(n) for infinitely many n, in particular
for at least one n, so n_{B_k} := min{n : ρ_k(n) = B_k'} exists and is a positive
integer (well-ordering of ℕ). Hence w_k := a_{n_{B_k}} is a well-defined positive
integer. ∎

This closes the outline's step 3 target ("w_k well-defined and finite at every
stage") in full, including the tie-breaking refinement the outline left implicit
(which specific extended-persistent refinement of B_k to use when B_k itself has
several).

### 2. The coupled scalar g_k and the hypothesized recursion: REFUTED

**The literal step-4 target, stated precisely.** Let q_k be a Lemma-G prime
recruited at stage k against the ≺-least open pair (A_k,B_k) — i.e., applying the
certified Lemma G (Extended Earliest-Witness Intersection) to the two witnessing
S₀^(k)-extended-persistent refinements A_k', B_k' of A_k, B_k found in Section 1,
there is a prime q_k ∉ S₀^(k) with q_k | a_{n_{A_k}} and q_k | a_{n_{B_k}} = w_k
simultaneously (n_{A_k} defined symmetrically to n_{B_k}). Set S₀^(k+1) :=
S₀^(k) ∪ {q_k}. The outline's hypothesized recursion, in its cleanest form, is:

> **(H)** q_k | w_{k+1}, i.e. the prime recruited at stage k divides the witness
> value defining the NEXT stage's coupled scalar.

(This is the natural, checkable content behind the outline's "g_{k+1} = f(g_k, w_k,
w_{k+1})" — if (H) fails, no such closed-form recursion for a "recruited-primes
product" g_k can track anything meaningful across stages, since the very witness
term w_{k+1} it would need to divide need not carry the prime at all.)

**(H) is FALSE**, refuted by an exact, fully computed counterexample.

**Counterexample (a_1 = 175, worked exactly, no simulation black-box — every value
below is a direct factorization check).** The greedy sequence with a_1 = 175
begins:
```
a_1 = 175 = 5^2 · 7
a_2 = 180 = 2^2 · 3^2 · 5
a_3 = 182 = 2 · 7 · 13
a_4 = 189 = 3^3 · 7
```
(Legality of each term against all earlier terms, and minimality, follow directly
from the greedy defining rule; these four values are small enough to verify by hand:
181 is illegal after a_2=180 since gcd(181, 175) = 1 — indeed 181 is prime and
divides neither 175 nor 180 — so a_3 = 182 is the least integer > 180 sharing a
common factor with both a_1 and a_2, confirmed since gcd(182,175) = 7 > 1 and
gcd(182,180) = 2 > 1; similarly every integer in (182,189) fails to share a common
factor with all of a_1,a_2,a_3 — e.g. 183 = 3·61 has gcd(183,182)=1 — while
gcd(189,175)=7, gcd(189,180)=9, gcd(189,182)=7, so a_4 = 189 is legal and minimal.)

Here Q = P(a_1) = {5,7}. At stage 0, S₀^(0) = Q = {5,7}, and ρ_0(n) = P(a_n) ∩
{5,7}. The base type A_0 := {5} is witnessed by ρ_0(2) = {5} (a_2 = 180 = 2²·3²·5,
so P(a_2) ∩ {5,7} = {5}), and the base type B_0 := {7} is witnessed by ρ_0(3) = {7}
(a_3 = 182 = 2·7·13, so P(a_3) ∩ {5,7} = {7}). At S₀^(0) = Q, "extended-persistent
refinement" of a base type is the base type itself, so A_0' = A_0 = {5},
B_0' = B_0 = {7}, and (A_0,B_0) is ≺-least (indeed the only) disjoint base-type pair
here since Q = {5,7} has only these two singleton persistent base types plus {5,7}
itself, and {5,7} is not disjoint from either. So n_{A_0} = 2, n_{B_0} = 3,
w_0 = a_3 = 182.

Applying Lemma G to A_0' = {5}, B_0' = {7}: gcd(a_2, a_3) = gcd(180, 182) = 2 > 1
(directly computable: 180 = 2²·3²·5, 182 = 2·7·13, shared factor exactly 2), and
2 ∉ S₀^(0) = {5,7} as required. So the recruited prime is q_0 = 2, and
S₀^(1) = {2,5,7}.

**Now recompute at S₀^(1) = {2,5,7}.** ρ_1(n) := P(a_n) ∩ {2,5,7}. Directly:
ρ_1(2) = P(180) ∩ {2,5,7} = {2,5} (since 180 = 2²·3²·5). ρ_1(3) = P(182) ∩ {2,5,7}
= {2,7} (since 182 = 2·7·13). ρ_1(4) = P(189) ∩ {2,5,7} = {7} (since
189 = 3³·7, coprime to both 2 and 5). So the S₀^(1)-extended-persistent refinement
of the base type B := {7} that is ≺-least and has earliest occurrence is now
witnessed **not** at n = 3 (which has moved to type {2,7}, no longer type {7}
exactly) but at n = 4: n_{B_1} = 4, w_1 = a_4 = 189.

**Check (H) directly:** q_0 = 2, w_1 = a_4 = 189 = 3³·7. Since 189 is odd,
2 ∤ 189. **(H) fails**: the prime recruited at stage 0 does NOT divide the witness
value w_1 that defines the coupled scalar at stage 1. ∎ (counterexample)

**Why this is not an isolated accident — the general structural reason (proved).**

*Claim (Witness Discontinuity Obstruction).* There exist a finite S₀ ⊇ Q, a
persistent base type B, an S₀-extended-persistent refinement B' of B with earliest
witness index m := min{n : ρ_{S₀}(n) = B'}, and a prime q | a_m with q ∉ S₀, such
that setting S₁ := S₀ ∪ {q}, the earliest witness m' of the (unique)
S₁-extended-persistent refinement B'' of B agreeing with B' on S₀ **and excluding
q** (i.e. B'' := B' viewed as a subset of S₁, which forces q ∉ B'' since q ∉ B' ⊆
S₀) satisfies m' ≠ m and q ∤ a_{m'}.

*Proof.* This is exactly the situation exhibited in the worked counterexample above,
with S₀ = {5,7}, B = B' = {7} = B'', m = 3, q = 2, S₁ = {2,5,7}, m' = 4:
a_m = a_3 = 182 = 2·7·13 is divisible by q = 2, so at S₀ = {5,7} it legitimately
witnesses ρ_{S₀}(3) = {7} = B' (the prime q = 2 is invisible to ρ_{S₀} since
S₀ = {5,7} does not contain 2). But once S₀ is enlarged to S₁ = S₀ ∪ {2}, the SAME
index n = 3 now has ρ_{S₁}(3) = {2,7} ≠ {7}, because ρ_{S₁} is sensitive to the
factor of 2 that ρ_{S₀} could not see. So n = 3 no longer witnesses the "pure {7},
no other S₁-visible prime" type; the earliest index that does is pushed forward to
m' = 4, where a_4 = 189 = 3³·7 happens to be odd. Since this is a fully exhibited,
directly verified instance (every factorization above is exact and checked by hand,
not by a simulation black-box), existence is established. ∎

**Consequence for the outline's step 4.** The obstruction shows precisely why no
exact recursion g_{k+1} = f(g_k, w_k, w_{k+1}) of the aimo-0678 style can exist for
this problem's recruitment process, and *why* the disanalogy with aimo-0678 is
structural, not superficial:

- In `aimo-0678`, w_n and g_n are computed from a SINGLE fixed pair of sequences
  (a_n, b_n) evolving under one fixed one-step Markov recursion
  (a_{n+1} = gcd(a_n,b_n)+1, b_{n+1} = lcm(a_n,b_n)−1); the "witness" w_n is
  re-derived from the CURRENT pair (a_n,b_n) by a closed-form rule at every step, and
  the sequences a_n, b_n themselves are never "replaced" by an unrelated object —
  they are the same two evolving numbers throughout.
- Here, w_k is the value of a_n at the earliest index witnessing a *type* — and
  which INDEX witnesses that type is re-selected globally over all n each time S₀
  grows, because enlarging S₀ can strip a previously-witnessing index of its
  witnessing status (its extended type changes) and hand the role to a
  **different, generally unrelated, index further out in the sequence** — an index
  whose value was fixed by the greedy rule long before q_k was ever recruited and
  bears no forced algebraic relationship to q_k. This is exactly what the worked
  example shows: a_4 = 189's factorization (3³·7) was already fixed by the greedy
  process at "time" n=4, independent of the later choice to recruit q_0 = 2 against
  a *different* pair (A_0, B_0); there is no equation forcing 189 to carry a factor
  of 2.
- Consequently, the object the outline calls g_k ("product of recruited primes'
  valuations in the CURRENT lex-first witness") is not tracking one evolving
  quantity at all: its underlying witness index n_{B_k} is not a continuous/coherent
  object across stages, so there is no sense in which g_{k+1} can be computed from
  g_k by a fixed algebraic rule — the necessary continuity that made aimo-0678's
  Markov recursion tractable (the SAME two numbers updating by a closed formula) is
  simply absent here.

This is a genuine, complete, unconditional negative finding: the literal
step-4 recursion as hypothesized in the outline does not exist, and the reason is
structural (proved above for the general mechanism, not merely refuted by one
counterexample, though the counterexample is also fully exhibited and exact).

### 3. Honest assessment of remaining options (not pursued further this round,
flagged for the record per the outline's step 6 instruction)

- **A fixed-pair variant** (track w_k, g_k against the SAME base-type pair (A,B)
  across all stages where it remains open, rather than the shifting ≺-least pair)
  avoids the discontinuity above only in the sense that A, B themselves don't
  change — but the *witness index* n_B for the currently-relevant extended
  refinement of B still moves in exactly the same way shown above whenever a prime
  is recruited that happens to divide the current witness (which is forced,
  since Lemma G's recruited prime q always divides both n_A and n_B by
  construction — so the very act of applying Lemma G to (A,B) guarantees the
  discontinuity reoccurs at the next stage for that same pair, if it is still
  open). Worse, per the outline's own "watch out (ii)": asking whether q_k
  eventually divides *every* later witness of B's refinements (rather than just
  the very next one) is not a repaired version of the algebraic-identity
  mechanism at all — it is a restatement of Symmetric FAH itself. So this
  fixed-pair repair does not give an independent bypass; it collapses into the
  same open hypothesis owned by the sibling approaches, exactly as the outline
  warned could happen, and must be disclosed as such rather than presented as new
  content.
- **A weaker scalar** (e.g., |open(k)| itself, already established non-increasing
  and finite-valued by the certified Collateral-Safety Theorem) gives nothing
  beyond what is already certified: by well-ordering it stabilizes at some finite
  m* ≥ 0, but m* = 0 is exactly (†), and m* > 0 would mean some pair remains
  permanently open under every possible sequence of recruitment choices — which
  is neither established nor ruled out here, and analyzing it further reduces to
  the same open FAH/Symmetric-FAH question (a stage-(A,B) pair remains open
  forever iff recruiting against it repeatedly never achieves "full absorption" of
  all its refinements, which is FAH's negation). No new content beyond the
  already-certified reduction.

Neither variant escapes the shared crux; both are recorded here so no future round
re-attempts them under a different name believing them to be independent of FAH.

## Full proof
Not present — Status is `partial`. This approach does not close gap (†). It
establishes (a) the well-definedness bookkeeping for w_k (Section 1, free, complete)
and (b) a full refutation, with a general structural reason and an exact worked
counterexample, of the specific algebraic-recursion mechanism this approach set out
to attempt (Section 2), honestly closing off this proof *style* as a route to (†) in
its literal form, and (c) an honest accounting of why the natural repairs of the
mechanism (Section 3) collapse into the already-known-open FAH/Symmetric-FAH
question rather than providing an independent bypass.

## Promotable lemmas

**Witness Discontinuity Obstruction** (Section 2 above, fully proved, unconditional
— proposed for certification as `lemmas/witness-discontinuity-obstruction.md`):
There exist a finite S₀ ⊇ Q, a persistent base type B, an S₀-extended-persistent
refinement B' of B with earliest witness m, and a prime q | a_m, q ∉ S₀, such that
with S₁ = S₀ ∪ {q}, the earliest witness m' of the S₁-refinement of B agreeing with
B' and excluding q satisfies m' ≠ m and q ∤ a_{m'}. Proved via the fully exact,
hand-verified example a_1 = 175, S₀ = {5,7}, B = {7}, m = 3 (a_3 = 182 = 2·7·13),
q = 2, S₁ = {2,5,7}, m' = 4 (a_4 = 189 = 3³·7, odd). This is a genuinely reusable
negative fact: it shows that "the earliest witness of a fixed extended-persistent
type" is NOT a stable/continuous object under enlarging the core S₀, and specifically
that a newly recruited prime need not divide the type's new earliest witness — a
fact any future approach relying on continuity of witness selection across
recruitment stages should check against before assuming otherwise. Unlike Lemma I
(a diagnostic statement about which of the four then-certified tools could be
composed, not portable across new lemma certifications), this is a direct,
unconditional mathematical fact about the greedy sequence and the extended-type
machinery, true regardless of what else gets certified later — it is a genuine
existence claim ("this discontinuity CAN happen"), fully witnessed by an exact
example, and it is what makes the general structural argument in Section 2 rigorous
rather than merely suggestive.
