## imo-2026-06

p-position-small-prime-classification: new
Target: Prove that for the given greedy sequence there are positive integers T and L such that a_{n+T}=a_n+L for every n>=1.
Technique: Impartial-game P-position recursion plus minimal-counterexample descent and prime-factor stripping; adapt the exact crux moves of aimo-0030, then use modular arithmetic/CRT and periodic enumeration.
Skeleton:
  1. Fix A=a_1 and define a decreasing impartial game on integers m>=A, in which a move m->x is allowed when A<=x<m and gcd(m,x)=1; call m good when it is a P-position (the next player loses) — by well-founded recursion on m.
  2. Show that m is good exactly when it is noncoprime to every smaller good integer, and hence that the given sequence is precisely the increasing enumeration of all good integers — by the standard P/N-position recursion and induction on the enumeration index.
  3. Show any two good integers are noncoprime, and in particular every good integer has a prime divisor in common with A — by applying the characterization in Step 2 to the larger member of the pair.
  4. Prove the prime-stripping lemma: if b>=A has a prime divisor <=A, there is x with A<=x<=b, having exactly the same prime divisors <=A as b and no prime divisor >A — take the product s of the distinct small prime divisors and, when b has a large prime q>A, multiply s by the least power of one chosen small prime p that reaches A; minimality gives x<pA<sq<=b. If b has only small prime factors, take x=b.
  5. Prove the strengthened small-witness theorem: every two good integers have a common prime divisor <=A — if not, choose a violating good pair b<b' with b' minimal; replace b by the stripped x<=b, which is coprime to b', so x is bad; a legal move from x reaches a smaller good b*, and then (b*,b) is a violating good pair with larger member <b', a contradiction.
  6. Prove signature invariance: two integers u,v>=A divisible by exactly the same primes <=A are either both good or both bad — if, say, u is bad and v good, the P/N recursion supplies a smaller good w coprime to u; Step 5 gives a small common prime of v and w, which the shared signature forces to divide u, contradiction (and interchange u,v for the other orientation).
  7. Put L equal to the product of all primes p<=A. Since m and m+L have the same small-prime signature, Step 6 makes the indicator of goodness L-periodic on [A,infinity) — by modular arithmetic.
  8. Let T be the number of good integers in any interval [r,r+L) with r>=A. It is positive (A and A+L are both good), independent of r by Step 7, and translation by L order-preservingly bijects the good integers in one residue cycle to the next; therefore their increasing enumeration satisfies a_{n+T}=a_n+L for every n.
Key lemmas (claim + the one-line mechanism that makes it true):
  - P-position characterization — a position is losing exactly when every legal move leads to a winning position, so good m means no smaller good integer is coprime to m.
  - Prime-stripping lemma — the least-power construction from aimo-0030 preserves the <=A prime signature, while x<pA<sq<=b removes every large prime without crossing above b.
  - Small-witness theorem — minimality of the larger violating good number, followed by stripping and one P/N move, manufactures a strictly smaller violating pair.
  - Signature invariance — a bad representative has a coprime move to a good number, while the small-witness theorem makes that impossible for a good representative with the same signature.
  - Periodic-enumeration lemma — an increasing periodic subset of the integers shifts by its modulus after exactly the number of occupied residues in one period.
Open gaps: The builder must write the P/N recursion carefully, verify every inequality and edge case in the prime-stripping lemma (especially the no-large-prime case), and formalize the two orientations in signature invariance and the index count in Step 8. The strategic route itself has no conjectural <=A witness-prime assumption: Step 5 proves the needed bound.
Cases to cover: b has no prime >A versus b has one; the exponent in the least-power construction is 0 versus positive; either member of a similar pair is the bad one.
Watch out for: “Good” is a game-theoretic auxiliary notion and must be proved to enumerate exactly the original sequence. Do not replace Step 5 by the false assertion that every term shares one fixed prime. This approach borrows the crux of aimo-0030 but must prove it here from scratch.

