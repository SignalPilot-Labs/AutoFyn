## imo-2026-06 — Lens: hunt for a genuinely NEW top-level mechanism/technique
(not yet tried in any form across rounds 1–6), targeting either the
multi-companion-bundle-finiteness gap in `𝓥_S`, or a route around FCBC/`𝓥_S`
entirely.

**Headline verdict: no genuinely new mechanism found that escapes the gap.**
Two candidates looked initially promising and got real analytical + numerical
work this session; both are shown below to either (a) fail quantitatively on
contact with this problem's actual structure, or (b) reduce, on honest
inspection, to an already-certified round-1 fact (Lemma R) whose own
certification note already flags "strengthening this to uniformity is exactly
the open gap" — i.e. they are not new escapes, they are the gap restated via a
different construction. This is itself a useful, load-bearing negative result
(two more falsifiable "obvious next things" now closed off), not a null report.

### What's been tried — brief map (read for full detail: `current.md`, the 8
`approaches/*.md` files, and `/tmp/round-5/`, `/tmp/round-6/` explorer reports)

Confirmed already exhausted (do not re-suggest to the outliner):
- Edge-clique-cover / infinite Ramsey on the whole problem (round 5,
  `math-explorer-fresh-framing.md` opening 1) — proved equivalent to FCBC in
  graph language, not a bypass.
- Morse–Hedlund / subword complexity (round 5, opening 3) — cannot exclude
  Sturmian-type aperiodic-but-low-complexity behavior without smuggling in a
  finite-backbone argument.
- Ultrafilter/compactness limit (round 5, opening 5) — strictly weaker than
  the already-tried Pool-Lemma compactness framing.
- Generating-function encoding (round 5, opening 6) — the greedy min-rule
  doesn't linearize.
- Bounded-clique-size transversal / `ω(a_n)=O(1)⟹` FCBC (round 5, opening 4;
  round 3 ND1/ND2) — gives only the vacuous "Single-Cover" (`H=rad(a_1)`
  always trivially works and carries zero information — round 5's "L-first
  necessity" lemma, opening 2, proves this formally).
- Analytic/density/Mertens/Borel–Cantelli/second-moment on `Σ1/q` or
  `ΣD_n(q)²` (round 6, `math-explorer-analytic-tools.md`) — structurally
  mismatched: bounds *concurrent* state or density, not *cumulative distinct
  arrivals*; no randomness to exploit (fully deterministic sequence).
- Compactness/König's lemma on the tree of candidate covering sets (round 4,
  folded into `explicit-window-backbone-construction`'s Lemma W4 Pool
  Lemma) — proved FCBC equivalent to pool-existence via elementary finite
  descent; the write-up explicitly notes König's lemma gives the identical
  equivalence, no added power.
- Recursive/nested induction on core depth `|S|` (round 6,
  `core-depth-induction.md`) — Step 3's "depth-d→depth-(d-1) companion reuse"
  reduction concretely refuted (12 of 13 fresh values on the round's own
  motivating example do not have the conjectured shape).
