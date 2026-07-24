## imo-2026-04 (Mulan's Triangle Game) — new-framing lens (challenging the shared x=c−B gap)

### HEADLINE FINDING: the "algebraic collapse" gap looks illusory — a pure F-avoidance invariant
### (no transcendence machinery) appears to already close Direction III completely.

Both live approaches (and-or-closure-rank-induction, transcendence-genericity-invariant) build an
invariant S requiring "≥1 transcendental angle over ℚ(θ)" AND "no angle in F" (F := positive integer
multiples of θ below 180). They get stuck because a Shan-Yu-forced child can become **fully
algebraic while still F-free** (the x=c−B collapse), which drops out of their S because S demands a
transcendental witness.

But re-examining the already-proved **Sub-lemma B / Lemma D** inside `and-or-closure-rank-induction.md`
(and its θ>90 special case, separately CERTIFIED in `lemmas/device-classification-theta-gt-90.md`):
this lemma's proof **never uses transcendence** — it is a pure linear-algebra case check over the four
ways a split's two "new" angle slots (x, 180−x−B in child1; A−x, x+B in child2) could each equal a
multiple of θ. It shows: **if T has no angle in F (F-free) and 180/θ∉ℤ, then for every legal split at
least one child is F-free** — full stop, regardless of whether angles are algebraic or transcendental.

This is precisely a Shan-Yu-maintainable invariant with **no side condition needed beyond F-freeness
itself**. A clean strong induction on the AND–OR rank k closes it immediately:

- Base: W₀={θ∈T}. F-free ⟹ θ∉T (θ∈F) ⟹ T∉W₀.
- Step: assume every F-free triangle ∉ W_k. Let T be F-free. By Sub-lemma B, every split of T has ≥1
  F-free child; that child ∉ W_k by IH; so no split has *both* children in W_k ⟹ T∉W_{k+1}.
- Hence every F-free T ∉ W_k for all k ⟹ T ∉ W(θ) = ∪W_k.

Since F is a **finite** set (≤⌊180/θ⌋ values) for any fixed θ, an F-free starting triangle trivially
exists (e.g. two equal irrational angles chosen to avoid the finite bad list), giving Shan-Yu a
concrete surviving start for **every** θ with 180/θ∉ℤ — covering both θ>90 (already certified this
way, with F={θ} only) and the open 0<θ<90, 180/θ∉ℤ case, **in one unified argument**, with zero
transcendence bookkeeping.

**Why I think the previous two rounds missed this:** they were trying to prove a *stronger* invariant
than needed (S = F-free AND has a transcendental angle), apparently because they assumed F-freeness
alone might not survive future rounds once a child goes "fully algebraic." But Sub-lemma B's guarantee
of "≥1 F-free child" holds identically whether the triangle's angles are algebraic or transcendental —
nothing in its 4-combo case check refers to field membership, only to whether specific *values* equal
specific *multiples of θ*. The "collapse to fully algebraic" is a red herring: an F-free-but-algebraic
child is still F-free, and that is all the induction needs at every subsequent step.

### Verification performed (this round, my own checks — not yet reviewer-certified)

1. Re-derived Lemma D's 4-combo exclusion algebra by hand three times (matches the certified θ>90
   version exactly, generalized to arbitrary multiples aθ, bθ instead of just θ itself) — no error
   found.
2. Re-ran the induction argument above line by line — it is a standard AND-OR closure induction, no
   gap visible.
3. **Computational stress test** (exact `Fraction` arithmetic, no rounding): for θ ∈ {50, 72, 40,
   100/3, 220/7} (all with 180/θ ∉ ℤ), generated ~5000 random F-free triangles each, applied a random
   legal split (random vertex, random x∈(0,vertex)), and checked whether *both* children could ever
   simultaneously acquire an F-angle. **Zero counterexamples in ~25000 trials total.** This is strong
   corroborating (not proof-level) evidence Lemma D/Sub-lemma B is correct as a blanket statement.

```
theta= 50    bad= 0 / 4996
theta= 72    bad= 0 / 4999
theta= 40    bad= 0 / 4997
theta= 100/3 bad= 0 / 4999
theta= 220/7 bad= 0 / 4999
```

### Caveat / what still needs outliner+builder+reviewer scrutiny

I could be missing something the previous two rounds (and a proof-reviewer) implicitly saw and didn't
articulate crisply — this needs a fresh, careful write-up and adversarial review, not just my
recomputation. Specific things to double check when writing this up formally:
- That "F-free" (all 3 angles avoid the finite set {θ,2θ,...}) is exactly the right invariant, and
  that the induction on W_k truly terminates/covers all of W(θ) as a countable union (standard, but
  state it explicitly).
- That the starting F-free triangle construction is fully rigorous (trivial cardinality argument:
  finite bad set vs. continuum of choices) — write it out explicitly rather than "trivially."
- Double-check Sub-lemma B's case-4 exclusion (180−x−B=aθ, x+B=bθ ⟹ (a+b)θ=180) is airtight for ALL
  positive integers a,b, not just small ones — it is (pure algebra, no bound on a,b needed).
- Re-verify against the concrete "collapse" example the round-2 team worried about: T with neighbour B
  algebraic, Mulan cuts at x=mθ−B. I checked by hand: child1=(mθ−B,B,180−mθ) is F-free **exactly by
  Sub-lemma B's combo-1 exclusion** (mθ−B∈F would force B∈F, contradiction) — consistent, not a
  counterexample, just a case where the F-free child happens to be fully algebraic, which is fine.

