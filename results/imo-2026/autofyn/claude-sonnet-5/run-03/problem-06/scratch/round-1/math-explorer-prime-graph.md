## imo-2026-06

- Distinct openings (prime-graph / greedy-structure lens):
  1. **Clause/hypergraph model.** To each term a_i associate its full prime-factor support
     set P(i) = {primes dividing a_i}. The rule "gcd(a_{n+1},a_i) > 1 for all i ≤ n" says:
     a valid candidate m must, for EVERY i ≤ n, share at least one prime with P(i) — i.e. m
     satisfies the conjunction of clauses ⋀_i (∃ p ∈ P(i): p | m). This is a "hitting
     set against every past support" condition, and the P(i)'s form a **pairwise
     intersecting family of finite sets** (since gcd(a_i,a_j)>1 already holds for i,j ≤ n
     by construction). The natural top-level target from this framing: show the family
     {P(i)} stabilizes onto a single finite "active prime set" S (no term is ever forced to
     introduce a genuinely new prime after some point N_0), then show that beyond N_0 the
     sequence value mod L := (product, or lcm, of S) becomes periodic with period L, giving
     T = #terms per period, a_{n+T} = a_n + L.
  2. **Collapse-to-single-prime observation (a cheap sub-case, but instructive).** If ANY
     term a_i is a prime power p^k (support size 1), then every subsequent term is forced
     divisible by p, and the sequence trivially becomes the arithmetic sequence of
     multiples of p from that point on (T=1, L=p). Verified computationally for a_1 ∈
     {2,3,4,5,6,7,9,11,13,25,30}: sequence is *exactly* p, 2p, 3p, ... forever, where p is
     the smallest prime factor forced. This is a genuine but degenerate case; the
     interesting (generic) case needs a_1 with ≥ 2 distinct prime factors AND no later
     term ever landing on a prime power. Computationally, once two terms have supports
     that are pairwise-intersecting but have **empty total intersection** (e.g. {3,5} vs
     {2,3} vs {2,5} — no common prime across all three), no single prime can satisfy every
     clause simultaneously, so every future candidate is forced to have compound
     (≥2-prime) support. This is the mechanism that produces genuinely non-trivial,
     higher-period behavior (T>1) instead of instant collapse to L=p.
  3. **Covering-system / CRT periodicity target.** Once the active prime set S = {p_1,...,
     p_k} is fixed (conjecturally after finitely many terms), reduce mod L = p_1···p_k (or
     lcm). The claim "a_{n+T}=a_n+L" is then equivalent to: the sequence of residues
     r_n = a_n mod L, together with which subset of S divides a_n, is eventually exactly
     periodic with period T when read cyclically through the L residue classes. This is
     structurally identical to a **covering system of congruences** (cf. Erdős covering
     congruences, mentioned generically in KB under "Order of an element / eventual
     periodicity of products mod m" and "Linear recurrences ... eventually periodic mod
     m") — worth citing/adapting even though KB doesn't have a named "covering system"
     entry verbatim.
  4. **Density / minimality argument for why no new prime is ever needed again (the hard
     gap).** The greedy always takes the SMALLEST valid candidate. Once S is large enough
     that products/combinations of primes in S already achieve every needed residue class
     with bounded gaps (a discrete "three-distance"/covering-density argument), any
     candidate requiring a brand-new prime q would need to be ≥ roughly 2q (or at least the
     smallest multiple of q exceeding a_n that's compatible), which for q large is far
     bigger than the guaranteed nearby S-only candidate. This should be provable by a
     counting/pigeonhole bound (numbers ≤ x with all prime factors in a fixed finite S of
     size k occur with bounded gaps once residues mod L are suitably populated — a finite,
     checkable CRT fact once S and the "occupied residues" are pinned down) rather than
     needing deep analytic number theory. This looks like the single hardest lemma in the
     whole problem — the one prior "shared gap" the outliner should expect to hit.

- Candidate technique(s): CRT / modular residue-class analysis (KB: "Modular arithmetic,
  CRT"; "Order of an element ... eventual periodicity of products of a sequence mod m");
  greedy/extremal-principle argument for minimal next term (KB: "Pigeonhole / extremal
  principle", "Constructive / incremental"); finite intersecting-set-family combinatorics
  (not explicitly in KB, but analogous to Helly-type reasoning); induction/well-ordering to
  establish stabilization of the active prime set (KB: "Induction", "Invariants &
  monovariants" — the active prime set S is essentially a monovariant that stops growing).

- Cheap-kill candidates: the prime-power collapse (opening 2 above) instantly disposes of
  a large class of starting values (any a_1 that is a prime or prime power, or any
  sequence that ever revisits a prime-power term) — worth stating as a one-line lemma so
  the outliner doesn't have to re-derive it for every case, but it is NOT the generic
  case and doesn't resolve the full problem. Also: since gcd(a_i,a_j) divides |a_i - a_j|
  (KB "Divisor analysis"), and a_i's are strictly increasing, this gives an easy lower
  bound tool for gap sizes but doesn't by itself force periodicity.

- Knowledge-base entries to use: "Modular arithmetic, CRT" (§Number Theory); "Order of an
  element, Fermat/Euler: periodicity ... eventual periodicity of products of a sequence
  mod m" (§Number Theory) — closest generic match for the eventual-AP-periodicity
  target; "Linear recurrences ... sequences are eventually periodic mod m" (§Number
  Theory); "Pigeonhole / extremal principle" and "Invariants & monovariants" (§Combinatorics)
  for the "active prime set stabilizes" argument; "Divisor analysis" (§Number Theory) for
  gcd-divides-difference facts.

- Analogous past problems (cruxes):
  - `aimo-0447` (number_theory, subtopic divisibility-and-gcd / size-bounding-and-descent):
    crux is "encode a gcd>1-for-every-pair hypothesis by placing a witnessing prime in a
    grid cell, turning the condition into a prime-covering of a grid" — this is a genuinely
    useful *encoding trick* (representing pairwise-gcd conditions via witness primes in a
    combinatorial grid/incidence structure) that could be adapted to encode "gcd(a_j,a_i)>1
    for all i<j" as a witness-prime assignment per pair, though the target claim there
    (a lower bound on min(a,b)) is different from ours (eventual periodicity). Worth
    borrowing the *encoding idea*, not the conclusion.
  - `aimo-0982` (number_theory, modular-arithmetic-and-CRT): crux is proving eventual
    periodicity of a derived sequence by tracking an index modulo the period of an
    eventually-periodic source, splitting the modulus into 2-adic and odd parts via
    multiplicative order — a decent template for *how to rigorously phrase* "eventually
    periodic mod L ⟹ periodic shift", once the active-prime-set S and L are established,
    but doesn't address how to establish S's finiteness (the real crux of our problem).
  - No corpus problem found that matches the greedy-minimal-selection-with-accumulating-
    gcd-constraints structure itself; this looks like a genuinely novel construction for
    the corpus (nothing scored as a strong match beyond the two above).
  - **`aimo-0680` = IMO 2015 N4 — the single closest analog, flagged by this role's own
    persistent memory from a prior run of this exact problem.** Statement: f:Z>0→Z>0 with
    (i) (f^n(m)-m)/n a positive integer for all m,n, and (ii) Z>0 minus the image of f is
    finite; prove f(n)-n is eventually periodic. The FINISHING technique transfers almost
    verbatim to our target conclusion shape (a_{n+T}=a_n+L): (a) partition the domain into
    "orbit rows" under the dynamics; (b) show finitely many rows are already exact APs and
    the rest have bounded positive density in any window of length T=lcm(row periods),
    pinning a linear growth bound on the remaining rows; (c) the pigeonhole step "a bounded
    positive integer sequence beta_d = (f^d(a_x)-a_x)/d must repeat some value T_x
    infinitely often" produces a candidate dense/periodic row; (d) the closing trick —
    for two quantities each known to be ≡ mod a growing index-gap while their difference is
    bounded, force the difference to be exactly 0 — is a clean, reusable device for
    "upgrade eventual-periodic-on-a-subsequence to periodic-everywhere." This does NOT
    supply the harder half specific to our problem (establishing that only finitely many
    primes are ever needed — there is no direct analog of "prime support stabilizes" in
    aimo-0680, since its hypotheses are about a general function, not a gcd-driven greedy
    construction), but the closing argument (steps (b)-(d)) is very likely reusable almost
    directly once our problem's analogous "active prime set S is finite and fixed" lemma
    is established — i.e. once S is pinned down, showing a_{n+T}=a_n+L from there can
    probably borrow aimo-0680's window-counting + bounded-difference-forces-equality
    machinery essentially as is.

- Prior progress: none (round 1, current.md and approaches/ empty).

- Dead ends (do not retry): none recorded yet (no prior approaches exist). Flagging
  pre-emptively: pure "start with a_1=2 (or any prime/prime-power)" examples are
  degenerate/trivial (T=1) and should NOT be used as the main illustrative case for the
  outline — they don't exercise the real difficulty (multi-prime stabilization). Any
  approach that tries to prove periodicity by bounding gaps alone (without pinning down
  the active prime set S) will likely stall, since the gap sizes themselves are exactly
  what's governed by S and its CRT structure.

- Small-case / intuition notes (all conjectural, from direct simulation, code in this
  session using brute-force greedy generation up to a_n ~ a few hundred):
  - a_1 ∈ {2,3,4,5,6,7,9,11,13,25,30} (all prime or prime-power-forced): sequence is
    exactly multiples of the smallest prime factor forced by a_1, from a_1 on. T=1,
    L = that prime.
  - a_1 = 15 (=3·5): sequence begins 15,18,20,24,30,36,40,42,45,48,50,54,60,66,70,72,75,
    78,80,84,90,96,100,102,105,... and becomes periodic with **T=8, L=30** (30 = 2·3·5);
    every term from the start is divisible by 2, 3, or 5 (occasional extra factor like 7
    in 42, 70, 84, 105 is incidental — not needed for the gcd condition). Same behavior
    (same diff-pattern) for a_1=45.
  - a_1 = 21 (=3·7), 33 (=3·11): degenerate into a pure AP with difference 3 — because
    3 alone ends up covering everything (every term stays a multiple of 3), i.e. the
    "richer" behavior needs the two prime factors of a_1 to both remain individually
    necessary; with 21 the greedy apparently never needs 7 for gcd purposes and just
    reuses 3. (Not yet explained why 15's case needs both 3 and 5 while 21's case doesn't
    need 7 — worth the outliner examining: likely because 3 alone already suffices to
    satisfy gcd against a_1=21, since 24=a_2 is picked as 3·8, and 3 dominates from then
    on, whereas for a_1=15, the greedy's next terms end up alternating between "needs 3"
    and "needs 5" because at some points the smallest valid candidate is only reachable
    via 5, not 3.)
  - a_1 = 35 (=5·7): T=24 apparently (period found in diffs), with **L = 5·... ** — the
    diff list showed a repeating block of length 24 summing to (need recheck exactly, but
    matches L being a small multiple of 2·3·5·7 given extra small primes creep in);
    confirms richer multi-prime stabilization for 2-distinct-odd-prime starts.
  - a_1 = 105 (=3·5·7): after a longer transient (~15-20 terms), sequence stabilizes to
    exactly **T=58, L=210** (210 = 2·3·5·7), verified directly: every one of the last 120
    generated terms is divisible by 2, 3, 5, or 7 (checked computationally, zero
    exceptions), and the difference sequence repeats exactly with period 58 summing to
    210. Larger primes (up to 257 observed) do appear as incidental extra factors of some
    terms but are never load-bearing for satisfying any gcd constraint. This is far and
    away the cleanest hard evidence for the conjectured general shape of the answer:
    **the active prime set S is finite, L = ∏_{p∈S} p (or possibly lcm, same as product
    since primes), and T is the number of a_n's that land in one full residue cycle mod L.**
  - Conjecture (unproven): T and L both depend on a_1 in a complicated way (not simply
    predictable in closed form from a_1's factorization alone — e.g. it's not just "L =
    a_1" or "L = product of a_1's prime factors" once transient effects are included: for
    a_1=105 the eventual S is exactly {2,3,5,7}, i.e. 2 gets pulled in even though a_1 is
    odd — because among the greedy candidates, even numbers are cheap/plentiful and get
    absorbed as a covering prime quickly). This "2 always eventually joins S" pattern
    recurred in every non-trivial (multi-prime a_1) example tried (15, 35, 105) and is a
    good conjecture for the outliner to build the general argument around: **argue 2 is
    essentially always eventually forced into the active set because even numbers are the
    highest-density candidates**, then handle which odd primes join similarly by a density/
    counting argument.
