## imo-2026-06

- Distinct openings (genuinely far from antichain / monovariant-on-A_n):

  **(1) Double-freeze value-stream monovariant (crux-corpus transplant, NOT an A_n-set statistic).**
  Sister problem `aimo-0678` (ISL N4, "gcd/lcm recurrence eventually periodic") solves an
  eventual-periodicity claim with a two-stage argument that is structurally different from
  everything tried so far: (i) a monovariant `w_n = min{m ≥ a_n : m ∤ s_n}` defined on the
  **actual term value** `a_n` and a frozen auxiliary quantity `s_n` (not on the admissible-set
  `A_n` as a whole), proved non-increasing hence eventually constant `w`; (ii) *given* that
  freeze, a **second, finer invariant** `g_n = gcd(w, s_n)` is proved *exactly* constant
  thereafter by direct algebraic substitution, and periodicity drops out as the finite cycle
  `g+1 → g+2 → … → w → g+1`. The transplantable idea for us is the **shape** of the argument,
  not the formulas: track a monovariant on the *actual chosen values* `a_n` (using the
  greedy/smallest-choice mechanism itself, not the passive constraint-set `A_n`), let it freeze,
  then look for a *second* invariant that becomes exactly constant post-freeze and pins the
  cycle directly — bypassing "prove Π finite" as an explicit intermediate target altogether.
  This is exactly what the certified obstruction lemma (`monovariants-and-obstruction.md`) says
  is missing: "the Crux needs the greedy CHOICE dynamics a_n, not any A_n-set statistic." Nobody
  in the population has yet tried a *value-stream* (as opposed to set-of-A_n) monovariant. Caveat:
  aimo-0678's dynamics (gcd+1, lcm−1) are much simpler/deterministic-state than ours (gcd>1 with
  ALL previous terms, arbitrarily many active constraints), so the transplant is only structural,
  not literal — this is genuinely worth a dedicated approach slot, but is unproven speculation,
  not a working technique yet.

  **(2) Growth/counting bound on when a NEW prime can enter a minimal support, using the greedy
  *choice* directly (not just membership in A).** Since `a_{n+1}` is chosen as the SMALLEST
  admissible integer, a large prime `q` divides `a_{n+1}` "for free" (incidentally) unless it is
  load-bearing. Attempt: show any prime `q` that ever becomes *necessary* (i.e. sits in a
  ⊆-minimal support `G`) must have entered by an index/value bound tied to `a_1`, by using
  minimality directly against the smallest-choice rule at the moment of first necessity, rather
  than working through the abstract E1–E3 machinery. This targets the *same* reduced crux
  (q ≤ a₁) the population already isolated, but via a direct minimality-of-choice argument on
  `a_{n+1} = min{...}` instead of the antichain/transversal formalism — a different proof
  *mechanism* for the same numeric target. Not yet attempted by any approach file.

  **(3) Covering-system framing (evaluated, weaker than expected).** `A = {c : c meets every
  G∈𝓐_∞}` looks like a covering system's complement, but covering-system theory (Erdős,
  minimum modulus, etc.) governs *finite* covering systems of congruences; here the object of
  interest is exactly whether the "moduli" (primes in Π) are finite in number, which is what's
  circular — CRT doesn't supply new leverage until Π is already known finite. This framing
  collapses back to the density monovariant already tried and refuted as insufficient
  (`monovariants-and-obstruction.md` Lemma A). Not a genuinely new route; deprioritize.

- Candidate technique(s): value-stream (choice-level) monovariant à la aimo-0678's `w_n`/`g_n`
  double-freeze pattern (opening 1); direct greedy-minimality argument on first-necessity of a
  prime (opening 2). Both still target essentially the same "why can't Π be infinite" wall, but
  via mechanisms that use the actual `a_n` sequence dynamics instead of set-of-admissible-integers
  statistics — this is the axis the obstruction lemma says is required.

- Cheap-kill candidates: none obvious for finiteness itself (already checked: no A_n-only
  statistic works, certified). One easy sanity/parity check worth keeping in mind: `#𝓐_∞ ≤
  2^{π(a₁)}`-type bound is NOT available since Π may include primes > a₁'s own prime factors
  (e.g. a₁=385 has Π ∋ 19 ∉ primes(385)); no pigeonhole shortcut found.

- Knowledge-base entries to use: (need to check `knowledge_base.md` directly — did not find an
  entry specific to greedy gcd-chain sequences; the closest generic entries are standard
  pigeonhole/CRT/periodicity-of-linear-recurrence type results, none of which resolve the crux
  by themselves per the obstruction already logged.)

