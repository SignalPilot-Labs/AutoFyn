# imo-2026-01 — confluence / unique normal form (Newman's lemma)

## Status
solved

## Approaches tried
- (round 1) Confluence via Newman's lemma on the MULTISET rewrite system. Part (a) via the lex potential (P, c) (product primary, count secondary) plus the radical-support invariant (exactly-one). Part (b) via: the multiset rewrite is terminating (part a) and locally confluent (critical-pair joinability, proven by a per-prime valuation analysis), hence confluent by Newman's lemma, hence every starting multiset has a unique normal form, hence the single surviving value M is independent of the move order. — Outcome: complete, both parts, no gaps. The per-prime local-confluence step rests on the Euclidean identity gcd(min(u,v),|u−v|)=gcd(u,v), the same algebraic core that powers the invariant approaches; the differentiator is the proof ARCHITECTURE (local confluence + Newman's lemma), which never needs to identify M by a formula. (Reviewer note: on POSITIONED boards local confluence fails — e.g. (2,3,2) — because the two branches land M in different positions; this is why the rewrite is defined on MULTISETS, where positions are quotiented out and the failure disappears. The problem's conclusion concerns only the value M, which is position-independent, so the multiset system is a faithful model.)

## Current best
A complete, rigorous proof of both parts. Part (a): termination by the well-founded lexicographic potential (P, c) where P = product of all entries (positive integer, non-increasing, strictly drops by a factor ≥2 on every non-coprime move) and c = count of entries >1 (non-increasing, drops by 1 on coprime or equal pairs); "exactly one >1" combines c ≤ 1 (no move left) with c ≥ 1 (radical-support invariant: the set of prime divisors of the total product is move-invariant and initially nonempty, so the product stays >1 forever). Part (b): the multiset rewrite is terminating (part a); it is locally confluent (the only non-trivial critical pair is two moves sharing one element — the "triple" {a,b,c} — and both branches reduce to the same normal form, shown by decomposing into per-prime valuations where the subtractive-Euclidean system is confluent with the unique normal form {gcd,0,…,0}); by Newman's lemma a terminating locally-confluent system is confluent; confluence gives a unique normal form; since a normal form has exactly one entry >1 (part a), that unique entry is M, independent of choices.

## Full proof

We restate the move. Given two board entries m, n > 1, let g = gcd(m, n).
Write m = g·x, n = g·y with gcd(x, y) = 1 (so x = m/g, y = n/g). Then the two
replacements are g and x·y. Indeed lcm(m, n) = g·x·y (since lcm(m,n)·gcd(m,n) =
m·n gives lcm = m·n/g = g·x·y), hence lcm(m,n)/gcd(m,n) = x·y. So a move sends
the pair (m, n) = (g·x, g·y) to (g, x·y). We record three immediate facts:

  (F1) The pair-product changes from m·n = g²·x·y to g·(x·y) = (m·n)/g.
  (F2) The product of the two outputs is g·(x·y) = lcm(m,n) = (m·n)/g.
  (F3) In p-adic valuations, the pair (α, β) = (v_p(m), v_p(n)) is sent to
       (min(α, β), |α − β|): for v_p(g) = min(α, β) (since g = gcd), and
       v_p(x·y) = v_p(x) + v_p(y) = (α − min(α,β)) + (β − min(α,β))
                = α + β − 2·min(α,β) = |α − β|   (WLOG α ≥ β ⇒ α − β).
       This is one subtractive-Euclidean step on the valuation pair.

The board always holds exactly 2026 entries (a move replaces two entries by two
entries), and entries equal to 1 are inert: no move ever selects a 1 (a move
requires both selected entries > 1).

────────────────────────────────────────────────────────────────
PART (a). Termination with exactly one entry > 1.
────────────────────────────────────────────────────────────────

Define two board quantities:
  • P = the product of all 2026 entries (a positive integer);
  • c = the number of entries strictly greater than 1 (an integer, 0 ≤ c ≤ 2026).

**Lemma A1 (P is non-increasing; it strictly drops on every non-coprime move).**
A move on the pair (m, n) with g = gcd(m, n) changes the pair-product from m·n to
(m·n)/g (fact F2). Every other entry is untouched, so P_new = P_old/g. If g = 1
(coprime pair) P is unchanged; if g ≥ 2 then P_new = P/g ≤ P/2, a strict drop
(and an integer, since g | m·n | P_old). ∎

