## imo-2026-06 — lens: covering-system / density (Σ1/p²) + aimo-0421 recursive dichotomy

### Setup recap
Everything is certified-reduced to the single residual gap **E5″**: every ⊆-minimal support
`G∈𝓐_∞` with `∏G≥a₁` satisfies `∏(G∖{p_max}) < a₁` (equiv. sufficient `∏G<2a₁`). The
complementary regime `∏G<a₁` is fully closed (Prop 12.A). The anchor-partition route (finiteness
of each fiber `Q_p`, `p∈P=primes(a₁)`) is a certified equivalent (`anchor-partition.md`, Lemma A),
but was shown to collapse onto the same wall whenever the closing move is "force a common
sub-support `S⊊G` to be realized" — that move is now off-limits (per dispatch).

### What I tried on this lens (both prescribed levers), and why each fails to open new ground

**1. Direct density-of-A route (Σ over primes / covering fraction of the admissible set `A`).**
This is the most natural "covering system" reading: `A = {c : c meets every G∈𝓐_∞}` looks like the
complement of a covering system, and one might hope `density(A)→0` if `𝓐_∞` is infinite (too many
constraints ⇒ vanishing density ⇒ contradicts `A⊇{a_n}` unbounded/positive density from growth
Lemma 2). **This is EXACTLY the route already tried and refuted** in
`monovariants-and-obstruction.md` (density monovariant + the `{p*,q_k}` obstruction family):
density(A_n) is non-increasing but *converges* to a positive limit `1/p*>0` even with `Π` infinite
(the family `G_k={p*,q_k}`, `q_k→∞`, gives `density→1/p*`, never hitting 0, and never freezing).
So a raw Σ-density argument on `A` **cannot** distinguish "finitely many minimal supports" from
"infinitely many, each contributing a `→0` but never-zero density decrement" (the decrements form a
convergent series `Σ(1-1/q_k)`-type product, not a divergent one). This is a **certified dead end**;
I re-verified the reasoning (the density decrement at each new constraint `G_k={p*,q_k}` is
`(1-1/p*)(1/q_{k-1}-1/q_k)`-scale, summable). Re-affirm: do not resubmit this exact form.

**2. aimo-0447 grid-covering, re-examined for an UPPER-bound (not lower-bound) use.**
The aimo-0447 crux (`past_crux_moves_database.json`, problem_id `aimo-0447`,
`size-bounding-and-descent`) covers a *fixed* `N×N` grid by primes; small primes `p≤εn²` cover
`≤N²Σ1/p²+…<N²/2` cells (Σ1/p²<1/2 is the load-bearing numeric fact), forcing >half the grid to
carry primes `>εn²`, and DISTINCTNESS of those large primes (each hits an interval of length `N`
at most once) then gives a **lower bound** `∏(distinct large primes)≤ value`. This exact mechanism
is **already imported** into this problem as the certified `R1/R2` lower jaw
(`realizer-value-pincer.md`: `u(G)≥∏G≥P_{|G|}`, the primorial bound) — so this lever's natural
output is a *lower* bound on `u(G)`, which we already have. **The missing piece for E5″ is an
UPPER bound on `∏G`**, and the grid-covering mechanism has no natural upper-bound analogue: in
aimo-0447 the "large primes are forced to exist because small primes can't cover the grid" — but
here we'd need the reverse ("large primes can't coexist because … covers too much"), and the only
way I could find to make that bite is: **two large primes `q₁,q₂` (both order `√a₁`) in the same
`G` would need `q₁q₂≥a₁`, i.e. would need the small companion `G∖{p_max}` itself to already have
radical `≥a₁`** — but bounding that is *circular* (it **is** a form of E5″/(W) restated), not an
independent covering fact.

