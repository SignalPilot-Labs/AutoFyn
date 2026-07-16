# One-orbit tail-envelope lemma

Under the hypotheses of the arithmetic-orbit lemma, suppose the displacement \(g=f-\mathrm{id}\) satisfies, for all positive \(x,y\),
\[
|g(x)-g(y)|(2x+2y+g(x)+g(y))\le (x-y-g(y))^2. \tag{D}
\]
If \(g(v)=c>0\), then
\[
|g(t)-c|\le \frac{c^2}{8t}\qquad(t\ge v+c/2).
\]

## Proof

The arithmetic-orbit lemma gives \(g(v+nc)=c\) for every integer \(n\ge0\). For \(t\ge v+c/2\), let
\[
k=\left\lfloor\frac{t-v}{c}+\frac12\right\rfloor.
\]
Then \(k\ge1\) and \(|t-(v+kc)|\le c/2\). Set \(y=v+(k-1)c\). Thus \(g(y)=c\), and (D) gives
\[
|g(t)-c|(2t+2y+g(t)+c)\le (t-(v+kc))^2\le c^2/4.
\]
The arithmetic-orbit lemma also gives \(g(t)\ge0\), so the coefficient on the left is at least \(2t\). Division yields the claim. ∎
