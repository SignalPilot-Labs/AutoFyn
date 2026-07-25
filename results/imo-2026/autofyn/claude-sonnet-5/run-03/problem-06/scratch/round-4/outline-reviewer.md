# Outline review — round 4 — imo-2026-06

Reviewed: `/tmp/round-4/proof-outliner.md`, `results/imo-2026-06/current.md`, all
`approaches/*.md` (focused on state-compactness-pigeonhole.md §10,
jacobsthal-covering-bound.md §7, active-set-stabilization.md's new Sperner
section, renormalization-induction-on-seed.md), and relevant `lemmas/*.md`
(adjacent-link-lemma, lambda-stabilization). Numerically verified several
claims by simulation (python3, gcd-based greedy generation, sympy
primefactors) rather than taking the outline's assertions at face value.

## 1. state-compactness-pigeonhole §10 — Hitting-Set Lemma

**Verdict: sound, not circular, but zero new leverage on the actual gap
(honestly labeled as such).**

Checked the proof by hand: "Unified Central Claim for Q" unwinds to
"$\tau_n\cap\tau_j\ne\emptyset$ for all $n,j$" which unwinds to
"$Q\cap R(a_n)\cap R(a_j)\ne\emptyset$" which unwinds to "$Q\cap
W(n,j)\ne\emptyset$" — literally the same three-line chain of definitional
substitutions in both directions, no hidden appeal to $L$ or to the
still-unknown periodic tail. **Not circular**: $Q$ is not used to *define*
$L$ inside this lemma's own proof; $L=L(Q)$ only appears afterward, in §4,
as a derived quantity of a *given* $Q$. So this is exactly what the outline
itself says it is — a pure reformulation, not a new proof of anything. The
"free partial coverage" corollary ($Q_0$ hits every $W(1,j)$) is likewise
just a restatement of the already-certified Lemma $Q_0$/Corollary of §9.2,
correctly flagged as recovering existing content, not new content.

