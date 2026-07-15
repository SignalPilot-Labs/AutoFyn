# Corrected directed-coordinate and incidence lemma

Normalize `A=0`, `B=e_0`, `C=q e_\gamma`, where `q>0` and `0<\gamma<\pi`. Put
`\alpha=\angle KBA=\angle ACL`, `\beta=\angle LBK=\angle LNC`, and
`\delta=\angle LCK=\angle BMK`. The interior ray orders give
\[
K=e_0-r e_{-\alpha}=\tfrac12e_0+s e_\delta
=q e_\gamma-w e_{\gamma+\alpha+\delta},
\]
\[
L=q e_\gamma-u e_{\gamma+\alpha}
=e_0-v_0e_{-(\alpha+\beta)}=\tfrac q2e_\gamma+z e_{\gamma-\beta},
\]
with all six parameters positive. Taking oriented determinants gives
\[
r=\frac{\sin\delta}{2\sin(\alpha+\delta)},\qquad
v:=\frac uq=\frac{\sin\beta}{2\sin(\alpha+\beta)}.
\]
The positivity of the ray parameters and of `\sin\beta,\sin\delta` proves that both denominators are positive. The remaining two incidences give
\[
q=F(\delta),\qquad qF(\beta)=1,
\]
where
\[
F(t)=\frac{\cos\gamma-\cos t\cos(\gamma+2\alpha+t)}
{2\sin^2(\alpha+t)}.
\]

This is certified by direct determinant expansion and the displayed product-to-sum computation in the reviewed approach.
