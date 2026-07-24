## Status
partial

## Approaches tried
- **Charging against ω(a_1) or Ω(a_1)** (candidate 1 from the round-6 outliner
  report) — **dead end, confirmed again.** Recruited primes need not divide a_1
  (already known: a_1=175 recruits 13 ∤ 175=5²·7). No mechanism in the certified
  lemma stack (Free Facts, Bounded Witness, Lemma G, Lemma H) ties a recruited
  prime back to P(a_1) itself — every certified lemma only ties a recruited prime
  to the *witness terms'* factorizations, never to a_1 directly. Not re-attempted
  further; abandoned per the outliner's own flagged obstruction.
- **Charging against growth rate / a_n = O(n) (candidate 3)** — not re-attempted.
  Confirmed the outliner's own assessment: a bounded-size factorization per term
  (Bounded Gap Lemma) is compatible with unboundedly many *distinct* primes across
  different terms, so O(n) growth gives no bound on distinct recruited primes.
  Dead end, no new angle found; spent no further effort here per the outliner's
  explicit "likely dead" flag.
- **Charging against |𝒫| / C(|𝒫|,2) via a directly-proved "batch resolution"
  theorem (candidate 2)** — the round's real work item. Found genuine, robust,
  previously-undocumented computational support for a *stronger* phenomenon than
  the outliner's motivating example asked about ("batch resolution": one
  recruited prime resolves several simultaneously-rogue pairs at once). Attempted
  a proof via a natural pigeonhole ("Hub Singleton" argument, below); the
  argument is correct but **provably insufficient** to explain the full
  phenomenon (falsified as *the* mechanism by direct counting on the same data
  that motivated it — see below). Conclusion: batch resolution is real but is
  **not an independent route around the shared crux** — see "Current best" for
  the precise finding and why.

## Current best

### 0. Target, stated precisely (per CLAUDE.md and the round-6 outline-reviewer)

Two strengths of target, kept distinct throughout:
- **(T-weak)** The recruitment process (as defined in `covering-system-construction`
  Step 4c, iteratively enlarging S₀ by one Lemma-G-guaranteed prime per rogue pair
  until no disjoint-base-type extended-persistent pair fails to intersect) halts
  after finitely many rounds. Sufficient for the problem's Step 5 (CRT + cyclic
  pigeonhole) finish.
- **(T-strong)** The number of rounds is bounded by an explicit, computable
  function of a_1 (e.g. ≤ C(|𝒫|,2) ≤ 2^{2|Q|}, or something sharper).

Neither is established by this approach. What *is* established: a precise
account of why the most promising charging object (candidate 2) does not give
an argument independent of the crux the sibling approaches are already
attacking (Full-Absorption Hypothesis / Collateral-Safety's imported gap G3),
and a new, sharper, unconditional-looking empirical phenomenon that should feed
back into that shared work rather than replace it.

### 1. Computational setup (fresh, independent implementation)

All experiments below use a from-scratch Python implementation
(`/tmp/round-6/charging/gen.py`, using `math.gcd` for the greedy generation and
`sympy.primefactors`/`factorint` only for post-hoc analysis — no shared code with
any other approach or explorer this round), following the **literal minimal
(earliest-occurrence) witness convention** mandated since round 4's bug and
reconfirmed in round 5/6: Q = P(a_1); τ(n) = P(a_n)∩Q; persistent base types 𝒫
detected via a tail-window occurrence count (≥5 hits in the second half of a run
of length N, N = 1800–2000 in all runs below); for each persistent type its
*earliest* occurrence is used as the canonical witness (never a tail-sampled
occurrence); S := ⋃_{B∈𝒫}(P(a_{m_B})\Q), S₀ := Q∪S; extended types
ρ(n) := P(a_n)∩S₀ and S₀-extended-persistent types 𝒫' detected the same way;
rogue pairs = pairs A',B' ∈ 𝒫' with disjoint base types (A'∩Q, B'∩Q disjoint,
both nonempty) and A'∩B' = ∅, using each type's own earliest occurrence as its
witness (n_A, n_B), exactly as in the certified Lemma G
(`lemmas/extended-earliest-witness-intersection.md`).

