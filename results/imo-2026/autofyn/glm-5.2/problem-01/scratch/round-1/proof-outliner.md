# imo-2026-01 — proof-outliner field (round 1)

Problem: 2026 integers >1 on a blackboard; a move picks two integers m,n>1 in
different positions and replaces them by gcd(m,n) and lcm(m,n)/gcd(m,n);
continue while possible. (a) Prove termination after finitely many moves with
exactly one integer M>1 left. (b) Prove M is independent of choices.

Round 1, no prior approaches. Three explorers converged on a clean core
(per-prime invariant D_p = gcd of all positionwise p-valuations). I field
**three** genuinely different framings varying along the two axes the dispatch
named (termination potential; part-(b) route). All three are `new` (nothing to
advance yet). All verified numerically (10 boards, 10 move orders each, 0
failures; M = ∏_p p^{D_p} confirmed).

The move, in the rewrite form used by every approach: let g = gcd(m,n),
m = gx, n = gy with gcd(x,y) = 1. The two replacements are g and xy. Note
xy = lcm(m,n)/gcd(m,n) and gcd(g, xy) = 1. In p-adic valuations the pair
(α,β) = (v_p(m), v_p(n)) is sent to (min(α,β), |α−β|) — one subtractive-
Euclidean step (standard: v_p(gcd)=min, v_p(lcm/gcd)=max−min=|α−β|).

---

## per-prime-euclidean-invariant  (new)  — PRIMARY, nominate to advance

Target: Both (a) and (b). Whole problem end to end.
Technique: Per-prime valuation decomposition + Euclidean-gcd identity
(invariant/monovariant). The move is literally a parallel subtractive-Euclid
step on each prime's valuation vector; the gcd of each coordinate's entries is
invariant, and that invariant pins the unique survivor.

Skeleton:
  1. Set up p-adic valuation bookkeeping. For each prime p and board position i
     let a_i^{(p)} = v_p(value_i). Lemma L1: under a move on positions i,j,
     (a_i^{(p)}, a_j^{(p)}) -> (min(a_i,a_j), |a_i − a_j|). — by v_p(gcd)=min,
     v_p(lcm/gcd)=|α−β| (KB "Divisor analysis: gcd structure").
  2. Define D_p := gcd of all a_i^{(p)} across positions, with gcd(x,0)=x (so
     positions where p does not divide the value are invisible). Lemma L2:
     D_p is invariant under a move. — because
     gcd(min(α,β), |α−β|) = gcd(α,β) (the Euclidean identity), and the gcd of
     a list is unchanged when one replaces two entries α,β by two entries whose
     gcd equals gcd(α,β).
  3. Termination via lexicographic potential (W, c): W = ∑_i Ω(value_i) =
     ∑_p ∑_i a_i^{(p)} (total prime-factor count, a nonneg integer); c =
     #{i : value_i > 1}. Lemma L3: every move strictly decreases (W,c) in
     lex order. Case analysis on the chosen pair (m,n):
       (i) gcd(m,n) > 1 and m ≠ n: W drops by Ω(gcd(m,n)) ≥ 1 (because
           gcd(m,n) divides the pair-product mn but the new pair-product is
           mn/gcd(m,n), and g,xy together carry Ω(g) fewer prime factors —
           equivalently min(α,β)+|α−β| = max(α,β) ≤ α+β with strict drop when
           min(α,β)≥1 for some p); c unchanged.
       (ii) gcd(m,n) = 1 (forcing m ≠ n): W unchanged, c drops by 1 (new pair
           (1, mn)).
       (iii) m = n: new pair (m, 1); W drops by Ω(m), c drops by 1. (Edge case;
            must be explicit since gcd>1 but c still drops.)
     (W,c) ∈ ℕ² with lex order; well-founded (W can drop only finitely often,
     bounded below by 0; between W-drops, c bounded below by 0 and drops by 1).
     => finitely many moves.
  4. "Exactly one >1" — two halves. Termination gives c ≤ 1 at the end.
     Lemma L4: c ≥ 1 always. Since initially all 2026 numbers are >1, some
     prime p divides some value, so D_p ≥ 1 for that p; D_p is invariant (L2),
     so D_p ≥ 1 forever, forcing at least one value to carry p, i.e. c ≥ 1
     forever. Together c = 1. — by invariant L2 + nonempty initial prime
     support.
  5. Part (b): at the terminal board the sole >1 entry is M (rest are 1). For
     each prime p the valuation multiset is {v_p(M), 0, …, 0}, whose gcd is
     v_p(M) (gcd(x,0)=x). By invariance (L2) this equals D_p, so
     v_p(M) = D_p for every p. Hence M = ∏_p p^{D_p}, a function of the
     INITIAL board only. — by L2 + terminal shape.
  6. Conclude: M is determined by the initial board (the formula above), hence
     independent of the move order. QED both parts.