cnf-minimal-transversals: new
Target: Prove the periodic-translation claim end to end by showing the greedy monotone divisibility formula has a finite basis and then enumerating its periodic models.
Technique: Boolean-CNF dualization, divisibility-minimal squarefree transversals, and an essential-prime elimination descent; modular arithmetic/CRT is the endgame.
Skeleton:
  1. For each selected term set P_i={p:p|a_i} and encode stage-n admissibility as F_n=AND_{i<=n}(OR_{p in P_i}[p|x]); represent its models as a union of multiples of the divisibility-minimal squarefree hitting products D_n.
  2. Verify the exact update D_{n+1}=min_div({lcm(d,p):d in D_n, p|a_{n+1}}), and verify a_{n+1}=min_{d in D_n} d(floor(a_n/d)+1) — by distributing the new clause and deleting divisibility-dominated products.
  3. Establish the unconditional syndetic bound a_{n+1}-a_n<=rad(A): a_n+rad(A) has the same residues modulo every prime of A, and for each earlier a_i one may choose a common prime of a_i and A.
  4. Prove an essential-prime elimination lemma without positing a prime bound: if q>A occurs in a minimal hitting product d in D_n, use the private-witness clause for q (minimality supplies a row hit by q and by no other prime of d), strip that row to a canonical integer with the same <=A signature as in the least-power move of aimo-0030, and combine the greedy minimality plus the bounded interval (a_k,a_k+rad(A)] to replace q by a smaller divisor or delete d. Iterate descent until every minimal hitting product is supported on primes <=A.
  5. Conclude that every D_n lies in the finite Boolean lattice of squarefree products of primes <=A; since each new clause can only shrink the model set, the represented state stabilizes after finitely many strict changes — by finiteness and the monovariant “number of surviving residue signatures.”
  6. Let D be the stabilized antichain and M=lcm(D). Prove the selected sequence is the increasing enumeration of U=union_{d in D} dN above A: any skipped integer failed an already-present clause and can never become admissible later, while every selected integer is in U after stabilization; separately account for the finite prefix and show stabilization actually identifies the global model set relevant to all indices.
  7. Count the occupied residues of U modulo M to obtain T and use translation by M to conclude a_{n+T}=a_n+M; if Step 6 yields only tail translation, absorb the finite prefix only after proving the formula from n=1 (or enlarge/adjust the state so all clauses are included).
Key lemmas (claim + the one-line mechanism that makes it true):
  - Antichain update identity — distributivity turns “old hitting product AND one prime from the new row” into lcm(d,p), and divisibility removes redundant products.
  - Private-witness property — every factor in a minimal transversal has a clause not hit by the other factors, otherwise that factor can be deleted.
  - Essential-prime elimination — a private large prime must be replaceable using a stripped <=A signature and the least-choice interval; this is the load-bearing descent, not an assumed <=A witness bound.
  - Finite stabilization — after elimination there are only finitely many squarefree products over the finite prime set {p<=A}.
  - No-resurrection of skipped integers — clauses only accumulate, so failure at the time an integer is passed is permanent.
Open gaps: Step 4 is a major unproved lemma: the builder must connect the private-witness row and prime stripping to an actual smaller admissible competitor or a dominated transversal; bounded gaps alone do not make that connection. Step 6 must prove global, not merely eventual, translation. This approach is valuable only if Step 4 is genuinely advanced rather than replaced by the conjectural assertion that essential primes are <=A.
Cases to cover: q's private row may contain several <=A primes; replacement may merge with an existing factor; D may contain a singleton; pre-stabilization terms versus stabilized tail.
Watch out for: Per-stage periodicity and monotone clauses do not imply stabilization. The gap bound is pruning only. Do not invoke Noetherianity over infinitely many prime variables without proving finite support.

finite-window-forgetting: new
Target: Prove the periodic-translation claim by showing the least-choice process has bounded memory and hence a finite residue-state automaton.
Technique: Syndeticity plus a temporal “old constraints become redundant” lemma, followed by finite deterministic state recurrence; adapt the confinement-before-periodicity move of aimo-0577 and aimo-0678.
Skeleton:
  1. Put R=rad(A) and prove 1<=a_{n+1}-a_n<=R by testing a_n+R against every prior term using a prime common to that term and A.
  2. Partition every interval of length R into candidate offsets and attach to each rejected offset the earliest prior term coprime to it; formulate a bounded-memory lemma asserting that there is W=W(A) such that, for every n, satisfying the last W selected constraints already implies satisfying all earlier constraints.
  3. Attack the bounded-memory lemma by an extremal witness-chain argument: if an old constraint is still essential, choose the least candidate in the current R-window witnessed only by that old term; following the terms that rejected successive smaller offsets should create a strictly descending chain of <=A prime signatures or a repeated signature that makes the old witness redundant.
  4. Once W exists, encode a state by the W recent values modulo a fixed modulus M formed from the finitely many essential witness signatures furnished by Step 3, together with their order inside the current R-window; prove this finite state determines the next gap and successor state.
  5. A repeated state gives a periodic gap word. Use determinism backward along the actually reached cycle, or prove the initial state already lies on the cycle, to obtain a period from n=1 rather than only eventual periodicity; sum one period of gaps to obtain L and conclude a_{n+T}=a_n+L.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Uniform gap bound — translation by rad(A) preserves divisibility by every prime of A, and each old term meets A.
  - Bounded-memory/forgetting lemma — an essential old blocker should force a new strict descent among finitely many A-prime signatures when tracked through a bounded candidate window.
  - Finite-state recurrence — bounded memory plus residues modulo one fixed modulus leaves finitely many deterministic states, as in the confinement moves of aimo-0577 and aimo-0678.
  - From gap cycle to translation — summing T consecutive periodic gaps gives a constant L.
