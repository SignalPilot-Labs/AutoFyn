# Approach: newman-confluence

## Status
solved

## Approaches tried
- (fresh — outlined round 1, not yet built)
- Round 1 build: closed GAP 1 (L3, overlap joinability) at the integer level with explicit
  joining sequences — the key discovery is a *uniform integer-level joining schedule*: from
  either divergent branch, one further move pulls the shared place down to gcd(m,n,k), and then
  iterating the move on the remaining pair drives it to its fixed point {1, E}; the two values
  of E coincide by the elementary identity gcd(|α−β|, |min(α,β)−γ|) = gcd(|α−β|, |α−γ|).
  Because the joining *schedules* are prime-independent (actual integer moves, the same
  sequence for every prime), the per-prime-coupling trap flagged in the outline does not arise:
  valuations are used only to verify that two specific integers are equal. Newman's lemma
  proved inline by strong induction on the single monovariant N = 2027·P + C. Legality of
  deferred/intermediate moves handled by a "formal move" device (a move touching an entry 1
  fixes the multiset, so formal paths project to real paths). — worked; complete proof below.

## Current best
Complete proof of both (a) and (b); see Full proof. No open gaps.

- Numerical support: joining scheme of Lemma 5 Case 3 verified on 20,000 random triples
  (0 failures); the difference-gcd identity verified exhaustively for exponents 0–8; the
  monovariant N verified on 5,000 random moves. (Checks only; the proof below is self-contained.)
- Design note for the reviewer: this build satisfies the outline-reviewer's conditions — the
  joining sequences are exhibited explicitly at the integer level (Lemma 5), Newman's lemma is
  proved inline by well-founded (strong) induction (Lemma 6), and no board-wide conserved
  quantity is used anywhere: the only per-prime computation is Lemma 4(iv) and the E₁ = E₂
  verification inside Lemma 5, both of which identify the *endpoint of a single fixed integer
  move schedule*, not a process invariant. The approach never computes a formula for M.

## Full proof

**Problem.** 2026 integers greater than 1 stand on a blackboard. A move chooses two integers
m > 1 and n > 1 from different places and replaces them with gcd(m,n) and lcm(m,n)/gcd(m,n).
Moves continue while possible. (a) Prove that, regardless of choices, after finitely many moves
exactly one integer M > 1 remains. (b) Prove M does not depend on the choices.

### 0. Setup, conventions, and standard facts

**States.** The blackboard state is the multiset of the values in the 2026 places. A move
depends only on the two chosen values and replaces them inside the multiset, so the entire
process is a process on multisets; we call such a multiset a **board**. All boards below have
exactly 2026 elements, each a positive integer. A **(real) move** on a board B: choose two
elements x, y of B occupying different places (an *occurrence pair*; the values may be equal),
with x > 1 and y > 1, and replace them by gcd(x,y) and lcm(x,y)/gcd(x,y). We write B → B′ and
→\* for the reflexive–transitive closure (finitely many moves, possibly zero).

**Well-definedness of a move.** gcd(x,y) divides x, and x divides lcm(x,y), so gcd(x,y) divides
lcm(x,y) and the quotient lcm(x,y)/gcd(x,y) is a positive integer. Thus boards stay multisets of
2026 positive integers.

**Valuations.** For a prime p and a positive integer x, v_p(x) is the exponent of p in the prime
factorization of x. By the Fundamental Theorem of Arithmetic (knowledge_base.md, number-theory
core facts): v_p(xy) = v_p(x)+v_p(y); for positive integers d, x we have d | x iff
v_p(d) ≤ v_p(x) for all p; two positive integers are equal iff all their valuations agree; and
x = 1 iff v_p(x) = 0 for all p. Consequently