- Analogous past problems (cruxes):
  - **`aimo-0678` (ISL N4)** — closest genuine analogue: also proves *eventual periodicity* of
    an integer sequence defined by a gcd-based recurrence, via a two-stage
    monovariant-then-exact-invariant argument on the value stream. Crux move: "construct a
    min-of-a-set integer monovariant that never increases (forcing a freeze), then show a second
    finer invariant becomes exactly constant post-freeze, yielding periodicity directly." Worth
    a dedicated approach attempting the value-stream transplant (opening 1 above).
  - **`aimo-0503` (ISL N3)** — "gcd of consecutive terms bounds the gap from below" — same genre
    (gcd conditions on a sequence forcing growth), but its target is a growth *lower bound*
    (`a_n ≥ 2^n`), not periodicity; the technique (gap ≥ gcd, multiplier bounding) is essentially
    already subsumed by our certified L2/L3 (gap bound, distance–prime). Not a new lead, just
    confirms our free lemmas are the standard toolkit for this genre.
  - **`aimo-0727` (ISL N5)** — sequence with divisibility condition on partial sums, conclusion
    about which primes/moduli eventually divide terms ("if infinitely many primes appear, then
    every n eventually divides some term") — thematically close (primes appearing in a growing
    sequence) but the mechanism (partial-sum divisibility, quotient sequence unbounded) doesn't
    transplant; the conclusion direction is even opposite in spirit (there, infinitude of primes
    is a *hypothesis* driving stronger conclusions; here infinitude of primes in minimal supports
    is the thing to be *refuted*). Read for orientation only, not a crux to reuse.
  - `aimo-0514` ("reversibility ⇒ state graph is union of cycles ⇒ purely periodic") is the
    genre of the already-attempted-and-unsolved `reversible-state-bijection` approach in this
    population (status: unsolved, skeleton, crux gap open) — do not re-suggest without a new
    idea for defining a *finite* state space, since our state space (residues mod the eventual
    L₀) is only finite once Π is already known finite — same circularity as opening (3).

- Prior progress: Whole problem reduced to the single Crux (𝓐_∞ finite / Π finite), sharpened to
  a numerically-tight target: every prime in a ⊆-minimal support is ≤ a₁ (worst ratio 1.0, only
  when a₁ prime). Certified unconditional lemmas E1 (enumeration {a_n}=A∩[a₁,∞)), E2(⇒) (minimal
  supports are ⊆-minimal transversals of themselves), E3 (private-witness distance q ≤ |t−t'|)
  reduce the crux to bounding these witness distances by a₁. All of this stands; my exploration
  did not find a way around needing to close this same numeric target, only alternative *proof
  mechanisms* (value-stream monovariant, direct greedy-minimality) that might reach it without
  going through the antichain/order-theoretic machinery.

- Dead ends (do not retry):
  - Any A_n-set-only statistic (density, max-gap, or any function of the admissible set alone) —
    certified impossible by the concrete obstruction family `{p*, q_k}` in
    `monovariants-and-obstruction.md`. Re-verified by inspection this round; the obstruction proof
    is sound (density → 1/p* without freezing; max-gap freezes but is consistent with infinite Π).
  - M-threshold confinement (`p|L ⇒ p ≤ M=rad(a₁)`) — refuted, a₁=375 has 19|L, 19>15=M. Any
    approach bounding primes by `rad(a₁)` instead of `a₁` itself is dead on arrival.
  - Reversible-state-bijection / covering-system framing as a *standalone* route — both reduce
    circularly to "Π finite" without adding new leverage (state space / modulus is only finite
    once the crux is already granted).

- Small-case / intuition notes (numerical, conjecture only, python simulation this round):
  - Simulated a₁ ∈ {4,6,105,375,385,139,9375,15015} up to 250–400 terms. In every case the
    "last newly-introduced minimal support" (by first-occurrence term value) appeared early,
    at a term value ≤ ~1.8·a₁ in all tested cases (e.g. a₁=385: last new minimal support first
    occurs at a_n=693, ratio 1.80; a₁=15015: ratio 1.05; a₁=139 prime: ratio 1.00). This is
    consistent with — but does NOT prove — the reduced crux q ≤ a₁, and additionally suggests an
    even sharper conjecture: **all minimal supports first appear among terms ≤ C·a₁ for a small
    absolute constant C (empirically C ≈ 2)**, i.e. the alphabet doesn't just have bounded primes
    but stabilizes within an a₁-proportional *window of terms*, not just eventually. This
    "early formation" phrasing might be a more tractable target for opening (2)'s direct greedy-
    minimality argument (bound the term-index of first necessity, not just the prime size) —
    worth flagging to the outliner as a possibly-easier equivalent formulation of the crux.
  - Caveat: these are truncated simulations (finite term windows), so "no new minimal support
    after index X" is only evidence within the simulated range, not a proof that no larger
    minimal support appears arbitrarily far out — the same caveat the existing lemma files already
    carry (worst ratio q/a₁=1.0 observed, not proved).
