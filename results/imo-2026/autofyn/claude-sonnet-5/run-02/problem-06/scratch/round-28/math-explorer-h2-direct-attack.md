## imo-2026-06 (H2 "direct N(S_0)=0 attack" lens)

- **Headline finding: this is NOT a fresh, untried angle — it was already tried
  (round 23, `direct-s0-self-absorption`) AND already proven, by a certified
  general theorem, to be structurally unresolvable by any finite-data/numeric
  method (round 19, `core-growth-monotonicity`, Proposition 3 "Non-
  Constructivity of `M_B`"). Round 27's Rules-file phrasing ("H2's untried
  direct N(S_0)=0 attack") is a stale/inaccurate characterization that the
  outliner should NOT act on as if it were a fresh lever. My new large-scale
  simulations (below) are consistent with, and reinforce, this
  already-certified impossibility rather than opening a new door.**

### What "N(S_0)=0 direct attack" actually means and what's already certified

- H2 (per the certified **Termination Criterion Lemma**,
  `lemmas/termination-criterion-lemma.md`) is precisely: does the absorption
  chain `S_0 ⊆ S_1 = S_0⁺ ⊆ S_2 = S_1⁺ ⊆ ...` (where `S⁺ := S ∪
  ⋃_{j≤N(S)}P(a_j)`) reach a fixed point in finitely many steps? Equivalently,
  is `(N(S_k))_{k≥0}` bounded? Each individual `N(S_k)` is already PROVEN
  finite (Extended Persistent-Type Pigeonhole, generic in any finite core) —
  what's open is boundedness of the whole sequence as `k→∞`, i.e. whether the
  core-enlarging process ever stops needing to enlarge.
- The "direct `N(S_0)=0`" framing (round 23's `direct-s0-self-absorption`
  approach) is the special case asking whether `S_0` (or the round's `S_0' :=
  S_0 ∪ ⋃_{j≤N_0}P(a_j)`) is ALREADY self-absorbing, i.e. `k=0` suffices with
  zero further enlargement rounds. Round 23 built this out in full and found:
  (a) it reduces to exactly the `M=N_0` instance of the already-certified
  **Monotone Chain Reformulation Lemma** — no new leverage; (b) the only
  natural mechanism for proving containment (**Bounded Witness Lemma**) is
  PROVEN insufficient (certified `lemmas/bounded-witness-insufficiency-for-
  containment.md`): it only supplies existence of ONE shared prime, never
  absence of extra primes, and these are logically independent facts; (c) a
  fresh 20,500-term simulation on both hard seeds (4807, 11305) showed new
  never-before-seen extended-`S_0`-types still arriving in the final 5% of the
  window — directly contradicting the round-17 "N(S_0)=0 on 9/9 seeds" premise
  that had motivated optimism (that premise was a terminology collision: its
  `S_0` was `Q`, not the Finite Core Theorem's enlarged core).
- **Deeper, more decisive fact (already certified, round 19,
  `core-growth-monotonicity` Proposition 3, "Non-Constructivity of `M_B`",
  which applies verbatim to `N(S)` itself):** for ANY finite core `S` and any
  candidate bound `K`, the observed data up to index `K` is logically
  consistent with BOTH "the process has already stabilized" and "a currently-
  singleton extended type will recur arbitrarily far beyond `K`, pushing the
  true threshold arbitrarily high." This is a genuine diagonal/two-consistent-
  extensions argument (not an empirical difficulty) proving that **no finite
  amount of simulation, however large, can ever certify `N(S_0)=0`, or any
  specific finite bound on `N(S_0)`, or its negation** — a "singleton-so-far"
  type observed near the tail of a window could equally be (i) a genuinely
  non-recurring transient exception (contributing to `N(S_0)`) or (ii) a
  rare-but-truly-persistent type that will recur far later (contributing
  NOTHING to `N(S_0)`, since persistent types never count as exceptions no
  matter how sparse). These two scenarios are indistinguishable from any
  bounded prefix. This is a certified, general theorem, not a conjecture.

### New numeric experiments this round (large scale, 3 seeds, own fresh script)

I wrote an efficient exact greedy simulator (bitmask/big-integer coverage
check: for each prime `p`, maintain a big-int bitmask of which prior indices
`p` divides; test candidate `c` by OR-ing the bitmasks of `c`'s own prime
factors and checking the union covers all prior indices — this made ~750k-term
exact simulations feasible in under 5 minutes, a substantial scale-up from
round 23's 20,500 terms). Then computed the base-Q-persistent types, the
Finite Core Theorem's `S_0` (canonical witnesses = first occurrence of each
persistent base type), and tracked new-extended-`S_0`-type arrivals over the
whole window.

Results (own from-scratch script, `/tmp/h2experiment/sim.py` +
`analyze.py`):

| seed | terms simulated | `S_0` reproduced | distinct extended types | last new-type arrival | decile arrival counts |
|---|---|---|---|---|---|
| 4807 | 751,730 | `{2,3,5,7,11,19,23,73,127}` (exact match to round 23's independently-verified value — confirms my methodology is correct) | 216 | n=734,249 (**97.67%** of window) | 162,15,10,5,5,8,5,0,3,3 |
| 11305 | 700,000 | `{2,3,5,7,13,17,19,23,29,37,43,101}` (exact match to round 23) | 794 | n=698,797 (**99.83%** of window) | 440,89,64,47,37,33,25,21,19,19 |
| 105945 | 400,000 | `{2,3,5,7,11,13,19,29,43,101,109,163,883,1009}` (new, not previously computed at this seed to my knowledge) | 571 | n=397,316 (**99.33%** of window) | 322,59,39,32,26,25,16,22,17,13 |

Conjectural observations (numeric evidence only, NOT proof, consistent with
round 25's honest "deceleration but not termination" finding, now at ~15-35x
the previous window size):
- On all three seeds, new extended-`S_0`-types keep arriving essentially all
  the way to the edge of a 400k-750k-term window (97.7%-99.8%), i.e. the
  literal target "`N(S_0)=0`" (or even "`N(S_0)` < some specific bound visible
  in a window this large") is **not observable as true** at this scale, on any
  tested seed — the deceleration never visibly reaches zero.
- 4807's decile counts (162→...→0,3,3) look like a genuinely decaying-toward-
  small tail; 11305's (440→...→19,19) look concerningly close to *flat* in the
  last few deciles rather than continuing to decay — this is new, sharper
  evidence than round 25 had (round 25's own data was more limited) that for
  11305 specifically, the arrival rate MAY be leveling off at a slow-but-
  nonzero rate rather than genuinely tapering to zero; this is exactly the
  kind of ambiguity Proposition 3 predicts is undecidable from any finite
  window — pushing to 5M or 50M terms would very likely show the same
  qualitative ambiguity, not resolve it, per the certified impossibility
  above.
- 105945 (previously flagged inconclusive at round 21 for a different,
  literal-period metric) shows its BASE-level persistence threshold `N_0`
  itself only stabilizing at n≈330,873 (82.7% of a 400k window) — a much later
  base-level stabilization than 4807/11305 (both `N_0=0`), underscoring how
  seed-dependent even the *first* pigeonhole threshold is, and how easily a
  seed can look "still transient" deep into a large window.

### Is there a genuinely new mechanism worth a build slot?

No concrete new mechanism was found. Two considerations:
1. **Any mechanism that only reads finite-prefix numeric data (however much)
   is already proven unable to resolve `N(S_0)=0`, or any instance of the
   Monotone Chain family's `∃M: N(S_M)≤M` target, by the certified
   Non-Constructivity result** — so no amount of further simulation (even at
   1M-10M terms) should be dispatched as if it could settle this; it can only
   ever produce "no violation observed yet," which is already the state of
   the art since round 21-25.
2. The only way past this in principle is a mechanism that does NOT reduce to
   reading a bounded prefix — e.g. an actual invariant / well-ordering /
   compactness-style argument giving CONTROL over the tail without observing
   it. `core-growth-monotonicity` (round 19) explicitly checked the two most
   natural such routes (rate-control via the Threshold Recursion Bound Lemma;
   monotonicity of self-absorption under enlargement) and both failed with
   proofs, not just search. No third structural candidate is currently on the
   table anywhere in the workspace, and this round's search did not surface
   one either — I looked for (and did not find) any approach or lemma
   attempting the alternative reframing "is `S_∞ := {primes dividing
   infinitely many a_n}` finite?" (a static, non-adaptive-chain rephrasing of
   H2's existence question); this MIGHT be a genuinely different target
   (sidesteps having to guess a finite core from a prefix at all), but I did
   not find time to check it for hidden circularity (it may just relabel the
   same non-constructive pigeonhole quantity) — flag as a *possible* fresh
   angle for a future round to pre-screen (per the round-5
   `reversible-transition-map` precedent: check for disguised equivalence
   BEFORE spending a build slot), not as something ready to build now.

### Recommendation

**Park H2's "direct N(S_0)=0" attack — do not dispatch it again as if it were
untried.** It has been tried (round 23) and the underlying finite-data
mechanism class it belongs to has been proven, in general, incapable of
resolving H2 (round 19's Non-Constructivity theorem). My new 400k-750k-term
simulations do not change this: they are consistent with (not contradicting)
the certified impossibility, and give a somewhat sharper (still inconclusive,
by design unresolvable) picture of deceleration-vs-plateau on the three
tested seeds. If a math-explorer wants to keep pushing on H2 next round, the
only defensible options are (i) pre-screen the `S_∞`-finiteness reframing for
non-circularity before proposing a build, or (ii) accept H2 (like H1) as a
practical ceiling and continue banking subfamily-theorem APPROVEs
(`a1-pq` extensions, `a1-9q`/`a1-11q`, etc.) as the run's floor deliverable,
per round 27's priority (b)/(c).

### Candidate technique(s)
None concretely viable for H2 right now. If pursued: a genuinely
non-finite-data structural argument (invariant/monotonicity/compactness) for
absorption-chain termination — not another prefix simulation or
Bounded-Witness-style presence argument (both classes now provably
insufficient).

### Cheap-kill candidates
None new. (Existing cheap kill already applied: Bounded Witness Lemma cannot
give containment — certified, `bounded-witness-insufficiency-for-
containment.md`.)

### Knowledge-base / lemma entries used
`lemmas/self-absorbing-core-theorem.md`, `lemmas/termination-criterion-
lemma.md`, `lemmas/monotone-chain-reformulation-lemma.md` (inside
`approaches/core-growth-monotonicity.md`), `lemmas/bounded-witness-
insufficiency-for-containment.md`, `lemmas/extended-persistent-type-
pigeonhole.md`, `lemmas/unbounded-total-prime-support-theorem.md` (confirms
raw prime support is unconditionally unbounded but does not itself refute
H2 — self-absorption only needs a finite recurring TYPE pattern at a fixed
core, not zero further primes ever).

### Analogous past problems (crux corpus)
Not applicable to this lens — this was an internal-mechanism/numeric audit of
an already-explored H2 sub-question, not a new-problem-framing search; no
crux-corpus query was needed or would be informative here (the obstruction is
workspace-internal, proven from this problem's own certified lemmas, not a
missing external technique).

### Prior progress
`direct-s0-self-absorption` (partial): Propositions 1-3 certified/complete
(reduces to Monotone Chain family at `M=N_0`; Bounded Witness Lemma proven
insufficient); H2 existence hypothesis itself untouched.
`core-growth-monotonicity` (partial): Binary Refinement Lemma, Threshold
Recursion Bound Lemma, Non-Constructivity of `M_B` (Prop 3), Monotone Chain
Reformulation Lemma, Non-Monotonicity Gap (Prop 5) — all certified/complete;
H2 existence itself untouched, and Prop 3/Prop 4 jointly prove no
bounded-prefix mechanism can ever close it.

### Dead ends (do not retry)
- Literal "`N(S_0)=0`" or "`N(S_0')≤N_0`" as a provable target via Bounded
  Witness Lemma or any presence-only mechanism (round 23, certified
  insufficiency).
- Rate-control on `N(S_M)` via one-prime-at-a-time refinement (round 19,
  Threshold Recursion Bound Lemma + Non-Constructivity, certified dead).
- Assuming self-absorption is monotone under core enlargement (round 19,
  Proposition 5: not established, and no route to establish it currently
  known).
- Any further large-N direct simulation aimed at literally proving/refuting
  `N(S_0)=0` or a specific bound — provably cannot succeed regardless of scale
  (round 19 Prop 3); useful only as descriptive/qualitative evidence, not as a
  path to resolution.

### Small-case / intuition notes (all conjectural, not proof)
- On all 3 tested seeds (4807, 11305, 105945), new extended-`S_0`-types keep
  arriving up to 97.7%-99.8% of very large windows (400k-750k terms) —
  qualitatively consistent with round 25's "deceleration, not termination"
  finding, now confirmed at much larger scale.
- 11305's decile arrival counts (440,89,64,47,37,33,25,21,19,19) look close to
  flattening near ~19-20 per 70k-term decile in the tail rather than
  continuing to decay toward 0 — mild evidence (not proof, and per Prop 3
  provably unresolvable by any amount of further simulation) that this
  particular seed's arrival rate might not even be heading to zero, which
  would be evidence AGAINST H2's existence hypothesis for this seed, though
  this cannot be confirmed or refuted by simulation in principle.
- Seed 105945 shows that even the base-level (`Q`-level) persistence
  threshold `N_0` can itself take a large fraction (82.7%) of a 400k-term
  window to stabilize — a caution that "looks stable so far" at the base
  level is a weak/unreliable signal for harder seeds, reinforcing that H2 is
  seed-sensitive and its numeric picture is not close to settled even at
  700k-750k terms.
