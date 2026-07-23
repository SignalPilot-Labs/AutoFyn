## imo-2026-06 (lens: structural/extremal argument on "fan" objects)

### Headline finding: a new, provable (not just numerical) lemma — "First-Occurrence Minimality" (FOM)

**Claim (FOM).** For every index `n≥2`, if `rad(a_n)` does not equal `rad(a_i)` for any
`i<n` (i.e. `a_n` is the *first* term ever to realize the radical value
`C:=rad(a_n)`), then `a_n = T_C`, where `T_C := min{x∈ℤ : x>a_1, rad(x)=C}`
(a fixed integer depending only on `C` and `a_1`, well-defined since
`{(∏_{p∈C}p)^t : t≥1}` has radical `C` and is unbounded — same `T_C` as
`imprint-automaton-periodicity.md`'s "Step 0", which only checked ONE
instance of this numerically; FOM generalizes and *proves* it for every
instance).

**Proof (elementary, no new machinery — I did not find this already certified
anywhere in `lemmas/` or in `approaches/*.md`; grepped for "first occur",
"T_C", "minimal representative" and only found the single numerical
spot-check in `imprint-automaton-periodicity.md`'s Step 0).**
Key fact used: `gcd(x,y)>1 ⟺ rad(x)∩rad(y)≠∅`, so admissibility of a
candidate integer depends **only on its radical**, not its magnitude — the
same radical is either admissible against a given prefix `a_1,…,a_m` or not,
regardless of which specific integer realizes it.

Suppose toward contradiction `n` is a first occurrence of `C` with
`a_n≠T_C`. Since `a_n` itself is an integer `>a_1` with radical `C`,
`T_C≤a_n` by minimality of `T_C`; so assume `a_n>T_C` strictly. `T_C` cannot
equal any `a_i` (`i<n`), since that would give `rad(a_i)=C`, contradicting
"first occurrence at `n`". So `T_C` falls strictly inside a unique gap
`a_i<T_C<a_{i+1}` for some `i` with `i+1≤n` (using `a_1<T_C` which holds by
`T_C`'s definition). Since `a_n` is a genuine term, its own admissibility
gives `C∩rad(a_j)≠∅` for **every** `j=1,…,n-1` — in particular for every
`j≤i` (`i≤n-1`). Since `rad(T_C)=C` too, `T_C` is **also** admissible against
`a_1,…,a_i` (identical radical ⇒ identical intersection facts), and
`T_C>a_i`. By the greedy rule's minimality, `a_{i+1}≤T_C`; combined with
`T_C≤a_{i+1}` (choice of `i`) this forces `a_{i+1}=T_C` exactly. But
`i+1≤n-1<n` (since `a_n>T_C=a_{i+1}` and the sequence is strictly
increasing), so index `i+1<n` already has radical `C` — contradicting `n`
being the first occurrence. ∎

**A free corollary, also new:** "`C` is added to the antichain `𝓜_n` at step
`n`" happens **iff** step `n` is `C`'s first occurrence (if `C` were realized
earlier without being dominated it would already be in the antichain; if
dominated earlier, No-Resurrection — already certified,
`theorem-V-veto-finite-iff-MRS.md` — keeps it dominated forever, so it can
never re-enter). So **every collapse/insertion event's new value is exactly
`T_C`**, not just "observed to match" as round 5 found on one example.

### Rigorous corollary: fan-size IS bounded, conditional only on absorption happening

Combining FOM with plain strict monotonicity of `(a_n)` gives, **rigorously
(not numerically)**: if a sub-core `C'` is ever realized (its first
occurrence, by FOM, is exactly `a_m=T_{C'}` for the collapse index `m`), then
every fan member `C'∪{q}` that was antichain-resident *before* step `m`
(i.e. got removed/dominated at the collapse) has value `<a_m=T_{C'}`
(strict monotonicity — it existed at a strictly earlier index). Since any
term with radical `C'∪{q}` is a multiple of both `q` and `∏(C')`, its value
is `≥q·∏(C')`. Combining: `q<T_{C'}/∏(C')`. **Only finitely many primes**
satisfy this, giving an explicit, finite, `a_1`-and-`C'`-computable upper
bound `π(T_{C'}/∏(C'))` on fan size — **fully closing the "how big can a fan
grow" half of round 5's sub-lemma (b), unconditionally, given only that the
fan is eventually absorbed.**

### Numerical confirmation (large-scale, zero exceptions)

- **FOM tested directly** (every distinct radical's first occurrence vs.
  `T_C`) on 5 stress cases (`a_1=15,247,375,2747,4087`, 500 terms each) plus
  **30 fresh random semiprime/3-factor `a_1` values** (seeded, `a_1∈[106,
  11803]`, 300 terms each, ~6000+ distinct radicals checked in total):
  **zero violations** (the only "mismatch" is the trivial `n=1` boundary
  case, since `T_C` requires strictly `>a_1` while `a_1` realizes its own
  radical at `n=1`, not a real counterexample).
- **Extremal fan-size bound tested** on 70+ actual collapse events across 17
  `a_1` values (`15,35,65,105,143,221,247,375,1001,2431,4087,4199,91,323,
  1573,2747`, plus the hardest known case `a_1=21528751` to `N=30000`, 54
  collapse events there alone): **every single collapse's absorbing term
  exactly equals `T_C` for the newly-added core `C`, and every collapse's
  fan size is `≤` the bound `π(T_C/∏(C))`** — zero exceptions (`a_1=
  21528751` alone gives 54 independent confirmations, e.g. core `{7,103}`
  absorbs 1096 fan members, bound `3762`; core `{7,11,41,103}` absorbs `2`,
  bound `18`).

### New structural finding: why some fans never collapse at all (permanent finite freezing)

`a_1=247` (`P_1={13,19}`): the two proper-core channels `S={13}`, `S={19}`
each stabilize at exactly **3** elements with **zero collapse events ever**
(checked to `N=6000`). Diagnosed why: the "bare" target `T_{13}=2197`
(smallest integer `>247` with radical exactly `{13}`) can **never** become
an actual term, because `gcd(2197, x)=1` for any term `x` in the *disjoint*
`S={19}` channel (e.g. `rad=[2,3,19]`) — and by the same monotone-hardening
argument as FOM's proof (admissibility, once permanently failed against a
fixed earlier term, is a **permanent** obstruction, never re-checked or
undone), `{13}` alone can **never** be realized, so this fan can never be
"purely" absorbed by its own core — it just freezes at whatever finite
antichain of 2-or-3-prime radicals happens to intersect every other active
channel. This generalizes Lemma TC's mechanism (which shows `S=P_1` forces
triviality) down one level: a candidate absorbing core `C'` for channel `S`
is only reachable if `C'` itself carries enough "extra" primes to intersect
**every other currently-active channel**, not just be `⊇S`. This is a
genuinely new qualitative insight but **not** yet a general lemma — I did
not attempt to formalize "which C' work" in general, only diagnosed one
example precisely.

