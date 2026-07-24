## imo-2026-06

### central-sets-idempotent-recurrence: new
Target: the whole problem — a_{n+T} = a_n + L eventually (and, if achieved cleanly,
literally from n=1) — via the certified CRT + cyclic-pigeonhole finish
(covering-system-construction Step 5), with FAH/Cofinite FAH supplied by a genuinely
new toolkit (idempotent ultrafilters / Hindman's theorem / the Central Sets Theorem
on βℕ) instead of any of the 16 already-dead pigeonhole/magnitude/counting mechanisms.

Technique: Ramsey-theoretic recurrence in (βℕ,+). Q = P(a_1) is finite, so
{A_p := {n : p | a_n}}_{p∈Q} is a finite coloring of ℕ. Any minimal idempotent in
(βℕ,+) restricted to this coloring picks out a member cell that is **central**
(in Furstenberg's sense); central sets satisfy the **Central Sets Theorem**: they
contain, for ANY finitely many sequences (y_i(n))_{n}, simultaneous IP-shifted
configurations. This is fundamentally more structured recurrence than the plain
"occurs infinitely often" that Persistent-Type Pigeonhole already gives for free —
the bet is that this extra structure can upgrade "some prime of a fixed finite set
recurs" to **syndetic** (bounded-gap) recurrence of the SPECIFIC Lemma-G/Generalized-
Bounded-Witness prime q, which plain pigeonhole cannot deliver.

Skeleton:
  1. Fix disjoint extended-persistent types A', B' (base types A, B disjoint) with
     witness indices n_A, n_B as in the certified Generalized Bounded Witness Lemma —
     by <Generalized Bounded Witness Lemma, lemmas/generalized-bounded-witness-lemma.md>
     there is a specific prime q ∉ S₀ with q | a_n for infinitely many n of type A'.
  2. Reformulate "q | a_n for n of type A'" as membership in a color class of the
     FINITE coloring of the index set {n : ρ(n) = A'} by "does q divide a_n, and if
     not, which prime of a fixed candidate set does" — by construction this is a
     finite partition (finitely many divisor classes, Confined-GCD Lemma,
     lemmas/confined-gcd-lemma.md, already certifies the alphabet is finite).
  3. Apply the Central Sets Theorem (imported from Ramsey theory; NOT currently in
     knowledge_base.md — must be stated and proved/cited carefully by the builder,
     e.g. via Hindman/Strauss "Algebra in the Stone-Čech Compactification" or a
     from-scratch idempotent-ultrafilter argument) to the color class containing
     infinitely many A'-type "q divides" indices, to attempt to upgrade "infinitely
     often" to **syndetic** (bounded gaps between successive q-divisible A'-type
     occurrences) — this is the genuinely new content over every previously-tried
     mechanism (all 16 dead mechanisms use only ordinary pigeonhole/counting, never
     get better than "infinitely often").
  4. IF Step 3 succeeds (syndeticity, not yet cofiniteness): attempt a SEPARATE
     bridging step combining syndeticity with the finite Confined-GCD alphabet and
     the Bounded Gap Lemma's linear magnitude ceiling to force the bounded gaps down
     to zero eventually (i.e. syndetic + finite-alphabet + no unbounded competing
     divisor class ⟹ cofinite) — this bridging step is itself UNPROVEN and must be
     attempted honestly as its own gap, not assumed.
  5. Given Cofinite FAH (from steps 3-4, if they succeed), invoke the already-
     certified Cofinite Sufficiency Lemma (lemmas/cofinite-sufficiency-lemma.md) and
     the existing CRT + cyclic-pigeonhole finish (covering-system-construction Step 5)
     to conclude eventual periodicity — this step is NOT new, already proved.

Key lemmas (claim + mechanism):
  - Finite coloring by q-divisibility class is well-defined on a persistent type's
    occurrence set — because Confined-GCD Lemma already fixes the finite alphabet
    (divisor classes of a fixed integer b), so this is bookkeeping, not new content.
  - (OPEN, the crux of this approach) Central-set / idempotent-ultrafilter recurrence
    upgrades "infinitely often" to "syndetic" for the Lemma-G prime's divisibility
    class — because central sets are, by the Central Sets Theorem, guaranteed rich
    simultaneous recurrence structure (IP-shift-stable) that a plain nonprincipal
    ultrafilter argument alone (which only reproduces existing pigeonhole facts, per
    the explorer's Opening 1 risk note) does not obviously supply; this must be
    checked rigorously, not assumed, and may simply fail to give more than "IP-set"
    (still not cofinite) recurrence.
  - (OPEN, second-stage bridging) Syndetic + finite-alphabet + linear-growth ceiling
    ⟹ cofinite — because a syndetic set with bounded gap B, combined with only
    finitely many possible "which divisor class wins" outcomes per gap, MIGHT force
    eventual stabilization via a second pigeonhole on the (bounded) gap pattern
    itself — this is a genuinely new idea not previously tried (every dead mechanism
    worked with "infinitely often," never "syndetic"), but it is speculative and
    unverified.

Open gaps: Step 3 (does CST/idempotent-ultrafilter machinery actually deliver
syndeticity here, or only IP-density, which the explorer flagged as the likely
outcome and which would NOT close the gap) and Step 4 (does syndeticity even
suffice, granting it). Builder must attempt Step 3 first as a cheap-ish check (does
the color class even admit an explicit IP-set argument for THIS problem's specific
structure) before investing in Step 4; if Step 3 only delivers IP-density (the
explorer's flagged most-likely outcome), this approach should be RETHINK'd honestly
rather than forced through, since IP-density is provably not stronger than the
already-certified "infinitely often" pigeonhole facts in the one respect that
matters (never gives "every sufficiently large n," per the explorer's Opening 1 risk
assessment, matching all 16 prior existential-to-universal failures).

Cases to cover: none (single mechanism, either it works or it is diagnosed dead like
mechanisms 1-16).

Watch out for: (a) do NOT let "central set" language quietly repackage the already-
certified Extended Persistent-Type Pigeonhole as if it were new content — check any
claimed upgrade line-by-line against what plain pigeonhole already gives for free;
(b) this toolkit is absent from knowledge_base.md, so the builder must state and
prove (or precisely cite with a correct statement) the Central Sets Theorem itself,
not just wave at "Hindman's theorem"; (c) budget: if the first check (does this
concretely buy syndeticity on a real seed, e.g. a_1=4807/11305's already-known rogue
pairs, beyond ordinary recurrence) fails quickly, report RETHINK rather than
building out the full βℕ machinery for a dead end — per the explorer's own risk
flag, this is plausible and should not be hidden if found.

---

### greedy-exchange-cost-potential: revise
Target: the whole problem (same as always: a_{n+T}=a_n+L), with this round's
concrete task scoped NARROWLY to formalizing and certifying the fresh explorer's
"No-Restart Lemma" as a standing negative fact — NOT a re-attempt of any of the 16
dead FAH mechanisms (per dispatch: don't waste a builder slot re-hitting the
confirmed wall).

Technique: direct computation + a short structural argument (not a new attack on
FAH). This is explicitly a defensive/bookkeeping addition, scoped to prevent future
rounds from re-losing time to restart-based inductions (as rounds 3, 5, and 8's
seed-coupling-induction have each independently done, in three different disguises).

Skeleton:
  1. State precisely: for n_0 ≥ 2, define the "restarted" sequence b_1 := a_{n_0},
     b_{k+1} := smallest integer > b_k with gcd(b_{k+1}, b_i) > 1 for all i ≤ k. Claim:
     b_k ≠ a_{n_0 + k - 1} in general, for k ≥ 2 — by <direct computation, e.g.
     a_1=15: true a_6=36 vs restarted-at-a_5=30 giving b_2=32>true-successor-path>.
  2. Prove the general reason this must fail whenever it fails: legality of a_{n+1}
     is defined via gcd>1 against ALL of a_1,...,a_n (the FULL history), while the
     restarted process only imposes gcd>1 against b_1,...,b_k (a proper, typically
     much smaller, constraint set) — by <definition unwinding: any index i<n_0 whose
     term a_i is coprime to a candidate value c is a real constraint the true process
     enforces but the restarted process cannot see>, so whenever some i<n_0 exists
     with gcd(c,a_i)=1 for the true process's minimal legal candidate at the
     corresponding step, the restarted process accepts a smaller illegal-for-the-true-
     process value, causing divergence at the very first such step.
  3. State the resulting certified corollary precisely: NO seed-reduction / induction-
     on-ω(a_1) / minimal-counterexample argument that reduces the general problem to a
     "smaller" instance by treating a later term a_{n_0} as a fresh seed is valid
     UNLESS it explicitly carries forward the full constraint set {a_1,...,a_{n_0-1}}
     (in which case it is not actually a smaller/independent instance).

Key lemmas (claim + mechanism):
  - No-Restart Lemma / History-Dependence Lemma: the restarted sequence generically
    diverges from the true continuation at the first index where some early term
    is coprime to the true process's actual minimal candidate but not to the
    restarted process's shorter constraint list — because legality is a conjunction
    over the FULL history (not the tail), a strictly monotone-shrinking property in
    the number of constraints as one moves the "start index" later, so dropping
    constraints can only ever admit MORE candidates as legal, never fewer, making
    exact reproduction non-generic.

Open gaps: none for this narrow scoped task — it is a direct, checkable, essentially
complete argument; the builder's job is to write it up rigorously (general
argument, not just the a_1=15 instance) and get it certified. This does NOT touch
or attempt FAH itself.

Cases to cover: the general argument (step 2) must be shown to apply whenever ANY
early term imposes a real constraint invisible to the restart — builder should also
give one concrete instance (a_1=15, already computed by the explorer) as a
worked example, and check whether there exist DEGENERATE seeds where restarting
happens to coincide with the true continuation (e.g. if n_0=1, trivially — this is
the excluded base case), to state the lemma's hypotheses precisely (n_0 ≥ 2 and at
least one earlier term genuinely constrains some candidate the restarted process
would otherwise accept).

Watch out for: don't overclaim this as closing any part of FAH — it is purely a
negative/defensive fact about a proof STYLE (restart-based induction), independent
of the main crux, useful only to save future rounds' effort.

---

### n1-periodicity-reconciliation: new
Target: the whole problem, with this round's concrete task on the SECONDARY gap
(extending eventual periodicity a_{n+T}=a_n+L, proved for n > N₁' by the certified
CRT+cyclic-pigeonhole finish, back to literal n=1) — a genuinely different wall from
FAH, untouched since round 5's reversible-transition-map first identified its
precise obstruction, giving real population diversity away from the 16-times-dead
FAH corridor.

Technique: direct reconciliation of the transient regime with the eventual cycle,
via an explicit FINITE check rather than an abstract injectivity argument (the
injectivity route was shown insufficient in round 5 — see Watch out for). Conditional
on FAH/Cofinite FAH (still open) for the "T, L exist eventually" half; this
approach's job is only the n=1 extension, honestly flagged as conditional.

Skeleton:
  1. Import, unchanged: the certified finish (a_{n+T}=a_n+L for n > N₁', where N₁' is
     the explicit finite threshold from the Finite Core / Extended Persistent-Type
     Pigeonhole construction) — by <covering-system-construction Step 5, conditional
     on (†)/FAH>.
  2. State the target precisely: show a_{n+T} = a_n + L holds for ALL n ≥ 1, not just
     n > N₁' — equivalently (by round 5's certified obstruction), show the actual
     early terms a_1,...,a_{N₁'} already lie on the SAME eventual periodic cycle,
     i.e. a_{N₁'+T} = a_{N₁'} + L extends backward consistently.
  3. NEW mechanism (not injectivity): use the EXPLICIT FINITENESS of N₁' (an
     effectively computable bound from the certified Finite Core Theorem / Extended
     Persistent-Type Pigeonhole's proofs, both of which are constructive, not merely
     existential) to reduce the n=1 extension to a FINITE, in-principle-checkable
     claim: verify a_{n+T} = a_n + L directly for the finitely many n = 1,...,N₁'
     by unwinding the actual greedy definition on this finite prefix (using only
     Free Facts + the Bounded Gap Lemma's explicit magnitude ceiling to bound the
     search space) — by <Exact-Equality Reduction Lemma, lemmas/exact-equality-
     reduction-lemma.md (round 7, reduces the n=1 gap to exactly N₀−1 explicit
     equalities) if compatible, else re-derive an analogous finite reduction for T,L>.
  4. IF the finite check in Step 3 can be turned into a GENERAL argument (not just
     seed-by-seed verification) — e.g. by showing the early terms' constraint set is
     a SUBSET of the eventual regime's, so the greedy process's choices on the
     prefix already coincide with what the eventual cyclic rule would pick, once one
     checks the prefix's own legal candidates never fall outside the eventual
     residue class G — state this as the key new lemma and attempt to prove it;
     if it fails (as round 5 flagged is plausible, since prefix terms face WEAKER
     constraints), report the precise obstruction rather than forcing a claim.

