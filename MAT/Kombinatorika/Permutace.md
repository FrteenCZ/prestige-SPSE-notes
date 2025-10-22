#MAT/Kombinatorika #MAT
# Bez opakování
**uspořádaná** k-tice z k čelnů
= [[Faktoriál]]
$$
\begin{align}
P_{n}&=n! && \text{bez opakování}
\end{align}
$$
# Permutace s opakováním
Pokud se prvky ve výběru mohou opakovat, pak počet permutací s opakováním z $n$ prvků je určen
$$
P^{\prime}\left(k_1, k_2, \ldots, k_n\right)=\frac{\left(k_1+k_2+\ldots+k_n\right)!}{k_{1}!\cdot k_{2}!\cdot \ldots \cdot k_{n}!}
$$
kde se jednotlivé prvky opakují $k_{1},k_{2},\dots ,k_{n}$ -krát

---
Kolik anagramů z  
$$
\begin{align}
\{ P;R;A;H;A \} && &P'(1,1,2,1)=\frac{(1+1+2+1)!}{1!\cdot1!\cdot 2! \cdot 1!}=\frac{120}{2}=\boxed{60} \\
\{ A,B,R,A,K,A,D,A,B,R,A \} && &P'(5, 2, 2, 1, 1)=\frac{11!}{120\cdot 2 \cdot 2 \cdot 1 \cdot 1}=\boxed{83160} \\
\{ \text{Mazda}, \text{Škoda}, \text{Tatra} \} && &P'(2,2,2)=\frac{6!}{2\cdot 2\cdot 2}=\boxed{90} \\
\{ 4, 4, 4, 4, 3, 3, 3, 3, 3, 3 \} && &P'(4, 6)=\frac{10!}{24 \cdot 720}=\boxed{210}
\end{align}
$$