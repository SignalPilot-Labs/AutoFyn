## Status
partial

## Round 11 field of rival approaches for the outline-reviewer

Round 11's three math-explorers (CRT/multiplicative-structure, automaton/graph-walk,
Lemma K + Confined-GCD + Window Resolution combination) all independently converged
on the same wall already diagnosed since round 6 (Lemma I): every certified tool
supplies only S₀-level (type-membership) or single-fixed-witness information, never
IDENTITY-level information about which outside-core prime divides an arbitrary far
term. Twelve mechanisms are confirmed dead (see `current.md` rounds 6–10). No
explorer found a counterexample to FAH/Symmetric FAH anywhere.

The one genuinely open, not-yet-dead thread is the Lemma K explorer's sharpened
sub-question: **can any construction of a competitor `c` be FORCED to have its
Lemma-K blocking witness `j` satisfy `P(a_j) ⊄ S₀` (ideally `P(a_j) ∩ F'' ≠ ∅`)?**
Nothing certified supplies this; the explorer's own experiments show the *naive*
Lemma K construction (`c := q·⌊a_n/q⌋`) empirically always routes its blocking
witness to `a_1` or another S₀-saturated early term (0/384 hits on `q*` itself,
across two independent experiments on `a_1=4807`).

This round's field: **one revised approach with a genuinely new, precisely
specified construction attacking that exact sub-question** (build-ready), **one
approach advanced without a new mechanism** (kept alive for ranking continuity,
with an explicit note on how to exploit the first approach's success if it lands),
and **one new approach opening a technique family not yet tried anywhere in this
workspace** (analytic/sieve density bound on the exception set itself, as opposed
to counting/pigeonhole over a fixed finite alphabet), per CLAUDE.md's
plateau-breaking mandate (this is the fourth-plus consecutive round of convergence
on one wall).

## Approaches tried (this round, not re-proposed)
- **CRT/multiplicative-structure-of-a_1 lens** (`math-explorer-crt.md`) — `q`'s
  identity is fixed by the greedy dynamics, not recoverable from `a_1`'s residues,
  exponents, or CRT class; the one clean CRT-shaped regularity found (fixed-unit
  value gaps within a persistent type) is provably equivalent to the periodicity
  conclusion itself (via `reversible-transition-map`'s certified S-sufficiency⟺(†)
  equivalence) — using it as a premise would be circular. Dead end, not re-proposed.
- **Automaton/graph-walk encoding lens** (`math-explorer-automaton.md`) — the
  divisor-class state space is real (it IS the certified Confined-GCD alphabet) but
  the transition function is exactly gap (†)/the Successor Claim in disguise;
  isomorphic to two already-dead mechanisms (round 5's S-sufficiency⟺(†) theorem,
  round 9's Successor-Transport Reduction Lemma + round-9/10 stall). Dead end, not
  re-proposed as a distinct 13th mechanism.
- **`witness-index-descent`, `recruitment-round-charging`, `scalar-well-ordering-lock-in`,
  `reversible-transition-map`, `confined-competitor-construction`, `seed-coupling-induction`**
  — all previously RETHINK'd/dead-ended (see `current.md` rounds 5–10); not
  re-proposed in their dead forms.
- **`density-sieve-contradiction`, `hypergraph-transversal`** (stale since round 1,
  Elo ~1370–1400, `expanded: 0`) — inspected both this round as candidates for
  revival per CLAUDE.md option (c)/(b). **Verdict: not revivable as originally
  framed.** Both approaches' entire "Key Lemma / THE GAP" (Step 3 in each file) is
  "prove the eventual prime core / eventual minimal antichain support is finite" —
  this exact fact is now a *free, unconditional, already-certified* corollary of
  round-1's **Finite Core Theorem** (`lemmas/finite-core-theorem.md`) plus round-6's
  **Collateral-Safety Theorem** (`lemmas/collateral-safety-theorem.md`, giving a
  FIXED finite list of base-type pairs). Reviving either file literally would spend
  a whole round re-deriving something already proved, then land at the exact same
  CRT+cyclic-pigeonhole finish (their own Step 5/step 5) that every other approach
  already reaches — i.e., they would immediately collapse onto the FAH wall with no
  new content. **However, `density-sieve-contradiction`'s underlying TECHNIQUE
  (sieve/Mertens-style density estimate) has never been tried against the actual
  open target (bounding the FAH exception set), only against the now-moot
  core-finiteness question** — this observation seeds this round's new approach
  below (`sieve-density-exception-bound`), which reuses the technique but retargets
  it, rather than reviving the dead file's stated gap.

## Current best
Unconditional, established (see `current.md` for full list; unchanged this round):
Free Facts, Bounded/Generalized Bounded Gap Lemmas, Persistent-Type Pigeonhole,
Finite Core Theorem, Generalized Bounded Witness Lemma + Recruitment Corollary,
Extended Persistent-Type Pigeonhole, Canonical-Refinement Lemma, Monotonicity of
Resolution, Collateral-Safety Theorem (closes gap (†) exactly to base-type-pair
FAH/Symmetric FAH termination), Singleton-Side FAH (handles `|F'|=1` or `|F''|=1`
fully), Confined-GCD Lemma, Cofinite Sufficiency Lemma, Window Resolution Lemma,
Lemma K (Adjacent-Multiple-Blocking), Minimality Tautology Lemma (scope-narrowed).
**The single remaining crux is FAH/Symmetric FAH in the genuinely hard
`|F'|,|F''| ≥ 2` regime** — equivalently, per the Cofinite Sufficiency Lemma,
Cofinite FAH: the exception set `E = {n > n_B : ρ(n)=A', q* ∤ a_n}` is finite.

## Full proof
Not present — Status is `partial`.

---

# Approach 1 (REVISE): `greedy-exchange-cost-potential` — Forced-Escape Blocking
Construction

### Target
The full problem claim, via the certified reduction: prove Cofinite FAH for an
arbitrary rogue pair `(A',B')` with canonical prime `q* := min(F'∩F'')`, i.e. that
`E := {n > n_B : ρ(n)=A', q*∤a_n}` is finite.

### Why this is not a repeat of any dead mechanism
This is NOT the naive Lemma K construction (`c := q·⌊a_n/q⌋`, empirically shown
this round to route its blocking witness to `a_1`/S₀-heavy terms — 0/384 hits on
`q*`). It is NOT the Escape-Budget/window mechanism (killed by the
Growing-Constraint Obstruction — that mechanism's witness pool provably grows
unboundedly; this construction's witness, by design, is anchored differently, see
below). It targets the Lemma K explorer's precisely-stated open sub-question
directly, with a concrete, checkable construction not previously attempted in this
workspace.

### Skeleton
Fix a rogue pair `(A',B')`, witnesses `n_A<n_B`, `S₀ ⊇ Q`, `q* ∈ F'∩F''` (so
`q* ∉ S₀` by definition of `F''=P(a_{n_B})\S₀`, hence `gcd(q*, ∏_{p∈S₀}p)=1`).
Suppose toward a contradiction that `E` is infinite; let `n ∈ E` be arbitrary (an
`A'`-occurrence past `n_B` with `q*∤a_n`).

1. **CRT-glued competitor.** Let `M := ∏_{p∈S₀} p`. By CRT (since `gcd(q*,M)=1`),
   there is a unique residue class `r (mod q*M)` with `r ≡ a_n (mod M)` and
   `r ≡ 0 (mod q*)`. Let `c` be the representative of this class in the interval
   `(a_{n-1}, a_{n-1}+q*M]` (well-defined and unique since the interval has length
   exactly `q*M`).
   - **Key property (by construction, needs only CRT — no new lemma):** `c ≡ a_n
     (mod p)` for every `p ∈ S₀` — i.e. `c` and `a_n` have IDENTICAL divisibility
     behavior with respect to every S₀-prime — and `q*|c` (unlike `a_n`, by
     hypothesis `n∈E`).
2. **S₀-legality of `c` is automatic (inherits from `a_n`'s own, already-proved,
   legality).** For any `j<n` whose legality-witnessing shared prime with `a_n`
   (guaranteed to exist by Free Facts, `gcd(a_n,a_j)>1`) can be taken to be an
   `S₀`-prime `p`, `c` shares that same prime `p` with `a_j` too (since `p|a_n ⟺
   p|c` for `p∈S₀`, by step 1). So `c` cannot be illegal against any such `j`.
3. **THE GAP — the only way `c` can be illegal.** If `c` is illegal against some
   `j<n` (i.e. `gcd(c,a_j)=1`), then by step 2, `a_n`'s legality against THIS
   SPECIFIC `a_j` cannot have been witnessed by any `S₀`-prime — i.e. the shared
   prime(s) between `a_n` and `a_j` lie entirely outside `S₀` (a "junk" or
   `F`-type prime unique to this pair). **This is not yet proved to happen** — it
   is the branch Lemma K's dichotomy produces IF `c` is illegal; the open work is
   showing (i) `c` is not always `≤ a_{n-1}` (branch (a), which gives no
   information — this needs a magnitude argument, see Risk 1 below), and (ii) that
   branch (b), when it fires, is genuinely usable — i.e., that the forced
   "outside-S₀ shared prime" between `a_j` and `a_n` can be pinned down further
   (ideally shown to force `q*|a_j`, or shown to recur with bounded multiplicity
   across the infinitely many `n∈E`, giving the desired finiteness via a
   pigeonhole over a NOW-CONTROLLED alphabet — e.g. `Div(b)` from Confined-GCD, if
   `j` can additionally be tied to the `n_B`-anchored alphabet).
4. **Apply Lemma K's dichotomy to `c` with the target prime baked in by
   construction** (not, as in the original Lemma K, chosen generically): since
   `c` already has `q*|c`, this construction does not need Lemma K's own
   `q`-parameter at all — it replaces "round `a_n` down to avoid `q`" with "CRT-glue
   a same-S₀-signature integer that already carries `q*`." This is the genuinely
   new ingredient: earlier attempts (naive Lemma K) tried to make `c` AVOID a
   prime and hoped the blocking witness would reveal information; this
   construction makes `c` **carry** the target prime `q*` and **match** `a_n`'s
   S₀-signature by design, so that if `c` fails to be a legal (and smaller-or-equal)
   candidate, the failure is forced to route through non-S₀ territory — the exact
   opposite of the naive construction's observed failure mode.

### Risks / open sub-steps (honest, not glossed over)
- **Risk 1 (magnitude/branch (a)).** Need to check `c` is not trivially
  `≤ a_{n-1}` (which would make step 3 vacuous, no information). `c` lies in
  `(a_{n-1}, a_{n-1}+q*M]` by construction — this is a genuine candidate,
  strictly greater than `a_{n-1}`, so branch (a) of Lemma K (`c ≤ a_{n-1}`) is
  IMPOSSIBLE by this construction's own definition (unlike the naive Lemma K,
  where branch (a) could fire) — this is actually a strengthening over the
  original Lemma K, not a new risk, but the builder MUST verify `c ≠ a_n$ itself
  (should hold automatically since `q*∤a_n` but `q*|c`) and that `c`'s
  well-definedness doesn't secretly collapse (e.g. `c` should be checked to be a
  positive integer, distinct from every earlier term, etc. — routine but must be
  written out).
- **Risk 2 (does branch (b) actually fire, i.e. is `c` ever illegal at all?).**
  It is logically possible `c` turns out to be FULLY legal against every `j<n`.
  If so, `c` is a legal candidate with `a_{n-1} < c`. If additionally `c < a_n`,
  this DIRECTLY CONTRADICTS `a_n`'s minimality (the actual greedy choice) —
  i.e. gives a proof, not just a diagnostic! If `c ≥ a_n`, no contradiction, but
  also no information; the builder must compute/bound `c` vs `a_n` (both are
  determined mod `q*M`, roughly comparable in size to `a_n` up to an error of
  `O(q*M)` — this needs the certified Generalized Bounded Gap Lemma or a direct
  argument, not yet done). **This branch, if it can be shown to occur with `c<a_n`
  infinitely often, would PROVE Cofinite FAH directly** (each such `n` gives an
  immediate contradiction to `n` even being a legal term unless `q*|a_n` after
  all) — this is the most promising sub-case to check computationally FIRST,
  before the more delicate branch-(b) analysis.
- **Risk 3 (per Sandwich Genericity Theorem's caution).** The already-certified
  Sandwich Genericity / Escape-Cost Vacuity Theorem shows arguments built ONLY
  from the class-blind magnitude sandwich cannot discriminate by class. This
  construction does NOT rely solely on magnitude — the discriminating content is
  the CRT-forced identity `q*|c`, an explicit residue-class (identity-level, not
  magnitude-level) fact. Magnitude is used only to rule out the now-impossible
  branch (a) and to bound `c` vs `a_{n-1}`/`a_n` in Risk 2 — a legitimate,
  narrower use. The builder MUST explicitly verify this distinction holds up (i.e.
  that no step secretly reduces to a pure magnitude comparison) before claiming
  the construction escapes the Escape-Cost Vacuity Theorem's scope.

### Computational sanity check (dispatch to builder as Step 0)
Before any proof-writing, run this construction on the workspace's standard
rogue-pair testbeds (`a_1=187`, `209`, `247`, `385`, `4807`, `11305`) and report,
for a sample of exceptional-looking indices (or, absent real exceptions since FAH
has never failed empirically, for EVERY `A'`-occurrence past `n_B` treated
hypothetically as if checking the construction's mechanics): does `c` land `< a_n`
and turn out fully legal (Risk 2's promising sub-case)? Does branch (b), when it
fires, always route through a non-S₀ prime shared between `a_j` and `a_n` as
predicted by step 3? This is a cheap, decisive first check.

### Certified lemmas to reuse (no re-proof needed)
Free Facts, Confined-GCD Lemma (for `F''`/`Div(b)` if the analysis reaches
Risk 2's pigeonhole), Adjacent-Multiple-Blocking (Lemma K, for the dichotomy
shape), Generalized Bounded Gap Lemma (for magnitude bookkeeping in Risk 1/2).

---

# Approach 2 (ADVANCE, no new mechanism this round): `covering-system-construction`

### Status
Kept live for ranking continuity (highest Elo, most-developed approach, 9
certified lemmas traced to it). No new mechanism is dispatched to it this round
— three explorer lenses and the Lemma K combination lens all confirmed the same
wall this approach already sits at (Collateral-Safety Theorem's exact reduction of
(†) to base-type-pair FAH/Symmetric FAH termination, `current.md` round 6).

### Note for next round (do not build against this yet — conditional on Approach 1)
Round 8's Fixed-Witness Divisor-Chain mechanism died because the pigeonholed
alternate prime `r` could land in `S₀` (specifically `r ∈ A'`, giving no
contradiction with rogueness — see `current.md` ROUND 8). **If Approach 1's
Forced-Escape Construction succeeds in forcing a blocking witness's shared prime
to lie outside `S₀`, this is EXACTLY the missing ingredient that would repair
Round 8's dead dichotomy** (its branch (a), "r ∈ S₀", would become impossible by
the same construction). This is a genuine instance of CLAUDE.md's guidance (b):
inspecting a dead mechanism's true failure mode and finding it is fixable by
combining it with a new, not-previously-co-used tool. **Do not dispatch this
combination yet** — it is strictly downstream of Approach 1's construction
actually working; dispatching it prematurely would duplicate Approach 1's
unverified core content in a second file.

---

# Approach 3 (NEW): `sieve-density-exception-bound`

### Target
The full problem claim, via the same certified reduction (Collateral-Safety +
Cofinite Sufficiency): prove the FAH exception set `E` is finite for an arbitrary
rogue pair, using an analytic/counting-density technique — a genuinely different
technique family from every one of the twelve dead mechanisms (all of which used
either infinite pigeonhole over a fixed finite alphabet, magnitude sandwiches, or
definitional/tautological minimality arguments — none used density/sieve
estimates against the actual FAH target).

### Why this is not a repeat of `density-sieve-contradiction` (round 1, dead-in-spirit)
That file's entire gap was proving the eventual prime core is finite — a fact now
FREE via the certified Finite Core Theorem + Collateral-Safety Theorem (round 1,
round 6). Reviving it literally adds nothing. This approach reuses only the
TECHNIQUE (sieve/Mertens-style density estimates) and retargets it at the actual
open quantity: the density, within the (infinite) set of `A'`-type occurrences
past `n_B`, of exceptional indices where `q*∤a_n`.

### Skeleton
1. Fix a rogue pair, `q*`, `F''`, `b`, `Div(b)`, `D_bad` (Confined-GCD Lemma's
   already-certified finite alphabet). `E = ⋃_{d∈D_bad} \{n>n_B : ρ(n)=A',
   g_n=d\}` where `g_n := gcd(a_n,a_{n_B})`.
2. **Key Lemma (density bound on `E` — THE GAP).** For each fixed `d ∈ D_bad`,
   estimate the density (within the `A'`-occurrence index set, using the Bounded
   Gap Lemma's linear value-vs-index sandwich to convert between index-density
   and value-density) of integers `m` in the arithmetic-progression-like range
   swept by the greedy process that are `≡` a residue forcing `gcd(m,a_{n_B})=d`
   exactly (not merely `d|gcd`), via an inclusion–exclusion / Mertens-type
   estimate over the primes of `b/d`. The greedy process's actual term `a_n` is
   not a uniformly random integer, so this step needs a genuine, non-circular
   argument for why the greedy-selected subsequence of `A'`-occurrences should
   track the "generic" density rather than adversarially concentrate on `D_bad`
   classes — **this is the true open content**, analogous to (but a strictly
   different technique from) every previously-tried mechanism's stall point.
   Two sub-routes, both untried in this workspace:
   (a) **Direct sieve on the raw integers**: bound, among all integers in a long
   window `(a_{n_B}, X]`, the count that are simultaneously (i) legal as
   `A'`-type terms (all `S₀`-primes match `A'`) and (ii) in a `D_bad`
   `g`-class — compare against the count that are `q*`-good — using Mertens'
   estimate `∏_{p≤x}(1-1/p) ~ 1/\ln x` restricted to the finitely many primes of
   `S₀∪F''`, and argue the greedy process, by ALWAYS taking the smallest legal
   integer, cannot systematically prefer the sparser `D_bad` classes over a
   sustained range without eventually being forced into the denser `q*`-good
   class (an extremal/greedy-optimality argument — no known certified lemma
   supplies this, flagged as the primary sub-route to attempt first, as it avoids
   probabilistic language in favor of a direct greedy-vs-density comparison).
   (b) **Summability via Borel–Cantelli-style bound (deterministic analogue)**:
   if the "probability" that a random `A'`-occurrence lands in `D_bad` decays like
   `O(1/k^{1+ε})` at its `k`-th occurrence (rather than a constant), then `E`
   would be provably finite by a deterministic summable-tail argument, WITHOUT
   needing full cofiniteness density-1 — this is a strictly weaker, more
   tractable target than sub-route (a) and should be tried second if (a) stalls.
3. **Given** the Key Lemma yields `E` finite (either sub-route), Cofinite FAH
   holds, and the already-certified `Cofinite Sufficiency Lemma` + `Collateral-
   Safety Theorem` finish the whole problem exactly as in every other approach's
   Step 5/CRT finish.

### Open gaps
- Step 2 (density/summability bound on `E`, non-circular, without secretly
  re-deriving core-finiteness) is the entire unresolved content — genuinely
  untried in this workspace against this specific target.
- The standard secondary "periodicity from n=1" gap, unaffected by this approach,
  remains open downstream as in every other approach.

### Cases to cover
- `|D_bad|=0` (i.e. `Div(b)\{1\}` is entirely `q*`-divisible) — trivial, FAH holds
  immediately with zero density argument needed; should reduce cleanly and serves
  as a sanity check of the setup.
- `|D_bad|≥1` — the genuinely hard case; test first on the workspace's own
  `a_1=4807` rogue pair (`D_bad={13}`, `Div(b)=\{1,13,17,221\}` — already
  identified this round by the Lemma K explorer) as a concrete testbed before
  attempting the general bound.

### Watch out for
- Do not silently assume the greedy-selected subsequence of `A'`-occurrences is
  "random" or "equidistributed" — this is exactly the unproved content; any
  density argument must derive its bound from the greedy MINIMALITY rule itself
  (an extremal argument), not from an unjustified equidistribution heuristic.
- Distinguish density-zero (insufficient — Cofinite Sufficiency needs literal
  finiteness, not just density zero) from a genuinely summable/finite bound;
  density-zero alone, if that is all sub-route (a) can deliver, is a real partial
  result worth recording honestly but does NOT close the problem — flag this
  distinction explicitly if reached.

---

## Recommendation to outline-reviewer
Given twelve dead mechanisms plus three more explorer-lens confirmations this
round with zero new counterexamples found anywhere (strong evidence FAH is simply
true, the difficulty is entirely in proving it), the field above puts one
concrete, precisely-specified, previously-untried construction on the table
(Approach 1 — the most promising, directly answering the Lemma K explorer's
sharpened open sub-question) alongside one genuinely different technique family
(Approach 3 — analytic/sieve density, never before tried against the actual FAH
target in this workspace) and keeps the leading approach alive for continuity
(Approach 2). If Approach 1's Step 0 computational check comes back negative
(construction doesn't behave as predicted) or Approach 3 also stalls at the same
"can't derive a non-circular bound from greedy minimality alone" wall, that would
be a strong signal — across now 16+ independently-framed attempts — to escalate to
the orchestrator per CLAUDE.md option (c): consider whether the problem's crux
needs a resource genuinely outside the gcd-pigeonhole/existence-magnitude family
altogether (e.g. a literature/crux-corpus search specifically for "greedy
minimal-legal-integer construction with joint divisibility constraints" as a named
technique elsewhere, which this round's CRT explorer reports finding nothing
matching in the corpus so far).