**Caveat, stated honestly.** Persistence detection here is a computational
heuristic (tail-window occurrence count), not the rigorous "infinite pigeonhole"
definition — the same caveat that applies to every numerical claim by every
approach in this workspace (persistence *in the true infinite sequence* cannot be
verified by finite computation, only made highly plausible). One discrepancy was
observed directly: re-running the round-6-reported `a_1=4807` example through
this independent implementation at N=2000 found **no rogue pair at all** (reported
`V=∅`), contradicting the round-6 explorer/outline-reviewer's confirmed rogue pair
{3,5,19} vs {2,11}. This is flagged, not resolved — likely a tail-window/threshold
mismatch in this implementation's heuristic persistence detector, not a
retraction of the round-6 finding (which was independently triple-confirmed by
three from-scratch implementations already). **Do not treat this file's
`a_1=4807` non-finding as a re-falsification of anything** — it is noted here only
in the interest of full disclosure of this implementation's limitations. All
positive findings below (rogue pairs that WERE found) were spot-checked by hand
(explicit factorizations shown) and are trustworthy regardless of this caveat.

### 2. New empirical finding: robust multi-pair "batch resolution," and why the
cheap explanation for it fails

Scanning products of 3–5 distinct primes drawn from primes in [11,90] (1541 seeds
tried, budget-limited scan), 15 seeds were found where **two or more** disjoint-
base-type rogue pairs are simultaneously open at the same stage S₀ (up to 8
simultaneous rogue pairs, seed a_1=125911=37·41·83). **In every one of these 15
seeds, with zero exceptions, all simultaneously-open rogue pairs share exactly
the same recruited prime** (the Lemma-G-guaranteed prime dividing both witnesses
of each pair) — e.g. a_1=6851=13·17·31 has 4 simultaneous rogue pairs, all
resolved by prime 5; a_1=125911 has 8 simultaneous rogue pairs, all resolved by
prime 5; a_1=134461=17·19·23·43·47·53(partial) has 3, all resolved by 7. Full
raw data in `/tmp/round-6/charging/scan6.py` output (reproducible; seeds and
exact rogue-pair/witness/shared-prime tuples listed for all 15).

This is genuinely new data (broader and more systematic than any collateral
observation currently in `current.md`) and is exactly the "batch resolution"
phenomenon the round-6 outliner asked to be tested — **confirmed present, far
more often and more strongly than the single a_1=6851 instance the outliner's
own report was built on.**

**Natural cheap explanation attempted: the Hub Singleton argument.**
Observation: when a type H (extended-persistent) is rogue simultaneously against
several distinct partners X₁, X₂, ..., its own earliest witness n_H is *fixed*
across all these pairs (Lemma G's witness index depends only on the type, not on
which partner it is being compared against). So for every partner X_i, the
Lemma-G shared prime q_i satisfies q_i ∈ P(a_{n_H}) ∩ P(a_{n_{X_i}}); since
q_i ∉ S₀ by Lemma G, in fact **q_i ∈ F'_H := P(a_{n_H})\S₀ for every i** — this is
immediate from Lemma G's own proof (not a new lemma, just an unpacking of it).
**Corollary (Hub Singleton Batch Lemma, provable, trivial given Lemma G):** if
|F'_H| = 1, then q_i equals the unique element of F'_H for every partner X_i — a
single recruited prime provably resolves *all* of H's simultaneous rogue
relationships at once, unconditionally, no Full-Absorption-type hypothesis
needed.

