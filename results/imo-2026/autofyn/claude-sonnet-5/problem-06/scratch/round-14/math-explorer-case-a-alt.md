## imo-2026-06 (lens: Case-A alternative route via Lemma WF, bypassing Backbone Permanence)

### Headline finding (high confidence, numerically + logically verified, NOT yet reviewer-certified)

**The Case A / Case B distinction is NOT a hard barrier to Lemma WF — and Lemma
WF, used directly (no Backbone Permanence, no Lemma BS, no running
intersection B_k at all), appears to FULLY AND UNCONDITIONALLY CLOSE
Conjecture (JW) for BOTH a_1=2747 and a_1=4087**, the two Case A instances
this round's dispatch targeted. If a builder formalizes this and it survives
review, both become fully solved concrete instances of the whole IMO problem
(3rd and 4th, after a_1=247 in round 13) — and, crucially, WITHOUT needing an
explicit stabilization-index bound for Lemma BS at all. That gap becomes moot
for these two instances.

### The mechanism: Singleton-Chain Closure (a sharper special case of Lemma WF)

Lemma WF (`lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`,
certified round 13) states: fix disjoint nonempty cores `S,S'`, a fixed index
`i_0` with `S(i_0)=S'`. Then **for every** `k∈I_S`, `comp(a_k)∩comp(a_{i_0})
≠∅`. This is proved from only Corollary P″ (unordered Lemma P′, unconditional)
+ Lemma XC (`lemmas/lemma-XC-NIDF-FT-cross-companion-transversal.md`,
unconditional, no boundedness/permanence hypothesis at all). **Nothing in
Lemma WF's hypotheses references Case A/B, backbone realization, or any
"eventually" quantifier** — it is a pure `∀k∈I_S` fact from ONE fixed witness,
true immediately and forever, by definition of the sequence (every pair of
terms has gcd>1). The Case A/B split (Lemma BS/Theorem CAC,
`lemmas/lemma-BS-backbone-stabilization-and-theorem-CAC.md`) is a DIFFERENT,
independently-invented classification specific to the *running-intersection*
approach — it is not a precondition anywhere in Lemma WF/XC/P″'s statements
or proofs. There is no logical reason Lemma WF can't be applied to a pair
classified (empirically, via the backbone-intersection process) as "Case A."

**New refinement found this round ("Singleton-Chain Closure"):** if a class
`I_{S'}` contains a low-index member with `|comp|=1` (companion set is a
SINGLE prime `q`), Lemma WF with that one witness forces `q | a_k`
UNCONDITIONALLY for **every** `k` in the opposite class `I_S` — no case-split,
no disjunction. If enough such singleton witnesses exist across the "menu"
of primes needed, the whole pair closes in one step. This is a strengthening
of round 13's FW1 (which used one singleton witness for one fact among
several) into a *complete, disjunction-free* closure when singleton witnesses
happen to cover the whole menu.

### Verified computation for a_1=2747 (P_1={41,67}, sole disjoint doubly-infinite pair ({41},{67}))

Generated the sequence with a fast minimal-radical-antichain generator
(cross-validated against exact brute force on `a_1=15`, first 40 terms, zero
discrepancies — see `/tmp/round-14/gen.py`). Exact factorizations
independently confirmed via `sympy.factorint`:

- `a_3 = 2814 = 2·3·7·67` → `S={67}`, `comp={2,3,7}` (the "menu").
- `a_13 = 3321 = 3^4·41` → `S={41}`, `comp={3}` (singleton).
- `a_14 = 3362 = 2·41^2` → `S={41}`, `comp={2}` (singleton).
- `a_163 = 11767 = 7·41^2` → `S={41}`, `comp={7}` (singleton).

