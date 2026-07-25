## imo-2026-06 — INTENDED-LEVER HUNT (R7)

### HEADLINE FINDING: the official solution was located and it closes the run's open crux.

IMO 2026 already occurred (per the run's simulated "today" 2026-07-25) and the AoPS Wiki has the
verbatim problem statement and two solutions publicly posted. I fetched them via `r.jina.ai` proxy
(network partially worked: `curl` direct to artofproblemsolving.com returned 403/Cloudflare, but the
jina.ai reader-proxy succeeded, `https://r.jina.ai/https://artofproblemsolving.com/wiki/index.php/2026_IMO_Problems`
and `.../2026_IMO_Problems/Problem_6`). **The fetched statement is a VERBATIM word-for-word match**
to our problem_id imo-2026-06 (same "smallest integer >a_n with gcd>1 vs all i≤n", same conclusion
`a_{n+T}=a_n+L`). This is the real problem; the AoPS "Solution 2" is a community-vetted official-style
proof (not a random blog) — treat as **external, high-confidence but unverified by our own
proof-reviewer**, per CLAUDE.md rigor rules it must still be re-derived from scratch by a builder, not
cited.

### The lever: "key terms" + explicit power-of-anchor-prime rescaling witness

Solution 2 (source: `artofproblemsolving.com/wiki/index.php/2026_IMO_Problems/Problem_6`, verbatim
transcribed below with our variable names cross-referenced) proves Π (our Finite-Alphabet crux)
finite via a **sequential greedy key-term selection + one explicit rescaled witness per candidate**,
NOT via any global inequality on ∏G, p_max, or |t−t′|. This is genuinely different from every route
in the Rules/Broken list:

1. **Key terms.** Walk `a_1,a_2,...` in order; select `a_n` as a "key term" iff no previously
   selected key term `b` has `P(b)⊆P(a_n)` (P = prime factor set). This is exactly our `𝓐_∞`
   (⊆-minimal supports), but generated as a running/first-occurrence sequential filter, not a
   global minimality statement — this reformation itself sidesteps the "simultaneous
   interaction across all of 𝓐_∞" difficulty (our §7b/§8.4) because everything is stated with
   respect to *terms already seen*.
2. **Domination property (their (3), ≈ our R1/E1/E2):** if `x∈A`, `m≥a_1`, `P(x)⊆P(m)` then
   `m∈A`. Proved from their (1) pairwise-non-coprimality (= our L4) and (2) (minimality
   contrapositive, ≈ our E3/private-witness). Every term (not just key terms) has its support
   containing some earlier key term's support.
3. **The threshold and the witness (THE NEW LEVER).** Fix `Q=P(a_1)`, `q_0=max Q` (so `q_0≤a_1`,
   `q_0` PRIME — sharper than our `M=rad(a_1)`), and set the **a_1-only ceiling `C=a_1·q_0`**.
   Suppose toward contradiction a key term `x>C` introduces a prime `p` never seen in ANY earlier
   key term. Since `a_1` is itself the first key term, `p∉Q`; since `gcd(x,a_1)>1`, pick
   `q∈P(x)∩Q` (`q≠p`, so `q≤a_1`). Let `S=P(x)\{p}` (a **proper subset of x's support**, `q∈S`),
   `r=∏S`.
   - **Property (4):** every earlier key term `b` has `P(b)∩S≠∅` (because `P(b)∩P(x)≠∅` by
     pairwise-non-coprimality, and `p∉P(b)` since `p` is "new").
   - **Build `y`:** if `r≥a_1`, take `y=r`. Else take the *smallest* `t` with `y=r·q^t≥a_1`; then
     `r·q^{t-1}<a_1` so `y<q·a_1≤q_0·a_1=C<x`, and `P(y)=S` (multiplying by powers of `q∈S` adds
     no new primes). **In both cases `a_1≤y<x`, `P(y)=S`.**
   - **`y` is realized (`y∈A`):** every term `a_i` occurring before `x` either IS an earlier key
     term `b` (then `P(b)∩S≠∅` by (4), done) or is dominated by some earlier key term `b`
     (`P(b)⊆P(a_i)`, so `P(a_i)∩S⊇P(b)∩S≠∅`). So **no term before `y` is coprime to `y`** — this
     is a purely *local, already-determined-by-index* fact (only uses terms with index < that of
     `y`, which is < index of `x`), and by (2)-contrapositive `y∈A`.
   - **Contradiction:** since `y∈A`, `y` contains all prime factors of SOME earlier key term `b`
     (domination property again), so `P(b)⊆P(y)=S⊊P(x)`. But that means `x` (assumed to be a
     *new* key term, i.e. dominated by no earlier key term) IS dominated by `b` — contradiction.
4. **Finiteness.** So no key term `>C` ever introduces a genuinely new prime; only finitely many key
   terms are `≤C` (trivial, `a_n→∞`); their combined prime set `K` is finite; all later key terms'
   supports `⊆K`; distinct key terms have distinct supports (else the later one would've been
   dominated at selection time) ⟹ **at most `2^{|K|}` key terms total ⟹ 𝓐_∞ finite ⟹ Π finite.**
5. Endgame (their §"2026 IMO/Q6" and eqns 6–10): exactly our certified no-transient + periodicity
   endgame — `d_j=rad(b_j)`, `L=lcm(d_1,...,d_s)`, `m∈A ⟺ m+L∈A` for `m≥a_1`, `T=|A∩[a_1,a_1+L)|`.
   Matches our machinery verbatim (E1/no-transient/Reduction Lemma).

### Why this survives the run's guardrails (checked against every Rule/Broken entry)

- **Not the JSC/spread-bound lever (R5, dead):** `y` is not built by subtracting two realizer
  values `t−t′`; it's built by *multiplying* the residual radical `r=∏S` by powers of a **known
  small anchor prime `q≤a_1`** until it lands in the fixed window `[a_1, q_0·a_1)`. No
  `|t−t′|`-style spread inequality is invoked anywhere.
- **Not the RBD/rejection-budget lever (R6, dead):** no rejection-stream accounting; this is a
  single deterministic witness per hypothetical over-threshold key term, not a global sum over
  recruits.
- **Not the R4 Collapse "common sub-support of an infinite family" lever (dead):** R4's forbidden
  move needed a core `B` shared by an ASSUMED-INFINITE sub-family of `𝓐_∞`, and it died because such
  a `B` is not a global transversal of ALL of `𝓐_∞` (doesn't meet elements outside that infinite
  sub-family). Here `S=P(x)\{p}` is **local to one candidate `x`**, and the proof that `y∈A` uses
  only "`y` is not coprime to any term with index *strictly before* `y`'s position" — a finite,
  already-fixed set determined purely by the FORWARD/dynamic admissibility criterion (their (2)), not
  a transversal-of-everything requirement. It never needs `S` to meet supports appearing after `x`.
  This is the precise technical distinction our anchor-partition Collapse theorem's scope did not
  cover (R4 was about a *shared* core over infinitely many members; this is a *per-candidate* local
  witness that only needs to dominate terms already emitted).
- **Not an A_n-only monovariant (obstruction, dead):** it explicitly reads chosen values (the actual
  term `x`, the actual key terms selected so far), consistent with the run's own R2 finding that the
  closing argument MUST read greedy choices, not just the admissible set.
- **Numerically reproduced and matches our own certified `L`:** ran the key-term selection + `C=a_1·q_0`
  threshold on `a_1=375` (N=900 terms): `Q={3,5}`, `q_0=5`, `C=1875`. All 6 key terms found are
  `≤1875` (`375,378,380,384,399,490`), combined prime pool `K={2,3,5,7,19}` — **exactly** the run's
  independently-certified `L=3990=2·3·5·7·19` (R1 finding). This is strong corroborating evidence the
  argument is not just plausible-looking but produces the exact right answer on our own test case.

### Distinct openings for the outliner
1. **Primary: adopt the key-term + rescaling-witness lever wholesale**, restated in our own
   notation/lemma chain (E1/E2/E3/no-transient survive verbatim as infrastructure; this replaces the
   open E5″ arrow entirely with a self-contained finiteness proof that doesn't route through
   ∏G/p_max bounds at all — it can likely REPLACE the E4/E5/E5″ chain, not just close it).
2. Alternative framing: keep our `𝓐_∞`/antichain language, but prove the exact analogue of their
   step 3 as a *new* lemma "**Rescale-Witness Lemma**": for any `G∈𝓐_∞` with `∏G≥ q_0·a_1` (where
   `q_0=max P(a_1)`) and any `p∈G`, `∏(G\{p})·q^t∈A` for suitable `q∈G∩P(a_1)`, `t≥0`, landing in
   `[a_1,q_0a_1)`, hence some `B∈𝓐_∞` has `B⊆G\{p}⊊G`, contradicting `G`'s ⊆-minimality unless no
   such `G` exists beyond the threshold — i.e. **only finitely many minimal supports have
   `∏G≥q_0·a_1`**, done since the complementary regime is already closed (Prop 12.A, `∏G<a_1`
   closed, and the sliver `a_1≤∏G<q_0a_1` is also finite by the same primorial/cardinality
   argument as 12.A/R2).

### Candidate technique(s)
Explicit local witness construction via multiplicative rescaling by a small anchor prime `q≤a_1`
(not a magnitude/spread inequality); sequential greedy "key term" selection as the concrete
realization of the ⊆-minimal-support antichain; contradiction via re-invoking E1/E2-style
domination on the constructed witness.

### Cheap-kill candidates
None needed — the lever is constructive, not a bound to falsify. (Numerically reconfirmed on
`a_1=375`, matches certified `L` exactly — see above.)

### Knowledge-base entries to use
Whatever KB entries already back E1/E2/E3/no-transient (pairwise-intersecting family, minimality/
extremality arguments) — same as prior rounds; no new KB entry needed, this is a self-contained
construction.

### Analogous past problems (cruxes)
Did not find a closer corpus analog this round than the already-recorded aimo-0447/aimo-0678 (see
prior rounds); this lever is closer to a **direct constructive "build a smaller witness that must be
realized"** move than to any of those — recommend the outliner treat the AoPS Solution 2 itself as
the primary transplant source this round instead of the corpus.

### Prior progress
Full E1–E4, Prop 12.A/12.B, R1/R2, TAS, RBD as certified in `results/imo-2026-06/lemmas/*` — all still
valid, all still usable as infrastructure. The new lever plugs into the SAME endgame (no-transient +
Reduction Lemma) so nothing certified is wasted.

### Dead ends (do not retry)
Unchanged from run_state.md Rules/Broken — the new lever explicitly avoids all of them (see the
"survives the guardrails" analysis above). Do NOT let a builder mistake the new lever's `S=P(x)\{p}`
for the forbidden "common sub-support of an infinite family" (R4 Collapse) — the load-bearing
difference (local/per-candidate vs. global/shared-by-infinitely-many, and "not coprime to
already-earlier terms" vs. "transversal of ALL of 𝓐_∞") must be preserved when the outliner
re-derives it from scratch.

### Small-case / intuition notes
CONJECTURE-GRADE nothing here — the AoPS argument, if it re-verifies under our own proof-reviewer's
scrutiny, is a complete proof, not a conjecture. What remains genuinely open for us is only the
**re-derivation and independent verification** (per CLAUDE.md: "a retrieved crux/external solution is
a hint to adapt, never a citation — every borrowed step must still be proven from scratch"). The
numeric check on `a_1=375` (key terms all `≤C=1875`, pool `={2,3,5,7,19}=` our certified `L`'s prime
factors) is strong corroborating evidence, not a proof.