The incremental-recruitment construction (§10.2) is honestly flagged as an
**open, unproved** termination question — good, no overclaiming. One thing
to tighten for the builder: the "genuine (partial) monotonicity fact" (set
of unhit pairs is monotone non-increasing) is trivial and adds nothing
toward a bound on $K$; the outline already says this ("gives no bound on
$K$"), so no correction needed, but flag to the builder not to spend time
polishing it further — the only live target is the self-referential bound
in the last bullet, which remains just as hard as the original gap. This is
CHANGES REQUESTED only in the trivial sense that the central gap is still
open; the outline itself is sound and should proceed.

## 2. jacobsthal-covering-bound §7 — "cheap numerical kill-check" on $\Lambda$

**Verdict: the check was NOT run (correctly, honestly flagged as "do this
first, before any proof attempt" — a to-do, not a claim of completion). I
ran it. Result: the literal candidate as stated FAILS, and a natural
correction ALSO fails on one of the outline's own three proposed test
instances.** This is real, decisive information the outliner should have
caught before handing this to a builder, so I'm flagging it now to save a
build cycle.

Two concrete problems, both numerically verified (python3, `sympy.primefactors`,
exact greedy simulation, 150–250 terms):

- **(a) "$Q:=\Lambda$" (literally, no enlargement) is not even a legal
  candidate under the population's own standing convention $Q\supseteq
  Q_0=R(a_1)$.** Checked for $a_1\in\{15,21,35,65,77,99,33\}$: in *every*
  instance, $Q_0\not\subseteq\Lambda$ (e.g. $a_1=35$: $Q_0=\{5,7\}$,
  $\Lambda=\{2,3,5\}$ — $7\notin\Lambda$). Consequently $\Lambda$ alone
  fails as a hitting set immediately and for a trivial reason: pairs like
  $(a_1,a_3)$ for $a_1=35$ share only prime $7$, and $7\notin\Lambda$. This
  isn't the "hard" open question the outline is trying to isolate — it's an
  artifact of not unioning in $Q_0$, which every other part of the
  population's machinery assumes is present.
- **(b) The natural fix, $Q:=\Lambda\cup Q_0$, works for $a_1=35$ and
  $a_1=65$ but FAILS for $a_1=99$** — one of the outline's own three named
  test instances. Exhaustive check over the first 150 terms of $a_1=99$
  finds 105 pairs sharing only prime $5$, and $5\notin\Lambda\cup Q_0=
  \{2,3,11\}$ for that instance (the true eventual period recruits $5$ from
  neither the seed nor any *adjacent*-pair link). This is a genuine,
  reproducible counterexample, not a fluke of transient behavior — the bad
  pairs continue well past term 100.

**Required change:** tell the builder (i) the candidate must be
$\Lambda\cup Q_0$, not $\Lambda$ alone, to even respect the population's
$Q\supseteq Q_0$ convention; (ii) do not spend a build cycle "discovering"
that this candidate already fails at $a_1=99$ — record it as a fact
established by this review and move straight to the outline's own fallback
sub-case 2 (bounded enlargement $\Lambda^{(2)},\Lambda^{(k)}$, i.e. link
primes for gap-2, gap-3, ... pairs, testing whether $a_1=99$'s missing
prime $5$ shows up in $\Lambda^{(2)}$ and whether the enlarged family stays
inside a fixed universe). If a modest bounded enlargement also fails to
capture prime $5$ for $a_1=99$, this whole $\Lambda$-based mechanism should
be reported as dead (a fourth failed mechanism for this approach), not
patched indefinitely. This is CHANGES REQUESTED, not RETHINK — the general
Λ-candidate-testing idea is still a legitimate methodology and the fallback
path is untested, but the builder must start from the corrected/falsified
premise above, not redo the naive check.

## 3. active-set-stabilization — Sperner/antichain argument

**Verdict: sound, honestly one-directional, NOT a repeat of the rounds
2–3 "counting implies termination" fallacy.**

The argument only uses Sperner's theorem for an *upper* bound on
$|\mathcal T^\ast(Q)|$ given $|Q|$ — it does not claim this upper bound, by
itself, forces termination of recruitment. The outline explicitly states
the missing piece ("the converse direction ... is what is needed to turn
this into a termination argument, and is **not yet established**") and
frames the exchange argument (does each recruitment step strictly grow the
antichain?) as the first thing to check computationally, with an explicit
instruction that if the antichain does not strictly grow at every step,
"this mechanism needs a different invariant or is dead." This is exactly
the right epistemic posture — no unjustified leap from "the codomain is
bounded" to "the process terminates." Distinct in mechanism from
state-compactness's recruitment-order construction and jacobsthal's
$\Lambda$-candidate testing, as claimed. APPROVE as stated; the open
exchange-argument check should be the builder's first move, exactly as the
outline says.

## 4. renormalization-induction-on-seed — new approach

**Verdict: base case verified correct (independently, numerically);
inductive step honestly open, not silently assuming the conclusion.**

Independently simulated the greedy sequence for $a_1\in\{4,8,9,16,25,27,
32,49,81\}$ (a spread of prime powers, even and odd): every instance gives
constant increments equal to the prime, matching $T=1,L=p$ exactly as
claimed. The proof itself (§3) is a clean two-part induction (candidates
strictly between consecutive multiples of $p$ are never valid; the next
multiple of $p$ always is) with no gap and no appeal to unproved machinery.

The inductive step is correctly and non-circularly flagged as open: the
naive "lock $\min R(a_1)$ and induct on $\omega(a_1)$" idea is refuted with
a genuine counterexample ($a_1=35$: eventual $L=210=2\cdot3\cdot5\cdot7$
recruits primes 2,3 not in $R(a_1)=\{5,7\}$ at all, so no renormalization
by removing an existing prime can produce them) — this is exactly the same
recruitment phenomenon the $Q$-machinery approaches are fighting, correctly
identified as such rather than hidden. No step in §3 or §4 assumes
periodicity or the existence of $L$/$Q$ in order to derive them (checked
line by line — the base case proof uses only Lemma 0 and the raw greedy
rule; the inductive-step discussion is explicitly hypothetical/refuted, not
used as a premise anywhere). This is a genuinely different top-level
architecture (whole-attempt induction on the seed, not another $Q$/Good_Q
variant), satisfying the plateau-break requirement. APPROVE, register.

## Field diversity

Three approaches (state-compactness-pigeonhole, jacobsthal-covering-bound,
active-set-stabilization) still target the Unified Central Claim, but via
three genuinely different combinatorial devices this round (hitting-set
reformulation + recruitment-order construction; concrete finite-candidate
testing; antichain/Sperner sizing) — legitimate per the population's own
"attack the shared hard lemma via different mechanisms" allowance, not a
single-framing collapse. renormalization-induction-on-seed is a structurally
distinct fourth line. No sibling-slug fragmentation detected — each
approach file targets the full problem end to end (existence of $T,L$),
not a sub-lemma in isolation.

## No approach is doomed / fatally circular

Nothing here rises to RETHINK. The Hitting-Set Lemma is a correct, sound
reformulation (not circular). The Sperner argument correctly avoids the
counting-implies-termination trap. The renormalization base case is
correct. jacobsthal's §7 candidate fails as literally stated, but the
underlying methodology (test concrete finite candidates via the Hitting-Set
Lemma) is still legitimate and has an untested fallback — CHANGES REQUESTED
with the corrected/falsified starting point documented above, not RETHINK.

## Ranking

Registered `renormalization-induction-on-seed` (cold start). Ran
`update_ranking` anchoring the newcomer against all three established
approaches, and re-ranked the established three against each other based on
this round's verified contributions: state-compactness-pigeonhole's fully
proved Hitting-Set Lemma (real, if inert, new content) edges out
active-set-stabilization's honest-but-not-yet-actionable Sperner upper
bound, both clearly ahead of jacobsthal-covering-bound (whose round-4
candidate mechanism is now shown, by this review's own numerical check, to
fail on one of its own three test instances). Resulting Elo: state-
compactness-pigeonhole ~1606 (highest), active-set-stabilization ~1571,
renormalization-induction-on-seed ~1489 (new, anchored below the two
mature leaders but above jacobsthal this round), jacobsthal-covering-bound
~1450 (three rounds, no monovariant, round-4 candidate already falsified).
`bounded-link-invariant` and `growth-rate-contradiction` untouched this
round per the outliner's own deprioritization (mechanism dead, no new
content proposed) — left live in the ranker but excluded from comparisons
since no new evidence arrived for either this round.

build set: state-compactness-pigeonhole, active-set-stabilization, jacobsthal-covering-bound, renormalization-induction-on-seed
