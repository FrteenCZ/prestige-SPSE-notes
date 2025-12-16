#MAT #MAT/Pravděpodobnosti
# Náhodný pokus
Náhodný pokus je **každá opakovatelná činnost prováděná za stejných podmínek**, jejíž výsledek je **nejistý** a závisí na **náhodě**.

**Příklady:**
- hod kostkou
- losování ve Sportce
- výběr žáků z třídy

## Množina všech možných výsledků
Vyjmenujeme **všechny možné výsledky**, které se navzájem **vylučují** → vzniká **množina všech možných výsledků**.

- Hod kostkou → 6 výsledků
- Ze 28 žáků vybíráme 4 → počet možností je $\begin{pmatrix}28\\4\end{pmatrix}$
- _Osudí_ = pytlík / krabice, ze které losujeme
- $A\cap B=\emptyset$ disjunktní - jevy se vzájemně vylučují = vzájemně neslučitelné

---

# Náhodný jev
Náhodný jev je **každá podmnožina** množiny všech možných výsledků.  
Jev vyjadřuje tvrzení o výsledku náhodného pokusu, o kterém lze rozhodnout, zda je **pravdivé**.

- Je pravdivý → jev **nastává**
- Je nepravdivý → jev **nenastává**

## Druhy jevů
- **Nemožný jev** – např. při hodu kostkou padne 7
- **Jistý jev** – padne číslo 1 až 6
- **Elementární jev** – výsledek, který již nelze dále rozložit
    - např. "padne 2"
    - **není elementární**: „padne sudé“ (lze rozložit na {2, 4, 6})

---

Máme 4 různé koule: **B, Č, M, Z**  
Vybíráme 2 koule ([[Combination]]):
$$  
\left\{  
\{B, Č\},  
\{B, M\},  
\{B, Z\},  
\{Č, M\},  
\{Č, Z\},  
\{M, Z\}  
\right\}  
$$
B: mezi taženými je B = 3
M: mezi taženými je M = 3
$B\cup M=5$
$B\cap M=1$

---

# Klasická definice pravděpodobnosti
**Pravděpodobnost jevu je mírou očekávání toho že daný náhodný jev nastane**

- náhodný splňuje předpoklady
	- všech možných výsledků je stejný počet
	- všechny jsou stejně pravděpodobné
	- všechny výsledky se navzájem vylučují
$$
\begin{align}
P(A)=\frac{m}{n}
\end{align}
$$
$m$ - počet příznivých výsledků jevu A
$n$ -  celkový počet výsledků

---
číslo od 1-20, P=? že je prime
$$
\begin{align}
\text{primes} = \{ 2, 3, 5,7, 11, 14, 17,19 \} \\
P(A)=\frac{8}{20}
\end{align}
$$
---
30 celkem
2   *1*
10 *2*
12 *3*
5   *4*
1   *5*

$$
\begin{gathered}
1 && 2,3 && <4 \\
P(1)=\frac{2}{30}=\frac{1}{15} && P(2,3)=\frac{22}{30}=\frac{11}{15} && P(1,2,3)=\frac{12}{15}
\end{gathered}
$$
---
dvě kostky
padne 1 a 1
$$
\frac{1}{6}\cdot \frac{1}{6} =\frac{1}{36}
$$
---
celkem 60
špatný  6
$P$ správný 4
$$
\begin{align}
P=\frac{\begin{pmatrix}
54 \\
4
\end{pmatrix}}{\begin{pmatrix}
60 \\
4
\end{pmatrix}} = 0.64
\end{align}
$$
---
ze 32 dostane 8
$P$ esa
$$
\begin{align}
P=\frac{\begin{pmatrix}
28 \\
4
\end{pmatrix}}{\begin{pmatrix}
32 \\
8
\end{pmatrix}}=\pu{ 2‰ }
\end{align}
$$
---
500 lístků
5 *1.*
10 *2.*
40 *3.*
$$
\begin{align}
P(\text{výhra}) = \frac{55}{500}=0.11
\end{align}
$$---
25 studentů
10 dívek
5 lístků
$$
P=\frac{\begin{pmatrix}
10 \\
2
\end{pmatrix}\cdot \begin{pmatrix}
15 \\
3
\end{pmatrix}}{\begin{pmatrix}
25 \\
5
\end{pmatrix}}=\frac{13}{43}
$$
---
52 karet
4 vybíram
$$
\begin{align}
\text{esa}=1 && \text{esa}\geq1 \\
P=\frac{4\cdot\begin{pmatrix}
48 \\
3
\end{pmatrix}}{\begin{pmatrix}
52 \\
4
\end{pmatrix}} && P'=\frac{\begin{pmatrix}
48 \\
4
\end{pmatrix}}{\begin{pmatrix}
52 \\
4
\end{pmatrix}} \\
P=0.26 && P'= 0.7187367 \\
&& P=1-P' \\
&& P=0.28
\end{align}
$$
---
10 broskví
2 nahnělé
2 berem
$$
P=\frac{8}{10}\cdot \frac{7}{9}=0.622
$$---

# Statistická definice pravděpodobnosti
[[Statistika]]
$$p(A) = \frac{\text{jev nastal}=\text{absolutní četnost}~n(A)}{\text{počet pokusů}=n}$$

| n    | n(A) | p(A) |
| ---- | ---- | ---- |
| 100  | 18   | .18  |
| 500  | 75   | .15  |
| 1000 | 170  | .17  |
| 2000 | 330  | .165 |
| 3000 | 512  | .171 |
| 4000 | 664  | .166 |
| 5000 | 831  | .166 |

---
