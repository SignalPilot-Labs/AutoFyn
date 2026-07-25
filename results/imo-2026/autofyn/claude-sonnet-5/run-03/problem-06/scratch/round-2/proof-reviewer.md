# Proof review — imo-2026-06, round 2

Reviewed independently:
1. `results/imo-2026-06/approaches/jacobsthal-covering-bound.md`
2. `results/imo-2026-06/approaches/active-set-stabilization.md`
3. `results/imo-2026-06/approaches/state-compactness-pigeonhole.md`

Method: re-derived the load-bearing claim of each file from scratch and
cross-checked with independent Python simulation of the actual greedy
sequence (`gcd`-based greedy construction for $a_1 \in \{15,35,105\}$, up to
700 terms), plus a 200-trial randomized computational check of the general
combinatorial lemma (Lemma P) and a direct max-gap computation for the
$g(Q)$ example. All numeric/example claims in all three files check out
exactly as stated; no arithmetic or example error was found in any of them.

## 1. jacobsthal-covering-bound.md

**Verdict: CHANGES REQUESTED. Status: partial (self-report correct).**

Content verified:
- The concrete counterexample ($a_1=35$: $a_1,a_2,a_3,a_4 = 35,40,42,45$,
  $\gcd(42,35)=7$, $\gcd(42,40)=2$, $2\notin\{5,7\}$) is exactly reproduced
  by direct simulation. The conclusion drawn — "membership in $H(Q)$ is not
  a valid safety certificate; only multiples of $L_Q$ are" — is correct and
  is a genuine (if modest) negative result. The $g(P)=5$ computation for
  $Q=\{5,7\}$ was independently recomputed (max gap in $H(\{5,7\})$ over one
  period is indeed 5) and matches.
- Section 2's claim that $P=R(a_1)$ already covers the full history forever
  is correct but is a re-derivation of content already inside the certified
  `lemmas/bounded-gap-via-rad-a1.md` (its internal "Fact"). Not new, though
  legitimately used here to make a fresh point (the phase-induction's
  intended trigger for enlarging $Q$ never fires).
- No termination bound / monovariant for the central self-sufficiency gap is
  produced. The file itself is explicit and honest about this — it correctly
  reports **partial**, not solved, and does not overclaim. The "dead-end"
  framing (ruling out $g(Q)$-threshold and prime-size-threshold mechanisms)
  is itself correctly proved, not merely asserted — this is real, if
  negative, progress: it forecloses two specific natural mechanisms so the
  next round does not retry them.

Gap that remains, precisely: no argument (in this file or elsewhere in the
population) bounds how long or how far "minimality-driven" recruitment of
primes outside a growing $Q$ can continue. This is the single missing
ingredient for Hypothesis SS.

## 2. active-set-stabilization.md

**Verdict: CHANGES REQUESTED. Status: partial (self-report correct).**

Content verified:
- Theorem A (eventual periodicity given Hypothesis SS): re-checked the
  proof line by line. The pigeonhole step is now correctly scoped — it only
  claims existence of *some* coincident pair $(p,q)$ with $p<q\ge n_1$, and
  the induction step $r_{p+j+1}=g(r_{p+j})=g(r_{q+j})=r_{q+j+1}$ is valid
  because $g$ is a genuine function of the residue alone (justified earlier
  via CRT). This is a correct fix of the round-1 fallacy; no residual
  circularity or fallacy found.
- The Monotonicity Obstruction Lemma: this is a completely elementary and
  correct fact (if $\mathcal T_1 \subsetneq \mathcal T$ and $\mathcal T_n$ is
  $\subseteq$-monotone, then $\mathcal T_1 \ne \mathcal T_m$ whenever
  $\mathcal T_m = \mathcal T$ — immediate from $\mathcal T_1 \subseteq
  \mathcal T_m$). It is correctly scoped as ruling out only the
  *state-recurrence* family of fixes, not the underlying periodicity claim
  itself, and the file is careful to note (with a verified numerical
  example) that the target conclusion is nonetheless true. This is a
  legitimate, general, reusable negative lemma — certified.
- Lemma T (translation compatibility) and Lemma M (minimal-type reduction):
  both re-derived independently by hand; both correct, both elementary and
  general-purpose. Certified, each with a caveat that neither alone closes
  the prefix-extension gap (the file itself documents this honestly with
  worked-example residual gaps, e.g. Lemma M closes $5\to3$ but not
  $3\to1$).
- Numerical claim ($a_1=15$, $T=8$, $L=30$, holds from $n=1$ for 592 checked
  pairs): independently reproduced via simulation up to 700 terms; the
  minimal working period is indeed $T=8,L=30$ and holds from $n=1$ with no
  exceptions found in the checked range.

No error found. The file correctly identifies both gaps (central,
untouched by design/division-of-labor; secondary, narrowed but not closed)
and does not overclaim.

## 3. state-compactness-pigeonhole.md

**Verdict: CHANGES REQUESTED. Status: partial (self-report correct).**

Content verified:
- Proposition B (static reformulation of greedy acceptance): both
  directions re-checked by hand. The ($\Leftarrow$) direction's use of
  "largest $n$ with $a_n<m$" and the subsequent minimality contradiction
  argument is correct and non-circular (it does not assume periodicity or
  any unproved hypothesis — only monotonicity of $(a_n)$, which is
  certified). This is a genuinely new, clean, reusable static
  characterization. Certified.
