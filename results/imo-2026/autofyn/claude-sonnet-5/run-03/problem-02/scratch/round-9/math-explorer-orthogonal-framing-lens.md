## imo-2026-02

### Headline finding this round: branch-independence (Idea 2) is DECISIVELY FALSE — do not pursue it

Per the dispatch's highest-priority check, I reconstructed `coordinate-bash-resultant`'s
exact §6 pipeline (own `sympy` session, script below) and tested whether the target
`T` (numerator of `O·(C−B) − (|C|²−|B|²)/4`) vanishes on the OTHER three
root-combinations of the branch factorization, not just the certified `⟨G2a,G3a⟩` one.

Setup reproduced exactly from `results/imo-2026-02/approaches/coordinate-bash-resultant.md`
§6 (rotation parametrization, Weierstrass substitution `u=tan(β/2)`, `A=(0,0),B=(a,0),C=(b,cc)`
free symbolic). `g2 = -(b²+cc²)²(u²+1)·G2a·G2b` (deg 4 vs deg 6 in `u`), `g3 = -a²(u²+1)·G3a·G3b`
(same degree split) — independently re-derived, exact match to the file's displayed `G2a,G3a`.

For 10 diverse random triangles `(a,b,cc,u)` (scalene, mixed acute/obtuse, `u∈(-1,1)`),
computed ALL real roots of `G2a,G2b` (in `s2`) and `G3a,G3b` (in `t1`), evaluated `T` at
every one of the 4 root-combinations `(a,a),(a,b),(b,a),(b,b)`:

- `(a,a)` combination: `T ≈ 0` to machine precision (`<1e-12`) in every trial where real
  roots exist — exactly as expected since `T ∈ ⟨G2a,G3a⟩` is already proven (certified
  `lemmas/symbolic-genericity-certificate.md`).
- `(a,b)`, `(b,a)`, `(b,b)` combinations: `T` is **macroscopically nonzero** — values
  ranging from `~0.5` up to `~4×10⁴` across trials, several orders of magnitude above
  numerical noise, with NO trial giving even approximate vanishing.