**3. aimo-0421 recursive dichotomy ("prime divides infinitely many terms" vs "finitely many").**
Applied to Π: the dichotomy is `(I)` some prime has infinite fiber `{n:p|a_n}`, vs `(II)` every
prime has a finite fiber. `(I)` for the anchor `p*∈P` is trivial (Lemma 1 + pigeonhole over `P`
finite — already used verbatim in `anchor-partition.md` Lemma A's proof). I tested whether `(II)`
could ever hold for a *non-anchor* recruit `q∈Π\P` (which would let a finite-fiber argument bite,
à la aimo-0421's "coprime-selection" branch). **Numerically it never does**: e.g. for `a₁=375`,
`q=19` divides `423` of the first `6000` terms (density `≈1/17`, consistent with `19` being part of
the eventual periodic structure once `Π` stabilizes) — every prime that ever enters a minimal
support recurs with density `≈1/q` forever, matching what finite-`Π`-periodicity would predict.
So `(II)` (finite fiber) is empirically **never** the case for a genuinely-recruited prime; the
dichotomy collapses to `(I)` for every candidate prime and gives **no discriminating power** — it
cannot distinguish "this prime belongs to a genuinely infinite `Π`" from "this prime belongs to the
true finite `Π`," because both look identical from the fiber-density side (both would show positive
recurring density, exactly as the `{p*,q_k}` obstruction family also illustrates from the density
angle). This lever does not open new ground either.

**4. A structural sanity check that clarifies WHY these levers keep failing.**
I directly measured "all primes dividing any of the first `N` terms" (not restricted to minimal
supports) for `a₁=375,899,385` at `N=6000`: this set is **genuinely unbounded and still growing**
at `N=6000` (`|primes dividing some term| = 639` for `a₁=375`, new primes introduced up to the very
last term). This is expected and harmless (a term can carry "junk" large prime factors that are not
part of any minimal support), but it means: **any covering/density argument phrased over "primes
occurring somewhere in the sequence" is doomed** — that set provably has no bound. The only
tractable object is `𝓐_∞` itself (via E1/E2 realizability), and once you restrict to it, the
"resource" that made aimo-0447's grid argument work (a *fixed*, finite region that must be fully
covered) has no counterpart: `𝓐_∞`'s members are indexed by an unbounded value range with no fixed
ambient size to run a pigeonhole-on-coverage-fraction argument against, short of picking the very
window `[a₁,∏G]` — which routes straight back to "realize a sub-support inside that window," the
**forbidden move**.

### A genuinely new (but still open) sharpening surfaced by this search

Numerically (25 random seeds `a₁∈[6,5000]`, `772` distinct large-regime minimal supports checked,
`0` violations; also the original 16 curated seeds): **every minimal support `G` with `∏G≥a₁` has
AT MOST ONE prime exceeding `√a₁`.** I.e. writing `G`'s primes increasingly `q₁<⋯<q_r`, always
`q_{r-1} ≤ √a₁` (often much smaller). This is *stronger* than E5″ in form (E5″ only needs
`q₁⋯q_{r-1}<a₁`; "at most one prime `>√a₁`" would give it immediately together with a primorial-type
bound on the rest) and might be a cleaner target to hand the outliner — but I could not find a proof
route for it that avoids the same forbidden sub-support-realization step: "if two primes `q,q'>√a₁`
both lay in `G`, then `S=G∖{q,q'}∪{one of them}` would need its own product bound," which again
bottoms out in realizing a smaller support to contradict minimality. Flagging as **numeric-only,
not proved**, and honestly noting it does not evade the identified wall — it's a sharper restatement
of it, offered as possible outliner material, not a bypass.

### Verdict on this lens
Both prescribed levers were investigated in depth and **neither yields an independent route around
the forbidden sub-support-realization wall**: the density-of-`A` instantiation is a *certified* dead
end (matches the existing Obstruction), the aimo-0447-style covering instantiation only reproduces
the already-certified lower jaw (R1/R2) and has no natural upper-bound counterpart, and the
aimo-0421 dichotomy is empirically vacuous here (every recruited prime shows infinite/positive-density
fiber, so the dichotomy never splits). This should be read as a *negative* scouting result: I could
not open new terrain on this lens beyond the sharpened numeric conjecture above. The outliner should
weigh this against continuing to invest in the residual-anchor-peeling / window-inequality framing,
or seeking an entirely different top-level target (not yet tried: an explicit *algebraic* CRT/coprimality
construction bounding `u(G)` via an interval-covering argument on `[a₁, C·a₁]` for an EXPLICIT small
constant `C` — i.e. try to prove `∏G<2a₁` (E5-★) directly by exhibiting, for any candidate `G` with
`∏G≥2a₁`, a genuinely different (non-sub-support) obstruction — e.g. via a direct greedy-choice
argument at the specific index realizing `u(G)`, tracking what integer the greedy rule would have
picked instead in `[a₁,∏G)` and showing it must already meet `G∖{p_max}`'s complement-of-witnesses
without invoking "sub-support of `G` is a term." I did not find this argument; flagging it as the
remaining honest direction distinct from what's been tried, but unexplored by me due to time.

### Distinct openings (summary for outliner)
- Density-of-`A` covering argument: DEAD (matches certified Obstruction).
- aimo-0447 grid-covering imported for upper bound: fails, no analogue; already fully used for lower
  bound (R1/R2, certified).
- aimo-0421 recursive dichotomy on prime fibers: empirically vacuous (all recruited primes show
  infinite/positive-density fiber; dichotomy never discriminates).
- New (conjectural, unproved) sharpening: at most one prime `>√a₁` per large-regime minimal support
  — numerically robust (772/772 seeds), but I found no proof avoiding the forbidden move.

### Candidate technique(s)
None of the density/covering techniques close the gap without the forbidden move. If pursued
further, the only remaining shape I can point to is a direct "trace the greedy choice at the
specific value `u(G)`" argument (not sub-support realization, but tracking what the *actual*
admissible-set structure forces the greedy rule to have produced strictly before `u(G)`) — unexplored,
flagged as a possible next lens, not a finding.

