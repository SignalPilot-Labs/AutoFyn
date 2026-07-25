## imo-2026-06 (lens: prefix-extension gap, non-recurrence mechanisms)

### Distinct openings

1. **NEW — "Self-Type-Compatibility Lemma" (verified correct, unconditional, not previously in the population).**
   Using only the already-certified `lemmas/pairwise-non-coprimality.md` fact
   ($\gcd(a_i,a_j)>1$ for all $i\ne j$) plus set containment (no pigeonhole,
   no state recurrence at all):

   **Claim.** Fix any finite prime set $Q$. If $R(a_i)\subseteq Q$ (i.e.
   index $i$'s *entire* factorization already lies in $Q$), then for
   **every** other index $j$ (earlier or later!), $\tau_i := R(a_i)\cap Q$
   and $\tau_j := R(a_j)\cap Q$ intersect. *Proof:* pairwise non-coprimality
   gives a prime $p\mid\gcd(a_i,a_j)$; since $p\mid a_i$ and $R(a_i)\subseteq
   Q$, $p\in Q$; hence $p\in R(a_i)\cap Q=\tau_i$ and $p\in R(a_j)\cap
   Q=\tau_j$ (as $p\mid a_j$, $p \in Q$). $\blacksquare$

   **Immediate corollary (unconditional, no hypothesis needed):** under
   Hypothesis SS's own requirement $Q\supseteq Q_0=R(a_1)$, taking $i=1$
   gives $R(a_1)\subseteq Q$ automatically — so **$\mathrm{Good}_Q(a_1)$
   holds trivially, for every valid choice of $Q$ in Hypothesis SS, with no
   dependence on $n^*$ or on which types have "appeared yet."** This
   directly kills the naive worry that $a_1$'s type might fail to hit some
   not-yet-realized future type: it can't, by this lemma. So **the very
   first index is never an obstruction** to extending the type-family
   compatibility relation backward to $n=1$ — a genuinely different,
   forward-looking (non-recurrence) argument, exactly matching the lens
   requested.

   **Stronger corollary (propagation, not just anchoring at $n=1$).** If
   $R(a_i)\subseteq Q$ for *every* $i<n$ (i.e. the whole prefix before $n$
   uses only primes already in $Q$), then $\tau_n$ automatically meets
   $\tau_i$ for every $i<n$ — **regardless of whether $a_n$ itself uses a
   prime outside $Q$.** (The witnessing common prime is forced into $Q$ via
   the *earlier* term's full containment, not the later one's.) This
   localizes the only possible source of a prefix-extension failure to
   indices $i$ with $R(a_i)\not\subseteq Q$ ("prime-recruiting" indices) —
   it is a sharper diagnostic of *where* the gap can bite, not a full
   closure.

2. **Numerically re-examined the "run stabilized rule from start" idea
   (state-compactness-pigeonhole's rejected fix) at a finer grain.**
   Verified computationally (a_1 = 15, 21, 33, 35, 45, 77, 105 — see Small-case
   notes) that in *every* tested example, exact periodicity with the correct
   *minimal* $(T,L)$ genuinely holds from $n=1$ (not just eventually), even
   though $R(a_i)\subseteq Q$ fails for many individual terms throughout the
   sequence (e.g. for $a_1=35$, $Q=\{2,3,5,7\}$, terms like
   $110=2\cdot5\cdot11$ and $130=2\cdot5\cdot13$ use an outside prime, yet
   periodicity is undisturbed). This confirms the outside primes are
   genuinely "harmless noise" — $\mathrm{Good}_Q$ only reads $R(m)\cap Q$, so
   an extra prime outside $Q$ never *hurts*; what would hurt is a term whose
   $Q$-restricted type $\tau_i$ fails to meet some other type. The
   Self-Type-Compatibility Lemma above explains structurally why this rarely
   happens: most terms in the tested examples are covered because *some*
   earlier or later index has $R(\cdot)\subseteq Q$ and shares the
   witnessing prime.

3. **Mechanism "choose a larger $T$" (multiple of the pigeonhole period) —
   evaluated and downgraded.** This does not look like the right lens: Lemma
   P (`lemmas/periodicity-of-residue-class-union.md`) already gives *exact*
   periodicity of a residue-class-union listing with the *minimal* $T =
   |\mathrm{GoodRes}(Q)|$, not a multiple; the numerical checks above show
   the true minimal $(T,L)$ pair (not an artificially enlarged one) already
   works from $n=1$ in every example tried. Inflating $T$ to a multiple
   doesn't address the actual mismatch (which is about the *set* of accepted
   values near $n=1$ matching $\mathrm{GoodRes}$, not about the period
   length) — no evidence this repairs anything the minimal $T$ doesn't
   already fix. Not recommended as a separate mechanism.

4. **Backward induction directly on the recursive/minimality definition
   (idea 2 from the dispatch) — evaluated, looks structurally blocked.**
   Tried to see whether "$a_{n+1+T}=a_{n+1}+L$" could be used to deduce
   "$a_{n+T}=a_n+L$" by inverting the minimality definition. The obstruction:
   the map $a_n\mapsto a_{n+1}$ (smallest $m>a_n$ meeting the *finitely many
   realized* historical constraints) is not efficiently invertible from
   $a_{n+1}$ alone — recovering $a_n$ requires knowing the entire constraint
   set active at step $n$, which is exactly the unknown prefix data. This
   route seems to require essentially re-deriving the whole prefix from
   scratch, i.e., it doesn't avoid the very difficulty it's meant to route
   around. Do not pursue further without a genuinely new idea for inverting
   the greedy step.

### Candidate technique(s)
- The Self-Type-Compatibility Lemma above (pairwise-non-coprimality +
  containment, no pigeonhole) is the most promising *new* building block —
  it is a genuinely different, forward/structural argument (not
  recurrence-of-state), matching exactly what `monotonicity-obstruction.md`
  says is needed.
- Crux move `aimo-0514`: "when each state deterministically forces both its
  successor **and predecessor**, the transition map is a bijection on the
  finite state set, so every orbit is *purely* periodic, not just eventually
  periodic" — this is the general shape of argument that would close the
  gap if applicable: prove the eventual transition map $g$ on
  $\mathrm{GoodRes}(Q)\subset\mathbb Z/L\mathbb Z$ is **reversible all the
  way back to $a_1$'s own residue**, rather than merely recurrent. Lemma P
  already shows $g$ (successor-in-$\mathrm{GoodRes}$) is a bijection on the
  *set* $\mathrm{GoodRes}$ itself (trivial, since it's a cyclic order), so
  reversibility of $g$ is not the missing piece — the missing piece is
  showing $a_1,\dots,a_{n^*-1}$ (the literal prefix) are *already* elements
  of the $\mathrm{GoodRes}$-listing (i.e. that the true greedy rule and the
  eventual rule coincide that early), which is a different (harder,
  number-theoretic) claim than pure reversibility of the abstract map.

### Cheap-kill candidates
- Check, for each certified/candidate $Q$ in a worked example, exactly which
  indices $i$ have $R(a_i)\not\subseteq Q$ (the only possible failure
  points per finding #1's diagnostic) and see if there's a bound on how many
  such indices exist before $Q$ becomes literally self-sufficient — this
  reduces "prove periodicity from $n=1$" to "prove finitely many, boundedly
  many terms use an outside prime" which is closer in spirit to the
  (still-open) central Hypothesis SS gap itself. Not a full mechanism yet,
  but a sharper finite target than "prove Hypothesis SS with $n^*=1$" wholesale.

### Knowledge-base entries to use
- Did not find a new named `knowledge_base.md` entry beyond what the
  population already cites (CRT, pigeonhole). The load-bearing new fact this
  round is a direct corollary of the already-certified
  `lemmas/pairwise-non-coprimality.md`, not a fresh KB import.

### Analogous past problems (cruxes)
- `aimo-0514` (combinatorics, `processes-and-algorithms` /
  `invariants-and-monovariants`): "reversible deterministic process ⇒ state
  graph is a union of cycles ⇒ purely periodic, not eventually periodic."
  Genuinely analogous in *shape* (this problem also needs an
  eventually-periodic sequence upgraded to purely-periodic-from-the-start),
  but the mechanism there (an explicit bijective local rule with a
  reconstructible predecessor) doesn't transplant directly, because our
  transition rule (greedy "smallest exceeding a_n satisfying constraints")
  is not obviously reversible in the relevant regime (the realized-so-far
  constraint set changes with $n$, unlike a fixed local turn-rule). Useful
  as a target shape for a mechanism, not a ready-made proof template.
- `aimo-0916` (combinatorics, `processes-and-algorithms`): "stabilize a
  descending chain of images of a self-map on a finite set, then take the
  power that restricts to the identity on the stable core" — same idea as
  the population's existing orbit-pigeonhole route (already tried, already
  known to only give *eventual* periodicity, not periodicity from $n=1$).
  Not a new lead for the prefix gap specifically, since it has exactly the
  same "transient vs. core" structure already ruled insufficient by
  `monotonicity-obstruction.md`.
- No crux found that fixes an eventually-periodic-from-a-greedy-minimality
  process to purely-periodic-from-index-1 by a non-recurrence route; this
  appears to be a genuinely under-explored corner even in the corpus.

### Prior progress
See `results/imo-2026-06/current.md`: central gap (Hypothesis SS,
self-sufficiency of a finite active prime set) remains open; conditional on
it, tail periodicity ($n>m_0$) is proved via two independent routes
(orbit-pigeonhole and residue-class-union, both certified). Prefix-extension
(this round's target) remains open; `monotonicity-obstruction.md` rules out
one whole family of state-pigeonhole fixes, and
`state-compactness-pigeonhole.md` round 2 separately rejects "run the
stabilized rule from the start."

### Dead ends (do not retry)
- "Enlarge the pigeonhole state (residue, or residue+accumulating type-set)
  and hope the $n=1$ state recurs" — provably impossible in general, by the
  certified Monotonicity Obstruction Lemma (`lemmas/monotonicity-obstruction.md`).
  Re-verified this round: correct, general, applies to any monotone
  set-valued state component.
- "Run the eventual stabilized rule $\mathrm{Good}_Q$ from $n=1$ and hope it
  reproduces the true sequence" — refuted in `state-compactness-pigeonhole.md`
  round 2 (the true early-regime rule is *weaker*, using only realized
  constraints, so $a_{n+1}\le b_{n+1}$ with strict inequality typical
  pre-stabilization). Re-checked this round: the argument is sound (the true
  candidate set for early $n$ is a strict superset of the $\mathrm{Good}_Q$
  candidate set, by Proposition B), so this fix genuinely cannot work as
  stated.
- "Blow up $T$ to an arbitrary multiple of the pigeonhole period" — no
  evidence this helps; the minimal $(T,L)$ pair already works from $n=1$ in
  every tested example (see Small-case notes), so there's no mismatch to
  paper over with a larger period.
- Naive backward induction inverting the greedy-minimality step one index at
  a time — structurally blocked (the forward map is not invertible from a
  single later value without reconstructing the whole earlier constraint
  history); do not retry without a fundamentally new idea for inversion.

### Small-case / intuition notes (all conjectural, verified only by
computation, not proof)
- Computed sequences for $a_1\in\{6,10,15,21,33,35,45,77,105\}$. In **every**
  case, exact periodicity $a_{n+T}=a_n+L$ holds for **all** $n\ge1$ with the
  minimal $(T,L)$ pair (verified up to the computed range: e.g. $a_1=15$:
  $T=8,L=30$; $a_1=35$: $T=34,L=210$; $a_1=105$: $T=58,L=210$; $a_1=77$:
  $T=18,L=154$). No example found (yet) with a genuine transient where the
  minimal $(T,L)$ *fails* for some small $n$ before "kicking in" later —
  this is strong (but still only empirical) evidence that Hypothesis SS, if
  provable at all, is provable with $n^*=1$ directly (i.e. the
  prefix-extension gap may not need a *separate* mechanism from the central
  gap — strengthening Hypothesis SS itself to hold from $n^*=1$, using the
  final/correct $Q$ rather than $Q_0=R(a_1)$, might close both gaps at once).
  This reframes the secondary gap: instead of "prove Hypothesis SS
  eventually, then separately extend backward," the outliner could consider
  targeting **"Hypothesis SS with $n^*=1$" as the single unified target**,
  using the Self-Type-Compatibility Lemma (opening #1 above) as a first
  building block, since it already unconditionally disposes of the $n=1$
  boundary case.
- For $a_1=35$ (Q={2,3,5,7}), checked which prefix indices have
  $R(a_i)\subseteq Q$: fails at $i=14$ ($110=2\cdot5\cdot11$), $i=17$
  ($130=2\cdot5\cdot13$), $i=22$ ($165=3\cdot5\cdot11$), etc. — these
  "outside-prime" indices are scattered throughout the whole sequence (not
  confined to a bounded prefix), yet periodicity is never disturbed. This
  confirms opening #1's point: an index with $R(a_i)\not\subseteq Q$ is not
  automatically a failure point, because *some other* index (sharing the
  same actual common prime, which happens to lie in $Q$ anyway) still
  supplies the required intersection — worth further investigation, but not
  resolved this round.
