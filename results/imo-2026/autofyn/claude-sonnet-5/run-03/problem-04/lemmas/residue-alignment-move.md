# Lemma: Residue-alignment cut (Lemma 3 of ngon-arc-reduction)

**Source.** `approaches/ngon-arc-reduction.md`. This is the key new move that closes the
"if" direction for all n ≥ 3 in one step, without any discrete/token-game reduction. It is
NOT a "forced" (shave-type) move in the sense of `mod-theta-invariant.md` /
`maximal-safe-set-fixedpoint.md` (those files prove pure shave/up-shave sequences alone can
never finish the "if" direction from a starting triangle with no angle a multiple of θ); this
lemma is precisely the "genuine non-forced move planting a value into both children" that
those files identify as necessary but do not construct. Verified independently by the
reviewer both algebraically and by randomized `Fraction`-exact simulation (n = 3..14,
thousands of trials, zero violations) and by full game-tree simulation of the resulting
strategy end-to-end (2600 random trials across n=2..14) — see proof-reviewer round-1 review.

**Statement.** Fix n≥3 and θ=180°/n. Suppose the current triangle (X,Y,Z) has NO angle that
is a θ-multiple, and X>θ (cut vertex R has angle X; the other two vertices P,Q carry angles
Y,Z). Write Y = mθ + r_Y with m=⌊Y/θ⌋≥0 and r_Y∈(0,θ) (strict, since Y is not a θ-multiple).
Cutting from R to the point on PQ realizing t = θ − r_Y produces
$$\text{child}_1=(Y,\ \theta-r_Y,\ (n-m-1)\theta),\qquad \text{child}_2=(Z,\ X-\theta+r_Y,\ (m+1)\theta),$$
with $1\le n-m-1\le n-1$ and $1\le m+1\le n-1$ both integers: **both possible children already
contain an angle that is an exact positive integer multiple of θ**, regardless of which one
Shan-Yu keeps.

**Proof.** See `approaches/ngon-arc-reduction.md`, §1, Lemma 3 (full algebra, including the
bound m ≤ n−2 derived from Y = 180−X−Z < 180−θ = (n−1)θ, and the positivity/angle-sum checks
for both children).

**Status.** No gap; certified for reuse.
