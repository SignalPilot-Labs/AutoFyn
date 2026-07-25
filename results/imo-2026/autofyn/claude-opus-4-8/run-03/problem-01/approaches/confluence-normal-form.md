## Status
unsolved

## Approach: elementary (a) + order-independence of M via rewriting-system confluence

Framing: treat the board process as an abstract terminating rewriting system and prove
part (b) as UNIQUENESS OF THE NORMAL FORM — never computing a closed form for M. Part (a)
is proved by a fully elementary, prime-free monovariant. This is the framing furthest from
the "compute M = ∏ p^{g_p}" route: it establishes order-independence directly, structurally.

### Target
(a) exactly one entry >1 survives after finitely many moves; (b) its value M is the same
for every sequence of choices (order-independence), proved WITHOUT a closed form.

### Skeleton — part (a) (prime-free)
1. Product monovariant. P = ∏_i a_i. A move replaces m,n by (g,ℓ) with g·ℓ = lcm(m,n) =
   mn/gcd(m,n) ≤ mn, so P is non-increasing, and strictly drops by a factor gcd(m,n)≥2 when
   gcd(m,n)>1. — by g·ℓ = lcm(m,n).
2. Active-count. A = #{entries >1}. When gcd(m,n)=1 the outputs are (1, mn): A drops by 1.
   A never increases (only two slots touched; a 1 stays 1). — direct.
3. Termination. There are ≤ log_2(P_0) moves with gcd>1 (each halves P at least) and ≤ 2026
   moves with gcd=1 (each drops A by 1, A≥0). Total moves finite. — well-founded descent on
   the pair (A, P). (KB: Invariants & monovariants.)
4. Non-collapse + at-most-one. g·ℓ = lcm(m,n) > 1 so the two outputs are never both 1: each
   move keeps ≥1 active entry, so A≥1 always. A move is legal iff A≥2, so terminal ⟹ A≤1.
   Hence terminal A = 1 exactly. ∎(a)

### Skeleton — part (b) (confluence / Newman)
5. Local confluence (diamond up to reconvergence). If from board B two different single
   moves lead to B1 and B2, there is a board B3 reachable from both B1 and B2. — by cases:
   (i) the two moves use disjoint position-pairs ⇒ they commute (apply the other move; both
   give the same B3 in one step, since they touch disjoint slots). (ii) the two moves share
   exactly one position (three slots i,j,k involved) ⇒ reduce to the finite 3-slot problem
   and show reconvergence (Gap 1). Moves sharing two positions are identical.
6. Termination + local confluence ⇒ confluence ⇒ unique normal form. — Newman's Lemma
   (a terminating, locally confluent abstract rewriting system has a unique normal form),
   proved by well-founded induction on the termination order from Step 3.
7. Part (b). The terminal board (unique normal form) is the same multiset regardless of
   choices; its single entry >1 is M. Hence M is independent of the choices. ∎(b)

### Key lemmas (claim + mechanism)
- Lemma P (monovariant): g·ℓ = lcm(m,n) = mn/gcd(m,n); so P non-increasing, halving when
  gcd>1; A drops when gcd=1. Gives termination and (via lcm>1) non-collapse.
- Lemma LC-disjoint: moves on disjoint slot-pairs commute — because each acts only on its
  two slots and leaves the others verbatim, so order does not matter.
- Lemma LC-overlap (the crux, Gap 1): two moves sharing one slot among three entries
  (x,y,z), one move on (x,y) the other on (x,z), reconverge. Mechanism to develop: the
  three-entry sub-board is itself a terminating system (Step 3 restricted to 3 slots) with a
  unique normal form on 3 entries, provable by strong induction on (A,P) restricted to the
  3 slots; both B1 and B2 continue to that shared 3-slot normal form. This is a genuinely
  self-contained finite sub-problem, NOT a re-use of the g_p invariant.

### Open gaps (builder fills)
- Gap 1 (local confluence, overlap case): rigorous proof that two overlapping single moves
  on three entries reconverge. Options: (a) prove the 3-entry board has a unique terminal by
  induction on its own (A,P) potential and note both B1,B2 lead there; (b) an explicit
  finite case analysis of (x,y,z) move interleavings. This is the load-bearing hard step and
  what makes this approach genuinely different (and riskier) than per-prime-gcd-invariant.
- Newman's Lemma statement + its well-founded-induction proof, or a citation-grade
  self-contained version, using the Step-3 termination order as the well-founded relation.

### Cases to cover
- Local confluence: disjoint pairs / share-one-slot / identical moves — all three.
- Termination buckets: gcd=1 moves vs gcd>1 moves.

### Watch out for
- Newman's Lemma needs LOCAL confluence AND termination; do not conflate local with global
  confluence (global is the conclusion, not a hypothesis). Proving global directly is
  circular with the goal.
- Beware accidentally re-deriving g_p to prove local confluence — that collapses this into
  the per-prime approach. Keep the overlap lemma self-contained on 3 entries.
- The "≤1 survivor" is definitional (legality needs two entries >1); do not over-argue it.
- Risk: if local-confluence proves intractable to write cleanly, this approach RETHINKs to a
  direct order-independence argument; flag early. (Global order-independence is numerically
  confirmed, so a valid proof exists; the question is whether the confluence write-up is
  clean.)
