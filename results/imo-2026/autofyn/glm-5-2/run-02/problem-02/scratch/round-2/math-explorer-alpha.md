# imo-2026-02 — lens: the α-condition crux

## Summary verdict

The α-condition **is** the closing step for both crux identities, and I can now state the mechanism precisely. Three load-bearing findings:

1. **The round-1 notes had the WRONG external-angle sign.** The directed external-angle theorem on Γ is the **SUM** form, not the difference form the notes guessed. This gives a clean arc-sum equality for α.
2. **The `power-secant-product` approach has a SIGN ERROR in Step 4 (iv).** `∠CAW = -(b+β)` in directed form, **not** `b-β` as written. The approach's stated crux (**) with `sin(b-β)` is **FALSE** (off by 0.04–0.09 across every tested config). The **corrected** (**) with `sin(b+β)` holds to machine precision. This is the numpy sign-trap the round-1 rules warned about — it bit the approach.
3. **α is load-bearing (necessity + sufficiency, verified).** Dropping `∠KBA = ∠ACL` (keeping the β and γ conditions) makes **both** the corrected (**) **and** `OM=ON` fail simultaneously. So α is exactly the missing condition; it is not a shared-wall artifact.

---

## Where each crux is stuck (exact quotes)

**`antipode-rightangle` (T):** the gap is (approach file, §Gap):
> "Unproved: the derivation of identity (T) from (R1) together with the metric constraints (C1),(C2) … A direct sympy symbolic derivation was attempted but did not terminate within the round budget."

(T): `cos C · cos(∠AKL) · cos(∠BLA) = cos(C+β) · cos(∠BKA) · cos(∠ALK)`.
(T) was "verified to 1e-14" — and (T) ⟺ OM=ON (rigorous trig-Ceva reformulation), so (T) is TRUE; the gap is purely the *derivation* from (R1)+(C1)+(C2).

**`power-secant-product` (**):** the gap is (approach file, Step 5):
> "Identity (**) … Proving it requires deploying the THIRD angle condition `∠KBA = ∠ACL` (the α-condition) … via the external-angle theorem on Γ (B and C are exterior to Γ), it is equivalent … to `2α = arc(KP) − arc(AR) = arc(QL) − arc(AS)`."

(**) as stated: `sin a · sin(γ−a) · sin u · sin(γ−u) / sin²γ = sin b · sin(b−β) · sin w · sin(w+β) / sin²β`.
The arc relation quoted is the **WRONG (difference) form**; and the `sin(b−β)` is a **sign error** (see §Sign error below). The corrected identity is what actually holds.

---

## Finding 1 — The directed external-angle theorem on Γ is the SUM form

For an external point X with two secants meeting Γ at (near₁, far₁) and (near₂, far₂), the **directed** angle between the secants is

> ∡(secant₁, secant₂) = ½·[ arc(far₁ → far₂) + arc(near₁ → near₂) ]   (mod π),

arcs directed CCW mod 2π. This was verified numerically by brute force over all arc pairings: the **only** combination reproducing `∡(BA,BK) = -α` is `½(arc(AR)+arc(PK))` (B-side) and `½(arc(AS)+arc(QL))` (C-side), NOT any difference. (Named: directed external angle = inscribed-angle theorem applied to the two secant lines, treating the external point as a limit; KB `Geometry — synthetic toolkit, angle chasing` / `circle/triangle configuration facts`.)

Consequence — the **α-condition translates to the arc-sum equality** (verified to 1e-14 on scalene/isoceles/obtuse/tall triangles, α ∈ {10,20,25,30}°):

> **2α = arc(RA) + arc(KP) = arc(AS) + arc(QL)   (mod 2π),**

where P = 2nd∩(AB,Γ), Q = 2nd∩(AC,Γ), R = 2nd∩(BK,Γ), S = 2nd∩(CL,Γ). This **corrects** the round-1 notes' `2α = arc(KP) − arc(AR) = arc(QL) − arc(AS)` (wrong sign). Equivalently, since `arc(KP) = -arc(PK) = -2u` and `arc(QL) = 2w`:
> `arc(RA) = 2(α + u)`,   `arc(AS) = 2(α − w)`.

So the α-condition fixes the angular positions of R and S on Γ (relative to A) in terms of α, u, w.

## Finding 2 — Sign error in `power-secant-product` Step 4 (iv); corrected crux (**)

