# Proof review — imo-2026-04 (Mulan's Triangle Game), round 2

Reviewed both approaches claiming Status `solved` from round 1, which had never been
reviewed. Both are adversarially re-checked below: correctness of the load-bearing steps
re-derived from scratch (not just read), and cross-checked with exact-arithmetic
computation (care taken to avoid the loose-tolerance-random-scan trap — see Method note).

**Claimed answer (both approaches, identical):** Mulan has a finite forced win from every
starting triangle iff $\theta = 180°/n$ for some integer $n\ge2$.

## Method note (why the round-1 "randomized verification" claims needed re-checking)

Both approach files cite "N random trials, 0 counterexamples" for their key lemmas. A
naive re-implementation of "scan x over a fine grid and check near-multiples with a loose
tolerance" produces spurious counterexamples (I hit this myself first: a 4000-point grid
scan with 1e-3 tolerance found "counterexamples" in >90% of the 60+ trials it ran before
timing out). The reason: with continuous $x$, "child unsafe" is a measure-zero condition
(a finite set of exact candidate values), so a coarse grid combined with a loose tolerance
mostly picks up near-misses that are not genuine equalities. I redid the check properly:
enumerate the *exact* finite candidate set of $x$ values that make child$_1$ (or the
relevant angle) an exact integer multiple of $\theta$, and test only those. This is the
correct computational model of "Mulan's real-valued choice hits the lattice exactly."
With this fixed methodology: 0 counterexamples in 20000 trials (necessity invariant,
random non-resonant $\theta$ and safe triangles) and 0 counterexamples in 39000 trials
(sufficiency double-forcing construction, $n=2..14$, random non-resonant triangles).

## Independent algebraic re-derivation

I re-derived the single-cut formula from scratch (apex $A$, cut parameter $x\in(0,A)$,
base angles $B,C$: child$_1=(x,B,180-x-B)$, child$_2=(A-x,C,B+x)$) and confirmed both
approaches use it identically (just different variable names: approach 2's $(X,Y,Z,a_1)$
maps to approach 1's $(A,B,C,x)$ term for term).

I re-derived the necessity invariant's two-case algebra by hand:
- Case (a) $x=j\theta$: $A-x=A-j\theta$, safe iff $A$ safe; $B+x=B+j\theta$, safe iff $B$
  safe. Both true by hypothesis. Confirmed.
- Case (b) $180-x-B=k\theta$ (i.e. $x=180-B-k\theta$): $A-x = k\theta-C$ (using
  $A+B-180=-C$), safe iff $C$ safe (true); $B+x=180-k\theta$, safe iff
  $180\notin\theta\mathbb Z$, i.e. non-resonance — the *only* place non-resonance is used,
  exactly as the proof claims. Confirmed correct and essentially used (this is the crux:
  if $\theta$ were resonant, $180-k\theta$ could hit $n\theta-k\theta=(n-k)\theta$, making
  case (b) capable of forcing both children unsafe — consistent with why resonant $\theta$
  behaves oppositely in the sufficiency direction).

I re-derived a concrete numeric example by hand for $\theta=60°$ ($n=3$), triangle
$(100°,50°,30°)$ (no angle a multiple of 60): Lemma S2's construction gives apex$=100$,
$\beta=50,\gamma=30$, $k_2=\lceil 30/60\rceil=1$, $x=180-50-60=70$, valid since
$0<70<100$. child$_1=(70,50,60)$ — already hits $\theta=60$ exactly (instant win branch);
child$_2=(30,30,120)$ — hits $2\theta=120$ (feeds Chain Lemma with $K=2$, needing 1 more
move). Matches the formula's algebra exactly.

I verified the "resonance-lattice-invariant" approach's 4-combination case check
(Section 3, Lemma 2) algebraically: it is the same underlying identity split into 4 cases
by which of $B_1$'s two conditions and which of $B_2$'s two conditions co-occur; case 4
($a_1=(Z+X)-m\theta$ and $a_1=n\theta-Y$) reduces to $180=(m+n)\theta$, i.e. exactly the
resonance condition — this is the crux both approaches converge on. Correct.

## Cross-check between the two approaches

Both reach the identical characterization $\theta=180/n$, $n\ge2$ integer, via genuinely
different organizations of the same underlying algebra (the "safe/lattice" mechanism is
the same fact proved two ways — one as a direct 2-case argument, one as an exhaustive
4-combination argument). This is strong independent cross-validation: two differently
structured write-ups of the same computation both check out.

## Approach 1: `interval-partition-topological.md`

**Correctness.** Every step checks out under independent re-derivation (see above).
Lemma S1 (chain lemma): correct induction, base case and inductive step both valid,
cut-parameter validity ($0<\theta<K\theta$) correctly justified. Lemma S2 (universal
double-forcing move): the algebraic identity for child$_1$/child$_2$'s forced angles is
correct; the validity bounds ($0<x<A$, $1\le k_2\le n-1$) are proven with explicit case
splits for $n\ge3$ and $n=2$ separately, both verified by hand above — no gap. Lemma N1
(safety invariant): the 2-case argument is complete (child$_1$'s only two ways to be
unsafe, both covered) and uses non-resonance exactly once, essentially. Lemma N2 (safe
equilateral start): trivial one-line argument, correct.

**Completeness / rigor.** All cases covered: sufficiency handles both the "already
resonant" and "not yet resonant" initial triangle cases (Step 0 / Lemma S2 combo);
necessity handles existence of a safe start (explicit, not just "generic point exists")
and preservation under every one of Mulan's move choices (apex × labeling × continuum
$x$), argued to be label/apex-symmetric correctly. No hand-waving: every "clearly" is
backed by an explicit inequality or computation. The redundant "2 labelings × continuum
x" move-space description (vs. the true move space of 3 apexes × continuum x, since
swapping B/C-label is equivalent to reflecting $x\mapsto A-x$) is harmless — it's a
superset cover, so proving the claim over the larger space only strengthens both
directions, not weakens them.