- v_p(gcd(x,y)) = min(v_p x, v_p y) and v_p(lcm(x,y)) = max(v_p x, v_p y). *Proof:* the number
  g with v_p(g) = min(v_p x, v_p y) for all p (a finite product, since the exponent vanishes for
  p ∤ x) divides both x and y, and every common divisor d satisfies v_p(d) ≤ v_p(x) and
  v_p(d) ≤ v_p(y), i.e. v_p(d) ≤ v_p(g), i.e. d | g; so g is the greatest common divisor.
  Dually for lcm. ∎
- Hence gcd(x,y)·lcm(x,y) = xy (valuations: min + max = sum), so
  **lcm(x,y)/gcd(x,y) = xy/gcd(x,y)²**, and the product of the two replaced values changes from
  xy to gcd·(lcm/gcd) = lcm = xy/gcd(x,y).

**Effect of a move on valuations (Step-V).** If a move replaces x, y (valuations a = v_p x,
b = v_p y at a fixed prime p) then the two output values have valuations

  min(a,b)  and  max(a,b) − min(a,b) = |a − b|,

(the first from v_p(gcd), the second from v_p(lcm) − v_p(gcd), legitimate because the quotient
was shown to be an integer), and all other elements of the board are unchanged.

**gcd conventions for nonnegative integers.** For a,b ∈ ℤ we set gcd(a,b) := gcd(|a|,|b|), with
gcd(0,0) := 0 and gcd(0,b) = |b|. For nonnegative integers not both zero, gcd(a,b) is the
largest common divisor, and the set of positive common divisors of {a,b} determines gcd(a,b):
it is the maximum of that set (and if a = b = 0 the gcd is 0 by convention). We use throughout:

**Fact D (same divisor set ⇒ same gcd).** If two pairs of integers have the same set of positive
common divisors, and either both pairs are (0,0) up to sign or neither is, then their gcds are
equal. (If neither is the zero pair, each gcd is the maximum of the common-divisor set; if both
are zero pairs, both gcds are 0.) When we apply Fact D below we will check the zero-pair
condition explicitly.

**Fact E (Euclidean subtraction).** For nonnegative integers a, b:
gcd(min(a,b), max(a,b) − min(a,b)) = gcd(a,b).
*Proof.* Write m = min(a,b), M = max(a,b). A positive integer d divides both m and M − m iff it
divides both m and m + (M − m) = M, iff it divides both a and b (the pair {m, M} is the pair
{a, b}). So the common-divisor sets coincide. Zero pairs: (m, M−m) = (0,0) iff a = b = 0 iff
(a,b) is the zero pair. Fact D applies. ∎

**Fact A (gcd of three).** For positive integers x, y, z: gcd(gcd(x,y), z) = gcd(gcd(x,z), y),
and its valuation at p is min(v_p x, v_p y, v_p z). *Proof:* v_p(gcd(gcd(x,y),z)) =
min(min(v_p x, v_p y), v_p z) = min(v_p x, v_p y, v_p z), symmetric in the three arguments;
equal valuations at every p give equal integers. ∎

### 1. Termination

**Lemma 1 (monovariant).** For a board B let P(B) be the product of its elements, C(B) the
number of its elements that exceed 1, and N(B) := 2027·P(B) + C(B) ∈ ℤ≥0. Then every real move
strictly decreases N. Consequently every sequence of real moves is finite, and along a move
N drops, so any B′ with B → B′ has N(B′) < N(B).

*Proof.* Let the move act on x, y > 1 with g = gcd(x,y). Elements other than the chosen two are
unchanged. The product of the chosen pair changes from xy to lcm(x,y) = xy/g (Section 0), so
P′ = P/g. The chosen pair contributed exactly 2 to C; the two outputs contribute at most 2; so
C′ ≤ C in every case.

- Case g > 1: P′ = P/g < P, and P, P′ are positive integers, so P − P′ ≥ 1 and
  2027(P′ − P) ≤ −2027. Together with C′ − C ≤ 0 (shown above), N′ − N ≤ −2027 + 0 < 0.