### Cheap-kill candidates
- None found on this lens beyond the negative structural fact: "primes dividing *some* term" is
  provably unbounded (`|Π_terms|=639` by `N=6000` for `a₁=375`, still growing) — so any argument
  must operate strictly on `𝓐_∞`/E1/E2-realized minimal supports, never on raw term divisors. This
  is a warning, not a pruning tool.

### Knowledge-base / crux entries consulted
- `aimo-0447` (`size-bounding-and-descent`): grid-covering `Σ1/p²<1/2` ⇒ distinct large primes ⇒
  primorial lower bound. Already fully imported as certified `R1/R2`
  (`lemmas/realizer-value-pincer.md`). No further juice found for the upper bound.
- `aimo-0421` (`divisibility-and-gcd`/`size-bounding-and-descent`): pigeonhole-on-finite-gcd-image +
  recursive dichotomy (infinite-fiber prime vs finite-fiber-everywhere). Structure doesn't transfer
  usefully — our analogous dichotomy is empirically one-sided (never hits the finite-fiber case for
  a genuine `Π`-member).
- `knowledge_base.md`: no dedicated covering-system/Σ1/p² entry found via grep beyond the crux
  corpus; no new named KB entry to add.

### Analogous past problems (cruxes)
- `aimo-0447` — genuinely analogous in *form* (a "which primes must occur, size-bound via
  primorial/grid-covering" problem) but its crux is already exhausted here (imported as R1/R2); it
  does not supply the missing upper bound.
- `aimo-0421` — analogous only in the "pigeonhole on divisor/gcd structure, infinite vs finite fiber"
  flavor; on inspection the dichotomy does not bite in this problem (see §3 above). Not a strong
  match beyond that structural echo.
- No other corpus entry found (via `size-bounding-and-descent` review) closer than these two.

### Prior progress
As stated in `current.md` / `redundant-constraint-antichain.md`: E1–E4, R1, R2, Prop 12.A, Prop 12.B
all certified; sole open gap E5″ (`∏(G∖{p_max})<a₁` for `∏G≥a₁`), equivalently E5-★ (`∏G<2a₁`).
Anchor-partition (Lemma A) certified as an equivalent reformulation (fiber finiteness), also proved
to collapse onto the same wall when closed via sub-support realization.

### Dead ends (do not retry)
- Raw density(`A`)/covering-fraction argument to force `Π` finite directly — certified dead
  (`monovariants-and-obstruction.md` Obstruction family, re-verified this round).
- aimo-0447 grid-covering re-applied hoping for an upper bound on `∏G` — no analogue exists; already
  fully exploited as the lower bound R1/R2.
- aimo-0421-style finite-fiber dichotomy on Π-primes — empirically vacuous, every recruited prime
  has positive-density (effectively infinite) fiber, so case (II) never triggers.
- (Reaffirmed from R4, not retried here) any argument whose closing step forces a proper sub-support
  `S⊊G` to be realized as a term to contradict minimality — proven to collapse to E5 verbatim.

### Small-case / intuition notes (all labeled CONJECTURE — not proofs)
- `max|G|≤4` on every tested seed (prior rounds; reconfirmed).
- `∏G/a₁≤1.45`, `redMax/a₁≤0.73` (prior rounds, `realizer-value-pincer.md`).
- NEW this round: for every large-regime minimal support tested (16 curated + 25 random seeds, 772
  supports total, `a₁` up to `5000`), **at most one prime of `G` exceeds `√a₁`** — a candidate
  sharper form of (W)/E5″, unproved, offered as possible outliner material.
- NEW this round: primes that enter `Π` (even "large" ones like `19` for `a₁=375`) recur with
  density `≈1/q` among terms once recruited (`19` hits `423/6000≈1/14` terms) — consistent with,
  but not proof of, the eventual-periodicity conjecture; also explains why fiber-based dichotomies
  (lever 3) don't discriminate.
- NEW this round (methodological caution): the set of primes dividing *some* term of the sequence
  (not restricted to minimal supports) is provably unbounded and still growing at `N=6000` terms —
  any covering/density argument must operate on `𝓐_∞` specifically, never on raw term-divisor sets.
