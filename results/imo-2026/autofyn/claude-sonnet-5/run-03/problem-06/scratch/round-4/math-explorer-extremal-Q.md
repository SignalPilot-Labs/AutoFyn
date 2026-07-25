## imo-2026-06

### Distinct openings (extremal/minimal-Q construction lens)

All four openings below target the single unified central gap (Reduction
Lemma, `lemmas/reduction-lemma-ss1-vs-unified-claim.md`): does there exist a
finite $Q\supseteq R(a_1)$ with $\mathrm{Good}_Q(a_n)$ for every $n$? None of
them repeat the four dead mechanisms (g(Q) threshold, prime-size threshold,
$\Lambda$-split, windowed $\epsilon_n$ automaton).

**Opening 1 — "load-bearing recruitment count" (the population's own flagged
but untried idea).** `jacobsthal-covering-bound.md` §3 explicitly names, as
its one remaining untried mechanism, bounding *the number of steps at which
an outside prime can still provide a strict saving over the $L_Q$-fallback*
as a function of how much of $Q$'s "signature coverage" (which subsets of $Q$
occur as $\{R(a_i)\cap Q\}$) has saturated. Concretely: define $Q_n$ as the
running set of primes ever load-bearing up to step $n$ (a prime $p$ is
*load-bearing at step $n{+}1$* if $p$ is the/a prime actually certifying
$\gcd(a_{n+1},a_i)>1$ for some $i\le n$ for which no other already-active
prime works). Try to show a genuinely new load-bearing recruitment can only
happen while the "signature multiset" $\mathcal T_n=\{R(a_i)\cap Q_n\}$ is
still growing, and since $\mathcal T_n\subseteq 2^{Q_n}$, growth of $Q_n$
feeds back into a bound on how much $\mathcal T_n$ can still grow — a
mutual-recursion / self-bounding argument, not a size threshold on any single
prime (this is the structural difference from the two dead "threshold"
mechanisms, which tried to bound an individual prime's size or the covering
gap $g(Q)$, both shown false by residue-alignment counterexamples). **Status:
genuinely untried as a rigorous lemma; the population has only stated it as
a direction, never attempted a proof.** This is the most promising candidate
I can identify that is (a) not one of the four dead mechanisms and (b) not a
restatement of the Reduction Lemma's already-unified target.

**Opening 2 — extremal/minimal $Q^*$ characterized via the Adjacent-Link +
$\Lambda$-stabilization machinery, but going "one hop further" than the
already-refuted $\Lambda$-split.** `finite-subtraction-vacuous.md` correctly
kills the naive split $Q=\Lambda\cup(Q\setminus\Lambda)$. But note the
Adjacent-Link Lemma bounds only *consecutive*-pair gcds; it says nothing
about $\mathrm{gcd}(a_i,a_j)$ for $|i-j|\ge2$. A genuinely different
construction: define $\Lambda^{(k)}$ analogously for gap-$k$ pairs
($\Lambda^{(k)}_n:=\bigcup_{i}\{p:p\mid\gcd(a_i,a_{i+k})\}$) and ask whether
$\bigcup_{k\ge1}\Lambda^{(k)}$ stabilizes to a *fixed finite universe*
independent of $k$ — this would need a $k$-uniform bound on
$\gcd(a_i,a_{i+k})$ analogous to `bounded-gap-via-rad-a1.md`, which is NOT
automatic (the bounded-gap lemma only bounds $a_{i+1}-a_i$, not
$a_{i+k}-a_i$, though trivially $a_{i+k}-a_i\le kR$, giving
$\gcd(a_i,a_{i+k})\mid$ something $\le kR$ that grows with $k$ — so the
"fixed universe" trick that made $\Lambda$ work does **not** obviously
transplant to $\Lambda^{(k)}$ for $k\ge2$; this needs to be checked carefully
before building on it, and may itself be a dead end. Flagging as an opening
to explore, not a working construction.)

