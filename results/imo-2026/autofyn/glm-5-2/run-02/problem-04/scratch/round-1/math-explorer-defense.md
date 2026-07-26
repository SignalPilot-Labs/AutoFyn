# imo-2026-04 — DEFENSE route (Shan-Yu's invariant / the complement of Mulan's winning set)

Scouting the defense: for which θ can Shan-Yu keep every angle away from θ forever?
Lens owner: math-explorer-defense. Round 1 (no prior approaches; ranker returned empty).

## Exact angle transform (verified — corrects the dispatch's slightly-off form)

Triangle with angles A,B,C (A+B+C=180). Mulan picks P on side BC (WLOG which side
she cuts to the opposite vertex), cuts from P to A, splitting angle A into
α (∠BAP, the part near B) + β (∠PAC, near C), α+β=A, α,β>0. The two children:

- **child1 = △ABP**: {α, B, 180−α−B}  (the angle at P is ∠APB = 180−α−B = β+C)
- **child2 = △ACP**: {β, C, 180−β−C} = {β, C, α+B}  (∠APC = α+B)

Numerical check (A=50,B=60,C=70, α=17.3): child1=(17.3,60,102.7), child2=(32.7,70,77.3);
sums 180; the two P-angles 102.7+77.3=180 (B,P,C collinear). ✓

NOTE: the dispatch prompt wrote children as "{α,B,180−β} and {β,C,180−α}". That form is
**incorrect** (it does not sum to 180 in general). The correct third angles are
180−α−B (=β+C) and 180−β−C (=α+B). Mulan chooses which vertex to split (any of A,B,C)
and the split ratio α; Shan-Yu chooses which child survives.

## One-move both-θ force (the core algebraic fact)

