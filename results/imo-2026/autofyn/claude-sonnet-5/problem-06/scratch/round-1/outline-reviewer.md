# Outline review — imo-2026-06, round 1

Read: `/tmp/round-1/proof-outliner.md`, `problems.jsonl` entry, `knowledge_base.md`.
`results/imo-2026-06/current.md` and `results/imo-2026-06/approaches/*.md` do **not
yet exist** (empty directory) — the outliner's report was written only to
`/tmp/round-1/proof-outliner.md`; it did not seed the `results/imo-2026-06/approaches/<slug>.md`
files it describes. Per the tool contract ("The outliner seeds the approach's
commentary `results/<id>/approaches/<slug>.md`"), that seeding is still owed —
flagged below so this round's builders (or the outliner next round) create these
files rather than assuming they already exist.

Sanity-checked computationally (python3, `math.gcd` greedy simulation):
- Free Lemma Q verified exactly for a_1 ∈ {4, 8, 9}: sequence is a_1, a_1+p, a_1+2p, ...
  confirming the prime-power base case and its proof (only a_n+p survives the gcd
  test against a_1=p^k). Sound, no issues.
- a_1=21, a_1=55 (two-prime products with a dominant prime power appearing early)
  do collapse to a single-prime pattern (T=1) as approach 2 claims — supports its
  Step 3 "one prime silently absorbs the hub" base case.
- a_1=247=13·19 (the stress test) simulated to 1500 terms: max gap stays at 78
  from term ~50 through term 1500 (encouraging for boundedness), but the set of
  *distinct primes appearing* keeps growing with no sign of leveling off (101
  distinct primes by term 1500, new large primes recruited in every 300-term
  window through the end of the run) — consistent with the outliner's own report
  that 15000 terms did not show visible stabilization. This is genuinely hard;
  I did not attempt to resolve it, only used it to sanity-check the outline's
  claims are not obviously contradicted by data.
- **Found a fatal flaw in `minimal-witness-index-descent`** (detailed below) via
  direct computation on the Tight(n) definition.

---

## backbone-existence-crt — CHANGES REQUESTED

Technique (density-driven prime recruitment + CRT + pigeonhole + Bezout
backward-sharpening) is the right shape for this kind of problem and matches
the standard playbook for "eventually periodic gcd-defined sequence" results.
Case split (|P_1|=1 via Lemma Q, |P_1|≥2 main case) is complete. No circularity.

Issue to fix before/while building:
- **Step 3's mechanism has a real logical gap, not just an unproven inequality.**
  The argument shows "each *individual* old index causes at most one
  recruitment" (once resolved, stays resolved). That bounds recruitments *per
  index*, but it does **not** by itself bound the *total* number of
  recruitments, because as n→∞ infinitely many new indices are created, each
  of which could in principle be the trigger for its own one-time recruitment.
  The outline's own text half-acknowledges this ("the density bound must be
  strong enough to guarantee the unresolved-index set does not grow faster
  than it is resolved") but Step 3 doesn't state what quantity is being
  compared — it needs an explicit inequality of the form "rate at which new
  unresolved indices can appear ≤ rate at which the density bound resolves
  them," with both rates made explicit in terms of |H_n|. Ask the builder to
  either produce that inequality or report precisely why it fails (e.g. an
  a_1=247-scale counterexample to a specific proposed rate bound).
- Step 6 (n=1 sharpening via Bezout/backward propagation) is honestly flagged
  as unexecuted — fine to leave as a gap, but the builder should attempt it
  concretely against crux `aimo-0648`'s device rather than gesture at it again.

Verdict: sound skeleton, hard but honestly-flagged central lemma, real
technique — approved to build, expect `partial` this round.

---

## intersecting-family-covering-construction — CHANGES REQUESTED

Genuinely distinct order of operations from approach 1 (construct-then-verify
vs. prove-existence-then-derive), and its Step 6 correctly notes this sidesteps
the separate n=1-sharpening step needed elsewhere — a real structural
advantage worth preserving in the field. Case split is complete (Lemma Q +
induction on k=|P_1| intended for the main case), and the a_1=21/a_1=55
computational check above supports the claimed "single-prime absorption" base
case for the induction.

Issue to fix:
- Step 3's claim ("if some p∈P_1 is only ever finitely labeled, greedy
  minimality would eventually prefer other primes ... giving a periodic
  sub-pattern with p pruned") is stated as a plausibility argument, not a
  mechanism. As written it doesn't explain *why* greedy minimality would
  produce a *detectable*, provable sub-pattern rather than just an irregular
  tail — this needs the same level of rigor Step 3 in approach 1 is asked for
  (an explicit monovariant or counting argument), not merely "greedy would
  eventually prefer." Flag this to the builder as the load-bearing gap to
  either close or precisely characterize where it breaks.
- Step 4/5 (finiteness of helper set E, invariant preservability) is honestly
  flagged as open — acceptable to leave as a gap for this round.

Verdict: approved — distinct enough mechanism (construction order, avoids
separate backward-sharpening) to be worth a parallel build against approach 1,
even though both ultimately resolve variants of the same backbone-finiteness
fact (per CLAUDE.md, sharing a target lemma via a genuinely different route is
not by itself a reason to cut).

---

## bounded-gap-density-covering — APPROVE (as a fast, cheap test)

This is the one approach that is structurally different in *target*, not just
order: it seeks a generic bound d_n ≤ D(a_1) without ever pinning down which
primes form the backbone. If it closes, it is a strictly shorter, cleaner
proof than the other two; if it fails, it fails cheaply and the outline
already instructs the builder to report the specific failure point (Step 2)
rather than nurse a doomed line — good practice, keep it.

No structural or logical issues found in the skeleton itself (Step 3-4 pigeonhole
+ Bezout sharpening is the same generic machinery used correctly elsewhere).
The self-flagged risk (a covering-density bound proves *some* window contains
an H-divisible integer, but not that it's simultaneously compatible with
*every* earlier term) is exactly right and matches what the a_1=247 empirical
data suggests is the hard part (gaps did stay bounded at 78 through 1500 terms
in my check, which is mildly encouraging, but that's compatible with either a
provable density bound or with a coincidence of small-term data — not
conclusive either way).

Verdict: approved, but expect and accept a fast dead-end report at Step 2 as a
legitimate, valuable outcome this round (not a failure to route around).

---

## minimal-witness-index-descent — RETHINK (cut, do not register)

**Fatal flaw: the central definition (Tight(n)) is vacuous by construction,
and the Step 3→Step 4 inference is a non-sequitur even if it weren't.**

The problem's own defining recursion requires `gcd(a_{n+1}, a_i) > 1` for
*every* `i = 1,...,n`, which includes `i = n` itself. So `gcd(a_n, a_{n+1}) > 1`
holds **automatically, for every n, by definition** — not as a consequence of
any "debt-clearing" behavior. I verified this directly:

```
gen(21, 30): gcd(a_i, a_{i+1}) > 1 for every consecutive pair — trivially true
```

Given `Tight(n) := {i≤n : no prime dividing a_i also divides any a_j with
i<j≤n}`, this means for every `i<n`, taking `j=i+1` (which is always ≤n once
`n≥i+1`) already disqualifies `i` from `Tight(n)`, **regardless of any
structural property of the sequence**. I computed this directly for
`a_1=247` up to n=600: `Tight(n) = {n}` (singleton, just the most recent
index) at *every* single n tested — not because "debt is bounded," but
because the definition can never produce anything else. `Tight(n)`'s
boundedness (Step 3's whole claimed content) is therefore a **content-free
triviality that follows immediately from the problem statement itself**, not
a genuine structural fact requiring greedy-minimality or a monovariant.

Worse, **Step 4 does not follow even granting Step 3**: it claims "the primes
needed at step n+1 come only from `∪_{i∈Tight(n)} primes(a_i) ∪ P_1`." Since
`Tight(n)` is always just `{n}`, this reduces to claiming a_{n+1} only needs
compatibility with `a_n` and `P_1` — but the problem requires compatibility
with **every** `i≤n`, and the fact that some earlier index `i` was "resolved"
by *some* later term `a_j` (`j≤n`, `j` possibly far from `n+1`) says nothing
about whether `a_{n+1}` itself shares any prime with `a_i` — the resolving
prime for `a_i` (shared with `a_j`) need not be a prime of `a_{n+1}` at all.
This is a genuine logical gap connecting two steps, not merely an unproven
plausible claim — the chain "Tight(n) bounded ⇒ finite-modulus reduction"
does not hold as stated.

This is fixable in principle (some other invariant tracking "primes not yet
permanently re-covered" rather than "the literal next successor" might carry
real content), but the approach as outlined does not identify that invariant
and instead builds on a degenerate one. Sending back to the outliner rather
than to the builder: this needs a different definition, not a patch.

**Do not register this slug.** If the outliner wants to salvage the
"elementary index/debt tracking, not primes" framing next round, it must
define the tracked set using *non-adjacent* recurrence (e.g. track, for each
i, whether some prime of a_i divides infinitely many later terms / is
permanently "in the periodic pattern," not merely whether *some* later index
shares a prime with it) and re-derive Step 4's connection from scratch.

---

## Diversity assessment (per CLAUDE.md's single-gap-trap warning)

The outliner's own notes flag that all four approaches converge on one of two
closely-related hard facts. After cutting approach 4 for an independent fatal
flaw, the surviving three do differ in a meaningful way for round 1 (existence
proof vs. explicit construction vs. generic bound without structure
identification), and CLAUDE.md explicitly says sharing a target lemma via
different routes is not itself a reason to cut. That said: **if, next round,
both backbone-existence-crt and intersecting-family-covering-construction
report the exact same stuck inequality (a density/counting bound that won't
close), that is the moment to stop nursing variations and tell the outliner
to open something that attacks periodicity-from-n=1 as its *primary* target
via a wholly different global argument** (the outliner's own suggested
fallback: a self-similarity/symmetry argument sidestepping backbone-finiteness
entirely), rather than a fourth variant of "find the finite backbone." Also
worth reseeding next round: a genuinely different elementary mechanism to
replace the cut minimal-witness-index-descent slot, since 2 of 3 remaining
approaches share the CRT/backbone machinery closely.

## Process note

`results/imo-2026-06/approaches/*.md` and `results/imo-2026-06/current.md` do
not exist yet — builders for the three approved slugs below should create
`approaches/<slug>.md` themselves (seeded from the outline content above) if
the outliner did not do so before their dispatch, since the ranking
registration has already happened without a backing file.

---

build set: backbone-existence-crt, intersecting-family-covering-construction, bounded-gap-density-covering
