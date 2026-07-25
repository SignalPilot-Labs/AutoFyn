## imo-2026-02

### Correction to the dispatch framing (checked, not speculated)
The dispatch describes "fixed-point-concyclic's Rem=0 condition in 3 real
variables (h1,h2,h3)" as the cleanest current open surface. Per
`current.md` round 8 and `lemmas/rem-zero-free-corollary-of-genericity-branch.md`
(independently re-derived twice, builder + reviewer), **Rem=0 is no longer
an open condition** — it is a *proven free polynomial corollary* of the
already-certified branch `⟨G2a,G3a⟩` (Gröbner remainder exactly 0, both
directions verified). So there is no longer a live "Rem=0 in (h1,h2,h3)"
surface to import a technique into — that surface has literally collapsed
into the *same* `(t1,s2,u,a,b,cc)` polynomial ring that
`coordinate-bash-resultant-boundary` already works in (Theorem 8, §7.3-7.4
of `fixed-point-concyclic.md`). The genuinely single remaining shared gap,
concretely, is branch selection: excluding `G2b=G3b=0` in favor of
`G2a=G3a=0`, currently formalized by `coordinate-bash-resultant-boundary`'s
own two-part target (I)/(II) in `A,B,β` (§15 of that file) — this is
literally the target the "import Q(m)" question should be asked about,
since it's already the same computation as Rem=0's substance.

### What I actually tested: does the AB=1/AC=m Q(m) machinery, pushed one
step further (substituting the true Law-of-Sines value `m=sinB/sin(A+B)`
directly into `Q(m)`, i.e. the same substitution `coordinate-bash-resultant-
boundary` round 8 already used to fix its `M0` counterexample), reveal new
structure for the still-open (I)/(II) inequalities?

**Yes — a genuinely new, previously-undocumented structural fact, verified
symbolically (sympy, exact, zero-residual identities, not numerics):**

Write (I) as `f(β)>0` and (II) as `g(β)>0` where (both derived by exact
`sympy.expand(..., trig=True)` + coefficient collection on `sinβ, cosβ`,
residual 0 in every step):
```
f(β) = P sinβ + Q cosβ + K   (this is (I): 2sin(A+B)(sinβ+sinA) − sinB·sin(A+β) > 0)
g(β) = −P sinβ − Q cosβ + K  (this is (II): sinB·sin(A+β) − 2sin(A+B)(sinβ−sinA) > 0)
```
with
```
P = sin(A−B)/2 + 3sin(A+B)/2
Q = −sinA·sinB
K = 2sinA·sin(A+B)
```
i.e. **g = 2K − f exactly** — a clean algebraic identity I had not seen
recorded anywhere in the population's files. Consequence: **(I) ∧ (II) is
exactly equivalent to the single double-sided bound `0 < f(β) < 2K`**, i.e.
writing `f(β) = K + [P sinβ + Q cosβ]` (a pure sinusoid of amplitude
`R=√(P²+Q²)` centered at `K`), (I)∧(II) says the oscillating part
`P sinβ+Q cosβ` stays strictly inside `(−K,K)` for all `β∈(0,γ)`.

Also computed exactly: `R² − K² = sin²(2A+B) ≥ 0` (a clean closed form,
zero-residual `sympy.factor`/`simplify`), so `R ≥ |K|` always — the
sinusoid's amplitude is never smaller than the offset, meaning `f` genuinely
*can* leave `(0,2K)` somewhere over a full period; the claim is intrinsically
domain-restricted (matches round 6/8's observation that a global positivity
certificate is impossible here — this is the analogous fact for this target).

Numerically confirmed `f(0) = sinA·(2sin(A+B) − sinB)` can be ≤0 in ~25% of
random `(A,B)` (200k samples) — but this is *expected and harmless*: (I)'s
hypothesis `sin(A+3β)<0` (i.e. `B2>0`) generically fails near `β=0`, so `β=0`
is outside the actual claim's domain; f(0)'s sign is not required.
`f(β=B) = (2sinA+sinB)·sin(A+B) > 0` unconditionally (all three factors
positive for `A,B∈(0,π), A+B<π`) — a clean, provable boundary value at one
natural reference point, though `β=B` is not generally the domain's actual
right endpoint `γ=min(B,C)`.

### Does this close (I)/(II)? No — but it changes the target's shape
This is a genuine (if partial) transfer: it converts the two-inequality
target into **one** clean "amplitude vs. offset, restricted to a sub-arc"
claim (`|P sinβ+Q cosβ| < K` on `β∈(0,γ)`), with `R,K` both in exact closed
form and `R²−K²` factored. That is a strictly smaller-looking target than
(I),(II) as separately-stated trig inequalities, and is the natural next
lever: the standard technique for `R sin(β+φ) < K$ type claims restricted to
a sub-interval is to check the two endpoints (`β→0⁺` restricted to where the
hypothesis holds, and `β→γ⁻`) plus monotonicity/single-critical-point
analysis (`f'(β)=0` has at most one solution per period since `f` is a
single-frequency sinusoid) — the same proof template that already closed
`sin(A+3β)<0`-type crossing lemmas (`branch-crossing-locus-equals-angle-B/C`,
`disc(Q)>0`) elsewhere in the population, just applied to an *offset*
sinusoid instead of a homogeneous one. This was NOT completed this round
(scouting only) — the endpoint value at the true `γ=min(B,C)` (not the
simpler `β=B` reference point I checked) still needs to be evaluated and
signed, and the monotonicity/critical-point case-split still needs to be
worked out.

