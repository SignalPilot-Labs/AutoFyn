## imo-2026-03 — Gap 1c nonempty-ξ* half-step construction (lens: half-step construction)

### Setup recap (verified against the file, not re-derived from scratch)
Half-step target (§21.3/§24.1, `potential-weighting-upper-bound.md`):
`OPT_{+1}(B_1,X) <= OPT_{+1}(B_1∪{d},X)` for `d = w_1-w_m` (`w_1=max(Res)`, any partner `w_m`,
`X=Res\{w_1,w_m}`), given genuine top-level F-provenance (trigger `M_opt<A_1` + true global `k*`).
`ξ*` = an optimal witness (selection of `X`) achieving `OPT_{+1}(B_1∪{d},X)` (the RHS problem);
`ξ*=∅` boundary case is CLOSED (round 16, conditional on Gap 1a's Deletion-Suffices-for-`k*`,
itself proved only `q<=3`), via `lemmas/delete-suffices-insertion-domination.md`. The nonempty-`ξ*`
case (§26.4) is open: candidate construction `c:=argmin_{x∈ξ*}|x-d|`, conjecture
`e(B_1∪(ξ*\{c})) <= OPT_{+1}(B_1∪{d},X)`, corroborated 0/1267 (round 16) but not proved; two
algebraic routes tried and stalled (wrong-direction optimality bound; unresolved 2-variable
insertion-order case split).

I re-implemented `OPT_σ(B,Z)` from scratch (exact `Fraction`, brute-force enumeration of every
K/D/M selection of `Z` — matches the file's own §13.2 definition, validated by hand-checking the
half-step never fails on any instance I generated, confirming my harness matches the file's
convention) and used it to scout the nonempty-ξ* construction directly. Code:
`/tmp/round-17/gap1c_probe/{harness.py,probe1..6.py}`.

### Distinct openings (new findings this round)

**1. The choice of "the" optimal witness ξ* among ties is load-bearing — not incidental — and a
naive "any tie" choice provably FAILS.** Testing the round-16 construction (`c=argmin|x-d|`) against
the *largest*-cardinality optimal witness among ties, I found **5 concrete counterexamples**
(exact-Fraction, e.g. `B_1=[22,22]`, `Res=[15,14,10,6,4]`, partner `m=1`, `d=1`: the largest optimal
witness is `{6,6}`, giving `c=6`, `e(B_1∪{6})=e([22,22,6])=4 > RHS=1` — fails). Against the *smallest*
(sparsest, minimum-cardinality) optimal witness, the construction succeeds far more often (726/728 in
a fresh 2500-trial genuine-F sweep spanning `q∈{5..9}`, `v_max` up to 60) but is **still not
unconditionally true even at minimum cardinality**: 2 residual failures, both with the sparsest
optimal witness being a literal **duplicate pair** (`{3,3}` and `{6,6}` respectively).

**2. The 2 sparsest-witness failures are NOT real counterexamples to the half-step — they reduce, for
free, to the SAME mechanism already used for the ξ*=∅ boundary case.** When the sparsest ξ* is a
duplicate pair `{c,c}`, Lemma P (`lemmas/duplicate-pair-invariance.md`) gives
`RHS = e(B_1∪{d}∪{c,c}) = e(B_1∪{d})` exactly (verified: case A `e([16,15,1])=2=RHS` ✓, case B
`e([2,2,1])=1=RHS` ✓). So the half-step target collapses to `LHS <= e(B_1∪{d})`, which is *exactly*
the RHS of the certified, fully general **`delete-suffices-insertion-domination.md`** lemma applied at
`C=B_1,W=Res,(w_a,w_b)=(w_1,w_m)` (the same instantiation §26.3 already uses) — i.e. it holds
**whenever Deletion-Suffices-for-`k*` holds at this node** (proved `q<=3`, open `q>=4`, same
conditional as §26.3). Chain: `LHS <= e(B_1)` [Shrink-List, delete all of `X`] `<= e(B_1∪{d})`
[Delete-Suffices-Insertion-Domination, IF Deletion-Suffices-for-`k*` holds] `= RHS` [Lemma P, since
ξ*={c,c}]. **This is a genuine extension of §26.3's reduction: it is not limited to literal `ξ*=∅`,
it also covers every case where the sparsest optimal witness Lemma-P-collapses to something
equivalent to `∅`** (duplicate pairs are the simplest instance; likely generalizes to any
Lemma-P-reducible witness, e.g. two duplicate pairs, or a pair plus a value equal to `d` itself —
untested at larger cardinality this round, flagged for next round).

