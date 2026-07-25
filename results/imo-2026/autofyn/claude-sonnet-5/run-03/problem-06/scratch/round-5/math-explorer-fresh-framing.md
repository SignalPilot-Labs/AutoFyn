## imo-2026-06

### Distinct openings (genuinely different from Q/Good_Q machinery)

**Opening 1 — Scalar bounded-gap pigeonhole on g_n(T), no primes at all.**
Using the already-certified, unconditional `bounded-gap-via-rad-a1.md`
(`a_{n+1}-a_n ≤ R := rad(a_1)` for every n, no transient), define, for any
FIXED T ≥ 1, `g_n(T) := a_{n+T} - a_n`. Since each of the T individual gaps
lies in `[1,R]`, `g_n(T) ∈ [T, TR]` — a set of at most `TR` possible integer
values, for every n. By plain pigeonhole (infinitely many n, finitely many
values), for every fixed T there is a value L(T) and an INFINITE set
`Y_T ⊆ ℕ` with `a_{n+T} = a_n + L(T)` for all `n ∈ Y_T`. This is
unconditional, elementary, and — I checked — is NOT the family killed by
`monotonicity-obstruction.md`: that lemma rules out pigeonhole on a state
that includes a monotonically *accumulating set* component (e.g. a growing
"type" $\mathcal T_n$); here the pigeonholed object is a bare scalar
difference with no accumulating set component, so the obstruction does not
apply. This is a genuinely new, certifiable building block not currently in
`lemmas/`. It gives infinitely-often periodicity "for free" for every T; the
open problem becomes turning "infinitely often, for every T" into "always,
for some T" — i.e. it relocates the central gap to an EXTENSION step that
is scalar/arithmetic in flavor rather than prime-set-flavored.

I stress-tested the most naive extension idea and it is FALSE in general
(verified computationally, a_1=99, T=1): "two CONSECUTIVE good indices
(n, n+1 both satisfying g_n(T)=L(T)) implies g_m(T)=L(T) for all m ≥ n" —
false already at n=5, breaks within a handful of steps when T is not the
true period. So a naive local-matching induction will not work; any
extension argument needs a genuinely global ingredient (this is consistent
with, and gives independent scalar-level confirmation of, why the field's
existing local/windowed mechanisms have all failed). Do NOT re-propose bare
"two consecutive matches propagate" as a finishing move.