**Lemma A2 (c is non-increasing; case split on the chosen pair).**
We split the chosen pair (m, n) into three disjoint cases.
  (i) gcd(m, n) ≥ 2 and m ≠ n. Then g ≥ 2 and the outputs are (g, x·y) with
      x, y coprime and not both 1 (m ≠ n ⟹ not (x = y = 1)). So x·y ≥ 2: if one
      of x, y equals 1 the other is ≥ 2 (coprime, not both 1); if both ≥ 2 their
      product is ≥ 4. Hence both outputs are > 1, and the pair's contribution to c
      is 2 before and 2 after: c is unchanged.
  (ii) gcd(m, n) = 1 (forcing m ≠ n, for if m = n then g = m ≥ 2). The outputs
       are (1, m·n); the entry 1 contributes 0 to c and m·n > 1 contributes 1,
       versus the pair's old contribution of 2. So c drops by 1.
  (iii) m = n (so g = m ≥ 2). The outputs are (m, m/m) = (m, 1): one entry > 1
        and one entry equal to 1, contribution 1, down from 2. So c drops by 1.
These three cases are exhaustive and disjoint (they partition by "coprime" /
"equal" / "non-coprime distinct"), so c never increases, and it drops by exactly
1 in cases (ii) and (iii) and is fixed in case (i). ∎

**Lemma A3 (termination).** Order boards by the lexicographic potential
(P, c) with P primary. Lemmas A1–A2 show (P, c) is non-increasing in lex order
under every move, and it strictly decreases: in case (i) P strictly drops (c
fixed); in cases (ii),(iii) P is fixed and c strictly drops. The lexicographic
order on ℕ² is well-founded (there is no infinite strictly decreasing sequence:
P is a positive integer that can strictly drop only finitely many times, and
between two drops of P, the secondary coordinate c — a non-negative integer —
can strictly drop only finitely many times). Hence no infinite sequence of
moves exists; the process terminates. ∎

(Equivalently: suppose infinitely many moves. P is a positive integer and
non-increasing, so it stabilises after finitely many strict drops; from then on
every move has g = 1 (else P would drop, contradicting stabilisation), so every
move is of type (ii) and c drops by 1 each time — but c is a non-negative
integer, so after finitely many such moves c < 2 and no move remains, a
contradiction.)

**Lemma A4 (radical-support invariance).** The set of prime divisors of the
total product P is invariant under moves. A move on (m, n) replaces the pair by
(g, x·y) with g·(x·y) = lcm(m, n). The prime divisors of the new pair are
primes(g) ∪ primes(x·y) = primes(g·(x·y)) = primes(lcm(m, n)) = primes(m) ∪
primes(n) (the last equality because lcm(m, n) carries every prime dividing m or
n and no other: v_p(lcm) = max(v_p(m), v_p(n))). So the pair's prime support is
unchanged, hence the prime support of P is unchanged. ∎

**Lemma A5 (exactly one entry > 1 at termination).** At a terminal board no
move is possible, which requires fewer than two entries > 1, i.e. c ≤ 1. By
Lemma A4 the radical (prime support) of P is invariant and is non-empty
initially (every one of the 2026 entries is > 1, hence has a prime divisor), so
P > 1 at every board, in particular at termination. If c = 0 then every entry
is 1 and P = 1, contradicting P > 1; hence c ≥ 1. Together c = 1: exactly one
entry M > 1 remains (the other 2025 entries are all 1). ∎

This completes part (a): the process always terminates with exactly one entry
greater than 1. ∎_part(a)

────────────────────────────────────────────────────────────────
PART (b). M is independent of the choices — via confluence.
────────────────────────────────────────────────────────────────

We prove that any complete play from a fixed starting board reaches the same M,
by establishing confluence of an associated rewrite system. Because the
conclusion concerns only the value M (which does not depend on which position
holds it), we model a board as a MULTISET of integers (forgetting positions).
This is faithful: the value M at a terminal board is determined by the multiset
(the sole non-1 entry), and the move on a multiset is well-defined — pick two
values > 1, remove one copy of each, insert gcd(m, n) and lcm(m, n)/gcd(m, n).