Step 4 (iv) claims `∠CAW = b − β`. Numerically (scalene A=(0,0),B=(4,0),C=(1,3), α=25°): `∠CAW = 41.95°`, but `b − β = -56.16° − 14.21° = -70.37°`. They are **not equal** (mod 180° either: 41.95 vs 109.63). The correct directed identity (verified to 1e-15 across all 12 tested configs) is

> **∠CAW = -(b + β)**   (directed mod π),

i.e. `∠CAW = -b - β`. (The approach's `b - β` only matches if b, β are taken as unsigned *magnitudes* — the round-1 "acute-angle numpy pick" trap, exactly as warned.) The other three Step-4 lemmas are correct: `∠ALV = γ-u` ✓, `∠BAV = γ-a` ✓, `∠AKW = -(w+β)` ✓. (All verified to 1e-13.)

This propagates into (**): the approach computes
`NL·NW = 4R² · sin b · sin(∠AKW) · sin w · sin(∠CAW)/sin²β`
`     = 4R² · sin b · sin(-(w+β)) · sin w · sin(-(b+β))/sin²β`
`     = 4R² · sin b · sin(b+β) · sin w · sin(w+β)/sin²β`   (two minus signs cancel).

So the **corrected crux identity** is

> **(**)_corr:   `sin a · sin(γ−u) · sin u · sin(γ−a) / sin²γ  =  sin b · sin(b+β) · sin w · sin(w+β) / sin²β`**

(the RHS has `sin(b+β)`, not `sin(b−β)`). Verified to ~1e-13 across 11 configs (scalene/isoceles/obtuse/tall × α∈{10,20,30}°; one obtuse α=30 config hit a fsolve branch issue, not a counterexample). The approach's written `sin(b−β)` version is **false** at the same configs (off by 0.04–0.09).

### Arc form of the corrected crux (verified to 1e-16)

Using `sin(½arc(XY)) = |XY|/(2R)` and `2γ = arc(AV)+arc(PK)`, `2β = -(arc(AW)+arc(QL))`:

> **LHS =** `sin(½arc(AK))·sin(½arc(AV))·sin(½arc(PK))·sin(½arc(PV)) / sin²(½(arc(AV)+arc(PK)))`
> **RHS =** `sin(½arc(AL))·sin(½arc(QW))·sin(½arc(QL))·sin(½arc(AW)) / sin²(½(arc(AW)+arc(QL)))`

where V = 2nd∩(MK,Γ), W = 2nd∩(NL,Γ). Note `arc(AK)+arc(PV) = arc(AV)+arc(PK) = 2γ` (directed-arc additivity, automatic). Ptolemy on cyclic quad (A,V,P,K) is the natural tool (verified: `AV·PK + VP·KA = AP·KV`).

## Finding 3 — α is load-bearing (necessity + sufficiency)

I dropped the α-condition by letting `∠KBA = α_B` and `∠ACL = α_C` vary independently (keeping `∠LBK=∠LNC=β`, `∠LCK=∠BMK=γ`), solving the 2 incidence equations for (β,γ). Results:

| α_B | α_C | LHS_corr | RHS_corr | **(LHS−RHS)** | **OM−ON** |
|----|----|----|----|----|----|
| 25° | 25° (α holds) | -0.13533 | -0.13533 | 1e-16 | 2e-15 |
| 25° | 20° (dropped) | -0.12337 | -0.13628 | **0.0129** | **0.057** |
| 30° | 20° (dropped) | -0.11994 | -0.15121 | **0.0313** | **0.147** |

So when the α-condition is dropped, **the corrected (**) fails AND OM=ON fails, in lockstep** (and the failure grows as α_B−α_C grows). When α holds, both hold to machine precision. Hence α is exactly the closing condition for (**) (and, since (**) ⟺ OM=ON, for the theorem). This is a clean necessity-and-sufficiency numerical certificate.

---

## The remaining bridge for the builder

The α-condition's arc-sum equality involves **R and S**, but the corrected (**) involves only **A,K,P,V** (B-side) and **A,L,Q,W** (C-side) — R, S do not appear in (**). So the bridge is **not** a one-step arc manipulation; it must also use the **midpoint/incidence structure** that defines V, W from R, S:

- B, M are both on line AP (M = midpoint of AB, so `AM = MB = AB/2`). Lines through K and B, K and M meet Γ again at R and V. The pencil at K projectively maps the line AP to Γ, sending (A,P,B,M) ↦ (A,P,R,V). So **(A,P;R,V) = (A,P;B,M)** as cross-ratios — this is the projective link between R and V via the midpoint.
- Symmetrically, (A,Q;S,W) = (A,Q;C,N) via the pencil at L, with N midpoint of AC.

So the α-condition (arc-sum, fixing R and S on Γ) + the two projective cross-ratio links (midpoint structure, fixing V from R and W from S) together must yield the corrected (**). The builder's job: combine (a) the α arc-sum, (b) the projective/pencil relation (midpoint → cross-ratio on Γ), (c) Ptolemy on the cyclic quads, to derive the corrected (**) — or, on the antipode side, to derive (T) from (R1)+(C1)+(C2). Both (T) and (**)_corr are ⟺ OM=ON, so closing either one closes the problem.

### Candidate mechanism (named, not developed — the builder's call)

- **Ptolemy** on cyclic quad (A,V,P,K): `AV·PK + VP·KA = AP·KV`. Expresses products of `sin(½arc)` — the building blocks of the arc-form LHS. Likely the core algebraic identity once R,S are eliminated.
- **Projective cross-ratio** `(A,P;R,V) = (A,P;B,M)` via the pencil at K (and the C-side analogue) — this is the midpoint structure entering as a clean projective relation, eliminating R in favour of V (and S in favour of W). KB `Geometry — synthetic toolkit` (projective ideas / power of a point).
- **Directed external-angle theorem, SUM form** (Finding 1) to translate the α-condition into the arc-sum — the entry point.

---

## Cheap-kill candidates
- The α-drop numerical certificate (Finding 3) is a cheap *necessity* check, not a proof. No parity/pigeonhole-style kill applies — this is a pure angle-chase/trig identity problem.

## Knowledge-base entries to use (named)
- `Geometry — synthetic toolkit`: angle chasing, **power of a point** (secant form: `MA·MP = MK·MV` — the reduction), trig cevians (Ceva/Menelaus — the (T) reformulation).
- `Geometry — circle/triangle configuration facts`: **inscribed-chord formula** `chord = 2R sin(½arc)`, **Ptolemy** (the natural identity for the arc-form products), Thales (the antipode characterisation).
- `Geometry — synthetic toolkit`: **projective ideas / cross-ratio** (the pencil-at-K link (A,P;R,V)=(A,P;B,M) — the midpoint structure).
- `General Proof Methods — direct proof` + directed angles mod π (the SUM-form external angle).

## Analogous past problems (cruxes)
The crux corpus has **no geometry cruxes** (`crux_moves_documentation.md`: "geometry — Not in the corpus yet"). The problems DB does have geometry solutions; the closest analogous (judged by setup, not by crux since none extracted):
- **`aimo-0021` (IMO-SL 2013 G2)** — M,N midpoints of AB,AC; crux move = *reflection about the perpendicular bisector of AT* mapping M↔X, N↔Y (homothety+reflection exploiting midpoint symmetry). Analogous because it shares the M,N-midpoints-of-AB,AC setup and uses a midpoint-symmetry move; the *mechanism differs* (reflection vs our arc-sum/external-angle), so it is a hint to *look for a midpoint-symmetry simplification* — but no reflection sends B↔C here (the configuration is not B↔C symmetric: the α-condition is the one asymmetric angle).
- **`aimo-0644` (USA_TSTST 2011 4)** — M,N midpoints of AB,AC; crux = *homothety at H between circumcircle and nine-point circle* + power of a point `MH·HP' = HN·HQ'` → M,N,P,Q concyclic → radical axis. Analogous because it reduces a midpoint/circumcentre claim to a power-of-a-point product equality at the two midpoints — exactly the structure of our `power-secant-product` reduction `OM=ON ⟺ MK·MV = NL·NW`. The crux move (homothety+power product at midpoints) is the *same reduction family*; the *closing identity* there is a power equality, here it is the α-driven sine-product.
- **`aimo-0705` (USAMO 2024 5)** — crux = *directed-angle chase* `∠BEM = ∠ABM` proving tangency, exploiting a midpoint M and an equal-angle condition. Analogous only in flavour (directed-angle chase + midpoint); the configuration is different.

Best match: **`aimo-0644`** (same midpoint-power-product reduction family). No crux move is directly portable; both reductions here need the α arc-sum, which is problem-specific.

## Prior progress
- `antipode-rightangle`: full chain rigorous down to (T); (T) verified, derivation gap open.
- `power-secant-product`: reduction + sine-rule expressions + Step 4 lemmas (3 of 4 correct) rigorous; crux identity stated but **wrong-signed** (see Finding 2). After sign fix, (**)_corr verified.
- `analytic-branch-cert`: central certificate FALSE (ring pseudo-remainder artifact); not the route to push.
- Numerically the theorem holds to ~1e-12 on every sampled configuration; the open problem is purely a rigorous closing argument. My α-drop experiment confirms *what* that closing argument must use (the α-condition, via the SUM-form external angle).

## Dead ends (do not retry)
- The **DIFFERENCE-form** external-angle relation `2α = arc(KP) − arc(AR)` (round-1 notes) — **wrong**; the SUM form is `2α = arc(RA)+arc(KP)`. Do not re-derive with the difference form.
- The **`sin(b−β)`** version of (**) (round-1 `power-secant-product` Step 5) — **false**; use `sin(b+β)`. Do not re-verify the wrong version (the round-1 "verified to 1e-6" was the numpy sign-trap the rules warned about).
- The three "spiral similarities" and isogonality `∠BAK=∠CAL` — all FALSE (round 1, verified); do not revive.
- The `analytic-branch-cert` saturation certificate (Prop 4) — FALSE (ring pseudo-remainder); do not revive without a correct field-reduction certificate.

## Small-case / intuition notes (conjecture labels)
- **Conjecture (numerically certain, not proven):** the α-condition (via the SUM-form external-angle arc-sum `2α = arc(RA)+arc(KP) = arc(AS)+arc(QL)`), combined with the pencil-at-K cross-ratio `(A,P;R,V) = (A,P;B,M)` (midpoint structure) and its C-side analogue, implies the corrected (**)_corr. Every piece is verified numerically; the symbolic derivation is the builder's open task.
- **Conjecture:** the same mechanism closes (T) on the antipode side (since (T) ⟺ (**)_corr ⟺ OM=ON, all equivalent); (T)'s derivation from (R1)+(C1)+(C2) is the same α-condition, encoded in (C1),(C2).
- Ptolemy on (A,V,P,K) and (A,W,Q,L) is the most likely single algebraic identity to absorb the arc-form LHS/RHS once R,S are eliminated via the cross-ratio links.

## Promotable lemmas worth certifying into `results/imo-2026-02/lemmas/`
1. **Lemma (directed external angle, SUM form).** *For an external point X with two secants meeting Γ at (near₁,far₁),(near₂,far₂), `∡(secant₁,secant₂) = ½[arc(far₁→far₂)+arc(near₁→near₂)]` (mod π, arcs directed CCW).* Verified numerically across all configs; proof = directed inscribed-angle theorem (limit of an inscribed angle as the vertex tends to the external point). Reusable by ANY approach that needs to express an external angle on Γ as an arc relation (both `antipode-rightangle` and `power-secant-product` need it).
2. **Lemma (α arc-sum).** *`∠KBA = ∠ACL = α` ⟺ `2α = arc(RA)+arc(KP) = arc(AS)+arc(QL)` (mod 2π)*, with P,Q,R,S the 2nd intersections of AB,AC,BK,CL with Γ=(AKL).* Direct corollary of Lemma 1. This is the α-condition's on-Γ translation.
3. **Lemma (corrected Step-4 sign).** *`∠CAW = -(b+β)` (directed mod π), where b=∠AKL, β=∠LNC, W=2nd∩(NL,Γ).* Corrects the round-1 `b−β`. Reusable by `power-secant-product` and any Γ-chord approach.
4. **Lemma (α is load-bearing — numerical certificate).** *With the β,γ conditions enforced, the corrected (**) (and hence OM=ON) holds iff ∠KBA=∠ACL.* Numerical (necessity+sufficiency); not a proof, but a certificate that the α-condition is the right target and that no further hidden constraint is needed. Useful for the outliner to know the gap is exactly one condition.
5. **Lemma (projective cross-ratio link — stated, needs proof).** *With M the midpoint of AB and R=2nd∩(BK,Γ), V=2nd∩(MK,Γ), the pencil at K gives `(A,P;R,V) = (A,P;B,M)` as cross-ratios (line AP ↔ Γ).* The midpoint structure enters here. (This is the candidate bridge; unproven but numerically the projectivity holds.) If certified, it eliminates R in favour of V and is the key to deriving (**)_corr from the α arc-sum.

---

*Files: report at `/tmp/round-2/math-explorer-alpha.md`. Approach files read: `results/imo-2026-02/approaches/{antipode-rightangle,power-secant-product}.md`, `results/imo-2026-02/current.md`. No proof written; scouting only.*
