# Lemma: Branch / orientation lemma (angle conditions become sign-fixed cross-products)

**Certified** (proof-reviewer, round 1). All four sign claims re-derived independently.

Coordinates `B=(0,0)`, `C=(a,0)`, `A=(p,q)` with `q>0`; `M,N` midpoints of `AB,AC`.
For vectors `V,W` write `cross(V,W)=V_1W_2−V_2W_1`, `dot(V,W)=V_1W_1+V_2W_2`, and let
`δ(V,W)∈(−π,π]` be the oriented angle from `V` to `W`.

Under the problem's region hypotheses (`K∈△BMC`, `L∈△BNC`) and inside-angle hypotheses
(`K` inside `∠LBA`, `L` inside `∠ACK`):

- `K` lies on the clockwise side of ray `BA` (`cross(A−B,K−B)<0`) and the CCW side of ray
  `CA` (`cross(A−C,K−C)>0`); the same two side-relations hold for `L`.
- Consequently the four oriented angles equal the corresponding unsigned angles, all in
  `(0,π)`:
  `δ(B−M,K−M)=∠BMK`, `δ(L−N,C−N)=∠LNC`, `δ(L−B,K−B)=∠LBK`, `δ(L−C,K−C)=∠LCK`.

**Proof.** The two side-relations for `K` follow from region membership: line `BA` passes
through `B,M`, and `cross(A−B,C−B)=−qa<0`, so all of `△BMC` (edge `BM` on the line, third
vertex `C`) is on the clockwise side; strict interiority gives `cross(A−B,K−B)<0`.
Likewise `cross(A−C,B−C)=qa>0` and `cross(A−C,M−C)=aq/2>0`, so `△BMC` is on the CCW side
of `CA`, giving `cross(A−C,K−C)>0`. For `L∈△BNC`: `cross(A−C,B−C)=qa>0` (edge `CN` on line
`CA`), so `cross(A−C,L−C)>0`; and `cross(A−B,N−B)=−qa/2<0`, so `cross(A−B,L−B)<0`.

Given the sides, oriented-angle additivity (valid because all rays sit within a common
half-plane relative to `BA`/`CA`, no wraparound) turns the "inside-the-angle" betweenness
into the four equalities. Directly, `cross(B−M,K−M)=s·t_K(p²+q²)>0` and
`cross(L−N,C−N)=s·t_L((p−a)²+q²)>0` (with `K` on the ray `t_K·u`, `L=C+t_L·d_L`, `s>0`,
`t_K,t_L>0`) confirm the first two; the other two follow from the inside-angle hypotheses
via `δ(L−B,K−B)=(−∠KBA)−(−∠LBA)=∠LBK` and `δ(L−C,K−C)=∠ACK−∠ACL=∠LCK`.

**Use.** This converts the unsigned angle equalities of conditions 2,3 into
`cross(L−B,K−B)·dot(L−N,C−N)=cross(L−N,C−N)·dot(L−B,K−B)` and the analogue for cond 3,
with no lost sign or spurious branch.
</content>