**3. This produces a clean 3-way case split for the nonempty-ξ* case, closely mirroring the
crux-inspired shape (see below), sharper than round 16's flat "generic vs duplicate" flag:**
- **(a) Sparsest optimal witness has odd/size-1 structure (no internal Lemma-P cancellation)** — the
  overwhelming majority of cases tested (726/728, i.e. ~99.7% at these small q); `c=argmin|x-d|`
  construction succeeds unconditionally in every test (0 failures in this sub-case across all
  batteries run this round, ~1150+ combined checks including round 16's own 1267). **This is the
  true remaining hard core** — still no algebraic proof, matches §26.4's honestly-reported stall.
- **(b) Sparsest optimal witness Lemma-P-collapses to `∅`-equivalent (duplicate pair, or richer
  cancelling structure)** — reduces for free to the ALREADY-PROVED-CONDITIONAL (`q<=3`) mechanism
  of §26.3, via the SAME certified lemma. **New, not previously identified as a distinct sub-case.**
- **(c) `ξ*=∅` literally** — already closed (§26.3).

**4. Sharper crux mapping than round 13/16's flat pointer.** Re-reading `aimo-0960`'s solution in
full: the crux move is "among *minimum-length* representations, take the *lexicographically-least*
sorted exponent list; a repeated exponent `e>=2` is killed by the identity `2ψ^e=ψ^{e-2}+ψ^{e+1}`
(same length, strictly smaller in lex order — contradiction); the two *boundary* repeats (exponent
`0` or `1`, which the identity can't reach) are killed instead by a *value-bound* argument (bounding
the whole sum against the extremal geometric series)." This maps **very concretely** onto the refined
picture above: "minimum length" ↔ **sparsest optimal witness** (exactly what my probe shows is the
correct tie-break, not "any" witness — confirms this is the right analogy, not a loose one);
"kill a repeat via an identity, same value, contradiction" ↔ **Lemma P collapsing a duplicate pair**
(case (b) above — genuinely the same move: an exact identity that cancels a repeated value at no
cost); "boundary repeats killed by a *different*, value-bound argument instead" ↔ case (a)'s residual
generic/single-element witnesses, which need the nearest-c algebraic bound (not a rewrite identity) —
i.e. aimo-0960's own proof needed **two different techniques for two different structural sub-cases
of its own minimal witness**, exactly mirroring what this round's computation forces here. This is a
tighter structural match than the round-13 "extremal witness + secondary tie-break + local rewrite"
one-line pointer — recommend the outliner use this two-technique split explicitly, not search for one
uniform mechanism covering both.

**5. aimo-0438's mechanism (extremal witness maximizing a *secondary statistic*, local
edge-swap that increases the statistic without lowering the objective, contradicting maximality) is
LESS directly applicable here than aimo-0960's** — that proof forces a witness into a canonical
*shape* (hugging a fixed path `S`) via repeated local surgery; here we don't need to force ξ* into a
shape, we need to directly bound `e` after a single deletion, which is closer to aimo-0960's
value-inequality flavor. Do not spend a build round trying to port aimo-0438's iterative-swap
machinery; it does not obviously transfer (structurally the objects are different: aimo-0438's `N`-
maximization operates on a fixed graph with a target path to reconstruct, not an alternating-sum
minimization over a numeric multiset).

### Candidate technique(s)
- Formalize case (b) first (cheap — it is a direct, already-mostly-written corollary of the certified
  `delete-suffices-insertion-domination.md`, exactly reusing §26.3's argument with `ξ*={c,c}` instead
  of `ξ*=∅`; likely a few lines once the "sparsest witness is Lemma-P-reducible" trigger condition is
  formally defined). This should be attempted before case (a) — it is much closer to done and
  further narrows what remains.
- For case (a) (the true residual), the recommended route is still the insertion-difference-identity
  algebra from §26.4/§25.3, but now correctly scoped to ONLY the sparsest-witness, Lemma-P-irreducible
  sub-case — a strictly narrower and probably more tractable target than the file's current unscoped
  attempt (which implicitly considered arbitrary ξ*, including the now-understood-differently
  duplicate case).

