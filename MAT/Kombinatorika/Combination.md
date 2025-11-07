#MAT #MAT/Kombinatorika 
**neuspořádaná** (**nezáleží** na pořadí) *k-tice* z n prvků
$$
\begin{align}
C_{k}(n)=\begin{pmatrix}
n \\
k
\end{pmatrix} = \frac{n!}{k!(n-k)!} 
\end{align}
$$
---
$$
\begin{gathered}
\text{všechny} && - && \text{chlapci} &&-&& \text{dívky} &&=&& \text{CHxD} \\
C_{2}(25) &&-&& C_{2}(15) &&-&& C_{2}(10) &&=&& 150
\end{gathered}
$$
# vlastnosti kombinačních čísel
$$
\begin{gathered} \\
n\geq k\\
\begin{pmatrix}
n \\
k
\end{pmatrix} = \frac{n!}{k!(n-k)!} \\
\begin{pmatrix}
n \\
1
\end{pmatrix}=n\\
\begin{pmatrix}
n \\
n
\end{pmatrix}=1 \\
\begin{pmatrix}
n \\
0
\end{pmatrix}=1 \\
\begin{pmatrix}
n \\
n-k
\end{pmatrix}= \begin{pmatrix}
n \\
k
\end{pmatrix} \\
\begin{pmatrix}
n \\
k
\end{pmatrix}
+
\begin{pmatrix}
n \\
k+1
\end{pmatrix}
=
\begin{pmatrix}
n +1\\
k+1
\end{pmatrix}
\end{gathered}
$$
---

# Příklady
$$
\begin{pmatrix}
4 \\
4
\end{pmatrix}
+
\begin{pmatrix}
5 \\
4
\end{pmatrix}
+
\begin{pmatrix}
6 \\
4
\end{pmatrix}
+
\begin{pmatrix}
7 \\
4
\end{pmatrix}
+
\begin{pmatrix}
8 \\
4
\end{pmatrix}
=
\begin{pmatrix}
4 \\
4
\end{pmatrix}+2\cdot\begin{pmatrix}
4 \\
3
\end{pmatrix}+4\cdot\begin{pmatrix}
4 \\
2
\end{pmatrix}
+ 8\cdot\begin{pmatrix}
4 \\
1
\end{pmatrix}+16\cdot\begin{pmatrix}
4 \\
0
\end{pmatrix}
=
\begin{pmatrix}
126 \\
1
\end{pmatrix}
$$
---
$$
\begin{align}
\begin{pmatrix}
n \\
n-2
\end{pmatrix} = \frac{n!}{(n-2)!(2)!} = \frac{n\cdot(n-1)\cdot(n-2)!}{(n-2)!\cdot2!}=\frac{n^{2}-n}{2} \\
\\
\begin{pmatrix}
n+5 \\
n+3
\end{pmatrix} - \begin{pmatrix}
n+4 \\
n+2
\end{pmatrix} = \begin{pmatrix}
n+4 \\
n+3
\end{pmatrix} = \frac{(n+4)!}{(n+3)!(1)!}=\frac{(n+4)}{1}=n+4 \\
 \\
5n=\begin{pmatrix}
n \\
n-2
\end{pmatrix} = \frac{n^{2}-n}{2} \\
10n=n^{2}-n \\
11n-n^{2}=0 \\
n(11-n)=0 \\
n=\{ \cancel0,11 \}
\end{align}
$$
---
$$
\begin{align}
\begin{pmatrix}
x \\
x-2
\end{pmatrix}+\begin{pmatrix}
x \\
x-1
\end{pmatrix}=\begin{pmatrix}
x+1 \\
2
\end{pmatrix} \\
\begin{pmatrix}
x+1 \\
x-1
\end{pmatrix}=\begin{pmatrix}
x+1 \\
2
\end{pmatrix} \\
\frac{(x+1)x}{2}=\frac{(x+1)!}{2(x-1)!} \\
x^{2}+x=x^{2}+x \\
0=0 \\
x \in N-\{ 1 \}
\end{align}
$$
---
$$
\begin{align}
\begin{pmatrix}
x+3 \\
x+1
\end{pmatrix}-3\begin{pmatrix}
x-1 \\
x-2
\end{pmatrix}=7 \\
\frac{(x+2)(x+3)}{2}-\frac{3\cdot(x-1)}{1}=7 \\
x^{2}+5x+6-6x+6=14 \\
x^{2}-x-2=0 \\
x=\{ -1, 2 \} \\
\boxed{P=\{ 2 \}}
\end{align}
$$