**Opening 2 — ISL 2015 N6 (aimo-0680, already flagged in round 1) re-examined
as a structural template, not just a finishing-move donor.** I re-read its
full official solution (not just the earlier round's fragment). Its shape:
(a) show the map is injective, partition the domain into finitely many
"rows" (orbits) via the codomain-defect condition; (b) for a row that is
"dense enough," derive an EXACT ARITHMETIC-PROGRESSION law $f^j(a_x) = a_x +
jT_x$ for an infinite index set, using a strong extra hypothesis: $d \mid
f^d(m)-m$ for ALL $m,d$ (given in the problem, not derived); (c) extend this
from the infinite index set to literally every $j$ via a "sandwich"
divisibility trick: pick $y$ far ahead in the infinite set so that
$(y-j)$ exceeds a known bound on $|f^j(a_x)-(a_x+jT_x)|$, and note both
$f^y(a_x)-f^j(a_x)$ and $f^y(a_x)-(a_x+jT_x)$ are divisible by $y-j$, so
their difference — the quantity you want to show is 0 — is divisible by
$y-j$ AND smaller in absolute value, forcing it to vanish.
**This sandwich trick is the single most valuable transplant candidate in
the corpus for closing our own extension gap (Opening 1's leftover
problem)**, but it does NOT transplant verbatim: our sequence has no given
hypothesis analogous to "$d \mid f^d(m)-m$ for all $m,d$." That divisibility
is exactly what would need to be independently derived for our greedy
sequence before the sandwich argument could run — and I do not see an
obvious source for it (checked: `a_{n+d}-a_n` is not generally divisible by
`d`; e.g. quick check below). So: report this as a HINT worth an outliner
trying to construct a substitute "boundedness + divisibility" pair specific
to our greedy rule (not as a ready-made lemma), rather than as a solved
transplant.

**Opening 3 — direct lcm-of-gaps candidate for L, tested and refuted as a
closed form (consistent with, and reinforcing, round 4's dead ends).**
Since every gap `d_n ∈ [1,R]`, the number `Λ := lcm(1,...,R)` is a fixed,
a-priori-computable, sequence-independent integer. I tested whether `L`
(the true empirical period-shift) always divides some small multiple of
`Λ`, or whether `Λ` itself could serve as a candidate modulus for a
finite-state automaton on gaps. This is effectively the same territory as
the already-dead `windowed-epsilon-automaton-failure.md` (finite alphabet ≠
periodic without unbounded lookback) — I did not find a new angle here
beyond what's already certified dead; flagging as **checked, not
promising**, so the outliner doesn't need to re-spend a round on it.

**Opening 4 — dynamical/ergodic compactness on `(a_n mod p)` for a single
growing prime**: considered but did not find independent traction beyond
what jacobsthal-covering-bound and state-compactness-pigeonhole already do;
did not pursue further given time budget — flagging as unexplored rather
than dead.

### Candidate technique(s)
- The **pigeonhole-on-scalar-difference** lemma (Opening 1) as a fresh,
  certifiable, unconditional building block, orthogonal to the killed
  set-state pigeonhole family.
- The **ISL 2015 N6 sandwich/divisibility trick** (Opening 2) as the
  strongest available donor mechanism for turning "infinitely often" into
  "always" — contingent on deriving a substitute divisibility fact for this
  problem's greedy rule (open, non-trivial, worth a dedicated approach).

### Cheap-kill candidates
- None new beyond what's already certified; Opening 3's "gap-alphabet
  automaton" territory is a re-confirmation of an existing dead end
  (`windowed-epsilon-automaton-failure.md`), not a new kill.

### Knowledge-base entries to use
- `knowledge_base.md` "Order of an element, Fermat/Euler: periodicity of aⁿ
  mod m; eventual periodicity of products of a sequence mod m" (line ~65) —
  generic periodicity-mod-m technique, already implicitly used by the Q/L
  framework; no new leverage found beyond current use.
- `knowledge_base.md` "Pigeonhole / extremal principle" (lines 108, 188) —
  supports Opening 1's scalar pigeonhole formally, but this is elementary
  enough not to need a named KB citation beyond standard pigeonhole.
- No Jacobsthal-function, compactness/König, or covering-system entry exists
  in `knowledge_base.md` (checked, absent) — jacobsthal-covering-bound's
  machinery is imported from outside the KB, not from a named entry.

### Analogous past problems (cruxes)
- `aimo-0680` (IMO-SL 2015 N6, domain number_theory) — genuinely the closest
  analog by conclusion shape ("f(n)-n eventually periodic" ≅ "a_{n+T}=a_n+L").
  Crux move: injective-orbit "Table" decomposition + boundedness pigeonhole
  + a sandwich-divisibility extension trick. Re-confirmed analogous at the
  conclusion level; its middle-step divisibility hypothesis does **not**
  hold for our sequence and must be independently supplied — this is new
  information beyond round 1's flagging (round 1 only matched the *finishing
  move* superficially; I checked the *full* solution and found the
  finishing move's precondition is unmet, narrowing what's actually
  transplantable to just the sandwich-trick *shape*, not the lemma itself).
- No other crux in `number_theory` subtopics `sequences-and-recurrences`
  (only 6 entries, all unrelated: polynomial recurrences, continued
  fractions, functional-equation iteration — none involve a greedy
  gcd-covering construction) or in a targeted keyword search
  ("covering system", "jacobsthal", "greedy"+"gcd") turned up anything else
  resembling this problem's greedy-minimum-under-growing-constraint-set
  structure. This appears to be a genuine corpus gap (confirms round 4's
  finding), not a missed search.

### Prior progress
Central gap unchanged from round 4's `current.md`: does a finite
$Q\supseteq R(a_1)$ exist such that every pair $a_i,a_j$ shares a prime
factor in $Q$ (equivalently $Q_{\min}=\mathrm{Nec}\cup R(a_1)$
self-sufficient)? Still fully open. This report does not close it; it
supplies (1) one new unconditional lemma-candidate (Opening 1) usable by any
approach, (2) a sharper, verified characterization of what would be needed
to transplant the closest crux analog (Opening 2), and (3) confirmation that
two more speculative directions (Opening 3, gap-alphabet automaton; naive
local-matching propagation) are dead, without spending a build round on
them.

### Dead ends (do not retry)
All prior rounds' dead ends stand (see `run_state.md` Rules, rounds 1-4;
not repeated here). New this round:
- **"Two consecutive matching indices for g_n(T)=L(T) propagate forever"**
  — false in general, verified computationally (a_1=99, T=1: breaks after
  n=5). Do not propose bare local-window propagation as a finishing move
  for the extension step opened by Opening 1.
- **ISL 2015 N6's sandwich trick used verbatim** — its precondition ($d
  \mid f^d(m)-m$ for all $m,d$) does not hold for this problem's sequence
  and has no obvious substitute found yet; only the trick's *shape* is
  transplantable pending a new derived divisibility fact, not the lemma.

### Small-case / intuition notes
- Confirmed numerically (a_1 ∈ {35,65,99,105}, 4000 terms): true minimal
  period pairs (T,L) found by robust tail-matching all hold from n=0 with
  zero transient (consistent with round 2-4's repeated finding) — e.g.
  a_1=99: T=72, L=330; a_1=65: T=58, L=390. Labeled conjecture-confirmed-by-
  extensive-numerics only, not proof.
- For T=1 (raw gap sequence, NOT the true period) at a_1=99, the mode gap
  value 6 occurs at 2110/3999 steps — i.e. even the most common single-step
  gap value occurs a clear minority-but-substantial fraction of the time,
  and long non-consecutive runs of it do not imply global periodicity
  (matches Opening 1's negative finding above).
