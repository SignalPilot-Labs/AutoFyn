## imo-2026-06 — lens: periodicity-from-n=1

### Headline finding
Round 2's negative result ("no-pre-period shortcut fails for a1=35,65") is an
artifact of testing with the WRONG covering set (`H=rad(a_1)`, guessed, as the
reviewer note already flagged). Using the CORRECT/true covering set (computed
directly from the actual generated sequence via a "minimal-radical antichain"
frontier, not guessed from `a_1` alone), I re-ran the exact same test — with a
bug-fixed simulator — on 7 distinct examples (`a_1 = 15,35,65,105,143,221,1001`,
covering both trivial/Case-I and genuine Case-II instances) and found **zero
exceptions**: not only does periodicity hold from `n=1` in every case, but the
finer diagnostic (below) shows the two "obstructions" flagged in Theorem 2.4's
Part 3 (`Σ_n ≠ Σ_∞` for small `n`, and a possible transient before the residue
orbit enters its cycle) **do not actually manifest** in any tested example, even
though `Σ_n` genuinely is a strict subset of `Σ_∞` at `n=1` in every case. This
substantially reopens Gap 2 as tractable and reframes exactly what needs proving.

### Distinct openings
1. **"Gap is a pure function of `a_n mod L` from n=1" (empirical law).** For
   each of the 7 examples (true `T,L` found by tail-matching the *actual*
   greedy sequence, no `H` needed for this test), I checked whether
   `a_{n+1}-a_n` depends only on `a_n mod L`, testing every occurrence of a
   repeated residue across ~4000-6000 simulated terms. **Zero violations** in
   all 7 cases. Moreover the number of *distinct residues visited* over the
   whole run exactly equals `T` in every case — meaning the orbit is a pure
   cycle from the very first term, with **no transient states at all** (if
   there were a pre-period, distinct-residues-visited would exceed `T`). This
   is a sharper, more direct target than "does `a_{n+T}=a_n+L` hold from
   n=1" — it is the literal residue-dynamics statement whose proof would
   settle Gap 2 outright, assuming `L` (i.e., a finite covering set) is known.
2. **The precise "coincidence lemma" to prove (localizes Gap 2 exactly).**
   Using `H` = the true, empirically-computed covering set (union of primes in
   the minimal-radical antichain / "frontier" of `{rad(a_i)}` after it
   stabilizes — NOT `rad(a_1)`), and `Σ_n`/`Σ_∞` exactly as defined in
   Theorem 2.2/2.3 (`intersecting-family-covering-construction.md`), I
   directly compared `min{x>a_n : x hits Σ_n}` vs. `min{x>a_n : x hits Σ_∞}`
   for `n=1,...,15` in 4 Case-II examples (`a_1=35,65,105,143`). Result:
   **exact equality in every single case tested (60/60 checks)**, including at
   `n=1` where `Σ_1` is a proper subset of `Σ_∞` (e.g. for `a_1=35`,
   `|Σ_1|=1` vs `|Σ_∞|=8`). This is the exact statement that, if proved in
   general, collapses BOTH of Theorem 2.4 Part 3's obstructions at once
   (`N_1=1` effectively bypassed since the *weaker* rule already agrees with
   the eventual rule, and no separate dynamical transient survives either).
   **This is the single cleanest target for the outliner to hand to a
   builder**: "prove `min{x>a_n: x hits Σ_n} = min{x>a_n: x hits Σ_∞}` for
   every `n≥1`, given `H` finite" — strictly sharper than the vague
   "periodicity from n=1" gap statement currently in `current.md`.