### Distinct openings surfaced
1. **(RECOMMENDED, this report) Pure F-avoidance invariant.** Drop the transcendence requirement
   entirely; use Sub-lemma B (already written and reviewer-reviewed as individually correct inside
   and-or-closure-rank-induction.md) as the WHOLE survival engine via the k-induction above. If this
   holds under scrutiny, it **fully closes Direction III with no further machinery** — potentially
   solving the entire problem this round. This is not "routing around" the shared gap by a bypass in
   the same framing — it is showing the two rounds' framing (transcendence tracking) was solving a
   harder problem than necessary; the genuinely simpler pure-combinatorial invariant they proved as a
   *sub-step* (Sub-lemma B) was already sufficient on its own.
2. **Explicit Shan-Yu strategy, restated cleanly.** "Always keep whichever child is F-free (Sub-lemma
   B guarantees existence); if both are F-free, keep either." This is a fully explicit, constructive
   defensive strategy — no adversary-argument subtlety, no need to reason about Mulan's intentions.
   Worth stating this way in the outline for clarity/rigor (constructive strategy > existential
   invariant).
3. (Not pursued further, since #1 looks sufficient) Measure-theoretic "generic θ-free triangles form a
   full-measure invariant set" — subsumed by #1 since F-avoidance doesn't need measure/genericity at
   all, just finiteness of F.
4. (Not pursued) A monovariant/potential distinct from F-avoidance — unnecessary if #1 holds; F-freeness
   itself already IS the right monovariant (a boolean invariant, not a strictly-decreasing potential,
   but functions the same way: "stay in the safe region forever").

### Candidate technique(s)
AND–OR game-tree closure induction (standard combinatorial game theory) + a purely algebraic
finite-case exclusion lemma (Lemma D / Sub-lemma B, already drafted, reviewer-reviewed as correct in
isolation). No field theory / transcendence degree needed.

### Cheap-kill candidates
- **Finiteness of F.** F(θ) has at most ⌊180/θ⌋ elements — a trivial pigeonhole fact that immediately
  gives existence of an F-free starting triangle (2-dimensional continuum of triangles minus finitely
  many bad affine slices). Use this instead of invoking transcendental numbers/ℚ(θ) at all.
- Parity/valuation arguments: not needed, not applicable here (already correctly ruled out by round 2).

### Knowledge-base entries to use
- Invariants & monovariants (combinatorics section) — but note: the needed invariant is a simple
  finite-avoidance set membership, not a measure/transcendence-flavored one. Cite this KB entry for
  the general proof pattern ("show a property survives every adversary move ⟹ survives forever"),
  not for any specific machinery.
- AND-OR game / adversary-argument pattern — already used correctly by the certified normal-form
  lemma; continue using it as the game-theoretic skeleton.

### Analogous past problems (cruxes)
Consistent with round-2's finding: `aimo-0236` (two-phase invariant, defender stays one step ahead
via a witness) is a structurally relevant template for *how to write* a defender-maintains-invariant
proof, but do not import its specific p-adic content — here the "witness" is simply membership in the
finite complement of F, nothing p-adic. `aimo-0445` (fork/double-threat pattern) matches Mulan's
"seed a multiple then peel" attacker-side construction (already used, ⊇ direction), not the defender
side. No closer geometry-forcing-game crux exists in the corpus (confirmed again this round).

### Prior progress
Per `current.md`: ⊇ direction (θ=180/m ⟹ Mulan wins) and θ>90 impossibility are both COMPLETE and
CERTIFIED. The claimed open gap is Direction III (0<θ<90, 180/θ∉ℤ ⟹ Shan-Yu survives). This report's
finding: the gap may already be closed by material the field already produced (Sub-lemma B /
Lemma D) — it just needs to be **used directly** (as a pure F-avoidance invariant) instead of being
folded into an unnecessarily strong transcendence-based invariant S. If the outliner/builder confirms
this, Direction III becomes COMPLETE and the whole problem is SOLVED this round.

### Dead ends (do not retry)
- Building a transcendence-degree / field-genericity invariant (S = F-free AND has a transcendental
  angle) — this is what stalled both live approaches for 2 rounds on the x=c−B collapse. The collapse
  is only a problem for THIS stronger invariant, not for plain F-avoidance. Do not re-attempt
  patching S with a "safe algebraic set 𝒞(θ)" — likely unnecessary complexity; try the simpler
  invariant first.
- The dyadic/90-halving invariant (explicit-shanyu-peel-potential) — already correctly RETHINK'd,
  confirmed false, do not revisit.
- {90/n} as the answer — already disproven (θ=60 is a 2-move win), settled, do not revisit.

### Small-case / intuition notes (conjecture unless marked proved)
- **Proved (algebra, hand-checked 3×) + strongly corroborated (25000 random-trial computation, zero
  counterexamples):** for any θ with 180/θ∉ℤ, F-freeness is a Shan-Yu-maintainable invariant against
  every legal Mulan split. This directly implies Direction III via the standard W_k induction.
- If this holds, the full answer θ=180/m (m∈ℤ, m≥2) is completely settled with all three directions
  (⊇, θ>90, and 0<θ<90/180-θ∉ℤ) unified under one clean AND-OR / finite-avoidance argument — no
  transcendence, no genericity, no measure theory needed anywhere in the proof.
