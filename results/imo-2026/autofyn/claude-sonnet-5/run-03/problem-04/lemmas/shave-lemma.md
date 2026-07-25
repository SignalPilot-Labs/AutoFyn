# Lemma: Pure shave / forced-shave chain (Lemma 2)

**Source.** Certified from `approaches/ngon-arc-reduction.md`; the identical statement (as
"Shave lemma" / "Down-shave lemma") is independently re-derived in `shave-and-halve-forcing.md`
and `maximal-safe-set-fixedpoint.md`.

**Statement.** Suppose the current triangle has some angle X > θ at vertex R, with the other
two angles Y (at P), Z (at Q). Cutting from R to the point on PQ with t = θ (a legal cut by
the Cut Formula, since 0 < θ < X) gives child1 = (Y, θ, 180−Y−θ), child2 = (Z, X−θ, Y+θ).
Child1 already contains the angle θ, so Shan-Yu is forced (on pain of an immediate loss) to
keep child2. Consequently: whenever the current triangle has an angle equal to an exact
positive integer multiple kθ (k≥1) at some vertex, Mulan can force — regardless of Shan-Yu's
play — a deterministic sequence of k−1 further such moves at the same vertex, after which
that vertex's angle equals exactly θ, ending the game in her favor.

**Proof.** Direct substitution t=θ into the Cut Formula; child1's middle coordinate is
literally θ, so keeping it is an immediate loss for Shan-Yu, forcing child2. In child2 the
shaved vertex's angle becomes X−θ = (k−1)θ; iterate at the same vertex while (k−1)≥1 falls
by exactly one multiple of θ each application; the game stops (Mulan wins) the moment this
value first equals θ, i.e. after k−1 applications. ∎

**Status.** No gap; certified for reuse.