3. **Structural analogue from the crux corpus: aimo-0577's permutation trick.**
   IMO-SL-style problem (Croatia, greedy `x_{k+1}=x_k+d` or `x_k/a`) proves
   "no pre-period" for its greedy orbit via: (i) confine the state to a finite
   invariant set `S` (via a boundedness argument), (ii) show the transition
   map `f:S→S` is **injective** by exhibiting an explicit inverse on each
   branch, hence `f` is a permutation of the finite set `S`, hence **every
   point's forward orbit is immediately periodic — no pre-period possible for
   ANY starting point of a permutation**. This is structurally the right
   *shape* of argument for our Gap 2 (if `G:\mathbb Z/L\mathbb Z \to \mathbb
   Z/L\mathbb Z` from Theorem 2.4 can be shown injective on the relevant
   invariant subset, pre-period vanishes identically, for free, without
   needing opening 2's finer coincidence lemma at all). Not yet checked
   whether `G` actually is injective in our setting (see Cheap-kill /
   Small-case notes below) — worth testing directly once `L` is known for a
   given `a_1`.
4. **Reframing Gap 1 and Gap 2 as entangled, not independent.** The
   frontier/antichain construction used for opening 2 (minimal `rad(a_i)`
   sets under inclusion, pruned incrementally) is itself a *candidate,
   computable construction* of the covering set `H` for Gap 1 — it stabilized
   at a small finite antichain in every tested Case-II example (sizes 3-7)
   well within the first few thousand terms. This is not proof that it always
   stabilizes (Gap 1 remains open in general), but it is a concrete
   *algorithm* other explorers/approaches attacking Gap 1 could analyze
   directly (see Prior progress) — and per opening 2, whatever `H` this
   produces appears to make the coincidence lemma hold too, suggesting the two
   gaps may share one unified proof mechanism rather than needing two
   separate arguments.

### Candidate technique(s)
- Injectivity/permutation-of-finite-state argument (aimo-0577-style) to kill
  the dynamical-transient obstruction outright.
- Direct "coincidence lemma" (opening 2) via strong induction on `n`,
  possibly using Lemma 1's gap bound (`a_{n+1}-a_n \le \mathrm{rad}(a_1)` or,
  once `H` pinned down, `\le L`) plus a divisibility-density argument: an `x`
  in the narrow window `(a_n, a_n+L]` that satisfies even a *few* of the
  covering constraints (Σ_n small) tends, for structural/density reasons tied
  to `L` being a bounded lcm, to already satisfy all of `Σ_∞` — this is the
  substance to be made rigorous, not yet a proof.
- KB "Pigeonhole / extremal principle" (line 108) is the base tool already in
  use (Lemma 2.3, Theorem 2.4); no dedicated "permutation ⇒ no pre-period"
  entry exists in `knowledge_base.md` yet — worth the outliner citing the
  aimo-0577 crux move directly as the adapted technique if this route is taken.

### Cheap-kill candidates
- None found that kill an approach. One useful cheap *diagnostic*: for a
  candidate `H`/`L`, check `|{distinct residues visited}| == T` (found period)
  — if strictly greater, there IS a genuine transient and the coincidence
  lemma is false for that `H`; if equal, it's consistent with zero transient.
  In every one of my 7 tests this diagnostic passed (equality), suggesting
  the phenomenon may be structurally forced, not coincidental — worth
  testing on a wider a_1 sample before a builder invests in a full proof.

### Knowledge-base entries to use
- **Pigeonhole / extremal principle** (`knowledge_base.md` line 108) — already
  the backbone of Lemma 2.3 / Theorem 2.4; the sharpened openings above are
  refinements of how it's applied, not a replacement.
