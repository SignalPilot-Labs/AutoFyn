## imo-2026-06 (lens E5 — bounding |G| for ⊆-minimal minimal supports)

### Setup recap (all certified, not re-derived here)
Crux (Finite Alphabet) ⟺ E4: `sup_{G∈𝓐_∞}|G| < ∞` (size-bound-reduction.md). Available
certified facts to build E5 from: Anchor (every `G∈𝓐_∞` meets fixed finite `P=F(a₁)`,
`|P|=ω(a₁)`), Gap bound (`a_{n+1}-a_n≤M=rad(a₁)`, hence `a_n=Θ(n)`), Distance–prime
(`q|(a_i-a_j)⟹q≤|a_i-a_j|`), E1 (terms = `A∩[a₁,∞)` exactly), E2(⇒)/(⇐) (self-blocking:
members = finite minimal transversals of `𝓐_∞`), E3 (private witness: `∀p∈G ∃G_p∈𝓐_∞`,
`G∩G_p={p}`, giving two terms `t,t'` with `gcd(t,t')=p^m`, `p≤|t-t'|`).

### Distinct openings for E5

**Opening 1 — "interval-covering / grid" bound, borrowed from aimo-0447 (most promising lead).**
The crux corpus problem aimo-0447 (ISL/IMO-flavor "gcd(a+i,b+j)>1 for all i,j in a grid ⟹
min{a,b}>(cn)^{n/2}") uses exactly this pattern: place a prime in each grid cell witnessing the
pairwise gcd condition, note a prime `p` exceeding the interval length divides **at most one**
value of a length-`p` interval (this is literally certified L3/Distance-prime here), then argue
that if *many* cells in one line are covered by primes exceeding a threshold, those primes must
be **pairwise distinct**, forcing the line's value to be at least their product — a lower bound
that grows too fast to be consistent with the interval length. Applied here: a minimal support
`G` of size `r` is realized by a term `t=a_i` with `F(t)⊇G` (in fact `=G` for the *minimal*
realizing term, by E2(⇐)-style reasoning), so `t ≥ ∏_{p∈G} p`, a product of `r` distinct primes —
already super-exponential in `r` if the primes are unrestricted. The open step is to find the
**matching upper bound on `t`** (a "line/window length" analogous to aimo-0447's `N`) coming from
the *index* of `t` and the gap bound (`a_n=Θ(n)`, gaps `≤M`) that contradicts a large product —
i.e. show that a term realizing a size-`r` minimal support cannot appear "too late" (bound its
index in terms of `a₁,M` alone, not in terms of `r`), so that `t`'s value is capped independent
of `r`, forcing `r` bounded. This is structurally the same "product-vs-window" collision as the
stalled §10 ERW target in `redundant-constraint-antichain.md`, but re-aimed at *cardinality*
rather than *formation time* — worth re-attempting since E4 changes the target quantity (a
combinatorial count, not an arithmetic magnitude) and may admit a cleaner window argument than ERW
did. **Not solved; flagged as the strongest candidate technique, borrowed and adapted from
aimo-0447's crux move**, not directly transplantable (the setups differ: aimo-0447 has a genuine
2D grid of independent gcd constraints, our problem has a 1D sequence with a fixed *anchor* `P`
and self-blocking family — the adaptation to a matching argument is open work, not done here).

**Opening 2 — chain-descent run "locally" per support (dual of E4's proof).** E4's own proof
(chain-descent B_1⊊B_2⊊…) shows: *if `𝓐_∞` is infinite, minimal supports of unbounded size exist*
— it is a global argument bounding the whole family's max size by contradiction, not a
per-support bound. A genuinely different opening is to run an **analogous local chain construction
anchored at a single fixed `G`**: for `G∈𝓐_∞` with `|G|=r`, build a chain of "necessity witnesses"
— for each `p∈G`, E3 gives `G_p` with `G∩G_p={p}`; iterate by looking at `G_p`'s own witnesses,
trying to force a chain of length `r` inside the *fixed finite* set `P` (Anchor) via pigeonhole,
which would give `r≤|P|=ω(a₁)` directly. **This is exactly the numeric pattern that FAILS**: my
own quick resimulation (see Small-case notes below) found `a₁=9375` (`ω(a₁)=2`) has `maxMemberSize
=4 > ω(a₁)`, so a naive `r ≤ ω(a₁)` bound is false. Do not pursue "`|G|≤|P|`" as stated; if
revived, the bound must be `ω(a₁)+f(M)` or similar, not `ω(a₁)` alone. Flag as a **partial dead
end** — the naive chain-through-P idea is refuted numerically, but a *weaker* additive bound
(`|G| ≤ ω(a₁) + c` for some small absolute or `a₁`-dependent `c`) is not excluded and is untested
territory.

**Opening 3 — density/counting argument via gap bound (a support of size r forces r "private
recruitment events" that a bounded-density process cannot sustain arbitrarily often).** Each
`p∈G` (|G|=r) has a private witness pair `(t,t')` with `gcd(t,t')=p^m` and no other shared prime —
so of the (at most) `M`-spaced sequence of terms, `r` distinct pairs must each be "singly linked"
by a distinct large prime. Combine with the density monovariant `δ_n≥1/M` (certified in
`monovariants-and-obstruction.md`) and the fact that a term divisible by a *new* large prime `q`
occurs relatively rarely (density `~1/q` in `A`, since `A` requires meeting every prior support,
and adding a prime-`q` requirement to be a witness costs a `1/q` density factor per E3-style
argument). A size-`r` support "spends" `r` such rare recruitment events *simultaneously satisfied
by one integer* `t=∏G`-ish — the same tension the monovariant obstruction family
(`monovariants-and-obstruction.md`) shows CANNOT be resolved by density/max-gap statistics of
`A_n` alone. **Likely a dead end as stated** for the same reason the certified obstruction rules
out `A_n`-only arguments: it is exactly the density argument that the obstruction family defeats
(density converges to `1/p*` without ever freezing while the family's minimal supports stay
2-element forever — so density-type counting cannot, by itself, detect a *size* bound either,
mirroring why it cannot detect a *finiteness* bound). Only useful if sharpened using E1
realizability (which the obstruction family lacks, being non-realizable/non-self-blocking) to
exclude a genuine size blow-up — this needs the SAME arithmetic realizability ingredient as
Opening 1, so it likely collapses into the same open gap rather than being a truly independent
route.

**Opening 4 — "at most one large-prime-per-window" pigeonhole, direct from L3 + gap bound (cheap
partial result, not full E5).** Since gap `≤M`, any interval of length `M` contains at most one
term with an EXACT value; but more useful: by Distance–prime (L3), if a prime `q>|G|·M` (say)
divides two DIFFERENT terms realizing `G` and its size-`r` witness set, all `r` witness pairs
`(t,G),(t,G_p)` are constrained. A **cheap partial structural fact** worth checking first (see
cheap-kill candidates below): can two DISTINCT large primes `q,q'` (both `>M`, both in the *same*
minimal support `G`) be shown never to co-occur, by an aimo-0447-style "distinct primes force
distance apart" argument applied to consecutive terms rather than the witness pair? I.e., is it
possible to show every minimal support has **at most one** prime exceeding `M` (so
`|G| ≤ |P| + 1` trivially, since the rest of `G` lies in the fixed finite set of primes `≤M`,
which is itself of size `π(M)`, not just `|P|`)? Numerically FALSIFIED already in the existing
data: `a₁=385` has `19∈Π` (one large prime, consistent), but `a₁=9375` maxsize=4 while
`M=rad(9375)=15`, `π(15)=6` primes `≤15` (2,3,5,7,11,13) — need to check directly how many of the
4 primes in the size-4 support exceed `M=15` (the file records `67∈Π` for 9375, a large prime, but
doesn't give the full support tuple). **Action for the outliner/builder: recompute the actual
size-4 minimal support(s) for `a₁=9375` to see if more than one prime `>M` co-occurs in a single
support — this decides whether Opening 4's "≤1 large prime per support" cheap kill is alive or
dead** (I did not have time to extract this from the existing numerics; it is a fast, concrete,
falsifiable check for the next round).

### Cheap-kill candidates
- **"At most one prime `>M` per minimal support"** (Opening 4) — cheap, concrete, falsifiable by
  directly listing the 4-element minimal support(s) found for `a₁=9375` (or `a₁=1155`, which also
  has `maxMemberSize=4`, `M=1155` — note for `1155` since `M=a₁` itself, "large" is vacuous, a
  worse test case; use `9375` or `375` instead, both have `M=15≪a₁`). **Do this check first** —
  it is the single fastest way to kill or validate the most promising cheap structural handle.
- **"`|G| ≤ ω(a₁)`"** — FALSIFIED (see Small-case notes: `9375` gives `4 > ω(9375)=2`). Do not
  reintroduce.
- Parity / simple pigeonhole on `P` alone (Opening 2's naive form) — refuted, see above.

### Candidate technique(s)
- **Grid/interval-covering + "large prime hits an interval at most once" (aimo-0447 crux move)** —
  the single most promising transplant; needs a bespoke "window vs. index" argument specific to
  this problem's 1D greedy structure (not a direct copy).
- Pigeonhole chain-descent (already used for E4; a *local* per-support version is the natural next
  attempt, Opening 2, but its naive form is dead).
- Density/monovariant counting (Opening 3) — likely blocked by the same certified obstruction that
  kills pure `A_n`-statistics for the Crux itself.

### Knowledge-base entries to use
- **Pigeonhole / extremal principle** (`knowledge_base.md` Combinatorics) — already the engine of
  E4's chain-descent; any E5 attempt via Opening 1/2 will likely reuse it.
- **Divisor analysis / bounding a finite search by size** (Number Theory section) — relevant to
  turning "product of r distinct primes ≤ some bound" into `r` bounded.
- No entry in `knowledge_base.md` currently covers "grid covering by primes" or "size of a minimal
  transversal of a self-blocking clutter" directly — this is exactly the gap the crux corpus fills
  (see below); consider proposing a KB entry for the aimo-0447-style technique if E5 closes via it.

### Analogous past problems (cruxes)
- **aimo-0447** (number_theory, `size-bounding-and-descent`) — **best match**. "gcd(a+i,b+j)>1 for
  all i,j in an (n+1)×(n+1) grid ⟹ min{a,b}>(cn)^{n/2}." Crux moves: (1) encode a pairwise-gcd
  hypothesis as a prime covering a grid; (2) a prime `p` divides `≤⌈N/p⌉` values of a length-`N`
  interval, so it covers `≤⌈N/p⌉²` cells — small primes can't cover the whole grid (`Σ1/p²` bound);
  (3) **the crux payoff**: on a deficient line, the surviving primes exceed the interval length, so
  by "a prime `>N` divides at most one value of the interval" they are **pairwise distinct**,
  forcing the line's value to be `≥` their product, i.e. exponentially large in the count of large
  primes. This is precisely the missing ingredient for Opening 1: our `t≥∏G` bound is the same
  move; what's missing is aimo-0447's matching *upper* bound on `t`/the "line length" (there, `N`;
  here, presumably `a₁,M`, or the term's index) to close the pincer. Genuinely analogous, not
  forced — same "gcd>1 pairwise / cover with primes / large primes are automatically distinct in a
  bounded window" shape as our problem.
- **aimo-0030** (number_theory, `divisibility-and-gcd`) — "good/bad number game," proves a
  periodicity-by-prime-signature-mod-`P` result (`P`=product of small primes `≤k`) essentially
  identical in *flavor* to our ALREADY-CERTIFIED endgame (§4–5 of `redundant-constraint-antichain`:
  `A` periodic mod `L₀`, from the *finite alphabet* input) — but its crux moves (Claims 1–3, minimal
  counterexample on the pair `(n,n')`) target proving *periodicity itself* from finiteness of small
  primes, which we already have unconditionally (no-transient-fixed-successor.md); it does **not**
  address bounding the number of large primes that can co-occur, so it is not directly useful for
  E5, only confirms the endgame shape is a known pattern. Not a crux-move source for E5 specifically.
- **aimo-0099** ("bound one closure-linked set's size by injecting into the other, fixing the
  largest element and dividing by each smaller element") — a genuine "bound set cardinality by
  injection" crux move, but its mechanism (divide the max by each other element to get `|B|-1`
  distinct images in `A`, then use a separate bound on `|A|`) does not obviously transplant: there
  is no natural "other side" of comparable/dual size in our clutter to inject into. Listed as a
  *weak* analog — worth 5 minutes of thought (does `𝓐_∞` have any natural dual/complementary
  bounded family a size-`r` support could inject into, e.g. its `r` private witnesses `G_p`? Those
  ARE `r` distinct minimal supports, each ⊆ (in some rough sense) sharing exactly one prime with
  `G`; if a companion bound on the number of DISTINCT minimal supports sharing a *given* prime `p*`
  with `G` existed, that would bound `r` — but no such companion bound is currently available,
  same open-gap territory as Opening 2/3), but not pursued further here.

### Prior progress
Everything up through E4 (Size-Bound Reduction) is certified; the sole gap is E5:
`sup_{G∈𝓐_∞}|G|<∞`. No approach in the population has yet produced a proof attempt of E5 itself
(the §10 ERW target in `redundant-constraint-antichain.md` targets a *different* quantity —
formation-time window `K` — and stalled; §11.4 explicitly states E5 as open with no attempt beyond
noting "the wall.").

### Dead ends (do not retry)
- **`|G| ≤ ω(a₁)` (Opening 2, naive form).** Falsified: `a₁=9375` has `ω(a₁)=2` but a minimal
  support of size 4 (file `size-bound-reduction.md` §11.3 table; independently reproduced for
  `a₁=15015`, `ω=5`, `maxsize=5` — consistent there but NOT a proof of `|G|=ω(a₁)` in general since
  9375 breaks even the weaker `≤ω(a₁)+1`).
- **Pure `A_n`-statistic / density-only arguments (Opening 3 as stated).** The certified obstruction
  family in `monovariants-and-obstruction.md` shows density and max-gap freeze/converge without
  detecting unbounded structure; the same mechanism likely defeats a naive density-counting
  argument for bounding `|G|`, not just for the Crux itself. Any revival must route through E1
  realizability (arithmetic, not just `A_n`-statistics), same caveat already on record.
- **ERW window target (§10 of `redundant-constraint-antichain.md`).** Already flagged stalled by
  the population; retargeting it at cardinality (my Opening 1) is a genuinely different quantity,
  not a retry, but the underlying "per-window independence" difficulty it hit is very likely the
  same wall Opening 1 will hit — be aware, not naive.

### Small-case / intuition notes (all CONJECTURE, not proof)
- Reproduced independently (own simulation, `a₁=15015=3·5·7·11·13`, `ω(a₁)=5`): stabilized minimal
  supports at `N=1500` terms give `max|G| = 5 = ω(a₁)` exactly, `6` minimal supports total. This is
  consistent with, but does not by itself establish, any clean formula (`9375` already breaks
  `|G|≤ω(a₁)`).
- From the certified table (`size-bound-reduction.md` §11.3): `max|G|≤4` across all 10 tested
  seeds, and `max|G|` is small (`1`–`4`) even when `|Π|` (total distinct primes ever appearing) is
  as large as `6` — i.e. **many small minimal supports, not one giant one**, is the observed
  regime. This is the qualitative shape any E5 proof should expect to produce: not a single
  bloated support, but boundedly-many small ones, reinforcing that a *local* per-support argument
  (Opening 1/2) is the right shape rather than a global density argument (Opening 3).
- No case tested so far has `|G| ≥ 5` for `a₁ < 20000` other than the `ω(a₁)=5` seed `15015` where
  `|G|=5=ω(a₁)`; whether `|G|` can exceed `ω(a₁)` by more than `+2` for larger, more prime-rich
  `a₁` is untested and would be a cheap next numerical experiment (e.g. `a₁ = 3·5·7·11·13·17` or
  `a₁` a large prime power with extra small-prime perturbation) before investing in Opening 1's
  full argument.
