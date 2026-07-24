## imo-2026-06

**Context (round 12).** 14 mechanisms across 6 rounds (6-11), spanning existential/
pigeonhole, magnitude-sandwich, tautological-minimality, CRT-glue/competitor-
construction (every modulus variant), and aggregate density/sieve-counting, are all
confirmed dead as routes to FAH/Symmetric FAH ("Cofinite FAH") within the
persistent-type/extended-type reconciliation framing. Round 11's reviewer mandated a
genuinely different corridor or a bespoke fallback. This round's three explorers
independently confirm: (a) multiplicative/valuation structure of a_1 gives no new
lever (multiplicative lens); (b) the |F'|=2 "bespoke small case" re-lands on the same
seeds/wall, not new terrain (smallcase lens); (c) a combinatorics-on-words
(Morse-Hedlund) reformulation is genuinely untried, though it is an EQUIVALENCE, not
a bypass, of the goal (freshframe lens). Field below: one new plateau-breaking
approach (subword complexity), one revived-but-redirected approach (seed-coupling,
now via aggregate/existential induction instead of the falsified positional
correspondence), one advanced-for-continuity leader (covering-system-construction),
and greedy-exchange-cost-potential goes quiet this round (stale, its family of
mechanisms — CRT-glue — is fully closed, and this round's explorers found no new
angle for it specifically; re-touching it now would waste a build slot on a slug with
nothing new to attempt, per the workspace's own NEVER-rule against patching without a
genuinely new fix in hand).

---

### subword-complexity-periodicity (NEW)

Target: there exist positive integers T, L such that a_{n+T} = a_n + L for all
sufficiently large n (and, as the secondary/lower-priority gap, for all n ≥ 1
literally).

Technique: combinatorics on words — the Morse–Hedlund theorem (a sequence over a
finite alphabet is eventually periodic iff its factor/subword-complexity function is
eventually bounded, equivalently p(k) ≤ k for some k), applied to the gap sequence
g_n := a_{n+1} - a_n, PLUS a genuinely new mechanism (a finite-defect automaton /
pumping argument on S₀-signature windows) to attack the resulting complexity-
boundedness target by a route different from FAH's direct "prove a fixed prime
divides every occurrence" mechanism. **Honesty flag, stated explicitly per the
freshframe explorer's own caution:** proving bounded complexity of (g_n) is logically
EQUIVALENT to the problem's actual claim, so this is NOT a bypass of the underlying
difficulty — it is a different TOOLSET (window/pumping combinatorics instead of
divisibility-witness recruitment) aimed at the same wall, which is exactly what
round 11's mandate asked for (a genuinely different corridor, not a reroute within
the same one).