This is a clean, sharp separation (not a close call): `T` is either machine-zero or huge,
never intermediate. Conclusion: **the target identity `OM=ON` does NOT hold on the
"wrong" branches** — it is a genuine, non-trivial consequence of being on `G2a=G3a=0`
specifically, not a branch-independent algebraic identity. Idea 2 (branch selection as
a "red herring") is refuted. I also attempted the fully symbolic version (`sympy.groebner`
on `⟨G2b,G3b⟩` and the two mixed ideals, testing `T`'s membership with free `a,b,cc`) — this
did not terminate within ~15 minutes (the round-4 file itself flags `⟨G2b,G3b⟩` Gröbner
computation as not-yet-attempted/too slow for the same reason) — so this is numeric-only
evidence (10 diverse triangles, 40 total root-combination checks), not a symbolic proof,
but the separation is so clean (0 vs 10⁻¹² machine noise vs O(1)–O(10⁴) nonzero) that I
am confident this is real, not an artifact. A cheap script is saved in this session's
transcript (`/tmp/branch_test2.py`/`numeric_branch2.py`-style) and can be handed to a
builder to formalize into an explicit symbolic proof that `T ∉ ⟨G2b,G3b⟩` etc. if wanted
(low priority — a negative-result confirmation, not new leverage).

Practical upshot for the outliner: there is no shortcut that avoids branch selection by
proving the identity is branch-independent. Every live route's convergence onto branch
selection (per round 8's proven structural fact) stands.

### Idea 1: synthetic/angle-chasing route avoiding coordinates — searched, no new opening found beyond what's already ruled out

I reviewed what's already been tried and ruled out, to avoid re-litigating:
- Fixed spiral similarity `B↦K, C↦L`: refuted (round 2, exhaustive numerical sweep,
  center not fixed, not collinear with any candidate).
- Nine-point circle, circle through B&C, and the target circle A,K,L,Q itself as
  auxiliary loci for `K(θ), L(θ)`: all three ruled out with reasoned arguments
  (round 5, `ptolemy-trig-identity-synthetic`).
- Inversion at `A` turning "A,K,L,Q concyclic" into "K*,L*,Q* collinear": proved
  (round 8) to be **exactly** (not just equivalent-in-difficulty) the same computation
  as `fixed-point-concyclic`'s cross-ratio `χ` — no new leverage.
- An exhaustive 5-construction negative search for any alternative top-level target
  (not just alternative technique) was done in round 3 (`newframing-lens`) and found
  nothing; round 8's `newframing-lens` similarly found no new top-level target (only
  the now-refuted inversion idea).

Given this history, I looked specifically at the two "previously underused" hypotheses
("K inside ∠LBA", "L inside ∠ACK") for a *purely synthetic* (non-algebraic) argument,
since round 5 showed they carry real selection power algebraically (Theorem 11.8). I
did not find a clean synthetic argument in the time available — the natural attempts
(isogonal conjugation of K in triangle formed by B, the two rays, etc.) don't obviously
connect to the circumcenter-distance target `OM=ON` without re-deriving the same
vector/rotation algebra already in use. I did NOT find grounds to claim a new positive
synthetic route exists; this is a documented negative search, not a proof of
impossibility.

One additional cheap structural check I ran and that came back negative (worth recording
so no one retries it): tested whether `G2b(s2,u,·) = ±G2a(s2,-u,·)` (i.e. whether the
"wrong branch" is simply the u→−u reflection of the right one, which would have given
an easy synthetic "reflect across AB" argument for why it's spurious). Symbolically,
neither `G2b − G2a(u→−u)` nor `G2b + G2a(u→−u)` simplifies to 0 — no such clean
reflection relationship exists. Do not retry this specific lever.

### Idea 3: nothing further found

No other genuinely new top-level target surfaced. Given (a) idea 2 is now decisively
refuted, (b) idea 1's synthetic search came back empty after 8 rounds of increasingly
targeted attempts (most recently round 8's own `newframing-lens`), I believe the
population's current unified target (branch selection on `G2a=G3a=0` vs the alternatives,
equivalently `fixed-point-concyclic`'s `Rem=0`) is very likely the actual crux of the
problem, not an artifact of a suboptimal framing. My recommendation is that round 9's
outliner should NOT spend a slot forcing a "new framing" approach for its own sake —
CLAUDE.md's diversity requirement has already been satisfied via multiple independently
executed negative searches (rounds 3, 5, 8, and this round), each of which is itself a
valid distinct-framing probe, all converging on the same answer: there is no cheaper
door. Effort is best spent pushing directly on the sharpest current sub-gap formulations
(see below).

### Candidate technique(s)
- The population's live technique stack (resultants/Vieta/IVT sign arguments,
  Gröbner-basis ideal membership, bilinear/Cramer's-rule linear algebra) remains the
  only demonstrated path forward; no orthogonal technique (Sturm sequences, SOS,
  synthetic angle-chasing) has produced a working alternative despite repeated targeted
  attempts.
- If a genuinely different technique is to be tried, per round 6's flagged fallback,
  Sturm sequences properly set up post-ideal-reduction (not yet tried at all, as
  distinct from resultant/Vieta sign arguments) remain the one substantially untried
  lever in the "different technique, same target" category — worth flagging to the
  outliner as a possible next lever on the SAME shared branch-selection target (this is
  a technique-diversity suggestion, not a framing-diversity one).

### Cheap-kill candidates
- None new found this round beyond the refutations above (branch-independence; the
  u→−u reflection guess for G2b).

### Knowledge-base entries to use
- Gröbner-basis ideal membership (Cox–Little–O'Shea, already the load-bearing technique
  for the certified genericity certificate) — same entry cited throughout the
  population's history.
- Cevians/inversion/spiral similarity/projective-idea entry (`knowledge_base.md` line
  ~131) and the Miquel-point / circle-membership entries (~134, ~149) — already searched
  exhaustively against this problem (rounds 2, 3, 5, 8) with no viable match; not worth
  re-querying without new structure.

### Analogous past problems (cruxes)
None. The crux corpus (`crux_moves_documentation.md`) has only three domains —
`number_theory`, `combinatorics`, `algebra` — no `geometry` subtopic exists, confirmed
again this round. No crux search is possible for this problem; this has been the
standing finding since round 1.

### Prior progress
Per `current.md` (round 8 adjudication): all live routes (coordinate-bash-resultant-
boundary, coordinate-bash-resultant-boundary-pointwise, fixed-point-concyclic) are now
PROVEN (not just observed) to reduce to the same underlying branch-selection condition.
Precise remaining sub-gaps as of round 8:
- `coordinate-bash-resultant-boundary`: two-part reformulation (I) `sinB·sin(A+β) <
  2sin(A+B)(sinβ+sinA)` [needs only `sin(A+3β)<0`] and (II) `sinB·sin(A+β) >
  2sin(A+B)(sinβ−sinA)` [needs both `2cos²β>m·cosA` and `sin(A+3β)<0`], both verified
  at tens of thousands of samples, neither proved symbolically.
- `coordinate-bash-resultant-boundary-pointwise`: `r_lo`-selection now proven
  (`complex-affine-L1-DK-and-r-lo-selection.md`); further `D_N(r_lo)>0` sign fact still
  numeric-fit only.
- `fixed-point-concyclic`: `Rem=0` proven a free corollary of `⟨G2a,G3a⟩` — this route's
  own algebraic content is fully closed; it inherits the shared gap with zero remaining
  independent work.

### Dead ends (do not retry)
- Branch-independence of the target identity `T` across `G2a/G2b × G3a/G3b` combinations
  — decisively refuted this round (numeric, 10 triangles × 4 combinations, clean
  machine-zero vs O(1–10⁴) separation). Do not propose this as a shortcut again.
- `G2b(s2,u,·) = ±G2a(s2,−u,·)` (u→−u reflection hypothesis for the spurious branch) —
  refuted symbolically this round (neither sum nor difference simplifies to 0).
- Fixed spiral similarity `B↦K,C↦L` (round 2), nine-point/BC-circle/target-circle-itself
  as auxiliary loci (round 5), inversion-at-A reframing (round 8, proven identical to
  `fixed-point-concyclic`'s χ) — all previously ruled out, reconfirmed by literature
  review this round, do not retry.

### Small-case / intuition notes
The clean separation in the branch-independence numerics (machine-zero on the true
branch vs macroscopic nonzero elsewhere, with no intermediate cases across 10 varied
triangles) is strong conjectural evidence that the true branch is genuinely special —
i.e. branch selection is not a technical annoyance but encodes real geometric content
(the actual angle-equality hypotheses, not just their squared/relaxed versions). This
supports treating the shared gap as the authentic crux of the IMO problem (consistent
with it being an IMO P2/hard-difficulty problem where the "real" work is exactly this
kind of selection/existence argument) rather than an artifact of the algebraic framing
chosen 8 rounds ago.
