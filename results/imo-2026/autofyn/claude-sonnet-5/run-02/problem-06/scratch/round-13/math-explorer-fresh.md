## imo-2026-06

### Framing of this report
Dispatched as the mandatory plateau-break lens: attack the WHOLE problem fresh,
using only Free Facts, Bounded Gap Lemma, and Finite Core Theorem as given, and
actively avoiding the type/witness/rogue-pair/recruitment vocabulary that all 14
dead FAH mechanisms and the Morse-Hedlund corridor share. I did not attempt a
full proof. Below are genuinely new top-level angles, a concrete negative fact
worth banking, and an honest risk assessment of each new angle (all of them are
speculative — none has been checked to actually close the gap).

### Distinct openings

**1. Idempotent-ultrafilter / Stone–Čech (βℕ) recurrence, à la Hindman/Central
Sets Theorem — genuinely untried toolkit, not in knowledge_base.md.**
Q = P(a_1) is finite. For n ≥ 2, gcd(a_n,a_1) > 1 means some p ∈ Q divides a_n,
so {A_p := {n : p | a_n}}_{p∈Q} covers ℕ. Any nonprincipal ultrafilter U on ℕ
must contain one fixed A_{p0} (finite union covering ℕ, ultrafilters are
closed under finite unions/complements) — this reproduces "some prime of Q
recurs on a U-large set" without any explicit pigeonhole bookkeeping, and
generalizes verbatim to any finite alphabet S₀ (recovering the certified
Extended Persistent-Type Pigeonhole for free, in different language). The
reason this MIGHT be more than a repackaging: idempotent ultrafilters (Galvin–
Glazer / the algebraic structure of (βℕ,+) or of a semigroup built from the
"prime-recruitment" operation) give combinatorially much richer recurrence
than plain pigeonhole — e.g. Hindman's theorem / IP-sets / the Central Sets
Theorem produce simultaneous, "polynomial-shift-stable" recurrence for
*infinitely many* structured index sets at once, not just one infinite set.
This MIGHT let one show a stronger-than-cofinite form of recurrence for the
Lemma-G prime q (e.g. q divides a_n along an IP-set of shifts relative to
n_B, not just infinitely many n) in one clean non-constructive stroke, instead
of the case-by-case "existential-to-universal" bookkeeping that has now failed
14 times.
- **Where it likely breaks:** IP/syndetic/central-set recurrence is still an
  "infinitely many / densely many" statement, not "every single one" — the
  same existential vs. universal gap that Lemma H, the Successor Claim, and
  EEA all hit. Nothing about idempotent ultrafilters intrinsically upgrades
  "recurs on a rich set" to "recurs on every occurrence." It would need to be
  combined with a genuinely NEW ingredient (see below) to close the actual
  gap, not just restate it more abstractly. Also: this toolkit is absent from
  knowledge_base.md and the crux corpus almost certainly has no matching
  entry (Olympiad-style, not ultrafilter-style) — high risk of being a dead
  end that costs a full round just to set up the machinery before hitting the
  same wall.

**2. p-adic / profinite limit argument on the indicator sequence.**
Fix a prime p. The sequence of p-adic valuations v_p(a_n) (or just the
indicator [p | a_n]) lives in a compact space ({0,1}^ℕ under the product
topology, or ℤ_p under p-adic limits along a subsequence). Take a
subsequential limit of the empirical "type profile" as n → ∞ along a
non-principal ultrafilter or a diagonal compactness argument over the (Q ∪ S)-
level finite alphabet; this recovers the same "eventual finite type" picture
the Finite Core Theorem already gives unconditionally, so this angle by itself
is NOT new content — it is a topological restatement of already-certified
Persistent-Type Pigeonhole. **Assessment: this angle collapses into machinery
already fully proved; not worth a round's build effort on its own.** I flag it
only to warn the outliner it will look tempting but adds nothing beyond what
is already certified.