Key lemmas (claim + one-line mechanism):
  - L1 (move = (min,|α−β|) on valuations) — because v_p(gcd)=min(α,β) and
    v_p(lcm/gcd)=max(α,β)−min(α,β)=|α−β|.
  - L2 (D_p invariant) — because gcd(min(α,β),|α−β|)=gcd(α,β) is the Euclidean
    identity; replacing two list entries by two with the same gcd preserves the
    list-gcd.
  - L3 ((W,c) lex strictly decreases) — case split (i)/(ii)/(iii); W is
    additive over primes so the prime-coupling is handled automatically.
  - L4 (c ≥ 1 forever) — D_p ≥ 1 for some p is invariant, forbidding all-ones.
  - L5 (terminal M = ∏ p^{D_p}) — terminal valuation multiset {v_p(M),0,…,0}
    has gcd v_p(M), equated to D_p by invariance.

Open gaps (builder fills):
  - Rigorous proof of the Euclidean identity gcd(min(α,β),|α−β|)=gcd(α,β) from
    scratch (one line via gcd(α,β)=gcd(α−β,β), but must be spelled out).
  - The W-drop sign in case (i) for ALL primes simultaneously: need
    min(α,β)+|α−β| = max(α,β) < α+β whenever min(α,β)≥1; summed over p this is
    the Ω(gcd) drop. Make the sum-over-primes step explicit.
  - Well-foundedness of lex ℕ² stated, not hand-waved (one sentence: W bounded
    below by 0, drops by ≥1 finitely often; c bounded below by 0).
  - Edge case m=n written out (gcd>1 but c drops; must not be absorbed into
    case (i)).

Cases to cover: the three pair-cases (i) gcd>1 & m≠n, (ii) gcd=1, (iii) m=n.
Watch out for:
  - Forgetting case (iii) m=n (gcd>1 so it does NOT fall under case (ii), yet c
    drops — easy to miscount).
  - Defining D_p = gcd of the NONZERO valuations vs gcd-with-zeros: must state
    gcd(x,0)=x so the two are equivalent; {6,10} shows D_3 = gcd(1,0)=1 (giving
    M=30), NOT min=0 (which would wrongly give M=2).
  - "Exactly one >1" needs BOTH halves (termination → c≤1 AND D_p≥1 → c≥1);
    either alone is partial.

---

## integer-termination-invariant-pin  (new)  — rival, nominate to advance

Target: Both (a) and (b). Whole problem.
Technique: Valuation-FREE termination (integer product potential) for part (a);
per-prime invariant D_p for part (b) only. The (a) half never invokes prime
factorization — a genuinely different termination potential from approach 1.

Skeleton:
  1. Rewrite the move as (gx, gy) -> (g, xy), g = gcd(m,n), gcd(x,y)=1.
     Lemma M1: the product P of all board entries is non-increasing, and
     strictly decreases (by an integer factor gcd(m,n) ≥ 2) whenever the chosen
     pair is non-coprime (gcd>1). — because the pair-product mn = g²xy becomes
     g·xy = mn/g, so P_new = P_old / g.
  2. Lemma M2: the count c = #{value > 1} never increases; it drops by 1 on a
     coprime pair (gcd=1, new pair (1, mn)) or on an equal pair (m=m, new pair
     (m,1)); it is unchanged only when gcd>1 and m≠n (new pair (g, xy), both
     >1 since g≥2 and xy≥1 with xy=1 iff x=y=1 iff m=n). Case split.
  3. Termination via lex (P, c), P primary, c secondary. Suppose infinitely
     many moves. Since P is a positive integer non-increasing, P stabilizes
     after finitely many moves; thereafter every move must have gcd(m,n)=1 (else
     P strictly drops), so by M2 every subsequent move drops c by 1. But c is a
     nonneg integer, so it reaches 0 in finitely many steps — after which no
     move is possible (need two values >1). Contradiction. => finite
     termination. (This is well-foundedness of lex (P,c) without naming
     factorizations.)
  4. "Exactly one >1" via the radical-support invariant (valuation-free).
     Lemma M3: the set S of prime divisors of the total product P is invariant.
     — because primes(mn) = primes(m)∪primes(n) = primes(g)∪primes(xy)
     (since g·xy = lcm(m,n) has the same prime support as mn). S is nonempty
     initially (all 2026 entries >1), so P > 1 forever. At termination c ≤ 1;
     P > 1 forces c = 1 (a single entry carries all of P). No valuations used
     in part (a).
  5. Part (b): now invoke valuations ONLY here. Define D_p = gcd of all
     positionwise v_p(a_i) (gcd(x,0)=x). Lemma M4 (invariance): D_p preserved
     by the move — same Euclidean identity
     gcd(min(α,β),|α−β|)=gcd(α,β) as approach 1's L2. At the terminal board
     (one M>1, rest 1) the valuation list is {v_p(M),0,…,0}, gcd = v_p(M); so
     v_p(M) = D_p and M = ∏_p p^{D_p}, a function of the initial board only.
     => independent of choices.