- No other KB entry is specific to "eventual-periodic ⇒ periodic-from-start";
  this appears to be genuinely bespoke content the population must construct
  (matches round 2's finding, re-confirmed).

### Analogous past problems (cruxes)
- **`aimo-0577`** (Croatia, IMO-SL-type, greedy `x_{k+1}=x_k+d` or `x_k/a`,
  subtopics `size-bounding-and-descent` / `modular-arithmetic-and-CRT`,
  domain `number_theory`). Crux move: confine the greedy orbit to a finite
  invariant set, then show the transition map is a **permutation** (via an
  explicit inverse) of that set, so periodicity holds with NO pre-period from
  the very first term. Genuinely analogous in target (greedy integer
  recurrence, "no pre-period" is exactly the sub-claim needed) though the
  concrete mechanism (explicit inverse formula) doesn't transfer verbatim —
  our transition map `G` is defined via a "smallest hitting integer" rule with
  no obvious closed-form inverse, so an adapted injectivity argument (not a
  literal formula-inversion) would be needed.
- **`aimo-0678`** (already flagged round 2, IMO-SL 2015 N4, same target
  "eventually periodic" for a coupled gcd/lcm recurrence) — only proves
  *eventual* periodicity (from some `N`), explicitly not periodicity-from-
  start; its official solution provides no technique for eliminating the
  pre-period, confirmed again this round. Still the best analogue for the
  overall proof *shape* (bound one coordinate, reduce the other mod its lcm,
  finite-state pigeonhole) already fully exploited by Theorem 2.4.
- No other crux in the corpus (searched `number_theory` +
  `sequences-and-recurrences`/`modular-arithmetic-and-CRT` for "periodic",
  "eventually", "greedy", "least/smallest/minimal integer") gives a technique
  for upgrading eventual periodicity to periodicity-from-start beyond these
  two; `aimo-0577`'s permutation trick is the standout candidate, everything
  else found was tangential (digit-periodicity, unrelated greedy-bound
  problems).

### Prior progress
Theorem 2.2 (H-hitting characterization), Lemma 2.3 (Σ-stabilization), and
Theorem 2.4 (conditional eventual periodicity, `n≥N_2`) — all certified,
unchanged this round (see `lemmas/theorem-2.4-conditional-eventual-
periodicity.md` and `approaches/intersecting-family-covering-construction.md`
Part 2). My work this round sharpens *what remains* (Part 3's Gap 2) into the
concrete "coincidence lemma" (opening 2 above), backed by fresh, corrected
numerical evidence — this is new since round 2 (round 2's own test of the
analogous phenomenon used the wrong `H` and reported a negative/inconclusive
result; this round's corrected test is unambiguously positive on every
instance tried).

### Dead ends (do not retry)
- **Do not reuse round 2's `H=rad(a_1)` (or `rad(a_1)\cup\{2\}`) as a stand-in
  for the true covering set when testing periodicity-from-1 mechanisms** — it
  was numerically shown (round 2, re-confirmed by the exact same failure
  mode when I initially tried a naive frontier-antichain implementation, see
  Bug note below) to give false negatives that do not reflect the true
  covering set's behavior.
- **Do not blindly reuse "minimal radical antichain" pruning code without the
  fix below** — a subtle off-by-equality bug (see next section) produces
  spurious "backbone collapses to a single huge prime" artifacts that are
  numerically compelling-looking but wrong; independently sanity-check any
  such construction against a slow, brute-force `all(gcd(x,a)>1 for a in
  seq)` simulation on the first few hundred terms before trusting it (as
  memory rule #1 already advises for other structural claims — apply the same
  discipline here).

### Small-case / intuition notes (labeled conjectural)
- **[Conjecture, strong evidence, corrected numerics]**: for the TRUE
  covering set `H` (not a naive guess), `\min\{x>a_n:x\text{ hits }\Sigma_n\}
  =\min\{x>a_n:x\text{ hits }\Sigma_\infty\}` for every `n\ge1`. Verified
  60/60 direct checks across `a_1\in\{35,65,105,143\}`, `n=1..15` each.
- **[Conjecture, strong evidence]**: consequently `a_{n+T}=a_n+L` holds for
  **every** `n\ge1` (not just eventually), verified by tail-matched-`(T,L)`
  testing from `n=1` with **zero exceptions** across `a_1\in\{15,35,65,105,
  143,221,1001\}` (up to 4000-6000 simulated terms each); `a_1=247,375` did
  not converge to a detectable period even at 30000 terms (consistent with
  round 2's report that these are hard/slow Case-II instances — this is a
  computational-reach limitation, not evidence against the conjecture).
- **Bug found and fixed (methodological note for future numeric explorers)**:
  a naive "minimal-radical antichain" (frontier) implementation for
  incrementally tracking the minimal covering constraints has an
  off-by-equality trap — when a NEW term's radical exactly equals an
  EXISTING frontier element, the naive `remove supersets / add if not
  dominated` logic (using non-strict `≤` in both the removal and the
  "already dominated" check) deletes the existing element without
  re-adding it, silently losing a real constraint. This produced a false
  "the sequence's backbone collapses to the single huge prime 65537" artifact
  for `a_1=247` in an early pass. Fixed by using strict-subset removal
  (`rx < S`, not `rx <= S`) paired with a non-strict "already present or
  dominated" check (`any(S <= rx ...)`). Re-verified against a slow O(n²)
  brute-force simulation (exact match on first 300 terms) before trusting any
  further output. **Any future approach that tries to compute/construct `H`
  or `W` algorithmically (relevant to Gap 1 too) should use this corrected
  logic, not reinvent it.**
