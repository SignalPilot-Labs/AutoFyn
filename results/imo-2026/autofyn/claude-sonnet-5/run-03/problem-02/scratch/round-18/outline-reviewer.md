# Round 18 — outline-reviewer

## Independent re-verification of the round's critical claim (gap 6 identity)

I re-derived, from scratch, the two defining functions directly from the
raw definitions in `approaches/coordinate-bash-resultant-boundary-
pointwise-tangent.md` and `lemmas/d1-nonnegative-on-boundary-curve.md`
(own fresh `sympy` session, own `X_0, β_0, K_c, P, Q, G` built term by
term, not copied from the explorer's report or the outliner's
reconstruction):

```
G_curve(u) = 2*(8*sin(u)**2 - 3)*sin(u)*cos(u)**2      [u := A/3 + π/6]
h(u)       = cos(2u) - 1/4                              (= 3/4 - 2 sin²u)
```

`sp.expand_trig(G_curve_u - (-8 sin u cos²u)·h_u)` returns exactly `0`.
**The identity `G_curve(A) = -8 sin(u) cos²(u) · h(A)` is confirmed —
independently re-derived, exact, zero residual.** This matches the
explorer's report and the outliner's summary of it.

(a) **Identity holds exactly** — confirmed above, own derivation.

(b) **Cofactor nonzero on the relevant domain** — confirmed. For
`A∈(0,π/2)` (the population's already-established domain fact, round 11
of `-pointwise`), `u=A/3+π/6∈(π/6,π/3)⊂(0,π/2)`, so `sin u,cos u>0`
strictly; no case split needed.

(c) **`G_curve(A*)=0` already certified, and — new finding beyond what
either report claimed — A\* actually has an exact closed form.**
Solving `G_curve(u)=0` on `(π/6,π/3)` reduces (via the identity's own
factorization, or directly) to `8 sin²u = 3`, i.e. `sin u = √6/4`, which
has a **unique** solution on `(π/6,π/3)` since `sin` is strictly
increasing there and `sin²u` sweeps `(1/4,3/4)∋3/8`. Hence
$$A^* = 3\arcsin(\sqrt6/4) - \pi/2 \quad\text{exactly.}$$
Checked numerically against the population's standing 40-digit value
(`0.4063777806843303293871746903293092626710…`): agreement to `~10⁻⁴²`.
Checked symbolically: `sympy.simplify(G_curve(u*))` and
`sympy.simplify(h(u*))` both return exact `0` at `u* = asin(√6/4)`,
confirmed independently (own `sympy` session, `solveset` on the open
interval also returns exactly this one point). **This means fact (ii)
(`h(A*)=0`) no longer needs to route through the identity + a separately
"already-certified" numeric root at all — it is directly, trivially
verifiable in closed form.** This closed form also resolves the deeper
worry behind the round-17 rejection: previously `A*` was only known via
`mpmath.findroot` (a floating-point search, not a certificate), so
"`G_curve(A*)=0`" was itself only high-precision numerics, not a proof.
With the closed form, `G_curve(A*)=0` is a one-line algebraic
verification, no root-finding required. This makes the gap-6 closure
stronger than either the explorer or outliner realized — not just an
"iff" reducing one unproved fact to an already-certified one, but a
route that removes the numeric-root dependency from the whole argument.

**Caveat for the builder, not a blocker.** The rest of the lemma
(`d1-nonnegative-on-boundary-curve.md` Steps 1–4) still uses a
certified `mpmath.iv` bracket of `B*` built from the old floating-point
value; that machinery is fine to reuse as-is (the bracket only needs to
contain the true `B*`, and the closed form confirms the existing bracket
does, to `10⁻⁴²` margin), but the builder should note in the writeup that
`A*`'s closed form is available and consistent, since it strengthens
several "certified"-but-numeric citations elsewhere in the file (e.g. the
Step 1 `Φ`-bracket) without requiring them to be redone.

## Verdict on the outliner's field

The outliner's top-priority claim survives independent re-derivation in
full, and is in fact slightly understated (a bonus closed-form for `A*`
was found in this review, not previously reported). This is a real,
verified narrowing of gap 6, not a repeat of round 17's false claim —
round 17's rejection specifically targeted an *unproved* coincidence
cited as free; this round supplies the actual proof of that coincidence,
independently checked from raw definitions two ways (symbolic identity +
exact closed-form root), not a numeric coincidence dressed up again.
**It is not yet a certified lemma** — correctly, the outliner does not
mark anything solved; this remains scouted content for the builder to
write up rigorously (multiple-angle expansion shown as hand-checkable
polynomial arithmetic, per the outliner's own instruction) and for the
proof-reviewer to adjudicate. Given the population's one false
solved-claim already on this exact route (round 17), the builder must
not mark Status `solved` prematurely — that call is the reviewer's, per
the outliner's own build instructions (item 4), which I confirm are
correctly scoped.

The reconstructed diversity-report content (SOS's 3 diagnostic tests,
`spiral-similarity-bootstrap`'s framing) is reasonable and consistent
with `current.md`'s round-17 record and the live `-sos` and
`spiral-similarity-bootstrap.md` files, which I read directly. No
reason to distrust the reconstruction on the points that matter for
build dispatch.

## Ranking actions taken

- Registered `spiral-similarity-bootstrap` (was unregistered — confirmed
  absent from `.ranking.json` before this review), cold-start Elo 1500,
  summary reflecting its corrected framing (target `ℓ = h(A,1/2)`(perp-
  bisector(BC)), not a false "O = fixed point" claim, per the file's own
  already-recorded self-correction).
- Recorded one head-to-head comparison reflecting this round's actual
  outcome differential: `coordinate-bash-resultant-boundary-pointwise-
  tangent` over `coordinate-bash-resultant-boundary-pointwise-sos`
  (independently-verified real progress on a sharp, previously-unproved
  identity vs. continued honest diagnostic work with no certificate).
  New Elo: tangent 1756.6, sos 1555.6.
- `coordinate-bash-resultant-boundary` intentionally left untouched
  (sat out this round, no new work, already `stale:true`, no prejudice —
  matches the outliner's own framing).

## Build set — confirmed, unchanged from the outliner's recommendation

All three of the outliner's picks hold up under independent scrutiny:
`-tangent` for the (now more strongly evidenced) gap-6 closure attempt,
`-sos` as continued honest insurance/diagnostic work, and
`spiral-similarity-bootstrap` as genuine diversity insurance against the
field's concentration on the coordinate-bash/resultant family (now
sharper risk than usual, since a single silent gap in `-tangent` would
be a single point of failure for the whole run if it were the only live
route).

build set: coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary-pointwise-sos, spiral-similarity-bootstrap
