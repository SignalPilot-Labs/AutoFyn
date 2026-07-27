# imo-2026-01 — outline-reviewer report (round 1)

Reviewer start: 2026-07-23 19:44 UTC. Clean workspace, three new approaches from
the outliner. I read `current.md` (unsolved, no prior), the outliner field, the
knowledge base, and the valuation explorer. I ran numerical checks before
judging.

## Numerical sanity (Bash)

1. **Move semantics + D_p invariant + final M formula.** Simulated 5 boards
   × 50 random move orders each. Confirmed: every run terminates with exactly
   one entry >1; that entry equals ∏_p p^{D_p} (D_p = gcd of positionwise
   p-valuations, gcd(x,0)=x) in every case; D_p is invariant move-to-move, no
   violations. Boards {6,10,15}→30, {4,8,3}→6, {12,18,30}→30,
   {2,3,5,7}→210, {100,200,50,75}→150. **Core invariant claims are solid.**

2. **C1 per-prime triple joinability** (approach 3's crux). BFS over all
   valuation triples (α,β,γ)∈{0..5}³: after the two divergent moves
   (min(α,β),|α−β|,γ) vs (min(α,γ),β,|α−γ|), the two resulting triples always
   have a common reduct (215/215 triples rejoin at depth 7). **Per-prime C1
   holds.**

3. **Board-level local confluence — CRITICAL FINDING.** I tested the
   positioned-board critical pair (move(i,j) vs move(i,k), shared position) on
   all triples of values in {2..12}³: **local confluence FAILS on positioned
   boards in 72/1331 cases.** Concrete counterexample: board (2,3,2) →
   move(0,1) gives (1,6,2), move(0,2) gives (2,3,1); these two boards have
   *no common positioned reduct* (one terminates at (1,6,1), the other at
   (1,1,6) — same value M=6, different positions). So **Newman's lemma does
   NOT apply to the rewriting system on positioned boards** — the system is
   not locally confluent there. The two termini differ only in *which position*
   holds M, never in the *value* M.

4. **Multiset-level local confluence.** Reframed the rewrite on unordered
   multisets (sorted tuples): the same critical-pair test passes 1331/1331 at
   depth 6. **The confluence idea is salvageable, but only after quotienting
   positions (working on multisets).** This is exactly the C2-lift failure the
   outliner flagged as "most likely failure point" — and it is a real failure
   of the outline as written, not a nitpick.

## Verdicts

### per-prime-euclidean-invariant — APPROVE

Sound end to end. The technique (per-prime p-adic decomposition + Euclidean
identity invariant + (W,c) lex monovariant) is the right one and is
numerically confirmed. Step checks:
- L1 (move = (min,|α−β|) on valuations): correct, follows from
  v_p(gcd)=min, v_p(lcm/gcd)=max−min=|α−β|.
- L2 (D_p invariant): the engine is gcd(min(α,β),|α−β|)=gcd(α,β), the standard
  Euclidean identity — a one-liner via gcd(α,β)=gcd(α−β,β). Mechanism stated,
  correct.
- L3 ((W,c) lex strict decrease): the three-case split (i) gcd>1 & m≠n,
  (ii) gcd=1, (iii) m=n is **exhaustive and disjoint** (case iii must be
  separate because gcd>1 but c still drops — the outline correctly flags
  this). The W-drop = Ω(gcd(m,n))≥1 in case (i) is right because
  min(α,β)+|α−β|=max(α,β)≤α+β with strict drop when min(α,β)≥1 for some p,
  and summed over primes (additivity) this is the Ω(g) drop. No circularity.
- L4 (c≥1 forever): some prime has D_p≥1 initially (all entries >1);
  invariant, so c can never hit 0. Correct.
- L5 (terminal M=∏ p^{D_p}): terminal valuation list {v_p(M),0,…,0} has gcd
  v_p(M); equated to D_p by invariance. Correct.

Load-bearing lemmas all carry a stated mechanism. Gaps flagged for the builder
(Euclidean identity spelled out, sum-over-primes W-drop, lex well-foundedness,
m=n edge) are all genuine "write it out" gaps, not conceptual holes. **Both
halves present** (termination + exactly-one via c≤1 ∧ c≥1; part (b) via the
formula). This is the intended solution. Likely solves in one build.

### integer-termination-invariant-pin — APPROVE (with one note)

Sound, genuinely different in the part-(a) potential (integer product P vs
valuation-sum W). Step checks:
- M1 (P non-increasing, strict drop by factor g≥2 on non-coprime moves):
  pair-product mn=g²xy → g·xy=mn/g, so P_new=P_old/g. Correct.
- M2 (c non-increasing, case split): coprime pair → (1,mn), c drops; equal
  pair → (m,1), c drops; otherwise (g,xy) both >1, c unchanged. The crux
  "xy=1 iff m=n" is correct (lcm/gcd=1 ⟺ m|n and n|m ⟺ m=n). Case split
  exhaustive and disjoint.
- Termination by contradiction (P stabilizes ⟹ all moves coprime ⟹ c strictly
  drops ⟹ contradiction) is valid; well-foundedness of lex (P,c) is implicit
  in this argument. No factorization used in part (a) — the differentiator is
  real.
- M3 (radical support invariant): primes(g·xy)=primes(mn). Correct because
  lcm has the same prime support as the product. c≥1 follows (P>1 forever).
- M4 (D_p pin for part b): **imports L2/L5 from approach 1.** This is the
  shared-gap dependency the outliner flagged. It is not a flaw (D_p is
  verified solid above), but approaches 1 & 2 share this single point of
  failure for part (b). Worth noting, not blocking.

Gaps for the builder: write out the M2 case split explicitly, make the
infinite-run contradiction explicit, spell out the lcm-prime-support equality.
All fixable. **Both halves present.** APPROVE.

### confluence-unique-normal-form — CHANGES REQUESTED

The technique (abstract rewriting / Newman's lemma) is a legitimate,
genuinely different proof STRUCTURE for part (b) — it does not pin M with an
invariant but shows any two plays reach the same value. As a diversity hedge
against the shared D_p invariant of approaches 1 & 2 it is well-motivated.
However, **the outline as written contains a real error** that must be fixed
before the proof can be correct:

- **Fatal-as-written: step 5 (C2 lift) is false on positioned boards.** My
  numerical test (finding 3 above) shows the positioned-board rewrite is NOT
  locally confluent: e.g. (2,3,2) → {(1,6,2), (2,3,1)} have no common
  positioned reduct. The per-prime C1 is sound, but "the rejoinder moves are
  on the same three positions for every prime, so one sequence of board moves
  realizes the common reduct for all primes at once" is **not true as stated**
  — the per-prime rejoinder lands M in different positions for different
  divergent branches, so there is no single positioned board that is the
  common reduct. The outline's step 5 hand-wave is the exact failure the
  outliner worried about.

- **The fix (salvageable): reframe the rewrite on MULTISETS (quotient
  positions).** I verified (finding 4) that multiset-level local confluence
  holds for all 1331 small triples at depth 6. The problem's conclusion is
  only about the value M (position-independent), so a multiset rewrite system
  is a faithful model. The builder must: (a) define the rewrite on multisets
  of integers >1 (move picks two values, replaces by gcd and lcm/gcd, removes
  any 1s); (b) re-prove local confluence at the multiset level — either by a
  direct integer-level critical-pair computation (the multiset triple case)
  or by carefully justifying the per-prime-to-multiset lift (the per-prime
  rejoinder schedules must be shown compatible *as multiset moves*, where the
  binding constraint is relaxed because positions are unlabelled); (c) then
  invoke Newman's lemma on the multiset system to get a unique normal-form
  multiset, hence a unique value M.

- Other points are fine: termination via (P,c) is reused correctly from
  approach 2; the circularity warning (don't use uniqueness of M inside the
  confluence proof) is correctly observed; the dead "staged Euclidean-then-
  merge" framing is correctly excluded.

The core crux (C1) is numerically solid per-prime and on multisets; the
problem is purely that the outline lifts it to the wrong carrier (positioned
boards). That is a fixable gap in an otherwise right technique, not a dead
end — hence CHANGES REQUESTED, not RETHINK. I field it as the secondary,
lower-ranked rival so the part-(b) mechanism is not monocultural, with the
explicit instruction that the builder MUST use the multiset carrier, not
positioned boards. If the multiset local-confluence proof does not come
together in the build, route back to the outliner.

## Ranking (whole field, head-to-head)

All three are new at cold-start 1500; rankings below are by prospects, anchored
to the verification above.

- per-prime-euclidean-invariant > integer-termination-invariant-pin (1 is
  self-contained on both halves; 2's part (b) imports 1's invariant — 1 is
  the more direct, fully self-contained line).
- per-prime-euclidean-invariant > confluence-unique-normal-form (sound &
  gap-ready vs needs a carrier rework).
- integer-termination-invariant-pin > confluence-unique-normal-form (sound vs
  needs a carrier rework).

Applied via update_ranking. Result: per-prime 1531, integer 1500,
confluence 1469.

## Diversity note for the orchestrator

The field hedges both axes: approaches 1 & 2 share the part-(b) D_p invariant
(verified solid, not a present danger) but diversify part (a) (valuation-sum W
vs integer product P); approach 3 diversifies part (b) entirely (confluence
vs invariant pin) and is the only member not depending on D_p. No monoculture
risk this round. The shared D_p invariant is the single point of failure for
{1,2}; if a future round finds a flaw in the Euclidean identity, approach 3 is
the sole survivor — keep it alive (but it must clear the multiset hurdle
first).

build set: per-prime-euclidean-invariant, integer-termination-invariant-pin, confluence-unique-normal-form