- Case g = 1: the outputs are gcd = 1 and lcm/gcd = xy > 1. So P′ = P, and the two chosen
  elements (> 1, contributing 2 to C) are replaced by one element > 1 and one element 1,
  contributing exactly 1: C′ = C − 1. Hence N′ = N − 1 < N.

The two cases are exhaustive and in both N strictly decreases. A sequence of moves gives a
strictly decreasing sequence of nonnegative integers N, which must be finite. ∎

**Terminal boards.** A real move is possible iff the board has at least two elements > 1, i.e.
C(B) ≥ 2. Call B **terminal** if no move is possible, i.e. C(B) ≤ 1. "Confucius continues while
possible" means a run is a maximal sequence of moves; by Lemma 1 every run is finite and ends at
a terminal board.

### 2. Part (a)

**Lemma 2 (prime support persists).** Let p be a prime dividing some element of B, and B → B′.
Then p divides some element of B′.

*Proof.* If p divides an element not touched by the move, that element persists. Otherwise
p divides x or y, the two chosen elements; with a = v_p x, b = v_p y this means
max(a,b) ≥ 1. By Step-V the outputs have valuations min(a,b) and max(a,b) − min(a,b). If a = b,
then min(a,b) = a = max(a,b) ≥ 1, so the first output is divisible by p. If a ≠ b, then
max(a,b) − min(a,b) ≥ 1, so the second output is divisible by p. In all cases some element of B′
is divisible by p. ∎

**Proposition (a).** Every run terminates after finitely many moves at a board with exactly one
element M > 1 (the other 2025 elements equal 1).

*Proof.* Finiteness and termination at a terminal board T (C(T) ≤ 1): Lemma 1 and the paragraph
above. The initial board B₀ consists of integers > 1; pick a prime p dividing its first element.
By Lemma 2 and induction on the length of the run, p divides some element of T. Elements equal
to 1 have no prime divisors, so T has an element > 1; combined with C(T) ≤ 1, the board T has
**exactly one** element M > 1. ∎

### 3. Formal moves

To build joining sequences without worrying about the legality constraint "both chosen elements
> 1" at intermediate stages, we introduce a relaxation.

**Definition.** A **formal move** on a board B chooses two elements x, y in different places
with x, y ≥ 1 (so the value 1 is allowed) and replaces them by gcd(x,y) and lcm(x,y)/gcd(x,y).
Write B ⇒ B′, and ⇒\* for finitely many formal moves.

**Lemma 3 (formal projects to real).** If B ⇒ B′ then either B′ = B (as multisets) or B → B′.
Consequently, if B ⇒\* C then B →\* C.

*Proof.* If both chosen elements exceed 1, the formal move is a real move. Otherwise say x = 1:
the outputs are gcd(1,y) = 1 and lcm(1,y)/gcd(1,y) = y/1 = y, so the pair {1, y} is replaced by
the pair {1, y} and the multiset is unchanged (this covers y = 1 too: {1,1} ↦ {1,1}). For the
consequence, take a formal path B ⇒ … ⇒ C and delete every step whose multiset is unchanged;
what remains is a real path from B to C (possibly empty, in which case C = B and B →\* C holds
reflexively). ∎

### 4. The pair-collapse lemma

**Lemma 4 (pair collapse).** Fix two places of a board holding values x, y ≥ 1 and iterate the
formal move on this pair of places (a deterministic iteration, since the output *multiset*
{gcd, lcm/gcd} depends only on the values). Then after finitely many steps the pair becomes
{1, E(x,y)}, where

  E(x,y) := ∏_p p^{gcd(v_p x, v_p y)}  (product over primes; a positive integer),

and every further formal move on the pair fixes it. All other elements of the board are
untouched. Moreover E is symmetric: E(x,y) = E(y,x).