### Distinct openings
1. **(New, this round) The offset-sinusoid reformulation**: (I)∧(II) ⟺
   `0<f(β)<2K` with `f=K+P sinβ+Q cosβ`, `P,Q,K,R²−K²` all in exact closed
   form above — a genuinely smaller, unified target replacing two separate
   inequalities, ready for an endpoint+monotonicity closure attempt next
   round (not yet attempted).
2. Original (I)/(II) split (per `coordinate-bash-resultant-boundary` §15) —
   still valid, now known to be literally `2K−f` and `f` of the same
   sinusoid, so any proof of the unified target above proves both at once.
3. The shared-branch-selection framing itself (fixed-point-concyclic's
   Rem=0 = G2b-exclusion, proven identical by Theorem 8) means ANY progress
   on (I)/(II) or on `coordinate-bash-resultant-boundary-pointwise`'s
   parallel G2a-same-root gap closes the WHOLE problem via every live route
   simultaneously — worth stating explicitly to the outliner so builders
   don't waste effort re-deriving Rem in isolation.

### Candidate technique(s)
Endpoint-evaluation + single-critical-point (derivative sign) analysis of
the offset sinusoid `f(β)=K+P sinβ+Q cosβ` on `β∈(0,γ)`, `γ=min(∠B,∠C)`,
combined with the (still needed) precise identification of where the
hypothesis `sin(A+3β)<0` (`B2>0`) actually starts holding within that
interval (needed for (I)'s effective sub-domain) and where `Y>0` holds
(needed for (II)'s effective sub-domain, jointly with `B2>0`) — i.e. reuse
`branch-crossing-locus-equals-angle-B/C`-style crossing-point identification
but now as the actual left endpoint of the effective sub-interval, not just
a harmless-crossing fact.

### Cheap-kill candidates
None new found. The `f(0)` sign varying (~25% of samples) is NOT a
counterexample (domain excludes small β generically) but is a trap: do not
mistake `f(0)≤0` for a violation without first checking the hypothesis
`sin(A+3β)<0` holds at that β.

### Knowledge-base entries to use
- Trig product-to-sum / angle-addition identities (used throughout; already
  cited by the population).
- Law of Sines (already cited, `coordinate-bash-resultant-boundary` §14).
- Single-frequency sinusoid sign/threshold analysis — same family of
  elementary calculus already used for the certified crossing lemmas
  (`branch-crossing-locus-equals-angle-B.md`, `-C.md`,
  `q-quadratic-discriminant-and-roots.md`), extended here to the offset
  (non-homogeneous) case.

### Analogous past problems (cruxes)
Per `crux_moves_documentation.md` (re-confirmed this round, consistent with
round-1's finding recorded in `/tmp/memory/math-explorer.md`): the crux
corpus has no geometry-domain entries usable for this problem's synthetic
content. For the pure trig-inequality sub-target (I)/(II) specifically, no
targeted corpus search was performed this round (out of scope for the
lens); a future round could search `subtopic` bins for "trigonometric
inequality" / "sinusoid bound" if geometry entries remain absent, but this
was not attempted here — flagged as untried, not ruled out.

### Prior progress
See `current.md` round 8 summary: genericity certificate closed (all
triangles); Rem=0 proved a free corollary of `⟨G2a,G3a⟩` (closes
fixed-point-concyclic's own content entirely); magnitude bound closed;
G2a-selection (Theorem 11.8) closed; disc(Q)=16sin²A closed unconditionally
with exact roots `r1,r2`. Sole remaining shared gap: (I)∧(II) (equivalently
G2b exclusion, equivalently the G2a-side same-root correlation in the
pointwise sibling) — now reformulated (this round) as the single bound
`0<f(β)<2K` on one offset sinusoid, in exact closed form.

### Dead ends (do not retry)
- `M0≤r2` bound lever — proven false (round 8, explicit counterexample,
  independently reproduced). Do not retry.
- Treating (I) and (II) as needing genuinely different techniques — this
  round shows they are literally `f` and `2K−f` of the *same* sinusoid, so
  a single unified argument suffices for both; don't dispatch them as two
  separate proof efforts.
- Do not expect `f(0)>0` or any full-period positivity — `R≥|K|` always
  (`R²−K²=sin²(2A+B)≥0`), so no global/full-period certificate can exist;
  the claim is intrinsically domain-restricted, exactly as with `Ψ(τ,A,C)`
  in the ptolemy route (round 6 finding) — same shape of obstruction,
  independently confirmed here in a different route's target.

### Small-case / intuition notes (conjectural where noted)
- Verified exactly (not conjecture): `g=2K−f`, `R²−K²=sin²(2A+B)`,
  `f(β=B)=(2sinA+sinB)sin(A+B)>0` unconditionally.
- Conjectural (numeric only, inherited from round 8's 25k-sample sweep, not
  independently re-run this round): `0<f(β)<2K` holds throughout the actual
  effective domain (β∈(0,γ) intersected with the `B2>0`/`Y>0` hypotheses).
- The true right endpoint `γ=min(∠B,∠C)` was not evaluated symbolically
  this round (only the simpler reference point `β=B`); this is the natural
  next concrete computation for a builder to attempt.
