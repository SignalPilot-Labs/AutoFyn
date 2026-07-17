# Lemma DyadicLower — confined lower bound A ≥ 1 on Δ (certified round 6)

**REPLACES and REFUTES** the round-5 "Descent Lemma" / "receiver-existence" claim, which was
rejected (receiver-existence FALSE at a=0 clustered vertices, e.g. n=4 frags
{2,10/3,10/3,11/3,11/3}). Those never entered `lemmas/`; this file is the corrected replacement.

**Setup (units of §3).** Intacts I = {2^0,…,2^{n−1}} fixed; fragments a nonnegative multiset with
≤ n+1 slots summing to 2^n. A = alternating sum of the merged sorted list = μ{N odd} (Lemma R),
piecewise-affine on the simplex Δ = {(g_1,…,g_{n+1}) : g_i ≥ 0, Σ g_i = 2^n}. By the fragment-count
bound at most one fragment exceeds 2^{n−1} (a ≤ 1); write R = {a=0} = {all fragments ≤ 2^{n−1}}.

**Statement.** For every n ≥ 3, min_Δ A ≥ 1; equivalently the confined lower bound O ≥ 2^n holds.
(n ≤ 2 by the direct base-case analysis §7.)

**Directional derivative (verified at tie-laden configs).** For a mass transfer e_a − e_b
(fragment a up, fragment b down), the one-sided derivative is
    A′₊(e_a − e_b) = (−1)^{G(g_a)} + (−1)^{Geq(g_b)},
G(v)=#{pieces > v}, Geq(v)=#{pieces ≥ v}. (Reviewer-verified in exact arithmetic over 5·10^4
tie-laden multisets; up-move uses G, down-move uses Geq.) Call a **receiver** a fragment with G odd.

**Proof.** On the a=1 part A ≥ 1 (top-fragment cascade §4.2.4). On R take a global minimiser v (A
continuous, R compact). The top piece is the intact 2^{n−1}. Dichotomy on the max fragment w_1:

- **Case 1 (w_1 ≤ 2^{n−2}).** The second-largest piece is the intact 2^{n−2}, so
  A(v) ≥ v_1 − v_2 = 2^{n−1} − 2^{n−2} = 2^{n−2} ≥ 1 (all later brackets of the sorted alternating
  sum are ≥ 0). Holds at every such point, no minimality needed. (Both round-5 counterexamples land
  here: max frag ≤ 4 = 2^{n−2}, giving A = 5.)

- **Boundary (w_1 = 2^{n−1}).** Borrowing ε from a second positive fragment yields nearby a=1 configs
  (A ≥ 1); by continuity A(v) ≥ 1.

- **Case 2 (2^{n−2} < w_1 < 2^{n−1}).** Only the intact 2^{n−1} exceeds w_1, so G(w_1) = 1 (odd):
  **w_1 is a named receiver by counting** (not an existence claim — valid at ties). For each distinct
  positive fragment b the direction e_{w_1} − e_b is feasible; minimality gives
  A′₊ = −1 + (−1)^{Geq(b)} ≥ 0, forcing Geq(b) even: **no positive fragment is a donor.** Let f_min be
  the smallest positive fragment, N_tot = n + #{positive fragments}.
  - (2a) N_tot odd: f_min can't be the global min (else Geq(f_min)=N_tot odd = donor), so the global
    min is the intact 1, all fragments > 1, and 1 sits at rank N_tot (odd) contributing +1 while the
    remaining even-count block has alternating sum ≥ 0. Hence A(v) = A′ + 1 ≥ 1.
  - (2b) N_tot even, f_min > 1: transfer e_{w_1} − e_{f_min} is flat (A′₊ = 0) until f_min crosses the
    largest intact I* < f_min, after which A′₊ = −2. Either w_1 reaches 2^{n−1} first (a=1 closure,
    A(v) ≥ 1) or the descent past I* while interior contradicts minimality — so (2b) yields A(v) ≥ 1
    or is impossible.
  - (2c) N_tot even, f_min ≤ 1: f_min is the global min, transfer e_{w_1} − e_{f_min} is flat and
    crosses nothing (nothing in (0,f_min)), so A stays = A(v) until w_1 reaches 2^{n−1} (a=1, A ≥ 1)
    or f_min reaches 0, giving a minimiser v′ with one fewer positive fragment and N_tot(v′) odd,
    closed by (2a). Well-founded: #{positive fragments} strictly decreases (floor 2 = a=1 boundary),
    and the first flat step already flips N_tot to odd.

Exhaustive on w_1 ∈ (0, 2^{n−1}]; hence min_R A ≥ 1, and with the a=1 cascade A ≥ 1 on all of Δ. ∎

**Verification.** Reviewer-checked min_Δ A = 1 exactly, 0 failures over 2·10^5 random + clustered
a=0 configs each n = 3,4,5 (including tie-laden vertices).

**Scope / what this does NOT close.** This is the **confined** lower bound (all XY cuts inside R_n).
It does NOT settle **L2** — XY spending cuts *outside* R_n (fragmenting an intact R_j, j<n) — which
needs the analogue on an augmented simplex. L2 remains an open lower-bound gap.

**Certification.** Reviewer-verified round 6: directional-derivative formula confirmed at ties;
Case-2 receiver named by counting (fixes the round-5 refutation); (2a/2b/2c) exhaustive and each
closed; flat-move termination via a strictly-decreasing integer weight. No empirical percentage in
the statement. Admitted to the shared cache.