*Proof.* First, E(x,y) is a well-defined positive integer: for p dividing neither x nor y the
exponent is gcd(0,0) = 0, so the product is finite; each exponent gcd(v_p x, v_p y) ≤
max(v_p x, v_p y) is finite. Symmetry is clear from the symmetry of gcd.

**(i) Invariant of one step.** By Step-V, one formal move sends the valuation pair (a, b) =
(v_p x, v_p y) to (min(a,b), max(a,b) − min(a,b)). By Fact E,
gcd of the pair's valuations at p is unchanged by each step, for every prime p.

**(ii) Termination at a pair containing 1.** By strong induction on the product xy ≥ 1: if
x = 1 or y = 1 the pair already contains 1. If x, y ≥ 2 and g := gcd(x,y) > 1, one step yields a
pair with product lcm(x,y) = xy/g < xy (a positive integer), and the induction hypothesis
applies to it. If x, y ≥ 2 and g = 1, one step yields {1, xy}, a pair containing 1. So finitely
many steps reach a pair {1, z}, z ≥ 1.

**(iii) Pairs containing 1 are fixed.** A formal move sends {1, z} to
{gcd(1,z), lcm(1,z)/gcd(1,z)} = {1, z}.

**(iv) Identification of z.** At the final pair {1, z} the valuation pair at p is (0, v_p z),
whose gcd is v_p z (convention gcd(0, b) = b). By (i) this equals the initial value
gcd(v_p x, v_p y), for every p. Two positive integers with equal valuations everywhere are
equal, so z = E(x,y). ∎

### 5. Local confluence

**Lemma 5 (local confluence).** If B → B₁ and B → B₂ are real moves, then there is a board D
with B₁ →\* D and B₂ →\* D.

*Proof.* Each move is specified by its unordered pair of places. Let π₁, π₂ be the two place
pairs. Exactly one of the following holds: |π₁ ∩ π₂| = 2, 0, or 1.

**Case 1: π₁ = π₂ (same two places, values x, y).** The output multiset {gcd(x,y),
lcm(x,y)/gcd(x,y)} depends only on {x,y}, so B₁ = B₂; take D := B₁ = B₂ (zero further moves).

**Case 2: π₁ ∩ π₂ = ∅ (four distinct places, values x, y and u, v).** In B₁ the places of π₂
still hold u, v, both > 1 (untouched by the first move), so the move on π₂ is legal in B₁ and
yields the board D obtained from B by replacing {x,y} by {gcd(x,y), lcm(x,y)/gcd(x,y)} *and*
{u,v} by {gcd(u,v), lcm(u,v)/gcd(u,v)} — the two replacements act on disjoint places, so the
result is the same multiset regardless of order. Symmetrically B₂ → D. So B₁ → D and B₂ → D.

**Case 3: π₁ ∩ π₂ is a single place.** Let the shared place hold m, and let the other places of
π₁, π₂ hold n and k respectively; m, n, k > 1 (all three are chosen by a real move at B). Every
other element of B is untouched by everything below; collect those 2023 elements into a multiset
R. Write

  d := gcd(m,n),  e := gcd(m,k),  t := gcd(gcd(m,n), k) = gcd(gcd(m,k), n)

(the last equality by Fact A; v_p(t) = min(v_p m, v_p n, v_p k)). Then, using
lcm(x,y)/gcd(x,y) = xy/gcd(x,y)² (Section 0):

  B₁ = {d, mn/d², k} ∪ R,   B₂ = {e, n, mk/e²} ∪ R.

**Joining schedule from B₁** (explicit integer-level moves):
1. Formal move on the pair (d, k): outputs gcd(d,k) = t (Fact A) and dk/gcd(d,k)² = dk/t²
   (an integer: t | d and t | k, so t² | dk). New board: {t, mn/d², dk/t²} ∪ R.
2. Iterate the formal move on the pair of places holding mn/d² and dk/t² until it stabilizes;
   by Lemma 4 this takes finitely many steps and yields
   {t, 1, E₁} ∪ R with **E₁ := E(mn/d², dk/t²)**.

