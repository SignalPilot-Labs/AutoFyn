# Lemma 0: Nine-point-center reduction of OM = ON

**Statement.** Let ABC be a triangle, M and N the midpoints of AB and AC
respectively, and N9 the nine-point center of ABC (the circumcenter of the
medial triangle). For any point P in the plane,
```
PM² − PN² = (2P − M − N)·(N − M).
```
Consequently, for any point O,
```
OM = ON  ⟺  (O − N9)·(C − B) = 0.
```

**Proof.** The first identity is the vector difference-of-squares
`|a|² − |b|² = (a+b)·(a−b)` applied with `a = P−M`, `b = P−N`, so
`a+b = 2P−M−N` and `a−b = N−M`.

Since M and N are the midpoints of two sides of ABC, both lie on the
nine-point circle of ABC, hence `N9M = N9N`. Instantiating the first
identity at `P = O` and at `P = N9` and subtracting (the `−M−N` part of the
first factor is independent of P and cancels in the subtraction, leaving
only the linear-in-P part):
```
OM² − ON² − (N9M² − N9N²) = 2(O − N9)·(N − M),
```
and since `N9M² − N9N² = 0`, this gives `OM² − ON² = 2(O − N9)·(N − M)`.
Because M, N are the midpoints of AB, AC, segment MN is the midline of ABC
parallel to BC, so `N − M = (C − B)/2`. Substituting:
```
OM² − ON² = (O − N9)·(C − B),
```
which is zero iff `OM = ON` (since OM, ON ≥ 0). ∎

**Coordinate corollary (WLOG frame B=(0,0), C=(1,0), A=(p,q)).** In this
frame, `C − B = (1,0)`, so `OM = ON ⟺ O_x = (N9)_x`. Direct computation of
the circumcenter of the medial triangle `M=(p/2,q/2)`, `N=((p+1)/2,q/2)`,
midpoint(B,C)=(1/2,0) gives `(N9)_x = p/2 + 1/4` (independently verified by
symbolic computation, `sympy`, in the round-1 review). So the target reduces
to the single scalar identity `O_x = p/2 + 1/4`.

**Status.** Fully proved, unconditional on the K,L hypotheses of the
problem. Independently re-derived and symbolically checked (sympy) by the
round-1 proof-reviewer; used by all three round-1 approaches
(`complex-number-argument-bash`, `nine-point-locus-two-position`,
`spiral-similarity-radical-axis`). Certified for shared reuse.
