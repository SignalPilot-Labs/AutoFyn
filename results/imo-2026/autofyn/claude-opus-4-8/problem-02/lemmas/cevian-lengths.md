# Lemma (certified, round 1) — cevian lengths BK, CL

Source approach: `power-of-point-BC` (also in `trig-lawofsines`). Certified by
proof-reviewer.

Set `θ=∠KBA=∠ACL` (E1), `β=∠LBK=∠LNC` (E2), `γ=∠BMK=∠LCK` (E3). `M,N` midpoints of
`AB,AC`.

> **BK = (AB/2)·sinγ / sin(θ+γ)**,   **CL = (AC/2)·sinβ / sin(θ+β)**.

*Proof.* In `△BMK`, `M` lies on segment `AB` so ray `BM=`ray `BA`, giving
`∠MBK=∠KBA=θ`; `∠BMK=γ`; hence `∠BKM=π−θ−γ`. With `BM=AB/2`, Law of Sines gives
`BK=BM·sin(∠BMK)/sin(∠BKM)=(AB/2)sinγ/sin(θ+γ)`. Mirror in `△CNL` (`∠NCL=∠ACL=θ`,
`∠CNL=β`, `CN=AC/2`) gives `CL`. ∎

Status: gap-free, elementary Law of Sines. CERTIFIED.