Open gaps: Steps 2-3 are wholly unproved and are the core of this framing; in particular, it is not yet established that witness chains descend rather than acquire new incidental large primes. Step 5 must eliminate a transient, since a generic finite automaton gives only eventual periodicity.
Cases to cover: an offset may have several rejecting witnesses; repeated versus strictly new A-prime signatures; cycle with a nonempty transient versus cycle starting at the initial state.
Watch out for: Bounded gaps alone do not imply bounded memory or periodicity. The modulus M must emerge from Step 3 and cannot be defined from all raw prime factors, which may be infinite.

translation-equivariant-greedy-set: new
Target: Prove directly that the whole selected set is invariant under one positive translation and deduce the indexed relation a_{n+T}=a_n+L for every n.
Technique: Greedy maximal-set characterization on the coprimality graph, canonical representatives of residue signatures, and strong induction under a translation; this is an order-theoretic framing rather than state stabilization.
Skeleton:
  1. Let G be the set of integers selected by scanning m=A,A+1,... and accepting m exactly when it is noncoprime to every previously accepted integer; prove this scan is equivalent to the original recurrence.
  2. Let P be the product of primes <=A. For each m>=A construct a canonical representative c(m)<=m having the same <=A prime-divisibility signature and no larger prime factors, via the least-power prime-stripping construction surfaced in aimo-0030.
  3. Prove by strong induction on max(x,y) the exchange theorem: if x,y>=A have the same <=A signature, then x is accepted by the greedy scan if and only if y is accepted. In the contrary minimal pair, use a previously accepted coprime blocker for the rejected member, replace that blocker by its canonical representative, and use minimality to transfer its accepted status; the transferred blocker is forced coprime to both representatives, contradiction.
  4. Since m and m+P have equal signatures, Step 3 gives m in G iff m+P in G for every m>=A; thus G is exactly translation-invariant by P from its first element, with no transient.
  5. Let T be the number of accepted residues in [A,A+P). Translation by P bijects each consecutive block of T selected integers onto the next one, so the increasing enumeration satisfies a_{n+T}=a_n+P for all n.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Greedy-scan equivalence — the recurrence always chooses the first integer after the current accepted one adjacent (by noncoprimality) to every earlier accepted vertex.
  - Canonical representative — multiplying the product of small signature primes by the least needed power reaches A while the presence of any q>A gives the strict size comparison c(m)<sq<=m.
  - Exchange theorem — a minimal signature-discrepant pair yields a smaller accepted blocker whose stripped representative transfers acceptance and coprimality, contradicting the greedy decision.
  - Translation-to-index lemma — exact invariance of an ordered set by P shifts its kth element by P after the fixed number T of occupied residues.
Open gaps: Step 3 is substantial: the builder must orient the minimal counterexample so every canonical representative is strictly smaller when needed and verify that stripping preserves all coprimality relations required in the contradiction. If that direct exchange stalls, it should not silently import the game-theoretic P-position theorem from the first approach, because that would collapse the two framings.
Cases to cover: x<y and y<x; blocker already has no large prime versus requires stripping; canonical representative equals the original blocker; signatures with one or several small primes.
Watch out for: A selected integer always has at least one <=A prime factor because it meets A, but an arbitrary rejected blocker need not; apply canonical stripping only after proving the relevant blocker is selected. Exact invariance from A is required—eventual invariance alone does not prove the statement for every n.
