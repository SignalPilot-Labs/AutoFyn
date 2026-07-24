## imo-2026-06 — round 20 outline field

Field: 4 slugs (1 revise, 1 copy-of-revise, 1 new, 1 advance).

---

### 1. `triangle-consistency-pigeonhole` — revise

Target: the problem's actual claim (existence of T,L with a_{n+T}=a_n+L for
all n≥1), via the Master Conditional Theorem's H1 (FAH) hypothesis — this
approach attacks H1 specifically; H2 is out of scope (handled elsewhere).

Technique: elementary gcd/pigeonhole exchange over the *choice of witness*
(Constrained Singleton Coherence), NOT sieve/density (that route is
certified dead within this same file, §5.3).

Skeleton:
1. Fix a rogue pair of disjoint-base-type persistent types `(A',B')` at the
   recruited core `S_0` — exists by the Finite Core Theorem / Extended
   Persistent-Type Pigeonhole (already certified; cite, don't reprove).
2. For a FIXED occurrence `m_A` of `A'`, pigeonhole
   `d(x):=\gcd(a_{m_A},a_x)` over `x\in X_{B'}` (against the finite divisor
   set of `a_{m_A}`) to get an infinite `X_{B'}^{(0)}` with `d(x)=d^*`
   constant, `d^*`'s prime factors confined to `F'_{m_A}` — by
   `lemmas/double-witness-nested-pigeonhole.md` + `lemmas/confined-gcd-
   lemma.md` (cite, already certified).
3. **New Lemma — Constrained Singleton Coherence** (prove in full this
   round): if `x\in X_{B'}^{(0)}` is itself a singleton occurrence
   (`P(a_x)\setminus S_0=\{q_x\}`), then since `d^*\mid a_x` and all of
   `d^*`'s prime factors lie outside `S_0`, `d^*` is forced to be a power of
   `q_x` alone. Two corollaries: (a) **Composite-Exclusion**: if `d^*` has
   ≥2 distinct prime factors, `X_{B'}^{(0)}` contains ZERO singleton
   occurrences; (b) **Prime-Power Coherence**: if `d^*=q^k`, every singleton
   `x\in X_{B'}^{(0)}` (if any) has `q_x=q` — automatic prime-matching, no
   further search needed.
4. **Open gap (the sharpened, narrower existence question)**: show that for
   SOME choice of witness `m_A` ranging over occurrences of `A'`, the
   induced dominant/majority pigeonhole class `d^*(m_A)` is (i) a prime
   power AND (ii) actually contains a singleton occurrence of `B'`. Attempt
   via an exchange/extremal argument over the choice of `m_A` — e.g. try
   `m_A` = earliest occurrence first (matches both known hard test seeds,
   `a_1=4807,11305`, per explorer verification); if that fails in general,
   use `lemmas/elementary-omega-bound.md` (`|F'_{m_A}|=O(\log m_A)`, so only
   finitely many candidate divisor-classes per fixed `m_A`) to bound a
   search, and try to show minimality of the greedy rule biases `F'_{m_A}`
   itself toward being small/singleton for infinitely many `m_A`.
5. Symmetrize: repeat 2-4 with roles of `A'`,`B'` swapped to get a matching
   singleton on the other side.
6. Apply `lemmas/two-sided-singleton-witness-theorem.md` (already certified,
   cite) to conclude Cofinite FAH for `(A',B')`, hence (generic pair) H1.
7. Feed into the (already gap-free, audited round 20) Master Conditional
   Theorem for the full claim, jointly with H2 (handled by other approaches).

Key lemmas (claim + mechanism):
- Constrained Singleton Coherence — because `d^*` divides `a_x`, all of
  `d^*`'s prime factors lie outside `S_0` (Confined-GCD Lemma), and if `x`
  is a singleton its *entire* outside-core part is one prime `q_x`, so any
  divisor of `a_x` supported outside `S_0` is a power of `q_x` — forcing
  `d^*=q_x^j` for some `j`.
- Composite-Exclusion Corollary — immediate contrapositive of the above: `d^*`
  with ≥2 distinct primes cannot divide any singleton's `a_x`.

Open gaps: step 4, existence of a witness `m_A` whose induced pigeonhole
class is both a prime power AND non-emptily populated by a singleton — this
is the sharpened residual, distinct from (narrower than) the original FAH
existence hypothesis.

Cases to cover: none beyond the generic disjoint-base-type rogue pair
(already scoped by the Master Conditional Theorem).

Watch out for: (a) do NOT let the exchange-over-`m_A` argument silently
collapse into "core-enlargement recruitment," which the singleton-witness
explorer traced this round and found structurally equivalent to H1/H2's own
open content (recorded dead-shaped in the report) — mandate the builder
explicitly check its proposed exchange mechanism against this trap before
investing; (b) step 4(ii) (an actual singleton EXISTING in the class) is
separate from step 4(i) (class is a prime power) — proving (i) alone is not
enough, don't let the write-up conflate them.

---

### 2. `triangle-critical-dichotomy-witness` — copy-of `triangle-consistency-pigeonhole`

Same starting file/state as approach 1 (both attack the Two-Sided Singleton
Witness Theorem's existence hypothesis for H1), but pursues a genuinely
different construction so both can run in parallel without one blocking the
other for a builder slot.

Target: same as approach 1 (H1 via existence of a two-sided singleton
witness for a rogue pair `(A',B')`).

Technique: `lemmas/critical-prime-dichotomy.md`'s branch (b) — "sole
rescuer" singleton *intersection with a fixed earlier index*, instead of
approach 1's pigeonholed-gcd-class route. Genuinely different mechanism
(intersection with a past term vs. pigeonhole over a class of later terms).

Skeleton:
1. Same setup as approach 1, steps 1.
2. For occurrences `n\in X_{A'}` and each outside-core prime `q'\mid a_n`,
   apply the Critical Prime Dichotomy Lemma: either (a) stripping `q'` from
   `a_n` drops it below `a_{n-1}` (uninformative branch, already known
   dead-shaped), or (b) `q'` is the *sole rescuer* of some earlier index
   `i<n`, i.e. `P(a_i)\cap P(a_n)=\{q'\}` exactly.
3. **New target lemma**: show branch (b) fires infinitely often within
   `X_{A'}` with a *structured* rescued index `i` (e.g. `i` always lying in
   a fixed small window, or always itself lying in a specific persistent
   type) — this directly hands a singleton-style intersection fact
   (`P(a_i)\cap P(a_n)=\{q'\}`) with NO pigeonhole step needed, if `i` can
   be pinned down.
4. **Bridging step (the open gap)**: relate the rescued index `i` to the
   rogue pair's type structure `B'` — does `i`'s occurrence type interact
   with `B'` in a way that lets the same `q'` serve as the matching
   singleton on the `B'` side? Untried; flagged by the singleton-witness
   explorer as "not developed further this pass."
5. If bridged, invoke `lemmas/two-sided-singleton-witness-theorem.md` as in
   approach 1 step 6.

Key lemmas: Critical Prime Dichotomy branch (b) itself is already certified
(mechanism: minimality of `a_n` forces every non-rescuing outside-core prime
removable without breaking legality, leaving exactly the rescuer prime as
load-bearing) — the NEW content here is steps 3-4, not yet proved.

Open gaps: step 3 (does branch (b) fire infinitely often with a structured
`i`?) and step 4 (bridging `i` to `B'`) — both fully open.

Cases to cover: none beyond generic rogue pair.

Watch out for: this may turn out to be the SAME underlying fact as approach
1's existence gap in different vocabulary — mandate the builder explicitly
check for equivalence/redundancy with approach 1's Step 4 before investing
heavily, and report a clean RETHINK (not force artificial distinctness) if
they collapse into one fact.

---

### 3. `a1-3q-subfamily-theorem` — new

Target: the problem's actual claim (T,L existence), scoped explicitly and
completely to the subfamily `a_1 = 3q` for prime `q ≥ 7` (`q≠5` excluded by
name, with the exclusion justified): prove `a_n = 3q+3(n-1)` for every
`n ≥ 1`, i.e. literal `T=1, L=3` periodicity from `n=1`. Does NOT touch H1
or H2 — self-contained, unconditional, elementary, adding a third certified
floor subfamily alongside `2|a_1` and `a_1=p^k`.

Technique: self-contained strong induction (same proof shape as
`lemmas/prime-power-seed-literal-periodicity-theorem.md`), generalized from
`|Q|=1` to `|Q|=2` by handling the ONE extra intermediate candidate
(`a_n+2`) with a case split instead of the singleton-`P(a_1)` shortcut.

Skeleton:
1. Base case `n=1`: trivial.
2. Strong induction hypothesis: `a_i = 3q+3(i-1)` for all `i ≤ n` (so `3 |
   a_i` for every `i ≤ n`).
3. **Illegality of `a_n+1`**: consecutive integers are coprime — cite
   `lemmas/free-facts-gcd.md` (universal, no new argument needed).
4. **Illegality of `a_n+2`** (the one nontrivial candidate; THIS is the
   proof's real content): `a_n \equiv 0 \pmod 3 \Rightarrow a_n+2\equiv 2
   \pmod 3`, so `3 \nmid (a_n+2)`. Since `P(a_1)=\{3,q\}`, any common factor
   of `a_n+2` and `a_1` is confined to `\{1,q\}` (3 is excluded). Case
   split on whether `q \mid (a_n+2)`:
   - **Case (a) `q\nmid(a_n+2)`**: then `\gcd(a_n+2,a_1)=1`, illegal via
     `i=1` directly — done, no further argument needed.
   - **Case (b) `q\mid(a_n+2)`** (occurs periodically, roughly density
     `1/q` in `n`, per the explorer's numeric check): `\gcd(a_n+2,a_1)=q>1`
     so the `i=1` check alone does NOT rule this out; need a DIFFERENT
     earlier index `i<n` with `\gcd(a_n+2,a_i)=1`. **Open gap — prove**:
     some FIXED small early index (candidate: `i=2`, `a_2=3(q+1)`) is
     coprime to `a_n+2` whenever `q\mid(a_n+2)` — i.e. derive the exact
     modular condition under which `\gcd(a_n+2,3(q+1))=1` and show it holds
     whenever `q\mid(a_n+2)`, or else identify the correct small witness
     index if `a_2` alone doesn't suffice (bounded search over a FEW early
     terms, structurally like the workspace's Universal Early Intersection
     Lemma machinery, not an unbounded FAH-style search).
5. **Legality of `a_n+3`**: `3\mid a_n` and `3\mid 3`, so `3\mid(a_n+3)`;
   since `3\mid a_i` for all `i\le n`, `\gcd(a_n+3,a_i)\ge 3>1` for every
   `i\le n`.
6. Minimality of `a_{n+1}` then forces `a_{n+1}=a_n+3=3q+3n`, closing the
   induction.

Key lemmas (claim + mechanism):
- **Confined common-factor dichotomy**: any common factor of `a_n+2` and
  `a_1=3q` lies in `\{1,q\}` — because `3\nmid(a_n+2)` (mod-3 residue clash
  with the inductive hypothesis `3|a_n`) and `P(a_1)=\{3,q\}`.
- **Fixed early-witness blocks the `q`-coincidence escape** (THE open
  lemma) — mechanism to establish: show `\gcd(a_n+2,a_2)=1` (or, if that
  specific witness fails on inspection, the correct small witness) exactly
  in the residue regime where `q\mid(a_n+2)`, by direct modular
  computation on `a_2=3(q+1)` (its own prime factorization is fixed and
  small, independent of `n`).

Open gaps: step 4 case (b) — the fixed-witness blocking argument. Everything
else in the skeleton is either already-certified content or a direct
computation.

Cases to cover: `q\equiv 1` vs `q\equiv 2 \pmod 3` (since `q\ne 3` by
coprimality of `q` and `a_1=3q`'s own factor 3, both residues are possible
and must both be checked in the modular computation); explicit exclusion of
`q=5` with the reason restated (already-documented Odd-Prime
Non-Trivialization counterexample, persistent period-4 alternation).

Watch out for: (1) do NOT let this proof secretly require the general,
already-REFUTED `a_1=p\cdot q, q\gg p` machinery — it must stay genuinely
elementary/self-contained, bounded-witness-search only; (2) explicitly
verify the fixed-witness mechanism against `q=7,11,13` (small `q`, tightest
case) before trusting it generalizes to all `q\ge 7`; (3) if the fixed
single early witness (`a_2`) provably does NOT suffice for some `q`, do not
silently retry the unbounded "search until it works" pattern that
characterizes the still-open general FAH crux — if the needed witness set's
size is not uniformly bounded across all `q`, report this honestly as a
dead end for THIS specific technique, not force a claim.

---

### 4. `n1-periodicity-reconciliation` — advance

Target: unchanged — the conditional Master Conditional Theorem chain
(reduces the general claim to H1+H2, both precisely stated) plus the
consolidated unconditional floor-deliverable write-up. Does not touch H1/H2
directly this round (per the round-17+ escalation rule: after 3+
consecutive dead fresh-framing sweeps, consolidate/audit rather than force
a mechanism).

Recommended continuation (2 concrete tasks, per this round's audit
explorer's §3 recommendation and the fresh-framing explorer's §3 finding):

1. **Fix and re-certify the Generalized Class-Blindness Obstruction (§7)**
   at its CORRECT, narrower scope. Round 19's reviewer found the "two
   scenarios agree" step circular for statistics that reference the
   realized legality-history data (`Φ(N)` depending on `W(N)`). Per the
   reviewer's own check, the theorem IS correct if restricted to genuinely
   *ambient/decoupled-from-realized-data* statistics — matching the true
   scope of its two certified predecessors (Escape-Cost Vacuity, Density-
   Argument Vacuity Corollary). Restate and re-prove §7 at this restricted
   scope (weaker: does NOT cover density/second-moment/finite-Fourier/LP-
   relaxation sub-cases that use realized occupation counts — say so
   explicitly, do not re-claim the broader coverage). Additionally, fold in
   the fresh-framing explorer's new standing meta-rule this round (found
   independently, generalizes the same defect): *any* future argument
   premised on "two legal continuations/scenarios consistent with the same
   finite data" is invalid unless it supplies an EXPLICIT construction
   (e.g. two concrete `a_1` seeds verified computationally to share a long
   common core/prefix then diverge) — because the recursion is fully
   deterministic given `a_1`, so no such ensemble exists a priori. Certify
   this meta-rule as a citable screening corollary (not a new proof of
   anything positive) so future rounds can invoke it by name instead of
   re-discovering the circularity each time.
2. **Assemble the tightened floor-deliverable write-up** per the audit
   explorer's 6-point structure: (i) problem statement up front; (ii) the
   `2|a_1` and `a_1=p^k` theorems reproduced inline (short proofs, not just
   cited) as a clean union-of-subfamilies result; (iii) the Master
   Conditional Theorem stated with H1, H2 spelled out in full; (iv) an
   honest one-paragraph summary of which FAH mechanism families were tried
   and killed, correctly distinguishing "certified dead" from "argued but
   not yet certified" (the restricted Class-Blindness Obstruction from task
   1 above); (v) if `a1-3q-subfamily-theorem` (approach 3) is proved this
   round or a future round, add it as a THIRD floor subfamily to the union;
   (vi) explicitly keep `Status: partial` for the general claim.

Key lemmas: none new beyond the restricted-scope re-proof of task 1 (a
correct, narrower version of already-attempted content — mechanism:
inherits the Escape-Cost Vacuity / Density-Argument Vacuity Corollary's own
proof verbatim once the statistic class is restricted to ambient-only).

Open gaps: none introduced beyond what's already open (H1, H2); this
approach's job is consolidation + one honest scope-correction, not new
attack surface.

Cases to cover: none (write-up/consolidation task).

Watch out for: do not let the restricted Class-Blindness Obstruction's
narrower scope get silently overstated back to the original §7 claim in the
write-up — the reviewer explicitly flagged this exact overclaim risk last
round; state the narrower scope plainly in both the certified lemma file
and the current.md summary.

---

## Recommended build-set candidates (for outline-reviewer to evaluate)

Primary recommendation: `triangle-consistency-pigeonhole`,
`triangle-critical-dichotomy-witness`, `a1-3q-subfamily-theorem`,
`n1-periodicity-reconciliation` — all 4. Rationale: approaches 1-2 are the
strongest live FAH-crux thread (two genuinely different constructions for
the same narrowed existence gap, worth running in parallel per the copy
criterion); approach 3 is a concrete, scoped, achievable floor-deliverable
target independent of H1/H2 (adds real certified content even if H1/H2 stay
open); approach 4 is low-risk consolidation/hedge work that also closes a
flagged overclaim risk from round 19. If the outline-reviewer wants to
economize builder slots, the single approach safest to defer is #2
(`triangle-critical-dichotomy-witness`) since it's explicitly flagged as
possibly redundant with #1 pending a builder's own equivalence check — but
recommend keeping it if slots allow, since population diversity on the
strongest live thread is valuable this round.