Key lemmas:
  - M1 (P non-increasing, strict drop by factor g≥2 on non-coprime moves) —
    because pair-product mn -> g·xy = mn/g.
  - M2 (c non-increasing; case split) — coprime pair -> (1,mn); equal pair ->
    (m,1); otherwise both outputs >1.
  - M3 (radical support invariant) — primes(g·xy)=primes(g)∪primes(xy)=
    primes(gx)∪primes(gy)=primes(mn).
  - M4 (D_p invariant + terminal pin) — Euclidean identity, same as L2/L5.

Open gaps (builder fills):
  - M2 case split fully written (especially the "xy=1 iff m=n" equivalence).
  - The infinite-run contradiction made explicit (P stabilizes => all moves
    coprime => c strictly drops => contradiction).
  - M3 prime-support equality spelled out (lcm has the same prime support as
    the product).
  - M4 = imports L2/L5 from approach 1; if approach 1's proof is certified
    first, this becomes a free import. Otherwise self-contained here.

Cases to cover: coprime pair / equal pair / non-coprime distinct pair (for M2).
Watch out for:
  - The "xy=1 iff m=n" step is the crux of M2; getting it wrong breaks the
    count.
  - Approach 1 and this approach SHARE the part-(b) invariant M4 — if that
    invariant is flawed both die together. This is the shared-gap risk; the
    confluence approach (below) is the hedge.

---

## confluence-unique-normal-form  (new)  — secondary rival, higher risk

Target: Both (a) and (b). Whole problem.
Technique: Abstract rewriting / Newman's lemma. Termination (from the integer
potential (P,c) of approach 2's steps 1–4) + local confluence => global
confluence => unique normal form => M independent of choices. This is a
genuinely different PROOF STRUCTURE for part (b): instead of exhibiting an
invariant pinning M, it shows any two complete play sequences reach the same
terminal element. The explorers flagged it as harder/messier; field it as a
secondary rival so the field is not monocultural on the part-(b) mechanism
(the shared invariant M4 is the single point of failure for approaches 1 & 2).

Skeleton:
  1. Termination + exactly-one: reuse the valuation-free (P,c) lex potential
     and radical-support invariant (approach 2, steps 1–4). Every terminal
     state has exactly one entry >1.
  2. Local confluence (the HARD step). The rewrite system is terminating. By
     Newman's lemma (terminating + locally confluent => confluent), it suffices
     to check local confluence: for any state and any two one-move reductions,
     the two resulting states have a common reduct after further moves.
  3. Reduce local confluence to critical pairs. Disjoint redexes (two moves
     on four distinct positions) trivially commute. The only non-trivial
     critical pair is two moves sharing exactly one position: a triple
     (a, b, c) at positions i,j,k. Let S1 = state after move(i,j) and
     S2 = state after move(i,k). Lemma C1 (triple joinability): S1 and S2
     have a common reduct. — this is the load-bearing crux.
  4. Prove C1. Write a = gx, b = gy, c = gz (g = gcd(a,b); but the shared
     position a participates in two different gcds). Work in p-adic valuations:
     the triple of exponents (α,β,γ) undergoes two Euclidean steps
     (min(α,β),|α−β|,γ) vs (min(α,γ),β,|α−γ|). Lemma C2: these two triples
     have a common reduct under the parallel Euclidean step. — by a finite
     case analysis on the order of α,β,γ (six orderings); in each, both
     reduce to the sorted triple's Euclidean normal form
     (gcd(α,β,γ), 0, 0). The gcd-of-three is preserved by each step (same
     Euclidean identity), and the subtractive-Euclidean algorithm on three
     numbers terminates at (gcd, 0, 0) regardless of step order.
  5. Lift C1 (per-prime) to C1 (integer board). The board move applies the same
     position-pair to ALL primes simultaneously. Since per-prime the triple
     always rejoins, and the rejoinder moves on the triple positions are the
     SAME positions across primes, one sequence of board moves realizes the
     common reduct for all primes at once. (This lift is subtle — see gaps.)
  6. Conclude: terminating + locally confluent => confluent (Newman) => unique
     normal form. Since every normal form has exactly one entry >1 (step 1),
     that unique entry is M, independent of choices. (Part (b).) Part (a) is
     step 1.

