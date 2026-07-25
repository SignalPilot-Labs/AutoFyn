## imo-2026-01 (confluence / abstract-rewriting-system lens)

### Key structural fact (the reduction that makes everything else work)
Fix a prime `p` and let `x_i = v_p(a_i)` be the exponent of `p` in board entry `a_i`.
For any prime `p`, `v_p(gcd(m,n)) = min(v_p(m),v_p(n))` and
`v_p(lcm(m,n)/gcd(m,n)) = max(v_p(m),v_p(n)) - min(v_p(m),v_p(n)) = |v_p(m)-v_p(n)|`.
So **a single board move acts on the exponent-vector of every prime independently and
identically**: it replaces the pair `(a,b)` at the touched positions with
`(min(a,b), |a-b|)`. This is *exactly one step of the subtractive Euclidean algorithm*
applied simultaneously, prime-by-prime, to the two chosen board slots. This single
observation is the crux move for BOTH parts, and it turns the problem into 2026-vector /
per-prime bookkeeping instead of an ad hoc gcd/lcm argument.

Two elementary identities (verified symbolically and by a 200000-trial random sweep in
Python, see below) drive everything:
1. **Invariant identity**: `gcd(min(a,b), |a-b|) = gcd(a,b)` for all nonnegative integers
   `a,b` (standard Euclidean-algorithm fact).
2. **Monovariant identity**: `min(a,b)^2 + |a-b|^2 ≤ a^2+b^2`, with equality iff
   `min(a,b)=0`, and strict inequality whenever `a,b>0` and `a≠b`.

### Distinct openings
1. **Part (a) via lexicographic potential (fully worked, ready to write up).**
   Let `N` = number of board entries `>1`, and `Σ = Σ_i Σ_p v_p(a_i)^2` (sum, over all
   board entries and all primes, of the square of each prime's exponent — a finite
   nonnegative integer since almost all exponents are 0). Claim: every move strictly
   decreases the pair `(N, Σ)` in lexicographic order.
   - `N` never increases: writing `g=gcd(m,n)`, `q=lcm(m,n)/gcd(m,n)`, we have
     `g·q = lcm(m,n) ≥ max(m,n) > 1`, so **not both** of `g,q` can equal 1; hence the
     move turns 2 entries `>1` into at least 1 entry `>1`, i.e. `N` drops by 0 or 1.
   - When `N` is unchanged (both `g,q>1`), some prime `p` divides `gcd(m,n)`
     (else `gcd(m,n)=1` forces `q=mn`, `g=1`, contradicting `g>1`); for that prime,
     `min(v_p(m),v_p(n))>0` and `v_p(m)≠v_p(n)` is not required — strict decrease of
     `Σ` needs only ONE prime with `min>0`, giving `Σ` strictly smaller (identity 2 above,
     summed over all primes, is non-increasing per prime and strictly decreasing for at
     least the primes dividing `gcd(m,n)`).
   - `(N,Σ) ∈ ℕ×ℕ` lexicographically well-ordered ⟹ process terminates.
   - Termination value of `N`: since `N` starts at 2026 and drops by at most 1 per move
     (never skips from 2 to 0), and the process only *stops* when `N≤1` (fewer than two
     entries `>1` left to pick), the terminal `N` is **exactly 1**. This directly gives
     part (a), including the "exactly one" (not zero) count, for free.
