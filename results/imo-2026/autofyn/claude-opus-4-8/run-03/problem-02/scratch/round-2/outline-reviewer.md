# Outline review — imo-2026-02 (IMO 2026 P2), round 2

Focus: verify the Orientation Lemma route that closes coordinate-identity's load-bearing
sign gap is genuinely rigorous (not numerics-in-disguise, not circular). I independently
verified the sign chain both numerically (83 admissible interior configs, zero exceptions:
`/tmp/check_signs.py`) and symbolically (the two half-vector cross-identities: `sympy`,
exact zero residual).

---

## coordinate-identity — VERDICT: APPROVE (build it; two bookkeeping corrections listed, non-fatal)

The Orientation Lemma route is **sound, non-circular, and non-numeric**. It genuinely closes
the round-1 gap. Verification of each link:

- **Mechanism is valid.** sign(arg((L−B)/(K−B))) = sign(cross(BK,BL)) and
  sign(arg((L−N)/(C−N))) = sign(cross(NC,NL)) (both are `sign Im[z2·conj(z1)]`). Same sign +
  equal unsigned magnitude (both in (0,π), equal by the hypothesis ∠LBK=∠LNC) ⟹ literal
  directed equality ⟹ EA=0 with ε=+1. This is an honest unsigned→directed upgrade, not an
  assertion. The final magnitude step (line 85 gap (d)) is real and must be written, but it
  is a one-liner and correct.
- **Lemma H** (barycentric): valid. K∈int△BMC, edge BM⊂line AB, so K on C-side of line AB ⟹
  sign(cross(BA,BK))=sign(cross(BA,BC)). I confirmed cross(BA,BC)=−h(p+q)<0 symbolically.
- **Lemma R** (ray-betweenness): valid. "K inside ∠LBA" is literally ray BK between BA,BL, so
  sign(cross(BK,BL))=sign(cross(BA,BK))=−1. L∈int△BNC ⟹ ray NL between NB,NC.
- **Half-vector cross-identity**: `cross(N−B,C−B)=½cross(A−B,C−B)=½cross(BA,BC)` — I verified
  this is EXACTLY zero residual in sympy. Parameter-free, no case split, no continuity. Good.
- **Target signs**, independently confirmed exceptionless over 83 interior configs:
  `cross(BK,BL)=cross(NC,NL)=−1`, `cross(CL,CK)=cross(MB,MK)=+1`. Matches the outline.

**Corrections the builder MUST apply (do not copy the outline verbatim at these spots):**

1. **Sign-naming slip in the Condition-A bullet (outline line 69).** It writes
   "`cross(NC,NB) = −cross(N−B,C−B) = +½h(p+q) > 0`". The object equal to `+½h(p+q)` is
   `cross(NB,NC)`, **not** `cross(NC,NB)`. I verified symbolically `cross(NB,NC)=+h(p+q)/2`
   but `cross(NC,NB)=−h(p+q)/2 < 0`. The correct chain: `cross(NB,NC)=+½h(p+q)>0` (this
   matches the outline's own correct reference bullet, line 54–60) ⟹ by Lemma R at N,
   `cross(NL,NC)` shares that sign (>0) ⟹ `cross(NC,NL)=−cross(NL,NC)<0`, i.e. `−1`. The final
   target `−1` is right; only the intermediate label is wrong. The outline flags "carry the
   two-swap sign carefully" — this is exactly that swap; get it right.
2. **Condition-B mirror: state the orientation reversal explicitly.** σ (B↔C, M↔N, K↔L) is a
   reflection, so it **reverses** planar orientation; that is precisely why the mirror target
   is `+1` and not `−1`. The builder must note the reflection flips the cross-product sign,
   not silently carry `−1` through. I confirmed `cross(CL,CK)=cross(MB,MK)=+1` over all 83
   configs, and `cross(MC,MB)=−h(p+q)/2` symbolically (the C/M reference sign).

**Other required (already in the outline's gap list, keep):** delete the numerical-model
sentences (lines 54–56, 65–68 of the approach file); scope the §5 continuity argument strictly
to the finite `a_K·a_L=0` zero-set (it is NOT the orientation step); state the one-line
∠LBA<π check (no reflex reading); extract the whole thing as `lemmas/orientation-sign.md`.

No circularity: the certified algebraic engine (ideal identity, remainder 0) and the geometric
Orientation Lemma are independent; FK=FL=0 is established from interiority, then substituted.
This is the strongest approach and is now one rigorous, fully-scoped lemma from a complete solve.

---

## pow-reduction-trig — VERDICT: APPROVE (advance as independent-framing insurance)

Lemmas 1–3 are rigorous per round-1 review. GAP-2 (the balance identity E(β)≡0) is genuinely
open and numeric-only. This route does NOT share the orientation wall (its reduction used
unsigned law-of-sines magnitudes), so keeping it live preserves field diversity — correct call.

Caveat for the builder: the outline's mechanism for E(β)≡0 ("should reduce to a product-to-sum
/ sum-to-product sine collapse") is a **hope, not a mechanism**. The build task is to actually
produce the symbolic identity in sympy (express all sub-triangle lengths via law of sines,
expand pow(M,ω)−pow(N,ω), simplify to 0) — a numeric recheck is not progress here. If the sine
collapse does not close cleanly this remains partial; that is acceptable (it is insurance).

---

## synthetic-sigma-spiral — not in build set this round (correct)

Same orientation wall as coordinate-identity PLUS an additional open crux (c·MX=b·NY). Once
`lemmas/orientation-sign.md` is certified from the coordinate-identity build, this route can
import it to discharge its Steps 3–4 sign bullets — but its own crux stays open, so it is lower
priority. Leave for a later round unless a third builder is free (then advance by importing the
lemma). No new logical flaw; ranked below the two build-set approaches.

## midpoint-doubling-phantom — unbuilt, lowest Elo. Not this round.

## orientation-sign (shared lemma) — correctly NOT a rival slug

Registered as a lemma target (`lemmas/orientation-sign.md`), built inside coordinate-identity,
certified separately. Not registered in the ranker (it is not a whole-problem attempt). Correct.

---

## Field diversity check

The field is NOT collapsed to one framing. coordinate-identity (complex/coordinate) and
pow-reduction-trig (power-of-a-point / law-of-sines) hit **different** walls: the orientation
sign vs. the E(β)≡0 trig identity. synthetic-sigma-spiral shares the orientation wall but that
wall is being closed this round. Good separation; no single-gap trap.

## Registration / ranking

No new slugs to register (both build-set approaches already in the population). Ranked the whole
field head-to-head via `update_ranking`:
coordinate-identity 1558 (closest to solve, route verified sound this round) >
pow-reduction-trig 1553 (one honest open gap) > synthetic-sigma-spiral 1472 (two open gaps) >
midpoint-doubling-phantom 1416 (unbuilt). Stale flags cleared.

build set: coordinate-identity, pow-reduction-trig
