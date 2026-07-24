# Lemma: σ-invariance and the supplementary relation

**Certified** (proof-reviewer, round 1). Relabelling checked; L2 re-derived and numerically
confirmed (`∠LBA+∠NLC=180.000°` on admissible configs).

## L1 (σ-invariance)
The relabelling `σ : A↦A, B↔C, M↔N, K↔L` maps the problem's hypothesis-and-conclusion
system to itself: it **fixes** condition 1 (`∠KBA=∠ACL`), **swaps** condition 2
(`∠LBK=∠LNC`) and condition 3 (`∠LCK=∠BMK`), maps each region/inside-angle hypothesis to
another such hypothesis, and **fixes** the conclusion `OM=ON` (since `σ` permutes `{A,K,L}`
it fixes `⊙AKL` and hence `O`, and swaps `M,N`).

*Proof.* Relabel vertices in each unsigned angle: `∠KBA↦∠LCA=∠ACL`, `∠ACL↦∠ABK=∠KBA`
(cond 1 fixed); `∠LBK↦∠KCL=∠LCK`, `∠LNC↦∠KMB=∠BMK` (cond 2 ↦ cond 3), and `σ²=id` gives
cond 3 ↦ cond 2. Region: `K∈△BMC ↦ L∈△CNB=△BNC`, `K` inside `∠LBA ↦ L` inside `∠KCA=∠ACK`,
both hypotheses; symmetrically for `L`'s constraints. □

**Caveat.** `σ` is a FORMAL relabelling symmetry, not an isometry when `AB≠AC`; by itself
it forces nothing about `O`. It only licenses "prove a B-side fact, get the C-side by σ."

## L2 (supplementary relation)
Under the hypotheses, `∠LBA + ∠NLC = π`, and its σ-image `∠KCA + ∠MKB = π`.

*Proof.* `K` inside `∠LBA` gives `∠LBA=∠KBA+∠LBK`. By cond 2, `∠LBK=∠LNC`; by cond 1,
`∠KBA=∠ACL`. So `∠LBA=∠ACL+∠LNC`. Since `N∈` segment `AC`, ray `CN=`ray `CA`, so
`∠LCN=∠ACL`. Angle sum in `△LNC`: `∠LNC+∠LCN+∠NLC=π`, i.e. `∠LNC+∠ACL=π−∠NLC`.
Substituting, `∠LBA=π−∠NLC`. Apply L1 to obtain `∠KCA+∠MKB=π`. □
</content>