**Proof.** By Lemma WF with `i_0=3` (`S(i_0)={67}`): for every `k∈I_{41}`,
`comp(a_k)∩{2,3,7}≠∅`. **[A]**
By Lemma WF with `i_0=13,14,163` (all `S(i_0)={41}`) applied three times: for
every `k∈I_{67}`, `comp(a_k)∩{3}≠∅`, `comp(a_k)∩{2}≠∅`, `comp(a_k)∩{7}≠∅`,
i.e. `{2,3,7}⊆comp(a_k)` for **every** `k∈I_{67}`, unconditionally. **[B]**
Now fix arbitrary `i∈I_{41}, j∈I_{67}`. By [A], `comp(a_i)` contains some
`p∈{2,3,7}`. By [B], `comp(a_j)⊇{2,3,7}∋p`. So `p∈comp(a_i)∩comp(a_j)`, hence
`\gcd(a_i,a_j)≥p>1`. **This holds for every such pair, with W={2,3,7}.**
`∎` — Conjecture (JW) is closed for this pair with explicit `W_{S,S'}={2,3,7}`.

**Sanity check (not part of the proof, confidence-only):** regenerated to
`N=200,000` (11,193,164 max value) and directly checked: every realized
`I_{41}` member's comp intersects `{2,3,7}`, every realized `I_{67}` member's
comp is a superset of `{2,3,7}` — **zero violations**, matching the proof
exactly (as it must, since the proof is unconditional — this is a bug check
on the generator/logic, not evidence in itself).

### Verified computation for a_1=4087 (P_1={61,67}, sole pair ({61},{67}))

Even simpler — BOTH classes have low-index singleton witnesses for the SAME
prime:

- `a_5 = 4288 = 2^6·67` → `S={67}`, `comp={2}` (singleton).
- `a_54 = 7442 = 2·61^2` → `S={61}`, `comp={2}` (singleton).

**Proof.** By Lemma WF with `i_0=5` (`S(i_0)={67}`): for every `k∈I_{61}`,
`2|a_k`, unconditionally. By Lemma WF with `i_0=54` (`S(i_0)={61}`): for
every `k∈I_{67}`, `2|a_k`, unconditionally. Fix any `i∈I_{61},j∈I_{67}`:
both divisible by 2, so `\gcd(a_i,a_j)≥2>1`. `∎` — closed with `W_{S,S'}={2}`,
the simplest possible witness set (a single global prime).

**Sanity check:** regenerated to `N=200,000` (max value 12,775,840): every
member of both classes divisible by 2 — zero violations.

### Why this fully solves the two instances (via already-certified machinery)