**Opening 3 — direct existence via the Reduction Lemma's own structure: build
$Q$ as the closure of $R(a_1)$ under a **finite, explicitly bounded** number
of forced additions, each addition justified by a *counting* argument on how
many distinct "signature types" $\tau=R(a_n)\cap Q$ can coexist before the
greedy rule is forced to introduce a genuinely new prime to keep producing a
*minimal* (not just valid) next term.** This is a sharper version of Opening
1: instead of tracking "load-bearing at some step," track the **finite
poset** of signature types $\mathcal T\subseteq 2^Q$ directly, and try to
show that once $\mathcal T$ stops growing (which — by a pigeonhole on
$|2^{Q_n}|$ if $Q_n$ were already known finite — would follow, but $Q_n$
finiteness is exactly what's unproved, so this is circular as stated) OR
alternatively bound the recruitment process by the **number of distinct
sets $R(a_n)\cap Q_{n-1}$ that can occur among the FIRST $n$ terms before
some new prime is forced**, using an explicit sunflower/covering-design
argument (a family of finite sets that pairwise intersect within a bounded
universe has bounded "new witness" needs — cf. Helly-type / sunflower lemma
territory, not present in `knowledge_base.md` currently, worth adding if
this pans out). I could not verify numerically whether this avoids
circularity in the time available; flagging as a genuinely different idea to
test, not a working construction.

**Opening 4 — reversibility / bijection framing for the *prefix-extension*
half instead of the existence half (crux-inspired, see below).** Rather than
constructing $Q$ from scratch, ask: once $Q$ (or the eventual period tail) is
known to exist for $n\ge n_1$, is the greedy step map *invertible* on the
finite state space (the residues mod $L=\prod Q$ combined with the finite
signature data)? If the transition were a bijection on a finite state set,
the orbit would be **purely periodic with no transient at all**, sidestepping
`monotonicity-obstruction.md`'s "specific state recurs" obstruction entirely
(that lemma blocks arguments claiming a *forward* pigeonhole recurrence
forces backward extension; it says nothing about genuine bijectivity). This
is exactly the mechanism in the crux corpus's `aimo-0514` (see below). I
flag this as a **structurally distinct idea from the four dead mechanisms**,
though I have doubts it applies directly: the greedy step $a_{n+1}=\min\{m>a_n:
\mathrm{Good}_Q(m)\}$ is manifestly **not reversible** in the state variables
usually tracked (it is a $\min$-operator, and min-operators are typically
many-to-one, not bijective) — so this needs its own dedicated check before
being trusted, and may fail immediately once someone tries to write down the
"state" and the claimed inverse map. Since this attacks prefix-extension
rather than existence-of-$Q$, per the Reduction Lemma it is now logically
subsumed by existence-of-$Q$ anyway — so this is lower priority than Openings
1–3, included for completeness since the dispatch mentioned covering
systems / greedy termination broadly.

### Candidate technique(s)
- Opening 1/3: a counting/pigeonhole argument on the **signature poset**
  $\mathcal T_n\subseteq 2^{Q_n}$ combined with a self-referential bound on
  $|Q_n|$ — genuinely different in kind from the four dead mechanisms (those
  bounded a single prime's *size*; this would bound the *number of distinct
  set-signatures*, a combinatorial quantity, not an arithmetic one).
- Opening 2: extend Adjacent-Link/$\Lambda$-stabilization to gap-$k$ pairs —
  needs an explicit new bound (does not currently exist in the population).
- Opening 4: reversibility of a finite-state map (cf. `aimo-0514`), likely
  inapplicable here because the recursion is a $\min$, but worth a 10-minute
  check before discarding.

### Cheap-kill candidates
- **Before investing in Opening 3's sunflower/covering-design machinery**:
  check numerically whether the number of *distinct* signatures
  $R(a_n)\cap Q$ (for the true, empirically-observed eventual $Q$) actually
  stabilizes early or keeps growing throughout the transient — if it keeps
  growing for a long transient with no visible bound tied to $|Q|$, the
  "signature poset stops growing early" intuition behind Opening 3 is
  probably false and should be dropped fast.
- **Before investing in Opening 2**: check numerically whether
  $\Lambda^{(2)}$ (gap-2 link primes) stays inside a fixed universe as $n$
  grows, for 2–3 values of $a_1$. If it doesn't (grows unboundedly / includes
  arbitrarily large primes), Opening 2 is dead on arrival — cheap to check
  before any proof attempt.