Skeleton:
  1. (Free, certified) g_n ∈ {1, ..., a_1} for all n — finite alphabet — by the
     Bounded Gap Lemma (`lemmas/bounded-gap-lemma.md`).
  2. State the Morse–Hedlund theorem explicitly (classical, not in `knowledge_base.md`
     — cite it by name and give its one-line proof idea in the writeup): for a
     sequence x over a finite alphabet, define p(k) := #{distinct length-k
     contiguous factors of x}. If p(k₀) ≤ k₀ for some k₀, then every length-k₀ factor
     has a UNIQUE right-extension in x for all k ≥ k₀ (no "special factors" beyond
     k₀) — call this Right-Extension Determinism at level k₀. By pigeonhole, two
     starting positions m < n share the same length-k₀ window; Right-Extension
     Determinism forces the sequence from position m onward to agree with the
     sequence from position n onward INDEX BY INDEX, forever — giving eventual
     periodicity with period T = n - m exactly (this is the actual mechanism, not
     merely "cite Morse-Hedlund" — the builder must carry out this pigeonhole +
     determinism argument explicitly, since the theorem's citation alone is not a
     proof per CLAUDE.md).
  3. Reduce the target to: **∃ k₀ such that no length-k₀ window of (g_n) is
     "special"** (has ≥ 2 distinct legal right-extensions occurring infinitely often
     in the actual sequence — note: since (g_n) is a single realized sequence, not a
     shift-space, "special" here must be defined carefully as: two positions m, n
     with identical length-k₀ windows (g_m,...,g_{m+k₀-1}) = (g_n,...,g_{n+k�0-1}) but
     g_{m+k₀} ≠ g_{n+k₀}). Call the set of such "colliding" window-pairs the DEFECT
     set at level k₀.
  4. **Key Lemma (Finite-Defect Boundedness — the new mechanism, open gap):** the
     total number of DISTINCT length-k₀ windows that ever exhibit a collision (i.e.
     have two extensions disagreeing) is finite and, in fact, bounded by a quantity
     computable from the already-certified finite data: the extended-persistent-type
     alphabet 𝒫' (Extended Persistent-Type Pigeonhole, item 9 in Current Best) and
     the finite core S₀ (Finite Core Theorem). Mechanism: a window of length k₀ ≥ 2
     encodes, via the running value a_n mod L₀ (L₀ := ∏_{p ∈ S₀} p, by the certified
     Confined-GCD / Cofinite Sufficiency reduction), an S₀-residue class; there are
     only L₀ such classes, a FIXED finite number independent of k₀. If eventually
     (past some threshold) the S₀-residue class of a_n alone determines g_n (i.e. the
     "successor rule" becomes eventually a function of a_n mod L₀), then windows
     collapse to residue classes and defects vanish past the threshold — this is
     PRECISELY the already-flagged equivalence to FAH (reversible-transition-map,
     round 5, certified "S-sufficiency ⟺ V=∅ at level S₀"). **So the genuinely new
     content this approach must supply, to avoid being a mere restatement, is a
     WEAKER target that still suffices for Morse–Hedlund**: not "zero defects
     eventually" (= FAH) but "**finitely many defect WINDOWS total**, even if each one
     is visited infinitely often" — i.e. bound the number of distinct residue classes
     that ever exhibit a collision, not eliminate collisions. If only finitely many of
     the L₀ residue classes are ever "ambiguous" (produce two different next gaps at
     different visits), a modified pigeonhole (ignoring those finitely many bad
     classes, working only with the eventually-safe classes) can still force
     eventual periodicity, PROVIDED every sufficiently long run of visits eventually
     lands only in safe classes — itself a claim needing proof, not automatic.
  5. Given step 4 (however it resolves), conclude via step 2's pigeonhole + determinism
     argument, producing an explicit finite bound on both T and L₀ (hence L), and
     separately address the secondary n=1-literal gap (unresolved by any approach so
     far; out of scope for a first pass, flag explicitly).

Key lemmas (claim + mechanism):
  - **Right-Extension Determinism ⟹ eventual exact periodicity** — because two
    positions sharing an identical length-k₀ window, together with unique
    right-extension at every level ≥ k�0, forces index-by-index agreement forever by
    induction on the offset from the shared window (a one-line induction: agreement
    at position m+j implies, via unique right-extension of the length-k₀ window
    ending there, agreement at m+j+1).
  - **Finite-Defect Boundedness** (open, the real gap) — because the number of
    S₀-residue classes is finite (L₀ = ∏S₀ p, already certified), so ANY argument
    bounding "how ambiguous" the successor rule is per residue class reduces to a
    finite-alphabet question; the new idea is to COUNT ambiguity rather than
    ELIMINATE it, which is logically weaker than FAH and might be provable by a
    pigeonhole/pumping argument even where FAH itself resists — untested, this is
    the round's genuine speculative content.