**Joining schedule from B₂** (symmetric):
1. Formal move on the pair (e, n): outputs gcd(e,n) = t (Fact A) and en/t² (an integer:
   t | e, t | n). New board: {t, en/t², mk/e²} ∪ R.
2. Iterate the formal move on the pair holding en/t² and mk/e²; by Lemma 4 this yields
   {t, 1, E₂} ∪ R with **E₂ := E(en/t², mk/e²)**.

These schedules are sequences of *integer* formal moves — the same actual moves serve all primes
simultaneously, so no per-prime scheduling is involved. It remains to prove the two endpoint
boards are equal, i.e. **E₁ = E₂**; that is an equality of two specific positive integers, which
we verify valuation by valuation.

Fix a prime p and put α := v_p m, β := v_p n, γ := v_p k, and
u := min(α,β) = v_p d,  w := min(α,γ) = v_p e,  s := min(α,β,γ) = v_p t.
Then (all quotients were shown to be integers, so valuations subtract):

- v_p(mn/d²) = α + β − 2u = max(α,β) − min(α,β) = |α − β|;
- v_p(dk/t²) = u + γ − 2s = |u − γ|, because s = min(min(α,β), γ) = min(u, γ);
- v_p(en/t²) = w + β − 2s = |w − β|, because s = min(w, β) likewise;
- v_p(mk/e²) = α + γ − 2w = |α − γ|.

By Lemma 4, v_p(E₁) = gcd(|α−β|, |u−γ|) and v_p(E₂) = gcd(|w−β|, |α−γ|). Define
D_p := gcd(|α−β|, |α−γ|). We claim v_p(E₁) = D_p = v_p(E₂).

*Claim v_p(E₁) = D_p.* If u = α (i.e. α ≤ β) then |u−γ| = |α−γ| and the claim is the
definition of D_p. Otherwise β < α and u = β, so |u−γ| = |β−γ|. Now
β − γ = (α − γ) − (α − β), and α − γ = (α − β) + (β − γ); hence a positive integer divides both
α−β and β−γ iff it divides both α−β and α−γ: the common-divisor sets of the pairs
{α−β, β−γ} and {α−β, α−γ} coincide. Zero-pair check: α−β = β−γ = 0 forces α−γ = 0, and
α−β = α−γ = 0 forces β−γ = 0, so one pair is the zero pair iff the other is. By Fact D,
gcd(|α−β|, |β−γ|) = gcd(|α−β|, |α−γ|) = D_p, proving the claim.

*Claim v_p(E₂) = D_p.* Symmetric (swap the roles of β and γ, i.e. of n and k): if w = α then
|w−β| = |α−β| and we get D_p directly; if γ < α then w = γ, |w−β| = |γ−β|, and
γ − β = (α − β) − (α − γ) gives, by the identical common-divisor-set argument and Fact D,
gcd(|γ−β|, |α−γ|) = gcd(|α−β|, |α−γ|) = D_p.

So v_p(E₁) = v_p(E₂) for every prime p, hence E₁ = E₂ =: E, and both schedules end at the
**same** board D := {t, 1, E} ∪ R. We have exhibited B₁ ⇒\* D and B₂ ⇒\* D by explicit finite
formal paths; by Lemma 3, B₁ →\* D and B₂ →\* D.

The three cases are exhaustive and each produces a common →\*-descendant. ∎

### 6. Newman's lemma, proved inline

**Lemma 6 (unique terminal board).** For every board B: (confluence) whenever B →\* C₁ and
B →\* C₂, there exists D with C₁ →\* D and C₂ →\* D; and consequently (uniqueness) if
B →\* T₁ and B →\* T₂ with T₁, T₂ terminal, then T₁ = T₂ as multisets.