Splitting angle X (one of A,B,C) into α+β=X, Mulan makes **both** children carry a θ-angle
(forcing Shan-Yu to keep a θ-triangle, hence winning next turn's check) iff:
- **X = 2θ** (then α=θ, β=θ: both children have θ at the split vertex), OR
- **θ = 90°** (the self-supplement: the two P-angles are supplementary and equal at 90°;
  split any valid angle X with α=90−B; works for every triangle, one move).

Derivation: child1 has a θ-angle iff α∈{θ, 180−B−θ}; child2 iff α∈{X−θ, θ−B}. Intersecting
the two 2-element sets gives four equations, of which two are degenerate (B=0, C=0) and
the remaining two are X=2θ and θ=90. Verified numerically for θ∈{90,60,45,30,72,100,120}.

**Consequence (SOLID): for θ ∈ (90°,180°), both-θ is NEVER achievable** — 2θ>180 (no angle
can equal 2θ) and θ≠90. So every move leaves at least one θ-free child; Shan-Yu keeps it;
the game never ends. ⇒ **All θ>90° are DEFENSIBLE.** (Initial triangle: equilateral, no
angle > 90.) This is airtight.

**θ=90° is a universal one-move Mulan win** (self-supplement, split any angle at α=90−B).
SOLID.

## Winning set — strongly supported conjecture

**Mulan wins iff θ = 180°/(2^a·3^b) for integers a,b≥0 with a+b≥1**
(i.e. θ/180 = 1/(2^a·3^b), a "3-smooth reciprocal").

Evidence (fine-grid game-tree search depth 4–5, steps up to 24, plus analytic trap verification):
- Confirmed WINS: θ=90 (n=2), 60 (n=3), 45 (n=4), 30 (n=6), 22.5 (n=8), 20 (n=9),
  11.25 (n=16). Each n here is 2^a·3^b.
- Confirmed LOSSES (no win ≤4–5 from multiple starts): θ=36 (n=5), 18 (n=10), 72 (n=2.5),
  67.5 (n=8/3), 54, 40, 80, 100, 120, 135. Each has a prime ≥5 in n's factorization
  (or non-integer n).
- The boundary n=5 (θ=36) is the key disproof of the weaker conjectures "θ=180/2^k only"
  (false: θ=60,30,20 win) and "all θ=180/n" (false: n=5,7,10 lose).

Why only primes 2 and 3 appear:
- **Factor 2**: self-supplement base θ=90=180/2; halving (eq1: angle=2θ → split at α=θ →
  both children have θ) sends n → n/2. Gives all n=2^a.
- **Factor 3**: the **3θ=180 trap** at θ=60=180/3. Splitting angle A (with an adjacent
  angle B<θ) at α=θ−B creates child1 with a 2θ-angle (third angle = 180−(θ−B)−B = 180−θ
  = 2θ since 3θ=180) and child2 with a θ-angle (immediate). Shan-Yu is forced into the
  2θ-child, then eq1 finishes. **Universal**: every non-equilateral triangle has some
  angle <60=θ (else all ≥60 ⇒ equilateral ⇒ already has θ); use it. Verified analytically
  from {36,72,72} (split 72@24 → {24,36,120} & {48,72,60}; then 120@60 → both 60) and
  from {50,50,80} (split 80@10 → {10,50,120} & {70,50,60}; then 120@60). Combining 2- and
  3-reductions gives all 2^a·3^b.

NOTE the 3-reduction for general 3|n (not just n=3) was NOT fully pinned down — the n=9
(θ=20) win line found by search used a different route (self-supplement α=90−B creating
4θ=80, then halving 80→40→20), not a clean "n→n/3" trap. The outliner must construct the
recursive offense for all 2^a·3^b. Candidate: base cases n=2 (self-supplement) and n=3
(3θ=180 trap); reductions n→n/2 (halving, needs angle=2θ=180/(n/2) which is a winning
value) and n→n/3 (a 3-trap generalizing the 3θ=180 identity, needs working out).

## Defense invariants for the complement (the route's main deliverable)

### Case 1: θ>90°. Trivial (above). SOLID.

### Case 2: θ/180 rational whose reduced denominator has a prime factor ≥5
(e.g. θ=36=180/5, 72=2·180/5, 40=2·180/9, 54=3·180/10, and θ=180/n for any n with a
prime ≥5). **Angle-group invariant.** Let G(T)=⟨A,B⟩⊂(R/180°·Z) be the subgroup generated
by the angles (C=180−A−B is redundant). Key facts:
- θ∉G(T) ⇒ no angle of T equals θ (sufficient safety this turn).
- Mulan's operations only add **2,3-smooth reciprocals** to the group: self-supplement
  introduces 180/2; the 3-trap introduces 180/3; halving introduces 180/2^a. So the group
  stays inside ⟨G(T_0), {180/(2^a·3^b)}⟩.
- Pick initial T_0 with G(T_0) cyclic of order q', where q' is an ODD PRIME ≥5 not dividing
  θ's denominator (e.g. for θ=36=180/5, take q'=7; T_0 = {180/7, 2·180/7, 4·180/7}, a
  valid triangle). Then θ ∉ ⟨1/q', {1/(2^a·3^b)}⟩ because θ's denominator has a prime
  p≥5 with p≠q', hence p ∤ q'·2^a·3^b. So θ is NEVER an angle. **DEFENSIBLE.** ✓

### Case 3: irrational θ. Angle-group invariant again.
Pick T_0 rational (e.g. equilateral). θ irrational ∉ any rational subgroup; the 2,3-
closure stays rational; θ never an angle. **DEFENSIBLE.** ✓

### Case 4 (GAP — hard): pure-2,3-dyadic NON-unit θ, i.e. θ = m·180°/2^s with m>1 odd
(e.g. θ=67.5=3·180/8, θ=135=3·180/4 [but >90, trivial], θ=45·3=135...). Here θ/180 =
m/2^s is a dyadic rational but NOT a 3-smooth reciprocal (m>1). The angle-group invariant
FAILS: θ lies in every 2,3-closure (m/2^s = c/(2^a·3^b) solvable for a≥s). Yet search
shows these are LOSSES (defensible), so a different invariant is needed.

Candidate for Case 4: **mθ-chain avoidance** — maintain "no angle ∈ {mθ : m≥1, mθ<180}".
- The chain-top (largest mθ<180) lies in (90°,180°) for any θ<90°, hence is unforceable
  (both-(top) needs angle=2·top>180). So the top can't be created ⇒ the whole chain is
  unforceable ⇒ θ never appears.
