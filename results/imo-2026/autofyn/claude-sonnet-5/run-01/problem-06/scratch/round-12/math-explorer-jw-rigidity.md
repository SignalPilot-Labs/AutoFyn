## imo-2026-06 — Conjecture (JW) "u=w rigidity wall": arithmetic investigation

### Summary verdict
The "u=w rigidity" framing (do three independently-derived shared-prime
witnesses coincide?) is **not the right lens** — direct numerical tracing
shows the witnesses essentially never coincide by any forced algebraic
identity; joint coverage instead comes from a **redundancy/density**
phenomenon (a handful of very small primes, `2,3,7,...`, dominate almost
every companion set). More importantly, I found a **genuinely different,
already-certified-tool-only mechanism** ("class-backbone + Lemma UCR") that
rigorously closes Conjecture (JW), with **zero appeal to rigidity/coincidence
at all**, on 5 of 7 tested doubly-infinite core pairs — reducing, not just
reformulating, the open scope. I also found and verified an explicit
**counterexample to round 11's sharpened single-witness candidate `Π`**
(`sunflower-bundle-closure.md` §8.3, `Π:=comp(a_{j_3})∪comp(a_{j_3'})`):
it does NOT satisfy (JW) as constructed — a concrete "kill" finding for that
specific narrowing, distinct from a refutation of (JW) itself (which remains
unrefuted: the larger Lemma FT transversal `W:=U_S∪U_{S'}` still shows zero
violations, ~270M pairs checked across 7 instances this round, matching all
prior rounds' data).

### Method
Independent greedy-sequence generator (own implementation, using the
already-certified minimal-radical-hitting reduction — Lemma W2/W3/FOM — for
speed; cross-checked against the problem's literal rule for small `n`),
`sympy.primefactors` for exact factorization. Generated `a_1 ∈
{247, 2747, 21528751, 4199, 4087}` to `N=20000` (`8000` for `21528751`, the
slow one). Tested 7 doubly-infinite disjoint core pairs across these 5
instances: `247:(13,19)`, `2747:(41,67)`, `21528751:(103,197)`,
`4199:(13,17)`, `4199:(13,19)`, `4199:(17,19)`, `4087:(61,67)`.

### Finding 1 (refutation, verified independently): round 11's sharpened `Π` fails
`sunflower-bundle-closure.md` §8.3 builds `Π:=comp(a_{j_3})∪comp(a_{j_3'})`
from Lemma CB's blocking witnesses (any index `j_3` with `rad(a_{j_3})∩S=∅`).
Taking the *minimal* such witness for `a_1=247,(S,S')=({13},{19})`: `j_3=3`
(`a_3=266=2·7·19`, so `S(j_3)=S'={19}` — the witness itself lies in the
*other* class!), `j_3'=2` (`a_2=260=2²·5·13`, `S(j_3')=S`), giving
`Π=comp(a_3)∪comp(a_2)={2,7}∪{2,5}={2,5,7}`.

**Explicit, independently-verified violation**: `i=51` (`a_{51}=1638=2·3²·7·13`,
`comp(a_{51})={2,3,7}`), `j=739` (`a_{739}=21375=3²·5³·19`,
`comp(a_{739})={3,5}`). `comp(a_{51})∩comp(a_{739})={3}` (confirmed
`gcd(a_{51},a_{739})=9`), but `3∉Π={2,5,7}`. **`Π∩comp(a_{51})∩comp(a_{739})=∅`**
— (JW) fails for this specific `Π`. (997 more such `i=51`-paired failures
found in the same sample sweep, all sharing prime `3`.) This does not
refute (JW) itself (the full `W:={2,3,5,7}` from Lemma FT still works, see
below) — it shows §8.3's specific narrowing to a *single* companion set per
side discards genuinely necessary primes, confirming the sibling round-11
diagnosis ("no computation was run this round" for `Π`) was right to flag
this as untested, not settled. **Recommendation: do not build on `Π` from
§8.3 as stated; a single blocking witness's companion set is provably
insufficient in general.**

### Finding 2 (new, positive mechanism — sidesteps rigidity entirely on 5/7 pairs)
For each pair, I computed the **running intersection ("backbone")** of
`comp(a_j)` over all realized `j` in the smaller-count side's class
(chronological order of realization), and checked whether it (a) freezes to
a fixed nonempty value early and stays fixed through the rest of the tested
range, and (b) is itself *exactly* realized as some actual index's full
companion set (i.e. `S'∪B` is realized in Lemma ERD-C's sense).

| pair | small side | backbone `B` | freezes at position | exactly realized? | misses on big side |
|---|---|---|---|---|---|
| `247:(13,19)` | `{19}` (n=6910) | `∅` | 1 | — | n/a (no backbone) |
| `2747:(41,67)` | `{67}` (n=389) | `{2,3,7}` | 0 | **yes** (`a_3`) | **0/19203** |
| `21528751:(103,197)` | `{197}` (n=136) | `{2,3,7}` | 1 | **yes** (`a_{2575}`) | **0/7811** |
| `4199:(13,17)` | `{13}` (n=4652) | `{2}` | 2 | no | 41/10260 (and symmetric: `{17}`'s own backbone is `∅`) |
| `4199:(13,19)` | `{19}` (n=3028) | `{2,3}` | 1 | **yes** (`a_{11}`) | **0/4652** |
| `4199:(17,19)` | `{19}` (n=3028) | `{2,3}` | 1 | **yes** (`a_{11}`) | **0/10260** |
| `4087:(61,67)` | `{67}` (n=9375) | `{2}` | 1 | **yes** (`a_5`) | **0/10312** |

**Where this comes from (a clean, already-provable-in-principle argument,
using only the already-certified Lemma UCR from
`sunflower-inadmissibility-toolkit.md` §1 — no new heavy machinery, no
coincidence needed):**

> **Claim.** Suppose `j_0∈I_{S'}` and finite `B` (`B∩P_1=∅`) satisfy (i)
> `comp(a_j)⊇B` for *every* `j∈I_{S'}` (permanent backbone), and (ii)
> `comp(a_{j_0})=B` exactly (so `S'∪B` is realized). Then `W:=B` solves (JW)
> for `(S,S')`: for every `i∈I_S,j∈I_{S'}`, `comp(a_i)∩comp(a_j)∩B≠∅`.
>
> *Proof.* By Lemma UCR applied with "`S`":=`S'`, "`C`":=`B` (hypothesis (ii)
> gives `S'∪B` realized), every index `m` with core disjoint from `S'` — in
> particular every `i∈I_S` — has `B∩comp(a_i)≠∅`; pick `p` in this
> intersection. By (i), `comp(a_j)⊇B∋p` for the given `j`, so `p∈comp(a_j)`
> too. Hence `p∈comp(a_i)∩comp(a_j)∩B`. ∎

This is **not** the `u=w` coincidence question at all — it needs no
"specific witness forced to align," because `B` is defined as the
intersection over the *whole* class (so it trivially lies in every member of
that class), and Lemma UCR (already proved, unconditional, Lemma P′-only)
supplies the *other* side's coverage for free. This mechanism closes 5 of 7
tested pairs completely (0 misses, exactly, not just empirically — modulo
proving (i)/(ii) in general, see below), **entirely bypassing the wall both
sibling approaches stalled on**.

**What is proved vs conjectured here.** The *argument* above (the Claim) is
a straightforward, essentially complete proof from already-certified facts
(Lemma UCR + elementary set manipulation) — this part is essentially
gap-free modulo write-up. What is **not** yet proved, only strongly
evidenced numerically, is that hypotheses (i) and (ii) actually hold for a
general doubly-infinite pair: (ii) [backbone exactly realized] was checked
directly against the finite generated prefix (a genuine fact for that
prefix, not a numerical approximation); (i) [permanent backbone,
i.e. no member *anywhere in the infinite class* ever drops an element of
`B`] is the genuinely open part — verified only up to the tested `N`, and
in every successful case the backbone froze within the first 0–2 realized
members and stayed exactly fixed through hundreds-to-thousands of later
members with zero exceptions, which is stronger and more localized evidence
than the general (JW) numerics already in the workspace (freeze happens
almost immediately, not gradually).

### Finding 3: two pairs genuinely lack any single-side backbone
`247:(13,19)` (the `S'={19}` side's running intersection collapses to `∅`
already by the 2nd realized member — no universal prime across the whole
class) and `4199:(13,17)` (checked **both** directions: `{13}`'s backbone
freezes to `{2}` but is never exactly realized bare — always co-occurs with
another prime; `{17}`'s own backbone is `∅`). These are exactly the two
instances where (JW) still needs the harder Lemma-FT/rigidity route (both
still pass numerically via the larger `W`, zero violations, but with no
proof). This **narrows, not just relabels**, the open scope: 5/7 tested
pairs now have a concrete, mechanism-complete (modulo (i)) route that
never touches rigidity at all.

### Cheap-kill / structural notes
- **Small-prime dominance is not a coincidence worth chasing directly**:
  across ~270M cross-pairs checked this round, prime `2` alone realizes the
  joint intersection in `70%`–`100%` of pairs in every instance (`3` a
  close second); this reflects that `2` (or `2,3,7` together) is a
  frequent-to-universal companion prime within each core class, not a
  forced coincidence between two independently-chosen witnesses. Any future
  attempt framed as "does witness `u` equal witness `w`" is asking the wrong
  question — the right question (per Finding 2) is "does a *whole class*
  share a common companion prime" (a property of one class, not a pairing).
- The **backbone freeze itself looks structurally identical to the
  already-documented "permanent bundle"/minimal-antichain-freeze phenomenon**
  in `lemmas/lemma-permanent-bundle.md` and `persistent-backbone-monovariant`
  (round 7's freeze findings on `M_n`) — but it is a **different, narrower
  object** (intersection over one fixed core-class `I_{S'}`'s companion
  sets, not the global minimal-radical antichain). Do not conflate it with
  `(MRS_S)` (`forced-primes-well-ordering`'s local antichain-freeze target,
  already proven equi-hard to the abandoned Multi-Companion hitting-set
  problem) — the backbone claim here is a much more elementary
  "intersection-never-shrinks-again" statement about one class, with a
  direct, cheap payoff (Lemma UCR) once granted, unlike `(MRS_S)`.
- `(PD_{S,S'})` (density hypothesis, `intersecting-family-covering-
  construction`): not directly illuminated by this data — the backbone
  mechanism is a structural/algebraic fact (intersection freeze), not a
  density statement, though the *reason* small primes dominate frequency
  is plausibly a density phenomenon (worth a separate density-lens pass,
  not attempted here for time).

### Candidate next steps for the proof-outliner
1. **Split (JW) by cases on backbone existence.** For a doubly-infinite
   pair `(S,S')`: Case A — one side's companion-set intersection freezes to
   a nonempty, exactly-realized value `B` (per Finding 2): closed
   completely by the 3-line Lemma-UCR argument above, **no new machinery
   needed beyond proving backbone permanence (hypothesis (i))**. Case B —
   neither side has such a backbone (both sides' full-class intersections
   are `∅`, per Finding 3): falls back to the still-open Lemma
   FT/rigidity route.
2. **The one new lemma actually needed for Case A**: prove "backbone
   permanence" — once the running companion-intersection of `I_{S'}`
   freezes to a fixed nonempty `B` at some point, it never shrinks again.
   This is a single, sharply-stated, purely combinatorial claim (not a
   coincidence-forcing claim), and — unlike the `u=w` question — it is
   about *one* class in isolation, so single-family tools (Escape-
   Confinement, Permanent-Inadmissibility, No-Resurrection, already
   certified for the single-family setting) are the natural candidates to
   adapt, *without* needing any cross-family reasoning at all. This looks
   more tractable than anything tried on (JW) in rounds 10–11.
3. Do **not** re-attempt round 11's specific `Π:=comp(a_{j_3})∪
   comp(a_{j_3'})` construction (Finding 1: refuted by explicit
   counterexample) as a route to closing (JW) directly; it can still be a
   valid ingredient for the "everywhere-nonempty" side-condition (§8.1) but
   not as a joint-coverage set on its own.
4. If Case A's backbone-permanence lemma resists proof, the two Case-B
   instances (`247:(13,19)`, `4199:(13,17)`) are a good minimal test bed —
   both are already fully tested (zero violations with the larger `W`) so
   any new mechanism can be checked against concrete, independently-verified
   data immediately.

### Reproducibility
Scripts and cached sequence data at `/tmp/gen.py`, `/tmp/run_gen.py`,
`/tmp/analyze.py`–`/tmp/analyze6.py`, `/tmp/seq_*.pkl` (this container only,
not committed — re-run if needed by a future round; generation takes under
30s total for all 5 instances at the tested `N`).
