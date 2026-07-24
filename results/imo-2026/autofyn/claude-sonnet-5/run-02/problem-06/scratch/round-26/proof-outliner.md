## imo-2026-06

a1-5q-subfamily-theorem: revise
Target: For `a_1=5q`, every prime `q≥7` outside the finite exceptional set
`Bad(5)={7,13,19}`: literal `T=1,L=5` periodicity, `a_n=5q+5(n-1)` for
every `n≥1`.
Technique: Direct strong induction, instantiating the certified
`p`-uniform reduction (`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`,
from `a1-pq-subfamily-theorem`, round 25) at `p=5`, then closing the
resulting finite residual table with the certified sieve toolkit
(`lemmas/legendre-sieve-gap-bound.md`, `lemmas/primorial-floor-bound.md`) —
the exact template that closed `a1-3q`/`a1-3q^2`/`a1-3q^3`.
Skeleton:
  1. Base case `n=1`: `a_1=5q=5(q+1-1)`. — by definition.
  2. `a_n+5` legal (both terms divisible by 5 under IH `H(n)`), `a_n+1`
     illegal (consecutive-integer coprimality, `i=n` witness). — by
     `gcd(x,x+1)=1`.
  3. For `j∈{2,3,4}` (three bands, since `P(a_1)={5,q}` leaves three
     nonzero residues mod 5 to exclude): `5∤(a_n+j)`, so `a_n+j` illegal
     via `i=1` whenever `q∤(a_n+j)` (Case (a)). — direct divisibility,
     already proved `p`-uniformly in `a1-pq` Step (2.1).
  4. Case (b) (`q|(a_n+j)`, write `N=qK`): import verbatim the
     Generalized `K_0`-Boundedness Lemma — for each `(j,r)` pair
     (`j∈{2,3,4}`, `r=q mod 5∈{1,2,3,4}`, 12 cells total), the first
     Case-(b) occurrence has `K_0(j,r)=5+s_0(j,r)` where
     `s_0(j,r)∈{1,...,4}` is the unique solution of `s_0·r≡j (mod 5)` —
     a `q`-independent constant. Build the explicit 12-cell table
     (`s_0`, `K_0`, `n_0(j,r;q)=1+(s_0 q-j)/5`) for `p=5`.
  5. Step-4 sufficient-window closure (`a1-pq` Step (4)): for each of the
     12 cells, compute the explicit threshold
     `Q_1(5,j,r)=(5(K_0+1)+j)/s_0`; every prime `q≡r (mod 5)` with
     `q≥Q_1` is closed for free (window of `n_0-1` consecutive integers
     `≥K_0` guarantees a coprime witness).
  6. `k≥1` closure (`a1-pq` Step (5), same Legendre-Sieve/Primorial-Floor
     machinery as `a1-3q`): for each cell's residual `k` range below the
     generic-bound threshold, tabulate `K(k)=K_0(j,r)+5k`, compute
     `ω(K(k))`, and derive `q_thresh(5,j,r,k)` — closing all but finitely
     many `(j,r,k,q)` quadruples symbolically.
  7. Hand/computer-verify every below-threshold candidate quadruple by
     direct witness search (exactly as `q=7,q=11` were resolved for
     `p=3`). This step must reproduce, from the symbolic closure — not
     just cite the round-26 numeric scan — that `q∈{7,13,19}` are the
     ONLY quadruples with no witness (permanent divergence), and every
     other below-threshold candidate (e.g. `q=11`, `r=1`, matching the
     explorer's found near-miss) resolves via an explicit witness.
  8. Assembly: induction closes for every `q∉{7,13,19}`; the three
     exceptions are recorded as genuine, with their exact deviation index
     and mechanism (mirroring the certified `q=5` exclusion write-up for
     `a1-3q`).
Key lemmas (claim + mechanism):
  - Generalized `K_0`-Boundedness (imported, certified) — because
    `s_0(j,r)` solves a fixed linear congruence mod `p`, independent of
    `q`'s magnitude, so the window's growth is purely a function of
    `(j,r)`, not `q`.
  - `Bad(5)={7,13,19}` exactly — because in each case the first Case-(b)
    window has `K_0=6` (the minimal possible value, `s_0=1`, occurring
    precisely when `j≡r (mod 5)`) and the window length `n_0-1` is far
    too short (`1,2,3` respectively) to guarantee a coprime witness by
    the generic pigeonhole bound, AND (this is the part not yet proved
    symbolically, only checked numerically to `q<2000`) direct
    enumeration of the actual window at each of these three q confirms
    literally no witness exists — must be proved, not just numerically
    observed, exactly as `q=5` was proved (not just observed) exceptional
    for `p=3`.
Open gaps: Step 7's symbolic/analytic completion of the residual-table
closure for `p=5` (the numeric scan to `q<2000` is strong evidence, not
proof, that no exception lurks beyond the scanned range — must derive
the explicit `q_thresh` values and confirm every prime above them is
provably closed, mirroring exactly how `a1-3q` needed the sieve toolkit
to rule out exceptions beyond its own numeric range).
Cases to cover: `j∈{2,3,4}` × `r∈{1,2,3,4}` (12 cells) × (`k=0` vs `k≥1`
residual band per cell) — all must be covered; do not stop at a subset.
Watch out for: the near-miss `q=11` (`j=2,r=1`, crude bound fails but a
genuine witness exists) — a template for how "below threshold" does NOT
automatically mean "exception"; every below-threshold candidate needs an
actual witness search, not a default classification as bad.

a1-7q-subfamily-theorem: new
Target: For `a_1=7q`, every prime `q≥11` outside the finite exceptional
set `Bad(7)={11,13}`: literal `T=1,L=7` periodicity, `a_n=7q+7(n-1)` for
every `n≥1`.
Technique: Identical template to `a1-5q-subfamily-theorem` above,
instantiating the same certified `p`-uniform machinery at `p=7` (5 bands
`j∈{2,...,6}`, 6 residues `r∈{1,...,6}`, 30 cells — larger table, same
method, no new theory).
Skeleton:
  1-8. Same as `a1-5q-subfamily-theorem`'s skeleton with `p=7`, `j` ranging
     over `{2,...,6}`, `r` over `{1,...,6}`.
Key lemmas (claim + mechanism):
  - Same imported Generalized `K_0`-Boundedness / gcd-difference Witness
    Lemma, `p=7` instantiation.
  - `Bad(7)={11,13}` exactly — same minimal-window mechanism as `a1-5q`
    (this round's explorer confirmed the qualitative pattern by
    simulation but did NOT band-trace `p=7` symbolically — this is new
    work, not a copy of the `p=5` derivation).
Open gaps: the full 30-cell table has not been symbolically built or
band-traced (explorer only ran the numeric simulation, not the `(j,r)`
decomposition, for `p=7`); building it and closing the residual bands is
the entire content of this approach. Given the larger table, treat this
as a secondary/lower-priority build relative to `a1-5q` — if capacity is
tight, `a1-5q` should get priority since its cells are already fully
band-traced by this round's explorer.
Cases to cover: `j∈{2,...,6}` × `r∈{1,...,6}` (30 cells) × (`k=0` vs
`k≥1`) — larger casework than `a1-5q`, same shape.
Watch out for: do not assume the `p=5` pattern ("exceptions occur exactly
at `j≡r`, i.e. `s_0=1`") transfers automatically to `p=7` without
checking every cell — this is only a 2-data-point conjecture per the
explorer, not yet verified as a shortcut.

a1-pq-subfamily-theorem: advance
Target: unchanged (the `p`-uniform reduction theorem for the whole
`a_1=pq` family, any odd prime `p`) — this round's advance targets the
open gap #2 in the file's own "Open gaps" section: a general structural
result about `Bad(p)`, not another per-`p` numeric table (that work is
now split off to `a1-5q`/`a1-7q` above).
Technique: Use the pattern surfaced by this round's explorer — every
confirmed genuine exception so far (`p=3:q=5`; `p=5:q∈{7,13,19}`) occurs
exactly at a cell with `s_0(j,r)=1` (the minimal possible value, giving
the shortest possible window `K_0=p+1`) — and attempt to either PROVE this
as a general theorem (a genuine exception can only occur at an `s_0=1`
cell) or find a counterexample refuting it.
Skeleton:
  1. Formalize the claim: "if `s_0(j,r)≥2`, then for every prime
     `q≡r (mod p)` in band `j`, a witness always exists at `k=0`" (no
     genuine exception possible outside the minimal-window cells).
  2. Attempt a direct proof: for `s_0≥2`, `K_0=p+s_0≥p+2`, and the window
     length at `n_0-1` — express `n_0-1` in terms of `s_0,p,q` via the
     explicit formula from `a1-pq` Step (3) and compare growth rates; look
     for a clean inequality (e.g. `n_0-1 ≥ K_0` once `s_0≥2` for `q` above
     a SMALL, `p`-independent-order threshold) that would make Step 4 of
     `a1-pq` apply automatically without any per-cell threshold
     computation.
  3. If the direct proof fails, test the conjecture computationally
     against `p=5,7` (using the two new tables being built in the sibling
     approaches this round) as the first real stress test beyond the
     2-data-point base.
  4. If proved: this collapses the "per-`p` at-risk candidate set" from
     `O(p^2)` cells to only the `O(p)` cells with `s_0=1` (one `s_0=1`
     residue `r` per band `j`, `p-2` bands), a genuine structural
     reduction reusable for every future `p`.
Key lemmas (claim + mechanism):
  - Minimal-Window Necessity Conjecture (open, to be attacked): a genuine
    `Bad(p)` exception requires `s_0(j,r)=1` — because non-minimal `K_0`
    gives strictly more window growth per unit `q`-increment relative to
    the fixed `K_0`, so larger `s_0` bands "outrun" their own threshold
    faster; this is a plausibility argument, not yet a proof — the
    builder must either supply the missing inequality or refute the
    conjecture with an explicit `s_0≥2` counterexample.
Open gaps: the conjecture itself is unproved; this is genuinely open
research within the workspace, not a routine mechanical task like the
`a1-5q`/`a1-7q` builds.
Cases to cover: none fixed in advance — depends on what the proof
attempt or counterexample search finds.
Watch out for: do not let this advance consume the round's only build
slot if the mechanical `a1-5q` closure (a near-certain APPROVE) is left
unbuilt — this is a stretch target, lower priority than the two concrete
per-`p` closures above.

covering-system-construction: advance
Target: unchanged (H1/FAH via the rogue-pair/witness-alphabet framing) —
this round's advance targets a concrete, bounded sub-question left open
by the certified Reduced-Alphabet Corollary (round 12): for the standing
test seed `a_1=4807` (rogue pair `A'={3,5,19}`,`B'={2,11}`,
`n_A=6,n_B=7`), the corollary reduces the open FAH-exception alphabet to
the single divisor class `d=13` (`D_bad(17)={13}`). Attempt to either
prove `g_n=13·(\text{unit part})` never occurs for the relevant `n`
(ruling out this last class unconditionally) or exhibit it occurring
(showing FAH fails, or at least this rogue pair's naive resolution does).
Technique: Direct analysis of what `g_n=d` (`d\in D_bad(q*)`) would
require — trace back through the Confined-GCD Lemma's proof to see
exactly which arithmetic conditions on `a_n` a witness with cofactor
class `d=13` would need to satisfy, and check whether those conditions
are compatible with the sequence's own generation rule (legality/
minimality), the same style of direct compatibility check used
successfully in several already-certified vacuity results
(Escape-Cost Vacuity, Same-Type Triangle Vacuity).
Skeleton:
  1. Restate precisely what `d=13` as a value of the relevant gcd witness
     would mean for the underlying sequence data at the specific
     indices/classes involved. — by unpacking the Confined-GCD Lemma's
     definitions.
  2. Check compatibility against the problem's minimality/legality rule
     (does forcing this class require an illegal move, or a move already
     ruled out by an existing certified lemma, e.g. the Bounded Gap
     Lemma or Free Facts)? — direct case check.
  3. If incompatible: certify a new, narrow Vacuity result for this
     specific residual class (a genuine, if small, further narrowing of
     FAH's open content). If compatible/inconclusive: report honestly as
     a further-open residual, no overclaim.
Key lemmas (claim + mechanism): none new claimed in advance — this is an
exploratory compatibility check on the one already-isolated residual
class, not a new machinery lemma.
Open gaps: the entire compatibility question is open; this may well
dead-end (matching the file's own "34+ prior confirmed-dead mechanism"
pattern) — if so, report as RETHINK-worthy honestly rather than force a
positive spin, per this round's H1-explorer finding that no new H1
corridor was found.
Cases to cover: the single residual class `d=13` for the `a_1=4807` seed
only (do not attempt the general `|F''|≥3` case this round — out of
scope per the file's own honest-scope statement).
Watch out for: this is explicitly NOT a new H1 mechanism — it is a
bounded, concrete follow-up on already-certified bookkeeping. If the
builder finds no traction within the compatibility check, do not spiral
into open-ended FAH speculation; report the negative finding plainly and
let the approach stay `partial`/`unsolved` as appropriate.

Note (not a build entry): `a1-3qk-subfamily-theorem`'s `m=4` extension is
explicitly HELD OUT this round. This round's `m4`-lens explorer found (1)
a genuine counterexample at `q=17,k=0` that provably does NOT resettle to
constant gap 3 (breaking the literal claim as stated for `m=4`), and (2)
the naive threshold-scaling from the `m=3` closure blows up to an
infeasible `~2×10^11` verification range (vs `m=3`'s tractable 737,282) —
two independent, non-routine obstacles, not a "bigger table, same
difficulty" repeat. Forcing a build here risks a wasted slot on a
target the explorer explicitly flagged as not-ready. The approach stays
`partial` at its already-certified `m=1,2,3` floor; revisit `m=4` only
once either (a) a genuinely sharper sieve inequality is found (bringing
the threshold down from `~2×10^11` to something checkable), or (b) a
non-exhaustive uniform-witness argument replaces the sieve-existence
approach for the large-`q` regime. Do not re-propose the naive
"exclude q=17 and hope the rest is routine" framing without addressing
obstacle (2) explicitly.