- CRUCIAL CAVEAT: this avoidance FAILS for the winning θ=60 (n=3), because the 3θ=180
  special trap CREATES 2θ=120 as a third angle without going through the chain (3θ=180
  identity). For Case-4 θ (m>1 odd, pure 2,3), there is NO kθ=180 identity with small k
  (k=180/θ = 2^s/m, not an integer for m>1), so the bypass doesn't fire. This is the
  distinguishing reason. Needs the outliner to prove no OTHER bypass exists (self-supplement
  + halving only produce 3-smooth reciprocals, and a Case-4 θ=m/2^s·180 with m>1 odd is
  NOT a 3-smooth reciprocal, so it's never produced by Mulan's 2,3-machinery — BUT sums
  like 180−α−B could in principle hit it; the outliner must rule this out, likely via the
  group/avoidance combo).

### Unifying the defense cases
The cleanest single framing the outliner should aim for: **θ is defensible iff θ is NOT a
3-smooth reciprocal of 180°.** The defense splits into the angle-group invariant (Cases
2,3: denominator has a prime ≥5, or irrational) and the mθ-chain avoidance (Case 4: pure
2,3-dyadic non-unit). Whether these merge into one clean invariant is open — possibly a
"theta is not in the multiplicative semigroup generated by {2,3} acting on 180°, AND not
a sum-product the 2,3-machinery can hit" formulation.

## Distinct openings for the outliner (rival approaches the defense route suggests)

1. **Angle-group / subgroup-of-(R/180Z) defense** (Cases 2,3): pick T_0 with cyclic group
   of prime order q'≥5 avoiding θ's denominator; prove the group stays in the 2,3,q'-
   closure, never hitting θ. Number-theoretic, clean for rational-with-prime-≥5 and
   irrational θ.
2. **mθ-chain avoidance defense** (Case 4, θ>90 trivially): maintain no-angle-in-mθ-chain;
   top is >90 unforceable; no kθ=180 bypass for non-3-smooth θ. Needs careful proof that
   Mulan's 2,3-machinery + third-angle sums can't land on mθ.
3. **Direct offense construction** (for the winning direction): recursive 2,3-smooth
   strategy — base n=2 (self-supplement), n=3 (3θ=180 trap); reductions n→n/2 (halving) and
   n→n/3 (3-trap, general form to be constructed). This is the OTHER direction (Mulan wins),
   not defense, but the defense route needs it characterized to know the boundary.
4. **Potential/Lyapunov invariant** (untried): a real-valued function of the triple that
   Shan-Yu keeps bounded away from the θ-region. Less promising than the algebraic
   group/chain invariants but worth a mention for diversity.

## Cheap-kill candidates
- θ>90°: both-θ impossible — instant defense, no machinery. (The biggest cheap kill.)
- θ=90°: self-supplement — instant one-move offense.
- θ=60°: 3θ=180 trap — two-move universal offense.
- For rational θ with a prime ≥5 in the denominator: the angle-group argument is a
  one-shot structural kill (no computation).

## Knowledge-base entries to use
- **Invariants & monovariants** (Combinatorics): the angle-group and mθ-chain are
  invariants Shan-Yu preserves.
- **Modular arithmetic, CRT / divisor analysis** (Number Theory): the prime-factorization
  structure of θ's denominator (which primes appear: 2,3 vs ≥5) is the crux of the
  characterization.