- **Opening 4**: a 5-minute attempt to write the claimed inverse map down
  explicitly (given $a_{n+1} \bmod L$ and $Q$-signature, can $a_n \bmod L$
  be recovered?) will likely refute it immediately, since multiple $a_n$
  residues can map to the same minimal $a_{n+1}$ — recommend checking this
  before dispatching a builder on it.

### Knowledge-base entries to use
- `knowledge_base.md` "Modular arithmetic, CRT" / "eventual periodicity of
  products of a sequence mod m" (lines ~59–80) — generic background, already
  used by the population's pigeonhole approaches; relevant if Opening
  1/3 produces a genuine finite-state reduction.
- `knowledge_base.md` "Pigeonhole / extremal principle" (lines ~108) — same
  caveat as above; the population has already learned (Monotonicity
  Obstruction Lemma) that a bare state-pigeonhole cannot reach $n=1$ /
  cannot bound $Q$ directly without a fixed finite universe first —
  reuse only in combination with an argument giving a fixed universe (as
  Adjacent-Link did for $\Lambda$).
- No entry in `knowledge_base.md` currently covers sunflower lemmas / VC-type
  bounds on set-systems — if Opening 3 (signature poset) turns out to be
  the right idea, this is a gap in the KB worth flagging to the outliner.

### Analogous past problems (cruxes)
- **`aimo-0678`** (ISL-style: $a_{n+1}=\gcd(a_n,b_n)+1$,
  $b_{n+1}=\mathrm{lcm}(a_n,b_n)-1$, prove $(a_n)$ eventually periodic) —
  genuinely the closest analog in the corpus: same target shape (eventual
  periodicity of an integer sequence from a number-theoretic recurrence).
  Its crux moves: (1) a frozen invariant $s_n=a_n+b_n$ in a "nice regime",
  (2) a **min-of-a-set integer monovariant** $w_n=\min\{m\ge a_n: m\nmid
  s_n\}$ proved non-increasing to force boundedness, (3) **once one
  coordinate is bounded, reduce the other modulo the lcm of the bounded
  coordinate's attainable values**, turning the pair into a map on a finite
  state set, closing via pigeonhole. This is structurally the SAME finishing
  move already used (successfully, for the "eventually" half) by
  `active-set-stabilization`/`state-compactness-pigeonhole` — so it confirms
  the population's finishing machinery is the right shape, but its FIRST
  move (a frozen invariant + min-of-a-set monovariant to get boundedness in
  the first place) is different from anything tried here: worth asking
  whether an analogous "min-of-a-set" monovariant can be built directly on
  $|Q_n|$ or on the signature poset size, rather than on gap size (which is
  what the four dead mechanisms tried and which is a genuinely different
  quantity from $|Q_n|$).
- **`aimo-0514`** (3-regular planar graph walk, prove periodicity is total
  not eventual via reversibility/bijection on a finite "turn" state space) —
  analogous only for the *prefix-extension* half (Opening 4 above); the
  mechanism (bijectivity of the step map on a finite state set) looks hard to
  transplant here since our step map is a $\min$-operator, not obviously
  invertible. Include with a caveat, not a strong match.
- **`aimo-0648`** (floor-of-average recurrence, prove eventually constant via
  bounded state + pigeonhole, then a Bezout-combination propagation argument)
  — same generic "bounded state ⟹ eventually periodic" shape as the
  population's already-used finishing lemma; not offering anything new for
  the existence-of-$Q$ gap specifically.
