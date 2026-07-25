# Lemma U: `g(\theta)=\beta_L(\theta)-\alpha(\theta) \to A` as `\theta\to0^+`

**Status:** Certified (proof-reviewer, round 22).

**Source:** `approaches/ptolemy-trig-identity-synthetic.md`, Search 4 (Round 22),
"New Lemma U".

## Statement
Fix a triangle `ABC`. For `\theta\in(0,\min(B,C))`, let `U(\theta):=\cot\alpha(\theta)`
be the genuine (larger) root of `\tilde P_1U^2+\tilde Q_1U+\tilde R_1=0` with
`\tau=\tan\theta`,
`\tilde P_1=\sin A\,\tau(\tau\cos C-\sin C)`,
`\tilde Q_1=\sin A\sin C(\tau^2+1)+2\tau\sin B`,
`\tilde R_1=-2\tau^2\sin C\cos A-\tau\sin A\sin C+\sin A\cos C`,
i.e. `U=(-\tilde Q_1-\sqrt{\Delta_1})/(2\tilde P_1)`, `\Delta_1=\tilde Q_1^2-4\tilde P_1\tilde R_1`;
let `V(\theta)` be the same with `B,C` swapped. Set `\alpha=\pi/2-\arctan U`,
`\alpha'=\pi/2-\arctan V`, `\beta_L=A-\alpha'`, `g=\beta_L-\alpha`. Then
$$\lim_{\theta\to0^+}g(\theta)=A.$$

## Proof
At `\tau=0`: `\tilde P_1(0)=0`, `\tilde Q_1(0)=\sin A\sin C`, `\tilde R_1(0)=\sin A\cos C`,
so `\Delta_1(0)=\sin^2A\sin^2C`, `\sqrt{\Delta_1(0)}=\sin A\sin C`. The numerator
`N(\tau)=-\tilde Q_1-\sqrt{\Delta_1}` is continuous with `N(0)=-2\sin A\sin C\ne0`,
while `\tilde P_1(\tau)=\tau(-\sin A\sin C)(1+O(\tau))`. Hence
`U(\tau)=N(\tau)/(2\tilde P_1(\tau))=\tfrac1\tau(1+O(\tau))\to+\infty` as `\tau\to0^+`
(using `N(0)/(-2\sin A\sin C)=1`). Since `\tau=\tan\theta\to0^+` as `\theta\to0^+`,
`U(\theta)\to+\infty`, so `\alpha\to0`; identically `V\to+\infty`, `\alpha'\to0`,
`\beta_L\to A`, `g\to A`. `\blacksquare`

## Independent verification (round 22)
mpmath, 50 dps: `g(10^{-8})\to A` with diff `\approx2\times10^{-8}` (consistent with
the `O(\tau)` linear approach) for triangles `(A,B)=(1.1,1.1),(0.6,1.3),(1.9,0.5)`.

## Scope
A rigorous boundary value only. Does NOT close the approach's target `(\dagger)`
(`g(\theta)>0` on the whole domain): individual monotonicity of `\alpha,\beta_L` is
false (round-22 counterexample), and convexity of `g` alone is insufficient.