- **Kronecker equidistribution** (Number Theory): only relevant if irrational θ needs a
  density argument (it doesn't here — the rational-group invariant suffices), so likely
  not needed.
- **Vieta jumping / infinite descent** (Number Theory): possibly for the offense chain
  (descent on n = 2^a·3^b via reductions), but not clearly.
- **Casework / exhaustion** (General): the θ>90 / θ=90 / θ<90 split is natural casework.

## Analogous past problems (cruxes)
- The crux corpus has NO geometry problems (geometry subtopic not extracted), and this is
  a geometry/combinatorial-game hybrid. The closest analogues are in
  `combinatorics/games-and-strategy` and `invariants-and-monovariants`, but the specific
  structure (angle-group under a splitting operation on a triangle) is idiosyncratic.
  **None genuinely analogous** — do not force a match. (Did not run a corpus query since
  geometry is absent and the game's invariant is problem-specific; the outliner may still
  query `games-and-strategy` for invariant-game cruxes.)

## Prior progress
None (round 1, empty workspace).

## Dead ends (do not retry)
- **"θ=90° only" conjecture** (my first guess): FALSE. θ=60,45,30,22.5,20 all win.
- **"θ=180°/n for all integer n" conjecture**: FALSE. n=5 (θ=36), n=7, n=10 (θ=18) are
  LOSSES (no win found to depth 5, fine grid). Disproves the "all unit fractions" guess.
- **"All dyadic rationals θ=180·m/2^s win" conjecture**: FALSE. θ=67.5 (m=3,s=3), θ=135
  (m=3,s=2) are LOSSES (67.5 no win ≤4; 135>90 trivially defensible). Only the UNIT
  dyadics (m=1) and 3-smooth reciprocals win.
- **Coarse-grid game search** (steps≤10, depth≤4): MISSES traps — it failed to find the
  θ=60 win from {36,72,72} (the winning α=24 is off-grid). Do not trust coarse-grid
  "no win" results; use fine grid (steps≥20) or analytic trap-finding.
- **Naive "rational angles only" invariant** (the dispatch's suggested Q·180° defense for
  irrational θ): FAILS — Mulan controls the split point continuously and can introduce
  irrational angles at will. The correct irrational-θ defense is the angle-GROUP invariant
  (a discrete subgroup), not "all angles rational."

## Small-case / intuition notes (all CONJECTURE except labeled SOLID)
- SOLID: θ∈(90,180) defensible; θ=90 win in 1; θ=60 win in 2 (3θ=180 trap, universal).
- CONJECTURE: winning set = {180/(2^a·3^b) : a,b≥0, a+b≥1}. Supported by fine search +
  analytic traps for n∈{2,3,4,6,8,9,16} (wins) and n∈{5,7,10,2.5,8/3} (losses).
- CONJECTURE: defense for rational θ with denominator-prime ≥5 uses the angle-group
  invariant (cyclic group of order q'≥5, q'∤denominator); airtight on the group level,
  needs outliner to confirm the 2,3,q'-closure is exactly what Mulan can reach.
- OPEN (the hard gap): defense for pure-2,3-dyadic non-unit θ (e.g. 67.5) — angle-group
  fails, mθ-chain avoidance is the candidate but must be proven to resist all of Mulan's
  2,3-machinery including third-angle sums. n=12 (θ=15), n=18 (θ=10), n=24 (θ=7.5)
  (conjectured wins) and n=11,13 (conjectured losses) are UNTESTED — outliner should
  verify to lock the 3-smooth characterization.

## Hard gap for this route
Two things the outliner must nail:
1. **Offense closure under n→n/3**: construct the general 3-reduction trap (not just the
   n=3 base case) to prove all 2^a·3^b win. The n=9 (θ=20) search-win used a non-obvious
   route (self-supplement creating 4θ, then halving); a clean recursive n→n/3 mechanism
   is not yet identified.
2. **Defense for pure-2,3-dyadic non-unit θ (Case 4)**: the angle-group invariant can't
   reach these (they're in every 2,3-closure). The mθ-chain avoidance works for θ>45 (top
   >90 unforceable) but for θ≤45 with pure-2,3-dyadic-non-unit form (do such θ exist?
   θ=m·180/2^s, m>1 odd, ≤45 ⟺ m/2^s ≤ 1/4 ⟺ e.g. m=3,s=4: θ=33.75; m=5,s=5: θ=28.125;
   m=3,s=5: θ=16.875) the chain-top is still >90, so mθ-avoidance should hold — but the
   interaction with Mulan's 2,3-machinery (which produces 3-smooth reciprocals that could
   sum to mθ) needs a proof, not just the group argument.