Both `a_1` have `|P_1|=2`, so by Theorem SW
(`lemmas/theorem-SW-stabilization-sufficiency.md`, certified round 9) the
**only** non-automatic case in its 3-way exhaustive split is exactly the one
doubly-infinite disjoint core pair — `Lemma SW1` handles `S(i)∩S(j)≠∅`
(including the top core `P_1` itself, per that file's own note), and there
are no finite-`I_S` proper cores to worry about here (both proper cores are
confirmed infinite — this is exactly why prior rounds classified these as
"doubly-infinite disjoint core pair" candidates for Case A/B in the first
place, per `lemmas/lemma-BS-backbone-stabilization-and-theorem-CAC.md`'s own
listing of `2747:(41,67)` and `4087:(61,67)` as such instances). With the
pair now closed, `H:=P_1∪W_{S,S'}` (`{2,3,7,41,67}` for 2747, `{2,61,67}`
for 4087) satisfies FCBC, and Theorem 5.1 (`lemmas/theorem-5.1-master-
conditional-theorem.md`) gives explicit `T,L` with `a_{n+T}=a_n+L` for every
`n≥1` — the exact headline conclusion of the whole IMO problem, for these two
specific `a_1`.

### Distinct openings surfaced

1. **Singleton-Chain Closure directly closes 2747 and 4087** (this report's
   main finding) — bypasses Backbone Permanence/Lemma BS entirely, no
   explicit stabilization-index bound needed.
2. A general **template**: for ANY `a_1` with a doubly-infinite disjoint core
   pair `(S,S')`, search low-index members of EACH class for singleton
   companions; if the union of singleton-forced primes on each side already
   intersects (or if one side's singleton set covers the whole "menu" of the
   other side's smallest witness), the pair closes with zero case-split —
   strictly easier to search for than a full disjunctive covering table
   (FW1/FW2's method) and MUCH easier than proving Backbone Permanence.
3. When singleton witnesses aren't immediately available on the forcing side,
   the general disjunctive/transversal chaining method (below) is a fallback,
   but empirically (see "what did NOT work" below) it can stall the same way
   FCBC stalled in general — singleton witnesses are the clean win when they
   exist.

### Cheap-kill candidates / negative results found en route

- **Naive "first-N-witnesses" transversal chaining alone (without hunting for
  singletons) does NOT obviously close 2747**: using the first 8–150
  low-index members of `I_{41}` as clauses to build minimal hitting sets
  (transversals) constraining `I_{67}`, one "avoid {2,3,7}" alternate
  transversal branch kept absorbing new primes as more witnesses were added
  (`{2,3,7}` vs. a growing `{2,3,5,11,13,17,19,23,...}` branch that never
  closed) — the same "cycling primes"/unbounded-witness-set obstruction
  documented in rounds 3/8/9 for the general FCBC problem. **Do not rely on
  bulk/generic transversal chaining without first searching for singleton
  witnesses** — the generic method looked stuck exactly the way the general
  problem is stuck, until the singleton-witness search (idx13,14,163) found
  the actual clean closure. This is a useful methodological lesson: always
  search explicitly for `|comp|=1` witnesses in the smaller/target class
  before falling back to full disjunctive chaining.
- Verified (script `/tmp/round-14/wf_test.py`, `minimal_transversals`
  function) that this obstruction is real and reproducible, not a coding bug
  — increasing witness count from 8 to 150 never closed the "avoid 7" branch
  via the generic method; only the targeted singleton search did.

### Candidate technique(s)

Lemma WF (certified) + Corollary P″ + Lemma XC (both certified,
unconditional, no permanence/boundedness hypotheses) + Theorem SW (certified)
+ Theorem 5.1 (certified). All ingredients are already in `lemmas/`; no new
lemma needs to be invented, only this specific application assembled and
formalized into an approach file / lemma file for a_1=2747 and a_1=4087.

### Knowledge-base entries to use

None new beyond what's already cited in the certified lemma files above —
this is pure elementary number theory (gcd, radical, pigeonhole-style
disjunction combination), no external KB entry needed.

### Analogous past problems (cruxes)

Not re-searched this round (dispatch's focus was numerical verification of a
specific mechanism on specific instances, and round 13's math-explorer
already searched the corpus for the witness-chaining mechanism's origin).
None flagged as newly relevant.

### Prior progress

Builds directly on round 13's certified Lemma WF/Theorem FW1/FW2
(`a_1=4199:(13,17)` and `a_1=247` solved) and round 12's certified Lemma
BS/Theorem CAC (existence-only backbone stabilization, explicit-bound gap
still open in general). This round's finding does NOT close the general
explicit-bound gap for Backbone Permanence — it shows that gap is simply
**irrelevant** for the specific instances `a_1=2747,4087`, because a
completely different (and simpler) mechanism closes them directly.

### Dead ends (do not retry)

- Do not re-attempt Early/Bounded Stabilization (EBS) — still refuted, see
  round 13 (unaffected by this finding, since this finding uses no running
  intersection at all).
- Do not rely on generic/bulk low-index-witness transversal chaining without
  first searching for singleton (`|comp|=1`) witnesses — see the negative
  result above; it can look exactly as stuck as general FCBC.

### Small-case / intuition notes

- The reason 2747 and 4087 close so cleanly is that their SMALL/thin proper
  core class (e.g. `I_{67}` for 2747 has only ~59-98 members through
  `n=3000-5000`, vs. `I_{41}`'s ~2879-4800) still has enough LOW-INDEX
  DIVERSITY to realize each menu prime as a standalone singleton companion
  early — this is a favorable structural feature of `|P_1|=2` instances with
  small prime factors, not a general guarantee. **Conjecture (untested this
  round, flagged for future work)**: this Singleton-Chain Closure mechanism
  may generalize to more `a_1` instances (including the other Case A
  candidates listed in `lemma-BS...md`: `21528751:(103,197)`,
  `4199:(13,19)`, `4199:(17,19)`) — worth a dedicated search next round if
  sibling explorers' routes on those instances don't already close them by
  other means.