2. **Part (b) via the exact per-prime invariant (fully worked, ready to write up).**
   For each prime `p`, define `G_p = gcd(v_p(a_1), …, v_p(a_2026))` (ordinary integer
   gcd of the 2026 exponents, using `gcd(x,0)=x`). By identity 1 above, a move replaces
   the touched pair's contribution `gcd(x_i,x_j)` with `gcd(min(x_i,x_j),|x_i-x_j|)`,
   which is the SAME value; since `gcd` of a whole multiset equals the gcd of any two
   entries combined with the gcd of the rest, `G_p` is an **exact invariant** of every
   move, for every prime `p` simultaneously. At the terminal state (`N=1`), the exponent
   multiset for prime `p` is `(v_p(M), 0, 0, …, 0)`, so `gcd` of that multiset is exactly
   `v_p(M)`. Hence **`v_p(M) = G_p` for every prime `p`, independent of Confucius's
   choices** — this pins down `M = ∏_p p^{G_p}` exactly, proving (b) directly without
   ever needing a confluence/diamond-lemma argument. (Only finitely many primes have
   `G_p>0`, namely those dividing at least one — actually all — of the `a_i`... more
   precisely those dividing `gcd`... need care: `G_p>0` iff `p` divides every `a_i`? No:
   `G_p = gcd of exponents`, which is `>0` whenever the exponents aren't "eventually
   arbitrary"; concretely `G_p` is well-defined and finite for every prime dividing ANY
   `a_i`, and `G_p=0` is possible even if `p` divides some `a_i` — e.g. exponents
   `(1,2)` have `gcd=1`, not 0; exponents `(1,0)` (p divides one number, not the other)
   have `gcd(1,0)=1`. Actually `G_p=0` can only happen if `p` divides NONE of the `a_i`
   (all exponents 0), OR more subtly if... check: `gcd(1,0)=1≠0`. In general
   `gcd(x_1,...,x_k)=0` iff all `x_i=0`. So `G_p>0` for every prime `p` dividing at least
   one `a_i`. This needs to be double-checked/stated carefully in the outline — it does
   NOT mean `M` is huge; `M = ∏_p p^{G_p}` is exactly the answer and the product is
   automatically finite since only finitely many primes divide any `a_i`.)
3. **Confluence / Newman's-lemma framing (the assigned lens, but a dead-weight
   alternative once opening 2 is available).** One could instead prove local confluence
   — any two single moves from the same board state can be joined by further move
   sequences reaching a common state — and invoke termination (opening 1) + Newman's
   lemma to get global confluence, hence uniqueness of the normal form `M`. This is a
   valid alternative route, but it is *strictly more work* than opening 2: local
   confluence for this rewriting system is itself proved by essentially the same
   per-prime `gcd`-invariant argument (you'd show two different move choices both
   preserve `G_p`, so both roads lead to a state with the same `G_p` data, which is
   basically re-deriving opening 2 through extra machinery). **Recommendation: use
   opening 2 as the primary route for (b); do not build a full Newman's-lemma
   apparatus — it buys nothing extra here since the exact invariant already gives
   uniqueness directly, and (b) reduces to a two-line invariant computation, not an
   induction on rewrite length.**
4. **Direct product/size monovariant (weaker, but a simple gut-check
   for (a) alone).** Product `∏ a_i` over the board is non-increasing (`gq = lcm(m,n) =
   mn/gcd(m,n) ≤ mn`), strictly decreasing unless `gcd(m,n)=1`. Alone this does NOT
   prove termination (coprime moves can preserve the product indefinitely in principle),
   so it must be paired with the `N`-drop argument from opening 1 — consistent with, and
   subsumed by, opening 1's lexicographic potential. Useful only as a secondary sanity
   check / alternate phrasing, not a new route.

### Candidate technique(s)
- Per-prime exponent-vector reduction of the gcd/lcm move to the *subtractive Euclidean
  algorithm step* `(a,b) ↦ (min(a,b), |a-b|)` — this is the master technique, applies
  to both parts.
- Well-founded lexicographic monovariant `(N, Σ)` for termination (part a).
- Exact invariant `G_p = gcd` of a prime's exponent multiset, for uniqueness (part b).
- Newman's lemma / confluence is available as a backup framing but is redundant once the
  exact invariant is in hand (see opening 3).

### Cheap-kill candidates
- The "product of all board numbers" monovariant alone is NOT sufficient for
  termination (fails to rule out infinite coprime-move loops) — ruled out as a
  standalone proof of (a), but valid combined with the count `N`.
- v_p(gcd of the NUMBERS) (i.e. `min` of exponents) is NOT the right invariant for (b) —
  I initially conflated "gcd of the exponent list" with "v_p of gcd of the numbers";
  these are different operations (`min` vs integer-`gcd`) and only the latter
  (`gcd of exponents`) is preserved by the move. Flag this for the outliner/builder:
  it is an easy sign error to make, verify with the identity `gcd(min(a,b),|a-b|)=gcd(a,b)`,
  NOT `min(min(a,b),|a-b|)=min(a,b)` (false in general, e.g. a=3,b=5: min=3,diff=2,
  min(3,2)=2≠min(3,5)=3).

### Knowledge-base entries to use
- **Number Theory / Divisor analysis**: gcd/lcm structure, exactly the `v_p` bookkeeping
  used above.
- **Number Theory / Modular arithmetic** section's general "reduce prime-by-prime"
  ethos (CRT-style independence across primes) — motivates treating each prime's
  exponent vector separately.