**The multiset rewrite system R.** States are multisets of 2026 positive
integers. A move (redex) picks two values m, n > 1 in the multiset and replaces
one copy of each by g = gcd(m, n) and x·y = lcm(m, n)/gcd(m, n). A normal form
is a state admitting no move, i.e. at most one value > 1; by Lemma A5 every
normal form is {M, 1, 1, …, 1} for a single M > 1 (and 2025 ones). We will show
every state has a UNIQUE normal form, which pins M independent of the move order.

We invoke a standard tool of abstract rewriting:

> **Newman's lemma.** If an abstract rewrite system is strongly normalizing
> (terminating: no infinite reductions) and locally confluent (every one-step
> divergence rejoins: whenever S → S₁ and S → S₂, the states S₁ and S₂ have a
> common reduct), then it is confluent (every divergence rejoins). A terminating
> confluent system has a unique normal form for every starting state.

R is terminating (Lemma A3, which applies verbatim to multisets). It remains to
prove local confluence.

**Reduction of local confluence to two structural cases.** Suppose two
different moves are possible from a multiset S, leading to S₁ (move on the pair
of values {a, b}) and S₂ (move on the pair {c, d}). The two pairs of selected
multiset elements share 0, 1, or 2 elements.

  (C1) Disjoint redexes — the two moves consume disjoint multiset elements
       (no single copy is contested; if a value appears in both pairs but
       with multiplicity ≥ 2, the moves take different copies and are
       disjoint). The two moves then touch disjoint sets of copies, so they
       commute: performing move {a,b} then move {c,d} (on the still-present
       copies) yields the same multiset as performing them in the opposite
       order — both remove their own two copies and add their own two
       outputs, independently. Hence S₁ and S₂ each reach this common
       multiset in one further move. Joinable. ✓

  (C2) Two pairs sharing two elements. Then the pairs are identical as
       multiset operations (removing the same two values), so the "two moves"
       coincide — not a genuine divergence. No critical pair. ✓

  (C3) Overlapping redexes — the pairs share exactly one multiset element (the
       shared value a is present in a single copy that both moves would
       consume; the values a, b, c need not be pairwise distinct, but b ≠ c as
       values else the two moves coincide — see the note below). Writing the
       common remainder of the board as R (untouched by both moves), the two
       resulting boards are
         S₁ = R ∪ { gcd(a,b),  lcm(a,b)/gcd(a,b),  c }    (move on {a, b}),
         S₂ = R ∪ { gcd(a,c),  b,                   lcm(a,c)/gcd(a,c) }  ({a, c}).
       This is the only non-trivial critical pair, and is the crux.
       (Note on the case split: when the shared value a has multiplicity ≥ 2 in
       the multiset, the two moves consume DIFFERENT copies of a and are in
       fact disjoint — case (C1) — and commute. The genuine overlap (C3) arises
       precisely when a single copy is contested. The values b, c are the
       values of the non-shared copies in the two pairs; b ≠ c as values is
       exactly the condition that the two pairs are different moves. The value
       a may coincide with b or c (e.g. a = b = 2 when two distinct copies of 2
       play the roles of a and b), which is permitted: the per-prime analysis
       below handles all (α, β, γ), including α = β.)

────────────────────────────────────────────────────────────────
THE CRUX: the overlapping critical pair rejoins (Lemma C).
────────────────────────────────────────────────────────────────

We prove that S₁ and S₂ (with common context R) have a common reduct. The
vehicle is a per-prime valuation analysis. We first establish confluence of a
simpler, per-prime system, then lift.

**Lemma P (subtractive-Euclidean confluence).** Consider the rewrite on finite
MULTISETS of non-negative integers, where a move picks two POSITIVE entries
u, v and replaces them by (min(u, v), |u − v|). This system is confluent;
moreover every multiset reduces to the unique normal form {d, 0, …, 0} where
d = gcd of all entries of the starting multiset (with gcd(x, 0) = x).