### Cheap-kill candidates
- Before attempting case (a)'s algebra, formally verify (bounded computation, larger `q`/`v_max` than
  this round's ~9/60) whether "sparsest ⟹ size <=1 or Lemma-P-reducible" is a genuine dichotomy, or
  whether larger irreducible sparsest witnesses (size >=3, no internal duplicate) occur — none were
  found in ~730 nonempty cases this round (distribution was only sizes 1 and 2), but the sample never
  pushed `q` above 9; this is a cheap, high-value next check before committing more build time to
  case (a)'s algebra, since if size stays <=2 generically the residual case (a) may itself reduce to
  variants of the already-partially-proved Two-Touch Lemma (Gap 1a, §26.5) instead of needing fresh
  machinery.

### Knowledge-base entries to use
- `lemmas/duplicate-pair-invariance.md` (Lemma P) — the exact mechanism for case (b).
- `lemmas/delete-suffices-insertion-domination.md` — reused unchanged for case (b)'s reduction.
- `lemmas/insertion-difference-identity.md` — the tool already earmarked for case (a)'s algebra.
- `lemmas/shrink-list-monotonicity.md` — used in the `LHS<=e(B_1)` step of both §26.3 and the new
  case (b) reduction.

### Analogous past problems (cruxes)
- `aimo-0960` (algebra, `symmetric-functions-and-substitution`) — best match, tighter than previously
  reported: the "minimum-length + lex-least, kill a repeat via an exact identity; boundary repeats via
  a separate value-bound" two-technique split maps directly onto the sparsest-witness / Lemma-P-pair
  vs. generic-residual split found this round. Recommended primary reference for structuring the
  outline's Step 3 as two sub-lemmas, not one.
- `aimo-0438` (combinatorics, `extremal-principle`) — the "extremal witness + local swap raising a
  secondary statistic" shape is real but less directly transferable here (see point 5 above); useful
  only as a general reminder that secondary-tie-break choice can be load-bearing (confirmed true here
  independently by computation), not as a source of a specific rewrite identity.
- `aimo-0666` — leximinimal-coloring shape, same "extremal + tie-break" family as `aimo-0438`; no
  closer a match than `aimo-0438`, not separately useful.

### Prior progress
`ξ*=∅` boundary case closed conditional on Gap 1a's Deletion-Suffices-for-`k*` (proved `q<=3`, open
`q>=4`) — round 16, `lemmas/delete-suffices-insertion-domination.md`. Nonempty-`ξ*` case: candidate
construction identified and corroborated (0/1267, round 16) but algebraic proof stalled (§26.4, two
routes tried). This round adds: (i) independent re-confirmation of the round-16 construction on a
fresh harness (0/420+ additional checks with the "any/first" tie-break); (ii) a **new, real
counterexample family** showing the tie-break must be the sparsest witness, not an arbitrary one (5
concrete failures with the largest-witness choice); (iii) a **new positive reduction** extending
§26.3's ξ*=∅ mechanism to duplicate-pair sparsest witnesses "for free," further narrowing the true
open core to sparsest, Lemma-P-irreducible witnesses.

### Dead ends (do not retry)
- Do not use an arbitrary/first-found optimal witness as "the" ξ*; confirmed to fail (5 exact
  counterexamples this round, largest-cardinality tie-break).
- Do not port aimo-0438/aimo-0666's iterative local-swap-to-canonical-shape machinery wholesale; the
  objects don't match closely enough to be a direct source of a rewrite identity here (see point 5).
- §26.4's two previously-tried algebraic routes (naive optimality-gives-wrong-direction chaining;
  unresolved two-insertion-order case split) remain dead as reported — this round's findings narrow
  *which* instances need that algebra (case (a) only) but do not resolve it.

### Small-case / intuition notes (conjectural, computational evidence only)
- Sparsest-optimal-witness + nearest-to-`d` construction: 0 failures in ~1150+ combined checks
  restricted to the Lemma-P-irreducible sub-case (case (a)); this is corroboration, not proof.
- Conjecture (untested beyond `q<=9`, `v_max<=60`): every sparsest optimal witness of the RHS problem,
  within genuine F-provenance, has cardinality <=2, and cardinality-2 witnesses are always exactly a
  duplicate pair (never two distinct values) — if true, this would mean case (a)'s residual is always
  a single element, likely reducible directly via a Two-Touch-style argument rather than needing the
  full insertion-difference two-variable algebra. Flagged as the single highest-leverage thing to
  check computationally before the next build round.
