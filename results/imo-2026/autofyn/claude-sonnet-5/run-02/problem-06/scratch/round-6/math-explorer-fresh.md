# math-explorer (fresh-framing lens), round 6 — IMO 2026 P6 (imo-2026-06)

## Mandate
Per CLAUDE.md's explicit "break a shared-gap plateau" instruction: after 5 rounds all
three live lines (covering-system-construction, greedy-exchange-cost-potential,
witness-index-descent / reversible-transition-map) converged on ONE crux — the
Universal Singleton Hypothesis + "no collateral rogue pairs" — and three independent
monovariants died on the same "refinement manufactures bigger objects" wall. This
report does NOT patch that crux. It surveys genuinely different routes to the *whole*
problem and reports honestly where each would stall.

## What I read
`current.md` (all 493 lines, rounds 1–5), `knowledge_base.md`, and skimmed all 8
approach files. I will not re-derive the existing certified lemma stack; see
`current.md` §"Current best" for the full list (Free Facts, Bounded Gap Lemma,
Persistent-Type Pigeonhole, Finite Core Theorem, Canonical-Refinement Lemma, Lemma G,
Monotonicity of Resolution, Same-Side Ordering, Critical Prime Dichotomy / Lemma H).

## Crux-corpus mining (new resource, not previously used by this population)

I queried `past_crux_moves_database.json` (2434 cruxes) across **all three domains**
(number_theory, combinatorics, algebra), not just number_theory, per the task's
instruction, searching for "greedy sequence," "eventually periodic," "finite state,"
"complement," "compactness" load-bearing moves.

**Most important find: `aimo-0678`** (ISL/EGMO-flavor, France) — *"a_0,b_0≥2,
a_{n+1}=gcd(a_n,b_n)+1, b_{n+1}=lcm(a_n,b_n)-1; prove (a_n) is eventually periodic."*
This is the closest structural analog in the whole corpus to our problem (a coupled
integer recursion, prove eventual periodicity, no closed form). Its crux chain:
1. Isolate a regime (a_n | b_n) where the recursion simplifies, giving a frozen
   invariant s_n = a_n+b_n.
2. Build an explicit **integer monovariant** w_n = min{m ≥ a_n : m ∤ s_n}, prove it is
   non-increasing, hence eventually constant — this **bounds a_n** unconditionally.
3. Once a_n is bounded (finitely many values), reduce b_n modulo M := lcm(all
   attainable a_n values). Because the recursion a_{n+1}=gcd(a_n,b_n)+1,
   b_{n+1}=lcm(a_n,b_n)-1 is **memoryless** (a genuine 2-term Markov map), the pair
   (a_n, b_n mod M) is a deterministic function of (a_{n-1}, b_{n-1} mod M) alone.
   Finitely many such pairs ⟹ pigeonhole on the *state*, not on individual terms,
   forces the state sequence — hence (a_n) — eventually periodic.

