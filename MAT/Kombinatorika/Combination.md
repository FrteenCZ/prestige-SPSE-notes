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