*Proof of Lemma P.* We verify the three ingredients.

  (P-termination) Define the weight W = Σ (sum of all entries). When u, v > 0
  are replaced by (min(u,v), |u−v|), their contribution changes from u + v to
  min(u,v) + |u − v|. But min(u,v) + |u − v| = max(u, v) = u + v − min(u,v),
  and min(u, v) ≥ 1 (both positive), so the contribution strictly drops by
  min(u,v) ≥ 1; all other entries are unchanged. Hence W strictly decreases by
  at least 1 at every move. W is a non-negative integer, so the system
  terminates.

  (P-invariant) The gcd of all entries is invariant. We use the Euclidean
  identity
    gcd(min(u, v), |u − v|) = gcd(u, v).                                       (∗)
  To prove (∗): if u ≥ v then min = v, |u − v| = u − v, and
  gcd(v, u − v) = gcd(v, u) = gcd(u, v) (the standard Euclidean step
  gcd(a, b) = gcd(a, b − a), here with a = v, b = u); if u < v the same
  argument with the roles swapped gives gcd(u, v − u) = gcd(u, v). So the gcd
  of the two replaced entries is unchanged, and the gcd of the whole multiset
  is preserved.

  (P-unique normal form) A normal form admits no move, so no two positive
  entries coexist: at most one entry is positive. If exactly one entry x is
  positive and the rest are 0, the gcd of the multiset is x (since
  gcd(x, 0, …, 0) = x); by invariance x = d. If all entries are 0 then d = 0.
  So the only normal form is {d, 0, …, 0}, uniquely determined by d, which is
  fixed by the start state.

  (P-confluence) A terminating system in which every element has a unique
  normal form is confluent: given any divergence x ↠ y₁, x ↠ y₂, extend both
  paths (by termination) to normal forms; both equal the unique normal form,
  hence y₁ and y₂ rejoin there. ∎

**Remark.** Lemma P is a statement about the per-prime valuation system only;
it is proved from scratch above (termination by the weight, the Euclidean
identity (∗) for the invariant, and the unique-normal-form characterization of
confluence). It does not assume anything about the board system.

**Lemma C (the overlapping critical pair rejoins).** Consider a board
multiset S in which two moves share exactly one element: the first move acts on
the value-pair {a, b}, the second on {a, c}, where a is the shared element (a
single copy), b ≠ c as values (else the two moves coincide), and a, b, c may
otherwise coincide as values (e.g. {a, b} = {2, 2} is allowed when a second
copy of 2 plays the role of b). Let R = S \ {the three involved copies} be the
(common) remainder of the board, untouched by both moves. Write
  S₁ = R ∪ { gcd(a,b),  lcm(a,b)/gcd(a,b),  c }     (after the move on {a,b}),
  S₂ = R ∪ { gcd(a,c),  b,                   lcm(a,c)/gcd(a,c) }  (after {a,c}).
Then S₁ and S₂ have a common reduct under R.

*Proof of Lemma C.* Both S₁ and S₂ reduce to normal forms by Lemma A3; call
them NF₁ = {M₁, 1, …, 1} and NF₂ = {M₂, 1, …, 1} (exactly one non-1 entry, by
Lemma A5; the 1's fill the remaining 2025 positions, and R has been absorbed
into the reduction). We prove M₁ = M₂ by showing v_p(M₁) = v_p(M₂) for every
prime p.

Fix a prime p and write (α, β, γ) = (v_p(a), v_p(b), v_p(c)); let ρ₁, ρ₂, …
be the p-valuations of the (common) entries of R. By fact (F3) the move on
{a, b} sends the valuation pair (α, β) to (min(α, β), |α − β|), so the
p-valuation multiset of S₁ is {min(α, β), |α − β|, γ} ∪ {ρ_i}; likewise the
p-valuation multiset of S₂ is {min(α, γ), β, |α − γ|} ∪ {ρ_i}.

Now run the board reduction S₁ ↠ NF₁ and project it to prime p: every board
move on two values (x, y) applies, at prime p, the subtractive-Euclidean step
(v_p(x), v_p(y)) → (min(v_p(x),v_p(y)), |v_p(x) − v_p(y)|) to that valuation
pair — a valid move of the system of Lemma P, touching the SAME two positions.
So the projected sequence is a legitimate reduction in the
subtractive-Euclidean system, from {min(α, β), |α − β|, γ} ∪ {ρ_i} to the
p-valuation multiset of NF₁, which is {v_p(M₁), 0, …, 0} (M₁ is the only non-1
entry of NF₁, so only it can carry a positive p-valuation; all 1's contribute
0).