**3. A structural negative fact worth banking: "restart-at-a-later-index"
inductions are invalid, concretely verified.**
Every induction/well-ordering attempt so far (rounds 3, 5, 8's seed-coupling)
implicitly or explicitly treats a later term a_{n0} as if it could seed an
independent instance of the same greedy process. This is FALSE, and I checked
it concretely: for a_1 = 15, the true sequence is
15,18,20,24,30,36,40,42,45,48,50,54,60,66,70,72,75,78,80,84,...
Taking a_5 = 30 as a *fresh* seed a_1' := 30 and running the SAME greedy rule
from scratch gives 30,32,34,36,38,40,42,44,46,48,... — completely different
from the true continuation 30,36,40,42,45,48,50,54,60,66,... (already at the
very next term: true a_6=36, restarted "a_2"=32). The reason: legality of
a_{n+1} depends on gcd > 1 against ALL of a_1,...,a_n, not just the tail from
n0 on; a fresh seed only imposes the constraint against itself, so it accepts
many candidates (e.g. 32, sharing only factor 2 with 30) that the true
process would reject because they fail against some earlier term (e.g. 18,
20, or 45, which the true process must also satisfy). **Conclusion: any
approach that reduces the general case to a smaller instance by "restarting"
at a later index is unsound as stated and should be rejected on sight** unless
it explicitly re-derives and carries forward the FULL history's constraint set
(not just the tail), in which case it is no longer actually a smaller
instance of the same problem. This has not been explicitly flagged this
sharply/concretely before in current.md (round 8's seed-coupling-induction was
falsified empirically on its own specific "Seed-Coupling Lemma," not on this
more general structural reason) — worth citing to kill any future revival of
that whole induction family faster.

**4. Reframe as Hall's-theorem / SDR existence, but on the FULL infinite
history rather than a finite core (a genuinely different bookkeeping unit).**
Legality of m as a_{n+1} is exactly: the bipartite graph with left vertices
{a_1,...,a_n} and right vertices P(m) has a system where every left vertex is
adjacent (via shared divisibility) to some right vertex — i.e. P(m) is a
transversal/hitting set, checkable via Hall's condition on the "co-graph."
This is the same content as the already-explored (and stale, effectively
subsumed) `hypergraph-transversal` approach; I confirm on rereading it that
its Step 3 gap ("finiteness of the eventual minimal antichain's prime
support") is EXACTLY the FAH-equivalent crux again, just phrased in extremal
set theory language. **Not a new opening — flagging so the outliner does not
waste a round rediscovering this equivalence.**

### Candidate technique(s)
Idempotent ultrafilters / Hindman-style combinatorics (opening 1) is the one
genuinely new toolkit surfaced this round. Everything else surveyed either
collapses into already-certified machinery (opening 2, opening 4) or is a
negative/pruning fact (opening 3), not a new attack surface.

### Cheap-kill candidates
- Before investing in ultrafilter machinery: check whether "IP-set / central
  set" recurrence, once unpacked concretely for THIS problem's specific
  covering structure, reduces to literally the same disjunction the certified
  Generalized Bounded Witness Lemma already gives (some prime of a finite set
  recurs richly) — if so it is a relabeling, not new content, and should be
  abandoned in under a page of work rather than built out in full.
- Parity/size check on opening 3: this is now a proved (by explicit
  computation) structural fact, cheap to re-verify on any seed in under 5
  lines of Python; recommend certifying it as a short lemma ("No-Restart
  Lemma" / "History-Dependence Lemma") so no future round re-attempts a
  restart-based induction without re-deriving this from scratch.

### Knowledge-base entries to use
`knowledge_base.md`'s **Hall's marriage theorem / SDR** (Combinatorics
section) is the natural home for opening 4 (already subsumed/dead, so no
action needed beyond noting the equivalence). **Pigeonhole / extremal
principle** and **Invariants & monovariants** (Combinatorics section) are the
generic tools underlying essentially every one of the 14 dead mechanisms —
any NEW mechanism should explicitly explain what it does beyond these two
already-exhausted entries. No KB entry currently corresponds to
ultrafilter/idempotent-semigroup methods (opening 1) — if the outliner wants
to pursue it, it will need to be developed essentially from scratch, which is
a real cost to weigh against its speculative payoff.

### Analogous past problems (cruxes)
I did not run a fresh corpus query this round (dispatch instructions
prioritized fresh top-level strategy over corpus retrieval, and the workspace
records — round 8 through round 12 — already document an exhaustive corpus
search for "eventually periodic greedy sequence" analogues with no direct
structural match found). I have no new candidate to add; deferring to the
existing exhaustive-search conclusion already on file rather than re-running
a search that has been reported to come up empty in prior rounds.

### Prior progress
Unchanged from current.md: Free Facts, Bounded Gap Lemma, Generalized Bounded
Gap Lemma, Persistent-Type Pigeonhole, Bounded/Generalized Bounded Witness
Lemma, Finite Core Theorem, the |Q|=1 special case (fully solved), the
Canonical-Refinement / F_A∩F_B≠∅ lemmas, and (round 12) the Gap-Periodicity
Equivalence and EEA-implies-periodicity theorems are all certified and
unconditional. The single open crux (FAH / Symmetric FAH / equivalently EEA at
some finite core) remains open after 14 confirmed-dead mechanisms across 7
rounds. I did not close it and do not believe opening 1 closes it either
without further genuinely new input (see risk note above) — I am reporting it
as unexplored terrain, not a solution.

### Dead ends (do not retry)
All 14 previously-confirmed-dead FAH mechanisms (existential/pigeonhole,
magnitude-sandwich, tautological-minimality, CRT-glue/competitor-construction,
sieve/density, automaton/graph-walk, Morse-Hedlund/subword-complexity) — see
current.md for the full list; I did not find a way around any of them this
round. Additionally, confirmed and sharpened this round: any "restart the
greedy process at a later index a_{n0} as a fresh seed" induction (implicitly
used in flavor by rounds 3/5's well-ordering attempts and explicitly by round
8's seed-coupling-induction) is structurally unsound — concrete
counterexample above (a_1=15, restart at a_5=30 diverges from the true
sequence at the very next term).

### Small-case / intuition notes
- Conjecture (extensively tested by prior rounds, not by me this round): FAH
  holds literally (0 counterexamples across dozens of seeds and ~90 rogue-pair
  records). My contribution here is not new empirical support but a caution
  that any new mechanism must supply genuinely new information connecting
  DIFFERENT occurrences' legality-critical primes — ultrafilter/idempotent
  methods are a candidate SOURCE of such new information (via structured,
  simultaneous recurrence rather than one-at-a-time pigeonhole) but this is
  conjectural; I have not verified it actually delivers the needed universal
  (not just dense) conclusion.
- The restart-invalidity fact (opening 3) is proved outright (not
  conjectural) by the direct computation shown above.
