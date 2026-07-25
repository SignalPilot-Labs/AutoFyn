# Outline review — imo-2026-06, round 5

Reviewed: `/tmp/round-5/proof-outliner.md` against `results/imo-2026-06/current.md`,
all files in `results/imo-2026-06/approaches/`, `lemmas/`, and `.ranking.json`.
Persistence check passed: all round-5 edits are actually on disk (approach-file
mtimes 01:10–01:13 UTC, before the outliner report's 01:15 mtime) — no repeat
of the round-2 "report-only, never persisted" failure.

## state-compactness-pigeonhole — advance — APPROVE

Target and skeleton are the established, certified Reduction Lemma / Hitting-Set
Lemma machinery (both independently re-verified in prior rounds). The new step 3
target ("redundant-covering density": once a prime's divisibility-index set is
dense enough, every later pair is automatically hit with multiplicity ≥2,
blocking new Nec growth) is honestly stated as **open**, not claimed proved —
good. It correctly cites `chain-transitivity-obstruction.md` as a trap to avoid
(pair-by-pair density argument, not transitive chaining) — this is the right
caveat given that lemma's content.

No fatal flaw. Proceed.

## active-set-stabilization — advance — APPROVE

Same $Q_{\min}$ framing, attacked via a per-term redundancy count $\rho(n) :=
|R(a_n)\cap Q_{\min}|$ rather than the hitting-set reformulation. Correctly
flagged as open (no proof, only numerical support cited). Good discipline:
explicitly splits "primes in $R(a_1)$" (bounded gap, from the certified
`bounded-gap-via-rad-a1.md`) from "recruited primes outside $R(a_1)$" (no a
priori bound — cites the real counterexamples $a_1=375$ recruiting prime 7 at
witness index 26, and $a_1=194287$ recruiting prime 103 > every factor of
$a_1$) and refuses to assume a uniform bound across both. This is exactly the
kind of caveat my rules require (memory rule #5/#7 class of trap) and it is
present, not glossed over.

**Caution to flag for the builder (not a rejection):** $\rho(n)\ge2$
(every *term* carries ≥2 $Q_{\min}$-primes) is not obviously equivalent to
state-compactness-pigeonhole's step-3 target (every *pair* is hit with
multiplicity ≥2) — a term having two $Q_{\min}$-primes does not by itself
guarantee any specific other term shares two of them. This is a real logical
gap inside the "Redundancy Growth Lemma" as stated, not fatal to the outline
(both are honestly labeled open targets, not finished proofs), but the builder
must either close this gap explicitly or restate the lemma so it actually
implies pairwise ≥2-multiplicity — flag this so it isn't silently assumed.

**Diversity note (not a rejection, a process flag):** these two "advance"
approaches are, as the outliner itself diagnoses, variants of one framing and
their round-5 targets (redundant pairwise coverage vs. redundant per-term
count) are closely related mechanisms both aimed at the same "eventual
redundancy ≥2 blocks new Nec growth" idea. If both stall on essentially the
same wall this round, that is strong evidence the "redundancy ≥2" idea itself
needs to be abandoned rather than reframed a third way next round — the
outliner should watch for this specific failure mode.

## renormalization-induction-on-seed — revise — APPROVE

Verified the round-5 diagnosis independently: simulated $a_1=35$ and confirmed
prime 5 does *not* divide every term after index 2 but recurs with a mixed
periodic/near-periodic pattern (div-by-5 indicator over the first 60 terms:
mostly 1, with isolated 0's at scattered positions) — consistent with the
approach's claim that "locked forever" (the old $M=1$ notion) is too strong
and the correct necessary property is "periodically active" (general $M$).
Also independently recomputed $a_1=65$: sequence $65,70,75,78,80,90,\dots$
confirms $a_3=75$ (Third-Term Dichotomy Lemma, matches) and $a_4=78$ (lock
already broken at step 4, since $78 = 2\cdot3\cdot13$ shares no factor of 5
with $a_3=75$'s continuation), exactly as claimed.

**Circularity check (the item flagged by the dispatch): real, and honestly
handled, not hand-waved.** The revision explicitly states step 3 "risks
re-deriving the very same central existence gap ... in different language,
since $M$ is not bounded a priori by anything known about $a_1$ alone" and
instructs the next builder to attack *only* step 2 (periodic activity of a
single prime, independent of already knowing $T$) and not proceed to step 3/4
until step 2 has an unconditional proof. This is the correct response to a
self-admitted circularity risk (my rule: elevate self-flagged circularity to
an explicit gate before later dependent lemmas) — the outline already does
this itself. Approve as written; the builder must not skip past this gate.

The redefinition itself is mathematically sound: "if eventual periodicity
holds with shift $T$, every prime dividing $L$ is periodically active with
$M=T$" follows directly from the definition of periodicity and the certified
`periodicity-of-residue-class-union.md` — a legitimate necessary condition,
unlike the old $M=1$ notion which the $a_1=35$ data actively falsifies.

## scalar-difference-pigeonhole — new — APPROVE

Independently verified the free lemma: $g_n(T) = \sum_{k=0}^{T-1}
(a_{n+k+1}-a_{n+k}) \in [T,TR]$ by telescoping the certified bounded-gap
lemma — correct, and the pigeonhole conclusion (some value recurs on an
infinite index set) is immediate and correctly not overclaimed as more than
that. Independently re-simulated the negative check: $a_1=99$, diffs
$3,3,3,2,4,6,6,6,3,\dots$ — the match value 3 holds for three consecutive
gaps then breaks, confirming "two/three consecutive matches propagate
forever" is false, exactly as the approach states (a real, useful negative
result, not a strawman).

Genuinely orthogonal framing — no primes, no $Q$, no Nec — good plateau-break
candidate per CLAUDE.md's rule. The open target (syndeticity of $Y_{T^\ast}$)
is precisely and honestly stated as unproved, with a correctly-flagged harder
fallback (ISL 2015 N6 sandwich, explicitly noted as requiring a substitute
divisibility fact that does not currently exist for this recurrence — the
approach correctly does NOT claim this substitute fact, unlike a plausible
trap of silently assuming $d\mid a_{n+d}-a_n$). No fatal flaw.

## frozen-invariant-monovariant — new — APPROVE (with the construction still
genuinely unfinished, correctly labeled as such)

This is the second item the dispatch asked me to scrutinize for hand-waving.
Verdict: **honest, not hand-waved.** Section 1 (universally-dividing prime set
$U_n$ stabilizes) is a real, free, fully-proved lemma (finite non-increasing
chain of subsets of $R(a_1)$) — correct and trivial, no issue. Section 2 (the
actual monovariant $w_n(M)$) is explicitly and repeatedly flagged as **not
rigorously specified** ("This is not yet a rigorously specified quantity...
presented here as the concrete next construction to formalize, not as an
established lemma"), with monotonicity explicitly marked "not attempted here,
flagged as the single hardest step," and the same $M$-selection circularity
risk as renormalization-induction-on-seed explicitly called out with two
named candidate resolutions (uniform-over-a-fixed-range vs.
$M$-independent reformulation). This is exactly the right way to present an
unfinished construction: no step claims more than it has, and the "watch out
for" section correctly forbids reducing the exceptional-step classifier to a
bounded window (citing the correct certified negative lemma,
`windowed-epsilon-automaton-failure.md`).

Since §2 is honestly unspecified rather than a completed-but-wrong proof,
there is nothing to reject here — the outline correctly hands the builder a
precise TODO (specify "pattern fails" rigorously; pick a non-circular route
for $M$) rather than a false claim to build on. Approve as a legitimate new
architecture with real free content plus a clearly scoped open problem.

## jacobsthal-covering-bound, bounded-link-invariant, growth-rate-contradiction

Not nominated this round (correctly — each has explicitly reported no
untried mechanism per `current.md`/`.ranking.json`: jacobsthal plateaued 2
rounds with no a priori bound on $K(a_1)$; bounded-link-invariant's central
mechanism proven impossible; growth-rate-contradiction dead-end since round
2). Excluding them from the build set is correct per the "no forward lever"
deprioritization rule (memory rule from round 4 / `run_state.md` Rules).
None are cut from the population (still ranked, still eligible to return if a
genuinely new idea appears).

## Population / ranking action taken

- Registered new approaches `scalar-difference-pigeonhole` and
  `frozen-invariant-monovariant` (both APPROVE, cold-start Elo).
- No branching requested by the outliner this round — no `copy_approach` call.
- Ranked the whole field via `update_ranking` (15 comparisons), anchoring the
  two newcomers against both the strongest live approaches and the
  established dead/plateaued ones (per the "don't compare newcomers only to
  each other" rule), and gave state-compactness-pigeonhole vs
  active-set-stabilization a draw since both received equally strong,
  equally-unproven "advance" outlines this round. Post-update Elo (best
  first): state-compactness-pigeonhole ~1622, active-set-stabilization
  ~1599, scalar-difference-pigeonhole ~1534, renormalization-induction-on-seed
  ~1527, frozen-invariant-monovariant ~1492, bounded-link-invariant ~1430,
  jacobsthal-covering-bound ~1406, growth-rate-contradiction ~1390.

## Summary verdicts

| slug | verdict |
|---|---|
| state-compactness-pigeonhole | APPROVE |
| active-set-stabilization | APPROVE (flag: verify $\rho(n)\ge2$ actually implies pairwise multiplicity ≥2, don't assume it) |
| renormalization-induction-on-seed | APPROVE (circularity gate is real, self-flagged, correctly gated — builder must not skip past step 2 to step 3/4) |
| scalar-difference-pigeonhole | APPROVE |
| frozen-invariant-monovariant | APPROVE (construction honestly unfinished — builder's job is to make §2 rigorous, not assume it works) |

All five approaches reviewed pass the outline gate: right techniques for
their respective framings, no circular reasoning slipped through as settled,
no missing cases (none of these outlines has reached a case-split yet), and
every open lemma is labeled with its actual mechanism (or explicitly labeled
unspecified) rather than hidden behind "then it follows." This is a genuine
plateau-break round per CLAUDE.md: 2 approaches advance the dominant framing,
1 is revised onto a non-circular target, and 2 open architectures (scalar
arithmetic, monovariant descent) that touch none of the $Q$/Nec machinery.

build set: state-compactness-pigeonhole, active-set-stabilization, renormalization-induction-on-seed, scalar-difference-pigeonhole, frozen-invariant-monovariant