### Nesting depth: confirmed 3 levels (extends round 5's depth-2 finding)

For `a_1=21528751` (to `N=30000`), traced explicit **3-level nested
collapse chains**, e.g. core `{7,17,19,103}` (added `n=17351`) is itself
later absorbed into `{7,17,103}` (`n=23059`), which is itself later absorbed
into `{7,103}` (`n=27832`) — a genuine depth-3 chain, one level deeper than
round 5's `a_1=2747` depth-2 example (`{2,41}`⊂ its own fan). 50 of the 54
collapse events at this `a_1` are links in such nesting chains. **No bound
on nesting depth is known or suggested by this data** — future arguments
for "Bounded Core Family" must not assume shallow (2-level) recursion.

### Distinct openings surfaced

1. **Formalize and certify FOM as a standalone lemma** (proof above is
   short, elementary, fully general — looks buildable in one pass). This
   alone is worth certifying regardless of whether it closes the main gap:
   it rigorously replaces round 5's single-example numeric spot-check with
   a proven general fact, and gives, as a free corollary, the rigorous
   fan-size bound (closing half of sub-lemma (b)).
2. **Reduce (MRS_S)/`𝓥_S`-finiteness, via FOM + the fan-size corollary, to a
   single sharper existence question**: is it true that for every proper
   core `S⊊P_1`, only finitely many distinct "absorbing" sub-cores `C'⊇S`
   are ever realized (i.e. only finitely many `T_{C'}` values are ever
   actually hit)? Given FOM, `𝓥_S`'s infinitude can now ONLY happen via
   either (a) infinitely many distinct absorbing events (infinite chain of
   ever-larger `C'`s each finitely bounding its own fan, per the corollary,
   but infinitely many of them), or (b) one channel that genuinely never
   collapses AND never stops growing (an infinite, uncollapsed antichain
   within `S`) — FOM does not rule out either, but sharpens exactly what a
   proof must exclude.