Open gaps: Step 4 (Finite-Defect Boundedness, and specifically whether "finitely many
ambiguous classes" is provable when "zero ambiguous classes" (FAH) is not) is
completely open — the builder's FIRST task should be a cheap numerical check on the
existing hard seeds (a_1 = 4807, 11305, 315 — the last a fresh long-transient seed
from this round's multiplicative-lens explorer) of whether the number of DISTINCT
colliding S₀-residue classes is finite and small, as opposed to FAH's "zero
collisions" claim which already has 500+ seeds of zero-exception support. If even
this weaker count is not visibly finite/small on these seeds, retract immediately —
do not force the mechanism. Step 5's secondary n=1-literal gap is untouched.

Cases to cover: none beyond the alphabet-size argument (already handled generically).

Watch out for: (i) do not let the builder cite "Morse-Hedlund" as if invoking the
theorem's NAME proves anything — the pigeonhole + determinism argument (step 2) must
be written out in full; (ii) do not let "finite defect set" quietly become "empty
defect set" (= FAH) without flagging that this is the harder, already-dead target —
the whole point is to see if the WEAKER finite-count version is tractable; (iii) the
freshframe explorer's own complexity computation (a_1=105 plateaus at p(k)=58, a_1=4807
still slowly growing at k=20) is empirical curiosity only, not evidence either way for
step 4 — do not cite it as support.

---

### seed-coupling-induction (REVISE)

Target: same as always — prove eventual periodicity for every valid sequence (a_n),
by strong induction on k := ω(a_1) = |Q|.

Technique: strong induction on |Q|, via an AGGREGATE/existential correspondence
between a_1's instance and a reduced seed's instance — explicitly NOT the round-8
literal term-by-term positional correspondence, which was cleanly and reproducibly
falsified (a_1=105 removing p=7: stable 55% mismatch density and different limiting
type frequencies, 16/56/28% vs 25/50/25% — do not re-propose that map). This is a
genuinely different top-level strategy from FAH-direct approaches: it never tries to
pin down a single absorbing prime for a rogue pair; it tries to inherit periodicity
from a SMALLER instance of the same problem.

Skeleton:
  1. Base case |Q| = 1: fully solved already (Current Best item 10, unconditional,
     no gap) — a_{n+1} = a_n + q for all n, T=1, L=q.
  2. Inductive hypothesis: every valid sequence with seed b_1 satisfying ω(b_1) ≤ k-1
     is eventually periodic (with SOME finite T(b_1), L(b_1) — no uniform bound
     needed across all such b_1, since the induction is one-seed-at-a-time via the
     specific reduced seed constructed in step 3, not a bound-transfer over the whole
     class).
  3. **Reduction construction (open gap, the crux of the revision):** given a_1 with
     ω(a_1) = k ≥ 2, let p_k be a prime factor of a_1 and b_1 := a_1 with p_k's full
     power removed (b_1 := a_1 / p_k^{v_{p_k}(a_1)}), so ω(b_1) = k-1. Run the
     b_1-process to get its own sequence (b_n), eventually periodic by the inductive
     hypothesis with period (T_b, L_b) at core S₀(b_1).
  4. **Key Lemma A (Base-Type Correspondence, Aggregate Form — open, replaces the
     falsified positional version):** the persistent base types of a_1's Q-instance,
     restricted to those NOT involving p_k (i.e. types τ ⊆ Q \ {p_k}), correspond —
     not term-by-term, but as an unordered correspondence between persistent-TYPE
     SETS — to the persistent base types of b_1's (Q\{p_k})-instance. Mechanism to
     attempt: both processes select terms via the identical gcd-based minimality
     rule against the SAME set of primes Q\{p_k} once p_k-divisibility is
     "projected out"; the difference between the two processes is exactly whether
     p_k-divisibility is ALSO required. This is a genuinely different relationship
     than round 8's attempted map (which tried to match actual index positions n
     between the two sequences) — here we only claim the SET of persistent types
     (not their positions or frequencies) matches, which is a much weaker and
     possibly true claim even though the falsified stronger form is false.
  5. **Key Lemma B (New-Prime Pair Resolution — open, but with a concrete
     off-the-shelf gadget available):** for base-type pairs where exactly one side's
     type contains p_k, resolve FAH-for-that-pair directly using the
     already-certified Confined-GCD Lemma + Singleton-Side FAH Lemma: since only ONE
     new prime (p_k) distinguishes the two types, the "reduced-alphabet" observation
     from this round's smallcase explorer applies — D_bad (the set of possible
     "bad" gcd classes) collapses to a small, explicit finite set determined by p_k
     alone, since one side of the pair is now trivially resolved (its type is exactly
     "contains p_k", a single-prime signature). This does NOT itself close FAH for
     that pair (the smallcase explorer confirmed the residual single-class question
     is exactly as hard as the general one) — it only says the pair COUNT needing
     resolution via Lemma A's inductive inheritance is smaller than the full
     C(|𝒫|,2). Scope this honestly: Lemma B narrows bookkeeping, it does not close
     anything by itself.
  6. Combine: if Lemma A holds, all "old" pairs (not involving p_k) inherit
     resolution from the smaller b_1-instance (by strong induction); pairs involving
     p_k still need direct resolution — same open crux, but restricted to a strictly
     smaller, single-prime-parametrized family of pairs. This does NOT close FAH in
     general (be explicit: this is a reduction of scope, not a proof), but it gives a
     genuinely different inductive skeleton that could, in principle, isolate exactly
     which "new prime" cases are hard, rather than treating all rogue pairs
     uniformly.

Key lemmas (claim + mechanism):
  - **Base-Type Correspondence (Aggregate Form)** — because both processes apply an
    IDENTICAL gcd-minimality rule over the same prime set Q\{p_k}, differing only in
    whether p_k is also required; the SET of persistent types (not the positional
    sequence) is plausibly determined by the rule's prime-set alone, unlike the
    positional/frequency claim round 8 falsified. UNPROVED — first task for the
    builder is a cheap numerical check (a_1 = 105 vs b_1 = 15, and 2-3 more pairs)
    of whether the TYPE SETS (ignoring position/frequency) actually match, before
    investing in a general proof; round 8's own falsifying data (frequency mismatch)
    is about a different, stronger claim and does not automatically kill this one,
    but must be re-checked against the weaker aggregate form specifically.
  - **New-Prime Pair Resolution's D_bad collapse** — because a pair with one side's
    type containing p_k singly reduces to the already-certified Confined-GCD Lemma's
    small-alphabet recast (imported directly from this round's smallcase explorer
    finding — a genuine, provable one-line corollary of Confined-GCD + Singleton-Side
    FAH, worth certifying regardless of whether the overall induction closes).

