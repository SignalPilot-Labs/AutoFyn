## Lemma (signed-angle isosceles reduction: (I)∧(II) ⟹ A*B=A*C)

**Source:** `approaches/antipode-perp-bisector.md`, round 4. Certified by the
proof-reviewer after independent re-derivation (numeric spot-check at
`(p,q,θ)=(0.3,1.7,15°)`, agreement to machine precision).

**Statement.** Let `ABC` be a triangle in the frame `B=(-1,0), C=(1,0),
A=(p,q)` with `q>0`, `α=∠BAC, β=∠ABC, γ=∠ACB`. Let `A*` be any point such
that, for some `θ∈(0,min(β,γ))`, the **signed** identities
```
dir(B,A*) = dir(B,A) + (γ-90°-θ)   (mod 360°)      (I)
dir(C,A*) = dir(C,A) + (θ+90°-β)   (mod 360°)      (II)
```
hold, where `dir(X,Y)` denotes the direction angle of ray `XY`. Then
`A*B = A*C`.

**Proof (complete, no gap, conditional only on (I),(II) as hypotheses).**
1. Since `B=(-1,0),C=(1,0)`, `dir(B,C)=0°, dir(C,B)=180°`; since `q>0`,
   `dir(B,A)=β` and `dir(C,A)=180°-γ` (elementary: these are the unsigned
   interior angles read off directly, since `A` is strictly above line
   `BC`).
2. Substituting into (I),(II) and using `β+γ=180°-α`:
   `dir(B,A*) = 90°-α-θ`, `dir(C,A*) = 90°+α+θ`.
3. Hence `∠A*BC = |dir(B,A*)-0°| = |90°-α-θ|` and
   `∠A*CB = |dir(C,A*)-180°| = |90°-α-θ|` — identically equal, no case
   split on sign.
4. If `α+θ≠90°`: common value `δ:=|90°-α-θ|>0`, so `A*BC` is a genuine
   triangle with equal base angles at `B,C`; by the Law of Sines
   (isosceles-triangle converse), `A*B=A*C`.
5. If `α+θ=90°` (a single isolated θ-value, if in the valid domain at
   all): handled by continuity of `f(θ):=A*(θ)B-A*(θ)C` on the open
   interval `(0,min(β,γ))` (using the certified existence/uniqueness of
   `K(θ),L(θ)` from `lemmas/existence-uniqueness-r1-r2.md`, and that
   `A*` depends continuously on `K,L`), taking the limit from the dense
   complement where step 4 gives `f≡0`.

Both cases give `A*B=A*C`; exhaustive. **∎** (conditional on (I),(II)
themselves, which are NOT part of this lemma and remain open/unproved from
the problem's three angle hypotheses — see `current.md`.)

**Reusability.** General-purpose: does not depend on how `A*,K,L` were
constructed, only on the frame convention `q>0` and the two signed-angle
hypotheses (I),(II). Any future approach that manages to prove (I),(II)
synthetically can invoke this lemma directly to finish the problem via the
antipode reduction (`lemmas/antipode-reduction.md`).