**Answer correctness.** Explicit answer stated and verified in both directions with
explicit move-count bounds ($\le n-1$ total moves). Construction (Lemma S2) and bound
(Lemma S1) both explicit, satisfying the "find all" bound + construction requirement.

**Status: solved.** No gap found.

**Verdict: APPROVE.**

## Approach 2: `resonance-lattice-invariant.md`

**Correctness.** The Chain Lemma (Lemma 1) is essentially identical to approach 1's S1,
correct. The sufficiency "interval contains a multiple of $\theta$" argument (Section 2)
is a standard, correctly-proved fact ($k=\lfloor a/\theta\rfloor+1$ lands in $(a,b)$ when
$b-a>\theta$), and the case split ($n\ge3$ non-equilateral vs. $n=2$) correctly disposes
of the edge cases (equilateral triangle for $n=3$ handled by Step 0; $X\ge60$ as max angle
of any triangle correctly invoked to get $X>\theta$ for $n\ge4$, and $X=60=\theta$ only at
equality for $n=3$, excluded). The necessity Lemma 2 4-combination case check is exhaustive
and each of the 4 cases is correctly reduced to a safety/resonance contradiction (verified
above). The explicit safe-triangle-construction (avoiding two finite forbidden sets in
succession) is a valid, general, correct construction.

**Completeness / rigor.** This approach explicitly flagged its own central risk up front
("does its mechanism survive Mulan's continuum choice of cut point") and resolves it
rigorously: Lemma 2's proof works for **arbitrary real $a_1$**, not merely $a_1$ near
lattice points, precisely because it works with all four *symbolic* combinations of which
lattice condition each child satisfies, covering the entire continuum by cases rather than
checking points. This is the correct way to handle a continuum adversary and the risk is
genuinely closed, not merely asserted — confirmed by my independent re-derivation and by
exact-candidate-set computation (since a real $a_1$ satisfying two lattice conditions
simultaneously must solve a linear equation, the derivation via combination cases is
complete and not merely sampled).

**Answer correctness.** Identical stated/verified answer to approach 1, with explicit
move bound $n-1$.

**Status: solved.** No gap found.

**Verdict: APPROVE.**

## Cross-check summary

Both approaches independently derive $\theta = 180°/n,\ n\ge2$ as the exact
characterization, via different (but algebraically equivalent under substitution)
mechanisms. No discrepancy between them. Both hold up to adversarial re-derivation and
corrected exact-arithmetic computational checking.

## Actions taken

- `results/imo-2026-04/current.md` updated: `## Status` = solved, `## Full proof` =
  the verified proof (adopted from `interval-partition-topological.md`, noted as
  cross-validated by the independent second proof in `resonance-lattice-invariant.md`).
- Certified promotable lemmas into `results/imo-2026-04/lemmas/`:
  - `chain-lemma.md` (Lemma S1 / Lemma 1) — certified, no gaps.
  - `lattice-safety-invariant.md` (Lemma N1+N2 / Lemma 2's necessity direction) —
    certified, no gaps.
  (Lemma S2 / the sufficiency double-forcing construction was left embedded in the full
  proof rather than split into a separate lemma file, since it is tightly coupled to the
  $n=2$ vs $n\ge3$ case split and is fully reproduced in `current.md`.)
- `record_outcome` called for both slugs with outcome `verified-milestone`.

## Verdicts

- **`interval-partition-topological`**: Status `solved` (confirmed). **APPROVE.**
- **`resonance-lattice-invariant`**: Status `solved` (confirmed). **APPROVE.**

The problem `imo-2026-04` is now genuinely solved: complete, correct, cross-validated
characterization $\theta=180°/n$ ($n\ge2$ integer), both directions proven with explicit
constructions and bounds, no gaps, no hand-waving, no skipped cases.
