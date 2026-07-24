# proof-builder report — imo-2026-02 / slug trig-metric-identity

Status: **solved** (complete, rigorous, general triangle).

## What I proved
`OM=ON` for the whole 1-parameter family, via the metric route.

Chain:
1. **Reduction (by hand, §1).** Frame `B=(0,0),C=(a,0),A=(p,q)`, `q>0`. Since `M,N`
   share height `q/2`, `OM²−ON²=(a/2)(2O_x−(2p+a)/2)`, so `OM=ON ⇔ O_x=(2p+a)/4`
   (= the stated `OB²−OC²=(AB²−AC²)/2`). No K,L used.
2. **Branch fixing (§2–3), the reviewer's flag (a).** From the region hypotheses I
   prove by half-plane sign tests that `K` is clockwise of ray `BA`, CCW of ray `CA`;
   same for `L`. This fixes the two rotation directions (`K=t_K·u`, `L=C+t_L·d_L`,
   `t_K,t_L>0`, common `s=tan(θ/2)>0`) AND the orientation of all four relevant angles.
   Two crosses are manifestly positive: `cross(MB,MK)=s·t_K(p²+q²)`,
   `cross(NL,NC)=s·t_L·|CA|²`; the other two (`cross(BL,BK)`, `cross(CL,CK)`) are forced
   positive by the "inside angle LBA / inside angle ACK" betweenness. So each unsigned
   angle equals its oriented angle in `(0,π)` — no lost sign.
3. **Exact encoding + decoupling (§4).** Conditions 2,3 ⇔ `E2=0`, `E3=0`
   (`sin(δ1−δ2)=0` with both args in `(−π,π)`). Crucially `E2=t_K·H(t_L)` and
   `E3=t_L·G(t_K)` — the system **decouples**: `H` depends only on `t_L`, `G` only on
   `t_K` (both quadratic). So conditions ⇔ `G(t_K)=0`, `H(t_L)=0`.
4. **Crux identity (§5), the reviewer's flag (b).** Target `T:=4·num_x−(2p+a)·D`.
   Exact polynomial division over `Q(p,q,a,s)` gives explicit cofactors with
   `T = q_G·G + q_H·H` **identically** — checked as an EXACT symbolic zero
   (`expand(q_G·G+q_H·H−T)=0` and remainder `0`, two `assert`s), not a numeric sweep.
   Script: `results/imo-2026-02/verify.py` (runs in ~2s, prints the two zeros).
5. **Conclude:** `G=H=0 ⇒ T=0 ⇒ O_x=(2p+a)/4 ⇒ OM=ON`. ∎

## Reviewer flags addressed
- (a) Signs/branches: handled by the half-plane + betweenness Orientation Lemma (§2–3),
  giving a genuine `⇔` between each unsigned angle condition and its polynomial; no
  square-and-hope, no spurious roots relied on.
- (b) sympy = exact symbolic zero only: yes — the decisive step is an exact cofactor
  identity `T=q_G·G+q_H·H` via exact division; numerics were used ONLY to pick the branch,
  which §3 then proves. Script saved under `results/imo-2026-02/verify.py`.

## Gap remaining
None. The proof does not even need solvability of the family (L2 in the old outline):
the problem hands us `K,L`; I only use that any admissible `(K,L)` satisfies `G=H=0`,
and the ideal-membership identity then forces the conclusion.

## Spec concerns
None. `answer_type=none` (proof only); no final numeric answer required.

## Note for reviewer / population
- Promotable: **L1** (coordinate goal reduction) and **L-orient** (branch-fixing
  orientation lemma) — both fully proved, listed in the approach file.
- The decoupling `E2=t_K·H(t_L)`, `E3=t_L·G(t_K)` is the structural reason the family is
  tractable; it reflects that `∠LBK,∠LNC` depend only on `L` (direction of `BK` fixed by
  θ) and `∠LCK,∠BMK` only on `K`. Useful hint for the synthetic approaches.