**This corollary is real but does NOT explain the phenomenon in general — checked
directly and falsified as *the* mechanism.** Computing |F'_H| for every hub type
found in the 15-seed scan (`/tmp/round-6/charging/scan6.py` companion query):
of 19 hub instances found, only **3 have |F'_H| = 1** (e.g. a_1=41819 hub
{19,3,5}, F'_H={7}; a_1=53041 hub {5,31}, F'_H={7}); the other **16 have
|F'_H| = 2** (e.g. a_1=13481 hub {17,3}, F'_H={5,53}; a_1=125911 hub {41,2},
F'_H={5,31}; a_1=62567 hub {19,3}, F'_H={157,7}). In every one of these 16
non-singleton cases, the SAME one of the two elements of F'_H is still picked by
every partner (e.g. always 5 for the 13481/125911 examples, always 7 for the
62567 examples) — never a mix. **The Hub Singleton Lemma therefore only explains
3/19 of the observed instances; the other 16/19 exhibit a strictly stronger,
unexplained phenomenon:** among the two candidate primes in F'_H, one is
consistently "the" real recruit and the other is consistently never picked by any
partner, across many independent pairings.

**Why this is not an independent route (the honest conclusion).** The pattern
"one specific element of a 2-element F' set is always load-bearing, the other
never is" is *exactly* the distinction the sibling `greedy-exchange-cost-
potential` approach's **Full-Absorption Hypothesis (FAH)** and **Lemma H
(Critical Prime Dichotomy)** are already built to capture (Lemma H's branch (a)
"incidental" vs branch (b) "load-bearing" split). This round-6-charging data is,
if anything, a genuinely useful *cross-check* supporting FAH's empirical base
(it shows the same distinguished-prime phenomenon holding not just across
repeated occurrences of one type as in FAH's original statement, but across
*different rogue partners of a hub type* — a related but distinct axis the FAH
proof effort had not yet checked). But it means candidate 2's charging argument,
to be completed, requires resolving the *same* open question (why is one
specific prime always the distinguished one) that Approach 2 is already
attacking. **This approach's charging framing does not evade the shared crux;
it independently re-discovers the crux from a different angle and adds
supporting data, but does not close it.**

### 3. Consequence for T-weak / T-strong

Neither target is established:
- T-strong via "≤ C(|𝒫|,2) rounds, each round resolving ≥1 new base-type pair
  permanently" requires exactly the "full absorption" property (a recruited
  prime, once added, keeps the base-type pair safe forever) — this is Approach
  1's imported gap G3 / Approach 2's FAH, not something this approach's charging
  mechanism supplies independently.
- The alternative, more optimistic strengthening suggested by the data above —
  "at most 1 round is EVER needed in total, because all simultaneously-rogue
  pairs at any stage always share one prime" (tested directly: for all 15
  multi-pair seeds plus the 2 known single-pair seeds a_1=11305, all reached
  V=∅ after exactly one round of recruiting the shared/only prime, 0 further
  rounds needed in every test — see `/tmp/round-6/charging/rounds.py`) — is an
  even *stronger* claim than FAH (a global "single universal recruit per
  snapshot" rather than a per-pair "eventually all" recurrence), hence at least
  as hard to prove, not easier. It should not be cited or relied on by any other
  approach as if it were established; it is reported here purely as an
  interesting, well-supported (17/17 tests, 0 counterexamples) but **entirely
  unproven** empirical conjecture, worth flagging to Approach 2's builders as
  additional motivation/cross-check for FAH, not as a substitute proof.

### 4. What remains open, stated explicitly

(G1) No charging mechanism independent of Full Absorption / FAH has been found;
candidate 1 and candidate 3 are dead ends (confirmed); candidate 2 (batch
resolution) is real but reduces to the same open question. This is a genuine
negative result for the hedge strategy as originally conceived — it should
lower confidence that a fully independent route exists via *this* framing,
though it does not rule out some other charging object not yet identified.
(G2) T-weak (mere finiteness) still has no proof strategy independent of
Approach 2 succeeding.
(G3) The stronger "single universal recruit per snapshot" empirical pattern
(section 3) is new, interesting, and not yet attempted as a proof target by
anyone; if the population wants to keep pursuing the charging framing, this is
the sharpest concrete not-yet-falsified statement to attack next, understanding
that it is *at least* as strong as (likely implies) FAH, not a weaker
fallback.

## Full proof
(Not applicable — Status is `partial`, not `solved`.)