- Crux corpus: `aimo-0477` (bounded ascending divisor chain — needs a fixed
  finite ambient lattice, doesn't transfer), `aimo-0134` (monovariant +
  difference-identity transfer — no monotone quantity found), `aimo-0628`
  (residue-sparseness + Fermat forcing — wrong direction), `aimo-0157`/
  `aimo-0611` (Zsigmondy — wrong direction, guarantees new primes, opposite of
  what's needed) — all checked and killed in rounds 3–6.

### Candidate 1 (new this session): the `aimo-0447` grid/density-counting crux

`aimo-0447` (IMO 2019 SL N8, "if `gcd(a+i,b+j)>1` for all `0≤i,j≤n` then
`min{a,b}>(cn)^{n/2}`") was **not previously checked** by any prior round (not
in any approach file's crux list, not in round 5/6's corpus searches, which
targeted `sequences-and-recurrences`/`processes-and-algorithms`-flavored
cruxes, not this one, filed under `divisibility-and-gcd`). Its crux move is
structurally very close to our problem: encode a "pairwise `gcd>1`"
hypothesis by placing a witnessing prime in each grid cell, then show small
primes can only cover a bounded fraction of cells (since `Σ_p 1/p²<1/2`, a
**convergent** series, unlike the divergent `Σ1/p` round 6 already
correctly flagged as the wrong resource to exploit) — forcing large,
necessarily-distinct primes into some row, and hence a huge product lower
bound.

**Adaptation attempted.** Our sequence satisfies the exact hypothesis type
(Lemma P′: `gcd(a_i,a_j)>1` for *every* pair, not just a finite grid) and,
via the already-certified Lemma 1 (`lemmas/lemma-1-uniform-gap-bound.md`,
unconditional), `a_N = O(N)` — giving an analogous "range `R=O(N)` over `N`
distinct integers" setup. This gives, unconditionally and elementarily
(no new machinery): for any prime `p`, `m_p(N):=|\{i≤N:p\mid a_i\}|≤R/p+1
=O(N/p)`, and since every pair needs a witnessing prime,
`Σ_p C(m_p(N),2) ≥ C(N,2)`.

**Why it fails quantitatively (numerically confirmed, not just suspected).**
`aimo-0447`'s argument needs the "small-prime" contribution
`Σ_{p small}m_p(N)²` to be **below** half the total pair count so the
deficiency is forced onto large primes. In `aimo-0447`'s own problem this
works because the range length equals `n` (the same order as the grid side).
In our problem the range is `R=O(\mathrm{rad}(a_1)\cdot N)`, a *constant
multiple* of `N` — and that constant is exactly `\mathrm{rad}(a_1)≥2`, not
`1`. Checked directly (`/tmp/round-7/density_check.py`, `N=1500`,
`a_1=247,2747,91`): summing `m_p(N)²` over just `p≤200` already gives
`3.46×10^6`–`4.66×10^6`, i.e. **3.5–4.1× larger** than `N²/2=1.125×10^6` —
the deficiency needed for the argument never materializes; small primes
(`2,3,5,7,…`, essentially never in `P_1`) already overwhelm the pair budget
by themselves (e.g. prime `2` alone divides `1267`/`1500`, `1051`/`1500`,
`1425`/`1500` of the first `1500` terms in the three test cases). **This is a
clean, decisive numerical refutation of the direct transplant** — not merely
"didn't find a use," an actual quantitative failure, so it should not be
retried without a fundamentally different accounting (e.g. some argument
specific to *this* problem's small-prime structure that this session did not
find).

**Verdict: dead end, but worth recording precisely** (a plausible-looking
crux match, now closed off with numbers, rather than "not found insufficient
by inspection").

### Candidate 2 (new this session): canonical/min-homogeneous Ramsey
extraction on the pairwise-intersecting radical family

Idea: since every vertex `i` of the complete "shares-a-prime" graph on
indices (Lemma P′) sees only finitely many "colors" (any witnessing prime for
edge `(i,j)` necessarily divides `a_i`, hence lies in the finite set
`rad(a_i)`), the *standard* diagonal construction for Ramsey's theorem on
locally-finite-but-not-globally-bounded colorings applies: pick `t_1=1`, use
finite pigeonhole on `rad(a_{t_1})`'s colors to extract an infinite
monochromatic-from-`t_1` set, let `t_2` be its minimum, repeat. This
produces `t_1<t_2<t_3<\cdots` and primes `c_1,c_2,c_3,\dots` (each
`c_i\in\mathrm{rad}(a_{t_i})`) such that for all `i<j`, `c_i\mid
\gcd(a_{t_i},a_{t_j})` — a "min-homogeneous" infinite subsequence.

**On inspection, this is exactly Lemma R iterated, and Lemma R's own
certification note already says why it doesn't close the gap.** The
*single-step* version of this construction — for one fixed index `i`, extract
an infinite set of later indices all sharing one witness prime from
`rad(a_i)` — is **already certified as Lemma R** (`lemmas/lemma-R-eternal-
witness.md`, round 1, itself generalizing crux `aimo-0421`'s device). Lemma
R's certification note states explicitly: *"the lemma gives an eternal
witness existing for each fixed `i`, but does not by itself give a single
prime that is an eternal witness for every `i` simultaneously... strengthening
this uniformity is exactly the open backbone finiteness content."* Iterating
Lemma R along a diagonal sequence `t_1<t_2<\cdots` (candidate 2's
construction) produces exactly the color sequence `(c_i)` whose *finiteness of
range* is, verbatim, this same open uniformity question, just relocated onto
an extracted subsequence instead of asked directly of the whole sequence —
the `c_i`'s are free to include a fresh companion prime every time
(exactly the multi-companion-bundle behavior already observed and flagged as
the residual difficulty in `persistent-backbone-monovariant.md`'s
Multi-Companion Reduction Proposition). No new leverage.

**Verdict: dead end, and a clean explanation of *why* — this Ramsey
construction is definitionally Lemma R (round 1) run along an infinite
diagonal, not new content.** Worth recording so no future round re-derives
Lemma R under Ramsey-theoretic language and mistakes it for progress.

### Other ideas considered and ruled out quickly (per dispatch's suggested list)

- **Explicit-construction-of-`L`-bypassing-existence-of-`H`.** On inspection
  this does not actually sidestep the existential difficulty: round 4 already
  found three *independent* constructions of the canonical `H` (window,
  minimal-radical-antichain union, forced-primes union) that agree exactly —
  i.e., we already have an explicit *candidate* `H`/`L`. The entire remaining
  gap is proving that candidate (or any other) is *finite* — an explicit
  formula for `L` in terms of `a_1`'s factorization does not remove the need
  to prove finiteness of the underlying prime set unless the formula is an a
  priori fixed bound depending only on `\mathrm{rad}(a_1)` — and round 3–4
  already falsified the natural candidate "`K` a clean function of
  `\omega(a_1)` alone" (the 11-value table in `explicit-window-backbone-
  construction.md`). No new explicit-construction idea escaping this was
  found this session.
- **Dickson's Lemma / well-quasi-order tools.** Checked: Dickson's Lemma
  applies to `\mathbb{N}^k` for *fixed* `k`; our radicals are finite subsets
  of an *unbounded-dimension* prime space (companion primes are unboundedly
  large and unboundedly numerous across the family), so `(\mathcal{P}_{fin}
  (\text{primes}),\subseteq)` is well-founded (no infinite descending chain —
  already exploited via the certified No-Resurrection Lemma) but **not** a
  well-quasi-order (infinite antichains of finite sets exist trivially, e.g.
  all singletons) — this is precisely why `𝓥` being an infinite antichain is
  not excluded by general poset theory alone; Dickson's Lemma does not apply
  and Higman's Lemma (WQO on words over a WQO alphabet) needs the alphabet
  itself to be WQO, which the (unbounded) prime set is not known to supply
  anything beyond what's already used. No new leverage found.
- **Residue-structure / CRT-refined gap bound.** Checked whether a joint
  CRT analysis of forced residues mod several small primes at once could
  refine Lemma 1's crude gap bound (`d_n∈\{1,\dots,\mathrm{rad}(a_1)\}`) into
  something that pins down *which* companion prime gets recruited next. This
  is exactly round 6's Opening C (narrow-fresh-framing explorer): checked and
  refuted the natural "smallest available prime first" guess
  (`a_1=2747,S=\{41\}` recruits `13,17,19,23` before `5`). No CRT-based
  refinement was found this session that predicts recruitment order or
  bounds companion count; consistent with, not beyond, that finding.

### Crux corpus: additional targeted queries run this session (not previously logged)

Queried `past_crux_moves_database.json` directly (not just via
`crux_moves_documentation.md`'s subtopic index) for `hitting set`,
`hitting-set`, `transversal`, `sunflower`, `delta-system`/`delta system`,
`compactness`, `ultrafilter`, `könig`/`konig` across `technique`+`how_used`
text of all 2434 cruxes: **zero hits** for `sunflower`, `delta-system`,
`compactness`, `ultrafilter`, `könig` (confirms round 6's "confirmed absent"
finding extends to these specific set-theoretic terms, not just
Mertens/Borel–Cantelli). The `transversal` hits (`aimo-0596`, `aimo-0597`,
`aimo-0719`, `aimo-1001`, `aimo-1020`) are all geometric/combinatorial-design
"system of distinct representatives across a symmetric structure" uses with
no structural match to an infinite hitting-set-on-primes question. Also
queried `greedy`, `smallest integer`, `radical`, `squarefree`, `recruit`,
`gcd(a`, `shares a prime factor`: the two genuinely close hits were
`aimo-0447` (analyzed above, Candidate 1) and `aimo-0421` (already certified
into Lemma R, round 1 — see Candidate 2). No unchecked close analogue
remains that this session's keyword sweep surfaced.

### Recommendation for round 7's outliner

Given six rounds of exhaustive framing-search (three more genuinely fresh
threads killed this round, each with a concrete, non-hand-wavy reason —
quantitative failure for Candidate 1, definitional reduction to an
already-certified fact for Candidate 2), I do **not** think another top-level
reframing attempt is the highest-value use of round 7. The two live,
narrowing threads from round 6 (Single-Companion Finiteness Lemma's
`Λ_S`/`J_S` machinery, and the Coarsening Lemma's cross-bucket-domination
framing) both isolate the *same* precise residual content — a local
hitting/covering question on `\{\mathrm{rad}(a_j):j\in J_S\}` — more sharply
than anything a fresh top-level framing produced this session. If a genuinely
different tool is still wanted (per `current.md`'s own round-6
recommendation), the most promising unexplored-by-me angle is a **direct
combinatorial argument on the companion-COUNT itself** (round 6's Opening B,
empirically 2–4 per channel, never observed to grow with `a_1`'s size) rather
than another abstract existence framing — this session's negative results
reinforce, rather than contradict, that recommendation.