Open gaps: Lemma A (Base-Type Correspondence, Aggregate Form) is completely open and
UNTESTED even numerically — mandatory first step before any deeper work. Lemma B's
residual single-class question is exactly the FAH wall in miniature, so even a full
proof of Lemma A only isolates, not closes, the crux.

Cases to cover: p_k with exponent 1 vs. exponent ≥ 2 in a_1 — the reduction b_1 :=
a_1/p_k^{v} removes the FULL power, so b_1 is always squarefree at p_k; verify the
inductive hypothesis genuinely applies to b_1 regardless of a_1's original exponent
(this matters per the multiplicative-lens explorer's finding that non-squarefree
seeds like a_1=315 can have much longer transients — check Lemma A's numerical test
includes at least one non-squarefree a_1, e.g. 315, not just squarefree seeds).

Watch out for: do not let this collapse back into round 8's exact falsified claim by
accident — Lemma A must be checked as an aggregate/set claim, explicitly NOT a
positional/frequency claim, and the builder must state which of the two it is testing
at every step.

---

### covering-system-construction (ADVANCE — kept for ranking continuity, the current
leader)

Target: same as always — the population's most-developed approach (9 build rounds),
carrying the full certified reduction chain (Free Facts through Collateral-Safety
Theorem) that pins the entire remaining gap to base-type-pair-level FAH/Symmetric
FAH termination.

Technique: unchanged — persistent/extended-type reconciliation via CRT + cyclic
pigeonhole, given FAH. No new mechanism is dispatched to this slug this round (all 14
mechanisms tried within this framing are dead, and round 11 explicitly bars
re-attempting any of them); it is kept live and nominated for advancement ONLY so
the reviewer's ranking has continuity with the certified reduction chain it owns
(Collateral-Safety Theorem, Canonical-Refinement Lemma, etc.), and so a builder can,
if time permits, perform the bookkeeping task of certifying this round's small
"Reduced-Alphabet Corollary" (Confined-GCD + Singleton-Side FAH ⟹ D_bad collapses to
a small explicit set when one side of a rogue pair is a singleton) as a shared lemma
importable by `seed-coupling-induction`'s Lemma B above — a real but modest task, not
a claim of progress on FAH itself.

Skeleton: unchanged from the certified reduction chain in `current.md` items 1-12;
no new steps this round.

Key lemmas: none new dispatched; import the Reduced-Alphabet Corollary (see
`seed-coupling-induction` Lemma B mechanism above) as a small certifiable byproduct
if the builder has spare capacity.

Open gaps: FAH/Symmetric FAH itself — unchanged, 14 confirmed-dead mechanisms, do NOT
re-attempt any of them (full list: existential/pigeonhole [Lemma I and predecessors],
magnitude-sandwich [Sandwich Genericity / Escape-Cost Vacuity], tautological-
minimality [Minimality Tautology Lemma], CRT-glue/competitor-construction in every
modulus variant [Minimal-Modulus Generalization], aggregate density/sieve-counting
[Density-Argument Vacuity Corollary]).

Cases to cover: none new.

Watch out for: do not let this slug's builder invent a 15th variant within the same
corridor "just to have something to do" — if there is no genuinely new mechanism and
no bookkeeping task (Reduced-Alphabet Corollary certification) worth doing, the
builder should explicitly report "no new content this round" rather than manufacture
a disguised repeat of a dead mechanism.

---

### greedy-exchange-cost-potential — QUIET this round (not in build set)

Rationale: stale (last touched round 11), its entire mechanism family (CRT-glue/
competitor-construction) is now fully closed (14th mechanism, Minimal-Modulus
Generalization), and this round's three explorers (multiplicative, smallcase,
freshframe) found no new angle specific to this slug — the smallcase explorer's
"Reduced-Alphabet Corollary" and the freshframe explorer's Morse-Hedlund idea are
both better housed in other slugs (covering-system-construction bookkeeping and the
new subword-complexity-periodicity approach, respectively). Per the workspace's own
NEVER-rule, do not dispatch a builder to this slug without a genuinely new fix in
hand; leave it registered (no Elo action) for a future round if a new angle emerges.