Key lemmas (claim + mechanism):
  - (OPEN, the actual target) Prefix-Cycle Consistency: the finitely many early terms
    a_1,...,a_{N₁'} already lie on the unique eventual periodic cycle — because
    N₁' is an EXPLICIT, finite, computable quantity (unlike an abstract "eventually"),
    this is in principle a finite verification, not an infinite induction; the
    mechanism to attempt is checking that every early legal candidate's residue mod
    L already lies in the eventual-persistent residue set G (round 5's obstruction:
    this is NOT automatic, since early terms have fewer constraints and could in
    principle pick an out-of-G residue — this must be checked, not assumed).
  - Exact-Equality Reduction (import, round 7 certified): reduces the n=1 gap to a
    finite, explicit list of N₀−1 equalities to check — reuse this reduction
    machinery rather than re-deriving it, then attempt to close the reduced finite
    claim via the Prefix-Cycle Consistency mechanism above (round 7 already showed
    the naive period-rescaling fix is NOT automatic — this approach must find a
    different closing argument, not repeat the dead one).

Open gaps: the entire Prefix-Cycle Consistency claim (Step 3-4) is open; also
whether it can be proved in general or only seed-by-seed (if only seed-by-seed, this
does not close the secondary gap in general and must be reported honestly as such).

Cases to cover: none beyond the single reconciliation claim, but the builder should
sanity-check on at least 2-3 concrete seeds (e.g. a_1=105, T=58, L=210, already on
record) whether the early terms verifiably lie on the eventual cycle, as a cheap
first check before attempting the general argument.

Watch out for: this approach is EXPLICITLY conditional on FAH/(†) (still the primary
open gap) — it does not and cannot close the primary crux; do not let its Status
imply the whole problem is closer to solved than it is. Also: round 5's
reversible-transition-map already showed the injectivity/cycle-structure route by
itself is insufficient (the tail's backward-continuation need not match the true
early terms) — this approach must use the EXPLICIT finiteness/computability of N₁'
directly (a genuinely different lever), not re-attempt the same abstract injectivity
argument in new words.

---

### Not advanced this round (no new content found, per dispatch instructions)
- **covering-system-construction**: bespoke |F''|=2 explorer found the only fresh
  idea (multi-witness pigeonhole via Singleton-Side FAH's all-occurrences strength)
  collapses into the already-dead Recruitment-Budget mechanism (round 9). No new
  mechanism to dispatch; holding at current Elo/state rather than wasting a build
  slot re-confirming the same wall.
- **subword-complexity-periodicity**: de Bruijn/Morse-Hedlund-corridor explorer
  checked 3 additional combinatorics-on-words refinements (return words/derived
  sequences, full de Bruijn graphs, special-factor counting) and confirmed all
  either collapse into the certified Lemma B/EEA machinery or presuppose FAH before
  any word-complexity tool applies. No new corridor found this round; holding.
