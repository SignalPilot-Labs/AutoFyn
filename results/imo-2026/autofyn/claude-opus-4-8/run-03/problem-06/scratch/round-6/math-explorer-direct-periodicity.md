## imo-2026-06 — Route (ii): direct periodicity of the gap word, bypassing "Π finite"

### Distinct openings scouted (within route ii)

1. **Finite-state / Myhill–Nerode automaton on (a_n mod K) or on a window of recent gaps.**
   Concretely: find fixed K (finite set of primes S, K=∏S) and fixed U⊆Z/KZ such that,
   for large n, admissibility of c∈(a_n,a_n+M] depends only on c mod K. This is *exactly*
   the hypothesis of the already-certified **Reduction Lemma** (free-lemmas.md /
   anomaly-count-terminates.md §"General reduction"): "finite modulus K + fixed residue
   set U ⇒ periodicity." I traced this hypothesis line by line: it says admissibility
   testing against every minimal support F∈𝓐_∞ reduces to a residue check mod K. Since
   distinct minimal supports use **private-witness primes** (certified E3: q ≤ distance,
   and TAS: a large prime's witness is disjoint from the fixed anchor set), a minimal
   support F whose controlling/private prime q does not divide K genuinely changes
   which c meet F — you cannot capture "does q|c" by a residue mod K that omits q. So the
   Reduction Lemma's hypothesis, unpacked, **requires every essential prime across all of
   𝓐_∞ to divide K**, i.e. requires Π (or at least its "necessary" part) to be finite.
   **This opening is the Reduction-Lemma path already on record — it does not bypass
   Π-finite, it restates it.**

2. **Sliding-window pigeonhole on (a_n, d_n,...,d_{n+k-1}) for fixed window length k.**
   Same content as (1): a bounded window of k consecutive terms only reveals which
   *small* primes (those ≤ some bound growing with the window's actual values) divide
   those terms; it cannot certify that no future large private-witness prime will ever
   surface. This is literally the "dynamical automaton on the value stream" framing that
   R3's `value-stream-double-freeze` proved **collapses to Π-finite** (certified negative,
   "automaton finite-state ⟺ Π finite", flagged in Rules as forbidden to reopen). I
   independently re-derived the collapse via the private-witness argument above, so the
   R3 result is corroborated, not just cited.

3. **Checked for a genuine "converse gap"** — i.e., could A be eventually periodic mod
   some finite K even though 𝓐_∞ (hence Π) is literally infinite, because the excess
   minimal supports beyond K become *automatically redundant* for large c (never actually
   exclude anything)? This would be a real bypass if true. I traced it using the certified
   E3 (private-witness q ≤ |t−t'|) and TAS (a large prime's private witness H is disjoint
   from the fixed anchor set P): a minimal support F with a large private prime q ∉ primes(K)
   DOES exclude a genuine residue class mod q from A (namely c ≡ 0 mod q is required to
   meet F via that witness, and q ∤ K means this is not a periodic-mod-K condition). So
   redundancy cannot happen for a private-witness prime — **the converse gap does not
   exist**; A eventually periodic mod finite K is genuinely equivalent to Π-finite (up to
   the "necessary vs redundant primes" distinction already built into 𝓐_∞ being minimal
   supports). This closes off what looked like the one promising loophole in this lens.

4. **aimo-0648-style "invariant window + Bezout closing" mechanism** (corpus transplant
   candidate, `number_theory/sequences-and-recurrences`, technique: "Show an order
   statistic (max/min) of the terms is preserved by the recurrence to confine the sequence
   to a bounded interval, forcing eventual periodicity of an integer sequence"). Read the
   full solution: it works because the state window there has an **a priori fixed size**
   n_0=d_1 (given by the problem statement itself, not something to be proved), so
   boundedness of values ⇒ boundedness of the *state* is immediate, and periodicity
   follows by pigeonhole on that a priori-finite window, then a Bezout argument on the
   d_i's (gcd=1) pins exact stabilization. **This does NOT transplant**: in our problem
   the "memory" needed to compute s(a_n) is not an a priori fixed-size window of past
   terms — it is exactly "how many primes are structurally relevant," which is the open
   question (Π finite) itself. There is no analogue of "n_0 is given" here. I record this
   as a genuine near-miss, not usable as stated.

5. **Combinatorics-on-words / Ramsey / van der Waerden on the bounded gap word directly**
   (d_n ∈ {1,...,M}, a FIXED finite alphabet for ALL n, per certified Gap-bound lemma L2 —
   this is the one asset that is real and does not require Π finite). In general, a bounded
   integer word over a finite alphabet need **not** be eventually periodic (Sturmian words,
   Thue–Morse, and other morphic words satisfy strong recurrence-of-factors properties from
   VdW/Ramsey-type theorems yet are never eventually periodic). So VdW/Ramsey alone gives
   only "some pattern recurs infinitely often," not periodicity — it needs an EXTRA rigidity
   fact special to our recurrence (e.g. that recurrence of a long enough window *forces*
   the map governing future gaps to be identical, i.e. Myhill–Nerode determinism) to upgrade
   recurrence-of-a-pattern to periodicity-of-the-whole-tail. That extra ingredient is again
   exactly openings (1)/(2), i.e. Π-finite. I could not find or construct a version of this
   that avoids requiring Π-finite; flagging as speculative/untried but structurally very
   likely to hit the same wall, not to be counted as new leverage without a concrete new
   rigidity lemma attached.

### Verdict on the lens

Every concrete mechanization of "prove periodicity directly" that I could construct reduces,
on inspection, to exactly the certified Reduction Lemma hypothesis (finite K + fixed U), which
is provably equivalent to Π-finite (via E3 private-witness / TAS: an excess large private prime
genuinely breaks periodicity mod any K not divisible by it — verified the "converse gap" does
NOT exist, opening 3 above). This matches and reinforces the already-certified R3 result
(value-stream-double-freeze automaton collapse) and the Rules entry forbidding re-opening
"dynamical automaton on the value stream." **I did not find a genuinely new top-level route
inside lens (ii); it appears to be exhausted/closed by prior certified work**, not merely
under-explored. The only unexamined thread (VdW/Ramsey combinatorics-on-words, opening 5) is
mathematically insufficient on its own (bounded alphabet ⇏ periodic in general) and I could not
identify the missing rigidity ingredient without smuggling in Π-finite.

### Candidate technique(s)
None new. Confirms: Reduction Lemma / finite-automaton framing = Π-finite in disguise
(re-derived independently via E3 + TAS, corroborating R3's certified negative result).

### Cheap-kill candidates
- The "converse gap" check (opening 3) is itself a cheap structural kill: it rules out the
  one place this lens could have produced independent leverage, in one paragraph, using
  only already-certified E3 + TAS. Worth stating explicitly in the outline so no future round
  re-tries "maybe periodicity is weaker than Π-finite."

### Knowledge-base entries to use
- None beyond what's already certified in this problem's own lemma files (E3 private-witness,
  TAS two-anchor scaffold, Reduction Lemma, no-transient fixed-successor). `knowledge_base.md`
  has no automata/morphic-word specific entry (checked: only "order of an element" / "linear
  recurrences ⇒ eventually periodic mod m" generic entries, not applicable — our modulus is
  exactly the unknown).

### Analogous past problems (cruxes)
- `aimo-0648` (number_theory, sequences-and-recurrences) — "bounded window ⇒ eventually
  periodic ⇒ Bezout combination forces exact stabilization." Read in full; does **not**
  transplant (its window size is a priori given by the problem, ours is the crux itself) —
  recorded as a near-miss so nobody re-proposes it without addressing this gap.
- `aimo-0514` (combinatorics, processes-and-algorithms/invariants) — "reversible process ⇒
  state graph is union of cycles ⇒ purely periodic," already tried as `reversible-state-bijection`
  in R1 and cut at outline (unregistered) — consistent with my finding that finite-state framings
  are the exhausted direction.
- `aimo-0982` (digit subsequence sampled at 2^n-th positions) — same "track index modulo period
  of an already-known-periodic source" shape; not analogous here since we don't have an a priori
  periodic source to sample from.
- No genuinely new analog found for "prove periodicity of a greedy/gcd process directly without
  a finiteness intermediate" — the corpus's closest matches (aimo-0648, aimo-0514) both rely on
  an a priori finite state that our problem does not hand us for free.

### Prior progress
Unchanged by this lens: whole theorem certified-equivalent to E5″ (redundant-constraint-antichain,
§13.1, per run_state). No-transient / fixed-successor (a_{n+1}=s(a_n) from n=1) and the Reduction
Lemma remain the certified assets; this exploration used them to CLOSE OFF lens (ii) rather than
advance it.

### Dead ends (do not retry)
- Any "find finite K + fixed U" / automaton / bounded-window-state mechanism to prove periodicity
  directly — re-confirmed equivalent to Π-finite (R3 certified + independently re-derived here via
  E3/TAS). Do not re-seed.
- aimo-0648 window-invariant transplant — structurally inapplicable (no a priori bounded memory
  given in our problem).
- Van der Waerden/Ramsey-only argument on the bounded gap word — mathematically insufficient
  alone (bounded alphabet does not imply eventual periodicity, cf. Sturmian/Thue–Morse); no
  extra rigidity ingredient found that avoids Π-finite.

### Small-case / intuition notes (conjecture, numeric evidence only)
- Simulated a_1=105 (N=400 terms) and a_1=375 (N=400 terms): gap word d_n confirmed to lie in a
  small fixed alphabet ({2,3,4,6} for a_1=375, {2,3,4,6} for a_1=105 at this depth) — consistent
  with certified Gap-bound L2 (d_n ≤ rad(a_1)). No periodicity is visible yet at N=400 for
  a_1=375 (matches R3's note that convergence for this seed needs N~900); this is pure numeric
  evidence, not a proof of anything new.
- Recommendation to outliner: given lens (ii) is now closed (not just unexplored), R7's mandate
  for "genuinely different top-level route" should focus on lens (i) (a JOINT/global potential
  over the whole system of minimal supports simultaneously, attacking the §7b/§8.4 "simultaneous
  interaction" difficulty head-on) or lens (iii) (a different reduction of the ORIGINAL problem
  that avoids ever forming the minimal-support antichain 𝓐_∞ at all — e.g. working directly with
  the sequence of newly-recruited primes as they are recruited, rather than with supports).
