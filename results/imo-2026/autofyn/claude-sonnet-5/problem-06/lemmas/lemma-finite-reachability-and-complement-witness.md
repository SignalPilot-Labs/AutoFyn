# Complement Witness Fact, Escape-Confinement Pairwise-Disjoint-Bundle-Count Corollary, and the Finite-Reachability Theorem

**Source.** `results/imo-2026-06/approaches/persistent-backbone-monovariant.md`
(round 8, "Round 8: Realized–Blocked Dichotomy, the Pigeonhole Corollary,
and the Finite-Reachability Theorem"). Depends on the already-certified
Escape-Confinement Lemma (`lemmas/lemma-escape-confinement.md`),
`lemmas/lemma-ERD-realized-blocked-dichotomy.md` (RBD, merged this round),
and the Permanent Bundle Lemma's (SA) hypothesis
(`lemmas/lemma-permanent-bundle.md`).

## Complement Witness Fact

**Statement.** If `I_S≠∅` for a proper core `S`, then `J_{S^c}≠∅`, where
`S^c:=P_1∖S`.

**Proof.** Let `i∈I_S` (`rad(a_i)∩P_1=S` exactly). For any `q∈S^c`:
`q∈P_1` and `rad(a_i)∩P_1=S` (not `S∪{q}`), so `q∉rad(a_i)`. Hence
`rad(a_i)∩S^c=∅`, i.e. `i∈J_{S^c}`. `∎`

**Scope note.** This proves the complementary direction to the standing
open "core-avoiding witness `j_3` with `rad(a_{j_3})∩S=∅`, i.e.
`J_S≠∅`" hypothesis — it does **not** by itself establish `J_S≠∅`.
(**Superseded in part** by `lemmas/lemma-SR-self-realized-core-shortcut.md`'s
Cross-approach synergy note: combining this file's own RBD Lemma with Lemma
SR shows the `J_S≠∅`/core-avoiding-witness hypothesis is not actually
needed as an independent open gap — see that lemma file.)

## Escape-Confinement Pairwise-Disjoint-Bundle-Count Corollary

**Statement.** Fix a proper core `S` with `I_S≠∅`, and suppose a
core-avoiding witness `j_3` exists (`rad(a_{j_3})∩S=∅`). Then **every**
family of pairwise-disjoint bundles for `S` (`Q_i:=rad(a_i)∖S`, `i∈I_S`)
has size `≤|comp(a_{j_3})|`.

**Proof.** `S` is blocked by `j_3`. By the RBD Lemma, `S` is (therefore)
never realized, so every `i∈I_S` is an escape from `κ:=S`. By the
Escape-Confinement Lemma, every bundle `Q_i` contains a prime of the fixed
finite set `W_0:=comp(a_{j_3})`. A pairwise-disjoint family
`{Q_{i_1},…,Q_{i_r}}` then injects into `W_0` (choosing one witness prime
per bundle; distinct by disjointness), giving `r≤|W_0|`. `∎`

**Scope note.** Bounds pairwise-*disjoint* families only, not the total
count of realized bundles (which can pairwise-intersect and still be
infinite). This is the identical mechanism, phrased independently, as
`sunflower-bundle-closure`'s §4b Case (a) Corollary (see
`lemmas/theorem-UBS-sufficiency.md`) — genuine cross-approach convergence,
not a coincidence, since both derive from the same Escape-Confinement
Lemma applied identically to `κ=S`.

## Finite-Reachability Theorem (conditional on NIBC)

**Setup.** For each blocked bare value `κ`, fix `j(κ):=min{j:rad(a_j)∩κ=∅}`
and `W_κ:=comp(a_{j(κ)})`. Define `R_0:={S}`,
`R_{t+1}:={κ∪{q}:κ∈R_t, κ blocked, q∈W_κ}`, `R:=⋃_{t≥0}R_t`. **NIBC** ("No
Infinite Blocked Chain" for `S`): no infinite sequence
`S=κ_0⊊κ_1⊊κ_2⊊⋯` with every `κ_t` blocked and
`κ_{t+1}∈{κ_t∪{q}:q∈W_{κ_t}}`.

**Statement.** If `S` satisfies NIBC, `R` is finite.

**Proof (sketch, full detail in the source file).** Each `R_t` is finite by
induction (finite branching, `|W_κ|<∞`). If `R` were infinite, `R_t≠∅` for
every `t` (monotone extinction), so the associated finitely-branching path
tree `𝒯` (nodes = paths `(κ_0,…,κ_t)`) has a node at every depth. By a
directly-proved form of König's Lemma for finitely-branching trees (proved
from scratch: greedily extend a path whose subtree has nodes at unboundedly
many depths, which some child must inherit by finite branching), `𝒯` has an
infinite path — an infinite blocked chain, contradicting NIBC. `∎`

**Reachability Theorem for (SA)-bundles.** If a core-avoiding witness for
`S` exists and `Q` is a bundle for `S` satisfying the Permanent Bundle
Lemma's Subset Avoidance (SA) hypothesis, then `S∪Q∈R` (proved by an
explicit induction on `|Q|` constructing a chain in `R`, using the
Escape-Confinement Lemma at each step to extract a new element of `Q`; full
detail and a hand-verified worked example, `a_1=2747,S={67},Q={2,3,7}`, in
the source file).

**Corollary.** If a core-avoiding witness for `S` exists and `S` satisfies
NIBC, the number of distinct (SA)-satisfying bundles for `S` is finite (at
most `|R|`); combined with the already-certified Permanent Bundle Lemma,
this bounds the count of **permanent** bundles for `S`.

## Honest scope limit (proved, not merely diagnosed, by the source)

Every bundle **not** satisfying (SA) is unreachable via this construction
(immediate contrapositive), and every transient (eventually-dominated)
bundle fails (SA) by definition (its dominator, once it exists, realizes a
proper subset of the bundle). Hence this entire mechanism (Corollary +
Escape-Confinement Corollary) is structurally blind to transient bundles —
it can only ever bound the permanent/(SA)-satisfying share of `Λ_S`, never
the transient share, which remains a fully open, separate difficulty.

## Certification

All statements independently re-derived by the round-8 proof-reviewer
(Complement Witness Fact: one-line, no gap; Pairwise-Disjoint Corollary: no
gap, confirmed identical mechanism to `sunflower-bundle-closure`'s version;
Finite-Reachability Theorem: the König's-Lemma-style argument re-derived
by hand, no gap, standard "greedily extend along an infinitely-extending
child" argument; Reachability Theorem: the inductive chain construction
re-derived and independently checked against the worked example
`a_1=2747,S={67},Q={2,3,7}` via a fresh sequence generator — `a_2=2788`
(rad `{2,17,41}`), `a_3=2814` (rad `{2,3,7,67}`), `a_4=2829` (rad
`{3,23,41}`), `a_{10}=3157` (rad `{7,11,41}`) — exact match with the
source's claimed witnesses and extracted primes `2,3,7` in that order).
Certified `solved`-quality for all unconditional statements; the
Finite-Reachability Theorem and its Corollary are certified as **conditional**
on NIBC (open) and core-avoiding-witness existence (dissolved — see
`lemmas/lemma-SR-self-realized-core-shortcut.md`'s synergy note — leaving
NIBC as the sole remaining open hypothesis for this specific mechanism).
