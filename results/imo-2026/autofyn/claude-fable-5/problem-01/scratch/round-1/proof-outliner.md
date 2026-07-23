# Proof-outliner — round 1

## imo-2026-01

Field rationale: all three explorers converged on the same terrain (exponent map
(a,b) -> (min(a,b), |a-b|) per prime; exact invariant g_p = gcd of the valuation multiset; lex
monovariant for termination), verified algebraically and on 1500+ randomized trials. The clear
favorite is the direct invariant proof. To keep the field genuinely diverse rather than two
dressings of one idea, the second approach proves part (b) by a different engine entirely —
Newman's lemma on the rewriting system (uniqueness of normal form), never computing M — whose
crux (overlap joinability) is a wall the invariant route does not share. Two approaches, both
new; no dead ends to challenge (fresh workspace). No corpus crux transfers (all three explorers
searched; nearest matches aimo-0324 / aimo-0590 / aimo-0678 are style reminders only, not
borrowable — self-contained elementary derivation is the right call).

---

per-prime-gcd-invariant: new
File: results/imo-2026-01/approaches/per-prime-gcd-invariant.md
Target: Both parts: (a) after finitely many moves exactly one integer M > 1 remains; (b) M is
independent of choices — with the explicit value M = prod_p p^{g_p}, g_p = gcd_i v_p(a_i) over
the initial board.
Technique: Exact invariant + strict monovariant (knowledge_base.md "Invariants & monovariants",
Combinatorics; "Invariant / monovariant", General Proof Methods). Fully elementary v_p and gcd
identities.
Skeleton:
  1. A move sends the exponent pair at each prime p to (min(a,b), |a-b|) — by v_p(gcd) = min,
     v_p(lcm) = max (proved inline from prime factorization).
  2. Termination: (S, C) with S = sum_i Omega(a_i), C = #{entries > 1} strictly lex-decreases
     each move — Delta S = -Omega(gcd(m,n)); coprime moves output (1, mn) so C drops; C never
     increases — well-founded lex order on N x {0,...,2026}.
  3. Terminal boards have C <= 1 (a move needs two entries > 1; "continues while possible").
  4. g_p := gcd of the multiset {v_p(x) : x on board} is an EXACT invariant — because
     gcd(a,b) = gcd(min(a,b), |a-b|) (Euclidean subtraction) + gcd-associativity over untouched
     entries; induct on move count.
  5. Not all ones: any prime p | a_1 has g_p >= 1 initially (gcd of a multiset containing a
     positive value); an all-ones terminal board would force g_p = 0 — contradiction. With 3,
     exactly one entry M > 1: part (a).
  6. Terminal valuation multiset at p is {v_p(M), 0, ..., 0}, gcd v_p(M); invariance gives
     v_p(M) = g_p(initial) for all p, so M = prod_p p^{g_p(initial)} — choice-free: part (b).
Key lemmas (claim + mechanism):
  - L1: outputs' valuations are min(a,b), |a-b| — because v_p(gcd) = min, v_p(lcm) = max,
    max - min = |a-b|.
  - L2: (S, C) strictly lex-decreases — because Delta S = -Omega(gcd(m,n)) and the coprime case
    outputs an exact 1.
  - L3: g_p invariant — because gcd(a,b) = gcd(min(a,b), |a-b|) plus gcd-associativity.
  - L4: g_p >= 1 for any prime dividing any initial entry — gcd of a multiset with a positive
    member is positive.
Open gaps: full rigorous write-up of L1–L4 (incl. zero-valuation / all-zero-gcd conventions and
inline proofs of the "standard" facts), the induction over moves, and the C-never-increases case
check (incl. m = n giving outputs (m, 1)).
Cases to cover: gcd(m,n) = 1; gcd(m,n) > 1 with m != n; m = n. Exponent cases: a = b > 0,
a != b both positive, exactly one zero, both zero.
Watch out for: invariance may be per-prime but termination must be a single GLOBAL monovariant
(coupling pitfall — explorer-recorded); outputs of a move are NOT always coprime (4,6 -> 2,6);
"exactly one" requires the not-all-ones half; 2026 is a red herring.

---

newman-confluence: new
File: results/imo-2026-01/approaches/newman-confluence.md
Target: Both parts: (a) exactly one M > 1 remains after finitely many moves; (b) M independent of
choices — proved as uniqueness of the normal form of a terminating, locally confluent rewriting
system, with NO formula for M.
Technique: Abstract rewriting — termination monovariant + local confluence + Newman's lemma
(proved inline by well-founded induction; not in KB). Genuinely different route to (b): a
joinability argument, not a conserved quantity.
Skeleton:
  1. States = multisets of 2026 positive integers; step = the move; normal form = at most one
    entry > 1.
  2. Termination: (P, C), P = product of entries — P_new = P/gcd(m,n), coprime moves drop C —
    strict lex descent, well-founded.
  3. Local confluence: disjoint moves commute verbatim (diamond); overlapping moves (triple
    m, n, k sharing one position) need explicit joining sequences — THE crux gap. Candidate
    mechanism: prove 3-element boards have a unique terminal multiset by strong induction on
    their product, then run both branches to that terminal state.
  4. Newman's lemma: terminating + locally confluent => unique normal form (well-founded
    induction, written out).
  5. Not all ones: prime support never vanishes (exhaustive exponent-pair case check), so the
    unique normal form has exactly one entry M > 1: part (a).
  6. Unique normal form as a multiset => same M for all runs: part (b).
Key lemmas (claim + mechanism):
  - L1: (P, C) lex-decreases — pair-product mn falls to lcm(m,n) = mn/gcd(m,n).
  - L2: disjoint moves commute — each move reads/writes only its own two positions.
  - L3 (crux): overlap joinability — via unique-terminal-multiset for 3-boards by strong
    induction on the product; must be built at the INTEGER level (per-prime joining sequences
    don't compose: one schedule serves all primes).
  - L4: Newman — well-founded induction on the terminating relation.
  - L5: prime support persists — case check on (a,b): (a,a>0) -> min = a > 0; both positive
    distinct -> both outputs positive; one zero -> |a-b| > 0.
Open gaps: L3 is the load-bearing hard gap (no circularity: the 3-board statement gets its own
self-contained induction); Newman written with proof; L1/L2/L5 full case write-ups including
m = n and legality of deferred moves.
Cases to cover: disjoint vs overlapping vs identical move pairs; overlap sub-cases by
coprimality pattern; m = n; gcd = 1.
Watch out for: the per-prime coupling trap in L3; non-coprime outputs; Newman needs BOTH
hypotheses; confluence alone doesn't rule out the all-ones normal form (needs L5). If L3
resists, RETHINK this slug — the invariant approach does not share this wall.

---

Cheap kill considered and adopted: the entire favorite approach IS the cheap kill (one
elementary identity + one lex monovariant); no heavy machinery (LTE, Zsigmondy, CRT) was
rejected because none is remotely needed. Rejected framings recorded by explorers (do not
revive): P as an exact invariant (false — monovariant only); squarefree-part-of-P invariance
(false algebraically); M = squarefree kernel of P (refuted by board [9,16,25], M = 3600);
"outputs of a move are coprime" (false, 4,6 -> 2,6).

Recommendation to the outline-reviewer: per-prime-gcd-invariant is the favorite and should
anchor the build set; newman-confluence is the far-apart fallback worth one builder if capacity
allows (its L3 gap is real but the numerical local-confluence evidence is strong: 0 mismatches
over 200 branch tests on full terminal multisets).