**Why this is directly relevant, and why it does NOT bypass our crux.** Step 3's
finite-pigeonhole argument is *trivial once memorylessness is secured* — that's the
whole content of the proof, and it is exactly the "finite-automaton" framing
`reversible-transition-map` already tried and proved (this round's field) to be
*logically equivalent* to V = ∅. The crux-corpus find lets us say **precisely** why
aimo-0678 is easy where ours is hard: its recursion only ever looks at the PREVIOUS
pair (a_n,b_n) — two-term memory, closed under the map by construction. Our
recursion's defining condition — gcd(a_{n+1},a_i) > 1 for **every** i ≤ n, all the way
back to i=1 — is *a priori* infinite-memory; compressing it to bounded memory (a fixed
finite core S₀) is exactly the content of the Finite Core Theorem, and proving that
this compression is *permanently* sufficient (no term ever needs a "new" prime the
compressed state can't see) **is** the Universal Singleton Hypothesis / rogue-pair
gap. So aimo-0678's technique doesn't hand us a bypass — it hands us a clean
diagnosis: **our problem is exactly one gap harder than aimo-0678's paradigm**, because
our admissibility condition is a covering condition against a *growing* history rather
than a fixed 2-term state. This is worth recording in `knowledge_base.md` /
`current.md` so nobody re-proposes "just do the aimo-0678 trick" as if it were new.

**Secondary find:** `aimo-0077` (card-flipping game, extremal-principle) — *"assume
nontermination forces a repeating state-cycle in a finite state space (≤2^2008
configurations), take the MINIMAL card number flipped within that cycle, derive a
contradiction from minimality."* This is the same "finite state space ⟹ eventual cycle,
then minimize within the cycle" pattern as `witness-index-descent`'s dead well-ordering
attempt — confirms (again) that a bare minimal-counterexample-within-the-cycle argument
is the natural first thing to try and that our problem's specific obstruction (new
recruitment can create SMALLER witnessing indices than any seen so far, i.e. the
"cycle" itself is not stable under refinement) is a genuinely unusual failure mode, not
one this corpus's other pigeonhole-on-a-cycle problems exhibit. No new idea here beyond
confirming the existing RETHINK was justified.

**`aimo-0421`** (gcd-collision problem, "every prime divides only finitely many
elements of an infinite set ⟹ only finitely many elements meet a fixed pair") is the
right *flavor* of lemma (bounding "how many terms can share extra primes with a fixed
pair") but is a statement about an unstructured infinite set S, not a greedy/ordered
sequence — I could not find a way to adapt its finite-fiber pigeonhole to attack rogue
pairs specifically; flagging it as inspiration only, not a route.

I did not find any corpus crux (combinatorics or algebra) using a genuine
compactness/König's-lemma diagonal argument on greedy number sequences, nor a
Beatty-sequence rigidity crux applicable here — those ideas (below) are not corpus-backed
and would need to be built from scratch.

## Two genuinely different framings considered (not developed as full approaches)

### Framing 1 — Complement / "skipped integers" reframing
Define the complement C = {m > a_1 : m ∉ {a_n}}. Computed for a_1=175 (n up to 400):
density of C among (a_1, a_400] is noticeably concentrated on integers with a *small*
prime-support intersection with the currently realized types (as expected). The
reframing doesn't change the underlying object: m is skipped at stage n exactly when m
fails to hit some *realized* type among a_1..a_{n-1}, which is the same admissibility
condition as before, just phrased negatively. **Verdict: not a new proof route** — it's
a restatement, and would hit the identical rogue-pair wall, since "which finite type
family determines skippedness" is precisely the open question. Not recommending
further pursuit as a primary-gap attack (matches the pattern CLAUDE.md warns about:
routing around the gap in the same framing).

### Framing 2 — Bound the *number of recruitment rounds* by a prime-counting argument
(rather than proving V = ∅ outright)
Idea: instead of proving no rogue pair ever needs a new prime (V=∅ forever), directly
upper-bound the total number of recruitment rounds ever needed by something like
Ω(a_1) or the number of distinct primes dividing any single early term — i.e., show the
recruitment process is a strictly decreasing function of some quantity tied to a_1's
factorization, so it terminates in ≤ f(a_1) rounds regardless of whether V=∅ is ever
literally achieved. This would be weaker (doesn't need the Universal Singleton
Hypothesis at all) and would only need "recruitment rounds are finite," feeding the same
CRT finish with S := the terminal (finite, by this bound) core.

**Small computational probe** (a_1 = 6,10,12,30,35,175 — the seeds named in the task):
only a_1=175 among these has |Q| ≥ 2 with any nontrivial rogue-pair structure at all
(the others have |Q|=1, the fully-solved trivial case per current.md item #10, or
collapse immediately). This is too thin a sample to test a "rounds ≤ f(a_1)" bound
against — round 5's own testing (up to ~200 seeds) never observed more than ONE
recruitment round, which is *consistent* with such a bound existing (e.g. rounds ≤
|Q|−1, or rounds ≤ ω(a_1)) but the field has not yet tried to prove any such
**explicit numeric cap** directly — every prior attempt tried to prove the cap is
literally 0 or that the *set* V is literally empty, not that the round-count is merely
*finite*. This is a strictly easier target than V=∅ and has NOT been tried.
**Where it would likely stall:** to bound rounds by f(a_1) you'd need to show each
recruitment round consumes a resource that only has f(a_1)-many "charges" — the natural
candidate (number of distinct primes in a_1, or in the earliest terms) doesn't obviously
decrease under recruitment, since a rogue pair's recruited prime need not come from
a_1's factorization at all (in the 175-example chain, 13 was recruited, not a prime of
175=5²·7). So the natural charging argument doesn't have an obvious accounting object
yet — this is a real gap in the idea, not a finished route, but it is a genuinely
different target (finiteness of round-count vs. exact emptiness of V) that the existing
population has not attempted and that would suffice for the same CRT finish.

## Recommendation for next round
1. **Record the aimo-0678 diagnosis** in `current.md` (why the "obvious" finite-automaton
   trick from the closest corpus analog does NOT bypass our crux, and precisely which
   extra structural fact — memorylessness — our recursion lacks) so no future round
   re-proposes it as new.
2. **Open one new approach** on Framing 2 (bounding the NUMBER of recruitment rounds by
   an explicit function of a_1, rather than proving V=∅/Universal Singleton Hypothesis
   outright) — genuinely weaker target, not yet attempted, still sufficient for the CRT
   finish. Needs a charging/potential argument for what a recruitment round consumes;
   none identified yet, flagged as the immediate open sub-problem for whoever picks
   this up.
3. Framing 1 (complement) is **not** recommended as a new build — confirmed to be a
   restatement of the same open condition, not a different attack.
4. Do not re-attempt: any bare finite-automaton/state-pigeonhole argument (aimo-0678
   style) without first separately closing the memorylessness gap — that is just
   `reversible-transition-map` again, already shown equivalent to V=∅.

## Files
- Read (no edits): `/home/agentuser/repo/results/imo-2026-06/current.md`,
  `/home/agentuser/repo/knowledge_base.md`,
  `/home/agentuser/repo/crux_moves_documentation.md`,
  `/home/agentuser/repo/past_crux_moves_database.json`,
  `/home/agentuser/repo/past_problems_database.json`,
  all files under `/home/agentuser/repo/results/imo-2026-06/approaches/` (skimmed).