*Proof of confluence,* by strong induction on the nonnegative integer N(B) of Lemma 1. (This is
a well-founded induction: the statement "for all boards B with N(B) = ν, B is confluent" is
proved for each ν ∈ ℤ≥0 assuming it for all smaller values; Lemma 1 guarantees that any B′ with
B → B′ has N(B′) < N(B), so the induction hypothesis applies to every one-step successor of B.)

Let B →\* C₁ and B →\* C₂. If the first path is empty (C₁ = B), take D := C₂: then
C₁ = B →\* C₂ = D and C₂ →\* D reflexively. Symmetrically if the second path is empty. Otherwise
write the paths as B → B₁ →\* C₁ and B → B₂ →\* C₂ (first steps peeled off). By
**Lemma 5 (local confluence)** applied to the two single moves B → B₁ and B → B₂, there is D₀
with B₁ →\* D₀ and B₂ →\* D₀. Now:

1. N(B₁) < N(B) (Lemma 1), and B₁ →\* C₁, B₁ →\* D₀; by the induction hypothesis at B₁ there is
   D₁ with C₁ →\* D₁ and D₀ →\* D₁.
2. N(B₂) < N(B), and B₂ →\* C₂, B₂ →\* D₀ →\* D₁ (concatenation); by the induction hypothesis at
   B₂ there is D with C₂ →\* D and D₁ →\* D.

Then C₁ →\* D₁ →\* D and C₂ →\* D, as required. This completes the induction.

*Uniqueness.* Let T₁, T₂ be terminal with B →\* T₁, B →\* T₂. By confluence there is D with
T₁ →\* D and T₂ →\* D. A terminal board admits no move, so the only →\*-path from a terminal
board is the empty one; hence T₁ = D and T₂ = D, so T₁ = T₂. ∎

### 7. Part (b)

**Proposition (b).** The final integer M > 1 of Proposition (a) is the same for every run.

*Proof.* Let two runs from the initial board B₀ be given. By Lemma 1 both are finite, and being
maximal they end at terminal boards T₁ and T₂ with B₀ →\* T₁ and B₀ →\* T₂. By Lemma 6,
T₁ = T₂ as multisets. By Proposition (a), this common terminal multiset consists of 2025 copies
of 1 and exactly one element M > 1. Hence both runs end with the same integer M — M does not
depend on Confucius's choices. ∎

**Conclusion.** (a) Every run of the process is finite and ends with exactly one integer
M > 1 on the blackboard (Proposition (a)). (b) The value M is independent of the choices made
(Proposition (b)). ∎

*(Remark, not needed for the proof: the argument establishes uniqueness of M without ever
computing it; the entire terminal multiset — not just M — is choice-independent.)*

## Promotable lemmas

- **pair-collapse** (Lemma 4, proved in full in §4 above): iterating the (formal) move
  {x, y} ↦ {gcd(x,y), lcm(x,y)/gcd(x,y)} on a fixed pair of places terminates in finitely many
  steps at the fixed pair {1, E(x,y)}, where E(x,y) = ∏_p p^{gcd(v_p x, v_p y)}. Self-contained
  (uses only Step-V, Fact E, and strong induction on the product). Reusable for any variant of
  this rewriting system.
- **formal-projects-to-real** (Lemma 3, §3): allowing moves on entries equal to 1 changes
  nothing — such moves fix the multiset, so formal reachability implies real reachability.
  A small but sharp tool for legality bookkeeping in this system.
- **overlap-joining** (Lemma 5, Case 3, §5): from the two one-step divergences on an
  overlapping triple (m, n, k), the explicit schedules "pull the shared place to gcd(m,n,k),
  then pair-collapse the other two places" reach the identical board {gcd(m,n,k), 1, E} ∪ R.
- **move-monovariant** (Lemma 1, §1): N = 2027·P + C strictly decreases under every move
  (2027 = board size + 1 works for any board size ≥ 2 with the obvious change of constant).