- No crux in the corpus attacks a **greedy/minimal-selection covering
  recurrence** (i.e. "$a_{n+1}$ = least integer satisfying constraints
  against the WHOLE history") the way this problem does — the corpus's
  eventual-periodicity examples are all fixed-formula recurrences (gcd/lcm,
  floor-average), not greedy-minimum-over-growing-constraint-set recurrences.
  This is a genuine structural gap in the corpus, not a missed match.

### Prior progress
See `results/imo-2026-06/current.md`: Reduction Lemma (round 3, certified)
unifies the central existence gap and the prefix-extension gap into one
statement. 22 certified lemmas in `lemmas/`. No approach has yet produced a
construction or existence proof for $Q$.

### Dead ends (do not retry)
1. **g(Q) covering-gap threshold** (`jacobsthal-covering-bound` round 2) —
   refuted via $a_1=35$ concrete counterexample (membership in $H(Q)$ is not
   a safety certificate against the full history).
2. **Prime-size threshold** ($p_0<g(Q)$ necessary for recruitment,
   `growth-rate-contradiction` round 2) — refuted: a prime's first multiple
   after $a_n$ can land at distance 1 regardless of the prime's size
   (residue-alignment counterexample, e.g. $a_n\equiv-1\pmod{p_0}$).
3. **$\Lambda$-split tautology** ($Q=\Lambda\cup(Q\setminus\Lambda)$,
   `jacobsthal-covering-bound` round 3) — proved logically vacuous:
   $Q\setminus\Lambda$ finite $\iff$ $Q$ finite whenever $\Lambda$ is finite
   (elementary set theory, `finite-subtraction-vacuous.md`).
4. **Windowed $\epsilon_n$ automaton** (`bounded-link-invariant` round 3) —
   proved impossible in general: even when the relative-gap statistic locks
   to a constant, the exceptional-step indicator has period tied to the
   *cumulative* value $a_n\bmod R$, invisible to any bounded window.

I verified (by re-reading, not just trusting the labels) that all four are
genuinely different failure modes — not variants of a single idea relabeled —
so my Openings 1–4 above were chosen to avoid all four mechanisms' actual
content, not just their names.

### Small-case / intuition notes (conjecture, not proof)
- Simulated $a_1\in\{15,21,35,77,105,33,6,12\}$ for 400 terms (Python +
  sympy, brute-force greedy). Observation: **every** prime up to a fairly
  large bound eventually appears as a factor of some term, and moreover
  recurs multiple times within the simulated window (e.g. for $a_1=15$: $2$
  appears 350/400 times, $3$: 300/400, but also $47$ already appears $\ge3$
  times by term 400). This is consistent with (not a proof of) the
  conditional fact recorded in `growth-rate-contradiction.md` that *if*
  periodicity holds, every prime not dividing $L$ must still recur
  infinitely often as an incidental factor. It confirms the key difficulty
  for Openings 1/3: "recurs" and "load-bearing / in $Q$" are empirically very
  different properties (most recurring primes are NOT in the true $Q$), so
  any recruitment-counting argument must track *necessity for a gcd
  witness*, not mere recurrence — a strictly finer distinction than anything
  the four dead mechanisms tried to make.
- For $a_1=15$: numerically found (2000 terms, gap-sequence period search)
  $T=8$, $L=30$, i.e. the conjectured $Q=\{2,3,5\}=\mathrm{rad}(30)$ — only
  **one** prime ($2$) is recruited beyond $R(a_1)=\{3,5\}$. This is a small,
  concrete instance of "bounded forced recruitment," consistent with (but far
  from proving) the idea that recruitment beyond $R(a_1)$ is itself a finite
  process — worth using as a first test case for any Opening-1/3 mechanism a
  future builder tries to formalize (if the mechanism can't even explain why
  exactly one extra prime ($2$) gets recruited for $a_1=15$ and not, say,
  $7$, it isn't sharp enough yet).