Key lemmas:
  - C1 (triple critical-pair joinability) — per-prime, by case analysis on the
    six orderings of (α,β,γ); both divergent Euclidean steps reach the common
    normal form (gcd(α,β,γ),0,0).
  - C2 (per-prime => board lift) — the rejoinder moves are on the same three
    positions for every prime, so a single board-move sequence realizes the
    common reduct for all primes.
  - Newman's lemma (standard abstract-rewriting theorem; not in KB — cite as
    standard, state precisely).

Open gaps (builder fills — these are the real cruxes):
  - C1's six-case verification must be written out explicitly; this is the
    make-or-break step. (If any case fails to rejoin, the whole approach dies.)
  - C2 (per-prime-to-board lift): show the per-prime rejoinder moves can be
    scheduled so that they are valid board moves simultaneously for all primes.
    This is non-trivial because a board move on positions (i,j) changes the
    valuations for EVERY prime at those positions; one must check the per-prime
    reduct schedules are COMPATIBLE. If this lift fails, the confluence
    argument does NOT lift from per-prime to the board, and the approach is
    dead. FLAGGED as the most likely failure point.
  - State Newman's lemma correctly (termination + local confluence, not global).

Cases to cover: six orderings of (α,β,γ) in C1.
Watch out for:
  - C2 lift is the hidden trap: per-prime confluence does not automatically
    imply board confluence under a shared position-pair. The builder must
    either justify the lift or find an integer-level (valuation-free) proof of
    C1. If neither works, route back to outliner.
  - Do NOT use the uniqueness of M (the very thing being proved) inside the
    confluence proof — that would be circular (explorers' warning).
  - The staged "Euclidean-then-merge" framing is a DEAD END (do not use):
    non-coprime states persist mid-process for arbitrary move orders
    (verified on {4,8,3}); there is no clean two-phase split.

---

## Field summary

Three new approaches, genuinely different in framing:

1. **per-prime-euclidean-invariant** — valuation route for BOTH halves;
   (W,c) termination + D_p invariant. Cleanest, intended solution. Nominate
   to advance (likely solves in one build).
2. **integer-termination-invariant-pin** — valuation-FREE (a) via (P,c) +
   radical support; (b) via D_p. Differs from 1 in the (a) potential (integer
   vs valuation-sum). Nominate to advance.
3. **confluence-unique-normal-form** — (a) via (P,c); (b) via Newman's lemma
   (terminating + local confluence => unique normal form). Genuinely different
   part-(b) structure (no invariant pinning M). Higher risk: crux is C1 triple
   joinability + the per-prime-to-board lift C2. Field as secondary rival so
   the field is not monocultural on the D_p invariant (which is the single
   shared point of failure for approaches 1 & 2).

Diversity check: approaches 1 & 2 share part (b) (the D_p invariant M4) but
diversify part (a) (W-sum vs P-product). Approach 3 diversifies part (b)
(confluence vs invariant). The field thus hedges both axes. If the D_p
invariant turns out flawed, approach 3 survives; if the (P,c) termination has
a flaw, approach 1's (W,c) survives.

No copy/branch recommended this round: no live approach yet has two viable
paths for the SAME gap (round 1, all new). Re-evaluate next round once builders
report which gaps closed vs dead-ended.

Dead framing to avoid (recorded): the staged "Euclidean-phase then
coprime-merge-phase" split — non-coprime states persist mid-process for
arbitrary move orders; do not propose.

Build set (all three, one builder each): `per-prime-euclidean-invariant`,
`integer-termination-invariant-pin`, `confluence-unique-normal-form`.
