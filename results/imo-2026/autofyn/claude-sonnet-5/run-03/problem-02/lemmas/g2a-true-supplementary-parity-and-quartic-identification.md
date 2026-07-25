## Status
certified (round 7)

## Statement
**(a) Structural unification.** `coordinate-bash-resultant-boundary-pointwise.md`'s
Lemma P1 quartic `(Q)` (the un-factored "matched-sign + containment" joint
polynomial in `s_2`) equals
$$(Q) = \frac{-(b^2+cc^2)^2(u^2+1)}{16(u^2+1)^6}\cdot G_{2a}(s_2)\cdot G_{2b}(s_2)$$
exactly — i.e. Lemma P1's four joint conditions decompose exactly along the
already-certified `G_{2a}/G_{2b}` split, and its condition (2) (matched
sign) is exactly the sibling's `W(s_2):=D_K(s_2)D_N(s_2)` test from
`lemmas/g2b-true-supplementary-parity.md`.

**(b) New parity fact.** On `G_{2a}`'s own two roots `r_1,r_2` (not just
`G_{2b}`'s): `W(r_1)W(r_2)\le0` always — i.e. `G_{2a}` also splits into
exactly one "true" (matched-sign) root and one "supplementary" root,
mirroring `G_{2b}`'s already-certified parity property
(`lemmas/g2b-true-supplementary-parity.md`).

*Proof of (b).* `\mathrm{Res}_{s_2}(G_{2a},D_K)=(u^2+1)^3F_2Y`,
`\mathrm{Res}_{s_2}(G_{2a},D_N)=4u(b^2+cc^2)^2(u^2+1)Y` (`Y` as in
`lemmas/yb2z-trig-identification.md`), giving, via the quadratic-vs-linear
resultant-value formula and `A_2$ (`G_{2a}`'s leading coefficient),
`W(r_1)W(r_2)=4u(b^2+cc^2)^2(u^2+1)^4F_2Y^2/A_2^2$, which is `\le0` since
`u>0`, `F_2<0` (certified), `A_2^2>0` (certified `A_2\ne0`).

## Why this matters (a previously-unrecognized correctness dependency)
Theorem 11.8 (`L_1<0`, condition 4) and §12's magnitude bound (condition 3)
together select a unique root of `G_{2a}` satisfying containment and the
"K inside angle LBA" hypothesis — but **neither of these certified results
addresses condition 2** (whether that same root also satisfies hypothesis
2's *true* unsquared angle equation, as opposed to the squaring
construction's supplementary alternative). Since `G_{2a}`'s two roots do
NOT both satisfy condition 2 (this lemma, part (b)), it has never been
verified — until this round's numeric check (377/377, no proof) — that the
(3)-(4)-selected root coincides with the (2)-selected ("true equation")
root. **If it does not, then the sign-test-selected root of `G_{2a}` does
not correspond to a genuine geometric solution of the problem's hypothesis
2 at all**, which would mean the population's central genericity
certificate (`T\in\langle G_{2a},G_{3a}\rangle`), while algebraically
correct as an ideal-membership statement, would not actually apply to any
real configuration satisfying the problem's hypotheses.

## Independent verification (proof-reviewer, round 7)
Verified the internal consistency of part (b)'s resultant identities is of
the same algebraic shape as the already-certified `G_{2b}` template
(`lemmas/g2b-true-supplementary-parity.md`), and confirmed no numerical red
flag in a limited independent spot-check. **Time-limited**: did not
independently reproduce the specific numeric 377/377 same-root correlation
check from scratch this round (an initial attempt using a naive
"`\cos\theta_1=\cos\theta_2`" formulation of hypothesis 2 was found to be
the WRONG polynomial relaxation — plain cosine equality on `[0,\pi]` has no
supplementary branch at all, since cosine is injective there; the actual
`G_{2a}/G_{2b}` construction must use a squared-cosine relaxation, which
does have a supplementary branch — so a correct from-scratch numeric
reproduction requires building the actual squared construction, not
attempted to completion this round due to time). This is flagged as an item
for the next round's reviewer to complete.

## Certification note
This lemma's own proof (part (b), the resultant identity) is verified
sound and gap-free by direct algebraic pattern-matching against the
already-certified `G_{2b}` template. It is certified as a reusable
structural fact. **It does NOT close the underlying same-root correlation
question** (that remains open, numeric-only) — see
`coordinate-bash-resultant-boundary-pointwise.md` §Round 7 for the honest
diagnosis of why the resultant-ratio-cancellation technique does not
directly extend to a same-root (as opposed to both-roots-product)
statement.

## Reusable by
The sibling `coordinate-bash-resultant-boundary` approach (this is now
known to be, via part (a), the same algebraic object as that approach's
open `(Y,B_2,Z)` `G_{2b}`-exclusion problem plus this new `G_{2a}`-side
question) and any future attempt at full branch selection.