3. **Try to prove a "permanent freeze" dichotomy**: formalize the `a_1=247`
   mechanism (permanent inadmissibility of "too-bare" sub-cores due to
   cross-channel non-intersection) into a general lemma bounding which `C'`
   can ever be eligible absorbers for channel `S`, given the OTHER
   currently/eventually-active channels of `a_1`. This is the most
   promising concrete next target from this round's findings — it directly
   attacks the still-open "does the fan ever stop growing" question with a
   NEW, provable-looking mechanism (cross-channel intersection necessity),
   rather than re-attempting the already-refuted DM-order-alone or
   monotone-count approaches.

### Cheap-kill candidates
- None found that immediately kill the whole gap. But FOM itself acts as a
  structural pruning tool: it rules out ANY proof strategy that worries
  about "delayed" appearances of a radical (values larger than `T_C`) —
  every appearance is exactly at `T_C`, so counting/density arguments can
  work directly with the fixed integers `T_C` instead of unknown sequence
  positions.

### Candidate technique(s)
FOM's proof technique (radical-only dependence of admissibility + monotone
non-increasing admissibility of a fixed radical as the prefix grows) is a
genuinely reusable elementary tool, distinct from the DM-multiset-order tool
and from the channel-splitting/assembly machinery already certified. It
combines cleanly with Theorem CD's core decomposition and Lemma P′
(pairwise intersection) already in `lemmas/`.

### Knowledge-base entries to use
No new KB entries beyond what prior rounds already identified (FCBC/(MRS)
machinery is homegrown, not from `knowledge_base.md`). FOM's proof uses only
elementary well-ordering, already within scope of "Name your tools" (no
external theorem needed — should be stated as a self-contained Lemma with
its own name, e.g. "Lemma FOM").

### Analogous past problems (cruxes)
Did not run a fresh corpus query this round (dispatch scope was numeric/
structural probing of fans, not corpus search); round 2's crux find
(aimo-0678, IMO-SL 2015 N4, non-increasing monovariant) remains the only
previously-identified analogue and is already known insufficient alone
(round 5 finding, still valid) — FOM is a different kind of tool (an exact
value-identity, not a monovariant) and has no flagged analogue in the corpus
from prior rounds' searches.

### Prior progress
See `current.md` Round 5 update and the cited lemma files — unchanged/
inherited baseline: (MRS) ⟺ `𝓥` finite ⟺ `𝓥_S` finite for each of `≤2^k-2`
proper cores `S⊊P_1` (Theorem V, Theorem CD, Lemma TC, all certified). This
round's FOM lemma and its fan-size corollary are **new, not yet certified**
— they should go through the normal outline→build→review pipeline before
being added to `lemmas/`.

### Dead ends (do not retry)
No new dead ends found this round. Reaffirm existing ones from `current.md`/
`run_state.md`: DM-multiset-order alone (necessary, not sufficient); H=
rad(L_per) circularity; plain cardinality monovariant on `|𝓜_n|`/`|𝓥_S|`
(non-monotone, proven false by the `a_1=4087` n=54 collapse, still valid —
note this round's FOM does NOT resurrect a monovariant argument, it is a
value-identity fact, orthogonal to monotonicity).

### Small-case / intuition notes (labeled as conjecture unless marked PROVED)
- **PROVED this round** (see above, elementary argument, not yet
  reviewer-verified): First-Occurrence Minimality (FOM) — `a_n=T_{rad(a_n)}`
  whenever `rad(a_n)` is a first occurrence.
- **PROVED this round, corollary of FOM + monotonicity**: fan size at any
  collapse is `≤π(T_{C'}/∏(C'))`, an explicit finite bound, given the
  collapse happens.
- **Conjecture, strong numerical support (0/70+ violations across 17 `a_1`
  including the hardest known case)**: every tested proper-core channel
  either (A) permanently freezes at a small finite size with zero collapses
  (e.g. `a_1=247`, `91`), or (B) undergoes finitely many collapse events,
  each an exact `T_C` hit, with the whole channel eventually stabilizing.
  No case showing unbounded/non-terminating growth was found in any test
  (consistent with FCBC being true, but not a proof it always happens).
- **Conjecture, qualitative, one worked example only**: permanent freezing
  (case A above) happens specifically because "too bare" sub-cores are
  permanently cross-channel-inadmissible — needs generalizing beyond
  `a_1=247` before it can be trusted as a general mechanism.
- **Empirical, not fully explained**: nesting depth reaches (at least) 3 for
  `a_1=21528751`; no case tested shows depth 4+, but the search was not
  exhaustive (only 17 `a_1` values, and depth was measured only by chain-
  following, not by an independent bound).