- **Combinatorics / Invariants & monovariants**: "a quantity preserved (or monotone)
  across moves" — directly the technique for both (a) (monovariant `(N,Σ)`) and (b)
  (invariant `G_p`).
- **General Proof Methods / Invariant-monovariant**: same, generic citation.
- No entry in `knowledge_base.md` is titled "Newman's lemma" or "confluence" — it is not
  present in the KB; if used, it would need to be stated and proved from scratch (finite
  branching + termination ⟹ every maximal chain from a state reaches the same normal
  form, standard diamond-lemma argument), but as noted, opening 2 supersedes it.

### Analogous past problems (cruxes)
- Searched `past_crux_moves_database.json` for `gcd`, `lcm`, `blackboard`, `euclidean`,
  `valuation`, and the `invariants-and-monovariants` / `processes-and-algorithms`
  subtopics (number_theory & combinatorics domains). No problem with the *same*
  gcd/lcm-swap mechanic was found.
- **`aimo-0836`** (China, "board of 1..n, move erases a,b writes a+b and |a-b| if
  absent") is the closest surface-level analog: it's also a two-element
  sum/difference-type rewrite process with a "double a pair via two moves" gadget and a
  minimal-counterexample descent argument for reducibility. The MECHANIC differs (their
  outputs are `a+b, |a-b|`, ours are `gcd(m,n), lcm(m,n)/gcd(m,n)` — genuinely different
  operations, not the same up to relabeling), so this is a *weak* analogy: useful only
  as a reminder that "sum/difference-flavored rewrite processes on a board" are a known
  crux family and that Euclidean-algorithm-style potential arguments (`min`/`|diff|`,
  monotone sum-of-squares) are the standard tool there too — but no lemma or invariant
  transfers directly.
- No stronger match found. Judgment: **none of the corpus problems are genuinely
  analogous enough to borrow a specific crux move from**; the per-prime reduction here
  is problem-specific to the gcd/lcm-swap mechanic.

### Prior progress
None — `results/imo-2026-01/current.md` and `approaches/` are empty; this is round 1,
first exploration of this problem.

### Dead ends (do not retry)
- None recorded yet (fresh problem). Self-flagged near-miss during this exploration:
  conflating "gcd of the exponent multiset" (`G_p`, the correct invariant) with "`v_p`
  of the gcd of the actual numbers" (`min` of exponents, NOT invariant) — see
  Cheap-kill section. Any approach that tries to identify `M` with
  `gcd(a_1,...,a_2026)` or with `lcm(a_1,...,a_2026)` is wrong; verified numerically
  (e.g. board `[12,18,20]`: `gcd=2`, `lcm=180`, but the actual terminal value is `30 =
  2^{gcd(2,1,2)}·3^{gcd(1,2,0)}·5^{gcd(0,0,1)} = 2^1·3^1·5^1`).

### Small-case / intuition notes (computational, labeled as verified-by-simulation
conjecture until written as a rigorous proof)
Ran a Python simulation (`gcd`/`lcm` moves applied in random order until stuck) on 6
test boards, each with 20 random move-orderings, and compared the observed unique
survivor `M` against the predicted closed form
`M = ∏_p p^{gcd(v_p(a_1),…,v_p(a_k))}`:

```
[12, 18, 20]                         predicted 30   observed {30}   (always terminates, ~5 moves)
[8, 12, 18, 30]                      predicted 30   observed {30}
[2,3,4,5,6,7,8,9,10]                 predicted 210  observed {210}
[100, 225, 60, 36]                   predicted 60   observed {60}
[2026,2026,2026,2026,2026]           predicted 2026 observed {2026}
[30,105,70,42]                       predicted 210  observed {210}
```
Every trial terminated (no cycling observed, consistent with the lexicographic-potential
proof) and every trial's final `M` matched the closed form exactly, across all random
move orders tested — strong computational confirmation of both (a) (termination) and
(b) (order-independence + the specific value) for these instances. This is evidence,
not a proof, but combined with the algebraic identities verified above (200k-trial
symbolic sweep of `gcd(min(a,b),|a-b|)=gcd(a,b)` and the sum-of-squares monotonicity),
the outliner should treat the closed-form answer
`M = ∏_p p^{gcd(v_p(a_1),…,v_p(a_2026))}` and the `(N,Σ)` termination potential as
essentially proof-ready, not merely conjectural — the remaining work is writing the
argument up rigorously and double-checking the "not both g,q equal 1" and "`G_p` well
defined / finite product" edge cases explicitly.