By Lemma P this projected reduction must end at the UNIQUE normal form
{d₁, 0, …, 0}, where d₁ is the gcd of the starting multiset
{min(α, β), |α − β|, γ} ∪ {ρ_i}. By the Euclidean identity (∗) applied to the
first two entries (gcd(min(α,β), |α−β|) = gcd(α, β)), then gcd-folded with γ
and with every ρ_i:
  d₁ = gcd( min(α, β), |α − β|, γ, ρ₁, ρ₂, … )
     = gcd( α, β, γ, ρ₁, ρ₂, … ).
Hence {v_p(M₁), 0, …, 0} = {d₁, 0, …, 0}, i.e. v_p(M₁) = d₁.

The identical argument for S₂ gives v_p(M₂) = d₂, where
  d₂ = gcd( min(α, γ), β, |α − γ|, ρ₁, ρ₂, … )
     = gcd( α, γ, β, ρ₁, ρ₂, … )         (by (∗) on the first and third
                                           entries, then gcd with β and ρ_i)
     = gcd( α, β, γ, ρ₁, ρ₂, … ) = d₁.
So v_p(M₂) = d₂ = d₁ = v_p(M₁).

Therefore v_p(M₁) = v_p(M₂) for every prime p; since both M₁, M₂ are positive
integers, M₁ = M₂. The shared normal form NF₁ = NF₂ is a common reduct of S₁
and S₂, proving Lemma C. ∎

(Observe that the common context R contributes the valuations ρ_i identically
to d₁ and d₂; the only entries that can differ between the two branches are
the active triple's, and the Euclidean identity (∗) shows they contribute the
same gcd(α, β, γ) to both. The lift from per-prime confluence (Lemma P) to the
board critical pair is legitimate because Lemma P gives confluence — meaning
EVERY reduction schedule, including the particular one induced by the coupled
board moves, reaches the unique per-prime normal form — so no schedule
synchronization across primes is required.)

**Local confluence of R.** Combining cases (C1) and (C3) (with (C2) vacuous):
every one-step divergence from a multiset S rejoins — disjoint redexes commute
(C1), and the only non-trivial critical pair, the overlapping triple (C3),
rejoins by Lemma C. So R is locally confluent.

**Confluence of R (Newman's lemma).** R is terminating (Lemma A3) and locally
confluent; by Newman's lemma R is confluent. Hence every starting multiset has
a UNIQUE normal form.

**M is independent of choices.** A normal form is, by Lemma A5, a multiset
{M, 1, …, 1} with a single non-1 entry. Confluence gives a unique normal form
for the starting multiset, hence a unique value M, regardless of the order in
which Confucius selects pairs. ∎_part(b)

────────────────────────────────────────────────────────────────
Combining parts (a) and (b): regardless of the choices made, after finitely
many moves exactly one integer M > 1 remains, and M depends only on the initial
multiset (not on the move order). ∎
────────────────────────────────────────────────────────────────

## Promotable lemmas

- **Lemma P — subtractive-Euclidean confluence.** The rewrite on finite
  multisets of non-negative integers, where a move picks two positive entries
  (u, v) and replaces them by (min(u, v), |u − v|), is confluent, with the
  unique normal form {d, 0, …, 0} where d = gcd of the starting multiset (with
  gcd(x, 0) = x). Proved from scratch via: termination by the weight Σ (which
  strictly drops by min(u,v) ≥ 1), the Euclidean identity
  gcd(min(u,v),|u−v|) = gcd(u,v) for the invariant, and the
  unique-normal-form characterization of confluence for terminating systems.
  (Proved in approach `confluence-unique-normal-form`, Lemma P.)

- **Lemma (radical-support invariance).** The set of prime divisors of the
  product of all board entries is invariant under the move
  (m, n) → (gcd(m,n), lcm(m,n)/gcd(m,n)): primes of the new pair equal
  primes(gcd) ∪ primes(lcm/gcd) = primes(lcm) = primes(m) ∪ primes(n).
  (Proved in approach `confluence-unique-normal-form`, Lemma A4.)

- **Lemma (the move is (min, |α−β|) on p-valuations).** Under the move
  (m, n) → (gcd(m,n), lcm(m,n)/gcd(m,n)), the p-adic valuation pair
  (v_p(m), v_p(n)) = (α, β) is sent to (min(α,β), |α−β|), because
  v_p(gcd) = min(α,β) and v_p(lcm/gcd) = max(α,β) − min(α,β) = |α−β|.
  (Fact (F3) in approach `confluence-unique-normal-form`.)
