(Bernoulliovo schéma)
#MAT #MAT/Pravděpodobnosti 

$n$ nezávislých pokusů
- `true`(zdařilý) - $p$
- `false`(nezdařilý) - $q$
$p+q=1$

$A_{k}$ - $k=$ počet `true`
$P(A_{k})=\begin{pmatrix}n\\k\end{pmatrix}\cdot p^k\cdot q^{n-k}$
---
$$
\begin{align}
n = 10 \\
p = 0.25 \\
k=5 \\
\sum_{k=5}^{10}\frac{n!}{k!\left(n-k\right)!}\cdot\left(\frac{1}{4}\right)^{k}\cdot\left(\frac{3}{4}\right)^{\left(n-k\right)}\approx\boxed{0.0781269073486}
\end{align}
$$
---
$$
\begin{align}
p_{1}=0.95 \\
p_{2}=0.90 \\
p_{3}=0.80 \\
 \\
P_{1}=0.684 \\
 \\
P_{2}=0.019 \\
 \\
P_{3}=0.032
\end{align}
$$