- Lemma P (exact periodicity of a listed union of residue classes mod $L$):
  re-derived the bijection argument by hand (translation-by-$L$ map $C\to
  C'$, order-preserving, bijective, base case + induction) — correct. Also
  independently stress-tested computationally: 200 randomized trials over
  $(L, \text{GoodRes}, c)$ all confirm $c_{j+T}=c_j+L$ for every checked $j$
  with no counterexample. This is a strong, general, unconditional
  combinatorial fact, strictly cleaner than an orbit-pigeonhole telescoping
  argument. Certified.
- The conditional Theorem of §5 (periodicity of the tail given Hypothesis
  SS) is correctly derived from Proposition B + Lemma P, and is consistent
  with (proves the same conclusion as) active-set-stabilization's
  independent Theorem A — good cross-check, not double-counted as
  independent resolution (the file itself says so explicitly, correctly).
- The rejected fix for Gap 2 ("run the stabilized rule $b_n$ from the
  start") — the argument that $(b_n)$ and $(a_n)$ can genuinely diverge for
  small $n$ because the true early candidate set is a strict superset of the
  $Q$-Good candidate set — is correct reasoning (the true rule before
  stabilization is provably weaker/different, so no a priori reason for
  $a_n=b_n$). Correctly recorded as a negative finding, not glossed over.

No error found. Central gap (Hypothesis SS) and secondary gap (prefix
extension) both remain honestly open.

## Cross-approach consistency check

All three approaches, working independently, agree on:
(a) the round-1 target "$S$ finite" is refuted (a necessary-condition
derivation showing $S$ must be cofinite in the primes if the target
conclusion holds) — re-verified the algebra of this derivation myself
(residue-class invertibility argument mod $p$ for $p \nmid L$) and it is
correct;
(b) $Q_0 = R(a_1)$ is an unconditional (pigeonhole-free) finite covering
set, sharper than the round-1 $S$-covering lemma;
(c) two independent conditional derivations of tail-periodicity (orbit
pigeonhole vs. residue-class-union) agree exactly;
(d) the prefix-extension gap is real and at least one entire family of naive
fixes (state-pigeonhole) is now provably ruled out.
This convergence from three structurally different framings increases
confidence that the diagnosis (central gap = Hypothesis SS; secondary gap =
prefix extension) is the correct remaining target, not an artifact of one
approach's specific machinery.

## Lemmas certified this round

Written to `results/imo-2026-06/lemmas/`:
- `prime-factors-a1-cover-forever.md` — unconditional, standalone extraction
  of the "$P=R(a_1)$ covers every term" fact (previously only inline inside
  `bounded-gap-via-rad-a1.md`), with caveat.
- `covering-membership-not-safety-certificate.md` — negative result from
  jacobsthal-covering-bound, with caveat that it is negative-only.
- `monotonicity-obstruction.md` — from active-set-stabilization, general,
  unconditional, with caveat on scope.
- `translation-compatibility.md` — from active-set-stabilization,
  unconditional, with caveat (sufficient but not necessary condition).
- `minimal-type-reduction.md` — from active-set-stabilization, unconditional,
  with caveat on residual scope.
- `set-theoretic-acceptance-characterization.md` (Proposition B) — from
  state-compactness-pigeonhole, unconditional.
- `periodicity-of-residue-class-union.md` (Lemma P) — from
  state-compactness-pigeonhole, unconditional, computationally re-verified.
- `eventual-periodicity-given-hypothesis-ss.md` — a single canonical
  **conditional** lemma citing both active-set-stabilization's Theorem A and
  state-compactness-pigeonhole's Section-5 theorem as independent,
  cross-checked derivations of the same conditional statement (explicitly
  labeled conditional on the unproved Hypothesis SS, per the "never promote
  without caveat" rule; not to be cited as closing any part of the problem).

No lemma was rejected outright this round; each was either genuinely new and
correct, or (in the covering-by-$P$ case) a useful standalone extraction of
an already-certified fact, certified as its own file to avoid future
approaches re-deriving it inline.

## Overall round assessment

All three built approaches: **CHANGES REQUESTED** (Status: partial, matching
each builder's own self-report — no overclaiming detected, no downgrade
needed). None is RETHINK — all three are legitimate, correctly-scoped
reductions to the same well-defined open gaps (central: Hypothesis SS;
secondary: prefix extension), and each closed off at least one specific
negative-result mechanism this round rather than merely restating open
questions. `results/imo-2026-06/current.md` has been updated accordingly
(Status remains `partial`, with an updated `Approaches tried` log and
`Current best` section reflecting this round's confirmed negative results
and the sharpened central/secondary gap statements).

No approach reached `solved`; the run's goal (a complete rigorous proof) is
not yet met. The central open gap — Hypothesis SS / self-sufficiency of a
finite active prime set, with greedy minimality as the essential missing
ingredient — is now more sharply constrained than at the start of the round
(two more candidate mechanisms proven unsound), and the secondary gap
(prefix extension) likewise (one more candidate mechanism, plus a whole
family via the Monotonicity Obstruction Lemma, proven incapable).

Files touched:
- `/home/agentuser/repo/results/imo-2026-06/current.md` (updated)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/prime-factors-a1-cover-forever.md` (new)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/covering-membership-not-safety-certificate.md` (new)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/monotonicity-obstruction.md` (new)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/translation-compatibility.md` (new)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/minimal-type-reduction.md` (new)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/set-theoretic-acceptance-characterization.md` (new)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/periodicity-of-residue-class-union.md` (new)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/eventual-periodicity-given-hypothesis-ss.md` (new, conditional)
